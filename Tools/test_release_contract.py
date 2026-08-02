#!/usr/bin/env python3
"""Source-level contract for the uploadable Court of Shadows 3.9.2 release."""

from __future__ import annotations

import ast
import json
import os
import re
import runpy
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GAME = ROOT / "game"
OLD_GAME = ROOT / "old-game"

APPROVED_VERSION = "3.9.2"
APPROVED_ANDROID_PACKAGE = "com.xiaoyiai.courtofshadows"
APPROVED_ANDROID_API = 36
MINIMUM_ANDROID_NUMERIC_VERSION = 1_785_596_475
EXPECTED_OLD_GAME_SCRIPT_COUNT = 56

APPROVED_ENDING_KEYS = (
    "iron_lord",
    "shadow_king",
    "holy_guardian",
    "peoples_lord",
    "truth",
    "borgia",
    "vassal",
    "fall",
    "sea",
)
APPROVED_CHINESE_STATS = ("权力", "财富", "信仰", "忠诚", "声望", "谋略")
APPROVED_ENGLISH_STATS = (
    "Power",
    "Wealth",
    "Faith",
    "Loyalty",
    "Reputation",
    "Intrigue",
)
APPROVED_SOUTHERN_OUTCOME_KEYS = ("free", "ruler", "fall", "outwit", "vassal")
STALE_RELEASE_PHRASES = (
    "v3.2",
    "v3.1",
    "版本：3.1",
    "即将登陆 TapTap · Steam",
    "New Game+ 二周目解锁新内容",
    "New Game+ unlocks additional content",
    "隐藏结局",
    "hidden ending",
)

FIVE_ENDING_CLAIM = re.compile(
    r"(?:五|5)\s*(?:个|种)?\s*"
    r"(?:独特|截然不同|完全不同(?:的)?|不同(?:的)?)?\s*结局|"
    r"\b(?:five|5)\s+(?:(?:distinct|unique|different|main|total)\s+)?endings\b",
    re.IGNORECASE,
)
ENGLISH_NG_PLUS_UNLOCKS_CONTENT = re.compile(
    r"\bNew Game\+\s+"
    r"(?:(?!\b(?:does\s+not|doesn't|will\s+not|won't|never)\b)[^.\n]){0,48}?"
    r"\bunlocks?\s+"
    r"(?:(?!\b(?:no|not|without)\b)[A-Za-z-]+\s+){0,5}content\b",
    re.IGNORECASE,
)
KNOWN_READ_ONLY_CONTAINER_CALLS = {
    "all",
    "any",
    "bool",
    "dict",
    "frozenset",
    "len",
    "list",
    "max",
    "min",
    "repr",
    "set",
    "sorted",
    "str",
    "sum",
    "tuple",
}


def read_text(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def executable_source(source: str) -> str:
    """Blank comments and string bodies while preserving source offsets."""
    result = list(source)
    index = 0
    quote = ""
    while index < len(source):
        if quote:
            if source.startswith(quote, index):
                for cursor in range(index, index + len(quote)):
                    result[cursor] = " "
                index += len(quote)
                quote = ""
            elif source[index] == "\\":
                result[index] = " "
                if index + 1 < len(source) and source[index + 1] != "\n":
                    result[index + 1] = " "
                index += 2
            else:
                if source[index] != "\n":
                    result[index] = " "
                index += 1
            continue

        if source[index] == "#":
            while index < len(source) and source[index] != "\n":
                result[index] = " "
                index += 1
            continue
        if source[index] in {'"', "'"}:
            quote = (
                source[index] * 3
                if source.startswith(source[index] * 3, index)
                else source[index]
            )
            for cursor in range(index, index + len(quote)):
                result[cursor] = " "
            index += len(quote)
            continue
        index += 1
    return "".join(result)


def executable_assignment_value(source: str, left_hand_side: str) -> str | None:
    """Return the value of the one executable assignment for a release field."""
    matches = list(re.finditer(
        rf"(?m)^{re.escape(left_hand_side)}\s*=",
        executable_source(source),
    ))
    if not matches:
        return None
    if len(matches) != 1:
        raise AssertionError(
            f"{left_hand_side} must have exactly one executable assignment"
        )
    match = matches[0]
    line_end = source.find("\n", match.end())
    if line_end < 0:
        line_end = len(source)
    return source[match.end() : line_end].strip()


def assigned_literal(source: str, name: str):
    """Return a Python literal assigned to *name* inside a Ren'Py source file."""
    code = executable_source(source)
    match = re.search(rf"(?m)^\s*{re.escape(name)}\s*=\s*", code)
    if match is None:
        raise AssertionError(f"assignment for {name!r} not found")

    index = match.end()
    while index < len(source) and source[index].isspace():
        index += 1
    if source.startswith("_p(", index):
        index += len("_p(")
        while index < len(source) and source[index].isspace():
            index += 1
    if index == len(source) or source[index] not in '([{"':
        raise AssertionError(f"assignment for {name!r} is not a supported literal")

    if source[index] in "([{":
        pairs = {"(": ")", "[": "]", "{": "}"}
        stack = [pairs[source[index]]]
        cursor = index + 1
        quote = ""
        escaped = False
        while cursor < len(source):
            char = source[cursor]
            if quote:
                if escaped:
                    escaped = False
                elif char == "\\":
                    escaped = True
                elif source.startswith(quote, cursor):
                    cursor += len(quote)
                    quote = ""
                    continue
            elif char in {'"', "'"}:
                quote = char * 3 if source.startswith(char * 3, cursor) else char
                cursor += len(quote)
                continue
            elif char in pairs:
                stack.append(pairs[char])
            elif char == stack[-1]:
                stack.pop()
                if not stack:
                    try:
                        return ast.literal_eval(source[index : cursor + 1])
                    except (SyntaxError, ValueError) as exc:
                        raise AssertionError(
                            f"assignment for {name!r} is not a closed literal"
                        ) from exc
            cursor += 1
        raise AssertionError(f"literal assigned to {name!r} is unterminated")

    quote = '"' * 3 if source.startswith('"' * 3, index) else '"'
    end = source.find(quote, index + len(quote))
    if end < 0:
        raise AssertionError(f"string assigned to {name!r} is unterminated")
    try:
        return ast.literal_eval(source[index : end + len(quote)])
    except (SyntaxError, ValueError) as exc:
        raise AssertionError(f"assignment for {name!r} is not a string literal") from exc


def python_function(source: str, name: str) -> ast.FunctionDef:
    """Parse one indented function from an ``init python`` Ren'Py block."""
    match = re.search(
        rf"(?ms)^    def {re.escape(name)}\(.*?(?=^    def |\Z)",
        source,
    )
    if match is None:
        raise AssertionError(f"function {name!r} not found")
    module = ast.parse(textwrap.dedent(match.group(0)))
    function = module.body[0]
    if not isinstance(function, ast.FunctionDef):
        raise AssertionError(f"{name!r} did not parse as a function")
    return function


def literal_dict_keys(dictionary: ast.Dict, subject: str) -> set[str]:
    keys: list[str] = []
    for key in dictionary.keys:
        if key is None:
            raise AssertionError(f"{subject} must not use dictionary unpacking")
        if not isinstance(key, ast.Constant) or not isinstance(key.value, str):
            raise AssertionError(f"{subject} contains a non-string key")
        keys.append(key.value)
    if len(keys) != len(set(keys)):
        raise AssertionError(f"{subject} contains a duplicate key")
    return set(keys)


def assigned_dict_keys(function: ast.FunctionDef, name: str) -> set[str]:
    for node in ast.walk(function):
        if not isinstance(node, ast.Assign) or not isinstance(node.value, ast.Dict):
            continue
        if any(isinstance(target, ast.Name) and target.id == name for target in node.targets):
            return literal_dict_keys(node.value, name)
    raise AssertionError(f"dictionary assignment for {name!r} not found")


def returned_dict_keys(function: ast.FunctionDef) -> set[str]:
    returns = [
        node.value
        for node in ast.walk(function)
        if isinstance(node, ast.Return) and isinstance(node.value, ast.Dict)
    ]
    if len(returns) != 1:
        raise AssertionError(f"expected one literal dictionary return, found {len(returns)}")
    return literal_dict_keys(returns[0], f"return value of {function.name}")


def init_python_tree_containing(source: str, marker: str) -> ast.Module:
    """Parse the indented ``init python`` block that contains *marker*."""
    lines = source.splitlines()
    for start, line in enumerate(lines):
        if line.strip() != "init python:" or line.startswith((" ", "\t")):
            continue
        body: list[str] = []
        for candidate in lines[start + 1 :]:
            if candidate and not candidate.startswith((" ", "\t")):
                break
            body.append(candidate)
        block = "\n".join(body)
        if marker in block:
            return ast.parse(textwrap.dedent(block))
    raise AssertionError(f"init python block containing {marker!r} not found")


def _named_assignment(tree: ast.AST, name: str) -> ast.Assign:
    assignments = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Assign)
        and any(isinstance(target, ast.Name) and target.id == name for target in node.targets)
    ]
    if len(assignments) != 1:
        raise AssertionError(f"expected one assignment to {name!r}, found {len(assignments)}")
    return assignments[0]


def _subscript_key_domain(
    key: ast.expr,
    dynamic_domains: dict[str, set[str]],
) -> set[str] | None:
    if isinstance(key, ast.Constant) and isinstance(key.value, str):
        return {key.value}
    if isinstance(key, ast.Name):
        return dynamic_domains.get(key.id)
    if (
        isinstance(key, ast.Subscript)
        and isinstance(key.value, ast.Subscript)
        and isinstance(key.value.value, ast.Name)
        and key.value.value.id == "ranked"
        and isinstance(key.slice, ast.Constant)
        and key.slice.value == 1
    ):
        return dynamic_domains.get("route_id")
    return None


def validate_container_does_not_escape(tree: ast.AST, name: str) -> None:
    """Reject aliases and calls that could mutate a guarded container off-tree."""
    for node in ast.walk(tree):
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            value = node.value
            if isinstance(value, ast.Name) and value.id == name:
                raise AssertionError(f"{name} escapes through an alias assignment")
        elif isinstance(node, ast.Call):
            direct_arguments = [*node.args, *(keyword.value for keyword in node.keywords)]
            if not any(
                isinstance(argument, ast.Name) and argument.id == name
                for argument in direct_arguments
            ):
                continue
            if (
                isinstance(node.func, ast.Name)
                and node.func.id in KNOWN_READ_ONLY_CONTAINER_CALLS
            ):
                continue
            raise AssertionError(f"{name} is passed to an unknown call")


def validate_mapping_mutations(
    tree: ast.AST,
    name: str,
    allowed_keys: set[str],
    dynamic_domains: dict[str, set[str]] | None = None,
) -> None:
    """Reject map growth that cannot be proven to target an existing key."""
    dynamic_domains = dynamic_domains or {}
    initial = _named_assignment(tree, name)
    if not isinstance(initial.value, ast.Dict):
        raise AssertionError(f"initial {name!r} assignment is not a dictionary")
    initial_keys = literal_dict_keys(initial.value, name)
    if not initial_keys <= allowed_keys:
        raise AssertionError(f"{name} initializes unknown keys: {initial_keys - allowed_keys}")

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == name and node is not initial:
                    raise AssertionError(f"{name} is reassigned after its literal definition")
                if not (
                    isinstance(target, ast.Subscript)
                    and isinstance(target.value, ast.Name)
                    and target.value.id == name
                ):
                    continue
                domain = _subscript_key_domain(target.slice, dynamic_domains)
                if domain is None:
                    raise AssertionError(f"{name} uses an unknown subscript assignment")
                if not domain <= allowed_keys:
                    raise AssertionError(f"{name} assigns unknown keys: {domain - allowed_keys}")
        elif isinstance(node, ast.AugAssign):
            target = node.target
            if (
                isinstance(target, ast.Name)
                and target.id == name
            ) or (
                isinstance(target, ast.Subscript)
                and isinstance(target.value, ast.Name)
                and target.value.id == name
            ):
                raise AssertionError(f"{name} uses an unchecked augmented update")
        elif isinstance(node, ast.Delete):
            for target in node.targets:
                if (
                    isinstance(target, ast.Name)
                    and target.id == name
                ) or (
                    isinstance(target, ast.Subscript)
                    and isinstance(target.value, ast.Name)
                    and target.value.id == name
                ):
                    raise AssertionError(f"{name} is deleted or loses a key")
        elif (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id == name
        ):
            if node.func.attr in {"setdefault", "pop", "popitem", "clear"}:
                raise AssertionError(f"{name}.{node.func.attr} is not an allowed value update")
            if node.func.attr != "update":
                continue
            if len(node.args) > 1:
                raise AssertionError(f"{name}.update has too many arguments")
            update_keys: set[str] = set()
            if node.args:
                if not isinstance(node.args[0], ast.Dict):
                    raise AssertionError(f"{name}.update uses an unknown mapping")
                update_keys.update(literal_dict_keys(node.args[0], f"{name}.update"))
            for keyword in node.keywords:
                if keyword.arg is None:
                    raise AssertionError(f"{name}.update uses dictionary unpacking")
                update_keys.add(keyword.arg)
            if not update_keys <= allowed_keys:
                raise AssertionError(f"{name}.update adds unknown keys: {update_keys - allowed_keys}")
    validate_container_does_not_escape(tree, name)


def validate_sequence_is_literal_only(tree: ast.AST, name: str) -> None:
    """Reject mutations that could make a literal catalog drift at runtime."""
    initial = _named_assignment(tree, name)
    if not isinstance(initial.value, (ast.List, ast.Tuple)):
        raise AssertionError(f"initial {name!r} assignment is not a sequence")
    mutators = {
        "append",
        "extend",
        "insert",
        "remove",
        "pop",
        "clear",
        "reverse",
        "sort",
    }
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == name and node is not initial:
                    raise AssertionError(f"{name} is reassigned after its literal definition")
                if (
                    isinstance(target, ast.Subscript)
                    and isinstance(target.value, ast.Name)
                    and target.value.id == name
                ):
                    raise AssertionError(f"{name} is changed through a subscript")
        elif isinstance(node, ast.AugAssign):
            target = node.target
            if (
                isinstance(target, ast.Name)
                and target.id == name
            ) or (
                isinstance(target, ast.Subscript)
                and isinstance(target.value, ast.Name)
                and target.value.id == name
            ):
                raise AssertionError(f"{name} uses an augmented update")
        elif isinstance(node, ast.Delete):
            for target in node.targets:
                if (
                    isinstance(target, ast.Name)
                    and target.id == name
                ) or (
                    isinstance(target, ast.Subscript)
                    and isinstance(target.value, ast.Name)
                    and target.value.id == name
                ):
                    raise AssertionError(f"{name} is deleted or loses an item")
        elif (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id == name
            and node.func.attr in mutators
        ):
            raise AssertionError(f"{name}.{node.func.attr} mutates the catalog")
    validate_container_does_not_escape(tree, name)


def renpy_screen(source: str, name: str) -> str:
    match = re.search(
        rf"(?ms)^screen {re.escape(name)}(?:\([^\n]*\))?:.*?"
        r"(?=^(?:screen|label|default|define|init|transform|style)\b|\Z)",
        source,
    )
    if match is None:
        raise AssertionError(f"screen {name!r} not found")
    return match.group(0)


def without_renpy_comments(source: str) -> str:
    return "\n".join(
        line for line in source.splitlines() if not line.lstrip().startswith("#")
    )


def assert_contains_all(
    case: unittest.TestCase,
    source: str,
    required: tuple[str, ...],
    subject: str,
) -> None:
    missing = [fragment for fragment in required if fragment not in source]
    case.assertEqual(missing, [], f"{subject} is missing approved facts: {missing}")


def assert_father_son_is_not_a_main_ending(source: str) -> None:
    block = renpy_label(source, "ending_father_son_epilogue")
    assert_no_main_ending_progress_mutation(block, "Father/Son epilogue")


def assert_southern_outcome_contract(source: str) -> None:
    ending_info = assigned_literal(source, "_southern_ending_info")
    keys = tuple(row[0] for row in ending_info)
    if keys != APPROVED_SOUTHERN_OUTCOME_KEYS:
        raise AssertionError(f"unexpected Southern outcome catalog: {keys}")
    finish = python_function(source, "southern_finish")
    finish_source = ast.unparse(finish)
    if not re.search(
        r"persistent\.southern_endings_seen\.add\(ending_key\)",
        finish_source,
    ):
        raise AssertionError("Southern outcomes must use their own persistence set")
    if re.search(
        r"persistent\.endings_seen(?:\.(?:add|update)|\s*=)",
        finish_source,
    ):
        raise AssertionError("Southern outcomes must not write main ending progress")
    if "store.southern_outcome = ending_key" not in finish_source:
        raise AssertionError("Southern outcomes must expose the current-run outcome")
    assert_no_main_ending_progress_mutation(
        source,
        "Southern expansion",
    )


def renpy_label(source: str, name: str) -> str:
    match = re.search(
        rf"(?ms)^label {re.escape(name)}:.*?(?=^label |\Z)",
        source,
    )
    if match is None:
        raise AssertionError(f"label {name!r} not found")
    return match.group(0)


def assert_no_main_ending_progress_mutation(source: str, subject: str) -> None:
    code = executable_source(source)
    reference = re.search(
        r"""\b(?:persistent\.)?endings_seen\b|"""
        r"""\b(?:record|unlock|mark|complete)_ending\b""",
        code,
    )
    if reference is not None:
        raise AssertionError(
            f"{subject} must not reference main ending progress: {reference.group(0)}"
        )


def assert_no_stale_release_phrases(source: str) -> None:
    for phrase in STALE_RELEASE_PHRASES:
        if phrase.casefold() in source.casefold():
            raise AssertionError(f"stale release phrase remains: {phrase}")


class VersionAndAndroidContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.options = read_text("game/options.rpy")
        cls.android = json.loads(read_text("android.json"))

    def test_config_and_android_versions_match_392(self) -> None:
        config_version = executable_assignment_value(
            self.options, "define config.version"
        )
        self.assertIsNotNone(config_version)
        self.assertEqual(config_version, f'"{APPROVED_VERSION}"')
        self.assertEqual(self.android["version"], APPROVED_VERSION)

    def test_version_and_android_contract_reject_multiline_string_decoys(self) -> None:
        fixture = (
            'reference = """\n'
            'define config.version = "3.9.2"\n'
            '    build.android_package = "com.xiaoyiai.courtofshadows"\n'
            '    build.android_target_api = 36\n'
            '"""\n'
            'define config.version = "3.9.2"\n'
            '    build.android_package = "com.xiaoyiai.courtofshadows"\n'
            '    build.android_target_api = 36\n'
            'define config.version = "0.0.0"\n'
            '    build.android_package = "example.wrong"\n'
            '    build.android_target_api = 1\n'
        )
        original_options = self.options
        self.options = fixture
        try:
            with self.assertRaises(AssertionError):
                self.test_config_and_android_versions_match_392()
            with self.assertRaises(AssertionError):
                self.test_android_package_and_api_agree_with_build_source()
        finally:
            self.options = original_options

    def test_android_package_and_api_agree_with_build_source(self) -> None:
        source_package = executable_assignment_value(
            self.options, "    build.android_package"
        )
        source_api = executable_assignment_value(
            self.options, "    build.android_target_api"
        )
        self.assertIsNotNone(source_package)
        self.assertIsNotNone(source_api)
        self.assertEqual(source_package, f'"{APPROVED_ANDROID_PACKAGE}"')
        self.assertEqual(self.android["package"], APPROVED_ANDROID_PACKAGE)
        self.assertEqual(int(source_api), APPROVED_ANDROID_API)
        self.assertEqual(self.android["target_version"], APPROVED_ANDROID_API)
        self.assertEqual(self.android["orientation"], "sensorLandscape")
        self.assertIn("define build.android_landscape = True", self.options)

    def test_android_numeric_version_meets_verified_floor(self) -> None:
        self.assertGreaterEqual(
            self.android["numeric_version"], MINIMUM_ANDROID_NUMERIC_VERSION
        )


class EndingCatalogContractTests(unittest.TestCase):
    def test_catalog_and_three_source_maps_use_exactly_nine_endings(self) -> None:
        effects = read_text("game/effects.rpy")
        difficulty = read_text("game/difficulty.rpy")
        approved = set(APPROVED_ENDING_KEYS)

        catalog = assigned_literal(effects, "_ending_keys")
        info_keys = set(assigned_literal(effects, "_ending_info"))
        effects_tree = init_python_tree_containing(effects, "_ending_info")
        route_function = python_function(difficulty, "get_finale_route_availability")
        route_keys = assigned_dict_keys(route_function, "routes")
        ranked = _named_assignment(route_function, "ranked").value
        if not isinstance(ranked, ast.List):
            raise AssertionError("ranked ending routes must be a literal list")
        ranked_route_keys = {
            item.elts[1].value
            for item in ranked.elts
            if isinstance(item, ast.Tuple)
            and len(item.elts) == 2
            and isinstance(item.elts[1], ast.Constant)
            and isinstance(item.elts[1].value, str)
        }
        self.assertEqual(len(ranked_route_keys), len(ranked.elts))
        self.assertTrue(ranked_route_keys <= approved)
        ending_function = python_function(difficulty, "get_finale_ending_availability")
        availability_keys = returned_dict_keys(ending_function)

        self.assertEqual(tuple(catalog), APPROVED_ENDING_KEYS)
        self.assertEqual(info_keys, approved)
        self.assertEqual(route_keys - {"resist"}, approved)
        self.assertEqual(route_keys - approved, {"resist"})
        self.assertEqual(availability_keys, approved)
        validate_mapping_mutations(effects_tree, "_ending_info", approved)
        validate_sequence_is_literal_only(effects_tree, "_ending_keys")
        validate_mapping_mutations(
            route_function,
            "routes",
            approved | {"resist"},
            dynamic_domains={"route_id": ranked_route_keys},
        )

    def test_father_son_hidden_epilogue_stays_outside_main_ending_progress(self) -> None:
        chapter_five = read_text("game/chapter5.rpy")
        expansion = read_text("game/endings_expansion.rpy")
        self.assertIn("label ending_father_son_epilogue:", expansion)
        self.assertIn("jump ending_father_son_epilogue", expansion)
        assert_father_son_is_not_a_main_ending(chapter_five + expansion)

    def test_southern_outcomes_use_a_separate_five_key_catalog_and_progress_set(self) -> None:
        southern = read_text("game/southern_expansion.rpy")
        assert_southern_outcome_contract(southern)


class EndingCatalogGuardTests(unittest.TestCase):
    def test_literal_reader_ignores_assignments_inside_multiline_strings(self) -> None:
        source = (
            'reference = """legacy catalog:\n'
            'target = ["stale"]\n'
            '"""\n'
            'target = ["approved"]\n'
        )
        self.assertEqual(assigned_literal(source, "target"), ["approved"])

    def test_father_son_guard_rejects_record_ending_registration(self) -> None:
        with self.assertRaises(AssertionError):
            assert_father_son_is_not_a_main_ending(
                'label ending_father_son_epilogue:\n'
                '    $ seen = persistent.endings_seen\n'
                '    $ seen.add("father_son")\n'
            )

    def test_southern_outcome_guard_rejects_main_ending_progress_write(self) -> None:
        source = (
            "init python:\n"
            "    def southern_finish(ending_key, achievement):\n"
            "        persistent.southern_endings_seen.add(ending_key)\n"
            "        store.southern_outcome = ending_key\n"
            "    _southern_ending_info = [\n"
            '        ("free", "", "", "", ""), ("ruler", "", "", "", ""),\n'
            '        ("fall", "", "", "", ""), ("outwit", "", "", "", ""),\n'
            '        ("vassal", "", "", "", ""),\n'
            "    ]\n"
            "    def unrelated_southern_code():\n"
            "        seen = persistent.endings_seen\n"
            "        seen.add('free')\n"
        )
        with self.assertRaises(AssertionError):
            assert_southern_outcome_contract(source)

    def test_literal_map_keys_reject_non_strings_and_unpacking(self) -> None:
        for expression in ('{"iron_lord": False, 1: False}', '{"iron_lord": False, **extra}'):
            dictionary = ast.parse(expression, mode="eval").body
            self.assertIsInstance(dictionary, ast.Dict)
            with self.subTest(expression=expression):
                with self.assertRaises(AssertionError):
                    literal_dict_keys(dictionary, "fixture")

    def test_map_mutations_reject_unknown_subscripts_and_updates(self) -> None:
        fixtures = (
            "routes = {'iron_lord': False}\nroutes[unknown] = True",
            "routes = {'iron_lord': False}\nroutes['tenth'] = True",
            "routes = {'iron_lord': False}\nroutes.update(extra)",
            "routes = {'iron_lord': False}\nroutes.update({'tenth': True})",
            "routes = {'iron_lord': False}\nroutes.setdefault('iron_lord', True)",
            "routes = {'iron_lord': False}\nroutes.pop('iron_lord')",
            "routes = {'iron_lord': False}\nroutes.popitem()",
            "routes = {'iron_lord': False}\nroutes.clear()",
            "routes = {'iron_lord': False}\ndel routes['iron_lord']",
            "routes = {'iron_lord': False}\ndel routes",
            "routes = {'iron_lord': False}\nalias = routes",
            "routes = {'iron_lord': False}\nconsume(routes)",
        )
        for source in fixtures:
            with self.subTest(source=source):
                with self.assertRaises(AssertionError):
                    validate_mapping_mutations(
                        ast.parse(source),
                        "routes",
                        {"iron_lord", "resist"},
                    )

    def test_map_mutations_allow_value_changes_for_existing_keys(self) -> None:
        tree = ast.parse(
            "routes = {'iron_lord': False, 'resist': False}\n"
            "routes['iron_lord'] = True\n"
            "routes['resist'] = True\n"
            "routes.update({'iron_lord': False})\n"
            "routes.get('iron_lord')\n"
            "len(routes)"
        )
        validate_mapping_mutations(tree, "routes", {"iron_lord", "resist"})

    def test_catalog_guard_rejects_reordering_and_deletion(self) -> None:
        fixtures = (
            "_ending_keys = ['iron_lord']\n_ending_keys.reverse()",
            "_ending_keys = ['iron_lord']\n_ending_keys.sort()",
            "_ending_keys = ['iron_lord']\ndel _ending_keys[0]",
            "_ending_keys = ['iron_lord']\ndel _ending_keys",
            "_ending_keys = ['iron_lord']\nalias = _ending_keys",
            "_ending_keys = ['iron_lord']\nconsume(_ending_keys)",
            "_ending_keys = ['iron_lord']\n_ending_keys[0] += '_changed'",
        )
        for source in fixtures:
            with self.subTest(source=source):
                with self.assertRaises(AssertionError):
                    validate_sequence_is_literal_only(ast.parse(source), "_ending_keys")

        validate_sequence_is_literal_only(
            ast.parse("_ending_keys = ['iron_lord']\nlen(_ending_keys)"),
            "_ending_keys",
        )


class ReleaseCopyGuardTests(unittest.TestCase):
    def test_five_ending_claim_variants_are_detected(self) -> None:
        for claim in (
            "五个结局",
            "五种结局",
            "五结局",
            "5结局",
            "five endings",
            "5 endings",
            "5 unique endings",
        ):
            with self.subTest(claim=claim):
                self.assertRegex(claim, FIVE_ENDING_CLAIM)

    def test_english_ng_plus_new_content_variants_are_detected(self) -> None:
        for claim in (
            "New Game+ unlocks new content",
            "New Game+ unlocks additional story content",
            "New Game+ mode unlocks brand-new bonus story content",
            "New Game+ will unlock extra narrative content",
        ):
            with self.subTest(claim=claim):
                self.assertRegex(claim, ENGLISH_NG_PLUS_UNLOCKS_CONTENT)

        for denial in (
            "New Game+ does not unlock separate story content",
            "New Game+ will not unlock additional content",
            "New Game+ unlocks no additional story content",
        ):
            with self.subTest(denial=denial):
                self.assertNotRegex(denial, ENGLISH_NG_PLUS_UNLOCKS_CONTENT)

    def test_bare_v31_is_a_stale_release_phrase(self) -> None:
        with self.assertRaises(AssertionError):
            assert_no_stale_release_phrases("Current release: v3.1")


class PlayerFacingCopyContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        options = read_text("game/options.rpy")
        effects = read_text("game/effects.rpy")
        cls.about = assigned_literal(options, "define gui.about")
        cls.privacy = renpy_screen(effects, "privacy_policy_screen")
        cls.rating = renpy_screen(effects, "rating_popup")
        cls.pv = without_renpy_comments(read_text("game/pv.rpy"))
        cls.readme = read_text("README.txt")
        cls.description = read_text("DESCRIPTION.txt")
        cls.developer_note = read_text("DEVELOPER_NOTE.txt")
        cls.store = read_text("store_assets/taptap_description.txt")
        cls.current_copy = {
            "About": cls.about,
            "Privacy": cls.privacy,
            "Rating": cls.rating,
            "PV": cls.pv,
            "README": cls.readme,
            "Description": cls.description,
            "Developer note": cls.developer_note,
            "Store listing": cls.store,
        }

    def test_about_states_the_approved_release_facts(self) -> None:
        assert_contains_all(
            self,
            self.about,
            ("艾登堡", "继承", "领主", "父亲", "五章", "九个主线结局", "隐藏尾声"),
            "About",
        )
        self.assertRegex(
            self.about,
            re.compile(r"(?:死因|死亡|遇害|骤逝).{0,24}(?:疑案|疑云|真相|谜)", re.DOTALL),
        )
        self.assertIn("v3.9.2", self.about)

    def test_privacy_copy_matches_the_current_build(self) -> None:
        self.assertIn("版本：3.9.2", self.privacy)
        self.assertIn("更新日期：2026年8月", self.privacy)

    def test_rating_copy_is_platform_neutral_and_close_only(self) -> None:
        for platform_name in (
            "TapTap",
            "Steam",
            "好游快爆",
            "Google Play",
            "GooglePlay",
            "App Store",
        ):
            self.assertNotIn(platform_name.casefold(), self.rating.casefold())

        labels = re.findall(r'(?m)^\s*textbutton "([^"]+)":', self.rating)
        actions = re.findall(r"(?m)^\s*action\s+(.+)$", self.rating)
        self.assertTrue(labels)
        self.assertEqual(len(actions), len(labels))
        for label in labels:
            self.assertNotRegex(label, r"(?:去|前往|打开|跳转|留下).*(?:评分|评价|商店)")
        for action in actions:
            self.assertIn('Hide("rating_popup")', action)
            self.assertNotRegex(action, r"\b(?:OpenURL|Jump|Call|Show)\s*\(")

    def test_pv_is_a_partial_preview_with_factual_platforms(self) -> None:
        self.assertIn("部分结局预览", self.pv)
        self.assertRegex(self.pv, r"九条路\W+九种代价")
        self.assertIn("PC · Android", self.pv)
        self.assertNotIn("即将登陆 TapTap · Steam", self.pv)

    def test_readme_is_for_windows_players_and_describes_the_current_game(self) -> None:
        assert_contains_all(
            self,
            self.readme,
            ("Windows", "CourtOfShadows.exe", "五章", "九个主线结局", "隐藏尾声"),
            "README",
        )
        for internal_phrase in ("下载 Ren'Py SDK", "项目结构", "后续开发计划"):
            self.assertNotIn(internal_phrase, self.readme)

    def test_chinese_release_descriptions_use_the_real_catalog_and_values(self) -> None:
        for subject, source in (
            ("Description", self.description),
            ("Developer note", self.developer_note),
        ):
            with self.subTest(subject=subject):
                assert_contains_all(
                    self,
                    source,
                    ("九个主线结局", "隐藏尾声", *APPROVED_CHINESE_STATS),
                    subject,
                )

        chinese_store = self.store.split("Steam Store Description", 1)[0]
        assert_contains_all(
            self,
            chinese_store,
            (
                "五章",
                "九个主线结局",
                "隐藏尾声",
                "南境",
                "五个独立结果",
                *APPROVED_CHINESE_STATS,
            ),
            "Chinese store listing",
        )

    def test_english_store_copy_uses_the_same_approved_facts(self) -> None:
        english_store = self.store.split("Steam Store Description", 1)[-1]
        for pattern in (
            r"\bfive\b.*\bchapters\b",
            r"\bnine\b.*\bmain endings\b",
            r"\bhidden epilogue\b",
            r"\bSouthern\b.*\bfive separate outcomes\b",
        ):
            self.assertRegex(english_store, re.compile(pattern, re.IGNORECASE))
        for stat in APPROVED_ENGLISH_STATS:
            self.assertRegex(english_store, rf"(?i)\b{stat}\b")

    def test_current_copy_contains_no_stale_release_claims(self) -> None:
        rewrite_history = re.compile(
            r"每(?:一)?个选择都将改写历史|"
            r"\bevery (?:choice|decision) (?:will )?"
            r"(?:change|changes|rewrite|rewrites|shape|shapes) history\b",
            re.IGNORECASE,
        )
        for subject, source in self.current_copy.items():
            with self.subTest(subject=subject):
                assert_no_stale_release_phrases(source)
                self.assertNotRegex(source, rewrite_history)
                for line in source.splitlines():
                    if not FIVE_ENDING_CLAIM.search(line):
                        continue
                    partial_preview = (
                        "部分" in line and "预览" in line
                    ) or "partial preview" in line.casefold()
                    self.assertTrue(
                        partial_preview,
                        f"{subject} still claims five total endings: {line.strip()}",
                    )

    def test_current_copy_contains_no_numeric_playtime_promise(self) -> None:
        playtime = re.compile(
            r"(?<!\d)\d+\s*(?:[-–—~至到]\s*\d+\s*)?(?:小时|hours?\b)",
            re.IGNORECASE,
        )
        violations = {
            subject: match.group(0)
            for subject, source in self.current_copy.items()
            if (match := playtime.search(source)) is not None
        }
        self.assertEqual(violations, {})


class TrailerPathContractTests(unittest.TestCase):
    def test_default_trailer_paths_stay_in_checkout_from_any_cwd(self) -> None:
        script = ROOT / "Tools" / "make_trailer.py"
        original_cwd = Path.cwd()

        with tempfile.TemporaryDirectory() as unrelated_cwd:
            try:
                os.chdir(unrelated_cwd)
                trailer = runpy.run_path(
                    str(script), run_name="trailer_path_contract_probe"
                )
            finally:
                os.chdir(original_cwd)

        self.assertEqual(Path(trailer["PROJ"]).resolve(), ROOT)
        self.assertEqual(
            Path(trailer["OUT"]).resolve(),
            ROOT / "store_assets" / "trailer_v392.mp4",
        )


class NewGamePlusContractTests(unittest.TestCase):
    def test_implementation_inherits_twenty_percent_of_exactly_three_values(self) -> None:
        extras = read_text("game/extras.rpy")
        assignments = {
            (bonus, source, factor)
            for bonus, source, factor in re.findall(
                r"persistent\.ng_plus_bonus_(\w+)\s*=\s*"
                r"int\(store\.(\w+)\s*\*\s*(0\.\d+)\)",
                extras,
            )
        }
        self.assertEqual(
            assignments,
            {
                ("power", "power", "0.2"),
                ("wealth", "wealth", "0.2"),
                ("intrigue", "intrigue", "0.2"),
            },
        )

    def test_current_ng_plus_copy_names_inherited_values_not_new_story(self) -> None:
        sources = {
            "Description": read_text("DESCRIPTION.txt"),
            "Developer note": read_text("DEVELOPER_NOTE.txt"),
            "Chinese store listing": read_text("store_assets/taptap_description.txt").split(
                "Steam Store Description", 1
            )[0],
        }
        for subject, source in sources.items():
            with self.subTest(subject=subject):
                assert_contains_all(
                    self,
                    source,
                    ("20%", "权力", "财富", "谋略"),
                    f"{subject} New Game+ copy",
                )
                self.assertNotRegex(source, r"(?:解锁|开放)(?:独立的?)?(?:新)?(?:剧情|故事)?内容")

        english_store = read_text("store_assets/taptap_description.txt").split(
            "Steam Store Description", 1
        )[-1]
        assert_contains_all(
            self,
            english_store,
            ("20%", "Power", "Wealth", "Intrigue"),
            "English store New Game+ copy",
        )
        self.assertNotRegex(
            english_store,
            ENGLISH_NG_PLUS_UNLOCKS_CONTENT,
        )


class OldGameSourceContractTests(unittest.TestCase):
    def test_old_game_contains_the_exact_56_current_script_rpycs(self) -> None:
        expected = {
            source.relative_to(GAME).with_suffix(".rpyc")
            for source in GAME.rglob("*.rpy")
        }
        actual = {
            compiled.relative_to(OLD_GAME)
            for compiled in OLD_GAME.rglob("*.rpyc")
        }
        self.assertEqual(len(expected), EXPECTED_OLD_GAME_SCRIPT_COUNT)
        self.assertEqual(actual, expected)

    def test_required_old_save_node_guard_still_passes(self) -> None:
        result = subprocess.run(
            [sys.executable, "-m", "Tools.test_old_game_compat"],
            cwd=ROOT,
            text=True,
            encoding="utf-8",
            errors="replace",
            capture_output=True,
            check=False,
        )
        output = "\n".join(part for part in (result.stdout, result.stderr) if part)
        self.assertEqual(result.returncode, 0, output)
        self.assertIn("Ran 6 tests", output)
        self.assertIn("OK", output)


if __name__ == "__main__":
    unittest.main()

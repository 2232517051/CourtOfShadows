#!/usr/bin/env python3
"""Source-level contract for the uploadable Court of Shadows 3.9.2 release."""

from __future__ import annotations

import ast
import functools
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
APPROVED_PACKAGE_EXCLUSIONS = (
    "game/test_game.rpyc",
    "game/audio/music/*_alt.mp3",
    "game/audio/music/test3.wav",
    "game/audio/narration/test_guy.mp3",
    "game/audio/narration/voice_test/**",
    "game/images/hd/**",
    "game/images/backup_sd/**",
    "game/images/webp_backup/**",
    "store_assets/**",
    "tests/**",
    "docs/**",
    "Tools/**",
    "_speaker_report.txt",
    "_ui_wiring_review.png",
    "all_chars.txt",
    "bgm_suno_progress.json",
    "CANON.md",
    "CHANGELOG.txt",
    "CHANGELOG_v3.0.md",
    "CLAUDE.md",
    "combat_ui_mockup.png",
    "cover_horizontal.png",
    "cover_vertical.png",
    "crisis_check_proposal.md",
    "DESCRIPTION.txt",
    "DEVELOPER_NOTE.txt",
    "first_meet_report.txt",
    "FORBIDDEN_PHRASES.md",
    "game_icon_256.jpg",
    "game_icon_256.png",
    "logo.png",
    "logo_gold.png",
    "long_dialogue.txt",
    "missing_portraits_A.txt",
    "missing_portraits_B.txt",
    "missing_portraits_full.json",
    "promo_horizontal.png",
    "promo_vertical.png",
    "sfx_elevenlabs_progress.json",
    "STYLE.md",
    "taptap_promo.png",
    "TapTap_v3.5.1_hotfix.md",
    "TapTap_v3.5_更新公告.md",
    "TapTap_v3.6_更新公告.md",
    "TapTap_v3.7_更新公告.md",
    "TapTap_v3.8_更新公告.md",
    "TapTap_v3.9_更新公告.md",
    "TapTap_回归声明.md",
    "ui_icons_progress.json",
    "voice_mapping.json",
    "wallpaper_library.png",
    "事件时间线审计报告.md",
)
# Protected by the 2026-07-31 release audit. These paths were present in the
# prior APK but have no reliable direct .rpy filename references.
PROTECTED_DYNAMIC_UI_PATHS = (
    "game/images/ui/panel_frame.png",
    "game/images/ui/box_confirm.png",
    "game/images/ui/lock_slot_square.png",
    "game/images/ui/box_slot.png",
    "game/images/ui/lock_slot_wide.png",
    "game/images/ui/box_choice.png",
    "game/images/ui/card_slot.png",
    "game/images/ui/box_namebox.png",
    "game/images/ui/progress_track.png",
    "game/images/ui/box_choice_hover.png",
    "game/images/ui/box_textbox.png",
    "game/images/ui/divider_gold.png",
    "game/images/ui/progress_fill.png",
    "game/images/ui/ctl_check_on.png",
    "game/images/ui/ctl_radio_on.png",
    "game/images/ui/ico_harp.png",
    "game/images/ui/ctl_radio_off.png",
    "game/images/ui/ctl_check_off.png",
    "game/images/ui/box_notify.png",
    "game/images/ui/ui_gallery.png",
    "game/images/ui/ctl_scroll_thumb.png",
    "game/images/ui/ctl_scroll_track.png",
)
PROTECTED_ANDROID_BUILD_INPUTS = (
    "android-icon.png",
    "android-icon_background.png",
    "android-icon_foreground.png",
    "android-presplash.png",
)
# Ren'Py 8.5.2 early base rules relevant to source-input protection. The
# built-in old-game rule omits compatibility bytecode from archives; it does
# not authorize a project rule that hides the compiler inputs themselves.
RENPY_EARLY_INPUT_RULES = (
    ("old-game/", None),
    ("android-*.png", "android"),
    ("android-*.jpg", "android"),
)
ALLOWED_INIT_BUILD_FIELDS = {
    "android_package",
    "android_permissions",
    "android_target_api",
    "ios_bundle_identifier",
    "ios_bundle_name",
    "executable_name",
    "mac_architectures",
    "google_play_key",
    "google_play_salt",
}
ALLOWED_DEFINE_BUILD_FIELDS = {"name", "android_landscape", "ios_landscape"}
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


def _init_python_blocks(source: str) -> list[tuple[int, int, ast.Module]]:
    """Return real top-level init-python bodies without interpreting Ren'Py."""
    blocks: list[tuple[int, int, ast.Module]] = []
    lines = source.splitlines()
    executable_lines = executable_source(source).splitlines()
    if len(executable_lines) != len(lines):
        raise AssertionError("executable-source masking changed the line count")
    init_python = re.compile(r"^init(?:\s+-?\d+)?\s+python(?:\s+in\s+\w+)?:\s*$")

    for start, line in enumerate(executable_lines):
        if line.startswith((" ", "\t")):
            continue
        if re.match(r"^init\s+offset\s*=", line):
            raise AssertionError("init offset is forbidden in build configuration")
        if init_python.fullmatch(line) is None:
            continue
        if line != "init python:":
            raise AssertionError("build configuration must use exact 'init python:'")
        body: list[str] = []
        end = start + 1
        for original, candidate in zip(
            lines[start + 1 :], executable_lines[start + 1 :]
        ):
            if candidate.strip() and not candidate.startswith((" ", "\t")):
                break
            body.append(original)
            end += 1
        if not body:
            continue
        wrapper = ast.parse("if True:\n" + "\n".join(body)).body[0]
        if not isinstance(wrapper, ast.If):
            raise AssertionError("init-python wrapper did not parse as a suite")
        blocks.append((start, end, ast.Module(body=wrapper.body, type_ignores=[])))
    return blocks


def _is_build_contract_attribute(node: ast.AST) -> bool:
    return (
        isinstance(node, ast.Attribute)
        and isinstance(node.value, ast.Name)
        and node.value.id == "build"
        and node.attr in {"classify", "documentation"}
    )


def _literal_build_call(call: ast.Call) -> tuple[str, tuple[object, ...]]:
    if not _is_build_contract_attribute(call.func):
        raise AssertionError("only direct build.classify/documentation calls are allowed")
    name = call.func.attr
    if call.keywords:
        raise AssertionError("active build calls must not use keyword arguments")
    try:
        arguments = tuple(ast.literal_eval(argument) for argument in call.args)
    except (ValueError, TypeError) as exc:
        raise AssertionError("active build calls must use literal arguments") from exc

    if name == "classify":
        valid = (
            len(arguments) == 2
            and isinstance(arguments[0], str)
            and (arguments[1] is None or isinstance(arguments[1], str))
        )
    else:
        valid = len(arguments) == 1 and isinstance(arguments[0], str)
    if not valid:
        raise AssertionError(f"unsupported active build.{name} call: {arguments!r}")
    return name, arguments


def active_literal_build_calls(source: str) -> list[tuple[str, tuple[object, ...]]]:
    """Validate the strict options grammar and return its ordered build calls."""
    blocks = _init_python_blocks(source)
    if len(blocks) != 1:
        raise AssertionError("options must contain exactly one real init-python block")
    outside_violations = options_build_contract_scope_violations(source)
    if outside_violations:
        raise AssertionError("; ".join(outside_violations))

    _, _, tree = blocks[0]
    calls: list[tuple[str, tuple[object, ...]]] = []
    assigned_fields: set[str] = set()
    for statement in tree.body:
        if isinstance(statement, ast.Expr) and isinstance(statement.value, ast.Call):
            calls.append(_literal_build_call(statement.value))
            continue
        if not isinstance(statement, ast.Assign) or len(statement.targets) != 1:
            raise AssertionError("init-python build statements must be top-level calls or assignments")
        target = statement.targets[0]
        if not (
            isinstance(target, ast.Attribute)
            and isinstance(target.value, ast.Name)
            and target.value.id == "build"
            and target.attr in ALLOWED_INIT_BUILD_FIELDS
        ):
            raise AssertionError("unsupported init-python build assignment target")
        if target.attr in assigned_fields:
            raise AssertionError(f"duplicate build.{target.attr} assignment")
        try:
            ast.literal_eval(statement.value)
        except (ValueError, TypeError) as exc:
            raise AssertionError(f"build.{target.attr} must use a literal value") from exc
        assigned_fields.add(target.attr)
    return calls


_GLOBAL_BUILD_NAME = re.compile(r"(?<![\w.])build\b")
_RENPY_STORE_BUILD = re.compile(
    r"\b(?:renpy\s*\.\s*)?store\s*\.\s*build\b"
)
_DYNAMIC_CALL = re.compile(
    r"\b(?:getattr|setattr|delattr|globals|locals|vars|exec|eval|__import__)\s*\("
)
_BUILD_WORD = re.compile(r"\bbuild\b")
_STORE_ALIAS_IMPORT = re.compile(
    r"(?m)^[ \t]*(?:import[ \t]+renpy\s*\.\s*store|"
    r"from[ \t]+renpy[ \t]+import[ \t]+store)[ \t]+as[ \t]+([A-Za-z_]\w*)\b"
)


def _balanced_call_source(source: str, masked: str, start: int) -> str:
    opening = masked.find("(", start)
    depth = 0
    for index in range(opening, len(masked)):
        if masked[index] == "(":
            depth += 1
        elif masked[index] == ")":
            depth -= 1
            if depth == 0:
                return source[start : index + 1]
    return source[start : start + 512]


def _build_reference_lines(source: str) -> list[int]:
    """Find executable references to Ren'Py's global build object."""
    masked = executable_source(source)
    reference_patterns = [_GLOBAL_BUILD_NAME, _RENPY_STORE_BUILD]
    reference_patterns.extend(
        re.compile(rf"\b{re.escape(match.group(1))}\s*\.\s*build\b")
        for match in _STORE_ALIAS_IMPORT.finditer(masked)
    )
    lines = {
        masked.count("\n", 0, match.start()) + 1
        for pattern in reference_patterns
        for match in pattern.finditer(masked)
    }
    for match in _DYNAMIC_CALL.finditer(masked):
        line_end = source.find("\n", match.start())
        one_line = source[match.start() : line_end if line_end >= 0 else len(source)]
        candidates = (one_line, _balanced_call_source(source, masked, match.start()))
        for candidate in candidates:
            try:
                tree = ast.parse(candidate.strip(), mode="eval")
            except SyntaxError:
                continue
            if any(
                isinstance(node, ast.Constant)
                and isinstance(node.value, str)
                and _BUILD_WORD.search(node.value)
                for node in ast.walk(tree)
            ):
                lines.add(masked.count("\n", 0, match.start()) + 1)
                break
    return sorted(lines)


def external_build_contract_violations(
    sources: dict[str, str],
) -> dict[str, str]:
    """Return global Ren'Py build references outside game/options.rpy."""
    violations: dict[str, str] = {}
    for path, source in sources.items():
        if path.replace("\\", "/") == "game/options.rpy":
            continue
        lines = _build_reference_lines(source)
        if lines:
            violations[path] = f"Ren'Py build reference on line {lines[0]}"
    return violations


def options_build_contract_scope_violations(source: str) -> list[str]:
    """Validate build syntax outside the one strict init-python block."""
    try:
        blocks = _init_python_blocks(source)
    except (AssertionError, SyntaxError) as exc:
        return [str(exc)]
    if len(blocks) != 1:
        return ["options must contain exactly one real init-python block"]
    start, end, _ = blocks[0]
    lines = source.splitlines()
    masked_lines = executable_source(source).splitlines()
    scan_lines = list(lines)
    violations: list[str] = []
    defined_fields: set[str] = set()
    define_build = re.compile(r"^define\s+build\.([A-Za-z_]\w*)\s*=")
    for index, (line, masked_line) in enumerate(zip(lines, masked_lines)):
        if start <= index < end:
            scan_lines[index] = ""
            continue
        match = define_build.match(masked_line)
        if match is None:
            continue
        field = match.group(1)
        scan_lines[index] = ""
        if field not in ALLOWED_DEFINE_BUILD_FIELDS:
            violations.append(f"line {index + 1}: unsupported define build.{field}")
            continue
        if field in defined_fields:
            violations.append(f"line {index + 1}: duplicate define build.{field}")
            continue
        try:
            ast.literal_eval(line.split("=", 1)[1].strip())
        except (SyntaxError, ValueError, TypeError):
            violations.append(f"line {index + 1}: define build.{field} must be literal")
            continue
        defined_fields.add(field)
    violations.extend(
        f"line {line}: build is only allowed in the strict options block"
        for line in _build_reference_lines("\n".join(scan_lines))
    )
    return violations


def literal_classification_rules(
    calls: list[tuple[str, tuple[object, ...]]],
) -> list[tuple[str, str | None]]:
    """Return direct literal classify rules with supported Ren'Py targets."""
    rules: list[tuple[str, str | None]] = []
    for name, arguments in calls:
        if (
            name != "classify"
            or len(arguments) != 2
            or not isinstance(arguments[0], str)
            or (arguments[1] is not None and not isinstance(arguments[1], str))
        ):
            continue
        rules.append((arguments[0], arguments[1]))
    return rules


def renpy_pattern_matches(path: str, pattern: str) -> bool:
    """Match one Ren'Py build pattern using the launcher's glob semantics."""
    regex = ""
    cursor = 0
    while cursor < len(pattern):
        if pattern.startswith("**", cursor):
            regex += ".*"
            cursor += 2
        elif pattern[cursor] == "*":
            regex += "[^/]*/?"
            cursor += 1
        elif pattern[cursor] == "[":
            end = pattern.find("]", cursor + 1)
            if end < 0:
                regex += re.escape(pattern[cursor])
                cursor += 1
            else:
                regex += pattern[cursor : end + 1]
                cursor = end + 1
        else:
            regex += re.escape(pattern[cursor])
            cursor += 1
    compiled = re.compile(regex + "$", re.IGNORECASE)
    return compiled.match(path) is not None or compiled.match("/" + path) is not None


def first_literal_classification(
    rules: list[tuple[str, str | None]], path: str
) -> tuple[str, str | None]:
    """Classify a file while modeling ancestor-directory traversal and pruning."""
    parts = path.strip("/").split("/")
    for length in range(1, len(parts)):
        directory = "/".join(parts[:length]) + "/"
        classification = _first_literal_rule_for_entry(rules, directory, is_dir=True)
        if classification is not None and classification[1] is None:
            return classification

    classification = _first_literal_rule_for_entry(rules, path, is_dir=False)
    if classification is not None:
        return classification
    return "**", "all"


def _first_literal_rule_for_entry(
    rules: list[tuple[str, str | None]], path: str, *, is_dir: bool
) -> tuple[str, str | None] | None:
    bare_path = path.rstrip("/")
    match_names = (bare_path + "/", bare_path) if is_dir else (path,)
    for pattern, target in rules:
        if not any(renpy_pattern_matches(name, pattern) for name in match_names):
            continue
        if target is None and is_dir:
            directory_prefix = pattern.rstrip("*")
            if pattern != directory_prefix and any(
                renpy_pattern_matches(name, directory_prefix)
                for name in match_names
            ):
                continue
        return pattern, target
    return None


@functools.lru_cache(maxsize=1)
def current_repository_files() -> tuple[str, ...]:
    result = subprocess.run(
        ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
        cwd=ROOT,
        capture_output=True,
        check=False,
    )
    if result.returncode:
        raise AssertionError(
            "could not enumerate current repository files: "
            + result.stderr.decode("utf-8", errors="replace")
        )
    return tuple(
        sorted(
            path.replace("\\", "/")
            for path in result.stdout.decode("utf-8", errors="strict").split("\0")
            if path
        )
    )


def exclusion_probe_paths(pattern: str) -> tuple[str, ...]:
    probes: set[str] = {
        path
        for path in current_repository_files()
        if renpy_pattern_matches(path, pattern)
    }
    if pattern in {
        "game/images/hd/**",
        "game/images/backup_sd/**",
        "game/images/webp_backup/**",
    }:
        directory = pattern.removesuffix("**")
        probes.update(
            directory + "probe" + extension
            for extension in (".png", ".webp", ".jpg")
        )
    elif pattern == "game/audio/narration/voice_test/**":
        probes.update(
            {
                "game/audio/narration/voice_test/probe.mp3",
                "game/audio/narration/voice_test/probe.ogg",
                "game/audio/narration/voice_test/probe.wav",
            }
        )
    elif pattern == "game/audio/music/*_alt.mp3":
        probes.add("game/audio/music/probe_alt.mp3")
    elif pattern.endswith("/**"):
        directory = pattern.removesuffix("**")
        probes.update(
            directory + "probe" + extension
            for extension in (
                ".txt",
                ".md",
                ".rpyc",
                ".png",
                ".webp",
                ".jpg",
                ".ogg",
                ".mp3",
                ".wav",
            )
        )
    else:
        probes.add(pattern)
    return tuple(sorted(probes))


def exclusion_order_violations(
    rules: list[tuple[str, str | None]],
    required_patterns: tuple[str, ...],
) -> list[str]:
    """Report approved exclusions shadowed by an earlier inclusion rule."""
    violations: list[str] = []
    for required in required_patterns:
        positions = [
            index
            for index, rule in enumerate(rules)
            if rule == (required, None)
        ]
        if len(positions) != 1:
            continue
        exclusion_index = positions[0]
        probes = exclusion_probe_paths(required)
        for pattern, target in rules[:exclusion_index]:
            if target is None:
                continue
            if any(renpy_pattern_matches(probe, pattern) for probe in probes):
                violations.append(f"{required} appears after {pattern}")
                break
    return violations


def missing_project_files(paths: tuple[str, ...]) -> list[str]:
    return [path for path in paths if not (ROOT / path).is_file()]


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


class PackagingParserGuardTests(unittest.TestCase):
    def test_strict_config_rejects_ambiguous_build_syntax(self) -> None:
        fixtures = (
            '''init python:
    if False:
        build.classify("decoy.png", None)
''',
            '''init python:
    def helper():
        build.classify("decoy.png", None)
''',
            '''init python:
    build.base_patterns.clear()
''',
            '''init python:
    build.clear()
''',
            '''init python:
    build.remove("game/**")
''',
            '''init python:
    first, second = build, object()
''',
            '''init python:
    helper = lambda: build.classify("decoy.png", None)
''',
            '''init python:
    import build
''',
            '''init python:
    exec("build.classify('decoy.png', None)")
''',
            '''init python:
    eval("build.classify")
''',
            '''init python:
    __import__("build")
''',
            '''init python:
    getattr(build, "classify")("decoy.png", None)
''',
            '''init python:
    alias = build.classify
''',
            '''init python:
    build.android_package = build.ios_bundle_identifier = "duplicate"
''',
            '''init python:
    build.base_patterns = []
''',
            '''init python:
    build.android_package = runtime_value
''',
            '''init python:
    build.classify(runtime_pattern, None)
''',
            '''init 10 python:
    build.documentation("README.txt")
''',
            '''init offset = 10
init python:
    build.documentation("README.txt")
''',
            '''init python:
    build.documentation("README.txt")
init python:
    build.documentation("SECOND.txt")
''',
        )
        for source in fixtures:
            with self.subTest(source=source):
                with self.assertRaises(AssertionError):
                    active_literal_build_calls(source)

    def test_external_scanner_rejects_build_evidence_without_other_build_false_positive(
        self,
    ) -> None:
        sources = {
            "game/exec_rogue.py": 'exec("build.classify(\\"game/**\\", None)")\n',
            "game/reflection_rogue.rpy": 'define rogue = getattr(renpy.store, "build")\n',
            "game/store_rogue.rpym": "x = renpy.store.build\n",
            "game/short_store_rogue.py": "store.build.classify('game/**', None)\n",
            "game/global_rogue.rpy": "define packaging = build\n",
            "game/import_rogue.py": "from renpy.store import build\n",
            "game/store_alias_rogue.py": '''import renpy.store as runtime_store
runtime_store.build.classify("game/**", None)
''',
            "game/from_store_alias_rogue.py": '''from renpy import store as runtime_store
runtime_store.build.classify("game/**", None)
''',
            "game/unrelated.py": '''taxonomy.classify("family")
getattr(taxonomy, "classify")
other.build.classify("not-renpy-build")
decoy = "build.classify('string.png', None)"
# exec("build.clear()")
''',
        }
        self.assertEqual(
            set(external_build_contract_violations(sources)),
            {
                "game/exec_rogue.py",
                "game/reflection_rogue.rpy",
                "game/store_rogue.rpym",
                "game/short_store_rogue.py",
                "game/global_rogue.rpy",
                "game/import_rogue.py",
                "game/store_alias_rogue.py",
                "game/from_store_alias_rogue.py",
            },
        )

    def test_outer_triple_quoted_strings_cannot_create_init_blocks(self) -> None:
        decoy_rules = "\n".join(
            f"    build.classify({pattern!r}, None)"
            for pattern in APPROVED_PACKAGE_EXCLUSIONS
        )
        decoy_rules += (
            '\n    build.classify("README.txt", "windows")'
            '\n    build.documentation("README.txt")'
        )
        wrappers = (
            'define decoy = _p("""\n{body}\n""")\n',
            'python:\n    reference = """\n{body}\n"""\n',
        )
        for wrapper in wrappers:
            source = wrapper.format(
                body="init -100 python:\n" + decoy_rules
            ) + '''init python:
    build.documentation("REAL.txt")
'''
            with self.subTest(wrapper=wrapper.splitlines()[0]):
                self.assertEqual(
                    active_literal_build_calls(source),
                    [("documentation", ("REAL.txt",))],
                )

    def test_strict_options_grammar_accepts_direct_literals_and_allowed_fields(self) -> None:
        source = '''define build.name = "Game"
define build.android_landscape = True
define build.ios_landscape = True
init python:
    # build.classify("comment.png", None)
    build.classify("exclude.png", None)
    build.documentation("README.txt")
    build.android_package = "example.game"
    build.android_permissions = []
    build.android_target_api = 36
    build.ios_bundle_identifier = "example.game"
    build.ios_bundle_name = "Game"
    build.executable_name = "Game"
    build.mac_architectures = "universal"
    build.google_play_key = None
    build.google_play_salt = None
'''
        self.assertEqual(
            active_literal_build_calls(source),
            [
                ("classify", ("exclude.png", None)),
                ("documentation", ("README.txt",)),
            ],
        )

    def test_options_outer_build_defines_are_strict(self) -> None:
        fixtures = (
            'define build.unknown = 1\n',
            'define build.name = runtime_name\n',
            'define rogue = build.classify("game/**", "all")\n',
            'define rogue = exec("build.clear()")\n',
        )
        for prefix in fixtures:
            source = prefix + '''init python:
    build.documentation("README.txt")
'''
            with self.subTest(prefix=prefix):
                self.assertTrue(options_build_contract_scope_violations(source))

    def test_order_guard_rejects_an_inclusion_before_its_exclusion(self) -> None:
        cases = (
            ("game/test_game.rpyc", "game/**.rpyc"),
            ("game/audio/music/*_alt.mp3", "game/**.mp3"),
            (
                "game/audio/music/*_alt.mp3",
                "game/audio/music/battle_prepare_alt.mp3",
            ),
            ("game/images/hd/**", "game/**.png"),
            ("logo.png", "**"),
        )
        for exclusion, inclusion in cases:
            with self.subTest(exclusion=exclusion, inclusion=inclusion):
                reversed_source = f'''init python:
    build.classify("{inclusion}", "all")
    build.classify("{exclusion}", None)
'''
                reversed_rules = literal_classification_rules(
                    active_literal_build_calls(reversed_source)
                )
                self.assertEqual(
                    exclusion_order_violations(reversed_rules, (exclusion,)),
                    [f"{exclusion} appears after {inclusion}"],
                )

                correct_source = f'''init python:
    build.classify("{exclusion}", None)
    build.classify("{inclusion}", "all")
'''
                correct_rules = literal_classification_rules(
                    active_literal_build_calls(correct_source)
                )
                self.assertEqual(
                    exclusion_order_violations(correct_rules, (exclusion,)),
                    [],
                )

    def test_first_match_guard_detects_protected_path_exclusions(self) -> None:
        source = '''init python:
    build.classify("game/images/ui/", None)
    build.classify("old-game/", None)
    build.classify("README.txt", None)
    build.classify("android-**", None)
'''
        rules = literal_classification_rules(active_literal_build_calls(source))
        expected = {
            PROTECTED_DYNAMIC_UI_PATHS[0]: ("game/images/ui/", None),
            "old-game/script.rpyc": ("old-game/", None),
            "README.txt": ("README.txt", None),
            PROTECTED_ANDROID_BUILD_INPUTS[0]: ("android-**", None),
        }
        for path, classification in expected.items():
            with self.subTest(path=path):
                self.assertEqual(
                    first_literal_classification(rules, path),
                    classification,
                )

    def test_windows_only_ui_classification_is_not_all_platform(self) -> None:
        source = '''init python:
    build.classify("game/images/**", "windows")
'''
        rules = literal_classification_rules(active_literal_build_calls(source))
        classification = first_literal_classification(
            rules, PROTECTED_DYNAMIC_UI_PATHS[0]
        )
        violations = {
            PROTECTED_DYNAMIC_UI_PATHS[0]: classification
            for _ in (0,)
            if classification is None or classification[1] != "all"
        }
        self.assertEqual(
            violations,
            {PROTECTED_DYNAMIC_UI_PATHS[0]: ("game/images/**", "windows")},
        )


class PackagingClassificationContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.options = read_text("game/options.rpy")
        cls.calls = active_literal_build_calls(cls.options)
        cls.rules = literal_classification_rules(cls.calls)

    def test_approved_release_payload_has_one_direct_exclusion_rule_each(self) -> None:
        counts = {
            pattern: self.rules.count((pattern, None))
            for pattern in APPROVED_PACKAGE_EXCLUSIONS
        }
        violations = {
            pattern: count
            for pattern, count in counts.items()
            if count != 1
        }
        self.assertEqual(
            violations,
            {},
            f"approved release exclusions need one direct rule each: {violations}",
        )

    def test_build_contract_is_confined_to_game_options(self) -> None:
        self.assertEqual(options_build_contract_scope_violations(self.options), [])
        sources = {
            path.relative_to(ROOT).as_posix(): path.read_text(encoding="utf-8")
            for path in GAME.rglob("*")
            if path.suffix in {".rpy", ".rpym", ".py"}
        }
        self.assertEqual(external_build_contract_violations(sources), {})

    def test_release_exclusions_precede_matching_inclusion_rules(self) -> None:
        self.assertEqual(
            exclusion_order_violations(self.rules, APPROVED_PACKAGE_EXCLUSIONS),
            [],
        )

    def test_readme_is_directly_classified_for_windows_and_as_documentation(self) -> None:
        readme_rules = [rule for rule in self.rules if rule[0] == "README.txt"]
        self.assertEqual(readme_rules, [("README.txt", "windows")])
        documentation_calls = [
            arguments
            for name, arguments in self.calls
            if name == "documentation" and arguments == ("README.txt",)
        ]
        self.assertEqual(documentation_calls, [("README.txt",)])
        self.assertEqual(
            first_literal_classification(self.rules, "README.txt"),
            ("README.txt", "windows"),
        )

    def test_old_game_compiler_inputs_are_not_excluded_by_source_rules(self) -> None:
        self.assertEqual(
            first_literal_classification(
                list(RENPY_EARLY_INPUT_RULES), "old-game/script.rpyc"
            ),
            ("old-game/", None),
        )
        violations = {}
        for compiled in OLD_GAME.rglob("*.rpyc"):
            relative = compiled.relative_to(ROOT).as_posix()
            classification = first_literal_classification(self.rules, relative)
            if classification[1] is None:
                violations[relative] = classification[0]
        self.assertEqual(violations, {})

    def test_audited_dynamic_ui_paths_remain_included(self) -> None:
        self.assertEqual(len(PROTECTED_DYNAMIC_UI_PATHS), 22)
        self.assertEqual(missing_project_files(PROTECTED_DYNAMIC_UI_PATHS), [])
        violations = {}
        for path in PROTECTED_DYNAMIC_UI_PATHS:
            classification = first_literal_classification(self.rules, path)
            if classification[1] != "all":
                violations[path] = classification
        self.assertEqual(violations, {})

    def test_android_icon_and_presplash_inputs_remain_available(self) -> None:
        self.assertTrue(
            set(PROTECTED_ANDROID_BUILD_INPUTS).isdisjoint(APPROVED_PACKAGE_EXCLUSIONS)
        )
        self.assertEqual(missing_project_files(PROTECTED_ANDROID_BUILD_INPUTS), [])
        violations = {}
        for path in PROTECTED_ANDROID_BUILD_INPUTS:
            self.assertEqual(
                first_literal_classification(list(RENPY_EARLY_INPUT_RULES), path),
                ("android-*.png", "android"),
            )
            classification = first_literal_classification(self.rules, path)
            if classification[1] is None:
                violations[path] = classification[0]
        self.assertEqual(violations, {})


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

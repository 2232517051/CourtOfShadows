#!/usr/bin/env python3
"""Source-level contract for the uploadable Court of Shadows 3.9.2 release."""

from __future__ import annotations

import ast
import json
import re
import subprocess
import sys
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


def read_text(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def assigned_literal(source: str, name: str):
    """Return a Python literal assigned to *name* inside a Ren'Py source file."""
    match = re.search(rf"(?m)^\s*{re.escape(name)}\s*=\s*", source)
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
                    return ast.literal_eval(source[index : cursor + 1])
            cursor += 1
        raise AssertionError(f"literal assigned to {name!r} is unterminated")

    quote = '"' * 3 if source.startswith('"' * 3, index) else '"'
    end = source.find(quote, index + len(quote))
    if end < 0:
        raise AssertionError(f"string assigned to {name!r} is unterminated")
    return ast.literal_eval(source[index : end + len(quote)])


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


def assigned_dict_keys(function: ast.FunctionDef, name: str) -> set[str]:
    for node in ast.walk(function):
        if not isinstance(node, ast.Assign) or not isinstance(node.value, ast.Dict):
            continue
        if any(isinstance(target, ast.Name) and target.id == name for target in node.targets):
            return {
                key.value
                for key in node.value.keys
                if isinstance(key, ast.Constant) and isinstance(key.value, str)
            }
    raise AssertionError(f"dictionary assignment for {name!r} not found")


def returned_dict_keys(function: ast.FunctionDef) -> set[str]:
    returns = [
        node.value
        for node in ast.walk(function)
        if isinstance(node, ast.Return) and isinstance(node.value, ast.Dict)
    ]
    if len(returns) != 1:
        raise AssertionError(f"expected one literal dictionary return, found {len(returns)}")
    return {
        key.value
        for key in returns[0].keys
        if isinstance(key, ast.Constant) and isinstance(key.value, str)
    }


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


class VersionAndAndroidContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.options = read_text("game/options.rpy")
        cls.android = json.loads(read_text("android.json"))

    def test_config_and_android_versions_match_392(self) -> None:
        config_version = re.search(
            r'(?m)^define config\.version\s*=\s*"([^"]+)"', self.options
        )
        self.assertIsNotNone(config_version)
        self.assertEqual(config_version.group(1), APPROVED_VERSION)
        self.assertEqual(self.android["version"], APPROVED_VERSION)

    def test_android_package_and_api_agree_with_build_source(self) -> None:
        source_package = re.search(
            r'(?m)^\s*build\.android_package\s*=\s*"([^"]+)"', self.options
        )
        source_api = re.search(
            r"(?m)^\s*build\.android_target_api\s*=\s*(\d+)", self.options
        )
        self.assertIsNotNone(source_package)
        self.assertIsNotNone(source_api)
        self.assertEqual(source_package.group(1), APPROVED_ANDROID_PACKAGE)
        self.assertEqual(self.android["package"], APPROVED_ANDROID_PACKAGE)
        self.assertEqual(int(source_api.group(1)), APPROVED_ANDROID_API)
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
        route_function = python_function(difficulty, "get_finale_route_availability")
        route_keys = assigned_dict_keys(route_function, "routes")
        ending_function = python_function(difficulty, "get_finale_ending_availability")
        availability_keys = returned_dict_keys(ending_function)

        self.assertEqual(tuple(catalog), APPROVED_ENDING_KEYS)
        self.assertEqual(info_keys, approved)
        self.assertEqual(route_keys - {"resist"}, approved)
        self.assertEqual(route_keys - approved, {"resist"})
        self.assertEqual(availability_keys, approved)


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
            ("五章", "九个主线结局", "隐藏尾声", *APPROVED_CHINESE_STATS),
            "About",
        )
        self.assertIn("v3.9.2", self.about)

    def test_privacy_and_rating_copy_match_the_current_build(self) -> None:
        self.assertIn("版本：3.9.2", self.privacy)
        self.assertIn("更新日期：2026年8月", self.privacy)
        self.assertNotIn("TapTap", self.rating)
        self.assertNotIn('textbutton "去评分"', self.rating)
        self.assertRegex(self.rating, r'textbutton "(?:关闭|知道了|下次再说)"')

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
        stale_exact = (
            "v3.2",
            "版本：3.1",
            "即将登陆 TapTap · Steam",
            "New Game+ 二周目解锁新内容",
            "New Game+ unlocks additional content",
            "隐藏结局",
            "hidden ending",
        )
        five_endings = re.compile(
            r"(?:五|5)\s*个?\s*(?:独特|截然不同|不同|distinct|unique)?\s*结局|"
            r"\bfive\s+(?:distinct\s+|unique\s+)?endings\b",
            re.IGNORECASE,
        )

        for subject, source in self.current_copy.items():
            with self.subTest(subject=subject):
                for phrase in stale_exact:
                    self.assertNotIn(phrase.casefold(), source.casefold())
                for line in source.splitlines():
                    if not five_endings.search(line):
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
            "About": assigned_literal(read_text("game/options.rpy"), "define gui.about"),
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
            re.compile(r"New Game\+ unlocks (?:additional|new) content", re.IGNORECASE),
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

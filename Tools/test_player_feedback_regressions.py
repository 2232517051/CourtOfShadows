from __future__ import annotations

import importlib.util
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GAME = ROOT / "game"


def read_game_file(name: str) -> str:
    return (GAME / name).read_text(encoding="utf-8")


def character_image_tag(name: str) -> str:
    characters = read_game_file("characters.rpy")
    match = re.search(
        rf'^define {re.escape(name)} = Character\([^\n]*image="(\w+)"\)',
        characters,
        re.MULTILINE,
    )
    if match is None:
        raise AssertionError(f"character image binding for {name!r} not found")
    return f"{match.group(1)}_img"


def label_body(name: str, label: str) -> str:
    text = read_game_file(name)
    match = re.search(
        rf"(?ms)^label {re.escape(label)}(?:\([^\n]*\))?:\s*\n(.*?)(?=^label |\Z)",
        text,
    )
    if match is None:
        raise AssertionError(f"label {label!r} not found in {name}")
    return match.group(1)


def source_indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def source_block(lines: list[str], start: int) -> tuple[list[str], int]:
    """Return an indentation-scoped Ren'Py block and its exclusive end index."""
    indent = source_indent(lines[start])
    for end in range(start + 1, len(lines)):
        if lines[end].strip() and source_indent(lines[end]) <= indent:
            return lines[start:end], end
    return lines[start:], len(lines)


def find_source_line(lines: list[str], exact: str) -> int:
    matches = [index for index, line in enumerate(lines) if line.strip() == exact]
    if len(matches) != 1:
        raise AssertionError(f"expected one source line {exact!r}, found {len(matches)}")
    return matches[0]


def menu_outcomes(lines: list[str], menu_start: int) -> tuple[list[tuple[str, list[str]]], int]:
    """Parse only direct choice blocks belonging to one Ren'Py menu."""
    menu_indent = source_indent(lines[menu_start])
    _, menu_end = source_block(lines, menu_start)
    outcomes: list[tuple[str, list[str]]] = []
    for index in range(menu_start + 1, menu_end):
        stripped = lines[index].strip()
        if (
            source_indent(lines[index]) == menu_indent + 4
            and stripped.startswith('"')
            and stripped.endswith('":')
        ):
            outcome_block, _ = source_block(lines, index)
            outcomes.append((stripped[1:-2], outcome_block))
    return outcomes, menu_end


def state_assignments(lines: list[str]) -> list[str]:
    return [
        line.strip()
        for line in lines
        if line.strip().startswith(
            ("$ marriage_route =", "$ marriage_warm =", "$ marriage_proposal_open =")
        )
    ]


def load_portrait_scanner():
    spec = importlib.util.spec_from_file_location(
        "portrait_scanner_under_test", ROOT / "scan_missing_portraits.py"
    )
    if spec is None or spec.loader is None:
        raise AssertionError("could not load scan_missing_portraits.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PortraitContractTests(unittest.TestCase):
    def test_unregistered_show_gate_uses_real_word_boundaries(self) -> None:
        scanner = load_portrait_scanner()
        lines = [
            "show known_img at left\n",
            "    show missing_img at right with dissolve\n",
            "# show ignored_img at left\n",
            "showcase fake_img\n",
        ]
        self.assertEqual(
            scanner.find_unregistered_shows(lines, {"known_img"}),
            [(2, "missing_img")],
        )

    def test_character_definitions_use_semantic_portraits(self) -> None:
        characters = read_game_file("characters.rpy")
        southern = read_game_file("southern_expansion.rpy")
        self.assertRegex(characters, r'define little_girl = Character\("小女孩", color="#[0-9a-f]+"\)')
        self.assertIn('define queen_rep = Character("王后方代表", color="#9370db", image="queen_envoy")', characters)
        self.assertIn('define baron_rep = Character("男爵方代表", color="#2f4f4f", image="noble_werner")', characters)
        self.assertIn('define tax_man = Character("公会税吏", color="#8a7a4a", image="tax_collector")', southern)
        self.assertIn('define guild_clerk = Character("公会账房", color="#9a8a6a", image="merchant_guild")', southern)

    def test_dialogue_shows_match_speaker_and_child_stays_off_screen(self) -> None:
        chapter = read_game_file("chapter5.rpy")
        southern = read_game_file("southern_expansion.rpy")
        self.assertNotRegex(chapter, r'(?s)show blacksmith_wife_img[^\n]*\n\s*little_girl ')
        self.assertRegex(chapter, r'(?s)show queen_envoy_img[^\n]*\n\s*queen_rep ')
        self.assertRegex(chapter, r'(?s)show noble_werner_img[^\n]*\n\s*baron_rep ')
        self.assertRegex(southern, r'(?s)show tax_collector_img[^\n]*\n\s*tax_man ')
        self.assertRegex(southern, r'(?s)show merchant_guild_img[^\n]*\n\s*guild_clerk ')

    def test_departing_characters_clear_before_following_narration(self) -> None:
        chapter = read_game_file("chapter5.rpy")
        baron_envoy_tag = character_image_tag("baron_envoy")
        self.assertRegex(chapter, rf'(?s)show {re.escape(baron_envoy_tag)}[^\n]*\n\s*baron_envoy ')
        self.assertRegex(
            chapter,
            rf'送走了男爵的密使后，你以为这一天的访客到头了。"\s*\n\s*hide {re.escape(baron_envoy_tag)}',
        )
        self.assertRegex(chapter, r'她那天夜里离开了艾登堡。没有告诉你她去哪。"\s*\n\s*hide elena_img')


class MarriageContractTests(unittest.TestCase):
    def test_chapter_three_opens_talks_without_accepting_marriage(self) -> None:
        lines = label_body("chapter3.rpy", "ch3_end").splitlines()
        choice_start = find_source_line(lines, '"回信，愿意谈这桩联姻":')
        choice_block, _ = source_block(lines, choice_start)
        self.assertEqual(
            state_assignments(choice_block),
            [
                "$ marriage_proposal_open = True",
                "$ marriage_route = False",
                "$ marriage_warm = False",
            ],
        )
        self.assertIn(
            '$ log_decision("第三章", "同意会面商谈联姻")',
            [line.strip() for line in choice_block],
        )

    def test_chapter_four_meeting_has_only_three_explicit_state_results(self) -> None:
        palace_lines = label_body("chapter4.rpy", "ch4_palace").splitlines()
        guard_start = find_source_line(
            palace_lines, "if marriage_proposal_open or marriage_route:"
        )
        _, meeting_end = source_block(palace_lines, guard_start)
        menu_starts = [
            index
            for index in range(guard_start + 1, meeting_end)
            if palace_lines[index].strip() == "menu:"
        ]
        self.assertEqual(len(menu_starts), 1)
        menu_start = menu_starts[0]
        outcomes, menu_end = menu_outcomes(palace_lines, menu_start)
        self.assertLess(menu_end, meeting_end)
        self.assertEqual(
            [choice for choice, _ in outcomes],
            [
                "接受婚约，把它当成纯粹的盟约",
                "接受婚约，也愿意认识英格丽",
                "到此为止，结束联姻商谈",
            ],
        )

        expected_states = [
            [
                "$ marriage_route = True",
                "$ marriage_warm = False",
                "$ marriage_proposal_open = False",
            ],
            [
                "$ marriage_route = True",
                "$ marriage_warm = True",
                "$ marriage_proposal_open = False",
            ],
            [
                "$ marriage_route = False",
                "$ marriage_warm = False",
                "$ marriage_proposal_open = False",
            ],
        ]
        self.assertEqual(
            [state_assignments(outcome) for _, outcome in outcomes], expected_states
        )

        post_menu_lines = palace_lines[menu_end:meeting_end]
        self.assertEqual(state_assignments(post_menu_lines), [])

    def test_legacy_marriage_route_is_preserved_and_admitted(self) -> None:
        self.assertIn("default marriage_proposal_open = False", read_game_file("characters.rpy"))
        compat_lines = read_game_file("save_compat.rpy").splitlines()
        defaults_start = find_source_line(compat_lines, "_store_defaults = {")
        defaults_block, defaults_end = source_block(compat_lines, defaults_start)
        default_lines = [line.strip() for line in defaults_block]
        self.assertIn('"marriage_proposal_open": False,', default_lines)
        self.assertNotIn('"marriage_route":', default_lines)

        loop_start = find_source_line(
            compat_lines, "for var_name, default_val in _store_defaults.items():"
        )
        self.assertGreater(loop_start, defaults_end)
        loop_block, _ = source_block(compat_lines, loop_start)
        self.assertEqual(
            [line.strip() for line in loop_block if line.strip()],
            [
                "for var_name, default_val in _store_defaults.items():",
                "if not hasattr(store, var_name):",
                "setattr(store, var_name, default_val)",
            ],
        )

        legacy_state = {"marriage_route": True}
        if "marriage_proposal_open" not in legacy_state:
            legacy_state["marriage_proposal_open"] = False
        self.assertEqual(
            legacy_state,
            {"marriage_route": True, "marriage_proposal_open": False},
        )

        palace_lines = label_body("chapter4.rpy", "ch4_palace").splitlines()
        self.assertIsNotNone(
            find_source_line(palace_lines, "if marriage_proposal_open or marriage_route:")
        )

    def test_declining_marriage_reopens_only_the_non_corsair_elena_acceptance(self) -> None:
        palace_lines = label_body("chapter4.rpy", "ch4_palace").splitlines()
        decline_start = find_source_line(palace_lines, '"到此为止，结束联姻商谈":')
        decline_block, _ = source_block(palace_lines, decline_start)
        self.assertEqual(
            state_assignments(decline_block),
            [
                "$ marriage_route = False",
                "$ marriage_warm = False",
                "$ marriage_proposal_open = False",
            ],
        )

        elena_lines = label_body("chapter4.rpy", "ch4_elena").splitlines()
        self.assertEqual(
            elena_lines[
                find_source_line(
                    elena_lines,
                    '"握住她的手" if not marriage_route and not corsair_romance:',
                )
            ].strip(),
            '"握住她的手" if not marriage_route and not corsair_romance:',
        )
        self.assertEqual(
            elena_lines[
                find_source_line(
                    elena_lines,
                    '"沉默片刻，把目光移向远处的天际线" if not marriage_route and corsair_romance:',
                )
            ].strip(),
            '"沉默片刻，把目光移向远处的天际线" if not marriage_route and corsair_romance:',
        )
        self.assertEqual(
            elena_lines[
                find_source_line(
                    elena_lines,
                    '"告诉她，你已经接受了与英格丽的婚约" if marriage_route:',
                )
            ].strip(),
            '"告诉她，你已经接受了与英格丽的婚约" if marriage_route:',
        )


if __name__ == "__main__":
    unittest.main()

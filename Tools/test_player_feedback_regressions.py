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
        chapter = read_game_file("chapter3.rpy")
        choice = chapter.split('"回信，愿意谈这桩联姻":', 1)[1].split('"婉拒，我另有打算":', 1)[0]
        self.assertIn("$ marriage_proposal_open = True", choice)
        self.assertNotIn("$ marriage_route = True", choice)
        self.assertIn("同意会面商谈联姻", choice)

    def test_chapter_four_requires_explicit_acceptance_or_exit(self) -> None:
        palace = label_body("chapter4.rpy", "ch4_palace")
        self.assertIn("if marriage_proposal_open or marriage_route:", palace)
        for choice in (
            "接受婚约，把它当成纯粹的盟约",
            "接受婚约，也愿意认识英格丽",
            "到此为止，结束联姻商谈",
        ):
            self.assertIn(choice, palace)
        political = palace.split('"接受婚约，把它当成纯粹的盟约":', 1)[1].split('"接受婚约，也愿意认识英格丽":', 1)[0]
        warm = palace.split('"接受婚约，也愿意认识英格丽":', 1)[1].split('"到此为止，结束联姻商谈":', 1)[0]
        decline = palace.split('"到此为止，结束联姻商谈":', 1)[1].split("$ hide_all_chars()", 1)[0]
        self.assertIn("$ marriage_route = True", political)
        self.assertIn("$ marriage_warm = False", political)
        self.assertIn("$ marriage_route = True", warm)
        self.assertIn("$ marriage_warm = True", warm)
        self.assertIn("$ marriage_route = False", decline)
        self.assertIn("$ marriage_warm = False", decline)
        for result in (political, warm, decline):
            self.assertIn("$ marriage_proposal_open = False", result)

    def test_new_proposal_state_is_save_compatible(self) -> None:
        self.assertIn("default marriage_proposal_open = False", read_game_file("characters.rpy"))
        self.assertIn('"marriage_proposal_open": False', read_game_file("save_compat.rpy"))

    def test_elena_scene_names_the_accepted_engagement(self) -> None:
        chapter = read_game_file("chapter4.rpy")
        self.assertIn('"告诉她，你已经接受了与英格丽的婚约" if marriage_route:', chapter)
        self.assertIn("我已经接受了北境的婚约", chapter)
        self.assertIn('"感谢她的付出，但保持距离" if not marriage_route:', chapter)


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import importlib.util
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GAME = ROOT / "game"


def read_game_file(name: str) -> str:
    return (GAME / name).read_text(encoding="utf-8")


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
        self.assertRegex(chapter, r'送走了男爵的密使后，你以为这一天的访客到头了。"\s*\n\s*hide baron_envoy_img')
        self.assertRegex(chapter, r'她那天夜里离开了艾登堡。没有告诉你她去哪。"\s*\n\s*hide elena_img')


if __name__ == "__main__":
    unittest.main()

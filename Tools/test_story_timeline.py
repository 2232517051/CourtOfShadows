from __future__ import annotations

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


class FinaleCountdownTests(unittest.TestCase):
    def test_chapter_five_uses_existing_ten_day_preparations(self) -> None:
        chapter_start = label_body("chapter5.rpy", "chapter5_start")
        war_clouds = label_body("chapter5.rpy", "ch5_war_clouds")

        self.assertNotIn("call gov_building(5)", chapter_start)
        self.assertNotIn("call gov_festival", chapter_start)
        for choice in ("立即派出更多斥候", "加强城防", "先确保百姓安全"):
            self.assertIn(choice, war_clouds)


class MysteryTimelineTests(unittest.TestCase):
    def test_tunnel_anchor_does_not_reuse_numbered_second_day(self) -> None:
        tunnel = label_body("chapter3.rpy", "ch3_tunnel_exploration")
        self.assertNotIn("第二天傍晚", tunnel)
        self.assertIn("次日傍晚", tunnel)

    def test_prince_file_tracks_the_fathers_recent_death(self) -> None:
        prince = read_game_file("chapter4_prince.rpy")
        self.assertNotIn("二十年前那场「意外」", prince)
        self.assertIn("你父亲那场「病故」的处置记录", prince)

    def test_final_choice_displays_the_original_testament(self) -> None:
        final_choice = label_body("chapter5.rpy", "ch5_final_choice")
        self.assertNotIn("遗诏复本", final_choice)
        self.assertIn("遗诏的原本", final_choice)

    def test_truth_calendar_advances_from_the_will_date(self) -> None:
        truth = label_body("chapter5.rpy", "ending_truth")
        epilogue = label_body("endings_expansion.rpy", "ending_truth_epilogue")

        self.assertEqual(truth.count("格里菲斯朝的两百九十三年"), 2)
        self.assertNotIn("格里菲斯朝的两百七十三年", truth)
        self.assertIn("新王历五年·春", epilogue)
        self.assertNotIn("王历二十七年·春", epilogue)

    def test_father_son_epilogue_uses_five_year_gap(self) -> None:
        epilogue = label_body("endings_expansion.rpy", "ending_father_son_epilogue")

        self.assertIsNone(re.search(r"十(?:多)?年", epilogue))
        self.assertGreaterEqual(epilogue.count("五年"), 3)
        for impossible_memory in (
            "没有看着你长大",
            "没有看到你第一次骑马",
            "没有看到你第一次举起剑",
        ):
            self.assertNotIn(impossible_memory, epilogue)


if __name__ == "__main__":
    unittest.main()

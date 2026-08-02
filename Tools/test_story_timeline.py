from __future__ import annotations

import re
import unittest
from pathlib import Path

from PIL import Image


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


def testcase_body(name: str) -> str:
    text = read_game_file("test_game.rpy")
    match = re.search(
        rf"(?m)^testcase {re.escape(name)}(?:\([^\n]*\))?:[ \t]*$",
        text,
    )
    if match is None:
        raise AssertionError(f"testcase {name!r} not found in test_game.rpy")

    body_lines = []
    for line in text[match.end() :].splitlines():
        if line.strip() and not line[0].isspace():
            break
        body_lines.append(line)
    return "\n".join(body_lines)


def stops_music(source: str) -> bool:
    if re.search(
        r"(?m)^\s*(?:stop\s+music\b|(?:\$\s*)?(?:stop_music|stop_bgm)\s*\()",
        source,
    ):
        return True

    api_stops = re.finditer(
        r"(?m)^\s*(?:\$\s*)?renpy\.music\.stop\s*\(([^)]*)\)", source
    )
    for match in api_stops:
        arguments = match.group(1)
        named_channel = re.search(
            r"\bchannel\s*=\s*([\"'])([^\"']+)\1", arguments
        )
        if named_channel:
            if named_channel.group(2) == "music":
                return True
            continue

        positional_channel = re.match(r"\s*([\"'])([^\"']+)\1", arguments)
        if positional_channel:
            if positional_channel.group(2) == "music":
                return True
            continue

        # renpy.music.stop() defaults to the music channel. Treat dynamic
        # channel expressions conservatively because they cannot prove safety.
        return True

    return False


class FinaleCountdownTests(unittest.TestCase):
    def test_chapter_five_uses_existing_ten_day_preparations(self) -> None:
        chapter_start = label_body("chapter5.rpy", "chapter5_start")
        war_clouds = label_body("chapter5.rpy", "ch5_war_clouds")

        self.assertNotIn("call gov_building(5)", chapter_start)
        self.assertNotIn("call gov_festival", chapter_start)
        for choice in ("立即派出更多斥候", "加强城防", "先确保百姓安全"):
            self.assertIn(choice, war_clouds)


class ChapterMusicContinuityTests(unittest.TestCase):
    def test_chapter_three_opening_has_bgm_after_the_cinematic(self) -> None:
        cinematic = label_body("cinematics.rpy", "cinematic_chapter3")
        chapter_start = label_body("chapter3.rpy", "chapter3_start")

        cinematic_track = 'play music "audio/music/conspiracy.ogg"'
        track_start = cinematic.index(cinematic_track)
        cinematic_keeps_music = not stops_music(cinematic[track_start:])

        after_cinematic = chapter_start.split(
            "call cinematic_chapter3 from _call_cinematic_ch3", 1
        )[1]
        before_first_line = after_cinematic.split('"暗杀事件后的第三天。"', 1)[0]
        chapter_restarts_music = bool(
            re.search(r"(?m)^\s*(?:play music|\$ play_music\()", before_first_line)
        )

        self.assertTrue(
            cinematic_keeps_music or chapter_restarts_music,
            "chapter 3 stops the cinematic BGM and enters its opening dialogue in silence",
        )

    def test_chapter_three_skip_path_preserves_music(self) -> None:
        cinematics = read_game_file("cinematics.rpy")
        chapter_three = label_body("cinematics.rpy", "cinematic_chapter3")
        skip_handler = re.search(
            r"(?ms)^    def skip_cinematic\(\):\s*\n(.*?)(?=^    def |^default )",
            cinematics,
        )

        self.assertLess(
            chapter_three.index('play music "audio/music/conspiracy.ogg"'),
            chapter_three.index("show screen cin_overlay"),
            "the skip control becomes interactive before chapter 3 starts its BGM",
        )
        self.assertIsNotNone(skip_handler)
        self.assertFalse(
            stops_music(skip_handler.group(1)),
            "skipping a cinematic stops the BGM before the chapter opening",
        )

    def test_music_stop_detector_understands_default_and_explicit_channels(self) -> None:
        for stopping_call in (
            "stop music fadeout 2.0",
            "$ stop_music(fadeout=2.0)",
            "$ stop_bgm()",
            "renpy.music.stop()",
            "renpy.music.stop(fadeout=2.0)",
            'renpy.music.stop("music")',
            'renpy.music.stop(channel="music")',
        ):
            self.assertTrue(stops_music(stopping_call), stopping_call)

        for other_channel in (
            'renpy.music.stop("voice")',
            'renpy.music.stop(channel="sound")',
            'renpy.music.stop(fadeout=0.5, channel="voice")',
        ):
            self.assertFalse(stops_music(other_channel), other_channel)


class FatherSonAssetTests(unittest.TestCase):
    def test_father_son_render_baselines_are_revision_tagged(self) -> None:
        screenshot_dir = ROOT / "tests" / "screenshots"
        baselines = sorted(screenshot_dir.glob("father_son_*"))
        expected_nodes = {"empty", "manifested", "departed"}
        revision_pattern = re.compile(
            r"^father_son_(empty|manifested|departed)@([0-9a-f]+)\.png$"
        )

        self.assertEqual(len(baselines), 3)
        matches = [revision_pattern.fullmatch(path.name) for path in baselines]
        self.assertTrue(
            all(matches),
            f"father-son baselines must be revision-tagged PNGs: "
            f"{[path.name for path in baselines]}",
        )
        self.assertEqual({match.group(1) for match in matches if match}, expected_nodes)
        self.assertEqual(len({match.group(2) for match in matches if match}), 1)
        for path in baselines:
            with Image.open(path) as image:
                self.assertEqual(image.size, (1280, 720))

    def test_father_son_cg_pair_meets_release_contract(self) -> None:
        assets = (
            GAME / "images" / "cg_father_son_empty.webp",
            GAME / "images" / "cg_father_son.webp",
        )

        for asset in assets:
            self.assertTrue(asset.is_file(), f"missing father-son CG: {asset.name}")
            with Image.open(asset) as image:
                self.assertEqual(image.format, "WEBP")
                self.assertEqual(image.size, (1280, 720))

        self.assertLessEqual(sum(asset.stat().st_size for asset in assets), 1024 * 1024)
        self.assertFalse(any((GAME / "video").glob("*father_son*")))

    def test_father_son_cgs_are_defined_and_registered(self) -> None:
        image_defs = read_game_file("images_def.rpy")
        gallery = read_game_file("gallery.rpy")

        self.assertIn(
            'image cg_father_son_empty = Transform("images/cg_father_son_empty.webp", size=(1280, 720), fit="cover")',
            image_defs,
        )
        self.assertIn(
            'image cg_father_son = Transform("images/cg_father_son.webp", size=(1280, 720), fit="cover")',
            image_defs,
        )
        self.assertIn('("cg_father_son", "烛下告别")', gallery)

    def test_father_son_epilogue_stages_manifestation_and_departure(self) -> None:
        epilogue = label_body("endings_expansion.rpy", "ending_father_son_epilogue")
        reveal_anchor = epilogue.index('"你看到了。"')
        departure_anchor = epilogue.index('"他的身影越来越淡。像是晨雾在阳光下慢慢消散。"')
        first_empty = epilogue.index(
            "scene cg_father_son_empty as father_son_cg at father_son_slow_push with dissolve"
        )
        manifested = epilogue.index(
            "show cg_father_son as father_son_cg with Dissolve(1.5)"
        )
        final_empty = epilogue.rindex(
            "show cg_father_son_empty as father_son_cg with Dissolve(2.0)"
        )
        final_black = epilogue.rindex("scene black with fade")
        music = epilogue.index('$ play_music("audio/music/grief.ogg", fadein=2.0)')
        heartbeat = epilogue.index('$ play_sound("audio/sfx/heartbeat.ogg")')
        gallery_unlock = epilogue.index('$ unlock_gallery("cg_father_son")')

        self.assertIn("transform father_son_slow_push:", read_game_file("endings_expansion.rpy"))
        self.assertLess(music, first_empty)
        self.assertLess(first_empty, reveal_anchor)
        self.assertLess(reveal_anchor, heartbeat)
        self.assertLess(heartbeat, manifested)
        self.assertLess(manifested, gallery_unlock)
        self.assertLess(departure_anchor, final_empty)
        self.assertLess(final_empty, final_black)

    def test_father_son_render_regression_executes_production_atl(self) -> None:
        test_game = read_game_file("test_game.rpy")
        render_testcase = testcase_body("test_father_son_cg_render")
        ending_source = read_game_file("endings_expansion.rpy")

        self.assertIn("testcase test_father_son_cg_render:", test_game)
        executable_lines = [
            line.strip()
            for line in render_testcase.splitlines()
            if line.strip() and not line.lstrip().startswith("#")
        ]
        normalization = (
            "$ renpy.set_physical_size((config.screen_width, config.screen_height))"
        )
        physical_size_assertion = (
            "assert eval (renpy.get_physical_size() == "
            "(config.screen_width, config.screen_height))"
        )
        first_fixture = next(
            (
                index
                for index, line in enumerate(executable_lines)
                if line.startswith("run Start(")
            ),
            None,
        )
        self.assertIsNotNone(first_fixture, "father-son render testcase has no fixture")
        for command in (normalization, physical_size_assertion):
            self.assertIn(command, executable_lines)
            self.assertLess(executable_lines.index(command), first_fixture)
        self.assertIn(
            'run Start("test_father_son_cg_atl_smoke_fixture") until screen "say" timeout 4.0',
            test_game,
        )
        self.assertIn("pause 2.2", test_game)
        self.assertIn("label test_father_son_cg_atl_smoke_fixture:", test_game)
        self.assertIn(
            "scene cg_father_son_empty as father_son_cg at father_son_slow_push",
            test_game,
        )
        self.assertIn(
            """transform father_son_slow_push:
    xalign 0.5
    yalign 0.5
    zoom 1.0
    parallel:
        linear 20.0 zoom 1.025
    parallel:
        matrixcolor BrightnessMatrix(0.0)
        pause 1.8
        linear 0.18 matrixcolor BrightnessMatrix(0.018)
        linear 0.28 matrixcolor BrightnessMatrix(-0.008)
        linear 0.22 matrixcolor BrightnessMatrix(0.0)
        repeat""",
            ending_source,
        )


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

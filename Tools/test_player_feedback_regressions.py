from __future__ import annotations

import importlib.util
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GAME = ROOT / "game"


def read_game_file(name: str) -> str:
    return (GAME / name).read_text(encoding="utf-8")


def character_image_tag(name: str, source_name: str = "characters.rpy") -> str:
    characters = read_game_file(source_name)
    match = re.search(
        rf'^define {re.escape(name)} = Character\([^\n]*image="(\w+)"\)',
        characters,
        re.MULTILINE,
    )
    if match is None:
        raise AssertionError(
            f"character image binding for {name!r} not found in {source_name}"
        )
    return f"{match.group(1)}_img"


def label_body(name: str, label: str) -> str:
    return label_body_from_text(read_game_file(name), label, source_name=name)


def label_body_from_text(text: str, label: str, source_name: str = "source") -> str:
    match = re.search(
        rf"(?ms)^label {re.escape(label)}(?:\([^\n]*\))?:\s*\n(.*?)(?=^[^ \t\r\n]|\Z)",
        text,
    )
    if match is None:
        raise AssertionError(f"label {label!r} not found in {source_name}")
    return match.group(1)


def source_without_comments(lines: list[str]) -> str:
    """Return live source text while excluding comment-only lines."""
    return "\n".join(
        line for line in lines if not line.lstrip().startswith("#")
    )


def call_targets(lines: list[str]) -> list[str]:
    """Return Ren'Py call targets in source order, ignoring optional from labels."""
    targets: list[str] = []
    for line in lines:
        match = re.fullmatch(
            r"call (?P<target>[A-Za-z_]\w*)(?: from [A-Za-z_]\w*)?",
            line.strip(),
        )
        if match is not None:
            targets.append(match.group("target"))
    return targets


SELENE_CHARACTER_DIALOGUE_RE = re.compile(r"(?m)^\s*corsair\s+[\"']")
SELENE_DIRECT_REUNION_RE = re.compile(
    r"(?m)^(?![^\n]*(?:(?:商人|水手|船员|旅人|有人)[^。；\n]{0,4}"
    r"(?:说|称|提到|听到)|听说|据说|传闻|消息))[^\n]*"
    r"(?:赛琳(?:本人)?|她)[^。；\n]{0,20}"
    r"(?:来到|走进|走到|站在|出现|抵达|回到|驶入|登上|"
    r"(?:与|和)你(?:相见|重逢|跳舞|同行)|牵住你|挽住你|拥抱你|吻你)"
    r"|你[^。；\n]{0,8}(?:与|和)(?:赛琳|她)[^。；\n]{0,8}"
    r"(?:相见|重逢|跳舞|同行|拥抱)",
)
SELENE_DIRECT_DELIVERY_RE = re.compile(
    r"(?:赛琳(?:本人)?|她)[^，。；\n]{0,8}"
    r"(?:送来|捎来|寄来|带来|递来|送到|捎到|寄到|带到|递到)"
    r"[^，。；\n]{0,8}(?:信|口信|字条|包裹|消息)",
)


def ending_section(name: str, label: str) -> str:
    text = read_game_file(name)
    match = re.search(
        rf"(?ms)^label {re.escape(label)}:\s*\n(.*?)(?=^label ending_|\Z)",
        text,
    )
    if match is None:
        raise AssertionError(f"ending section {label!r} not found in {name}")
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


def direct_source_branches(
    lines: list[str], start: int, end: int, indent: int
) -> list[tuple[str, list[str]]]:
    """Return one direct if/elif/else chain with indentation-scoped bodies."""
    first = next(
        (
            index
            for index in range(start, end)
            if source_indent(lines[index]) == indent
            and re.fullmatch(r"if .+:", lines[index].strip())
        ),
        None,
    )
    if first is None:
        return []

    branches: list[tuple[str, list[str]]] = []
    branch_start = first
    while branch_start < end:
        branch_end = end
        next_sibling: int | None = None
        for index in range(branch_start + 1, end):
            stripped = lines[index].strip()
            if not stripped or stripped.startswith("#"):
                continue
            line_indent = source_indent(lines[index])
            if line_indent < indent:
                branch_end = index
                break
            if line_indent == indent:
                branch_end = index
                if re.fullmatch(r"elif .+:|else:", stripped):
                    next_sibling = index
                break

        branches.append(
            (lines[branch_start].strip(), lines[branch_start:branch_end])
        )
        if next_sibling is None:
            break
        branch_start = next_sibling

    return branches


def find_source_line(lines: list[str], exact: str) -> int:
    matches = [index for index, line in enumerate(lines) if line.strip() == exact]
    if len(matches) != 1:
        raise AssertionError(f"expected one source line {exact!r}, found {len(matches)}")
    return matches[0]


def menu_outcomes(
    lines: list[str], menu_start: int
) -> tuple[list[tuple[str, str | None, list[str]]], int]:
    """Parse only direct choice blocks belonging to one Ren'Py menu."""
    menu_indent = source_indent(lines[menu_start])
    _, menu_end = source_block(lines, menu_start)
    outcomes: list[tuple[str, str | None, list[str]]] = []
    for index in range(menu_start + 1, menu_end):
        stripped = lines[index].strip()
        match = re.fullmatch(r'"(?P<choice>.+)"(?: if (?P<condition>.+))?:', stripped)
        if source_indent(lines[index]) == menu_indent + 4 and match is not None:
            outcome_block, _ = source_block(lines, index)
            outcomes.append(
                (match.group("choice"), match.group("condition"), outcome_block)
            )
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


class SourceParsingContractTests(unittest.TestCase):
    def test_label_body_stops_before_next_top_level_section_comment(self) -> None:
        people = label_body("endings_expansion.rpy", "ending_peoples_epilogue")

        self.assertNotIn("## 隐藏结局：父与子", people)
        self.assertNotIn("transform father_son_slow_push", people)

    def test_label_body_stops_at_each_real_top_level_boundary(self) -> None:
        fixtures = {
            "section comment": (
                'label target:\n    "inside"\n\n## next section\n    "leaked"\n'
            ),
            "transform": (
                'label target:\n    "inside"\n\ntransform next_transform:\n    alpha 1.0\n'
            ),
            "label": 'label target:\n    "inside"\n\nlabel next_label:\n    "leaked"\n',
        }

        for boundary, source in fixtures.items():
            with self.subTest(boundary=boundary):
                body = label_body_from_text(source, "target")
                self.assertIn('"inside"', body)
                self.assertNotIn("next", body)
                self.assertNotIn("leaked", body)

    def test_selene_contact_patterns_reject_direct_contact_in_both_quote_styles(self) -> None:
        for direct_dialogue in ('    corsair "我回来了。"', "    corsair '我回来了。'"):
            with self.subTest(direct_dialogue=direct_dialogue):
                self.assertIsNotNone(SELENE_CHARACTER_DIALOGUE_RE.search(direct_dialogue))

        self.assertIsNotNone(
            SELENE_DIRECT_REUNION_RE.search("她来到广场，与你跳舞。")
        )
        self.assertIsNotNone(SELENE_DIRECT_REUNION_RE.search("赛琳和你重逢。"))
        self.assertIsNotNone(SELENE_DIRECT_DELIVERY_RE.search("她捎来信。"))
        self.assertIsNone(
            SELENE_DIRECT_REUNION_RE.search("商人说她回到潮汐港继续航海。")
        )

    def test_direct_branches_stop_before_outer_cleanup_and_later_chain(self) -> None:
        lines = [
            "    if marriage_route:",
            "        if marriage_warm:",
            '            "warm home event"',
            "        else:",
            '            "cold home event"',
            "        hide ingrid_img",
            "    elif corsair_romance:",
            '        "corsair event"',
        ]

        nested = direct_source_branches(lines, 1, len(lines), 8)

        self.assertEqual(
            [condition for condition, _ in nested],
            ["if marriage_warm:", "else:"],
        )
        self.assertEqual(
            [line.strip() for line in nested[-1][1] if line.strip()],
            ["else:", '"cold home event"'],
        )

    def test_direct_branches_stop_at_outer_dedent_without_cleanup(self) -> None:
        lines = [
            "    if marriage_route:",
            "        if marriage_warm:",
            '            "warm home event"',
            "        else:",
            '            "cold home event"',
            "    elif corsair_romance:",
            '        "corsair event"',
        ]

        nested = direct_source_branches(lines, 1, len(lines), 8)

        self.assertEqual(
            [line.strip() for line in nested[-1][1] if line.strip()],
            ["else:", '"cold home event"'],
        )


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
            [choice for choice, _, _ in outcomes],
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
            [state_assignments(outcome) for _, _, outcome in outcomes], expected_states
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

        palace_lines = label_body("chapter4.rpy", "ch4_palace").splitlines()
        find_source_line(palace_lines, "if marriage_proposal_open or marriage_route:")

    def test_declining_marriage_closes_the_proposal_state(self) -> None:
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

    def test_elena_confession_menu_has_directly_guarded_outcomes(self) -> None:
        elena_lines = label_body("chapter4.rpy", "ch4_elena").splitlines()
        guard_start = find_source_line(elena_lines, "if rel_elena >= 30:")
        _, guard_end = source_block(elena_lines, guard_start)
        guard_indent = source_indent(elena_lines[guard_start])
        menu_starts = [
            index
            for index in range(guard_start + 1, guard_end)
            if source_indent(elena_lines[index]) == guard_indent + 4
            and elena_lines[index].strip() == "menu:"
        ]
        self.assertEqual(len(menu_starts), 1)
        outcomes, menu_end = menu_outcomes(elena_lines, menu_starts[0])
        self.assertEqual(menu_end, guard_end)
        self.assertEqual(
            [(choice, condition) for choice, condition, _ in outcomes],
            [
                ("握住她的手", "not marriage_route and not corsair_romance"),
                ("沉默片刻，把目光移向远处的天际线", "not marriage_route and corsair_romance"),
                ("告诉她，你已经接受了与英格丽的婚约", "marriage_route"),
                ("感谢她的付出，但保持距离", "not marriage_route"),
            ],
        )
        marriage_body = outcomes[2][2]
        self.assertIn(
            'player "艾琳娜，我已经接受了北境的婚约。英格丽和议会的人都在等我履行它。"',
            [line.strip() for line in marriage_body],
        )
        self.assertIn(
            'player "我不能一面让她承担这份盟约，一面又向你伸手。那对你们两个人都不公平。"',
            [line.strip() for line in marriage_body],
        )


class EndingTimelineContractTests(unittest.TestCase):
    def test_each_core_ending_uses_the_five_year_anchor(self) -> None:
        for label in (
            "ending_iron_lord",
            "ending_shadow_king",
            "ending_holy_guardian",
            "ending_peoples_lord",
        ):
            with self.subTest(label=label):
                section = ending_section("chapter5.rpy", label)
                self.assertIn('"战后第五年。"', section)
                self.assertNotIn('"十年后。"', section)

    def test_people_core_uses_the_non_year_retrospective(self) -> None:
        people = ending_section("chapter5.rpy", "ending_peoples_lord")
        self.assertIn(
            '"后来的人谈起那场战争，未必还记得谁在王都占了上风。"',
            people,
        )
        self.assertIn(
            '"但艾登堡的人记得，有一个领主在众人争夺王座时，先守住了自己的百姓。"',
            people,
        )
        self.assertNotIn("几百年后", people)

    def test_side_character_fates_keep_mood_music_before_retrospective(self) -> None:
        fates = label_body("endings_expansion.rpy", "ending_side_characters_fate")
        lines = fates.splitlines()
        light_start = next(
            index
            for index, line in enumerate(lines)
            if line.strip() == 'if _fate_mood == "light":'
        )
        light_block, light_end = source_block(lines, light_start)
        neutral_block, neutral_end = source_block(lines, light_end)
        dark_block, dark_end = source_block(lines, neutral_end)

        self.assertEqual(
            [line.strip() for line in light_block if line.strip()],
            [
                'if _fate_mood == "light":',
                'play music "audio/music/dawn.ogg" fadein 3.0',
            ],
        )
        self.assertEqual(
            [line.strip() for line in neutral_block if line.strip()],
            [
                'elif _fate_mood == "neutral":',
                'play music "audio/music/grief.ogg" fadein 3.0',
            ],
        )
        self.assertEqual(
            [line.strip() for line in dark_block if line.strip()],
            ["else:", 'play music "audio/music/sad.ogg" fadein 3.0'],
        )

        heading = 'centered "{size=+4}— 回望战后旧事 —{/size}"'
        self.assertEqual(lines[dark_end].strip(), heading)
        self.assertEqual(sum(line.strip() == heading for line in lines), 1)
        self.assertNotIn("— 一年之后 —", fates)

    def test_iron_memorial_consumes_actual_battle_outcome(self) -> None:
        iron = label_body("endings_expansion.rpy", "ending_iron_epilogue")
        self.assertIn('if iron_battle_outcome == "pyrrhic":', iron)
        self.assertIn("两百多人", iron)
        self.assertIn("七十多人", iron)
        self.assertNotIn("三百七十二", iron)


class EndingRouteContractTests(unittest.TestCase):
    ENDING_TYPES = (
        "truth",
        "iron_lord",
        "shadow_king",
        "holy_guardian",
        "peoples_lord",
        "borgia",
        "vassal",
        "fall",
        "sea",
        "future_nonsea",
    )

    def route_lines(self) -> list[str]:
        game_ending = label_body("chapter5.rpy", "game_ending").splitlines()
        start = find_source_line(game_ending, "## 播放详细尾声")
        end = find_source_line(
            game_ending,
            "## 终局结算（批31: 属性面板/图鉴计数下移至全部尾声之后, 不再打断叙事收束）",
        )
        return game_ending[start:end]

    def test_real_game_ending_routes_each_fate_sequence_once(self) -> None:
        route = self.route_lines()
        people_start = find_source_line(route, 'if ending_type == "peoples_lord":')
        people_block, people_end = source_block(route, people_start)
        post_start = find_source_line(
            route, 'if ending_type not in ("sea", "peoples_lord"):'
        )
        post_block, post_end = source_block(route, post_start)

        self.assertLess(people_start, people_end)
        self.assertLess(people_end, post_start)
        self.assertLess(post_start, post_end)
        self.assertEqual(call_targets(people_block), ["ending_side_characters_fate"])
        self.assertEqual(
            [line.strip() for line in people_block if line.strip()],
            [
                'if ending_type == "peoples_lord":',
                "call ending_side_characters_fate from _call_ending_side_chars_before_people",
                '$ play_music("audio/music/ending_triumph.ogg", fadein=1.5)',
            ],
        )
        self.assertEqual(
            call_targets(route[people_end:post_start]), ["ending_epilogue_router"]
        )
        self.assertEqual(call_targets(post_block), ["ending_side_characters_fate"])
        self.assertEqual(
            call_targets(route),
            [
                "ending_side_characters_fate",
                "ending_epilogue_router",
                "ending_side_characters_fate",
            ],
        )

        actual_plans: dict[str, list[str]] = {}
        for ending_type in self.ENDING_TYPES:
            plan: list[str] = []
            if ending_type == "peoples_lord":
                plan.extend(call_targets(people_block))
            plan.extend(call_targets(route[people_end:post_start]))
            if ending_type not in ("sea", "peoples_lord"):
                plan.extend(call_targets(post_block))
            actual_plans[ending_type] = plan

        for ending_type, plan in actual_plans.items():
            with self.subTest(ending_type=ending_type):
                expected = (
                    ["ending_side_characters_fate", "ending_epilogue_router"]
                    if ending_type == "peoples_lord"
                    else ["ending_epilogue_router"]
                    if ending_type == "sea"
                    else ["ending_epilogue_router", "ending_side_characters_fate"]
                )
                self.assertEqual(plan, expected)
                self.assertEqual(plan.count("ending_epilogue_router"), 1)
                self.assertEqual(
                    plan.count("ending_side_characters_fate"),
                    0 if ending_type == "sea" else 1,
                )

    def test_side_character_content_remains_available_to_the_router(self) -> None:
        fates = label_body("endings_expansion.rpy", "ending_side_characters_fate")
        router = label_body("endings_expansion.rpy", "ending_epilogue_router").splitlines()
        people_start = find_source_line(router, 'elif ending_type == "peoples_lord":')
        people_block, _ = source_block(router, people_start)

        self.assertEqual(
            [line.strip() for line in people_block if line.strip()],
            ['elif ending_type == "peoples_lord":', "jump ending_peoples_epilogue"],
        )
        self.assertIn("马库斯的归宿", fates)
        self.assertIn("卡尔的归宿", fates)
        self.assertIn("if marcus_returned:", fates)
        self.assertIn('"战后第三个月, 你收到一封没有落款的信。"', fates)
        self.assertIn("if karl_returned:", fates)
        self.assertIn('"你确实抽空去过一次温特菲尔德村。"', fates)


class PeopleCoreContractTests(unittest.TestCase):
    def people_label_lines(self) -> list[str]:
        return label_body("chapter5.rpy", "ending_peoples_lord").splitlines()

    def people_core_lines(self) -> list[str]:
        people = self.people_label_lines()
        start = find_source_line(people, '"战后第五年。"')
        end = find_source_line(people, '$ unlock_achievement("peoples_lord")')
        return people[start:end]

    def test_core_people_ending_consumes_resources_and_buildings(self) -> None:
        people = self.people_label_lines()
        core = self.people_core_lines()
        wealth_start = find_source_line(core, "if wealth >= 60:")
        school_start = find_source_line(core, "if built_school:")
        granary_start = find_source_line(core, "if built_granary:")
        companions_start = find_source_line(core, "if elena_romance:")

        wealth_block = core[wealth_start:school_start]
        school_block = core[school_start:granary_start]
        granary_block = core[granary_start:companions_start]

        self.assertIn("else:", [line.strip() for line in wealth_block])
        self.assertIn("else:", [line.strip() for line in school_block])
        self.assertIn("else:", [line.strip() for line in granary_block])
        self.assertIn("学堂", "\n".join(school_block))
        self.assertNotIn("公仓", "\n".join(school_block))
        self.assertIn("公仓", "\n".join(granary_block))
        self.assertNotIn("学堂", "\n".join(granary_block))
        people_source = "\n".join(people)
        anchor = find_source_line(people, '"战后第五年。"')
        pre_anchor_source = "\n".join(people[:anchor])
        self.assertNotRegex(
            pre_anchor_source,
            r"(?:最繁忙的贸易中心|最繁荣的城镇|修建了新的房屋、道路和水渠)",
        )
        for unconditional_claim in (
            "地区最繁忙的贸易中心",
            "北方最繁荣的城镇",
            "修建了新的房屋、道路和水渠",
            "不需要担心战争、饥荒和压迫",
        ):
            with self.subTest(unconditional_claim=unconditional_claim):
                self.assertNotIn(unconditional_claim, people_source)

    def test_core_people_ending_consumes_every_companion_in_order(self) -> None:
        core = self.people_core_lines()
        companions_start = find_source_line(core, "if elena_romance:")
        closing_start = find_source_line(
            core, '"人民领主的故事后来越传越远，也越传越不像原样。"'
        )
        companions = core[companions_start:closing_start]
        direct = direct_source_branches(
            core, companions_start, closing_start, source_indent(core[companions_start])
        )
        self.assertEqual(
            [condition for condition, _ in direct],
            [
                "if elena_romance:",
                "elif marriage_route:",
                "elif corsair_romance:",
                "else:",
            ],
        )

        companion_source = "\n".join(companions)
        self.assertIn("英格丽", companion_source)
        self.assertIn("妻子", companion_source)
        self.assertIn("赛琳", companion_source)

        marriage_lines = direct[1][1]
        marriage_nested = direct_source_branches(
            marriage_lines, 1, len(marriage_lines), source_indent(marriage_lines[0]) + 4
        )
        self.assertEqual(
            [condition for condition, _ in marriage_nested],
            ["if marriage_warm:", "else:"],
        )

        corsair_lines = direct[2][1]
        corsair_nested = direct_source_branches(
            corsair_lines, 1, len(corsair_lines), source_indent(corsair_lines[0]) + 4
        )
        self.assertEqual(
            [condition for condition, _ in corsair_nested],
            ['if southern_outcome == "fall":', "else:"],
        )
        fall_source = "\n".join(corsair_nested[0][1])
        surviving_source = "\n".join(corsair_nested[1][1])
        self.assertIn("空处", fall_source)
        self.assertIn("没有捎来一个字", fall_source)
        self.assertIn("绳结", surviving_source)
        self.assertIn("商人", surviving_source)
        self.assertIn("没捎过话", surviving_source)
        self.assertNotIn("show corsair_img", "\n".join(corsair_lines))
        for direct_contact in ("一封", "信上", "回信", "驶进艾登堡"):
            with self.subTest(direct_contact=direct_contact):
                self.assertNotIn(direct_contact, fall_source)
                self.assertNotIn(direct_contact, surviving_source)


class PeopleExpansionContractTests(unittest.TestCase):
    def people_lines(self) -> list[str]:
        return label_body("endings_expansion.rpy", "ending_peoples_epilogue").splitlines()

    def household_branches(self) -> list[tuple[str, list[str]]]:
        lines = self.people_lines()
        start = find_source_line(lines, "## —— 第二幕半：留在身边的人 ——")
        end = find_source_line(lines, "## —— 第三幕：治理之道 ——")
        return direct_source_branches(lines, start + 1, end, 4)

    def test_expansion_material_conditions_have_direct_scoped_bodies(self) -> None:
        lines = self.people_lines()
        first_act_end = find_source_line(lines, "## —— 第二幕：奥尔德里克的告别 ——")
        opening = lines[:first_act_end]
        opening_source = "\n".join(opening)

        wealth_start = find_source_line(opening, "if wealth >= 60:")
        granary_start = find_source_line(opening, "if built_granary:")
        school_start = find_source_line(opening, "if built_school:")
        clinic_start = find_source_line(opening, "if built_clinic:")
        self.assertLess(wealth_start, granary_start)
        self.assertLess(granary_start, school_start)
        self.assertLess(school_start, clinic_start)

        wealth = direct_source_branches(opening, wealth_start, granary_start, 4)
        granary = direct_source_branches(opening, granary_start, school_start, 4)
        school = direct_source_branches(opening, school_start, clinic_start, 4)
        clinic = direct_source_branches(opening, clinic_start, first_act_end, 4)

        self.assertEqual([condition for condition, _ in wealth], ["if wealth >= 60:", "else:"])
        self.assertIn("领库也终于有余钱", source_without_comments(wealth[0][1]))
        self.assertNotIn("远称不上富庶", source_without_comments(wealth[0][1]))
        self.assertIn("远称不上富庶", source_without_comments(wealth[1][1]))
        self.assertNotIn("领库也终于有余钱", source_without_comments(wealth[1][1]))

        self.assertEqual([condition for condition, _ in granary], ["if built_granary:", "else:"])
        self.assertIn(
            "公仓门上挂着公开的收支牌", source_without_comments(granary[0][1])
        )
        self.assertNotIn(
            "新公仓一直没能建成", source_without_comments(granary[0][1])
        )
        self.assertIn(
            "新公仓一直没能建成", source_without_comments(granary[1][1])
        )
        self.assertNotIn(
            "公仓门上挂着公开的收支牌", source_without_comments(granary[1][1])
        )

        self.assertEqual([condition for condition, _ in school], ["if built_school:"])
        school_source = source_without_comments(school[0][1])
        self.assertIn("学堂", school_source)
        self.assertNotIn("诊所", school_source)
        self.assertNotIn("公仓", school_source)

        self.assertEqual([condition for condition, _ in clinic], ["if built_clinic:"])
        clinic_source = source_without_comments(clinic[0][1])
        self.assertIn("诊所新馆", clinic_source)
        self.assertNotIn("学堂", clinic_source)
        self.assertNotIn("公仓", clinic_source)

        self.assertNotIn('"第二天', opening_source)
        self.assertNotIn("整个王国最富庶、最和平的领地", opening_source)

    def test_expansion_households_advance_as_distinct_festival_or_home_events(self) -> None:
        direct = self.household_branches()
        self.assertEqual(
            [condition for condition, _ in direct],
            [
                "if elena_romance:",
                "elif marriage_route:",
                "elif corsair_romance:",
                "else:",
            ],
        )

        for condition, branch in direct:
            for index, line in enumerate(branch):
                if not line.strip().startswith("scene "):
                    continue
                previous = index - 1
                while previous >= 0 and (
                    not branch[previous].strip()
                    or branch[previous].lstrip().startswith("#")
                ):
                    previous -= 1
                with self.subTest(scene_clear=condition, scene=line.strip()):
                    self.assertGreaterEqual(previous, 0)
                    self.assertRegex(
                        branch[previous].strip(), r"^\$ hide_all_chars\([^)]*\)$"
                    )

        elena_lines = direct[0][1]
        elena_nested = direct_source_branches(
            elena_lines,
            1,
            len(elena_lines),
            source_indent(elena_lines[0]) + 4,
        )
        self.assertEqual(
            [condition for condition, _ in elena_nested],
            ["if rel_elena >= 50:", "else:"],
        )
        first_elena_nested = elena_lines.index(elena_nested[0][1][0])
        self.assertIn("苹果木牌", "\n".join(elena_lines[:first_elena_nested]))
        self.assertIn("牵住你的手", "\n".join(elena_nested[0][1]))
        self.assertIn("独自走向舞圈", "\n".join(elena_nested[1][1]))

        marriage_lines = direct[1][1]
        marriage_nested = direct_source_branches(
            marriage_lines,
            1,
            len(marriage_lines),
            source_indent(marriage_lines[0]) + 4,
        )
        self.assertEqual(
            [condition for condition, _ in marriage_nested],
            ["if marriage_warm:", "else:"],
        )
        first_nested = marriage_lines.index(marriage_nested[0][1][0])
        marriage_preamble = "\n".join(marriage_lines[:first_nested])
        self.assertIn("妻子", marriage_preamble)
        self.assertRegex(marriage_preamble, r"家|家庭")
        warm_source = "\n".join(marriage_nested[0][1])
        cold_source = "\n".join(marriage_nested[1][1])
        self.assertIn("挽着你的手", warm_source)
        self.assertIn("两双沾了泥的鞋", warm_source)
        self.assertNotIn("长桌两端", warm_source)
        self.assertIn("一前一后", cold_source)
        self.assertIn("长桌两端", cold_source)
        self.assertNotIn("挽着你的手", cold_source)
        self.assertNotIn("hide ingrid_img", cold_source)

        household_source = "\n".join(
            line for _, branch in direct for line in branch
        )
        self.assertIn("艾琳娜", household_source)
        self.assertIn("英格丽", household_source)
        self.assertIn("赛琳", household_source)
        self.assertNotRegex(
            household_source, r"你们的孩子|你们的儿女|生下|生了|继承人"
        )
        self.assertNotRegex(
            household_source,
            r"盐价表|共用的书桌|绳头|绳结|南边来的商人|水渠|面粉",
        )
        self.assertIn("门房一家", "\n".join(direct[3][1]))
        self.assertIn("独自上楼", "\n".join(direct[3][1]))

    def test_corsair_household_has_state_specific_event_without_direct_contact(self) -> None:
        corsair_lines = self.household_branches()[2][1]
        nested = direct_source_branches(
            corsair_lines,
            1,
            len(corsair_lines),
            source_indent(corsair_lines[0]) + 4,
        )
        self.assertEqual(
            [condition for condition, _ in nested],
            ['if southern_outcome == "fall":', "else:"],
        )
        fall_source = "\n".join(nested[0][1])
        surviving_source = "\n".join(nested[1][1])
        self.assertIn("第一段结束前", fall_source)
        self.assertIn("从侧巷回了城堡", fall_source)
        self.assertNotIn("把曲子听完", fall_source)
        self.assertIn("把曲子听完", surviving_source)
        self.assertIn("杯沿", surviving_source)
        self.assertNotIn("从侧巷回了城堡", surviving_source)

        corsair_source = "\n".join(corsair_lines)
        corsair_tag = character_image_tag("corsair", "southern_expansion.rpy")
        self.assertIn("你在副歌里想起赛琳", corsair_source)
        self.assertIsNone(SELENE_CHARACTER_DIALOGUE_RE.search(corsair_source))
        self.assertNotRegex(
            corsair_source,
            rf"(?m)^\s*show\s+{re.escape(corsair_tag)}\b",
        )
        self.assertIsNone(SELENE_DIRECT_REUNION_RE.search(corsair_source))
        self.assertIsNone(SELENE_DIRECT_DELIVERY_RE.search(corsair_source))

        for legal_indirect_news in (
            "商人说她仍在南方航海。",
            "商人说她回到潮汐港继续航海。",
            "有人从潮汐港听到赛琳还活着的传闻。",
            "商人捎来关于她的消息。",
        ):
            with self.subTest(legal_indirect_news=legal_indirect_news):
                self.assertIsNone(SELENE_DIRECT_REUNION_RE.search(legal_indirect_news))
                self.assertIsNone(SELENE_DIRECT_DELIVERY_RE.search(legal_indirect_news))

    def test_delegation_uses_known_lord_title_without_unexplained_ranks(self) -> None:
        lines = self.people_lines()
        start = find_source_line(lines, "## —— 第三幕：治理之道 ——")
        end = find_source_line(lines, "## —— 第四幕：黄昏漫步 ——")
        delegation = "\n".join(lines[start:end])

        self.assertIn("领主大人，克恩伯爵派我们来向您请教治理之道", delegation)
        self.assertIn("多谢领主大人赐教", delegation)
        self.assertNotRegex(delegation, r"大公|公爵|侯爵|子爵|男爵")
        self.assertNotRegex(
            delegation, r"(?:大公|公爵|侯爵|伯爵|子爵|男爵)大人"
        )

    def test_festival_chronology_ends_on_the_second_day_for_every_household(self) -> None:
        people = self.people_lines()
        household_end = find_source_line(people, "## —— 第三幕：治理之道 ——")
        final_act = find_source_line(people, "## —— 第五幕：晚年与远讯 ——")
        second_day_source = "\n".join(people[household_end:final_act])

        self.assertEqual(second_day_source.count("丰收节的第二天"), 1)
        self.assertRegex(
            second_day_source,
            r"第二天黄昏[^\n]*为期两天的丰收节[^\n]*尾声",
        )

    def test_reform_and_dark_lily_copy_uses_concrete_natural_actions(self) -> None:
        people = "\n".join(self.people_lines())

        self.assertNotIn("列席权仍被拖延", people)
        self.assertIn("村社代表列席议事的提案仍被搁置", people)
        self.assertNotIn("接受同一种去处", people)
        self.assertIn("不愿公开的人可以离开，不再参与监察", people)

    def test_national_change_identifies_coalition_content_charge_and_retry(self) -> None:
        people = label_body("endings_expansion.rpy", "ending_peoples_epilogue")
        for marker in (
            "城镇行会",
            "村社推举的代表",
            "愿意公开账目的小领主",
            "公开地租与税款去向",
            "列席地方议事",
            "被控『煽动抗税』",
            "把提案拆成两份",
            "先接受了公开账目",
            "撤下公示牌",
            "驳回卷宗",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, people)

        self.assertNotIn("艾登堡没有替整个王国作答", people)
        self.assertNotIn("艾登堡只在史册边缘留下一个较早的例子", people)
        self.assertNotIn("几十个领地的代表坐在一张桌上，一条条把旧律改了", people)

    def test_posthumous_tail_contains_no_protagonist_second_person_reference(self) -> None:
        people = label_body("endings_expansion.rpy", "ending_peoples_epilogue")
        self.assertNotIn("transform father_son_slow_push", people)
        death_line = '"你是在一个平凡的春日清晨走的。"'
        self.assertEqual(people.count(death_line), 1)
        after_death = people.split(death_line, 1)[1]

        self.assertNotRegex(after_death, r"(?m)^\s*player\s+[\"']")
        self.assertNotRegex(after_death, r"[你您]")
        for subject in ("村社", "地方议会", "史家", "王后", "男爵", "弗雷德里克", "暗百合", "雷恩"):
            with self.subTest(subject=subject):
                self.assertIn(subject, after_death)

    def test_posthumous_tail_consumes_each_surviving_state_directly(self) -> None:
        lines = self.people_lines()
        queen_start = find_source_line(lines, "if queen_trust:")
        baron_start = find_source_line(lines, "if baron_peace_path:")
        prince_start = find_source_line(lines, "if prince_ally:")
        lily_start = find_source_line(lines, "if dark_lily_joined:")
        rayn_start = find_source_line(
            lines,
            '"雷恩把守军改成了小规模常备队与村社轮值并存。有人嫌村社轮值遇警时集结太慢，他只说，百姓需要的是能回家种地的兵，不是另一支只听一个人命令的私军。"',
        )

        queen = direct_source_branches(lines, queen_start, baron_start, 4)
        baron = direct_source_branches(lines, baron_start, prince_start, 4)
        prince = direct_source_branches(lines, prince_start, lily_start, 4)
        lily = direct_source_branches(lines, lily_start, rayn_start, 4)

        self.assertEqual(
            [condition for condition, _ in queen], ["if queen_trust:", "else:"]
        )
        self.assertIn("退出议会", "\n".join(queen[0][1]))
        self.assertIn("拒绝了最初几轮让步", "\n".join(queen[1][1]))

        self.assertEqual(
            [condition for condition, _ in baron],
            ["if baron_peace_path:", "else:"],
        )
        self.assertIn("地方议会代表", "\n".join(baron[0][1]))
        self.assertIn("组织过抵抗", "\n".join(baron[1][1]))

        self.assertEqual(
            [condition for condition, _ in prince], ["if prince_ally:", "else:"]
        )
        self.assertIn("化名去了南方教书", "\n".join(prince[0][1]))
        self.assertIn("流亡海外", "\n".join(prince[1][1]))

        self.assertEqual(
            [condition for condition, _ in lily],
            ["if dark_lily_joined:", "elif dark_lily_destroyed:", "else:"],
        )
        self.assertIn("公开监察员", "\n".join(lily[0][1]))
        self.assertIn("早已覆灭", "\n".join(lily[1][1]))
        self.assertIn("没有在一夜间消失", "\n".join(lily[2][1]))


if __name__ == "__main__":
    unittest.main()

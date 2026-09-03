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
    """Return live source text without comments outside quoted strings."""
    live_lines: list[str] = []
    for line in lines:
        quote: str | None = None
        escaped = False
        comment_at: int | None = None
        for index, char in enumerate(line):
            if escaped:
                escaped = False
                continue
            if quote is not None and char == "\\":
                escaped = True
                continue
            if char in ("\"", "'"):
                if quote is None:
                    quote = char
                elif quote == char:
                    quote = None
                continue
            if char == "#" and quote is None:
                comment_at = index
                break

        live_line = line if comment_at is None else line[:comment_at].rstrip()
        if live_line.strip() or not line.strip():
            live_lines.append(live_line)
    return "\n".join(live_lines)


def live_source_lines(lines: list[str]) -> tuple[str, ...]:
    """Return nonblank executable lines after quote-aware comment removal."""
    return tuple(
        line.rstrip()
        for line in source_without_comments(lines).splitlines()
        if line.strip()
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
_SELENE_ACTOR = r"(?:赛琳|她)(?:本人)?(?!本人|的)"
_SELENE_LETTER_AUTHORSHIP = (
    r"(?:赛琳|她)(?:本人)?(?:亲手)?"
    r"(?:的(?:来信|信|口信|字条|包裹)|"
    r"(?:写|寄|捎|送)来(?:的)?(?:来信|信|口信|字条|包裹)|来信)"
)
_SELENE_TEXT_SEGMENT_RE = re.compile(r"[^。！？!?；;\n]+")
_SELENE_REPORT_CUE_RE = re.compile(
    r"(?:(?:商人|水手|船员|旅人|有人)[^，,。！？!?；;\n]{0,4}"
    r"(?:说|称|提到|听到|告诉)|听说|据说|传闻|消息)"
)
_SELENE_DIRECT_REUNION_PATTERNS = (
    re.compile(
        rf"(?P<selene>{_SELENE_ACTOR})[^。！？!?；;\n]{{0,20}}"
        r"(?P<action>来到|走进|走到|站在|出现|抵达|回到|驶入|登上|"
        r"(?:与|和)你(?:相见|重逢|跳舞|同行)|牵住你|挽住你|拥抱你|吻你)"
    ),
    re.compile(
        rf"你[^。！？!?；;\n]{{0,8}}(?:与|和)(?P<selene>{_SELENE_ACTOR})"
        r"[^。！？!?；;\n]{0,8}(?P<action>相见|重逢|跳舞|同行|拥抱)"
    ),
    re.compile(
        rf"你[^。！？!?；;\n]{{0,12}}"
        r"(?P<action>见到|看见|遇见|碰见|迎到|等到)了?"
        rf"(?P<selene>{_SELENE_ACTOR})"
    ),
)
_SELENE_DIRECT_DELIVERY_PATTERNS = (
    re.compile(
        rf"(?P<selene>{_SELENE_ACTOR})[^，,。！？!?；;\n]{{0,8}}"
        r"(?P<action>送来|捎来|寄来|带来|递来|送到|捎到|寄到|带到|递到)"
        r"[^，,。！？!?；;\n]{0,8}(?:信|口信|字条|包裹|消息)"
    ),
    re.compile(
        r"你[^，,。！？!?；;\n]{0,12}"
        r"(?P<action>收到|接到|拿到|读到|拆开)"
        rf"[^，,。！？!?；;\n]{{0,12}}"
        rf"(?P<selene>{_SELENE_LETTER_AUTHORSHIP})"
    ),
)


def _has_unreported_selene_contact(
    text: str, patterns: tuple[re.Pattern[str], ...]
) -> bool:
    """Return whether a sentence segment contains Selene's direct action."""
    for segment_match in _SELENE_TEXT_SEGMENT_RE.finditer(text):
        segment = segment_match.group(0)
        report_cues = tuple(_SELENE_REPORT_CUE_RE.finditer(segment))
        for pattern in patterns:
            for contact in pattern.finditer(segment):
                selene_start = contact.start("selene")
                if not any(report.start() < selene_start for report in report_cues):
                    return True
    return False


def has_selene_direct_reunion(text: str) -> bool:
    return _has_unreported_selene_contact(text, _SELENE_DIRECT_REUNION_PATTERNS)


def has_selene_direct_delivery(text: str) -> bool:
    return _has_unreported_selene_contact(text, _SELENE_DIRECT_DELIVERY_PATTERNS)


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
    def test_source_without_comments_strips_inline_comments_but_preserves_hashes_in_strings(self) -> None:
        lines = [
            "    # whole-line comment",
            "    $ _review_probe = True  # stripped marker",
            "    $ compact = 1# stripped without space",
            '    "double # stays"  # stripped tail',
            "    'single # stays'  # stripped tail",
            r'    player "escaped \"quote # stays\""  # stripped tail',
            r"    player 'escaped \'quote # stays\''  # stripped tail",
            '    $ color = "#fff"  # stripped palette note',
            "    $ label = \"apostrophe ' and hash # stay\"  # comment \" quote",
        ]

        self.assertEqual(
            source_without_comments(lines),
            "\n".join(
                [
                    "    $ _review_probe = True",
                    "    $ compact = 1",
                    '    "double # stays"',
                    "    'single # stays'",
                    r'    player "escaped \"quote # stays\""',
                    r"    player 'escaped \'quote # stays\''",
                    '    $ color = "#fff"',
                    "    $ label = \"apostrophe ' and hash # stay\"",
                ]
            ),
        )

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

        self.assertTrue(has_selene_direct_reunion("她来到广场，与你跳舞。"))
        self.assertTrue(has_selene_direct_reunion("赛琳和你重逢。"))
        self.assertTrue(has_selene_direct_delivery("她捎来信。"))
        self.assertTrue(has_selene_direct_reunion("她听完消息后来到广场。"))
        self.assertTrue(has_selene_direct_delivery("她听完消息后捎来信。"))
        self.assertFalse(has_selene_direct_reunion("商人说她回到潮汐港继续航海。"))

    def test_selene_recipient_first_direct_letter_is_not_indirect_news(self) -> None:
        self.assertTrue(has_selene_direct_delivery("你收到一封赛琳的来信。"))

        for legal_indirect_news in (
            "你收到商人的来信，信里说赛琳仍在南方航海。",
            "商人说他收到过赛琳的来信。",
        ):
            with self.subTest(legal_indirect_news=legal_indirect_news):
                self.assertFalse(has_selene_direct_delivery(legal_indirect_news))

    def test_selene_protagonist_first_pronominal_meeting_is_not_indirect_news(self) -> None:
        self.assertTrue(has_selene_direct_reunion("你在广场见到了她。"))
        self.assertTrue(
            has_selene_direct_reunion(
                "商人说完消息。她随后来到广场，与你跳舞。"
            )
        )

        for legal_indirect_news in (
            "商人告诉你，他在潮汐港见到了她。",
            "有人说他在南方见到过赛琳。",
            "你听说他见到了她。",
        ):
            with self.subTest(legal_indirect_news=legal_indirect_news):
                self.assertFalse(has_selene_direct_reunion(legal_indirect_news))

    def test_selene_possessive_people_and_objects_are_not_direct_contact(self) -> None:
        for legal_possessive_reference in (
            "你在广场见到了她的船员。",
            "她的船员捎来消息。",
            "你收到赛琳的船员寄来的信。",
            "你在码头看见了赛琳的旧船。",
            "她本人的船员捎来消息。",
            "你在码头看见了赛琳本人的旧船。",
        ):
            with self.subTest(legal_possessive_reference=legal_possessive_reference):
                self.assertFalse(
                    has_selene_direct_reunion(legal_possessive_reference)
                )
                self.assertFalse(
                    has_selene_direct_delivery(legal_possessive_reference)
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
        chapter_lines = live_source_lines(chapter.splitlines())
        baron_envoy_tag = character_image_tag("baron_envoy")
        self.assertRegex(chapter, rf'(?s)show {re.escape(baron_envoy_tag)}[^\n]*\n\s*baron_envoy ')
        departure_narration = '"送走了男爵的密使后，你以为这一天的访客到头了。"'
        departure_index = find_source_line(chapter_lines, departure_narration)
        self.assertEqual(
            chapter_lines[departure_index - 1].strip(),
            f"hide {baron_envoy_tag} with dissolve",
        )
        self.assertRegex(chapter, r'她那天夜里离开了艾登堡。没有告诉你她去哪。"\s*\n\s*hide elena_img')

    def test_peace_montage_clears_the_last_negotiating_representative(self) -> None:
        chapter_lines = live_source_lines(read_game_file("chapter5.rpy").splitlines())
        peace_montage = '"又一轮讨价还价。但这次，方向已经明确了——和平。"'
        peace_montage_index = find_source_line(chapter_lines, peace_montage)
        self.assertEqual(
            chapter_lines[peace_montage_index - 1].strip(), "$ hide_all_chars()"
        )
        self.assertEqual(
            chapter_lines[peace_montage_index - 2].strip(),
            'baron_rep "男爵阁下原则上同意。但需要在第三条中加入——"',
        )


class MarriageContractTests(unittest.TestCase):
    def test_chapter_three_opens_talks_without_accepting_marriage(self) -> None:
        lines = label_body("chapter3.rpy", "ch3_end").splitlines()
        choice_start = find_source_line(lines, '"回信，答应在王都会面":')
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
                "接受婚约，除此之外不作承诺",
                "接受婚约，问英格丽本人的打算",
                "拒绝婚约，结束商谈",
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
        decline_start = find_source_line(palace_lines, '"拒绝婚约，结束商谈":')
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
                ("告诉她你已答应北境婚约", "marriage_route"),
                ("感谢她的付出，但保持距离", "not marriage_route"),
            ],
        )
        marriage_body = outcomes[2][2]
        self.assertIn(
            'player "艾琳娜，我在使馆答应了英格丽。婚礼还没办，但我已经对她应下这门婚事。"',
            [line.strip() for line in marriage_body],
        )
        self.assertIn(
            'player "既然她也答应了这桩婚事，我就不能转过身来，再接下你的心意。"',
            [line.strip() for line in marriage_body],
        )

    def test_marriage_copy_preserves_ingrids_agency_and_separates_talks_from_wedding(self) -> None:
        palace = label_body("chapter4.rpy", "ch4_palace")
        self.assertIn("你肯来，至少说明你没有把母亲的信当成婚书。", palace)
        self.assertIn("母亲把我送到这里，是让我自己开口。", palace)
        self.assertIn("别因为我住进来多添一袋粮。", palace)
        self.assertIn("这是我来听的答复。我收下。", palace)
        self.assertIn("婚事的提议，到此为止。", palace)
        self.assertNotIn("盟书草案留下", palace)
        self.assertNotIn("这是我们共同的命运", palace)
        self.assertNotIn("从现在起，你就是我的妻子", palace)
        self.assertNotIn("$ wedding_attended = True", palace)
        self.assertIn("婚礼还没办", label_body("chapter4.rpy", "ch4_elena"))


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

    def test_people_core_closes_without_a_second_year_jump(self) -> None:
        people = ending_section("chapter5.rpy", "ending_peoples_lord")
        self.assertIn(
            '"广场上又有人为水渠拍了桌子。"',
            people,
        )
        self.assertIn(
            '"五年前的旗帜早已收进库房。大厅的桌上，摊开的仍是欠租、修桥和水渠。"',
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
        self.assertIn("[iron_battle_dead]人", iron)
        self.assertNotIn("两百多人", iron)
        self.assertNotIn("七十多人", iron)
        self.assertNotIn("三百七十二", iron)

    def test_iron_route_consumes_governance_and_expansion_preparation(self) -> None:
        chapter5 = read_game_file("chapter5.rpy")
        for state in (
            "ch5_exp_defender_bonus",
            "ch5_exp_skirmish_result",
            "ch5_exp_enemy_morale_hit",
            "ch5_exp_casualties",
            "ch5_exp_deserter_intel",
            "ch5_exp_war_strategy",
            "ch5_exp_final_formation",
            "famine_prevented",
            "built_granary",
            "governance_prosperity",
        ):
            self.assertIn(state, chapter5)
        self.assertIn("iron_player_regulars =", chapter5)
        self.assertIn("iron_total_troops =", chapter5)
        self.assertIn("iron_battle_dead = max", chapter5)
        self.assertNotIn("同时迎战两路大军", chapter5)

    def test_baron_can_be_broken_before_the_royal_battle(self) -> None:
        expansion = read_game_file("chapter5_expansion.rpy")
        self.assertIn("baron_field_power_broken = True", expansion)
        self.assertIn("northern_lords_unified = True", expansion)
        self.assertIn("拆掉了把他们绑在一起的那只手", expansion)

    def test_self_rule_variant_resolves_the_barbarians(self) -> None:
        chapter5 = read_game_file("chapter5.rpy")
        epilogue = read_game_file("endings_expansion.rpy")
        self.assertIn("self_rule_declared = True", chapter5)
        self.assertIn("顺应人心，宣告北境自立", chapter5)
        self.assertIn("jump ending_iron_self_rule_epilogue", epilogue)
        self.assertIn("label ending_iron_self_rule_epilogue:", epilogue)
        self.assertIn("三万蛮兵重新结盟", epilogue)
        self.assertIn("北境证明了自己能把三万人挡在村庄之外", epilogue)

    def test_popular_famine_solution_records_survival(self) -> None:
        governance = read_game_file("governance.rpy")
        choice = governance.index("亲自下村组织自救")
        outcome = governance.index("三周后春雨来了", choice)
        self.assertIn("$ famine_prevented = True", governance[choice:outcome])


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

    def test_core_people_ending_opens_with_costs_before_recovery(self) -> None:
        people = "\n".join(self.people_label_lines())
        self.assertIn("城墙完整地立着，但城墙以外的一切都付出了代价。", people)
        self.assertIn("这场仗没有被谁赢下", people)
        self.assertIn("今夜先让他们有地方睡。桥和集市的账，明天再算。", people)
        self.assertNotIn("整个北方只有一个领地没有被战火摧毁", people)
        self.assertNotIn("人们叫你『父亲』", people)
        self.assertNotIn("没有阵营之分——只有需要保护的人", people)
        self.assertNotIn("想为您立一座铜像", people)
        self.assertNotIn("就是你们的日子", people)
        self.assertNotIn("补充兵员", people)
        self.assertNotIn("来年该补多少", people)
        self.assertIn(
            "你没有坐上王座。五年后，艾登堡仍要收租、修桥、分水，也仍允许村民来大厅争这些事。",
            read_game_file("chapter5.rpy"),
        )

    def test_core_people_ending_consumes_every_companion_in_order(self) -> None:
        core = self.people_core_lines()
        companions_start = find_source_line(core, "if elena_romance:")
        closing_start = find_source_line(
            core, '"广场上又有人为水渠拍了桌子。"'
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
        self.assertIn("婚后", companion_source)
        self.assertIn("赛琳", companion_source)
        self.assertIn("门房一家", companion_source)
        self.assertNotIn("仍是你的妻子", companion_source)
        self.assertNotIn("没有替你预备好的家庭", companion_source)

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
        self.assertIn("婚后五年", marriage_preamble)
        self.assertIn("家书", marriage_preamble)
        self.assertNotIn("以你的妻子身份", marriage_preamble)
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

    def test_corsair_household_live_source_matches_canonical_snapshot(self) -> None:
        corsair_lines = self.household_branches()[2][1]
        actual_live_lines = live_source_lines(corsair_lines)
        canonical_live_lines = (
            "    elif corsair_romance:",
            "        $ hide_all_chars()",
            "        scene bg village with dissolve",
            "        $ hide_all_chars()",
            '        "广场边，一队外乡乐师奏起潮汐港的旧曲。你在副歌里想起赛琳，却没有上前打听曲子的来处。"',
            '        if southern_outcome == "fall":',
            '            "第一段结束前，你放下没喝完的苹果酒，从侧巷回了城堡。"',
            '            "门廊的灯还亮着。你让门房关上外门，自己上楼；那支曲子没有跟进来。"',
            "        else:",
            '            "你站在人群外把曲子听完。乐师漏掉换拍时，你用杯沿轻轻补了三下。"',
            '            "最后一个音落下，你把空杯放进木盘，跟着散场的人群走回城堡。"',
        )

        self.assertSequenceEqual(
            actual_live_lines,
            canonical_live_lines,
            "Corsair live-source mismatch: first sequence is actual; "
            "second is canonical expected",
        )

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
        self.assertFalse(has_selene_direct_reunion(corsair_source))
        self.assertFalse(has_selene_direct_delivery(corsair_source))

        for legal_indirect_news in (
            "商人说她仍在南方航海。",
            "商人说她回到潮汐港继续航海。",
            "有人从潮汐港听到赛琳还活着的传闻。",
            "商人捎来关于她的消息。",
        ):
            with self.subTest(legal_indirect_news=legal_indirect_news):
                self.assertFalse(has_selene_direct_reunion(legal_indirect_news))
                self.assertFalse(has_selene_direct_delivery(legal_indirect_news))

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
        household_start = find_source_line(
            people, "## —— 第二幕半：留在身边的人 ——"
        )
        household_end = find_source_line(people, "## —— 第三幕：治理之道 ——")
        final_act = find_source_line(people, "## —— 第五幕：晚年与远讯 ——")
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

        corsair_lines = direct[2][1]
        corsair_nested = direct_source_branches(
            corsair_lines,
            1,
            len(corsair_lines),
            source_indent(corsair_lines[0]) + 4,
        )
        self.assertEqual(
            [condition for condition, _ in corsair_nested],
            ['if southern_outcome == "fall":', "else:"],
        )

        early_day_jump = re.compile(
            r"(?:第二天|第二日|次日|翌日|隔天|次晨|翌晨|一夜(?:之后|过去|过后))"
        )
        household_variants = (
            ("Elena", direct[0][1]),
            ("Ingrid full branch", direct[1][1]),
            ("Ingrid warm", marriage_nested[0][1]),
            ("Ingrid cold", marriage_nested[1][1]),
            ("Corsair full branch", direct[2][1]),
            ("Corsair fall", corsair_nested[0][1]),
            ("Corsair non-fall", corsair_nested[1][1]),
            ("no partner", direct[3][1]),
        )
        for variant, branch in household_variants:
            with self.subTest(variant=variant):
                self.assertNotRegex(source_without_comments(branch), early_day_jump)

        household_source = source_without_comments(
            people[household_start:household_end]
        )
        self.assertNotRegex(household_source, early_day_jump)

        second_day_line = (
            '"丰收节的第二天。一支来自南方克恩伯爵领的代表团抵达了艾登堡。"'
        )
        second_day_start = find_source_line(people, second_day_line)
        self.assertGreater(second_day_start, household_end)
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
        self.assertIn("这本账上只有总数。你们平时就凭这个收租？", people)
        self.assertIn("往年新麦先拿去抵租。今年交完，还剩了这一袋。", people)
        self.assertNotIn("这是我吃过的最好的面包", people)
        for unexplained_or_modern_term in (
            "节签",
            "旧地租和新地租",
            "征集签名",
            "查账期限",
            "刊出",
            "补还日期",
            "每季必须查账",
            "临时征发",
            "一套能带回去的办法",
            "分工很清楚",
        ):
            with self.subTest(unexplained_or_modern_term=unexplained_or_modern_term):
                self.assertNotIn(unexplained_or_modern_term, people)

        self.assertRegex(people, r"各村[^。\n]*代表")
        self.assertRegex(people, r"账房[^。\n]*(?:收支|账)[^。\n]*(?:广场|公示)")
        self.assertNotIn("领主之位由谁接手", people)
        self.assertNotIn("地方议会按旧章程补上空位", people)
        self.assertIn("代表们带着旧账和旧章程守在大厅门外", people)
        self.assertNotIn("拒绝在新税册上按印", people)

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
            "封口已经裂开",
            "每封信按日期压在艾登堡的账册下面",
            "艾登堡那一页最脏",
            "守门人让开了门",
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
        self.assertIn("暗百合", "\n".join(queen[0][1]))
        self.assertNotIn("没有再下令阻拦", "\n".join(queen[0][1]))
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


class MissingEndingContractTests(unittest.TestCase):
    def married_outcome(self, label: str) -> list[str]:
        lines = label_body("chapter5.rpy", label).splitlines()
        direct_indent = min(source_indent(line) for line in live_source_lines(lines))
        matches = [
            index
            for index, line in enumerate(lines)
            if source_indent(line) == direct_indent
            and re.fullmatch(r"(?:if|elif) marriage_route:", line.strip())
        ]
        self.assertEqual(
            len(matches),
            1,
            f"{label} must contain one reachable marriage_route outcome branch",
        )
        branch, _ = source_block(lines, matches[0])
        return branch

    def assert_substantive_ingrid_outcome(
        self, label: str, temperature: str, branch: list[str]
    ) -> None:
        outcome_lines = live_source_lines(branch[1:])

        self.assertTrue(
            any(
                re.match(r"ingrid\s+[\x22']", line.strip()) is not None
                or (
                    line.strip().startswith(('"', "'"))
                    and "英格丽" in line
                )
                for line in outcome_lines
            ),
            (
                f"{label} {temperature} marriage outcome must contain an Ingrid "
                "dialogue or narration statement"
            ),
        )

    def assert_ingrid_marriage_outcomes(self, label: str) -> None:
        branch = self.married_outcome(label)
        branch_source = source_without_comments(branch)

        self.assertRegex(branch_source, r"(?:\bingrid\b|英格丽)")
        nested = direct_source_branches(
            branch, 1, len(branch), source_indent(branch[0]) + 4
        )
        self.assertEqual(
            [condition for condition, _ in nested],
            ["if marriage_warm:", "else:"],
            f"{label} must structurally provide warm and cold married outcomes",
        )
        self.assert_substantive_ingrid_outcome(label, "warm", nested[0][1])
        self.assert_substantive_ingrid_outcome(label, "cold", nested[1][1])

    def test_people_lord_retains_rear_army_withdrawal_causality(self) -> None:
        people = label_body("chapter5.rpy", "ending_peoples_lord")
        lines = people.splitlines()
        speech = find_source_line(lines, 'player "而是熬到了最后的人。"')
        next_scene = next(
            index
            for index in range(speech + 1, len(lines))
            if lines[index].strip() == "scene bg castle_exterior with dissolve"
        )
        post_speech_lines = lines[speech + 1 : next_scene]
        post_speech_bridge = source_without_comments(post_speech_lines)
        narration_paragraphs = [
            line.strip()
            for line in live_source_lines(post_speech_lines)
            if re.fullmatch(r'"(?:[^"\\]|\\.)*"', line.strip())
        ]

        self.assertRegex(people, r"另一支军队.*后方出现.*迫使.*撤退")
        self.assertNotIn("你击退了每一支试图劫掠你领地的军队", people)
        self.assertEqual(len(narration_paragraphs), 3)
        for replay_marker in ("第三天", "号角", "后方", "撤退"):
            with self.subTest(replay_marker=replay_marker):
                self.assertNotIn(replay_marker, post_speech_bridge)
        for duplicate_or_downstream_marker in (
            "战争结束得很难看",
            "艾登堡守住了城门",
            "流民",
            "手艺",
            "修路",
            "集市",
            "马厩",
        ):
            with self.subTest(marker=duplicate_or_downstream_marker):
                self.assertNotIn(duplicate_or_downstream_marker, post_speech_bridge)

    def test_truth_humble_epilogue_reaches_both_ingrid_marriage_outcomes(self) -> None:
        self.assert_ingrid_marriage_outcomes("truth_humble_epilogue")

    def test_borgia_ending_reaches_both_ingrid_marriage_outcomes(self) -> None:
        self.assert_ingrid_marriage_outcomes("ending_borgia")

    def test_sea_ending_reaches_both_ingrid_marriage_outcomes(self) -> None:
        self.assert_ingrid_marriage_outcomes("ending_sea")

    def test_sea_ending_prioritizes_marriage_over_corsair_reunion(self) -> None:
        lines = label_body("chapter5.rpy", "ending_sea").splitlines()
        guard = find_source_line(
            lines, "if corsair_romance and not marriage_route:"
        )
        branches = direct_source_branches(
            lines, guard, len(lines), source_indent(lines[guard])
        )

        self.assertEqual(
            [condition for condition, _ in branches],
            ["if corsair_romance and not marriage_route:", "else:"],
        )

    def test_sea_extended_epilogue_prioritizes_marriage_over_corsair_reunion(
        self,
    ) -> None:
        lines = label_body("endings_expansion.rpy", "ending_sea_epilogue").splitlines()
        direct_indent = min(source_indent(line) for line in live_source_lines(lines))
        direct_guards = [
            index
            for index, line in enumerate(lines)
            if source_indent(line) == direct_indent
            and re.fullmatch(r"if .+:", line.strip())
        ]

        self.assertEqual(len(direct_guards), 1)
        guard = direct_guards[0]
        self.assertEqual(
            lines[guard].strip(), "if corsair_romance and not marriage_route:"
        )
        branches = direct_source_branches(lines, guard, len(lines), direct_indent)
        self.assertEqual(
            [condition for condition, _ in branches],
            ["if corsair_romance and not marriage_route:", "else:"],
        )

    def test_sea_ending_router_directly_enters_the_extended_epilogue(self) -> None:
        lines = list(
            live_source_lines(
                label_body("endings_expansion.rpy", "ending_epilogue_router").splitlines()
            )
        )
        direct_indent = min(source_indent(line) for line in lines)
        sea_branch = find_source_line(lines, 'elif ending_type == "sea":')

        self.assertEqual(source_indent(lines[sea_branch]), direct_indent)
        self.assertLess(sea_branch + 1, len(lines))
        self.assertEqual(
            lines[sea_branch + 1].strip(), "jump ending_sea_epilogue"
        )
        self.assertEqual(
            source_indent(lines[sea_branch + 1]), source_indent(lines[sea_branch]) + 4
        )

    def test_sea_warm_marriage_distinguishes_both_letters_and_the_ring(
        self,
    ) -> None:
        lines = label_body("chapter5.rpy", "ending_sea").splitlines()
        marriage_start = find_source_line(lines, "if marriage_route:")
        departure_preamble = source_without_comments(lines[:marriage_start])
        marriage_branch = self.married_outcome("ending_sea")
        nested = direct_source_branches(
            marriage_branch,
            1,
            len(marriage_branch),
            source_indent(marriage_branch[0]) + 4,
        )
        warm_source = source_without_comments(nested[0][1])

        self.assertRegex(
            departure_preamble,
            r"奥尔德里克[\s\S]*印戒在信封里[\s\S]*信放在书桌正中",
        )
        self.assertRegex(
            warm_source,
            r"(?:英格丽房门[\s\S]{0,240}(?:第二封信|短笺)|"
            r"(?:第二封信|短笺)[\s\S]{0,240}(?:英格丽|房门|门缝))",
        )
        self.assertNotIn("把信和印戒一并交到奥尔德里克手上", warm_source)
        self.assertIn("你", warm_source)
        self.assertNotIn("婚姻的漫长年月", warm_source)
        self.assertNotRegex(
            warm_source,
            r"(?:^|[\s，。！？——\x22'])他(?:把|将|另|吹|背|回|走|知道)",
        )
        for repeated_preamble_action in (
            r"(?:封好|滴上)蜡",
            r"(?:把|将)[^。！？\n]{0,80}(?:第一封信|给奥尔德里克的信|这封信)"
            r"[^。！？\n]{0,30}(?:放|摆|搁)[^。！？\n]{0,20}书桌",
            r"(?:把|将)[^。！？\n]{0,40}金鹰印戒[^。！？\n]{0,30}"
            r"(?:裹|塞|放)[^。！？\n]{0,20}(?:信纸|信封)",
        ):
            with self.subTest(repeated_preamble_action=repeated_preamble_action):
                self.assertNotRegex(warm_source, repeated_preamble_action)
        for premature_departure_action in (
            r"(?:收拾|背起|提起|带上)[^。！？\n]{0,20}行囊",
            r"(?:从|穿过)[^。！？\n]{0,16}(?:侧门|后门|城门)"
            r"[^。！？\n]{0,16}(?:离开|出去|走出|穿出)",
        ):
            with self.subTest(premature_departure_action=premature_departure_action):
                self.assertNotRegex(warm_source, premature_departure_action)

    def test_people_posthumous_paths_publish_accounts_exactly_once(self) -> None:
        lines = label_body("endings_expansion.rpy", "ending_peoples_epilogue").splitlines()
        death = find_source_line(lines, '"你是在一个平凡的春日清晨走的。"')
        school_start = next(
            index
            for index in range(death + 1, len(lines))
            if lines[index].strip() == "if built_school:"
        )
        next_act = next(
            index
            for index in range(school_start + 1, len(lines))
            if lines[index].strip().startswith("## —— 第七幕")
        )
        branches = direct_source_branches(
            lines, school_start, next_act, source_indent(lines[school_start])
        )
        self.assertEqual(
            [condition for condition, _ in branches],
            ["if built_school:", "else:"],
        )

        school_source = source_without_comments(branches[0][1])
        church_source = source_without_comments(branches[1][1])
        self.assertIn("学堂", school_source)
        self.assertIn("教堂侧屋", church_source)

        shared_lines = [
            line
            for line in lines[school_start + 1 : next_act]
            if source_indent(line) == source_indent(lines[school_start])
            and line.strip().startswith(('"', "'"))
        ]
        shared_source = source_without_comments(shared_lines)
        self.assertRegex(shared_source, r"各村[^。\n]*代表")

        def account_posting_count(source: str) -> int:
            return sum(
                "账房" in sentence
                and ("收支" in sentence or "账" in sentence)
                and ("贴" in sentence or "公示" in sentence)
                for sentence in re.split(r"[。！？!?；;\n]", source)
            )

        for path, branch_source in (
            ("school", school_source),
            ("church", church_source),
        ):
            with self.subTest(path=path):
                self.assertEqual(
                    account_posting_count(branch_source + "\n" + shared_source), 1
                )

    def test_truth_cold_marriage_clears_ingrid_before_departure(self) -> None:
        branch = self.married_outcome("truth_humble_epilogue")
        nested = direct_source_branches(
            branch, 1, len(branch), source_indent(branch[0]) + 4
        )
        cold_lines = list(live_source_lines(nested[1][1]))
        departure = find_source_line(
            cold_lines,
            '"她点了一下头——像是确认某条附加条款的执行方式——然后先你一步向马厩的方向走去。你们的终点相同，但她从不觉得有同行的必要。"',
        )

        self.assertEqual(
            cold_lines[departure - 1].strip(), "hide ingrid_img with dissolve"
        )

    def test_borgia_marriage_portrait_matches_physical_presence(self) -> None:
        branch = self.married_outcome("ending_borgia")
        nested = direct_source_branches(
            branch, 1, len(branch), source_indent(branch[0]) + 4
        )
        first_nested = branch.index(nested[0][1][0])
        preamble = source_without_comments(branch[:first_nested])
        warm_lines = list(live_source_lines(nested[0][1]))
        cold_source = source_without_comments(nested[1][1])
        departure = find_source_line(
            warm_lines,
            '"她离开时没有回头。此后你们仍住在同一座城堡，仍在对外公函上共用纹章。但你清楚，这桩婚姻里最后一个肯当面告诉你\'你错了\'的人，已经不会再开口了。"',
        )

        self.assertNotIn("show ingrid_img", preamble)
        self.assertIn(
            "show ingrid_img at left with dissolve",
            [line.strip() for line in warm_lines],
        )
        self.assertEqual(
            warm_lines[departure - 1].strip(), "hide ingrid_img with dissolve"
        )
        self.assertNotIn("show ingrid_img", cold_source)
        self.assertNotRegex(cold_source, r"(?m)^\s*ingrid\s+[\x22']")


class LatestPlayerFeedbackClosureTests(unittest.TestCase):
    def test_apothecary_evidence_and_leads_preserve_continuity(self) -> None:
        expansion = read_game_file("chapter3_expansion.rpy")
        event = read_game_file("random_events_expansion.rpy")

        self.assertIn("$ ch3_black_liquid_sampled = True", expansion)
        self.assertIn("$ ch3_ritual_evidence_recorded = True", expansion)
        self.assertNotIn("$ ch3_herbalist_met = False", expansion)
        self.assertIn("if assassin_garden_warning_known:", expansion)
        self.assertIn(
            '("flag", "assassin_garden_warning_known", True)', event
        )

    def test_antidote_knowledge_unlocks_real_items_and_crafting(self) -> None:
        expansion = read_game_file("chapter3_expansion.rpy")
        deepening = read_game_file("chapters_deepening.rpy")
        crafting = read_game_file("crafting.rpy")

        self.assertGreaterEqual(expansion.count('$ add_item("antidote", 1)'), 2)
        self.assertIn("$ ch3_antidote_learned = True", deepening)
        self.assertGreaterEqual(deepening.count('$ add_item("antidote", 1)'), 2)
        self.assertIn('"knowledge_flag": "ch3_antidote_learned"', crafting)
        self.assertIn('getattr(store, knowledge_flag, False)', crafting)

    def test_public_formula_has_a_queen_reaction(self) -> None:
        deepening = read_game_file("chapters_deepening.rpy")
        chapter4 = read_game_file("chapter4.rpy")

        self.assertIn("$ ch3_antidote_formula_shared = True", deepening)
        self.assertIn("if ch3_antidote_formula_shared:", chapter4)
        self.assertIn("御药房守了二十年的方子", chapter4)

    def test_romance_choice_warns_and_elena_relationship_uses_rel_api(self) -> None:
        expansion = read_game_file("chapter3_expansion.rpy")
        southern = read_game_file("southern_expansion.rpy")

        self.assertNotIn('change_stat("rel_elena"', expansion)
        self.assertIn("确认恋爱承诺 · 将关闭艾琳娜恋爱线", southern)

    def test_iron_battle_has_resource_penalties_and_explicit_death(self) -> None:
        chapter5 = read_game_file("chapter5.rpy")
        difficulty = read_game_file("difficulty.rpy")

        for source in (chapter5, difficulty):
            self.assertIn("if wealth < 15:", source)
            self.assertIn("if reputation < 20:", source)
        self.assertIn("iron_war_score >= 24 + get_war_threshold_mod()", chapter5)
        self.assertIn("$ iron_battle_defeat = True", chapter5)
        self.assertIn("艾登堡领主战死", chapter5)


if __name__ == "__main__":
    unittest.main()

# v3.10 Timeline and Nine-Ending Tests Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Remove month-long activities from the ten-day finale, make the truth epilogue's dates and evidence names consistent, and update developer tests/tools to cover all nine endings with configured difficulty thresholds.

**Architecture:** Keep permanent governance construction confined to Chapters 2 and 3 and reuse Chapter 5's existing three war-preparation choices. Protect story dates with a focused source-level regression test, then expose a pure route-to-ending mapping that the nine-entry developer catalog and Ren'Py tests share.

**Tech Stack:** Ren'Py 8.5.2 script/test framework, Python 3 `unittest`, PowerShell, existing CoS narrative scanners.

## Global Constraints

- Do not alter Chapter 3 pacing, soft checks, package size, release copy, or the northern expansion entrance.
- Do not set `built_school`, `built_clinic`, `built_granary`, or `built_watchtower` from Chapter 5 temporary preparations.
- Keep `gov_building` and `gov_festival` labels available for legacy saves; remove only their Chapter 5 calls.
- Narrative edits must use contextually close Chinese passages from both `jerian_zh.txt` and `brante_zh.txt` as Few-shot examples.
- Before narrative edits, read `CANON.md` and `FORBIDDEN_PHRASES.md`; after them, run all narrative and portrait/overlap gates required by `CLAUDE.md`.
- Use TDD: add each regression first, run it and observe the expected failure, then apply the smallest production change.
- Commit each independently testable task on the current branch; preserve unrelated user changes.

---

## File Map

- `Tools/test_story_timeline.py`: focused source-level regression tests for the known Chapter 3–5 timeline and evidence-name failures.
- `game/chapter3.rpy`: disambiguate the tunnel scene's relative day.
- `game/chapter4_prince.rpy`: identify the prince's file as a record of the father's recent official “illness death.”
- `game/chapter5.rpy`: remove finale calls to quarterly content, display the original testament, and correct the old-calendar year.
- `game/endings_expansion.rpy`: align the truth epilogue and father-son hidden epilogue to five years and the reset calendar.
- `CANON.md`: record the player-reported timeline rules so later edits do not reintroduce them.
- `game/difficulty.rpy`: provide the pure route-to-nine-ending mapping.
- `game/balance.rpy`: expand the developer reachability catalog from five to nine endings.
- `game/test_game.rpy`: test the catalog, configured thresholds, special endings, resistance mapping, and provide nine quick ending fixtures.

---

### Task 1: Protect and repair the finale timeline

**Files:**

- Create: `Tools/test_story_timeline.py`
- Modify: `game/chapter3.rpy:2143-2151`
- Modify: `game/chapter4_prince.rpy:307-313`
- Modify: `game/chapter5.rpy:35-43, 2331-2341, 5367-5377`
- Modify: `game/endings_expansion.rpy:529-540, 3520-3780`
- Modify: `CANON.md`

**Interfaces:**

- Consumes: existing Ren'Py labels and the canonical will date `王历二百七十三年` in `game/chapter3.rpy`.
- Produces: `Tools/test_story_timeline.py`, a standalone zero-dependency regression gate invoked with Python.

- [x] **Step 1: Add the failing source-level regression test**

Create `Tools/test_story_timeline.py` with the following content:

```python
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
```

- [x] **Step 2: Run the new test and verify RED**

Run:

```powershell
python Tools/test_story_timeline.py -v
```

Expected: six tests run; the countdown, day anchor, prince document, testament, calendar, and father-son tests fail on the currently known strings/calls.

- [x] **Step 3: Remove non-war activities from `chapter5_start`**

Replace the construction/festival block with:

```renpy
    ## 终章只保留十天内能完成的战时准备；季度建设与丰收祭不再从本章触发。

    ## 治理报告
    call gov_report(5) from _call_gov_rep5
```

Do not delete `gov_building` or `gov_festival`, and do not change any `built_*` flag.

- [x] **Step 4: Apply the minimal Chapter 3–5 text corrections**

Use these replacement lines:

```renpy
    "次日傍晚，你决定把壁炉后的密道彻底查一遍。"
```

```renpy
    prince "是你父亲那场「病故」的处置记录。上面有他的名字，也有经手人的签字。"
```

```renpy
            "你从怀中取出先王遗诏的原本，在阳光下展开。"
```

In both truth-ending calendar reset branches, use:

```renpy
        "他随即下令重铸国玺。王历自这一年起重新计数——格里菲斯朝的两百九十三年，到此为止。"
```

and:

```renpy
        "委员会的第一项决议是重铸国玺、重启王历——格里菲斯朝的两百九十三年，到此为止。"
```

- [x] **Step 5: Align the expanded truth and father-son epilogues**

Use the truth header:

```renpy
    centered "{size=+10}五年后{/size}"
    centered "{size=+6}新王历五年·春{/size}"
```

In `ending_father_son_epilogue`, replace the false decade/childhood claims with concrete lines that fit a father who died at the main-story opening:

```renpy
    "父亲去世以后，你一直没有动过这些东西。"
```

```renpy
    "像你少年时许多个傍晚那样。"
```

```renpy
    player "……五年了。"

    $ hide_all_chars()
    "\"是啊。五年了。\""
```

```renpy
    "\"没能看到你接过艾登堡。\""
    "\"没能在你第一次独自坐上领主席时，告诉你别慌。\""
    "\"也没能在今天拍着你的肩膀，说一句做得好。\""
    "\"这些……是我欠你的。\""
```

Use “五年” for the later missing-corner sentence and the ending card. Do not add a new time jump.

- [x] **Step 6: Record the canon rule**

Append this entry to `CANON.md` under “已修 canon 错误历史”:

```markdown
> **3.10 时间线审计 2026-08-01**：终章不再触发季度建设与丰收祭，只保留十日战备；父亲于 1347 年主线开场前去世，因此王子文件与“父与子”尾声不得把他的死或主角童年错写成十年、二十年前；真相线旧王历由遗诏的二百七十三年顺延二十年至二百九十三年，重启后五年尾声使用“新王历五年”。
```

- [x] **Step 7: Run the timeline regression and narrative gates; verify GREEN**

Run:

```powershell
python Tools/test_story_timeline.py -v
python Tools/scan_ai_smell.py
python Tools/scan_canon.py
python scan_missing_portraits.py
python scan_narration_overlap.py
rg -n -B 1 "show .* at left" game/chapter3.rpy game/chapter4_prince.rpy game/chapter5.rpy game/endings_expansion.rpy
```

Expected: timeline test passes 6/6; missing portraits and narration overlap report 0; no newly added `show ... at left` lacks the required predecessor. AI/canon scanners may retain their documented baseline samples, but none may point to a newly changed line.

- [x] **Step 8: Commit the timeline repair**

```powershell
git add Tools/test_story_timeline.py game/chapter3.rpy game/chapter4_prince.rpy game/chapter5.rpy game/endings_expansion.rpy CANON.md
git commit -m "fix: align finale timeline and evidence text"
```

---

### Task 2: Replace the five-ending test catalog with nine endings

**Files:**

- Modify: `game/test_game.rpy:55-106, 562-703`
- Modify: `game/difficulty.rpy:32-118`
- Modify: `game/balance.rpy:12-92`

**Interfaces:**

- Consumes: `get_finale_route_availability(...) -> dict[str, bool]`, `_ending_threshold_config`, and `_ending_keys`.
- Produces: `get_finale_ending_availability(routes: dict[str, bool]) -> dict[str, bool]` with exactly the nine persistent ending keys.

- [x] **Step 1: Add a failing Ren'Py nine-ending testsuite**

Add this suite after `test_critical_finale_routes` in `game/test_game.rpy`:

```renpy
################################################################################
## 3.10 regression: developer ending catalog must match all nine real endings.
################################################################################

testsuite test_ending_catalog:
    testcase catalog_matches_persistent_ending_keys:
        $ _catalog_matches = set(_ending_requirements.keys()) == set(_ending_keys)
        assert eval (_catalog_matches)

    testcase primary_routes_use_configured_thresholds:
        parameter (difficulty_name, stat_name, ending_id) = [
            ("easy", "power", "iron_lord"),
            ("easy", "intrigue", "shadow_king"),
            ("easy", "faith", "holy_guardian"),
            ("easy", "loyalty", "peoples_lord"),
            ("normal", "power", "iron_lord"),
            ("normal", "intrigue", "shadow_king"),
            ("normal", "faith", "holy_guardian"),
            ("normal", "loyalty", "peoples_lord"),
            ("hard", "power", "iron_lord"),
            ("hard", "intrigue", "shadow_king"),
            ("hard", "faith", "holy_guardian"),
            ("hard", "loyalty", "peoples_lord"),
        ]

        $ _threshold = _ending_threshold_config[difficulty_name]["primary"]
        $ _route_kwargs = {"difficulty": difficulty_name, stat_name: _threshold}
        $ _ending_routes = get_finale_ending_availability(get_finale_route_availability(**_route_kwargs))
        assert eval (_ending_routes[ending_id])

    testcase special_routes_map_to_real_endings:
        parameter (route_kwargs, ending_id) = [
            ({"difficulty": "hard", "father_murder_mastermind_known": True, "testament_original_obtained": True}, "truth"),
            ({"difficulty": "hard", "intrigue": 70, "deep_mother_herb": "poison", "poison_evidence": True}, "borgia"),
            ({"difficulty": "hard", "rel_queen": 30}, "vassal"),
            ({"difficulty": "hard"}, "fall"),
            ({"difficulty": "hard", "southern_outcome": "free"}, "sea"),
            ({"difficulty": "hard", "rel_baron": 30}, "iron_lord"),
        ]

        $ _ending_routes = get_finale_ending_availability(get_finale_route_availability(**route_kwargs))
        assert eval (_ending_routes[ending_id])
```

- [x] **Step 2: Run the new testsuite and verify RED**

Run:

```powershell
..\renpy.exe . test test_ending_catalog --hide-execution all
```

Expected: catalog assertion reports only five registered endings, and later cases cannot call the not-yet-defined `get_finale_ending_availability`.

- [x] **Step 3: Add the pure route-to-ending mapping in `difficulty.rpy`**

Add immediately after `get_finale_route_availability`:

```python
    def get_finale_ending_availability(routes):
        """Map visible finale routes to the nine persistent ending ids."""
        return {
            "iron_lord": bool(routes.get("iron_lord") or routes.get("resist")),
            "shadow_king": bool(routes.get("shadow_king")),
            "holy_guardian": bool(routes.get("holy_guardian")),
            "peoples_lord": bool(routes.get("peoples_lord")),
            "truth": bool(routes.get("truth")),
            "borgia": bool(routes.get("borgia")),
            "vassal": bool(routes.get("vassal")),
            "fall": bool(routes.get("fall")),
            "sea": bool(routes.get("sea")),
        }
```

- [x] **Step 4: Expand `_ending_requirements` and use the ending mapping**

Add `borgia`, `vassal`, `fall`, and `sea` entries to `game/balance.rpy`, each with `stat: None`, using the same names/colors/icons already defined in `_ending_info`. Then change the start of `check_ending_reachability` to:

```python
        results = []
        routes = get_current_finale_route_availability()
        endings = get_finale_ending_availability(routes)
        primary_threshold = get_ending_threshold("primary")

        for end_id, info in _ending_requirements.items():
            reachable = endings[end_id]
```

Handle non-stat gaps before the generic stat branch:

```python
            elif end_id == "borgia":
                missing = []
                if store.deep_mother_herb != "poison":
                    missing.append("母亲的毒药教诲")
                if store.intrigue < 70:
                    missing.append("谋略 70")
                if not store.poison_evidence:
                    missing.append("暮色之露证据")
                gap_desc = "还缺：" + "、".join(missing)
            elif end_id == "vassal":
                relation_threshold = 30 if primary_threshold >= 70 else 0
                gap_desc = "王后关系需达到 %d" % relation_threshold
            elif end_id == "fall":
                gap_desc = "仍有其他核心路线可选"
            elif end_id == "sea":
                gap_desc = "南境路线未形成可离境结果"
```

Keep the existing truth, holy-guardian, and generic primary-stat descriptions.

- [x] **Step 5: Complete the nine quick ending fixtures and remove fixed-threshold assumptions**

In `test_ending_truth`, add:

```renpy
    $ testament_original_obtained = True
```

Add four labels after it:

```renpy
label test_ending_borgia:
    $ player_name = "测试·毒药"
    $ intrigue = 70
    $ deep_mother_herb = "poison"
    $ poison_evidence = True
    $ ending_type = "borgia"
    jump ending_borgia

label test_ending_vassal:
    $ player_name = "测试·附庸"
    $ rel_queen = 30
    $ ending_type = "vassal"
    jump ending_vassal

label test_ending_fall:
    $ player_name = "测试·陷落"
    $ ending_type = "fall"
    jump ending_fall

label test_ending_sea:
    $ player_name = "测试·南渡"
    $ southern_outcome = "free"
    $ corsair_romance = False
    $ ending_type = "sea"
    jump ending_sea
```

In `test_systems`, replace the fixed power setup with:

```renpy
    $ power = get_ending_threshold("primary")
```

Keep the other three primary stats below the active primary threshold before checking that iron is reachable and shadow is not.

- [x] **Step 6: Run focused ending tests; verify GREEN**

Run:

```powershell
..\renpy.exe . test test_ending_catalog --hide-execution all
..\renpy.exe . test test_critical_finale_routes --hide-execution all
..\renpy.exe . lint
```

Expected: all 19 catalog cases pass (1 catalog + 12 primary + 6 special), critical finale regression passes, and lint reports no errors.

- [x] **Step 7: Commit the nine-ending catalog**

```powershell
git add game/difficulty.rpy game/balance.rpy game/test_game.rpy
git commit -m "test: cover all nine finale endings"
```

---

### Task 3: Run complete gates and review the finished batch

**Files:**

- Review: all changes after commit `2dca340`
- Modify only if a gate or review finds an in-scope defect.

**Interfaces:**

- Consumes: the two task commits and every repository gate listed below.
- Produces: a clean branch with passing evidence and no unresolved review findings.

- [x] **Step 1: Run all Python regression tests**

```powershell
python -m unittest discover -s Tools -p "test_*.py" -v
```

Expected: all discovered Python tests pass, including six timeline regressions and the existing release classifier tests.

- [x] **Step 2: Run the full Ren'Py test suite and lint**

```powershell
..\renpy.exe . test --hide-execution all
..\renpy.exe . lint
```

Expected: every desktop testcase passes and lint reports zero errors.

- [x] **Step 3: Run narrative/release scanners**

```powershell
python Tools/scan_ai_smell.py
python Tools/scan_canon.py
python scan_missing_portraits.py
python scan_narration_overlap.py
python Tools/test_release_regressions.py
```

Expected: no new hit on a changed narrative line; missing portraits, narration overlap, and release regressions report zero violations.

- [x] **Step 4: Review the implementation against the approved spec**

Invoke the `code-review` skill with fixed point `2dca340`. Check especially:

- Chapter 5 no longer reaches month-long content before announcing ten days.
- Permanent `built_*` state remains untouched.
- father-son text no longer implies the father missed the protagonist's childhood.
- route `resist` maps to `iron_lord` without becoming a tenth persistent ending.
- the catalog and `_ending_keys` cannot silently drift apart.

Expected: no P0/P1/P2 finding remains. Fix any in-scope finding with a failing regression first, rerun the focused gate, and commit the repair.

- [x] **Step 5: Verify clean handoff state**

```powershell
git status --short
git log -4 --oneline
```

Expected: clean worktree; design commit plus independently reviewable timeline and nine-ending commits are present.

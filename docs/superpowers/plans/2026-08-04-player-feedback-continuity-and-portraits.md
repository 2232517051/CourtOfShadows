# Player Feedback Continuity and Portraits Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 修复玩家已报告的立绘错配、联姻静默锁线、结局时间倒退、铁腕伤亡不一致，以及人民领主结局缺少家庭交代和因果失真。

**Architecture:** 用一个聚焦的源码级回归文件锁定“上游状态必须被下游消费”的契约；每项先制造红灯，再以最小范围修改既有 Ren'Py 标签和静态扫描器。保留九结局入口、持久化结局键和旧 label，不合并核心结局与扩展尾声。

**Tech Stack:** Ren'Py 8.5.2、Python 3 `unittest`、项目现有静态扫描器与 Ren'Py testsuite/lint。

## Global Constraints

- 所有新增或改写的游戏文案，在动笔前必须重新读取 `C:/Users/22325/.codex/skills/writing-game-copy/references/corpora/jerian_zh.txt` 与 `C:/Users/22325/.codex/skills/writing-game-copy/references/corpora/brante_zh.txt` 的相关段落，并只以这两套中文文本作为 Few-shot 文风参考。
- 不移动或重命名现有结局 label，不改变 `persistent.endings_seen` 键，不新增结局入口。
- 新变量固定命名为 `marriage_proposal_open`，默认值固定为 `False`；只有第四章明确接受婚约后才允许 `marriage_route = True`。
- 伴侣消费顺序固定为 `elena_romance`、`marriage_route`（继续区分 `marriage_warm`）、`corsair_romance`、无伴侣。
- 四个核心结局的远景时间固定为“战后第五年”；人民核心结局不得在五年扩展尾声之前跳到“几百年后”。
- 铁腕纪念碑必须读取 `iron_battle_outcome`：`pyrrhic` 对应“两百多人”，`decisive` 对应“七十多人”。
- 人民结局必须读取 `wealth`、`built_school`、`built_granary` 等既有状态；低财富仍可和平，但不得宣称全国最富庶或所有工程都已完成。
- 主角死亡后不得再以第二人称让主角行动；全国变化必须由后来许多人的谈判、失败和再尝试推动。
- 每个任务先运行新增聚焦测试确认 RED，再实现并确认 GREEN；提交前只运行一次完整 Python 测试套件。
- 每次修改后运行项目要求的立绘、叙述重叠、AI 味、正典、发布回归和 lint 门禁；不得依据启发式结果做全局批量替换。
- 每个主题单独提交，提交信息正文必须说明资源结论。
- 美术、音乐、音效、动画均不新增；只复用 `queen_envoy.png`、`noble_werner.png`、`tax_collector.png`、`merchant_guild.png`、`ingrid.png` 与既有背景/音乐；不增加二进制包体。

## File Map

- Create `Tools/test_player_feedback_regressions.py`: 本批次所有源码契约测试，按任务逐步扩展。
- Modify `scan_missing_portraits.py`: 提取可测试的 `find_unregistered_shows()`，修复 `show *_img` 的真实单词边界。
- Modify `game/characters.rpy`: 修正角色立绘绑定并新增联姻商谈默认状态。
- Modify `game/save_compat.rpy`: 为旧档补 `marriage_proposal_open`。
- Modify `game/southern_expansion.rpy`: 税吏与账房改用现有语义匹配立绘。
- Modify `game/chapter3.rpy`: “愿意谈”只开启联姻商谈。
- Modify `game/chapter4.rpy`: 三项联姻确认/退出，并让艾琳娜段落解释正式婚约。
- Modify `game/chapter5.rpy`: 错图与离场、四个时间锚、人民核心结局资源与家庭分支。
- Modify `game/endings_expansion.rpy`: 铁腕伤亡、回望标题、人民扩展尾声现实化与家庭分支。

---

### Task 1: Portrait Identity, Off-screen Child, and Registry Gate

**Files:**
- Create: `Tools/test_player_feedback_regressions.py`
- Modify: `scan_missing_portraits.py:398-424`
- Modify: `game/characters.rpy:96-99`
- Modify: `game/southern_expansion.rpy:77,89,401,441,2387,2395`
- Modify: `game/chapter5.rpy:707-716,764-777,4076-4083,4184-4191,5719-5728`

**Interfaces:**
- Consumes: existing `CHAR_IMG_TAGS`, `hide_all_chars()`, and registered image tags.
- Produces: `find_unregistered_shows(lines: Iterable[str], registered: set[str]) -> list[tuple[int, str]]`; corrected source bindings for later full-branch scans.

- [ ] **Step 1: Write the failing portrait and scanner tests**

Create `Tools/test_player_feedback_regressions.py` with:

```python
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
        self.assertRegex(chapter, r'密使被请了出去。"\s*\n\s*hide baron_envoy_img')
        self.assertRegex(chapter, r'她那天夜里离开了艾登堡。没有告诉你她去哪。"\s*\n\s*hide elena_img')


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the focused tests and verify RED**

Run: `python -m unittest Tools.test_player_feedback_regressions.PortraitContractTests -v`

Expected: failures for missing `find_unregistered_shows`, wrong character bindings, shared representative image, child/adult image reuse, and missing departure clears.

- [ ] **Step 3: Implement the testable registry parser**

At module scope in `scan_missing_portraits.py`, add:

```python
SHOW_IMG_RE = re.compile(r"\bshow\s+(\w+_img)\b")


def find_unregistered_shows(lines, registered):
    bad = []
    for line_number, line in enumerate(lines, 1):
        if line.lstrip().startswith("#"):
            continue
        for tag in SHOW_IMG_RE.findall(line):
            if tag not in registered:
                bad.append((line_number, tag))
    return bad
```

Replace the inner line loop in `check_char_img_registry()` with:

```python
        path = os.path.join(GAME_DIR, fname)
        with open(path, encoding="utf-8") as source:
            for line_number, tag in find_unregistered_shows(source, registered):
                bad.append((fname, line_number, tag))
```

- [ ] **Step 4: Correct portrait bindings and every matching `show`**

Use these exact character definitions:

```renpy
define little_girl = Character("小女孩", color="#e8d0b8")
define queen_rep = Character("王后方代表", color="#9370db", image="queen_envoy")
define baron_rep = Character("男爵方代表", color="#2f4f4f", image="noble_werner")
```

```renpy
define tax_man = Character("公会税吏", color="#8a7a4a", image="tax_collector")
define guild_clerk = Character("公会账房", color="#9a8a6a", image="merchant_guild")
```

Change the two tax-man `show soldier_generic_img` calls paired with `tax_man` to `show tax_collector_img`, and both guild-clerk `show merchant_karl_img` calls to `show merchant_guild_img`. In the child scene, replace each adult image setup immediately before `little_girl` with `$ hide_all_chars()` and no `show`.

For both representative exchanges use the exact alternating pattern:

```renpy
    $ hide_all_chars("queen_envoy_img")
    show queen_envoy_img at left with dissolve
    queen_rep "叛军必须无条件投降！这是王室的底线！"
    $ hide_all_chars("noble_werner_img")
    show noble_werner_img at left with dissolve
    baron_rep "投降？王后先交出篡改遗诏的证据！"
```

and:

```renpy
    $ hide_all_chars("queen_envoy_img")
    show queen_envoy_img at left with dissolve
    queen_rep "……王后陛下可以接受这些条件。但第四条需要修改——"
    $ hide_all_chars("noble_werner_img")
    show noble_werner_img at left with dissolve
    baron_rep "男爵阁下原则上同意。但需要在第三条中加入——"
```

Immediately after the literal narration that the envoy was shown out, add `hide baron_envoy_img with dissolve`. Immediately after the narration that Elena left Aidenburg, add `hide elena_img with dissolve` before any further narration.

- [ ] **Step 5: Verify GREEN and run portrait-specific gates**

Run:

```powershell
python -m unittest Tools.test_player_feedback_regressions.PortraitContractTests -v
python scan_missing_portraits.py
python -m unittest discover -s Tools -p "test_*.py" -q
git diff --check
```

Expected: focused tests pass; registry reports `0 处未注册`; full Python suite passes; `git diff --check` is silent.

- [ ] **Step 6: Commit the portrait task**

```powershell
git add Tools/test_player_feedback_regressions.py scan_missing_portraits.py game/characters.rpy game/southern_expansion.rpy game/chapter5.rpy
git commit -m "fix: correct portrait identity and departure clears" -m "Assets: reuse existing portraits only; no new art, music, SFX, animation, or package-size increase."
```

---

### Task 2: Marriage Proposal State and Explicit Exit

**Files:**
- Modify: `Tools/test_player_feedback_regressions.py`
- Modify: `game/characters.rpy:250-256`
- Modify: `game/save_compat.rpy:383-390`
- Modify: `game/chapter3.rpy:6099-6108`
- Modify: `game/chapter4.rpy:903-950,2547-2643`

**Interfaces:**
- Consumes: `marriage_route`, `marriage_warm`, `elena_romance`, `corsair_romance`.
- Produces: `marriage_proposal_open: bool`; a three-result confirmation menu whose accepted outcomes alone set `marriage_route`.

- [ ] **Step 1: Add failing marriage contract tests**

Append this class to `Tools/test_player_feedback_regressions.py`:

```python
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
```

- [ ] **Step 2: Run the focused marriage tests and verify RED**

Run: `python -m unittest Tools.test_player_feedback_regressions.MarriageContractTests -v`

Expected: all four tests fail because the proposal flag and explicit decline path do not yet exist.

- [ ] **Step 3: Add defaults and make chapter three open talks only**

In `characters.rpy` add:

```renpy
default marriage_proposal_open = False # 希尔达的联姻提议仍在商谈，尚未成为正式婚约
```

In `_store_defaults` in `save_compat.rpy` add:

```python
            "marriage_proposal_open": False,
```

Replace the first chapter-three result with:

```renpy
        "回信，愿意谈这桩联姻":
            $ marriage_proposal_open = True
            $ marriage_route = False
            $ marriage_warm = False
            $ log_decision("第三章", "同意会面商谈联姻")
            $ change_stat("intrigue", 3)
            player "回信给伯爵夫人。就说我愿意在王都会面。盟约和婚约，都当面谈清楚。"
            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "我这就安排。开春前，议会的人会再来。"
```

- [ ] **Step 4: Replace the fourth-chapter confirmation menu**

Change the guard to `if marriage_proposal_open or marriage_route:` and replace its menu with:

```renpy
        menu:
            "接受婚约，把它当成纯粹的盟约":
                $ marriage_route = True
                $ marriage_warm = False
                $ marriage_proposal_open = False
                $ log_decision("第四章", "接受联姻——纯粹的政治盟约")
                player "那就把话挑明。我出兵和粮，议会给我北境的支持。婚约是封住盟书的火漆，不是感情。"
                hide player_char_img
                $ hide_all_chars("ingrid_img")
                show ingrid_img at left with dissolve
                ingrid "好。你不拿空话哄我，我也不会拿温情骗你。"

            "接受婚约，也愿意认识英格丽":
                $ marriage_route = True
                $ marriage_warm = True
                $ marriage_proposal_open = False
                $ log_decision("第四章", "接受联姻——愿意认识英格丽本人")
                $ change_stat("intrigue", 2)
                player "盟约我接受。可既然要共度一生，我想知道我娶的是怎样的人，不只是一纸条款。"
                hide player_char_img
                $ hide_all_chars("ingrid_img")
                show ingrid_img at left with dissolve
                "英格丽看了你一会儿。使馆窗外的车轮声从石路上碾过去。"
                ingrid "北边来谈婚事的人，通常先问嫁妆和兵。你是第一个先问我的。"
                ingrid "我不是一封信能写完的人。你若真有耐心，就慢慢看。"

            "到此为止，结束联姻商谈":
                $ marriage_route = False
                $ marriage_warm = False
                $ marriage_proposal_open = False
                $ log_decision("第四章", "结束与北疆议会的联姻商谈")
                player "盟约可以另谈，婚约到此为止。我不能在没选定之前，就让两家把一生当成已经成交的货物。"
                hide player_char_img
                $ hide_all_chars("ingrid_img")
                show ingrid_img at left with dissolve
                ingrid "这答复会让母亲发火。可它至少是你的答复。"
                ingrid "我会原话带回去。盐路的事，以后照旧在桌上谈。"
```

- [ ] **Step 5: Add the marriage-specific Elena response**

Before the corsair-specific menu item add:

```renpy
            "告诉她，你已经接受了与英格丽的婚约" if marriage_route:
                $ log_decision("第四章", "婉拒艾琳娜——已经接受北境婚约")
                hide elena_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "艾琳娜，我已经接受了北境的婚约。英格丽和议会的人都在等我履行它。"
                player "我不能一面让她承担这份盟约，一面又向你伸手。那对你们两个人都不公平。"
                hide player_char_img
                $ hide_all_chars("elena_img")
                show elena_img at left with dissolve
                "艾琳娜低头看了看自己放在膝上的手。"
                elena "我明白了。至少这一次，不是别人替你选了沉默。"
                $ change_rel("rel_elena", 10)
```

Change the generic distance item to:

```renpy
            "感谢她的付出，但保持距离" if not marriage_route:
```

- [ ] **Step 6: Verify GREEN and save-compatibility gates**

Run:

```powershell
python -m unittest Tools.test_player_feedback_regressions.MarriageContractTests -v
python Tools/test_release_regressions.py
python -m unittest discover -s Tools -p "test_*.py" -q
git diff --check
```

Expected: marriage tests and full suite pass; release regression script exits `0`; diff check is silent.

- [ ] **Step 7: Commit the marriage task**

```powershell
git add Tools/test_player_feedback_regressions.py game/characters.rpy game/save_compat.rpy game/chapter3.rpy game/chapter4.rpy
git commit -m "fix: require explicit marriage acceptance" -m "Assets: narrative state and existing portraits only; no new art, music, SFX, animation, or package-size increase."
```

---

### Task 3: Ending Time Anchors and Iron Casualties

**Files:**
- Modify: `Tools/test_player_feedback_regressions.py`
- Modify: `game/chapter5.rpy:3209,3735,4239,4722,4764-4768`
- Modify: `game/endings_expansion.rpy:1358-1385,3812-3824`

**Interfaces:**
- Consumes: `iron_battle_outcome` values `pyrrhic` and `decisive`.
- Produces: one consistent five-year horizon and a retrospective side-character frame.

- [ ] **Step 1: Add failing timeline and casualty tests**

Append:

```python
class EndingTimelineContractTests(unittest.TestCase):
    def test_core_endings_do_not_jump_to_ten_years(self) -> None:
        self.assertNotIn('"十年后。"', read_game_file("chapter5.rpy"))

    def test_people_core_does_not_jump_centuries_before_epilogue(self) -> None:
        people = label_body("chapter5.rpy", "ending_peoples_lord")
        self.assertNotIn("几百年后", people)

    def test_side_character_fates_are_framed_as_retrospective(self) -> None:
        fates = label_body("endings_expansion.rpy", "ending_side_characters_fate")
        self.assertIn("— 回望战后旧事 —", fates)
        self.assertNotIn("— 一年之后 —", fates)

    def test_iron_memorial_consumes_actual_battle_outcome(self) -> None:
        iron = label_body("endings_expansion.rpy", "ending_iron_epilogue")
        self.assertIn('if iron_battle_outcome == "pyrrhic":', iron)
        self.assertIn("两百多人", iron)
        self.assertIn("七十多人", iron)
        self.assertNotIn("三百七十二", iron)
```

- [ ] **Step 2: Run timeline tests and verify RED**

Run: `python -m unittest Tools.test_player_feedback_regressions.EndingTimelineContractTests -v`

Expected: four failures for current ten-year lines, centuries line, neutral fate title, and fixed memorial count.

- [ ] **Step 3: Apply the exact time anchors and retrospective title**

Replace all four core occurrences of:

```renpy
    "十年后。"
```

with:

```renpy
    "战后第五年。"
```

Replace the people-ending centuries sentence pair with:

```renpy
    "后来的人谈起那场战争，未必还记得谁在王都占了上风。"
    "但艾登堡的人记得，有一个领主在众人争夺王座时，先守住了自己的百姓。"
```

In `ending_side_characters_fate`, retain mood-specific music selection but replace all mood-specific centered headings with one heading after the conditional:

```renpy
    if _fate_mood == "light":
        play music "audio/music/dawn.ogg" fadein 3.0
    elif _fate_mood == "neutral":
        play music "audio/music/grief.ogg" fadein 3.0
    else:
        play music "audio/music/sad.ogg" fadein 3.0

    centered "{size=+4}— 回望战后旧事 —{/size}"
```

- [ ] **Step 4: Make the iron memorial conditional**

Replace the fixed count with:

```renpy
    if iron_battle_outcome == "pyrrhic":
        player "两百多人。"
        player "两百多条命。"
    else:
        player "七十多人。"
        player "七十多条命。"

    player "换来了和平。但——"
    player "值得吗？"
```

- [ ] **Step 5: Verify GREEN and timeline gates**

Run:

```powershell
python -m unittest Tools.test_player_feedback_regressions.EndingTimelineContractTests -v
python Tools/test_story_timeline.py -q
python -m unittest discover -s Tools -p "test_*.py" -q
git diff --check
```

Expected: focused and timeline tests pass; full suite passes; diff check is silent.

- [ ] **Step 6: Commit the timeline task**

```powershell
git add Tools/test_player_feedback_regressions.py game/chapter5.rpy game/endings_expansion.rpy
git commit -m "fix: align ending chronology and battle losses" -m "Assets: text and existing state only; no new art, music, SFX, animation, or package-size increase."
```

---

### Task 4: Core People's Lord Resources and Family

**Files:**
- Modify: `Tools/test_player_feedback_regressions.py`
- Modify: `game/chapter5.rpy:4722-4768`

**Interfaces:**
- Consumes: `wealth`, `built_school`, `built_granary`, `elena_romance`, `marriage_route`, `marriage_warm`, `corsair_romance`.
- Produces: a short core ending that truthfully previews material conditions and every mutually exclusive household state.

- [ ] **Step 1: Add failing core-ending consumption tests**

Append:

```python
class PeopleCoreContractTests(unittest.TestCase):
    def test_core_people_ending_consumes_resources_and_buildings(self) -> None:
        people = label_body("chapter5.rpy", "ending_peoples_lord")
        self.assertIn("if wealth >= 60:", people)
        self.assertIn("if built_school:", people)
        self.assertIn("if built_granary:", people)
        self.assertNotIn("不需要担心战争、饥荒和压迫", people)

    def test_core_people_ending_consumes_every_companion_in_order(self) -> None:
        people = label_body("chapter5.rpy", "ending_peoples_lord")
        order = [
            people.index("if elena_romance:"),
            people.index("elif marriage_route:"),
            people.index("if marriage_warm:"),
            people.index("elif corsair_romance:"),
        ]
        self.assertEqual(order, sorted(order))
        self.assertIn("英格丽", people)
        self.assertIn("赛琳", people)
```

- [ ] **Step 2: Run core-ending tests and verify RED**

Run: `python -m unittest Tools.test_player_feedback_regressions.PeopleCoreContractTests -v`

Expected: failures because the current core ending is unconditional and only branches for Elena.

- [ ] **Step 3: Replace the core five-year outcome and family block**

Replace the block from `"战后第五年。"` through the two closing legacy sentences before achievement unlock with:

```renpy
    "战后第五年。"

    if wealth >= 60:
        "艾登堡的集市比战前更大。商队肯在这里过夜，因为路上有人巡守，账目也不用靠塞钱才能办完。"
    else:
        "艾登堡没有变成传闻里的富庶之地。税收仍紧，冬天仍要计算每一袋粮；但战火没有再烧进村子，欠收的人家也不必卖掉土地。"

    if built_school:
        "城里的学堂还开着。铁匠和佃农的孩子挤在同一排长凳上，先学会写自己的名字。"
    else:
        "学堂还只是一张压在书房里的图纸。识字的修士每旬来两次，在教堂侧屋教孩子们认字。"

    if built_granary:
        "公仓熬过了两个歉收年。领民记得那两次开仓，也记得账册上每一袋粮的去处。"
    else:
        "新公仓始终没能动工。每到收获季，村社只得把旧仓逐间修补，再共同留出过冬的粮。"

    "这里仍有争吵、欠债和没修完的路。可人们愿意留下，因为他们知道自己的话能进大厅，自己的命不会被随手拿去填一场战争。"

    if elena_romance:
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "他们又在广场上等你。东村和西村为了水渠吵了半个月。"
        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "那就让两边都来。今天把账和地界摊开。"
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        "艾琳娜把一沓卷宗递给你，另一只手自然地搭上你的肩。五年里，她没有再替谁藏起自己的名字。"
        elena "我陪你。免得他们吵到天黑。"
        hide elena_img with dissolve
    elif marriage_route:
        $ hide_all_chars("ingrid_img")
        show ingrid_img at left with dissolve
        if marriage_warm:
            "英格丽把北境寄来的盐价表摊在你们共用的书桌上。纸角压着她今早从花园剪下的一枝石南。"
            ingrid "母亲说盐路今年能再放宽一成。她还说，你上次寄去的苹果酒太甜。"
            "她说到最后一句时笑了。五年前写在盟书上的婚姻没有变成传说，却成了你们每天一起核账、争论和吃晚饭的生活。"
        else:
            "英格丽仍是你的妻子，也是北境议会与艾登堡之间最稳固的联络人。你们各有房间，各管一摞公文，在正式场合从不让对方难堪。"
            ingrid "北境的盐车明早到。我会去验货。南边来的请愿归你。"
            "这不是温柔的婚姻，但也不是被遗忘的婚约。你们守住了各自答应承担的那一半。"
        hide ingrid_img with dissolve
    elif corsair_romance:
        $ hide_all_chars()
        "书房窗边压着一封从南境辗转而来的信。信纸有海盐留下的白痕，封口系着赛琳惯用的绳结。"
        "信上只有两行：『北边冷不冷？我这里风大。还活着就回信。——赛琳』"
        "你把回信交给下一支南下商队。你们之间隔着陆路和海，却没有把彼此当成一段已经结束的旧事。"
    else:
        $ hide_all_chars()
        "你独自站在城楼上。大厅里有人等着议水渠，厨房里有人为明天的面包争一袋面粉。"
        "这里没有替你预备好的家庭。你守住的是一座由许多普通家庭组成的城。"

    "人民领主的故事后来越传越远，也越传越不像原样。"
    "艾登堡的人只记得，有一个领主在众人争夺王座时，先守住了自己的百姓。"
```

- [ ] **Step 4: Verify GREEN and core-ending gates**

Run:

```powershell
python -m unittest Tools.test_player_feedback_regressions.PeopleCoreContractTests -v
python Tools/test_story_timeline.py -q
python -m unittest discover -s Tools -p "test_*.py" -q
git diff --check
```

Expected: focused tests and full suite pass; no timeline regression; diff check is silent.

- [ ] **Step 5: Commit the core ending task**

```powershell
git add Tools/test_player_feedback_regressions.py game/chapter5.rpy
git commit -m "fix: ground the people ending in player state" -m "Assets: reuse Ingrid and existing backgrounds/music; no new art, music, SFX, animation, or package-size increase."
```

---

### Task 5: Expanded People's Lord Family, Scale, and Posthumous Voice

**Files:**
- Modify: `Tools/test_player_feedback_regressions.py`
- Modify: `game/endings_expansion.rpy:2828-2944,3138-3244,3250-3309,3413-3501`

**Interfaces:**
- Consumes: the same resource and companion state as Task 4 plus existing `queen_trust`, `baron_peace_path`, `prince_ally`, `dark_lily_joined`, and `dark_lily_destroyed`.
- Produces: a five-year epilogue where Ingrid/Elena/Selene/no-partner are mutually exclusive, reform spreads gradually, and the narrative changes subject after the protagonist dies.

- [ ] **Step 1: Add failing expanded-ending tests**

Append:

```python
class PeopleExpansionContractTests(unittest.TestCase):
    def test_expansion_conditions_prosperity_and_construction(self) -> None:
        people = label_body("endings_expansion.rpy", "ending_peoples_epilogue")
        self.assertIn("if wealth >= 60:", people)
        self.assertIn("if built_school:", people)
        self.assertIn("if built_granary:", people)
        self.assertNotIn("整个王国最富庶、最和平的领地", people)

    def test_expansion_consumes_family_states_in_order(self) -> None:
        people = label_body("endings_expansion.rpy", "ending_peoples_epilogue")
        indices = [
            people.index("if elena_romance:"),
            people.index("elif marriage_route:"),
            people.index("if marriage_warm:"),
            people.index("elif corsair_romance:"),
        ]
        self.assertEqual(indices, sorted(indices))
        self.assertIn("英格丽", people)
        self.assertIn("赛琳", people)

    def test_people_route_does_not_invent_a_duchy(self) -> None:
        people = label_body("endings_expansion.rpy", "ending_peoples_epilogue")
        self.assertNotIn("公爵大人", people)
        self.assertNotIn("公爵头衔", people)

    def test_posthumous_section_has_no_second_person_protagonist_actions(self) -> None:
        people = label_body("endings_expansion.rpy", "ending_peoples_epilogue")
        after_death = people.split('"你是在一个平凡的春日清晨走的。"', 1)[1]
        self.assertNotIn('player "', after_death)
        self.assertNotRegex(after_death, r'(?m)^\s*"你(?:给|听|看|忙|让|知道|回|走|说|做|命令)')

    def test_national_change_includes_resistance_and_retries(self) -> None:
        people = label_body("endings_expansion.rpy", "ending_peoples_epilogue")
        self.assertIn("第一份改革案", people)
        self.assertIn("被否决", people)
        self.assertIn("又有人重新提出", people)
```

- [ ] **Step 2: Run expanded-ending tests and verify RED**

Run: `python -m unittest Tools.test_player_feedback_regressions.PeopleExpansionContractTests -v`

Expected: failures for unconditional prosperity, missing marriage/Selene branches, duke references, posthumous second person, and frictionless national reform.

- [ ] **Step 3: Condition the opening material outcome**

Replace the unconditional prosperity paragraph at the beginning with:

```renpy
    "五年前，战争的阴影还压在每一个家庭门口。如今，田里重新有了收成，广场也敢办丰收节。"

    if wealth >= 60:
        "商队把艾登堡当作北路上最可靠的落脚处。集市比战前更大，领库也终于有余钱修补战争留下的缺口。"
    else:
        "这里远称不上富庶。税收仍紧，歉收年仍要挨家核算口粮；可田地没有再被军队踩烂，领民也不必为一笔苛税逃离故乡。"

    if built_granary:
        "公仓门上挂着公开的收支牌。两次歉收时，它让最穷的人家也熬到了春天。"
    else:
        "新公仓一直没能建成。各村把旧仓补了又补，每年共同留粮，谁也不敢把冬天说得太轻巧。"

    "和平没有消灭贫穷，也没有让争端绝迹。它只让这里的人终于能在明天继续处理今天没解决的事。"
```

In the school celebration replace `player "……这比什么公爵头衔都值钱。"` with `player "……这比宫廷里的任何赏赐都值钱。"`.

- [ ] **Step 4: Replace the Elena-only companion interlude**

Replace the complete “第二幕半：花园另一头” block with:

```renpy
    ## —— 第二幕半：留在身边的人 ——

    if elena_romance:
        scene bg palace_garden with dissolve
        "花园另一头，艾琳娜卷着袖口，正把一桶水提到新翻的菜地旁。"
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "奥尔德里克说退休以后只管种花。今天已经替厨房翻了半块菜地。"
        "五年来，她一直留在艾登堡。不是王后的眼线，不是暗百合的刀，只以自己的名字生活。"
        if rel_elena >= 50:
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "让他慢一点。明天我们陪他把苹果树下那块地收完。"
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            "她把沾着泥的手递给你。你握住了，没有在意掌心的土。"
            elena "好。可你先把大厅里那群人应付完。"
        else:
            elena "您先忙。我把水浇完，就去看东村送来的账。"
            "她说得平常。能够平常地安排明天，已是她替自己争来的生活。"
        hide elena_img with dissolve
    elif marriage_route:
        scene bg palace_garden with dissolve
        $ hide_all_chars("ingrid_img")
        show ingrid_img at left with dissolve
        "英格丽从花园门外进来，臂弯里夹着北境议会刚送到的盐价表。五年前，她以一纸盟约来到这里；如今她仍是你的妻子。"
        if marriage_warm:
            ingrid "母亲又嫌艾登堡的酒太甜。可她把你送的两桶都留下了。"
            "她在你身边坐下，把公文分了一半给你。你们为盐税争过许多次，也在争完以后共用同一张餐桌。"
            ingrid "先把这些看完。晚上陪我去丰收节。上次那支舞，你踩了我三次。"
        else:
            ingrid "北境的盐车明早入城。我去验货。克恩伯爵的人，由你接待。"
            "你们各守一间书房，各自履行盟约。没有人把它误认作爱情，但也没有人再把这桩婚姻当作一句忘在第四章里的承诺。"
        hide ingrid_img with dissolve
    elif corsair_romance:
        scene bg study with dissolve
        $ hide_all_chars()
        "回到书房时，你看见窗边压着一封迟到数月的南境来信。纸上有海盐留下的白痕，封口系着赛琳惯用的绳结。"
        "『北边冷不冷？我这里风大。还活着就回信。——赛琳』"
        "她没有许诺上岸，你也没有许诺离开领地。可每逢商路畅通，信仍会穿过半个王国，落到彼此手里。"
    else:
        scene bg palace_garden with dissolve
        $ hide_all_chars()
        "花园里只剩奥尔德里克翻土的声音。你没有伴侣，也没有一个被史书称作家族延续的孩子。"
        "大厅里仍有人等你。艾登堡的许多家庭，就是你决定继续承担的生活。"
```

- [ ] **Step 5: Correct title and prosperity claims in the visiting-delegation scene**

Use `"领主大人，克恩伯爵派我们来向您请教治理之道。"` and `"多谢领主大人赐教。我会一字不差地转告我家伯爵。"`.

Replace the unconditional comparison with:

```renpy
    if wealth >= 60:
        "\"而艾登堡经历了同一场战争，如今商路恢复，田地也重新有了收成。\""
    else:
        "\"而艾登堡并不富裕，却没有继续加税逼人逃荒，村子也还能过日子。\""
```

- [ ] **Step 6: Replace the national-reform and posthumous sequence**

Replace the block from “关于南方的消息越来越多” through雷恩的小铺结局 with:

```renpy
    "关于南方的消息越来越多。有人抄走艾登堡公开账册的格式，也有人来旁听村社怎样争一条水渠。"
    "第一份改革案送进王都议会时，被贵族以『动摇旧律』为由否决。第二份删掉了一半条文，仍没能通过。"
    "有人因此入狱，有人退回自己的领地，也有人在几年后又把同样的问题重新提出。"
    "艾登堡没有替整个王国作答。它只是证明了一件事：领民不下跪，税收照样能进仓；账目公开，领主也不必失去威信。"

    "弗雷德里克王子回来过一次，又离开了。有人说他选择了另一种生活。"
    "这些消息传得很远。你听过，记在心里，第二天仍要去处理田界、欠税和没修完的路。"

    ## —— 第六幕：无字的石头 ——

    "你是在一个平凡的春日清晨走的。"
    "没有号角，没有仪仗。按你留下的嘱咐——只在你最喜欢的那棵苹果树下，埋了一块无字的石头。"

    if built_school:
        "艾登堡没有乱。第二天，铁匠的锤声照常响起，孩子们照常去学堂，面包照常出炉。"
    else:
        "艾登堡没有乱。第二天，铁匠的锤声照常响起，孩子们照常在教堂侧屋认字，面包照常出炉。"

    "这片土地没有因为失去一位好领主就停止运转。村社推举了新的代表，账房照旧把收支贴上广场。"

    ## —— 第七幕：史册一角 ——

    "很多年后，一位写史的人在旧卷里读到艾登堡。那几页没有写天堂：歉收照样发生，村社照样争吵，也有继任者试图收回已经让出的权力。"
    "有的规矩被废掉，后来又有人重新提出；有的地方照搬艾登堡的办法，却因为豪强阻挠而失败。"
    "旧秩序最终退去，并非出自某一个人的命令。许多人谈判、反抗、妥协，也有人为一次失败付出半生。"
    "艾登堡只在史册边缘留下一个较早的例子：变化曾经在一小块土地上发生过，因此后来的人知道，它可以再发生。"

    if queen_trust:
        "王后晚年逐渐退出议会。她保住了性命，也保住一座乡间庄园；至于她是否承认旧制度走到了尽头，史家没有一致答案。"
    else:
        "王后拒绝了最初几轮让步。她的派系在争斗中瓦解，最终被迫离开王都；旧制度的支持者仍借她的名字反扑过数次。"

    if baron_peace_path:
        "男爵较早交出了私人军队，后来成为地方议会代表。他的务实帮助过新制度，也让许多人怀疑他只是换了一种方式保住影响力。"
    else:
        "男爵组织过抵抗。抵抗失败后，他失去头衔和领地；他的旧部没有立刻消失，边地冲突又延续了数年。"

    if prince_ally:
        "弗雷德里克化名去了南方教书。他偶尔写文章谈责任，从不署上王族旧姓。"
    else:
        "弗雷德里克流亡海外，成了复辟者反复举起的一面旗。旗帜渐渐褪色，麻烦却没有立刻结束。"

    if dark_lily_joined:
        "暗百合内部为是否走到阳光下争论了多年。一部分成员成为公开监察员，另一部分离开；继任者没有强迫所有人接受同一种答案。"
    elif dark_lily_destroyed:
        "暗百合早已覆灭。后来的人只能从残缺档案里知道，旧制度的阴影中曾有过这样一群人。"
    else:
        "暗百合没有在一夜间消失。随着公开申诉和地方议会逐渐建立，它的成员一年比一年少，最后一批人把徽章锁进了箱底。"

    "雷恩把守军改成了小规模常备队与村社轮值并存。有人嫌这样太慢，他只说，百姓需要的是能回家种地的兵，不是另一支只听一个人命令的私军。"
    "晚年时，他在校场旁开了一间磨农具的小铺。孩子们仍叫他队长。"
```

- [ ] **Step 7: Verify GREEN and run narrative gates**

Run:

```powershell
python -m unittest Tools.test_player_feedback_regressions.PeopleExpansionContractTests -v
python Tools/test_story_timeline.py -q
python Tools/scan_ai_smell.py
python Tools/scan_canon.py
python -m unittest discover -s Tools -p "test_*.py" -q
git diff --check
```

Expected: focused tests and full suite pass; AI/canon scanners complete without new blocking findings attributable to this task; diff check is silent.

- [ ] **Step 8: Commit the expanded ending task**

```powershell
git add Tools/test_player_feedback_regressions.py game/endings_expansion.rpy
git commit -m "fix: complete the people epilogue household" -m "Assets: reuse Ingrid and existing backgrounds/music; no new art, music, SFX, animation, or package-size increase."
```

---

### Task 6: Full Verification and Release Gate Evidence

**Files:**
- Modify only if a required gate exposes a regression in files already touched by Tasks 1-5.

**Interfaces:**
- Consumes: all task commits.
- Produces: fresh verification evidence for the exact branch state and a clean worktree.

- [ ] **Step 1: Run the full Python suite and focused regression file**

```powershell
python -m unittest Tools.test_player_feedback_regressions -v
python -m unittest discover -s Tools -p "test_*.py" -v
python Tools/test_release_regressions.py
```

Expected: all commands exit `0`, with no warnings or unexpected output.

- [ ] **Step 2: Run all narrative and portrait scanners**

```powershell
python scan_missing_portraits.py
python scan_narration_overlap.py
python Tools/scan_ai_smell.py
python Tools/scan_canon.py
```

Expected: portrait registry reports zero unregistered tags; narration scan retains its documented default scope; no new blocking AI/canon finding comes from changed passages.

- [ ] **Step 3: Manually verify `show ... at left` predecessors in changed files**

```powershell
rg -n -B 2 -A 1 "show (queen_envoy|noble_werner|ingrid|elena)_img at left" game/chapter4.rpy game/chapter5.rpy game/endings_expansion.rpy
rg -n -B 2 -A 1 "show (tax_collector|merchant_guild)_img" game/southern_expansion.rpy
```

Expected: each changed `show` is preceded by a matching `hide_all_chars("<same_tag>")` or an intentional full clear.

- [ ] **Step 4: Run Ren'Py testsuite and lint from the SDK runtime**

```powershell
& 'E:/Projects/renpy-8.5.2-sdk/renpy.exe' . test
& 'E:/Projects/renpy-8.5.2-sdk/renpy.exe' . lint
```

Expected: testsuite and lint exit `0`; no new parse, undefined image, unreachable choice, or interpolation errors.

- [ ] **Step 5: Refresh font/release preparation only if changed text requires it**

```powershell
python Tools/prepare_release.py
git status --short
```

Expected: preparation exits `0`. If it updates a tracked font because of genuinely new glyphs, inspect and commit that generated change with an asset/package-size note; otherwise no binary file changes are allowed.

- [ ] **Step 6: Run final repository checks**

```powershell
git diff --check
git status --short
git log --oneline -8
```

Expected: diff check is silent, working tree is clean, and Tasks 1-5 appear as separate topical commits.

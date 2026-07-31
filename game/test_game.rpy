## ============================================================
## 自动化测试脚本
## test_game.rpy
## 用法: renpy.exe CourtOfShadows --test test_walkthrough
## ============================================================


################################################################################
## 1. Ren'Py 内置测试框架 — 自动走通游戏
################################################################################

## 主测试：快速走通游戏，验证不会崩溃
testcase test_walkthrough:
    ## 从主菜单稳定启动，并完成一次性开局设置
    $ persistent.privacy_agreed = True
    $ persistent.tutorial_seen = True
    run Start() until screen "difficulty_select" timeout 4.0
    click "确认"
    pause until screen "name_input_screen" timeout 4.0
    click "使用默认"
    pause 0.5

    ## 连续点击推进剧情，直到遇到选择
    ## 第一章
    ## 自动点击推进剧情
    click
    pause 0.3
    click
    pause 0.3
    click
    pause 0.3
    click
    pause 0.3
    click
    pause 0.3
    click
    pause 0.3
    click
    pause 0.3
    click
    pause 0.3
    click
    pause 0.3
    click


## 3.9.2 critical regression: finale routes must always expose a valid choice,
## and legacy chapter-three truth state must not imply chapter-four knowledge.
testcase test_critical_finale_routes:
    $ _full_lily_faith = get_finale_route_availability(faith=80, difficulty="hard", lily_full_member=True, rel_queen=20, rel_baron=20)
    $ _full_lily_holy_hidden = not _full_lily_faith["holy_guardian"]
    $ _full_lily_fall_visible = _full_lily_faith["fall"]
    $ _full_lily_has_route = any(_full_lily_faith.values())
    assert eval (_full_lily_holy_hidden)
    assert eval (_full_lily_fall_visible)
    assert eval (_full_lily_has_route)

    $ _partial_truth = get_finale_route_availability(difficulty="hard", rel_queen=20, rel_baron=20, father_poison_method_known=True, father_poison_executor_known=True, testament_original_obtained=True)
    $ _partial_truth_hidden = not _partial_truth["truth"]
    $ _partial_truth_has_route = any(_partial_truth.values())
    assert eval (_partial_truth_hidden)
    assert eval (_partial_truth_has_route)

    $ _complete_truth = get_finale_route_availability(difficulty="hard", rel_queen=20, rel_baron=20, father_murder_mastermind_known=True, testament_original_obtained=True)
    $ _complete_truth_visible = _complete_truth["truth"]
    $ _complete_truth_has_route = any(_complete_truth.values())
    assert eval (_complete_truth_visible)
    assert eval (_complete_truth_has_route)

    $ _independent_faith = get_finale_route_availability(faith=80, difficulty="hard", lily_full_member=False, rel_queen=20, rel_baron=20)
    $ _independent_faith_visible = _independent_faith["holy_guardian"]
    $ _independent_fall_hidden = not _independent_faith["fall"]
    $ _independent_faith_has_route = any(_independent_faith.values())
    assert eval (_independent_faith_visible)
    assert eval (_independent_fall_hidden)
    assert eval (_independent_faith_has_route)

    $ _chapter_three_legacy_is_not_mastermind = not legacy_true_implies_mastermind(True, ch3_dark_lily_visited=True)
    $ _prince_ally_legacy_is_mastermind = legacy_true_implies_mastermind(True, prince_ally=True)
    $ _pending_prince_legacy_is_mastermind = legacy_true_implies_mastermind(True, prince_answer_pending=True)
    $ _logged_prince_legacy_is_mastermind = legacy_true_implies_mastermind(True, decisions=[("第五章", "战前答复王子，结成同盟", "")])
    $ _logged_prince_refusal_is_mastermind = legacy_true_implies_mastermind(True, decisions=[("第五章", "战前回绝王子", "")])
    assert eval (_chapter_three_legacy_is_not_mastermind)
    assert eval (_prince_ally_legacy_is_mastermind)
    assert eval (_pending_prince_legacy_is_mastermind)
    assert eval (_logged_prince_legacy_is_mastermind)
    assert eval (_logged_prince_refusal_is_mastermind)


################################################################################
## 3.9.2 regression: every formal chapter entry must initialize a blank run once
################################################################################

testsuite test_new_run_bootstrap:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)

        $ _test.timeout = 4.0
        $ persistent.privacy_agreed = True
        $ persistent.tutorial_seen = True
        $ persistent.ng_plus_unlocked = False
        $ persistent.ng_plus_bonus_power = 0
        $ persistent.ng_plus_bonus_wealth = 0
        $ persistent.ng_plus_bonus_intrigue = 0
        $ persistent.difficulty = "normal"

    after testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)

    testcase blank_formal_entries_require_setup:
        parameter (entry_label, bootstrap_return) = [
            ("prologue", "_call_new_run_bootstrap_prologue"),
            ("chapter1_start", "_call_new_run_bootstrap_chapter1"),
            ("chapter2_start", "_call_new_run_bootstrap_chapter2"),
            ("chapter3_start", "_call_new_run_bootstrap_chapter3"),
            ("chapter4_start", "_call_new_run_bootstrap_chapter4"),
            ("chapter5_start", "_call_new_run_bootstrap_chapter5"),
            ("southern_arc_standalone", "_call_new_run_bootstrap_southern_standalone"),
        ]

        run Start(entry_label) until screen "difficulty_select" timeout 4.0
        assert screen "difficulty_select"
        assert eval (bootstrap_return in renpy.get_return_stack())

    testcase setup_is_complete_and_idempotent:
        $ persistent.ng_plus_unlocked = True
        $ persistent.ng_plus_bonus_power = 5
        $ persistent.ng_plus_bonus_wealth = 7
        $ persistent.ng_plus_bonus_intrigue = 4

        run Start("southern_arc_standalone") until screen "difficulty_select" timeout 4.0
        click "简单"
        click "确认"
        pause until screen "name_input_screen" timeout 4.0
        click "使用默认"
        pause until screen "chapter_title" timeout 4.0

        assert eval (persistent.difficulty == "easy")
        assert eval (bool(player_name.strip()))
        assert eval (get_inventory() == {"iron_sword": 1, "leather_armor": 1, "health_potion": 2, "bandage": 2})
        assert eval ((power, wealth, faith, loyalty, reputation, intrigue) == (55, 57, 45, 50, 50, 49))
        assert eval (_new_run_bootstrap_done)
        assert eval ("_call_show_chapter_southern" in renpy.get_return_stack())

        $ _bootstrap_stats_before_second_call = (power, wealth, faith, loyalty, reputation, intrigue)
        $ _bootstrap_inventory_before_second_call = list(inventory_items)
        run Call("new_run_bootstrap")
        pause 0.1
        assert eval ((power, wealth, faith, loyalty, reputation, intrigue) == _bootstrap_stats_before_second_call)
        assert eval (inventory_items == _bootstrap_inventory_before_second_call)

    testcase after_load_protects_existing_run:
        run Start("test_new_run_after_load_driver") until screen "chapter_title" timeout 4.0
        assert eval (_new_run_bootstrap_done)
        assert eval (inventory_items == [("synthetic_loaded_item", 7)])
        assert eval (_after_load_rollback_limit_before > 0)
        assert eval (_after_load_rollback_limit_after == 0)
        assert eval (_after_load_rollback_block_after > _after_load_rollback_block_before)
        assert not screen "difficulty_select"
        assert not screen "name_input_screen"
        assert eval ("_call_show_chapter_1" in renpy.get_return_stack())


label test_new_run_after_load_driver:
    $ _new_run_bootstrap_done = False
    $ inventory_items = [("synthetic_loaded_item", 7)]
    $ renpy.checkpoint()
    $ _after_load_rollback_limit_before = renpy.game.log.rollback_limit
    $ _after_load_rollback_block_before = renpy.game.log.rollback_block
    call after_load from _call_after_load_bootstrap_test
    $ _after_load_rollback_limit_after = renpy.game.log.rollback_limit
    $ _after_load_rollback_block_after = renpy.game.log.rollback_block
    jump chapter3_start


################################################################################
## 2. 测试用快速通关标签 — 验证各结局不会崩溃
################################################################################

## 铁腕领主结局测试
label test_ending_iron_lord:
    ## 设置满足铁腕领主结局的属性
    $ player_name = "测试·铁腕"
    $ power = 80
    $ wealth = 50
    $ faith = 30
    $ loyalty = 40
    $ reputation = 50
    $ intrigue = 30
    $ rel_aldric = 70
    $ rel_elena = 40
    $ rel_bishop = 30
    $ rel_baron = 10
    $ rel_captain = 60
    $ rel_queen = 30
    $ ending_type = "iron_lord"
    jump ending_iron_lord

## 影中之王结局测试
label test_ending_shadow_king:
    $ player_name = "测试·影王"
    $ power = 40
    $ wealth = 50
    $ faith = 30
    $ loyalty = 30
    $ reputation = 40
    $ intrigue = 80
    $ rel_aldric = 50
    $ rel_elena = 70
    $ rel_bishop = 20
    $ rel_baron = 30
    $ rel_captain = 40
    $ rel_queen = 50
    $ dark_lily_joined = True
    $ ending_type = "shadow_king"
    jump ending_shadow_king

## 圣光守护结局测试
label test_ending_holy_guardian:
    $ player_name = "测试·圣光"
    $ power = 30
    $ wealth = 40
    $ faith = 80
    $ loyalty = 50
    $ reputation = 60
    $ intrigue = 20
    $ rel_aldric = 60
    $ rel_elena = 30
    $ rel_bishop = 80
    $ rel_baron = 10
    $ rel_captain = 50
    $ rel_queen = 40
    $ alliance_church = True
    $ ending_type = "holy_guardian"
    jump ending_holy_guardian

## 人民领主结局测试
label test_ending_peoples_lord:
    $ player_name = "测试·人民"
    $ power = 40
    $ wealth = 50
    $ faith = 40
    $ loyalty = 80
    $ reputation = 70
    $ intrigue = 30
    $ rel_aldric = 80
    $ rel_elena = 50
    $ rel_bishop = 50
    $ rel_baron = 20
    $ rel_captain = 80
    $ rel_queen = 30
    $ ending_type = "peoples_lord"
    jump ending_peoples_lord

## 真相大白结局测试（最佳结局）
label test_ending_truth:
    $ player_name = "测试·真相"
    $ power = 50
    $ wealth = 50
    $ faith = 50
    $ loyalty = 50
    $ reputation = 60
    $ intrigue = 60
    $ rel_aldric = 70
    $ rel_elena = 60
    $ rel_bishop = 40
    $ rel_baron = 20
    $ rel_captain = 60
    $ rel_queen = 50
    $ father_murder_mastermind_known = True
    $ father_letters_found = True
    $ poison_evidence = True
    $ ending_type = "truth"
    jump ending_truth


################################################################################
## 3. 一键验证所有系统 — 不进入剧情，只测试函数
################################################################################

label test_systems:
    ## 测试属性系统
    "开始系统测试..."

    $ power = 50
    $ change_stat("power", 10)
    if power != 60:
        "错误：change_stat 异常！期望 power=60，实际=[power]"

    $ change_stat("power", -5)
    if power != 55:
        "错误：change_stat 负值异常！期望 power=55，实际=[power]"

    ## 测试属性钳制
    $ power = 150
    $ clamp_stats()
    if power != 100:
        "错误：clamp_stats 未正确钳制！期望 power=100，实际=[power]"

    $ power = -20
    $ clamp_stats()
    if power != 0:
        "错误：clamp_stats 负值钳制异常！期望 power=0，实际=[power]"

    ## 测试结局可达性分析
    $ power = 80
    $ intrigue = 30
    $ faith = 30
    $ loyalty = 30
    $ father_murder_mastermind_known = False
    $ _results = check_ending_reachability()
    $ _reachable = [r[0] for r in _results if r[2]]
    if "iron_lord" not in _reachable:
        "错误：铁腕领主应该可达但检测为不可达！"
    if "shadow_king" in _reachable:
        "错误：影中之王不应该可达但检测为可达！"

    ## 测试收藏品系统
    $ persistent.collectibles_found = set()
    $ collect_item("letter_father_1")
    if "letter_father_1" not in persistent.collectibles_found:
        "错误：收藏品系统异常！"

    ## 测试决策日志
    $ _decisions = []
    $ log_decision("测试章节", "测试选择", "测试结果")
    $ _test_decs = get_decisions()
    if len(_test_decs) == 0:
        "错误：决策日志记录异常！"

    ## 测试彩蛋名字检测
    $ _test_egg = check_name_easter_egg("小燚")
    if _test_egg is None:
        "错误：名字彩蛋检测异常！"

    ## 测试成就系统
    $ persistent.achievements = set()
    $ unlock_achievement("first_steps")
    if "first_steps" not in persistent.achievements:
        "错误：成就解锁异常！"

    "所有系统测试通过！"

    return


################################################################################
## 4. 属性边界测试
################################################################################

label test_stat_boundaries:
    "开始属性边界值测试..."

    ## 测试所有属性在 0-100 范围内
    $ power = 0
    $ wealth = 0
    $ faith = 0
    $ loyalty = 0
    $ reputation = 0
    $ intrigue = 0

    ## 大量减少，确保不会低于0
    $ change_stat("power", -50)
    $ clamp_stats()
    if power < 0:
        "错误：power 低于0！值=[power]"

    ## 大量增加，确保不会超过100
    $ power = 95
    $ change_stat("power", 50)
    $ clamp_stats()
    if power > 100:
        "错误：power 超过100！值=[power]"

    ## 测试好感度范围
    $ rel_aldric = 100
    $ change_rel("rel_aldric", 50)
    ## 好感度应该有上限保护

    $ rel_baron = -100
    $ change_rel("rel_baron", -50)
    ## 好感度应该有下限保护

    "属性边界测试完成！"

    return

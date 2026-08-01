## ============================================================
## 自动化测试脚本
## test_game.rpy
## 用法: renpy.exe CourtOfShadows --test test_walkthrough
## ============================================================


################################################################################
## 1. Ren'Py 内置测试框架 — 自动走通游戏
################################################################################

## 主测试：快速走通游戏，验证不会崩溃
testsuite test_walkthrough:
    before testcase:
        $ _test.walkthrough_persistent_snapshot = {"privacy_agreed": persistent.privacy_agreed, "tutorial_seen": persistent.tutorial_seen}
        $ persistent.privacy_agreed = True
        $ persistent.tutorial_seen = True

    after testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        $ persistent.privacy_agreed = _test.walkthrough_persistent_snapshot["privacy_agreed"]
        $ persistent.tutorial_seen = _test.walkthrough_persistent_snapshot["tutorial_seen"]
        assert eval (all(getattr(persistent, name) == value for name, value in _test.walkthrough_persistent_snapshot.items()))
        $ renpy.save_persistent()

    testcase quick_start:
        ## 从主菜单稳定启动，并完成一次性开局设置
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
    $ father_poisoned_known = False
    $ father_poison_method_known = False
    $ confirm_father_poison_method()
    assert eval (father_poisoned_known)
    assert eval (father_poison_method_known)

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


################################################################################
## 3.9.2 save compatibility: legacy HQ executor knowledge needs exact provenance.
################################################################################

testsuite test_evidence_migration:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        $ _test.timeout = 4.0
        $ _test.evidence_chapters_completed_snapshot = None if persistent.chapters_completed is None else set(persistent.chapters_completed)

    after testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        $ persistent.chapters_completed = None if _test.evidence_chapters_completed_snapshot is None else set(_test.evidence_chapters_completed_snapshot)
        $ renpy.save_persistent()

    testcase legacy_executor_provenance_matrix:
        parameter (entry_label, expected_executor) = [
            ("test_evidence_migration_joined", True),
            ("test_evidence_migration_destroyed", True),
            ("test_evidence_migration_independent", True),
            ("test_evidence_migration_skipped", False),
            ("test_evidence_migration_mid_scene", False),
        ]

        run Start(entry_label) until screen "say" timeout 4.0
        assert eval (father_poison_executor_known == expected_executor)

    testcase prince_murder_disclosure_does_not_imply_poison_method:
        run Start("test_evidence_migration_prince_only") until screen "say" timeout 4.0
        assert eval (father_poisoned_known)
        assert not eval (father_poison_method_known)


label test_evidence_migration_joined:
    call test_evidence_migration_driver(joined=True, visited=True) from _call_test_evidence_migration_joined
    "旧档递毒者迁移检查完成。"
    return


label test_evidence_migration_destroyed:
    call test_evidence_migration_driver(destroyed=True, visited=True) from _call_test_evidence_migration_destroyed
    "旧档递毒者迁移检查完成。"
    return


label test_evidence_migration_independent:
    call test_evidence_migration_driver(visited=True, decisions=[("第三章", "保持独立，不加入暗百合", "")]) from _call_test_evidence_migration_independent
    "旧档递毒者迁移检查完成。"
    return


label test_evidence_migration_skipped:
    call test_evidence_migration_driver() from _call_test_evidence_migration_skipped
    "旧档递毒者迁移检查完成。"
    return


label test_evidence_migration_mid_scene:
    call test_evidence_migration_driver(visited=True) from _call_test_evidence_migration_mid_scene
    "旧档递毒者迁移检查完成。"
    return


label test_evidence_migration_prince_only:
    $ persistent.chapters_completed = set()
    $ father_poisoned_known = True
    $ father_poison_method_known = False
    $ poison_evidence = False
    $ ch3_deep_cure_found = False
    $ true_killer_known = False
    call after_load from _call_after_load_evidence_migration_prince_only
    "王子只确认谋杀，不确认毒物。"
    return


label test_evidence_migration_driver(joined=False, destroyed=False, visited=False, decisions=None):
    $ true_killer_known = True
    $ father_poison_executor_known = False
    $ father_murder_mastermind_known = False
    $ dark_lily_joined = joined
    $ dark_lily_destroyed = destroyed
    $ ch3_dark_lily_visited = visited
    $ prince_ally = False
    $ prince_answer_pending = False
    $ _decisions = list(decisions or [])
    call after_load from _call_after_load_evidence_migration
    return


################################################################################
## Mobile regression: all seven finale choices must remain reachable.
################################################################################

default _test_mobile_choice_overflow_seventh_selected = False
default _test_desktop_choice_first_selected = False

testcase test_mobile_choice_overflow:
    if eval (renpy.variant("small")):
        run Start("test_mobile_choice_overflow_fixture") until screen "choice" timeout 4.0
        screenshot "mobile_choice_overflow_important"
        pause 2.0
        assert eval (renpy.get_screen_variable("choice_is_important", screen="choice") is True)
        $ _mobile_choice_viewport = renpy.get_displayable("choice", "choice_scroll")
        $ _mobile_choice_viewport_bounds = renpy.test.testfocus.focus_from_displayable(_mobile_choice_viewport)
        assert eval (_mobile_choice_viewport_bounds is not None)
        assert eval (_mobile_choice_viewport_bounds.y == 160)
        assert eval (_mobile_choice_viewport_bounds.h == 440)
        screenshot "mobile_choice_overflow_initial"
        scroll id "choice_scroll" amount 1000
        pause 0.5
        $ _mobile_choice_viewport = renpy.get_displayable("choice", "choice_scroll")
        assert eval (_mobile_choice_viewport.yadjustment.range > 0)
        assert eval (_mobile_choice_viewport.yadjustment.value == _mobile_choice_viewport.yadjustment.range)
        screenshot "mobile_choice_overflow_scrolled"
        click "第七项：放下旧日的王冠，与所有盟友共同建立新的议会秩序"
        pause until screen "say" timeout 4.0
        assert eval (_test_mobile_choice_overflow_seventh_selected)
        click
        pause until screen "main_menu" timeout 4.0


testcase test_desktop_choice_sanity:
    run Start("test_desktop_choice_sanity_fixture") until screen "choice" timeout 4.0
    pause 2.0
    click "保留王廷法统"
    pause until screen "say" timeout 4.0
    assert eval (_test_desktop_choice_first_selected)
    click
    pause until screen "main_menu" timeout 4.0


testcase test_father_son_cg_render:
    $ _test.timeout = 4.0
    run Start("test_father_son_cg_atl_smoke_fixture") until screen "say" timeout 4.0
    pause 2.2
    click
    pause until screen "main_menu" timeout 4.0

    run Start("test_father_son_cg_render_fixture") until screen "say" timeout 4.0
    pause 1.0
    screenshot "father_son_empty"
    click
    pause until screen "say" timeout 4.0
    pause 1.0
    screenshot "father_son_manifested"
    click
    pause until screen "say" timeout 4.0
    pause 1.0
    screenshot "father_son_departed"
    click
    pause until screen "main_menu" timeout 4.0


## 配方详情曾因嵌套字典插值在打开时崩溃。
testcase test_crafting_detail_render:
    run Start("test_crafting_detail_render_fixture") until screen "crafting_screen" timeout 4.0
    pause 0.3
    assert eval (get_success_rate("health_potion") == 88)
    click "治疗药水"
    pause 0.3
    assert eval (renpy.get_screen_variable("selected_recipe", screen="crafting_screen") == "health_potion")
    click "结束锻造测试"
    pause until screen "main_menu" timeout 4.0


screen test_crafting_detail_exit():
    zorder 1000

    textbutton "结束锻造测试":
        xalign 1.0
        yalign 1.0
        action Return(True)


label test_crafting_detail_render_fixture:
    $ intrigue = 60
    $ crafting_skill_bonus = 0
    $ inventory_items = [("medicinal_herbs", 8), ("waterskin", 4)]
    show screen crafting_screen
    show screen test_crafting_detail_exit
    $ ui.interact()
    hide screen test_crafting_detail_exit
    hide screen crafting_screen
    return


label test_mobile_choice_overflow_fixture:
    $ _test_mobile_choice_overflow_seventh_selected = False
    $ mark_important_choice()

    menu:
        "第一项：接受摄政之位，以王廷法统维持北境来之不易的和平|权力 +10 盟友信任 -5":
            return
        "第二项：公开父亲遇害的全部证据，让贵族与教会共同接受审判|声望 +10 阴谋 -5":
            return
        "第三项：率领边境军团继续南下，彻底结束诸侯割据造成的战乱|权力 +15 忠诚 -10":
            return
        "第四项：兑现对自由城邦的承诺，承认港口与商路的自治权利|财富 +10 王廷关系 -5":
            return
        "第五项：邀请暗百合进入议会，以秘密情报守护脆弱的新秩序|阴谋 +10 教会关系 -5":
            return
        "第六项：将兵权交还各地领主，用公开盟约约束下一任统治者|忠诚 +10 权力 -10":
            return
        "第七项：放下旧日的王冠，与所有盟友共同建立新的议会秩序|全体关系 +10 历史将记住这一刻":
            $ _test_mobile_choice_overflow_seventh_selected = True
            "第七个分支已执行。"

    return


label test_desktop_choice_sanity_fixture:
    $ _test_desktop_choice_first_selected = False

    menu:
        "保留王廷法统|权力 +5":
            $ _test_desktop_choice_first_selected = True
            "桌面选项分支已执行。"
        "交还边境兵权|忠诚 +5":
            return
        "公开全部证据|声望 +5":
            return

    return


label test_father_son_cg_render_fixture:
    $ quick_menu = False
    scene cg_father_son_empty as father_son_cg
    "空椅测试画面。"
    show cg_father_son as father_son_cg with dissolve
    "父亲显形测试画面。"
    show cg_father_son_empty as father_son_cg with dissolve
    "父亲消失后的空椅测试画面。"
    scene black
    $ quick_menu = True
    return


label test_father_son_cg_atl_smoke_fixture:
    $ quick_menu = False
    scene cg_father_son_empty as father_son_cg at father_son_slow_push
    "父子 CG ATL 烛光测试画面。"
    scene black
    $ quick_menu = True
    return


################################################################################
## 3.9.2 regression: accessibility controls must drive Ren'Py preferences.
################################################################################

default _test_accessibility_original_font_size = 1.0
default _test_accessibility_original_high_contrast = False
default _test_accessibility_original_text_cps = 0
default _test_accessibility_seventh_selected = False

testsuite test_accessibility_settings:
    before testcase:
        $ _test.timeout = 4.0
        $ _test_accessibility_original_font_size = preferences.font_size
        $ _test_accessibility_original_high_contrast = preferences.high_contrast
        $ preferences.font_size = 1.0
        $ preferences.high_contrast = False

    after testcase:
        $ preferences.font_size = _test_accessibility_original_font_size
        $ preferences.high_contrast = _test_accessibility_original_high_contrast
        $ renpy.save_persistent()
        $ renpy.restart_interaction()
        if screen "accessibility_settings":
            click "« 返回"
            pause until screen "main_menu" timeout 4.0
        if screen "preferences":
            click "« 返回"
            pause until screen "main_menu" timeout 4.0

    testcase branded_size_buttons_set_exact_native_factors:
        run ShowMenu("accessibility_settings") until screen "accessibility_settings" timeout 4.0

        click "小"
        assert eval (preferences.font_size == 0.9)
        click "标准"
        assert eval (preferences.font_size == 1.0)
        click "大"
        assert eval (preferences.font_size == 1.25)
        click "特大"
        assert eval (preferences.font_size == 1.5)

    testcase contrast_buttons_set_native_preference:
        run ShowMenu("accessibility_settings") until screen "accessibility_settings" timeout 4.0

        click "开启"
        assert eval (preferences.high_contrast)
        click "关闭"
        assert eval (not preferences.high_contrast)

    testcase normal_preferences_page_exposes_accessibility_entry:
        run ShowMenu("preferences") until screen "preferences" timeout 4.0
        assert eval (renpy.get_displayable("preferences", "accessibility_entry") is not None)


testsuite test_accessibility_render:
    before testcase:
        $ _test.timeout = 4.0
        $ _test_accessibility_original_font_size = preferences.font_size
        $ _test_accessibility_original_high_contrast = preferences.high_contrast
        $ _test_accessibility_original_text_cps = preferences.text_cps
        $ preferences.font_size = 1.5
        $ preferences.high_contrast = False
        $ preferences.text_cps = 0

    after testcase:
        $ preferences.font_size = _test_accessibility_original_font_size
        $ preferences.high_contrast = _test_accessibility_original_high_contrast
        $ preferences.text_cps = _test_accessibility_original_text_cps
        $ renpy.save_persistent()
        $ renpy.restart_interaction()
        if screen "preferences":
            click "« 返回"
            pause until screen "main_menu" timeout 4.0

    testcase small_touch_dialogue_and_seven_long_choices_render_at_150_percent:
        if eval (renpy.variant("small")):
            run Start("test_accessibility_render_fixture") until screen "say" timeout 4.0
            $ _quick_history_displayable = renpy.get_displayable("quick_menu", "quick_history")
            $ _quick_preferences_displayable = renpy.get_displayable("quick_menu", "quick_preferences")
            $ _quick_bar_displayable = renpy.get_displayable("quick_menu", "quick_menu_bar")
            assert eval (_quick_history_displayable is not None)
            assert eval (_quick_preferences_displayable is not None)
            assert eval (_quick_bar_displayable is not None)
            $ _quick_history_bounds = renpy.test.testfocus.focus_from_displayable(_quick_history_displayable)
            $ _quick_preferences_bounds = renpy.test.testfocus.focus_from_displayable(_quick_preferences_displayable)
            $ _quick_bar_bounds = renpy.test.testfocus.focus_from_displayable(_quick_bar_displayable)
            assert eval (_quick_history_bounds is not None)
            assert eval (_quick_preferences_bounds is not None)
            assert eval (_quick_bar_bounds is not None)
            assert eval (_quick_history_bounds.x >= 0)
            assert eval (_quick_preferences_bounds.x + _quick_preferences_bounds.w <= config.screen_width)
            $ _say_what_bounds = renpy.test.testfocus.focus_from_displayable(renpy.get_displayable("say", "what"))
            assert eval (_say_what_bounds is not None)
            assert eval (_say_what_bounds.y + _say_what_bounds.h <= _quick_bar_bounds.y)
            screenshot "accessibility_150_dialogue"
            click pos (0.5, 0.5)
            pause until screen "choice" timeout 4.0
            pause 2.0
            $ _choice_viewport_bounds = renpy.test.testfocus.focus_from_displayable(renpy.get_displayable("choice", "choice_scroll"))
            $ _choice_quick_bar_bounds = renpy.test.testfocus.focus_from_displayable(renpy.get_displayable("quick_menu", "quick_menu_bar"))
            assert eval (_choice_viewport_bounds is not None)
            assert eval (_choice_quick_bar_bounds is not None)
            assert eval (_choice_viewport_bounds.y + _choice_viewport_bounds.h <= _choice_quick_bar_bounds.y)
            screenshot "accessibility_150_choices_initial"
            scroll id "choice_scroll" amount 1000
            pause 0.5
            screenshot "accessibility_150_choices_scrolled"
            click "第七项：放下旧日的王冠，与所有盟友共同建立公开、平等而长久的新议会秩序"
            pause until screen "say" timeout 4.0
            assert eval (_test_accessibility_seventh_selected)
            click "设置"
            pause until screen "preferences" timeout 4.0
            assert screen "preferences"
            screenshot "accessibility_150_preferences"


testcase test_accessibility_migration:
    $ _legacy_accessibility = type("LegacyAccessibility", (), {})()
    $ _legacy_accessibility.text_size_offset = 8
    $ _legacy_accessibility.high_contrast = True
    $ _legacy_accessibility.accessibility_preferences_migrated = False
    $ _native_accessibility = type("NativeAccessibility", (), {})()
    $ _native_accessibility.font_size = 1.0
    $ _native_accessibility.high_contrast = False
    $ _migrate_legacy_accessibility_preferences(_legacy_accessibility, _native_accessibility)
    assert eval (_native_accessibility.font_size == 1.5)
    assert eval (_native_accessibility.high_contrast)
    assert eval (_legacy_accessibility.accessibility_preferences_migrated)

    ## A completed migration must never overwrite a later player choice.
    $ _native_accessibility.font_size = 0.9
    $ _native_accessibility.high_contrast = False
    $ _migrate_legacy_accessibility_preferences(_legacy_accessibility, _native_accessibility)
    assert eval (_native_accessibility.font_size == 0.9)
    assert eval (not _native_accessibility.high_contrast)

    ## Legacy defaults carry no intent and must preserve existing native choices.
    $ _legacy_defaults = type("LegacyAccessibilityDefaults", (), {})()
    $ _legacy_defaults.text_size_offset = 0
    $ _legacy_defaults.high_contrast = False
    $ _legacy_defaults.accessibility_preferences_migrated = False
    $ _native_existing = type("NativeAccessibilityExisting", (), {})()
    $ _native_existing.font_size = 1.25
    $ _native_existing.high_contrast = True
    $ _migrate_legacy_accessibility_preferences(_legacy_defaults, _native_existing)
    assert eval (_native_existing.font_size == 1.25)
    assert eval (_native_existing.high_contrast)


label test_accessibility_render_fixture:
    $ _test_accessibility_seventh_selected = False

    "这是百分之一百五十字号下的真实对话渲染测试：较长的句子应当完整换行，不能被对话框边缘或快捷菜单裁切。"

    menu:
        "第一项：接受摄政之位，以王廷法统维持北境来之不易的和平与稳定|权力 +10 盟友信任 -5":
            return
        "第二项：公开父亲遇害的全部证据，让贵族与教会共同接受公正审判|声望 +10 阴谋 -5":
            return
        "第三项：率领边境军团继续南下，彻底结束诸侯割据造成的漫长战乱|权力 +15 忠诚 -10":
            return
        "第四项：兑现对自由城邦的承诺，承认港口、商路与议会的自治权利|财富 +10 王廷关系 -5":
            return
        "第五项：邀请暗百合进入议会，以秘密情报守护来之不易的脆弱新秩序|阴谋 +10 教会关系 -5":
            return
        "第六项：将兵权交还各地领主，用公开盟约约束每一位未来的统治者|忠诚 +10 权力 -10":
            return
        "第七项：放下旧日的王冠，与所有盟友共同建立公开、平等而长久的新议会秩序|全体关系 +10 历史将记住这一刻":
            $ _test_accessibility_seventh_selected = True
            "第七个无障碍渲染测试分支已执行。"

    return


################################################################################
## 3.9.2 regression: every formal chapter entry must initialize a blank run once
################################################################################

testsuite test_new_run_bootstrap:
    before testcase:
        ## 全新 persistent 下 testcase hook 可能早于主菜单首帧；无论当前
        ## context 在哪里，都发出回主菜单动作并等待 screen 真正出现。
        run MainMenu(confirm=False) until screen "main_menu" timeout 4.0

        $ _test.timeout = 4.0
        $ _test.bootstrap_persistent_snapshot = {"privacy_agreed": persistent.privacy_agreed, "tutorial_seen": persistent.tutorial_seen, "ng_plus_unlocked": persistent.ng_plus_unlocked, "ng_plus_bonus_power": persistent.ng_plus_bonus_power, "ng_plus_bonus_wealth": persistent.ng_plus_bonus_wealth, "ng_plus_bonus_intrigue": persistent.ng_plus_bonus_intrigue, "difficulty": persistent.difficulty}
        $ persistent.privacy_agreed = True
        $ persistent.tutorial_seen = True
        $ persistent.ng_plus_unlocked = False
        $ persistent.ng_plus_bonus_power = 0
        $ persistent.ng_plus_bonus_wealth = 0
        $ persistent.ng_plus_bonus_intrigue = 0
        $ persistent.difficulty = "normal"

    after testcase:
        run MainMenu(confirm=False) until screen "main_menu" timeout 4.0
        $ persistent.privacy_agreed = _test.bootstrap_persistent_snapshot["privacy_agreed"]
        $ persistent.tutorial_seen = _test.bootstrap_persistent_snapshot["tutorial_seen"]
        $ persistent.ng_plus_unlocked = _test.bootstrap_persistent_snapshot["ng_plus_unlocked"]
        $ persistent.ng_plus_bonus_power = _test.bootstrap_persistent_snapshot["ng_plus_bonus_power"]
        $ persistent.ng_plus_bonus_wealth = _test.bootstrap_persistent_snapshot["ng_plus_bonus_wealth"]
        $ persistent.ng_plus_bonus_intrigue = _test.bootstrap_persistent_snapshot["ng_plus_bonus_intrigue"]
        $ persistent.difficulty = _test.bootstrap_persistent_snapshot["difficulty"]
        assert eval (all(getattr(persistent, name) == value for name, value in _test.bootstrap_persistent_snapshot.items()))
        $ renpy.save_persistent()

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
        $ _test.after_load_driver_started = False
        run Start("test_new_run_after_load_driver")
        pause until eval (_test.after_load_driver_started and "_call_show_chapter_1" in renpy.get_return_stack() and renpy.get_screen("chapter_title") is not None) timeout 4.0
        assert eval (_new_run_bootstrap_done)
        assert eval (inventory_items == [("synthetic_loaded_item", 7)])
        assert eval (_after_load_rollback_limit_before > 0)
        assert eval (_after_load_rollback_limit_after == 0)
        assert eval (_after_load_rollback_block_after > _after_load_rollback_block_before)
        assert not screen "difficulty_select"
        assert not screen "name_input_screen"
        assert eval ("_call_show_chapter_1" in renpy.get_return_stack())


label test_new_run_after_load_driver:
    $ _test.after_load_driver_started = True
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
    $ testament_original_obtained = True
    $ father_letters_found = True
    $ poison_evidence = True
    $ ending_type = "truth"
    jump ending_truth

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
    $ power = get_ending_threshold("primary")
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

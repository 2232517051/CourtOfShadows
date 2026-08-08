python early:
    if renpy.game.args.command == "test":
        config.save_token_keys.append("MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAExo2SI8BWrAFvbMVUXBKeQQh7qUUZla9zkj3pRpmgydQUvjYMGKooT+i5vs43/U/TRRcJ012sOh4KxcDYezLuJw==")


label _test_lint_reachability_root:
    if True == True:
        return


testsuite global:
    teardown:
        exit


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

    testcase ending_availability_is_an_exact_nine_key_outcome_map:
        parameter (route_kwargs, resistance_kwargs, expected_endings) = [
            (
                {"difficulty": "hard", "power": 72},
                {"difficulty": "hard", "power": 72},
                {"iron_lord": True, "shadow_king": False, "holy_guardian": False, "peoples_lord": False, "truth": False, "borgia": False, "vassal": False, "fall": False, "sea": False},
            ),
            (
                {"difficulty": "normal", "power": 55, "rel_baron": -1, "rel_queen": -1},
                {"difficulty": "normal", "power": 55, "rel_baron": -1},
                {"iron_lord": True, "shadow_king": False, "holy_guardian": False, "peoples_lord": False, "truth": False, "borgia": False, "vassal": False, "fall": True, "sea": False},
            ),
            (
                {"difficulty": "hard", "rel_baron": 30},
                {"difficulty": "hard", "rel_baron": 30},
                {"iron_lord": False, "shadow_king": False, "holy_guardian": False, "peoples_lord": False, "truth": False, "borgia": False, "vassal": False, "fall": True, "sea": False},
            ),
            (
                {"difficulty": "hard", "rel_baron": 30},
                {"difficulty": "hard", "rel_baron": 30, "alliance_baron": True, "baron_supply_intel": True},
                {"iron_lord": True, "shadow_king": False, "holy_guardian": False, "peoples_lord": False, "truth": False, "borgia": False, "vassal": False, "fall": False, "sea": False},
            ),
            (
                {"difficulty": "hard", "rel_baron": 30},
                {"difficulty": "hard", "rel_baron": 30, "baron_supply_intel": True},
                {"iron_lord": True, "shadow_king": False, "holy_guardian": False, "peoples_lord": False, "truth": False, "borgia": False, "vassal": False, "fall": True, "sea": False},
            ),
            (
                {"difficulty": "hard", "southern_outcome": "free"},
                None,
                {"iron_lord": False, "shadow_king": False, "holy_guardian": False, "peoples_lord": False, "truth": False, "borgia": False, "vassal": False, "fall": True, "sea": True},
            ),
        ]

        $ _exact_routes = get_finale_route_availability(**route_kwargs)
        $ _resistance_outcomes = None if resistance_kwargs is None else get_resistance_battle_outcomes(**resistance_kwargs)
        $ _exact_endings = get_finale_ending_availability(_exact_routes, _resistance_outcomes)
        assert eval (_exact_endings == expected_endings)
        assert eval (set(_exact_endings.keys()) == set(_ending_keys))

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
        ]

        $ _ending_routes = get_finale_ending_availability(get_finale_route_availability(**route_kwargs))
        assert eval (_ending_routes[ending_id])


################################################################################
## 3.10 regression: balance report copy must describe real battle outcomes.
################################################################################

testsuite test_balance_ending_report:
    before testcase:
        $ _test.balance_report_store_names = ("power", "intrigue", "faith", "loyalty", "wealth", "rel_baron", "rel_queen", "lily_full_member", "father_poison_method_known", "father_poison_executor_known", "father_murder_mastermind_known", "testament_original_obtained", "deep_mother_herb", "poison_evidence", "southern_outcome", "alliance_baron", "prince_ally", "rel_captain", "ch5_pay_advance_pension", "marriage_route", "iron_thorn_controlled", "baron_supply_intel")
        $ _test.balance_report_store_snapshot = {name: getattr(store, name) for name in _test.balance_report_store_names}
        $ _test.balance_report_persistent_snapshot = {"difficulty": persistent.difficulty}
        $ _test.balance_report_defaults = {"power": 0, "intrigue": 0, "faith": 0, "loyalty": 0, "wealth": 0, "rel_baron": -1, "rel_queen": -1, "lily_full_member": False, "father_poison_method_known": False, "father_poison_executor_known": False, "father_murder_mastermind_known": False, "testament_original_obtained": False, "deep_mother_herb": "", "poison_evidence": False, "southern_outcome": "none", "alliance_baron": False, "prince_ally": False, "rel_captain": 0, "ch5_pay_advance_pension": False, "marriage_route": False, "iron_thorn_controlled": False, "baron_supply_intel": False}
        $ [setattr(store, name, value) for name, value in _test.balance_report_defaults.items()]

    after testcase:
        $ [setattr(store, name, value) for name, value in _test.balance_report_store_snapshot.items()]
        $ persistent.difficulty = _test.balance_report_persistent_snapshot["difficulty"]
        assert eval (all(getattr(store, name) == value for name, value in _test.balance_report_store_snapshot.items()))
        assert eval (persistent.difficulty == _test.balance_report_persistent_snapshot["difficulty"])
        $ renpy.save_persistent()

    testcase normal_direct_iron_report_includes_win_and_loss:
        $ persistent.difficulty = "normal"
        $ power = 55
        $ _balance_report = {row[0]: row for row in check_ending_reachability()}
        assert eval (_balance_report["iron_lord"][2])
        assert eval (_balance_report["fall"][2])
        assert eval (_balance_report["iron_lord"][3] == "已满足条件")
        assert eval (_balance_report["fall"][3] == "已满足条件")
        assert eval (_ending_requirements["iron_lord"]["requirement"] == "权力路线可选，或铁腕会战存在胜利路径")
        assert eval (_ending_requirements["fall"]["desc"] == "未能守住艾登堡（失败结局）")
        assert eval (_ending_requirements["fall"]["requirement"] == "没有其他核心路线可选，或铁腕会战存在战败路径")

    testcase supported_hard_resistance_report_has_no_loss_path:
        $ persistent.difficulty = "hard"
        $ rel_baron = 30
        $ alliance_baron = True
        $ baron_supply_intel = True
        $ _balance_report = {row[0]: row for row in check_ending_reachability()}
        assert eval (_balance_report["iron_lord"][2])
        assert eval (not _balance_report["fall"][2])
        assert eval (_balance_report["fall"][3] == "仍有其他核心路线可选；铁腕会战当前没有战败路径")

    testcase unsupported_hard_resistance_report_has_no_win_path:
        $ persistent.difficulty = "hard"
        $ rel_baron = 30
        $ _balance_report = {row[0]: row for row in check_ending_reachability()}
        assert eval (not _balance_report["iron_lord"][2])
        assert eval (_balance_report["fall"][2])
        assert eval (_balance_report["iron_lord"][3] == "铁腕会战当前没有胜利路径")


testsuite test_resistance_battle_transition:
    before testcase:
        $ _test.resistance_difficulty_snapshot = persistent.difficulty

    after testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False) until screen "main_menu" timeout 4.0
        $ persistent.difficulty = _test.resistance_difficulty_snapshot
        $ renpy.save_persistent()

    testcase low_score_hard_resistance_reaches_grind_failure:
        $ _test.timeout = 30.0
        run Start("test_resistance_battle_loss_fixture") until screen "say" timeout 4.0
        advance until screen "choice" timeout 30.0
        pause 1.0
        click "截断补给线——让他们饿三天再打"
        pause 0.5
        advance until screen "choice" timeout 30.0
        pause 1.0
        click "亲自率领前锋出击"
        pause 0.5
        advance until screen "choice" timeout 30.0
        pause 1.0
        $ _test.choice_text = "记住这一切，继续前进"
        pause until eval (len([f for f in renpy.display.focus.focus_list if f.x is not None and _test.choice_text.casefold() in f.widget._tts_all(True).casefold() and isinstance(getattr(f.widget, "action", None), renpy.ui.ChoiceReturn)]) == 1) timeout 4.0
        click "记住这一切，继续前进"
        pause 0.5
        advance until screen "choice" timeout 30.0
        pause 1.0
        assert eval (not _iron_prepared)
        assert eval (iron_war_score < 12 + get_war_threshold_mod())
        click "硬拼——你没有更好的选择了"
        pause 0.5
        advance
        advance
        advance
        advance until eval (ending_type == "fall") timeout 10.0
        assert eval (ending_type == "fall")


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


## BEGIN TASK 3 WINTER STATE SUITES
init python:
    _WINTER_ALLOWED_STORE_DEFAULT_WRITES = (
        "governance_events_seen",
        "winter_interlude_status",
        "winter_investigations",
        "winter_policy",
        "winter_seed_priority",
    )
    _WINTER_NONDEFAULT_FORBIDDEN_STATE = (
        "_iron_prepared",
        "ch3_lily_alliance_independent",
    )

    def _test_winter_project_default_names(store_name):
        names = set()
        for statement in renpy.ast.default_statements:
            if not isinstance(statement, renpy.ast.Default):
                continue
            filename = str(statement.filename).replace("\\", "/")
            project_source = filename.startswith("game/") or "/game/" in filename
            if not project_source or filename.endswith("game/test_game.rpy"):
                continue
            if statement.store == store_name:
                names.add(statement.varname)
        return tuple(sorted(names))

    def _test_winter_freeze(value):
        if isinstance(value, dict):
            frozen_items = (
                (_test_winter_freeze(key), _test_winter_freeze(item))
                for key, item in value.items()
            )
            return (type(value).__name__, tuple(sorted(frozen_items, key=repr)))
        if isinstance(value, (list, tuple)):
            return (type(value).__name__, tuple(_test_winter_freeze(item) for item in value))
        if isinstance(value, (set, frozenset)):
            frozen_items = (_test_winter_freeze(item) for item in value)
            return (type(value).__name__, tuple(sorted(frozen_items, key=repr)))
        if isinstance(value, (bool, bytes, float, int, str, type(None))):
            return (type(value).__name__, value)
        raise TypeError("unsupported winter snapshot type: {}".format(type(value).__name__))

    def _test_winter_trace_label(name, abnormal):
        del abnormal
        if not getattr(_test, "winter_trace_enabled", False):
            return
        _test.winter_labels.append(name)
        if name in ("_call_gov_merch2", "_call_gov_build2", "_call_gov_famine2"):
            _test.winter_pad_snapshots[name] = (
                gov_merchant_outcome,
                built_granary,
                famine_prevented,
                renpy.music.get_playing(channel="music"),
            )

    def _test_winter_begin_trace():
        _test.winter_trace_enabled = True
        _test.winter_labels = []
        _test.winter_pad_snapshots = {}
        if _test_winter_trace_label not in config.label_callbacks:
            config.label_callbacks.append(_test_winter_trace_label)

    def _test_winter_end_trace():
        _test.winter_trace_enabled = False
        while _test_winter_trace_label in config.label_callbacks:
            config.label_callbacks.remove(_test_winter_trace_label)

    def _test_winter_track(channel="music"):
        playing = renpy.music.get_playing(channel=channel)
        if playing is None:
            return None
        return str(playing).replace("\\", "/")

    def _test_winter_choice_ready(text):
        matches = [
            focus
            for focus in renpy.display.focus.focus_list
            if focus.x is not None
            and text.casefold() in focus.widget._tts_all(True).casefold()
            and isinstance(getattr(focus.widget, "action", None), renpy.ui.ChoiceReturn)
        ]
        return len(matches) == 1

    def _test_winter_action_ready(text):
        matches = [
            focus
            for focus in renpy.display.focus.focus_list
            if focus.x is not None
            and text.casefold() in focus.widget._tts_all(True).casefold()
            and getattr(focus.widget, "action", None) is not None
        ]
        return len(matches) == 1


testsuite test_winter_interlude_state:
    before testcase:
        $ assert "winter_interlude_status" in globals(), "winter state helper missing"
        $ _test.winter_state_snapshot = (winter_interlude_status, tuple(winter_investigations), winter_policy, winter_seed_priority, list(governance_events_seen), famine_prevented, gov_merchant_outcome)

    after testcase:
        $ winter_interlude_status, winter_investigations, winter_policy, winter_seed_priority, _winter_events, famine_prevented, gov_merchant_outcome = _test.winter_state_snapshot
        $ governance_events_seen[:] = _winter_events

    testcase status_precedence_matrix:
        parameter (raw_snapshot, projection, expected_winter) = [
            (("legacy", "trade", "preserve", ("market", "route"), True, "regulated", ("famine_crisis",)), "internal", ("legacy", ("market", "route"), "trade", "preserve")),
            (("delegated", "trade", "preserve", ("market", "route"), True, "regulated", ("famine_crisis",)), "internal", ("delegated", (), "delegated", "neutral")),
            (("completed", "trade", "feed_now", ("route", "market"), False, "", ()), "internal", ("completed", ("market", "route"), "trade", "feed_now")),
            (("active", "ration", "neutral", ("village",), False, "", ("merchant_negotiation",)), "internal", ("active", ("village",), "ration", "neutral")),
            (("active", "ration", "neutral", ("village",), False, "", ("merchant_negotiation",)), "outside", ("delegated", (), "delegated", "neutral")),
            (("unseen", "", "neutral", (), True, "", ()), "internal", ("legacy", (), "", "neutral")),
            (("unseen", "", "neutral", (), False, "regulated", ()), "internal", ("legacy", (), "", "neutral")),
            (("unseen", "", "neutral", (), False, "", ("famine_crisis",)), "internal", ("legacy", (), "", "neutral")),
            (("unseen", "", "neutral", (), False, "", ("merchant_negotiation",)), "internal", ("legacy", (), "", "neutral")),
            (("unseen", "", "neutral", (), False, "", ()), "internal", ("unseen", (), "", "neutral")),
            (("unseen", "", "neutral", (), False, "", ()), "outside", ("delegated", (), "delegated", "neutral")),
            (("damaged", "trade", "preserve", ("market", "village"), True, "regulated", ("famine_crisis",)), "internal", ("delegated", (), "delegated", "neutral")),
        ]

        $ assert "resolve_winter_interlude_context" in globals(), "winter state helper missing"
        $ _winter_context = resolve_winter_interlude_context(raw_snapshot, projection)
        assert eval (isinstance(_winter_context, tuple))
        assert eval ((_winter_context.status, _winter_context.investigations, _winter_context.policy, _winter_context.seed_priority) == expected_winter)

    testcase delegation_is_idempotent:
        $ governance_events_seen[:] = []
        $ apply_winter_delegation()
        $ apply_winter_delegation()
        assert eval ((winter_interlude_status, winter_investigations, winter_policy, winter_seed_priority) == ("delegated", (), "delegated", "neutral"))
        assert eval (governance_events_seen.count("winter_interlude") == 1)
        assert eval (governance_events_seen.count("famine_crisis") == 1)
        assert eval ("merchant_negotiation" not in governance_events_seen)

    testcase finalizer_compatibility_markers_are_idempotent:
        $ governance_events_seen[:] = []
        $ _first_finalize = finalize_winter_interlude("trade", "preserve", ("route", "market"))
        $ _second_finalize = finalize_winter_interlude("trade", "preserve", ("market", "route"))
        assert eval (_first_finalize and _second_finalize)
        assert eval ((winter_interlude_status, winter_investigations, winter_policy, winter_seed_priority) == ("completed", ("market", "route"), "trade", "preserve"))
        assert eval (governance_events_seen.count("winter_interlude") == 1)
        assert eval (governance_events_seen.count("famine_crisis") == 1)
        assert eval ("merchant_negotiation" not in governance_events_seen)
        assert eval (get_winter_context(outside=False).status == "completed")

    testcase invalid_values_fall_back_to_neutral:
        parameter (policy_name, seed_name, investigation_values) = [
            ("invalid", "preserve", ("market", "village")),
            ("trade", "invalid", ("market", "village")),
            ("trade", "preserve", ()),
            ("trade", "preserve", ("market",)),
            ("trade", "preserve", ("market", "market")),
            ("trade", "preserve", ("market", "village", "route")),
            ("trade", "preserve", ("market", "unknown")),
            ("trade", "preserve", ("market", "village", "unknown")),
        ]

        $ governance_events_seen[:] = []
        $ _winter_valid = finalize_winter_interlude(policy_name, seed_name, investigation_values)
        assert eval (not _winter_valid)
        assert eval ((winter_interlude_status, winter_investigations, winter_policy, winter_seed_priority) == ("delegated", (), "delegated", "neutral"))
        assert eval (governance_events_seen == ["winter_interlude", "famine_crisis"])

    testcase invalid_completed_payload_never_reclassifies_as_legacy:
        parameter raw_snapshot = [
            ("completed", "invalid", "preserve", ("market", "village"), True, "regulated", ("famine_crisis", "merchant_negotiation")),
            ("completed", "trade", "invalid", ("market", "village"), True, "regulated", ("famine_crisis", "merchant_negotiation")),
            ("completed", "trade", "preserve", ("market", "market"), True, "regulated", ("famine_crisis", "merchant_negotiation")),
            ("completed", "trade", "preserve", ("market", "village", "route"), True, "regulated", ("famine_crisis", "merchant_negotiation")),
        ]

        $ _winter_internal = resolve_winter_interlude_context(raw_snapshot, "internal")
        $ _winter_outside = resolve_winter_interlude_context(raw_snapshot, "outside")
        assert eval ((_winter_internal.status, _winter_internal.investigations, _winter_internal.policy, _winter_internal.seed_priority) == ("delegated", (), "delegated", "neutral"))
        assert eval ((_winter_outside.status, _winter_outside.investigations, _winter_outside.policy, _winter_outside.seed_priority) == ("delegated", (), "delegated", "neutral"))

    testcase twelve_orders_normalize_to_six_pairs:
        parameter (ordered_values, expected_pair) = [
            (("market", "village"), ("market", "village")),
            (("village", "market"), ("market", "village")),
            (("market", "granary"), ("market", "granary")),
            (("granary", "market"), ("market", "granary")),
            (("market", "route"), ("market", "route")),
            (("route", "market"), ("market", "route")),
            (("village", "granary"), ("village", "granary")),
            (("granary", "village"), ("village", "granary")),
            (("village", "route"), ("village", "route")),
            (("route", "village"), ("village", "route")),
            (("granary", "route"), ("granary", "route")),
            (("route", "granary"), ("granary", "route")),
        ]

        assert eval (normalize_winter_investigations(ordered_values) == expected_pair)

    testcase thirty_six_core_combinations_have_benefit_and_burden:
        parameter (investigation_pair, policy_name, seed_name) = [
            (pair, policy, seed)
            for pair in (("market", "village"), ("market", "granary"), ("market", "route"), ("village", "granary"), ("village", "route"), ("granary", "route"))
            for policy in ("trade", "ration", "requisition")
            for seed in ("preserve", "feed_now")
        ]

        $ _winter_valid = finalize_winter_interlude(policy_name, seed_name, investigation_pair)
        $ _winter_outcome = WINTER_OUTCOME_CONTRACTS[(policy_name, seed_name)]
        assert eval (_winter_valid)
        assert eval (all(_winter_outcome[key] for key in ("benefit", "burden", "followup")))
        assert eval ((winter_policy, winter_seed_priority, winter_investigations) == (policy_name, seed_name, investigation_pair))

    testcase four_investigations_only_mitigate_their_named_cost:
        $ _winter_pairs = (("market", "village"), ("market", "granary"), ("market", "route"), ("village", "granary"), ("village", "route"), ("granary", "route"))
        $ _winter_observed = {(pair, policy, seed): select_winter_mitigation(policy, seed, pair, {}) for pair in _winter_pairs for policy in WINTER_POLICIES for seed in WINTER_SEED_PRIORITIES}
        python:
            _winter_expected = {
                (("market", "village"), "trade", "preserve"): "market_trade",
                (("market", "village"), "trade", "feed_now"): "market_trade",
                (("market", "village"), "ration", "preserve"): "village_preserve",
                (("market", "village"), "requisition", "preserve"): "village_preserve",
                (("market", "granary"), "trade", "preserve"): "market_trade",
                (("market", "granary"), "trade", "feed_now"): "market_trade",
                (("market", "granary"), "ration", "preserve"): "granary_ration",
                (("market", "granary"), "ration", "feed_now"): "granary_ration",
                (("market", "route"), "trade", "preserve"): "market_trade",
                (("market", "route"), "trade", "feed_now"): "market_trade",
                (("market", "route"), "ration", "feed_now"): "route_feed_now",
                (("market", "route"), "requisition", "feed_now"): "route_feed_now",
                (("village", "granary"), "trade", "preserve"): "village_preserve",
                (("village", "granary"), "ration", "preserve"): "granary_ration",
                (("village", "granary"), "ration", "feed_now"): "granary_ration",
                (("village", "granary"), "requisition", "preserve"): "village_preserve",
                (("village", "route"), "trade", "preserve"): "village_preserve",
                (("village", "route"), "trade", "feed_now"): "route_feed_now",
                (("village", "route"), "ration", "preserve"): "village_preserve",
                (("village", "route"), "ration", "feed_now"): "route_feed_now",
                (("village", "route"), "requisition", "preserve"): "village_preserve",
                (("village", "route"), "requisition", "feed_now"): "route_feed_now",
                (("granary", "route"), "trade", "feed_now"): "route_feed_now",
                (("granary", "route"), "ration", "preserve"): "granary_ration",
                (("granary", "route"), "ration", "feed_now"): "granary_ration",
                (("granary", "route"), "requisition", "feed_now"): "route_feed_now",
            }
        assert eval ({key: value for key, value in _winter_observed.items() if value is not None} == _winter_expected)


testsuite test_winter_interlude_legacy_migration:
    before testcase:
        $ _test.winter_migration_snapshot = (winter_interlude_status, tuple(winter_investigations), winter_policy, winter_seed_priority, list(governance_events_seen), famine_prevented, gov_merchant_outcome)

    after testcase:
        $ winter_interlude_status, winter_investigations, winter_policy, winter_seed_priority, _winter_events, famine_prevented, gov_merchant_outcome = _test.winter_migration_snapshot
        $ governance_events_seen[:] = _winter_events
        $ renpy.unlink_save("winter-active-mid-save")

    testcase unseen_plus_famine_success_becomes_legacy:
        $ winter_interlude_status, winter_investigations, winter_policy, winter_seed_priority = "unseen", (), "", "neutral"
        $ famine_prevented, gov_merchant_outcome = True, ""
        $ governance_events_seen[:] = []
        $ migrate_winter_interlude_state()
        assert eval (winter_interlude_status == "legacy")
        assert eval (winter_legacy_famine_success())

    testcase unseen_plus_merchant_outcome_becomes_legacy:
        $ winter_interlude_status, winter_investigations, winter_policy, winter_seed_priority = "unseen", (), "", "neutral"
        $ famine_prevented, gov_merchant_outcome = False, "regulated"
        $ governance_events_seen[:] = []
        $ migrate_winter_interlude_state()
        assert eval (winter_interlude_status == "legacy")
        assert eval (gov_merchant_outcome == "regulated")

    testcase unseen_plus_famine_marker_without_success_becomes_legacy:
        $ winter_interlude_status, winter_investigations, winter_policy, winter_seed_priority = "unseen", (), "", "neutral"
        $ famine_prevented, gov_merchant_outcome = False, ""
        $ governance_events_seen[:] = ["famine_crisis"]
        $ migrate_winter_interlude_state()
        assert eval (winter_interlude_status == "legacy")
        assert eval (not winter_legacy_famine_success())

    testcase explicit_delegated_beats_stale_legacy_markers:
        $ winter_interlude_status, winter_investigations, winter_policy, winter_seed_priority = "delegated", ("market", "route"), "trade", "preserve"
        $ famine_prevented, gov_merchant_outcome = True, "regulated"
        $ governance_events_seen[:] = ["famine_crisis", "merchant_negotiation"]
        $ migrate_winter_interlude_state()
        assert eval ((winter_interlude_status, winter_investigations, winter_policy, winter_seed_priority) == ("delegated", (), "delegated", "neutral"))
        assert eval (not winter_legacy_famine_success())

    testcase active_mid_interlude_survives_after_load:
        run Start("test_winter_active_save_driver") until screen "say" timeout 4.0
        assert eval (renpy.can_load("winter-active-mid-save"))
        click
        pause until screen "main_menu" timeout 4.0
        $ winter_interlude_status, winter_investigations, winter_policy, winter_seed_priority = "delegated", (), "delegated", "neutral"
        run FileLoad("winter-active-mid-save", confirm=False, slot=True) until screen "say" timeout 4.0
        assert eval ((winter_interlude_status, winter_investigations, winter_policy, winter_seed_priority) == ("active", ("market",), "trade", "neutral"))
        assert eval (get_winter_context(outside=False).status == "active")
        assert eval (get_winter_context(outside=True).status == "delegated")
        run MainMenu(confirm=False) until screen "main_menu" timeout 4.0

    testcase no_evidence_outside_interlude_reads_as_neutral:
        $ winter_interlude_status, winter_investigations, winter_policy, winter_seed_priority = "unseen", (), "", "neutral"
        $ famine_prevented, gov_merchant_outcome = False, ""
        $ governance_events_seen[:] = []
        $ migrate_winter_interlude_state()
        assert eval (winter_interlude_status == "unseen")
        assert eval ((get_winter_context(outside=True).status, get_winter_context(outside=True).policy, get_winter_context(outside=True).seed_priority) == ("delegated", "delegated", "neutral"))

    testcase real_famine_success_after_save_loads_as_legacy:
        run FileLoad("winter-legacy-famine-success-after", confirm=False, slot=True) until eval (winter_interlude_status == "legacy") timeout 4.0
        assert eval (famine_prevented)
        assert eval (winter_legacy_famine_success())
        run MainMenu(confirm=False) until screen "main_menu" timeout 4.0

    testcase real_chapter2_no_governance_save_loads_as_neutral:
        run FileLoad("winter-legacy-chapter2-no-governance", confirm=False, slot=True) until eval (winter_interlude_status == "unseen") timeout 4.0
        assert eval (not famine_prevented and not gov_merchant_outcome)
        assert eval (get_winter_context(outside=True).status == "delegated")
        run MainMenu(confirm=False) until screen "main_menu" timeout 4.0


testsuite test_winter_interlude_ending_invariance:
    testcase every_core_and_delegated_result_preserves_forbidden_state:
        parameter (policy_name, seed_name, investigation_pair) = [
            (policy, seed, pair)
            for pair in (("market", "village"), ("market", "granary"), ("market", "route"), ("village", "granary"), ("village", "route"), ("granary", "route"))
            for policy in ("trade", "ration", "requisition")
            for seed in ("preserve", "feed_now")
        ] + [(None, None, ())]

        $ governance_events_seen[:] = []
        $ _winter_store_default_names = tuple(name for name in _test_winter_project_default_names("store") if name not in _WINTER_ALLOWED_STORE_DEFAULT_WRITES)
        $ _winter_persistent_default_names = _test_winter_project_default_names("store.persistent")
        assert eval ({"path_marks_martial", "path_active_martial", "dark_lily_joined", "dark_lily_destroyed", "governance_prosperity", "ending_epilogue_seen", "iron_battle_outcome"}.issubset(set(_winter_store_default_names)))
        assert eval ({"achievements", "endings_seen", "northern_endings_seen", "southern_endings_seen", "difficulty"}.issubset(set(_winter_persistent_default_names)))
        $ _winter_forbidden_snapshot = {name: _test_winter_freeze(getattr(store, name)) for name in _winter_store_default_names}
        $ _winter_persistent_snapshot = {name: (hasattr(persistent, name), _test_winter_freeze(getattr(persistent, name, None))) for name in _winter_persistent_default_names}
        $ _winter_optional_snapshot = {name: (hasattr(store, name), _test_winter_freeze(getattr(store, name, None))) for name in _WINTER_NONDEFAULT_FORBIDDEN_STATE}
        $ _winter_route_kwargs = {"difficulty": "hard", "power": 72, "father_murder_mastermind_known": True, "testament_original_obtained": True, "southern_outcome": "free"}
        $ _winter_battle_kwargs = {"difficulty": "hard", "power": 72, "alliance_baron": True, "rel_baron": 30, "baron_supply_intel": True}
        $ _winter_routes_before = get_finale_route_availability(**_winter_route_kwargs)
        $ _winter_battle_before = get_resistance_battle_outcomes(**_winter_battle_kwargs)
        $ _winter_endings_before = get_finale_ending_availability(_winter_routes_before, _winter_battle_before)
        $ _winter_write_result = apply_winter_delegation() if policy_name is None else finalize_winter_interlude(policy_name, seed_name, investigation_pair)
        $ _winter_store_changes = {name: (value, _test_winter_freeze(getattr(store, name))) for name, value in _winter_forbidden_snapshot.items() if _test_winter_freeze(getattr(store, name)) != value}
        $ _winter_optional_changes = {name: (value, (hasattr(store, name), _test_winter_freeze(getattr(store, name, None)))) for name, value in _winter_optional_snapshot.items() if (hasattr(store, name), _test_winter_freeze(getattr(store, name, None))) != value}
        $ _winter_persistent_changes = {name: (value, (hasattr(persistent, name), _test_winter_freeze(getattr(persistent, name, None)))) for name, value in _winter_persistent_snapshot.items() if (hasattr(persistent, name), _test_winter_freeze(getattr(persistent, name, None))) != value}
        assert eval (_winter_store_changes == {})
        assert eval (_winter_optional_changes == {})
        assert eval (_winter_persistent_changes == {})
        assert eval (get_finale_route_availability(**_winter_route_kwargs) == _winter_routes_before)
        assert eval (get_resistance_battle_outcomes(**_winter_battle_kwargs) == _winter_battle_before)
        assert eval (get_finale_ending_availability(get_finale_route_availability(**_winter_route_kwargs), get_resistance_battle_outcomes(**_winter_battle_kwargs)) == _winter_endings_before)

    testcase easy_normal_hard_boundary_route_sets_are_identical:
        parameter (difficulty_name, main_value) = [
            ("easy", 54), ("easy", 55), ("easy", 56),
            ("normal", 64), ("normal", 65), ("normal", 66),
            ("hard", 71), ("hard", 72), ("hard", 73),
        ]

        $ _winter_route_kwargs = {"difficulty": difficulty_name, "power": main_value}
        $ _winter_routes_before = get_finale_route_availability(**_winter_route_kwargs)
        $ _winter_endings_before = get_finale_ending_availability(_winter_routes_before)
        $ finalize_winter_interlude("ration", "feed_now", ("village", "granary"))
        assert eval (get_finale_route_availability(**_winter_route_kwargs) == _winter_routes_before)
        assert eval (get_finale_ending_availability(get_finale_route_availability(**_winter_route_kwargs)) == _winter_endings_before)

    testcase truth_lily_borgia_sea_fall_sets_are_identical:
        parameter route_kwargs = [
            {"difficulty": "hard", "father_murder_mastermind_known": True, "testament_original_obtained": True},
            {"difficulty": "hard", "faith": 80, "lily_full_member": True},
            {"difficulty": "hard", "intrigue": 70, "deep_mother_herb": "poison", "poison_evidence": True},
            {"difficulty": "hard", "southern_outcome": "free"},
            {"difficulty": "hard"},
        ]

        $ _winter_routes_before = get_finale_route_availability(**route_kwargs)
        $ _winter_endings_before = get_finale_ending_availability(_winter_routes_before)
        $ finalize_winter_interlude("requisition", "preserve", ("market", "route"))
        assert eval (get_finale_route_availability(**route_kwargs) == _winter_routes_before)
        assert eval (get_finale_ending_availability(get_finale_route_availability(**route_kwargs)) == _winter_endings_before)

    testcase resistance_battle_outcomes_are_identical:
        parameter battle_kwargs = [
            {"difficulty": "easy", "power": 40, "intrigue": 35, "loyalty": 35},
            {"difficulty": "normal", "power": 55, "intrigue": 45, "loyalty": 50},
            {"difficulty": "hard", "power": 72},
            {"difficulty": "hard", "rel_baron": 30},
            {"difficulty": "hard", "alliance_baron": True, "rel_baron": 30, "baron_supply_intel": True},
            {"difficulty": "hard", "prince_ally": True, "rel_captain": 60, "ch5_pay_advance_pension": True, "marriage_route": True, "iron_thorn_controlled": True},
        ]

        $ _winter_battle_before = get_resistance_battle_outcomes(**battle_kwargs)
        $ finalize_winter_interlude("trade", "feed_now", ("market", "granary"))
        assert eval (get_resistance_battle_outcomes(**battle_kwargs) == _winter_battle_before)


testsuite test_winter_interlude_continuations:
    before testcase:
        run MainMenu(confirm=False) until screen "main_menu" timeout 4.0
        $ _test_winter_begin_trace()

    after testcase:
        run MainMenu(confirm=False) until screen "main_menu" timeout 4.0
        $ _test_winter_end_trace()
        $ renpy.music.stop(channel="sound")

    testcase merchant_save_returns_through_only_merchant_pad:
        run FileLoad("winter-legacy-merchant-inside", confirm=False, slot=True) until screen "choice" timeout 4.0
        assert eval (renpy.get_return_stack() == ["_call_gov_merch2"])
        $ set_weather("snow")
        $ renpy.show("aldric_img")
        $ renpy.music.play("audio/sfx/fire_crackle.ogg", channel="sound", loop=True)
        $ _test.choice_text = "有限合作——设立监管，允许商会经营但限制价格"
        pause until eval (len([f for f in renpy.display.focus.focus_list if f.x is not None and _test.choice_text.casefold() in f.widget._tts_all(True).casefold() and isinstance(getattr(f.widget, "action", None), renpy.ui.ChoiceReturn)]) == 1) timeout 4.0
        click "有限合作——设立监管，允许商会经营但限制价格"
        advance until eval ("ch2_after_winter_interlude" in _test.winter_labels) timeout 30.0
        assert eval ([name for name in _test.winter_labels if name in ("_call_gov_merch2", "_call_gov_build2", "_call_gov_famine2")] == ["_call_gov_merch2"])
        assert eval (winter_interlude_status == "legacy")
        assert eval (gov_merchant_outcome == "regulated")
        assert eval (_test.winter_pad_snapshots["_call_gov_merch2"][0] == "regulated")
        assert eval (_test_winter_track("music") == str(_test.winter_pad_snapshots["_call_gov_merch2"][3]).replace("\\", "/"))
        assert eval (_test_winter_track("sound") is None and get_weather() is None)
        assert eval (not set(renpy.get_showing_tags(layer="master")).intersection(CHAR_IMG_TAGS))

    testcase building_save_returns_through_only_building_pad:
        run FileLoad("winter-legacy-building-inside", confirm=False, slot=True) until screen "choice" timeout 4.0
        assert eval (renpy.get_return_stack() == ["_call_gov_build2"])
        $ set_weather("snow")
        $ renpy.show("aldric_img")
        $ renpy.music.play("audio/sfx/fire_crackle.ogg", channel="sound", loop=True)
        $ _test.building_before = (gov_merchant_outcome, built_granary, famine_prevented)
        $ _test.choice_text = "暂不建设——把人手和石料留到下一季"
        pause until eval (len([f for f in renpy.display.focus.focus_list if f.x is not None and _test.choice_text.casefold() in f.widget._tts_all(True).casefold() and isinstance(getattr(f.widget, "action", None), renpy.ui.ChoiceReturn)]) == 1) timeout 4.0
        click "暂不建设——把人手和石料留到下一季"
        advance until eval ("ch2_after_legacy_governance" in _test.winter_labels) timeout 30.0
        assert eval ([name for name in _test.winter_labels if name in ("_call_gov_merch2", "_call_gov_build2", "_call_gov_famine2")] == ["_call_gov_build2"])
        assert eval (winter_interlude_status == "legacy")
        assert eval ((gov_merchant_outcome, built_granary, famine_prevented) == _test.building_before)
        assert eval (_test.winter_pad_snapshots["_call_gov_build2"][:3] == _test.building_before)
        assert eval (_test_winter_track("music") == str(_test.winter_pad_snapshots["_call_gov_build2"][3]).replace("\\", "/"))
        assert eval (_test_winter_track("sound") is None and get_weather() is None)
        assert eval (not set(renpy.get_showing_tags(layer="master")).intersection(CHAR_IMG_TAGS))

    testcase famine_save_returns_through_only_famine_pad:
        run FileLoad("winter-legacy-famine-inside", confirm=False, slot=True) until screen "choice" timeout 4.0
        assert eval (renpy.get_return_stack() == ["_call_gov_famine2"])
        $ set_weather("snow")
        $ renpy.show("aldric_img")
        $ renpy.music.play("audio/sfx/fire_crackle.ogg", channel="sound", loop=True)
        $ _test.choice_text = "购买粮食——花钱买平安，用金币换性命"
        pause until eval (len([f for f in renpy.display.focus.focus_list if f.x is not None and _test.choice_text.casefold() in f.widget._tts_all(True).casefold() and isinstance(getattr(f.widget, "action", None), renpy.ui.ChoiceReturn)]) == 1) timeout 4.0
        click "购买粮食——花钱买平安，用金币换性命"
        advance until eval ("ch2_after_legacy_governance" in _test.winter_labels) timeout 30.0
        assert eval ([name for name in _test.winter_labels if name in ("_call_gov_merch2", "_call_gov_build2", "_call_gov_famine2")] == ["_call_gov_famine2"])
        assert eval (winter_interlude_status == "legacy")
        assert eval (famine_prevented)
        assert eval (_test.winter_pad_snapshots["_call_gov_famine2"][2])
        assert eval (_test_winter_track("music") == str(_test.winter_pad_snapshots["_call_gov_famine2"][3]).replace("\\", "/"))
        assert eval (_test_winter_track("sound") is None and get_weather() is None)
        assert eval (not set(renpy.get_showing_tags(layer="master")).intersection(CHAR_IMG_TAGS))


testsuite test_winter_interlude_routing:
    before testcase:
        run MainMenu(confirm=False) until screen "main_menu" timeout 4.0
        $ _test_winter_begin_trace()
        $ renpy.unlink_save("auto_ch-winter_interlude")

    after testcase:
        run MainMenu(confirm=False) until screen "main_menu" timeout 4.0
        $ _test_winter_end_trace()
        $ renpy.unlink_save("auto_ch-winter_interlude")
        $ renpy.music.stop(channel="sound")

    testcase completed_delegated_active_and_invalid_reentries_never_use_pads:
        parameter (entry_state, expected_state) = [
            (("completed", ("market", "route"), "trade", "preserve"), "completed"),
            (("delegated", (), "delegated", "neutral"), "delegated"),
            (("legacy", (), "", "neutral"), "legacy"),
            (("active", ("market",), "trade", "neutral"), "delegated"),
            (("damaged", ("market",), "trade", "preserve"), "delegated"),
        ]
        assert eval (renpy.has_label("winter_interlude_start"))
        $ _test.winter_route_state = entry_state
        run Start("test_winter_routing_driver") until eval ("chapter2_start" in _test.winter_labels) timeout 6.0
        assert eval (winter_interlude_status == expected_state)
        assert eval (not any(name in _test.winter_labels for name in ("_call_gov_merch2", "_call_gov_build2", "_call_gov_famine2")))
        assert eval (not renpy.can_load("auto_ch-winter_interlude"))
        assert eval (get_weather() is None and renpy.get_screen("weather_snow") is None)
        assert eval (not set(renpy.get_showing_tags(layer="master")).intersection(CHAR_IMG_TAGS))
        assert eval (_test_winter_track("sound") is None)

    testcase unseen_delegate_creates_slot_and_reaches_chapter2_without_pads:
        assert eval (renpy.has_label("winter_interlude_start"))
        $ _test.winter_route_state = ("unseen", (), "", "neutral")
        run Start("test_winter_routing_driver") until screen "say" timeout 6.0
        assert eval (renpy.can_load("auto_ch-winter_interlude"))
        advance until screen "choice" timeout 4.0
        $ _test.choice_text = "交给奥尔德里克"
        pause until eval (len([f for f in renpy.display.focus.focus_list if f.x is not None and _test.choice_text.casefold() in f.widget._tts_all(True).casefold() and isinstance(getattr(f.widget, "action", None), renpy.ui.ChoiceReturn)]) == 1) timeout 4.0
        click "交给奥尔德里克"
        pause until eval ("chapter2_start" in _test.winter_labels) timeout 6.0
        assert eval (winter_interlude_status == "delegated")
        assert eval (not any(name in _test.winter_labels for name in ("_call_gov_merch2", "_call_gov_build2", "_call_gov_famine2")))
        assert eval (_test_winter_track("sound") is None)

    testcase active_choice_is_internal_only_and_cannot_flow_into_chapter2:
        assert eval (renpy.has_label("winter_interlude_start"))
        $ _test.winter_route_state = ("unseen", (), "", "neutral")
        run Start("test_winter_routing_driver") until screen "say" timeout 6.0
        advance until screen "choice" timeout 4.0
        $ _test.choice_text = "亲自主持"
        pause until eval (len([f for f in renpy.display.focus.focus_list if f.x is not None and _test.choice_text.casefold() in f.widget._tts_all(True).casefold() and isinstance(getattr(f.widget, "action", None), renpy.ui.ChoiceReturn)]) == 1) timeout 4.0
        click "亲自主持"
        pause until screen "say" timeout 4.0
        assert eval (winter_interlude_status == "active")
        advance until eval ("chapter2_start" in _test.winter_labels) timeout 6.0
        assert eval (winter_interlude_status == "delegated")
        assert eval (get_winter_context(outside=True).status == "delegated")
        assert eval (not any(name in _test.winter_labels for name in ("_call_gov_merch2", "_call_gov_build2", "_call_gov_famine2")))
        assert eval (_test_winter_track("sound") is None)

    testcase completed_and_delegated_reentries_reach_both_production_anchors_without_pads:
        parameter entry_state = ["completed", "delegated"]
        $ _test.winter_route_state = (("completed", ("market", "route"), "trade", "preserve") if entry_state == "completed" else ("delegated", (), "delegated", "neutral"))
        run Start("test_winter_routing_driver") until screen "chapter_title" timeout 6.0
        pause until eval (_chapter_card_clickable and renpy.get_screen("chapter_title") is not None) timeout 4.0
        keysym "K_RETURN"
        pause until screen "story_recap" timeout 4.0
        pause until eval (_recap_clickable and renpy.get_screen("story_recap") is not None) timeout 4.0
        keysym "K_RETURN"
        pause until eval (renpy.get_screen("rel_chapter_effect_summary") is not None or renpy.get_screen("cin_overlay") is not None) timeout 4.0
        if eval (renpy.get_screen("rel_chapter_effect_summary") is not None):
            click "继续"
        pause until screen "cin_overlay" timeout 24.0
        click "跳过"

        advance until screen "choice" timeout 30.0
        pause until eval (_test_winter_choice_ready("这是一个机会——让其他贵族认识新的艾登堡领主。")) timeout 4.0
        click "这是一个机会——让其他贵族认识新的艾登堡领主。"
        advance until screen "choice" timeout 30.0
        pause until eval (_test_winter_choice_ready("暂时收好，到了王都再调查。")) timeout 4.0
        click "暂时收好，到了王都再调查。"
        advance until screen "choice" timeout 30.0
        pause until eval (_test_winter_choice_ready("先不声张——在弄清楚之前，不能让任何人知道这枚徽章的存在。")) timeout 4.0
        click "先不声张——在弄清楚之前，不能让任何人知道这枚徽章的存在。"
        advance until screen "choice" timeout 30.0
        pause until eval (_test_winter_choice_ready("你已经赎够了罪，奥尔德里克。")) timeout 4.0
        click "你已经赎够了罪，奥尔德里克。"
        advance until screen "choice" timeout 30.0
        pause until eval (_test_winter_choice_ready("我收下。我会像你一样，守护应该守护的东西。")) timeout 4.0
        click "我收下。我会像你一样，守护应该守护的东西。"
        advance until screen "choice" timeout 30.0
        pause until eval (_test_winter_choice_ready("你做了正确的事，雷恩。")) timeout 4.0
        click "你做了正确的事，雷恩。"
        advance until screen "choice" timeout 30.0
        pause until eval (_test_winter_choice_ready("说实话——我也有很多疑惑")) timeout 4.0
        click "说实话——我也有很多疑惑"
        advance until eval ("ch2_after_legacy_governance" in _test.winter_labels) timeout 30.0
        assert eval (winter_interlude_status == entry_state)
        assert eval (_test.winter_labels.index("ch2_after_winter_interlude") < _test.winter_labels.index("ch2_after_legacy_governance"))
        assert eval (not any(name in _test.winter_labels for name in ("_call_gov_merch2", "_call_gov_build2", "_call_gov_famine2")))

    testcase blank_entry_runs_bootstrap_before_any_winter_write:
        assert eval (renpy.has_label("winter_interlude_start"))
        run Start("winter_interlude_start") until screen "difficulty_select" timeout 4.0
        assert eval ("_call_new_run_bootstrap_winter_interlude" in renpy.get_return_stack())
        assert eval (winter_interlude_status == "unseen")


testsuite test_winter_interlude_audio:
    before testcase:
        run MainMenu(confirm=False) until screen "main_menu" timeout 4.0
        $ _test_winter_begin_trace()

    after testcase:
        run MainMenu(confirm=False) until screen "main_menu" timeout 4.0
        $ _test_winter_end_trace()
        $ clear_weather()
        $ hide_all_chars()
        $ renpy.music.stop(channel="music")
        $ renpy.music.stop(channel="sound")

    testcase cleanup_true_stops_only_temporary_winter_music:
        assert eval (renpy.has_label("winter_interlude_cleanup"))
        $ _test.winter_cleanup_stop = True
        $ _test.winter_cleanup_track = "audio/music/winter_wind.ogg"
        run Start("test_winter_cleanup_driver") until screen "say" timeout 6.0
        assert eval (_test_winter_track("music") is None)
        assert eval (_test_winter_track("sound") is None)
        assert eval (get_weather() is None and renpy.get_screen("weather_snow") is None)
        assert eval (not set(renpy.get_showing_tags(layer="master")).intersection(CHAR_IMG_TAGS))

    testcase cleanup_false_preserves_legacy_music:
        assert eval (renpy.has_label("winter_interlude_cleanup"))
        $ _test.winter_cleanup_stop = False
        $ _test.winter_cleanup_track = "audio/music/castle_calm.ogg"
        run Start("test_winter_cleanup_driver") until screen "say" timeout 6.0
        assert eval (_test_winter_track("music").endswith("audio/music/castle_calm.ogg"))
        assert eval (_test_winter_track("sound") is None)
        assert eval (get_weather() is None and renpy.get_screen("weather_snow") is None)

    testcase cleanup_true_stops_the_existing_music_channel:
        assert eval (renpy.has_label("winter_interlude_cleanup"))
        $ _test.winter_cleanup_stop = True
        $ _test.winter_cleanup_track = "audio/music/castle_calm.ogg"
        run Start("test_winter_cleanup_driver") until screen "say" timeout 6.0
        assert eval (_test_winter_track("music") is None)
        assert eval (_test_winter_track("sound") is None)

    testcase chapter2_cinematic_returns_to_real_castle_calm_channel:
        run Start("test_winter_chapter2_audio_driver") until screen "chapter_title" timeout 4.0
        pause until eval (_chapter_card_clickable and renpy.get_screen("chapter_title") is not None) timeout 4.0
        keysym "K_RETURN"
        pause until screen "story_recap" timeout 4.0
        pause until eval (_recap_clickable and renpy.get_screen("story_recap") is not None) timeout 4.0
        keysym "K_RETURN"
        pause until eval (renpy.get_screen("rel_chapter_effect_summary") is not None or renpy.get_screen("cin_overlay") is not None) timeout 4.0
        if eval (renpy.get_screen("rel_chapter_effect_summary") is not None):
            click "继续"
        pause until screen "cin_overlay" timeout 24.0
        click "跳过"
        pause until eval (_test_winter_track("music") is not None and _test_winter_track("music").endswith("audio/music/castle_calm.ogg")) timeout 8.0
        assert eval ("chapter2_start" in _test.winter_labels)
        assert eval ("cinematic_chapter2" in _test.winter_labels)


testsuite test_winter_interlude_chapter_select:
    before testcase:
        run MainMenu(confirm=False) until screen "main_menu" timeout 4.0
        $ _test.winter_select_persistent_snapshot = {"chapters_completed": None if persistent.chapters_completed is None else set(persistent.chapters_completed), "privacy_agreed": persistent.privacy_agreed, "tutorial_seen": persistent.tutorial_seen, "ng_plus_unlocked": persistent.ng_plus_unlocked, "ng_plus_bonus_power": persistent.ng_plus_bonus_power, "ng_plus_bonus_wealth": persistent.ng_plus_bonus_wealth, "ng_plus_bonus_intrigue": persistent.ng_plus_bonus_intrigue, "difficulty": persistent.difficulty, "skip_autosave": persistent._skip_next_chapter_autosave}
        $ persistent.chapters_completed = {"chapter1"}
        $ persistent.privacy_agreed = True
        $ persistent.tutorial_seen = True
        $ persistent.ng_plus_unlocked = False
        $ persistent.ng_plus_bonus_power = 0
        $ persistent.ng_plus_bonus_wealth = 0
        $ persistent.ng_plus_bonus_intrigue = 0
        $ persistent.difficulty = "normal"
        $ persistent._skip_next_chapter_autosave = False
        $ renpy.unlink_save("auto_ch-winter_interlude")

    after testcase:
        run MainMenu(confirm=False) until screen "main_menu" timeout 4.0
        $ renpy.unlink_save("auto_ch-winter_interlude")
        $ persistent.chapters_completed = _test.winter_select_persistent_snapshot["chapters_completed"]
        $ persistent.privacy_agreed = _test.winter_select_persistent_snapshot["privacy_agreed"]
        $ persistent.tutorial_seen = _test.winter_select_persistent_snapshot["tutorial_seen"]
        $ persistent.ng_plus_unlocked = _test.winter_select_persistent_snapshot["ng_plus_unlocked"]
        $ persistent.ng_plus_bonus_power = _test.winter_select_persistent_snapshot["ng_plus_bonus_power"]
        $ persistent.ng_plus_bonus_wealth = _test.winter_select_persistent_snapshot["ng_plus_bonus_wealth"]
        $ persistent.ng_plus_bonus_intrigue = _test.winter_select_persistent_snapshot["ng_plus_bonus_intrigue"]
        $ persistent.difficulty = _test.winter_select_persistent_snapshot["difficulty"]
        $ persistent._skip_next_chapter_autosave = _test.winter_select_persistent_snapshot["skip_autosave"]
        $ renpy.save_persistent()

    testcase blank_action_preserves_sentinel_and_mainline_replaces_real_slot:
        run Start("test_winter_chapter_select_sentinel_driver") until screen "say" timeout 6.0
        assert eval (renpy.can_load("auto_ch-winter_interlude"))
        $ _test.winter_select_sentinel_json = dict(renpy.slot_json("auto_ch-winter_interlude"))
        assert eval (_test.winter_select_sentinel_json.get("_save_name") == "winter-select-sentinel")
        assert eval (_test.winter_select_sentinel_json.get("winter_select_marker") == "sentinel-v1")
        assert eval (renpy.list_saved_games(r"^auto_ch-winter_interlude$", fast=True) == ["auto_ch-winter_interlude"])

        run MainMenu(confirm=False) until screen "main_menu" timeout 4.0
        run ShowMenu("chapter_select") until screen "chapter_select" timeout 4.0
        pause until eval (_test_winter_action_ready("第一个冬天")) timeout 4.0
        click "第一个冬天"
        pause until screen "difficulty_select" timeout 4.0
        click "简单"
        click "确认"
        pause until screen "name_input_screen" timeout 4.0
        click "使用默认"
        pause until screen "say" timeout 6.0
        assert eval ((first_decree, southern_outcome, built_granary, gov_merchant_outcome, winter_interlude_status) == ("", "delegated", False, "", "unseen"))
        assert eval (persistent._skip_next_chapter_autosave is False)
        assert eval (dict(renpy.slot_json("auto_ch-winter_interlude")) == _test.winter_select_sentinel_json)

        run MainMenu(confirm=False) until screen "main_menu" timeout 4.0
        run FileLoad("auto_ch-winter_interlude", confirm=False, slot=True) until screen "say" timeout 6.0
        assert eval ((first_decree, southern_outcome, built_granary, gov_merchant_outcome, winter_interlude_status) == ("建设", "vassal", True, "", "unseen"))

        run MainMenu(confirm=False) until screen "main_menu" timeout 4.0
        run Start("test_winter_chapter_select_mainline_driver") until screen "say" timeout 6.0
        assert eval ((first_decree, southern_outcome, built_granary, gov_merchant_outcome, winter_interlude_status) == ("民生", "free", False, "", "unseen"))
        assert eval (renpy.slot_json("auto_ch-winter_interlude").get("winter_select_marker") is None)
        assert eval (dict(renpy.slot_json("auto_ch-winter_interlude")) != _test.winter_select_sentinel_json)

        run MainMenu(confirm=False) until screen "main_menu" timeout 4.0
        run FileLoad("auto_ch-winter_interlude", confirm=False, slot=True) until screen "say" timeout 6.0
        assert eval ((first_decree, southern_outcome, built_granary, gov_merchant_outcome, winter_interlude_status) == ("民生", "free", False, "", "unseen"))


label test_winter_active_save_driver:
    $ winter_interlude_status = "active"
    $ winter_investigations = ("market",)
    $ winter_policy = "trade"
    $ winter_seed_priority = "neutral"
    $ renpy.save("winter-active-mid-save")
    "Winter active save fixture."
    return


label test_winter_routing_driver:
    $ _new_run_bootstrap_done = True
    $ winter_interlude_status, winter_investigations, winter_policy, winter_seed_priority = _test.winter_route_state
    $ governance_events_seen[:] = []
    $ famine_prevented, gov_merchant_outcome = False, ""
    $ set_weather("snow")
    $ renpy.show("aldric_img")
    $ play_music("audio/music/winter_wind.ogg")
    $ renpy.music.play("audio/sfx/fire_crackle.ogg", channel="sound", loop=True)
    jump winter_interlude_start


label test_winter_cleanup_driver:
    $ _new_run_bootstrap_done = True
    $ set_weather("snow")
    $ renpy.show("aldric_img")
    $ play_music(_test.winter_cleanup_track)
    $ renpy.music.play("audio/sfx/fire_crackle.ogg", channel="sound", loop=True)
    call winter_interlude_cleanup(_test.winter_cleanup_stop) from _call_test_winter_cleanup_first
    call winter_interlude_cleanup(_test.winter_cleanup_stop) from _call_test_winter_cleanup_second
    "Winter cleanup runtime checkpoint."
    return


label test_winter_chapter2_audio_driver:
    $ _new_run_bootstrap_done = True
    $ apply_winter_delegation()
    jump chapter2_start


label test_winter_chapter_select_sentinel_driver:
    $ _new_run_bootstrap_done = True
    $ first_decree = "建设"
    $ southern_outcome = "vassal"
    $ built_granary = True
    $ famine_prevented = False
    $ gov_merchant_outcome = ""
    $ governance_events_seen[:] = []
    $ winter_interlude_status, winter_investigations, winter_policy, winter_seed_priority = "unseen", (), "", "neutral"
    $ renpy.save("auto_ch-winter_interlude", extra_info="winter-select-sentinel", extra_json={"winter_select_marker": "sentinel-v1"})
    "Winter chapter-select sentinel checkpoint."
    return


label test_winter_chapter_select_mainline_driver:
    $ _new_run_bootstrap_done = True
    $ first_decree = "民生"
    $ southern_outcome = "free"
    $ built_granary = False
    $ famine_prevented = False
    $ gov_merchant_outcome = ""
    $ governance_events_seen[:] = []
    $ winter_interlude_status, winter_investigations, winter_policy, winter_seed_priority = "unseen", (), "", "neutral"
    $ persistent._skip_next_chapter_autosave = False
    jump winter_interlude_start


## END TASK 3 WINTER STATE SUITES


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

label _test_lint_reachability_mobile_render:
    if True == True:
        return


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
    $ renpy.set_physical_size((config.screen_width, config.screen_height))
    pause 0.3
    assert eval (renpy.get_physical_size() == (config.screen_width, config.screen_height))
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


label test_resistance_battle_loss_fixture:
    $ persistent.difficulty = "hard"
    $ power = 0
    $ intrigue = 0
    $ faith = 0
    $ loyalty = 0
    $ wealth = 0
    $ rel_baron = 30
    $ rel_captain = 0
    $ alliance_baron = False
    $ prince_ally = False
    $ ch5_pay_advance_pension = False
    $ marriage_route = False
    $ iron_thorn_controlled = False
    $ baron_supply_intel = False
    $ resist_route = True
    $ iron_battle_outcome = "decisive"
    $ ending_type = ""
    jump ending_iron_lord


################################################################################
## 3.9.2 regression: accessibility controls must drive Ren'Py preferences.
################################################################################

## 3.9.2 release metadata: render the production About and privacy screens,
## exercise their real dismiss actions, and leave persistent consent unchanged.
label _test_lint_reachability_release_metadata:
    if True == True:
        return


testsuite test_release_metadata_render:
    setup:
        $ _test.timeout = 4.0
        $ _test.release_metadata_persistent_snapshot = {"privacy_agreed": persistent.privacy_agreed}
        $ _test.release_metadata_quick_menu_snapshot = quick_menu
        $ persistent.privacy_agreed = True

    teardown:
        $ persistent.privacy_agreed = _test.release_metadata_persistent_snapshot["privacy_agreed"]
        $ quick_menu = _test.release_metadata_quick_menu_snapshot
        $ renpy.save_persistent()
        assert eval (persistent.privacy_agreed == _test.release_metadata_persistent_snapshot["privacy_agreed"])
        assert eval (quick_menu == _test.release_metadata_quick_menu_snapshot)

    testcase production_about_renders_and_returns_to_main_menu:
        run ShowMenu("about") until screen "about" timeout 4.0
        pause 0.5
        screenshot "release_metadata_about"
        scroll amount 20 pos (0.7, 0.6)
        pause 0.5
        screenshot "release_metadata_about_license"
        click "« 返回"
        pause until screen "main_menu" timeout 4.0
        assert eval (renpy.get_screen("about") is None)

    testcase production_privacy_policy_renders_and_accept_returns_to_main_menu:
        $ quick_menu = False
        assert eval (not quick_menu)
        run Start("test_release_metadata_privacy_fixture") until screen "privacy_policy_screen" timeout 4.0
        pause 2.0
        screenshot "release_metadata_privacy"
        scroll amount 20 pos (0.6, 0.45)
        pause 0.5
        screenshot "release_metadata_privacy_version"
        $ persistent.privacy_agreed = False
        assert eval (not persistent.privacy_agreed)
        click "同意并继续"
        pause until screen "main_menu" timeout 4.0
        assert eval (persistent.privacy_agreed)
        assert eval (renpy.get_screen("privacy_policy_screen") is None)


label test_release_metadata_privacy_fixture:
    call screen privacy_policy_screen
    return

default _test_accessibility_original_font_size = 1.0
default _test_accessibility_original_high_contrast = False
default _test_accessibility_original_text_cps = 0
default _test_accessibility_seventh_selected = False

label _test_lint_reachability_accessibility:
    if True == True:
        return


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
            pause until screen "say" timeout 4.0
            run MainMenu(confirm=False) until screen "main_menu" timeout 4.0

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

label _test_lint_reachability_new_run:
    if True == True:
        return


testsuite test_new_run_bootstrap:
    before testcase:
        ## 全新 persistent 下 testcase hook 可能早于主菜单首次画面；无论当前
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
            ("winter_interlude_start", "_call_new_run_bootstrap_winter_interlude"),
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

## Winter governance state kernel and structural story-routing graph.

default winter_interlude_status = "unseen"
default winter_investigations = ()
default winter_policy = ""
default winter_seed_priority = "neutral"


init python:
    from collections import namedtuple

    WINTER_STATUSES = ("unseen", "active", "delegated", "completed", "legacy")
    WINTER_INVESTIGATION_ORDER = ("market", "village", "granary", "route")
    WINTER_POLICIES = ("trade", "ration", "requisition")
    WINTER_SEED_PRIORITIES = ("preserve", "feed_now")
    WINTER_LEGACY_EVENTS = ("famine_crisis", "merchant_negotiation")

    WINTER_OUTCOME_CONTRACTS = {
        ("trade", "preserve"): {
            "benefit": "trade_preserved_seed",
            "beneficiary": "farmers_and_trade_route",
            "burden": "trade_repayment_and_tight_rations",
            "bearer": "treasury_and_townspeople",
            "action": "audited_purchase_contracts",
            "followup": "trade_preserve_recovery",
        },
        ("trade", "feed_now"): {
            "benefit": "trade_immediate_relief",
            "beneficiary": "town_relief_recipients",
            "burden": "trade_seed_shortfall",
            "bearer": "treasury_and_farmers",
            "action": "market_grain_distribution",
            "followup": "trade_feed_recovery",
        },
        ("ration", "preserve"): {
            "benefit": "ration_preserved_seed",
            "beneficiary": "smallholders_and_farmers",
            "burden": "ration_hunger_and_reserve_pressure",
            "bearer": "garrison_and_townspeople",
            "action": "published_ration_ledgers",
            "followup": "ration_preserve_recovery",
        },
        ("ration", "feed_now"): {
            "benefit": "ration_broad_relief",
            "beneficiary": "town_relief_recipients",
            "burden": "ration_reserve_and_seed_loss",
            "bearer": "garrison_and_farmers",
            "action": "open_granary_distribution",
            "followup": "ration_feed_recovery",
        },
        ("requisition", "preserve"): {
            "benefit": "requisition_preserved_seed",
            "beneficiary": "smallholders_and_farmers",
            "burden": "requisition_compensation_debt",
            "bearer": "estates_and_lordship",
            "action": "sealed_compensation_vouchers",
            "followup": "requisition_preserve_recovery",
        },
        ("requisition", "feed_now"): {
            "benefit": "requisition_immediate_relief",
            "beneficiary": "broad_relief_recipients",
            "burden": "requisition_debt_and_seed_shortfall",
            "bearer": "estates_lordship_and_farmers",
            "action": "requisition_wagons_and_vouchers",
            "followup": "requisition_feed_recovery",
        },
    }

    WinterContext = namedtuple(
        "WinterContext",
        (
            "status",
            "investigations",
            "policy",
            "seed_priority",
            "famine_prevented",
            "merchant_outcome",
            "governance_events",
        ),
    )

    def normalize_winter_investigations(values):
        try:
            raw_values = tuple(values)
        except (TypeError, ValueError):
            return ()
        if len(raw_values) != 2:
            return ()
        if raw_values[0] == raw_values[1]:
            return ()
        if any(value not in WINTER_INVESTIGATION_ORDER for value in raw_values):
            return ()
        return tuple(
            value for value in WINTER_INVESTIGATION_ORDER if value in raw_values
        )

    def _winter_events_tuple(values):
        if not isinstance(values, (list, tuple, set, frozenset)):
            return ()
        return tuple(values)

    def _winter_raw_investigations(values):
        if isinstance(values, tuple):
            return values
        if isinstance(values, (list, set, frozenset)):
            return tuple(values)
        return ()

    def _make_winter_context(
            status, investigations, policy, seed_priority,
            famine_success, merchant_outcome, events):
        return WinterContext(
            status,
            investigations,
            policy,
            seed_priority,
            bool(famine_success),
            merchant_outcome,
            events,
        )

    def _winter_delegated_context(famine_success, merchant_outcome, events):
        return _make_winter_context(
            "delegated",
            (),
            "delegated",
            "neutral",
            famine_success,
            merchant_outcome,
            events,
        )

    def resolve_winter_interlude_context(raw_snapshot, projection):
        if projection not in ("internal", "outside"):
            raise ValueError("projection must be 'internal' or 'outside'")
        if not isinstance(raw_snapshot, tuple) or len(raw_snapshot) != 7:
            return _winter_delegated_context(False, "", ())

        (
            status,
            policy,
            seed_priority,
            raw_investigations,
            famine_success,
            merchant_outcome,
            raw_events,
        ) = raw_snapshot
        events = _winter_events_tuple(raw_events)
        investigations = _winter_raw_investigations(raw_investigations)

        if status == "legacy":
            return _make_winter_context(
                "legacy",
                investigations,
                policy,
                seed_priority,
                famine_success,
                merchant_outcome,
                events,
            )

        if status == "delegated":
            return _winter_delegated_context(
                famine_success, merchant_outcome, events
            )

        if status == "completed":
            canonical = normalize_winter_investigations(raw_investigations)
            if (
                    policy in WINTER_POLICIES
                    and seed_priority in WINTER_SEED_PRIORITIES
                    and canonical):
                return _make_winter_context(
                    "completed",
                    canonical,
                    policy,
                    seed_priority,
                    famine_success,
                    merchant_outcome,
                    events,
                )
            return _winter_delegated_context(
                famine_success, merchant_outcome, events
            )

        if status == "active":
            if projection == "outside":
                return _winter_delegated_context(
                    famine_success, merchant_outcome, events
                )
            return _make_winter_context(
                "active",
                investigations,
                policy,
                seed_priority,
                famine_success,
                merchant_outcome,
                events,
            )

        if status == "unseen":
            legacy_evidence = bool(
                famine_success
                or merchant_outcome
                or any(event in events for event in WINTER_LEGACY_EVENTS)
            )
            if legacy_evidence:
                return _make_winter_context(
                    "legacy",
                    investigations,
                    policy,
                    seed_priority,
                    famine_success,
                    merchant_outcome,
                    events,
                )
            if projection == "outside":
                return _winter_delegated_context(
                    famine_success, merchant_outcome, events
                )
            return _make_winter_context(
                "unseen",
                investigations,
                policy,
                seed_priority,
                famine_success,
                merchant_outcome,
                events,
            )

        return _winter_delegated_context(
            famine_success, merchant_outcome, events
        )

    def get_winter_context(outside=True):
        raw_snapshot = (
            winter_interlude_status,
            winter_policy,
            winter_seed_priority,
            winter_investigations,
            famine_prevented,
            gov_merchant_outcome,
            tuple(governance_events_seen),
        )
        projection = "outside" if outside else "internal"
        return resolve_winter_interlude_context(raw_snapshot, projection)

    def _append_winter_compatibility_markers():
        for event in ("winter_interlude", "famine_crisis"):
            if event not in governance_events_seen:
                governance_events_seen.append(event)

    def apply_winter_delegation():
        global winter_interlude_status
        global winter_investigations
        global winter_policy
        global winter_seed_priority
        winter_interlude_status = "delegated"
        winter_investigations = ()
        winter_policy = "delegated"
        winter_seed_priority = "neutral"
        _append_winter_compatibility_markers()

    def finalize_winter_interlude(policy, seed_priority, investigations):
        global winter_interlude_status
        global winter_investigations
        global winter_policy
        global winter_seed_priority
        canonical = normalize_winter_investigations(investigations)
        if (
                policy not in WINTER_POLICIES
                or seed_priority not in WINTER_SEED_PRIORITIES
                or not canonical):
            apply_winter_delegation()
            return False
        winter_interlude_status = "completed"
        winter_investigations = canonical
        winter_policy = policy
        winter_seed_priority = seed_priority
        _append_winter_compatibility_markers()
        return True

    def mark_winter_legacy():
        global winter_interlude_status
        winter_interlude_status = "legacy"

    def migrate_winter_interlude_state():
        global winter_interlude_status
        global winter_investigations
        global winter_policy
        global winter_seed_priority
        context = get_winter_context(outside=False)
        if context.status == "active" or context.status == "unseen":
            return
        if context.status == "legacy":
            winter_interlude_status = "legacy"
            return
        winter_interlude_status = context.status
        winter_investigations = context.investigations
        winter_policy = context.policy
        winter_seed_priority = context.seed_priority

    def winter_legacy_famine_success():
        context = get_winter_context(outside=True)
        return context.status == "legacy" and context.famine_prevented

    def select_winter_mitigation(policy, seed_priority, investigations, immediate_inputs):
        if type(immediate_inputs) is not tuple or len(immediate_inputs) != 7:
            return None
        canonical = normalize_winter_investigations(investigations)
        if not canonical:
            return None
        if "market" in canonical and policy == "trade":
            return "market_trade"
        if "granary" in canonical and policy == "ration":
            return "granary_ration"
        if "village" in canonical and seed_priority == "preserve":
            return "village_preserve"
        if "route" in canonical and seed_priority == "feed_now":
            return "route_feed_now"
        (
            merchant_outcome,
            southern_state,
            existing_granary,
            decree,
            soft_wealth,
            soft_loyalty,
            soft_power,
        ) = immediate_inputs
        if merchant_outcome == "regulated" and policy == "trade":
            return "merchant_regulated_trade"
        if southern_state in ("ruler", "fall") and policy == "trade":
            return "southern_trade_terms"
        if existing_granary and policy == "ration":
            return "existing_granary_ration"
        if decree == "治安" and policy == "trade":
            return "decree_security_trade"
        if decree in ("民生", "建设") and policy == "ration":
            return "decree_civic_ration"
        if decree == "军事" and policy == "requisition":
            return "decree_military_requisition"
        if soft_wealth >= 60 and policy == "trade":
            return "wealth_trade"
        if soft_loyalty >= 60 and policy == "ration":
            return "loyalty_ration"
        if soft_power >= 60 and policy == "requisition":
            return "power_requisition"
        return None


label winter_interlude_start:
    $ _winter_interlude_blank_entry = not _new_run_bootstrap_done
    call new_run_bootstrap from _call_new_run_bootstrap_winter_interlude

    if _winter_interlude_blank_entry:
        $ first_decree = ""
        $ southern_outcome = "delegated"
        $ built_granary = False
        $ famine_prevented = False
        $ gov_merchant_outcome = ""
        $ governance_events_seen[:] = [event for event in governance_events_seen if event not in WINTER_LEGACY_EVENTS]

    $ _winter_entry_context = get_winter_context(outside=False)
    if _winter_entry_context.status in ("completed", "legacy") or winter_interlude_status == "delegated":
        jump winter_interlude_exit
    if _winter_entry_context.status != "unseen":
        $ apply_winter_delegation()
        jump winter_interlude_exit

    $ auto_chapter_save("winter_interlude")
    call winter_interlude_brief from _call_winter_interlude_brief
    jump winter_interlude_exit


label winter_interlude_brief:
    scene bg study
    play music "audio/music/winter_wind.ogg" fadeout 1.0 fadein 1.0 if_changed
    "【结构占位·危机简报】粮价一周内翻倍；市场限售；账面库存与实际行情不符。"

    menu:
        "亲自主持":
            $ winter_interlude_status = "active"
            call winter_market_and_council from _call_winter_market_and_council

        "交给奥尔德里克":
            call winter_interlude_delegate from _call_winter_interlude_delegate

    return


label winter_interlude_delegate:
    $ apply_winter_delegation()
    "【结构占位·委托结果】neutral_delegate；不声明任何政策收益，也不替你作出政策决定。"
    return


label winter_market_and_council:
    $ set_weather("snow")
    scene bg market
    play music "audio/music/market_bustle.ogg" fadeout 1.0 fadein 1.0 if_changed
    "【结构占位·粮市】排队、争执、空粮袋；各方只掌握部分事实。"
    scene bg council_hall
    "【结构占位·紧急议事】商人、农户、守军与账房陈述各自处境。"
    call winter_investigation_menu from _call_winter_investigation_menu
    return


label winter_investigation_menu:
    "粮价：高｜库存：不足｜民情：不安"
    menu:
        "粮市账本":
            call winter_investigate_market("first") from _call_winter_first_market
            call winter_choose_second_investigation("market") from _call_winter_second_after_market

        "村庄种粮":
            call winter_investigate_village("first") from _call_winter_first_village
            call winter_choose_second_investigation("village") from _call_winter_second_after_village

        "城堡粮仓":
            call winter_investigate_granary("first") from _call_winter_first_granary
            call winter_choose_second_investigation("granary") from _call_winter_second_after_granary

        "北方商路":
            call winter_investigate_route("first") from _call_winter_first_route
            call winter_choose_second_investigation("route") from _call_winter_second_after_route

    return


label winter_choose_second_investigation(first):
    if first == "market":
        menu:
            "村庄种粮":
                call winter_investigate_village("second") from _call_winter_second_village_after_market
                call winter_omitted_reports(first, "village") from _call_winter_omitted_market_village

            "城堡粮仓":
                call winter_investigate_granary("second") from _call_winter_second_granary_after_market
                call winter_omitted_reports(first, "granary") from _call_winter_omitted_market_granary

            "北方商路":
                call winter_investigate_route("second") from _call_winter_second_route_after_market
                call winter_omitted_reports(first, "route") from _call_winter_omitted_market_route

    elif first == "village":
        menu:
            "粮市账本":
                call winter_investigate_market("second") from _call_winter_second_market_after_village
                call winter_omitted_reports(first, "market") from _call_winter_omitted_village_market

            "城堡粮仓":
                call winter_investigate_granary("second") from _call_winter_second_granary_after_village
                call winter_omitted_reports(first, "granary") from _call_winter_omitted_village_granary

            "北方商路":
                call winter_investigate_route("second") from _call_winter_second_route_after_village
                call winter_omitted_reports(first, "route") from _call_winter_omitted_village_route

    elif first == "granary":
        menu:
            "粮市账本":
                call winter_investigate_market("second") from _call_winter_second_market_after_granary
                call winter_omitted_reports(first, "market") from _call_winter_omitted_granary_market

            "村庄种粮":
                call winter_investigate_village("second") from _call_winter_second_village_after_granary
                call winter_omitted_reports(first, "village") from _call_winter_omitted_granary_village

            "北方商路":
                call winter_investigate_route("second") from _call_winter_second_route_after_granary
                call winter_omitted_reports(first, "route") from _call_winter_omitted_granary_route

    elif first == "route":
        menu:
            "粮市账本":
                call winter_investigate_market("second") from _call_winter_second_market_after_route
                call winter_omitted_reports(first, "market") from _call_winter_omitted_route_market

            "村庄种粮":
                call winter_investigate_village("second") from _call_winter_second_village_after_route
                call winter_omitted_reports(first, "village") from _call_winter_omitted_route_village

            "城堡粮仓":
                call winter_investigate_granary("second") from _call_winter_second_granary_after_route
                call winter_omitted_reports(first, "granary") from _call_winter_omitted_route_granary

    else:
        call winter_interlude_delegate from _call_winter_invalid_first_delegate

    return


label winter_investigate_market(visit_order):
    if visit_order == "omitted":
        "【结构占位·低可信报告·粮市账本】抬价与运输成本并存；信息未现场核实。{#winter_omitted_market}"
    else:
        scene bg market
        "【结构占位·已调查·粮市账本·[visit_order]】抬价、断路、护运和资金占用共同影响粮价。{#winter_selected_market}"
    return


label winter_investigate_village(visit_order):
    if visit_order == "omitted":
        "【结构占位·低可信报告·村庄种粮】藏粮可能用于春播；信息未现场核实。{#winter_omitted_village}"
    else:
        scene bg village
        "【结构占位·已调查·村庄种粮·[visit_order]】农户保粮主要为明年春播，并非单纯抗命。{#winter_selected_village}"
    return


label winter_investigate_granary(visit_order):
    # TEMPORARY ART MISMATCH: bg study stands in for Task 10 bg_winter_granary.
    if visit_order == "omitted":
        "【结构占位·低可信报告·城堡粮仓】受潮与旧账可能高估库存；信息未现场核实。{#winter_omitted_granary}"
    else:
        scene bg study
        "【结构占位·已调查·城堡粮仓·[visit_order]】受潮粮、旧账和层层报喜高估可用库存。{#winter_selected_granary}"
    return


label winter_investigate_route(visit_order):
    if visit_order == "omitted":
        "【结构占位·低可信报告·北方商路】冰雪与运输损耗可能拖慢到货；信息未现场核实。{#winter_omitted_route}"
    else:
        scene bg study
        "【结构占位·已调查·北方商路·[visit_order]】路线图与货单显示冰雪、损耗和周边采购共同造成到货不足。{#winter_selected_route}"
    return


label winter_omitted_reports(first, second):
    scene bg council_hall
    $ winter_investigations = normalize_winter_investigations((first, second))
    if not winter_investigations:
        call winter_interlude_delegate from _call_winter_invalid_pair_delegate
        return

    if "market" not in winter_investigations:
        call winter_investigate_market("omitted") from _call_winter_omitted_market
    if "village" not in winter_investigations:
        call winter_investigate_village("omitted") from _call_winter_omitted_village
    if "granary" not in winter_investigations:
        call winter_investigate_granary("omitted") from _call_winter_omitted_granary
    if "route" not in winter_investigations:
        call winter_investigate_route("omitted") from _call_winter_omitted_route

    call winter_crisis_escalates from _call_winter_crisis_escalates
    return


label winter_crisis_escalates:
    scene bg great_hall
    play music "audio/music/tension.ogg" fadeout 1.0 fadein 1.0 if_changed
    "【结构占位·共同原因】多项因素共同造成缺口；不存在单一责任方，也没有单一措施能够解决全部缺口。{#winter_shared_cause}"
    "【结构占位·危机升级】粮车未按时抵达；城内出现抢购。"
    call winter_choose_policy from _call_winter_choose_policy
    return


label winter_choose_policy:
    "粮价：高｜库存：不足｜民情：不安"
    menu:
        "高价购粮并担保商路":
            call winter_choose_seed_priority("trade") from _call_winter_seed_trade

        "开仓配给并公开账目":
            call winter_choose_seed_priority("ration") from _call_winter_seed_ration

        "征用大户余粮并开具补偿凭据":
            call winter_choose_seed_priority("requisition") from _call_winter_seed_requisition

    return


label winter_choose_seed_priority(policy):
    "粮价：高｜库存：不足｜民情：不安"
    menu:
        "保留春播种粮":
            call winter_resolve_outcome(policy, "preserve") from _call_winter_resolve_preserve

        "先让更多人熬过眼前的冬天":
            call winter_resolve_outcome(policy, "feed_now") from _call_winter_resolve_feed_now

    return


label winter_resolve_outcome(policy, seed_priority, immediate_inputs=None, mitigation=None):
    if not finalize_winter_interlude(policy, seed_priority, winter_investigations):
        call winter_interlude_delegate from _call_winter_invalid_result_delegate
        return

    $ immediate_inputs = (gov_merchant_outcome, southern_outcome, built_granary, first_decree, wealth, loyalty, power)
    $ mitigation = select_winter_mitigation(policy, seed_priority, winter_investigations, immediate_inputs)
    call winter_consequence(WINTER_OUTCOME_CONTRACTS[(policy, seed_priority)], mitigation, immediate_inputs) from _call_winter_consequence
    return


label winter_consequence(outcome, mitigation, immediate_inputs):
    scene bg great_hall
    play music "audio/music/castle_calm.ogg" fadeout 1.0 fadein 1.0 if_changed
    "【结构占位·收益】[outcome['benefit']]"
    "【结构占位·受益者】[outcome['beneficiary']]"
    "【结构占位·负担】[outcome['burden']]"
    "【结构占位·承担者】[outcome['bearer']]"
    "【结构占位·行动物件】[outcome['action']]"
    "【结构占位·后续回响】[outcome['followup']]"
    if winter_policy == "trade" and immediate_inputs[1] not in ("", "delegated"):
        "【结构占位·南境购粮条件】[immediate_inputs[1]]；只改变购买条件。"
    if mitigation is not None:
        "【结构占位·单项缓解】[mitigation]；不删除负担或承担者。"
    else:
        "【结构占位·单项缓解】none；保留完整负担与承担者。"
    return


label winter_interlude_exit:
    call winter_interlude_cleanup from _call_winter_cleanup_exit
    jump chapter2_start


label winter_interlude_cleanup(stop_temporary_music=True):
    $ clear_weather()
    $ renpy.music.stop(channel="sound", fadeout=0.0)
    $ hide_all_chars()
    if stop_temporary_music:
        $ stop_music(fadeout=0.0)
    return

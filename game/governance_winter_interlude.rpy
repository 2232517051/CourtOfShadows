## Winter governance state kernel. Story routing is implemented separately.

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
            "burden": "trade_repayment",
            "followup": "trade_preserve_recovery",
        },
        ("trade", "feed_now"): {
            "benefit": "trade_immediate_relief",
            "burden": "trade_seed_shortfall",
            "followup": "trade_feed_recovery",
        },
        ("ration", "preserve"): {
            "benefit": "ration_preserved_seed",
            "burden": "ration_hunger",
            "followup": "ration_preserve_recovery",
        },
        ("ration", "feed_now"): {
            "benefit": "ration_broad_relief",
            "burden": "ration_reserve_loss",
            "followup": "ration_feed_recovery",
        },
        ("requisition", "preserve"): {
            "benefit": "requisition_preserved_seed",
            "burden": "requisition_obligation",
            "followup": "requisition_preserve_recovery",
        },
        ("requisition", "feed_now"): {
            "benefit": "requisition_immediate_relief",
            "burden": "requisition_seed_shortfall",
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
        del immediate_inputs
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
    "结构占位：冬季治理幕间章"

    menu:
        "亲自主持":
            $ winter_interlude_status = "active"
            "结构占位：主动治理流程"
            jump winter_interlude_delegate

        "交给奥尔德里克":
            jump winter_interlude_delegate


label winter_interlude_delegate:
    $ apply_winter_delegation()
    jump winter_interlude_exit


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

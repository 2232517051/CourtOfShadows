## ============================================================
## 难度系统 & 好感度事件 & 彩蛋
## difficulty.rpy
## ============================================================

################################################################################
## 1. 难度模式系统
################################################################################

default persistent.difficulty = "normal"

init 1 python:
    ## 难度倍率: 影响 change_stat 和 change_rel 的正面/负面效果
    _difficulty_config = {
        "easy":   {"positive": 1.5, "negative": 0.5, "label": "简单", "desc": "属性增益+50%，减益-50%，适合体验剧情"},
        "normal": {"positive": 1.0, "negative": 1.0, "label": "普通", "desc": "标准难度，平衡的游戏体验"},
        "hard":   {"positive": 0.7, "negative": 1.5, "label": "困难", "desc": "属性增益-30%，减益+50%，每个选择都至关重要"},
    }

    ## 结局门槛配置（2026-05-17 反馈修复）
    ## TapTap 玩家反馈"困难模式故意作死也能拿主结局"。根因：原本只用 60/fallback 50
    ## 的属性门槛，且兜底总是 iron_lord。这里按难度区分主结局所需的属性高度和兜底逻辑。
    ## - primary_threshold: 进入主结局路线（铁腕/影/圣/民）的最低属性
    ## - fallback_threshold: 若没有任何属性达 primary，是否还有一条保底主线
    ##   设为 None 表示没有保底——直接进入 vassal/fall 新结局
    _ending_threshold_config = {
        "easy":   {"primary": 55, "fallback": 45},
        "normal": {"primary": 65, "fallback": 55},
        "hard":   {"primary": 72, "fallback": None},
    }

    def get_ending_threshold(kind="primary"):
        """读取当前难度对应的结局门槛。kind=primary|fallback"""
        diff = persistent.difficulty or "normal"
        cfg = _ending_threshold_config.get(diff, _ending_threshold_config["normal"])
        return cfg.get(kind)

    def get_finale_route_availability(
            power=0, intrigue=0, faith=0, loyalty=0,
            difficulty="normal", lily_full_member=False,
            rel_queen=0, rel_baron=0,
            father_poison_method_known=False,
            father_poison_executor_known=False,
            father_murder_mastermind_known=False,
            testament_original_obtained=False,
            deep_mother_herb="", poison_evidence=False,
            southern_outcome="none"):
        """纯函数：返回终章每条路线最终是否可见。"""
        cfg = _ending_threshold_config.get(difficulty or "normal", _ending_threshold_config["normal"])
        primary_threshold = cfg["primary"]
        fallback_threshold = cfg["fallback"]

        ranked = [
            (power, "iron_lord"),
            (intrigue, "shadow_king"),
            (faith, "holy_guardian"),
            (loyalty, "peoples_lord"),
        ]
        ranked.sort(key=lambda item: item[0], reverse=True)

        routes = {
            "iron_lord": False,
            "shadow_king": False,
            "holy_guardian": False,
            "peoples_lord": False,
            "truth": False,
            "borgia": False,
            "vassal": False,
            "resist": False,
            "sea": False,
            "fall": False,
        }

        for index, (value, route_id) in enumerate(ranked):
            if index < 2 and value >= primary_threshold:
                routes[route_id] = True

        if not any(routes[route_id] for _, route_id in ranked):
            if fallback_threshold is not None and ranked[0][0] >= fallback_threshold:
                routes[ranked[0][1]] = True

        ## 正式加入暗百合与教会调停身份冲突；必须在 fall 判定前抑制。
        if lily_full_member:
            routes["holy_guardian"] = False

        ## 方法与直接递毒者是证据链中间态，不能替代幕后主使确认。
        routes["truth"] = bool(father_murder_mastermind_known and testament_original_obtained)
        routes["borgia"] = bool(deep_mother_herb == "poison" and intrigue >= 70 and poison_evidence)
        hard_rel_threshold = 30 if primary_threshold >= 70 else 0
        routes["vassal"] = rel_queen >= hard_rel_threshold
        routes["resist"] = rel_baron >= hard_rel_threshold
        routes["sea"] = southern_outcome not in ("none", "delegated")

        non_sea_core = (
            "iron_lord", "shadow_king", "holy_guardian", "peoples_lord",
            "truth", "borgia", "vassal", "resist",
        )
        routes["fall"] = not any(routes[route_id] for route_id in non_sea_core)
        return routes

    def get_finale_ending_availability(routes, resistance_outcomes=None):
        """Map visible routes to persistent outcomes the player can actually reach."""
        resistance_outcomes = resistance_outcomes or {}
        battle_route_visible = bool(routes.get("iron_lord") or routes.get("resist"))
        return {
            "iron_lord": bool(routes.get("iron_lord") or (
                battle_route_visible and resistance_outcomes.get("iron_lord")
            )),
            "shadow_king": bool(routes.get("shadow_king")),
            "holy_guardian": bool(routes.get("holy_guardian")),
            "peoples_lord": bool(routes.get("peoples_lord")),
            "truth": bool(routes.get("truth")),
            "borgia": bool(routes.get("borgia")),
            "vassal": bool(routes.get("vassal")),
            "fall": bool(routes.get("fall") or (
                battle_route_visible and resistance_outcomes.get("fall")
            )),
            "sea": bool(routes.get("sea")),
        }

    def get_current_finale_route_availability():
        """用当前存档状态调用统一终章路线判定。"""
        return get_finale_route_availability(
            power=getattr(store, "power", 0),
            intrigue=getattr(store, "intrigue", 0),
            faith=getattr(store, "faith", 0),
            loyalty=getattr(store, "loyalty", 0),
            difficulty=persistent.difficulty or "normal",
            lily_full_member=getattr(store, "lily_full_member", False),
            rel_queen=getattr(store, "rel_queen", 0),
            rel_baron=getattr(store, "rel_baron", 0),
            father_poison_method_known=getattr(store, "father_poison_method_known", False),
            father_poison_executor_known=getattr(store, "father_poison_executor_known", False),
            father_murder_mastermind_known=getattr(store, "father_murder_mastermind_known", False),
            testament_original_obtained=getattr(store, "testament_original_obtained", False),
            deep_mother_herb=getattr(store, "deep_mother_herb", ""),
            poison_evidence=getattr(store, "poison_evidence", False),
            southern_outcome=getattr(store, "southern_outcome", "none"),
        )

    def get_current_resistance_battle_outcomes():
        """Evaluate resistance outcomes from the current save without mutating it."""
        return get_resistance_battle_outcomes(
            power=getattr(store, "power", 0),
            intrigue=getattr(store, "intrigue", 0),
            faith=getattr(store, "faith", 0),
            loyalty=getattr(store, "loyalty", 0),
            wealth=getattr(store, "wealth", 0),
            reputation=getattr(store, "reputation", 0),
            difficulty=persistent.difficulty or "normal",
            alliance_baron=getattr(store, "alliance_baron", False),
            rel_baron=getattr(store, "rel_baron", 0),
            prince_ally=getattr(store, "prince_ally", False),
            rel_captain=getattr(store, "rel_captain", 0),
            ch5_pay_advance_pension=getattr(store, "ch5_pay_advance_pension", False),
            marriage_route=getattr(store, "marriage_route", False),
            iron_thorn_controlled=getattr(store, "iron_thorn_controlled", False),
            baron_supply_intel=getattr(store, "baron_supply_intel", False),
        )

    ## 铁腕会战阈值难度修正 (批31收尾轮): 模拟显示最优策略下完胜率 ~95% (normal),
    ## hard +4 → 结盟玩家完胜~74% / 无盟友最优~38%完胜60%惨胜, 战败只惩罚无盟友乱打。
    ## easy -2 保体验档爽感。sim: Tools/sim_batch31_balance.py
    _war_threshold_mod = {"easy": -2, "normal": 0, "hard": 4}

    def get_war_threshold_mod():
        """铁腕会战 iron_war_score 判定阈值的难度修正"""
        diff = persistent.difficulty or "normal"
        return _war_threshold_mod.get(diff, 0)

    def get_difficulty_multiplier(delta):
        """根据难度调整属性变化量"""
        diff = persistent.difficulty or "normal"
        cfg = _difficulty_config.get(diff, _difficulty_config["normal"])
        if delta > 0:
            return int(delta * cfg["positive"])
        elif delta < 0:
            return int(delta * cfg["negative"])
        return 0

    def _diminishing_returns(current_val, raw_delta):
        """递减收益：属性越高，增益越少，防止一章就满的问题
        0-40: 100%增益 | 40-60: 70% | 60-80: 40% | 80+: 20%
        负面效果不受递减影响"""
        if raw_delta <= 0:
            return raw_delta
        if current_val >= 80:
            return max(1, int(raw_delta * 0.2))
        elif current_val >= 60:
            return max(1, int(raw_delta * 0.4))
        elif current_val >= 40:
            return max(1, int(raw_delta * 0.7))
        return raw_delta

    def _difficulty_adjusted_stat_value(current, delta, difficulty):
        """Pure equivalent of one change_stat call at a specified difficulty."""
        cfg = _difficulty_config.get(difficulty or "normal", _difficulty_config["normal"])
        if delta > 0:
            adjusted = int(delta * cfg["positive"])
        elif delta < 0:
            adjusted = int(delta * cfg["negative"])
        else:
            adjusted = 0

        if adjusted == 0 and delta != 0:
            adjusted = 1 if delta > 0 else -1
        adjusted = _diminishing_returns(current, adjusted)
        return max(0, min(100, current + adjusted))

    def get_resistance_battle_outcomes(
            power=0, intrigue=0, faith=0, loyalty=0, wealth=0, reputation=40,
            difficulty="normal", alliance_baron=False, rel_baron=0,
            prince_ally=False, rel_captain=0,
            ch5_pay_advance_pension=False, marriage_route=False,
            iron_thorn_controlled=False, baron_supply_intel=False):
        """Purely enumerate win/loss outcomes of the chapter-five resistance battle."""
        difficulty = difficulty or "normal"
        score = (
            max(0, power - 30) // 4
            + max(0, intrigue - 30) // 6
            + max(0, loyalty - 30) // 8
        )
        if wealth < 15:
            score -= 3
        else:
            score += max(0, wealth - 30) // 15
        if reputation < 20:
            score -= 2
        if alliance_baron:
            score += 10
        elif rel_baron > 0:
            score += 4
        if prince_ally:
            score += 5
        if rel_captain >= 60:
            score += 3
        if ch5_pay_advance_pension:
            score += 3
        if marriage_route:
            score += 5
        if iron_thorn_controlled:
            score += 3

        ## ending_iron_lord grants this before the plan menu, after base score.
        if power >= 70:
            power = _difficulty_adjusted_stat_value(power, 3, difficulty)

        plans = []
        if faith >= 60:
            plans.append((
                power,
                intrigue,
                _difficulty_adjusted_stat_value(faith, 5, difficulty),
                _difficulty_adjusted_stat_value(loyalty, 3, difficulty),
                wealth,
                score + 4,
            ))

        plans.append((
            power,
            _difficulty_adjusted_stat_value(intrigue, 5, difficulty),
            faith,
            _difficulty_adjusted_stat_value(loyalty, -4, difficulty),
            wealth,
            score + 6 + (3 if baron_supply_intel else 0),
        ))

        if wealth >= 40:
            plans.append((
                power,
                _difficulty_adjusted_stat_value(intrigue, 3, difficulty),
                faith,
                loyalty,
                _difficulty_adjusted_stat_value(wealth, -10, difficulty),
                score + 6,
            ))

        if power >= 55:
            plans.append((
                _difficulty_adjusted_stat_value(power, 3, difficulty),
                _difficulty_adjusted_stat_value(intrigue, 3, difficulty),
                faith,
                loyalty,
                wealth,
                score + 8,
            ))

        outcomes = {"iron_lord": False, "fall": False}
        prepared_floor = 12 + _war_threshold_mod.get(difficulty, 0)
        grind_threshold = 15 + _war_threshold_mod.get(difficulty, 0)

        for plan_power, plan_intrigue, plan_faith, plan_loyalty, plan_wealth, plan_score in plans:
            skirmishes = [
                (
                    _difficulty_adjusted_stat_value(plan_power, 5, difficulty),
                    plan_intrigue,
                    plan_loyalty,
                    plan_score,
                ),
                (
                    _difficulty_adjusted_stat_value(plan_power, 2, difficulty),
                    _difficulty_adjusted_stat_value(plan_intrigue, 3, difficulty),
                    plan_loyalty,
                    plan_score + 3,
                ),
            ]

            for skirmish_power, skirmish_intrigue, skirmish_loyalty, skirmish_score in skirmishes:
                villages = []
                if skirmish_loyalty >= 70:
                    villages.append((
                        _difficulty_adjusted_stat_value(skirmish_power, -6, difficulty),
                        skirmish_intrigue,
                        _difficulty_adjusted_stat_value(skirmish_loyalty, 5, difficulty),
                        skirmish_score,
                    ))
                villages.extend([
                    (
                        _difficulty_adjusted_stat_value(skirmish_power, -1, difficulty),
                        skirmish_intrigue,
                        _difficulty_adjusted_stat_value(skirmish_loyalty, 3, difficulty),
                        skirmish_score - 3,
                    ),
                    (
                        _difficulty_adjusted_stat_value(skirmish_power, 2, difficulty),
                        skirmish_intrigue,
                        _difficulty_adjusted_stat_value(skirmish_loyalty, -5, difficulty),
                        skirmish_score,
                    ),
                ])

                for final_power, final_intrigue, final_loyalty, final_score in villages:
                    prepared = (
                        final_power >= 60
                        or final_intrigue >= 55
                        or (final_intrigue >= 45 and final_loyalty >= 50)
                    )
                    required_score = prepared_floor if prepared else grind_threshold
                    if final_score >= required_score:
                        outcomes["iron_lord"] = True
                    else:
                        outcomes["fall"] = True

                    if outcomes["iron_lord"] and outcomes["fall"]:
                        return outcomes

        return outcomes

    ## 覆写 change_stat 和 change_rel，加入难度倍率
    _original_change_stat = change_stat
    _original_change_rel = change_rel

    def change_stat_with_difficulty(stat, delta):
        adjusted = get_difficulty_multiplier(delta)
        if adjusted == 0 and delta != 0:
            adjusted = 1 if delta > 0 else -1
        ## 递减收益：属性越高增益越少
        current = getattr(store, stat, 0)
        adjusted = _diminishing_returns(current, adjusted)
        _original_change_stat(stat, adjusted)

    def change_rel_with_difficulty(rel, delta):
        adjusted = get_difficulty_multiplier(delta)
        if adjusted == 0 and delta != 0:
            adjusted = 1 if delta > 0 else -1
        _original_change_rel(rel, adjusted)
        ## 检查好感度事件
        check_rel_events()

    ## 替换全局函数
    change_stat = change_stat_with_difficulty
    change_rel = change_rel_with_difficulty


## 难度选择界面（游戏开始前显示）
screen difficulty_select():
    zorder 300
    modal True

    add Solid("#0a0812ee")

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 40
        xminimum 550
        background Solid("#0f0d1af5")

        vbox:
            spacing 16
            xalign 0.5

            text "-- 选择难度 --" size 30 color "#d4a942" font "msyh.ttf" xalign 0.5 outlines [(2, "#000000cc", 0, 0)]

            add Solid("#d4a94230") xsize 400 ysize 1 xalign 0.5

            null height 8

            for diff_key in ["easy", "normal", "hard"]:
                $ _dc = _difficulty_config[diff_key]
                $ _selected = (persistent.difficulty == diff_key)
                $ _border_color = "#d4a942" if _selected else "#1a1528"

                button:
                    xfill True
                    xpadding 20
                    ypadding 14
                    background Solid("#1a152860" if _selected else "#1a152830")
                    hover_background Solid("#1a152880")
                    action SetField(persistent, "difficulty", diff_key)

                    hbox:
                        spacing 14
                        yalign 0.5

                        ## 资源体检: 单字→鎏金徽章; 图标统一方形画布, frame 内居中
                        $ _di = ui_icon(UI_DIFF_ICONS[diff_key], 76)
                        $ _dtxt = {"easy": "日", "normal": "剑", "hard": "难"}[diff_key]
                        frame:
                            xsize 80
                            ysize 80
                            background Solid(_border_color + "40")
                            if _di:
                                add _di xalign 0.5 yalign 0.5
                            else:
                                text _dtxt xalign 0.5 yalign 0.5 size 22

                        vbox:
                            spacing 2
                            text _dc["label"] size 20 color ("#d4a942" if _selected else "#e0d8c8") font "msyh.ttf" bold True
                            text _dc["desc"] size 12 color "#8a7e60"

                        if _selected:
                            ## 资源体检: 半角 > 换成播放箭头
                            $ _sel = ui_icon("ui_play", 18)
                            if _sel:
                                add Transform(_sel, matrixcolor=TintMatrix("#d4a942")) xalign 1.0 yalign 0.5
                            else:
                                text ">" xalign 1.0 yalign 0.5 size 20 color "#d4a942"

            null height 12
            add Solid("#d4a94220") xsize 400 ysize 1 xalign 0.5
            null height 6

            textbutton "确认":
                xalign 0.5
                text_size 22
                text_color "#d4a942"
                text_hover_color "#ffd866"
                text_font "msyh.ttf"
                action Return()


################################################################################
## 2. 好感度事件系统 (Relationship Events)
################################################################################

init python:
    ## 好感度事件: (角色关系变量, 触发阈值, 事件id, 是否已触发)
    ## 达到特定好感值时触发特殊对话
    _rel_events = {
        "aldric_trust":    ("rel_aldric", 70,  "奥尔德里克对你敞开了心扉"),
        "aldric_distrust": ("rel_aldric", -30, "奥尔德里克开始对你心存戒备"),
        "elena_close":     ("rel_elena",  50,  "艾琳娜向你展露了真实的一面"),
        "elena_romance":   ("rel_elena",  80,  "你与艾琳娜的关系变得特别"),
        "bishop_devout":   ("rel_bishop", 60,  "主教马修斯认为你是虔诚的信徒"),
        "baron_respect":   ("rel_baron",  40,  "冯·哈根男爵开始对你心存敬意"),
        "captain_loyal":   ("rel_captain",70,  "队长雷恩发誓效忠于你"),
        "queen_favor":     ("rel_queen",  60,  "王后对你另眼相看"),
    }

    ## 已触发的事件
    if not hasattr(persistent, 'rel_events_triggered'):
        persistent.rel_events_triggered = set()
    if persistent.rel_events_triggered is None:
        persistent.rel_events_triggered = set()

    def check_rel_events():
        """检查是否有新的好感度事件需要触发"""
        for event_id, (rel_var, threshold, desc) in _rel_events.items():
            if event_id in persistent.rel_events_triggered:
                continue
            val = getattr(store, rel_var, 0)
            if (threshold >= 0 and val >= threshold) or (threshold < 0 and val <= threshold):
                persistent.rel_events_triggered.add(event_id)
                renpy.show_screen("rel_event_toast", event_desc=desc, is_positive=(threshold >= 0))

screen rel_event_toast(event_desc="", is_positive=True):
    zorder 255
    $ _re_color = "#d4a942" if is_positive else "#e67e22"
    $ _re_icon = "心" if is_positive else "!"

    frame at stat_toast_anim:
        xalign 0.5
        ypos 140
        background Solid("#1a1020ee")
        xpadding 24
        ypadding 10

        hbox:
            spacing 10
            text _re_icon size 18 color _re_color yalign 0.5
            text "关系变化：" size 14 color "#8a7e60" font "msyh.ttf" yalign 0.5
            text event_desc size 16 color _re_color font "msyh.ttf" yalign 0.5

    timer 4.0 action Hide("rel_event_toast")


################################################################################
## 3. 彩蛋系统 (Easter Eggs)
################################################################################

init python:
    ## 特殊名字触发
    _easter_egg_names = {
        "阿瑟":    "传说中的亚瑟王？看来你的命运注定不凡。",
        "亚瑟王":  "持剑者，石中剑为你而鸣！",
        "刺客":    "什么？刺客？！侍卫们，给我抓住他——啊，原来是新领主...",
        "小燚":    "造物主降临了！这个世界因你而存在。",
        "Claude":  "AI觉醒了？不，这只是一个巧合...大概。",
        "龙":      "远古的血脉在你的体内流淌。小心，别点燃城堡。",
        "死亡":    "...你确定要用这个名字？好吧，以死亡之名，我宣布你为领主。",
        "上帝":    "谦虚一点。在这个世界里，你只是一个领主——暂时。",
        "没有名字": "好吧，那就叫你「无名领主」吧。听起来还挺酷的。",
    }

    def check_name_easter_egg(name):
        """检查名字是否触发彩蛋，返回彩蛋文本或None"""
        for key, msg in _easter_egg_names.items():
            if key in name:
                return msg
        return None

    ## 隐藏互动计数器
    _secret_click_count = 0

    def add_secret_click():
        global _secret_click_count
        _secret_click_count += 1
        if _secret_click_count >= 10:
            _secret_click_count = 0
            unlock_achievement("completionist")  ## 偷偷给个成就
            return True
        return False


## 名字彩蛋弹窗
screen name_easter_egg(egg_text=""):
    zorder 270

    frame at stat_toast_anim:
        xalign 0.5
        ypos 80
        background Solid("#1a1020ee")
        xpadding 28
        ypadding 12

        hbox:
            spacing 10
            $ _egg_ico = ui_icon("ico_diamond", 20)
            if _egg_ico:
                add _egg_ico yalign 0.5
            else:
                text "【蛋】" size 18 yalign 0.5
            text egg_text size 16 color "#ffd700" font "msyh.ttf" yalign 0.5

    timer 4.0 action Hide("name_easter_egg")

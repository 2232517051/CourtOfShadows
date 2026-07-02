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

                        frame:
                            xsize 44
                            ysize 44
                            background Solid(_border_color + "40")
                            if diff_key == "easy":
                                text "日" xalign 0.5 yalign 0.5 size 22
                            elif diff_key == "normal":
                                text "剑" xalign 0.5 yalign 0.5 size 22
                            else:
                                text "难" xalign 0.5 yalign 0.5 size 22

                        vbox:
                            spacing 2
                            text _dc["label"] size 20 color ("#d4a942" if _selected else "#e0d8c8") font "msyh.ttf" bold True
                            text _dc["desc"] size 12 color "#8a7e60"

                        if _selected:
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
            text "【蛋】" size 18 yalign 0.5
            text egg_text size 16 color "#ffd700" font "msyh.ttf" yalign 0.5

    timer 4.0 action Hide("name_easter_egg")

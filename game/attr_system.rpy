## ============================================================
## attr_system.rpy — 属性进阶系统（布兰特设计哲学）
## 包含：阶位系统、骰子判定、统一修改函数、路线印记、
##       高属性代价、关系状态、三个UI Screen
## ============================================================

################################################################################
## init python 块 — 所有函数定义
################################################################################

init python:
    import random as _attr_random

    ## ──────────────────────────────────────────────
    ## A. 属性阶位系统 (Tier System)
    ## ──────────────────────────────────────────────

    ## 每属性5阶 (0-19 / 20-39 / 40-59 / 60-79 / 80-100)
    TIER_DATA = {
        "power": {
            "labels": ["手无缚鸡", "初显锋芒", "铁腕领主", "威震一方", "无人能敌"],
            "colors": ["#8a7e60",  "#c8a850",  "#d4a942",  "#e8c060",  "#ffd700"],
        },
        "intrigue": {
            "labels": ["人情世故", "精于算计", "运筹帷幄", "深不可测", "腹黑帝王"],
            "colors": ["#8a7e60",  "#9370db",  "#7b2d8b",  "#5b0ea6",  "#3d0066"],
        },
        "faith": {
            "labels": ["心存疑虑", "虔诚信徒", "主教之友", "布道者",   "圣光使者"],
            "colors": ["#8a7e60",  "#c8b890",  "#d4a942",  "#f0d060",  "#fffacd"],
        },
        "wealth": {
            "labels": ["入不敷出", "勉强维持", "殷实之家", "家财万贯", "富可敌国"],
            "colors": ["#8a7e60",  "#a08040",  "#c8a850",  "#d4a942",  "#ffd700"],
        },
        "reputation": {
            "labels": ["臭名昭著", "默默无闻", "小有名气", "声名远扬", "名垂千古"],
            "colors": ["#8b0000",  "#8a7e60",  "#c8b890",  "#d4a942",  "#ffd700"],
        },
        "loyalty": {
            "labels": ["人心离散", "暗流涌动", "民心稳固", "赤胆忠心", "誓死效忠"],
            "colors": ["#8b0000",  "#c0392b",  "#c8b890",  "#27ae60",  "#1abc9c"],
        },
    }

    ## 阶位突破叙事文字 (升到该阈值 / 降过该阈值)
    TIER_CROSS_NARRATIVE = {
        "power": {
            20: ("初显锋芒", "#c8a850",
                 "你初次展现了作为领主的力量，随从们开始对你刮目相看。",
                 "曾经的威势已消退，你的权威受到了质疑。"),
            40: ("铁腕领主", "#d4a942",
                 "铁腕领主的威名已在北境传开。",
                 "昔日的威慑已成往事。"),
            60: ("威震一方", "#e8c060",
                 "你的名字令周边领主噤若寒蝉，无人敢轻易挑衅。",
                 "曾令人闻风丧胆的威名，如今已日渐黯淡。"),
            80: ("无人能敌", "#ffd700",
                 "北境之内，无人敢于正面撼动你的权力。你已成为这片土地的真正主宰。",
                 "权柄动摇，曾经无人能敌的你开始面临四面楚歌。"),
        },
        "intrigue": {
            20: ("精于算计", "#9370db",
                 "你开始学会在权谋的游戏中步步为营。",
                 "曾经的精明已被磨平，你变得不再敏锐。"),
            40: ("运筹帷幄", "#7b2d8b",
                 "棋局已在你的掌握之中，对手的算计皆在你的预料之内。",
                 "你的谋略开始失去光彩，对手渐渐摸清了你的路数。"),
            60: ("深不可测", "#5b0ea6",
                 "没有人能看穿你的真实意图，你的笑容背后藏着无数条退路。",
                 "昔日深不可测的面纱已被揭开一角。"),
            80: ("腹黑帝王", "#3d0066",
                 "整个朝堂都成了你的棋盘，每一步都在你的算计之中。盟友们开始感到不安。",
                 "你深不可测的谋略开始让连盟友也疑惧，局势渐渐失控。"),
        },
        "faith": {
            20: ("虔诚信徒", "#c8b890",
                 "你开始认真地践行信仰，教会的人注意到了你的诚意。",
                 "你的信仰开始动摇，教会的人感受到了疏离。"),
            40: ("主教之友", "#d4a942",
                 "主教将你视为可信赖的友人，教会的大门为你敞开。",
                 "你与教会的关系出现了裂痕，昔日的信任已不复从前。"),
            60: ("布道者", "#f0d060",
                 "你的虔诚感染了周围的人，领民们开始以你为信仰的榜样。",
                 "布道者的光环逐渐褪去，你的信仰显得不再那么坚定。"),
            80: ("圣光使者", "#fffacd",
                 "教会将你奉为圣光在人间的使者，信徒们对你顶礼膜拜。这份荣耀沉重而危险。",
                 "圣光使者的称号已成过去，你与教会过于亲密引发的争议令你难以脱身。"),
        },
        "wealth": {
            20: ("勉强维持", "#a08040",
                 "领地财政终于有所好转，你不再为日常开销而忧虑。",
                 "财务状况再度告急，入不敷出的日子又回来了。"),
            40: ("殷实之家", "#c8a850",
                 "库房渐丰，你可以开始考虑更长远的投资与布局。",
                 "财富缩水，殷实之家的底气大不如前。"),
            60: ("家财万贯", "#d4a942",
                 "你的财富引来了各方的注意，商人们争相与你合作。",
                 "财富流失，家财万贯的名声开始动摇。"),
            80: ("富可敌国", "#ffd700",
                 "富可敌国的你成了各路人马觊觎的目标，财富既是庇护，也是枷锁。",
                 "富可敌国的财富已大幅缩水，觊觎者暂时收起了贪婪的目光。"),
        },
        "reputation": {
            20: ("默默无闻", "#8a7e60",
                 "你开始在人们的记忆中留下印记，虽不显赫，却也有迹可循。",
                 "你的名声再度沉入了默默无闻的深渊。"),
            40: ("小有名气", "#c8b890",
                 "你的名字开始在周边领地流传，人们提起你时带着几分好奇。",
                 "曾经积累的名声悄然流逝，你变得不再引人注目。"),
            60: ("声名远扬", "#d4a942",
                 "你的事迹已传至远方，无论走到哪里，人们都知道你的名字。",
                 "声名远扬的风光已成过去，你的名字不再令人振奋。"),
            80: ("名垂千古", "#ffd700",
                 "史书之中将会留有你的名字，后世提起这个时代，都会提起你。",
                 "名垂千古的机遇悄然溜走，历史可能不会如你所愿地铭记你。"),
        },
        "loyalty": {
            20: ("暗流涌动", "#c0392b",
                 "民间的不满开始聚集，领地内暗流涌动，你需要警惕。",
                 "局势进一步恶化，人心离散已成定局。"),
            40: ("民心稳固", "#c8b890",
                 "你的治理赢得了大多数领民的认可，领地趋于安定。",
                 "曾经稳固的民心出现了动摇，不满情绪再度蔓延。"),
            60: ("赤胆忠心", "#27ae60",
                 "你的领民愿意为你赴汤蹈火，这份信任是你最坚实的后盾。",
                 "赤胆忠心的追随者开始产生疑虑，你需要重新赢得他们的心。"),
            80: ("誓死效忠", "#1abc9c",
                 "领民们视你为家人与守护者，愿以性命相托。这是一份沉甸甸的承诺。",
                 "誓死效忠的信念开始动摇，你必须做些什么来挽回这份失去的信任。"),
        },
    }

    def get_tier(stat_name):
        """返回阶位索引 0-4"""
        val = getattr(store, stat_name, 0)
        if val >= 80:
            return 4
        elif val >= 60:
            return 3
        elif val >= 40:
            return 2
        elif val >= 20:
            return 1
        else:
            return 0

    def get_tier_label(stat_name):
        """返回当前阶位中文名"""
        data = TIER_DATA.get(stat_name)
        if not data:
            return ""
        return data["labels"][get_tier(stat_name)]

    def get_tier_color(stat_name):
        """返回当前阶位颜色hex"""
        data = TIER_DATA.get(stat_name)
        if not data:
            return "#c8b890"
        return data["colors"][get_tier(stat_name)]

    ## ──────────────────────────────────────────────
    ## B. 布兰特式骰子判定
    ## ──────────────────────────────────────────────

    def dice_check(stat_name, difficulty):
        """
        1d10 + stat_bonus vs difficulty
        stat_bonus = (stat_val - 30) // 10，范围 -3 到 +7
        difficulty: 2-10，成功需要 roll + bonus >= difficulty
        返回: (bool成功, int骰子值1-10, int加成, int总计, str描述)
        """
        stat_val = getattr(store, stat_name, 30)
        bonus = max(-3, min(7, (stat_val - 30) // 10))
        roll = _attr_random.randint(1, 10)
        total = roll + bonus
        success = total >= difficulty

        if success:
            if total >= difficulty + 4:
                desc = "大成功"
            else:
                desc = "成功"
        else:
            if total <= difficulty - 4:
                desc = "大失败"
            else:
                desc = "失败"

        return (success, roll, bonus, total, desc)

    ## ──────────────────────────────────────────────
    ## C. 统一属性修改函数（带叙事通知）
    ## ──────────────────────────────────────────────

    STAT_LABELS_CN = {
        "power":      "权力",
        "intrigue":   "谋略",
        "faith":      "信仰",
        "wealth":     "财富",
        "reputation": "声望",
        "loyalty":    "忠诚",
    }

    ## 【墓碑】本文件原有的 change_stat(含 STAT_CHANGE_SCALE=0.4 / STAT_COST_SCALE=0.6
    ## 与高位衰减公式)已于 2026-07-28 删除 —— 它自 effects.rpy 出现起就是死代码, 从未生效
    ## (2026-07-15 真机实测确认)。
    ##
    ## 全项目 change_stat 的真实链条(唯一权威):
    ##   difficulty.rpy:94  change_stat = change_stat_with_difficulty
    ##     → 难度倍率 (正: easy ×1.5 / normal ×1.0 / hard ×0.7; 负: easy ×0.5 / hard ×1.5; int 截断, 归零取±1)
    ##     → _diminishing_returns 递减收益 (0-40:100% | 40-60:70% | 60-80:40% | 80+:20%)
    ##     → effects.rpy change_stat (原值直加 + clamp 0..100 + record_stat + toast
    ##       + 预警 + 成就)
    ## 实测(easy): intrigue 20 +10 → 35; intrigue 80 +10 → 83。
    ##
    ## Tools/sim_batch31_balance.py 已同步改为模拟上述真实链条(同一提交)。
    ## 本文件保留的 get_tier / TIER_CROSS_NARRATIVE / 路线印记等均为存活代码, 别顺手删。

    ## ──────────────────────────────────────────────
    ## D. 路线印记系统 (Identity Path)
    ## ──────────────────────────────────────────────

    PATH_NAMES_CN = {
        "martial":   ("铁血路线", "武力与威慑", "#e74c3c"),
        "scheme":    ("谋士路线", "算计与暗影", "#9b59b6"),
        "faith":     ("圣光路线", "信仰与救赎", "#f1c40f"),
        "diplomacy": ("外交路线", "口才与联盟", "#2ecc71"),
    }

    ## 激活所需印记数
    PATH_ACTIVATION_THRESHOLD = 3

    def add_path_mark(path_name):
        """增加一枚路线印记，满3枚自动激活"""
        mark_var = "path_marks_" + path_name
        active_var = "path_active_" + path_name

        if not hasattr(store, mark_var):
            return

        current = getattr(store, mark_var, 0)
        if current >= PATH_ACTIVATION_THRESHOLD:
            ## 已激活，无需再增
            return

        setattr(store, mark_var, current + 1)
        new_count = current + 1

        if new_count >= PATH_ACTIVATION_THRESHOLD and not getattr(store, active_var, False):
            setattr(store, active_var, True)
            path_info = PATH_NAMES_CN.get(path_name, (path_name, "", "#d4a942"))
            renpy.show_screen(
                "path_activated_popup",
                path_name=path_info[0],
                path_desc=path_info[1],
                path_color=path_info[2],
            )

    def has_path(path_name):
        """检查路线是否已激活"""
        return getattr(store, "path_active_" + path_name, False)

    def get_dominant_path():
        """返回当前印记最多的路线名（未激活也算），平局返回 None"""
        paths = ["martial", "scheme", "faith", "diplomacy"]
        counts = {p: getattr(store, "path_marks_" + p, 0) for p in paths}
        max_count = max(counts.values())
        if max_count == 0:
            return None
        leaders = [p for p, c in counts.items() if c == max_count]
        if len(leaders) == 1:
            return leaders[0]
        return None

    ## ──────────────────────────────────────────────
    ## E. 高属性双面代价检查
    ## ──────────────────────────────────────────────

    HIGH_STAT_CONSEQUENCES = {
        "power":    (80, "power_too_high",    "权力过盛引发了王后的警惕..."),
        "intrigue": (80, "intrigue_too_high", "你深不可测的谋略让连盟友也开始疑惧..."),
        "wealth":   (80, "wealth_too_high",   "富可敌国的你成了各路人马的目标..."),
        "faith":    (80, "faith_too_high",    "你与教会过于亲密，引起了部分领民的反感..."),
    }

    def check_high_stat_warnings():
        """检查高属性代价，每个只触发一次（用flag防重复）"""
        warnings = []
        for stat_name, (threshold, flag_var, warn_text) in HIGH_STAT_CONSEQUENCES.items():
            val = getattr(store, stat_name, 0)
            already = getattr(store, flag_var, False)
            if val >= threshold and not already:
                setattr(store, flag_var, True)
                warnings.append(warn_text)
        return warnings

    ## ──────────────────────────────────────────────
    ## F. 关系状态函数
    ## ──────────────────────────────────────────────

    REL_STATES = [
        (-100, -60,  "死敌",   "#8b0000", "✕"),
        (-60,  -30,  "敌视",   "#c0392b", "↓↓"),
        (-30,   0,   "警惕",   "#e67e22", "↓"),
        (  0,   30,  "中立",   "#8a7e60", "—"),
        ( 30,   60,  "友善",   "#27ae60", "↑"),
        ( 60,   80,  "信任",   "#2ecc71", "↑↑"),
        ( 80,  101,  "誓盟",   "#1abc9c", "★"),
    ]

    def get_rel_state(rel_val):
        """返回 (状态名, 颜色, 图标)"""
        for lo, hi, name, color, icon in REL_STATES:
            if lo <= rel_val < hi:
                return (name, color, icon)
        ## 边界保护
        if rel_val >= 80:
            return ("誓盟", "#1abc9c", "★")
        return ("死敌", "#8b0000", "✕")

    ## ──────────────────────────────────────────────
    ## 兼容旧代码：clamp_stats（新版，使用 setattr）
    ## ──────────────────────────────────────────────

    def clamp_stats():
        for s in ["power", "wealth", "faith", "loyalty", "reputation", "intrigue"]:
            setattr(store, s, max(0, min(100, getattr(store, s, 0))))

    ## ──────────────────────────────────────────────
    ## 兼容旧代码：change_will / change_courage
    ## ──────────────────────────────────────────────

    def change_will(delta):
        """修改勇气值（通用名称）"""
        store.courage = max(0, min(store.max_courage, store.courage + delta))

    def has_courage(amount):
        """检查勇气是否充足"""
        return store.courage >= amount

    def change_courage(delta):
        """兼容旧代码，内部调用 change_will"""
        change_will(delta)


################################################################################
## G. 三个新 Screen
################################################################################

## ── G1. stat_change_popup ──────────────────────────────────────────────────
## 右下角浮现："+5 权力 · 铁腕领主"
## 参数：stat_label(str), delta(int), new_val(int), tier_label(str), tier_color(str)

transform stat_popup_show:
    on show:
        alpha 0.0 xoffset 60
        ease 0.3 alpha 1.0 xoffset 0
    on hide:
        ease 0.4 alpha 0.0 xoffset 40

screen stat_change_popup(stat_label, delta, new_val, tier_label, tier_color):
    zorder 180
    modal False

    ## 右下角
    frame at stat_popup_show:
        xalign 0.98
        yalign 0.92
        background Solid("#0f0d1ae8")
        xpadding 16
        ypadding 10

        vbox:
            spacing 4
            xalign 1.0

            hbox:
                spacing 6
                xalign 1.0

                ## 增减符号与数值 — delta 是 clamp 后的 actual_delta, 触顶时为 0
                if delta > 0:
                    text "+[delta]" size 20 color "#2ecc71" bold True font "msyh.ttf"
                elif delta < 0:
                    text "[delta]" size 20 color "#e74c3c" bold True font "msyh.ttf"
                else:
                    ## 触顶/软顶/触底/无变化 — 不再假飘 "+0", 给明确语义
                    if new_val >= 100:
                        text "已至顶峰" size 16 color "#f0c050" bold True font "msyh.ttf"
                    elif new_val >= 80:
                        ## 选择深度 pass: 80+ 软顶, 加点几近无效 → 提示玩家分散投资
                        text "已臻巅峰" size 16 color "#f0c050" bold True font "msyh.ttf"
                    elif new_val <= 0:
                        text "已至谷底" size 16 color "#7d6a8f" bold True font "msyh.ttf"
                    else:
                        text "无变化" size 16 color "#888888" font "msyh.ttf"

                text "[stat_label]" size 20 color "#c8b890" font "msyh.ttf"

            ## 阶位标签
            if tier_label:
                text "· [tier_label]" size 13 color tier_color font "msyh.ttf" xalign 1.0

    timer 2.0 action Hide("stat_change_popup")


## ── G2. tier_cross_popup ───────────────────────────────────────────────────
## 画面中央：阶位突破叙事文字
## 参数：text(str), tier_label(str), tier_color(str)

transform tier_cross_show:
    on show:
        alpha 0.0 zoom 0.92
        ease 0.5 alpha 1.0 zoom 1.0
    on hide:
        ease 0.5 alpha 0.0 zoom 1.04

screen tier_cross_popup(text, tier_label, tier_color):
    zorder 190
    modal False

    add Solid("#000000a0") at tier_cross_show

    frame at tier_cross_show:
        xalign 0.5
        yalign 0.42
        xsize 480
        background Solid("#0f0d1af2")
        xpadding 36
        ypadding 28

        vbox:
            spacing 14
            xalign 0.5

            ## 装饰线
            add Solid(tier_color) xsize 200 ysize 1 xalign 0.5

            ## 阶位名称
            text "[tier_label]" size 24 color tier_color font "msyh.ttf" bold True xalign 0.5

            ## 叙事文字
            text text size 16 color "#c8b890" font "msyh.ttf" text_align 0.5 xalign 0.5

            ## 装饰线
            add Solid(tier_color) xsize 200 ysize 1 xalign 0.5

    timer 3.0 action Hide("tier_cross_popup")


## ── G3. path_activated_popup ───────────────────────────────────────────────
## 画面中央全屏暗色：路线激活
## 参数：path_name(str), path_desc(str), path_color(str)

transform path_popup_show:
    on show:
        alpha 0.0
        ease 0.6 alpha 1.0
    on hide:
        ease 0.5 alpha 0.0

screen path_activated_popup(path_name, path_desc, path_color):
    zorder 195
    modal False

    ## 全屏暗色覆盖
    add Solid("#00000099") at path_popup_show

    frame at path_popup_show:
        xalign 0.5
        yalign 0.45
        xsize 520
        background Solid("#0f0d1af8")
        xpadding 44
        ypadding 36

        vbox:
            spacing 16
            xalign 0.5

            ## 顶部装饰双线
            vbox:
                spacing 4
                xalign 0.5
                add Solid(path_color) xsize 280 ysize 2 xalign 0.5
                add Solid(path_color) xsize 200 ysize 1 xalign 0.5

            ## 标题
            text "路线已激活" size 14 color "#8a7e60" font "msyh.ttf" xalign 0.5

            ## 路线名称
            text "[path_name]" size 30 color path_color font "msyh.ttf" bold True xalign 0.5

            ## 描述
            text "[path_desc]" size 18 color "#c8b890" font "msyh.ttf" xalign 0.5

            ## 底部装饰双线
            vbox:
                spacing 4
                xalign 0.5
                add Solid(path_color) xsize 200 ysize 1 xalign 0.5
                add Solid(path_color) xsize 280 ysize 2 xalign 0.5

    timer 2.5 action Hide("path_activated_popup")

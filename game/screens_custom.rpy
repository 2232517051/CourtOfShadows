## ============================================================
## 领主状态面板 — 大厂级设计 (按 S 键打开)
## ============================================================

init python:
    ## 属性图标映射
    stat_icons = {
        "power": ("剑", "权力", "#e74c3c"),
        "wealth": ("金", "财富", "#f39c12"),
        "faith": ("十", "信仰", "#9b59b6"),
        "loyalty": ("盾", "忠诚", "#3498db"),
        "reputation": ("*", "声望", "#2ecc71"),
        "intrigue": ("刃", "谋略", "#7f8c8d"),
    }

    ## 关系数据
    relation_data = [
        ("rel_aldric", "奥尔德里克", "管家", "#8b0000"),
        ("rel_elena", "艾琳娜", "侍女", "#9370db"),
        ("rel_bishop", "主教马修斯", "教会", "#ffd700"),
        ("rel_baron", "冯·哈根男爵", "贵族", "#2f4f4f"),
        ("rel_captain", "队长雷恩", "军队", "#4682b4"),
        ("rel_queen", "伊莎贝拉王后", "王室", "#800080"),
    ]

    ## 关系等级阈值
    _rel_thresholds = [("冷淡", -50), ("中立", -10), ("友好", 20), ("亲密", 60), ("满", 100)]

    def get_next_rel_info(rel_val):
        """返回 (下一等级名, 还差多少)"""
        for label, threshold in _rel_thresholds:
            if rel_val < threshold:
                return (label, threshold - rel_val)
        return ("", 0)

transform stats_panel_show:
    on show:
        alpha 0.0 xoffset 40
        ease 0.35 alpha 1.0 xoffset 0
    on hide:
        ease 0.25 alpha 0.0 xoffset 40

transform stats_overlay_show:
    on show:
        alpha 0.0
        ease 0.25 alpha 1.0
    on hide:
        ease 0.2 alpha 0.0

screen stats_screen():
    tag menu
    modal True
    zorder 150

    ## 半透明暗色遮罩
    add Solid("#000000aa") at stats_overlay_show
    key "K_ESCAPE" action Hide("stats_screen")
    key "K_s" action Hide("stats_screen")

    ## 安卓返回键关闭面板
    key "game_menu" action Hide("stats_screen")

    ## 右侧面板（手机全屏，PC侧边栏）
    frame at stats_panel_show:
        xalign 1.0
        yalign 0.5
        xpadding 0
        ypadding 0
        if renpy.variant("small"):
            xsize 1.0
            ysize 1.0
        else:
            xsize 440
            ysize 660
        background Solid("#0f0d1af0")

        vbox:
            spacing 0

            ## ═══ 标题栏 ═══
            frame:
                xfill True
                ysize 70
                background Solid("#1a1528")
                xpadding 24
                ypadding 0

                hbox:
                    yalign 0.5
                    xfill True

                    vbox:
                        text "[player_name]" size 24 color "#d4a942" font "msyh.ttf" outlines [(2, "#000000cc", 0, 0)]
                        text "艾登堡领主" size 14 color "#8a7e60"

                    textbutton "X":
                        xalign 1.0
                        yalign 0.0
                        text_size 20
                        text_color "#6a5e48"
                        text_hover_color "#d4a942"
                        action Hide("stats_screen")

            ## 分隔线
            add Solid("#d4a94230") xsize 1.0 ysize 2

            ## ═══ 可滚动内容区 ═══
            viewport:
                xfill True
                ysize 586
                mousewheel True
                draggable True
                scrollbars "vertical"

                frame:
                    background None
                    xpadding 24
                    ypadding 16
                    xfill True

                    vbox:
                        spacing 6

                        ## ─── 核心属性 ─── ##
                        hbox:
                            spacing 6
                            text "*" size 18 color "#d4a942" yalign 0.5
                            text "核心属性" size 18 color "#d4a942" font "msyh.ttf"

                        null height 4

                        ## 属性条 — 双列布局（含趋势箭头和预警）
                        grid 2 3:
                            spacing 8
                            xfill True

                            ## 权力
                            vbox:
                                spacing 2
                                hbox:
                                    text "剑 权力" size 14 color "#e0d8c8" xsize 70
                                    $ _trend_power = get_stat_trend("power")
                                    if _trend_power == "up":
                                        text "^" size 12 color "#2ecc71" yalign 0.5
                                    elif _trend_power == "down":
                                        text "v" size 12 color "#e74c3c" yalign 0.5
                                    text "[power]" size 14 color "#e74c3c" xalign 1.0 bold True
                                bar:
                                    value StaticValue(power, 100)
                                    xmaximum 180
                                    ysize 8
                                    left_bar Solid("#e74c3c")
                                    right_bar Solid("#1a1528")
                                if power <= STAT_DANGER_LOW:
                                    text "! 危险" size 10 color "#e74c3c"

                            ## 财富
                            vbox:
                                spacing 2
                                hbox:
                                    text "金 财富" size 14 color "#e0d8c8" xsize 70
                                    $ _trend_wealth = get_stat_trend("wealth")
                                    if _trend_wealth == "up":
                                        text "^" size 12 color "#2ecc71" yalign 0.5
                                    elif _trend_wealth == "down":
                                        text "v" size 12 color "#e74c3c" yalign 0.5
                                    text "[wealth]" size 14 color "#f39c12" xalign 1.0 bold True
                                bar:
                                    value StaticValue(wealth, 100)
                                    xmaximum 180
                                    ysize 8
                                    left_bar Solid("#f39c12")
                                    right_bar Solid("#1a1528")
                                if wealth <= STAT_DANGER_LOW:
                                    text "! 危险" size 10 color "#e74c3c"

                            ## 信仰
                            vbox:
                                spacing 2
                                hbox:
                                    text "十 信仰" size 14 color "#e0d8c8" xsize 70
                                    $ _trend_faith = get_stat_trend("faith")
                                    if _trend_faith == "up":
                                        text "^" size 12 color "#2ecc71" yalign 0.5
                                    elif _trend_faith == "down":
                                        text "v" size 12 color "#e74c3c" yalign 0.5
                                    text "[faith]" size 14 color "#9b59b6" xalign 1.0 bold True
                                bar:
                                    value StaticValue(faith, 100)
                                    xmaximum 180
                                    ysize 8
                                    left_bar Solid("#9b59b6")
                                    right_bar Solid("#1a1528")
                                if faith <= STAT_DANGER_LOW:
                                    text "! 危险" size 10 color "#e74c3c"

                            ## 忠诚
                            vbox:
                                spacing 2
                                hbox:
                                    text "盾 忠诚" size 14 color "#e0d8c8" xsize 70
                                    $ _trend_loyalty = get_stat_trend("loyalty")
                                    if _trend_loyalty == "up":
                                        text "^" size 12 color "#2ecc71" yalign 0.5
                                    elif _trend_loyalty == "down":
                                        text "v" size 12 color "#e74c3c" yalign 0.5
                                    text "[loyalty]" size 14 color "#3498db" xalign 1.0 bold True
                                bar:
                                    value StaticValue(loyalty, 100)
                                    xmaximum 180
                                    ysize 8
                                    left_bar Solid("#3498db")
                                    right_bar Solid("#1a1528")
                                if loyalty <= STAT_DANGER_LOW:
                                    text "! 危险" size 10 color "#e74c3c"

                            ## 声望
                            vbox:
                                spacing 2
                                hbox:
                                    text "* 声望" size 14 color "#e0d8c8" xsize 70
                                    $ _trend_reputation = get_stat_trend("reputation")
                                    if _trend_reputation == "up":
                                        text "^" size 12 color "#2ecc71" yalign 0.5
                                    elif _trend_reputation == "down":
                                        text "v" size 12 color "#e74c3c" yalign 0.5
                                    text "[reputation]" size 14 color "#2ecc71" xalign 1.0 bold True
                                bar:
                                    value StaticValue(reputation, 100)
                                    xmaximum 180
                                    ysize 8
                                    left_bar Solid("#2ecc71")
                                    right_bar Solid("#1a1528")
                                if reputation <= STAT_DANGER_LOW:
                                    text "! 危险" size 10 color "#e74c3c"

                            ## 谋略
                            vbox:
                                spacing 2
                                hbox:
                                    text "刃 谋略" size 14 color "#e0d8c8" xsize 70
                                    $ _trend_intrigue = get_stat_trend("intrigue")
                                    if _trend_intrigue == "up":
                                        text "^" size 12 color "#2ecc71" yalign 0.5
                                    elif _trend_intrigue == "down":
                                        text "v" size 12 color "#e74c3c" yalign 0.5
                                    text "[intrigue]" size 14 color "#7f8c8d" xalign 1.0 bold True
                                bar:
                                    value StaticValue(intrigue, 100)
                                    xmaximum 180
                                    ysize 8
                                    left_bar Solid("#7f8c8d")
                                    right_bar Solid("#1a1528")
                                if intrigue <= STAT_DANGER_LOW:
                                    text "! 危险" size 10 color "#e74c3c"

                        null height 12

                        ## 分割线
                        add Solid("#d4a94220") xsize 1.0 ysize 1

                        null height 8

                        ## ─── 人物关系 ─── ##
                        hbox:
                            spacing 6
                            text "*" size 18 color "#d4a942" yalign 0.5
                            text "人物关系" size 18 color "#d4a942" font "msyh.ttf"

                        null height 6

                        ## 关系列表（含等级进度提示）
                        for var_name, char_name, title, char_color in relation_data:
                            $ rel_val = getattr(store, var_name, 0)
                            $ rel_pct = (rel_val + 100) / 200.0
                            ## 等级划分: 敌对(<-50), 冷淡(<-10), 中立(<20), 友好(<60), 亲密(>=60)
                            $ rel_label = "敌对" if rel_val < -50 else ("冷淡" if rel_val < -10 else ("中立" if rel_val < 20 else ("友好" if rel_val < 60 else "亲密")))
                            $ rel_color = "#e74c3c" if rel_val < -50 else ("#e67e22" if rel_val < -10 else ("#8a7e60" if rel_val < 20 else ("#2ecc71" if rel_val < 60 else "#d4a942")))
                            ## 距下一等级还差多少
                            $ _next_label, _next_gap = get_next_rel_info(rel_val)

                            frame:
                                xfill True
                                ypadding 8
                                xpadding 12
                                background Solid("#1a152800")

                                vbox:
                                    spacing 3

                                    hbox:
                                        xfill True
                                        hbox:
                                            spacing 8
                                            text char_name size 15 color char_color font "msyh.ttf" bold True yalign 0.5
                                            text title size 11 color "#6a5e48" yalign 0.5

                                        hbox:
                                            xalign 1.0
                                            spacing 6
                                            text rel_label size 12 color rel_color yalign 0.5
                                            text "[rel_val]" size 13 color rel_color bold True yalign 0.5

                                    ## 好感度条 (-100 到 100, 居中为0)
                                    bar:
                                        value StaticValue(rel_pct, 1.0)
                                        xmaximum 380
                                        ysize 5
                                        left_bar Solid(rel_color)
                                        right_bar Solid("#1a1528")

                                    ## 距下一等级提示
                                    if _next_label and _next_gap > 0 and rel_val < 100:
                                        text "距「[_next_label]」还需 +[_next_gap]" size 10 color "#4a4040"

                        null height 12

                        ## 分割线
                        add Solid("#d4a94220") xsize 1.0 ysize 1

                        null height 8

                        ## ─── 剧情标记 ─── ##
                        hbox:
                            spacing 6
                            text "【卷】" size 18 color "#d4a942" yalign 0.5
                            text "重要抉择" size 18 color "#d4a942" font "msyh.ttf"

                        null height 4

                        if father_death_known:
                            text "• 已知晓父亲死因真相" size 13 color "#8a7e60"
                        if secret_passage_found:
                            text "• 发现了城堡密道" size 13 color "#8a7e60"
                        if spy_network:
                            text "• 建立了间谍网络" size 13 color "#8a7e60"
                        if alliance_baron:
                            text "• 与男爵结盟" size 13 color "#8a7e60"
                        if alliance_church:
                            text "• 与教会结盟" size 13 color "#8a7e60"
                        if dark_lily_joined:
                            text "• 加入了暗百合" size 13 color "#8a7e60"
                        if dark_lily_destroyed:
                            text "• 摧毁了暗百合" size 13 color "#8a7e60"
                        if elena_romance:
                            text "• 与艾琳娜的浪漫" size 13 color "#9370db"
                        if queen_trust:
                            text "• 获得王后信任" size 13 color "#800080"
                        if first_decree:
                            text "• 首项法令: [first_decree]" size 13 color "#8a7e60"

                        null height 10


## 快捷键：S 键打开/关闭状态面板
init python:
    def toggle_stats():
        if renpy.get_screen("stats_screen"):
            renpy.hide_screen("stats_screen")
        else:
            renpy.show_screen("stats_screen")
        renpy.restart_interaction()

    config.underlay.append(renpy.Keymap(s=toggle_stats))


## ============================================================
## 属性变化通知 — 屏幕上方金色弹幕
## ============================================================

screen stat_change_notify(stat_name, old_val, new_val):
    zorder 200
    $ delta = new_val - old_val
    $ color = "#2ecc71" if delta > 0 else "#e74c3c"
    $ sign = "+" if delta > 0 else ""

    frame:
        xalign 0.5
        ypos 80
        background Solid("#0f0d1aee")
        xpadding 24
        ypadding 10

        hbox:
            spacing 8
            text stat_name size 16 color "#d4a942" font "msyh.ttf" yalign 0.5
            text "[sign][delta]" size 18 color color bold True yalign 0.5

    timer 2.0 action Hide("stat_change_notify")

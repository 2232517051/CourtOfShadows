## ============================================================
## 平衡性调试 & 结局可达性分析
## balance.rpy
## 开发者工具：Shift+B 打开调试面板
## ============================================================


################################################################################
## 1. 结局需求定义 & 可达性检查
################################################################################

init python:

    ## 结局需求配置：(结局id, 名称, 需求描述, 检查函数)
    _ending_requirements = {
        "iron_lord": {
            "name": "铁腕领主",
            "icon": "剑",
            "color": "#e74c3c",
            "desc": "以武力征服一切",
            "requirement": "权力 >= 60",
            "check": lambda: store.power >= 60,
            "stat": "power",
            "threshold": 60,
        },
        "shadow_king": {
            "name": "影中之王",
            "icon": "刃",
            "color": "#7f8c8d",
            "desc": "在暗影中操控全局",
            "requirement": "谋略 >= 60",
            "check": lambda: store.intrigue >= 60,
            "stat": "intrigue",
            "threshold": 60,
        },
        "holy_guardian": {
            "name": "圣光守护",
            "icon": "十",
            "color": "#9b59b6",
            "desc": "以信仰之力化解战争",
            "requirement": "信仰 >= 60",
            "check": lambda: store.faith >= 60,
            "stat": "faith",
            "threshold": 60,
        },
        "peoples_lord": {
            "name": "人民领主",
            "icon": "心",
            "color": "#3498db",
            "desc": "守护百姓的幸福",
            "requirement": "忠诚 >= 60",
            "check": lambda: store.loyalty >= 60,
            "stat": "loyalty",
            "threshold": 60,
        },
        "truth": {
            "name": "真相大白",
            "icon": "日",
            "color": "#f39c12",
            "desc": "揭露全部真相（最佳结局）",
            "requirement": "发现真凶 (true_killer_known = True)",
            "check": lambda: store.true_killer_known,
            "stat": None,
            "threshold": None,
        },
    }

    def check_ending_reachability():
        """
        分析当前属性状态，返回各结局的可达性报告。
        返回格式: list of (结局id, 名称, 是否可达, 差距描述)
        """
        results = []

        for end_id, info in _ending_requirements.items():
            reachable = info["check"]()

            if reachable:
                gap_desc = "已满足条件"
            else:
                if info["stat"]:
                    ## 数值型条件：计算差距
                    current_val = getattr(store, info["stat"], 0)
                    needed = info["threshold"] - current_val
                    stat_names = {
                        "power": "权力", "wealth": "财富", "faith": "信仰",
                        "loyalty": "忠诚", "reputation": "声望", "intrigue": "谋略"
                    }
                    stat_label = stat_names.get(info["stat"], info["stat"])
                    gap_desc = "还需 %s +%d（当前 %d / 需要 %d）" % (stat_label, needed, current_val, info["threshold"])
                else:
                    ## 布尔型条件（真相结局）
                    gap_desc = "需要在第三章发现父亲死因真相"

            results.append((end_id, info["name"], reachable, gap_desc))

        return results

    def get_reachable_count():
        """返回当前可达的结局数量"""
        return sum(1 for _, _, reachable, _ in check_ending_reachability() if reachable)


################################################################################
## 2. 调试/平衡面板界面 (Shift+B，仅开发者模式)
################################################################################

screen balance_debug():
    ## 调试面板：显示所有属性、关系、剧情标记和结局可达性
    zorder 400
    modal True

    key "K_ESCAPE" action Hide("balance_debug")
    key "shift_K_b" action Hide("balance_debug")

    add Solid("#0a0812ee")

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 24
        xminimum 750
        xmaximum 800
        background Solid("#0f0d1af8")

        viewport:
            mousewheel True
            draggable True
            xfill True
            ysize 550

            vbox:
                spacing 12

                ## 标题栏
                hbox:
                    xfill True
                    hbox:
                        spacing 8
                        text "【工具】" size 22 yalign 0.5
                        text "平衡性调试面板" size 24 color "#d4a942" font "msyh.ttf" bold True

                    textbutton "X 关闭":
                        xalign 1.0
                        text_size 16
                        text_color "#e74c3c"
                        text_hover_color "#ff6b6b"
                        action Hide("balance_debug")

                add Solid("#d4a94240") xsize 1.0 ysize 1

                ## ──────────────────────────────────────
                ## 区域A：核心属性一览
                ## ──────────────────────────────────────
                text "* 核心属性" size 18 color "#d4a942" font "msyh.ttf"

                grid 3 2:
                    spacing 8
                    xalign 0.5

                    for _stat_key, _stat_label, _stat_color in [("power", "权力", "#e74c3c"), ("wealth", "财富", "#f39c12"), ("faith", "信仰", "#9b59b6"), ("loyalty", "忠诚", "#3498db"), ("reputation", "声望", "#2ecc71"), ("intrigue", "谋略", "#7f8c8d")]:
                        $ _sv = getattr(store, _stat_key, 0)
                        frame:
                            xsize 220
                            xpadding 12
                            ypadding 8
                            background Solid("#1a152850")

                            vbox:
                                spacing 4
                                hbox:
                                    xfill True
                                    text _stat_label size 14 color "#e0d8c8" font "msyh.ttf"
                                    text "[_sv]/100" size 14 color _stat_color bold True xalign 1.0

                                bar:
                                    value StaticValue(_sv, 100)
                                    xfill True
                                    ysize 6
                                    left_bar Solid(_stat_color)
                                    right_bar Solid("#1a1528")

                                ## 属性快速调整按钮（开发用）
                                hbox:
                                    spacing 4
                                    xalign 0.5
                                    textbutton "-10":
                                        text_size 11
                                        text_color "#e74c3c"
                                        text_hover_color "#ff6b6b"
                                        action [SetVariable(_stat_key, max(0, _sv - 10)), renpy.restart_interaction]
                                    textbutton "-5":
                                        text_size 11
                                        text_color "#e78c3c"
                                        text_hover_color "#ffaa6b"
                                        action [SetVariable(_stat_key, max(0, _sv - 5)), renpy.restart_interaction]
                                    textbutton "+5":
                                        text_size 11
                                        text_color "#3cbe7c"
                                        text_hover_color "#6bffaa"
                                        action [SetVariable(_stat_key, min(100, _sv + 5)), renpy.restart_interaction]
                                    textbutton "+10":
                                        text_size 11
                                        text_color "#2ecc71"
                                        text_hover_color "#6bff9b"
                                        action [SetVariable(_stat_key, min(100, _sv + 10)), renpy.restart_interaction]

                null height 4

                ## ──────────────────────────────────────
                ## 区域B：角色好感度
                ## ──────────────────────────────────────
                text "* 角色好感度" size 18 color "#d4a942" font "msyh.ttf"

                grid 4 2:
                    spacing 6
                    xalign 0.5

                    for _rel_key, _rel_name, _rel_color in [("rel_aldric", "奥尔德里克", "#8b0000"), ("rel_elena", "艾琳娜", "#9370db"), ("rel_bishop", "主教", "#ffd700"), ("rel_baron", "男爵", "#2f4f4f"), ("rel_captain", "队长雷恩", "#4682b4"), ("rel_queen", "王后", "#800080"), ("rel_prince", "王子", "#4169e1"), ("rel_lily", "暗百合", "#2d1b4e")]:
                        $ _rv = getattr(store, _rel_key, 0)
                        $ _rv_color = "#2ecc71" if _rv > 0 else ("#e74c3c" if _rv < 0 else "#6a5e48")

                        frame:
                            xsize 170
                            xpadding 8
                            ypadding 6
                            background Solid("#1a152840")

                            vbox:
                                spacing 2
                                text _rel_name size 12 color _rel_color font "msyh.ttf"
                                hbox:
                                    text "[_rv]" size 16 color _rv_color bold True
                                    text "/100" size 10 color "#4a4030" yalign 1.0

                null height 4

                ## ──────────────────────────────────────
                ## 区域C：剧情标记
                ## ──────────────────────────────────────
                text "【剧情标记】" size 18 color "#d4a942" font "msyh.ttf"

                grid 3 5:
                    spacing 4
                    xalign 0.5

                    for _flag_name, _flag_label in [("father_death_known", "知晓死因"), ("secret_passage_found", "发现密道"), ("spy_network", "间谍网络"), ("alliance_baron", "男爵同盟"), ("alliance_church", "教会同盟"), ("merchant_deal", "商人合作"), ("assassination_survived", "刺杀幸存"), ("dark_lily_joined", "加入暗百合"), ("dark_lily_destroyed", "摧毁暗百合"), ("true_killer_known", "发现真凶"), ("father_letters_found", "密信收集"), ("poison_evidence", "毒药证据"), ("queen_trust", "王后信任"), ("prince_ally", "王子盟友"), ("elena_romance", "艾琳娜恋情")]:
                        $ _fv = getattr(store, _flag_name, False)
                        $ _f_icon = ">" if _fv else "×"
                        $ _f_color = "#2ecc71" if _fv else "#e74c3c60"

                        frame:
                            xsize 220
                            xpadding 8
                            ypadding 4
                            background Solid("#1a152830")

                            hbox:
                                spacing 6
                                text _f_icon size 14 color _f_color yalign 0.5
                                text _flag_label size 13 color ("#c8b890" if _fv else "#4a4030") font "msyh.ttf"

                                ## 切换按钮（开发用）
                                textbutton ("关" if _fv else "开"):
                                    xalign 1.0
                                    text_size 11
                                    text_color "#d4a942"
                                    text_hover_color "#ffd866"
                                    action [ToggleVariable(_flag_name), renpy.restart_interaction]

                null height 4
                add Solid("#d4a94230") xsize 1.0 ysize 1
                null height 4

                ## ──────────────────────────────────────
                ## 区域D：结局可达性分析
                ## ──────────────────────────────────────
                hbox:
                    spacing 8
                    text "【目标】" size 18 yalign 0.5
                    text "结局可达性分析" size 18 color "#d4a942" font "msyh.ttf"
                    $ _reachable_n = get_reachable_count()
                    text "（[_reachable_n]/5 可达）" size 14 color "#8a7e60" yalign 0.5

                for _end_id, _end_name, _end_reachable, _end_gap in check_ending_reachability():
                    $ _e_info = _ending_requirements[_end_id]
                    $ _e_border = _e_info["color"] if _end_reachable else "#1a1528"

                    frame:
                        xfill True
                        xpadding 16
                        ypadding 10
                        background Solid((_e_info["color"] + "15") if _end_reachable else "#0f0d1a40")

                        hbox:
                            spacing 12
                            yalign 0.5

                            ## 状态图标
                            frame:
                                xsize 36
                                ysize 36
                                background Solid(_e_info["color"] + ("40" if _end_reachable else "15"))
                                text _e_info["icon"] xalign 0.5 yalign 0.5 size 18

                            ## 结局信息
                            vbox:
                                spacing 2
                                hbox:
                                    spacing 8
                                    text _end_name size 16 color (_e_info["color"] if _end_reachable else "#4a4030") font "msyh.ttf" bold True
                                    if _end_reachable:
                                        text "V 可达" size 12 color "#2ecc71" yalign 0.5
                                    else:
                                        text "× 未满足" size 12 color "#e74c3c80" yalign 0.5

                                text "条件: [_e_info['requirement']]" size 12 color "#6a5e48"
                                text _end_gap size 12 color ("#2ecc71" if _end_reachable else "#e78c3c")

                null height 8
                add Solid("#d4a94230") xsize 1.0 ysize 1
                null height 4

                ## ──────────────────────────────────────
                ## 区域E：难度 & 持久化状态
                ## ──────────────────────────────────────
                text "【设置】系统状态" size 18 color "#d4a942" font "msyh.ttf"

                grid 2 3:
                    spacing 6
                    xalign 0.5

                    for _sys_label, _sys_val in [("当前难度", persistent.difficulty or "normal"), ("NG+解锁", "是" if persistent.ng_plus_unlocked else "否"), ("已完成章节", str(len(persistent.chapters_completed or set()))), ("已解锁结局", str(len(persistent.endings_seen or set())) + "/5"), ("收藏品", str(len(persistent.collectibles_found or set())) + "/" + str(len(collectible_items))), ("成就", str(len(persistent.achievements or set())) + "/" + str(len(achievement_data)))]:
                        frame:
                            xsize 330
                            xpadding 12
                            ypadding 6
                            background Solid("#1a152830")

                            hbox:
                                spacing 8
                                text _sys_label size 13 color "#8a7e60" font "msyh.ttf" xsize 100
                                text _sys_val size 14 color "#e0d8c8" bold True


################################################################################
## 3. 快捷键绑定 (仅开发者模式)
################################################################################

init python:
    ## Shift+B 打开平衡性调试面板（仅在 config.developer 为 True 时生效）
    def _toggle_balance_debug():
        if config.developer:
            if renpy.get_screen("balance_debug"):
                renpy.hide_screen("balance_debug")
            else:
                renpy.show_screen("balance_debug")
            renpy.restart_interaction()

    config.keymap.setdefault("game_menu", [])
    config.underlay.append(renpy.Keymap(shift_K_b=_toggle_balance_debug))

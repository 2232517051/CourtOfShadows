## ============================================================
## 死亡/危机机制 — crisis.rpy
## 危机事件系统：根据属性和勇气计算成功率，失败受伤，3次死亡
## ============================================================

################################################################################
## 1. 危机变量
################################################################################

default crisis_active = False
default crisis_dice_bonus = 0
default crisis_dice_total = 0
default crisis_injuries = 0          ## 受伤次数，3次=死亡
default crisis_type = "combat"       ## 当前危机类型
default crisis_difficulty = 5        ## 当前危机难度(1-10)
default crisis_success_label = ""    ## 成功后跳转
default crisis_fail_label = ""       ## 失败后跳转
default crisis_success_chance = 50   ## 计算出的成功率
default crisis_description = ""      ## 危机描述文本
default crisis_courage_cost = 20     ## 迎接挑战消耗的勇气
default crisis_courage_gain = 15     ## 退缩回复的勇气
default crisis_allow_skip = True     ## 是否允许玩家退缩(False = 强制面对, 用于剧情上不能逃避的关键时刻)
default crisis_result = ""           ## "success" / "fail" / "retreat"
default crisis_roll_value = 0        ## 骰子结果
default crisis_injury_text = ""      ## 受伤描述
default crisis_context_mods = []     ## 本次危机的语境修正 [(标签, 数值), ...], trigger_crisis 时生成

## 受伤减益效果 — 已废弃(2026-07-26)。这三个变量从未真正扣属性、也不参与判定,
## 受伤界面却显示「权力 -3(伤势影响)」, 属于显示欺诈; 真实惩罚一直是
## crisis_injuries 计数(每伤 bonus -1, 上限 -2), 界面已改为如实显示后者。
## default 保留仅为旧存档兼容, 不再有任何读写。
default injury_debuff_power = 0      ## 权力减益
default injury_debuff_intrigue = 0   ## 谋略减益
default injury_debuff_faith = 0      ## 信仰减益

################################################################################
## 2. 危机函数
################################################################################

init python:
    import random as _crisis_random

    ## 危机类型数据 (图标, 名称, 主属性)
    CRISIS_TYPES = {
        "combat":   ("剑", "战斗危机", "power"),
        "intrigue": ("刃", "阴谋危机", "intrigue"),
        "faith":    ("十", "信仰危机", "faith"),
        "survival": ("盾", "生存危机", "loyalty"),
    }

    ## 受伤描述模板
    INJURY_DESCRIPTIONS = {
        "combat":   ["你在战斗中被敌人的刀刃划伤了手臂。", "一记重击让你的肋骨隐隐作痛。", "箭矢擦过你的肩头，留下一道血痕。"],
        "intrigue": ["暗算让你中了轻微的毒，头脑昏沉。", "你在阴谋中失算，被对手抓住了把柄。", "一个陷阱差点要了你的命，你勉强逃脱。"],
        "faith":    ["信仰的动摇让你精神萎靡。", "诅咒的阴影笼罩着你，内心不安。", "你目睹了不该看到的东西，心神受创。"],
        "survival": ["严寒让你的手指失去了知觉。", "缺水和饥饿让你体力不支。", "你在荒野中迷路，身心俱疲。"],
    }

    ## 危机类型 → 属性/中文名 映射(bonus 计算与界面共用一份)
    CRISIS_STAT_MAP = {
        "combat":   "power",
        "intrigue": "intrigue",
        "faith":    "faith",
        "survival": "loyalty",
    }
    CRISIS_STAT_CN = {
        "combat": "权力", "intrigue": "谋略", "faith": "信仰", "survival": "忠诚",
    }

    def _auto_context_mods(crisis_type):
        """自动语境修正: 玩家攒下的剧情关系在对应类型的危机里帮一把。
        每条 +1(= 一个骰面 = 10% 成功率), 与 chapter4 潜入难度随暗百合关系
        变化的手写先例(chapter4.rpy _stealth_diff)同量级。"""
        mods = []
        if crisis_type == "intrigue" and getattr(store, "dark_lily_joined", False):
            mods.append(("暗百合的眼线", 1))
        if crisis_type == "faith" and getattr(store, "alliance_church", False):
            mods.append(("教会同盟", 1))
        if crisis_type == "combat" and getattr(store, "ch1_exp_captain_respect", False):
            mods.append(("雷恩的信服", 1))
        return mods

    def crisis_bonus_parts(crisis_type):
        """统一计算危机判定加成, 返回 (总加成, 分项列表[(标签, 数值), ...])。
        判定界面与结算共用这一份, 杜绝两处逻辑各自漂移。"""
        stat_name = CRISIS_STAT_MAP.get(crisis_type, "power")
        stat_val = getattr(store, stat_name, 30)

        parts = []
        base = max(-3, min(7, (stat_val - 30) // 10))
        parts.append(("{} {}".format(CRISIS_STAT_CN.get(crisis_type, "属性"), stat_val), base))

        if store.courage >= 60:
            parts.append(("勇气充沛", 1))

        injury_penalty = min(2, store.crisis_injuries)
        if injury_penalty:
            parts.append(("伤势 {}处".format(store.crisis_injuries), -injury_penalty))

        for _label, _val in store.crisis_context_mods:
            parts.append((_label, _val))

        total = sum(v for _, v in parts)
        return total, parts

    def calculate_crisis_chance(crisis_type, difficulty):
        """
        布兰特式 1d10 + bonus vs difficulty, 返回显示用成功概率(0-100)。
        bonus 组成见 crisis_bonus_parts(属性/勇气/伤势/语境修正)。
        成功概率 = 可成功的骰面数 / 10 * 100
        例：difficulty=6, bonus=2 → 需要 roll>=4 → 7个面 → 70%
        """
        bonus, _ = crisis_bonus_parts(crisis_type)

        ## 需要骰子 >= (difficulty - bonus)
        needed_roll = difficulty - bonus
        ## 骰子范围 1-10，成功面数
        success_faces = max(0, 10 - max(0, needed_roll - 1))
        chance = success_faces * 10

        return max(0, min(100, chance))

    def trigger_crisis(crisis_type, difficulty, description, success_label, fail_label, courage_cost=20, courage_gain=15, allow_skip=True, context_mods=None):
        """触发危机事件。allow_skip=False 强制玩家面对(隐藏退缩按钮), 用于剧情上不能逃避的关键时刻。
        context_mods: 额外语境修正 [(标签, 数值), ...], 叠加在自动修正之上,
        供调用点把「此时此地」的剧情状态写进判定(标签会逐条显示给玩家)。"""
        store.crisis_active = True
        store.crisis_type = crisis_type
        store.crisis_difficulty = difficulty
        store.crisis_description = description
        store.crisis_success_label = success_label
        store.crisis_fail_label = fail_label
        store.crisis_courage_cost = courage_cost
        store.crisis_courage_gain = courage_gain
        store.crisis_allow_skip = allow_skip
        store.crisis_context_mods = _auto_context_mods(crisis_type) + list(context_mods or [])
        store.crisis_success_chance = calculate_crisis_chance(crisis_type, difficulty)
        store.crisis_result = ""
        store.crisis_roll_value = 0

    def resolve_crisis(brave=True):
        """
        新解算：实际使用 dice_check 函数（布兰特式 1d10 + bonus）
        成功时：调用 add_path_mark(对应路线) 增加印记
        失败时：调用 _apply_injury
        意志消耗/恢复：使用 change_will()
        crisis_dice_bonus / crisis_dice_total 供 UI 显示
        """
        if brave:
            ## 消耗勇气
            change_will(-store.crisis_courage_cost)

            ## 加成与界面同源(crisis_bonus_parts), 含属性/勇气/伤势/语境修正。
            ## 注意: 勇气修正读的是扣完 courage_cost 之后的值——与旧逻辑一致,
            ## 玩家在界面上看到的加成可能因这次消耗掉档, 属已知口径, 不在本次改动。
            bonus, _ = crisis_bonus_parts(store.crisis_type)

            ## 掷骰
            roll = _crisis_random.randint(1, 10)
            total = roll + bonus
            store.crisis_roll_value = roll
            store.crisis_dice_bonus = bonus
            store.crisis_dice_total = total

            if total >= store.crisis_difficulty:
                ## 成功
                store.crisis_result = "success"
                ## 回复勇气
                change_will(25)
                ## 路线印记
                path_map = {
                    "combat":   "martial",
                    "intrigue": "scheme",
                    "faith":    "faith",
                    "survival": "diplomacy",
                }
                add_path_mark(path_map.get(store.crisis_type, "martial"))
            else:
                ## 失败 — 受伤
                store.crisis_result = "fail"
                store.crisis_injuries += 1
                _apply_injury(store.crisis_type)
        else:
            ## 退缩
            store.crisis_result = "retreat"
            change_will(store.crisis_courage_gain)

        store.crisis_active = False

    def _apply_injury(crisis_type):
        """受伤: 抽一条受伤文案。实际惩罚由 crisis_injuries 计数承担
        (crisis_bonus_parts 里每伤 -1, 上限 -2; 满 3 处死亡),
        不再写入 injury_debuff_*(那套减益从未生效, 见文件头注释)。"""
        descs = INJURY_DESCRIPTIONS.get(crisis_type, INJURY_DESCRIPTIONS["combat"])
        store.crisis_injury_text = _crisis_random.choice(descs)

    def is_dead():
        """检查是否死亡"""
        return store.crisis_injuries >= 3

    def clear_injuries():
        """清除所有伤势（读档/重开时）"""
        store.crisis_injuries = 0
        store.injury_debuff_power = 0
        store.injury_debuff_intrigue = 0
        store.injury_debuff_faith = 0
        store.crisis_injury_text = ""

################################################################################
## 3. 危机事件UI — 全屏覆盖
################################################################################

transform crisis_overlay_show:
    on show:
        alpha 0.0
        ease 0.4 alpha 1.0
    on hide:
        ease 0.3 alpha 0.0

transform crisis_panel_appear:
    on show:
        alpha 0.0 zoom 0.9
        ease 0.5 alpha 1.0 zoom 1.0
    on hide:
        ease 0.3 alpha 0.0 zoom 0.95

transform crisis_dice_spin:
    ## 简单的数字滚动效果
    on show:
        alpha 0.0 zoom 0.5
        ease 0.2 alpha 1.0 zoom 1.2
        ease 0.15 zoom 1.0

screen crisis_event():
    modal True
    zorder 200

    ## 全屏暗色覆盖
    add Solid("#000000dd") at crisis_overlay_show

    $ _ct = CRISIS_TYPES.get(crisis_type, ("?", "未知危机", "power"))
    $ _icon = _ct[0]
    $ _name = _ct[1]
    $ _chance = crisis_success_chance
    $ _can_brave = has_courage(crisis_courage_cost)

    ## 危机面板
    frame at crisis_panel_appear:
        xalign 0.5
        yalign 0.5
        xsize 500
        background Solid("#0f0d1af5")
        xpadding 32
        ypadding 28

        vbox:
            spacing 16
            xalign 0.5

            ## 标题
            hbox:
                xalign 0.5
                spacing 10
                text _icon size 32 color "#e74c3c" yalign 0.5
                text _name size 28 color "#e74c3c" font "msyh.ttf" bold True yalign 0.5

            ## 分隔线
            add Solid("#e74c3c40") xsize 0.9 ysize 2 xalign 0.5

            ## 危机描述
            text crisis_description size 16 color "#c8b890" font "msyh.ttf" text_align 0.5 xalign 0.5

            null height 4

            ## 成功率显示
            frame:
                xalign 0.5
                background Solid("#1a152880")
                xpadding 24
                ypadding 12

                vbox:
                    spacing 8
                    xalign 0.5

                    text "成功率" size 14 color "#8a7e60" xalign 0.5

                    ## 成功率数值 — 颜色根据高低变化
                    if _chance >= 70:
                        text "[_chance]%" size 36 color "#2ecc71" bold True xalign 0.5
                    elif _chance >= 40:
                        text "[_chance]%" size 36 color "#f39c12" bold True xalign 0.5
                    else:
                        text "[_chance]%" size 36 color "#e74c3c" bold True xalign 0.5

                    ## 成功率条
                    bar:
                        value StaticValue(_chance, 100)
                        xmaximum 300
                        ysize 10
                        xalign 0.5
                        if _chance >= 70:
                            left_bar Solid("#2ecc71")
                        elif _chance >= 40:
                            left_bar Solid("#f39c12")
                        else:
                            left_bar Solid("#e74c3c")
                        right_bar Solid("#1a1528")

                    ## 判定公式 + 加成分项(与结算共用 crisis_bonus_parts, 见 9.2 语境修正改造)
                    $ _bonus_show, _bonus_parts = crisis_bonus_parts(crisis_type)
                    text "1d10 + [_bonus_show] ≥ [crisis_difficulty]" size 12 color "#8a7e60" font "msyh.ttf" xalign 0.5

                    vbox:
                        spacing 2
                        xalign 0.5
                        for _plabel, _pval in _bonus_parts:
                            if _pval > 0:
                                text "[_plabel]　{color=#2ecc71}+[_pval]{/color}" size 12 color "#8a7e60" font "msyh.ttf" xalign 0.5
                            elif _pval < 0:
                                text "[_plabel]　{color=#e74c3c}[_pval]{/color}" size 12 color "#8a7e60" font "msyh.ttf" xalign 0.5
                            else:
                                text "[_plabel]　+0" size 12 color "#8a7e60" font "msyh.ttf" xalign 0.5

            ## 当前伤势提醒
            if crisis_injuries > 0:
                text "当前伤势：[crisis_injuries]/3" size 14 color "#e74c3c" xalign 0.5

            null height 4

            ## 选项按钮
            hbox:
                xalign 0.5
                spacing 20

                ## 迎接挑战
                if _can_brave:
                    textbutton "迎接挑战":
                        text_size 18
                        text_color "#d4a942"
                        text_hover_color "#ffd700"
                        text_font "msyh.ttf"
                        xsize 180
                        action [Function(resolve_crisis, brave=True), Return("brave")]
                else:
                    ## 勇气不足 — 灰色不可点
                    frame:
                        xsize 180
                        background Solid("#1a152880")
                        xpadding 12
                        ypadding 8
                        vbox:
                            xalign 0.5
                            text "迎接挑战" size 18 color "#4a4a4a" font "msyh.ttf" xalign 0.5
                            text "需要 [crisis_courage_cost] 勇气" size 12 color "#8b1a1a" xalign 0.5

                ## 退缩 (allow_skip=False 时不显示)
                if crisis_allow_skip:
                    textbutton "退缩":
                        text_size 18
                        text_color "#6a5e48"
                        text_hover_color "#c8b890"
                        text_font "msyh.ttf"
                        xsize 180
                        action [Function(resolve_crisis, brave=False), Return("retreat")]

            ## 退缩说明 (allow_skip=False 时不显示)
            if crisis_allow_skip:
                text "退缩：回复 [crisis_courage_gain] 勇气，但错过奖励" size 12 color "#6a5e48" xalign 0.5

################################################################################
## 4. 骰子结果Screen
################################################################################

screen crisis_dice_result():
    modal True
    zorder 210

    add Solid("#000000cc")

    frame at crisis_panel_appear:
        xalign 0.5
        yalign 0.5
        xsize 400
        background Solid("#0f0d1af5")
        xpadding 32
        ypadding 28

        vbox:
            spacing 16
            xalign 0.5

            ## 骰子数值
            text "[crisis_roll_value]" at crisis_dice_spin size 64 bold True xalign 0.5:
                if crisis_result == "success":
                    color "#2ecc71"
                else:
                    color "#e74c3c"

            ## 判定细节（新增）
            text "骰子 [crisis_roll_value] + 加成 [crisis_dice_bonus] = [crisis_dice_total]" size 14 color "#8a7e60" font "msyh.ttf" xalign 0.5

            ## 需要的数值
            text "需要总计 ≥ [crisis_difficulty]" size 16 color "#8a7e60" font "msyh.ttf" xalign 0.5

            ## 结果文字
            if crisis_result == "success":
                text "挑战成功！" size 28 color "#2ecc71" font "msyh.ttf" bold True xalign 0.5
            else:
                text "挑战失败..." size 28 color "#e74c3c" font "msyh.ttf" bold True xalign 0.5

    timer 2.5 action Hide("crisis_dice_result")

################################################################################
## 5. 受伤Screen
################################################################################

screen injury_screen():
    modal True
    zorder 200

    add Solid("#000000dd")

    frame at crisis_panel_appear:
        xalign 0.5
        yalign 0.5
        xsize 450
        background Solid("#1a0808f5")
        xpadding 32
        ypadding 28

        vbox:
            spacing 16
            xalign 0.5

            ## 标题
            text "负伤" size 28 color "#e74c3c" font "msyh.ttf" bold True xalign 0.5

            add Solid("#e74c3c40") xsize 0.9 ysize 2 xalign 0.5

            ## 受伤描述
            text crisis_injury_text size 16 color "#c8b890" font "msyh.ttf" text_align 0.5 xalign 0.5

            null height 8

            ## 当前伤势
            hbox:
                xalign 0.5
                spacing 8
                text "伤势：" size 18 color "#e0d8c8" font "msyh.ttf"

                ## 显示伤痕标记
                for i in range(3):
                    if i < crisis_injuries:
                        $ _ij = ui_icon("ico_alert", 22)
                        if _ij:
                            add _ij yalign 0.5
                        else:
                            text "X" size 22 color "#e74c3c" bold True
                    else:
                        $ _ijo = ui_icon("ico_alert", 22)
                        if _ijo:
                            add Transform(_ijo, matrixcolor=SaturationMatrix(0.0) * BrightnessMatrix(-0.6)) yalign 0.5
                        else:
                            text "O" size 22 color "#4a4a4a"

                text " [crisis_injuries]/3" size 18 color "#e74c3c" bold True

            ## 减益效果 — 如实显示真正生效的惩罚(危机判定加成扣减, 上限-2),
            ## 不再显示从未生效的「权力 -3(伤势影响)」假减益。
            $ _injury_penalty_disp = min(2, crisis_injuries)
            if _injury_penalty_disp > 0:
                text "此后危机判定加成 -[_injury_penalty_disp]（伤势影响）" size 14 color "#e74c3c" xalign 0.5

            ## 死亡警告
            if crisis_injuries >= 2:
                null height 4
                text "！ 再受一次伤就会死亡！" size 16 color "#ff0000" bold True xalign 0.5

            null height 8

            textbutton "继续":
                text_size 18
                text_color "#d4a942"
                text_hover_color "#ffd700"
                text_font "msyh.ttf"
                xalign 0.5
                action Return()

################################################################################
## 6. 死亡Screen
################################################################################

screen death_screen(cause="你的伤势过重，倒在了权谋的漩涡中。"):
    modal True
    zorder 300

    add Solid("#000000f0")

    frame at crisis_panel_appear:
        xalign 0.5
        yalign 0.5
        xsize 500
        background Solid("#0a0505f5")
        xpadding 40
        ypadding 36

        vbox:
            spacing 20
            xalign 0.5

            null height 20

            ## 死亡标题
            text "你的故事到此结束" size 32 color "#8b0000" font "msyh.ttf" bold True xalign 0.5

            add Solid("#8b000060") xsize 0.8 ysize 2 xalign 0.5

            ## 死因
            text cause size 18 color "#8a7e60" font "msyh.ttf" text_align 0.5 xalign 0.5

            null height 10

            ## 伤痕标记
            hbox:
                xalign 0.5
                spacing 6
                $ _dx = ui_icon("ico_alert", 26)
                if _dx:
                    add Transform(_dx, matrixcolor=TintMatrix("#8b0000")) yalign 0.5
                    add Transform(_dx, matrixcolor=TintMatrix("#8b0000")) yalign 0.5
                    add Transform(_dx, matrixcolor=TintMatrix("#8b0000")) yalign 0.5
                else:
                    text "X" size 24 color "#8b0000" bold True
                    text "X" size 24 color "#8b0000" bold True
                    text "X" size 24 color "#8b0000" bold True

            null height 20

            ## 按钮
            vbox:
                spacing 12
                xalign 0.5

                textbutton "读取存档":
                    text_size 20
                    text_color "#d4a942"
                    text_hover_color "#ffd700"
                    text_font "msyh.ttf"
                    xalign 0.5
                    action ShowMenu("load")

                textbutton "重新开始":
                    text_size 20
                    text_color "#6a5e48"
                    text_hover_color "#c8b890"
                    text_font "msyh.ttf"
                    xalign 0.5
                    action [Function(save_persistent_before_menu), MainMenu(confirm=False)]

################################################################################
## 7. 危机事件脚本 Label — 通用流程
################################################################################

## 用法：
## $ trigger_crisis("combat", 5, "边境遭遇战", "crisis_combat_win", "crisis_combat_lose")
## call crisis_encounter

label crisis_encounter:
    ## 显示危机事件界面，等待玩家选择
    call screen crisis_event

    ## 根据结果分支
    if crisis_result == "success":
        ## 显示骰子结果
        show screen crisis_dice_result
        pause 2.5
        hide screen crisis_dice_result
        jump expression crisis_success_label

    elif crisis_result == "fail":
        ## 显示骰子结果
        show screen crisis_dice_result
        pause 2.5
        hide screen crisis_dice_result

        ## 显示受伤界面
        call screen injury_screen

        ## 检查是否死亡
        if is_dead():
            call screen death_screen(cause=crisis_injury_text)
            return

        jump expression crisis_fail_label

    else:
        ## 退缩 — 返回调用处继续剧情
        return

## ============================================================
## 勇气系统 — courage.rpy
## 勇气代表主角面对危险时的胆魄，影响大胆选项的可用性
## ============================================================

## 注意：courage / max_courage 变量定义在 characters.rpy 中

################################################################################
## 1. 勇气函数
################################################################################

init python:
    def change_courage(amount):
        """改变勇气值并显示通知"""
        old = store.courage
        store.courage = max(0, min(store.max_courage, store.courage + amount))
        delta = store.courage - old
        if delta != 0:
            _show_stat_toast("勇气", delta, False)

    def has_courage(required):
        """检查是否拥有足够勇气"""
        return store.courage >= required

    def courage_check(required):
        """用于menu选项的勇气检查，返回True/False"""
        return store.courage >= required

    def get_courage_color():
        """根据勇气值返回对应颜色"""
        if store.courage >= 70:
            return "#d4a942"   ## 金色 — 高勇气
        elif store.courage >= 35:
            return "#e67e22"   ## 橙色 — 中等勇气
        else:
            return "#8b1a1a"   ## 暗红 — 低勇气

    def get_courage_level():
        """返回勇气等级描述"""
        if store.courage >= 80:
            return "无畏"
        elif store.courage >= 60:
            return "勇敢"
        elif store.courage >= 40:
            return "镇定"
        elif store.courage >= 20:
            return "犹豫"
        else:
            return "怯懦"

################################################################################
## 3. 勇气HUD — 常驻显示在屏幕左上角（游戏进行时）
################################################################################

screen courage_hud():
    zorder 100

    frame:
        xpos 15
        ypos 15
        background Solid("#0f0d1acc")
        xpadding 12
        ypadding 8

        hbox:
            spacing 6
            ## 火焰图标
            $ _c_color = get_courage_color()
            text "火" size 18 color _c_color yalign 0.5
            text "[courage]" size 16 color _c_color bold True yalign 0.5 font "msyh.ttf"

        ## 鼠标悬停提示
        tooltip "[courage]/[max_courage] — [get_courage_level()]"

################################################################################
## 4. 勇气条 — 嵌入状态面板（在核心属性下方）
################################################################################

screen courage_panel_section():
    ## 此screen可以被use到stats_screen中
    vbox:
        spacing 4

        hbox:
            spacing 6
            text "火" size 18 color "#d4a942" yalign 0.5
            text "勇气" size 18 color "#d4a942" font "msyh.ttf"

        null height 2

        vbox:
            spacing 2
            hbox:
                $ _c_color = get_courage_color()
                $ _c_level = get_courage_level()
                text "火 勇气" size 14 color "#e0d8c8" xsize 70
                text _c_level size 12 color _c_color yalign 0.5
                text "[courage]" size 14 color _c_color xalign 1.0 bold True
            bar:
                value StaticValue(courage, max_courage)
                xmaximum 180
                ysize 8
                left_bar Solid(_c_color)
                right_bar Solid("#1a1528")
            if courage <= 20:
                text "! 勇气不足" size 10 color "#8b1a1a"

################################################################################
## 5. 勇气不足提示弹窗
################################################################################

screen courage_insufficient(required=0):
    zorder 250

    frame at stat_toast_anim:
        xalign 0.5
        ypos 100
        background Solid("#3d1111ee")
        xpadding 28
        ypadding 12

        hbox:
            spacing 10
            text "火" size 18 color "#8b1a1a" yalign 0.5
            text "勇气不足！需要 [required] 勇气" size 16 color "#e74c3c" font "msyh.ttf" yalign 0.5

    timer 2.0 action Hide("courage_insufficient")

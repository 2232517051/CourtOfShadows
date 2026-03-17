## ============================================================
## 大厂级演出效果系统
## effects.rpy — 震屏/闪白/章节卡/教程/评分/属性通知
## ============================================================

################################################################################
## 1. 屏幕特效 Transform
################################################################################

## ── 震屏（轻微） ──
transform screen_shake_light:
    xoffset 0 yoffset 0
    ease 0.05 xoffset 5
    ease 0.05 xoffset -5
    ease 0.05 yoffset 3
    ease 0.05 xoffset 3
    ease 0.05 yoffset -3
    ease 0.05 xoffset -2
    ease 0.05 xoffset 0 yoffset 0

## ── 震屏（强烈） ──
transform screen_shake_heavy:
    xoffset 0 yoffset 0
    ease 0.04 xoffset 12
    ease 0.04 xoffset -10
    ease 0.04 yoffset 8
    ease 0.04 xoffset 8
    ease 0.04 yoffset -6
    ease 0.04 xoffset -6
    ease 0.04 yoffset 4
    ease 0.04 xoffset 4
    ease 0.04 xoffset -2
    ease 0.04 yoffset -2
    ease 0.04 xoffset 0 yoffset 0

## ── 角色登场 (从下方滑入) ──
transform char_entrance:
    alpha 0.0 yoffset 50
    ease 0.5 alpha 1.0 yoffset 0

## ── 角色退场 ──
transform char_exit:
    alpha 1.0 yoffset 0
    ease 0.4 alpha 0.0 yoffset 30

## ── 角色说话时轻微弹跳 ──
transform char_speak:
    yoffset 0
    ease 0.1 yoffset -5
    ease 0.15 yoffset 0

## ── 慢放大（戏剧性时刻） ──
transform dramatic_zoom:
    zoom 1.0
    ease 2.0 zoom 1.05

## ── 呼吸效果（待机角色） ──
transform char_idle:
    block:
        ease 3.0 yoffset -3
        ease 3.0 yoffset 0
        repeat


################################################################################
## 2. 全屏闪白/闪红/渐黑
################################################################################

## ── 闪白 ──
screen flash_white():
    zorder 200
    add Solid("#ffffff") at flash_effect
    timer 0.5 action Hide("flash_white")

## ── 闪红（受伤/死亡） ──
screen flash_red():
    zorder 200
    add Solid("#ff0000") at flash_effect
    timer 0.6 action Hide("flash_red")

## ── 闪金（成就/重要获得） ──
screen flash_gold():
    zorder 200
    add Solid("#d4a942") at flash_effect_slow
    timer 0.8 action Hide("flash_gold")

transform flash_effect:
    alpha 0.8
    ease 0.5 alpha 0.0

transform flash_effect_slow:
    alpha 0.6
    ease 0.8 alpha 0.0


################################################################################
## 3. 章节过场动画 (Chapter Title Card)
################################################################################

screen chapter_title(chapter_num="第一章", chapter_name="新主登基", chapter_desc=""):
    zorder 200
    modal True

    ## 全黑背景
    add Solid("#0a0812")

    ## 装饰粒子
    text "·" xpos 200 ypos 200 size 10 color "#d4a94220" at particle_float(200, 200, 6.0)
    text "·" xpos 900 ypos 400 size 8 color "#d4a94218" at particle_float(900, 400, 8.0)

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 8

        ## 上装饰线
        add Solid("#d4a94250") xsize 300 ysize 1 xalign 0.5 at fade_in_up(0.3)

        null height 12

        ## 章节编号
        text chapter_num:
            xalign 0.5
            size 22
            color "#8a7e60"
            font "msyh.ttf"
            at fade_in_up(0.5)

        ## 章节名
        text chapter_name:
            xalign 0.5
            size 52
            color "#d4a942"
            font "msyh.ttf"
            outlines [(3, "#000000cc", 0, 0), (6, "#d4a94220", 0, 0)]
            at fade_in_up(0.8)

        ## 章节描述
        if chapter_desc:
            null height 6
            text chapter_desc:
                xalign 0.5
                size 18
                color "#6a5e48"
                at fade_in_up(1.1)

        null height 12

        ## 下装饰线
        add Solid("#d4a94250") xsize 300 ysize 1 xalign 0.5 at fade_in_up(1.3)

    ## 底部提示
    text "点击继续":
        xalign 0.5
        yalign 0.95
        size 14
        color "#4a4030"
        at fade_in_up(2.0)

    ## 点击关闭
    timer 1.5 action SetVariable("_chapter_card_clickable", True)
    if _chapter_card_clickable:
        key "mouseup_1" action Hide("chapter_title")
        key "K_RETURN" action Hide("chapter_title")
        key "K_SPACE" action Hide("chapter_title")

default _chapter_card_clickable = False

## 便捷调用 label
label show_chapter(ch_num="第一章", ch_name="新主登基", ch_desc=""):
    $ _chapter_card_clickable = False
    show screen chapter_title(ch_num, ch_name, ch_desc)
    with dissolve
    pause
    hide screen chapter_title
    with dissolve
    return


################################################################################
## 4. 属性变化通知系统 (自动弹出)
################################################################################

init python:

    ## 属性中文名映射
    _stat_names = {
        "power": "权力", "wealth": "财富", "faith": "信仰",
        "loyalty": "忠诚", "reputation": "声望", "intrigue": "谋略",
    }

    _rel_names = {
        "rel_aldric": "奥尔德里克", "rel_elena": "艾琳娜",
        "rel_bishop": "主教马修斯", "rel_baron": "冯·哈根男爵",
        "rel_captain": "队长雷恩", "rel_queen": "伊莎贝拉王后",
        "rel_prince": "王子弗雷德里克", "rel_lily": "暗百合",
    }

    def change_stat(stat, delta):
        """改变属性并显示通知。用法: $ change_stat("power", 10)"""
        old = getattr(store, stat, 0)
        new = max(0, min(100, old + delta))
        setattr(store, stat, new)
        name = _stat_names.get(stat, stat)
        ## 记录属性历史（趋势箭头用）
        record_stat(stat, new)
        renpy.show_screen("stat_toast", stat_name=name, delta=delta, is_rel=False)
        check_max_stat()
        ## 属性预警检测
        warning = get_stat_warning(stat)
        if warning:
            renpy.show_screen("stat_warning_toast", warning_text=warning, is_danger=(new <= STAT_DANGER_LOW))
        ## 检查隐藏成就
        check_hidden_achievements()

    def change_rel(rel, delta):
        """改变好感度并显示通知。用法: $ change_rel("rel_elena", 15)"""
        old = getattr(store, rel, 0)
        new = max(-100, min(100, old + delta))
        setattr(store, rel, new)
        name = _rel_names.get(rel, rel)
        renpy.show_screen("stat_toast", stat_name=name, delta=delta, is_rel=True)
        ## 检查隐藏成就
        check_hidden_achievements()

## ── 属性变化弹幕 ──
screen stat_toast(stat_name="", delta=0, is_rel=False):
    zorder 250
    $ sign = "+" if delta > 0 else ""
    $ color = "#2ecc71" if delta > 0 else "#e74c3c"
    $ icon = "心" if is_rel else "*"

    frame at stat_toast_anim:
        xalign 0.5
        ypos 60
        background Solid("#0f0d1aee")
        xpadding 28
        ypadding 12

        hbox:
            spacing 10
            text icon size 18 color "#d4a942" yalign 0.5
            text stat_name size 17 color "#e0d8c8" font "msyh.ttf" yalign 0.5
            text "[sign][delta]" size 20 color color bold True yalign 0.5

    timer 2.0 action Hide("stat_toast")

transform stat_toast_anim:
    on show:
        alpha 0.0 yoffset -20
        ease 0.3 alpha 1.0 yoffset 0
    on hide:
        ease 0.3 alpha 0.0 yoffset -20


################################################################################
## 5. 抉择前自动存档提示
################################################################################

screen autosave_indicator():
    zorder 150
    frame:
        xalign 1.0
        yalign 0.0
        xoffset -10
        yoffset 10
        background Solid("#0f0d1acc")
        xpadding 16
        ypadding 8

        hbox:
            spacing 6
            text "【存】" size 14 yalign 0.5
            text "自动存档..." size 13 color "#8a7e60" yalign 0.5

    timer 2.0 action Hide("autosave_indicator")

## 在关键抉择前调用
label autosave_before_choice:
    $ renpy.force_autosave()
    show screen autosave_indicator
    pause 0.5
    return


################################################################################
## 6. 隐私政策弹窗 (首次启动必须同意)
################################################################################

default persistent.privacy_agreed = False

screen privacy_policy_screen():
    zorder 350
    modal True

    add Solid("#000000dd")

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 40
        ypadding 30
        xmaximum 700
        background Solid("#0f0d1af5")

        vbox:
            spacing 14
            xalign 0.5

            text "用户协议与隐私政策":
                size 26
                color "#d4a942"
                font "msyh.ttf"
                xalign 0.5
                outlines [(2, "#000000cc", 0, 0)]

            add Solid("#d4a94230") xsize 500 ysize 1 xalign 0.5

            null height 4

            viewport:
                xfill True
                ysize 340
                scrollbars "vertical"
                mousewheel True
                draggable True

                vbox:
                    spacing 10

                    text "{b}隐私政策{/b}" size 18 color "#e0d8c8" font "msyh.ttf"

                    text '欢迎使用《权谋之庭》（以下简称"本游戏"）。开发者FFire的工作室非常重视您的隐私保护。请在使用前仔细阅读以下内容：' size 14 color "#c0b8a8"

                    text "{b}1. 个人信息收集{/b}" size 15 color "#d4a942" font "msyh.ttf"
                    text "本游戏为纯单机游戏，{b}不会收集、上传或分享您的任何个人信息{/b}。游戏存档仅保存在您的本地设备上，不会传输至任何服务器。" size 14 color "#c0b8a8"

                    text "{b}2. 传感器使用{/b}" size 15 color "#d4a942" font "msyh.ttf"
                    text "本游戏基于RenPy引擎开发，引擎底层框架（SDL）会访问设备传感器（如加速度计、陀螺仪），仅用于检测屏幕方向以适配横竖屏显示。传感器数据仅在本地使用，不会被收集、存储或上传。" size 14 color "#c0b8a8"

                    text "{b}3. 第三方SDK说明{/b}" size 15 color "#d4a942" font "msyh.ttf"
                    text "本游戏使用以下引擎自带组件：" size 14 color "#c0b8a8"
                    text "- {b}视频播放组件{/b}（video_play_edit_sdk）：用于播放游戏内过场动画，可能访问传感器以适配显示方向。该组件不会收集或上传任何个人信息。" size 14 color "#c0b8a8"
                    text "本游戏未集成任何广告SDK、统计SDK、推送SDK或社交SDK。" size 14 color "#c0b8a8"

                    text "{b}4. 存储权限{/b}" size 15 color "#d4a942" font "msyh.ttf"
                    text "本游戏使用设备本地存储空间保存游戏进度（存档）和用户设置。存储权限仅用于读写游戏自身的存档文件，不会访问您设备上的其他文件（如照片、通讯录等）。" size 14 color "#c0b8a8"

                    text "{b}5. 网络访问{/b}" size 15 color "#d4a942" font "msyh.ttf"
                    text "本游戏不需要网络连接，不会访问互联网，不会与任何服务器通信。" size 14 color "#c0b8a8"

                    text "{b}6. 用户权利{/b}" size 15 color "#d4a942" font "msyh.ttf"
                    text "您可以随时通过卸载游戏来删除所有本地数据。如有疑问请联系开发者：2232517051@qq.com" size 14 color "#c0b8a8"

                    text "{b}7. 适龄提示{/b}" size 15 color "#d4a942" font "msyh.ttf"
                    text "本游戏适合12岁及以上用户。游戏包含中世纪宫廷题材的虚构剧情。" size 14 color "#c0b8a8"

                    null height 4
                    text "版本：2.1 | 更新日期：2026年3月 | 开发者：FFire的工作室" size 12 color "#6a5e48"

            null height 8
            add Solid("#d4a94230") xsize 500 ysize 1 xalign 0.5
            null height 4

            hbox:
                xalign 0.5
                spacing 40

                textbutton "不同意（退出）":
                    text_size 18
                    text_color "#8a7e60"
                    text_hover_color "#e74c3c"
                    text_font "msyh.ttf"
                    action Quit(confirm=False)

                textbutton "同意并继续":
                    text_size 20
                    text_color "#d4a942"
                    text_hover_color "#ffd866"
                    text_font "msyh.ttf"
                    text_outlines [(2, "#000000cc", 0, 0)]
                    action [SetField(persistent, "privacy_agreed", True), Hide("privacy_policy_screen"), Return()]


################################################################################
## 7. 新手引导 (首次游玩显示)
################################################################################

default persistent.tutorial_seen = False

screen tutorial_overlay():
    zorder 300
    modal True

    add Solid("#000000cc")

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 40
        xminimum 600
        background Solid("#0f0d1af5")

        vbox:
            spacing 16
            xalign 0.5

            ## 标题
            text "* 操作指南":
                size 30
                color "#d4a942"
                font "msyh.ttf"
                xalign 0.5
                outlines [(2, "#000000cc", 0, 0)]

            add Solid("#d4a94230") xsize 400 ysize 1 xalign 0.5

            null height 8

            ## 操作说明
            vbox:
                spacing 10

                hbox:
                    spacing 12
                    text "【鼠】" size 20 yalign 0.0
                    vbox:
                        text "点击屏幕 / 回车" size 18 color "#e0d8c8" font "msyh.ttf"
                        text "推进对话" size 14 color "#8a7e60"

                hbox:
                    spacing 12
                    text "【S】" size 20 yalign 0.0
                    vbox:
                        text "按 S 键" size 18 color "#e0d8c8" font "msyh.ttf"
                        text "查看领主状态（属性 & 人物关系）" size 14 color "#8a7e60"

                hbox:
                    spacing 12
                    text "【存】" size 20 yalign 0.0
                    vbox:
                        text "右键 / ESC" size 18 color "#e0d8c8" font "msyh.ttf"
                        text "打开游戏菜单（存档/读档/设置）" size 14 color "#8a7e60"

                hbox:
                    spacing 12
                    text "剑" size 20 yalign 0.0
                    vbox:
                        text "选择很重要！" size 18 color "#d4a942" font "msyh.ttf"
                        text "每个决定影响属性、好感度和故事走向" size 14 color "#8a7e60"

            null height 12

            ## 手机额外提示
            if renpy.variant("small") or renpy.variant("touch"):
                vbox:
                    spacing 6
                    add Solid("#d4a94220") xsize 400 ysize 1 xalign 0.5
                    null height 4
                    text "【触屏操作】" size 16 color "#d4a942" font "msyh.ttf" xalign 0.5
                    text "• 点击屏幕推进对话" size 13 color "#8a7e60" xalign 0.5
                    text "• 底部快捷栏：存档、状态、设置" size 13 color "#8a7e60" xalign 0.5
                    text "• 返回键打开菜单" size 13 color "#8a7e60" xalign 0.5
                null height 8

            add Solid("#d4a94230") xsize 400 ysize 1 xalign 0.5

            null height 8

            textbutton "开始冒险":
                xalign 0.5
                text_size 22
                text_color "#d4a942"
                text_hover_color "#ffd866"
                text_font "msyh.ttf"
                text_outlines [(2, "#000000cc", 0, 0)]
                action [SetField(persistent, "tutorial_seen", True), Hide("tutorial_overlay")]
                activate_sound "audio/sfx/ui_confirm.ogg"


################################################################################
## 7. TapTap 评分引导 (通关后)
################################################################################

default persistent.rating_asked = False

screen rating_popup():
    zorder 300
    modal True

    add Solid("#000000cc")

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 40
        xminimum 480
        background Solid("#0f0d1af5")

        vbox:
            spacing 14
            xalign 0.5

            text "* 感谢游玩！":
                size 28
                color "#d4a942"
                font "msyh.ttf"
                xalign 0.5

            add Solid("#d4a94230") xsize 300 ysize 1 xalign 0.5

            text "如果你喜欢《权谋之庭》":
                size 18
                color "#e0d8c8"
                xalign 0.5

            text "请在 TapTap 给我们一个好评":
                size 16
                color "#8a7e60"
                xalign 0.5

            text "你的支持是我们最大的动力！":
                size 16
                color "#8a7e60"
                xalign 0.5

            null height 10

            hbox:
                xalign 0.5
                spacing 20

                textbutton "去评分":
                    text_size 20
                    text_color "#d4a942"
                    text_hover_color "#ffd866"
                    text_font "msyh.ttf"
                    action [SetField(persistent, "rating_asked", True), Hide("rating_popup")]
                    activate_sound "audio/sfx/ui_confirm.ogg"

                textbutton "下次再说":
                    text_size 18
                    text_color "#6a5e48"
                    text_hover_color "#8a7e60"
                    action Hide("rating_popup")
                    activate_sound "audio/sfx/ui_cancel.ogg"


################################################################################
## 8. 成就解锁弹窗
################################################################################

screen achievement_popup(ach_name="", ach_desc=""):
    zorder 260

    frame at achievement_pop_anim:
        xalign 0.5
        ypos 100
        background Solid("#1a1528f0")
        xpadding 30
        ypadding 16

        hbox:
            spacing 14
            yalign 0.5

            ## 星星图标
            frame:
                xsize 44
                ysize 44
                background Solid("#d4a94225")
                text "*" xalign 0.5 yalign 0.5 size 24 color "#ffd700"

            vbox:
                spacing 2
                text "* 成就解锁" size 13 color "#d4a942"
                text ach_name size 20 color "#e0d8c8" font "msyh.ttf" bold True
                if ach_desc:
                    text ach_desc size 13 color "#8a7e60"

    timer 3.5 action Hide("achievement_popup")

transform achievement_pop_anim:
    on show:
        alpha 0.0 yoffset -30
        ease 0.4 alpha 1.0 yoffset 0
    on hide:
        ease 0.5 alpha 0.0 yoffset -30


################################################################################
## 9. CG 解锁辅助函数
################################################################################

init python:
    def unlock_gallery(img_name):
        """在剧情中展示CG时调用，解锁画廊。用法: $ unlock_gallery("bg_castle_exterior")"""
        if img_name not in persistent.gallery_unlocked:
            persistent.gallery_unlocked.add(img_name)


################################################################################
## 9. BGM 渐变播放辅助
################################################################################

init python:
    def play_bgm(track, fadein=2.0, fadeout=1.5):
        """播放BGM并自动crossfade。用法: $ play_bgm("audio/music/tension.ogg")"""
        renpy.music.play(track, channel="music", fadein=fadein, fadeout=fadeout)

    def stop_bgm(fadeout=2.0):
        """停止BGM。用法: $ stop_bgm()"""
        renpy.music.stop(channel="music", fadeout=fadeout)


################################################################################
## 10. 剧情回顾系统 (Previously on...)
################################################################################

init python:
    ## 每章结束后更新回顾文本
    _chapter_recaps = {
        "chapter1": (
            "第一章 · 新主登基",
            [
                "父亲突然离世，你从王都赶回艾登堡继承领主之位。",
                "老骑士奥尔德里克、卫队长雷恩、主教马修斯以及王后派来的艾琳娜——各怀心思的人围绕在你身边。",
                "一封来自'暗百合'的神秘密信暗示父亲的死另有隐情。",
                "冯·哈根男爵趁你立足未稳，在边境集结军队施压。",
                "你化解了第一次危机，颁布了第一道政令，开始了权力之路。",
            ]
        ),
        "chapter2": (
            "第二章 · 领主会议",
            [
                "你前往哈伦堡出席区域领主会议。",
                "冯·哈根男爵在会上发难，企图侵占你的铁矿。",
                "王后借机推行新税法，各方势力暗中角力。",
                "会议中一场突如其来的暗杀袭击，差点要了你的命。",
                "你在权谋的夹缝中艰难求存，积累了宝贵的政治经验。",
            ]
        ),
        "chapter3": (
            "第三章 · 暗百合",
            [
                "领地内出现神秘失踪事件，暗百合的符号频繁出现。",
                "你深入调查，发现暗百合是一个遍布王国的秘密组织。",
                "父亲生前与暗百合有着不为人知的联系。",
                "你面临抉择——加入暗百合还是将其捣毁。",
                "父亲死因的真相逐渐浮出水面。",
            ]
        ),
        "chapter4": (
            "第四章 · 王都风云",
            [
                "你踏上前往王都觐见王后的旅途。",
                "王宫中暗流涌动——王后、王子、贵族各有算计。",
                "你被卷入更大的政治漩涡，必须在各方势力间周旋。",
                "与艾琳娜的关系发生了微妙的变化。",
                "一场更大的风暴正在酝酿。",
            ]
        ),
    }

    def get_recap(chapter_id):
        return _chapter_recaps.get(chapter_id, None)

screen story_recap(chapter_id):
    zorder 200
    modal True

    add Solid("#0a0812ee")

    $ recap = get_recap(chapter_id)

    if recap:
        $ recap_title, recap_lines = recap

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 10
            xmaximum 700

            text "前情提要" size 16 color "#8a7e60" xalign 0.5 at fade_in_up(0.2)

            add Solid("#d4a94240") xsize 200 ysize 1 xalign 0.5 at fade_in_up(0.3)

            text recap_title:
                size 36 color "#d4a942" font "msyh.ttf" xalign 0.5
                outlines [(2, "#000000cc", 0, 0)]
                at fade_in_up(0.4)

            null height 8

            for idx, line in enumerate(recap_lines):
                hbox:
                    spacing 10
                    xalign 0.5
                    at fade_in_up(0.6 + idx * 0.2)

                    text "+" size 14 color "#d4a94280" yalign 0.0 yoffset 4
                    text line size 18 color "#c8b890" xmaximum 600

            null height 16

            add Solid("#d4a94240") xsize 200 ysize 1 xalign 0.5 at fade_in_up(1.8)

        text "点击继续":
            xalign 0.5 yalign 0.95 size 14 color "#4a4030"
            at fade_in_up(2.0)

        timer 1.0 action SetVariable("_recap_clickable", True)
        if _recap_clickable:
            key "mouseup_1" action Hide("story_recap")
            key "K_RETURN" action Hide("story_recap")
            key "K_SPACE" action Hide("story_recap")

default _recap_clickable = False

## 便捷调用
label show_recap(chapter_id="chapter1"):
    $ _recap_clickable = False
    show screen story_recap(chapter_id)
    with dissolve
    pause
    hide screen story_recap
    with dissolve
    return


################################################################################
## 11. 结局路线图
################################################################################

init python:
    _ending_info = {
        "iron_lord":    ("铁腕领主", "以铁与血铸就和平", "#c0392b", "剑"),
        "shadow_king":  ("影中之王", "在阴影中操控一切", "#2c3e50", "刃"),
        "holy_guardian": ("圣光守护", "以信仰之光驱散黑暗", "#f39c12", "十"),
        "peoples_lord": ("人民领主", "守护最平凡的幸福", "#27ae60", "心"),
        "truth":        ("真相大白", "正义也许会迟到", "#3498db", "秤"),
    }

    _ending_keys = ["iron_lord", "shadow_king", "holy_guardian", "peoples_lord", "truth"]

    _key_choices = [
        ("第一章", "第一个危机", ["外交", "军事", "教会", "间谍"]),
        ("第一章", "第一道政令", ["军事", "民生", "治安", "建设"]),
        ("第二章", "领主会议立场", ["支持王后", "反对王后", "折中方案"]),
        ("第三章", "暗百合", ["加入", "摧毁", "利用"]),
        ("第四章", "王都阵营", ["王后", "王子", "中立"]),
        ("第五章", "最终决战", ["铁腕", "暗影", "圣光", "人民", "真相"]),
    ]

screen ending_route_map():
    tag menu
    use game_menu(_("结局路线"), scroll="viewport"):
        vbox:
            spacing 16

            ## 标题
            hbox:
                spacing 8
                text "【图】" size 24 color "#d4a942" yalign 0.5
                text "结局路线图" size 26 color "#d4a942" font "msyh.ttf"

            $ seen = persistent.endings_seen if persistent.endings_seen else set()
            text "已解锁 [len(seen)]/5 个结局" size 14 color "#6a5e48"

            null height 10

            ## 结局卡片
            for eid in _ending_keys:
                $ e_name, e_desc, e_color, e_icon = _ending_info[eid]
                $ is_seen = eid in seen

                frame:
                    xfill True
                    xpadding 20
                    ypadding 16
                    background Solid("#1a152840" if is_seen else "#0f0d1a40")

                    hbox:
                        spacing 16
                        yalign 0.5

                        ## 图标
                        frame:
                            xsize 52
                            ysize 52
                            background Solid(e_color + "30" if is_seen else "#1a1528")

                            if is_seen:
                                text e_icon xalign 0.5 yalign 0.5 size 24
                            else:
                                text "?" xalign 0.5 yalign 0.5 size 24 color "#2a2040"

                        vbox:
                            spacing 3
                            if is_seen:
                                text e_name size 20 color "#e0d8c8" font "msyh.ttf" bold True
                                text e_desc size 14 color "#8a7e60"
                            else:
                                text "??? — 锁 未解锁" size 20 color "#3a3040" font "msyh.ttf"
                                text "完成游戏解锁此结局" size 14 color "#2a2030"

                        if is_seen:
                            text ">" xalign 1.0 yalign 0.5 size 20 color e_color

            null height 16
            add Solid("#d4a94220") xsize 1.0 ysize 1
            null height 10

            ## 关键分支点提示 (只在至少通关1次后显示)
            if len(seen) > 0:
                hbox:
                    spacing 8
                    text "+" size 20 color "#d4a942" yalign 0.5
                    text "关键分支点" size 22 color "#d4a942" font "msyh.ttf"

                null height 6

                for ch_name, choice_name, options in _key_choices:
                    frame:
                        xfill True
                        xpadding 16
                        ypadding 10
                        background Solid("#1a152820")

                        hbox:
                            spacing 12
                            text ch_name size 13 color "#d4a942" yalign 0.5 xminimum 60
                            text choice_name size 16 color "#c8b890" font "msyh.ttf" yalign 0.5
                            text "->" size 14 color "#6a5e48" yalign 0.5
                            text " / ".join(options) size 13 color "#6a5e48" yalign 0.5

            null height 16

            ## 提示
            frame:
                xalign 0.5
                xpadding 24
                ypadding 12
                background Solid("#1a152840")
                text "【提示】 不同的选择组合将导向不同的结局" size 14 color "#8a7e60" font "msyh.ttf"


################################################################################
## 12. 属性预警弹窗
################################################################################

screen stat_warning_toast(warning_text="", is_danger=True):
    zorder 255
    $ w_color = "#e74c3c" if is_danger else "#f39c12"
    $ w_icon = "!" if is_danger else "!"

    frame at stat_warning_anim:
        xalign 0.5
        ypos 110
        background Solid("#1a0a0aee" if is_danger else "#1a1510ee")
        xpadding 24
        ypadding 10

        hbox:
            spacing 8
            text w_icon size 18 color w_color yalign 0.5
            text warning_text size 15 color w_color font "msyh.ttf" yalign 0.5

    timer 3.5 action Hide("stat_warning_toast")

transform stat_warning_anim:
    on show:
        alpha 0.0 yoffset -15
        ease 0.3 alpha 1.0 yoffset 0
    on hide:
        ease 0.4 alpha 0.0 yoffset -15


################################################################################
## 13. 动态BGM系统 — 根据剧情紧张度切换配乐
################################################################################

init python:
    ## 紧张度等级: calm, normal, tense, battle, mystery
    _bgm_layers = {
        "calm":    "audio/music/castle_calm.ogg",
        "normal":  "audio/music/great_hall.ogg",
        "tense":   "audio/music/tension.ogg",
        "battle":  "audio/music/battle_prepare.ogg",
        "mystery": "audio/music/night_mystery.ogg",
        "victory": "audio/music/victory.ogg",
        "sad":     "audio/music/sad.ogg",
    }

    _current_mood = "normal"

    def set_mood(mood, fadein=2.0, fadeout=1.5):
        """根据紧张度自动切换BGM。用法: $ set_mood("tense")"""
        global _current_mood
        if mood == _current_mood:
            return
        _current_mood = mood
        track = _bgm_layers.get(mood)
        if track and renpy.loadable(track):
            renpy.music.play(track, channel="music", fadein=fadein, fadeout=fadeout, if_changed=True)

    def get_mood():
        return _current_mood

    def auto_mood():
        """根据当前属性自动判断紧张度"""
        ## 任一核心属性极低 -> 紧张
        danger_stats = [store.power, store.wealth, store.loyalty]
        if any(s <= 15 for s in danger_stats):
            set_mood("tense")
            return
        ## 关系全部友好 -> 平静
        rels = [store.rel_aldric, store.rel_elena, store.rel_captain]
        if all(r >= 40 for r in rels):
            set_mood("calm")
            return
        set_mood("normal")


################################################################################
## 14. 通关后多结局提示系统
################################################################################

screen ending_complete_hint(current_ending=""):
    zorder 280
    modal True

    add Solid("#000000dd")

    $ seen = persistent.endings_seen if persistent.endings_seen else set()
    $ total = 5
    $ remaining = total - len(seen)

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 40
        xminimum 550
        background Solid("#0f0d1af5")

        vbox:
            spacing 14
            xalign 0.5

            ## 当前结局
            text "* 恭喜通关！" size 30 color "#d4a942" font "msyh.ttf" xalign 0.5 outlines [(2, "#000000cc", 0, 0)]

            add Solid("#d4a94230") xsize 400 ysize 1 xalign 0.5

            if current_ending and current_ending in _ending_info:
                $ e_name, e_desc, e_color, e_icon = _ending_info[current_ending]
                hbox:
                    xalign 0.5
                    spacing 10
                    text e_icon size 28 yalign 0.5
                    vbox:
                        text e_name size 24 color e_color font "msyh.ttf" bold True
                        text e_desc size 15 color "#8a7e60"

            null height 8

            ## 结局收集进度
            hbox:
                xalign 0.5
                spacing 6
                text "结局收集:" size 16 color "#c8b890" font "msyh.ttf"
                text "[len(seen)]/[total]" size 18 color "#d4a942" bold True

            ## 进度条
            bar:
                value StaticValue(len(seen), total)
                xmaximum 350
                ysize 8
                left_bar Solid("#d4a942")
                right_bar Solid("#1a1528")
                xalign 0.5

            null height 6

            ## 未解锁结局提示
            if remaining > 0:
                frame:
                    xalign 0.5
                    xpadding 20
                    ypadding 12
                    background Solid("#1a152860")

                    vbox:
                        spacing 6
                        text "还有 [remaining] 个结局等待发现：" size 15 color "#c8b890" font "msyh.ttf"

                        for eid in _ending_keys:
                            if eid not in seen:
                                $ ei = _ending_info[eid]
                                hbox:
                                    spacing 8
                                    text "•" size 14 color "#6a5e48"
                                    text "???" size 14 color "#4a4040"
                                    text "— 尝试不同的选择路线" size 13 color "#3a3030"
            else:
                text "* 恭喜！你已解锁全部结局！" size 18 color "#ffd700" font "msyh.ttf" xalign 0.5

            null height 12

            hbox:
                xalign 0.5
                spacing 20

                textbutton "查看路线图":
                    text_size 18
                    text_color "#d4a942"
                    text_hover_color "#ffd866"
                    text_font "msyh.ttf"
                    action [Hide("ending_complete_hint"), ShowMenu("ending_route_map")]
                    activate_sound "audio/sfx/ui_confirm.ogg"

                textbutton "返回主菜单":
                    text_size 18
                    text_color "#8a7e60"
                    text_hover_color "#c8b890"
                    text_font "msyh.ttf"
                    action [Hide("ending_complete_hint"), MainMenu()]
                    activate_sound "audio/sfx/ui_click.ogg"

                if remaining > 0:
                    textbutton "再玩一次":
                        text_size 18
                        text_color "#2ecc71"
                        text_hover_color "#44e88a"
                        text_font "msyh.ttf"
                        action [Hide("ending_complete_hint"), Start()]
                        activate_sound "audio/sfx/ui_confirm.ogg"


################################################################################
## 15. 淡入上浮 Transform（供各 screen 使用）
################################################################################

## fade_in_up 已在前面定义，此处补充更多实用动画

## ── 从左滑入 ──
transform slide_in_left(delay=0.0):
    alpha 0.0 xoffset -40
    pause delay
    ease 0.4 alpha 1.0 xoffset 0

## ── 脉冲高亮 ──
transform pulse_glow:
    block:
        ease 0.8 alpha 0.6
        ease 0.8 alpha 1.0
        repeat

################################################################################
## 权谋之庭 — 大厂级UI · screens.rpy
################################################################################

init offset = -1

################################################################################
## 自定义 Transform 和工具
################################################################################

transform menu_btn_hover:
    on hover:
        ease 0.15 xoffset 8
    on idle:
        ease 0.15 xoffset 0

transform title_breathe:
    alpha 0.85
    block:
        ease 2.5 alpha 1.0
        ease 2.5 alpha 0.85
        repeat

transform title_glow:
    alpha 0.0
    block:
        ease 3.0 alpha 0.4
        ease 3.0 alpha 0.0
        repeat

transform choice_appear(delay=0):
    alpha 0.0 xoffset -30
    pause delay
    ease 0.4 alpha 1.0 xoffset 0

transform choice_hover:
    on hover:
        ease 0.12 zoom 1.02
    on idle:
        ease 0.12 zoom 1.0

transform fade_in_up(delay=0.0):
    alpha 0.0 yoffset 20
    pause delay
    ease 0.4 alpha 1.0 yoffset 0

transform slot_hover:
    on hover:
        ease 0.15 zoom 1.03
    on idle:
        ease 0.15 zoom 1.0

transform slow_pan:
    xalign 0.4
    block:
        ease 30.0 xalign 0.6
        ease 30.0 xalign 0.4
        repeat

transform overlay_fade:
    alpha 0.0
    ease 0.5 alpha 1.0

transform particle_float(xstart, ystart, dur):
    pos (xstart, ystart)
    alpha 0.0
    ease 1.0 alpha 0.6
    block:
        ease dur yoffset -200 alpha 0.0
        yoffset 0 alpha 0.0
        ease 1.0 alpha 0.6
        repeat


################################################################################
## 基本样式
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")

style button:
    properties gui.button_properties("button")
    hover_sound "audio/sfx/ui_hover.ogg"

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5

style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Solid("#1a1420")
    thumb Solid("#d4a94280")
    hover_thumb Solid("#d4a942cc")
    unscrollable "hide"

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Solid("#1a1420")
    thumb Solid("#d4a94260")
    hover_thumb Solid("#d4a942cc")
    unscrollable "hide"

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"

style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)


################################################################################
## 对话界面 (Say Screen)
################################################################################

screen say(who, what):

    $ _say_window_height = int(gui.textbox_height * preferences.font_size) if renpy.variant("small") and preferences.font_size > 1.0 else gui.textbox_height

    window:
        id "window"
        if renpy.variant("small") and preferences.font_size > 1.0:
            ysize _say_window_height
            background Transform("gui/textbox.png", xalign=0.5, yalign=1.0, ysize=_say_window_height)

        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    ## 对话肖像已禁用 — 使用大立绘 (show xxx_img) 代替
    # add SideImage() xpos 110 yalign 1.0


init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height
    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5
    outlines [(2, "#00000080", 0, 0)]

style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    adjust_spacing False
    outlines [(1, "#00000060", 0, 0)]
    line_spacing 6


################################################################################
## 输入界面
################################################################################

screen input(prompt):
    style_prefix "input"

    window:
        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


################################################################################
## 选项界面 (Choice Screen) — 大厂级设计
################################################################################

screen choice(items):
    style_prefix "choice"

    ## 防误触计时器：选项出现后短暂延迟才可点击
    default choice_ready = False
    timer 0.6 action SetScreenVariable("choice_ready", True)

    fixed:
        ## 重要抉择模式：特殊视觉效果
        if getattr(store, "important_choice", False):
            add Solid("#0a0812cc")
            ## 顶部提示
            vbox:
                xalign 0.5
                yalign 0.12
                spacing 6
                add Solid("#d4a94260") xsize 160 ysize 1 xalign 0.5
                text "— 重要抉择 —" size 22 color "#d4a942" xalign 0.5 outlines [(2, "#000000cc", 0, 0)]
                text "请谨慎选择，此决定将影响后续剧情走向" size 14 color "#8a7e60" xalign 0.5
                add Solid("#d4a94260") xsize 160 ysize 1 xalign 0.5
        else:
            add Solid("#0a081288")

        if renpy.variant("small"):
            side "c r":
                style "choice_side"
                if getattr(store, "important_choice", False):
                    ypos 160
                    ysize 440
                else:
                    ypos 35
                    ysize 565

                viewport:
                    id "choice_scroll"
                    style "choice_viewport"
                    draggable True
                    mousewheel True
                    pagekeys True

                    use choice_items(items, choice_ready)

                vbar:
                    style "choice_vscrollbar"
                    value YScrollValue("choice_scroll")
        else:
            use choice_items(items, choice_ready)

    ## 重要抉择结束后自动重置标记
    if getattr(store, "important_choice", False):
        timer 0.1 action SetVariable("important_choice", False)


screen choice_items(items, choice_ready):
    style_prefix "choice"

    vbox:
        xalign 0.5
        if not renpy.variant("small"):
            yalign 0.45
        yfit True
        spacing 8

        for idx, i in enumerate(items):
            ## 解析选项文本和提示：用 "|" 分隔，如 "选择王室|权力+10 声望-5"
            ## 先做变量替换再拆分——menu 语句的 caption 传到这里时 [var] 尚未展开,
            ## 软检定提示(soft_hint 返回 "|xx不足…")靠替换后才出现的 "|" 挂载副行。
            ## 下方 text 均已 substitute False, 不会二次替换。
            $ _parts = renpy.substitute(i.caption).split("|", 1)
            $ _caption = _parts[0]
            $ _hint = _parts[1] if len(_parts) > 1 else ""

            button:
                if choice_ready:
                    action i.action
                else:
                    action NullAction()
                at choice_appear(idx * 0.1), choice_hover
                xsize gui.choice_button_width
                yalign 0.5
                xalign 0.5

                if not choice_ready:
                    background Solid("#1a152866")
                elif getattr(store, "important_choice", False):
                    background Solid("#1a1528cc")
                    hover_background Solid("#2a2040ee")
                else:
                    background Solid("#1a1528bb")
                    hover_background Solid("#2a2040dd")

                frame:
                    xfill True
                    xpadding 24
                    ypadding 14
                    background None

                    vbox:
                        spacing 4
                        hbox:
                            xfill True
                            ## 选项序号
                            text str(idx + 1) + "." size 20 color "#d4a942" yalign 0.0 xsize 30 outlines [(1, "#000000", 0, 0)]

                            text _caption:
                                style "choice_button_text"
                                yalign 0.0
                                xfill True
                                substitute False

                        ## 后果提示
                        if _hint:
                            hbox:
                                xoffset 30
                                spacing 8
                                for _h in _hint.split():
                                    if "+" in _h:
                                        text _h style "choice_hint_text" color "#2ecc71" substitute False
                                    elif "-" in _h:
                                        text _h style "choice_hint_text" color "#e74c3c" substitute False
                                    else:
                                        text _h style "choice_hint_text" color "#8a7e60" substitute False


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text
style choice_hint_text is default
style choice_side is side
style choice_viewport is viewport
style choice_vscrollbar is vscrollbar

style choice_vbox:
    xalign 0.5
    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")
    outlines [(2, "#000000", 0, 0), (1, "#000000", 1, 1)]

style choice_hint_text:
    size (gui.interface_text_size * 3 // 5)

style choice_side:
    xalign 0.5
    xsize gui.choice_button_width + gui.scrollbar_size + 18
    spacing 18

style choice_viewport:
    xsize gui.choice_button_width
    yfill True

style choice_vscrollbar:
    xsize gui.scrollbar_size
    yfill True
    base_bar Solid("#3a3040dd")
    thumb Solid("#d4a942")
    hover_thumb Solid("#ffe082")
    unscrollable "show"


################################################################################
## 快捷菜单 (Quick Menu) — 精简底栏
################################################################################

screen quick_menu():
    zorder 100

    if quick_menu:
        hbox:
            style_prefix "quick"
            style "quick_menu"

            if not renpy.variant("small"):
                ## PC/平板: 完整快捷栏
                textbutton _("回退") action Rollback()
                textbutton _("历史") action ShowMenu('history')
                textbutton _("快进") action Skip() alternate SkipToChoice()
                textbutton _("跳抉择") action SkipToChoice()
                textbutton _("自动") action Preference("auto-forward", "toggle")
                textbutton _("存档") action ShowMenu('save')
                textbutton _("读档") action ShowMenu('load')
                textbutton _("快存") action QuickSave()
                textbutton _("快读") action QuickLoad()
                textbutton _("状态") action Show("stats_screen")
                textbutton _("设置") action ShowMenu('preferences')
            else:
                ## 手机: 精简快捷栏
                textbutton _("历史") action ShowMenu('history')
                textbutton _("存档") action ShowMenu('save')
                textbutton _("读档") action ShowMenu('load')
                textbutton _("快存") action QuickSave()
                textbutton _("快读") action QuickLoad()
                textbutton _("快进") action Skip() alternate SkipToChoice()
                textbutton _("跳抉择") action SkipToChoice()
                textbutton _("状态") action Show("stats_screen")
                textbutton _("设置") action ShowMenu('preferences')


init python:
    config.overlay_screens.append("quick_menu")
    quick_menu = True

style quick_menu is hbox
style quick_button is default
style quick_button_text is button_text

style quick_menu:
    xalign 0.5
    yalign 1.0

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")
    outlines [(1, "#000000", 0, 0)]


################################################################################
## 主菜单导航 (Navigation)
################################################################################

screen navigation():

    vbox:
        xpos gui.navigation_xpos
        yalign 0.5
        style_prefix "navigation"
        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("开始游戏"):
                at menu_btn_hover
                action Start()
                text_size 26
                text_font "msyh.ttf"

            textbutton _("章节选择"):
                at menu_btn_hover
                action ShowMenu("chapter_select")

            textbutton _("读取存档"):
                at menu_btn_hover
                action ShowMenu("load")

            textbutton _("鉴赏模式"):
                at menu_btn_hover
                action ShowMenu("gallery_hub")

            ## 南境游记的入口已并入「章节选择」(gallery.rpy chapter_list 的「外章」),
            ## 与「序章」并列 —— 它是主线目录的一部分, 不再是主菜单上单开的一栏。
            ## 北境游记(开发中)的入口一并移除: 它本来就锁在 config.developer 后面、无 else 分支,
            ## 正式版玩家从来看不见, 删掉零可见变化; 开发者仍可 shift+O 控制台 jump northern_dlc_start。

            textbutton _("宣传PV"):
                at menu_btn_hover
                action Start("pv_play")

            textbutton _("玩家社群"):
                at menu_btn_hover
                # QQ 群 145409117 加群链接 (复用铁与誓项目的 universal-share)
                action OpenURL("https://qun.qq.com/universal-share/share?ac=1&authKey=OHMV3Hb2Lo1QFclWKOLr%2B8iwQfwXeyu74Ib2wLlkElIIve%2FY7vqnxVEQJtkWq%2Fov&busi_data=eyJncm91cENvZGUiOiIxNDU0MDkxMTciLCJ0b2tlbiI6IkhFQlI3K1pKenIrUlR3OXoxaE94Wk5kZGxqOG5DNDdBMk4rYkpHZGFKUnUxOVdyVXRGVzdicWI4bHJjbWJDaEYiLCJ1aW4iOiIyMjMyNTE3MDUxIn0%3D&data=oeKNIpKew9u2T1pruU_KahpzwxzCgqoz7kYH8Haj3FdxKz5PggWGTKQoaxnmODFhG-RwIv5II5asQ-ykqQKyDA&svctype=4&tempid=h5_group_info")
                text_size 26
                text_font "msyh.ttf"

            textbutton _("游戏设置"):
                at menu_btn_hover
                action ShowMenu("preferences")

            if renpy.variant("pc"):
                textbutton _("退出游戏"):
                    at menu_btn_hover
                    action Quit(confirm=False)

        else:

            textbutton _("历史"):
                at menu_btn_hover
                action ShowMenu("history")

            textbutton _("保存游戏"):
                at menu_btn_hover
                action ShowMenu("save")

            textbutton _("读取存档"):
                at menu_btn_hover
                action ShowMenu("load")

            textbutton _("领主状态"):
                at menu_btn_hover
                action Show("stats_screen")

            textbutton _("决策日志"):
                at menu_btn_hover
                action ShowMenu("decision_journal")

            textbutton _("游戏设置"):
                at menu_btn_hover
                action ShowMenu("preferences")

            if _in_replay:
                textbutton _("结束回放"):
                    at menu_btn_hover
                    action EndReplay(confirm=True)

            else:
                textbutton _("返回主菜单"):
                    at menu_btn_hover
                    action MainMenu()


## ════════════════════════════════════════════════════════════════
## 鉴赏模式 — 汇总画廊/音乐/成就/图鉴等入口
## ════════════════════════════════════════════════════════════════

screen gallery_hub():

    tag menu

    use game_menu(_("鉴赏模式"), scroll="viewport"):

        style_prefix "gallery_hub"

        vbox:
            spacing 12

            text "收藏与鉴赏" size 22 color "#d4a942" font "msyh.ttf" bold True
            add Solid("#d4a94240") xsize 300 ysize 1
            null height 4

            textbutton _("画廊"):
                text_size 18 text_color "#e0d8c8" text_hover_color "#d4a942"
                action ShowMenu("cg_gallery")

            textbutton _("音乐鉴赏"):
                text_size 18 text_color "#e0d8c8" text_hover_color "#d4a942"
                action ShowMenu("music_room")

            textbutton _("成就"):
                text_size 18 text_color "#e0d8c8" text_hover_color "#d4a942"
                action ShowMenu("achievement_screen")

            textbutton _("结局路线"):
                text_size 18 text_color "#e0d8c8" text_hover_color "#d4a942"
                action ShowMenu("ending_route_map")

            textbutton _("角色图鉴"):
                text_size 18 text_color "#e0d8c8" text_hover_color "#d4a942"
                action ShowMenu("character_codex")

            textbutton _("收藏品"):
                text_size 18 text_color "#e0d8c8" text_hover_color "#d4a942"
                action ShowMenu("collectibles_screen")

            textbutton _("地图"):
                text_size 18 text_color "#e0d8c8" text_hover_color "#d4a942"
                action ShowMenu("world_map")

            null height 8
            add Solid("#d4a94220") xsize 300 ysize 1
            null height 4

            text "更多" size 18 color "#8a7e60" font "msyh.ttf"
            null height 2

            textbutton _("辅助功能"):
                text_size 16 text_color "#8a7e60" text_hover_color "#d4a942"
                action ShowMenu("accessibility_settings")

            textbutton _("关于游戏"):
                text_size 16 text_color "#8a7e60" text_hover_color "#d4a942"
                action ShowMenu("about")

            if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
                textbutton _("帮助"):
                    text_size 16 text_color "#8a7e60" text_hover_color "#d4a942"
                    action ShowMenu("help")


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    left_padding 4

style navigation_button_text:
    properties gui.text_properties("navigation_button")
    outlines [(2, "#000000cc", 0, 0)]
    hover_outlines [(2, "#00000080", 0, 0)]


################################################################################
## 主菜单 (Main Menu) — 电影级设计
################################################################################

screen main_menu():
    tag menu

    ## 背景 + 慢速平移
    add gui.main_menu_background at slow_pan

    ## 暗角 vignette 效果
    add Solid("#00000000"):
        xsize 1280
        ysize 720

    ## 左侧暗色渐变面板
    frame:
        style "main_menu_frame"

    ## 装饰性粒子
    text "·" at particle_float(200, 300, 8.0):
        size 12 color "#d4a94230"
    text "·" at particle_float(120, 500, 10.0):
        size 8 color "#d4a94220"
    text "·" at particle_float(250, 200, 12.0):
        size 10 color "#d4a94228"

    ## 标题区域
    vbox:
        xalign 0.98
        yalign 0.92
        spacing 4

        ## 主标题(资源体检: 系统字排版换定制暗金 logo, PIL 产 game/images/logo.png)
        add Transform("images/logo.png", size=(420, 140), fit="contain"):
            xalign 1.0
            at title_breathe

        null height 4

        text "[config.version]":
            style "main_menu_version"
            xalign 1.0

    ## AI 合成内容标识
    frame:
        xalign 0.0 yalign 1.0
        xoffset 20 yoffset -15
        background Solid("#0a0812cc")
        xpadding 10 ypadding 6
        text "本游戏部分美术素材由 AI 辅助生成" size 12 color "#8a7e60"

    ## 导航按钮
    use navigation


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 320
    yfill True
    background Solid("#0a081290")

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")
    color "#6a5e48"


################################################################################
## 游戏菜单框架 (Game Menu)
################################################################################

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":
                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True

                        vbox:
                            spacing spacing
                            transclude

                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        spacing spacing
                        transclude

                else:
                    transclude

    use navigation

    textbutton _("« 返回"):
        style "return_button"
        action Return()
        text_outlines [(2, "#000000cc", 0, 0)]

    ## 标题标签 + 装饰
    vbox:
        xpos 340
        ypos 30
        spacing 4

        label title:
            text_outlines [(2, "#000000aa", 0, 0)]

        add Solid("#d4a94240") xsize 120 ysize 2

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120
    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 320
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 900

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    size 36
    color gui.accent_color
    yalign 0.5
    outlines [(2, "#000000aa", 0, 0)]

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30


################################################################################
## 关于界面
################################################################################

screen about():
    tag menu

    use game_menu(_("关于游戏"), scroll="viewport"):
        style_prefix "about"

        vbox:
            spacing 10

            label "[config.name!t]"
            text _("版本 [config.version!t]\n")

            if gui.about:
                text "[gui.about!t]\n"

            text _("使用 {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only] 制作。\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


################################################################################
## 存档/读档界面 — 精致卡片设计
################################################################################

screen save():
    tag menu
    use file_slots(_("保存游戏"))

screen load():
    tag menu
    use file_slots(_("读取存档"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("第 {} 页"), auto=_("自动存档"), quick=_("快速存档"))

    use game_menu(title, scroll="viewport"):

        vbox:
            xfill True
            spacing 10

            ## 页面标签
            button:
                style "page_label"
                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## 存档槽位网格（可滚动）
            vpgrid:
                style_prefix "slot"
                cols gui.file_slot_cols
                xalign 0.5
                spacing gui.slot_spacing
                mousewheel True
                draggable True

                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1

                    button:
                        action FileAction(slot)
                        at slot_hover

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%Y年%m月%d日 %H:%M"), empty=_("— 空存档位 —")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## 页面导航
            vbox:
                style_prefix "page"
                xalign 0.5

                hbox:
                    xalign 0.5
                    spacing gui.page_spacing

                    textbutton _("«") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _("»") action FilePageNext()
                    key "save_page_next" action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("上传同步"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("下载同步"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 5
    xalign 0.5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


################################################################################
## 游戏设置界面
################################################################################

screen preferences():
    tag menu

    use game_menu(_("游戏设置"), scroll="viewport"):
        vbox:
            spacing 4

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):
                    vbox:
                        style_prefix "radio"
                        label _("显示")
                        textbutton _("窗口") action Preference("display", "window")
                        textbutton _("全屏") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("快进")
                    textbutton _("未读文本") action Preference("skip", "toggle")
                    textbutton _("选项后") action Preference("after choices", "toggle")
                    textbutton _("转场效果") action InvertSelected(Preference("transitions", "toggle"))

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:
                    label _("文字速度")
                    bar value Preference("text speed")

                    label _("自动前进时间")
                    bar value Preference("auto-forward time")

                vbox:
                    if config.has_music:
                        label _("音乐音量")
                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:
                        label _("音效音量")
                        hbox:
                            bar value Preference("sound volume")
                            if config.sample_sound:
                                textbutton _("测试") action Play("sound", config.sample_sound)

                    if config.has_voice:
                        label _("语音音量")
                        hbox:
                            bar value Preference("voice volume")
                            if config.sample_voice:
                                textbutton _("测试") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing
                        textbutton _("全部静音"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

            null height gui.pref_spacing
            textbutton _("辅助功能设置"):
                id "accessibility_entry"
                action ShowMenu("accessibility_settings")
                style "check_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 240

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 360

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 460


################################################################################
## 历史界面
################################################################################

screen history():
    tag menu

    predict False

    use game_menu(_("历史"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:
                has fixed:
                    yfit True

                if h.who:
                    label h.who:
                        style "history_name"
                        substitute False
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("对话历史为空。")


define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty
style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text
style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


################################################################################
## 帮助界面
################################################################################

screen help():
    tag menu
    default device = "keyboard"

    use game_menu(_("帮助"), scroll="viewport"):
        style_prefix "help"

        vbox:
            spacing 15

            hbox:
                textbutton _("键盘") action SetScreenVariable("device", "keyboard")
                textbutton _("鼠标") action SetScreenVariable("device", "mouse")
                if GamepadExists():
                    textbutton _("手柄") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():
    hbox:
        label _("回车")
        text _("推进对话并激活界面。")
    hbox:
        label _("空格")
        text _("推进对话但不选择选项。")
    hbox:
        label _("方向键")
        text _("导航界面。")
    hbox:
        label _("Escape")
        text _("打开游戏菜单。")
    hbox:
        label _("Ctrl")
        text _("按住时快进对话。")
    hbox:
        label _("Tab")
        text _("切换对话快进。")
    hbox:
        label _("Page Up")
        text _("回退到之前的对话。")
    hbox:
        label _("Page Down")
        text _("前进到之后的对话。")
    hbox:
        label "H"
        text _("隐藏用户界面。")
    hbox:
        label "S"
        text _("打开状态面板。")
    hbox:
        label "V"
        text _("切换辅助{a=https://www.renpy.org/l/voicing}自动朗读{/a}。")
    hbox:
        label "Shift+A"
        text _("打开无障碍菜单。")


screen mouse_help():
    hbox:
        label _("左键点击")
        text _("推进对话并激活界面。")
    hbox:
        label _("中键点击")
        text _("隐藏用户界面。")
    hbox:
        label _("右键点击")
        text _("打开游戏菜单。")
    hbox:
        label _("鼠标滚轮上")
        text _("回退到之前的对话。")
    hbox:
        label _("鼠标滚轮下")
        text _("前进到之后的对话。")


screen gamepad_help():
    hbox:
        label _("右扳机\nA/下方按钮")
        text _("推进对话并激活界面。")
    hbox:
        label _("左扳机\n左肩键")
        text _("回退到之前的对话。")
    hbox:
        label _("右肩键")
        text _("前进到之后的对话。")
    hbox:
        label _("十字键、摇杆")
        text _("导航界面。")
    hbox:
        label _("Start、Guide、B/右方按钮")
        text _("打开游戏菜单。")
    hbox:
        label _("Y/上方按钮")
        text _("隐藏用户界面。")
    textbutton _("校准") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 260
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0


################################################################################
## 确认对话框 — 电影级模态
################################################################################

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    style_prefix "confirm"

    add Solid("#000000bb")

    frame:
        at overlay_fade

        vbox:
            xalign .5
            yalign .5
            spacing 30

            ## 装饰线
            add Solid("#d4a94260") xsize 200 ysize 1 xalign 0.5

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            add Solid("#d4a94260") xsize 200 ysize 1 xalign 0.5

            null height 10

            hbox:
                xalign 0.5
                spacing 60

                textbutton _("确认"):
                    action yes_action
                    text_size 22
                    text_color "#d4a942"
                    text_hover_color "#ffd866"
                    text_outlines [(2, "#000000cc", 0, 0)]

                textbutton _("取消"):
                    action no_action
                    text_size 22
                    text_color "#8a7e60"
                    text_hover_color "#c8b890"
                    text_outlines [(2, "#000000cc", 0, 0)]

    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Solid("#12101aee")
    xalign 0.5
    yalign 0.5
    xpadding 80
    ypadding 60
    xminimum 500

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"
    color "#e0d8c8"
    outlines [(2, "#000000aa", 0, 0)]
    size 24


################################################################################
## 更新检查弹窗（好游快爆）
################################################################################

screen update_notice(new_ver="3.1", update_url="https://www.3839.com/a/"):
    modal True
    zorder 200
    style_prefix "confirm"

    add Solid("#000000bb")

    frame:
        at overlay_fade

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20

            add Solid("#d4a94260") xsize 200 ysize 1 xalign 0.5

            text "发现新版本" size 28 color "#d4a942" xalign 0.5 outlines [(2, "#000000cc", 0, 0)]

            null height 5

            text "当前版本：v[config.version]" size 18 color "#8a7e60" xalign 0.5
            text "最新版本：v[new_ver]" size 18 color "#c9a84c" xalign 0.5

            null height 5

            text "建议前往好游快爆下载最新版本\n获取更多内容和修复" size 16 color "#6a5e48" xalign 0.5 text_align 0.5

            add Solid("#d4a94260") xsize 200 ysize 1 xalign 0.5

            null height 10

            hbox:
                xalign 0.5
                spacing 60

                textbutton "立即更新":
                    action OpenURL(update_url)
                    text_size 22
                    text_color "#d4a942"
                    text_hover_color "#ffd866"
                    text_outlines [(2, "#000000cc", 0, 0)]

                textbutton "稍后再说":
                    action Hide("update_notice")
                    text_size 22
                    text_color "#8a7e60"
                    text_hover_color "#c8b890"
                    text_outlines [(2, "#000000cc", 0, 0)]


################################################################################
## 跳过提示
################################################################################

transform delayed_blink(delay, cycle):
    alpha .5
    pause delay
    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .6)
        repeat

screen skip_indicator():
    zorder 100
    style_prefix "skip"

    frame:
        hbox:
            spacing 6
            text _("快进中")
            $ _sk = ui_icon("ctl_skip_arrow", 22)
            if _sk:
                add _sk at delayed_blink(0.0, 1.0) yalign 0.5
            else:
                text ">" at delayed_blink(0.0, 1.0) style "skip_triangle"
                text ">" at delayed_blink(0.2, 1.0) style "skip_triangle"
                text ">" at delayed_blink(0.4, 1.0) style "skip_triangle"


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    font "DejaVuSans.ttf"


################################################################################
## 通知
################################################################################

screen notify(message):
    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0 yoffset -10
        ease 0.3 alpha 1.0 yoffset 0
    on hide:
        ease 0.3 alpha 0.0 yoffset -10

style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos
    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding
    xalign 0.5

style notify_text:
    properties gui.text_properties("notify")


################################################################################
## NVL
################################################################################

screen nvl(dialogue, items=None):
    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        if gui.nvl_list_length:
            for i in dialogue[-gui.nvl_list_length:]:
                window:
                    has hbox:
                        spacing gui.nvl_spacing

                    if i.who is not None:
                        text i.who:
                            id "who" + str(i.id)
                            style "nvl_label"

                    text i.what:
                        id "what" + str(i.id)

        if items:
            vbox:
                for i in items:
                    textbutton i.caption:
                        action i.action
                        style "nvl_button"

    ## 对话肖像已禁用 — 使用大立绘 (show xxx_img) 代替
    # add SideImage() xalign 0.0 yalign 1.0

style nvl_window is default
style nvl_entry is default
style nvl_label is say_label
style nvl_dialogue is say_dialogue
style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True
    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_thought_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign


################################################################################
## Bubble
################################################################################

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:
            window:
                id "namebox"
                style "bubble_namebox"
                text who id "who"

        text what id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default
style bubble_namebox_label is bubble_who
style bubble_window_id is bubble_window

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"
    size gui.name_text_size

style bubble_what:
    align (0.5, 0.5)
    textalign 0.5
    layout "subtitle"
    color "#000"
    size gui.text_size

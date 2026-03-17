################################################################################
## GUI Configuration — 权谋之庭 · 大厂级暗黑宫廷风
################################################################################

init offset = -2

init python:
    gui.init(1280, 720)

define config.check_conflicting_properties = True


################################################################################
## 音效 — UI交互反馈
################################################################################

define gui.activate_sound = "audio/sfx/ui_click.ogg"
define gui.hover_sound = "audio/sfx/ui_hover.ogg"


################################################################################
## 配色 — 暗黑皇家金
################################################################################

define gui.accent_color = '#d4a942'
define gui.idle_color = '#b8a878'
define gui.idle_small_color = '#8a7e60'
define gui.hover_color = '#ffd866'
define gui.selected_color = '#ffe8a0'
define gui.insensitive_color = '#4a4030aa'
define gui.muted_color = '#5a4e3a'
define gui.hover_muted_color = '#7a6e5a'

define gui.text_color = '#e0d8c8'
define gui.interface_text_color = '#c8b890'


################################################################################
## 字体
################################################################################

define gui.text_font = "msyh.ttf"
define gui.name_text_font = "msyh.ttf"
define gui.interface_text_font = "msyh.ttf"

define gui.text_size = 24
define gui.name_text_size = 26
define gui.interface_text_size = 22
define gui.label_text_size = 30
define gui.notify_text_size = 18
define gui.title_text_size = 56


################################################################################
## 菜单背景
################################################################################

define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"


################################################################################
## 对话框
################################################################################

define gui.textbox_height = 220
define gui.textbox_yalign = 1.0

define gui.name_xpos = 280
define gui.name_ypos = 0
define gui.name_xalign = 0.0

define gui.namebox_width = None
define gui.namebox_height = None
define gui.namebox_borders = Borders(5, 5, 5, 5)
define gui.namebox_tile = False

define gui.dialogue_xpos = 300
define gui.dialogue_ypos = 56
define gui.dialogue_width = 720
define gui.dialogue_text_xalign = 0.0


################################################################################
## 按钮
################################################################################

define gui.button_width = None
define gui.button_height = None
define gui.button_borders = Borders(6, 6, 6, 6)
define gui.button_tile = False

define gui.button_text_font = gui.interface_text_font
define gui.button_text_size = gui.interface_text_size

define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

define gui.button_text_xalign = 0.0

define gui.radio_button_borders = Borders(22, 6, 6, 6)
define gui.check_button_borders = Borders(22, 6, 6, 6)
define gui.confirm_button_text_xalign = 0.5
define gui.page_button_borders = Borders(12, 6, 12, 6)

define gui.quick_button_borders = Borders(12, 4, 12, 0)
define gui.quick_button_text_size = 14
define gui.quick_button_text_idle_color = '#6a5e48'
define gui.quick_button_text_hover_color = '#d4a942'
define gui.quick_button_text_selected_color = gui.accent_color


################################################################################
## 选项按钮
################################################################################

define gui.choice_button_width = 820
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(120, 12, 120, 12)
define gui.choice_button_text_font = "msyh.ttf"
define gui.choice_button_text_size = 24
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = "#e0d8c8"
define gui.choice_button_text_hover_color = "#ffd866"
define gui.choice_button_text_insensitive_color = "#4a403888"


################################################################################
## 存档槽位按钮
################################################################################

define gui.slot_button_width = 280
define gui.slot_button_height = 220
define gui.slot_button_borders = Borders(12, 12, 12, 12)
define gui.slot_button_text_size = 14
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = '#8a7e60'
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

define config.thumbnail_width = 256
define config.thumbnail_height = 144

define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


################################################################################
## 定位和间距
################################################################################

define gui.navigation_xpos = 50
define gui.skip_ypos = 10
define gui.notify_ypos = 48
define gui.choice_spacing = 16
define gui.navigation_spacing = 6
define gui.pref_spacing = 12
define gui.pref_button_spacing = 0
define gui.page_spacing = 0
define gui.slot_spacing = 14
define gui.main_menu_text_xalign = 1.0


################################################################################
## 框架
################################################################################

define gui.frame_borders = Borders(6, 6, 6, 6)
define gui.confirm_frame_borders = Borders(50, 50, 50, 50)
define gui.skip_frame_borders = Borders(20, 8, 60, 8)
define gui.notify_frame_borders = Borders(20, 8, 50, 8)
define gui.frame_tile = False


################################################################################
## 条、滚动条和滑块
################################################################################

define gui.bar_size = 28
define gui.scrollbar_size = 8
define gui.slider_size = 28

define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(4, 4, 4, 4)
define gui.slider_borders = Borders(6, 6, 6, 6)

define gui.vbar_borders = Borders(6, 6, 6, 6)
define gui.vscrollbar_borders = Borders(4, 4, 4, 4)
define gui.vslider_borders = Borders(6, 6, 6, 6)

define gui.unscrollable = "hide"


################################################################################
## 历史
################################################################################

define config.history_length = 250

define gui.history_height = 150
define gui.history_spacing = 0

define gui.history_name_xpos = 170
define gui.history_name_ypos = 0
define gui.history_name_width = 170
define gui.history_name_xalign = 1.0

define gui.history_text_xpos = 190
define gui.history_text_ypos = 4
define gui.history_text_width = 720
define gui.history_text_xalign = 0.0


################################################################################
## NVL
################################################################################

define gui.nvl_borders = Borders(0, 10, 0, 20)
define gui.nvl_list_length = 6
define gui.nvl_height = 115
define gui.nvl_spacing = 10

define gui.nvl_name_xpos = 430
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 150
define gui.nvl_name_xalign = 1.0

define gui.nvl_text_xpos = 450
define gui.nvl_text_ypos = 8
define gui.nvl_text_width = 590
define gui.nvl_text_xalign = 0.0

define gui.nvl_thought_xpos = 240
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 780
define gui.nvl_thought_xalign = 0.0

define gui.nvl_button_xpos = 450
define gui.nvl_button_xalign = 0.0


################################################################################
## 本地化
################################################################################

define gui.language = "unicode"


################################################################################
## 移动端适配 — TapTap/Android
################################################################################

init python:

    ## ── 触屏通用（手机+平板）──
    @gui.variant
    def touch():

        ## 按钮触摸区域加大（最小44px触控目标）
        gui.quick_button_borders = Borders(40, 14, 40, 0)
        gui.button_borders = Borders(8, 8, 8, 8)
        gui.radio_button_borders = Borders(28, 8, 8, 8)
        gui.check_button_borders = Borders(28, 8, 8, 8)

        ## 触屏不需要 hover 音效（没有鼠标悬停）
        gui.hover_sound = None

        ## 滚动条加粗方便触摸拖动
        gui.scrollbar_size = 14
        gui.slider_size = 36

    ## ── 小屏手机（<1280px宽）──
    @gui.variant
    def small():

        ## 字体全面放大
        gui.text_size = 32
        gui.name_text_size = 38
        gui.notify_text_size = 26
        gui.interface_text_size = 30
        gui.button_text_size = 30
        gui.label_text_size = 36
        gui.title_text_size = 52

        ## 对话框适配全宽
        gui.textbox_height = 260
        gui.name_xpos = 80
        gui.name_ypos = 0
        gui.dialogue_xpos = 90
        gui.dialogue_ypos = 60
        gui.dialogue_width = 1100

        ## 选项按钮全宽
        gui.choice_button_width = 1200
        gui.choice_button_text_size = 30
        gui.choice_button_borders = Borders(80, 14, 80, 14)
        gui.choice_spacing = 12

        ## 导航按钮加大间距
        gui.navigation_spacing = 14
        gui.navigation_xpos = 30

        ## 设置页按钮间距
        gui.pref_button_spacing = 8
        gui.pref_spacing = 14

        ## 滑块加大
        gui.slider_size = 44
        gui.scrollbar_size = 14

        ## 历史记录
        gui.history_height = 200
        gui.history_text_width = 700
        gui.history_name_width = 200
        gui.history_name_xpos = 200
        gui.history_text_xpos = 220

        ## 存档页: 手机2列
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2
        gui.slot_button_width = 400
        gui.slot_button_height = 280
        gui.slot_spacing = 16

        ## 快捷栏加大
        gui.quick_button_text_size = 22
        gui.quick_button_borders = Borders(44, 16, 44, 0)

        ## 页码按钮
        gui.page_button_borders = Borders(16, 8, 16, 8)

        ## NVL
        gui.nvl_height = 170
        gui.nvl_name_width = 305
        gui.nvl_name_xpos = 325
        gui.nvl_text_width = 915
        gui.nvl_text_xpos = 345
        gui.nvl_text_ypos = 5
        gui.nvl_thought_width = 1240
        gui.nvl_thought_xpos = 20
        gui.nvl_button_width = 1240
        gui.nvl_button_xpos = 20

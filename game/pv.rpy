## ============================================================
## 权谋之庭 — 宣传PV (Promotional Video)
## pv.rpy — 游戏开场宣传动画
## ============================================================

################################################################################
## PV 专用 Transform
################################################################################

## 慢速放大（Ken Burns 效果）
transform pv_slow_zoom_in:
    zoom 1.0 alpha 0.0
    ease 0.8 alpha 1.0
    ease 6.0 zoom 1.12

## 慢速缩小
transform pv_slow_zoom_out:
    zoom 1.1 alpha 0.0
    ease 0.8 alpha 1.0
    ease 6.0 zoom 1.0

## 慢速平移（左->右）
transform pv_pan_right:
    xalign 0.3 alpha 0.0
    ease 0.8 alpha 1.0
    ease 6.0 xalign 0.7

## 慢速平移（右->左）
transform pv_pan_left:
    xalign 0.7 alpha 0.0
    ease 0.8 alpha 1.0
    ease 6.0 xalign 0.3

## PV 文字淡入（居中大字）
transform pv_text_fade(delay=0.0):
    alpha 0.0 zoom 0.95
    pause delay
    ease 0.6 alpha 1.0 zoom 1.0
    pause 2.0
    ease 0.5 alpha 0.0

## PV 文字从下浮入
transform pv_text_rise(delay=0.0):
    alpha 0.0 yoffset 30
    pause delay
    ease 0.5 alpha 1.0 yoffset 0

## PV 文字淡出
transform pv_text_fadeout(delay=0.0):
    pause delay
    ease 0.5 alpha 0.0

## 角色剪影闪现
transform pv_char_flash(xpos_val=0.5, delay=0.0):
    xalign xpos_val yalign 1.0 alpha 0.0 zoom 0.95
    pause delay
    ease 0.3 alpha 1.0 zoom 1.0
    pause 1.5
    ease 0.4 alpha 0.0

## 标题登场（大气放大）
transform pv_title_appear:
    alpha 0.0 zoom 0.8
    ease 1.2 alpha 1.0 zoom 1.0

## 标题呼吸光效
transform pv_title_glow:
    alpha 0.0
    pause 1.5
    block:
        ease 2.0 alpha 0.5
        ease 2.0 alpha 0.0
        repeat

## 装饰线展开
transform pv_line_expand(delay=0.0):
    xsize 0 alpha 0.0
    pause delay
    ease 0.8 xsize 400 alpha 1.0

## LOGO 区域定位 transforms
transform pv_pos_line1:
    xalign 0.5 yalign 0.32 alpha 0.0 yoffset 30
    pause 0.3
    ease 0.5 alpha 1.0 yoffset 0

transform pv_pos_title:
    xalign 0.5 yalign 0.42 alpha 0.0 zoom 0.8
    ease 1.2 alpha 1.0 zoom 1.0

transform pv_pos_subtitle:
    xalign 0.5 yalign 0.52 alpha 0.0 yoffset 30
    pause 0.8
    ease 0.5 alpha 1.0 yoffset 0

transform pv_pos_line2:
    xalign 0.5 yalign 0.58 alpha 0.0 yoffset 30
    pause 1.0
    ease 0.5 alpha 1.0 yoffset 0

transform pv_pos_tagline:
    xalign 0.5 yalign 0.68 alpha 0.0 yoffset 30
    ease 0.5 alpha 1.0 yoffset 0

transform pv_pos_platform:
    xalign 0.5 yalign 0.82 alpha 0.0 yoffset 30
    ease 0.5 alpha 1.0 yoffset 0

## 闪屏（白色闪烁）
transform pv_flash:
    alpha 0.0
    ease 0.05 alpha 0.9
    ease 0.3 alpha 0.0


################################################################################
## PV 专用 Screen — 电影宽银幕黑边
################################################################################

screen pv_letterbox():
    zorder 100
    ## 上黑边
    add Solid("#000000"):
        xsize 1280 ysize 90
        xpos 0 ypos 0
    ## 下黑边
    add Solid("#000000"):
        xsize 1280 ysize 90
        xpos 0 ypos 630

## PV 跳过按钮
screen pv_skip_btn():
    zorder 300
    textbutton "跳过 PV >":
        xalign 0.95 yalign 0.05
        text_size 14
        text_color "#8a7e6080"
        text_hover_color "#d4a942"
        text_font "msyh.ttf"
        action Jump("pv_end")


################################################################################
## PV 主体 Label
################################################################################

label pv_play:

    ## 关闭所有界面，进入纯演出模式
    $ renpy.block_rollback()
    $ _dismiss_pause = True
    $ quick_menu = False
    window hide

    show screen pv_letterbox
    show screen pv_skip_btn

    ## ══════════════════════════════════════════
    ## 第一段：黑幕 + 悬念文字
    ## ══════════════════════════════════════════

    scene black
    pause 0.5

    play music "audio/music/sad.ogg" fadein 3.0

    ## 年代背景
    show expression Text("{color=#c8b890}{size=26}公元1347年 · 深秋{/size}{/color}", outlines=[(2, "#000000", 0, 0)]) at pv_text_fade(0.3) as pvt1
    pause 3.5

    show expression Text("{color=#e8dcc0}{size=36}一封讣告，改变了一切。{/size}{/color}", outlines=[(2, "#000000", 0, 0)]) at pv_text_fade(0.0) as pvt2
    pause 3.5

    ## ══════════════════════════════════════════
    ## 第二段：城堡外景 — 继承
    ## ══════════════════════════════════════════

    scene bg_castle_exterior at pv_slow_zoom_in with dissolve
    pause 1.0

    play sound "audio/sfx/horse_gallop.ogg"

    show expression Text("{color=#e8dcc0}{size=28}父亲骤逝，你从王都匆匆赶回\n接手这片守护了三十年的领地。{/size}{/color}", outlines=[(2, "#000000", 0, 0)]) at pv_text_rise(0.5) as pvt3
    pause 4.0
    hide pvt3 with dissolve

    ## ══════════════════════════════════════════
    ## 第三段：大厅 — 各方势力登场
    ## ══════════════════════════════════════════

    scene bg_great_hall at pv_pan_right with fade
    play sound "audio/sfx/crowd_murmur.ogg"
    pause 0.5

    show expression Text("{color=#ffd866}{size=32}权力的棋盘已经摆好{/size}{/color}", outlines=[(2, "#000000", 0, 0)]) at pv_text_rise(0.3) as pvt4
    pause 2.5
    hide pvt4 with dissolve

    ## 角色快闪
    show aldric_img at pv_char_flash(0.2, 0.0) as pv_c1
    show expression Text("{color=#ff6b6b}{size=22}奥尔德里克 — 忠诚的老骑士{/size}{/color}", outlines=[(2, "#000000", 0, 0)]) at pv_text_rise(0.0) as pvtc1
    pause 2.0
    hide pvtc1 with dissolve
    hide pv_c1 with dissolve

    show elena_img at pv_char_flash(0.5, 0.0) as pv_c2
    show expression Text("{color=#c8a2ff}{size=22}艾琳娜 — 来自王宫的神秘使者{/size}{/color}", outlines=[(2, "#000000", 0, 0)]) at pv_text_rise(0.0) as pvtc2
    pause 2.0
    hide pvtc2 with dissolve
    hide pv_c2 with dissolve

    show baron_img at pv_char_flash(0.8, 0.0) as pv_c3
    show expression Text("{color=#7ecfcf}{size=22}冯·哈根男爵 — 野心勃勃的邻国领主{/size}{/color}", outlines=[(2, "#000000", 0, 0)]) at pv_text_rise(0.0) as pvtc3
    pause 2.0
    hide pvtc3 with dissolve
    hide pv_c3 with dissolve

    ## ══════════════════════════════════════════
    ## 第四段：紧张升级 — 边境危机
    ## ══════════════════════════════════════════

    stop music fadeout 1.5
    pause 0.5
    play music "audio/music/tension.ogg" fadein 2.0

    scene bg_border at pv_slow_zoom_in with fade
    play sound "audio/sfx/sword_draw.ogg"
    pause 0.8

    show expression Text("{color=#ff4444}{size=34}边境告急{/size}{/color}", outlines=[(2, "#000000", 0, 0)]) at pv_text_fade(0.0) as pvt5
    pause 2.5

    show expression Text("{color=#e8dcc0}{size=26}男爵的铁骑已在边境集结\n你的第一场考验来临{/size}{/color}", outlines=[(2, "#000000", 0, 0)]) at pv_text_rise(0.0) as pvt6
    pause 3.5
    hide pvt6 with dissolve

    ## ══════════════════════════════════════════
    ## 第五段：快速蒙太奇 — 五章场景闪切
    ## ══════════════════════════════════════════

    ## 教堂
    scene bg_church_interior at pv_slow_zoom_out with Dissolve(0.3)
    show bishop_img at pv_char_flash(0.5, 0.0) as pv_c4
    show expression Text("{color=#ffd866}{size=24}信仰，还是权术？{/size}{/color}", outlines=[(2, "#000000", 0, 0)]) at pv_text_rise(0.2) as pvt7
    pause 2.0
    hide pvt7 with dissolve

    ## 地下密室
    scene bg_underground at pv_slow_zoom_in with Dissolve(0.3)
    show lily_master_img at pv_char_flash(0.5, 0.0) as pv_c5
    show expression Text("{color=#b88aff}{size=24}暗百合……父亲死亡的真相{/size}{/color}", outlines=[(2, "#000000", 0, 0)]) at pv_text_rise(0.2) as pvt8
    pause 2.0
    hide pvt8 with dissolve

    ## 王宫
    scene bg_throne_room at pv_pan_left with Dissolve(0.3)
    show queen_img at pv_char_flash(0.3, 0.0) as pv_c6
    show prince_img at pv_char_flash(0.7, 0.0) as pv_c7
    show expression Text("{color=#d4a0ff}{size=24}王都暗流涌动，每个人都是棋子{/size}{/color}", outlines=[(2, "#000000", 0, 0)]) at pv_text_rise(0.2) as pvt9
    pause 2.5
    hide pvt9 with dissolve

    ## 战场
    scene bg_battlefield at pv_slow_zoom_in with Dissolve(0.3)
    play sound "audio/sfx/sword_draw.ogg"
    show expression Text("{color=#ff4444}{size=30}内战一触即发{/size}{/color}", outlines=[(2, "#000000", 0, 0)]) at pv_text_fade(0.0) as pvt10
    pause 2.0

    ## ══════════════════════════════════════════
    ## 第六段：白闪 + 核心台词
    ## ══════════════════════════════════════════

    scene black with Dissolve(0.1)
    show text "" as flash_layer at pv_flash
    pause 0.3

    stop music fadeout 2.0

    ## 核心问题
    show expression Text("{color=#ffd866}{size=40}选定一条路，也要承担它的代价。{/size}{/color}", outlines=[(3, "#000000", 0, 0)]) at pv_text_fade(0.3) as pvt11
    pause 3.0

    scene black with dissolve
    pause 0.5

    ## 部分结局预览
    show expression Text("{color=#c8b890}{size=18}部分结局预览{/size}{/color}", outlines=[(2, "#000000", 0, 0)]) at pv_text_fade(0.0) as pve0
    pause 1.5
    hide pve0 with dissolve

    show expression Text("{color=#ff6b6b}{size=24}铁腕领主 — 以铁与血铸就和平{/size}{/color}", outlines=[(2, "#000000", 0, 0)]) at pv_text_rise(0.0) as pve1
    pause 1.5
    hide pve1 with dissolve
    show expression Text("{color=#8ecae6}{size=24}影中之王 — 在阴影中操控一切{/size}{/color}", outlines=[(2, "#000000", 0, 0)]) at pv_text_rise(0.0) as pve2
    pause 1.5
    hide pve2 with dissolve
    show expression Text("{color=#ffd866}{size=24}圣光守护 — 以信仰之光驱散黑暗{/size}{/color}", outlines=[(2, "#000000", 0, 0)]) at pv_text_rise(0.0) as pve3
    pause 1.5
    hide pve3 with dissolve
    show expression Text("{color=#7ecf7e}{size=24}人民领主 — 守护最平凡的幸福{/size}{/color}", outlines=[(2, "#000000", 0, 0)]) at pv_text_rise(0.0) as pve4
    pause 1.5
    hide pve4 with dissolve
    show expression Text("{color=#8ecae6}{size=24}真相大白 — 正义也许会迟到{/size}{/color}", outlines=[(2, "#000000", 0, 0)]) at pv_text_rise(0.0) as pve5
    pause 1.5
    hide pve5 with dissolve

    pause 0.3

    ## ══════════════════════════════════════════
    ## 第七段：LOGO + 标题
    ## ══════════════════════════════════════════

    play music "audio/music/main_theme.ogg" fadein 2.0

    scene bg_castle_exterior at pv_slow_zoom_out
    ## 暗色遮罩
    show text "" as dark_overlay

    pause 1.0

    ## 装饰线（上）
    show text "{color=#d4a94260}{size=6}------------------------------{/size}{/color}" at pv_pos_line1 as pvline1

    ## 主标题
    show text "{color=#d4a942}{size=72}{font=msyh.ttf}权谋之庭{/font}{/size}{/color}" at pv_pos_title as pvtitle

    ## 副标题
    show text "{color=#8a7e60}{size=22}{font=msyh.ttf}Court of Shadows{/font}{/size}{/color}" at pv_pos_subtitle as pvsubtitle

    ## 装饰线（下）
    show text "{color=#d4a94260}{size=6}------------------------------{/size}{/color}" at pv_pos_line2 as pvline2

    pause 3.0

    ## Tagline
    show expression Text("{color=#e0d8c8}{size=24}{font=msyh.ttf}九条路 · 九种代价{/font}{/size}{/color}", outlines=[(2, "#000000", 0, 0)]) at pv_pos_tagline as pvtagline

    pause 3.0

    ## 平台信息
    show expression Text("{color=#c8b890}{size=18}{font=msyh.ttf}PC · Android{/font}{/size}{/color}", outlines=[(2, "#000000", 0, 0)]) at pv_pos_platform as pvplatform

    pause 4.0

    ## ══════════════════════════════════════════
    ## 结束 — 渐黑，返回主菜单
    ## ══════════════════════════════════════════

label pv_end:

    hide screen pv_skip_btn
    hide screen pv_letterbox
    stop music fadeout 3.0
    stop sound fadeout 1.0

    scene black with Dissolve(2.0)
    pause 1.0

    $ quick_menu = True
    $ _dismiss_pause = True

    return

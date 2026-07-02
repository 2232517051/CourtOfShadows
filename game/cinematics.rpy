## 章节过场动画系统
## 模仿《布兰特的苦难人生》风格
## 剪纸风插画 + 视差平移 + 英文配音 + 羊皮纸质感 + ~30秒

# ==========================================
# Transitions
# ==========================================

define cin_dissolve = Dissolve(1.5)
define cin_slow = Dissolve(2.5)
define cin_fade = Fade(1.5, 0.5, 1.5)

# 等待语音播放完毕 (保证配音不被截断)
init python:
    def wait_voice(min_time=3.0):
        """等待至少min_time秒，且等语音播完再继续"""
        if store._cin_skip:
            return
        renpy.pause(min_time, hard=True)
        if store._cin_skip:
            return
        ## 最多额外等待30秒，防止语音通道卡死导致无限循环
        waited = 0.0
        while renpy.music.is_playing(channel="voice") and waited < 30.0:
            if store._cin_skip:
                return
            renpy.pause(0.2, hard=True)
            waited += 0.2
        renpy.pause(0.5, hard=True)

    def skip_cinematic():
        """跳过当前过场动画——仅设标志位并驱散当前暂停，让 cinematic label 自然 return"""
        store._cin_skip = True
        store._dismiss_pause = True
        store.quick_menu = True
        renpy.music.stop(channel="voice")
        renpy.music.stop(channel="sound")
        for s in ["cin_overlay", "cin_text", "cin_sub", "cin_em", "cin_title"]:
            renpy.hide_screen(s)
        ## 驱散当前 hard pause，不调用 renpy.scene() / renpy.return_statement()
        ## 避免在 jump 进入的章节里 return 落点错误导致退回主菜单
        renpy.end_interaction(True)

default _cin_skip = False

# ==========================================
# 文字样式 — 模拟手写/书页感
# ==========================================

style cin_narration:
    color "#d4c5a0"
    size 28
    font "msyh.ttf"
    outlines [(2, "#0a0a0a", 0, 0)]
    text_align 0.5
    line_spacing 10

style cin_emphasis:
    color "#c9a84c"
    size 30
    font "msyh.ttf"
    outlines [(2, "#0a0a0a", 0, 0)]
    text_align 0.5
    bold True

style cin_chapter_num:
    color "#8a7a5a"
    size 22
    font "msyh.ttf"
    outlines [(1, "#0a0a0a", 0, 0)]
    text_align 0.5

style cin_chapter_title:
    color "#c9a84c"
    size 44
    font "msyh.ttf"
    outlines [(2, "#0a0a0a", 0, 0), (1, "#1a1a2e", 1, 1)]
    text_align 0.5
    bold True

style cin_chapter_sub:
    color "#7a6a4a"
    size 20
    font "msyh.ttf"
    outlines [(1, "#0a0a0a", 0, 0)]
    text_align 0.5

# ==========================================
# Transforms — 布兰特式视差平移
# ==========================================

# 插画缓慢向左平移 (视差效果, 布兰特核心动画)
transform cin_parallax_left:
    subpixel True
    xanchor 0.47 yanchor 0.5 xpos 0.5 ypos 0.5
    zoom 1.15
    linear 20.0 xanchor 0.53

# 插画缓慢向右平移
transform cin_parallax_right:
    subpixel True
    xanchor 0.53 yanchor 0.5 xpos 0.5 ypos 0.5
    zoom 1.15
    linear 20.0 xanchor 0.47

# 文字浮现 (轻微上移+淡入)
transform cin_text_in:
    alpha 0.0 yoffset 8
    ease 1.2 alpha 1.0 yoffset 0

# 文字消散
transform cin_text_out:
    alpha 1.0
    ease 0.8 alpha 0.0

# 装饰线展开
transform cin_line_grow:
    xsize 0
    ease 1.2 xsize 60

# ==========================================
# Screens
# ==========================================

# 羊皮纸纹理 + 宽银幕条 + 暗角
screen cin_overlay():
    zorder 90
    # 上下黑条 (窄一点, 更电影感)
    frame:
        xfill True ysize 60 ypos 0
        background "#000000"
    frame:
        xfill True ysize 60 yalign 1.0
        background "#000000"
    # 暗角
    add "gui/overlay/cinematic_vignette.png" alpha 0.8
    # 羊皮纸纹理
    add "gui/overlay/parchment_overlay.png" alpha 0.4
    # 跳过按钮
    textbutton "跳过 ▶▶":
        xalign 0.97 yalign 0.02
        text_size 18
        text_color "#8a7a5a"
        text_hover_color "#c9a84c"
        action Function(skip_cinematic)

# 中央叙事文字
screen cin_text(line1, line2=""):
    zorder 100
    vbox:
        xalign 0.5 yalign 0.48
        xmaximum 750
        spacing 6
        text line1 style "cin_narration" xalign 0.5 at cin_text_in
        if line2:
            text line2 style "cin_narration" xalign 0.5 at cin_text_in

# 中央强调文字
screen cin_em(line):
    zorder 100
    frame:
        xalign 0.5 yalign 0.48
        xmaximum 750
        background None
        text line style "cin_emphasis" xalign 0.5 at cin_text_in

# 底部字幕 (配合语音, 半透明底)
screen cin_sub(sub):
    zorder 100
    frame:
        xalign 0.5 yalign 0.84
        xmaximum 850
        background Solid("#00000099")
        padding (24, 10, 24, 10)
        text sub style "cin_narration" xalign 0.5 at cin_text_in

# 章节标题卡
screen cin_title(num, title, sub=""):
    zorder 100
    vbox:
        xalign 0.5 yalign 0.45
        spacing 10
        hbox:
            xalign 0.5 spacing 16
            frame:
                yalign 0.5 ysize 1
                background "#6a5a3a"
                at cin_line_grow
            text "第[num]章" style "cin_chapter_num" at cin_text_in
            frame:
                yalign 0.5 ysize 1
                background "#6a5a3a"
                at cin_line_grow
        null height 4
        text title style "cin_chapter_title" xalign 0.5 at cin_text_in
        if sub:
            null height 2
            text sub style "cin_chapter_sub" xalign 0.5 at cin_text_in

# ==========================================
# 第一章 过场 — 新主登基 (~30秒)
# ==========================================

label cinematic_chapter1:
    window hide
    $ quick_menu = False
    $ _dismiss_pause = False
    $ _cin_skip = False

    stop music fadeout 1.5
    scene black
    pause 0.5

    # 钟声 + 黑底文字 (布兰特式: 先黑屏出文字)
    play sound "audio/sfx/bell_toll.ogg"
    show screen cin_text("公元1347年。深秋。", "艾登堡的领主，永远地闭上了双眼。")
    pause 4.0
    hide screen cin_text with cin_dissolve
    pause 0.5

    # 章节标题卡
    play music "audio/music/sad.ogg" fadein 2.5
    show screen cin_title(1, "新主登基", "The New Lord Ascends")
    pause 3.5
    hide screen cin_title with cin_dissolve
    pause 0.3

    # 插画背景 + 视差平移 + 语音字幕
    scene bg castle_exterior at cin_parallax_left with cin_slow
    show screen cin_overlay
    pause 0.8

    voice "audio/narration/ch1_line1.mp3"
    show screen cin_sub("1347年深秋，艾登堡的老领主咽下了最后一口气。")
    $ wait_voice(7.0)
    hide screen cin_sub

    play sound "audio/sfx/horse_gallop.ogg" volume 0.5
    voice "audio/narration/ch1_line2.mp3"
    show screen cin_sub("他唯一的继承人，年仅二十二岁，在冷雨与沉默中策马三日。")
    $ wait_voice(7.0)
    hide screen cin_sub

    voice "audio/narration/ch1_line3.mp3"
    show screen cin_sub("然而等待他的，并非哀悼与安宁——而是一场早已布好的棋局。")
    $ wait_voice(7.0)
    hide screen cin_sub

    # 淡出
    hide screen cin_overlay
    scene black with cin_slow
    stop music fadeout 2.0
    pause 1.0

    $ _dismiss_pause = False
    $ _cin_skip = False
    $ _dismiss_pause = True
    $ quick_menu = True
    window auto
    return

# ==========================================
# 第二章 过场 — 领主会议 (~30秒)
# ==========================================

label cinematic_chapter2:
    window hide
    $ quick_menu = False
    $ _dismiss_pause = False
    $ _cin_skip = False

    stop music fadeout 1.5
    scene black
    pause 0.5

    if not _cin_skip:
        show screen cin_text("一个月过去了。", "贵族们的目光，已经投向了这位年轻的领主。")
        pause 4.0
        hide screen cin_text with cin_dissolve
        pause 0.5

    if not _cin_skip:
        play music "audio/music/tension.ogg" fadein 2.5
        show screen cin_title(2, "领主会议", "The Council of Lords")
        pause 3.5
        hide screen cin_title with cin_dissolve
        pause 0.3

    if not _cin_skip:
        scene bg great_hall at cin_parallax_right with cin_slow
        show screen cin_overlay
        pause 0.8

    if not _cin_skip:
        voice "audio/narration/ch2_line1.mp3"
        show screen cin_sub("年轻领主登位已有一月。")
        $ wait_voice(4.0)
        hide screen cin_sub

    if not _cin_skip:
        play sound "audio/sfx/crowd_murmur.ogg" volume 0.4
        voice "audio/narration/ch2_line2.mp3"
        show screen cin_sub("五位领主齐聚大厅，各怀心思。")
        $ wait_voice(5.0)
        hide screen cin_sub

    if not _cin_skip:
        voice "audio/narration/ch2_line3.mp3"
        show screen cin_sub("在权谋之庭，每句话都是武器，每次沉默都是陷阱。")
        $ wait_voice(6.0)
        hide screen cin_sub

    hide screen cin_overlay
    scene black with dissolve
    stop music fadeout 2.0

    $ _cin_skip = False
    $ _dismiss_pause = True
    $ quick_menu = True
    window auto
    return

# ==========================================
# 第三章 过场 — 暗百合 (~30秒)
# ==========================================

label cinematic_chapter3:
    window hide
    $ quick_menu = False
    $ _dismiss_pause = False
    $ _cin_skip = False

    stop music fadeout 1.5
    scene black
    pause 0.5

    if not _cin_skip:
        show screen cin_text("暗杀事件后的第三天。", "伤疤还在作痛。")
        pause 4.0
        hide screen cin_text with cin_dissolve
        pause 0.5

    if not _cin_skip:
        play music "audio/music/conspiracy.ogg" fadein 2.5
        show screen cin_title(3, "暗百合", "The Dark Lily")
        pause 3.5
        hide screen cin_title with cin_dissolve
        pause 0.3

    if not _cin_skip:
        scene bg forest_path at cin_parallax_left with cin_slow
        show screen cin_overlay
        pause 0.8

    if not _cin_skip:
        voice "audio/narration/ch3_line1.mp3"
        show screen cin_sub("脸上的伤疤时刻提醒着他——有人要他死。")
        $ wait_voice(6.0)
        hide screen cin_sub

    if not _cin_skip:
        voice "audio/narration/ch3_line2.mp3"
        show screen cin_sub("农民在森林附近失踪，暗百合的符号出现在墙壁和门上。")
        $ wait_voice(7.0)
        hide screen cin_sub

    if not _cin_skip:
        voice "audio/narration/ch3_line3.mp3"
        show screen cin_sub("一个古老的秘密在地底涌动，比城堡本身还要久远。")
        $ wait_voice(6.0)
        hide screen cin_sub

    hide screen cin_overlay
    scene black with dissolve
    stop music fadeout 2.0

    $ _cin_skip = False
    $ _dismiss_pause = True
    $ quick_menu = True
    window auto
    return

# ==========================================
# 第四章 过场 — 王都风云 (~30秒)
# ==========================================

label cinematic_chapter4:
    window hide
    $ quick_menu = False
    $ _dismiss_pause = False
    $ _cin_skip = False

    stop music fadeout 1.5
    scene black
    pause 0.5

    if not _cin_skip:
        play sound "audio/sfx/horse_gallop.ogg" volume 0.4
        show screen cin_text("城门在晨雾中缓缓开启。", "身后是家园，前方是未知的王都。")
        pause 4.0
        hide screen cin_text with cin_dissolve
        pause 0.5

    if not _cin_skip:
        play music "audio/music/great_hall.ogg" fadein 2.5
        show screen cin_title(4, "王都风云", "The Capital")
        pause 3.5
        hide screen cin_title with cin_dissolve
        pause 0.3

    if not _cin_skip:
        scene bg royal_palace at cin_parallax_right with cin_slow
        show screen cin_overlay
        pause 0.8

    if not _cin_skip:
        voice "audio/narration/ch4_line1.mp3"
        show screen cin_sub("城门在黎明时分缓缓开启，领主策马奔向王都。")
        $ wait_voice(5.0)
        hide screen cin_sub

    if not _cin_skip:
        voice "audio/narration/ch4_line2.mp3"
        show screen cin_sub("五天的路途，穿越每一处阴影都可能藏着敌人的土地。")
        $ wait_voice(5.0)
        hide screen cin_sub

    if not _cin_skip:
        voice "audio/narration/ch4_line3.mp3"
        show screen cin_sub("王座不等待任何人——但权力的游戏从不停歇。")
        $ wait_voice(5.0)
        hide screen cin_sub

    hide screen cin_overlay
    scene black with dissolve
    stop music fadeout 2.0

    $ _cin_skip = False
    $ _dismiss_pause = True
    $ quick_menu = True
    window auto
    return

# ==========================================
# 第五章 过场 — 最终决战 (~30秒)
# ==========================================

label cinematic_chapter5:
    window hide
    $ quick_menu = False
    $ _dismiss_pause = False
    $ _cin_skip = False

    stop music fadeout 1.5
    scene black
    pause 0.5

    if not _cin_skip:
        play sound "audio/sfx/thunder.ogg"
        show screen cin_text("春天来了。", "但带来的不是生机——而是战争。")
        pause 4.0
        hide screen cin_text with cin_dissolve
        pause 0.5

    if not _cin_skip:
        play music "audio/music/war_drums.ogg" fadein 2.5
        show screen cin_title(5, "最终决战", "The Final Stand")
        pause 3.5
        hide screen cin_title with cin_dissolve
        pause 0.3

    if not _cin_skip:
        scene bg battlefield at cin_parallax_left with cin_slow
        show screen cin_overlay
        pause 0.8

    if not _cin_skip:
        voice "audio/narration/ch5_line1.mp3"
        show screen cin_sub("春天来了，却没有带来温暖——只有战争的鼓声。")
        $ wait_voice(5.0)
        hide screen cin_sub

    if not _cin_skip:
        play sound "audio/sfx/heartbeat.ogg" volume 0.6
        voice "audio/narration/ch5_line2.mp3"
        show screen cin_sub("南方三千大军，北方两千五百铁骑，艾登堡夹在中间。")
        $ wait_voice(8.0)
        hide screen cin_sub

    if not _cin_skip:
        voice "audio/narration/ch5_line3.mp3"
        show screen cin_sub("最终的抉择就在眼前。不仅关乎一位领主——更关乎城墙内的每一个灵魂。")
        $ wait_voice(7.0)
        hide screen cin_sub

    hide screen cin_overlay
    scene black with dissolve
    stop music fadeout 2.0

    $ _cin_skip = False
    $ _dismiss_pause = True
    $ quick_menu = True
    window auto
    return

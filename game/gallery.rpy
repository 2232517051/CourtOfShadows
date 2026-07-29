## ============================================================
## CG画廊 & 音乐鉴赏 & 成就展示 & 章节选择
## 大厂级设计
## ============================================================

## ════════════════════════════════════════════════════════════
## CG画廊
## ════════════════════════════════════════════════════════════

init python:
    gallery_images = [
        ("bg_castle_exterior", "艾登堡城堡"),
        ("bg_great_hall", "大厅"),
        ("bg_study", "书房"),
        ("bg_border", "北方边境"),
        ("bg_council_hall", "领主议事厅"),
        ("bg_market", "哈伦堡集市"),
        ("bg_forest_path", "密林小径"),
        ("bg_underground", "暗百合密室"),
        ("bg_church_interior", "大教堂"),
        ("bg_royal_palace", "王宫"),
        ("bg_throne_room", "王座大厅"),
        ("bg_palace_garden", "宫廷花园"),
        ("bg_dungeon", "地牢"),
        ("bg_battlefield", "战场"),
        ## 南境游记 DLC
        ("bg_tideport_harbor", "潮汐港"),
        ("bg_tideport_tavern", "断锚酒馆"),
        ("bg_tideport_beach", "潮汐港海堤"),
        ("bg_tideport_ship", "海雀号货舱"),
        ("bg_tideport_office", "港务厅"),
        ("bg_tideport_fleet", "兵临港外"),
        ## ── 2026-07-30 资源体检新增(Codex 生成) ──
        ("bg_village", "村庄"),
        ("bg_raven_deck", "渡鸦号"),
        ("bg_herb_garden", "药草园"),
        ("bg_forest_grave", "林间墓地"),
        ("bg_study_night", "书房之夜"),
        ("bg_south_port", "南港暮色"),
        ## ── CG(避脸构图, 2026-07-30) ──
        ("cg_unmask", "面具坠地"),
        ("cg_confession_elena", "星下双影"),
        ("cg_confession_corsair", "船首星辰"),
        ("cg_end_iron", "残旗破晓"),
        ("cg_end_shadow", "密室烛影"),
        ("cg_end_holy", "彩窗圣典"),
        ("cg_end_people", "麦野长桌"),
        ("cg_end_truth", "晨光诏书"),
        ("cg_end_borgia", "王冠鸩影"),
        ("cg_end_vassal", "鹰旗低垂"),
        ("cg_end_fall", "烬中金鹰"),
        ("cg_end_sea", "船尾斗篷"),
        ## ── 孤儿资产接线批(2026-07-30) ──
        ("bg_castle_kitchen", "炉火深厨"),
        ("bg_poor_district", "暮色穷巷"),
        ("bg_healer_house", "药草小屋"),
        ("bg_blacksmith", "锻铁炉前"),
        ("bg_castle_treasury", "地库密藏"),
        ("bg_interrogation_room", "石室讯堂"),
    ]

    gallery_characters = [
        ("aldric", "奥尔德里克"),
        ("elena", "艾琳娜"),
        ("bishop", "主教马修斯"),
        ("baron", "冯·哈根男爵"),
        ("captain", "队长雷恩"),
        ("queen", "伊莎贝拉王后"),
        ("merchant_karl", "商人卡尔"),
        ("lily_master", "暗百合首领"),
        ("prince", "弗雷德里克王子"),
        ("corsair", "渡鸦船长赛琳"),
    ]

transform gallery_thumb_hover:
    on hover:
        ease 0.2 zoom 1.08
    on idle:
        ease 0.2 zoom 1.0

screen cg_gallery():
    tag menu
    use game_menu(_("画廊"), scroll="viewport"):
        style_prefix "gallery"

        vbox:
            spacing 20

            ## ─── 场景 ───
            hbox:
                spacing 8
                text "*" size 20 color "#d4a942" yalign 0.5
                text "场景画廊" size 22 color "#d4a942" font "msyh.ttf"
            $ scene_unlocked = len([x for x, _ in gallery_images if x in persistent.gallery_unlocked])
            text "已解锁 [scene_unlocked]/[len(gallery_images)] 幅场景" size 13 color "#6a5e48"

            null height 4

            grid 4 11:
                spacing 12
                xfill True

                for img_name, img_label in gallery_images:
                    $ img_path = "images/" + img_name + ".webp"
                    $ is_unlocked = img_name in persistent.gallery_unlocked
                    if renpy.loadable(img_path) and is_unlocked:
                        vbox:
                            spacing 4
                            frame:
                                xsize 190
                                ysize 107
                                background Solid("#1a152800")

                                imagebutton:
                                    idle Transform(img_path, size=(190, 107))
                                    hover Transform(img_path, size=(190, 107))
                                    action Show("fullscreen_image", img=img_path)
                                    at gallery_thumb_hover

                            text img_label size 12 xalign 0.5 color "#b8a878"
                    else:
                        vbox:
                            spacing 4
                            frame:
                                xsize 190
                                ysize 107
                                background Solid("#0f0d1a")
                                text "锁" xalign 0.5 yalign 0.5 size 28 color "#2a2040"
                            text "？？？" size 12 xalign 0.5 color "#3a3040"

                for i in range(4 * 11 - len(gallery_images)):
                    null

            null height 20
            add Solid("#d4a94220") xsize 1.0 ysize 1
            null height 10

            ## ─── 角色 ───
            hbox:
                spacing 8
                text "*" size 20 color "#d4a942" yalign 0.5
                text "角色肖像" size 22 color "#d4a942" font "msyh.ttf"
            $ char_unlocked = len([x for x, _ in gallery_characters if x in persistent.gallery_unlocked])
            text "已解锁 [char_unlocked]/[len(gallery_characters)] 位角色" size 13 color "#6a5e48"

            null height 4

            grid 5 2:
                spacing 12
                xfill True

                for img_name, img_label in gallery_characters:
                    $ img_path = "images/" + img_name + ".png"
                    $ is_unlocked = img_name in persistent.gallery_unlocked
                    if renpy.loadable(img_path) and is_unlocked:
                        vbox:
                            spacing 4
                            frame:
                                xsize 150
                                ysize 150
                                background Solid("#1a152800")

                                imagebutton:
                                    idle Transform(img_path, size=(150, 150))
                                    hover Transform(img_path, size=(150, 150))
                                    action Show("fullscreen_image", img=img_path)
                                    at gallery_thumb_hover

                            text img_label size 12 xalign 0.5 color "#b8a878" font "msyh.ttf"
                    else:
                        vbox:
                            spacing 4
                            frame:
                                xsize 150
                                ysize 150
                                background Solid("#0f0d1a")
                                text "锁" xalign 0.5 yalign 0.5 size 28 color "#2a2040"
                            text "？？？" size 12 xalign 0.5 color "#3a3040"

                for i in range(5 * 2 - len(gallery_characters)):
                    null


## ─── 全屏查看 ───
screen fullscreen_image(img):
    modal True
    zorder 200

    add Solid("#000000ee")
    ## 资源体检P0: 原尺寸绘制会裁切/溢出 1024 级立绘, 统一 contain 适配虚拟画布
    add Transform(img, size=(1280, 720), fit="contain") xalign 0.5 yalign 0.5

    ## 关闭提示
    frame:
        xalign 0.5
        yalign 0.97
        background Solid("#0f0d1acc")
        xpadding 20
        ypadding 8
        text "点击任意位置关闭" size 14 color "#6a5e48"

    key "mouseup_1" action Hide("fullscreen_image")
    key "K_ESCAPE" action Hide("fullscreen_image")


## ════════════════════════════════════════════════════════════
## 音乐鉴赏
## ════════════════════════════════════════════════════════════

init python:
    ## 音乐曲目: (文件, 名称, 描述, 图标, 解锁条件章节)
    ## 解锁条件: None=默认解锁, "chapter1"=通过第一章后解锁, 以此类推
    music_tracks_data = [
        ("audio/music/main_theme.ogg", "主旋律", "权谋之庭主题曲", "*", None),
        ("audio/music/castle_calm.ogg", "城堡日常", "平静的领地生活", "城", None),
        ("audio/music/great_hall.ogg", "大厅", "庄严的议事氛围", "剑", "chapter1"),
        ("audio/music/tension.ogg", "暗流涌动", "紧张的阴谋时刻", "刃", "chapter2"),
        ("audio/music/battle_prepare.ogg", "战鼓雷鸣", "备战的号角声", "剑", "chapter2"),
        ("audio/music/night_mystery.ogg", "夜之谜", "神秘的夜晚", "月", "chapter3"),
        ("audio/music/victory.ogg", "凯旋", "胜利的欢呼", "*", "chapter5"),
        ("audio/music/sad.ogg", "悲歌", "悲伤的旋律", "泪", "chapter4"),
        ("audio/music/tavern_lively.ogg", "酒馆欢歌", "热闹的民谣与欢笑", "酒", "chapter2"),
        ("audio/music/forest_ambient.ogg", "密林低语", "自然的呼吸与鸟鸣", "林", "chapter2"),
        ("audio/music/rain_storm.ogg", "暴雨将至", "雷鸣与骤雨", "雨", "chapter1"),
        ("audio/music/market_bustle.ogg", "集市喧嚣", "繁忙市集的烟火气", "市", "chapter2"),
        ("audio/music/church_choir.ogg", "圣歌回荡", "教堂唱诗班的庄严", "圣", "chapter3"),
        ("audio/music/dungeon_drip.ogg", "幽暗地牢", "滴水与锁链的回响", "牢", "chapter4"),
        ("audio/music/harbor_waves.ogg", "港湾波涛", "海风与潮声", "港", "chapter2"),
        ("audio/music/campfire.ogg", "篝火夜话", "温暖的火焰与虫鸣", "火", "chapter2"),
        ("audio/music/war_drums.ogg", "战鼓擂动", "震撼大地的战争序曲", "鼓", "chapter5"),
        ("audio/music/coronation.ogg", "加冕礼赞", "辉煌的典礼乐章", "冕", "chapter5"),
        ("audio/music/conspiracy.ogg", "暗流涌动", "密谋与窃语", "谋", "chapter3"),
        ("audio/music/chase.ogg", "亡命追逐", "紧迫的追击节奏", "追", "chapter4"),
        ("audio/music/romance.ogg", "柔情似水", "浪漫的心弦颤动", "情", "chapter2"),
        ("audio/music/grief.ogg", "深渊悲恸", "无尽的哀伤", "哀", "chapter1"),
        ("audio/music/revelation.ogg", "真相揭晓", "震撼的发现时刻", "真", "chapter3"),
        ("audio/music/betrayal.ogg", "背信弃义", "刺痛人心的背叛", "叛", "chapter4"),
        ("audio/music/hope.ogg", "曙光初现", "黎明前的希望之光", "望", "chapter5"),
        ("audio/music/winter_wind.ogg", "朔风凛冽", "孤寂的冬日寒风", "寒", None),
        ("audio/music/dawn.ogg", "破晓新生", "新一天的开始", "晨", "chapter5"),
        ("audio/music/ritual.ogg", "暗夜仪式", "神秘的古老典礼", "祭", "chapter3"),
        ## 番外配乐（剧情未直接使用，作为收藏曲）
        ("audio/music/throne.ogg", "铁王座", "至高权力的孤独与重量", "座", "chapter5"),
        ("audio/music/escape.ogg", "密道亡奔", "火把映墙，追兵在后", "逃", "chapter4"),
        ## 外章 · 南境游记
        ## 解锁条件原本是 None —— 而 is_music_unlocked(None) 恒返回 True(见下), 于是没去过
        ## 南境的玩家在音乐室里就能读到「王军压境」「自由港，守住了自由，代价也已付清」
        ## 这类曲名和描述, 等于把外章的走向提前剧透。改挂 "southern"。
        ## (老档靠 save_compat.rpy 的 init 迁移补上 chapters_completed 里的 "southern",
        ##  否则这一行会从每个老玩家的音乐室里抽走 6 首已经听过的曲子。)
        ("audio/music/southern_port.ogg", "潮汐港", "南方自由港的喧嚣与海风", "港", "southern"),
        ("audio/music/southern_tavern.ogg", "断锚酒馆", "水手与走私客的粗粝欢闹", "酒", "southern"),
        ("audio/music/southern_corsair.ogg", "渡鸦船长", "豪迈中藏着柔情的海上之心", "渡", "southern"),
        ("audio/music/southern_scheme.ogg", "火并疑云", "码头暗处有人在拨弄棋局", "谋", "southern"),
        ("audio/music/southern_fleet.ogg", "兵临港外", "黑水之上压来的桅灯之墙", "舰", "southern"),
        ("audio/music/southern_freeport.ogg", "自由港", "守住了自由，代价也已付清", "由", "southern"),
        ## ── 2026-07-30 资源体检新增(suno, 用户官网生成) ──
        ("audio/music/sea_theme.ogg", "远渡", "大提琴送别，海风裹着未还的债", "帆", "chapter5"),
        ("audio/music/ending_triumph.ogg", "破晓", "铜管吹散长夜，霜痕留在旗上", "旭", "chapter5"),
        ("audio/music/ending_dark.ogg", "丧钟", "低弦拖过空殿，余音不散", "墟", "chapter5"),
        ("audio/music/ending_bitter.ogg", "残局", "小调收弦处圆号独暖，赢了又如何", "茧", "chapter5"),
    ]

    def is_music_unlocked(req_chapter):
        if req_chapter is None:
            return True
        if persistent.chapters_completed and req_chapter in persistent.chapters_completed:
            return True
        return False

    ## 兼容旧变量名
    music_tracks = [(f, n, d, i) for f, n, d, i, _ in music_tracks_data]

screen music_room():
    tag menu
    use game_menu(_("音乐鉴赏"), scroll="viewport"):
        vbox:
            spacing 16

            hbox:
                spacing 8
                text "【乐】" size 24 color "#d4a942" yalign 0.5
                text "音乐鉴赏" size 26 color "#d4a942" font "msyh.ttf"

            $ _unlocked_music = len([1 for _,_,_,_,req in music_tracks_data if is_music_unlocked(req)])
            text "[_unlocked_music]/[len(music_tracks_data)] 首原创配乐已解锁" size 14 color "#6a5e48"

            null height 8

            for track_file, track_name, track_desc, track_icon, track_req in music_tracks_data:
                $ _m_unlocked = is_music_unlocked(track_req)
                frame:
                    xfill True
                    xpadding 16
                    ypadding 12
                    background Solid("#1a152800")
                    hover_background Solid("#1a152880")

                    if _m_unlocked and renpy.loadable(track_file):
                        button:
                            action Play("music", track_file, fadein=1.0)
                            xfill True
                            background None

                            hbox:
                                spacing 14
                                yalign 0.5

                                ## 图标
                                frame:
                                    xsize 44
                                    ysize 44
                                    background Solid("#d4a94215")
                                    text track_icon xalign 0.5 yalign 0.5 size 20

                                vbox:
                                    spacing 2
                                    text track_name size 18 color "#e0d8c8" font "msyh.ttf"
                                    text track_desc size 13 color "#6a5e48"

                                ## 播放图标
                                text ">" xalign 1.0 yalign 0.5 size 16 color "#d4a94260"
                    else:
                        hbox:
                            spacing 14
                            yalign 0.5
                            frame:
                                xsize 44
                                ysize 44
                                background Solid("#0f0d1a")
                                text "锁" xalign 0.5 yalign 0.5 size 16
                            vbox:
                                text track_name size 18 color "#3a3040" font "msyh.ttf"
                                if track_req:
                                    text "通过相关章节解锁" size 13 color "#2a2030"
                                else:
                                    text "音频文件缺失" size 13 color "#2a2030"

            null height 16
            add Solid("#d4a94220") xsize 1.0 ysize 1
            null height 8

            ## 停止按钮
            frame:
                xalign 0.5
                xpadding 24
                ypadding 10
                background Solid("#1a152880")

                textbutton "# 停止播放":
                    action Stop("music", fadeout=1.0)
                    text_size 16
                    text_color "#8a7e60"
                    text_hover_color "#d4a942"


## ════════════════════════════════════════════════════════════
## 成就展示
## ════════════════════════════════════════════════════════════

screen achievement_screen():
    tag menu
    use game_menu(_("成就"), scroll="viewport"):
        vbox:
            spacing 12

            ## 标题
            hbox:
                spacing 8
                text "*" size 24 color "#d4a942" yalign 0.5
                text "成就殿堂" size 26 color "#d4a942" font "msyh.ttf"

            $ ach_count = len(persistent.achievements) if persistent.achievements else 0
            $ ach_total = len(achievement_data)
            text "已解锁 [ach_count]/[ach_total]" size 14 color "#6a5e48"

            ## 进度条
            bar:
                value StaticValue(ach_count, ach_total)
                xmaximum 400
                ysize 6
                left_bar Solid("#d4a942")
                right_bar Solid("#1a1528")

            null height 10

            for key in achievement_data:
                $ a_data = achievement_data[key]
                $ a_name = a_data[0]
                $ a_desc = a_data[1]
                $ a_hidden = a_data[2] if len(a_data) > 2 else False
                $ a_hint = a_data[3] if len(a_data) > 3 else "继续游戏解锁"
                $ unlocked = key in persistent.achievements

                frame:
                    xfill True
                    xpadding 16
                    ypadding 12
                    background Solid("#1a152840" if unlocked else "#0f0d1a40")

                    hbox:
                        spacing 14
                        yalign 0.5

                        ## 成就图标
                        frame:
                            xsize 44
                            ysize 44
                            background Solid("#d4a94220" if unlocked else "#1a1528")

                            if unlocked:
                                text "*" xalign 0.5 yalign 0.5 size 22 color "#ffd700"
                            elif a_hidden:
                                text "？" xalign 0.5 yalign 0.5 size 22 color "#6a3080"
                            else:
                                text "*" xalign 0.5 yalign 0.5 size 22 color "#2a2040"

                        vbox:
                            spacing 2
                            if unlocked:
                                text a_name size 17 color "#e0d8c8" font "msyh.ttf" bold True
                                text a_desc size 13 color "#8a7e60"
                            elif a_hidden:
                                text "隐藏成就" size 17 color "#6a3080" font "msyh.ttf"
                                text a_hint size 13 color "#4a3060"
                            else:
                                text a_name size 17 color "#3a3040" font "msyh.ttf"
                                text a_hint size 13 color "#2a2030"


## ════════════════════════════════════════════════════════════
## 章节选择
## ════════════════════════════════════════════════════════════

init python:
    ## 「外章」= 原「南境游记」DLC, 已并入主线目录, 排在第一章与第二章之间(它在时间线上
    ## 就落在那个月里: script.rpy 第一章末深秋 → chapter2.rpy 开场"一个月过去了")。
    ## 主菜单不再为它单开一栏(screens.rpy 原 443-467 已删)。
    chapter_list = [
        ("prologue", "序章", "金鹰之子", "prologue", "学院、王都，归乡前最后的日子"),
        ("chapter1", "第一章", "新主登基", "chapter1_start", "初临领地，面对未知的挑战"),
        ("southern", "外章", "南境游记", "southern_arc_standalone", "潮汐港的火并，与一条断了的盐路"),
        ("chapter2", "第二章", "领主会议", "chapter2_start", "贵族间的明争暗斗"),
        ("chapter3", "第三章", "暗百合", "chapter3_start", "神秘组织浮出水面"),
        ("chapter4", "第四章", "王都风云", "chapter4_start", "踏入更大的棋局"),
        ("chapter5", "第五章", "最终决战", "chapter5_start", "一切的终章"),
    ]

    ## **必须与 chapter_list 等长**: 下面 screen 里是 `for idx, (...) in enumerate(chapter_list)`
    ## 再按 idx 取图标, 少一个元素直接 IndexError 崩掉整个章节选择页。
    chapter_icons = ["序", "I", "外", "II", "III", "IV", "V"]

screen chapter_select():
    tag menu
    use game_menu(_("章节选择"), scroll="viewport"):
        vbox:
            spacing 16

            ## 标题
            hbox:
                spacing 8
                text "【章】" size 24 color "#d4a942" yalign 0.5
                text "章节选择" size 26 color "#d4a942" font "msyh.ttf"

            text "通关后解锁章节——从头开始，或带档重玩" size 14 color "#6a5e48"

            null height 10

            for idx, (ch_id, ch_num, ch_name, ch_label, ch_desc) in enumerate(chapter_list):
                $ is_unlocked = ch_id in persistent.chapters_completed or ch_id == "chapter1" or ch_id == "prologue"

                frame:
                    xfill True
                    xpadding 0
                    ypadding 0
                    background Solid("#1a152800")

                    if is_unlocked:
                        ## 带档开始(replay.rpy): 槽位来自真实游玩经过该章开头时的自动存档。
                        ## 白板开局先置 _skip_next_chapter_autosave, 防止默认状态覆盖真周目槽位;
                        ## 只对入口有自动存档的章节设(序章/外章白板路径上没有这个存档点)。
                        $ ch_slot = "auto_ch-" + ch_id
                        $ has_slot = renpy.can_load(ch_slot)
                        $ blank_action = ([SetField(persistent, "_skip_next_chapter_autosave", True), Start(ch_label)]
                                          if ch_id in ("chapter1", "chapter2", "chapter3", "chapter4", "chapter5")
                                          else Start(ch_label))
                        hbox:
                            xfill True
                            spacing 6
                            button:
                                action blank_action
                                xsize (0.80 if has_slot else 1.0)
                                xpadding 20
                                ypadding 16
                                background Solid("#1a152840")
                                hover_background Solid("#1a152880")

                                hbox:
                                    spacing 16
                                    yalign 0.5

                                    ## 章节编号
                                    frame:
                                        xsize 56
                                        ysize 56
                                        background Solid("#d4a94215")
                                        text chapter_icons[idx] xalign 0.5 yalign 0.5 size 26 color "#d4a942" font "msyh.ttf"

                                    vbox:
                                        spacing 3
                                        text ch_num size 13 color "#d4a942"
                                        text ch_name size 20 color "#e0d8c8" font "msyh.ttf" bold True
                                        text ch_desc size 13 color "#8a7e60"

                                    ## 箭头
                                    text ">" xalign 1.0 yalign 0.5 size 16 color "#d4a94260"

                            if has_slot:
                                button:
                                    action FileLoad(ch_slot, slot=True)
                                    xfill True
                                    ypadding 16
                                    background Solid("#d4a94218")
                                    hover_background Solid("#d4a94230")
                                    vbox:
                                        xalign 0.5
                                        yalign 0.5
                                        spacing 2
                                        text "带档开始" xalign 0.5 size 15 color "#d4a942" font "msyh.ttf"
                                        text "续上次轨迹" xalign 0.5 size 11 color "#8a7e60"

                    else:
                        frame:
                            xfill True
                            xpadding 20
                            ypadding 16
                            background None

                            hbox:
                                spacing 16
                                yalign 0.5

                                frame:
                                    xsize 56
                                    ysize 56
                                    background Solid("#0f0d1a")
                                    text chapter_icons[idx] xalign 0.5 yalign 0.5 size 26 color "#2a2040" font "msyh.ttf"

                                vbox:
                                    spacing 3
                                    text ch_num size 13 color "#2a2040"
                                    text "[ch_name] — 未解锁" size 20 color "#3a3040" font "msyh.ttf"

            null height 16
            add Solid("#d4a94220") xsize 1.0 ysize 1
            null height 8

            ## 结局统计
            frame:
                xalign 0.5
                xpadding 24
                ypadding 12
                background Solid("#1a152840")

                hbox:
                    spacing 12
                    text "【卷】" size 18 yalign 0.5
                    $ endings_count = len(persistent.endings_seen) if persistent.endings_seen else 0
                    text "已解锁结局： [endings_count]/9" size 16 color "#8a7e60" font "msyh.ttf" yalign 0.5

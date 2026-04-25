## ============================================================
## 权谋之庭 — 扩展系统
## extras.rpy
## 角色图鉴 / 决策日志 / 地图 / 收藏品 / 片尾字幕
## 章节统计 / New Game+ / 关键抉择倒计时 / 辅助功能
## ============================================================


################################################################################
## 1. 角色图鉴系统 (Character Codex)
################################################################################

init python:
    ## 角色百科数据: (id, 名称, 称号, 颜色, 简介, 详细背景)
    codex_characters = [
        ("aldric", "奥尔德里克", "艾登堡老管家", "#8b0000",
         "你父亲最信任的骑士，现在成为你的忠实守护者。",
         "奥尔德里克年轻时曾是王国最出色的骑士之一。三十年前，他救下了你的父亲，从此成为艾登堡最忠诚的仆从。\n\n他性格严肃但心地善良，对你既是管家也是长辈。他知道许多关于你父亲的秘密，但并非全部。\n\n「我曾发誓守护这座城堡，直到最后一刻。」"),

        ("elena", "艾琳娜", "王后密使", "#9370db",
         "伊莎贝拉王后派来的神秘侍女，身份成谜。",
         "艾琳娜表面上是王后派来协助新领主的侍女，但她的真实身份远不止于此。她精通礼仪、情报收集和宫廷政治。\n\n随着故事深入，她与你之间的关系可能超越主仆。她的忠诚到底属于王后还是你？\n\n「有些事情，只有亲眼看到才能相信。」"),

        ("bishop", "主教马修斯", "教区主教", "#ffd700",
         "掌管艾登堡教区的虔诚教士，拥有巨大的精神影响力。",
         "马修斯是一个真正的信徒，他相信信仰的力量可以解决一切问题。但他也是一个精明的政治家，深谙如何利用教会的权威。\n\n他与你的父亲关系密切，似乎知道一些关于暗百合的秘密。\n\n「上帝的旨意不可违背，但解读权在我们手中。」"),

        ("baron", "冯·哈根男爵", "邻境贵族", "#2f4f4f",
         "野心勃勃的邻境领主，觊觎你的铁矿和领地。",
         "冯·哈根男爵是一个典型的旧贵族——傲慢、贪婪、但并非愚蠢。他的领地比你的大三倍，军事力量也更强。\n\n他一直在等待机会吞并艾登堡，你父亲的死给了他这个机会。但如果你展现出足够的实力，他也可能成为盟友。\n\n「弱者没有谈判的资格。」"),

        ("captain", "队长雷恩", "卫队队长", "#4682b4",
         "忠诚的卫队长，你在军事上最可靠的依仗。",
         "雷恩是一个出身平民的军人，凭借出色的战斗技巧和忠诚晋升为卫队长。他对贵族政治不太感兴趣，但绝对忠于艾登堡。\n\n他训练有素、纪律严明，在士兵中有极高的威望。\n\n「剑比言辞更诚实。」"),

        ("queen", "伊莎贝拉王后", "一国之母", "#800080",
         "睿智而强势的王后，在国王体弱时实际掌控着王国。",
         "伊莎贝拉王后是一个真正的政治家。她聪明、果断、无情——但也公正。她推行的政策大多是为了王国的利益，尽管手段有时令人不寒而栗。\n\n她对你的态度取决于你是否有用。在她眼中，每个人都是棋子。\n\n「王冠的重量，不是每个人都承受得起。」"),

        ("prince", "弗雷德里克王子", "王国继承人", "#4169e1",
         "年轻的王子，与王后的关系微妙。",
         "弗雷德里克是国王唯一的儿子，但他与母亲伊莎贝拉的关系并不好。他认为王后的铁腕统治正在扼杀王国的活力。\n\n他年轻、理想主义，渴望改变。但他是否有足够的能力和智慧来实现他的抱负？\n\n「这个王国需要的不是更多的铁腕，而是更多的信任。」"),

        ("lily_master", "暗百合首领", "秘密组织领袖", "#2d1b4e",
         "遍布王国的地下组织首领，身份神秘莫测。",
         "暗百合是一个存在了数百年的秘密组织，他们的目标——或者说他们声称的目标——是守护王国的平衡。\n\n首领的真实身份鲜为人知，但他/她显然掌握着许多不为人知的秘密，包括你父亲死亡的真相。\n\n「在阴影中，我们守望着光明。」"),

        ("merchant_karl", "商人卡尔", "行商巨贾", "#d2691e",
         "精明的商人，控制着地区的贸易网络。",
         "卡尔是一个白手起家的商人，他的商队遍布王国各地。他不关心政治——除非政治影响到他的生意。\n\n他可以成为你最有价值的经济盟友，但他的忠诚只属于金币。\n\n「每个人都有价格，区别只是货币不同。」"),
    ]

    ## 角色解锁状态（首次对话即解锁）
    def is_codex_unlocked(char_id):
        return char_id in persistent.gallery_unlocked


screen character_codex():
    tag menu
    use game_menu(_("角色图鉴"), scroll="viewport"):
        vbox:
            spacing 16

            ## 标题
            hbox:
                spacing 8
                text "*" size 24 color "#d4a942" yalign 0.5
                text "角色图鉴" size 26 color "#d4a942" font "msyh.ttf"

            $ _codex_unlocked = len([1 for cid, *_ in codex_characters if is_codex_unlocked(cid)])
            text "已解锁 [_codex_unlocked]/[len(codex_characters)] 位角色" size 14 color "#6a5e48"

            null height 10

            for char_id, char_name, char_title, char_color, char_brief, char_detail in codex_characters:
                $ _c_unlocked = is_codex_unlocked(char_id)

                frame:
                    xfill True
                    xpadding 20
                    ypadding 16
                    background Solid("#1a152840" if _c_unlocked else "#0f0d1a40")

                    if _c_unlocked:
                        button:
                            action Show("codex_detail", char_name=char_name, char_title=char_title, char_color=char_color, char_brief=char_brief, char_detail=char_detail, char_id=char_id)
                            xfill True
                            background None

                            hbox:
                                spacing 16
                                yalign 0.5

                                ## 角色头像框
                                frame:
                                    xsize 56
                                    ysize 56
                                    background Solid(char_color + "30")
                                    text char_name[0] xalign 0.5 yalign 0.5 size 26 color char_color font "msyh.ttf"

                                vbox:
                                    spacing 3
                                    text char_name size 20 color "#e0d8c8" font "msyh.ttf" bold True
                                    text char_title size 13 color "#8a7e60"
                                    text char_brief size 12 color "#6a5e48" xmaximum 550

                                ## 好感度
                                $ _codex_rel_var = "rel_" + ("aldric" if char_id == "aldric" else ("elena" if char_id == "elena" else ("bishop" if char_id == "bishop" else ("baron" if char_id == "baron" else ("captain" if char_id == "captain" else ("queen" if char_id == "queen" else ("prince" if char_id == "prince" else ("lily" if char_id == "lily_master" else ""))))))))
                                if _codex_rel_var:
                                    $ _codex_rel_val = getattr(store, _codex_rel_var, 0)
                                    vbox:
                                        xalign 1.0
                                        text "[_codex_rel_val]" size 16 color char_color bold True xalign 0.5
                                        text "好感" size 10 color "#6a5e48" xalign 0.5

                                text ">" xalign 1.0 yalign 0.5 size 16 color "#d4a94260"
                    else:
                        hbox:
                            spacing 16
                            yalign 0.5

                            frame:
                                xsize 56
                                ysize 56
                                background Solid("#0f0d1a")
                                text "?" xalign 0.5 yalign 0.5 size 26 color "#2a2040"

                            vbox:
                                spacing 3
                                text "???" size 20 color "#3a3040" font "msyh.ttf"
                                text "在游戏中遇到此角色后解锁" size 13 color "#2a2030"


## 角色详情弹窗
screen codex_detail(char_name="", char_title="", char_color="#d4a942", char_brief="", char_detail="", char_id=""):
    modal True
    zorder 250

    add Solid("#000000cc")

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 40
        ypadding 30
        xminimum 650
        xmaximum 700
        background Solid("#0f0d1af5")

        vbox:
            spacing 12

            ## 标题
            hbox:
                spacing 12
                frame:
                    xsize 52
                    ysize 52
                    background Solid(char_color + "30")
                    text char_name[0] xalign 0.5 yalign 0.5 size 24 color char_color font "msyh.ttf"
                vbox:
                    text char_name size 28 color char_color font "msyh.ttf" bold True
                    text char_title size 15 color "#8a7e60"

            add Solid("#d4a94230") xsize 1.0 ysize 1

            ## 详细介绍
            viewport:
                xfill True
                ysize 300
                mousewheel True
                draggable True

                text char_detail size 16 color "#c8b890" line_spacing 6

            add Solid("#d4a94220") xsize 1.0 ysize 1

            ## 关闭按钮
            textbutton "关闭":
                xalign 0.5
                text_size 18
                text_color "#8a7e60"
                text_hover_color "#d4a942"
                action Hide("codex_detail")

    key "K_ESCAPE" action Hide("codex_detail")
    key "mouseup_3" action Hide("codex_detail")


################################################################################
## 2. 决策日志系统 (Decision Journal)
################################################################################

default _decisions = []

init python:
    ## 决策记录: 列表 of (章节, 选择描述, 结果简述)
    ## 在剧情中通过 log_decision() 记录
    ## 使用 default 变量，确保决策日志随存档保存/加载

    def log_decision(chapter, choice, result=""):
        """记录一个决策。用法: $ log_decision("第一章", "选择外交手段", "与男爵达成停战")"""
        store._decisions.append((chapter, choice, result))

    def get_decisions():
        return store._decisions

    def get_decisions_by_chapter(ch):
        return [(c, choice, result) for c, choice, result in store._decisions if c == ch]

screen decision_journal():
    tag menu
    use game_menu(_("决策日志"), scroll="viewport"):
        vbox:
            spacing 16

            ## 标题
            hbox:
                spacing 8
                text "【卷】" size 24 color "#d4a942" yalign 0.5
                text "决策日志" size 26 color "#d4a942" font "msyh.ttf"

            $ _all_decisions = get_decisions()
            text "共 [len(_all_decisions)] 条决策记录" size 14 color "#6a5e48"

            null height 8

            if len(_all_decisions) == 0:
                frame:
                    xfill True
                    xpadding 24
                    ypadding 20
                    background Solid("#1a152840")
                    text "尚无决策记录。在游戏中做出选择后，你的每个重要决定都会被记录在这里。" size 16 color "#6a5e48" font "msyh.ttf"
            else:
                ## 按章节分组显示
                $ _chapters_seen = []
                for ch, choice, result in _all_decisions:
                    if ch not in _chapters_seen:
                        $ _chapters_seen.append(ch)

                for ch_name in _chapters_seen:
                    ## 章节标题
                    frame:
                        xfill True
                        xpadding 16
                        ypadding 8
                        background Solid("#d4a94210")
                        text ch_name size 18 color "#d4a942" font "msyh.ttf" bold True

                    $ _ch_decisions = get_decisions_by_chapter(ch_name)
                    for idx, (_c, _choice, _result) in enumerate(_ch_decisions):
                        frame:
                            xfill True
                            xpadding 20
                            ypadding 10
                            background Solid("#1a152820")

                            vbox:
                                spacing 4
                                hbox:
                                    spacing 8
                                    text "+" size 14 color "#d4a94280" yalign 0.0 yoffset 2
                                    text _choice size 16 color "#e0d8c8" font "msyh.ttf"
                                if _result:
                                    hbox:
                                        spacing 8
                                        text "  " size 14
                                        text "-> [_result]" size 13 color "#8a7e60"

            null height 16

            ## 提示
            frame:
                xalign 0.5
                xpadding 24
                ypadding 12
                background Solid("#1a152840")
                text "【提示】 每个决策都影响着故事的走向和最终结局" size 14 color "#8a7e60" font "msyh.ttf"


################################################################################
## 3. 地图系统 (Map)
################################################################################

init python:
    ## 地点数据: (id, 名称, 描述, x%, y%, 解锁章节, 图标)
    map_locations = [
        ("aidenburg", "艾登堡", "你的领地，一切故事的起点", 0.35, 0.55, None, "城"),
        ("border", "北方边境", "与冯·哈根男爵领地接壤的前线", 0.35, 0.18, "chapter1", "剑"),
        ("halenborg", "哈伦堡", "区域领主会议的举办地", 0.65, 0.40, "chapter2", "殿"),
        ("market", "哈伦堡集市", "繁华的商贸中心", 0.72, 0.50, "chapter2", "市"),
        ("forest", "黑暗密林", "暗百合的秘密据点所在", 0.20, 0.38, "chapter3", "林"),
        ("underground", "暗百合密室", "隐藏在地下的秘密组织总部", 0.22, 0.50, "chapter3", "穴"),
        ("church", "大教堂", "主教马修斯的教区中心", 0.50, 0.60, "chapter1", "堂"),
        ("capital", "王都", "王国的权力中心", 0.75, 0.25, "chapter4", "都"),
        ("palace", "王宫", "伊莎贝拉王后的宫殿", 0.80, 0.20, "chapter4", "宫"),
        ("garden", "宫廷花园", "王宫中宁静的花园", 0.85, 0.30, "chapter4", "园"),
        ("dungeon", "地牢", "阴暗的囚禁之所", 0.45, 0.72, "chapter4", "牢"),
        ("battlefield", "决战之地", "最终的战场", 0.50, 0.10, "chapter5", "刃"),
    ]

    def is_location_unlocked(req):
        if req is None:
            return True
        if persistent.chapters_completed and req in persistent.chapters_completed:
            return True
        ## 当前正在玩的章节也应该解锁之前的地点
        ch_order = ["chapter1", "chapter2", "chapter3", "chapter4", "chapter5"]
        if req in ch_order:
            idx = ch_order.index(req)
            for i in range(idx):
                if ch_order[i] in (persistent.chapters_completed or set()):
                    continue
            return True  # 宽松解锁：只要到达该章节即可
        return False

screen world_map():
    tag menu
    use game_menu(_("地图"), scroll=None):
        fixed:
            xsize 820
            ysize 560

            ## 地图底色
            add Solid("#0a0812") xsize 820 ysize 560

            ## 网格装饰
            for i in range(0, 820, 82):
                add Solid("#d4a94208") xpos i ypos 0 xsize 1 ysize 560
            for i in range(0, 560, 56):
                add Solid("#d4a94208") xpos 0 ypos i xsize 820 ysize 1

            ## 地图标题
            text "* 王国全境图" xpos 10 ypos 10 size 16 color "#d4a94260" font "msyh.ttf"

            ## 连接线（简化版）
            ## 艾登堡 -> 北方边境
            add Solid("#d4a94215") xpos 287 ypos 101 xsize 2 ysize 200
            ## 艾登堡 -> 教堂
            add Solid("#d4a94215") xpos 287 ypos 308 xsize 123 ysize 2
            ## 哈伦堡 -> 王都
            add Solid("#d4a94215") xpos 533 ypos 140 xsize 2 ysize 84

            ## 地点标记
            for loc_id, loc_name, loc_desc, lx, ly, loc_req, loc_icon in map_locations:
                $ _loc_unlocked = is_location_unlocked(loc_req)
                $ _lx = int(lx * 820)
                $ _ly = int(ly * 560)

                if _loc_unlocked:
                    button:
                        xpos _lx - 20
                        ypos _ly - 20
                        xsize 40
                        ysize 40
                        background None
                        action Show("map_location_detail", loc_name=loc_name, loc_desc=loc_desc, loc_icon=loc_icon)

                        vbox:
                            spacing 2
                            xalign 0.5
                            text loc_icon xalign 0.5 size 22
                            text loc_name xalign 0.5 size 10 color "#d4a942" font "msyh.ttf"
                else:
                    frame:
                        xpos _lx - 12
                        ypos _ly - 12
                        xsize 24
                        ysize 24
                        background Solid("#1a1528")
                        text "?" xalign 0.5 yalign 0.5 size 12 color "#2a2040"


## 地点详情弹窗
screen map_location_detail(loc_name="", loc_desc="", loc_icon=""):
    zorder 260
    modal True

    add Solid("#00000099")

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 40
        ypadding 30
        xminimum 400
        background Solid("#0f0d1af5")

        vbox:
            spacing 12
            xalign 0.5

            text loc_icon xalign 0.5 size 40
            text loc_name size 26 color "#d4a942" font "msyh.ttf" xalign 0.5 bold True
            add Solid("#d4a94230") xsize 300 ysize 1 xalign 0.5
            text loc_desc size 16 color "#c8b890" xalign 0.5 text_align 0.5

            null height 8

            textbutton "关闭":
                xalign 0.5
                text_size 16
                text_color "#8a7e60"
                text_hover_color "#d4a942"
                action Hide("map_location_detail")

    key "K_ESCAPE" action Hide("map_location_detail")
    key "mouseup_1" action Hide("map_location_detail")


################################################################################
## 4. 收藏品系统 (Collectibles)
################################################################################

init python:
    ## 收藏品数据: (id, 名称, 类型, 描述, 内容文本)
    collectible_items = {
        "letter_father_1": ("父亲的密信（一）", "信件",
            "在书房密室中发现的信件",
            "吾儿：\n\n当你读到这封信时，我恐怕已不在人世。有些事情，我一直不敢告诉你。\n\n暗百合并非你想象中的邪恶组织。他们存在了数百年，目的是维持王国的权力平衡。我年轻时加入了他们，但后来我发现，平衡的代价有时太过残忍。\n\n小心身边的人。\n\n——你的父亲"),

        "letter_father_2": ("父亲的密信（二）", "信件",
            "暗百合密室中的第二封信",
            "致我最亲爱的孩子：\n\n如果你已经找到了第一封信，那么你一定也到了暗百合的领地。\n\n关于我的死因——不要相信任何人的一面之词。真相往往隐藏在最不可能的地方。查一查主教的账本，看看教堂最近的捐款去了哪里。\n\n愿上帝保佑你。"),

        "poison_bottle": ("空毒药瓶", "物证",
            "在某个意想不到的地方发现的毒药瓶",
            "一个精致的玻璃小瓶，瓶身刻有炼金术符号。瓶内残留的紫色液体散发着微弱的甜味——这是「影之吻」毒药的特征。\n\n这种毒药无色无味，溶于酒中后几乎无法被察觉。中毒者会在数日内逐渐衰弱，看起来就像自然病亡。"),

        "baron_pact": ("男爵的秘密协议", "文件",
            "领主会议中截获的文件",
            "兹协议如下：\n\n甲方（冯·哈根男爵）承诺在新领主继位三个月内发动攻势，夺取艾登堡铁矿的控制权。\n\n乙方（已涂抹）承诺提供军饷支持，并在事成后分享铁矿收益的三成。\n\n签署日期：（你父亲去世前两周）"),

        "elena_locket": ("艾琳娜的挂坠", "饰品",
            "艾琳娜不小心遗落的挂坠盒",
            "一枚精致的银质挂坠盒，表面刻着王室的百合花纹。打开后里面有一幅微型肖像画——画中是一个年轻的女孩和一个穿着王室服装的女人。\n\n女孩的面容与艾琳娜极为相似，而那个女人...是年轻时的伊莎贝拉王后？"),

        "lily_symbol": ("暗百合徽章", "信物",
            "暗百合组织的身份标识",
            "一枚黑色的百合花形徽章，背面刻着一行古老的铭文：\n\n「Umbra Custos Lucis」\n\n——影是光的守护者。\n\n这枚徽章由某种不知名的金属铸造，触感冰凉，似乎永远不会变暖。据说只有核心成员才能拥有这样的徽章。"),

        "war_map": ("战争部署图", "文件",
            "最终决战前的军事部署",
            "一张详细的军事地图，标注了各方势力的兵力部署：\n\n• 艾登堡守军：约500人\n• 男爵军队：约1500人\n• 王室援军：视政治态度而定\n• 教会骑士：视信仰值而定\n• 暗百合暗杀小队：视关系而定\n\n地图边缘用红笔标注：「关键在于争取盟友。」"),

        "queen_decree": ("王后密令", "文件",
            "王后写给某人的秘密命令",
            "致忠诚的执行者：\n\n新任艾登堡领主的能力已经得到验证。根据观察报告，他（值得信任/需要监控）。\n\n继续执行原定计划。铁矿的归属关系到王国的军事命脉，不可让它落入不可控的势力手中。\n\n必要时...采取一切手段。\n\n——I.R."),
    }

    collectible_hints = {
        "war_map":         "据说压在某张旧桌的暗格里，很少有人记得去翻。",
        "lily_symbol":     "有些身份的证物，只有在最不经意的搜身里才会露出来。",
        "poison_bottle":   "一个空瓶子，被人藏在商人也会路过的地方。",
        "letter_father_1": "父亲生前没说出口的话，往往藏在最常去却最少被打扫的房间。",
        "letter_father_2": "另一封信，只有走进某个不该被知道的地方的人，才有机会看到。",
        "baron_pact":      "贵族之间的默契，总会在某场会议的角落留下一纸。",
        "queen_decree":    "只有走进她的宫殿，并且走得足够深的人，才碰得到这种东西。",
        "elena_locket":    "一枚遗落的挂坠盒。它的主人还没决定是否让你看到它。",
    }

    if persistent.collectibles_found is None:
        persistent.collectibles_found = set()

    def collect_item(item_id):
        """收集一个物品。用法: $ collect_item("letter_father_1")"""
        already_had = item_id in persistent.collectibles_found
        persistent.collectibles_found.add(item_id)
        if item_id in collectible_items:
            name = collectible_items[item_id][0]
            if already_had:
                renpy.show_screen("collectible_found_toast", item_name=name + "（已收集）")
            else:
                renpy.show_screen("collectible_found_toast", item_name=name)
            renpy.play("audio/sfx/ui_confirm.ogg", channel="sound")

screen collectible_found_toast(item_name=""):
    zorder 260

    frame at stat_toast_anim:
        xalign 0.5
        ypos 60
        background Solid("#1a1020ee")
        xpadding 28
        ypadding 12

        hbox:
            spacing 10
            text "【物】" size 18 yalign 0.5
            text "获得收藏品:" size 16 color "#8a7e60" font "msyh.ttf" yalign 0.5
            text item_name size 18 color "#d4a942" font "msyh.ttf" bold True yalign 0.5

    timer 3.0 action Hide("collectible_found_toast")


screen collectibles_screen():
    tag menu
    use game_menu(_("收藏品"), scroll="viewport"):
        vbox:
            spacing 16

            hbox:
                spacing 8
                text "【物】" size 24 color "#d4a942" yalign 0.5
                text "收藏品" size 26 color "#d4a942" font "msyh.ttf"

            $ _found = len(persistent.collectibles_found) if persistent.collectibles_found else 0
            $ _total = len(collectible_items)
            text "已收集 [_found]/[_total]" size 14 color "#6a5e48"

            bar:
                value StaticValue(_found, _total)
                xmaximum 400
                ysize 6
                left_bar Solid("#d4a942")
                right_bar Solid("#1a1528")

            null height 10

            ## 按类型分组
            $ _types_seen = []
            for _cid in collectible_items:
                $ _ctype = collectible_items[_cid][1]
                if _ctype not in _types_seen:
                    $ _types_seen.append(_ctype)

            for _type_name in _types_seen:
                ## 类型标题
                frame:
                    xfill True
                    xpadding 12
                    ypadding 6
                    background Solid("#d4a94210")
                    text _type_name size 16 color "#d4a942" font "msyh.ttf"

                for _cid in collectible_items:
                    $ _c_data = collectible_items[_cid]
                    if _c_data[1] == _type_name:
                        $ _c_found = _cid in persistent.collectibles_found

                        frame:
                            xfill True
                            xpadding 20
                            ypadding 12
                            background Solid("#1a152840" if _c_found else "#0f0d1a40")

                            if _c_found:
                                button:
                                    action Show("collectible_detail", item_name=_c_data[0], item_type=_c_data[1], item_desc=_c_data[2], item_text=_c_data[3])
                                    xfill True
                                    background None

                                    hbox:
                                        spacing 14
                                        yalign 0.5

                                        frame:
                                            xsize 40
                                            ysize 40
                                            background Solid("#d4a94220")
                                            text "【卷】" xalign 0.5 yalign 0.5 size 18

                                        vbox:
                                            spacing 2
                                            text _c_data[0] size 16 color "#e0d8c8" font "msyh.ttf" bold True
                                            text _c_data[2] size 12 color "#8a7e60"

                                        text ">" xalign 1.0 yalign 0.5 size 16 color "#d4a94260"
                            else:
                                hbox:
                                    spacing 14
                                    yalign 0.5
                                    frame:
                                        xsize 40
                                        ysize 40
                                        background Solid("#0f0d1a")
                                        text "?" xalign 0.5 yalign 0.5 size 18 color "#2a2040"
                                    vbox:
                                        text "???" size 16 color "#3a3040" font "msyh.ttf"
                                        text collectible_hints.get(_cid, "在游戏中探索发现") size 12 color "#2a2030"


## 收藏品详情
screen collectible_detail(item_name="", item_type="", item_desc="", item_text=""):
    modal True
    zorder 260

    add Solid("#000000cc")

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 40
        ypadding 30
        xminimum 600
        xmaximum 650
        background Solid("#0f0d1af5")

        vbox:
            spacing 12

            hbox:
                spacing 10
                text "【卷】" size 22 yalign 0.5
                vbox:
                    text item_name size 24 color "#d4a942" font "msyh.ttf" bold True
                    text "[item_type] — [item_desc]" size 13 color "#8a7e60"

            add Solid("#d4a94230") xsize 1.0 ysize 1

            viewport:
                xfill True
                ysize 300
                mousewheel True
                draggable True

                text item_text size 16 color "#c8b890" line_spacing 8

            add Solid("#d4a94220") xsize 1.0 ysize 1

            textbutton "关闭":
                xalign 0.5
                text_size 18
                text_color "#8a7e60"
                text_hover_color "#d4a942"
                action Hide("collectible_detail")

    key "K_ESCAPE" action Hide("collectible_detail")


################################################################################
## 5. 片尾字幕滚动 (Credits Roll)
################################################################################

screen credits_roll():
    zorder 300
    modal True

    add Solid("#0a0812")

    ## 滚动字幕
    viewport at credits_scroll_anim:
        xfill True
        ysize 720
        xalign 0.5

        vbox:
            spacing 20
            xalign 0.5
            null height 720

            ## 游戏标题
            text "权谋之庭" size 56 color "#d4a942" font "msyh.ttf" xalign 0.5 outlines [(3, "#000000cc", 0, 0)]
            text "Court of Shadows" size 24 color "#8a7e60" xalign 0.5
            add Solid("#d4a94240") xsize 300 ysize 1 xalign 0.5

            null height 40

            ## 制作团队
            text "— 制 作 —" size 18 color "#d4a942" xalign 0.5
            null height 10
            text "游戏设计 & 编程" size 14 color "#8a7e60" xalign 0.5
            text "小燚" size 22 color "#e0d8c8" font "msyh.ttf" xalign 0.5
            null height 20

            text "剧本 & 世界观" size 14 color "#8a7e60" xalign 0.5
            text "小燚" size 22 color "#e0d8c8" font "msyh.ttf" xalign 0.5
            null height 20

            text "UI/UX 设计" size 14 color "#8a7e60" xalign 0.5
            text "小燚 & Claude" size 22 color "#e0d8c8" font "msyh.ttf" xalign 0.5
            null height 20

            text "音乐 & 音效" size 14 color "#8a7e60" xalign 0.5
            text "小燚" size 22 color "#e0d8c8" font "msyh.ttf" xalign 0.5
            null height 40

            add Solid("#d4a94230") xsize 200 ysize 1 xalign 0.5
            null height 20

            ## 引擎
            text "— 技 术 —" size 18 color "#d4a942" xalign 0.5
            null height 10
            text "游戏引擎" size 14 color "#8a7e60" xalign 0.5
            text "Ren'Py 8.5.2" size 22 color "#e0d8c8" xalign 0.5
            null height 20

            text "AI 辅助开发" size 14 color "#8a7e60" xalign 0.5
            text "Claude (Anthropic)" size 22 color "#e0d8c8" xalign 0.5
            null height 40

            add Solid("#d4a94230") xsize 200 ysize 1 xalign 0.5
            null height 20

            ## 角色结局卡
            text "— 角 色 —" size 18 color "#d4a942" xalign 0.5
            null height 10

            for _cid, _cname, _ctitle, _ccolor, _cbrief, _cdetail in codex_characters:
                frame:
                    xalign 0.5
                    xpadding 30
                    ypadding 12
                    xminimum 400
                    background Solid("#1a152830")

                    hbox:
                        spacing 14
                        xalign 0.5
                        frame:
                            xsize 36
                            ysize 36
                            background Solid(_ccolor + "30")
                            text _cname[0] xalign 0.5 yalign 0.5 size 18 color _ccolor font "msyh.ttf"
                        vbox:
                            text _cname size 18 color _ccolor font "msyh.ttf"
                            text _ctitle size 12 color "#6a5e48"

            null height 40
            add Solid("#d4a94230") xsize 200 ysize 1 xalign 0.5
            null height 30

            ## 感谢
            text "— 特 别 感 谢 —" size 18 color "#d4a942" xalign 0.5
            null height 10
            text "感谢每一位玩家的支持" size 20 color "#c8b890" font "msyh.ttf" xalign 0.5
            text "你们的选择，造就了这个故事" size 16 color "#8a7e60" xalign 0.5
            null height 60

            ## 版权
            text "© 2026 小燚工作室" size 14 color "#4a4030" xalign 0.5
            text "All Rights Reserved" size 12 color "#3a3020" xalign 0.5

            null height 400

    ## 跳过提示
    frame:
        xalign 1.0
        yalign 1.0
        xoffset -20
        yoffset -20
        background Solid("#0a081280")
        xpadding 16
        ypadding 8
        text "点击跳过" size 13 color "#4a4030"

    key "mouseup_1" action Hide("credits_roll")
    key "K_ESCAPE" action Hide("credits_roll")
    key "K_SPACE" action Hide("credits_roll")

transform credits_scroll_anim:
    yoffset 0
    linear 45.0 yoffset -3000


################################################################################
## 6. 章节结束统计 (Chapter Summary)
################################################################################

init python:
    ## 记录章节开始时的属性快照
    _chapter_start_stats = {}

    def snapshot_chapter_start():
        """在章节开始时调用，记录初始属性"""
        _chapter_start_stats["power"] = store.power
        _chapter_start_stats["wealth"] = store.wealth
        _chapter_start_stats["faith"] = store.faith
        _chapter_start_stats["loyalty"] = store.loyalty
        _chapter_start_stats["reputation"] = store.reputation
        _chapter_start_stats["intrigue"] = store.intrigue

    def get_stat_delta(stat):
        """获取属性相对章节开始时的变化"""
        start = _chapter_start_stats.get(stat, 0)
        current = getattr(store, stat, 0)
        return current - start

screen chapter_summary(ch_name="第一章", ch_title="新主登基"):
    zorder 250
    modal True

    add Solid("#0a0812ee")

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 40
        xminimum 600
        background Solid("#0f0d1af5")

        vbox:
            spacing 14
            xalign 0.5

            ## 标题
            text "[ch_name] 完成" size 16 color "#8a7e60" xalign 0.5
            text ch_title size 32 color "#d4a942" font "msyh.ttf" xalign 0.5 outlines [(2, "#000000cc", 0, 0)]

            add Solid("#d4a94230") xsize 400 ysize 1 xalign 0.5

            null height 6

            ## 属性变化对比
            text "* 属性变化" size 18 color "#d4a942" font "msyh.ttf" xalign 0.5

            null height 4

            grid 2 3:
                spacing 10
                xalign 0.5

                for _stat_key, _stat_label, _stat_color in [("power", "权力", "#e74c3c"), ("wealth", "财富", "#f39c12"), ("faith", "信仰", "#9b59b6"), ("loyalty", "忠诚", "#3498db"), ("reputation", "声望", "#2ecc71"), ("intrigue", "谋略", "#7f8c8d")]:
                    $ _sd = get_stat_delta(_stat_key)
                    $ _sv = getattr(store, _stat_key, 0)
                    $ _s_sign = "+" if _sd > 0 else ""
                    $ _s_dcolor = "#2ecc71" if _sd > 0 else ("#e74c3c" if _sd < 0 else "#6a5e48")

                    frame:
                        xsize 240
                        xpadding 14
                        ypadding 8
                        background Solid("#1a152840")

                        hbox:
                            spacing 8
                            text _stat_label size 14 color "#e0d8c8" font "msyh.ttf" xsize 50
                            text "[_sv]" size 16 color _stat_color bold True xsize 30
                            if _sd != 0:
                                text "([_s_sign][_sd])" size 13 color _s_dcolor yalign 0.5

            null height 10

            ## 本章决策
            $ _ch_decs = get_decisions_by_chapter(ch_name)
            if len(_ch_decs) > 0:
                text "【卷】 本章决策" size 18 color "#d4a942" font "msyh.ttf" xalign 0.5
                for _dc, _dchoice, _dresult in _ch_decs:
                    hbox:
                        spacing 8
                        xalign 0.5
                        text "+" size 12 color "#d4a94280" yalign 0.0 yoffset 3
                        text _dchoice size 14 color "#c8b890"

            null height 14

            add Solid("#d4a94220") xsize 400 ysize 1 xalign 0.5

            textbutton "继续":
                xalign 0.5
                text_size 20
                text_color "#d4a942"
                text_hover_color "#ffd866"
                text_font "msyh.ttf"
                action Return()

    key "K_RETURN" action Return()
    key "K_SPACE" action Return()
    key "mouseup_1" action Return()

    ## 安全超时：30秒后自动继续
    timer 30.0 action Return()

## 便捷调用 label
label show_chapter_summary(ch_name="第一章", ch_title="新主登基"):
    call screen chapter_summary(ch_name, ch_title)
    return


################################################################################
## 7. New Game+ 系统
################################################################################

default persistent.ng_plus_unlocked = False
default persistent.ng_plus_bonus_power = 0
default persistent.ng_plus_bonus_wealth = 0
default persistent.ng_plus_bonus_intrigue = 0

init python:
    def activate_ng_plus():
        """通关后激活 New Game+"""
        persistent.ng_plus_unlocked = True
        ## 二周目奖励：保留 20% 的属性
        persistent.ng_plus_bonus_power = int(store.power * 0.2)
        persistent.ng_plus_bonus_wealth = int(store.wealth * 0.2)
        persistent.ng_plus_bonus_intrigue = int(store.intrigue * 0.2)

    def apply_ng_plus():
        """在新游戏开始时应用 New Game+ 奖励"""
        if persistent.ng_plus_unlocked:
            store.power += persistent.ng_plus_bonus_power
            store.wealth += persistent.ng_plus_bonus_wealth
            store.intrigue += persistent.ng_plus_bonus_intrigue
            clamp_stats()

screen ng_plus_banner():
    zorder 200

    frame at fade_in_up(0.5):
        xalign 0.5
        ypos 40
        background Solid("#1a1020ee")
        xpadding 28
        ypadding 12

        vbox:
            spacing 4
            xalign 0.5
            text "* New Game+" size 20 color "#ffd700" font "msyh.ttf" xalign 0.5
            text "二周目加成已生效" size 14 color "#d4a942" xalign 0.5
            hbox:
                spacing 16
                xalign 0.5
                if persistent.ng_plus_bonus_power > 0:
                    text "权力+[persistent.ng_plus_bonus_power]" size 12 color "#e74c3c"
                if persistent.ng_plus_bonus_wealth > 0:
                    text "财富+[persistent.ng_plus_bonus_wealth]" size 12 color "#f39c12"
                if persistent.ng_plus_bonus_intrigue > 0:
                    text "谋略+[persistent.ng_plus_bonus_intrigue]" size 12 color "#7f8c8d"

    timer 4.0 action Hide("ng_plus_banner")


################################################################################
## 8. 关键抉择倒计时 (Timed Choice)
################################################################################

default _timed_choice_remaining = 0
default _timed_choice_default = 0

screen timed_choice_timer(seconds=10):
    zorder 180

    $ _tc_pct = float(_timed_choice_remaining) / float(seconds) if seconds > 0 else 0.0
    $ _tc_color = "#2ecc71" if _tc_pct > 0.5 else ("#f39c12" if _tc_pct > 0.2 else "#e74c3c")

    frame:
        xalign 0.5
        ypos 8
        xsize 300
        background Solid("#0f0d1acc")
        xpadding 16
        ypadding 8

        vbox:
            spacing 4
            hbox:
                xfill True
                text "【时】 限时决策" size 13 color _tc_color font "msyh.ttf"
                text "[_timed_choice_remaining]秒" size 14 color _tc_color bold True xalign 1.0

            bar:
                value StaticValue(_tc_pct, 1.0)
                xfill True
                ysize 4
                left_bar Solid(_tc_color)
                right_bar Solid("#1a1528")

    timer 1.0 action If(_timed_choice_remaining > 1, SetVariable("_timed_choice_remaining", _timed_choice_remaining - 1), [Hide("timed_choice_timer"), Jump("_timed_choice_timeout")]) repeat True


## 用法示例 label:
## label some_timed_choice:
##     $ _timed_choice_remaining = 10
##     $ _timed_choice_default = 1  # 超时默认选第几个(0-based)
##     show screen timed_choice_timer(seconds=10)
##     menu:
##         "选项A":
##             ...
##         "选项B":
##             ...
##     hide screen timed_choice_timer
##     return

label _timed_choice_timeout:
    hide screen timed_choice_timer
    ## 超时时由调用方处理默认选择
    return


################################################################################
## 9. 辅助功能设置 (Accessibility)
################################################################################

default persistent.text_size_offset = 0
default persistent.high_contrast = False

init python:
    def apply_accessibility():
        """应用辅助功能设置"""
        offset = persistent.text_size_offset or 0
        style.default.size = 24 + offset
        style.say_dialogue.size = 24 + offset
        style.say_label.size = 26 + offset

screen accessibility_settings():
    tag menu
    use game_menu(_("辅助功能"), scroll="viewport"):
        vbox:
            spacing 20

            hbox:
                spacing 8
                text "【辅】" size 24 color "#d4a942" yalign 0.5
                text "辅助功能" size 26 color "#d4a942" font "msyh.ttf"

            null height 8

            ## 字体大小调节
            frame:
                xfill True
                xpadding 20
                ypadding 16
                background Solid("#1a152840")

                vbox:
                    spacing 10

                    text "字体大小" size 18 color "#e0d8c8" font "msyh.ttf"
                    text "调整游戏文字的显示大小" size 13 color "#6a5e48"

                    $ _ts_label = "标准" if persistent.text_size_offset == 0 else ("大" if persistent.text_size_offset == 4 else ("特大" if persistent.text_size_offset == 8 else "小"))
                    text "当前: [_ts_label]" size 14 color "#d4a942"

                    hbox:
                        spacing 12

                        $ _tc_small = "#d4a942" if persistent.text_size_offset == -2 else "#6a5e48"
                        textbutton "小":
                            text_size 16
                            text_color _tc_small
                            text_hover_color "#ffd866"
                            action SetField(persistent, "text_size_offset", -2)

                        $ _tc_std = "#d4a942" if persistent.text_size_offset == 0 else "#6a5e48"
                        textbutton "标准":
                            text_size 18
                            text_color _tc_std
                            text_hover_color "#ffd866"
                            action SetField(persistent, "text_size_offset", 0)

                        $ _tc_big = "#d4a942" if persistent.text_size_offset == 4 else "#6a5e48"
                        textbutton "大":
                            text_size 20
                            text_color _tc_big
                            text_hover_color "#ffd866"
                            action SetField(persistent, "text_size_offset", 4)

                        $ _tc_xl = "#d4a942" if persistent.text_size_offset == 8 else "#6a5e48"
                        textbutton "特大":
                            text_size 22
                            text_color _tc_xl
                            text_hover_color "#ffd866"
                            action SetField(persistent, "text_size_offset", 8)

            ## 高对比度
            frame:
                xfill True
                xpadding 20
                ypadding 16
                background Solid("#1a152840")

                vbox:
                    spacing 10
                    text "高对比度模式" size 18 color "#e0d8c8" font "msyh.ttf"
                    text "增强文字与背景的对比度，方便阅读" size 13 color "#6a5e48"

                    hbox:
                        spacing 16
                        $ _hc_on = "#d4a942" if persistent.high_contrast else "#6a5e48"
                        textbutton "开启":
                            text_size 16
                            text_color _hc_on
                            text_hover_color "#ffd866"
                            action SetField(persistent, "high_contrast", True)

                        $ _hc_off = "#d4a942" if not persistent.high_contrast else "#6a5e48"
                        textbutton "关闭":
                            text_size 16
                            text_color _hc_off
                            text_hover_color "#ffd866"
                            action SetField(persistent, "high_contrast", False)

            ## 自动文字速度
            frame:
                xfill True
                xpadding 20
                ypadding 16
                background Solid("#1a152840")

                vbox:
                    spacing 10
                    text "文字显示速度" size 18 color "#e0d8c8" font "msyh.ttf"
                    text "调整对话文字的显示速度" size 13 color "#6a5e48"

                    bar:
                        value Preference("text speed")
                        xmaximum 400
                        ysize 28
                        left_bar Solid("#d4a942")
                        right_bar Solid("#1a1528")

            ## 自动前进速度
            frame:
                xfill True
                xpadding 20
                ypadding 16
                background Solid("#1a152840")

                vbox:
                    spacing 10
                    text "自动前进速度" size 18 color "#e0d8c8" font "msyh.ttf"
                    text "自动前进模式下的等待时间" size 13 color "#6a5e48"

                    bar:
                        value Preference("auto-forward time")
                        xmaximum 400
                        ysize 28
                        left_bar Solid("#d4a942")
                        right_bar Solid("#1a1528")

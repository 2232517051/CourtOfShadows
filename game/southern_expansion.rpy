## ============================================================
## 南境游记 DLC — 第一弹《潮汐港的火并》
## ------------------------------------------------------------
## 独立外传：从主菜单进入，自包含小档，不依赖主线进度。
## 设定时点：本传主角治下某年，南境自由港来信求援。
## 当前为垂直切片（第一幕），后续幕次待扩。
## 美术：海港/沙滩/酒馆三张 bg + 商人公会立绘已有真素材；
##       女船长赛琳立绘暂用 safe_image 回退 noble_lady 占位，待生成 corsair.png。
## ============================================================

## ─── 南境 DLC 专用变量 ───
default southern_visited = False
default southern_quest_stage = 0
default southern_faction = ""              # "pirates" / "guild" / "neutral"
default alliance_pirates = False           # 倒向海盗议会（自由船主联盟）
default alliance_guild = False             # 倒向金锚商人公会
default southern_brokered_peace = False    # 促成停火
default rel_corsair = 0                    # 赛琳好感（-100~100）
default corsair_romance = False            # 赛琳恋爱 flag
default southern_first_impression = ""     # 酒馆初遇时玩家的态度
default southern_united = False            # 第三幕是否促成两派联合
default persistent.southern_dlc_progress = 0
## DLC 结局单独成 set，不混进主线 persistent.endings_seen（避免污染 8 结局图鉴计数）
default persistent.southern_endings_seen = set()

## ─── 南境 DLC 新角色 ───
## 渡鸦船长赛琳：自由船主联盟话事人之一，精明、盗亦有道，非刻板凶悍海盗
define corsair = Character("赛琳", color="#2e8b8b", image="corsair")
## 金锚公会大执事维斯帕：公会一方代表，复用现有 merchant_guild 立绘
define guild_master = Character("维斯帕执事", color="#b8860b", image="merchant_guild")
## 港口杂役/水手通用
define dockhand = Character("码头工", color="#8a8a8a", image="servant_generic")
define sailor = Character("水手", color="#6a7a8a", image="servant_generic")
## 自称中立的掮客费舍尔——实为王廷密探（第二幕揭）
define broker = Character("掮客费舍尔", color="#8a8a8a", image="noble_werner")
## 海雀号船上的少年水手
define ship_boy = Character("少年水手", color="#a89878", image="servant_generic")


## ============================================================
## 入口
## ============================================================

label southern_dlc_start:

    $ southern_visited = True
    $ quick_menu = True

    ## 外传设定在领主治下，主角已立足——给一个已成势的属性基线，
    ## 而非主线开局的新丁数值（否则 intrigue/reputation 门槛选项全为死枝）。
    python:
        power = 50
        wealth = 50
        faith = 45
        loyalty = 50
        reputation = 50
        intrigue = 45

    scene black with fade
    pause 0.5

    centered "{size=+8}南境游记{/size}"
    pause 1.2
    centered "{size=+4}第一弹 · 潮汐港的火并{/size}"
    pause 1.5
    scene black with dissolve

    ## ── 框架：一封来自南境的信 ──
    play music "audio/music/tension.ogg" fadeout 1.0 fadein 2.0 if_changed

    voice "audio/narration/south_a1_01.mp3"
    "信是奥尔德里克拿进来的。火漆上压着一个你没见过的纹章——一只铁锚，缠着绳。"

    $ hide_all_chars()
    show aldric_img at left with dissolve

    aldric "南边来的，大人。潮汐港。"

    player "潮汐港？那不是个不归王国管的港口吗。"

    aldric "正是因为不归王国管，他们才会来找您而不是找王廷。"

    aldric "信里说，港口里两伙人打起来了。金锚公会和那些……船主。他们封了码头。"

    "你接过信。字写得急，墨迹有几处晕开——像是边写边有人在催。"

    "落款是港务厅，但盖的是公会的章。"

    player "这跟艾登堡有什么关系？"

    aldric "大人，艾登堡的盐，三成走南境海路。铁器的好钢，也是。"

    aldric "潮汐港停一个月，您冬天就得拿木柴腌肉。"

    "你心里算了下府库的存盐。撑不到开春。"

    player "备马。不，备船。"

    aldric "……我这把老骨头，怕是要在甲板上吐三天。"

    player "那就留下看家。我自己去。"

    aldric "那不行。您一个人去那种地方，我夜里睡不着。"

    "他还是收拾了行李。第二天天没亮，你们就上了路。"

    pause 0.5
    scene black with dissolve


    ## ============================================================
    ## 第一幕 · 抵港
    ## ============================================================

    play music "audio/music/southern_port.ogg" fadeout 1.5 fadein 2.0 if_changed

    scene bg tideport_beach with fade
    pause 0.3

    voice "audio/narration/south_a1_02.mp3"
    "海风先到。咸的，还带着鱼和焦油的味道。"

    voice "audio/narration/south_a1_03.mp3"
    "你这辈子没见过这么多船。桅杆挤在一起，像一片被砍秃了的林子。"

    show aldric_img at left with dissolve

    aldric "到了。这就是潮汐港。"

    "远处的码头拉着铁链，几艘船横在港口入口。没人卸货，也没人出海。"

    aldric "您看那边——链子锁着码头。封港了。"

    "岸上的人不少，可没人忙活。他们三三两两站着，手都揣在怀里。揣着什么，你不想猜。"

    scene bg tideport_harbor with dissolve

    "你们沿着栈道往里走。木板被海水泡得发黑，每一步都黏脚。"

    dockhand "外乡人？挑日子来的不巧。"

    "一个码头工挡了一下路，又自己让开了。他看了眼你腰间的印戒。"

    dockhand "内陆来的贵人。来收账还是来送死？"

    player "来谈事的。"

    dockhand "那更得小心。这港口现在，谈事比动刀危险。"

    "他啐了一口，走了。"

    aldric "大人，我们先找个地方落脚，打听清楚再说。"

    aldric "前头有家酒馆，叫'断锚'。听名字就知道，是船上人聚的地方。"

    player "那就去断锚。"

    pause 0.3
    scene black with dissolve


    ## ============================================================
    ## 第一幕 · 断锚酒馆 · 初遇赛琳
    ## ============================================================

    play music "audio/music/southern_tavern.ogg" fadeout 1.5 fadein 1.5 if_changed

    scene bg tideport_tavern with fade
    pause 0.3

    "酒馆里比外头活络。火光、烟、湿羊毛和烈酒的味道。一个角落有人在掷骰子，另一个角落有人在低声谈一笔不能见光的买卖。"

    "你刚找了张桌子坐下，就听见门口一阵安静。"

    "进来一个女人。她不高，可整间屋子的目光都往她身上落——然后又赶紧移开。"

    show corsair_img at right with dissolve

    "她外套的下摆湿了一圈，靴子上沾着没干的盐渍。腰上挂着一把弯刀，刀鞘磨得发亮，那是常拔的痕迹。"

    "她扫了一圈，目光在你这张生面孔上停了半秒，又收了回去。她走到吧台，敲了两下。"

    corsair "老样子。还有，那桌内陆来的——他们的账记我头上。"

    "她没回头，却显然是说你。"

    menu:
        "起身道谢，自报家门":
            $ southern_first_impression = "polite"
            $ change_rel("rel_corsair", 8)
            $ hide_all_chars("corsair_img")
            show player_char_img at left with dissolve

            player "多谢。在下艾登堡领主[player_name]。敢问恩人名号？"

            "她这才转过身，挑了挑眉。"

            corsair "领主。真稀奇，王国的贵人肯站起来跟我说话。"

            corsair "赛琳。这港口里，他们叫我渡鸦。"

            corsair "至于恩人——一杯酒的事，别记太重。我只是不喜欢看人挨宰。"

        "不动声色，先看她想做什么":
            $ southern_first_impression = "wary"
            $ change_rel("rel_corsair", 3)

            "你没动。一杯来路不明的酒，背后总挂着价钱。你想先看清这价钱是什么。"

            "她端着酒走过来，自己拉开你对面的椅子坐下。"

            show player_char_img at left with dissolve

            corsair "聪明。换我也不喝陌生人的酒。"

            corsair "赛琳。渡鸦。这港口里没几个内陆人敢这么稳地坐着——你要么是有底气，要么是不知道自己踩进了什么。"

            player "那要看你接下来想说什么。"

            corsair "我喜欢这话。"

        "直接问她：封港是不是你们干的":
            $ southern_first_impression = "blunt"
            $ change_rel("rel_corsair", -3)
            $ change_rel("rel_corsair", 6)

            "你没绕。"

            show player_char_img at left with dissolve

            player "码头上的铁链，是你们船主联盟锁的吗？"

            "酒馆里近处几桌的声音低了下去。她端酒的手停在半空，看了你一会儿，笑了。"

            corsair "开门见山。我喜欢，也讨厌。"

            corsair "链子不是我们锁的，是公会锁的。他们说要'保护港口秩序'。"

            corsair "可你这么问，说明你已经听了一边的话。坐下，听听另一边的。"

            corsair "赛琳。渡鸦。坐。"

    $ hide_all_chars("corsair_img")
    show corsair_img angry at right with dissolve

    ## ── 赛琳交代局势 ──
    corsair "我猜你是冲着海路来的。盐、铁、好钢——内陆领主能为这些跑这么远，不奇怪。"

    player "码头封一天，我冬天就难过一分。我想知道这港口到底出了什么事。"

    corsair "出了什么事？金锚公会想把整个港口攥进自己手里。"

    corsair "他们控制码头、定价、放贷。以前我们这些船主交一笔泊费，进出自由。现在他们要抽两成货，还要登记每一票买卖。"

    corsair "登记。你懂这两个字在港口意味着什么吗——意味着以后哪条船能出海，由公会说了算。"

    corsair "上个月,有条船不肯登记。公会说它'走私',扣了船,人到现在没放。我们去要人,他们就锁了码头,说是我们先动的手。"

    corsair "所以现在港口里两伙人对着干。他们有港务厅和钱，我们有船和刀。"

    "她喝了一口，把杯子搁下。"

    corsair "你来得正好，也来得正不是时候。"

    corsair "公会那边的大执事，维斯帕，今晚就想见你。他们消息比海鸥还灵。"

    pause 0.3


    ## ============================================================
    ## 第一幕 · 维斯帕登场
    ## ============================================================

    "话音没落，酒馆的门又开了。这次进来的人不一样——绸面的外袍，干燥的靴子，身后跟着两个不像水手的随从。"

    show corsair_img at right with dissolve
    show guild_master_img at left with dissolve

    corsair "说曹操。"

    guild_master "渡鸦船长。又在用酒收买人心。"

    guild_master "还有这位——艾登堡的领主。久仰。金锚公会大执事，维斯帕。"

    "他对你欠了欠身，礼数周到，眼睛却一直在量你腰上的印戒值多少钱。"

    guild_master "船长跟您说的，大概是'公会要吞了港口'这一套吧。"

    guild_master "我换个说法。这港口三百年没有王法，谁拳头硬谁说话。船多的劫船少的，没靠山的连泊位都抢不到。"

    guild_master "公会做的事，是给它立规矩。登记、抽税、护航。乱港变商港。"

    corsair "立规矩。规矩立完，规矩就是你。"

    guild_master "至少我的规矩写在纸上，船长。你的规矩在刀上。"

    "两个人都不再看对方，都看着你。"

    guild_master "领主大人，您要的是稳定的海路。能给您稳定的，是秩序，不是一群随时会翻脸的船主。"

    guild_master "站在公会这边。我们保您艾登堡的盐铁优先放行，价钱也好谈。"

    corsair "他没告诉你'优先'的意思——意思是别人靠后。今天他给你优先，明天换个出价更高的，你就是那个靠后的。"

    corsair "跟我们走。船主认人不认章。你帮我们撬开公会的手，这港口的船，以后认艾登堡的旗。"

    "两边都把话放下了。现在轮到你。"

    pause 0.5

    ## ============================================================
    ## 第一幕 · 核心抉择
    ## ============================================================

    menu:
        "站公会——秩序能保海路（倾向 财富/谋略）":
            $ southern_faction = "guild"
            $ alliance_guild = True
            $ change_rel("rel_corsair", -15)
            $ log_decision("南境游记", "在潮汐港选择支持金锚公会")
            $ change_stat("wealth", 5)

            $ hide_all_chars()
            show guild_master_img at left with dissolve

            player "我要的是十年都不断的海路。船主今天讲义气，明天可能就把货卖给出价高的人。"
            player "公会有账本，有章程。我跟有章程的人打交道。"

            guild_master "明智。艾登堡不会后悔。"

            "维斯帕笑了。那笑容里没有高兴，只有'又算对了一笔'的满足。"

            $ hide_all_chars()
            "门口传来椅子翻倒的声音。你回头，赛琳已经走了。门还在晃。"

            "维斯帕替你斟上酒。赛琳的位子空着，椅子倒在地上，没人去扶。"

        "站船主——自由的港才认你的旗（倾向 声望/勇气）":
            $ southern_faction = "pirates"
            $ alliance_pirates = True
            $ change_rel("rel_corsair", 18)
            $ log_decision("南境游记", "在潮汐港选择支持自由船主联盟")
            $ change_stat("reputation", 5)

            $ hide_all_chars()
            show corsair_img at right with dissolve

            player "公会的规矩写在纸上，纸是他们印的。"
            player "我宁可跟认人的人打交道。船主联盟，艾登堡跟你们走。"

            corsair "……我以为内陆的贵人都只会算盐价。"

            corsair "你算的是别的。行。这杯我陪你喝。"

            "她把刀往桌上一搁，第一次真正坐了下来。维斯帕的脸沉了，他没再说话，带着随从退了出去。"

            "她替你满上酒，又给自己满上。这一坛，你们一人一半。"

        "都不站——把两边按在一张桌子上谈（需 谋略≥45 或 声望≥45）" if intrigue >= 45 or reputation >= 45:
            $ southern_faction = "neutral"
            $ southern_brokered_peace = True
            $ change_rel("rel_corsair", 12)
            $ log_decision("南境游记", "在潮汐港试图斡旋停火")
            $ change_stat("intrigue", 4)

            $ hide_all_chars()
            show corsair_img at right with dissolve
            show guild_master_img at left with dissolve

            player "你们两个都想拉我站队。可我站哪边，哪边赢，输的那边就掀桌子——港口照样停。"
            player "我要的是港口开着。所以我谁都不站。"

            guild_master "那您来这一趟，图什么？"

            player "图你们俩今晚坐下来，把扣的船和锁的链子,一样换一样。"

            corsair "他放人，我们就撤链子？"

            player "他先放一半人，你们先撤一半链子。剩下的，明天我看着你们换。"

            "维斯帕和赛琳都没立刻答应。可两个人都没走——在这种地方，不走，就是在听。"

            corsair "……内陆来的，倒会算。"

            guild_master "暂且听听。但只是暂且。"

            "没人赢，也没人掀桌子。维斯帕留了两个随从盯着，赛琳的刀还搁在桌上没收。明天的事，明天再说。"

        "先不表态，今晚我要自己去码头看看（谨慎）":
            $ southern_faction = ""
            $ change_rel("rel_corsair", 5)
            $ log_decision("南境游记", "暂不选边，决定先自行查证")

            $ hide_all_chars()
            "你两边都没应。"

            player "两位的话我都听了。可我谁的话都还没信。"
            player "今晚我自己去码头看看那条铁链，看看那些扣下的船。明天再给二位答复。"

            guild_master "……谨慎。也行。希望您看见的，跟您听见的一样。"

            corsair "随你。不过夜里的码头不安全，外乡人。"
            corsair "要去，带上这个。"

            "她解下腰间一枚铜哨，丢给你。"

            corsair "吹响它，附近水里要是有我的人，会来。要是没有——那就跑快点。"

            $ change_rel("rel_corsair", 5)
            "你接住了哨子。冰凉，边缘有牙印——被人紧张地咬过很多次。"

    pause 0.5
    $ southern_quest_stage = 1
    $ persistent.southern_dlc_progress = 1

    ## ============================================================
    ## 第一幕收束 + 钩子
    ## ============================================================

    $ hide_all_chars()
    scene black with fade
    pause 0.5

    "那天夜里，你没睡好。有件事对不上。"

    "公会说船主先动的手。船主说公会先扣的船。两边都信誓旦旦，可没有一个人，说得出第一刀是谁先捅的。"

    "好像有谁，特意不让这个问题有答案。"

    if southern_faction == "guild":
        "你站了公会。可维斯帕算账太顺了，顺得像早就排好了。"
    elif southern_faction == "pirates":
        "你站了船主。可赛琳要的'撬开公会的手'，听着也太急了点。"
    elif southern_faction == "neutral":
        "你压着两边谈了。可越谈你越觉得，他们俩谁都不想真打——是别人想让他们打。"
    else:
        "你谁都没站。明天天一亮，你就去那条铁链和那些扣下的船边上，自己看。"

    pause 1.5
    scene black with dissolve

    centered "{size=+5}第一幕 · 完{/size}"
    pause 1.5

    $ unlock_southern_milestone()

    jump southern_act2


## ── DLC 第一弹结束界面 ──
screen southern_dlc_return():
    modal True
    zorder 200
    add Solid("#0a0812f0")

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 40
        ypadding 30
        background Solid("#1a1528f0")

        vbox:
            spacing 18
            xalign 0.5

            text "南境游记 · 第一弹到此结束" size 24 color "#d4a942" font "msyh.ttf" xalign 0.5

            text "感谢试玩。你在潮汐港的选择已记录，将影响后续幕次。" size 15 color "#c8b890" font "msyh.ttf" xalign 0.5

            null height 6

            textbutton "返回主菜单":
                xalign 0.5
                text_size 20
                text_color "#d4a942"
                text_hover_color "#ffd866"
                action MainMenu(confirm=False)


## ── DLC 进度里程碑 ──
init python:
    def unlock_southern_milestone():
        ## southern_act1 已在 characters.rpy 的 achievement_data 正式注册
        unlock_achievement("southern_act1")

    def southern_finish(ending_key, achievement):
        """登记 DLC 结局：独立 set + 成就 + 解锁画廊，不碰主线 endings_seen。"""
        persistent.southern_endings_seen.add(ending_key)
        unlock_achievement(achievement)
        if corsair_romance:
            unlock_achievement("southern_lover")
        ## 解锁场景画廊 + 赛琳肖像（六张场景在任意路线都会出现在结局前）
        for _g in ("bg_tideport_harbor", "bg_tideport_beach", "bg_tideport_tavern",
                   "bg_tideport_ship", "bg_tideport_office", "bg_tideport_fleet", "corsair"):
            unlock_gallery(_g)

    ## 结局路线图用：(key, 名称, 描述, 颜色, 图标)
    _southern_ending_info = [
        ("free",  "自由港",     "促成联合，潮汐港自治存续",   "#2e8b8b", "港"),
        ("ruler", "港口新主",   "倒向一方，掌港却失其自由",   "#b8860b", "旗"),
        ("fall",  "潮汐港陷落", "卖港换盐路，自由港覆灭",     "#3d3a36", "灰"),
    ]


## ============================================================
## 第三幕 · 潮信
## ------------------------------------------------------------
## 王军压境的高潮 + 3 分歧结局：
##   自由港(联合/最佳) · 港口新主(倒向一方/bittersweet) · 陷落(坏)
## 由第一幕站队 + 本幕最终抉择 + 属性/恋爱共同决定。
## ============================================================

label southern_act3:

    play music "audio/music/southern_scheme.ogg" fadeout 1.0 fadein 1.5 if_changed
    scene bg tideport_tavern with fade
    pause 0.3

    centered "{size=+6}第三幕 · 潮信{/size}"
    pause 1.2
    scene bg tideport_tavern with dissolve

    voice "audio/narration/south_a3_01.mp3"
    "天一亮，断锚酒馆成了临时的议事厅。门口有船主的人把守，桌上摊着港口的海图。"

    voice "audio/narration/south_a3_02.mp3"
    "你、维斯帕、赛琳，三个人围着那张图。昨天还要拔刀，今天得在傍晚之前想出活路。"

    show corsair_img at right with dissolve
    show guild_master_img at left with dissolve

    guild_master "港务厅那帮老爷已经在备茶水彩绸，准备开门迎王师了。在他们眼里，换个主子而已。"

    corsair "我的船能堵航道。可我有三条快船，对面是一支分舰队。堵得了一时，堵不住。"

    corsair "硬打，我们没赢面。"

    ## ── 破局点：否认借口（高谋略玩家自己想到，否则由 NPC 点破）──
    if intrigue >= 50:
        player "那就不打。"

        "两个人都看你。"

        player "王军要的是'平乱'这个名义。港口乱，他们进来才叫平乱。"
        player "可要是傍晚他们到的时候，整个港口好端端的，人人站在码头上，秩序得像过节——他们一炮打过来，那就不是平乱，是当着全海域的面屠港。"

        player "王廷丢不起这个脸。别的自由港会看，给王国跑海运的商会也会看。"

        guild_master "……让他们师出无名。"
    else:
        player "总有破法。他们千里压过来，图的是什么？"

        guild_master "图一个名义。'平乱'。"

        guild_master "潮汐港乱，他们才进得来。这道理我做了半辈子生意，反倒是今早才想透——他们要的从来不是赢，是我们先乱给他们看。"

        corsair "所以要是港口不乱呢？要是傍晚他们到的时候，整个港好端端的，人都齐齐站在码头上？"

        guild_master "那一炮打下来，就不是平乱，是屠港。王廷丢不起这个脸。"

    "海图上那支正在逼近的舰队，第一次显得没那么不可战胜。"

    "可办法归办法。要让整个港口一条心站出来——公会和船主，得先把刀收回鞘里。这一步，落在你身上。"

    pause 0.5

    ## ============================================================
    ## 第三幕 · 最终抉择
    ## ============================================================

    menu:
        "促成联合——让整个港口站成一条心，逼王军师出无名":
            $ log_decision("南境游记", "第三幕：促成两派联合，否认王军借口")

            ## 联合是否成功：调停过 / 声望或谋略够 / 恋爱加成
            if southern_brokered_peace or reputation >= 50 or intrigue >= 50 or corsair_romance:
                $ southern_united = True
                jump ending_southern_free
            else:
                "你想把两边拧到一处。可你昨天站得太偏，话说出口，另一半人不信。"
                "公会和船主在最后关头还是各按各的算盘。整齐的港口没站成，站成了两摊。"
                $ southern_united = False
                jump ending_southern_ruler

        "靠你站定的那一方硬抗，用港口的地利拼一场" if southern_faction == "guild" or southern_faction == "pirates":
            $ log_decision("南境游记", "第三幕：倒向一方武力对抗王军")
            $ southern_united = False
            jump ending_southern_ruler

        "给王军主帅递话——用艾登堡的名义换盐路特许，保自己":
            $ log_decision("南境游记", "第三幕：与王军私下交易，出卖港口")
            jump ending_southern_fall


## ============================================================
## 结局一 · 自由港（联合 / 最佳）
## ============================================================

label ending_southern_free:

    $ hide_all_chars()
    play music "audio/music/southern_fleet.ogg" fadeout 1.5 fadein 2.0 if_changed
    scene bg tideport_fleet with fade

    "傍晚。王军的桅灯排成一道墙，压到了港口外的浅水线。"

    scene bg tideport_harbor with dissolve

    "可码头上没有慌乱。"

    "公会的账房、船主的水手、卖鱼的、补帆的、开酒馆的——全站出来了。一排一排，沿着栈桥站得整整齐齐，像在等一场仪式，不像在等一场仗。"

    show corsair_img at right with dissolve
    show guild_master_img at left with dissolve

    "你站在最前头。手里是费舍尔烧剩的半卷文书，和维斯帕连夜从港务厅翻出的往来账。"

    "你早把消息递了出去——递给昨夜过港的他国商船，递给下游两个自由港。此刻港口外，除了王军的船，还泊着十几条挂着各色旗号的商船，都在看。"

    "王军特使乘小艇上岸。他准备好的说辞是'应港务厅之请，入港平乱'。可他眼前的港口，没有乱。"

    player "特使大人。乱在哪里？请指给这些船看。"

    "你把那半卷文书举起来。火烧的焦边底下，是王廷密探费舍尔的手记——怎么递假密报给公会，怎么劝船主动手，怎么把一个空盐船说成军火船。"

    player "第一刀不是公会捅的，也不是船主捅的。是你们的人，费舍尔。点完火，他跑了。"

    "岸上十几条商船的人都听见了。特使的脸白了一层。"

    "他要么下令开炮——当着全海域，炮轰一个秩序井然的自由港；要么撤。"

    "这个名声，王廷担不起。"

    pause 0.8

    "桅灯，一盏一盏，掉头了。"

    play music "audio/music/southern_freeport.ogg" fadeout 2.0 fadein 2.0 if_changed
    scene bg tideport_beach with dissolve

    "舰队退到海平线以下那天，港口的铁链解开了。海雀号第一个出港，少年水手在桅杆上冲岸边挥手。"

    "公会和船主坐下来，重立了港约：登记取消，泊费照旧，船主在港务厅有了一席。维斯帕和赛琳谁都没全赢——可港口开着，三百年的自由还在。"

    show guild_master_img at left with dissolve
    guild_master "领主大人，艾登堡的盐铁，往后在潮汐港优先放行。这次不是施舍，是港口欠您的。"

    $ hide_all_chars()

    if corsair_romance:
        show corsair_img at right with dissolve
        corsair "盐路的事，公会算他们的。我算我的。"

        corsair "下一趟你的盐船北上，我亲自押。我想看看艾登堡的雪——听说内陆的雪，落在海上化得慢。"

        "她说完，把那枚你还回去的铜哨又塞回你手里。"

        corsair "留着。下回你吹响它，我从哪片海都给你赶过来。"

        "渡鸦船长说话算话。这一点，整片南海都知道。"
    else:
        show corsair_img happy at right with dissolve
        corsair "你这内陆来的，搅了一池子浑水，又替我们澄清了。"

        corsair "记住断锚的门朝哪开。下回来，酒还是记我账上。"

    pause 0.5
    $ hide_all_chars()
    scene black with dissolve

    centered "{size=+8}自由港{/size}"
    pause 1.2
    centered "{size=+3}潮汐港照旧是谁都能进、谁都不属于的港。{/size}"
    pause 1.0
    centered "{size=+3}你没有拿走它。你只是让它，还是它自己。{/size}"
    pause 2.0

    $ southern_finish("free", "southern_free")
    jump southern_dlc_complete


## ============================================================
## 结局二 · 港口新主（倒向一方 / bittersweet）
## ============================================================

label ending_southern_ruler:

    $ hide_all_chars()
    play music "audio/music/southern_fleet.ogg" fadeout 1.5 fadein 2.0 if_changed
    scene bg tideport_fleet with fade

    "傍晚。王军压到港外。你没有整个港口，你只有半个。"

    if southern_faction == "pirates":
        "船主联盟的快船倾巢而出。赛琳的渡鸦号当先，借着对暗礁和潮汐的熟，在王军的大船之间穿来穿去，放火、撞舵、割锚索。"
        "公会的人缩在账房里，没动。"
    elif southern_faction == "guild":
        "公会砸下重金，雇光了港里所有能拿刀的人，又用钱买通了王军里几个押粮的军官，让他们的火药受了潮。"
        "船主们冷眼旁观，没帮你——你昨天站了公会，今天他们凭什么帮你。"
    else:
        "你临时拢起一支杂凑的队伍。可港口没有一条心，各打各的。"

    "这一仗，王军没占到便宜，到底撤了。可港口也烧塌了小半。"

    pause 0.5
    scene bg tideport_beach with dissolve

    "硝烟散尽，潮汐港还在——只是它变了。"

    "另一半人被你压了下去。从今往后，谁能进港、谁能出海、谁说了算，由你定。港务厅挂上了艾登堡的金鹰旗。"

    "船照常进出，货照常装卸。你的盐路，从此稳稳当当。"

    if corsair_romance and southern_faction == "pirates":
        $ hide_all_chars()
        show corsair_img sad at right with dissolve
        corsair "我们赢了。可你看这港口……它现在有主人了。"
        corsair "我跟了你，不后悔。只是往后再有人说'潮汐港是自由港'，我大概会笑一声。"
        "她没再说下去。有些东西保住了，有些东西，是保不住的。"
    else:
        "你成了潮汐港实际的主人。一个三百年没有主人的港口，现在有了。"
        "夜里你站在港务厅的窗前，听着外头照旧的喧闹。喧闹是真的。自由不是了。"

    pause 0.5
    $ hide_all_chars()
    scene black with dissolve

    centered "{size=+8}港口新主{/size}"
    pause 1.2
    centered "{size=+3}你保住了潮汐港。它开着，认你的旗。{/size}"
    pause 1.0
    centered "{size=+3}只是它不再是谁都能自由进出的那个港了。{/size}"
    pause 2.0

    $ southern_finish("ruler", "southern_ruler")
    jump southern_dlc_complete


## ============================================================
## 结局三 · 潮汐港陷落（坏）
## ============================================================

label ending_southern_fall:

    $ hide_all_chars()
    play music "audio/music/southern_fleet.ogg" fadeout 1.5 fadein 2.0 if_changed
    scene bg tideport_fleet with fade

    "你没等到傍晚。"

    "午后，你乘小艇出港，登上了王军旗舰。你给主帅递了话：艾登堡无意搅进港口的乱局，只求一纸盐铁特许。"

    "主帅很满意。一个内陆领主肯让路，比一场仗省事得多。"

    "傍晚，王军不费一炮进了港。港务厅开门迎接，彩绸铺到了栈桥上。"

    "公会被'整编'，维斯帕成了王廷的港务官，绸袍换了官袍，脸上没什么两样。"

    "船主联盟被定为'海寇'。抓的抓，散的散。"

    show corsair_img sad at right with dissolve

    if corsair_romance:
        corsair "原来你北上那条盐路，比这一港的人都重。"
        corsair "也好。各为其主。"
        "她看你的眼神里没有恨，那比恨更难受。然后她转身上了渡鸦号。"
        "据说渡鸦号冲出了封锁线。据说。从此南海上再没人见过那面挂着渡鸦的黑帆。"
    else:
        "听说渡鸦号在合围里冲出了一个缺口，扯着破帆遁进了夜雾。听说而已。"
        "从此南海上，再没人见过那面黑帆。"

    pause 0.5
    $ hide_all_chars()
    scene bg tideport_beach with dissolve

    "你回到艾登堡那天，盐车正好进城。满满当当，价钱比往年还低。"

    "你的盐路稳了——稳稳地捏在王廷手里。比从前更稳，也比从前更不由你。"

    pause 0.5
    scene black with dissolve

    centered "{size=+8}潮汐港陷落{/size}"
    pause 1.2
    centered "{size=+3}你保住了艾登堡的盐。{/size}"
    pause 1.0
    centered "{size=+3}潮汐港，连同那面黑帆，没了。{/size}"
    pause 2.0

    $ southern_finish("fall", "southern_fall")
    jump southern_dlc_complete


## ============================================================
## DLC 通关结算
## ============================================================

label southern_dlc_complete:

    $ persistent.southern_dlc_progress = 3
    $ southern_quest_stage = 3

    scene black with dissolve
    pause 0.5

    python:
        _seen = len(persistent.southern_endings_seen)
    centered "{size=+4}南境游记 · 第一弹 完{/size}"
    pause 1.0
    centered "{size=+3}潮汐港结局收集：[_seen]/3{/size}"
    pause 1.0
    if _seen >= 3:
        centered "{size=+3}你已看遍潮汐港的三种命运。{/size}"
        pause 1.2
    centered "{size=+3}——后续卷次开发中——{/size}"
    pause 2.0

    call screen southern_dlc_return


## ============================================================
## 第二幕 · 第一刀
## ------------------------------------------------------------
## 揭"第三方挑动"：王廷想借两派火并吞港。
## 含赛琳恋爱线门槛（rel_corsair >= 30 触发 confirm，>= 80 深化）。
## ============================================================

label southern_act2:

    play music "audio/music/harbor_waves.ogg" fadeout 1.0 fadein 2.0 if_changed

    scene bg tideport_harbor with fade
    pause 0.3

    centered "{size=+6}第二幕 · 第一刀{/size}"
    pause 1.2
    scene bg tideport_harbor with dissolve

    voice "audio/narration/south_a2_01.mp3"
    "天没亮你就醒了。海雾压在桅杆上，整个港口像泡在一碗冷汤里。"

    voice "audio/narration/south_a2_02.mp3"
    "你要找的那条船，叫海雀号。就是被公会扣下、点着这场火的那条。它锁在最里头的死角栈桥，铁链缠了三圈。"

    show aldric_img at left with dissolve

    aldric "大人，这船看着不像走私的。走私的船吃水深，它浮得高——舱里没多少货。"

    player "空船，却扣了人。我想上去看看。"

    ## ── 上船：按第一幕站队给不同的开门方式 ──
    if southern_faction == "guild":
        "栈桥口站着公会的人。你昨晚站了公会，这会儿一亮印戒，他们就让开了。"
        guild_master "领主大人想看？请便。公会没什么见不得人的。"
        "维斯帕话说得敞亮。敞亮得让你更想看。"
    elif southern_faction == "pirates":
        "栈桥口站着公会的人，本来要拦。赛琳的两个船员从水边摸上来，一左一右站到你身后，那两个人就改了主意。"
        corsair "我说过，夜里的码头不安全。所以我让人跟着你。"
    elif southern_faction == "neutral":
        "栈桥口的看守认得你——昨晚压着两边谈的就是你。他犹豫了一下，到底没拦。"
        dockhand "您是来看公道的。我让开。出了事别说是我放的。"
    else:
        "栈桥口没人。昨夜你谁都没站，也就没人替你开门，也没人盯着你。雾帮了你。"

    pause 0.3
    scene bg tideport_ship with dissolve

    "你踩着结霜的跳板上了海雀号。甲板是空的。"

    "底舱更空。几袋粗盐，一卷新绳，半桶焦油。没有兵器，没有违禁货——什么劫掠王国船队的赃物都没有。"

    "公会说这船走私军火。可这舱里连一把多余的刀都找不出来。"

    "你正要走，听见货堆后头有动静。"

    show ship_boy at right with dissolve

    ship_boy "别……别叫人。我不是贼。这是我的船。"

    "一个少年从盐袋后头爬出来。手腕上有勒过的红痕——被绑过，又挣脱了。"

    player "海雀号的人？他们不是被公会带走了吗。"

    ship_boy "带走了。就剩我躲下来。我想等船放出去，把它开走。"

    ship_boy "大人，我们没走私。我对着大海发誓。我们就是运盐的。"

    menu:
        "那公会为什么咬定你们走私？":
            $ change_rel("rel_corsair", 2)
            player "空舱一桶盐，公会凭什么说你们走私军火？"

        "先别急。慢慢说，那天到底发生了什么":
            $ change_rel("rel_corsair", 4)
            player "你先坐下。手给我看看——这伤得包。慢慢说，那天的事，一件一件讲。"
            "少年愣了一下。大概没料到一个内陆来的贵人会先看他的手。"

    ship_boy "raid 的前一天，来了个人。穿得体面，不像码头上的。他说他是掮客，帮人牵线买卖的。"

    ship_boy "他跟船老大讲，公会盯上海雀号了，要拿我们'立规矩'，抓了人就不会放——让我们别坐着等，趁早联络船主联盟，硬一把。"

    ship_boy "船老大没听他的。船老大说我们清白，怕什么。"

    ship_boy "第二天，公会就来了。说接到密报，海雀号给船主联盟运军火。"

    "你心里那处一直对不上的地方，咔哒一声，对上了一点。"

    player "那个掮客，叫什么？长什么样？"

    ship_boy "他说他叫费舍尔。不高，话很软，左手缺半根小指。口音……不是海边的，是内陆的。像王都那边。"

    "王都那边。"

    pause 0.5
    scene black with dissolve

    ## ============================================================
    ## 第二幕 · 拼图
    ## ============================================================

    play music "audio/music/tension.ogg" fadeout 1.0 fadein 1.5 if_changed
    scene bg tideport_tavern with fade

    "你回到断锚，把少年的话在心里摆开。"

    "一个内陆口音的'掮客'，raid 前一天去找海雀号，劝他们硬抗。"

    "同一天，公会接到'密报'，说海雀号走私军火。"

    "船是空的。密报是假的。劝人硬抗的，和递假密报的，会不会是同一只手？"

    ## ── 调取已知信息：玩家若谋略/声望高，自己就能拼出动机 ──
    if intrigue >= 45 or reputation >= 45:
        "你不用别人提醒，也想得通这背后图什么。"
        "潮汐港三百年不归王法。王廷要它，缺的从来不是兵，是借口。"
        "让港口自己打起来，打到港务厅扛不住，开口'请王军入港平乱'——借口就有了。船一进来，就不走了。"
        $ change_stat("intrigue", 4)
    else:
        "可一个掮客，挑动两伙人互相捅刀，图什么？这上头你还想不透。"

    "门开了。该来的都来了——赛琳从海上来，维斯帕从街上来。你昨天没让他们散，今天他们就还坐在一张桌子的两头。"

    show corsair_img at right with dissolve
    show guild_master_img at left with dissolve

    player "你们两个，谁认识一个叫费舍尔的掮客？左手缺半根小指，内陆口音。"

    "维斯帕的脸先变了。只变了一瞬，又收住。可你看见了。"

    guild_master "……港务厅介绍来的中间人。说能帮公会和外港牵线。我见过两面。"

    corsair "我也见过。他来跟我们船主递过话，说公会要赶尽杀绝，劝我们先下手。"

    "两个人对看了一眼。这一眼里头，头一回没有火，只有一样东西：两边都被同一个人喂了相反的话。"

    guild_master "他跟你们说公会要赶尽杀绝？"

    corsair "他跟你们说我们要运军火？"

    "桌上静了。窗外有海鸥在叫。"

    player "递假密报给公会的是他。劝船主动手的也是他。海雀号是空的——这场火，第一刀不是你们谁捅的。是他点的。"

    pause 0.5

    ## ============================================================
    ## 第二幕 · 赛琳恋爱线门槛（仿 Elena）
    ## ============================================================

    if rel_corsair >= 30:
        $ hide_all_chars()
        scene bg tideport_beach with dissolve
        play music "audio/music/southern_corsair.ogg" fadeout 1.5 fadein 2.0 if_changed

        "维斯帕回公会查费舍尔的底。剩下的事要等夜里。赛琳说她想透透气，叫你陪她走一段海堤。"

        show corsair_img sad at right with dissolve

        corsair "我在这港口混了十二年。被人骗过，也骗过人。可这回……我差点提着刀冲进公会，替别人杀人。"

        corsair "要不是你非要去看那条空船，我这辈子都不会知道，是谁拿我当刀使。"

        menu:
            "你不是刀。是这港口少有的、肯先问一句的人":
                $ corsair_romance = True
                $ change_rel("rel_corsair", 20)
                $ log_decision("南境游记", "在海堤上向赛琳交心")

                player "你不是谁的刀。这港口动刀的人多，肯先问一句'为什么'的人少。你是后一种。"

                "她停下脚步，看了你很久。海风把她额前的碎发吹起来。"

                corsair "内陆来的贵人，嘴倒甜。"

                "她嘴上这么说，却没躲开你的目光。"

                corsair "这片海认死理：救过你命的人，你得记一辈子。"
                corsair "可你昨天救的不是我的命。是我的手——没让它替别人去沾不该沾的血。这个，我记得更重。"

                if rel_corsair >= 80:
                    ## 恋爱深化（高好感才解锁，仿 Elena rel>=80）
                    "她忽然伸手，把你被海风吹乱的衣领抚平。这个动作她自己大概都没察觉。"
                    corsair "等这事了了……你那条北边的盐路，我亲自给你押船。"
                    corsair "不为艾登堡的旗。为你。"
                    "她说完自己先别过头去看海，耳根有点红。渡鸦船长的耳根。"

            "现在先别说这些。费舍尔还没揪出来":
                $ change_rel("rel_corsair", 5)
                player "这些话等抓住费舍尔再说。现在松一口气，太早。"

                corsair "……也对。是我贪那点海风了。"
                "她笑了一下，那笑里有点你看不太懂的东西，很快就被她收进了惯常的镇定里。"

        $ hide_all_chars()
        scene black with dissolve

    ## ============================================================
    ## 第二幕收束 + 第三幕钩子
    ## ============================================================

    play music "audio/music/southern_scheme.ogg" fadeout 1.0 fadein 1.5 if_changed
    scene bg tideport_office with fade

    "当夜，你们去港务厅找费舍尔。房是空的。床没睡过，文书烧了一半，火盆里还有余温——他走得很急，就在你们拼出真相的前后脚。"

    show corsair_img at right with dissolve
    show guild_master_img at left with dissolve

    corsair "跑了。"

    guild_master "不是跑。是去报信了。"

    "维斯帕站在窗前，望着港口外头那片黑沉沉的海。你顺着他的目光看过去。"

    play music "audio/music/southern_fleet.ogg" fadeout 1.5 fadein 2.0 if_changed
    scene bg tideport_fleet with dissolve

    "天边有光。低得不像星——一排一排的桅灯，正从外海往港口压过来。"

    guild_master "王军的'护港分舰队'。打着平乱的旗号。比我想的快。"

    guild_master "费舍尔不是去报信。他是来确认我们打到了哪一步——好让那支船队，名正言顺地进港。"

    corsair "什么平乱。他们要的是这个港。"

    "两个昨天还要拔刀相向的人，此刻并肩站在同一扇窗前，看着同一片灯火。"

    player "港口还有几天？"

    corsair "顺风的话，他们明天傍晚就到。"

    "几天？不。是几个时辰。"

    pause 1.5
    scene black with dissolve

    centered "{size=+5}第二幕 · 完{/size}"
    pause 1.2
    if corsair_romance:
        centered "{size=+3}费舍尔点了第一刀就跑了。剩下的烂摊子和那支逼近的船队，你和她一起扛。{/size}"
    else:
        centered "{size=+3}王军压境。这一回，潮汐港要么拧成一股，要么不剩一块板。{/size}"
    pause 2.0

    $ persistent.southern_dlc_progress = 2
    $ southern_quest_stage = 2

    jump southern_act3

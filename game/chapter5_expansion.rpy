## ============================================================
## 第五章扩展：最终决战 — 战前深度叙事
## chapter5_expansion.rpy
## 军议 / 动员备战 / 战前最后一夜 / 前哨战 / 风暴前的抉择
## ============================================================

## ── 扩展剧情标记 ──
default ch5_exp_war_strategy = ""           # "defend" / "attack" / "divide" / "diplomacy"
default ch5_exp_council_unity = 0           # 军议中的团结度
default ch5_exp_mobilize_focus = ""         # "walls" / "militia" / "supplies"
default ch5_exp_npc_farewells = 0           # 战前对话完成数
default ch5_exp_night_mood = ""             # "resolute" / "melancholy" / "fierce"
default ch5_exp_skirmish_tactic = ""        # "ambush" / "frontal" / "lure"
default ch5_exp_skirmish_result = ""        # "victory" / "pyrrhic" / "retreat"
default ch5_exp_casualties = 0             # 前哨战伤亡
default ch5_exp_enemy_morale_hit = False   # 是否打击了敌军士气
default ch5_exp_queen_ultimatum = ""        # "accept" / "reject" / "counter"
default ch5_exp_baron_response = ""         # "accept" / "reject" / "exploit"
default ch5_exp_lily_advice_taken = False   # 是否采纳暗百合建议
default ch5_exp_final_formation = ""        # "iron_wall" / "hidden_blade" / "holy_shield" / "peoples_bastion"
default ch5_exp_defender_bonus = 0          # 防御加成
default ch5_exp_speech_given = False        # 是否发表了战前演说
default ch5_exp_elena_promise = False       # 艾琳娜的承诺
default ch5_exp_aldric_legacy = False       # 奥尔德里克的传承
default ch5_exp_captain_oath = False        # 雷恩的誓言
default ch5_exp_bishop_blessing = False     # 主教的祝福
default ch5_exp_supply_line_cut = False     # 是否切断敌军补给
default ch5_exp_deserter_intel = False      # 逃兵情报
default ch5_exp_wall_breach = False         # 城墙是否被破坏

## ============================================================
## 第一部分：军议 — War Council (~300行)
## ============================================================

label ch5_exp_war_council:

    $ play_music("audio/music/tension.ogg", fadein=2.0)

    scene bg great_hall with dissolve
    $ unlock_gallery("bg_great_hall")
    $ set_mood("tense")

    "艾登堡的大厅里，所有的窗帘都被拉上了。"

    "长桌上铺着一张巨大的地图，四角压着铁制的烛台。蜡烛的火光在地图上投下跳动的影子，仿佛那些标记的军队真的在移动。"

    "你的核心幕僚围站在桌旁，每个人的脸上都带着凝重的表情。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    $ unlock_gallery("aldric")

    aldric "领主大人，所有人已到齐。军议可以开始了。"

    hide aldric_img
    show captain_img at right with dissolve
    $ unlock_gallery("captain")

    captain "最新斥候报告——敌军分两路逼近。"

    captain "南路：王后军三千人，由蒙塔古伯爵率领，沿官道北上。先锋部队已经进入我们南方三十里内。"

    captain "北路：冯·哈根男爵联军两千五百人，以骑兵为主，从格鲁瓦尔德堡南下。预计四天后抵达艾登堡以北的旷野。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "也就是说，我们被夹在中间了。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "正是如此。如果两军联手，我们将面对五千五百人的联军。以我们二百五十人的兵力——"

    captain "坦率地说，正面对抗毫无胜算。"

    hide aldric_img with dissolve
    hide captain_img with dissolve

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    $ unlock_gallery("elena")

    elena "但两军未必会联手。"

    elena "蒙塔古伯爵的目标是「平叛」——也就是消灭男爵。而男爵的目标是「推翻暴政」——也就是对抗王后。"

    elena "我们对他们而言，都只是附带目标。真正的敌人是彼此。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "所以关键在于——我们选择站在哪一边，还是两边都不站。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "没错。我整理了四种可行的战略方案。"

    hide elena_img with dissolve

    scene bg great_hall with dissolve

    "你环顾众人，示意艾琳娜继续。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve

    elena "第一种：死守艾登堡。关闭城门，不介入任何一方的战斗。"

    elena "优点是保存实力，避免直接冲突。缺点是——无论谁赢了，都可能回头来收拾我们。"

    elena "第二种：主动出击。趁两军尚未合流，先击溃其中一支的先锋部队，以战养战。"

    elena "优点是掌握主动权。缺点是——兵力悬殊，风险极高。"

    elena "第三种：分化瓦解。利用双方阵营内部的矛盾，拉拢可争取的力量，让敌人自己瓦解。"

    elena "这需要时间和情报网络的支持。"

    elena "第四种：外交斡旋。借助教会或其他中立势力的名义，推动停战谈判。"

    elena "这条路最和平，但也最脆弱——只要任何一方不配合，就会功亏一篑。"

    hide elena_img with dissolve

    "每个人都在消化这些方案。有人端起茶杯，发现早已凉透了。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "从军事角度来说，我倾向于死守。城墙是我们最大的优势。"

    captain "在开阔地上和五千人对战是送死。但在城墙后面，我们的二百五十人至少能抵挡十倍的敌人——前提是他们没有攻城器械。"

    hide captain_img with dissolve

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "管家的意见——死守固然安全，但一旦粮食耗尽，就是坐以待毙。"

    aldric "我们需要至少一个外部盟友来打破僵局。"

    hide aldric_img with dissolve

    if alliance_church:
        $ hide_all_chars("bishop_img")
        show bishop_img at left with dissolve
        $ unlock_gallery("bishop")
        bishop "教会可以派出使者，以圣母的名义呼吁停火。"
        bishop "蒙塔古伯爵是虔诚的信徒，他可能会响应。但男爵……恐怕不会把教会放在眼里。"
        hide bishop_img with dissolve
        $ ch5_exp_council_unity += 1

    if bishop_total_loyalty:
        $ hide_all_chars("bishop_img")
        show bishop_img at left with dissolve
        if alliance_church:
            bishop "此外——我个人还能额外召集一批退伍老兵。他们是我的信徒，忠诚可靠。"
        else:
            bishop "虽然教会官方尚未表态……但我个人已经做好了准备。"
            bishop "我的信徒中有不少退伍士兵。只要您一声令下，他们愿意为艾登堡拿起武器。"
        hide bishop_img with dissolve
        $ ch5_exp_council_unity += 1

    if dark_lily_joined:
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "暗百合方面也传来了消息。首领说——"
        elena "「两军之中皆有我们的人。只需一个信号，就能在关键时刻制造混乱。」"
        elena "但首领的条件是——无论最终谁赢了，暗百合的利益必须得到保障。"
        hide elena_img with dissolve
        $ ch5_exp_council_unity += 1

    if alliance_baron:
        $ hide_all_chars()
        "你想起与男爵之间微妙的关系。他曾是你的盟友——至少表面上是。"
        "也许这份旧日的联系，可以在关键时刻被利用。"
        $ ch5_exp_council_unity += 1

    if spy_network:
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "另外，我们的间谍网络传回了一条重要情报——"
        elena "男爵联军中的维克托领主暗中联络了蒙塔古伯爵。他在考虑临阵倒戈。"
        elena "如果我们能在合适的时机推他一把……"
        hide elena_img with dissolve
        $ change_stat("intrigue", 2)
        $ ch5_exp_council_unity += 1

    if elena_skills_used:
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "还有一条——我之前部署的那些「眼线」已经开始回报了。"
        elena "敌军后勤线上有一个关键的补给站，守卫薄弱。如果提前破坏，他们的攻势至少推迟三天。"
        hide elena_img with dissolve
        $ ch5_exp_council_unity += 1

    $ hide_all_chars()
    "你仔细听完了所有人的意见，目光落回地图上。"

    "四条路，每一条都有风险。但你必须选一条。"

    menu:
        "死守艾登堡——以城墙为盾，等待时机":
            $ ch5_exp_war_strategy = "defend"
            $ change_stat("power", 3)
            $ change_stat("loyalty", 2)
            $ ch5_exp_defender_bonus += 5

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我们守城。艾登堡的城墙经过这些日子的加固，是我们最大的资本。"

            player "雷恩，从今天起，所有人进入战备状态。城外的一切物资全部搬入城内。"

            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "遵命！"

            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "奥尔德里克，清点所有存粮和饮水。我要一份精确的清单。"

            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "马上去办。"

            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我们不需要赢——只需要撑到两支大军打完。当鹬蚌相争的时候，我们做那个渔翁。"

            $ hide_all_chars()
            "众人点头。这是最保守、也最稳妥的策略。"

            "但你也知道——被动等待，就是把主动权让出去。两军先打谁，打多久，全看天意。"

        "主动出击——趁敌军分散，各个击破":
            $ ch5_exp_war_strategy = "attack"
            $ change_stat("power", 5)
            $ change_stat("reputation", 3)

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "等待不是我的风格。在敌人合流之前，我们要先发制人。"

            hide aldric_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve

            captain "领主大人，这——兵力差距太大了！"

            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "所以我们不打正面。趁夜色突袭王后军的先锋营地，打乱他们的部署。"

            player "然后迅速撤回城中。让他们知道——艾登堡不是任人宰割的羔羊。"

            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "……如果是突袭的话，以精锐夜袭百人规模的先锋营，确实有可能。"

            captain "但风险很高。一旦被发现，退路可能被切断。"

            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "所以我需要你挑出最精锐的五十人。速度要快，打完就走。"

            hide captain_img with dissolve

            "这是一个大胆的计划。但大胆有时候就是活路。"

        "分化瓦解——利用敌军内部矛盾":
            $ ch5_exp_war_strategy = "divide"
            $ change_stat("intrigue", -15)  ## 消耗机制大轮: 动用全部情报渠道散假情报=烧网络, 谋略储备被花掉
            $ change_stat("reputation", 2)

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "正面打不过，那就让他们自己打自己。"

            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve

            elena "你是说——利用男爵联军内部的裂痕？"

            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "不只是男爵那边。蒙塔古伯爵和王后也有分歧。"

            player "我需要你动用所有的情报渠道，向两边散布经过精心设计的假情报。"

            player "让王后军以为男爵在和我们密谈投降。让男爵以为王后已经买通了他的部下。"

            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "一个经典的离间计。简单，但有效。"

            elena "我需要两天时间来部署。"

            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你有一天半。"

            hide elena_img with dissolve

            $ hide_all_chars()
            "代价是，你手上的眼线几乎要倾巢而出。假情报一旦散出去，对方迟早会顺着源头清查——保得住几个是几个。"

        "外交斡旋——以谈判化解战争" if alliance_church or faith >= 50:
            $ ch5_exp_war_strategy = "diplomacy"
            $ change_stat("faith", 3)
            $ change_stat("reputation", 5)

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "战争不是唯一的解决方式。如果能不流血就化解这场危机——"

            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve

            bishop "领主大人，您是在说——和谈？"

            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "主教大人，我需要教会以中立调停者的身份，向双方发出停战邀请。"

            player "在圣母的名义下，至少蒙塔古伯爵不会拒绝坐下来谈。"

            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "这……确实是一条值得尝试的路。但男爵那边——"

            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "男爵不在乎教会。但他在乎时间。他的后勤撑不了太久。"

            player "只要我们能把他拖上谈判桌，时间就站在我们这边。"

            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "我这就去安排使者。"

            hide bishop_img with dissolve

            "谈判的事交给了教会。你能做的，只有等使者带回消息。"

    $ ch5_exp_council_unity += 2

    scene bg great_hall with dissolve

    "军议持续了整整三个时辰。当你最终宣布散会时，窗外的天色已经暗了下来。"

    "每个人都领到了自己的任务，脚步匆匆地离开了大厅。"

    "你独自站在地图前，手指按在艾登堡的位置上。"

    "地图上，它小得用一根手指就能盖住。"

    if ch5_exp_council_unity >= 4:
        "你的人站在一起。这就够了。"
        $ change_stat("loyalty", 3)
    elif ch5_exp_council_unity >= 2:
        "你的幕僚们各有想法，但最终都选择了信任你的判断。"
    else:
        "你的幕僚们面带忧虑地离开了。你知道他们对你的计划心存疑虑。但犹豫的时间已经过去了。"

    return

## ============================================================
## 第二部分：动员与备战 — Mobilization (~300行)
## ============================================================

label ch5_exp_mobilize:

    $ play_music("audio/music/battle_prepare.ogg", fadein=2.0)

    scene bg castle_exterior with dissolve
    $ unlock_gallery("bg_castle_exterior")
    $ set_mood("tense")

    "军议结束后的第二天，整座艾登堡都动了起来。"

    "城门外的道路上，满载着粮食和木材的牛车排成了长队。城墙上，石匠和士兵并肩工作，修补每一处裂缝。"

    "空气中弥漫着铁锈、汗水和新鲜锯木的气息。"

    "你穿上轻便的皮甲，决定亲自巡视城防。"

    ## --- 巡视城墙 ---

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "领主大人！北墙的修缮进度已经完成了八成。"

    captain "但东南角的箭塔有些老化。如果被投石车击中，可能撑不住。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "让我看看。"

    $ hide_all_chars()
    "你沿着城墙走了一圈。石阶上被来回搬运的脚步磨得光滑，城垛上新铺了一层灰浆。"

    "每隔二十步就有一个弓箭手的位置，旁边整齐地摆着箭筒和火油罐。"

    "你在东南角停下脚步，用手按了按墙面。确实，砖石之间的灰浆已经开裂了。"

    hide captain_img with dissolve

    menu:
        "亲自巡视——你的声望本身就是力量" if reputation >= 60:
            $ ch5_exp_mobilize_focus = "morale"
            $ change_stat("loyalty", 5)
            $ change_stat("reputation", 3)
            $ ch5_exp_defender_bonus += 4

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "城墙、民兵、物资——这些都靠人。我亲自走一趟。"

            $ hide_all_chars()
            "你脱下领主的礼袍，换上一身简朴的旧式军装，在三天里走遍了艾登堡每一个角落。"

            "城墙下你帮石匠搬过砖。民兵营里你跟新兵一起吃过粗粮。粮仓里你和搬运工一起对过账。"

            "百姓认得你。守军认得你。连难民营里的孩子都拉着你的衣角问——「大人，我们会赢吗？」"

            "你只回答一句——「会。」"

            "三天后，整个艾登堡都不一样了。每个人都知道：领主就在身边。"

        "集中人手加固东南角":
            $ ch5_exp_mobilize_focus = "walls"
            $ change_stat("power", 3)
            $ ch5_exp_defender_bonus += 3

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "雷恩，调三十人过来。我要在两天内把东南角加固到和其他地方一样坚固。"

            $ hide_all_chars()
            "铁匠们连夜赶制了铁钉和铁栓，用来加固松动的石块。"

            "石匠们用新的灰浆重新填补了每一条裂缝。一些老兵甚至在城墙内侧堆起了土坡——即使城墙被攻破，土坡也能减缓敌军的推进。"

            "两天后，东南角焕然一新。你拍了拍坚实的墙面，微微点头。"

        "扩大民兵训练规模":
            $ ch5_exp_mobilize_focus = "militia"
            $ change_stat("loyalty", 3)
            $ change_stat("power", 2)

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "城墙的事交给石匠。我更担心的是人手不够。"

            player "从难民和领民中再征召一百名志愿者。不需要他们上阵杀敌，能守城就行。"

            $ hide_all_chars()
            "消息传出后，报名的人比预想的多。"

            "铁匠的儿子，面包师的学徒，甚至一个独臂的退伍老兵——他们都来了。"

            "老兵站在队列最前面，用仅剩的左手举着一把生锈的剑。"

            $ hide_all_chars("soldier_generic_img")
            show soldier_generic_img at left with dissolve
            veteran "领主大人，我右手没了，但左手还能砍人。"

            "你走上前，握住了他的手。"

            if knows_eagle_network:
                "握手的时候，你看见那把锈剑的柄尾——一个磨得快平的记号。和西塔上老弗雷德里克那把，是同一个。"

                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "这把剑，哪来的？"

                $ hide_all_chars("soldier_generic_img")
                show soldier_generic_img at left with dissolve
                veteran "我祖父传的。他说他的祖父给一个大人物当过卫兵——名字没传下来。"

                $ hide_all_chars()
                "『剑卫护身。残部老死于无名。』——剑卫散了几百年，无名的剑还在无名的人手里，守着一座城。"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "老兵到场，这城守得住。"

            "民兵们爆发出了一阵欢呼。他们或许不是精锐，但保卫家园的决心不输任何人。"

        "全力囤积物资":
            $ ch5_exp_mobilize_focus = "supplies"
            $ change_stat("wealth", -3)
            $ change_stat("intrigue", 2)
            $ ch5_exp_defender_bonus += 2

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "城墙可以慢慢修，但物资必须现在就囤够。"

            player "奥尔德里克，把金库打开。我要买下方圆五十里内所有能买到的粮食、药草和铁矿。"

            $ hide_all_chars()
            "接下来两天，一批又一批的物资被运进城堡。粮仓被塞得满满当当，连走廊里都堆起了麻袋。"

            "铁匠铺的炉火昼夜不息，源源不断地锻造箭头、枪尖和铁蒺藜。"

            "药房里的大夫们忙着熬制止血药和退烧汤，空气中弥漫着苦涩的草药味。"

            "你知道——围城打到最后，比的是谁的粮仓先见底。"

    ## --- 治理系统成果展示 ---

    scene bg castle_exterior with dissolve

    "巡视继续。你走下城墙，来到城堡内的广场。"

    if governance_prosperity >= 70:
        "过去几个月的治理成果在此刻充分显现。"

        "广场上，训练有素的民兵正在队列演练。装备整齐划一——银子花对了地方。"

        "粮仓区传来清点物资的吆喝声——储备充足，至少能撑三个月。"

        "城墙上，刚刚安装的新型弩炮在阳光下闪着冷光。那是你花重金从南方商人手中买来的。"

        $ ch5_exp_defender_bonus += 5
        $ change_stat("power", 3)

        "你深吸一口气，把手掌按在城墙的石砖上。石头被太阳晒得发烫。这些日子的辛苦没有白费——艾登堡已经不再是从前那个破旧的小城堡了。"

    elif governance_prosperity >= 50:
        "广场上的景象让你既欣慰又忧虑。"

        "民兵的装备凑合，训练也还过得去。粮仓里有存粮，但经不起长期消耗。"

        "城墙修补了，但总觉得还差了些什么。"

        $ ch5_exp_defender_bonus += 2

        "够了吗？也许够了。也许不够。你只能祈祷命运不要太刻薄。"

    else:
        "广场上的景象让你心沉了下去。"

        "民兵拿着五花八门的武器——镰刀、锄头、甚至削尖的木棍。他们的眼神中写满了恐惧。"

        "粮仓空了大半。城墙上还有几处裂缝来不及修补。"

        "你咬住了腮帮肉。如果当初能把更多精力放在治理上……但后悔已经来不及了。"

        "你只能用你现有的一切去战斗。"

    if built_granary:
        "山丘上那座五千石的粮仓装得满满当当。管事的老吏拍着仓门告诉你：围城三个月，饿不死人。"
        $ ch5_exp_defender_bonus += 1

    if built_watchtower:
        "北岗的望楼日夜有人值守，旗语白天传、烽火夜里传。敌军离城还有半天路程，你就能收到警报。"
        $ ch5_exp_defender_bonus += 1

    if famine_prevented:
        "民兵队列里有不少河谷来的面孔。那年大旱，领地没有饿死一个人——挨过那个冬天的人，如今站在这里。"

    if governance_infrastructure >= 60:
        ## 治理子属性读点 (批31收尾轮): 基建底子在守城战兑现
        "先前修的路和桥这时候显出用处：粮车从村里到城门只要半天，城墙根下的排水沟也早清过淤——雨季围城，最先垮的往往不是墙，是墙脚的积水。"
        $ ch5_exp_defender_bonus += 1

    ## --- 战前NPC对话 ---

    scene bg great_hall with dissolve

    "傍晚时分，你回到大厅。一天的巡视让你疲惫不堪，但还有更重要的事要做。"

    "你决定和每一个重要的人谈一谈——也许是最后一次。"

    ## --- 与奥尔德里克的战前对话 ---

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "领主大人，您今天走了太多路。让我给您倒杯热茶。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "奥尔德里克，坐下。我有话对你说。"

    "老管家愣了一下，然后缓缓坐在了你对面。"

    if secret_passage_found and not (ch1_deep_cellar_choice == "seal" and not passage_re_opened):
        if passage_re_opened:
            player "如果明天……如果城堡守不住了——你带着百姓从那条重新打通的密道撤离。"
        else:
            player "如果明天……如果城堡守不住了——你带着百姓从密道撤离。"
    else:
        if ch1_deep_cellar_choice == "seal":
            player "如果明天……如果城堡守不住了——你带着百姓走北门。趁夜色，绕开主战场。"
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "……是。"
            "他没有提密道。这事你们都心知肚明。"
        else:
            player "如果明天……如果城堡守不住了——你带着百姓从北门撤离。趁夜色离开。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "领主大人——"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "这不是商量。这是命令。"

    if rel_aldric >= 60:
        "老管家缓缓站起身，像年轻时那样挺直了腰板。"

        hide player_char_img
        $ hide_all_chars("aldric_img")
        show aldric_img at left with dissolve
        aldric "我侍奉您的父亲三十年。他临终时拉着我的手说——「照顾好我的孩子。」"

        aldric "我答应了他。这是我一生中最重的承诺。"

        aldric "所以——恕我不能遵从您的命令。"

        aldric "如果城墙倒了，我会站在您身边。就像当年站在老领主身边一样。"

        "他浑浊的眼中闪着坚定的光。你知道再说什么都没用。"

        hide aldric_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "……固执的老头。"

        hide player_char_img
        $ hide_all_chars("aldric_img")
        show aldric_img at left with dissolve
        aldric "这一点，您和您的父亲一模一样。"

        $ ch5_exp_aldric_legacy = True
        $ change_rel("rel_aldric", 5)
        $ ch5_exp_npc_farewells += 1
    else:
        aldric "我明白。我会安排好撤离路线的。"
        aldric "领主大人，请一定……保重。"
        $ ch5_exp_npc_farewells += 1

    hide aldric_img with dissolve

    ## --- 与雷恩的战前对话 ---

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "领主大人，巡视辛苦了。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "雷恩，士兵们的状态怎么样？"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "说实话——紧张。很多人是第一次面对真正的战争。"

    captain "但我在他们眼中看到了一样东西——不是恐惧，是决心。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "那你呢？你怕不怕？"

    "雷恩的手不自觉地摸了摸剑柄。"

    if rel_captain >= 60:
        hide player_char_img
        $ hide_all_chars("captain_img")
        show captain_img at left with dissolve
        captain "怕。但不是怕死。"

        captain "怕的是……辜负了您的信任。怕保护不了那些把命交给我的人。"

        captain "我这辈子遇到过很多领主。有的贪婪，有的懦弱，有的自大。"

        captain "但您不一样。您是第一个会问士兵「你怕不怕」的领主。"

        captain "所以——哪怕前面是刀山火海，我也会跟着您。"

        hide captain_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "雷恩……"

        hide player_char_img
        $ hide_all_chars("captain_img")
        show captain_img at left with dissolve
        captain "不用说了。去休息吧，领主大人。明天还有硬仗要打。"

        $ ch5_exp_captain_oath = True
        $ change_rel("rel_captain", 5)
    else:
        captain "军人不该谈论恐惧。但我可以告诉您——"
        captain "我的剑磨好了，铠甲也擦亮了。明天见分晓。"

    $ ch5_exp_npc_farewells += 1

    hide captain_img with dissolve

    ## --- 与艾琳娜的战前对话 ---

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve

    elena "巡视完了？"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "嗯。城防的情况比预想的好一些。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "那就好。"

    "她走到窗边，看着窗外逐渐黯淡的天色。"

    elena "你知道吗？我小时候在街上流浪的时候，最怕的就是天黑。"

    elena "因为天黑之后，你看不见危险从哪里来。"

    elena "但现在……我反而希望天不要亮。因为天亮之后，一切都会改变。"

    if elena_romance:
        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "不管明天发生什么，有些事不会改变。"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "比如？"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "比如——你对我来说很重要。"

        "她转过身，窗外透进来的微光映在她的侧脸上。"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "你总是在最不合适的时候说最好听的话。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "也许正因为时间不多，才更要说。"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "……笨蛋。"

        "她轻轻握住了你的手，力道很紧。"

        elena "答应我。活着。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "你也是。"

        $ ch5_exp_elena_promise = True
        $ change_rel("rel_elena", 5)
    else:
        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "领主大人，有件事我一直没对你说。"

        elena "当初来到艾登堡，只是为了完成任务。我把你当成一颗棋子。"

        elena "但这段时间——你让我明白了一件事。"

        elena "艾登堡的人不欠我什么——但我不想看他们死。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "谢谢你的坦诚，艾琳娜。"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "别谢我。我留下来是因为自己想留。"

    $ ch5_exp_npc_farewells += 1

    hide elena_img with dissolve

    ## --- 与主教的战前对话 ---

    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    $ unlock_gallery("bishop")

    bishop "领主大人，我来是想告诉您——明天黎明，我会在教堂举行一场祈祷仪式。"

    bishop "为所有即将上战场的人祈求圣母的庇佑。"

    hide bishop_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "主教大人，你真的相信祈祷有用吗？"

    "主教低下头，双手合十。"

    if faith >= 50:
        hide player_char_img
        $ hide_all_chars("bishop_img")
        show bishop_img at left with dissolve
        bishop "我相信。不是因为圣母一定会回应——而是因为信仰本身就是一种力量。"

        bishop "当一个人跪在圣母像前祈祷的时候，他心中的恐惧会少一些，勇气会多一些。"

        bishop "这不是奇迹，但也不亚于奇迹。"

        bishop "领主大人，您愿意和您的士兵一起参加祈祷吗？"

        menu:
            "参加祈祷":
                $ ch5_exp_bishop_blessing = True
                $ change_stat("faith", 5)
                $ change_stat("loyalty", 3)

                hide bishop_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "我会的。如果我的士兵们在祈祷，我没理由缺席。"

                hide player_char_img
                $ hide_all_chars("bishop_img")
                show bishop_img at left with dissolve
                bishop "圣母会保佑您的。保佑艾登堡。"

                "你在心中默念了一句——不管圣母是否在听，至少你的士兵们需要看到你和他们站在一起。"

            "婉拒但表示尊重":
                $ change_stat("faith", 2)

                hide bishop_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "我有太多事要处理。但请替我向圣母转达——保佑我的人民。"

                hide player_char_img
                $ hide_all_chars("bishop_img")
                show bishop_img at left with dissolve
                bishop "我会的，领主大人。"

    else:
        bishop "也许有用，也许没用。但它至少能让人的心安定下来。"

        bishop "在战争面前，人需要抓住些什么——信仰、希望、或者仇恨。"

        bishop "领主大人，您抓住的是什么？"

        hide bishop_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "责任。"

        hide player_char_img
        $ hide_all_chars("bishop_img")
        show bishop_img at left with dissolve
        bishop "……这或许是最沉重的一种。但也是最不会让人迷失的一种。"

    $ ch5_exp_npc_farewells += 1

    hide bishop_img with dissolve

    if ch5_exp_npc_farewells >= 4:
        $ hide_all_chars()
        "和每一个人谈完之后，你感到一种奇特的平静。"
        "恐惧还在。但明天站上城墙的，不止你一个。"
        $ change_stat("loyalty", 3)

    return

## ============================================================
## 第三部分：战前最后一夜 — The Last Night (~300行)
## ============================================================

label ch5_exp_last_night:

    $ play_music("audio/music/campfire.ogg", fadein=2.0)

    scene bg castle_exterior_night with dissolve
    $ unlock_gallery("bg_castle_exterior")
    $ set_mood("melancholy")
    $ set_weather("clear", "normal")

    "夜色如同黑色的天鹅绒，覆盖了艾登堡。"

    "月亮高悬在城堡的尖塔之上，把银色的光洒在每一块石头上。远处的旷野在月光下像一面巨大的银镜，平静得令人不安。"

    "城堡里没有人睡觉。"

    "厨房的灯还亮着——厨娘们在烤最后一批干粮。武器库前排着长队——每个人都在领取明天要用的箭矢和绷带。"

    "教堂的钟声在午夜时分敲了十二下。"

    "你穿过庭院，看到篝火旁围坐着一群士兵。他们没有说话，只是安静地看着火焰。"

    "火光映在他们的脸上——有人在发呆，有人在祈祷，有人在擦拭妻子送的护身符。"

    "一个年轻的士兵在给家里写信。他写了又撕，撕了又写，最后把纸揉成一团扔进了火里。"

    "你走上前，在他身边坐了下来。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "写不出来？"

    $ hide_all_chars("soldier_generic_img")
    show soldier_generic_img at left with dissolve
    young_soldier "领主大人！我——"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "坐下，坐下。不用起身。"

    $ hide_all_chars()
    $ hide_all_chars("soldier_generic_img")
    show soldier_generic_img at left with dissolve
    young_soldier "我想给我娘写封信……但不知道该说什么。"

    young_soldier "说「我很好」？她肯定不信。说「我害怕」？她会更担心。"

    young_soldier "说「如果我回不来」……我连想都不敢想。"

    menu:
        "告诉他写真心话就好":
            $ ch5_exp_night_mood = "resolute"
            $ change_stat("loyalty", 2)

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你就写——「娘，我想你了。等打完仗，我就回去看你。」"

            $ hide_all_chars("soldier_generic_img")
            show soldier_generic_img at left with dissolve
            young_soldier "这……也行吗？"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你娘不需要知道你在做什么。她只需要知道你想她了。"

            $ hide_all_chars()
            "年轻人想了想，认真地点了点头。然后低下头，重新开始写。"

            "这一次，他没有撕。"

        "替他写一封简短的信":
            $ ch5_exp_night_mood = "melancholy"
            $ change_stat("reputation", 2)

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "把笔给我。我来写。"

            $ hide_all_chars()
            $ hide_all_chars("soldier_generic_img")
            show soldier_generic_img at left with dissolve
            young_soldier "领主大人？！"

            "你接过笔，在纸上写了几行字。"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "「您的儿子在艾登堡一切安好。他是一个勇敢的战士，领主大人为他骄傲。等春花开了，他就回家。」"

            $ hide_all_chars()
            "年轻人接过信纸，读了一遍又一遍。眼眶红了。"

            $ hide_all_chars("soldier_generic_img")
            show soldier_generic_img at left with dissolve
            young_soldier "谢谢您……领主大人。"

        "拍拍他的肩，什么都不说":
            $ ch5_exp_night_mood = "fierce"
            $ change_stat("power", 2)

            "你没有说话，只是拍了拍他的肩膀。"

            "年轻人挺直了腰板。"

            young_soldier "领主大人，明天我一定不会给您丢脸。"

    "你站起身，继续在城堡中游走。"

    ## --- 与Aldric的深夜回忆 ---

    scene bg study_night with dissolve
    $ unlock_gallery("bg_study_night")

    "路过书房时，你看到里面还亮着灯。推开门，奥尔德里克正坐在桌前，面前摊着一本泛黄的册子。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "还没睡？"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "老人家觉少。"

    "你走近一看——那是一本很旧的账本。上面是你父亲的笔迹。"

    aldric "这是老领主记的家族账本。每一笔收支都清清楚楚。"

    aldric "你看这里——十五年前，他花了三十个金币修缮了村子里的水井。旁边备注写着——「饮水之恩，不可忘也。」"

    aldric "还有这里——十二年前，瘟疫横行，他自费购买了一百份草药分发给领民。"

    aldric "账本上写着——「一人之财，万人之命。孰轻孰重，不言自明。」"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "父亲……他一直都是这样的人吗？"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "是。从我认识他的第一天起，就是这样。"

    aldric "所以当他发现了王后的秘密时——他没有选择沉默。"

    aldric "他说——「如果我不站出来，谁来站出来？」"

    "你轻轻合上了账本，把它放回书架上。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我明白他为什么要那样做了。"

    player "因为有些事，比活着更重要。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "您越来越像他了，领主大人。这是好事，也让我担心。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "不要担心。我会比他走得更远——而且，我会活着走下去。"

    hide aldric_img with dissolve

    ## --- 与Elena的坦白 ---

    scene bg palace_garden_night with dissolve
    $ unlock_gallery("bg_palace_garden")

    "你来到花园。星星稀稀拉拉挂了几颗，花丛的轮廓在暗中起伏。"

    "艾琳娜靠在一棵老橡树下，仰望着星空。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve

    elena "睡不着？"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "今晚谁都睡不着。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "我在想一些乱七八糟的事。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "比如？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "比如——如果当初我没有来艾登堡，现在会在哪里。"

    if elena_spy_known:
        elena "也许在某个城市的暗巷里，继续做我的间谍活计。偷情报，卖消息，在刀尖上跳舞。"
    else:
        elena "也许在某个城市的暗巷里，继续做那些见不得光的事。在刀尖上跳舞。"

    elena "不会遇到你，不会在乎一座从没听说过的城堡和里面的人。"

    elena "也不会在战前的夜里，心跳得像打鼓一样。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "后悔来了吗？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "不。这是我做过的最好的决定。"

    "她从树下走出来。你等眼睛适应了黑暗，才看清她的神色——不像白天那样滴水不漏。"

    elena "有件事我一直没告诉你。"

    elena "我父亲——他的死，也许并不像我一直以为的那么简单。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "什么意思？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "关于我的身世，你已经知道了。但有一件事我一直没有说。"

    elena "我父亲的死——可能不是急病。在侍女学院学了毒药学之后，我回想他去世前的症状……那不像是普通的病。"

    elena "也许是暮色之露，也许是别的什么。我没有证据。但我知道，有人不希望我们家继续留在王都。"

    elena "有件事我也是后来才拼出来的——"

    elena "父亲在去世前一年，曾在王宫某位大人物的私邸做过几个月文书。回来后整个人变得沉默，常常半夜醒来盯着窗外。"

    elena "他临终前断断续续提过一句话：「那个酒杯不该是那个颜色」。"

    elena "当时家里没人懂他在说什么。直到我在侍女学院学了毒药学——"

    "她抬眼望向远处。"

    elena "暮色之露在紫光下会显出特殊的颜色。父亲也许偶然瞥见了什么……本不该让一个外人看到的东西。"

    elena "我们家不是什么显赫的贵族。但凡是看到了不该看的——不管头衔大小，结局都一样。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "艾琳娜……"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "不用同情我。我说这些只是想让你知道——"

    elena "这场战争对我来说，不只是帮你打仗。这也是我自己的仇。"

    elena "所以——不管你怎么选，我都会在你身边。不是因为义务，是因为我们有同样的敌人。"

    if father_poison_method_known:
        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "我们会让真相大白的。你的父亲，我的父亲——所有被暮色之露夺去生命的人，都会得到公道。"
        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "……嗯。"
        "她的声音有些颤抖。这是你第一次看到她如此脆弱。"
    else:
        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "谢谢你告诉我这些。我不会让你失望的。"

    hide elena_img with dissolve

    ## --- 与Captain的战争经验 ---

    scene bg castle_exterior with dissolve

    "你登上城楼。雷恩已经在那里了，双手撑在城垛上，眺望着远方。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "领主大人。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你在看什么？"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "看那片旷野。明天那里可能就会变成战场。"

    captain "我在想——多少人明天还能站着看日落。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "雷恩，给我讲讲你的第一次战斗。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "那年我十七岁。北方边境的一次小冲突。对手是一群马匪。"

    captain "我记得自己握着剑的手一直在抖。训练了几百遍的刺杀动作，到了真正面对人的时候，全忘了。"

    captain "第一个冲上来的马匪，我连躲都忘了躲。是旁边的老兵拉了我一把。"

    captain "老兵对我说——「别看他们的脸。看他们的武器。脸会让你犹豫，武器不会。」"

    captain "后来我学会了。战场上不能犹豫。犹豫一秒，就是一条命。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "那你现在呢？还会犹豫吗？"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "不会了。但我会害怕。每一次战斗前都会害怕。"

    captain "那个老兵后来告诉我——「不害怕的人活不过第二场仗。害怕才是活下去的本能。」"

    captain "他说对了。他打了二十年仗，每次都害怕，但每次都活了下来。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "他现在怎么样？"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "……第二十一场仗的时候，没能活下来。"

    "城墙上的风变冷了。你裹紧了披风。"

    captain "领主大人，我说这些不是想吓您。"

    captain "我是想说——明天不管发生什么，请信任您的士兵。他们不是英雄，但他们是真正的战士。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我信任他们。就像信任你一样。"

    hide captain_img with dissolve

    ## --- 主教的祈祷 ---

    if faith >= 50:
        scene bg great_hall with dissolve

        "经过教堂时，你听到了低沉的祈祷声。"

        "烛光从半开的门缝中漏出来，在黑暗的走廊上画出一条金色的线。"

        "你推开门。主教跪在圣母像前，双手合十，口中喃喃有词。"

        $ hide_all_chars("bishop_img")
        show bishop_img at left with dissolve

        "他没有回头，但似乎感觉到了你的存在。"

        bishop "……主啊，请宽恕我们即将犯下的罪。"

        bishop "不是因为我们想杀戮。是因为我们想守护。"

        bishop "如果流血是不可避免的……那就请让它少一些。再少一些。"

        "你静静地听完了他的祈祷。"

        bishop "领主大人。"

        hide bishop_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "我不想打扰你。"

        hide player_char_img
        $ hide_all_chars("bishop_img")
        show bishop_img at left with dissolve
        bishop "你没有打扰。也许……你也需要在圣母面前说几句话。"

        menu:
            "跪下祈祷":
                $ change_stat("faith", 3)

                $ hide_all_chars()
                "你走到圣母像前，缓缓跪下。"

                "你不知道该说什么。但当膝盖触碰到冰冷的石地面时，所有的重压似乎轻了一些。"

                hide bishop_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "如果你能听到的话——请保佑他们。不是我，是他们。"

                "你不知道圣母是否在听。但说出来的那一刻，心中的乱麻似乎理清了一些。"

            "站在一旁默默注视":
                $ change_stat("intrigue", 1)

                $ hide_all_chars()
                "你没有跪下。但你站在阴影中，注视着烛光中的圣母像。"

                "那张慈悲的面容在摇曳的火光中仿佛活了过来。她的眼睛似乎在看着你，带着一种无言的悲悯。"

                "你在那张面容前站了很久。没说话，也没跪。走出教堂的时候，心跳比刚进来时慢了一点。"

        hide bishop_img with dissolve

    ## --- 城墙独白 ---

    scene bg castle_exterior with dissolve
    $ set_weather("clear", "normal")

    "所有人都散去了。城堡终于安静下来。"

    "你独自登上城堡最高的塔楼。"

    "从这里望出去，可以看到整片大地。北方的地平线上，有隐约的火光——那是敌军的营火。"

    "南方也有。两面的火光像是两条缓缓逼近的火蛇，把艾登堡围在中间。"

    "风从北方吹来，带着泥土和铁锈的气味。"

    "你闭上眼睛。"

    "父亲的面容浮现在脑海中。不是梦里那个苍老憔悴的影子，而是记忆中那个高大温暖的男人。"

    "他牵着你的手走在麦田里，告诉你——「这片土地上的每一个人都是我们的家人。领主的意义不是统治，而是守护。」"

    "你睁开眼，目光变得坚定。"

    "是的，父亲。我明白了。"

    "明天，不管面对的是什么——"

    "我会用你教给我的方式去面对。"

    "你深吸了一口气。寒冷的空气灌入肺中，冻得胸口发疼。"

    "当你再吐出这口气时——"

    "你已经准备好了。"

    return

## ============================================================
## 第四部分：前哨战 — Skirmish (~300行)
## ============================================================

label ch5_exp_skirmish:

    $ play_music("audio/music/battle_prepare.ogg", fadein=2.0)

    scene bg castle_exterior with dissolve
    $ unlock_gallery("bg_castle_exterior")
    $ set_mood("tense")

    "黎明。"

    "第一缕阳光还没越过东方的山脊，号角声就撕裂了沉睡的空气。"

    "不是艾登堡的号角——是从北方传来的。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "领主大人！敌军先锋到了！"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "多少人？"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "大约三百骑兵，打着男爵的旗号。他们在城北的山坡上列阵！"

    $ hide_all_chars()
    "你快步登上城楼。北方的山坡上，果然整齐地排列着一队骑兵。"

    "晨曦中，他们的铠甲反射着暗淡的金光。旗帜上绣着冯·哈根男爵的狼首徽章——一只张着血盆大口的黑狼。"

    "一名骑兵从队列中驰出，手持白旗。"

    hide captain_img with dissolve

    "他在城墙下停住，仰头大喊——"

    $ hide_all_chars("soldier_generic_img")
    show soldier_generic_img at left with dissolve
    vanguard "城内领主听着！冯·哈根男爵的先锋部队已经到达！"

    vanguard "男爵再次给你机会——打开城门，加入联军！否则——"

    vanguard "我们将把这座城堡从地图上抹去！"

    "你站在城垛后面，冷冷地看着他。"

    menu:
        "用弓箭回复——射断他的白旗":
            $ change_stat("power", 3)
            $ change_stat("reputation", -2)
            $ play_sound("audio/sfx/arrow_fly.ogg")

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "弓手。"

            $ hide_all_chars()
            "旁边的弓箭手会意，搭箭拉弦。箭矢呼啸而出——精准地射断了那面白旗的旗杆。"

            "先锋官的马受惊跳了几步。他的脸色铁青，拨马回去了。"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "这就是我的回答。"

            "城墙上的士兵爆发出一阵叫好声。但你知道——这意味着谈判的窗口彻底关闭了。"

        "冷静地拒绝":
            $ change_stat("reputation", 2)

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "回去告诉男爵——艾登堡不接受威胁。但如果他愿意以平等的身份对话，我们的大门敞开。"

            $ hide_all_chars()
            $ hide_all_chars("soldier_generic_img")
            show soldier_generic_img at left with dissolve
            vanguard "你会后悔的！"

            "他拨马转身，扬起一阵尘土。"

        "沉默不语，让他自己走":
            $ change_stat("intrigue", 3)

            "你什么也没说。"

            "先锋官等了很久，脸上的怒意渐渐变成了不安。"

            "最终，他拨马离开了。"

    "半个时辰后——敌军开始移动了。"

    scene bg castle_exterior with dissolve

    show captain_img at left with dissolve

    captain "他们分成了三队！左翼和右翼各百骑，正面约百骑！"

    captain "看阵型——他们打算试探性进攻。不是全力攻城，是在摸我们的底细。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "明白了。他们想看看我们有多少人，守备怎么样。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "领主大人，怎么应对？"

    $ hide_all_chars()
    "你快速分析了局势。三百骑兵，不足以攻城，但足以造成压力。他们的真正目的是侦察。"

    "如果你让他们轻松摸清了底细，主力到达后就会对着你的软肋下刀。"

    "如果你能给他们一个深刻的教训——主力部队就会犹豫。"

    hide captain_img with dissolve

    menu:
        "伏击——引诱他们进入埋伏圈":
            $ ch5_exp_skirmish_tactic = "ambush"
            $ change_stat("intrigue", 5)

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "把城门打开。"

            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve

            captain "打开？！领主大人！"

            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "听我说。城门打开，但在城门内侧两边埋伏弓箭手和长枪兵。"

            player "同时在城门前的道路两侧挖好的壕沟里铺上干草和火油。"

            player "他们看到城门大开，一定会以为我们在投降或者出了什么变故。骑兵的本能是冲锋。"

            player "等他们冲到壕沟位置——点火。同时弓箭手齐射。"

            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "……好一个口袋阵。"

            hide captain_img with dissolve

            $ hide_all_chars()
            "准备工作在紧张中完成。城门缓缓打开，像一个张开的嘴巴。"

            "敌军骑兵果然犹豫了。他们在远处观望了一会儿，然后先锋官挥了挥手——约五十骑开始朝城门方向慢慢推进。"

            "越来越近。你能看到马蹄扬起的尘土，听到铁蹄敲击地面的节奏。"

            "三百步……两百步……一百步……"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "点火！"

            $ play_sound("audio/sfx/fire_burst.ogg")

            $ hide_all_chars()
            "壕沟里的干草和火油轰然燃起，火墙瞬间蹿起两丈高！"

            "冲在最前面的骑兵来不及勒马，连人带马栽入了火海。惨叫声和马的嘶鸣声混在一起。"
            if map_studied:
                "壕沟的位置正是雷恩照你昨夜在鹰隼峡圈下的地形定的——干草铺到哪一步、火油泼多宽，他都按你画的算过。"
                "第一排骑兵栽进去时，没有一匹冲得出火墙。"
                $ change_stat("intrigue", 3)

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "弓手！放箭！"

            $ play_sound("audio/sfx/arrow_fly.ogg")

            $ hide_all_chars()
            "箭雨从城门两侧的埋伏位置倾泻而出。混乱中的骑兵成了活靶子。"

            "不到一刻钟，敌军先锋就陷入了彻底的混乱。残余的骑兵拼命后撤，丢下了十几具尸体和更多受伤的战马。"

            $ ch5_exp_skirmish_result = "victory"
            $ ch5_exp_enemy_morale_hit = True
            $ ch5_exp_casualties = 3
            $ change_stat("power", 3)

            "你关上了城门。城墙上爆发出震天的欢呼声。"

            "第一战，大胜。我方仅三人轻伤。"

        "正面迎击——用弓箭和城防阻击":
            $ ch5_exp_skirmish_tactic = "frontal"
            $ change_stat("power", 3)

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "所有弓手上城墙！准备滚石和火油！"

            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve

            captain "是！全体弓手就位！"

            hide captain_img with dissolve

            $ hide_all_chars()
            "敌军骑兵开始向城墙逼近。他们排成松散的队形，试图减少弓箭的杀伤。"

            "但城墙上的弓手们训练有素。"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "等他们进入射程——齐射！"

            $ play_sound("audio/sfx/arrow_fly.ogg")

            $ hide_all_chars()
            "第一轮箭雨落下，几名骑兵翻身落马。但其他人迅速散开，从不同方向逼近。"

            "他们不是来攻城的——而是在城墙下来回奔驰，用弓箭向城墙上射击，试图压制守军。"

            "一支流箭擦过你的耳畔。你连眼睛都没眨。"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "稳住！不要浪费箭矢！只打有把握的目标！"

            $ hide_all_chars()
            "双方你来我往地交锋了将近一个时辰。敌军留下了二十多具尸体，但城墙上也有伤亡——五名弓手中箭，其中两人伤势较重。"

            "最终，敌军鸣金收兵，退出了射程。"

            $ ch5_exp_skirmish_result = "pyrrhic"
            $ ch5_exp_casualties = 7
            $ change_stat("loyalty", 2)

            "你看着城墙上被血染红的石砖，心中沉重。"

            "这只是先锋。真正的大战还没开始。"

        "诱敌深入——故意示弱，让他们轻敌":
            $ ch5_exp_skirmish_tactic = "lure"
            $ change_stat("intrigue", 5)

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "让城墙上只留十个弓手。其余人全部隐藏起来。"

            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve

            captain "只留十个？"

            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我要让他们以为我们只有很少的守军。这样他们回去汇报后，主力会轻视我们。"

            player "让他们轻敌。轻敌了，就会露出破绽。"

            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "领主大人……高明。"

            hide captain_img with dissolve

            $ hide_all_chars()
            "敌军骑兵试探性地逼近。城墙上稀稀拉拉地射出几支箭——故意偏了不少。"

            "骑兵们越发大胆，甚至有人驰到城墙下嘲笑。"

            $ hide_all_chars("soldier_generic_img")
            show soldier_generic_img at left with dissolve
            vanguard "就这点人？男爵说得没错——这座城堡就是一只纸老虎！"

            "你在城墙后面听着他们的嘲笑，面无表情。"

            "让他们笑吧。你等得起。"

            "敌军在城下耀武扬威了一阵，然后心满意足地撤退了。他们认为已经摸清了你的「底细」。"

            $ ch5_exp_skirmish_result = "retreat"
            $ ch5_exp_enemy_morale_hit = False
            $ ch5_exp_casualties = 0

            "没有伤亡。但真正的胜利，要等到主力到来时才能见分晓。"

    scene bg castle_exterior with dissolve

    ## --- 战后的现实 ---

    if ch5_exp_casualties > 0:
        "战斗结束后，你走下城墙，来到临时搭建的伤兵棚。"

        if built_clinic:
            "玛格丽特带着诊所的两个学徒在棚里坐镇，大夫和修女们听她调度。伤员没有一个因为等不到人而死。"
        else:
            "大夫和修女们忙碌地穿梭在伤员之间。空气中弥漫着血腥味和草药的苦涩。"

        "一个受了箭伤的年轻士兵躺在草席上，脸色苍白。你认出了他——就是昨晚写不出信的那个人。"

        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "汤姆？"

        $ hide_all_chars("soldier_generic_img")
        show soldier_generic_img at left with dissolve
        young_soldier "领主……大人……"

        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "你会没事的。大夫说只是擦伤。"

        $ hide_all_chars("soldier_generic_img")
        show soldier_generic_img at left with dissolve
        young_soldier "我……我没给您丢脸吧？"

        $ hide_all_chars("player_char_img")
        show player_char_img sad at left with dissolve
        player "你是最勇敢的战士。"

        $ hide_all_chars()
        "他笑了笑。然后闭上了眼睛。"

        "你站在伤兵棚外面，感到一种锥心的痛。"

        "你能承受得住吗？"

        "你必须承受得住。"

    if ch5_exp_skirmish_result == "victory":
        hide player_char_img
        $ hide_all_chars("captain_img")
        show captain_img at left with dissolve
        captain "领主大人，大胜！此战歼敌近四十人，俘虏七人！"
        captain "敌军先锋部队已经退出了五里之外。短时间内不会再来了。"
        hide captain_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "审讯俘虏。我要知道男爵主力的确切位置和兵力部署。"
        hide player_char_img
        $ hide_all_chars("captain_img")
        show captain_img at left with dissolve
        captain "是！"

        $ hide_all_chars()
        "俘虏的供词印证了之前的情报——男爵主力约两千人，预计两天后到达。"
        "此外，你还得到了一个重要消息——男爵军中有一批从西方雇来的攻城器械师。"
        "如果他们带来了投石车或攻城塔……城墙的优势就会大打折扣。"

        $ ch5_exp_deserter_intel = True
        $ change_stat("intrigue", 3)

        hide captain_img with dissolve

        if not baron_field_power_broken and (power >= 55 or intrigue >= 50):
            $ mark_important_choice()
            menu:
                "乘胜追击——趁男爵联军动摇，先统一北境|击溃前期强敌，获得周边领主兵力":
                    $ baron_field_power_broken = True
                    $ northern_lords_unified = True
                    $ alliance_baron = False
                    $ change_rel("rel_baron", -35)
                    $ change_stat("power", 5)
                    $ change_stat("reputation", 5)

                    $ hide_all_chars("player_char_img")
                    show player_char_img at left with dissolve
                    player "三百先锋败了，男爵主力还没到。现在退回城里，只是在等他重新攥紧拳头。"
                    player "把俘虏口供和联军名册抄三份。艾琳娜，送给那几个被男爵强征来的领主。雷恩，点齐能走的兵。"

                    hide player_char_img
                    $ hide_all_chars("captain_img")
                    show captain_img at left with dissolve
                    captain "您要在他的两千人合流之前，直接端掉军营？"

                    hide captain_img
                    $ hide_all_chars("player_char_img")
                    show player_char_img at left with dissolve
                    player "不是打两千人。是让两千人里真正愿意替他死的，先显出来。"

                    $ hide_all_chars()
                    "当天夜里，男爵联军的三座营门同时起了火。不是你的兵点的——是收到名册的北境领主自己动了手。"
                    "他们本就不愿替冯·哈根送命。先锋惨败、粮道暴露，给了他们退出联军的理由。你带兵压到鹰隼峡时，五面领主旗在阵前倒转，矛尖一齐指向黑狼旗。"
                    "男爵试图用八百铁骑冲开缺口。雷恩没有接战，只守住峡口；失去步兵和粮车的骑兵绕了两次，最终护着男爵退回格鲁瓦尔德堡。"
                    "这一战没有歼灭两千五百人。你做的是更彻底的事——拆掉了把他们绑在一起的那只手。"
                    "三天后，六位北境小领主在艾登堡签下共同防务约书。男爵仍有城堡和残余铁骑，却再也不能代表整个北方。"

                "见好就收——守住艾登堡，不把胜利押在追击上":
                    $ hide_all_chars("player_char_img")
                    show player_char_img at left with dissolve
                    player "我们的任务是守城，不是被一场小胜冲昏头。收拢兵马，封死城门。"
                    $ hide_all_chars()
                    "男爵的先锋退回主力。你保住了人，却也给了黑狼重新整队的时间。"

    elif ch5_exp_skirmish_result == "pyrrhic":
        "你回到城墙上。士兵们在清理战场——收集敌军留下的箭矢和武器。每一支箭、每一把剑都是宝贵的资源。"

        $ hide_all_chars("captain_img")
        show captain_img at left with dissolve
        captain "领主大人，伤亡统计出来了。七人受伤，其中两人重伤。无人阵亡。"
        captain "但箭矢消耗了三成。如果按这个速度，撑不过三次大规模进攻。"
        hide captain_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "让铁匠加紧赶制。同时把敌军留下的箭回收利用。"
        hide captain_img with dissolve

    else:
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "他们走了。而且——看起来非常得意。"
        elena "他们一定会告诉男爵，艾登堡兵力空虚，不堪一击。"
        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "那就好。"
        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "你故意的。"
        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "兵法有云——「能而示之不能。」"
        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "你越来越可怕了，领主大人。"
        hide elena_img with dissolve

    ## ── backlog7·人物弧光: 雷恩抗命私修北墙 (勾 ch5 城防菜单"不做特别处理") ──
    if ch5_north_wall_neglected:
        $ hide_all_chars()
        "战报里有一处你盯了很久：敌军先锋在北墙试探了两轮，没讨到便宜，才转向别处。"

        "你的命令是「北墙暂时够用」。"

        "你去了北墙。内侧新砌了整整一排石料，灰浆还没干透。活很细，是老石匠的手艺。"

        $ hide_all_chars("captain_img")
        show captain_img at left with dissolve
        captain "是我改的。用的我自己的饷银，换防的空档干的活，没占白天一个工。"

        captain "您可以罚我。但那段墙后面，睡着城里四十几户人。"

        hide captain_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve

        menu:
            "「罚一个月饷。然后把南墙也照这个修法给我修了。」":
                $ change_rel("rel_captain", 6)
                $ change_stat("loyalty", 3)
                $ log_decision("第五章", "认下雷恩的抗命，罚饷并委以南墙")
                player "罚一个月饷。然后——把南墙也照这个修法给我修了。"
                $ hide_all_chars("captain_img")
                show captain_img at left with dissolve
                captain "……是。"
                $ hide_all_chars()
                "他敬了个礼，转身就走。你看见他嘴角压着一点没压住的东西。"
                "罚单当天贴出去了。当晚军营里没人议论罚饷的事，人人都在说南墙。"

            "「下不为例。」":
                $ change_rel("rel_captain", -4)
                $ change_stat("power", 2)
                $ log_decision("第五章", "警告雷恩不得再抗命")
                player "墙修得好。但命令就是命令——下不为例。"
                $ hide_all_chars("captain_img")
                show captain_img at left with dissolve
                captain "是。"
                $ hide_all_chars()
                "一个字，干脆利落。他的军礼一丝不苟，眼神照直——你知道，下一次他还会这么干。"

    $ hide_all_chars()
    "前哨战结束了。但每个人都知道——这只是暴风雨前的闪电。"

    "真正的风暴，正在地平线上聚集。"

    return

## ============================================================
## 第五部分：风暴前的抉择 — Eve of Battle (~300行)
## ============================================================

label ch5_exp_eve_of_battle:

    $ play_music("audio/music/tension.ogg", fadein=2.0)

    scene bg study with dissolve
    $ unlock_gallery("bg_study")
    $ set_mood("tense")

    "前哨战后的第二天。"

    "三封信几乎同时到达了艾登堡。"

    "你把它们展开在书桌上，逐一审视。"

    ## --- 王后的最后通牒 ---

    "第一封：王后伊莎贝拉的亲笔信。印着王室火漆，字迹端庄而冰冷。"

    $ hide_all_chars("queen_img")
    show queen_img angry at left with dissolve
    $ unlock_gallery("queen")

    queen "致艾登堡领主——"

    queen "本宫最后一次给你选择的机会。"

    queen "冯·哈根男爵是叛国贼。支持他的人，都将以叛国罪论处。"

    queen "但如果你在三天内打开城门，向王室效忠——"

    queen "本宫不仅既往不咎，还将封你为北方总督，统管五个领地。"

    queen "这是本宫最后的仁慈。三天之后，蒙塔古伯爵的大军将替本宫讨回一切。"

    hide queen_img with dissolve

    $ hide_all_chars()
    "你放下王后的信。五个领地的管辖权——这个诱饵比上次更大了。"

    "但你比谁都清楚——王后的承诺和她的毒药一样不可信。"

    if father_murder_mastermind_known:
        "而且——这个女人毒杀了你的父亲。无论她许诺什么，你都不会忘记这一点。"

    menu:
        "写一封措辞模糊的回信，拖延时间":
            $ ch5_exp_queen_ultimatum = "counter"
            $ change_stat("intrigue", 3)

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "回信就这么写——「陛下恩典，臣感激涕零。然北方局势复杂，容臣三日内安排妥当，即刻率部南下效忠。」"

            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "你根本不打算南下。"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "当然不。但这能给我们争取三天时间。三天之内，很多事都可能发生。"
            hide elena_img with dissolve

        "明确拒绝":
            $ ch5_exp_queen_ultimatum = "reject"
            $ change_stat("reputation", 3)
            $ change_stat("power", 2)
            $ change_rel("rel_queen", -10)

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "不需要回信。沉默就是最好的答案。"

            $ hide_all_chars()
            "你把王后的信扔进了壁炉。火焰吞噬了那些华丽的辞藻和虚伪的承诺。"

            "让她来吧。该来的总会来。"

        "假意接受，暗中设计":
            $ ch5_exp_queen_ultimatum = "accept"
            $ change_stat("intrigue", 5)
            $ change_stat("faith", -2)  ## balance pass 修法 1: 假意答应换取布局空间, 欺骗换胜利

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "回信告诉她——我接受条件。请蒙塔古伯爵派一支小队来接收城堡。"

            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "你想引蛇出洞？"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "蒙塔古伯爵如果派人来，就说明他信了。到时候我们可以直接和他谈判——绕过王后。"
            player "如果他不信，至少也会犹豫几天。犹豫就意味着他没有全力进攻。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "险棋。但……值得一试。"
            hide elena_img with dissolve

    ## --- 男爵的威胁 ---

    "第二封信：男爵的密函。没有火漆，用粗糙的麻纸包裹，字迹潦草。"

    $ hide_all_chars("baron_img")
    show baron_img angry at left with dissolve
    $ unlock_gallery("baron")

    baron "艾登堡的小鬼——"

    if ch5_exp_skirmish_tactic == "lure":
        baron "你那点小把戏挺有意思——装可怜骗了我的先头骑兵。"
    else:
        baron "你的先锋部队给了我的人一个教训。好得很。"

    baron "但你以为这改变了什么吗？"

    baron "我的两千铁骑已经在路上了。你那座破城堡，在我面前就像纸糊的一样。"

    baron "最后的机会——交出你手中的遗诏和证据，打开城门。"

    baron "否则——我保证让艾登堡的每一块石头都浸满鲜血。"

    hide baron_img with dissolve

    "男爵的信比王后的更直白。他不玩虚的——他直接威胁。"

    if father_letters_found:
        "而且他提到了遗诏——他知道你手中有证据。这意味着他的间谍网络比你想象的更深。"

    if baron_blackmail_option:
        "你想起了男爵的秘密——那段他极力掩盖的过去。如果把这个筹码亮出来，也许能让他的威胁变成一纸空文。"

    menu:
        "嗤之以鼻地拒绝":
            $ ch5_exp_baron_response = "reject"
            $ change_stat("power", 3)

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "让他来。我倒要看看他的两千铁骑怎么爬城墙。"

            "你把男爵的信和王后的信一起扔进了壁炉。"

        "利用男爵信中的情报":
            $ ch5_exp_baron_response = "exploit"
            $ change_stat("intrigue", 4)

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "这封信透露了不少信息。"

            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve

            elena "他说「两千铁骑」——但之前的情报是两千五百人。"

            elena "要么他在虚张声势，要么——有五百人脱离了联军。"

            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "联系维克托领主。如果是他带走了五百人……也许他真的在考虑倒戈。"

            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "我这就安排。"

            hide elena_img with dissolve

        "假装投降，实际上准备里应外合" if ch5_exp_war_strategy == "divide":
            $ ch5_exp_baron_response = "accept"
            $ change_stat("intrigue", 5)

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "回信告诉男爵——我愿意交出证据。请他亲自来取。"

            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "你疯了？万一他真来了——"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "他不会来。但他的亲信会。一个能直接和男爵身边人对话的机会——比任何间谍都值钱。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "……你比我想象的更像间谍。"
            hide elena_img with dissolve

        "用他的把柄反威胁" if baron_blackmail_option:
            $ ch5_exp_baron_response = "blackmail"
            $ change_stat("intrigue", 5)
            $ change_stat("reputation", -3)  ## 威胁手段的代价: 名声受损 (balance pass 修法 1)

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "回信告诉男爵——他在南方的那些旧事，我全都知道。"
            player "如果他不收回威胁，这些证据会传遍整个王国。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "你手里真有这些东西？"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "有。而且足以毁掉他。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "好手段。但小心——被逼入绝境的猛兽最危险。"
            hide elena_img with dissolve

    ## --- 暗百合的建议 ---

    if dark_lily_joined:

        scene bg dungeon with dissolve
        $ unlock_gallery("bg_dungeon")

        $ hide_all_chars()
        "第三封信——如果能叫信的话——是一片黑色的纸片，上面只有两行字，墨迹在烛光下隐隐发亮。"

        "你认得那笔迹——暗百合首领亲书。"

        "「年轻的领主。暗百合已经做好了准备。」"

        "「在男爵军中，我们有十二个人。在王后军中，有八个。」"

        "「你只需要给一个信号——任何时候——他们就会行动。」"

        "「但请记住：暗百合只行动一次。一次之后，他们的身份就会暴露。」"

        "「所以——选择最好的时机。」"

        if lily_double_agent:
            "纸片的背面还有一段更小的字——"

            "「对了——你安插的那个双面间谍传回了一份绝密情报。」"

            "「男爵的军师与伯爵有私下联络。他们可能在密谋单独停战，把男爵架空。」"

            "「这个情报价值连城——你可以用它来分化敌军指挥层。」"
            $ change_stat("intrigue", 3)

        "信末没有署名。只有一朵小小的暗色百合印记。"

        menu:
            "指示他们在关键战役时制造混乱":
                $ ch5_exp_lily_advice_taken = True
                $ change_stat("intrigue", 5)
                $ change_rel("rel_lily", -10)

                "你在回信的空白处提笔——斟酌了许久才落下第一个字。"

                "「等双方主力交战最激烈的时候再行动。」"

                "「在男爵军中散布假消息说后方被偷袭。在王后军中放火烧粮草。」"

                "「信号——城楼上升起三面黑旗。」"

                "你将纸片封入蜡丸，交给等在窗外的暗影信使。"
                "散布假消息、烧粮草——要动用的人手是最多的。十二个加八个，几乎全数要露面。"
                "几天后回执到了，只有一行小字：「这一次，我们押上了所有人。希望它值得。」"

            "让暗百合暗杀男爵军中的关键将领":
                $ ch5_exp_lily_advice_taken = True
                $ change_stat("intrigue", 4)
                $ change_stat("power", 2)
                $ change_rel("rel_elena", -8)

                "你落笔回复——字迹冷硬如刀。"

                "「男爵联军的号令本就不齐。战前夜除掉一两个关键将领——联军就会自行瓦解。」"

                "「暗杀有风险。若失败，你们的人会暴露。」"

                "「但我相信暗百合的能力。」"

                "你合起蜡丸，将它交予窗外的信使。对方没有回话，只留下一片压低的羽毛作为回执。"
                $ hide_all_chars("elena_img")
                show elena_img at left with dissolve
                elena "战前一夜在自己人的营帐里割喉……"
                elena "我不拦你。但这种事做了，就别指望我替你说它干净。"
                hide elena_img with dissolve

            "暂时保留这张底牌":
                $ ch5_exp_lily_advice_taken = False
                $ change_rel("rel_lily", 8)

                "你提笔作答——字句简短。"

                "「还不是时候。我需要看到战场上的局势才能做判断。」"

                "几天后，一片新的黑色纸片又悄无声息地出现在书桌上。"

                "「沉得住气。一次性的刀，不该为了一时痛快就拔出来。」"

                "「我的人会等你的信号。别让他们等到战事结束。」"

    elif dark_lily_destroyed:
        $ hide_all_chars()
        "第三封信——来自一个没有署名的人。字迹歪歪扭扭，写在一块破布上。"

        "「城中有人记得你父亲的恩情。如果你需要帮助，在城墙上挂一面黑旗。」"

        "你盯着这块破布看了很久。暗百合虽已被你铲除，可你父亲这些年在城中留下的善意，仍在悄无声息地流转。"

        menu:
            "把黑旗备好，以防万一":
                $ change_stat("intrigue", 2)
                "你把一面黑旗放在了城楼的角落。不一定会用——但有备无患。"

            "忽略这封信":
                "你把破布扔到了一边。陌生人的善意，代价往往比你想象的要大。"

    else:
        $ hide_all_chars()
        "第三封信——来自一个没有署名的人。字迹歪歪扭扭，写在一块破布上。"

        "「城中有暗百合的旧人。如果你需要帮助，在城墙上挂一面黑旗。」"

        "你盯着这块破布看了很久。暗百合——即使你没有加入他们，他们的影子似乎也无处不在。"

        menu:
            "把黑旗备好，以防万一":
                $ change_stat("intrigue", 2)
                "你把一面黑旗放在了城楼的角落。不一定会用——但有备无患。"

            "忽略这封信":
                "你把破布扔到了一边。暗百合的帮助，代价往往比你想象的要大。"

    ## --- 最终战略布局 ---

    scene bg great_hall with dissolve
    $ unlock_gallery("bg_great_hall")

    "处理完所有信件后，你最后一次站在了地图前。"

    "所有的信息都在这里了。两支敌军的位置、兵力、弱点。你的资源、盟友、底牌。"

    "现在，你需要做出最终的战略布局——这将决定明天的战斗如何展开。"

    show captain_img at right with dissolve

    hide captain_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "领主大人，一切准备就绪。就等您的最终命令了。"

    hide aldric_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "士兵们已经就位。不管什么命令，他们都会执行。"

    "你的目光在地图上缓缓移动。最终，手指停在了一个位置上。"

    menu:
        "铁壁阵——以绝对防御消耗敌军":
            $ ch5_exp_final_formation = "iron_wall"
            $ change_stat("power", 5)
            $ ch5_exp_defender_bonus += 5

            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "全军固守。把所有兵力集中在城墙上。"

            player "每一块石头都是我们的武器。每一个箭垛都是一座堡垒。"

            player "不主动出击，不浪费一个人。让他们来撞墙——撞到头破血流为止。"

            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "铁壁阵！明白！我这就去重新部署！"

            "这是一个纯粹的消耗战策略。你赌的是——敌军的耐心和粮草，都会在你之前耗尽。"

        "暗刃阵——在防御中寻找反击机会":
            $ ch5_exp_final_formation = "hidden_blade"
            $ change_stat("intrigue", 5)
            $ ch5_exp_defender_bonus += 3

            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "表面上固守，但暗中留出一支精锐作为奇兵。"

            if secret_passage_found and not (ch1_deep_cellar_choice == "seal" and not passage_re_opened):
                if passage_re_opened:
                    player "雷恩，挑选五十名最精锐的士兵，从那条重新打通的密道出城，埋伏在北面的树林里。"
                else:
                    player "雷恩，挑选五十名最精锐的士兵，从密道出城，埋伏在北面的树林里。"
                if aldric_knows_passage:
                    player "让奥尔德里克带路——他比任何人都熟悉那条密道的每一个拐角。"
                    "有奥尔德里克的引导，这支奇兵能以最快的速度穿过密道，不留任何痕迹。"
                    $ ch5_exp_defender_bonus += 2
            else:
                player "雷恩，挑选五十名最精锐的士兵，趁夜色从北门出城，埋伏在北面的树林里。"

            player "等敌军全力攻城时，从背后突袭他们的指挥部。"

            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "釜底抽薪！如果能打掉他们的指挥官——"

            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "整支军队就会陷入混乱。到时候城内也全力出击，一举破敌。"

            $ hide_all_chars()
            "这是一个高风险高回报的策略。一旦成功，可以以少胜多。但如果那五十人被发现——你就少了五分之一的兵力。"

        "圣盾阵——以教会之名化解敌意" if alliance_church or faith >= 60:
            $ ch5_exp_final_formation = "holy_shield"
            $ change_stat("faith", 5)
            $ change_stat("reputation", 3)

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "在城墙上升起教会的旗帜。让主教率领教士们站在最前面。"

            player "蒙塔古伯爵是虔诚的信徒。他的士兵也是。当他们看到教会的旗帜——"

            player "他们会犹豫。犹豫就意味着不会全力进攻。"

            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve

            bishop "您要把教会作为盾牌？"

            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "不是盾牌。是良心。我在给蒙塔古伯爵的士兵一个不战而退的理由。"

            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "……这确实可能奏效。至少对南军是这样。"

            hide bishop_img with dissolve

            $ hide_all_chars()
            "这是一个用信仰作为武器的策略。它可能瓦解南方王后军的进攻意志——但对不信教的北方男爵联军无效。"

        "民堡阵——全民皆兵，守护家园" if loyalty >= 60:  ## balance pass 修法 3: 50→60
            $ ch5_exp_final_formation = "peoples_bastion"
            $ change_stat("loyalty", 5)
            $ ch5_exp_defender_bonus += 4

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "每一个能拿得动东西的人，都是守城的力量。"

            player "士兵守城墙，民兵守街道，妇女老人在后方搬运物资和救治伤员。"

            player "每一条巷子都是防线。每一间房子都是堡垒。"

            player "就算他们攻破了城墙——他们也休想轻松占领这座城堡。"

            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve

            aldric "全民皆兵……领主大人，这意味着平民也会有伤亡。"

            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我知道。所以我会站在最前面。如果领主都不怕死，百姓就不会退缩。"

            hide player_char_img with dissolve

            "这是一个与人民共存亡的策略。它能最大限度地发挥你的人力优势——但代价可能是惨重的平民伤亡。"

    hide aldric_img with dissolve
    hide captain_img with dissolve

    ## --- 铺垫五大结局 ---

    scene bg study with dissolve

    "部署完毕后，你独自坐在书房里。"

    "蜡烛燃到了尽头，发出最后一点微弱的光。"

    "你看着地图上代表艾登堡的那个小小标记。"

    "明天之后，这个标记可能变成一个战场——也可能变成一个传奇。"

    if power >= 50:
        "你把腰间的剑拔出一寸又推了回去。够了——明天让它说话。"
    if intrigue >= 50:
        "你微微一笑。棋盘已经摆好，所有的棋子都在它们应该在的位置上。接下来，只需要等待对手犯错。"
    if faith >= 50:
        "你闭上眼，在心中默念了一句祷词。念完，按在剑柄上的手松开了。"
    if loyalty >= 50:
        "你望向窗外。城堡里灯火通明——你的人民没有一个人逃跑。他们选择留下来，和你一起面对风暴。"
    if testament_original_obtained:
        "你打开密室，最后一次审视了那份遗诏。这张薄薄的羊皮纸上，写着足以颠覆一切的真相。也许明天——真相就是你最锋利的武器。"

    "你吹灭了蜡烛。"

    "黑暗中，你听到了风声。"

    "风从北方来，带着铁和血的味道。"

    "风暴已经来了。"

    if ch5_exp_speech_given or ch5_exp_aldric_legacy or ch5_exp_captain_oath or ch5_exp_elena_promise:
        "但你不是一个人。"
        "你的身后，站着每一个愿意为你而战的人。"

    "你站起身，推开书房的门，走进了黎明前最黑暗的那一刻。"

    "当太阳再次升起的时候——"

    "一切都将揭晓。"

    return

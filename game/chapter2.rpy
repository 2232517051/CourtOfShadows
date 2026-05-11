## ============================================================
## 第二章：领主会议
## ============================================================

label chapter2_start:

    ## 安全重置：防止上一章过场动画的 _dismiss_pause 泄漏
    $ _dismiss_pause = True
    $ quick_menu = True
    window auto

    $ renpy.force_autosave()
    $ snapshot_chapter_start()

    scene black with fade

    call show_chapter("第二章", "领主会议", "贵族间的明争暗斗") from _call_show_chapter
    call show_recap("chapter1") from _call_show_recap
    call apply_rel_chapter_effects from _call_rel_ch2

    ## 章节过场动画
    call cinematic_chapter2 from _call_cinematic_ch2

    "一个月过去了。"

    "艾登堡在你的治理下勉强度过了初冬。第一道政令的效果已经显现——"

    if first_decree == "军事":
        "边境巡逻队多次击退了小股盗匪，士气高涨。但粮食问题依然严峻。"
    elif first_decree == "民生":
        "百姓感念你的仁慈，领地内人心安定。但金库空虚，让你夜不能寐。"
    elif first_decree == "治安":
        "商路重开后，税收明显回升。但北方边境的防务仍是隐患。"
    elif first_decree == "建设":
        "城堡焕然一新，如同铁壁。"
        if secret_passage_found:
            "而那条密道的秘密，只有你和奥尔德里克知道。"

    "今天，区域领主会议即将召开。这是你第一次以领主身份出席。"

    "哈伦堡——中立城镇，距艾登堡两日路程。那里是各领主商议大事的传统之地。"

    "你必须在那里证明自己不只是父亲的影子，而是一个值得尊重的领主。"

    ## 章节间过渡：篝火夜话 + 梦境
    call interlude_ch1_ch2 from _call_interlude12
    call interlude_ch1_ch2_dream from _call_interlude12_dream

    ## NPC支线（第二章可用）— 先揭秘再承诺
    call npc_merchant_karl_past from _call_npc_mkp
    call npc_aldric_secret from _call_npc_as2

    ## NPC深度支线 — 基于已揭秘的骑士团身份展开
    if aldric_personal_done:
        call npc_aldric_promise from _call_npc_ap
    call npc_captain_past from _call_npc_cp2

    ## 治理系统：商会谈判
    call gov_merchant from _call_gov_merch2

    ## 章节深化
    call ch2_deep_church_midnight from _call_ch2_dcm

    ## ============================================================
    ## 场景1：出发前的准备
    ## ============================================================

label ch2_preparation:

    $ play_music("audio/music/castle_calm.ogg", fadein=2.0)
    scene bg study with dissolve
    $ unlock_gallery("bg_study")

    $ trigger_random_event("rest")

    "清晨的书房里，微弱的阳光从窗棂间漏进来，在地板上画出淡金色的格子。"

    "你坐在父亲留下的那张橡木桌前，桌上铺满了地图和文书。"

    "哈伦堡的地形图、各领主的家徽画册、去年的会议纪要——一夜未眠，你把能找到的资料都翻了一遍。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    $ unlock_gallery("aldric")

    aldric "领主大人，关于此次会议，老臣有几点要提醒。"

    aldric "与会者共有五位领主，但真正需要注意的只有两个人。"

    aldric "一是冯·哈根男爵。上次的事他不会忘。"

    if rel_baron > 0:
        aldric "不过，你之前的外交手腕似乎让他对你有了些许好感。这是好事。"
    else:
        aldric "他对我们怀恨在心，今日必定会发难。"

    aldric "二是王后的代表。据说王后本人不会出席，但她的眼线无处不在。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "其他三位领主呢？"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "东边的格雷伯爵，老成持重，向来不偏不倚。他在会上很少发言，但一旦开口，往往一锤定音。"

    aldric "南边的威尔斯子爵，与男爵有姻亲关系，但此人贪财，利字当头什么亲戚都能卖。"

    aldric "还有西面的施泰因伯爵夫人，她丈夫在南方战役中战死，如今独自撑起领地。是个厉害的女人。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "看来每个人都不简单。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "权谋之局，从无简单之人。领主大人务必谨慎。"

    aldric "对了，路途需要两天，沿途并不太平。老臣建议带足护卫。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你不随行吗？"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "老臣年事已高，这把老骨头经不起两天的颠簸了。城堡的事务也需要人坐镇。"

    aldric "但艾琳娜会随行。她对宫廷礼仪和各家底细都颇为熟悉。"

    "奥尔德里克顿了顿，目光变得意味深长。"

    aldric "另外……注意她的一举一动。她是王后派来的人，别忘了这一点。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你是说，她可能会在会上替王后说话？"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "老臣只是提醒您——在权谋之庭里，每个人都有自己的角色。包括老臣自己。"

    hide aldric_img with dissolve
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    $ unlock_gallery("elena")

    elena "领主大人，关于会议，我也有些消息。"

    elena "王后近来在削减地方领主的权力。这次会议，她可能会借机推行新税法。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "新税法？具体是什么内容？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "将各领地的税收上缴比例从两成提高到三成。表面上是为了王室的军费开支，实际上……"

    elena "是为了削弱各领主的财力，从而巩固王室的中央集权。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你作为王后的人，告诉我这些，不怕她知道？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "领主大人，我是来协助您的。我的职责是让您做出最明智的决定——"

    elena "不论那个决定对王后是否有利。"

    "她的语气很诚恳，但你没有错过她嘴角那一瞬间的犹豫。"

    ## 阿威克反馈 (batch 13 #4, 2026-05-11): 玩家 61 分钟仍困惑艾琳娜好坏,
    ## 加 5 行内心独白释疑 — 不破悬念, 让玩家知道"她至少站在你这边".
    $ hide_all_chars()
    "她还在隐瞒什么——这一点你心里清楚。"

    "可你今晚来之前对新税法一无所知，现在你心里有底了。"

    "出门前你不知道有人在背后议论你的安危，现在你知道了。"

    "她的身份你以后总会查清——但今晚的两次提点，都是实打实救你于风险。"

    "至少这一点，你愿意先信。"

    if rel_elena >= 15:
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "另外……有人在暗中筹划对你不利的事。请务必小心。"
        $ change_stat("intrigue", 5)

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "什么样的事？你能说得更具体些吗？"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "我只是偶然听到一些只言片语。有人在讨论'艾登堡的新领主走不出哈伦堡'。"

        elena "我不确定是谁说的，但……请您路上多加提防。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "多谢提醒。"

    "你如何准备这次会议？"

    menu:
        "仔细研究每位领主的底细" if intrigue >= 25:
            $ change_stat("reputation", 5)
            $ change_rel("rel_elena", 5)
            player "艾琳娜，把你知道的每个人的弱点都告诉我。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "领主大人英明。"
            elena "东边的格雷伯爵欠了教会一大笔债；南边的威尔斯子爵与男爵有姻亲关系……"
            elena "施泰因伯爵夫人虽然精明强干，但她的领地今年遭了旱灾，急需外部援助。"
            elena "至于男爵……他最大的弱点是虚荣。他比任何人都在乎面子。"
            $ hide_all_chars()
            "你花了一整个上午，将每位与会者的底牌摸了个透。"
            "每个人的姻亲、债务、领地隐患、近年来的政策失误——你一一记在心里。"
            "这是你第一次感受到谋略的力量。信息，有时候比刀剑更加锋利。"

        "准备丰厚的礼物，以示诚意":
            $ change_stat("wealth", -10)
            $ change_stat("reputation", 10)
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "备上我们最好的铁器和皮毛，作为礼物带去。"
            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "明白了。这些礼物虽然花费不少，但能让人看到艾登堡的诚意。"
            $ hide_all_chars()
            "你亲自挑选了礼物：一柄精钢打造的短剑给男爵，一面银质圣像给可能在场的教会代表，"
            "上等的狐皮披肩给施泰因伯爵夫人，一套镶嵌宝石的酒具给威尔斯子爵。"
            "至于格雷伯爵——你选了一本古老的法典抄本。奥尔德里克说他是个学究。"
            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "礼多人不怪。至少能让他们知道，艾登堡虽然换了领主，但排面还在。"

        "带上全副武装的卫队，以示实力":
            $ change_stat("power", 5)
            $ change_stat("loyalty", 5)
            player "雷恩，挑二十个最精锐的士兵随行。全副武装。"
            show captain_img at right with dissolve
            $ unlock_gallery("captain")
            captain "遵命！保证让其他领主知道艾登堡不好惹！"
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "铠甲要擦亮，旗帜要崭新。每个人都要像是随时能上阵杀敌的样子。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "领主大人放心！我挑的人，个个都是刀口上舔过血的。"
            "雷恩兴冲冲地去挑人了。他铠甲上的铁扣还没扣好就跑了出去——这家伙永远比你更急。你摇了摇头：有时候最好的防御就是让敌人不敢进攻。"
            hide captain_img with dissolve

        "向主教请求祝福，借教会之威":
            $ change_stat("faith", 15)
            $ change_rel("rel_bishop", 10)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "请主教在出发前为我们祈福。带上教会的旗帜一同前往。"
            "主教欣然应允。教会的旗帜在你的队伍中格外醒目。"
            hide player_char_img with dissolve
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            $ unlock_gallery("bishop")
            bishop "愿圣光照耀你的前路，领主大人。在这乱世中，信仰是最坚固的盾牌。"
            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "多谢主教大人的祝福。"
            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "路上小心。哈伦堡虽是中立之地，但各方势力盘根错节。"
            bishop "记住，教会永远是你的后盾——只要你不忘圣光的教诲。"
            hide bishop_img with dissolve
            $ hide_all_chars()
            "你带着教会的旗帜出发。一路上，沿途的百姓看到旗帜都跪下祈祷。"
            "教会的影响力，远比你想象的深远。"

    hide elena_img with dissolve

    ## ============================================================
    ## 场景1.5：前往哈伦堡的旅途
    ## ============================================================

    $ set_mood("calm")
    $ set_weather("fog", "light")
    $ play_music("audio/music/castle_calm.ogg", fadein=2.0)
    scene bg forest_path with dissolve
    $ unlock_gallery("bg_forest_path")

    "队伍在晨雾中出发了。"

    "艾登堡的城墙在身后渐渐变小，最后消失在起伏的丘陵之间。"

    "初冬的清晨寒意逼人，呼出的白气在空中凝成一团又一团的小云朵。"

    "道路两旁的橡树已经落尽了叶子，光秃秃的枝干伸向灰蒙蒙的天空，像是一双双干枯的手在祈求什么。"

    "你骑在马背上，身后是二十名卫兵和三辆辎重车。艾琳娜骑着一匹枣红色的母马，紧跟在你右侧。"

    show elena_img at right with dissolve

    elena "领主大人，从这里到哈伦堡，正常行程需要两天。"

    elena "第一天走官道，在渡鸦旅店过夜。第二天穿过莱因河谷，午后就能抵达。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "这条路安全吗？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "官道上一般不会有问题。但过了莱因河之后……那一带的林子很深，盗匪偶有出没。"

    elena "不过有卫队随行，应该不必担心。"

    $ hide_all_chars()
    "你点点头，目光扫过两旁的树林。枯叶在风中簌簌作响。"

    "行至中午，队伍在一处溪流边停下休息。"

    hide elena_img with dissolve

    "士兵们生起篝火，烤起干粮。溪水清冽，倒映着铅灰色的天空。"

    "你坐在一块大石头上，默默整理着思绪。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve

    "艾琳娜端着一碗热汤走过来。"

    elena "领主大人，喝口热的吧。天冷，不能空着肚子赶路。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "多谢。"

    "你接过汤碗，喝了一口。是野菌炖兔肉，味道出乎意料地好。"

    player "你还会做饭？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "在王宫里学的。王后身边的人，什么都得会一些。"

    "她在你身旁坐下，望着城墙下的灯火。"

    elena "领主大人……我可以问您一个问题吗？"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "说。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "您为什么选择继承领地？"

    elena "我听说您在王都的学院里成绩很好，本可以留在那里，谋一个安稳的前程。"

    elena "回到艾登堡，面对的是一堆烂摊子和随时可能兵临城下的邻居。为什么要回来？"

    menu:
        "因为责任——『这是父亲留给我的，我不能丢下。』":
            $ change_stat("loyalty", 5)
            $ change_rel("rel_elena", 5)
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "这是父亲留给我的一切。不管多难，我不能丢下。"
            player "艾登堡的每一个百姓，每一寸土地，都是他用一生守护的。如果我逃了，他泉下有知会瞑目吗？"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "……您比我想象的更像您父亲。"
            "她的眼神中闪过一丝难以捉摸的光，转瞬即逝。"

        "因为真相——『我要查清父亲的死因。』":
            $ change_stat("loyalty", 5)
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "因为父亲死得蹊跷。我回来，不只是为了继承，更是为了找到真相。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "……"
            "艾琳娜的表情微微一变，但很快恢复了平静。"
            elena "真相有时候比谎言更危险，领主大人。"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "但我宁可面对危险的真相，也不愿活在安全的谎言里。"

        "因为野心——『王都太小了，我要自己的天下。』":
            $ change_stat("power", 5)
            $ change_stat("reputation", 5)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "说实话？因为在王都当别人的附庸，不如在自己的领地当家做主。"
            player "学院里教的都是书本上的东西。真正的学问，在这里——在刀尖上，在人心里。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "领主大人倒是坦诚。"
            "她看着你，眼睛弯了一下。"
            elena "我喜欢坦诚的人。在宫廷里，这是最稀缺的品质。"

        "反问她——『你呢？为什么来艾登堡？』":
            $ change_stat("loyalty", 5)
            $ change_rel("rel_elena", 3)
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我倒想问问你。放着王宫的安逸不待，跑到这穷乡僻壤来，为什么？"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "我……"
            "她犹豫了一下。"
            elena "王后的命令，不容拒绝。"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "仅此而已？"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "仅此而已。"
            $ hide_all_chars()
            "她低下头，不再说话。但你注意到她的手指无意识地攥紧了衣角。"
            "这个女人有秘密。不过——谁没有呢。"

    hide elena_img with dissolve

    "下午，队伍继续前行。"

    "官道上偶尔能遇到往来的商队和行脚僧人。你注意到，今天路上的人比平时少了很多。"

    "也许是因为初冬。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "领主大人，前面有情况。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "什么情况？"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "路中间有一辆翻了的马车，看起来是商人的。有几个人在旁边。"

    $ hide_all_chars()
    "你策马上前，看到一辆货车歪在路边的水沟里，一个轮子断了。"

    "三个衣着朴素的人正在试图把货物从车上搬下来。其中一个年纪较大的人看到你的队伍，急忙迎上来。"

    hide captain_img
    $ hide_all_chars("servant_generic_img")
    show servant_generic_img at left with dissolve
    caravan_hand "贵人！求求您帮帮忙！我们的车坏了，货物搬不动，天黑前到不了渡鸦旅店就完了！"

    caravan_hand "这一带入夜后不安全，求贵人行个方便！"

    menu:
        "买下他们这趟运的全部货——一次解决他们整个商队的难题" if wealth >= 40:
            $ change_stat("wealth", -8)
            $ change_stat("reputation", 8)
            $ change_stat("loyalty", 3)
            hide servant_generic_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你们这一车货, 我全要了。运到艾登堡再算账。"
            $ hide_all_chars()
            "商人愣了几秒, 然后跪了下来——这不是答谢, 是发自内心的感激。"
            "他们今天不只是修了车——是不用担心明年开春能不能再启程。"
            "艾登堡在卡尔达商道上的口碑, 从这一刻起多了一个版本。"
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "领主大人……您这一手不是好心, 是经营。"

        "让士兵帮忙修车":
            $ change_stat("reputation", 5)
            $ change_stat("loyalty", 3)
            hide servant_generic_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "雷恩，派几个人帮他们把车修好。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "是。"
            "士兵们七手八脚地帮忙换了备用轮子，又帮商人把货物重新装好。"
            hide captain_img
            $ hide_all_chars("servant_generic_img")
            show servant_generic_img at left with dissolve
            caravan_hand "多谢贵人！多谢！您是哪家的大人？小人日后定当报答！"
            hide servant_generic_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "艾登堡。"
            hide player_char_img
            $ hide_all_chars("servant_generic_img")
            show servant_generic_img at left with dissolve
            caravan_hand "艾登堡！原来是新领主大人！小人听说过您——好人啊！"
            "商人千恩万谢地走了。雷恩瞥了一眼车辙碾过的泥地，嘀咕了一句。"
            hide servant_generic_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "领主大人，您真是好心。不过赶路要紧，咱们得加快步伐了。"

        "保持警惕，先派人查看是否有埋伏":
            $ change_stat("intrigue", 5)
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "等等。先派两个人绕到后面看看，确保没有埋伏。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "领主大人谨慎。"
            "两名士兵从侧面迂回查看，片刻后回来报告。"
            hide servant_generic_img
            $ hide_all_chars("soldier_generic_img")
            show soldier_generic_img at left with dissolve
            soldier "禀领主大人，没有异常。就是普通的商人，车确实坏了。"
            hide soldier_generic_img with dissolve
            "你这才下令帮忙。虚惊一场，但小心无大错。"

        "无暇顾及，继续赶路":
            hide soldier_generic_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我们赶时间。继续走。"
            $ hide_all_chars()
            "商人们失望地看着你的队伍从旁边经过。你听到身后传来低声的咒骂。"
            "有时候，赶路比施恩更重要。但你心里隐约有些不舒服。"

    hide captain_img with dissolve

    "午后的阳光变得稀薄起来。天空中堆满了铅灰色的云，像是要下雪。"

    "你加快了队伍的行进速度。冬天的白昼很短，你不想在天黑后还暴露在荒野上。"

    show elena_img at right with dissolve

    elena "领主大人，看那边。"

    $ hide_all_chars()
    "艾琳娜指向路边。在一棵枯死的橡树下，竖着一块粗糙的石碑。"

    "你走近一看——石碑上刻着几行字，已经被风雨侵蚀得模糊不清。但你还是勉强辨认出来：'此路通哈伦堡，旅人谨行。'"

    "石碑下面还有一行更小的字：'乱世之中，唯谨慎者活。'"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "这块碑据说是上一次内战时立的。那时候，这条路上每天都有人死。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "内战？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "大约四十年前。当时的国王暴毙，几个亲王争夺王位。各领主也被迫站队。"

    elena "最后是现任王后——当时她还是邻国的一位公主——联合了教会和几个大领主，平定了叛乱。"

    elena "从那以后，王后就一直在想办法防止类似的事再次发生。这就是她削弱领主权力的根本原因。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "所以新税法不只是敛财，而是一种预防手段。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "可以这么理解。"

    $ hide_all_chars()
    "你看了艾琳娜一眼。她今天透露的信息比以往任何时候都多。"

    "是因为信任你了，还是因为有人让她这么做？"

    hide elena_img with dissolve

    "傍晚时分，你的队伍抵达了渡鸦旅店。"

    scene bg market with dissolve
    $ unlock_gallery("bg_market")
    $ play_music("audio/music/tavern_lively.ogg", fadein=2.0)

    "这是一座建在官道岔口的石头客栈，门口挂着一只木雕的乌鸦作为招牌。"

    "旅店不大，但干净暖和。壁炉里的火烧得很旺，空气中弥漫着烤肉和麦酒的气味。"

    "你的士兵在旅店外面扎营，你和艾琳娜则住进了楼上的客房。"

    "晚餐时，你在旅店的大厅里遇到了一些有趣的人——"

    "角落里坐着一群佣兵，看制服像是从南方来的。他们喝着酒，压低声音在谈论什么。"

    "吧台边有个穿着教士袍的年轻人，独自喝着热牛奶，面前摊着一本厚厚的书。"

    "还有一对老夫妇，看起来像是农民，紧张兮兮地抱着一个包袱。"

    menu:
        "去和佣兵搭话，打探消息":
            $ change_stat("intrigue", 5)
            "你端着酒杯走到佣兵们的桌前。"
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "各位，介意我坐下吗？"
            "佣兵头领是个满脸刀疤的大汉，上下打量了你一眼。"
            hide player_char_img with dissolve
            $ hide_all_chars("soldier_generic_img")
            show soldier_generic_img at left with dissolve
            soldier "看你的打扮，是个贵族？坐吧。"
            hide soldier_generic_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我是路过的旅人。听说你们从南方来？"
            hide player_char_img
            $ hide_all_chars("soldier_generic_img")
            show soldier_generic_img at left with dissolve
            soldier "嗯。最近南方的活儿不好接了。王后在整顿军务，好多领主不敢再私下雇佣兵了。"
            soldier "所以我们往北走，看看有没有人需要刀子。"
            "你在心里记下了这个信息。王后在削弱地方领主的武装力量——这和新税法是一套组合拳。"

        "和教士聊天":
            $ change_stat("faith", 8)
            "你走到吧台边，在教士旁边坐下。"
            hide soldier_generic_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "这么晚了还在读书？"
            hide soldier_generic_img
            $ hide_all_chars("servant_generic_img")
            show servant_generic_img at left with dissolve
            scholar "啊，是的。这本是关于王国建国史的。您也感兴趣？"
            hide servant_generic_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "说不上感兴趣，但最近总在想一些关于权力和传承的问题。"
            hide player_char_img
            $ hide_all_chars("servant_generic_img")
            show servant_generic_img at left with dissolve
            scholar "权力与传承……这本书里倒是有一段很有趣的记载。"
            scholar "据说王国第一任国王在登基时，曾与六大家族定下盟约——王室与贵族共治天下。"
            scholar "但这个盟约后来不知为何失传了。如今的王室……似乎早已忘记了这份约定。"
            hide servant_generic_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "有意思。"
            "你记住了这个年轻教士说的话。也许将来会有用。"

        "关心那对老夫妇":
            $ change_stat("loyalty", 3)
            $ change_stat("reputation", 3)
            "你注意到那对老夫妇一直在不安地张望，好像在躲什么人。"
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "两位老人家，可是遇到了什么难事？"
            "老妇人差点被你吓到，老头则护在她前面。"
            hide player_char_img
            $ hide_all_chars("servant_generic_img")
            show servant_generic_img at left with dissolve
            refugee "大……大人，我们没有惹事……"
            hide servant_generic_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "别紧张。我只是看你们神色不安。"
            hide player_char_img
            $ hide_all_chars("servant_generic_img")
            show servant_generic_img at left with dissolve
            refugee "我们……我们是从北边逃来的。我们村子里有人失踪，三个年轻人一夜之间就不见了。"
            refugee "村长说是被山贼抓走了，但我不信……我看到那些人穿的都是黑衣服，不像山贼。"
            "你的心沉了一下。北边……失踪……黑衣人。"
            hide servant_generic_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你们村子在哪里？"
            hide player_char_img
            $ hide_all_chars("servant_generic_img")
            show servant_generic_img at left with dissolve
            refugee "靠近……靠近冯·哈根男爵领地的边界。"
            "又是男爵的方向。你把这件事记在了心里。"

        "早点休息，养精蓄锐":
            $ hide_all_chars()
            "你决定不浪费时间在旅店里闲聊。明天还有一整天的路要走，更重要的是，会议才是真正的战场。"
            "你嘱咐雷恩加强警戒，便回房歇息。"

    "夜深了。旅店的大厅渐渐安静下来，空气中只剩烤肉的余味和一股散不掉的烟气。"

    "你回到楼上的房间，正准备就寝，忽然听到门外传来轻轻的脚步声。"

    $ play_sound("audio/sfx/door_knock.ogg")

    "三声轻叩。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve

    elena "领主大人，是我，艾琳娜。打扰了。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "进来。"

    "艾琳娜推门进来。她已经换了一身便装，长发散落在肩上，和白天那个干练的侍从判若两人。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "我刚才在院子里转了一圈。"

    elena "旅店后面的马厩里，有一匹马不属于店里的任何客人，也不属于我们。"

    elena "那匹马的鞍具上有冯·哈根家族的纹章。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "男爵的人？在这里？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "有可能只是路过的信使。但也有可能……是盯着我们的。"

    menu:
        "让雷恩去查":
            $ change_stat("power", 3)
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我让雷恩派人去查。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "低调一些比较好。不要打草惊蛇。"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你说得对。让人暗中注意就好。"

        "不理会，可能是巧合":
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "也许真是巧合。这条路上来往的人不少。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "希望如此。"
            "但你注意到艾琳娜的眉头并没有舒展。"

        "问艾琳娜是否察觉到其他异常":
            $ change_stat("loyalty", 5)
            $ change_rel("rel_elena", 3)
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "除了这个，你还注意到什么？"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "那几个佣兵……他们说是从南方来找活儿的，但我看到他们中有一个人的腰带上挂着一枚王室的徽章。"
            elena "普通佣兵不会有那种东西。"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你的意思是——他们可能是王后的人？"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "我不确定。但在这个节骨眼上，任何异常都值得注意。"

    elena "领主大人，早点休息吧。明天到了哈伦堡，才是真正的较量。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你也早些睡。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "……晚安，领主大人。"

    "她退出房间时，你注意到她在门口停了一瞬——像是想说什么，最终还是没有开口。"

    hide elena_img with dissolve

    $ hide_all_chars()
    "你躺在床上，盯着天花板上跳动的烛影。"

    "各种念头在脑海里交织缠绕：男爵的野心、王后的算计、父亲的死因……"

    "还有艾琳娜。她到底是王后的眼睛，还是真心想帮你的人？"

    "窗外，风声呜咽，像是某种预兆。"

    "你翻了个身，闭上眼睛。不管明天等待你的是什么，你都必须打起精神面对。"

    "……"

    "但你睡不着。"

    "你披上外衣，走下楼。大厅里已经没有人了，壁炉里的火快要熄灭，只剩最后几块木炭还泛着暗红色的微光。"

    "你推开旅店的后门，走进院子。几个值夜的士兵在篝火旁围坐着，火光在他们疲惫的脸上投下跳动的光影。"

    $ play_music("audio/music/campfire.ogg", fadein=2.0)
    "你走向篝火，在一截枯木上坐下。夜风很冷，但火焰的温度让你的心稍稍安定了些。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve

    "艾琳娜也没有睡。她抱着膝盖坐在篝火的另一边，望着火焰出神。"

    elena "领主大人也睡不着？"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "心里太多事，躺不住。"

    $ hide_all_chars()
    "她往旁边挪了挪，给你让出一个靠近火堆的位置。你走过去坐下。"

    "火堆里的松枝偶尔爆出一声脆响，溅起细碎的火星，在夜空中划出短暂的轨迹后熄灭。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "领主大人，明天到了哈伦堡，会议上最重要的不是说了什么——而是什么时候说。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "此话怎讲？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "领主会议有一个不成文的规矩。新领主第一次参会，所有人都会试探你。"

    elena "男爵会挑衅，子爵会套话，伯爵夫人会冷眼旁观。而格雷伯爵……他会在最关键的时刻问你一个看似无关紧要的问题。"

    elena "你的回答将决定他对你的态度——而他的态度，往往就是整个会议的风向标。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你参加过领主会议？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "没有。但我在王宫里见过太多类似的场面。权谋的底层逻辑是相通的。"

    "她用一根树枝拨了拨火堆。火焰窜高了一些，照亮了她的半张脸。那双紫灰色的眼眸里映着火光，深邃得像两口古井。"

    elena "领主大人，您想过吗——到了会议上，您打算扮演什么角色？"

    "你想了想，这确实是一个需要在抵达之前就想清楚的问题。"

    menu:
        "我要做调停者——让各方都觉得我值得合作":
            $ change_stat("reputation", 8)
            $ change_stat("reputation", 5)
            $ log_decision("第二章", "选择在会议上扮演调停者的角色")
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我不打算站任何人的队。我要让每个人都觉得，和我合作比和我作对更划算。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "调停者……这是最难的一条路。因为你必须比在场的每一个人都更了解局势。"
            elena "但如果做到了——您将成为所有人都不敢轻视的那个人。"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "父亲在这张桌上坐了三十年。如果他能做到，我也能。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "……令尊确实是这方面的高手。不过，他最后还是被人算计了。"
            "这句话像一盆冷水，浇得你一激灵。但她说的是事实。"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "所以我要比他更小心。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "那就记住一件事——在圆桌上，沉默有时候比千言万语更有力量。"

        "我要展示力量——让他们知道艾登堡不可欺":
            $ change_stat("power", 8)
            $ change_stat("loyalty", 5)
            $ log_decision("第二章", "选择在会议上展示力量")
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "他们都觉得我年轻好欺负。我偏要让他们看看，新领主不是软柿子。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "展示力量需要实力做后盾。否则就只是……虚张声势。"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我带的二十个卫兵是真刀真枪上过阵的。我的铁矿是整个北方最好的。这些不够吗？"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "够不够，取决于对手。男爵的私兵比你多五倍。"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "但他没有我的铁矿。没有铁，再多的兵也只是拿着木棍的农民。"
            "艾琳娜看了你一眼，用鼻子笑了一下。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "领主大人倒是想得透彻。那我就放心了。"

        "我要韬光养晦——先观察，后出手":
            $ change_stat("intrigue", 5)
            $ change_stat("reputation", 3)
            $ log_decision("第二章", "选择在会议上韬光养晦")
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "第一次参会，我不了解那些人的底牌。贸然出头是最愚蠢的。"
            player "我打算少说多听，让他们以为我只是个无害的年轻人。等摸清了每个人的路数，再做打算。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "韬光养晦……这需要极大的耐心。有些挑衅，您可能不得不忍下来。"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "忍字头上一把刀。但那把刀不是用来割自己的——是用来等时机割别人的。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "……您不像您的年龄。"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我在王都的学院里学的不只是书本。"
            "篝火映着她的侧脸，她低头沉思了片刻。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "那就祝领主大人心想事成。不过——韬光养晦最怕的不是敌人看穿，而是自己忍不住。"

    $ hide_all_chars()
    "篝火渐渐矮了下去。你往火堆里添了几根干柴，火焰重新跳跃起来。"

    "远处的林子里传来一声狼嚎，悠长而凄厉，像是从远古传来的某种呼唤。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "领主大人，我再告诉您一件事。这是我自己的判断，不代表王后的立场。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "说。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "这次会议，表面上是讨论税法。但真正的博弈不在圆桌上——而是在桌下。"

    elena "每个领主都有不想被别人知道的秘密。谁掌握了这些秘密，谁就掌握了筹码。"

    elena "而在哈伦堡这种地方，秘密像溪水一样流淌。只要你肯弯腰，就能捧起一掬。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你是在教我如何当一个领主。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "我是在帮您活过这次会议。"

    $ hide_all_chars()
    "她的语气突然变得郑重。火光映在她的脸上，你第一次看到了她眼底深处的一丝忧虑。"

    "你想追问，但她已经站起身来。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "夜深了。明天还要早起赶路。领主大人，晚安。"

    $ hide_all_chars()
    "她走了。你独自坐在篝火旁，望着满天繁星，思绪像那些火星一样在黑暗中明灭不定。"

    "风又起了，把篝火吹得忽明忽暗。"

    "你把斗篷裹紧了些，终于起身回到房间。这一次，你倒头便睡着了。"

    hide elena_img with dissolve

    "第二天一早，队伍继续出发。"

    scene bg forest_path with dissolve
    $ unlock_gallery("bg_forest_path")
    $ play_music("audio/music/forest_ambient.ogg", fadein=2.0)

    "过了莱因河之后，地形变得起伏不平。道路穿过一片广袤的橡树林，阳光被层层叠叠的枝干遮挡，只有零星的光斑洒在地面上。"

    "空气中有一股潮湿的腐叶气味，混合着远处不知什么动物的叫声。"

    "林中的道路比官道窄了许多，队伍不得不拉成一条长线。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "领主大人，过了这片林子就是哈伦堡的地界了。再有两个时辰就能到。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "加快速度。我不想在林子里待太久。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "是。"

    hide captain_img with dissolve

    $ hide_all_chars()
    "穿过最后一道山坳，视野骤然开阔——"

    "哈伦堡出现在你的眼前。"

    ## ============================================================
    ## 场景1.75：抵达哈伦堡
    ## ============================================================

    scene bg castle_exterior with dissolve
    $ unlock_gallery("bg_castle_exterior")
    $ play_music("audio/music/harbor_waves.ogg", fadein=2.0)

    "哈伦堡是一座建在两河交汇处的中等城镇。城墙由灰白色的石灰岩砌成，在冬日的阳光下泛着冷冷的光。"

    "城门口插着六面旗帜——代表参加会议的各个领地，以及中立城镇本身。"

    "你看到了自己的家族旗帜——金鹰旗。它被挂在从左数第四面的位置上。不是最显眼的，但也不是最偏的。"

    "城门处的卫兵看到你的队伍，迎了上来。"

    $ hide_all_chars("soldier_generic_img")
    show soldier_generic_img at left with dissolve
    soldier "敢问可是艾登堡的领主大人？请出示信物。"

    "你拿出领主徽章——一只金色的鹰，抓着一柄铁锤——这是艾登堡的纹章。"

    soldier "确认无误。请进。领主大人的住处已经安排妥当。"

    "你的卫兵被安排在城门外的军营驻扎——这是规矩，各领主的私兵不得进城。只允许带五名贴身护卫入城。"

    hide soldier_generic_img with dissolve
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "领主大人，我带四个人跟着您。其余的在城外候命。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "好。保持警戒，随时准备接应。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "遵命。"

    hide captain_img with dissolve

    $ hide_all_chars()
    "你带着艾琳娜和五名护卫走进了哈伦堡的城门。"

    "城内的景象让你有些意外——虽然是中立城镇，但哈伦堡比你想象的更繁华。"

    scene bg market with dissolve
    $ unlock_gallery("bg_market")
    $ play_music("audio/music/market_bustle.ogg", fadein=2.0)

    "石板铺就的主街两旁是一排排商铺，卖着各地的特产。"

    "铁匠铺传来叮叮当当的打铁声，面包房飘出新鲜出炉的麦香，皮革商的摊位上挂满了各种颜色的皮囊和马具。"

    "一群孩子在街上追逐嬉戏，一个老人在墙角晒太阳，一对年轻夫妇在摊位前挑选布料。"

    "如此平常的景象。你站在原地看了很久，脚步怎么也迈不动。这里的人不用操心领地的安危，不用应对男爵的野心，不用揣测王后的意图。"

    "他们只需要过好自己的日子。而你——你必须为艾登堡所有人的日子负责。"

    "街上的人比你预想的多——不仅有本地居民，还有不少外地来的商人和旅客。"

    "你注意到街上有好几家酒馆生意兴隆。领主会议对哈伦堡来说是一年中最赚钱的时候。"

    "政治游戏的背后，总有人在数钱。"

    "显然，领主会议带来了可观的人气和商机。"

    show elena_img at right with dissolve

    elena "领主大人，各领主的住处安排在城中心的贵宾院。我们先去安顿，然后……"

    elena "会议是明天上午。今天下午，各领主通常会在城里走动，互相'偶遇'。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "'偶遇'？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "就是非正式的接触。正式会议上不好说的话，在这种场合更容易开口。"

    elena "如果领主大人想在会前做些功课，今天下午是最好的机会。"

    hide elena_img with dissolve

    $ hide_all_chars()
    "你安顿好行李后，决定趁下午的时间在城里转转。"

    "这既是为了了解哈伦堡的环境，也是为了——如艾琳娜所说——制造一些有价值的'偶遇'。"

    ## ============================================================
    ## 场景1.8：会前交际
    ## ============================================================

    "你换了一身整洁但不过分华丽的衣服，带着艾琳娜走进了哈伦堡的街道。"

    "走过集市的时候，你注意到一个摆着古董和书籍的摊位前，站着一位衣着考究的中年男人。"

    "他正专注地翻看一本泛黄的古籍，身边站着两个随从。"

    show elena_img at right with dissolve

    elena "（低声）那是格雷伯爵。学识渊博，嗜书如命。他在领主中德高望重，但从不站队。"

    elena "如果能在会前和他搭上话，明天会议上可能会有意想不到的好处。"

    hide elena_img with dissolve

    menu:
        "主动上前与格雷伯爵攀谈":
            $ grey_met = True
            $ change_stat("reputation", 5)
            $ change_stat("loyalty", 3)
            "你走向书摊，假装浏览旁边的书架。"
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "这部《王国律令汇编》倒是难得一见。版本很老了。"
            "格雷伯爵抬起头，带着几分惊讶地看着你。"
            hide player_char_img
            $ hide_all_chars("count_grey_img")
            show count_grey_img at left with dissolve
            count_grey "哦？年轻人也识得这部典籍？"
            hide count_grey_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "家父的书房里有一部残本。可惜缺了第三卷。"
            hide player_char_img
            $ hide_all_chars("count_grey_img")
            show count_grey_img at left with dissolve
            count_grey "你父亲……你是艾登堡的新领主？"
            hide count_grey_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "正是。格雷伯爵大人。"
            hide player_char_img
            $ hide_all_chars("count_grey_img")
            show count_grey_img at left with dissolve
            count_grey "嗯……令尊是个博学的人。可惜天不假年。"

            count_grey "说起来——你大概不记得了。十几年前你还很小，老夫曾带犬子费利克斯去艾登堡拜访令尊。那孩子……让你受了委屈。"

            count_grey "那次回来后，老夫狠狠教训过他。但教育这种事——有些孩子吃这一套，有些孩子不吃。"

            "格雷伯爵叹了口气，目光转向远处。"

            count_grey "如今他四十了，还是个不成器的废物。我让他在封地里管马场——也只配管马场。"

            count_grey "你倒是站到这里来了。"

            "老人的语气里有一种复杂的情绪——既是替自己儿子惋惜，也是一种长辈对你的认可。"

            count_grey "年轻人，明天的会议上，老夫有一个忠告给你——"
            count_grey "少说话，多听。第一次参加会议的领主，最容易犯的错就是急于表态。"
            hide count_grey_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "多谢伯爵指点。"
            hide player_char_img
            $ hide_all_chars("count_grey_img")
            show count_grey_img at left with dissolve
            count_grey "不是指点，是老人家的唠叨。哈哈。"
            "格雷伯爵拍拍你的肩膀，拿着买好的书离开了。简短的交流，但你感觉这位老领主对你的印象不错。"

        "暂时不去，先看看其他人":
            $ hide_all_chars()
            "你决定先观察一下其他领主的动向，等更好的时机再与格雷伯爵接触。"

    "继续往前走，你来到了一家高级酒馆——'银杯酒馆'。门口停着几辆华丽的马车。"

    "酒馆二楼的露台上，一个身材魁梧的中年人正大声说笑，身边围着几个随从。"

    show elena_img at right with dissolve

    elena "（低声）那是威尔斯子爵。男爵的姻亲，但为人圆滑，谁的钱多就跟谁走。"

    elena "他最近在做葡萄酒生意，赚了不少钱，但也因此和南方的几个领地起了纠纷。"

    hide elena_img with dissolve

    menu:
        "上去打个招呼":
            $ change_stat("reputation", 3)
            "你走上酒馆二楼，向子爵致意。"
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            if wells_met:
                player "子爵大人，又见面了。"
            else:
                player "威尔斯子爵大人，久仰大名。"
            "子爵上下打量了你一下，脸上挂起了商人式的笑容。"
            hide player_char_img
            $ hide_all_chars("viscount_wells_img")
            show viscount_wells_img at left with dissolve
            if wells_met:
                viscount_wells "哟，小艾登堡领主！没想到这么快就又见面了。"
                viscount_wells "令尊那股倔脾气你没少学吧？每次开会都要和男爵吵个天翻地覆。"
            else:
                viscount_wells "哈！你就是老艾登堡领主的儿子？"
                viscount_wells "令尊可是个倔脾气的人——每次开会都要和男爵吵个天翻地覆。"
            viscount_wells "你呢？你是站你爹的队，还是打算走自己的路？"
            hide viscount_wells_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我来会议是为了所有人的利益，不是为了站谁的队。"
            hide player_char_img
            $ hide_all_chars("viscount_wells_img")
            show viscount_wells_img at left with dissolve
            viscount_wells "哈哈哈，说得好！来，喝一杯！这是我领地出产的红酒，王都里都卖疯了！"
            "你陪他喝了一杯。酒确实不错。但你也注意到，这个人的眼睛一直在打量你身上的配饰，评估你的身价。"
            $ wells_met = True

        "不去，继续逛":
            $ hide_all_chars()
            "你决定不在这个时候接近子爵。他和男爵的关系太近了，现在接触可能被误解。"

    "你转过一个街角，忽然看到了一个意想不到的人。"

    "在一条僻静的巷子里，一个身穿黑色长袍的女人正从一扇侧门走出来。她身边跟着两个沉默的卫兵。"

    show elena_img at right with dissolve

    elena "（低声，几乎是气声）领主大人，那是施泰因伯爵夫人。"

    elena "她刚从城中的商会出来……很奇怪，那个商会据说只接待特定的客户。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "什么样的客户？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "有钱的、有权的，或者……有秘密的。"

    hide elena_img with dissolve

    $ hide_all_chars()
    "你犹豫了一下，伯爵夫人已经注意到了你。"

    "她停下脚步，目光锐利地看向你。"

    $ hide_all_chars("countess_stein_img")
    show countess_stein_img at left with dissolve

    countess_stein "你就是艾登堡的新领主？"

    $ steinfurt_met = True

    hide countess_stein_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "正是。伯爵夫人大人。"

    hide player_char_img
    $ hide_all_chars("countess_stein_img")
    show countess_stein_img at left with dissolve
    countess_stein "嗯。我见过你父亲几次。他是个好人——这在贵族里很少见。"

    countess_stein "希望你也是。这个世道，好人活得不容易。"

    hide countess_stein_img with dissolve

    $ hide_all_chars()
    "她没有多说什么，带着卫兵转身离开。短短几句话，却让你感受到了一种沉稳的力量。"

    "你注意到她走路时微微跛着一条腿——也许是旧伤。一个在丈夫死后独自撑起领地的女人，背后一定有不为人知的故事。"

    "……"

    "你继续往前走。在一个小广场上，你看到了一群人围成半圆，中间传来一个苍老而浑厚的声音。"

    "挤过人群，你看到一个白发苍苍的老人坐在一块磨平的石墩上。他穿着打了补丁的灰袍，但腰板挺得很直，眼神里有一种历经沧桑后的清明。"

    "他手里拿着一把旧琴，随口拨弄着，一边讲着故事。"

    $ hide_all_chars("storyteller_img")
    show storyteller_img at left with dissolve
    storyteller "……从前，有一座花园。花园里长着一朵最美的百合花。"

    storyteller "所有人都说，那朵百合花是花园里最纯洁、最高贵的——白如初雪，香飘十里。"

    storyteller "于是国王想摘下它，戴在王冠上。"

    storyteller "但百合花说：'我只在泥土里才能活。你把我摘下来，我就会枯萎。'"

    storyteller "国王不听。他摘下了百合花，戴在了头上。"

    storyteller "三天之后——百合花枯了。"

    storyteller "但奇怪的是，国王也开始枯萎。他的头发变白了，皮肤干裂了，力量一天天流失。"

    "老人停顿了一下，扫视着围观的人群，目光在你脸上短暂地停留了一瞬。"

    storyteller "国王这才明白——百合花不是花园的装饰，而是花园的根。没有了根，花园就会死去。"

    storyteller "可是已经晚了。百合花碎成了粉末，从王冠的缝隙里飘散，落在了花园的每一个角落。"

    storyteller "从那以后，花园里长出了无数朵百合花。它们不再是一朵，而是千千万万朵。"

    storyteller "国王再也无法摘尽它们了。"

    $ hide_all_chars()
    "人群中有人鼓掌，有人往老人面前的碗里扔铜板。但你站在原地，心中泛起了一种说不清的不安。"

    "百合花……暗百合？这只是巧合吗？"

    show elena_img at right with dissolve

    "你注意到艾琳娜的表情也变得微妙。她的目光追随着那个老人，眉心轻轻拧了一下。"

    elena "（低声）有趣的寓言。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "（低声）你觉得他在暗示什么？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "（低声）也许什么都没暗示。街头说书人讲的故事，大多是祖祖辈辈传下来的老段子。"

    elena "（低声）但这个版本……我从没听过。"

    hide elena_img with dissolve

    menu:
        "去和说书人攀谈，打探故事的来源":
            $ change_stat("intrigue", 8)
            "你等人群散去后，走到老人面前。"
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "老先生，你的故事很有意思。百合花和国王——这是哪里的传说？"
            "老人抬起头，看着你。他的眼睛浑浊，但目光深邃得像一口没有底的井。"
            hide player_char_img
            $ hide_all_chars("storyteller_img")
            show storyteller_img at left with dissolve
            storyteller "年轻人，好故事不问出处。问的人太多了，故事就变了味。"
            hide storyteller_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "那我换个问法——这个故事想说的是什么？"
            hide player_char_img
            $ hide_all_chars("storyteller_img")
            show storyteller_img at left with dissolve
            storyteller "说的是权力。"
            "老人的声音突然变得很轻，像是在自言自语。"
            storyteller "权力就像那朵百合花。你想拥有它，就必须让它长在泥土里。拔起来戴在头上——你和它一起死。"
            storyteller "真正聪明的人不会去摘花。他会去做花园的泥土。"
            "这个看似普通的老人，说出的话却字字扎心。"
            hide storyteller_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "多谢指教。"
            hide player_char_img
            $ hide_all_chars("storyteller_img")
            show storyteller_img at left with dissolve
            storyteller "不敢当。老朽只是个讲故事的人。"
            "他笑了笑，拾起碗里的铜板，背着琴慢慢离开。碗底还留着一枚他没拿走的铜板——你弯腰捡起来，发现铜板的背面刻着一个你从未见过的符号。这个人远不像表面上那么简单。"
            $ log_decision("第二章", "与说书人交谈，听到关于权力的寓言")

        "记在心里，但不去接触——也许有人在看着":
            $ change_stat("intrigue", 5)
            $ hide_all_chars()
            "你没有上前。在一个各路势力汇聚的城镇里，一个讲百合花故事的说书人——"
            "也许只是巧合，也许是试探。无论如何，主动接触都可能暴露你对'百合花'这个符号的在意。"
            "你假装不经意地从老人身边走过，余光却把他的面容牢牢记住——花白的头发，左颊一道陈年刀疤，右手小指缺了半截。"
            "如果将来需要找到这个人，你认得出他。"

        "先回去再说——身边人多眼杂，不宜在此攀谈":
            $ change_stat("reputation", 5)
            "你不动声色地扫了一眼四周。说书人身边围着几十号人，而你的侍卫就站在三步之外。"
            "这些侍卫里有多少是真正忠于你的？有多少是别人安插的眼线？你无法确定。"
            "在这种环境下和一个讲'百合花'寓言的老头攀谈——等于向所有人宣告你对暗百合感兴趣。"
            "你把老人的面容牢牢记住——花白的头发，左颊一道陈年刀疤，右手小指缺了半截。"
            "然后，你若无其事地转身离开了。"

            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "（低声）艾琳娜，记住那个说书人的长相。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "（低声）您是想……"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "（低声）回城堡后，用密室说话。这里耳目太多了。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "（低声）明白。"
            hide elena_img with dissolve

            "回到贵宾院后，你让艾琳娜遣散了所有侍从，在内室关上了门。"
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "那个说书人讲的百合花寓言，你也听到了。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "百合花——暗百合。不可能是巧合。"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "所以他要么是暗百合的人在试探，要么是知情者在借故事传话。无论哪种，此人都有价值。"
            player "但我不能亲自去接触他。万一身边有间谍，我一去就等于暴露了态度。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "您想让我派人去？"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "不。你亲自去。换一身装扮，夜里去找他。告诉他——花园的泥土想见见种花的人。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "……好。如果他真的是那边的人，他会懂这句话。"
            "你满意地点了点头。谨慎不是懦弱——在这个人人都可能是棋子的局面里，每一步都要走得滴水不漏。"
            $ log_decision("第二章", "谨慎行事，回城堡后秘密派艾琳娜联络说书人")

        "不以为意——只是一个老头在讨钱罢了":
            $ hide_all_chars()
            "你转身继续往前走。一个街头说书人的寓言，没必要过度解读。"
            "但不知为何，那个故事在你脑海中挥之不去。百合花碎成粉末，落在花园的每一个角落——"
            "千千万万朵。"
            "你摇了摇头，把这个念头驱散了。"

    "逛了一下午，你回到贵宾院。"

    "天色渐暗，仆人在房间里点起了蜡烛。晚餐是烤鹿肉和黑面包，味道远不如家里的好。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve

    elena "领主大人，我打听到了一些消息。"

    elena "男爵今天下午和威尔斯子爵在酒馆密谈了很久。看来他在会前就开始拉票了。"

    elena "另外，施泰因伯爵夫人去过的那个商会……据说和一个叫'北方商盟'的组织有关。"

    elena "这个商盟近年来势力扩张很快，甚至开始插手领主之间的事务。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "政治和金钱，永远纠缠在一起。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "正是如此。"

    elena "还有一件事。我在城里看到了一些奇怪的人——穿着灰色斗篷，行踪隐秘。他们好像在监视各领主的住处。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "灰色斗篷……王后的人？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "也许。也许不是。"

    "她的回答很含糊。你看了她一眼，没有追问。"

    elena "领主大人，今晚早些休息吧。明天的会议，才是最关键的战场。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你说得对。明天……就看我们的了。"

    hide elena_img with dissolve

    $ hide_all_chars()
    "你坐在窗前，望着哈伦堡的夜景。零星的灯火在黑暗中闪烁，像是棋盘上散落的棋子。"

    "明天，你将第一次坐上那张圆桌。"

    "父亲曾经坐过的位置，如今等待着你。"

    "你吹灭了蜡烛。"

    ## 扩展剧情：宴会交锋 / 棋局博弈 / 联盟试探
    call ch2_exp_banquet from _call_ch2_exp_banquet

    ## ============================================================
    ## 场景2：领主会议
    ## ============================================================

label ch2_council:

    $ set_mood("tense")
    $ clear_weather()
    $ play_music("audio/music/great_hall.ogg", fadein=2.0)
    scene bg council_hall with dissolve
    $ unlock_gallery("bg_council_hall")

    "领主会议在中立城镇哈伦堡的议事厅举行。"

    "这座议事厅建于百年之前，穹顶高耸，四面墙上悬挂着各领地的家徽。"

    "正中央是一张巨大的圆形石桌，据说是用整块花岗岩凿成的。桌面上刻着王国的版图，每位领主的席位正对着自己的领地方位。"

    "厅内的光线来自高处的彩色玻璃窗。冬日的阳光透过玻璃，在石桌上投下斑驳的色彩——红色、蓝色、金色，交错在一起，像是命运的丝线。"

    "你深吸一口气，推开了议事厅那扇沉重的橡木大门。门轴发出低沉的吱呀声，像是古老的叹息。"

    "厅内的空气凝重而肃穆，混合着蜡烛的燃烧味和石头墙壁特有的潮湿气息。"

    "你走进议事厅的时候，大多数人已经到了。"

    "你注意到每位领主身后都站着一到两名随从或谋士——这些人虽然没有资格坐在桌旁，但他们的耳语往往能左右主人的决定。"

    "艾琳娜站在你身后，靠着墙壁。她的目光在厅内快速扫过，像是在评估每一个人的位置和状态。"

    "圆形石桌旁，五位领主各怀心事。"

    $ grey_met = True
    "格雷伯爵坐在北面的席位上，面前放着一杯清水和几份文书，面容沉静如古井。"

    $ wells_met = True
    "威尔斯子爵坐在南面，身上的锦缎在灯光下闪闪发亮。他正和身边的随从嘀咕什么，时不时发出一阵低笑。"

    $ steinfurt_met = True
    "施泰因伯爵夫人坐在西面，身着黑色丧服，但腰间佩着一把精致的短刀——在正式场合佩刀，这是一种无声的宣示。"

    "你的位置在东面。椅背上雕刻着你家族的纹章——金鹰和铁锤。父亲的手曾无数次抚过这些雕纹。"

    "你走过去，在石椅上坐下。椅子冰凉，像是在提醒你：权力的宝座从来不会给人温暖。"

    "但你的脊背挺得笔直。"

    "你注意到冯·哈根男爵的目光一直盯着你。"

    $ hide_all_chars("baron_img")
    show baron_img at left with dissolve
    $ unlock_gallery("baron")

    baron "哦，艾登堡的新领主。久仰大名。"

    baron "令尊在世时，可是这张桌上的常客。不知年轻的领主……能否撑起这把椅子？"

    $ hide_all_chars()
    "议事厅内一片寂静。所有人都在看你。"

    "议事厅里安静得能听见墙上挂毯被穿堂风吹动的声音。所有人都在等你的回答。"

    menu:
        "从容回应——『家父教导我，椅子的重量不在于谁坐，而在于谁站得住。』":
            $ change_stat("reputation", 15)
            $ change_rel("rel_baron", 5)
            $ log_decision("第二章", "在会议上沉着应对男爵的挑衅")
            hide baron_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "家父教导我，椅子的重量不在于谁坐，而在于谁站得住。"
            hide player_char_img
            $ hide_all_chars("baron_img")
            show baron_img at left with dissolve
            baron "……哼，倒是有几分令尊的风骨。"
            $ hide_all_chars()
            "其他领主交换了赞许的目光。格雷伯爵微不可察地点了点头。"
            "施泰因伯爵夫人的嘴角则浮起了一抹淡淡的笑意。"

        "针锋相对——『男爵大人上次带了两百人来给家父吊唁，这份厚礼我还没来得及回报。』":
            $ change_stat("power", 10)
            $ change_rel("rel_baron", -15)
            $ log_decision("第二章", "强硬反击男爵的挑衅")
            hide baron_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "男爵大人上次带了两百人来给家父吊唁，这份厚礼我还没来得及回报。"
            "议事厅内倒吸一口凉气。男爵的脸色变得铁青。"
            hide player_char_img
            $ hide_all_chars("baron_img")
            show baron_img at left with dissolve
            baron "你——！"
            "格雷伯爵轻轻咳了一声，出面打圆场。"
            hide baron_img
            $ hide_all_chars("count_grey_img")
            show count_grey_img at left with dissolve
            count_grey "年轻人有锐气是好事。但这里是议事厅，不是校场。各位，我们开始正事吧。"
            "气氛才勉强缓和下来。但你看到施泰因伯爵夫人投来了一个意味深长的目光——她似乎对你的胆识有几分欣赏。"

        "谦虚低调——『晚辈初来乍到，还请各位前辈多多指教。』":
            $ change_stat("reputation", 5)
            $ change_stat("loyalty", 5)
            $ log_decision("第二章", "谦逊回应男爵的挑衅")
            hide count_grey_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "晚辈初来乍到，还请各位前辈多多指教。"
            hide player_char_img
            $ hide_all_chars("baron_img")
            show baron_img at left with dissolve
            baron "呵……至少比令尊知道什么叫礼貌。"
            $ hide_all_chars()
            "你不动声色，但心里记下了这句话。"
            "格雷伯爵看了你一眼，目光中有几分赞赏——他似乎认出了你故意示弱的策略。"

    hide baron_img with dissolve

    "一位穿着哈伦堡议事官制服的老人站起来，清了清嗓子。"

    $ hide_all_chars("herald_img")
    show herald_img at left with dissolve
    herald "诸位领主大人，本次会议正式开始。"

    herald "按照惯例，先由各领地汇报近况，然后讨论公共事务。"

    $ hide_all_chars()
    "各领主依次汇报。你注意到了几个关键信息——"

    "男爵的领地今年扩建了两座哨塔，军费开支大增。但他的语气暗示，这些钱不是他自己出的。"

    "威尔斯子爵大谈葡萄酒贸易的利润，但对领地内的盗匪问题避而不提。"

    "施泰因伯爵夫人言简意赅地报告了旱灾后的恢复情况，措辞严谨，没有夸大也没有隐瞒。"

    "格雷伯爵用平淡的语气说了几句，大意是一切如常。但你注意到他说到'教会事务'时，眉头微微皱了一下。"

    "轮到你了。"

    menu:
        "如实汇报艾登堡的情况，包括困难":
            $ change_stat("reputation", 5)
            $ change_stat("loyalty", 3)
            hide herald_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "艾登堡目前面临几个挑战——粮食储备不足、北方边境的安全隐患、以及税收下降。"
            player "但我们已经采取了措施。我有信心在入春前扭转局面。"
            $ hide_all_chars()
            "你的坦诚赢得了几位领主的好感。格雷伯爵点了点头，施泰因伯爵夫人也投来了一个赞许的目光。"
            "但男爵的嘴角露出了一丝冷笑——他大概把你的困难当成了可以利用的弱点。"

        "报喜不报忧，展现实力":
            $ change_stat("power", 3)
            $ change_stat("reputation", 3)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "艾登堡一切安好。卫队已经扩编，商路畅通，百姓安居乐业。"
            $ hide_all_chars()
            "你说的并非全是事实，但在这张桌上，示弱等于送命。"
            "男爵狐疑地看着你，显然不太相信。但他没有证据反驳。"

        "避重就轻，转移话题":
            $ change_stat("intrigue", 5)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "艾登堡的情况各位都清楚，不必多说。我更关心的是——各位对最近频繁出现的盗匪问题有什么看法？"
            $ hide_all_chars()
            "你巧妙地把话题引向了公共安全，避免了暴露自己的弱点。"
            "几位领主开始讨论盗匪问题，男爵的脸色变得有些不自然——也许是因为有传言说那些盗匪和他有关。"

    "公共事务讨论开始。"

    "先是一些例行公事——商路维护的费用分摊、边境巡逻的协调安排、以及对两起领地纠纷的仲裁。"

    "格雷伯爵在纠纷仲裁时展现了惊人的法律素养。他引经据典，不偏不倚，让双方都无话可说。"

    "你默默观察着每个人的反应。威尔斯子爵在无聊地转着手中的酒杯；男爵则不耐烦地敲着桌面，显然在等真正的重头戏。"

    "施泰因伯爵夫人全程沉默，但她的目光在每个人脸上逡巡，像是一只猎鹰在审视猎物。"

    "例行议程结束后，议事官清了清嗓子，拿出了一份新的文书。"

    "你注意到他的手在微微发抖——显然，他也知道接下来要宣布的内容会在这间屋子里掀起风暴。"

    "讨论进入了核心议题——"

    "正式议程开始。第一个议题就是王后推行的新税法——"

    "要求所有领地将税收的三成上缴王室，比原来多了整整一成。"

    "议事官把卷轴递到王后特使手里。一位身着紫色袍服的中年男子上前一步，展开卷轴，高声宣读。"

    hide player_char_img
    $ hide_all_chars("queen_envoy_img")
    show queen_envoy_img at left with dissolve
    queen_envoy "王后陛下谕令：鉴于王国边防军费日增，北方蛮族频频犯境，王室决定调整各领地税赋比例，由原来的两成提高至三成。"

    queen_envoy "此令即日起执行，各领地须在春耕前完成首批税银的解缴。"

    $ hide_all_chars()
    "宣读完毕，议事厅里安静了片刻。然后——"

    "像是一颗石子投入平静的水面，涟漪迅速扩散。"

    show elena_img at right with dissolve

    elena "（低声）这就是我说的。王后想用税法收紧对地方的控制。"

    elena "（低声）注意男爵的反应。他一定会第一个跳出来。"

    hide elena_img with dissolve

    $ hide_all_chars()
    "果然——"

    "领主们议论纷纷。这时，男爵站了起来。"

    "他的椅子在石板地面上发出刺耳的摩擦声，整个议事厅都安静了下来。"

    $ hide_all_chars("baron_img")
    show baron_img angry at left with dissolve

    baron "各位，王后的新税法分明是在压榨我们。我提议，联名上书反对！"

    baron "三成税赋！我的领民辛苦一年，到头来三成都要交给王都那些不事生产的人？"

    baron "我的士兵在北方替王室挡蛮族，王室不但不感恩，反而还要多收我们的钱？"

    "他环视一圈，最后把目光落在你身上。"

    baron "年轻的艾登堡领主，你怎么看？你父亲可是最反对加税的。"

    hide baron_img with dissolve

    $ hide_all_chars()
    "所有人的目光都转向了你。"

    "你能感受到几道不同的视线——男爵期待你站在他那边；格雷伯爵在冷静地观察你；威尔斯子爵在等着看风向再做决定。"

    "施泰因伯爵夫人则低头看着自己手中的短刀，似乎对你的回答并不感兴趣——但你知道，她在仔细地听。"

    show elena_img at right with dissolve

    elena "（低声）三个选择，三条路。反对男爵会记你的好，但你就上了王后的黑名单。"

    elena "（低声）支持王后，男爵会视你为叛徒。折中方案风险最小，但也最考验你的口才。"

    hide elena_img with dissolve

    "这是一个关键时刻。你的表态将决定你在贵族圈中的立场。"

    menu:
        "支持男爵，反对新税法":
            jump ch2_oppose_tax

        "支持王后的新税法":
            jump ch2_support_tax

        "提出折中方案":
            jump ch2_compromise_tax

label ch2_oppose_tax:
    $ log_decision("第二章", "在税法问题上反对王后")
    $ change_rel("rel_baron", 20)
    $ change_rel("rel_queen", -20)
    $ change_stat("reputation", 10)
    $ change_stat("power", 5)

    "你站起身来。在这张圆桌上，坐着说话和站着说话，分量是不同的。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "男爵说得对。新税法加重了百姓负担，我支持联名上书。"

    player "我父亲生前就反对过类似的提案。他说过一句话——'税赋不是鞭子，不能用来驯服领民。'"

    "你的声音在议事厅里回荡。你看到格雷伯爵的眼中闪过一丝光——那句话，也许正是你父亲在这张桌上说过的。"

    hide player_char_img with dissolve
    show baron_img happy at left with dissolve
    baron "好！果然是老领主的儿子！"

    $ hide_all_chars()
    "男爵走到你面前，伸出手。他的手掌粗糙有力，像是常年握剑的人。"

    "你握住了它。"

    $ hide_all_chars("baron_img")
    show baron_img at left with dissolve
    baron "从今天起，你就是我冯·哈根的朋友。有人敢动你，先过我这关。"

    $ alliance_baron = True

    $ hide_all_chars()
    "威尔斯子爵见风使舵，也表示赞同。施泰因伯爵夫人没有表态，但也没有反对。"

    "格雷伯爵缓缓开口。"

    show count_grey_img at right with dissolve

    count_grey "既然多数领主反对，那就依惯例联名上书吧。但老夫希望用词温和一些——毕竟，我们不是在宣战。"

    "联名信很快拟好。五位领主——不，四位签了字。施泰因伯爵夫人沉默良久，最终也按下了自己的印章。"

    hide count_grey_img with dissolve
    hide baron_img with dissolve

    show elena_img sad at right with dissolve
    elena "（低声）领主大人……你确定要与王后为敌吗？"
    "你注意到艾琳娜的表情变得复杂。她的眼中有担忧，也有……别的什么。"

    elena "（低声）联名信送到王都的那天，你的名字就会出现在王后的案头。"

    elena "（低声）她不会忘记的。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "（低声）有些事，不能因为害怕就不去做。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "（低声）……我明白了。"

    "她低下头，不再说话。但你注意到她的手在袖中微微颤抖。"

    hide elena_img with dissolve

    $ council_outcome = "反对"

    jump ch2_after_council

label ch2_support_tax:
    $ log_decision("第二章", "在税法问题上支持王后")
    $ change_rel("rel_queen", 20)
    $ change_rel("rel_baron", -25)
    $ change_stat("faith", 12)

    "你没有站起来。在男爵怒火中烧的时候，保持坐姿反而显得更有分量。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "新税法虽然增加了负担，但王室需要资金来维护和平。我支持。"

    player "各位，北方的蛮族不会因为我们少交了税就不来犯境。"

    player "与其在这里争论一成税赋，不如想想——如果王室的军队因为缺饷而无法驻守北疆，我们自己得花多少钱来抵御蛮族？"

    "你的话让几位领主陷入了沉思。但男爵不是会沉思的人。"

    hide player_char_img with dissolve
    show baron_img angry at left with dissolve
    baron "你……！枉我还以为你有你父亲的骨气！"
    "男爵怒目而视，一拳砸在桌上。石桌上的水杯都跳了一下。"

    baron "你父亲在这张桌上为领民据理力争的时候，你还在王都吃奶！你有什么资格替他改变立场？"

    hide baron_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "正因为我从王都来，我看到了你们看不到的东西。"

    player "王室的困难是真实的。如果我们逼得太紧，王后可能会采取更极端的措施——比如直接收回领地。"

    $ hide_all_chars()
    "议事厅再次陷入沉默。你说的不是危言耸听——历史上，王室确实这么干过。"

    "格雷伯爵捋着胡须，若有所思。威尔斯子爵的眼珠子转了转，显然在重新评估形势。"

    "最终，反对的联名信没有凑齐足够的签名。男爵怒气冲冲地坐下，从此不再看你一眼。"

    hide baron_img with dissolve

    show elena_img happy at right with dissolve
    elena "（微笑）领主大人的选择很明智。王后会记住您的忠诚。"
    $ change_rel("rel_elena", 10)

    elena "（低声）不过……请注意今晚的安全。男爵的脾气不好，您公然反对他，他可能会做出不理智的事。"

    hide elena_img with dissolve

    $ council_outcome = "支持"

    jump ch2_after_council

label ch2_compromise_tax:
    $ log_decision("第二章", "在税法问题上提出折中方案")
    $ change_stat("reputation", 15)
    $ change_stat("wealth", 5)
    $ change_rel("rel_baron", 5)
    $ change_rel("rel_queen", 5)

    "你没有急着站起来，也没有保持沉默。你先环顾了一圈，等所有人的目光都集中在你身上时，才缓缓开口。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "诸位，我有一个提议。与其争论税率，不如讨论税收的用途。"

    "你注意到格雷伯爵微微坐直了身体——他对你的话产生了兴趣。"

    player "如果王室承诺将新增税收用于修建商路和剿灭盗匪，我们不是都能受益吗？"

    player "商路通畅了，各领地的贸易收入自然会增加。到时候，多缴的那一成税赋，不过是九牛一毛。"

    $ hide_all_chars()
    "议事厅安静了一瞬。然后，几位领主开始点头。"

    "施泰因伯爵夫人第一次开口说话。"

    $ hide_all_chars("countess_stein_img")
    show countess_stein_img at left with dissolve

    countess_stein "这个提议有道理。我的领地遭了旱灾，如果王室能用税款来修复灌溉渠，我可以接受新税法。"

    hide countess_stein_img with dissolve

    "你借势继续。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "伯爵夫人说得好。每个领地的需求不同，如果税款能定向使用在各领地最需要的地方——这就不是在收税，而是在投资。"

    hide player_char_img with dissolve
    $ hide_all_chars("baron_img")
    show baron_img at left with dissolve
    baron "唔……倒是有几分道理。但谁来监督王室？说好的修路，转头拿去养王宫的闲人怎么办？"

    hide baron_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我们可以成立一个领主监督委员会。"

    player "每年由委员会审核税款的使用情况。如果王室违约，下一年的税赋自动恢复原来的比例。"

    $ hide_all_chars()
    "这番话让在场的每一位领主都开始认真考虑。"

    "格雷伯爵终于开口了。"

    show count_grey_img at right with dissolve

    count_grey "年轻人的提议确实可行。关键在于——王后是否会接受监督委员会的存在。"

    hide count_grey_img
    hide player_char_img with dissolve
    $ hide_all_chars("baron_img")
    show baron_img at left with dissolve
    baron "……好。如果你能说服王后接受这个条件，我可以考虑。"

    "男爵的语气勉强，但你看得出来，他对你的印象改变了——说不上好感，更像是一种不情不愿的尊重。"

    hide count_grey_img with dissolve
    hide baron_img with dissolve

    $ hide_all_chars()
    "会议在一种意外和谐的气氛中结束。没有人完全满意，但也没有人觉得吃了大亏。"

    "这就是折中方案的魅力——让每个人都觉得自己赢了一点。"

    show elena_img happy at right with dissolve

    elena "领主大人……您今天的表现让我刮目相看。"

    elena "这个方案如果真的能推行，对所有人都好。包括王后。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "关键是能不能推行。王后未必愿意接受监督。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "……我会把今天的讨论详细报告给王后。相信我，她比你想象的更开明。"

    "你注意到艾琳娜说这话时，语气里带着一种微妙的骄傲——像是在为王后辩护，又像是在向你保证什么。"

    hide elena_img with dissolve

    $ council_outcome = "折中"
    $ unlock_achievement("council_master")

    jump ch2_after_council

    ## ============================================================
    ## 场景3：会后的市集与商人卡尔
    ## ============================================================

label ch2_after_council:

    $ play_music("audio/music/market_bustle.ogg", fadein=2.0)
    scene bg market with dissolve
    $ unlock_gallery("bg_market")

    $ trigger_random_event("explore")

    "会议结束后，议事厅外的气氛骤然松弛下来。"

    "各领主的随从们三三两两地聚在一起，互相打探消息。领主们则各自散去，或回住处休息，或在城里闲逛。"

    "你决定在哈伦堡的集市上散步。一来是为了透透气——议事厅里的紧张让你的肩膀酸痛不已。"

    "二来，你想看看这座中立城镇的商业环境。也许将来可以利用。"

    "集市比你昨天看到的更加热闹。会议期间，各领地的商人都赶来做生意，摊位一直摆到了城门口。"

    "你路过一个卖草药的摊位，一个卖铁器的摊位，一个卖布匹的摊位——"

    if deep_marcus_confession == "forgive":

        "人群突然拥挤起来。你身边一个生意人被推搡着往你这边倒。"

        "一只手从侧面伸出，稳稳地接住了那个人。"

        $ hide_all_chars("friend_marcus_img")
        show friend_marcus_img at left with dissolve

        friend_marcus "抓稳。"

        $ hide_all_chars()
        "马库斯站在你身边，穿着旅人的深色斗篷。他没有看你，只是看着被他扶住的生意人点了点头。"

        "——然后他借着扶人那一瞬，低声说了一句只有你才听得到的话——"

        $ hide_all_chars("friend_marcus_img")
        show friend_marcus_img at left with dissolve
        friend_marcus "你右后方那个戴皮帽的，跟了你两个街口。北方口音，不是商人。"

        friend_marcus "今天我先解决他。下次见面之前——保重。"

        $ hide_all_chars()
        "下一秒，他消失在人群里。"

        "半个时辰后，你听到酒馆方向有短暂的骚动。事后没人提起，集市又恢复了平常的喧嚣。"

        "你只知道——那个戴皮帽的，你再没见过。"

        if deep_marcus_truly_loyal:
            "原来他从昨夜起就一直跟在暗处。你给过他一次原谅，他还你一辈子的看护。"

    "然后，一个穿着旅行斗篷的中年人拦住了你。"

    "他从人群中走出来，动作从容，仿佛在这里等你已久。"

    $ hide_all_chars("merchant_karl_img")
    show merchant_karl_img at left with dissolve
    $ unlock_gallery("merchant_karl")

    if karl_past_done:
        merchant "领主大人，又见面了。"
        "依旧是那身朴素的旅行装束。但暮色集市上他独自摩挲那枚温特菲尔德徽章的样子，已经印在你脑里——眼前这个商人不是萍水相逢的行脚客，而是一个把过去藏得很深的人。"
    elif karl_met:
        merchant "领主大人，又见面了。集市上那桩纠纷，多谢您公正裁决——让我卡尔对您印象深刻。"
        "他微微欠身。你还记得那天在艾登堡村庄市场的他——一袭简朴的旅行装束。这次你注意到更多细节：他靴子上的银扣和手指上那枚不起眼却价值不菲的碧玺戒指，确认了你当日的判断——这不是一个普通的行商。"
    else:
        merchant "领主大人，鄙人卡尔，行走四方的商人。"
        "他微微欠身。虽然穿着朴素，但你注意到他靴子上的银扣和手指上那枚不起眼却价值不菲的碧玺戒指——这不是一个普通的行商。"

    $ karl_met = True

    merchant "久闻艾登堡铁矿出产的精铁品质上乘，不知领主大人是否有兴趣谈一笔买卖？"

    hide merchant_karl_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "什么买卖？"

    hide player_char_img
    $ hide_all_chars("merchant_karl_img")
    show merchant_karl_img at left with dissolve
    merchant "我有一条从南方港口到北方要塞的商路。如果艾登堡的精铁能加入我的货单……"

    merchant "我可以保证，每月给领地带来至少两百金币的稳定收入。"

    "他压低了声音。"

    merchant "当然，我也带来了一些……不那么值钱，但或许对领主大人更有用的东西。"

    merchant "消息。"

    "这个字眼让你的注意力瞬间集中。"

    hide merchant_karl_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "消息？什么样的消息？"

    hide player_char_img
    $ hide_all_chars("merchant_karl_img")
    show merchant_karl_img at left with dissolve
    merchant "这要看领主大人更关心哪方面。关于领主会议的内幕，还是关于……更私人的事？"

    "他的目光直直地看着你，瞳孔深处闪烁着精明的光。"

    menu:
        "签订贸易协议":
            $ change_stat("wealth", 25)
            if prologue_study_focus == "commerce":
                $ change_stat("wealth", 5)
            $ merchant_deal = True
            $ change_rel("rel_baron", -5)
            $ log_decision("第二章", "与商人卡尔达成贸易协议")
            hide merchant_karl_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            if prologue_study_focus == "commerce":
                player "两百金币？我看过精铁的市价——八折太高了，七五折，加上转运费由你承担。"
                hide player_char_img
                $ hide_all_chars("merchant_karl_img")
                show merchant_karl_img at left with dissolve
                merchant "（眼中闪过一丝惊讶）领主大人懂行情。七五折……成交。"
                hide merchant_karl_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
            else:
                player "两百金币？说说你的条件。"
            hide player_char_img
            $ hide_all_chars("merchant_karl_img")
            show merchant_karl_img at left with dissolve
            merchant "很简单。精铁以市价八折供货，我负责运输和销售。"
            merchant "另外，如果领主大人需要任何……特殊物品，我都能搞到。"
            merchant "稀有药草、域外典籍、甚至是某些……不便公开交易的东西。"
            hide merchant_karl_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你的'特殊物品'——具体指什么？"
            hide player_char_img
            $ hide_all_chars("merchant_karl_img")
            show merchant_karl_img at left with dissolve
            merchant "领主大人想要什么，就是什么。卡尔行走天下二十年，没有搞不到的东西。"
            merchant "当然，特殊服务需要特殊的价格。"
            hide merchant_karl_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "成交。先把贸易的事定下来，其他的以后再说。"
            hide player_char_img
            $ hide_all_chars("merchant_karl_img")
            show merchant_karl_img at left with dissolve
            merchant "愉快的合作！"
            $ hide_all_chars()
            "卡尔从斗篷内层掏出一份羊皮纸契约，条款写得密密麻麻，但核心内容和他说的一致。"
            "你仔细看了两遍，确认没有陷阱后，签下了你的名字。"
            $ hide_all_chars("merchant_karl_img")
            show merchant_karl_img at left with dissolve
            merchant "合作愉快。领主大人，这是第一个月的定金——五十金币。"
            "他递过来一个沉甸甸的皮袋。你掂了掂，重量不假。"
            merchant "另外，送领主大人一个免费的消息——作为新客户的见面礼。"
            merchant "今晚子时，在集市西头的旧仓库——会有一场不该发生的交易。如果领主大人感兴趣的话。"
            "他意味深长地笑了笑，往集市深处走了几步就和石墙的颜色混在了一起。"

        "先听听他的消息":
            $ change_stat("wealth", 5)
            $ log_decision("第二章", "向商人卡尔购买情报")
            hide merchant_karl_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "消息？什么消息值得你专程来找我？"

            "卡尔的表情变得严肃。他左右看了看，确认没有人在注意。"

            hide player_char_img
            $ hide_all_chars("merchant_karl_img")
            show merchant_karl_img at left with dissolve
            merchant "领主大人的父亲……去世前一个月，从我这里买过一样东西。"

            merchant "一本关于毒药的书。"

            "你的心跳猛然加速。"

            hide merchant_karl_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "什么？"

            "你强迫自己保持平静，但指甲已经不自觉地陷入了掌心。"

            hide player_char_img
            $ hide_all_chars("merchant_karl_img")
            show merchant_karl_img at left with dissolve
            merchant "不要惊讶，领主大人。您的父亲是个深谋远虑的人。他买那本书的时候说——"

            merchant "'如果有人想用毒药对付我，我至少要知道他们用的是什么。'"

            merchant "当时我以为他是多虑了。但后来……"

            hide merchant_karl_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "后来他就死了。"

            hide player_char_img
            $ hide_all_chars("merchant_karl_img")
            show merchant_karl_img at left with dissolve
            merchant "是的。而我知道另一件事——"

            if dusk_dew_known:
                merchant "就在老领主去世的那一天，有人从我的另一个客户那里买走了一瓶'暮色之露'。"

                "这个名字你听过——你已经知道那是什么。从卡尔的语气里，他显然也不意外你认得这个词。"

                hide merchant_karl_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "那瓶毒药，你知道是谁买的？"

                hide player_char_img
                $ hide_all_chars("merchant_karl_img")
                show merchant_karl_img at left with dissolve
                merchant "聪明。既然您已经知道它是什么，我就省去解释——直接说关键。"
            else:
                merchant "就在老领主去世的那一天，有人从我的另一个客户那里买走了一瓶'暮色之露'。"

                "你从未听过这个名字，但从卡尔的语气中，你知道它不是什么好东西。"

                hide merchant_karl_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "暮色之露是什么？"

                hide player_char_img
                $ hide_all_chars("merchant_karl_img")
                show merchant_karl_img at left with dissolve
                merchant "那是一种无色无味的毒药，服下后会在三天内发作，症状……酷似急性恶疾。"

                merchant "除非事先知道中毒的迹象，否则任何大夫都会误诊为自然病亡。"

            $ father_death_known = True
            $ poison_evidence = True
            $ father_poisoned_known = True
            $ dusk_dew_known = True

            $ hide_all_chars()
            "你强压住内心的震动，不动声色。但你的脑海里已经翻起了惊涛骇浪。"

            "父亲不是病死的。他是被毒杀的。"

            "而他自己，也许早就预感到了这个结局。"

            hide merchant_karl_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "那瓶毒药……是谁买的？"

            hide player_char_img
            $ hide_all_chars("merchant_karl_img")
            show merchant_karl_img at left with dissolve
            merchant "这个信息嘛……可就不是免费的了。五百金币，如何？"

            "五百金币。相当于艾登堡半个月的全部税收。"

            menu:
                "付钱" if wealth >= 30:
                    $ change_stat("wealth", -15)
                    merchant "领主大人爽快。买家是……教会的人。一个穿灰色修士袍的人。"

                    $ hide_all_chars()
                    "教会的人？"

                    "你的脑海中闪过主教马修斯的脸。那个慈眉善目、总是笑呵呵的老人——"

                    "不。不能太早下结论。穿灰色修士袍的人多了去了。但教会和父亲的死之间，似乎有了一条隐秘的线索。"

                    $ change_stat("intrigue", 5)
                    $ collect_item("poison_bottle")

                    $ hide_all_chars("merchant_karl_img")
                    show merchant_karl_img at left with dissolve
                    merchant "还有一件事，免费送您。那个修士买完毒药后，往北走了——不是回教堂的方向，而是去了……男爵的领地。"

                    $ hide_all_chars()
                    "男爵和教会。两股看似不相干的力量，在你父亲的死上交汇了。"

                    "你把桌上的铜板转了三圈，最后一把攥住。总有一天，你会查清楚这一切。"

                "先欠着，以后再付":
                    merchant "嗯……看在未来合作的份上，我可以等。但请领主大人记住这笔账。"
                    merchant "买家的身份，等您付清了再告诉您。"
                    merchant "不过我可以给您一个提示——免费的。那个买家……不是商人，不是贵族，也不是平民。"
                    merchant "他属于一个……特殊的阶层。"
                    "特殊的阶层？教会？军队？还是别的什么？"
                    $ merchant_deal = True

                "拒绝":
                    hide merchant_karl_img
                    $ hide_all_chars("player_char_img")
                    show player_char_img at left with dissolve
                    player "我自己会查出来的。"
                    hide player_char_img
                    $ hide_all_chars("merchant_karl_img")
                    show merchant_karl_img at left with dissolve
                    merchant "随您。不过真相这东西，有时候晚一步知道，就太迟了。"

            ## 听完消息后，卡尔主动提起贸易的事
            merchant "对了，领主大人，咱们之前说的铁矿贸易的事——您还有兴趣吗？"
            merchant "每月两百金币的稳定收入，条件不变。"

            menu:
                "签订贸易协议":
                    $ change_stat("wealth", 25)
                    $ merchant_deal = True
                    $ change_rel("rel_baron", -5)
                    hide merchant_karl_img
                    $ hide_all_chars("player_char_img")
                    show player_char_img at left with dissolve
                    player "成交。把契约拿来吧。"
                    hide player_char_img
                    $ hide_all_chars("merchant_karl_img")
                    show merchant_karl_img at left with dissolve
                    merchant "爽快！"
                    "卡尔从斗篷内层掏出一份羊皮纸契约，你仔细审阅后签下了名字。"
                    merchant "合作愉快。这是第一个月的定金——五十金币。"
                    "他递过来一个沉甸甸的皮袋。"

                "暂时不需要":
                    hide merchant_karl_img
                    $ hide_all_chars("player_char_img")
                    show player_char_img at left with dissolve
                    player "铁矿的事以后再说。"
                    hide player_char_img
                    $ hide_all_chars("merchant_karl_img")
                    show merchant_karl_img at left with dissolve
                    merchant "没关系。如果领主大人改变主意，随时来找我。银杯酒馆三楼最里面那间——敲三下。"

        "不感兴趣，婉拒":
            hide merchant_karl_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "多谢好意，但艾登堡的铁矿暂时不对外合作。"
            hide player_char_img
            $ hide_all_chars("merchant_karl_img")
            show merchant_karl_img at left with dissolve
            merchant "可惜。如果领主大人改变主意，可以来哈伦堡的旅店找我。"
            merchant "我会在这里待到月底。我的房间在银杯酒馆三楼最里面那间——记住，敲三下。"
            "商人离去了。你不知道自己错过了什么。"

    hide merchant_karl_img with dissolve

    $ hide_all_chars()
    "集市上的人越来越少。夕阳把石板路染成了橘红色。"

    "你在一个角落里找到了一张长椅，坐下来，闭上眼睛。"

    "今天发生了太多事。会议的结果、商人的消息、各领主的面孔和心机——"

    "一切都在你的脑海里旋转，像是一盘错综复杂的棋局。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve

    elena "领主大人，在想什么？"

    "艾琳娜不知什么时候站在了你面前。夕阳映在她的脸上，那双紫灰色的眼睛在光线下变得几乎透明。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "在想……我父亲在这张桌上坐了三十年，每一次是不是也像今天这样累。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "也许比今天更累。毕竟，他面对的棋局比你现在的更复杂。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你了解我父亲？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "我在王宫里听过关于他的事。他是少数几个敢在王后面前说'不'的领主。"

    elena "王后尊重他，但也忌惮他。他活着的时候，王后从不敢动加税的心思。"

    elena "现在他走了……很多人都觉得，时代变了。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "时代确实变了。但有些东西不该变。"

    "你看着远方渐渐变暗的天际线。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "领主大人……"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "嗯？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "有一天，如果我做了什么让您不理解的事——请相信，我有我的理由。"

    "这句话来得毫无征兆，像是一颗突然落下的石子。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你在说什么？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "没什么。只是……感慨而已。走吧，天快黑了。城里不比自己的领地安全。"

    $ hide_all_chars()
    "她转身先走了。空气里留下一缕淡淡的草药味——是她衣服上常有的那种。你站了一会儿，说不清在等什么。"

    "这个女人知道的，远比她表现出来的多。"

    hide elena_img with dissolve

    "你回到贵宾院，吃了简单的晚餐，然后让雷恩加强了警戒。"

    "明天一早就出发回艾登堡。会议的事已经尘埃落定，没有必要在哈伦堡多待。"

    scene bg study with dissolve
    $ unlock_gallery("bg_study")

    "入夜后，你在房间里整理今天的笔记。蜡烛的光在墙上投下摇曳的影子。"

    "你把每位领主的态度和言行都记在一张羊皮纸上——这是父亲教你的习惯。"

    "'观人于微'，他曾经说过，'一个人的立场藏在他的眼神里，他的野心写在他的手势中。'"

    "你写下了几条关键记录："

    "'格雷伯爵——提到教会时皱眉。与教会有矛盾？可利用。'"

    "'威尔斯子爵——风向标，无立场。以利诱之，不难争取。'"

    "'施泰因伯爵夫人——独立且强硬。可能的盟友，但需要找到共同利益。'"

    "'男爵——虚荣、暴躁、有野心。危险，但也正因如此，可预测。'"

    "你停下笔，看着这张纸。突然觉得自己和父亲之间的距离，在这一刻变得很近。"

    "也许父亲在这张桌上——在某个相似的夜晚——也写过类似的笔记。"

    $ play_sound("audio/sfx/door_knock.ogg")

    "两声沉闷的敲门声打断了你的思绪。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "领主大人，有个情况。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "说。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "我在城墙上巡视的时候，看到男爵的随从在城门附近和一个陌生人交谈。"

    captain "那个陌生人穿着深色斗篷，交谈结束后往南门方向走了。"

    captain "我不确定这意味着什么，但……总觉得不太对劲。"

    menu:
        "派人跟踪那个陌生人":
            $ change_stat("intrigue", 5)
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "能追上吗？"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "我已经派了一个机灵的弟兄跟上去了。但城里巷子多，不一定能跟到。"
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "好。有消息立刻告诉我。"
            "半个时辰后，士兵回来了。"
            hide captain_img
            $ hide_all_chars("soldier_generic_img")
            show soldier_generic_img at left with dissolve
            soldier "大人，那个人从南门出城了。走得很快，像是有急事。"
            soldier "我没敢跟出城外——天太黑了，而且城外有男爵的人在巡逻。"
            "男爵的人在哈伦堡城外巡逻？这不合规矩。"
            hide soldier_generic_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "记住那个人的样子了吗？"
            hide player_char_img
            $ hide_all_chars("soldier_generic_img")
            show soldier_generic_img at left with dissolve
            soldier "没看清脸。但他走路有个特点——左脚微跛。"
            "你把这个细节记在了心里。左脚微跛的人，穿深色斗篷。"

        "暂时不管，明天一早离开就是":
            hide soldier_generic_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "也许只是男爵在安排回程的事。不用太紧张。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "是，大人。不过我还是会加强夜间巡逻。"

        "去找男爵当面问":
            $ change_stat("power", 3)
            $ change_rel("rel_baron", -3)
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "走，我去找男爵问清楚。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "领主大人——这不太好吧？半夜去找男爵……"
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "怕什么。做了亏心事的人才怕半夜敲门。"
            "你大步走向男爵的住处。门口的卫兵拦住了你。"
            hide player_char_img
            $ hide_all_chars("soldier_generic_img")
            show soldier_generic_img at left with dissolve
            soldier "男爵已经歇息了，请领主大人明日再来。"
            hide soldier_generic_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "那就转告男爵——我看到了他的人在城里和陌生人接头。如果有什么事，希望他能坦诚以告。"
            $ hide_all_chars()
            "卫兵的脸色变了一下，但还是恭敬地答应了。"
            "你转身离去。不管男爵今晚做了什么，你至少让他知道——你在看着。"

    hide captain_img with dissolve

    "你回到房间，却怎么也睡不着。"

    "窗外，石板路上泛着一层冷白的光。远处传来狗吠，断断续续的。"

    "远处的钟楼敲了十二下。午夜了。"

    "你闭上眼睛，强迫自己入睡。明天还有漫长的路要走。"

    "但你有一种预感——回去的路不会太平。"

    ## 扩展剧情：领主会议闭幕日 - 签署决议，领主们告别
    call ch2_exp_aftermath from _call_ch2_exp_aftermath

    ## ============================================================
    ## 场景4：夜间危机——暗杀
    ## ============================================================

label ch2_assassination:

    $ set_mood("battle")
    $ play_music("audio/music/night_mystery.ogg", fadein=1.0)
    scene bg forest_path with dissolve
    $ unlock_gallery("bg_forest_path")

    $ trigger_random_event("travel")

    "天还没亮，你就下令出发了。"

    "与其在一个充满潜在敌人的城市里多待一刻，不如早点回到自己的地盘。"

    "队伍在星光下离开了哈伦堡的城门。清晨的空气冷得像刀子，每呼吸一口都能感觉到肺里的灼痛。"

    "你裹紧斗篷，策马走在队伍中间。艾琳娜紧跟在你身后。"

    "一路无事。穿过莱因河谷，走过渡鸦旅店——你连停都没停，只是让士兵们换了马匹和饮水。"

    "你想尽快赶回去。直觉告诉你，速度是最好的护身符。"

    "……"

    "夜深了。你的队伍在返回艾登堡的路上，穿过一片密林。"

    "这是旅途的最后一段。再过一个时辰，你就能看到艾登堡的城墙了。"

    if deep_marcus_confession == "distance":

        "忽然，前方林道有马蹄声由远及近。"

        "树木的缝隙里，月光照出一个骑手——他勒住马，静静看着你的队伍过去。"

        "但你没有停下，也没有回头。"

        "那马蹄声从你身边擦过，随后逐渐远去。"

    "月光被树冠遮挡，四周一片漆黑。马蹄踩在落叶上发出沙沙的声响，偶尔有枯枝在马蹄下折断，声音尖锐刺耳。"

    "夜风从林间穿过，带着一股潮湿的腐败气息。"

    if intrigue >= 35 or (rel_elena >= 15 and spy_network):
        "你的直觉告诉你有什么不对。"

        "树林太安静了——没有虫鸣，没有夜鸟。甚至连风声都突然消失了，像是整片森林屏住了呼吸。"

        "你的后颈汗毛倒竖。这种感觉，你在王都的兵法课上学到过一个词来形容——"

        "'杀气'。"

        show elena_img at right with dissolve

        elena "（极轻的耳语）领主大人……我也感觉到了。"

        hide elena_img with dissolve

        menu:
            "立刻下令警戒":
                $ play_sound("audio/sfx/sword_draw.ogg")
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "全军警戒！有埋伏！"
                "你的声音在寂静的林中炸开，像是一块石头砸碎了一面镜子。"
                jump ch2_ambush_prepared

            "悄悄让雷恩做准备":
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "（低声）雷恩，做好战斗准备。不要声张。"
                $ hide_all_chars("captain_img")
                show captain_img at left with dissolve
                captain "（低声）明白。"
                "雷恩无声地示意后方的士兵们悄悄拔出武器。动作之默契，说明他们经历过不止一次夜间伏击。"
                hide captain_img with dissolve
                jump ch2_ambush_prepared
    else:
        $ hide_all_chars()
        "你的脑海里还在回想着会议上的种种细节，并没有留意到周围的异常。"

        "士兵们也困了。几个人在马背上直打瞌睡。"

        "突然——"
        jump ch2_ambush_surprised

label ch2_ambush_prepared:
    $ change_stat("power", 10)
    $ change_stat("loyalty", 10)
    $ assassination_survived = True

    $ play_music("audio/music/chase.ogg", fadein=0.5)
    "话音刚落，黑暗中射出数支弩箭！"

    "嗖嗖嗖——箭矢破空的声音在寂静的夜里格外刺耳。"

    "但你的士兵早有准备，用盾牌挡住了致命的一击。"

    "弩箭叮叮当当地弹在铁盾上，溅出几点火星。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "伏兵！保护领主！"

    $ hide_all_chars()
    "雷恩的声音如同雷鸣。他抽出长剑，翻身下马，挡在你前面。"

    "一场混战在黑暗中爆发。"

    "袭击者训练有素——他们从树上跳下，无声无息地扑向你的卫兵。动作迅捷凶猛，像是一群黑色的猎豹。"

    "但你的卫队更胜一筹。雷恩挑选的都是百战之兵，即便在突袭中也能迅速组成防御阵型。"

    $ play_sound("audio/sfx/sword_draw.ogg")

    "你也拔出了剑。虽然你的剑术不如雷恩，但父亲从小就教过你——领主的剑不能只是装饰品。"

    "一个黑衣人从侧面扑来，弯刀直劈你的脖颈。你本能地举剑格挡——"

    "叮！"

    "巨大的力量差点让你脱手。但你稳住了，随即用脚踹中对方的腹部。"

    "黑衣人踉跄后退，被赶来的卫兵一刀劈倒。"

    show elena_img at right with dissolve

    $ hide_all_chars()
    "你余光看到艾琳娜从腰间抽出一把匕首，干净利落地划开了一个偷袭她的黑衣人的喉咙。"

    "那个动作太熟练了——不是侍从的手法，更像是……杀手。"

    "但你没有时间细想。"

    hide elena_img with dissolve

    "几分钟后，大部分袭击者被击退。残余的黑衣人消失在树林深处，像是来时一样无声无息。"

    "地上留下了五具尸体和一个受伤的俘虏。你的士兵也有伤亡——两人重伤，一人轻伤。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "领主大人，抓到一个活的！"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "让我看看他。"

    $ hide_all_chars()
    "你蹲下身，借着火把的光查看这个刺客。他穿着黑色紧身衣，脸上蒙着布。"

    "你扯下他的面罩——是一张陌生的脸，年纪不大，二十出头，面容清秀得不像杀手。"

    "但他的眼神冰冷如铁——那是受过严格训练的人才会有的目光。"

    "你翻开他的袖子——手腕内侧有一个刺青。"

    "一把匕首刺穿一朵百合花。"

    "暗百合。"

    $ collect_item("lily_symbol")

    hide captain_img with dissolve

    if father_death_known:
        "和那封密信上的标记一模一样。暗百合——先是神秘的信件，现在是杀手。他们到底是敌是友？"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    hide captain_img
    $ hide_all_chars("assassin_char_img")
    show assassin_char_img at left with dissolve
    assassin "呵……你比你父亲机警。"

    "俘虏开口了。他的声音沙哑，像是嗓子受过伤。"

    hide assassin_char_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "谁派你来的？"

    hide player_char_img
    $ hide_all_chars("assassin_char_img")
    show assassin_char_img at left with dissolve
    assassin "杀了我吧。我什么都不会说。"

    "他的语气平静得可怕，像是真的已经做好了赴死的准备。"

    menu:
        "交给雷恩审讯":
            $ change_stat("power", 5)
            hide assassin_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "交给我，领主大人。我有的是办法让他开口。"
            $ hide_all_chars()
            "雷恩的语气变平了。他把俘虏拖到一边，脚步声很快被林中的虫鸣吞没了。"
            "不久后，你听到了一声压抑的惨叫。"
            "你知道雷恩的手段不会温柔。但在这个时候，你需要答案。"
            "半个时辰后，雷恩回来了。"
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "大人。他只说了一件事——'七瓣莲花将在月圆之夜绽放'。然后就……咬舌了。"
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "死了？"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "没死。我堵住了他的嘴。但他再也说不出话来了。"
            "七瓣莲花……月圆之夜……又是谜语。暗百合的人似乎只会用这种方式说话。"

        "亲自审讯——用智慧而非暴力":
            $ change_stat("intrigue", 5)
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你的组织想杀我，同时又在一个月前邀请我去磨坊会面。这不矛盾吗？"
            hide player_char_img
            $ hide_all_chars("assassin_char_img")
            show assassin_char_img at left with dissolve
            assassin "……"
            "刺客的眼神闪动了一下。你抓住了这个破绽。"
            hide assassin_char_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "所以，派你来的人和写那封信的人，不是同一个人。暗百合内部有分歧。"
            hide player_char_img
            $ hide_all_chars("assassin_char_img")
            show assassin_char_img at left with dissolve
            assassin "……你比我想象的聪明。"
            hide assassin_char_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "让我猜猜。你们中有人想让我活着，有人想让我死。而你属于后者。"
            "刺客沉默了很长时间。然后，他说了一句话。"
            hide player_char_img
            $ hide_all_chars("assassin_char_img")
            show assassin_char_img at left with dissolve
            assassin "那朵百合花有七片花瓣。有些朝上，有些朝下。你猜——你父亲是哪一片？"
            $ hide_all_chars()
            "你愣住了。父亲……和暗百合有关？"
            "在你追问之前，刺客突然挣脱了束缚——不是向你冲过来，而是撞向了旁边的一棵树。"
            "头骨撞击树干的声音，在寂静的夜里格外沉闷。"
            hide assassin_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "他……死了。"
            $ hide_all_chars()
            "你看着那具瘫软的身体。"
            "父亲是百合花的一片花瓣——这是什么意思？"

        "放了他，让他带话回去":
            $ change_stat("intrigue", 8)
            $ change_rel("rel_lily", 10)
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "回去告诉你的主人，我不是猎物，是谈判对象。"
            "刺客惊愕地看着你。显然，他没有想到这种反应。"
            player "下次再来，带的不是弩箭，而是条件。"
            $ hide_all_chars()
            "你割断了他的绳子。"
            "雷恩急了。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "领主大人！这——"
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "放他走，雷恩。"
            $ hide_all_chars()
            "刺客活动了一下麻木的手腕。他看了你很久，然后做了一件出人意料的事——"
            "他单膝跪下，对你行了一礼。"
            hide player_char_img
            $ hide_all_chars("assassin_char_img")
            show assassin_char_img at left with dissolve
            assassin "你和你父亲一样……出人意料。"
            "然后他转身走了，走得比来的时候快。"
            hide assassin_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "领主大人……您确定这样做是对的？"
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "不确定。但如果暗百合真的和父亲有关联，我需要一条对话的渠道。"
            player "一条用弩箭打不开的渠道。"

    hide captain_img with dissolve

    $ hide_all_chars()
    "战斗结束了，但疑问像刺客留下的血迹一样蔓延开来。"

    "你看着地上那些黑衣刺客的尸体。他们的装备精良，动作配合默契——这不是一般的盗匪。"

    "训练这样一支队伍需要大量的时间和金钱。暗百合的背后，一定有强大的力量支撑。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve

    elena "领主大人，您受伤了吗？"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "没事。你呢？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "只是一些擦伤。"

    "你看着她。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "艾琳娜，你刚才杀那个人的时候，动作非常专业。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "在王宫里，每个侍从都要学基本的防身术。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "那不是防身术。那是杀人术。"

    "艾琳娜的瞳孔微微收缩了一下。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "……领主大人看到了不该看到的东西。"

    elena "但既然您看到了，我只能说——我有我的过去。王后选中我来艾登堡，不仅仅是因为我会写字算账。"

    elena "我的职责是保护您的安全。这也是王后的意思。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "保护我，还是监视我？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "两者不矛盾。"

    "她的语气不卑不亢。你盯着她的眼睛看了片刻，然后笑了一下。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "至少，你是个诚实的监视者。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "我尽量。"

    hide elena_img with dissolve

    ## 玩家此刻已知 elena 是王后派来的(2925"王后选中我来艾登堡"+2944"诚实的监视者"),
    ## set flag 防 chapter 3 elena 身份揭露段(if not elena_spy_known)信息重复.
    $ elena_spy_known = True

    jump ch2_end

label ch2_ambush_surprised:
    $ assassination_survived = True

    "一切发生在一瞬间。"

    "先是马匹突然躁动不安——你的坐骑打了个响鼻，不肯继续往前走。"

    "你还没来得及反应——"

    "树丛中突然射出数支弩箭！"

    "嗖——嗖——嗖——"

    "走在最前面的一个士兵中箭倒地，连惨叫都没来得及发出。"

    "紧接着，第二支箭——直奔你的面门。"

    "你本能地侧头，箭矢擦过你的脸颊，锋利的箭头割开了皮肤。鲜血顺着下颌滴落在斗篷上。"

    "如果你晚偏一寸——那支箭就射进了你的眼睛。"

    "疼痛让你瞬间清醒。恐惧紧随其后——但很快被愤怒取代。"

    $ play_sound("audio/sfx/sword_draw.ogg")

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "伏兵！保护领主！"

    $ hide_all_chars()
    "混乱中，雷恩从旁边策马冲过来，用盾牌挡在你身前，为你挡住了第二轮箭雨。"

    "一支箭射穿了他的左肩。箭头从肩胛骨后面探出来，血花飞溅。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "嘶——没事！小伤！领主大人快走！"

    $ hide_all_chars()
    "他的声音因为疼痛而变得嘶哑，但手中的剑依然稳当。"

    $ change_rel("rel_captain", 15)

    "黑暗中，不知道有多少敌人。你只能看到影子——像幽灵一样在树间穿梭的黑色影子。"

    "你的卫兵在混乱中组织起了防线。钢铁碰撞的声音、喊叫声、马嘶声混成一片。"

    "一个黑衣人冲到了你面前，弯刀带着呼啸砍来——"

    show elena_img at right with dissolve

    "电光石火之间，一道银光从侧面闪过。艾琳娜不知何时出现在你身旁，她手中的匕首精准地刺入了黑衣人的咽喉。"

    elena "领主大人，快走！"

    "你来不及惊讶于她的身手。更多的敌人涌上来了。"

    hide elena_img with dissolve

    $ hide_all_chars()
    "你拔出剑，和雷恩背靠背，在黑暗中厮杀。"

    "刀锋划过空气的声音、金属碰撞的火花、喘息声和怒吼声——一切都混在一起，变成了一团嗜血的噩梦。"

    "你挡住了一个黑衣人的劈砍，反手一剑，在他的手臂上划出一道深深的口子。"

    "那人发出一声闷哼，后退了几步，黑得只能看见轮廓，然后连轮廓也没了。"

    "又一个黑衣人从你的左侧冲过来。你来不及反应——"

    "一把剑从你身后探出，挡住了那致命的一击。是雷恩。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "大人！注意左边！"

    $ hide_all_chars()
    "他单手举着盾牌，肩膀上的箭还插着，鲜血已经把半边铠甲都染红了。但他的剑依然凶猛。"

    "不知过了多久，袭击者终于撤退了。"

    "他们来得无声无息，去得也毫无征兆。"

    "一瞬间，林中又恢复了死一般的寂静。只有伤者的呻吟和马匹的嘶鸣。"

    "你的卫队拼死反击，最终击退了袭击者。"

    "地上留下了三具黑衣人的尸体。没有活口。"

    "你的队伍损失惨重——四人受伤，一匹马倒毙。那个中第一箭的士兵，已经没有了呼吸。"

    "你蹲在他身边，看着他年轻的、永远定格在惊愕中的脸。他叫什么名字？你竟然不知道。"

    "一个在你的队伍里为你卖命的人，你连他的名字都不知道。"

    "你蹲在那里没动。靴子在血泊边缘蹭了一下，留下一道红印。"

    "但你在其中一具尸体的手腕上发现了一个刺青——"

    "一把匕首刺穿一朵百合花。暗百合。"

    if father_death_known:
        "和那封密信上的标记一模一样。他们到底想要什么？"
        "先是信件，后是刺客。暗百合对你的态度似乎并不统一。"
    else:
        "你从未见过这个标记，但本能告诉你它很重要。"
        "你把那只手臂上的图案仔细记在了心里。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "领主大人，您的脸……让我处理伤口。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "先处理你的肩膀。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "小伤——"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "那不是小伤。你肩膀上插着一支箭。"

    "你叫来一个会基本包扎的士兵，帮雷恩处理了伤口。箭头拔出来的时候，雷恩连眉头都没皱一下。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "领主大人……是我失职。应该提前派斥候探路的。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "不怪你。我们都没料到会在自己的地盘附近遇袭。"

    "你看着雷恩满是血污的脸，嗓子一紧，想说什么却卡在了喉咙里。"

    player "雷恩。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "大人？"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "谢谢你。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "……这是属下分内之事。"

    "他别过头去。但你看到他的眼眶红了一瞬。"

    hide captain_img with dissolve

    jump ch2_end

    ## 章节深化：间谍的代价 / 男爵的私信
    call ch2_deep_spy from _call_ch2_dspy
    call ch2_deep_baron_letter from _call_ch2_dbl

    ## 治理系统：饥荒危机 / 建设工程
    call gov_famine_crisis from _call_gov_famine2
    call gov_building from _call_gov_build2

    ## 治理报告
    call gov_report from _call_gov_rep2

    ## ============================================================
    ## 第二章结尾
    ## ============================================================

label ch2_end:

    $ set_mood("tense")

    $ clamp_stats()
    $ check_max_stat()
    $ persistent.chapters_completed.add("chapter2")

    ## 章节结束统计
    call show_chapter_summary("第二章", "领主会议") from _call_show_chapter_summary

    ## 章节间过渡：返程旅途（含暗林谷伏击）— 须在"回到艾登堡"scene 之前
    call interlude_ch2_ch3 from _call_interlude23_at_ch2end

    $ play_music("audio/music/tension.ogg", fadein=2.0)
    scene bg castle_exterior with dissolve
    $ unlock_gallery("bg_castle_exterior")

    "你带着伤口和疑问回到了艾登堡。"

    "当城堡的轮廓出现在地平线上时，你长长地出了一口气。那座灰色的城堡从未像今天这样让你觉得亲切。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "领主大人！您回来了！脸上的伤——"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "无碍。一点皮外伤。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "发生了什么事？"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我们在回来的路上遇到了伏击。暗百合的人。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "暗百合……"

    "奥尔德里克的脸色变了。他的手不自觉地攥紧了椅子扶手。"

    if aldric_personal_done:
        ## 奥尔德里克的秘密已在章节前段揭示——此处为回顾性对话
        aldric "暗百合……当年刺杀先王的刺客，走的也是暗道。今天这些人伏击您的手法——训练有素，装备精良，绝不是寻常匪徒。"

        hide aldric_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "你觉得和当年的事有关？"

        hide player_char_img
        $ hide_all_chars("aldric_img")
        show aldric_img at left with dissolve
        aldric "老臣不敢妄下定论。但三十年了，那些暗中行事的人……也许从未消失。"

        "他的目光落在你身上，带着一种你熟悉的沉重——那是他在书房中向你坦白骑士团往事时同样的神情。"

        aldric "领主大人，先让大夫处理您的伤口。今晚的事，明日再细细商议。"
    else:
        ## 安全兜底：若支线未触发
        aldric "领主大人，有些事……也许到了该告诉你的时候了。"

        aldric "但不是现在。先让大夫处理您的伤口，好好休息一晚。明天，老臣有话对您说。"

        hide aldric_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "关于父亲？"

        hide player_char_img
        $ hide_all_chars("aldric_img")
        show aldric_img at left with dissolve
        aldric "关于一切。"

    "老骑士的语气异常沉重。你从他脸上读到了深深的忧虑——不只是为今晚的伏击，更像是某种古老的恐惧被重新唤醒。"

    hide aldric_img with dissolve

    $ hide_all_chars()
    "你回到大厅。城堡里的仆人们听说了伏击的事，都紧张得不行。"

    "一个年轻的侍女端着热水和药膏跑过来，手都在抖。"

    $ hide_all_chars("servant_marta_img")
    show servant_marta_img at left with dissolve
    maid "领主大人！您受伤了！让我来……让我来处理……"

    hide servant_marta_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "不用紧张。只是擦伤。"

    $ hide_all_chars()
    "你让她帮你清洗了脸上的伤口。药膏涂上去的时候，一阵刺痛让你咬紧了牙关。"

    "侍女退下后，你独自坐在大厅的长椅上。壁炉里的火烧得很旺，但你觉得浑身发冷——那是战斗过后的虚脱，也是肾上腺素退去后的反噬。"

    "你的手还在微微发抖。你把手插进口袋里，不想让任何人看到。"

    $ play_sound("audio/sfx/door_knock.ogg")

    "轻轻的脚步声。"

    $ play_music("audio/music/romance.ogg", fadein=2.0)
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve

    "艾琳娜端着一碗热气腾腾的汤药走过来。她换了一身干净的衣服，但右手虎口的伤口还缠着白布。"

    elena "领主大人，大夫配的汤药。说是活血化瘀的，趁热喝。"

    "你接过碗。药很苦，但热度从喉咙一路烧到胃里，冰冷的身体终于有了一丝暖意。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你的手——"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "已经处理过了。真的只是擦伤。"

    $ hide_all_chars()
    "她在你旁边坐下，拿起一条干净的布巾，蘸了清水，轻轻擦拭你脸上伤口周围的血迹。"

    "她的动作很轻，轻得几乎感觉不到。但每一次布巾碰到皮肤，你都能感受到她指尖传来的微微颤抖。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "会留疤吗？"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "大概会。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "……对不起。如果我更早发现那些伏兵——"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你已经说过了。不是你的错。"

    $ hide_all_chars()
    "壁炉里的木柴发出一声脆响，火星四溅。"

    "你看着跳动的火焰，脑海里闪过林中那些黑衣人冰冷的眼神，闪过第一个中箭倒下的士兵——你连他的名字都不知道。"

    "你咬住腮帮肉，咬得嘴里泛起铁锈味。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "今天……有人为我死了。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "……是的。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我甚至不知道他叫什么名字。一个为我卖命的人，我连他是谁都不知道。"

    "你的声音在最后几个字上微微发颤。你没有刻意隐藏——也许是因为太累了，也许是因为，在这个深夜的壁炉前，你终于可以不像一个领主那样伪装。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "他叫吕克。二十三岁，北方边境的农家子弟。去年入伍，弓术很好。"

    "你猛地转头看向她。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你认识他？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "我记住了队伍里每一个人的名字和来历。这是我的习惯。"

    "她的眼眶微微泛红，但没有哭。她只是静静地看着你，目光里有一种你从未在她脸上见过的东西——不是同情，不是怜悯，而是……共鸣。"

    elena "领主大人，吕克的死不是你的错。战场上的事，谁都无法完全掌控。"

    elena "但你记住了他。这就够了。一个记住每一个牺牲者名字的领主——值得为他赴死。"

    "你低下头，盯着碗里残余的药汤。深褐色的液面上映出你自己的倒影——疲惫的、带着伤疤的、年轻的脸。"

    menu:
        "向艾琳娜敞开心扉——『有时候，我真的不知道自己能不能扛住。』":
            $ change_rel("rel_elena", 15)
            $ change_stat("loyalty", 5)
            $ log_decision("第二章", "在受伤后向艾琳娜敞开心扉")
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "艾琳娜……有时候，我真的不知道自己能不能扛住这一切。"
            player "父亲扛了三十年。他比我强太多了。而我——我只是个从学院回来的年轻人。"
            player "我甚至不知道怎么给一个为我死去的士兵的家人写信。"
            $ hide_all_chars()
            "艾琳娜沉默了片刻。然后她做了一件意想不到的事——"
            "她伸出手，轻轻握住了你的手。"
            "她的手指冰凉，但握得很紧。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "你不需要和你父亲一样。你只需要做你自己。"
            elena "领主大人……不。让我叫你的名字。"
            elena "你已经比你以为的更坚强了。今天的你，和一个月前从王都赶回来的那个少年——已经不是同一个人了。"
            $ hide_all_chars()
            "你看着她的手。那只手上有茧，有伤口，有岁月的痕迹——这不是一双养尊处优的手。"
            "你没有抽回手。"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "……谢谢你。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "不用谢我。我只是……在做我想做的事。"
            $ hide_all_chars()
            "她的手指微微收紧了你的手背。那一刻，你觉得她不像王后的密探，不像精于权术的侍从——"
            "她只是一个在深夜里握着你手的人。"

        "保持距离——『你不需要担心我。我是领主，这是我的责任。』":
            $ change_stat("power", 5)
            $ change_stat("loyalty", 5)
            $ log_decision("第二章", "在受伤后保持了领主的距离感")
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你不需要担心我。这条疤会好的。吕克的事……我会记住，然后继续走下去。"
            player "领主不能在下属面前露出软弱。这是父亲教我的第一课。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "……领主大人说得对。"
            "她收回了手中的布巾，重新恢复了那副公事公办的神情。但你没有错过她眼中一闪而过的失落。"
            elena "那您早点休息。如果伤口有任何不适，随时叫我。"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "好。你也去休息吧。"
            $ hide_all_chars()
            "她站起身，向你行了一礼。脚步声在走廊里渐渐远去。"
            "你独自坐在空荡荡的大厅里。角落里堆着没拆的信，每一封都在等你拿主意。"
            "你知道自己做了正确的选择——至少是一个领主应该做的选择。"
            "但为什么心里会有一种空落落的感觉？"

        "转移话题——『告诉我关于暗百合你知道的一切。』":
            $ change_stat("reputation", 5)
            $ change_rel("rel_elena", 5)
            $ log_decision("第二章", "在受伤后追问暗百合的情报")
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "艾琳娜，别管伤口了。告诉我——暗百合，你知道多少？"
            "艾琳娜的表情微微一变。她放下布巾，正视着你的眼睛。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "暗百合……是一个古老的组织。至少有两百年的历史。"
            elena "在王宫里，它像是一个传说——所有人都听过，但没有人真正见过。"
            elena "据说他们不效忠任何领主、任何王室。他们有自己的信条——"
            elena "'在黑暗中守护平衡。'"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "守护平衡？他们今晚可不像是在守护平衡。他们在杀我。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "这正是奇怪的地方。如果暗百合真的派人杀你……他们不应该失败的。"
            elena "除非——那些杀手不是暗百合的主流势力。可能是一个分支，或者……冒名的。"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你的意思是，有人在利用暗百合的名义？"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "我不确定。但有一件事我确定——"
            elena "暗百合的标记不是随便什么人都能纹在手腕上的。那个刺青需要特殊的墨水和仪式。"
            elena "所以那些人和暗百合确实有关。只是……关系有多深，我不清楚。"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你知道的比你说的多。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "……也许吧。但有些事，不到时候不能说。请您相信我。"
            "你盯着她看了很久。她没有躲闪。"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "好。我暂时信你。"

    "夜已经很深了。大厅里只剩你们两个人和桌上没收走的盘子。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "领主大人，喝完药就去休息吧。伤口需要时间愈合——身上的和心里的都是。"

    "她最后看了你一眼，然后轻轻地走了。"

    hide elena_img with dissolve

    $ set_mood("calm")

    scene bg study with dissolve
    $ unlock_gallery("bg_study")

    "你回到书房坐下。桌上的墨水瓶没盖盖子，边上的羊皮纸蜷了角。那道新鲜的伤痕在铜镜的反光中显得格外醒目。"

    "你拿起桌上的铜镜，仔细端详自己的面容。"

    "铜镜里映出的是一张年轻的脸——但已经不再稚嫩了。脸颊上那道浅浅的血痕，像是命运留下的第一道刻印。"

    "你把铜镜放下，闭上眼睛。"

    "你闭上眼，但脑子停不下来。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve

    "你正准备上楼，艾琳娜又出现在书房门口。她似乎换了一身衣服，发丝还带着些许水汽。"

    elena "领主大人，还没休息？"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "在整理笔记。你呢？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "睡不着。"

    "她走进来，在你对面坐下。深夜的凉意跟着她一起溜了进来，你注意到她的轮廓比白天柔和了许多。"

    if aldric_personal_done:
        elena "领主大人，奥尔德里克说今晚的伏击和当年的事有关……您怎么看？"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "他告诉过我先王遇刺的经过。如果暗百合真的和三十年前那些人有关……"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "那就不只是一群刺客那么简单了。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "一切都和父亲有关。"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "……是的。而且恐怕比我们想象的更深。"
    else:
        elena "领主大人，明天奥尔德里克要和您谈的事，恐怕不会轻松。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "你知道他要说什么？"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "不知道。但从他的表情来看……应该和您父亲有关。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "一切都和父亲有关。"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "……是的。也许是时候面对那些被埋藏的真相了。"

    $ hide_all_chars()
    "她站起身，把椅子轻轻推回桌边，头也不回地走了。"

    "门在她身后关上的那一刻，你忽然觉得书房变得空荡荡的。"

    hide elena_img with dissolve

    scene bg bedroom with dissolve

    "你上楼，躺在床上。"

    "身体因为疲惫而沉重，但脑子却异常清醒。"

    "你坐在窗前，望着窗外的月亮。夜风从窗缝里渗进来，带着初冬的寒意。"

    "领主会议的结果已经传遍了各个领地——"

    if council_outcome == "反对":
        "你站在了男爵一边，公然反对王后。这让你赢得了部分领主的尊重，但也上了王后的黑名单。"
        "男爵的联名信已经快马送往王都。等到王后读到你的名字时——你不知道等待你的会是什么。"
    elif council_outcome == "支持":
        "你支持了王后的新税法。王后会记住你的忠诚，但男爵视你为叛徒。"
        "在男爵看来，你背叛了你父亲的遗志。这个仇，他会记一辈子。"
    elif council_outcome == "折中":
        "你的折中方案赢得了广泛赞誉。但真正的考验是——王后会接受你的条件吗？"
        "如果她接受了，你就是促成领主与王室和解的功臣。如果她拒绝……你就在两边都不讨好。"

    "而暗杀事件让一切变得更加复杂。"

    "有人想要你的命。是男爵？是暗百合？还是另有其人？"

    "刺客的装备和训练水平都不是普通势力能提供的。在你的领地周围，有一股你看不见的力量在运作。"

    if poison_evidence:
        "商人卡尔的话在你脑海中回响——父亲死于毒药，而买毒药的人……与教会有关。"
        "毒药、刺客、秘密组织——这一切之间有什么联系？"
        "你在纸上写下了三个名字：暗百合、教会、男爵。然后在它们之间画上了问号。"

    "你望向窗外的月亮。它已经圆了。"

    "圆月把树影投在地上，那些影子斑驳交错，像是无数只窥探的眼睛。"

    if father_death_known:
        "磨坊……那封信约你满月之夜去磨坊。"
        "今夜就是满月。"
        "你看着那轮悬在天边的满月，脑海中浮现出信上的字迹——'若想知道真相，满月之夜，独自来磨坊。'"
        "你把那封信揉成一团又展开来，折痕已经模糊了字迹。不管那里等待你的是陷阱还是答案——你都必须去。"

        "远处，城堡的钟楼响起了午夜的钟声。十二下沉闷的回响，在寂静的夜空中久久不散。"

        "你披上深色斗篷，从侧门溜出城堡。月光把你的影子拉得很长。"

        scene bg forest_path with dissolve

        "磨坊在镇子边缘，紧挨着一片枯死的老林。月光下，那座废弃的石磨坊像一头沉睡的巨兽。"

        "你推开虚掩的木门。铰链发出刺耳的尖叫。"

        "里面空无一人。"

        "但墙壁上——月光从破洞照进来，正好落在一处刻痕上。"

        "一朵百合。花瓣舒展，根部缠绕着荆棘。暗百合的标记。"

        "旁边的石台上放着一只小木盒，盒盖上压着一张羊皮纸。"

        "你展开纸条。字迹工整而陌生——"

        "「你来了。这说明你还有求真的勇气。」"

        "「但今夜不是时候——你身后有人跟踪。我们都不安全。」"

        "「留意你身边的人。你父亲的死不是孤例。暮色之露仍在流通。」"

        "「下次见面，不会再是纸条。」"

        "纸条没有署名。你翻过来——背面画着一个简单的符号：一只睁开的眼睛。"

        $ dark_lily_first_contact = True
        $ dusk_dew_known = True

        "你把纸条收入怀中。木盒里只有一小瓶深紫色的液体和一张标签——'暮色之露·样本'。"

        "你迅速环顾四周。月光下，远处似乎有个影子一闪而过，但当你追出门时，只剩空荡荡的林间小路。"

        scene bg study with dissolve

        "你沿原路返回城堡，心跳一路没有平复。"

        "纸条上的话在你脑中翻来覆去——'你父亲的死不是孤例'。这些人知道的比你多得多。"

        "但他们为什么要帮你？"

    if not father_death_known:
        "远处，城堡的钟楼响起了午夜的钟声。十二下沉闷的回响，在寂静的夜空中久久不散。"

    "回到艾登堡的那一刻，你才意识到自己有多累。"

    "窗外，一只夜枭发出了一声长鸣。悠远而苍凉，像是古老的预言。"

    "你沉沉睡去。梦里，有一朵百合花在黑暗中缓缓绽放。"

    if dusk_dew_known:
        "它的花瓣洁白如雪，却散发着淡淡的苦杏仁味——那是暮色之露的气息。"
    else:
        "它的花瓣洁白如雪，却散发着一股淡淡的苦杏仁味——那味道你从未闻过，但它让你背脊发凉，仿佛本能知道那不属于花香的范畴。"

    "花瓣上站着七个影子。其中一个，看起来很像你的父亲。"

    "他朝你伸出手，嘴唇微动，似乎在说什么。但你听不见。"

    "你拼命想靠近他——"

    "然后你醒了。"

    $ play_music("audio/music/dawn.ogg", fadein=2.0)
    "窗外，天色已经微微发白。又是新的一天。"

    "属于你的棋局，已经进入了第二回合。"

    scene black with dissolve

    $ renpy.force_autosave()

    jump chapter3_start

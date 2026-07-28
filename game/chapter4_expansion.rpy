## ============================================================
## 第四章扩展：王都探索与觐见准备
## 在 chapter4.rpy "这场棋局，你不能输。" 之后被 call 调用
## ============================================================

## 新变量定义
default ch4_exp_explored_market = False
default ch4_exp_explored_cathedral = False
default ch4_exp_explored_slums = False
default ch4_exp_heard_prince_rumor = False
default ch4_exp_met_reinhart = False
default ch4_exp_met_countess = False
default ch4_exp_library_clue = False
default ch4_exp_overheard_plot = False
default ch4_exp_lily_contact = False
default ch4_exp_eve_strategy = ""
default ch4_exp_court_impression = ""
default ch4_exp_slum_info = False
default ch4_exp_cathedral_prayer = False
default ch4_exp_merchant_tip = False
default ch4_exp_reinhart_favor = 0
default ch4_exp_countess_trust = 0
default ch4_exp_preparation_level = 0

## ============================================================
## Part 1: 抵达王都（第二天清晨，正式探索）
## ============================================================

label ch4_exp_arrival:

    $ play_music("audio/music/great_hall.ogg", fadein=2.0)
    scene bg royal_palace with dissolve
    $ set_mood("normal")

    "又是一个清晨。王都的头几天已经在观察、打探和夜巡里悄悄溜走——今天，你在丝绸床单上醒来。"

    "窗外传来王都特有的喧嚣——远处钟楼的晨钟、街上马车的辘辘声、还有卖花女清脆的叫卖。"

    "贵宾馆的套房比艾登堡那间石砌卧室阔气太多，你至今没习惯。"

    $ play_sound("audio/sfx/knock.ogg")

    "一阵急促的敲门声打断了你的思绪。"

    show elena_img at right with dissolve

    elena "领主大人，该起来了。礼典官已经在楼下等候。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "礼典官？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "觐见王后有一套繁琐的礼仪。他来教您……怎么跪，怎么说话，怎么呼吸。"

    "她的语气里带着一丝嘲讽。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我还需要学怎么呼吸？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "在王后面前，连呼吸的节奏都不能出错。"

    hide elena_img with dissolve

    $ hide_all_chars()
    "你穿戴整齐后下了楼。"

    "大厅里站着一个瘦高的男人，身穿紫色的宫廷制服，胸前挂着银质的礼典徽章。"

    "他看起来大约五十岁，脸上的表情像是用尺子量出来的——精确、刻板、毫无温度。"

    narrator "礼典官微微欠身，动作如同提线木偶般优雅而僵硬。"

    narrator "「艾登堡领主阁下，鄙人奥伯特·冯·魏德纳，王室首席礼典官。」"

    narrator "「奉王后陛下之命，前来为阁下讲解觐见礼仪。」"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "有劳了。"

    $ hide_all_chars()
    narrator "礼典官从袖中取出一卷羊皮纸，展开后足有三尺长。"

    narrator "「首先，关于称谓——」"

    narrator "「觐见的是摄政王后伊莎贝拉陛下。注意，是「陛下」，不是「殿下」。」"

    narrator "「虽然她并非国王，但摄政期间享有与国王同等的礼遇。」"

    narrator "「进入觐见厅后，在红线处止步，行三鞠躬礼。第一鞠躬向王座，第二鞠躬向王后本人，第三鞠躬向王室徽章。」"

    narrator "「王后开口前，不可主动说话。王后未许可前，不可落座。王后未示意前，不可抬头直视。」"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "规矩还真多。"

    narrator "礼典官面无表情地说：「这已经是简化版了。完整版有七十二条。」"

    menu:
        "认真学习每一条礼仪":
            $ change_stat("intrigue", 5)
            $ change_stat("reputation", 3)
            $ change_courage(-8)
            $ ch4_exp_preparation_level += 2

            player "请详细说明。我不想在王后面前失礼。"

            $ hide_all_chars()
            narrator "礼典官罕见地露出一丝赞许的神色。"

            narrator "「很好。大多数地方领主都觉得这些是无聊的繁文缛节。」"

            narrator "「但在王都，礼仪就是武器。一个错误的鞠躬角度，可能意味着冒犯；一句不合时宜的话，可能被解读为叛逆。」"

            "你花了整整一个时辰，记下了所有的细节。"

            "鞠躬的角度、退步的距离、说话的措辞……每一个环节都有严格的规定。"

            "枯燥，但你知道这些知识在明天可能救你一命。"
            "等你把七十二条规矩在脑子里过完，已是深夜。你回房躺下，那些角度和措辞还在翻来覆去，迷迷糊糊到天快亮才合眼。明天得顶着这口气上场。"

        "挑重点记，其他随机应变":
            $ change_stat("intrigue", 3)
            $ ch4_exp_preparation_level += 1

            player "把最重要的告诉我就行。其他的，我随机应变。"

            narrator "礼典官嘴角微微一抽，但还是照做了。"

            narrator "「那么——最重要的三点：」"

            narrator "「第一，不要直视王后的眼睛超过三秒。她会把长时间的注视视为挑衅。」"

            narrator "「第二，不要提及先王。这是宫中的禁忌话题。」"

            narrator "「第三，如果王后赐酒，必须饮尽。这是信任的象征——拒绝等于表示你怀疑她会下毒。」"

            "你点点头，把这三条记在心里。"
            "剩下的时间你留给了自己——早点歇下，养足精神。该记的记了，多的临场再说。"

            if poison_evidence:
                "……第三条让你心中一凛。以她的手段，在酒中做手脚并非不可能。"

        "故意表现得不在意":
            $ change_stat("power", 3)
            $ change_rel("rel_queen", -10)
            $ change_stat("reputation", -4)

            player "我是艾登堡领主，不是来参加舞会的学徒。该怎么做，我自有分寸。"

            narrator "礼典官的表情冷了几分。"

            narrator "「阁下自便。但鄙人必须提醒——上一个不遵守觐见礼仪的领主，是北境的霍尔伯爵。」"

            narrator "「他向王后行礼时角度不够，被解读为傲慢。三个月后，他的领地被以叛国罪收回。」"

            narrator "「当然，这也许只是巧合。」"

            "他的话让空气冷了几度。你没有接话，但心里暗暗记住了他说的一切。"
            "奥伯特离开时没再多看你一眼。你清楚，今晚你这副态度，明天会一字不差地传进王后耳朵里。"

    narrator "礼典官收起羊皮纸，又说了一句：「对了，觐见是在后天。明天，王后安排了一场晚宴，欢迎各地来京的领主。」"

    narrator "「建议阁下出席。那是觐见前建立人脉的好机会。」"

    "礼典官走后，你叫来了艾琳娜和雷恩。"

    hide player_char_img
    show captain_img at right with dissolve

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我们有一天半的时间。觐见在后天，明晚有晚宴。"

    player "在那之前，我想了解这座城市。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "领主大人是想去逛逛？我可以安排护卫。"

    hide captain_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "带太多人太招摇。换便装，我陪您去就够了。"

    hide elena_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "那我呢？"

    hide captain_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "你留在这里看好我们的东西。顺便——"

    "她压低声音。"

    elena "把房间里那三个暗格全部堵死。昨晚我发现壁炉通风口后面有新鲜的蜡烛痕迹。"

    elena "有人一直在那里偷听。"

    hide elena_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "……我明白了。"

    "雷恩的脸色变得严肃起来。"

    hide elena_img with dissolve
    hide captain_img with dissolve

    $ hide_all_chars()
    "你换上一件朴素的灰色外套，把艾登堡的家徽藏进里衣。"

    "镜子里的你看起来像一个富裕的商人或者小贵族的管家——不起眼，但也不寒酸。"

    "艾琳娜则换了一身深蓝色的连帽长裙，遮住了她那头引人注目的银色长发。"

    "你们从贵宾馆的侧门悄悄离开，汇入王都清晨的人流中。"

    "冬日的阳光冷而清亮，空气里弥漫着烤面包和炒栗子的香气。"

    "在这一刻，你不是什么领主——只是一个第一次来到大城市的年轻人。"

    "但这种轻松只持续了片刻。你很快注意到，至少有两个人在不远处尾随着你们。"

    show elena_img at right with dissolve

    elena "发现了吗？灰衣服的那个在左边，戴帽子的在右后方。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "王后的人？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "不好说。可能是王后的密探，也可能是其他势力的眼线。王都里盯人是一门生意。"

    if knows_eagle_network:
        elena "看左边那个换位置的走法——先停，数三步，再跟。只看，不动手，谁付钱替谁看。"

        elena "这是幽卫散部传下来的手艺。七近卫散伙几百年了，这门生意一直没断过。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "你怎么懂这些？"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "莲卫的后人认得幽卫的后人。同一张桌子上散的伙，规矩都还认得。"

        elena "区别是他们卖给出价的人。我们……挑主人。"

    elena "不用管他们。我们按计划行事就好。"

    hide elena_img with dissolve

    "你们继续向前走去，融入了赫尔曼斯堡的喧嚣之中。"

    return

## ============================================================
## Part 2: 王都探索
## ============================================================

label ch4_exp_explore:

    $ play_music("audio/music/forest_ambient.ogg", fadein=2.0)
    scene bg royal_palace with dissolve
    $ set_mood("normal")

    "王都的主干道宽阔得可以并排通过六辆马车，两旁种着修剪整齐的菩提树。"

    "每隔百步就有一座喷泉或雕像，大多是历代国王的塑像——你注意到格里菲斯七世的雕像格外崭新，底座上刻着「英明仁圣」四个金字。"

    "讽刺的是，这位「英明仁圣」的国王被自己的妻子毒死了。"

    show elena_img at right with dissolve

    elena "王都分成四个区：北区是王宫和贵族宅邸，东区是大教堂和学院，南区是集市和商会，西区……"

    elena "西区是贫民区。也叫「灰区」——因为那里的天空永远是灰色的，工坊的烟囱日夜不停。"

    elena "我们的时间不多。您想先去哪里？"

    hide elena_img with dissolve

    menu:
        "去南区的集市":
            $ ch4_exp_explored_market = True
            call ch4_exp_explore_market from _call_exp_market

        "去东区的大教堂":
            $ ch4_exp_explored_cathedral = True
            call ch4_exp_explore_cathedral from _call_exp_cathedral

        "去西区的贫民区":
            $ ch4_exp_explored_slums = True
            call ch4_exp_explore_slums from _call_exp_slums

    $ hide_all_chars()
    "时间在不知不觉中流逝。"

    "日头渐高，街上的行人越来越多。你意识到你们已经在外面逛了快两个时辰。"

    show elena_img at right with dissolve

    elena "还有时间再看一个地方。趁天还没黑。"

    hide elena_img with dissolve

    $ hide_all_chars()
    menu:
        "去南区的集市" if not ch4_exp_explored_market:
            $ ch4_exp_explored_market = True
            call ch4_exp_explore_market from _call_exp_market_2

        "去东区的大教堂" if not ch4_exp_explored_cathedral:
            $ ch4_exp_explored_cathedral = True
            call ch4_exp_explore_cathedral from _call_exp_cathedral_2

        "去西区的贫民区" if not ch4_exp_explored_slums:
            $ ch4_exp_explored_slums = True
            call ch4_exp_explore_slums from _call_exp_slums_2

        "回贵宾馆休息，为晚宴做准备":
            "你决定见好就收。今天收集到的信息已经够多了。"
            $ change_stat("intrigue", 2)

    "你和艾琳娜循原路返回贵宾馆。"

    "一路上，你都在消化今天看到和听到的一切。"

    "这座城市比你想象的更复杂。表面繁华，底下到处是裂口。"

    "而你即将踏入这团乱麻的中心。"

    return

## --- 子场景：集市 ---

label ch4_exp_explore_market:

    scene bg royal_palace with dissolve

    "南区的集市是王都最热闹的地方。"

    "数百个摊位沿街排开，从东方的香料到北境的毛皮，从山地工坊的精钢到南方织工的轻纱——你能在这里找到整个大陆的货物。"

    if persistent.southern_endings_seen:
        "靠墙一个不起眼的摊子上堆着粗盐，麻袋口印着一只缠绳的铁锚。那是潮汐港的记号。南边那场火并过去这么久，它的盐倒是一路北上，摆到了王都的集市上。"

    "叫卖声此起彼伏，各种语言和口音混在一起。"

    $ play_sound("audio/sfx/crowd_murmur.ogg")

    "你随意走进一家看起来颇有规模的杂货铺。老板是个红脸膛的胖子，正在和一个顾客讨价还价。"

    if knows_root_network:
        "等秤的工夫，你的目光落在柜台那杆黄铜秤上。秤杆底端刻着一小团缠绕的树根。"
        "《六卫终录》里的那句话是真的——根卫没死。他们就在这些商会里，就在这杆秤上。"
        "你不动声色地记下了这家商号的名字。南边的商路上还有多少这样的记号，值得让艾琳娜查一查。"
        $ change_stat("intrigue", 3)

    "你假装挑选货物，耳朵却在捕捉周围的对话。"

    narrator "「……新税又加了两成。照这样下去，年底前得关掉三分之一的店铺。」"

    narrator "「嘘！小声点。上次老马抱怨税重，第二天密探就上门了。」"

    narrator "「我就纳闷了，先王在的时候可不是这样。那时候商税才一成五……」"

    narrator "「先王？那都是二十年前的事了。现在是王后的天下。」"

    "你装作不经意地问了句。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "这位兄台，最近生意怎么样？"

    $ hide_all_chars()
    narrator "胖老板警惕地看了你一眼，然后露出职业笑容。"

    narrator "「嘿，爷，您是外地来的吧？看您穿戴就知道是有身份的人。」"

    narrator "「生意嘛……还成，还成。王后治下国泰民安，我们做买卖的没什么好抱怨的。」"

    "他说最后一句话时，眼睛飞快地瞟了一下门外——你注意到门外确实站着一个不像是顾客的人。"

    menu:
        "推一袋金币过去——「告诉我你今天没说完的那部分」" if wealth >= 60:
            $ change_stat("wealth", -10)
            $ change_stat("intrigue", 5)
            $ ch4_exp_merchant_tip = True

            "你不动声色地把一袋金币放在柜台下面， 推了过去。"

            narrator "胖老板的手指捏了捏袋子的厚度， 立刻明白了你的意思。他把袋子收进围裙， 表情松了下来。"

            narrator "「贵客真是爽快人。」"

            narrator "「您是来觐见王后的吧？我说几句， 您听了就忘——上个月西区死了十几个人， 官面上是瘟疫， 实际是被灭了口。」"

            narrator "「都是打听先王遗诏的人。」"

            if true_killer_known:
                "先王遗诏——你心中一动。如果王后篡改了遗诏， 那被灭口就完全说得通了。"

            narrator "「还有——大主教马修斯最近来王都了。那老头一般不轻易出主教座堂。他来了， 肯定有大事。」"

            narrator "「再多您给再多金币， 我也不知道。这个城市深的地方， 我够不着。」"

            "你又往柜台下塞了半袋金币。「这袋不为打听。」你说。胖老板把它收得比第一袋更快——他知道这是封口的价钱。"

            $ change_stat("wealth", -5)

        "给他看艾登堡的家徽，表明身份":
            $ change_stat("power", 3)
            $ change_stat("reputation", 3)
            $ change_stat("intrigue", -8)
            $ ch4_exp_merchant_tip = True

            "你不动声色地翻出里衣上的金鹰徽章，让他瞥了一眼。"

            narrator "胖老板的眼睛猛地瞪大了一瞬，然后迅速恢复了镇定。"

            narrator "「原来是……咳，贵客驾到。里面请，里面请。」"

            "他把你引进后堂，用一种完全不同的语气说话。"

            narrator "「领主大人恕罪。外面耳目太多，不得不装。」"

            narrator "「您是来觐见王后的吧？给您提个醒——最近王都不太平。」"

            narrator "「上个月，西区死了十几个人，官面上说是瘟疫，但我听说是被灭了口。」"

            narrator "「都是些打听先王遗诏的人。」"

            if true_killer_known:
                "先王遗诏——你心中一动。如果王后篡改了遗诏，那被灭口就完全说得通了。"

            narrator "「还有——大主教马修斯最近来王都了。那老头一般不轻易离开主教座堂。他来了，肯定有大事。」"

            "你默默记下了这些信息。"
            narrator "「对了，领主大人——」胖老板压低声音，「您方才亮徽章那一下，门口站着的那位，怕是看了个正着。这集市里，王后的眼睛不少。」"
            "你心里一沉。为了换他这几句话，你把自己的脸露在了不该露的地方。"

        "不暴露身份，继续旁敲侧击":
            $ change_stat("intrigue", 5)
            $ ch4_exp_merchant_tip = True

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我是北边来做皮草生意的。听说王都机会多。"

            $ hide_all_chars()
            narrator "「机会是多，就是税也多。不过只要打点好关系，还是能赚的。」"

            narrator "「对了，爷，您要是做大买卖，建议去拜拜大教堂。不是求神——是求人。」"

            narrator "「教堂的总管事和税务官是连襟。只要教堂那边说一句话，税能少两成。」"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "教会的手伸得够长的。"

            $ hide_all_chars()
            narrator "「在王都，教会的手比王后的手还长。您可别说是我说的。」"

            "你笑着点点头，默默记下了这条信息。"

        "买些东西就走，不引起注意":
            $ change_stat("intrigue", 2)

            "你买了一小袋东方香料和一条丝绸手帕——作为觐见的备用礼物。"

            $ change_stat("wealth", -2)

            "胖老板热情地送你到门口，但你能感觉到他松了一口气——少一个问问题的客人，就少一分风险。"

    "离开杂货铺后，你继续在集市里转悠。"

    "你注意到一个有趣的现象——集市的核心区域繁华热闹，但越往边缘走，空铺子就越多。"

    "有些店铺的招牌还在，门却被钉死了，窗户上贴着「充公」的封条。"

    hide player_char_img
    show elena_img at right with dissolve

    elena "这些都是交不起税被查封的。三年前还没有这么多空铺子。"

    elena "王后的税制像绞索——每年紧一圈，直到勒死为止。"

    hide elena_img with dissolve

    $ hide_all_chars()
    "你沉默地走过一排又一排空荡荡的店面。"

    return

## --- 子场景：大教堂 ---

label ch4_exp_explore_cathedral:

    scene bg royal_palace with dissolve

    "东区的大教堂是王都最宏伟的建筑之一——仅次于王宫本身。"

    "双塔高耸入云，白色大理石的墙壁上雕刻着无数圣徒的面孔。"

    "正门上方是一面巨大的彩色玻璃窗，描绘着圣光降临的场景——金色的光芒从天而降，照亮了跪拜的众生。"

    "你走进教堂，空气中弥漫着乳香和蜡烛的气味。"

    $ play_sound("audio/sfx/bell_toll.ogg")

    "穹顶高得令人眩晕，阳光透过彩窗洒下五彩斑斓的光斑。"

    "教堂里很安静。几十个信徒跪在长椅上祈祷，偶尔传来轻微的啜泣声。"

    "你注意到，这些信徒大多衣着朴素——他们不是贵族，而是普通的百姓。"

    show elena_img at right with dissolve

    elena "大教堂是王都唯一一个免税的地方。穷人来这里，至少能得到一碗粥和一个安全的角落。"

    elena "教会用施舍换取信仰。在王都，这门生意比任何商铺都赚。"

    hide elena_img with dissolve

    $ hide_all_chars()
    "你沿着中殿走向祭坛。半路上，一个穿着白色法袍的年轻神职人员拦住了你。"

    narrator "「先生，您是来祈祷的吗？还是来捐献的？」"

    "他的语气恭敬而职业——显然能从你的衣着判断出你不是普通的信徒。"

    menu:
        "捐一笔钱，借机打听消息":
            $ change_stat("faith", 5)
            $ change_stat("wealth", -3)
            $ change_rel("rel_bishop", 8)
            $ ch4_exp_cathedral_prayer = True

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我想为家人点一盏长明灯。"

            narrator "「当然。长明灯分三等——金灯一百银币，银灯五十，铜灯二十。」"

            player "金灯。"

            $ hide_all_chars()
            "你掏出钱袋。年轻神职人员的态度立刻殷勤了三分。"
            "一百银币的金灯不是小数目。从这一刻起，你在这座教堂里就是被记住的客人，不是被盯着的生人。"

            narrator "「请跟我来。我带您去圣光厅——那里是点长明灯的专用殿堂。」"

            "他领你走过一条侧廊，边走边攀谈。"

            narrator "「先生看起来不像本地人。最近王都来了不少外地贵客——大概都是为了觐见吧。」"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "听说主教马修斯也来了？"

            $ hide_all_chars()
            "年轻神职人员的脚步顿了一下。"

            narrator "「……主教大人确实来了。昨天到的。他住在教堂后面的主教府。」"

            narrator "「听说是有要事和王后商议。具体是什么——我们这些小人物就不知道了。」"

            "他的声音压得很低，显然这个话题让他紧张。"

            "你点了灯，在圣像前站了片刻。光柔和而温暖，落在脸上。"

            if father_letters_found:
                "你想起了父亲信中的话——「不要信任教会的高层，他们的虔诚只是一张面具。」"
                "大主教费雷恩……他在先王遗诏的篡改中扮演了什么角色？"

        "在教堂中祈祷，感受氛围" if faith >= 45:
            $ change_stat("faith", 8)
            $ change_rel("rel_bishop", 5)
            $ ch4_exp_cathedral_prayer = True

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我来祈祷。"

            $ hide_all_chars()
            "你走到一排长椅前跪下，双手合十。"

            "你不确定自己信不信神。但在这个充满阴谋和危险的地方，向某种更高的存在祈求庇护，至少能让你心安一些。"

            "你闭上眼睛，在心中默默祈祷。"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "（如果有神在听……请指引我。让我找到真相，保护我在乎的人。）"

            $ hide_all_chars()
            "不知过了多久，你睁开眼睛。彩窗的光在地上慢慢挪动。"

            "你感到一种久违的平静。"

            "起身时，你注意到旁边跪着一个老妇人。她抬起头，用浑浊的眼睛看着你。"

            narrator "「年轻人，你的眼睛里有很重的杀气。」"

            narrator "「但你的心还是善的。老身为你祈过祷了——愿圣光照亮你前方的路。」"

            "你微微点头致谢。不知为何，她的话让你心中微微一暖。"

        "不进教堂，在外面观察":
            $ change_stat("intrigue", 5)
            $ change_rel("rel_bishop", -10)

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我在外面看看就好。"

            $ hide_all_chars()
            "你没有进入教堂，而是绕着建筑走了一圈。"

            "教堂后面是一片封闭的庭院——主教府。高墙上拉着铁丝网，门口有教会武装守卫把守。"

            "你注意到，主教府的守卫装备精良——他们穿的不是教会传统的白色盔甲，而是黑色的轻甲，腰间挂着短剑和袖弩。"
            "你绕墙的时候，一名灰袍卫一直没把视线从你身上移开。等你走远，他低声对身边的人说了句什么。"

            hide player_char_img
            show elena_img at right with dissolve

            elena "那是教会的「灰袍卫」——原先是已故费雷恩大主教创建的私人武装，现在归教会直辖。"

            elena "别看只有几十人，每一个都是从教会孤儿院中精挑细选、从小训练的精锐。"

            elena "忠诚度绝对没问题——因为他们的整个世界就是教会。"
            elena "而且他们记性好得很。你今天在墙根下转的这一圈，主教府明天就会知道。"

            hide elena_img with dissolve

            $ hide_all_chars()
            "你默默记下了这些细节。教会在王都的势力比你预想的要强大得多——他们不仅有信仰，还有刀。"

    "离开大教堂区域时，你回头看了一眼那座宏伟的建筑。"

    "阳光下它庄严圣洁。可你已经知道，那些彩窗后面的人，跟王宫里的没两样。"

    return

## --- 子场景：贫民区 ---

label ch4_exp_explore_slums:

    scene bg royal_palace with dissolve
    $ set_mood("dark")

    "西区的贫民区像是另一个世界。"

    "从主干道向西拐进一条小巷之后，一切都变了——宽敞的石板路变成了泥泞的小径，整洁的石楼变成了摇摇欲坠的棚屋。"

    "空气中弥漫着腐烂和烟尘的味道。排水沟里流淌着黑色的污水，苍蝇嗡嗡作响。"

    "街上的人大多面黄肌瘦、衣衫褴褛，瘦得脱了形。"

    "有些人蹲在墙根下发呆，有些人在翻垃圾堆找吃的，有些人用空洞的眼神看着你——然后迅速移开目光。"

    show elena_img at right with dissolve

    elena "三年前这里还没这么糟。那时候至少还有工坊在开工。"

    elena "后来王后加了匠人税，大半的铁匠铺和织坊都关了。工人失去了生计，就变成了……这样。"

    hide elena_img with dissolve

    $ hide_all_chars()
    "你走过一个拐角，看到一群孩子围在一个破桶边，争抢着什么。"

    "走近一看——他们在抢一块发霉的面包。"

    "你的胃微微抽搐了一下。这些孩子中最大的不超过十岁，最小的大概只有四五岁。"

    "他们看到你的衣着后，有的后退，有的伸出脏兮兮的手。"

    narrator "「大人……给口吃的吧……两天没吃了……」"

    menu:
        "给他们钱和食物":
            $ change_stat("loyalty", 5)
            $ change_stat("wealth", -3)
            $ ch4_exp_slum_info = True

            "你掏出几枚银币，又把腰间的干粮袋解下来。"

            "孩子们一拥而上，但没有哄抢——一个稍大的女孩站出来，把食物一份一份地分给每个人。"

            "她最后才给自己留了一小块，然后向你鞠了一躬。"

            narrator "「谢谢大人。您……不像这里的那些贵人。」"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你们的父母呢？"

            $ hide_all_chars()
            narrator "女孩的眼神黯了一下。「死了。病死的、饿死的、被抓走的……各种死法。」"

            narrator "「上个月，灰区死了好多人。官面上说是疫病。但我看见了——是穿黑衣的人半夜来的。」"

            narrator "「他们把人从家里拖出去，再也没回来。」"

            "你的血管里流过一阵寒意。"

            hide player_char_img
            show elena_img at right with dissolve

            elena "……和这一路打听到的对上了。有人在灭口。"

            hide elena_img with dissolve

            "你又给了女孩几枚银币。"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "如果有人问起——你今天没见过我们。"

            narrator "女孩把银币藏进破鞋子里，认真地点了点头。「大人放心。灰区的人都知道——看见什么都没看见。」"

            if deep_street_justice == "help":
                $ hide_all_chars()
                "你正要离开，巷子的另一头走出一个十六七岁的少年。"

                "瘦，鼻子上有一道旧疤——像是小时候被人打断过。"

                "他看着你，沉默了几秒，然后开口——"

                narrator "「您是……艾登堡的[player_name]大人？」"

                "你愣了一下。然后想起来——很多年前，在另一座城的另一条小巷里，你给过一个被欺负的男孩自己仅剩的零花钱，告诉他可以去圣·尤里安修道院的后门找你。"

                "你后来再也没见过他。"

                narrator "「我去过修道院找您。您已经走了。」"

                narrator "「但您给的那些钱，让我撑过了那个冬天。」"

                "他从怀里掏出一枚很小的旧铜币，摊开手心让你看一眼——你认得出，那是你当年给他的钱里最不起眼的一枚。"

                narrator "「这枚我留着。您以后若有用得着我的地方——来贫民区找「乌鸦」。」"

                "他转身没入巷子深处，没有再回头。"

                "你看着他的背影。当年那个蜷缩在墙角的孩子活了下来。还在照顾比他更小的孩子。"

                "心里某处沉了一下——又轻了一下。"

        "观察但不暴露自己的财力":
            $ change_stat("intrigue", 5)
            $ ch4_exp_slum_info = True

            $ hide_all_chars()
            "你没有掏钱——在贫民区露财是很危险的事。但你把这一切都看在了眼里。"

            "你注意到墙壁上有一些用炭笔画的符号——一朵倒挂的百合花。"

            show elena_img at right with dissolve

            elena "……暗百合的标记。"

            if dark_lily_joined:
                elena "看来暗百合在灰区也有布局。这倒不意外——贫民区历来是秘密组织的温床。"
            elif dark_lily_destroyed:
                elena "那是暗百合的旧标记。看来他们被铲除之后，余党还没来得及清理痕迹。"
            else:
                elena "暗百合在贫民区招募人手。穷人是最好的间谍——因为没有人会注意他们。"

            hide elena_img with dissolve

            $ hide_all_chars()
            "你还注意到，灰区的街角站着一些纹着特殊纹身的壮汉——他们不像乞丐，更像是某种地下秩序的维护者。"

            "灰区有灰区的规矩。"

        "离开这里，这不是你现在该关心的":
            $ change_stat("power", 3)
            $ change_rel("rel_elena", -2)

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我们走。这里的问题不是一天能解决的。"

            show elena_img at right with dissolve

            elena "……也是。"

            "她的语气里有一丝失望，但你选择忽略了它。"

            elena "不过，领主大人——"

            elena "您今天在这条巷子里看到的，明天在觐见厅里，没人会说给您听。"

            hide elena_img with dissolve

            "你没有接话。但那些孩子的眼神，在你离开之后还萦绕了很久。"

    hide player_char_img with dissolve
    return

## ============================================================
## Part 3: 宫廷交际（觐见前夜晚宴）
## ============================================================

label ch4_exp_court_social:

    $ play_music("audio/music/great_hall.ogg", fadein=2.0)
    scene bg royal_palace with dissolve
    $ set_mood("normal")

    "晚宴设在王宫东翼的玫瑰厅——一个能容纳两百人的巨大宴会厅。"

    "水晶吊灯从穹顶垂下，烛光把整个大厅染成了温暖的金色。"

    "长桌上铺着绣花白布，摆满了银质餐具和鲜花。侍从穿梭其间，端着盛满葡萄酒的银壶。"

    $ play_sound("audio/sfx/crowd_murmur.ogg")

    "你穿着从艾登堡带来的最好的礼服——深蓝丝绒，银线金鹰——走进了这片光怪陆离的世界。"

    "大厅里已经聚集了五六十人。男人们身着华服，女人们珠光宝气。"

    "低声的交谈、银铃般的笑声、酒杯碰撞的叮当声，交织成一首属于上流社会的夜曲。"

    show elena_img at right with dissolve

    elena "（低声）我会在大厅边上。有事用眼神示意我。"

    elena "注意——那边穿绿衣服的是莱因哈特大臣，王后的心腹，掌管王都税务和情报。"

    if steinfurt_met:
        elena "另一边——施泰因伯爵夫人也在。上次会议您见过了。记住，她和王后不和。"
    else:
        elena "另一边坐着的老妇人是施泰因伯爵夫人，东三省最大的领主。她和王后不和。"

    elena "还有角落里那个独自喝酒的年轻人——我不认识，但他一直在观察所有人。"

    hide elena_img with dissolve

    $ hide_all_chars()
    "你端起一杯酒，开始在人群中游走。"

    "宴会厅是另一种战场，一样要命。"

    ## --- 莱因哈特大臣 ---

    "你首先注意到的是莱因哈特大臣。"

    "他大约四十五岁，身材修长，穿着一件深绿色的锦缎外套，上面用金线绣着麦穗和天平的图案——象征着财政和法律。"

    "他的脸很窄，像一把刀的侧面。眼睛是浅灰色的，像两块磨光的钢片，锐利而冰冷。"

    "此刻他正和几个贵族交谈，嘴角挂着一个恰到好处的微笑——既不显得热情，也不显得傲慢。"

    "那笑容是练出来的，分寸拿捏得一丝不差，反而不像真的。"

    menu:
        "主动上前自我介绍":
            $ change_stat("reputation", 5)
            $ change_stat("intrigue", 3)
            $ change_rel("rel_queen", 4)
            $ ch4_exp_met_reinhart = True

            "你端着酒杯走了过去。"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "莱因哈特大臣阁下，久仰大名。鄙人艾登堡领主[player_name]。"

            $ hide_all_chars()
            narrator "莱因哈特转过身来，灰色的眼睛在你脸上停留了两秒——就像在核对一份文件。"

            narrator "「啊，年轻的艾登堡领主。我读过关于您的报告。」"

            narrator "「在边境问题上处理得相当漂亮。比您父亲当年……有过之而无不及。」"

            "他提到你父亲时，语气轻描淡写，像在说一道已经端走的菜。但你捕捉到了他话中的试探。"
            "莱因哈特记下了你的名字。他记下的东西，王后迟早会看到——你主动走到了王后耳目的跟前。"

            menu:
                "感谢他的称赞":
                    $ change_stat("reputation", 3)
                    $ change_rel("rel_queen", 6)
                    $ change_rel("rel_stein", -5)

                    $ hide_all_chars("player_char_img")
                    show player_char_img at left with dissolve
                    player "大臣过奖了。初来乍到，还请多多指教。"

                    $ hide_all_chars()
                    narrator "「客气了。在王都，「指教」是不值钱的。但如果您需要「建议」——我的门总是开着的。」"

                    narrator "他递过一张烫金的名帖。「有空来喝茶。」"

                    "你收下名帖。这张纸比寻常的厚，也沉。"
                    narrator "大厅另一侧，施泰因伯爵夫人的目光扫过你和莱因哈特之间那张名帖，停了一瞬。在她那一派人眼里，你刚刚站了队。"

                "提起父亲，观察他的反应":
                    $ change_stat("intrigue", 5)
                    $ change_stat("reputation", -6)
                    $ change_rel("rel_queen", -4)

                    $ hide_all_chars("player_char_img")
                    show player_char_img at left with dissolve
                    player "说到家父……他生前对王都的政局也多有关注。不知大臣与他可曾有过交集？"

                    $ hide_all_chars()
                    narrator "莱因哈特的微笑凝固了不到一秒——如果你不是全神贯注地盯着他，根本不会注意到。"

                    narrator "「令尊……是位可敬的人。他的去世是王国的损失。」"

                    narrator "「不过——在晚宴上聊这些未免扫兴。我们改天找个安静的地方细谈？」"

                    "他在转移话题。你笑着点了点头，但心里记下了他那一瞬间的表情变化。"
                    "邻桌两位贵族交换了一个眼神。在这种场合提一位故去领主的旧账，不是聪明人会做的事——这话明天就会传开。"

                    "他对你父亲的事知道多少？——也许比他愿意表现出来的多得多。"
                    narrator "莱因哈特会把今晚写进给王后的报告。你提的这个名字，本不该由你先开口。"

                "客套几句后找理由离开":
                    $ change_stat("intrigue", 2)
                    $ change_stat("reputation", -2)

                    $ hide_all_chars("player_char_img")
                    show player_char_img at left with dissolve
                    player "多谢。初到王都，想多和各位前辈认识认识。先失陪了。"

                    $ hide_all_chars()
                    narrator "「请便。」"

                    "他目送你离开，灰色的眼睛在你背后停留了片刻——你能感觉到那道目光的重量。"
                    narrator "他不会主动来找你了。你在王都最有用的一双耳朵跟前，什么也没留下。"

        "先观察，不急着接触":
            $ change_stat("intrigue", 5)
            $ ch4_exp_met_reinhart = True

            "你没有急着上前，而是在不远处驻足，假装品酒，耳朵却在仔细捕捉他的对话。"

            narrator "「……新税的征收进度如何？」"

            narrator "「西区还有些抵触，不过不成气候。灰区的工匠已经基本清理干净了。」"

            narrator "「王后对明年的战备预算有什么看法？」"

            narrator "「战备？哈——王后陛下的视野不止于此。但这些不是在宴会上谈的话。」"

            "战备预算？这引起了你的注意。王后在为什么战争做准备？"
            "你多知道了一件事，却也错过了让莱因哈特记住你的机会——今晚他不会主动来认你了。"

        "不理会他，去找施泰因伯爵夫人":
            $ change_stat("intrigue", 3)
            "你决定把莱因哈特留到以后再打交道。此刻有更值得接触的目标。"

    ## --- 施泰因伯爵夫人 ---

    "你转向大厅的另一侧，向施泰因伯爵夫人走去。"

    "伯爵夫人大约六十岁，但看起来比实际年龄年轻十岁。"

    "她穿着一件深红色的丝绒长裙，脖子上戴着一条夸张的红宝石项链——那些宝石大得像鸽子蛋，在灯光下闪烁着血一样的红光。"

    "她的头发灰白相间，向后梳成一个严厉的发髻，露出一张轮廓分明的面孔——高颧骨、尖下巴、一双总是微微眯着的眼睛。"

    "她看起来像一只年迈但仍然危险的鹰。"

    $ ch4_exp_met_countess = True

    "你走近时，她正在和一个年轻的女伴低声交谈。看到你，她微微扬起下巴。"

    narrator "施泰因伯爵夫人用锐利的目光上下打量着你。"

    if steinfurt_met:
        narrator "「艾登堡的小领主，又见面了。」"

        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "伯爵夫人别来无恙。"

        $ hide_all_chars()
        narrator "「无恙？在这种场合能无恙的人，要么是蠢货，要么是狠角色。」"

        narrator "「上次会议匆匆一面，没来得及细聊。你父亲——很有城府的男人，但不够狠。」"
    else:
        narrator "「你就是新任的艾登堡领主？比我想象的年轻。」"

        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "伯爵夫人眼力过人。"

        $ hide_all_chars()
        narrator "「在我这个年纪，看人看得多了。」"

        narrator "「你父亲我见过几面。很有城府的男人——但不够狠。」"

    narrator "「在这个世道，不够狠的人活不长。他就是个例子。」"

    "她的话像一根细针，精准地扎在你的神经上。但你保持了平静。"

    menu:
        "反问她——「您见过他几面，怎么这么了解我父亲？」" if intrigue >= 70:
            $ change_stat("intrigue", 5)
            $ change_rel("rel_queen", -8)
            $ change_rel("rel_stein", 8)

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "您说见过他几面。但「有城府」「不够狠」——这两句不是几面之缘能下的判断。"
            player "您跟我父亲， 走得比您今晚说的近。"

            $ hide_all_chars()
            narrator "伯爵夫人的酒杯停在嘴边， 半秒。然后她笑了——这次的笑意到了眼底。"

            narrator "「……年轻人， 你这一手不该只属于二十几岁的人。」"

            narrator "「你父亲跟我有些旧账， 是的。算不上朋友， 但也不是敌人。他来王都几次， 我们密谈过——你说对了。」"

            "她把酒杯放下， 看你的眼神变了。不是因为问的人聪明——是问的人精确到她无法回避。"

            narrator "「年轻人， 如果你在王都需要一个……不那么偏向王后的朋友， 我的府邸在北区玫瑰街尽头。」"
            "几步之外，那位绿衣大臣的目光在你和伯爵夫人之间扫过一遍，又移开了。今晚谁跟谁多说了两句话，明天都会摆到王后案头。"

        "顺着她的话聊，拉近关系":
            $ change_stat("intrigue", 5)
            $ change_rel("rel_queen", -8)
            $ change_rel("rel_stein", 5)

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "所以伯爵夫人一定是够狠的那种人。"

            $ hide_all_chars()
            narrator "伯爵夫人哼了一声，算是认了——那是你今晚见过的第一个真实的反应。"

            narrator "「聪明的孩子。你父亲要是有你一半的锋利，也不至于——」"

            "她及时收住了嘴，但你已经听懂了她没说完的话。"

            narrator "「算了。过去的事就让它过去。」"

            narrator "「我倒想知道——你来王都，除了觐见王后，还有什么打算？」"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "学习。观察。了解这个国家的真实状况。"

            $ hide_all_chars()
            narrator "「好回答。不露底牌，也不装蒜。」"

            narrator "「年轻人，如果你在王都需要一个……不那么偏向王后的朋友，我的府邸在北区玫瑰街尽头。」"

            narrator "「红门的那栋。记住了吗？」"

            "你点了点头。这是一个明确的橄榄枝——施泰因伯爵夫人在试探你，是否愿意站到王后的对立面。"

        "不动声色地为父亲说话":
            $ change_stat("reputation", 3)
            $ change_rel("rel_stein", 3)

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "家父或许不够狠。但他是一个正直的人。"

            $ hide_all_chars()
            narrator "「正直？」伯爵夫人哼了一声，「在这种地方，正直是最大的奢侈品。」"

            narrator "「不过——我尊重正直的人。尤其是在这个满口谎言的宫廷里。」"

            narrator "她的语气软了一些，端着酒杯的手指松了松。"

        "保持距离，礼貌客套":
            $ change_stat("intrigue", 2)

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "伯爵夫人过誉了。在下初来乍到，不敢妄言。"

            $ hide_all_chars()
            narrator "「又一个谨小慎微的年轻人。」她摇了摇头，「也罢。这种地方，小心总是没错的。」"

            "她转过身去，继续和女伴交谈，像是已经对你失去了兴趣。"

    ## --- 宴会中的传闻 ---

    "宴会渐入佳境。酒过三巡，人们的防备松懈了一些，声音也渐渐大了起来。"

    "你在人群里慢慢走，把各处的对话都听进耳朵。"

    "不同的桌子旁，流传着不同的传闻。"

    narrator "「……你们听说了吗？王子已经两个月没在公开场合露面了。」"

    narrator "「说是在秋水宫「静养」。但谁信呢？」"

    narrator "「听说是和王后吵了一架。王子想要亲政，王后不肯交权。」"

    narrator "「嘘——这种话也敢说？小心你的脑袋。」"

    $ ch4_exp_heard_prince_rumor = True

    "你假装不经意地靠近那桌。"

    narrator "「秋水宫的守卫最近换了一批。以前是王室卫队，现在是莱因哈特的人。」"

    narrator "「也就是说——是王后的人。」"

    if not prince_imprisoned_known:
        narrator "「王子现在是被软禁了。明眼人都看得出来。」"

        narrator "「但没人敢说。上一个公开替王子说话的贵族……现在还在地牢里关着呢。」"

        "你默默记下了这些信息。弗雷德里克王子——先王唯一的儿子，二十二岁。"

        "如果先王的遗诏是真的，那王位本就应该传给他。而王后一直抓着权力不放，甚至不惜软禁自己的亲生儿子。"

        $ prince_imprisoned_known = True
    else:
        narrator "「王子的事，你们都听说了吧？秋水宫的守卫越来越多了。」"

        "这些传言和你已经知道的一致——王子确实被软禁了。"

    "这个女人的权欲，远比你想象的可怕。"

    "宴会持续到深夜。你微醺但清醒地离开了玫瑰厅。"

    "走廊上的灯火已经暗了一半。侍从们无声地收拾着残局。"

    "你回头望了一眼灯火通明的宴会厅，笑声还没停，谁也看不出谁是真心。"

    $ ch4_exp_court_impression = "complex"

    hide player_char_img with dissolve
    return

## ============================================================
## Part 4: 暗中调查（晚宴之后的夜间行动）
## ============================================================

label ch4_exp_investigation:

    $ play_music("audio/music/night_mystery.ogg", fadein=2.0)
    scene bg royal_palace with dissolve
    $ set_mood("dark")

    "回到贵宾馆，已经接近子时。"

    "雷恩在门口等着你，脸上的表情很严肃。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "领主大人，您不在的时候出了些事。"

    captain "下午我清理暗格的时候，在壁炉通风口发现了这个。"

    "他递给你一个小小的金属圆筒——大约拇指粗细，上面刻着精细的花纹。"

    captain "里面是一张纸条。已经被取出来了——但管壁上还残留着墨迹。"

    captain "我把残迹拓了下来。"

    hide captain_img with dissolve

    $ hide_all_chars()
    "你接过拓本。上面的字迹模糊但勉强可读——"

    narrator "「……三号目标已到。密切监视。如有异动，立即向暗焰汇报。——伏笔」"

    "三号目标——你心中一沉。你就是三号目标。"

    if darkflame_known:
        "暗焰——暗百合的叛徒分支，与王后有关联的那一派。"
    else:
        "暗焰——你记住了这个名字。看来有某个势力在暗中监视你的一举一动。"
        $ darkflame_known = True

    show elena_img at right with dissolve

    elena "看来我们的到来，早就在对方的预料之中。"

    elena "这个「伏笔」应该是暗焰在贵宾馆安插的暗哨。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "能查出是谁吗？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "贵宾馆的侍从一共七人。我会在今晚逐一排查。"

    elena "但更重要的是——这说明暗焰在王都的势力比我们想的要深。"

    if dark_lily_joined:
        elena "我需要和影卫在王都的联络人接头。他们应该有暗焰在王都的活动情报。"
    else:
        elena "我们没有暗百合的人脉支持。调查起来会困难得多。但也不是完全没有办法。"

    hide elena_img with dissolve

    $ hide_all_chars()
    "你在房间里来回踱步，思考着下一步的行动。"

    "晚宴上获得的信息、白天在城里的见闻、现在这张纸条——所有的碎片都在指向一个方向。"

    "连秋水宫的守卫都换成了王后的人。你在这座城里的一举一动，她恐怕都看得见。"

    menu:
        "夜探王宫图书馆，寻找遗诏线索" if not testament_original_obtained:
            $ change_stat("intrigue", 8)
            $ change_stat("courage", -10)
            call ch4_exp_inv_library from _call_exp_inv_lib

        "夜探王宫图书馆，查阅伪遗诏相关档案" if testament_original_obtained:
            $ change_stat("intrigue", 8)
            $ change_stat("courage", -10)
            call ch4_exp_inv_library from _call_exp_inv_lib2

        "在贵宾馆附近偷听，看看有没有人在监视":
            $ change_stat("intrigue", 5)
            call ch4_exp_inv_eavesdrop from _call_exp_inv_eaves

        "联络暗百合在王都的接头人" if dark_lily_joined:
            $ change_stat("intrigue", 7)
            call ch4_exp_inv_lily_contact from _call_exp_inv_lily

        "独自分析手头的线索" if not dark_lily_joined:
            $ change_stat("intrigue", 5)
            call ch4_exp_inv_solo from _call_exp_inv_solo

    "夜色渐深。行动结束后，你回到贵宾馆的房间。"

    "窗外的王都沉入了黑暗之中，只有零星的灯火在远处闪烁。"

    "你把今夜收集到的所有信息摊开在桌面上，用蜡烛的微光一一审视。"

    $ ch4_exp_preparation_level += 1

    if ch4_exp_library_clue:
        "图书馆的发现尤其令你震惊——先王驾崩前夕的宫廷记录中，有一整段被人刻意涂抹。"
        "涂抹的痕迹很新，不超过三年。有人在逐条抹掉关于那段历史的记载。"

    if ch4_exp_overheard_plot:
        "你偷听到的密谈更加令人不安——有人在王都秘密集结武装力量，规模不小。"
        "是王后在防备什么？还是另有势力在暗中布局？"

    if ch4_exp_lily_contact:
        "暗百合的情报证实了你最坏的猜测——暗焰不仅渗透了贵宾馆，还渗透了王宫的守卫队伍。"
        "你在这座城市里的一举一动，都有可能被暗焰汇报给王后。"

    "线索你已经攒了不少，可最要紧的那几条还没着落。"

    "而明天的觐见，也许正是找到它们的机会。"

    return

## --- 子场景：夜探图书馆 ---

label ch4_exp_inv_library:

    "夜半时分，你披上一件深色的斗篷，从贵宾馆的侧门溜了出去。"

    "王宫图书馆位于王宫东翼的一座独立塔楼中。据说收藏了建国四百年来的所有重要文献。"

    show elena_img at right with dissolve

    elena "我替您探过了。图书馆夜间只有两个守卫。换岗是在丑时——也就是再过半个时辰。"

    elena "换岗的间隙大约有五分钟。够您进去了。但出来就得随机应变。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你不一起去？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "我在外面替您望风。如果有意外，我会扔一颗石子击窗——听到声音就立刻藏起来。"

    hide elena_img with dissolve

    $ hide_all_chars()
    "你在图书馆对面的暗巷中等了半个时辰。"

    "终于，你看到两个守卫交接班。趁着交接的间隙，你贴着墙根快速移动，从一扇没锁的侧窗翻了进去。"

    "图书馆内部漆黑一片。你点燃一根细蜡烛，用手掌遮住大部分光芒，只留一线微光。"

    "书架从地面一直延伸到天花板，像一面面纸做的墙壁。灰尘在微光中飘浮，空气中有一股古老羊皮纸的霉味。"

    "你需要快速找到目标——先王驾崩前后的宫廷记录。"

    menu:
        "直奔编年史区域，查阅先王驾崩记录":
            $ change_stat("intrigue", 5)
            $ ch4_exp_library_clue = True

            "你根据书架上的分类标签快速定位——「王室编年史·格里菲斯七世卷」。"

            "厚厚的羊皮卷被你从架上抽出。你翻到先王驾崩的那一年——"

            "大部分内容是例行公事的记录：朝会、法令、军事调动。但你注意到了几处异常——"

            "先王驾崩前三个月的记录中，有一段被黑色墨水涂抹得面目全非。"

            "你把蜡烛凑近，试图透过涂抹看到下面的原文。隐约能辨认出几个字——"

            narrator "「……遗诏……委托……艾登堡……摄政……」"

            "你的心跳骤然加速。遗诏、艾登堡、摄政——这三个词放在一起只有一个含义。"

            if father_was_regent_known:
                "这证实了你之前的猜测——先王确实留下了遗诏，指定父亲为摄政者。而记载被人刻意抹去了。"
            else:
                "先王确实留下了遗诏，指定你的父亲为摄政者。而这段记载被人刻意抹去了。"
                $ father_was_regent_known = True

            if not testament_forged_known:
                "遗诏被篡改了——有人不想让这个真相浮出水面。"
                $ testament_forged_known = True

            "你迅速在脑海中记下了卷册的编号和被涂改的页码。"

            if father_letters_found:
                "这和父亲信中的暗示完全吻合——他当年就已经知道了。"

        "寻找关于暮色之露的记载":
            $ change_stat("intrigue", 5)
            $ ch4_exp_library_clue = True

            "你转向药典和毒物学的书架——如果暮色之露是被用来毒杀先王的工具，图书馆里应该有相关记载。"

            "你翻了好几本厚重的药典，终于在一本名为《论王室御用毒物之防范》的古书中找到了相关内容。"

            narrator "「暮色之露：一种慢性毒药，从暮色兰花的花蕊中提取。无色无味，溶于酒水。」"

            narrator "「中毒者初期无症状，三至六个月后出现体力衰退、面色灰暗、记忆混乱。」"

            narrator "「致死周期约一年。死后症状与自然衰老极为相似，难以辨别。」"

            narrator "「解毒方法：无。一旦中毒超过三个月，不可逆转。」"

            "你的手微微发抖。这段描述和先王生前最后一年的状况完全吻合——体力衰退、面色灰暗、记忆混乱……"

            if father_poisoned_known:
                "你早已知道——父亲也是被同样的毒药害死的。这本古书只是再一次证实了那个残酷的事实。"
            else:
                "更可怕的是——你父亲死前也出现了同样的症状。"
                $ father_poisoned_known = True

            if poison_evidence:
                "之前你已经找到了毒物的物证。现在又有了文献佐证。两条证据链正在合拢。"

        "翻找有关暗百合历史的记载":
            $ change_stat("intrigue", 5)

            "你对暗百合的历史一直只有口口相传的了解。也许官方文献里有更详细的记录。"

            "你在「秘密组织卷」中找到了一份被标记为「已封存」的文档——但封印已经被拆开过了。"

            narrator "「暗百合始末录（节选）：」"

            narrator "「暗百合创建于格里菲斯一世时期，由国王贴身近卫「莲卫」发展而来。」"

            narrator "「初期为国王的私人情报机构，后逐渐独立运作。」"

            narrator "「一百年前分裂为三支：影卫（正统派）、铁刺（激进派）、暗焰（——此处被撕去——）」"

            "关于暗焰的记载被撕掉了。有人不想让你——或任何人——知道暗焰的真实来历。"

            "你把书放回原位，心中又多了一个疑团。"

    "一声轻响——窗户上传来石子击打玻璃的声音。"

    "那是艾琳娜的暗号——有人来了。"

    "你迅速吹灭蜡烛，摸黑躲到了书架后面。"

    "门口传来钥匙转动的声音。一束灯光扫过图书馆——"

    narrator "「……谁在这里？」"

    "守卫的脚步声在书架间回荡。灯光在你藏身的书架前晃了一下——你屏住呼吸，一动不动。"

    "过了漫长的一分钟，脚步声渐渐远去。"

    narrator "「大概是老鼠吧。这地方年久失修……」"

    "你等守卫锁门离开后，从一扇高窗翻了出去，沿着塔楼外壁攀下。"

    "艾琳娜在下面接住了你。"

    hide player_char_img
    show elena_img at right with dissolve

    elena "收获如何？"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "值得。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "那就好。走，回去。这个时间街上再被人看到就说不清了。"

    hide elena_img with dissolve

    return

## --- 子场景：偷听 ---

label ch4_exp_inv_eavesdrop:

    "你没有冒险去图书馆，而是选择了一种更稳妥的方式——偷听。"

    "贵宾馆旁边是一座小型的联络站，白天你注意到有不少穿黑衣的人进进出出。"

    "艾琳娜告诉你，那是王都密探的一个据点。"

    show elena_img at right with dissolve

    elena "密探们习惯在夜间开碰头会。如果我们能找到一个合适的位置……"

    hide elena_img with dissolve

    $ hide_all_chars()
    "你和艾琳娜悄悄摸到联络站的外墙下。"

    "墙上有一扇通风窗，用铁栅栏封着。透过栅栏，你能隐约看到里面的灯光，听到模糊的对话声。"

    "你把耳朵贴近——"

    $ ch4_exp_overheard_plot = True

    narrator "「……三号已经参加了晚宴。和施泰因那个老太婆聊了很久。」"

    narrator "「施泰因？她不是一直想拉拢外地领主反对王后吗？」"

    narrator "「上面说了，暂时不动三号。让他觐见，看看他什么态度。」"

    narrator "「如果他站在王后这边，就放他走。如果他表现出敌意……」"

    narrator "「那就让他和他父亲一样——永远留在王都。」"

    "最后一句话让你的血液几乎凝固。"

    "「和他父亲一样」——你攥紧了拳头。他们提到了你的父亲。"

    "这些人知道你父亲死亡的内情吗？"

    narrator "「对了，马修斯那边有什么消息？」"

    narrator "「主教已经到了。明天会参加觐见仪式。王后让他做见证人。」"

    narrator "「见证什么？」"

    narrator "「不知道。上面没说。但肯定不只是一场普通的觐见。」"

    "对话声渐渐变小——他们可能转移了位置，或者降低了音量。"

    "你和艾琳娜交换了一个眼神，悄悄撤离了。"

    show elena_img at right with dissolve

    elena "这是一个重要的情报。觐见不是普通的觐见——王后有特殊的安排。"

    elena "而且……他们说「让他和父亲一样」。这已经不是威胁了，这是预谋。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我知道了。明天的觐见，我必须更加小心。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "不止小心。我们需要一个退路——万一事情失控，得有撤离的方案。"

    hide elena_img with dissolve

    return

## --- 子场景：暗百合接头 ---

label ch4_exp_inv_lily_contact:

    "你决定利用暗百合在王都的网络获取情报。"

    show elena_img at right with dissolve

    elena "影卫在王都有一个秘密联络点。在东区药材街的「老陈药铺」后面。"

    elena "暗号是——「有没有去年的暮色兰花」。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "暮色兰花……制作暮色之露的原料？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "是。这个暗号本身就是一种宣言——表明我们知道真相。"

    hide elena_img with dissolve

    $ hide_all_chars()
    "你和艾琳娜在夜色的掩护下来到药材街。"

    "老陈药铺的门已经关了，但后门留了一条缝。"

    "你推门而入，一股浓烈的草药味扑面而来。"

    "柜台后面坐着一个干瘦的老者，戴着一副黄铜框的小圆眼镜，在烛光下翻看一本发黄的医书。"

    "他抬起头，混浊的眼睛在你身上停留了一秒。"

    narrator "「打烊了。明天再来。」"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "有没有去年的暮色兰花？"

    $ hide_all_chars()
    "老者的动作停顿了一瞬——真的只是一瞬。然后他站起身来，走到店铺最里面，拨开一道暗门上的药材帘子。"

    narrator "「跟我来。」"

    "你和艾琳娜跟着他走进暗门，穿过一条狭窄的地下通道，来到一间不大的密室。"

    "密室里坐着三个人——都蒙着面，只露出眼睛。"

    "居中的那个人向你点了点头。"

    narrator "「艾登堡领主。影卫已经等候多时。」"

    $ ch4_exp_lily_contact = True

    menu:
        "开门见山，直接询问暗焰在王都的势力":
            $ change_stat("intrigue", 5)

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "暗焰在王都的势力有多大？"

            $ hide_all_chars()
            narrator "「比你想象的大。也比我们想象的大。」"

            narrator "「暗焰已经渗透了王宫守卫、王都密探、甚至部分教会武装。」"

            narrator "「我们估计，暗焰在王都至少有三百人的暗桩——大多数伪装成普通人。」"

            narrator "「冯·哈根男爵虽然不在王都，但他的触手无处不在。」"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "那你们呢？影卫在王都有多少人？"

            $ hide_all_chars()
            narrator "「不到一百。但每一个都是精锐。」"

            narrator "「我们的优势不在人数——在于信息网络。暗焰的渗透是广而浅，我们的渗透是窄而深。」"

            narrator "「比如——我们在王后身边有一个人。身份绝对可靠。」"

            "你心中一动。王后身边有影卫的人？这是一张极为重要的牌。"

        "询问明天觐见有什么特殊情况":
            $ change_stat("intrigue", 5)

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我听说明天的觐见不是普通觐见。王后有什么特殊安排？"

            $ hide_all_chars()
            narrator "蒙面人歪了歪头。"

            narrator "「我们也在查这件事。目前只知道两点——」"

            narrator "「第一，主教马修斯会作为见证人出席。这在普通觐见中极为罕见。」"

            narrator "「第二，王后在觐见厅旁边的密室准备了……一些东西。我们的人没能查清是什么。」"

            narrator "「但有一种可能——王后打算在觐见时对你提出某种……要求。或者指控。」"

            narrator "「如果你的回答不让她满意——密室里准备的东西，可能就是给你的。」"

            "你攥了攥剑柄。觐见，可能是一场鸿门宴。"

        "请求影卫在觐见时提供暗中保护":
            $ change_stat("power", 5)
            $ change_rel("rel_lily", 5)

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "明天觐见时，能否安排人在暗中接应？"

            $ hide_all_chars()
            narrator "「已经安排了。觐见厅的三名侍从中，有一个是我们的人。」"

            narrator "「如果出现危险，他会发出暗号——杯子落地的声音。」"

            narrator "「听到暗号后，从觐见厅左侧的帷幕后面可以进入一条暗道。」"

            narrator "「暗道通向王宫地下的排水渠，从那里可以出城。」"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "但愿用不到。"

            $ hide_all_chars()
            narrator "「但愿。不过——以王后的手段，做最坏的打算总是明智的。」"

    "密会持续了约半个时辰。"

    "你又获得了一些零散但有价值的情报——包括暗焰在贵宾馆的暗哨身份（是七个侍从中那个最沉默寡言的），以及王后近期频繁召见军事将领的信息。"

    "离开药铺前，蒙面人最后说了一句——"

    narrator "「领主大人。影卫选择了您，就和两百年前选择格里菲斯一世一样。」"

    narrator "「不是因为您的权力——而是因为这个王国本来该有的样子。」"

    narrator "「请不要让我们失望。」"

    "你沉默地点了点头，和艾琳娜沿着暗巷快步离开。斗篷的下摆刮过石板路，身后的王都渐渐沉寂。"

    hide player_char_img with dissolve
    return

## --- 子场景：独自分析 ---

label ch4_exp_inv_solo:

    "没有暗百合的情报网络支持，你只能依靠自己的观察和分析。"

    "你把今天收集到的所有信息铺在桌上，逐一梳理。"

    show elena_img at right with dissolve

    elena "我来帮您整理。"

    "艾琳娜从怀中取出一支炭笔和几张白纸，开始画一张关系网——"

    elena "核心是王后。她的直接控制力量包括：莱因哈特负责的密探网络、宫廷卫队、以及通过教会高层掌握的宗教资源——费雷恩虽死，但他留下的势力仍为王后所用。"

    if not baron_is_darkflame_known:
        elena "间接力量包括：暗焰——暗百合的叛徒分支，由冯·哈根男爵指挥，名义上仍服从于王后。"
        $ baron_is_darkflame_known = True
    else:
        elena "至于暗焰——男爵那边的人——你已经知道。它如今已经不在王后阵营，但男爵有自己的盘算，也不会站到我们这边。"

    elena "潜在的反对力量：施泰因伯爵夫人为首的地方领主派、被软禁的弗雷德里克王子、以及……"

    elena "以及影卫——暗百合的正统派。但他们的势力在王都有限。"

    hide elena_img with dissolve

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "那我们呢？我们有什么？"

    hide player_char_img
    show elena_img at right with dissolve

    elena "说实话——不多。"

    elena "您有艾登堡领主的身份、一支三十人的护卫队、还有我。"

    elena "以及——今天收集到的这些信息碎片。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "够了。在棋盘上，一个兵只要走到底线，就能变成后。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "前提是你能走到底线。"

    "她说完低下头，又去画那张关系网了。"

    hide elena_img with dissolve

    $ hide_all_chars()
    "你沉思了很久。"

    "最终，你在纸上写下了三个关键词——遗诏、暮色之露、王子。"

    "这三个词，串联起了这盘棋局中最重要的线索。"

    if not testament_forged_known:
        "如果你能找到先王的真实遗诏，证明王后篡改了遗诏——那就等于撬动了她权力的根基。"
    elif not testament_original_obtained:
        "遗诏被篡改的事你已经知道了——现在缺的是原件，是铁证。"
    else:
        "遗诏的原件已经在你手里——现在要做的，是把它送到能改变局势的人面前。"

    if not father_poisoned_known:
        "暮色之露是王后最大的秘密。先王和你的父亲都死于同一种毒药——如果能把这个证据公之于众……"
    else:
        "暮色之露的事你早已心知肚明。如果能把毒药的证据公之于众……"

    "而弗雷德里克王子——他是唯一合法的继承人。如果能把他从软禁中解救出来……"

    "但这一切，都要等过了明天的觐见之后才能谋划。"

    "现在，你需要的是——活过明天。"

    return

## ============================================================
## Part 5: 觐见前夜（深夜对话与心理准备）
## ============================================================

label ch4_exp_eve:

    $ play_music("audio/music/campfire.ogg", fadein=2.0)
    scene bg royal_palace with dissolve
    $ set_mood("calm")

    "夜已经很深了。窗外的月光被云层遮去了大半，只在地板上投下一片朦胧的银灰。"

    "你知道自己应该休息。明天是最重要的一天——你需要精神饱满地面对王后。"

    "可你停不下来，脑子一遍遍过着明天可能出的各种岔子。"

    "一阵轻轻的敲门声打断了你的思绪。"

    $ play_sound("audio/sfx/knock.ogg")

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "领主大人，还没睡？"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "睡不着。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "我也是。"

    "雷恩走进来，在你对面的椅子上坐下。烛光照着他饱经风霜的面孔——每一道皱纹都像是用刀刻出来的。"

    captain "跟了您父亲十二年，您继任后又一直跟着。明天的觐见……说不紧张是假的。"

    captain "您父亲当年也来过王都。他回来后对我说——"

    captain "「雷恩，那个地方不是人待的。」"

    captain "我当时以为他在开玩笑。现在看来……他没有。"

    menu:
        "和雷恩聊聊父亲在王都的经历":
            $ change_stat("intrigue", 3)
            $ change_rel("rel_captain", 5)

            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "父亲来王都那次，发生了什么？"

            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "那是……二十多年前了。先王还在世。"

            captain "您父亲是来参加一场贵族集会的。回来之后，他变了一个人。"

            captain "以前他笑得很多，之后就很少笑了。开始加固城堡、训练民兵、在书房里待到深夜。"

            captain "他从来没告诉我原因。但我猜……他在王都看到了什么不该看到的东西。"

            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve

            if testament_forged_known and captain_truth_known:
                player "也许是遗诏的事——大厅里我跟你和奥尔德里克交代过的那一桩。"

                hide player_char_img
                $ hide_all_chars("captain_img")
                show captain_img at left with dissolve
                captain "嗯。先王指定老领主摄政，王后改了遗诏。"

                hide captain_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "他二十年前回来后那些反常——加固城堡、训练民兵、深夜不睡——大概就是从那时候开始的。"
            elif testament_forged_known:
                player "也许是遗诏的事。"

                hide player_char_img
                $ hide_all_chars("captain_img")
                show captain_img at left with dissolve
                captain "遗诏？"

                "你犹豫了一下——但雷恩是你最信任的人之一。"

                hide captain_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "先王可能在遗诏中指定了父亲为摄政者。王后篡改了遗诏。"
            else:
                player "也许他发现了什么不该知道的秘密。"

                hide player_char_img
                $ hide_all_chars("captain_img")
                show captain_img at left with dissolve
                captain "也许吧。您父亲是个聪明人——聪明人在王都往往活不长。"

                hide captain_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "……雷恩，谢谢你告诉我这些。"

            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve

            if testament_forged_known:
                if captain_truth_known:
                    captain "……我早就猜到了八九分。"

                    "雷恩沉默了几秒，火光在他眼里跳动。"

                    captain "您愿意再说一遍，说明您已经准备好面对这一切。我会跟着您走下去。"
                else:
                    captain "……我的天。"

                    "雷恩的脸色变得铁青。"

                    captain "难怪……难怪他后来一直在暗中调查教会。他一定是在找遗诏的线索。"

                    captain "然后他死了。"

                    $ captain_truth_known = True
            else:
                captain "……"

                "雷恩沉默了很久。烛火在他眼眶里微微跳动。"

                captain "也许他看得比我们都远。他在做什么……我到现在都没完全想明白。"

                captain "但我知道一件事——他回来之后，所有的准备都是为了你。"

            "蜡烛的火焰轻轻摇曳，在墙上拉出两道长长的影子。"

        "问雷恩有没有什么战术建议":
            $ change_stat("power", 3)
            $ change_rel("rel_captain", 3)

            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你打过那么多仗，明天的觐见——你有什么建议？"

            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "觐见不是打仗……但也差不多。"

            captain "战场上最重要的是什么？不是武力——是情报。"

            captain "知道敌人想要什么，比知道敌人有多少兵更重要。"

            captain "明天——您不需要赢。您只需要不输。"

            captain "看清王后想要什么，然后——不给她，也不得罪她。"

            captain "拖。拖到我们有足够的筹码再翻牌。"

            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "拖字诀？"

            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "老兵的智慧。急的永远是进攻方。我们是防守方——时间在我们这边。"

        "告诉他早点休息，明天需要他在最佳状态":
            $ change_rel("rel_captain", 3)

            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "雷恩，去睡吧。明天我需要你以最佳状态保护我。"

            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "领主大人也是。"

            "他站起身，走到门口时停了一下。"

            captain "领主大人——不管明天发生什么，我都在您身后。"

            captain "就像当年在您父亲身后一样。"

            "他的声音很稳，没有一丝犹豫。"

    hide captain_img with dissolve

    "雷恩离开后不久，又传来一阵更轻的敲门声。"

    $ play_sound("audio/sfx/knock.ogg")

    hide player_char_img
    show elena_img at right with dissolve

    elena "还醒着？"

    "她没等你回答就走了进来，手里端着两杯热酒。"

    elena "睡前喝一杯。薰衣草泡的，有助于安神。"

    $ hide_all_chars()
    "她把一杯递给你，自己端着另一杯在窗边坐下。"

    "窗外透进来一缕微光，映在她的脸上——那张总是带着冷静面具的脸，在此刻有一种你很少看到的柔和。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你看起来也没睡。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "职业病。每到任务前夜都睡不着。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "这对你来说也是一次「任务」？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "……不。不是任务。"

    "她顿了顿，抿了一口酒。"

    elena "任务是有雇主的。而我现在……"

    elena "我不确定我是为了什么在做这些。"

    menu:
        "（直视她）也许是为了你自己相信的东西":
            $ change_rel("rel_elena", 8)
            $ change_stat("loyalty", 3)
            $ change_courage(-8)

            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你曾经是王后的侍女，后来加入暗百合，再后来来到艾登堡。"

            player "每一次选择，你都是在离王后更远一步。"

            player "也许你早就知道答案了——你只是不愿意承认。"

            "月光在她的眼睛里流转。她低头看着自己的手，像是第一次认出那双手。"

            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "……也许你说得对。"

            elena "我在王后身边看到了太多黑暗。毒杀、阴谋、灭口……她把这些叫做「必要的牺牲」。"

            elena "我曾经也这么以为。直到——"

            elena "直到我看到你处理那些事情的方式。你也面对同样的困境，但你没有选择最卑劣的手段。"

            elena "也许这就是区别。"

            if elena_romance:
                "她低下头，声音变得几乎像是呢喃。"
                elena "也许……也因为你。"
                "你的心跳漏了一拍。你没有说话，只是低头喝了一口酒。"

            "你们就这样聊到烛火快烧尽。明天的觐见，你一个字都没多想——这一夜你给了她，没留给王后。"

        "（半开玩笑）也许是因为这杯酒太好喝了，不想浪费":
            $ change_rel("rel_elena", 5)

            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "说不定是因为你泡的酒太好喝了。"

            "艾琳娜忍不住笑了。那是一个真实的、没有防备的笑——你第一次看到她笑成这样。"

            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "你总是这样——在最紧张的时候说傻话。"

            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "这叫做「缓解压力的高级技巧」。"

            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "你从哪儿学的？"

            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "天赋。"

            "她摇了摇头，但嘴角的笑意没有消退。"

            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "好吧。为了你这个「天赋」——"

            elena "明天，我会全力保护你。"

        "（严肃地）问她对明天觐见的看法":
            $ change_stat("intrigue", 5)
            $ change_rel("rel_elena", 3)
            $ ch4_exp_preparation_level += 1

            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你是最了解王后的人。明天——我该怎么应对她？"

            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "王后最擅长的是读人。她会在见面的第一秒就开始分析你——你的表情、语气、站姿、眼神。"

            elena "所以——不要试图骗她。她能看穿大多数谎言。"

            elena "但你可以选择只说真话的一部分。让她看到你想让她看到的东西。"

            elena "比如——展示你的忠诚，但不展示你的能力。让她觉得你是一个听话但平庸的年轻领主。"

            elena "这是最安全的策略。"

            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "如果她已经通过密探了解了我的真实能力呢？"

            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "那就更不能伪装了。表现出能力，但同时表现出愿意为她所用。"

            elena "在她眼中，有能力的忠臣是资产。有能力的敌人……是必须消灭的威胁。"
            "她把王后读人的习惯、说话的尺度，一条条讲给你听。你都记下了——这一夜的功夫，花在了明天的觐见上。"

    "你们静静地坐着，喝完了各自的酒。窗外的夜空渐渐透出鱼肚白的微光——天快亮了。"

    hide elena_img with dissolve

    $ hide_all_chars()
    "艾琳娜离开后，你独自站在窗前。"

    "远处，王宫的轮廓在黎明中渐渐清晰——白色的穹顶、高耸的尖塔、如同皇冠般的城垛。"

    "再过几个时辰，你就要走进那座宫殿，面对这个国家最危险的女人。"

    "你想起了父亲。想起他在书房里伏案写信的背影。想起他偶尔抬起头来看你时，那双充满忧虑的眼睛。"

    "他是不是也曾像你一样，在某个深夜里，独自面对一个不确定的明天？"

    "你的拳头不由自主地攥紧了。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "（低声）父亲……你没能做到的事，我会替你做完。"

    $ hide_all_chars()
    "你合上窗户。"

    "该来的总会来。"

    $ ch4_exp_preparation_level += 1

    if ch4_exp_preparation_level >= 4:
        "你已经做了充分的准备——了解了王都的暗流、收集了情报、建立了人脉、获得了盟友的支持。"
        "无论王后有什么打算，你都有底牌可打。"
        $ change_stat("intrigue", 5)
    elif ch4_exp_preparation_level >= 2:
        "你做了一些准备。算不上万全之策，不过走进觐见厅的时候不至于两眼一抹黑。"
        $ change_stat("intrigue", 3)
    else:
        "你的准备还不够充分。但时间不等人。你只能走一步看一步。"

    "你吹灭了最后一根蜡烛，在黎明前最后的黑暗中闭上了眼睛。"

    "不是为了睡觉——只是为了让这一刻的宁静多留一会儿。"

    "因为你知道——明天一早，就要进宫见王后了。"

    hide player_char_img with dissolve
    return

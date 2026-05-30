## ============================================================
## NPC深度场景：五段角色个人故事
## npc_depth.rpy
## 商人卡尔的过去 / 队长雷恩的战争往事 / 主教马修斯的信仰危机
## 艾琳娜的故乡回忆 / 奥尔德里克的誓言
## ============================================================
## 不define新角色，使用characters.rpy中已有角色
## 属性用 $ xxx += N，好感度用 $ rel_xxx += N
## 勇气用 change_courage()
## ============================================================

## ── 深度场景进度标记 ──
default karl_past_done = False
default captain_war_done = False
default bishop_doubt_done = False
default elena_homeland_done = False
default aldric_promise_done = False

## ── 内部变量 ──
default karl_revenge_known = False
default karl_full_story = False
default captain_war_regret = False
default bishop_doubt_deep = False
default elena_parents_known = False
default aldric_badge_given = False


## ============================================================
## 1. 商人卡尔的过去（约240行）
## 条件：merchant_deal 影响信任深度
## 影响：wealth, intrigue
## ============================================================

label npc_merchant_karl_past:

    $ karl_past_done = True

    scene bg market with dissolve

    "集市已经收摊，摊贩们正在拆卸帐篷。暮色将整条街道染成昏黄的颜色。"

    "你注意到卡尔没有像往常一样忙着清点货物。他独自坐在一个空木箱上，盯着手里的什么东西出神。"

    $ hide_all_chars("merchant_karl_img")
    show merchant_karl_img at left with dissolve

    "走近了你才看清——那是一枚铜制的商会徽章，磨损得几乎看不清上面的纹饰。"

    hide merchant_karl_img
    show player_char_img at left with dissolve
    player "卡尔？今天收摊倒是早。"

    hide player_char_img
    show merchant_karl_img at left with dissolve
    merchant "啊，领主大人……"

    "他仓促地将徽章收入怀中，但动作太慢，你已经看见了。"

    merchant "没什么，只是……在想一些旧事罢了。"

    menu:
        "你看起来心事重重。"

        "那枚徽章——是王都商会的？":
            $ change_stat("intrigue", 2)
            "卡尔的眼神闪了一下，像是被人戳中了旧伤。"

            merchant "……领主大人好眼力。"

        "想聊聊吗？有时候说出来会好受些。":
            "卡尔苦涩地笑了一下。"

            merchant "您是第一个这么问我的贵族。"

    merchant "这枚徽章……是王都商会的会员章。曾经，我也是那里的人。"

    "他翻过徽章，背面刻着一个名字——卡尔·温特菲尔德。"

    merchant "温特菲尔德商号，听说过吗？"

    hide merchant_karl_img
    show player_char_img at left with dissolve
    player "……似乎在旧账册里见过这个名字。"

    hide player_char_img
    show merchant_karl_img at left with dissolve
    merchant "那就对了。二十年前，温特菲尔德是王都第三大商号。香料、丝绸、铁器——我们什么都做。"

    "他的目光变得遥远，像是在看一幅只有自己能看见的画。"

    merchant "我父亲花了一辈子把商号做到那个规模。我十六岁就跟着他跑商路，从南方的港口到北境的矿场，大半个王国的路我都走过。"

    merchant "二十三岁那年，父亲去世，商号交到我手上。我发誓要让温特菲尔德成为王都第一。"

    "他的声音变得低沉，像是暴风雨前压得很低的云。"

    merchant "然后……伊莎贝拉摄政了。"

    hide merchant_karl_img
    show player_char_img at left with dissolve
    player "王后？"

    hide player_char_img
    show merchant_karl_img at left with dissolve
    merchant "摄政第二年，她推行了新税制。说是为了充盈国库、巩固边防。实际上呢？"

    merchant "对商人征收三成额外税。三成！在原有税基上再加三成！"

    "卡尔的手不自觉地握紧了徽章。"

    merchant "大商号还能撑一撑。但她的税吏不是来收税的——他们是来敲骨吸髓的。"

    merchant "你交了正税，他们说你漏报了货物。你补交了罚款，他们说你仓库里的存货也要缴税。你缴完存货税，他们又来查你三年前的账——三年前的！"

    "他猛地站起来，木箱被踢翻在地。但他随即意识到自己的失态，缓缓坐了回去。"

    merchant "抱歉……每次想到这些，我就……"

    hide merchant_karl_img
    show player_char_img at left with dissolve
    player "继续说。"

    hide player_char_img
    show merchant_karl_img at left with dissolve
    merchant "最后一击来自一个叫莫里斯的税吏长。他看上了我在王都的三处店铺，说要「依法没收」。"

    merchant "我去申诉，被拒绝。我去找关系，发现所有人都不敢帮我。最后我才知道——莫里斯是王后宠臣的表弟。"

    merchant "一夜之间，温特菲尔德商号的招牌被摘了下来。我站在空荡荡的店铺前，看着莫里斯的人把我父亲一辈子的心血搬空……"

    "卡尔的声音终于碎裂了。他别过头去，望着窗外渐沉的暮色。"

    if merchant_deal:

        "因为之前的合作，你和卡尔之间已经建立了一定的信任。他似乎决定告诉你更多。"

        merchant "领主大人……既然我们已经是合作伙伴，有些话我不该再瞒着您。"

        merchant "我来艾登堡，不只是做生意。"

        $ karl_revenge_known = True

        hide merchant_karl_img
        show player_char_img at left with dissolve
        player "……你有别的目的？"

        hide player_char_img
        show merchant_karl_img at left with dissolve
        merchant "复仇。"

        "这个字从他嘴里说出来时，带着一种冰冷的平静。"

        merchant "莫里斯那条狗如今已经是王都的财务总管了。王后给了他更大的权力，他比以前更加猖狂。"

        merchant "但他有个弱点——他的走私渠道必须经过艾登堡附近的山路。如果我能掌握证据……"

        menu:
            "卡尔的复仇计划……"

            "我可以帮你。打击贪腐对艾登堡也有好处。":
                $ change_stat("wealth", 5)
                $ change_stat("intrigue", 5)
                $ karl_full_story = True

                merchant "领主大人……！"

                "卡尔的眼眶泛红。他重重地抱拳，深深鞠躬。"

                merchant "我在南路的商队里安插了人。如果您允许，我可以把他们收集到的走私情报全部交给您。"

                merchant "这些情报不仅能扳倒莫里斯——还能让您在王都拥有一张意想不到的底牌。"

                hide merchant_karl_img
                show player_char_img at left with dissolve
                player "走私情报？"

                hide player_char_img
                show merchant_karl_img at left with dissolve
                merchant "莫里斯不是一个人在捞。他背后是一整条链子——从边境的走私贩子，到王都的贵族买家。这条链子上挂着不少大人物的名字。"

                "卡尔从怀中取出一张折叠得很紧的纸条。"

                merchant "这是第一批名单。请您过目。"

                "你展开纸条。上面列着七个名字，其中有三个你在领主会议上见过。"

                hide merchant_karl_img
                show player_char_img at left with dissolve
                player "这些人……"

                hide player_char_img
                show merchant_karl_img at left with dissolve
                merchant "是的。如果用得好，这些名字就是刺向王后根基的匕首。"

            "我理解你的愤怒，但复仇之路太危险了。":
                $ change_stat("wealth", 3)
                $ change_stat("intrigue", 3)

                merchant "……您说得对。我一个商人，想跟王后的人斗，确实是蚍蜉撼树。"

                merchant "但我至少要让艾登堡不重蹈王都的覆辙。只要您继续公平对待商人，温特菲尔德的幽灵就不会在这里徘徊。"

                "卡尔收起了徽章，目光中的寒意淡了一些。"

            "你有证据吗？没有证据的复仇只会害了自己。":
                $ change_stat("intrigue", 4)
                $ change_stat("wealth", 3)

                merchant "证据……我一直在收集。但还不够，远远不够。"

                merchant "不过，领主大人这么问，是不是意味着——如果证据够了，您愿意帮忙？"

                hide merchant_karl_img
                show player_char_img at left with dissolve
                player "到时候再说。"

                hide player_char_img
                show merchant_karl_img at left with dissolve
                merchant "好。我会继续收集。到了时候，我一定第一个来找您。"

    else:

        "卡尔摇了摇头，像是决定到此为止。"

        merchant "说太多了……领主大人，请恕我失礼。"

        merchant "只是想告诉您——我选择在艾登堡扎根，不是因为这里生意好做。是因为这里的领主……至少看起来，不会像王都那些人一样。"

        $ change_stat("wealth", 3)
        $ change_stat("intrigue", 2)

    "卡尔将铜徽章重新揣入怀中，站起身来，向你行了一个比平时更深的礼。"

    merchant "夜深了，领主大人。感谢您愿意听一个老商人絮叨。"

    $ hide_all_chars()
    "他走入暮色之中。那个弓着腰的背影，比平日里精明干练的商人卡尔，显得苍老了十岁。"

    "你低头看着手掌——关于王都的税吏、关于被碾碎的商号、关于复仇——这些碎片在你脑海中慢慢拼成一幅更大的画面。"

    "伊莎贝拉的统治之下，又有多少个温特菲尔德？"

    hide merchant_karl_img with dissolve

    return


## ============================================================
## 2. 队长雷恩的战争往事（约240行）
## 影响：courage, rel_captain
## ============================================================

label npc_captain_war_story:

    $ captain_war_done = True

    scene bg castle_exterior with dissolve

    "黄昏时分，你在城墙上找到了雷恩。"

    "他独自坐在垛口边，手里端着一壶酒，却似乎一口都没喝。他的目光越过原野，看向北方远处灰蒙蒙的山脊。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    hide captain_img
    show player_char_img at left with dissolve
    player "雷恩？你在看什么？"

    hide player_char_img
    show captain_img at left with dissolve
    captain "……北边。"

    "他顿了一下，像是在决定要不要继续说。"

    captain "风向变了。从北面吹来的风，闻起来像……铁锈和泥土混在一起的味道。"

    captain "上一次闻到这种味道，是二十年前。"

    hide captain_img
    show player_char_img at left with dissolve
    player "二十年前？"

    hide player_char_img
    show captain_img at left with dissolve
    captain "北境之战。领主大人，您那时候还没出生。"

    "雷恩终于喝了一口酒，但脸上的表情比酒更苦。"

    captain "先王格里菲斯七世在位第十二年，北境蛮族突破了山隘。三万蛮兵，像洪水一样涌过来。"

    captain "我那年十九岁，刚从军两年。分到北境第三军团，说好听点叫「边防精锐」——其实就是一群吃不饱饭的穷小子，穿着生锈的铁甲，扛着钝刀去送死。"

    hide captain_img
    show player_char_img at left with dissolve
    player "你参加了那场战役？"

    hide player_char_img
    show captain_img at left with dissolve
    captain "参加？我从头打到尾。"

    "雷恩放下酒壶，伸出右手。在暮色中你才注意到，他的右手小指是断的——一直以来他都用手套遮着。"

    captain "第一天就丢了这个。一个蛮族的斧头劈下来，我举刀去挡，刀断了，斧刃削掉了我的小指。"

    captain "我当时想——完了，第一天就要死在这了。"

    captain "结果没死。旁边一个老兵一刀砍断了蛮族的腿。那个老兵叫格拉姆，比我大十五岁，满嘴脏话，酒量惊人。"

    "雷恩低下头看着自己残缺的手，没说话。"

    captain "格拉姆救了我之后说——「小子，战场上不是看谁勇敢，是看谁命硬。你命硬不硬，明天就知道了。」"

    captain "第二天他就死了。"

    "风从北方吹来，带着深秋的寒意。"

    captain "那场仗打了四十天。四十天。您知道四十天是什么概念吗？"

    captain "前十天，你还能分清敌人和战友。中间十天，你只能分清活人和死人。最后二十天——你连自己是不是还活着都分不清了。"

    menu:
        "你想问他什么？"

        "你是怎么活下来的？":
            $ change_courage(5)
            $ change_rel("rel_captain", 5)

            captain "靠运气。纯粹的运气。"

            captain "我旁边的人一个接一个倒下——左边的被长矛穿透了胸膛，右边的被马蹄踩碎了头骨。我站在中间，浑身是血，大部分不是我的。"

            captain "最后一天，我们等来了先王亲率的援军。格里菲斯七世骑着白马冲在最前面——那是我这辈子见过最壮观的景象。"

            captain "蛮族溃败。我跪在尸山血海里，听到身后有人在欢呼，但我只能哭。"

        "那场仗最后是怎么赢的？":
            $ change_courage(3)
            $ change_rel("rel_captain", 3)
            $ change_stat("intrigue", 2)

            captain "先王格里菲斯七世亲征。他没有躲在后方等战报——他带着五千禁卫军，星夜驰援。"

            captain "整整三天三夜的急行军，五千人硬是在蛮族合围之前赶到了。"

            captain "先王挥剑冲在第一排。他的铠甲被砍得全是豁口，但他没退一步。"

            captain "那一天，我知道了什么叫真正的王。不是坐在金椅子上发号施令的人——是愿意和你一起流血的人。"

        "格拉姆……你经常想起他吗？":
            $ change_rel("rel_captain", 8)

            "雷恩的手明显颤了一下。"

            captain "每天。"

            captain "他有个女儿，当时才三岁。他跟我说过，等打完仗就回家，再也不当兵了。"

            captain "战后我去找过他的家人。他女儿已经被送到孤儿院了——他妻子在他死后不久就病倒了，没撑过那个冬天。"

            captain "我每年都给那个孤儿院送钱。不多，但……至少能让自己好过一点。"

    captain "领主大人，您知道我为什么跟您说这些吗？"

    hide captain_img
    show player_char_img at left with dissolve
    player "为什么？"

    hide player_char_img
    show captain_img at left with dissolve
    captain "因为战争又要来了。我闻得到那个味道。"

    "他站起身来，面朝北方。暮色中，他的身影像一柄插在城墙上的旧剑。"

    captain "北境的蛮族在集结。王后的军队忙着镇压南方的叛乱，北边兵力空虚。各领地的领主各怀鬼胎，没人愿意往北境增兵。"

    captain "如果蛮族再次南下——不，不是如果，是早晚的事——这一次，不会有格里菲斯七世骑着白马来救我们了。"

    hide captain_img
    show player_char_img at left with dissolve
    player "这一次……轮到我们自己了。"

    hide player_char_img
    show captain_img at left with dissolve
    captain "是的。"

    "雷恩转过身来，他的眼神在暮色中显得格外深沉。"

    captain "我跟了您父亲十五年，又跟了您。您和您父亲一样，有一种让人愿意为之赴死的东西。"

    captain "但领主大人——请不要让好人白白赴死。战争不是故事里写的那样，没有什么光荣的冲锋。战场上只有泥、血、和哭声。"

    menu:
        "雷恩的话让你深思。"

        "我会竭尽所能避免战争。但如果避无可避，我会和士兵们站在一起。":
            $ change_courage(8)
            $ change_rel("rel_captain", 8)
            $ captain_war_regret = True

            "雷恩的眼中闪过一道光——那是一种被理解的释然。"

            captain "……这就够了。"

            captain "如果必须打，就让我站在您前面。这条老命，早就该在二十年前交代的。多活的每一天，都是赚的。"

        "战争……有没有可能用谈判解决？":
            $ change_courage(3)
            $ change_rel("rel_captain", 5)
            $ change_stat("intrigue", 3)

            captain "谈判？和蛮族？"

            "雷恩想了想，没有直接否定。"

            captain "二十年前不可能。但现在……蛮族也有新的首领了，听说是个年轻人，比他父亲聪明得多。"

            captain "也许，可以试试。但谈判桌上的筹码，永远是你手里有多少兵。"

        "格里菲斯七世已经不在了。但他的精神可以留下。":
            $ change_courage(5)
            $ change_rel("rel_captain", 6)
            $ change_stat("reputation", 3)

            captain "他的精神……"

            "雷恩低头看了看自己残缺的右手，然后握成了拳。"

            captain "先王曾经对我们说过一句话。他说——「一个国家的脊梁不是国王，是那些在黑暗中坚守的普通人。」"

            captain "我记了二十年。今天，我把这句话也说给您听。"

    "夜色已经完全笼罩了城墙。远处的原野上，零星的灯火像散落的星子。"

    captain "谢谢您听我说这些，领主大人。好久没跟人提起北境的事了。"

    "雷恩拿起酒壶，终于痛快地灌了一大口。"

    captain "走吧，天冷了。明天还有一队新兵要训练——那些小子连刀都握不稳，跟我当年一样。"

    $ hide_all_chars()
    "他粗糙的笑声消散在夜风里。而你站在城墙上多停留了一会儿，望着北方那片看不见的山脊。"

    "风的味道——你还闻不出来。但你记住了雷恩的话。"

    hide captain_img with dissolve

    return


## ============================================================
## 3. 主教马修斯的信仰危机（约240行）
## 条件：alliance_church 影响坦诚程度
## 影响：faith, rel_bishop
## ============================================================

label npc_bishop_doubt:

    $ bishop_doubt_done = True

    scene bg church_interior with dissolve

    "深夜，你收到主教马修斯的一封短笺，只写了一句话——"

    "{i}「若方便，请来教堂。后门。」{/i}"

    "教堂后门通向一间狭小的忏悔室。烛光摇曳中，马修斯跪在圣像前，但他没有在祈祷——他只是低着头，一动不动。"

    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve

    "你轻轻敲了敲门框。他转过头，眼底的疲惫像经年的灰尘一样厚。"

    bishop "您来了……感谢。"

    bishop "请坐。这里没有别人——连神明，我现在都不确定是否还在倾听。"

    hide bishop_img
    show player_char_img at left with dissolve
    player "马修斯？你还好吗？"

    hide player_char_img
    show bishop_img at left with dissolve
    bishop "不好。"

    "他的坦诚让你有些意外。平日里的马修斯总是温文尔雅、措辞谨慎——像一面永远光洁的铜镜。"

    bishop "领主大人，我今天找您来，不是以主教的身份——而是以一个罪人的身份。"

    if bishop_confession_done:
        # 玩家已经在醉酒忏悔中得知遗诏真相，跳过重复叙述
        "他从法袍内取出一卷羊皮纸——你认出来了，那是先王遗诏的篡改版本。"

        bishop "那晚我喝醉了，说了很多……但今天，我想清醒地、正式地把一切告诉你。"

        bishop "我不想让你觉得那只是一个醉汉的胡话。那些都是真的。每一个字。"

        "马修斯将羊皮纸放在桌上，像是放下了一块烧红的铁。"

        menu:
            "面对主教的正式告白……"

            "你为什么现在才说？":
                $ change_stat("faith", 2)
                $ change_rel("rel_bishop", 3)

                bishop "因为害怕。"

                bishop "但我更害怕沉默。每天站在圣坛上布道，教人向善、教人正直——而我自己藏着这样一个秘密，我觉得自己是这个教堂里最大的伪善者。"

            "原始遗诏还存在吗？":
                $ change_stat("intrigue", 3)
                $ change_rel("rel_bishop", 3)

                bishop "存在。"

                bishop "那晚我对你说过——费雷恩让我销毁它，但我没有。那份原件还在一个只有我知道的地方，这二十年没被任何人发现。"

                bishop "时机合适时我会交给你。到那天，我也就该准备面对我应得的后果了。"

            "你在怀疑自己的信仰？":
                $ change_stat("faith", 5)
                $ change_rel("rel_bishop", 5)

                "马修斯抬起头。他的眼中有泪光，但没有落下。"

                bishop "不是怀疑神明。是怀疑……人。"

                bishop "有时候我站在圣坛上，看着下面那些虔诚的信徒——农夫、铁匠、洗衣妇——他们真心地相信教会会保护他们。而我知道教会把他们卖给了王后。"

                bishop "那种感觉……比什么都痛苦。"

    else:
        "他从法袍内取出一卷羊皮纸。纸张很旧，但保存得极好。"

        bishop "这是先王格里菲斯七世的遗诏。"

        "你的心猛地跳了一下。"

        bishop "……是篡改后的版本。"

        hide bishop_img
        show player_char_img at left with dissolve
        player "你怎么会有这个？"

        hide player_char_img
        show bishop_img at left with dissolve
        bishop "因为……篡改遗诏的人之一，就是教会。"

        "他的声音像一根绷到极限的弦，随时可能断裂。"

        bishop "二十年前，先王驾崩。原始遗诏中指定了艾登堡领主——也就是您的父亲——作为唯一的摄政，直到王子成年。"

        bishop "但伊莎贝拉不甘心将权力拱手让人。她找到了大主教费雷恩——我的前任上级——提出了一笔交易。"

        hide bishop_img
        show player_char_img at left with dissolve
        player "什么交易？"

        hide player_char_img
        show bishop_img at left with dissolve
        bishop "教会支持她独揽摄政权，作为交换，王后将教会的征税权从三个行省扩大到全国。"

        bishop "大主教费雷恩答应了。他在先王驾崩的当晚，亲手将遗诏调了包，用教会的印章为篡改后的版本背书。"

        "马修斯将羊皮纸放在桌上，像是放下了一块烧红的铁。"

        bishop "那一夜我就跪在祭坛旁——作为费雷恩的年轻学生，亲眼看着老师用教会的印章为篡改后的遗诏背书。我那时年轻又虔诚，对老师的命令深信不疑；等我意识到自己见证的是什么，一切都已经发生了。"

        menu:
            "面对这个惊人的真相……"

            "你为什么现在才说？":
                $ change_stat("faith", 2)
                $ change_rel("rel_bishop", 3)

                bishop "因为害怕。"

                bishop "我害怕说出来之后，我所信仰的一切都会崩塌。教会是我的家、我的根——如果教会本身就是罪恶的帮凶，那我这些年的祈祷、我的信仰……算什么？"

                "他的手指紧紧攥着胸前的圣徽。"

                bishop "但沉默比恐惧更可怕。二十年了，这个秘密像毒药一样侵蚀着我的灵魂。"

            "遗诏……原始版本还存在吗？":
                $ change_stat("intrigue", 3)
                $ change_rel("rel_bishop", 3)

                "主教的眼神躲闪了一瞬。他看着手中的杯子，没有立刻回答。"

                bishop "……存在。"

                bishop "我不该告诉你的——但你既然问了，我也不想再骗你。"

                bishop "如果它的下落泄露出去，藏它的人和知情的人都活不过三天。所以现在，我只能告诉你这些：它还在。在一个安全的地方。"

                bishop "当时机合适，当我有足够的勇气——我会把它交给一个能用它揭开真相的人。也许……就是你。"

            "你在怀疑自己的信仰？":
                $ change_stat("faith", 5)
                $ change_rel("rel_bishop", 5)

                "马修斯抬起头。他的眼中有泪光，但没有落下。"

                bishop "不是怀疑神明。是怀疑……人。"

                bishop "我相信神明是慈悲的。但神明的代言人呢？教会的长老们呢？他们披着圣袍，行的是权力的勾当。"

                bishop "我曾经以为沉默是一种保护。现在我知道了——沉默就是同谋。"

                bishop "那种感觉……比什么都痛苦。"

        ## 主教质疑场景揭示了遗诏篡改和父亲摄政权的真相
        $ testament_forged_known = True
        $ ferein_role_known = True
        $ father_was_regent_known = True

    if alliance_church:

        "因为你和教会已经建立了同盟关系，马修斯对你的信任更进了一步。"

        bishop "领主大人……既然我们是盟友，那我就不该对您有所隐瞒。"

        bishop "我一直在暗中联络教会内部同样对大主教不满的人。我们……可以算是一个小小的改革派。"

        $ bishop_doubt_deep = True

        hide bishop_img
        show player_char_img at left with dissolve
        player "改革派？有多少人？"

        hide player_char_img
        show bishop_img at left with dissolve
        bishop "不多。七个人。分布在五个行省。但每一个都在教会中有一定的影响力。"

        bishop "我们的目标不是推翻教会——而是清除教会中与王后勾结的蛀虫，恢复教会本应有的样子。"

        menu:
            "对于马修斯的改革派……"

            "我支持你。教会需要真正的信仰者来领导。":
                $ change_stat("faith", 5)
                $ change_rel("rel_bishop", 8)

                bishop "领主大人……！"

                "马修斯起身，向你深深行礼。他的眼角终于有泪滑落。"

                bishop "有您这句话，我……这些年的挣扎就没有白费。"

                bishop "我会将改革派的名单和联络方式交给您。在适当的时候，我们可以里应外合，彻底清理教会中的腐败。"

                bishop "这不仅是为了信仰——也是为了那些无辜的信徒。"

            "先稳住。教会内部的事，不宜操之过急。":
                $ change_stat("faith", 3)
                $ change_rel("rel_bishop", 5)
                $ change_stat("intrigue", 2)

                bishop "您说得对。太急了反而会打草惊蛇。"

                bishop "大主教耳目众多。如果被他察觉改革派的存在，我们所有人都会被以「异端」的罪名处决。"

                bishop "我会继续潜伏。但请您记住——当风暴来临时，教会内部不全是敌人。"

    else:

        "马修斯似乎还有什么想说，但最终摇了摇头。"

        bishop "我今天说的这些，已经足够让我被革职甚至处死了。但我选择相信您。"

        $ change_stat("faith", 3)
        $ change_rel("rel_bishop", 5)

    "他重新跪在圣像前，双手合十。但这一次，他的姿态不再是机械的仪式——而是一个真正在寻求答案的人。"

    bishop "领主大人，您信神吗？"

    hide bishop_img
    show player_char_img at left with dissolve
    player "……"

    hide player_char_img
    show bishop_img at left with dissolve
    bishop "有时候我羡慕那些不信的人。他们至少不用承受……被自己的信仰背叛的痛苦。"

    bishop "但也正因为我还信——我才不愿意让教会继续堕落下去。"

    "他抬起头，烛光映在他的眼中，像两簇微弱但不肯熄灭的火焰。"

    bishop "谢谢您来。谢谢您听我说这些。"

    bishop "请您……替我保守这个秘密。"

    $ hide_all_chars()
    "你点头，转身走出忏悔室。身后传来低沉的诵经声——不知是祈祷，还是忏悔。"

    "走出教堂时，夜空中繁星密布。你忽然想——在那些星星背后，真的有什么在注视着这一切吗？"

    "如果有，他一定很失望。"

    hide bishop_img with dissolve

    return


## ============================================================
## 4. 艾琳娜的故乡回忆（约250行）
## 条件：elena_romance 影响互动方式
## 影响：rel_elena, loyalty
## ============================================================

label npc_elena_homeland:

    if elena_homeland_done:
        return

    $ elena_homeland_done = True

    scene bg castle_exterior with dissolve

    "初雪。城堡的花园里铺上了一层薄薄的白色。"

    "你在花园的角落发现了艾琳娜。她站在一棵光秃秃的老梧桐树下，仰着头看飞舞的雪花。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve

    $ hide_all_chars()
    "她没有穿平时那身利落的深色衣裙，而是裹着一件明显过大的灰色斗篷——那是士兵们的制式斗篷，不知道她从哪里弄来的。"

    "最让你意外的是她的表情。那张永远冷静、永远带着几分算计的脸上，此刻只有一种你从未见过的东西——柔软。"

    hide elena_img
    show player_char_img at left with dissolve
    player "艾琳娜？这么冷的天……"

    hide player_char_img
    show elena_img at left with dissolve
    elena "……下雪了。"

    "她说这三个字的语气，像是一个小女孩在说「我想回家」。"

    elena "我家乡也会下雪。比这里更大、更密。"

    if elena_spy_known:
        "你从未听她提起过家乡。她的间谍身份你已经知道了，但关于她真正的出身——那个人，而非那件武器——你一无所知。"
    else:
        "你从未听她提起过家乡。事实上，关于她的过去，你知道的几乎为零。"

    hide elena_img
    show player_char_img at left with dissolve
    player "你的家乡……在哪里？"

    "雪花落在她的睫毛上，融化成细小的水珠。她没有擦。"

    hide player_char_img
    show elena_img at left with dissolve
    elena "王都。我出生在王都。"

    elena "我家曾经是贵族——虽然早就没落了。小时候住在旧城区的一栋老宅子里，冬天窗户漏风，但花园里有一棵很大的梧桐树。下雪的时候，整棵树都会变成白色的。"

    "她的目光柔和了一瞬，但很快又沉了下去。"

    elena "我父亲……在我很小的时候就去世了。母亲后来改嫁，搬去了别的地方。再也没回来看过我。"

    hide elena_img
    show player_char_img at left with dissolve
    player "那你呢？谁照顾你？"

    hide player_char_img
    show elena_img at left with dissolve
    elena "没有人。"

    "她的声音突然变冷了，像是有什么开关被触动。"

    if elena_spy_known:
        elena "你已经知道我是谁了——侍女学院出来的间谍，王后的棋子，后来变成暗百合的人。"
    else:
        elena "我不是你以为的那种人。我是侍女学院训练出来的间谍——王后的棋子。"
        $ elena_spy_known = True
        if dark_lily_exists_known:
            elena "后来变成暗百合的人。"
        else:
            elena "后来我背叛了她，加入了一个叫暗百合的组织。"
            $ dark_lily_exists_known = True

    elena "但你不知道的是——那些年我到底害了多少人。"

    "她的手不自觉地攥紧了斗篷的边缘。"

    elena "艾登堡之前，我执行过三次任务。每一次，都意味着一个家族的崩塌。"

    hide elena_img
    show player_char_img at left with dissolve
    player "第四个……就是艾登堡。你来之前，已经毁过三个人家？"

    hide player_char_img
    show elena_img at left with dissolve
    elena "是。已经毁掉了三个人的人生。王后让我监视他们，我提供的情报让他们失去了一切。"

    "雪越下越大。艾琳娜的声音很平静，像是在讲别人的故事。但她的手在颤抖。"

    elena "五年前我被派来艾登堡，任务是监视老领主——你的父亲。"

    elena "但你父亲发现了我的身份。我以为自己死定了。"

    elena "他却对我说：「一个十二岁就被训练成工具的孩子，不应该为别人的野心负责。」"

    menu:
        "你不知道该说什么。"

        "后来呢？父亲是怎么做的？" if not elena_identity_exposed_known:
            $ change_rel("rel_elena", 5)
            $ change_stat("loyalty", 3)
            $ elena_parents_known = True

            elena "他把我介绍给了暗百合。"

            "她的语气里有自嘲，也有苦涩。"

            elena "从那以后，表面上我是双重间谍——给王后写报告，为暗百合收集情报。但实际上，我的一切行动都是为了你父亲。"

            elena "你父亲从来没有把我当成间谍或者工具。他会问我吃得好不好、住得习不习惯。"

            elena "那是我第一次知道，原来被人关心是这种感觉。"

        "侍女学院……王后还在用这种方式培养间谍吗？":
            $ change_stat("intrigue", 3)
            $ change_rel("rel_elena", 3)
            $ elena_parents_known = True

            elena "当然。现在学院里还有几十个像我当年一样的女孩。"

            elena "没落贵族的孤女、无人认领的孩子……王后从来不缺原材料。"

            elena "讽刺吗？她用别人的不幸来铸造自己的武器。"

        "你不用继续说了。我能看出来这些回忆很痛苦。":
            $ change_rel("rel_elena", 8)
            $ elena_parents_known = True

            "艾琳娜愣了一下。"

            elena "……您是认真的吗？"

            elena "从来没有人这么说过。学院的训练官说「过去是累赘」。王后说「忘记过去才能向前走」。"

            elena "但我忘不掉。旧宅子的花园、那棵梧桐树、父亲抱着我看雪的样子……"

            "她的声音终于碎裂了，像薄冰上突然出现的裂痕。"

    if elena_romance:

        $ hide_all_chars()
        "你走近她。雪花落在你们两个人的肩头。"

        "她没有躲开——这对一个习惯了保持距离的人来说，本身就是一种信任。"

        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "……你为什么对我这么好？"

        hide elena_img
        show player_char_img at left with dissolve
        player "因为你值得被好好对待。"

        hide player_char_img
        show elena_img at left with dissolve
        elena "不。我是间谍。我接近你是带着任务来的。我不值得——"

        hide elena_img
        show player_char_img at left with dissolve
        player "那是过去的你。我看到的是现在的你。"

        "她低下头。有东西从她的脸颊滑落，不知道是雪水还是别的什么。"

        hide player_char_img
        show elena_img at left with dissolve
        elena "王都旧城区……如果有一天太平了，我想回去看看。那栋老宅子还在不在，花园里的梧桐树还在不在。"

        elena "如果……如果你愿意的话，可以一起去吗？"

        $ change_rel("rel_elena", 10)
        $ change_stat("loyalty", 5)

        hide elena_img
        show player_char_img at left with dissolve
        player "当然。"

        "她终于抬起头，眼眶是红的，但嘴角有一丝真实的、不带任何伪装的笑。"

        hide player_char_img
        show elena_img at left with dissolve
        elena "谢谢你。"

        $ hide_all_chars()
        "雪继续下着。你们并肩站在老梧桐树下，肩膀几乎靠在一起。"

        "这或许是自你们相识以来，她第一次卸下了所有的盔甲。"

    else:

        "艾琳娜抬起袖子擦了擦眼角，动作很快，像是不想被你看见。"

        elena "抱歉。说这些做什么呢。过去的事……改变不了。"

        $ change_rel("rel_elena", 5)
        $ change_stat("loyalty", 3)

        hide elena_img
        show player_char_img at left with dissolve
        player "改变不了过去，但可以改变将来。"

        hide player_char_img
        show elena_img at left with dissolve
        elena "将来？"

        "她看着你，眼神里有一丝困惑——也许还有一丝微弱的希望。"

        elena "也许吧。至少在艾登堡……我不再觉得自己只是一颗棋子了。"

    $ hide_all_chars()
    "雪渐渐停了。花园里一片银白。"

    "艾琳娜将那件灰色斗篷裹紧了一些，向你微微点头。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "领主大人，今天的话……请忘了吧。明天我还是那个冷面的情报官。"

    $ hide_all_chars()
    "但你知道你不会忘。"

    "那个在雪中仰头的少女，那个父亲早逝、母亲改嫁后被独自留下的孤儿，那个被迫成为棋子却从未放弃温柔的女人——这些碎片拼在一起，才是完整的艾琳娜。"

    "你终于理解了她为什么总是在白天戴着面具。"

    "因为面具之下的东西，太脆弱了。"

    hide elena_img with dissolve

    return


## ============================================================
## 5. 奥尔德里克的誓言（约230行）
## 影响：rel_aldric, reputation
## ============================================================

label npc_aldric_promise:

    $ aldric_promise_done = True

    scene bg study with dissolve

    "又是一个深夜。灰烬塌了一块，炉子里的木头烧到一半就灭了——没人加柴。"

    "奥尔德里克端着一杯热茶走进来——这是他每晚都会做的事。但今晚，他手里除了茶杯，还多了一个小小的锦盒。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "少主，请先喝茶。"

    "他将茶杯放在桌上，然后将锦盒小心翼翼地放在一旁。那个锦盒的绸面已经褪色，但角落里绣着的鹰徽依然清晰。"

    hide aldric_img
    show player_char_img at left with dissolve
    player "奥尔德里克？那是什么？"

    hide player_char_img
    show aldric_img at left with dissolve
    aldric "……一件我保存了三十年的东西。"

    "他没有立刻打开锦盒，而是在你对面的椅子上坐了下来。昏暗的灯光下，他布满皱纹的脸看起来比平时更老、也更沉重。"

    aldric "少主，您还记得我跟您说过，我曾经是皇家骑士团的成员吗？"

    hide aldric_img
    show player_char_img at left with dissolve
    player "第七席。奥尔德里克·冯·布伦纳。"

    hide player_char_img
    show aldric_img at left with dissolve
    aldric "您记得。"

    "他露出一个欣慰的微笑，但那微笑很快被一种更复杂的情绪取代。"

    aldric "骑士团有一个传统——每当一位骑士被国王亲自授勋时，国王会赐予他一枚私人徽章。不是官方的军衔徽章，而是国王亲手选的、只属于那位骑士的信物。"

    aldric "格里菲斯七世给了我这个。"

    $ hide_all_chars()
    "他打开锦盒。"

    "里面是一枚银质徽章，比一般的军徽小得多，大约只有一枚银币大小。正面刻着一柄剑与一面盾交叉的图案，细节精致得像是出自王宫最好的工匠之手。"

    "你翻过徽章，背面刻着一行极小的字——"

    hide aldric_img
    show player_char_img at left with dissolve
    player "「守护者永不背弃」……"

    hide player_char_img
    show aldric_img at left with dissolve
    aldric "这是格里菲斯七世亲笔刻的。他的手工并不算好——您看这里，这个'弃'字的最后一笔歪了。"

    "老人轻轻用手指描过那个歪斜的笔画，像是在触摸一段遥远的记忆。"

    aldric "那是一个秋天的傍晚。先王刚刚打完北境之战回来，满身的伤还没养好，就急着给参战的骑士们授勋。"

    aldric "轮到我的时候，他拿出这枚徽章，笑着说——「奥尔德里克，我刻了一晚上，刻坏了三枚。这是第四枚，将就看吧。」"

    "奥尔德里克的声音开始发颤。"

    aldric "我当时单膝跪地，先王亲手把徽章别在我的胸口。他说——"

    aldric "「守护者永不背弃。这不是命令，是请求。我请求你，无论将来发生什么，都不要忘记今天你发过的誓。」"

    aldric "我说——「陛下，臣用生命起誓。」"

    "炉膛里的铁架子烧得通红，发出一声金属的呻吟。"

    if aldric_personal_done:
        aldric "少主，还记得我跟您说过先王遇刺的事吗？那晚的刺客……其实只是最后一击。"

        if queen_poisoned_king_known:
            aldric "您已经知道了吧——暮色之露。王后用了整整两年。刺客不过是来收割最后一口气的。"
        else:
            aldric "后来我查明了真相。刺客只是表象——先王在那之前已经被人下了整整两年的慢性毒药。"
            aldric "是暮色之露。王后用了整整两年，慢慢地、一滴一滴地毒杀了他。刺客不过是在先王油尽灯枯时，来收割最后一口气的。"
            $ queen_poisoned_king_known = True
    else:
        aldric "二十年前，先王驾崩。我没能保护他——我在千里之外的艾登堡，接到消息时已经晚了三天。"

        if queen_poisoned_king_known:
            aldric "您已经知道真相了——暮色之露。王后用了整整两年。"
        else:
            aldric "后来我才知道，是暮色之露。王后用了整整两年，慢慢地、一滴一滴地毒杀了他。"
            $ queen_poisoned_king_known = True

    aldric "两年……先王一定很痛苦。他一定知道有人在害他。但他什么都没说——也许是为了保护什么人，也许是因为证据不够，也许……只是因为他太善良了。"

    "奥尔德里克闭上了眼睛。一滴浊泪从他的皱纹间滑落。"

    aldric "三十年了。我每天都在想——如果我当时在他身边，是不是就能发现？是不是就能阻止？"

    aldric "但我不在。守护者永不背弃——而我背弃了他。"

    hide aldric_img
    show player_char_img at left with dissolve
    player "奥尔德里克……那不是你的错。"

    hide player_char_img
    show aldric_img at left with dissolve
    aldric "不。是我的错。"

    "他的语气不容争辩，带着一种自我审判的残酷。"

    aldric "我发过誓。誓言不会因为距离而失效。我应该更警觉、应该更早察觉王后的异样、应该——"

    "他停住了。双手慢慢攥成了拳头。"

    aldric "但现在说这些已经没有意义了。少主……我找您来，是为了另一件事。"

    "他将锦盒推向你。"

    aldric "我想把这枚徽章交给您。"

    hide aldric_img
    show player_char_img at left with dissolve
    player "给我？但这是先王赐给你的——"

    hide player_char_img
    show aldric_img at left with dissolve
    aldric "正因为是先王赐的，才更应该传下去。"

    "奥尔德里克站起身来。尽管他的眼中还有泪痕，但他的腰板挺得笔直——在这一刻，他不再是佝偻的老管家，而是当年那个意气风发的皇家骑士。"

    aldric "少主，您是先王血脉的守护者。您身上流的不是格里菲斯的血，但您守的是格里菲斯的土地、格里菲斯的子民。"

    aldric "先王若在天有灵，他会希望这枚徽章交到一个……真正配得上「守护者」这三个字的人手里。"

    menu:
        "奥尔德里克将徽章递向你……"

        "我收下。我会像你一样，守护应该守护的东西。":
            $ change_rel("rel_aldric", 10)
            $ change_stat("reputation", 8)
            $ aldric_badge_given = True

            "你郑重地接过徽章。银质的小物件握在手中，比想象的更有分量——也许是因为它承载了三十年的重量。"

            aldric "谢谢您，少主。"

            "老人再次单膝跪地——这一次，他跪的不是国王，而是他选择守护的人。"

            aldric "从今天起，这枚徽章就是您的了。它不会给您带来权力或财富——但它会提醒您，在最黑暗的时刻，有些东西值得坚守。"

            aldric "守护者永不背弃。"

            "你将徽章别在胸口内侧——贴着心脏的位置。"

            hide aldric_img
            show player_char_img at left with dissolve
            player "永不背弃。"

        "我不确定自己配得上这份传承，但我会努力去配得上。":
            $ change_rel("rel_aldric", 8)
            $ change_stat("reputation", 5)
            $ aldric_badge_given = True

            "奥尔德里克摇了摇头。"

            hide player_char_img
            show aldric_img at left with dissolve
            aldric "少主，没有人一开始就配得上。先王授勋那天，我也觉得自己不够格。"

            aldric "配得上不是一种状态，是一种选择。每一天，每一个决定，你都在选择——要做怎样的人。"

            "你伸出手，接过了徽章。"

            aldric "请收好它。在您需要力量的时候——不是刀剑的力量，而是坚持的力量——请握住它。"

            "徽章很凉。但你知道它会慢慢被你的体温捂热，就像那句誓言会慢慢成为你自己的。"

        "你留着吧，奥尔德里克。先王把它给了你，它属于你。":
            $ change_rel("rel_aldric", 6)
            $ change_stat("reputation", 3)

            "奥尔德里克愣住了。然后他笑了——一种苦涩的、但也带着温暖的笑。"

            aldric "少主……您太像您父亲了。他也是这样——总是把重要的东西留给别人。"

            aldric "好吧。那我替您保管。但请您记住——这枚徽章，随时都可以来拿。"

            aldric "在您需要它的那一天——它一定在这里等您。"

    $ hide_all_chars()
    "夜渐渐深了。奥尔德里克帮你续上茶，又往炉子里添了两块柴，然后向你行礼告退。"

    "走到门口时，他停下了脚步。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "少主。"

    hide aldric_img
    show player_char_img at left with dissolve
    player "嗯？"

    hide player_char_img
    show aldric_img at left with dissolve
    aldric "您父亲去世前的最后一封信里，写了一句话。我一直没告诉您，因为我觉得时机不到。"

    aldric "但今晚……也许时机到了。"

    hide aldric_img
    show player_char_img at left with dissolve
    player "他写了什么？"

    hide player_char_img
    show aldric_img at left with dissolve
    aldric "「奥尔德里克，我的时间不多了。请替我看着那孩子。不是让他成为我——而是让他成为他自己。」"

    $ hide_all_chars()
    "门轻轻关上了。"

    "你独自坐在书房里。窗外的夜色浓得像墨，风从窗缝钻进来，带着深秋的凉意。"

    "桌上的茶已经凉了。但你胸口的位置——无论是否别着那枚徽章——都有一种温热的感觉在蔓延。"

    "「守护者永不背弃。」"

    "你将这句话低声念了一遍。然后又念了一遍。"

    "直到窗外的天空露出第一丝灰白。"

    hide aldric_img with dissolve

    return

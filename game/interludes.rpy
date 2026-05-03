## ============================================================
## 章间过渡 — 四段章间叙事
## ============================================================

## ── 第一章 → 第二章 过渡 ──────────────────────────

label interlude_ch1_ch2:

    scene bg_castle_corridor with dissolve
    play music "audio/music/night_mystery.ogg" fadeout 2.0 fadein 3.0

    "夜已深沉。你回到书房，烛火在风中摇曳不定。"

    "桌上堆满了文书——税收账册、边境巡逻报告、来自王都的密函。"

    "你刚刚度过了作为领主的第一次真正考验。桌上那些未拆的密函在提醒你——还有更多考验在等着。"

    if father_death_known:
        "父亲死因的疑云仍然笼罩在你心头。那些隐约的线索指向一个你不愿面对的真相。"
    else:
        "关于父亲的死，你知道的仍然太少。或许有些事情，注定要在日后才能浮出水面。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "少主，有一封信。"

    "奥尔德里克递来一封蜡封的信函。蜡封上是王室的百合花纹章。"

    hide aldric_img
    show player_char_img at left with dissolve
    player "王都来的？"

    hide player_char_img
    show aldric_img at left with dissolve
    aldric "是的。信使说……领主会议将在三周后召开。所有持有封地的贵族必须出席。"

    $ hide_all_chars()
    "你拆开信函。洋皮纸上的字迹工整而冰冷："

    "{i}致艾登堡领主：兹令各领地之主于霜月十五日齐聚王都，参加年度领主会议。届时将商讨边境防务、税制改革及继承法修订等议题。缺席者将被视为对王座的不敬。{/i}"

    "继承法修订……你嗅到了阴谋的气味。"

    menu:
        "这对你意味着什么？"

        "这是一个机会——让其他贵族认识新的艾登堡领主。":
            $ change_stat("reputation", 3)
            "你决定把这次会议视为展示自己的舞台。"
            "在政治的棋盘上，你要让所有人记住你的名字。"

        "这是一个陷阱——有人想把所有贵族聚在一起，方便下手。":
            $ change_stat("intrigue", 3)
            "你的目光扫过信函上的每一个字，寻找隐藏的含义。"
            "把所有有权势的人聚在同一个地方……这本身就是最大的危险。"

        "这是一次考验——王后想看看你是否听话。":
            $ change_stat("power", 2)
            $ change_stat("intrigue", 1)
            "新继位的年轻领主，正是最容易被拿捏的对象。"
            "王后一定在观察你。问题是，你要表现得多顺从？"

    "你将信函折好，放入抽屉的暗格中。"

    if spy_network:
        "你的眼线已经在王都布下。等你到达时，关于各方势力的情报应该已经准备就绪。"
    else:
        "王都对你来说几乎是未知的领域。你需要在抵达前尽可能多地了解局势。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "少主，还有一件事。"

    "老管家的声音压得很低。"

    aldric "您父亲……在去世前几周，曾频繁与一个来自南方的商人通信。我在整理旧文书时发现了这些。"

    $ hide_all_chars()
    "他递上几张泛黄的纸条。字迹潦草，像是匆忙写就。"

    "大部分内容是关于货物交易的寻常通信，但有一行字格外醒目——"

    "{i}「货已备妥，待霜月交割。请务必亲至。」{/i}"

    "霜月。领主会议的时间。"

    menu:
        "这些信件说明什么？"

        "父亲可能有我不知道的秘密盟友。":
            $ change_stat("intrigue", 2)
            "在你继承领地之前，父亲就已经在编织某种网络。"
            "也许这张网现在可以为你所用。"

        "暂时收好，到了王都再调查。":
            $ change_stat("intrigue", 1)
            $ change_stat("power", 1)
            "你将纸条和王室信函放在一起，锁入暗格。"
            "有些谜题需要到正确的地方才能解开。"

        "交给奥尔德里克去追查这个商人。":
            $ change_rel("rel_aldric", 3)
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "我会尽力的，少主。"
            $ hide_all_chars()
            "老管家郑重地将纸条收好。对他而言，守护艾登堡家族的秘密已是毕生使命。"

    "窗外，第一片雪花飘落。"

    "冬天要来了。而你即将踏上前往王都的路。"

    "临行前，奥尔德里克送来了秋季的税收账册。你治下的几个村庄虽然不富裕，但粮税和工匠税的收入总算填上了一部分亏空。"
    $ change_stat("wealth", 3)

    "在那里，更大的风暴正在酝酿。"

    play sound "audio/sfx/page_turn.ogg"
    scene black with fade
    pause 1.0

    return

## ── 第二章 → 第三章 过渡 ──────────────────────────

label interlude_ch2_ch3:

    scene bg_road_night with dissolve
    play music "audio/music/forest_ambient.ogg" fadeout 2.0 fadein 3.0

    "从哈伦堡返回的路上，马车在泥泞的道路上颠簸前行。"

    "窗外起风了。初冬的寒意渗进石墙的每一道缝隙。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "领主大人，前方的桥被洪水冲毁了。我们需要绕道。"

    "队长雷恩骑马靠近马车窗口，雨水顺着他的铠甲流淌。"

    hide captain_img
    show player_char_img at left with dissolve
    player "绕道要多久？"

    hide player_char_img
    show captain_img at left with dissolve
    captain "走山路的话，多半天。但……"

    "他犹豫了一下。"

    captain "山路会经过暗林谷。那个地方……最近有些不太平。"

    menu:
        "你的决定？"

        "走山路，我们赶时间。":
            $ change_stat("courage", 5)
            captain "明白。弟兄们，戒备！"
            $ hide_all_chars()
            "车队转向山路。松林在两侧合拢，像一道黑色的幕墙。"

            "行至半途，你听到了远处的哭声。"

            "一个衣衫褴褛的女人跪在路边，怀里抱着一个孩子。"

            menu:
                "停下来查看。":
                    $ change_stat("loyalty", 3)
                    $ change_stat("reputation", 2)
                    "你命令车队停下。那女人名叫玛莎，是附近村庄的农妇。"
                    "她的村子遭了瘟疫。丈夫死了，她带着孩子逃出来，已经走了三天。"
                    "你让她上了马车，给了她干粮和水。"
                    hide captain_img
                    show player_char_img at left with dissolve
                    player "到了艾登堡，我会安排人照顾你。"
                    $ hide_all_chars()
                    "女人泪流满面地道谢。她不知道，她带来的消息将改变一切。"
                    "瘟疫。正从南方蔓延而来。"

                "不能停——这可能是陷阱。":
                    $ change_stat("intrigue", 3)
                    hide player_char_img
                    show captain_img at left with dissolve
                    captain "同意。这种手法太常见了。"
                    $ hide_all_chars()
                    "车队加速驶过。你回头看了一眼那个蜷缩的身影，心中五味杂陈。"
                    "但后来你听说了从南方传来的瘟疫消息。也许那个女人说的是真的。"

            ## 暗林谷伏击（山路才会遭遇）
            call interlude_ch2_ch3_ambush from _call_ambush_mountain

        "等洪水退了再走。安全第一。":
            $ change_stat("power", 2)
            "你命令车队在桥头扎营等待。"
            "雨下了一整夜。你在帐篷里借着烛光翻阅从王都带回的文件。"
            "其中一份引起了你的注意——南方几个领地报告了异常的死亡率。"
            "瘟疫。这个词像一道闪电划过你的脑海。"

    "无论你选择了哪条路，回到艾登堡时，坏消息已经在等着你了。"

    scene bg_castle_gate with dissolve

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "少主！您终于回来了！"

    "奥尔德里克的脸色苍白得吓人。"

    aldric "城外的村庄……出事了。有人病倒了，症状很奇怪。高烧、黑斑、咳血……"

    "你的心沉了下去。"

    hide aldric_img
    show player_char_img at left with dissolve
    player "有多少人？"

    hide player_char_img
    show aldric_img at left with dissolve
    aldric "目前知道的……至少二十人。而且每天都在增加。"

    if alliance_church:
        "你立刻想到了主教马修斯。教会的修道院或许有治疗的经验。"
    else:
        $ hide_all_chars()
        "你需要帮助。但在这个时候，能信任谁？"

    "你站在城堡的大门前，望向远方灰蒙蒙的天际线。"

    "领主会议上的权谋已经够让人头疼了。但命运似乎觉得这还不够。"

    "瘟疫来了。而你的领民在看着你。"

    play sound "audio/sfx/page_turn.ogg"
    scene black with fade
    pause 1.0

    return

## ── 第三章 → 第四章 过渡 ──────────────────────────

label interlude_ch3_ch4:

    scene bg_study_night with dissolve
    play music "audio/music/conspiracy.ogg" fadeout 2.0 fadein 3.0

    "雨季过去了。艾登堡的空气里多了泥土翻新的味道。"

    "一阵敲门声打断了你的沉思。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "打扰了，领主大人。"

    "艾琳娜走进书房，手中拿着一封信。她的表情比平时更为严肃。"

    elena "这封信是今晚刚到的。送信的人……骑了三天三夜没有停歇。马都跑死了。"

    $ hide_all_chars()
    "你接过信。蜡封上不是王室的百合纹章，而是一个你从未见过的标记——"

    "一只被锁链缠绕的鹰。"

    hide elena_img
    show player_char_img at left with dissolve
    player "这是谁的纹章？"

    hide player_char_img
    show elena_img at left with dissolve
    elena "弗雷德里克王子。"

    $ hide_all_chars()
    "你拆开信。王子的字迹凌乱而急促："

    "{i}致艾登堡领主：我被囚禁了。王后以「保护」之名将我软禁在秋水宫。她要对王国做出不可挽回的事。我需要能信任的人。如果你还记得父辈的誓约——请来。{/i}"

    "父辈的誓约。你的父亲与先王之间的承诺。"

    if father_letters_found:
        "你在父亲的遗物中见过类似的措辞。先王托付过你的父亲什么……而现在，这份托付落在了你身上。"
    else:
        "你不确定这个「誓约」具体指什么。但王子的语气中透着真实的恐惧。"

    menu:
        "面对王子的求救信："

        "立刻出发——如果信是真的，每耽搁一天都可能致命。":
            $ change_stat("courage", 5)
            $ change_rel("rel_prince", 5)
            "你起身抓起佩剑。"
            hide elena_img
            show player_char_img at left with dissolve
            player "备马。今夜出发。"
            hide player_char_img
            show elena_img at left with dissolve
            elena "领主大人！您不能一个人——"
            hide elena_img
            show player_char_img at left with dissolve
            player "我不是一个人。通知队长雷恩，挑选六名精锐随行。"

        "先核实消息——这可能是王后设下的圈套。":
            $ change_stat("intrigue", 5)
            "你将信反复翻看，甚至对着烛光检查是否有隐写的文字。"
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "这封信可能是伪造的。在确认之前，我不会贸然行动。"
            hide player_char_img
            show elena_img at left with dissolve
            elena "明智的选择。但如果是真的……"
            hide elena_img
            show player_char_img at left with dissolve
            player "那我们必须更加小心。让我们的人先去探探路。"

        "这不关我的事——我要保护自己的领地。":
            $ change_stat("power", 3)
            $ change_rel("rel_prince", -5)
            "你将信放下，揉了揉太阳穴。"
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "艾登堡刚经历了瘟疫，我的人民需要我在这里。"
            hide player_char_img
            show elena_img at left with dissolve
            elena "您确定吗？如果王子记恨——"
            hide elena_img
            show player_char_img at left with dissolve
            player "比起一个被囚禁的王子，我更担心领地的重建。"
            "但在接下来的几个夜晚，你总是会想起那封信上绝望的字迹。"

    if elena_romance:
        hide player_char_img
        show elena_img at left with dissolve
        elena "无论你做什么决定……请小心。"
        "她的目光中有你无法忽视的担忧。"
        hide elena_img
        show player_char_img at left with dissolve
        player "我会的。"
    else:
        hide player_char_img
        show elena_img at left with dissolve
        elena "局势越来越复杂了。"
        hide elena_img
        show player_char_img at left with dissolve
        player "从我继承这个位置的那一天起，就没有简单过。"

    $ hide_all_chars()
    "你走到窗前。远处窗口透出的暖光星星点点，庭院里安静得能听见自己的呼吸。"

    "奥尔德里克在你的书桌上留了一份简报：经过几个月的治理，领地的税收比去年同期增长了不少。"
    "至少在财政上，艾登堡正在从你父亲去世后的混乱中慢慢恢复。"
    $ change_stat("wealth", 5)

    "远处，王都的方向，仿佛有什么东西在等待着你。"

    "是命运？是陷阱？还是两者兼有？"

    "无论如何，你知道——平静的日子已经结束了。"

    play sound "audio/sfx/page_turn.ogg"
    scene black with fade
    pause 1.0

    return

## ── 第四章 → 第五章 过渡 ──────────────────────────

label interlude_ch4_ch5:

    play music "audio/music/revelation.ogg" fadeout 2.0 fadein 3.0
    scene bg castle_exterior with dissolve

    "回到艾登堡的第三天。"

    "你原以为回到自己的领地就能安心，但不安比在王都时更甚。"

    "消息像雪片一样飞来——"

    if dark_lily_destroyed:
        "「有人在王都城墙上发现了一些奇怪的标记。不过据说那个组织已经被铲除了。」"
        "传言总是落后几个月。但局势确实在变。"
    else:
        "「有人在王都城墙上发现了暗百合的标记。就画在王宫对面！」"

        if dark_lily_joined:
            "暗百合的动作比你想象的更大胆。"
        else:
            "暗百合。这个名字现在出现在了王都的城墙上。局势在加速恶化。"

    "「南方三个伯爵联名上书，要求召开紧急议会。」"

    $ change_stat("intrigue", 2)

    "你正在书房里消化这些情报，门外传来急促的脚步声。"

    scene bg_castle_gate with dissolve

    "你赶到城门口。奥尔德里克已经在那里了。他身边站着一个你不认识的人。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "少主，这位是……"

    $ hide_all_chars()
    "那人向前一步，行了一个标准的王室礼节。"

    "「艾登堡领主大人。我是王后陛下的特使。奉命传达王后的旨意。」"

    "他展开一卷羊皮纸："

    "{i}鉴于近日之种种变故，王后陛下决定对边境诸领地实行特别监管。自即日起，各领主需每月向王都呈报领地事务，接受王室督查官的定期巡视。特此通告。{/i}"

    "特别监管。换个说法——王后在收紧控制。"

    menu:
        "面对王后的特使："

        "恭敬地接受旨意。":
            $ change_rel("rel_queen", 3)
            $ change_stat("power", -3)
            hide aldric_img
            show player_char_img at left with dissolve
            player "请转告王后陛下，艾登堡永远忠于王座。"
            $ hide_all_chars()
            "特使满意地点头离去。"
            "但你知道，每一份报告都将是一场精心设计的表演——向王后展示她想看到的，隐藏她不该知道的。"

        "提出异议但不拒绝。":
            $ change_stat("reputation", 3)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "这份旨意……是否适用于所有领地？还是只有边境？"
            $ hide_all_chars()
            "特使脸上闪过一丝不悦。"
            "「所有边境领地，领主大人。这是为了王国的安全。」"
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我理解。但我希望我的异议能被记录在案。"
            "你接过羊皮纸，但你的态度表明了一切。"

        "当面拒绝——这超越了王后的权限。":
            $ change_stat("courage", 5)
            $ change_rel("rel_queen", -8)
            $ change_stat("reputation", 3)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "根据先王颁布的《领地自治法》，王室无权对领地实施单方面监管。"
            $ hide_all_chars()
            "特使的脸色变了。"
            "「领主大人，我劝您——」"
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "请转告王后：艾登堡尊重王座，但不接受违法的命令。"
            $ hide_all_chars()
            "特使冷冷地看了你一眼，转身离去。"
            "这意味着战争。不是刀剑的战争，而是更危险的那种。"

    "特使离开后，你站在城门前沉思。"

    if queen_trust:
        "你曾以为可以和王后建立某种信任。但这道旨意打碎了你的幻想。"
    else:
        "王后的敌意比你预想的来得更快。你需要为接下来的暴风雨做好准备。"

    hide player_char_img
    show aldric_img at left with dissolve
    aldric "少主……"

    "老管家欲言又止。你转向他。"

    hide aldric_img
    show player_char_img at left with dissolve
    player "说。"

    hide player_char_img
    show aldric_img at left with dissolve
    aldric "您不在的这些天，领地里发生了一些事。"

    "他的声音沉重得像铅。"

    aldric "有三个村庄的村长联名写了请愿书。他们要求……领主大人亲自处理几桩积压已久的事务。"

    aldric "还有，修道院报告说……有修士看到了奇怪的人在墓地附近徘徊。每到月圆之夜就会出现。"

    if father_letters_found:
        $ hide_all_chars()
        "墓地。你父亲就葬在那里。"
        "有人在深夜造访你父亲的墓……这绝不是巧合。"
    else:
        "墓地？你皱起眉头。在这个节骨眼上，任何异常都值得警惕。"

    "你推开城堡的大门。"

    "王都的权力游戏、王后的步步紧逼、领地内部的暗流涌动——"

    "所有的线索都在指向一个终点。"

    "而你，站在这一切的中心。"

    "最后的抉择，已经近在眼前。"

    play sound "audio/sfx/page_turn.ogg"
    scene black with fade
    pause 1.0

    return

## ============================================================
## 章间深度子场景 — 四段被call调用的扩展叙事
## ============================================================

## ── 第一章后的梦境 ──────────────────────────────────

label interlude_ch1_ch2_dream:

    scene black with dissolve
    play music "audio/music/night_mystery.ogg" fadeout 2.0 fadein 3.0

    "你不记得自己是什么时候睡着的。"

    "烛火在某个时刻熄灭了，黑暗像潮水一样涌进书房，然后——"

    "你开始做梦。"

    scene bg_study_night with dissolve

    "父亲的书房。一切都和你记忆中一模一样。"

    "橡木书架上摆满了皮革封面的典籍，空气中弥漫着墨水和松脂的气息。一切都和你记忆中一模一样——连桌角那个磨出毛边的墨水瓶都没挪过位置。"

    "你站在门口，像小时候那样——不敢打扰，又舍不得离开。"

    "父亲坐在书桌前，背对着你。他的肩膀比你记忆中要瘦削得多。"

    "他在写信。鹅毛笔的沙沙声在寂静的房间里格外清晰。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "父亲……？"

    "他没有回头。但他开口了。"

    if father_death_known:

        "他的声音疲惫而沉重，像是一个已经知道自己时日无多的人。"

        hide player_char_img
        show aldric_img at left with dissolve
        aldric "你来了。"

        $ hide_all_chars()
        "不——那不是奥尔德里克的声音。是父亲的。在梦里，所有的声音都混在一起。"

        "他缓缓转过身来。你看到了他的脸——苍白如纸，眼眶深陷，嘴唇上带着一层不自然的灰紫色。"

        "暮色之露。你现在知道了那是什么——艾琳娜在地窖里给你看过的那个泛绿色的瓶子。"

        "父亲看着你，目光中没有愤怒，没有恐惧——只有一种深沉的悲哀。"

        "「你已经知道了，是吗？」"

        "他的声音像是从很远很远的地方传来。"

        "「真相是一把双刃剑，孩子。它给你力量，也给你枷锁。」"

        "他将手中的信折好，放入一个你从未见过的暗格中。"

        "「我留下的东西……不是为了让你复仇。是为了让你活下去。」"

        "火焰突然变成了深紫色，整个书房开始扭曲。书架上的书一本接一本地坠落，每一本打开的书页上都写满了同一个词——"

        "「{b}暮色之露{/b}」"

        "父亲的身影开始消散，像雾气被风吹散。"

        "「别信任任何人。」"

        "「但也别……独自一人。」"

    else:

        "他的声音平静而温和，和你记忆中的每一个夜晚一样。"

        "「还没睡？」"

        "你想走近，但双脚像是被钉在了地板上。"

        hide aldric_img
        show player_char_img at left with dissolve
        player "您在写什么？"

        $ hide_all_chars()
        "他停下笔，似乎在斟酌措辞。"

        "「给一个老朋友的信。关于……一些陈年旧事。」"

        "他站起身，走到窗边。夜色映出他的侧脸轮廓，你注意到他的鬓角比你印象中白了许多。"

        "「有些事情，我应该早点告诉你的。但我总觉得你还小，总觉得还有时间。」"

        "他叹了口气。"

        "「时间是最大的骗子。它让你以为明天永远会来。」"

        "他转向你，目光中有某种你读不懂的东西——像是歉疚，又像是警告。"

        "「书桌的第三个抽屉，最底下，有一层假底。」"

        "「如果有一天你需要答案——去那里找。」"

        "火焰突然跳动了一下，书房里的光线忽明忽暗。父亲的身影变得模糊，像是隔着一层水帘。"

        "「照顾好艾登堡。照顾好……你自己。」"

    "你伸出手想要抓住他，但你的手穿过了他的身体，只触到了冰冷的空气。"

    scene black with vpunch

    "你猛地醒了过来。"

    pause 0.5

    scene bg_bedroom with dissolve

    "心跳如鼓。额头上全是冷汗。"

    "窗外，东方刚刚泛起一线灰白。凌晨时分，万籁俱寂。"

    "你呆坐在床上，梦中的一切仍然清晰得像是真实的记忆。"

    "然后你感觉到了——枕头下面，有什么硬硬的东西硌着你的后脑勺。"

    "你掀开枕头。"

    "一枚铜质徽章静静地躺在那里。"

    "它不大，只有拇指甲盖大小。正面是一只展翅的鹰——和父亲书房里挂着的那幅家族纹章一模一样。"

    "但背面刻着一行极小的字，需要凑到烛光前才能勉强辨认："

    "{i}「吾之血脉，吾之誓约。格里菲斯七世亲授。」{/i}"

    "先王……亲授？"

    "你翻来覆去地看着这枚徽章。它怎么会在你的枕头下？是奥尔德里克放的？还是……一直都在，只是你从未注意？"

    "无论如何，这枚徽章证明了一件事——你的父亲与先王之间，有着比你所知更深的联系。"

    menu:
        "这枚徽章意味着什么？"

        "这是一份信物——也许能用来证明身份或兑现某种承诺。":
            $ change_stat("intrigue", 3)
            $ change_stat("power", 2)
            "你将徽章小心地收入贴身的口袋。"
            "在这个充满谎言的世界里，一件实物的证据比千言万语更有分量。"
            "也许有一天，当你面对先王的血脉时，这枚徽章就是你最好的敲门砖。"

        "这是一个警告——父亲想告诉我，有些承诺比性命更重。":
            $ change_stat("courage", 3)
            $ change_stat("loyalty", 2)
            "你握紧徽章，感受着铜质的冰凉慢慢被掌心捂热。"
            "父亲为了守护某个承诺，付出了一切。这枚徽章是他留给你的遗志。"
            "你不知道自己是否有他那样的勇气。但你知道你必须试试。"

        "先不声张——在弄清楚之前，不能让任何人知道这枚徽章的存在。":
            $ change_stat("intrigue", 4)
            $ change_stat("faith", 1)
            "你用一条旧手帕将徽章层层包好，藏入床头暗格的最深处。"
            "梦也好，父亲的遗物也好——在你弄清楚一切之前，这将是你一个人的秘密。"
            "有时候，沉默本身就是最强大的武器。"

    "窗外的天色渐渐亮了起来。"

    "你用冷水洗了把脸，把梦的余温从皮肤上洗去。"

    "但那枚徽章的重量，始终贴在你的心口。"

    "父亲在梦中说的话——无论是真是幻——你决定记住每一个字。"

    "新的一天开始了。而你的肩上，又多了一个秘密。"

    return

## ── 第二章后的伏击事件 ──────────────────────────────

label interlude_ch2_ch3_ambush:

    scene bg_road_night with dissolve
    play music "audio/music/battle_prepare.ogg" fadeout 1.0 fadein 2.0

    "车队进入暗林谷后，气氛骤然变了。"

    "松林遮蔽了最后一丝月光。道路两旁的树木像沉默的哨兵，枝桠在风中发出嘎吱嘎吱的声响。"

    "你注意到队长雷恩的手已经按在了剑柄上。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "都打起精神来。这地方我不喜欢。"

    $ hide_all_chars()
    "他的声音压得很低，但在寂静的夜里，每一个字都清晰无比。"

    "你正要说什么，突然——"

    "一支箭从左侧的黑暗中射出，钉在了马车门框上，箭尾嗡嗡颤抖。"

    "如果你的头再偏三寸，那支箭就插进了你的太阳穴。"

    play sound "audio/sfx/sword_clash.ogg"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "伏击！全体戒备！保护领主！"

    "黑暗中爆发出一阵呐喊声。火把从树林两侧同时亮起，将整个山谷照得忽明忽暗。"

    if dark_lily_joined:

        $ hide_all_chars()
        "你在火光中看清了袭击者的面容——黑色面罩，轻便的皮甲，腰间别着淬毒的短刀。"

        "这不是山贼。山贼不会有这种装备，也不会有这种训练有素的包抄阵型。"

        "暗焰。暗百合三派中最激进的那一派。"

        $ darkflame_known = True

        "你加入了暗百合，但暗焰不服。冯·哈根男爵的人——他们在清除异己。"

        "领头的暗焰刺客一个翻身跃上马车顶部，短刀在月光下闪出寒芒。"

        "「男爵大人说了——这条路上不需要第二个声音。」"

        "他的刀直刺你的喉咙。"

    else:

        "袭击者大约有二十人。他们穿着破旧的皮衣，手持各种杂七杂八的武器——铁锤、镰刀、生锈的长剑。"

        "看起来是山贼。但山贼会在官道上伏击一支武装护卫队吗？"

        "为首的是一个独眼大汉，满脸横肉，嘴里叼着一根草棍。"

        "「把值钱的东西都留下！要钱不要命！」"

        "但你注意到了——他腰带上挂着的皮袋里，隐约露出一角黑色丝绸。"

        "暗百合的信物。"

        "这些「山贼」，是有人花钱雇来的。"

    captain "保持阵型！"

    "雷恩拔剑迎上了第一波攻击。"

    "你从未在真正的战场上见过雷恩。在城堡里，他只是一个沉默寡言的中年军人，总是站在你身后两步远的地方。"

    "但此刻——"

    "他的剑像一道银色的闪电。第一个冲上来的袭击者甚至没看清他的动作，就已经捂着手腕倒在了地上。"

    "第二个从侧面扑来，雷恩不回头，反手一剑，剑脊拍在对方的膝盖上，骨裂的声音清晰可闻。"

    "第三个、第四个——雷恩像一堵移动的铁壁，挡在马车和袭击者之间。"

    "他的剑法没有花哨的招式，每一击都精准、狠辣、致命。这是在真正的战场上磨练出来的技艺。"

    captain "领主大人，低下头！"

    "你本能地伏下身体。一支箭从你头顶掠过。"

    "雷恩顺着箭来的方向掷出一把匕首。树林中传来一声惨叫，接着一个身影从树枝上跌落。"

    "战斗激烈而混乱。你的护卫们训练有素，但袭击者在数量上占优。"

    "一个袭击者绕过了防线，出现在了马车的另一侧。你与他四目相对。"

    "他举起了一把锈迹斑斑的短斧，眼里闪着贪婪和凶狠的光。"

    menu:
        "危急时刻——"

        "拔剑迎战——你不是手无缚鸡之力的书生。":
            $ change_stat("courage", 5)
            $ change_rel("rel_captain", 3)
            "你抽出随身的短剑，跳下马车。"
            "对方显然没料到一个贵族少爷会主动迎战。他愣了一瞬——而这一瞬就是致命的。"
            "你记得奥尔德里克教你的第一课：不要等对手准备好。"
            "你一剑刺出，对方慌忙格挡。短斧和短剑碰撞的火花溅在你脸上。"
            "你不是他的对手——你知道。但你只需要撑到——"
            captain "滚开！"
            "雷恩的剑从侧面斩来，将那人劈倒在地。"
            captain "好胆量，领主大人。但下次请留在马车里。"
            "他嘴上这么说，但拍了拍你的肩，力道比平时重。"

        "抓起马车里的弩——远程反击更明智。":
            $ change_stat("intrigue", 3)
            $ change_rel("rel_captain", 3)
            "你扑向马车角落的武器箱，翻出那把旅行弩。"
            "装填。瞄准。扣扳机。"
            "弩矢嗡地一声射出，钉进了那人的肩膀。他惨叫着跌倒。"
            "你又装了一发，转向另一个方向。在这场混战中，你至少射倒了三个敌人。"
            captain "好射术！"
            "雷恩在混战中朝你点了点头。有一个能自保的领主，比什么都让护卫安心。"

        "大声呼喊身份——告诉他们攻击领主的后果。":
            $ change_stat("power", 3)
            $ change_stat("reputation", 3)
            hide captain_img
            show player_char_img at left with dissolve
            player "我是艾登堡领主！攻击我就是对王座宣战！你们每一个人都将被处以绞刑！"
            $ hide_all_chars()
            "你的声音在山谷中回荡。"
            "几个袭击者明显犹豫了。一个年轻的甚至开始后退。"
            "他们可能是拿钱办事，但没人愿意为了几个金币搭上全家的性命。"
            "混乱中，有人喊道：「撤！不值当！」"
            "一部分袭击者开始溃逃。但最顽固的几个仍然在战斗。"
            hide player_char_img
            show captain_img at left with dissolve
            captain "说得好，领主大人。但还是躲好——"
            $ hide_all_chars()
            "雷恩解决了最后两个不长眼的家伙。"

    "战斗在几分钟内结束了。"

    "地上躺着七八个袭击者。你的护卫有两人受了轻伤，一匹马被箭射中了腿。"

    "雷恩擦了擦剑上的血，走到你身边。他的呼吸平稳得令人惊讶，仿佛刚才的一切不过是一次例行巡逻。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "都结束了，领主大人。"

    hide captain_img
    show player_char_img at left with dissolve
    player "雷恩……谢谢你。"

    "他似乎不太习惯被感谢。过了一会儿，才开口。"

    hide player_char_img
    show captain_img at left with dissolve
    captain "这是我的职责。您父亲在世时，我发过誓——守护艾登堡的每一位主人。"

    captain "您父亲也曾被伏击过，不止一次。"

    hide captain_img
    show player_char_img at left with dissolve
    player "他怎么应对的？"

    hide player_char_img
    show captain_img at left with dissolve
    captain "和您一样——没有退缩。"

    "他的语气中有一丝微不可察的温度。"

    captain "您比我预想的更像他。"

    $ change_rel("rel_captain", 5)

    "你命令护卫搜查袭击者的尸体和物品。"

    if dark_lily_joined:
        $ hide_all_chars()
        "正如你所料——暗焰的标记无处不在。毒药、密码本、以及一封写着你名字的处决令。"
        "冯·哈根男爵比你想象的更急于除掉你。"
        $ change_rel("rel_baron", -5)
    else:
        "在领头者的尸体上，你找到了一个皮袋。里面是五十枚金币和一张纸条。"
        "纸条上只有三个字：{i}「杀了他。」{/i}"
        "字迹陌生。但那些金币上铸着王都的徽记——这种成色的金币，只有在王都的钱庄才能铸造。"
        "有人从王都出钱买你的命。"

    "车队重新上路。"

    "你坐在马车里，手里攥着从袭击者身上搜到的证据。"

    "夜色中，松林沙沙作响，仿佛在低语着什么。"

    "你看了一眼骑在马车旁边的雷恩。他的目光警惕地扫视着四周，剑始终没有还鞘。"

    "有这样一个人在身边——你突然觉得，这条危机四伏的路，并不像之前想的那么难走。"

    hide captain_img with dissolve

    return

## ── 第三章后elena的坦白 ──────────────────────────────

label interlude_ch3_ch4_confession:

    if elena_identity_exposed_known:
        return

    scene bg_study_night with dissolve
    play music "audio/music/conspiracy.ogg" fadeout 2.0 fadein 3.0

    "那天晚上，你处理完一天的公务，正准备吹灭蜡烛。"

    "门外传来两声轻叩。不是奥尔德里克那种稳重的叩门方式——更轻，更犹豫。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "进来。"

    $ hide_all_chars()
    "艾琳娜推门而入。她没有穿平时那件深蓝色的管事裙装，而是一件朴素的灰色斗篷，兜帽半掩着她的面容。"

    "她反手关上门，顿了一下，才转过身来。"

    "烛光下，你看到她的眼睛微微发红——像是哭过，又拼命忍住了。"

    hide player_char_img
    show elena_img at left with dissolve
    elena "领主大人……我有些话，必须今晚告诉你。"

    "她的声音比平时低了许多，少了那种惯常的从容和精明。"

    elena "如果明天之后你不再信任我，我……能理解。"

    hide elena_img
    show player_char_img at left with dissolve
    player "坐下说。"

    "你指了指壁炉旁的椅子。她犹豫了一下，在椅子边缘坐下，身体前倾，双手紧紧绞在一起。"

    hide player_char_img
    show elena_img at left with dissolve
    elena "你知道我是间谍。这不是秘密——至少，不再是了。"

    elena "但你不知道的是……我从来不只为一个主人工作。"

    "她咬了下嘴唇内侧。"

    elena "暗百合、王后、你父亲——在过去五年里，我同时为三方传递消息。"

    elena "暗百合以为我是他们安插在艾登堡的眼线。王后以为我是她渗透暗百合的棋子。"

    elena "而你的父亲……"

    "她停顿了很长时间。窗外有风刮过，把窗框吹得嘎吱响了两声。"

    elena "你的父亲是唯一知道全部真相的人。是他安排了这一切。"

    hide elena_img
    show player_char_img at left with dissolve
    player "……什么？"

    hide player_char_img
    show elena_img at left with dissolve
    elena "你父亲从一开始就知道暗百合会往他身边安插人手。与其被动等待，不如主动选择——所以他通过秘密渠道联系了暗百合，'请求'他们派一个情报员来。"

    elena "那个人就是我。但在我被暗百合'派遣'到艾登堡的第一天，你父亲就把我叫进了这间书房。"

    elena "他什么都知道。我的真实身份，我的联络暗号，甚至我在暗百合中的代号——「细雨」。"

    elena "他给了我一个选择：被揭穿然后消失，或者……成为他真正的眼睛和耳朵。"

    elena "我选择了后者。从那天起，我成了三重间谍——对外是暗百合的人，对王后是渗透暗百合的棋子，但真正效忠的是你父亲。"

    $ elena_spy_known = True
    $ elena_identity_exposed_known = True

    hide elena_img
    show player_char_img at left with dissolve
    player "那现在呢？父亲已经不在了。"

    "这个问题像一把刀，切入了房间里最后一层伪装。"

    hide player_char_img
    show elena_img at left with dissolve
    elena "……"

    if elena_romance:

        "她抬起头看着你。那双一向精明冷静的眼睛里，此刻满是脆弱。"

        elena "你知道答案的。"

        $ hide_all_chars()
        "你确实知道。在那些深夜的交谈中，在那些目光交错的瞬间，在她每一次拼命隐藏又拼命流露的温柔里——"

        "你早就知道了。"

        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "我留下来不是因为你父亲的安排。不是因为暗百合。不是因为任何使命或者义务。"

        elena "我留下来……是因为你。"

        "她的声音终于颤抖了。"

        elena "我知道这很愚蠢。一个间谍不应该对任何人产生感情。这是我们的第一条戒律。"

        elena "但有些事情……不是戒律能管得了的。"

        "壁炉的火映在她脸上，像一层淡淡的金色面纱。你从未见过她这样的表情——所有的伪装和盔甲都卸下了，只剩下一个疲惫的、害怕的、却又无比真诚的女人。"

    else:

        elena "你父亲临终前，通过奥尔德里克给我传了最后一句话。"

        elena "他说：「守护我的孩子。这是我对你最后的请求。」"

        elena "所以我留了下来。不是为了暗百合，不是为了王后。是为了你父亲的遗愿。"

        elena "但你有权知道真相。你有权选择——继续用我，还是让我离开。"

    $ hide_all_chars()
    "炉火噼啪声像是时钟在走。你在消化这一切。"

    "你在消化这一切。五年。三方势力。一个在所有人之间走钢丝的女人。"

    "而你的父亲，是那个在暗中操纵全局的人。"

    hide elena_img
    show player_char_img at left with dissolve
    player "暗百合现在认为你的忠诚在哪里？"

    hide player_char_img
    show elena_img at left with dissolve
    elena "他们不确定。你父亲死后，我中断了联络。他们派过人来试探，但我没有回应。"

    elena "这意味着他们迟早会做出判断——我要么还是他们的人，要么已经叛变。如果是后者……"

    "她做了一个抹脖子的手势。"

    elena "但这不是最紧迫的。"

    "她从斗篷内侧取出一个小小的蜡封纸卷。"

    elena "这是我最后一次从王都得到的消息。两天前到的。"

    $ hide_all_chars()
    "你展开纸卷。上面只有寥寥几行字，但每一行都像一记重锤："

    "{i}「王后正在秘密组建一支直属军队。兵员从南方各省招募，不经过正规军事系统。预计兵力三千到五千。」{/i}"

    "{i}「目标未知。但集结地点在王都以北三十里的猎鹰堡。」{/i}"

    "{i}「时间——入冬之前。」{/i}"

    "猎鹰堡。那个位置，正好卡在王都通往北方诸领地的必经之路上。"

    "包括通往艾登堡的路。"

    hide elena_img
    show player_char_img at left with dissolve
    player "入冬之前……还有多少时间？"

    hide player_char_img
    show elena_img at left with dissolve
    elena "最多六周。"

    menu:
        "面对这个情报——"

        "全面备战——如果王后要动手，我们必须做好准备。":
            $ change_stat("power", 4)
            $ change_rel("rel_elena", 3)
            $ change_stat("intrigue", 1)
            hide elena_img
            show player_char_img at left with dissolve
            player "从明天开始，征召后备民兵。加固城墙。储备粮草和箭矢。"
            hide player_char_img
            show elena_img at left with dissolve
            elena "这会引起王后的注意。她会知道你已经得到了消息。"
            hide elena_img
            show player_char_img at left with dissolve
            player "让她知道。有时候，展示力量本身就是最好的威慑。"
            hide player_char_img
            show elena_img at left with dissolve
            elena "……明白了。我会帮你拟定防御方案。"
            "她的声音里多了一分笃定——像是终于找到了可以依靠的支点。"

        "秘密联络其他领主——一个人对抗王后是自杀。":
            $ change_stat("intrigue", 4)
            $ change_rel("rel_elena", 5)
            hide elena_img
            show player_char_img at left with dissolve
            player "这份情报，你能确认准确度吗？"
            hide player_char_img
            show elena_img at left with dissolve
            elena "我的消息来源从未出过错。"
            hide elena_img
            show player_char_img at left with dissolve
            player "好。我需要你帮我做一件事——秘密联络北方三领的领主。告诉他们，猎鹰堡的事。"
            hide player_char_img
            show elena_img at left with dissolve
            elena "你要组建联盟？"
            hide elena_img
            show player_char_img at left with dissolve
            player "王后可以碾碎一个领地。但五个领地联合起来……那就是另一回事了。"
            hide player_char_img
            show elena_img at left with dissolve
            elena "这很危险。如果消息走漏——"
            hide elena_img
            show player_char_img at left with dissolve
            player "这就是为什么我需要你。只有你能做到不留痕迹。"
            "她看着你，缓缓点了点头。"

        "先确认消息——贸然行动可能正中圈套。":
            $ change_stat("intrigue", 5)
            $ change_rel("rel_elena", 2)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "这也可能是假消息。故意泄给你，看我们的反应。"
            hide player_char_img
            show elena_img at left with dissolve
            elena "你怀疑是陷阱？"
            hide elena_img
            show player_char_img at left with dissolve
            player "我怀疑一切。这是你教我的。"
            "她微微一怔，然后露出了一个苦涩的微笑。"
            hide player_char_img
            show elena_img at left with dissolve
            elena "好的学生。那……你要我重新联络王都的线人？"
            hide elena_img
            show player_char_img at left with dissolve
            player "小心行事。不要暴露你还活跃着。像一条蛰伏的蛇——只看，不动。"
            hide player_char_img
            show elena_img at left with dissolve
            elena "明白。"

    "你将纸卷放在蜡烛上点燃，看着它在指尖化为灰烬。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "还有一件事。"

    "她站起身，走到你身前。"

    elena "无论你最终如何看待我——间谍也好，骗子也好——有一件事是真的。"

    elena "你父亲是一个了不起的人。而你……正在成为和他一样的人。"

    if elena_romance:
        "她伸出手，轻轻碰了一下你的手背。只是一瞬间，但那份温度像烙印一样留了下来。"
        elena "小心。"
        "她转身走向门口，在门槛处停了一下，没有回头。"
        elena "晚安。"
    else:
        "她理了理衣袖，恢复了平时那种干练的姿态。"
        elena "我会继续为艾登堡效力。直到你不再需要我的那一天。"
        $ hide_all_chars()
        "她退出书房，轻轻带上了门。"

    "你独自坐在书房里，目光落在桌上摊开的地图上。"

    "三千到五千人的军队。王后的秘密力量。猎鹰堡。六周。"

    "棋盘上的局面越来越清晰了——也越来越危险了。"

    "你需要盟友。你需要力量。你需要……时间。"

    "而时间，正是你最缺的东西。"

    hide elena_img with dissolve

    return

## ── 第四章后的紧急会议 ──────────────────────────────

label interlude_ch4_ch5_council:

    scene bg_castle_gate with dissolve
    play music "audio/music/revelation.ogg" fadeout 2.0 fadein 3.0

    "你回到艾登堡时，城堡大门前站满了人。"

    "不是迎接的欢呼——是焦虑的等待。"

    "奥尔德里克、队长雷恩，还有十几个面色凝重的管事和军官。"

    "他们的表情告诉你——出事了。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "少主，您可算回来了。"

    hide aldric_img
    show player_char_img at left with dissolve
    player "发生了什么？"

    if first_decree == "军事":
        "奥尔德里克的声音沉重如铁。"
        hide player_char_img
        show aldric_img at left with dissolve
        aldric "您下令扩充的民兵……出了问题。三个村庄拒绝交出征召名额。他们说——您把他们的儿子送去当兵，田里的庄稼就没人收了。"
        aldric "更糟的是，有人在煽动。有个来路不明的人在村子里散布谣言，说您要用农民的血来换贵族的权力。"
        "你心中一沉。内部的裂痕，有时比外敌更致命。"

    elif first_decree == "economy":
        aldric "您推行的商税改革引发了反弹。三家最大的商会联合抵制新税制，他们封锁了通往艾登堡的主要商路。"
        aldric "市场上的粮价在三天内涨了两倍。如果再持续一周，城里就要断粮了。"
        "一场没有刀剑的围城战。那些商人比你想象的更有手段。"

    else:
        aldric "南边的两个村庄爆发了冲突。一个村子的水源被上游的村子截断，双方从口角升级到了械斗。"
        aldric "已经有三人重伤。如果不及时处理，恐怕会演变成更大的骚乱。"
        "内忧。在外患逼近的时候，你的领地自己先乱了。"

    hide aldric_img
    show player_char_img at left with dissolve
    player "召集所有人到大厅。立刻。"

    scene bg_castle_corridor with dissolve

    "一刻钟后，大厅里坐满了人。"

    "奥尔德里克坐在长桌的右侧，面前摊开着账册和文书。"

    "队长雷恩站在门口，全副武装——他永远是最后一个坐下的人。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "领主大人，边境巡逻队也带回了消息。"

    captain "北方蛮族的斥候被我们的巡逻队发现了。不是一个两个——是成群的。"

    captain "他们在探路。这意味着大部队不远了。"

    $ hide_all_chars()
    "你的脑海中闪过那份关于王后秘密军队的情报。南边是王后的猎鹰堡，北边是蛮族的铁蹄——"

    "艾登堡夹在中间。"

    if alliance_church:
        "门被推开，主教马修斯走了进来。他的白色法袍在火把光中几乎发光。"

        hide captain_img
        show bishop_img at left with dissolve
        bishop "上帝保佑，我来晚了。"

        "他在长桌末端坐下，双手交握，目光沉静。"

        bishop "修道院已经收到了南方教区的通报。各地都在准备……'大斋戒'。"

        "大斋戒——教会的暗语，意思是战争即将来临。"

        bishop "教会无法公开站队。但艾登堡的信徒们……可以做好他们自己的准备。"
    else:
        $ hide_all_chars()
        "你环顾大厅。主教没有来。教会在这个时候保持沉默——这本身就是一种态度。"
        "你只能依靠自己人了。"

    hide bishop_img
    show aldric_img at left with dissolve
    aldric "少主，我整理了一份报告。"

    "他展开一张长长的羊皮纸。"

    aldric "粮食储备：以当前人口计算，可支撑两个月。如果算上可能涌入的难民，缩短到六周。"
    aldric "武器装备：长矛两百杆，弓箭充足，但铠甲严重不足。正规守军加上民兵，总兵力约四百人。"
    aldric "城墙状况：北墙在去年的暴风雨中受损，修缮工程只完成了三分之二。"

    hide aldric_img
    show captain_img at left with dissolve
    captain "四百人。守一座城，勉强够。但如果敌人超过两千……"

    "他没有说完。不需要说完。每个人都知道那意味着什么。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我们有三个问题需要解决。"

    "你站起身，手掌按在地图上。"

    player "第一——领地内部的乱子必须平息。第二——北墙必须修完。第三——我们需要更多的兵员和物资。"

    player "这三件事不能一件一件来。必须同时进行。"

    "所有人都看着你，等你分配任务。"

    menu:
        "最优先的资源应该投入哪里？"

        "军事优先——修城墙、扩军、打造武器。没有防御，一切都是空谈。":
            $ change_stat("power", 5)
            $ change_stat("loyalty", -2)
            $ change_stat("wealth", -3)
            player "雷恩，我授权你征调所有可用的劳力来修北墙。工匠、农夫——所有人。"
            hide player_char_img
            show captain_img at left with dissolve
            captain "明白。但这会影响秋收——"
            hide captain_img
            show player_char_img at left with dissolve
            player "如果敌人攻破城墙，秋收的粮食也保不住。"
            hide player_char_img
            show aldric_img at left with dissolve
            aldric "少主……百姓们会有怨言的。"
            hide aldric_img
            show player_char_img at left with dissolve
            player "我知道。但活着的人才有资格抱怨。"
            "你的声音斩钉截铁。大厅里没有人再反对。"

            if alliance_church:
                hide player_char_img
                show bishop_img at left with dissolve
                bishop "教会可以派修士去安抚民众。至少……让他们知道这是为了保护所有人。"
                hide bishop_img
                show player_char_img at left with dissolve
                player "谢谢你，主教。"

            $ hide_all_chars()
            "从第二天开始，艾登堡变成了一座巨大的工地。"
            "铁匠日夜不停地打造箭头和矛尖。城墙上的缺口一寸一寸地被填补。"
            "百姓们虽有怨言，但当他们看到领主亲自搬运石块时，声音渐渐小了。"

        "民生优先——先解决内部矛盾，赢得民心。军心来自民心。":
            $ change_stat("loyalty", 5)
            $ change_stat("power", -2)
            $ change_stat("reputation", 3)
            player "奥尔德里克，我要亲自去那几个闹事的村子。"
            hide player_char_img
            show aldric_img at left with dissolve
            aldric "少主，现在外出很危险——"
            hide aldric_img
            show player_char_img at left with dissolve
            player "我不去，那些村子的人就会觉得我不在乎他们。一个不在乎百姓的领主，不值得百姓为他守城。"

            $ hide_all_chars()
            "你当场拍板：议事一散，你就启程，亲自去那几个出事的村庄。"
            "倾听每一个抱怨。坐在农舍的长凳上和老人们喝粗茶。抱起生病的孩子。"
            "不做不切实际的承诺，但要让他们知道——你看见了他们。"

            "等村长拉着你的手说"开口就是"那一刻，比任何盔甲都更稳固艾登堡的脚跟。"

            if alliance_church:
                hide player_char_img
                show bishop_img at left with dissolve
                bishop "这才是真正的领袖。上帝保佑仁慈的统治者。"
                "主教当场承诺，让教会的修士陪同你一同走访，安抚民心。"

        "经济优先——没有钱粮，军队和民心都是空话。":
            $ change_stat("wealth", 5)
            $ change_stat("power", -2)
            $ change_stat("intrigue", 2)
            hide bishop_img
            show player_char_img at left with dissolve
            player "奥尔德里克，打开父亲的战时储备金。"
            hide player_char_img
            show aldric_img at left with dissolve
            aldric "少主……那是您父亲留给最危急时刻的——"
            hide aldric_img
            show player_char_img at left with dissolve
            player "现在还不够危急吗？"
            $ hide_all_chars()
            "老管家深吸了一口气。然后他点了点头，从怀中取出一把铁钥匙。"

            "城堡地下室的尽头，一扇从未打开过的铁门在钥匙的转动下缓缓开启。"
            "里面是六箱金币、三箱银币，以及——"
            "一批密封完好的武器。长弓、连弩、甚至两套精钢板甲。"
            hide player_char_img
            show aldric_img at left with dissolve
            aldric "您的父亲……一直在为这一天做准备。"
            hide aldric_img
            show player_char_img at left with dissolve
            player "……他比我想象的看得更远。"

            $ hide_all_chars()
            "你用这笔财富打通了几条关键的商路，从南方紧急采购了粮食和铁矿。"
            "同时，你秘密派人收买了几个关键的消息灵通人士——你需要知道敌人的一举一动。"

            if alliance_church:
                hide player_char_img
                show bishop_img at left with dissolve
                bishop "教会的粮仓也可以在紧急时刻开放。算是……上帝对艾登堡的馈赠。"
                hide bishop_img
                show player_char_img at left with dissolve
                player "主教大人，这份恩情我记在心里。"

    $ hide_all_chars()
    "会议持续到了深夜。"

    "当最后一个人离开大厅时，你独自站在地图前。"

    "地图上标注着艾登堡的每一寸土地——村庄、农田、山脉、河流、道路。"

    "你用手指描着北方的边界线。那条线的另一边，是无尽的荒原和即将南下的铁蹄。"

    "你又描了描南方的道路。那条路的尽头，是王都——和一个正在磨刀的王后。"

    hide player_char_img
    show captain_img at left with dissolve
    captain "领主大人。"

    "你没听到雷恩走近。他站在你身后，递来一杯热酒。"

    captain "您应该休息了。"

    hide captain_img
    show player_char_img at left with dissolve
    player "雷恩，你觉得我们撑得过去吗？"

    hide player_char_img
    show captain_img at left with dissolve
    captain "说实话？不知道。"

    captain "但我见过比这更绝望的仗。在西境战役的时候，我们被十倍的敌人围了三个月。"

    captain "最后活下来的人只有原来的三分之一。但我们活下来了。"

    captain "活下来的关键不是兵力，不是城墙。是领头的人——让所有人相信，天亮之后还有明天。"

    "他看着你，目光坦诚而坚定。"

    captain "您就是那个人，领主大人。"

    "你接过热酒，喝了一口。辛辣的液体烧过喉咙，带来一阵短暂的暖意。"

    hide captain_img
    show player_char_img at left with dissolve
    player "那就让他们来吧。"

    $ hide_all_chars()
    "你最后看了一眼地图，吹灭了大厅里最后一根蜡烛。"

    "在黑暗中，你听到了远处城墙上巡逻兵的脚步声，听到了铁匠铺传来的叮当敲击声——即使在深夜，也有人在为即将到来的风暴做准备。"

    "战争的阴影已经笼罩了这片土地。"

    "但艾登堡还没有倒下。你也没有。"

    "黎明前的黑暗是最浓的。但黎明总会来。"

    "——只要还有人愿意守到天亮。"

    hide player_char_img with dissolve

    return

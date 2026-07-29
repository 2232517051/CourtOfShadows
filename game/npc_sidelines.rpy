## ============================================================
## NPC支线故事：角色深度个人弧线
## npc_sidelines.rpy
## 奥尔德里克的秘密 / 雷恩的过去 / 艾琳娜的暗面
## 主教的忏悔 / 村长的请求 / 男爵的隐藏荣誉 / 暗百合的考验
## ============================================================

## ── 新角色定义 ──
define village_elder = Character("村长老汉斯", color="#8b7355")

## ── 支线进度标记 ──
default aldric_personal_done = False
default captain_past_done = False
default elena_dark_past_done = False
default bishop_confession_done = False
default village_elder_quest_done = False
default baron_honor_known = False

## ── 支线内部变量 ──
default aldric_will_fight = False
default captain_knows_weakness = False
default captain_war_pledge = False
default elena_trust_deep = False
default elena_skills_used = False
default bishop_gave_key = False
default bishop_total_loyalty = False
default village_well_ruling = ""
default baron_plot_discovered = False
default baron_peace_path = False
default baron_blackmail_option = False
default lily_traitor_fate = ""
default lily_double_agent = False

## ============================================================
## 第一弧线：奥尔德里克的秘密（约150行）
## 可在第二章至第三章调用
## ============================================================

label npc_aldric_secret:

    $ aldric_personal_done = True

    scene bg study_night with dissolve

    "深夜，书房中只剩一盏孤灯。你正在翻阅父亲留下的旧日志，忽然听到门外传来沉重而犹豫的脚步声。"

    "那脚步在门前停了很久——长到你几乎以为是风声的错觉。"

    "终于，三声缓慢的叩门声响起。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    $ hide_all_chars()
    "奥尔德里克推门而入。他没有穿平日整洁的管家服，而是一身旧棉衣，头发也不像往常那样梳得一丝不苟。"

    "他手里端着一个锈迹斑斑的铁盒，像是从地窖深处翻出来的旧物。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "少主……打扰您了。"

    aldric "我知道现在时辰不早，但有些话……如果今晚不说，我怕自己明天又会找借口拖下去。"

    "你从未见过奥尔德里克这副模样。这个永远沉稳、永远从容的老人，此刻双手微微颤抖。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "坐下说，奥尔德里克。什么事让你这般不安？"

    "他缓缓落座，将铁盒放在桌上。生锈的锁扣被他用力掰开，里面是一柄断剑、一枚旧徽章，和一封泛黄的信。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "少主，我……并不是一直都是管家。"

    "他拿起那枚徽章，上面刻着一头展翅的雄鹰——那是旧王国皇家骑士团的标志，你在历史书中见过。"

    aldric "三十年前，我是国王的近卫骑士。你们叫了我三十年的管家。但我的真名是奥尔德里克·冯·布伦纳——皇家骑士团第七席。"

    "你惊讶地看着这个你从小看到大的老人。他佝偻的身躯下，似乎还隐藏着某种早已被岁月磨去棱角的力量。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "皇家骑士……？"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "是的。我曾经誓死效忠先王格里菲斯七世。那是一个……好人。一个好国王。"

    "他的声音变得沙哑，仿佛每一个字都要穿过三十年的尘埃。"

    aldric "先王遇刺那晚，我就在他身边。"

    "灯火摇曳，在奥尔德里克苍老的面容上投下深深的阴影。"

    aldric "那是一个冬夜。先王批阅奏折到很晚，遣散了大部分侍卫。只留我一人守在外面。"

    aldric "刺客从暗道里出来——有人打开了密道的机关，这意味着宫廷内部有人配合。"

    aldric "我听到先王的呼喊，破门而入。但已经……太迟了。"

    "老人低下头，你看到一滴泪落在断剑的剑刃上。"

    aldric "我杀了两个刺客，但第三个已经得手了。先王倒在血泊中，用最后的力气对我说了一句话——"

    aldric "「保护我的人民，奥尔德里克。」"

    "房间里很安静。只有窗外的风声，和他嗓子里压不下去的沙哑。"

    aldric "我没能保护他。我一辈子都没能原谅自己。"

    aldric "骑士团解散后，我隐姓埋名，来到你父亲的领地。你父亲……他知道我的身份，但从未揭穿过。"

    aldric "他给了我管家的职位，让我有个安身之所。而我……把守护你们父子当成了自己的赎罪。"

    "他终于抬起头，浑浊的老眼中有一种你从未见过的恳切。"

    aldric "三十年了。三十年来，我每一天都在想，如果当时我快一步……如果我当时就在屋内……"

    aldric "少主，现在您也面临着危机四伏的局面。我不想……再一次眼睁睁看着我守护的人倒下。"

    "这个老人——不，这个曾经的骑士——将三十年的愧疚与悲伤全部倾倒在你面前。"

    menu:
        "你已经赎够了罪，奥尔德里克。":
            $ change_stat("loyalty", 5)
            $ change_rel("rel_aldric", 15)
            $ log_decision("NPC支线", "宽恕了奥尔德里克")

            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你已经赎够了罪。这三十年来，你尽心尽力地守护着我们家。父亲信任你，我也信任你。"

            player "先王的死不是你的错。真正有罪的是那些策划阴谋的人。"

            "你伸出手，握住老人粗糙的手掌。"

            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "少主……"

            "奥尔德里克的泪水终于落下。你在这一刻明白了——这个老人等这句话，等了整整三十年。"

            aldric "谢谢您……谢谢您。"

            $ hide_all_chars()
            "那一夜，你们在书房中一直谈到天明。他给你讲述了许多关于先王的故事，关于父亲年轻时的往事。"

            "你对奥尔德里克的了解，在这一夜之间变得无比深刻。"

        "你为什么不告诉我父亲真相？":
            $ change_stat("intrigue", 5)
            $ change_rel("rel_aldric", 5)
            $ log_decision("NPC支线", "质问奥尔德里克为何隐瞒")

            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你在我们身边三十年，为什么不把这些告诉父亲？他有权知道。"

            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "……我怕。"

            aldric "我怕他知道真相后会看不起我。一个连国王都保护不了的骑士，有什么资格守在他身边？"

            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "但父亲一直知道你的身份。他选择沉默，说明他信任你。"

            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "是……也许您说得对。也许是我太懦弱了。"

            "老人的手颤抖了一下。然后他从铁盒里取出那封泛黄的信。"

            aldric "这是先王临终前几天写的一封密函。我一直没有勇气打开它。"

            aldric "也许……是时候了。"

            $ hide_all_chars()
            "你接过信函。封蜡上的雄鹰印记依然清晰。这封三十年前的密信，也许藏着改变一切的秘密。"

            "你小心翼翼地打开信封，扫了一眼内容——这关乎王位继承的真相。"

            "你将这个信息深深记在心里。"

        "那你愿意再次拿起剑吗？":
            $ change_stat("power", 5)
            $ change_rel("rel_aldric", 10)
            $ aldric_will_fight = True
            $ log_decision("NPC支线", "请求奥尔德里克重新拿起剑")

            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "过去的事已经无法改变。但现在——我需要你。"

            player "不是作为管家，而是作为骑士。奥尔德里克，你愿意再次拿起剑吗？"

            "老人愣住了。他低头看着那柄断剑，手指抚过锈蚀的刃口。"

            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "我……已经老了。手不如从前稳了，眼也花了。"

            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "但你的经验还在。你知道如何战斗，如何布阵，如何训练士兵。"

            player "我们即将面对的敌人不简单。我需要一个真正上过战场的人来教导我。"

            $ hide_all_chars()
            "奥尔德里克缓缓站起身来，挺直了那弯曲了三十年的脊背。"

            "在那一瞬间，你仿佛看到了三十年前那个意气风发的皇家骑士的影子。"

            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "如果少主需要……那么，从明天起，我在后院等您。"

            aldric "三十年的生锈不是一天能磨去的。但我会把我所知道的一切，都传授给您。"

            $ hide_all_chars()
            "从那天起，每天黎明时分，你都能在后院看到奥尔德里克的身影。他手持木剑，一招一式虽已迟缓，却依然带着旧日骑士的凛然风骨。"

            "你在他的指导下，剑术突飞猛进。"

    hide aldric_img with dissolve

    "这一夜过后，你和奥尔德里克之间的关系发生了微妙而深刻的变化。"

    "白天他照旧端茶、掌灯、称你「少主」。但你已经见过铁盒里的那柄断剑了。"

    return

## ============================================================
## 第二弧线：雷恩队长的过去（约150行）
## 可在第二章至第三章调用
## ============================================================

label npc_captain_past:

    $ captain_past_done = True

    scene bg castle_exterior with dissolve

    "傍晚，夕阳将城堡的石墙染成暗红色。你在城墙巡视时，发现雷恩独自站在箭塔上，望着北方的群山出神。"

    "他手中握着一枚旧军徽——不是你领地的徽记，而是一枚被刻意划花了的鹰爪纹章。"

    "那是冯·哈根男爵的军徽。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "雷恩？你在看什么？"

    "他猛地回过神，将军徽攥进拳头。但他看到是你之后，紧绷的肩膀慢慢松了下来。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "领主大人……我只是在想一些旧事。"

    "你在他身旁的垛口坐下。远处的群山在暮色中变得模糊。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我注意到每次提起男爵，你的反应都比常人激烈。"

    player "雷恩，你和男爵之间到底有什么过往？"

    "风从山谷中吹来，带着松脂和泥土的气味。雷恩没有立刻回答——他低头摸了摸腰带上那道旧伤疤的位置。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "……我曾经是男爵的人。"

    "你没有表现出惊讶——你早就有所察觉。"

    captain "十二年前，我是男爵军队中的一名百夫长。我的部队驻扎在北部边境，负责防御蛮族入侵。"

    captain "男爵……那时候还不像现在这么阴鸷。至少在表面上，他还像一个合格的领主。"

    "雷恩转动着手中的军徽，声音变得低沉而沉重。"

    captain "直到那一年冬天。北方的一个村庄——格伦瓦德——拒绝缴纳男爵额外征收的冬税。"

    captain "男爵给我下了一道命令：「烧了它。连同所有拒绝服从的人一起。」"

    "你注意到雷恩握拳的手指关节发白。"

    captain "我去了格伦瓦德。那是一个两千多人的边境村子。我看到了老人、妇女、孩子……他们只是穷，交不起额外的税。"

    captain "我的副手问我什么时候开始。我站在村口，看着一个小女孩抱着一只瘸腿的羊从我面前走过。她对我笑了一下。"

    captain "我……下不了手。"

    "暮色更深了，第一颗星星出现在天际。"

    captain "我当场违抗了军令。带着我的百人队撤了回去，告诉男爵：格伦瓦德已经缴清了税款。"

    captain "但谎言没能维持多久。男爵派了另一支部队去核实。"

    captain "他发现村庄完好无损后，宣布我为叛徒。我的部下被打散编入其他部队，而我……被判处鞭刑五十，然后流放。"

    "雷恩解开衣领，在昏暗的光线中，你隐约看到他后背上纵横交错的旧伤疤。"

    captain "五十鞭。男爵亲自监刑，还用了浸过盐水的皮鞭。"

    captain "行刑结束后，我被扔在荒野中等死。是你的父亲……"

    "他的声音微微颤抖。"

    captain "你父亲的巡逻队发现了奄奄一息的我。他不仅救了我的命，还给了我队长的职位。"

    captain "从那以后，我发誓用一生来报答这份恩情。"

    "你终于理解了为什么雷恩对你的家族如此忠诚，也理解了他对男爵那种深入骨髓的仇恨。"

    menu:
        "你做了正确的事，雷恩。":
            $ change_stat("loyalty", 5)
            $ change_rel("rel_captain", 15)
            $ log_decision("NPC支线", "肯定了雷恩的选择")

            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你做了正确的事。一个好的军人，应该知道什么命令可以服从，什么命令不能。"

            player "格伦瓦德的人因为你而活了下来。你是一个有良知的战士，我为此感到骄傲。"

            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "……"

            $ hide_all_chars()
            "雷恩没有说话，但你看到他握着军徽的手终于松开了。"

            "他将那枚被划花的军徽用力扔下城墙。铜片在空中翻了几个跟头，很快就看不见了。"

            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "过去的就让它过去吧。现在，我只为艾登堡而战。"

            "你拍了拍他的肩膀。这个沉默寡言的队长，此刻眼中闪烁着你从未见过的光芒。"

        "男爵一定因此恨你入骨。":
            $ change_stat("intrigue", 5)
            $ change_rel("rel_captain", 5)
            $ captain_knows_weakness = True
            $ log_decision("NPC支线", "从雷恩处获取男爵弱点")

            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "这就解释了为什么男爵对我们领地始终怀有敌意。你在他的军队中抗命——对他来说这是奇耻大辱。"

            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "不只是恨。男爵是一个绝不容许背叛的人。在他看来，我的存在就是对他权威的嘲讽。"

            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "那你一定很了解他。告诉我，他有什么弱点？"

            "雷恩犹豫了一下，然后压低了声音。"

            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "男爵最大的弱点……是他的骄傲。他无法容忍任何人质疑他的判断。"

            captain "还有——他的左翼部队。那是他最精锐的骑兵团，但指挥官沃尔夫是个酒鬼。"

            captain "如果真到了交战的那一天……集中力量攻击左翼，男爵的阵型就会崩溃。"

            "你将这个关键的情报牢牢记住。战场上，一个弱点足以决定胜负。"

        "如果战争真的来了，你会怎么做？":
            $ change_stat("power", 3)
            $ change_stat("loyalty", 3)
            $ change_rel("rel_captain", 10)
            $ captain_war_pledge = True
            $ log_decision("NPC支线", "雷恩承诺亲自对抗男爵")

            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "男爵的野心越来越大。如果有一天战争不可避免……你准备好了吗？"

            "雷恩转过身来面对你。在暮色的映照下，他的表情变得如刀刃般冷硬。"

            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "准备好了。"

            captain "实际上，我每天都在为那一天做准备。"

            captain "领主大人，我向你发誓——如果战争来临，我会亲手面对男爵。"

            captain "不是为了复仇，是为了终结他的暴行。格伦瓦德不应该是最后一个差点被屠灭的村庄。"

            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你不必独自面对他。"

            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "我知道。但这是我的责任——作为一个曾经见证他残暴的人。"

            "雷恩单膝跪下，将拳头抵在胸前。"

            captain "我的剑永远为艾登堡而举，我的命永远为您所用。"

            "你伸手把他从地上扶了起来。"

    hide captain_img with dissolve

    $ hide_all_chars()
    "夜幕完全降临。你们一同走下城墙，回到温暖的灯火中。"

    "关于雷恩的过去，你终于知道了全貌。这个铁骨铮铮的汉子，曾经为了无辜的生命付出过惨痛的代价。"

    return

## ============================================================
## 第三弧线：艾琳娜的暗面（约180行）
## 可在第三章调用
## ============================================================

label npc_elena_past:

    $ elena_dark_past_done = True

    scene bg forest_path with dissolve

    "夜虫叫得正欢。你失眠后出来散步，却在城堡后院的老橡树下看到了一个身影。"

    "艾琳娜穿着一身黑衣，正在对着树干反复投掷一把匕首。每一刀都精准地插在同一个位置——树干上已经被凿出了一个深深的凹痕。"

    "她的动作快得几乎看不清，但每一次投掷之间，你都能感受到一种压抑的、几近疯狂的专注。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "艾琳娜？这么晚了……"

    $ hide_all_chars()
    "她猛地回头。在那一瞬间，你看到她眼中闪过一丝你从未见过的东西——不是警惕，是恐惧。"

    "像一只被逼到角落的野猫。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "……是你。"

    "她迅速收起匕首，但你注意到她的手在微微发抖。她的眼圈发红，像是刚哭过。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你还好吗？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "做了噩梦。老毛病了。"

    $ hide_all_chars()
    "她在树下坐下来，双手抱着膝盖。月光穿过树叶的缝隙，在她身上投下斑驳的光影。"

    "你在她身边坐下。森林中传来猫头鹰的低鸣和远处溪水的声响。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    ## ch3 早期: 只露"受过训练 / 手上有血"的情绪裂缝, 不交代王后/暗百合/双重间谍身份.
    ## 完整身份坦白(双重间谍)留到 ch3_elena_secret(暗百合章末), 那里才 set 两个 known flag.
    ## 因此本场景不 set elena_spy_known / elena_identity_exposed_known, 以保住章末高潮.
    if elena_spy_known:
        elena "我是王后的人——这个你在路上已经看出来了。"

        elena "可有些事，我连你都没提过。今晚……也还说不全。"
    else:
        elena "我不是你以为的那种管事。这把刀，我很小就开始练了。"

    $ hide_all_chars()
    "她没有往下说全。你看得出来，她今晚肯交出来的，只有一角。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "我手上有人命。不止一条。"

    elena "是别人逼我做的，可刀是我握着的。这笔账赖不掉。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你不用今晚就全说出来。"

    player "我对你的来历，只知道奥尔德里克提过的那一层——王后派来的侍从。剩下的，你想说的时候再说。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "……谢谢你。"

    "她苦笑了一声。那笑容比哭还难看。"

    elena "我从小长在一个不把人当人的地方。在那儿，写字算账是次要的，真正要学会的是怎么悄没声地结果一个人。"

    "她继续说着，声音平静得不像在讲自己。"

    elena "那些人的脸，我全记得。有时候在梦里，他们站成一排看着我。不说话，就看着。"

    "她无意识地摸着自己的手腕——你隐约看到几道淡淡的旧疤。"

    elena "你知道最难受的是什么吗？不是那些事本身。是我做完之后，手很稳。"

    elena "一点都不抖。"

    "寂静在你们之间蔓延开来。猫头鹰不知何时停了，整片森林像是在屏着气。"

    "月光照在她脸上，你看到一道泪痕。"

    elena "你父亲是少数几个……拿我当人看的人。可他也不在了。"

    "她转过头看你。那双紫色的眼睛里，是化不开的孤独，还有一点不敢声张的指望。"

    elena "所以……你现在看到的这个女人，手上是有血的。这一点，我瞒不了你。"

    elena "有时候我半夜醒来，发现自己手里不知什么时候又多了一把刀。本能反应。"

    elena "你……害怕吗？"

    menu:
        "你现在安全了，艾琳娜。":
            $ change_stat("loyalty", 3)
            $ change_rel("rel_elena", 20)
            $ elena_trust_deep = True
            $ log_decision("NPC支线", "安慰艾琳娜，承诺她是安全的")

            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你现在安全了。"

            "你也说不清为什么会冒出这句话。但她听见的时候，肩膀几不可察地抖了一下。"

            player "你不是工具。你是一个从那种地方活下来的人。那些事不是你选的——你那时还是个孩子。"

            "你伸出手，轻轻覆上她冰凉的手背。她浑身一颤，像是触电一般——但没有缩回去。"

            player "我父亲把这个家交到你手里，他不会看错人。"

            player "在我眼里，你不是一把刀，也不是谁手里的工具。你就是艾琳娜。别的我不在乎。"

            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "……"

            "她沉默了很久。你感到她的手从冰凉变得温暖，然后她的手指慢慢收拢，反握住了你的手。"

            elena "你说话的方式……总是让人没办法防备。"

            $ hide_all_chars()
            "她没有把话说完。那天夜里，你们就那样在老橡树下坐着，谁也没再开口。"

            "她的手一直反握着你的，没有松开。"

        "你杀过多少人？一共？":
            $ change_stat("intrigue", 3)
            $ change_rel("rel_elena", 5)
            $ log_decision("NPC支线", "直接追问艾琳娜的过去")

            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "那些任务……一共有几个人？"

            "你的问题直接而冷静。艾琳娜看了你一眼——她的眼中没有愤怒，反而有一丝……释然。"

            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "三个。"

            "她回答得很轻，但很坚定。仿佛把这个数字压在心里很多年了，今夜终于愿意拿出来。"

            elena "第一个是商人，四十多岁。第二个是一个小贵族的管家。"

            "她一个一个数着，像是在念诵一段简短却沉重的祷文。"

            elena "第三个……是一个女人。他们说她是叛徒。我后来才知道，她只是想带自己的孩子离开侍女学院。"

            "她的声音在最后一个人时微微颤抖。"

            elena "那个女人在死之前对我说：「你也只是个孩子啊。」"

            elena "那是我逃走的导火索。因为我忽然意识到——如果我继续留下来，总有一天，我也会变成像那些训练我的人一样的……东西。"

            "你沉默了片刻。三个人，三张她至今记得的脸。"

            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "记住那些面孔是好事。说明你还有良知。"

            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "……也许吧。但有时候我宁愿忘记。"

        "艾琳娜，我需要你的技能。":
            $ change_stat("power", 3)
            $ change_stat("intrigue", 3)
            $ change_rel("rel_elena", -5)
            $ elena_skills_used = True
            $ log_decision("NPC支线", "务实地看待艾琳娜的能力")

            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你所经历的那些是不公平的，我承认。但现在我们面临真实的威胁。"

            player "你的技能——你在侍女学院学到的一切——对我们至关重要。"

            "艾琳娜定定地看着你。你在她眼中看到了一丝失望，但很快被一种职业化的冷漠取代。"

            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "……我就知道。"

            elena "果然。到头来，每个人需要的都是我的刀。"

            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "不——我需要的是你。但我不会假装你的技能不重要。我们都在这盘棋局上，我需要你最好的一面。"

            "她站起身来，拍了拍衣服上的草屑。暗中看不太清她的脸，但你从声音里听出她的表情恢复了平日的淡漠。"

            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "行。你要用我的技能，可以。但别指望我会喜欢这样。"

            elena "还有——别再用那种可怜的眼神看我。我最讨厌被可怜。"

            $ hide_all_chars()
            "她走得比来的时候快。你隐约觉得，自己刚才也许说错了话。"

            "但在残酷的权谋世界中，有些时候务实比温情更重要——你试着这么告诉自己。"

    hide elena_img with dissolve

    "夜色渐深，你独自坐在老橡树下，思考着艾琳娜的过去。"

    "一个在黑暗中长大的少女，身上背负着几条人命的重量。"

    "她和你父亲之间，显然还有一段你不知道的过往。"

    "现在父亲不在了，她留在了你身边。这份信任不轻，你得想清楚怎么接。"

    return

## ============================================================
## 第四弧线：主教的忏悔（约150行）
## 可在第三章至第四章调用
## ============================================================

label npc_bishop_confession:

    $ bishop_confession_done = True

    scene bg church with dissolve

    "你深夜收到侍从的报告——主教马修斯独自在教堂里，已经喝了整整一壶酒。"

    "这不寻常。主教虽然不是苦修之人，但从未如此失态过。"

    "你决定亲自去看看。"

    "推开教堂厚重的橡木门，烛光摇曳的圣堂中弥漫着浓重的酒气。"

    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve

    $ hide_all_chars()
    "马修斯主教瘫坐在第一排长椅上，手中攥着一只银质酒壶。他的法袍歪斜，圣徽歪在一边。"

    "在他面前的祭坛上，十字架在烛光中投下巨大的阴影。"

    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "啊……年轻的领主。来……来找老朽忏悔的吗？"

    "他的声音含糊不清，但眼神中有一种异样的清醒——那种喝了很多酒、反而变得可怕地清醒的状态。"

    hide bishop_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "主教，你喝醉了。让我送你回去。"

    hide player_char_img
    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "醉了？不……不，我二十年来第一次这么清醒。"

    "他摇摇晃晃地站起来，指着祭坛上的十字架。"

    bishop "你看那个——至高的审判者。二十年来我每天对着它祈祷。祈求宽恕。但它从来不回答我。"

    bishop "也许是因为……有些罪孽，连上帝都不愿意听。"

    hide bishop_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你到底在说什么？"

    "主教转过身来面对你。烛光从他背后照来，让他的面容隐没在阴影中。"

    if bishop_doubt_done:
        # 玩家已经从 npc_bishop_doubt 中得知遗诏真相，跳过重复叙述
        hide player_char_img
        $ hide_all_chars("bishop_img")
        show bishop_img at left with dissolve
        bishop "遗诏的事……你已经知道了。"

        bishop "但你不知道的是——我每天都活在这份罪孽里。二十年了。"

        "他又灌了一口酒。醉意让他比平时坦诚得多。"

        bishop "白天跟你说的时候，我还能假装冷静。但到了夜里——"

        bishop "你的父亲……他是先王指定的唯一摄政人选。如果遗诏没被篡改，也许你的父亲今天还活着。而我明知真相，却什么都没做。"

        "你半天没能说出话来。"

        ## 此路径也揭示了遗诏真相——确保flag已设置
        $ testament_forged_known = True
        $ ferein_role_known = True
        $ father_was_regent_known = True

    else:
        hide player_char_img
        $ hide_all_chars("bishop_img")
        show bishop_img at left with dissolve
        bishop "先王的遗诏。你听说过吗？"

        "你的心猛然一跳。先王格里菲斯七世的遗诏——关于王位继承的最后安排——一直是个谜团。有人说它被销毁了，有人说它根本不存在。"

        hide bishop_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "遗诏？那不是传说吗？"

        hide player_char_img
        $ hide_all_chars("bishop_img")
        show bishop_img at left with dissolve
        bishop "不是传说。它存在过。"

        "主教的声音变得低沉而痛苦。"

        bishop "因为我发现了真相——却选择了沉默。"

        "教堂中陷入了令人窒息的寂静。蜡烛的火焰在你们之间颤抖。"

        bishop "二十年前。先王驾崩后，遗诏被密封在王宫的保险库中。"

        bishop "遗诏的内容……与王后希望的继承安排不同。先王在遗诏中指定了你的父亲——艾登堡领主——作为唯一的摄政。不是王后。"

        bishop "王后不甘心。她找到了大主教费雷恩——我的上级——达成了一笔肮脏的交易。教会支持她独揽摄政权，作为交换，王后将教会的征税权扩大到全国。"

        bishop "费雷恩在先王驾崩的当晚，亲手将原始遗诏调了包。他用教会的印章为篡改后的版本背书。"

        "他用力闭上眼睛，似乎在重温那段可怕的记忆。"

        bishop "那晚我就在场——作为他的随身副主教，端着烛台，什么都没来得及反应。"

        bishop "调包之后，他把那份原件递给我，命令我拿去销毁。他信任我——以为我会按命令执行。"

        bishop "我接过原件走出房间，在烧毁它之前的最后一刻……我没有下手。我把它藏了起来。"

        bishop "这二十年来，那份原件一直在我手里。我没敢告诉任何人——直到今天对你说出这些。"

        bishop "我本该站出来揭发。但我害怕。害怕教会的报复，害怕牵连家人。于是我选择了沉默——这沉默，比亲手犯罪更可耻。"

        bishop "从那以后……王后稳坐摄政的宝座。而教会因为这份「功劳」，获得了前所未有的权力。我也因此被提拔为主教。"

        bishop "呵。多讽刺。一个知道真相却选择缄默的人，穿着圣洁的法袍，在上帝面前布道。"

        "他又灌了一口酒。你的脑中飞速运转——这个信息的分量，你比任何人都清楚。"

        bishop "这二十年来，我做了很多事来弥补。建学校、施粥棚、保护村民免受贵族欺压……"

        bishop "但我知道。这些善行永远填不满我心里那个洞。因为我的沉默，整个王国的命运都改变了。"

        bishop "如果当年我站出来……也许一切都会不同。也许你不用承受这些。"

        "你张了张嘴，最后什么也没说出来。"

        ## 主教忏悔揭示了遗诏篡改和父亲摄政权的真相——设置对应flag
        $ testament_forged_known = True
        $ ferein_role_known = True
        $ father_was_regent_known = True

    menu:
        "为他赦罪——以你能给的全部虔信" if faith >= 60:
            $ change_stat("faith", 5)
            $ change_rel("rel_bishop", 15)
            $ log_decision("NPC支线", "亲自为主教赦罪")

            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "主教大人， 跪下。"

            $ hide_all_chars()
            "你站起来。语气很平静——但不容置疑。"
            "马修斯愣了一下， 然后真的跪了下来。"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我不是教士， 没有赦罪的权力。但我以艾登堡领主的名义， 以你二十年守护那个匣子的事实， 替上天暂时记下你的悔。"
            player "余下的， 你跟上天去说。"

            $ hide_all_chars()
            "马修斯哭了——是真的哭了， 不是哀嚎， 是一个老人多年压抑后的释放。"
            "他从地上爬起来时， 你看到他眼神里有种二十年没出现过的东西——一个可以重新挺直腰杆的牧者。"

        "上帝会宽恕你的，主教。":
            $ change_stat("faith", 8)
            $ change_rel("rel_bishop", 10)
            $ log_decision("NPC支线", "以信仰宽恕了主教")

            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你犯了错。但你花了二十年在赎罪。上帝看得到。"

            player "《圣经》说，七十个七次的饶恕。你已经在那条路上走了二十年了。"

            "主教呆呆地看着你，像是不敢相信自己听到的话。"

            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "你……你不恨我？如果遗诏没被篡改，你的父亲也许——"

            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "也许。但「也许」改变不了已经发生的事。"

            player "主教，我不是来审判你的。我是来告诉你——继续你的赎罪之路。用行动，而不是用酒。"

            "你从他手中抽走酒壶。他没有反抗，只是低下头，肩膀不停地颤抖。"

            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "谢谢你……年轻的领主。谢谢你。"

            $ hide_all_chars()
            "你在教堂中陪他坐了很久，直到他酒醒。从那以后，主教再也没有喝过酒。"

            "而他对你的信仰和忠诚，变得比任何时候都更加坚定。"

        "证据在哪里？旧遗诏藏在哪里？":
            $ change_stat("intrigue", 8)
            $ change_rel("rel_bishop", 5)
            $ bishop_gave_key = True
            $ log_decision("NPC支线", "从主教处获取遗诏证据")

            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "主教，你说你把旧遗诏藏了起来——它还在吗？在哪里？"

            "主教抬起头，醉意似乎一瞬间消退了大半。他放下酒杯，身体坐直了。"

            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "你……你想要它？"

            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "如果那份遗诏真的能证明先王的本意，它就是改变一切的筹码。"

            "主教闭上眼睛，嘴唇微动，像是在做最后一次祈祷。然后他伸手探入法袍的内袋，取出一把古铜色的小钥匙。"

            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "教堂地下室。最深处有一个假墙——你推右边第三块石头，墙会打开。"

            bishop "里面有一个铁箱。这把钥匙可以打开它。"

            "你接过钥匙。它冰凉沉重。"

            bishop "拿走它吧。也许它能帮你做成我二十年前没有勇气做的事。"

            bishop "但你要小心——王后如果知道旧遗诏还存在，她会不惜一切代价销毁它。和你。"

            "你将钥匙贴身收好。"

            ## ── 玩家亲自下地下室取遗诏 ──
            hide bishop_img with dissolve
            $ hide_all_chars()

            "主教的酒意再度涌上，他靠着长椅合上双眼，呼吸渐渐沉稳。酒壶从他松开的手中滑落，在石板上发出轻响。"

            "你不打算等到明天。"

            scene bg underground with dissolve
            $ unlock_gallery("bg_underground")

            "你提着一盏油灯，顺着教堂侧翼的石阶向下走。空气逐层变得阴冷潮湿，弥漫着陈年熏香与霉味交织的气息。"

            "地下室比想象中深。灯火照在壁画上——天使与恶魔的搏斗、圣徒的殉道，颜色早已斑驳。"

            "最深处是一面看似平常的石墙。你从右向左数——一块、两块、第三块。"

            "你伸手按住那块石头，用力向内推。"

            "短暂的寂静之后，机括的低鸣传来。石墙缓缓让开，露出一个隐藏的壁龛。"

            "壁龛中静静放着一个铁箱，箱身刻着教会的十字徽记，锁孔蒙着一层薄灰——显然多年未被打开。"

            "你从怀中取出那把古铜色的小钥匙，插入锁孔。"

            "钥匙转动的一瞬，锁簧清脆作响——箱盖轻轻弹开。"

            "里面衬着褪色的红绒。上面摆放着三样东西。"

            "第一样——一份泛黄的羊皮卷，蜡封上印着皇家徽章，完好如初。"

            "第二样——一枚金色印章，展翅的鹰，是先王格里菲斯七世的私人纹章。"

            "第三样——一张折叠的便笺，封口写着：「致我的学生马修斯——仅在极端情况下拆阅。」"

            "你先拆开了便笺。费雷恩的笔迹苍劲有力——"

            "『马修斯，如果你在读这封信，说明我已经不在了。这个匣子里有两样东西你必须守护：先王的原始遗诏和他的私人印章。』"

            "『没有这枚印章，任何人都无法证明遗诏是伪造的——因为印章只有一枚。官方版本上的印章是仿制的。对比细节，就能证明哪份是真、哪份是假。』"

            "你展开羊皮卷。顶端的皇家徽章以金粉绘制，与印章纹样分毫不差。正文是先王的亲笔——字迹颤抖，那是一个垂死之人留下的最后意志。"

            "遗诏的内容明确得令人心悸——摄政权属于你的父亲，王后不得干政。"

            "你的手微微发抖。二十年的秘密，就躺在你手里。"

            $ testament_original_obtained = True

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "（这份遗诏……加上印章……就是推翻整个谎言的物证。）"

            $ hide_all_chars()
            "你将羊皮卷、印章、便笺仔细取出，收入怀中。然后合上铁箱，把石块推回原位——墙面重新合拢，没有留下任何痕迹。"

            scene bg church_interior with dissolve
            "你走出地下室时，主教仍在长椅上熟睡。他不会察觉壁龛已被打开；也不会知道，从这一刻起，真正的博弈才刚刚开始。"

        "你欠我父亲一条命，主教。":
            $ change_stat("power", 5)
            $ change_rel("rel_bishop", -5)
            $ bishop_total_loyalty = True
            $ log_decision("NPC支线", "用愧疚要求主教效忠")

            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你亲口说的——如果遗诏没被篡改，我父亲也许还活着。"

            player "那你欠我们家一条命。"

            "你的声音冷硬如铁。主教被你的语气惊醒了几分，恐惧取代了他脸上的醉意。"

            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "我……我知道。"

            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "那就用行动来还。从今天起，你的每一分力量、每一条情报、每一份忠诚，都属于艾登堡。"

            player "不是因为信仰，不是因为良心，而是因为你欠我们的。听明白了吗？"

            "主教跪了下来。不是信徒的跪拜，而是一个罪人在审判者面前的臣服。"

            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "我……明白了。从今以后，我是您的人。完全的，彻底的。"

            bishop "无论您需要什么——教会的资源、情报网络、甚至是……不那么光彩的手段——我都会为您做到。"

            $ hide_all_chars()
            "你冷冷地看着跪在地上的主教。你不确定自己是否做得太过分了。"

            "而一个完全忠诚的主教，比一个被良心折磨的主教有用得多。"

    hide bishop_img with dissolve

    "你离开教堂时，天边已经泛起了鱼肚白。"

    "身后的教堂里，十字架的阴影在晨光中缓缓移动，仿佛连上帝也在审视着今夜发生的一切。"

    return

## ============================================================
## 第五弧线：村长的请求（约120行）
## 可在第一章至第二章调用
## ============================================================

label npc_village_quest:

    $ village_elder_quest_done = True

    scene bg village with dissolve

    "一个阳光明媚的早晨，你在领地巡视时来到了辖区内最大的村庄——石泉村。"

    "村口的老榆树下，两群人正对峙着。一边是红脸的铁匠一家，另一边是黑瘦的牧羊人一家。双方互相指着对方的鼻子叫骂。"

    "中间站着一个白须飘飘的老人，正徒劳地试图拉开两家人。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "少主，那就是石泉村的村长——老汉斯。看起来出了什么纠纷。"

    "老汉斯注意到了你们的到来，连忙迎上前，行了一个颤巍巍的礼。"

    hide aldric_img with dissolve

    $ hide_all_chars("village_elder_img")
    show village_elder_img at left with dissolve
    village_elder "领主大人！您来得正好！老朽实在压不住这两家人了。"

    hide village_elder_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "怎么回事？"

    hide player_char_img
    $ hide_all_chars("village_elder_img")
    show village_elder_img at left with dissolve
    village_elder "是水井的事。石泉村祖祖辈辈就靠村中那口老井吃水。"

    village_elder "铁匠柯林一家在这里住了六代人，那口井就在他家旁边，一直是他们在维护。"

    village_elder "可上个月，牧羊人约根一家在自家地里建新羊圈的时候，挖地基不小心挖断了一条地下水脉。"

    village_elder "现在老井的水量减了一半。两家人就为了谁有优先用水的权利打了起来。"

    "你点点头。水源纠纷在农村是大事——关系到庄稼灌溉和日常饮水。"

    hide village_elder_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "让我去现场看看。"

    scene bg village with dissolve

    "你来到老井旁边。井口的石壁上长满了青苔，确实是一口年头很久的井。你往下望去，水位比正常水井低了不少。"

    "然后你去查看了约根家新建的羊圈。地基挖掘确实切断了一条暗河支流——但问题是，这个地基的设计异常深，超出了建羊圈的需要。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "少主，这个地基……挖得太深了。建羊圈用不着挖这么深。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "是谁给约根出的主意，地基要挖这么深？"

    $ hide_all_chars()
    "你叫来了牧羊人约根。这是个老实巴交的汉子，一问之下，他支支吾吾地说出了实情。"

    "一个月前，一个自称是「男爵派来的测量官」的人来到村子，告诉约根说他家地下有矿脉，让他往深里挖。"

    "那个测量官不仅免费帮他做了地基设计，还给了他五个银币作为「鼓励」。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "男爵的人……"

    $ hide_all_chars()
    "你和奥尔德里克交换了一个眼神。这不是一个单纯的邻里纠纷——有人在背后操纵。"

    "如果男爵系统性地破坏边境村庄的水源，不出三年，这些村庄就会因为无水可用而废弃。到时候，男爵就能不费一兵一卒地蚕食你的领地。"

    "但眼下，你首先要解决两家人的纠纷。"

    menu:
        "判给铁匠柯林家——他们世代维护水井":
            $ change_stat("loyalty", 5)
            $ village_well_ruling = "original"
            $ log_decision("NPC支线", "判水井归原来的铁匠家")

            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "这口井由柯林家世代维护，优先使用权理应归他们。"

            player "但约根家也不能没水用。约根，你需要在三日内修复被切断的水脉，恢复老井的水量。费用由领地公库补贴一半。"

            "铁匠柯林一家露出了感激的神色。牧羊人约根虽然不太情愿，但听到有补贴也没有再闹。"

            hide player_char_img
            $ hide_all_chars("village_elder_img")
            show village_elder_img at left with dissolve
            village_elder "领主大人英明！这样两家人都能过下去了。"

            "你的裁决公正而有人情味。石泉村的村民们看到了你作为领主的担当，一时间口碑大振。"

        "两家共享水源——制定公平的用水规则":
            $ change_stat("reputation", 5)
            $ village_well_ruling = "shared"
            $ log_decision("NPC支线", "判两家共享水源")

            hide village_elder_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "水源是公共资源，不应该属于任何一家。从今天起，石泉村的水井由村公所统一管理。"

            player "每家按人口分配用水量。柯林家负责日常维护，约根家负责修复水脉。维护费用由全村分摊。"

            "两家人面面相觑。这个方案不偏不倚——虽然谁都没有完全满意，但也都能接受。"

            hide player_char_img
            $ hide_all_chars("village_elder_img")
            show village_elder_img at left with dissolve
            village_elder "领主大人这是大智慧啊！一碗水端平，两家都没话说。"

            "你建立了一套公平的水源管理制度。消息传开后，周边几个村庄也纷纷效仿。你「公正之主」的名声越传越远。"

        "追查男爵的阴谋——这不是意外":
            $ change_stat("intrigue", 5)
            $ baron_plot_discovered = True
            $ log_decision("NPC支线", "追查男爵破坏水源的阴谋")

            hide village_elder_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "这件事没有这么简单。约根，那个测量官长什么样？"

            "约根回忆了半天，描述了一个留着络腮胡、戴皮帽的中年人。你让人记录下了他的特征。"

            player "奥尔德里克，派人去周边村庄调查——是不是还有其他村子也出现过类似的「测量官」。"

            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "是，少主。"

            $ hide_all_chars()
            "三天后，调查结果让你倒吸一口凉气。"

            "不仅石泉村——周边五个村庄都遭到了类似的操纵。有的是水源被破坏，有的是牧场被引导放牧过度，还有的是农田被建议种植错误的作物。"

            "这是一个精心策划的、旨在削弱你领地边境经济的系统性阴谋。而幕后的黑手，指向了冯·哈根男爵。"

            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "男爵在不动一兵一卒的情况下，就想让我的边境村庄慢慢死掉。"

            player "好手段……但现在我知道了。"

            $ hide_all_chars()
            "你下令加强边境村庄的安全巡查，驱逐一切来历不明的外人。同时将这条重要情报记录在案——如果将来与男爵交涉，这就是铁证。"

            "至于水井纠纷，你简单地判了两家共享，然后用公款修复了水脉。"

    hide aldric_img with dissolve

    "离开石泉村的时候，老汉斯一直送到村口。"

    hide player_char_img
    $ hide_all_chars("village_elder_img")
    show village_elder_img at left with dissolve
    village_elder "领主大人，老朽活了七十多年，见过不少领主。您是最让人放心的一个。"

    "你向老人点头致意。也许在这个波谲云诡的权力游戏中，保护好这些最普通的百姓，才是你最重要的责任。"

    hide village_elder_img with dissolve

    return

## ============================================================
## 第六弧线：男爵的隐藏荣誉（约130行）
## 可在第四章至第五章调用
## ============================================================

label npc_baron_honor:

    $ baron_honor_known = True

    scene bg dungeon with dissolve

    "地牢中弥漫着潮湿和铁锈的气味。你来审讯一个在边境冲突中被俘的男爵士兵。"

    "这个士兵名叫海因里希，是一个老兵。他的手臂在战斗中受了伤，但眼神依然坚毅不屈。"

    "你原本只是想从他口中获取军事情报，但谈话的方向出乎你的意料。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "海因里希，你为男爵效力多久了？"

    $ hide_all_chars("soldier_generic_img")
    show soldier_generic_img at left with dissolve
    heinrich "二十三年。从我十六岁入伍到现在。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "二十三年……你了解男爵吗？"

    $ hide_all_chars()
    $ hide_all_chars("soldier_generic_img")
    show soldier_generic_img at left with dissolve
    heinrich "领主大人，我知道您和男爵是对头。但在您判我之前，我能不能……说几句话？"

    "你示意他继续。"

    heinrich "所有人都说男爵是个暴君、一个野心家、一头只知道吞噬的野兽。但是……他不只是那样。"

    "你挑了挑眉。"

    heinrich "二十年前。北方蛮族大举南侵。王廷的援军迟迟不到——因为伊莎贝拉王后认为北方边境「不值得浪费军费」。"

    heinrich "整个北部边境只有男爵一支军队。蛮族的兵力是我们的三倍。所有人都在撤退——只有男爵说：「不退。」"

    "老兵挺直了佝偻的腰，声音里有了不一样的东西。"

    heinrich "他带着我们三百人，死守格伦瓦德隘口七天七夜。第三天的时候，蛮族突破了左翼防线。男爵亲自带着骑兵去堵口。"

    heinrich "那一战……他失去了左眼。一支蛮族的箭射穿了他的面甲。但他没有倒下。他用独眼指挥了剩下四天的战斗。"

    heinrich "第七天，蛮族退了。格伦瓦德全村两千多人——男女老少——保住了性命。"

    "你陷入了沉思。你听过北方蛮族入侵的历史，但从来没有听说过男爵在其中扮演的角色。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "以他的战功，为什么还只是个男爵？"

    $ hide_all_chars()
    $ hide_all_chars("soldier_generic_img")
    show soldier_generic_img at left with dissolve
    heinrich "这个问题我们也问过。他每次都推辞封赏——说什么「边疆之臣不敢僭越」。"

    heinrich "后来我才想明白。一个男爵养三百私兵，没人会多看一眼。但如果是伯爵养三百私兵——王都的眼睛就全盯过来了。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "王后没有派援军？"

    $ hide_all_chars()
    "海因里希苦笑了一下。"

    $ hide_all_chars("soldier_generic_img")
    show soldier_generic_img at left with dissolve
    heinrich "不仅没有援军。战后，王后还削减了男爵的军饷，说他「擅自开战，耗费国库」。"

    heinrich "但那还不是最让男爵心寒的事。"

    "老兵的声音变得沉重。"

    heinrich "男爵的第一任妻子——艾玛夫人。她是一个温柔善良的女人，在战争期间负责后方的伤员救治。"

    heinrich "战后不久，王后以「通敌叛国」的罪名逮捕了艾玛夫人。说她在战争中私通蛮族——纯粹是莫须有的罪名。"

    heinrich "审判……不，那算不上审判。那只是一场表演。三天后，艾玛夫人被处决了。"

    heinrich "男爵跪在刑场上，一声没哭。但从那以后……他就变了。"

    "地牢中的空气似乎变得更加寒冷。你终于理解了男爵身上那股不可理喻的仇恨和偏执的根源。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "所以他恨王后。"

    $ hide_all_chars()
    $ hide_all_chars("soldier_generic_img")
    show soldier_generic_img at left with dissolve
    heinrich "不只是恨。他要报复。他要让王后付出代价。这就是他这些年来所有行动的核心——不是野心，是复仇。"

    heinrich "我不是在替他开脱。他做的很多事确实过分了。但领主大人……他不是一个纯粹的恶人。他是一个被逼成恶人的人。"

    "这些信息彻底改变了你对男爵的认知。一个守护村庄的英雄、一个失去妻子的丈夫、一个被国家背叛的忠臣——这些形象与你之前认识的那个冷酷阴鸷的男爵截然不同。"

    menu:
        "这改变了一切。也许我们不必非要兵戎相见。":
            $ change_stat("reputation", 5)
            $ change_rel("rel_baron", 10)
            $ baron_peace_path = True
            $ log_decision("NPC支线", "了解真相后考虑与男爵和谈")

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "也许……我一直在用错误的方式看待男爵。"

            player "如果他的真正敌人是王后，而不是我——那么我们之间也许存在谈判的空间。"

            "你让侍从给海因里希松了绑，端上了热汤和面包。"

            player "海因里希，如果我放你回去，你能把一封信带给男爵吗？"

            $ hide_all_chars("soldier_generic_img")
            show soldier_generic_img at left with dissolve
            heinrich "领主大人……您是认真的？"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我是认真的。这个世界上已经有太多仇恨了。如果能化干戈为玉帛，为什么不试试？"

            $ hide_all_chars()
            "老兵看着你的眼睛，似乎在判断你是否真诚。最后，他缓缓点了点头。"

            $ hide_all_chars("soldier_generic_img")
            show soldier_generic_img at left with dissolve
            heinrich "好。我把信带到。但我不能保证男爵会怎么做——他心里的仇恨太深了。"

            "你花了一整夜写那封信。你知道这也许是一步险棋，但有时候，和平的代价比战争的代价要小得多。"

        "可怜之人必有可恨之处。这不能为他的行为开脱。":
            $ change_stat("intrigue", 3)
            $ change_stat("power", 3)
            $ log_decision("NPC支线", "承认真相但不改变立场")

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我理解他的遭遇。但这不能成为他侵略邻邦、残害无辜的理由。"

            player "一个人的痛苦不能成为制造更多痛苦的借口。"

            $ hide_all_chars()
            "海因里希低下了头。他知道你说得没错。"

            $ hide_all_chars("soldier_generic_img")
            show soldier_generic_img at left with dissolve
            heinrich "也许吧。但人……不是总能做到理性的。"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我记住了你告诉我的这些。也许有一天我会需要这些信息。但今天——我不会因为同情而放松警惕。"

            $ hide_all_chars()
            "你让人好好照料海因里希的伤，然后走出了地牢。"

            "男爵的故事让你感到同情。但也仅止于同情。"

            "你不能因为理解一个敌人，就忘记他仍然是一个敌人。"

        "我能利用这一点。":
            $ change_stat("intrigue", 8)
            $ baron_blackmail_option = True
            $ log_decision("NPC支线", "打算利用男爵的过去")

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "有趣……非常有趣。"

            "你的大脑开始高速运转。男爵对王后的仇恨、他失去妻子的伤痛——这些都是可以被利用的弱点。"

            player "海因里希，你还知道关于艾玛夫人案件的更多细节吗？比如……参与审判的法官、伪证的证人？"

            $ hide_all_chars()
            "海因里希不安地看着你。"

            $ hide_all_chars("soldier_generic_img")
            show soldier_generic_img at left with dissolve
            heinrich "领主大人……您想做什么？"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我想做能做的事。如果男爵的仇恨能被引导——比如引导向正确的方向——那对所有人都是好事。不是吗？"

            $ hide_all_chars()
            "海因里希咬了咬嘴唇。他意识到自己可能说得太多了。"

            "但无论如何，信息已经在你手中了。男爵的痛处、他的执念、他那个被冤杀的妻子——这些都是棋局上有力的筹码。"

            "你可以用它们来谈判，用它们来威胁，甚至用它们来策反男爵——让他把刀转向王后。"

            "问题只在于：你愿意走多远？"

    "你离开地牢，回到了地面上。阳光刺得你眯了眯眼睛。"

    "男爵的故事你听完了。他那边怎么处理，你心里得有个数。"

    hide player_char_img with dissolve

    return

## ============================================================
## 第七弧线：暗百合首领的考验（约150行）
## 可在第三章调用，需 dark_lily_joined = True
## ============================================================

label npc_lily_test:

    if not dark_lily_joined:
        "你尚未加入暗百合，无法触发此事件。"
        return

    scene bg dungeon with dissolve

    "暗百合的地下据点。石壁上的火把发出幽暗的红光，将每个人的影子拉得又长又扭曲。"

    "你被召到了据点最深处的一间密室——暗百合首领亲自召见你。"

    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve

    lily_master "来了。坐。"

    "首领的声音从兜帽的阴影中传出，听不出年龄和情绪。面前的石桌上放着一壶酒和两只杯子。"

    lily_master "你加入暗百合已经有些时日了。我一直在观察你。"

    lily_master "你的能力毋庸置疑。但有一样东西，我还没有看清——你的判断力。"

    hide lily_master_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "判断力？"

    hide player_char_img
    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    lily_master "杀一个人容易。决定该不该杀一个人，难。"

    "首领将一份羊皮纸推到你面前。上面写着一个名字和几行潦草的笔迹。"

    lily_master "暗百合内部出了一个叛徒。代号「夜莺」。她一直在向王后出卖我们的情报。"

    lily_master "过去三个月，王后的密探至少四次精准地出现在我们的接头地点。每一次都是在「夜莺」参与了联络之后。"

    hide lily_master_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你查实了？"

    hide player_char_img
    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    lily_master "查实了。证据确凿。但这不是重点。"

    $ hide_all_chars()
    "首领拍了拍手。密室的侧门打开了，两个黑衣人押着一个蒙着头的人走进来。"

    "黑布被揭开。你看到的是一个年轻女人——大约二十五六岁，面色苍白，眼中有恐惧，也有一丝……坦然。"

    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    lily_master "这就是「夜莺」。真名玛莎。你来决定她的命运。"

    hide lily_master_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "等等——为什么让我来决定？"

    hide player_char_img
    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    lily_master "因为这是你的考验。暗百合不养没有判断力的人。"

    "你看着面前的年轻女人。她浑身发抖，但没有求饶。"

    hide lily_master_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "让我先和她谈谈。"

    "首领做了个手势，黑衣人退了出去。密室中只剩下你、首领和这个叫玛莎的女人。"

    player "玛莎，为什么出卖暗百合？"

    $ hide_all_chars()
    "她用沙哑的声音回答。"

    "玛莎 \"……我丈夫。他被王后的人抓了。关在王都的黑狱里。\""

    "玛莎 \"他们告诉我——如果我不给他们情报，我丈夫就会死。\""

    "你心中一沉。这不是一个简单的背叛故事。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你有孩子吗？"

    $ hide_all_chars()
    "玛莎 \"两个。最大的五岁，最小的……还在吃奶。\""

    "她的泪水终于落了下来。"

    "玛莎 \"我知道我背叛了暗百合。我做好了赴死的准备。但我的孩子……求你们……别牵连他们。\""

    "你转向暗百合首领。兜帽下看不清表情，但你感到首领也在审视着你的反应。"

    hide player_char_img
    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    lily_master "你听到了。一个叛徒，但理由是为了救自己的丈夫。如何处置？"

    $ hide_all_chars()
    "密室中陷入了沉寂。火把的噼啪声格外刺耳。你面前是一个年轻的母亲——一个为了丈夫而背叛组织的女人。"

    "这不是黑与白、对与错那么简单的事。"

    menu:
        "放她走。":
            $ change_stat("loyalty", 5)
            $ change_rel("rel_lily", 5)
            $ lily_traitor_fate = "released"
            $ log_decision("NPC支线", "放走了暗百合叛徒")

            hide lily_master_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "放她走。"

            hide player_char_img
            $ hide_all_chars("lily_master_img")
            show lily_master_img at left with dissolve
            lily_master "……理由？"

            hide lily_master_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "她不是为了钱，不是为了权力。她是为了救自己的家人。如果我们连这样的人都要杀——那我们和王后有什么区别？"

            player "暗百合存在的意义是什么？是维护弱者的利益。玛莎就是弱者之一。"

            $ hide_all_chars()
            "密室中寂静了很长时间。你甚至开始担心首领会不会翻脸。"

            "然后，一声低沉的笑从兜帽下传出。"

            hide player_char_img
            $ hide_all_chars("lily_master_img")
            show lily_master_img at left with dissolve
            lily_master "好。非常好。"

            lily_master "这个回答……比我预期的要好。"

            lily_master "大多数人面对叛徒只会想到惩罚。只有真正的领袖才会看到——惩罚一个被逼无奈的人，只会制造更多的敌人。"

            "首领站起身来，朝玛莎走去。玛莎惊恐地缩了一下，但首领只是轻轻拍了拍她的肩膀。"

            lily_master "玛莎。你走吧。带上你的孩子，离开这座城。去南方——那里暗百合的人会给你新的身份。"

            lily_master "至于你丈夫——我们会想办法。"

            $ hide_all_chars()
            "玛莎瘫坐在地上，泣不成声。"

            "你走出密室的时候，首领在背后说了一句：「你通过了。」"

            "你没有回头。但你知道——今天你做的这个决定，在暗百合中赢得的分量，比十次完美的任务都重。"

        "处决她。规矩就是规矩。":
            $ change_stat("power", 5)
            $ change_rel("rel_lily", 5)
            $ lily_traitor_fate = "executed"
            $ log_decision("NPC支线", "处决了暗百合叛徒")

            hide lily_master_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "处决她。"

            "玛莎浑身一震。你避开了她的目光。"

            player "我同情她的处境。但暗百合的纪律不能被践踏。如果背叛的代价只是一句「情有可原」，那以后谁都可以找借口出卖组织。"

            player "今天放过她，明天就会有第二个、第三个。"

            hide player_char_img
            $ hide_all_chars("lily_master_img")
            show lily_master_img at left with dissolve
            lily_master "……冷酷。但有道理。"

            "首领做了个手势。黑衣人重新进来，将哭泣的玛莎带走了。你不知道她最终的结局，也不想知道。"

            lily_master "你心里不舒服？"

            hide lily_master_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "不舒服。但这是必要的。"

            hide player_char_img
            $ hide_all_chars("lily_master_img")
            show lily_master_img at left with dissolve
            lily_master "是的。权力的本质就是做让自己不舒服的决定。"

            lily_master "你通过了。你没逃避，也没装作没听见——这就够了。"

            $ hide_all_chars()
            "你走出密室。走廊里回荡着远处隐约传来的哭声，像一根细针，扎在你心口。"

            "你告诉自己这是必要的。你重复了很多次。但今夜，你知道自己不会睡得好。"

        "利用她做双面间谍。":
            $ change_stat("intrigue", 10)
            $ change_rel("rel_lily", 3)
            $ lily_traitor_fate = "double_agent"
            $ lily_double_agent = True
            $ log_decision("NPC支线", "将叛徒变为双面间谍")

            hide lily_master_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "不杀她。也不放她走。利用她。"

            hide player_char_img
            $ hide_all_chars("lily_master_img")
            show lily_master_img at left with dissolve
            lily_master "……继续说。"

            hide lily_master_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "王后认为玛莎还在为她传递情报。我们不打破这个假象——反而通过玛莎向王后输送假情报。"

            player "真真假假掺在一起。七分真三分假。让王后基于错误的信息做出错误的判断。"

            "你能感到兜帽下的目光在反复审视你。"

            hide player_char_img
            $ hide_all_chars("lily_master_img")
            show lily_master_img at left with dissolve
            lily_master "风险很大。如果玛莎被识破，不仅她会死，我们的假情报渠道也会暴露。"

            hide lily_master_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "所以我们需要给她足够的动力。"

            "你转向玛莎。"

            player "玛莎。如果你愿意做双面间谍——向王后传递我们指定的情报——我们不仅不杀你，还会帮你救出你丈夫。"

            player "但如果你再次背叛……"

            $ hide_all_chars()
            "你没有说完。你不需要说完。"

            "玛莎看着你，眼中的恐惧慢慢被一种绝望的希望取代。"

            "玛莎 \"我……我愿意。只要能救我丈夫，你们让我做什么都行。\""

            hide player_char_img
            $ hide_all_chars("lily_master_img")
            show lily_master_img at left with dissolve
            lily_master "有胆识。也有算计。"

            "首领的语气中带着一丝赞许。"

            lily_master "好。就按你说的办。但玛莎，你从现在起只接受这位大人的直接指挥。"

            lily_master "如果你出了任何差错——不会有第二次机会。"

            $ hide_all_chars()
            "玛莎颤抖着点了点头。你在暗百合中多了一枚棋子——但这枚棋子是活的，有感情的，有软肋的。"

            "使用她的时候，你需要格外小心。"

    hide lily_master_img with dissolve

    "你从暗百合的据点出来，夜风吹在脸上，带来一丝清冷。"

    "地下的世界和地上的世界，规则从来都不一样。在那里，每一个决定都可能关乎生死。"

    "而你，正在学习如何在这两个世界之间游走。"

    return

## ============================================================
## 辅助入口：支线选择菜单
## 可在各章节通过 call npc_sideline_menu 调用
## ============================================================

label npc_sideline_menu:

    "你有一些空闲时间，可以去拜访领地中的人们。"

    menu:
        "去找奥尔德里克聊聊" if not aldric_personal_done:
            call npc_aldric_secret from _call_npc_aldric_secret

        "去找雷恩队长" if not captain_past_done:
            call npc_captain_past from _call_npc_captain_past

        "去找艾琳娜" if not elena_dark_past_done:
            call npc_elena_past from _call_npc_elena_past

        "去见主教马修斯" if not bishop_confession_done:
            call npc_bishop_confession from _call_npc_bishop_confession

        "去石泉村看看" if not village_elder_quest_done:
            call npc_village_quest from _call_npc_village_quest

        "审讯男爵的俘虏" if not baron_honor_known:
            call npc_baron_honor from _call_npc_baron_honor

        "前往暗百合据点" if not dark_lily_joined and not dark_lily_destroyed:
            "你尚未与暗百合建立联系。"

        "前往暗百合据点" if dark_lily_joined and lily_traitor_fate == "":
            call npc_lily_test from _call_npc_lily_test

        "暂时不去找任何人":
            pass

    return

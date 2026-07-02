## ============================================================
## 第四章：王都风云
## ============================================================

label chapter4_start:

    ## 安全重置：防止上一章过场动画的 _dismiss_pause 泄漏
    $ _dismiss_pause = True
    $ quick_menu = True
    window auto

    $ renpy.force_autosave()
    $ snapshot_chapter_start()
    scene black with fade

    call show_chapter("第四章", "王都风云", "踏入更大的棋局") from _call_show_chapter_2
    call show_recap("chapter3") from _call_show_recap_2
    call apply_rel_chapter_effects from _call_rel_ch4

    ## 章节间过渡：王后传召信件 + 出发前夜 Elena 坦白
    ## (必须在 cinematic_chapter4 之前——cinematic 画的是"城门开启+royal_palace 远景"
    ## 即启程画面, 若放在 interlude 之前会出现"画面已到王都, 又被拉回艾登堡书房"的时序错乱)
    call interlude_ch3_ch4 from _call_interlude34
    call interlude_ch3_ch4_confession from _call_interlude34_conf

    ## 章节过场动画 (启程: 城门开启 → 王都远景)
    call cinematic_chapter4 from _call_cinematic_ch4

    ## NPC深度支线
    call npc_elena_homeland from _call_npc_eh

    ## NPC支线：男爵的隐藏荣誉
    call npc_baron_honor from _call_npc_bh4

    ## 章节深化场景移到"抵达王都并入住"之后再触发
    ## (下方 L747 附近)，避免在艾登堡出发前就出现"到达王都第三夜"的时间错乱

    $ trigger_random_event("travel")

    "从艾登堡到王都，骑马需要五天。"

    ## ============================================================
    ## 旅途第一天：启程
    ## ============================================================

    $ play_music("audio/music/castle_calm.ogg", fadein=2.0)
    scene bg castle_exterior with dissolve
    $ unlock_gallery("bg_castle_exterior")
    $ set_mood("calm")

    "出发那天清晨，天色还未大亮。"

    "艾登堡的城门在晨雾中缓缓打开，铁链发出沉闷的声响。"

    "你骑在马上，回头望了一眼自己的城堡。晨光勾勒出塔楼的轮廓，巨大而沉静。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    $ unlock_gallery("captain")

    captain "领主大人，护卫队已经集结完毕。二十名骑兵，十名步兵，足够应对路上的意外。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "辎重呢？"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "两辆马车。一辆装觐见的礼物和衣物，一辆装干粮和帐篷。"

    captain "按照行程，我们每天赶六十里路，第五天傍晚应该能到王都。"

    hide captain_img with dissolve

    show elena_img at right with dissolve
    $ unlock_gallery("elena")

    elena "领主大人，路上有几个地方需要注意。"

    elena "第二天会经过哈伦堡，那里是中立领地，可以补给。"

    elena "第三天进入王室直辖领地后，沿途会有驿站。但也会有更多的眼线。"

    if dark_lily_joined:
        elena "暗百合在沿途安排了三个接应点。如果遇到危险，我们可以迅速转移。"
    else:
        elena "我之前做情报工作时走过几次这条路，沿途有几条隐蔽的岔道。万一遇到麻烦，可以迅速脱离。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你对王都的路线很熟悉。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "我曾经……经常走这条路。"

    "她的语气里有一丝你捕捉不到的情绪。你没有追问。"

    hide elena_img with dissolve

    $ hide_all_chars()
    "队伍缓缓出发。马蹄声在晨雾中回荡，沉重而有节奏。"

    "你最后一次回头，看到奥尔德里克站在城墙上，目送你远去。"

    "老骑士没有挥手，只是静静地站着，身体挺得很直。"

    if not dark_lily_joined:
        "你忽然想起，城镇酒馆里曾有老兵说过：「别看奥尔德里克现在是个管家，当年他替先王办的那些差事，知道的人早就入土了。」"
        "你一直当作是醉话。但经历了这么多事之后，你开始觉得这个老骑士可能比你想象的复杂得多。"
    else:
        "你回头望着城墙上的身影，心里默默盘算着暗百合的据点位置。有他们在暗处接应，这一路至少不会是孤军深入。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    $ unlock_gallery("aldric")

    aldric "（远远地喊）一路平安，领主大人。艾登堡等您回来。"

    hide aldric_img with dissolve

    "你点了点头，转过身去，策马前行。"

    if deep_marcus_confession == "exploit":

        $ hide_all_chars("elena_img")
        show elena_img at right with dissolve

        elena "领主大人……上次您托我留意的那个人，最后的消息半月前传回来了。之后就再无动静。"

        elena "伯爵那边应该……已经没什么用了。"

        $ hide_all_chars()
        "你没有回答。队伍继续向前。"

    ## ============================================================
    ## 旅途第二天：路上的对话
    ## ============================================================

    $ play_music("audio/music/forest_ambient.ogg", fadein=2.0)
    scene bg forest_path with dissolve
    $ unlock_gallery("bg_forest_path")

    "第二天，队伍穿过一片古老的橡树林。"

    "树冠遮天蔽日，阳光像碎金一样洒落在林间小道上。"

    "空气中弥漫着泥土和落叶的气息，偶尔能听到远处的鸟鸣。"

    "这片森林据说有三百年的历史，是先王狩猎的皇家猎场。"

    "如今，它只是一条通往王都的必经之路。"

    $ play_sound("audio/sfx/horse_gallop.ogg")

    show elena_img at right with dissolve

    "艾琳娜催马上前，与你并辔而行。"

    elena "领主大人，趁路上有空，我想和您谈谈觐见的事。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你说。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "伊莎贝拉王后……不是一个简单的女人。"

    elena "先王驾崩后，她以摄政之名执掌大权，至今已有二十年。"

    elena "在这二十年里，她铲除了至少五位不服从的领主。有的被指控叛国，有的……不明不白地死了。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "包括我父亲？"

    "艾琳娜的目光闪了一下。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "也许。但我目前没有证据。"

    elena "我想说的是——在王后面前，千万不要暴露你的底牌。"

    elena "她会用各种手段试探你——恩威并施，软硬兼施。你必须像一面镜子，让她只能看到自己想看到的东西。"

    ## batch 14 反馈"编辑部替补" (2026-05-11) #2 王后逻辑 lore explain:
    ## 解释王后"奢侈+欠军费" 内在矛盾 — 是政治姿态不是个人欲望
    elena "还有一件事——您可能会觉得奇怪。王后宫廷里满是金银帷幔，王室国库却年年向贵族借钱发军饷。"

    elena "这不是她贪。是她故意做给底下贵族看的： 「王室还撑得起这种排场，你们就别想着我们已经穷到要让步。」"

    elena "二十年了，这套排场是她压住北方领主的关键。您觐见的时候，不要把「欠军费」当作王室软弱——她会用您的判断反过来试探您。"

    menu:
        "向艾琳娜询问更多关于王后的事":
            $ change_stat("intrigue", 5)
            $ change_rel("rel_elena", 5)
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你似乎对王后非常了解。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            if elena_spy_known:
                elena "我在她身边待过好几年——这你已经知道了。"
                elena "但了解一个人和面对一个人是两回事。我想告诉你一些……实用的东西。"
            else:
                elena "……因为我曾经在她身边待过。"
                hide elena_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "什么意思？"
                hide player_char_img
                $ hide_all_chars("elena_img")
                show elena_img at left with dissolve
                elena "我在暗百合之前，最早是王后的侍女。她从小培养我，教我读书、骑马、用毒……"
                elena "然后把我送到各个领主身边，充当她的耳目。"
                hide elena_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "所以你来艾登堡，也是她的安排？"
                hide player_char_img
                $ hide_all_chars("elena_img")
                show elena_img at left with dissolve
                elena "最初是。但后来……"
                "她下意识看了一眼门口，确认没有第三个人。"
                elena "后来的事情变得复杂了。"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            if elena_spy_known:
                player "你真的不再听命于王后了？到了她的地盘上……我需要确认。"
                hide player_char_img
                $ hide_all_chars("elena_img")
                show elena_img at left with dissolve
                elena "我在出发前那晚已经把一切告诉您了。我的答案不会变。"
                elena "何况——王后若知道我背叛了她，等着我的可比等着您的更狠。"
            else:
                player "你现在——为谁效力？"
                hide player_char_img
                $ hide_all_chars("elena_img")
                show elena_img at left with dissolve
                elena "这个问题，等我想清楚了再回答您。"

        "提醒自己保持警惕":
            $ change_stat("intrigue", 3)
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我记住了。谢谢你的忠告。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "不客气。保护您也是在保护我自己。"

        "问她王都有哪些值得注意的人物" if intrigue >= 45:
            $ change_stat("intrigue", 8)
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "除了王后，王都里还有谁需要注意？"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "弗雷德里克王子。先王唯一的儿子，今年二十二岁。"
            elena "他名义上是储君，但王后一直把持着权力，不肯还政于他。"
            elena "据说王子对此很不满，但他很聪明，从不公开表达不满。"
            elena "还有宫廷宰相蒙塔古伯爵——他是王后最忠诚的臣子，也是王室军队的统帅。"
            elena "最后是教廷驻王都的特使。教会在王都的影响力比你想象的大得多。"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "真是一团乱麻。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "王都从来不缺乱麻。缺的是能解开它们的人。"

    hide elena_img with dissolve

    $ hide_all_chars()
    "队伍继续前行。你的脑海中不断盘算着即将面对的局面。"

    "午后，你们路过一个小村庄。"

    "村子很穷。茅草屋顶上覆盖着苔藓，泥泞的道路两旁是几头瘦骨嶙峋的牛。"

    "一群孩子站在路边，好奇地看着你的队伍经过。"

    "一个衣衫褴褛的老乞丐跪在路边，向你的方向磕头。他脸上满是污垢，身后跟着几个更瘦的孩子。"

    $ hide_all_chars("beggar_img")
    show beggar_img at left with dissolve
    beggar "贵人行行好……我们三天没吃东西了……"

    menu:
        "命令队伍停下，分发一些干粮":
            $ change_stat("loyalty", 5)
            $ change_stat("reputation", 5)
            $ change_stat("wealth", -3)
            hide beggar_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "停下。把一车干粮分给村民。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "可是领主大人，这些是我们五天的口粮……"
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "到了哈伦堡可以补给。他们不行。"
            $ hide_all_chars()
            "士兵们开始分发食物。村民们跪了一地，泪流满面。"
            "一个孩子跑过来，往你手里塞了一朵野花。"
            "你把花别在马鞍上，继续前行。"

        "抛下几枚银币，不做停留":
            $ change_stat("wealth", -1)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "给他们一些银币。我们不能耽搁。"
            $ hide_all_chars()
            "你丢下一小袋银币，队伍没有放慢速度。"
            "你回头看了一眼——村民们正在争抢那些银币。"
            "你心里有些不是滋味。"

        "不停留，继续赶路":
            $ change_stat("power", 2)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "不要停。我们有正事要办。"
            $ hide_all_chars()
            "队伍从村庄旁边呼啸而过，扬起一片尘土。"
            "你没有回头。"

    ## ============================================================
    ## 旅途第三天：夜间扎营
    ## ============================================================

    $ play_music("audio/music/campfire.ogg", fadein=2.0)
    scene bg forest_path with dissolve
    $ unlock_gallery("bg_forest_path")

    "第三天夜晚，队伍在一片空地上扎营。"

    "篝火噼啪作响，火星飞舞，在黑暗的树冠下像无数只萤火虫。"

    $ play_sound("audio/sfx/fire_crackle.ogg")

    "士兵们三三两两地围坐在火堆旁，低声交谈。有人在擦拭武器，有人已经裹着毯子睡着了。"

    "你独自坐在一棵大树下，翻看着从父亲书房中带来的文件。"

    "这些文件记录了父亲与王都之间长达十年的通信。大部分是例行公事——税务报告、兵员呈报、边境巡查记录。"

    "但有几封信的措辞很奇怪。字面上是在讨论庄稼收成，但用词之间暗藏着另一层意思。"

    if father_letters_found:
        "你把这些信件和之前在书房密格中找到的文件对照，发现了一些惊人的巧合——"
        "父亲提到的「第七次收成不佳」，对应着密码日记中「暗百合第七次联」的记录。"
        "父亲在用粮食收成的隐喻，和某个人交换着关于暗百合的情报。"
        "那个人……是谁？"
        $ change_stat("intrigue", 5)

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "领主大人，该休息了。明天还要赶路。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "雷恩，你觉得王都是什么样的地方？"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "嗯……我去过一次，跟着老领主。那时候我还是个新兵。"

    captain "怎么说呢——又大又吵。到处是人，到处是马车，空气里全是烤面包和马粪的味道。"

    captain "但最让我不舒服的是那些贵族的眼神。他们看人的方式……好像在看一件商品。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "所以你不喜欢王都？"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "我是个武人，大人。我喜欢简单的东西。敌人在前面，我拔剑迎上去。"

    captain "王都的那些弯弯绕绕，不适合我。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "但适合我？"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "老领主能在那些人中间周旋了一辈子，您肯定也行。"

    captain "况且——您还有我们保护您的安全，不是吗？"

    "雷恩笑了，露出他那排被风吹日晒得有些发黄的牙齿。"

    $ hide_all_chars("captain_img")
    show captain_img happy at left with dissolve

    "你不禁也笑了。"

    hide captain_img with dissolve

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve

    "夜深了，大部分人都已入睡。艾琳娜却还醒着，坐在火堆对面，目光落在跳动的火焰上。"

    elena "睡不着？"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "太多事情要想。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "领主大人……你有没有想过，如果你不是领主，你会做什么？"

    menu:
        "会做一个旅行者，去看看这个世界":
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "也许会骑着马，走遍每一个城镇和村庄。看看不同的人过着什么样的日子。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "听起来……很自由。"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你呢？如果你不是……你现在的身份，你想做什么？"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "我想开一家小酒馆。在某个没有人认识我的小镇上。"
            elena "每天做做饭，和客人聊聊天。不用防备任何人。"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "也许有一天你可以。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "也许吧。"
            "她轻轻嗯了一声，但眼底的忧郁没有散去。"
            $ change_rel("rel_elena", 5)

        "没想过。我生来就是领主的儿子":
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我从来没有选择的余地。生在这个家庭，就注定了这条路。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "……也是。我也一样。"
            elena "有些人的命运，从出生的那一刻就被写好了。"
            "火堆中的木头塌了一块，溅起一串火星。"
            $ change_rel("rel_elena", 3)

        "会做一个学者，去研究古代的历史":
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我对父亲书房里那些古老的文献很感兴趣。也许会去王都的大图书馆，当一个默默无闻的学者。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "你的气质确实更像学者，而不是领主。"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "这是夸奖还是批评？"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "是观察。学者有学者的力量——他们用知识改变世界，而不是用刀剑。"
            $ change_stat("intrigue", 3)
            $ change_rel("rel_elena", 5)

    hide elena_img with dissolve

    $ hide_all_chars()
    "你最终还是躺下了。星星从树缝中透出来，闪闪烁烁。"

    "明天，队伍就要进入王室直辖领地了。"

    "你闭上眼睛，在虫鸣和火焰的低语中，缓缓入睡。"

    ## ============================================================
    ## 旅途第四天：王室直辖领地
    ## ============================================================

    $ play_music("audio/music/forest_ambient.ogg", fadein=2.0)
    scene bg forest_path with dissolve

    "第四天。"


    "昨夜还是参差的山路和野生的灌木丛，今早眼前却是笔直的石板大道和修剪齐整的行道树。"

    "你们已经进入了王室直辖领地。"

    "路面从泥土变成了平整的石板，道旁每隔百步便立着一根刻有王室徽记的石柱。远处的田野齐整得不见一丝杂乱，金黄的麦浪一望无际。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "从这里开始，每一座驿站都有王室的耳目。说话做事，都要比昨天更小心。"

    hide elena_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "前方两里有个驿站。要不要停下来补给？"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve

    menu:
        "塞几枚银币让驿站管事「忘记」我们路过" if wealth >= 50:
            $ change_stat("wealth", -3)
            $ change_stat("intrigue", 5)
            $ change_rel("rel_captain", -10)

            player "雷恩，停一下。我去后院。"

            hide player_char_img with dissolve
            $ hide_all_chars()
            "你下马，走到驿站后院。管事正在给一匹瘦马刷毛——见你来，手立刻顿住。"

            "你没说话，从腰间钱袋里取出五枚银币，慢慢摆在草料桶边沿上。"

            "管事的目光落在银币上。"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我们没在这里停过。马也没饮过你这里的水。"

            $ hide_all_chars()
            "管事低头沉默了三秒，伸手把银币扫进了围裙口袋。"

            "「……驿站今天没接客。明早换班的人也不会知道有谁路过。」"

            "你回到队伍前，没多说一个字。"

            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "你刚才——?"

            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "塞了几个银币。让他报上去的时候漏掉我们这一队。"

            player "五个银币换一晚的安静——这买卖划算。"
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "划算。可那管事要是被王后的人一吓，照样把咱们抖出去。买来的嘴，不牢。"
            hide captain_img with dissolve

        "停下补给，顺便打探消息":
            $ change_stat("intrigue", 4)

            player "停一下。水袋也该灌满了。"

            hide player_char_img with dissolve

            $ hide_all_chars()
            "驿站不大，但异常整洁——木桌擦得发亮，墙上挂着王室的旗帜。"

            "驿站的管事是个面色红润的中年人，笑容热情得过了头。他一边替你们灌水，一边不停地打量队伍中的每个人。"

            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "注意到了吗？他数了三遍我们有多少人。"

            hide elena_img with dissolve

            "离开驿站后，艾琳娜压低了声音。"

            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "他会把我们的人数、行进方向、甚至您的长相报告上去。到王都之前，王后就会知道您来了。"

            hide elena_img with dissolve

        "不停，直接赶路":
            $ change_stat("power", 2)
            $ change_stat("intrigue", -8)

            player "不停了。越少和人接触越好。"

            hide player_char_img with dissolve

            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "明白。全队加速！"
            hide captain_img with dissolve

            "队伍绕过驿站，沿着大道继续前行。路上遇到几队巡逻的王室骑兵——他们远远地注视着你们，但没有上前盘问。"

            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "他们记住了我们的旗帜。不过没关系，到了这里，想隐藏行踪本来就不现实。"
            elena "只是这一路绕开了所有人，王都那边什么风声您也没听着。进城之前，咱们等于是蒙着眼。"
            hide elena_img with dissolve

    $ hide_all_chars()
    "午后，一支挂着陌生旗帜的车队从对面驶来。华丽的马车、全副武装的护卫——显然也是某位前往王都的贵族。"

    "对方的车队缓缓靠边让路。车帘掀起一角，一双眼睛打量了你片刻，便放下了帘子。"

    "没有人打招呼。在王室直辖领地的大道上，陌生贵族之间保持距离是一种默契——你不知道对方站在哪一边。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "认出那面旗了。是北方海因里希伯爵的家徽。"

    captain "他也去王都……看来不只我们收到了召见。"
    hide captain_img with dissolve

    $ hide_all_chars()
    "傍晚时分，队伍在一座废弃的路边神坛旁扎营。石砌的神坛已经长满了青苔，但圣母的雕像依然完好。"

    "你坐在神坛的台阶上，看着远方的地平线。王都就在那个方向——明天傍晚，你就能看到它的城墙了。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "明天到了王都，一切都会不一样。在那里，笑容是武器，沉默是盾牌。"

    elena "记住——不要轻信任何人的善意。包括那些看起来最真诚的人。"
    hide elena_img with dissolve

    $ hide_all_chars()
    "夜风从平原上吹来，带着麦田和泥土的气息。比山林里的风更温暖，也更沉重。"

    "你裹紧披风，闭上了眼睛。"

    "明天，王都。"

    ## ============================================================
    ## 旅途第五天：抵达王都
    ## ============================================================

    $ play_music("audio/music/great_hall.ogg", fadein=3.0)
    scene bg royal_palace with dissolve
    $ unlock_gallery("bg_royal_palace")

    "第五天傍晚。"

    "当队伍翻过最后一道山丘时，王都终于出现在你的视野中。"

    "你不由自主地勒住了马缰。"

    "王都——赫尔曼斯堡。"

    "一座建在平原上的巨城，城墙高达四十尺，用灰白色的巨石砌成，在夕阳下泛着金色的光芒。"

    "城墙上旌旗猎猎，每隔五十步就有一座瞭望塔，塔尖上闪烁着信号灯的微光。"

    "城内，高耸的尖塔和穹顶层层叠叠，像一片由石头长成的森林。"

    "最显眼的是王宫——坐落在城市中央的一座小山上，白色的宫殿群像一顶巨大的王冠，俯视着整座城市。"

    "旁边是大教堂的双塔，高耸入云，塔尖的金色十字架在余晖中燃烧般闪耀。"

    "城外是绵延数里的市集和民居。数不清的马车和行人在城门口排起了长队。"

    "你从未见过这样的景象。艾登堡和它相比，不过是棋盘角落里的一颗小卒。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "领主大人……这就是王都啊。"

    "雷恩的眼睛瞪得像铜铃，嘴巴微微张着。"

    captain "我上次来的时候还没这么大。他们又扩建了？"

    hide captain_img with dissolve

    show elena_img at right with dissolve

    elena "城墙是三年前重修的。王后花了整整一年的税收来建造它。"

    elena "据说可以抵挡十万大军围攻一年。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "难怪税那么重。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "王后的野心和她的城墙一样大。"

    "她的声音里有一种复杂的情绪——敬畏中夹杂着厌恶。"

    hide elena_img with dissolve

    $ hide_all_chars()
    "王都的城门比你记忆中更高。或者是你变矮了。"

    "你策马缓缓走向城门。城墙越来越近，越来越高。"

    "城门口的卫兵验过你的通行令牌后，向你行了一个军礼。"

    $ hide_all_chars("soldier_generic_img")
    show soldier_generic_img at left with dissolve
    soldier "艾登堡领主阁下，王宫已为您安排了住所。请随侍从前往。"

    $ hide_all_chars()
    "进入城门的那一刻，喧嚣像潮水般扑面而来。"

    "叫卖声、马蹄声、车轮碾过石板路的咕噜声、孩子的笑闹声、铁匠铺里的叮当声——"

    "所有的声音混在一起，形成了一种你从未体验过的嘈杂。"

    "街道两旁是密密麻麻的房屋，三层甚至四层的木石建筑鳞次栉比。"

    "商铺的招牌在微风中轻轻摇晃——铁匠铺、面包店、裁缝铺、药材行、珠宝商……"

    "偶尔能看到穿着华丽的贵族乘坐马车经过，车厢上镶着家族徽章。"

    "也有衣衫褴褛的乞丐蜷缩在墙角，用空洞的眼神看着这个繁华的世界。"

    "你注意到，王都的繁华和贫穷就这样贴在一起。"

    menu:
        "仔细观察街道上的人群":
            $ change_stat("intrigue", 5)
            "你放慢马速，目光扫视着街道两侧的每一个角落。"
            "你注意到街角站着几个身着便装的人，但他们的站姿和眼神出卖了他们——那是训练有素的暗哨。"
            "你还注意到，有些商铺的门口挂着一种特殊的铃铛——据说那是向王宫密探缴纳过「保护费」的标记。"
            "这座城市的每一块石板下面，都埋藏着秘密。"

        "直奔王宫安排的住所":
            $ change_stat("power", 3)
            "你催马前行，不让任何事情分散你的注意力。"
            "你需要在觐见之前好好休息，理清思路。"

        "观察城防布置":
            $ change_stat("power", 5)
            "你用军事的眼光打量着城墙和街道。"
            "城防部署严密——每个路口都有巡逻队，城墙上的弓箭手视野开阔。"
            "但你也注意到了一些弱点：南门的城墙有一处裂缝被草草修补过，城西的排水渠宽度足够一个人爬过。"
            "这些信息也许将来会有用。"

    "侍从引着你穿过一条又一条街道，最终来到王宫旁的贵宾馆。"

    "那是一座小巧精致的二层石楼，门口有两名王室卫兵站岗。"

    "你的卫队被安排在附近的营房。只有雷恩和艾琳娜被允许随你住进贵宾馆。"

    "房间出乎意料地豪华——丝绸的床单、银质的烛台、墙上挂着名家绘制的风景画。"

    "但你知道，这种豪华背后，可能藏着无数双耳朵。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve

    elena "这里有至少三个暗格可以藏人。窗帘后面、壁炉上方的通风口、还有床下的地板。"

    elena "我会把它们都检查一遍。在那之前——"

    elena "说话请小声。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你对这种地方太熟悉了。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "经验之谈。"

    hide elena_img with dissolve

    $ hide_all_chars()
    "你站在窗前，俯瞰着王都。城里的灯火逐渐亮了起来。"

    "过几日，你将觐见伊莎贝拉王后。在此之前，你要看清这座城市。"

    "你深吸一口气，告诉自己——无论发生什么，都不能露出破绽。"

    "当夜，你被安排在客房歇息。枕头散着檀木与薄荷的气味，柔软得让人警觉。"

    "接下来的几日，你游走于王都的街巷、庙堂与酒馆之间——白天陪同礼典官熟悉觐见流程，夜里独自在宫墙的阴影里聆听。"

    ## 章节深化场景（原本错误地在艾登堡出发前就 call，移到这里——
    ## 主角已抵达王都且入住贵宾馆，后续几天内发生的观察与线索）
    call ch4_deep_queen_weakness from _call_ch4_dqw
    call ch4_deep_poet from _call_ch4_dpoet
    call ch4_deep_dungeon_echo from _call_ch4_dde

    "你想起这些晚上看到、听到的一切。它们将决定你下一步怎么走。"

    ## ============================================================
    ## 第四章扩展：王都探索与觐见准备
    ## ============================================================
    call ch4_exp_arrival from _call_ch4_exp_arrival
    call ch4_exp_explore from _call_ch4_exp_explore
    call ch4_exp_court_social from _call_ch4_exp_court_social
    call ch4_exp_investigation from _call_ch4_exp_investigation
    call ch4_exp_eve from _call_ch4_exp_eve

    ## ── 鹰卫信使网络支线 · 引入 ──
    $ hide_all_chars()
    "王都的最后一夜，你拐进一家不起眼的酒馆避雨。"
    "角落里坐着一个灰斗篷的人，帽檐压得很低，面前一杯酒一口都没喝。"
    "你本不会多看他一眼。但他搁在桌上的左手——食指内侧，有一道浅疤，形状像一只展翅的鸟。"
    if knows_eagle_network:
        "鹰卫的暗记。和《六卫终录》里记录的一模一样。先王的鹰卫解散了，可这张信息网没断——而你，恰好认得这道疤。"
        menu:
            "上前接头":
                "你在他对面坐下，压低声音说了半句不相干的话——你赌他会接下半句。"
                "他抬眼，在你脸上停了一瞬，然后用同样低的声音接了上来。"
                "「……好久没人对得上这句了。」他说。"
                "鹰卫的信使。先王的传讯网，到今天还存在。你刚刚重启了它。"
                $ eagle_network = True
                $ change_stat("intrigue", 2)
                "「想要什么，写下来，交给任何一家门口挂铜铃的酒馆伙计。三天内有回音。」"
                "「但这网是先王留下的，不是你的私产。用一次，欠一次人情。别透支。」"
                "「头一笔人情，现在就还。门口挂铜铃那几家酒馆，伙计要打点，信鸽要喂，你出。」"
                "你数出一小袋银钱压在桌角。这张网不白用——你刚替自己买下了它第一次开口的价钱。"
                $ change_stat("wealth", -15)
                "他丢下几枚铜板，起身走进雨里。你没有回头看他。"
            "记下他，先不打草惊蛇":
                $ change_stat("intrigue", 2)
                "你没有过去。你只是把他的脸、那道疤、他坐的位置，都记进了脑子里。"
                "你没动用它，也就没欠它人情。你正要去觐见王后——一个王后的封臣，身上挂着先王旧部的暗线，这事现在不能沾。"
                "但你认得这道疤了。这张网就在王都，真到了走投无路那天，你找得回来。"
    else:
        "灰斗篷的人喝光杯里的酒，起身，走进雨里。你多看了一眼，没看出什么名堂。"

    ## ============================================================
    ## 场景1：王宫 - 觐见前
    ## ============================================================

label ch4_palace:

    $ play_music("audio/music/great_hall.ogg", fadein=2.0)
    scene bg royal_palace with dissolve
    $ unlock_gallery("bg_royal_palace")
    $ set_mood("normal")

    ## ── 政治联姻线「盟约」· 王都会面 ──
    if marriage_route:
        scene bg royal_palace with dissolve
        "觐见之前，你先见了另一个人。"

        "英格丽随北疆议会的代表团一起到了王都，住在使馆区。希尔达没来——按她信里的话，『谈盟约不需要母亲在场，需要的是你们俩能不能共事』。"

        $ hide_all_chars("ingrid_img")
        show ingrid_img at left with dissolve
        ingrid "艾登堡的继承人。比传闻里年轻。"

        hide ingrid_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "传闻里我什么样？"

        hide player_char_img
        $ hide_all_chars("ingrid_img")
        show ingrid_img at left with dissolve
        ingrid "心狠，或者心软，看是谁在说。北边的人押不准你，所以母亲让我来看。"
        ingrid "我把话说在前头。这桩婚事我不指望感情。我要的是北境的盐路重新通，要的是开春后议会不再饿肚子。你要什么，你自己清楚。"

        hide ingrid_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve

        menu:
            "把它当成纯粹的盟约，各取所需":
                $ marriage_warm = False
                $ log_decision("第四章", "联姻——纯粹的政治盟约")
                player "那我们就把话挑明。我出兵和粮，议会给我北境的忠诚。婚约是封口的火漆，不是感情。"
                hide player_char_img
                $ hide_all_chars("ingrid_img")
                show ingrid_img at left with dissolve
                ingrid "痛快。我喜欢不绕弯的人。"

            "盟约可以谈，但我想先认识你这个人":
                $ marriage_warm = True
                $ log_decision("第四章", "联姻——愿意认识英格丽本人")
                $ change_stat("intrigue", 2)
                player "盟约我答应。但既然要共度一生，我想知道我娶的是个什么样的人，而不只是一纸条款。"
                $ hide_all_chars("ingrid_img")
                show ingrid_img at left with dissolve
                "英格丽愣了一下。她大概没料到这句。"
                ingrid "……北边的男人不问这个。他们只问嫁妆和兵力。"
                ingrid "你要是真想知道，那就慢慢看。我不是一封信能写完的人。"

        $ hide_all_chars()

    ## ── 联姻拖延的后果（批31: 「先拖着」不再静默等同婉拒） ──
    if ch3_marriage_delayed and not marriage_route:
        "在王都的第二天，一个风尘仆仆的北疆信使追上了你。火漆还是那枚渡鸦纹。"

        "『艾登堡的继承人：北境等不到你「弄清楚」的那一天。盐路一天不通，议会一天在失血。』"

        "『提议就此作罢。愿你南边的事，办得比北边利落。——希尔达』"

        $ change_rel("rel_hilda", -3)

    "几日筹备过后——觐见的日子到了。"

    ## ── 鹰卫信使网络支线 · 兑现(觐见前送来王后底牌) ──
    if eagle_network:
        "觐见的前一夜，你客房的窗台上多了一只小铜铃，底下压着一张没有署名的纸条。"
        "字迹潦草，是鹰卫信息网的回音——"
        "「她要的不是你的忠诚，是你的刀。北境的男爵她容不下，想借你的手除掉。明天她会试你——看你是听话的狗，还是会咬人的狼。」"
        "你把纸条凑到烛火上，看它烧成灰，落进铜盆。"
        "你现在知道她要什么了。这场觐见，你不是没准备走进去的。"
        $ change_stat("intrigue", 3)
        $ eagle_intel = True

    ## ── 卡尔复仇支线兑现: 七人走私名单 (批31, 仿 eagle_intel 模式) ──
    if karl_full_story:
        "行囊夹层里还缝着一样东西——卡尔给你的那份名单。七个名字，一条从南方港口一直通到王宫膳房的走私链。"
        "真到了对质的那一步，王后的账，不只写在王座上。"
        $ change_stat("intrigue", 2)

    "天还未亮，内侍已在门外轻声传话——「王后陛下于巳时在王座大厅召见艾登堡领主。」"

    "你一早就醒了。窗外，王都的钟塔敲了六下——清脆的钟声在晨光中回荡。"

    if ch4_deep_queen_weakness:
        "那夜走廊里那个在画像前落泪的女人，今晨将重新戴上铁的面具。你也必须戴上你的。"

    $ play_sound("audio/sfx/bell_toll.ogg")

    "你穿上了从艾登堡带来的最好的衣服——深蓝色的丝绒外套，银线绣着艾登堡的家徽——一只展翅的金鹰。"

    "镜子里的你看起来……还算像一个领主。年轻，但不失威严。"

    show elena_img at right with dissolve

    elena "领主大人，觐见的时间是巳时。在那之前，有几位前来拜访的贵族等在客厅。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "哪些人？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "格雷伯爵、南方的威尔斯子爵，还有一位自称是教廷特使随从的人。"

    elena "他们来得这么早，恐怕不只是出于礼貌。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "让他们等着。我先见格雷伯爵。"

    hide elena_img with dissolve

    $ hide_all_chars()
    "格雷伯爵穿着一件剪裁考究但朴素的深灰色长袍，花白的胡须修剪得一丝不苟。六十七岁的老伯爵虽然身形微胖，但举手投足间自有一股学者的沉稳气度。"

    "他看到你时微微点头，浑浊的老眼中闪过一丝精明的光。"

    hide player_char_img
    $ hide_all_chars("count_grey_img")
    show count_grey_img at left with dissolve
    if wedding_attended:
        count_grey "又见面了，领主大人！婚宴上那半个时辰，老夫可还记得。"
        if grey_support_promised:
            count_grey "我许过的话作数——下次领主会议，老夫支持您的提案。今天来，是老夫也有一事相托。"
        else:
            count_grey "你我算是熟人了，不必寒暄。"
    elif grey_met:
        count_grey "又见面了，领主大人！"
        count_grey "自上次会议一别，听闻您在艾登堡做得风生水起，果然名不虚传。"
    else:
        count_grey "领主大人！终于见到您了！"
        count_grey "久闻艾登堡新主英明果决，今日一见，果然仪表堂堂！"

    hide count_grey_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "伯爵过奖了。不知伯爵前来，有何赐教？"

    hide player_char_img
    $ hide_all_chars("count_grey_img")
    show count_grey_img at left with dissolve
    count_grey "赐教不敢当。只是听说您也要觐见王后，想提前和您打个招呼。"

    count_grey "觐见时，王后可能会提到边境军费分摊的事。如果您能在那个议题上支持我的提案……"

    count_grey "伯爵府的门，将永远为您敞开。"

    menu:
        "以平等姿态回应——你的名声已传到王都" if reputation >= 60:
            $ change_stat("reputation", 3)
            $ change_rel("rel_grey", 5)
            hide count_grey_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "伯爵，互相帮助是好事。但您也清楚——艾登堡的名声这一年也传到了王都。"
            player "我们之间不是一方求另一方的关系。是同盟。"
            hide player_char_img
            $ hide_all_chars("count_grey_img")
            show count_grey_img at left with dissolve
            count_grey "哈哈……果然不能拿对待新人的态度看你。"
            count_grey "好。同盟。改日设宴，我请你喝艾登堡进贡的那种红酒——你应该比我更熟悉它的味道。"
            "格雷伯爵这一次的笑意终于到了眼底。这是声望的价值——别人不再把你当作可施舍的对象。"

        "答应帮忙，换取将来的支持":
            $ change_stat("intrigue", 5)
            $ change_stat("reputation", 3)
            hide count_grey_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "伯爵的提案，我愿意考虑。但相应地，也许将来艾登堡需要帮助的时候……"
            hide player_char_img
            $ hide_all_chars("count_grey_img")
            show count_grey_img at left with dissolve
            count_grey "那是自然！自然！我们互相帮助嘛！"
            "格雷伯爵满面笑容地离开了。你不确定他的承诺值多少钱，但在王都多一个朋友总比多一个敌人好。"

        "婉拒，保持中立":
            $ change_stat("intrigue", 3)
            hide count_grey_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "伯爵的好意我领了。但在听到具体提案之前，我不便表态。"
            hide player_char_img
            $ hide_all_chars("count_grey_img")
            show count_grey_img at left with dissolve
            count_grey "哈哈……年轻人就是谨慎。好，好。那我们改日再谈。"
            "格雷伯爵笑着离开了，但你注意到他眼中的笑意并没有到达眼底。"

        "直接问他觐见时需要注意什么" if intrigue >= 45:
            $ change_stat("intrigue", 8)
            hide count_grey_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "伯爵是王都的常客。不知觐见王后时，有什么需要注意的？"
            hide player_char_img
            $ hide_all_chars("count_grey_img")
            show count_grey_img at left with dissolve
            count_grey "哦？年轻人虚心请教，好事！好事！"
            count_grey "记住一件事——王后问你什么，你都要回答。但不要回答她没有问的事。"
            count_grey "还有，千万不要直视她的眼睛超过三秒。她不喜欢被人盯着看。"
            count_grey "最后——如果她请你喝茶，不要喝。那不是款待，是她让人放松警惕的老办法。见过有人喝完之后，在朝堂上把心里话说了个底朝天。"
            hide count_grey_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "多谢伯爵指点。"
            hide player_char_img
            $ hide_all_chars("count_grey_img")
            show count_grey_img at left with dissolve
            count_grey "不客气，不客气。年轻人前途无量啊！"

    $ hide_all_chars()
    "送走几位访客后，你在房间里静坐了一会儿，理清思绪。"

    "然后，你起身，走出了贵宾馆。"

    "王宫就在眼前。"

    "比你想象的更加宏伟。"

    "三重城墙，每一重都比城市的外墙更高更厚。"

    "城门上方雕刻着王室的徽章——一只戴着王冠的狮子，脚下踩着蔓延的荆棘。"

    "穿过第一道城门，是一片宽阔的庭院。两排银杏树整齐地排列在道路两侧，金色的叶子在微风中簌簌作响。"

    "第二道城门内是近卫军的营房和兵器库。你看到成排的铠甲在阳光下闪着寒光。"

    "第三道城门——通往王宫本身。"

    "大理石台阶有四十八级，每一级都宽得可以并排走十个人。"

    "台阶两侧站着身穿金甲的近卫，手持长戟，纹丝不动，像是雕像。"

    "你拾级而上，每一步都能感受到这座建筑的重量——它不仅仅是石头的重量，更是权力的重量。"

    show elena_img at right with dissolve

    elena "领主大人，在王宫里，隔墙有耳。请谨言慎行。"

    if dark_lily_joined:
        elena "暗百合在宫中也有眼线。如果需要帮助，去花园的第三棵玫瑰花丛后面找。"

    hide elena_img with dissolve

    $ hide_all_chars()
    "一位侍从引你穿过长长的走廊。"

    "走廊的天花板是拱形的，上面绑着精美的壁画——描绘着王国建立以来的重大事件。"

    "开国之战、加冕典礼、条约签订、教堂落成……每一幅画都在诉说着这个王国的荣耀。"

    "你的靴跟敲在大理石地板上，发出清脆的回响。"

    "走廊两侧挂满了历代国王的画像。你在最后一幅前停下脚步——"

    "那是先王的画像。一个面容刚毅的中年人。他的眼睛是深褐色的，嘴角带着一丝不易察觉的忧郁。"

    "在他的画像下方，刻着一行字：「格里菲斯七世，圣裁者，正义之盾。」"

    "画像旁边就是伊莎贝拉王后的画像。她的目光冰冷而锐利，仿佛能穿透画框。"

    "她的画像下面没有刻字——只有一个王冠的浮雕。"

    "你注意到先王的画像和王后的画像之间，有一块明显的空白。"

    "那里本应挂着什么？被摘下了？还是从未被挂上？"

    if intrigue >= 50:
        "你的直觉告诉你——那块空白处，也许曾经挂着一幅被故意移除的画像。也许是某个不该被记住的人。"

    "侍从催促你继续前行。"

    if knows_eagle_network:
        ## 七近卫·盾卫遗制回响 (《六卫终录》: 盾卫守备之法为王后所取, 并入王室禁军)
        "路过廊柱时，你注意到宫墙上禁军换岗的走法——三步一顿，交盾不交枪，两人的视线永远错开着盯住两个方向。"

        "《六卫终录》里写过：盾卫守城，其法为王后所取。开国年间七近卫的规矩，如今还活在这些宫墙上。"

    "你收回目光，跟着侍从走向大厅的尽头——王座大厅的大门。"

    "两扇三丈高的橡木大门上镶嵌着黄铜的狮子头。"

    "侍从叩了三下。门缓缓打开。"

    $ play_sound("audio/sfx/crowd_murmur.ogg")

    "一阵低沉的嗡嗡声从门内传来——那是数十名朝臣的窃窃私语。"

    ## ============================================================
    ## 场景2：觐见王后
    ## ============================================================

label ch4_throne:

    $ play_music("audio/music/tension.ogg", fadein=2.0)
    scene bg throne_room with dissolve
    $ unlock_gallery("bg_throne_room")
    $ set_mood("tense")

    "王座大厅。"

    "这是你见过的最大的室内空间。穹顶高达十丈，由十二根巨大的石柱支撑。"

    "每根石柱上都缠绕着镀金的浮雕——蛇、鹰、狮子和荆棘交织在一起，象征着王权的力量。"

    "阳光从彩色玻璃窗洒入，在地面上投下五彩斑斓的光斑。"

    "大厅两侧站满了朝臣和贵族——男人们穿着绸缎和天鹅绒，女人们戴着珠宝和羽毛。"

    "所有人的目光都在你进入的那一刻聚焦过来。"

    "有好奇的、有审视的、有蔑视的、也有不动声色的。"

    "你感觉这大厅里每一步都不能走错。"

    "侍从高声通报——"

    $ hide_all_chars("court_herald_img")
    show court_herald_img at left with dissolve
    court_herald "艾登堡领主，{b}[player_name]{/b}觐见！"

    $ hide_all_chars()
    "你沿着长长的红色地毯走向王座。"

    "每走一步，你都能感受到两侧目光的重量。"

    "地毯的尽头，是七级台阶。台阶之上——"

    hide court_herald_img
    $ hide_all_chars("queen_img")
    show queen_img at left with dissolve
    $ unlock_gallery("queen")

    $ hide_all_chars()
    "伊莎贝拉王后端坐在王座上。"

    "她穿着深紫色的长裙，肩上披着白色的貂皮披风。王冠上的红宝石在阳光下闪烁，像凝固的血滴。"

    "她的脸苍白、精致，像是一件瓷器。五十岁左右的年纪，但保养得极好，看起来不过四十。"

    "唯有那双眼睛——深灰色的，冰冷的，带着一种看透一切的锐利——暴露了她的年龄和她的心机。"

    "你在台阶下站定，单膝跪地。"

    hide queen_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "臣，艾登堡领主[player_name]，参见王后陛下。"

    hide player_char_img
    $ hide_all_chars("queen_img")
    show queen_img at left with dissolve
    queen "起来。"

    $ hide_all_chars()
    "她的声音不大，但在空旷的大厅中回荡，带着不容置疑的威严。"

    "你站起身，抬头与她对视。"

    $ hide_all_chars("queen_img")
    show queen_img at left with dissolve
    queen "艾登堡的新领主。你比我想象的年轻。"

    "她的目光在你身上停留了几秒，像一把无形的刀，在丈量你的份量。"

    queen "你父亲是个聪明人。可惜，聪明人往往活不长。"

    ## 选择深度样板: ch3"主动出击"秘密联络异见领主的延迟代价 —— 王后早已知情
    if courted_rival_lords:
        queen "对了——听说你回北方之后，和格雷、施泰因那几位领主走得近了。"
        $ hide_all_chars()
        "她说得很随意，像在问今年的收成。你后背沁出一层薄汗。"
        $ hide_all_chars("queen_img")
        show queen_img at left with dissolve
        queen "新领主多交朋友是好事。不过——挑朋友之前，先看清楚谁手里攥着你的把柄。"
        $ hide_all_chars()
        "她知道。你以为瞒得严严实实的事，到底还是传进了王座大厅。"
        $ change_rel("rel_queen", -10)

    $ hide_all_chars()
    "你不确定这是感叹还是威胁。大厅中响起一阵低低的窃笑。"

    "你保持着平静的表情。"

    $ hide_all_chars("queen_img")
    show queen_img at left with dissolve
    queen "我召你来，是有两件事要谈。"

    queen "第一，北方边境的局势。冯·哈根男爵近来动作频频，我需要你替我盯着他。"

    queen "艾登堡地处要冲，是北方通往王都的门户。你明白这意味着什么。"

    if eagle_intel:
        $ hide_all_chars()
        "（信息网没说错。她要借你的刀除掉男爵。她以为这是试探——可你昨夜就拿到了答案。）"

    hide queen_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "臣明白。艾登堡是王室的屏障。"

    hide player_char_img
    $ hide_all_chars("queen_img")
    show queen_img at left with dissolve
    queen "很好。不过光明白还不够，我需要你做到。"

    queen "我会给你一千枚金币和三百套军械，用于加强艾登堡的防务。"

    queen "作为交换——每月一份详细的北方动态报告，直接送到我手中。"

    menu:
        "以领地民望做担保——你已名声在外" if reputation >= 60:
            $ log_decision("第四章", "以民望做担保, 王后给了额外奖励")
            $ change_stat("reputation", 5)
            $ change_stat("wealth", 30)
            $ change_stat("power", 5)
            hide queen_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "臣愿领旨。陛下可问王都的人——艾登堡这一年的民望，不输王室任何一个直辖郡。这便是臣给陛下的担保。"
            hide player_char_img
            $ hide_all_chars("queen_img")
            show queen_img at left with dissolve
            queen "……你倒是真敢说。"
            "王后看了你许久，然后抬手招来侍从。"
            queen "再加五百金币，五十套军械。看你能不能把这份「民望」兑现成边境的安宁。"
            "你领旨退下。这是你第一次拿外人的评价当作筹码——而王后给了。"

        "接受条件":
            $ log_decision("第四章", "接受王后的条件")
            $ change_stat("wealth", 25)
            $ change_stat("power", 5)
            $ change_stat("reputation", -3)
            $ change_rel("rel_queen", 5)
            hide queen_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "臣领命。"
            hide player_char_img
            $ hide_all_chars("queen_img")
            show queen_img at left with dissolve
            queen "很好。我喜欢爽快的人。"

        "提出附加条件——请求减免税赋":
            $ change_stat("intrigue", 5)
            $ change_stat("wealth", 18)
            hide queen_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            if prologue_study_focus == "commerce":
                player "臣愿效力。但容臣算一笔账——艾登堡年贡六百金币，北防开支至少八百。若陛下减免一年税赋，臣可将差额全部投入边防。对王室而言，这笔买卖比直接拨款更划算。"
                hide player_char_img
                $ hide_all_chars("queen_img")
                show queen_img at left with dissolve
                queen "（微微一笑）你倒是把账算到我头上来了。"
                "她沉吟片刻，手指轻叩扶手。"
                queen "一年。减免一年。但我要看到成效。"
                $ change_stat("wealth", 18)
            else:
                player "臣愿效力。但艾登堡初经易主，百废待兴，若能减免一年税赋，臣必能更好地守卫北方。"
                hide player_char_img
                $ hide_all_chars("queen_img")
                show queen_img at left with dissolve
                queen "（挑眉）你倒是不客气。"
                "她沉吟片刻。"
                queen "半年。减免半年。别让我失望。"
                $ change_stat("wealth", 12)

        "委婉表示需要更多支持":
            $ change_stat("reputation", 5)
            hide queen_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "臣感激陛下的支持。但男爵势力庞大，仅凭艾登堡一地之力……"
            hide player_char_img
            $ hide_all_chars("queen_img")
            show queen_img at left with dissolve
            queen "你是在讨价还价？"
            hide queen_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "臣是在如实禀报边境的形势。"
            hide player_char_img
            $ hide_all_chars("queen_img")
            show queen_img at left with dissolve
            queen "……哼。我会让蒙塔古伯爵另拨五百人驻扎在艾登堡以南。这样你放心了？"
            $ change_stat("power", 8)

    if council_outcome == "反对":
        queen "第二……你在领主会议上反对我的新税法。"

        "她的声音冷了几度。大厅中的窃窃私语瞬间安静。"

        queen "我想听听你的理由。当着我的面。"

        "所有人都在看着你。你感觉到身后无数双眼睛灼烧着你的后背。"

        menu:
            "坚持立场——税法确实不合理" if power >= 55:
                $ change_stat("power", 10)
                $ change_rel("rel_queen", -15)
                hide queen_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "陛下，新税法加重了百姓负担。领地如果被压垮，王室的根基也会动摇。"
                hide player_char_img
                $ hide_all_chars("queen_img")
                show queen_img at left with dissolve
                queen "你是在教我治国？"
                hide queen_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "臣只是在陈述事实。"
                "大厅中鸦雀无声。你能感觉到空气中的紧张几乎凝成了实质。"
                $ hide_all_chars("queen_img")
                show queen_img angry at left with dissolve
                queen "（冷笑）倒是有几分胆量。"
                queen "你父亲当年也是这样跟先王说话的。看来倔强是你们家族的通病。"
                $ hide_all_chars("queen_img")
                show queen_img at left with dissolve

            "解释并示好——为了百姓，非为不敬":
                $ change_stat("reputation", 10)
                $ change_rel("rel_queen", 5)
                $ change_stat("power", -8)
                hide queen_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "陛下，臣反对的不是税法本身，而是时机。艾登堡刚经历易主，百姓需要喘息。"
                player "待局势稳定，臣定当足额缴纳。"
                hide player_char_img
                $ hide_all_chars("queen_img")
                show queen_img at left with dissolve
                queen "嗯……这番话还算中听。"
                queen "但我要你记住——下次在公开场合反对我之前，先来和我私下谈。"
                queen "我不喜欢在人前被打脸。"
                $ hide_all_chars()
                "你看见席间几位领主交换了眼神。当着满朝的面，你退了这一步，他们都记下了。"

            "动用情报网——不解释，反将一军" if eagle_intel and intrigue >= 50:
                ## 消耗机制大轮 Phase 2: 花 intrigue 换决定性社交优势(把棋子翻成对手)
                $ change_stat("intrigue", -30)  ## 当庭显露你早知她底牌=暴露王都有你的眼线, 那条暗线当场报废
                $ change_stat("power", 8)
                $ change_rel("rel_queen", 5)  ## 她重新评估你: 不是棋子, 是值得敬畏的对手
                hide queen_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "时机。臣反对的是时机。"
                player "不过——陛下真正想听的，恐怕不是这个。"
                hide player_char_img
                $ hide_all_chars("queen_img")
                show queen_img at left with dissolve
                queen "哦？"
                hide queen_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "陛下要的不是臣的税，是臣的刀。北境的男爵陛下容不下，想借臣的手除掉。"
                player "臣说得对吗？"
                $ hide_all_chars()
                "大厅死一般安静。没有人敢这样跟王后说话。"
                "王后盯着你看了很久。脸上的怒意慢慢退去，换成一种重新打量的神色。"
                $ hide_all_chars("queen_img")
                show queen_img at left with dissolve
                queen "（轻声）你在王都有眼睛。"
                queen "有意思。我以为艾登堡送来的是一条听话的狗。"
                queen "看来是匹狼。"
                $ hide_all_chars()
                "这一回合你赢了——王后不再拿你当棋子，开始拿你当对手。"
                "代价是那条把消息递进王宫的暗线。她今夜就会去揪它，你再也用不上了。"
    else:
        queen "第二，我有一个任务交给你。"

    queen "我听说你遭到了暗杀未遂。"

    "她说这话时语气平淡，仿佛在谈论天气。"

    queen "你知道是谁干的吗？"

    menu:
        "如实相告——提到暗百合" if father_death_known:
            $ change_rel("rel_queen", 10)
            $ change_stat("intrigue", -5)
            hide queen_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "一个叫暗百合的组织。他们似乎与先王有关。"
            "王后的眼神闪过一丝……是惊讶？还是恐惧？你看得不太真切。"
            hide player_char_img
            $ hide_all_chars("queen_img")
            show queen_img at left with dissolve
            if dark_lily_destroyed:
                queen "暗百合……你说的是那群被你铲除的叛逆分子？"
                queen "干得好。那些人是这个王国的毒瘤。"
            else:
                queen "暗百合……那群疯子还没消停。"
                queen "他们是一群危险的叛逆分子。你最好远离他们。"
            "你注意到她在说「叛逆分子」这四个字时，语气格外用力。仿佛这个词承载着比字面更重的分量。"
            "你把暗百合递了出去。从这一刻起，她知道你愿意对她交底——这是你能给的诚意，也是递出去就收不回的一张牌。"
            $ queen_trust = True

        "只说不知——隐瞒暗百合":
            $ change_stat("intrigue", 5)
            $ change_rel("rel_queen", -5)
            hide queen_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "臣还在调查。目前没有线索。"
            hide player_char_img
            $ hide_all_chars("queen_img")
            show queen_img at left with dissolve
            queen "是吗。"
            $ hide_all_chars()
            "王后的目光停留在你脸上多了一秒。你不确定她是否相信了。"
            "但你的表情没有任何破绽。在艾琳娜的训练下，你已经学会了如何在权力者面前戴上面具。"
            "王后没再追问，只是把目光从你身上移开，不再多看一眼。"
            "你守住了暗百合这张牌。但在她眼里，你刚刚从一个或许能交心的人，变回了一个普通的边境领主。"

        "反问——『也许陛下比我更清楚？』" if intrigue >= 50:
            $ change_stat("intrigue", 8)
            $ change_rel("rel_queen", -10)
            hide queen_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "也许陛下比臣更清楚是谁干的。"
            $ hide_all_chars()
            "大厅的空气瞬间凝固。"
            "你听到身后有人倒吸了一口凉气。"
            $ hide_all_chars("queen_img")
            show queen_img angry at left with dissolve
            queen "你在暗示什么？"
            hide queen_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "臣只是在想，谁会希望一个边境小领主死呢？"
            hide player_char_img
            $ hide_all_chars("queen_img")
            show queen_img at left with dissolve
            queen "……你很大胆。大胆的人要么成为英雄，要么变成尸体。"
            $ hide_all_chars("queen_img")
            show queen_img at left with dissolve
            queen "希望你是前者。"
            $ hide_all_chars()
            "她的嘴角浮现出一个意味深长的微笑。那个笑容让你的脊背一阵发凉。"
            "你赢了这一个回合，赢来的是她的注意。但从今往后她看你，会先掂量你藏着什么，再听你说了什么。"

    "觐见结束。你退出王座大厅时，腿有些发软。"

    "倒不是怕。是维持那张面具，耗尽了你全部的力气。"

    hide queen_img with dissolve

    ## ============================================================
    ## 新增场景：宫廷宴会
    ## ============================================================

    $ play_music("audio/music/great_hall.ogg", fadein=2.0)
    scene bg great_hall with dissolve
    $ unlock_gallery("bg_great_hall")

    "当晚，王后在大厅举办宴会，款待各地前来觐见的领主。"

    $ play_sound("audio/sfx/crowd_murmur.ogg")

    "大厅被装扮得金碧辉煌。数十盏水晶吊灯将整个空间照得如同白昼。"

    "长桌上铺着白色的亚麻布，摆满了银盘和水晶杯。烤全鹿、焗蘑菇、蜂蜜酒、南方的水果——你从未见过这么丰盛的宴席。"

    "乐师们在角落里演奏着柔和的曲子。侍女们穿梭在宾客之间，端着托盘送酒。"

    "你被安排在长桌的中段——不太近也不太远的位置。这本身就是一种暗示：王后还没有决定如何对待你。"

    show elena_img at right with dissolve

    if wells_met:
        elena "（低声）对面是威尔斯子爵——领主会议上见过的。别忘了，他和男爵是姻亲。"
    else:
        elena "（低声）领主大人，坐在您对面的是南方的威尔斯子爵——他和男爵是姻亲。"

    elena "您左边的是教廷特使安德烈亚斯——教会在王都的代言人。"

    elena "右边那个空位……是给王子留的。"

    hide elena_img with dissolve

    $ hide_all_chars()
    "你环顾四周，观察着每一个人。"

    "贵族们三三两两地聚在一起，低声交谈。他们的笑容像戴着面具——精致、得体，却看不到任何真实的情感。"

    "你注意到几个有趣的细节——"

    "威尔斯子爵频频向王后的方向张望，眼神中带着焦虑。"

    "教廷特使安德烈亚斯一直在和旁边的人耳语，偶尔朝你的方向看一眼。"

    "还有一些你不认识的贵族在悄悄议论着什么，目光闪烁不定。"

    "宴会进行了大约半个时辰，一个年轻人姗姗来迟。"

    $ hide_all_chars("prince_img")
    show prince_img at left with dissolve
    $ unlock_gallery("prince")

    $ hide_all_chars()
    "他穿着一件天蓝色的丝绒外套，金色的卷发松松地垂在肩上，面容俊朗，嘴角挂着一丝慵懒的微笑。"

    "——这就是弗雷德里克王子。"

    "他走进大厅时，所有人的目光都转向了他。有人恭敬地点头，有人刻意回避。"

    "王子仿佛对这一切浑然不觉。他大步走到你旁边的空位坐下。"

    $ hide_all_chars("prince_img")
    show prince_img at left with dissolve
    prince "你就是艾登堡的新领主？听说你今天在母后面前表现得不错。"

    $ prince_met = True

    hide prince_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "殿下过奖。"

    hide player_char_img
    $ hide_all_chars("prince_img")
    show prince_img at left with dissolve
    prince "别紧张。在宴会上，你可以放松一点。"

    "他端起酒杯，漫不经心地抿了一口。"

    prince "你知道吗，这个大厅里至少有三组人在密谋。四组人在互相监视。还有两组人假装不认识对方。"

    prince "而我母后——她坐在主位上，把这一切看在眼里，乐在其中。"

    "你下意识地看了一眼主位。王后确实在微笑，但那种笑容让你不寒而栗——像一个棋手看着棋盘上的棋子在自相残杀。"

    menu:
        "试探王子的态度":
            $ change_stat("intrigue", 5)
            hide prince_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "殿下对这些密谋……怎么看？"
            hide player_char_img
            $ hide_all_chars("prince_img")
            show prince_img at left with dissolve
            prince "怎么看？"
            "他笑了，笑容中有一种与年龄不符的苍凉。"
            prince "我觉得它们很无聊。但也很危险。"
            prince "就像这杯酒——好喝，但喝多了会死人。"
            $ change_rel("rel_prince", 3)  ## batch 14 #7 王子好感: 5→3 减弱小加成累加

        "保持礼貌的距离":
            hide prince_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "殿下风趣。臣对王都的规矩还不太熟悉。"
            hide player_char_img
            $ hide_all_chars("prince_img")
            show prince_img at left with dissolve
            prince "规矩？王都最大的规矩就是——没有规矩。只有利益。"

        "直接问他关于父亲的事" if intrigue >= 45:
            $ change_stat("intrigue", 8)
            $ change_stat("loyalty", -2)  ## balance pass 修法 1: 把父辈情谊工具化套王子情报
            $ change_rel("rel_prince", 1)  ## batch 14 #7 王子好感: 3→1 减弱小加成累加
            hide prince_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "殿下……臣斗胆。您认识先父吗？"
            hide player_char_img
            $ hide_all_chars("prince_img")
            show prince_img at left with dissolve
            prince "你父亲？当然认识。他每年来王都觐见时，都会给我带一把小木剑。"
            prince "那时候我还是个孩子。你父亲是少数几个把我当孩子对待的大人。"
            prince "大多数人……只把我当一枚棋子。"
            "他的声音放轻了，手指无意识地摩挲着酒杯的杯沿。"

    hide prince_img with dissolve

    $ hide_all_chars()
    "宴会继续进行。酒过三巡，气氛渐渐热络起来。"

    "有人开始跳舞。悠扬的音乐在大厅中回荡。"

    "一位穿着鹅黄色裙子的年轻贵族女子走到你面前，微微行了一个屈膝礼。"

    $ hide_all_chars("noble_lady_img")
    show noble_lady_img at left with dissolve
    noble_lady "领主大人，赏脸跳一支舞吗？"

    menu:
        "以名声做姿态——主动向众人致意" if reputation >= 50:
            $ change_stat("reputation", 5)
            $ change_stat("intrigue", 3)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            "你站起身，但没有走向那位女子。你环视四周，微微抱拳——"
            player "诸位，在下边境出身，不擅这等贵人之舞。但若有人愿听『艾登堡』这一年的故事——欢迎过来一谈。"
            $ hide_all_chars()
            "片刻安静。然后角落里传来一声轻笑——是格雷伯爵。"
            "陆续有人走过来。穿鹅黄裙的女子微微一怔，但很快也跟着围了过来。"
            "你没跳一支舞，却让半个大厅的人都坐在了你身边。"

        "接受邀请":
            $ change_stat("reputation", 5)
            $ hide_all_chars()
            "你站起身，伸出手。她笑了，把手放在你的掌心中。"
            "你并不擅长跳舞——在艾登堡的边境，没有人教过你这种贵族的礼仪。"
            "但你凭着直觉和一些生硬的步伐，勉强没有踩到她的脚。"
            $ hide_all_chars("noble_lady_img")
            show noble_lady_img at left with dissolve
            noble_lady "领主大人跳得不错。"
            hide noble_lady_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你不必客气。我知道自己像一只穿了靴子的熊。"
            $ hide_all_chars()
            "她笑了。周围几位贵族也投来了友善的目光。"
            "也许在王都，一支笨拙的舞蹈比一场精彩的演说更能赢得好感。"

        "婉拒——今晚不是跳舞的时候":
            $ change_stat("intrigue", 3)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "小姐的好意我心领了。但我不善舞蹈，怕失了礼数。"
            hide player_char_img
            $ hide_all_chars("noble_lady_img")
            show noble_lady_img at left with dissolve
            noble_lady "可惜。也许下次吧。"
            $ hide_all_chars()
            "她转身离去。你注意到她走向了教廷特使的身边——也许这次邀请并非出自好意。"

    "夜渐深。宴会上的人开始陆续离去。"

    "你也准备告辞时，一个侍从悄悄塞给你一张纸条。"

    "你在灯光下展开——纸条上只有简短的一行字：「花园。子时。——F。」"

    "F……弗雷德里克？"

    "你把纸条揉成一团，扔进了壁炉。"

    ## ============================================================
    ## 场景3：花园密会
    ## ============================================================

label ch4_garden:

    $ play_music("audio/music/night_mystery.ogg", fadein=2.0)
    scene bg palace_garden with dissolve
    $ unlock_gallery("bg_palace_garden")
    $ set_mood("calm")
    $ set_weather("fireflies")

    ## Zane 反馈(2026-06-07): 删掉此处随机事件 — 花园是脚本化的子时密会, 随机商人/遭遇会插在潜入之前"冒出来又没了"
    ## (正对玩家"突然冒出跟剧情不搭的内容"那条; 只删这一处脚本化紧张段, 不全局降频——batch14 刻意调高过随机事件)

    "子时。"

    "你独自走进了宫廷花园。"

    "夜风送来花香，混合着泥土的清冷气息。修剪整齐的灌木和盛开的玫瑰在暗中只剩下轮廓和气味。"

    "花园比你想象的大得多。蜿蜒的石径在花丛中穿行，两侧是大理石雕像——天使、骑士、神话中的英雄。"

    "黑得只能看见轮廓，那些雕像的影子像是在窃窃私语。"

    "喷泉在花园中央静静地流淌，水声在寂静的夜里格外清晰。"

    "你沿着石径走了一圈，没有看到任何人。"

    "也许是一个陷阱？你的手不由自主地摸向腰间的匕首。"

    "就在这时——"

    "一个年轻人从花丛后走出来。他披着一件不起眼的灰斗篷，把华服遮在下面，走两步就回头看一眼来路。"

    $ hide_all_chars("prince_img")
    show prince_img at left with dissolve

    if prince_letter_response == "heed":
        prince "你收到我的信了。我就知道你会来。"
    elif prince_letter_response == "decline":
        prince "你来了。我还以为，那封信你看过就当没看过。"
    else:
        prince "你来了。信还没核实清楚就敢来——比我想的有胆色。"

    hide prince_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "殿下在信里说，宫里上下都是王后的耳目。可你这会儿怎么出得来？"

    hide player_char_img
    $ hide_all_chars("prince_img")
    show prince_img at left with dissolve
    prince "秋水宫的后墙有一道花匠走的小门。守卫以为我歇下了。"

    prince "我顶多有半个时辰。听见脚步声，咱们就各走各的，别回头。"

    $ hide_all_chars()
    "他在一张石凳上坐下，拍了拍旁边的位置。"

    "你犹豫了一下，在他旁边坐了下来。"

    "远处喷泉的水光映在他脸上，你第一次近距离看清了这个年轻的王子——"

    "他的眼睛是浅蓝色的，像冬天的天空。眼底有一种与他的年龄不相称的疲惫。"

    $ hide_all_chars("prince_img")
    show prince_img at left with dissolve
    prince "你觉得今晚的宴会怎么样？"

    hide prince_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "……很热闹。"

    hide player_char_img
    $ hide_all_chars("prince_img")
    show prince_img at left with dissolve
    prince "热闹？"

    "他笑了，但那笑容里没有一丝快乐。"

    $ hide_all_chars("prince_img")
    show prince_img sad at left with dissolve

    prince "那是一群披着人皮的狼在互相嗅闻。他们在判断谁是猎物，谁是同伴。"

    prince "我在这种宴会上长大。从七岁开始，每一顿饭都是一场战争。"

    prince "你不知道哪一杯酒里有毒，哪一句话会被断章取义，哪一个微笑背后藏着匕首。"

    hide prince_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "听起来……不像一个王子该过的生活。"

    hide player_char_img
    $ hide_all_chars("prince_img")
    show prince_img at left with dissolve
    prince "王子？王子不过是一个住在笼子里的囚犯，笼子是金做的罢了。"

    "他转头看着你。"

    prince "我母后……伊莎贝拉，她不是一个好的统治者。"

    prince "税越来越重，领主们人心惶惶，边境不稳——这个国家正在走向深渊。"

    prince "你在领地里，也感受到了吧？"

    hide prince_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "百姓确实过得很辛苦。"

    hide player_char_img
    $ hide_all_chars("prince_img")
    show prince_img at left with dissolve
    prince "不只是百姓。连贵族们都开始动摇了。男爵的反叛只是开始。"

    prince "如果母后继续这样下去，用不了三年，这个国家就会陷入内战。"

    "他的声音很平静，但你能听出其中的焦虑。"

    prince "我需要盟友。"

    "你警觉地打量着这个年轻的王子。他看起来真诚，但在王宫里，真诚可能是最精巧的伪装。"

    menu:
        "问他理想中的王国是什么样子":
            $ change_stat("intrigue", 5)
            $ change_rel("rel_prince", 5)
            hide prince_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "殿下，如果有一天你坐上那个位置——你想建立一个什么样的王国？"
            hide player_char_img
            $ hide_all_chars("prince_img")
            show prince_img at left with dissolve
            prince "你是第一个问我这个问题的人。"
            "他抬头望着月亮，思索了一会儿。"
            prince "一个公平的王国。贵族和百姓不应该是狼和羊的关系。"
            prince "税收应该用在修路、建学堂、办济贫院上，而不是用来修建王后的城墙和宴会厅。"
            prince "我想让每一个孩子都有书读。让每一个农民都能吃饱饭。让正义不再只是有钱人的专利。"
            if built_school:
                hide prince_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "学堂我在艾登堡已经建了一座。农家的孩子上午下地，下午认字。"
                hide player_char_img
                $ hide_all_chars("prince_img")
                show prince_img at left with dissolve
                $ change_rel("rel_prince", 3)
                prince "……真的？"
                "他看你的眼神变了。不再是看一个可以争取的盟友，而是看一个已经在做他想做的事的人。"
                prince "那你比我快了一步。"
            hide prince_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "这是很好的愿景。但实现它需要付出巨大的代价。"
            hide player_char_img
            $ hide_all_chars("prince_img")
            show prince_img at left with dissolve
            prince "我知道。所以我需要愿意付出这个代价的人站在我身边。"

        "直接问他打算怎么做":
            $ change_stat("intrigue", 3)
            hide prince_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "盟友……你打算怎么做？"
            hide player_char_img
            $ hide_all_chars("prince_img")
            show prince_img at left with dissolve
            prince "我不会弑母。这一点你放心。"
            prince "但我打算在合适的时机，联合足够多的领主，以和平的方式迫使她退位。"
            prince "先王的遗诏中本就规定了王子成年后应继承王位。母后一直压着不执行。"
            prince "我需要的是——证据和支持者。"

    prince "作为交换，我可以给你想要的东西。"

    prince "比如……你父亲的案子。"

    "你的心跳漏了一拍。"

    prince "我知道他是怎么死的。"

    "花园中只剩下喷泉的水声和你加速的心跳。"

    menu:
        "与王子结盟":
            $ log_decision("第四章", "与弗雷德里克王子结盟")
            $ prince_ally = True
            $ change_rel("rel_prince", 25)
            $ change_rel("rel_queen", -10)
            hide prince_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "殿下想要什么？"
            hide player_char_img
            $ hide_all_chars("prince_img")
            show prince_img at left with dissolve
            prince "很简单。当我登基的那天，我需要你的支持和你的兵。"
            prince "作为回报，你的领地将获得特许贸易权，税收减半。"
            prince "还有——你父亲的真正死因，以及凶手的名字。"
            hide prince_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "成交。但我需要先看到诚意。"
            hide player_char_img
            $ hide_all_chars("prince_img")
            show prince_img at left with dissolve
            prince "公平。明天，我会派人送一封信到你的住处。那里面有你想要的答案。"
            $ hide_all_chars()
            "你们握了手。喷泉的水声盖过了一切，王子的手掌温暖而有力。"
            "他给你想要的一切——凶手的名字、减税、特许贸易权。可天底下没有白给的东西。从今夜起，他登基那天你得拿出兵来，这笔账记下了。"
            "他笑了一下，转身走开。你看着他的背影消失在喷泉那一侧的回廊。"

        "拒绝——你不想卷入王位之争":
            $ log_decision("第四章", "拒绝与王子结盟")
            $ change_rel("rel_prince", -10)
            hide prince_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "殿下的好意我心领了。但我只是一个边境领主，王都的事情太大了。"
            hide player_char_img
            $ hide_all_chars("prince_img")
            show prince_img at left with dissolve
            prince "可惜。回头有事派人来找我。"
            prince "不过，你迟早会发现——在这个国家，没有人能置身事外。"
            prince "你父亲试过。他的下场你也看到了。"
            prince "还有——你父亲想知道的答案，就在我手里。你今晚要是走了，它就跟着我一起留在这座宫里。"
            $ hide_all_chars()
            "那句话像一根刺。但真正让你后半夜睡不着的，是你刚刚亲手推开了父亲案子唯一的线索。"

        "假意答应，实则向王后告密" if queen_trust:
            $ change_rel("rel_queen", 25)
            $ change_rel("rel_prince", -30)
            $ prince_betrayed = True
            hide prince_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "殿下说得有理。我愿意效力。"
            hide player_char_img
            $ hide_all_chars("prince_img")
            show prince_img at left with dissolve
            prince "太好了！我就知道你是可以信任的人。"
            $ hide_all_chars()
            "你微笑着，心里已经在盘算如何将这件事报告给王后。"
            "在这个游戏里，每一步都必须精确。"
            "你和他握手时，手心是冷的。"

        "试探——问更多关于父亲的事":
            $ change_stat("intrigue", 5)
            hide prince_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "在我做任何决定之前……先告诉我关于我父亲的事。"
            hide player_char_img
            $ hide_all_chars("prince_img")
            show prince_img at left with dissolve
            if not testament_forged_known:
                prince "你父亲发现了母后篡改先王遗诏的证据。母后命教会的人除掉了他。"
                prince "具体是谁动的手，我不知道。但下令的人是我的母亲。"
                $ testament_forged_known = True
                $ true_killer_known = True
                $ hide_all_chars()
                "你闭上眼睛。尽管你已经有了心理准备，但亲耳听到这个真相，依然像一把刀。"
                "月光依旧温柔，但你的世界已经不一样了。"
            else:
                prince "你应该已经知道了——遗诏的事，还有你父亲的死因。"
                prince "下令的人，是我的母亲。这一点我可以亲口证实。"
                $ true_killer_known = True
                "从王子口中听到这句话，你心中的最后一丝疑虑也消散了。"
            hide prince_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "……我需要考虑。"
            hide player_char_img
            $ hide_all_chars("prince_img")
            show prince_img at left with dissolve
            prince "我会等你的答复。"
            prince "但别考虑太久。时间不站在我们这边。"

    ## ── 王子的过去：导师之死（加深动机） ──

    "夜风吹过花园，将一片花瓣卷到了王子的膝上。他低头看了看，苦笑了一声。"

    prince "你知道我为什么要反对自己的母亲吗？"

    prince "不只是因为她是一个糟糕的统治者。"

    $ hide_all_chars("prince_img")
    show prince_img sad at left

    prince "我七岁的时候，有一个老骑士——他叫西里尔。是父王派来教我剑术和骑马的。"

    prince "西里尔不是一个好老师。他喝酒，脾气暴躁，教我骑马的时候摔了我十七次。"

    prince "但他是唯一一个从不把我当王子的人。"

    prince "他叫我「小子」。揍我的时候跟揍自己孙子一样。"

    "王子的声音变得很轻，像是怕惊醒什么人。"

    prince "十岁那年的冬天，西里尔突然消失了。母后说他告老还乡了。"

    prince "我信了。"

    prince "直到三年后，一个醉酒的侍卫在我面前说漏了嘴——"

    prince "西里尔死了。死在地牢里。因为他在教我读书时，给了我一本关于先王时期法律的旧书。"

    prince "那本书里记载了王位继承的正统程序。"

    prince "母后觉得他在蛊惑我。"

    "王子抬起头，望着夜空。你看到他用力眨了几下眼睛，喉结滚动了一下。"

    prince "一个老人，一辈子效忠王室，最后死在自己守护的城堡的地牢里。因为他给一个孩子看了一本书。"

    menu:
        "你在那之后就开始计划了？":
            $ change_rel("rel_prince", 3)  ## batch 14 #7 王子好感: 5→3 减弱小加成累加
            $ prince_mentor_known = True
            hide prince_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "所以……从那时起，你就开始了？"
            hide player_char_img
            $ hide_all_chars("prince_img")
            show prince_img at left with dissolve
            prince "不。从那时起，我开始假装。"
            prince "假装不在乎。假装是一个只知道喝酒跳舞的纨绔王子。"
            prince "十二年了。十二年的假装，只为了等一个机会。"
            prince "而你——也许就是那个机会。"

        "那你为什么不恨她？":
            $ change_rel("rel_prince", 1)  ## batch 14 #7 王子好感: 3→1 减弱小加成累加
            $ prince_mentor_known = True
            hide prince_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "她杀了你的导师……你不恨她吗？"
            hide player_char_img
            $ hide_all_chars("prince_img")
            show prince_img at left with dissolve
            prince "恨？"
            prince "她是我的母亲。我恨她做的事，但我没办法恨她这个人。"
            prince "也许这就是为什么我想用和平的方式解决——"
            prince "我不想看到更多的血。西里尔的血已经够了。"

        "保持沉默，不作评价":
            $ prince_mentor_known = True
            $ hide_all_chars()
            "你没有说话。有些痛苦，不需要语言来回应。"
            "两个失去过重要之人的年轻人沉默地坐着，安静得能听见远处狗吠。"
            "喷泉的水声填满了一切空隙。"

    hide prince_img with dissolve

    ## ============================================================
    ## 新增场景：宫廷图书馆
    ## ============================================================

    scene bg study with dissolve
    $ unlock_gallery("bg_study")

    $ play_music("audio/music/night_mystery.ogg", fadein=2.0)

    "从花园回来后，你辗转难眠。"

    "索性披衣起身，决定去做一件来王都之前就计划好的事——"

    "去王宫图书馆查阅先王时期的档案。"

    "王宫图书馆在宫殿的西翼，是一座三层的圆形建筑，藏书据说超过十万卷。"

    "你在夜间找到了入口。守夜的管理员是个半聋的老人，在你出示了领主令牌后，颤巍巍地为你开了门。"

    "图书馆内部比外面看起来更加壮观。三层的书架从地面延伸到穹顶，像一座由书籍建成的峡谷。"

    "空气中弥漫着陈旧羊皮纸和蜡烛油的气味——这是时间本身的味道。"

    "你来这里有一个明确的目的：查阅先王在位最后几年的宫廷记录。"

    if testament_forged_known:
        "如果王子说的是真的——王后篡改了先王遗诏——那么也许在这些旧档案中能找到蛛丝马迹。"
    else:
        "父亲的信中曾暗示先王临终前留下了重要文件。也许在这些旧档案中能找到蛛丝马迹。"

    menu:
        "找教会档案员私下打听先王临终圣礼" if faith >= 50:
            $ change_stat("faith", 5)
            $ change_stat("intrigue", 5)
            $ ch4_archive_priest_route = True

            $ hide_all_chars()
            "你绕过中央阅档大厅，直接去了教会档案侧室。"

            "档案员是个年过六旬的老修士，正在抄一本破旧的圣经。"

            "你没拿身份。你只是合十行了一礼，用修道院里学的祷词起头。"

            "老修士抬头看了你一眼。两秒后，他放下了笔。"

            "「……您是哪个堂区出来的子弟？ 这段祷词只有南方修道院讲。」"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "圣·尤里安。我父亲也是。"

            $ hide_all_chars()
            "老修士的眼睛里有了不一样的东西。"

            "「……请坐。我倒杯热水。您是来问什么的？」"

            "你压低声音：「先王临终前最后一次圣礼，哪位主教主持？当时是否有第二位见证？」"

            "老修士沉默了很久。然后他站起身，走到角落的木箱前，取出一本用红绳系的薄册。"

            "「这本临终圣礼日志没归在公档。当时主持的是费雷恩大主教。见证人位空着——」"

            "「——按规矩，临终圣礼必须有两位神职在场。没有第二位，这场圣礼在教会眼里其实不算成立。」"

            "你的手指略微一紧。这是教会内部都不公开的秘密。而你，因为虔信，因为说出「圣·尤里安」四个字，一个老修士愿意告诉你。"

            "你向他鞠了一礼。没说谢。他也没说不客气。但你走出门时，他在你背后轻声说了一句："

            "「……走吧。圣母保佑您查到您想查的。」"

        "仔细搜查先王最后三年的宫廷日志":
            $ change_stat("intrigue", 5)
            "你在浩如烟海的档案中翻找了整整两个时辰。"
            "大多数文件都是例行公事——赐封、税赋、外交照会。"
            "但在先王驾崩前三个月的记录中，你发现了一些不寻常的条目——"
            "连续七天的宫廷日志被人撕掉了。只留下参差不齐的纸边。"
            "这七天——正好是先王病重到驾崩的那段时间。"
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "有人刻意销毁了这些记录……"
            $ hide_all_chars()
            "你还在角落里找到了一本看起来很不起眼的账本。翻开一看，竟然是先王私人药房的用药记录。"
            "记录的最后一页写着：「圣历四七三年秋，奉命配制{b}暮色之露{/b}解药一剂。未果。药材不足。」"
            if poison_evidence:
                "暮色之露——你在商人卡尔那里听过这个名字。那是一种无色无味的毒药。"
                "先王的药房在配制它的解药？这说明——"
                "有人在给先王下毒，而先王知道这件事。他试图自救，但没有成功。"
                $ change_stat("intrigue", 5)
            else:
                "暮色之露……这个名字你记住了。也许它很重要。"

        "查找父亲在王都的活动记录" if intrigue >= 45:
            $ change_stat("intrigue", 8)
            "你找到了宫廷来访记录。你父亲的名字出现了很多次——几乎每年都来觐见两到三次。"
            "但在先王驾崩前一年，他的来访次数突然增加到了每月一次。"
            "而且，记录显示他每次来访时，都会单独面见先王——这在当时是极不寻常的特权。"
            "更奇怪的是，在先王驾崩之后，你父亲再也没有来过王都。"
            "直到他自己去世。"

        "寻找先王遗诏的相关文件" if intrigue >= 58:
            $ change_stat("intrigue", 12)
            "你在档案中搜索「遗诏」相关的记录。"
            "你找到了先王驾崩后的继位公告——上面写着「先王遗诏，命王后伊莎贝拉摄政，直至王子成年。」"
            "但「成年」的定义模糊不清。按照王国旧律，王子十六岁即为成年。弗雷德里克今年已经二十二岁了。"
            "也就是说，王后早就应该还政于王子。但她没有。"
            "你还注意到，这份继位公告上的先王印章——和你在图书馆其他文件上看到的印章略有不同。"
            "普通人不会注意到这个差别。但你在父亲的书房里见过先王的亲笔信，上面的印章……"
            "印章是被伪造的。"
            if testament_forged_known:
                "又一份证据。你早已知道遗诏是伪造的——但亲眼看到第二份佐证，仍让你握紧了拳头。"
            else:
                "你的手开始颤抖。如果这是真的——整个王国的权力根基都是建立在一份伪诏之上。"

    "就在准备离开时，你用袖子拂过一个不起眼的档案箱——箱盖下方露出一角被折叠过的羊皮纸。"

    "你小心翼翼地抽出来——那是一封火漆未启的密令，印鉴正是王后的百合纹章。它本该在昨夜送出，却被什么人匆忙遗落在这里。"

    $ collect_item("queen_decree")
    "你把这封密令连同刚才的发现一起折好，藏进内衣口袋。"

    "离开图书馆时，你回头看了一眼——在阴暗的走廊尽头，似乎有一个身影一闪而过。"

    "有人在跟踪你？"

    "你加快脚步，回到了住所。"

    "回到房间后，你锁好门，把文件摊在桌上仔细研读。"

    "蜡烛烧了大半，蜡泪淌到桌面上。你的脑海里渐渐拼凑出一幅可怕的画面——"

    if queen_poisoned_king_known and testament_forged_known:
        "文件印证了你已经知道的事实——先王被毒杀，遗诏是伪造的。但亲眼看到白纸黑字的证据，感觉完全不同。"
    elif queen_poisoned_king_known:
        "先王被毒杀——这你已经知道了。但文件揭示了更多：遗诏很可能是伪造的。"
        $ testament_forged_known = True
    elif testament_forged_known:
        "遗诏被篡改——这你早有怀疑。但文件中还有更可怕的真相：先王并非自然死亡，有人下毒。"
        $ queen_poisoned_king_known = True
    else:
        "先王并非自然死亡。有人下毒。而遗诏很可能是伪造的。"
        $ queen_poisoned_king_known = True
        $ testament_forged_known = True

    "你的父亲发现了这一切——所以他也死了。"

    "现在，你走上了和父亲同样的道路。"

    "你看着窗外夜色中的王宫，那些高耸的塔尖在夜色里沉默地立着。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve

    elena "领主大人，你今晚去了图书馆？"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你怎么知道？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "你靴子上有图书馆地下室特有的灰白色粉尘。"

    "你低头看了一眼——确实如此。"

    elena "找到什么了？"

    menu:
        "如实告知艾琳娜你的发现":
            $ change_rel("rel_elena", 5)
            $ change_stat("intrigue", 3)
            $ hide_all_chars()
            "你把今晚的发现一五一十地告诉了她。"
            "艾琳娜的表情从平静变为凝重，最后变成了一种你从未见过的——恐惧。"
            $ hide_all_chars("elena_img")
            show elena_img sad at left with dissolve
            elena "如果这些是真的……你手中握着的，是足以颠覆整个王国的东西。"
            elena "你必须把文件藏好。最好不要放在身上——万一被搜身……"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你有什么建议？"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "花园的第三棵玫瑰丛后面有一个石头松动的缝隙。我小时候经常在那里藏东西。"
            elena "没有人知道那个地方。"

        "含糊其辞——找到了一些有趣的历史文献":
            $ change_stat("intrigue", 5)
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "只是一些老旧的档案。关于先王时代的宫廷记录。很枯燥。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "……你不想告诉我。"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "不是不想。是不能。知道得越多越危险——这话你应该比我更懂。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "也对。"
            "她把准备说的话咽了回去，话题转开了。"

    elena "还有一件事——我刚才在走廊上看到一个可疑的人。"

    elena "他穿着侍从的衣服，但走路的姿势不对。那是受过军事训练的步伐。"

    elena "我跟了他一段，他走进了王后寝宫方向的侧廊。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "王后的人？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "很可能。她在监视你。"

    elena "从现在起，我们说任何重要的话，都去花园。只有露天的地方才相对安全。"

    hide elena_img with dissolve

    $ hide_all_chars()
    "你把文件藏在枕头下的暗格里——那是艾琳娜第一天检查房间时发现的。"

    "然后你吹灭了蜡烛，躺在黑暗中，听着自己的心跳。"

    "你想起了父亲书房里那句话——「知道得越少，越安全。」"

    "但你已经知道了太多。退路已经断了。"

    "唯一的选择，是继续向前。"

    ## ============================================================
    ## 场景4：艾琳娜的真心
    ## ============================================================

label ch4_elena:

    $ play_music("audio/music/sad.ogg", fadein=2.0)
    scene bg palace_garden with dissolve
    $ unlock_gallery("bg_palace_garden")
    $ set_mood("calm")
    $ set_weather("fireflies")

    "第二天傍晚。"

    "觐见的事务告一段落，你感到疲惫。"

    "在王都的每一刻，你都必须保持警惕，每一句话都要经过三重思考才能说出口。"

    "你在花园的长椅上坐下，想要片刻的安宁。"

    "夕阳将天边染成橘红色，像一幅正在燃烧的画。"

    "花园里弥漫着玫瑰和紫藤的香气。喷泉的水声轻柔地回荡。"

    "一只画眉鸟落在旁边的树枝上，歌唱了几声，又飞走了。"

    "这一刻，你几乎忘了自己身在何处。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve

    elena "领主大人。"

    "她的声音从身后传来，轻得像一缕风。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你跟来了。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "保护您是我的职责。无论是王后的命令……还是我自己的选择。"

    $ hide_all_chars()
    "她在你旁边坐下，保持着恰到好处的距离——不太近，也不太远。"

    "夕阳的余晖洒在她的脸上，给她平时冷峻的面容镀上了一层柔和的金色。"

    "在这余晖中，你第一次认真地看着艾琳娜。"

    "她脸上没有浓妆，皮肤被风霜磨过，颧骨边有一道浅浅的旧疤。这张脸在满厅贵妇里显得格格不入。"

    "她的眼睛里没有了平时的机警和算计，取而代之的是一种你从未见过的柔软。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "领主大人，来了王都之后……您有没有觉得这里和艾登堡很不一样？"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "当然不一样。这里更大、更复杂、也更危险。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "不是那个意思。我是说……人。"

    elena "在艾登堡，卖面包的老婆婆会叫你「好孩子」。铁匠看到你经过会大声打招呼。连城门口的守卫都知道你喜欢早起散步。"

    elena "而在这里——每个人看你的眼神都在估算你的价值。你是谁、你有多少兵、你站在哪边——这就是你的全部。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你在这样的环境里长大的。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    if elena_spy_known:
        elena "我的过去……你已经知道了大部分。但有一件事我一直没说——"

        elena "那些任务里，有个男爵……后来被以叛国罪处死了。在绞刑架上，他一直在喊冤。"
    else:
        elena "我的过去……没落贵族的孤女，侍女学院的工具。"

        elena "她们教我读书写字，也教我使毒、用剑、监视他人。十二岁的孩子，被一步步磨成了一件武器。"

        elena "毕业后，我被派去各地执行任务。监视王后怀疑不忠的领主。艾登堡是我的第四个任务。"

        elena "有个男爵……后来被以叛国罪处死了。在绞刑架上，他一直在喊冤。"

        $ elena_spy_known = True

    elena "我不知道他是不是真的无辜。但我知道，是我提供的情报把他送上了绞刑架。"

    "她的声音很平静，像是在讲述别人的故事。但你看到她的手指紧紧地攥着衣角。"

    if not elena_identity_exposed_known:
        elena "后来，你的父亲发现了我的身份。但他没有恨我——他说，一个十二岁就被训练成工具的孩子，不应该为别人的野心负责。"

        elena "他把我介绍给了暗百合。他们说，王后才是真正的敌人。"
    else:
        elena "我父亲识破我、把我引向暗百合——这些你都听我讲过了。"

    elena "但在暗百合……我依然只是一枚棋子。只是换了一个主人。"

    elena "领主大人，从来没有人……像你这样对待我。"

    elena "在王后身边，我是工具。在暗百合那里，我是棋子。"

    elena "只有你……从第一天起就问我需不需要休息，住得习不习惯。"

    elena "那天你受了伤，你做的第一件事是问我有没有事。"

    elena "你知道吗——那一刻，我第一次不知道怎么回答了。"

    elena "因为……从来没有人在乎过我是否安好。"

    if rel_elena >= 30:
        elena "我……"

        "她的声音突然变得很轻，像是在说一句很重很重的话——轻得几乎要被风吹走。"

        elena "我不知道这算不算……我不懂那个词。"

        elena "但我知道，每次看到你平安无事，我就会松一口气。"

        elena "每次你对我笑，我心里就会暖一下。"

        elena "这种感觉……很陌生。但我不讨厌它。"

        menu:
            "握住她的手" if not marriage_route:
                $ log_decision("第四章", "与艾琳娜确认浪漫关系")
                $ elena_romance = True
                $ change_rel("rel_elena", 25)
                $ hide_all_chars()
                "你伸出手，握住了她的。她的手微微发抖。"
                "她的手比你想象的小。掌心有薄茧——那是多年使剑留下的痕迹。"
                hide elena_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "无论接下来发生什么，我会保护你。"
                hide player_char_img
                $ hide_all_chars("elena_img")
                show elena_img at left with dissolve
                elena "……傻瓜。应该是我保护你才对。"
                $ hide_all_chars()
                "她笑了。你从来没见过她这样笑。"
                "不是那种训练出来的微笑，也不是面具般的礼貌。"
                "是一种从心底溢出来的、带着泪光的笑。"
                "夕阳完全沉入了地平线。最后一缕金光消失的瞬间，她把头靠在了你的肩上。"
                "你们就这样在暮色中坐了很久。"
                "没有说话。不需要说话。"

            "感谢她的付出，但保持距离":
                $ log_decision("第四章", "与艾琳娜保持距离")
                $ change_rel("rel_elena", 10)
                hide elena_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "艾琳娜，你不是任何人的工具。在艾登堡，你是自由的。"
                player "不管以后怎样——你的人生应该由你自己决定。不是王后，不是暗百合，也不是我。"
                hide player_char_img
                $ hide_all_chars("elena_img")
                show elena_img at left with dissolve
                elena "……谢谢你。"
                $ hide_all_chars()
                "她的声音很轻，但你听到了其中的重量。"
                "像一个背负了太久重担的人，终于听到有人说：「你可以放下了。」"
    else:
        elena "……算了，什么都没有。"
        "她别过头去，但你看到她的睫毛上似乎有什么东西在闪烁。"
        elena "我只是想说，无论您做什么选择，我都会站在您这边。"
        elena "这不是命令。是我的决定。"
        $ change_rel("rel_elena", 10)

    hide elena_img with dissolve

    "你独自在花园里又坐了一会儿。"

    "夜空中繁星点点。你想起了艾登堡的夜空——那里的星星更亮，因为没有城市的灯火遮挡。"

    "但此刻，你不确定自己还能回到那片星空之下。"

    "王都的漩涡已经将你卷入其中。"

    if elena_romance and rel_elena >= 80:
        ## batch 5 反馈"云" (2026-05-05): 花园握手后独处, 恋爱推进
        "你以为今晚就这样过去了——"

        "脚步声从花径那头传来。不急。"

        $ hide_all_chars("elena_img")
        show elena_img at right with dissolve
        elena "您还坐在这里。我以为您回了。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "看星空。"

        $ hide_all_chars()
        "她在你旁边坐下。隔着一掌的距离。"

        "她随手拿过一截枯枝，在地上画了一个不规则的圆。"

        $ hide_all_chars("elena_img")
        show elena_img at right with dissolve
        elena "王都的夜空看不到几颗星星。"

        elena "我十六岁那年，在北方某地住过半年。那里一抬头就是整条银带。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "艾登堡的星空也比这里亮。"

        player "等这事完了，一起回去看一次。"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at right with dissolve
        elena "……我记着。别食言。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "这次真去。我们俩去，不带兵，不带随从。"

        player "走山路，五天。"

        $ hide_all_chars()
        "她没接话。也没移开。"

        "过了好一会儿，她把头轻轻靠在了你的肩上。"

        "你伸手扶了一下她垂落到锁骨边的一缕发丝，没拨开，只是让它顺着她的颈线垂下来。"

        "没再说话。谁也没说。"

        "夜风吹过花径，把刚才她在地上画的那个不规则的圆吹得淡了，但还在。"

        $ change_rel("rel_elena", 10)

    ## ============================================================
    ## 新增场景：觐见之后的清晨——王子的信
    ## ============================================================

    scene bg royal_palace with dissolve
    $ unlock_gallery("bg_royal_palace")
    $ play_music("audio/music/castle_calm.ogg", fadein=2.0)

    "又过了几天。一个清晨。"

    "你刚洗漱完毕，就听到门外有人轻叩。"

    if prince_ally:
        "是一个穿着普通仆人衣服的年轻人。他递给你一个蜡封的信封，然后迅速离去。"

        "你拆开信封。里面是一张薄薄的纸——王子的笔迹，工整而有力。"

        "信的内容比你预想的更加震撼——"

        "王子列出了三个关键人物的名字：主教马修斯、宰相蒙塔古伯爵、以及一个你从未听过的名字——「影子法官」格里芬。"

        "据王子所说，这三个人参与了对你父亲的谋害。"

        "主教提供了宗教审判的借口，宰相负责执行，而格里芬——是实际动手的人。"

        "信的最后一行写着：「这是我的诚意。现在，你愿意信任我了吗？」"

        $ griffin_known = True
        $ collect_item("baron_pact")

        menu:
            "将信件妥善保管，作为日后的证据":
                $ change_stat("intrigue", 5)
                "你把信件折好，缝进了外套的衬里。"
                "这封信的价值不可估量——它不仅是真相的线索，也是一把悬在某些人头上的剑。"

            "记住内容后烧掉信件——太危险了" if intrigue >= 45:
                $ change_stat("intrigue", 8)
                $ change_stat("reputation", -2)
                "你把信上的每一个字都深深刻进脑海，然后将信纸投入壁炉的火焰中。"
                "纸张在火中卷曲、发黑、化为灰烬。"
                "有些东西，只能存在于记忆中。"

    elif prince_betrayed:
        "你在房间里写了一封密信，详细记录了王子昨晚的言行。"
        "然后，你叫来一个可靠的侍从。"
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "把这封信送到王后的侍女总管手中。亲手交，不要经过任何人。"
        $ hide_all_chars()
        "侍从领命而去。你靠在椅子上，闭上眼睛。"
        "你做的事是正确的……吗？"
        "你不确定。但你选择了这条路，就必须走到底。"
    else:
        "你靠在窗边，凝望着王都的晨雾。"
        "王子昨晚的话仍在脑海中回荡。你没有做出任何承诺——既没有结盟，也没有背叛。"
        "在这座充满阴谋的城市里，保持中立也许是最困难的选择。"

    "你正在思考下一步行动时——"

    ## ============================================================
    ## 场景5：背叛
    ## ============================================================

label ch4_betrayal:

    $ play_music("audio/music/betrayal.ogg", fadein=1.0)
    scene bg royal_palace with dissolve
    $ unlock_gallery("bg_royal_palace")

    "一阵急促的脚步声将你从沉思中惊醒。"

    $ play_sound("audio/sfx/door_knock.ogg")

    "砰砰砰——有人在猛烈地敲门。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "领主大人！大事不好！"

    "雷恩满头大汗地冲进房间，脸色铁青。"

    if prince_betrayed:
        captain "王子殿下被逮捕了！说是谋反！"
        captain "而且……王后要见您。她说要「奖赏您的忠诚」。"

        $ hide_all_chars()
        "计划正在按预期进行。"

        "但走出房间时，你看到走廊尽头——两个近卫正押着一个人走过。"

        "是弗雷德里克。"

        "他的手被铁链锁着，嘴角有血迹。衣衫凌乱，头发散落。"

        "但他没有低头。他昂着下巴，像一个行走在刑场上的国王。"

        "他的目光扫过走廊，看到了你。"

        "那一刻，他的眼睛里没有愤怒——只有一种冰冷的了然。"

        "他什么也没说。但你读懂了他的目光：「我知道是你。」"

        "你的计划奏效了。但看着他被押解经过时，你心里有什么东西——碎了一小块。"

    elif prince_ally:
        captain "有人向王后告发了王子殿下的密谋！"
        captain "王子被关进了地牢！而您的名字也在告密信上！"
        $ change_rel("rel_queen", -20)
        hide captain_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "什么？！"
        hide player_char_img
        $ hide_all_chars("captain_img")
        show captain_img at left with dissolve
        captain "告密信很详细——包括昨晚你们在花园密会的时间和内容。"
        captain "有人在暗中监视你们！"

        show elena_img at right with dissolve
        elena "是花园里的暗哨。我检查过了——在第三棵橡树后面有一个隐蔽的瞭望点。"
        elena "应该是王后的人。他们可能从一开始就在监视花园。"
        hide elena_img with dissolve

        $ hide_all_chars("captain_img")
        show captain_img at left with dissolve
        captain "领主大人，我们必须马上行动，否则下一个被抓的就是您！"
        captain "我已经让卫队做好了撤离准备。但时间不多——"
        captain "王宫的大门随时可能关闭。"
    else:
        captain "王宫出大事了！王子殿下被指控谋反，已经被关押！"
        captain "整个王宫都乱成了一锅粥——"
        captain "王都全面戒严，所有外地领主不得离开！"
        captain "城门已经关闭，街上到处是巡逻的士兵。"

    hide captain_img with dissolve

    if prince_ally and not prince_betrayed:
        $ hide_all_chars()
        "你的心跳得撞到嗓子。你只有几秒钟。"

        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve

        elena "领主大人，我了解这座王宫。有三条路可以走。"
        elena "第一，去地牢救人。我知道地牢的布局和守卫换班的时间。"
        elena "第二，撇清关系。销毁所有证据，否认一切。以你目前的身份，他们很难定你的罪。"
        elena "第三，趁乱逃离王都。城西的排水渠可以通到城外。"
        elena "无论你选哪条路——我都跟你走。"

        hide elena_img with dissolve

        menu:
            "冒险营救王子" if power >= 55:
                $ change_stat("power", 10)
                $ change_rel("rel_prince", 30)
                $ change_rel("rel_queen", -30)
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "我答应过他。我不能食言。"
                jump ch4_rescue

            "撇清关系，否认一切":
                $ change_stat("intrigue", 5)
                $ change_rel("rel_prince", -20)
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "告诉所有人，我根本不认识王子。那天晚上我一直在房间里。"
                "雷恩迟疑了一下，但还是点了头。"
                hide player_char_img
                $ hide_all_chars("captain_img")
                show captain_img at left with dissolve
                captain "明白。我去安排人证。"

                $ hide_all_chars()
                "三天后，你听说地牢里的王子一个字都没为你辩解。他既没有指认你，也没有否认。"
                "他只是沉默。那种沉默比任何愤怒都要锋利。"

                jump ch4_deny

            "趁乱逃离王都":
                $ change_stat("power", -5)
                $ change_rel("rel_prince", -15)
                hide captain_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "我们走。现在就走，趁他们还没来抓我。"
                "雷恩跟在后面，半晌没出声，最后还是开了口。"
                $ hide_all_chars("captain_img")
                show captain_img at left with dissolve
                captain "殿下还在地牢里。"
                $ hide_all_chars()
                "你没停下脚步。他也没再问第二遍。"
                jump ch4_escape
    else:
        jump ch4_aftermath

    ## ============================================================
    ## 场景5a：营救王子
    ## ============================================================

label ch4_rescue:
    $ play_music("audio/music/dungeon_drip.ogg", fadein=1.0)
    scene bg dungeon with dissolve
    $ unlock_gallery("bg_dungeon")
    $ set_mood("battle")
    $ clear_weather()

    "地牢在王宫的最底层——深入地下三层的石头迷宫。"

    "空气潮湿而冰冷，弥漫着铁锈和霉变的气味。"

    "火把在墙上的铁架上跳动，将你的影子投射在粗糙的石壁上，像一群鬼魅。"

    "你带着雷恩和几个忠诚的士兵，在艾琳娜的引导下潜入了地牢。"

    show elena_img at right with dissolve

    elena "（低声）前面有两个守卫。换班时间在半个时辰之后。"

    if dark_lily_joined:
        elena "暗百合的人已经打通了关节。"
        "几分钟后，你看到两个守卫突然打了个大大的哈欠，然后靠在墙上，缓缓滑坐下去——睡着了。"
        elena "迷香。无色无味。他们会睡到天亮。"
        $ change_stat("intrigue", 5)
    else:
        "你用金币买通了一个看守。代价不菲。"
        $ change_stat("wealth", -15)
        elena "（低声）他只能给我们一刻钟的时间。我们必须快。"

    hide elena_img with dissolve

    $ hide_all_chars()
    "你压低声音，看着面前三道铁门。"

    "第一道刚刚撬开，里面是回字形的廊道。三道门，一道比一道厚。"

    "王子在最深处。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "（低声）这一段——我们退不出去了。一旦警报响起，整个王宫都会扑下来。"

    hide elena_img with dissolve
    $ hide_all_chars()
    "王子的命悬在这一晚。"

    menu:
        "让艾琳娜引开守卫":
            $ hide_all_chars()
            "你点头。"
            "艾琳娜没多说一个字，转身溶进墙影里——她的脚步声在三秒后就听不见了。"
            "你们贴在墙边等。"

            $ trigger_crisis("intrigue", 5,
                "艾琳娜在另一头制造响动。如果她的动静恰到好处, 守卫追过去, 你们这边就空了——但守卫如果太警觉, 她就回不来了。",
                "ch4_rescue_stealth_win", "ch4_rescue_stealth_lose",
                courage_cost=25, allow_skip=False)
            call crisis_encounter from _call_crisis_ch4_lure
            ## allow_skip=False 不会 fall-through, 此处 jump 兜底
            jump ch4_rescue_stealth_lose

        "直接迷香放倒":
            $ hide_all_chars()
            if dark_lily_joined:
                "暗百合的人递了一只小瓷瓶过来。"
                "「这一剂量是按守卫的体型算的。」暗百合的女人说话像数账。「呼吸十二次内见效。」"
                "你点头。"
            else:
                "你只有一只玻璃瓶——艾登堡药匠配的旧方子。"
                "剂量你拿不准。少了不睡，多了出事。"

            $ _stealth_diff = 2 if dark_lily_joined else 4
            $ trigger_crisis("intrigue", _stealth_diff,
                "迷香的剂量必须刚好。少了, 守卫只会发懵; 多了——你们今晚就要在地牢深处给两个穿盔甲的尸体收尾。",
                "ch4_rescue_stealth_win", "ch4_rescue_stealth_lose",
                courage_cost=25, allow_skip=False)
            call crisis_encounter from _call_crisis_ch4_smoke
            jump ch4_rescue_stealth_lose

        "假扮巡查官":
            $ hide_all_chars()
            "你脱下外袍，换上从一个值夜执事身上扒下来的灰色长服。"
            "雷恩演副官——他半张脸藏在兜帽下，手里握着一卷假造的巡查文牒。"

            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "（低声）这一行守卫里，只要有一个人多问一句，我们就完了。"

            hide captain_img with dissolve
            $ hide_all_chars()

            $ trigger_crisis("intrigue", 6,
                "你们走到第一道铁门前。守卫抬头看你, 火把照着你伪造的徽记。这一关——靠的是脸不发烫, 手不发抖。",
                "ch4_rescue_stealth_win", "ch4_rescue_stealth_lose",
                courage_cost=25, allow_skip=False)
            call crisis_encounter from _call_crisis_ch4_disguise
            jump ch4_rescue_stealth_lose

label ch4_rescue_stealth_win:
    $ hide_all_chars()
    "三道铁门一道道开过去。"
    "睡着的睡着，被骗走的被骗走，被绕开的被绕开。"
    "王子的牢房就在最深处——你听见自己心跳的声音。"

    $ log_decision("第四章", "成功潜入地牢")

    jump ch4_rescue_inner

label ch4_rescue_stealth_lose:
    $ hide_all_chars()
    "计划在最后一道门前出了岔。"

    "一个守卫多看了你两眼，眨眼之间，警铃响了。"

    $ play_sound("audio/sfx/sword_draw.ogg")

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "我顶上！领主大人退后！"

    "雷恩第一个冲上去，用剑挡下三人围攻。"

    "你看见他左肩中了一刀，血顺着甲片流下——但他还站着。"

    captain "走！别管我！"

    hide captain_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "（咬牙）王子的牢房——快！"

    hide elena_img
    $ hide_all_chars()
    "你和艾琳娜拖着雷恩冲进最深的牢房——"

    "牢房空了。"

    "石床上的镣铐还摆着，但人不见了。"

    "王后已经把王子转移到了更下层——而那个位置，你们今晚到不了。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "（低声）撤。从我来时的暗道走。再耽搁十息，王宫的卫队就堵到这里。"

    hide elena_img with dissolve

    $ hide_all_chars()
    "你扶着雷恩，跟着艾琳娜钻进墙后的窄缝。"
    "你们沿着她事先摸过的路，在守卫合围之前钻出王宫。"

    "王子还在敌人手里。"
    "但你们活着出来了。"

    $ ch4_rescue_partial = True
    $ log_decision("第四章", "潜入失败, 王子被转移, 退回艾登堡")

    jump ch4_rescue_partial_recovery

label ch4_rescue_inner:
    "你们穿过一道又一道铁门，越走越深。"

    "地牢深处的牢房更加阴暗。你看到一些锈迹斑斑的刑具挂在墙上——铁夹、拉架、烙铁……"

    "你不想知道这些东西被用在过多少人身上。"

    "终于，在最深处的一间牢房前，你们停下了脚步。"

    $ hide_all_chars("prince_img")
    show prince_img at left with dissolve

    $ hide_all_chars()
    "王子蜷缩在牢房角落。他的嘴角有血迹，一只眼睛肿了起来。华贵的衣服已经破烂不堪。"

    "但他看到你的那一刻，眼睛里亮起了一道光。"

    $ hide_all_chars("prince_img")
    show prince_img at left with dissolve
    prince "你来了……我以为你会弃我于不顾。"

    hide prince_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我答应过的事不会食言。走吧。"

    hide player_char_img
    $ hide_all_chars("prince_img")
    show prince_img at left with dissolve
    prince "等等——他们审问了我。我什么都没说。但他们知道你的事了。"

    prince "你回不去艾登堡了……至少不能走大路。"

    hide prince_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "这些以后再说。先离开这里。"

    $ play_sound("audio/sfx/sword_draw.ogg")

    $ hide_all_chars()
    "雷恩砍断了牢门的铁链。你扶起王子，搭着他的肩膀向外走去。"

    "在逃离的路上，你们遇到了一队巡逻的守卫。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "领主大人！前面有六个人！"

    menu:
        "硬闯——直接杀出去":
            $ change_stat("power", 5)
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "抽剑！"
            $ play_sound("audio/sfx/sword_draw.ogg")
            $ hide_all_chars()
            "你拔出剑，冲在最前面。"
            "短暂而激烈的搏斗。火把被打翻，在地上滚动，光影混乱。"
            "你的剑法也许不如那些职业剑手，但你的决心弥补了技术的不足。"
            "雷恩挡下了一记劈砍，反手一剑刺穿了对方的肩膀。"
            "三分钟后，六个守卫全部倒下。没有人被杀死——你只用了剑背和剑柄。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "领主大人，您不杀他们？"
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "他们也是在执行命令。走。"

        "让艾琳娜想办法悄悄绕过" if intrigue >= 45:
            $ change_stat("intrigue", 8)
            $ change_stat("reputation", -2)
            $ hide_all_chars()
            "艾琳娜的脚步声一瞬间就没了。几秒后，你听到走廊另一端传来一声响动——像是什么东西倒了。"
            "守卫们立刻警觉起来，向声音的方向跑去。"
            "通道空了。你们迅速穿过。"
            "艾琳娜像一只猫一样无声无息地出现在你身后。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "走。快。他们马上会发现。"

    hide captain_img with dissolve
    hide prince_img with dissolve

label ch4_rescue_aftermath:
    scene bg forest_path with dissolve
    $ unlock_gallery("bg_forest_path")

    if ch4_rescue_partial:
        ## 失败分支: 王子在艾登堡西边山林被神秘人放出, 跟主角会合后启程回艾登堡
        ## (栀子 batch 11 第 1 条: 失败分支不能用"爬出王宫"叙事, 地点矛盾)
        "晨雾还没散尽。三个人——你、雷恩、王子——牵着两匹半马，沿着山林边缘的小径向东。"

        "马蹄踩在湿润的落叶上，几乎听不见声音。这片山林是艾登堡西边的天然屏障，再走半日就能进入你的领地。"

        "王子不再是王宫深处那个浑身是伤的囚徒。粗布外袍下的肩膀已经直起来一些，眼睛里也有了光。"

        "你回头望了一眼来路。雾气吞掉了树影，但你知道——王宫的探子迟早会追到这里。"

        "城墙上的信号灯，王都那边的卫队……都不在你眼前。但你心里清楚——"
    else:
        "你们从地牢的一条废弃排水渠爬出了王宫，在暗夜中穿过了几条小巷。"

        "城门已经关闭。但艾琳娜带你们找到了城西的排水渠出口——"

        "一个半人高的石洞，通向城外的护城河。"

        "你们一个接一个地爬出去。护城河的水冰冷刺骨，你浑身湿透，但你没有停下。"

        "当你终于站在城外的旷野上时，回头望了一眼灯火通明的王都。"

        "城墙上的信号灯亮了——他们已经发现了。"

        "你们成功逃出了地牢，在暗夜中离开了王都。"

    "但你知道，从这一刻起，你和王后之间再无回旋的余地。"

    "你不再是一个安分守己的边境领主了。"

    "你是一个叛逆者。一个通缉犯。一个站在王子身边的人。"

    "而王子——这个浑身是伤、却依然昂着头的年轻人——他用沙哑的声音说——"

    $ hide_all_chars("prince_img")
    show prince_img at left with dissolve

    prince "谢谢你。我不会忘记今晚。"

    prince "从今天起，你不再只是我的盟友。你是我的兄弟。"

    hide prince_img with dissolve

    $ hide_all_chars()
    "你没有说话。只是在黑暗中点了点头。"

    "你们在夜色中疾驰了两个时辰，终于在一条偏僻的岔路口停下了马。"

    jump ch4_prince_farewell

    ## ============================================================
    ## 场景5b：否认一切
    ## ============================================================

label ch4_deny:

    $ play_music("audio/music/tension.ogg", fadein=2.0)
    scene bg royal_palace with dissolve
    $ unlock_gallery("bg_royal_palace")

    "你装作若无其事，在王宫中度过了忐忑的两天。"

    "这两天是你人生中最漫长的四十八个小时。"

    "每一次有脚步声在走廊响起，你都会不由自主地竖起耳朵。"

    "每一次有人敲门，你的手都会摸向腰间的匕首。"

    "王后派了两拨人来问话。"

    "第一拨是一个文官——他彬彬有礼地询问你在王都的行程，你去过哪里，见过哪些人。"

    "你回答得滴水不漏。你说自己大部分时间都在住所里休息，偶尔去花园散步。"

    "第二拨来的是一个近卫军官——他的态度就没那么友善了。"

    $ hide_all_chars("soldier_generic_img")
    show soldier_generic_img at left with dissolve
    soldier "有人看到你那天晚上出现在花园。"

    hide soldier_generic_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我的确去了花园。散步。一个人。"

    hide player_char_img
    $ hide_all_chars("soldier_generic_img")
    show soldier_generic_img at left with dissolve
    soldier "你遇到什么人了吗？"

    hide soldier_generic_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "一只猫。它对我不太友好。"

    $ hide_all_chars()
    "军官盯着你看了很久。你回望着他，面无表情。"

    "最终，他转身离去。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve

    elena "他们暂时没有证据。但你不能掉以轻心。"

    elena "我检查了王子被逮捕时的审讯记录——他没有供出你。"

    elena "但如果他们继续审……"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我们必须尽快离开。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "明天戒严应该会解除。到时候你以「领地有急事」为由请辞，应该可以走。"

    hide elena_img with dissolve

    $ hide_all_chars()
    "王后派人来问过话。你应对得滴水不漏。"

    "最终，由于缺乏证据，你被允许离开王都。"

    "走出城门的那一刻，你长长地呼出一口气。"

    "但你知道王后的眼线会一直盯着你。从今以后，你的一举一动都在她的监视之下。"

    "而花园里的那个王子——你不知道等待他的将是什么。"

    "你没有回头。"

    jump ch4_end

    ## ============================================================
    ## 场景5c：逃离王都
    ## ============================================================

label ch4_escape:

    $ play_music("audio/music/chase.ogg", fadein=1.0)
    scene bg forest_path with dissolve
    $ unlock_gallery("bg_forest_path")

    "你连夜离开了王都。"

    "时间紧迫。你来不及收拾行李，只带了武器和那些从图书馆找到的文件。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve

    elena "跟我走。我知道一条路。"

    hide elena_img with dissolve

    $ hide_all_chars()
    "艾琳娜带路，穿过城西的排水渠——那条只有她知道的逃生通道。"

    "排水渠的入口隐藏在一间废弃仓库的地板下面。你们搬开沉重的木板，一股恶臭扑面而来。"

    "水没到膝盖，冰冷刺骨。黑暗中你只能听到水声和自己沉重的呼吸。"

    "排水渠又窄又矮，你必须弯着腰前行。头顶不时有水滴落下，冰凉地打在脖子上。"

    "走了大约一刻钟，前方出现了微弱的月光——那是出口。"

    "爬出排水渠时，你的手被石壁划破了。血和泥水混在一起，火辣辣地疼。"

    "护城河就在眼前。你们涉水而过，冰冷的河水几乎让你失去知觉。"

    scene bg forest_path with dissolve
    $ unlock_gallery("bg_forest_path")

    "雷恩带着卫队在城外五里的林子里接应。看到你浑身湿透、狼狈不堪的样子，他的脸上闪过一丝心疼。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "领主大人！您没事吧？"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "走。别停。他们很快就会追来。"

    hide captain_img with dissolve

    $ hide_all_chars()
    "你们换了马，连夜向北疾驰。"

    "马蹄声在空旷的原野上回荡。夜风刮在湿透的衣服上，冷得刺骨。"

    "但你不敢停。你知道，王后的追兵可能已经在身后了。"

    show elena_img at right with dissolve

    elena "不要走大路。走林间小道。我知道一条近路，可以绕过王室直辖领地的哨卡。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你对逃跑这件事……似乎很有经验。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "这不是我第一次从王都逃出来。"

    "她的语气很平淡，但你能听出其中的苦涩。"

    hide elena_img with dissolve

    $ hide_all_chars()
    "逃亡的路上，你回头望了一眼灯火通明的王都。"

    "城墙上的信号火在跳动，像一只巨大的眼睛在黑暗中注视着你。"

    "你知道，下次再来这里，要么是凯旋，要么是以囚犯的身份。"

    "你活着离开了。"

    jump ch4_end

    ## ============================================================
    ## 场景5d：背叛的aftermath
    ## ============================================================

label ch4_aftermath:

    if prince_betrayed:
        $ play_music("audio/music/great_hall.ogg", fadein=2.0)
        scene bg throne_room with dissolve
        $ unlock_gallery("bg_throne_room")

        "王后在王座大厅召见了你。"

        "这一次，大厅里只有你和她。连侍从都被屏退了。"

        $ hide_all_chars("queen_img")
        show queen_img at left with dissolve

        queen "你做得很好。"

        "她的语气和昨天判若两人——少了威严，多了一丝……亲近？"

        queen "在你之前，已经有三个领主向我报告过弗雷德里克的异动。但只有你——"

        queen "只有你提供了最详细、最有用的情报。"

        queen "作为奖赏，我免除艾登堡三年的税赋。"

        $ change_stat("wealth", 30)
        $ change_rel("rel_queen", 20)

        queen "另外，你在北方监视男爵的任务——我会额外拨付两千金币作为经费。"

        queen "记住，忠诚的人会得到回报。"

        $ hide_all_chars()
        "你跪下谢恩。王后的赏赐丰厚得超出了你的预期。"

        "但你心里清楚——这份丰厚的赏赐，是用一个年轻人的自由换来的。"

        hide queen_img with dissolve

        "走出大殿时，你经过了通往地牢的走廊。"

        "那里——两个近卫正押着一个人走下台阶。"

        "是弗雷德里克。"

        "他的手铐在昏暗的灯光下发出冷冽的金属光泽。"

        "他看到了你。"

        "他的眼里满是不可置信。然后——那不可置信变成了一种深沉的、无法言喻的悲伤。"

        "他没有说话。只是慢慢地摇了摇头。"

        "然后，他被押进了地牢的阴影中。"

        "你站在走廊里，很久很久没有动。"

        "你告诉自己：这是正确的选择。这是唯一的选择。"

        "但你知道——弗雷德里克的那个眼神，会跟随你很久很久。"

    else:
        $ play_music("audio/music/tension.ogg", fadein=2.0)
        scene bg royal_palace with dissolve
        $ unlock_gallery("bg_royal_palace")

        "王子的事件让整个王都人心惶惶。"

        "街道上的巡逻队增加了三倍。贵宾馆里的领主们个个如坐针毡。"

        "没有人知道接下来会发生什么——王后会不会扩大清洗的范围？"

        "你在忐忑中度过了三天。"

        "期间，你尽量保持低调——不见客、不出门、只在房间里等消息。"

        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve

        elena "戒严解除了。城门重新开放。"

        elena "你被允许离开。但我建议你——走得快一点。"

        hide elena_img with dissolve

        $ hide_all_chars()
        "你被允许在戒严解除后离开。但这次经历让你对王都的权力游戏有了更深的认识。"

        "王都的权力没有游戏的规则。走进去的人，很少能全身而退。"

    jump ch4_end

    ## ============================================================
    ## 第四章结尾
    ## ============================================================

label ch4_end:

    $ clamp_stats()
    $ check_max_stat()
    $ persistent.chapters_completed.add("chapter4")

    ## 章节结束统计
    call show_chapter_summary("第四章", "王都风云") from _call_show_chapter_summary_2

    $ play_music("audio/music/sad.ogg", fadein=2.0)
    scene black with dissolve
    $ set_mood("sad")

    "你回到了艾登堡。"

    "五天的归途，比来时漫长了十倍。"

    "一路上，你一直在想——自己做的选择究竟是对还是错。"

    "每一次闭上眼睛，你都会看到王都的画面——"

    "王后冰冷的目光。"

    "王子月光下的身影。"

    "艾琳娜眼底的柔软。"

    "地牢里阴暗的火把。"

    "这些画面交织在一起，像一张越收越紧的网。"

    "权力的游戏没有对错。只有赢家和输家。"

    "——你的父亲也这么想过吗？在他生命的最后，他是否也曾怀疑过自己的选择？"

    scene bg castle_exterior with dissolve
    $ unlock_gallery("bg_castle_exterior")

    "艾登堡的城墙出现在地平线上时，你的心终于安定了一些。"

    "不管外面的世界如何天翻地覆——这里是你的家，你的领地，你的责任。"

    $ play_sound("audio/sfx/horse_gallop.ogg")

    "当你策马穿过城门时，城墙上的守卫认出了你，欢呼声此起彼伏。"

    "城里的百姓听到消息，纷纷涌上街头。他们的脸上带着如释重负的笑容——领主回来了，一切就会没事的。"

    "你不确定一切是否真的会没事。但你对他们微笑着点头，因为他们需要这份安心。"

    scene bg great_hall with dissolve
    $ unlock_gallery("bg_great_hall")

    "你来不及换下旅途的衣服，就被请到了大厅。"

    "你不在的这些天，积攒了一摞需要处理的文件。税务报告、巡逻记录、商队的通行许可……"

    "但这些现在都不重要了。"

    ## ── 主教马修斯：遗诏证据交接 ──
    if true_killer_known:
        "你刚踏进城门，就看到一个意想不到的人在等着你。"

        $ hide_all_chars("bishop_img")
        show bishop_img at left with dissolve

        bishop "领主大人……您终于回来了。"

        "马修斯主教站在教堂门前，脸色苍白，眼窝深陷。显然这些天他也没怎么休息过。"

        hide bishop_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "主教？你怎么在这里等我？"

        hide player_char_img
        $ hide_all_chars("bishop_img")
        show bishop_img at left with dissolve

        if testament_original_obtained:
            bishop "您去王都的这些天，有人来翻查过教堂的档案室。"

            bishop "他们没找到遗诏——多亏您之前就带走了。但这说明有人在追查。"

            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你没事吧？"

            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "暂时没事。但我想告诉您——您手上那份遗诏是真的。如果需要，我愿意在任何人面前作证。"

            bishop "因为您的父亲也问过我同样的问题——「你为什么信任我？」"

            bishop "我的答案至今没变。"
        else:
            bishop "您去王都的这些天，我一直在想——关于那件事。"

            "他压低了声音，左右张望了一下。"

            bishop "那个……我答应您的东西。我想了很久，决定还是交给您保管比较安全。"

            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你是说——"

            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "先王的遗诏原本。"

            "他从教袍内层取出一个用蜡封密封的皮卷筒，双手颤抖着递过来。"

            bishop "这些年来我一直藏在教堂地窖的暗格里。但最近……有人开始翻查教堂的档案室。"

            bishop "我不知道是谁在找，但我不能冒这个险了。放在您手里，比放在我这里安全。"

            $ testament_original_obtained = True
            $ testament_from_bishop_hand = True

            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "为什么信任我？"

            "主教双手交握，指节微微发白。"

            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "因为您的父亲也问过我同样的问题。"

        bishop "他说：「马修斯，总有一天真相需要一个足够勇敢的人来揭开。」"

        bishop "二十年了。我每天都在向圣母忏悔。也许……是时候了。"

        hide bishop_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "主教，你会因为这件事受到牵连。"

        hide player_char_img
        $ hide_all_chars("bishop_img")
        show bishop_img at left with dissolve
        bishop "我知道。但继续沉默下去，我的灵魂会先于我的身体死去。"

        bishop "领主大人，不管您打算怎么使用这份遗诏——请答应我一件事。"

        bishop "让真相以最少的代价被揭开。这个国家已经流了太多血了。"

        hide bishop_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve

        ## 选择深度 pass R2 (2026-06-16): 补"与教会结盟"选择, 激活此前从不置真的死 flag alliance_church
        ## (被 ch5_exp 圣盾阵 / interludes / npc_depth 读 ~10 处, 之前全是死分支)。
        ## 隐藏/延迟代价: 教会(费雷恩)本是杀父共犯, 结盟=接住这笔旧账(ch5 真相时兑现); 且与暗百合互斥。
        menu:
            "请教会公开站到你这边——与马修斯结盟" if faith >= 40 and not lily_full_member:
                $ alliance_church = True
                $ change_rel("rel_bishop", 10)
                $ change_stat("faith", 6)
                player "马修斯，光有一份遗诏不够。我要教会公开站到我这边。"
                hide player_char_img
                $ hide_all_chars("bishop_img")
                show bishop_img at left with dissolve
                bishop "……好。教会与您同进退。"
                bishop "但有句话得说在前头——教会站出来，不只是为您，也是替费雷恩还债。"
                bishop "您接住教会的支持，也就接住了这笔二十年的旧账。它干净不到哪里去。"
                hide bishop_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "我接。"
                $ hide_all_chars()
                if dark_lily_joined:
                    $ change_rel("rel_lily", -15)
                    "话出口时你想起影卫。圣母教会和暗百合是不共戴天的两家——你这一步，影迟早会知道。"
                else:
                    "你点了头。这个盟友手上沾着你父亲的血——眼下你还顾不上跟它算这笔账。"
            "心领，但不结盟——只留马修斯一个人证":
                player "我会的。谢谢你，马修斯。教会就别牵涉进来了——你一个人作证，已经够危险。"
                $ hide_all_chars()
                "马修斯松了口气，肩膀塌下去一点，没再坚持。"
                "教会不出面，意味着圣母会的名号、它能动员的虔诚领主、它替你呼吁停火的分量——这些你都用不上了。真打起来，你手里只剩自己这点人马。"

        $ hide_all_chars()
        "你把皮卷筒贴身藏好。这薄薄的一卷羊皮纸——比任何武器都更具有毁灭性的力量。"

        "你现在手中握着的，是能够颠覆整个王国的真相。"

        $ change_rel("rel_bishop", 15)

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "领主大人，您回来了。"

    $ hide_all_chars()
    "老骑士的脸上有一丝藏得很深的担忧——你不在的这些天，他一定没有睡好。"

    "他的眼袋更深了，鬓角似乎又白了几缕。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "王都的事……我都听说了。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "消息传得倒是快。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "这种事情，瞒不住的。信鸽比马跑得快。"

    if prince_ally and not prince_betrayed:
        aldric "王子被捕的消息传遍了整个王国。各地领主人心浮动。"
        aldric "有人说这是王后的阴谋，有人说王子确实在密谋造反。"
        aldric "但所有人都注意到了一件事——"
        aldric "艾登堡的领主在事发前后离开了王都。"
        aldric "这说明什么？有人觉得你是同谋，有人觉得你足够聪明。"

    if prince_betrayed:
        aldric "您向王后告密的事……也传出来了。"
        aldric "有些领主对您颇有微词。但也有人说您做了正确的选择。"
        aldric "无论如何，您现在是王后的人了。这条路，走到底就是荣华富贵，走错一步就是万劫不复。"

    if elena_romance:
        aldric "还有……"
        "老骑士看了一眼站在你身后的艾琳娜。"
        aldric "我注意到你和艾琳娜小姐之间的关系似乎……有了变化。"
        aldric "老臣多嘴一句——在权力的游戏中，感情是最大的弱点。"
        aldric "但也是最强的铠甲。"
        aldric "看你怎么用了。"
    else:
        aldric "还有——你身边那位艾琳娜小姐。"
        aldric "她是个能干的人，但别忘了她的过去。信任要给，但要留三分。"

    "他走到窗前，看着远处的天空。几只乌鸦掠过城堡上方，叫声嘶哑。"

    aldric "外面的世界变了。各地领主开始选边站。"

    aldric "有人支持王后，有人暗中支持王子。"

    aldric "还有一些人——他们两边都不站，只想在乱局中捞好处。"

    aldric "而所有人都在看着艾登堡。看着你。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "为什么？"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "因为你去了一趟王都，见了王后，见了王子——然后活着回来了。"

    aldric "在如今的局势下，活着从王都回来本身就是一种能力的证明。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "因为我们掌握着真相。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "真相是最危险的武器，领主大人。"

    aldric "它可以推翻王朝，也可以让持有它的人粉身碎骨。"

    aldric "问题是——您准备好用它了吗？"

    hide aldric_img with dissolve

    "你站在大厅的窗前，看着夕阳在远处的山脊上缓缓沉没。"

    show elena_img at right with dissolve

    if elena_romance:
        "艾琳娜走到你身边，安静地站着。她的手轻轻碰了碰你的手指。"
    else:
        "艾琳娜走到你身边，双手抱臂，和你一起看着窗外。"

    elena "想什么呢？"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "在想……从现在开始，每走一步都可能是最后一步。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "那就让每一步都值得。"

    hide elena_img with dissolve

    scene bg study with dissolve
    $ unlock_gallery("bg_study")

    "入夜。你回到书房，铺开地图。"

    "在地图上，你用墨笔标注了几个关键的位置——"

    if dark_lily_destroyed:
        "王都。男爵的领地。教会的据点。"
    else:
        "王都。男爵的领地。教会的据点。暗百合可能的藏身处。"

    "还有，最重要的——艾登堡。"

    "它就在所有势力的交汇点上，像一枚被放在棋盘中央的棋子。"

    "你的手指在地图上缓缓移动，最终停在了艾登堡的标记上。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "父亲……你当年是不是也坐在这里，看着同样的地图，思考着同样的问题？"

    $ hide_all_chars()
    "没有人回答你。窗外有风刮过城墙的垛口，发出低沉的呜咽声。"

    $ play_sound("audio/sfx/fire_crackle.ogg")

    "你拿起笔，在地图的空白处写下了一行字——"

    "「无论如何，保护艾登堡的百姓。」"

    "这是你给自己的底线。"

    "不管接下来的风暴有多猛烈，这条底线不能突破。"

    scene black with dissolve

    "窗外，北风呼啸而起。"

    "冬天就要过去了。"

    "但真正的严寒——不在天上，在人心里。"

    "风暴即将来临。"

    if dark_lily_destroyed:
        "北方的男爵在磨刀。王都的王后在收网。"
    else:
        "北方的男爵在磨刀。王都的王后在收网。暗百合在暗处注视着一切。"

    "而你——站在所有力量的交汇点上，手握着能改变一切的真相。"

    "你必须做好最后的准备。"

    "因为接下来——"

    "你将做出一生中最重要的决定。"

    scene black with dissolve

    $ renpy.force_autosave()

    jump chapter5_start


label ch4_rescue_partial_recovery:
    ## fail 路径: 玩家撤回艾登堡, 几日后通过暗线汇合王子
    scene black with dissolve
    $ play_music("audio/music/dawn_after_storm.ogg", fadein=2.0)

    "三天后，艾登堡。"

    scene bg bedroom with dissolve
    $ unlock_gallery("bg_bedroom")
    $ set_mood("mystery")

    "雷恩躺在城堡西厢的客房里。"
    "肩上的伤被城里的医师缝了十二针——医师说不会断臂，但持剑得养上一两个月。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "（声音哑）领主大人……是我没顶住那一刻。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你顶住了。我们都活着回来了。"
    player "下一次找王子，不会再让你冲在前面。"

    hide player_char_img with dissolve
    $ hide_all_chars()

    "你走出客房。雷恩没接你那句话——你也知道他下次还是会冲在前面。"

    "第五天的傍晚，艾琳娜来了。"

    scene bg study with dissolve
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "我的人在王宫底层有一条线。"

    elena "王子被转下三层之后，第二天晚上，牢门是从里面打开的。"

    elena "守卫的尸体被人挪走了，没留血痕。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "王宫里，有人不愿意他干干净净地死掉。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "王后想留个干净的故事——「王子病死狱中」。"
    elena "可她底下的人，不是每一个都愿意背这个故事。"

    elena "王子现在在艾登堡西边的一片山林里。一个人。我们的人在远处看着他，没靠近。"

    elena "他在等你。"

    hide elena_img with dissolve

    ## ── 森林边缘汇合 ──
    scene bg forest_path with dissolve
    $ unlock_gallery("bg_forest_path")
    $ set_weather("fog", "light")

    "第六天，黎明前。"

    "你和雷恩——他左臂还吊着布带——骑马到了那片山林的边缘。"

    "树影里站着一个瘦了一圈的人。"
    "华贵的衣服没了，换的是粗布外袍。脸上的肿消了，但嘴角的伤痂还在。"

    $ hide_all_chars("prince_img")
    show prince_img at left with dissolve
    prince "你来了……"
    prince "我以为你不会来了。"

    hide prince_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我答应过的事不会食言。只是来晚了。"

    hide player_char_img
    $ hide_all_chars("prince_img")
    show prince_img at left with dissolve
    prince "牢里那一夜——铁门是从外面被人撬开的。我没看清那人的脸。"
    prince "他没说话。只是把镣铐砸开，给了我一袋干粮和一把短剑，然后就走了。"

    prince "我现在还不知道，那是谁的人。"

    hide prince_img with dissolve
    $ hide_all_chars()
    "你心里多了一根刺。"
    "在王宫里，不只有想杀你的人。还有想留你一条命的人——而那个人，你现在还不知道是谁。"

    "你扶王子上马。雷恩的左臂用不上，但他能用右手牵两匹缰绳。"

    "三个人，两匹半马，在雾里掉头，朝艾登堡走。"

    $ log_decision("第四章", "潜入失败, 王子被神秘人放出, 三人森林汇合")

    jump ch4_rescue_aftermath

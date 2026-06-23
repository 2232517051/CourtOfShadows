## ============================================================
## 第五章：最终决战
## ============================================================

label chapter5_start:

    ## 安全重置：防止上一章过场动画的 _dismiss_pause 泄漏
    $ _dismiss_pause = True
    $ quick_menu = True
    window auto

    $ renpy.force_autosave()
    $ snapshot_chapter_start()
    scene black with fade

    call show_chapter("第五章", "最终决战", "一切的终章") from _call_show_chapter_3
    call show_recap("chapter4") from _call_show_recap_3
    call apply_rel_chapter_effects from _call_rel_ch5

    ## 章节过场动画
    call cinematic_chapter5 from _call_cinematic_ch5

    ## 章节间过渡：归乡之路 + 紧急会议
    call interlude_ch4_ch5_council from _call_interlude45_council
    call interlude_ch4_ch5 from _call_interlude45

    ## 章节间过渡: 老朋友回归 (2026-05-17 dccdfrsx 反馈新增)
    ## 马库斯/卡尔在战前最后给玩家一次出场, 回收伏笔
    call interlude_ch4_ch5_old_friend from _call_interlude45_friend

    ## 章节深化：逃兵的故事
    call ch5_deep_deserter from _call_ch5_ddeserter

    ## 治理系统：建设 / 丰收祭（如果达标）
    call gov_building from _call_gov_build5
    if governance_prosperity >= 60:
        call gov_festival from _call_gov_fest5

    ## 治理报告
    call gov_report from _call_gov_rep5

    "开春了。冰雪消融，但空气中弥漫着战争的气息。"

    "王后以「镇压叛乱」为由，集结了王室军队，准备清洗不服从的领主。"

    "冯·哈根男爵则联合了北方诸侯，公然举旗反叛。"

    "而你，站在两股势力的交汇点上，手握着足以改变一切的真相。"

    ## ============================================================
    ## 战争阴云
    ## ============================================================

label ch5_war_clouds:

    $ play_music("audio/music/tension.ogg", fadein=2.0)
    scene bg castle_exterior with dissolve
    $ unlock_gallery("bg_castle_exterior")
    $ set_mood("tense")
    $ set_weather("fog", "normal")

    $ trigger_random_event("rest")

    "三月初春的早晨，艾登堡的城墙上结着一层薄霜。"

    "你站在城垛上，远眺北方的地平线。那里有隐约的烟尘——那是军队行进的痕迹。"

    "一名骑兵从远处疾驰而来，马蹄声在清晨的空气中格外清晰。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    $ unlock_gallery("captain")

    captain "领主大人！前方斥候回报！"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "说。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "王后的军队已经从王都出发，约三千人，沿着南方官道北上。"

    captain "男爵的联军也在集结，估计有两千五百人，正从北方的格鲁瓦尔德堡向南推进。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "两支大军……我们正好在中间。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "是的。按目前的行军速度，他们将在十天后在艾登堡以北的平原交战。"

    captain "而我们的领地，正好在两军的必经之路上。"

    menu:
        "立即派出更多斥候，密切监视双方动向":
            $ change_stat("intrigue", 3)
            $ change_stat("power", -8)
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "雷恩，把所有能派出去的斥候都派出去。我要知道他们每一步的动向。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "明白！我立刻安排。"
            "你的斥候网络在接下来的日子里不断传回情报，让你对战局有了清晰的了解。"
            captain "斥候全撒出去了，城头能巡墙的人就薄了。这几天我们看得清敌人，却也最经不起一支奇兵。"

        "加强城防，做好防御准备":
            $ change_stat("power", 3)
            $ change_stat("wealth", -12)
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "不管谁来，我们先确保艾登堡安全。加固城墙，储备滚石和火油。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "遵命！我已经命人检查了所有防御工事，还有几处需要修缮。"
            "城墙上的守军增加了一倍，每个箭垛都配备了弓手。账房的开支也跟着翻了一番——火油、滚石、加饷，库银肉眼可见地往下掉。"

        "先确保百姓安全，疏散村庄":
            $ change_stat("loyalty", 3)
            $ change_stat("wealth", -12)
            $ change_stat("intrigue", -8)
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "百姓的安全是第一位的。通知所有城外的村庄，让他们带上粮食和牲畜进城。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "领主大人仁慈。我这就安排。"
            "接下来几天，源源不断的村民涌入艾登堡，城内很快变得拥挤起来。"
            "粮仓的存粮按人头一算，原本能撑两个月，如今怕是连一个月都难。混在难民里的生面孔太多，谁是逃命的、谁是来探路的，一时也理不清。"

    hide captain_img with dissolve

    scene bg great_hall with dissolve
    $ unlock_gallery("bg_great_hall")

    "你回到大厅时，几名领民代表已经等在那里了。"

    "一个白发苍苍的老农跪在地上，身体在发抖。"

    $ hide_all_chars("farmer_rep_img")
    show farmer_rep_img at left with dissolve
    old_farmer "领主大人！求您救救我们啊！北边的村子说看到了军队的旗帜！"

    old_farmer "上次打仗的时候，我还是个孩子……那些兵就像蝗虫一样，抢走了一切……"

    $ hide_all_chars()
    "一个年轻的铁匠站出来，眼中带着愤怒。"

    $ hide_all_chars("soldier_generic_img")
    show soldier_generic_img at left with dissolve
    young_blacksmith "领主大人，让我们拿起武器吧！我们愿意为保卫家园而战！"

    $ hide_all_chars()
    "旁边的一个妇人紧紧抱着孩子，泪水无声地流淌。"

    $ hide_all_chars("blacksmith_wife_img")
    show blacksmith_wife_img at left with dissolve
    woman_refugee "大人……我丈夫去年冬天病死了……只剩我和孩子……我们能去哪里呢……"

    "你看着这些惶恐的面孔，肩膀沉了下去——铠甲好像比早上重了几斤。"

    menu:
        "向他们承诺会保护所有人":
            $ change_stat("loyalty", 5)
            $ change_stat("reputation", 3)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我向你们发誓——只要我还站在这里，就不会让任何人伤害你们。"
            player "艾登堡的城墙会保护每一个人。"
            $ hide_all_chars()
            "老农泪流满面地磕头。铁匠挺起了胸膛。妇人紧紧地抱着孩子，终于不再颤抖。"
            "你的承诺像一颗石子投入湖面，在民间荡起了层层涟漪。人们开始称你为「守护者」。"
            "你把话说满了。从这一刻起，任何一条留给自己的退路、任何一次见势不妙的撤退，都会变成背弃。你给了他们一个守护者，也给自己套上了一根再不能松开的链子。"
            $ change_stat("reputation", 2)
            $ change_stat("intrigue", -8)

        "坦率地告知形势严峻":
            $ change_stat("reputation", 2)
            $ change_stat("intrigue", 2)
            $ change_stat("loyalty", -6)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我不会欺骗你们。形势确实严峻。但我也不会坐以待毙。"
            player "我需要你们的合作——能拿武器的，协助守城。老弱妇孺，在城堡里避难。"
            player "大家齐心协力，我们才能撑过去。"
            "人们脸上的恐惧没散。多数人点了头——也有几家当天夜里就收拾了细软，赶在城门落锁前出了城。"
            "留下来的人信你。可城里少了几十张面孔。"

        "用强硬的语气让他们冷静下来":
            $ change_stat("power", 3)
            $ change_stat("loyalty", -10)
            $ harsh_with_refugees = True
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "都给我冷静！恐慌解决不了任何问题！"
            player "回去做好你们的本职工作。守城的事，交给我和士兵。"
            $ hide_all_chars()
            "人群安静了下来。有些人被你的威严震住，有些人则面露不安。"
            "人群散了。铁匠没再开口，只是攥紧了拳头走在最后。"

    "领民们退下之后，大厅里只剩下你和几个亲信。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    $ unlock_gallery("aldric")

    aldric "领主大人，我在整理库房时发现了一些东西。"

    aldric "是老领主——您父亲当年留下的军事笔记。"

    aldric "里面详细记录了艾登堡周围的地形，以及几条隐蔽的行军路线。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "父亲……"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "老领主虽然不善征战，但他是个极其细心的人。"

    aldric "他似乎早就预料到了有一天会发生战争。"

    menu:
        "仔细研读父亲的笔记":
            $ change_stat("intrigue", 3)
            $ change_stat("power", 2)
            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "把笔记给我。我要仔细研究。"
            $ hide_all_chars()
            "你花了一整夜研读父亲的笔记。字迹工整，条理清晰——你仿佛看到了一个从未了解过的父亲。"
            "笔记中标注了三条从艾登堡通往北方森林的隐蔽小道，以及河流在春季涨水时的通行情况。"
            "这些信息在即将到来的战争中可能至关重要。"

        "感慨地收起笔记":
            $ change_stat("loyalty", 2)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "父亲……即使在天上，也在守护着我们。"
            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "老领主一定在看着您，为您骄傲。"
            "你将笔记小心地收起，决定在需要时再仔细研读。"

    hide aldric_img with dissolve

    "接下来的几天，更多的消息不断传来。"

    scene bg study with dissolve
    $ unlock_gallery("bg_study")

    "你在书房里展开地图，上面标满了两军的位置和行进路线。"

    if spy_network:
        "你的间谍网络不断传回新的情报，让你对双方的一举一动了如指掌。"

        "一封密信被悄悄送到你的书桌上——来自你安插在王后军中的细作。"

        "密信中写道：「王后军中士气不高。许多士兵是被强征入伍的农民。」"

        "「王后的亲信将领蒙塔古伯爵与军中其他将领有嫌隙。」"

        "「此外，王后军的粮草补给线过长，一旦被切断，最多支撑七天。」"

        $ change_stat("intrigue", 3)
    else:
        "你派出的斥候陆续回营，带来了零星但有用的消息。"

        "奥尔德里克根据这些碎片般的情报，凭借多年的军事经验在地图上标出了几处关键节点。"

        $ hide_all_chars("aldric_img")
        show aldric_img at left with dissolve
        aldric "这里、这里、还有这里——地形狭窄，适合伏击。王后军人多，但地利在我们这边。"
        hide aldric_img with dissolve

        $ hide_all_chars()
        "没有间谍网络的精准情报，你只能依靠老兵的直觉和地形的优势。但有时候，经验比情报更可靠。"

    "你的手指在地图上缓缓移动，仿佛在下一盘巨大的棋局。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    $ unlock_gallery("elena")

    elena "你在想什么？"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "在想这场战争中，每个人的位置。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "不只是地图上的位置吧？"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你说得对。还有立场。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    if dark_lily_destroyed:
        elena "王后、男爵、教会……每个人都有自己的算盘。"
    else:
        elena "王后、男爵、教会、暗百合……每个人都有自己的算盘。"

    if elena_romance:
        elena "但你不一样。你是唯一一个还在乎「对错」的人。"
        elena "这既是你的弱点，也是你的力量。"
        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "听起来像是在夸我。"
        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "也许吧。"
        "她低下头笑了一声，没出声。"
    else:
        elena "你已经想好站在哪一边了吗？"
        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "还没有。但很快就必须做出决定了。"
        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "无论你怎么选，都会有人不满意。"
        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "我知道。但我不能什么都不做。"

    hide elena_img with dissolve

    $ hide_all_chars()
    "窗外，一只信鸽扑棱着翅膀落在窗台上。"

    "你取下它脚上绑着的纸卷。"

    $ hide_all_chars("baron_img")
    show baron_img angry at left with dissolve
    $ unlock_gallery("baron")

    "信是男爵写的。"

    baron "致艾登堡领主：战争在即，你必须选边。中立者的下场比敌人更惨。给你三天时间。——冯·哈根"

    hide baron_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "……"

    "你将信纸放在烛火旁，看着火舌吞噬了那些威胁性的文字。"

    hide baron_img with dissolve

    $ hide_all_chars()
    "几乎同时，一名王室使者也到达了艾登堡。"

    $ hide_all_chars("queen_img")
    show queen_img angry at left with dissolve
    $ unlock_gallery("queen")

    queen "王后陛下致艾登堡领主：王室需要你的忠诚。在即将到来的战争中站在正义的一方，否则你将被视为叛逆。"

    hide queen_img with dissolve

    $ hide_all_chars()
    "两封信，两个威胁。你被夹在中间，进退维谷。"

    "但你心里清楚。这不是站谁那边的事，是你想成为什么样的人。"

    ## ============================================================
    ## 各方动向
    ## ============================================================

label ch5_factions_move:

    scene bg study with dissolve
    $ unlock_gallery("bg_study")

    "接下来的三天里，你收到了大量情报。"

    "每一条消息都像是拼图的一块——慢慢拼凑出这场即将到来的大战的全貌。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve

    elena "让我把目前掌握的情况做个总结。"

    elena "王后方面——她的三千大军由蒙塔古伯爵统领，沿南方官道北上。"

    elena "但军中士气不高。许多士兵是被强征入伍的农民，对这场「平叛」战争毫无热情。"

    elena "蒙塔古伯爵本人是个老派军人，作战风格保守但稳健。"

    elena "他和王后之间似乎也有分歧——他主张谈判，王后坚持武力。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "男爵那边呢？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "男爵联军大约两千五百人，以北方骑兵为主。"

    elena "核心力量是男爵自己的八百铁骑——这是整个北方最精锐的骑兵部队。"

    elena "但联军的问题在于指挥系统混乱。五个领主各有各的想法，男爵很难统一号令。"

    elena "尤其是西北的维克托领主和东边的加斯帕领主，他们是被迫加入的。"

    elena "如果战局不利，他们随时可能倒戈。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "教会呢？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "教会表面上保持中立，但主教马修斯已经暗中联络了教廷。"

    elena "教廷的态度很微妙——他们不希望任何一方获得压倒性的胜利。"

    elena "一个分裂的王国更有利于教会扩大影响力。"

    if dark_lily_joined:
        elena "至于暗百合——首领已经在两军中都安插了人手。"
        elena "他们不会主动参战，但会在关键时刻影响局势。"
        elena "首领让我转告你——「棋局已经摆好，就等你下第一步棋了。」"
    else:
        elena "另外，我自己的消息渠道也传来了一些有用的东西。"
        elena "王后军中有几个中层军官对这场仗心存抵触——他们私下抱怨这是「贵族的权力游戏」。"
        elena "如果局势僵持，这些人未必会死战到底。"

    hide elena_img with dissolve

    "你站在地图前，手指缓缓划过每一个标记。"

    if dark_lily_destroyed:
        "王后军从南面来，男爵联军从北面来。教会在观望。"
    else:
        $ hide_all_chars()
        "王后军从南面来，男爵联军从北面来。教会在观望，暗百合在暗处。"

    "而你——站在所有力量的交汇点上。"

    "不知不觉间，你已经成为了这盘棋上最关键的一颗棋子。"

    scene bg castle_exterior with dissolve
    $ unlock_gallery("bg_castle_exterior")

    "第二天一早，城门外来了一支小规模的队伍。"

    "他们衣衫褴褛，满身泥泞，看起来已经赶了很远的路。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "领主大人，是从北方逃来的难民。大约五十人。"

    captain "他们说男爵的军队经过他们的村庄时，强征了所有的粮食和壮丁。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "让他们进来。安排食物和住所。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "是。但是领主大人，如果难民继续增加——"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "那就继续收容。直到城里再也容不下为止。"

    hide captain_img with dissolve

    $ hide_all_chars()
    "难民中有一个老人，自称是北方一个小领地的退休管家。"

    "他带来了一个重要的消息——"

    $ hide_all_chars("servant_generic_img")
    show servant_generic_img at left with dissolve
    retired_steward "领主大人，我在来的路上亲眼看到了男爵的军队。"

    retired_steward "他们的骑兵确实强大，但步兵的装备很差。很多人连像样的铠甲都没有。"

    retired_steward "另外，男爵军的粮草辎重走的是另一条路——沿着河谷的小道。"

    retired_steward "只有不到一百人护送。如果有人切断那条补给线……"

    menu:
        "记下这个情报，留待日后使用":
            $ change_stat("intrigue", 3)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "谢谢你的消息。你会得到妥善的安置。"
            "你把这个情报默默记在心里。河谷、小道、不足百人——大致的轮廓有了，可老人没说清具体在哪一段下手。真要用，还得另寻门路。"

        "追问更多细节":
            $ change_stat("intrigue", 3)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "那条河谷小道的具体位置在哪里？护卫部队有多少人？都是什么编制？"
            $ hide_all_chars()
            $ hide_all_chars("servant_generic_img")
            show servant_generic_img at left with dissolve
            retired_steward "老朽记性不太好了……但大致的位置我可以在地图上指出来。"
            "你把老人带到书房，在地图上标注了男爵军补给线的位置。"
            "这条信息可能在关键时刻改变战局。"
            $ baron_supply_intel = True
            "你把老人留在书房，对着地图问了整整一个上午。等标完那条河谷小道，难民安置、城防部署都得往后挪一挪——但这条线的位置，你算是吃进肚里了。"

        "不太在意这些细节":
            $ change_stat("loyalty", -7)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "好的，辛苦了。去休息吧。"
            $ hide_all_chars()
            "老人愣了一下，慢慢退了出去。门口几个跟着难民进城的人把这一幕看在眼里——他们走了几十里来投奔你，换来的是一句『去休息吧』。这种事，传得比情报快。"

    "时间一天天过去。空气中的紧张气氛越来越浓。"

    scene bg great_hall with dissolve
    $ unlock_gallery("bg_great_hall")

    "又一个清晨，你在大厅里接见了一位意外的来客。"

    "一个穿着华丽斗篷的中年人，自称是王后的特使。"

    $ hide_all_chars("queen_envoy_img")
    show queen_envoy_img at left with dissolve
    queen_envoy "领主大人，王后陛下派我来传达她的最后提议。"

    queen_envoy "如果您愿意在即将到来的战争中支持王室——"

    queen_envoy "王后承诺战后封您为侯爵，并将北方三个领地的管辖权交给您。"

    queen_envoy "此外，王室将免除艾登堡未来五年的赋税。"

    menu:
        "表示会认真考虑":
            $ change_rel("rel_queen", 8)
            $ change_stat("reputation", -3)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "这是一个很有诚意的提议。请转告王后陛下，我需要时间考虑。"
            $ hide_all_chars()
            $ hide_all_chars("queen_envoy_img")
            show queen_envoy_img at left with dissolve
            queen_envoy "当然。但请不要等太久——时间不站在任何人这边。"
            "特使走后，你把这个提议压在了心里。门外几个老臣交换了眼神——领主对王室留了一道门，这事天黑前就会传遍内城。"

        "委婉拒绝":
            $ change_stat("reputation", 2)
            $ change_rel("rel_queen", -8)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "请转告王后陛下，艾登堡珍视与王室的关系。"
            player "但在这种敏感时期，我需要先确保我领地百姓的安全。"
            $ hide_all_chars("queen_envoy_img")
            show queen_envoy_img at left with dissolve
            queen_envoy "……我明白了。希望您不会后悔这个决定。"
            "他没有再多说，但你听得出——「百姓的安全」这四个字，在王后耳朵里和「拒绝」是同一个意思。"

        "直接拒绝":
            $ change_stat("power", 2)
            $ change_rel("rel_queen", -15)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "回去告诉王后——我不是用爵位和金钱可以收买的。"
            $ hide_all_chars("queen_envoy_img")
            show queen_envoy_img at left with dissolve
            queen_envoy "领主大人，这恐怕不是一个明智的——"
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "送客。"
            $ hide_all_chars()
            "特使面色铁青地离开了。你很清楚——从今往后，王后那扇门对你彻底关上了。你不在乎，至少现在不在乎。"

    "特使离开后不到两个时辰，又有一个人来了——"

    "这次是男爵的密使。他不像王后的特使那样大张旗鼓，而是悄悄从后门进来的。"

    $ hide_all_chars("servant_generic_img")
    show servant_generic_img at left with dissolve
    baron_envoy "领主大人，男爵阁下让我转达——"

    baron_envoy "如果您加入联军，男爵承诺事成之后与您平分北方的权力。"

    baron_envoy "您将成为男爵之下、万人之上的人物。"

    menu:
        "当面拒绝并让卫兵把他赶出去" if power >= 50:
            $ change_stat("power", 5)
            $ change_stat("reputation", 3)
            $ change_rel("rel_baron", -10)
            $ ch5_baron_envoy_ejected = True

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "雷恩，把他送出去。不必客套，走快一点。"

            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "明白。"

            $ hide_all_chars()
            "雷恩没让密使走完三步，直接把他往门口架。密使想回头说话，但已经过了大殿门。"

            "你回到桌前。这事会传回男爵那里，三天之内。"

            "密使的马刚出城门，你已经在传令雷恩加固北墙。"

        "表示会认真考虑":
            $ change_stat("intrigue", 2)
            $ change_rel("rel_queen", -8)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "告诉男爵，我需要时间。"
            $ hide_all_chars("servant_generic_img")
            show servant_generic_img at left with dissolve
            baron_envoy "男爵给您三天时间。三天之后如果没有回复——他会把您视为敌人。"
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我听到了。"
            $ hide_all_chars()
            "拖一手有拖一手的代价。密使前脚出门，王后那边的眼线后脚就把消息递了回去——艾登堡的领主在两头之间留着话口子，谁也没回绝。王后不喜欢这种人。"

        "委婉拒绝":
            $ change_stat("reputation", -3)
            $ change_rel("rel_baron", 6)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "感谢男爵的好意。但我有自己的考量。"
            $ hide_all_chars("servant_generic_img")
            show servant_generic_img at left with dissolve
            baron_envoy "……男爵不会高兴的。"
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "请转达我的敬意。"
            $ hide_all_chars()
            "你给密使留了体面，也给自己留了退路。可城里那些等着看领主硬气一回的人，这回什么都没等到——你既没把男爵的人轰出去，也没站到谁那边。一个没立场的领主，名声是攒不起来的。"

        "试图从密使那里套取更多情报":
            $ change_stat("intrigue", 4)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "男爵联军现在的情况怎么样？实力如何？"
            $ hide_all_chars("servant_generic_img")
            show servant_generic_img at left with dissolve
            baron_envoy "联军……实力很强。北方最精锐的骑兵都在我们这边。"
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "那后勤呢？粮草够吗？"
            "密使犹豫了一下。"
            $ hide_all_chars("servant_generic_img")
            show servant_generic_img at left with dissolve
            baron_envoy "……足够支撑整场战役。"
            "他说话时眼神闪烁——你知道他在撒谎。这证实了你之前得到的情报——男爵军的后勤确实是弱点。"
            $ baron_supply_intel = True

    "送走了男爵的密使后，你独自在书房里坐了很久。"

    "两边都在拉拢你，两边都在威胁你。"

    "你就像一根绷紧的弦——两头都有人在拉，稍有不慎就会断裂。"

    scene bg castle_exterior with dissolve
    $ unlock_gallery("bg_castle_exterior")

    "傍晚时分，你登上城楼，看着远方的地平线。"

    "北方的天空被夕阳染成了血红色。"

    "城墙下，新安置的难民正在排队领取食物。孩子们在空地上追逐嬉戏——对他们来说，这里比家更安全。"

    "一个小女孩跑到城墙下面，仰着头对你喊——"

    $ hide_all_chars("blacksmith_wife_img")
    show blacksmith_wife_img at left with dissolve
    little_girl "大人！大人！你会保护我们吗？"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "会的。"

    $ hide_all_chars()
    $ hide_all_chars("blacksmith_wife_img")
    show blacksmith_wife_img at left with dissolve
    little_girl "拉钩？"

    "你忍不住笑了。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "拉钩。"

    $ hide_all_chars()
    "小女孩满意地跑走了。她掉了一根头绳在地上——你弯腰捡起来，攥在手心里。决意更加坚定了。"

    "不管你最终选择什么路——有一件事是确定的。"

    "你要保护这些人。用你能想到的一切方式。"

    ## ============================================================
    ## 军事部署
    ## ============================================================

label ch5_military_deploy:

    $ play_music("audio/music/battle_prepare.ogg", fadein=2.0)
    scene bg great_hall with dissolve
    $ unlock_gallery("bg_great_hall")

    "战前的军事会议。"

    "地图铺在长桌上，桌上还散落着木制的兵棋——代表各方军队的位置。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "领主大人，让我汇报一下我们的军事准备情况。"

    captain "常备军方面，我们有两百名正规军。其中六十名重步兵，八十名轻步兵，四十名弓箭手，二十名骑兵。"

    if harsh_with_refugees:
        captain "民兵志愿者只来了二十几个。那天大厅里您发的那通火，传到村里就变了味——好些人觉得连您自己都没底，何必去送命。"
    else:
        captain "此外还有五十名民兵志愿者。他们的训练还不够充分，但保家卫国的热情很高。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "装备情况？"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "正规军的装备基本齐全。但民兵的装备比较简陋——大多只有皮甲和简单的武器。"

    if wealth >= 50:
        captain "不过，领主大人之前拨付的军费让我们采购了一批新的装备。"
        captain "至少每个人都有一件像样的铠甲和一把磨好的剑了。"
    else:
        captain "装备不足是我们最大的短板。不过铁匠们正在日夜赶工。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "城防呢？"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "城墙高三丈，厚一丈二。四座箭塔，每座配备五名弓手。"

    captain "城门加固了铁皮，还准备了滚石、火油和沸水。"

    captain "唯一的弱点是北墙——去年冬天的暴风雪损坏了一段，虽然修补了，但强度不如其他地方。"

    menu:
        "亲自指挥北墙改造——你要的是把它变成杀场" if power >= 70:
            $ change_stat("power", 5)
            $ change_stat("loyalty", 3)
            $ change_stat("intrigue", -10)
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "雷恩，跟我去北墙。我亲自盯三天。"
            player "石匠加固。陷阱布在内侧三十步。城上设三排弓手暗位，对准内侧死角——让北墙不只是难破， 是破了就死。"
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "……明白。亲自来盯， 工艺只会比我多想一倍。"
            $ hide_all_chars()
            "三天里你和士兵睡在城墙下。手上磨出两层老茧。但当北墙被加固到每块石都像是为攻城战量身定做时——士气也跟着起来了。"
            "走过来挑刺的老兵都摇头笑了一声。不只是力量本身——是力量摆出来的姿态。"
            "这三天你眼里只有那段墙。城里另外那些要你亲自过问的人和事，只能先搁着——奥德递进来的几张条子，你压根没翻。"

        "加强北墙的防御":
            $ change_stat("power", 3)
            $ change_stat("wealth", -8)
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "调更多人手去加固北墙。同时在北墙后面再建一道木栅栏作为第二道防线。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "好主意。多调人手、再添一道木栅，料和工钱我从账上支。"
            captain "省是省不下，但这道墙稳了。"
            "接下来两天，北墙的防御被大大加强了。"

        "在北墙设置陷阱":
            $ change_stat("intrigue", 3)
            $ change_stat("loyalty", -12)
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "不要修补北墙。让它看起来像是弱点。然后在城墙内侧设置陷阱。"
            player "如果敌人从北墙突破，正好落入我们的圈套。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "……是好计。可守北墙那批弟兄得知道，他们站的是请君入瓮的那道口子。"
            captain "我去跟他们说。这话不好开口。"
            "北墙成了陷阱。守在那儿的人嘴上不说，眼神里都明白自己站在哪。"

        "不做特别处理":
            $ change_stat("loyalty", -8)
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "北墙的情况暂时够用了。把精力放在其他方面。"
            "雷恩没接话，记下了，转身去安排别处。当晚换防的老兵里有人提了一句北墙，话没说完就被旁边的人用胳膊肘顶了回去。"

    hide captain_img with dissolve
    hide player_char_img

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "领主大人，关于物资储备的情况——"

    aldric "粮仓中的存粮可以供城内目前的人口食用约两个月。"

    aldric "如果继续有难民涌入，这个时间会缩短到一个月左右。"

    aldric "饮水方面，城堡内有两口深井，暂时不用担心。"

    aldric "药草和绷带的储备也比较充足——多亏了教会的援助。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "钱呢？"

    if wealth >= 60:
        hide player_char_img
        $ hide_all_chars("aldric_img")
        show aldric_img at left with dissolve
        aldric "金库充裕。足以支付士兵三个月的军饷，外加一些应急开支。"
    elif wealth >= 30:
        aldric "金库的情况中规中矩。大约可以维持两个月。"
    else:
        aldric "金库……有些紧张。一个月的军饷还是能付得起的。"

    menu:
        "拿一半金库银币给战死者家属预付抚恤金" if wealth >= 60:
            $ change_stat("wealth", -15)
            $ change_stat("loyalty", 10)
            $ change_stat("reputation", 5)
            $ ch5_pay_advance_pension = True

            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "奥尔德里克，拿一半金库银币出来。按当前士兵名册，每家先发 20 银。"

            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "……领主大人，这是预付抚恤金？"

            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "对。战死的，这钱当兵家拿；活下来的，算退伍补贴。"

            player "我不想让任何一个士兵带着「家里没钱」这一句话上战场。"

            $ hide_all_chars()
            "奥德当晚就让账房按名册分发。第二天清晨，操练场上的士兵安静了一会儿——然后开始一遍一遍地齐声唱艾登堡军歌。"

            "你站在城楼上听了半个时辰。"

        "拨出专款犒赏三军":
            $ change_stat("wealth", -5)
            $ change_stat("loyalty", 3)
            $ change_stat("power", 2)
            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "拿出一千银币，每个士兵发三个月的预付军饷。"
            player "让他们知道，无论发生什么，他们的家人会得到保障。"
            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "是。这会极大地提振士气。"

        "节省开支，准备长期消耗" if wealth >= 45:
            $ change_stat("wealth", 8)
            $ change_stat("loyalty", -8)
            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "战争可能持续很久。我们需要精打细算。"
            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "明白。我会削减不必要的开支。"
            aldric "……只是有句话得说在前头。抚恤和犒赏的钱都压下来了，底下已经有人嚼舌根，说领主把银子看得比命重。"
            $ hide_all_chars()
            "账面上省下的银子是实打实的。可那几天，操练场上的口令喊得没从前那么齐了。"

    hide aldric_img with dissolve

    $ hide_all_chars()
    "军需的账目核到最后一笔。能调的人、粮、械都已就位，剩下的要等敌人先动。"

    "你能做的，就是尽一切可能做好准备——然后在变化来临时迅速应对。"

    scene bg castle_exterior with dissolve
    $ unlock_gallery("bg_castle_exterior")

    "你站在城楼上，看着城外操练的士兵。"

    "他们排成整齐的队列，雷恩喊一声口令，全队走一遍刺杀。"

    "每一次刺出，都伴随着整齐的呐喊——那是勇气的声音，也是恐惧的掩饰。"

    "你的目光掠过操场，看到了城墙下正在搬运物资的百姓。"

    "老人、妇女、孩子——他们用自己的方式为即将到来的战争做着准备。"

    "有人在搬石头加固城墙，有人在晾晒草药，有人在缝补士兵的衣物。"

    "铁匠铺传来叮叮当当的打铁声，日夜不停。"

    "面包房的烟囱冒着白烟——他们在加班烤制干粮。"

    "这是一座即将面对风暴的城堡。但这座城堡里的每一个人，都在为生存而战。"

    ## balance pass 修法 2 续 12 (2026-05-11): 战前城楼俯视新加 menu
    ## 之前是纯叙事过场, 现在加 4 选项 (3 stat condition + 1 fallback)
    ## 覆盖 reputation/loyalty/intrigue 40 阈值 + power 路线 fallback
    menu:
        "你看着，知道自己还能做点什么。"

        "下城楼，亲自帮老人搬一块石头" if reputation >= 40:
            $ change_stat("reputation", 5)
            $ change_stat("loyalty", 3)
            $ change_stat("intrigue", -10)

            "你解了披风，沿城墙的窄梯下到城下。"

            "老人姓魏，八十一了，牙没剩几颗。他认得你。你没问他多大，直接把石头从他手里接过来。"

            "你帮他垒了五块石头。走的时候，他抓住你的胳膊，又松开了。"

            "他没说一个字。你也没问。"

            "老魏转头跟身边的邻居说了几句。他们看你的眼神变了。"
            "垒完最后一块石头，天已经黑透了。书房里那张铺开的舆图，今晚是看不成了。"

        "去铁匠铺，给打了一夜的老铁匠送一壶水" if loyalty >= 40:
            $ change_stat("loyalty", 5)
            $ change_stat("reputation", 3)
            $ change_stat("intrigue", -10)

            "铁匠铺烧了一整夜。老铁匠汉斯眼眶通红，手腕的肌腱凸起。"

            "你递过一壶凉水。他接过去，没说谢，一口气喝完。"

            "「领主大人，我这把年纪本来要干不动了。」"

            "「可您父亲十年前救过我儿子。我这把锤子，这几天都是给您家打的。」"

            "你点了点头。没说话。"

            "汉斯转身又开始打铁。火光把他的脸染成深红色。"
            "你在铁匠铺待到炉火压低。回主楼时雷恩已经睡下，舆图上该圈的隘口，只能等明早再说。"

        "回书房，把昨晚没看完的舆图研究完" if intrigue >= 40:
            $ change_stat("intrigue", 5)
            $ change_stat("power", 3)

            "你转身走回主楼。"

            "书房里的舆图昨晚被你按方位铺开了——男爵军的可能行军路线，王后军的预备阵地，你领地的几条隘口。"

            "你重新看了一遍。上次没注意到——男爵军过来必经鹰隼峡，而鹰隼峡两侧的山林正好可以伏弩。"

            "你拿铅笔在地图上画了一个圈。"

            "晚饭前，你叫雷恩进来。把圈给他看。"

            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "我连夜带二十人过去勘察地形。"
            $ map_studied = True

            hide captain_img with dissolve

        "不下城楼，继续看":
            $ change_stat("intrigue", 4)
            $ change_stat("loyalty", -6)

            "你没动。城楼上风大，把你的披风吹得鼓起。"

            "你看着下面，一动不动，看了很久。"

            "风把搬石头的老人的咳嗽声、铁匠铺的打铁声、孩子们的哭声，都卷到你站的地方。"

            "你把全城的备战看了个遍——哪段墙人手不够，哪队操练松垮，谁在偷懒。这些你都记下了。"

            "城楼下的士兵抬头看了你几次。整整一个傍晚，领主站在高处一动不动，没下来跟他们说一句话。"

            "等天暗了，你才下城楼。"

    ## 扩展剧情：军议 / 动员 / 战前夜 / 前哨战 / 风暴前夜
    call ch5_exp_war_council from _call_ch5_exp_war_council
    call ch5_exp_mobilize from _call_ch5_exp_mobilize
    call ch5_exp_last_night from _call_ch5_exp_last_night
    call ch5_exp_skirmish from _call_ch5_exp_skirmish
    call ch5_exp_eve_of_battle from _call_ch5_exp_eve_of_battle

    ## ============================================================
    ## 最终准备
    ## ============================================================

label ch5_preparation:

    scene bg great_hall with dissolve
    $ unlock_gallery("bg_great_hall")

    ## ── 政治联姻线「盟约」· 婚约落定 ──
    if marriage_route:
        "决战之前，还有一桩事要了结。"

        "婚礼在艾登堡办，北疆议会派了渡鸦旗下的全部话事人到场。希尔达站在英格丽身后，从头到尾没笑，却在仪式结束时对你点了头——这是你见过她最接近认可的表情。"

        "盟约写进了血脉。北境的盐路重新由你的人马护送，议会的卫队第一次开进了王畿以南。"
        $ change_stat("loyalty", 8)
        $ unlock_achievement("statecraft_marriage")

        if marriage_warm:
            $ hide_all_chars("ingrid_img")
            show ingrid_img at left with dissolve
            ingrid "我母亲说，我把一桩买卖谈成了一段日子。"
            ingrid "她不知道是夸我还是骂我。我也不知道。"
            $ hide_all_chars()
            "你没接话。但那天夜里，你们谁都没急着谈下一桩盟约。"
        else:
            "你和英格丽各守各的算盘。盟约稳固，日子客气。北境的兵是你的了，英格丽的心思仍是议会的。这桩婚事办成了它该办成的样子，不多不少。"

        $ hide_all_chars()
        scene bg great_hall with dissolve

    "决战在即。你再次召集核心幕僚，做最后的确认。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "领主大人，所有准备都已就绪。各方面都已按照之前军议的部署执行。"

    hide aldric_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    if power >= 50:
        captain "城防已加固完毕。将士们士气高昂——都在等领主大人的号令。"
    else:
        captain "城防已尽力加固。兵力虽寡，但每个人都做好了以死相搏的准备。"

    hide captain_img with dissolve

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve

    if spy_network:
        elena "最新情报——男爵军中有至少三个领主是被迫加入的。如果战局不利，他们随时可能倒戈。"
        elena "王后那边，蒙塔古伯爵和其他将领之间矛盾重重。如果我们能利用这些裂痕……"
        $ change_stat("intrigue", 2)
    else:
        elena "情报方面没有新的变化，敌军动向和之前军议时掌握的一致。"

    hide elena_img with dissolve

    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    $ unlock_gallery("bishop")

    if faith >= 50:
        bishop "教廷已经表态——在这场风暴中，他们选择站在您这边。"
        $ change_stat("faith", 8)
    else:
        bishop "教会仍在观望。但无论如何，我个人会留在您身边。"

    hide bishop_img with dissolve

    $ hide_all_chars()
    "你环顾四周——奥尔德里克、雷恩、艾琳娜、马修斯，每一张面孔都写满了坚定。"

    "一切已经就绪。现在只剩下最后的决定。"

    menu:
        "亲自走遍城堡每一处——你要的是「人都看见过你」" if loyalty >= 60:
            $ change_stat("loyalty", 5)
            $ change_stat("reputation", 3)
            $ log_decision("第五章", "亲自走遍城堡, 让所有人都看见领主")

            $ hide_all_chars()
            "你不召见任何人。你拎着一壶酒， 从城墙顶到地下水井， 一路走下去。"
            "厨子停下手里的活叫了一声领主。马夫从马厩出来抹了把汗。难民营里的孩子追着你跑了几步。"
            "你不说什么大话。只是问问每个人吃饭了没， 家里有没有需要照顾的事。"
            "回到书房时已是深夜。城堡里几乎每个人都见过你了。"
            "明天打仗， 不会有人想着逃。因为他们今晚都跟你说过话。"
            jump ch5_final_night

        "召见每一位核心幕僚，了解他们的真实想法":
            $ log_decision("第五章", "召见幕僚听取意见")
            jump ch5_counsel_all

        "独自思考，然后做出决定":
            $ log_decision("第五章", "独自思考做出决定")
            jump ch5_final_night

label ch5_counsel_all:

    scene bg study with dissolve
    $ unlock_gallery("bg_study")

    "做最终决定之前，你想再听一遍每位幕僚的看法。一个一个找过来谈。"

    ## --- 与奥尔德里克谈话 ---

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "奥尔德里克，说说你的真实想法。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "领主大人，我是个老人了。我一生侍奉艾登堡两代领主。"

    aldric "我见过太多权力的争夺。最终的赢家未必是最强的，而是最能审时度势的。"

    if rel_aldric >= 70:
        aldric "但是，我想对您说一句逾越的话——"
        aldric "您的父亲如果还在，他会希望您做正确的事，而不仅仅是做聪明的事。"
        aldric "有时候，正义比胜利更重要。"
        hide aldric_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "……谢谢你，奥尔德里克。"
    elif rel_aldric >= 40:
        hide player_char_img
        $ hide_all_chars("aldric_img")
        show aldric_img at left with dissolve
        aldric "我的建议是——无论您选择哪条路，都要确保艾登堡能够存续。"
        aldric "领地比领主更重要。这是老领主教给我的。"
    else:
        aldric "我只是一个管家，不敢妄议军国大事。"
        aldric "但请您至少……不要忘记这片土地上生活着的人民。"

    menu:
        "问他关于父亲的事":
            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            if true_killer_known:
                player "奥尔德里克……父亲的事，我们都心知肚明了。明天之后，他也该瞑目了。"
                hide player_char_img
                $ hide_all_chars("aldric_img")
                show aldric_img at left with dissolve
                aldric "……是啊。"
                aldric "老领主等这一天，等了二十年。我替他等了二十年。"
                aldric "真相是一把双刃剑，领主大人。它能伸张正义，也能引发更大的混乱——但不论结局如何，您不是一个人在扛。"
            else:
                player "奥尔德里克……你觉得父亲当年，是因为什么被杀的？"
                hide player_char_img
                $ hide_all_chars("aldric_img")
                show aldric_img at left with dissolve
                aldric "……"
                aldric "老领主太正直了。他发现了一个不该发现的秘密，而且他不愿意保持沉默。"
                aldric "如果他能像其他领主一样假装看不见……也许还活着。"
                aldric "但那样的话，他就不是老领主了。"
            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我明白了。谢谢你。"

        "感谢他的建议":
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你说得对。我会慎重考虑的。"
            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "老朽的话，领主大人听听就好。"

    if aldric_will_fight:
        hide player_char_img
        $ hide_all_chars("aldric_img")
        show aldric_img at left with dissolve
        aldric "大人——还有一件事。"
        aldric "我虽然老了，但剑还提得动。如果开战，请让我站在城墙上。"
        aldric "我来不是管家身份。是个老兵，愿意为您打这一仗。"
        hide aldric_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "奥尔德里克……你不必——"
        hide player_char_img
        $ hide_all_chars("aldric_img")
        show aldric_img at left with dissolve
        aldric "我必须。这是我自己的选择。"

    hide aldric_img with dissolve

    ## --- 与雷恩谈话 ---

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "雷恩，坐下说话。不用那么拘谨。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "是，领主大人。"

    "雷恩坐下后，却依然保持着笔挺的姿势。你不禁有些好笑。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "如果你是领主，你会怎么做？"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "我？"

    "雷恩愣了一下，然后认真地想了想。"

    if rel_captain >= 60:
        captain "如果我是领主……我会带着我的人，去做我认为对的事。"
        captain "战场上没有绝对的对错，但有一件事是确定的——你必须保护你身后的人。"
        captain "领主大人，无论您做出什么决定，我和我的士兵都会跟随您。"
        captain "我跟着您，不是冲忠诚那种事。是信任。"
        hide captain_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "……谢谢你，雷恩。"
        $ change_rel("rel_captain", 5)
    else:
        hide player_char_img
        $ hide_all_chars("captain_img")
        show captain_img at left with dissolve
        captain "我是个军人。军人服从命令。"
        captain "但如果可以的话……我希望能少死一些人。"
        hide captain_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "我也是。"

    menu:
        "问他对这一仗最担心什么":
            player "两军对垒——这次比西境那场更难打。你最担心什么？"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "西境那年我们只有一个方向要守。这次我们既要防北墙，也要防内鬼。"
            captain "我训练士兵时总说一句话——"
            captain "「活着回来比当英雄更重要。」"
            captain "领主大人，如果开战的话，请不要亲自冲在最前面。"
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我会考虑的。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "我知道您不会考虑的。所以我会紧紧跟在您身边。"

        "拍拍他的肩膀":
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "不管怎样，谢谢你一直以来的付出。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "这是我的荣幸，领主大人。"

    if captain_war_pledge:
        hide player_char_img
        $ hide_all_chars("captain_img")
        show captain_img at left with dissolve
        captain "领主大人——我之前说过的话，愿意为您赴死，每一个字都算数。"
        captain "这一仗，我的剑、我的命，都是您的。"

    hide captain_img with dissolve

    ## --- 与艾琳娜谈话 ---

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "艾琳娜，我需要听听你的分析。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "分析？还是想听我的真心话？"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "两者都要。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "好吧。先说分析——"

    elena "从纯粹的利益角度来看，最聪明的做法是等双方打完，然后趁虚而入。"

    elena "但这需要极高的时机把握能力，而且一旦失败，就会成为所有人的敌人。"

    elena "次优的选择是加入即将获胜的一方。但问题是——现在谁都不知道谁会赢。"

    elena "最安全的选择是闭门不出，固守艾登堡。但这也意味着放弃了影响未来局势的机会。"

    if elena_romance:
        elena "至于真心话……"
        "她走近了一步，声音低了下来。"
        elena "我不在乎你选择哪条路。我在乎的是你能活着。"
        elena "这几个月来……你已经不只是一个领主了。至少对我来说。"
        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "艾琳娜……"
        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "别说了。你的眼睛已经告诉我答案了。"
        "她轻轻地把头靠在你的肩上，只是一瞬间。"
        elena "好了，感性的话到此为止。说说你的计划吧，领主大人。"
        $ change_rel("rel_elena", 5)
    else:
        elena "至于真心话——我觉得你已经有了答案，只是需要别人推你一把而已。"
        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "也许吧。"
        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "那我推你一把——不管你怎么选，别后悔就行。"

    if elena_trust_deep:
        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "……还有一件私事。"
        elena "无论明天发生什么——你要活着回来。这是命令。"
        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "你什么时候开始给领主下命令了？"
        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "从我决定信任你的那一天起。"
    else:
        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "领主大人，明天的仗不好打。您多保重。"
        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "你也是，艾琳娜。"

    if dark_lily_joined:
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "对了，暗百合方面也有消息。"
        elena "首领让我转告你——组织在这次行动中可以提供三十名精锐刺客的支援。"
        elena "不多，但如果用在关键位置上，效果会远超一支普通军队。"
        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "暗百合的效率，我向来不怀疑。"
    else:
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "外部援助方面——我联系了几个旧日的线人。不算正规军，但关键时刻能帮上忙。"
        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "有总比没有强。"

    hide elena_img with dissolve

    ## --- 与主教谈话 ---

    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve

    hide bishop_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "主教大人，教会是什么态度？"

    hide player_char_img
    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "教会永远站在和平的一边。"

    hide bishop_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "这话说了等于没说。"

    hide player_char_img
    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "……好吧，让我说得更直白一些。"

    if faith >= 60:
        bishop "您是难得的虔诚领主。教会需要您这样的人来证明信仰的力量。"
        bishop "如果您选择以教会的名义推动和平，教廷会全力支持。"
        bishop "我可以动用教会的影响力，号召双方停战。"
        bishop "圣母的名义，在这片土地上依然有巨大的力量。"
        $ change_stat("faith", 10)
    elif faith >= 40:
        bishop "教会可以提供有限的支持。但请理解——教会不能公然卷入世俗的战争。"
        bishop "我们可以为伤兵提供救治，为难民提供庇护。"
        bishop "但要教会出面调停……需要您展现更多的诚意。"
    else:
        bishop "恕我直言，领主大人与教会的关系并不算亲密。"
        bishop "在这种时候寻求教会的帮助……需要付出相应的代价。"

    if poison_evidence:
        "你看着主教的眼睛，缓缓说道——"
        hide bishop_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "主教大人，「暮色之露」这个名字，你是否还记得？"
        "主教的脸色微微一变。"
        hide player_char_img
        $ hide_all_chars("bishop_img")
        show bishop_img at left with dissolve
        bishop "……您究竟想说什么？"
        hide bishop_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "我知道的比你想象的多。但现在不是算旧账的时候。"
        player "我需要你的合作。作为回报，我可以暂时忘记一些事情。"
        hide player_char_img
        $ hide_all_chars("bishop_img")
        show bishop_img at left with dissolve
        bishop "……我明白了。"
        "主教低下了头，你知道他已经没有选择了。"

    if bishop_total_loyalty:
        hide player_char_img
        $ hide_all_chars("bishop_img")
        show bishop_img at left with dissolve
        bishop "领主大人——撇开这些不谈。"
        bishop "我对您的忠诚不是因为利益交换。教会的全部资源，已在随时待命。"
        bishop "无论结局如何——我与艾登堡共进退。"

    if bishop_gave_key:
        hide player_char_img
        $ hide_all_chars("bishop_img")
        show bishop_img at left with dissolve
        bishop "对了——那把钥匙，您还留着吗？"
        hide bishop_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "一直带在身上。"
        hide player_char_img
        $ hide_all_chars("bishop_img")
        show bishop_img at left with dissolve
        bishop "好。如果战况危急，地下密室里有教会积攒多年的物资。那把钥匙能打开它们。"

    hide bishop_img with dissolve

    ## --- 与暗百合首领谈话（如果加入了） ---

    if dark_lily_joined:

        scene bg dungeon with dissolve
        $ unlock_gallery("bg_dungeon")

        $ hide_all_chars("lily_master_img")
        show lily_master_img at left with dissolve
        $ unlock_gallery("lily_master")

        lily_master "年轻的领主，你来了。"

        hide lily_master_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "首领，暗百合在这场战争中扮演什么角色？"

        hide player_char_img
        $ hide_all_chars("lily_master_img")
        show lily_master_img at left with dissolve
        lily_master "暗百合不参与战争。战争是愚蠢的权力游戏。"

        if lily_full_member:
            lily_master "但你既然走的是影卫一脉——我们关心秩序。混乱对我们的事业没有好处。"
        else:
            lily_master "但你跟影卫订了合作的契——我们关心秩序。混乱对我们的事业没有好处。"

        lily_master "如果你需要，影卫可以在关键时刻……改变天平的倾斜方向。"

        lily_master "一次精准的暗杀，一份关键的情报，一场及时的背叛——"

        lily_master "这些才是真正决定战争走向的因素。"

        "她停顿了一下，从袖中取出一张折起的纸条。"

        lily_master "还记得我之前提过吗——王后身边，有我们的人。"

        lily_master "她贴身的女官，三年前是影卫送进去的。她递出来的东西，比一支军队都管用。"

        $ shadow_guard_asset_revealed = True

        menu:
            "请暗百合协助执行一个精密的计划":
                $ change_stat("intrigue", 5)
                hide lily_master_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "我需要暗百合的人渗透双方阵营。不需要杀人，只需要制造混乱。"
                hide player_char_img
                $ hide_all_chars("lily_master_img")
                show lily_master_img at left with dissolve
                lily_master "有意思。你越来越像我们的人了。"
                lily_master "我会安排的。具体的行动计划，稍后送到你手上。"
                ## R2 隐藏/延迟代价: ch3"合作=互不臣属"看着干净, 但借影卫的刀=欠影卫的债, 那四个字开始作废
                if not lily_full_member:
                    lily_master "不过——当初你说『互不臣属』。这话还作数，但每借我们一次刀，那四个字就薄一分。"
                    lily_master "今天这个忙，我记在账上了。"
                    $ change_stat("reputation", -5)
                    $ change_rel("rel_lily", 8)
                    $ hide_all_chars()
                    "你知道她没说错。一个领主使着影卫的人做暗活，这事一旦漏出去，『清白』两个字就跟你没关系了。"

            "表示感谢但暂时不需要":
                hide lily_master_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "谢谢首领。等我需要的时候，会联系你。"
                hide player_char_img
                $ hide_all_chars("lily_master_img")
                show lily_master_img at left with dissolve
                lily_master "门永远为你敞开，年轻的领主。"
                lily_master "但记住——在这场棋局中，犹豫不决比做出错误的决定更危险。"

        hide lily_master_img with dissolve

    ## --- 与王子谈话（如果是盟友） ---

    if prince_ally and not prince_betrayed:
        call ch5_prince_letter from _call_ch5_prince_letter

    ## 章节深化：战前祈祷 / 最后的家书
    call ch5_deep_prayer from _call_ch5_dprayer
    call ch5_deep_last_letter from _call_ch5_dletter

    jump ch5_final_night

    ## ============================================================
    ## 诀别之夜
    ## ============================================================

label ch5_final_night:

    $ play_music("audio/music/campfire.ogg", fadein=2.0)
    scene bg castle_exterior with dissolve
    $ unlock_gallery("bg_castle_exterior")

    $ trigger_random_event("rest")

    "决战前夜。"

    "篝火在庭院中噼啪作响，城墙上的火把一盏接一盏地亮着，像是一条明灭不定的长蛇。"

    "城堡里异常安静。有些士兵在擦拭武器，有些在写家书。"

    "篝火在庭院中噼啪作响，火光映照着一张张或紧张或平静的脸。"

    "你独自站在城楼上，望着远方的黑暗。"

    "明天，一切都将改变。"

    "身后传来脚步声。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "领主大人，您应该休息了。明天会是漫长的一天。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "睡不着。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "老领主在大战前夜也总是睡不着。他会在书房里看书到天亮。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "他看什么书？"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "历史。他总说——「了解过去的错误，才能避免在未来重蹈覆辙」。"

    "你微微一笑。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "奥尔德里克，如果……如果明天出了什么事……"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "领主大人不要说这种不吉利的话。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我必须说。如果我出了什么事，艾登堡就交给你了。保护好百姓。"

    if rel_aldric >= 60:
        hide player_char_img
        $ hide_all_chars("aldric_img")
        show aldric_img at left with dissolve
        aldric "……领主大人。我侍奉您的父亲三十年，侍奉您将近一年。"
        aldric "这一年里，我看着您从一个懵懂的年轻人，成长为一个真正的领主。"
        aldric "明天不管发生什么，我都会在您身边。"
        $ hide_all_chars("aldric_img")
        show aldric_img sad at left with dissolve
        aldric "就像当年在您父亲身边一样——只是这一次，我不会再让悲剧重演。"
        "老管家的眼眶泛红了。你别过脸去，盯着墙上那幅父亲的旧画看了好一会儿。"
        hide aldric_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "谢谢你，奥尔德里克。谢谢你一切。"
    else:
        hide player_char_img
        $ hide_all_chars("aldric_img")
        show aldric_img at left with dissolve
        aldric "我会的，领主大人。这是我的职责。"

    hide aldric_img with dissolve

    $ hide_all_chars()
    "你走下城楼，来到庭院里。"

    "篝火旁，几个士兵正在低声交谈。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "领主大人！您怎么——"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "别起来。让我也坐一会儿。"

    $ hide_all_chars()
    "你在篝火旁坐了下来。士兵们面面相觑，有些不知所措。"

    "一个年轻的士兵——看起来不到二十岁——紧张地握着手中的剑。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你叫什么名字？"

    $ hide_all_chars("soldier_generic_img")
    show soldier_generic_img at left with dissolve
    young_soldier "回……回领主大人，小的叫汤姆。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "汤姆，你害怕吗？"

    $ hide_all_chars("soldier_generic_img")
    show soldier_generic_img at left with dissolve
    young_soldier "……害怕。但我更怕让领主大人失望。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "害怕是正常的。不害怕的人才有问题。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "领主大人说得对。上过战场的人都知道——恐惧不是弱点，是活下去的本能。"

    "你又看向另一个年长的士兵，他正在打磨一把缺了口的剑。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你呢？你为什么而战？"

    $ hide_all_chars()
    $ hide_all_chars("soldier_generic_img")
    show soldier_generic_img at left with dissolve
    veteran "为了我在城里的老婆和三个孩子。只要他们平安，我什么都愿意做。"

    "你环顾篝火旁的每一张脸。年轻的，年老的；紧张的，平静的。"

    "这些人，都把自己的命运交到了你手上。"

    menu:
        "把财库所有应急金分给士兵——明天活下来，这是退伍金" if wealth >= 50:
            $ change_stat("wealth", -10)
            $ change_stat("loyalty", 8)
            $ change_stat("reputation", 5)
            $ ch5_eve_split_treasury = True

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "雷恩，把财库剩下的金币全部分了。"

            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "全部？"

            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "每人五枚银币。活下来的算退伍金。"

            player "死了的——送回家，给妻子，给父母。"

            player "财库里留不下钱了。让它在活人手里发挥它该有的作用。"

            $ hide_all_chars()
            "士兵们一开始没反应过来。等明白是怎么回事，队伍里有人哭了。"

            "一个老兵走过来，抓住你的手攥得发白： 「领主大人……这钱我们家三代人都没见过。」"

            "你点头，没多说。"

            "消息很快传遍营地。有人把银币收进贴身的衣袋，有人攥着不放，反复数。"

        "举杯共饮，鼓舞士气":
            $ change_stat("loyalty", 3)
            $ change_stat("reputation", 2)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "雷恩，把酒拿出来。今晚每人一杯。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "领主大人？"
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "该省的时候省，该花的时候花。明天就要打仗了，让弟兄们暖暖身子。"
            $ hide_all_chars()
            "酒壶传了一圈又一圈。渐渐地，气氛不再那么凝重了。"
            "有人开始哼起了家乡的歌，有人讲起了荤笑话，还有人红着眼眶说起了远方的亲人。"
            "你静静地听着，火光映在你的脸上。"
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "弟兄们。明天不管发生什么——我为你们骄傲。"
            "篝火旁沉默了一瞬。然后，所有人齐声说道——"
            crowd "「为了艾登堡！」"

        "安静地陪伴他们":
            $ change_stat("loyalty", 2)
            $ hide_all_chars()
            "你没有说太多话，只是安静地坐在篝火旁。"
            "火堆噼啪响着，没有人起身离开。"
            "士兵们知道——他们的领主没有躲在城堡里，而是和他们坐在同一堆篝火旁。"
            "有人往火里添了根柴，谁也没说话。"

    hide captain_img with dissolve

    ## --- 与艾琳娜的最后对话 ---

    scene bg palace_garden with dissolve
    $ unlock_gallery("bg_palace_garden")

    "夜深了。你独自来到城堡的花园。"

    "花园里黑得只能看见轮廓——花还没有开放，毕竟才刚入春。"

    "但空气中已经有了一丝泥土和新芽的气息。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve

    elena "我就知道你会来这里。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你也睡不着？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "有谁能在这种夜晚睡着呢？"

    "她走到你身边，两人并肩站着。夜风灌进领口，带着初春泥土的凉意。"

    if elena_romance:
        elena "你知道吗？我从来没有想过自己会在乎一个人到这种程度。"

        elena "当我还是个孤儿的时候，我告诉自己——不要相信任何人，不要依赖任何人。"

        elena "但你问我累不累。你受伤的时候，第一件事是问我有没有事。"

        elena "从来没有人，为我做过这些。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "我知道。"

        $ hide_all_chars()
        "你伸手碰了一下她的手背。她的手凉，但没有缩开。"

        $ hide_all_chars("elena_img")
        show elena_img sad at left with dissolve

        elena "别得意。如果你明天死了，我会恨你一辈子。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "那我就努力不死。"

        "她靠在你的肩上。月光把两个人的影子拉得很长。"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "答应我一件事。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "什么事？"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "不管明天发生什么，不要做英雄。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "这个我不能答应你。"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "我就知道。"

        "她叹了口气，然后踮起脚尖，在你的脸颊上轻轻一吻。"

        elena "那就答应我另一件事——活着回来。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "这个，我答应你。"

        $ change_rel("rel_elena", 5)

    else:
        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "领主大人，有些话我不知道以后还有没有机会说。"

        elena "和你共事这段时间，是我人生中最充实的日子。"

        elena "不管明天的结果如何，我都不后悔来到艾登堡。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "谢谢你，艾琳娜。没有你的情报和分析，我走不到今天。"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "那就好。至少我的存在不是毫无意义的。"

        "她微笑了一下，然后转身离去。"

        elena "早点休息，领主大人。明天需要你头脑清醒。"

    hide elena_img with dissolve

    $ hide_all_chars()
    "花园里恢复了寂静。你抬头望向满天星斗。"

    "父亲，你在天上看着我吗？"

    "明天，我将做出我一生中最重要的决定。"

    "但愿我不会让你失望。"

    "你转身走回城堡。"

    "推开书房的门，你最后一次审视地图上的每一个标记。"

    scene bg study with dissolve
    $ unlock_gallery("bg_study")

    "烛芯歪了，光影跟着歪，地图上的标记一半明一半暗。"

    "你的目光在地图上的几个位置之间来回移动——"

    if dark_lily_destroyed:
        "王后军的行军路线，男爵联军的集结地，教会的势力范围……"
    else:
        "王后军的行军路线，男爵联军的集结地，教会的势力范围，暗百合的据点……"

    "还有，那份藏在密室中的遗诏。"

    "所有的线索，所有的选择，都在这一刻汇聚到了一起。"

    "你闭上眼睛，在黑暗中做出了决定。"

    ## ============================================================
    ## 最终抉择
    ## ============================================================

label ch5_final_choice:

    $ play_music("audio/music/tension.ogg", fadein=2.0)
    scene bg great_hall with dissolve
    $ unlock_gallery("bg_great_hall")

    "黎明时分。第一缕阳光穿过大厅的彩色玻璃窗，在地面上投下斑斓的光影。"

    "你的核心幕僚再次齐聚大厅。每个人的脸上都写满了期待和紧张。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "领主大人，所有人都在等待您的决定。"

    hide aldric_img with dissolve

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "士兵们已经集合完毕，随时听候调遣。"

    hide captain_img with dissolve

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve

    elena "情报已经更新到最新状态。无论您做出什么决定，我们都准备好了。"

    hide elena_img with dissolve

    $ hide_all_chars()
    "你站了起来，环顾四周。"

    "这些人——奥尔德里克、雷恩、艾琳娜——还有城堡外那些等待你命令的士兵和百姓。"

    "他们的命运，都系在你接下来的一句话上。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我已经做出了决定。"

    "大厅里一片寂静。"

    ## 根据积累的属性，筛选最突出的路线（只显示最高的1-2条专属路线 + 真相 + 保底）
    ## 避免所有路线同时出现显得杂乱
    ## 2026-05-26 洋溢之后批次反馈: 困难模式 60 属性百分百过检定 → 改用 difficulty.rpy
    ## 的 get_ending_threshold(), 让 hard=72/无保底、normal=65/55、easy=55/45 真正生效
    python:
        _ending_stats = [
            ("power", power, "iron_lord"),
            ("intrigue", intrigue, "shadow_king"),
            ("faith", faith, "holy_guardian"),
            ("loyalty", loyalty, "peoples_lord"),
        ]
        _ending_stats.sort(key=lambda x: x[1], reverse=True)
        _primary_th = get_ending_threshold("primary")
        _fallback_th = get_ending_threshold("fallback")
        _top_endings = set()
        for _i, (_sname, _sval, _eid) in enumerate(_ending_stats):
            if _sval >= _primary_th and _i < 2:
                _top_endings.add(_eid)
        ## 没有任何属性达 primary，且当前难度允许保底 → 取最高的那条
        if not _top_endings and _fallback_th is not None and _ending_stats[0][1] >= _fallback_th:
            _top_endings.add(_ending_stats[0][2])

        ## 2026-05-27 实装 vassal/fall 兜底结局
        _vassal_available = rel_queen >= (30 if _primary_th >= 70 else 0)
        _resist_available = rel_baron >= (30 if _primary_th >= 70 else 0)
        _truth_available = true_killer_known and testament_original_obtained
        _borgia_available = (deep_mother_herb == "poison" and intrigue >= 70 and poison_evidence)
        _any_main = bool(_top_endings) or _truth_available or _borgia_available
        _fall_only = not (_any_main or _vassal_available or _resist_available)

    $ mark_important_choice()
    menu:
        "以铁和血终结战争——用武力征服一切|权力路线 → 铁腕领主" if "iron_lord" in _top_endings:
            $ log_decision("第五章", "选择以铁血手段终结战争")
            $ ending_type = "iron_lord"
            player "这个世界只尊重力量。既然和平无法用嘴巴说出来，那就用剑来实现。"
            player "雷恩，全军出击。目标——击溃一切敌人。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "是！全军听令！"
            $ hide_all_chars()
            "大厅中响起了铠甲的碰撞声和脚步声。战争的机器开始运转。"
            call ending_decision_pause from _call_decision_pause_iron
            jump ending_iron_lord

        "让双方互相消耗，坐收渔利——暗中操控全局|谋略路线 → 影中之王" if "shadow_king" in _top_endings:
            $ log_decision("第五章", "选择在暗影中操控一切")
            $ ending_type = "shadow_king"
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "最高明的战争，是让敌人自己打败自己。"
            player "艾琳娜，启动我们的计划。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "明白。"
            $ hide_all_chars()
            "暗处的阴谋开始铺开，慢慢罩住整个战场。"
            call ending_decision_pause from _call_decision_pause_shadow
            jump ending_shadow_king

        "借教会之力，以信仰终止战争|信仰路线 → 圣光守护" if "holy_guardian" in _top_endings and not lily_full_member:
            $ log_decision("第五章", "选择以信仰之光化解争端")
            $ ending_type = "holy_guardian"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "刀剑只能制造死亡，不能带来和平。"
            player "主教大人，我需要教会站出来，用圣母的名义呼吁停战。"
            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "教会……愿意承担这个使命。"
            $ hide_all_chars()
            "你与教会联手，开始了一场用信仰对抗武力的战争。"
            call ending_decision_pause from _call_decision_pause_holy
            jump ending_holy_guardian

        "保护子民——固守艾登堡，拒绝战争|忠诚路线 → 人民领主" if "peoples_lord" in _top_endings:
            $ log_decision("第五章", "选择守护人民的幸福")
            $ ending_type = "peoples_lord"
            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我不是任何人的棋子，也不需要任何人的王座。"
            player "我只需要保护好我的人民。艾登堡的百姓，就是我最大的财富。"
            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "领主大人……"
            $ hide_all_chars()
            "你做出了一个出乎所有人意料的决定——放弃争霸，全力守护。"
            call ending_decision_pause from _call_decision_pause_peoples
            jump ending_peoples_lord

        "公布先王遗诏真相——让正义重见天日|真相路线 → 真相大白" if true_killer_known and testament_original_obtained:
            $ log_decision("第五章", "选择揭露全部真相")
            $ ending_type = "truth"
            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "这个王国建立在一个谎言之上。是时候让真相大白了。"
            player "我的父亲为此付出了生命。我不能让他白死。"
            $ hide_all_chars()
            "你从怀中取出那份尘封多年的遗诏复本，在阳光下展开。"
            "这一刻，你不是在为自己而战——而是在为二十年前被掩盖的正义而战。"
            call ending_decision_pause from _call_decision_pause_truth
            jump ending_truth

        "用毒药清理一切——以母亲的方式收尾|毒药路线 → 毒药公爵" if deep_mother_herb == "poison" and intrigue >= 70 and poison_evidence:
            $ log_decision("第五章", "选择以毒药逐一清理敌人")
            $ ending_type = "borgia"
            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "战场上的剑只能杀一个人。但一杯酒——可以让一整个家族在三个月内消失。"
            player "我母亲六岁就教会了我这个道理。"
            $ hide_all_chars()
            "你慢慢站起来，走到书房深处的那个旧木柜前。"
            "柜子最底层的暗格里，放着一个紫色的小瓶——你继任以来悄悄收集的「暮色之露」。"
            "够用了。"
            call ending_decision_pause from _call_decision_pause_borgia
            jump ending_borgia

        "效忠王后，换取艾登堡安全|附庸结局 → 附庸领主 (妥协)" if _vassal_available:
            $ ending_type = "vassal"
            $ log_decision("第五章", "选择效忠王后, 艾登堡降为附庸")
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "在两个选择都不好的时候，选那个能保住更多人性命的。"
            player "通知王后——艾登堡愿意效忠。"
            "你做出了一个务实的选择。不光荣，但你的人和领地保住了。"
            call ending_decision_pause from _call_decision_pause_pragmatic
            jump ending_vassal

        "加入男爵联军，对抗王后暴政|反抗路线 风险较高" if _resist_available:
            $ ending_type = "iron_lord"
            $ log_decision("第五章", "选择加入男爵联军反抗")
            player "王后的统治建立在谎言和暴力之上。是时候终结了。"
            player "告诉男爵——艾登堡与他并肩作战。"
            "你选择了反抗。前路艰险，而你站在了你认为正确的一边。"
            call ending_decision_pause from _call_decision_pause_resist
            jump ending_iron_lord

        "什么都做不了，等命运来到艾登堡的城门下|失败结局 → 艾登堡陷落" if _fall_only:
            $ ending_type = "fall"
            $ log_decision("第五章", "无路可走, 静候艾登堡陷落")
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "……我没有牌可以打了。"
            $ hide_all_chars()
            "大厅里没人接话。每个人都看着别处。"
            call ending_decision_pause from _call_decision_pause_fall
            jump ending_fall

    ## ============================================================
    ## 结局1：铁腕领主
    ## ============================================================

label ending_iron_lord:

    $ play_music("audio/music/war_drums.ogg", fadein=2.0)
    scene bg battlefield with dissolve
    $ unlock_gallery("bg_battlefield")
    $ set_mood("battle")
    $ set_weather("rain", "heavy")

    # ── 战力评估 (花露水反馈: 让属性 + 领主好感真正决定战局, 而非无脑通关) ──
    python:
        iron_war_score = 0
        iron_war_score += max(0, power - 30) // 4       # 军事投入
        iron_war_score += max(0, intrigue - 30) // 6    # 谋略部署
        iron_war_score += max(0, loyalty - 30) // 8     # 军心士气
        if alliance_baron:
            iron_war_score += 10                        # 男爵盟约 = 成建制的援军
        elif rel_baron > 0:
            iron_war_score += 4                          # 男爵中立偏善 = 至少不背刺
        if prince_ally:
            iron_war_score += 5                          # 王子的人脉
        if rel_captain >= 60:
            iron_war_score += 3                          # 雷恩的精锐死忠
        if ch5_pay_advance_pension:
            iron_war_score += 3                          # 抚恤已发: 士兵知道家里有着落, 阵前不惜命 (选择深度 L2)

    "艾登堡的军队集结完毕。旗帜在春风中猎猎作响。"
    if ch5_pay_advance_pension:
        "队列里没人交头接耳。抚恤银上个月就发到了各家手里——他们清楚，就算自己回不来，家里也有米下锅。这种安静，雷恩说，比喊破嗓子的口号顶用。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    if power >= 70:
        captain "领主大人，我们的兵力已经扩充到三百人。加上征召的民兵，接近五百。"
        captain "装备也是上乘——感谢您这几个月来在军事上的投入。"
        hide captain_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "够了。这些兵力，足够应对眼前的局势。"
        $ change_stat("power", 3)
    else:
        if rel_baron > 0:
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "男爵愿意与我们联手。加上他的兵力，我们有近四百人。"
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "告诉男爵，我们在北坡汇合。"
        else:
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "我们的兵力有限，但士气高昂。"
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "兵不在多而在精。我们用策略弥补数量上的不足。"

    if captain_knows_weakness:
        hide player_char_img
        $ hide_all_chars("captain_img")
        show captain_img at left with dissolve
        captain "领主大人，还记得我提过的敌军弱点吗？他们的左翼换防时有短暂的空档。"
        captain "如果我们在那个时机集中突击——可以打乱他们的整条防线。"
        hide captain_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "记得。这个情报留到关键时刻用。"

    hide captain_img with dissolve

    ## ── 战前谋略：情报与准备 ──
    scene bg study with dissolve

    "大军开拔前夜。你在书房里铺开了地图，召集核心幕僚做最后的战前部署。"

    show elena_img at right with dissolve
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    hide captain_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "我的探子带回了敌军的情报。他们的主力驻扎在北坡，大约八百人。"

    hide elena_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "比我们多。但不是不能打。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "光靠硬拼不行。我们需要一个计划。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "我有三条情报，每一条都可以利用。"

    elena "第一，敌军的粮草补给线经过石桥谷，只有一条路。"

    elena "第二，敌军中有一支雇佣兵，忠诚度不高——给够了钱就可能临阵倒戈。"

    elena "第三，北坡西面的山路没有设防，可以派一支小队绕后。"

    $ mark_important_choice()
    menu:
        "祈祷夜——以信仰为全军点一夜的火" if faith >= 60:
            $ change_stat("faith", 5)
            $ change_stat("loyalty", 3)
            $ iron_war_score += 4
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "马修斯主教，今夜城堡广场——给全军一场祈祷。"

            player "不是求胜，是让每一个明早要走上战场的人，知道他不是一个人。"

            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "……老朽明白。我会让每一位修士今夜都不睡，跟士兵们站在一起。"

            $ hide_all_chars()
            "那一夜，城堡广场上烛火彻夜不熄。"

            "老兵们围着主教坐着，听他低声念诵祷词。"

            "没有人说话，也没有人离开。"

            "第二天清晨，当大军开拔时，你看见许多士兵的盔甲下都塞着主教发的祈祷珠。"

            "他们走得很慢——但没人再回头看。"

        "截断补给线——让他们饿三天再打|谋略+ 敌军士气大降":
            $ change_stat("intrigue", 5)
            $ change_stat("reputation", -8)
            $ change_stat("loyalty", -4)
            $ iron_war_score += 6
            if baron_supply_intel:
                $ iron_war_score += 3
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "派一百人去石桥谷，毁掉桥梁，截断补给。我们等三天再开战。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "高明。饿了三天的士兵，连剑都举不起来。"
            hide elena_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "遵命！"
            $ hide_all_chars()
            "三天后，前线传来消息——敌军已经开始宰杀战马充饥。"
            if baron_supply_intel:
                "男爵军的补给走河谷小道，护卫不足百人——这底细你早摸清了。这一刀，你知道往哪儿切。"
            "那座石桥是石桥谷百姓进出大山的唯一一条路。桥断了，这个春天他们运不出一捆柴、换不回一袋盐。"
            "军中也有怨言——在野外干等三天，比打仗还磨人。"

        "收买雇佣兵——瓦解敌军内部|需财富≥40 · 战场上获得内应" if wealth >= 40:
            $ change_stat("wealth", -10)
            $ change_stat("intrigue", 3)
            $ change_stat("reputation", -5)
            $ iron_war_score += 6
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "准备五百金币，通过暗线联系那支雇佣兵的头领。"
            player "告诉他——临阵倒戈，事后加倍付酬。拒绝的话，战后秋后算账。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "明白。我今夜就安排人去接触。"
            $ hide_all_chars()
            "第二天，回信来了——雇佣兵同意在战斗最激烈时「调转枪头」。"
            "用钱买来的忠诚靠不靠得住，你心里没底。买通敌阵叛将这种事也瞒不了多久——传开了，没人会说这是光明正大的打法。"
            "一枚埋在敌军内部的棋子，已经就位了。"

        "山路绕后——前后夹击|需权力≥55 · 战术优势" if power >= 55:
            $ change_stat("power", 3)
            $ change_stat("intrigue", 3)
            $ change_rel("rel_captain", -10)
            $ iron_war_score += 8
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "雷恩，你带一百精锐，连夜从西面山路绕到敌军后方。"
            player "主力正面推进时，你从背后杀出。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "声东击西，前后夹击！领主大人果然读过兵法！"
            captain "只是——我带走的是您身边最好的一百个人。这一去，您正面就少了一道屏障。"
            "当夜，雷恩带着一百名精挑细选的士兵从西门出发。没有火把，没有号角，只有甲胄在黑暗中轻轻碰撞的声音。"

    hide elena_img with dissolve
    hide captain_img with dissolve

    scene bg battlefield with dissolve

    "大军开拔之前，你做了最后的检阅。"

    "士兵们排列成整齐的方阵，长矛如林，盾牌如墙。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "雷恩，你跟了我多久了？"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "从第一天起，领主大人。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "那就再跟我打最后一仗。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "荣幸之至。"

    hide captain_img with dissolve

    "你骑上战马，拔出佩剑，对着你的士兵们高声说道——"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "弟兄们！你们中有些人是老兵，有些人是第一次上战场。"

    player "但今天，你们都是艾登堡的勇士！"

    player "我不会欺骗你们——前方有危险，有流血，有死亡。"

    player "但只要我们团结一致，就没有任何力量能击败我们！"

    player "为了艾登堡！为了我们的家！"

    crowd "「为了艾登堡！！！」"

    "震天的呐喊声在晨风中回荡。"

    scene bg battlefield with dissolve
    $ unlock_gallery("bg_battlefield")

    "大军向北进发。沿途的村庄已经空无一人——村民们早已逃往安全的地方。"

    "田野里残留着去年的枯草，被早春的泥泞浸透。"

    "第三天，你的前锋部队与敌军的斥候遭遇。"

    "第一场小规模冲突爆发了。"

    menu:
        "亲自率领前锋出击":
            $ change_stat("power", 5)
            $ change_stat("reputation", 3)
            $ change_rel("rel_captain", -12)
            "你策马冲在最前面，剑光划过空气。"
            "敌军的斥候被你的气势震慑，很快溃散。"
            "士兵们看到领主亲自冲锋，士气大振。"
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "领主大人！您不能这么冒险！"
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我的士兵在流血，我怎么能躲在后面？"
            $ hide_all_chars()
            "消息传开后，你的军队士气暴涨，而敌军则开始恐惧——这个年轻的领主不是个花架子。"
            "一个年轻的士兵——就是前夜篝火旁的汤姆——在你身边奋勇作战。"
            "他的动作还很生涩，但眼中有着不输任何老兵的决心。"
            $ hide_all_chars("soldier_generic_img")
            show soldier_generic_img at left with dissolve
            young_soldier "领主大人！我掩护您！"
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "好小子！跟紧我！"
            $ hide_all_chars()
            "乱军里你挨了一记。左臂的甲被劈开一道口子，血顺着护腕往下淌。你顾不上——但回阵时雷恩的脸，比挨了刀还难看。"

        "让雷恩指挥前锋，自己统领全局":
            $ change_stat("intrigue", 3)
            $ change_stat("power", 2)
            $ iron_war_score += 3
            $ change_rel("rel_captain", 4)
            $ hide_all_chars()
            "你站在山丘上，用旗语指挥部队的行动。"
            "雷恩率领前锋以精妙的战术击溃了敌军斥候。"
            "你的冷静和判断力让整支军队像一台精密的机器一样运转。"
            "雷恩在前头打得游刃有余。回阵时他朝山丘上的你点了点头——领主肯把刀递到他手里、自己稳坐中军，这份信他领了。代价是你没在士兵眼前露脸，这一仗的彩头记在雷恩名下，不在你头上。"

    "前哨战获胜后，你的军队继续推进。"

    "第二天，你遇到了一个被遗弃的村庄。"

    "房屋全烧了，田地踩烂了。一个老人坐在废墟上，茫然地看着天空。"

    $ hide_all_chars("farmer_rep_img")
    show farmer_rep_img at left with dissolve
    old_man "他们来了……像蝗虫一样……拿走了一切……"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "是谁干的？"

    $ hide_all_chars("farmer_rep_img")
    show farmer_rep_img at left with dissolve
    old_man "穿铠甲的人……我分不清是哪边的……对我们来说都一样……"

    "战争的残酷不在于战场上的厮杀——而在于那些被波及的无辜之人。"

    menu:
        "亲自跪在老人面前——以你的名义起誓重建" if loyalty >= 70:
            $ change_stat("loyalty", 5)
            $ change_stat("reputation", 5)
            $ change_stat("power", -6)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "老人家。"
            "你下马， 单膝跪在他面前。"
            player "我以艾登堡领主的名义起誓——这场仗打完， 我亲自带石匠回来。"
            player "你的房子会有屋顶。你的田会有人翻。你儿子的坟前会有人烧纸。"
            $ hide_all_chars()
            "老人愣了。然后他握住你的手， 说不出话， 只是流泪。"
            "周围的士兵静下来了。他们看见领主单膝跪在一个庄稼老汉面前。"
            "雷恩站在马边没动。这位打了十二年仗的老兵心里清楚：肯为一个老人下跪的领主，士兵会替他卖命；可下跪这件事本身，也让一些人记住了——原来这位领主也会跪。"

        "留下食物和士兵守这里":
            $ change_stat("loyalty", 3)
            $ change_stat("power", -1)
            $ iron_war_score -= 3
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "留十个人在这里。帮老百姓重建家园。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "但领主大人，我们的兵力本就不——"
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "执行命令。"
            "十个人，加上半车干粮，从北上的队列里被划了出去。雷恩没再争——他只是在花名册上勾掉了那十个名字。这一队人马，三天后的旷野上你是用不上了。"

        "记住这一切，继续前进":
            $ change_stat("power", 2)
            $ change_stat("loyalty", -5)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "记住这些。记住战争的代价。等一切结束了，我们会回来重建。"
            $ hide_all_chars()
            "你勒转马头，队伍跟着你走了。没人出声。可你背后那点窸窣的脚步声里，少了点什么——昨夜篝火旁还跟你说笑的几个新兵，今早盯着那片废墟，谁也没看你。"

    "第三天和第四天，你又遇到了几次小规模遭遇。"

    "每一次，你都果断地击退了敌人，同时尽量减少自己的伤亡。"

    "你的军队在战斗中越来越默契——新兵在真正的战场上迅速成长为合格的战士。"

    "第五天，两军主力终于在旷野上对峙了。"

    scene bg battlefield with dissolve
    $ unlock_gallery("bg_battlefield")

    "对面的军阵一眼望不到头。旌旗蔽日，铠甲的反光刺得人睁不开眼。"

    "你的心跳加速。这是真战争——决战级别的，不是过去那些零星冲突。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "领主大人，敌军正在列阵。他们的骑兵在左翼，步兵在中央，弓手在后方。"

    captain "按照正常的打法，我们应该——"

    # 是否具备一条像样的战术 — 否则只能硬拼 (花露水反馈: 准备不足要付代价)
    $ _iron_prepared = (power >= 60) or (intrigue >= 55) or (intrigue >= 45 and loyalty >= 50)
    menu:
        "正面强攻，以气势压倒对方|需权力≥60" if power >= 60:
            $ change_stat("power", 5)
            $ change_stat("loyalty", -7)
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "全军出击！一鼓作气冲垮他们！"
            $ hide_all_chars()
            "老兵们对望了一眼。这一令的意思他们都懂——头一排撞上去的人，活下来的不会多。"
            "战鼓擂响。你的军队如洪流般冲向敌阵。"
            "铁与铁的碰撞，血与血的交融。战场上响彻着惨叫和呐喊。"
            if iron_war_score >= 22:
                "你的兵甲是这几个月一刀一枪攒出来的。硬撞之下，先撕开防线的是你。"
                "代价不轻，但第一回合是你赢了。"
            else:
                $ iron_battle_outcome = "pyrrhic"
                "可你的人手不够厚。正面对撞，两边都在往下掉人。"
                "你赢了第一回合——靠的是拿命去填。雷恩的脸色很难看。"

        "采用迂回战术，先攻击敌军侧翼|需谋略≥55" if intrigue >= 55:
            $ change_stat("intrigue", 3)
            $ change_stat("power", 3)
            $ change_rel("rel_captain", -8)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "雷恩，带两百人从树林绕到敌军右翼。我在正面吸引他们的注意力。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "……是。"
            $ hide_all_chars()
            "他没多说什么，但你听得出那个停顿。把两百人从主阵抽走，正面就得拿单薄的阵线去顶——他清楚，你也清楚。"
            if iron_war_score >= 18:
                "你的计划完美地执行了。当雷恩的部队从侧翼杀出时，敌军阵脚大乱。"
                "一场漂亮的迂回战，让你以最小的代价取得了最大的战果。"
            else:
                $ iron_battle_outcome = "pyrrhic"
                "迂回是对的，可你能分出去的人太少。雷恩那一击没能凿穿。"
                "敌军缓了过来。你扳回了局面，但战线被拖成了消耗战。"

        "先防御，等待敌军露出破绽再反击|需谋略≥45 · 忠诚≥50" if intrigue >= 45 and loyalty >= 50:
            $ change_stat("intrigue", 4)
            $ change_stat("loyalty", 2)
            $ change_stat("reputation", -6)
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "结成防御阵型。盾墙在前，长矛在后。让他们先来攻。"
            $ hide_all_chars()
            "对面阵中有人哄笑起来，隔着旷野喊艾登堡的领主缩了。这话会随败兵传开——可你不在乎，先挨过这几波再说。"
            if iron_war_score >= 16:
                "敌军发起了一波又一波的冲锋，但你的防线像磐石一样岿然不动。"
                "随着进攻的失败，敌军的士气开始下降。终于，你看到了破绽——"
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "全军反击！！！"
                "你的反攻势不可挡。疲惫的敌军在你凌厉的攻势下迅速崩溃。"
            else:
                $ iron_battle_outcome = "pyrrhic"
                "盾墙撑住了前几波。可你的兵太疲，阵线一处接一处地凹下去。"
                "你等到了反击的破绽——但反扑出去的力气，已经剩不下多少了。"

        "硬拼——你没有更好的选择了" if not _iron_prepared:
            $ change_stat("power", 2)
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "顶上去。没有别的办法了。"
            $ hide_all_chars()
            if iron_war_score >= 14:
                $ iron_battle_outcome = "pyrrhic"
                "你没有奇兵，没有内应，能做的只有把人压上去。"
                "靠一股不肯退的狠劲，你险险撕开了一道口子——但每一步都踩在自己人身上。"
            else:
                "你没有奇兵，没有内应，也没有足够的人。"
                "拿三百人去填一场根本没准备好的会战——结果就摆在眼前。"
                jump ironlord_battle_lost

    hide captain_img with dissolve

    $ hide_all_chars()
    "战斗打了整整一天。从黎明打到黄昏。"

    "中午时分，战局一度胶着。"

    "你的左翼受到了猛烈攻击，防线出现了裂缝。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "领主大人！左翼快撑不住了！"

    menu:
        "用早就埋下的反间——让他们的右翼调头攻自己人" if intrigue >= 60:
            $ change_stat("intrigue", -25)  ## 消耗机制大轮: 动用=烧暗子。布了三个月的反间用一次就废, 情报网元气大伤
            $ change_stat("loyalty", 2)
            $ change_stat("reputation", -3)  # 阴谋手段, 战后名声受损
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "雷恩， 现在。让你那个「被俘的」信使把假军令递出去。"
            $ hide_all_chars()
            "三个月前你就准备好了这一手——伪造的盟军调令， 骑着对方军队制服的信使。"
            "这一手只能用一次。信使一旦递出假令就会暴露， 伪造的渠道也会被对方顺藤摸瓜查封——你布了三个月的这条暗线， 为这一仗烧光了。"
            $ trigger_crisis("intrigue", 6,
                "信使要让敌军右翼指挥官相信那是自己将军的笔迹。这一刻——靠的是你伪造的细节真的骗得过老兵的眼睛。",
                "ironlord_ruse_win", "ironlord_ruse_lose",
                courage_cost=15)
            call crisis_encounter from _call_crisis_ironlord_ruse

        "亲自率领预备队增援左翼":
            $ change_stat("power", 3)
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "跟我来！"
            $ hide_all_chars()
            $ trigger_crisis("combat", 7,
                "你冲进了左翼的混战。这一刻——你的剑得真能砍开围你的人, 你的旗帜得让士兵们抬起头。",
                "ironlord_charge_win", "ironlord_charge_lose",
                courage_cost=20)
            call crisis_encounter from _call_crisis_ironlord_charge

        "命令右翼迂回，从侧面攻击敌军":
            $ change_stat("intrigue", 3)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "左翼继续坚守！右翼绕到敌军后方——给我咬住他们！"
            $ hide_all_chars()
            $ trigger_crisis("intrigue", 5,
                "右翼要走一个大弧线绕到敌军后方。这一刻——靠的是你定的时间表真的对得上, 不晚不早。",
                "ironlord_flank_win", "ironlord_flank_lose",
                courage_cost=10)
            call crisis_encounter from _call_crisis_ironlord_flank

    label ironlord_post_left_flank:
    hide captain_img with dissolve

    "下午三点，战场上的局势翻了——"

    "敌军的主将出现在了你的视线范围内。他骑着一匹黑色战马，在战场中央指挥着部队。"

    menu:
        "集中兵力，直取敌将":
            $ change_stat("power", 5)
            "你集中了所有能调动的骑兵，形成了一个锋利的箭头阵型。"
            "目标只有一个——敌军主将。"
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "随我冲！！！"
            $ hide_all_chars()
            "铁蹄声如雷。你的骑兵像一把利剑，直接刺入了敌军的心脏。"
            "敌将的护卫拼死抵抗，但挡不住你势不可挡的冲锋。"
            "当你的剑尖指向敌将的咽喉时——他扔下了手中的武器。"
            $ hide_all_chars("soldier_generic_img")
            show soldier_generic_img at left with dissolve
            enemy_general "……我投降。"
            "主将被俘的消息传开后，敌军的抵抗迅速瓦解。"

        "围而不攻，逼迫敌军投降":
            $ change_stat("intrigue", 4)
            $ change_stat("loyalty", 2)
            "你没有急于求成。相反，你命令部队从三面包围敌军，只留下一条退路。"
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "让他们跑。追击的时候总比死战的伤亡小。"
            $ hide_all_chars()
            "果然，被包围的敌军开始从那条唯一的退路逃散。"
            "没有了阵型的溃兵毫无威胁。你的骑兵在后面追击，收获了大量俘虏。"

    "当夕阳染红了战场时，你站在山丘上俯瞰着满地的旗帜。"

    "有些旗帜还在飘扬。有些永远倒下了。"

    "遍地的尸体诉说着战争的残酷。有些面孔还保持着恐惧的表情，永远凝固在死亡的瞬间。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "领主大人……我们赢了。"

    "雷恩的声音有些沙哑。他的铠甲上满是血迹——有敌人的，也有他自己的。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "伤亡如何？"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    if iron_battle_outcome == "pyrrhic":
        captain "我们阵亡了两百多人， 伤了三百多。敌军——是我们的两倍， 不是三倍。"
    else:
        captain "我们阵亡了七十多人，伤了一百多。敌军……至少是我们的三倍。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    if iron_battle_outcome == "pyrrhic":
        player "两百多人……"
        $ hide_all_chars()
        "你闭上了眼睛。两百多条生命。每一个都是一个家庭塌下来。"
        "这场仗你赢了， 但代价大得让你不敢去看名册。"
    else:
        player "七十多人……"
        $ hide_all_chars()
        "你闭上了眼睛。七十多条生命。每一个都是一个家庭的支柱。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "领主大人，这已经是最好的结果了。在这种规模的战斗中——"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我知道。让人收拢伤兵，安葬阵亡者。每一个人都要记录姓名。"

    player "战后，他们的家人会得到抚恤。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "是！"

    hide captain_img with dissolve

    if elena_romance:
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "你受伤了。"
        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "皮外伤。"
        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "让我看看。"
        "她的手轻轻地检查着你手臂上的伤口，动作很温柔。"
        elena "你又没听我的话。说好了不当英雄的。"
        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "我没当英雄。我只是在保护我的人。"
        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "……我恨你。"
        "但她眼中的泪水出卖了她的真实感受。"
        hide elena_img with dissolve
    else:
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "领主大人，您的手臂在流血。"
        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "不碍事。先处理伤兵的事。"
        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "……好吧。但之后必须让医官看看。"
        hide elena_img with dissolve

    $ hide_all_chars()
    "战争结束了。你活了下来。"

    "接下来的日子里，你率军北上，接收了战败一方的领地。"

    "那些曾经不把你放在眼里的领主们，如今纷纷低下了高贵的头颅。"

    scene bg great_hall with dissolve
    $ unlock_gallery("bg_great_hall")
    $ set_mood("victory")
    $ clear_weather()

    "你回到艾登堡时，城门两旁挤满了欢迎的人群。"

    "鲜花、欢呼、泪水——混杂在一起。"

    "有人在庆祝胜利，有人在悼念亡者。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "领主大人，王都来了使者。"

    $ hide_all_chars()
    "使者带来了一个令人意外的消息——各方势力请求谈判。"

    "你的军事胜利让所有人都明白了一个道理——艾登堡不是好惹的。"

    "但胜利之后，如何处置战败者，将决定你未来的统治根基。"

    hide aldric_img with dissolve

    ## ── 战后处置：权谋选择 ──
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    show elena_img at right with dissolve

    hide elena_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "领主大人，战俘有三百多人。败军的领主也在其中。怎么处置？"

    hide captain_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "另外，战败方的领地现在群龙无首。是吞并，还是扶植傀儡？"

    $ mark_important_choice()
    menu:
        "宽大为怀——释放战俘，与战败方签订平等条约|忠诚+ 声望+ 敌意消除":
            $ change_stat("loyalty", 10)
            $ change_stat("reputation", 10)
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "释放所有战俘。告诉他们的领主——过去的事既往不咎，但下一次我不会再手下留情。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "领主大人仁慈！"
            hide captain_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "……这招比杀了他们更厉害。从此他们欠你一条命。"
            "消息传开后，周围的领主纷纷遣使示好。一个仁慈而强大的领主——是所有人都想结交的盟友。"

        "杀鸡儆猴——处决首恶，释放士兵|权力+ 声望- 威慑四方" if power >= 55:
            $ change_stat("power", 10)
            $ change_stat("reputation", -5)
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "士兵是无辜的，放他们回家。但挑起战争的人——必须付出代价。"
            $ hide_all_chars()
            "你在城门前公开处决了三名主要战犯。"
            "从那以后，再没有人敢轻视艾登堡的旗帜。"
            "但也有人在背后说——这个年轻的领主，比他父亲更冷酷。"

        "吞并领地——将战败方纳入版图|权力+ 财富+ 管理压力大" if power >= 60:
            $ change_stat("power", 15)
            $ change_stat("wealth", 18)
            $ change_stat("reputation", -3)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "战败者的领地归入艾登堡管辖。派驻官员，接管税收和防务。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "领主大人的野心不小。"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "不是野心。是责任。那些领地的百姓需要一个能保护他们的人。"
            "你的版图一夜之间扩大了三倍。但随之而来的，是治理的巨大压力。"

    hide captain_img with dissolve
    hide elena_img with dissolve

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "和平来了？"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "是的。虽然是建立在武力之上的和平——但确实是和平。"

    hide aldric_img with dissolve

    $ play_music("audio/music/main_theme.ogg", fadein=2.0)
    scene black with dissolve

    "此后的日子里，你凭借在战争中积累的军功和威望，成为北方最强大的领主。"

    "你重建了被战火摧毁的村庄，安置了失去家园的难民。"

    "你建立了一支强大的常备军，让任何心怀不轨的势力都不敢轻举妄动。"

    "人们称你为「铁腕领主」。"

    "你的领地繁荣昌盛，边境安宁。没有人敢挑战你的权威。"

    scene bg great_hall with dissolve
    $ unlock_gallery("bg_great_hall")

    "十年后。"

    "你坐在大厅的领主之位上，听取幕僚们的汇报。"

    "艾登堡已经从一个小领地，发展成了北方最富饶的城邦。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "领主大人，今年的税收再创新高。北方各领主的贡品也已经到齐。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "嗯。拨出三成用于修路和水利。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "是。"

    aldric "另外……今天是老领主的忌日。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我知道。备一束野花，我去墓前。"

    hide aldric_img with dissolve

    "你来到父亲的墓前，把那束野花放在墓碑下。"

    player "父亲，我做到了。"

    player "我用你不一定认同的方式——但我保护了这片土地，保护了我们的人民。"

    player "你会原谅我吗？"

    "风吹过墓碑上的苔藓，仿佛在回应你的话语。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "领主大人，您实现了老领主未竟的梦想。"

    aldric "但愿这份和平，能够持久。"

    "你转过身，看着远处繁忙的城镇。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "和平是需要维护的。只要有人试图打破它——"

    player "铁腕，随时准备好。"

    hide aldric_img with dissolve

    $ hide_all_chars()
    "但有时在深夜，你会想起战场上那些倒下的人。"

    "你赢了。但你失去了一些永远无法挽回的东西。"

    "这就是铁腕领主的代价。救了所有人，自己睡不着觉。"

    if elena_romance:
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "又做噩梦了？"
        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "嗯。梦见了战场。"
        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "那些人的牺牲不是没有意义的。因为你，更多人活了下来。"
        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "我知道。但知道和释怀，是两回事。"
        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "那就让时间来慢慢释怀吧。"
        "她握住你的手。在黑暗中，这份温暖让你感到安心。"
        hide elena_img with dissolve
    else:
        $ hide_all_chars()
        "有时在深夜醒来，你会独自走到城墙上，看着远方沉默的原野。"
        "没有人在身边。但城中安睡的百姓，就是你继续前行的理由。"

    $ unlock_achievement("iron_lord")
    $ persistent.endings_seen.add("iron_lord")

    jump game_ending

## ── 铁腕线左翼危机 crisis labels (栀子 2026-05-02 反馈: 缺判定) ──
label ironlord_ruse_win:
    "信使在敌阵后方「被巡逻队抓住」， 信件搜出， 当场宣读。"
    "敌军右翼指挥官认不出真假， 但他认得自己将军的笔迹——你伪造的笔迹。"
    "右翼调头朝中军开火。十分钟后， 敌阵从内部崩溃。"
    "左翼的危机解了， 不是因为你派了人去救——是因为敌人开始救自己。"
    jump ironlord_post_left_flank

label ironlord_ruse_lose:
    $ iron_battle_outcome = "pyrrhic"
    "信使经验不够。当敌方一个老校官皱眉问「这印章不太对吧」时， 他的眼神慌了一瞬。"
    "信件露馅。信使当场被绞，反间彻底失败。"
    "左翼的防线在援兵调到之前就真的崩了——你赢的代价大了。"
    jump ironlord_post_left_flank

label ironlord_charge_win:
    "你带着最后的预备队冲向了左翼。你的出现重新点燃了士兵们的斗志。"
    "在你的带领下，摇摇欲坠的防线重新稳固了下来。"
    "敌军看到你的旗帜出现在左翼，犹豫了一瞬——就是这一瞬间的犹豫，改变了战局。"
    jump ironlord_post_left_flank

label ironlord_charge_lose:
    $ iron_battle_outcome = "pyrrhic"
    "你冲进了混战， 但敌人的预备队比你想象的多。"
    "一支长矛擦着你的腰侧划过， 你的战马倒下了。"
    "雷恩拼死把你从战阵里拽出来——左翼是稳了， 可大半的预备队没回来。"
    jump ironlord_post_left_flank

label ironlord_flank_win:
    "你的命令被迅速执行。右翼的部队以一个大胆的弧线绕到了敌军身后。"
    "当敌人发现自己被两面夹击时，已经来不及了。"
    jump ironlord_post_left_flank

label ironlord_flank_lose:
    $ iron_battle_outcome = "pyrrhic"
    "右翼出发得晚了一刻——这一刻足够让对方哨兵发出警报。"
    "你的右翼撞上了敌军临时调头的步兵方阵， 两线都陷入了苦战。"
    "左翼最后是靠人头硬填回来的——胜利留下的不是欢呼， 是阵亡名单。"
    jump ironlord_post_left_flank

## ── 铁腕线会战惨败 → 艾登堡陷落 (花露水反馈: 准备不足要有战败结局) ──
label ironlord_battle_lost:
    $ hide_all_chars()
    scene bg battlefield with dissolve
    "你的中军是从正中央被凿穿的。"
    "没有援军，没有内应，没有一支能绕到敌后的奇兵——你能押上的，只有正面那三百人。"
    "他们撑了不到一个时辰。"
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "领主大人！阵线断了！再不走就走不掉了！"
    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "……鸣金。带能带走的人撤。"
    $ hide_all_chars()
    "雷恩拽住你的马缰，往艾登堡的方向退。"
    "你回头看了最后一眼。你的旗帜倒在泥水里，没有人去扶。"
    $ change_stat("power", -10)
    $ change_stat("reputation", -8)
    $ change_stat("loyalty", -5)
    "残部退回了城里。北方那两支大军，跟着你的背影，一路压到了艾登堡城下。"
    $ ending_type = "fall"
    $ log_decision("第五章", "铁腕会战惨败, 退守艾登堡")
    jump ending_fall

    ## ============================================================
    ## 结局2：影中之王
    ## ============================================================

label ending_shadow_king:

    $ play_music("audio/music/night_mystery.ogg", fadein=2.0)
    scene bg study with dissolve
    $ unlock_gallery("bg_study")

    "书房里，你摊开地图，开始部署你精心策划的计划。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve

    elena "你确定要走这条路？一旦被任何一方发现，我们就是全天下的公敌。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "所以不能被发现。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "……好吧。说说你的计划。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "第一步——情报。"

    if shadow_guard_asset_revealed:
        player "影卫早就在王后内宫埋了人。她送出来的，比一支斥候营加起来都准。"
        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "兵力部署、口粮调度、贵族站位——全在这卷羊皮纸上。"
        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve

    if spy_network:
        player "我们的间谍网络已经渗透了双方阵营。利用这个优势，我们可以让双方的行动完全透明。"
        "你的间谍网络在战争中发挥了决定性作用。"
        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "情报优势是碾压性的。双方的每一步行动，我们都了如指掌。"
        $ change_stat("intrigue", 5)
    else:
        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "虽然我们没有成熟的间谍网络，但艾琳娜的个人情报能力是顶级的。"
        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "谢谢夸奖。我会尽力的。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "第二步——挑拨。"

    player "我向男爵「不小心」泄露王后军队的行军路线和薄弱环节。"

    player "同时，我向王后「善意地」提供男爵的军粮储备位置和联军内部的分歧。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "让双方都以为你在帮他们。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "第三步——消耗。"

    player "情报是错的。双方会在最不利的地形上死磕。"

    player "不管谁赢，都会元气大伤。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "第四步呢？"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "第四步——我「及时」出现，以调停者的身份终结战争。"

    player "一个在战争中保持中立、实力完整的领主，突然出现在精疲力竭的双方面前——"

    player "他们除了接受我的条件，别无选择。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "……你什么时候变得这么可怕的？"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "被逼的。"

    hide elena_img with dissolve

    "计划开始执行。"

    scene bg battlefield with dissolve
    $ unlock_gallery("bg_battlefield")

    "第一步走得异常顺利。"

    "你向男爵派出了一名信使，带着一份「无意中获得」的王后军行军路线图。"

    $ hide_all_chars("baron_img")
    show baron_img at left with dissolve

    baron "艾登堡领主果然识时务。这份情报价值连城。"

    baron "传令下去——我们在鹰隼峡设伏，打王后军一个措手不及！"

    hide baron_img with dissolve

    "与此同时，你的另一名信使正在赶往王后军营。"

    $ hide_all_chars("queen_img")
    show queen_img at left with dissolve

    queen "你是说，男爵的粮仓在溪谷镇？"

    hide queen_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "是的，王后陛下。据我的线人报告，那里只有少量守卫。"

    hide player_char_img
    $ hide_all_chars("queen_img")
    show queen_img at left with dissolve
    queen "如果我们能烧掉他的粮草……"

    queen "好。派一支骑兵去执行这个任务。"

    hide queen_img with dissolve

    $ hide_all_chars()
    "王后军的骑兵突袭了溪谷镇——但那里早已被你暗中清空。"

    "男爵的伏击圈也扑了个空——因为你提供的路线图有一个「微小的错误」。"

    "双方都没有得到预期的结果，反而在意料之外的地点遭遇了。"

    "一场混乱而血腥的遭遇战爆发了。"

    scene bg battlefield with dissolve
    $ unlock_gallery("bg_battlefield")

    "你站在远处的山丘上，用望远镜观察着战场。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve

    elena "他们打起来了。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "比预计的早了半天。男爵的先锋部队太急了。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "战况如何？"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "旗鼓相当。正是我们需要的结果。"

    $ hide_all_chars()
    "双方激战了两天。"

    "第一天傍晚——"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve

    elena "战况报告——双方各损失了约三分之一的兵力。"

    elena "男爵的骑兵在第一天的冲锋中造成了很大的伤亡，但王后军的弓箭手也给了他们沉重的打击。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "谁占上风？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "目前势均力敌。但王后军的后勤补给比男爵好——如果拖下去，男爵会先撑不住。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "那就不能让它拖下去。我们需要加速消耗。"

    menu:
        "让间谍散布男爵即将投降的假消息":
            $ change_stat("intrigue", 5)
            $ change_stat("faith", -2)  ## balance pass 修法 1: 反间计 = 谎言战术, 信仰受损
            player "让我们的人在男爵军中散布消息——说男爵已经秘密向王后求和。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "如果联军中的那些被迫加入的领主相信了这个消息——"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "他们会在战场上临阵倒戈。男爵的联军将从内部崩溃。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "同时，王后军会以为胜利在望而放松警惕。"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "正合我意。"
            $ hide_all_chars()
            "假消息像毒药一样在男爵联军中蔓延。"
            "果然，第二天的战斗中，维克托领主的部队突然撤出了战场。"
            "男爵的防线出现了巨大的缺口——但王后军也因为追击而阵型散乱。"

        "切断双方的补给线":
            $ change_stat("intrigue", 4)
            $ change_stat("power", 2)
            player "派出两支小队。一支去截断王后军的粮草运输队，另一支去毁掉男爵的补给站。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "让双方都饿着打？"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "饥饿的军队耗不起长期战斗。他们只会更疯地进攻——然后更快崩溃。"
            $ hide_all_chars()
            "你的小队完美地执行了任务。第二天，双方的士兵开始因为饥饿而变得暴躁。"
            "战斗变得更加血腥和混乱——正是你需要的。"

    hide elena_img with dissolve

    if dark_lily_joined:
        "在战斗最激烈的时候，暗百合的人悄悄执行了第二阶段的计划——"
        "他们暗杀了男爵军中的两名将领，又让王后军的补给车队「意外」迷路。"
        "双方都以为是对方的阴谋，更加疯狂地厮杀。"
        $ change_stat("intrigue", 5)

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve

    elena "双方的伤亡都很惨重。男爵损失了近一半的兵力，王后军也好不到哪里去。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "是时候了。"

    hide elena_img with dissolve

    "你下令全军出发，打着「和平调停」的旗帜向战场推进。"

    scene bg battlefield with dissolve
    $ unlock_gallery("bg_battlefield")

    "当你的军队出现在战场边缘时，筋疲力尽的双方都停止了战斗。"

    "你骑马走到两军之间，声音清晰地回荡在整个战场上——"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "够了！这场战争，到此为止！"

    player "你们看看这片土地——遍地的尸体，烧毁的村庄，破碎的家庭！"

    player "无论谁赢了这场战争，都已经输了！"

    "双方的将领面面相觑。他们已经精疲力竭，既没有力气继续战斗，也没有力气反对你。"

    menu:
        "提出一个看似公平的停战方案":
            $ change_stat("intrigue", 5)
            $ change_stat("reputation", 3)
            player "我提议——双方各退三十里。由我和教会共同主持和谈。"
            player "所有争议领地由中立方裁定归属。战俘全部释放。"
            $ hide_all_chars()
            "这个方案看着公平。其实——中立方裁定的权力在你手里。"
            "双方都太疲惫了，没有人仔细思考其中的含义。他们只想停战。"

        "直接以武力威胁迫使双方接受你的条件":
            $ change_stat("power", 3)
            $ change_stat("intrigue", 3)
            player "你们现在有两个选择——接受我的条件，或者面对我这支完整的军队。"
            player "以你们现在的状态，你们觉得谁能赢？"
            "沉默。"
            "然后，双方都不情愿地点了头。"

    "和平——或者说，你精心设计的「和平」——降临了。"

    scene black with dissolve

    "此后的日子里，你成为了王国最有影响力的人。"

    "靠的不是王冠，是情报和操控。"

    scene bg study with dissolve
    $ unlock_gallery("bg_study")

    "你的书房里多了一张新的地图——上面标注的不再是军事据点，而是你的情报网络。"

    "你的间谍遍布每一个领地、每一座教堂、每一个商队。"

    "每一个领主的秘密都在你的掌握之中。每一个商人的交易都逃不过你的耳目。"

    "没有人知道你的全部实力，但所有人都害怕你。"

    "人们在私下称你为「影中之王」。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "领主大人，今天又有三个领主送来了「礼物」。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "他们想要什么？"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "北方的贸易路线许可。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "让他们等着。越急越好。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "……领主大人越来越像一个真正的政治家了。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "这是夸奖还是批评？"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "老朽不敢妄加评论。"

    hide aldric_img with dissolve

    $ hide_all_chars()
    "十年后。"

    "你坐在书房里，面前是一份份密报。"

    "王后已经退居幕后，男爵在战争中受了重伤，不久后病逝。"

    "新一代的贵族们成长起来了——他们从出生起就活在你的阴影下。"

    "你不是国王，但你比国王更有权力。"

    "你的一句话可以让一个领主破产，一个暗示可以让一支军队调动。"

    if elena_romance:
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "你赢了。但你快乐吗？"
        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "快乐不是领主需要考虑的事情。"
        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "那作为一个人呢？"
        "风灌进窗缝发出一声低哨，你沉默了很久。"
        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "……有你在，够了。"
        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "这个答案……勉强及格。"
        "她走过来，站在你身后，轻轻地把手放在你的肩上。"
        if elena_spy_known:
            elena "你知道吗？有时候我会想——如果你不是领主，我不是间谍——"
        else:
            elena "你知道吗？有时候我会想——如果我们不是被命运安排在这个位置上——"
        elena "我们会是什么样的人？"
        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "大概会是个平凡的、快乐的人。"
        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "……是啊。但那不是我们。"
        "你们在沉默中分享着彼此的孤独。在这座权力的巅峰上，只有你们两个人。"
        hide elena_img with dissolve
    else:
        $ hide_all_chars()
        "夜深了。书房里只有你一个人。"
        "你放下密报，望向窗外。夜色沉沉，只有远处城墙上巡逻兵的火把在移动。这座你亲手编织的权力之网，在黑暗中无声运转。"
        "你赢了一切，却发现——站在巅峰的人，总是孤独的。"

    "这就是影中之王的宿命——你拥有一切，却不能让任何人知道。"

    "你的名字不会出现在史书上。但每一页历史的背后，都有你的影子。"

    $ unlock_achievement("shadow_king")
    $ persistent.endings_seen.add("shadow_king")

    jump game_ending

    ## ============================================================
    ## 结局3：圣光守护
    ## ============================================================

label ending_holy_guardian:

    $ play_music("audio/music/church_choir.ogg", fadein=2.0)
    scene bg church_interior with dissolve
    $ unlock_gallery("bg_church_interior")

    "大教堂的穹顶上，彩色玻璃窗过滤了阳光，在地面上投下五彩斑斓的光影。"

    "你和主教马修斯并肩站在祭坛前，准备执行一个前所未有的计划——"

    "以圣母的名义，阻止这场战争。"

    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve

    bishop "领主大人，教廷已经同意了我们的计划。"

    bishop "教皇亲自签发了一道敕令——任何参与这场战争的人，都将被逐出教会。"

    bishop "在这个时代，被逐出教会意味着什么，您应该清楚。"

    hide bishop_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "意味着他们的灵魂将永远得不到救赎。在这个信仰深入骨髓的时代——"

    player "这比死刑更可怕。"

    hide player_char_img
    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "没错。但我们要做的不仅仅是威胁。"

    bishop "我们要让他们明白——和平不是软弱，是一种更硬的力量。"

    hide bishop_img with dissolve

    $ hide_all_chars()

    ## 选择深度 pass R3 (2026-06-16): 教会结盟者走圣光结局——你正用杀父的那个机构换和平。
    ## round2 的 church-complicity 只在真相结局兑现, 但信仰流最常走圣光线, 这里补上反讽(无属性罚, 代价是埋掉的公道)。
    if alliance_church:
        "圣母像在烛光里低头看着你。你想起马修斯那句话——教会站出来，是替费雷恩还债。"
        "费雷恩配的那杯毒，杀了你父亲。而现在，你要借这只手去换一场和平。"
        "你父亲的公道，今天换成了和平。这笔账你自己记着，不会有第二个人替你记。"
        pause 1.0

    "你的计划分为三步。"

    "第一步——召集。以教会的名义，邀请所有参战方参加一场和平会议。"

    scene bg great_hall with dissolve
    $ unlock_gallery("bg_great_hall")

    "信使带着教皇的敕令和你的邀请函，分别前往王后军营和男爵的城堡。"

    "同时，教会的修士们开始在各地传播和平的信息。"

    "在教堂里，在集市上，在田间地头——修士们用圣母的故事来感化民心。"

    "战争的狂热在信仰的力量面前，开始慢慢降温。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "领主大人，王后和男爵都回信了。"

    captain "他们……都同意参加和平会议。虽然语气不太情愿。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "他们不情愿也得来。被逐出教会的代价，没有人承受得起。"

    hide captain_img with dissolve

    "第二步——会议。在教堂中，让双方坐下来谈判。"

    scene bg church_interior with dissolve
    $ unlock_gallery("bg_church_interior")

    "和平会议在艾登堡大教堂举行。"

    "双方的代表分坐两侧，中间隔着一张长桌。"

    "空气中弥漫着紧张的气氛。有些人的手还放在剑柄上。"

    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve

    bishop "在圣母的注视下，我们今天聚集在这里，不是为了争论谁对谁错——"

    bishop "而是为了寻找一条所有人都能接受的道路。"

    show queen_img angry at right with dissolve

    queen "主教大人，你让我和叛逆坐在同一张桌子上，这本身就是对王室的侮辱。"

    $ hide_all_chars("baron_img")
    show baron_img angry at left with dissolve

    baron "叛逆？是谁先背叛了先王的遗志？"

    "两方顿时剑拔弩张。"

    menu:
        "沉默走开":
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "……"
            "你没有动，也没有说话。"

            hide player_char_img
            $ hide_all_chars("baron_img")
            show baron_img angry at left with dissolve
            baron "（斜眼）领主大人不愿表态？那也是表态。"

            hide baron_img
            $ hide_all_chars("queen_img")
            show queen_img at right with dissolve
            queen "（冷笑）我先收剑——这一次。"

            hide queen_img with dissolve
            $ hide_all_chars()

            "男爵慢一拍，也收了剑。但他撤剑之前的目光在你身上多停了一秒。"

            "双方表面平静，但你成了作壁上观的领主。"

            $ ch5_clash_silent = True
            $ log_decision("第五章", "教堂调停: 沉默走开, 双方表面撤剑")

            jump ch5_negotiate_after_clash

        "以信仰的力量平息争端":
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "够了——"

            hide player_char_img with dissolve
            $ hide_all_chars()

            $ trigger_crisis("faith", 4,
                "你在剑拔弩张的瞬间开口, 试图用圣堂的权威压住双方。这一刻——靠的是你的话真正震慑得住人, 信仰深则有威。",
                "ch5_clash_faith_win", "ch5_clash_faith_lose",
                courage_cost=15)
            call crisis_encounter from _call_crisis_ch5_faith

            ## 退缩 fall-through (玩家临时改主意)
            "你顿住了——话到嘴边又咽了回去。"
            "主教从中调和了两句，双方表面撤剑——但你看得出，他们都没把这次平息当真。"
            jump ch5_negotiate_after_clash

        "用理性分析说服双方":
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "让我们算一笔账——"

            hide player_char_img with dissolve
            $ hide_all_chars()

            $ trigger_crisis("intrigue", 4,
                "你试图用利害分析压住激情。这一刻——靠的是你的算术真的对得上, 而且对方真的听得进去。",
                "ch5_clash_intrigue_win", "ch5_clash_intrigue_lose",
                courage_cost=15)
            call crisis_encounter from _call_crisis_ch5_intrigue

            ## 退缩 fall-through
            "你顿住了——话堵在喉咙里。"
            "主教从中调和了两句，双方表面撤剑——但你看得出，他们都没把这次平息当真。"
            jump ch5_negotiate_after_clash

label ch5_clash_faith_win:
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你们是在圣母面前！"
    player "不管你们在外面是什么身份，在这座教堂里，你们都是圣母的子民。"
    player "任何在圣堂中拔剑的人，将被永远逐出教会。"

    hide player_char_img with dissolve
    $ hide_all_chars()

    "穹顶下回响着你的话。"
    "沉默。双方的手缓缓离开了剑柄。"

    $ change_stat("faith", 12)
    $ log_decision("第五章", "信仰平息争端, 双方剑入鞘")

    jump ch5_negotiate_after_clash

label ch5_clash_faith_lose:
    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "（接住你的话）领主大人说得对。圣母在上，拔剑就是辱神——"

    hide bishop_img
    $ hide_all_chars("baron_img")
    show baron_img angry at left with dissolve
    baron "（不为所动）领主大人，圣母的话，留给那些虔诚的人吧。"

    hide baron_img
    $ hide_all_chars("queen_img")
    show queen_img at right with dissolve
    queen "（撇嘴）主教大人能让我把剑收起来——但不是你。"

    hide queen_img with dissolve
    $ hide_all_chars()

    "所幸主教从中调和，双方表面撤剑——"
    "但你看得出，他们都没把你放进眼里。"

    $ change_stat("rel_bishop", -3)
    $ crisis_injuries -= 1   ## 抵消 crisis 系统自动 +1, 决策 (i) 实施
    $ log_decision("第五章", "信仰说服未成, 主教兜底")

    jump ch5_negotiate_after_clash

label ch5_clash_intrigue_win:
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "这场战争打了十天，双方各损失了多少？"
    player "如果继续打下去，最后的结果只有一个——两败俱伤，让外敌趁虚而入。"
    player "和平对所有人都有利。这不是信仰的问题，是常识。"

    hide player_char_img with dissolve
    $ hide_all_chars()

    "数字是最有说服力的论据。"
    "双方的将领开始低声议论。"

    $ change_stat("intrigue", 3)
    $ change_stat("faith", 8)
    $ log_decision("第五章", "理性算账, 双方将领议论")

    jump ch5_negotiate_after_clash

label ch5_clash_intrigue_lose:
    $ hide_all_chars("baron_img")
    show baron_img angry at left with dissolve
    baron "（冷哼）领主大人在这种时候耍嘴皮子？"

    hide baron_img
    $ hide_all_chars("queen_img")
    show queen_img at right with dissolve
    queen "（微讽）数字解决不了血债。"

    hide queen_img with dissolve
    $ hide_all_chars()

    "你被两边同时呛回去，话堵在喉咙里。"

    "所幸主教从中调和，双方表面撤剑——"
    "但男爵看你的眼神，多了一分轻慢。"

    $ change_stat("rel_baron", -3)
    $ crisis_injuries -= 1   ## 抵消 crisis 系统自动 +1, 决策 (i) 实施
    $ log_decision("第五章", "理性辩驳未成, 男爵轻慢")

    jump ch5_negotiate_after_clash

label ch5_negotiate_after_clash:
    hide baron_img with dissolve
    hide queen_img with dissolve
    hide bishop_img with dissolve

    $ hide_all_chars()
    "谈判谈了整整三天。"

    "第一天——互相指责。"

    scene bg church_interior with dissolve
    $ unlock_gallery("bg_church_interior")

    "双方代表一坐下就开始互相指责。"

    $ hide_all_chars("noble_werner_img")
    show noble_werner_img at left with dissolve
    queen_rep "叛军必须无条件投降！这是王室的底线！"

    baron_rep "投降？王后先交出篡改遗诏的证据！"

    "眼看谈判就要破裂——"

    menu:
        "用教会的权威压住双方" if faith >= 55:
            $ change_stat("faith", 10)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "安静！在圣母的殿堂里，用这种态度说话，是对神的亵渎！"
            "你的声音在穹顶下回响。双方都不自觉地低下了头。"
            player "你们来这里是为了和平，不是为了吵架。如果只想吵架，外面的战场够大。"

        "提出一个折衷方案缓和气氛":
            $ change_stat("intrigue", 3)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "两位，我理解你们的立场。但请允许我提一个建议——"
            player "我们先不讨论谁对谁错。我们先讨论一个更基本的问题——如何停止流血。"
            $ hide_all_chars()
            "双方犹豫了一下，但最终点了头。至少，他们愿意继续谈。"

    "第二天——讨价还价。"

    scene bg church_interior with dissolve
    $ unlock_gallery("bg_church_interior")

    "你和主教一起斡旋，双方开始谈具体条件。"

    "但每一条都充满了争议——"

    "领土划分，赔偿金额，战俘处置，军队裁撤……"

    "你在两方之间来回穿梭，用尽了你所有的外交智慧。"

    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve

    bishop "领主大人，王后方坚持男爵必须解散联军。男爵方坚持王后必须退位。"

    bishop "双方的底线差得太远了。"

    hide bishop_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "那就找一个双方都能接受的中间点。"

    menu:
        "提议建立权力分享机制":
            $ change_stat("intrigue", 3)
            $ change_stat("reputation", 3)
            player "如果双方都不愿意让步——那就不要让任何一方独揽大权。"
            player "建立一个由领主、教会和王室共同组成的议政会。重大决策由多数表决。"
            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "这……这是一个前所未有的提议。"
            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "所以它也许能打破僵局。"
            "这个提议让双方都沉思了很久。不完美——可它给了双方一个保全颜面的台阶。"

        "以信仰为突破口" if faith >= 58:
            $ change_stat("faith", 12)
            player "主教大人，请宣读教廷关于战争的最新敕令。"
            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "教廷敕令——任何继续战争的人，将被逐出教会，其灵魂永堕地狱。"
            $ hide_all_chars()
            "大厅里一片死寂。在这个信仰的时代，这个威胁比任何军事力量都要可怕。"
            "双方的代表面面相觑。他们可以不怕死——但没有人不怕下地狱。"

    hide bishop_img with dissolve

    "第三天——最后的谈判。"

    scene bg church_interior with dissolve
    $ unlock_gallery("bg_church_interior")

    "经过两天的拉锯，双方都已经筋疲力尽了。"

    "你看准了时机，提出了最终的和平方案——"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "各位，这是我拟定的最终和平协议。"

    player "第一——双方立即停火，军队后撤三十里。"

    player "第二——建立由教会主持的和平委员会，处理所有争端。"

    player "第三——各领主保留现有领地，但必须宣誓效忠和平协议。"

    player "第四——设立特别法庭，调查战争中的罪行。任何一方的战犯都将受到审判。"

    player "第五——教会监督一切。任何违反协议的人，将被逐出教会。"

    $ hide_all_chars()
    "大厅里没有人说话。蜡烛芯爆了一下，溅出一粒火星。"

    "然后——"

    $ hide_all_chars("noble_werner_img")
    show noble_werner_img at left with dissolve
    queen_rep "……王后陛下可以接受这些条件。但第四条需要修改——"

    baron_rep "男爵阁下原则上同意。但需要在第三条中加入——"

    "又一轮讨价还价。但这次，方向已经明确了——和平。"

    "每一天，你都在各方之间穿梭斡旋。"

    "你用教会的权威压住双方的火气，用理性的分析打消他们的顾虑。"

    "你做出了许多让步——也迫使双方做出了让步。"

    "第三天傍晚，当最后一条条款被写下时——"

    scene bg church_interior with dissolve
    $ unlock_gallery("bg_church_interior")

    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve

    bishop "和平协议……达成了。"

    $ hide_all_chars()
    "教堂的钟声响了起来。庄严而悠远，回荡在整个城镇。"

    "外面的百姓们听到钟声，爆发出了欢呼。"

    "和平来了。"

    hide bishop_img with dissolve

    "第三步——维护和平。建立一个由教会和你共同主持的和平委员会。"

    "这个委员会负责裁决各领主之间的争端，防止战争再次爆发。"

    $ play_music("audio/music/main_theme.ogg", fadein=3.0)
    scene black with dissolve

    "此后的日子里，你成为了教会在世俗世界最重要的代理人。"

    "人们称你为「圣光守护者」。"

    "你的领地在教会的庇护下繁荣发展。穷人有面包，病人有药，孤儿有归宿。"

    "你在每个村庄建了学校，在每座城镇建了医院。"

    "战争的创伤在信仰和慈善的滋养下慢慢愈合。"

    scene bg church_interior with dissolve
    $ unlock_gallery("bg_church_interior")

    "十年后。"

    "你站在新建成的大教堂里，阳光透过巨大的玫瑰窗照进来。"

    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve

    bishop "这座教堂是您信仰的见证，领主大人。"

    hide bishop_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "这不是我一个人的功劳，主教大人。"

    hide player_char_img
    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "教廷已经决定授予您「圣光守护者」的封号。这是教会给予世俗之人的最高荣誉。"

    hide bishop_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "荣誉不是我追求的东西。我只想让这片土地上的人民能够安居乐业。"

    hide bishop_img with dissolve

    $ hide_all_chars()
    "但代价是——教会的影响力渗透到了生活的每一个角落。"

    "法律要符合教义，教育要以经文为本，商业要得到教会的许可。"

    "你有时会想，这究竟是信仰的胜利，还是另一种形式的控制。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "领主大人，有几个村民来投诉——教会的税收太重了。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "……我会和主教大人谈谈的。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "他们还说，教会不允许他们阅读教义以外的书籍。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "……"

    "这是你为和平付出的代价——你拯救了人们的身体，但是否也束缚了他们的灵魂？"

    hide aldric_img with dissolve

    if elena_romance:
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "你在想什么？"
        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "我在想——信仰是拯救，还是枷锁？"
        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "也许两者都是。就像权力一样。"
        elena "信仰本身没意义。意义在用信仰的人。"
        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "你说得对。不是靠教会——我该想办法改它。"
        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "那可是一条比战争更漫长的路。"
        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "我有时间。"
        hide player_char_img with dissolve
        show elena_img happy at left with dissolve
        "她微笑了。那个笑容让你相信——一切都值得。"
        hide elena_img with dissolve

    $ hide_all_chars()
    "圣光守护者的道路，是一条永无止境的旅途。"

    "但只要还有人在黑暗中需要光明，你就不会停下脚步。"

    $ unlock_achievement("holy_guardian")
    $ persistent.endings_seen.add("holy_guardian")

    jump game_ending

    ## ============================================================
    ## 结局4：人民领主
    ## ============================================================

label ending_peoples_lord:

    $ play_music("audio/music/castle_calm.ogg", fadein=2.0)
    scene bg castle_exterior with dissolve
    $ unlock_gallery("bg_castle_exterior")
    $ set_mood("sad")
    $ set_weather("rain", "light")

    "天刚亮的时候，城堡外的村民已经开始向这边汇集——他们听说，领主不走了。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "领主大人，您确定不参战吗？无论哪方获胜，都不会善待旁观者。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我不是旁观者。我只是选择了一个不同的战场。"

    player "我的战场不在荒野上，而是在城墙之内——保护每一个需要保护的人。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "但如果敌军来攻——"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "那我们就守。守到最后一个人。"

    hide aldric_img with dissolve

    $ hide_all_chars()
    "你下达了一系列命令——"

    "第一，加固城墙。每一块松动的石头都要重新加固。"

    "第二，储备粮食。城内的粮仓必须装满，至少能支撑三个月。"

    "第三，收容难民。所有城外的百姓，不管来自哪个领地，一律接收。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "领主大人，城外的难民越来越多了。按这个速度，我们的粮食储备——"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "把我府上的存粮也拿出来。领主吃什么，百姓就吃什么。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "可是——"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "没有可是。执行命令。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "是！"

    hide captain_img with dissolve

    $ hide_all_chars()
    "城门外，排着长长的队伍。"

    "老人、孩子、妇女、伤兵——他们拖着疲惫的身躯，带着仅有的一点家当。"

    "有些人从北方逃来，有些人从南方逃来——战争把他们从家园中连根拔起。"

    "一个抱着婴儿的年轻母亲跪在城门口。"

    $ hide_all_chars("blacksmith_wife_img")
    show blacksmith_wife_img at left with dissolve
    young_mother "大人！求求您收留我们！我的孩子……他已经两天没吃东西了……"

    menu:
        "亲自接过孩子，下令安置难民":
            $ change_stat("loyalty", 5)
            $ change_stat("reputation", 5)
            "你走到她面前，轻轻接过她怀中的婴儿。"
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "不用跪。在艾登堡，没有人需要下跪。"
            player "来人，把她们安排到暖和的地方去。给孩子找些热牛奶。"
            $ hide_all_chars()
            "年轻母亲泣不成声地感谢你。你的举动被城中的人看在眼里。"
            "那一天，你不再只是一个领主——你成了所有无家可归者的希望。"

        "下令开放粮仓，分发食物":
            $ change_stat("loyalty", 3)
            $ change_stat("wealth", -5)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "开放粮仓！每个难民一碗粥、一块面包。"
            player "安排住处——教堂、仓库、马厩——只要能遮风挡雨的地方都用上。"
            $ hide_all_chars()
            "城中迅速忙碌起来。在你的组织下，难民们被有序地安置。"

    "接下来的日子，是艰难的守城战。"

    scene bg castle_exterior with dissolve
    $ unlock_gallery("bg_castle_exterior")

    "第一支敌军出现在第七天。"

    "一支五百人的部队——不知道是王后的还是男爵的——出现在城外。"

    "他们的旗帜上满是泥土和血迹，士兵们的眼中有一种掠夺的狂热。"

    $ hide_all_chars("soldier_generic_img")
    show soldier_generic_img at left with dissolve
    commander "城中之人听着！打开城门，交出粮食和财物，我们可以不伤害你们！"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "领主大人，怎么办？"

    menu:
        "霸气回应，震慑敌军":
            $ change_stat("power", 3)
            $ change_stat("loyalty", 3)
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "告诉他们——艾登堡不接受威胁。"
            player "如果他们敢进攻，我会让他们知道什么叫做代价。"
            $ hide_all_chars()
            "你的声音从城墙上传下去，清晰而坚定。"
            "敌军的指挥官犹豫了。他看着城墙上密密麻麻的守军，做出了判断——"
            "攻城的代价太高。他们转向了别处。"

        "用外交手段化解危机":
            $ change_stat("intrigue", 3)
            $ change_stat("wealth", -3)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "派人出去谈判。给他们一些粮食——作为「过路费」。让他们走。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "给敌人粮食？"
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "不战而屈人之兵。损失一点粮食，总比损失人命好。"
            "你的策略奏效了。敌军拿了粮食后离开了——虽然不体面，但没有流血。"

    hide captain_img with dissolve

    $ hide_all_chars()
    "第九天，又有一批难民到来。这次是从南方来的——王后军经过的地方也不好过。"

    "一个受伤的男人被同伴搀扶着走进来。他的左臂缠着血迹斑斑的绷带。"

    $ hide_all_chars("soldier_generic_img")
    show soldier_generic_img at left with dissolve
    wounded_man "大人……我们村被烧了……我老婆还在里面……没出来……"

    "他说着说着就哭了。你的牙关咬紧，颊骨绷出一条线。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "不管是哪边干的——这种行为是不可饶恕的。"

    player "战争是领主之间的事。伤害百姓的军队，不配称为军队。"

    $ hide_all_chars()
    "你的话被城中的人传开了。越来越多的人开始相信——在这场战争中，只有艾登堡是安全的。"

    "第十天，城中的人口已经翻了一倍。粮食开始变得紧张。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "领主大人，按照目前的消耗速度，我们的粮食只能维持四十天了。"

    menu:
        "实行定量配给":
            $ change_stat("loyalty", 2)
            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "从今天起，每人每天定量配给。不分士兵和百姓，人人平等。"
            player "包括我在内。"
            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "领主大人也要吃一样的份量？"
            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "当然。领主和百姓同甘共苦——这才叫领主。"
            "这个决定极大地赢得了百姓的信任。人们看到领主和他们吃一样的食物，再也没有人抱怨配给不公。"

        "组织城内生产自给自足":
            $ change_stat("intrigue", 2)
            $ change_stat("wealth", 8)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "城内空地全种成快菜。妇女和老人负责加工、储存粮食。"
            player "另外，派人在夜间从城外的森林里打猎和采集。"
            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "是个好办法。产出有限，不过能多撑几天就多撑几天。"

    hide aldric_img with dissolve

    $ hide_all_chars()
    "第十一天，城里出现了一个感人的场景——"

    "一群孩子自发地组成了「小小搬运队」，帮忙把物资从仓库搬到各个分发点。"

    "最小的孩子只有五六岁，却一脸严肃地抱着两个面包跑来跑去。"

    "一个白发老妪坐在城墙下，为受伤的士兵缝补衣物。她的眼睛已经不太好了，但手中的针线依然稳健。"

    "一个失去了一条腿的退伍老兵，拄着拐杖在城墙上巡逻。他不能战斗，但他能看到远方的敌人。"

    "你看着这些人，心中充满了力量。"

    "这就是你要守的——这些人。墙塌了能再砌，人没了就真没了。"

    "第十二天，第二支敌军出现。这次是一千人的大部队。"

    "他们不打算谈判——直接开始攻城。"

    scene bg castle_exterior with dissolve
    $ unlock_gallery("bg_castle_exterior")

    "攻城战打了三天。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "领主大人！西墙告急！他们搭起了云梯！"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "调预备队去支援！弓箭手压制云梯下的士兵！"

    $ hide_all_chars()
    "你在城墙上来回奔跑，指挥防御。箭矢从你耳边呼啸而过。"

    "第一天，你击退了四次进攻。"

    "第二天，你击退了六次进攻。城墙上开始出现裂缝。"

    "第三天——"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "领主大人！他们撤了！"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "什么？"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "他们撤退了！"

    $ hide_all_chars()
    "你从城垛上探出头去。敌军确实在撤退——匆忙而混乱。"

    "原来，战场上的形势发生了变化。另一支军队在他们的后方出现，迫使他们不得不撤退。"

    hide captain_img with dissolve

    "艾登堡保住了。"

    "但城中的物资已经消耗了大半。接下来的日子将更加艰难。"

    "你组织城里的百姓自己种、自己收——"

    "在城墙内开辟菜地，用城堡的水井保证饮水，把每一粒粮食都精确分配。"

    "这场仗打的不是地盘，是命。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "领主大人，粮食还能支撑一个月。但如果战争持续更久——"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "一个月就够了。只要我们撑过这个月，双方的大军都会精疲力竭。"

    player "到那时候，和平自然会来。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "您的意思是——让他们打，我们守？"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "正是如此。在这场战争中，最后站着的人不一定是打赢了的人——"

    player "而是熬到了最后的人。"

    hide aldric_img with dissolve

    $ hide_all_chars()
    "你击退了每一支试图劫掠你领地的军队——无论他们举着谁的旗帜。"

    "在你的城墙之下，有被你收留的王后军逃兵，也有男爵联军的伤兵。"

    "在这里，没有阵营之分——只有需要保护的人。"

    $ play_music("audio/music/hope.ogg", fadein=3.0)
    scene black with dissolve

    "战争最终结束。没人赢——所有人都打不动了。"

    "当和平降临时，人们发现——整个北方只有一个领地没有被战火摧毁。"

    "艾登堡。"

    scene bg castle_exterior with dissolve
    $ unlock_gallery("bg_castle_exterior")

    "流民涌入你的领地。商人在你的城堡下安家。你的集市成为了地区最繁忙的贸易中心。"

    "你用收容难民时建立的分配系统来管理越来越多的人口。"

    "你把空闲的土地分给了失去家园的农民，让他们重新开始生活。"

    "你组织匠人修建了新的房屋、道路和水渠。"

    "慢慢地，艾登堡从一个小小的领地，变成了北方最繁荣的城镇。"

    "人们不叫你领主。他们叫你「父亲」。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "领主大人，今天又有一批新的移民到来了。"

    aldric "他们来自南方——听说了您的仁德，不远千里而来。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "安排住处和工作。每个人都要有事做——闲着会出问题。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "是。另外——城中的长老们想为您立一座铜像。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "不需要。把那些钱用来修桥。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "……是。"

    hide aldric_img with dissolve

    $ hide_all_chars()
    "十年后。"

    "艾登堡已经不再是一个领地——它是一个小小的国度。"

    "你制定的法律保护每一个人——无论贫富贵贱。"

    "你建立的学校让每一个孩子都有机会读书识字。"

    "你修建的道路连接了周围所有的村庄和城镇。"

    "在你的治下，人们不需要担心战争、饥荒和压迫。"

    if elena_romance:
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "你放弃了一切野心，却得到了最珍贵的东西。"
        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "是什么？"
        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "人心。"
        "你看着窗外繁忙的集市，听着孩子们的笑声。"
        "你笑了一下。"
        hide elena_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "后悔吗？"
        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "从来没有。"
        "她靠在你的肩上，微笑着看着这片你们共同守护的土地。"
        hide elena_img with dissolve
    else:
        $ hide_all_chars()
        "你站在城楼上，看着脚下这座繁荣的城镇。"
        "孩子们在街道上奔跑嬉戏，商人们在集市上讨价还价，农民们在田间劳作。"
        "你选择的「胜利」是守护。"

    "人民领主的故事，成为了这片土地上最动人的传说。"

    "几百年后，当人们谈起那场战争时，他们不记得谁赢了、谁输了——"

    "他们只记得，有一个领主，在所有人都想着争权夺利的时候，选择了保护自己的百姓。"

    $ unlock_achievement("peoples_lord")
    $ persistent.endings_seen.add("peoples_lord")

    jump game_ending

    ## ============================================================
    ## 结局5：真相大白（最佳结局）
    ## ============================================================

label ending_truth:

    $ play_music("audio/music/tension.ogg", fadein=2.0)
    scene bg study with dissolve
    $ unlock_gallery("bg_study")

    "真相不能贸然公布。你需要做充分的准备。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve

    elena "你确定要这么做？一旦公布真相，就没有回头路了。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "正义等了二十年。不能再等了。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "好。那我们需要一个完美的计划。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "首先——我们需要确保遗诏的真实性无可争议。"

    if dark_lily_joined:
        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "暗百合已经帮我们鉴定了遗诏的真伪。"
        elena "羊皮纸的年代、墨水的成分、印章的蜡封——全部与二十年前的记录吻合。"
        elena "此外，首领还提供了一份当年参与篡改遗诏的人员名单。"
        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "这些人现在在哪里？"
        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "大部分已经不在了。但有三个人还活着——其中一个就在我们的控制之下。"
        $ change_stat("intrigue", 5)
    else:
        elena "我已经找到了一个当年的目击者——一个老修士。"
        elena "他年事已高，但记忆清晰。他愿意作证。"

    hide elena_img with dissolve

    $ hide_all_chars()
    "你的计划是这样的——"

    "在两军交战之前，以「紧急和谈」的名义召集所有关键人物。"

    "然后，在所有人面前公布真相。"

    "这个计划的关键在于——你必须让真相本身的力量足以压倒所有的反对。"

    scene bg great_hall with dissolve
    $ unlock_gallery("bg_great_hall")

    "你给所有相关方都发出了邀请——以「避免战争」为由。"

    "王后没有派代表，而是亲自来了——这种动摇国本的事，她不放心交给任何人。她要亲眼看着，亲手压下去。男爵亲自出席，教会派来了主教。"

    "还有各地的领主、商人和百姓代表。"

    "大厅里坐满了人。空气中弥漫着紧张和期待。"

    scene bg throne_room with dissolve
    $ unlock_gallery("bg_throne_room")

    "你站在大厅的中央，环顾四周。"

    "所有的目光都集中在你身上。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "感谢各位的到来。我知道你们中的很多人正急着去战场。"

    player "但在那之前，有一件事必须先解决。"

    player "这件事关系到这场战争的根源——也关系到这个王国二十年来的真相。"

    "大厅里一片窃窃私语。"

    $ hide_all_chars("queen_img")
    show queen_img at left with dissolve

    queen "你想说什么？"

    hide queen_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "王后陛下，我想说的是——"

    "你从怀中取出那份尘封二十年的羊皮纸，在所有人面前展开。"

    player "这是先王的遗诏。{b}真正的遗诏{/b}。"

    "大厅里瞬间安静了。"

    player "上面写着——先王指定的摄政人选不是伊莎贝拉王后——"

    player "而是我的父亲，艾登堡的老领主。"

    "一片哗然。"

    hide player_char_img
    $ hide_all_chars("queen_img")
    show queen_img at left with dissolve
    queen "一派胡言！这是伪造的！卫兵——"

    menu:
        "用证据一步步击溃王后的辩驳":
            $ change_stat("intrigue", 5)
            hide queen_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "王后陛下，请容我把话说完。"
            player "如果这是伪造的，那么请解释——为什么这份羊皮纸上的印章，"
            player "与先王的私印完全吻合？为什么墨水的成分与二十年前的官方文书一致？"
            "你一件一件地拿出证据。每一件都像一把刀，插进王后精心维护了二十年的谎言中。"
            if poison_evidence:
                player "更重要的是——我手中还有另一份证据。"
                player "关于「暮色之露」。"
                "大厅里再次安静了。有些人的脸色开始发白。"
                player "我的父亲不是病死的。他是被人用「暮色之露」——一种罕见的毒药——毒杀的。"
                player "因为他发现了遗诏被篡改的真相。"
                hide player_char_img
                $ hide_all_chars("queen_img")
                show queen_img at left with dissolve
                queen "你……你有什么证据——"
                hide queen_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "证据就在这里。"
                $ hide_all_chars()
                "你拿出了毒药的鉴定报告、购买记录，以及一个证人的书面证词。"
                "每一份都是铁证。"

        "用道义压力迫使真相浮出水面" if faith >= 55:
            $ change_stat("faith", 10)
            $ change_stat("reputation", 5)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "王后陛下，我没有必要伪造这样的东西。"
            player "如果我想的是权力，我有一百种更简单的方法。"
            player "我公布真相，是因为我的父亲为此付出了生命。二十年了。"
            player "一个儿子为父亲讨回公道——这有什么错吗？"
            $ hide_all_chars()
            "你的话语击中了在场每一个人的心。许多人的脸上露出了同情的表情。"
            "王后的反驳在这种道义压力面前，显得苍白无力。"

    "大厅里的气氛已经完全转变了。"

    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve

    if poison_evidence:
        hide bishop_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "主教大人，「暮色之露」——这个名字你应该不陌生吧？"
        "主教的脸色惨白。他的手在发抖。"
        hide player_char_img
        $ hide_all_chars("bishop_img")
        show bishop_img at left with dissolve
        bishop "我……我只是服从命令……"
        hide bishop_img
        $ hide_all_chars("queen_img")
        show queen_img at left with dissolve
        queen "闭嘴！"
        hide queen_img
        $ hide_all_chars("bishop_img")
        show bishop_img at left with dissolve
        bishop "不……我不能再沉默了。"
        bishop "二十年了。二十年来我每天都在向圣母忏悔——"
        bishop "是的。遗诏是被篡改的。老领主是被毒杀的。我……参与了。"
        "教堂里爆发了巨大的喧哗。"
        if alliance_church:
            ## R2 延迟兑现: ch4 与教会结盟时马修斯说过"这笔账干净不到哪里去"。现在当众摊开——你的盟友是共犯。
            "你站在原地，没动。这个低着头认罪的人，是你亲手请进来的盟友。"
            "你接住教会支持的那天就被告知过：这笔账干净不到哪里去。现在它当着满堂的人摊开了。"
            "你父亲的血，有一份就在你此刻盟友的手上。"
            $ change_stat("reputation", -6)
        $ change_stat("faith", 12)
    else:
        hide bishop_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "主教大人，你是否愿意在圣母面前发誓，你对此一无所知？"
        $ hide_all_chars()
        "主教低下了头。"
        "漫长的沉默。"
        "然后——"
        hide player_char_img
        $ hide_all_chars("bishop_img")
        show bishop_img at left with dissolve
        bishop "……我不能发这个誓。因为我的灵魂承受不了更多的谎言。"
        "他的沉默和坦白，就是最响亮的证词。"

    hide bishop_img with dissolve

    ## 王子盟友路线的隐形好感预警：议会抉择前的侧笔，提示玩家当前王子心态
    if prince_ally and not prince_betrayed:
        if rel_prince < 25:
            "议会召开前夕，你托人给王子捎了口信。"
            "来人带回的只有一句话：「他听完了。」"
            "他听完了。没别的。"
        elif rel_prince < 40:
            "你最近一次见到王子，是在一场酒宴的远处角落。"
            "他朝你举了举杯，然后转过头去和别人说话。"
            "那杯酒他没喝完。"

    if prince_ally and not prince_betrayed:
        "你没料到他会出现在这里——一个本该被软禁在王宫里的人。"
        "战事当前，王宫的守卫和耳目大半调去了别处。对一个隐忍十二年、早把人脉铺到宫墙之外的人，这点缝隙足够了。"
        ## 好感度过低：王子被迫反水
        if rel_prince < 25:
            call ch5_prince_betrayal from _call_ch5_prince_betrayal
        else:
            ## 好感度足够：王子站出来对抗王后
            call ch5_prince_confronts_queen from _call_ch5_prince_confronts

    $ hide_all_chars("queen_img")
    show queen_img at left with dissolve

    $ hide_all_chars()
    "大厅里的空气仿佛凝固了。所有人都看向王后，等待她的反应。"

    "但伊莎贝拉王后没有崩溃。她甚至没有慌张。"

    "她缓缓站起身来，环顾大厅，目光扫过每一张面孔——那是一个统治了二十年的女人才有的目光。"

    $ hide_all_chars("queen_img")
    show queen_img at left with dissolve
    queen "说完了？"

    "她的声音平静得令人不寒而栗。"

    queen "那现在轮到我说了。"

    queen "是的。遗诏是我改的。"

    "大厅里一片哗然，但王后抬起一只手，所有的声音都压了下去。二十年的积威，不是一朝一夕能消散的。"

    queen "先王驾崩时，北方蛮族兵临城下，国库空虚，三个公爵在密谋瓜分国土。"

    queen "先王选的摄政人选是谁？一个连自己领地的税都收不齐的人。"

    queen "你们觉得他能撑过那一年吗？"

    "她看向你，目光如刀。"

    queen "你的父亲是个好人。我从不否认。但好人不一定是能拯救这个国家的人。"

    queen "我改了遗诏。我接过了这个烂摊子。"

    queen "然后呢？北方蛮族击退，三个公爵瓦解。边境二十年没有战火——国库也从空虚到充盈。"

    queen "这些——是谁做到的？"

    "大厅里一阵骚动。不少人的表情变得复杂起来——因为她说的是事实。"

    queen "至于毒杀……"

    "她的目光闪过一丝几不可察的阴影，但很快恢复了冷静。"

    queen "你的父亲发现了真相，要把它公之于众。我劝过他——给我时间，等局势稳定下来，我会把权力交还。"

    queen "他不听。"

    queen "如果真相在那时候泄露，你们猜会发生什么？三个公爵会立刻起兵，蛮族会趁机南下，无数人会死在战火里。"

    queen "我选择牺牲一个人，来换整个王国的安宁。"

    "她的声音终于带上了一丝疲惫，但仍然没有崩溃。"

    queen "你说我是罪人。也许是。但这个王国里的每一个人——包括你——都活在我这个「罪人」撑起来的和平里。"

    "你不得不承认，她的反击比你预想的要有力得多。"

    menu:
        "用逻辑反驳——和平不是杀人的借口":
            $ change_stat("reputation", 5)
            $ change_stat("intrigue", 3)
            hide queen_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "王后陛下的政绩，没有人否认。"
            player "但我想请问——如果任何人都可以用「为了大局」来杀人，那法律还有什么意义？"
            player "今天你为了王国杀了我父亲。明天别人也可以为了「大局」杀你。后天呢？"
            player "如果这个先例被允许，那在座的每一位——你们谁能保证自己不会成为下一个「必要的牺牲」？"
            $ hide_all_chars()
            "你的话像一盆冷水泼在了那些开始动摇的人脸上。"
            "几个领主交换了眼神，缓缓点了头。"

        "承认她的功绩，但要求以法律裁决":
            $ change_stat("reputation", 3)
            $ change_stat("loyalty", 5)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "王后陛下，我不否认你的功绩。这二十年的和平，有你的心血。"
            player "但我的父亲也是一个为了王国甘愿付出一切的人。他不该死得不明不白。"
            player "我不是来复仇的。我是来让真相回到它该在的地方。"
            player "至于功过——让法律和历史来评判。不是你，也不是我。"

        "提出谈判——给她一条体面的退路" if intrigue >= 45:
            $ change_stat("intrigue", 8)
            $ change_stat("power", -3)  # 谈判让步, 权力没拿满
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "王后陛下，你说得对。你确实为这个国家付出了很多。"
            player "所以我不想把事情做绝。"
            player "你可以选择体面地退位。保留王太后的尊号，保留你的私产。"
            player "但权力——必须交还。真相——必须公开。"
            player "这是我能给你的最好的条件了。"
            "王后的眼睛微微眯了起来。你看得出她在飞速计算着利弊。"

        "要求严惩——正义不能打折":
            $ change_stat("power", 5)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "够了，王后。你的功绩不能为你赎罪。"
            player "篡改遗诏是叛国。毒杀忠良是谋杀。无论动机如何，罪就是罪。"
            player "在场的各位是见证人——今天，正义不会再缺席。"

    $ hide_all_chars()

    python:
        ## 困难模式 + 声望/铁证不足 → 真相压不住一个掌权二十年的王后, 只能靠强硬手段惨胜。
        ## (2026-06-16 秦霸先反馈: 真相大白是唯一不吃难度的主结局, 困难一次过。
        ##  普通/简单仍走干净胜利, 不锁玩家; 仅困难下根基不够时付代价。)
        _truth_weight = reputation + intrigue // 2
        if poison_evidence:
            _truth_weight += 20
        if prince_ally and not prince_betrayed and rel_prince >= 25:
            _truth_weight += 20
        if dark_lily_joined:
            _truth_weight += 10
        _truth_contested = (persistent.difficulty == "hard" and _truth_weight < 85)

    if _truth_contested:
        "王后没有立刻屈服。"

        "她环顾大厅，去找那些还没有低头的人——而她找到了几个。"

        "「老领主的冤屈该查。可蛮族就压在边境上，这个节骨眼上动摇王后，谁来收场？」北境一位领主开了口，附和声跟着响起来。"

        "你压不住这股动摇。光靠一份二十年前的遗诏，撼不动一个掌权二十年的人。"

        "你只能把话说重——点名那几个收过王后好处的领主，把当年的旧账一笔笔翻出来，逼他们把嘴闭上。"

        "大厅安静了下来。你赢了，可赢得难看。在场的人都记住了你逼人就范的那副样子。"

        $ change_stat("reputation", -8)
        $ change_stat("loyalty", -4)
    else:
        "王后沉默了很长时间。"

        "她的目光掠过大厅里的每一张脸——她在寻找支持者。"

        "但她看到的只有回避的目光和低下的头。二十年的恩威并施，在铁证面前轰然崩塌。"

    hide player_char_img
    $ hide_all_chars("queen_img")
    show queen_img at left with dissolve
    queen "……"

    $ hide_all_chars()
    "她重新坐回王座。这次坐得端正，背挺得直。"

    "就像她这二十年来每一天做的那样。"

    $ hide_all_chars("queen_img")
    show queen_img at left with dissolve
    queen "我不会求饶。求饶不是伊莎贝拉做的事。"

    queen "但我有一个条件。"

    queen "不管你们怎么处置我——不要牵连弗雷德里克。他什么都不知道。"

    queen "这一切，从头到尾，都是我一个人的决定。"

    $ hide_all_chars()
    "即便在最后一刻，她想的仍然不是自己。"

    "你不禁对这个女人生出了一种复杂的情绪——恨不起来，也原谅不了。"

    $ hide_all_chars("queen_img")
    show queen_img at left with dissolve
    queen "裁决吧。"

    "她的声音平静如水。没有眼泪，没有哀求。一个政治家最后的尊严。"

    hide queen_img with dissolve

    ## ============================================================
    ## 月光疾风反馈 v3.12: 王后自请退位分支
    ## 条件 rel_queen >= 50 + prince_ally 且 not prince_betrayed
    ## "王后也不是十恶不赦之人，结局应该让她自己放下"
    ## ============================================================
    if rel_queen >= 50 and prince_ally and not prince_betrayed:
        $ play_music("audio/music/sad.ogg", fadein=2.0)
        scene bg study with dissolve

        "那天夜里，宫廷大殿熄了灯。"

        "你独自坐在书房里——等一个没人通报、却注定会来的人。"

        "门外脚步声轻而稳。"

        $ hide_all_chars("queen_img")
        show queen_img at left with dissolve
        queen "我可以坐下吗？"

        hide queen_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "请。"

        hide player_char_img
        $ hide_all_chars("queen_img")
        show queen_img at left with dissolve
        queen "白天我说「裁决吧」——那是说给所有人听的。"

        queen "现在没有别人。我想和你单独谈一次。"

        $ hide_all_chars()
        "她在你对面坐下。蜡烛在你们之间的桌面上烧得很低。"

        "你没有让仆人添。这种话不需要更多的光。"

        $ hide_all_chars("queen_img")
        show queen_img at left with dissolve
        queen "你父亲本该是摄政王。这件事我知道了二十年。"

        queen "格雷芬七世走得不安稳——这件事，也是我让的。"

        queen "下毒的命令不是我下的，但我知道是谁。我没有制止。"

        $ hide_all_chars()
        "她没有为自己辩解。也没有要求宽恕。"

        "你听着，没有打断。"

        $ hide_all_chars("queen_img")
        show queen_img at left with dissolve
        queen "我以为我做的一切，都是为了弗雷德里克。"

        queen "今天下午，他来找过我。"

        queen "他说——「母亲，我已经长大了。你不需要再为我流血了。」"

        queen "他说这句话的时候，看着我的眼睛。"

        queen "我以为这二十年是在替他扫干净路。"

        queen "他不需要了。"

        $ hide_all_chars()
        "你没有说话。沉默就是最沉重的回答。"

        $ hide_all_chars("queen_img")
        show queen_img at left with dissolve
        queen "明早的朝会上，我会自请退位。"

        queen "南方有一座修道院。我母亲临终前在那里住过几年。"

        queen "我想去那里——不是流放，是去把这条命过完。"

        hide queen_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "您不必先来跟我说一声。新王不会拒绝，您也清楚。"

        hide player_char_img
        $ hide_all_chars("queen_img")
        show queen_img at left with dissolve
        queen "你知道为什么我要先来跟你说？"

        queen "因为这一座修道院，二十年前，我也对你父亲提过。"

        queen "我说——「如果你执意要公布那份遗诏，就让我去那里，从此不问朝政。」"

        queen "他笑了。他说，「好。」"

        queen "可第二天他就死了。"

        $ hide_all_chars()
        "你身体一震。"

        "你以为你已经听过这个故事的所有版本——但你没有。"

        $ hide_all_chars("queen_img")
        show queen_img at left with dissolve
        queen "二十年了。每一年，我都对自己说： 明年我就放下。"

        queen "明年。明年。"

        queen "现在不能再骗自己了。"

        queen "对不起。"

        hide queen_img with dissolve

        $ hide_all_chars()
        "她起身的时候没有回头。"

        "门关上的那一刻，你听见走廊那一头有人在轻声啜泣——"

        "是弗雷德里克。"

        "他一直站在门外。"

        pause 1.5

        $ change_stat("faith", 5)
        $ change_stat("intrigue", 5)
        $ change_rel("rel_queen", 10)
        $ queen_reconciled = True

    ## ============================================================
    ## /月光疾风分支结束
    ## ============================================================

    $ play_music("audio/music/coronation.ogg", fadein=3.0)
    scene black with dissolve

    "真相大白的那天，整个王国都震动了。"

    "消息像野火一样传遍了每一个角落。"

    "人们在街头巷尾议论着——二十年的谎言，终于被揭穿了。"

    if queen_reconciled:
        "伊莎贝拉王后并未被公审。"

        "她在退位诏书上签下自己的名字，然后离开王都，去南方修道院静修。"

        "人们说，她临走前没有带走任何东西，只在桌上留下一封信——"

        "信里只有一句话： 「若有人问起王后，就说她终于学会了，一个母亲该如何停下来。」"

        "参与篡改遗诏和毒杀老领主的同谋仍被一一审判——这场清算，谁都不能替谁承担。"
    else:
        "伊莎贝拉王后退位。参与篡改遗诏和谋杀的人被一一审判。"

    if prince_ally and not prince_betrayed:
        "弗雷德里克王子登基为新王。"
        "他在加冕典礼上说的第一句话是——"
        "「这个王国不会再建立在谎言之上。」"

        "他随即下令重铸国玺。王历自这一年起重新计数——格里菲斯朝的两百七十三年，到此为止。"
    else:
        "在领主们的推举下，一个摄政委员会被建立起来，暂时治理国家。"

        "委员会的第一项决议是重铸国玺、重启王历——格里菲斯朝的两百七十三年，到此为止。"

    "而你，作为揭露真相的人，被封为公爵——王国除国王外最高的爵位。"

    "你的父亲终于得到了迟来的正义。"

    scene bg palace_garden with dissolve
    $ unlock_gallery("bg_palace_garden")
    $ play_music("audio/music/dawn.ogg", fadein=3.0)

    "春天。花园里的花终于开了。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "领主大人……不，公爵大人。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "奥尔德里克，别叫我公爵。那太生分了。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "是……领主大人。"

    "老管家的眼眶湿润了。这个服侍了两代领主的老人，终于看到了正义的降临。"

    aldric "老领主在天之灵，一定会为您骄傲的。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "奥尔德里克，这不是我一个人的功劳。"

    player "你守护了这个家族三十年。没有你，就没有今天。"

    player "谢谢你一直守在我身边。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "领主大人……"

    "老管家终于没有忍住，泪水顺着布满皱纹的脸颊流了下来。"

    aldric "能看到这一天……老朽此生无憾了。"

    hide aldric_img with dissolve

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    if prince_ally and not prince_betrayed:
        captain "公爵大人，新王殿下派人来了。他想请您担任王国的首席顾问。"

        hide captain_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "首席顾问？"

        hide player_char_img
        $ hide_all_chars("captain_img")
        show captain_img at left with dissolve
        captain "是的。新王说——「这个王国需要一个敢说真话的人。」"

        hide captain_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "……让我想想。"
    else:
        hide player_char_img
        $ hide_all_chars("captain_img")
        show captain_img at left with dissolve
        captain "公爵大人，摄政委员会来函了。他们推举您担任首席摄政官。"

        hide captain_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "首席摄政官？"

        hide player_char_img
        $ hide_all_chars("captain_img")
        show captain_img at left with dissolve
        captain "是的。委员会说——「没有比您更合适的人选了。」"

        hide captain_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "……这是一份沉重的责任。让我想想。"

    hide captain_img with dissolve

    menu:
        "接受任命——你的责任不止艾登堡":
            pass

        "婉拒——回艾登堡守护领地与人民":
            jump truth_humble_epilogue

    if elena_romance:
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "一切都结束了。"
        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "不。一切才刚刚开始。"
        "你握住她的手。这次是阳光下，上次在黑暗的花园里。"
        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "你打算接受新王的邀请吗？"
        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "你觉得呢？"
        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "我觉得……你注定是要做大事的人。"
        elena "但不管你做什么决定，我都会在你身边。"
        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "那你的回答就是我的回答。"
        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "……笨蛋。"
        $ hide_all_chars()
        "但她笑了。那个笑容比春天的花更灿烂。"
        "春天来了。新的故事正在开始。"
        hide elena_img with dissolve
    else:
        "你站在花园里，感受着春风拂面。"
        "二十年前种下的那颗种子，终于开花结果了。"
        "你的父亲可以安息了。"
        "而你——还有一个王国等着你去守护。"

    "真相大白。正义实现。"

    "但你知道——在这个世界上，真相从来都不是终点。"

    "它是一个新的起点。"

    "一个更好的、建立在真相而非谎言之上的未来——正从你脚下展开。"

    $ unlock_achievement("truth_ending")
    $ persistent.endings_seen.add("truth")

    jump game_ending

label truth_humble_epilogue:

    $ truth_declined_regency = True

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "您想好了？"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "替我回信——谢绝任命。真相大白之后，我答应过自己，要回艾登堡。"

    player "王都需要的是新的政治家，不是我。"

    player "父亲守了艾登堡一辈子。我也想守它一辈子。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "……明白了，领主大人。"

    "雷恩没有再多劝。他知道你下了决心就改不回来了——这一点你和老领主一模一样。"

    if elena_romance:
        hide captain_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "你不留在王都？"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "我属于艾登堡。"

        player "你呢？"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "我属于你在的地方。"

        $ hide_all_chars()
        "她笑了。这笑容里没有花园里的算计，没有王都里的伪装——只有春风。"
    else:
        hide captain_img
        $ hide_all_chars()
        "你独自站在窗前，望着远方。"
        "王都的事让王都的人去办。艾登堡有它自己的春天要等。"

    scene bg castle_exterior with dissolve

    "你回到艾登堡那天，全城的人都在城门口等你。这一次，他们的笑容是真的。"

    "你没有公爵的仪仗，也没有摄政官的金印。只有奥尔德里克手里那本翻烂了的领地账册，和雷恩腰间那把守了三代领主的剑。"

    "夏天，村庄的麦子熟了。"

    "秋天，城墙上的裂缝补好了。"

    "冬天，大雪封山——你和老人们围着炉火，听他们讲老领主年轻时的故事。"

    "春天，一个孩子在城门口拉住你的衣角，问你能不能讲讲那只金鹰的故事。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "好。给我一杯热茶——这故事很长。"

    $ hide_all_chars()
    "真相大白。正义实现。"

    "你没有去做帝国的轴心——你只是回来了。"

    "回到一个真正属于你的地方。"

    $ unlock_achievement("truth_ending")
    $ persistent.endings_seen.add("truth")

    jump game_ending

    ## ============================================================
    ## 结局：毒药公爵 (波吉亚式坏结局, batch 6 #4)
    ## ============================================================
    ## 触发: deep_mother_herb == "poison" + intrigue >= 70 + poison_evidence
    ## 玩家从童年就对毒感兴趣, 累积谋略和毒药知识, 最终用母亲教过的方式
    ## 收场——但代价是变成自己最初故事里"那个王后"
    ## ============================================================

label ending_borgia:

    $ play_music("audio/music/conspiracy.ogg", fadein=2.0)

    scene black with fade
    pause 0.8
    centered "{size=+10}毒药公爵{/size}"
    pause 1.5

    ## ── 第一幕：花园重启 ──
    scene bg castle_garden with dissolve

    "夜色降临艾登堡。你独自走进城堡西侧那片荒废多年的花园。"

    "母亲死后， 这里就再没有人打理。但你记得每一株药草的位置——母亲教过你， 你从未忘。"

    "深蓝色的狼毒草还在角落里。它居然活下来了， 二十多年。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "母亲——你当年没说完的那句『除非』， 我自己想明白了。"

    player "除非， 是你不想再忍了的时候。"

    $ hide_all_chars()
    "你蹲下来， 用一把小刀挖出狼毒草的根。"

    "你不打算再让花园荒废。它会成为艾登堡最重要的房间——不在城堡里， 而是在所有人都看不见的地方。"

    ## ── 第二幕：第一杯酒 ──
    scene bg royal_palace with dissolve
    pause 0.4

    "三个月后。王都。"

    "王后召你觐见， 设了私宴。她想拉拢你——以为你跟她父辈一样， 是可以用名利驯服的小领主。"

    $ hide_all_chars("queen_img")
    show queen_img at left with dissolve
    queen "孩子， 喝一杯。这是南方进贡的红酒， 普通人这辈子尝不到。"

    hide queen_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "陛下美意， 臣岂敢推辞。"

    "你举起酒杯， 跟她碰了一下。两杯酒看起来一模一样。"

    "你母亲教过你——把毒下在自己的杯子里， 别人就永远不会怀疑。然后在敬酒的瞬间， 用袖口盖住交换。"

    "这是六岁那年她讲给你的故事里没说出口的最后一句。"

    $ hide_all_chars()
    "三个月后， 王后开始头痛。两个月后， 她起不了床。"

    "王宫上下都说陛下是悲伤过度——毕竟她最近失去了好几个心腹近臣， 都是同样的「急病」。"

    "只有你知道， 这只是开始。"

    ## ── 第三幕：清单上的名字 ──
    scene bg study with dissolve

    "一年里， 你列了一张清单。"

    "上面有费雷恩的余党、教会的暗焰、男爵的死忠、还有那些当年知道你父亲死因却选择沉默的人。"

    "你不需要打仗。你只需要在合适的宴席上递上一杯合适的酒。"

    if rel_aldric >= 50:
        $ hide_all_chars("aldric_img")
        show aldric_img at left with dissolve
        aldric "领主大人……您手上的这种东西， 我父亲那一辈见过。下场都不太好。"

        hide aldric_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "我知道。但我不会让你看到那种下场。"

        player "你也不必看见今晚之后我做的任何事。"

        $ hide_all_chars()
        "奥尔德里克沉默了很久。然后他把书房的钥匙留在桌上， 转身走了。"

        "第二天他递交了辞呈。理由是身体不适， 想回家种花。"

        "你批了。你给他一笔够他过完后半辈子的银子。"

        "你知道他不是怕你。是不愿意目睹你变成什么样子。"

        $ change_rel("rel_aldric", -30)

    if elena_romance:
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "你以为我没看出来？"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "……"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "我父亲死在这种东西手里。我以为， 我跟着你， 是为了让世上少一条这样的命。"

        elena "可你——你成了用它的人。"

        "她没有大声。她只是看着你， 像看着一个她以为认识但其实不认识的人。"

        elena "我不能跟一个会下毒的人睡在同一张床上。"

        "她那天夜里离开了艾登堡。没有告诉你她去哪。"

        "你没有阻拦。你也没有派人去找。"

        $ change_rel("rel_elena", -50)

    ## ── 第四幕：登顶 ──
    scene bg throne_room with dissolve
    pause 0.5

    "三年后。"

    "王国大半的旧贵族悄悄消失了——有的「病死」， 有的「意外」， 有的「失踪」。每一桩看似都跟你无关。"

    "新王登基那天， 国玺由你亲手递上。"

    "弗雷德里克王子年轻， 信任你。议会里能反对你的老臣， 早就一个接一个进了你的清单。"

    "他给了你一个新爵位——『公爵』。"

    "也是这个国家除国王之外最高的爵位。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "陛下圣明。"

    "你跪下接旨。声音平稳得听不出任何情绪。"

    $ hide_all_chars()
    "没有人怀疑你。因为每一个开始怀疑你的人， 都没活到下一个春天。"

    ## ── 第五幕：终局 ──
    scene bg castle_garden with dissolve
    pause 0.5

    "五年后。"

    "你五十岁出头， 但看起来更老。头发大半白了。"

    "你独自坐在母亲的花园里。这里现在是整个公爵府最隐秘的地方——没有侍从能进， 包括你最信任的那几个。"

    "因为最信任的那几个， 已经死了。"

    "不是别人下手。是你。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "母亲。"

    player "我现在懂你那个故事的最后一句了。"

    player "故事里那个王后， 她不是赢了。她只是——再也无法相信任何人。"

    $ hide_all_chars()
    "你抬头看夜空。狼毒草的花在月光下泛着深紫色， 跟二十多年前一模一样。"

    "你坐在那里很久。然后从怀中掏出一个紫色的小瓶——「暮色之露」的最后一瓶。"

    "你看着它， 像看一个老朋友。"

    "夜风掠过花园， 带着药草的气味。母亲生前最后一次抱你的时候， 身上就是这种味道。"

    pause 1.0

    scene black with fade
    pause 1.5

    centered "{size=+8}你成了你母亲故事里的那个王后{/size}"

    pause 2.0

    centered "{size=+6}「能保护你的人， 只有你自己。」{/size}"
    centered "{size=+6}——母亲， 多年以前{/size}"

    pause 3.0

    $ unlock_achievement("borgia_ending")
    $ persistent.endings_seen.add("borgia")

    jump game_ending

    ## ============================================================
    ## 结局7：附庸领主 (妥协) — 效忠王后, 保住城堡失去自主
    ## 2026-05-27 实装. 触发: 4 主属性均未达难度 primary 门槛 + rel_queen 达难度阈值
    ## ============================================================

label ending_vassal:

    $ play_music("audio/music/sad.ogg", fadein=2.0)
    scene bg great_hall with dissolve
    $ set_mood("sad")

    centered "{size=+10}附庸领主{/size}"
    pause 1.5

    scene bg great_hall with dissolve

    "三天后， 王后的使者抵达艾登堡。"

    "黑色铠甲的骑士在外院列阵， 八匹马拉着一辆贴金漆的马车停在大厅门口。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "少主， 协约已经按您说的拟好了。"

    aldric "三条： 艾登堡保留旧界， 守军不超过原编一半， 每年向王都纳贡两次。"

    aldric "您只要在最下面那行签个名。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve

    player "纸笔。"

    $ hide_all_chars()
    "你接过羽毛笔， 笔尖在墨池里蘸了一下。"

    "停了一会儿。"

    ## 选择深度 pass B3 (2026-06-16): 第四章与王子结过盟的玩家, 在此把"投效王后"的延迟代价兑现——
    ## 签字 = 背叛王子。之前结盟时看不到这一刀, 现在它落下来。
    if prince_ally and not prince_betrayed:
        "笔尖悬在纸面上。你想起花园里那只温暖有力的手，还有那句「当我登基的那天，我需要你的支持」。"
        "你握手答应过他。现在这一签，等于把弗雷德里克卖给了他想推翻的母亲。"
        "他不会原谅你。你也不打算解释。"
        $ prince_betrayed = True
        $ change_rel("rel_prince", -40)

    "然后写下了你的名字。"

    pause 1.2

    scene bg castle_exterior with dissolve
    $ set_weather("rain", "light")

    "签约后的第七天， 王后的旗帜挂上了艾登堡的城楼。"

    "不是替代你的旗——是和你的金鹰并排挂着， 王旗在上， 你的在下。"

    "城里的人没说什么。 这种事看多了。"

    pause 1.0

    if rel_aldric >= 50:
        $ hide_all_chars("aldric_img")
        show aldric_img at left with dissolve
        aldric "少主， 老朽留下来。"
        aldric "您父亲守过这座城。 老朽不能在这种时候走。"
        hide aldric_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "谢谢。"
        $ hide_all_chars()
    else:
        "奥尔德里克写了一封辞呈， 第二天清晨悄悄走了。"
        "他没和你告别。 你也没去拦。"

    pause 0.8

    if rel_captain >= 40:
        "雷恩留下了一半的兵。 另一半解甲归田， 他亲自一户一户去通知的。"
        "他自己留下来， 当艾登堡的守备队长——名义上不再是你的人， 是王后册封的。"
    else:
        "雷恩走了。 他说他不愿意挂王旗下守城。"
        "你没挽留。 这种事不能强求。"

    pause 0.8

    if elena_romance:
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "我不走。"
        elena "你这种时候更需要有人在身边。"
        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "……谢谢。"
        $ hide_all_chars()
    elif rel_elena >= 50:
        "艾琳娜没多说什么， 默默把情报网解散了。"
        "她说附庸领主不需要这些东西。 这话她没看着你说。"
    else:
        "艾琳娜在签约后第二天就消失了。"
        "你猜她回了她原来该回的地方。"

    pause 1.2

    scene bg castle_garden with dissolve
    $ set_mood("calm")
    $ set_weather("clear")

    "一年后。"

    "艾登堡的春天来得跟往年一样。 田里的麦子按时播下， 城里的市集按时开张。"

    "你站在花园里看那些藤蔓。 母亲种下的那些。"

    "你保住了它们。 也保住了城里那两千七百多个名字。"

    "代价就是——王都来的文书你要先看， 再决定要不要照办。"

    "桥卫每个季度来一次， 收税， 同时也是来看看你还在不在。"

    pause 1.0

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve

    player "父亲。"

    player "你当年会怎么选？"

    $ hide_all_chars()

    "风没有回答。"

    "但你知道——如果他当年也走到这一步， 大概也会签那个名字。"

    "因为他比你更清楚： 守不住的城， 不如做附庸保住人。"

    pause 1.5

    scene black with fade

    centered "{size=+8}你保住了艾登堡{/size}"

    pause 1.2

    centered "{size=+6}代价是它再也不属于你一个人{/size}"

    pause 2.5

    $ unlock_achievement("vassal_ending")
    $ persistent.endings_seen.add("vassal")

    jump game_ending


    ## ============================================================
    ## 结局8：艾登堡陷落 (失败) — 什么都没准备好, 命运降临
    ## 2026-05-27 实装. 触发: 4 主属性 + truth + borgia 均不可走, 且 rel_queen/baron 都不够
    ## ============================================================

label ending_fall:

    $ play_music("audio/music/war_drums.ogg", fadein=2.0)
    scene bg castle_exterior with dissolve
    $ set_mood("battle")
    $ set_weather("rain", "heavy")

    centered "{size=+10}艾登堡陷落{/size}"
    pause 1.5

    scene bg castle_exterior with dissolve

    "你站在城墙上， 看着北方。"

    "黑压压的一片， 是王后的军队。"

    "西边也有一片， 那是男爵的人。 他们没和王后联手， 也没和你联手， 就这么各走各的路从两个方向压过来。"

    "两军中间隔着艾登堡。"

    pause 1.0

    if power >= 30:
        $ hide_all_chars("captain_img")
        show captain_img at left with dissolve
        captain "领主大人， 守军不到一百二十人。"
        captain "正规军八十， 民兵四十。 王后那边光骑兵就八百， 男爵那边步兵两千。"
        captain "守一天可以， 守一周不可能。"
        hide captain_img
    else:
        "你没有像样的军队。 雷恩当初要的兵你没批， 城墙加固的钱你拿去给税赋空账填了。"
        "现在能用的人， 加上厨子和马夫， 不到八十。"

    pause 0.8

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "少主……"

    aldric "您父亲打仗的时候， 至少手里有些牌。"

    aldric "您这局……"

    aldric "老朽不知道说什么了。"

    hide aldric_img
    $ hide_all_chars()
    pause 1.0

    "天亮的时候， 第一轮箭雨落到了城墙上。"

    "北门撑了不到一个时辰。"

    "南门更快——男爵的人没费多大力气就把它推开了。"

    scene black with fade
    pause 1.5

    scene bg battlefield with dissolve
    $ set_weather("rain", "heavy")

    "大厅里着火了。 不知道是哪一边的人放的。"

    "你抓起父亲的剑， 站在桌子后面。"

    "门外脚步声越来越近。"

    pause 1.0

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve

    player "……早知道当初多做点什么。"

    $ hide_all_chars()

    "门被踹开了。"

    pause 0.5

    scene black with fade
    pause 2.0

    centered "{size=+10}艾登堡陷落{/size}"

    pause 1.5

    centered "{size=+6}领主下落不明{/size}"

    pause 1.5

    centered "{size=+5}王后军烧毁了大厅。 男爵军劫走了财库。 两边都没费什么力气。{/size}"

    pause 2.5

    centered "{size=+5}城里的人后来说—— 那个春天他们的领主什么也没做。{/size}"

    pause 2.0

    centered "{size=+5}什么也没做， 是最容易的选择， 也是代价最重的。{/size}"

    pause 3.0

    $ unlock_achievement("fall_ending")
    $ persistent.endings_seen.add("fall")

    jump game_ending


    ## ============================================================
    ## 通用结局处理
    ## ============================================================

label game_ending:

    $ clamp_stats()
    $ persistent.chapters_completed.add("chapter5")

    ## 检查隐藏成就
    $ check_hidden_achievements()
    if not alliance_baron and not alliance_church and not dark_lily_joined:
        $ unlock_achievement("lone_wolf")

    ## 和平使者: 不走军事路线 — 没结军事同盟 + power 没刷到极高 + reputation 立得住 (靠声望治理)
    ## (栀子 batch 11 第 6 条: pacifist dead code 修复, 给一个粗判定; 严格"零军事手段"判定需追踪 military_used 标志, 留 backlog)
    if not alliance_baron and power < 60 and reputation >= 60:
        $ unlock_achievement("pacifist")

    ## 检查是否达成全结局 (5 主线 + borgia + vassal + fall = 8 总数, 2026-05-27 vassal/fall 实装后修正)
    if len(persistent.endings_seen) >= 8:
        $ unlock_achievement("completionist")

    scene black with dissolve

    centered "{size=+12}权谋之庭{/size}"

    "最终属性："
    "权力： [power] | 财富： [wealth] | 信仰： [faith]"
    "忠诚： [loyalty] | 声望： [reputation] | 谋略： [intrigue]"

    if ending_type == "iron_lord":
        centered "{size=+8}结局：铁腕领主{/size}"
        "以铁与血铸就和平。你的名字将被铭刻在战争的史册上。"
    elif ending_type == "shadow_king":
        centered "{size=+8}结局：影中之王{/size}"
        "在阴影中操控一切。你的名字无人知晓，但你的力量无处不在。"
    elif ending_type == "holy_guardian":
        centered "{size=+8}结局：圣光守护{/size}"
        "以信仰之光驱散战争的阴霾。你的名字将在教堂的颂歌中永远传唱。"
    elif ending_type == "peoples_lord":
        centered "{size=+8}结局：人民领主{/size}"
        "放弃权力的巅峰，守护最平凡的幸福。人民的爱戴，是最崇高的王冠。"
    elif ending_type == "truth":
        centered "{size=+8}结局：真相大白{/size}"
        "正义也许会迟到，但永远不会缺席。真相是最锋利的剑。"
    elif ending_type == "borgia":
        centered "{size=+8}结局：毒药公爵{/size}"
        "你登顶了，代价是再也无法相信任何人。这是行差踏错的尽头——母亲故事里那个王后的真正结局。"
    elif ending_type == "vassal":
        centered "{size=+8}结局：附庸领主{/size}"
        "你保住了城， 也保住了人。 代价是这块土地不再只听你的话。"
    elif ending_type == "fall":
        centered "{size=+8}结局：艾登堡陷落{/size}"
        "什么也没做， 是最容易的选择， 也是代价最重的。"
    else:
        centered "{size=+8}结局{/size}"
        "你的故事在这里画上了句号。"

    "已解锁 [len(persistent.endings_seen)]/8 个结局"

    if len(persistent.endings_seen) >= 8:
        "恭喜你解锁了所有结局！你已经完整地体验了权谋之庭的每一条道路。"
        "每一个选择都没有绝对的对错——只有不同的代价和收获。"

    ## 播放详细尾声
    call ending_epilogue_router from _call_ending_epilogue_router

    ## 老朋友的归宿 (2026-05-17 dccdfrsx 反馈新增)
    ## 在结局个人尾声播完后给马库斯/卡尔一个 closure
    call ending_side_characters_fate from _call_ending_side_chars

    ## 激活 New Game+
    $ activate_ng_plus()

    centered "{size=+6}感谢您的游玩{/size}"

    ## 播放片尾字幕
    show screen credits_roll
    pause

    ## TapTap 评分引导
    if not persistent.rating_asked:
        show screen rating_popup
        pause

    ## 多结局提示 — 显示收集进度和未解锁结局
    show screen ending_complete_hint(current_ending=ending_type)
    pause

    return

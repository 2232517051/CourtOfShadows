## ============================================================
## 第三章：暗百合
## ============================================================

label chapter3_start:

    ## 安全重置：防止上一章过场动画的 _dismiss_pause 泄漏
    $ _dismiss_pause = True
    $ quick_menu = True
    window auto

    $ renpy.force_autosave()
    $ snapshot_chapter_start()
    scene black with fade

    call show_chapter("第三章", "暗百合", "神秘组织浮出水面") from _call_show_chapter_1
    call show_recap("chapter2") from _call_show_recap_1
    call apply_rel_chapter_effects from _call_rel_ch3

    ## 章节过场动画
    call cinematic_chapter3 from _call_cinematic_ch3

    "暗杀事件后的第三天。"

    $ player_scarred = True  ## 切换到带疤版立绘 (canon: ch3 遇刺)

    "你的脸上留下了一道浅浅的疤痕。每次照镜子，都在提醒你——有人要你死。"

    "但你没有时间舔舐伤口。领地内的事务不会因为你的伤痛而停下。"

    "更何况，暗处的敌人也不会给你喘息的机会。"

    ## interlude_ch2_ch3 已删除: 其返程/暗林谷伏击/瘟疫报信分别与 ch2_assassination、
    ## ch2_end 回城戏、gov_plague 重复. chapter 3 开场直接在艾登堡处理事务.

    ## NPC深度支线
    call npc_captain_war_story from _call_npc_cws
    call npc_bishop_doubt from _call_npc_bd

    ## NPC支线（第三章可用）
    call npc_elena_past from _call_npc_ep3
    call npc_bishop_confession from _call_npc_bc3

    ## 商人卡尔的过去（自第二章开头移入：哈伦堡贸易协议之后，深谈分支才可达）
    call npc_merchant_karl_past from _call_npc_mkp

    ## 章节深化（承接领主会议）：男爵的私信
    call ch2_deep_baron_letter from _call_ch2_dbl

    ## 章节深化
    call ch3_deep_captain_scar from _call_ch3_dcs
    call ch3_deep_cure from _call_ch3_dcure

    ## 治理系统：税务改革 / 瘟疫恐慌 / 建设
    call gov_tax_reform from _call_gov_tax1
    call gov_plague from _call_gov_plague3
    call gov_building from _call_gov_build3

    ## ============================================================
    ## 第一部分：异常迹象（~400行）
    ## ============================================================

label ch3_strange_signs:

    $ play_music("audio/music/castle_calm.ogg", fadein=2.0)
    scene bg castle_exterior with dissolve
    $ unlock_gallery("bg_castle_exterior")

    $ trigger_random_event("explore")

    "清晨。艾登堡的城墙在朝阳下闪烁着金色的光芒。"

    "你站在城墙上，俯瞰着领地的全貌。田野、村庄、远处的森林——一切看起来平静如常。"

    if merchant_deal:
        "早上账房送来消息：卡尔商队的第一笔月钱入了库。两百金币，一枚不少。"
        $ change_stat("wealth", 3)

    "但你心里清楚，麻烦还没过去。"

    show captain_img at right with dissolve
    $ unlock_gallery("captain")

    captain "领主大人，早安。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "雷恩，有什么新情况？"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "有几件事需要您注意。"

    if ch1_deep_widow_verdict == "pay":

        captain "还有……一件私人的事。"

        "雷恩停顿了一下，脸上浮起一丝温和的笑容。"

        captain "你还记得那个偷面包的寡妇家？上个月，她的儿子——就是那个少年汉斯——被面包师弗里茨雇了做学徒。"

        captain "他现在每周来城堡送面包。昨天寡妇来报告，说孩子已经学会了烘焙的基本手法。冬天来临前，他们家已经存够了粮食。"

        "你把手中的茶盏轻轻放下，没说话。"

        "嘴角不觉泛起一丝淡笑——那笔救济金，看来确实没有白花。"

    captain "首先，北部的三个村庄报告说有农民失踪。最近半个月，已经有七个人不见了。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "七个人？这不正常。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "是的。我派人去调查了，但没有发现任何线索。没有打斗痕迹，没有血迹，人就像凭空消失了一样。"

    "你皱起眉头。农民失踪不是小事——这些人是领地的根基。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "失踪的人有什么共同点吗？"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "都是青壮年男性，年龄在二十到四十之间。而且……"

    "雷恩犹豫了一下。"

    captain "他们都住在靠近森林边缘的地方。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "森林……"

    $ hide_all_chars()
    "你想起了父亲生前常说的话——「森林里有很多秘密，有些最好不要去探究。」"

    "现在你开始怀疑，父亲说的并不是什么猎人的迷信。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    if herman_moerg_tip:
        captain "对了，上次那个行脚商人提的莫格伯爵——我托西边的同乡打听过了。两百新兵是真的，但到现在没出过营。"

        captain "剿匪不像，倒像是在等着看谁先动手。西边暂时不用担心，但值得盯着。"

    captain "还有一件事。"

    "雷恩从怀中掏出一块粗糙的布片，上面画着一个奇怪的符号——一朵倒置的百合花。"

    captain "这个符号最近在领地内频繁出现。墙壁上、树干上、甚至教堂的门口都有。"

    "你接过布片，仔细端详。那朵倒置的百合花线条流畅，不像是随手涂鸦。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    if dark_lily_exists_known:
        player "这个标记——我认得。暗百合。"

        $ hide_all_chars()
        "你之前的调查里已经碰到过这三个字。但你没想到它的触手已经伸到了艾登堡的街巷。"

        $ hide_all_chars("captain_img")
        show captain_img at left with dissolve
        captain "……您果然知道。"

        captain "那就好说了。这个符号最近在领地内频繁出现——墙壁、树干、甚至教堂的门口。不是巧合。"
    else:
        player "这是什么意思？"

        hide player_char_img
        $ hide_all_chars("captain_img")
        show captain_img at left with dissolve
        captain "我不确定。但老一辈的人说，这是一个古老组织的标记。"

        captain "他们叫它……暗百合。"

        $ hide_all_chars()
        "暗百合。"

        "这个名字在你脑中敲出一点模糊的回响——你说不清在哪里碰到过它，但那种熟悉感挥之不去。"

        "不管它是什么，它显然不满足于做一个传说。"

        $ dark_lily_exists_known = True

    menu:
        "召集附近领主家臣联合搜山" if power >= 50:
            $ change_stat("power", 8)
            $ change_stat("reputation", 3)
            $ change_stat("loyalty", -2)
            $ ch3_dark_lily_response = "force"

            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "雷恩，给附近三家友好领主发信——艾登堡领主请求，三日内派家臣武装支援。"

            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "您要他们出兵搜山？"

            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "联合搜山。三百人马，五座森林同时排查。我倒要看看他们躲哪儿去。"

            $ hide_all_chars()
            "三天后，三百名武装家臣分作五队进入了艾登堡周边森林。"

            "没找到暗百合的人——但暗百合那个月之后再没有失踪案。"

            "你向友好领主回了重礼+答应未来三年内对方有需要可以反过来求援。"

            "这是一笔账。但你立了威——「艾登堡可以叫得动三百兵」。这个消息会传得很远。"

            jump ch3_after_field_choice

        "让雷恩加派巡逻":
            $ change_stat("loyalty", 5)
            $ change_rel("rel_captain", -8)
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "加派人手，特别是森林边缘的区域。我不想再有人失踪。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            "雷恩没有立刻应声。"
            captain "……遵命。我会安排双倍巡逻。"
            captain "只是大人——人手就这么多。林子大，分散开来，每一处都薄。真要有人动手，巡逻队拦不住，只能事后收尸。"
            $ hide_all_chars()
            "雷恩走后，你盯着地上他靴子踩过的泥印。你知道他说得对：双倍巡逻只是把人摊薄。你没下围剿的令，是因为还没拿准——可暗百合不会等你拿准。"
            jump ch3_after_field_choice

        "亲自去失踪地点调查":
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "准备马匹。我亲自去看看。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "领主大人，暗杀事件刚过，您亲自出行太危险了。"
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "正因为刚刚有人想杀我，我更不能躲在城堡里。"
            hide player_char_img with dissolve

            $ hide_all_chars()
            $ trigger_crisis("intrigue", 4,
                "你执意亲自前往森林边缘的失踪地点。雾深林密，任何蛛丝马迹都可能是陷阱——也都可能是暗百合留下的破绽。",
                "ch3_dark_lily_field_win", "ch3_dark_lily_field_lose",
                courage_cost=25)
            call crisis_encounter from _call_crisis_ch3_field

            ## 退缩 fall-through
            "你顿了一下。雷恩说得对——这不是逞英雄的时候。"
            "调查的事先交给雷恩。你回到城堡，把那块倒置百合的布片放在桌上，盯着它出神。"
            jump ch3_after_field_choice

        "先不管失踪的事，调查符号的来源" if intrigue >= 45:
            $ change_stat("intrigue", 8)
            $ change_stat("reputation", -2)
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "失踪的事先交给你处理。我对这个符号更感兴趣。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "领主大人？"
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "帮我找一个懂古代纹章学的人。越快越好。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "是，大人。"
            jump ch3_after_field_choice

label ch3_dark_lily_field_win:
    scene bg forest_path with dissolve
    $ unlock_gallery("bg_forest_path")
    $ set_mood("mystery")
    $ set_weather("fog", "normal")

    "雷恩和三个士兵随你走进雾中。失踪农民的踪迹断在一道溪边——蹄印没了，没有挣扎的痕迹。"

    "你蹲下，在湿泥里看见一行鞋印——尺码偏小，鞋底纹路是城里制鞋匠用的细密齿，不是村民的草编。"

    "你又在树根下挑出一块半埋的麻布，边角绣着倒置的百合。绣线很新——这个标记最近还在被人佩戴。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "领主大人，他们撤得很急。一刻钟前还在这里。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "城里的鞋。新绣的章。"
    player "暗百合不是传说。是有人、有装备、有组织的活人。"

    hide player_char_img with dissolve
    $ hide_all_chars()
    "你把鞋印的轮廓和那块麻布一起放进怀里。雾在退，但你心里那块阴影才刚开始浓起来。"

    $ change_stat("intrigue", 5)
    $ dark_lily_field_intel = True
    $ log_decision("第三章", "现场获得暗百合实证")

    jump ch3_after_field_choice

label ch3_dark_lily_field_lose:
    scene bg forest_path with dissolve
    $ unlock_gallery("bg_forest_path")
    $ set_mood("battle")
    $ set_weather("fog", "normal")

    "你和雷恩走进雾中。"

    "一支箭从侧面树丛里射出，扎在你左前方的树干上——再偏半尺就是你的喉咙。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "领主大人，后退！"

    "雷恩一把把你按倒，拔剑挡在你身前。"

    $ play_sound("audio/sfx/sword_draw.ogg")

    "三个黑衣人从树上跃下。雷恩独自硬接，士兵们围上去厮杀。"

    captain "走！这里我们顶住！"

    hide captain_img
    $ hide_all_chars()
    "一个士兵把你拖回马背。回头一眼——黑衣人正撤进雾里，什么都没留下。"

    "你来得太晚，什么也没看见。"

    $ log_decision("第三章", "现场调查中伏，未获实证")

    jump ch3_after_field_choice

label ch3_after_field_choice:
    hide captain_img with dissolve

    ## --- 村庄调查插曲 ---

    $ set_mood("mystery")
    $ set_weather("fog", "normal")
    scene bg forest_path with dissolve
    $ unlock_gallery("bg_forest_path")

    "森林里的事还没完。"

    "当天下午，又一个农民失踪的消息传来。这次是一个铁匠——村子里最强壮的人。"

    "他的妻子哭着跑到城堡求见你。"

    $ hide_all_chars("blacksmith_wife_img")
    show blacksmith_wife_img sad at left with dissolve

    blacksmith_wife "领主大人！求您救救我丈夫！"

    blacksmith_wife "昨晚他去森林里取木炭，就再也没有回来……"

    blacksmith_wife "我去找他，只看到他的斧头扔在地上，还有……这个。"

    $ hide_all_chars()
    "她颤抖着递给你一块布条。上面画着那个你已经见过的符号——倒置的百合花。"

    "但这一次，百合花旁边多了一行小字：「沉默者将得到庇护。」"

    hide blacksmith_wife_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "沉默者将得到庇护……这是什么意思？"

    "铁匠的妻子摇着头，泣不成声。"

    hide blacksmith_wife_img with dissolve

    menu:
        "召集所有铁匠樵夫家属当众发誓" if reputation >= 50:
            $ change_stat("reputation", 5)
            $ change_stat("loyalty", 5)
            $ ch3_public_oath = True

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "奥尔德里克，把所有铁匠樵夫的家属都叫到城堡前的广场。"

            player "今天下午，我要在他们面前说话。"

            $ hide_all_chars()
            "下午三时，广场上来了七十几个人。大半是女人和孩子。"

            "你站在台阶上，没读稿。"

            "「你们中间已经有四个人失踪。有人告诉你们： 沉默会得到庇护。我告诉你们： 那是骗人的。」"

            "「今天起，城堡里养二十个壮丁，谁家出事报到城堡，当天就有人上山找。」"

            "「找得回我送他回家。找不回的，家里口粮我管。」"

            "广场上一开始没人说话。然后是铁匠的妻子先跪下来，把头磕在石板上。"

            "其他人一个跟一个也跪下了。"

            "你没有让他们起来。"

            "你转身走回城堡的时候，雷恩在身后说了一句："

            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "今天这事，北方很快就会听说。森林里的人也会听到。"

        "安慰她并承诺会找回她丈夫":
            $ change_stat("loyalty", 5)
            $ change_stat("reputation", 5)
            player "我会找到你的丈夫。在那之前，你和孩子搬到城堡里来住。我派人保护你们。"
            hide player_char_img
            $ hide_all_chars("blacksmith_wife_img")
            show blacksmith_wife_img at left with dissolve
            blacksmith_wife "谢谢领主大人……谢谢您……"
            $ hide_all_chars()
            "你叫来一个侍女，安排铁匠的妻子住下。"
            "然后你走到窗前，看着远处的森林。"
            "那片浓密的绿色里，藏着什么秘密？"

        "仔细询问铁匠失踪前的异常情况":
            $ change_stat("reputation", 5)
            hide blacksmith_wife_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "在你丈夫失踪之前，他有没有提到什么异常的事？有没有见过什么陌生人？"
            hide player_char_img
            $ hide_all_chars("blacksmith_wife_img")
            show blacksmith_wife_img at left with dissolve
            blacksmith_wife "他……他前几天确实说过一件怪事。"
            blacksmith_wife "他说，有个穿黑斗篷的人来铁匠铺，不打东西，只是站在那里看。"
            blacksmith_wife "他问那人要什么，那人说：「很快你就会知道。」"
            blacksmith_wife "然后就走了。第二天……他就不见了。"
            hide blacksmith_wife_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "黑斗篷的人……长什么样？"
            hide player_char_img
            $ hide_all_chars("blacksmith_wife_img")
            show blacksmith_wife_img at left with dissolve
            blacksmith_wife "看不清脸。戴着兜帽。但他的手上——我丈夫说——他的手上有一个纹身。"
            hide blacksmith_wife_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "什么样的纹身？"
            hide player_char_img
            $ hide_all_chars("blacksmith_wife_img")
            show blacksmith_wife_img at left with dissolve
            blacksmith_wife "一朵……花。"
            "你和雷恩交换了一个眼神。"

        "命令雷恩立刻搜索森林" if power >= 55:
            $ change_stat("power", 10)
            hide blacksmith_wife_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "雷恩！带二十个人，立刻搜索北边的森林。重点搜查铁匠最后出现的地方。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "是！"
            $ hide_all_chars()
            "雷恩带着一队人马飞奔而去。"
            "你等了三个小时。"
            "雷恩回来的时候，脸色很难看。"
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "大人……我们在森林深处发现了一些东西。"
            captain "有人在那里建了一个临时营地。至少住过二十个人。"
            captain "但我们到的时候，人已经撤走了。只留下了一些痕迹——和这个。"
            "他递给你一块金属牌。上面刻着倒置的百合花，背面写着一个数字——'7'。"
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "七……和失踪的人数一样。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "还有一件事。营地周围有车轮印。他们往南走了。"
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "往南？南面是……"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "冯·哈根男爵的领地。"
            $ hide_all_chars()
            "一切似乎有了一个方向。"
            $ change_stat("reputation", 8)

    "你站在城墙上，看着夕阳缓缓沉入地平线。"

    "你的手不自觉地攥紧了城垛的石头，指节发白。"

    "这不是普通的犯罪事件。这是有组织、有目的的行动。"

    "而暗百合——不管它是什么——已经把手伸进了你的领地。"

    "你决定回大厅。有些事情需要和奥尔德里克商量。"

    ## --- 与奥尔德里克的对话 ---

    scene bg great_hall with dissolve
    $ unlock_gallery("bg_great_hall")

    "回到大厅，你发现奥尔德里克已经在等你了。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    $ unlock_gallery("aldric")

    aldric "听说又有人失踪了？"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你消息倒是灵通。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "领地里发生的事，没有我不知道的。"

    "奥尔德里克的语气一如既往地自信，但你注意到他的眼神中多了一丝忧虑。"

    aldric "年轻的领主，我有些话想跟你说。关于你的父亲。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "父亲？"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "你父亲晚年的行为……很异常。"

    "老骑士在椅子上坐下，似乎在回忆往事。"

    aldric "大约从十年前开始，他经常在深夜独自出入书房。有时候，我看到他的书房灯火通明到天亮。"

    aldric "他变得越来越多疑，甚至不让任何人碰他书桌上的东西。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你觉得他在隐瞒什么？"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "不只是隐瞒。他在……准备什么。"

    aldric "有一次，我半夜路过书房，听到他在自言自语。他说——"

    aldric "「如果我出了什么事，他们一定会来找我的孩子。」"

    "你的心猛然一缩。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "他说的「他们」是谁？"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "我不知道。我问过他，但他只是摇摇头，说：「你不需要知道。知道得越少，越安全。」"

    "奥尔德里克看着你，目光深邃。"

    aldric "但现在……你已经不安全了。所以，也许是时候让你知道一切了。"

    menu:
        "请奥尔德里克告诉你所有他知道的":
            $ change_rel("rel_aldric", 10)
            $ change_stat("loyalty", 5)
            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "告诉我，奥尔德里克。我需要知道。"
            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "你父亲在去世前的最后几个月，频繁与一些陌生人见面。那些人总是深夜来，天亮前走。"
            aldric "我只见过他们的身影——都穿着深色斗篷，脸上蒙着面纱。"
            aldric "有一次，我在走廊上撞见了其中一个人。他的斗篷上绣着一朵百合花。"
            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "暗百合……"
            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "你也听说了那个名字？"
            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "今早雷恩告诉我的。领地内到处出现这个组织的符号。"
            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "那么事情比我想象的更严重了。"
            aldric "你父亲可能不只是和暗百合有联系——他可能就是暗百合的一部分。"

        "问奥尔德里克为什么现在才说这些":
            $ change_rel("rel_aldric", -5)
            $ change_stat("power", 5)
            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你早就知道这些，为什么到现在才告诉我？"
            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "因为你父亲让我发誓保密。他说，除非你主动问起，否则不要提起任何关于暗百合的事。"
            aldric "他说，如果你没有注意到那些迹象，说明时机还没到。"
            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "而现在，符号到处出现，人在失踪——时机到了？"
            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "恐怕是的。"

        "保持沉默，让奥尔德里克继续说" if intrigue >= 45:
            $ change_stat("intrigue", 8)
            $ change_stat("reputation", -2)
            $ hide_all_chars()
            "你没有说话，只是安静地看着老骑士。"
            "奥尔德里克理解了你的意思。"
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "你和你父亲一样，善于倾听。好吧，让我把我知道的都告诉你。"
            aldric "暗百合不是普通的秘密组织。它有很长的历史——据说有两百多年了。"
            aldric "你父亲晚年最大的变化，就是他开始相信一件事——"
            aldric "当今王后的摄政权，是建立在谎言之上的。"

    aldric "无论如何，我建议你仔细搜查你父亲的书房。"

    aldric "他一定留下了什么东西给你。他太精明了，不可能什么都没留下。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我之前已经翻过书房了。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "你翻过书架后面的暗格吗？你检查过地板下面吗？你看过壁炉里的每一块砖吗？"

    "显然，你之前的搜查太粗糙了。"

    aldric "你父亲有一个习惯——把最重要的东西藏在最不起眼的地方。"

    aldric "他曾经在一本烹饪书里藏过军事部署图。在一幅风景画的背面贴过密信。"

    aldric "你不能按常理来找。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你了解他比我多得多。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "那是因为我跟了他三十年。从他还是个毛头小伙子的时候就开始了。"

    "奥尔德里克的目光落在墙上那把旧剑上，声音放轻了。"

    $ hide_all_chars("aldric_img")
    show aldric_img sad at left with dissolve

    aldric "他年轻时和你很像——倔强、勇敢，有一股不服输的劲头。"

    aldric "但后来……权力和秘密慢慢改变了他。他变得沉默、谨慎，有时候甚至有些偏执。"

    aldric "到了最后几年，他几乎不和任何人说心里话了。连我都被排斥在外。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你不怨他？"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "怨？不。我理解他。"

    aldric "当一个人背负着能够颠覆整个王国的秘密时，他不敢信任任何人，是合情合理的。"

    aldric "但他信任了一个人——或者说一群人。暗百合。"

    aldric "去书房吧，仔细找。你父亲藏东西的手段，可不是随便翻翻就能发现的。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "奥尔德里克。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "什么？"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "谢谢你告诉我这些。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "别谢我。把真相找出来就行。你父亲值得一个交代。"

    hide aldric_img with dissolve

    ## --- 男爵的信使 ---

    "你正要去书房，一个侍卫急匆匆地跑来。"

    $ hide_all_chars("soldier_generic_img")
    show soldier_generic_img at left with dissolve
    soldier "大人！城门口来了一个人，说是冯·哈根男爵的信使。"

    hide soldier_generic_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "男爵的信使？他来做什么？"

    hide player_char_img
    $ hide_all_chars("soldier_generic_img")
    show soldier_generic_img at left with dissolve
    soldier "他说有一封男爵的亲笔信，必须当面交给您。"

    menu:
        "接见信使":
            $ hide_all_chars()
            "你来到城门口。"
            "信使是一个中年男人，穿着男爵家族的制服——暗绿色配银边。"
            hide soldier_generic_img
            $ hide_all_chars("servant_generic_img")
            show servant_generic_img at left with dissolve
            messenger "领主大人。冯·哈根男爵让我转交此信，并等候您的回复。"
            $ hide_all_chars()
            "你打开信封。"
            "信是男爵的手笔——笔迹生硬，措辞傲慢。"
            "「致艾登堡领主：近闻贵领地出现一些……不安定因素。失踪的农民、奇怪的符号——这些事在我的领地上也有发生。本男爵提议共同调查此事。如蒙允诺，请遣使者至我堡商谈。——冯·哈根男爵。」"
            "你反复读了两遍，嘴角露出一丝冷笑。"
            hide servant_generic_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "共同调查？他以为我会相信这种鬼话。"
            if darkflame_known:
                "如果男爵真的和暗焰有关，那这封信就是试探——看你知道多少，看你会怎么反应。"
            else:
                "如果男爵真的在背后搞什么名堂，那这封信就是试探——看你知道多少，看你会怎么反应。"

            menu:
                "亲自带剑去——让他知道艾登堡不怕硬碰硬" if power >= 60:
                    $ change_stat("power", 5)
                    $ change_rel("rel_baron", -5)
                    player "替我回信：领主三日后亲自前往。让男爵备好酒——也备好剑。"
                    "你不打算搞那些客气的虚招。男爵想试探， 你就让他直接看到锋。"
                    "三日后你按时到了。男爵的姿态一开始很高， 但你坐下不到半个时辰， 他的语调已经在悄悄软。"

                "写一封客气但模糊的回信":
                    $ change_stat("intrigue", 5)
                    $ change_rel("rel_baron", 5)
                    player "替我回信：领主对男爵的提议深表感谢，愿择日商议。"
                    "你没有答应，也没有拒绝。给自己留了回旋的余地。"

                "拒绝，并警告男爵管好自己的事" if power >= 55:
                    $ change_stat("power", 10)
                    $ change_rel("rel_baron", -10)
                    player "回信：艾登堡的事务由本领主处理，不劳男爵费心。如果男爵的领地上也有问题，建议男爵先管好自己的领民。"
                    "信使的脸色有些难看，但他恭敬地接过回信离开了。"

                "接受邀请——借机探查男爵的意图" if intrigue >= 45:
                    $ change_stat("intrigue", 8)
                    $ change_stat("faith", -3)  ## 表面接受 / 实为算计的代价 (balance pass 修法 1)
                    $ change_rel("rel_baron", 5)
                    player "回信：本领主将于三日后遣使者前往。望男爵以礼相待。"
                    "你不会亲自去——但派一个可靠的人去打探虚实，是个好主意。"

        "拒绝接见，让信使把信留下":
            $ change_stat("power", 5)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "让他把信留在城门口。我不见他。"
            hide player_char_img
            $ hide_all_chars("soldier_generic_img")
            show soldier_generic_img at left with dissolve
            soldier "是，大人。"
            "不久后，侍卫把信拿来了。你看过内容后，把信扔进壁炉。"
            hide soldier_generic_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "男爵的邀请……不值一提。"

    $ hide_all_chars()
    "处理完男爵的事后，你终于可以去书房了。"

    "你决定立刻去书房。"

    "但在走出大厅的时候，你注意到一件奇怪的事——"

    "大厅角落里站着一个你不认识的侍从。他看到你注意到他后，迅速低下了头。"

    menu:
        "上前盘问那个侍从":
            $ change_stat("power", 5)
            $ change_stat("reputation", 5)
            "你走到那个侍从面前。"
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你是谁？我没见过你。"
            hide player_char_img
            $ hide_all_chars("servant_generic_img")
            show servant_generic_img at left with dissolve
            servant "回、回领主大人，小人是新来的。管事安排我在大厅服侍。"
            hide servant_generic_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "新来的？谁批准雇用你的？"
            hide player_char_img
            $ hide_all_chars("servant_generic_img")
            show servant_generic_img at left with dissolve
            servant "是……是艾琳娜小姐。"
            $ hide_all_chars()
            "你记住了这个人的脸。他的眼神太躲闪了，不像一个普通的侍从。"
            "你决定暗中留意他。"

        "假装没看见，但暗中让人跟踪他" if intrigue >= 45:
            $ change_stat("intrigue", 8)
            $ change_stat("loyalty", -3)  ## 阴谋监视盟友的代价 (balance pass 修法 1)
            "你若无其事地走出大厅，但在走廊上低声吩咐一个卫兵。"
            hide servant_generic_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "看到大厅里那个新来的侍从了吗？跟着他，记录他的一切行踪。不要被发现。"
            hide player_char_img
            $ hide_all_chars("soldier_generic_img")
            show soldier_generic_img at left with dissolve
            soldier "是，大人。"

        "不在意，继续去书房":
            $ hide_all_chars()
            "你没有多想，径直走向书房。"
            "也许只是一个普通的新侍从。你不能疑神疑鬼。"

    ## ============================================================
    ## 第二部分：父亲的书房（~500行）
    ## ============================================================

label ch3_fathers_study:

    $ play_music("audio/music/night_mystery.ogg", fadein=2.0)
    scene bg study with dissolve
    $ unlock_gallery("bg_study")

    "你再次踏入父亲的书房。这一次，你不打算放过任何角落。"

    "阳光从窗户斜照进来，照亮了空气中悬浮的灰尘。"

    "书房的布局你已经很熟悉了——一张大书桌、三面墙的书架、一个壁炉、一幅父亲的画像。"

    "你拢了拢衣领，开始系统性的搜查。"

    "首先，书桌。"

    "你把每一个抽屉都拉出来，检查是否有夹层或暗格。"

    "第一个抽屉——信件、印泥、封蜡。没有异常。"

    "第二个抽屉——账本、地图、领地的契约。你仔细翻看，没有发现隐藏的内容。"

    "第三个抽屉——空的。但你注意到，这个抽屉比其他抽屉浅了大约两寸。"

    menu:
        "仔细检查第三个抽屉的底部":
            $ change_stat("reputation", 5)
            "你把抽屉完全抽出来，翻转过来。"
            "果然——底板是双层的。你用指甲撬开一个缝隙，发现里面有一张折叠的羊皮纸。"
            "上面画着一幅图——看起来像是城堡的地下结构图。"
            "你的心跳加速了。"
            "图上用红墨标注了几个位置，旁边写着密密麻麻的小字，但用的是某种你不认识的密码。"
            $ father_letters_found = True
            $ collect_item("letter_father_1")

        "先检查其他地方，待会儿再回来":
            "你把抽屉推回去，决定先检查别的地方。"
            "也许书架上有更重要的发现。"

    "接下来，书架。"

    "三面墙的书架上摆满了书籍。法律典籍、历史文献、地理志、骑士小说……"

    "你一本一本地取下来翻看。大多数书都很正常，页面之间没有夹带任何东西。"

    "但你没有放弃。你把每一本书都抽出来，检查它的重量和厚度是否正常。"

    "第一面墙——大约一百二十本书。花了你整整一个小时。什么也没发现。"

    "你的耐心开始被磨损，但你想起奥尔德里克的话——你父亲藏东西的手段不是一般人能想到的。"

    "第二面墙。你开始检查每一本书的书脊——有没有异常的厚度、颜色或质地。"

    "翻到第三十七本时，你注意到了一件事。"

    "这本书叫《税赋改革论》。看起来很无聊，但它的书脊上有一个极其微小的记号——一个用针刻出来的小点。"

    "你翻开它。内容确实是关于税赋改革的。但在第一百页，有一个折角。"

    "折角所在的那一行写着：「第三，从第七栏起。」"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "这是……线索？"

    $ hide_all_chars()
    "你思考了一会儿。第三面墙，第七本书？"

    "你走到第三面墙，数到第七本书。"

    "那是一本《骑士团年鉴》。你翻开它——里面夹着一张薄薄的丝绢。"

    "丝绢上画着一个简单的图案：六朵花围成一圈，中间是一只眼睛。"

    "你把丝绢收好。也许以后会用到。"

    "继续搜查。你回到第二面墙。"

    "当你翻到第二面墙的中间位置时，你注意到了一些异常。"

    "有一排书的书脊颜色和其他的不太一样——更新，更亮。像是后来放进去的。"

    "你把这些书全部取出来。"

    "它们的标题看起来很普通：《王国税务总论》、《领地管理概要》、《边境防御手册》——"

    "但当你打开《边境防御手册》时，里面的内容让你呆住了。"

    "这根本不是什么防御手册。每一页都是密密麻麻的日记，用父亲的笔迹写成。"

    "而且，日记的内容是用一种奇特的方式编排的——每一段的第一个字连起来，才是真正的内容。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "这是……密码日记？"

    $ hide_all_chars()
    "你坐到桌前，点亮所有的蜡烛，开始尝试破译。"

    "第一页的第一段有二十个字。你把每段的第一个字提取出来——"

    "组成了一句不通顺的话。不对，可能不是每段第一个字。"

    "你尝试每行第一个字。也不对。"

    "每行最后一个字。不通顺。"

    "你烦躁地揉了揉太阳穴。父亲设计的密码不会这么简单。"

    "你重新审视书页。注意到每一段的行距不太一样——有些段落行距更宽，有些更窄。"

    "宽行距的段落——你数了一下——正好有七个。"

    "你把这七个段落的第一个字提取出来：暗、百、合、第、七、次、联。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "暗百合第七次联……"

    "接着是窄行距段落的第一个字：络、他、们、带、来、了、先、王、遗、诏、的、抄、本。"

    player "络。他们带来了先王遗诏的抄本！"

    $ hide_all_chars()
    "规律找到了——宽行距和窄行距交替，各自段落的第一个字连起来才是正文。"

    "你兴奋地继续破译。速度快了很多。"

    "你花了近一个小时，把前三页全部破译了出来。"

    "第一页的完整内容："

    "『暗百合第七次联络。他们带来了先王遗诏的抄本。如果这是真的，那整个王国的权力结构都建立在谎言之上。我必须谨慎行事。马修斯最近的来访越来越频繁，我怀疑他在监视我。』"

    "第二页的内容让你更加不安："

    "『今天在集市上看到了一个熟悉的符号——倒置的百合花。暗百合在领地内留下了接头暗号。我按照暗号去了约定地点，见到了他们的联络人。他告诉我，暗百合内部出现了分裂。有人被王后收买了。我必须更加小心。』"

    "第三页："

    "『收到了一封匿名信。信上说我的书房被人监视了。我检查了所有的角落，没有发现异常。』"

    "『但为了安全，我开始使用这种密码记录。如果有人翻到这本书，他们只会看到无聊的防御手册。』"

    "『只有知道规律的人，才能读懂真正的内容。我的孩子——如果你读到这里，说明你足够聪明。我为你骄傲。继续读下去。』"

    "你的眼眶微微湿润了。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "父亲……"

    $ hide_all_chars()
    "你继续翻看，逐页破译。"

    "『第十二年。暗百合的人又来了。这次带来的是一个女人——她说她是先王的侍女，亲眼看到了遗诏被篡改的过程。教会大主教费雷恩亲手销毁了原件，用假遗诏取而代之。伊莎贝拉成了摄政王后，而本应继承摄政权的……是我。』"

    if testament_forged_known:
        "日记的内容印证了你已经知道的事实。但亲眼看到父亲的笔迹写下这些，感觉完全不同。"

        if father_was_regent_known:
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "所以主教说的都是真的……父亲亲手记录了这一切。"
        else:
            player "父亲……他本该是摄政者？"
    else:
        "你的手在颤抖。"

        player "父亲……他本该是摄政者？"

    $ testament_forged_known = True
    $ ferein_role_known = True
    $ father_was_regent_known = True

    $ hide_all_chars()
    "『第十三年。我决定保密。如果这个真相泄露，会引发内战。我不想让无辜的人流血。但暗百合的人越来越急切——他们说王后的统治越来越残暴，必须有人站出来。』"

    "你停下来，走到窗边，看着窗外的天空。"

    "父亲明明该是摄政者，却一直忍着，谁也没告诉。"

    "你在窗边站了很久。"

    "你再次坐下，继续破译。"

    "『第十三年，秋。暗百合的联络人变了。新来的是一个女人，自称'影'。她比之前的联络人更谨慎，也更有威严。她说，暗百合即将迎来一个新的首领。旧首领病重，即将传位。她说新首领——也就是她——会改变策略，不再被动等待。』"

    "『第十三年，冬。奥尔德里克开始怀疑什么了。他几次在深夜看到我出入书房，问我是不是身体不好。我敷衍了过去。但我知道老朋友的直觉是敏锐的，瞒不了他太久。我在考虑是否应该告诉他。』"

    "你想起了奥尔德里克说的——他知道一些，但不知道全部。父亲最终还是没有把全部真相告诉他。"

    "『第十四年，春。冯·哈根男爵来访。他表面上是谈边境巡防的事，但我从他的眼神中看到了别的东西。他在打量我，像一条蛇在观察猎物。我怀疑他知道了什么——或者，他本身就参与了阴谋。』"

    "你的拳头不自觉地握紧了。"

    "『第十四年，夏。我发现了一件更可怕的事。先王的死……可能也不是自然死亡。』"

    "『有人在他的酒中下了慢性毒药——暮色之露。而最有嫌疑的人，就是现在的王后。』"

    "『暮色之露是一种无色无味的毒药，需要连续服用数月乃至数年才会致命——剂量越低，耗时越长，也越难被察觉。受害者看起来像是慢性病死亡，几乎无法被发现。』"

    ## batch 14 反馈"编辑部替补" (2026-05-11) #4 毒药神话化软化:
    ## 加 1 句具体 lore, 让暮色之露像真实存在的稀有草药制品而非魔法毒药
    "『据说它来自南方深山某种紫色苔藓的根须，采集极难，提炼更难。能稳定提出毒物的工坊，整个王国不超过三家。』"

    "『但暗百合的炼金术士在先王的遗物中检测到了残留。』"

    if queen_poisoned_king_known:
        "你已经从别处得知了先王被毒杀的真相——但日记中的详细记录让这一切更加触目惊心。父亲亲自调查了毒药的来源和剂量。"

        "这种冷血和耐心，让你再次不寒而栗。"
    else:
        "你感觉血液都要凝固了。"

        "连续服用数月……先王在不知不觉中被自己的妻子毒杀了？"

        "这种冷血和耐心，让你不寒而栗。"

    $ poison_evidence = True
    $ queen_poisoned_king_known = True
    $ dusk_dew_known = True

    "『第十四年，秋。我派了一个信任的人去王都调查暮色之露的来源。他查到了——毒药是教会的炼金术士格温制造的。格温是费雷恩大主教的人。一切线索都指向教会——但教会是主谋还是工具？我还不确定。』"

    "『第十四年，冬。我的人在王都被人发现了。他们杀了他，伪装成意外。我失去了一个忠诚的仆人。我开始意识到——我面对的不是一两个人，而是一个庞大的系统。一个从宫廷到教会到地方贵族的完整网络。我一个人……根本无法对抗。』"

    "父亲在日记中的语气从最初的愤怒，逐渐变成了无奈和疲惫。"

    "『第十五年。马修斯主教开始频繁来访。他的眼神让我不安。我怀疑他已经知道我在调查什么。教会在这件事中扮演了什么角色？他们是同谋，还是被利用了？马修斯和费雷恩不一样——他似乎有自己的良心。但良心在权力面前，往往不堪一击。』"

    "『第十五年，春。我开始为最坏的情况做准备。我在书房里设置了暗格和密道入口，把最重要的证据分散藏在不同的地方。』"

    "『如果有一天我出了事，我的孩子必须能找到这些东西。但我又不能把线索留得太明显——否则敌人会先一步找到。』"

    "『这是一场与时间和命运的赌博。』"

    "『第十五年，夏。'影'来见我。她说暗百合内部出现了严重的裂痕。』"

    "『一个叫「暗焰」的派系被王后收买了，正在从内部瓦解组织。她怀疑暗焰的人就在我身边。她让我加倍小心。』"

    "『我问她暗焰的首领是谁。她说——「一个你认识的人。一个你不会怀疑的人。」』"

    "『至今我都没能查出那个人是谁。』"

    $ darkflame_known = True

    "你盯着这段话。「一个你认识的人。一个你不会怀疑的人。」"

    "是谁？男爵？主教？还是……"

    "你不敢继续往下想。"

    "你翻到最后几页。日记的笔迹变得潦草了——父亲在写这些的时候，手一定在发抖。"

    "『第十五年，秋。我感觉自己的身体不太对。最近总是头晕，食欲不振，晚上盗汗。我怀疑……但我不敢验证。如果我真的被下了毒——暮色之露——那我还有多少时间？』"

    if father_death_known:
        "你早已从暗百合那里得知了父亲的死因。但读到父亲亲笔写下的这些文字——那种孤立无援的绝望——比任何转述都更加真实。"
    else:
        "你的呼吸急促起来。"

    "『第十五年，冬。我已经确定了。我的症状和先王当年的症状完全一致。有人在我的食物或酒中下了暮色之露。我不知道是谁——厨房？酒窖？还是某个我信任的人？我没有时间去追查了。我只能把最后的线索留给我的孩子。』"

    "你翻到最后几页。"

    "『最后一页。如果你在读这些字，我的孩子，说明我已经不在了。我把一切都藏在你最不可能找到的地方——壁炉后面。记住：向左三次，向右两次，再向左一次。不要相信任何人，除非他们出示暗百合的印记——一朵倒置的百合花。你的父亲。』"

    $ father_letters_found = True
    $ father_death_known = True

    "你合上假书，双手按在桌面上，深深呼吸。"

    "一时间，太多的信息涌入你的脑海。"

    "父亲不只是知道暗百合——他与暗百合有深入的联系。"

    if not testament_forged_known or not father_was_regent_known:
        "先王的遗诏被篡改。父亲本该是摄政者。先王可能是被毒杀的。"
    else:
        "日记中的那些真相在脑海里翻涌——每一条都触目惊心。"

    "而父亲自己的死……"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "暮色之露……同样的毒药？"

    $ hide_all_chars()
    "你想到了一个可怕的可能性——杀害先王的人，也杀害了你的父亲。"

    "现在，同一把刀可能悬在你的头顶。"

    "但父亲的遗言说了——壁炉后面。"

    "你走到壁炉前，仔细观察。"

    "壁炉是用大块的灰色石头砌成的，看起来很普通。但父亲说了一串指令——向左三次，向右两次，再向左一次。"

    "你试着推动壁炉上方的一块石头。"

    "没有反应。"

    "你又试了壁炉侧面的石头。"

    "还是没有。"

    menu:
        "回想父亲日记里的暗号系统" if intrigue >= 60:
            $ change_stat("intrigue", 5)
            "你不去摸石头。你坐下来， 把日记翻到第一页。"
            "父亲所有暗号都是六位组合， 字母用花语代替。「左三右二左一」 = 「蔷薇蔷薇蔷薇 / 罂粟罂粟 / 蔷薇」。"
            "你重新数了壁炉上方的浮雕——六朵花， 顺序是： 蔷薇、玫瑰、罂粟、罂粟、蔷薇、罂粟。"
            "对应他暗号本里某一页的标题——"
            "「藏书在花后」。"
            "你伸手按住对应位置， 一连六个动作精准得没有一次试错。"
            "壁炉后壁缓缓滑开。这扇门， 你从没真的去找过——你父亲早就告诉过你怎么开了。"
            $ secret_passage_found = True

        "仔细观察壁炉的装饰图案":
            $ change_stat("reputation", 5)
            "你退后一步，重新审视壁炉。"
            "壁炉的上方有一排装饰性的浮雕——六朵花。"
            "六朵花……向左三次，向右两次，再向左一次。"
            "你伸手按住第一朵花，向左旋转。咔嗒。"
            "第二朵花，向左。咔嗒。"
            "第三朵花，向左。咔嗒。"
            "第四朵花，向右。咔嗒。"
            "第五朵花，向右。咔嗒。"
            "第六朵花，向左。咔嗒——"
            "轰！"
            "壁炉的整个后壁缓缓滑开了，露出一个黑洞洞的入口。"
            $ secret_passage_found = True

        "尝试按照'左三右二左一'的顺序敲击石砖":
            $ change_stat("reputation", 5)
            "你沿着壁炉的石砖，按照指令的顺序敲击。"
            "左边第一块——没反应。左边第二块——没反应。左边第三块——"
            "你的指节碰到石砖时，感觉这块砖有些松动。"
            "你更用力地按压。砖块向内陷了一寸。"
            "但没有其他反应。你意识到可能不只是敲击，而是需要旋转什么东西。"
            "你重新审视壁炉，终于注意到了上方的花朵浮雕。"
            "按照指令旋转每一朵花后——壁炉后壁缓缓打开了。"
            $ secret_passage_found = True

        "用蛮力推动壁炉":
            $ change_stat("power", 5)
            "你双手按在壁炉上，使出全力推动。"
            "石头纹丝不动。"
            "你不甘心，又狠狠地撞了两下。"
            "壁炉内部传来一声沉闷的「咔嗒」——但不是打开的声音。"
            "是什么东西卡住了。"
            "你试了试壁炉上方的花朵浮雕，但无论怎么旋转，它们都纹丝不动。"
            "机关锁死了。"
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "该死……"
            $ hide_all_chars()
            "父亲留下的线索到此中断了。壁炉后面的秘密，你暂时无法触及。"
            "你只能另寻他法。"
            $ secret_passage_found = False
            jump ch3_no_passage

    "一股陈旧潮湿的空气扑面而来。"

    "壁炉后面是一条狭窄的石阶，向下延伸，消失在黑暗中。"

    "你取了一根蜡烛，犹豫片刻。"

    menu:
        "立刻进入":
            $ change_stat("power", 5)
            "你毫不犹豫地踏上了石阶。手里只有一根蜡烛，腰间没带剑，书房里也没留下字条——没人知道你在下面。"
            "石壁上爬满了苔藓，空气中弥漫着霉味。"
            "你的蜡烛在通道中投下摇曳的影子。"

        "先做好准备再进入":
            $ change_stat("faith", 5)
            $ change_stat("power", 5)
            "你从墙上取下一把短剑，又多拿了几根蜡烛。"
            "在书桌上留了一张纸条——以防万一。这一通收拾花了你小半个时辰；下面要真有人，这会儿也该听见动静走远了。"
            "然后，你踏入了通道。"

        "去找奥尔德里克一起来":
            $ change_rel("rel_aldric", 10)
            $ change_stat("loyalty", 5)
            $ change_stat("intrigue", -8)
            $ aldric_knows_passage = True
            "你决定不独自冒险。你快步走出书房，找到了奥尔德里克。"
            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "密道？我就知道你父亲藏了什么。"
            aldric "走吧，我和你一起去。"
            $ hide_all_chars()
            "有老骑士在身边，你安心了不少。"
            "你们一前一后踏入了通道。"
            "有奥尔德里克在，你不再是独自面对父亲留下的东西。但接下来墙上的每一幅壁画，他都会和你一起看见——父亲跟暗百合的牵连，从此多了一个知情人。"

    ## ============================================================
    ## 第三部分：暗百合的线索（~400行）
    ## ============================================================

label ch3_dark_lily_clues:

    $ set_mood("mystery")
    $ clear_weather()
    $ dark_lily_exists_known = True

    "石阶向下延伸了大约三十步，然后变成了一条水平的隧道。"

    "空气变得阴冷潮湿。你能听到远处有水滴落的声音，在寂静中回响。"

    "你的脚步声在石壁间回荡。"

    "隧道的墙壁上每隔几步就有一个铁制的火把座。你点燃了其中几个。"

    "在火光的照映下，隧道显得比想象中更宽敞。天花板大约有两米高，足以让一个成年人直立行走。"

    "这不是临时挖掘的地道——这是经过精心设计和建造的永久性通道。"

    "石壁被打磨得很光滑。地面铺着整齐的石板。排水沟沿着墙角延伸，把渗水引向远处。"

    "你不禁感叹——建造这条通道的人，投入了巨大的人力和财力。"

    "走了大约五十步后，你看到了隧道壁上刻着的文字和图案。"

    "那些图案和领地内出现的符号一模一样——倒置的百合花。"

    "但这里的图案更精细，周围还环绕着你不认识的古老文字。"

    "你停下脚步，仔细观察这些刻文。"

    "文字的书写方式很古老——你认出了一些字母，但排列方式和现代语言不同。"

    "这可能是两百年前的古老书写体系。你需要一个语言学家才能完全破译。"

    "但有些图案是不需要文字就能理解的——"

    "一幅壁画描绘了一群人围成圈，中间是一朵巨大的百合花。每个人都举起右手，手掌朝向百合花。"

    "宣誓仪式。"

    "另一幅壁画描绘了一个戴王冠的人躺在床上，周围站着七个人。他们的表情悲痛而坚毅。"

    "先王驾崩的场景。"

    "第三幅壁画最让你震动——一个人影站在暗处，手中握着一把匕首，匕首上沾着毒液。匕首指向王冠。"

    "暗杀者。"

    "或者……下毒者。"

    "你继续前行。"

    "隧道在前方分成了两条岔路。"

    "岔路口的石壁上刻着两个符号——左边是一只眼睛，右边是一只手。"

    "眼睛代表什么？手代表什么？你不确定。"

    menu:
        "走左边——那边的墙壁上有更多刻文":
            $ change_stat("reputation", 5)
            "你选择了左边的通道。"
            "这条通道更窄，你不得不侧身才能通过。"
            "但墙壁上的刻文越来越密集，仿佛在讲述一个完整的故事。"
            "你走了大约五分钟，通道突然开阔了——"
            "你来到了一个小房间。房间中央有一张石桌，上面放着一个封了蜡的铁匣。"
            "你打开铁匣。里面有一枚银质徽章，形状正是倒置的百合花。"
            "徽章背面刻着两个字——「信使」。"
            "还有一张羊皮纸，上面画着一幅地图——标注了从城堡到集市的一条秘密路线。"
            "地图上有一个地点被画了圈，旁边写着：「每月望日，子时。」"
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "每月望日……今天是什么日子？"
            $ hide_all_chars()
            "你在心里算了算。今天正好是望日。"
            "这是命运的安排，还是某种巧合？"

        "走右边——那边有微弱的光线" if intrigue >= 45:
            $ change_stat("intrigue", 8)
            "你选择了右边的通道。"
            "越往前走，空气越清新，你甚至能感觉到微弱的风。"
            "这条通道最终通向了一个隐藏的出口——城堡外墙下方的一个排水口。"
            "你小心地探出头，发现自己在城堡北面的树丛中。"
            "地面上有新鲜的脚印。有人最近走过这条通道。"
            "你沿着脚印追踪了一段距离。脚印指向了集市的方向。"
            "你决定回去，先做好准备，然后去集市调查。"

    "不管走了哪条路，你都得到了一个关键信息——暗百合的线索指向了集市。"

    "你从密道返回书房，整理了一下发现的物品和信息。"

    $ collect_item("letter_father_2")

    "密道的存在证实了你的猜测——城堡下面有一个完整的地下网络，而暗百合对它了如指掌。"

    "你的父亲也是这个网络的一部分。"

    "现在，你需要做出下一步的决定——去集市，找到暗百合的联络人。"

    "但你不能大张旗鼓地去。作为领主，你的脸太容易被认出来了。"

    "你叫来了一个信任的侍女，让她帮你找一套普通人的衣服——粗布衬衫、麻布裤子、一件带兜帽的旧斗篷。"

    "穿上这些衣服后，你照了照镜子。"

    "镜子里的人看起来像一个普通的旅行者，或者一个落魄的商人。脸上的那道疤痕反而给你增添了几分风霜感。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "应该不会被认出来。"

    "你把短剑藏在斗篷里，把银质徽章贴身收好，然后从城堡的侧门溜了出去。"

    scene bg market with dissolve
    $ unlock_gallery("bg_market")
    $ play_music("audio/music/market_bustle.ogg", fadein=2.0)

    "傍晚时分的集市热闹非凡。"

    "商贩们的叫卖声此起彼伏。铁匠的锤击声、牲口的嘶鸣声、孩子的笑声——汇成一片喧嚣。"

    "空气中弥漫着烤肉、面包和啤酒的味道。几个醉汉在酒馆门口高唱着不着调的歌。"

    "你低着头穿过人群。偶尔有人撞到你的肩膀，但没人多看你一眼。"

    "你在人群中注意到了一些细节——"

    "卖水果的摊贩偷偷往几个水果上画了百合花的标记。"

    "一个修鞋匠的摊位上挂着一面旗帜，旗帜的角落里绣着一朵几乎看不见的百合花。"

    "他们是暗百合的人？还是只是巧合？"

    "你继续走。沿着密道中发现的地图指引，穿过拥挤的人群，来到集市的东北角。"

    "这里是一条幽暗的小巷。一家不起眼的草药铺还亮着灯。"

    "店铺的招牌上写着——「百合草药」。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "百合草药……"

    $ hide_all_chars()
    "你推门而入。"

    "一个老妇人坐在柜台后面，正在研磨什么东西。她没有抬头。"

    hide player_char_img
    $ hide_all_chars("lily_root_img")
    show lily_root_img at left with dissolve
    apothecary "客人要什么？治感冒？补身子？还是……别的？"

    "你注意到她的围裙上绣着一朵百合花——不是倒置的，但你直觉告诉你这不是巧合。"

    menu:
        "什么都不出示——直接报出几个内部暗号" if intrigue >= 70:
            $ change_stat("intrigue", 5)
            $ change_rel("rel_lily", -5)  ## 厚度: 外人能背出内部暗号=安全漏洞, 暗百合从一开始就提防你
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "「七瓣莲花将在月圆之夜绽放」。「壁炉后的人没有倒下」。"
            $ hide_all_chars()
            "老妇人的研磨棒停了。她看了你三秒， 然后慢慢转身， 把店门口的木牌翻成了「已打烊」。"
            $ hide_all_chars("lily_root_img")
            show lily_root_img at left with dissolve
            apothecary "你哪里学来的？"
            hide lily_root_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我父亲留给我一本日记。我翻得不下百遍。"
            $ hide_all_chars()
            "她盯着你， 终于叹了口气。"
            $ hide_all_chars("lily_root_img")
            show lily_root_img at left with dissolve
            apothecary "一个外人能一字不差地报出我们的暗号——你知道这说明什么吗？说明这套暗号已经不安全了。"
            apothecary "你父亲怎么知道的， 你又记了多少——这些我们迟早要问清楚。在那之前， 你在我们眼里不是自己人， 是个会走路的窟窿。"
            apothecary "跟我来。"
            "她推开了柜台后面的一扇暗门。门轴的声音很轻， 但她让你走在前面——她不放心把背留给你。"

        "出示在密道中找到的银质徽章" if intrigue >= 45:
            $ change_stat("intrigue", 8)
            $ hide_all_chars()
            "你从怀中取出那枚银质徽章，放在柜台上。"
            "老妇人终于抬起头来。她的眼睛在看到徽章的一瞬间猛然睁大。"
            $ hide_all_chars("lily_root_img")
            show lily_root_img at left with dissolve
            apothecary "你……你是怎么得到这个的？"
            hide lily_root_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我父亲留给我的。"
            "老妇人盯着你看了很久。然后她慢慢站起身，走到门口，把「营业中」的牌子翻成了「已打烊」。"
            hide player_char_img
            $ hide_all_chars("lily_root_img")
            show lily_root_img at left with dissolve
            apothecary "跟我来。"
            "她推开了柜台后面的一扇暗门。"

        "提起暗百合的名字":
            $ change_stat("intrigue", 5)
            hide lily_root_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我不是来买药的。我想找暗百合。"
            "老妇人的研磨动作停了一秒，然后恢复了正常。"
            hide player_char_img
            $ hide_all_chars("lily_root_img")
            show lily_root_img at left with dissolve
            apothecary "暗百合？没听说过。您是在说花吗？百合花我们有卖。"
            hide lily_root_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你知道我说的不是花。"
            "你直视她的眼睛。"
            player "我是艾登堡的领主。我父亲和暗百合有联系。他已经不在了。现在，我需要找到他们。"
            "老妇人沉默了片刻。然后她锁上了门。"
            hide player_char_img
            $ hide_all_chars("lily_root_img")
            show lily_root_img at left with dissolve
            apothecary "……你确实长得像老领主。跟我来。"

        "假装普通客人，暗中观察":
            $ change_stat("intrigue", 5)
            hide lily_root_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "帮我配一副安神药。"
            hide player_char_img
            $ hide_all_chars("lily_root_img")
            show lily_root_img at left with dissolve
            apothecary "好的。需要加蜂蜜吗？"
            $ hide_all_chars()
            "你一边等她配药，一边暗中打量这间店铺。"
            "柜台后面的架子上摆满了各种草药，但有一个角落被布帘遮住了。"
            "你隐约看到布帘后面有一扇门。"
            "你付了药钱，走出店铺，但并没有走远。"
            "你在暗处等了一个小时。"
            "终于，一个蒙面人从店铺的侧门走了出来。"
            "你悄悄跟了上去。"
            "蒙面人在小巷中七拐八拐，最终闪进了一栋废弃建筑的后门——门在身后无声合上。"
            "你记住了这个地点。明天晚上，你要再来。"
            jump ch3_study_return

    "老妇人带着你穿过暗门，走下一段陡峭的楼梯。"

    "楼梯尽头是一间地下室。地下室很小，但收拾得很干净。"

    "四面墙上挂着黑色的帷幕，中央是一张圆桌。桌上放着一盏油灯和几张地图。"

    "地下室里有两个人在等着。一名老妇人坐在桌后，旁边站着一个沉默的男子，都戴着面具。"

    "老妇人开口了。"

    $ hide_all_chars("lily_root_img")
    show lily_root_img at left with dissolve
    lily_interviewer "老领主的孩子？"

    hide lily_root_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "是。我是艾登堡的新领主。"

    hide player_char_img
    $ hide_all_chars("lily_root_img")
    show lily_root_img at left with dissolve
    lily_interviewer "你来这里想要什么？"

    hide lily_root_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "真相。"

    "老妇人和身旁的男子交换了一个眼神。"

    hide player_char_img
    $ hide_all_chars("lily_root_img")
    show lily_root_img at left with dissolve
    lily_interviewer "在得到真相之前，你需要通过一个考验。"

    hide lily_root_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "什么考验？"

    hide player_char_img
    $ hide_all_chars("lily_root_img")
    show lily_root_img at left with dissolve
    lily_interviewer "信任的考验。"

    "老妇人从桌上拿起一杯酒，递到你面前。"

    lily_interviewer "喝下它。"

    menu:
        "毫不犹豫地喝下":
            $ hide_all_chars()
            "你接过酒杯，一饮而尽。"
            if intrigue >= 45:
                ## backlog7·检定重写: 门槛移入体内两档化 — 识破药性稳住舌头 vs 药性上头说漏嘴
                $ change_stat("intrigue", 8)
                $ change_rel("rel_lily", 10)
                "酒液入喉，带着一股苦涩的草药味。舌根一麻——你认出来了：吐真草。这不是敬酒，是审讯。"
                "你顺着药劲说话，句句是真，但每句都停在该停的地方。"
                $ hide_all_chars("lily_root_img")
                show lily_root_img at left with dissolve
                lily_interviewer "……你的胆量，像你父亲。舌头比他还稳。"
            else:
                $ change_rel("rel_lily", 5)
                $ change_stat("reputation", -3)
                "酒液入喉，带着一股苦涩的草药味。你的视线模糊了一瞬——然后话就自己往外走了。"
                "等你咬住舌头，已经把翻过父亲书房暗格的事说了出去。老妇人一动不动地听着。"
                $ hide_all_chars("lily_root_img")
                show lily_root_img at left with dissolve
                lily_interviewer "胆量像你父亲。可惜舌头嫩了些——吐真草面前，嫩舌头是要吃亏的。"
                "你不知道这句话会传到多少人的耳朵里。"
            "老妇人摘下了面具。一张布满皱纹却眼神锐利的脸，左眼下方有一道淡淡的旧伤疤。"
            lily_interviewer "我是暗百合的联络人。你可以叫我'根'。"

        "先闻一闻":
            $ change_stat("reputation", 5)
            $ hide_all_chars()
            "你接过酒杯，凑近鼻子。"
            "一股浓烈的草药味。你认出了其中几种——薄荷、迷迭香……还有一种你不认识的味道。"
            hide lily_root_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "这是什么？"
            hide player_char_img
            $ hide_all_chars("lily_root_img")
            show lily_root_img at left with dissolve
            lily_interviewer "一种古老的草药配方。无害。但它能让人暂时无法说谎。"
            hide lily_root_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "真话药？"
            hide player_char_img
            $ hide_all_chars("lily_root_img")
            show lily_root_img at left with dissolve
            lily_interviewer "可以这么理解。喝了它，我们会问你几个问题。你的回答将决定你是否值得信任。"
            "你犹豫了一下，然后喝了下去。"
            $ change_rel("rel_lily", 5)

        "拒绝喝" if power >= 55:
            $ change_stat("power", 10)
            $ change_rel("rel_lily", -5)
            hide lily_root_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我不喝来路不明的东西。"
            hide player_char_img
            $ hide_all_chars("lily_root_img")
            show lily_root_img at left with dissolve
            lily_interviewer "那你怎么证明你值得信任？"
            hide lily_root_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我来到这里，就是我的诚意。如果我想对付你们，可以带一队士兵来。"
            "他打量了你一番。"
            hide player_char_img
            $ hide_all_chars("lily_root_img")
            show lily_root_img at left with dissolve
            lily_interviewer "……也有道理。那我们换一种方式。"
            lily_interviewer "回答我三个问题。如果你的回答让我满意，我会带你见我们的首领。"

    "无论你选择了什么，接下来都是一连串的问题。"

    lily_interviewer "第一个问题——你为什么要找暗百合？"

    menu:
        "为了查明父亲的死因":
            hide lily_root_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我的父亲不是自然死亡。我要找出真相。"
            hide player_char_img
            $ hide_all_chars("lily_root_img")
            show lily_root_img at left with dissolve
            lily_interviewer "复仇……一个容易理解的动机。但查真相和报私仇,走的不一定是同一条路。"

        "为了对抗王后和教会":
            hide lily_root_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "如果父亲的日记所言属实，那王后和教会欠我一个交代。"
            hide player_char_img
            $ hide_all_chars("lily_root_img")
            show lily_root_img at left with dissolve
            lily_interviewer "你想要复仇？"
            hide lily_root_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我想要正义。"
            hide player_char_img
            $ hide_all_chars("lily_root_img")
            show lily_root_img at left with dissolve
            lily_interviewer "希望你能分清这两者的区别。"

        "为了保护领地和领民":
            hide lily_root_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "有人在暗中威胁我的领地。农民失踪，符号出现——我需要知道发生了什么。"
            hide player_char_img
            $ hide_all_chars("lily_root_img")
            show lily_root_img at left with dissolve
            lily_interviewer "你关心的是领民……这很好。"

    lily_interviewer "第二个问题——如果查出真相后，发现你必须与整个王国为敌，你怎么办？"

    menu:
        "为了真相，即使与世界为敌也在所不惜":
            $ change_stat("faith", 5)
            hide lily_root_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "真相不应该被埋没。不管代价多大。"
            hide player_char_img
            $ hide_all_chars("lily_root_img")
            show lily_root_img at left with dissolve
            lily_interviewer "那不是勇气,是鲁莽。一个年轻领主单挑整个王国,只会被磨成齑粉。我们不需要烈士。"

        "我会寻找盟友，集聚力量，再做打算":
            $ change_stat("loyalty", 5)
            hide lily_root_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "一个人对抗整个王国是愚蠢的。我会寻找志同道合的人。"
            hide player_char_img
            $ hide_all_chars("lily_root_img")
            show lily_root_img at left with dissolve
            lily_interviewer "现实的想法。但'集聚力量'要时间,而时间正是我们缺的。所以我们才需要你。"

        "我会权衡利弊，选择对领地最有利的道路":
            $ change_stat("wealth", 5)
            $ change_stat("power", 5)
            hide lily_root_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "真相重要，但我的领民更重要。我会根据情况做出判断。"
            hide player_char_img
            $ hide_all_chars("lily_root_img")
            show lily_root_img at left with dissolve
            lily_interviewer "权衡利弊。可在我们这场仗里,对领地最有利的路,常常意味着背叛。你清楚自己要卷进什么吗?"

    lily_interviewer "最后一个问题——你信任你身边的人吗？"

    menu:
        "我只信任自己":
            $ change_stat("power", 5)
            hide lily_root_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "在这个世界上，只有自己是可靠的。"
            hide player_char_img
            $ hide_all_chars("lily_root_img")
            show lily_root_img at left with dissolve
            lily_interviewer "那意味着你会拒绝我们伸出的手。一个孤身一人的领主,熬不过第一个冬天。"

        "我信任奥尔德里克和雷恩":
            $ change_stat("loyalty", 5)
            hide lily_root_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "有几个人是我可以依靠的。但信任也有限度。"
            hide player_char_img
            $ hide_all_chars("lily_root_img")
            show lily_root_img at left with dissolve
            lily_interviewer "有限度的信任……这倒是健康的态度。"

        "我正在学习信任谁":
            $ change_stat("reputation", 5)
            hide lily_root_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "信任是需要时间验证的。我还在观察。"
            hide player_char_img
            $ hide_all_chars("lily_root_img")
            show lily_root_img at left with dissolve
            lily_interviewer "最好的回答。你父亲花了十年才开始信任我们。"

    lily_interviewer "很好。你通过了。"

    $ lily_trial_passed = True

    lily_interviewer "三天后的子时，来城外的废弃磨坊。我们的首领会亲自见你。"

    $ hide_all_chars()
    "你点了点头，转身离开。"

    "走出草药铺时，夜空中星辰满布。你抬头看了一眼天。三天后，子时，废弃磨坊。"

    jump ch3_study_return

## ============================================================
## 蛮力路线 — 密道被锁死，走替代路线
## ============================================================

label ch3_no_passage:

    "壁炉后的秘密暂时无法触及。但你还有父亲的日记。"

    "你重新坐回书桌前，继续破译那本密码日记。"

    "虽然无法进入密道，但日记中的线索仍然指向了一个地方——"

    "『如果壁炉的机关无法打开，不要绝望。去集市东北角的百合草药铺。那里是暗百合的一个联络点。铺子的老妇人叫「根」——出示你的家族印戒，她会认出你。』"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "集市的草药铺……"

    $ hide_all_chars()
    "父亲果然留了后手。即使一条路断了，还有另一条路。"

    "但没有密道中的信使徽章，你该如何证明自己的身份？"

    "你翻遍了书房的暗格，在一个上锁的小铁匣里找到了一封父亲的亲笔信——"

    "信封上写着：「交给根」。"

    $ collect_item("letter_father_2")

    "你把信贴身收好。"

    "你叫来了一个信任的侍女，让她帮你找一套普通人的衣服——粗布衬衫、麻布裤子、一件带兜帽的旧斗篷。"

    "穿上后，镜子里的人像一个落魄的旅行者。脸上的疤痕反而增添了几分风霜感。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "应该不会被认出来。"

    "你把短剑藏在斗篷里，从城堡侧门溜了出去。"

    scene bg market with dissolve
    $ unlock_gallery("bg_market")
    $ play_music("audio/music/great_hall.ogg", fadein=2.0)

    "傍晚的集市热闹非凡。叫卖声、锤击声、笑声——汇成一片喧嚣。"

    "没有密道中的地图指引，你只能凭日记中的描述去找。"

    "东北角。百合草药。"

    "你在集市中穿行，留意着每一个可能的线索。"

    "一个卖水果的摊贩偷偷往几个水果上画了百合花标记。"

    "一个修鞋匠的旗帜角落绣着一朵几乎看不见的百合花。"

    "你沿着这些隐秘的标记，最终来到集市东北角的一条幽暗小巷。"

    "一家不起眼的草药铺还亮着灯。招牌上写着——「百合草药」。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "百合草药……"

    $ hide_all_chars()
    "你推门而入。"

    "一个老妇人坐在柜台后面，正在研磨什么东西。她没有抬头。"

    hide player_char_img
    $ hide_all_chars("lily_root_img")
    show lily_root_img at left with dissolve
    apothecary "客官买什么药？"

    menu:
        "出示父亲的亲笔信":
            hide lily_root_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "这是我父亲留给你的。"
            $ hide_all_chars()
            "老妇人接过信，仔细看了看信封上的笔迹。"
            "她的手微微颤抖。"
            hide player_char_img
            $ hide_all_chars("lily_root_img")
            show lily_root_img at left with dissolve
            apothecary "你是……老领主的孩子？"
            hide lily_root_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "是的。"
            "老妇人盯着你看了很久。然后她站起身，走到门口，翻过了「营业中」的牌子。"
            hide player_char_img
            $ hide_all_chars("lily_root_img")
            show lily_root_img at left with dissolve
            apothecary "跟我来。"

        "出示家族印戒":
            $ hide_all_chars()
            "你从怀中取出那枚金鹰印戒。"
            "老妇人的目光落在印戒上，瞳孔骤然收缩。"
            $ hide_all_chars("lily_root_img")
            show lily_root_img at left with dissolve
            apothecary "金鹰……你是艾登堡的继承人？"
            hide lily_root_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我父亲让我来找你。"
            "老妇人的目光在戒指和你的脸之间来回移动。然后她走到门口翻过了牌子。"
            hide player_char_img
            $ hide_all_chars("lily_root_img")
            show lily_root_img at left with dissolve
            apothecary "跟我来。"

    $ hide_all_chars()
    "她带你穿过后院，来到一间隐蔽的地下室。"

    "和密道相比，这里简陋得多。但墙上挂着一幅百合花旗帜，桌上堆满了卷轴和信件。"

    $ hide_all_chars("lily_root_img")
    show lily_root_img at left with dissolve
    lily_root "你父亲是我们最重要的盟友之一。他的死……是一个巨大的损失。"

    hide lily_root_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我在他的日记中得知了暗百合的存在。但壁炉后的机关被我弄坏了。"

    hide player_char_img
    $ hide_all_chars("lily_root_img")
    show lily_root_img at left with dissolve
    lily_root "机关锁死了？"

    "老妇人叹了口气。"

    lily_root "那条密道是你父亲花了好几年修建的。但也罢——密道只是工具，重要的是你来了。"

    lily_root "我叫'根'。暗百合在艾登堡的联络人。"

    lily_root "你父亲留下了太多未完成的事。而你的敌人，不会给你太多时间。"

    lily_root "三天后的子时，来城外的废弃磨坊。我们的首领会亲自见你。"

    $ hide_all_chars()
    "你点了点头，转身离开。"

    "走出草药铺时，夜空中星辰满布。虽然没有找到密道，但你找到了暗百合的人。"

    "也许这条路更难走。不过，你不是一个人。"

    jump ch3_study_return_no_passage

label ch3_study_return_no_passage:

    scene bg study with dissolve
    $ unlock_gallery("bg_study")
    $ play_music("audio/music/castle_calm.ogg", fadein=2.0)

    "回到城堡后，你把今天的发现整理了一遍。"

    "父亲的密码日记、集市上的暗百合联络人——"

    "虽然壁炉后的密道被锁死了，但你仍然找到了通往真相的道路。"

    "你在书桌上铺开一张大羊皮纸，开始画线索图。"

    "中心写着「父亲之死」。"

    "「暗百合」——父亲的盟友，草药铺是联络点。"
    if bishop_confession_done or matthias_has_testament_known or testament_original_obtained:
        "「教会」——费雷恩篡改遗诏。马修斯当年亲眼见证，私藏了原本。"
    else:
        "「教会」——费雷恩篡改遗诏，马修斯可能知情。"
    "「王后」——最大的嫌疑人。"
    "「冯·哈根男爵」——行为可疑。"

    "你坐在书桌前，继续翻看日记。"

    "随着破译的深入，一个令人不安的事实浮出水面——父亲反复提到一个他称之为'影'的人。"

    "『影今天又来了。她带来了一个惊人的消息——教会大主教费雷恩在去年已经秘密去世了。接任者是他的学生马修斯。但马修斯并不知道篡改遗诏的全部真相。』"

    "『影的真实身份我始终不知道。她从不摘下面纱。但她的声音很年轻——也许三十出头。』"

    "『影最后一次来见我是在三个月前。她说她感觉到了危险。如果她失去联系，让我去百合草药铺找根。』"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "影……会是谁？"

    $ hide_all_chars()
    "你继续翻看日记。后面的内容越来越沉重——"

    "『我的身体每天都在衰弱。暮色之露的效果越来越明显了。我估计自己最多还有半年。』"

    "你合上日记，揉了揉疲惫的眼睛。"

    "窗外，天已经泛白了。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "父亲，你放心。就算密道打不开，我也会找到真相。"

    ## 跳过密道探索，直接进入暗百合总部
    jump ch3_dark_lily_hq

label ch3_study_return:

    scene bg study with dissolve
    $ unlock_gallery("bg_study")
    $ play_music("audio/music/castle_calm.ogg", fadein=2.0)

    "回到城堡后，你把今天的发现整理了一遍。"

    "父亲的密码日记、壁炉后的密道、集市上的暗百合联络人——"

    "拼图正在慢慢成形，但你知道，还有很多碎片缺失。"

    "你在书桌上铺开一张大羊皮纸，开始画一幅初步的线索图。"

    "中心写着「父亲之死」。"

    "从中心延伸出三条线——"

    "「暗百合」——父亲的盟友，但内部有叛徒。"

    if bishop_confession_done or matthias_has_testament_known or testament_original_obtained:
        "「教会」——费雷恩篡改遗诏。马修斯当年亲眼见证，私藏了原本。暮色之露来源于教会。"
    else:
        "「教会」——费雷恩篡改遗诏，马修斯可能知情。暮色之露来源于教会。"

    "「王后」——最大的嫌疑人。可能毒杀了先王，也可能是杀害父亲的幕后黑手。"

    "你又在旁边加了一条——「冯·哈根男爵」。他的行为一直可疑。"

    "看着这幅图，你感到一阵眩晕。这比你想象的要复杂得多。"

    "你坐在书桌前，翻开那本伪装成《边境防御手册》的日记，继续破译。"

    "随着你越读越多，一个令人不安的事实浮出水面——"

    "父亲在日记中反复提到一个人。一个他称之为'影'的人。"

    "『影今天又来了。她带来了一个惊人的消息——教会大主教费雷恩在去年已经秘密去世了。接任者是他的学生马修斯。但马修斯并不知道篡改遗诏的全部真相。他只知道一部分。』"

    "『影说，马修斯是被利用的棋子。真正的操纵者，始终是王后。』"

    "你继续翻页。"

    "『影的真实身份我始终不知道。她从不摘下面纱。但她的声音很年轻——也许三十出头。』"

    "『她的知识面极广，从炼金术到政治阴谋，无所不知。我有时候怀疑她是不是某个贵族家庭出身的女子。』"

    "『但暗百合的规矩是不问出身，不问过去。我只需要知道她是可靠的就够了。』"

    "『影最后一次来见我是在三个月前。她说她感觉到了危险——暗焰的人可能已经查到了她的行踪。』"

    "『她说如果她失去联系，让我去集市东北角的百合草药铺。那里是暗百合的一个联络点。』"

    "『铺子的老妇人叫'根'——她是暗百合最资深的联络人之一。只要出示信使徽章，她会帮助你。』"

    "百合草药铺。你今天去过了。"

    "父亲的日记、密道中的徽章、集市上的草药铺，开始指向同一个地方。"

    "你的父亲为你铺设了一条完整的线索链。他知道自己可能保不住命，所以提前做好了准备。"

    "你的手指在那一页上停了很久。"

    "你继续翻看日记。后面的内容越来越沉重——"

    "『我的身体每天都在衰弱。暮色之露的效果越来越明显了。我估计自己最多还有半年。』"

    "『在这半年里，我必须把所有的线索都安排好。密道的入口、日记的密码、联络人的位置——每一环都不能出错。』"

    "『如果我的孩子找不到这些线索，那一切就真的结束了。二十年的调查、先王的冤屈、暗百合的牺牲——都会化为乌有。』"

    "『我不能让这种事发生。』"

    "『今天把最后一封信藏好了。壁炉后面的密道入口是最后一道防线。』"

    "『我在六朵花的机关上增加了一个新的保护——如果有人用错误的顺序操作三次，机关会锁死，密道入口将永远无法打开。这是为了防止敌人暴力破解。』"

    "『我的孩子——如果你读到这里，请记住：向左三次，向右两次，再向左一次。千万不要搞错顺序。』"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我……差点搞错了。"

    $ hide_all_chars()
    "你回想起刚才操作壁炉机关的情景。父亲在机关上设置了保护——错误操作三次就会锁死。"

    "你这才明白，刚才在壁炉前若是急着乱试，机关早就锁死了。"

    "父亲把最后一道防线藏在了顺序里。"

    "你合上日记，揉了揉疲惫的眼睛。"

    "窗外，天已经泛白了。你在书房里待了整整一夜。"

    "但你不觉得累。太多的真相等着你去发掘。"

    "你走到窗边，看着第一缕晨光照在城堡的塔楼上。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "父亲，你放心。我不会辜负你的期望。"

    "你低声说，仿佛在对远方的亡灵许下承诺。"

    ## ============================================================
    ## 第四部分：密道探索（~500行）
    ## ============================================================

label ch3_tunnel_exploration:

    $ play_music("audio/music/tension.ogg", fadein=2.0)
    scene bg study with dissolve
    $ unlock_gallery("bg_study")

    "第二天傍晚，你决定彻底探索壁炉后的密道系统。"

    "你带上了短剑、火把、绳索和一壶水。"

    if secret_passage_found:
        "既然已经打开了壁炉的机关，再次进入并不困难。"
    else:
        "你按照父亲日记中的指示，打开了壁炉后的通道。"
        $ secret_passage_found = True

    scene bg underground with dissolve
    $ unlock_gallery("bg_underground")

    "你沿着石阶向下走去。这一次，你要走得更深。"

    "之前你已经探索了前面的岔路。但在岔路的更深处，你发现了第三条通道——一条被坍塌的碎石半掩的狭窄通路。"

    "你花了半个小时清理碎石，终于打通了通路。"

    "通道在这里变得更宽阔了，天花板也高了许多。"

    "你举高火把，看到了让你屏息的景象——"

    "墙壁上刻满了壁画。"

    "壁画描绘的是王国建立之初的历史：一位戴着王冠的骑士率领军队征服了这片土地。"

    "骑士的身边有七个人——七名近卫。"

    "每一名近卫的胸前都刻着一个标记。"

    "你辨认出了其中一个——倒置的百合花。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "暗百合……是先王的七近卫之一。"

    $ hide_all_chars()
    "壁画的最后一幅——"

    "先王临终的场景。他躺在床上，把一份文书交给了站在床边的七近卫。"

    "但有一个人站在阴影中，手里拿着另一份文书——表情阴鸷，目光中充满了贪婪。"

    "那个人戴着一顶王冠……不，是一顶王后的冕冠。"

    "你继续前行。"

    "通道再次分叉。这一次是三条路。"

    "左边的通道里有微弱的光亮。"
    "中间的通道传来水流声。"
    "右边的通道一片漆黑，但地面上有新鲜的脚印。"

    menu:
        "走左边——有光的地方":
            $ change_stat("reputation", 5)
            "你走向光亮。"
            "通道拐了两个弯后，空气中的温度开始变化——不再阴冷，反而有一种干燥温暖的感觉。"
            "光亮越来越强。你灭掉火把，仅靠通道中的光线就足以看清路。"
            "最终，你来到了一个相当大的房间。"
            "你站在门口，呆住了。"
            "房间的四面墙上镶嵌着发光的矿石——某种你从未见过的荧光矿物，散发着幽蓝的微光。"
            "矿石的排列不是随机的——它们形成了精美的图案，像星空一样布满整个天花板。"
            "房间大约有大厅的一半大小。四面墙壁上安装着木质的架子，上面整齐地摆放着卷轴和书籍。"
            "房间中央有一个石质的圆台，上面也摆满了卷轴。"
            "你环顾四周，用力眨了下眼。"
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "这是……一个地下图书馆？"
            $ hide_all_chars()
            "这里是一个资料库——暗百合的资料库。"
            "你走到圆台前，小心地拿起第一卷卷轴。"
            "羊皮纸已经发黄，但保存得非常好。干燥温暖的环境和矿石散发的微光似乎有某种防腐的效果。"
            "你翻开了第一卷。"
            "标题写着：《暗百合创始录》。"
            "『先王格里菲斯一世建国之初，设七近卫以护王座。七近卫各司其职：剑卫护身、盾卫守城、幽卫暗察、鹰卫传讯、根卫通商、桥卫联络、莲卫守秘。暗百合即莲卫所创，取百合倒悬之形，意为隐于暗中、守护光明。后世暗百合分裂时，正统派承'影'之名（取莲卫之暗察遗风），是为下文影卫一脉——并非七近卫之幽卫。』"
            "第一卷记录了暗百合的起源——它确实是先王的七近卫之一建立的，目的是守护先王的真正遗愿。"
            "你在架子最底层抽出一卷更薄的——《六卫终录》。莲卫之外的六卫，下场都记在这里。"
            "『剑卫护身。先王崩，所护已无，遂解。残部老死于无名。』"
            if ch1_deep_old_guard_story:
                "「残部老死于无名。」你在这行字上停了一会儿。"
                "西塔上那把剑还立在你的房里。柄尾磨平的记号，那个不肯留名的老头——老弗雷德里克问了四十三年没问出来的答案，原来写在这里。"
            "『盾卫守城。其守备之法为王后所取，并入王室禁军。今日宫墙之上仍循其制。』"
            "『鹰卫传讯。信鸽驿骑之网未断，散落各城，识其暗记者，仍可凭之通信。』"
            "『根卫通商。化整为零，没入南方诸商会。商路之上犹有其影。』"
            "『幽卫暗察。无主而自散，渐成游散耳目，受雇于出价之人。』"
            if ch2_baron_emissary_intercepted:
                "「受雇于出价之人。」你想起哈伦堡城门外那个深色斗篷的人——不是本地口音，拿了卷轴就往王后旧领的方向去。原来那一行人，几百年前就有了名字。"
            "『桥卫联络。分裂之际不知所踪，至今无人再见其标记。』"
            "你合上卷册。先王立七卫护王座，如今只剩莲卫一脉，以暗百合之名活到今天。"
            "你把鹰卫那一条又看了一遍——『识其暗记者，仍可凭之通信』。你记下了那个暗记的样子：一只展翅的鸟，刻在食指内侧。说不定哪天用得上。"
            $ knows_eagle_network = True
            "根卫那一条旁边画着另一个记号：一团缠绕的树根。批注小字写着——『多刻于秤杆底端、门楣角上』。你也记下了。"
            $ knows_root_network = True
            "桥卫那一条的页脚也画着记号：三道弧线，叠成一座拱桥。批注只有半句——『此记已绝』。"
            "一个再也不会出现的记号。你不知道为什么，还是把它记住了。"
            "你继续翻看第二卷。"
            "标题：《历代影主志》。"
            "第二卷记录了组织的传承——从建立到现在，已经有十七代首领。"
            "每一代首领的记载都包括他们的代号、任期和主要事迹。"
            "你注意到第十二代影主的记载特别长——"
            "『第十二代影主'霜'。任期四十三年。她是暗百合历史上任期最长的首领。在她的领导下，暗百合从一个小型护卫组织发展成了覆盖整个王国的情报网络。但也是在她的晚年，组织内部出现了第一次严重的分歧。』"
            "第三卷的标题让你心头一紧——《分裂纪事》。"
            "『第十四代首领之后，暗百合分裂为三个派系：'"
            "『影卫——忠于先王遗志，誓死守护遗诏。首领代号为'影'。影卫主张通过和平手段、情报战和外交施压来恢复正统。他们相信暴力只会带来更多的暴力。』"
            "『铁刺——主张武力推翻王后，恢复正统。首领代号为'棘'。铁刺认为和平手段太慢、太软弱。他们在边境地区招募退伍军人和不满的农民，组建了一支秘密武装。』"
            "『暗焰——已被王后收买，成为叛徒。首领代号为'烬'。暗焰的成员大多是被利诱或威胁而叛变的。他们的任务是从内部瓦解暗百合，并向王后提供关于暗百合行动的情报。』"
            $ darkflame_known = True
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "三个派系……"
            $ hide_all_chars()
            "暗百合并不是铁板一块。内部的分歧和矛盾，比表面看到的深得多。"
            "你又翻了几卷——发现了一份暗焰叛徒的名单。"
            "名单很长，但大多数名字你不认识。只有一个名字让你心里一沉——"
            "名单的最后一行，用红墨写着一个问号，旁边备注：「疑似暗焰高层。身份待确认。代号——烬。」"
            "暗焰的首领'烬'——至今身份不明。"
            "难怪之前有人试图暗杀你——那可能是暗焰派系干的。"
            "你把几份重要的卷轴塞进怀中。这些资料太珍贵了，你需要仔细研读。"
            $ change_stat("reputation", 5)

        "走中间——有水声的地方":
            $ change_stat("wealth", 5)
            "你走向水声。"
            "通道的地面开始变得湿滑。你不得不放慢脚步，紧贴墙壁行走。"
            "水声越来越大，从轻柔的滴答声变成了哗哗的流水声。"
            "通道越来越潮湿，最终你来到了一条地下河。"
            "河水在荧光矿石的映照下泛着幽蓝的光，像一条流动的星河。"
            "河水不深，大约到膝盖。水温出奇地温暖——也许地下有温泉。"
            "你脱掉靴子，趟水走了一段。河底是光滑的卵石，走起来并不困难。"
            "河道拐了一个弯后，你发现了一个令人惊讶的东西——"
            "河岸上有一条小船。船身很窄，只能坐一个人。船桨靠在船舷上。"
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "有人用船在这里来往？"
            $ hide_all_chars()
            "你检查了小船。船身保养得很好，木头上涂了防水的桐油。"
            "船底有一些新鲜的水渍——说明最近有人用过。"
            "你决定上船，看看河水通向哪里。"
            "你划着小船顺流而下。河道在黑暗中蜿蜒，偶尔有荧光矿石照亮一段路。"
            "大约划了十分钟，你看到了前方有光——自然光。"
            "河道的出口在一片茂密的灌木丛后面。你小心地探出头。"
            "这是城堡北面的树林。出口隐藏在一个小瀑布的后面。"
            "你在河岸上发现了几个脚印。有人经常走这条路。"
            "脚印有大有小——至少有三个不同的人经常使用这条水路。"
            "你记住了这个出口的位置。然后划船原路返回。"
            "这条水路可以在紧急情况下用来撤离——这是一个重要的发现。"
            $ change_stat("wealth", 5)

        "走右边——追踪脚印" if intrigue >= 45:
            $ change_stat("intrigue", 8)
            "你蹲下来仔细观察脚印。"
            "脚印很小——是女人的脚印。而且很新，可能就在几个小时前留下的。"
            "你心中一动。城堡里的女性并不多——侍女、厨娘、还有……艾琳娜。"
            "你沿着脚印追踪。通道七拐八拐，你几乎迷失了方向。"
            "好在你带了绳索——你每到一个岔路口就在墙壁上做一个标记，确保能找到回去的路。"
            "通道的结构越来越复杂。有些地方甚至出现了阶梯——有向上的，有向下的。"
            "你开始意识到，这个密道系统远比你想象的庞大。它不只是连接书房和外部的通道——"
            "它连接了城堡内部的多个房间。"
            "脚印在一个分岔口分成了两组——一组向左，一组向右。"
            "你跟着向右的脚印走。通道变得狭窄，你不得不弯腰才能通过。"
            "最终，脚印消失在一面看似普通的石墙前。"
            "你推了推石墙——它是活动的。"
            "你只推开了一条缝，透过缝隙向里面看——"
            "你看到了一个女人的身影。她坐在桌前，正在写什么东西。"
            "有人走过门口，桌上的烛焰横了一下，又直了回来。"
            "是艾琳娜。"
            "你瞪大了眼睛。"
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "艾琳娜……她知道密道的存在？"
            $ hide_all_chars()
            "你看到她把写好的纸条折好，放进一个信封。然后她站起身，走到窗边，把信封绑在一只信鸽的脚上。"
            "信鸽扑扇着翅膀飞走了。"
            "她在给谁送信？王后？还是暗百合？"
            "你迅速退回通道，轻轻关上石墙。"
            "你的心在狂跳。"
            "你需要时间消化这个发现。"
            $ change_stat("intrigue", 5)

    "你在密道中待了足足四个小时。"

    "当你终于从壁炉后回到书房时，天已经完全黑了。"

    "你在地图上标注了密道的路线——它比你想象的要庞大得多。"

    "艾登堡的地下，藏着一整片密道网络。"

    "你疲惫地坐在椅子上，正要休息，突然——"

    "你意识到自己的衣服上沾满了密道里的泥土和苔藓。如果有人看到你这副模样，一定会起疑。"

    "你匆忙换了一件干净的衬衫，把脏衣服塞进柜子里。"

    "刚关上柜门——"

    "门被轻轻叩响了。"

    "你心里一紧。这个时间来敲门——"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    $ unlock_gallery("elena")

    elena "领主大人，还没休息吗？"

    $ hide_all_chars()
    "她站在门口，手里端着一杯热茶。火光映照在她的脸上，柔和而美丽。"

    if not elena_spy_known:
        "林子里那一夜还压在你心头——她受过训练，手上有血。这些她认了。"

        "可她到底替谁做事，始终没说。"

        "你看着她端茶的那只手。落杯无声，稳得不像一个普通侍从。"

        "你看着艾琳娜的脸，张了张嘴，又合上了。"

        "如果那些脚印真的是她的……如果她送出的信鸽是在向某人汇报你的行踪……"

        "她到底站在哪一边？"
    else:
        "她的身份你早已知道——王后的眼线，也是暗百合的人。但今夜，她带来的是一杯热茶，不是一封报告。"

        "你看着艾琳娜的脸，张了张嘴，又合上了。"

        "刚才看到的那只信鸽——她是在替谁传话？是王后那边的常规汇报，还是……另有隐情？"

    menu:
        "直接质问她是否知道密道的存在":
            $ change_stat("power", 5)
            $ change_rel("rel_elena", -12)
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "艾琳娜，你去过城堡下面的密道吗？"
            "她的表情没有变化——太过完美的平静。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "密道？领主大人在说什么？"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "不要装了。我发现了那些通道。"
            "远处传来钟声，连敲了三下。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "……领主大人发现了多少？"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "足够多了。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "那我们需要谈谈。但不是现在——这里不安全。"
            elena "明天，在花园里。我会告诉你一切。"
            "她答应了。但你看得出，从这一刻起，她看你的眼神里多了一层戒备——你亮了牌，她也收起了底牌。"

        "若无其事地与她交谈，暗中观察":
            $ change_stat("intrigue", 5)
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "在整理父亲的遗物。你有什么事？"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "侍卫长让我转告您，明天上午有几个村长来请愿。关于失踪的农民。"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "好的，我知道了。"
            $ hide_all_chars()
            "你仔细观察她的表情。她看起来很正常——和往常一样温和、得体。"
            "但你注意到她的靴子上有一点潮湿的泥土。"
            "密道里的泥土。"
            "你什么都没说。但你知道，艾琳娜藏着秘密。"
            "你没有逼她，所以她也没给你答案。你多看清了一分，却也仍旧落在她后面一步——她明早还会照常进来回话，像什么都没发生过。"
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve

        "问她关于暗百合的事" if not elena_spy_known:
            $ change_stat("intrigue", 8)
            $ change_rel("rel_elena", -8)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "艾琳娜，你听说过暗百合吗？"
            "她微微一怔。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "暗百合？那是一个古老的传说，不是吗？"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "传说？什么样的传说？"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "据说是先王时代的一个秘密组织。但那都是很久以前的事了。"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "如果我告诉你，这个组织现在依然存在呢？"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "……那就很值得担忧了。领主大人是在哪里听到这些的？"
            "她的反应……有些奇怪。不像是惊讶，更像是——警惕。"
            "你看见她的指尖几不可察地收紧了一瞬。你打探暗百合的事，等于告诉她你在往最深的地方挖——从今往后，她对你只会更小心。"

    elena "领主大人，不管怎样，请您注意安全。最近的事情太多了。"

    hide elena_img with dissolve

    $ hide_all_chars()
    "你目送艾琳娜离开，心中充满了疑问。"

    "她到底是谁？王后的间谍？暗百合的成员？还是两者都是？"

    "你摇了摇头，强迫自己先休息。明天还有很多事要做。"

    ## ============================================================
    ## 第五部分：暗百合总部（~600行）
    ## ============================================================

label ch3_dark_lily_hq:

    $ ch3_dark_lily_visited = True
    $ play_music("audio/music/conspiracy.ogg", fadein=2.0)
    scene black with dissolve

    "三天后。子时。"

    "你独自来到城外的废弃磨坊。"

    "破旧的磨坊在黑暗中像一具骨架。夜风灌进破窗，发出呜呜的声响。"

    "你推开吱呀作响的木门。"

    scene bg underground with dissolve
    $ unlock_gallery("bg_underground")

    "磨坊内部比外面看起来大得多。地板上有一个打开的活板门，石阶向下延伸。"

    "你走下石阶。"

    "石阶尽头是一条宽阔的走廊，两侧的墙壁上燃烧着蓝色的火焰——和你在密道资料库里看到的荧光矿石是同一种东西。"

    "走廊的尽头是一扇巨大的铁门。门上雕刻着一朵精美的倒置百合花。"

    "你还没来得及敲门，铁门就自己打开了。"

    "门后是一个巨大的地下空间——比你见过的任何大厅都要宏伟。"

    "石柱支撑着高高的穹顶。蓝色的荧光矿石镶嵌在四面八方，让整个空间笼罩在一层幽蓝的光辉中。"

    "大厅中央有一个圆形的平台，上面站着一个人。"

    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    $ unlock_gallery("lily_master")
    $ lily_master_met = True

    lily_master "欢迎来到暗百合的中枢。"

    lily_master "我等你很久了。"

    "她摘下了兜帽。一张年约四十的女性面容，眉宇间透着不怒自威的气质。"

    lily_master "我是暗百合的首领——第十七代影主。你可以叫我……影。"

    hide lily_master_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你……就是暗百合的首领？"

    hide player_char_img
    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    lily_master "是。从你父亲还在人世的那一天起，我就在等一个机会——亲自见见他的继承人。"

    hide lily_master_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我通过了？"

    hide player_char_img
    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    lily_master "你来了，这就是答案。"

    $ hide_all_chars()
    "她走下平台，来到你面前。"

    "近距离看，她比你想象的更有气场。她的眼睛是深褐色的，看不出情绪。"

    "她的左手无名指上戴着一枚银色的百合花戒指——和你在密道中找到的徽章同款。"

    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    lily_master "在我告诉你一切之前，让我先带你看看这个地方。"

    lily_master "你需要知道，你面对的是什么样的组织。"

    $ hide_all_chars()
    "她领着你在地下空间中行走。你这才意识到，这不只是一个大厅——这是一座完整的地下设施。"

    "大厅的四周有十几个门洞，通向不同的房间。"

    "影带你走进第一个房间——训练场。"

    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    lily_master "这是我们的训练区。影卫的成员必须掌握基本的格斗和潜行技术。"

    $ hide_all_chars()
    "训练场的面积不大，但设施齐全。墙上挂着各种武器——短剑、匕首、弩、绳索、飞刀。"

    "地面上画着练习用的圆圈和标记。"

    "你注意到角落里有几个稻草人，上面插满了飞刀——每一把都正中要害。"

    hide lily_master_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你们有多少人？"

    hide player_char_img
    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    lily_master "影卫在这个地区有大约八十人。整个王国范围内，大约三百人——王畿一百多，南境一百，北境几十。"

    hide lily_master_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "三百人……对抗整个王国的军队？"

    hide player_char_img
    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    lily_master "我们不需要对抗军队。我们的武器是情报、渗透和策略。三百人足以撬动一个王国。"

    $ hide_all_chars()
    "她带你走进第二个房间——情报室。"

    "这间房间的四面墙上贴满了地图和图表。一张巨大的王国地图上标注着各种颜色的图钉——"

    "红色代表敌人的据点，蓝色代表影卫的联络点，绿色代表潜在的盟友。"

    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    lily_master "这是我们的情报网络。王畿和南境的主要城市都有联络点，北境只在几个关键领地布了人。"

    lily_master "在王都，我们有十二名暗探。在教会总部，有三名。在大领主的城堡里，多数能塞进一名——南境密一些，北境疏一些。"

    hide lily_master_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "王畿、南境、北境——你说得像是三个不同的地方。"

    hide player_char_img
    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    lily_master "王国一向分三块。王畿八领是王后直辖的根基，南境十几个领地是先王老臣聚集的地盘，北境七领常年防御外族，自成一脉。"

    lily_master "王后那三千机动军是王畿直属——能不能调动外境的私兵，还得看领主们的脸色。"

    lily_master "这也是为什么——三百人足够撬动王国。我们不需要遍布每一寸土地。我们只需要在每一处关节上有一个人。"

    hide lily_master_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "这些人……他们知道自己在为谁工作吗？"

    hide player_char_img
    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    lily_master "大部分只知道自己是某个秘密组织的成员。只有核心人员才知道暗百合的全貌。"

    "她指了指地图上艾登堡的位置。上面标着一个蓝色图钉和一个黄色图钉。"

    lily_master "蓝色是我们的联络人——你在集市上见过的那个人，'根'。"

    lily_master "黄色……是一个双重身份的成员。在你身边。"

    hide lily_master_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "……艾琳娜。"

    hide player_char_img
    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    lily_master "你已经猜到了？"

    hide lily_master_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我在密道中发现了通向她房间的通路。"

    hide player_char_img
    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    lily_master "很好。你的观察力比你父亲更敏锐。不过他当年也很快就察觉了——据说不到三个月。"

    $ hide_all_chars()
    "她带你走进第三个房间——炼金实验室。"

    "空气中弥漫着草药和化学品的混合气味。工作台上摆满了瓶瓶罐罐、蒸馏器和研磨工具。"

    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    lily_master "这是我们的炼金实验室。暗百合在草药学和毒理学方面有很深的造诣。"

    hide lily_master_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "暮色之露……你们也能制造？"

    hide player_char_img
    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    lily_master "能制造，也能检测。正是在这个实验室里，我们确认了你父亲的死因。"

    "她从架子上拿下一个小玻璃瓶。瓶子里是一种暗紫色的液体。"

    lily_master "这就是暮色之露。无色无味——但在紫光下会呈现这种颜色。"

    lily_master "我们在你父亲的酒杯上提取了残留物，用紫光照射后确认了成分。"

    "她把瓶子放回架子上。"

    lily_master "我们同时研发了解毒药——但太晚了。你父亲服用暮色之露已经超过六个月，解毒已经不可能了。"

    "你的指甲深陷掌心，留下四道白痕。"

    hide lily_master_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "如果早一点发现……"

    hide player_char_img
    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    lily_master "如果、如果。这个世界上没有如果。"

    lily_master "但我们可以确保同样的事不再发生。"

    "她转过身，带你走向最后一个房间。"

    if not dark_lily_exists_known:
        lily_master "暗百合成立于两百年前，由先王格里菲斯一世的贴身近卫建立。"

        lily_master "格里菲斯一世预见到，自己死后，宫廷中的权力斗争将会撕裂这个王国。"

        lily_master "所以他秘密组建了暗百合，赋予他们一个使命——守护王国的真正秩序。"
    else:
        lily_master "暗百合的历史，你应该已经有所了解了。"

        lily_master "但你只知道表面。让我告诉你更多。"

    "她带你走进一间侧室。墙壁上挂满了画像——历代暗百合首领的画像。"

    lily_master "第一代影主是格里菲斯一世的兄弟。他放弃了一切世俗的身份，隐入暗处。"

    lily_master "从那以后，每一代影主都是如此——没有名字，没有身份，只有使命。"

    hide lily_master_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "两百年……你们一直在暗中活动？"

    hide player_char_img
    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    lily_master "是的。大多数时候，王国的统治者是合法的，暗百合只需要默默观察。"

    lily_master "但二十年前，情况变了。"

    "她的声音变得沉重。"

    if not father_was_regent_known:
        lily_master "先王——格里菲斯七世，在驾崩前留下了一份遗诏。遗诏中指定的摄政者……是你的父亲。"

        hide lily_master_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "我的父亲？！"

        hide player_char_img
        $ hide_all_chars("lily_master_img")
        show lily_master_img at left with dissolve
        lily_master "那你也知道，遗诏被篡改了。"

        hide lily_master_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "是教会大主教费雷恩干的。"
    else:
        lily_master "看来你已经知道——你父亲本是先王指定的摄政者。"

        hide lily_master_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "嗯。"

        hide player_char_img
        $ hide_all_chars("lily_master_img")
        show lily_master_img at left with dissolve
        lily_master "那你也知道，遗诏被篡改了。"

        hide lily_master_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "是教会大主教费雷恩干的。"

    hide player_char_img
    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    if not queen_poisoned_king_known:
        lily_master "不完全是。费雷恩只是执行者。真正的策划者，是伊莎贝拉。"

        lily_master "她本是一个小国的公主，嫁给格里菲斯七世后野心膨胀。她想要的不是做一个王后——她想要绝对的权力。"

        lily_master "格里菲斯七世发现了她的野心，在遗诏中刻意排除了她。"

        lily_master "但伊莎贝拉收买了费雷恩。在先王驾崩的那个夜晚，遗诏被调换了。"
    else:
        lily_master "不完全是。费雷恩只是执行者。幕后主使你应该也猜到了——伊莎贝拉。"

        lily_master "但伊莎贝拉收买了费雷恩。在先王驾崩的那个夜晚，遗诏被调换了。"

    hide lily_master_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "如果你们知道这一切，为什么不站出来揭露？"

    hide player_char_img
    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    lily_master "因为没有证据。"

    "她叹了一口气。"

    lily_master "原始遗诏被费雷恩销毁了——至少我们是这么认为的。没有原件，仅凭我们的证词，谁会相信？"

    lily_master "而且，伊莎贝拉的统治在最初并不差。经济稳定，边境安宁。站出来指控她，只会引发内战。"

    lily_master "你的父亲也是这么想的。他选择了沉默。"

    hide lily_master_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "但后来……他被杀了。"

    hide player_char_img
    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    lily_master "是的。因为他发现了一个更大的秘密。"

    "她带你走进另一间房间。这间房间里只有一面墙有内容——一张巨大的人物关系图。"

    lily_master "格里菲斯七世不是自然死亡。有人在他的酒中下了慢性毒药。"

    lily_master "你的父亲在调查这件事时，发现了毒药的来源——暮色之露。"

    lily_master "这种毒药极其罕见，只有教会的炼金术士才能制造。"

    lily_master "你父亲追踪到了一个关键人物——教会的药剂师格温。"

    lily_master "格温在你父亲接触她之后不久，就「意外死亡」了。"

    lily_master "而你的父亲……也在半年后去世了。官方说是疾病。"

    lily_master "但我们检验了他的遗物——他的酒杯上有暮色之露的残留。"

    $ poison_evidence = True
    $ father_death_known = True
    $ true_killer_known = True

    hide lily_master_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "同样的毒药……杀了先王，也杀了我父亲。"

    hide player_char_img
    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    lily_master "没错。"

    hide lily_master_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "下毒的人是谁？"

    hide player_char_img
    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    lily_master "我们只能确认，毒药来自教会。但教会是否受伊莎贝拉的指使，我们没有直接证据。"

    hide lily_master_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "毒药从教会运到艾登堡之后……是谁递到我父亲嘴边的？"

    hide player_char_img
    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    lily_master "您父亲身边的酒窖管事——汉斯。一个跟了卡尔大人二十年的老人。"

    lily_master "他在卡尔大人去世后第二天，被发现淹死在自家的井里。官方说是悲伤过度跳井自尽。"

    $ hide_all_chars()
    "你脑中翻涌起那张被时光磨得模糊的脸——汉斯。你小时候偷溜进酒窖，是他笑着把你赶出去的人。"
    "他的死，是悲伤？还是又一次灭口？"

    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    lily_master "毒药从他手里递出去——这一条线索我们查到了。"

    lily_master "至于他是被谁收买、又是谁让他闭嘴的——王后？费雷恩？还是某个我们尚不知晓的人？这正是我们没有直接证据的部分。"

    lily_master "不过……有一个人可能知道真相。"

    hide lily_master_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "谁？"

    hide player_char_img
    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    lily_master "你身边的那位——马修斯主教。"

    lily_master "他是费雷恩的学生。费雷恩在篡改遗诏后不久就死了，但他一定把一些秘密传给了马修斯。"

    lily_master "马修斯知道多少？他是同谋还是被蒙在鼓里？我们一直没能确定。"

    "你在心里反复咀嚼着这些名字和脉络。"

    hide lily_master_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你说暗百合内部有三个派系。"

    hide player_char_img
    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    lily_master "你已经知道了？"

    hide lily_master_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "在密道的资料库里看到的。影卫、铁刺、暗焰。"

    hide player_char_img
    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    lily_master "我领导的是影卫——最大的派系。我们主张通过和平手段恢复正统。"

    lily_master "铁刺是激进派，他们想要直接发动政变推翻王后。他们的首领是一个叫'棘'的人，身份不明。"

    lily_master "暗焰……是叛徒。他们已经被王后收买，成了王后的暗探。他们的任务是破坏暗百合的行动。"

    hide lily_master_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "之前暗杀我的人……"

    hide player_char_img
    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    lily_master "很可能是暗焰的人。他们想在你发现真相之前除掉你。"

    hide lily_master_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你怎么知道他们不会再来？"

    hide player_char_img
    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    lily_master "他们一定会再来。所以你需要暗百合的保护。"

    "她直视你的眼睛。"

    lily_master "现在，你有一个选择。"

    lily_master "加入影卫，和我们一起揭露真相，恢复正统。"

    lily_master "或者，走你自己的路。但我不保证你能活到看见日出。"

    hide lily_master_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "这是威胁吗？"

    hide player_char_img
    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    lily_master "这是现实。你已经知道了太多。暗焰的人不会放过你。"

    lily_master "如果你不在我们的保护下，你就是一个活靶子。"

    menu:
        "提议合作而非加入，互不臣属" if intrigue >= 60:
            $ change_rel("rel_lily", 15)
            $ change_stat("intrigue", 8)
            $ change_stat("reputation", -2)
            $ ch3_lily_alliance_independent = True
            $ dark_lily_joined = True  # 栀子反馈 2026-05-21: 合作=暗百合给情报, 后续 chapter4 联络接头人选项需要这个 flag

            hide lily_master_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "影主，加入和不加入都不是我想要的答案。"

            player "我有第三个提议。"

            hide player_char_img
            $ hide_all_chars("lily_master_img")
            show lily_master_img at left with dissolve
            lily_master "说。"

            hide lily_master_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "影卫给我情报，我给艾登堡的资源——粮道，人脉，中立城镇关系。"

            player "我不进你的系统，你也不进我的。但我们共享暗焰的信息，共享暮色之露的查证。"

            player "你那边有损失，艾登堡的财库出三分之一。我这边出事，你那边接应。"

            player "对等。不臣属。"

            $ hide_all_chars()
            "影主看着你，看了很久。比刚才任何一次都久。"

            $ hide_all_chars("lily_master_img")
            show lily_master_img at left with dissolve
            lily_master "你父亲也提过类似的话。二十年前。"

            lily_master "那时候我没答应——我当时还以为加入是唯一的选项。"

            lily_master "你比他往前走了一步。"

            hide lily_master_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "那今天答应吗？"

            hide player_char_img
            $ hide_all_chars("lily_master_img")
            show lily_master_img at left with dissolve
            lily_master "……答应。"

            lily_master "影卫从今天起跟艾登堡平起平坐。你的需求，我的人会知道。我的需求，你的人也得知道。"

            $ hide_all_chars()
            "她转身走回内殿。你也转身走出门。"

            "出门的时候，守在外面的影卫向你低头致意——一个礼节，跟你进来时不一样。"

        "加入影卫":
            $ dark_lily_joined = True
            $ lily_full_member = True
            $ change_rel("rel_lily", 30)
            ## 选择深度 pass: 秘密效忠影卫=分裂的忠诚(且无人知晓), 不该+。换来的是 rel_lily 与情报, 代价是治理底气
            $ change_stat("loyalty", -4)
            ## 影卫印记=与圣母教会决裂(本分支台词已承诺), 落地 faith 代价, 对齐同菜单加入铁刺的 faith-5
            $ change_stat("faith", -5)
            $ log_decision("第三章", "加入暗百合·影卫")
            hide lily_master_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我父亲为真相而死。我不会辜负他的牺牲。"
            hide player_char_img
            $ hide_all_chars("lily_master_img")
            show lily_master_img at left with dissolve
            lily_master "好。从今天起，你是影卫的一员。"
            lily_master "你的代号是……「继承者」。"
            lily_master "我会安排影卫中最优秀的人手保护你。同时，我会把我们掌握的所有情报交给你。"
            lily_master "但你必须记住一件事——影卫的铁律是：不到万不得已，不流无辜人的血。"
            lily_master "还有一句你该清楚——戴上影卫的印记，圣母教会的门就对你关上了。"
            lily_master "他们容得下悔过的罪人，容不下我们这样的人。日后你想借圣母的名义号令谁，没人会听。"
            hide lily_master_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "那扇门我本来也没指望。"
            $ hide_all_chars()
            "话说得轻。你心里清楚：往后真要圣母教会站到你这边，已经没这条路了。"
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我记住了。"
            hide player_char_img
            $ hide_all_chars("lily_master_img")
            show lily_master_img at left with dissolve
            lily_master "还有一件事……你身边的人中，有暗焰的内应。"
            hide lily_master_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "谁？"
            hide player_char_img
            $ hide_all_chars("lily_master_img")
            show lily_master_img at left with dissolve
            lily_master "我不确定。但要小心。不要对任何人透露你加入了影卫。"
            "你郑重地点了点头。"

        "加入铁刺" if power >= 65:
            $ dark_lily_joined = True
            $ lily_full_member = True
            $ change_rel("rel_lily", -10)
            $ change_stat("power", 20)
            $ change_stat("loyalty", -3)
            ## 选择深度 pass: 加入异端铁刺 → 不该+信仰(教会属性)。与圣光路线互斥的代价
            $ change_stat("faith", -5)
            $ log_decision("第三章", "加入暗百合·铁荆棘")
            hide lily_master_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "和平手段太慢了。我父亲等了十年，等到的是一杯毒酒。"
            player "铁刺的方式激进，可它有效。"
            hide player_char_img
            $ hide_all_chars("lily_master_img")
            show lily_master_img at left with dissolve
            lily_master "……你确定？铁刺的方法会流很多血。"
            hide lily_master_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "必要的血，我愿意承担。"
            hide player_char_img
            $ hide_all_chars("lily_master_img")
            show lily_master_img at left with dissolve
            lily_master "我无法阻止你。但我希望你能三思。"
            lily_master "铁刺的首领'棘'，每月初一会在边境的一个据点出现。你可以去找他。"
            lily_master "但请记住——一旦踏上那条路，就没有回头的余地了。"

        "不加入任何派系，保持独立":
            $ change_stat("faith", 5)
            $ change_stat("power", 5)
            $ log_decision("第三章", "保持独立，不加入暗百合")
            hide lily_master_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我不会加入任何组织。我是艾登堡的领主，不是谁的棋子。"
            hide player_char_img
            $ hide_all_chars("lily_master_img")
            show lily_master_img at left with dissolve
            lily_master "独立？在这盘棋局中，没有人能独善其身。"
            hide lily_master_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "那我就做棋盘上的那个变数。"
            hide player_char_img
            $ hide_all_chars("lily_master_img")
            show lily_master_img at left with dissolve
            lily_master "……有趣。你比你父亲更有野心。"
            lily_master "好吧。即使你不加入我们，我也不会伤害你。"
            lily_master "但如果你需要帮助——老磨坊，随时。"

        "摧毁暗百合" if power >= 60:
            $ dark_lily_destroyed = True
            $ change_stat("power", 15)
            $ change_stat("loyalty", -3)
            $ change_rel("rel_lily", -30)
            $ log_decision("第三章", "选择摧毁暗百合")
            hide lily_master_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "一个存在了两百年的秘密组织，内部分裂成三个派系，互相倾轧——"
            player "你们的存在本身就是王国不稳定的根源之一。"
            hide player_char_img
            $ hide_all_chars("lily_master_img")
            show lily_master_img at left with dissolve
            lily_master "你……什么意思？"
            hide lily_master_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "也许真正需要的不是揭露什么真相，而是让所有暗处的势力都消失。"
            hide player_char_img
            $ hide_all_chars("lily_master_img")
            show lily_master_img at left with dissolve
            lily_master "你想摧毁暗百合？"
            hide lily_master_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "如果那是必要的。"
            hide player_char_img
            $ hide_all_chars("lily_master_img")
            show lily_master_img at left with dissolve
            lily_master "你太天真了。暗百合不是你能消灭的。"
            lily_master "但我不会和你为敌——前提是你不要做出愚蠢的事。"
            "你转身离开。身后，影的目光像刀一样刺在你的背上。"

    hide lily_master_img with dissolve

    $ hide_all_chars()
    "你离开了暗百合的中枢。"

    "走出磨坊时，月亮已经偏西了。你估计已经在地下待了将近三个小时。"

    "回城堡的路上，你反复思考着影告诉你的一切。"

    "遗诏被篡改、先王被毒杀、父亲被灭口——"

    "如果这些都是真的，那你面对的敌人遍布王畿和各地。"

    "而你，已经身在网中。"

    ## ============================================================
    ## 第六部分：艾琳娜的秘密（~500行）
    ## ============================================================

label ch3_elena_secret:

    $ play_music("audio/music/castle_calm.ogg", fadein=2.0)
    scene bg castle_exterior with dissolve
    $ unlock_gallery("bg_castle_exterior")

    "第二天清晨。"

    "你在花园里找到了艾琳娜。"

    "她站在一丛盛开的百合花旁，背对着你。阳光在她的发间流转。"

    "你注意到，她在看的正是白色的百合花。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "艾琳娜。"

    "她转过身。她的表情平静如常，但你注意到她的眼睛下方有淡淡的黑眼圈——她昨晚也没睡好。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "领主大人，早安。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我们需要谈谈。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "……我知道。"

    "她环顾四周，确认没有其他人在附近。"

    elena "但不是在这里。跟我来。"

    hide elena_img with dissolve

    scene bg forest_path with dissolve
    $ unlock_gallery("bg_forest_path")

    "她带你走出花园，沿着一条林间小径，来到城堡后方的一片小树林里。"

    "这里安静、隐蔽，远离城堡中任何可能偷听的人。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve

    if dark_lily_destroyed:
        elena "领主大人，我欠你一个解释。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "你确实欠我一个解释。"

        player "我知道密道的事。我知道暗百合的事——那个组织已经被我摧毁了。"

        player "所以你到底是谁的人？"

        "你注视着她的反应。提到暗百合的时候，她的瞳孔微微收缩了一下。"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "……你摧毁了暗百合。我知道。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "你是暗百合的人。"

        "你没有抬调子。你不是在问她，是在告诉她。"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "……我曾经是。"

        "你的手不自觉地按上了剑柄。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "继续说。"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        if elena_spy_known:
            elena "王后派我来的事，你在路上已经看穿了。但还有一层，我一直瞒着你——"

            elena "我也曾是暗百合的成员。"
        else:
            elena "我是王后安排到你身边的人。但同时——我也曾是暗百合的成员。"

        elena "双重间谍。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "双重间谍。"

        player "所以当我冒着生命危险摧毁那个组织的时候，你就站在我身边，假装什么都不知道？"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "我没有假装。但有很多事我确实无法告诉你——"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "为什么？怕我连你一起清算？"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "……是的。我害怕。"

        if not elena_spy_known:
            elena "但请你听我说完。五年前，王后派我来艾登堡监视你的父亲。我是从王后的侍女学院——实际上是间谍培训营——毕业的。艾登堡是我的第四个任务。"
        else:
            elena "这些你已经知道了——王后派我来，间谍培训营出身。"

        if not elena_identity_exposed_known:
            elena "但你的父亲不到三个月就查出了我的身份。"

            elena "他没有揭穿我。他给了我一个选择——继续做王后的棋子，或者做一个有良心的人。"

            elena "我选择了后者。你父亲把我引荐给了暗百合。从那以后，我向王后报告无害的信息，同时为暗百合收集真正重要的情报。"
        else:
            elena "你父亲早就看穿了我，给了我重新选择的机会。这些你都知道。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "那你为什么不阻止我摧毁暗百合？"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "因为我也想看着它倒下。"

        "你没有料到她会这么说。"

        elena "暗百合已经不是你父亲当年加入的那个组织了。暗焰的渗透、内部的腐化——"

        elena "里面早就空了。我不会拦你。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "那你父亲的死呢？你事先知道吗？"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "不知道。"

        "她的声音发颤。"

        elena "下毒的人不是通过我的渠道。王后的间谍网不止我一个人——还有其他渠道，我至今不知道是谁。"

        elena "当我发现的时候……已经太晚了。那是我最大的遗憾。"

        $ hide_all_chars("elena_img")
        show elena_img sad at left with dissolve

        elena "你父亲对我有恩。他死后，我留下来是为了保护你。这一点从未改变。"

        elena "无论你信不信——我对你的忠诚不是暗百合给我的任务。是你父亲用善意换来的。"

        elena "如果你要因此惩罚我，我不会反抗。但请你先听完最后一件事。"

        menu:
            "你的话一个字都不能信——暗百合余孽的借口罢了":
                $ change_rel("rel_elena", -25)
                $ change_stat("power", 5)
                hide elena_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "暗百合的人最擅长的就是编故事。你怎么证明你说的不是另一套谎言？"
                hide player_char_img
                $ hide_all_chars("elena_img")
                show elena_img at left with dissolve
                elena "……我无法证明。"
                elena "但接下来的情报关系到你的生死。你可以不信任我，但请听完。"
                "她的眼神黯淡了下去，但依然保持着最后的镇定。"

            "交出你掌握的所有情报——这是你唯一的出路" if intrigue >= 45:
                $ change_rel("rel_elena", -5)
                $ change_stat("intrigue", 8)
                $ change_stat("loyalty", -3)  ## 强压 Elena 交情报的代价: 团队信任受损 (balance pass 修法 1)
                hide elena_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "暗百合已经不存在了，你的忠诚也就没有了约束。"
                player "把你知道的一切都交出来。当作你这些年欺骗我的代价。"
                hide player_char_img
                $ hide_all_chars("elena_img")
                show elena_img at left with dissolve
                elena "好。我本来也打算这么做。"
                elena "关于王后的布局、残余势力的动向——所有情报，我会全部告诉你。"
                $ change_stat("loyalty", 5)

            "看在父亲的份上——我给你一次机会" if loyalty >= 55:
                $ change_rel("rel_elena", 10)
                $ change_stat("loyalty", 10)
                hide elena_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "如果不是因为父亲信任过你，你现在已经在地牢里了。"
                player "我给你一次机会。但如果你再有任何隐瞒——"
                hide player_char_img
                $ hide_all_chars("elena_img")
                show elena_img at left with dissolve
                elena "不会了。我发誓——再不会有秘密。"
                "她的肩膀微微松了下来。那不像是伪装。"

            "暗百合已经是过去式了——我只关心你现在的立场":
                $ change_stat("loyalty", 5)
                hide elena_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "过去的事追究起来没完没了。暗百合已经不存在了。"
                player "我只问你一个问题——你现在，站在谁那边？"
                hide player_char_img
                $ hide_all_chars("elena_img")
                show elena_img at left with dissolve
                elena "站在你这边。从你父亲给我选择的那天起，就一直是。"
                elena "以前碍于暗百合的规矩不能坦白。现在没有什么能阻止我了。"
                hide elena_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "那就证明给我看。"
                hide player_char_img
                $ hide_all_chars("elena_img")
                show elena_img at left with dissolve
                elena "我这就证明。"

    elif dark_lily_joined:
        elena "领主大人，我欠你一个解释。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "从哪里开始？你知道密道的事？你是暗百合的人？还是王后的间谍？"

        "艾琳娜舔了下干裂的嘴唇。"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "都是。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "……什么？"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        if elena_spy_known:
            elena "王后派我来的，这你在路上就看穿了。但还有一层我一直没说——"

            elena "我也是暗百合的成员。"
        else:
            elena "我是王后安排到你身边的人。但同时……我也是暗百合的成员。"

        elena "双重间谍。"

        "你盯着她，心中翻涌着各种情绪——愤怒、震惊、困惑。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "从什么时候开始的？"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "从你父亲还在世的时候。"

        if not elena_spy_known:
            elena "五年前，王后派我来艾登堡，表面上是辅佐老领主处理政务，实际上是监视他。"

            elena "王后怀疑你的父亲在暗中调查遗诏的事，她需要有人汇报他的一举一动。"

            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "所以你是帮凶。"

            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "不！"

            "她的声音猛然提高，然后又降了下来。"

            elena "……我不是。听我说完。"

            elena "我确实是王后派来的。但到了艾登堡之后，你的父亲……他发现了我的身份。"

            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "他发现了？"

            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
        else:
            elena "王后派我来监视你父亲——这些你已经知道了。"

        if not elena_identity_exposed_known:
            elena "你父亲远比王后想象的聪明。他用了不到三个月就查出了我的真实身份。"

            elena "但他没有揭穿我。他找我谈话，给我看了一些东西——先王的遗诏抄本、暮色之露的证据、教会的秘密。"

            elena "他说：「你可以选择——继续做王后的棋子，或者做一个有良心的人。」"

            "她的声音微微颤抖。"

            elena "我选择了后者。"

            "她停顿了一下，似乎在回忆那个改变一切的夜晚。"

            elena "你可能想知道我为什么会做出那个选择。"

            elena "我出生在王都的一个没落贵族家庭。父亲早逝，母亲改嫁。我被送进了王后的侍女学院。"

            elena "侍女学院……听起来很优雅，但实际上是王后培养间谍和密探的地方。"

            elena "我们从十二岁开始接受训练——情报收集、密码通信、伪装渗透、甚至……暗杀技术。"

            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "暗杀？"

            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "是的。但我从来没有执行过暗杀任务。我的专长是渗透和情报。"

            elena "毕业后，我被派往各个领地。艾登堡是我的第四个任务。"

            elena "在前三个任务中，我从来没有质疑过自己。王后说谁有问题，我就去监视谁。"

            elena "但你的父亲不一样。"

            elena "他是我遇到过的第一个真正……善良的人。"

            elena "他不仅没有因为我是间谍而恨我，反而关心我的处境。他说：「一个十二岁就被训练成工具的孩子，不应该为别人的野心负责。」"

            "她的声音发颤。你看到她的眼角闪着泪光。"

            $ hide_all_chars("elena_img")
            show elena_img sad at left with dissolve

            elena "那是我第一次觉得，自己不是一个工具，而是一个人。"

            elena "你父亲把我介绍给了暗百合。从那以后，我就成了双重间谍——向王后报告无关紧要的信息，同时为暗百合收集真正重要的情报。"

            elena "每个月我会给王后写一份报告——内容都是经过暗百合审核的，只包含一些无害的信息。比如「老领主今天接见了商人」或者「领地的税收正常」之类的。"

            elena "王后从来没有怀疑过。她以为我是她最忠诚的耳目。"
        else:
            elena "你父亲识破了我的身份，给了我重新选择的机会——这些你都清楚。"

            $ hide_all_chars("elena_img")
            show elena_img sad at left with dissolve

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "那你给暗百合的情报呢？"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "那些才是真正重要的——王后的计划、教会的动向、宫廷中的阴谋。我利用王后对我的信任，获取了大量内部情报。"

        elena "这些情报帮助暗百合在很多关键时刻做出了正确的判断。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "我父亲死的时候呢？你为什么没能保护他？"

        "艾琳娜低下了头。你看到一滴泪滑过她的脸颊。"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "那是我最大的遗憾。"

        elena "你父亲的死……我事先不知道。下毒的人不是通过我这个渠道。"

        elena "王后对你父亲的监视不止我一个人。还有其他渠道，我不知道是谁。"

        elena "当我发现的时候……已经太晚了。"

        "她的眼眶微微泛红。"

        elena "你父亲对我有恩。他没有杀我，没有揭穿我，反而给了我一个重新选择的机会。"

        elena "他死后，暗百合的首领——影，让我留在艾登堡，继续保护他的继承人。"

        elena "也就是你。"

        menu:
            "我无法信任你——双重间谍的话不可信":
                $ change_rel("rel_elena", -20)
                $ change_stat("power", 5)
                hide elena_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "你的每一句话都可能是谎言。一个双重间谍，我怎么知道你到底为谁效力？"
                hide player_char_img
                $ hide_all_chars("elena_img")
                show elena_img at left with dissolve
                elena "……我理解你的怀疑。我不会要求你立刻信任我。"
                elena "但请你看看我的行动——我保护过你多少次？暗杀事件那晚，是我先发现了刺客的踪迹，及时叫来了雷恩。"
                hide elena_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "也许那只是为了维持你的掩护。"
                hide player_char_img
                $ hide_all_chars("elena_img")
                show elena_img at left with dissolve
                elena "那我无话可说。只能用时间来证明。"
                $ hide_all_chars()
                "她转身，慢慢走回城堡。"
                "你没有追上去。只是把门边她刚才靠过的那把椅子慢慢推回了原位。"

            "证明你的忠诚——告诉我王后在策划什么" if intrigue >= 45:
                $ change_rel("rel_elena", 5)
                $ change_stat("intrigue", 8)
                $ change_stat("reputation", -2)
                hide elena_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "如果你真的站在我这边，就告诉我一些有价值的东西。"
                hide player_char_img
                $ hide_all_chars("elena_img")
                show elena_img at left with dissolve
                elena "王后最近在集结力量。她对边境领主的忠诚度越来越不放心。"
                elena "她计划在下个月召集所有领主入都觐见。名义上是朝贡，实际上是筛选——"
                elena "对她不够忠诚的领主，会被找各种借口剥夺领地。"
                hide elena_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "包括我？"
                hide player_char_img
                $ hide_all_chars("elena_img")
                show elena_img at left with dissolve
                elena "尤其是你。你父亲的事她以为处理干净了，但你最近的行为引起了她的注意。"
                elena "那个新来的侍从——你注意到的那个——就是王后新派来的眼线。"
                hide elena_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "果然……"
                hide player_char_img
                $ hide_all_chars("elena_img")
                show elena_img at left with dissolve
                if knows_eagle_network:
                    elena "不过有个底细你该知道——他不是王后自己养的人，是买来的。干这行的散在各城，谁出价就替谁看。"
                    elena "老话管这路人叫幽卫散部——先王七近卫散了之后剩下的一支。"
                    elena "他不效忠她，只效忠价钱。这种人——也能被更高的价钱买走。"
                elena "我可以帮你应付他。但你需要更加小心。"
                $ change_stat("loyalty", 5)

            "我相信你——父亲信任你，我也选择信任" if loyalty >= 55:
                $ change_rel("rel_elena", 25)
                $ change_stat("loyalty", 10)
                hide elena_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "父亲的判断力一向很准。他信任你，我也愿意给你一次机会。"
                hide player_char_img
                $ hide_all_chars("elena_img")
                show elena_img at left with dissolve
                elena "领主大人……"
                hide elena_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "但如果我发现你在对我撒谎——"
                hide player_char_img
                $ hide_all_chars("elena_img")
                show elena_img at left with dissolve
                elena "你不会的。我发誓。"
                "她的眼神中有一种你从未见过的坚定。"
                elena "从现在起，我会对你完全坦白。关于王后的计划、暗百合的动向——所有我知道的，都告诉你。"
                hide elena_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "好。那就从现在开始。"

            "你的双重身份太危险了——选一边站":
                $ change_stat("loyalty", 5)
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "你不能一直脚踩两条船。迟早有一天会被两边同时发现。"
                hide player_char_img
                $ hide_all_chars("elena_img")
                show elena_img at left with dissolve
                elena "……你说得对。"
                hide elena_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "选一边。现在。"
                hide player_char_img
                $ hide_all_chars("elena_img")
                show elena_img at left with dissolve
                elena "我已经选了。从你父亲给我机会的那天起，我就选了这边。"
                elena "但我需要继续维持王后那边的掩护。只有这样，我才能为你提供情报。"
                hide elena_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "那你必须非常小心。"
                hide player_char_img
                $ hide_all_chars("elena_img")
                show elena_img at left with dissolve
                elena "我一直很小心。"


    else:
        elena "领主大人，我欠你一个解释。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "确实。有些事我一直想问你。"

        player "你和暗百合是什么关系？你又为谁工作？"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "……你察觉到了。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "你的行为有太多不合常理的地方。一个普通的管家不可能知道那么多秘密。"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "你说得对。我不是普通的管家。"

        if elena_spy_known:
            elena "王后派我来的事，你早就看穿了。但还有一层——"

            elena "我也是暗百合的成员。"
        else:
            elena "我是王后安排到你身边的人。但同时——我也是暗百合的成员。"

        elena "双重间谍。"

        "双重间谍。这个词在你脑中反复回响。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "……继续说。"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        if not elena_spy_known:
            elena "五年前，王后派我来艾登堡，监视你的父亲。我出身于没落贵族，十二岁被送进王后的侍女学院——实际上是间谍培训营。"

            elena "毕业后被派往各地。艾登堡是我的第四个任务。"
        else:
            elena "王后派我来监视你父亲——间谍培训营出身，这些你都知道了。"

        if not elena_identity_exposed_known:
            elena "但你的父亲用不到三个月就查出了我的真实身份。"

            elena "他没有揭穿我。他找我谈话，给我看了遗诏的抄本、暮色之露的证据。"

            elena "他说：「你可以选择——继续做王后的棋子，或者做一个有良心的人。」"

            elena "我选择了后者。"

            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "他把你介绍给了暗百合。"

            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "是的。从那以后，我向王后报告无害的信息——「老领主今天接见了商人」之类的。"

            elena "真正重要的情报——王后的计划、教会的动向——我传给暗百合。"
        else:
            elena "你父亲早就看穿了我，给了我选择的机会。这些你都知道了。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "你为什么现在告诉我这些？"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "因为局势已经到了不能再隐瞒的地步。"

        elena "而且……你有权知道真相。关于你父亲的死，关于王后——你需要完整的信息。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "我父亲的死——你事先知道吗？"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "不知道。那是我最大的遗憾。"

        elena "下毒的人不是通过我这个渠道。王后的间谍网不止我一个人。"

        elena "当我发现的时候……已经太晚了。"

        "她的声音微微颤抖。"

        $ hide_all_chars("elena_img")
        show elena_img sad at left with dissolve

        elena "你父亲对我有恩。他死后，暗百合让我留下来保护你。"

        elena "不管你怎么看待暗百合——保护你这件事，是我自己的选择。"

        menu:
            "双重间谍——你到底忠于谁？":
                $ change_rel("rel_elena", -10)
                $ change_stat("power", 5)
                hide elena_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "一个人不可能同时效忠两个主人。你到底站在哪边？"
                hide player_char_img
                $ hide_all_chars("elena_img")
                show elena_img at left with dissolve
                elena "我站在你父亲选择的那一边——真相的一边。"
                elena "王后那边只是掩护。暗百合是手段。但我真正效忠的，是你父亲的遗志。"
                "你注视着她的表情，试图判断她的话有几分可信。"

            "这些情报有多可靠？证明你的价值" if intrigue >= 45:
                $ change_rel("rel_elena", 5)
                $ change_stat("intrigue", 8)
                $ change_stat("reputation", -2)  ## backlog7: 补漏 — 对齐镜像分支 3555 的盘问代价
                hide elena_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "坦白是一回事，有没有真本事是另一回事。"
                player "告诉我一些能证明你价值的情报。"
                hide player_char_img
                $ hide_all_chars("elena_img")
                show elena_img at left with dissolve
                elena "王后正在集结力量。她计划召集所有领主入都觐见，筛选不够忠诚的人。"
                elena "还有——那个新来的侍从，就是王后新派来的眼线。我可以帮你应付他。"
                if knows_eagle_network:
                    elena "顺带说一句，他不是王后自己养的人，是买来的——幽卫散部那一行的，谁出价替谁看。"
                    elena "他不效忠她，只效忠价钱。记住这一点，说不定有用。"
                $ change_stat("loyalty", 5)

            "父亲信任你的判断——我尊重他的选择" if loyalty >= 55:
                $ change_rel("rel_elena", 20)
                $ change_stat("loyalty", 10)
                hide elena_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "父亲很少看走眼。如果他选择信任你，一定有他的道理。"
                hide player_char_img
                $ hide_all_chars("elena_img")
                show elena_img at left with dissolve
                elena "领主大人……"
                elena "我不会辜负这份信任。从现在起，我会对你完全坦白。"
                "她的眼神中多了一份你从未见过的真诚。"

            "你的身份我知道了——暂时保持现状":
                $ change_stat("loyalty", 5)
                $ change_stat("intrigue", 3)
                hide elena_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "你作为双重间谍的身份，暂时对我来说是有用的。"
                player "继续向王后报告无害信息，真正的情报交给我。"
                hide player_char_img
                $ hide_all_chars("elena_img")
                show elena_img at left with dissolve
                elena "明白。我会像以前一样维持掩护。"
                elena "但这次，所有情报只对你一个人负责。"
                hide elena_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "好。我们的合作关系从现在开始。"
                hide player_char_img
                $ hide_all_chars("elena_img")
                show elena_img at left with dissolve
                elena "是。"

    $ hide_all_chars()
    "无论你说了什么，有一件事你必须承认——"

    "艾琳娜的坦白，让你对整个局势有了更清晰的认识。"

    ## 坦白事件闭合: 设 flag 防 npc_sidelines.rpy 森林夜话 / interludes.rpy 后续场景再走"初次坦白"分支
    ## (Måneskin 2026-05-18 反馈: 高好感互通秘密后又被要求把秘密说一遍)
    $ elena_spy_known = True
    $ elena_identity_exposed_known = True

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "还有一件事我必须告诉你。这可能是最重要的。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "还有什么？"

    "艾琳娜犹豫了一下，似乎在权衡该不该说。然后她下定了决心。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "暗百合内部的暗焰派系……他们的首领——代号'烬'——"

    elena "是冯·哈根男爵。"

    $ baron_is_darkflame_known = True

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "什么？！"

    $ hide_all_chars()
    "你的大脑飞速运转。男爵——你的邻居、你的对手——竟然是暗焰的首领？"

    "你回想起男爵最近送来的那封信——「共同调查失踪案」。那不是善意，那是试探。"

    "你回想起父亲的日记——「冯·哈根男爵来访。他的眼神像一条蛇在观察猎物。」"

    "一切都串联起来了。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "冯·哈根男爵表面上是你的对手，但他的势力远不止你看到的那些。"

    elena "他不仅是一个领主——最初，他是王后在边境地区的代理人。"

    elena "暗焰就是他替王后建的情报网。监控各领主、渗透暗百合、压制异见者——全是他的手笔。"

    elena "但后来王后做了一件让他永远无法原谅的事。从那以后，暗焰就不再听王后的了。"

    elena "男爵没有解散这张网——他把它反过来对准了王后。从掌握情报的人，变成了必须行动的人。暗焰是手段，反叛才是目的。"

    elena "之前的暗杀、领地内的骚乱、农民的失踪——都是他在为最终的清算蓄力。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "暗杀我的人……是男爵派的？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "是暗焰的人。男爵提供资金和情报，暗焰提供人手和执行。"

    elena "暗杀失败后，男爵很恼火。他没想到你能活下来。"

    elena "所以他改变了策略——从直接暗杀变成了渗透和瓦解。"

    elena "那个新来的侍从就是他安排的。他的任务是监视你的一切行动，特别是你是否在调查你父亲的死因。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "那封要求「共同调查」的信呢？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "那是另一层试探。如果你接受邀请，说明你还不知道他的真实身份。如果你拒绝——他就会更加警惕。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "还有呢？男爵的势力到底有多大？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "他在南部边境有大约五百名私兵。其中一部分是招募的雇佣兵，一部分是……"

    elena "你领地上失踪的那些农民。"

    $ change_stat("power", 5)

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "那些失踪的农民……"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "被暗焰的人带走了。他们在森林里建了一个秘密营地，训练私兵。"

    elena "男爵在暗中准备一支对抗王后的军队。一旦你被召入都城，这支军队就会占领艾登堡。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "他们动作真快。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "所以你必须先下手为强。"

    hide elena_img with dissolve

    "你回到城堡，脑中不停地转着。"

    if not baron_is_darkflame_known:
        "艾琳娜的信息太多了——男爵是暗焰首领、王后准备清洗领主、农民被抓去训练私兵——"
    else:
        $ hide_all_chars()
        "艾琳娜的信息太多了——王后准备清洗领主、农民被抓去训练私兵——"

    "每一条都是炸弹。"

    "你需要冷静下来，把所有的线索串联起来。"

    ## ============================================================
    ## 第七部分：真相浮现（~500行）
    ## ============================================================

label ch3_truth_emerges:

    $ play_music("audio/music/revelation.ogg", fadein=2.0)
    scene bg study with dissolve
    $ unlock_gallery("bg_study")

    $ trigger_random_event("rest")

    "你把自己关在书房里整整一天。"

    "门外传来侍从的脚步声、花园里的鸟鸣声——但你什么都听不见。"

    "你的全部注意力都集中在桌面上。"

    "所有的证据和线索都摊开在桌上——"

    "父亲的密码日记——记录了十五年的调查。"
    if secret_passage_found:
        "密道中发现的卷轴——暗百合两百年的历史。"
    if not testament_forged_known or not queen_poisoned_king_known:
        "暗百合首领的证词——遗诏被篡改，先王被毒杀。"
    else:
        "暗百合首领的证词——与日记中的发现相互印证。"
    if baron_is_darkflame_known:
        "艾琳娜的情报——男爵是暗焰首领，王后在布局。"
    else:
        "艾琳娜的情报——关于男爵与王后之间的隐秘联系。"
    if poison_evidence:
        "暮色之露的残留物——毒药的直接证据。"

    "你在一张大羊皮纸上画了一幅关系图。"

    "中心是先王格里菲斯七世。"

    "从他出发，线索延伸到——"

    if not testament_forged_known or not ferein_role_known or not queen_poisoned_king_known:
        "王后伊莎贝拉——动机：夺权。手段：收买费雷恩篡改遗诏。可能用暮色之露毒杀先王。"
    else:
        "王后伊莎贝拉——你已经掌握了她的动机和手段。"

    if not ferein_role_known:
        "教会大主教费雷恩——执行篡改遗诏。制造了暮色之露。事后被灭口（伪装成疾病死亡）。"
    else:
        "教会大主教费雷恩——已知的关键执行者，死因可疑。"

    if bishop_confession_done or matthias_has_testament_known or testament_original_obtained:
        "主教马修斯——费雷恩的学生、当年调包之夜的亲历者。违命保留了原件二十年。"
    else:
        "主教马修斯——费雷恩的学生。知情程度未知。可能保存了费雷恩留下的东西。"

    if secret_passage_found:
        "你的父亲——发现真相，成为威胁。被暮色之露长期毒杀。死前留下密码日记和密道线索。"
    else:
        "你的父亲——发现真相，成为威胁。被暮色之露长期毒杀。死前留下密码日记。"

    if not dark_lily_exists_known:
        "暗百合——先王七近卫之一创立的秘密组织。分裂为三派：影卫（正统）、铁刺（激进）、暗焰（叛徒）。"
    else:
        "暗百合——你已了解这个组织的历史和内部分裂。"

    if not baron_is_darkflame_known:
        "冯·哈根男爵——暗焰首领'烬'。王后的走狗。招募私兵，绑架农民。"
    else:
        "冯·哈根男爵——暗焰首领，你已知道他的真面目。"

    if not ferein_role_known:
        "你用红线连接了关键节点——从王后到费雷恩，从费雷恩到暮色之露，从暮色之露到父亲的死。"
    else:
        "你用红线连接了所有已知的关键节点——一条完整的罪恶链条。"

    "然后你又画了一条蓝线——从父亲到暗百合，从暗百合到你。"

    "你退后一步，审视整张图。"

    "两个圆圈——红色和蓝色——在你这里交汇。"

    "你就是所有线索的汇聚点。"

    "你盯着这张图看了很久。"

    if testament_original_obtained:
        ## 玩家已从主教处拿到遗诏原本——不再需要"物证缺失"的推理
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "直接证据已经在我手里——先王的原始遗诏。"

        $ hide_all_chars()
        "你看向书桌角落那个蜡封的皮卷筒。那就是二十年前费雷恩让马修斯销毁的原件——他违命保留至今，如今到了你手里。"

        "你的证据链已经完整：动机、手段、受害者、证人、物证——"

        "剩下的问题只有一个：怎么用它。"

        "影的话在你耳边回响：「有了原始遗诏，真相才有了无法辩驳的锋芒。」"

        $ matthias_has_testament_known = True
    else:
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "还缺一个关键——直接证据。"

        $ hide_all_chars()
        "你的证据链已经很完整了：动机、手段、受害者、证人——"

        "但有一样东西缺失了——物证。"

        "口供可以翻，日记可以被说成伪造，甚至暮色之露的残留也可以被质疑为误检——"

        "唯一无法辩驳的物证，就是先王的原始遗诏。"

        "影的话在你耳边回响：「没有原始遗诏，仅凭证词，谁会相信？」"

        "但费雷恩真的销毁了原始遗诏吗？"

        if not ferein_role_known:
            "你回想父亲的日记——『费雷恩在篡改遗诏后不久就死了。』"

            "一个人在做了这么大的事之后突然死去——这本身就很可疑。"

            "你在图上标注了一个问号：「费雷恩之死——自然死亡？还是被灭口？」"

            "如果是被灭口——那是谁干的？王后？"

            "一个可怕的推理在你脑中成形：王后利用费雷恩篡改遗诏后，为了灭口，杀了费雷恩。"
        else:
            "费雷恩的角色你已经很清楚了——篡改遗诏的执行者，随后离奇死亡。"

            "你在图上标注了一个问号：「费雷恩之死——被灭口的可能性极大。」"

        "但费雷恩不是傻子。他一定知道自己的危险。"

        if not ferein_role_known:
            "如果费雷恩没有销毁原件，而是藏了起来呢？"
        else:
            "你已经知道费雷恩篡改了遗诏——但他真的销毁了原件吗？"

        "作为一个精明的教会高层，他一定会给自己留一条后路——「如果我死了，原件就会公之于众」之类的安排。"

        "但他死得太突然了。也许他来不及启动后手。"

        "如果他留了一手——作为保护自己的筹码——但在他被灭口之前，没来得及告诉任何人呢？"

        "除了……他最亲近的学生——马修斯。"

        "你拿起鹅毛笔，在马修斯的名字旁边画了一个大大的圆圈。"

        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "马修斯……你到底知道多少？"

        $ matthias_has_testament_known = True

    if testament_original_obtained:
        ## 玩家已从主教处拿到原件——不再需要"去找主教取证"的 menu
        ## 跳过推理段，直接进入证据整理阶段
        $ hide_all_chars()
        if testament_from_bishop_hand:
            "你回忆与马修斯的最后一次见面——他把蜡封的皮卷筒双手递过来时指节发白的样子。"

            "他已经把自己最后的筹码交出来了。现在是如何使用它的问题。"
        else:
            "你回忆与马修斯的最后一次见面——他把那把古铜色小匙塞到你手里时指节发白的样子。"

            "教堂地下室假墙后那个铁箱里安静地躺着先王的羊皮卷，二十年没人动过。马修斯把钥匙交给你的那一刻，已经把自己最后的筹码托付出去了。"

            "现在是如何使用它的问题。"

        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "接下来，要把所有证据整理成一份无懈可击的东西。"

        $ hide_all_chars()
        "你吹灭了书桌上多余的烛台，只留最近的一盏。羊皮纸上的线索图在烛光里投下深浅不一的阴影。"

        "每一份副本都要经得起质疑——因为下一次翻开它，就是在王都的大殿上。"

        jump ch3_prepare_evidence

    $ hide_all_chars()
    "你回忆与马修斯的每一次见面。他总是温和有礼，但有时候你能在他的眼中看到一丝……恐惧。"

    "不是对你的恐惧。是对某种更大的东西的恐惧。"

    if not matthias_has_testament_known:
        "也许他一直带着费雷恩的秘密，活在恐惧中——害怕被王后发现，害怕被牵连。"
    else:
        "你越来越确信——马修斯手中握着关键的东西。"

    "如果是这样，那接近他需要技巧。不能吓到他，否则他可能会销毁一切。"

    "也不能太温和，否则他可能会继续装聋作哑。"

    "你需要找到一个恰当的方式——让他觉得，把秘密交出来，比继续隐藏更安全。"

    menu:
        "立刻去找马修斯主教":
            $ change_stat("power", 5)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "答案可能就在马修斯手上。"
            "你起身，大步走出书房。"
            jump ch3_confront_bishop_early

        "先做好充分准备再去找他" if intrigue >= 45:
            $ change_stat("intrigue", 8)
            $ ch3_prepared_first = True
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "不能贸然行动。我需要更多筹码。"
            "你决定先把手头的证据整理好，然后再去找马修斯。"
            jump ch3_prepare_evidence

        "派人暗中调查马修斯的行踪":
            $ change_stat("intrigue", 5)
            $ change_stat("power", 5)
            $ change_stat("loyalty", -2)  ## balance pass 修法 1: 暗中监视盟友 (马修斯是叔父辈), 内部诚信受损
            $ ch3_prepared_first = True
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "先不打草惊蛇。让我看看马修斯最近在做什么。"
            "你叫来一个信任的侍卫，让他暗中跟踪主教的行踪。"
            jump ch3_prepare_evidence

    ## --- 提前找主教 ---
label ch3_confront_bishop_early:

    $ set_mood("tense")
    scene bg church_interior with dissolve
    $ unlock_gallery("bg_church_interior")
    $ play_music("audio/music/church_choir.ogg", fadein=2.0)

    if ch3_prepared_first:
        "你已经做好了充分的准备——证据整理妥当，思路清晰。带着周密的计划，你推开了教堂的大门。"

    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    $ unlock_gallery("bishop")

    bishop "领主大人，今天怎么有空来教堂？"

    hide bishop_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "马修斯，我直说了。费雷恩大主教——你的老师——他留下了什么东西给你吗？"

    "主教的脸色变了。"

    hide player_char_img
    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "你……你在说什么？"

    hide bishop_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    if not matthias_has_testament_known:
        player "先王的遗诏。原件。费雷恩篡改了遗诏，但他不可能真的销毁原件。太有价值了。"
    else:
        player "先王的遗诏原件。我知道费雷恩没有销毁它——而你是他最亲近的学生。"

    "主教沉默了很长时间。你可以看到他额头上冒出了细密的汗珠。"

    hide player_char_img
    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "领主大人，你不知道你在触碰什么。"

    hide bishop_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我知道。我还知道，我的父亲因为这件事被杀了。用的是暮色之露——教会的炼金术士才能制造的毒药。"

    "主教的手开始颤抖。"

    $ hide_all_chars("bishop_img")
    show bishop_img sad at left with dissolve

    bishop "我……我不知道你在说什么。"

    hide bishop_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你知道。你的眼神出卖了你。"

    menu:
        "威逼——'如果你不合作，我会公开教会的丑闻'" if power >= 55:
            $ change_stat("power", 10)
            $ change_rel("rel_bishop", -20)
            $ change_stat("faith", -10)
            $ log_decision("第三章", "以武力威胁主教")
            player "马修斯，我可以选择把所有事情公之于众。教会篡改先王遗诏、制造毒药害人——"
            player "你觉得信徒们会怎么看？"
            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "你……你不能……"
            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我可以。除非你告诉我真相。"
            "主教瘫坐在椅子上。"
            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "……费雷恩临死前……确实给了我一样东西。"
            bishop "但他让我发誓，永远不要打开。"
            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "那是什么？"
            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "一个密封的盒子。我一直锁在教堂的密室里。"
            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "带我去。"
            "主教犹豫了一下，最终站起身来，领着你走向教堂的深处。"
            $ change_stat("intrigue", 8)

        "利诱——'帮助我，我可以保护教会'":
            $ change_rel("rel_bishop", 10)
            $ change_stat("wealth", 5)
            $ change_stat("faith", 12)
            $ log_decision("第三章", "以利益收买主教")
            player "马修斯，我不是你的敌人。你的老师可能犯了错误，但那不是你的错。"
            player "帮助我找到真相，我会确保教会不受牵连。"
            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "……你能做到吗？"
            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我是领主。我的领地内，教会的安全由我保障。"
            "主教长叹一声。"
            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "费雷恩确实留了一个盒子给我。他说那是「最后的保险」。"
            bishop "我一直不敢打开它。但如果你保证教会的安全……"
            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我保证。"
            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "跟我来。"

        "起誓——以艾登家纹章起誓教会一切受我保护" if faith >= 50:
            $ change_stat("faith", 3)
            $ log_decision("第三章", "以誓言换取主教信任")

            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "……起誓？ 这种时候， 谁还信誓言？"

            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "马修斯，我以艾登的金鹰起誓——"

            player "今天从您口里出来的话，出此门即烂在我肚里。您给我的物件，我用即焚，不留指向教会的痕迹。"

            player "信不信我，看您。"

            player "但我父亲就是相信誓言的人。他到死都没违背过任何一句。"

            $ hide_all_chars()
            "主教看着你的眼睛，看了很久。他在判断： 这个年轻领主的「誓言」，是真的，还是只是政治姿态。"

            $ trigger_crisis("faith", 5,
                "马修斯需要在你脸上读出来——你是来骗他的，还是真能扛起这句誓言。",
                "ch3_bishop_oath_win", "ch3_bishop_oath_lose",
                courage_cost=20, allow_skip=False)
            call crisis_encounter from _call_crisis_ch3_oath
            jump ch3_bishop_oath_lose

        "感情牌——'我只想知道父亲为什么死'":
            $ change_rel("rel_bishop", 5)
            $ change_stat("faith", 5)
            $ log_decision("第三章", "以情理说服主教")
            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "马修斯，我不关心政治。我只想知道，我的父亲是怎么死的。"
            player "他是一个好人。他不该那样死去。"
            "主教闭上了眼睛。你看到他的眼角有泪光。"
            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "老领主……是一个好人。我也这么认为。"
            bishop "费雷恩的事……我知道一些。但我一直害怕面对。"
            bishop "好吧。跟我来。有些东西我保存了很多年，一直不敢看。"

    hide bishop_img with dissolve

label ch3_bishop_take_to_vault:
    $ hide_all_chars()
    "主教带你穿过教堂的长廊。长廊两侧的彩色玻璃窗投下斑驳的光影。"

    "你注意到走廊上挂着历代主教的画像。费雷恩的画像在最里面——一个面容严肃的老人，目光锐利如鹰。"

    "你在画像前停了一步。这就是篡改遗诏的人——教会的最高权力者。"

    "他的脸上看不出罪恶的痕迹。也许犯下大罪的人，往往比谁都显得正直。"

    "马修斯注意到你在看画像。"

    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve

    bishop "费雷恩大人……是一个复杂的人。他虔诚、博学、严格——但也有软弱的时候。"

    bishop "王后的压力……不是所有人都能抵挡的。"

    hide bishop_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你在为他辩解？"

    hide player_char_img
    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "不。我在试图理解他。就像我试图理解自己为什么沉默了二十年一样。"

    $ hide_all_chars()
    "你没有回答。你们继续走。"

    "马修斯从腰间取出一串钥匙，打开了走廊尽头的一扇厚重的橡木门。"

    "门后是一段向下的楼梯。楼梯很窄，只能一个人通过。墙壁上的火把在气流中摇曳。"

    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "教堂的地下密室。只有历任主教才知道入口。"

    $ hide_all_chars()
    "你们走下楼梯。空气变得阴冷，弥漫着古老的熏香味道——和一丝令人不安的霉味。"

    "密室比你想象的要大。大约有三间普通房间那么宽。"

    "四面墙壁上绘满了宗教壁画——天使与恶魔的战争、圣人的殉道、王国建立时的祝福仪式。"

    "壁画的颜色已经褪去了大半，但仍然能看出当年的精美。"

    "密室的角落里堆放着各种木箱和铁匣——教会数百年来积累的秘密文件和圣物。"

    "密室最深处是一面看似普通的石墙。马修斯走过去，从右向左数到第三块石头，用力按了下去。"

    "机括的低鸣传来——石墙缓缓让开，露出一个隐藏的壁龛。"

    "壁龛中静静放着一个铁箱，箱身刻着教会的十字徽记，锁孔蒙着一层薄灰——显然多年未被打开。"

    hide bishop_img with dissolve

    scene bg underground with dissolve
    $ unlock_gallery("bg_underground")

    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve

    bishop "这就是费雷恩留给我的。"

    bishop "二十年了。它一直在这里。我每个月都会来看一眼，确认它还在。但我从来没有打开过。"

    bishop "费雷恩临终时说：「保管好它。如果有一天你需要用到它——那说明我所做的一切都失败了。」"

    $ hide_all_chars()
    "马修斯从法袍内袋取出一把古铜色的小钥匙，插入铁箱的锁孔——只听“咔哒”一声，锁簧应声而开。"

    "你的手微微发抖。二十年的秘密，就在这个铁箱里。"

    "你深吸一口气，掀开箱盖。"

    "箱内衬着红色的天鹅绒。里面有三样东西。"

    "第一样——一份羊皮纸，泛黄、古旧，但保存完好。蜡封上印着皇家徽章。"

    "第二样——一枚金色的印章，上面是先王的个人纹章——一头展翅的鹰。"

    "第三样——一封信。信封上写着：「致我的学生马修斯——仅在极端情况下拆阅。」"

    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "那封信……我从来没敢拆。"

    hide bishop_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我来。"

    $ hide_all_chars()
    "你先拆开了信。费雷恩的笔迹苍劲有力——"

    "『马修斯，如果你在读这封信，说明我已经不在了。』"

    "『这个匣子里有两样东西你必须守护：先王的原始遗诏和他的私人印章。』"

    "『没有这枚印章，任何人都无法证明遗诏是伪造的——因为印章只有一枚，而官方使用的那份伪遗诏上的印章是仿制的。对比两枚印章的细节，就能证明哪份是真、哪份是假。』"

    "『我一生做了很多错事。这是我唯一能做的弥补。愿上天宽恕我。——你的老师，费雷恩。』"

    "你放下信，拿起那份羊皮纸。"

    "小心地解开蜡封——二十年的蜡已经变得很脆，你花了好一会儿才完整地打开。"

    "你展开羊皮纸。"

    "顶端是皇家徽章——用金粉绘制的鹰，与印章上的纹章完全一致。"

    "正文是先王的亲笔。字迹有些颤抖——这是一个垂死之人写下的最后意志。"

    "遗诏的内容让你心潮澎湃——"

    "『朕，格里菲斯七世，于神圣王冠之下，立此最终遗诏。'"

    "『朕之子弗雷德里克年幼，尚不能独理国政。朕将摄政之权，授予艾登堡领主，朕之忠臣，辅政至王子成年。'"

    "『王后伊莎贝拉心怀叵测，不得干政，不得接触国玺，不得以任何名义行使王权。'"

    "『此为朕之最终遗愿，违者以叛逆论。'"

    "『——格里菲斯七世亲笔。赐印于王历二百七十三年秋。』"

    "遗诏的底部盖着先王的私人印章——与匣子里的金色印章纹样完全吻合。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "这就是原始遗诏……"

    $ hide_all_chars()
    "你的声音在颤抖。"

    "你手中拿着的不只是一张纸——这是一把能够推翻整个王国权力结构的钥匙。"

    if not father_was_regent_known:
        "二十年前，你的父亲本应该成为摄政者——辅佐年幼的王子治理国家。"

        "如果遗诏没有被篡改，王后不会有任何权力，你的父亲不会死，王国也许会走上一条完全不同的道路。"
    else:
        "白纸黑字，印证了日记中的一切。父亲确实是先王指定的摄政者。"

    "但这一切都被一个女人的野心毁掉了。"

    hide player_char_img
    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "费雷恩没有销毁它。他留了一份……还有印章……作为保护自己的筹码。"

    bishop "但他还是被灭了口。而我……一直活在恐惧中，守着这个匣子，不敢看，不敢说。"

    hide bishop_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "印章是关键。有了它，我们可以证明官方版本的遗诏是伪造的。"

    hide player_char_img
    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "是的。费雷恩在信中说得很清楚——官方遗诏上的印章是仿制的。对比细节就能看出差异。"

    hide bishop_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "这意味着……我们不只有遗诏原件，还有证明伪造的物证。"

    "你感到一阵眩晕。这比你预想的还要有力。"

    player "你为什么不站出来？"

    hide player_char_img
    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "因为我怕死。"

    "主教的声音很轻，充满了羞耻。"

    bishop "费雷恩死的时候，我亲眼看到了那些人的手段。我害怕了。我选择了沉默。"

    bishop "二十年……我带着这个秘密活了二十年。每天都在祈祷上天宽恕我的怯懦。"

    menu:
        "为他设一条退路——以艾登堡的名义保他余生" if loyalty >= 60:
            $ change_stat("loyalty", 5)
            $ change_rel("rel_bishop", 20)
            $ change_stat("faith", 3)
            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "二十年的恐惧， 够了。"
            player "你跟我回艾登堡。我给你一座院子， 一队卫士， 一份没人能动的安宁。"
            player "你余生只做一件事——把你知道的， 写下来。"
            $ hide_all_chars()
            "马修斯哭了。这次不是悔恨——是终于有人愿意接住他这二十年的重量。"
            "你给了一个怕死的老人一条可以坦然走完的路。这比惩罚更难， 也更值得。"

        "严厉斥责——'你的沉默害死了我的父亲'":
            $ change_rel("rel_bishop", -15)
            $ change_stat("power", 5)
            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "如果你早些站出来，我的父亲就不用死！"
            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "我知道……我知道！我的罪孽深重……"
            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "但现在后悔已经来不及了。你能做的，就是帮我把这件事做到底。"
            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "……是。我会的。这是我唯一能赎罪的方式。"

        "表示理解——'你也是受害者'" if faith >= 58:
            $ change_rel("rel_bishop", 15)
            $ change_stat("faith", 12)
            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "费雷恩的错不应该由你来承担。你保住了这份遗诏——这已经足够。"
            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "领主大人……你和老领主一样宽容。"
            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "但从现在起，你必须和我站在一起。"
            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "我愿意。以上天之名，我愿意。"

        "冷静分析——'这份遗诏需要验证'":
            $ change_stat("reputation", 5)
            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我们不能贸然使用这份遗诏。首先要确认它的真实性。"
            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "你说得对。我可以安排教会的文书专家来鉴定。"
            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "不行。教会里不知道还有没有暗焰的人。我们需要一个中立的专家。"
            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "……你考虑得很周到。"

    hide bishop_img with dissolve

    if not testament_original_obtained:
        $ testament_original_obtained = True
        $ hide_all_chars()
        "你小心翼翼地将遗诏收好，藏在贴身的衣物里。"

        "这份遗诏——如果是真的——就是改变整个王国的钥匙。"

        "但同时，它也是一个致命的烙印。"

        "谁拿着它，谁就是王后的头号目标。"

    if ch3_prepared_first:
        ## 已做过证据准备，跳过 ch3_prepare_evidence 直接进入后续
        jump ch3_post_evidence
    else:
        jump ch3_prepare_evidence

## ============================================================
## crisis 候选 B (2026-05-11): 主教对峙起誓型 menu 选项的 win/lose 分支
## menu 入口在 chapter3.rpy:4079 第 4 选项 (faith >= 30)
## win → jump ch3_bishop_take_to_vault (同 3 原选项收尾, 拿到原件)
## lose → 没拿到原件 + jump ch3_prepare_evidence (testament 留 default False)
## ============================================================

label ch3_bishop_oath_win:
    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "……我信你。"

    bishop "费雷恩当年也起过誓。他发誓时眼神不对——我看了一辈子人，看得出来。"

    bishop "您，我赌您一次。"

    bishop "盒子，我给您。"

    $ change_rel("rel_bishop", 20)
    $ change_stat("faith", 8)

    hide bishop_img with dissolve

    jump ch3_bishop_take_to_vault

label ch3_bishop_oath_lose:
    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "……您父亲也起过誓。我看着他守了一辈子。"

    bishop "您还年轻。这种誓——您还扛不住。"

    bishop "盒子的事，我不能给您。"

    bishop "您去别处找证据吧。这里没有。"

    hide bishop_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "……"

    $ hide_all_chars()
    "你站了一会儿，没说话。"

    "马修斯转身回了内殿。教堂门外，风把落叶卷上石阶。"

    "你空手回了住处。接下来要找的证据，得换条路。"

    $ change_stat("faith", -3)

    jump ch3_prepare_evidence

    ## --- 准备证据 ---
label ch3_prepare_evidence:

    scene bg study with dissolve
    $ unlock_gallery("bg_study")
    $ play_music("audio/music/night_mystery.ogg", fadein=2.0)

    "你回到书房，把所有的证据摊在桌上。"

    if not testament_forged_known:
        "一、父亲的密码日记——记录了暗百合的联络和先王遗诏被篡改的事实。"
    else:
        "一、父亲的密码日记——你已熟知其中的每一条线索。"

    "二、暮色之露——毒杀先王和父亲的毒药，来源指向教会。"

    if poison_evidence:
        "三、毒药的残留物证——从父亲的遗物中提取。"

    if dark_lily_joined:
        "四、暗百合首领的证词——尽管是口头的，但与其他证据相互印证。"
    elif not dark_lily_destroyed:
        "四、关于暗百合的情报——虽然你未加入他们，但从各方渠道获得的信息相互印证。"

    if not baron_is_darkflame_known:
        "五、艾琳娜的情报——男爵是暗焰首领，王后在暗中布局。"
    else:
        "五、艾琳娜的情报——关于男爵和王后的阴谋，你已了然于胸。"

    "这些证据单独来看都不够有力，但放在一起——"

    "一条完整的证据链正在形成。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "还不够。我需要一个无法辩驳的铁证。"

    "你沉思良久。"

    if testament_original_obtained:
        "最关键的证据——先王的原始遗诏——已经在你手中了。"
    else:
        $ hide_all_chars()
        "最关键的证据——先王的原始遗诏——还不在你手中。"

        "但你知道线索指向谁——马修斯。费雷恩的学生，教会秘密的继承者。"

        hide player_char_img with dissolve

        "准备工作已经就绪。现在，是时候去找马修斯了。"

        jump ch3_confront_bishop_early

    "你目前能做的就是把已有的证据妥善保管，防止被人销毁。"

    if secret_passage_found and dark_lily_joined:
        "你在书房的暗格里藏了一份副本，又通过密道把另一份副本送到了暗百合那里。"
    elif secret_passage_found:
        "你在书房的暗格里藏了一份副本，又通过密道把另一份副本藏在了地下通道深处的隐蔽角落。"
    else:
        "你在书房的暗格里藏了一份副本，又让奥尔德里克秘密地把另一份副本送到了安全的地方。"

    "鸡蛋不能放在一个篮子里。"

    "做完这一切后，你终于允许自己稍微放松了一下。"

    "你靠在椅子上，闭上眼睛。"

    "但你知道，更大的风暴正从王都的方向聚拢过来。"

label ch3_post_evidence:

    ## 扩展剧情：深度调查 / 森林探险 / 草药师支线 / 教团渗透 / 终局对峙
    ## 必须在危机之前调用，否则玩家刚经历高潮又突然回到平静调查
    call ch3_exp_investigation from _call_ch3_exp_investigation

    ## 章节深化：暗百合入会仪式 (仅正式成员, "合作"分支跳过 — 批 20 bug 修复 2026-05-26)
    if lily_full_member:
        call ch3_deep_ritual from _call_ch3_dritual

    ## NPC支线：暗百合成员考验 (同上, 仅正式成员)
    if lily_full_member:
        call npc_lily_test from _call_npc_lt3

    ## ============================================================
    ## 第八部分：抉择时刻（~400行）
    ## ============================================================

label ch3_critical_choice:

    $ play_music("audio/music/great_hall.ogg", fadein=2.0)
    scene bg great_hall with dissolve
    $ unlock_gallery("bg_great_hall")

    "又过了两天。"

    "你召集了你最信任的人——奥尔德里克和雷恩——在大厅中密谈。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    show captain_img at right with dissolve

    hide captain_img
    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我有一些事情要告诉你们。这些事情可能会改变一切。"

    $ hide_all_chars()
    "你犹豫了一下。一旦说出口，就没有回头的余地了。"

    "奥尔德里克和雷恩——他们是你在这个世界上最信任的两个人。"

    "如果连他们都不能信任，那你就真的孤身一人了。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我发现了父亲死亡的真相。"

    "你从头开始，把一切都告诉了他们。"

    if secret_passage_found and baron_is_darkflame_known:
        "密码日记。暗百合。密道。暮色之露。先王遗诏被篡改。王后的阴谋。男爵是暗焰首领。艾琳娜的双重身份。"
    elif secret_passage_found:
        "密码日记。暗百合。密道。暮色之露。先王遗诏被篡改。王后的阴谋。"
    elif baron_is_darkflame_known:
        "密码日记。暗百合。暮色之露。先王遗诏被篡改。王后的阴谋。男爵是暗焰首领。艾琳娜的双重身份。"
    else:
        $ hide_all_chars()
        "你把已经掌握的一切——从父亲的日记到王后的阴谋——一五一十地告诉了他们。"

    $ captain_truth_known = True

    "你说了整整一个小时。"

    "说完后，大厅里一片沉默。墙上那面褪色的织锦壁毯被穿堂风吹得微微鼓起，像有人在后面屏息窃听。"

    "奥尔德里克的表情像石头一样凝固。他的双手紧紧攥着椅子的扶手，指节发白。"

    "雷恩的手不自觉地握紧了剑柄。他的脸色从震惊变成了愤怒，又从愤怒变成了冷酷。"

    show captain_img angry at right with dissolve

    "最终，是奥尔德里克先开口。"

    hide player_char_img
    show aldric_img sad at left with dissolve

    aldric "……我就知道。我就知道老领主的死不简单。"

    aldric "那些年……我看着他一天天消瘦下去，以为是操劳过度。"

    aldric "但暮色之露……慢性毒药……那些症状——头晕、食欲不振、盗汗——全都对得上。"

    "老骑士的眼眶泛红了。你第一次看到他如此失态。"

    aldric "我应该发现的。我跟了他三十年，我应该发现的。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "不是你的错，奥尔德里克。父亲自己都不确定，直到最后几个月才确认。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "所以……王后才是幕后黑手？先王、老领主——都是她杀的？"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "最大的嫌疑人。而且我们现在有了物证——先王的原始遗诏和私人印章。"

    show captain_img angry at right with dissolve

    captain "那还等什么？直接公布出去！"

    hide captain_img
    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "没那么简单。"

    "老骑士已经恢复了冷静。"

    aldric "我们手中的证据虽然有力，但王后的势力盘踞王畿，再延伸到大部分外境。她控制着王畿驻军、教会、大多数贵族——"

    aldric "如果我们冒然公布，她会说遗诏是伪造的，然后以叛逆罪名讨伐我们。"

    aldric "到时候，不只是你，整个艾登堡都会被夷为平地。"

    hide aldric_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "那……我们怎么办？"

    hide captain_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "不管证据够不够，你现在处于极度危险中。王后迟早会发现你在调查。"

    aldric "也许她已经知道了——那个新来的侍从不是一直在监视你吗？"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "那个问题我已经在处理了。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "大人，您打算怎么做？"

    $ hide_all_chars()
    "你环视了一下大厅。石墙上挂毯的花纹在昏暗中几乎辨认不出。"

    "这个大厅——你父亲曾在这里做出无数决定。现在轮到你了。"

    menu:
        "主动出击——收集更多证据，联合盟友，在适当的时候公开真相" if intrigue >= 45:
            $ change_stat("intrigue", 8)
            $ change_stat("power", 5)
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我们不能坐以待毙。但也不能鲁莽行动。"
            player "继续收集证据，同时秘密联合对王后不满的其他领主。"
            player "等时机成熟，我们一起行动。"
            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "这是最稳妥的方案。但需要时间。"
            hide aldric_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "时间够吗？王后随时可能动手——"
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "时机成熟时，我会亲赴王都。但在那之前，我要确保艾登堡的安全。"
            player "雷恩，你负责领地的防御。加强城墙，训练民兵。"
            player "奥尔德里克，你帮我联络其他可能的盟友。特别是那些和王后有嫌隙的领主。"
            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "我认识几个。但他们是否愿意参与这种事……我不确定。"
            aldric "还有一句话我得说在前头，大人。联络的人越多，您的意图就越藏不住。这些领主里，难保没有一个会拿您的密信去王后那儿换一份恩宠。"
            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我知道这个险。但坐着等死，是更大的险。至少试试。"
            $ change_stat("loyalty", 5)
            ## 选择深度样板: 亮牌联络异见领主, 埋下"消息走漏"伏笔, ch4 觐见兑现
            $ courted_rival_lords = True

        "防守为主——加强领地防御，等待对方露出破绽" if power >= 55:
            $ change_stat("power", 10)
            $ change_stat("loyalty", 10)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "眼下最重要的是保护好自己和领地。"
            player "雷恩，我要你把艾登堡变成一座堡垒。加倍城防，储备粮食和武器。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "遵命。我会立刻着手。"
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "奥尔德里克，你负责内部安全。清查城堡中所有可疑的人——特别是新来的。"
            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "你是说那个新侍从？"
            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "他，还有其他任何可疑的人。"
            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "交给我。"

        "深入虎穴——主动前往王都，在核心圈子中寻找机会":
            $ change_stat("intrigue", 5)
            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我要去王都。"
            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "主动送上门？那可能是自投罗网。"
            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "也可能是唯一的机会。在王都，我可以接触到更多的信息和盟友。"
            if testament_original_obtained:
                player "而且，我们已经有了原始遗诏——要让它真正成为武器，只能带它去王都，在那里找到愿意公开它的人。"
            else:
                player "而且，如果原始遗诏真的藏在教会的某个地方——王都是最可能的藏身之处。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "太危险了，大人。在王都，您没有自己的军队。"
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我不需要军队。我需要的是智慧和人脉。"
            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "……你和你父亲一样固执。"
            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "但我会比他更小心。"

        "全面反击——联合暗百合，发动政变" if not dark_lily_destroyed:
            if dark_lily_joined:
                $ change_stat("power", 15)
                ## 选择深度 pass: 联合异端发动政变 → 忠诚不该+。僭越王权又结盟异端, 民心动摇
                $ change_stat("loyalty", -8)
                $ change_rel("rel_lily", 10)
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "不能再等了。暗百合的力量加上我们自己的军队——"
                hide player_char_img
                $ hide_all_chars("aldric_img")
                show aldric_img at left with dissolve
                aldric "政变？！你疯了吗？"
                hide aldric_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "不是疯了，是清醒了。二十年的隐忍换来的是更多的牺牲。"
                hide player_char_img
                $ hide_all_chars("captain_img")
                show captain_img at left with dissolve
                captain "大人……我愿意跟随你，但这条路一旦开始就没有回头。"
                hide captain_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "我知道。所以我们必须赢。"
            else:
                $ change_stat("power", 10)
                player "我想联合一切可以联合的力量，包括暗百合。"
                hide player_char_img
                $ hide_all_chars("aldric_img")
                show aldric_img at left with dissolve
                aldric "暗百合？你信任他们？"
                hide aldric_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "我不完全信任。但敌人的敌人就是朋友。"
                hide player_char_img
                $ hide_all_chars("aldric_img")
                show aldric_img at left with dissolve
                aldric "暂时的朋友。别忘了，暗百合内部也有叛徒。"
                hide aldric_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "我会小心的。"

    hide aldric_img with dissolve
    hide captain_img with dissolve

    $ hide_all_chars()
    "决策已定。"

    "你知道，从这一刻起，一切都不可能回到从前了。"

    "这条路通向哪里，你看不到头。"

    "无论结局如何，你都不后悔。"

    "因为这条路，是你父亲用生命为你铺就的。"

    ## ============================================================
    ## 第九部分：教会的干预（~400行）
    ## ============================================================

label ch3_church_intervention:

    $ play_music("audio/music/church_choir.ogg", fadein=2.0)
    scene bg church_interior with dissolve
    $ unlock_gallery("bg_church_interior")

    "就在你以为一切尽在掌控时，教会出手了。"

    "那天清晨，你还在书房里研究证据。窗外的天空阴沉沉的，乌云从西面压过来。"

    "一阵急促的敲门声打断了你的思绪。"

    "开门一看——是教堂的一个小修士，满头大汗，气喘吁吁。"

    $ hide_all_chars("servant_generic_img")
    show servant_generic_img at left with dissolve
    messenger "领主……领主大人！主教大人让小人送这封信给您！他说万分紧急！"

    $ hide_all_chars()
    "你接过信。信封没有封蜡——说明主教来不及做正式的封印。"

    "信上写着：「领主大人，教堂，现在，一个人。——马修斯。」"

    "字迹潦草。你能感觉到写信时的慌张。"

    "你立刻披上斗篷，快步走向教堂。"

    scene bg church_interior with dissolve
    $ unlock_gallery("bg_church_interior")

    "教堂里比平时安静。几个修士低着头在走廊上匆匆走过，没有人抬头看你。"

    "教堂里安静得让人发紧。"

    "你来到教堂的后厅。主教站在祭坛前，背对着你。他的肩膀在微微发抖。"

    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve

    "马修斯转过身。他的脸色苍白如纸，嘴唇微微发青——像是受了极大的惊吓。"

    bishop "领主大人，出事了。大事不好了。"

    hide bishop_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "冷静。告诉我发生了什么。"

    hide player_char_img
    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "王都的教会总部……昨天深夜派人来了。不是普通的使者——"

    bishop "是一个审判官。"

    $ hide_all_chars()
    "审判官。"

    "在教会的体系中，审判官是最令人恐惧的存在。他们拥有不受限制的调查权，可以搜查任何教会产业，审讯任何神职人员。"

    "甚至连地方主教也无法拒绝他们的要求。"

    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "他叫赛巴斯蒂安。据说是教会中最冷酷的审判官之一。"

    bishop "他带着六个武装护卫——每一个都佩戴着教会审判庭的徽章。"

    hide bishop_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "一个审判官来这种偏远的地方？这不寻常。"

    hide player_char_img
    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "非常不寻常。审判官通常只在大教区活动。他们来到艾登堡——只有一个原因。"

    bishop "他……他在调查费雷恩的案子。"

    hide bishop_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "什么？费雷恩早已秘密去世——"

    hide player_char_img
    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "但有人重新打开了这个案子。赛巴斯蒂安说，教会总部最近收到了「可靠的举报」。"

    bishop "举报说费雷恩临终前留下了一些「危险的文件」——"

    bishop "而且这些文件可能在我手中。"

    "你的心猛然一紧。"

    hide bishop_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你告诉他了？"

    hide player_char_img
    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "没有！我发誓我没有。我装作一无所知。"

    bishop "但赛巴斯蒂安不是好糊弄的人。他盯着我看了整整一分钟——像在读我的灵魂。"

    bishop "他说：「马修斯主教，费雷恩大主教是你的老师。他死前的最后几天，只有你在他身边。如果他留了什么东西，你一定知道。」"

    bishop "我否认了。但他显然不信。"

    hide bishop_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "是谁举报的？"

    hide player_char_img
    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "我不知道。但消息的准确性——有人知道费雷恩留了东西给我。"

    bishop "能知道这件事的人……"

    hide bishop_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "暗焰。"

    hide player_char_img
    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "你也这么想？"

    hide bishop_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    if not baron_is_darkflame_known:
        player "冯·哈根男爵——暗焰的首领。他一定有人渗透在教会内部。"
    else:
        player "男爵的手一定伸进了教会内部。"

    hide player_char_img
    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "赛巴斯蒂安明天就要正式搜查教堂的密室。他有权这么做——我无法拒绝。"

    bishop "如果他找到那个盒子……"

    $ hide_all_chars()
    "你明白了。"

    if testament_original_obtained:
        "原始遗诏已经在你手里，但印章和父亲留下的信还在那个盒子里——一旦落入审判官之手，就等于给了王后把你和马修斯一起定罪的口实。"
    else:
        "如果审判官拿到了原始遗诏和印章——那一切证据都会消失。"

    "教会总部会把这些东西送到王都。王后会亲手销毁它们。"

    "然后，真相将永远被埋葬。"

    "你绝不能让这种事发生。"

    menu:
        "今晚就把盒子转移走" if intrigue >= 45:
            $ change_stat("intrigue", 8)
            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你能在今晚把盒子从密室里取出来吗？"
            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "可以……但如果审判官发现盒子不见了，他会怀疑我。"
            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "那就让他怀疑。你的安全我来保障。"
            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "……好。今晚子时，密室。"
            $ hide_all_chars()
            "你点了点头，转身离开教堂。"
            "你需要安排一个万全的计划。"

        "先见见这个审判官，摸清他的底细":
            $ change_stat("power", 5)
            $ change_stat("reputation", 5)
            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我想见见这个审判官。"
            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "你……你确定？他不是好惹的人。"
            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "正因为如此，我更要亲自了解他。"
            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "他叫赛巴斯蒂安。据说是教会中最冷酷的审判官之一。"
            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "安排我和他见面。就说我是来欢迎教会使者的。"
            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "好……好吧。"

        "让暗百合的人处理" if not dark_lily_destroyed:
            if dark_lily_joined:
                $ change_stat("intrigue", 8)
                $ change_stat("reputation", -2)
                $ change_rel("rel_lily", 5)
                hide bishop_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "我会联系影。暗百合有办法对付教会的审判官。"
                hide player_char_img
                $ hide_all_chars("bishop_img")
                show bishop_img at left with dissolve
                bishop "暗百合？你真的和他们有联系？"
                hide bishop_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "你不需要知道细节。但我不会让遗诏落入王后的手中。"
                hide player_char_img
                $ hide_all_chars("bishop_img")
                show bishop_img at left with dissolve
                bishop "……我开始理解你父亲为什么信任暗百合了。"
            else:
                $ change_stat("intrigue", 5)
                hide bishop_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "我有一些……特殊的渠道可以处理这件事。"
                hide player_char_img
                $ hide_all_chars("bishop_img")
                show bishop_img at left with dissolve
                bishop "什么渠道？"
                hide bishop_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "你不需要知道。但你需要配合我。"
                hide player_char_img
                $ hide_all_chars("bishop_img")
                show bishop_img at left with dissolve
                bishop "好。只要能保住那个盒子。"

        "将计就计——让审判官找到一个假的盒子":
            $ change_stat("intrigue", 5)
            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "马修斯，你还有别的密封盒子吗？大小差不多的。"
            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "有……一个放圣物的盒子，大小相近。"
            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "今晚把遗诏取出来，放进一些无关紧要的教会文件到原来的盒子里。"
            player "让审判官找到它。他拿走的是一个空壳。"
            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "偷梁换柱……你的心思缜密得可怕。"
            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "在这盘棋局中，不缜密就会死。"
            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "……我明白了。今晚就办。"

    hide bishop_img with dissolve

    $ hide_all_chars()
    "你走出教堂。外面开始下雨了——细密的雨丝打在你的脸上。"

    "你站在教堂门口，看着灰蒙蒙的天空。"

    "教会的介入让局势更加复杂了。"

    "审判官的到来意味着——王后已经嗅到了危险。她不再满足于通过男爵暗中操控，而是动用了教会这个最强大的工具。"

    "教会审判庭的权力几乎不受限制。在教会的领地上——包括教堂和修道院——审判官的权力甚至大于领主。"

    "这意味着你无法用武力阻止搜查。强行阻止教会审判只会给王后一个讨伐你的完美借口——「蔑视神权」。"

    "你必须用智慧。"

    "你快步返回城堡。"

    "在路上，你遇到了艾琳娜。她撑着一把伞，像是专门在等你。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve

    elena "领主大人，我听说教堂来了一个审判官。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "消息传得真快。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "他叫赛巴斯蒂安·维克多。我在王都的时候就听说过他的名字。"

    elena "他是王后最信任的教会打手之一。表面上是审判官，实际上替王后做很多见不得光的事。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你确定？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "确定。他之前「调查」过另外两个对王后有威胁的地方主教。一个被免职，一个死在了审判过程中——「心脏病突发」。"

    "你的血液都凉了。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "所以他不只是来搜查的——他可能还要对马修斯动手。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "很有可能。王后想一石二鸟——拿到费雷恩留下的东西，同时消除马修斯这个知情者。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我不能让这种事发生。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "我有一个建议。"

    elena "赛巴斯蒂安有一个弱点——他贪财。教会审判官的俸禄其实很低，但他过着奢侈的生活。"

    elena "如果你能在他面前展示足够的利益——也许可以暂时拖住他。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "用钱买时间？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "不只是钱。领地的支持、教会在艾登堡的特权——他在乎这些。"

    menu:
        "采纳艾琳娜的建议，同时做两手准备":
            $ change_stat("loyalty", 5)
            $ change_stat("wealth", -5)
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "好主意。你帮我安排一次和赛巴斯蒂安的「偶遇」。让他觉得我是一个值得拉拢的人。"
            player "同时，我去安排证据的转移。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "明白。我会处理好的。"

        "不信任她的判断，自己来处理":
            $ change_stat("power", 5)
            $ change_stat("faith", 5)
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我自有安排。你做好你的本职工作就行。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "……是，领主大人。"
            "她什么都没说，走的时候没回头。门关上的声音比平时重了一些。"

    hide elena_img with dissolve

    scene bg study with dissolve
    $ unlock_gallery("bg_study")

    "回到城堡后，你立刻找来了雷恩。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "雷恩，教堂来了一个教会审判官——赛巴斯蒂安·维克多。这个人很危险。我需要你做几件事。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "审判官？我听说那些人有生杀予夺的权力。他们有权力搜查任何地方，甚至领主的城堡。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "理论上是的。但在我的领地上，没有我的允许，谁也别想横行霸道。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "需要我做什么？"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "三件事。第一，安排人手守住教堂附近的所有出入口。如果审判官试图带走什么东西或者带走什么人，我要第一时间知道。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "明白。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "第二，把城堡的安保提升到最高级别。我有一种预感，教会的审判官只是前奏，接下来可能还有更大的动作。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "大人……您是说……"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我在说，做好最坏的打算。"

    "雷恩的表情凝重了。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "我去安排。"

    hide captain_img with dissolve

    $ hide_all_chars()
    "当夜晚来临时，你没有睡觉。"

    "你坐在书房的窗边，看着教堂方向的灯火。"

    "主教在那里，正在执行你的计划。"

    "审判官也在那里，可能正在磨刀霍霍。"

    "而你……在等待。"

    "等待一个时机——"

    "当所有的棋子都到位的时候，给出致命的一击。"

    "深夜时分，一只信鸽落在你的窗台上。"

    "鸽子的脚上绑着一个小纸条。你打开它。"

    "纸条上只有三个字：「已完成。」"

    "主教成功了。遗诏安全了。"

    "你终于允许自己松了一口气。"

    "但你没有去睡。你在窗边又坐了很久。"

    ## ============================================================
    ## 第十部分：章末危机（~300行）
    ## ============================================================

label ch3_chapter_crisis:

    $ set_mood("battle")
    $ play_music("audio/music/battle_prepare.ogg", fadein=2.0)
    scene bg castle_exterior with dissolve
    $ unlock_gallery("bg_castle_exterior")

    "第二天黎明。"

    "你被急促的敲门声惊醒。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "大人！紧急情况！"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "怎么了？"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "城外发现了一支武装人员！大约两百人，正在从南面逼近！"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "什么？！"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "他们没有打旗帜，没有任何标识。但装备精良——全副武装。"

    "你迅速穿上衣甲，跑上城墙。"

    hide captain_img with dissolve

    scene bg castle_exterior with dissolve
    $ unlock_gallery("bg_castle_exterior")

    "在晨雾中，你看到了他们——一支黑压压的队伍，从森林中涌出，正在向城堡推进。"

    "没有旗帜，没有号角——这不是正规军。"

    "这是暗焰的私兵。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    show captain_img at right with dissolve

    hide captain_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "他们来了。比我预想的快。"

    hide aldric_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "大人，城堡的守军只有一百五十人。敌人至少有两百。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "他们的目的是什么？攻城？"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "不。他们的目的是你。或者更准确地说——是你手中的证据。"

    aldric "消息走漏了。不知道是谁泄的密。"

    "你咬紧牙关。"

    menu:
        "全力防守——死守城堡" if power >= 60:
            $ change_stat("power", 15)
            $ change_stat("loyalty", 10)
            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "关闭所有城门！全军上墙！"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "遵命！"
            $ hide_all_chars()
            "号角声响彻艾登堡。城门轰然关闭，吊桥升起。"
            "士兵们迅速就位，弓箭手排列在城墙上。"
            "你站在城墙最显眼的位置，让所有人都能看到你。"
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "他们以为两百人就能拿下艾登堡？告诉他们，他们错了！"
            $ hide_all_chars()
            "守军发出一声怒吼。士气高涨。"
            "敌人在城墙下停住了。他们似乎没想到城堡已经有了准备。"
            "双方对峙了一个上午。最终，敌人在午时撤退了。"
            "他们不是来攻城的——他们是来试探的。"
            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "他们会再来。下一次，人数会更多。"
            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "那我们就用这段时间做准备。"

        "派人突围求援" if secret_passage_found:
            $ change_stat("loyalty", 5)
            $ change_stat("wealth", 5)
            player "雷恩，派你最快的骑手突围求援。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "北门外也有敌人的哨骑——"
            if captain_knows_passage:
                hide captain_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "那就用密道——你和奥尔德里克都知道的那条。"
                hide player_char_img
                $ hide_all_chars("captain_img")
                show captain_img at left with dissolve
                captain "明白。我立刻安排骑手。"
            else:
                hide captain_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "那就用密道。"
                hide player_char_img
                $ hide_all_chars("captain_img")
                show captain_img at left with dissolve
                captain "密道？"
                hide captain_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "城堡下面有密道通向外面。我发现的。奥尔德里克知道路线。"
                "奥尔德里克点了点头。"
            hide player_char_img
            hide captain_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "我带人从密道出去。两天之内，援军就到。"
            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "去吧。小心。"
            $ hide_all_chars()
            "奥尔德里克带着两个信使消失在城堡地下。"
            "你则留在城墙上，指挥防御。"

        "主动出击——在他们完成包围之前冲出去" if power >= 65:
            $ change_stat("power", 20)
            $ change_stat("loyalty", 5)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "他们还没有完成包围。南面的这支是主力——北面一定薄弱。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "大人想突围？"
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "不是突围。是反击。"
            player "我亲自带五十人从北门出击，绕到他们侧翼。雷恩，你带剩下的人守城。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "大人！太危险了！"
            hide captain_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "让他去。他父亲年轻时也是这样——亲自上阵。"
            $ hide_all_chars()
            "你带着五十名精锐骑兵从北门冲出。"
            "正如你所料，敌人的主力集中在南面。北面只有少量哨骑。"
            "你绕了一个大弧，从西面杀入敌人的侧翼。"
            "突如其来的打击让敌人阵脚大乱。他们没想到守军会主动出击。"
            "混战持续了不到半个小时。敌人撤退了，留下了十几具尸体。"
            "你俘虏了三个人。也许能从他们口中得到有用的信息。"

        "通过密道转移证据——保命要紧" if secret_passage_found:
            $ change_stat("intrigue", 8)
            $ _take_alt_route = False

            if ch1_deep_cellar_choice == "seal" and not passage_re_opened:
                $ hide_all_chars("aldric_img")
                show aldric_img at left with dissolve
                aldric "大人——密道虽然您下令封了，但石墙不是一夜之间砌起来的。"
                aldric "若您下令，工匠和卫队连夜可以重新打通。代价是花费些时间和材料……且封过又开的事，难免要走漏些风声。"

                hide aldric_img with dissolve

                menu:
                    "重新启用密道——花代价换回退路":
                        $ change_stat("wealth", -10)
                        $ change_stat("intrigue", -3)
                        $ change_stat("loyalty", -3)
                        $ change_rel("rel_baron", -3)
                        $ passage_re_opened = True

                        $ hide_all_chars()
                        "你下令重启密道。两位老工匠领着十几个卫队连夜砸开砖墙——天亮前，密道再次贯通。"
                        "但消息也悄悄传进了几个老姓氏的耳朵里。封死的东西被重启，本身就是一种信号。"

                    "不重启——另寻他法":
                        $ change_stat("intrigue", 5)
                        $ change_stat("power", -5)
                        $ change_stat("wealth", -3)
                        $ _take_alt_route = True

                        $ hide_all_chars("player_char_img")
                        show player_char_img at left with dissolve
                        player "密道已经封了。我们另想办法。"
                        player "雷恩，让你最可靠的两名侍卫换上商队衣袍——明日清晨借采办名义出北门。"
                        player "证据由我亲手装好，让其中一人贴身藏匿。北门哨骑认识艾登堡的采办车，应该不会查得太严。"

                        hide player_char_img
                        $ hide_all_chars("captain_img")
                        show captain_img at left with dissolve
                        captain "可若是查到了——"

                        hide captain_img
                        $ hide_all_chars("player_char_img")
                        show player_char_img at left with dissolve
                        player "查到就一同担。两位侍卫的家眷我会照顾终生，他们也明白。"

                        $ hide_all_chars()
                        "你回到书房，把日记、遗诏副本、关系图缝进一卷羊皮护贴。两名侍卫领命离开。"
                        "押上命的不只是那两个人。这一夜你睡在书房——窗外攻城的号角断断续续，像是有人在催债。"

            if not _take_alt_route:
                hide aldric_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "证据比城堡重要。如果他们是冲着证据来的，就不能让他们得手。"
                player "奥尔德里克，你和雷恩守城。我从密道离开，把证据转移到安全的地方。"
                hide player_char_img
                $ hide_all_chars("aldric_img")
                show aldric_img at left with dissolve
                aldric "你要独自走密道？"
                hide aldric_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "不是独自。艾琳娜知道密道的路线。她和我一起走。"
                hide player_char_img
                $ hide_all_chars("aldric_img")
                show aldric_img at left with dissolve
                aldric "……你确定？"
                hide aldric_img
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "确定。"
                $ hide_all_chars()
                "你回到书房，取出所有的证据——日记、遗诏副本、关系图——全部装进一个皮囊。"
                "然后，你和艾琳娜一起走进了壁炉后的密道。"
                "在你身后，城堡响起了战斗的号角。"

    hide aldric_img with dissolve
    hide captain_img with dissolve

    "不管你选择了什么，一件事是确定的——"

    "消息已经走漏了。敌人知道你在调查什么，也知道你掌握了什么。"

    "安全的假象已经彻底破碎了。"

    ## 扩展/深化/NPC支线已移至抉择时刻之前（ch3_critical_choice上方）
    ## 避免危机高潮后突然跳回平静调查场景

    ## 治理报告
    call gov_report from _call_gov_rep3

    ## ============================================================
    ## 第三章结尾
    ## ============================================================

label ch3_end:

    $ clamp_stats()
    $ check_max_stat()
    $ persistent.chapters_completed.add("chapter3")

    ## 章节结束统计
    call show_chapter_summary("第三章", "暗百合") from _call_show_chapter_summary_1

    if true_killer_known:
        $ unlock_achievement("truth_seeker")
    if secret_passage_found:
        $ unlock_achievement("secret_passage")

    $ play_music("audio/music/tension.ogg", fadein=2.0)
    scene black with dissolve

    "线索已经够了。现在需要的是决定。"

    "几天过去了。"

    "城堡外墙上被攻城车砸出的缺口还没补完，被烧掉的储粮已经从邻近村庄紧急调来。但死去的卫兵再也回不来——你连给每家都派人送抚恤的时间都还不够。"

    "伤势最重的几个在医师的帐篷里呻吟了整整三天。你亲自守过其中两夜。"

    ## ── 政治联姻线「盟约」入口(希尔达伯爵夫人遣使) ──
    "你还没缓过气，北边先来了人。"

    "灰隘口的信使在午后到达。他没穿议会的制服，斗篷上沾着北边的雪。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "希尔达伯爵夫人派你来的？"

    "信使递上一封火漆封口的信。火漆上压的是北疆议会的渡鸦纹，不是哪一家的私章。你拆开。希尔达的字迹很硬，像她本人。"

    "『艾登堡的继承人：北境的盐路断了三个月，议会撑不了第二个冬天。我需要一个南边的盟友，一个靠得住、不会在开春后翻脸的盟友。』"

    "『把话挑明：我有一个女儿，英格丽。你还没成婚。盟约写在纸上随时能撕，写进血脉里就不一样了。你考虑清楚，开春前给我答复。』"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "北疆议会的盟约……这不是小事。希尔达不是会为感情送女儿的人。她要的是艾登堡的兵和粮。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve

    menu:
        "回信，愿意谈这桩联姻":
            $ marriage_route = True
            $ log_decision("第三章", "接受希尔达伯爵夫人的联姻提议")
            $ change_stat("intrigue", 3)
            player "回信给伯爵夫人。就说——这个冬天，艾登堡和北疆议会站在一起。"
            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "我这就安排。开春前，议会的人会再来。"

        "婉拒，我另有打算":
            $ log_decision("第三章", "婉拒联姻提议")
            player "替我谢过伯爵夫人的好意。盟约可以谈，但不必用婚约来绑。"

        "先拖着，看看北境的局势再说":
            $ ch3_marriage_delayed = True
            $ log_decision("第三章", "对联姻提议拖延")
            player "回信说我需要时间。北境的事，我得先弄清楚。"

    $ hide_all_chars()

    "就在你以为喘口气的时候，一封来自王都的信送到了艾登堡——"

    "尽管城堡刚刚经历了一场袭击，信使仍然准时送达了王后的旨意。"

    "『伊莎贝拉王后陛下宣召艾登堡领主入都觐见。不得推辞。』"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve

    elena "领主大人……坏消息没完。王后召你入都。"

    elena "偏偏挑在这个时候。这可能是一个机会……也可能是一个陷阱。"

    elena "更大的可能——王后就是算准了你刚打完仗、元气未复，才抓这个节骨眼让你上路。"

    if dark_lily_joined:
        if elena_spy_known:
            elena "我的身份你已经知道了。既然你也和影达成了协议——接下来我们站在同一边。"
            elena "去王都的路上，我会一直在你身边。这是影的命令，也是我自己的选择。"
        else:
            elena "还有一件事。我知道暗百合联系过你。"
            elena "因为……我也是暗百合的人。"
            "你看着她。这一次，你没有感到惊讶。"
            elena "王后派我来监视你，但暗百合也安排我保护你。我一直身负双重使命。"
            elena "去王都的路上，我会保护你。这是影的命令，也是我自己的选择。"
            $ elena_spy_known = True
            $ elena_identity_exposed_known = True
        $ change_rel("rel_elena", 20)
        $ change_stat("loyalty", 5)
    else:
        elena "但不管是什么……您不能不去。拒绝王后的宣召，等于公开叛逆。"
        elena "而且……也许王都才是解开所有谜团的地方。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我会去的。"

    "你看了一眼窗外。天边乌云密布，一场暴风雨正在酝酿。"

    player "在去之前，我要做好万全的准备。"

    player "因为这一次——也许就没有回来的机会了。"

    hide elena_img with dissolve

    $ hide_all_chars()
    "你转过身，看着父亲的画像。"

    "画像中的老领主目光温和，但嘴角似乎带着一丝苦涩的微笑。"


    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "父亲……我会替你完成一切。"

    $ hide_all_chars()
    "你轻声说。"

    "然后，你开始整理行囊。"

    "王都之行，九死一生。"

    "但你别无选择。"

    if dark_lily_joined:
        "你握紧了怀中暗百合的银质徽章。"
        "暗处的力量，将与你同行。"
    elif dark_lily_destroyed:
        "你握紧了腰间的短剑。"
        "不靠任何人。只靠自己。"
    else:
        "你低头看着自己的双手。"
        "这一次，你谁也不靠。"

    if dark_lily_destroyed:
        "暗百合的残党或许还在暗处潜伏。但那已经是明天的事了。"
    else:
        "暗百合的故事还远未结束。"

    "而你的故事……远未到落幕的时候。"

    scene black with dissolve

    $ renpy.force_autosave()

    jump chapter4_start

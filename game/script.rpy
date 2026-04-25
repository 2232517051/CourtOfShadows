## ============================================================
## 权谋之庭 - Court of Shadows
## 第一章：新主登基
## ============================================================

## 隐私政策弹窗 — 在主菜单之前弹出（TapTap合规要求）
label splashscreen:
    if not persistent.privacy_agreed:
        call screen privacy_policy_screen
    return

label start:

    ## 如果序章尚未完成，先跳转到序章
    if not prologue_completed:
        jump prologue

    ## ============================================================
    ## 第一章：新主登基
    ## ============================================================

    ## 成年期主角肖像
    $ player.image_tag = "player_char"

    ## 第一章过场动画
    call cinematic_chapter1 from _call_cinematic_ch1

    ## 序幕
    $ set_mood("sad")
    $ set_weather("rain", "normal")
    stop music fadeout 1.0
    scene black with dissolve

    call show_chapter("第一章", "新主登基", "初临领地，面对未知的挑战") from _call_show_chapter_4

    ## ============================================================
    ## 梦境/回忆：父亲的最后一面
    ## ============================================================

    $ play_music("audio/music/rain_storm.ogg", fadein=2.0)
    scene bg study with dissolve
    $ unlock_gallery("bg_study")

    "——在出发前的最后一个夜晚，你做了一个梦。"

    "梦里，你回到了童年时的书房。壁炉里的火烧得正旺，映照着墙上悬挂的家族徽章。"

    "父亲坐在那把你熟悉的高背椅上，背对着你。他的肩膀宽厚而挺拔，像一座不可动摇的山。"

    "你叫了一声'父亲'。他没有回头。"

    "你想走近，但双腿像灌了铅一样沉重。每走一步，书房就好像拉长了一寸。"

    "火光突然黯淡了下去。父亲终于缓缓转过身来。"

    "他的面容苍老了许多——你记忆中那张坚毅的脸上布满了皱纹，眼窝深陷，目光中有一种你从未见过的疲惫。"

    "他张开嘴，似乎想说什么。但你什么也听不见，只有风声，像是从极远的地方呼啸而来。"

    "你努力地辨认他的口型。他在说——"

    "'不要……相信……'"

    "然后一切化为黑暗。"

    scene black with dissolve

    "你从梦中惊醒，浑身冷汗。"

    "马车仍在颠簸。窗外灰蒙蒙的天光透进来，你看到远处的山丘上，一座灰色的城堡渐渐浮现在视野中。"

    "艾登堡。"

    "你到家了。"

    ## ============================================================
    ## 场景1：抵达城堡
    ## ============================================================

label arrive_castle:

    $ play_music("audio/music/castle_calm.ogg", fadein=2.0)
    $ set_mood("calm")
    $ clear_weather()
    scene bg castle_exterior with dissolve
    $ unlock_gallery("bg_castle_exterior")
    $ play_sound("audio/sfx/horse_gallop.ogg")

    $ trigger_random_event("travel")

    "马车在泥泞的道路上颠簸了三天，终于驶入了艾登堡的领地。"

    "道路两旁是收割后的麦田，金黄的麦茬在雨中伏倒一片。偶尔有几棵老橡树矗立在田埂上，光秃秃的枝丫像是向天空伸出的枯瘦手指。"

    "空气中弥漫着泥土和腐叶的气息——那是深秋特有的、带着一丝寒意的味道。"

    "远处，灰色的城堡矗立在山丘之上，旗帜已经换成了黑色——丧旗。"

    "黑色的旗帜在风雨中沉重地翻卷，像是一只垂死的乌鸦在做最后的挣扎。城堡的轮廓在阴云下显得格外压抑，那些你儿时觉得雄伟的塔楼，此刻看来更像是一座巨大的墓碑。"

    "马车经过村庄时，你拉开了窗帘。"

    "几个农妇站在茅屋门前，怀里抱着孩子，默默地注视着你的马车驶过。她们的眼神中既有好奇，也有不安——老领主走了，新领主来了，这对她们的生活意味着什么？"

    "一个头发花白的老农站在路边，摘下破旧的帽子，朝你的方向深深鞠了一躬。"

    menu:
        "朝老农点头致意":
            $ change_stat("loyalty", 3)
            $ change_stat("reputation", 3)
            "你掀开车帘，郑重地朝老农点了点头。"
            "老人抬起头，弯下腰回了一礼——动作缓慢而郑重。他转身对身后的村民低声说了些什么，几个人也跟着弯下了腰。"
            "消息会传开的——新领主，不像传说中那么傲慢。"

        "放下窗帘，不想被人注视":
            "你放下了窗帘。此刻你没有心情应付任何人的目光。"
            "马车继续在泥泞中前行，车轮碾过水洼，溅起一片浑浊的泥浆。"

        "停下马车，走出来步行":
            $ change_stat("loyalty", 5)
            $ change_stat("reputation", 5)
            "你让车夫停下马车，自己推开车门，踩入泥泞的道路。"
            "冰冷的雨水打在脸上，但你没有退缩。你挺直腰背，沿着道路步行，让沿途的百姓都能看清你的脸。"
            "你是他们的新领主。你不会躲在马车里。"
            "村民们交头接耳，眼中的不安渐渐被另一种情绪取代——也许是敬意，也许是期待。"

    "城门前，一位白发苍苍的老人和一队士兵在雨中等候。"

    "老人穿着一件深红色的长袍，胸前佩戴着家族骑士的徽章。他的脊背微微弯曲——三十年的操劳在他身上留下了不可磨灭的痕迹——但他的目光依然锐利，像一只苍老却不失警觉的猎鹰。"

    "士兵们列成两排，铠甲上沾满了雨水，长矛笔直地指向阴沉的天空。他们的面容肃穆，但你能感觉到他们在偷偷打量你。"

    $ hide_all_chars("aldric_img")
    show aldric_img sad at left with dissolve
    $ unlock_gallery("aldric")

    aldric "少主……不，领主大人，欢迎回家。"

    "老人单膝跪地，声音微微发颤。他的眼眶泛红，你看得出他已经哭过了——也许不止一次。"

    aldric "老臣奥尔德里克，在此恭迎。请恕老臣未能保住老领主……"

    $ hide_all_chars()
    "他的声音哽住了。身后的士兵们同时单膝跪地，甲胄的碰撞声在雨中回响。"

    "你如何回应？"

    menu:
        "安慰他——『父亲的事不怪你，奥尔德里克。』":
            $ change_rel("rel_aldric", 10)
            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "父亲的事不怪你，奥尔德里克。你守护此地多年，辛苦了。"
            "你伸出手，将老人扶起。他的手粗糙而冰冷，握住你的那一刻，微微发抖。"
            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "领主大人宅心仁厚……老臣定当竭尽全力辅佐。"
            "老人抹了一把脸上不知是雨水还是泪水的东西，挺直了腰板。"
            aldric "老领主生前常说，少主有仁者之心。今日一见，果然如此。"

        "追问——『父亲究竟怎么死的？』":
            $ change_stat("reputation", 5)
            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "信上只说突发恶疾。我要听实话，奥尔德里克。"
            "老人的身体明显僵了一下。他的目光闪烁了一瞬，随即恢复了平静。"
            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "这……此处不是说话的地方。请领主大人先入城，稍后老臣详禀。"
            "他压低了声音，几乎只有你能听见。"
            aldric "城墙上有眼睛，路上有耳朵。领主大人，忍耐片刻。"
            $ father_death_known = True

        "表现威严——『我知道了。带我去大厅。』":
            $ change_stat("power", 5)
            $ change_stat("reputation", 5)
            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我知道了。前面带路。"
            "你的声音平静而冷淡，没有多余的情感。"
            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "……是，领主大人。请。"
            "老人慢慢站起身，脸上的悲伤被一层恭敬的面具所取代。但你注意到他的肩膀微微下沉了一些——仿佛你的冷淡在他身上又加了一层重担。"
            $ change_rel("rel_aldric", -5)

    hide aldric_img with dissolve

    ## --- 穿过城门，进入城堡 ---

    $ play_sound("audio/sfx/door_knock.ogg")

    $ hide_all_chars()
    "沉重的铁闸在绞盘的吱嘎声中缓缓升起。你走过吊桥，脚下的木板在雨水中发出沉闷的回响。"

    "护城河的水面泛着灰绿色的光，散发出一股陈腐的气息。几只乌鸦停在城墙的垛口上，歪着头打量你——这座城堡新的主人。"

    "穿过城门洞，一股夹杂着干草、马匹和炊烟的气味扑面而来。这是城堡的味道——你儿时再熟悉不过，如今却恍如隔世。"

    ## ============================================================
    ## 新增场景：城堡庭院探索
    ## ============================================================

    "你没有急着走进大厅，而是在庭院中停下了脚步。你想先看看这座城堡真实的模样——不是从书信中读到的，不是从回忆中拼凑的，而是此刻、此地、你亲眼所见的艾登堡。"

    "庭院的地面铺着粗糙的碎石，缝隙间长满了枯黄的杂草。一口老井立在院子中央，井沿的石头被岁月磨得光滑发亮。几只母鸡在马厩旁边啄食，对你的到来毫不在意。"

    "马厩里传来马匹打响鼻的声音。你走过去，看见一个满脸雀斑的少年正在给一匹黑马刷毛。他发现你的目光后，吓得手中的刷子差点掉在地上。"

    $ hide_all_chars("stable_boy_img")
    show stable_boy_img at left with dissolve
    stable_boy "领、领主大人！小的……小的是马厩的学徒，叫……叫汤米……"

    $ hide_all_chars()
    "少年的声音像是被捏住脖子的鹅，又尖又颤。他的膝盖磕在地上，发出一声闷响。"

    "你注意到他的衣服打了好几个补丁，双手通红——那是长期在寒冷中劳作留下的冻疮痕迹。"

    "旁边的铁匠铺里，一个光着膀子的壮汉正在敲打一块烧红的铁。火星四溅，映红了他汗涔涔的脸。看到你，他放下铁锤，粗声粗气地喊了一声。"

    hide stable_boy_img
    $ hide_all_chars("soldier_generic_img")
    show soldier_generic_img at left with dissolve
    soldier "新领主来了！大伙儿，行礼！"

    $ hide_all_chars()
    "几个正在搬运木桶的士兵闻声停下手中的活计，朝你的方向笨拙地弯腰行礼。他们的动作参差不齐——有人鞠躬，有人单膝跪地，有人只是呆呆地站着。"

    "你看得出来，这些人不是训练有素的精锐。他们的铠甲陈旧，有的缺了护肩，有的头盔上有明显的凹痕。但他们的眼神中有一种东西——一种在逆境中仍然没有熄灭的倔强。"

    "一个年迈的老兵拄着一根拐杖，从墙根的阴影中慢慢走出来。他的左腿从膝盖以下就没有了——那是某场战役留下的代价。"

    $ hide_all_chars("soldier_generic_img")
    show soldier_generic_img at left with dissolve
    soldier "老朽……曾在老领主麾下效力三十年。领主大人……您长得真像您父亲年轻时候。"

    $ hide_all_chars()
    "老兵多站了一会儿没走，嘴唇微微颤抖。那不是对新领主的敬畏，而是对旧主的怀念在新主身上找到了寄托。"

    "庭院中的所有人都在看着你。仆人们、士兵们、铁匠、马夫——他们等着你说些什么，做些什么。对他们来说，你的第一句话，就是艾登堡未来的风向标。"

    menu:
        "走到众人中间，一一问候":
            $ change_stat("loyalty", 5)
            $ change_stat("reputation", 5)
            $ log_decision("第一章", "亲切问候城堡庭院众人")
            "你没有站在远处俯视他们，而是走进了他们中间。"
            "你拉起跪着的马厩少年，拍了拍他的肩膀。你走到铁匠面前，问他最近有没有足够的炭火。你在老兵面前停下脚步，认真地听他讲述当年追随父亲征战的往事。"
            hide soldier_generic_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你们为艾登堡付出了半辈子。从今往后，我不会让你们的付出被辜负。"
            "庭院中安静了一瞬，然后老兵第一个开口，声音沙哑却响亮。"
            hide player_char_img
            $ hide_all_chars("soldier_generic_img")
            show soldier_generic_img at left with dissolve
            soldier "艾登堡万岁！新领主万岁！"
            "其他人跟着喊了起来——声音此起彼伏，在城堡的石墙间回荡。不算整齐，不算响亮，但真诚。"
            $ change_stat("loyalty", 3)

        "以领主之姿训话，要求各司其职":
            $ change_stat("power", 5)
            $ change_stat("reputation", 3)
            $ log_decision("第一章", "以威严姿态训话城堡众人")
            "你挺直腰背，目光缓缓扫过在场的每一个人。你的声音不大，但每一个字都清晰地送入每个人的耳朵。"
            hide soldier_generic_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "艾登堡换了新主，但规矩不变。各司其职，各尽其责。懈怠者罚，勤勉者赏。"
            "庭院中鸦雀无声。士兵们不自觉地站直了身体，仆人们低下了头。"
            player "马厩要干净，铁匠铺要不停火，城墙上的哨兵不准打盹。这些是最基本的要求。做到了，是分内之事；做不到，别怪我不留情面。"
            "老兵第一个直起腰板，用拐杖在地上重重一顿。"
            hide player_char_img
            $ hide_all_chars("soldier_generic_img")
            show soldier_generic_img at left with dissolve
            soldier "领主大人说得对！老朽虽然废了一条腿，但还能看门守夜！"
            "你微微点头。威严不是靠恐吓建立的，而是靠让每个人知道你认真对待每一件事。"

        "沉默地巡视，不发一言":
            $ change_stat("intrigue", 5)
            $ log_decision("第一章", "沉默巡视城堡庭院")
            $ hide_all_chars()
            "你什么也没说。你只是慢慢地走过庭院的每一个角落，用目光丈量着一切。"
            "马厩的门闩松了，你看在眼里。铁匠铺的烟囱歪了，你记在心里。水井旁的排水沟堵了，你也注意到了。"
            "你没有夸奖任何人，也没有责备任何人。你只是看着，像一只刚刚落在高处的鹰，俯瞰着自己的领地。"
            "这种沉默比任何言语都更有压迫感。庭院中的人们屏住呼吸，不敢发出一点声响。他们读不懂你的心思——而这正是你想要的效果。"
            "在权力的游戏中，让别人猜不透你，本身就是一种力量。"

    "内院中，仆人们排成两列，低着头等候。你的目光扫过他们——洗衣妇、马夫、厨娘、园丁——这些是维持城堡运转的根基，是最容易被忽视却最不可或缺的人。"

    "你走进城堡大门，沿途的仆人和士兵纷纷低头行礼。"

    "有些眼神中是敬畏，有些是好奇，还有些……是你读不懂的东西。"

    "一个年纪约莫四十岁的妇人从人群中走出，朝你深深一礼。她的围裙上沾着面粉，但举止端庄。"

    hide soldier_generic_img
    $ hide_all_chars("servant_marta_img")
    show servant_marta_img at left with dissolve
    housekeeper "领主大人，奴婢是城堡的总管事玛格丽特。老领主在时，城堡的日常事务皆由奴婢打理。"

    housekeeper "领主大人的寝室已经收拾好了。热水、干净的衣物都备下了。"

    menu:
        "感谢她的周到安排":
            $ change_stat("loyalty", 3)
            hide servant_marta_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "辛苦了，玛格丽特。一切照旧便好，不必特意改变什么。"
            hide player_char_img
            $ hide_all_chars("servant_marta_img")
            show servant_marta_img at left with dissolve
            housekeeper "是，领主大人。"
            "她愣了一下，像是想再说什么，最终只是低着头退回了人群中。你注意到她的眼圈也是红的。"

        "询问父亲最后几天的情况":
            $ change_stat("reputation", 3)
            hide servant_marta_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "玛格丽特，父亲最后几天……可有什么异常？"
            "妇人犹豫了一下，压低了声音。"
            hide player_char_img
            $ hide_all_chars("servant_marta_img")
            show servant_marta_img at left with dissolve
            housekeeper "老领主临终前三天，不让任何人进入书房。连饭食都是放在门口的。"
            housekeeper "最后是奥尔德里克大人破门而入，才发现……"
            "她没有说下去，只是低下了头。"

        "直接让她退下":
            hide servant_marta_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "知道了。退下吧。"
            $ hide_all_chars()
            "妇人恭敬地退开。你没有多看她一眼——此刻你的心思全在别处。"

    ## --- 穿过走廊，路过父亲的画像 ---

    "你沿着石砌的走廊向大厅走去。走廊的墙壁上挂着历代领主的画像——你的曾祖父、祖父，以及……你的父亲。"

    "你在父亲的画像前停下了脚步。"

    "画中的父亲约莫三十多岁的样子，正值壮年。他身穿铠甲，佩剑立于城堡之前，目光如炬，嘴角微微上扬——那是一种胸有成竹的自信，一种掌控一切的从容。"

    "你已经快八年没有面对面和他好好说过话了。上一次，是你十四岁那年短暂的回家探亲。"

    "那几天他已经苍老得让你心惊——头发白了大半，咳嗽一声像要把肺咳出来。但你们都假装没注意到。在那间熟悉的书房里，你们聊了一个下午，又好像什么都没真正说出口。"

    "那次分别时，他没有告诉你'如果我不在了'。他大概以为自己还能等到你下一次回家。"

    "你以为他也会永远在这里。"

    menu:
        "在画像前默默站立片刻":
            "你站在画像前，一言不发。走廊里只有雨水顺着石墙渗下来的滴答声。"
            "你在心里说：'我回来了，父亲。但你已经不在了。'"
            "你深吸一口气，转身继续前行。你没有时间悲伤。"

        "向画像轻声许诺":
            $ change_stat("loyalty", 3)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我会守住艾登堡的，父亲。"
            $ hide_all_chars()
            "你的声音很轻，轻到只有画中的父亲和你自己能听见。"
            "画中的父亲依然微笑着，目光平静地注视着前方——注视着某个你看不见的远方。"

        "快步走过，不敢多看":
            "你加快了脚步，不敢在画像前停留太久。你怕自己一旦停下来，那些压抑在心底的东西就会决堤而出。"
            "现在不是崩溃的时候。"

    ## ============================================================
    ## 场景2：大厅会面
    ## ============================================================

label great_hall:

    $ play_music("audio/music/great_hall.ogg", fadein=2.0)
    $ set_mood("normal")
    scene bg great_hall with dissolve
    $ unlock_gallery("bg_great_hall")
    $ play_sound("audio/sfx/fire_crackle.ogg")

    "大厅中，壁炉的火光映照着墙上的家族旗帜——一只金色的鹰。"

    "这座大厅是艾登堡的心脏。高耸的穹顶上悬挂着铁制的枝形烛架，数十支蜡烛在气流中摇曳不定，将跳动的光影投射在灰色的石壁上。"

    "长条形的橡木桌上摆放着银质烛台和几只酒杯。空气中弥漫着壁炉松木的香气、蜡烛燃烧的微苦气息，以及一丝若有若无的潮湿霉味——城堡太老了，墙壁深处的湿气永远无法根除。"

    "两面墙上挂着织锦壁毯——一面描绘着先祖征战的场景，另一面是艾登堡丰收庆典的盛况。织锦的颜色已经褪去了大半，但依稀能辨认出金色、暗红和深蓝的图案。"

    "地板上铺着干草和香草——迷迭香和百里香，按照传统用来驱虫和净化空气。你的靴子踩上去，发出轻微的沙沙声。"

    $ play_sound("audio/sfx/crowd_murmur.ogg")
    "几位重要人物已经在此等候。"

    "他们站在大厅的不同位置——你注意到，每个人选择站立的地方都颇有讲究，仿佛各自划定了自己的领地。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    $ unlock_gallery("captain")

    "首先上前的是一个身材魁梧的年轻军官。他的铠甲擦得锃亮，腰间佩着一把长剑，步伐沉稳有力。他的脸上有一道浅浅的伤疤，从左眉斜过鼻梁——那是战场留给他的勋章。"

    captain "卫队长雷恩，向新任领主致敬！"

    "他单膝跪地，右拳捶胸，动作干脆利落，带着军人特有的刚直。"

    captain "城堡防务一切正常，领主大人。四十名卫兵随时听候调遣。"

    menu:
        "询问卫队的详细情况":
            $ change_rel("rel_captain", 5)
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "四十人？配备如何？日常训练情况怎样？"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "领主大人好眼光！四十人中，二十名重甲步兵，十名弓箭手，十名骑兵。每日操练两个时辰。"
            captain "不过……自老领主病倒后，军饷已经拖了两个月。弟兄们嘴上不说，但心里难免……"
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我知道了。军饷的事我会尽快解决。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "多谢领主大人！"
            $ change_rel("rel_captain", 5)

        "点头示意他起身":
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "起来吧，雷恩。以后不必行此大礼。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "是！"
            "他站起身来，比你高了整整半个头。但他的眼神中没有任何轻视，只有坦诚的尊敬。"

        "考验他——'如果现在有人攻城，你能守多久？'":
            $ change_stat("power", 3)
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "雷恩，假如此刻有人率两百人攻城，你能守多久？"
            "雷恩没有犹豫，脱口而出。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "城堡坚固，粮水充足，四十人守一个月不成问题。但——"
            captain "西塔屋顶上月塌了一块，如果敌人用火箭，那里是个隐患。而且弓箭储备不足，只够三天的量。"
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "很好。你很诚实。"
            "你暗暗点头。一个不粉饰太平的将领，比一百个报喜不报忧的人更有价值。"
            $ change_rel("rel_captain", 10)

    $ hide_all_chars()
    show bishop_img at left with dissolve
    $ unlock_gallery("bishop")

    $ hide_all_chars()
    "主教是一个体态圆润的中年人，穿着一身金色镶边的白色法袍。他的手指上戴着一枚硕大的紫水晶戒指，在烛光下闪烁着幽冷的光。"

    "他的笑容温和而得体，但你注意到他的眼睛——那双眼睛精明、冷静，与那张笑脸完全不搭调。"

    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "主教马修斯，代表圣母教会，向新任领主致以祝福。"

    $ bishop_met = True

    bishop "愿圣光庇护艾登堡，也庇护年轻的领主。"

    "他画了一个圣号，然后意味深长地看着你。"

    bishop "老领主生前是教会的虔诚信徒。他每月都会向教堂捐献十枚金币。我相信年轻的领主也会延续这一传统？"

    menu:
        "答应延续捐献":
            $ change_stat("faith", 12)
            $ change_rel("rel_bishop", 10)
            $ change_stat("wealth", -3)
            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "自然。父亲的虔诚，我会继承。"
            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "如此甚好。圣母会保佑领主大人的。"
            "主教满意地点了点头。你注意到他的笑容终于蔓延到了眼睛里。"

        "暂不表态":
            $ change_stat("intrigue", 3)
            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "等领地的账目理清之后，再行商议。"
            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "唔……也罢。领主大人初来乍到，想必诸事繁忙。"
            "他的笑容没有变，但指尖那枚紫水晶戒指转了一圈——一个不经意的小动作，却透露出些许不悦。"

        "委婉质疑——'教会为艾登堡做了什么？'":
            $ change_stat("power", 5)
            $ change_rel("rel_bishop", -5)
            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "主教大人，在我决定捐献之前，可否告诉我，教会为艾登堡的百姓做了些什么？"
            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "……"
            "主教的笑容冻结了一瞬。随即，他恢复了那副温和的面具。"
            $ hide_all_chars("bishop_img")
            show bishop_img angry at left with dissolve
            bishop "教会为艾登堡超度亡灵，安抚人心，在瘟疫时施粥救济，在饥荒时开仓放粮。教会做的事情，比领主大人想象的要多得多。"
            "他的语气平静，但每一个字都像是淬了毒的针。"
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve

    hide bishop_img with dissolve

    $ hide_all_chars()
    "一个身着朴素衣裙的年轻女子站在角落，向你微微欠身。"

    "她的位置选得很巧妙——远离壁炉的光亮，半隐在一根石柱的阴影中。如果不是刻意留意，你几乎会忽略她的存在。"

    "她穿着一件灰蓝色的棉裙，没有任何首饰，头发简单地束在脑后。但她的气质与那身朴素的装扮格格不入——她站立的姿态优雅而警觉，像一只随时准备起飞的隼。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "这位是艾琳娜，王后陛下派来协助领主大人的……侍从。"

    "奥尔德里克在'侍从'这个词上停顿了一拍。你捕捉到了他语气中极为细微的讽刺——或者说，警告。"

    hide aldric_img with dissolve
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    $ unlock_gallery("elena")

    elena "艾琳娜，拜见领主大人。王后陛下对老领主的离世深表痛惜。"

    "她的声音低沉而悦耳，像是深秋傍晚的大提琴。她的目光直视着你——不卑不亢，没有仆从应有的怯懦。"

    elena "陛下命我留在艾登堡，协助领主大人处理政务。"

    "你对王后派人来这件事怎么看？"

    menu:
        "表示感谢——欢迎她留下":
            $ change_rel("rel_elena", 10)
            $ change_rel("rel_queen", 5)
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "替我转达对王后陛下的谢意。艾琳娜，请不要拘束。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "领主大人客气了。"
            $ hide_all_chars()
            "她歪了下头，像是在打量一件有趣的东西。"
            "那种笑容像是在说'我知道你在想什么'，又像是在说'你不知道我在想什么'。"
            "无论如何，这个女人绝非普通的侍从。"

        "委婉拒绝——暗示不需要监视":
            $ change_stat("power", 5)
            $ change_rel("rel_queen", -5)
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "请转告王后陛下，艾登堡一切安好，不劳挂心。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "……领主大人误会了，我只是来帮忙的。"
            "她的语调没有一丝波澜，但你注意到她的右手指尖微微收紧了一下——极其短暂，如果你不是恰好在看她的手，绝不会察觉。"
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "领主大人，王后的好意，还是接受为好……"
            "奥尔德里克的语气中有一丝急切。王后的人，不是你想拒绝就能拒绝的。"
            hide aldric_img with dissolve

        "不动声色——先观察":
            $ change_stat("intrigue", 5)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "嗯，辛苦了。奥尔德里克，给她安排住处。"
            $ hide_all_chars()
            "你不动声色，但暗暗记下了这枚棋子。"
            "她的来意、她的能力、她的忠诚——这些问题的答案，你会慢慢找到。"
            "不急。在权力的游戏中，最先亮出底牌的人，往往最先出局。"

    hide elena_img with dissolve

    ## ============================================================
    ## 新增场景：探索父亲的寝室
    ## ============================================================

    "会面结束后，奥尔德里克引你去父亲的——现在是你的——寝室。"

    scene bg study with dissolve
    $ unlock_gallery("bg_study")
    $ play_sound("audio/sfx/fire_crackle.ogg")

    "寝室在城堡的东塔二层。推开沉重的橡木门，一股陈旧的气息扑面而来。"

    "房间里的一切都保持着父亲生前的样子——床上的毛毯叠得整整齐齐，窗台上放着一只铜烛台，书桌上摊开着一卷地图。"

    "床头柜上有一个木框的小像——那是你母亲的画像。她在你七岁时病逝，你对她的记忆已随岁月渐渐模糊。但父亲把这幅画像保留了二十年，每天入睡前想必都会看上一眼。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "老领主的遗物都在这里。还没有人动过。"

    aldric "领主大人可以慢慢整理。如果有什么需要，吩咐门口的侍卫便是。"

    "奥尔德里克欲言又止，最终只是深深鞠了一躬，退了出去。"

    hide aldric_img with dissolve

    $ hide_all_chars()
    "你独自一人，站在父亲曾经生活了三十年的房间里。"

    "你决定看看——"

    menu:
        "翻看书桌上的地图和文件":
            $ change_stat("reputation", 5)
            "你走到书桌前。那卷展开的地图上画的是艾登堡及周边领地的地形。"
            "地图上有几个位置被父亲用红墨水圈了出来——北方的铁矿、东面的渡口、以及西南方向森林深处的一个无名之地。"
            "无名之地旁边，父亲用细小的字迹写了三个字：'磨坊旧址'。"
            "磨坊？你不记得那个方向有什么磨坊。你将这个疑点记在心里。"

        "打开衣柜和箱子":
            "衣柜里挂着父亲的几件外袍——厚实的毛料，颜色深沉，没有任何花哨的装饰。这就是你记忆中的父亲——朴素、实际、不尚虚华。"
            "箱子里有一些个人物品：一枚旧勋章、一双磨损的皮手套、还有一把小刀。"
            "小刀的刀柄上刻着一朵花的图案——你仔细辨认，那似乎是一朵百合花。"
            "你把小刀收了起来。也许这只是一件普通的饰物，但你的直觉告诉你并非如此。"
            $ change_stat("intrigue", 3)
            $ collect_item("lily_symbol")

        "看看母亲的画像":
            "你拿起那幅小像，凑到烛光下。"
            "画中的女人很年轻，有一双温柔的棕色眼睛和一头栗色的卷发。她微微笑着，嘴角的弧度和你照镜子时看到的如出一辙。"
            "你突然意识到——你有母亲的嘴唇，父亲的眉眼。"
            "你把画像轻轻放回原处。这幅画是父亲留在这个世界上最温柔的东西。"

    "窗外，天色已经完全暗了下来。雨停了，但云层依然厚重，没有星光。"

    "远处的村庄亮起了零星的灯火，像是撒在黑色绒布上的萤火虫。"

    "你站在窗前，冰冷的空气扑面而来。"

    "从明天开始，这片土地上的每一个人的命运，都和你绑在了一起。"

    ## ============================================================
    ## 新增场景：晚宴
    ## ============================================================

    $ play_music("audio/music/great_hall.ogg", fadein=2.0)
    scene bg great_hall with dissolve
    $ unlock_gallery("bg_great_hall")
    $ play_sound("audio/sfx/crowd_murmur.ogg")

    "入夜时分，大厅中摆设了一场晚宴——不算盛大，但也足够正式。"

    "这是你作为新领主的第一顿正餐，也是所有重要人物第一次同时坐在一张桌子前。"

    $ play_sound("audio/sfx/fire_crackle.ogg")

    "壁炉中的火烧得正旺。橡木长桌上铺着白色的亚麻桌布，摆放着陶碗、锡杯和几盘简单的食物——烤鹿肉、黑面包、根菜浓汤和一壶温热的蜂蜜酒。"

    "不算丰盛，但在深秋的寒夜里，这些食物散发出的热气让人感到一丝慰藉。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    "奥尔德里克坐在你的左手边，不时低声为你介绍桌上的每一个人。"

    aldric "对面坐的是磨坊主格伦——他控制着领地里一半的粮食加工，是个精明的生意人。"

    aldric "角落那位是猎场管事老布鲁诺——他在森林里待了四十年，对每一条小路了如指掌。"

    aldric "靠门口的那两位是村长——北村的托马斯和南村的汉斯。他们代表领地内大部分的农民。"

    hide aldric_img with dissolve

    $ hide_all_chars()
    "你环顾桌旁的面孔。雷恩坐在你的右手边，笔直的腰背一如他的为人——端正、警惕。主教马修斯坐在桌尾，优雅地切着鹿肉，时不时与旁边的人交换几句低语。"

    "艾琳娜坐在一个不起眼的位置，安静地用餐。但你注意到她的目光一直在移动——她在观察每一个人。"

    "宴席的气氛微妙。表面上是客套的寒暄，但每个人说出的每一句话都经过了精心的权衡。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "领主大人，听说您在王都的骑术学得不错？"

    menu:
        "谦虚地回答":
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "略通皮毛罢了。修道院里学的是书本，比不上你们在马背上长大的人。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "领主大人谦虚了。"
            "雷恩举杯向你致意，脸上浮现出一丝善意的微笑。"

        "自信地回应":
            $ change_stat("power", 3)
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "在王都的骑术锦标赛中拿过第三名。不过，那是用笔和墨水拿的第三名——考的是骑术理论。"
            "桌上响起了一阵轻笑。连一向严肃的奥尔德里克嘴角也动了一下。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "有趣。看来我们得给领主大人安排一些实践课了。"
            $ change_rel("rel_captain", 5)

    hide captain_img with dissolve
    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve

    "主教擦了擦嘴，将目光转向你。"

    bishop "领主大人，我听闻王都近来政局有些……微妙。不知领主大人怎么看？"

    "这是一个陷阱。无论你怎么回答，你的话都会在明天变成传遍领地的流言。"

    menu:
        "打太极——'我只关心艾登堡'":
            $ change_stat("reputation", 5)
            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "王都的事离我们太远了。我只关心艾登堡的百姓能不能吃饱饭、睡安稳。"
            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "呵呵，领主大人年纪轻轻，却深谙明哲保身之道。"
            "你无法判断他这句话是赞美还是讽刺。也许两者兼有。"

        "坦率地谈论——'王后的处境不容易'":
            $ change_rel("rel_queen", 5)
            $ change_stat("loyalty", 3)
            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "年幼的国王、强势的贵族、虎视眈眈的邻国——王后陛下肩上的担子，比任何人都重。"
            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "哦？领主大人倒是很同情王后。"
            "主教的目光锐利了几分。你知道这句话会被记下来——他在评估你的立场。"

        "反问主教——'您的消息比我灵通多了'":
            $ change_stat("intrigue", 8)
            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "主教大人的消息渠道遍布王国，何必问我？倒是想请教您——王都最近发生了什么？"
            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "哈哈，领主大人高抬教会了。我们不过是侍奉圣母的清修之人，哪有什么消息渠道。"
            "他说这话时面不改色——你几乎要佩服他的演技了。"

    hide bishop_img with dissolve

    $ hide_all_chars()
    "晚宴持续了将近两个时辰。酒过三巡之后，人们的话匣子渐渐打开了。"

    "磨坊主格伦抱怨粮价太低，猎场管事老布鲁诺说森林里的猎物比去年少了一半，两个村长则你一言我一语地诉说着今年秋收不尽如人意。"

    "你默默听着，把每一条信息都记在心里。这些看似琐碎的抱怨，拼凑在一起就是艾登堡的全貌——一片表面平静、实则千疮百孔的领地。"

    "晚宴散去后，人们三三两两地离开了大厅。你注意到一个细节——"

    "主教和艾琳娜在走廊拐角处驻足交谈了几句。两人的表情都很平淡，交谈也只持续了很短的时间。但你的直觉告诉你，那几句话并不像表面看起来那么随意。"

    ## ============================================================
    ## 新增场景：夜晚独步城墙，与艾琳娜对话
    ## ============================================================

    $ set_mood("mystery")
    $ set_weather("clear", "light")
    $ play_music("audio/music/night_mystery.ogg", fadein=2.0)
    scene bg castle_exterior with dissolve

    "晚宴散去后，大厅里只剩下残烛和冷掉的食物。你没有回房，而是独自沿着石阶登上了城堡的南城墙。"

    "夜风清冽，带着旷野上枯草和泥土的气息。云层终于散开了一些，几颗黯淡的星星像是被遗忘的钉子，零零散散地钉在苍穹上。"

    "你双手撑在城垛上，俯瞰着脚下沉睡的领地。远处的村庄只剩下一两点灯火，像是大地睁着的、疲惫的眼睛。"

    "夜深了。明天还有更难的事等着你。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve

    player "我真的能做好吗……"

    $ hide_all_chars()
    "你喃喃自语。夜风把你的声音卷走了，没有人听见。"

    "——或者说，你以为没有人听见。"

    hide player_char_img with dissolve

    $ play_sound("audio/sfx/footstep.ogg")

    "身后传来极轻的脚步声。你转过头——"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve

    elena "领主大人也睡不着？"

    $ hide_all_chars()
    "艾琳娜披着一件深色的斗篷，站在几步之外。月色下，她的面容半明半暗，那双沉静的眼睛映着星光，像两面深不见底的古井。"

    "她走到你身旁，也将双手撑在城垛上，目光投向远方。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "我在王都的时候，常常在宫墙上看夜景。从高处看下去，一切都显得很小，很安静。好像世间的纷争和算计，都被黑暗吞没了。"

    elena "但那只是错觉。黑暗中发生的事情，往往比白天更多。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve

    player "你在暗示什么？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "没有暗示。只是……感慨。"

    "她转过头看着你。"

    elena "领主大人，恕我直言——今晚的宴席上，每一个人都在试探你。您注意到了吗？"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "主教的那番话，雷恩的客套，磨坊主的抱怨……我知道，每句话都有弦外之音。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "您看得比我预想的透彻。但还有一些您也许没有注意到的细节。"

    "她压低了声音，像是怕夜风把她的话送到不该听到的人耳中。"

    elena "今晚宴席上，磨坊主格伦三次看向主教——每次都是在主教说话之后。他们之间有某种默契，也许是利益上的往来。"

    elena "另外，两位村长——北村的托马斯和南村的汉斯——他们虽然坐在一起，但整晚没有交谈过一句话。这说明他们之间有矛盾，而且是那种不愿在外人面前暴露的深层矛盾。"

    menu:
        "感谢她的洞察，询问更多":
            $ change_rel("rel_elena", 10)
            $ change_stat("loyalty", 5)
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你的观察力让我印象深刻。还有什么是我该知道的？"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "领主大人愿意听，我愿意说。"
            "她的目光柔和了一些——那是一种被认可后的放松，虽然转瞬即逝。"
            elena "在这座城堡里，真正忠于您的人，也许比您以为的要少。但真正想害您的人，也没有那么多。大部分人只是在观望——看您是一块可以依靠的磐石，还是一堵随时会倒的墙。"
            elena "您需要做的，是在他们做出判断之前，先让他们看到您的分量。"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你说得对。谢谢你，艾琳娜。"
            "她微微侧头，嘴角弯出一个细微的弧度。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "不必谢我。我只是做我该做的事。"

        "保持警惕，反问她的立场":
            $ change_stat("intrigue", 8)
            $ change_rel("rel_elena", 3)
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你告诉我这些，是出于好意，还是另有目的？"
            "她没有生气，甚至没有露出意外的表情。她只是平静地回望着你。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "领主大人，如果我想欺骗你，就不会在夜里跑到城墙上来跟您说这些。我会在白天，当着所有人的面，说您最想听的话。"
            elena "我选择在只有您一个人的时候说真话——这本身就是答案。"
            "她的逻辑无懈可击，但你仍然无法完全信任她。也许这就对了——在这座城堡里，完全信任任何人都是危险的。"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我记住你的话了。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "那就够了。"

    "夜风忽然大了起来，将你们的斗篷吹得猎猎作响。远处的山脊上，一只夜枭发出了一声长鸣——凄凉而孤独。"

    elena "夜深了。领主大人早些歇息吧。明天……会很忙的。"

    $ hide_all_chars()
    "她最后看了你一眼，然后转身沿着城墙走去。她的身影在月光下越来越小，最终消融在塔楼的阴影中。"

    "你又独自站了一会儿。头顶的星空寂静无声，脚下的大地沉沉入眠。"

    "你把艾琳娜的话在心里翻来覆去地咀嚼了几遍。她说的每一句话都像是精心打磨过的——既有用，又不会泄露太多她自己的底牌。"

    "这个女人很危险。但也许正因为危险，才有价值。"

    hide player_char_img with dissolve
    hide elena_img with dissolve
    $ clear_weather()

    ## ============================================================
    ## 新增场景：巡视城防
    ## ============================================================

    scene bg castle_exterior with dissolve
    $ unlock_gallery("bg_castle_exterior")

    "你没有立即回房。沿着城墙继续走了几步，你决定顺便巡视一下城堡的防务。"

    "北风呼啸而过，带着松脂和冰雪的气息。你裹紧了斗篷，继续沿着城垛向前走去。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    "雷恩正在城墙上巡查。看到你时，他显然有些意外。"

    captain "领主大人？这么晚了还没歇息？"

    show player_char_img at right with dissolve

    player "睡不着。带我看看城堡的防务。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "遵命。"

    "雷恩陪着你沿城墙走了一圈。他指着不同的方向，为你讲解城堡的防御布局。"

    captain "城堡有四座塔楼——东塔、西塔、南塔和瞭望塔。每座塔楼常驻两名哨兵，四个时辰换一次班。"

    captain "北面的城墙最厚，有六尺，因为北方是最可能的进攻方向。南面和西面靠山，地形本身就是天然屏障。"

    captain "唯一的弱点是东面的水门——为了方便运输，水门的城墙只有三尺厚，而且常年浸泡在水中，石基有些松动。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "东面水门……如果有人从那里偷袭呢？"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "老领主在世时，我提过这个隐患。但老领主说——"

    "雷恩犹豫了一下。"

    captain "他说，'有些门，是故意留着的。'"

    menu:
        "追问这句话的含义":
            $ change_stat("reputation", 5)
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "故意留着？什么意思？"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "我也不明白。当时以为老领主另有深意，就没有再追问。"
            captain "现在想来……也许老领主需要一条不被注意的出入通道？"
            "父亲在城堡的防御上故意留下一个漏洞——这要么是失误，要么是刻意为之。而你的父亲，不是一个会犯这种失误的人。"

        "下令加固水门":
            $ change_stat("power", 5)
            $ change_stat("wealth", -3)
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "不管老领主有什么考量，现在我是领主。明天就安排工匠加固水门。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "是，领主大人！这正是我一直想做的！"
            "雷恩的嗓音提了半个调，身体微微前倾。你能感觉到，他对你的信任又多了一分。"
            $ change_rel("rel_captain", 5)

        "记在心里，暂不处理":
            $ change_stat("intrigue", 3)
            "你没有说什么，只是默默记下了这个信息。父亲留下的'门'，也许有它存在的理由。在搞清楚原因之前，你不打算轻举妄动。"

    captain "对了，领主大人。还有一件事——"

    captain "西塔的屋顶上个月塌了一块。我用木板做了临时修补，但如果入冬前不修好，整座塔楼可能都会出问题。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "需要多少钱？"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "大约五十枚银币的材料费，再加上工匠的工钱。"

    "你点了点头。又是一笔开支。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "雷恩，你跟随我父亲多久了？"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "五年。我十八岁那年投奔艾登堡，老领主收留了我，给了我一碗饭吃，又一步步把我提拔到卫队长的位置。"

    captain "老领主对我有知遇之恩。这份恩情，我会报在领主大人身上。"

    "他的话朴实而真诚。在这座充满算计的城堡里，这种直率反而显得珍贵。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "谢谢你，雷恩。回去休息吧，明天还有很多事要做。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "是。领主大人也早些歇息。"

    hide captain_img with dissolve
    hide player_char_img with dissolve

    $ hide_all_chars()
    "雷恩单手捶了一下胸甲，转身大步离去。铁靴踩在城墙石砖上，声响干脆利落，渐渐远去。"

    "你独自站在城墙上，俯瞰着沉睡中的领地。"

    "北风呼啸而过，将你的斗篷吹得猎猎作响。远处的山脊上，隐约可以看到一簇微弱的火光——那是边境哨所的篝火。"

    "你的视线向南移动——村庄、田野、教堂的尖顶、蜿蜒的河流……一切都安静地沉浸在夜色中。"

    "这就是你的领地。这就是你的责任。"

    "你转身走下城墙。"

    ## ============================================================
    ## 场景3：第一个夜晚 - 书房密谈
    ## ============================================================

label first_night:

    $ play_music("audio/music/night_mystery.ogg", fadein=2.0)
    $ set_mood("mystery")
    $ set_weather("fog", "light")
    scene bg study with dissolve
    $ unlock_gallery("bg_study")
    $ play_sound("audio/sfx/fire_crackle.ogg")

    $ trigger_random_event("rest")

    "夜深了。你独自坐在父亲的书房里，翻看着领地的账目和信件。"

    "书房的壁炉已经点了起来，但依然无法完全驱走深秋的寒意。烛火在桌上投下摇曳的光影，将你的影子拉长在身后的墙壁上——像是父亲的鬼魂在默默注视着你。"

    "桌上堆满了需要处理的文书——税收报告、军需清单、商路许可、土地纠纷……每一份文件都在提醒你，治理一片领地远比你在书本上读到的要复杂得多。"

    "艾登堡的状况比你想象的要复杂："

    "税收在下降，北方边境有盗匪出没，粮仓的储量只够撑过这个冬天。"

    "你仔细翻阅着账本。数字不会说谎——艾登堡的岁入在过去三年里持续减少。父亲似乎在生命的最后几年里，将大量的金钱花在了某些不明用途上。账目上只简单标注着'特别支出'，没有任何细目。"

    "而最让你不安的，是桌上一封未拆的密信——"

    "信封上只有一个符号：一把匕首刺穿一朵百合花。"

    "信封用黑色的火漆封印，火漆上压着同样的图案。你将信封凑近烛光——纸质上乘，不是普通人能用得起的。"

    "你要拆开这封信吗？"

    menu:
        "立刻拆开":
            $ log_decision("第一章", "拆开暗百合的神秘密信")
            $ change_stat("power", 5)
            "你撕开信封，借着烛光阅读：\n"
            "『新领主：你父亲的死并非天意。若想知道真相，满月之夜，独自来磨坊。勿带随从。——一个朋友』"
            "你的手微微发抖。"
            "信纸上的墨迹已经干透了——这封信至少写于一周之前，也就是说，在你尚未回到艾登堡的时候，就已经有人预见到了你的到来。"
            "这个'朋友'知道你会回来，知道你会坐在这张书桌前，知道你会拆开这封信。"
            "你将信纸折好，贴身收起。磨坊——你想起了地图上那个标注着'磨坊旧址'的位置。"
            $ father_death_known = True
            $ dark_lily_exists_known = True

        "先不拆，找奥尔德里克来看":
            $ log_decision("第一章", "将密信交给奥尔德里克")
            $ change_rel("rel_aldric", 5)
            "你决定谨慎行事，派人请来奥尔德里克。"
            "片刻之后，老骑士推门而入。他显然还没有入睡——身上的衣服整整齐齐，仿佛一直在等你的召唤。"
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "这个符号……老臣见过。这是'暗百合'的标记，一个活跃在几个领地间的秘密组织。"
            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "暗百合？什么样的组织？"
            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "说实话，老臣也不十分清楚。只知道他们行事隐秘，成员遍布各地，上至贵族，下至农夫，谁也不知道身边的人是不是暗百合的人。"
            aldric "老领主生前曾多次收到他们的信。不过……老领主从未告诉老臣信的内容。"
            aldric "每次收到信后，老领主都会独自在书房待很久。有几次，老臣看到他拆完信后……脸色很难看。"
            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你觉得父亲的死和暗百合有关系吗？"
            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "老臣不敢妄言。但……"
            "奥尔德里克的目光落在墙上那幅旧地图上，好像在看另一个时代。"
            aldric "老领主临终前，握着老臣的手说了一句话——'告诉我的孩子，不要相信表面上的真相。'"
            "你的心猛然一紧。梦中父亲那未说完的话——'不要……相信……'"
            hide aldric_img with dissolve
            $ father_death_known = True
            $ dark_lily_exists_known = True

        "烧掉它——不想卷入阴谋":
            $ log_decision("第一章", "烧毁密信，不愿卷入阴谋")
            $ change_stat("power", 5)
            $ hide_all_chars()
            "你将信扔进壁炉。火焰瞬间吞噬了那张羊皮纸。"
            "黑色的火漆在火中融化，散发出一股刺鼻的气味。百合花的图案在火焰中扭曲、变形，最终化为一缕青烟。"
            "不管是什么人在玩什么把戏，你不打算按别人的剧本走。"
            "你是艾登堡的领主，不是任何人的棋子。"
            "但你不知道的是，有人正透过书房门缝，注视着你的一举一动。"
            "那道目光在你烧掉信件的瞬间，微微缩了一下——然后影子从门缝底下悄无声息地抽走了。"

    ## ═══ 阴谋危机事件：密信中的陷阱 ═══
    "就在你处理完密信的瞬间，一阵微弱的脚步声从门外传来。"

    "你抬头望去——走廊的烛火不知何时熄灭了几盏，黑暗正缓慢地朝书房蔓延。"

    "你的后颈汗毛竖了起来。这封信……也许不只是一封信，更是一个试探——有人在观察你的反应。"

    "如果你不能正确应对，这个'观察者'可能会成为真正的威胁。"

    $ trigger_crisis("intrigue", 4, "有人在暗中窥探你对密信的反应。你能否识破这场阴谋，反将对方一军？", "crisis_intrigue_letter_win", "crisis_intrigue_letter_lose")
    call crisis_encounter from _call_crisis_encounter

    ## 退缩的情况 — 直接继续
    "你决定暂时不去理会那种被窥视的感觉，继续翻阅其他文件。"
    jump after_letter_crisis

label crisis_intrigue_letter_win:

    scene bg study with dissolve
    $ log_decision("第一章", "识破密信陷阱")
    $ change_stat("intrigue", 10)
    $ change_courage(25)
    "你故意在桌上留下了一封伪造的回信，假装要赴约。"

    "然后悄悄从侧门绕出，在走廊的暗处等待。"

    "果然——一个身影像猫一样无声地靠近书房门，伸手去拿你留下的信件。"

    "你没有打草惊蛇，只是默默记住了那人的轮廓。太矮，不是骑士或男爵的人。太安静，不是普通侍从。"

    "这个人……来自暗百合。"

    $ dark_lily_exists_known = True

    "你回到书房，心中多了一份警觉，也多了一份信心——至少现在，暗处的人不知道你已经察觉了他们。"
    jump after_letter_crisis

label crisis_intrigue_letter_lose:

    scene bg study with dissolve
    $ log_decision("第一章", "密信陷阱中失算")
    $ change_stat("intrigue", -5)
    "你试图设下陷阱，但对方显然比你更老练。"

    "当你绕到走廊时，那里空无一人——只有一根已经熄灭的蜡烛还冒着余烟。"

    "你察觉到脖颈一凉，回头看去，书桌上你刚才放下的那封信……不见了。"

    "有人就在你离开的那几秒钟内，悄无声息地取走了信件。"

    "更可怕的是，你桌上的其他文件被翻动过了——那个人不仅拿走了暗百合的信，还看了你的账本和税收报告。"

    "一阵寒意从脊椎爬上后脑勺。你在这盘棋局中，暂时落了下风。"
    jump after_letter_crisis

label after_letter_crisis:

    scene bg study with dissolve
    "你继续翻阅桌上的文件。在一叠积压已久的信件中，你找到了几封有意思的东西——"

    "一封来自南方商人的信，提议开辟新的贸易路线，愿意预付一笔定金。"

    "一封来自邻近小领主的信，试探性地询问联姻的可能。"

    "还有一封没有署名的短信，只有一句话——'磨坊里的老鼠越来越多了。'"

    "你不确定这些信件中哪些是真正的机会，哪些是精心设计的陷阱。"

    "你揉了揉酸涩的眼睛。烛火已经矮了一大截，窗外的夜色浓得像墨汁。"

    "最终，疲惫战胜了警觉。你趴在书桌上，沉沉睡去。"

    ## ============================================================
    ## 新增场景：晨间议事
    ## ============================================================

    $ play_music("audio/music/castle_calm.ogg", fadein=2.0)
    $ set_mood("normal")
    $ set_weather("overcast", "light")
    scene bg great_hall with dissolve

    "清晨。灰白的天光从大厅的窄窗中透进来，将石壁上的家族旗帜照得黯淡无光。"

    "你被仆人叫醒时，脖子僵硬，半边脸上印着账本的纹路。你匆匆洗了把脸，换上一件干净的外袍，走进了大厅。"

    "这是你主持的第一次正式晨议。奥尔德里克、雷恩和艾琳娜已经在厅中等候。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "领主大人，早安。昨夜可休息好了？"

    show player_char_img at right with dissolve

    player "还过得去。说正事吧。"

    "你不想让他们看出你其实一夜没睡好。在这些人面前，任何弱点都可能被记住——甚至被利用。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "是。老臣先说领地内务——"

    aldric "秋收已经结束，但产量比去年少了两成。原因有三：其一，春季霜冻损毁了部分麦田；其二，灌溉渠年久失修，有三处决口未补；其三……"

    "老骑士顿了顿，声音低了下去。"

    aldric "其三，有些佃农在老领主病重期间离开了领地。他们不确定新领主会不会提高赋税，所以选择了逃避。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "逃了多少人？"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "约莫三十户。不算多，但如果消息继续传开，明年春耕的人手会不够。"

    hide aldric_img with dissolve
    hide player_char_img with dissolve
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "领主大人，末将来报军务。"

    "雷恩的汇报简洁利落，像他的刀法一样干脆。"

    captain "北方边境哨所传来的最新消息——冯·哈根男爵的领地近日异常活跃。大量马车从南方驶入他的城堡，看起来像是在囤积物资。"

    captain "另外，他的骑兵巡逻队比平时多了一倍，而且巡逻范围明显向我们的边境推移了。"

    show player_char_img at right with dissolve

    player "你的判断呢？"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "依末将看——他在做战争准备。囤物资、增巡逻、压边境，这是进攻前的标准动作。"

    captain "但有一点让我吃不准——他的步兵没有动。如果真要打仗，步兵应该最先集结才对。"

    hide captain_img with dissolve
    hide player_char_img with dissolve
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve

    elena "如果我可以补充一点——"

    "艾琳娜从角落里开口。她的声音不大，但大厅里的人都安静了下来。"

    elena "男爵此人，贪婪但不鲁莽。他不会在没有把握的情况下发动全面进攻。他目前做的，更像是一种姿态——用军事压力来试探新领主的底线。"

    elena "换句话说，他想看您会不会被吓住。如果您示弱，他就会得寸进尺；如果您强硬回应，他会暂时退缩，然后换一种方式来蚕食您的利益。"

    elena "真正危险的不是他的军队，而是他的耐心。这个人擅长打持久战——他会一点一点地削弱你，直到你自己崩溃。"

    hide elena_img with dissolve

    $ hide_all_chars()
    "三个人给出了三种视角——内政、军事、情报。拼在一起，就是艾登堡此刻面临的全貌：内有困境，外有强敌，而你只有一副刚刚摸到的牌。"

    "你靠在椅背上，手指交叉抵在下巴上。大厅里安静了片刻——所有人都在等你的回应。"

    menu:
        "以攻为守——'我们不能被动挨打'":
            $ change_stat("power", 5)
            $ change_stat("loyalty", 3)
            $ log_decision("第一章", "晨议立场: 主动出击")
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "被动等待不是我的风格。与其让男爵牵着鼻子走，不如我们先出牌。"
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "领主大人的意思是……主动出击？"
            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "不一定是军事上的出击。外交、贸易、情报——任何能打乱他节奏的手段都可以。让他知道，艾登堡的新领主不是一头待宰的羔羊。"
            "奥尔德里克点了点头，多倒了一杯酒推到你面前。雷恩的手不自觉地按上了剑柄——那是军人听到好消息时的本能反应。"
            hide aldric_img with dissolve

        "先稳内政——'攘外必先安内'":
            $ change_stat("loyalty", 5)
            $ change_stat("wealth", 18)
            $ log_decision("第一章", "晨议立场: 优先内政")
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "男爵的威胁是真实的，但我们自己的问题更紧迫。佃农流失、粮食减产、城堡失修——这些才是根基。"
            player "一座从内部腐烂的城堡，即使有再高的城墙也守不住。"
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "领主大人所言极是。老领主晚年也常说，治国如治病，内疾不除，外邪必侵。"
            "艾琳娜微微颔首。你注意到她的目光中多了一分你之前没见过的东西——也许是认同，也许是重新评估。"
            hide aldric_img with dissolve

        "静观其变——'让子弹再飞一会儿'":
            $ change_stat("intrigue", 8)
            $ log_decision("第一章", "晨议立场: 静观其变")
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "情报不够充分，判断不能下得太早。继续监视男爵的动向，同时不要暴露我们的意图。"
            player "在棋局中，最后一个落子的人，往往能看到最多的局势。"
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "领主大人的耐心……让我想起了王后陛下。她也是一个善于等待的人。"
            "你不知道这是恭维还是试探。但你选择把它当作恭维。"
            hide elena_img with dissolve

    $ hide_all_chars()
    "晨议结束，众人各自散去。阳光依然没有穿透云层——天空低沉，像是压在艾登堡上方的一块灰色铅板。"

    "你回到书房，继续整理昨夜未看完的文件。"

    scene bg study with dissolve
    $ play_sound("audio/sfx/fire_crackle.ogg")

    "午后的阳光终于从云缝中挤出来一线，在书桌上投下一道窄窄的光带。你正埋头翻阅一份陈旧的土地契约——"

    $ play_sound("audio/sfx/door_knock.ogg")
    "突然，门外传来急促的敲门声。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "领主大人，卫队长雷恩求见。有急报。"

    "你从椅子上站起来。雷恩的脸上写满了紧张——你还从未见过他这个表情。"

    show player_char_img at right with dissolve

    player "进来说。"

    "雷恩快步走到桌前，压低了声音。"

    ## ============================================================
    ## 场景4：第一个危机
    ## ============================================================

label first_crisis:

    scene bg study with dissolve

    $ play_music("audio/music/tension.ogg", fadein=1.0)
    $ set_mood("tense")

    "你立刻让雷恩去请奥尔德里克。同时派人到北方哨所催要详报。"

    "等老骑士赶到、斥候的第二封快马也送达时，窗外的天色已经完全暗了下来。"

    "你点起烛台，三人围坐在书桌旁。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "领主大人，北方边境的哨所传来消息——"

    captain "冯·哈根男爵的军队在我们的边境集结了约两百人。"

    captain "他们打着'护送吊唁使团'的旗号，但那阵仗……不像是来吊丧的。"

    $ hide_all_chars()
    "两百人。你的卫队只有四十人。"

    "你感到胃部一阵收紧。这是你作为领主面对的第一个威胁——而它来得比你预想的要快得多。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "哨所的斥候说，他们扎了大营，支起了攻城用的帐篷。如果只是吊唁，根本不需要这种阵仗。"

    captain "而且，他们的骑兵已经在我们的边境线上巡弋了。就差一步就踏入我们的领地了。"

    hide captain_img with dissolve
    hide player_char_img with dissolve
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "冯·哈根这条老狐狸……他觊觎我们的铁矿已经很久了。"

    aldric "老领主在时，他不敢轻举妄动。现在换了新领主，他大概想试探一下。"

    aldric "冯·哈根此人，贪婪而狡猾。他不会真的进攻——代价太高。但如果我们不做出回应，他就会得寸进尺。"

    aldric "今天是两百人'吊唁'，明天就可能是五百人'做客'。"

    hide aldric_img with dissolve

    $ hide_all_chars()
    "你的拳头在桌子底下攥紧了。第一晚。才到艾登堡的第一晚，你就要面对这样的局面。"

    "你看了一眼窗外的夜空。云层终于散开了一角，露出几颗冷清的星光。"

    "你深吸一口气。不能慌。你在王都读过的那些兵法和策论，现在是时候派上用场了。"

    call autosave_before_choice from _call_autosave_before_choice

    "这是你作为领主面对的第一个考验。你决定——"

    $ mark_important_choice()
    menu:
        "外交手段：派使者去谈判，表示愿意商议铁矿合作|声望+ 谋略+":
            jump crisis_diplomacy

        "示强：集结全部兵力到边境，做出备战姿态|权力+ 财富-":
            jump crisis_military

        "求助教会：请主教出面调停|信仰+ 欠教会人情":
            jump crisis_church

        "暗中行动：派人潜入男爵领地打探虚实|谋略+ 有风险":
            jump crisis_spy

    ## ---- 外交路线 ----
label crisis_diplomacy:

    scene bg great_hall with dissolve
    $ log_decision("第一章", "选择外交手段化解边境危机")
    $ change_stat("wealth", -5)
    $ change_stat("reputation", 10)
    $ change_rel("rel_baron", 15)

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    show player_char_img at right with dissolve
    player "准备一份礼物，派我们最好的使者去。告诉男爵，铁矿的事可以谈。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "领主大人英明。以退为进，不失为上策。"

    $ hide_all_chars()
    "你花了一个时辰斟酌使者带去的信件。每一个字、每一个措辞都经过了反复推敲——既要表达诚意，又不能露出软弱。"

    "你在信中写道：'尊敬的冯·哈根男爵阁下：承蒙阁下遣使吊唁，本领主不胜感激。先父在世时常言，与邻为善乃治国之本。艾登堡的铁矿产出丰富，然独享不如共利。本领主愿与阁下坦诚商议合作之事，以期两地共荣。'"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "好文笔。有理有节，不卑不亢。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "礼物方面，挑一匹好马和两坛陈年蜂蜜酒。不要太贵——太贵了反而像是在示弱。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "明白。老臣这就去安排。"

    hide aldric_img with dissolve
    hide player_char_img with dissolve

    "三天后，使者带回了男爵的回信。"

    $ hide_all_chars("baron_img")
    show baron_img at left with dissolve
    $ unlock_gallery("baron")

    baron "（信件）年轻的领主，你的诚意让我刮目相看。"
    baron "我愿意撤回军队，但有一个条件——在下月的领主会议上，我希望与你当面详谈。"

    $ hide_all_chars()
    "你读着信上那苍劲有力的字迹，把信纸折好放在桌上，手指在上面弹了一下。男爵的口气是居高临下的——他仍然把你当成一个可以摆布的年轻人。"

    "但他同意撤军了。这就够了。"

    hide baron_img with dissolve

    "军队撤了。但你知道，这只是暂时的。"

    "男爵想要的不只是铁矿。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "领主大人，此次危机虽然化解，但男爵的狼子野心不会就此罢休。"
    aldric "下月的领主会议上，他必然会狮子大开口。我们需要提前准备。"
    show player_char_img at right with dissolve
    player "我知道。外交争的不是一朝一夕，而是长远的势。"
    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "老领主……也是这么说的。"
    "老人的目光中闪过一丝欣慰，随即隐没在那张刻满皱纹的脸后面。"
    hide aldric_img with dissolve
    hide player_char_img with dissolve

    $ unlock_achievement("diplomat")

    jump first_decree

    ## ---- 军事路线 ----
label crisis_military:

    scene bg castle_armory with dissolve
    $ log_decision("第一章", "选择以武力示强")
    $ change_stat("power", 15)
    $ change_stat("loyalty", 10)
    $ change_stat("wealth", -10)
    $ change_rel("rel_baron", -20)

    $ play_music("audio/music/battle_prepare.ogg", fadein=1.0)
    $ set_mood("battle")

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    show player_char_img at right with dissolve
    player "雷恩，全军备战。把所有能拿起武器的人都召集起来。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "是！领主大人！"

    "雷恩的眼中燃起了一团火。你看得出，这个军人等这道命令已经等了很久。"

    $ hide_all_chars("captain_img")
    show captain_img happy at left with dissolve

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "另外，派人去北村和南村征召青壮农民。发给他们长矛和盾牌——质量不重要，数量要多。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "领主大人的意思是——"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "人数上我们拼不过他。但我们要让他知道，攻打艾登堡的代价，远比他想象的高。"

    hide captain_img with dissolve
    hide player_char_img with dissolve

    scene bg border with dissolve
    $ unlock_gallery("bg_border")

    "你征召了城堡附近的青壮农民，凑出了一百二十人的队伍。"

    "虽然装备简陋，但你亲自骑马到边境列阵，做出了不退缩的姿态。"

    "这是你第一次骑马上阵。冰冷的风灌进甲缝，手心攥着缰绳的地方出了一层薄汗。但你挺直了腰背，让自己看起来比实际感受到的要镇定得多。"

    "你命令士兵在边境点起篝火——数量是实际营帐的三倍。远远望去，火光连成一片，仿佛有一支庞大的军队驻扎在此。"

    ## ═══ 战斗危机事件：边境夜袭 ═══
    "对峙第一夜。你在营帐中审阅地图，突然帐外传来一阵骚动。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "领主大人！男爵派了一支精锐小队趁夜偷袭我们的左翼！"

    show player_char_img at right with dissolve

    player "多少人？"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "大约三十人，都是老兵。我们的农兵挡不住！"

    "你握紧了腰间的剑。这是一个关键时刻——如果你亲自带队反击，可以大幅提振士气。但也意味着将自己置于真正的危险之中。"

    hide captain_img with dissolve
    hide player_char_img with dissolve

    $ trigger_crisis("combat", 5, "男爵的精锐夜袭边境营地！你必须亲自带队反击，击退来犯之敌。", "crisis_combat_border_win", "crisis_combat_border_lose", courage_cost=25, courage_gain=15)
    call crisis_encounter from _call_crisis_encounter_1

    ## 退缩的情况
    $ hide_all_chars()
    "你命令雷恩自行处理夜袭，自己留在营帐中指挥全局。"
    "雷恩虽然勉强击退了敌人，但损失不小。士兵们私下议论着领主的勇气。"
    $ change_stat("loyalty", -5)
    $ change_courage(-5)
    jump after_border_crisis

label crisis_combat_border_win:

    scene bg border_night with dissolve
    $ log_decision("第一章", "亲自击退边境夜袭")
    $ change_stat("power", 10)
    $ change_stat("reputation", 10)
    $ change_courage(25)
    $ change_rel("rel_captain", 15)

    "你拔剑冲出营帐，在月光下大喊：'艾登堡的人，随我来！'"

    "也许是你的声音里带着某种不容置疑的力量，也许是士兵们终于等到了一个愿意与他们并肩作战的领主——农兵们举起了长矛，发出了一声呐喊。"

    "战斗很短。男爵的精锐没想到你会亲自出战，更没想到这些农兵在领主带领下会爆发出如此凶悍的战意。"

    "你在混战中砍翻了一个敌兵——这是你第一次真正意义上的杀人。热血溅在你的面颊上，腥甜的气味让你反胃，但你咬牙稳住了身形。"

    $ hide_all_chars("captain_img")
    show captain_img happy at left with dissolve
    captain "领主大人……您竟然亲自……"
    show player_char_img at right with dissolve
    player "一个连剑都不敢拔的领主，凭什么让别人为他卖命？"
    "雷恩的眼眶有些泛红。他单膝跪下，将沾血的剑横在胸前。"
    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "雷恩誓死追随领主大人！"
    hide captain_img with dissolve
    hide player_char_img with dissolve
    jump after_border_crisis

label crisis_combat_border_lose:

    scene bg border_night with dissolve
    $ log_decision("第一章", "边境夜袭中负伤")
    $ change_stat("power", -5)
    $ change_stat("loyalty", 5)

    "你拔剑冲出营帐，但黑暗中的战斗远比你想象的混乱。"

    "你看不清敌友，只能凭着喊杀声判断方向。一柄刀从侧面劈来——你勉强格挡，但力量的差距让你踉跄后退。"

    "要不是雷恩及时赶到挡住了那致命一击，你可能已经倒在了边境的泥地里。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "领主大人！您受伤了！快退到后方！"
    $ hide_all_chars()
    "你咬着牙，在雷恩的掩护下退回营帐。血从手臂上的伤口渗出，浸透了衬衣。"
    "虽然你的冲锋没能改变战局，但士兵们看到了你的勇气——一个敢流血的领主，至少值得追随。"
    hide captain_img with dissolve
    $ change_rel("rel_captain", 5)
    jump after_border_crisis

label after_border_crisis:

    scene bg border with dissolve

    "对峙又持续了一天。最终，男爵的军队悄然撤退。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "他们走了！领主大人，您赢了！"

    $ play_music("audio/music/victory.ogg", fadein=1.0)
    $ hide_all_chars()
    "士兵们欢呼起来。但奥尔德里克的脸上没有笑容。"

    "农民们把长矛往地上一扔，用粗糙的嗓门高喊着你的名字。一个满脸泥土的壮汉甚至跪在地上朝你磕头——也许他真的觉得你是一位英勇的领主，也许他只是庆幸自己不用死在边境上。"

    hide captain_img with dissolve
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    $ hide_all_chars("aldric_img")
    show aldric_img sad at left with dissolve

    aldric "领主大人，我们赢了面子，但也结了仇。男爵不会忘记这次的屈辱。"

    aldric "而且，征召农民打乱了秋收的节奏。有些田地的庄稼来不及收割，会影响冬天的粮食储备。"

    show player_char_img at right with dissolve

    player "这些我都知道。但有些时候，展示力量比保存实力更重要。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "……也许吧。但愿领主大人是对的。"

    hide aldric_img with dissolve
    hide player_char_img with dissolve

    $ unlock_achievement("warrior")

    jump first_decree

    ## ---- 教会路线 ----
label crisis_church:

    scene bg church_interior with dissolve
    $ log_decision("第一章", "寻求教会帮助")
    $ change_stat("faith", 20)
    $ change_rel("rel_bishop", 20)
    $ change_stat("power", -5)

    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve

    player "主教大人，教会能否出面调停此事？"

    hide player_char_img
    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "领主大人信赖教会，教会自然不会坐视不理。"

    "主教的笑容变得更加温和了——那种商人看到大主顾上门时的温和。"

    bishop "我会以圣母之名，要求男爵在新领主的丧期内保持克制。"

    bishop "教会的话语在这片土地上依然有分量——只要人们还敬畏圣母，就没有人敢公然违抗教会的调停。"

    bishop "当然……教会的帮助也不是无偿的。艾登堡的什一税，是不是该提高一些了？"

    "他的话说得不紧不慢，语气温和得像是在讨论天气。但你很清楚——这是一笔交易。救火可以，但要收费。"

    menu:
        "答应提高什一税":
            $ change_stat("faith", 15)
            $ change_rel("rel_bishop", 10)
            $ change_stat("wealth", -15)
            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "教会的慈悲，理应得到回报。"
            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "领主大人果然虔诚。放心，有教会在，无人敢犯艾登堡。"
            $ hide_all_chars()
            "主教双手合十，做出一副感恩戴德的姿态。但他的眼睛在笑——那是赢家的笑。"
            "你不知道这笔账日后会不会让你后悔。但此刻，你需要教会的力量。"

        "拒绝加税，但承诺修缮教堂":
            $ change_stat("wealth", -5)
            $ change_rel("rel_bishop", 5)
            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "什一税关系到百姓生计，不宜轻动。但教堂的修缮，我来负责。"
            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "唔……也算是诚意吧。好，我会去信给男爵的。"
            "主教的笑容淡了几分，但没有翻脸。你给了他面子，没给他里子——不满意，可也翻不了桌。"
            hide bishop_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "另外，主教大人，如果教堂需要新的祭坛装饰，也可以告诉我。"
            "你额外给了一个甜头。在谈判中，关键不在于给多少，而在于让对方觉得自己赚了。"
            hide player_char_img
            $ hide_all_chars("bishop_img")
            show bishop_img at left with dissolve
            bishop "领主大人有心了。圣母一定会庇佑你的。"

    hide bishop_img with dissolve
    hide player_char_img with dissolve

    $ play_sound("audio/sfx/bell_toll.ogg")
    $ hide_all_chars()
    "三天后，男爵撤军了。教会的面子，他还是要给的。"

    "据说主教写给男爵的信措辞极为严厉——以逐出教会相威胁。对于一个还需要教会为他的统治背书的男爵来说，这个代价太大了。"

    "但你在教会面前，欠下了一个人情。"

    "在这个世界上，人情债是最贵的。"

    $ unlock_achievement("holy_man")

    jump first_decree

    ## ---- 间谍路线 ----
label crisis_spy:

    scene bg study with dissolve
    $ log_decision("第一章", "选择暗中行动")
    $ change_stat("intrigue", 5)
    $ change_rel("rel_elena", 10)

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve

    player "我需要先弄清楚男爵的真实意图。"

    $ hide_all_chars()
    "你按住了想要立刻行动的冲动。两百人对四十人——硬碰硬是不智之举。外交谈判需要时间。求助教会则要付出代价。"

    "但如果能摸清男爵的底牌，一切就不一样了。"

    "你正在思考要派谁去时——"

    hide player_char_img with dissolve
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve

    elena "领主大人，恕我冒昧。"

    "你转过头。艾琳娜不知何时出现在书房门口——你甚至没有听到她的脚步声。这个女人走路像猫一样无声。"

    elena "我在男爵的领地有一些……故旧。如果领主大人信任我，三天之内，我能带回消息。"

    "她的目光平静而坦然——没有讨好，没有邀功，只是在陈述一个事实。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve

    player "你是王后派来的人。你怎么会在男爵的领地有故旧？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "领主大人聪明。正因为我是王后的人，所以各地都有我的……故旧。"

    "她没有解释更多。但这个回答本身就说明了很多——她不是一个普通的侍从，她是一张遍布王国的情报网的一部分。"

    menu:
        "信任她，让她去":
            $ log_decision("第一章", "信任艾琳娜建立间谍网络")
            $ change_rel("rel_elena", 15)
            $ change_stat("loyalty", 5)
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "去吧。小心行事。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "领主大人放心。"
            $ hide_all_chars()
            "她点了下头，什么都没多说，转身走了。斗篷角刮过门框，然后走廊又安静了下来。"
            "你看着她离去的方向，心中泛起复杂的情绪——你在信任一个你还不了解的人。但有时候，下注本身就是一种智慧。"
            hide elena_img with dissolve
            "三天后，艾琳娜带回了惊人的消息。"
            "她的衣裙上沾着泥土和草叶，但精神奕奕，眼中闪烁着完成任务的满足。"
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "男爵的军队其实只有八十人，其余是雇来充数的农民。"
            elena "他们的装备参差不齐——正规军有铠甲和长矛，但雇来的农民只有木棍和皮甲。列阵的时候把正规军放在前排，远远看去好像有两百精兵。"
            elena "而且……他的军费是向犹太商人借的高利贷。他撑不了多久。"
            elena "另外，他的小儿子最近在王都惹了麻烦，正需要一个有力的盟友。"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "好。非常好。"
            $ hide_all_chars()
            "你靠在椅背上，脑中快速盘算。男爵虚张声势，实力不足，财力枯竭，而且还有一个急需解决的家务事。这些弱点，每一个都可以利用。"
            "有了这些情报，你从容地派出使者，不卑不亢地提出了条件。"
            "男爵很快就撤了军。他不知道你是怎么摸清他底牌的。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "领主大人。"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "嗯？"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "情报的价值在于它的时效性。我建议您在男爵的领地保持长期的情报来源。如果您允许的话。"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你的意思是……建立一个间谍网？"
            $ hide_all_chars("elena_img")
            show elena_img happy at left with dissolve
            elena "我们称之为'消息渠道'。听起来更文雅一些。"
            "她第一次露出了真正的笑容——不是客套，不是敷衍，而是一种志同道合者之间的默契。"
            $ spy_network = True
            $ unlock_achievement("spy_master_ch1")

        "不信任，自己派人":
            $ log_decision("第一章", "拒绝艾琳娜，自行派人")
            $ change_rel("rel_elena", -10)
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "不必了。雷恩，挑两个机灵的士兵，便装潜入男爵领地侦察。"
            "艾琳娜的表情没有变化，但你注意到她的肩膀微微下沉了一寸——也许是失望，也许只是松了口气。"
            hide elena_img with dissolve
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "是，领主大人。"
            hide captain_img with dissolve
            $ hide_all_chars()
            "五天后，侦察兵带回了一些有用的消息，但不如预期详尽。"
            "男爵的军队确实是在虚张声势，但更多细节无从得知。"
            "士兵不是间谍——他们能看到营帐的数量，但看不到男爵书桌上的账本。"
            "你根据有限的情报做出了应对，男爵最终撤军了。"
            "但你总觉得少了一些什么。也许你拒绝艾琳娜，错过了一个机会。"
            "也许你做了正确的选择。谁知道呢。"

    hide elena_img with dissolve
    hide player_char_img with dissolve

    jump first_decree

    ## ============================================================
    ## 场景5：第一道政令
    ## ============================================================

label first_decree:

    $ clear_weather()
    $ play_music("audio/music/castle_calm.ogg", fadein=2.0)
    scene bg great_hall with dissolve
    $ unlock_gallery("bg_great_hall")

    $ trigger_random_event("rest")

    "危机暂时解除。但更多的麻烦已经在路上了——税收亏空、北境不稳、王都的目光正朝这边转来。"

    "在处理边境危机的这几天里，你几乎没有合过眼。疲惫像铅一样沉淀在你的骨头里，但你不能休息——至少现在不行。"

    "你在大厅中召集了所有重要人物。这一次，不是晚宴，而是正式的领主议事。"

    "作为新领主，你需要颁布第一道政令，向所有人宣示你的治国理念。"

    "你坐在大厅尽头那把高背的橡木椅上——领主之座。椅子的扶手上磨出了两道光滑的痕迹，那是你父亲三十年来的手印。你的手掌放上去，微凉。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "领主大人，领地目前有几件紧要之事，您打算先处理哪一件？"

    "老骑士从袖中取出一份清单，逐一念给你听。"

    aldric "第一，北方边境的防务需要加强，以防男爵再来。"

    aldric "第二，粮仓储量不足，需要想办法筹粮过冬。"

    aldric "第三，领地内的盗匪越来越猖獗，商队频频遇劫。"

    aldric "第四，城堡年久失修，上个月西塔的屋顶还塌了一块。"

    $ hide_all_chars()
    "他放下清单，目光殷切地看着你。你知道他有自己的倾向，但他克制住了——这个决定必须由你来做。"

    "大厅里其他人也都看着你。雷恩攥着剑柄，目光灼灼；主教双手交叠在胸前，嘴角含着一丝深不可测的微笑；艾琳娜靠在石柱旁，安静地等待。"

    "所有人都在等着你的第一道政令——它不仅决定了接下来要做什么，更重要的是，它将向所有人宣告你是一个什么样的领主。"

    call autosave_before_choice from _call_autosave_before_choice_1

    "你的第一道政令是——"

    $ mark_important_choice()
    menu:
        "加强边防，扩编卫队|权力+15 忠诚+10 财富-15":
            $ log_decision("第一章", "首项政令: 加强边防", "扩编卫队，加强军事力量")
            $ first_decree = "军事"
            $ change_stat("power", 15)
            $ change_stat("loyalty", 10)
            $ change_stat("wealth", -15)
            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "安全是一切的基础。征召新兵，加固边境哨所。"
            "你的声音在大厅中回荡，沉稳而有力。"
            hide aldric_img with dissolve
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "遵命！领主大人英明！"
            "雷恩激动得差点拔出剑来——他及时忍住了，但脸上的兴奋遮掩不住。"
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "雷恩，卫队扩编到六十人。另外征召二十名预备民兵，每月训练两天。"
            player "边境哨所增设烽火台，遇到异常立刻点烟示警。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "是！我这就去安排！"
            hide captain_img with dissolve
            $ hide_all_chars()
            "卫队从四十人扩充到了六十人。边境巡逻加倍。"
            "消息传到男爵耳中时，他一定会重新掂量进犯艾登堡的代价。"
            "然而，军费的增加让本就紧张的财政更加捉襟见肘。"
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "领主大人，征兵的费用加上铠甲和武器的采购，金库大概要少三分之一。"
            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我知道。但城堡没了，钱也留不住。"
            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "也是。"
            hide aldric_img with dissolve

        "开仓放粮，收买民心|忠诚+20 声望+10 财富-20":
            $ log_decision("第一章", "首项政令: 开仓放粮", "赢得民心但消耗财富")
            $ first_decree = "民生"
            $ change_stat("loyalty", 20)
            $ change_stat("reputation", 10)
            $ change_stat("wealth", -20)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "百姓是领地的根本。打开粮仓，确保每家每户都能过冬。"
            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "领主大人仁慈。但粮仓的储量……只怕不够。"
            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "不够就去买。先用金库的钱从南方商人那里进粮。"
            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "可是领主大人，金库的存银本就不多了。如果全拿去买粮——"
            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "奥尔德里克，一个让百姓饿死的领主，不配坐在这把椅子上。"
            "老骑士张了张嘴，最终没有再说什么。他深深地鞠了一躬。"
            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "老臣遵命。这就去安排。"
            hide aldric_img with dissolve
            $ hide_all_chars()
            "消息传开，百姓们对新领主感恩戴德。"
            "有人在村口立了你的长生牌位——这在艾登堡是从未有过的事。几个老人甚至流着泪说，这是三十年来他们吃的第一顿饱饭。"
            "但金库已经见底了。"
            "你知道，仁慈是有价格的。现在你用金钱买到了民心，但如果明天金库空了，民心又会变成什么？"

        "清剿盗匪，恢复商路|财富+18 声望+10 权力+5":
            $ log_decision("第一章", "首项政令: 清剿盗匪", "恢复商路增加收入")
            $ first_decree = "治安"
            $ change_stat("wealth", 18)
            $ change_stat("reputation", 10)
            $ change_stat("power", 5)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "盗匪不除，税收无从谈起。雷恩，带一队人去清剿。"
            hide aldric_img with dissolve
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            $ play_sound("audio/sfx/sword_draw.ogg")
            captain "正合我意！那些毛贼，该教训教训了！"
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "三路出击——北路沿山脊搜索，东路封锁河渡口，西路从森林边缘包抄。不给他们逃路。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "好计划！领主大人在王都学过兵法？"
            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "读过几本书而已。关键还得靠你在前线指挥。"
            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "交给我！"
            hide captain_img with dissolve
            $ hide_all_chars()
            "两周后，雷恩剿灭了三个匪窝，商路重新畅通。"
            "缴获的赃物中有一些值钱的东西——几匹绸缎、一箱铜器、还有一袋银币。"
            "税收开始恢复，但剿匪中损失了五名士兵。"
            "你命人在城门前为阵亡的士兵举办了葬礼。你亲自为每一位阵亡者致辞，记住他们的名字。这是他们应得的尊重。"
            "而且，有传言说这些盗匪背后有人指使……"
            "在匪首的营帐中发现了一些来路不明的武器——制式精良，不像是山贼能弄到的东西。"

        "修缮城堡，巩固根基|权力+10 财富-10 可能发现秘密":
            $ log_decision("第一章", "首项政令: 修缮城堡", "发现密道")
            $ first_decree = "建设"
            $ change_stat("power", 10)
            $ change_stat("wealth", -10)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "城堡是我们最后的堡垒。先把它修好。"
            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "明智之举。老臣这就去安排工匠。"
            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "不只是修屋顶。我要彻底检查城堡的每一个角落——城墙、地基、水井、地窖，全部检查一遍。"
            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "领主大人做事周全。老臣佩服。"
            hide aldric_img with dissolve
            $ hide_all_chars()
            "修缮工作有条不紊地展开。西塔的屋顶补好了，城墙的裂缝也被填上。"
            "水井清理出了半尺厚的淤泥，储水量提高了三成。几扇朽烂的大门换成了新的橡木门，铁制的合页和锁扣也全部更新。"
            "更重要的是，工人在修缮地下室时发现了一条密道——"
            "它通往城堡外的树林深处。"
            "密道的入口隐藏在一面假墙后面，用机关门巧妙地伪装成一堵普通的石墙。如果不是工人偶然碰到了机关，也许永远不会有人发现。"
            "密道里很窄，只能容一人通过。但保养得很好——墙壁上每隔几步就有一个铁质烛台，地面铺着平整的石板。"
            "这不是一条废弃的古道。这是一条有人一直在使用的通道。"
            $ secret_passage_found = True
            $ collect_item("war_map")

    ## ============================================================
    ## 新增场景：第一道政令后的反响
    ## ============================================================

    scene bg great_hall with dissolve
    $ unlock_gallery("bg_great_hall")

    "你的第一道政令颁布后的那个夜晚，你在书房里收到了一些意想不到的回应。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve

    elena "领主大人，打扰了。"

    elena "我只是想说——您今天的决定，我会如实向王后陛下汇报。"

    "她的坦率出乎你的意料。大多数间谍不会主动承认自己的身份和任务。"

    menu:
        "坦然接受——'你说的很好，随你汇报'":
            $ change_rel("rel_elena", 5)
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你的职责是向王后汇报，我的职责是治理领地。各行其是，互不干涉。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "领主大人果然豁达。"
            "她说了句「那我先——」话没说完就转身走了。到门口时回头看了你一眼——那个眼神中有一丝你读不懂的东西。"

        "试探她——'你打算怎么写？'":
            $ change_stat("intrigue", 5)
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你打算怎么写这份报告？"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "实话实说。年轻的领主初来乍到，面对边境危机应对得当。第一道政令虽有争议，但展现了决断力。"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "听起来不坏。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "因为您做得确实不坏。"
            "她的语气中没有奉承。你开始觉得，这个女人也许比你最初以为的更有意思。"
            $ change_rel("rel_elena", 3)

        "警告她——'小心你写的每一个字'":
            $ change_stat("power", 3)
            $ change_rel("rel_elena", -5)
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你可以写你想写的任何东西。但记住——你住在我的城堡里，吃我的饭。如果你的报告给我带来麻烦……"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "领主大人是在威胁我？"
            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我在提醒你。"
            "她行了一礼。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "我记住了。"
            "她退出书房。你不确定这是明智之举还是愚蠢之举——恐吓一个间谍，通常不会有好结果。"

    hide elena_img with dissolve

    $ hide_all_chars()
    "你独自在书房中坐了很久。"

    "窗外的夜色如墨，偶尔有一两声夜枭的鸣叫从远处的树林传来。蜡烛烧了一半，蜡泪沿着烛台淌下来，时间不早了。"

    "你想起了父亲。想起了梦中他未说完的话。想起了那封密信上的百合花标记。想起了奥尔德里克欲言又止的表情。"

    "这座城堡的每一块石头里都藏着秘密。而你，才刚刚掀开了最表面的一层。"

    "你抬头看向墙上父亲的画像。烛光中，画中人的目光似乎在注视着你——温和、忧虑、期待。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve

    player "我会弄清楚一切的，父亲。"

    hide player_char_img with dissolve

    $ hide_all_chars()
    "你低声说出这句话。然后站起身，走向寝室。"

    "明天还有很多事要做。后天也是。大后天也是。"

    "你有一种预感——平静的日子不会太久了。"

    ## 扩展剧情：城堡初夜 / 晨间议事 / 校场比武 / 巡视村庄 / 晚宴风云
    call ch1_exp_first_night from _call_ch1_exp_first_night

    ## 深化剧情：父亲坟前 / 巡逻 / 法庭 / 市场 / 艾琳娜教学 / 老兵故事 / 地窖秘密 / 城墙日落
    call ch1_deep_father_grave from _call_ch1_dfg
    call ch1_deep_patrol from _call_ch1_dpatrol
    call ch1_deep_court from _call_ch1_dcourt
    call ch1_deep_market from _call_ch1_dmarket
    call ch1_deep_elena_lesson from _call_ch1_delesson
    call ch1_deep_old_guard from _call_ch1_doldguard
    call ch1_deep_cellar from _call_ch1_dcellar
    call ch1_deep_sunset from _call_ch1_dsunset

    ## NPC支线：村长请求
    call npc_village_quest from _call_npc_vq1

    ## ============================================================
    ## 第一章结尾
    ## ============================================================

label chapter1_end:

    $ persistent.chapters_completed.add("chapter1")
    $ unlock_achievement("first_steps")

    ## 章节结束统计
    call show_chapter_summary("第一章", "新主登基") from _call_show_chapter_summary_3

    $ play_music("audio/music/main_theme.ogg", fadein=2.0)
    scene black with dissolve

    "就这样，你度过了成为领主的第一周。"

    "你处理了第一个危机，颁布了第一道政令，结识了身边的重要人物。"

    "你学会了一件事——在权力的世界里，没有一件事是简单的。每一个决定都有代价，每一次微笑背后都可能藏着刀。"

    "但你也学到了另一件事——你并不像自己以为的那么软弱。当危机来临的时候，你没有退缩。当需要决断的时候，你没有犹豫。"

    "也许父亲选择把你送去王都而不是留在身边，正是为了让你学会独立思考。也许他早就预见到了今天——预见到你需要独自面对这一切。"

    "而那些藏在暗处的棋手，已经开始布下一局了。"

    "在你看不见的地方，各方势力已经开始行动——"

    $ hide_all_chars("baron_img")
    show baron_img at left with dissolve
    $ hide_all_chars()
    "男爵在筹划他的下一步棋。"
    "他的书房里铺开了一张艾登堡的地图。他的手指在铁矿的位置上来回摩挲，眼中闪烁着贪婪的光。"
    hide baron_img with dissolve

    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    $ hide_all_chars()
    "主教向王都发出了密信。"
    "那封信用教会专用的密码写成，即使被截获也无人能读懂。信中写了什么，只有收信人和圣母知道。"
    hide bishop_img with dissolve

    show elena_img at right with dissolve
    $ hide_all_chars()
    "艾琳娜在深夜写下了什么报告。"
    "她的鹅毛笔在羊皮纸上沙沙作响，烛光将她的影子投在墙壁上。她写到某一处时，停下笔沉思了很久——然后划掉了那句话，换了另一种措辞。"
    hide elena_img with dissolve

    "而那封关于你父亲死因的线索，如同一根暗刺，扎在你心里。"

    "暗百合。磨坊。密信。消失在账目中的金钱。父亲临终前的遗言。"

    "这些碎片像散落的拼图，你还看不到全貌。但你知道，它们终将拼合在一起。"

    "窗外，月亮正在变圆。"

    "满月之夜就要到了。"

    scene black with dissolve

    $ renpy.force_autosave()

    jump chapter2_start

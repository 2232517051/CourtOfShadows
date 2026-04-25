## ============================================================
## 权谋之庭 - Court of Shadows
## 序章：金鹰之子
## ============================================================

## ────────────────────────────────────────────────────────────
## 序章专用变量
## ────────────────────────────────────────────────────────────

## 序章剧情标记
default prologue_bully_choice = ""
default prologue_father_question = ""
default prologue_grief_choice = ""
default prologue_study_focus = ""
default prologue_secret_heard = ""
default prologue_father_visit = ""
default prologue_banquet_style = ""
default prologue_completed = False

## 序章专用角色
define mother = Character("母亲", color="#e0c4a8", image="mother")
define father = Character("父亲", color="#8b7355", image="father")
define tutor = Character("修士卢卡", color="#a0926b", image="tutor")
define friend_marcus = Character("马库斯", color="#5b8a72", image="friend_marcus")
define bully_kid = Character("胖子费利克斯", color="#8b4513", image="bully_kid")
define old_guard = Character("老卫兵汉斯", color="#708090", image="old_guard")
define servant_marta = Character("女仆玛尔塔", color="#c4a882", image="servant_marta")
define priest_thomas = Character("神父托马斯", color="#daa520", image="priest_thomas")
define noble_werner = Character("维尔纳公子", color="#4682b4", image="noble_werner")
define countess_hilda = Character("希尔达伯爵夫人", color="#9370db", image="countess_hilda")

## ────────────────────────────────────────────────────────────
## 序章入口
## ────────────────────────────────────────────────────────────

label prologue:

    ## 新手引导
    if not persistent.tutorial_seen:
        call screen tutorial_overlay

    ## 难度选择（每次新游戏都可选）
    call screen difficulty_select

    ## New Game+ 奖励
    $ apply_ng_plus()
    if persistent.ng_plus_unlocked:
        show screen ng_plus_banner
        pause 1.0

    ## 输入名字（自定义界面，解决手机端卡住问题）
    scene black with dissolve
    $ _name_input_value = "亚瑟"
    call screen name_input_screen
    if _return == "default":
        $ player_name = "亚瑟"
    else:
        $ player_name = _name_input_value.strip()
        if player_name == "":
            $ player_name = "亚瑟"

    ## 彩蛋名字检测
    $ _egg = check_name_easter_egg(player_name)
    if _egg:
        show screen name_easter_egg(egg_text=_egg)
        pause 2.0

    ## 初始化物品背包
    call init_inventory from _call_init_inventory_prologue

    ## 记录章节初始属性
    $ snapshot_chapter_start()

    ## 序章过场动画
    call cinematic_prologue from _call_cinematic_prologue

    ## 恢复对话窗口
    window auto

    ## 进入第一阶段
    jump prologue_childhood


## ════════════════════════════════════════════════════════════
## 过场动画：序章
## ════════════════════════════════════════════════════════════

label cinematic_prologue:
    window hide
    $ quick_menu = False
    ## 不允许点击跳过，过场按时间自动播放
    $ _dismiss_pause = False
    $ _cin_skip = False

    stop music fadeout 1.5
    scene black
    pause 0.5

    play sound "audio/sfx/bell_toll.ogg"
    show screen cin_text("公元1325年。隆冬。", "在风雪中，一个孩子降生于艾登堡。")
    pause 4.0
    hide screen cin_text with cin_dissolve
    pause 0.5

    play music "audio/music/winter_wind.ogg" fadein 2.5
    show screen cin_title(0, "金鹰之子", "Son of the Golden Eagle")
    pause 3.5
    hide screen cin_title with cin_dissolve
    pause 0.3

    scene bg castle_exterior at cin_parallax_left with cin_slow
    show screen cin_overlay
    pause 0.8

    voice "audio/narration/ch0_line1.mp3"
    show screen cin_sub("1325年的冬天，比任何人记忆中的都要冷。")
    $ wait_voice(6.0)
    hide screen cin_sub

    voice "audio/narration/ch0_line2.mp3"
    show screen cin_sub("艾登堡领主的妻子在风雪中产下一子。接生婆说，孩子落地时没有哭。")
    $ wait_voice(9.0)
    hide screen cin_sub

    voice "audio/narration/ch0_line3.mp3"
    show screen cin_sub("直到父亲将他抱起，贴在胸口，他才发出了第一声啼哭。")
    $ wait_voice(6.0)
    hide screen cin_sub

    hide screen cin_overlay
    scene black with cin_slow
    stop music fadeout 2.0
    pause 1.0

    $ _dismiss_pause = False
    $ _cin_skip = False
    $ _dismiss_pause = True
    $ quick_menu = True
    window auto
    return


## ════════════════════════════════════════════════════════════
## 第一阶段：童年 (5-8岁) — "种子"
## ════════════════════════════════════════════════════════════

label prologue_childhood:

    ## 童年期主角肖像
    $ player.image_tag = "player_child"
    $ play_music("audio/music/castle_calm.ogg", fadein=2.0)

    call show_chapter("序章·上", "种子", "1330年，艾登堡") from _call_show_chapter_prologue1

    scene bg castle_exterior with dissolve
    $ unlock_gallery("bg_castle_exterior")

    "你五岁。"

    "夏天。城堡的庭院里长满了野草，蒲公英的白色绒毛在午后的阳光中飘荡。你追着它们跑，光着脚踩在温热的石板上。"

    "世界很大。大到你跑不到尽头。"

    "庭院的另一边，卫兵们在换岗。铠甲碰撞的声音清脆而有节奏，像某种你听不懂的音乐。你停下来看他们，直到一个老卫兵朝你咧嘴一笑。"

    $ hide_all_chars("old_guard_img")
    show old_guard_img at left with dissolve

    old_guard "小少爷，又跑出来啦？夫人到处找你呢。"

    hide old_guard_img with dissolve

    "你没理他，继续追蒲公英。五岁的你还不懂什么叫规矩。"

    scene bg great_hall with dissolve

    "傍晚，女仆玛尔塔把你从庭院里捞回来，浑身是土。她一边给你擦脸一边唠叨。"

    $ hide_all_chars("servant_marta_img")
    show servant_marta_img at left with dissolve

    servant_marta "少爷，您是领主的儿子，不能整天在泥地里打滚。明天要见格雷伯爵家的公子，您得体面些。"

    hide servant_marta_img with dissolve

    "你不知道格雷伯爵是谁。你只知道他的儿子费利克斯很胖，上次来的时候偷了你的木剑。"

    ## ──────────────────────────────────────
    ## 场景1：被贵族孩子欺负
    ## ──────────────────────────────────────

    scene bg castle_exterior with dissolve

    "第二天。费利克斯来了。"

    "他比你高半个头，圆滚滚的脸上带着一种你日后才学会辨认的表情——轻蔑。他身后跟着两个随从家的孩子，像两条尾巴。"

    $ hide_all_chars("bully_kid_img")
    show bully_kid_img at left with dissolve

    bully_kid "哟，小领主。听说你连马都不敢骑？"

    "你没说话。你确实不敢骑马。但你不想让他知道。"

    $ hide_all_chars("bully_kid_img")
    show bully_kid_img angry at left with dissolve

    bully_kid "我爹说，你们家迟早要完。你爹就知道守着这破城堡，连块新地都打不下来。"

    $ hide_all_chars()
    "他伸手推了你一把。不算很重，但足够让你踉跄两步。身后那两个孩子笑了。"

    "你的手指绷直了，指节发白。"

    menu:
        "揍他。不管他爹是谁。":
            $ change_stat("power", 5)
            $ change_courage(-5)
            $ prologue_bully_choice = "fight"
            $ log_decision("序章", "还击费利克斯", "权力+5，勇气消耗")

            "你冲上去，一拳砸在费利克斯的鼻子上。"

            "他没想到你会动手。愣了一瞬，然后嚎叫起来，鼻血顺着嘴角淌下去。那两个跟班吓得后退了三步。"

            "卫兵们赶来拉开你们的时候，费利克斯已经坐在地上哭了。你的指关节火辣辣地疼，但你一声不吭。"

            "那天晚上，父亲把你叫到书房。你以为会挨骂。"

            hide bully_kid_img with dissolve
            scene bg study with dissolve

            show father_img at left with dissolve

            father "听说你打了格雷家的孩子。"

            "你低着头，不说话。"

            father "打赢了？"

            $ hide_all_chars()
            "你点头。"

            "你偷偷抬眼看他，发现他嘴角似乎有一丝不易察觉的弧度。"

            $ hide_all_chars("father_img")
            show father_img happy at left with dissolve

            father "下次别打脸。容易留证据。"

            hide father_img with dissolve

        "去找父亲告状。这不公平。":
            $ change_stat("loyalty", 5)
            $ change_courage(3)
            $ prologue_bully_choice = "report"
            $ log_decision("序章", "向父亲告状", "忠诚+5")

            $ hide_all_chars()
            "你转身跑了。不是因为害怕——你去找父亲。"

            "这不公平。他比你大，还带了帮手。你要让大人来主持公道。"

            hide bully_kid_img with dissolve
            scene bg study with dissolve

            "父亲放下手中的文书，听完你的话，皱起了眉头。"

            $ hide_all_chars("father_img")
            show father_img at left with dissolve

            father "他推了你？"

            "你点头。"

            father "然后呢？"

            "你说，然后你来找他了。"

            father "记住，向上求助不丢人。但你得分清楚——什么时候该求助，什么时候该自己扛。"

            "他揉了揉你的头发。手掌粗糙，但温暖。"

            father "明天我会跟格雷伯爵谈。但这是最后一次。下次，你自己解决。"

            hide father_img with dissolve

        "忍。记住他的脸。":
            $ change_stat("intrigue", 5)
            $ change_courage(5)
            $ prologue_bully_choice = "endure"
            $ log_decision("序章", "忍耐费利克斯", "谋略+5")

            $ hide_all_chars()
            "你没动。"

            "费利克斯又推了你一下，你还是没动。他似乎觉得无趣了，'哼'了一声，带着他的跟班走了。"

            hide bully_kid_img with dissolve

            "你站在原地，看着他的背影。"

            "你把他的脸记住了。他说的每一个字，你都记住了。你不知道将来有什么用，但你就是记住了。"

            "那天晚上你睡不着。不是因为委屈。你在想——他为什么敢这样对你？因为他爹比你爹厉害吗？"

            "你翻了个身，盯着天花板。五岁的你第一次开始思考'力量'这个词。"

    ## ──────────────────────────────────────
    ## 童年深化场景 (6岁春 母亲的花园)
    ## ──────────────────────────────────────

    call prologue_deep_childhood_1 from _call_pdc1

    ## ──────────────────────────────────────
    ## 场景2：父亲教认家族徽章
    ## ──────────────────────────────────────

    scene bg study with dissolve
    $ unlock_gallery("bg_study")

    "六岁那年秋天。"

    "父亲破天荒地把你叫到书房，关上了门。壁炉里的火烧得很旺，映在墙上那面巨大的盾牌上——金色的鹰，展翅欲飞，利爪抓着一束箭。"

    "你以前看过这面盾牌无数次。但这是第一次，父亲让你坐到他膝盖上，指着它给你讲。"

    $ hide_all_chars("father_img")
    show father_img at left with dissolve

    father "这是我们家的徽章。认识吗？"

    "你说认识。金色的大鸟。"

    father "鹰。不是鸟，是鹰。"

    "他的声音很低，像是在说一件极其重要的事。"

    father "这只鹰已经守护我们家族两百年了。你的曾祖父，他的父亲，他的父亲的父亲——每一代人都在这只鹰的注视下出生、长大、老去。"

    "他停顿了一下。壁炉里的木柴发出一声脆响。"

    father "总有一天，这只鹰要交给你来守护。"

    "他看着壁炉，眼神突然变得很远。"

    father "先王曾对我说过一句话——'有些信任比血脉更重。'我到今天都没忘。"

    $ hide_all_chars()
    "他没有再说下去。你后来很多年才明白——那不是一句客套话，是一个小领主与一位国王之间不该存在的某种纽带。"

    "你那时不懂这句话的重量。你只是好奇。"

    menu:
        "父亲，我们家打过仗吗？":
            $ change_stat("power", 3)
            $ prologue_father_question = "war"
            $ log_decision("序章", "询问战争故事", "权力+3")

            $ hide_all_chars("father_img")
            show father_img at left with dissolve
            father "打过。"

            "他的眼神变了。变得很远，好像在看一个你看不见的地方。"

            father "你曾祖父在边境挡住过三千人的进攻。那年冬天，补给断了整整两个月。城墙上的守军饿得连弓都拉不开。"

            "你睁大了眼睛。"

            father "但他们没退。一步都没退。"

            "他低头看你，目光锐利。"

            father "记住，我们家的人不退。"

            "你使劲点头。虽然你不太明白为什么不能退。"

        "父亲，我们家有秘密吗？":
            $ change_stat("reputation", 3)
            $ prologue_father_question = "secret"
            $ log_decision("序章", "询问家族秘密", "谋略+3")

            "父亲看了你一眼。那个眼神很复杂。你长大后才学会辨认——那是惊讶，混着一丝……警惕？"

            $ hide_all_chars("father_img")
            show father_img at left with dissolve
            father "什么秘密？"

            $ hide_all_chars()
            "你说，每个家族都有秘密嘛。故事里都是这么说的。"

            "他沉默了好久。久到你以为他不会回答了。"

            $ hide_all_chars("father_img")
            show father_img at left with dissolve
            father "有。"

            "就一个字。"

            father "但秘密之所以是秘密，是因为知道的人越少越好。等你长大了，我再告诉你。"

            $ hide_all_chars()
            "他在骗你。你能感觉到。不是没有秘密——是秘密太重，他不想让一个六岁的孩子背。"

            "但你记住了。他说了'有'。"

        "父亲，我们为什么要去教堂？":
            $ change_stat("faith", 3)
            $ prologue_father_question = "faith"
            $ log_decision("序章", "询问信仰传统", "信仰+3")

            $ hide_all_chars("father_img")
            show father_img at left with dissolve
            father "因为人需要信仰。"

            "他说得很平静，没有平时跟神父说话时的那种客套。"

            father "不一定是信上帝。但你要信点什么。哪怕是信你自己。"

            $ hide_all_chars()
            "你歪着头想了想。"

            "你说，那你信什么？"

            "父亲没有马上回答。他看着壁炉里跳动的火焰，很久。"

            $ hide_all_chars("father_img")
            show father_img at left with dissolve
            father "我信这面盾牌。信这座城堡。信你母亲。信你。"

            "他低头看你，罕见地露出一个笑容。"

            $ hide_all_chars("father_img")
            show father_img happy at left with dissolve

            father "够了吗？"

            "你觉得够了。虽然你还不太懂。"

    hide father_img with dissolve

    ## ──────────────────────────────────────
    ## 场景3：母亲去世
    ## ──────────────────────────────────────

    scene black with fade
    $ play_music("audio/music/grief.ogg", fadein=2.0)

    "七岁。冬天。"

    "母亲病了。"

    "起初只是咳嗽。然后是发烧。然后是卧床不起。你不被允许进她的房间，但你每天都守在门外，听着里面传出的声音。"

    "有时是咳嗽。有时是低语。有时什么都没有。"

    "那种沉默最可怕。"

    scene bg study with dissolve

    "神父来了。医师来了。从镇上请来的药剂师也来了。他们进进出出，表情一次比一次沉重。"

    "有一天，女仆玛尔塔蹲下来，握着你的手。她的眼睛是红的。"

    $ hide_all_chars("servant_marta_img")
    show servant_marta_img sad at left with dissolve

    servant_marta "少爷……夫人想见您。"

    hide servant_marta_img with dissolve

    "你走进房间。母亲躺在床上，脸色白得像窗外的雪。她瘦了很多，手腕细得像树枝。但她看到你的时候，笑了。"

    $ hide_all_chars("mother_img")
    show mother_img sad at left with dissolve

    mother "过来。让我看看你。"

    "你走过去。她伸出手摸你的脸，手指冰凉。"

    mother "长高了。"

    $ hide_all_chars()
    "你不知道该说什么。你想说'你什么时候好'，但话到嘴边变成了沉默。因为你看到了她眼睛里的东西——一个七岁的孩子不该看懂的东西。"

    "告别。"

    $ hide_all_chars("mother_img")
    show mother_img at left with dissolve
    mother "听话。别让你父亲太操心。"

    "她停了停，像是在攒最后一点力气。"

    mother "不管将来发生什么……做个好人。"

    hide mother_img with dissolve

    "那天夜里，母亲走了。"

    scene black with dissolve

    "城堡里的人都在哭。女仆、厨娘、甚至那个平时凶巴巴的马夫。父亲没有哭。他坐在书房里，一个人，门关着。你从门缝里看到他的背影——挺直的，一动不动，像一尊石像。"

    "你站在走廊里，不知道该怎么办。"

    menu:
        "哭。哭到嗓子哑。":
            $ change_stat("power", 2)
            $ change_courage(-3)
            $ prologue_grief_choice = "cry"
            $ log_decision("序章", "号啕大哭", "权力+2（释放真实情感）")

            "你蹲在走廊的角落里，哭了。"

            "不是小声啜泣。是嚎啕大哭，那种五脏六腑都在翻搅的哭法。路过的仆人都停下来看你，有人想过来抱你，被你推开了。"

            "你不要安慰。你要妈妈。"

            "哭了很久。久到你不知道过了多长时间。最后是老卫兵汉斯把你抱起来，送回房间。他什么都没说，只是把毯子盖在你身上。"

            "第二天醒来，嗓子是哑的。眼睛肿得像桃子。"

            "但你感觉好了一点。只是一点。"

        "不哭。一声不出。":
            $ change_stat("power", 2)
            $ change_courage(3)
            $ prologue_grief_choice = "silent"
            $ log_decision("序章", "沉默面对", "谋略+2（学会隐藏情感）")

            "你没哭。"

            "不是不想哭。是哭不出来。好像有什么东西堵在喉咙里，上不去也下不来。"

            "你回到自己的房间，躺在床上，睁着眼睛看天花板。外面的风很大，吹得窗户咯吱作响。"

            "你想起母亲最后的样子。那只冰凉的手。那个笑容。"

            "你把被子拉过头顶，在黑暗里蜷成一团。"

            "从那天起，你学会了一件事——痛苦是可以藏起来的。藏得够深，别人就看不见。"

        "去教堂。为母亲祈祷。":
            $ change_stat("faith", 3)
            $ change_courage(2)
            $ prologue_grief_choice = "pray"
            $ log_decision("序章", "为母亲祈祷", "信仰+3")

            scene bg castle_chapel with dissolve

            "你去了教堂。"

            "城堡的小教堂冷得像冰窖。烛台上只剩半截蜡烛，摇曳的火光把圣像的影子拉得很长。"

            "你跪在冰冷的石地上，学着大人的样子，双手合十。"

            "你不太会祈祷。你只是反复说：请让她去一个不疼的地方。请让她去一个不疼的地方。"

            "不知道过了多久，神父来了。他没有说话，只是在你身边坐下。"

            $ hide_all_chars("priest_thomas_img")
            show priest_thomas_img at left with dissolve

            priest_thomas "上帝会照顾她的，孩子。"

            hide priest_thomas_img with dissolve

            "你不知道该不该信。但你宁愿信。"

    ## ──────────────────────────────────────
    ## 童年深化场景 (7岁地窖密语)
    ## ──────────────────────────────────────

    call prologue_deep_childhood_2 from _call_pdc2

    ## ──────────────────────────────────────
    ## 童年尾声：葬礼
    ## ──────────────────────────────────────

    scene black with fade

    "母亲的葬礼在三天后举行。"

    "全城堡的人都来了。父亲站在最前面，始终没有回头看你。牧师念了很长的祷文，你一个字都没听进去。"

    "你只记得棺木被抬走的时候，外面开始下雪了。大片大片的雪，落在你的睫毛上，化成冰凉的水。"

    "七岁的你失去了母亲。"

    "你不知道的是，你即将失去的远不止这些。"

    ## ──────────────────────────────────────
    ## 童年深化场景 (8岁伯特兰爵士的告别)
    ## ──────────────────────────────────────

    call prologue_deep_childhood_3 from _call_pdc3

    scene black with dissolve
    pause 0.5

    jump cinematic_prologue_2


## ════════════════════════════════════════════════════════════
## 过渡动画：童年→少年
## ════════════════════════════════════════════════════════════

label cinematic_prologue_2:
    window hide
    $ quick_menu = False
    $ _dismiss_pause = False
    $ _cin_skip = False

    stop music fadeout 1.5
    scene black
    pause 0.5

    show screen cin_text("五年后。", "父亲做了一个决定。")
    pause 3.5
    hide screen cin_text with cin_dissolve
    pause 0.5

    play music "audio/music/main_theme.ogg" fadein 2.0
    show screen cin_title(0, "萌芽", "The Seedling")
    pause 3.0
    hide screen cin_title with cin_dissolve

    scene bg church_interior at cin_parallax_right with cin_slow
    show screen cin_overlay
    pause 0.8

    voice "audio/narration/ch0_p2_line1.mp3"
    show screen cin_sub("1337年春，十二岁的领主之子被送往王都。")
    $ wait_voice(7.0)
    hide screen cin_sub

    voice "audio/narration/ch0_p2_line2.mp3"
    show screen cin_sub("圣安德烈修道院——王国最高学府。贵族子弟的摇篮，也是权力的温床。")
    $ wait_voice(8.0)
    hide screen cin_sub

    voice "audio/narration/ch0_p2_line3.mp3"
    show screen cin_sub("在修道院的殿堂中，他将明白——知识既是盾，也是剑。")
    $ wait_voice(6.0)
    hide screen cin_sub

    hide screen cin_overlay
    scene black with cin_slow
    stop music fadeout 1.5
    pause 0.5

    $ _dismiss_pause = False
    $ _cin_skip = False
    $ _dismiss_pause = True
    $ quick_menu = True
    window auto
    jump prologue_youth


## ════════════════════════════════════════════════════════════
## 第二阶段：少年 (12-15岁) — "萌芽"
## ════════════════════════════════════════════════════════════

label prologue_youth:

    ## 少年期主角肖像
    $ player.image_tag = "player_teen"
    $ play_music("audio/music/main_theme.ogg", fadein=2.0)

    call show_chapter("序章·中", "萌芽", "1337年，王都圣安德烈修道院") from _call_show_chapter_prologue2

    scene bg church_interior with dissolve
    $ unlock_gallery("bg_church_interior")

    "圣安德烈修道院坐落在王都的东北角，背靠一座小山。"

    "灰色的石墙爬满了常春藤，尖顶的钟楼在晨雾中若隐若现。从远处看，它像一座城堡多过像一座教堂。"

    "你十二岁。带着一箱书、一把短剑和父亲的一封信来到这里。"

    "信很短。你在马车上读了三遍。"

    "'学你该学的。别惹事。记住你是谁。'"

    "典型的父亲。三句话解决一切。"

    "修道院的门房是个秃顶的老修士，登记你的名字时，眉毛抬了抬。"

    $ hide_all_chars("tutor_img")
    show tutor_img at left with dissolve

    tutor "艾登堡的？嗯。你父亲年轻时也在这里读过书。那时候他打断了一个伯爵儿子的鼻梁骨。"

    "他瞥了你一眼。"

    tutor "希望你比他安分。"

    hide tutor_img with dissolve

    ## ──────────────────────────────────────
    ## 场景1：修道院生活，选择主修
    ## ──────────────────────────────────────

    scene bg church_interior with dissolve

    "修道院的生活枯燥且规律。"

    "清晨五点，钟声响。祈祷。早课。午饭。下午课。晚祷。熄灯。日复一日。"

    "你的同学来自王国各地——伯爵的次子、男爵的侄子、主教的外甥。还有几个商人的儿子，靠捐款买来的名额。"

    "他们之间有一套你花了半年才摸清的规矩：谁跟谁坐，谁先进门，谁的笑话该笑谁的不该笑。"

    "你和一个叫马库斯的同学走得最近。他是个小贵族的儿子，话不多，但脑子很快。"

    $ hide_all_chars("friend_marcus_img")
    show friend_marcus_img at left with dissolve

    friend_marcus "在这里，书本教你的东西只占一半。另一半，得自己学。"

    hide friend_marcus_img with dissolve

    $ hide_all_chars()
    "他说这话的时候，正帮你把墨水从衬衫上洗掉——被一个高年级的学生'不小心'泼的。"

    "半年后，你开始选择自己的方向。修道院允许学生在基础课之外选修一门专长。"

    menu:
        "剑术。身体是最可靠的武器。":
            $ change_stat("power", 5)
            $ prologue_study_focus = "sword"
            $ log_decision("序章", "选修剑术", "权力+5")

            "你选了剑术。"

            "教剑的是个退役骑士，独眼，左手缺了两根手指。他从不解释动作，只做示范。做一遍，你跟着做。错了，挨打。再做。再错，再挨打。"

            "第一个月，你浑身都是青紫。第二个月，你开始能挡住他的前三招。第三个月，他第一次朝你点了点头。"

            "没说好。但你知道那是好的意思。"

            "到了第二年，全修道院的同龄人里，没人愿意跟你对练了。因为你下手没轻没重。"

            "马库斯说你像条疯狗。你觉得是夸奖。"

        "策略。赢的方式不止一种。":
            $ change_stat("intrigue", 5)
            $ prologue_study_focus = "strategy"
            $ log_decision("序章", "选修策略", "谋略+5")

            "你选了策略。"

            "教策略的修士卢卡是个瘦小的老头，据说年轻时当过某位伯爵的幕僚。他不教你怎么打仗。他教你怎么不打仗就赢。"

            $ hide_all_chars("tutor_img")
            show tutor_img at left with dissolve

            tutor "棋盘上最强的棋子不是王后。是卒。因为卒足够多，足够不起眼，没人会在意一个卒的走向。等他们注意到的时候，卒已经变成了王后。"

            hide tutor_img with dissolve

            $ hide_all_chars()
            "你花了三年学这些东西。如何读懂一封信里没写出来的意思。如何从一个人的语气判断他在撒谎。如何让两个互相敌对的人同时觉得你站在他们那边。"

            "马库斯说你越来越像条蛇。你不置可否。"

        "神学。在这个世界上，信仰是最大的权力。":
            $ change_stat("faith", 5)
            $ prologue_study_focus = "theology"
            $ log_decision("序章", "选修神学", "信仰+5")

            "你选了神学。"

            "不是因为虔诚。至少一开始不是。是因为你注意到——在这座修道院里，甚至在整个王国里，能让国王和乞丐同时低头的只有一样东西。"

            "上帝。或者更准确地说，代表上帝说话的人。"

            "教神学的神父托马斯是个矛盾的人。他对穷人慈悲，对权贵冷淡，对你严格到近乎刻薄。"

            $ hide_all_chars("priest_thomas_img")
            show priest_thomas_img at left with dissolve

            priest_thomas "别背了。你把整本圣经背下来也没用。我问你——如果上帝是全能的，他为什么允许苦难存在？"

            hide priest_thomas_img with dissolve

            $ hide_all_chars()
            "这个问题你想了三天。"

            "三年后，你成了修道院里最好的辩手。不是因为你说得对，而是因为你懂得什么时候该沉默。"

        "商业。钱不是万能的，但没有钱万万不能。":
            $ change_stat("wealth", 5)
            $ prologue_study_focus = "commerce"
            $ log_decision("序章", "选修商业", "财富+5")

            "你选了商业。"

            "这在贵族子弟中算是'不体面'的选择。剑术才是正道，策略也说得过去，商业？那是商人该操心的事。"

            "但你不在乎。因为你发现了一个所有人都假装看不见的真相——这座修道院里最受尊敬的不是那个公爵的儿子，而是那个商人的儿子。因为他有钱请客。"

            "教商业的是个犹太裔学者，被修道院半请半胁地留下来的。他教你看账本，教你算利息，教你分辨好年份的羊毛和差年份的区别。"

            "更重要的是，他教你一句话——"

            "'每一枚金币都是一张选票。有足够多的金币，你可以选举自己当国王。'"

            "马库斯说你铜臭味越来越重。你说，铜臭味比血腥味好闻。"

    ## ──────────────────────────────────────
    ## 场景2：偷听到密谈
    ## ──────────────────────────────────────

    scene bg church_interior with dissolve

    "十三岁。秋天。"

    "那天你本不该在那里。"

    "晚祷结束后，你发现自己的笔记本落在了回廊。回去取的时候，你听到了声音——从神父托马斯的房间传来的。"

    "门没关严。缝隙里透出烛光和两个人的声音。"

    "一个是托马斯。另一个你不认识，声音低沉，带着外地口音。"

    "'……艾登堡的领主已经不听劝了。再这样下去……'"

    "'他知道太多了。那些信件……'"

    "'处理掉？'"

    "'不。还不到时候。但要做准备。'"

    "你听到了你父亲的名字。你的血一下子凉了。"

    "他们在说什么？什么信件？什么'处理掉'？"

    "你站在黑暗的走廊里，心跳如鼓。"

    menu:
        "踹开门，质问他们在说什么。":
            $ change_stat("power", 3)
            $ change_courage(-8)
            $ prologue_secret_heard = "confront"
            $ log_decision("序章", "闯进去质问", "权力+3，勇气大量消耗")

            "你推开了门。"

            "两个人同时看向你。托马斯的脸色瞬间变了。另一个人——黑袍，兜帽，你看不清他的脸。"

            $ hide_all_chars("priest_thomas_img")
            show priest_thomas_img angry at left with dissolve

            priest_thomas "……你怎么在这里？"

            $ hide_all_chars()
            "你的声音在发抖，但你没有退。"

            "你说：你们在说我父亲。我听到了。"

            "走廊里的火把在风中晃了晃，影子在墙上猛地扭曲了一下。"

            "然后托马斯笑了。一种你从未在他脸上见过的笑容——温和的，安抚的，假的。"

            $ hide_all_chars("priest_thomas_img")
            show priest_thomas_img at left with dissolve
            priest_thomas "孩子，你听错了。我们在讨论教区的事务。'艾登'是一个教区的名字。跟你父亲没有关系。"

            hide priest_thomas_img with dissolve

            $ hide_all_chars()
            "你不信。但那个黑袍人已经站了起来，身量很高，你不得不仰着头看他。"

            "他没有说话。只是看了你一眼。那一眼让你后背发凉。"

            "你退了出去。"

            "从那天起，托马斯对你格外'关照'。你说不清那是善意还是监视。"

        "悄悄离开。记住每一个字。":
            $ change_stat("intrigue", 5)
            $ change_courage(3)
            $ prologue_secret_heard = "eavesdrop"
            $ log_decision("序章", "偷听并记住", "谋略+5")

            "你屏住呼吸，贴着墙壁，一步一步向后退。"

            "你继续听了一会儿。他们又说了一些你听不太懂的话——什么'北方的协议'，什么'主教的态度'，什么'等到春天'。"

            "然后那个陌生人说了一句让你记了一辈子的话——"

            "'金鹰飞不了多久了。'"

            "你退到走廊尽头，转身，无声地跑回了宿舍。"

            "那天夜里你把听到的每一个字都写在了笔记本最后一页。然后撕下来，折好，塞进了枕头里的一个破洞。"

            "你不知道这些话意味着什么。但直觉告诉你——很重要。"

        "去找修道院院长报告。":
            $ change_stat("faith", 3)
            $ change_courage(2)
            $ prologue_secret_heard = "report_priest"
            $ log_decision("序章", "向院长报告", "信仰+3")

            "你去找了院长。"

            "老院长听完你的话，捏着念珠不动了。他的表情你读不懂——不像惊讶，更像是……为难。"

            "他让你回去睡觉，说会处理的。"

            "第二天，一切如常。托马斯照常上课。那个黑袍人不见了。院长再也没有提过这件事。"

            "但你注意到一个变化——院长开始经常到你的宿舍区散步。像是巡视，又像是守护。"

            "你不确定他是在保护你，还是在看着你。"

    ## ──────────────────────────────────────
    ## 少年深化场景 (13岁禁书)
    ## ──────────────────────────────────────

    call prologue_deep_youth_1 from _call_pdy1

    ## ──────────────────────────────────────
    ## 场景3：回家探亲
    ## ──────────────────────────────────────

    scene black with fade
    $ play_music("audio/music/grief.ogg", fadein=2.0)

    "十四岁。你第一次回家。"

    "两年没见，艾登堡看起来比你记忆中小了。——不，是你长大了。"

    scene bg castle_exterior with dissolve

    "城门口没有人迎接你。只有一个你不认识的年轻卫兵，行了个不太标准的礼。"

    "你找到父亲的时候，他在书房。"

    scene bg study with dissolve

    "门开了。他坐在那把高背椅上——你记忆中的那把。但他……变了。"

    "头发白了大半。脸颊凹陷下去，颧骨突出得像刀刃。他裹着一件厚厚的毛毯，虽然壁炉烧得很旺。"

    "他看到你的时候，眼睛亮了一下。只是一下。"

    $ hide_all_chars("father_img")
    show father_img sad at left with dissolve

    father "回来了。"

    $ hide_all_chars()
    "两个字。没有拥抱。没有'我想你了'。这是你的父亲。"

    "你坐在他对面，想找话说。但你发现——你不知道该跟他说什么。两年的距离，像一堵看不见的墙。"

    "他咳嗽了几声。不是普通的咳嗽——深的，从肺里翻出来的那种。"

    $ hide_all_chars("father_img")
    show father_img at left with dissolve
    father "学得怎么样？"

    $ hide_all_chars()
    "你说了一些。考试成绩、老师的评价、选修的课程。他听着，偶尔点头。你说不准他是在听还是在想别的事。"

    "你注意到书桌上摞着厚厚一叠信件。有些已经拆开了，有些还没有。最上面那封的火漆是你不认识的纹章——不是鹰，是某种蛇形的图案。"

    "你还注意到他的手。握笔的时候在抖。"

    menu:
        "父亲，你是不是生病了？发生了什么？":
            $ change_stat("loyalty", 3)
            $ prologue_father_visit = "question"
            $ log_decision("序章", "追问父亲状况", "谋略+3")

            "你忍不住了。"

            "你说：父亲，你看起来很不好。发生了什么？"

            "他的手停了。"

            $ hide_all_chars("father_img")
            show father_img at left with dissolve
            father "没什么。"

            $ hide_all_chars()
            "你不信。你说：我不是小孩了。"

            "他抬起头看你。很久。像是在衡量你是否真的不是小孩了。"

            $ hide_all_chars("father_img")
            show father_img at left with dissolve
            father "……有些事，知道了反而不好。"

            $ hide_all_chars()
            "又是这句话。和六岁时一模一样。"

            "但这次你没有放弃。你说：如果有人要对你不利，我需要知道。"

            "他沉默了。壁炉里的火'噼啪'作响。"

            $ hide_all_chars("father_img")
            show father_img at left with dissolve
            father "你在修道院……听到了什么？"

            $ hide_all_chars()
            "他的语气变了。不再是父亲对儿子的口吻。更像是……一个将领在问斥候。"

            "你犹豫了一下，把那天晚上听到的事告诉了他。他听完后，什么都没说。只是把桌上的那叠信件翻过去，让你看不到封面。"

            $ hide_all_chars("father_img")
            show father_img at left with dissolve
            father "回去之后，别太相信那个托马斯。"

            hide father_img with dissolve

            "就这一句。没有解释。"

        "父亲，我会照顾好自己的。你也要保重。":
            $ change_stat("loyalty", 5)
            $ prologue_father_visit = "comfort"
            $ log_decision("序章", "安慰父亲", "忠诚+5")

            $ hide_all_chars()
            "你没有问。"

            "不是不想问。是你看到了他眼角的疲惫，看到了那双发抖的手，你不忍心再给他增加任何负担。"

            "你说：父亲，我在修道院一切都好。你不用担心我。"

            "他点了点头。"

            "你说：你也要保重身体。"

            "然后他做了一件很少做的事——他站起来，走到你面前，拍了拍你的肩膀。"

            $ hide_all_chars("father_img")
            show father_img at left with dissolve
            father "你长大了。"

            $ hide_all_chars()
            "三个字。但你听出了很多东西。骄傲。欣慰。还有一种说不清的……歉意？"

            "那天晚上你失眠了。你躺在儿时的床上，听着窗外的风声，想起母亲，想起这座城堡，想起父亲那双发抖的手。"

            hide father_img with dissolve

            "你突然意识到一件事——父亲老了。真的老了。而你还不够强大。"

        "假装什么都没注意到。聊点别的。":
            $ change_stat("wealth", 3)
            $ prologue_father_visit = "ignore"
            $ log_decision("序章", "假装正常", "财富+3（学会了圆滑处世）")

            "你选择了沉默。"

            "不是不在乎。是你判断——此刻追问只会让他更不安。他不想让你担心，你就配合他。"

            "你开始聊修道院的饭菜。聊你养的一只猫。聊隔壁宿舍那个打呼噜像打雷的胖子。"

            "父亲听着，偶尔发出一两声低笑。那种笑很轻，但真实。"

            "你发现了一个技巧——有时候，假装一切正常，反而是最好的安慰。"

            "临走那天，父亲送你到城门口。以前从来没有过。"

            $ hide_all_chars("father_img")
            show father_img at left with dissolve
            father "路上小心。"

            hide father_img with dissolve

            "他的声音平静如常。但他站在那里看你走了很远，很远。你回头看了一眼，他还在。"

    ## ──────────────────────────────────────
    ## 少年深化场景 (14岁街头 → 15岁月夜)
    ## ──────────────────────────────────────

    call prologue_deep_youth_2 from _call_pdy2
    call prologue_deep_youth_3 from _call_pdy3

    ## ──────────────────────────────────────
    ## 少年尾声
    ## ──────────────────────────────────────

    scene black with fade

    "你回到了修道院。"

    "从那以后，父亲的来信越来越少。一个月一封变成两个月一封，再后来是半年。信的内容也越来越短。"

    "'一切安好。用功读书。'"

    "你把每一封都留着。夹在拉丁文语法书的最后几页，那个谁都不会翻的地方。"

    "你开始做噩梦。梦里总是同一个画面：那只金鹰从盾牌上飞下来，越飞越低，翅膀在流血，最终坠入黑暗。"

    "你十五岁了。不再是那个追蒲公英的孩子。"

    scene black with dissolve
    pause 0.5

    jump cinematic_prologue_3


## ════════════════════════════════════════════════════════════
## 过渡动画：少年→青年
## ════════════════════════════════════════════════════════════

label cinematic_prologue_3:
    window hide
    $ quick_menu = False
    $ _dismiss_pause = False
    $ _cin_skip = False

    stop music fadeout 1.5
    scene black
    pause 0.5

    show screen cin_text("三年后。", "你已不再是一个孩子。")
    pause 3.5
    hide screen cin_text with cin_dissolve
    pause 0.5

    play music "audio/music/great_hall.ogg" fadein 2.0
    show screen cin_title(0, "成长", "Coming of Age")
    pause 3.0
    hide screen cin_title with cin_dissolve

    scene bg royal_palace at cin_parallax_left with cin_slow
    show screen cin_overlay
    pause 0.8

    voice "audio/narration/ch0_p3_line1.mp3"
    show screen cin_sub("1343年。十八岁的你已经在王都小有名气。")
    $ wait_voice(7.0)
    hide screen cin_sub

    voice "audio/narration/ch0_p3_line2.mp3"
    show screen cin_sub("名声是一把双刃剑。它吸引盟友，也招来敌人。")
    $ wait_voice(6.0)
    hide screen cin_sub

    voice "audio/narration/ch0_p3_line3.mp3"
    show screen cin_sub("但在他选择自己的道路之前，命运已经替他做出了选择。")
    $ wait_voice(6.0)
    hide screen cin_sub
    hide screen cin_sub

    hide screen cin_overlay
    scene black with cin_slow
    stop music fadeout 1.5
    pause 0.5

    $ _dismiss_pause = False
    $ _cin_skip = False
    $ _dismiss_pause = True
    $ quick_menu = True
    window auto
    jump prologue_adult


## ════════════════════════════════════════════════════════════
## 第三阶段：青年 (18-21岁) — "成长"
## ════════════════════════════════════════════════════════════

label prologue_adult:

    ## 青年期主角肖像
    $ player.image_tag = "player_young"
    $ play_music("audio/music/great_hall.ogg", fadein=2.0)

    call show_chapter("序章·下", "成长", "1343年，王都") from _call_show_chapter_prologue3

    scene bg royal_palace with dissolve
    $ unlock_gallery("bg_royal_palace")

    "十八岁。你从圣安德烈修道院毕业了。"

    "六年的时间。你从一个什么都不懂的领主之子，变成了……一个什么都懂一点但什么都不精的年轻人。"

    "至少你自己是这么觉得的。别人的评价不太一样。"

    "马库斯——你最好的朋友，现在是某位子爵的幕僚——在毕业酒会上搂着你的肩膀说："

    $ hide_all_chars("friend_marcus_img")
    show friend_marcus_img at left with dissolve

    friend_marcus "你知道他们怎么叫你吗？'艾登堡的小鹰'。听着挺威风。不过我觉得你更像只鹌鹑。"

    hide friend_marcus_img with dissolve

    $ hide_all_chars()
    "你踹了他一脚。他笑着躲开了。"

    "毕业之后你没有回家。父亲来信说，让你留在王都'开阔眼界'。你觉得这话后面有别的意思，但你没有追问。"

    "你在王都租了一间小公寓，靠父亲寄来的不多不少的钱过日子。你旁听法庭的审判，去市场学讨价还价，在酒馆里听商人们吹牛。"

    ## ──────────────────────────────────────
    ## 青年深化场景 (19岁赌馆 → 20岁暗夜来客)
    ## ──────────────────────────────────────

    call prologue_deep_adult_1 from _call_pda1
    call prologue_deep_adult_2 from _call_pda2

    "三年。你从一个学生变成了一个——怎么说呢——还算懂事的年轻人。"

    ## ──────────────────────────────────────
    ## 场景1：贵族宴会
    ## ──────────────────────────────────────

    scene bg great_hall with dissolve
    $ unlock_gallery("bg_great_hall")

    "二十一岁。深秋。"

    "你收到了第一张真正重要的请柬——施泰因伯爵夫人的秋季宴会。"

    "在王都，施泰因伯爵夫人的宴会就是社交季的开幕式。能收到请柬本身就是一种认可。你不知道自己是怎么上了名单的——也许是马库斯帮的忙，也许是有人在试探你。"

    "你穿上了最好的一套衣服。不算华丽，但干净整洁。你在镜子前站了五分钟，练习了三遍微笑。"

    "然后你出门了。"

    scene bg great_hall with dissolve

    "宴会大厅亮如白昼。数百根蜡烛在枝形吊灯上燃烧，蜡油的甜腻气味混着香水和烤肉的味道。"

    "到处是人。贵族、骑士、商人、教士——这座大厅是一个微缩的王国。每张笑脸下面都藏着一本账。"

    "你站在入口处，拢了拢衣领。"

    "施泰因伯爵夫人——一个五十多岁的女人，灰色的头发梳得一丝不苟，脸上的皱纹像刻出来的——朝你走来。"

    $ hide_all_chars("countess_hilda_img")
    show countess_hilda_img at left with dissolve

    countess_hilda "艾登堡的小领主。终于见到真人了。"

    "她上下打量你，眼神犀利得像手术刀。"

    countess_hilda "你长得像你父亲年轻的时候。希望你比他聪明。"

    hide countess_hilda_img with dissolve

    $ hide_all_chars()
    "你不知道这是夸奖还是警告。你选择当作夸奖。"

    "她把你介绍给了几个人。你记住了两张脸——"

    "一个是维尔纳公子。金色头发，蓝眼睛，笑起来像阳光。但你注意到他看人的时候从不直视，总是稍微偏一点，像是在看你身后的某样东西。"

    "另一个是冯·哈根男爵的使者。黑衣，寡言，敬酒时酒杯举得比所有人都低。"

    "宴会进行到一半，你面对一个选择——"

    menu:
        "大放异彩。让所有人记住你的名字。":
            $ change_stat("reputation", 5)
            $ change_courage(-5)
            $ prologue_banquet_style = "shine"
            $ log_decision("序章", "宴会上大放异彩", "声望+5，勇气消耗")

            "你决定不当隐形人。"

            "当有人讨论边境局势的时候，你插了嘴。你引用了一段你在修道院学过的古典战例，分析了当前的形势，提出了一个大胆的观点。"

            "大厅安静了几秒。然后施泰因伯爵夫人鼓了一下掌。就一下。但足够了。"

            $ hide_all_chars("countess_hilda_img")
            show countess_hilda_img at left with dissolve

            countess_hilda "年轻人，你有点意思。"

            hide countess_hilda_img with dissolve

            $ hide_all_chars()
            "接下来的一个小时，不断有人走过来跟你搭话。有人夸你，有人试探你，有人只是来看看'那个说大话的年轻人'长什么样。"

            "你喝了太多酒。说了太多话。但你不后悔。"

            "因为当你离开的时候，至少有二十个人记住了你的名字。"

            "当然，其中一些人记住你，不见得是好事。"

        "低调观察。看清楚每个人的底牌。":
            $ change_stat("intrigue", 5)
            $ change_courage(3)
            $ prologue_banquet_style = "observe"
            $ log_decision("序章", "低调观察宴会", "谋略+5")

            "你选择做一个安静的旁观者。"

            "你靠着柱子，端着一杯你几乎没喝的酒，看。"

            "你看到施泰因伯爵夫人跟一个你不认识的枢机主教耳语了什么，对方的脸色变了。"

            "你看到维尔纳公子在跟三个不同的女人调情的间隙，偷偷跟一个信使交换了一张纸条。"

            "你看到冯·哈根男爵的使者一个人坐在角落里，但他的眼睛一直在转——他在数人头。"

            "你还看到一个细节——伯爵夫人的管家在给每位客人续酒的时候，会在某些人的杯子里多倒一点。那些人后来都说了太多话。"

            "你把这一切记在心里。像以前在修道院记笔记一样。"

            "这场宴会，你一个朋友都没交到。但你觉得收获比任何人都大。"

        "结交盟友。你不可能一个人走下去。":
            $ change_stat("loyalty", 5)
            $ change_courage(2)
            $ prologue_banquet_style = "network"
            $ log_decision("序章", "结交盟友", "忠诚+5")

            "你开始走动。"

            "不是毫无目的的闲逛。你选择性地接近某些人——那些看起来不那么显眼，但眼神清醒的人。"

            "你跟一个来自西部的小领主聊了聊领地管理。跟一个军需官讨论了粮食价格。跟一个退休的法官下了半盘棋（你输了，但输得体面）。"

            "这些人不是权贵。但他们是权力机器上的齿轮——不起眼，但不可或缺。"

            "马库斯凑过来，低声说："

            $ hide_all_chars("friend_marcus_img")
            show friend_marcus_img at left with dissolve

            friend_marcus "你在干什么？那些大人物你一个都不搭理。"

            $ hide_all_chars()
            "你说：大人物不缺朋友。"

            "马库斯想了一会儿，笑了。"

            $ hide_all_chars("friend_marcus_img")
            show friend_marcus_img at left with dissolve

            friend_marcus "行。你比我想的聪明。"

            hide friend_marcus_img with dissolve

            "宴会结束的时候，你的口袋里多了五张名片。都不是什么响当当的名字。但在未来的日子里，这五个人中有三个会在关键时刻站在你这边。"

    ## ──────────────────────────────────────
    ## 场景2：父亲的最后一封信
    ## ──────────────────────────────────────

    scene black with fade
    $ play_music("audio/music/night_mystery.ogg", fadein=2.0)

    "宴会之后不久，你收到了父亲的信。"

    "跟以往不同。这封信很长。"

    scene bg study with dissolve

    "你坐在窗边，就着月光读。"

    "'吾儿：'"

    "'写这封信的时候，窗外在下雨。秋天的雨，总让我想起你母亲。她走的那天也是这样的天气。'"

    "'我老了。这个事实比任何敌人都无情。手已经握不稳剑了。前天摔了一跤，膝盖到现在还是肿的。玛尔塔说我该找个大夫，我说不用。大夫治不了老。'"

    "'艾登堡还好。今年收成不错。但边境那边不太平。格雷伯爵和哈根男爵又在争地。我试着调停，但我说话已经不像以前那么管用了。人老了，分量就轻了。'"

    "'有些事我一直想告诉你，但总觉得时候不到。也许永远不会到。所以我把一些东西放在了书房的老地方。你知道是哪里。等你回来的时候，自己去看。'"

    "'别太相信任何人。这话你听了无数遍了。但我再说一遍——别太相信任何人。包括那些看起来对你好的人。尤其是那些看起来对你好的人。'"

    "'你是我这辈子做对的唯一一件事。'"

    "'父。'"

    "你把信读了三遍。"

    "第一遍读内容。第二遍读情绪。第三遍——读恐惧。"

    "这不是一封普通的家书。这是一封遗书。"

    "你攥着信纸，手在发抖。窗外的月亮被云遮住了，房间陷入黑暗。"

    "你想立刻动身回家。但理智告诉你——如果父亲想让你回去，他会直接说。他没说，说明他希望你留在王都。"

    "或者说明——回去已经太危险了。"

    ## ──────────────────────────────────────
    ## 场景3：噩耗
    ## ──────────────────────────────────────

    scene black with dissolve
    $ play_music("audio/music/grief.ogg", fadein=2.0)

    "你给父亲回了信。没有回音。"

    "一个月。两个月。三个月。"

    "你开始每天去驿站问。信使摇头。你开始失眠。开始每天凌晨三点醒来，盯着天花板，直到天亮。"

    "然后，在一个你已经不再抱希望的傍晚——"

    scene bg church_interior with dissolve

    "你正在住处的回廊里读书。"

    "一个信使踉踉跄跄地跑进来。浑身泥泞。眼眶通红。"

    "他跪在你面前。手里攥着一封信，火漆已经碎了。"

    "你不需要打开它。"

    "因为信使的表情已经告诉了你一切。"

    scene black with dissolve

    "你的手指失去了知觉。书卷滑落在地。"

    "回廊的石柱在视线中变得模糊。周围的一切声响——脚步、钟声、风——都沉入了深水之下。"

    "你听到信使的声音，很远，像从另一个世界传来的——"

    "'领主大人……于三日前……薨逝……'"

    "公元1347年。深秋。"

    "你的父亲走了。"

    ## ──────────────────────────────────────
    ## 序章尾声：骑马赶回
    ## ──────────────────────────────────────

    scene black with fade

    "你不记得自己是怎么收拾的行李。不记得是怎么跟王都告的别。不记得马是从哪里借的。"

    "你只记得三天的路程。三天的雨。三天的沉默。"

    "马车里堆满了你从王都带回的行李——几箱书籍、一把剑、一枚父亲年轻时赠你的家族印戒。"

    "你反复摩挲着印戒上那只展翅的金鹰。金属冰冷。不管你怎么捂，它都不会变暖。"

    "远处，灰色的城堡出现在地平线上。丧旗——黑色的旗帜在风雨中沉重地翻卷。"

    "你到家了。"

    "但'家'这个字，从此有了不同的含义。"

    ## ──────────────────────────────────────
    ## 序章结束：属性结算
    ## ──────────────────────────────────────

    scene black with dissolve
    pause 1.0

    $ prologue_completed = True

    "你是 [player_name]。二十二岁。艾登堡的新任领主。"

    "你的童年教会了你什么是失去。"
    "你的少年教会了你什么是选择。"
    "你的青年教会了你什么是孤独。"

    "现在，棋盘已经摆好。"
    "所有人都在等着看你的第一步。"

    scene black with dissolve
    pause 0.5

    ## 衔接第一章
    jump start

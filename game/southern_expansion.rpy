## ============================================================
## 南境游记 DLC — 第一弹《潮汐港的火并》
## ------------------------------------------------------------
## 独立外传：从主菜单进入，自包含小档，不依赖主线进度。
## 设定时点：本传主角治下某年，南境自由港来信求援。
## 完整三幕 + 三结局 + 赛琳恋爱线。
## 专属立绘(赛琳/维斯帕/少年水手/码头工)、专属场景 6 张、专属 BGM 6 首、
## 三幕开场英文配音、成就 + 结局图鉴 + 场景画廊 + 音乐室均已接入。
## ============================================================

## ─── 南境 DLC 专用变量 ───
default southern_visited = False
default southern_quest_stage = 0
default southern_faction = ""              # "pirates" / "guild" / "neutral"
default alliance_pirates = False           # 倒向海盗议会（自由船主联盟）
default alliance_guild = False             # 倒向金锚商人公会
default southern_brokered_peace = False    # 促成停火
default rel_corsair = 0                    # 赛琳好感（-100~100）
default corsair_romance = False            # 赛琳恋爱 flag
default southern_first_impression = ""     # 酒馆初遇时玩家的态度
default southern_united = False            # 第三幕是否促成两派联合
## 第一幕港口初探进度
default explored_dock = False
default explored_market = False
default explored_pier = False
default explored_office_ext = False
default dock_stand = ""                     # 码头事件玩家态度
default fisher_wife_promise = False         # 答应船员之妻打听下落
default broker_rumor_heard = False          # 提前听说"内陆掮客"(费舍尔预埋)
default port_insight = 0                     # 对潮汐港/两派的了解度(0-6)
default explored_guild_ext = False
default explored_oldtale = False
default met_sea_dog = False                  # 酒馆认识船主元老老汉斯
## 第二幕多步调查
default investigate_jail = False
default investigate_ledger = False
default investigate_inn = False
default investigate_office_q = False
default evidence_count = 0                    # 收集到的费舍尔证据数
default fisher_husband_found = False          # 探监见到陈船老大(回收陈嫂线)
default investigate_insider = False
default investigate_faction2 = False
default investigate_together = False
default persistent.southern_dlc_progress = 0
## 南境的 5 个分支结果单独成 set，不混进主线 persistent.endings_seen（避免污染 8 结局图鉴计数）。
## 两个 set 必须保持独立: 本文件存的是裸 key("vassal"/"fall"), 主线也有同名 key,
## 合并会让两边互相点亮。
default persistent.southern_endings_seen = set()

## ─── 并入主线用的状态契约 ───
## southern_from_mainline: 南境是从主线第一章末 call 进来的(True), 还是从章节选择当外传
##   单独进入的(False)。**极性不能反**: 默认 False, 由主线调用方置 True —— 这样老档
##   (停在外传里的)读进来走 default=False → 老收尾 → 与今天逐字一致。反过来写会让老档
##   落进主线返程戏, 然后在空 call stack 上 return 被甩回主菜单。
default southern_from_mainline = False
## southern_outcome: 南境结果对主线的唯一接口。"none"=没去过; "delegated"=出钱不亲自去;
##   其余为五个分支 key(vassal/outwit/free/ruler/fall)。主线只读这一个变量。
default southern_outcome = "none"
## 关系面板守卫(screens_custom.rpy REL_MET_GUARD): rel_corsair 有 29 处 change_rel 却
## 一直没有 met flag, 关系条从不显示。effects.rpy 的 change_rel 会自动由 rel_corsair 推出它。
default corsair_met = False

## ─── 南境 DLC 新角色 ───
## 渡鸦船长赛琳：自由船主联盟话事人之一，精明、盗亦有道，非刻板凶悍海盗
define corsair = Character("赛琳", color="#2e8b8b", image="corsair")
## 金锚公会大执事维斯帕：公会一方代表，复用现有 merchant_guild 立绘
define guild_master = Character("维斯帕执事", color="#b8860b", image="guild_master")
## 港口杂役/水手通用
define dockhand = Character("码头工", color="#8a8a8a", image="dockhand")
define sailor = Character("水手", color="#6a7a8a", image="servant_generic")
## 自称中立的掮客费舍尔——实为王廷密探（第二幕揭）
define broker = Character("掮客费舍尔", color="#8a8a8a", image="noble_werner")
## 海雀号船上的少年水手
define ship_boy = Character("少年水手", color="#a89878", image="ship_boy")
## 第一幕港口初探配角(复用现有立绘，语义贴合)
define old_salt = Character("老船工", color="#7a6a5a", image="old_salt")
define tax_man = Character("公会税吏", color="#8a7a4a", image="soldier_generic")
define fishmonger = Character("鱼贩阿姆", color="#8a8a6a", image="old_woman")
define fisher_wife = Character("船员之妻", color="#c4a882", image="blacksmith_wife")
define harbor_master = Character("港务官", color="#9a8a6a", image="harbor_master")
define sailor_old = Character("老水手", color="#6a7a7a", image="storyteller")
## 断锚酒馆群像
define tavern_keeper = Character("断锚老板", color="#8a7a5a", image="tavern_keeper")
define sea_dog = Character("老汉斯", color="#5a6a7a", image="sea_dog")
## 第二幕调查配角
define chen_captain = Character("陈船老大", color="#6a5a4a", image="chen_captain")
define xiao_liu = Character("学徒小六", color="#a89878", image="stable_boy")
define inn_keeper = Character("客栈老板", color="#8a8a7a", image="servant_generic")
define guild_clerk = Character("公会账房", color="#9a8a6a", image="merchant_karl")
define dissenter = Character("动摇的船主", color="#6a6a5a", image="soldier_generic")
## 第三幕王廷特使 / 主帅
define envoy_royal = Character("王廷特使", color="#7a5a5a", image="soldier_generic")
define royal_admiral = Character("王室主帅", color="#5a4a4a", image="royal_admiral")


## ============================================================
## 入口
## ============================================================

## 兼容别名: 老存档的 call stack / 旧引用仍按这个名字找入口, 保留一个版本周期。
## (既有的 `from _call_X` 子句一个字不许改 —— Ren'Py 存档记的是那个返回点名。)
label southern_dlc_start:
    jump southern_arc_standalone


## ── 入口 A: 独立外传(章节选择的「外章」走这条) ──
## 属性基线留在这里, 与并入主线前的体验逐字一致。
label southern_arc_standalone:

    ## 外传设定在领主治下，主角已立足——给一个已成势的属性基线，
    ## 而非主线开局的新丁数值（否则 intrigue/reputation 门槛选项全为死枝）。
    ## **这个块只属于独立入口**: 从主线 call 进来时绝不能跑, 否则直接抹掉玩家真实属性。
    python:
        power = 50
        wealth = 50
        faith = 45
        loyalty = 50
        reputation = 50
        intrigue = 45

    scene black with fade
    pause 0.5

    centered "{size=+8}南境游记{/size}"
    pause 1.2
    centered "{size=+4}第一弹 · 潮汐港的火并{/size}"
    pause 1.5
    scene black with dissolve

    call southern_arc from _call_southern_arc_standalone
    jump southern_dlc_complete


## ── 入口 B: 正文本体(主线 call 这条; 独立入口也经由上面 call 进来) ──
## **零属性写入** —— 属性由调用方负责。
label southern_arc:

    $ southern_visited = True
    $ quick_menu = True

    ## ── 框架：一封来自南境的信 ──
    play music "audio/music/tension.ogg" fadeout 1.0 fadein 2.0 if_changed

    voice "audio/narration/south_a1_01.mp3"
    "信是奥尔德里克拿进来的。火漆上压着一个你没见过的纹章——一只铁锚，缠着绳。"

    $ hide_all_chars()
    show aldric_img at left with dissolve

    aldric "南边来的，大人。潮汐港。"

    $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img")
    show player_char_img at left with dissolve
    player "潮汐港？那不是个不归王国管的港口吗。"

    $ hide_all_chars("aldric_img", "corsair_img", "ship_boy_img", "dockhand_img", "servant_generic_img", "soldier_generic_img", "merchant_karl_img", "blacksmith_wife_img", "farmer_rep_img", "old_woman_img", "noble_werner_img", "stable_boy_img", "storyteller_img")
    show aldric_img at left with dissolve
    aldric "正是因为不归王国管，他们才会来找您而不是找王廷。"

    aldric "信里说，港口里两伙人打起来了。金锚公会和那些……船主。他们封了码头。"

    "你接过信。字写得急，墨迹有几处晕开——像是边写边有人在催。纸的边角还沾着一点暗褐，不知是酒渍，还是别的什么。这封信送出来的时候，潮汐港大概已经不太平了。"

    "落款是港务厅，但盖的是公会的章。"

    $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
    show player_char_img at left with dissolve
    player "这跟艾登堡有什么关系？"

    $ hide_all_chars("aldric_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
    show aldric_img at left with dissolve
    aldric "大人，艾登堡的盐，三成走南境海路。铁器的好钢，也是。"

    aldric "潮汐港停一个月，您冬天就得拿木柴腌肉。"

    "你心里算了下府库的存盐。撑不到开春。盐这东西，平日没人想得起它，可一旦断了，腌不了肉、留不住鱼，一整个冬天的口粮都得跟着遭殃。一个内陆领主的命脉，竟系在千里之外一个不归他管的港口上——这道理，今天才嚼出味来。"

    $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
    show player_char_img at left with dissolve
    player "备马。不，备船。"

    "盐路断不得，这是其一。其二，你隐隐觉得，一个连王廷都管不着的自由港闹出的乱子，背后未必只是两伙生意人抢地盘那么简单。"

    $ hide_all_chars("aldric_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
    show aldric_img at left with dissolve
    aldric "……我这把老骨头，怕是要在甲板上吐三天。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "那就留下看家。我自己去。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "那不行。您一个人去那种地方，我夜里睡不着。"

    aldric "老臣这把年纪，吐三天还能爬起来。可您要是在那港口出了岔子，老臣就算把这把骨头吐散了，也没脸回去见艾登堡的列祖列宗。"

    "他还是收拾了行李。第二天天没亮，你们就上了路。"

    "先是六天陆路，翻过两道山，到王国南边的海港城换船。再往南，就出了王国的地界。"

    "海船摇摇晃晃。奥尔德里克果然在甲板上吐了三天，吐到后来连胆汁都没了，还硬撑着替你打理文书。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "大人……老臣这辈子，再不想见海了。"

    aldric "不过您这一趟值当。艾登堡的盐铁断不得。再说，能让您亲自跑这么远的事，多少年没有过了。"

    "你站在船头，看海一点点变蓝、变深。越往南，水越暖，风里的味道越陌生。"

    "第七天清晨，瞭望的水手喊了一声。天海交界处浮起一片密匝匝的桅杆，像从海里长出来的秃林——潮汐港，到了。"

    $ hide_all_chars()
    pause 0.5
    scene black with dissolve


    ## ============================================================
    ## 第一幕 · 抵港
    ## ============================================================

    play music "audio/music/southern_port.ogg" fadeout 1.5 fadein 2.0 if_changed

    scene bg tideport_beach with fade
    pause 0.3

    voice "audio/narration/south_a1_02.mp3"
    "海风先到。咸的，还带着鱼和焦油的味道。这味道跟艾登堡的全然不同——内陆的风里是泥土和炊烟，这里的风，是一整片活着的、躁动的海。"

    voice "audio/narration/south_a1_03.mp3"
    "你这辈子没见过这么多船。桅杆挤在一起，像一片被砍秃了的林子。"

    show aldric_img at left with dissolve

    aldric "到了。这就是潮汐港。"

    aldric "老臣年轻时押过一趟货来这儿，那会儿这港口就乱，可乱里有活气。如今再看……这活气底下，压着一口憋着的气。要出事。"

    "远处的码头拉着铁链，几艘船横在港口入口。没人卸货，也没人出海。"

    "对一个靠海吃饭的港口，封港就是断气。货堆在仓里发霉，鱼烂在舱里发臭，靠工钱过活的人，一天比一天眼神发慌。"

    aldric "您看那边——链子锁着码头。封港了。"

    "岸上的人不少，可没人忙活。他们三三两两站着，手都揣在怀里。揣着什么，你不想猜。"

    "你在艾登堡见惯了战前的村庄——也是这副样子。人还在，活气却抽走了，剩下一具空壳，等着不知什么时候落下来的那一刀。一个港口能憋成这样，绝不是一天两天的事。"

    scene bg tideport_harbor with dissolve

    "你们沿着栈道往里走。木板被海水泡得发黑，每一步都黏脚。"

    $ hide_all_chars("dockhand_img")
    show dockhand_img at right with dissolve
    dockhand "外乡人？挑日子来的不巧。"

    "一个码头工挡了一下路，又自己让开了。他看了眼你腰间的印戒。"

    dockhand "内陆来的贵人。来收账还是来送死？"

    $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img")
    show player_char_img at left with dissolve
    player "来谈事的。"

    dockhand "那更得小心。这港口现在，谈事比动刀危险。"

    "他啐了一口，走了。临走还回头看了你一眼，那眼神里没有恶意，只有一种见多了倒霉事的麻木——又一个不知死活、往火坑里跳的外乡人。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "大人，我们先找个地方落脚，打听清楚再说。"

    aldric "前头有家酒馆，叫'断锚'。船上人聚的地方，打听消息的好去处。"

    aldric "不过趁天还没全黑，大人想先在港里自己转转也使得。眼见的，比耳听的实在。"

    jump southern_explore_loop


## ============================================================
## 第一幕 · 港口初探（可选走访，看够了去断锚）
## ============================================================

label southern_explore_loop:
    $ hide_all_chars()
    scene bg tideport_harbor with dissolve

    if port_insight == 0:
        "潮汐港不讲你熟悉的那套规矩。没有城墙，没有领主的旗，只有海、船，和挤在岸边讨生活的人。"
        "天快黑了。趁最后一点光，你想自己看看这港口到底是怎么回事。"

    menu:
        "到码头，看公会怎么收税" if not explored_dock:
            jump southern_explore_dock
        "去鱼市，听市井怎么说" if not explored_market:
            jump southern_explore_market
        "走到栈桥尽头，看那条被扣的船" if not explored_pier:
            jump southern_explore_pier
        "去港务厅外，探探官面上的口风" if not explored_office_ext:
            jump southern_explore_office
        "去金锚公会大楼外，看看公会的家底" if not explored_guild_ext:
            jump southern_explore_guild
        "找个老水手，听潮汐港的来历" if not explored_oldtale:
            jump southern_explore_tale
        "看够了，去断锚酒馆":
            jump southern_to_tavern


label southern_explore_dock:
    $ explored_dock = True
    $ port_insight += 1
    "码头上，一队挂着金锚徽记的人围住了一条刚靠岸的渔船。"

    $ hide_all_chars("soldier_generic_img")
    show soldier_generic_img at right with dissolve
    tax_man "两成。渔获抽两成，按公会的规矩。船和人，都登记。"

    $ hide_all_chars("farmer_rep_img", "soldier_generic_img")
    show old_salt_img at left with dissolve
    old_salt "两成？我一船鱼刨去本钱剩不下几个铜板。我打了四十年鱼，从没人管我登不登记！"

    tax_man "从前没有，现在有了。不服，这泊位你别使。"

    "老船工的手在抖。不是怕，是气的。可他到底没再顶——身后那条破船，是一家老小的活路。"

    menu:
        "出面替老船工说话（声望）":
            $ dock_stand = "people"
            $ change_stat("reputation", 4)
            $ change_rel("rel_corsair", 3)
            $ hide_all_chars("player_char_img", "soldier_generic_img")
            show player_char_img at left with dissolve

            player "两成的税，立在哪条律上？拿出来我看看。"

            tax_man "你又是谁？"

            player "一个看不惯仗着人多欺负老实人的过路人。这税要是有章程，你拿章程；没有，就是抢。"

            "你没亮领主的身份。可你站的姿势、说话的腔调，让那税吏迟疑了。围观的人多了起来——在这种地方，人多，有时候比刀管用。"

            tax_man "……今天先这样。老东西，下回带齐了。"

            "公会的人散了。老船工要给你磕头，被你扶住。"

            $ hide_all_chars("old_salt_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
            show old_salt_img at left with dissolve
            old_salt "外乡人，记着断锚酒馆。往后你在潮汐港有难处，报老周的名字，使得。"

        "塞税吏几个钱，替老船工把这关过了（财富）":
            $ dock_stand = "money"
            $ change_stat("wealth", -3)
            $ change_stat("reputation", 2)
            $ hide_all_chars("soldier_generic_img")
            show soldier_generic_img at right with dissolve

            "你不动声色，把一小袋银币塞进税吏手里。"

            tax_man "……老东西今天走运。下回可没这好事。"

            "老船工冲你拱了拱手，没敢出声。今晚他这船鱼，总算能卖出去了。"

        "什么都不做，只在一旁看清公会的手段（谋略）":
            $ dock_stand = "watch"
            $ change_stat("intrigue", 3)

            "你没动。你想先看清这港口的规矩是怎么运转的。"

            "税吏抽了两成，登记了船和人，临走还踢翻了老船工的一筐鱼。鱼撒了一地，老船工蹲下去，一条一条捡。"

            "你看清了公会的'秩序'是怎么立起来的。"

    jump southern_explore_loop


label southern_explore_market:
    $ explored_market = True
    $ port_insight += 1
    scene bg tideport_harbor with dissolve
    "鱼市在码头西头。腥气、吆喝、讨价还价，比别处都热闹——封港封得了船，封不了人要吃饭。"

    $ hide_all_chars("old_woman_img")
    show old_woman_img at right with dissolve
    fishmonger "外乡人？看你这身料子就不是海边的。买鱼啊？今早的，新鲜。"

    $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img")
    show player_char_img at left with dissolve
    player "不买鱼。打听点事。这港口，怎么就闹成这样了？"

    $ hide_all_chars("old_woman_img", "player_char_img", "player_young_img", "player_teen_img", "player_child_img", "aldric_img", "guild_master_img", "old_salt_img", "sea_dog_img", "chen_captain_img", "blacksmith_wife_img")
    show old_woman_img at right with dissolve
    fishmonger "嗨，还能因为啥。金锚那帮人想当爹呗。"

    fishmonger "我跟你说句良心话——公会也不全是坏。早些年这港没人管，今天你的船被劫，明天他的货被抢，乱得很。公会立起来，好歹有个说理的地方。"

    fishmonger "可这两年，他们胃口越来越大。抽税、登记、放贷……说是立规矩，立着立着，规矩就成了他们一家的。"

    "她麻利地给一条鱼开膛，话没停。"

    fishmonger "船主那帮人也不是省油的。一个个认死理，认人不认章，翻起脸来照样动刀。两边斗，遭殃的是我们这些卖鱼的、扛包的。"

    menu:
        "潮汐港三百年没有王法，是怎么撑下来的？":
            $ change_stat("intrigue", 2)
            fishmonger "靠海呗。这港口卡在三条海路的口子上，盐、香料、好钢，南来北往都得打这过。"

            fishmonger "钱多的地方，谁都想要，可谁也独吞不下——王国要它，别的城邦也要它。谁伸手太狠，别人就联手掐他。三百年就这么平衡下来的。"

            fishmonger "所以这港谁也不属于。它就属于它自己。这话你记着，往后用得上。"

        "最近港里，有没有什么外来的生面孔？":
            $ broker_rumor_heard = True
            $ change_stat("intrigue", 2)
            fishmonger "你这么一问……还真有。前阵子来了个掮客，说话软乎乎的，内陆口音。"

            fishmonger "公会那边见他，船主那边也见他，两头跑。说是帮人牵线搭桥。"

            fishmonger "我这卖鱼的看不懂那些门道。可你说怪不怪——他一来，港里的火药味就重了。"

            "你把这句话记在了心里。一个两头跑的掮客，和一场越烧越旺的火。也许是巧合。"

    jump southern_explore_loop


label southern_explore_pier:
    $ explored_pier = True
    $ port_insight += 1
    scene bg tideport_beach with dissolve
    "栈桥尽头，一条三桅船被铁链锁在死角。船身吃水浅，浮得高——空船。船头漆着两个褪色的字：海雀。"

    "这就是点着这场火的那条船。公会说它走私，扣了船，押了人。"

    $ hide_all_chars("blacksmith_wife_img")
    show blacksmith_wife_img at right with dissolve
    "船边坐着个女人，怀里搂着个睡着的孩子。她望着那条船，像望着一座坟。"

    fisher_wife "您是……来看船的？还是来看热闹的？"

    $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img")
    show player_char_img at left with dissolve
    player "路过。这船上的人呢？"

    $ hide_all_chars("blacksmith_wife_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
    show blacksmith_wife_img at left with dissolve
    fisher_wife "被公会带走了。我男人是海雀号的水手。带走那天起，二十多天，活不见人。"

    fisher_wife "公会说他们走私军火。军火？您看那船——空的。我男人这辈子运过最危险的货，是一船腌咸鱼。"

    "她没哭。眼睛是干的，干得发红。"

    menu:
        "答应她，帮忙打听被扣船员的下落":
            $ fisher_wife_promise = True
            $ change_stat("reputation", 3)
            $ change_rel("rel_corsair", 4)
            $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
            show player_char_img at left with dissolve
            player "我在这港口有几个能说上话的人。你男人的下落，我替你问。"

            $ hide_all_chars("blacksmith_wife_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
            show blacksmith_wife_img at left with dissolve
            fisher_wife "外乡人，您别空许愿。这港里许愿的人多，应的人少。"

            $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
            show player_char_img at left with dissolve
            player "我应了，就不是空的。"

            "你不知道自己为什么对一个素不相识的妇人许这个诺。也许是她那双干得发红的眼睛，也许是她身上那股你在艾登堡的难民身上见过太多次的东西——走投无路的人，最后只剩一点不敢相信的指望。这种指望，你见不得它落空。"

            "她看了你很久，到底把那点不敢信的希望，小心收了起来。"

            $ hide_all_chars("blacksmith_wife_img")
            show blacksmith_wife_img at left with dissolve
            fisher_wife "海雀号的船老大姓陈。还有个半大孩子，叫小六，是船上学徒——要是您见着他，告诉他婶儿还等着他。"

            "你记下了。陈船老大，学徒小六。这两个名字，往后会有用。"

        "只问清楚情况，不轻易许诺":
            $ change_stat("intrigue", 2)
            $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
            show player_char_img at left with dissolve
            player "我不能答应你什么。但你说的，我记下了。"

            $ hide_all_chars("blacksmith_wife_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
            show blacksmith_wife_img at left with dissolve
            fisher_wife "……也对。会说话的人，都不轻易应承。"

            "她转回头，继续望着那条空船。你转身离开时，听见她很轻地哼起一支调子——大概是哄孩子的，也大概是哄她自己的。那调子你不认得，是南海一带船家的小曲，缠绵又苍凉，像浪一遍遍拍着礁石，不急不缓，却把石头都磨圆了。"

    jump southern_explore_loop


label southern_explore_office:
    $ explored_office_ext = True
    $ port_insight += 1
    scene bg tideport_harbor with dissolve
    "港务厅在港口正中，一栋石头楼，比周围的木屋气派得多。门口挂着金锚的旗——这地方早被公会拿住了。"

    "你没进去。一个穿官服的人正从里头出来，是港务官。"

    $ hide_all_chars("noble_werner_img")
    show harbor_master_img at right with dissolve
    harbor_master "这位面生。港务厅今日不办公——封港期间，一切照公会的章程来。"

    $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img")
    show player_char_img at left with dissolve
    player "我不是来办事的。只想问问，这港口的乱子，官面上打算怎么收场？"

    $ hide_all_chars("harbor_master_img", "player_char_img", "player_young_img", "player_teen_img", "player_child_img", "aldric_img", "guild_master_img", "old_salt_img", "sea_dog_img", "chen_captain_img", "blacksmith_wife_img")
    show harbor_master_img at right with dissolve
    harbor_master "收场？外乡人，这港三百年没有'官面'。我这港务官的印，盖谁的章，看谁的拳头硬。"

    harbor_master "如今公会拳头硬，我就盖公会的章。哪天换了人，我盖别人的。我这把位子，得活到下个月才行。"

    "圆滑得滴水不漏。但你听出了点别的——他话里没底气，像个知道大祸将至、却只想撑过今天的人。"

    menu:
        "试探：是不是有人在背后推着两边斗？（谋略）" if broker_rumor_heard or intrigue >= 45:
            $ change_stat("intrigue", 3)
            $ broker_rumor_heard = True
            player "公会和船主，斗了不是一天两天。可这火，是最近才烧旺的。是不是有人在添柴？"

            "港务官的眼神动了一下。很快，但你看见了。"

            harbor_master "……外乡人，有些话，知道得越多越短命。"

            harbor_master "我只提醒你一句：这港里最近多了张生面孔，比你还会问问题。你要是聪明，离他远点。"

            "他不肯再说。可'生面孔''会问问题'——和鱼市听来的掮客，对上了。"

        "直接问：你觉得这港口还撑得住吗？":
            $ change_stat("reputation", 1)
            harbor_master "撑不撑得住，不是我说了算。"

            harbor_master "我只知道一条：港口要是自己先乱透了，外头惦记它的人，就有借口伸手了。到那天，公会、船主，谁都落不着好。"

            "这话说得隐晦，却比方才任何一句都重。你记住了。"

    jump southern_explore_loop


label southern_explore_guild:
    $ explored_guild_ext = True
    $ port_insight += 1
    scene bg tideport_harbor with dissolve
    "金锚公会的大楼立在港口正中，三层石砌，比周围的木屋高出一截。门口两尊石锚，门楣上鎏金的徽记，老远就晃眼。"

    "你没进去，只在门外看。可光是门外这一会儿，就够你掂出公会的分量。"

    "一队护航的汉子正列队出操，刀枪齐整，喊号子的声音整齐划一——比港里那些散漫的船主，活像两个世界的人。"

    "账房的伙计抱着册子进进出出。放贷处门口排着长队，队伍里大半是面带难色的船主。"

    $ hide_all_chars("servant_generic_img")
    show servant_generic_img at right with dissolve
    "一个公会差役瞥见你张望，皮笑肉不笑地凑过来。"

    servant "这位贵客面生。来存货，还是来借贷？金锚公会，童叟无欺。"

    $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img")
    show player_char_img at left with dissolve
    player "随便看看。你们公会，倒是好大的家业。"

    $ hide_all_chars("servant_generic_img", "player_char_img", "player_young_img", "player_teen_img", "player_child_img", "aldric_img", "guild_master_img", "old_salt_img", "sea_dog_img", "chen_captain_img", "blacksmith_wife_img")
    show servant_generic_img at right with dissolve
    servant "那是。这港口三百年没个管事的，是公会把它从烂泥塘里拽出来的。如今有规矩、有秩序——这秩序可不是天上掉的，是真金白银砸出来的。"

    "你没接话。砸出来的秩序，砸的是谁的钱、谁的活路，他没说。可你心里有数了。"
    jump southern_explore_loop


label southern_explore_tale:
    $ explored_oldtale = True
    $ port_insight += 1
    scene bg tideport_beach with dissolve
    "栈桥边，一个晒得黝黑的老水手盘腿补网。你递过去一壶酒，他眼睛就亮了。"

    $ hide_all_chars("storyteller_img")
    show storyteller_img at right with dissolve
    sailor_old "想听潮汐港的事？那可有的说了。"

    sailor_old "三百年前，这儿是块没人要的烂滩。后来海路通了，盐、香料、好钢，南来北往都打这过。钱多的地方，苍蝇就多。"

    sailor_old "王国想要它，东边的城邦想要它，海那头的几个汗国也想要它。谁伸手，别人就联手剁他的手。剁来剁去谁也吞不下，这港口就自由了三百年。"

    $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img")
    show player_char_img at left with dissolve
    player "三百年没人吞得下。那现在呢？"

    "老水手往北边王国的方向努了努嘴，压低了声。"

    $ hide_all_chars("storyteller_img", "player_char_img", "player_young_img", "player_teen_img", "player_child_img", "aldric_img", "guild_master_img", "old_salt_img", "sea_dog_img", "chen_captain_img", "blacksmith_wife_img")
    show storyteller_img at right with dissolve
    sailor_old "现在那位北边的，胃口养肥了。听说在憋什么大招——想找个由头，名正言顺地把这港咽下去。"

    sailor_old "外乡人，我看你也是内陆来的。劝你一句：这港口的水，比海还深。沾上了，未必抽得出脚。"

    "一个补网的老水手，话里藏着比港务官还重的东西。你把'北边憋大招''找由头'这几个字，记在了心里。"
    jump southern_explore_loop


label southern_to_tavern:
    $ hide_all_chars()

    if port_insight >= 1:
        "天彻底黑了。白天在港里看的那些，夜里的酒馆该有人能给你说道说道。该去断锚了。"

    ## ── 去酒馆路上：aldric 的提点（块20）──
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "大人，老臣有句话，不知当讲不当讲。"

    $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img")
    show player_char_img at left with dissolve
    player "你我之间，几时还要这套。说。"

    $ hide_all_chars("aldric_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
    show aldric_img at left with dissolve
    aldric "这潮汐港水太浑。公会、船主、港务厅，背后还藏着您没看清的东西。"

    aldric "您是艾登堡的领主。盐路要紧，可您的命，比那条盐路要紧一万倍。"

    aldric "老臣伺候过您父亲，又看着您长大。您父亲当年，就是太想把每件事都做对，才……"

    "他没说下去。父亲的死，是你们之间从不轻易碰的伤口。"

    aldric "老臣只盼这一趟，您能囫囵着回去。盐路丢了能再挣，您要有个闪失，艾登堡就真塌了。"

    menu:
        "我有分寸。但有些事，看见了就不能装没看见":
            $ change_stat("reputation", 1)
            $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
            show player_char_img at left with dissolve
            player "放心，我有分寸。可这港口里那些被欺负的人，我既然看见了，就不能装没看见。这是你教我父亲、我父亲教我的。"
            "奥尔德里克怔了怔，浑浊的老眼里有什么动了一下。"
            $ hide_all_chars("aldric_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
            show aldric_img at left with dissolve
            aldric "……是老臣多嘴了。您比老臣想的，更像您父亲。"

        "你说得对，我会先顾着自己":
            $ change_stat("intrigue", 1)
            $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
            show player_char_img at left with dissolve
            player "你说得对。这趟我先把自己摘干净，不该蹚的浑水，不蹚。"
            $ hide_all_chars("aldric_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
            show aldric_img at left with dissolve
            aldric "这就对了。留得青山在，往后有的是机会。"

    "你们一前一后往断锚走去。夜里的港口，灯火稀稀落落，像撒在黑布上的几粒火星。"

    scene black with dissolve


    ## ============================================================
    ## 第一幕 · 断锚酒馆 · 初遇赛琳
    ## ============================================================

    play music "audio/music/southern_tavern.ogg" fadeout 1.5 fadein 1.5 if_changed

    scene bg tideport_tavern with fade
    pause 0.3

    "酒馆里比外头活络。火光、烟、湿羊毛和烈酒的味道。一个角落有人在掷骰子，另一个角落有人在低声谈一笔不能见光的买卖。"

    "墙上钉满了破旧的航海图，桌椅是用旧船板钉的，连吊灯都是几盏废弃的船灯。这地方像一条搁浅的船，停在岸上，装着一肚子下不了海的人。"

    "你刚找了张桌子坐下，老板就凑了过来。生面孔在这种地方，要么是肥羊，要么是麻烦——他得先掂量你是哪种。"

    $ hide_all_chars("merchant_karl_img")
    show tavern_keeper_img at right with dissolve
    tavern_keeper "喝点什么？丑话说前头：断锚不赊账，不管闲事，进了门各人管各人的嘴。"

    $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img")
    show player_char_img at left with dissolve
    player "一壶你们这儿最不上头的。再问件事——这港口闹成这样，你怎么看？"

    $ hide_all_chars("tavern_keeper_img", "player_char_img", "player_young_img", "player_teen_img", "player_child_img", "aldric_img", "guild_master_img", "old_salt_img", "sea_dog_img", "chen_captain_img", "blacksmith_wife_img")
    show tavern_keeper_img at right with dissolve
    tavern_keeper "我一个开酒馆的，两边的钱都收，两边的话都不接。"

    "他给你斟上酒，声音压低了些。"

    tavern_keeper "不过看你是外乡人，提醒你一句：这屋里左边那几桌是船主的人；右边角落闷头喝酒那两个，是公会的眼线。你坐当中，最稳妥。"

    tavern_keeper "断锚这名字怎么来的？我这条腿，早年就断在公会跟船主的一场火并里。打那天起，我这店谁的边都不站。"

    menu:
        "公会和船主，你觉得谁占理？":
            $ change_stat("intrigue", 1)
            $ broker_rumor_heard = True
            tavern_keeper "这港口讲理的没几个。公会有钱有港务厅，规矩是他们定的；船主有船有刀，认人不认章。一个想当爹，一个不认爹。"
            tavern_keeper "可这回邪门。这回的火烧得太旺，旺得不像两家自己斗出来的——倒像有人在底下成心添柴。"

        "那场火并，断锚为什么遭了殃？":
            $ change_stat("reputation", 1)
            tavern_keeper "火并的时候，谁管你一个开酒馆的？刀剑不长眼。"
            tavern_keeper "所以我劝你，这趟浑水能不蹚就别蹚。两边斗起来，最先倒霉的，永远是夹在当中的人。"

    "你正要再问，靠窗一桌有人扬声招呼你。"

    $ hide_all_chars("soldier_generic_img", "merchant_karl_img")
    show sea_dog_img at left with dissolve

    if dock_stand == "people":
        sea_dog "嘿，内陆来的。过来喝一杯。"
        sea_dog "白天在码头替老周出头那一下，我可看见了。肯替我们海上人撑腰的贵客，稀罕。"
    else:
        sea_dog "嘿，内陆来的。一个人坐当中喝闷酒，不像来谈生意的，倒像来看戏的。过来。"

    $ met_sea_dog = True
    "招呼你的是个独眼老头，脸上的褶子像被海风刻出来的。面前三个空酒碗，人却清醒得很。"

    sea_dog "老汉斯，跑了一辈子船。如今在船主联盟里，算半个说得上话的老骨头。"

    $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img")
    show player_char_img at left with dissolve
    player "汉斯船长。这港口的事，你怎么说？"

    $ hide_all_chars("sea_dog_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
    show sea_dog_img at left with dissolve
    sea_dog "怎么说？公会要掐死我们。"

    sea_dog "从前交一笔泊费，进出自由，海上的事海上人自己了。如今他们要抽两成、要登记、要每条船报备货色航线——"

    sea_dog "你懂这意思吗？哪天哪条船能出海、能装什么，都得他们点头。海上人没了自由的海，跟拴起来的狗有什么两样？"

    "他抓起酒碗又放下。"

    sea_dog "上个月海雀号被扣，就是因为不肯登记。一船腌咸鱼，他们咬定是军火。人抓走二十多天，活不见人。"

    if fisher_wife_promise:
        $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
        show player_char_img at left with dissolve
        player "海雀号……陈船老大，还有个叫小六的学徒。我答应了陈嫂，替她打听下落。"
        $ hide_all_chars("sea_dog_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
        show sea_dog_img at left with dissolve
        sea_dog "你连这都问到了？"
        $ change_rel("rel_corsair", 4)
        "他重重一巴掌拍在你肩上，差点把你从凳子上拍下去。"
        sea_dog "好。内陆来的，你这份心，老汉斯记下了。"
    else:
        sea_dog "你要是真想弄明白这港口的事，海雀号那条线，值得查。"
        $ broker_rumor_heard = True

    sea_dog "渡鸦今晚多半也来。她是我们这边话事的，比我这老骨头有用。你要谈，跟她谈。"

    "你正要再问，门口忽然一阵安静。"

    $ hide_all_chars()
    "进来一个女人。她不高，可整间屋子的目光都往她身上落——然后又赶紧移开。"

    show corsair_img at right with dissolve

    "她外套的下摆湿了一圈，靴子上沾着没干的盐渍。腰上挂着一把弯刀，刀鞘磨得发亮，那是常拔的痕迹。"

    "她个子不高，可走进来的那一刻，满屋子掷骰子的、谈买卖的、喝闷酒的，声音都低了半度。这种安静，不是怕，是敬——在这片认拳头的港口，能让人不动声色就矮三分的，没几个。"

    "她扫了一圈，目光在你这张生面孔上停了半秒，又收了回去。她走到吧台，敲了两下。"

    corsair "老样子。还有，那桌内陆来的——他们的账记我头上。"

    "她没回头，却显然是说你。整间酒馆的目光，又一次悄悄聚到你这桌——一个连渡鸦都肯替他付账的外乡人，到底是什么来头。在这个最不缺眼睛的港口，你刚落脚，就成了被掂量的对象。"

    menu:
        "起身道谢，自报家门":
            $ southern_first_impression = "polite"
            $ change_rel("rel_corsair", 8)
            $ hide_all_chars("corsair_img")
            show player_char_img at left with dissolve

            player "多谢。在下艾登堡领主[player_name]。敢问恩人名号？"

            "她这才转过身，挑了挑眉。"

            corsair "领主。真稀奇，王国的贵人肯站起来跟我说话。"

            corsair "我见过的内陆贵人，要么把我们当海寇防着，要么把我们当傻子哄着。肯正眼看我们一回的，你是头一个。"

            corsair "赛琳。这港口里，他们叫我渡鸦。"

            "渡鸦。乌鸦的一种，跟着死人和战场走。你不知道这名号的来历，可光听这两个字，就知道顶着它的人，手上不会太干净，心里也不会太软。"

            corsair "至于恩人——一杯酒的事，别记太重。我只是不喜欢看人挨宰。"

            "她说得轻巧，可你注意到，整间酒馆里被公会眼线盯着的那桌内陆人，只有你这一桌，她替你挡了。这港口里替人出头的人不多，她偏偏是其中一个。"

        "不动声色，先看她想做什么":
            $ southern_first_impression = "wary"
            $ change_rel("rel_corsair", 3)

            "你没动。一杯来路不明的酒，背后总挂着价钱。你想先看清这价钱是什么。打小看着你爹待客，你记住一件事：笑着端上来的东西，底下多半有钩子。"

            "她端着酒走过来，自己拉开你对面的椅子坐下。这一坐，满屋子的目光又活络起来——渡鸦肯跟谁同桌，在这港口，本身就是一种态度。你还没开口，就被她拽进了局里。"

            show player_char_img at left with dissolve

            corsair "聪明。换我也不喝陌生人的酒。在这港口活到现在，靠的就是这点谨慎。"

            corsair "赛琳。渡鸦。这港口里没几个内陆人敢这么稳地坐着——你要么是有底气，要么是不知道自己踩进了什么。"

            "她说话时一直盯着你的眼睛。那是一种在刀口上讨了多年生活的人才有的目光，能在一瞬间把对面的人称出几斤几两。被这样的目光打量，多数人会心虚地移开眼。你没有。这一点，她记下了。"

            player "那要看你接下来想说什么。"

            "她打量了你一会儿，像在重新估算你这个人的斤两。能稳稳坐在这种地方、还敢这么跟她说话的内陆人，她大概没见过几个。"

            corsair "我喜欢这话。"

            "她举起酒碗，跟你的碰了一下。酒是港里最劣的那种，辣得喉咙发烧，可她喝得痛快。你忽然觉得，跟这样一个不绕弯子的人打交道，比跟维斯帕那种笑里藏刀的，要省心得多——也危险得多。"

        "直接问她：封港是不是你们干的":
            $ southern_first_impression = "blunt"
            $ change_rel("rel_corsair", -3)
            $ change_rel("rel_corsair", 6)

            "你没绕。"

            show player_char_img at left with dissolve

            player "码头上的铁链，是你们船主联盟锁的吗？"

            "酒馆里近处几桌的声音低了下去。她端酒的手停在半空，看了你一会儿，笑了。"

            corsair "开门见山。我喜欢，也讨厌。"

            corsair "喜欢，是省得绕弯子。讨厌，是这种人往往不知道什么时候该闭嘴——在这港口，话问得太直，是会少几颗牙的。"

            corsair "链子不是我们锁的，是公会锁的。他们说要'保护港口秩序'。"

            corsair "可你这么问，说明你已经听了一边的话——多半是公会那张嘴。他们最会把锁链说成秩序。坐下，听听另一边的。"

            corsair "赛琳。渡鸦。坐。"

    $ hide_all_chars("corsair_img")
    show corsair_img angry at right with dissolve

    ## ── 赛琳交代局势 ──
    corsair "我猜你是冲着海路来的。盐、铁、好钢——内陆领主能为这些跑这么远，不奇怪。"

    $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img")
    show player_char_img at left with dissolve
    player "码头封一天，我冬天就难过一分。我想知道这港口到底出了什么事。"

    player "我不爱听一面之词。你说你的，回头我自会去看公会怎么说。两边的话都听了，我才好拿主意。"

    corsair "倒是个谨慎人。行，那我把话说在前头，省得你回头怪我没提醒。"

    corsair "出了什么事？金锚公会想把整个港口攥进自己手里。"

    corsair "他们控制码头、定价、放贷。以前我们这些船主交一笔泊费，进出自由。现在他们要抽两成货，还要登记每一票买卖。"

    corsair "登记。你懂这两个字在港口意味着什么吗——意味着以后哪条船能出海，由公会说了算。"

    corsair "我有个兄弟，跑了二十年盐。就因为得罪了公会的人，登记册上被划了个记号，从此条条航线都'恰好'有人比他先到。半年，他赔光了船。"

    corsair "公会不杀人。公会让你慢慢饿死，还得谢它给你立了规矩。"

    corsair "上个月,有条船不肯登记。公会说它'走私',扣了船,人到现在没放。我们去要人,他们就锁了码头,说是我们先动的手。"

    corsair "所以现在港口里两伙人对着干。他们有港务厅和钱，我们有船和刀。"

    corsair "你大概在想，有钱有官的，迟早赢。多半是。可我们这些海上人，认死理：宁可堂堂正正沉进海里，也不跪着在他们的册子上画押。"

    "她喝了一口，把杯子搁下。那只手骨节分明，虎口有常年握刀磨出的硬茧，可端杯子的姿势又意外地稳——一个能动刀，也能掌舵的人。"

    corsair "你来得正好，也来得正不是时候。"

    corsair "正好——你是个体面人，肯坐下来听两边说话。这港口里，体面人不多。"

    corsair "不是时候——你来这几天，正是这锅水要烧开的时候。一脚踩进来，想干净抽身，难了。"

    corsair "公会那边的大执事，维斯帕，今晚就想见你。他们消息比海鸥还灵。"

    corsair "你前脚进港，后脚他就知道了。这港口里没有秘密——至少对掏得起钱买消息的人来说，没有。所以你最好想清楚，要跟这样的人，站一边，还是站对面。"

    pause 0.3


    ## ============================================================
    ## 第一幕 · 维斯帕登场
    ## ============================================================

    "话音没落，酒馆的门又开了。这次进来的人不一样——绸面的外袍，干燥的靴子，身后跟着两个不像水手的随从。"

    "船主进酒馆，靴子是湿的，手是糙的。这人不一样：他的靴子从没沾过海水，手白净得像没碰过缆绳。在这满是咸腥味的屋子里，他身上那股熏香，格格不入，却又理直气壮。"

    $ hide_all_chars("corsair_img", "guild_master_img")
    show corsair_img at right with dissolve
    show guild_master_img at left with dissolve

    corsair "说曹操。"

    guild_master "渡鸦船长。又在用酒收买人心。"

    guild_master "还有这位——艾登堡的领主。久仰。金锚公会大执事，维斯帕。"

    "他对你欠了欠身，礼数周到，眼睛却一直在量你腰上的印戒值多少钱。这是个把什么都换算成数目的人——人情、面子、性命，在他眼里大概都标着价。"

    guild_master "船长跟您说的，大概是'公会要吞了港口'这一套吧。"

    guild_master "她那张嘴，能把黑的说成白的。可您是聪明人，不会光听一面之词。我也不跟您绕——公会要的不是吞，是管。一个没人管的港口，对您这样的大主顾，才是真正的灾难。"

    guild_master "我换个说法。这港口三百年没有王法，谁拳头硬谁说话。船多的劫船少的，没靠山的连泊位都抢不到。"

    guild_master "您是领主，治过地方，该懂——没有规矩的地方，最先饿死的不是强人，是老实人。船长口口声声的'自由'，对强者是自由，对弱者，是任人宰割。"

    guild_master "公会做的事，是给它立规矩。登记、抽税、护航。乱港变商港。"

    corsair "立规矩。规矩立完，规矩就是你。"

    guild_master "总好过你们那套——谁拳头硬谁是规矩。船长，你忘了十年前没公会的时候，这港口什么样？三天一抢，五天一杀，寡妇比渔船还多。"

    corsair "我没忘。可我也没忘，是谁把'抢'改成了'抽税'，把'杀'改成了'放贷'。换身绸衣裳的强盗，还是强盗。"

    guild_master "……牙尖嘴利。"

    guild_master "至少我的规矩写在纸上，船长。你的规矩在刀上。"

    "两人你一句我一句，针尖对麦芒。可你听着听着，咂摸出一点别的味道——他们斗得太熟练了，像一对吵了三十年的老冤家，每句话都正中对方旧伤。这样的两拨人，本不该这么轻易就被逼到要拔刀见血的地步。"

    "两个人都不再看对方，都看着你。"

    guild_master "领主大人，您要的是稳定的海路。能给您稳定的，是秩序，不是一群随时会翻脸的船主。"

    guild_master "您站公会这边，好处不止盐铁优先。艾登堡要在南境立个商号，公会替您张罗；要借钱周转，利钱给您算最低一档。"

    guild_master "船主能给您什么？几句江湖义气，一堆随时会沉的破船。义气这东西，押不了货，也还不了债。"

    guild_master "站在公会这边。我们保您艾登堡的盐铁优先放行，价钱也好谈。"

    corsair "他没告诉你'优先'的意思——意思是别人靠后。今天他给你优先，明天换个出价更高的，你就是那个靠后的。"

    corsair "公会的恩惠，都是租来的，按月收息。你拿了他的好处，就等于把脖子伸进他的套里。等你发觉勒得慌，已经挣不脱了。"

    corsair "跟我们走。船主认人不认章。你帮我们撬开公会的手，这港口的船，以后认艾登堡的旗。"

    corsair "维斯帕给你画的那些大饼——商号、低息、优先放行，听着是甜。可你想想，他凭什么给？还不是因为公会攥着这港口的脖子。哪天你不听话了，这些甜头，眨眼就成了套在你脖子上的绳。"

    corsair "我们船主给不了你大饼。可我们认人。你帮我们一回，这份情，南海上的船记一辈子。"

    "两边都把话放下了。现在轮到你。"

    ## ── 选边前：给玩家一天亲眼看两派（块3 深入两派）──
    $ hide_all_chars("player_char_img", "corsair_img")
    show player_char_img at left with dissolve
    player "两位的话我都听了。不过我有个毛病——光凭嘴上说的，我拿不准。"

    player "给我一天。公会怎么运转，船主怎么过活，我都亲眼看看。明晚，给二位答复。"

    $ hide_all_chars("guild_master_img", "corsair_img", "ship_boy_img", "dockhand_img", "servant_generic_img", "soldier_generic_img", "merchant_karl_img", "blacksmith_wife_img", "farmer_rep_img", "old_woman_img", "noble_werner_img", "stable_boy_img", "storyteller_img")
    show guild_master_img at left with dissolve
    guild_master "……痛快。公会没什么见不得人的，明早我派人来接您。"

    corsair "行。看清楚了再选。我不怕你看。"

    $ hide_all_chars()
    scene black with dissolve
    call southern_deep_dive from _call_southern_deep

    pause 0.5

    ## ============================================================
    ## 第一幕 · 核心抉择
    ## ============================================================

    menu:
        "站公会——秩序能保海路（倾向 财富/谋略）":
            $ southern_faction = "guild"
            $ alliance_guild = True
            $ change_rel("rel_corsair", -15)
            $ log_decision("南境游记", "在潮汐港选择支持金锚公会")
            $ change_stat("wealth", 5)

            $ hide_all_chars()
            show guild_master_img at left with dissolve

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我要的是十年都不断的海路。船主今天讲义气，明天可能就把货卖给出价高的人。"
            player "公会有账本，有章程。我跟有章程的人打交道。"

            $ hide_all_chars("guild_master_img", "corsair_img", "ship_boy_img", "dockhand_img", "servant_generic_img", "soldier_generic_img", "merchant_karl_img", "blacksmith_wife_img", "farmer_rep_img", "old_woman_img", "noble_werner_img", "stable_boy_img", "storyteller_img")
            show guild_master_img at left with dissolve
            guild_master "明智。艾登堡不会后悔。"

            "维斯帕笑了。那笑容里没有高兴，只有'又算对了一笔'的满足。"

            $ hide_all_chars()
            "门口传来椅子翻倒的声音。你回头，赛琳已经走了。门还在晃。"

            "维斯帕替你斟上酒。赛琳的位子空着，椅子倒在地上，没人去扶。"

            "当夜，断锚左边那几桌船主的人，一个接一个走了。你站了公会的消息，天没亮就传遍了港口。"

            "老汉斯托人捎来一句话：'内陆来的，我看错了你。'就这一句，没有别的。"

        "站船主——自由的港才认你的旗（倾向 声望/勇气）":
            $ southern_faction = "pirates"
            $ alliance_pirates = True
            $ change_rel("rel_corsair", 18)
            $ log_decision("南境游记", "在潮汐港选择支持自由船主联盟")
            $ change_stat("reputation", 5)

            $ hide_all_chars()
            show corsair_img at right with dissolve

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "公会的规矩写在纸上，纸是他们印的。"
            player "我宁可跟认人的人打交道。船主联盟，艾登堡跟你们走。"

            $ hide_all_chars("corsair_img", "player_char_img", "player_young_img", "player_teen_img", "player_child_img", "aldric_img", "guild_master_img")
            show corsair_img at right with dissolve
            corsair "……我以为内陆的贵人都只会算盐价。"

            corsair "你算的是别的。行。这杯我陪你喝。"

            "她把刀往桌上一搁，第一次真正坐了下来。维斯帕的脸沉了，他没再说话，带着随从退了出去。"

            "第二天一早，艾登堡商队在潮汐港的几笔交易，全被公会卡住了报关——维斯帕用最快的方式让你知道，得罪公会的代价。"

            "可栈桥上，船主们看你的眼神不一样了。一个内陆领主肯为他们站到公会对面，这在潮汐港，三十年没有过。"

            "她替你满上酒，又给自己满上。这一坛，你们一人一半。"

        "都不站——把两边按在一张桌子上谈（需 谋略≥45 或 声望≥45）" if intrigue >= 45 or reputation >= 45:
            $ southern_faction = "neutral"
            $ southern_brokered_peace = True
            $ change_rel("rel_corsair", 12)
            $ log_decision("南境游记", "在潮汐港试图斡旋停火")
            $ change_stat("intrigue", 4)

            $ hide_all_chars()
            show corsair_img at right with dissolve
            show guild_master_img at left with dissolve

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你们两个都想拉我站队。可我站哪边，哪边赢，输的那边就掀桌子——港口照样停。"
            player "我要的是港口开着。所以我谁都不站。"

            $ hide_all_chars("guild_master_img", "corsair_img", "ship_boy_img", "dockhand_img", "servant_generic_img", "soldier_generic_img", "merchant_karl_img", "blacksmith_wife_img", "farmer_rep_img", "old_woman_img", "noble_werner_img", "stable_boy_img", "storyteller_img")
            show guild_master_img at left with dissolve
            guild_master "那您来这一趟，图什么？"

            $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
            show player_char_img at left with dissolve
            player "图你们俩今晚坐下来，把扣的船和锁的链子,一样换一样。"

            $ hide_all_chars("corsair_img", "player_char_img", "player_young_img", "player_teen_img", "player_child_img", "aldric_img", "guild_master_img")
            show corsair_img at right with dissolve
            corsair "他放人，我们就撤链子？"

            player "他先放一半人，你们先撤一半链子。剩下的，明天我看着你们换。"

            "维斯帕和赛琳都没立刻答应。可两个人都没走——在这种地方，不走，就是在听。"

            corsair "……内陆来的，倒会算。"

            $ hide_all_chars("guild_master_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
            show guild_master_img at left with dissolve
            guild_master "暂且听听。但只是暂且。"

            "没人赢，也没人掀桌子。维斯帕留了两个随从盯着，赛琳的刀还搁在桌上没收。明天的事，明天再说。"

            "你谁也没得罪，也谁都没真正拉拢。这一夜的太平是你硬压出来的，压得住一夜，未必压得住第二夜。"

            "回客栈的路上，奥尔德里克低声说：'大人，骑墙最稳，也最险。两边都盯着您，看您到底往哪边倒。'"

        "先不表态，今晚我要自己去码头看看（谨慎）":
            $ southern_faction = ""
            $ change_rel("rel_corsair", 5)
            $ log_decision("南境游记", "暂不选边，决定先自行查证")

            $ hide_all_chars()
            "你两边都没应。"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "两位的话我都听了。可我谁的话都还没信。"
            player "今晚我自己去码头看看那条铁链，看看那些扣下的船。明天再给二位答复。"

            $ hide_all_chars("guild_master_img", "corsair_img")
            show guild_master_img at left with dissolve
            guild_master "……谨慎。也行。希望您看见的，跟您听见的一样。"

            $ hide_all_chars("corsair_img", "guild_master_img")
            show corsair_img at right with dissolve
            corsair "随你。不过夜里的码头不安全，外乡人。"
            corsair "要去，带上这个。"

            "她解下腰间一枚铜哨，丢给你。"

            corsair "吹响它，附近水里要是有我的人，会来。要是没有——那就跑快点。"

            $ change_rel("rel_corsair", 5)
            "你接住了哨子。冰凉，边缘有牙印——被人紧张地咬过很多次。一个在港口里横着走的渡鸦船长，也有过怕得只能咬着哨子等人来的时候。你把哨子收进了怀里。"

    pause 0.5
    $ southern_quest_stage = 1
    $ persistent.southern_dlc_progress = 1

    ## ============================================================
    ## 第一幕收束 + 钩子
    ## ============================================================

    $ hide_all_chars()
    scene black with fade
    pause 0.5

    "那天夜里，你没睡好。有件事对不上。"

    "公会说船主先动的手。船主说公会先扣的船。两边都信誓旦旦，可没有一个人，说得出第一刀是谁先捅的。"

    "好像有谁，特意不让这个问题有答案。"

    if southern_faction == "guild":
        "你站了公会。可维斯帕算账太顺了，顺得像早就排好了。"
    elif southern_faction == "pirates":
        "你站了船主。可赛琳要的'撬开公会的手'，听着也太急了点。"
    elif southern_faction == "neutral":
        "你压着两边谈了。可越谈你越觉得，他们俩谁都不想真打——是别人想让他们打。"
    else:
        "你谁都没站。明天天一亮，你就去那条铁链和那些扣下的船边上，自己看。"

    ## ── 恋爱支线：夜航（与赛琳够近、且没站死公会）──
    if rel_corsair >= 25 and southern_faction != "guild":
        call southern_night_voyage from _call_southern_voyage

    pause 1.5
    scene black with dissolve

    centered "{size=+5}第一幕 · 完{/size}"
    pause 1.5

    $ unlock_southern_milestone()

    jump southern_act2


## ── DLC 第一弹结束界面 ──
screen southern_dlc_return():
    modal True
    zorder 200
    add Solid("#0a0812f0")

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 40
        ypadding 30
        background Solid("#1a1528f0")

        vbox:
            spacing 18
            xalign 0.5

            text "南境游记 · 第一弹到此结束" size 24 color "#d4a942" font "msyh.ttf" xalign 0.5

            text "感谢试玩。你在潮汐港的选择已记录，将影响后续幕次。" size 15 color "#c8b890" font "msyh.ttf" xalign 0.5

            null height 6

            textbutton "返回主菜单":
                xalign 0.5
                text_size 20
                text_color "#d4a942"
                text_hover_color "#ffd866"
                action MainMenu(confirm=False)


## ── DLC 进度里程碑 ──
init python:
    def unlock_southern_milestone():
        ## southern_act1 已在 characters.rpy 的 achievement_data 正式注册
        unlock_achievement("southern_act1")

    def southern_finish(ending_key, achievement):
        """登记 DLC 结局：独立 set + 成就 + 解锁画廊，不碰主线 endings_seen。"""
        persistent.southern_endings_seen.add(ending_key)
        unlock_achievement(achievement)
        if corsair_romance:
            unlock_achievement("southern_lover")
        ## 解锁场景画廊 + 赛琳肖像（六张场景在任意路线都会出现在结局前）
        for _g in ("bg_tideport_harbor", "bg_tideport_beach", "bg_tideport_tavern",
                   "bg_tideport_ship", "bg_tideport_office", "bg_tideport_fleet", "corsair"):
            unlock_gallery(_g)

    ## 结局路线图用：(key, 名称, 描述, 颜色, 图标)
    _southern_ending_info = [
        ("free",  "自由港",     "促成联合，潮汐港自治存续",   "#2e8b8b", "港"),
        ("ruler", "港口新主",   "倒向一方，掌港却失其自由",   "#b8860b", "旗"),
        ("fall",  "潮汐港陷落", "卖港换盐路，自由港覆灭",     "#3d3a36", "灰"),
        ("outwit","螳螂捕蝉",   "纯靠谋略反将王廷，一兵未损",  "#9b59b6", "谋"),
        ("vassal","王旗下的港", "归附王廷，保住港却失其名分",  "#7a6a4a", "附"),
    ]


## ============================================================
## 第三幕 · 潮信
## ------------------------------------------------------------
## 王室军队压境的高潮 + 3 分歧结局：
##   自由港(联合/最佳) · 港口新主(倒向一方/bittersweet) · 陷落(坏)
## 由第一幕站队 + 本幕最终抉择 + 属性/恋爱共同决定。
## ============================================================

label southern_act3:

    play music "audio/music/southern_scheme.ogg" fadeout 1.0 fadein 1.5 if_changed
    scene bg tideport_tavern with fade
    pause 0.3

    centered "{size=+6}第三幕 · 潮信{/size}"
    pause 1.2
    scene bg tideport_tavern with dissolve

    voice "audio/narration/south_a3_01.mp3"
    "天一亮，断锚酒馆成了临时的议事厅。门口有船主的人把守，桌上摊着港口的海图。"

    voice "audio/narration/south_a3_02.mp3"
    "你、维斯帕、赛琳，三个人围着那张图。昨天还要拔刀，今天得在傍晚之前想出活路。"

    show corsair_img at right with dissolve
    show guild_master_img at left with dissolve

    guild_master "港务厅那帮老爷已经在备茶水彩绸，准备开门迎王室军队了。在他们眼里，换个主子而已。"

    corsair "我的船能堵航道。可我有三条快船，对面是一支分舰队。堵得了一时，堵不住。"

    corsair "硬打，我们没赢面。"

    ## ── 破局前的推演（块13）：几条法子都被否 ──
    $ hide_all_chars("soldier_generic_img")
    show sea_dog_img at left with dissolve
    sea_dog "没赢面也得打！我老汉斯这把骨头，宁可喂鱼，不给官军当顺民！"

    $ hide_all_chars("corsair_img", "player_char_img", "player_young_img", "player_teen_img", "player_child_img", "aldric_img", "guild_master_img")
    show corsair_img at right with dissolve
    corsair "喂鱼容易。喂完了，港口照样被占，我们白死。"

    $ hide_all_chars("sea_dog_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
    show sea_dog_img at left with dissolve
    sea_dog "那你说怎么办！"

    $ hide_all_chars("guild_master_img")
    show guild_master_img at left with dissolve
    guild_master "老法子——撒钱，买通对面的军官，让他们出工不出力。"

    $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img")
    show player_char_img at left with dissolve
    player "来不及。一支分舰队几十个军官，今晚买得通几个？"

    $ hide_all_chars("guild_master_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
    show guild_master_img at left with dissolve
    guild_master "……那就谈。我亲自上旗舰，献些岁币，求主帅退兵。"

    $ hide_all_chars("corsair_img", "player_char_img", "player_young_img", "player_teen_img", "player_child_img", "aldric_img", "guild_master_img")
    show corsair_img at right with dissolve
    corsair "谈？你以为他们千里压来，是为你那点岁币？他们要的是整个港。开口谈，就是开门请他们进来。"

    "桌上静了。打不过，买不动，谈不拢。屋里十几个人，头一回真切尝到'无路可走'是什么滋味。"

    ## ── 破局点：否认借口（高谋略玩家自己想到，否则由 NPC 点破）──
    if intrigue >= 50:
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "那就不打。"

        "两个人都看你。"

        player "王室军队要的是'平乱'这个名义。港口乱，他们进来才叫平乱。"
        player "可要是傍晚他们到的时候，整个港口好端端的，人人站在码头上，秩序得像过节——他们一炮打过来，那就不是平乱，是当着全海域的面屠港。"

        player "王廷丢不起这个脸。别的自由港会看，给王国跑海运的商会也会看。"

        $ hide_all_chars("guild_master_img", "corsair_img", "ship_boy_img", "dockhand_img", "servant_generic_img", "soldier_generic_img", "merchant_karl_img", "blacksmith_wife_img", "farmer_rep_img", "old_woman_img", "noble_werner_img", "stable_boy_img", "storyteller_img")
        show guild_master_img at left with dissolve
        guild_master "……让他们师出无名。"
    else:
        $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
        show player_char_img at left with dissolve
        player "总有破法。他们千里压过来，图的是什么？"

        $ hide_all_chars("guild_master_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
        show guild_master_img at left with dissolve
        guild_master "图一个名义。'平乱'。"

        guild_master "潮汐港乱，他们才进得来。这道理我做了半辈子生意，反倒是今早才想透——他们要的从来不是赢，是我们先乱给他们看。"

        show corsair_img at right with dissolve
        corsair "所以要是港口不乱呢？要是傍晚他们到的时候，整个港好端端的，人都齐齐站在码头上？"

        guild_master "那一炮打下来，就不是平乱，是屠港。王廷丢不起这个脸。"

    "海图上那支正在逼近的舰队，第一次显得没那么不可战胜。"

    "屋里的气氛松了一丝。可你心里清楚，路是有了，难的在后头——要让斗了三十年的公会和船主，在一夜之间拧成一股绳，比挡住那支舰队还难。"

    "可办法归办法。要让整个港口一条心站出来——公会和船主，得先把刀收回鞘里。这一步，落在你身上。"

    pause 0.5

    ## ============================================================
    ## 第三幕 · 最终抉择
    ## ============================================================

    menu:
        "促成联合——让整个港口站成一条心，逼王室军队师出无名":
            $ log_decision("南境游记", "第三幕：促成两派联合，否认王室军队借口")

            ## 联合是否成功：调停过 / 声望或谋略够 / 恋爱加成
            if southern_brokered_peace or reputation >= 50 or intrigue >= 50 or corsair_romance:
                $ southern_united = True
                call southern_prepare from _call_southern_prepare
                jump ending_southern_free
            else:
                "你想把两边拧到一处。可你昨天站得太偏，话说出口，另一半人不信。"
                "公会和船主在最后关头还是各按各的算盘。整齐的港口没站成，站成了两摊。"
                $ southern_united = False
                jump ending_southern_ruler

        "靠你站定的那一方硬抗，用港口的地利拼一场" if southern_faction == "guild" or southern_faction == "pirates":
            $ log_decision("南境游记", "第三幕：倒向一方武力对抗王室军队")
            $ southern_united = False
            jump ending_southern_ruler

        "智取——不靠人多，单凭证据和谋略，反将王廷一军" if intrigue >= 60 and evidence_count >= 3:
            $ log_decision("南境游记", "第三幕：智取，揭破王廷阴谋反制")
            jump ending_southern_outwit

        "给王室主帅递话——用艾登堡的名义换盐路特许，保自己":
            $ log_decision("南境游记", "第三幕：与王室军队私下交易，出卖港口")
            jump ending_southern_fall

        "代潮汐港向王廷请附——归顺王廷，换一纸自治诏书" if reputation >= 55:
            $ log_decision("南境游记", "第三幕：促成潮汐港归附王廷为自治领")
            jump ending_southern_vassal


## ============================================================
## 结局五 · 王旗下的港（附庸 / 妥协）
## ============================================================

label ending_southern_vassal:
    $ hide_all_chars()
    play music "audio/music/southern_fleet.ogg" fadeout 1.0 fadein 2.0 if_changed
    scene bg tideport_fleet with fade

    "你没让两边硬拼，也没出卖谁。你做了一件公会和船主都想不到的事——去跟王室主帅，谈条件。"

    $ hide_all_chars("soldier_generic_img")
    show soldier_generic_img at right with dissolve
    $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img")
    show player_char_img at left with dissolve
    player "主帅。打这一仗，你赢得了港口，输的是脸面——当着全海域屠一个自由港，王国往后还怎么跟人做生意？"

    player "我替潮汐港给王廷递个台阶：港口归顺，挂王旗，认王廷为宗主。但王廷要给一纸诏书，保港口自治——不驻军、不收编公会船主、商事照旧自理。"

    $ hide_all_chars("royal_admiral_img", "player_char_img", "player_young_img", "player_teen_img", "player_child_img", "aldric_img", "guild_master_img", "old_salt_img", "sea_dog_img", "chen_captain_img", "blacksmith_wife_img")
    show royal_admiral_img at right with dissolve
    royal_admiral "归顺，又要自治？天下哪有这样的好事。"

    player "有。这样王廷不费一兵一卒得了潮汐港的名分，各国商会挑不出错，你也不必背屠港的恶名。三方都有台阶下。"

    "主帅盯着你看了很久。一个内陆领主，替一个不属于他的港口，跟王室军队谈出了一条所有人都能活的路。"

    royal_admiral "……我请示王廷。"

    pause 0.8
    scene bg tideport_harbor with dissolve

    "三天后，王廷的诏书到了。潮汐港归附王廷，为'自治海港'，永不驻军，商事自理。"

    "港口的桅杆上，多了一面王旗。公会还是那个公会，船主还是那群船主，断锚酒馆照样卖它最不上头的酒。只是这港口三百年来头一回，头顶上有了个名义上的主子。"

    show corsair_img at right with dissolve
    if corsair_romance:
        corsair "挂面王旗就能换太平。我那些死脑筋的兄弟还在骂你卖了港。"
        corsair "可我知道——你要不递这个台阶，今晚海堤上站着的人，明天就得有一半喂鱼。自由这东西，有里子，比有面子要紧。"
    else:
        corsair "挂面王旗换条命。船主们骂你，可没一个真愿拿命去换那面没有王旗的天空。"
        corsair "你这台阶递得不光彩，却递得实在。潮汐港欠你一条命——尽管它未必肯认。"

    $ hide_all_chars()
    scene black with dissolve

    centered "{size=+8}王旗下的港{/size}"
    pause 1.2
    centered "{size=+3}潮汐港保住了里子，交出了名分。{/size}"
    pause 1.0
    centered "{size=+3}三百年的自由，从此挂在别人的旗下——可它还活着。{/size}"
    pause 2.0

    $ southern_finish("vassal", "southern_vassal")
    jump southern_dlc_complete


## ============================================================
## 结局四 · 螳螂捕蝉（智取 / 高谋略隐藏）
## ============================================================

label ending_southern_outwit:
    $ hide_all_chars()
    play music "audio/music/southern_scheme.ogg" fadeout 1.0 fadein 2.0 if_changed
    scene bg tideport_office with fade

    "你没去联合谁，也没打算硬拼。你手里有更利的东西——费舍尔留下的全部证据，和一个看透了王廷算盘的脑子。"

    "你想明白一件事：发兵的不是'王廷'，是王廷里某一派主战的人。他们想拿潮汐港立威、捞功。可这一派，在王廷里也有政敌。"

    "当夜，你誊了十几份东西，不是送给商船，是送给该送的人——"

    "一份递往王都，交到主战派政敌手里：你看，他们假造海寇之乱、挑动自由港自相残杀，败坏王国信誉。"

    "一份送往各国商会：王廷某派要吞港了，今天是潮汐港，明天就轮到你们的商路。"

    "一份，你甚至设法递到了主战派自己手里：你们的密探费舍尔，证据在我手上。再往前一步，这些就不止我一个人知道。"

    pause 0.8
    scene bg tideport_fleet with dissolve

    "傍晚，王室舰队压到港外。可它没进攻。它在外海停了整整一夜。第二天清晨，掉头走了——比来时还急。"

    scene bg tideport_harbor with dissolve

    "后来你才拼出那一夜的事。"

    "你递出去的证据在王都炸了锅。主战派的政敌抓住把柄，参了他们一本'擅启边衅、辱国丧信'。王廷为平息各方商会的物议，连夜下令撤兵，还把主战派几个头目下了狱。"

    "费舍尔背后那只手缩了回去，缩得比伸出来还快。因为它发现，这局里最危险的不是潮汐港的刀和船，是一个内陆来的领主，和他手里那几张纸。"

    show corsair_img at right with dissolve
    corsair "我到现在还没回过味来。王廷的兵压到家门口了，你没调一兵一卒，没流一滴血，他们就……自己走了？"

    $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img")
    show player_char_img at left with dissolve
    player "他们不怕潮汐港。他们怕自己人先把自己人办了。我只是把刀，递到了对的人手里。"

    corsair "……内陆的权谋，比我们海上的刀邪门多了。"

    if corsair_romance:
        "她忽然凑近，盯着你的眼睛看了很久，像头一回认识你。"
        corsair "我跟过不少厉害角色。可你这种——杀人不见血、退敌不沾刀的，头一个。说实话，有点怕你。"
        player "怕我？"
        corsair "怕你哪天，把我也算进哪盘棋里。"
        player "你不一样。算计别人，是因为他们是棋子。你不是。"
        "她愣了一下，别开脸，耳根又红了。"
        corsair "……油嘴滑舌。"

    "潮汐港保住了，一兵未损。公会、船主，谁都欠你一个天大的人情，却谁都没真正看懂，你是怎么做到的。"

    $ hide_all_chars()
    scene black with dissolve

    centered "{size=+8}螳螂捕蝉{/size}"
    pause 1.2
    centered "{size=+3}你没赢下一场仗。你让想打这场仗的人，输给了他自己人。{/size}"
    pause 1.0
    centered "{size=+3}潮汐港至今不知道，替它退了王室军队的，是一个外乡人。{/size}"
    pause 2.0

    $ southern_finish("outwit", "southern_outwit")
    jump southern_dlc_complete


## ============================================================
## 结局一 · 自由港（联合 / 最佳）
## ============================================================

label ending_southern_free:

    $ hide_all_chars()
    play music "audio/music/southern_fleet.ogg" fadeout 1.5 fadein 2.0 if_changed
    scene bg tideport_fleet with fade

    "傍晚。王室军队的桅灯排成一道墙，压到了港口外的浅水线。"

    scene bg tideport_harbor with dissolve

    "可码头上没有慌乱。"

    "全港的人都站出来了。"

    "老汉斯拄着他那条瘸腿，站在船主们最前头。断锚的老板搬了张凳子，把那条断腿支着，也来了。卖鱼的阿姆挽着袖子，鱼刀别在腰上。"

    "你昨天在码头替他出过头的老船工，领着一帮渔民，站在公会账房的隔壁——头一回，两拨人没有互相瞪眼。"

    if fisher_husband_found or fisher_wife_promise:
        "陈嫂抱着孩子，站在她男人身边。海雀号的七个汉子，刚从牢里出来，伤还没好，可一个不少地站着。"

    "公会的账房、船主的水手、卖鱼的、补帆的、开酒馆的——一排一排，沿着栈桥站得整整齐齐，像在等一场仪式，不像在等一场仗。"

    show corsair_img at right with dissolve
    show guild_master_img at left with dissolve

    "你站在最前头。手里是费舍尔烧剩的半卷文书，和维斯帕连夜从港务厅翻出的往来账。"

    "你早把消息递了出去——递给昨夜过港的他国商船，递给下游两个自由港。此刻港口外，除了王室军队的船，还泊着十几条挂着各色旗号的商船，都在看。"

    "王廷特使乘小艇上岸，身后跟着一队甲士。他准备好的说辞是'应港务厅之请，入港平乱'。可他眼前的港口，没有乱。"

    $ hide_all_chars("soldier_generic_img")
    show soldier_generic_img at right with dissolve
    envoy_royal "潮汐港港务厅有请，王师入港，弹压乱党。交出为首作乱者，余者不究。"

    envoy_royal "三炷香。香尽不开港门，视同抗命——届时刀剑无眼，休怪王师无情。"

    $ hide_all_chars("player_char_img", "soldier_generic_img")
    show player_char_img at left with dissolve
    show soldier_generic_img at right with dissolve
    player "特使大人，乱在哪里？请指给这些船看。"

    "你侧身让开。特使顺着你的手望去——栈桥上，公会的账房和船主的水手并排站着，渔民、店家、补帆的，一排一排，安静得像在等一场仪式。"

    envoy_royal "……装出来的太平，骗不了王师。来人——"

    "特使一抬手，要发难。可人群里走出两个人。"

    $ hide_all_chars("guild_master_img", "corsair_img")
    show guild_master_img at left with dissolve
    show corsair_img at right with dissolve
    guild_master "金锚公会大执事维斯帕。特使口中的'作乱者'，是指我？公会维持港口秩序三十年，账册俱在，欢迎查验。"

    corsair "自由船主联盟，渡鸦。要拿人，先说清楚：拿谁，凭什么。"

    "昨天还要拔刀相向的两拨人，此刻并肩堵在特使面前。特使准备好的戏，第一页就演不下去了。"

    $ hide_all_chars("soldier_generic_img", "player_char_img", "player_young_img", "player_teen_img", "player_child_img", "aldric_img", "guild_master_img")
    show soldier_generic_img at right with dissolve
    envoy_royal "你们……"

    $ hide_all_chars("player_char_img", "corsair_img")
    show player_char_img at left with dissolve
    show corsair_img at right with dissolve
    player "他没词了。因为按他的本子，这会儿你们俩该正杀得你死我活，好给王室军队一个'平乱'的由头。"

    "你举起那半卷烧焦的文书。焦边底下，是王廷密探费舍尔的手记——怎么递假密报给公会，怎么劝船主动手，怎么把一条空盐船说成军火船。"

    player "第一刀不是公会捅的，也不是船主捅的。是你们的人，费舍尔。点完火，他跑了。"

    "岸上十几条商船的人都听见了。特使的脸白了一层。"

    $ hide_all_chars("soldier_generic_img", "player_char_img", "player_young_img", "player_teen_img", "player_child_img", "aldric_img", "guild_master_img")
    show soldier_generic_img at right with dissolve
    envoy_royal "一派胡言！区区几张烧焦的废纸，也敢污蔑王师——"

    player "废纸？特使大可下令搜身，当着这些船，把费舍尔的手记一条条念出来，看是不是污蔑。"

    "特使张了张嘴，没念。他比谁都清楚那上头写的是什么。"

    "他要么下令开炮——当着全海域，炮轰一个秩序井然的自由港；要么撤。"

    "这个名声，王廷担不起。"

    pause 0.8

    "桅灯，一盏一盏，掉头了。"

    play music "audio/music/southern_freeport.ogg" fadeout 2.0 fadein 2.0 if_changed
    scene bg tideport_beach with dissolve

    "舰队退到海平线以下那天，港口的铁链解开了。海雀号第一个出港，少年水手在桅杆上冲岸边挥手。"

    "公会和船主坐下来，重立了港约：登记取消，泊费照旧，船主在港务厅有了一席。维斯帕和赛琳谁都没全赢——可港口开着，三百年的自由还在。"

    "重立港约那天，断锚酒馆挤满了人。维斯帕和老汉斯隔着一张桌子，谁也不看谁，到底在同一张约书上按了手印。"

    $ hide_all_chars("soldier_generic_img")
    show sea_dog_img at left with dissolve
    sea_dog "跟金锚同桌喝酒，我老汉斯活了六十年头一回。这口酒，是你这内陆来的逼我咽下的。今天，我认。"

    if fisher_husband_found or fisher_wife_promise:
        $ hide_all_chars("blacksmith_wife_img")
        show blacksmith_wife_img at right with dissolve
        "陈嫂抱着孩子挤到你面前，她男人就站在身后——海雀号的人，一个没少地回来了。"
        fisher_wife "贵人……我不会说漂亮话。这条命，这一家，记您一辈子。"
        "她男人没出声，只冲你深深一揖，到底红了眼。"

    "海雀号补好了帆，第一个出港。少年水手在桅杆上冲岸边挥手，喊的什么听不清，那笑脸隔着半个港都看得见。"

    $ hide_all_chars("guild_master_img")
    show guild_master_img at left with dissolve
    guild_master "领主大人，艾登堡的盐铁，往后在潮汐港优先放行。这次不是施舍，是港口欠您的。"

    $ hide_all_chars()

    if corsair_romance:
        show corsair_img at right with dissolve
        corsair "盐路的事，公会算他们的。我算我的。"

        corsair "下一趟你的盐船北上，我亲自押。我想看看艾登堡的雪——在海上混了这么久，还没见过雪长什么样。"

        "她说完，把那枚你还回去的铜哨又塞回你手里。"

        corsair "留着。下回你吹响它，我从哪片海都给你赶过来。"

        "渡鸦船长说话算话。这一点，整片南海都知道。"

        "那年冬天，一队挂着金鹰旗的盐车第一次碾进艾登堡的城门。押车的女人站在雪地里仰着头，看了很久。"

        "她没看过雪。可她说，值得跑这一趟。"

        "潮汐港还是那个谁也圈不住的自由港。只是往后每年冬天，南海上那面黑帆，总会往北边来一趟。"
    else:
        show corsair_img happy at right with dissolve
        corsair "你这内陆来的，搅了一池子浑水，又替我们澄清了。"

        corsair "记住断锚的门朝哪开。下回来，酒还是记我账上。"

    pause 0.5
    $ hide_all_chars()
    scene black with dissolve

    centered "{size=+8}自由港{/size}"
    pause 1.2
    centered "{size=+3}潮汐港照旧是谁都能进、谁都不属于的港。{/size}"
    pause 1.0
    centered "{size=+3}你没有拿走它。{/size}"
    pause 2.0

    $ southern_finish("free", "southern_free")
    jump southern_dlc_complete


## ============================================================
## 结局二 · 港口新主（倒向一方 / bittersweet）
## ============================================================

label ending_southern_ruler:

    $ hide_all_chars()
    play music "audio/music/southern_fleet.ogg" fadeout 1.5 fadein 2.0 if_changed
    scene bg tideport_fleet with fade

    "傍晚。王室军队压到港外。你没有整个港口，你只有半个。"

    if southern_faction == "pirates":
        $ hide_all_chars("corsair_img")
        show corsair_img at right with dissolve
        corsair "公会缩着不动？随他们。这片海，是我们船主的主场。"
        "船主联盟的快船倾巢而出。赛琳的渡鸦号当先，借着对暗礁和潮汐的熟，在王室军队的大船之间穿梭——放火、撞舵、割锚索。"
        "王室军队的大舰在窄水里转不开身，被快船咬得焦头烂额。可快船毕竟小，一轮齐射下来，沉了三条。"
        menu:
            "撤回快船，改守港口窄口，保存实力":
                $ change_stat("intrigue", 2)
                "你没让船主硬填。快船退守窄口，用沉船和暗礁卡住王室军队。损失小了，对面也突不进来。僵住了。"
            "让快船缠住王室军队主力，掩护火船冲阵":
                $ change_stat("power", 2)
                $ change_rel("rel_corsair", -2)
                "你赌了一把。快船死死缠住王室军队主力，几条火船冲进舰队。旗舰中了火，乱了阵脚——可冲锋的船主，回来的不到一半。"
    elif southern_faction == "guild":
        $ hide_all_chars("guild_master_img")
        show guild_master_img at left with dissolve
        guild_master "船主那帮泥腿子靠不住。打仗，还得看公会的银子。"
        "公会砸下重金，雇光了港里所有能拿刀的人，又买通王室军队几个押粮的军官，让火药受了潮。"
        "船主冷眼旁观——你昨天站了公会，今天他们凭什么帮你。"
        menu:
            "再撒一笔钱，从内部瓦解王室军队":
                $ change_stat("wealth", -4)
                $ change_stat("intrigue", 2)
                "维斯帕又撒下一笔钱。王室军队里收了钱的军官越来越多，攻势一波比一波软。这一仗，是用银子堆退的。"
            "把雇兵摆在明处，做出死守的架势":
                $ change_stat("power", 2)
                "你把雇佣兵全摆上城防，刀枪林立，做出血战到底的样子。王室主帅掂量了一下硬啃的代价，到底没下死手。"
    else:
        "你站谁都没站，临阵才拢起一支杂凑的队伍。渔民、散兵、看不下去的店家，各打各的。"
        "没有一条心的港口，打起仗来像一盘散沙。你亲自压在最前头，才勉强没让阵脚垮掉。"
        menu:
            "亲自带队堵住缺口，以命相搏":
                $ change_stat("power", 3)
                "你提着剑堵在码头缺口。身边的人见领主都拼了，也红了眼。这一仗赢得惨，你胳膊上添了道见骨的口子。"
            "弃守外港，把人收进内港死守":
                $ change_stat("intrigue", 2)
                "你当机立断弃了外港，把人全收进内港。丢了半个港，保住了人。王室军队占了空港，讨不到便宜，悻悻退了。"

    "这一仗，王室军队没占到便宜，到底撤了。可港口烧塌了小半，海面上浮着的，是两边的人。"

    pause 0.5
    scene bg tideport_beach with dissolve

    "硝烟散尽，潮汐港还在——只是它变了。"

    "另一半人被你压了下去。从今往后，谁能进港、谁能出海、谁说了算，由你定。港务厅挂上了艾登堡的金鹰旗。"

    "船照常进出，货照常装卸。你的盐路，从此稳稳当当。"

    if corsair_romance and southern_faction == "pirates":
        $ hide_all_chars()
        show corsair_img sad at right with dissolve
        corsair "我们赢了。可你看这港口……它现在有主人了。"
        corsair "我跟了你，不后悔。只是往后再有人说'潮汐港是自由港'，我大概会笑一声。"
        "她没再说下去。有些东西保住了，有些东西，是保不住的。"
    else:
        "你成了潮汐港实际的主人。一个三百年没有主人的港口，现在有了。"
        "夜里你站在港务厅的窗前，听着外头照旧的喧闹。"

        "往后的潮汐港，再没有公会和船主的火并——只剩一个声音说了算，你的。"

        "盐路稳了，税收清了，连海盗都少了。这港口从没这么有秩序过。"

        "只是偶尔，老船工会在背地里念叨：当年那个内陆来的领主，本来是来谈生意的。后来怎么就成了潮汐港的主人，谁也说不清。"

    pause 0.5
    $ hide_all_chars()
    scene black with dissolve

    centered "{size=+8}港口新主{/size}"
    pause 1.2
    centered "{size=+3}你保住了潮汐港。它开着，认你的旗。{/size}"
    pause 1.0
    centered "{size=+3}只是它不再是谁都能自由进出的那个港了。{/size}"
    pause 2.0

    $ southern_finish("ruler", "southern_ruler")
    jump southern_dlc_complete


## ============================================================
## 结局三 · 潮汐港陷落（坏）
## ============================================================

label ending_southern_fall:

    $ hide_all_chars()
    play music "audio/music/southern_fleet.ogg" fadeout 1.5 fadein 2.0 if_changed
    scene bg tideport_fleet with fade

    "你没等到傍晚。"

    "午后，你乘小艇出港，登上了王室旗舰。"

    $ hide_all_chars("soldier_generic_img")
    show royal_admiral_img at right with dissolve
    "主帅是个花白胡子的老将，眼睛像两口枯井。他没起身，只让你说。"

    royal_admiral "艾登堡的领主，亲自上我的船。说吧，想要什么，拿什么换。"

    $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img")
    show player_char_img at left with dissolve
    player "艾登堡无意搅进港口的乱局。我只求一纸盐铁特许，往后南境海路，给艾登堡留条道。"

    $ hide_all_chars("royal_admiral_img", "player_char_img", "player_young_img", "player_teen_img", "player_child_img", "aldric_img", "guild_master_img", "old_salt_img", "sea_dog_img", "chen_captain_img", "blacksmith_wife_img")
    show royal_admiral_img at right with dissolve
    royal_admiral "就这？空口白话谁都会说。你拿什么让我信，你不是来替那帮海寇拖时间的？"

    menu:
        "交出费舍尔的证据，帮王室军队把'平乱'做实":
            $ change_stat("intrigue", 2)
            "你把查到的一切——费舍尔的内陆官文、港务官的证词——当着主帅的面，一把火烧了。"
            player "这些东西，本能让王室军队师出无名。现在它们没了。这是我的诚意。"
            "主帅笑了。他要的就是这个：让唯一能戳穿这场局的人，亲手毁掉证据。"
            royal_admiral "痛快。艾登堡的盐铁特许，我替你向王廷请。"

        "交出船主联盟的底细，换更厚的特许":
            $ change_stat("wealth", 3)
            $ change_rel("rel_corsair", -30)
            "你报出了船主联盟的虚实：谁是头、多少条船、藏在哪片暗礁后头。"
            "主帅的笔一条条记下。每记一条，就是一个信过你的人，往后的死路。"
            royal_admiral "好。有了这些，王师进港事半功倍。特许，加倍给你。"
            "你拿到了更厚的特许。代价是，老汉斯、陈船老大那些人的脸，往后会在你梦里排着队。"

    "一个内陆领主肯让路，比一场仗省事得多。主帅很满意。"

    "傍晚，王室军队不费一炮进了港。港务厅开门迎接，彩绸铺到了栈桥上。"

    "公会被'整编'，维斯帕成了王廷的港务官，绸袍换了官袍，脸上没什么两样。"

    "船主联盟被定为'海寇'。抓的抓，散的散。"

    $ hide_all_chars()
    show corsair_img sad at right with dissolve

    if corsair_romance:
        corsair "原来你北上那条盐路，比这一港的人都重。"
        corsair "也好。各为其主。"
        "她看你的眼神里没有恨，那比恨更难受。然后她转身上了渡鸦号。"
        "据说渡鸦号冲出了封锁线。据说。从此南海上再没人见过那面挂着渡鸦的黑帆。"
    else:
        "听说渡鸦号在合围里冲出了一个缺口，扯着破帆遁进了夜雾。听说而已。"
        "从此南海上，再没人见过那面黑帆。"

        "潮汐港改了名，叫'靖海卫'。王廷在港口立了座碑，记着王室军队'平定海寇之乱'的功绩。"

        "碑文里没有费舍尔，没有海雀号，没有那场子虚乌有的'走私'。"

        "艾登堡的盐车照常进城，比往年还便宜。你站在城头看那些盐，有时会想起一个抱孩子的女人，和一个说'我们是清白的'的硬汉。可也只是想想。日子还得过。"

    pause 0.5
    $ hide_all_chars()
    scene bg tideport_beach with dissolve

    "你回到艾登堡那天，盐车正好进城。满满当当，价钱比往年还低。"

    "你的盐路稳了——稳稳地捏在王廷手里。比从前更稳，也比从前更不由你。"

    pause 0.5
    scene black with dissolve

    centered "{size=+8}潮汐港陷落{/size}"
    pause 1.2
    centered "{size=+3}你保住了艾登堡的盐。{/size}"
    pause 1.0
    centered "{size=+3}潮汐港，连同那面黑帆，没了。{/size}"
    pause 2.0

    $ southern_finish("fall", "southern_fall")
    jump southern_dlc_complete


## ============================================================
## DLC 通关结算
## ============================================================

label southern_dlc_complete:

    $ persistent.southern_dlc_progress = 3
    $ southern_quest_stage = 3

    scene black with dissolve
    pause 0.5

    python:
        _seen = len(persistent.southern_endings_seen)
    centered "{size=+4}南境游记 · 第一弹 完{/size}"
    pause 1.0
    centered "{size=+3}潮汐港结局收集：[_seen]/5{/size}"
    pause 1.0
    if _seen >= 5:
        centered "{size=+3}你已看遍潮汐港的五种命运。{/size}"
        pause 1.2
    centered "{size=+3}——后续卷次开发中——{/size}"
    pause 2.0

    call screen southern_dlc_return


## ============================================================
## 第一幕 · 深入两派（选边前 call，亲眼看公会与船主）
## ============================================================

label southern_deep_dive:

    ## ── 上午 · 金锚公会 ──
    ## 原为 bg council_hall —— 那张图玩家在 chapter1_expansion.rpy:658 已认作艾登堡议事厅、
    ## chapter2.rpy:1683 又是领主会议厅。并入主线后同一张图演南境公会大楼会当场撞脸。
    ## bg_tideport_office.webp 是南境的专属图, 已在 images/ 里, 零美术成本。
    play music "audio/music/great_hall.ogg" fadeout 1.0 fadein 2.0 if_changed
    scene bg tideport_office with fade

    "第二天一早，公会的人领你进了金锚的大楼。比港里任何屋子都气派——这钱，看得见来路。"

    $ hide_all_chars("guild_master_img")
    show guild_master_img at left with dissolve
    guild_master "领主大人，请。公会就三件事：记账、护航、放贷。看完，您就懂什么叫'秩序'了。"

    "他先带你进账房。一排排架子，每条进出港的船都有一本册子——船名、船主、货色、航线，记得清清楚楚。"

    guild_master "从前这港口，谁的货被劫了，连个说理的地方都没有。如今有账，丢了货，查得到、追得回。"

    $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img")
    show player_char_img at left with dissolve
    player "查得到、追得回——也管得住。哪条船能出海，你这账房一句话。"

    $ hide_all_chars("guild_master_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
    show guild_master_img at left with dissolve
    guild_master "大人通透。秩序就是这样：方便人，也约束人。"

    "护航队在后院操练。几十条精壮汉子，刀枪齐整，比港里散兵游勇的船主像支队伍。"

    guild_master "南境海路有海盗。护航队走一趟，商船太平。这笔钱船主嫌贵，可没了它，他们的货连港都出不了。"

    "放贷处排着队。你看见一个船主，为凑泊费和登记的押金，正签一张利滚利的借据。他的手在抖。"

    menu:
        "问维斯帕：这利钱，是不是太狠了？（谋略）":
            $ change_stat("intrigue", 2)
            guild_master "狠？大人，是他自己要借的。公会没逼谁。"
            guild_master "泊费涨、押金加，船主周转不开，只能借公会的钱。借了还不上，船就归公会。这不是逼，是让他们自己走到这一步。"
            "你听懂了。公会不抢船——它让你把船'借'给它，再让你还不上。"

        "不动声色，把公会的底细记下":
            $ change_stat("intrigue", 1)
            "你没多问。账房记着谁有什么，护航攥着武力，放贷掐着钱。三只手，把整个港口的脖子不轻不重地掐着。"

    ## ── 下午 · 船主一方 ──
    play music "audio/music/southern_corsair.ogg" fadeout 1.5 fadein 2.0 if_changed
    scene bg tideport_harbor with dissolve

    "下午，赛琳来接你。她没带你去气派地方——船主的'议事厅'，是栈桥边一条搁浅的旧船。"

    $ hide_all_chars("corsair_img")
    show corsair_img at right with dissolve
    corsair "公会给你看了账本和护卫队吧？气派得很。我这儿没那些。我只能给你看这个。"

    "她指向被铁链锁着的海雀号，又指向岸边几户低矮的窝棚。"

    corsair "海雀号，空船一条，扣了二十多天。船上七个人，活不见人。"

    if fisher_wife_promise:
        $ hide_all_chars("blacksmith_wife_img", "corsair_img")
        show corsair_img at right with dissolve
        show blacksmith_wife_img at left with dissolve
        "陈嫂抱着孩子，在窝棚前补一张破得不能再补的网。看见你，她站了起来。"
        fisher_wife "贵人……您真来了。我男人的下落，可有信儿？"
        $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img")
        show player_char_img at left with dissolve
        player "还没有。但我没忘。今天来，就是要把这件事弄清楚。"
        "她没再说什么，只把怀里的孩子又搂紧了些。"
        $ change_rel("rel_corsair", 5)
    else:
        "几个水手的家眷蹲在窝棚前，望着海。男人被扣走了，生计跟着断了。"

    $ hide_all_chars("corsair_img", "soldier_generic_img")
    show corsair_img at right with dissolve
    show sea_dog_img at left with dissolve
    "搁浅的旧船上，十几个船主正在争吵。老汉斯也在。"

    sea_dog "等下去，海雀号的人就没了！我说今晚就动手，砸了公会的码头，把人抢回来！"

    corsair "抢回来？汉斯，公会有护航队、有港务厅。你带这几十号人冲上去，是去送死，还是去给公会一个'船主先动手'的借口？"

    "船主们安静了。赛琳的话不好听，可在理。她在这群认死理的人里，是少数压得住火的。"

    menu:
        "支持赛琳：冲动只会中别人的圈套（谋略/声望）":
            $ change_rel("rel_corsair", 6)
            $ change_stat("reputation", 2)
            $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img")
            show player_char_img at left with dissolve
            player "她说得对。你们现在动手，正中某些人下怀——他们就等你们'先动手'。"
            "老汉斯瞪着独眼看了你半晌，到底坐下了。"
            $ hide_all_chars("sea_dog_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
            show sea_dog_img at left with dissolve
            sea_dog "……内陆来的都这么沉得住气？罢了，听渡鸦的。"

        "理解老汉斯：可人命等不起（勇气/忠诚）":
            $ change_stat("loyalty", 2)
            $ change_rel("rel_corsair", 2)
            $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img")
            show player_char_img at left with dissolve
            player "汉斯船长的火，我懂。船上七条命，每多扣一天都是煎熬。"
            player "但赛琳是对的。救人要救得活，别拿更多人的命去填。给我点时间。"
            $ hide_all_chars("sea_dog_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
            show sea_dog_img at left with dissolve
            sea_dog "……好。看你们的。可别让老汉斯等太久。"

    $ hide_all_chars("corsair_img")
    show corsair_img at right with dissolve
    corsair "看完了。公会的账本，我们的窝棚。我不跟你说哪边占理——你自己有眼睛。今晚回去，自己掂量。"

    ## ── 当晚：码头械斗（块30）──
    "看完两边，天已擦黑。你正要回客栈，码头那头忽然炸开一阵喧哗。"

    $ hide_all_chars()
    scene bg tideport_harbor with fade
    "公会的护卫和一群船主的水手，隔着一条破船对峙。起因是个泊位——可看那架势，分明是早憋着的火，借着泊位发出来。"

    "双方越骂越凶，刀都摸出来了。再有一句不对付，就是血。"

    show corsair_img at right with dissolve
    corsair "又来。这几天港里的火气邪门得很，一点就着。"

    menu:
        "挤进中间，硬把两边分开（勇气/声望）":
            $ change_stat("reputation", 3)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "都把刀收了！为一个破泊位，值当拿命填？"
            "你直接挤进两拨人当中。这种时候，一个不相干的外乡人敢站在刀刃中间，反倒让两边都愣了。"
            "你借这一愣，连压带劝，把两拨人分开了。有人骂骂咧咧，可到底没动手。"
            $ hide_all_chars("corsair_img", "player_char_img", "player_young_img", "player_teen_img", "player_child_img", "aldric_img", "guild_master_img")
            show corsair_img at right with dissolve
            corsair "……你这条命是不要了？不过——这港口，是该有个敢站中间的人。"

        "找出挑头的，当众揭穿他在拱火（谋略）":
            $ change_stat("intrigue", 3)
            $ broker_rumor_heard = True
            "你没急着劝。你盯着人群里几个嗓门最大的——骂得最凶，手却缩在后头，分明想让别人先动手。"
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你们几个面生。哪条船上的？倒比苦主还急着动刀。"
            "被你一指，那几个人对视一眼，趁乱挤出人群溜了。没了拱火的，对峙的两拨人也泄了气，骂几句各自散了。"
            $ hide_all_chars("corsair_img", "player_char_img", "player_young_img", "player_teen_img", "player_child_img", "aldric_img", "guild_master_img")
            show corsair_img at right with dissolve
            corsair "……你看出来了。这几天港里的火，总有几张生面孔在添柴。"

        "退到一边，看这火会烧成什么样（旁观）":
            $ change_stat("intrigue", 2)
            "你没动。你想看看，这港口的火药桶，到底一点就炸到什么地步。"
            "对峙差点变成械斗，亏得两边头目赶来连拉带骂才压下去。可那一刻剑拔弩张的样子，你记住了。"
            "两边都绷到了极限。再来一两回这样的事，不用王室军队，潮汐港自己就能烧成一片白地。"

    "一场险些见血的械斗，就为一个破船泊位。可你越想越觉得，这火，有人在底下扇。"

    $ hide_all_chars()
    scene black with dissolve

    "那一夜你想了很久。"

    "公会那套秩序是真的——账本、护航、放贷，一样不缺。可三样捏在一只手里，那只手就能随时收紧。"

    "船主的义气也是真的。可你下午见的那群人，认死理、讲交情，一盘散沙，公会一推就倒。"

    "两边你都看清了。可越看清，越觉得有件事不对——这场火烧得太巧。巧得像有人算计好，就等你们两边咬死对方。"

    return


## ============================================================
## 第二幕 · 多步调查（少年供述后 call，取证后再对质）
## ============================================================

label southern_investigate:
    play music "audio/music/southern_scheme.ogg" fadeout 1.0 fadein 2.0 if_changed
    scene bg tideport_harbor with fade
    "天亮了。你没急着回断锚——少年的话要查实，光听不够。"
    "费舍尔，内陆口音，左手缺半根小指，一个两头递话的掮客。你想知道他到底是谁，替谁办事。"

label southern_investigate_loop:
    menu:
        "去地牢，探被扣的海雀号船员" if not investigate_jail:
            jump si_jail
        "设法查公会登记册，找'密报'的来路" if not investigate_ledger:
            jump si_ledger
        "查费舍尔住过的客栈" if not investigate_inn:
            jump si_inn
        "再去港务厅，撬港务官的嘴" if not investigate_office_q:
            jump si_office
        "找公会里看不惯费舍尔的人探口风" if not investigate_insider:
            jump si_insider
        "摸摸船主联盟内部的风向" if not investigate_faction2:
            jump si_faction2
        "请赛琳陪你查最险的那条线" if rel_corsair >= 40 and not investigate_together:
            jump si_together
        "证据够了，回断锚对质" if evidence_count >= 2:
            jump si_done
        "证据还不够，接着查" if evidence_count < 2:
            "你摇摇头。手里这点东西，还按不住公会和船主。再查。"
            jump southern_investigate_loop


label si_jail:
    $ investigate_jail = True
    if southern_faction == "pirates" or met_sea_dog:
        "老汉斯认得看牢的。塞了点钱，你得了一炷香工夫，进了港务厅底下的地牢。"
    elif southern_faction == "guild":
        "你以公会盟友的名义要了张探视条子。维斯帕没拦——他大概觉得你查不出什么。"
    else:
        "你费了些口舌和银钱，才说动看牢的睁一只眼。"
    scene bg dungeon with fade
    $ hide_all_chars("soldier_generic_img")
    show chen_captain_img at left with dissolve
    chen_captain "又是谁？来套话的省省。"

    $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img")
    show player_char_img at left with dissolve
    player "我替陈嫂查海雀号的事。你是陈船老大？"

    $ hide_all_chars("chen_captain_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
    show chen_captain_img at left with dissolve
    chen_captain "……我婆娘？她和孩子，还好吗？"

    $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
    show player_char_img at left with dissolve
    player "我见过她。她在等你回去。"

    "这条硬汉的眼眶红了一下，又硬生生忍住。"

    $ hide_all_chars("chen_captain_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
    show chen_captain_img at left with dissolve
    chen_captain "我们没走私。一船腌咸鱼，公会咬定是军火，欲加之罪。"

    chen_captain "怪就怪在——抓进来第二天，来了个内陆口音的人'探望'。话软乎乎，左手缺半根指头。"

    $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
    show player_char_img at left with dissolve
    player "费舍尔。"

    $ hide_all_chars("chen_captain_img")
    show chen_captain_img at left with dissolve
    chen_captain "他没报名。可他问的全是船主联盟的事：谁是头、多少条船、敢不敢跟公会拼。"

    chen_captain "公会要我们认罪，他要我们跟公会拼命。两拨人，两个心思。"

    $ hide_all_chars("stable_boy_img", "soldier_generic_img")
    show chen_captain_img at left with dissolve
    show stable_boy_img at right with dissolve
    xiao_liu "大人，我记得那人！他走的时候跟狱卒说，'再关几天，火候就到了'。火候……什么火候？"

    $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img")
    show player_char_img at left with dissolve
    player "把你们两边都逼到动手的火候。"

    $ evidence_count += 1
    $ fisher_husband_found = True
    $ hide_all_chars("chen_captain_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
    show chen_captain_img at left with dissolve
    chen_captain "贵人，您要真能查清……求您给我婆娘带句话：我没给陈家丢人，我们是清白的。"

    "你应下了。陈船老大、小六、海雀号的清白，还有费舍尔在牢里'等火候'那句话——都记下了。"

    "走出地牢，外头的阳光晃得你眯了眼。牢里那七个被冤了二十多天、却还硬撑着说'我们是清白的'的汉子，比港口里任何一份证据都更让你下定决心：这局，你管定了。"
    jump southern_investigate_loop


label si_ledger:
    $ investigate_ledger = True
    if southern_faction == "guild":
        "你以盟友身份进了公会账房，说要核对艾登堡的盐铁记录。没人拦你翻'密报'那一栏。"
    else:
        "公会账房进不去。赛琳找了个欠她人情的公会小吏，半夜放你进去翻了一刻钟。"
    ## 同上: 公会账房不能用主线的议事厅图
    scene bg tideport_office with fade
    "举报海雀号'走私军火'的那份密报，是匿名的——塞进举报箱，没署名。"

    "可你比对了日子：密报投进来那天，正是费舍尔在港里出现的第三天。"

    $ hide_all_chars("merchant_karl_img")
    show tavern_keeper_img at right with dissolve
    tavern_keeper "那阵子……有个内陆人常来翻我们的进出港册子，说是受公会委托核账。可公会从没派过这么个人。"

    $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img")
    show player_char_img at left with dissolve
    player "他翻册子，是在挑哪条船下手。"

    "海雀号不肯登记，又跑南北盐路，最显眼。费舍尔挑中它，递了假密报，公会顺水推舟扣了船。一场火，就这么点着了。"

    $ evidence_count += 1
    jump southern_investigate_loop


label si_inn:
    $ investigate_inn = True
    scene bg tideport_tavern with fade
    "费舍尔住过港西的'潮信客栈'。你赶到时，他已退房三天。"

    $ hide_all_chars("servant_generic_img")
    show servant_generic_img at right with dissolve
    inn_keeper "那位客官？走得急。不过有几样我记得——"

    inn_keeper "付房钱用内陆官炉铸的银锭，崭新，港里见不着这成色。房里火盆烧过纸，烧得一塌糊涂。"

    inn_keeper "他在这儿前后见过七八拨人，公会的、船主的，都有。"

    "你上楼看了那间空房。火盆灰里，扒出半张没烧透的纸——公文格式，边角还留着一点朱红官印。"

    "一个港口掮客，用内陆官银付账，烧的是带官印的公文。这人的来路，藏不住了。"

    $ evidence_count += 1
    jump southern_investigate_loop


label si_office:
    $ investigate_office_q = True
    scene bg tideport_harbor with fade
    $ hide_all_chars("noble_werner_img")
    show harbor_master_img at right with dissolve
    "港务官见你又来，脸色不好看。可你把手里的东西往桌上一摊，他的脸白了。"

    $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img")
    show player_char_img at left with dissolve
    player "费舍尔。内陆官银，内陆公文。港务厅介绍的'中间人'——介绍他的，到底是谁？"

    $ hide_all_chars("harbor_master_img", "player_char_img", "player_young_img", "player_teen_img", "player_child_img", "aldric_img", "guild_master_img", "old_salt_img", "sea_dog_img", "chen_captain_img", "blacksmith_wife_img")
    show harbor_master_img at right with dissolve
    harbor_master "……我就知道迟早有人查到这。他不是我介绍的。他拿着内陆来的文书，直接上门。那文书的印……我这把位子，不敢不接待。"

    player "什么印？"

    harbor_master "这话不能说。说了，活不过今晚。"

    harbor_master "我只透你一句：他背后那只手，比公会、比船主都大得多。你要聪明，查到这儿就该收手。"

    "他不肯再说。可'内陆''官印''大得多的手'——指向哪里，你心里有数了。"

    $ evidence_count += 1
    jump southern_investigate_loop


label si_done:
    $ hide_all_chars()
    scene black with dissolve
    "你把查到的摆开。费舍尔在牢里套船主的虚实，给公会递假密报，付账用内陆官银，烧的是带官印的公文。"

    "连港务官都不敢提的那只手，藏在这一切背后。"

    "够了。该回断锚，把公会和船主，按到同一张桌子上了。"
    return


label si_insider:
    $ investigate_insider = True
    $ evidence_count += 1
    scene bg tideport_harbor with dissolve
    "公会不是铁板一块。你找上一个对维斯帕新规矩早有怨言的老账房，请他喝了顿酒。"

    $ hide_all_chars("merchant_karl_img")
    show merchant_karl_img at right with dissolve
    guild_clerk "费舍尔那人？嘿，邪门。他来公会，不走大执事的门子——直接见维斯帕上头的几位老爷。"

    $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img")
    show player_char_img at left with dissolve
    player "维斯帕上头？公会还有人压得过大执事？"

    $ hide_all_chars("merchant_karl_img", "player_char_img", "player_young_img", "player_teen_img", "player_child_img", "aldric_img", "guild_master_img", "old_salt_img", "sea_dog_img", "chen_captain_img", "blacksmith_wife_img")
    show merchant_karl_img at right with dissolve
    guild_clerk "明面上没有。可那回费舍尔一来，几位老爷关起门嘀咕了半宿，第二天就定了拿海雀号开刀。维斯帕自个儿，未必清楚上头收了谁的话。"

    "你心里一凉。费舍尔背后那只手，能越过维斯帕，直接拨动公会高层。这局，比你想的还深。"
    jump southern_investigate_loop


label si_faction2:
    $ investigate_faction2 = True
    $ evidence_count += 1
    scene bg tideport_beach with dissolve
    "船主联盟也不是人人跟赛琳一条心。你撞见两个船主在背人处嘀咕。"

    $ hide_all_chars("soldier_generic_img")
    show soldier_generic_img at right with dissolve
    dissenter "……与其被公会慢慢吞了，不如早点投北边的。王廷的船一来，谁先递投名状，谁就能保条命，说不定还分块肉。"

    "另一个啐了他一口，可没敢大声。"

    "你退了出来，没惊动他们。船主联盟的刀看着齐整，心是散的。王廷还没动手，光是'要来'这个信儿，就够把这盘散沙吹得更散。"

    "怪不得费舍尔有恃无恐。他要的从来不是赢一场火并——是让整个港口，自己烂掉。"
    jump southern_investigate_loop


label si_together:
    $ investigate_together = True
    $ evidence_count += 1
    play music "audio/music/southern_corsair.ogg" fadeout 1.0 fadein 2.0 if_changed
    scene bg tideport_beach with fade
    "有一条线最险——费舍尔常去港西一处废弃的盐仓，深更半夜，从不带人。那地方三面临水，一面是船主的地盘。"

    $ hide_all_chars("corsair_img")
    show corsair_img at right with dissolve
    corsair "废盐仓？那是我们船主的地界。你一个内陆人摸进去，不等费舍尔，先得让我的人当贼打了。我陪你去。"

    $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img")
    show player_char_img at left with dissolve
    player "那地方危险。"

    corsair "所以才要我陪。"

    "她说得理所当然。你没再推。"

    scene bg tideport_ship with dissolve
    "后半夜，你跟着赛琳从水路摸进盐仓。她在这片港口长大，黑灯瞎火里走得比你白天还稳，一伸手就把你从一处暗坑边拽了回来。"

    $ hide_all_chars("corsair_img", "player_char_img", "player_young_img", "player_teen_img", "player_child_img", "aldric_img", "guild_master_img")
    show corsair_img at right with dissolve
    corsair "脚下看着点。这仓底的烂板，一脚踩穿，掉下去就是没顶的盐卤。"

    $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img")
    show player_char_img at left with dissolve
    player "你倒熟。"

    corsair "小时候在这儿躲过债。嘘——"

    "她忽然按住你，把你一起压进一堆烂盐袋后头。仓库那头，有灯。"

    "费舍尔来了。他不是一个人——对面那个一身不起眼的短打，可站姿笔直，是个军人。两人压着声说话，你只听清几个字：'……傍晚发兵……叫他们烧得再旺些……'"

    "赛琳的手还按在你背上。黑暗里两个人挤在一处，近得能听见彼此的呼吸。"

    "等那两人走了，你们才从盐袋后头出来。"

    corsair "军人。内陆口音。费舍尔背后，是王廷的人。你这一趟，捅到根上了。"

    "她看着你，黑暗里眼睛亮得很。"

    corsair "……也不知该谢你，还是该骂你。把我卷进这么大一摊事。"

    player "现在退还来得及。"

    "她笑了一声，伸手拍掉你肩上的盐粒，动作比她想表现的要轻。"

    corsair "都摸到这儿了，谁退谁是孙子。走，回去。这条线，够把那两个老顽固按到桌上了。"
    $ change_rel("rel_corsair", 6)
    jump southern_investigate_loop


## ============================================================
## 第三幕 · 备战（选联合后 call，逼退王室军队前的一天准备）
## ============================================================

label southern_prepare:
    play music "audio/music/battle_prepare.ogg" fadeout 1.0 fadein 2.0 if_changed
    scene bg tideport_tavern with fade
    "你选了最难走的一条路——在王室军队到来之前，让公会和船主拧成一股绳。"

    "从今夜到明天傍晚王室军队压境，只剩一天。一天里，你得做完平时一个月都未必办成的事。"

    ## ── 环节一：说服维斯帕联手 ──
    $ hide_all_chars("guild_master_img")
    show guild_master_img at left with dissolve
    guild_master "联手？跟船主那帮泥腿子？领主大人，您说笑。"

    $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img")
    show player_char_img at left with dissolve
    player "听清楚：王室军队不是来帮你的。费舍尔是王廷的人，点这把火，就是要逼出'港口大乱'，好让王室军队名正言顺进来——把整个港，连你的公会，一锅端。"

    "你把那半张烧剩的官文，连同港务官的话，摊在他面前。维斯帕的算盘，头一回打不响了。"

    menu:
        "跟他算账：王室军队进来，你公会几十年的家业归谁？（谋略）":
            $ change_stat("intrigue", 3)
            $ hide_all_chars("guild_master_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
            show guild_master_img at left with dissolve
            guild_master "……归王廷。账本、护航、放贷，全成了他们的。"
            guild_master "我维斯帕算了一辈子账，倒没算到这一笔。"

        "摊牌：你不联手，我现在就把证据给船主，让他们只冲你来（威逼）":
            $ change_stat("power", 2)
            $ hide_all_chars("guild_master_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
            show guild_master_img at left with dissolve
            guild_master "……领主好手段。罢了，刀架到脖子上，谁还分公会船主。"

    guild_master "公会的钱、护航队，我出。但有一条：保住港，公会的账本不能废。"

    $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
    show player_char_img at left with dissolve
    player "保住港再说。账本的事，活下来的人慢慢谈。"

    ## ── 环节二：说服老汉斯别趁乱报复 ──
    $ hide_all_chars("soldier_generic_img")
    show sea_dog_img at left with dissolve
    sea_dog "跟金锚那帮吸血鬼联手？渡鸦点头了，我老汉斯不点。这些年他们怎么逼我们的，你忘了我没忘！"

    $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img")
    show player_char_img at left with dissolve
    player "我没让你忘。我让你先分清，今晚谁要你的命。"

    player "公会逼你，逼的是钱。王室军队来了，要的是命，是整个港。先把要命的挡回去，钱的账，往后跟公会一笔一笔算。"

    menu:
        "搬出海雀号：你现在跟公会拼，那七条命就真没了（忠诚）":
            $ change_stat("loyalty", 2)
            $ hide_all_chars("sea_dog_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
            show sea_dog_img at left with dissolve
            sea_dog "……海雀号。好。看在那七条命的份上，我这口气先咽下。先打官军。"

        "实话：你们各自都打不过王室军队，合起来才有一线（声望）":
            $ change_stat("reputation", 2)
            $ hide_all_chars("sea_dog_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
            show sea_dog_img at left with dissolve
            sea_dog "一线……行。就这一回听你的。可这梁子，我跟公会没完。"

    ## ── 环节三：布防 ──
    $ hide_all_chars("corsair_img")
    show corsair_img at right with dissolve
    scene bg tideport_harbor with dissolve
    $ hide_all_chars("corsair_img", "player_char_img", "player_young_img", "player_teen_img", "player_child_img", "aldric_img", "guild_master_img")
    show corsair_img at right with dissolve
    corsair "两边都点头了？你这张嘴，比我这把刀管用。"

    corsair "可光合心不够。来的是王廷的分舰队，硬碰没赢面。怎么打？"

    corsair "我活了这么大，头一回觉得，光有刀和船不够使。这一仗要赢，得靠你那套内陆人的弯弯绕。说吧，领主——你脑子里那点鬼主意。"

    menu:
        "沉几条旧船，封死航道窄口，让大船进不来":
            $ change_stat("intrigue", 2)
            "你指着港口入口那道窄水。几条不能再用的旧船，灌满石头沉下去，王室军队的大舰就挤不进来，只能在外海干瞪眼。"
            corsair "……这主意够损，够好。我这就让人去办。"

        "让船主的快船散进外海，专咬王室军队的补给和侧翼":
            $ change_stat("power", 2)
            "你让快船趁夜散出去，不正面打，专咬补给船和落单的侧翼。蚊子叮不死人，能叮得人睡不着。"
            corsair "游击。我们最擅长。成。"

    ## ── 环节四：散证据 + 联络他国商船 ──
    scene bg tideport_beach with dissolve
    "可你心里清楚，真正能逼退王室军队的，不是沉船，也不是快船——是让它没法'名正言顺'。"

    "当夜，你把费舍尔的内陆官文、港务官的证词，连同这场火的来龙去脉，抄了十几份，连夜送上港里泊着的他国商船，送往下游两个自由港。"

    $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img")
    show player_char_img at left with dissolve
    player "告诉他们：明天傍晚，来看王室军队怎么'平乱'。他们要敢炮轰一个好端端的自由港，今天看戏的，明天就是下一个。"

    "消息像退潮一样，悄没声地铺了出去。到天亮，港外多了十几条挂各色旗号的商船——都等着看。"

    ## ── 环节五（可选）：救海雀号船员 ──
    if fisher_husband_found:
        $ hide_all_chars("corsair_img")
        show corsair_img at right with dissolve
        "趁备战的乱，赛琳带人摸进了港务厅地牢。等你赶到，陈船老大他们已经出来了。"
        $ hide_all_chars("corsair_img", "soldier_generic_img")
        show corsair_img at right with dissolve
        show chen_captain_img at left with dissolve
        chen_captain "贵人……你真把我们捞出来了。"
        $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img")
        show player_char_img at left with dissolve
        player "回去见陈嫂吧。仗，有我们打。"
        $ hide_all_chars("chen_captain_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
        show chen_captain_img at left with dissolve
        chen_captain "不。我海雀号的人，也是潮汐港的人。这一仗，算我们一份。"
        $ change_rel("rel_corsair", 5)
        "七个被关了二十多天的汉子，抄起家伙站进了队伍。这一仗，又多了七条不要命的硬骨头。"

    $ hide_all_chars()
    scene black with dissolve
    "该做的，一夜之间都做了。说服、布防、散信、救人。"

    ## ── 压境前夜：与赛琳（块16，恋爱线）──
    if corsair_romance:
        $ hide_all_chars()
        play music "audio/music/southern_corsair.ogg" fadeout 1.0 fadein 2.0 if_changed
        scene bg tideport_beach with fade
        "后半夜，你在海堤上找到赛琳。她一个人坐着，渡鸦号泊在脚下的水里，随浪轻轻晃。"

        $ hide_all_chars("corsair_img")
        show corsair_img at right with dissolve
        corsair "睡不着？"

        $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img")
        show player_char_img at left with dissolve
        player "你也是。"

        corsair "明天傍晚王廷的兵就到。我打过不少仗，可没一次像这回——赢面这么小，要护的东西这么大。"

        "她难得露出这样的神情。不是渡鸦船长，只是一个怕失去的人。"

        corsair "要是明天……我是说要是。你别为我做傻事。你是艾登堡的领主，你的命，不只是你自己的。"

        menu:
            "我们会赢。我答应你":
                $ change_rel("rel_corsair", 6)
                player "明天太阳落山的时候，我们俩还会站在这片海堤上。我答应你。"
                corsair "……你倒会哄人。"
                "她靠了过来，头搁在你肩上。海风凉，她靠过来的肩膀是暖的。"
                corsair "好。我信你这一回。"

            "无论明天怎样，我都不后悔来这一趟":
                $ change_rel("rel_corsair", 5)
                player "我来潮汐港，本为一条盐路。可走到今天，盐路成了最不要紧的事。遇见你，我不后悔。"
                "她没说话，只伸手握住了你的手。她的手心有常年握刀磨出的茧，糙，可你舍不得松开。"

        "那一夜剩下的时间，你们没再说话。海堤上两个人，看着同一片黑沉沉的海，等天亮。"

    "剩下的，交给明天傍晚那片海。"
    return


## ============================================================
## 恋爱支线 · 夜航（第一幕选边当晚 call，与赛琳够近时）
## ============================================================

label southern_night_voyage:
    play music "audio/music/southern_corsair.ogg" fadeout 1.0 fadein 2.0 if_changed
    scene bg tideport_beach with fade

    "你正要回客栈，赛琳堵在了栈桥口。"

    $ hide_all_chars("corsair_img")
    show corsair_img at right with dissolve
    corsair "急着睡？跟我来。带你看样东西——白天看不见的。"

    $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img")
    show player_char_img at left with dissolve
    player "这么晚，去哪？"

    corsair "海上。怕了？"

    "你没怕。你上了渡鸦号。"

    scene bg tideport_beach with dissolve
    "渡鸦号悄没声地滑出港口。喧嚣、火并、公会船主，全被甩在身后。"

    "离了岸，海忽然就大了。头顶的星密得吓人，脚下的浪一下一下，把船托起来又放下。"

    show corsair_img at right with dissolve
    corsair "白天的潮汐港，是个抢钱抢地盘的烂泥塘。可一到海上……"

    "她张开手臂，像要把整片夜海揽进怀里。"

    corsair "这儿没有公会，没有王法，没有谁能在你的册子上记一笔。这片海，谁也圈不住。这才是我要守的东西。"

    menu:
        "问她：值得吗？为这片海，跟整个公会、整个王国作对":
            corsair "值不值，不用赢面算。"
            corsair "我爹烧死在这片海上。我要是连这点自由都守不住，那他白死，我也白活。"
            "她说得很轻，可你听出那底下压着的东西，比港里任何一把刀都硬。"
            $ change_rel("rel_corsair", 8)

        "只是站在她身边，陪她看海":
            "你没说话。有些时候，话是多余的。"
            "她侧头看了你一眼，没说什么。可你们之间那点东西，在夜风里悄悄变了。"
            $ change_rel("rel_corsair", 6)

    "渡鸦号在海上飘了大半夜。回港时，东边天际才泛起一点灰白。"

    show corsair_img at right with dissolve
    corsair "下了船，你还是艾登堡的领主，我还是港里的渡鸦。可今晚这片海，是咱俩的。"

    "她跳上栈桥，没回头。可你知道，有些东西从今夜起，不一样了。"

    "你在原地站了一会儿，海风把渡鸦号的影子拉得很长。你来潮汐港之前，从没想过会在一个海盗船长的甲板上，看一整夜的星。"

    $ hide_all_chars()
    scene black with dissolve
    return


## ============================================================
## 第二幕 · 第一刀
## ------------------------------------------------------------
## 揭"第三方挑动"：王廷想借两派火并吞港。
## 含赛琳恋爱线门槛（rel_corsair >= 30 触发 confirm，>= 80 深化）。
## ============================================================

label southern_act2:

    play music "audio/music/harbor_waves.ogg" fadeout 1.0 fadein 2.0 if_changed

    scene bg tideport_harbor with fade
    pause 0.3

    centered "{size=+6}第二幕 · 第一刀{/size}"
    pause 1.2
    scene bg tideport_harbor with dissolve

    voice "audio/narration/south_a2_01.mp3"
    "天没亮你就醒了。海雾压在桅杆上，整个港口像泡在一碗冷汤里。"

    voice "audio/narration/south_a2_02.mp3"
    "你要找的那条船，叫海雀号。就是被公会扣下、点着这场火的那条。它锁在最里头的死角栈桥，铁链缠了三圈。"

    show aldric_img at left with dissolve

    aldric "大人，这船看着不像走私的。走私的船吃水深，它浮得高——舱里没多少货。"

    $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img")
    show player_char_img at left with dissolve
    player "空船，却扣了人。我想上去看看。"

    ## ── 上船：按第一幕站队给不同的开门方式 ──
    if southern_faction == "guild":
        "栈桥口站着公会的人。你昨晚站了公会，这会儿一亮印戒，他们就让开了。"
        $ hide_all_chars("guild_master_img", "corsair_img")
        show guild_master_img at left with dissolve
        guild_master "领主大人想看？请便。公会没什么见不得人的。"
        "维斯帕话说得敞亮。敞亮得让你更想看。"
    elif southern_faction == "pirates":
        "栈桥口站着公会的人，本来要拦。赛琳的两个船员从水边摸上来，一左一右站到你身后，那两个人就改了主意。"
        $ hide_all_chars("corsair_img", "guild_master_img")
        show corsair_img at right with dissolve
        corsair "我说过，夜里的码头不安全。所以我让人跟着你。"
    elif southern_faction == "neutral":
        "栈桥口的看守认得你——昨晚压着两边谈的就是你。他犹豫了一下，到底没拦。"
        $ hide_all_chars("dockhand_img")
        show dockhand_img at right with dissolve
        dockhand "您是来看公道的。我让开。出了事别说是我放的。"
    else:
        "栈桥口没人。昨夜你谁都没站，也就没人替你开门，也没人盯着你。雾帮了你。"

    pause 0.3
    scene bg tideport_ship with dissolve

    "你踩着结霜的跳板上了海雀号。甲板是空的，结着一层薄霜——这船被扣了二十多天，没人上来过。"

    "缆绳盘得整整齐齐，帆叠得方方正正。一条要跑路走私的船，不会收拾得这么规矩。出事那天，船上的人大概以为，过一遍盘查就能放行。"

    "你顺着舱梯下到底舱。霉味、咸味，还有一点没散尽的鱼腥。"

    "你一处处搜过去：货舱的暗格是空的，压舱石底下没东西，连水手舱的铺位都翻了一遍。几袋粗盐，一卷新绳，半桶焦油——干干净净。"

    "底舱更空。没有兵器，没有违禁货，什么劫掠王国船队的赃物都没有。"

    "公会说这船走私军火。可你把整条船翻了个底朝天，连一把多余的刀都找不出来。"

    "一条空船，凭什么扣二十多天、押七条人命？除非——扣这条船，本就不是为了船上有什么。"

    "你正要走，听见货堆后头有动静。你和奥尔德里克对视一眼，他悄悄按住了腰间的短刀。这种地方，动静往往意味着麻烦。"

    show ship_boy_img at right with dissolve

    ship_boy "别……别叫人。我不是贼。这是我的船。"

    "一个少年从盐袋后头爬出来。手腕上有勒过的红痕——被绑过，又挣脱了。"

    $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img")
    show player_char_img at left with dissolve
    player "海雀号的人？他们不是被公会带走了吗。"

    ship_boy "带走了。就剩我躲下来。我想等船放出去，把它开走。"

    ship_boy "大人，我们没走私。我对着大海发誓。我们就是运盐的。"

    menu:
        "那公会为什么咬定你们走私？":
            $ change_rel("rel_corsair", 2)
            player "空舱一桶盐，公会凭什么说你们走私军火？"

        "先别急。慢慢说，那天到底发生了什么":
            $ change_rel("rel_corsair", 4)
            player "你先坐下。手给我看看——这伤得包。慢慢说，那天的事，一件一件讲。"
            "少年愣了一下。大概没料到一个内陆来的贵人会先看他的手。"

    ship_boy "那次搜查的前一天，来了个人。穿得体面，不像码头上的。他说他是掮客，帮人牵线买卖的。"

    ship_boy "他跟船老大讲，公会盯上海雀号了，要拿我们'立规矩'，抓了人就不会放——让我们别坐着等，趁早联络船主联盟，硬一把。"

    ship_boy "船老大没听他的。船老大说我们清白，怕什么。"

    ship_boy "现在想想……要是那天听了那人的，我们先去找了船主联盟，是不是公会就有理由说我们'通匪'了？那人……是不是一早就盼着我们去？"

    "一个吓坏的孩子，无意间说中了要害。费舍尔劝海雀号'硬一把'，本就不是为了帮他们——是为了给公会递一把刀。"

    ship_boy "第二天，公会就来了。说接到密报，海雀号给船主联盟运军火。"

    "你心里那处一直对不上的地方，咔哒一声，对上了一点。"

    player "那个掮客，叫什么？长什么样？"

    ship_boy "他说他叫费舍尔。不高，话很软，左手缺半根小指。口音……不是海边的，是内陆的。像王都那边。"

    "王都那边。"

    "光凭一个吓坏的少年一面之词，对质不了公会和船主。你得拿到实打实的东西。"

    $ hide_all_chars()
    scene black with dissolve
    call southern_investigate from _call_southern_investigate

    pause 0.5
    scene black with dissolve

    ## ============================================================
    ## 第二幕 · 拼图
    ## ============================================================

    play music "audio/music/tension.ogg" fadeout 1.0 fadein 1.5 if_changed
    scene bg tideport_tavern with fade

    "你回到断锚，把少年的话在心里摆开。"

    "一个内陆口音的'掮客'，搜查前一天去找海雀号，劝他们硬抗。"

    "同一天，公会接到'密报'，说海雀号走私军火。"

    "船是空的。密报是假的。劝人硬抗的，和递假密报的，会不会是同一只手？"

    ## ── 调取已知信息：玩家若谋略/声望高，自己就能拼出动机 ──
    if intrigue >= 45 or reputation >= 45:
        "你不用别人提醒，也想得通这背后图什么。"
        "潮汐港三百年不归王法。王廷要它，缺的从来不是兵，是借口。"
        "让港口自己打起来，打到港务厅扛不住，开口'请王室军队入港平乱'——借口就有了。船一进来，就不走了。"
        $ change_stat("intrigue", 4)
    else:
        "可一个掮客，挑动两伙人互相捅刀，图什么？这上头你还想不透。"

    "门开了。该来的都来了——赛琳从海上来，维斯帕从街上来。你昨天没让他们散，今天他们就还坐在一张桌子的两头。"

    show corsair_img at right with dissolve
    show guild_master_img at left with dissolve

    $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img")
    show player_char_img at left with dissolve
    player "你们两个，谁认识一个叫费舍尔的掮客？左手缺半根小指，内陆口音。"

    "维斯帕的脸先变了。只变了一瞬，又收住。可你看见了。这个把喜怒都锁在算盘后头的人，听见'费舍尔'三个字，眼里闪过的不是疑惑，是惊。他认得这名字，而且认得得不情愿。"

    $ hide_all_chars("guild_master_img", "corsair_img", "ship_boy_img", "dockhand_img", "servant_generic_img", "soldier_generic_img", "merchant_karl_img", "blacksmith_wife_img", "farmer_rep_img", "old_woman_img", "noble_werner_img", "stable_boy_img", "storyteller_img")
    show guild_master_img at left with dissolve
    guild_master "……港务厅介绍来的中间人。说能帮公会和外港牵线。我见过两面。"

    corsair "我也见过。他来跟我们船主递过话，说公会要赶尽杀绝，劝我们先下手。"

    "两个人对看了一眼。这一眼里头，头一回没有火，只有一样东西：两边都被同一个人喂了相反的话。"

    guild_master "他跟你们说公会要赶尽杀绝？"

    corsair "他跟你们说我们要运军火？"

    "桌上静了。窗外有海鸥在叫。"

    $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
    show player_char_img at left with dissolve
    player "递假密报给公会的是他。劝船主动手的也是他。海雀号是空的——这场火，第一刀不是你们谁捅的，是他点的。"

    if evidence_count >= 2:
        "你把这两天查到的，一样样摊在桌上：海雀号空船的实情，登记册里对不上的密报日期，客栈烧剩的内陆公文，港务官那句'背后那只手大得多'。"
        $ hide_all_chars("guild_master_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
        show guild_master_img at left with dissolve
        guild_master "……这些，你两天就查全了？"
        $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
        show player_char_img at left with dissolve
        player "我查的时候，你们俩还忙着算计怎么弄死对方。"
    else:
        "你把少年水手的话原原本本说了一遍。一个吓坏的孩子，编不出这么严丝合缝的局。"

    $ hide_all_chars("guild_master_img", "corsair_img")
    show guild_master_img at left with dissolve
    show corsair_img at right with dissolve
    guild_master "费舍尔……港务厅介绍他时，我就觉得来路不对。可他递的消息，条条戳在我心坎上——船主要反、要抢码头。我信了。"

    corsair "我也信了。他说公会要血洗船主，我差点带人就冲过去。"

    "两个人头一回没抬杠。被同一只手当刀使的人，在彼此脸上看见了自己的蠢。"

    menu:
        "挑明：你们再斗，就是替费舍尔背后那只手干活（谋略）":
            $ change_stat("intrigue", 2)
            $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img")
            show player_char_img at left with dissolve
            player "你们每多砍一刀，那只手就多一分'平乱'的借口。斗到两败俱伤，渔翁是谁，不用我说。"
            $ hide_all_chars("guild_master_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
            show guild_master_img at left with dissolve
            guild_master "……渔翁。好一个渔翁。"
        "先压旧账：现在不是算账的时候（声望）":
            $ change_stat("reputation", 2)
            $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img")
            show player_char_img at left with dissolve
            player "公会怎么逼船主，船主怎么恨公会，今天先搁着。今天还咬死对方，明天就一起被人收尸。"
            corsair "……内陆来的，你这张嘴，比我的刀还狠。"

    $ hide_all_chars("guild_master_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
    show guild_master_img at left with dissolve
    guild_master "那依领主之见，眼下怎么办？"

    $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img", "harbor_master_img", "tavern_keeper_img", "royal_admiral_img")
    show player_char_img at left with dissolve
    player "先弄清那只手是谁、要做什么。在那之前，公会和船主，谁都不许再动刀。"

    "维斯帕和赛琳对视一眼。三十年的仇没那么容易放下，可这一刻，他们都没反对。"

    pause 0.5

    ## ============================================================
    ## 第二幕 · 赛琳恋爱线门槛（仿 Elena）
    ## ============================================================

    if rel_corsair >= 30:
        $ hide_all_chars()
        scene bg tideport_beach with dissolve
        play music "audio/music/southern_corsair.ogg" fadeout 1.5 fadein 2.0 if_changed

        "维斯帕回公会查费舍尔的底。剩下的事要等夜里。赛琳说她想透透气，叫你陪她走一段海堤。"

        show corsair_img sad at right with dissolve

        corsair "我在这港口混了十二年。被人骗过，也骗过人。可这回……我差点提着刀冲进公会，替别人杀人。"

        corsair "要不是你非要去看那条空船，我这辈子都不会知道，是谁拿我当刀使。"

        menu:
            "你不是刀。是这港口少有的、肯先问一句的人":
                $ corsair_romance = True
                $ change_rel("rel_corsair", 20)
                $ log_decision("南境游记", "在海堤上向赛琳交心")

                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "你不是谁的刀。这港口动刀的人多，肯先问一句'为什么'的人少。你是后一种。"

                "她停下脚步，看了你很久。海风把她额前的碎发吹起来。那一瞬间，她脸上那层惯常的、连嘲带刺的硬壳松了一松，底下是个比谁都清楚自己在守什么、也比谁都怕守不住的人。"

                $ hide_all_chars("corsair_img", "player_char_img", "player_young_img", "player_teen_img", "player_child_img", "aldric_img", "guild_master_img")
                show corsair_img at right with dissolve
                corsair "内陆来的贵人，嘴倒甜。"

                "她嘴上这么说，却没躲开你的目光。"

                corsair "这片海认死理：救过你命的人，你得记一辈子。"
                corsair "可你昨天救的不是我的命。是我的手——没让它替别人去沾不该沾的血。这个，我记得更重。"

                ## ── 恋爱线推进：赛琳身世 / 渡鸦号 ──
                "海浪一下一下拍着海堤。她难得没有戒备，你也难得不急着走。"

                menu:
                    "渡鸦号，跟了你多久？":
                        corsair "十二年。它原先不叫渡鸦号，叫'海燕'，是我爹的船。"

                        corsair "我爹也是船主。那年公会的前身——一伙拿着王国特许状的商团——说我爹的船走私，扣了船，逼他认罪。"

                        corsair "我爹不肯认他没做的事。他们就把海燕连人带船，一把火烧了。"

                        "她的声音很平，平得像在讲别人的事。可你看见她攥着刀鞘的手，指节发白。"

                        corsair "我从灰里把船的骨架拖出来，重修了一遍，改名渡鸦。乌鸦跟着死人走——我要让烧船的人知道，这只乌鸦记仇。"

                        player "所以海雀号被扣，你才那么急。"

                        corsair "你看得真透。每次看见有人被'走私'两个字扣下船，我看见的都是我爹。"

                        $ change_rel("rel_corsair", 8)

                    "你恨公会，为什么不干脆离开这个港？":
                        corsair "走了，这港口就真成公会一家的了。"

                        corsair "老汉斯那样的老骨头，离了港活不下去。我走了，谁替他们说话？"

                        "她顿了顿，望着黑沉沉的海。"

                        corsair "再说，这片海是我爹葬身的地方。我不走。我要看着它一直自由下去。"

                        $ change_rel("rel_corsair", 6)

                "你没再追问。有些事，她愿意说多少，是多少。"

                "可这一夜之后，你看她的眼神，和她看你的，都和先前不一样了。"

                if rel_corsair >= 80:
                    ## 恋爱深化（高好感才解锁，仿 Elena rel>=80）
                    "她忽然伸手，把你被海风吹乱的衣领抚平。这个动作她自己大概都没察觉。"
                    corsair "等这事了了……你那条北边的盐路，我亲自给你押船。"
                    corsair "不为艾登堡的旗。为你。"
                    "她说完自己先别过头去看海，耳根有点红。渡鸦船长的耳根。"

                    "你没去看她的脸，只是在她身边坐下。两个人之间隔着一掌的距离，谁也没去填，可谁也没挪开。"

                    "海堤下，渡鸦号随浪轻轻摇。远处港口的灯火明明灭灭。这一刻没有公会，没有王室军队，没有明天的仗——只有海风，和身边这个人的呼吸。"

            "现在先别说这些。费舍尔还没揪出来":
                $ change_rel("rel_corsair", 5)
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "这些话等抓住费舍尔再说。现在松一口气，太早。"

                $ hide_all_chars("corsair_img", "player_char_img", "player_young_img", "player_teen_img", "player_child_img", "aldric_img", "guild_master_img")
                show corsair_img at right with dissolve
                corsair "……也对。是我贪那点海风了。"
                "她笑了一下，那笑里有点你看不太懂的东西，很快就被她收进了惯常的镇定里。"

                "海风从海堤那头吹过来，带着夜里的凉。你们并肩站了一会儿，谁也没再开口。有些话没说出口，可不知为什么，你觉得她都听见了。"

        $ hide_all_chars()
        scene black with dissolve

    ## ============================================================
    ## 第二幕收束 + 第三幕钩子
    ## ============================================================

    play music "audio/music/southern_scheme.ogg" fadeout 1.0 fadein 1.5 if_changed
    scene bg tideport_office with fade

    "拼出真相的当夜，你没让消息走漏。你跟维斯帕、赛琳定下计：趁费舍尔还以为自己天衣无缝，连夜把他扣下。"

    "公会的护卫封了港务厅前后门，船主的人盯死了码头每一条能出海的船。一张网，悄悄收紧。"

    "你带人摸进港务厅。费舍尔住的那间门虚掩着，里头还亮着灯。"

    "可你推门进去——房是空的。床没睡过，文书烧了一半，火盆里还有余温。他走得很急，就在你们收网的前一刻。"

    "桌上压着一张没来得及带走的纸条，几个字：'火候已到，请主上发兵。'墨迹还没干。"

    "他不是逃命，是去报信——告诉那只'大得多的手'：潮汐港这锅水，烧开了。"

    show corsair_img at right with dissolve
    show guild_master_img at left with dissolve

    corsair "跑了。"

    guild_master "不是跑。是去报信了。"

    "维斯帕站在窗前，望着港口外头那片黑沉沉的海。你顺着他的目光看过去。"

    play music "audio/music/southern_fleet.ogg" fadeout 1.5 fadein 2.0 if_changed
    scene bg tideport_fleet with dissolve

    "天边有光。低得不像星——一排一排的桅灯，正从外海往港口压过来。"

    "消息像瘟疫一样在港口里炸开。有人连夜往船上搬家当，有人把铺子的门板钉死，有人抱着孩子往山里跑。三百年没挨过兵灾的潮汐港，第一次尝到恐惧的味道。"

    $ hide_all_chars("guild_master_img", "corsair_img")
    show guild_master_img at left with dissolve
    guild_master "王廷的'护港分舰队'。打着平乱的旗号。比我想的快。"

    guild_master "费舍尔不是去报信。他是来确认我们打到了哪一步——好让那支船队，名正言顺地进港。"

    $ hide_all_chars("corsair_img", "guild_master_img")
    show corsair_img at right with dissolve
    corsair "什么平乱。他们要的是这个港。"

    "两个昨天还要拔刀相向的人，此刻并肩站在同一扇窗前，看着同一片灯火。"

    $ hide_all_chars("player_char_img", "corsair_img", "ship_boy_img", "dockhand_img")
    show player_char_img at left with dissolve
    player "港口还有几天？"

    corsair "顺风的话，他们明天傍晚就到。"

    "几天？不。是几个时辰。"

    pause 1.5
    scene black with dissolve

    centered "{size=+5}第二幕 · 完{/size}"
    pause 1.2
    if corsair_romance:
        centered "{size=+3}费舍尔点了第一刀就跑了。剩下的烂摊子和那支逼近的船队，你和她一起扛。{/size}"
    else:
        centered "{size=+3}王室军队压境。这一回，潮汐港要么拧成一股，要么不剩一块板。{/size}"
    pause 2.0

    $ persistent.southern_dlc_progress = 2
    $ southern_quest_stage = 2

    jump southern_act3

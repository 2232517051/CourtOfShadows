## ============================================================
## 第一章深化：新主登基 — 内心与领地
## chapter1_deepening.rpy
## 父亲坟前 / 首次巡逻 / 领主法庭 / 市场秘密
## 艾琳娜的第一课 / 老兵的故事 / 地窖秘密 / 城墙日落
## ============================================================

## ── 深化剧情标记 ──
default ch1_deep_patrol_done = False
default ch1_deep_court_held = False
default ch1_deep_market_visited = False
default ch1_deep_father_grave = False
default ch1_deep_elena_first_lesson = False
default ch1_deep_old_guard_story = False
default ch1_deep_cellar_found = False
default ch1_deep_sunset_watched = False

default ch1_deep_bridge_choice = ""        # "repair" / "note" / "villagers"
default ch1_deep_scouts_choice = ""        # "pursue" / "report" / "traps"
default ch1_deep_sheep_verdict = ""        # "split" / "fences" / "fine"
default ch1_deep_widow_verdict = ""        # "pardon" / "pay" / "work"
default ch1_deep_tax_verdict = ""          # "audit" / "trust_collector" / "trust_merchant"
default ch1_deep_blackmarket_choice = ""   # "shutdown" / "infiltrate" / "buy"
default ch1_deep_cellar_choice = ""        # "seal" / "secret" / "tell"
default ch1_deep_guard_funeral = ""        # "military" / "peaceful" / "tower"

## ============================================================
## 场景一：父亲的坟前 (~220行)
## ============================================================

label ch1_deep_father_grave:

    $ play_music("audio/music/sad_theme.ogg", fadein=3.0)
    $ set_mood("melancholy")

    scene bg forest_path with dissolve

    "清晨的薄雾还没有散去。"

    "你独自走出了城堡的后门，沿着一条被杂草掩没了大半的石板路向东走去。露水打湿了你的靴子，冷意从脚底蔓延上来。"

    "奥尔德里克跟在你身后十步远的地方，不言不语。你没有回头，但能听到他那双旧皮靴踩过落叶的声音——沙沙，沙沙，像是一个忠实的影子。"

    "你知道他不会走近，除非你主动开口。这是他侍奉了两代人后学会的分寸感。"

    "小路穿过一片白桦林。树干在雾气中泛着银白色的光，像是一排排沉默的哨兵。风吹过树梢，带来远处河水的潮湿气息。"

    "十五分钟后，你看到了它。"

    scene bg church with dissolve

    "一块灰色的石十字架，立在一棵老橡树下。没有围栏，没有雕饰，甚至连基座都是用普通的河石砌成的。"

    "上面只刻着一行字：卡尔·冯·艾登，1298—1347。"

    "就这些了。没有头衔，没有铭文，没有'忠诚的领主'或'慈爱的父亲'之类的话。父亲生前留下遗嘱，说一切从简。"

    "你在坟前站定。膝盖微微发软，不是因为走路累了，而是有一种说不清的力量在把你往下拽。"

    "你听到身后的脚步声停了。奥尔德里克大概在二十步开外的白桦树旁站住了。"

    "清晨的空气带着泥土和落叶腐烂的气味，有一丝甜，更多的是苦涩。"

    "你蹲了下来，用手拂去了墓碑上的落叶和灰尘。石头冰冷粗糙，触感像是触碰了时间本身。"

    "你张了张嘴，却发现不知道该说什么。"

    "……"

    "然后你开了口。声音很轻，像是怕吵醒什么人。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "……父亲。"

    "没有回应。只有风。"

    player "我回来了。"

    "你的声音在雾气中消散，像投入池塘的小石子，连涟漪都看不真切。"

    player "对不起，回来晚了。你走的时候……我不在。"

    "你低下头，盯着墓碑前泥土上的一丛野草。有几朵小小的紫色花，倔强地从石缝里钻出来。"

    player "他们说你走得很安详。但我知道……你一辈子都不安详。你只是不想让别人看到罢了。"

    "你顿了顿。"

    player "这座城堡比我记忆中的要破旧。城墙有三处需要修补，粮仓的存粮只够撑过冬天。你都知道的，对吗？你什么都知道，只是……来不及了。"

    $ hide_all_chars()
    "你闭上眼睛。"

    "一段记忆从脑海深处浮了上来——不是你刻意去想，而是它自己来找你的。"

    ## ── 回忆：骑马 ──

    scene black with dissolve
    pause 0.5

    "——你七岁。夏天。"

    scene bg forest_path with dissolve

    "父亲牵着一匹枣红色的老马，走在城堡外的草地上。你坐在马背上，两只小手死死抓着缰绳，浑身僵硬得像块木板。"

    "马每走一步，你就觉得自己要掉下来。"

    "'放松。'父亲说，声音低沉而平稳。他走在马的左侧，一只手搭在马鞍上，另一只手护着你的腿。"

    "'我害怕。'你说。"

    "'害怕是对的。'父亲说，'害怕说明你在认真对待它。但你不能让害怕决定你的动作。'"

    "'那我该怎么办？'"

    "父亲停下脚步，抬头看着你。阳光落在他的脸上，他的眼睛是深棕色的，像秋天的泥土。"

    "'你要学会和害怕一起骑马。'他说，'它是你的乘客，不是你的骑手。'"

    "然后他松开了手。"

    "你的心一下子提到了嗓子眼。但老马只是慢悠悠地向前走着，不紧不慢。风吹过你的头发。你能闻到草的味道，马汗的味道，还有远处炊烟的味道。"

    "你没有摔下来。"

    "你回头看父亲。他站在原地，双臂交叉，嘴角有一个极浅的弧度——那是他最接近微笑的表情。"

    ## ── 回到现实 ──

    scene bg church with dissolve

    "你睁开眼睛。泪水不知什么时候已经流了下来。"

    "你用袖子擦了擦脸，深呼吸了好几次，才让自己的声音稳住。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我现在……要学会和很多东西一起骑马了。害怕，孤独，还有你留下的那些……我还看不懂的谜。"

    player "我不知道自己能不能做好。但我会试。"

    $ hide_all_chars()
    "你站起身来。晨雾开始消散，阳光从云层的缝隙中落下来，在墓碑上投下金色的光斑。"

    "你从腰间抽出了短剑。剑柄上镶着家族的徽章——一只展翅的金鹰。"

    menu:
        "将剑放在墓碑前「这是我的誓言——我会用力量守护这片土地」":
            $ log_decision("第一章深化", "以剑宣誓")
            $ change_stat("power", 8)

            "你单膝跪地，将短剑横放在墓碑前。剑身上映出了你的倒影——一张年轻的、倔强的脸。"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "父亲，我以艾登家族的名义起誓——我会成为你未能成为的那种领主。不是仁慈，不是残暴，而是足够强大，强大到没人敢欺负我们的人。"

            $ hide_all_chars()
            "你把短剑从墓碑前拾起，剑柄被露水浸得冰凉。清晨的冷风灌进衣领，带走了最后一丝犹豫。"

            "你拿起剑，重新插回剑鞘。金属碰撞的声响清脆而坚决。"

        "采一束野花，放在墓碑前默默祈祷「愿神灵庇佑您的灵魂」":
            $ log_decision("第一章深化", "献花祈祷")
            $ change_stat("faith", 8)

            "你在墓碑旁找到了那丛紫色的野花，小心翼翼地连根采下。又从不远处摘了几朵白色的雏菊。"

            "你把花束放在墓碑前，然后双手合十，低下了头。"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "……愿上主赐予您安息。愿您的灵魂在彼岸找到您在此世未曾拥有的平静。"

            $ hide_all_chars()
            "你不确定自己信的是哪个神。但此刻，你愿意相信——在某个地方，父亲能听到你的声音。"

            "风吹过，花瓣微微颤动，像是一个无声的回应。"

        "只是……和他说说你的害怕「父亲，我很怕。真的很怕。」":
            $ log_decision("第一章深化", "坦诚倾诉恐惧")
            $ change_stat("loyalty", 5)
            $ change_stat("reputation", 3)

            "你什么都没做。你只是又蹲了下来，把额头抵在冰冷的墓碑上。"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "……父亲，我不想装了。"

            player "我很怕。真的很怕。每天早上醒来的第一个念头就是——我还不够格。我不知道怎么当一个领主。我甚至不知道怎么不让别人看出我在害怕。"

            player "他们都看着我，等着我做决定。可我……我还只是个孩子。你走的时候我才二十二。谁家二十二岁就要扛起一个领地啊。"

            "你的声音在最后碎裂了。你用力咬住嘴唇，直到尝到了血腥味。"

            player "……但我不会逃。这一点我可以向你保证。"

            $ hide_all_chars()
            "你在那里待了很久。久到露水打湿了你的膝盖，久到晨雾散尽，阳光完全照进了树林。"

    "你站起身，转身向回走。"

    hide player_char_img
    show aldric_img at right with dissolve

    $ hide_all_chars()
    "奥尔德里克就站在白桦树旁。他的老脸上看不出什么表情，但你注意到他的眼眶微微泛红。"

    "他没有问你说了什么。他只是默默地和你并肩走了一段，然后开口道："

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "大人……"

    aldric "您父亲生前有一句话，我一直记得。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "什么？"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "他说——'我种下的不是权力，不是领地。我种下的是一个人。'"

    "他顿了顿，看向远处那座在晨光中渐渐清晰的城堡。"

    aldric "他种下的种子已经发芽了。"

    $ hide_all_chars()
    "你没有回答。但你加快了脚步。"

    "城堡在等着你。"

    hide aldric_img with dissolve

    $ ch1_deep_father_grave = True

    return

## ============================================================
## 场景二：第一次巡逻 (~230行)
## ============================================================

label ch1_deep_patrol:

    $ play_music("audio/music/main_theme.ogg", fadein=2.0)
    $ set_mood("adventure")

    scene bg castle_exterior with dissolve

    show captain_img at right with dissolve

    captain "大人，马已经备好了。"

    "雷恩站在城堡大门前，身穿全套巡逻甲。他的那匹黑色战马在旁边打着响鼻，蹄子不安分地刨着地面。"

    captain "我挑了城堡里最温顺的母马给您。她叫'灰烬'，虽然名字不吉利，但脾气好得像只老狗。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "多谢。我的骑术……可能不如你期望的那么好。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "不需要多好。今天的巡逻以观察为主。您需要了解自己的领地——每一条路，每一座桥，每一个可能藏兵的山谷。"

    "你翻身上马。灰烬果然温顺，只是轻轻地晃了晃耳朵。"

    captain "走吧。先沿北线走，过河桥，穿松林，然后绕到东边的农场区。全程大约三个时辰。"

    hide captain_img with dissolve

    scene bg forest_path with dissolve

    "你们出了城堡，沿着北面的土路策马而行。"

    "清晨的阳光从树冠间漏下来，在路面上洒下斑驳的光影。空气里弥漫着松脂和湿土的气味。远处传来啄木鸟笃笃笃的敲击声，节奏均匀得像一个不知疲倦的鼓手。"

    show captain_img at right with dissolve

    captain "这条路是领地的主动脉。从城堡到北面的松林村，快马半个时辰。运粮车大概需要两个时辰。"

    "雷恩一边骑马一边指点着沿途的地形。"

    captain "看那边——那片山坡后面有一个天然的凹地。如果有敌人从北面来，可以在那里设伏。五十个弓箭手就能让三百人的队伍寸步难行。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你对这片地形了如指掌。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "您父亲要求的。他说，'了解你的土地，就像了解你手中剑的每一道纹路。'"

    $ hide_all_chars()
    "雷恩的声音在提到你父亲时微微一顿，然后很快恢复了平稳。"

    "你们继续向北，经过了两个小村子。村民们看到领主巡逻队经过，纷纷停下手中的活计，有人行礼，有人只是目送。你能感受到那些目光里混杂着好奇、期待和不确定。"

    ## ── 遭遇一：断桥 ──

    "大约一个时辰后，你们来到了一条河边。"

    "河水不深，但水流湍急。一座木桥横跨其上——或者说，曾经横跨其上。桥面中间断了一截，木板斜斜地插在水里，像一排歪掉的牙齿。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "该死。"

    "雷恩勒住马，脸色沉了下来。"

    captain "这座桥断了至少有两周了。桥对面是柳溪村，住着三十多户人家。也就是说，他们已经被切断了两周。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "为什么没有人上报？"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "可能报了。但您还没正式接手时，这些事……可能就搁置了。"

    "你看着断桥，然后看向对岸。隐约可以看到几缕炊烟。"

    menu:
        "下令立刻修桥「调人手过来，今天就开始」":
            $ log_decision("第一章深化", "立刻下令修桥")
            $ change_stat("wealth", -3)
            $ change_stat("loyalty", 8)
            $ ch1_deep_bridge_choice = "repair"

            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "传我的命令——今天下午就调工匠过来。我要这座桥三天之内修好。"

            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "大人，修桥需要木材和人力。这笔开支……"

            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我知道。从城堡的储备金里出。"

            "雷恩微微点头。你能看到他眼中一闪而过的赞许。"

            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "明白了。我会安排。"

            $ hide_all_chars()
            "你不经意间回头——河对岸，几个村民站在断桥那头远远地望着你们。他们可能听不清你说了什么，但他们看到了你停下来，看到了你指着桥说了很多话。"

            "有时候，看到就够了。"

        "记下来，回去再统一安排「这不是唯一需要修的东西」":
            $ log_decision("第一章深化", "记录断桥稍后处理")
            $ ch1_deep_bridge_choice = "note"

            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "记下来。回去后我要整理一份全部基础设施的维修清单，统一调度人力和预算。"

            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "……好的，大人。"

            $ hide_all_chars()
            "雷恩的语气平淡，但你能感觉到他有一丝失望。不过这是更理性的选择——你不能见一个修一个，那样很快就会把有限的资源耗尽。"

            "你看了一眼对岸，在心里默默说：再等几天。"

        "让柳溪村的人自己修「他们的桥，他们的责任」":
            $ log_decision("第一章深化", "让村民自己修桥")
            $ change_stat("power", 5)
            $ ch1_deep_bridge_choice = "villagers"

            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "传话给柳溪村——桥是他们用得最多的。让他们自己组织人手修。领地可以提供工具，但人力自理。"

            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "大人……柳溪村以老弱居多。年轻人大都去了南边的矿场做工。"

            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "那就让他们想办法。领主不能事事包办。"

            $ hide_all_chars()
            "雷恩没有再说什么。但他策马转身时，你看到他的嘴角抿成了一条直线。"

            "你告诉自己这是对的。你不能当一个烂好人。但胃里那一点微妙的不适感，一直到你们离开那条河才慢慢消散。"

    ## ── 遭遇二：边境斥候 ──

    scene bg forest_path with dissolve

    "你们继续向东行进，进入了一片更加茂密的松林。阳光在这里几乎被树冠完全遮住了，空气阴冷潮湿。马蹄踩在松针上，几乎发不出声音。"

    "雷恩突然举起拳头，做了一个停止的手势。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "停。"

    "他翻身下马，蹲在路边一棵大松树旁。你看到他用手指拨开地面的松针，露出了下面的泥土。"

    captain "……看这个。"

    "泥土上有清晰的脚印——不是村民的布鞋，是军靴。而且不止一双。"

    captain "至少三个人。脚印不超过两天。方向……从东往西。"

    "他站起来，目光扫过树林深处。"

    captain "从东面来——那是克雷恩男爵的地界。"

    captain "克雷恩是格雷伯爵的附庸——小封地，就夹在我们和格雷伯爵主领之间。这几年他和伯爵走得不近，倒是和王都那边有些小动作。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你觉得是谁？"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "斥候。专业的。你看脚步间距——他们在慢速行进，观察地形。不是路过的旅人，也不是迷路的猎人。"

    "他回到马旁，声音压低了。"

    captain "有人在侦察我们的领地。"

    menu:
        "派使者去克雷恩家明面交涉——亮家名压人" if reputation >= 30:
            $ log_decision("第一章深化", "派使者明面交涉克雷恩")
            $ change_stat("reputation", 5)
            $ change_stat("intrigue", 3)
            $ ch1_deep_scouts_choice = "envoy"

            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "派老兵杨去一趟克雷恩男爵家——穿家徽正装，明面上提一句。"

            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "明面交涉？这不就把咱们发现他们的事告诉对方了吗？"

            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "正是。让他们知道——艾登堡的新主，不需要靠暗箭。"

            player "让杨当着对方家臣的面问一句: '听说贵府最近往艾登堡边境派了几个 \"打猎的\"? 艾登可不是无主之地。'"

            $ hide_all_chars()
            "三天后，老兵回来了。男爵家给的回信: '想必是误会，已严令家臣不再越界。'"

            "你不知道这是真退还是装样。但至少这一回合，你没用一兵一卒，让对方先在台面上服了软。"

        "追踪他们「我要知道他们来这里干什么」":
            $ log_decision("第一章深化", "追踪斥候")
            $ change_stat("power", 5)
            $ ch1_deep_scouts_choice = "pursue"

            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "能追上吗？"

            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "两天前的踪迹……难。但不是不可能。"

            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "追。"

            "你们顺着脚印向东追了大约一刻钟。痕迹在一条小溪边消失了——他们涉水而行，抹去了踪迹。"

            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "老手。知道怎么甩尾巴。"

            "虽然没有追到人，但你在溪边发现了一小块布片挂在灌木上——深蓝色的染布，边缘有银线刺绣。"

            captain "克雷恩男爵家的侍卫制服。深蓝底银边。确认了。"

            "你把布片收入怀中。这是证据。"

        "先回去报告，加强巡逻「不要打草惊蛇」":
            $ log_decision("第一章深化", "返回加强巡逻")
            $ change_stat("intrigue", 8)
            $ ch1_deep_scouts_choice = "report"

            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "不追。我们只有两个人，追进别人的地盘太冒险。"

            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "那……"

            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "回去后加倍东面边境的巡逻。但不要声张。我不想让对方知道我们已经发现了。"

            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "……聪明。如果他们以为没被发现，就会变得大胆。大胆的人容易犯错。"

            "你点了点头。这是父亲教你的第一课——知道而不被知道你知道，这本身就是一种力量。"

        "在他们经过的路线上设陷阱「下次来就没那么好运了」":
            $ log_decision("第一章深化", "设置陷阱")
            $ change_stat("power", 8)
            $ ch1_deep_scouts_choice = "traps"

            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "他们走的是这条路线，对吧？"

            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "看起来是。"

            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "那就在这条路线上做些手脚。不是伤人的那种——我要捕捉。挖陷阱、设绊索、在几个关键位置埋铃铛。下次他们再来，我们就能活捉一个。"

            "雷恩看了你一眼，目光里有了一种新的东西。"

            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "……您父亲从来不会想到这种办法。"

            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我不是父亲。"

            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "不。您不是。"

            "他的语气里没有贬义。如果你听得仔细，甚至能捕捉到一丝……欣慰。"

    ## ── 遭遇三：旅行商人 ──

    scene bg forest_path with dissolve

    "巡逻的最后一段路上，你们在一个三岔路口遇到了一辆颜色鲜艳的马车。"

    "一个圆脸红鼻子的胖商人坐在车辕上啃面包。他的马车上堆满了各种货物——布匹、香料、小铁器，还有几坛酒。"

    "看到你们的巡逻甲，他赶紧跳下车，笑容满面地迎了上来。"

    "「哎呀呀，是新领主的巡逻队吗？我是旅行商人赫尔曼，常年在这一带走动。幸会幸会！」"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "赫尔曼。我认识你。去年你卖给驻军一批箭头，有三成是次品。"

    $ hide_all_chars()
    "赫尔曼的笑容僵了一瞬，但立刻恢复了。"

    "「雷恩队长说笑了！那不过是一点小小的误会……」"

    "你没有揭穿他，而是问起了沿途的见闻。商人的嘴比他的货物还丰富。"

    "「哎，说起来，最近这一带可不太平。西边的莫格伯爵在扩军——招了两百多号人，说是剿匪，可谁信呢？」"

    "「北边的松林村那个铁匠——他家闺女跟一个外地来的骑士跑了，现在铁匠逢人就说要打断那骑士的腿。」"

    "「啊，对了。你们的邻居克雷恩男爵——听说他最近跟王都的什么人走得很近。具体是谁，我就不清楚了。不过他在大量收购粮食，这一点是确定的。」"

    "你记住了每一个字。商人的闲话里，有时藏着比密探报告更有价值的东西。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "走吧，大人。天色不早了。"

    "你们和商人告别，策马返回城堡。"

    hide captain_img with dissolve

    scene bg castle_exterior with dissolve

    "回到城堡时，你的大腿和屁股都在抗议——你已经很久没有骑这么长时间的马了。"

    "但你的脑子很清醒。"

    "你现在知道了——你的领地不大，但地形复杂。有可以利用的险要地势，也有难以防守的薄弱环节。你的邻居们在暗中窥探，而你的百姓们在等待你的决定。"

    "这不仅仅是一次巡逻。这是你的第一堂实地课。"

    $ ch1_deep_patrol_done = True

    return

## ============================================================
## 场景三：领主法庭 (~250行)
## ============================================================

label ch1_deep_court:

    $ play_music("audio/music/great_hall.ogg", fadein=2.0)
    $ set_mood("formal")

    scene bg great_hall with dissolve

    "艾登堡的大厅被重新布置了。"

    "你的座椅——一把高背橡木椅，算不上王座，但足够有威严——被放在了大厅的北端，背后挂着家族的金鹰旗帜。两侧各站了两名卫兵，手持长矛，目视前方。"

    "大厅里已经挤满了人。农民、匠人、商人、小地主……他们三三两两地交头接耳，空气中弥漫着汗味、泥土味和隐约的焦虑。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "大人，一切准备就绪。今天有三个案子需要您裁决。"

    "奥尔德里克站在你的右手边，手里捧着一摞文书。他的声音很低，只有你能听到。"

    aldric "第一个是财产纠纷，第二个涉及偷窃，第三个是税务争议。我建议您……不要急于表态。先听完所有人的话。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "明白了。"

    $ hide_all_chars()
    "你坐到椅子上。木头在你的重量下微微嘎吱了一声。"

    "你环顾大厅。所有的目光都聚焦在你身上。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "艾登堡领主法庭——现在开庭。"

    ## ── 案件一：羊群纠纷 ──

    "两个中年男人被领到了你面前。一个粗壮矮胖，穿着打了补丁的羊皮背心；另一个瘦高干瘪，嘴唇紧抿成一条线。"

    aldric "原告——柏恩农场的约瑟。被告——磨坊坡的塞巴斯。争议标的——十二只绵羊。"

    $ hide_all_chars()
    "粗壮的那个先开口了，声音像破锣。"

    "「大人！我的羊被他偷了！十二只！前天早上一数，少了十二只，然后我就在他的羊圈里看到了它们！」"

    "瘦高的那个立刻反驳。"

    "「放你的屁！那些羊是从我自己的母羊生出来的！你凭什么说是你的？你的羊又没刻名字！」"

    "大厅里响起了一阵低笑。你敲了敲扶手，笑声止住了。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "安静。——奥尔德里克，有人调查过了吗？"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "是的。我派人去看了两家的羊圈。约瑟的羊圈围栏有一处大洞，足够羊钻过去。而塞巴斯的羊圈就在约瑟羊圈的下坡方向，中间隔了不到二百步。"

    $ hide_all_chars()
    "也就是说——羊可能是自己跑过去的。"

    "两个人的脸色都不太好看。"

    menu:
        "叫村里其他养羊户作证——这种事不止你们两家" if loyalty >= 30:
            $ log_decision("第一章深化", "领主法庭: 召邻里作证")
            $ change_stat("loyalty", 5)
            $ change_stat("reputation", 3)
            $ ch1_deep_sheep_verdict = "neighbors"

            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "奥尔德里克，把附近三个村的村长都叫来。还有边上养羊的几户人家。"

            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "为这十二只羊?"

            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "为以后还有多少十二只羊的事。"

            $ hide_all_chars()
            "下午，八九个村人挤进了大厅。你让他们自己说——"

            "'我家围栏也有裂痕，上个月跑了三只猪。' '我家羊也跑过，邻居把羊还回来了。'"

            "你听了半个时辰，没说话。最后下令——"

            "'十二只各得六只，按邻里旧例办。围栏破洞由领主出工匠，各家不必自掏钱修。'"

            "村人们一时没反应过来。一个老头先开口: '领主大人……真出工匠?'"

            "你点头。老人当场抹起了眼睛。"

        "平分羊群「各六只。各自回去修好围栏。」":
            $ log_decision("第一章深化", "领主法庭: 平分羊群")
            $ change_stat("reputation", 3)
            $ ch1_deep_sheep_verdict = "split"

            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "听清楚了——羊从破洞里跑出去，跑到下坡的羊圈里，这是天性，不是偷盗。"

            player "十二只羊，各得六只。约瑟，你回去修好围栏；塞巴斯，既然你白养了几天别人的羊，就算补偿了。"

            "两个人都不太满意，但也都没有反对。他们互相瞪了一眼，各自退下了。"

            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "……中规中矩的判决。"

        "把羊全部判给围栏完好的一方「谁的管理更好，羊就归谁」":
            $ log_decision("第一章深化", "领主法庭: 判给围栏好的一方")
            $ change_stat("power", 3)
            $ change_stat("reputation", 3)
            $ ch1_deep_sheep_verdict = "fences"

            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "围栏坏了不修，羊跑了怪别人——约瑟，你觉得合理吗？"

            "粗壮的男人张了张嘴，说不出话来。"

            player "十二只羊判给塞巴斯。约瑟，回去把围栏修好。如果你能证明那些羊身上有你的标记，可以来重新申诉。"

            $ hide_all_chars()
            "约瑟的脸涨得通红，但在卫兵的目光下，他低着头退下了。"

            "大厅里响起了一阵窃窃私语。有人觉得这判决太严了，但也有人在点头——至少这个领主做事有章法。"

        "罚两人各交五只羊充公「浪费领主的时间，代价不便宜」":
            $ log_decision("第一章深化", "领主法庭: 两人各罚五只羊")
            $ change_stat("power", 8)
            $ change_stat("wealth", 3)
            $ ch1_deep_sheep_verdict = "fine"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你们两个为了十二只羊闹到领主法庭来，浪费了所有人的时间。"

            "你的声音不高，但整个大厅都安静了。"

            player "各罚五只羊充入领地公库。剩下的两只，你们自己去分。"

            "两个人同时张大了嘴，脸色惨白。"

            player "下次再有这种鸡毛蒜皮的事，先去找村长调解。村长解决不了的，再来找我。听明白了吗？"

            $ hide_all_chars()
            "两个人忙不迭地点头，几乎是逃一样退出了大厅。"

            "你能感觉到大厅里的气氛变了——人们看你的眼神里，多了一些……敬畏。"

    ## ── 案件二：偷面包的少年 ──

    "接下来被领上来的是一个消瘦的少年——大概十五六岁，衣衫褴褛，手腕上还带着绳子。他低着头，肩膀微微发抖。"

    "在他身后跟着一个面容憔悴的妇人，眼眶红肿，显然哭了很久。"

    "另一边是一个红脸大胡子的男人——面包师傅。他双手环抱在胸前，一脸怒气。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "原告——面包师弗里茨。被告——寡妇玛格丽特之子汉斯。罪名——盗窃。"

    $ hide_all_chars()
    "面包师先说话了。"

    "「大人，这小崽子偷了我三个黑麦面包！我亲眼看到的！他从后门钻进来，抓起面包就跑。我追了两条街才把他按住。」"

    "寡妇扑通一声跪在了你面前，泪流满面。"

    "「大人开恩！我家男人去年死于疫病，留下我和三个孩子。我给人洗衣裳为生，但入冬后活计越来越少……孩子们已经三天没吃东西了。汉斯是怕弟弟妹妹饿死，才……才……」"

    "她说不下去了，只是不停地磕头。"

    "你看向那个少年。他始终没有抬头。但你注意到他的嘴唇干裂到发白，锁骨从破烂的领口里突出来，像是要刺破皮肤。"

    "面包师的语气稍微软了一点，但依然坚持。"

    "「我同情他们的遭遇。但偷就是偷。如果今天不惩罚，明天人人都来偷，我这面包铺还开不开了？」"

    menu:
        "自掏腰包付面包钱+给少年安排工作" if wealth >= 30:
            $ log_decision("第一章深化", "领主法庭: 自掏腰包解决偷面包")
            $ change_stat("wealth", -3)
            $ change_stat("loyalty", 5)
            $ change_stat("reputation", 5)
            $ ch1_deep_widow_verdict = "buy"

            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "弗里茨——这三个铜币我替少年付了。"

            "你从腰间钱袋里取出三枚铜币，放在面包师面前的桌上。"

            player "另外，你的面包铺要不要再请一个学徒? 每天给他一顿饭+月底两枚银币。少年我替你考察过——能扛能跑能算数。"

            $ hide_all_chars()
            "面包师愣了一下。他看了少年一眼，又看了你一眼。"

            "「……领主大人都开口了，老朽哪能不答应。汉斯，明天来铺子里报到。」"

            "少年抬起头，眼睛里第一次有了光。他不知道说什么，只能反复鞠躬。"

            "这事在城里传开了。三天后，有两户穷人家的孩子主动来城堡问能不能给他们也找份活。"

            "你给奥尔德里克写了张条子: '能干粗活的安排到马厩和铁匠铺，能算数的来记事房。工钱从我私库出。'"

        "赦免少年「他偷的是面包，不是金子。饥饿不是罪。」":
            $ log_decision("第一章深化", "领主法庭: 赦免偷面包少年")
            $ change_stat("loyalty", 8)
            $ ch1_deep_widow_verdict = "pardon"

            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "弗里茨。你的面包值多少？"

            "「三……三个铜币，大人。」"

            player "三个铜币。"

            "你站起身来。"

            player "一个孩子为了让弟弟妹妹不饿死而偷了三个铜币的面包。如果我因此砍他的手或把他关进地牢，那不是正义，是暴行。"

            "大厅里安静得针落可闻。"

            player "汉斯——看着我。"

            "少年终于抬起头。他的眼睛又黑又大，里面有恐惧，也有一种超出年龄的倔强。"

            player "你偷了东西。这是事实。但你为了家人，不是为了自己。我今天放了你。但你要记住——下次有困难，来城堡找管家。不要走这条路。"

            $ hide_all_chars()
            "少年的嘴唇颤了颤。"

            "「……谢谢大人。」"

            "寡妇在地上哭得更厉害了——但这一次是释然的泪水。"

        "自掏腰包付面包钱，再给寡妇一些救济「偷盗不能姑息，但贫困也不能无视」":
            $ log_decision("第一章深化", "领主法庭: 替少年付钱并救济")
            $ change_stat("wealth", -3)
            $ change_stat("reputation", 8)
            $ ch1_deep_widow_verdict = "pay"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "弗里茨，你的面包钱——三个铜币——从我的私库里出。你没有损失。"

            "面包师的怒气立刻消了大半。"

            player "玛格丽特。"

            "寡妇颤巍巍地抬起头。"

            player "去找管家奥尔德里克登记。从今天起，你家每月可以从领地的救济粮仓领取基本口粮，直到你的孩子们长大到可以做工为止。"

            $ hide_all_chars()
            "寡妇愣住了。然后她磕了一个头，一个极重的头，额头撞在石板地上，发出闷闷的声响。"

            "「大人……大人的恩德……」"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "别磕了。带你儿子回去吧。"

            "大厅里有人在鼓掌。你制止了——法庭不是表演的地方。但你注意到，很多人的目光变了。"

        "让少年到城堡做工抵罪「既惩罚了偷盗，也给了他一条活路」":
            $ log_decision("第一章深化", "领主法庭: 少年到城堡做工")
            $ change_stat("loyalty", 3)
            $ change_stat("faith", 3)
            $ ch1_deep_widow_verdict = "work"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "汉斯。你偷了面包，这是事实。法律就是法律，不能因为理由好听就视而不见。"

            "少年又低下了头。寡妇的呼吸急促起来。"

            player "但——我给你一个选择。从今天起，你到城堡做工。厨房、马厩、杂务——什么都行。工钱按正常雇工算。面包的钱从你的第一个月工钱里扣。"

            "你看着他。"

            player "这不是惩罚。这是机会。你愿意吗？"

            $ hide_all_chars()
            "少年缓缓抬起头。他看了看母亲，又看了看你。"

            "「……我愿意。」"

            "他的声音很轻，但很坚定。"

            "你点了点头。日后你会发现，这个叫汉斯的少年，会成为你最忠心的仆人之一。但那是后来的事了。"

    ## ── 案件三：税务争议 ──

    "最后一个案子的气氛截然不同。"

    "走上来的是两个衣着体面的人——一个是穿着暗红色外套的商人，面容精明；另一个是领地的税务官——一个留着八字胡的中年男人，神情紧张。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "原告——丝绸商人维克多。被告——税务官格哈特。争议——维克多声称上一次缴税时被多收了三十枚银币。"

    $ hide_all_chars()
    "商人维克多拱手行礼，姿态从容。"

    "「大人，我做的是正经生意。上个月我运了一批丝绸到领地内售卖，按照税率应缴纳七十枚银币。但格哈特大人收了我一百枚。多出来的三十枚，我要求退还。」"

    "税务官格哈特擦了擦额头的汗。"

    "「大人，他说的不对。那批丝绸是从外邦进口的，按照外邦商品税率，应该加收三成。我收的完全合规。」"

    "维克多冷笑了一声。"

    "「外邦商品税？那条规矩是十五年前定的，早就没人执行了。您父亲在世时，从来没收过这个税。」"

    "格哈特的脸一下子红了。"

    "「那是因为……以前的情况不同……」"

    "你看了奥尔德里克一眼。老管家微微摇了摇头——他也不确定。"

    menu:
        "彻底审计税务记录「我要看账本。全部的。」":
            $ log_decision("第一章深化", "领主法庭: 审计税务账本")
            $ change_stat("reputation", 8)
            $ ch1_deep_tax_verdict = "audit"

            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "两位都先退下。"

            "两个人一愣。"

            player "格哈特——三天之内，把过去一年的所有税务记录送到我的书房。全部的。一笔都不能少。"

            "税务官的脸色白了一瞬。"

            player "维克多——你也一样。把你的货运单据、交易记录全部整理好，交给管家。"

            player "我不凭任何人的一面之词下判断。账本会告诉我真相。"

            $ hide_all_chars()
            "商人微微点头，似乎对这个结果很满意。而税务官……你注意到他的手在微微发抖。"

            "你决定之后仔细看看那些账本。如果税务官真的在中饱私囊，这绝不只是三十枚银币的问题。"

        "支持税务官「税规就是税规。商人应该缴纳」":
            $ log_decision("第一章深化", "领主法庭: 支持税务官")
            $ change_stat("power", 5)
            $ ch1_deep_tax_verdict = "trust_collector"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "外邦商品税是写在律法里的。不管以前有没有执行，规矩就是规矩。维克多，三十枚银币不退。"

            $ hide_all_chars()
            "商人的脸沉了下来，但他没有争辩。他只是深深地鞠了一躬。"

            "「大人说的是。」"

            "他的声音恭敬而冰冷。你知道他心里不服。但你也知道——如果你当着所有人的面否定自己的官员，以后谁还会替你办事？"

            "税务官格哈特长舒了一口气，擦了擦汗。"

            "但你在心里记下了一个备注：这个格哈特……值得多留意。"

        "支持商人「过时的税法不应该选择性执行」":
            $ log_decision("第一章深化", "领主法庭: 支持商人")
            $ change_stat("reputation", 8)
            $ ch1_deep_tax_verdict = "trust_merchant"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "一条十五年没执行过的税法，突然拿出来用在一个商人身上——格哈特，你觉得这合理吗？"

            "税务官的嘴唇动了动，但没发出声音。"

            player "退还维克多三十枚银币。如果要恢复外邦商品税，需要我正式颁布法令。在那之前，一切按旧规矩来。"

            $ hide_all_chars()
            "维克多的脸上浮现出了笑意。他深深鞠躬。"

            "「大人英明。」"

            "格哈特低着头退下了。你看到他的拳头握得很紧。"

            "得罪一个官员，换来一个商人的好感。值不值得？只有时间会告诉你。"

    hide aldric_img with dissolve

    "三个案子审完。你的后背已经被汗水浸湿了——这比你想象的更累。不是身体上的累，而是每一个决定都像是在走钢丝。"

    "人群散去后，大厅恢复了空旷和安静。你靠在椅背上，闭上了眼睛。"

    "这就是权力的重量。不是刀剑的重量，不是金币的重量——而是无数人的命运压在你的每一句话上的重量。"

    $ ch1_deep_court_held = True

    hide player_char_img with dissolve
    return

## ============================================================
## 场景四：市场的秘密 (~200行)
## ============================================================

label ch1_deep_market:

    $ play_music("audio/music/market_bustle.ogg", fadein=2.0)
    $ set_mood("intrigue")

    scene bg marketplace with dissolve

    "艾琳娜给你找了一件灰色的旧斗篷和一顶羊毛帽子。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve

    elena "把帽子压低一点。你的脸还不至于家喻户晓，但不怕一万，只怕万一。"

    $ hide_all_chars()
    "你拉了拉帽檐，跟着她走进了艾登堡的集市。"

    "你以前只从城堡的窗户上远远看过这个集市。走进来才发现，它比你想象的要大得多——也混乱得多。"

    "窄窄的土路两边挤满了摊位。卖布的、卖铁锅的、卖草药的、卖腌鱼的。还有一个老妇人蹲在角落里卖自己编的柳条篮子。空气里交织着鱼腥味、香料味、烟熏味和人群汗酸味——一种属于生活本身的味道。"

    "叫卖声、讨价还价声、孩子的笑声、鸡的咯咯声——所有的声音混在一起，嗡嗡地震动着你的耳膜。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "看那边——那个卖布的。"

    "她用下巴指了指一个中年男人的摊位。他在兜售看上去品质不错的染布。"

    elena "注意他的指甲。"

    "你仔细看了看——那人的指甲下面全是发黑的颜色。"

    elena "指甲发黑，说明他自己染布，不是从染坊进货。自己染的利润比进货高三成。但他的定价和其他布商一样。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "所以他在赚暗利。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "不止。他的布摊旁边——看到那个买他布的妇人了吗？她是镇上裁缝铺老板的妻子。她不需要在这里买布，裁缝铺有自己的进货渠道。"

    "你皱了皱眉。"

    elena "她不是来买布的。她是来递消息的。你注意看——她翻了三匹布，但只在第二匹上摸了很久。然后她离开了，什么都没买。"

    "你回想了一下——确实如此。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "她在那匹布里摸到了什么？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "纸条。塞在布匹的夹层里。这是一种古老的传信方式——利用市场的人流掩护信息交换。"

    "你目不转睛地看着那个布商。他的表情没有任何变化，继续笑呵呵地吆喝着。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你早就知道了？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "我来艾登堡的第二天就注意到了。但我还没查清楚他们在传什么。"

    "艾琳娜带着你在市场里转了大约一个时辰。她像一个老师一样，不断指点着各种细节。"

    elena "闻到了吗？那个香料摊后面的味道——不是香料。是铁锈和油脂。有人在磨刀。"

    elena "那个乞丐——看他的手。长满了老茧，但不是握锄头的茧，是握剑的。他不是乞丐。"

    elena "那个卖苹果的姑娘，她的围裙口袋里鼓鼓的。不是钱，钱没那么重。是刀。"

    $ hide_all_chars()
    "你越听越心惊。这个看似平凡的集市底下，藏着一整个你从未想象过的暗流。"

    ## ── 发现黑市 ──

    "穿过集市的最深处，有一排看上去已经废弃了的仓库。木板墙上长满了苔藓，门口杂草齐膝。"

    "但艾琳娜径直走向了其中一间仓库的侧门。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "跟我来。不要说话。"

    $ hide_all_chars()
    "她推开了一扇半掩的门。你跟着走了进去。"

    "里面——出乎意料地——灯火通明。"

    "十几个人在一个昏暗但宽敞的空间里交易着什么。你的眼睛适应了光线后，看清了——"

    "短剑。匕首。弩。箭头。护甲。甚至还有几把长弓。"

    "有人在武装平民。"

    "而且这些不是猎人用的工具——这是战斗用的武器。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "看到了吧。有人在你的领地里经营着一个武器黑市。"

    "你压低了声音。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "谁？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "还不确定。但买家大多是周边村子的年轻人。他们在购买自卫用的武器——或者，有人在教他们觉得自己需要自卫。"

    "你环顾四周。没有人注意到你们——在这个地方，所有人都刻意不看别人的脸。"

    elena "卖家那边更有意思。你看——最里面那个负责验货的男人。他的靴子是军靴。标准的，不是猎人用的。有人在用军队渠道走私武器到民间。"

    "你搓了搓手掌。"

    menu:
        "回去派兵取缔「黑市必须关闭。平民不需要武器。」":
            $ log_decision("第一章深化", "取缔黑市")
            $ change_stat("power", 8)
            $ ch1_deep_blackmarket_choice = "shutdown"

            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "回去后我立刻派雷恩带人来查封这里。"

            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "可以。但你会打草惊蛇。这些人会转入更隐蔽的地方继续交易。你砍掉了蛇头，蛇身还在。"

            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "那也比放任自流好。我的领地上不能有不受控的武装力量。"

            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "……明白了。"

            $ hide_all_chars()
            "她的语气平淡，但你能感觉到她有些遗憾——也许她觉得这是一个更大棋局的线索，而你选择了最直接但未必最聪明的方式。"

            "但有些时候，直接就是最好的。"

        "让艾琳娜继续暗中调查「找出幕后的人更重要」":
            $ log_decision("第一章深化", "让艾琳娜渗透黑市")
            $ change_stat("intrigue", 8)
            $ change_rel("rel_elena", 5)
            $ ch1_deep_blackmarket_choice = "infiltrate"

            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "先不要惊动他们。你能不能渗透进去？"

            "艾琳娜的眼睛亮了一下。"

            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "我可以。给我两周时间。"

            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我需要知道：谁在提供武器？谁在买？为什么？"

            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "明白。我会以流动商人的身份接近卖方。这种人最喜欢新客户——新客户意味着新利润。"

            "你点了点头。"

            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "小心。"

            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "大人多虑了。这种地方，比王都的暗巷安全多了。"

            "她挑了下眉毛。这是你第一次在她脸上看到这种表情——不是恭敬，不是距离感，而是一个专业人士即将施展才华时的兴奋。"

        "买下一批武器充实自己的军备「既然有人在卖，不如我来买」":
            $ log_decision("第一章深化", "购买黑市武器")
            $ change_stat("power", 5)
            $ change_stat("wealth", -3)
            $ ch1_deep_blackmarket_choice = "buy"

            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "那些武器的质量怎么样？"

            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "中上。不是精品，但够用。价格比正规渠道便宜三四成。"

            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "想办法买一批。用假名。"

            "艾琳娜看了你一眼。"

            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "大人的意思是……"

            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我的武器库几乎是空的。正规渠道进货太慢太贵。既然有人在卖，没理由不利用。"

            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "黑市武器无法追踪来源。如果被发现，会有麻烦。"

            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "那就不要被发现。"

            "她轻轻点了点头。"

            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "明白了。我会安排。"

    hide elena_img with dissolve

    scene bg castle_exterior with dissolve

    "你们从市场回来时，已经是下午了。阳光从西边斜照过来，把城堡的影子拉得老长。"

    "你抖掉了灰色斗篷上的灰尘，把它折好交给了侍女。"

    "市场。黑市。密信。武装平民。"

    "你的领地底下藏着一整个你看不见的世界。而你刚刚只是掀开了这个世界的一角。"

    $ ch1_deep_market_visited = True

    return

## ============================================================
## 场景五：艾琳娜的第一课 (~220行)
## ============================================================

label ch1_deep_elena_lesson:

    $ play_music("audio/music/night_mystery.ogg", fadein=2.0)
    $ set_mood("intrigue")

    scene bg study with dissolve

    "夜深了。城堡里大多数人已经入睡。"

    "你按照艾琳娜的约定来到了书房。她已经在里面等你了——桌上摆了三样东西：一面小铜镜、一封蜡封的信、还有三个小玻璃瓶。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve

    elena "大人来了。请坐。"

    "她的语气和白天不同。没有了恭敬和距离，取而代之的是一种冷静的、专注的认真。"

    elena "今晚我要教您三件事。在王都，这三件事可能救您的命。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "听起来很严重。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "因为确实很严重。在艾登堡，一个错误的判断可能让您损失几只羊。在王都，一个错误的判断可能让您失去脑袋。"

    "她拿起了桌上的铜镜。"

    ## ── 第一课：读懂身体语言 ──

    elena "第一课——读人。人的嘴可以说谎，但身体不会。"

    elena "我现在要对您说三句话。其中有一句是谎话。您来判断是哪一句。"

    "她清了清嗓子，看着你的眼睛。"

    elena "第一句：我在来艾登堡之前，在王都的情报网工作了六年。"

    "她的目光平静如水，呼吸均匀，双手自然地放在膝盖上。"

    elena "第二句：我的父亲是一个铁匠，我在铁匠铺里长大。"

    "她说这句话时微微偏了一下头，嘴角有一个极轻微的——几乎看不到的——抽动。"

    elena "第三句：我来艾登堡，是因为有人委托我保护新任领主。"

    "她说完，双手交叠在膝盖上，等待你的回答。"

    menu:
        "第一句是谎话——六年太长了，你看起来不像干了那么久的人":
            $ log_decision("第一章深化", "读心术测试: 猜第一句")

            elena "错。六年是真的。甚至比六年更久——但多出来的那部分不方便说。"

            elena "您注意到了年龄和经验的不匹配，这说明您在思考。但您忽略了更重要的线索——身体语言。我说第一句话时，身体是放松的。放松意味着真实。"

        "第二句是谎话——你说那句话的时候嘴角抽了一下":
            $ log_decision("第一章深化", "读心术测试: 猜第二句")
            $ change_stat("reputation", 5)
            $ change_rel("rel_elena", 3)

            "艾琳娜的眼睛微微睁大了。"

            elena "……正确。"

            elena "我的父亲不是铁匠。至于他是什么……以后再说。重要的是，您注意到了那个微表情——说谎时的嘴角抽动。很多人能感觉到'有什么不对'，但很少有人能精确指出是哪里不对。"

            elena "您有天赋。"

        "第三句是谎话——保护我只是借口，你有自己的目的":
            $ log_decision("第一章深化", "读心术测试: 猜第三句")

            elena "有趣的推理。但……错了。我确实是来保护您的。虽然——"

            "她停顿了一下。"

            elena "——'保护'的定义可能比您想象的宽泛。"

            elena "正确答案是第二句。我说那句话时嘴角有一个微动——这是压制真实情绪的表现。下次请注意对方的嘴唇和眼角。那里最难伪装。"

    ## ── 第二课：密码解读 ──

    elena "第二课——密码。"

    "她拿起了那封蜡封的信，递给你。"

    elena "拆开看看。"

    $ hide_all_chars()
    "你揭开蜡封，展开信纸。上面写着一行看似毫无意义的文字："

    "'山中无虎，猴王称霸。东风不起，残叶满阶。'"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "这是……诗？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "这是一种叫做'藏头隐尾'的密码。规则很简单——取每句话的第一个字和最后一个字，交替排列。"

    "你在心里算了算。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "山……霸……东……阶？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "对。'山霸东阶'。这是一个地名的暗语——'东山台阶'——意思是接头地点在东山的石阶处。"

    "她又掏出了一张纸，上面写着更长的密文。"

    elena "但真正复杂的密码不会这么直白。看这个。"

    "你看到了一堆数字：7-3-2，15-1-4，22-8-1，9-6-3。"

    elena "这叫做'书页密码'。第一个数字是页码，第二个是行数，第三个是那行的第几个字。你需要一本特定的书——双方事先约定的那本——才能破解。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "如果不知道是哪本书呢？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "那你就需要试。好消息是，常用的书不多——圣经、地方志、税法手册。王都的间谍们最爱用的是一本叫《论诸国兴衰》的书——因为几乎每个贵族家里都有。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我父亲的书架上就有那本。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "我知道。"

    "你看了她一眼。她面无表情，但你总觉得她知道的比她说的多。"

    ## ── 第三课：识别毒药 ──

    elena "最后一课——毒药。"

    "她把那三个小玻璃瓶推到你面前。每个瓶子里装着不同颜色的液体——一个透明、一个淡黄、一个微微泛绿。"

    elena "不要打开它们。用鼻子靠近瓶口闻就行。告诉我你闻到了什么。"

    "你拿起第一个瓶子——透明的那个。靠近鼻子一闻——"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "什么都没闻到。就是水？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "这是颠茄提取液。无色、无味、几乎不可检测。三滴可以让一个成年人在八小时内心脏衰竭。致死后症状类似自然病亡。这是王都最常用的暗杀手段。"

    "你赶紧把瓶子放下。"

    elena "别怕。瓶子是密封的。但记住——如果有人递给你一杯看上去完全正常的酒或水，但你的直觉告诉你有什么不对……相信你的直觉。"

    "你拿起第二个——淡黄色的。这一次你小心多了。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "有一点……杏仁味？很淡。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "好。这是氰化物的稀释液。杏仁味是它的标志。如果你在食物或饮料里闻到了不该出现的杏仁味——立刻放下。这种毒致死极快，几乎没有救治的时间。"

    "最后一个——泛紫色的。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "这个……苦涩。像是某种草药。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "这是暮色之露。加入食物后几乎无法察觉。每次微量，日积月累，受害者会慢慢衰弱，看起来像久病不愈。"

    "她停顿了一下。"

    elena "您父亲去世前的最后几个月，身体急速衰退。所有人都说是操劳过度。但——"

    $ hide_all_chars()
    "她没有说完。但那半句话的重量，像一块巨石，压在了房间里每一寸空气上。"

    "你盯着那个紫色的瓶子。手指微微发抖。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "……你是说——"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "我什么都没说。我只是在教您识别毒药。至于您父亲的真正死因，那是另一个问题——一个还没有答案的问题。"

    "她把三个瓶子收了起来，站起身来。"

    elena "今天的课就到这里。记住——在王都，这些技能可能救您的命。"

    "她走到门口，停了一步。"

    elena "还有——不要相信任何人递给你的酒。包括我的。"

    "她的嘴角勾起一个极淡的弧度，转身走了。影子从门缝底下抽走了。"

    hide elena_img with dissolve

    $ hide_all_chars()
    "你一个人坐在书房里。油灯的火焰在微微跳动。"

    "你看着桌上残留的那封密码信，脑海里反复回响着艾琳娜最后那句半截的话。"

    "父亲的死……真的是操劳过度吗？"

    "你不知道。但你现在知道了一件事——在这个世界上，很多看上去自然的死亡，都不是自然的。"

    $ ch1_deep_elena_first_lesson = True

    return

## ============================================================
## 场景六：老兵的故事 (~200行)
## ============================================================

label ch1_deep_old_guard:

    $ play_music("audio/music/sad_theme.ogg", fadein=3.0)
    $ set_mood("melancholy")

    scene bg castle_exterior with dissolve

    show aldric_img at left with dissolve

    aldric "大人……有一件事，我不知道该不该现在告诉您。"

    "奥尔德里克的语气比平时更轻，像是怕吵到什么人。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "说。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "老弗雷德里克……城堡西塔的老卫兵。他……怕是撑不过今晚了。"

    "你愣了一下。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "弗雷德里克？"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "您可能不太记得他。他来城堡的时候，您还没出生。他从您祖父那一代就开始守西塔了。四十三年。"

    "四十三年。比你的年龄还长。"

    aldric "他想……见您一面。说有些话，想在走之前对新主人说。"

    "你没有犹豫。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "带我去。"

    hide aldric_img with dissolve

    scene bg castle_exterior with dissolve

    "西塔的楼梯很窄，螺旋向上。石壁上渗着水珠，空气潮湿而阴冷。你的每一步都踩在被几代人磨得光滑的石阶上。"

    "最顶层是一间小小的房间。一张木板床，一张桌子，一个挂满了旧衣物的木架。窗户正对着西方——每天傍晚，这里可以看到最完整的日落。"

    "老弗雷德里克躺在床上。他瘦得像一把干柴，脸上的皮肤薄得几乎能看到下面的骨头。但他的眼睛——一双浑浊的蓝眼睛——仍然亮着。"

    "看到你进来，他挣扎着想要坐起来。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "别动。躺着说。"

    $ hide_all_chars()
    "你拉了一把椅子，坐到他的床边。"

    "老人的嘴唇动了动。声音像是从很远的地方传来的，像一阵风穿过枯枝。"

    "「大人……谢谢您来。老头子……还以为见不到您了。」"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你要见我，我就来。——你感觉怎么样？"

    $ hide_all_chars()
    "他咧嘴笑了。没有几颗牙齿了。"

    "「快死了。但不怕。怕死的人当不了四十三年的兵。」"

    "他喘了几口气，然后开始说话。声音断断续续，但每一个字都像是经过了仔细挑选。"

    ## ── 第一个故事：祖父 ──

    "「我十七岁那年来到这座城堡。那时候的主人是您的祖父——康拉德大人。」"

    "「他……是个可怕的人。我这么说不是不敬。是实话。」"

    "「他打仗从来不输。整个北境没有人敢惹艾登堡。他一声令下，三百骑兵可以在一个时辰内集结。」"

    "「但是——」"

    "老人的眼睛看向窗外，像是在看几十年前的什么东西。"

    "「他杀人不眨眼。有一次，一个逃兵被抓回来——他让人在城门口把那个逃兵吊了三天。活活的。三天。整个镇子的人都能听到惨叫声。」"

    "「从那以后，再也没有人敢逃跑。但也再也没有人真心为他卖命。他们是怕他，不是忠于他。」"

    "「康拉德大人死的时候，没有人哭。」"

    ## ── 第二个故事：父亲 ──

    "「然后是您的父亲——卡尔大人。」"

    "他的语气变得柔和了一些。"

    "「卡尔大人是我见过最好的人。他记得每一个卫兵的名字，每年冬天给我们发双倍口粮。城堡里谁家有了孩子，他会亲自送一个银币过去做礼物。」"

    "「他不喜欢打仗。能谈就谈，能让就让。有人说他软弱——也许是吧。但在他手下当兵，你会觉得自己不只是一个工具。」"

    "「而且——这话我没跟别人说过——老国王在世的时候，对卡尔大人格外看重。不是因为兵多地广，恰恰是因为他不起眼。」"

    "「有些东西，国王不会交给最强的人，只会交给最信得过的人。您父亲守着一个不属于他的东西——我不知道是什么。但那个东西……也许就是他被盯上的原因。」"

    "老人的声音低了下去。"

    "「可是……好人不一定能保护好别人。」"

    "「王后的人来了之后——那些税吏、那些'顾问'——卡尔大人一步一步地退让。今天让出一块田，明天少收一笔税，后天把一个忠心的手下调走……」"

    "「他以为退让可以换来和平。但那些人是狼。你退一步，狼就进一步。直到你退无可退。」"

    "「卡尔大人……是被温柔杀死的。不是刀，不是毒。是他自己的善良。」"

    "你的手不知什么时候握成了拳。"

    ## ── 第三个故事：你 ──

    "老人转过头，直直地看着你。那双浑浊的蓝眼睛里，突然闪过一丝清明——像是临终的烛火最后的一次跳动。"

    "「我看过您小时候的样子。在校场上追着您父亲的战马跑，摔了爬起来，再摔再爬。」"

    "「我也看过您离开时的样子。背着包袱，站在城门口回头看了三次，才咬着牙走的。」"

    "「现在我看到您回来了。」"

    "他伸出一只枯瘦如柴的手，颤巍巍地，像是想要碰触你，又不敢。"

    "你握住了他的手。那只手冰凉而干燥，骨节突出，像是握着一把枯枝。"

    "「您有您祖父的勇气，和您父亲的心。」"

    "他的声音此刻异常清晰，像是用尽了最后的力量在说这句话。"

    "「也许——您能找到他们都缺少的平衡。」"

    "他的手微微紧了一下，然后慢慢松开了。"

    "「……拜托了。」"

    "他闭上了眼睛。呼吸变得很浅、很轻。但他还在呼吸。"

    "你轻轻地把他的手放回被子上。"

    "你走出了西塔。楼梯很暗。你用手扶着冰冷的石壁，一步一步向下走。"

    "那天夜里，弗雷德里克在睡梦中走了。据说他走的时候脸上带着笑。"

    ## ── 送别 ──

    "第二天清晨，你站在大厅里，面对着几个等待你决定的卫兵。"

    "奥尔德里克在一旁安静地等着。"

    menu:
        "按军礼安葬「他是一个战士。让他以战士的方式离开。」":
            $ log_decision("第一章深化", "老兵军礼安葬")
            $ change_stat("power", 5)
            $ ch1_deep_guard_funeral = "military"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "全副甲胄入殓。金鹰旗覆棺。卫兵列队送行。"

            "你停了停。"

            player "号角——吹三声。一声送别，一声致敬，一声……替所有没能等到他离开的人。"

            $ hide_all_chars()
            "那天的葬礼，城堡的每一个人都来了。号角声在山谷间回荡，像是大地在为一个老兵唱最后的歌。"

            "卫兵们站得笔直。有几个年轻的在偷偷擦眼泪。"

        "让他与家人一起安葬「他值得安宁。不是荣耀，是安宁。」":
            $ log_decision("第一章深化", "老兵与家人合葬")
            $ change_stat("loyalty", 8)
            $ ch1_deep_guard_funeral = "peaceful"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "他有家人吗？"

            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "有。妻子三年前走了，葬在南坡的墓地。有一个女儿嫁到了隔壁镇子。"

            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "把他葬在妻子旁边。仪式从简——他守了四十三年的岗，够累了。让他安安静静地走。"

            $ hide_all_chars()
            "葬礼在一个有阳光的下午举行。只有几个相熟的老卫兵和他的女儿在场。"

            "你站在远处看着。没有号角，没有旗帜。只有风声，和一个女人低低的啜泣。"

            "有些告别，不需要观众。"

        "以他的名字命名西塔「他在那里守了四十三年。那座塔应该记住他。」":
            $ log_decision("第一章深化", "以老兵命名西塔")
            $ change_stat("reputation", 8)
            $ ch1_deep_guard_funeral = "tower"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "从今天起，城堡的西塔改名为'弗雷德里克塔'。在塔底刻一块铭牌——上面写：弗雷德里克，忠诚卫士，守望四十三年。"

            $ hide_all_chars()
            "大厅里安静了一瞬。然后几个老卫兵——弗雷德里克的同辈人——缓缓地、用力地点了头。"

            "一座塔以一个普通卫兵的名字命名。这在艾登堡的历史上从未发生过。"

            "但从今以后，每一个抬头看向西塔的人，都会记住——有一个叫弗雷德里克的老兵，在那里守了一辈子。"

    $ ch1_deep_old_guard_story = True

    hide player_char_img with dissolve
    return

## ============================================================
## 场景七：地窖的秘密 (~200行)
## ============================================================

label ch1_deep_cellar:

    $ play_music("audio/music/night_mystery.ogg", fadein=2.0)
    $ set_mood("mystery")

    scene bg castle_exterior with dissolve

    "你失眠了。"

    "在城堡里住了这些天，你渐渐摸清了这座老建筑的脾气——哪块地板会吱嘎作响，哪扇窗户关不严，哪条走廊在半夜会有穿堂风。"

    "但今晚，你发现了一件以前没注意过的事。"

    "酒窖。"

    "你原本只是想找一瓶酒帮助入睡。提着油灯走下酒窖的石阶时，你注意到最里面的墙壁有一处不太对劲——那里的石块颜色比其他地方稍微深一些，灰缝也更新。"

    "你伸手推了一下。"

    "石块纹丝不动。"

    "你又试了试旁边的几块。第三块——最右下角的那块——在你用力推的时候，发出了一声沉闷的'咔嚓'。"

    "一整面墙——大约两步宽——缓缓地向内旋转了。"

    "一股潮湿的、混着霉味和铁锈味的空气扑面而来。你举起油灯，看到了一条向下的狭窄石阶。"

    "你犹豫了片刻。然后你走了下去。"

    scene bg study with dissolve

    "石阶通向一个不大的地下室——大概只有书房的一半大小。天花板很低，你必须微微弯腰。"

    "油灯的光照亮了里面的东西——"

    "靠墙排列着几个木架。上面放着长条形的油布包裹——你打开一个，里面是一把长剑。虽然有些锈迹，但仍然能看出曾经是上等的工艺。"

    "总共有六把剑，两张弩，还有一叠箭头。这些都不是普通的武器——它们的做工远远超过了领地卫兵的标配。"

    "木架旁边是一张小桌子。上面铺着一张泛黄的大幅地图——是艾登堡及其周边地区的详细地形图。上面用红墨水标注了许多符号和线路——有些你能看懂（道路、桥梁），有些完全不明所以。"

    "桌子的抽屉里，你找到了一本薄薄的皮面笔记本。"

    "你打开第一页——是密密麻麻的文字。父亲的字迹。"

    "但不是正常的文字——是某种密码。字母被替换了，而且没有明显的规律。"

    "你翻了几页，大部分都是这种密码。但在最后几页，也许是父亲太急了，或者太累了——他用了正常的文字写了几段。"

    "第一段：'第十七次会面。在老磨坊。他带来了北方的消息——王后的新税法将在明年春天实施。如果那样的话，艾登堡将失去最后的自主权。'"

    "第二段：'必须做好准备。但不能让任何人知道。信任是一种奢侈品，在这个时代。'"

    "最后一段——字迹变得潦草，几乎难以辨认："

    "'如果我死了，确保我的孩子知道真相。但不要太早——真相是一把双刃剑。过早知道的人会被它砍伤，而不是武装。'"

    "你的手在发抖。不是冷。"

    "你把笔记本翻到底。夹在最后一页里的，是一张对折的小纸条。上面只有一句话，不是父亲的字迹——一种更加秀丽的、带着花体装饰的字迹："

    "'卡尔——无论发生什么，记住：第七棵橡树下。'"

    "你不知道这是谁写的，也不知道第七棵橡树在哪里。但你把纸条塞进了怀里。"

    "你继续搜索了地下室。在最里面的角落，被一堆旧木箱挡住的，是另一扇门——更小、更矮。你费力地移开木箱，拉开了门。"

    "一阵清凉的、带着草木气息的风吹了进来。"

    "是一条隧道。石壁粗糙，显然是很久以前挖掘的。你沿着隧道走了大约一百步——隧道渐渐向上倾斜，最后终止于一扇木板门。"

    "你推开门——外面是森林。夜风灌了进来，带着松脂和腐叶的气味。你等眼睛适应了黑暗后辨认了一下方向——这个出口在城堡北面的松林边缘。"

    "一条秘密的逃生通道。"

    "你关上门，原路返回了地下室。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve

    "第二天，你叫来了艾琳娜。"

    elena "……这里的东西，除了您，还有谁知道？"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你是第一个。"

    "她拿起那本笔记本，快速翻了几页。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "这个密码我见过类似的体系。给我几天时间，我应该能破解大部分。"

    "她看向那张地图，眉头微微皱起。"

    elena "这些红色标记……不只是地形。有些是会面地点。有些是……撤退路线。您父亲在为某种最坏的情况做准备。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "什么样的最坏情况？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "……也许是他已经预见到的那种。"

    "壁炉里的木头塌了一块，火星溅到石板上。"

    elena "这条密道——大人打算怎么处理？"

    menu:
        "封死它「太危险了。如果别人也知道这条通道，就是一个致命的后门。」":
            $ log_decision("第一章深化", "封死密道")
            $ change_stat("power", 3)
            $ ch1_deep_cellar_choice = "seal"

            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "用石头和水泥把它封死。隧道两端都封。"

            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "明白了。虽然可惜——这条路如果需要紧急撤离的话，非常有用。"

            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我不打算撤离。这座城堡是我的，我不会从后门逃走。"

            "她没有反对。但你注意到她的目光在那扇小门上停留了很久。"

        "保密，但保留它作为紧急出口「有退路不是懦弱，是明智」":
            $ log_decision("第一章深化", "保留密道")
            $ change_stat("intrigue", 8)
            $ ch1_deep_cellar_choice = "secret"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "留着它。但只有你和我知道。如果有一天我们需要跑——这就是最后的退路。"

            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "……聪明的选择。我建议在隧道里存一些物资——干粮、水、一套换洗衣物和一小袋金币。如果真的要用到这条路，我们可能没有时间打包。"

            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "安排吧。"

            "你知道保留一条逃跑通道听起来不太英勇。但你不是你祖父——你不会为了面子把自己逼到绝路。"

        "告诉奥尔德里克和雷恩「我信任他们。他们有权知道。」":
            $ log_decision("第一章深化", "告诉核心成员密道")
            $ change_stat("loyalty", 8)
            $ ch1_deep_cellar_choice = "tell"
            $ aldric_knows_passage = True
            $ captain_knows_passage = True

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "叫奥尔德里克和雷恩来。他们是我最信任的人。这种事不应该瞒着他们。"

            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "大人——这条密道的价值在于没有人知道它的存在。知道的人越多，泄露的风险越大。"

            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我理解你的顾虑。但如果我连最亲近的人都不信任，那我跟一个人孤身在这座城堡里有什么区别？"

            "她看了你一会儿。"

            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "……您父亲大概也是这么想的。"

            "你不确定这是赞扬还是警告。也许两者都是。"

    hide elena_img with dissolve

    $ hide_all_chars()
    "那天夜里，你又把父亲的笔记本翻了一遍。那些密码文字在烛光下跳动着，像是无数等待被破解的秘密在对你眨眼。"

    "父亲留下的不只是一座城堡和一个头衔。"

    "他留下了一整个你尚未触及的黑暗世界的入口。"

    $ ch1_deep_cellar_found = True

    return

## ============================================================
## 场景八：城墙上的日落 (~130行)
## ============================================================

label ch1_deep_sunset:

    $ play_music("audio/music/castle_calm.ogg", fadein=3.0)
    $ set_mood("reflective")

    scene bg castle_exterior with dissolve

    "一天结束了。"

    "你独自爬上了城堡东面的城墙。这是城堡最高的一段——从这里可以看到整个领地：北面的松林、东面的农田、南面蜿蜒的河流、西面渐渐沉入地平线的太阳。"

    "风很大。你的斗篷在身后猎猎作响，像是一面被风灌满的旗帜。"

    "你把双手撑在城垛上，粗糙的石头硌着手掌。石头还残留着白天的余温，像是这座城堡在用最后一点热度温暖你。"

    "太阳正在落下。天边染成了一片浓烈的橘红色，像是有人把一整桶颜料倒在了天幕上。云层的边缘被镀上了金色。远处的山脊变成了深蓝色的剪影。"

    "空气里有傍晚特有的气味——炊烟、晚露、以及石头被太阳晒了一天后慢慢变凉的味道。"

    "你想起了这几天经历的一切。"

    if ch1_deep_father_grave:
        "父亲的坟前，那句还没说出口的话。那丛从石缝里倔强生长的紫花。"

    if ch1_deep_patrol_done:
        "巡逻路上的断桥和密林中的脚印。你的领地比你以为的更大，也更脆弱。"

    if ch1_deep_court_held:
        "法庭上那些注视着你的目光——期待的、恐惧的、审视的。每一个判决都像是在走钢丝。"

    if ch1_deep_market_visited:
        "市场底下暗流涌动的秘密。有人在武装你的人民，或者说——在武装他们反对你。"

    if ch1_deep_elena_first_lesson:
        "艾琳娜的课。那三个小瓶子。和她没有说完的那半句话。"

    if ch1_deep_old_guard_story:
        "弗雷德里克的最后一句话——'找到平衡'。祖父有勇气，父亲有善心。而你……"

    if ch1_deep_cellar_found:
        "父亲留下的地窖。那些密码。那封来自未知人的纸条。真相是一把双刃剑。"

    "这些天的重量一下子全部压了下来。你的肩膀不由自主地往下沉了沉。"

    ## ── 内心独白（根据属性变化） ──

    if power >= intrigue and power >= faith:
        "你站起来又坐了回去。力量。你需要的是力量。"
        "这个世界不会善待弱者。你的祖父明白这一点——虽然他走到了另一个极端。但至少在他的治下，没有人敢觊觎艾登堡。"
        "你不会成为暴君。但你会成为一座让所有人仰望的山。你会让每一个敌人在动手之前都要三思。"
        "权力不是目的。权力是保护自己和自己人的手段。"

    elif intrigue >= power and intrigue >= faith:
        "你眯起了眼睛，目光扫过远处模糊的地平线。在那之后——是你看不到的东西。"
        "这几天你学到了最重要的一课：你看到的永远只是表面。每一个微笑背后都可能藏着一把刀，每一句忠诚的誓言背后都可能有一个条件。"
        "你不需要比所有人都强。你需要比所有人都看得远。"
        "知识是最锋利的武器。而秘密是最坚固的盾。"

    elif faith >= power and faith >= intrigue:
        "你抬起头，看着天空中最后一抹金色的光。"
        "在这片混乱的土地上，在这个人人互相算计的时代里，你选择相信——相信有比权力和阴谋更高的东西。"
        "也许是神。也许是正义。也许只是人心深处那一点还没有被磨灭的善意。"
        "你不知道这种信念能撑多久。但此刻，它是你唯一不曾动摇的东西。"

    else:
        "你还没有找到自己的道路。力量、智慧、信仰——它们都在你面前铺开，像是交叉的岔路口。"
        "但也许不需要现在就选。也许道路本身会在你走的过程中渐渐显现。"
        "父亲也不是一开始就知道答案的。他用了一辈子去寻找，虽然最后没有找到。"
        "但你有他没有的东西——你有时间。"

    "太阳的最后一线光芒消失在了地平线下。天空从橘红渐变为紫灰，再到深蓝。第一颗星星亮了起来。"

    "城堡下方的村庄里，灯火次第亮起。像是地面上的星空。"

    "有脚步声从你身后传来。"

    if rel_elena >= rel_bishop:

        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve

        $ hide_all_chars()
        "艾琳娜走到你身旁。她没有说话，只是和你一起看着渐渐暗下去的天空。"

        "过了很久——或者很短，在这种时刻你分不清——她轻声说："

        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "漂亮的日落。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "嗯。"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "明天还会有。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "嗯。"

        "她不再说话了。你们就这样站着，两个人，两个影子，在城墙上被最后的暮光拉得很长很长。"

        hide elena_img with dissolve

    else:

        hide player_char_img
        $ hide_all_chars("aldric_img")
        show aldric_img at left with dissolve

        $ hide_all_chars()
        "奥尔德里克缓缓走到你身旁。他的步伐比白天更慢——老骨头怕冷，傍晚的风对他不太友好。"

        "他看了你一眼，没有问你在想什么。这是他的体贴。"

        $ hide_all_chars("aldric_img")
        show aldric_img at left with dissolve
        aldric "大人，厨房准备了热汤。"

        hide aldric_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "等一下。让我再看一会儿。"

        hide player_char_img
        $ hide_all_chars("aldric_img")
        show aldric_img at left with dissolve
        aldric "好。"

        $ hide_all_chars()
        "他就站在那里陪着你。你们一起看着天色一点一点暗下去，像是一扇慢慢关上的门。"

        "然后他说了一句很轻很轻的话——轻到你几乎以为是风声："

        $ hide_all_chars("aldric_img")
        show aldric_img at left with dissolve
        aldric "……您父亲也喜欢在这个位置看日落。"

        "你没有回答。"

        hide aldric_img with dissolve

    $ hide_all_chars()
    "夜色完全降临了。"

    "你最后看了一眼那片被星光覆盖的领地。那些村庄里亮着的灯火，每一盏都是一个家庭。他们在吃晚饭，在讲故事给孩子听，在盘算明天的活计。"

    "他们不知道他们的新领主正站在城墙上，在黑暗中对着星空发呆。"

    "他们只知道——城堡里有人在替他们操心。这就够了。"

    "你转身向楼梯走去。"

    "太阳落下去了。"

    "但你知道，它还会再升起来。"

    $ ch1_deep_sunset_watched = True

    return

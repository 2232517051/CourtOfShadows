## ============================================================
## 第一章扩展：新主登基 — 深度剧情
## chapter1_expansion.rpy
## 城堡初夜 / 晨间议事 / 校场比武 / 巡视村庄 / 晚宴风云
## ============================================================

## ── 扩展剧情标记 ──
default ch1_exp_study_secret = ""          # "read_all" / "read_partial" / "sealed"
default ch1_exp_elena_impression = ""      # "kind" / "formal" / "curious"
default ch1_exp_council_stance = ""        # "aggressive" / "cautious" / "balanced"
default ch1_exp_tax_decision = ""          # "raise" / "lower" / "restructure"
default ch1_exp_bandit_plan = ""           # "military" / "negotiate" / "ambush"
default ch1_exp_sparring_result = ""       # "victory" / "defeat" / "draw"
default ch1_exp_market_verdict = ""        # "merchant_side" / "farmer_side" / "compromise"
default ch1_exp_toast_style = ""           # "humble" / "bold" / "cunning"
default ch1_exp_secret_letter_found = False
default ch1_exp_hidden_room_found = False
default ch1_exp_captain_respect = False
default ch1_exp_villager_trust = False
default ch1_exp_noble_impressed = False
default ch1_exp_aldric_confession = False
default ch1_exp_elena_backstory = False
default ch1_exp_night_explored = False

## ============================================================
## 第一部分：城堡初夜 — First Night in the Castle (~300行)
## ============================================================

label ch1_exp_first_night:

    $ play_music("audio/music/night_mystery.ogg", fadein=2.0)

    scene bg castle_exterior_night with dissolve

    "夜色降临了艾登堡。"

    "白天的喧嚣渐渐平息，仆人们一个接一个地回到各自的房间。走廊里的火把在晚风中摇曳，将石墙上的阴影拉得忽长忽短。"

    "你站在卧室的窗前，俯瞰着城堡下方的村庄。零星的灯火像是撒在黑绒布上的碎金。远处的山脊线模糊地融入了夜空。"

    "一切都安静得不像话。安静到你能听见自己的心跳声。"

    "你睡不着。这座城堡的每一块石头都浸透了父亲的气息——走廊里残留的烟草味、书架上他翻过的书页、门把手上他手掌的磨痕。"

    "你决定起身，在城堡里走走。也许这能帮你理清思绪。也许不能。但总好过躺在床上盯天花板。"

    menu:
        "去父亲的书房「他留下了什么？」":
            $ log_decision("第一章扩展", "深夜前往父亲书房")
            jump ch1_exp_father_study

        "去厨房「也许能找到点吃的，顺便看看谁还没睡」":
            $ log_decision("第一章扩展", "深夜前往厨房")
            jump ch1_exp_kitchen_night

        "去城墙上走走「吹吹风，清醒一下」":
            $ log_decision("第一章扩展", "深夜独自上城墙")
            jump ch1_exp_ramparts_night

## ── 父亲的书房 ──

label ch1_exp_father_study:

    scene bg study with dissolve

    "你推开书房的门。铰链发出一声低沉的呻吟，像是城堡本身在叹息。"

    "窗外透进来的微光照出书桌上厚厚一层灰尘。自从父亲去世后，似乎没有人进来打扫过这里。"

    "空气中弥漫着陈旧的羊皮纸和墨水的气味，混着一丝淡淡的烟草味——那是父亲生前最爱的切尔瑞烟丝。"

    "你点燃了桌角的油灯。暖黄色的光芒将房间从黑暗中一点点剥离出来。"

    "书架上的书排列得整整齐齐——这是父亲为数不多的洁癖之一。历史、军事、法律、农学。他什么都读，什么都留了批注。"

    "你的目光落在书桌上。几份文件散落着，上面有父亲熟悉的字迹。你拿起最上面的一份——"

    "是一封未寄出的信。收信人的名字被墨水涂掉了，但信的内容清晰可读。"

    "'……我已经没有多少时间了。那些人正在步步紧逼。如果我的判断没有错，他们会在入冬前动手……'"

    "'……我唯一担心的是孩子。他还不够成熟，还不了解这座城堡下面埋着什么秘密。但也许这样更好。无知有时候是最好的盔甲……'"

    "'……如果你收到这封信，说明我已经不在了。请照顾好他。不是因为他是我的儿子——是因为这片土地需要一个好的领主……'"

    "你的手微微发颤。信纸上的字在烛光中模糊了——不是因为光线暗，是因为你的眼眶热了。"

    "你把信小心地折好，放入怀中。"

    "然后你开始翻找书桌的抽屉。"

    "第一个抽屉：税收记录。枯燥但规整。"

    "第二个抽屉：与周边领主的来往信件。语气客套，内容空洞。"

    "第三个抽屉——锁着的。"

    "你试了几把桌上散落的钥匙，第三把打开了。抽屉里只有一样东西——一本黑色皮面的笔记本。"

    "封面上没有任何文字。但翻开后，你看到了密密麻麻的笔记，以及——一张折叠起来的城堡地图。"

    "地图上标注了一个你从未见过的房间。位置在地下室的深处，标记是一个红色的圆点。旁边用父亲的笔迹写着一个词——"

    "'真相。'"

    menu:
        "立刻去找那个隐藏房间":
            $ change_stat("power", 8)
            $ change_courage(5)
            $ ch1_exp_hidden_room_found = True
            $ log_decision("第一章扩展", "深夜探索隐藏房间")

            "你拿起油灯，按照地图的指引走向地下室。"

            scene bg underground with dissolve

            "地下室的空气湿冷而沉重，像一只看不见的手压在你的胸口上。石阶在你的脚下发出空洞的回声。"

            "你沿着通道走了大约五十步，在一面看似普通的石墙前停了下来。根据地图，隐藏房间就在这面墙的后面。"

            "你用手摸索着石缝，指尖触到了一块微微凸起的石头。你按了下去——"

            "机关的声音在寂静中格外刺耳。石墙缓缓向一侧滑动，露出了一条狭窄的通道。"

            "通道的尽头是一间不大的密室。墙上挂着几幅画像——你不认识上面的人，但每幅画像下方都刻着一朵百合花。"

            "正中央的桌上放着一个铁箱。箱子没有锁，但封着火漆。火漆上的纹章不是金鹰——是一朵半开的百合。"

            "你犹豫了一下，但还是打开了箱子。"

            "里面有三样东西：一叠信件，一枚银质的徽章，以及一张泛黄的契约。"

            "信件是用暗语写的，你一时半会儿看不懂。银徽章上刻着百合花和一句拉丁文——'Lux in tenebris'，暗中之光。"

            "契约上的内容你能读懂——那是一份互助协定，签署者包括你的父亲和另外四个你不认识的名字。日期是十五年前。"

            "你的父亲在很久以前就加入了某个秘密组织。而这个组织——毫无疑问——与暗百合有关。"

            $ ch1_exp_secret_letter_found = True
            $ secret_passage_found = True
            $ dark_lily_exists_known = True
            $ change_stat("intrigue", 5)

            "你把所有东西放回原处，记住了密室的位置。这些秘密太沉重了，你需要时间来消化。"

            "你沿原路返回书房，手仍在微微发抖。"

        "仔细阅读笔记本「先了解全貌」":
            $ change_stat("reputation", 5)
            $ ch1_exp_study_secret = "read_all"
            $ log_decision("第一章扩展", "仔细研读父亲笔记本")

            "你坐在父亲的椅子上，就着烛光一页一页地翻读笔记本。"

            "笔记本的前半部分是父亲对领地事务的私人记录——税收、人口、军事力量的评估。写得非常详细，甚至精确到每一户农民的姓名和家庭状况。"

            "你从未想过父亲对领民了解如此之深。他不是那种深居简出的贵族——他去过每一个村庄，记住了每一张面孔。"

            "笔记本的后半部分风格突变。字迹变得潦草，语气变得急促。大量使用代号和暗语——'花匠'、'园丁'、'枯萎的玫瑰'。"

            "有一段话引起了你的注意——"

            "'……B已经开始怀疑我了。他的使者越来越频繁地出现在边境。如果他知道了协定的存在，一切都会崩塌。我必须更加小心……'"

            "'B'——冯·哈根男爵？"

            "你继续往下读。最后一页的日期是父亲去世前两周。"

            "'……我已经做了能做的一切。密室里的东西如果落入错误的手中会非常危险。但如果我的儿子能找到它们——也许还有希望。'"

            "'……愿金鹰庇佑艾登堡。'"

            "你合上笔记本，感到一阵沉重的压力。父亲留下了太多未解之谜。"

        "把笔记本锁回抽屉「现在不是时候」":
            $ change_stat("loyalty", 3)
            $ ch1_exp_study_secret = "sealed"
            $ log_decision("第一章扩展", "将笔记本锁回抽屉暂不查看")

            "你犹豫了片刻，最终还是把笔记本放回了抽屉，重新锁好。"

            "不是因为你不好奇。是因为你的直觉告诉你——在你还没有掌握足够的力量之前，知道太多反而危险。"

            "父亲在信中说过：无知有时候是最好的盔甲。"

            "你关上抽屉，熄灭了油灯。房间重新沉入黑暗，只有窗口泛着一层冷白。"

            "你在黑暗中站了一会儿，然后转身离开。"

            "有些秘密，可以等。"

    jump ch1_exp_elena_encounter

## ── 厨房偶遇 ──

label ch1_exp_kitchen_night:

    scene bg great_hall with dissolve

    "你沿着走廊摸黑走向厨房。城堡在夜里显得比白天大了三倍，每一个转角都像是一个未知的入口。"

    "厨房里竟然还亮着灯。一缕温暖的光线从门缝中透出来，伴随着轻微的碗碟碰撞声。"

    "你推开门——"

    show elena_img at left with dissolve

    "艾琳娜正站在灶台前，背对着你。她穿着一身朴素的亚麻裙，外面罩着围裙，正在往一个陶碗里倒热牛奶。"

    "听到门声，她猛地转过身。手中的牛奶壶差点脱手。"

    elena "领——领主大人！您怎么——这么晚——"

    "她的脸在烛光下红了一瞬，随即恢复了镇定。"

    elena "抱歉，我没想到您还没休息。我在……我在热牛奶。老夫人以前常说，睡不着的时候喝杯热牛奶会好些。"

    "你注意到她说的'老夫人'——那是指你的母亲。艾琳娜在你母亲去世前就已经在城堡里了？"

    hide elena_img
    show player_char_img at left with dissolve
    player "你认识我母亲？"

    "她的表情变得柔和了。"

    hide player_char_img
    show elena_img at left with dissolve
    elena "我很小的时候就被卖到了城堡。是夫人……是老夫人收留了我。她教我识字，教我做针线。她是个很温柔的人。"

    "她停了停，像是在斟酌措辞。"

    elena "您……想喝一杯吗？"

    menu:
        "坐下来和她聊聊「我想了解更多」":
            $ change_rel("rel_elena", 8)
            $ ch1_exp_elena_impression = "kind"
            $ ch1_exp_elena_backstory = True
            $ log_decision("第一章扩展", "与艾琳娜深夜长谈")

            "你在木桌旁坐了下来。"

            "艾琳娜有些局促地倒了两碗热牛奶，然后在你对面坐下。她坐得很端正，双手放在膝盖上，像是随时准备起身行礼。"

            hide elena_img
            show player_char_img at left with dissolve
            player "放松。这又不是早朝。"

            "她嘴角弯了一下——不算笑，不过嘴唇的线条松了下来。"

            "你们聊了很多。关于城堡，关于过去，关于父亲生前的日子。"

            hide player_char_img
            show elena_img at left with dissolve
            elena "老领主……他不是一个容易亲近的人。但他对领民很好。每年冬天，他都会亲自巡查每个村庄，确保没有人挨冻受饿。"

            elena "他说：'一个领主如果连自己的人民都保护不了，那他的领地不过是一座精美的坟墓。'"

            "你把这句话记在了心里。"

            elena "他最后几个月……变了。经常一个人关在书房里，有时候半夜还能看到书房亮着灯。他变得多疑，不让任何人单独进他的书房。"

            elena "我有一次给他送茶，推门进去的时候，他吓了一跳。我看到他正在烧什么东西——在壁炉里。纸。很多纸。"

            "你的心沉了一下。"

            hide elena_img
            show player_char_img at left with dissolve
            player "你看清了纸上的内容吗？"

            hide player_char_img
            show elena_img at left with dissolve
            elena "没有。但我看到了一个印记——百合花。倒置的百合花。"

            "厨房里安静了。只有灶膛中余烬偶尔发出的噼啪声。"

            "你把牛奶喝完。它很甜，带着一丝肉桂的香气。"

            hide elena_img
            show player_char_img at left with dissolve
            player "谢谢。以后如果你想起什么，随时来找我。"

            hide player_char_img
            show elena_img at left with dissolve
            elena "……是。"

            "她低下头，但你看到她的眼角有一丝光亮。也许是烛光的反射。也许不是。"

        "礼貌地谢绝「我只是路过」":
            $ change_rel("rel_elena", 3)
            $ ch1_exp_elena_impression = "formal"
            $ log_decision("第一章扩展", "礼貌谢绝艾琳娜的牛奶")

            hide elena_img
            show player_char_img at left with dissolve
            player "不用了，谢谢。我只是睡不着，出来走走。"

            "你的语气客气但有距离感。艾琳娜微微低头。"

            hide player_char_img
            show elena_img at left with dissolve
            elena "是。如果您需要什么，随时吩咐。"

            "你点了点头，转身离开了厨房。"

            "在走廊里，你隐约闻到了热牛奶的甜香。肉桂味的。"

            "你没有回头。"

    hide elena_img with dissolve

    jump ch1_exp_elena_encounter

## ── 城墙夜行 ──

label ch1_exp_ramparts_night:

    scene bg castle_exterior_night with dissolve

    "你登上了城堡的外墙。夜风扑面而来，带着旷野的气息——泥土、枯草和远处河流的腥甜。"

    "城墙上每隔二十步就有一个火把，但大部分已经在风中熄灭了。只剩下几点孤零零的火光在黑暗中挣扎。"

    "你沿着城墙慢慢走着。脚下的石砖被岁月磨得光滑，有些地方已经出现了裂缝。城堡确实老了——和它的上一任主人一样。"

    "你走到城墙的东北角，突然听到了一个声音——金属碰撞的声响。"

    "你放慢脚步，朝声音的方向望去。"

    show captain_img at right with dissolve

    "卫队长雷恩独自站在角楼的平台上，背对着你，对着一个木桩练剑。"

    "他的动作沉稳而有力，每一剑都带着呼啸的风声。星星稀稀拉拉挂了几颗，勉强照出剑身上冷冽的光。"

    "他似乎察觉到了你的存在，猛然转身——手中的剑直指你的方向。"

    "两人对视了一瞬。然后他收剑行礼。"

    captain "领主大人。深夜巡城？"

    hide captain_img
    show player_char_img at left with dissolve
    player "睡不着。你呢？"

    hide player_char_img
    show captain_img at left with dissolve
    captain "……也睡不着。"

    "他把剑插回鞘中，走到城垛旁，望着远处的黑暗。"

    captain "我跟随老领主十五年了。从我十六岁入伍的第一天起。他教我用剑，教我带兵，教我怎么做一个好的卫队长。"

    "他的声音很平静，但你听得出底下的暗流。"

    captain "他走的那天晚上，我也是在这里。就站在这个位置。"

    "他转过头看你。夜色中看不清表情，但你从他的眼神里读到了一种你没想到的东西——不是悲伤，是愧疚。"

    captain "我应该保护好他的。这是我唯一的职责。但我失败了。"

    menu:
        "「不是你的错。我也没能保护他。」":
            $ change_rel("rel_captain", 10)
            $ change_stat("loyalty", 3)
            $ log_decision("第一章扩展", "安慰雷恩")

            "你走到他身边，和他并肩站在城垛前。"

            hide captain_img
            show player_char_img at left with dissolve
            player "如果自责有用，我应该比你更自责。我甚至不在他身边。"

            "雷恩的喉结动了动。"

            hide player_char_img
            show captain_img at left with dissolve
            captain "……您跟老领主很像。他也从不怪别人。"

            "你没有说话。远处，一只夜鸟从树丛中惊飞，翅膀划破夜空的寂静。"

            captain "领主大人，我发誓——这条命，从今天起是您的。不管发生什么，我会用剑和血来守护您。"

            "他单膝跪下。你看到月光在他的铠甲上流淌，像是一层薄薄的银水。"

            "你伸出手，扶他起来。"

            hide captain_img
            show player_char_img at left with dissolve
            player "不需要跪。站在我身边就好。"

            $ ch1_exp_captain_respect = True

        "「告诉我他最后几天的情况」":
            $ change_stat("reputation", 5)
            $ change_rel("rel_captain", 5)
            $ log_decision("第一章扩展", "向雷恩询问父亲死前的情况")

            player "我想知道父亲最后几天发生了什么。一切细节。"

            "雷恩的表情变得严肃。"

            hide player_char_img
            show captain_img at left with dissolve
            captain "最后一周……老领主变得非常不安。他加强了城堡的守卫，但同时又打发走了几个老仆人。他说不信任他们。"

            captain "他拒绝了除我和奥尔德里克以外任何人送的食物和饮料。但他还是——"

            "他停住了。喉结上下滚动了一下。"

            captain "前一天晚上，他从书房出来，叫我过去。他跟我说了一句话：'如果我出了什么事，保护好我的儿子。别让他碰那些信。'"

            hide captain_img
            show player_char_img at left with dissolve
            player "什么信？"

            hide player_char_img
            show captain_img at left with dissolve
            captain "他没说。第二天早上，我去叫他起床的时候……"

            "雷恩没有说下去。但他的拳头在身侧攥得咯咯作响。"

            captain "医师说是心疾。但我不信。老领主的身体虽然不如从前，但远没有到猝死的程度。"

            captain "有人害了他。我确信。"

            $ change_stat("intrigue", 3)

    hide captain_img with dissolve

    jump ch1_exp_elena_encounter

## ── 深夜偶遇艾琳娜（汇合点） ──

label ch1_exp_elena_encounter:

    scene bg great_hall with dissolve

    "你在回卧室的路上经过了一条偏僻的走廊。走廊里的蜡烛已经灭了大半，火把的光只照到三步远。"

    "突然——你听到了脚步声。轻轻的，刻意压低的，像猫一样。"

    "你闪身躲进了一根柱子后面。"

    "一个身影从走廊的另一端走来。她手里提着一盏小灯笼，光线被手掌半遮着。"

    "——是艾琳娜。"

    "她走到走廊中段，突然停了下来。她弯下腰，在一块地板石下面摸索着什么。然后她取出一样东西——看起来像是一封信。"

    "她把信藏入袖中，转身准备离开。"

    "你有两个选择——"

    menu:
        "现身质问「你在做什么？」":
            $ change_stat("power", 3)
            $ change_rel("rel_elena", -5)
            $ log_decision("第一章扩展", "当面质问艾琳娜深夜行为")

            "你从柱子后面走出来。"

            show elena_img at left with dissolve

            hide elena_img
            show player_char_img at left with dissolve
            player "艾琳娜。"

            "她吓得差点摔倒。灯笼在她手中剧烈晃动，影子在墙壁上疯狂摇摆。"

            hide player_char_img
            show elena_img at left with dissolve
            elena "领——领主大人！我、我只是——"

            hide elena_img
            show player_char_img at left with dissolve
            player "你在地板下面藏了什么？"

            "她的脸色白了。嘴唇动了动，却说不出话来。"

            "你向她伸出手。"

            player "给我看看。"

            "她犹豫了很久。然后，颤抖着从袖中取出了那封信。"

            "你接过来一看——信封上没有收件人，但火漆上有一个模糊的百合花印记。"

            hide player_char_img
            show elena_img at left with dissolve
            elena "这……这是老领主交给我保管的。他说如果他出了什么事，让我把这封信交给新领主。也就是……您。"

            elena "但他又嘱咐我，要等到您在艾登堡住满一个月之后再交出来。他说……您需要时间先站稳脚跟。"

            "你看着手中的信，又看了看艾琳娜。她的眼中有恐惧，但没有欺骗。"

            hide elena_img
            show player_char_img at left with dissolve
            player "……我先收下了。"

            $ ch1_exp_secret_letter_found = True
            $ change_stat("intrigue", 5)

            hide elena_img with dissolve

        "假装没看见「让她保守这个秘密」":
            $ change_stat("intrigue", 5)
            $ change_rel("rel_elena", 3)
            $ log_decision("第一章扩展", "假装没看见艾琳娜的秘密行动")

            "你屏住呼吸，一动不动地贴在柱子后面。"

            "艾琳娜把信藏好后，快步离开了走廊。脚步声渐远，到拐角处就听不见了。"

            "你从柱子后面走出来，看着她消失的方向。"

            "她在替父亲保守某个秘密。什么秘密？那封信里写了什么？"

            "你可以现在就追上去逼问她。但你选择不这么做。"

            "信任是需要时间的。如果艾琳娜是忠诚的——而你的直觉告诉你她是——那么那封信迟早会到你手中。"

            "如果她不忠诚……那你就更应该静观其变，看看她会把信交给谁。"

            $ change_stat("intrigue", 3)

    $ ch1_exp_night_explored = True

    scene black with dissolve

    "你回到卧室，躺在床上。窗外的月亮已经偏西了。"

    "这是你在艾登堡的第一个夜晚。你发现了太多东西——父亲的秘密、隐藏的房间、管家的往事、女仆的信件。"

    "每一个答案都带来了更多的问题。"

    "你闭上眼睛。在黑暗中，你仿佛看到了父亲坐在书桌前的背影——挺拔的，孤独的，像一座即将崩塌的高塔。"

    "你在心中默默说了一句话——"

    "'我会找到真相的。'"

    "然后你沉入了梦乡。"

    jump ch1_exp_morning_council

## ============================================================
## 第二部分：晨间议事 — Morning Council (~300行)
## ============================================================

label ch1_exp_morning_council:

    $ play_music("audio/music/castle_calm.ogg", fadein=2.0)

    scene bg council_hall with dissolve

    "清晨的阳光透过议事厅高处的彩色玻璃窗洒下来，在长桌上铺开斑斓的光影。空气中飘浮着新点燃的蜂蜡烛的甜香。"

    "你昨夜几乎没怎么睡。但镜子前，你还是尽力让自己看起来精神抖擞。一个领主不能让人看出他的疲惫——这是你从修道院学到的第一课。"

    "议事厅的长桌两侧坐着四个人——这是你作为新领主的第一次正式议事。"

    show aldric_img at left with dissolve

    aldric "少主，所有人都到齐了。请入座。"

    "你走到长桌的首位坐下。椅背上雕着金鹰——你的家族徽章。椅子比你想象的硬得多。"

    "你环顾四周：左手边是奥尔德里克，右手边是雷恩。对面坐着两个你不太熟悉的人——一个是管理税收的书记官，满脸皱纹，眼神疲惫；另一个是领地的粮官，身材圆胖，表情紧张。"

    aldric "议事内容有三项。第一：匪患。第二：税收。第三：邻近领主的动向。"

    "你点了点头，示意他继续。"

    ## ── 议题一：匪患 ──

    aldric "首先是匪患。北部山区的黑狼帮在近三个月内抢劫了七支商队。两名商人被杀，货物损失约合三百金币。"

    hide aldric_img
    show captain_img at right with dissolve

    captain "他们有大约四十到五十人，藏身在铁匠峡谷的废弃矿洞里。地形易守难攻，强行进攻的话我们至少需要两百人。"

    hide captain_img
    show aldric_img at left with dissolve
    aldric "但我们的卫队目前只有一百二十人。其中一半分散在各个村庄和关隘。能调动的机动兵力最多六十人。"

    hide aldric_img
    show captain_img at left with dissolve
    captain "六十人攻一个有五十人防守的峡谷……伤亡会很大。"

    hide captain_img
    show aldric_img at left with dissolve
    aldric "领主大人，恕老朽直言——光靠艾登堡这点人，连匪帮都吃力。将来若有更大的麻烦，我们根本不够看。"

    hide aldric_img
    show player_char_img at left with dissolve
    player "那就不靠人数。两百人守不住一座城，但两百人足够守住一个秘密。我们赢不了硬仗——但可以让别人替我们打。"

    hide player_char_img with dissolve

    "你沉思着。匪患不解决，商路就断了。商路断了，税收就会锐减。但强攻的代价太高。"

    menu:
        "军事打击「集中兵力，一鼓作气」":
            $ change_stat("power", 8)
            $ change_courage(5)
            $ ch1_exp_bandit_plan = "military"
            $ log_decision("第一章扩展", "决定以军事手段剿匪")

            hide captain_img
            show player_char_img at left with dissolve
            player "调集所有能动的兵力。我们不能让匪患继续恶化。"

            hide player_char_img
            show captain_img at left with dissolve
            captain "六十人未必够——"

            hide captain_img
            show player_char_img at left with dissolve
            player "不需要正面强攻。我们先封锁峡谷的出入口，断水断粮。三天之内他们就会崩溃。同时派小股精锐从侧面的山路迂回，堵住他们的退路。"

            "雷恩思考了一会儿，手指在剑柄上敲了两下——那是他认真考虑某个提议时才有的动作。"

            hide player_char_img
            show captain_img at left with dissolve
            captain "……围困加迂回。消耗最小，效果最大。这个方案可行。"

            hide captain_img
            show player_char_img at left with dissolve
            player "一周内完成部署。商路每多断一天，我们就多损失一笔税收。"

            $ change_rel("rel_captain", 5)

        "招安谈判「给他们一条出路」":
            $ change_stat("reputation", 5)
            $ change_stat("loyalty", 5)
            $ ch1_exp_bandit_plan = "negotiate"
            $ log_decision("第一章扩展", "尝试招安土匪")

            player "他们为什么当匪？"

            "显然没人想过这个问题。"

            hide player_char_img
            show aldric_img at left with dissolve
            aldric "据说……黑狼帮的头目以前是个退伍老兵。北部山区今年遭了旱灾，庄稼绝收。那些'匪'里面有不少是走投无路的农民。"

            hide aldric_img
            show player_char_img at left with dissolve
            player "所以他们不是天生的匪，是被逼的。"

            "你站起身。"

            player "派使者去铁匠峡谷。告诉他们的头目——如果他们愿意放下武器，我可以给他们一条出路。退伍兵编入卫队，农民安排到领地的荒地上开垦。前三年免税。"

            hide player_char_img
            show captain_img at left with dissolve
            captain "大人，这太——"

            hide captain_img
            show player_char_img at left with dissolve
            player "太仁慈了？也许。但六十个士兵加上五十个归降的匪徒，就是一百一十人。这比强攻划算得多。"

            $ change_rel("rel_captain", -3)

        "设伏引蛇出洞「让他们自己送上门来」":
            $ change_stat("intrigue", 8)
            $ ch1_exp_bandit_plan = "ambush"
            $ log_decision("第一章扩展", "设计伏击土匪")

            player "强攻不行，招安也太慢。有没有办法让他们主动出来？"

            "你环顾众人，目光最终落在粮官身上。"

            player "下个月有大型商队经过吧？"

            hide player_char_img
            show servant_generic_img at left with dissolve

            servant "是、是的。格雷伯爵的秋粮商队，大约二十车。"

            hide servant_generic_img
            show player_char_img at left with dissolve
            player "把消息放出去。让黑狼帮知道这是一批大肥肉——但实际上，车里装的不是粮食，是我们的士兵。"

            "雷恩的眼神亮了起来。"

            hide player_char_img
            show captain_img at left with dissolve
            captain "诱饵战术。等他们劫车的时候，我们从两翼包抄。"

            hide captain_img
            show player_char_img at left with dissolve
            player "没错。在他们最松懈的时候一网打尽。"

            $ change_rel("rel_captain", 8)
            $ ch1_exp_captain_respect = True

            hide servant_generic_img with dissolve

    ## ── 议题二：税收 ──

    hide captain_img with dissolve

    hide player_char_img
    show aldric_img at left with dissolve
    aldric "第二个议题——税收。"

    "书记官颤颤巍巍地展开一卷账册，清了清嗓子。"

    show servant_generic_img at right with dissolve

    servant "领地的年税收约为一千二百金币。其中农业税六百，商业税三百，关税二百，其他一百。"

    servant "但今年的支出预计一千五百金币——城墙修缮三百，卫队饷银四百，行政开支二百，还有六百金币的王廷贡税。"

    servant "也就是说……我们有三百金币的缺口。"

    "你看了看账册。数字不会说谎。这个领地在财政上处于赤字状态。"

    hide servant_generic_img
    show aldric_img at left with dissolve
    aldric "老领主在世时靠积蓄填补了几年。但积蓄已经见底了。"

    menu:
        "提高税率「开源」":
            $ change_stat("wealth", 8)
            $ change_stat("loyalty", -8)
            $ ch1_exp_tax_decision = "raise"
            $ log_decision("第一章扩展", "决定提高领地税率")

            hide aldric_img
            show player_char_img at left with dissolve
            player "把农业税从十五提到二十。商业税从十提到十二。"

            "书记官的笔在纸上停住了。"

            hide player_char_img
            show servant_generic_img at left with dissolve
            servant "大人……百姓们已经很难了。再加税的话——"

            hide servant_generic_img
            show player_char_img at left with dissolve
            player "我知道。但城墙不修，来年哈根男爵一个冲锋就能踏平我们。卫队不养，匪患永远解决不了。"

            player "先撑过这个冬天。等商路恢复了，我们再想办法。"

            "你的语气不容置疑。书记官低下头，默默记录。"

            "你注意到奥尔德里克的眉头皱了一下。但他什么都没说。"

            $ change_rel("rel_aldric", -3)

        "削减开支「节流」":
            $ change_stat("wealth", 5)
            $ change_stat("power", -3)
            $ ch1_exp_tax_decision = "lower"
            $ log_decision("第一章扩展", "决定削减领地开支")

            player "不加税。削减开支。"

            "你拿过账册，逐项审视。"

            player "城墙修缮——先修北面和东面，其他方向暂缓，砍掉一半。卫队饷银——降低新兵薪水，老兵不动。行政开支——我不需要那么多侍从。砍掉三分之一。"

            hide player_char_img
            show aldric_img at left with dissolve
            aldric "少主，这些削减可能影响——"

            hide aldric_img
            show player_char_img at left with dissolve
            player "我知道。不过这样做，领民就不会觉得新领主上任第一件事是搜刮他们。"

            "你合上账册。"

            player "省下来的钱用来储备粮食。如果冬天特别冷，粮价会翻倍。到时候有粮食在手，比有金币在手更有用。"

            "书记官拼命点头。奥尔德里克的表情稍微舒展了一些。"

            $ change_rel("rel_aldric", 5)

        "改革税制「重新分配」":
            $ change_stat("wealth", 5)
            $ change_stat("reputation", 5)
            $ ch1_exp_tax_decision = "restructure"
            $ log_decision("第一章扩展", "决定改革领地税制")

            player "问题不在税率高低，在于税制不合理。"

            "你从书记官手中拿过账册，快速翻阅了几页。"

            player "农业税按田亩面积征收——但大户和小户交的比例一样。这对拥有几亩薄田的农民来说不公平。"

            player "从今天起，改成按收成比例征收。收成多的多交，收成少的少交。荒年减免。"

            player "商业税也一样。大商人的税率提高到十五，小摊贩降到五。"

            "书记官目瞪口呆。"

            hide player_char_img
            show servant_generic_img at left with dissolve
            servant "大人，这、这需要重新登记所有的——"

            hide servant_generic_img
            show player_char_img at left with dissolve
            player "我知道。所以从现在开始做。一个月内完成全领地的田亩和商户普查。"

            "你看着他们。"

            player "我父亲留下了一个好领地。但他也留下了一些需要改变的东西。改变从今天开始。"

            $ change_rel("rel_aldric", 8)
            $ change_stat("wealth", 3)

    ## ── 议题三：邻近领主 ──

    hide servant_generic_img with dissolve

    hide player_char_img
    show aldric_img at left with dissolve
    aldric "最后一个议题——邻近领主的动向。"

    "奥尔德里克的声音变得更加低沉。"

    aldric "冯·哈根男爵在边境增兵了。他的巡逻队越来越频繁地出现在我们的西部边界。上周，他的士兵甚至越过了界河，在我们的牧场上扎了营。"

    aldric "格雷伯爵保持中立，但他的态度很暧昧。我们不确定他会站在哪一边。"

    aldric "此外，主教马修斯上周派人来过——他想确认新领主对教会的'态度'。言外之意是，他希望您提高对教会的捐赠。"

    "三个方向，三股势力。你捏了下眉心。"

    hide aldric_img
    show player_char_img at left with dissolve
    player "关于男爵——先不动。让他越界扎营。一个月后如果他不撤，我们再谈。"

    player "关于伯爵——写封信，邀请他来做客。态度要热情，但不卑不亢。"

    player "关于主教——我会亲自去教堂拜访他。信仰是一面好盾牌，但不能让他把盾牌变成锁链。"

    show aldric_img at left with dissolve

    aldric "少主……您比我预期的更像一个领主。"

    "这是老管家第一次在议事中这样评价你。你不确定这是真心话还是安慰，但你选择当作真心话。"

    hide aldric_img with dissolve
    hide captain_img with dissolve

    "议事结束。你站起来，走到窗前。"

    "阳光已经升高了。城堡下方的村庄开始忙碌起来——农民赶着牛去田里，孩子在街道上追逐打闹，铁匠的锤声叮叮当当地响着。"

    "这些人的命运，现在握在你的手中。二十二岁的手。"

    "你握紧了拳头。不是因为紧张——是因为决心。"

    jump ch1_exp_training_yard

## ============================================================
## 第三部分：校场比武 — Training Yard (~250行)
## ============================================================

label ch1_exp_training_yard:

    $ play_music("audio/music/main_theme.ogg", fadein=2.0)

    scene bg castle_exterior with dissolve

    "午后。你换上了轻便的训练服，走向城堡后方的校场。"

    "校场是一块被踩得坚硬如铁的泥地，四周用木栅栏围着。角落里堆着木制训练刀剑、稻草靶和几副破旧的铠甲。"

    "二十几名卫兵正在校场上训练。有的在对练剑术，有的在跑步，有的在单杠上做引体向上。他们看到你来了，纷纷停下手中的动作，行礼致意。"

    "你注意到他们看你的眼神——好奇中夹杂着一丝审视。新领主来校场了，是来作秀的？还是真有两下子？"

    show captain_img at right with dissolve

    captain "领主大人。来视察训练吗？"

    hide captain_img
    show player_char_img at left with dissolve
    player "不只是视察。"

    "你走到武器架前，拿起了一柄训练用的木剑。掂了掂——分量还行。"

    player "雷恩，陪我练一练。"

    "校场上瞬间安静了。所有人都停下来看。"

    "雷恩的表情没有变化，但他的嘴角微微一动——是赞赏，还是觉得你在胡来？你读不出来。"

    hide player_char_img
    show captain_img at left with dissolve
    captain "大人确定？我可不会手下留情。"

    hide captain_img
    show player_char_img at left with dissolve
    player "我希望你不会。"

    "他从架子上取了一柄木剑。两人走到校场中央。士兵们自觉地围成一圈，给你们让出了一片空地。"

    "你攥了攥剑柄，举起了剑。"

    if prologue_study_focus == "sword":

        "六年的修道院剑术训练在这一刻被唤醒。你的身体记住了独眼骑士教给你的每一个动作——扎根、低重心、剑与前臂成一条直线。"

        "雷恩先出手。他的攻击快如闪电，一剑直刺你的左肩。你侧身闪开，同时反手一撩——木剑划过他的胸前铠甲，发出清脆的撞击声。"

        "他退了半步。眼中的审视变成了认真。"

        hide player_char_img
        show captain_img at left with dissolve
        captain "好。不是花架子。"

        "接下来的几分钟是一场真正的对决。你和雷恩你来我往，木剑的碰撞声在校场上回荡。泥土在你们的脚下被翻搅起来，汗水滴在干燥的地面上瞬间被吸收。"

        "你的速度和技巧可以和雷恩抗衡，但他的力量和经验明显胜过你一筹。每次硬碰硬，你的虎口都会被震得发麻。"

        "最终的结局在第三十七个回合——雷恩一记横扫突破了你的防线，木剑抵在了你的喉咙上。"

        "但在同一瞬间，你的剑也抵在了他的腹部。"

        captain "……平手。"

        "他看着你抵在他腹部的木剑，动作顿了顿，随即松开了握剑的手。"

        captain "如果这是真剑，我们两个都会死。但说实话——能逼到我做这种交换的人，不多。"

        $ ch1_exp_sparring_result = "draw"
        $ change_stat("power", 5)
        $ change_stat("reputation", 5)
        $ change_rel("rel_captain", 10)
        $ ch1_exp_captain_respect = True

    else:

        "你的剑术只是在修道院学的基础——防守还行，进攻就差了不少。而雷恩是战场上摸爬滚打过来的老兵，每一剑都带着实战的杀意。"

        "第一个回合，你就被打了个踉跄。他的攻击太快了，你的反应根本跟不上。"

        "第二个回合，你好歹挡住了他的劈砍，但手腕被震得几乎失去知觉。"

        "第三个回合——他虚晃一招，然后木剑轻巧地点在了你的肩膀上。"

        captain "结束了。"

        "你气喘吁吁地退了一步。三个回合，完败。"

        "周围的士兵们没有嘲笑——他们见过太多初出茅庐的年轻贵族被雷恩三招放倒。但你还是觉得脸上火辣辣的。"

        menu:
            "「再来一次。」":
                $ change_courage(8)
                $ change_stat("power", 3)
                $ log_decision("第一章扩展", "比武失败后要求再来")

                "你把掉在地上的木剑捡起来。"

                hide captain_img
                show player_char_img at left with dissolve
                player "再来。"

                "雷恩看了你一眼。"

                hide player_char_img
                show captain_img at left with dissolve
                captain "您已经——"

                hide captain_img
                show player_char_img at left with dissolve
                player "再来。"

                "这一次你没赢。也没在三个回合就输。你撑了七个回合。"

                "然后又来了一次。撑了十二个回合。"

                "到第四次的时候，你的衣服已经被汗水浸透了，手臂酸痛得几乎抬不起来。雷恩终于收了剑。"

                hide player_char_img
                show captain_img at left with dissolve
                captain "够了。您的底子不差，但缺实战经验。从明天起，每天来校场练一个时辰。三个月后，我保证您至少能撑二十个回合。"

                "你点了点头。嘴唇咸的——汗还是血？你没去管它。"

                "士兵们看你的眼神变了。不是因为你赢了——你没赢。是因为你站起来了四次。"

                $ ch1_exp_sparring_result = "defeat"
                $ change_rel("rel_captain", 8)
                $ ch1_exp_captain_respect = True

            "「我输了。教我。」":
                $ change_stat("reputation", 3)
                $ change_stat("power", 2)
                $ log_decision("第一章扩展", "虚心请教雷恩剑术")

                "你把木剑放回架子，走到雷恩面前。"

                hide captain_img
                show player_char_img at left with dissolve
                player "我的剑术不行。但我想学。你愿意教我吗？"

                "直白而坦诚。没有找借口，没有假装没输。"

                "雷恩的表情柔和了一瞬。"

                hide player_char_img
                show captain_img at left with dissolve
                captain "……明天清晨，日出时分。别迟到。"

                "你点了点头。"

                "周围的士兵面面相觑。他们的新领主——被三招放倒后没有恼怒，没有找借口，而是请求教导。"

                "这不是他们习惯的贵族做派。但也许，这正是他们需要的。"

                $ ch1_exp_sparring_result = "defeat"
                $ change_rel("rel_captain", 10)
                $ ch1_exp_captain_respect = True

    hide captain_img with dissolve

    "离开校场的时候，你的全身都在疼。但你的脚步很稳。"

    "力量不是天生的。但可以练出来。"

    "就像领导一个领地一样。"

    jump ch1_exp_village_visit

## ============================================================
## 第四部分：巡视村庄 — Village Visit (~300行)
## ============================================================

label ch1_exp_village_visit:

    $ play_music("audio/music/market_bustle.ogg", fadein=2.0)

    scene bg market with dissolve

    "第二天下午，你决定去巡视领地下方的村庄。"

    "奥尔德里克建议你带上卫队和全套仪仗——'让百姓看到新领主的威严'。你拒绝了。"

    show player_char_img at left with dissolve
    player "我要看到的是真实的村庄，不是被提前排练好的表演。"

    "你只带了艾琳娜和两名便装卫兵，换上了普通的外套，步行走进了村庄。"

    "这是一个典型的中世纪村庄——茅草屋顶的泥房、鹅卵石铺成的主街、一口石井、一座小教堂、一家铁匠铺和一个露天市场。"

    "空气中混杂着各种气味——面包房传来的酵母香、牛棚的腥膻、晾晒的腌肉发出的咸味，以及泥泞中不可言说的其他味道。"

    "村民们看到你时，有些迟疑。有人认出了你——消息传得很快。很快，街道两侧就聚集了一些人，远远地观望着。"

    "一个抱着孩子的老妇人朝你走来。她的背弯得像一张弓，脸上的皱纹比树皮还深。"

    crowd "您就是新领主？"

    player "是我。"

    crowd "老领主在的时候，路上的坑洼有人修。老领主走了以后，没人管了。我老婆子上周踩进坑里摔了一跤，膝盖到现在还肿着。"

    "她说得直白，不卑不亢。你感觉到了——这不是抱怨，是试探。她想看看新领主会怎么反应。"

    menu:
        "蹲下来看她的膝盖「先解决眼前的问题」":
            $ change_stat("loyalty", 8)
            $ change_stat("reputation", 5)
            $ log_decision("第一章扩展", "亲自关心受伤村民")

            "你在众人惊讶的目光中蹲了下来。"

            player "让我看看。"

            "老妇人愣住了。周围的村民也愣住了。一个领主——蹲在泥地上给一个农妇看膝盖？"

            "你轻轻卷起她的裤腿。膝盖确实肿了，青紫色的淤血扩散到了小腿。"

            player "艾琳娜，你带了药膏吗？"

            hide player_char_img
            show elena_img at left with dissolve

            elena "带了。金盏花膏，消肿止痛。"

            "她蹲下来，熟练地给老妇人涂抹药膏。老妇人的眼眶红了。"

            crowd "老领主……也这样。每次来村里都会问我们好不好……"

            hide elena_img
            show player_char_img at left with dissolve
            player "路会修的。我保证。"

            "你站起身来。周围的村民们看你的眼神变了——从观望变成了某种更温暖的东西。"

            hide elena_img with dissolve

            $ change_rel("rel_elena", 3)
            $ ch1_exp_villager_trust = True

        "严肃回应「我会安排人来修路」":
            $ change_stat("power", 3)
            $ change_stat("reputation", 3)
            $ log_decision("第一章扩展", "严肃回应村民的诉求")

            player "修路的事我记下了。三天之内会派人来。"

            "你的语气简短而坚定。老妇人点了点头，退到了一边。"

            "你继续往前走。你知道一个领主不能对每个人都嘘寒问暖——那样反而会让人觉得你软弱。但你也记住了她的话。"

            "修路。三天之内。你给自己定了一个期限。"

    ## ── 集市纠纷 ──

    scene bg market with dissolve

    "你走进了村庄的露天市场。几十个摊位沿着主街排开——卖蔬菜的、卖布匹的、卖陶器的、卖铁制品的。"

    "热闹的叫卖声在你耳边此起彼伏。空气中飘浮着烤栗子和热苹果酒的香气。"

    "突然——一阵吵闹声从市场的东端传来。"

    "你快步走过去，看到一群人围成一圈。圈子中央，两个男人正在激烈地争吵。"

    "一个是商人——你认出他穿着格雷伯爵领地的商人制服。另一个是本地农民——粗糙的手掌，被太阳晒得黝黑的脸。"

    show merchant_karl_img at left with dissolve

    merchant "你这个骗子！你卖给我的粮食里掺了沙子！整整三十袋，每袋至少少了两成！"

    crowd "你才是骗子！我的粮食是一粒一粒收的！是你的秤有问题！你们外地商人就知道欺负我们！"

    "围观的村民明显站在农民这边。但商人也不示弱——他拉来了两个随行的伙计作证。"

    "局面越来越紧张。有人已经开始挽袖子了。"

    "然后有人注意到了你。"

    crowd "领主大人来了！领主大人来了！"

    "所有人的目光转向你。商人和农民同时安静了下来。"

    "这是你作为领主要做的第一个公开裁决。所有人都在看着你。"

    menu:
        "当众检验粮食和秤「用事实说话」":
            $ change_stat("reputation", 5)
            $ change_stat("reputation", 8)
            $ ch1_exp_market_verdict = "compromise"
            $ log_decision("第一章扩展", "亲自验秤验粮，公正裁决")

            hide merchant_karl_img
            show player_char_img at left with dissolve
            player "把粮食和秤都拿来。"

            "你走到两人中间，面色平静。"

            player "在场有没有铁匠？借我一杆你自己用的秤。"

            "铁匠的妻子跑过来，递上了一杆秤。你亲手称了三袋粮食。"

            "结果——粮食确实偏轻，每袋大约少了一成。但商人的秤也有问题——偏重了半成。"

            player "粮食确实不够秤。但商人的秤也不准。两边都有问题。"

            "你看了看两人。"

            player "这样：农民补足缺少的粮食。商人用铁匠的秤重新计量，按公秤价格结算。差额双方各承担一半。"

            "商人和农民互相看了看。都不太满意，但也说不出什么。"

            player "而且从今天起——村市每月初由我的书记官来校验所有的秤。发现作假的，罚款十倍。"

            "人群中响起了一阵低语。几个村民点了点头。"

            "你的第一次裁决——不偏不倚，有理有据。也许不够精彩，但足够公正。"

            $ ch1_exp_villager_trust = True

        "偏向农民「保护自己的领民」":
            $ change_stat("loyalty", 8)
            $ change_stat("reputation", 3)
            $ change_stat("wealth", -3)
            $ ch1_exp_market_verdict = "farmer_side"
            $ log_decision("第一章扩展", "偏袒本地农民")

            player "你们从外地来做生意，在我的领地上赚钱，就要守我的规矩。"

            "你看着商人。"

            player "你的秤是你自己带的。你怎么证明你的秤是准的？"

            "商人哑口无言。"

            player "带不了证明就别来告状。这次就算了。但下次如果你还想在这里做生意——带上官方校验过的秤。"

            "商人灰溜溜地走了。村民们发出了一阵欢呼。"

            "但你知道——你刚才的裁决不够公正。农民的粮食可能确实掺了沙子。但在这个时刻，你需要的是领民的信任，而不是外地商人的好感。"

            "政治，有时候就是选择得罪谁。"

            $ ch1_exp_villager_trust = True
            $ change_rel("rel_aldric", -3)

        "偏向商人「维护商业秩序」":
            $ change_stat("wealth", 8)
            $ change_stat("loyalty", -5)
            $ ch1_exp_market_verdict = "merchant_side"
            $ log_decision("第一章扩展", "偏袒外地商人以维护商誉")

            player "商人远道而来做生意，是我们领地的贵客。如果连交易的基本诚信都保证不了，以后谁还愿意来这里？"

            "你看着农民。"

            player "回去把粮食重新筛一遍。如果确实掺了沙子，你要赔偿全部损失。如果没有问题，我会让商人道歉。"

            "农民的脸涨得通红，但他不敢顶嘴。周围的村民们不满地议论着。"

            "你知道你这个裁决不得人心。但商路是领地的命脉。如果艾登堡的名声变成'会骗外地商人的地方'，损失远不止三十袋粮食。"

            "有些时候，做正确的事和做受欢迎的事，不是同一回事。"

    hide merchant_karl_img with dissolve

    ## ── 村庄见闻 ──

    scene bg market with dissolve

    "处理完纠纷后，你继续在村庄里走了一圈。"

    "你去了铁匠铺——铁匠是个沉默寡言的中年人，正在打造一柄犁头。他告诉你今年的铁价涨了三成，因为北方的矿山出了事故。"

    "你去了面包房——面包师傅的妻子硬塞给你一块刚出炉的黑麦面包。粗糙但扎实，带着麦秆的清香。"

    "你去了教堂——村里的老牧师向你介绍了本堂的情况。教堂的屋顶漏了，他已经向主教申请修缮经费两年了，没有回音。"

    "你在一棵老橡树下坐了一会儿。橡树的年轮比这个村庄还老。树干上刻满了名字——几代人的名字，有些已经模糊不清。"

    "你在最高处的位置看到了一行字——'K·V·A 1310'。K·V·A——那是你祖父的名字缩写。"

    "他也曾坐在这棵树下。看着这些房屋，这些田地，这些面孔。"

    "你站起来，拍了拍衣服上的灰尘。太阳正在西沉，是时候回城堡了。"

    "在回去的路上，你做了几个决定——"

    "修路。校验秤。修教堂屋顶。给铁匠减税。"

    "不是什么惊天动地的事。但对这个村庄来说，这些比什么都重要。"

    jump ch1_exp_evening_feast

## ============================================================
## 第五部分：晚宴风云 — Evening Feast (~250行)
## ============================================================

label ch1_exp_evening_feast:

    $ play_music("audio/music/great_hall.ogg", fadein=2.0)

    scene bg great_hall with dissolve

    "你回到城堡时，发现大厅正在进行紧急的布置。仆人们穿梭忙碌着——铺桌布、摆银器、点蜡烛、挂织锦。"

    show aldric_img at left with dissolve

    aldric "少主——有客人来了。威尔斯子爵和两位地方骑士。他们说是'路过拜访'，但我们都知道，没有人会'路过'艾登堡。"

    hide aldric_img
    show player_char_img at left with dissolve
    player "他们想干什么？"

    hide player_char_img
    show aldric_img at left with dissolve
    aldric "试探您。老领主走了，所有人都想看看新领主是什么料。今晚的宴会将是您的第一次正式亮相。"

    "奥尔德里克的表情比平时更加严肃。"

    aldric "少主，请允许我直言——今晚的每一句话、每一个表情、甚至您举杯的姿势，都会被他们分析和传播。从某种意义上说，今晚比任何一场战役都重要。"

    hide aldric_img with dissolve

    "你回到房间换了正装——深蓝色的丝绒外套，金鹰纹章别在胸口。镜子里的你看起来比实际年龄成熟了几岁——也许是因为这两天的经历。"

    "你推开了宴会厅的大门。"

    ## ── 宴会开始 ──

    scene bg great_hall with dissolve

    "宴会厅灯火通明。长桌上摆满了食物——烤野猪、焖鹿肉、奶油浓汤、新鲜面包、蜂蜜蛋糕，以及成排的银酒壶。"

    "三位客人已经在座。"

    "威尔斯子爵——一个四十出头的瘦高男人，穿着考究到近乎夸张的天鹅绒服饰。他的嘴角永远带着一丝礼貌而空洞的微笑。"

    "他左边是贝尔福骑士——身材魁梧，满脸络腮胡，显然更擅长挥剑而不是说话。"

    "右边是温德尔骑士——年纪更大，表情阴沉，像是永远在算计什么。"

    show viscount_wells_img at left with dissolve

    viscount_wells "啊，年轻的领主！终于见到真人了。令尊生前常常提到您——总是满口赞美。"

    "你知道这是客套话。你父亲不是那种会'满口赞美'的人。"

    hide viscount_wells_img
    show player_char_img at left with dissolve
    player "子爵阁下远道而来，是艾登堡的荣幸。请入座。"

    "宴会开始了。"

    "前几道菜的时间里，对话一直维持着表面的礼貌——天气、收成、猎季。但你感觉到了暗流——威尔斯子爵的每一个问题都经过精心设计。"

    hide player_char_img
    show viscount_wells_img at left with dissolve
    viscount_wells "听说北部的匪患很严重？贵领地打算如何处理？"

    "这是第一次试探。如果你说正在处理，他会觉得你软弱。如果你说已经解决了，他会知道你在吹牛。"

    hide viscount_wells_img
    show player_char_img at left with dissolve
    player "正在处理中。我对结果很有信心。"

    "不多不少。子爵的笑容没变，但你注意到温德尔骑士和贝尔福骑士交换了一个眼神。"

    hide player_char_img
    show viscount_wells_img at left with dissolve
    viscount_wells "年轻人有自信是好事。不过如果需要帮助，我的骑士随时可以——"

    hide viscount_wells_img
    show player_char_img at left with dissolve
    player "多谢好意。但艾登堡的问题，由艾登堡自己解决。"

    "子爵举起酒杯，向你致意。但他的眼睛没有笑。"

    ## ── 宴会高潮：祝酒词 ──

    "几轮酒过后，气氛渐渐热络。这时候，威尔斯子爵提出了一个看似随意的建议——"

    hide player_char_img
    show viscount_wells_img at left with dissolve
    viscount_wells "按照惯例，新领主的第一次宴会应该致一段祝酒词。不知年轻的领主可有准备？"

    "他的语气很轻松，但意图很明确——这是逼你当众表态。你的祝酒词将被传遍整个地区，成为所有人评判你的依据。"

    "你站起身来。手中的银杯在烛光下闪烁。"

    "大厅安静了下来。所有人——客人、仆人、卫兵——都看着你。"

    menu:
        "谦逊恭敬「以退为进」":
            $ change_stat("reputation", 5)
            $ change_stat("loyalty", 5)
            $ ch1_exp_toast_style = "humble"
            $ log_decision("第一章扩展", "以谦逊姿态致祝酒词")

            hide viscount_wells_img
            show player_char_img at left with dissolve
            player "各位尊贵的客人——"

            "你深吸一口气。"

            player "我的父亲治理这片土地近三十年。三十年间，他从不曾让任何一个领民饿肚子，也不曾让任何一个敌人安然踏过边境。"

            player "我没有他的经验，没有他的智慧，甚至没有他的年纪。我只有二十二岁。在座的各位，恐怕都比我更了解这片土地。"

            player "但我有一样东西——我父亲交给我的承诺。守护这片土地，守护这里的人民。"

            player "所以今晚，我不敢以领主的身份向你们敬酒。我以一个学徒的身份——请各位多多指教。"

            "你举起酒杯。"

            player "为了艾登堡。为了和平。为了在座的每一位。"

            "掌声。不是那种敷衍的礼貌鼓掌——是真正的掌声。连贝尔福骑士那张粗犷的脸上都露出了动容的神色。"

            "威尔斯子爵鼓掌的同时微微眯起了眼睛——他在重新评估你。一个能说出这种话的年轻人，不是他原先以为的愣头青。"

            $ ch1_exp_noble_impressed = True

        "气势磅礴「宣示主权」":
            $ change_stat("power", 8)
            $ change_stat("reputation", 5)
            $ change_courage(5)
            $ ch1_exp_toast_style = "bold"
            $ log_decision("第一章扩展", "以强势姿态致祝酒词")

            player "各位——"

            "你的声音不高，但每一个字都清晰有力。"

            player "我父亲走了。金鹰旗依旧飘扬。这面旗帜在艾登堡的城墙上飘了两百年，从未落地。"

            player "有人也许觉得，老领主一走，艾登堡就散了。有人也许在打算盘——是不是该趁新领主年轻，占点便宜。"

            "你的目光扫过在座的每一个人。温德尔骑士低下了头。"

            player "我今天要告诉各位——不要。"

            player "我虽然年轻，但我的剑不钝，我的城墙不矮，我的人民不弱。试图试探艾登堡底线的人——我建议你们三思。"

            "你停顿了一秒，然后语气忽然柔和了。"

            player "但对朋友，我永远敞开大门。今晚在座的都是朋友。为了我们的友谊。干杯。"

            "掌声。但这次的掌声里夹杂着一丝敬畏。贝尔福骑士大声叫好。温德尔骑士面无表情。威尔斯子爵的眼睛闪了一下——像是在闪光中看到了一把出鞘的剑。"

            $ ch1_exp_noble_impressed = True
            $ change_rel("rel_captain", 5)

        "暗藏玄机「字里行间埋线索」":
            $ change_stat("intrigue", 8)
            $ change_stat("reputation", 5)
            $ ch1_exp_toast_style = "cunning"
            $ log_decision("第一章扩展", "以暗含深意的方式致祝酒词")

            player "各位尊贵的来客——"

            "你露出一个恰到好处的微笑。"

            player "我父亲生前教过我很多东西。其中最重要的一课是——永远记住谁在你困难的时候伸出了手。"

            "你看了看威尔斯子爵。"

            player "也要记住谁在你困难的时候袖手旁观。"

            "你看了看温德尔骑士。他的表情僵了一瞬。"

            player "当然，最重要的是——记住谁在你困难的时候落井下石。"

            "你的目光没有落在任何特定的人身上。但大厅里的气氛微妙地变了。"

            player "今晚的酒很好。明天开始，让我们一起面对前方的路。为了诚实的友谊——干杯。"

            "你饮尽杯中酒。'诚实的友谊'这几个字在空气中缓缓沉淀。每个人都在揣摩你到底知道些什么。"

            "威尔斯子爵的微笑终于出现了一丝裂痕。他在想——这个年轻人，到底是在随口说说，还是已经掌握了什么？"

            "不确定性。这才是最好的武器。"

            $ ch1_exp_noble_impressed = True

    ## ── 宴后密谈 ──

    hide viscount_wells_img with dissolve

    scene bg study with dissolve

    "宴会在午夜时分结束。客人们被安排在客房过夜。"

    "你回到书房，卸下了一整晚的面具。肩膀终于塌了下来——演了一整晚的戏，比练一天的剑还累。"

    show aldric_img at left with dissolve

    "奥尔德里克推门进来，手里端着一杯热茶。他把茶放在你面前，然后在你对面坐下。"

    aldric "少主今晚的表现……出乎所有人的意料。"

    hide aldric_img
    show player_char_img at left with dissolve
    player "包括你？"

    "老管家微微笑了。"

    hide player_char_img
    show aldric_img at left with dissolve
    aldric "包括我。"

    "他的目光落在壁炉上方那幅你父亲的画像上。然后他说了一段你没想到的话。"

    aldric "少主……有些事情，我应该更早告诉您的。"

    "他的声音低沉了下来。"

    aldric "老领主去世前一个月，他把我叫到书房。他给了我一个铁箱的钥匙，让我在他走后交给您。"

    aldric "他说：'等孩子准备好了再给他。如果他在第一个月就展现出领主的气质——就是时候了。'"

    "他从怀中取出一把泛着铜绿的小钥匙，放在桌上。"

    aldric "少主，您准备好了。"

    "你看着那把钥匙。它在烛光下安静地躺着，像是一扇门的邀请。"

    "通往真相的门。通往父亲的秘密的门。"

    "你伸手拿起了钥匙。金属冰凉地贴在掌心。"

    hide aldric_img
    show player_char_img at left with dissolve
    player "谢谢你，奥尔德里克。"

    "老管家站起身，向你深深鞠了一躬。"

    hide player_char_img
    show aldric_img at left with dissolve
    aldric "我侍奉过两代领主。第三代……我也会守到最后。"

    $ ch1_exp_aldric_confession = True
    $ change_rel("rel_aldric", 10)
    $ change_stat("loyalty", 3)

    hide aldric_img with dissolve

    ## ── 章节尾声 ──

    scene bg castle_exterior_night with dissolve

    "奥尔德里克走后，你站在窗前。"

    "城堡下方的村庄已经完全沉入了黑暗。只有远处山丘上的一两点篝火还在闪烁——也许是牧羊人，也许是猎人，也许是别的什么人。"

    "你手中攥着那把钥匙。掌心已经把金属捂暖了。"

    "这一天你做了太多事——探索城堡、主持议事、校场比武、巡视村庄、应对宴会。每一件事都像是一场考试。"

    "你不知道自己考得怎么样。也许及格了。也许勉强通过。也许……"

    "窗外，风吹动了城墙上的旗帜。黑色的丧旗在夜风中无声地翻卷。"

    "但你注意到——在丧旗的旁边，有人挂上了另一面旗帜。金色的鹰在深蓝色的底布上展翅欲飞。"

    "那是你的家族旗帜。有人——也许是雷恩，也许是奥尔德里克——已经在丧旗旁边升起了新的旗帜。"

    "旧的旗帜尚未降下。新的旗帜已经升起。"

    "就像这片土地一样。旧的领主走了，新的领主来了。哀伤与希望并存。"

    "你把钥匙塞进了贴身的口袋。"

    "明天，你会用这把钥匙打开父亲留下的铁箱。"

    "明天，你会知道更多的真相。"

    "但今晚——"

    "你只是一个站在窗前的二十二岁的年轻人。看着自己的领地，看着自己的人民，看着远处的山和更远处的星空。"

    "夜风凉而清冽，带着秋天的味道。"

    "你闭上了眼睛。"

    show storyteller_img at left with dissolve
    storyteller "公元1347年。深秋。"

    storyteller "艾登堡的新主人已在这座古老的城堡中度过了数个日夜。"

    storyteller "没有人知道他将成为怎样的领主——是铁腕的暴君，还是仁慈的明主？是运筹帷幄的谋士，还是冲锋陷阵的战士？"

    storyteller "但有一件事是确定的——"

    storyteller "棋盘已经摆好。棋子已经落座。"

    storyteller "第一步棋，已经走出。"

    scene black with dissolve

    "第一章扩展·完"

    return

## ============================================================
## 第二章扩展：领主会议深层剧情
## chapter2_expansion.rpy
## 会前准备 / 大厅辩论 / 私下会面 / 宴会 / 夜间阴谋
## ============================================================

## ── 扩展属性（映射到现有属性系统） ──
## authority → power, wisdom → intrigue, charm → reputation, military → loyalty
## 以下为新增关系变量

default rel_hilda = 0
default rel_grey = 0
default rel_wells = 0
default rel_stein = 0
default rel_people = 30

## ── 第二章扩展剧情标记 ──
default ch2_exp_aldric_briefed = False
default ch2_exp_tax_stance = ""          # "reform" / "maintain" / "compromise"
default ch2_exp_border_stance = ""       # "military" / "diplomatic" / "alliance"
default ch2_exp_trade_stance = ""        # "free" / "regulated" / "monopoly"
default ch2_exp_hilda_alliance = False
default ch2_exp_grey_secret = False
default ch2_exp_wells_bribed = False
default ch2_exp_stein_pact = False
default ch2_exp_werner_confronted = False
default ch2_exp_banquet_toast = ""       # "humble" / "bold" / "witty"
default ch2_exp_night_choice = ""        # "confront" / "follow" / "ignore"
default ch2_exp_spy_identity = ""        # "wells_agent" / "queen_agent" / "unknown"
default ch2_exp_secret_letter = False
default ch2_exp_poison_discovered = False
default ch2_exp_grey_favor = False
default grey_met = False
default steinfurt_met = False
default wells_met = False
default karl_met = False
default bishop_met = False
default prince_met = False
default hilda_met = False
default lily_master_met = False
default people_met = False
default dusk_dew_known = False
default lily_trial_passed = False
default ch2_exp_stein_trust = False
default ch2_exp_werner_humiliated = False
default ch2_exp_private_count = 0

## ============================================================
## 第四部分：宴会 — The Banquet
## ============================================================

label ch2_exp_banquet:

    scene bg castle_hall with dissolve
    $ play_music("audio/music/tavern_lively.ogg", fadein=2.0)

    "夜幕降临，哈伦堡的宴会厅灯火通明。"

    "这是会议前夜的欢迎宴——不是议事，只是旧识新交之间的寒暄与试探。明日的正式会议才是真正的战场。"

    "巨大的枝形吊灯上插满了蜡烛，将整个大厅照得如同白昼。长桌上摆满了丰盛的菜肴——烤全羊、炖野猪、蜜渍水果、新鲜出炉的面包。"

    "乐师们在角落里演奏着轻快的曲调。侍从们端着酒壶穿梭其间，不断给宾客们添酒。"

    "这是一场表面上的欢宴。谁和谁坐在一起，谁给谁斟了酒，你都看在眼里。"

    "你环视一圈——冯·哈根男爵并未到场。据说他的车队傍晚才过莱因河，赶不上今夜的宴席，明日会议上才会与你正面相见。"

    "已经到场的几位领主各自散坐在长桌两侧。你注意到，座位的安排很有讲究——"

    "你被安排在格雷伯爵和施泰因伯爵夫人之间。维尔纳公子在你的对面，不时投来挑衅的目光。"

    "酒过三巡，气氛渐渐热络起来。"

    "格雷伯爵悄声对你说——"

    $ hide_all_chars("count_grey_img")
    show count_grey_img at left with dissolve

    count_grey "注意看。"

    "维尔纳公子站了起来，举起酒杯。"

    hide count_grey_img with dissolve
    $ hide_all_chars("noble_werner_img")
    show noble_werner_img at left with dissolve

    noble_werner "诸位领主，我有一个提议——不如趁着酒兴，每人说一段祝词？"

    noble_werner "我先来。"

    "他清了清嗓子，环视全场。"

    noble_werner "敬这片土地上所有伟大的领主。有些人是靠自己的能力登上领主之位的，有些人……只是靠了一个好姓氏。"

    "他的目光毫不掩饰地落在了你身上。"

    noble_werner "但无论如何，希望我们都能证明自己配得上手中的权力。尤其是——某些刚刚继位的年轻领主。"

    $ hide_all_chars()
    $ hilda_met = True
    "嘲讽之意溢于言表。其他领主的反应各不相同——威尔斯子爵尴尬地咳嗽，施泰因伯爵夫人皱起了眉头，希尔达伯爵夫人面无表情地看着你。"

    "格雷伯爵轻轻碰了碰你的手肘。"

    hide noble_werner_img
    $ hide_all_chars("count_grey_img")
    show count_grey_img at left with dissolve

    count_grey "到你了。"

    "全场的目光集中到你身上。这是你在宴会上展现自我的时刻。"

    hide count_grey_img with dissolve
    hide noble_werner_img with dissolve

    menu:
        "维尔纳公子的挑衅需要一个回应。你的祝词将定义你在众人心中的形象。"

        "谦逊应对「以退为进」":
            $ ch2_exp_banquet_toast = "humble"
            $ change_stat("reputation", 5)
            $ change_rel("rel_grey", 10)
            $ change_rel("rel_hilda", 5)
            $ log_decision("第二章扩展", "宴会上谦逊应对")

            "你缓缓站起身来，举起了酒杯。"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "维尔纳公子说得没错。我确实是靠姓氏继承了领主之位。"

            "全场一静。"

            player "但这个姓氏代表着父辈的心血和百姓的信任。我不敢辜负它。"

            player "所以我的祝词很简单——敬所有在困境中依然坚守的人。不论是战场上流血的士兵，还是田地里劳作的农民。"

            player "我们坐在这里享用美酒佳肴，是因为有人在替我们负重前行。"

            "杯盏碰撞的声音都停了下来。然后，格雷伯爵第一个鼓起了掌。"

            hide player_char_img
            $ hide_all_chars("count_grey_img")
            show count_grey_img at left with dissolve

            count_grey "好。说得好。"

            "希尔达伯爵夫人也微微点头。维尔纳公子的脸上闪过一丝尴尬。"

        "针锋相对「直接回击」":
            $ ch2_exp_banquet_toast = "bold"
            $ change_stat("power", 5)
            $ change_courage(8)
            $ change_rel("rel_hilda", 8)
            $ change_rel("rel_grey", -3)
            $ log_decision("第二章扩展", "宴会上针锋相对")

            "你站起身来，目光直视维尔纳公子。"

            hide count_grey_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "感谢维尔纳公子的关心。是的，我是新领主，经验不足。"

            player "但至少——我是亲自坐在这里，而不是替我躲在家里的老父亲跑腿。"

            "全场倒吸一口凉气。你知道这句话很不客气，但维尔纳公子先开的火。"

            hide count_grey_img
            show noble_werner_img at right with dissolve

            noble_werner "你！"

            hide noble_werner_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我的祝词——敬这桌上还记得我父亲是怎么走的人。"

            "维尔纳公子气得面色通红，但在这个场合不好发作。"

            hide noble_werner_img
            hide player_char_img
            $ hide_all_chars("countess_hilda_img")
            show countess_hilda_img at left with dissolve
            hide noble_werner_img with dissolve

            countess_hilda "年轻人有血性。好。"

            "威尔斯子爵在一旁低声笑了起来。"

            $ ch2_exp_werner_humiliated = True

        "以幽默化解「四两拨千斤」":
            $ ch2_exp_banquet_toast = "witty"
            $ change_stat("reputation", 8)
            $ change_stat("wealth", 3)
            $ change_rel("rel_wells", 8)
            $ change_rel("rel_stein", 8)
            $ log_decision("第二章扩展", "宴会上以幽默化解")

            "你举起酒杯，脸上挂着从容的微笑。"

            hide countess_hilda_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "维尔纳公子的祝词很有深度。让我也来一个。"

            player "我听说有个故事——一只老狐狸对一只年轻的狼说：「你只是靠了一副好牙齿。」年轻的狼回答说：「是啊，但至少我的牙齿还在。」"

            "全场先是一愣，然后爆发出哄堂大笑。"

            player "所以——敬我们所有人的牙齿！无论是新的还是旧的，希望它们都能咬得动这个世界。"

            "格雷伯爵笑得合不拢嘴。威尔斯子爵笑得更是前仰后合。"

            hide countess_hilda_img
            show viscount_wells_img at right with dissolve

            viscount_wells "这个年轻人——有趣！我喜欢！"

            $ hide_all_chars()
            "甚至施泰因伯爵夫人也露出了难得的微笑。只有维尔纳公子的脸色很难看。"

    "宴会继续进行。酒越来越多，气氛越来越热。"

    hide count_grey_img with dissolve
    hide countess_hilda_img with dissolve
    hide viscount_wells_img with dissolve

    "你注意到维尔纳公子在角落里和一个黑衣人低声交谈。那人的斗篷遮住了大半张脸，看不清容貌。"

    "谈话结束后，维尔纳公子回到桌前。他端起酒杯朝你遥遥一举，嘴角露出一个意味深长的笑容。"

    hide player_char_img with dissolve
    $ hide_all_chars("noble_werner_img")
    show noble_werner_img at left with dissolve

    noble_werner "艾登堡领主，今天这顿酒我请了。但人生不是只有一场宴会。"

    noble_werner "有些账……以后再算。"

    "你感受到了这句话中隐含的威胁。"

    hide noble_werner_img with dissolve

    $ hide_all_chars()
    "宴会在午夜时分结束。宾客们陆续散去。你独自走在回房的路上，脑中翻涌着今日的种种见闻。"

    "忽然——"

    "你听到了一个不该在这个时间出现的声音。"

    "那是脚步声。很轻，很小心，像猫一样无声地移动。"

    "你停下脚步，屏住呼吸。在走廊的尽头，一个黑影一闪而过。"

    "那个方向——通往哈伦堡的档案室。"

    jump ch2_exp_night_intrigue

## ============================================================
## 第五部分：夜间阴谋 — Night Intrigue
## ============================================================

label ch2_exp_night_intrigue:

    scene bg castle_hall with dissolve
    $ play_music("audio/music/conspiracy.ogg", fadein=1.5)

    "走廊里很暗。蜡烛已经熄灭了大半，火把的光只照到三步远。"

    "那个黑影拐进了通往档案室的走廊，脚步声轻得像猫。你的心跳加速了——档案室里存放着哈伦堡的历年会议记录、各领主的秘密协议副本，甚至还有王室的特许令状。"

    "如果有人在偷取这些文件……"

    "你快速评估了一下形势。你身上没有武器，护卫们都在营房里。现在叫人可能会惊走那个黑影。"

    menu:
        "走廊尽头传来轻微的声响。"

        "直接追上去质问「正面交锋」":
            $ ch2_exp_night_choice = "confront"
            $ change_courage(10)
            $ change_stat("power", 5)
            $ log_decision("第二章扩展", "正面追踪夜间潜入者")

            "你没有犹豫，大步流星地朝档案室走去。"

            "推开沉重的木门时，你看到了那个黑影——他正弯腰在一个柜子里翻找什么。"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "站住！你是谁？"

            $ hide_all_chars()
            "黑影猛地转身。你等了一瞬让眼睛适应黑暗，才看到了一张蒙着面纱的脸，只露出一双惊慌的眼睛。"

            "那双眼睛——你觉得似曾相识。"

            "黑影没有回答，而是飞快地将手中的东西塞进斗篷里，然后朝窗户扑去。"

            "你毫不犹豫地冲上前，一把抓住了他的斗篷。"

            "在撕扯中，面纱滑落了。"

            "你愣住了。"

            "那是一张女人的脸。你见过这张脸——"

            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve

            elena "……是我。"

            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "艾琳娜？！你在这里做什么？"

            "艾琳娜的脸上闪过复杂的表情——惊慌、羞愧，还有一丝决绝。"

            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "我……我在执行任务。"

            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "谁的任务？"

            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "王后的。"

            "你的心沉了下去。奥尔德里克的提醒果然没有错——她终究还是王后的人。"

            elena "王后怀疑维尔纳家族在秘密筹备叛乱。她要我找到证据。"

            elena "这间档案室里有一份十年前的协议——维尔纳老伯爵与北方蛮族的秘密通商协议。如果这份文件存在，就足以证明维尔纳家族早就在与蛮族勾结。"

            $ ch2_exp_spy_identity = "queen_agent"

            menu:
                "艾琳娜是王后的密探。你发现了她的秘密身份。"

                "帮助她「一起寻找那份协议」":
                    $ change_rel("rel_elena", 15)
                    $ change_stat("loyalty", 8)
                    $ ch2_exp_secret_letter = True
                    $ log_decision("第二章扩展", "帮助艾琳娜窃取情报")

                    hide elena_img
                    $ hide_all_chars("player_char_img")
                    show player_char_img at left with dissolve
                    player "……我帮你找。"

                    hide player_char_img
                    $ hide_all_chars("elena_img")
                    show elena_img at left with dissolve
                    elena "你——你愿意帮我？"

                    hide elena_img
                    $ hide_all_chars("player_char_img")
                    show player_char_img at left with dissolve
                    player "维尔纳家族如果真的在与蛮族勾结，那就是所有领主的威胁。不只是王后关心这件事。"

                    $ hide_all_chars()
                    "你们摸着黑一起翻找档案，只靠一根快烧到底的蜡烛。终于，在一个落满灰尘的抽屉最底层，你发现了那份协议的副本。"

                    "文件上的内容让你倒吸一口凉气——维尔纳老伯爵不只是和蛮族通商，他还在向蛮族出售武器。"

                    $ hide_all_chars("player_char_img")
                    show player_char_img at left with dissolve
                    player "这……如果公之于众，维尔纳家族就完了。"

                    hide player_char_img
                    $ hide_all_chars("elena_img")
                    show elena_img at left with dissolve
                    elena "这正是王后想要的。"

                    "艾琳娜小心翼翼地将文件收好。她看着你，目光中多了一些说不清的东西。"

                    elena "谢谢你。我以为你会抓我交给其他领主。"

                    hide elena_img
                    $ hide_all_chars("player_char_img")
                    show player_char_img at left with dissolve
                    player "也许我该这么做。但我选择相信你。"

                    hide player_char_img
                    $ hide_all_chars("elena_img")
                    show elena_img at left with dissolve
                    elena "你不会后悔的。"

                    $ change_rel("rel_elena", 5)

                "让她离开，但没收文件「两面下注」":
                    $ change_stat("intrigue", 10)
                    $ change_rel("rel_elena", -5)
                    $ log_decision("第二章扩展", "没收艾琳娜的情报")

                    hide elena_img
                    $ hide_all_chars("player_char_img")
                    show player_char_img at left with dissolve
                    player "你走吧。但那份文件——留在我这里。"

                    hide player_char_img
                    $ hide_all_chars("elena_img")
                    show elena_img at left with dissolve
                    elena "什么？"

                    hide elena_img
                    $ hide_all_chars("player_char_img")
                    show player_char_img at left with dissolve
                    player "王后想要的证据，我来保管。我不会把你的身份告诉任何人。但这份文件应该由我来决定怎么用。"

                    "艾琳娜紧紧抿着嘴唇，显然很不情愿。但她知道自己没有选择的余地。"

                    hide player_char_img
                    $ hide_all_chars("elena_img")
                    show elena_img at left with dissolve
                    elena "……好。但王后迟早会知道这件事。"

                    hide elena_img
                    $ hide_all_chars("player_char_img")
                    show player_char_img at left with dissolve
                    player "让她知道。让她也知道——我不是任何人的棋子。"

                    "艾琳娜留下了文件，门合上了，蜡烛火焰晃了一下。"

                    $ ch2_exp_secret_letter = True

                "揭发她「将此事公开」":
                    $ change_stat("reputation", 5)
                    $ change_rel("rel_elena", -20)
                    $ change_courage(5)
                    $ log_decision("第二章扩展", "揭发艾琳娜的间谍身份")

                    $ hide_all_chars("player_char_img")
                    show player_char_img at left with dissolve
                    player "你知道你在做什么吗？在领主会议期间偷取机密文件——这是死罪。"

                    hide player_char_img
                    $ hide_all_chars("elena_img")
                    show elena_img at left with dissolve
                    elena "你要揭发我？"

                    hide elena_img
                    $ hide_all_chars("player_char_img")
                    show player_char_img at left with dissolve
                    player "我必须这么做。如果我放任王后的密探在哈伦堡偷窃情报而不报告——那我和你有什么区别？"

                    "艾琳娜闭上了眼睛。"

                    hide player_char_img
                    $ hide_all_chars("elena_img")
                    show elena_img at left with dissolve
                    elena "好吧。你做你认为正确的事。"

                    "第二天一早，你将此事报告给了格雷伯爵。老伯爵听完后捏着眉心想了很久，最终只说了一句话。"

                    hide elena_img
                    $ hide_all_chars("count_grey_img")
                    show count_grey_img at left with dissolve

                    count_grey "年轻人，胆子可以。脑子也得跟上。"

                    hide count_grey_img with dissolve

                    $ change_rel("rel_queen", -15)

            hide elena_img with dissolve

        "悄悄跟踪「暗中观察」":
            $ ch2_exp_night_choice = "follow"
            $ change_stat("intrigue", 10)
            $ change_stat("faith", -2)  ## balance pass 修法 1: 夜间窃探, 信仰受损
            $ log_decision("第二章扩展", "暗中跟踪夜间潜入者")

            $ hide_all_chars()
            "你压低身子，沿着墙壁的阴影悄悄跟了上去。"

            "黑影的动作很专业——每到一个转角都会停下来观察，确认没有人才继续前行。但你更小心。"

            "他推开了档案室的门，闪身而入。你躲在走廊的柱子后面，屏住呼吸。"

            "透过门缝，你看到黑影点燃了一根火折子。在微弱的火光中，你终于看清了他的脸——"

            "不——是她的脸。"

            "那是一个你不认识的女人。年约三十，面容清秀，但眼神锐利如刀。她穿着侍从的制服，但动作绝不像一个普通的侍从。"

            "她在一个柜子前停下来，用一把精致的开锁工具打开了锁。然后从里面取出一份文件，仔细阅读了一遍，又放了回去。"

            "接着，她从怀里掏出一张白纸和炭笔，飞快地抄写着什么。"

            "你注意到她的手腕上有一个纹身——一朵倒置的百合花。"

            "暗百合！"

            "你的心跳骤然加速。暗百合的人居然渗透到了哈伦堡的领主会议中！"

            "女人很快抄完了东西，将纸条塞进衣服内侧。然后她吹灭了火折子，朝门口走来。"

            "你紧紧贴着柱子，连呼吸都停了。"

            "她从你身边不到两步的距离经过。黑暗中你只能看到她的眼睛——冰冷、空洞。"

            "她的脚步声在走廊尽头拐了个弯就没了。你等了整整一盏茶的时间才敢动。"

            $ ch2_exp_spy_identity = "unknown"
            $ change_stat("reputation", 5)

            "你快步走到档案室，用同样的方法打开了那个柜子。里面的文件很多，但你注意到有一份被翻动过的痕迹。"

            "那是一份关于各领地军事力量的详细统计——每个领主有多少兵力、什么装备、驻扎在哪里。"

            "暗百合在收集军事情报。他们在筹划什么？"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "这件事必须告诉其他领主。但……该告诉谁？"

            menu:
                "暗百合在领主会议中安插了间谍。你掌握了关键信息。"

                "告诉格雷伯爵「让最有威望的人来处理」":
                    $ change_rel("rel_grey", 10)
                    $ change_stat("reputation", 5)
                    $ log_decision("第二章扩展", "向格雷伯爵报告暗百合间谍")

                    $ hide_all_chars()
                    "你决定找格雷伯爵。以他的威望和经验，他最有能力处理这件事。"

                    "第二天清晨，你在图书室里找到了老伯爵。他听完你的叙述后，脸色变得很凝重。"

                    $ hide_all_chars("count_grey_img")
                    show count_grey_img at left with dissolve

                    count_grey "暗百合……比老夫想象的还要猖狂。"

                    count_grey "你做得对，告诉了我。这件事老夫会处理。但在那之前——不要告诉任何人。包括你身边的人。"

                    count_grey "因为……暗百合的触手可能比你想的伸得更远。"

                    hide count_grey_img with dissolve

                "暂时保密「留作筹码」":
                    $ change_stat("intrigue", 8)
                    $ log_decision("第二章扩展", "暂时隐瞒暗百合间谍信息")

                    $ hide_all_chars()
                    "你决定暂时不说。在权谋之庭中，信息就是权力。而你现在拥有了一份别人都不知道的信息。"

                    "这份筹码，你要在最关键的时刻打出去。"

                    $ hide_all_chars("player_char_img")
                    show player_char_img at left with dissolve
                    player "再看看吧。暗百合的人既然渗透了哈伦堡，说不定还渗透了其他地方。贸然打草惊蛇，反而可能坏事。"

        "回房休息「不介入此事」":
            $ ch2_exp_night_choice = "ignore"
            $ log_decision("第二章扩展", "选择不介入夜间事件")

            $ hide_all_chars()
            "你犹豫了一下，最终决定不去冒险。"

            "也许那只是一个失眠的侍从。你刚到这里，还没有足够的实力去应对未知的危险。"

            "你转身回了自己的房间，锁好门，但一夜未能安睡。"

            "窗外的月亮被乌云遮住了。黑暗中，你隐约觉得有什么重要的东西正在从指缝间流走。"

    "无论你做了什么选择，这个夜晚都改变了你对这场领主会议的认知。"

    "税制和贸易，只是摆在桌面上的东西。桌面底下，每个人都揣着自己的算计。"

    "包括你。"

    hide player_char_img with dissolve
    ## 夜间阴谋结束，返回主线进行正式会议
    return

## ============================================================
## 第六部分：余波与总结 — Aftermath
## 从 chapter2.rpy 的会后流程调用
## ============================================================

label ch2_exp_aftermath:

    scene bg council_hall with dissolve
    $ play_music("audio/music/dawn.ogg", fadein=2.0)

    "——第二天清晨。闭幕签字。"

    "经过昨日那场漫长的辩论，你回到了同一间议事厅。空气里还残留着昨夜宴会香料酒的淡淡余味，但圆桌上已经换上了崭新的羊皮纸和数支蘸饱墨水的鹅毛笔。"

    "今天没有争吵，也没有试探。所有议题昨日已经辩完，现在只剩最后一步——把共识落在纸上。"

    "昨日席上的几位领主陆续就座，位置与昨日一致。格雷伯爵清了清嗓子，主持了最后的总结。"

    $ hide_all_chars("count_grey_img")
    show count_grey_img at left with dissolve

    count_grey "诸位，经过昨日的讨论，老夫整理了以下几点共识——"

    ## 使用主线的council_outcome变量来决定决议内容
    if council_outcome == "反对":
        count_grey "关于税制——我们将联名上书反对新税法，同时成立联合基金保障各领地的基本收入。"
    elif council_outcome == "支持":
        count_grey "关于税制——各领地将配合王室推行新税法，但要求派遣监察官保障公正执行。"
    elif council_outcome == "折中":
        count_grey "关于税制——有意愿的领地可以先行试点新税率，其余领地保留观望权。"
    else:
        count_grey "关于税制——各领地同意每年就税收问题进行一次协商。"

    count_grey "关于边防——各领地同意加强巡逻，共享边境情报。"

    count_grey "关于贸易——各领地同意降低过境关税，促进商路畅通。"

    count_grey "以上决议，需要三位以上的领主签字方能生效。"

    $ hide_all_chars()
    "一个一个，领主们在羊皮纸上签下了自己的名字。"

    "轮到维尔纳公子时，他犹豫了一下。"

    hide count_grey_img with dissolve
    $ hide_all_chars("noble_werner_img")
    show noble_werner_img at left with dissolve

    if ch2_exp_werner_humiliated:
        noble_werner "这份决议对南方不公平。但——"

        "他看了你一眼，笑了一下——那笑容没到眼睛。"

        noble_werner "我签。但这不代表我认输。"
    else:
        noble_werner "总得有人让步。今天就算我做了一回好人。"

    $ hide_all_chars()
    "五位领主全部签字。决议正式生效。"

    "会议结束后，领主们纷纷告辞。你站在哈伦堡的城门前，目送着一辆辆马车驶离。"

    hide noble_werner_img with dissolve

    "施泰因伯爵夫人临走时握了握你的手。"

    $ hide_all_chars("countess_stein_img")
    show countess_stein_img at left with dissolve

    countess_stein "你是个有潜力的年轻人。下次见面，也许我们可以谈更多。"

    "希尔达伯爵夫人骑着她的战马，在经过你身边时勒住了缰绳。"

    hide countess_stein_img with dissolve
    $ hide_all_chars("countess_hilda_img")
    show countess_hilda_img at left with dissolve
    $ hilda_met = True

    countess_hilda "年轻人，你还有很长的路要走。别松懈。"

    "格雷伯爵最后一个离开。他坐在马车里，掀开帘子看了你一眼。"

    hide countess_hilda_img with dissolve
    $ hide_all_chars("count_grey_img")
    show count_grey_img at left with dissolve

    count_grey "年轻人，临别老夫赠你一句——离百合花远些。别问为什么，记着就好。"

    hide count_grey_img with dissolve

    $ hide_all_chars()
    "马车渐行渐远，消失在蜿蜒的山路上。"

    "你深深地吸了一口气。冬日的空气冷冽清新，但你心中的火焰比任何时候都烧得旺盛。"

    "这场领主会议散了。往后这些领主盘算局势的时候，少不了要把你算进去。"

    ## 结算画面

    ## 属性变化总结
    if ch2_exp_secret_letter:
        "某些秘密文件落入了你的手中。它们将在未来发挥关键作用。"

    if ch2_exp_night_choice == "confront":
        "你在黑夜中正面拦下了潜入者，也因此知道了艾琳娜的秘密。"
    elif ch2_exp_night_choice == "follow":
        "你在暗中发现了惊人的秘密。暗百合的触手已经伸到了领主会议的心脏。"
    elif ch2_exp_night_choice == "ignore":
        "你选择了谨慎。那个走向档案室的黑影是谁，去做了什么，你没能知道。"

    $ change_stat("wealth", 3)
    $ change_stat("reputation", 3)
    $ log_decision("第二章扩展", "领主会议闭幕")

    return

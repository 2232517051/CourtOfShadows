## ============================================================
## 权谋之庭 - Court of Shadows
## 序章深化：被遗忘的记忆
## ============================================================
## 本文件为序章三阶段（童年/少年/青年）各增加深度场景，
## 丰富角色背景、伏笔和世界观。
## 需在主线适当位置 call 这些 label。
## ============================================================

## ────────────────────────────────────────────────────────────
## 新增变量
## ────────────────────────────────────────────────────────────

default deep_mother_herb = ""           # "poison" / "healing" / "question"
default deep_cellar_choice = ""         # "hide" / "reveal" / "flee"
default deep_cellar_heard_lily = False  # 童年期是否听到暗百合线索
default deep_farewell_promise = ""      # "strong" / "wise" / "stay"
default deep_forbidden_book = False     # 是否偷了禁书
default deep_forbidden_choice = ""      # "study" / "report" / "steal"
default deep_street_justice = ""        # "confront" / "shame" / "help"
default deep_marcus_confession = ""     # "forgive" / "distance" / "exploit"
default deep_marcus_truly_loyal = False # 马库斯是否真正忠诚
default deep_tavern_intel = False       # 是否获得酒馆情报
default deep_tavern_choice = ""         # "pay" / "outplay" / "refuse"
default deep_tavern_heard_lily = False  # 青年期是否在赌馆听到暗百合
default deep_night_visitor = ""         # "demand" / "heed" / "dismiss"
default deep_lily_contact_early = False # 是否提前接触暗百合


## ════════════════════════════════════════════════════════════
## 第一部分：童年深化 (3场景)
## ════════════════════════════════════════════════════════════


## ──────────────────────────────────────────────────────────
## 场景1：母亲的花园 (6岁)
## ──────────────────────────────────────────────────────────

label prologue_deep_childhood_1:

    scene bg castle_garden with dissolve

    "你六岁那年的春天，城堡后花园里开满了花。"

    "不是那种贵族夫人们喜欢的玫瑰和百合——母亲的花园里种的都是些奇怪的东西。薄荷、鼠尾草、茴香、还有好些你叫不出名字的植物。"

    "它们有的开着不起眼的小白花，有的叶片上布满了细密的绒毛，在阳光下泛着银色的光。你曾偷偷摘了一片尝，苦得你吐了半天舌头。"

    "母亲笑你笨。"

    $ hide_all_chars("mother_img")
    show mother_img at left with dissolve

    mother "傻孩子，不是什么东西都能往嘴里放的。"

    "她蹲下身，指着一丛低矮的紫色植物。叶片像针一样细，散发着刺鼻的气味。"

    mother "看这个。迷迭香。泡在热水里可以治头痛，但如果用量太大，会让人昏昏欲睡，三天三夜醒不过来。"

    "你歪着头看她。六岁的你觉得母亲说的话像故事一样有趣。"

    mother "还有这个——"

    "她走到花园角落，那里长着一棵你从没注意过的植物。它的花是深蓝色的，像夜空一样，花瓣上有隐约的紫色纹路。"

    mother "狼毒草。美不美？"

    "你点头。确实很美。"

    mother "碰它不要紧。但如果把它的根磨成粉，放进酒里……"

    $ hide_all_chars()
    "她没有说完。她看着那朵花，眼神忽然变得很远，好像在看某个你看不到的地方。"

    "很久之后你才明白那种眼神叫什么。叫恐惧。"

    "母亲忽然开口讲了一个故事。"

    $ hide_all_chars("mother_img")
    show mother_img at left with dissolve
    mother "很久以前，有一位王后。她不是最美的，也不是最聪明的，但她是最懂花的。"

    mother "她的花园比王宫还大。每一种花她都叫得出名字，知道它的脾性。哪些能治病，哪些能杀人。"

    mother "后来国王有了新宠。新宠年轻漂亮，会唱歌会跳舞，但她不懂花。"

    mother "王后送了新宠一盆花。白色的小花，开得很素净。新宠把花放在寝宫里，每天闻着花香入睡。"

    "你屏住呼吸。"

    mother "一个月后，新宠开始头痛。两个月后，她起不了床。三个月后……"

    "母亲停顿了一下。"

    mother "三个月后，所有人都说新宠是病死的。只有王后知道真相。"

    $ hide_all_chars()
    "你听得入迷了。六岁的孩子分不清故事和现实，也分不清善恶。你只觉得那个王后很厉害。"

    "然后你问了一个问题。"

    menu:
        "追问毒药的事。":
            $ change_stat("intrigue", 3)
            $ deep_mother_herb = "poison"
            $ log_decision("序章深化", "询问毒药", "谋略+3")

            hide mother_img
            $ hide_all_chars("player_child_img")
            show player_child_img at left with dissolve
            player "母亲，那个白色的花叫什么名字？"

            "母亲愣了一下。然后她笑了——像是想笑又忍住了——或者根本不是笑。"

            hide player_child_img
            $ hide_all_chars("mother_img")
            show mother_img at left with dissolve
            mother "你为什么想知道？"

            hide mother_img
            $ hide_all_chars("player_child_img")
            show player_child_img at left with dissolve
            player "我想知道。万一有坏人来，我可以保护你。"

            "母亲蹲下来，把你抱进怀里。她的身上有药草的味道，混着泥土的气息。"

            hide player_child_img
            $ hide_all_chars("mother_img")
            show mother_img at left with dissolve
            mother "那种花叫铃兰。记住它。记住它的样子。"

            "她把一小束铃兰放在你手心里。"

            mother "但你永远不要用它。除非……"

            $ hide_all_chars()
            "她又没有说完。你后来想了很多年，那个「除非」后面是什么。"

            "你始终没有得到答案。因为母亲第二年就死了。"

        "问母亲关于治病的草药。":
            $ change_stat("faith", 3)
            $ deep_mother_herb = "healing"
            $ log_decision("序章深化", "询问草药治病", "信仰+3")

            hide mother_img
            $ hide_all_chars("player_child_img")
            show player_child_img at left with dissolve
            player "母亲，那些能治病的花呢？你能教我吗？"

            "母亲的表情柔和了下来。她握着你的小手，带你走到花园的另一边。"

            hide player_child_img
            $ hide_all_chars("mother_img")
            show mother_img at left with dissolve
            mother "这是金盏菊。把花瓣泡水，可以退烧。这是白芷，嚼碎了敷在伤口上能止血。"

            "她一种一种地教你。你记不住那么多名字，但你记住了母亲弯腰采花时的样子——头发垂下来，遮住半边脸，像画里的圣母。"

            mother "治病比害人难得多。毒只需要一种，但救人需要许多种药配在一起。"

            "她摸了摸你的头。"

            mother "如果你以后想帮助别人，就要学会耐心。一株草药从种子到能入药，至少要三年。"

            $ hide_all_chars()
            "三年。对于六岁的你来说，三年就是半辈子了。"

            "但你认真地点了点头。母亲笑了。"

            "这是你记忆中母亲最后一次笑得那么开心。"

        "问母亲为什么要告诉你这些。":
            $ change_stat("faith", 2)
            $ change_stat("faith", 1)
            $ deep_mother_herb = "question"
            $ log_decision("序章深化", "追问缘由", "谋略+2 信仰+1")

            hide mother_img
            $ hide_all_chars("player_child_img")
            show player_child_img at left with dissolve
            player "母亲，你为什么要跟我说这些？"

            $ hide_all_chars()
            "母亲的手停在半空中。她看着你，像是在衡量什么。"

            "六岁的孩子问出了大人才会问的问题。"

            hide player_child_img
            $ hide_all_chars("mother_img")
            show mother_img at left with dissolve
            mother "因为……"

            "她犹豫了一下。"

            mother "因为总有一天你会需要知道这些。"

            hide mother_img
            $ hide_all_chars("player_child_img")
            show player_child_img at left with dissolve
            player "什么时候？"

            hide player_child_img
            $ hide_all_chars("mother_img")
            show mother_img at left with dissolve
            mother "我不知道。但那一天会来的。到时候，你要记住母亲今天教你的每一句话。"

            "她的语气忽然变得严肃，不像在跟一个孩子说话。你被吓到了，但没有哭。"

            mother "记住——这个世界上，能保护你的人只有你自己。花可以治人，也可以杀人。知道区别的人，才能活下去。"

            $ hide_all_chars()
            "你似懂非懂地点了头。很多年以后，当你在宫廷的黑暗中周旋时，你才真正听懂了母亲的话。"

            "她不是在教你种花。她是在教你求生。"

    scene bg castle_garden with dissolve

    "那天下午，母亲教了你如何辨认花园里的每一种植物。"

    "你虽然记不住所有的名字，但你记住了一件事——美丽的东西往往最危险。"

    "以及——母亲远比你以为的更不简单。"

    "一年后，母亲去世了。花园渐渐荒芜，杂草吞没了那些叫不出名字的药草。"

    "但你始终记得那棵狼毒草的位置。深蓝色的花，像夜空一样。"

    return


## ──────────────────────────────────────────────────────────
## 场景2：地窖里的声音 (7岁)
## ──────────────────────────────────────────────────────────

label prologue_deep_childhood_2:

    scene bg castle_interior with dissolve

    "那一年你七岁。母亲刚走不久。"

    "父亲变了。他不再像以前那样偶尔和你下棋，也不再在晚饭时跟你讲边关的故事。他总是把自己关在书房里，有时候半夜还能看到书房的灯火。"

    "女仆玛尔塔说父亲只是太忙了。但你觉得不是。你觉得他在害怕什么。"

    "一个深夜。你被噩梦惊醒——又是那个梦，母亲站在花园里叫你，你跑过去，她却越来越远。"

    "你睁开眼。城堡安静得只剩下风声。"

    "然后你听到了什么。"

    "脚步声。从走廊尽头传来，很轻，但在这样的深夜格外清晰。不是卫兵巡逻——卫兵的脚步是沉重的、有节奏的。这个人走路像猫。"

    "你从床上坐起来，悄悄推开门缝往外看。"

    "走廊里只有一盏残灯。你看到一个黑色的影子闪过拐角，往地窖的方向去了。"

    "七岁的孩子应该害怕。但那段时间你做了太多噩梦，现实反而显得没那么可怕。"

    "你赤着脚，跟了上去。"

    scene bg cellar with dissolve

    "地窖的门虚掩着。里面有光——不是烛光，是那种发黄的、摇摇晃晃的油灯光。"

    "你蹲在门外，把耳朵贴上去。"

    "父亲的声音。还有另一个人——你不认识。那个声音沙哑而低沉，像砂纸擦过铁器。"

    "父亲说——"

    "「百合」的事，再也不能拖了。"

    "那个陌生人回答——"

    "「誓约还在。只是代价越来越高。」"

    "父亲的声音听起来很疲惫。"

    "「我知道。但如果她查到……一切都完了。」"

    "「那就在她查到之前解决。金鹰的后裔不应该向任何人低头。」"

    "你的心跳得很快。你不完全明白他们在说什么，但你知道这是一件很严重的事。「百合」是什么？'她「又是谁？」誓约'又是什么意思？"

    "这时候你犯了一个错误——你往前探了一下身子，膝盖碰到了墙边的一只空桶。"

    "当啷一声。"

    "地窖里的对话戛然而止。"

    menu:
        "屏住呼吸，继续躲着偷听。":
            $ change_stat("intrigue", 4)
            $ deep_cellar_choice = "hide"
            $ deep_cellar_heard_lily = True
            $ log_decision("序章深化", "躲藏偷听", "谋略+4")

            "你几乎停止了呼吸。身体压得更低，缩在一只大酒桶的后面。"

            "地窖里传来脚步声。门被推开了一条更大的缝——你能看到一双黑色的靴子，靴筒上有银色的刺绣，花纹很复杂。"

            "那个人站在门口看了一会儿。你一动不动，连眼睛都不敢眨。"

            "然后他回去了。"

            "「是老鼠。这地窖几十年了，什么都有。」"

            "父亲的声音又响起来：「回到正题。百合花开的时候，东线必须稳住。如果……」"

            "他压低了声音，你只断断续续听到了几个词——「暗百合」、「使者」、「旧血脉」。"

            "你不懂。但你像一块海绵一样，把每一个词都吸了进去。"

            "他们又说了大约一炷香的时间。最后那个陌生人起身告辞。你听到他说了一句：「金鹰不死。百合不凋。」"

            "父亲回答：「但冬天总会来。」"

            "然后是开门声、脚步声、沉默。"

            "你在酒桶后面又蹲了很久，直到确认没有人了才溜回自己的房间。"

            "那一夜你没有再做噩梦。因为你根本就没敢睡。"

            "你把听到的那几个词反复在脑子里念——暗百合，使者，旧血脉。"

            "它们像种子一样，埋在了你七岁的记忆里。"

        "走出来面对父亲。":
            $ change_stat("power", 2)
            $ change_stat("loyalty", 2)
            $ deep_cellar_choice = "reveal"
            $ log_decision("序章深化", "现身面对", "权力+2 忠诚+2")

            "你从暗处走了出来。"

            "地窖的门被彻底推开。你看到了父亲——他坐在一张简陋的木桌旁，面前放着一盏油灯和几份文书。桌子对面的凳子上还有一个人坐过的痕迹，但那个人已经消失了。"

            "就好像从来不存在一样。"

            "父亲看到你的时候，脸上的表情经历了一次复杂的变化——先是惊讶，然后是怒气，最后变成了一种你说不清的东西。"

            $ hide_all_chars("father_img")
            show father_img at left with dissolve
            father "你怎么在这里？"

            "他的声音很冷。你缩了缩肩膀，但没有后退。"

            hide father_img
            $ hide_all_chars("player_child_img")
            show player_child_img at left with dissolve
            player "我……我做噩梦了。然后听到声音……"

            hide player_child_img
            $ hide_all_chars("father_img")
            show father_img at left with dissolve
            father "你听到了什么？"

            hide father_img
            $ hide_all_chars("player_child_img")
            show player_child_img at left with dissolve
            player "有人说百合。还有什么……誓约。"

            "油灯的火苗在父亲脸上投下阴影，让他看起来老了十岁。"

            hide player_child_img
            $ hide_all_chars("father_img")
            show father_img at left with dissolve
            father "过来。"

            "你走到他身边。他把你抱到膝盖上——这是母亲走后他第一次这样做。你能闻到他身上的酒味，还有墨水的气味。"

            father "听着，[player_name]。你今晚看到的、听到的，一个字都不能跟别人说。明白吗？"

            hide father_img
            $ hide_all_chars("player_child_img")
            show player_child_img at left with dissolve
            player "为什么？"

            hide player_child_img
            $ hide_all_chars("father_img")
            show father_img at left with dissolve
            father "因为这是大人的事。"

            "你想说你不是小孩子了。但你只有七岁。你确实是个小孩子。"

            father "总有一天我会告诉你一切。但不是现在。现在你需要做的只有一件事——"

            "他看着你的眼睛。"

            father "变强。足够强，强到能保护自己和这座城堡。懂吗？"

            $ hide_all_chars()
            "你点了点头。你不完全懂。但你记住了。"

            "父亲把你抱回了房间。那是他最后一次抱你。"

        "害怕，赶紧跑回房间。":
            $ change_stat("intrigue", -1)
            $ change_courage(-3)
            $ deep_cellar_choice = "flee"
            $ log_decision("序章深化", "恐惧逃跑", "谋略-1 勇气-3")

            "恐惧像一盆冷水浇下来。"

            "你转身就跑。赤脚踩在冰冷的石板上，噼啪作响。你不知道身后有没有人追你——你不敢回头看。"

            "你跑回自己的房间，把门关上，把被子拉过头顶。你的心跳得快要从嗓子眼里蹦出来。"

            "你听到走廊里有脚步声经过你的门口。它停了一下。然后继续走了。"

            "你不知道那是父亲还是那个陌生人。你闭上眼睛，把头埋得更深。"

            "第二天早上，一切像什么都没发生过一样。父亲坐在餐厅里喝茶，玛尔塔在忙早饭。没有人提起昨晚的事。"

            "你偷偷去看了一眼地窖。门锁着。从外面看，什么都没有。"

            "你几乎以为那只是一场梦。但你知道不是。因为你的脚底板上还沾着地窖的灰尘。"

            "那些词——百合、誓约——像影子一样跟着你。你试着忘掉它们，但做不到。"

            "它们会在你的记忆里沉睡很多年。直到有一天，你在父亲的遗物中发现一枚刻着百合花的戒指。"

    scene black with dissolve
    pause 0.3

    "关于那个深夜，关于地窖里的对话，你从来没有跟任何人提起过。"

    "这是你人生中学会保守的第一个秘密。"

    return


## ──────────────────────────────────────────────────────────
## 场景3：第一次告别 (8岁)
## ──────────────────────────────────────────────────────────

label prologue_deep_childhood_3:

    scene bg castle_exterior with dissolve

    "你八岁。初秋。枫叶红得像火。"

    "城堡的大门口停着一辆马车，车上装满了行李和武器。几匹战马在旁边打着响鼻，马蹄不安地刨着地面。"

    "一队士兵在做出发前的最后检查。他们穿着半旧的铠甲，表情严肃。空气中弥漫着马粪和铁锈的味道。"

    "你认识他们中的大多数人。他们是城堡的驻守军。但今天，他们要去很远的地方。"

    "北境告急。蛮族入侵。国王征召各地领主出兵支援。父亲派出了自己最好的一队骑兵，由他最信任的老战友——伯特兰爵士——率领。"

    $ hide_all_chars("bertrand_img")
    show bertrand_img at left with dissolve

    $ hide_all_chars()
    "伯特兰爵士已经五十多岁了。他的头发全白了，脸上有一道从额头到下巴的旧伤疤，据说是年轻时和一头熊搏斗留下的。他走路时右腿微微跛着——那是十年前的一场战役留下的纪念品。"

    "但他的眼睛还是亮的。像两把磨了多年的旧刀，刀刃虽然卷了，杀气还在。"

    "你从记事起就认识他。他教你骑第一匹马——其实是一头温顺的老驴。他教你用木剑——打你手心的时候毫不留情。他给你讲战场上的故事——从来不美化，从来不省略那些血腥的部分。"

    "「战争不是骑士小说，」他总是说。「战争是泥巴、屎尿和断掉的骨头。」"

    "现在他要走了。"

    "你站在大门口，看着他检查马鞍上的束带。他注意到了你，朝你招了招手。"

    $ hide_all_chars("bertrand_img")
    show bertrand_img at left with dissolve
    bertrand "过来，小家伙。"

    "你走过去。他蹲下来——膝盖发出咔嚓的响声——和你平视。"

    bertrand "我要走了。不知道什么时候回来。也许几个月，也许……"

    $ hide_all_chars()
    "他没有说下去。但你已经够大了，大到能听懂那些没说出口的话。"

    "他从腰间解下一把东西。是一把木剑——不是练习用的那种粗糙货色，而是一把真正用心雕刻的木剑。剑柄上刻着一只展翅的鹰——艾登堡家族的纹章。"

    $ hide_all_chars("bertrand_img")
    show bertrand_img at left with dissolve
    bertrand "这把剑跟了我三十年。当年你父亲亲手刻的。"

    "他把剑递给你。木头温热，带着掌心的温度。"

    bertrand "拿着它。替我守好这座城堡。"

    "你接过木剑。它对于八岁的你来说有点重，但你双手握紧，不让它掉下来。"

    hide bertrand_img with dissolve

    $ hide_all_chars()
    menu:
        "\"我会变强的。等你回来，我要跟你比剑。\"":
            $ change_stat("power", 3)
            $ change_courage(3)
            $ deep_farewell_promise = "strong"
            $ log_decision("序章深化", "承诺变强", "权力+3 勇气+3")

            "伯特兰爵士看着你，忽然笑了。那张布满皱纹和伤疤的脸因为笑容变得温和了一瞬间。"

            $ hide_all_chars("bertrand_img")
            show bertrand_img at left with dissolve
            bertrand "好小子。但我得警告你——我年纪虽然大了，剑术可没退步。你要是赢不了我，可别哭鼻子。"

            hide bertrand_img
            $ hide_all_chars("player_child_img")
            show player_child_img at left with dissolve
            player "我才不会哭！"

            hide player_child_img
            $ hide_all_chars("bertrand_img")
            show bertrand_img at left with dissolve
            bertrand "嗯。像你爹。你爹八岁的时候也这么说。后来我把他打哭了。"

            "你咬着嘴唇。你暗暗发誓，你绝对不会被打哭。"

            hide bertrand_img with dissolve

            $ hide_all_chars()
            "伯特兰爵士翻身上马。他对你行了一个标准的骑士礼——右手握拳放在胸口。那是只有对等之人之间才会行的礼。"

            "他把你当作一个战士了。"

            "你学着他的样子，握紧木剑，放在胸口。"

            "他笑了笑，拉紧缰绳，没有回头。马队缓缓开出城门，消失在枫叶如火的林道尽头。"

        "\"我会变聪明的。用智慧守护这里。\"":
            $ change_stat("reputation", 3)
            $ deep_farewell_promise = "wise"
            $ log_decision("序章深化", "承诺变聪明", "谋略+3")

            hide player_child_img
            $ hide_all_chars("bertrand_img")
            show bertrand_img at left with dissolve

            "伯特兰爵士挑了挑眉。然后他伸出粗糙的大手，拍了拍你的脑袋。"

            $ hide_all_chars("bertrand_img")
            show bertrand_img at left with dissolve
            bertrand "聪明。这个答案比你爹小时候的好。他那时候说的是「我要把他们全砍了」。"

            "他的目光变得认真。"

            bertrand "记住，小家伙。剑只能杀一个人，但脑子能救一千个人。"

            bertrand "不过——"

            "他拍了拍腰间的长剑。"

            bertrand "也别忘了练剑。聪明人手里没有剑，跟傻瓜没什么区别。"

            hide bertrand_img with dissolve

            $ hide_all_chars()
            "他翻身上马。在城门口停了一下，回过头对你说了最后一句话："

            "「照顾好你父亲。他比你想象的更需要你。」"

            "你点了点头。你不确定自己能做到，但你会试。"

            "马队渐渐远去。蹄声像雷鸣一样在石板路上回荡，然后越来越远，越来越轻，最后被风声淹没。"

        "眼眶发红，恳求他不要走。":
            $ change_stat("loyalty", 3)
            $ change_courage(-1)
            $ deep_farewell_promise = "stay"
            $ log_decision("序章深化", "恳求留下", "忠诚+3 勇气-1")

            "你的眼眶一下子就红了。"

            hide bertrand_img
            $ hide_all_chars("player_child_img")
            show player_child_img at left with dissolve
            player "你能不能不走……"

            "你的声音在发抖。你知道这很丢人——一个领主的儿子不应该哭。但你已经失去了母亲。你不想再失去任何人。"

            hide player_child_img
            $ hide_all_chars("bertrand_img")
            show bertrand_img at left with dissolve

            $ hide_all_chars()
            "伯特兰爵士看着你。他的表情没有变，但他的眼睛里有什么东西动了一下。"

            "他再次蹲下来，这次膝盖发出了更大的响声。他把你拉进怀里，铠甲硌得你肩膀生疼，但你不在乎。"

            $ hide_all_chars("bertrand_img")
            show bertrand_img at left with dissolve
            bertrand "嘿。听着。"

            "他的声音变得很轻，像是在哄一个比你更小的孩子。"

            bertrand "我这辈子上过很多次战场。每一次走的时候，都有人说「别去了」。你知道我为什么每次都活着回来了吗？"

            "你摇头。"

            bertrand "因为有人在等我。有人等你回来，你就不会死在外面。"

            "他把你松开，看着你的眼睛。"

            bertrand "所以，你就在这里等我。好不好？"

            hide bertrand_img with dissolve

            $ hide_all_chars()
            "你擦了擦眼睛，使劲点头。"

            "你看着他上马。他在马背上回头看了一眼。你觉得他的眼眶好像也有点红——但也许是阳光的错觉。"

            "马队走了。你站在城门口，一直站到太阳落山。"

    scene bg castle_exterior with dissolve

    "城堡空了很多。安静了很多。你每天拿着那把木剑在庭院里比划。有时候你跟影子打，有时候你跟空气打。"

    "你等伯特兰爵士回来。"

    "入冬后，第一场雪落下的那天，一匹没有骑手的马回到了城堡。马鞍上插着一根断箭，旗帜已经看不出颜色。"

    "北境的战事远比任何人预料的都惨烈。伯特兰爵士和他带去的大部分士兵都没有回来。"

    "父亲在书房里关了三天。出来的时候什么都没说。"

    "你把那把木剑挂在了自己房间的墙上。剑柄上的鹰还在展翅。"

    "你对着它发了一个八岁孩子所能发的最郑重的誓——"

    "你不会让任何人再白白牺牲。"

    return


## ════════════════════════════════════════════════════════════
## 第二部分：少年深化 (3场景)
## ════════════════════════════════════════════════════════════


## ──────────────────────────────────────────────────────────
## 场景4：修道院的禁书 (13岁)
## ──────────────────────────────────────────────────────────

label prologue_deep_youth_1:

    scene bg church_interior with dissolve

    "圣·尤里安修道院的图书馆号称拥有全王国最多的藏书。七千册手抄本和卷轴，从神学到天文，从历史到数学，整整占了三层楼。"

    "你十三岁。已经在修道院待了一年。你习惯了早祷、课业、晚祷的规律生活，也习惯了图书馆里那股混合着霉味和墨水味的独特气息。"

    "那天是个雨天。午课被取消了——修士卢卡说他头疼，让你们自行温习。"

    "你本来打算去练剑。但雨太大了，练武场变成了一片泥塘。"

    "于是你去了图书馆。"

    "图书馆三楼很少有人来。那里主要是一些古旧的手稿和已经过时的教会法典——对大多数学生来说毫无用处。但你偶尔喜欢翻翻那些泛黄的羊皮纸，看看几百年前的人是怎么思考的。"

    "你在一排书架的最深处发现了一面墙。不对——是一扇门，被书架挡住了大半。门上没有锁，但积了厚厚一层灰，显然很久没人开过。"

    "你犹豫了一下。然后好奇心战胜了一切。"

    "你推开了那扇门。"

    "门后是一个小房间，大概只有你寝室的一半大。一扇高窗透进灰蒙蒙的光。房间中央有一张书桌，桌上放着一只铁烛台。四面墙全是书架，塞满了书。"

    "这些书和外面的不一样。"

    "它们的封面是深色的皮革，没有标题。翻开来看，字迹潦草而急促，像是在赶时间写的。有些页面上有插图——不是圣像，而是一些复杂的图表和符号。"

    "你随手拿起一本。《论君主之术》——一个你没听过的名字写的。你翻了几页，看到了这样一段话：「一个君主宁可被人畏惧，也不要被人爱戴。因为恐惧的链条比爱的丝线更不容易断裂。」"

    "又拿起一本。《权力的七张面孔》。「所有的权力都是一种幻觉。但幻觉如果被足够多的人相信，它就变成了现实。」"

    "还有一本更薄的——像是某人的笔记。上面写着：「如果你想操纵一个人，就找到他最害怕的东西。恐惧是最好的缰绳。」"

    "你的心跳加速了。你知道这些书是被禁止的——教会不允许传播这种「邪恶」的思想。但你的眼睛像被粘在纸上一样，移不开。"

    "你正沉浸其中的时候，身后传来一个熟悉的声音。"

    $ hide_all_chars("friend_marcus_img")
    show friend_marcus_img at left with dissolve

    friend_marcus "我就猜你在这种地方。下雨天不练剑就往图书馆钻，你可真够无聊的。"

    "马库斯靠在门框上，怀里抱着一个苹果。他咬了一口，探头看你手里的书。"

    friend_marcus "什么东西？"

    "他凑过来看了一眼，脸色变了。"

    friend_marcus "你疯了？这些是禁书！要是被修士卢卡发现——不对，要是被院长发现，你就等着被开除吧！"

    "他压低了声音，但紧张是掩不住的。"

    friend_marcus "甚至不只是开除。我听说上一个偷看禁书的学生，被关了三个月的禁闭。出来的时候瘦了二十斤，眼睛都直了。"

    "你看着手里的书。这些文字比修道院教的任何东西都令你兴奋。它们像是打开了一扇窗，让你看到了世界的另一面——不是圣光照耀的那一面，而是阴影覆盖的那一面。"

    menu:
        "留下来，仔细研读这些禁书。":
            $ change_stat("intrigue", 5)
            $ deep_forbidden_choice = "study"
            $ log_decision("序章深化", "研读禁书", "谋略+8")

            "你看了马库斯一眼。"

            hide friend_marcus_img
            $ hide_all_chars("player_teen_img")
            show player_teen_img at left with dissolve
            player "你先出去。帮我看着门。"

            hide player_teen_img
            $ hide_all_chars("friend_marcus_img")
            show friend_marcus_img at left with dissolve
            friend_marcus "你——"

            hide friend_marcus_img
            $ hide_all_chars("player_teen_img")
            show player_teen_img at left with dissolve
            player "马库斯。你信得过我吗？"

            "他张了张嘴，又闭上了。最后他叹了口气。"

            hide player_teen_img
            $ hide_all_chars("friend_marcus_img")
            show friend_marcus_img at left

            friend_marcus "你这人……行吧。但你只有一个时辰。超过了我就进来把你拖出去。"

            hide friend_marcus_img with dissolve

            $ hide_all_chars()
            "他走了。你听到他在门外来回踱步的声音，然后渐渐安静下来——他大概找了个地方坐下了。"

            "你在那个密室里待了整整一个时辰。你翻阅了每一本书的目录，选了几本最有意义的仔细读。"

            "《论君主之术》教你如何在敌人环伺的朝廷中生存。《权力的七张面孔》分析了历史上每一种权力结构的优劣。那本薄薄的笔记——你后来猜测可能是某位已故院长的私人手记——则记录了无数阴谋的范例。"

            "你读得入了迷。直到马库斯敲门把你叫出来。"

            "回去的路上你没说话。你的脑子里塞满了新的想法。它们像火花一样跳跃、碰撞。"

            "你看世界的方式永远改变了。"

            "从那天起，你每隔几天就会偷偷溜进那个密室。一整个秋天，你把里面的书读了个遍。"

            "没有人发现。你很小心。而且你学到的第一课就是——如何不被发现。"

        "向院长报告这个发现。":
            $ change_stat("faith", 8)
            $ deep_forbidden_choice = "report"
            $ log_decision("序章深化", "报告院长", "信仰+8")

            "你放下了手里的书。"

            hide friend_marcus_img
            $ hide_all_chars("player_teen_img")
            show player_teen_img at left with dissolve
            player "你说得对。这些东西不该在这里。"

            hide player_teen_img with dissolve
            $ hide_all_chars("friend_marcus_img")
            show friend_marcus_img at left with dissolve

            friend_marcus "那我们……"

            hide friend_marcus_img
            $ hide_all_chars("player_teen_img")
            show player_teen_img at left with dissolve
            player "去找院长。"

            "马库斯明显松了口气。"

            hide friend_marcus_img with dissolve

            $ hide_all_chars()
            "你们找到了院长。他是个年过七旬的老修士，头发白得像雪，但眼睛锐利如鹰。"

            "他听完你们的报告后，缓缓摘下了眼镜。"

            "「你翻开看了吗？」"

            "你犹豫了一下。你可以说谎。但你选择了诚实。"

            $ hide_all_chars("player_teen_img")
            show player_teen_img at left with dissolve
            player "看了几页。但我觉得不对，就来告诉您了。"

            $ hide_all_chars()
            "院长点了点头。他看了你很长时间，那种目光像是在透过你的皮肤看你的灵魂。"

            "「大多数人发现禁书的第一反应是偷偷读完。你却选择了来报告。这需要比读书更大的勇气。」"

            "他站起来，慢慢走到你面前。"

            "「孩子，知识本身没有善恶。但使用知识的方式有。你做了正确的选择。」"

            "后来你听说，密室里的书被全部搬走了。有人说是烧掉了，有人说是转移到了更隐秘的地方。"

            "你没有后悔。但偶尔在深夜，你会想起那段话——「宁可被人畏惧，也不要被人爱戴。」——然后翻一个身，把它埋进枕头下面。"

        "偷偷带走一本最薄的。":
            $ change_stat("intrigue", 5)
            $ deep_forbidden_book = True
            $ deep_forbidden_choice = "steal"
            $ log_decision("序章深化", "偷书", "谋略+5 获得禁书")

            "你看了看四周。然后你做了一个决定。"

            "你把那本最薄的笔记——某位前任院长的私人手记——塞进了袍子里面。"

            $ hide_all_chars("friend_marcus_img")
            show friend_marcus_img at left with dissolve

            friend_marcus "你在干什么？！"

            hide friend_marcus_img
            $ hide_all_chars("player_teen_img")
            show player_teen_img at left with dissolve
            player "安静。"

            "你拉上袍子，拍了拍平整。从外面看完全看不出来。"

            player "我只拿这一本。其余的不碰。"

            hide player_teen_img
            $ hide_all_chars("friend_marcus_img")
            show friend_marcus_img at left with dissolve
            friend_marcus "你疯了。万一——"

            hide friend_marcus_img
            $ hide_all_chars("player_teen_img")
            show player_teen_img at left with dissolve
            player "不会有万一。这间密室积了这么厚的灰，说明很久没有人来过。少一本薄笔记，没人会注意到。"

            hide friend_marcus_img with dissolve

            $ hide_all_chars()
            "马库斯看你的眼神像在看一个陌生人。但他没有再说什么。"

            "那本笔记你藏在寝室床板底下的一个暗格里。接下来的几个月，你在深夜借着烛光一页一页地读。"

            "笔记的主人没有留名。但从内容来看，他是一个深谙权术的人。他记录了数十个宫廷阴谋的案例——有些成功了，有些失败了——并附上了自己的分析。"

            "其中有一段话你读了很多遍：「最好的阴谋家不是那个不被发现的人，而是那个即使被发现也没人敢追究的人。」"

            "这本笔记成了你少年时代最珍贵的教科书。它教会你的东西，比修道院的所有课程加起来还多。"

            "当然，代价是你有了一个永远不能对人说的秘密。"

            "但你已经习惯了。秘密是你最熟悉的东西。"

    scene black with dissolve
    pause 0.3

    "无论你做了什么选择，修道院的日子继续流淌。"

    "但那扇密室的门在你心中留下了一道印记。你开始意识到——这个世界上存在着两套规则。一套是光明正大的，人人都能看到；另一套藏在阴影里，只有少数人知晓。"

    "而你，已经窥见了阴影。"

    return


## ──────────────────────────────────────────────────────────
## 场景5：街头的正义 (14岁)
## ──────────────────────────────────────────────────────────

label prologue_deep_youth_2:

    scene bg town_market with dissolve

    "修道院每月有两天假期，学生们可以进城。大多数人去酒馆、去市集、去看杂耍。你通常和马库斯一起——他总是拉着你去看新上架的武器。"

    "那天的王都阳光明媚。街道上挤满了人。小贩们扯着嗓子叫卖，铁匠铺传来叮叮当当的敲打声，空气中弥漫着烤面包和马粪混合的气味。"

    "你和马库斯刚从一个武器铺出来——他花掉了半个月的零花钱买了一把匕首鞘——正往市集的方向走。"

    "然后你听到了哭声。"

    "在一条小巷的入口，一个衣衫褴褛的男孩蜷缩在地上。他大概十岁左右，瘦得像一根柴火棍，脸上有血——鼻子被打破了。"

    "站在他面前的是一个穿着锦缎外套的少年，身后跟着两个随从。你认识那件外套上的纹章——莱茵哈特伯爵家的。"

    "那个少年正笑着，一脚踢在男孩的肋骨上。"

    "「叫你挡路。平民的贱种也敢走在大路中间？」"

    "旁边有人在看，但没有人上前。平民不敢得罪贵族。贵族不愿多管闲事。"

    "男孩已经不哭了。他咬着嘴唇，眼睛里的光正在一点点熄灭。"

    $ hide_all_chars("friend_marcus_img")
    show friend_marcus_img at left with dissolve

    friend_marcus "那个是……莱茵哈特家的小儿子？叫什么来着。反正是个出了名的恶霸。"

    "马库斯压低了声音。"

    friend_marcus "别惹他。他爹是伯爵，咱们得罪不起。"

    hide friend_marcus_img with dissolve

    $ hide_all_chars()
    "你看着那个男孩。你想起了八岁时的自己——也是那样无助，那样孤独。"

    "你的手不自觉地攥紧了。"

    menu:
        "直接走过去，挡在男孩面前。":
            $ change_stat("power", 4)
            $ change_stat("reputation", 3)
            $ change_courage(4)
            $ deep_street_justice = "confront"
            $ log_decision("序章深化", "正面对峙", "权力+4 声望+3 勇气+4")

            "你没有犹豫。"

            "你走过去，站在那个男孩和伯爵小儿子之间。你比他高半个头。你的眼睛直视着他的。"

            $ hide_all_chars("player_teen_img")
            show player_teen_img at left with dissolve
            player "够了。"

            $ hide_all_chars()
            "伯爵的小儿子愣了一下。他上下打量你，目光落在你长袍上的修道院徽章上。"

            "「你哪儿来的修士？滚开，少管闲事。」"

            $ hide_all_chars("player_teen_img")
            show player_teen_img at left with dissolve
            player "我不是修士。我是艾登堡领主之子[player_name]。"

            $ hide_all_chars()
            "你报出了自己的名号。不是因为虚荣，而是因为你知道在这个世界上，一个名字有时候比一把剑更有用。"

            "效果是立竿见影的。伯爵小儿子的表情变了——他听过艾登堡。北方最大的领地之一。"

            "「……哼。不过是个乡下领主的崽子。」"

            "他嘴上硬，但脚步已经往后退了半步。他身后的两个随从互相看了一眼，明显不想惹麻烦。"

            $ hide_all_chars("player_teen_img")
            show player_teen_img at left with dissolve
            player "我再说一次。够了。"

            $ hide_all_chars()
            "你们对视着。街上的人都在看。"

            "最后，伯爵小儿子啐了一口，带着随从走了。临走时丢下一句：「你等着。我爹不会放过你的。」"

            "你没有理他。你蹲下来，看了看那个男孩的伤。鼻子破了，肋骨可能有淤伤，但没有大碍。"

            "你从袍子里掏出一块手帕递给他。他怯生生地接过去，一句话都没说。"

            "那天你多了一个对头——莱茵哈特家记住了你的名字。但你也在王都的平民中赢得了第一批尊重。"

            "有时候，正确的事情恰恰是最危险的事情。"

        "不动手，用言语让那个恶霸丢脸。":
            $ change_stat("reputation", 4)
            $ change_stat("reputation", 3)
            $ deep_street_justice = "shame"
            $ log_decision("序章深化", "言语羞辱", "谋略+4 声望+3")

            "你没有冲上去。你走过去，但保持着一种不远不近的距离。然后你开口了。"

            "你没有对伯爵小儿子说话。你对围观的人说。"

            $ hide_all_chars("player_teen_img")
            show player_teen_img at left with dissolve
            player "各位，快来看啊。莱茵哈特伯爵的公子，堂堂贵族之后，在光天化日之下殴打一个十岁的孩子。真是威风凛凛，令人钦佩。"

            $ hide_all_chars()
            "你的声音不大，但在安静的巷口格外清晰。围观的人开始窃窃私语。"

            "伯爵的小儿子涨红了脸。"

            "「你——你算什么东西？！」"

            $ hide_all_chars("player_teen_img")
            show player_teen_img at left with dissolve
            player "我是圣·尤里安修道院的学生。我叫[player_name]。我可以作证，我亲眼看到您对一个手无缚鸡之力的孩子拳脚相加。"

            "你顿了一下。"

            player "不知道伯爵阁下知道了这件事，会不会觉得脸上有光呢？"

            $ hide_all_chars()
            "这句话像一根针扎进了气球。伯爵小儿子的脸从红变白。他比任何人都清楚，他父亲最在意的就是家族名声。"

            "「你——你敢威胁我？！」"

            $ hide_all_chars("player_teen_img")
            show player_teen_img at left with dissolve
            player "这不是威胁。这是事实。事实不需要威胁。"

            $ hide_all_chars()
            "他气得发抖，但一个字都回不上来。他狠狠地瞪了你一眼，转身带着随从走了。走之前踢翻了一个小贩的推车，算是发泄。"

            "你走到男孩面前，帮他擦了擦脸上的血。他用一种看神仙一样的眼神看着你。"

            "那天的事情很快在修道院传开了。大多数人佩服你的胆量和口才。也有人说你太出风头了。"

            "但你不在乎。你学到了一件事——语言用对了地方，比拳头更锋利。"

        "不出头，悄悄绕到男孩身边帮他。":
            $ change_stat("loyalty", 4)
            $ change_stat("faith", 3)
            $ deep_street_justice = "help"
            $ log_decision("序章深化", "暗中帮助", "忠诚+4 信仰+3")

            "你没有上前。不是因为怕。是因为你知道，跟一个伯爵的儿子正面冲突不是明智之举。"

            "你绕到巷子的另一边，等那个恶霸踢够了、笑够了、带着随从大摇大摆地走了之后，你才走过去。"

            "男孩蜷缩在墙角，像一只受伤的小动物。他看到你走过来，本能地缩了一下。"

            $ hide_all_chars("player_teen_img")
            show player_teen_img at left with dissolve
            player "别怕。我不会伤害你。"

            $ hide_all_chars()
            "你蹲下来，检查了他的伤。鼻血还在流，右眼肿了一圈，肋骨那里一碰就疼。"

            "你把自己的外袍脱下来披在他身上——他的衣服太薄了，而且被扯破了好几处。"

            $ hide_all_chars("player_teen_img")
            show player_teen_img at left with dissolve
            player "你家在哪？我送你回去。"

            $ hide_all_chars()
            "男孩摇头。他的嘴唇在动，但声音小得几乎听不到。"

            "「没有家……」"

            "你愣了一下。然后你从口袋里掏出了这个月剩下的所有零花钱，塞在他手里。"

            $ hide_all_chars("player_teen_img")
            show player_teen_img at left with dissolve
            player "去找个地方先吃顿饱饭。如果还有人欺负你……"

            "你想了想。你能做什么呢？你也只是一个十四岁的修道院学生。"

            player "去圣·尤里安修道院的后门。跟守门的修士说你要找我。[player_name]。记住了吗？"

            $ hide_all_chars()
            "男孩点了点头。你不知道他会不会来找你。但你知道你做了自己能做的。"

            "马库斯在旁边什么都看在眼里。他没有说你对，也没有说你错。他只是拍了拍你的肩膀。"

            hide player_teen_img
            $ hide_all_chars("friend_marcus_img")
            show friend_marcus_img at left with dissolve

            friend_marcus "你这个人啊……"

            hide friend_marcus_img with dissolve

            "他没说完。但你们都知道他想说什么。"

    scene black with dissolve
    pause 0.3

    "那件事之后，你开始留意王都的另一面——不是贵族的宴会和修道院的课堂，而是小巷里的饥饿、底层人的卑微、以及权力被滥用时的丑陋。"

    "这个世界需要改变。但怎么改？用拳头，用脑子，还是用别的什么？"

    "你十四岁。还没有答案。但问题已经种下了。"

    return


## ──────────────────────────────────────────────────────────
## 场景6：月夜的密谈 (15岁)
## ──────────────────────────────────────────────────────────

label prologue_deep_youth_3:

    scene bg church_interior with dissolve

    "修道院的最后一年。你十五岁。"

    "秋天的夜晚来得很早。晚祷结束后，整座修道院沉入黑暗。只有走廊拐角的几盏长明灯还亮着，在石壁上映出摇晃的光影。"

    "你回到寝室准备睡觉。推开门，看到马库斯坐在你的床上。"

    "他没有开灯。在月光下，你只能看到他的轮廓。他的肩膀在微微颤抖。"

    $ hide_all_chars("friend_marcus_img")
    show friend_marcus_img at left with dissolve

    hide friend_marcus_img
    $ hide_all_chars("player_teen_img")
    show player_teen_img at left with dissolve
    player "马库斯？怎么了？"

    $ hide_all_chars()
    "他没有立刻说话。你走过去，在他旁边坐下。你能闻到他身上有酒味——他肯定偷偷喝了什么。"

    "你等着他开口。夜虫在墙角叫个不停。你等了很久，久到以为他睡着了。"

    "然后他开口了。"

    hide player_teen_img
    $ hide_all_chars("friend_marcus_img")
    show friend_marcus_img at left with dissolve
    friend_marcus "我有件事必须告诉你。如果我不说，我这辈子都不会安心。"

    "你等着。"

    friend_marcus "我爹……你知道我家的情况。"

    "你知道。马库斯的父亲是个小贵族，领地不大，但祖上有些名望。这几年家里的生意不好，据说欠了不少债。"

    friend_marcus "不只是欠了债。[player_name]，我爹欠了莱茵哈特伯爵一大笔钱。大到整个家族加起来都还不清的那种。"

    "你皱了皱眉。莱茵哈特伯爵——那个打人的恶霸的父亲。王都最有权势的贵族之一。"

    friend_marcus "半年前，伯爵找到我爹。说可以免除所有债务。条件是——"

    "他的声音变得很低。"

    friend_marcus "条件是让我留在你身边。盯着你。你做了什么、说了什么、见了什么人，都要报告给他。"

    $ hide_all_chars()
    "空气凝固了。"

    "月光从窗户射进来，在地上画出一个十字。你看着马库斯的脸——他没有看你。他低着头，盯着自己的手。"

    $ hide_all_chars("friend_marcus_img")
    show friend_marcus_img at left with dissolve
    friend_marcus "我……照做了。半年来，你跟谁聊天、读了什么书、去了什么地方，我都告诉了他的人。"

    "他的声音开始发抖。"

    friend_marcus "但我受不了了。你是我最好的朋友。唯一的朋友。我不能继续这样骗你。"

    "他终于抬起头，看着你的眼睛。月光下，你看到他脸上有泪痕。"

    friend_marcus "你可以恨我。你应该恨我。但我至少要让你知道真相。"

    hide friend_marcus_img with dissolve

    $ hide_all_chars()
    "房间里安静得能听到彼此的心跳。"

    "你花了很长时间消化这些话。愤怒？是的。受伤？也是。但更多的是……理解。你见过太多被逼到绝路的人做出的选择。马库斯不是坏人。他只是一个被困在角落里的孩子。"

    "和你一样。"

    menu:
        "原谅他，主动提出帮助他的家族。":
            $ change_stat("loyalty", 10)
            $ deep_marcus_confession = "forgive"
            $ deep_marcus_truly_loyal = True
            $ change_rel("rel_captain", 3)
            $ log_decision("序章深化", "原谅马库斯", "忠诚+10 马库斯忠诚")

            "你伸出手，放在他的肩膀上。"

            $ hide_all_chars("player_teen_img")
            show player_teen_img at left with dissolve
            player "马库斯。"

            "他畏缩了一下，像是在等你揍他。"

            player "抬头看着我。"

            "他慢慢抬起头。你看到了一双红肿的眼睛，里面装满了恐惧和愧疚。"

            player "你告诉了我真相。这比什么都重要。"

            hide player_teen_img
            $ hide_all_chars("friend_marcus_img")
            show friend_marcus_img at left with dissolve

            friend_marcus "可是我——"

            hide friend_marcus_img
            $ hide_all_chars("player_teen_img")
            show player_teen_img at left with dissolve
            player "你做了错事。但你选择了坦白。这说明你是什么样的人。"

            "你站起来，走到窗前。月亮很圆，照得整个庭院一片银白。"

            player "莱茵哈特伯爵想监视我，说明他对我有所忌惮。这不是坏事。"

            "你转过身。"

            player "至于你家的债务——让我想想办法。我父亲虽然不是王都最有权势的人，但他不是没有朋友。"

            hide player_teen_img
            $ hide_all_chars("friend_marcus_img")
            show friend_marcus_img at left with dissolve
            friend_marcus "你……你不恨我？"

            hide friend_marcus_img
            $ hide_all_chars("player_teen_img")
            show player_teen_img at left with dissolve
            player "我恨你没有早点告诉我。"

            "马库斯笑了。那是一种如释重负的笑，像是背了半年的石头终于放下了。"

            hide player_teen_img
            $ hide_all_chars("friend_marcus_img")
            show friend_marcus_img at left with dissolve
            friend_marcus "[player_name]。我这条命是你的。从今天起，我不会再对你撒一句谎。"

            hide friend_marcus_img with dissolve

            $ hide_all_chars()
            "你相信他。不是因为他的话，而是因为他的眼神。"

            "那天晚上你们谈了很久。你们商量了怎么应对伯爵的人——不是断绝联系，而是精心选择该透露什么、该隐瞒什么。"

        "感到被背叛，和他保持距离。":
            $ change_stat("power", 5)
            $ change_courage(2)
            $ deep_marcus_confession = "distance"
            $ log_decision("序章深化", "疏远马库斯", "谋略+5 勇气+2")

            "你站起来。走到窗前。"

            "你的后背对着他。你需要一点时间。"

            $ hide_all_chars("player_teen_img")
            show player_teen_img at left with dissolve
            player "半年。"

            "你的声音很平静。也许太平静了。"

            player "半年来，你坐在我旁边吃饭、跟我一起练剑、陪我逛书摊——每一天，你都在监视我。"

            hide player_teen_img
            $ hide_all_chars("friend_marcus_img")
            show friend_marcus_img at left with dissolve

            friend_marcus "我——"

            hide friend_marcus_img
            $ hide_all_chars("player_teen_img")
            show player_teen_img at left with dissolve
            player "让我说完。"

            "马库斯闭上了嘴。"

            player "我理解你的处境。我真的理解。但你刚才说的话，不会因为一个道歉就消失。"

            "你转过身。"

            player "我需要时间。也许很长的时间。在那之前——我们之间保持距离。"

            hide player_teen_img
            $ hide_all_chars("friend_marcus_img")
            show friend_marcus_img at left with dissolve
            friend_marcus "[player_name]……"

            hide friend_marcus_img
            $ hide_all_chars("player_teen_img")
            show player_teen_img at left with dissolve
            player "你可以继续给伯爵的人报告。告诉他们我说了什么、做了什么。我不在乎。但——"

            "你看着他的眼睛。"

            player "从现在起，我不会再对你说任何我不想让伯爵知道的事情。"

            hide friend_marcus_img with dissolve

            $ hide_all_chars()
            "马库斯低下头。你看到一滴水落在石地上。"

            "那天晚上他离开后，你一个人坐了很久。"

            "你告诉自己这是正确的选择。信任一旦碎裂，就不可能完好如初。最多只能拼起来——但裂痕永远在那里。"

            "你学到了一课。在这个世界上，没有任何人是完全可以信任的。包括你最好的朋友。"

            "这一课很痛。但很有用。"

        "利用这个局面——让马库斯传递假情报。":
            $ change_stat("intrigue", 5)
            $ deep_marcus_confession = "exploit"
            $ log_decision("序章深化", "利用马库斯传假情报", "谋略+10")

            "你的脑子开始高速运转。"

            "愤怒在那里，但你把它压了下去。这不是发火的时候。这是——机会。"

            $ hide_all_chars("player_teen_img")
            show player_teen_img at left with dissolve
            player "马库斯。你说你把关于我的一切都报告给了伯爵？"

            $ hide_all_chars("friend_marcus_img")
            show friend_marcus_img at left with dissolve

            friend_marcus "是……是的。"

            hide friend_marcus_img
            $ hide_all_chars("player_teen_img")
            show player_teen_img at left with dissolve
            player "那，如果我告诉你一些我「不小心」透露的消息，你照样报告上去——伯爵会相信吗？"

            "马库斯茫然地看着你。他显然没有料到你会是这个反应。"

            hide player_teen_img
            $ hide_all_chars("friend_marcus_img")
            show friend_marcus_img at left with dissolve
            friend_marcus "大概……会吧。他没有理由怀疑。"

            "你笑了。不是那种温暖的笑，而是一种更冷、更锐利的笑。"

            hide friend_marcus_img
            $ hide_all_chars("player_teen_img")
            show player_teen_img at left with dissolve
            player "那就继续做你一直在做的事。但从今天起，你报告什么，由我来决定。"

            hide player_teen_img
            $ hide_all_chars("friend_marcus_img")
            show friend_marcus_img at left with dissolve
            friend_marcus "你要……利用这个？"

            hide friend_marcus_img
            $ hide_all_chars("player_teen_img")
            show player_teen_img at left with dissolve
            player "伯爵想监视我？很好。让他看到我想让他看到的东西。"

            hide friend_marcus_img with dissolve

            $ hide_all_chars()
            "你开始在脑子里列清单。你可以让伯爵认为你对政治毫无兴趣；可以让他觉得你和某个他讨厌的人关系很差；可以散布你即将回乡的假消息，让他放松警惕。"

            "可能性是无限的。"

            "马库斯看着你的表情，像是第一次真正认识你。"

            hide player_teen_img
            $ hide_all_chars("friend_marcus_img")
            show friend_marcus_img at left with dissolve

            friend_marcus "你……不生气吗？"

            hide friend_marcus_img
            $ hide_all_chars("player_teen_img")
            show player_teen_img at left with dissolve
            player "当然生气。但生气解决不了问题。"

            "你拍了拍他的肩膀。力度比平时重了一些。"

            player "你用半年时间背叛了我。从现在起，你用余生来还。"

            hide friend_marcus_img with dissolve

            $ hide_all_chars()
            "马库斯不说话了。但他点了头。那个点头的动作很轻，却很坚定。"

            "你不确定这是不是最好的做法。你用友谊的碎片换了一枚棋子。但这是你目前能做出的最「聪明」的选择。"

            "只是……在深夜一个人的时候，你偶尔会觉得某个地方有点疼。你说不清是哪里。"

    scene black with dissolve
    pause 0.3

    "那个夜晚改变了你们的关系。不管你做了什么选择，你和马库斯之间都再也回不到从前那种单纯的友谊了。"

    "这就是长大的代价。你失去了一些东西——天真、信任、或者某种柔软的情感——换来了另一些东西。"

    "至于换来的那些东西值不值……你现在还不知道。"

    return


## ════════════════════════════════════════════════════════════
## 第三部分：青年深化 (2场景)
## ════════════════════════════════════════════════════════════


## ──────────────────────────────────────────────────────────
## 场景7：酒馆里的赌局 (19岁)
## ──────────────────────────────────────────────────────────

label prologue_deep_adult_1:

    scene bg tavern with dissolve

    "你十九岁。在王都已经独自生活了一年。"

    "你学会了很多修道院里学不到的东西。比如怎么在市集上还价（永远先出对方开价的三成），怎么看人（说话时不看你眼睛的人多半在撒谎），以及怎么喝酒（答案是别喝太多）。"

    "那天晚上，马库斯——你们的关系不管怎样，他仍然是你在王都最常联系的人——带你去了一个地方。"

    "「你总在酒馆里喝那种三铜板一杯的劣质麦酒，」他说。「该见见世面了。」"

    "他带你去的地方在王都东区的一条暗巷尽头。没有招牌，只有一扇不起眼的木门。门上刻着一个你不认识的符号——像一只闭合的眼睛。"

    "马库斯敲了三下门。门开了。"

    "里面和外面是两个世界。"

    "厅堂不大，但装潢精致。墙上挂着织锦，地上铺着厚厚的地毯。空气中飘着某种名贵香料的气味。几张圆桌分散在各处，桌上铺着绿色的绒布，上面放着骰子和纸牌。"

    "这是一个高级赌馆。出入的都是王都的有头有脸的人物——商人、小贵族、甚至还有几个你在修道院见过的教士。"

    "你们在一张角落的桌子坐下。马库斯要了两杯酒，开始教你玩一种叫「三王」的纸牌游戏。你输了几局，赢了几局，总的来说乐在其中。"

    "然后有人在你对面坐了下来。"

    "你抬头。是一个中年男人，留着修剪整齐的胡须，穿着一件深蓝色的丝绸外衣。他的手指上戴着好几枚戒指——每一枚都价值不菲。"

    "但最引人注目的是他的眼睛。浅灰色的，像冬天的湖水。冷静、深邃，而且——你直觉告诉你——极其危险。"

    "「艾登堡的小鹰。」他笑了笑。「久仰大名。」"

    $ hide_all_chars("player_young_img")
    show player_young_img at left with dissolve
    player "你认识我？"

    $ hide_all_chars()
    "「这座城里认识你的人比你想象的多。」"

    "他自我介绍叫赫尔曼。说自己是个商人，做东西南北的生意。他的语气随和，但你注意到他坐下来的时候，周围好几个人都不自觉地看了过来。"

    "「来一局？」他指了指桌上的纸牌。「不赌钱。赌消息。」"

    "「什么意思？」"

    "「你赢了，我告诉你一个关于你父亲的秘密。你输了……」"

    "他微微一笑。"

    "「你回答我一个问题。怎么样？」"

    hide player_young_img
    $ hide_all_chars("friend_marcus_img")
    show friend_marcus_img at left with dissolve

    friend_marcus "别答应。这个人不简单。"

    hide friend_marcus_img with dissolve

    $ hide_all_chars()
    "马库斯在你耳边小声说。但你已经被勾起了好奇心。关于父亲的秘密？"

    "「不赌消息也可以。」赫尔曼又说，「如果你更喜欢真金白银——我有一些关于宫廷里的情报。比如，谁在暗中调查你父亲。这种消息在外面买不到。但在这里——」"

    "他摊开手。"

    "「一切都有价格。」"

    menu:
        "付钱买情报。（财富-10）":
            $ change_stat("wealth", -10)
            $ deep_tavern_intel = True
            $ deep_tavern_choice = "pay"
            $ log_decision("序章深化", "付钱买情报", "财富-15 获得情报")

            "你考虑了一下。然后你从腰间解下钱袋，放在桌上。"

            "那是你半个月的生活费。"

            $ hide_all_chars("player_young_img")
            show player_young_img at left with dissolve
            player "够吗？"

            $ hide_all_chars()
            "赫尔曼拈起钱袋，掂了掂重量。"

            "「不够。但诚意够了。」"

            "他收起钱袋，身体微微前倾，声音压得只有你们两个人能听到。"

            "「你父亲在王都有敌人。不是一个，是一群。他们自称——」"

            "他的声音更低了。"

            "「王后的鹰犬。」"

            "你的心跳了一下。"

            "「两年前，王后派人秘密调查你父亲的领地。查税务、查军备、查与北境各部族的往来。你父亲知道这件事，所以才让你留在王都——不是开阔眼界，是避险。」"

            $ hide_all_chars("player_young_img")
            show player_young_img at left with dissolve
            player "避险？我在这里怎么就安全了？"

            $ hide_all_chars()
            "「因为你在王都，就等于在王后的眼皮底下。她看得到你，就不会觉得你父亲在暗中谋反。你是一枚人质，小鹰。只不过你自己不知道。」"

            "你想起父亲让你留在王都时的语气——平静、随意，好像只是一个无关紧要的建议。"

            "原来每一句话都有深意。"

            "「还有一件事。」赫尔曼说。「王后身边有一个人，专门负责监视各地领主的子嗣。一个女人。非常聪明，非常危险。」"

            $ hide_all_chars("player_young_img")
            show player_young_img at left with dissolve
            player "她叫什么？"

            $ hide_all_chars()
            "「这个嘛……超出今天的价格了。」"

            "他站起来，朝你微微鞠了一躬。"

            "「下次再来。带够钱。」"

            "他走了。你坐在桌前，手指无意识地翻弄着纸牌。你的脑子里全是他说的那些话。"

            "人质。你是一枚人质。"

            "这个认知像一盆冰水，浇在了你十九岁的骄傲上。"

        "跟他玩牌，靠智慧赢取情报。":
            $ deep_tavern_choice = "outplay"
            $ log_decision("序章深化", "尝试牌局", "")

            $ hide_all_chars("player_young_img")
            show player_young_img at left with dissolve
            player "不用花钱。我跟你赌。"

            $ hide_all_chars()
            "赫尔曼的眼睛亮了一下。他发牌。"

            "三王——三局两胜。第一局你输了。赫尔曼的牌技出神入化，他总能准确地猜到你手里的牌。"

            "第二局，你调整了策略。你故意打出几张误导性的牌，让他判断失误。这次你赢了。"

            "一比一平。决胜局。"

            "你的手心在出汗。整个赌馆的注意力都集中到了这张桌子上。"

            if intrigue >= 45:
                $ change_stat("intrigue", 5)
                $ deep_tavern_intel = True

                "你赢了。"

                "不是靠运气——是靠观察。你注意到赫尔曼每次拿到好牌时，左手无名指会微微动一下。一个极其细微的习惯动作，他自己可能都不知道。"

                "你利用了这个破绽。"

                "赫尔曼看着自己手里的牌，然后看着你，慢慢笑了。"

                "「有意思。很有意思。」"

                "他信守承诺。他告诉你，王后一直在暗中监视你父亲，你留在王都相当于一枚无形的人质。"

                "「记住这些。它们会在你需要的时候派上用场。」"

                "然后他起身离开了。像来时一样，无声无息。"

                "你赢了情报，没花一分钱。但你觉得——赫尔曼也许并不是输了。也许这一切都在他的计划之中。"

            else:
                $ change_stat("wealth", -7)

                "你输了。"

                "最后一张牌翻开的那一刻，你就知道结局了。赫尔曼的牌面完美得不像是巧合。"

                "「不用沮丧。你的牌技不错，只是经验不够。」"

                "他收起纸牌。"

                "「我赢了一个问题的权利。」"

                "他看着你的眼睛。"

                "「你父亲——有没有跟你提过一个叫「暗百合」的名字？」"

                $ deep_tavern_heard_lily = True

                "你不知道该怎么回答。你只是摇了摇头。"

                "「嗯。」他点了点头，像是在确认什么。「那就好。」"

                "他站起来，留下一枚银币。"

                "「这是赌注。算我请你喝酒。」"

                "你输了牌局，也没有得到情报。但那个名字——暗百合——又一次出现了。你开始觉得，所有看似无关的事情，也许都指向同一个方向。"

        "谢绝，起身离开。":
            $ deep_tavern_choice = "refuse"
            $ log_decision("序章深化", "拒绝赌局", "安全但错过情报")

            $ hide_all_chars("player_young_img")
            show player_young_img at left with dissolve
            player "不了。谢谢你的好意。"

            $ hide_all_chars()
            "你站起来。赫尔曼没有挽留你。他只是笑了笑。"

            "「谨慎。这在年轻人身上是稀罕品质。」"

            "你和马库斯离开了赌馆。走在暗巷里，夜风吹得你清醒了不少。"

            $ hide_all_chars("friend_marcus_img")
            show friend_marcus_img at left with dissolve

            friend_marcus "你做了聪明的决定。那个人浑身上下都是危险。"

            hide friend_marcus_img
            $ hide_all_chars("player_young_img")
            show player_young_img at left with dissolve
            player "我知道。但……"

            "你犹豫了一下。"

            player "他说他知道关于我父亲的事。我有点好奇。"

            hide player_young_img
            $ hide_all_chars("friend_marcus_img")
            show friend_marcus_img at left with dissolve
            friend_marcus "好奇害死猫。你不是猫。"

            hide friend_marcus_img with dissolve

            $ hide_all_chars()
            "你笑了笑。也许马库斯是对的。有些门不应该打开。有些交易不应该做。"

            "但那个男人的灰色眼睛留在你的记忆里，像一块冰，融不掉。"

            "你后来再也没有回到那个赌馆。但你偶尔会想——如果那天你留下来了，会发生什么？"

            "有些遗憾，要很久以后才能感受到它的重量。"

    scene black with dissolve
    pause 0.3

    "赌馆之夜过后，你对王都的认识又深了一层。"

    "这座城市的表面是繁华、秩序和礼仪。但在表面之下，暗流涌动。每一个微笑都可能藏着刀，每一句好话都可能是诱饵。"

    "你十九岁。你开始明白——在这个世界上，最贵的东西不是金子，而是信息。"

    return


## ──────────────────────────────────────────────────────────
## 场景8：暗夜来客 (20岁)
## ──────────────────────────────────────────────────────────

label prologue_deep_adult_2:

    scene bg player_room with dissolve

    "你二十岁的那个冬天。"

    "王都下了入冬以来最大的一场雪。街道上的积雪到了膝盖。大部分店铺都关了门，连酒馆里的酒鬼都不愿意出门。"

    "你窝在自己的小公寓里，烤着壁炉，读一本关于王国南部历史的旧书。窗外是无边无际的白色。"

    "夜里。大约三更。"

    "你被一阵声响惊醒——不是敲门声，而是窗户被推开的声音。"

    "你的手立刻摸向枕头下面的短刀。这个习惯是在王都养成的——这座城市的夜晚并不总是平静的。"

    "你睁开眼。壁炉的余烬还在发出微弱的红光。在那红光中，你看到了一个人影。"

    "一个女人。穿着深色的斗篷，兜帽遮住了大半张脸。她站在你房间的窗户旁边——二楼的窗户。雪夜。她是从外面翻进来的。"

    "你的手握紧了短刀。"

    $ hide_all_chars("player_young_img")
    show player_young_img at left with dissolve
    player "你是谁？怎么进来的？"

    $ hide_all_chars()
    "女人没有动。她的声音低沉而清晰，像是经过训练的。"

    "「别紧张，小鹰。我不是来伤害你的。」"

    $ hide_all_chars("player_young_img")
    show player_young_img at left with dissolve
    player "那你来做什么？"

    $ hide_all_chars()
    "「送一个消息。」"

    "她往前走了一步。壁炉的光映在她脸上——你能看到她的下半张脸。皮肤很白，嘴唇很薄。一道细小的伤疤从嘴角延伸到下颚。"

    "「你父亲的敌人已经知道你在长大。他们在盯着你。如果你继续留在王都——你会有危险。」"

    $ hide_all_chars("player_young_img")
    show player_young_img at left with dissolve
    player "什么敌人？具体点。"

    $ hide_all_chars()
    "「……具体的事情我无法全部告诉你。但你应该知道，有人在调查你父亲的过去。调查得越深，你的处境就越危险。」"

    "她停顿了一下。"

    "「你应该回家。回艾登堡。越快越好。」"

    $ hide_all_chars("player_young_img")
    show player_young_img at left with dissolve
    player "为什么要帮我？你到底是谁？"

    $ hide_all_chars()
    "「谁派我来的并不重要。重要的是——你的时间不多了。」"

    "她转身准备从窗户离开。你必须在几秒钟内做出决定。"

    menu:
        "拦住她，要求她表明身份。":
            $ change_stat("power", 5)
            $ deep_night_visitor = "demand"
            $ deep_lily_contact_early = True
            $ log_decision("序章深化", "要求表明身份", "谋略+5 提前接触暗百合")

            "你一个翻身从床上起来，挡在了窗户前面。"

            $ hide_all_chars("player_young_img")
            show player_young_img at left with dissolve
            player "你不说清楚，就别想走。"

            $ hide_all_chars()
            "女人停下了。她看着你——你第一次直视她的眼睛。黑色的，像深不见底的井。"

            "「你确定想知道？」"

            $ hide_all_chars("player_young_img")
            show player_young_img at left with dissolve
            player "我确定。"

            $ hide_all_chars()
            "窗外的雪落在屋檐上，发出细微的沙沙声。"

            "然后她伸出手，解开了斗篷的扣子。斗篷滑落，露出她里面的衣服——一件贴身的黑色皮衣，左胸口绣着一朵花。"

            "一朵百合。"

            if deep_cellar_heard_lily and deep_tavern_heard_lily:
                "你的呼吸停了一瞬。百合。暗百合。七岁那年在地窖里听到的名字。十九岁在赌馆里被问起的名字。"
            elif deep_cellar_heard_lily:
                "你的呼吸停了一瞬。百合。暗百合。七岁那年在地窖里听到的名字。"
            elif deep_tavern_heard_lily:
                "你的呼吸停了一瞬。百合。暗百合。十九岁在赌馆里被问起的名字。"
            else:
                "你的呼吸停了一瞬。百合。暗百合。一个你隐约听说过的名字。"

            "现在它出现在一个深夜闯入你房间的女人的胸口。"

            $ hide_all_chars("player_young_img")
            show player_young_img at left with dissolve
            player "暗百合……"

            $ hide_all_chars()
            "女人微微点头。"

            "「你知道这个名字。这比我预料的要多。」"

            $ hide_all_chars("player_young_img")
            show player_young_img at left with dissolve
            player "你们……和我父亲是什么关系？"

            $ hide_all_chars()
            "「这个问题，你应该去问你父亲。我只是一个信使。」"

            "她重新披上斗篷。"

            "「记住我说的话。离开王都。不是明天，不是下周——越快越好。」"

            "她翻身上了窗台。雪花涌进来，带着刺骨的寒意。"

            "「金鹰不死。百合不凋。」"

            "这句话。和那个夜晚地窖里的那句一模一样。"

            "然后她消失在了雪夜里。像一滴墨溶进了白纸。"

            "你站在窗前，心脏狂跳。暗百合——一个贯穿你整个人生的名字——终于不再只是一个传说。"

            "他们是真实的。他们在暗中保护你。或者——监视你。你还分不清。"

        "感谢她的警告，认真对待。":
            $ change_stat("loyalty", 3)
            $ change_stat("loyalty", 2)
            $ deep_night_visitor = "heed"
            $ log_decision("序章深化", "听从警告", "谋略+3 忠诚+2")

            "你放下了短刀。"

            $ hide_all_chars("player_young_img")
            show player_young_img at left with dissolve
            player "谢谢你。"

            $ hide_all_chars()
            "女人明显没有预料到这个回答。她停顿了一下。"

            "「不问我是谁？」"

            $ hide_all_chars("player_young_img")
            show player_young_img at left with dissolve
            player "你不想说，我问了也没用。但你大半夜翻窗进来只为了提醒一个陌生人——不管你的理由是什么，这份好意我收下了。"

            "你走到桌前，给自己倒了一杯水。手很稳。"

            player "我会考虑你说的话。回家这件事……不是不可以。但我需要一个理由——一个能对外面的人说的理由。"

            $ hide_all_chars()
            "女人轻声说——"

            "「你的父亲很快会给你写信。信里会给你理由。」"

            "这句话让你后背一凉。她不只是知道你的处境，她还知道你父亲的计划。她到底是什么人？"

            "但你没有追问。你说过了——她不想说，你不会逼。"

            "女人翻上了窗台。临走前她回过头。"

            "「你比你父亲年轻时聪明得多。他当年差点拔剑砍我的前辈。」"

            "然后她走了。"

            "你关上窗户，回到床上。你没有再睡着。你一直在想——父亲的信。"

            "三天后，信来了。父亲用一种异常正式的语气写道：「归来。家中有事——但不必急，把王都的事安排好再启程。」"

            "你把信收进抽屉。距离启程还有时间，足够你完成在王都的最后几件事。"

        "不以为然，认为这是某种圈套。":
            $ change_stat("power", 3)
            $ change_courage(3)
            $ deep_night_visitor = "dismiss"
            $ log_decision("序章深化", "不为所动", "权力+3 勇气+3")

            "你把短刀收了起来。你靠在床头，双手抱胸。"

            $ hide_all_chars("player_young_img")
            show player_young_img at left with dissolve
            player "一个陌生人半夜翻窗进来，叫我立刻离开王都。"

            "你笑了一声。"

            player "你觉得这像是善意的提醒，还是某种很拙劣的恐吓手段？"

            $ hide_all_chars()
            "女人没有动。"

            "「你不信？」"

            $ hide_all_chars("player_young_img")
            show player_young_img at left with dissolve
            player "我信不信不重要。重要的是——如果有人想让我害怕，他们派错人了。"

            "你站起来，走到她面前。你比她高出一个头。"

            player "回去告诉派你来的人：艾登堡的鹰不会因为几句话就夹着尾巴逃跑。"

            $ hide_all_chars()
            "女人看了你很久。那双黑色的眼睛像在看一个走不回来的人——不是愤怒，不是失望，更像是……惋惜？"

            "「傲慢。和你父亲一模一样。」"

            "她摇了摇头。"

            "「但愿你的运气比他好。」"

            "她从窗户翻了出去。几秒钟后，窗外只剩下飘落的雪花。"

            "你关上窗户，回到床上。你没有被她的话吓到。你见过太多试图利用恐惧来操纵别人的人。"

            "但——你也不是傻瓜。她的话你记在了心里。不是因为害怕，而是因为——一个能在雪夜无声翻进二楼窗户的人，不会是随便什么人。"

            "她的警告也许是真的。但你不会因为恐惧而做出决定。"

            "如果要离开王都，那必须是你自己的选择。不是因为别人的威胁。"

    scene black with dissolve
    pause 0.3

    "暗夜来客离开后的那些天，你反复思考她的话。"

    "你父亲的敌人。暗中的调查。百合的影子。所有的线索像散落的拼图碎片，你能感觉到它们属于同一幅图——但你还拼不出全貌。"

    "不过有一件事越来越清晰了：你不能永远做一个旁观者。"

    "不管你愿不愿意，权力的漩涡已经开始转动。而你——金鹰之子——已经被卷了进去。"

    "回家的日子，已经在视野里了。"

    return

## ============================================================
## 结局扩展 - 详细尾声篇
## endings_expansion.rpy
## 五大结局的详细尾声 + 隐藏结局「父与子」
## ============================================================

## 新增变量
default ending_epilogue_seen = False
default epilogue_faith_answer = ""
default epilogue_iron_choice = ""
default father_grave_visits = 0
default chose_honesty_in_prayer = False

## ============================================================
## 尾声入口 - 从各结局跳转到这里
## ============================================================

label ending_epilogue_router:

    $ ending_epilogue_seen = True

    if ending_type == "truth":
        jump ending_truth_epilogue
    elif ending_type == "iron_lord":
        jump ending_iron_epilogue
    elif ending_type == "shadow_king":
        jump ending_shadow_epilogue
    elif ending_type == "holy_guardian":
        jump ending_faith_epilogue
    elif ending_type == "peoples_lord":
        jump ending_peoples_epilogue
    else:
        return

## ============================================================
## 结局一：真相之路 - 扩展尾声
## The Truth Seeker Epilogue
## ============================================================

label ending_truth_epilogue:

    ## 婉拒首席摄政官任命 → 玩家走 chapter5 truth_humble_epilogue (回艾登堡守护一年四季),
    ## 那段已是完整尾声, 跳过这里整段王都"首席摄政官"扩展, 防叙事冲突.
    if truth_declined_regency:
        return

    scene black with fade

    centered "{size=+10}五年后{/size}"
    centered "{size=+6}王历二十七年·春{/size}"

    pause 1.0

    ## —— 第一幕：御前会议 ——

    scene bg throne_room with dissolve

    "五年过去了。"

    "当年那个为父报仇、揭露真相的年轻领主，如今已是整个王国最受信赖的重臣。"

    "公爵——这个王国除国王外最高的爵位，不再只是一个头衔。"
    "它意味着责任、权力，以及无数个不眠之夜。"

    "今天的御前会议上，讨论的是一桩棘手的贸易纠纷。"

    "南方的商会联盟与北方的矿主协会因为铁矿石的定价发生了严重分歧。"
    "双方各执一词，互不相让。如果处理不当，可能引发一场经济危机。"

    if prince_ally and not prince_betrayed:
        $ hide_all_chars("prince_img")
        show prince_img at left with dissolve

        prince "各位爱卿，南北两方的争端已经持续了三个月。朕需要一个解决方案。"

        $ hide_all_chars()
        "弗雷德里克国王——曾经那个迷茫的王子，如今已成长为一位沉稳的君主。"
        "但在遇到棘手问题时，他依然会习惯性地看向你。"

        $ hide_all_chars("prince_img")
        show prince_img at left with dissolve
        prince "[player_name]公爵，你怎么看？"

        hide prince_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "陛下，臣以为，争端的根源不在价格，而在于信息的不对称。"

        player "南方商会不知道北方的开采成本，北方矿主不了解南方的市场行情。"

        player "如果我们设立一个公开的价格委员会，由双方代表共同组成——"

        player "让所有数据透明公开，让每一个铜币的去向都清清楚楚——"

        player "那么，合理的价格自然会浮出水面。"

        hide player_char_img
        $ hide_all_chars("prince_img")
        show prince_img at left with dissolve
        prince "你总是这样……用真相解决一切问题。"

        "国王笑了。那是一个年轻人对老师的笑——带着敬意，也带着一丝调侃。"

        hide prince_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "真相不能解决一切问题，陛下。但它是解决大多数问题的起点。"

        hide player_char_img
        $ hide_all_chars("prince_img")
        show prince_img at left with dissolve
        prince "好。就照公爵的意思办。"

        if prince_mentor_known:

            prince "对了，[player_name]。关于新学院的事——"

            prince "朕决定以西里尔老师的名字来命名。'西里尔学院'。"

            prince "他教会了朕什么是真正的学问。虽然他选择了错误的道路，但他的教诲是真诚的。"

            hide prince_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "陛下胸怀宽广。西里尔若在天有灵，定会感到欣慰。"

            hide player_char_img
            $ hide_all_chars("prince_img")
            show prince_img at left with dissolve
            prince "人不能只被最后的错误定义。这也是你教会朕的。"

            $ hide_all_chars()
            "你微微颔首。五年前的那些事——背叛、阴谋、真相——如今都成了历史的一页。"
            "但历史的教训，永远不应被遗忘。"

        hide prince_img with dissolve

    else:
        "摄政委员会的会议厅里，七位委员正襟危坐。"
        "你坐在首席的位置——首席摄政官，这个王国实际上的最高决策者。"

        "没有国王。王位空悬已经五年了。"
        "有人说应该尽快选立新君，有人说摄政委员会运转良好，何必多此一举。"
        "你没有参与那些争论。你只做一件事——让这个国家变得更好。"

        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "南北争端的核心是信息不透明。"
        player "我提议设立公开价格委员会，让双方的成本和利润全部透明化。"
        player "只有在阳光下，才不会有暗箱操作的空间。"

        $ hide_all_chars()
        "委员们纷纷点头。五年来，你用'透明'二字治理这个国家，成效有目共睹。"
        "腐败减少了，税收增加了，百姓的信任也在一点一点建立起来。"

        "散会后，一位年长的委员走到你身边。"
        narrator "「首席大人，有件事我一直想说——您治国的方式，和当年的老领主很像。」"
        "你没有回答，只是点了点头。"
        "你比谁都清楚，这条路上的每一步，都踩在父亲留下的影子上。"

    "会议结束后，你独自站在窗前，看着王城的街道。"

    "街上人来人往，商贩吆喝，孩子嬉闹。"
    "和平——这个词在五年前还像一个遥不可及的梦想。"
    "现在，它就在眼前。真实而温暖。"

    if elena_romance:
        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve

        elena "又在发呆了？"

        "一只温暖的手搭上你的肩膀。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "想事情而已。"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "嗯。'想事情'是你的老毛病了。会议开完了？"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "嗯。贸易纠纷的事，基本有方案了。"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "我知道。我的人已经把南方商会的底牌查清楚了。"
        elena "他们声称的'运输成本暴涨'是假的。实际上是商会会长私吞了差价。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "……你什么时候查的？"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "你开会的时候。"

        $ hide_all_chars()
        "你苦笑着摇头。当年那个在暗巷里收集情报的间谍少女，如今已是王国的情报总监。"
        "也是你的妻子。"

        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "怎么，不高兴我先斩后奏？"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "不。我高兴的是——我永远不用担心被人蒙在鼓里。"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "那是当然。"

        "她沉默了一会儿。"

        elena "我父亲——你帮我查到了那条线。"

        "她的声音很轻，像是怕惊动什么。"

        elena "汉斯，那个酒窖管事——和我父亲死在同一年，用的是同一种毒药。"

        elena "我们家不算什么显赫的贵族，父亲也不是什么大人物。但那些被'暮色之露'夺去性命的人——都在同一份名单上。"

        elena "这五年里，我把那份名单上的每一个名字都核对完了。"

        elena "再没有第二个家庭，因为偶然瞥见不该看的东西，在沉默里慢慢死去。"

        "她转过头看你，眼底有一种你从未见过的平静。"

        elena "这是真相能给人的——我父亲生前没等到的——一个交代。"

        "你点了点头。这是你五年前没敢承诺、却终于做到的一件事。"

        "她靠在你肩上，看着窗外的夕阳。"

        elena "五年了。你不觉得累吗？"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "累。但值得。"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "嗯。值得。"

        $ hide_all_chars()
        "五年前你们在黑暗中并肩作战，如今在阳光下携手同行。"
        "有些东西——比权力、比爵位、比一切荣耀都更珍贵。"

        hide elena_img with dissolve

    else:
        "你一个人站在窗前，看着夕阳一寸一寸沉入城墙的轮廓后面。"

        "五年了。从一个被命运推上棋局的年轻人，到如今王国的柱石。"

        "有人问过你，这一路走来，最大的遗憾是什么。"

        "你没有回答。"

        "有些遗憾不是用语言能说清的。有些路，注定是一个人走的。"

        "夕阳的余晖洒满了空旷的走廊。你转过身，走向书房。"

        "明天还有很多事要做。这个国家不会因为你的沉思而停下脚步。"

    ## —— 第二幕：父亲的坟前 ——

    scene black with fade

    centered "{size=+8}秋·艾登堡{/size}"

    scene bg forest_path with dissolve

    "深秋时节，你踏上了回乡的路。"

    "艾登堡的树叶已经变成了金色和红色，铺满了山间的小路。"
    "空气中弥漫着泥土和落叶的气息——这是家的味道。"

    "你没有骑马，没有带随从。只有一个人陪着你。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    $ hide_all_chars()
    "奥尔德里克。"

    "七十多岁的老管家，白发苍苍，背已微驼。"
    "但他坚持要陪你走这段路。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "领主大人……不，公爵大人。您走慢些。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "奥尔德里克，叫我名字就好。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "那……可不行。规矩不能乱。"

    $ hide_all_chars()
    "你笑着摇头，放慢了脚步。"

    "小路尽头，是一座简朴的墓碑。"
    "墓碑上没有华丽的雕刻，只有几行端正的字："

    centered "{size=+4}艾登堡领主 卡尔·冯·艾登之墓{/size}"
    centered "忠诚、正义、不屈"

    "你在墓前站定。风吹过墓碑上的苔藓，带来泥土和青草的气味。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "父亲。"

    player "我又来看你了。"

    player "五年了。很多事情都变了。"

    player "当年你用生命守护的真相，终于大白于天下。"

    player "那些害你的人——有的伏法了，有的逃走了，有的……已经不在了。"

    player "但正义实现了。你的名字被刻在了王国的功勋碑上。"

    player "我做到了，父亲。"

    "秋风吹过，树叶沙沙作响。像是远方传来的低语。"

    player "我现在是公爵了。听起来很了不起，对吧？"

    player "但说实话……有时候我觉得自己还是当年那个站在你书房门口、什么都不懂的孩子。"

    player "我常常想——如果你还在，你会怎么做？你会做出怎样的选择？"

    player "但我知道……你已经做出了选择。你选择了真相。"

    player "我继承了你的选择。这就够了。"

    $ hide_all_chars()
    "你从怀中取出一封信——那是多年前从父亲书房里找到的最后一封家书。"
    "信纸已经泛黄，字迹却依然清晰。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你在信里说，'最重要的不是你拥有什么，而是你守护什么。'"

    player "我一直记得。"

    "你把信轻轻放在墓碑前，用一块小石头压住。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "领主大人……"

    "你转过头，看到老管家的眼里满是泪水。"

    aldric "老领主……会为您骄傲的。"

    aldric "老朽跟了您的父亲三十年，又跟了您五年。"

    aldric "这辈子……值了。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "奥尔德里克……"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "不过……"

    "老管家用袖子擦了擦眼睛，露出一个有些不好意思的笑容。"

    aldric "这大概是老朽最后一次陪您来了。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "……什么意思？"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "腿脚不行了。大夫说，明年春天可能就走不了远路了。"

    aldric "但没关系。该看的都看到了。该陪的都陪到了。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "奥尔德里克，你……"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "大人，不用难过。人总有这一天的。"

    aldric "能看到您成为今天的您——这已经是最好的结局了。"

    $ hide_all_chars()
    "你没有说话。你只是上前一步，紧紧握住了老管家的手。"

    "那双手——曾经为你准备早餐、为你整理衣冠、在你彷徨时拍着你肩膀的手——"
    "如今枯瘦如柴，但依然温暖。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "奥尔德里克。谢谢你。"

    player "谢谢你为这个家做的一切。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "……领主大人。"

    $ hide_all_chars()
    "老管家再也忍不住，佝偻着身子，默默哭了起来。"

    "秋风卷着落叶，在你们周围轻轻旋转。"
    "就像时光在这一刻放慢了脚步，允许两代人的忠诚有一个温柔的告别。"

    hide aldric_img with dissolve

    ## —— 第三幕：真相的代价 ——

    scene bg study with dissolve

    "夜深了。你回到艾登堡，坐在父亲曾经的书房里。"

    "书架上的书比五年前多了三倍。你在这里读过无数份报告、批复过无数道文书。"
    "但今晚，你只是坐着。"

    "桌上放着一封刚送到的急件——来自东方边境的情报。"

    "一个新兴的帝国正在东方崛起，他们的军队已经吞并了三个小国。"
    "下一个目标……可能就是你的王国。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "……"

    "你展开地图，看着东方那片巨大的阴影。"

    player "和平从来不是永恒的，对吗？"

    player "五年前，我以为揭露真相就是终点。"

    player "但真相只是一扇门。门后面，永远有新的问题等着你。"

    $ hide_all_chars()
    "你站起身，走到窗前。"

    "远处传来守夜人换岗的脚步声，铁器上凝了一层露水。"
    "远处传来守夜人悠长的号角声。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "真相的代价从未停止。"

    player "但我已经不害怕了。"

    player "因为我知道——只要我们敢于面对真相，就没有什么是不可战胜的。"

    if prince_ally and not prince_betrayed:
        $ hide_all_chars()
        "你回到书桌前，提起笔，开始给弗雷德里克国王写信。"

        "信的开头是——"

        centered "「陛下，东方有变。但请勿惊慌。」"
        centered "「真相是我们最好的武器。而我们——永远不会放下它。」"
    else:
        "你回到书桌前，提起笔，开始给摄政议会写信。"

        "信的开头是——"

        centered "「诸位大人，东方有变。但请勿惊慌。」"
        centered "「真相是我们最好的武器。而我们——永远不会放下它。」"

    "窗外，月亮渐渐隐入云层。"
    "但你知道——它明天还会升起来。"
    "就像真相一样。"


    ## ── 真相的代价 ──

    "真相公布之后，每一个人都必须面对它带来的后果。"

    "男爵的命运交给了法庭。"

    if baron_peace_path:
        "他曾在调查中提供过协助——也许是出于良心，也许是出于自保。但法庭认定这足以构成减刑的理由。"
        "他被流放而非处刑。一艘小船载着他驶向南方的海岸。他回头看了一眼——那是他最后一次看到这片土地。"
    else:
        "他以共谋罪和叛国罪被起诉。证据确凿，无从辩驳。"
        if prince_ally and not prince_betrayed:
            "法庭的审判持续了三天。最终的判决交给了弗雷德里克国王。你不知道结果——但真相已经给了正义一个迟到的机会。"
        else:
            "法庭的审判持续了三天。最终的判决交给了摄政议会。你不知道结果——但真相已经给了正义一个迟到的机会。"

    "真相大白的光芒照亮了每一个角落——包括暗百合的秘密。"

    if dark_lily_joined:
        "你为它说了话。你告诉法庭，暗百合曾在揭露真相的过程中提供过关键帮助。"
        "功过相抵。法庭要求它公开化、接受监管。不再有暗号和面具——但那份对正义的追求，被允许在阳光下继续。"
    elif dark_lily_destroyed:
        "它已经不存在了。真相的故事里不需要再提起一个已经消亡的名字。"
    else:
        "真相的曝光连带揭开了暗百合的全部秘密——联络网、藏身点、成员名册。"
        "它被迫解散。真相之光不分敌我。但也许，一个不再需要暗影保护的世界，正是暗百合最初的愿望。"

    scene black with fade

    centered "{size=+8}真相之路 · 尾声{/size}"
    centered "「有些路走了就不能回头。但回头看时，你会发现——」"
    centered "「每一步都是值得的。」"

    pause 2.0

    ## ── 隐藏结局触发：父与子 ──
    ## 条件: truth 完整路线 (知死因 + 真凶 + 密信) + 高忠诚 (rel_aldric >= 60)
    ## 即"做满了真相该做的所有事 + 老管家深度认同"才触发, 表达"父亲终于可以告别"
    if (not truth_declined_regency
            and father_poisoned_known
            and true_killer_known
            and father_letters_found
            and rel_aldric >= 60):
        jump ending_father_son_epilogue

    return

## ============================================================
## 结局二：铁腕领主 - 扩展尾声
## The Iron Lord Epilogue
## ============================================================

label ending_iron_epilogue:

    scene black with fade

    centered "{size=+10}五年后{/size}"
    centered "{size=+6}王历二十七年·冬{/size}"

    pause 1.0

    ## —— 第一幕：铁之阅兵 ——

    scene bg battlefield with dissolve

    "寒风凛冽。旌旗猎猎。"

    "五千名士兵整齐列阵，铠甲在冬日的阳光下闪烁着冷光。"
    "他们是这个王国最精锐的军队——艾登堡铁骑。"

    "而你，站在检阅台上，俯视着这支你亲手缔造的力量。"

    "五年前，你选择了铁与血的道路。"
    "五年后，你已是这个王国最令人畏惧的军事领主。"

    "没有人敢挑战你的权威。没有人敢在你的领地上越雷池一步。"
    "你的名字在边境之外也广为流传——不是作为英雄，而是作为一个不可战胜的存在。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "大人，阅兵准备就绪。五千铁骑，一人不缺。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "好。让他们开始。"

    $ hide_all_chars()
    "号角响起。铁骑如潮水般涌过检阅台前，马蹄声震动大地。"

    "每一个士兵都向你行注目礼——眼中带着敬畏，也带着一丝……恐惧。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "大人，这是王国有史以来最强大的军队。没有人能撼动我们。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "力量不是用来炫耀的。记住这一点。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "是！"

    if captain_war_pledge:
        captain "大人。五年前我曾对您立誓——我的命就是您的盾。"
        captain "五年过去了。这面盾还在。而且——比以前更硬了。"

    hide captain_img with dissolve

    $ hide_all_chars()
    "阅兵结束后，你独自走回营帐。"

    "营帐里有一面铜镜。你在镜前站定，看着镜中的自己。"

    "五年前那个青涩的年轻领主，如今已被岁月和战争雕刻成了另一个人。"
    "眼神锐利，嘴角紧抿，脸上带着常年握权者特有的冷峻。"

    "但在某个瞬间——"

    "你在镜中看到了另一张脸。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "……父亲？"

    $ hide_all_chars()
    "不。那不是父亲。"

    "那是你想象中父亲看着你时的表情。"
    "不是骄傲。不是欣慰。"
    "是……失望。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "……"

    "你闭上眼，然后转身离开了铜镜。"

    ## —— 第二幕：外交风云 ——

    scene bg great_hall with dissolve

    "三天后。艾登堡的大厅里迎来了一位特殊的客人。"

    "来自东方拉维尼亚帝国的特使——一个身披华丽锦袍、面带微笑的中年男人。"

    "拉维尼亚帝国。东方最强大的国家。他们的疆域是你的王国的三倍。"

    $ hide_all_chars("servant_generic_img")
    show servant_generic_img at left with dissolve
    envoy "久仰大名，公爵大人。拉维尼亚皇帝陛下派我前来，是为了表达友好之意。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "友好？你们的军队刚刚吞并了三个邻国。这就是你们表达友好的方式？"

    $ hide_all_chars("servant_generic_img")
    show servant_generic_img at left with dissolve
    envoy "那些小国……不值一提。皇帝陛下感兴趣的，是与贵国建立平等的同盟关系。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "平等？"

    $ hide_all_chars()
    $ hide_all_chars("servant_generic_img")
    show servant_generic_img at left with dissolve
    envoy "当然。毕竟在整个西方，只有您的军事力量值得我们尊重。"

    envoy "您在五年内建立了一支五千人的精锐铁骑。这在军事史上堪称奇迹。"

    envoy "皇帝陛下说——'能让铁骑之主成为朋友，远比让他成为敌人更明智。'"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "转告你的皇帝——我对同盟没有兴趣。"

    player "但如果他的军队敢踏入我的国土一步——"

    player "他将会明白'铁骑之主'这个称号不是浪得虚名。"

    $ hide_all_chars()
    "特使的笑容僵了一瞬，随即更深地鞠了一躬。"

    $ hide_all_chars("servant_generic_img")
    show servant_generic_img at left with dissolve
    envoy "大人果然如传闻中一样……令人敬畏。我会如实转告陛下的。"

    "特使离开后，大厅安静了下来。"

    if elena_romance:
        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve

        elena "你把他吓坏了。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "这正是我想要的效果。"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "……"

        "艾琳娜没有笑。她站在窗边，看着你的眼神和看窗外的雨没什么区别。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "怎么了？"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "你还记得五年前的自己吗？"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "什么意思？"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "五年前，你也曾害怕。你也曾犹豫。你也曾问自己——这样做对不对。"

        elena "但现在……你连一个外交官都要用恐吓的方式来对待。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "这不是恐吓。这是震慑。"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "有什么区别？"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "区别在于——震慑可以避免战争。"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "……也许吧。但你有没有想过——"

        elena "当所有人都害怕你的时候，你身边还会剩下谁？"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "你不是还在这里吗？"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "是。但不是因为你强大。"

        elena "是因为我还记得你害怕的样子。"

        elena "……如果有一天，连你自己都忘了——"

        elena "那权力就真的只是一座空城了。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "……我会记住的。"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "嗯。"

        "她转身离开。脚步声在空荡荡的大厅里回响了很久。"

        hide elena_img with dissolve

    ## —— 第三幕：战场纪念碑 ——

    scene bg battlefield with dissolve

    "黄昏时分。你独自来到了五年前那场大战的旧址。"

    "战场早已被荒草覆盖，但一座巨大的石碑矗立在原野中央。"

    "那是你下令修建的——阵亡将士纪念碑。"

    "碑上刻满了名字。密密麻麻，一行接一行。"

    "你走近，用手指轻轻触碰那些刻痕。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "刘易斯……佩恩……莫根……"

    $ hide_all_chars()
    "你认识其中一些名字。他们曾经是活生生的人——有家人，有梦想，有害怕的事情。"

    "如今，他们只是石碑上一个个冰冷的字。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "三百七十二人。"

    player "三百七十二条命。"

    player "换来了和平。但——"

    player "值得吗？"

    $ hide_all_chars()
    "没有人回答你。只有风声。"

    "你在纪念碑前站了很久，直到夕阳完全沉入地平线。"

    "天色暗了下来。你转身准备离开——"

    "突然，你听到了身后传来一阵急促的脚步声。"

    ## —— 第四幕：孩子的恐惧 ——

    scene bg village with dissolve

    "回去的路经过一个小村庄。"

    "你的护卫已经远远跟在后面——你习惯独行，不喜欢被人包围。"

    "村口，几个孩子正在玩耍。他们用木棍当剑，假装骑士互相比武。"

    "一个扎着辫子的小女孩看到了你——或者更准确地说，看到了你胸甲上的艾登堡徽章。"

    "小女孩的眼睛猛然瞪大。她转身就跑，一边跑一边喊——"

    "\"铁血公爵来了！快跑！\""

    "其他孩子也四散而逃，木棍丢了一地。"

    "村庄一瞬间安静了。门窗紧闭。连狗都不叫了。"

    "你站在空荡荡的村口，一动不动。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    "奥尔德里克不知什么时候赶了上来。他气喘吁吁，拄着拐杖。"

    aldric "大人……您没事吧？"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "……你看到了吗？"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "……是的。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "那个孩子……她跑了。"

    player "她看到我就跑了。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "大人……"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "就像看到了怪物一样。"

    "你闭上眼。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "大人。老朽斗胆说一句。"

    aldric "他们害怕你。就像当年……人们害怕你的祖父一样。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "祖父？"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "老领主——您的父亲——一辈子都在努力让人们忘记他父亲的暴虐。"

    aldric "您父亲说过：'真正的力量不是让人恐惧，而是让人信赖。'"

    aldric "而如今……"

    $ hide_all_chars()
    "老管家没有说完。但你听懂了。"

    "你变成了你祖父的样子。"
    "你的父亲用一生来纠正的错误——你花了五年就重蹈覆辙。"

    hide aldric_img with dissolve

    "你站在村口，身后是一地的木棍和散落的玩具。"

    "夜幕降临。你做出了一个选择——"

    menu:
        "接受这一切。恐惧是秩序的基石。":
            $ epilogue_iron_choice = "accept"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "……让他们怕吧。"

            player "恐惧可以维持和平。父亲的仁慈没能保护他——反而害死了他。"

            player "我不会犯同样的错误。"

            $ hide_all_chars()
            "你转身离开了村庄。步伐沉稳而决绝。"

            "身后，一扇窗户悄悄开了一条缝。一双孩子的眼睛从缝隙中看着你远去的背影。"

            "不是敬仰。"
            "是恐惧。"

            "但你已经不在乎了。"
            "或者说——你逼自己不再在乎。"

        "不。这不是我想要的。必须改变。":
            $ epilogue_iron_choice = "change"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "……不。"

            player "这不是我想要的。"

            player "我拿起剑，是为了保护他们——不是为了让他们害怕我。"

            $ hide_all_chars()
            "你朝村庄里走去。"

            "你敲开了第一扇门。一个颤抖的农妇打开了门。"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "不用怕。我只是……想问问，你们过得好吗？"

            $ hide_all_chars()
            "农妇愣住了。她大概从未想过——那个令人闻风丧胆的铁血公爵会站在她家门口，"
            "用这么温和的语气说话。"

            "\"大人……我们……我们很好……\""

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "如果有什么困难，可以告诉我。我来这里，不是来吓人的。"

            $ hide_all_chars()
            "那天晚上，你在村子里待了很久。"
            "你听了农民们的抱怨，看了他们破旧的房屋，摸了他们龟裂的手。"

            "你用了五年建立了一支铁军。"
            "也许，是时候花一些时间建立别的东西了。"

            "铁可以打造剑。"
            "但也可以打造犁。"


    ## ── 众人的命运 ──

    "五年过去了。你用铁腕重塑了这个王国。而每一个曾站在棋盘上的人，都有了各自的结局。"

    "王后伊莎贝拉——这个名字如今很少被人提起了。"

    if queen_trust:
        "她曾在关键时刻选择与你合作。你记得这一点。"
        "你允许她带少量随从离开王都，隐居到北方的圣灵修道院。她的余生将在祈祷和沉默中度过——体面，但再无翻身之日。"
    else:
        "她从未打算与你合作，你也不打算给她体面的退场。"
        "她被软禁在王都西塔的最高层。每天有人送饭，每月有人记录她的言行。她可以看到窗外的王国——但再也触碰不到。"

    if ch5_exp_queen_ultimatum == "reject":
        "你曾用沉默回应她的最后通牒。如今，沉默也成了她的日常——没有人再听她说话。"
    elif ch5_exp_queen_ultimatum == "accept":
        "她至今相信你当初是真心接受了她的条件。被自己的判断力背叛，比被敌人击败更令人痛苦。"

    "男爵的处置更为务实。"

    if baron_peace_path:
        "他曾在争端中选择和平路线，这为他保住了领地。但你收走了他的军权，拆散了他的私兵。"
        "一个没有爪牙的猛兽，只能老老实实地替你管理税收和道路。他心里清楚，这已经是最好的结局。"
    else:
        "他的领地被一分为三，分给了三个对你忠心的骑士。冯·哈根家族从男爵降为骑士，世袭荣耀一朝归零。"
        "你偶尔会收到他的请愿书——措辞恭敬，满纸卑微。你从不回复。"

    if ch5_exp_baron_response == "blackmail":
        "你手中的把柄至今仍在。他心里清楚——只要你愿意，那些旧事随时可以公之于众。这让他的每一封请愿书都格外卑微。"
    elif ch5_exp_baron_response == "exploit":
        "他至今不知道，你从他自己写的那封威胁信中读出了军事部署。他的狂妄，成了自己覆灭的第一块多米诺骨牌。"

    "至于王子——一个不再构成威胁的前王储。"

    if prince_ally:
        "他曾是你的盟友。你给了他一座乡间庄园和王族的虚衔。"
        "他在那里养马、读书、偶尔写信给你。信里从不谈政治。你知道那是一种默契。"
    else:
        "你将他流放到了东部边境。那里荒凉贫瘠，远离一切权力中心。"
        "他不得返回王都，终身不得。铁腕之下没有例外——哪怕对王族也一样。"

    "暗百合——这个游走在阴影中的组织，在铁腕秩序下没有容身之地。"

    if dark_lily_joined:
        "你将它改编为你的私人情报机构。换了名字，换了旗帜，但保留了那些最有用的人。"
        "他们不再为理想服务，只为你服务。这是铁幕之下唯一被允许存在的阴影。"
    elif dark_lily_destroyed:
        "你早在五年前就将它连根拔起。如今残余势力被彻底清扫，连那个名字都正在被人遗忘。"
    else:
        "你没有加入它，也没有摧毁它——但你的铁腕秩序挤压了它所有的生存空间。"
        "据说他们转入了更深的地下，苟延残喘。但你不在乎。在你建造的世界里，阴影无处藏身。"

    scene black with fade

    centered "{size=+8}铁腕领主 · 尾声{/size}"

    if epilogue_iron_choice == "accept":
        centered "「剑不会生锈，只要你不停地挥舞它。」"
        centered "「但握剑的手——终有一天会疲倦。」"
    else:
        centered "「铁不仅能铸剑，也能铸犁。」"
        centered "「也许，真正的力量不在于摧毁，而在于重建。」"

    pause 2.0

    return

## ============================================================
## 结局三：影之王 - 扩展尾声
## The Shadow King Epilogue
## ============================================================

label ending_shadow_epilogue:

    scene black with fade

    centered "{size=+10}五年后{/size}"
    centered "{size=+6}王历二十七年·秋夜{/size}"

    pause 1.0

    ## —— 第一幕：幕后之手 ——

    scene bg throne_room with dissolve

    "王座之上坐着一个你精心挑选的傀儡——哈特伯爵。"

    "他面容和善，声音洪亮，深受百姓爱戴。"
    "一个完美的门面。"

    "而你——站在王座后方的屏风之后，透过镂空的花纹，注视着这一切。"

    "\"哈特伯爵\"向大臣们宣布了新的政令——降低南方省份的赋税。"
    "这个政令是你昨晚写的。哈特只是照本宣科。"

    "大臣们纷纷赞颂伯爵的英明。"
    "没有人知道——这个王国真正的主人，就站在他们身后几步之遥。"

    "会议结束。大臣们鱼贯而出。"

    "你从屏风后走出来。"

    "\"哈特伯爵\"连忙站起，恭恭敬敬地让出了位置。"

    "\"大人。今天的表演……还满意吗？\""

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "不错。但你在宣读第三条政令时犹豫了一下。下次注意。"

    $ hide_all_chars()
    "\"是，大人。\""

    "你挥了挥手，他退了出去。"

    "空荡荡的王座大厅里只剩下你一个人。"

    "你走到王座前，用手轻轻触碰了一下扶手——但没有坐下。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "坐上去太显眼了。"

    if dark_lily_joined:
        $ hide_all_chars()
        "你转身走向暗门。一条只有你知道的密道通向你真正的'办公室'——"
        "城堡地下深处的暗百合总部。"

        scene bg study with dissolve

        "地下密室里弥漫着潮湿的石灰味。"

        "墙上挂着一张巨大的地图，上面插满了红色和蓝色的小旗。"
        "红旗代表暗百合的据点。蓝旗代表需要监视的目标。"

        "五年来，暗百合的网络已经遍布整个王国——甚至延伸到了邻国。"

        "每一座城市都有你的耳目。每一个权贵的秘密都在你的档案柜里。"
        "商人、贵族、教士、将军——他们的弱点、欲望、恐惧，你全都一清二楚。"

        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "今天的报告。"

        "一个无声无息出现在你身后的黑衣人递上一叠羊皮纸。"

        player "……北方的伯爵夫人与敌国使者秘密接触。把证据保存好，先不动她。"

        player "南方的银行家在走私禁运物资。切断他的供货渠道，让他自己来求我。"

        player "东部边境有一支来历不明的雇佣兵——查清他们的雇主。"

        $ hide_all_chars()
        "你一条一条地下达指令。冷静、精准、毫无犹豫。"

        "整个王国就像一台精密的机器，而你是唯一掌握所有齿轮的人。"

        if lily_double_agent:
            "而你最得意的棋子——是那个双面间谍。"
            "当年你把一个叛徒变成了一枚暗棋。五年来，她在敌我之间穿梭，为你传递了无数改变格局的情报。"
            "没有人知道她的真实效忠对象。包括她自己——也许连她也不确定了。"

    else:
        "你转身走向暗门。一条只有你知道的密道通向你真正的'办公室'——"
        "城堡最深处的秘密情报室。"

        scene bg study with dissolve

        "地下密室的空气沉闷而阴冷。"

        "墙上挂着一张巨大的地图，上面插满了红色和蓝色的小旗。"
        "红旗代表你的情报据点。蓝旗代表需要监视的目标。"

        "五年来，你亲手编织的情报网已经遍布整个王国——甚至延伸到了邻国。"

        "每一座城市都有你收买的线人。每一个权贵的秘密都在你的档案柜里。"
        "商人、贵族、教士、将军——他们的弱点、欲望、恐惧，你全都一清二楚。"

        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "今天的报告。"

        "一个无声无息出现在你身后的黑衣人递上一叠羊皮纸。"

        player "……北方的伯爵夫人与敌国使者秘密接触。把证据保存好，先不动她。"

        player "南方的银行家在走私禁运物资。切断他的供货渠道，让他自己来求我。"

        player "东部边境有一支来历不明的雇佣兵——查清他们的雇主。"

        $ hide_all_chars()
        "你一条一条地下达指令。冷静、精准、毫无犹豫。"

        "整个王国就像一台精密的机器，而你是唯一掌握所有齿轮的人。"


    ## —— 第二幕：爱人的质问 ——

    if elena_romance:
        scene bg palace_garden with dissolve

        "午夜。你从密室出来，走进了城堡后面的花园。"

        "暗中，一个身影靠在石柱上。"

        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve

        elena "又是一个不睡觉的夜晚？"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "你也没睡。"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "因为我在等你。"

        $ hide_all_chars()
        "她转过身。你等眼睛适应了黑暗才看清她的脸。"
        "美丽——但不再像从前那样明亮。有什么东西在她眼底，像一潭深水。"

        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "我有话要对你说。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "说。"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "你变了。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "人都会变。"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "不是这种变法。"

        "她走到你面前，直视着你的眼睛。"

        elena "五年前，你是一个为了真相可以赌上一切的人。"

        elena "你说过——你不想活在谎言里。你不想成为操纵别人的人。"

        elena "现在呢？"

        elena "你操纵着整个王国。你用谎言编织了一张巨大的网。"

        elena "你变成了你最恨的人。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "……我变成了一个能保护所有人的人。"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "保护？你把这叫保护？"

        elena "你连吃饭都要先让人试毒。你连睡觉都要在枕头下藏一把刀。"

        elena "你信任谁？你还信任谁？"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "我信任你。"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "……"

        elena "可我不信任你了。"

        "这句话像一把刀。"

        elena "不是因为你做了什么对不起我的事。"

        elena "是因为——我不知道你对我说的哪些话是真的，哪些是……'策略'。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "艾琳娜……"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "你不需要解释。我只是……累了。"

        elena "我陪你走了五年。但我发现——你走的路越来越暗，我已经看不见前方了。"

        "她转身，朝花园深处走去。"

        elena "我不会离开你。但我需要你回答一个问题。"

        elena "你控制了整个王国——但你控制得了你自己吗？"

        "她沿着花园小径走远了，脚步声渐渐被夜虫的叫声盖过。"

        hide elena_img with dissolve

        $ hide_all_chars()
        "你站在花园里，一个人。"
        "月亮很亮。但你的影子很长。"

    else:
        "午夜。你从密室出来，独自走进了花园。"

        "月光很亮。夜风很冷。"

        "你想不起上一次和人说真心话是什么时候了。"

        "在这个世界上，你控制着一切——除了你自己内心深处那个越来越模糊的声音。"

    if dark_lily_joined:
        ## —— 第三幕：影之传承 ——

        scene bg study with dissolve

        "第二天。密室里来了一个意想不到的访客。"

        $ hide_all_chars("lily_master_img")
        show lily_master_img at left with dissolve

        $ hide_all_chars()
        "暗百合的上一任首领——老影主。"

        "你已经五年没有见过这个人了。"
        "当年是她把暗百合的权力交给了你，然后像影子一样退出了所有人的视野。"

        "如今她再次出现——但已经不是你记忆中的样子了。"

        "她消瘦憔悴，脸色灰白，走路时要扶着墙壁。"
        "曾经那个翻手为云、覆手为雨的影中之主，如今看上去像一阵风就能吹倒。"

        $ hide_all_chars("lily_master_img")
        show lily_master_img at left with dissolve
        lily_master "好久不见了……小影主。"

        hide lily_master_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "你怎么来了？"

        hide player_char_img
        $ hide_all_chars("lily_master_img")
        show lily_master_img at left with dissolve
        lily_master "来看看我的继承人。"

        "她环顾四周，看着墙上的地图、桌上的文件、角落里的暗器架。"

        lily_master "做得不错。比我当年强多了。"

        hide lily_master_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "你不是来夸我的吧。"

        hide player_char_img
        $ hide_all_chars("lily_master_img")
        show lily_master_img at left with dissolve
        lily_master "不是。我是来……告别的。"

        "她缓缓坐下，喘了好一阵气。"

        lily_master "大夫说我活不过这个冬天。"

        hide lily_master_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "……"

        hide player_char_img
        $ hide_all_chars("lily_master_img")
        show lily_master_img at left with dissolve
        lily_master "别摆出那副表情。我们这行的人，能死在床上就算幸运了。"
        lily_master "我来，是想亲眼确认一件事——"

        lily_master "我选对了继承人。"

        "她看着你，浑浊的眼睛里闪过一丝光。"

        lily_master "我选对了。"

        lily_master "暗百合在你手里，比在任何人手里都强大。"

        lily_master "你做到了我做不到的事——你让影子有了形状，有了秩序，有了……目的。"

        hide lily_master_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "我只是做了该做的事。"

        hide player_char_img
        $ hide_all_chars("lily_master_img")
        show lily_master_img at left with dissolve
        lily_master "该做的事……"

        "老影主笑了。那笑容苍老而苦涩。"
        lily_master "你知道吗？我年轻的时候也这么说。"

        lily_master "'该做的事。'这四个字害了多少人，你知道吗？"

        lily_master "包括我自己。"

        hide lily_master_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "你后悔了？"

        hide player_char_img
        $ hide_all_chars("lily_master_img")
        show lily_master_img at left with dissolve
        lily_master "后悔？不。后悔是弱者的奢侈。"

        lily_master "但如果能重来……我会选一条有光的路。"

        "她站起来，摇摇晃晃地走向门口。"

        lily_master "小影主。记住一句话——"

        lily_master "影子之所以存在，是因为有光。如果光灭了……影子也就没有意义了。"

        "她没有回头。"

        hide lily_master_img with dissolve

    else:
        ## —— 第三幕：暗影的代价 ——

        scene bg study with dissolve

        "第二天。密室里来了一个意想不到的访客。"

        $ hide_all_chars("aldric_img")
        show aldric_img at left with dissolve

        $ hide_all_chars()
        "你的老师——退休的间谍大师奥尔德里克。"

        "五年前，是他教会你情报战的一切技巧——伪装、渗透、信息操控。"
        "你在他的基础上建立了如今遍布王国的情报帝国。"

        "如今他再次出现——但已经不是你记忆中的样子了。"

        "他消瘦憔悴，脸色灰白，走路时要扶着拐杖。"
        "曾经那个精明干练的间谍，如今看上去风烛残年。"

        $ hide_all_chars("aldric_img")
        show aldric_img at left with dissolve
        aldric "好久不见了……我的学生。"

        hide aldric_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "你怎么来了？"

        hide player_char_img
        $ hide_all_chars("aldric_img")
        show aldric_img at left with dissolve
        aldric "来看看我教出来的人。"

        "他环顾四周，看着墙上的地图、桌上的文件、角落里的密码本。"

        aldric "做得不错。比我当年强多了。"

        hide aldric_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "你不是来夸我的吧。"

        hide player_char_img
        $ hide_all_chars("aldric_img")
        show aldric_img at left with dissolve
        aldric "不是。我是来……告别的。"

        "他缓缓坐下，喘了好一阵气。"

        aldric "大夫说我活不过这个冬天。"

        hide aldric_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "……"

        hide player_char_img
        $ hide_all_chars("aldric_img")
        show aldric_img at left with dissolve
        aldric "别摆出那副表情。我们这行的人，能死在床上就算幸运了。"
        aldric "我来，是想亲眼确认一件事——"

        aldric "我没有看错人。"

        "他看着你，浑浊的眼睛里闪过一丝光。"

        aldric "我没有看错。"

        aldric "你的情报网，比任何组织都更精密、更高效。"

        aldric "你做到了我做不到的事——你不依靠任何组织，只凭自己的智慧和意志，编织了一张覆盖整个王国的网。"

        hide aldric_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "我只是做了该做的事。"

        hide player_char_img
        $ hide_all_chars("aldric_img")
        show aldric_img at left with dissolve
        aldric "该做的事……"

        "老人笑了。那笑容苍老而苦涩。"
        aldric "你知道吗？我年轻的时候也这么说。"

        aldric "'该做的事。'这四个字害了多少人，你知道吗？"

        aldric "包括我自己。"

        hide aldric_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "你后悔了？"

        hide player_char_img
        $ hide_all_chars("aldric_img")
        show aldric_img at left with dissolve
        aldric "后悔？不。后悔是弱者的奢侈。"

        aldric "但如果能重来……我会选一条有光的路。"

        "他站起来，摇摇晃晃地走向门口。"

        aldric "记住一句话——"

        aldric "影子之所以存在，是因为有光。如果光灭了……影子也就没有意义了。"

        "他没有回头。"

        hide aldric_img with dissolve


    $ hide_all_chars()
    "门关上了。密室里只剩下你一个人。"

    ## —— 第四幕：父亲的信 ——

    "你打开了书桌最底层的抽屉——那里放着一封你从未拆开的信。"

    if dark_lily_joined:
        "那是父亲的遗信。在你继承暗百合的那天发现的。"
    else:
        "那是父亲的遗信。在你开始建立情报网的那天发现的。"
    "你一直没有勇气打开它。因为你知道里面写了什么。"

    "今天，你终于拆开了。"

    "信纸已经泛黄，但父亲端正的字迹依然清晰——"

    centered "「我的孩子：」"
    centered "「如果你读到这封信，说明我已经不在了。」"
    centered "「我不知道你会走上怎样的路。但有一件事我必须告诉你——」"
    centered "「不要走我的路。」"
    centered "「我曾经以为可以用阴影来对抗阴影。」"
    centered "「结果，我变成了阴影的一部分。」"
    centered "「我失去了朋友，失去了信任，最后连自己的命也搭了进去。」"
    centered "「孩子，光明的路也许更难走。但至少——」"
    centered "「你不会迷路。」"

    "你把信放下。"

    "密室里很安静。只有蜡烛在轻轻跳动。"

    if dark_lily_joined:
        hide lily_master_img
    else:
        hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "父亲。"

    player "你说不要走你的路。"

    player "……对不起。"

    $ hide_all_chars()
    "你看了看四周——地图、暗器、密码本、情报卷宗。"

    "这就是你的世界。一个没有阳光的世界。"

    "你走到了你父亲曾经走过的同一条路的尽头。"
    "甚至走得更远。"

    "这是不是一种……悲剧？"

    "还是一种宿命？"

    "你不知道。你只是把信叠好，放回了抽屉。"

    "然后吹灭了蜡烛。"

    "黑暗中，你闭上了眼。"


    ## ── 棋盘上的棋子们 ──

    "你坐在黑暗中，回顾着棋盘上每一枚棋子的位置。"

    "王后伊莎贝拉——她以为自己仍然掌握着这个王国。"

    if queen_trust:
        "她曾信任你，如今她隐约感到有些事情不对。政令总是恰好符合你的利益，反对她的声音总是在关键时刻消失。"
        "她偶尔会在深夜惊醒，觉得自己像一只被丝线牵着的木偶。但她永远找不到那根线——因为那根线，就是她以为的'信任'。"
    else:
        "她从未信任过你，这反而让你的工作更简单。她把所有注意力放在防备明面上的敌人，完全没有意识到真正的操控来自暗处。"
        "她以为自己赢了。这是最讽刺的部分。"

    "冯·哈根男爵——曾经的暗焰首领，如今是你档案柜里最厚的一份卷宗。"

    if baron_peace_path:
        "你没有动他。你让他继续经营他的领地、继续他的小动作。"
        "他不知道的是，他身边的管家、他的信使、甚至他最宠信的副官——都在向你汇报。温水煮青蛙，是你最擅长的手法。"
    else:
        "你手里握着足以送他上绞刑架的证据——三份，分别藏在三个他永远找不到的地方。"
        "他知道你有把柄，但不知道有多少。这种恐惧比锁链更有效。他如今是你最听话的棋子，每一步都走在你画好的格子里。"

    "弗雷德里克王子——在你所有的棋子中，他是最好用的一枚。"

    if prince_betrayed:
        "你曾假意结盟，然后在最关键的时刻将他出卖给王后。他被捕入狱时脸上的表情——不是愤怒，而是不可置信。"
        "但即便是背叛，也是精心计算的一步棋。他的倒下为你换来了王后的信任——那才是真正的筹码。"
    elif prince_ally:
        "他以为你是朋友。你确实对他不错——在他需要帮助时伸出手，在他迷茫时给出建议。"
        "他不知道的是，每一次'帮助'都经过精心计算，每一条'建议'都通向你需要的方向。最残酷的操控，是让对方心怀感激。"
    else:
        "你让精心操纵的信息流一步步将他逼入死角。退路被堵死，盟友被策反——最后他'自愿'退出了权力角逐。"
        "他以为是命运弄人。他不知道命运有一个名字。"

    scene black with fade

    centered "{size=+8}影之王 · 尾声{/size}"
    centered "「在最深的黑暗中，你以为自己在操控一切。」"
    centered "「但也许——是黑暗在操控着你。」"

    pause 2.0

    return

## ============================================================
## 结局四：圣者守护 - 扩展尾声
## The Holy Guardian Epilogue
## ============================================================

label ending_faith_epilogue:

    scene black with fade

    centered "{size=+10}五年后{/size}"
    centered "{size=+6}王历二十七年·复活节{/size}"

    pause 1.0

    ## —— 第一幕：真理骑士团 ——

    scene bg church with dissolve

    "管风琴的旋律在教堂穹顶下回荡。"

    "阳光透过彩色玻璃窗洒下，在石板地面上投射出斑斓的光影。"
    "圣母像前，十二个年轻人单膝跪地，等待着神圣的时刻。"

    "你——真理骑士团的创立者，站在圣坛之前，手持受祝的长剑。"

    "五年前，你选择了信仰的道路。"
    "不是宗教的盲从，而是对善与正义的坚定信念。"

    "你创建了真理骑士团——一群誓死保护弱者、揭露腐败的骑士。"
    "他们不效忠于任何领主，只效忠于真理本身。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你们即将宣誓成为真理骑士。这不仅仅是一个头衔——"

    player "这是一份承诺。一份用余生去兑现的承诺。"

    player "你们将保护无力自保的人。你们将揭露被掩埋的真相。"

    player "你们将在黑暗中举起火把，即使那火光只够照亮一步的路。"

    player "你们准备好了吗？"

    $ hide_all_chars()
    "\"我们准备好了！\""

    "你举起长剑，依次触碰每个人的肩膀。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "以真理之名，以正义之名，以你们心中不灭的光——"

    player "起立吧，真理骑士。"

    "十二个年轻人站了起来。教堂里响起了庄严的颂歌。"

    hide player_char_img
    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve

    "主教马修斯——已经八十多岁了。他坐在教堂角落的轮椅上，颤巍巍地鼓着掌。"

    bishop "好……好啊……"

    "典礼结束后，你走到老主教身边。"

    hide bishop_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "主教大人，感觉如何？"

    hide player_char_img
    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "老了……眼花了……但今天这一幕，我看得清清楚楚。"

    bishop "你做到了我一辈子想做而做不到的事。"

    hide bishop_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "这也是您的功劳，主教大人。没有您的教导，就没有今天的骑士团。"

    hide player_char_img
    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "不……功劳是你的。"

    "老主教握住你的手，力气已经很小了，但那份郑重让你动容。"

    bishop "这是我的赎罪。"

    hide bishop_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "赎罪？"

    hide player_char_img
    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "当年你父亲遇害……我知道真相，却选择了沉默。"

    bishop "我害怕了。我以为沉默可以保全自己和教会。"

    bishop "但沉默是罪。比谎言更大的罪。"

    bishop "如今……看到这些年轻人立誓要打破沉默——"

    bishop "我终于觉得……上帝或许会原谅我了。"

    "他的声音颤抖着，浑浊的泪水顺着深深的皱纹流了下来。"

    hide bishop_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "上帝一定会的，主教大人。"

    hide bishop_img with dissolve

    ## —— 第二幕：父亲的大教堂 ——

    scene bg castle_exterior with dissolve

    "艾登堡的山坡上，一座宏伟的大教堂正在拔地而起。"

    "你给它起了一个名字——卡尔大教堂。"
    "以你父亲的名字命名。"

    "这不是一座普通的教堂。"
    "它的设计融合了东方和西方的建筑风格，有着高耸入云的尖塔和温暖的木质内饰。"
    "教堂的大门永远向所有人敞开——无论贫富贵贱，无论信仰深浅。"

    "今天，你亲自到工地监督施工。"

    "工人们在你身边忙碌着——搬石头、搅灰浆、安装彩色玻璃。"
    "有人在唱赞美诗。歌声在山谷中回荡，和着锤子敲击石头的节奏。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "东翼的穹顶还需要加固。冬天的雪很重，不能有任何隐患。"

    $ hide_all_chars()
    "\"是，大人！\""

    "你蹲下身，检查一块基石的接缝。"

    "\"大人，您不用亲自动手的……\""

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我父亲说过——'如果你不亲手触摸泥土，你就不会理解脚下的大地。'"

    if elena_romance:
        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve

        elena "泥巴都糊到脸上了，公爵大人。"

        "艾琳娜递过来一块手帕。她的表情带着一丝无奈，但嘴角是笑的。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "谢谢。你今天来得早。"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "我来看看进度。顺便……想和你说些事。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "什么事？"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "你知道我不信上帝。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "我知道。"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "但这五年来……看你做的这一切——"

        elena "骑士团、大教堂、孤儿院、流浪者收容所——"

        elena "我虽然不信上帝，但我信你。"

        elena "如果信仰能让一个人变成你这样——那也许信仰本身并不重要。"

        elena "重要的是……它让你成为了一个什么样的人。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "艾琳娜……"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "别感动了。走吧，今天还有三车石材等着验收呢。"

        "你笑了。她总是这样——在最深情的时刻用最实际的话来收尾。"

        elena "对了。晚上别忘了回家吃饭。你已经连续三天在工地过夜了。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "好。"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "你上次也这么说的。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "这次是真的。"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "……信你一次。"

        $ hide_all_chars()
        "她的笑容在阳光下很温暖。"
        "你们的爱不是轰轰烈烈的传奇。"
        "但就像这座正在建造的教堂——一砖一瓦，日积月累，坚不可摧。"

        hide elena_img with dissolve

    ## —— 第三幕：孤儿的提问 ——

    scene bg church with dissolve

    "傍晚。教堂的临时礼拜堂里，几个孤儿在蜡烛光下安静地读书。"

    "你创办的孤儿院就在教堂旁边。这些孩子——有的失去了父母，有的被遗弃。"
    "你给了他们一个家，一个名字，一个未来。"

    "一个七八岁的男孩走到你面前。他有一双很大很亮的眼睛。"

    "\"大人……我可以问你一个问题吗？\""

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "当然可以。"

    $ hide_all_chars()
    "男孩犹豫了一下，然后鼓起勇气——"

    "\"上帝真的存在吗？\""

    "教堂里安静了。其他孩子也抬起头，好奇地看着你。"

    "你看着孩子们仰起的脸。窗外的阳光正好照进教堂，把他们的头发染成金色。"

    menu:
        "\"是的。上帝存在，他一直在看着我们。\"":
            $ epilogue_faith_answer = "yes"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "是的。上帝存在。"

            player "你看不见他，摸不到他。但你能感受到他。"

            player "当你在黑暗中害怕时，心里那个告诉你'不要怕'的声音——那就是他。"

            player "当你看到别人受苦，心里那份不忍——那也是他。"

            player "他不在天上。他在你心里。在每一个善良的念头里。"

            $ hide_all_chars()
            "男孩想了想，点了点头。"

            "\"那……他为什么不帮我妈妈？妈妈生病的时候，我每天都祈祷。但她还是走了。\""

            "你蹲下身，和他平视。"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我不知道。"

            player "但我知道——你的妈妈一定也在某个地方看着你。"

            player "就像上帝一样。看不见，但一直都在。"

            $ hide_all_chars()
            "男孩的眼睛红了。但他没有哭。他只是紧紧抱住了你。"

        "\"我不知道。但善良是真实的。\"":
            $ epilogue_faith_answer = "goodness"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "老实说……我不知道。"

            player "这个问题太大了，连最聪明的人都回答不了。"

            player "但有一件事我可以确定——善良是真实的。"

            player "你帮助别人时的快乐是真实的。你被别人帮助时的感动是真实的。"

            player "也许上帝就藏在这些真实的东西里面。也许不是。"

            player "但不管上帝存不存在——做一个善良的人，永远不会错。"

            $ hide_all_chars()
            "男孩歪着头想了一会儿。"

            "\"那……善良也会消失吗？就像我妈妈一样？\""

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "不会。善良不会消失。"

            player "你妈妈对你的爱——那份善良——现在就在你心里。"

            player "只要你记得她，善良就会一直存在。"

            $ hide_all_chars()
            "男孩低下头，小声说了一句：'我会记得的。'"

        "\"答案在你自己心里。\"":
            $ epilogue_faith_answer = "heart"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "这是一个很好的问题。我很高兴你敢问。"

            player "但这个问题的答案——不在我这里。"

            player "它在你心里。"

            player "你慢慢长大，会读很多书，见很多人，经历很多事。"

            player "总有一天，你会找到属于你自己的答案。"

            player "到时候——不管答案是什么——记得要对自己诚实。"

            $ hide_all_chars()
            "男孩眨了眨大眼睛。"

            "\"可是……如果我找到的答案和别人不一样呢？\""

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "那就更好了。真理从来不害怕不同的声音。"

            player "记住——永远不要因为害怕而放弃思考。"

            $ hide_all_chars()
            "男孩认真地点了点头。\"我记住了。\""

    "你摸了摸男孩的头。蜡烛的光芒柔和而温暖。"

    "窗外，夕阳正在西沉。"

    ## —— 第四幕：晚祷 ——

    scene bg church with dissolve

    "孩子们都回去睡了。教堂里只剩你一个人。"

    "你跪在圣坛前，双手合十。"

    "彩色玻璃窗在夕阳的余晖中绽放出最后一抹绚丽的光芒。"
    "红的、蓝的、金的——投射在你的身上、你的手上、你的脸上。"

    "你闭上眼，感受着光的温度。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "……"

    $ hide_all_chars()
    "你不知道该说什么。"
    "五年来你说过无数次祈祷词，但此刻——"
    "你只是静静地跪着。"

    "教堂外面传来了风声，像是远方的歌。"

    "你想起了父亲。想起了那些在黑暗中挣扎的日子。"
    "想起了背叛和阴谋。想起了鲜血和眼泪。"

    "然后——你想起了今天那个男孩的眼睛。"
    "大大的，亮亮的。充满了对世界最朴素的好奇。"

    "在那双眼睛里，没有恐惧，没有仇恨，没有阴谋。"
    "只有——一个简单的问题。"

    "也许这就是答案。"

    "不是某本经书里写的答案。"
    "而是一个孩子敢于提问的勇气本身——就是答案。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "在所有的结局中，这个最安静。"

    player "也许……这就够了。"

    $ hide_all_chars()
    "你站起身，走出了教堂。"

    "外面，暮色四合。第一颗星星出现在天际。"
    "空气中弥漫着山花的清香和远处农舍飘来的炊烟味道。"

    "你抬头看了一眼天。"

    "和平不是没有痛苦。但和平意味着——痛苦之后，还有治愈的可能。"

    "你慢慢走下台阶，朝着正在建造中的大教堂的方向走去。"

    "它还没有完工。"
    "但轮廓已经显现——高耸、庄严、充满希望。"

    "就像信仰本身一样。"
    "永远在建造中。永远不会完工。"
    "但每一块砖，都值得。"


    ## ── 和平之后 ──

    "和平不是童话。和平是每一个人在新秩序中重新寻找自己的位置。"

    "和平协议签署的那一天，王后在羊皮纸上按下了印章。"

    if queen_trust:
        "她保留了王后的头衔和宫殿，但交出了军权和任命权。她成为和平的象征——一座被修剪过的花园。"
        "你偶尔会在教堂遇见她。她的眼神复杂，但再没有了当年的冰冷。也许，她也在学着接受。"
    else:
        "她被迫签下了每一条款项。笔锋用力过重，羊皮纸差点被划破。"
        "她保留了头衔，但所有人都知道那只是空壳。她的不甘写在每一道皱纹里——但大势已去，再多的不甘也翻不起浪花。"

    "男爵在新秩序中找到了自己的位置——虽然未必是他想要的。"

    if baron_peace_path:
        "他成为了南部地区的自治代表。少了军权，多了责任。他偶尔抱怨文书工作太多，但你注意到他治下的税收从未拖欠。"
        "和平给了他另一种活法。他是否感激，你不知道。你只知道他不再是敌人了。"
    else:
        "他在改革条约上签了字，但所有人都看得出他心不甘情不愿。"
        "他在私下仍有怨言，偶尔在酒后念叨'旧日的好时光'。但怨言终究只是怨言。他没有力量翻盘，也没有勇气再赌一次。"

    "王子获得了他很久以来最稀缺的东西——第二次机会。"

    if prince_ally:
        "在教会的庇护下，他重新开始学习治国之道。不是宫廷的权谋术，而是真正的治理——倾听、权衡、妥协。"
        "他偶尔会写信给你，问一些关于信仰和责任的问题。那些信越来越成熟。你看到了变化的可能。"
    else:
        "他主动请求去西部边境领地。那里贫穷、偏远，但没有阴谋。"
        "他说他想赎罪。能不能做到是另一回事——他迈出了第一步。新生总是从承认错误开始的。"

    "暗百合——光照之处，阴影自然消散。"

    if dark_lily_joined:
        "你花了两年时间说服他们。最终，他们放下了面具和暗号，转型为一个公开的商业行会。"
        "有些老成员不愿意。但更多的人选择了走进阳光。地下的理想，终于有了地面的形状。"
    elif dark_lily_destroyed:
        "它已经不存在了。在你建立真理骑士团之前，它就已经消亡。如今没有人再提起那个名字。"
    else:
        "没有人去清剿它，但也没有人再需要它。在一个真相可以公开说出的世界里，暗影中的守护者失去了存在的意义。"
        "据说它在慢慢萎缩。不是被消灭，而是被和平本身吸收了。"

    scene black with fade

    centered "{size=+8}圣者守护 · 尾声{/size}"
    centered "「在所有喧嚣的结局中，这是最安静的一个。」"
    centered "「没有铁骑，没有阴谋，没有王座。」"
    centered "「只有一座未完工的教堂，和一颗永远在追问的心。」"
    centered "「也许，这就够了。」"

    pause 2.0

    return

## ============================================================
## 结局五：民之守护者 - 扩展尾声
## The People's Lord Epilogue
## ============================================================

label ending_peoples_epilogue:

    scene black with fade

    centered "{size=+10}五年后{/size}"
    centered "{size=+6}王历二十七年·丰收节{/size}"

    pause 1.0

    ## —— 第一幕：丰收的喜悦 ——

    scene bg village with dissolve

    "艾登堡的秋天，是金色的。"

    "稻田翻滚着金色的波浪。果园里苹果压弯了树枝。"
    "空气中弥漫着新鲜面包和苹果酒的香味。"

    "今天是丰收节——艾登堡一年中最热闹的日子。"

    "五年前，这里还是一片凋敝。战争的阴影笼罩着每一个家庭。"
    "但如今——艾登堡已经成为了整个王国最富庶、最和平的领地。"

    "不是因为铁骑。不是因为阴谋。"
    "是因为你选择了一条最简单、也最困难的路——"
    "用心治理，真诚待民。"

    "广场上，人们在跳舞。提琴手拉着欢快的曲子。"
    "孩子们在大人腿间穿梭嬉闹，老人们坐在长椅上笑眯眯地看着一切。"

    "你——不再穿着铠甲，不再带着随从。"
    "一身普通的亚麻衣服，混在人群中间，端着一杯苹果酒。"

    "\"大人！来跳舞吧！\""

    "一个红脸的农妇拉住你的手，不由分说地把你拖进了舞池。"

    "你哈哈大笑，跟着音乐的节奏笨拙地转了两圈。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "等等——我不会这个步子——"

    $ hide_all_chars()
    "\"不要紧！跟着节拍就好！\""

    "周围的人都笑了。不是嘲笑——是那种看到一个朋友出糗时，发自内心的快乐。"

    "你也笑了。这种笑——在王城的大厅里，在御前会议上，你永远不会有。"

    if built_school:
        "丰收节的节目之一——是孩子们的诗朗诵。"

        "你五年前建造的学堂，如今已经培养出了一批能识字、能算数的孩子。"
        "这在整个王国都是罕见的。"

        "一个扎着两条辫子的小女孩站在台上，手里拿着一张皱巴巴的纸。"
        "她紧张地清了清嗓子——"

        "\"这首诗叫……《我们的领主》。\""

        "\"他不穿金甲，不骑白马，\""
        "\"他走在田埂上，鞋上沾满了泥巴。\""
        "\"他问我们吃得饱不饱，\""
        "\"问奶奶的腰还疼不疼。\""
        "\"他给我们建了学堂，\""
        "\"让我能读书，能写字，能念诗。\""
        "\"有人问我长大想当什么，\""
        "\"我说——我想当一个像领主大人一样的人。\""

        "台下一片掌声和笑声。"

        "你站在人群后面，用力忍住了眼眶中的热意。"

        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "……这比什么公爵头衔都值钱。"

    if built_clinic:
        $ hide_all_chars()
        "丰收节的另一个亮点——是诊所新馆的落成仪式。"

        "五年前你建造的简陋诊所，如今已经扩建成了一座正式的医馆。"

        "主治医师玛格丽特——五年前还在简陋诊所里独自撑着——"
        "如今已经成为远近闻名的名医，她亲手培训了五个新的医师。"

        "\"玛格丽特大夫\"" "大人，新馆今天正式开业！我想请您剪彩。"

        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "剪彩？我又不是什么大人物。"

        "\"玛格丽特大夫\"" "在艾登堡，您是最大的人物。"

        player "好吧。不过剪完彩你得帮我看看膝盖。跳舞跳伤了。"

        "\"玛格丽特大夫\"" "……大人，您今年才二十多岁。"

        player "所以呢？"

        $ hide_all_chars()
        "\"玛格丽特大夫\"" "所以您的膝盖不是伤了，是缺乏锻炼。"

        "周围的人都笑了。你也笑了。"

        "这就是你想要的艾登堡。不是一个所有人都战战兢兢的地方。"
        "而是一个可以开玩笑、可以犯傻、可以做自己的地方。"

    ## —— 第二幕：奥尔德里克的告别 ——

    scene bg palace_garden with dissolve

    "丰收节的喧嚣渐渐远去。"

    "你来到了城堡后面的花园。这里有一间小屋——你特意为奥尔德里克准备的。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    $ hide_all_chars()
    "老管家坐在门前的摇椅上，膝盖上盖着一条毛毯。"
    "他的白发在秋风中轻轻飘动。面前放着一杯已经凉了的茶。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "大人……您来了。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "丰收节不去凑热闹？"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "腿不行了。坐着听听热闹就够了。"

    "你在他身边坐下。花园里的菊花开得正艳。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "奥尔德里克，我做了一个决定。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "嗯？"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你从今天起退休。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "退……退休？"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你已经七十多岁了。够了。够了。"

    player "我给你准备了这间小屋。有花园，有菜地，有一棵苹果树。"

    player "你不用再操心任何事了。你可以种花，可以晒太阳，可以——"

    player "好好休息。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "大人……我……"

    "老管家的嘴唇颤抖着。他努力说些什么，但话到嘴边就碎成了零散的音节。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你跟了我父亲三十年，又跟了我五年。三十五年了。"

    player "三十五年，你没有请过一天假。没有为自己做过一件事。"

    player "是时候了，奥尔德里克。你值得拥有自己的生活。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "……三十六年。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "什么？"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "是三十六年。不是三十年。"

    aldric "我四十岁那年进了卡尔大人的家门。到今年……三十六年了。"

    "他看着自己枯瘦的双手，嘴角慢慢浮起一个笑容。"

    aldric "三十六年了。"

    aldric "我终于可以种花了。"

    $ hide_all_chars()
    "他的声音很轻。但每一个字都像一颗种子，落在你心里。"

    "你没有说话。你只是把手搭在他的肩上。"

    "老管家再也忍不住，浑浊的泪水顺着满是皱纹的脸颊流了下来。"
    "他哭得像一个孩子——虽然他已经七十七岁了。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "大人……谢谢您。"

    aldric "能在这里看着您长大……能看到艾登堡变成今天的样子……"

    aldric "老朽这辈子……值了。真的值了。"

    if aldric_will_fight:
        aldric "那天在城墙上——我说过要为您而战。您还记得吗？"
        hide aldric_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "我记得。你扛着剑站在弓手旁边，比谁都认真。"
        hide player_char_img
        $ hide_all_chars("aldric_img")
        show aldric_img at left with dissolve
        aldric "那是我这辈子做过最骄傲的事。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "值了。"

    $ hide_all_chars()
    "秋风卷起几片花瓣，落在老管家的膝盖上。"

    "他笑着拂去花瓣，像是在整理一件很珍贵的东西。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "大人……有一件事我一直没说。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "嗯？"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "您的父亲……去世前的最后一句话是说给我听的。"

    aldric "他说——'照顾好我的孩子。他比我想象的更坚强。'"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "……"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "他说对了。您确实比他想象的更坚强。"

    aldric "不——比我们所有人想象的都更坚强。"

    "你转过脸去，不让老管家看到你红了的眼眶。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "……去种你的花吧，老头子。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "嗯。我会种很多。每一朵都用您和老领主的名字来命名。"

    $ hide_all_chars()
    "你站起身，拍了拍他的肩膀，然后转身离开。"

    "走了几步，你回头看了一眼——"

    "老管家已经站起来，颤巍巍地走向花园的角落。"
    "他弯下腰，开始翻土。"

    "阳光洒在他弯曲的背上。"
    "三十六年的忠诚，终于迎来了一个温柔的句号。"

    hide aldric_img with dissolve

    ## —— 第二幕半：花园另一头 ——

    "你转身，准备走回大厅。"

    "走到拐角时，你停下了脚步。"

    "花园另一头，菊花丛与一畦新翻的菜地之间——艾琳娜站在那里。"

    "她穿着一件简单的亚麻长裙，袖口卷到肘上，手里拎着一只提水的木桶。"

    "她没有看你，只是在端详一畦刚长出嫩芽的薄荷。秋风吹过，她侧过脸去理了理被吹乱的头发。"

    "你看着她。"

    "这五年，她都在你身边。"

    "无论是那场风波，还是艾登堡这几年的变化——她从未离开。"
    "不是作为眼线，不是作为暗百合的人，也不是作为某个组织派来的工具。"
    "只是作为艾琳娜。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "您来了。"

    $ hide_all_chars()
    "她转过头，似乎早就察觉到你站在那里。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "奥尔德里克跟您说完了？"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "嗯。让他退休种花了。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "他等这一天等了三十六年。"

    elena "我帮他把菜地翻了一下。今年想种点儿什么——西红柿、薄荷、还有他喜欢的迷迭香。"

    "她一边说，一边把木桶轻轻放下。"

    if rel_elena >= 50:
        elena "明年开春，我想在那棵老橡树下，再种一片紫罗兰。"
        elena "你父亲生前最喜欢紫罗兰。我一直没机会种。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "好。陪你一起种。"

        $ hide_all_chars()
        "她笑了一下。那种笑很轻，却让你想起当年月光下的老橡树。"
        "那个晚上，她说自己'手很稳'。"
        "现在，她的手沾着泥土。一双不再握刀的手。"

        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "您知道吗——我已经很久没做过那个梦了。"

        elena "那些任务里的人，那些站成一排看着我的脸……他们终于不来了。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "他们走了。"

        player "你父亲对你说过——你安全了。"

        player "现在，是真的安全了。"

        $ hide_all_chars()
        "你站在她身边，看她把湿润的泥土轻轻盖回菜畦。"
        "夕阳把两个人的影子叠在一起，落在那片刚翻过的土上。"
    elif rel_elena >= 20:
        elena "您还记得那个晚上吗？我对您说我手很稳。"

        hide elena_img
        $ hide_all_chars("player_char_img")
        show player_char_img at left with dissolve
        player "记得。"

        hide player_char_img
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "我现在的手，沾着泥土。"

        elena "比起从前——我更喜欢这双手。"

        $ hide_all_chars()
        "她说完，没等你回应，就转过身继续侍弄那畦薄荷。"
        "你没有打断她。在艾登堡的秋日里，每个人都有自己安静的位置。"
    else:
        $ hide_all_chars("elena_img")
        show elena_img at left with dissolve
        elena "您先忙吧。我把这畦薄荷弄完，回头去厨房帮玛格丽特一把。"

        $ hide_all_chars()
        "她说得平淡，像是在交代一件再普通不过的家务。"
        "你点点头，没有多说。她和你之间，从来就不是用很多话维系的。"
        "但她还在这里。"
        "在革命之后，在风暴落定之后——她选择留在艾登堡的这一畦菜地旁边。"
        "这就够了。"

    hide elena_img with dissolve

    ## —— 第三幕：治理之道 ——

    scene bg great_hall with dissolve

    "丰收节的第二天。一支来自南方克恩伯爵领的代表团抵达了艾登堡。"

    "克恩伯爵领——曾经是王国最繁荣的领地之一。"
    "但五年来管理不善，加上天灾和战争的后遗症，如今已经满目疮痍。"

    "领头的是一个年轻的管事。他一脸疲惫，眼神中带着求助的急切。"

    "\"公爵大人，克恩伯爵派我们来向您请教治理之道。\""

    "\"我们的领地……实在是撑不下去了。农民在逃荒，商人在外迁，税收已经降到了十年最低。\""

    "\"而艾登堡……同样经历了战争，却成为了全国最富庶的领地。\""

    "\"我们想知道——您是怎么做到的？\""

    "你请他们坐下，给每人倒了一杯茶。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "没有秘诀。"

    "管事一脸困惑。\"没有秘诀？\""

    player "你们以为我有什么点石成金的法术？没有。"

    player "我做的事情很简单——"

    player "第一，倾听。走到田间地头，听农民说话。不是在大厅里听官员汇报。"

    player "第二，公平。同样的法律适用于所有人——贵族和平民一视同仁。"

    player "第三，透明。每一笔税收的用途都公开张贴在广场上。百姓知道他们的钱花在了哪里。"

    player "第四，耐心。好的治理不是一天建成的。它需要时间，需要信任，需要无数次的犯错和改正。"

    $ hide_all_chars()
    "管事认真地记录着。"

    "\"可是……如果农民不配合呢？如果有人偷税呢？如果——\""

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你问的这些问题——其实只有一个答案。"

    player "一个领主的力量不在于他有多少士兵，而在于有多少人愿意为他而战。"

    player "当百姓信任你的时候，他们不会偷税——因为他们知道税收是为了他们自己。"

    player "当百姓爱戴你的时候，你不需要士兵——因为每一个人都是你的守护者。"

    $ hide_all_chars()
    "管事站起身，深深鞠了一躬。"

    "\"多谢公爵大人赐教。我会一字不差地转告我家伯爵。\""

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "回去告诉你们伯爵——如果他愿意，可以亲自来。"

    player "我会带他去田里走走。那里比大厅更适合学习治理。"

    ## —— 第四幕：黄昏漫步 ——

    scene bg village with dissolve

    "黄昏。代表团离开了。丰收节也进入了尾声。"

    "你独自走在艾登堡的街道上。"

    "夕阳把一切都染成了暖金色——房屋、树木、石板路、还有路过的每一张脸。"

    "\"[player_name]，晚上好！\""
    "\"[player_name]，尝尝今年的新酒！\""
    "\"[player_name]，我家闺女会写自己名字了！谢谢您建的学堂！\""

    "人们用名字称呼你，不是用头衔。"
    "他们招手、微笑、递上一块面包或一杯酒。"
    "没有人下跪。没有人颤抖。"

    "你走过面包店，面包师正把最后一炉面包从烤炉里取出来。"
    "热气腾腾的香味扑面而来。"

    "你走过铁匠铺，铁匠的儿子正在学着打他人生中的第一把锄头。"
    "锤击声叮叮当当，充满了笨拙的热情。"

    "你走过教堂，晚祷的钟声刚刚响起。"
    "几个老人坐在台阶上，闭着眼睛听钟声回荡在山谷之间。"

    "然后——"

    "你看到了她。"

    "街角，一个白发苍苍的老太太坐在一把旧椅子上，面前摆着一个小篮子。"

    "你认出了她。五年前——不，更早——"
    "在你刚刚继承领主之位的那个艰难冬天，你曾经微服出巡，走进了她的家。"
    "她的丈夫刚刚去世，她一个人守着一间破屋，连面包都买不起。"

    "你悄悄给她留下了一袋银币。"

    "现在，她的面前——篮子里放着刚烤好的面包。"

    "她看到了你。老迈的眼睛一下子亮了起来。"

    "\"[player_name]……\""

    "她颤巍巍地站起来，从篮子里拿出一块面包——"

    "\"[player_name]，请吃一块面包。\""

    "\"当年您救了我的命。我一直想报答您，但我没有什么值钱的东西。\""

    "\"只有这个面包。是我自己做的。用的是今年的新麦。\""

    "你接过面包。它很轻，但在你手里重如千金。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "谢谢。这是我吃过的最好的面包。"

    $ hide_all_chars()
    "老太太笑了。满脸的皱纹挤在一起，像一朵盛开的花。"

    "\"[player_name]，您是好人。这辈子能遇到您这样的领主，是我们艾登堡的福气。\""

    "你咬了一口面包。"

    "很普通的面包。粗面粉，没有黄油，没有糖。"
    "但你吃得很慢，很认真。"

    "因为这块面包里有一个老人一辈子的感激。"
    "有今年丰收的阳光和雨水。"
    "有五年来无数个日夜的付出和坚守。"

    "你抬起头，看着夕阳下的艾登堡。"

    "金色的屋顶。升起的炊烟。远处田野里收割后的金色残茬。"
    "以及——到处可见的笑脸。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "这就是值得守护的一切。"

    $ hide_all_chars()
    "你继续朝前走。"

    "夕阳越来越低，但你的影子越来越长。"
    "它落在每一座房屋上，每一条街道上。"
    "不是遮挡——而是守护。"

    "你知道——明天太阳还会升起。"
    "孩子们还会去上学。铁匠还会敲锤子。老太太还会烤面包。"
    "而你——会一直在这里。守护着这一切平凡而珍贵的日常。"

    "直到你白发苍苍的那一天。"


    ## —— 第五幕：晚年与远讯 ——

    "你的白发一年比一年多。艾登堡的麦子一年比一年熟得更稳。"

    "偶尔有远方的商队路过，捎来一些王都的消息。"

    "关于王后的消息越来越少。有人说她病了，有人说她累了，有人说她的派系散了。"

    "关于南方的消息越来越多。几十个领地的代表坐在一张桌上，一条条把旧律改了——不是靠剑，是靠耐心。"

    "弗雷德里克王子回来过一次，又离开了。有人说他选择了另一种生活。"

    "你听着，点点头，然后回头去看田里的稻穗。"

    "那都是很远的事。远得像隔着一条大河。"


    ## —— 第六幕：无字的石头 ——

    "你是在一个平凡的春日清晨走的。"

    "没有号角，没有仪仗。按你留下的嘱咐——只在你最喜欢的那棵苹果树下，埋了一块无字的石头。"

    "艾登堡没有乱。第二天，铁匠的锤声照常响起，孩子们照常去学堂，面包照常出炉。"

    "这是你给这片土地最后的礼物——它已经不再需要你。"


    ## —— 第七幕：史册一角 ——

    "很多年后——也许几十年，也许更久——一位写史的人翻到一段闲笔。"

    "那段闲笔写道：「在旧秩序落幕之前很久，北境有一座叫艾登堡的小领地。那里的农人不下跪，贵族不苛税，孩子都识字。当时没有人把它当回事。」"

    "闲笔只写了这几行。翻页就过去了。"

    "而翻页之后——旧秩序如何一点点落下的——是另外的人，用另外的半生，才写到末尾的。"


    ## ── 旧秩序的落幕 ──

    "革命不是一天完成的。但每一天，都有旧世界的碎片在脱落。"

    "贵族特权被废除的那一天，王后的名字出现在公告的第一行。"

    if queen_trust:
        "她没有反抗。她早就看到了风向。"
        "她退隐到乡间的一座小庄园里，种花、读书、偶尔教附近的孩子们写字。她的生活变得简单——也许，比当王后时更真实。"
    else:
        "愤怒的民众冲进了王宫。她被驱逐出都城时，没有人为她送行。"
        "她的马车在暴雨中驶向远方。据说她去了邻国，靠变卖首饰度日。一个旧时代的终幕，没有掌声。"

    "封建领地制被废除了。对男爵来说，这意味着一切。"

    if baron_peace_path:
        "他是第一批主动放弃头衔的贵族。你不知道这是明智还是投机，但他确实成为了第一任民选议员。"
        "他在议会里的发言务实而老练——毕竟管理领地的经验不会因为换了头衔就消失。革命需要各种各样的人。"
    else:
        "他试图抵抗。召集残余私兵，拒绝签署放弃令。"
        "但历史的车轮不会为一个人停下。领地被没收，头衔被废除。他在街角酒馆里喝闷酒的样子，成了旧制度落幕的注脚。"

    "王族头衔——在新制度下，这个词已经没有了任何法律效力。"

    if prince_ally:
        "他化名融入了一座南方小镇。用他受过的教育教书，用他的学识为社区服务。"
        "没有人知道那个温和的教师曾是王子。也许，这正是他想要的。王冠落地后，他第一次感到了一种奇怪的轻松。"
    else:
        "他选择了流亡海外。在异国他乡，他成为了旧制度的最后象征——一面褪色的旗帜。"
        "据说他在写回忆录，把一切都归咎于命运。你没有读过。你忙着建设一个不需要王子的世界。"

    "在人民掌权的世界里，暗影中的守护者失去了意义。"

    if dark_lily_joined:
        "你给了他们一条路：从地下组织转型为民间监察力量。公开运作，接受监督，但保留那份对真相的执着。"
        "有些人适应了，有些人离开了。但那个从阴影中走出来的组织，第一次站在了阳光下。"
    elif dark_lily_destroyed:
        "它早已不存在了。人民不需要知道它曾经存在过。"
    else:
        "没有人下令解散它——它自己消失了。在一个人人都可以发声的世界里，秘密结社变得多余。"
        "最后一批成员默默摘下了徽章，走进了人群中。他们不再是暗百合，只是普通公民。这也许是最好的结局。"

    scene black with fade

    centered "{size=+8}民之守护者 · 尾声{/size}"
    centered "「他没有铁骑，没有王座，没有情报网。」"
    centered "「他只有一块面包，一个微笑，和一整个秋天的金色。」"
    centered "「但这就够了。」"
    centered "「这就是一切。」"

    pause 2.0

    return

## ============================================================
## 隐藏结局：父与子
## The Father and Son Hidden Ending
## ============================================================

label ending_father_son_epilogue:

    scene black with fade

    centered "{size=+10}深夜{/size}"
    centered "{size=+6}一切结束之后{/size}"

    pause 1.5

    scene bg study with dissolve

    "深夜。"

    "所有人都睡了。城堡里安静得只能听到风穿过走廊的声音。"

    "你独自坐在父亲的书房里。"

    "这间书房——你已经不知道来过多少次了。"
    "每一次重大的选择之前，你都会来这里坐一坐。"
    "像是在寻找什么指引。"

    "今晚也一样。一切都结束了——阴谋、战争、真相。"
    "但有一件事还没有结束。"

    "你心里有一个声音一直在说——"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "还差一声告别。"

    $ hide_all_chars()
    "你看着父亲的书桌。墨水瓶旁有一只干枯的鹅毛笔，笔尖朝下搁着，像是主人刚放下一样。"

    "桌上还摆着父亲用过的墨水瓶、羽毛笔、还有一个磨得发亮的镇纸。"
    "十多年了。你一直没有动过这些东西。"

    "风从窗缝钻了进来。蜡烛火苗猛跳了一下。"

    "然后——"

    "你看到了。"

    "书桌对面的那把旧椅子上——坐着一个人。"

    "你的心跳漏了一拍。"

    "那个人穿着一件深蓝色的长袍，头发花白，面容清瘦。"
    "他看起来很疲倦，但眼神温和而明亮。"

    "是父亲。"

    "卡尔。"

    "他坐在他的旧椅子上，就像从前那样——一只手撑着头，微微侧着身子。"
    "好像他只是在等你来敲门，就像十年前的每一个傍晚一样。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "……父亲？"

    $ hide_all_chars()
    "\"你来了。\""

    "他的声音——和你记忆中一模一样。低沉、温和、带着一丝你小时候最熟悉的笑意。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你……你是——"

    $ hide_all_chars()
    "\"坐下吧。\""

    "你不知道这是梦境，还是幻觉，还是别的什么。"
    "但你的脚不听使唤，走到了书桌前的椅子上，坐了下来。"

    "就这样——父与子，隔着一张书桌，面对面。"
    "像从前一样。"

    "\"让我看看你。\""

    "父亲仔细端详着你的脸。他的目光停留在你的眉眼之间、你的嘴角、你的双手。"

    "\"长大了。\""

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "……十年了。"

    $ hide_all_chars()
    "\"是啊。十年了。\""

    "他叹了一口气。不是悲伤的叹息——更像是一声漫长的释然。"

    "\"你做到了我做不到的事。\""

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "什么？"

    $ hide_all_chars()
    "\"活下来。而且——不仅仅是活下来。\""

    "\"你找到了真相。你守护了这片土地。你没有被仇恨吞噬。\""

    "\"你比我强。\""

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "不。我只是……继承了你留下的东西。"

    player "你的信念。你的正义。你教给我的一切。"

    player "如果不是你——"

    $ hide_all_chars()
    "\"嘘。\""

    "父亲微微摇头。他伸出手——"

    "但你知道那只手无法触碰你。"

    "他停在了半空中。然后，缓缓放下。"

    "\"我只有一个遗憾。\""

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "什么？"

    $ hide_all_chars()
    "\"没有看着你长大。\""

    "\"没有看到你第一次骑马。没有看到你第一次举起剑。\""

    "\"没有在你害怕的时候——告诉你'不用怕，父亲在'。\""

    "\"没有在你成功的时候——拍着你的肩膀说'好样的'。\""

    "\"这些……都是我亏欠你的。\""

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你不亏欠我任何东西。"

    player "你用你的生命——你的死亡——教会了我什么是勇气。"

    player "你不在的每一天——我都在想你会怎么做。"

    player "你一直在我身边。从来没有离开过。"

    $ hide_all_chars()
    "父亲看着你。那双和你如此相似的眼睛里，有光在闪动。"

    "\"……是吗。\""

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "是。"

    $ hide_all_chars()
    "蜡烛在轻轻作响。烛泪沿着铜座缓缓流下。"

    "然后——父亲笑了。"

    "那是你记忆深处最温暖的笑容。"
    "不是英雄的笑。不是领主的笑。"
    "是一个父亲——看到自己的孩子平安长大后——最朴素的笑。"

    "\"我该走了。\""

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "父亲——"

    $ hide_all_chars()
    "\"别难过。我去的地方没有阴谋，没有战争，没有毒药。\""

    "\"只有安宁。\""

    "他站了起来。长袍的下摆似乎在溶解，边缘变得模糊而透明。"

    "\"照顾好自己。照顾好奥尔德里克——那个老顽固大概要把你烦死了。\""

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "……他很好。"

    $ hide_all_chars()
    "\"照顾好艾登堡。照顾好——你爱的人。\""

    "他的身影越来越淡。像是晨雾在阳光下慢慢消散。"

    "\"我的孩子。我为你骄傲。\""

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "父亲——等一下——"

    $ hide_all_chars()
    "你站起来，伸出手——"

    "但你的手穿过了空气。"

    "椅子是空的。"

    "书房里只有你一个人。"

    "蜡烛的火苗稳稳地燃烧着。风停了。"

    "一切都像什么都没有发生过。"

    "但你知道——有什么东西不一样了。"

    "你心里那个缺了十年的角落——被填满了。"

    "不是被遗忘填满。"
    "而是被告别填满。"

    "你在书桌前坐了很久。"

    "然后你站起来，走到门口。"

    "你回头最后看了一眼——"

    "父亲的椅子。父亲的书桌。父亲的墨水瓶。"

    "这些东西以后还会在这里。但你不需要再来寻找什么了。"

    "因为你找到了。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "再见，父亲。"

    $ hide_all_chars()
    "你轻轻关上了书房的门。"

    "锁舌咔哒一声，落入了锁扣。"

    "走廊里很暗。但你的脚步——比任何时候都坚定。"

    "你朝自己的房间走去。"

    "明天还有很多事要做。还有很多路要走。"

    "但从今晚起——你不再是一个人了。"

    "因为你知道——无论你走多远——"

    "父亲的骄傲，会一直跟着你。"

    scene black with fade

    centered "{size=+8}隐藏结局：父与子{/size}"
    centered "「有些告别，要用十年才能说出口。」"
    centered "「有些骄傲，要等孩子长大了才能听到。」"
    centered "「关上那扇门——不是忘记。」"
    centered "「是终于学会了放手。」"

    pause 3.0

    return

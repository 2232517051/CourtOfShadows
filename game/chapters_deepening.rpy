# 章节深化场景 - 第二至第五章
# Deepening scenes for Chapters 2-5
# 独立场景，可从各章主线流程中调用，增添叙事深度

# ============================================================
# 变量定义
# ============================================================

default ch2_deep_spy_recruited = False
default ch2_deep_baron_letter = False
default ch3_deep_ritual_witnessed = False
default ch3_deep_cure_found = False
default ch4_deep_queen_weakness = False
default ch4_deep_court_poet = False
default ch5_deep_deserter_mercy = False
default ch5_deep_final_prayer = False

# ============================================================
# 第二章深化 - 场景一：间谍的代价
# ============================================================

label ch2_deep_spy:

    scene bg great_hall with dissolve

    "议事结束后，大厅渐渐空了下来。"
    "领主们三三两两地离去，低声交谈着各自的盘算。"

    "你正准备离开时，一个衣着朴素的仆人悄悄靠了过来。"

    "他大约四十来岁，面容平平无奇——正是那种在任何宴会上都不会引起注意的人。"

    $ hide_all_chars("servant_generic_img")
    show servant_generic_img at left with dissolve
    servant_common "大人，能否借一步说话？"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你是谁？有什么事？"

    $ hide_all_chars()
    "他左右环顾了一下，确认大厅里已经没有旁人。"

    $ hide_all_chars("servant_generic_img")
    show servant_generic_img at left with dissolve
    servant_common "小的名叫马丁，在城堡里做杂役已有十年。"
    servant_common "这十年里，小的听到过很多不该听到的事情……"
    servant_common "各位领主的私下谈话、密信往来、暗中交易——小的都略知一二。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你为什么要告诉我这些？"

    $ hide_all_chars()
    $ hide_all_chars("servant_generic_img")
    show servant_generic_img at left with dissolve
    martin "因为小的需要一位靠山。"
    martin "老领主在世时，对小的颇为照顾。如今他走了……"
    martin "小的想继续为艾登堡效力，但需要有人保护小的。"

    "他的眼神中带着几分恳切，但你注意到他的手指微微发抖。"
    "是紧张，还是在演戏？"

    "你仔细打量了他一番。他的鞋底磨损不均——左脚比右脚磨得更厉害。"
    "这说明他经常侧身贴墙站立，偷听别人说话。这至少证明他确实是个惯于窃听的人。"

    "但他的衣服内衬似乎比外面的粗布要好得多——有人在暗中资助他。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你现在为谁工作？如实说。"

    $ hide_all_chars()
    "马丁的表情僵了一瞬。"

    $ hide_all_chars("servant_generic_img")
    show servant_generic_img at left with dissolve
    martin "小的……小的只是一个普通仆人——"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "别在我面前耍花招。你衣服内衬的绸缎可不是仆人买得起的。"

    $ hide_all_chars()
    "马丁终于叹了口气。"

    $ hide_all_chars("servant_generic_img")
    show servant_generic_img at left with dissolve
    martin "……是男爵大人。他让小的留意您的一举一动。"
    martin "但小的说的也是真话——小的确实想为您效力。"
    martin "男爵给的钱不少，但他不是个好主子。他把人当棋子用完就扔。"

    "这倒是个有趣的局面。一个男爵安插的间谍，主动来投诚。"
    "他可能真心想换主人，也可能这本身就是男爵的另一层圈套。"

    menu:
        "收下他，让他做我的耳目":
            jump ch2_deep_spy_recruit

        "将计就计——让他做双面间谍":
            jump ch2_deep_spy_double

        "拒绝他——间谍不可信":
            jump ch2_deep_spy_refuse

label ch2_deep_spy_recruit:

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "好。从今天起，你为我做事。"
    player "男爵那边，你直接告诉他你被我发现了，已经无法继续。"

    $ hide_all_chars("servant_generic_img")
    show servant_generic_img at left with dissolve
    martin "大人英明！小的这就——"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "但有一个条件。"

    "你走近一步，压低声音。"

    player "如果你再敢脚踩两条船，我会让你知道什么叫真正的代价。"

    $ hide_all_chars()
    "马丁的脸色一白，连连点头。"

    $ hide_all_chars("servant_generic_img")
    show servant_generic_img at left with dissolve
    martin "小的明白！小的对天发誓，绝不背叛大人！"

    "此后数日，马丁果然带来了一些有用的情报——"
    "比如男爵正在秘密购买粮食，以及某位领主的妻子与教廷有着不为人知的联系。"

    "这些情报的真假还需要验证。不过，一扇新的窗口已经打开了。"

    $ ch2_deep_spy_recruited = True
    $ change_stat("intrigue", 5)
    $ change_stat("reputation", 3)

    "（马丁成为了你的情报员。他带来的消息有真有假，需要甄别。）"

    jump ch2_deep_spy_end

label ch2_deep_spy_double:

    "你在心里笑了一声。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "马丁，你很聪明——但还不够聪明。"
    player "我不会让你离开男爵。恰恰相反，你要继续为他工作。"

    $ hide_all_chars("servant_generic_img")
    show servant_generic_img at left with dissolve
    martin "大人的意思是……"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你继续向男爵汇报关于我的消息——但只汇报我想让他知道的。"
    player "同时，你把男爵那边的真正情报带给我。"

    $ hide_all_chars()
    "马丁话说到一半断了，随即低下头，深深一揖。"

    $ hide_all_chars("servant_generic_img")
    show servant_generic_img at left with dissolve
    martin "大人果然深谋远虑。小的愿意效劳。"
    martin "不过……如果男爵发现了呢？他的手段可不温柔。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "如果你做得够好，他不会发现。"
    player "如果你做得不好——那你也用不着担心男爵了，因为我会先找到你。"

    $ hide_all_chars()
    "马丁咽了口口水。"

    $ hide_all_chars("servant_generic_img")
    show servant_generic_img at left with dissolve
    martin "小的……小的一定竭尽全力。"

    "你转身离去，心中已经在盘算该让男爵'知道'些什么。"
    "一个精心编织的假情报网，比一千个士兵都要管用。"

    $ ch2_deep_spy_recruited = True
    $ change_stat("intrigue", 10)

    "（你将马丁发展为双面间谍。这是高风险的博弈——一旦败露，后果不堪设想。）"

    jump ch2_deep_spy_end

label ch2_deep_spy_refuse:

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "不必了。"

    $ hide_all_chars("servant_generic_img")
    show servant_generic_img at left with dissolve
    martin "大人？"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "一个连主人都能背叛的人，我不需要。"
    player "你回去告诉男爵——他的手段太低级了。"

    $ hide_all_chars()
    "马丁的脸上闪过一丝慌乱。"

    $ hide_all_chars("servant_generic_img")
    show servant_generic_img at left with dissolve
    martin "大人，小的是真心——"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "如果你是真心的，那就更不能用了。因为一个真心背叛旧主的人，迟早也会背叛新主。"
    player "走吧。我不会为难你。"

    $ hide_all_chars()
    "马丁呆立片刻，终于低着头退了出去。"

    "门关上了。你把他坐过的椅子挪回原处，顺手擦掉了桌上他留下的水渍。"
    "在这个尔虞我诈的世界里，信任是最昂贵的货币——你不打算轻易花出去。"

    $ change_stat("loyalty", 5)
    $ change_stat("reputation", 3)

    "（你拒绝了马丁。安全，但也失去了一个潜在的情报来源。）"

    jump ch2_deep_spy_end

label ch2_deep_spy_end:

    hide player_char_img with dissolve

    return

# ============================================================
# 第二章深化 - 场景二：男爵的私信
# ============================================================

label ch2_deep_baron_letter:

    scene bg study with dissolve

    show elena_img at left with dissolve

    elena "有件事需要你看看。"

    "艾琳娜的表情比平时更加严肃。她从袖中取出一封折叠的信纸递给你。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "这是什么？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "男爵的私信。我的人在他的信使经过河谷时截获的。"
    elena "信使已经被放走了——他不知道信被拆开过。我们用了特殊手法重新封好。"

    $ hide_all_chars()
    "你展开信纸。字迹苍劲有力，但仔细看，某些笔画有微微的颤抖。"

    "信上写着——"

    "{i}吾友：{/i}"
    "{i}病况日益加重。御医说还有两年，也许更少。{/i}"
    "{i}双腿的麻木已经蔓延到腰间。再过半年，恐怕就无法骑马了。{/i}"
    "{i}我必须在还能行动的时候，为家族做最后的安排。{/i}"
    "{i}艾登堡的新领主还年轻，根基不稳。这是最好的时机。{/i}"
    "{i}如果我倒下了，请务必照顾玛格丽特和孩子们。{/i}"
    "{i}——弗雷德里克{/i}"

    "你放下信纸，久久没有说话。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "他……在等死。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "是的。某种消耗性的疾病，可能是风痹症，也可能更严重。"
    elena "这解释了很多事情——他为什么这么急切，为什么不顾一切地扩张势力。"

    $ hide_all_chars()
    "男爵弗雷德里克——那个在议事厅里咄咄逼人、似乎永远精力充沛的铁腕人物。"
    "原来他一直在和时间赛跑。"

    "你想起他在议事时偶尔按住膝盖的小动作，当时以为只是习惯——"
    "现在才明白，那是在忍受疼痛。"

    hide elena_img
    show elena_img at right with move

    elena "问题是——我们该怎么利用这个消息？"

    "你看向窗外。天边的晚霞如血般殷红。"

    menu:
        "他也是一个在命运面前挣扎的人……":
            jump ch2_deep_baron_letter_sympathy

        "这是他的弱点——我们可以利用":
            jump ch2_deep_baron_letter_exploit

        "把这个消息分享给我们的盟友":
            jump ch2_deep_baron_letter_share

label ch2_deep_baron_letter_sympathy:

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "先把信放一放。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "什么？"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你不觉得……他和我们其实很像吗？"
    player "一个父亲，想在临死前为孩子们留下点什么。"
    player "我的父亲为了保护我，至死都在谋划。男爵也是这样。"

    "艾琳娜低下头，似乎在斟酌措辞。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "你是说……你同情他？"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "不完全是同情。是理解。"
    player "一个知道自己时日无多的人，他的绝望会让他做出疯狂的事。"
    player "但如果有人给他一条体面的退路——也许我们能避免一场不必要的战争。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "……你比我想象的更有远见。"
    elena "好吧。我会留意合适的时机，看看能否搭建一个秘密对话的渠道。"

    $ ch2_deep_baron_letter = True
    $ change_stat("loyalty", 5)
    $ change_stat("reputation", 5)
    $ change_rel("rel_elena", 5)
    $ change_rel("rel_baron", 3)

    "（你选择了理解和同情。这可能在未来打开一扇意想不到的门。）"

    jump ch2_deep_baron_letter_end

label ch2_deep_baron_letter_exploit:

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "一个垂死的人，是最危险的——但也是最容易犯错的。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "你打算怎么做？"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "他急于求成，就意味着他会忽略细节。"
    player "我们不需要正面对抗他——只需要拖延。每拖一天，他的身体就弱一分。"
    player "两年后，这个问题会自己解决。"

    "艾琳娜的手指无意识地摩挲着袖口的暗纹。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "……你说得对。时间站在我们这边。"
    elena "但要小心——一只被逼到绝路的野兽，反扑起来是最凶猛的。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "所以我们要让他觉得自己没有被逼到绝路。"
    player "给他一些小胜利，一些虚假的进展——让他以为一切都在掌控之中。"
    player "等他发现真相的时候，已经太晚了。"

    $ ch2_deep_baron_letter = True
    $ change_stat("intrigue", 8)
    $ change_rel("rel_elena", 3)

    "（你决定利用男爵的病情作为战略优势。冷酷，但有效。）"

    jump ch2_deep_baron_letter_end

label ch2_deep_baron_letter_share:

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "这个消息太重要了，不能只有我们两个知道。"
    player "通知奥尔德里克和雷恩队长。如果其他盟友可靠，也让他们知道。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "公开这种消息有风险。如果男爵知道我们截获了他的信——"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "所以要小心处理。只告诉最核心的人，而且不要透露来源。"
    player "就说是从男爵领地内的线人那里听到的传言。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "明白了。我会安排的。"

    "她收起信纸，转身要走，又停了下来。"

    elena "你觉得……其他领主会怎么反应？"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "有些人会像我们一样选择等待。有些人——可能会像秃鹫一样围上来。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "一个垂死之人的领地，是最肥美的猎物。"
    elena "希望我们的盟友们还有些底线。"

    $ ch2_deep_baron_letter = True
    $ change_stat("reputation", 5)
    $ change_stat("intrigue", 3)
    $ change_rel("rel_elena", 3)

    "（你选择与盟友共享情报。这巩固了联盟，但也增加了泄密的风险。）"

    jump ch2_deep_baron_letter_end

label ch2_deep_baron_letter_end:

    hide elena_img with dissolve

    return

# ============================================================
# 第二章深化 - 场景三：深夜的教堂
# ============================================================

label ch2_deep_church_midnight:

    scene bg church with dissolve

    "又是一个辗转难眠的夜晚。"
    "自从接手艾登堡以来，你的睡眠就像是被切成了碎片——"
    "每一段都太短，每一段都充满了噩梦。"

    "你披上外衣，走出卧室。走廊里的长明灯只剩下两盏还亮着，石板地凉得渗人。"

    "不知不觉间，你的脚步把你带到了教堂。"
    "教堂的大门虚掩着——有人比你来得更早。"

    "你轻轻推开门，看到了一个出乎意料的身影。"

    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve

    $ hide_all_chars()
    "主教大人跪在圣坛前，双手合十，身体微微颤抖。"
    "烛火将他的影子投射在墙壁上，巨大而孤独。"

    "他没有穿平时那身华丽的法袍，只着一件朴素的灰色衬衣。"
    "没有权杖，没有十字架，没有任何身份的标志——"
    "此刻的他，只是一个普通的祈祷者。"

    "你站在门口犹豫了一下。这显然是一个非常私密的时刻。"
    "但他已经察觉到了你的存在。"

    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "……进来吧。这是神的殿堂，不拒绝任何人。"

    "你走进教堂，在他身后几步远的地方停下。"

    hide bishop_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "打扰了，主教大人。我没想到这个时间会有人在这里。"

    hide player_char_img
    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "叫我马修斯就好。在这里，在这个时辰，没有什么主教。"
    bishop "只有一个……向上天寻求答案的老人。"

    $ hide_all_chars()
    "他站起身来，膝盖发出轻微的咔嚓声。面容上的疲惫比白天深了十倍。"

    "他在长椅上坐下，示意你也坐。"

    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "你也睡不着？"

    hide bishop_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "太多事情在脑子里转。"

    hide player_char_img
    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "……是啊。太多事情。"

    "蜡烛偶尔噼啪作响。烛影在主教苍老的面孔上摇晃不定。"

    bishop "我在这个教堂里祈祷了三十年。"
    bishop "三十年来，我一直相信神在倾听。相信世间万事皆有安排。"
    bishop "但最近……"

    "他的声音变得很轻。"

    bishop "你父亲是个好人。不是圣人——可他一直在试着做正确的事。"
    bishop "神为什么带走了他？为什么让一个恶人的阴谋得逞？"
    bishop "如果这是'安排'，那这个安排未免太残酷了。"

    hide bishop_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "主教——马修斯……"

    hide player_char_img
    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "我知道你会说什么。'一切都是考验''苦难中见真知'——"
    bishop "这些话我对别人说过一千遍。但今晚，轮到我需要听别人说了。"

    "他抬起头，目光中有一种近乎恳求的脆弱。"

    bishop "告诉我，年轻人……你相信什么？"
    bishop "在这个充满背叛和阴谋的世界里——你靠什么支撑自己？"

    menu:
        "说实话——我也有很多疑惑":
            jump ch2_deep_church_doubt

        "坚定他的信仰——他不能倒下":
            jump ch2_deep_church_encourage

        "信仰只是工具——坦诚但残酷的真相":
            jump ch2_deep_church_tool

label ch2_deep_church_doubt:

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我不知道。"

    "马修斯看着你，没有说话。"

    player "有些夜晚，我觉得父亲还在某个地方看着我。"
    player "有些夜晚，我觉得他只是消失了——像一颗烛火被风吹灭，什么都没有留下。"

    player "我不确定神是否存在。但我确定——"
    player "如果我停下来，如果我放弃，那些依靠我的人就真的没有希望了。"

    "马修斯安静地听着，眼眶渐渐泛红。"

    hide player_char_img
    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "……你知道吗，你父亲也说过类似的话。"
    bishop "他说，'不管天上有没有神，地上的人总得有人来守护。'"

    hide bishop_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "那他比我勇敢。我只是……还没有找到别的选择。"

    hide player_char_img
    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "也许……这就够了。"
    bishop "也许信仰不需要确定。也许——怀疑本身就是一种虔诚。"
    bishop "因为只有真正在乎的人，才会去质疑。"

    "他深深地吸了一口气，仿佛卸下了一个沉重的包袱。"

    bishop "谢谢你，孩子。谢谢你的诚实。"
    bishop "我已经很久没听人这样跟我说话了。"

    $ change_stat("faith", 5)
    $ change_rel("rel_bishop", 10)

    $ hide_all_chars()
    "那个夜晚，你们又聊了很久——关于生死、关于意义、关于那些永远没有答案的问题。"
    "月亮移过教堂的彩色玻璃窗，在地面上投下变幻的光影。"

    "（你与主教分享了真实的疑惑。一段深厚的精神纽带在深夜的教堂中形成。）"

    jump ch2_deep_church_end

label ch2_deep_church_encourage:

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "马修斯，听我说。"

    "你在他面前蹲下，平视他的眼睛。"

    player "我父亲被害的那天晚上，我也问过同样的问题。"
    player "神为什么不阻止？为什么让坏人得逞？"

    player "但后来我想明白了一件事——"
    player "如果没有黑暗，我们又怎么知道什么是光明？"

    player "您的信仰不是用来解释苦难的——它是用来战胜苦难的。"
    player "我父亲走了，但您还在。这座教堂还在。那些需要您引导的人还在。"
    player "如果您现在倒下了，谁来照亮他们的路？"

    "马修斯的眼泪终于掉了下来。"

    hide player_char_img
    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "你……你说得对。"
    bishop "是我软弱了。三十年的信仰，不应该被一个夜晚的疑惑击垮。"

    hide bishop_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "疑惑不是软弱。但放弃才是。"

    "他用衣袖擦了擦眼睛，缓缓站起身来。"

    hide player_char_img
    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "你父亲……如果他能看到你现在的样子，一定会为你骄傲。"
    bishop "你身上有一种光芒，孩子。不是权力的光芒——是比那更纯粹的东西。"

    "他走到圣坛前，重新点燃了一根快要熄灭的蜡烛。"

    bishop "从明天起，我会更坚定地站在你身边。"
    bishop "不只是作为教会的代表——而是作为一个被你重新点燃信念的人。"

    $ change_stat("faith", 5)
    $ change_rel("rel_bishop", 8)
    $ change_stat("reputation", 3)

    "（你用温暖和力量重新点燃了主教的信仰之火。他将成为你最坚定的精神支柱。）"

    jump ch2_deep_church_end

label ch2_deep_church_tool:

    "你犹豫了一下，但还是决定说出心里话。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "马修斯……你真的想听实话吗？"

    hide player_char_img
    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "我说了，今晚不需要安慰的话。"

    hide bishop_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "那好。"
    player "我认为——信仰是一种工具。"

    "马修斯的身体明显僵了一下。"

    player "别误会，我不是说神不存在。那个问题我回答不了，也许没人能回答。"
    player "我说的是——无论神是否存在，信仰本身都是有力量的。"
    player "因为它让人们有所敬畏，有所希望，有所约束。"

    player "你在教堂里念的每一篇祷文，安慰的每一个灵魂——"
    player "那些力量是真实的。不管它来自天上还是来自你自己的心。"

    hide player_char_img
    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "……你在说，我这三十年的虔诚，只是一场自欺欺人的把戏？"

    hide bishop_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "不。我在说，就算它是——它依然有意义。"
    player "一个农妇在暴风雨的夜里抱着十字架祈祷，她的恐惧真的减轻了。"
    player "一个垂死的战士听了你的临终祷告，真的安详地闭上了眼睛。"
    player "这些不是假的。这些是你创造的奇迹——不管背后有没有神的旨意。"

    "马修斯看了你很久很久。"

    hide player_char_img
    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "你的话……让我不舒服。"
    bishop "但我必须承认——我没有办法反驳你。"

    bishop "也许这就是为什么你能做领主，而我只能做牧师。"
    bishop "你看到的是世界本来的样子。而我……一直想把它看成神想让我看到的样子。"

    $ change_stat("intrigue", 5)
    $ change_rel("rel_bishop", 3)

    $ hide_all_chars()
    "那晚之后，主教看你的眼神变了。"
    "不再只有慈祥和亲切——多了一丝敬畏，和一丝难以言说的距离。"

    "（你说出了残酷的真相。主教被你的洞察力所震撼，但你们之间的关系变得更加复杂。）"

    jump ch2_deep_church_end

label ch2_deep_church_end:

    hide bishop_img with dissolve

    "走出教堂时，东方已经泛起了鱼肚白。"
    "新的一天又要开始了——带着它永远无法兑现的承诺。"

    return

# ============================================================
# 第三章深化 - 场景一：暗百合的仪式
# ============================================================

label ch3_deep_ritual:

    scene bg dungeon with dissolve

    "艾琳娜带你穿过一条隐秘的地下通道。"
    "潮湿的石壁上挂着绿色的苔藓，空气中弥漫着霉味和另一种更甜腻的气息——"
    "焚香。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "从这里开始，你必须绝对服从我的指示。"
    elena "核心仪式只对正式成员开放。即便你已经宣誓加入，擅自记录或泄露仪式内容——"

    "她用手指在脖子上比了一下。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "明白了。"

    $ hide_all_chars()
    "通道尽头是一扇沉重的铁门。艾琳娜敲了三下，停顿，再敲两下。"

    "门开了。"

    "眼前的景象让你屏住了呼吸。"

    "一个圆形的地下大厅，穹顶高耸入黑暗之中。"
    "数百根黑色蜡烛排列成同心圆的图案，火焰在无风的空气中纹丝不动。"
    "正中央是一张石台，台上放着一朵盛开的白色百合花——在黑暗中几乎是发光的。"

    "大约三十个黑袍人围绕着石台站立，面容隐藏在兜帽的阴影中。"
    "低沉的吟唱声从四面八方传来，像是大地本身在呻吟。"

    hide player_char_img
    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve

    $ hide_all_chars()
    "影主站在石台后方，今晚她没有戴兜帽。"
    "一张沉静而威严的面容，深褐色的眼睛在烛光中闪烁着锐利的光芒。"
    "唯有那双眼睛，深邃得像两口枯井，让人不敢久视。"

    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    lily_master "今夜，有新的花瓣要加入我们的花冠。"
    lily_master "上前来。"

    $ hide_all_chars()
    "两个年轻人走向石台，浑身发抖。他们是新加入的成员——今晚是他们的入会仪式。"

    "百合之主从袍中取出一把精致的银刀。刀刃上镌刻着蔷薇的花纹。"

    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    lily_master "暗百合的第一条戒律——鲜血为盟，至死不渝。"

    "她将银刀递给第一个年轻人。"

    lily_master "割开你的手掌。让你的血滴在百合花上。"
    lily_master "从此刻起，你的生命属于组织，你的秘密属于组织，你的死亡——也属于组织。"

    $ hide_all_chars()
    "年轻人颤抖着接过刀，在手掌上划了一道口子。"
    "鲜血滴落在白色的百合花瓣上，殷红色缓缓洇开。"

    "吟唱声骤然升高，然后戛然而止。"

    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    lily_master "你已被接纳。起来吧，暗百合的花瓣。"

    $ hide_all_chars()
    "第二个年轻人也完成了同样的仪式。"

    "然后——百合之主的目光转向了你。"

    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    lily_master "我们的新成员。艾登堡的领主。"
    lily_master "你已经宣过誓了。今夜，你以正式成员的身份见证我们的仪式。"

    $ hide_all_chars()
    "她的目光在你身上停留了一瞬——像是在确认什么。"

    "你感受到身旁艾琳娜微微松了口气。"

    "作为已经加入暗百合的成员，你可以选择如何参与这场仪式。"

    menu:
        "积极参与——深入融入组织":
            jump ch3_deep_ritual_join

        "冷静旁观——保持距离":
            jump ch3_deep_ritual_observe

        "暗中记录仪式的细节——这些情报太有价值了":
            jump ch3_deep_ritual_document

label ch3_deep_ritual_join:

    "你向前走了一步，接过银刀。"

    "刀刃冰凉，但刀柄上还残留着前一个人的体温——和恐惧。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我愿意。"

    $ hide_all_chars()
    "你毫不犹豫地划开手掌。痛感如电流般窜过全身。"
    "鲜血滴落在百合花上——此刻花瓣已经被三个人的血浸透，变成了深红色。"

    hide player_char_img
    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    lily_master "好。很好。"

    "她的声音里带着满意——和一丝不易察觉的占有欲。"

    lily_master "从今日起，你是暗百合的一瓣花叶。"
    lily_master "组织会保护你，帮助你，引导你。"
    lily_master "但记住——百合花凋谢时，花瓣也随之消亡。我们一荣俱荣，一损俱损。"

    $ hide_all_chars()
    "吟唱声再次响起，这次更加热烈。黑袍人们依次走过来，无声地向你点头致意。"

    "仪式结束后，艾琳娜在通道里叫住了你。"

    hide lily_master_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "你……真的这么做了。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "这是最快取得他们信任的方式。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "但你也把自己绑在了一条船上。百合之主不是个善人。"
    elena "她现在可以用这个血誓来要求你做很多事。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "包括对付男爵？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "包括——任何事。"

    $ ch3_deep_ritual_witnessed = True
    $ change_stat("intrigue", 5)
    $ change_rel("rel_elena", -3)

    "（你以血为盟，正式加入暗百合。获得了组织的信任，但也失去了一部分自由。）"

    jump ch3_deep_ritual_end

label ch3_deep_ritual_observe:

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "多谢百合之主的美意。但我今晚只是来观礼的。"
    player "加入与否——容我再考虑考虑。"

    "空气中的温度似乎下降了几度。"

    hide player_char_img
    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    lily_master "考虑？"

    hide lily_master_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "正因为我尊重这个仪式的神圣性，才不愿意在没有准备好的时候轻率地宣誓。"
    player "一个匆忙的誓言，不如一个深思熟虑的承诺。"

    "百合之主注视你良久。"

    hide player_char_img
    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    lily_master "……有意思。你父亲当年也拒绝了我的邀请。"
    lily_master "看来固执是遗传的。"

    "她收回银刀，转身回到石台后方。"

    lily_master "但要记住——你今晚看到的一切，已经超出了外人应该知道的范围。"
    lily_master "希望你的沉默……能和你的勇气一样可靠。"

    $ ch3_deep_ritual_witnessed = True
    $ change_stat("intrigue", 5)
    $ change_stat("loyalty", 3)

    "（你保持了独立，但也欠下了暗百合一个人情——沉默的代价。）"

    jump ch3_deep_ritual_end

label ch3_deep_ritual_document:

    "你在心中快速记忆着一切细节——"
    "大厅的形状、蜡烛的排列方式、石台的纹饰、银刀上的花纹。"
    "更重要的是人数——三十人——以及影主那张没有兜帽遮挡的脸。"

    "如果你能记住这些，就算日后与暗百合决裂，也有足够的筹码。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "今晚的仪式让我深受触动。容我回去好好想想。"

    hide player_char_img
    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve
    lily_master "当然。但不要想太久。"

    $ hide_all_chars()
    "仪式结束后，你立刻在一张羊皮纸上画下了大厅的布局草图。"
    "每一个细节都可能在将来救你一命——或者毁掉暗百合。"

    "但你也知道，如果这些记录被发现——你就彻底和暗百合为敌了。"

    hide lily_master_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "你刚才……一直在观察。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我的记忆力一直不错。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "你在记录仪式的细节。"

    "她的语气不是疑问——是陈述。"

    elena "……我不会阻止你。但如果影主发现了，我也保不了你。"

    $ ch3_deep_ritual_witnessed = True
    $ change_stat("intrigue", 8)

    "（你暗中记录了仪式的关键细节。这些情报价值连城——但一旦暴露，后果致命。）"

    jump ch3_deep_ritual_end

label ch3_deep_ritual_end:

    hide lily_master_img with dissolve

    return

# ============================================================
# 第三章深化 - 场景二：雷恩的伤疤
# ============================================================

label ch3_deep_captain_scar:

    scene bg study with dissolve

    "刺杀事件之后的第二天，你去探望雷恩队长。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    $ hide_all_chars()
    "他坐在一张木椅上，衬衣半解，一个侍女正在帮他包扎左肋的伤口。"
    "但你注意到——他更痛苦的不是新伤，而是左肩上一道从锁骨延伸到肩胛的旧疤。"
    "那道疤痕像一条蜿蜒的蜈蚣，泛着可怕的紫红色，看起来从未完全愈合。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "你来了，大人。我没事——皮肉伤。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "那个旧伤呢？"

    "雷恩的脸色变了一瞬。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "……旧伤也没事。只是天气变化的时候会疼。"

    "侍女包扎完毕，识趣地退了出去。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "雷恩，你不必对我隐瞒。我需要了解我身边每个人的状况。"
    player "那道伤疤是怎么来的？"

    "窗外传来训练场上的刀剑声和吆喝声。雷恩的目光落在窗外，像是透过那些操练的士兵看到了更久远的东西。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    if captain_past_done:
        ## 玩家已在 npc_captain_past 听过格伦瓦德完整往事（12年前/鞭刑/流放/父亲救）
        ## 此处不重复，只补城墙那天他没讲的那部分——肩膀烙铁审讯
        captain "……格伦瓦德那次，我在城墙上对你讲过一半。"

        captain "五十鞭、流放、你父亲救我——那些你都知道了。但有一段我没讲。"

        "他给自己倒了一杯酒，一饮而尽。"

        captain "鞭刑之前，男爵把我关在地牢里三天三夜。"
        captain "他们用烧红的铁条在我肩膀上烙——说每烙一下，就问我一次：'你还敢抗命吗？'"

        "他拉开衬衣，让你看到伤疤的全貌。不是一道——是十几道烙痕叠在一起。"

        captain "我每次都回答：'不杀平民。'"

        "他的声音平静得可怕，像是在讲述别人的故事。"

        captain "那三天，我以为自己出不去了。现在想来，能撑过来的原因只有一个——他们每次问的那个问题，我每次都知道自己的答案。"
    else:
        captain "……你父亲知道。但他从不提起，因为他知道我不愿意说。"

        "他给自己倒了一杯酒，一饮而尽。"

        captain "十二年前，我还在男爵的军队里做军官。"
        captain "有一天，男爵命令我们屠杀一个村子——因为那个村子的长老拒绝多交两成税。"

        captain "我拒绝了。"

        captain "然后男爵的人把我关进了地牢。三天三夜。"
        captain "他们用烧红的铁条在我肩膀上烙——说每烙一下，就问我一次：'你还敢抗命吗？'"

        "他拉开衬衣，让你看到伤疤的全貌。不是一道——是十几道烙痕叠在一起。"

        captain "我每次都回答：'不杀平民。'"

        "他的声音平静得可怕，像是在讲述别人的故事。"

        captain "男爵判了我五十鞭，然后流放。我被丢在荒野里等死。第三天，你父亲的巡逻队发现了我。"
        captain "从那天起，我就发誓效忠你的父亲——现在，效忠于你。"

        $ captain_past_done = True  ## 既然这里讲了完整版，同步 set 避免后续再重讲

    "这时门被推开了。"

    hide player_char_img
    show elena_img at right with dissolve

    elena "听说雷恩受伤了，我带了些药膏——"

    "她看到雷恩裸露的伤疤，目光停滞了一秒。"

    elena "……这些伤。需要重新处理。"

    hide elena_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "不用麻烦——"

    hide captain_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "闭嘴，坐好。"

    $ hide_all_chars()
    "艾琳娜的语气不容置疑。她从随身的皮囊中取出药膏和绷带，开始仔细地处理旧伤。"
    "她的动作很轻，但雷恩还是不自觉地皱了几次眉。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "这些疤痕的底层组织已经坏死了……我这儿有一种特殊配方的药膏，试试吧。"
    elena "完全消除做不到，疼痛会减轻不少。"

    hide elena_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "……谢了。"

    $ hide_all_chars()
    "他的声音里有一丝不好意思——这个铁骨铮铮的汉子，在接受温柔时反而手足无措。"

    "你看着这一幕，心中感慨万千。"

    menu:
        "男爵会为此付出代价。我发誓。":
            jump ch3_deep_scar_vengeance

        "我们会讨回公道——用正义的方式":
            jump ch3_deep_scar_justice

        "这会是你最后一道伤疤。我保证。":
            jump ch3_deep_scar_promise

label ch3_deep_scar_vengeance:

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "雷恩——看着我。"

    "他抬起头。"

    player "那些在你身上留下这些伤疤的人——每一个——我都会让他们偿还。"
    player "男爵也是。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "大人……"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "这不只是为了你。是为了那个被屠杀的村子。是为了所有被男爵践踏过的人。"

    "雷恩身体微微前倾，放下了正在擦拭的剑。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "我等这句话等了十二年。"

    hide captain_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "复仇……不是没有代价。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我知道。但有些账必须清算。"

    $ change_stat("power", 5)
    $ change_rel("rel_baron", -5)

    "（你向雷恩许下了复仇的誓言。队长的士气和忠诚大大提升，但复仇之路往往充满荆棘。）"

    jump ch3_deep_scar_end

label ch3_deep_scar_justice:

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我们不会用他们对待你的方式来对待他们。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "大人？"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "男爵会受到审判。不是私刑，不是暗杀——是光明正大的审判。"
    player "让所有人看到，我们和他们不一样。"

    "雷恩缓缓点头。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "你父亲也是这么说的。"
    captain "他说——'真正的强者不需要用暴力证明自己。'"
    captain "我信了他。现在，我也信你。"

    hide captain_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "如果真能做到的话……那将改变整个北方的规则。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "那就让我们来改变规则。"

    $ change_stat("loyalty", 8)
    $ change_stat("reputation", 3)

    "（你选择了正义而非复仇。雷恩被你的信念深深打动。）"

    jump ch3_deep_scar_end

label ch3_deep_scar_promise:

    "你走到雷恩面前，轻轻按住他完好的那只肩膀。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "听着，雷恩。"
    player "这道伤疤——以及你身上所有的伤疤——它们是过去的印记。"
    player "从今天起，我不会再让你受到这样的伤害。"
    player "你是我的盾，但我也会是你的。"

    "雷恩的嘴唇抖了一下。他迅速转过头去，不让你看到他的表情。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "……别说这种话，大人。我是武人，用不着——"

    "他的声音哽住了。"

    hide captain_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "……"

    $ hide_all_chars()
    "艾琳娜无声地微笑了一下，继续包扎伤口。"

    "过了一会，雷恩才重新转过头来，目光变得无比坚定。"

    hide elena_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "大人。只要我还有一口气在，就不会让任何人伤害你。"
    captain "这是我的回答。"

    $ change_stat("loyalty", 5)
    $ change_rel("rel_elena", 3)

    "老兵的眼角湿了一下。他赶紧低下头，用粗糙的指节擦了一把。"

    jump ch3_deep_scar_end

label ch3_deep_scar_end:

    hide captain_img with dissolve
    hide elena_img with dissolve

    return

# ============================================================
# 第三章深化 - 场景三：解药与毒药
# ============================================================

label ch3_deep_cure:

    scene bg study with dissolve

    show elena_img at left with dissolve

    elena "你需要看看这个。"

    "艾琳娜在桌上铺开了一张泛黄的羊皮纸——上面画满了植物图谱和复杂的化学配方。"

    elena "这是一页毒理学手稿——我以前在侍女学院抄录过的。"
    elena "看这里——'影月草'。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "影月草……"

    if father_poisoned_known or queen_poisoned_king_known:
        "这个名字让你的心猛然一沉——你已经知道，暮色之露正是杀死父亲的毒药。而影月草，就是它的原料。"
    else:
        $ hide_all_chars()
        "这个名字让你的血液一瞬间变冷。"
        "影月草——暮色之露的原料。杀死你父亲的，就是用这种植物炼制的毒药。"
        $ father_poisoned_known = True

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "我知道这很难。但你必须听我说完。"
    elena "影月草是一种极为罕见的植物。它的汁液可以制成致命的慢性毒药——"
    elena "无色无味，受害者会在数周内逐渐衰弱，看起来就像自然生病。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    if father_poisoned_known:
        player "……我知道。就像我父亲那样。"
    else:
        player "……就像我父亲那样。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "是的。但这里写着一件非常有趣的事——"

    "她指向羊皮纸底部的一段文字。"

    elena "'影月草经过特殊处理后，可以制成强效的解毒剂。'"
    elena "'此解毒剂不仅能解除影月草本身的毒性，还能中和大部分已知的植物性毒素。'"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "杀人的毒药……能变成救命的解药？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "毒与药，本就是一体两面。"
    elena "问题是——我需要活的影月草才能尝试。而我恰好知道一处秘密花圃的位置。"

    "三天后，艾琳娜从艾登堡北境松林深处的一处隐秘谷地带回了影月草的样本。"

    scene bg study with dissolve
    show elena_img at left with dissolve

    $ hide_all_chars()
    "艾琳娜在书房里支起了一套简陋的蒸馏装置——烧瓶、冷凝管和各种奇形怪状的玻璃容器。"
    "影月草被小心地切成薄片，浸泡在一种澄清的液体中。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "必须精确控制温度。太高会分解有效成分，太低则无法激活解毒因子。"

    $ hide_all_chars()
    "她的动作极其谨慎——处理的毕竟是世界上最致命的毒素之一。"
    "你在旁边帮忙递器具，同时也在学习整个过程。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你怎么知道这些配方的？"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "侍女学院不只教礼仪、诗文和琴棋。还教毒理学和解剖学——她们说女人的武器不是刀剑，是别人看不见的东西。"
    elena "我在那里学了五年毒理学。前辈说我是他见过最有天赋的学生。"

    "她苦笑了一下。"

    elena "讽刺吧？我最擅长的技能——是杀人的技术。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你现在正在用它救人。这就够了。"

    $ hide_all_chars()
    "她看了你一眼，没有说话，但手上的动作更加稳定了。"

    "几个小时后，一小瓶浅绿色的液体静静地放在桌上。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "成功了。这就是影月草解毒剂。"
    elena "一滴就能中和足以杀死三个人的毒素。"

    $ hide_all_chars()
    "你拿起那个小瓶，对着烛光端详。浅紫色的液体在瓶中微微摇晃——"
    "看起来那么无害，那么平静。就像它的另一面——毒药——也是那么无害、那么平静。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "如果父亲在世时就有这个……"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "……但现在有了。以后不会再有人用影月草夺走我们在乎的人。"

    "问题是——这瓶解药应该怎么处理？"

    menu:
        "留着自用——关键时刻能救命":
            jump ch3_deep_cure_keep

        "把配方交给领地的治疗师——让更多人受益":
            jump ch3_deep_cure_share

        "同时再酿制一瓶毒药——以备不时之需":
            jump ch3_deep_cure_poison

label ch3_deep_cure_keep:

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "这瓶解药太珍贵了。留在我身边，关键时刻可以救命。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "明智的选择。影月草的数量有限，我们不可能大量生产。"

    "她用蜡封好瓶口，又在外面包了一层防震的软布。"

    elena "随身携带。记住——如果你发现任何中毒的迹象，立刻服用三滴。"
    elena "但如果你已经中毒超过十天……解药也无能为力了。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "……就像我父亲那样。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "不会再有下一个了。"

    $ ch3_deep_cure_found = True
    $ change_stat("intrigue", 3)

    "（你保留了这瓶珍贵的解药。在未来的某一天，它也许会成为你最后的生命线。）"

    jump ch3_deep_cure_end

label ch3_deep_cure_share:

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "这个配方应该交给领地的治疗师。"
    player "如果男爵或其他敌人再用毒药——我们需要每个角落都有解毒的能力。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "你确定？这个配方如果泄露出去——敌人也能制造解药，我们的毒药就失效了。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我宁可让毒药失效，也不愿意看着无辜的人死在影月草下。"

    "艾琳娜看了你一会儿。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "……你和你父亲真像。"
    elena "好吧。我会亲自教治疗师制备的方法。但他必须发誓保密。"

    $ ch3_deep_cure_found = True
    $ change_stat("loyalty", 8)
    $ change_stat("reputation", 3)
    $ change_rel("rel_elena", 5)

    "（你选择分享救命的知识。这体现了领主对子民的责任感，也赢得了艾琳娜更深的尊敬。）"

    jump ch3_deep_cure_end

label ch3_deep_cure_poison:

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "解药做好了……再做一瓶毒药吧。"

    "艾琳娜的手停住了。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "……你说什么？"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "有矛就要有盾，有盾也要有矛。"
    player "我不会主动用毒。但如果有一天——我们被逼到了绝境——"
    player "我需要知道我们有这个选项。"

    "走廊里有脚步声经过，又渐渐远去。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "你知道这意味着什么吗？"
    elena "影月草毒药可以悄无声息地杀人。没有解药的人，根本不会知道自己中了毒。"
    elena "你确定你想握住这种力量？"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我确定。"

    "艾琳娜深深地看了你一眼。然后她转回去，开始另一轮蒸馏。"

    hide player_char_img
    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "……好吧。但答应我一件事。"
    elena "除非万不得已——绝对不要使用。"

    hide elena_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我答应你。"

    $ hide_all_chars()
    "桌上多了第二个小瓶——紫黑色的液体，像是浓缩了的夜色。"
    "一瓶救命，一瓶夺命。"
    "它们并排摆放着，像是一个关于人性的隐喻。"

    $ ch3_deep_cure_found = True
    $ change_stat("intrigue", 8)
    $ change_rel("rel_elena", -3)

    "（你同时拥有了解药和毒药。力量在手——但艾琳娜对你的信任出现了裂痕。）"

    jump ch3_deep_cure_end

label ch3_deep_cure_end:

    hide elena_img with dissolve

    return

# ============================================================
# 第四章深化 - 场景一：王后的弱点
# ============================================================

label ch4_deep_queen_weakness:

    scene bg royal_palace with dissolve

    "到达王都的第三个夜晚，你发现了一件奇怪的事。"

    "每到深夜，王后的侍卫就会换班——不是普通的换班，而是特意留出一个无人值守的空档。"
    "大约半个时辰。"

    "在这半个时辰里，王后会独自离开寝宫，走向城堡东翼的一间密封的房间。"
    "她不带侍女，不带护卫——完全独自一人。"

    "一个铁腕统治整个王国的女人，有什么事情需要如此秘密？"

    "好奇心驱使你跟了上去。走廊里暗淡的火把勉强照亮脚下的路——"
    "你贴着墙壁，控制着呼吸，跟在她身后约三十步的距离。"

    "王后走进那间房间，没有锁门——也许是因为她确信不会有人跟来。"

    "你在门缝外驻足。"

    "透过门缝，你看到了一幅令人意想不到的画面——"

    "房间里除了一面巨大的画像之外，什么都没有。"
    "画像上是一个英俊的中年男人，穿着全套的国王礼服——那是先王的肖像。"

    $ hide_all_chars("queen_img")
    show queen_img at left with dissolve

    $ hide_all_chars()
    "王后站在画像前，姿态不再是白天那个不怒自威的铁血女王。"
    "她的肩膀微微塌下来，像是一棵被压弯了的树。"

    $ hide_all_chars("queen_img")
    show queen_img at left with dissolve
    queen "……又是一天。"

    "她对着画像说话，声音轻得像叹息。"

    queen "朝堂上那些人又在争了。南方的税收有问题。东方的边界不安宁。"
    queen "你走了之后……什么都变得更难了。"

    "她伸出手，抚摸画像上男人的脸。"

    queen "你总说我太强硬了。你说'有时候柔软也是一种力量'。"
    queen "可是——如果我不强硬，这个国家早就散了。"

    "她的声音开始颤抖。"

    queen "我好累。真的好累。"
    queen "每天醒来的第一个念头就是——今天又要对抗谁？又要防备谁？"
    queen "你在的时候……至少还有一个人，我可以不用戴面具。"

    "一滴眼泪顺着她的脸颊滑落。她没有擦，任由它掉在地上。"

    queen "想你了。"

    $ hide_all_chars()
    "就这两个字。轻轻的，碎碎的，像深秋最后一片落叶。"

    "你退后了一步。脚下的石板发出了极其细微的声响——"
    "但在这安静的走廊里，它响如惊雷。"

    "王后的身体瞬间绷紧。"

    $ hide_all_chars("queen_img")
    show queen_img at left with dissolve
    queen "谁在外面？"

    $ hide_all_chars()
    "她的声音一瞬间恢复了白天的凛冽。"

    "你来不及躲藏。"

    "门被猛然推开。王后的眼神像两把出鞘的剑——"
    "当她看到是你时，那双眼睛里闪过震惊、愤怒、然后是——恐惧。"

    "铁血女王在害怕。不是害怕你——是害怕被人看到脆弱的一面。"

    $ hide_all_chars("queen_img")
    show queen_img at left with dissolve
    queen "你看到了多少？"

    "她的声音像结冰的湖面——表面平静，下面是致命的深渊。"

    menu:
        "坦诚——是的，我看到了。但我理解。":
            jump ch4_deep_queen_empathy

        "这个秘密是一张王牌——利用它":
            jump ch4_deep_queen_exploit

        "装作什么都没看到，转身离开":
            jump ch4_deep_queen_leave

label ch4_deep_queen_empathy:

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "陛下——"

    "你咬了下嘴唇内侧。"

    player "我看到了一个思念丈夫的女人。仅此而已。"

    "王后一动不动地盯着你。"

    player "我的父亲也去世了。有些夜晚，我也会对着他留下的东西说话。"
    player "好像……只要我说了，他就还在某个地方听着。"

    $ hide_all_chars()
    "沉默。漫长的沉默。"

    "然后王后做了一件你完全没有预料到的事——"
    "她叹了口气，肩膀又塌了下来。"

    hide player_char_img
    $ hide_all_chars("queen_img")
    show queen_img at left with dissolve
    queen "你多大了？"

    hide queen_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "二十三。"

    hide player_char_img
    $ hide_all_chars("queen_img")
    show queen_img at left with dissolve
    queen "……二十三。我像你这么大的时候，也刚失去了母亲。"
    queen "那时候我以为痛苦会随时间消退。现在才知道——它只是学会了藏起来。"

    "她转身看向画像。"

    queen "他叫理查德。在位十八年。不是个好国王——但是个好丈夫。"
    queen "他总说我比他更适合坐在王座上。"

    "她苦笑了一下。"

    queen "他说对了。但我宁愿他还在。"

    hide queen_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "陛下……"

    hide player_char_img
    $ hide_all_chars("queen_img")
    show queen_img at left with dissolve
    queen "回去吧。今晚的事——"

    hide queen_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "不会有第二个人知道。"

    "她注视你片刻，微微点了点头。"

    hide player_char_img
    $ hide_all_chars("queen_img")
    show queen_img at left with dissolve
    queen "你和你父亲不一样。他太老实了。你……更复杂。"
    queen "今晚——你选择了善意。我记住了。"

    $ ch4_deep_queen_weakness = True
    $ change_stat("reputation", 5)
    $ change_rel("rel_queen", 8)

    "（你用真诚回应了王后的脆弱。一段微妙的信任在铁幕之后开始萌芽。）"

    jump ch4_deep_queen_weakness_end

label ch4_deep_queen_exploit:

    "你迅速掩饰住自己的表情，换上一副恭敬的面孔。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "陛下恕罪。我只是路过，听到有声响——"

    hide player_char_img
    $ hide_all_chars("queen_img")
    show queen_img at left with dissolve
    queen "你在说谎。你在跟踪我。"

    hide queen_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "……好吧。是的。"
    player "但请陛下放心——我看到的，只会留在我心里。"
    player "当然……如果陛下愿意在某些事情上对艾登堡网开一面——"
    player "我的沉默会更加……牢固。"

    "王后的脸上闪过一丝阴冷的笑意——但那笑意之下，是深深的失望。"

    hide player_char_img
    $ hide_all_chars("queen_img")
    show queen_img at left with dissolve
    queen "原来你也是这种人。"
    queen "好。你想要什么？"

    hide queen_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "只是一个公平的谈判机会。在朝堂之外，不被其他领主干扰的对话。"

    hide player_char_img
    $ hide_all_chars("queen_img")
    show queen_img at left with dissolve
    queen "成交。但记住——"
    queen "能威胁我一次的人，通常没有机会威胁第二次。"

    $ ch4_deep_queen_weakness = True
    $ change_stat("intrigue", 10)
    $ change_rel("rel_queen", -5)

    "（你利用了王后的秘密作为筹码。获得了谈判的优势，但也在女王心中种下了仇恨的种子。）"

    jump ch4_deep_queen_weakness_end

label ch4_deep_queen_leave:

    "你立刻低下头。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "陛下恕罪。我迷路了——"

    $ hide_all_chars()
    "你不等她回答，转身快步离开。"

    "身后没有追兵的脚步声。她选择了放你走。"

    "回到自己的房间后，你靠在门上长出了一口气。"

    "铁血女王也有人性的一面。"
    "但你选择了不去触碰它——无论是用善意还是用恶意。"

    "有些秘密，最安全的处理方式就是当它不存在。"

    $ ch4_deep_queen_weakness = True
    $ change_stat("loyalty", 3)
    $ change_stat("faith", 3)

    "（你选择了尊重王后的隐私。没有获得任何优势，但也没有树敌。）"

    jump ch4_deep_queen_weakness_end

label ch4_deep_queen_weakness_end:

    hide queen_img with dissolve

    return

# ============================================================
# 第四章深化 - 场景二：宫廷诗人
# ============================================================

label ch4_deep_poet:

    scene bg great_hall with dissolve

    "在王都的日子里，宫廷宴会是无法避免的社交场合。"

    "觥筹交错间，一个清亮的声音突然穿透了嘈杂——"

    $ hide_all_chars("court_poet_img")
    show court_poet_img at left with dissolve
    court_poet "诸位大人，容小生献上新作一首——"
    court_poet "题为《北来的鹰》。"

    $ hide_all_chars()
    "大厅安静了下来。所有人的目光都转向了角落里那个手持琴弦的年轻人。"
    "他大约二十五六岁，容貌清秀，有一种不属于这个粗犷国度的精致。"

    $ hide_all_chars("court_poet_img")
    show court_poet_img at left with dissolve
    court_poet "北方飞来一只鹰，"
    court_poet "羽翼未丰志已凌。"
    court_poet "不知王庭风云险，"
    court_poet "且看雏鸟能几程？"

    $ hide_all_chars()
    "大厅里响起了一阵意味深长的笑声。"
    "不用想也知道——这首诗说的就是你。北方来的年轻领主，不知天高地厚。"

    "但接下来的一段，让笑声戛然而止——"

    $ hide_all_chars("court_poet_img")
    show court_poet_img at left with dissolve
    court_poet "莫笑少年骨未坚，"
    court_poet "老木参天也曾纤。"
    court_poet "他日若遂凌云志，"
    court_poet "敢教日月换新天。"

    $ hide_all_chars()
    "先贬后褒——这个诗人很会拿捏分寸。既让其他贵族发笑，又不至于真正得罪你。"

    "宴会结束后，你注意到这个诗人并没有和其他宾客一起离开——"
    "他独自走向了城堡外的小径，步伐急促，不时回头张望。"

    "好奇心再次驱使你跟了上去。"

    scene bg palace_garden with dissolve

    "在花园的一个僻静角落，诗人从怀中取出一封信和一支小巧的信鸽。"
    "他正将信绑在信鸽腿上——"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "有意思的通讯方式。"

    $ hide_all_chars()
    "诗人猛然转身，脸上的血色在月光下可见地褪去。"

    $ hide_all_chars("court_poet_img")
    show court_poet_img at left with dissolve
    court_poet "你——你怎么——"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你的诗写得不错。但你更大的才华似乎是——情报工作？"

    $ hide_all_chars()
    "你从他手中夺过信鸽，取下了那封信。"
    "信是用一种你不认识的文字写的——但信封上有一个纹章。"
    "一头戴冠的狮子——那是南方莱昂王国的标志。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "莱昂王国的间谍。伪装成宫廷诗人。"

    $ hide_all_chars()
    "诗人的挣扎只持续了几秒。然后他放弃了。"

    $ hide_all_chars("court_poet_img")
    show court_poet_img at left with dissolve
    court_poet "……是的。我叫卡洛斯。莱昂王国外交密使——或者说，间谍。"
    court_poet "你打算怎么处理我？交给王后？"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "那取决于你告诉我什么。"

    $ hide_all_chars()
    "卡洛斯苦笑了一下。"

    $ hide_all_chars("court_poet_img")
    show court_poet_img at left with dissolve
    court_poet "我在这个宫廷里已经潜伏了两年。我比大多数贵族都了解这里的秘密。"
    court_poet "所以——你是要用我交换王后的恩宠，还是……有别的想法？"

    menu:
        "和他交朋友——莱昂的情报对我很有价值":
            jump ch4_deep_poet_befriend

        "揭发他——向王后表忠心":
            jump ch4_deep_poet_expose

        "招募他——为我工作":
            jump ch4_deep_poet_recruit

label ch4_deep_poet_befriend:

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "卡洛斯——你的诗真的写得不错。"

    $ hide_all_chars("court_poet_img")
    show court_poet_img at left with dissolve
    court_poet "……什么？"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我是认真的。'敢教日月换新天'——有气魄。"
    player "一个有才华的人不应该困在这种危险的工作里。"

    $ hide_all_chars("court_poet_img")
    show court_poet_img at left with dissolve
    court_poet "你在同情我？"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我在和你交朋友。"
    player "你有你的任务，我有我的困境。也许我们可以互相帮助。"
    player "我不会揭发你。你也可以时不时分享一些——莱昂那边的有趣消息。"

    $ hide_all_chars()
    "卡洛斯瞪大了眼睛，然后——出人意料地——笑了。"

    $ hide_all_chars("court_poet_img")
    show court_poet_img at left with dissolve
    court_poet "你是我见过的最奇怪的领主。"
    court_poet "好吧。就当我交了一个奇怪的朋友。"

    $ ch4_deep_court_poet = True
    $ change_stat("intrigue", 5)
    $ change_stat("reputation", 3)

    "（你与莱昂间谍建立了友谊。一条通向南方情报的秘密渠道就此打开。）"

    jump ch4_deep_poet_end

label ch4_deep_poet_expose:

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "把你交给王后——是最稳妥的选择。"

    $ hide_all_chars()
    "卡洛斯的脸色变得惨白。"

    $ hide_all_chars("court_poet_img")
    show court_poet_img at left with dissolve
    court_poet "你知道她会怎么处置我吗？这个女人——"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我知道。但我需要她的信任，超过我需要你的情报。"

    $ hide_all_chars()
    "你叫来了守卫。"

    "第二天，王后当着全体朝臣的面宣布了这个消息——一个莱昂间谍被艾登堡领主揭发。"

    "王后看向你的目光里，多了一分不同寻常的赞许。"

    hide player_char_img
    $ hide_all_chars("queen_img")
    show queen_img at left with dissolve
    queen "年轻的艾登堡领主为王国立下了功劳。朕记在心里了。"

    $ ch4_deep_court_poet = True
    $ change_stat("reputation", 8)
    $ change_rel("rel_queen", 8)

    "（你揭发了间谍，赢得了王后的信任和朝堂的声望。但也失去了一个潜在的情报来源。）"

    jump ch4_deep_poet_end

label ch4_deep_poet_recruit:

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "为莱昂工作有什么好处？他们付你多少？"

    $ hide_all_chars("court_poet_img")
    show court_poet_img at left with dissolve
    court_poet "……每月五十金币。加上事成之后的一块封地。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我出双倍。而且不用你冒生命危险。"

    $ hide_all_chars("soldier_generic_img")
    show soldier_generic_img at left with dissolve
    carlos "你要我……为你工作？"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你有才华，有经验，还有现成的情报网。"
    player "为一个远在千里之外的国王卖命，不如为一个近在眼前的领主效力。"
    player "我保护你的安全，你为我收集情报。公平交易。"

    $ hide_all_chars()
    "卡洛斯沉思了很久。"

    $ hide_all_chars("soldier_generic_img")
    show soldier_generic_img at left with dissolve
    carlos "……我需要想想。"
    carlos "但我可以告诉你一件事作为见面礼——"
    carlos "莱昂王国正在和男爵秘密接触。他们想在北方扶植一个亲莱昂的势力。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "有意思。这个消息很有价值。"

    $ hide_all_chars()
    $ hide_all_chars("soldier_generic_img")
    show soldier_generic_img at left with dissolve
    carlos "算是投名状吧。给我三天时间考虑你的提议。"

    $ ch4_deep_court_poet = True
    $ change_stat("intrigue", 8)
    $ change_stat("wealth", -3)

    "（你试图招募莱昂间谍。如果成功，你将拥有一个极为稀有的双重情报员。）"

    jump ch4_deep_poet_end

label ch4_deep_poet_end:

    hide player_char_img with dissolve

    return

# ============================================================
# 第四章深化 - 场景三：地牢的回声
# ============================================================

label ch4_deep_dungeon_echo:

    scene bg dungeon with dissolve

    "王城的地牢在城堡最深处——向下走了三层旋转阶梯才到达。"
    "潮湿、阴冷、空气中弥漫着铁锈和腐朽的气味。"

    "你来这里本是为了查看关押政治犯的情况——作为朝臣的权利之一。"
    "但在一间空牢房的墙壁上，你发现了一些字迹。"

    "石墙上密密麻麻地刻满了文字——有些已经模糊不清，有些依然清晰可辨。"
    "都是过去几十年间被关在这里的囚犯留下的。"

    "你举起火把，逐行阅读——"

    "'{i}第47天。没有人来。也许已经被遗忘了。——威廉{/i}'"
    "'{i}愿神宽恕我的罪。——无名者{/i}'"
    "'{i}玛丽亚，等我回来。——R.K.{/i}'"

    "然后——在角落里，你看到了一段让你呼吸骤停的文字——"

    "'{i}我叫康拉德·冯·艾登。今天是我被关押的第一百三十天。{/i}'"
    "'{i}女王不会释放我，因为我知道太多。{/i}'"
    "'{i}但我不后悔。有些事情必须有人说出来。{/i}'"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "康拉德·冯·艾登……"

    $ hide_all_chars()
    "那是你的祖父。"

    "你用手指轻轻触摸那些刻痕。石壁冰凉，但你仿佛能感受到祖父刻字时的体温。"

    "继续读下去——"

    "'{i}第一百八十天。女王的使者来了。她提出条件：交出北方联盟的名单，就释放我。{/i}'"
    "'{i}我拒绝了。那些人信任我，我不能出卖他们。{/i}'"

    "'{i}第二百四十天。身体越来越差。但意志还在。{/i}'"
    "'{i}如果我死在这里，希望后人知道——艾登堡家族的人，不会屈膝。{/i}'"

    "'{i}第三百六十五天。整整一年了。{/i}'"
    "'{i}今天，女王终于派人来了。不是释放——是谈判。{/i}'"
    "'{i}她需要我。北方又出了乱子，她需要我去平息。{/i}'"
    "'{i}我提出了条件——大赦北方联盟的所有成员，永远不追究。{/i}'"
    "'{i}她答应了。{/i}'"

    "最后一行字迹特别深，像是用尽了全身的力气——"

    "'{i}一年的黑暗，换来所有人的自由。值了。——康拉德·冯·艾登{/i}'"

    "你在那面墙前站了很久。"

    "父亲从未和你提起过这些。也许他觉得你还太小。也许他想保护你不受家族沉重历史的压迫。"

    "但现在你知道了——你和王室的恩怨，不是从父亲的死开始的。"
    "它已经延续了至少三代人。"

    "祖父被前任女王关押一年。父亲被现任王后的阴谋害死。"
    "现在轮到你了。"

    "这个循环——是时候做个了断了。"

    menu:
        "我要打破这个循环——用和解，而非仇恨":
            jump ch4_deep_dungeon_peace

        "我要终结王室的暴政——祖辈的屈辱不能再继续":
            jump ch4_deep_dungeon_rebellion

        "感受历史的重量——这是家族命运的一部分":
            jump ch4_deep_dungeon_fate

label ch4_deep_dungeon_peace:

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "祖父……"

    "你对着墙壁低声说话，就像王后对着画像说话一样。"

    player "您用一年的苦难换来了和平。我不会让您的牺牲白费。"
    player "这一代——由我来终结仇恨。"

    $ hide_all_chars()
    "你从地上捡起一块碎石，在祖父的铭文旁边刻下了自己的文字——"

    "'{i}三代恩怨，到此为止。——您的孙子{/i}'"

    $ change_stat("loyalty", 8)
    $ change_stat("reputation", 3)

    "（你决心打破世代循环。和解的道路漫长而艰难，但也许这正是祖父所期望的。）"

    jump ch4_deep_dungeon_end

label ch4_deep_dungeon_rebellion:

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "够了。"

    "你握紧拳头。"

    player "三代人了。三代人在王室的阴影下忍辱负重。"
    player "祖父忍了一年，换来的是什么？又一代人的苦难。"
    if father_poisoned_known:
        player "父亲忍了一辈子，换来的是什么？一杯毒酒。"
    else:
        player "父亲忍了一辈子，换来的是什么？一具冰冷的尸体和一堆谎言。"

    player "我不会再忍了。"

    $ hide_all_chars()
    "你在祖父的铭文旁刻下——"

    "'{i}忍耐的时代结束了。——您的孙子{/i}'"

    $ change_stat("power", 8)
    $ change_rel("rel_queen", -5)

    "（你立下了改变命运的誓言。推翻旧秩序的决心在地牢的黑暗中点燃。）"

    jump ch4_deep_dungeon_end

label ch4_deep_dungeon_fate:

    "你在墙前静静站着，任由那些文字的重量压在肩上。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "也许……这就是艾登堡家族的宿命。"
    player "每一代都要面对王室的考验。每一代都要做出自己的选择。"

    $ hide_all_chars()
    "祖父选择了牺牲。父亲选择了隐忍。"
    "而你——还不知道自己的选择是什么。"

    "有一件事是确定的——"
    "你不是一个人在面对。在你身后，站着两代人的勇气和智慧。"

    "你跪了下来，在潮湿的地牢里低声祈祷——"
    "不是向神祈祷，而是向祖先。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "给我力量。给我智慧。让我做出正确的选择。"

    $ change_stat("faith", 5)
    $ change_stat("loyalty", 3)

    "（你在历史的回声中汲取力量。家族的传承成为你前进的动力。）"

    jump ch4_deep_dungeon_end

label ch4_deep_dungeon_end:

    hide player_char_img with dissolve

    return

# ============================================================
# 第五章深化 - 场景一：逃兵的故事
# ============================================================

label ch5_deep_deserter:

    scene bg castle_exterior with dissolve

    "前线的斥候带回了一个俘虏——准确地说，是一个逃兵。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "大人，他是在距离艾登堡五里外的树林里被发现的。"
    captain "穿着王后军队的制服，但没有武器。看起来是逃出来的。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "带他上来。"

    $ hide_all_chars()
    "两个士兵押着一个瘦小的年轻人走上前来。"
    "他大约二十岁出头，脸上满是泥垢和擦伤，衣服破烂不堪。"
    "最引人注目的是他的眼睛——充满恐惧，像一只被猎犬追到绝路的兔子。"

    $ hide_all_chars("soldier_generic_img")
    show soldier_generic_img at left with dissolve
    deserter "大……大人饶命！我不是……我不是故意要——"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "先别急。告诉我你的名字和经历。"

    $ hide_all_chars("soldier_generic_img")
    show soldier_generic_img at left with dissolve
    "逃兵努力控制住颤抖。"

    deserter "我叫……我叫托马斯。从莱顿村来的。"
    deserter "三个月前，王后的征兵官到村里抓壮丁。"
    deserter "我是铁匠的儿子——从没拿过剑。但他们不管这些。"
    deserter "拒绝入伍的人被当场吊死在村口的大树上。我亲眼看见……"

    "他的声音哽住了。"

    deserter "我老婆怀了孩子——六个月了。她一个人在家里……"
    deserter "我不能死。至少不能死在一场我根本不理解的战争里。"
    deserter "所以昨天晚上换岗的时候，我跑了。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "大人，按照战时法律，逃兵应当就地正法。这是常规。"

    $ hide_all_chars()
    "托马斯扑通一声跪在地上，额头磕在泥地里。"

    $ hide_all_chars("soldier_generic_img")
    show soldier_generic_img at left with dissolve
    deserter "大人……求您了……我只想回家看我老婆一眼……"
    deserter "就一眼……"

    "你看着这个跪在地上的年轻人。"
    "他的手上有老茧——那是铁锤留下的。这确实是一双铁匠的手，不是士兵的手。"

    menu:
        "杀一儆百——战争没有同情心的余地":
            jump ch5_deep_deserter_execute

        "放他走——让他回家":
            jump ch5_deep_deserter_release

        "留下他——给他一个新的选择":
            jump ch5_deep_deserter_recruit

label ch5_deep_deserter_execute:

    "你闭上了眼睛。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "雷恩。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "大人？"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "执行军法。"

    $ hide_all_chars()
    "托马斯的身体像被抽去了骨头一样瘫软下来。"

    $ hide_all_chars("soldier_generic_img")
    show soldier_generic_img at left with dissolve
    deserter "不……不！大人！求您——我的孩子——"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "把他带下去。让其他俘虏看着。"
    player "然后传令全军——凡有逃亡者，格杀勿论。"

    $ hide_all_chars()
    "两个士兵架起了托马斯。他疯狂挣扎，哭喊声回荡在城墙间。"

    "雷恩看了你一眼，没有说话。他转身执行了命令。"

    "那天晚上，你做了一个梦。"
    "梦里有一个女人抱着一个新生婴儿，站在一棵大树下等待着什么。"
    "她等了很久很久。"

    $ change_stat("power", 8)
    $ change_stat("loyalty", -5)

    "（你选择了铁腕手段。军纪得到了巩固，但某些东西在你心中永远碎掉了。）"

    jump ch5_deep_deserter_end

label ch5_deep_deserter_release:

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "给他水和食物。然后——放他走。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "大人！这不合军法——"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我知道。但我不会杀一个想回家看老婆的铁匠。"

    "你走到托马斯面前，蹲下身子，平视他的眼睛。"

    player "听好。我放你走。你回家去陪你的妻子。"
    player "但你要答应我一件事——不管这场仗最后谁赢了，你好好活着。"
    player "你的孩子需要一个父亲。"

    $ hide_all_chars()
    "托马斯泣不成声。他伏在地上，额头磕得咚咚作响。"

    $ hide_all_chars("soldier_generic_img")
    show soldier_generic_img at left with dissolve
    deserter "大人的恩德……小的来世做牛做马——"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "不需要来世。这辈子做个好父亲就够了。走吧。"

    $ hide_all_chars()
    "你让人给他换了平民的衣服，塞了一些干粮和几枚铜币。"
    "晨雾很快吞没了他的身影。你低头看了看自己的手——干粮的碎屑还粘在指缝里。你拍了拍手，深深地呼了一口气。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "大人……其他士兵会怎么想？"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "他们会知道——我们和王后不一样。我们不杀无辜的人。"

    $ ch5_deep_deserter_mercy = True
    $ change_stat("loyalty", 10)
    $ change_stat("reputation", 5)

    $ hide_all_chars()
    "此后的几天，一个奇怪的现象出现了——"
    "越来越多的王后军逃兵开始主动向艾登堡投降，而不是逃回自己的村庄。"
    "因为消息已经传开了——艾登堡的领主，不杀俘虏。"

    "（你的仁慈产生了意想不到的战略效果。仁义之名，比刀剑更加锋利。）"

    jump ch5_deep_deserter_end

label ch5_deep_deserter_recruit:

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你说你是铁匠的儿子？"

    $ hide_all_chars("soldier_generic_img")
    show soldier_generic_img at left with dissolve
    deserter "是……是的。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我们缺铁匠。不缺刽子手。"
    player "你愿意为艾登堡打铁吗？修补铠甲、锻造武器——用你真正擅长的本事。"

    $ hide_all_chars()
    "托马斯难以置信地抬起头。"

    $ hide_all_chars("soldier_generic_img")
    show soldier_generic_img at left with dissolve
    deserter "大人……您是认真的？"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我从不开空头支票。"
    player "但有个条件——等这场仗打完了，你告诉我所有你知道的关于王后军队的事。"
    player "营地布局、后勤路线、士气状况——任何细节都有用。"

    $ hide_all_chars()
    $ hide_all_chars("soldier_generic_img")
    show soldier_generic_img at left with dissolve
    deserter "我知道！我全都知道！"
    deserter "我跟着军需官搬过物资——我知道他们的粮草从哪里运来！"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "很好。雷恩，给他安排到铁匠铺去。顺便让人给他的妻子带个口信——她丈夫还活着。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "……是，大人。"

    $ ch5_deep_deserter_mercy = True
    $ change_stat("intrigue", 5)
    $ change_stat("loyalty", 5)

    "（你将一个逃兵变成了有价值的资产。既得到了军事情报，又赢得了人心。）"

    jump ch5_deep_deserter_end

label ch5_deep_deserter_end:

    hide captain_img with dissolve

    return

# ============================================================
# 第五章深化 - 场景二：战前的祈祷
# ============================================================

label ch5_deep_prayer:

    scene bg church with dissolve

    "决战前夜。"

    "整座城堡笼罩在一种奇异的寂静中——不是和平的宁静，而是暴风雨前的死寂。"

    "黄昏时分，教堂的钟声敲响了。不是平日的报时，而是——召集钟。"

    "所有人都来了。"

    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve

    $ hide_all_chars()
    "士兵们穿着还没擦亮的铠甲，手上还沾着磨刀石的粉末。"
    "妇女们牵着孩子，有些怀里还抱着襁褓中的婴儿。"
    "老人们拄着拐杖，步履蹒跚但坚定。"
    "就连厨房里的帮工和马厩里的马夫都来了——全城的人，挤满了小小的教堂。"

    "主教站在圣坛前，今晚他穿的是最华丽的法袍——仿佛这是最盛大的节日。"

    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "孩子们——今晚，我不讲经文。"
    bishop "因为明天的太阳升起时，我们中的一些人——也许再也看不到第二天的日落。"

    "教堂里一片沉寂。几个妇女开始低声啜泣。"

    bishop "所以今晚，我只想和你们一起——祈祷。"
    bishop "不是祈求胜利——虽然我们都渴望胜利。"
    bishop "而是祈求——无论明天发生什么——我们都能无愧于心。"

    $ hide_all_chars()
    "他跪了下来。全教堂的人跟着跪了下来。"
    "铠甲撞击地面的声音、衣裙窸窣的声音、孩子不安的哼哼声——然后，一切归于寂静。"

    "在这寂静中，一个清澈的童声突然响起——"

    "一个大约七八岁的小女孩，不知从哪里学来了一首古老的赞美诗。"
    "她的声音在石壁间回荡，像是从天堂传来的。"

    "一个接一个，更多的声音加入了合唱。"
    "先是孩子们，然后是妇女，然后是老人——"
    "最后，连那些粗犷的士兵也加入了，他们的声音沙哑而低沉，像大地的回响。"

    "歌声充满了整个教堂，穿过了石壁，飘向了夜空。"

    "主教从圣坛后面走出来，走到你面前。"

    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "他们需要听你说几句。"

    $ hide_all_chars()
    "所有人的目光都转向了你。"
    "数百双眼睛在烛火中闪烁，恐惧、期待、坚定、迷茫，都有。"

    "这些就是你要保护的人。不是抽象的'子民'——而是活生生的面孔。"
    "那个铁匠在最后一排默默站着。前排的老妇人在擦眼泪。"
    "角落里，一个母亲把孩子搂得更紧了。"

    menu:
        "激昂的演说——鼓舞士气，许诺胜利":
            jump ch5_deep_prayer_inspire

        "坦诚的话语——承认恐惧，但强调信念":
            jump ch5_deep_prayer_honest

        "不说话——跪下来，和他们一起祈祷":
            jump ch5_deep_prayer_silent

label ch5_deep_prayer_inspire:

    "你站起身来，走到圣坛旁边。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "艾登堡的子民们！"

    "你的声音在教堂中回荡。"

    player "明天，我们将面对这一生中最大的考验。"
    player "王后的军队人数是我们的三倍。他们有更多的骑兵、更多的攻城器械。"

    "人群中传来不安的低语。"

    player "但他们没有的——是我们拥有的东西。"
    player "他们为了一个暴君的野心而战。我们——为了守护自己的家而战！"
    player "他们的士兵是被征来的农夫，心里想着逃跑。我们的战士——每一个都知道自己在保护什么！"

    "你指向人群中的妇女和孩子。"

    player "是她们。是他们。是这座城堡里的每一张面孔。"
    player "明天，当敌人的旗帜出现在地平线上——记住你身后的人。"
    player "然后问自己——你愿意让他们落入敌人手中吗？"

    $ hide_all_chars()
    "篝火噼啪作响。然后——一个士兵站了起来。"

    $ hide_all_chars("soldier_generic_img")
    show soldier_generic_img at left with dissolve
    soldier "绝不！"

    "更多的人站起来。声音越来越大。"

    crowd "绝不！！"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "明天，我会骑在最前面。如果要死，我第一个死。"
    player "但我不打算死——因为我还有太多的承诺没有兑现！"

    $ hide_all_chars()
    "教堂里爆发出雷鸣般的欢呼声。士兵们用拳头捶打铠甲——铿锵声震耳欲聋。"

    $ ch5_deep_final_prayer = True
    $ change_stat("power", 8)
    $ change_stat("reputation", 5)

    "（你的演说点燃了全城的斗志。明天的战场上，每一个战士都会为你浴血奋战。）"

    jump ch5_deep_prayer_end

label ch5_deep_prayer_honest:

    "你站起来，但没有走到圣坛旁。你就站在人群中间——和他们在一起。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我不会骗你们——我害怕。"

    "人群安静了。这不是他们期待听到的。"

    player "我害怕明天的战斗。害怕失败。害怕再也见不到你们中的某些人。"

    "你看向那个抱着孩子的母亲。"

    player "我害怕对不起你们的信任。"

    $ hide_all_chars()
    "一个老兵慢慢开口了。"

    $ hide_all_chars("soldier_generic_img")
    show soldier_generic_img at left with dissolve
    veteran "大人……我们也害怕。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我知道。所以我不会假装一切都会好的。"
    player "也许明天我们会赢。也许不会。但有一件事我可以保证——"
    player "无论结局如何，我会和你们在一起。直到最后。"

    player "不是因为我不怕死——而是因为有些东西比死亡更重要。"
    player "是你们。是这个家。是我父亲留给我的信念——"
    player "人可以被打败，但不能被击垮。"

    $ hide_all_chars()
    "教堂里很安静。没有欢呼，没有口号。"
    "但你看到了一些比那更珍贵的东西——"
    "每一张脸上，恐惧仍在，但它们的眼神中多了一样东西。"
    "是信任。是'你跟你走'的无声承诺。"

    $ ch5_deep_final_prayer = True
    $ change_stat("loyalty", 8)
    $ change_stat("reputation", 5)

    "（你用坦诚代替了虚假的豪言。人们没有疯狂，但他们的决心更加坚定。）"

    jump ch5_deep_prayer_end

label ch5_deep_prayer_silent:

    "你没有说话。"

    "你缓缓跪了下来——不是在圣坛前，而是在人群中间。"
    "和一个老兵并肩，和一个小女孩相邻。"

    "你闭上眼睛，双手合十。"

    "一秒。两秒。三秒。"

    "然后——奇迹发生了。"

    "整个教堂的人，一个接一个，都跪了下来。"
    "没有人说话。没有人命令。"
    "领主和仆人跪在同一片地面上，将军和铁匠的肩膀靠在一起。"

    "在这一刻，没有尊卑，没有贫富，没有主仆。"
    "只有一群即将共同面对命运的人。"

    "不知道过了多久。"

    "当你睁开眼睛时，蜡烛已经短了一截。"
    "但每一张面孔都平静了。恐惧没有消失——它被一种更深沉的力量所包裹。"

    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "……"

    $ hide_all_chars()
    "主教没有说话。他只是默默地流泪——不是悲伤的泪，是被深深感动的泪。"

    $ ch5_deep_final_prayer = True
    $ change_stat("faith", 10)
    $ change_stat("loyalty", 5)

    "（无声的祈祷胜过千言万语。在这一刻，整座城堡成为了一个整体。）"

    jump ch5_deep_prayer_end

label ch5_deep_prayer_end:

    hide bishop_img with dissolve

    return

# ============================================================
# 第五章深化 - 场景三：最后的家书
# ============================================================

label ch5_deep_last_letter:

    scene bg study with dissolve

    "所有人都睡了——或者至少在假装入睡。"
    "你独自坐在书房里，面前摊着一张空白的羊皮纸。"

    "旁边的墨水已经研好了。笔搁在砚台上，等待着。"

    "每个将领在大战前夜都会写一封遗书。这是传统——也是面对死亡的方式。"

    "问题是——写给谁？说什么？"

    "烛火摇曳。窗外的月亮被云遮了一半。"

    if elena_romance:
        jump ch5_deep_letter_elena
    else:
        jump ch5_deep_letter_aldric_path

label ch5_deep_letter_elena:

    "你提起笔，墨水在纸上晕开一个小小的圆点。"

    "写给她。"
    "如果明天你回不来——至少要让她知道……"

    "笔尖在纸上移动，字迹不像平时那样工整——因为手在轻轻颤抖。"

    "'{i}艾琳娜：{/i}'"
    "'{i}如果你读到这封信，说明我没能兑现回来的承诺。{/i}'"
    "'{i}对不起。{/i}'"

    "你停了一下。用力眨了下眼。"

    "'{i}在遇到你之前，我以为自己只是在为父亲的遗愿而战。{/i}'"
    "'{i}但不知道从什么时候开始——也许是你第一次在月光下教我辨认毒草的那个夜晚——{/i}'"
    "'{i}我开始为自己而战了。{/i}'"
    "'{i}因为我想看到更多的明天。和你一起的明天。{/i}'"

    "'{i}你曾经说过，暗百合的花语是'永不凋谢的秘密'。{/i}'"
    "'{i}那让我告诉你一个秘密——{/i}'"
    "'{i}每次你走进房间的时候，我的心跳都会漏一拍。{/i}'"
    "'{i}每次你笑的时候，我都在想，这个世界也许没那么糟。{/i}'"

    "'{i}如果我死了，不要为我守候。找一个能让你安定下来的人。{/i}'"
    "'{i}但偶尔——请在深夜的花园里，为我留一朵百合。{/i}'"

    "'{i}永远的，{/i}'"

    "你在信末签上了自己的名字。"

    "然后是第二页——关于领地的安排。"

    "'{i}附：如我阵亡，艾登堡代行领主由奥尔德里克暂任。{/i}'"
    "'{i}领地财政由希尔达管家协助管理。{/i}'"
    "'{i}对领民免税一年——这是他们为这场战争付出的代价的补偿。{/i}'"

    "写完了。你把信折好，用蜡封印。"

    jump ch5_deep_letter_choice

label ch5_deep_letter_aldric_path:

    "你提起笔。"
    "写给奥尔德里克——那个从小看着你长大的老管家。"
    "如果你不在了，他要承担起保护这些人的责任。"

    "'{i}奥尔德里克：{/i}'"
    "'{i}如果你读到这封信，那么我已经追随父亲去了。{/i}'"
    "'{i}对不起，留下了这么多未完成的事。{/i}'"

    "'{i}你是看着我长大的人。从我摔倒的第一步，到我握剑的第一天。{/i}'"
    "'{i}父亲不在的日子里，你就是我的父亲。{/i}'"
    "'{i}这句话我从没当面说过——现在写在纸上，希望不算太迟。{/i}'"

    "'{i}请替我照顾好艾登堡。不是作为管家——而是作为这个家的守护者。{/i}'"
    "'{i}保护那些无法保护自己的人。这是父亲的遗愿，现在也是我的。{/i}'"

    "'{i}附：如我阵亡，领主职权暂由你代行。{/i}'"
    "'{i}领地财政维持现有方针。{/i}'"
    "'{i}对领民免税一年。{/i}'"
    "'{i}善待每一个从战场上回来的人——无论胜败。{/i}'"

    "写完了。你把信折好，用蜡封印。"

    jump ch5_deep_letter_choice

label ch5_deep_letter_choice:

    "信写好了，沉甸甸的。"

    "你该怎么处理它？"

    menu:
        "封好，交给信得过的人保管":
            jump ch5_deep_letter_seal

        "撕掉——我不会死，不需要遗书":
            jump ch5_deep_letter_tear

        "亲手交给奥尔德里克":
            jump ch5_deep_letter_give

label ch5_deep_letter_seal:

    "你用家族纹章的印戒在蜡封上按下印记。"
    "然后把信交给了最信任的侍卫。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "如果明天日落时我没有回来——把这封信交给该收到它的人。"
    player "如果我回来了——把信还给我。我亲手烧掉它。"

    $ hide_all_chars()
    $ hide_all_chars("soldier_generic_img")
    show soldier_generic_img at left with dissolve
    guard "是，大人。"

    "他接过信，像接过一件圣物般郑重。"

    "你回到椅子上，闭上眼睛。"
    "奇怪的是——写完遗书之后，心里反而平静了。"
    "该说的话都说了。该安排的事都安排了。"
    "明天——只需要战斗就好。"

    $ change_stat("loyalty", 5)

    "（你坦然接受了命运的不确定。遗书像是一道安全网——希望永远不需要用到。）"

    jump ch5_deep_letter_end

label ch5_deep_letter_tear:

    "你盯着那封写好的信看了很久。"

    "然后——一把将它撕成了碎片。"

    "纸片像雪花一样飘落在桌面和地板上。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我不需要遗书。"
    player "因为我——不会——死。"

    $ hide_all_chars()
    "不是盲目的自信。是一种近乎偏执的意志。"
    "父亲死了，你活了下来。暗杀没有成功，你活了下来。"
    "王后的阴谋、男爵的刀锋、暗百合的毒药——什么都没有杀死你。"

    "明天也一样。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我还有太多事没有做完。死神想带走我——他得排队。"

    $ hide_all_chars()
    "你拿起一杯酒，一饮而尽。酒液灼烧着喉咙——像是活着的证明。"

    $ change_stat("power", 5)
    $ change_stat("reputation", 3)

    "（你用傲骨回应了死亡的邀请。这份不屈的意志，是你最锋利的武器。）"

    jump ch5_deep_letter_end

label ch5_deep_letter_give:

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    $ hide_all_chars()
    "你去找了奥尔德里克。"
    "这个时辰，他应该已经睡了——但你发现他房间的灯还亮着。"

    "推开门，老管家正坐在桌前，手里拿着一个小小的木雕——"
    "那是你五岁时送给他的生日礼物。歪歪扭扭的小马，连腿都不对称。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "大人？这么晚了——"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "奥尔德里克。"

    "你把信递给他。"

    player "这是我的遗书。如果明天我没有回来——打开它。"

    "老管家看着那封信，没有立刻接。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "大人……"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "拿着。"

    $ hide_all_chars()
    "他伸出手——那双曾经把幼年的你从马背上接下来的手——现在布满了皱纹和老年斑。"

    "他的手在颤抖。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "老爷……不，大人。"
    aldric "老奴伺候了这个家三十余年。看着您的父亲从少年变成领主，又看着您从婴儿长成大人。"
    aldric "如果……如果您明天……"

    $ hide_all_chars()
    "他的声音越来越低，最终完全说不下去了。"

    "六十多岁的老人把脸埋进了双手里——"
    "他的肩膀在剧烈地颤抖。"

    "你在他面前蹲下来，就像小时候他在你面前蹲下来一样。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "奥尔德里克。看着我。"

    "他抬起头。满脸泪水。"

    player "我会尽全力活着回来。这是我对你的承诺。"
    player "但如果万一……你要坚强。你是艾登堡最后的支柱。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "大人……您小时候摔倒了从来不哭。每次都自己爬起来。"
    aldric "老奴总是站在旁边看着，随时准备扶您——但您从来不需要。"
    aldric "老奴一直为此骄傲。但现在……老奴只希望您还是那个会哭的孩子……"
    aldric "因为那样的话，老奴就可以把您藏起来，不让您去打仗……"

    "你抱住了这个老人。用力地，像小时候他抱你那样。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你已经为我做了所有你能做的。现在——换我来保护你了。"

    $ hide_all_chars()
    "你们在那个小房间里待了很久。没有再说话。"
    "窗外传来夜莺的歌声。明天就是决战了。"

    $ change_stat("loyalty", 8)
    $ change_rel("rel_aldric", 10)

    hide aldric_img with dissolve

    "（这一刻的温情，比任何战略都更有力量。有些东西值得你用生命去守护。）"

    jump ch5_deep_letter_end

label ch5_deep_letter_end:

    hide player_char_img with dissolve

    "东方的天际已经泛起了微光。"
    "新的一天——也许是最后一天——就要开始了。"

    return

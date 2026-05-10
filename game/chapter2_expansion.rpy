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
## 第一部分：会前准备 — Pre-Council Preparations
## ============================================================

label ch2_exp_preparations:

    scene bg study with dissolve
    $ play_music("audio/music/castle_calm.ogg", fadein=2.0)

    "领主会议前夜，哈伦堡的客房里烛火摇曳。"

    "你坐在临窗的书桌前，面前摊开着五位领主的资料卷宗。每一页都是奥尔德里克在你出发前亲手整理的。"

    "窗外的夜风带着初冬的寒意，远处的塔楼上隐约传来守夜人换岗的号角声。"

    "明天就是正式会议了。你必须对每一位与会者了如指掌。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "少主，老臣虽然不能亲赴哈伦堡，但在你出发前，有些事必须再叮嘱一遍。"

    aldric "这五位领主，各有各的脾性，各有各的算盘。你若不提前摸清他们的底牌，明日的会议就是一场赌局。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "那就从头说起吧，奥尔德里克。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "先说希尔达伯爵夫人。"

    "奥尔德里克翻开第一份卷宗，上面画着一位气质威严的中年女性肖像。"

    aldric "希尔达伯爵夫人，五十二岁，出身北方古老的冯·布伦家族。她的丈夫——老伯爵——在十年前的边境战争中阵亡后，她独自执掌北疆。"

    aldric "此人城府极深，但为人正派。她看重的是秩序和规矩，厌恶投机取巧之辈。"

    aldric "你父亲在世时与她关系不错。如果你表现得稳重可靠，她可能会成为你的盟友。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "她在这次会议上最关心什么？"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "北方边境的防务。匪患和邻国的骚扰让她的军队疲于奔命。她需要其他领主分担军费和兵力。"

    aldric "如果你在边防议题上支持她，她会记住这份人情。"

    "你点了点头，在卷宗上做了一个标记。"

    aldric "接下来是格雷伯爵。"

    "第二份卷宗上画的是一位鹤发童颜的老人，面容祥和但目光深邃。"

    aldric "格雷伯爵，六十七岁，在位已经四十年。他是五位领主中资历最老的，也是最受尊敬的。"

    aldric "此人极少公开表态，但他的沉默本身就是一种力量。一旦他开口，其他人通常会附和。"

    aldric "他关心的是整个地区的长期稳定，不喜欢急功近利的年轻人。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "他对我父亲怎么看？"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "尊重，但不亲近。你父亲太锐意进取，格雷伯爵更欣赏温和渐进的风格。"

    aldric "少主若想争取他的支持，切记——少说多听。在他面前逞能只会适得其反。"

    "你在心里记下了这一条。"

    aldric "第三位，威尔斯子爵。"

    "卷宗上的肖像是一个四十来岁的男人，蓄着精心修剪的胡须，眼神闪烁不定。"

    aldric "威尔斯子爵，四十三岁，出身并不显赫，靠着精明的商业头脑积累了大量财富，后来娶了一位伯爵的女儿才跻身贵族行列。"

    aldric "此人唯利是图，但也因此最容易被收买。他的立场完全取决于利益的天平倒向哪边。"

    aldric "他与男爵有姻亲关系，但正如我之前说的——在金币面前，亲戚算什么？"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "他在会议上想得到什么？"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "贸易通道。他一直想打通东西方的商路，但需要经过其他领主的地盘。关税和过路费是他最大的痛点。"

    aldric "如果你愿意在贸易问题上让步，他会很乐意做你的朋友——至少在利益一致的时候。"

    "你若有所思地敲了敲桌面。"

    aldric "第四位，施泰因伯爵夫人。"

    "这份卷宗上的肖像是一位银发如霜的女性，面容清冷但眼神犀利。"

    aldric "施泰因伯爵夫人，五十一岁。她的丈夫去年在南方战役中阵亡，如今独自支撑领地。"

    aldric "她是这五位中最务实的一个。不谈空话，只看实际利益。她的领地以矿产闻名，但缺乏农业基础。"

    aldric "她需要稳定的粮食供应来源，而你的艾登堡恰好是产粮重镇。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "这是一个天然的合作基础。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "正是如此。但她也是最难对付的谈判对手。不要以为她因为丧夫就好欺负——她比多数男性领主都精明。"

    aldric "最后一位——维尔纳公子。"

    "最后一份卷宗上画着一个二十多岁的年轻人，面容英俊但透着一股傲气。"

    aldric "维尔纳公子，二十六岁，南方维尔纳伯爵的长子。他代替年迈的父亲出席会议。"

    aldric "此人年轻气盛，好大喜功，急于在众人面前证明自己。某种程度上……和你有几分相似。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "这话可不像恭维。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "老臣说的是事实。他可能会把你视为竞争对手，也可能成为你的盟友——取决于你如何应对他。"

    aldric "但要当心，维尔纳公子背后是他那位老谋深算的父亲。他在会议上的一举一动，未必是他自己的主意。"

    "你合上最后一份卷宗，长长地呼了一口气。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "五位领主，五种脾气，五盘算计。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "这就是权谋之庭，少主。"

    aldric "还有一件事——"

    "奥尔德里克压低了声音，表情变得严肃。"

    aldric "老臣在你出发前收到了一封匿名信。信上只写了一句话——"

    aldric "「哈伦堡的酒杯里，不只有美酒。」"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "什么意思？"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "老臣不确定。可能是有人想在会议期间下毒，也可能只是恐吓。无论如何，宴会上——不要饮来路不明的酒。"

    $ ch2_exp_aldric_briefed = True
    $ change_stat("intrigue", 5)
    $ change_rel("rel_aldric", 5)
    $ log_decision("第二章扩展", "完成会前情报准备")

    menu:
        "你还想重点了解谁？"

        "深入了解希尔达伯爵夫人的弱点":
            $ change_stat("intrigue", 3)
            $ log_decision("第二章扩展", "重点研究希尔达")

            aldric "希尔达伯爵夫人看似刀枪不入，但她有一个软肋——她的独子。"

            aldric "她的儿子在三年前的一场战斗中受了重伤，至今卧床不起。她为此四处求医，甚至不惜向教会低头。"

            aldric "如果你提到她儿子的病情——注意，是以关心的口吻，而非威胁——她或许会对你卸下防备。"

            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我记住了。"

        "深入了解格雷伯爵的过往":
            $ change_stat("reputation", 3)
            $ log_decision("第二章扩展", "重点研究格雷伯爵")

            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "格雷伯爵年轻时也是个锐意进取的领主。但四十年前的一场内战改变了他。"

            aldric "那场内战中，他最好的朋友站在了对立面。两人最终在战场上相遇——格雷伯爵亲手杀了他。"

            aldric "从那以后，他变得极度厌恶冲突，主张一切以谈判解决。这也是他在会议上总是调停角色的原因。"

            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "一个背负过去的老人。"

            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "是的。如果你在会议上表现出和平解决问题的意愿，他会高看你一眼。"

        "深入了解威尔斯子爵的商业网络":
            $ change_stat("wealth", 3)
            $ log_decision("第二章扩展", "重点研究威尔斯子爵")

            aldric "威尔斯子爵的商业版图比你想象的大得多。他不仅控制着南方的丝绸贸易，还暗中参与了东方的香料走私。"

            aldric "他有一本秘密账簿，记录着所有不光彩的交易。如果谁能拿到那本账簿，就等于握住了他的命门。"

            aldric "当然，这只是传闻。但老臣派人打探过，这个传闻的可信度很高。"

            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "有意思。继续关注这条线索。"

    hide aldric_img with dissolve

    $ hide_all_chars()
    "你独自坐在烛光中，消化着奥尔德里克传授的情报。"

    "窗外的风更大了，吹得窗棂嘎嘎作响。明天的会议，将是一场真正的考验。"

    "你闭上眼睛，在心中默默演练着各种可能的情境。"

    "不知不觉间，东方的天际泛起了鱼肚白。"

    jump ch2_exp_grand_hall

## ============================================================
## 第二部分：大厅辩论 — The Grand Hall Debate
## ============================================================

label ch2_exp_grand_hall:

    scene bg castle_hall with dissolve
    $ play_music("audio/music/great_hall.ogg", fadein=2.0)

    "哈伦堡的大厅气势恢宏。穹顶高达三丈，巨大的石柱上雕刻着历代领主的纹章。"

    "阳光从彩色玻璃窗透进来，在地板上铺开斑斓的光影。长桌呈圆形排列，象征着领主间的平等地位——至少在名义上是如此。"

    "侍从们端着银壶穿梭其间，往每位领主面前的高脚杯里斟上温热的香料酒。"

    "你想起了奥尔德里克的警告，不动声色地将杯中酒推到一边。"

    "五位领主和他们的随从已经各就各位。你环视一圈，将每个人的表情都记在心中。"

    "希尔达伯爵夫人端坐在北方的位置，面色沉稳如山。她的甲胄上镌刻着冰狼的家徽。"

    "格雷伯爵坐在东面，闭着眼睛仿佛在打盹，但你注意到他的手指在不停地轻叩扶手——那是在思考。"

    "威尔斯子爵在南面，手里把玩着一枚金币，嘴角挂着精明的微笑。"

    "施泰因伯爵夫人坐在西面，面前整齐地摆着一沓文件，显然有备而来。"

    "维尔纳公子在你的对面，以一种挑衅的姿态靠在椅背上，双臂环抱于胸前。"

    $ hide_all_chars("count_grey_img")
    show count_grey_img at left with dissolve

    count_grey "诸位，既然人到齐了，我们开始吧。"

    "格雷伯爵缓缓睁开眼睛，那双浑浊的老眼在一瞬间变得锐利无比。"

    count_grey "今日议题有三：税制改革、边境防务、贸易通路。每个议题都关乎我们各自的利益，也关乎这片土地的未来。"

    count_grey "老夫先定一个规矩——每人发言不得超过一盏茶的时间。有理说理，不要吵架。"

    "他的目光扫过在场的每一个人，最后落在维尔纳公子身上多停了一秒。"

    count_grey "第一个议题：税制改革。如今各领地的税率参差不齐，商旅苦不堪言。谁先说？"

    "威尔斯子爵率先开口。"

    hide count_grey_img
    show viscount_wells_img at right with dissolve

    viscount_wells "既然格雷大人发话了，那我就不客气了。"

    viscount_wells "如今的税制简直是一团乱麻。我的商队从东到西走一趟，光是过路费就要交五次。每个领主的税率还不一样，从百分之五到百分之二十都有。"

    viscount_wells "我的提案很简单——统一税率，设立自由贸易区。商路畅通了，大家的钱袋子都会鼓起来。"

    hide viscount_wells_img
    $ hide_all_chars("countess_hilda_img")
    show countess_hilda_img at left with dissolve

    countess_hilda "子爵大人说得轻巧。"

    "希尔达伯爵夫人的声音不高，但如同寒冰般清冽。"

    countess_hilda "统一税率？统一成多少？你当然希望越低越好——因为你靠的是商业。可我的北疆靠什么？靠税收养兵。"

    countess_hilda "如果降低关税，我拿什么维持边境防线？等到蛮族入侵的时候，你的商队能替我挡刀吗？"

    hide countess_hilda_img
    $ hide_all_chars("viscount_wells_img")
    show viscount_wells_img at left with dissolve
    viscount_wells "伯爵夫人此言差矣。商路繁荣了，整个地区的经济都会受益。到时候你的税基扩大了，就算税率低一点，总收入也未必减少。"

    hide viscount_wells_img
    $ hide_all_chars("countess_hilda_img")
    show countess_hilda_img at left with dissolve
    countess_hilda "「未必减少」——子爵大人用词真是精妙。在「未必」和「确定」之间，隔着的可是边境上数千将士的性命。"

    "两人的争论越来越激烈。格雷伯爵轻轻敲了敲桌子。"

    hide countess_hilda_img
    $ hide_all_chars("count_grey_img")
    show count_grey_img at left with dissolve

    count_grey "两位各有道理。其他人怎么看？"

    "维尔纳公子抢先开口。"

    hide count_grey_img
    show noble_werner_img at right with dissolve
    hide count_grey_img with dissolve

    noble_werner "我看问题很简单。穷的领地自然想要高税率，富的领地自然想要低税率。这不是制度问题，是实力问题。"

    noble_werner "弱者应该向强者学习如何致富，而不是靠收税来吸血。"

    "此言一出，全场的气氛骤然紧张。"

    hide noble_werner_img with dissolve
    $ hide_all_chars("countess_hilda_img")
    show countess_hilda_img at left with dissolve

    countess_hilda "维尔纳公子，你若再说一遍'弱者'这个词，我保证你会后悔。"

    hide countess_hilda_img
    $ hide_all_chars("noble_werner_img")
    show noble_werner_img at left with dissolve
    noble_werner "伯爵夫人息怒，我只是就事论事——"

    "施泰因伯爵夫人咳嗽了一声，打断了这场即将失控的对话。"

    hide noble_werner_img with dissolve
    show countess_stein_img at right with dissolve

    countess_stein "诸位，与其互相攻击，不如听听新面孔的意见。"

    "她的目光转向了你。所有人的注意力瞬间集中过来。"

    countess_stein "年轻的艾登堡领主，你对税制改革有什么看法？"

    "大厅里安静下来。这是你在领主会议上的第一次发言——你知道，这番话将决定其他人对你的第一印象。"

    hide countess_hilda_img with dissolve
    hide countess_stein_img with dissolve

    menu:
        "这是你在领主会议上的第一次公开发言。"

        "提出折中方案「联合基金 + 阶梯税率」——你的城府已经显出来" if intrigue >= 60:
            $ ch2_exp_tax_stance = "compromise"
            $ change_stat("intrigue", 5)
            $ change_stat("reputation", 5)
            $ change_rel("rel_wells", 5)
            $ change_rel("rel_hilda", 5)
            $ change_rel("rel_grey", 3)
            $ log_decision("第二章扩展", "提出折中方案")

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "诸位, 各家领地情况不同, 一刀切的税率永远会得罪一半的人。"
            player "我提议——核心商道按统一低税率, 边境领地保留独立税权。商业利润提取百分之二, 专项注入边境军费基金, 由格雷伯爵监督。"
            $ hide_all_chars()
            "大厅静了几秒。然后格雷伯爵慢慢点了点头。"
            "希尔达和威尔斯没有表态——但都没有反对。"
            "新人第一次发言能让两派都说不出反对的话, 这本身就是一个胜利。"

        "支持税制改革「降低税率，促进贸易」":
            $ ch2_exp_tax_stance = "reform"
            $ change_stat("wealth", 5)
            $ change_stat("reputation", 3)
            $ change_rel("rel_wells", 10)
            $ change_rel("rel_hilda", -5)
            $ log_decision("第二章扩展", "支持税制改革")

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我认为威尔斯子爵的提案有可取之处。"

            player "艾登堡以农业立足，我们的粮食需要市场，市场需要畅通的商路。过高的关税只会让商人绕道而行，最终损害的是所有人的利益。"

            player "当然，希尔达伯爵夫人的顾虑也合情合理。我建议我们可以设立一个过渡期——先降低关税，同时建立一个联合基金，用贸易增长的收益来补贴边境防务。"

            hide player_char_img
            show viscount_wells_img at right with dissolve

            viscount_wells "说得好！这位年轻领主比在座某些老家伙明事理多了。"

            hide viscount_wells_img
            $ hide_all_chars("countess_hilda_img")
            show countess_hilda_img at left with dissolve

            countess_hilda "联合基金？谁来管理？谁来监督？空口白话谁都会说。"

            hide countess_hilda_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "可以由格雷伯爵担任基金的管理者。他的公正是在座各位都认可的。"

            "格雷伯爵微微颔首，似乎对这个提议并不反感。"

            hide viscount_wells_img with dissolve
            hide countess_hilda_img with dissolve
            hide player_char_img with dissolve
            $ hide_all_chars("count_grey_img")
            show count_grey_img at left with dissolve

            count_grey "年轻人，你倒是会拉人下水。不过……这个方案值得进一步讨论。"

        "维护现有税制「各领地自主，不宜妄动」":
            $ ch2_exp_tax_stance = "maintain"
            $ change_stat("power", 5)
            $ change_rel("rel_hilda", 10)
            $ change_rel("rel_wells", -8)
            $ log_decision("第二章扩展", "维护现有税制")

            hide count_grey_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "恕我直言，我认为目前不是改革税制的好时机。"

            player "各领地的情况千差万别。北疆需要军费，南方依赖贸易，东部靠矿产，西边靠农业。一刀切的税率只会制造更多问题。"

            player "每个领主最了解自己领地的需要。让各领地保持自主权，这才是稳定的基础。"

            hide count_grey_img
            $ hide_all_chars("countess_hilda_img")
            show countess_hilda_img at left with dissolve

            countess_hilda "年轻人说得在理。"

            hide countess_hilda_img
            show viscount_wells_img at right with dissolve

            viscount_wells "切，又是一个守旧派。这个地区要是由你们这些人管，到死都别想进步。"

            hide viscount_wells_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "子爵大人，进步不等于冒进。稳定才是繁荣的基石。"

            "格雷伯爵投来赞许的目光。"

            hide countess_hilda_img with dissolve
            hide viscount_wells_img with dissolve
            hide player_char_img with dissolve
            $ hide_all_chars("count_grey_img")
            show count_grey_img at left with dissolve

            count_grey "年轻人虽然保守，但话不糙。"

        "提出折中方案「建立贸易联盟，渐进改革」":
            $ ch2_exp_tax_stance = "compromise"
            $ change_stat("wealth", 5)
            $ change_stat("reputation", 5)
            $ change_rel("rel_grey", 10)
            $ change_rel("rel_stein", 5)
            $ log_decision("第二章扩展", "提出折中税制方案")

            hide count_grey_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "在座各位说的都有道理。问题不在于该不该改革，而在于怎么改。"

            player "我的建议是——不要一步到位，而是分步实施。"

            player "首先，有意愿的领地可以先组建一个贸易联盟，在联盟内部试行统一的低税率。这样既不强迫任何人，又能让大家看到实际效果。"

            player "如果试行成功，其他领地自然会加入。如果失败了，也不会影响全局。"

            "在场的人互相交换着目光。"

            hide player_char_img
            show countess_stein_img at right with dissolve

            countess_stein "这个方案……很务实。"

            hide countess_stein_img
            $ hide_all_chars("count_grey_img")
            show count_grey_img at left with dissolve

            count_grey "老夫同意。不急于求成，留有余地。这才是做大事的态度。"

            hide count_grey_img with dissolve
            $ hide_all_chars("noble_werner_img")
            show noble_werner_img at left with dissolve
            hide countess_stein_img with dissolve

            noble_werner "说到底还是什么都不做——"

            hide noble_werner_img
            $ hide_all_chars("count_grey_img")
            show count_grey_img at left with dissolve
            count_grey "维尔纳公子，年轻人的通病就是以为什么都不做就等于无能。有时候，不做比做更需要勇气。"

    "税制议题暂时告一段落。格雷伯爵清了清嗓子。"

    hide noble_werner_img with dissolve
    $ hide_all_chars("count_grey_img")
    show count_grey_img at left with dissolve

    count_grey "第二个议题——边境防务。"

    "希尔达伯爵夫人立刻坐直了身子。这显然是她最关心的话题。"

    hide count_grey_img
    $ hide_all_chars("countess_hilda_img")
    show countess_hilda_img at left with dissolve
    hide count_grey_img with dissolve

    countess_hilda "诸位都知道，北方边境的压力越来越大。去年冬天，蛮族的侵扰增加了三倍。我的军队独力支撑，已经到了极限。"

    countess_hilda "我的提案是——各领地按照人口比例分摊军费，共同组建一支边境联军。"

    hide countess_hilda_img
    show noble_werner_img at right with dissolve

    noble_werner "凭什么？蛮族又打不到我们南方。"

    hide noble_werner_img
    $ hide_all_chars("countess_hilda_img")
    show countess_hilda_img at left with dissolve
    countess_hilda "说这种话的人，要么是无知，要么是短视。"

    countess_hilda "北方一旦沦陷，蛮族的铁蹄下一步就是你们的南方。到时候你再想组建联军，已经来不及了。"

    hide noble_werner_img with dissolve
    show countess_stein_img at right with dissolve

    countess_stein "我同意希尔达伯爵夫人的基本判断。边境安全关乎所有人。"

    countess_stein "但我有一个疑问——联军的指挥权归谁？"

    hide countess_stein_img
    $ hide_all_chars("countess_hilda_img")
    show countess_hilda_img at left with dissolve
    countess_hilda "自然由我来统帅。北方是我的地盘，我最了解那里的情况。"

    hide countess_stein_img
    show noble_werner_img at right with dissolve
    hide countess_stein_img with dissolve

    noble_werner "呵，所以说白了就是让我们出钱，你来握兵权？"

    "会场又开始剑拔弩张。格雷伯爵叹了口气，再次转向你。"

    hide noble_werner_img with dissolve
    hide countess_hilda_img with dissolve
    $ hide_all_chars("count_grey_img")
    show count_grey_img at left with dissolve

    count_grey "艾登堡领主，你的领地位于中部，算是个中间位置。你怎么看边境防务？"

    hide count_grey_img with dissolve

    menu:
        "边防议题直接关系到军事和外交格局。"

        "全力支持联军方案「以军事手段保障安全」":
            $ ch2_exp_border_stance = "military"
            $ change_stat("power", 5)
            $ change_stat("loyalty", 3)
            $ change_rel("rel_hilda", 15)
            $ change_rel("rel_wells", -5)
            $ change_courage(5)
            $ log_decision("第二章扩展", "支持边境联军")

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "希尔达伯爵夫人说得对。唇亡齿寒的道理，在座各位应该都懂。"

            player "我支持联军方案。艾登堡愿意出人出粮。至于军费分摊的具体比例，可以进一步协商。"

            player "但指挥权不应该由一个人独揽。我建议成立联合军事委员会，重大决策需要多数领主同意。"

            hide player_char_img
            $ hide_all_chars("countess_hilda_img")
            show countess_hilda_img at left with dissolve

            countess_hilda "你愿意出兵？"

            hide countess_hilda_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "当然。保卫北方，就是保卫我们所有人。"

            "希尔达伯爵夫人看你的目光明显柔和了许多。"

            hide player_char_img
            $ hide_all_chars("countess_hilda_img")
            show countess_hilda_img at left with dissolve
            countess_hilda "你比你父亲更有担当。他在世时总是左右逢源，不肯表态。"

            hide countess_hilda_img
            show noble_werner_img at right with dissolve

            noble_werner "又一个被这个女人牵着鼻子走的人。"

            hide noble_werner_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "维尔纳公子，坐在温暖的南方嘲笑北方人的流血牺牲，这可不是什么光彩的事。"

            "维尔纳公子的脸色骤然铁青。"

        "主张外交手段「先与蛮族谈判」":
            $ ch2_exp_border_stance = "diplomatic"
            $ change_stat("reputation", 5)
            $ change_stat("faith", 3)
            $ change_rel("rel_grey", 10)
            $ change_rel("rel_hilda", -5)
            $ log_decision("第二章扩展", "主张外交解决边境")

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "在讨论军事手段之前，我想提一个也许不太受欢迎的建议——我们有没有试过和蛮族谈判？"

            "全场哗然。"

            hide noble_werner_img
            $ hide_all_chars("countess_hilda_img")
            show countess_hilda_img at left with dissolve

            countess_hilda "和蛮族谈判？你是在开玩笑吗？"

            hide countess_hilda_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我是很认真的。年年打仗，年年花钱，年年死人——这种循环什么时候是个头？"

            player "蛮族也是人。他们南下侵扰，多半是因为北方的寒冬让他们活不下去。如果我们能和他们达成某种协议——比如开放边境贸易——也许能从根本上解决问题。"

            hide countess_hilda_img with dissolve
            $ hide_all_chars("count_grey_img")
            show count_grey_img at left with dissolve

            count_grey "有意思。老夫活了六十多年，还没听哪个领主说过这种话。"

            hide count_grey_img
            $ hide_all_chars("countess_hilda_img")
            show countess_hilda_img at left with dissolve
            countess_hilda "因为这是天真的话。你没见过蛮族的刀子。"

            hide countess_hilda_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "也许我确实天真。但天真的想法不一定就是错误的想法。"

        "提出互助同盟「各领地轮流驻防」":
            $ ch2_exp_border_stance = "alliance"
            $ change_stat("power", 3)
            $ change_stat("reputation", 5)
            $ change_rel("rel_stein", 10)
            $ change_rel("rel_hilda", 5)
            $ log_decision("第二章扩展", "提出互助同盟方案")

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "联军是一个好想法，但实施起来困难重重。指挥权的问题就够吵上三天三夜。"

            player "不如换个思路——建立轮值制度。各领地的军队轮流到北方驻防，每次三个月。这样既分担了压力，又不涉及统一指挥权的敏感问题。"

            player "同时，驻防期间的军费由所有领地共同承担。算下来，每个领地的负担其实并不大。"

            hide countess_hilda_img
            show countess_stein_img at right with dissolve

            countess_stein "这个方案可行。而且轮值制度还有一个好处——各领地的士兵可以借机了解北方的地形和战术，万一真的发生大规模入侵，配合起来更默契。"

            hide countess_stein_img
            $ hide_all_chars("countess_hilda_img")
            show countess_hilda_img at left with dissolve

            countess_hilda "……倒也不是不行。但我要求——轮值部队必须接受我的战术指导，否则去了也是添乱。"

            hide countess_hilda_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "完全同意。战场上需要统一指挥。"

    "边防议题的讨论比预想的要顺利。接下来是最后一个议题。"

    hide countess_hilda_img with dissolve
    hide countess_stein_img with dissolve
    hide noble_werner_img with dissolve
    hide count_grey_img with dissolve
    $ hide_all_chars("count_grey_img")
    show count_grey_img at left with dissolve

    count_grey "最后一个议题——贸易通路。"

    "这是威尔斯子爵的主场。他立刻来了精神。"

    hide count_grey_img with dissolve
    $ hide_all_chars("viscount_wells_img")
    show viscount_wells_img at left with dissolve

    viscount_wells "我这里有一份详细的贸易地图。"

    "他展开一张巨大的羊皮纸，上面标注着错综复杂的商路网络。"

    viscount_wells "如今从东方到西方的商路要经过五个领地的关卡。每过一个关卡就要缴纳一次过路费。商人们不堪重负，很多已经转走海路了。"

    viscount_wells "我的提案是——开辟一条'黄金走廊'。沿这条路线取消所有关卡，建立统一的通行证制度。商人只需缴纳一次费用，沿途所有领地按比例分配。"

    hide viscount_wells_img
    $ hide_all_chars("countess_stein_img")
    show countess_stein_img at left with dissolve

    countess_stein "分配比例怎么算？"

    hide countess_stein_img
    $ hide_all_chars("viscount_wells_img")
    show viscount_wells_img at left with dissolve
    viscount_wells "按照商路经过各领地的里程来算，最公平。"

    hide countess_stein_img
    show noble_werner_img at right with dissolve
    hide countess_stein_img with dissolve

    noble_werner "这条'黄金走廊'恰好经过你的地盘最长，你当然觉得公平。"

    hide noble_werner_img
    $ hide_all_chars("viscount_wells_img")
    show viscount_wells_img at left with dissolve
    viscount_wells "维尔纳公子，我在这里谈的是生意，不是阴谋。如果你有更好的分配方式，请说。"

    "维尔纳公子哼了一声，没有回答。"

    hide viscount_wells_img with dissolve
    hide noble_werner_img with dissolve
    $ hide_all_chars("count_grey_img")
    show count_grey_img at left with dissolve

    count_grey "艾登堡领主呢？你的领地也在商路沿线。"

    hide count_grey_img with dissolve

    menu:
        "贸易通路关系到你的领地经济。"

        "支持自由贸易「开放商路，减少管制」":
            $ ch2_exp_trade_stance = "free"
            $ change_stat("wealth", 8)
            $ change_rel("rel_wells", 10)
            $ change_rel("rel_people", 5)
            $ log_decision("第二章扩展", "支持自由贸易")

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我支持黄金走廊的构想。商路畅通对所有人都是好事。"

            player "但我还想补充一点——除了取消关卡，我们还应该沿途建设驿站和仓储设施。这些基础建设的投入，短期看是支出，长期看会带来数倍的回报。"

            show viscount_wells_img at right with dissolve

            viscount_wells "英雄所见略同！年轻人，你有做生意的天分。"

            hide viscount_wells_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我只是觉得，让百姓过上好日子，比在会议上吵架更重要。"

            $ change_rel("rel_people", 5)

        "主张严格管控「保护本地产业」":
            $ ch2_exp_trade_stance = "regulated"
            $ change_stat("power", 5)
            $ change_rel("rel_wells", -10)
            $ change_rel("rel_hilda", 5)
            $ log_decision("第二章扩展", "主张贸易管控")

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "自由贸易听起来很美好，但现实是——如果完全开放商路，外来的廉价商品会摧毁本地的手工业。"

            player "我的领地有很多依靠手工业为生的百姓。如果他们的生计被打破，社会动荡在所难免。"

            player "我主张——开放贸易可以，但必须设立保护条款。对某些关键行业，需要保留关税壁垒。"

            show viscount_wells_img at right with dissolve

            viscount_wells "又是一个短视的保护主义者。"

            hide viscount_wells_img
            $ hide_all_chars("countess_hilda_img")
            show countess_hilda_img at left with dissolve

            countess_hilda "他说得有道理。不是所有领地都像你那样靠倒卖别人的东西过日子。"

        "提出利益交换「以贸易权换取政治支持」":
            $ ch2_exp_trade_stance = "monopoly"
            $ change_stat("intrigue", 8)
            $ change_stat("wealth", 3)
            $ change_rel("rel_wells", 5)
            $ change_rel("rel_stein", 8)
            $ log_decision("第二章扩展", "以贸易权换取政治支持")

            hide countess_hilda_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "贸易通路的问题，归根结底是利益分配的问题。与其争论谁占便宜谁吃亏，不如直说——各位想从这条商路上得到什么。"

            player "我提议，我们把贸易权和其他议题挂钩。比如——支持边防联军的领地，可以享受更低的通行费。这样大家都有动力合作。"

            hide countess_hilda_img
            hide player_char_img
            $ hide_all_chars("countess_stein_img")
            show countess_stein_img at left with dissolve

            countess_stein "把军事义务和贸易利益绑定？这个主意……有趣。"

            hide countess_stein_img
            show viscount_wells_img at right with dissolve

            viscount_wells "也就是说，出钱多的人赚得也多？这我没意见。"

            hide viscount_wells_img
            $ hide_all_chars("countess_hilda_img")
            show countess_hilda_img at left with dissolve
            hide countess_stein_img with dissolve

            countess_hilda "如果这意味着我的北疆能得到更多支持，我也可以考虑。"

    "三个议题全部讨论完毕。格雷伯爵宣布上午的会议到此结束，下午各领主可以私下交流。"

    hide countess_hilda_img with dissolve
    hide viscount_wells_img with dissolve
    hide player_char_img with dissolve
    $ hide_all_chars("count_grey_img")
    show count_grey_img at left with dissolve

    count_grey "诸位，午膳已备好。休息一下，下午继续。"

    hide count_grey_img with dissolve

    "你注意到，在散会的混乱中，施泰因伯爵夫人朝你微微点了点头——那是一个不易察觉的邀请。"

    jump ch2_exp_private_audiences

## ============================================================
## 第三部分：私下会面 — Private Audiences
## ============================================================

label ch2_exp_private_audiences:

    scene bg castle_hall with dissolve
    $ play_music("audio/music/castle_calm.ogg", fadein=2.0)

    "午膳过后，领主们三三两两地散开。有人在花园中散步，有人回房休息。"

    "你站在走廊的转角处，思考着下午该如何利用这段自由时间。"

    "施泰因伯爵夫人的暗示你已经注意到了。但其他人也可能想找你私谈。"

    "你的时间有限，最多只能安排两次私下会面。"

    $ ch2_exp_private_count = 0

    if ch1_deep_widow_verdict == "pardon":

        $ hide_all_chars()
        "走廊的侧窗投入午后的金色光线。就在你思考着如何分配时间时，一个熟悉的身影从走廊转角匆匆走过。"

        "那个少年——偷面包的汉斯。他手里端着一个茶盘，几缕蒸汽从茶杯口升起。"

        "他看到了你，突然停下脚步。眼睛里闪过一瞬间的惊慌，随即他深深低了头。"

        "那是一个完全不同的姿态。不是受审时被迫的低眉顺眼，而是一种内在的——敬畏。"

        "他小心翼翼地端正茶盘，生怕茶水溅出来。手还是会抖，但不是来自恐惧。"

        "「大人。」他轻声说，声音比半年前沉稳多了。「茶还是热的。」"

        "然后他继续向前走。步履还是个少年的模样，但茶盘端得平平稳稳，没有一滴溅出。"

label ch2_exp_private_choose:

    if ch2_exp_private_count >= 2:
        jump ch2_exp_banquet

    if ch2_exp_private_count == 0:
        "你决定先去见谁？"
    else:
        "你还有时间见一个人。"

    menu:

        "拜访施泰因伯爵夫人" if not ch2_exp_stein_pact:
            $ ch2_exp_private_count += 1
            jump ch2_exp_meet_stein

        "拜访希尔达伯爵夫人" if not ch2_exp_hilda_alliance:
            $ ch2_exp_private_count += 1
            jump ch2_exp_meet_hilda

        "拜访格雷伯爵" if not ch2_exp_grey_secret:
            $ ch2_exp_private_count += 1
            jump ch2_exp_meet_grey

        "拜访威尔斯子爵" if not ch2_exp_wells_bribed:
            $ ch2_exp_private_count += 1
            jump ch2_exp_meet_wells

        "直接前往宴会":
            jump ch2_exp_banquet

## ── 施泰因伯爵夫人 ──

label ch2_exp_meet_stein:

    scene bg study with dissolve
    $ play_music("audio/music/castle_calm.ogg", fadein=2.0)

    "你来到施泰因伯爵夫人的临时书房。她的侍从将你引到一间布置简洁的房间里。"

    "伯爵夫人坐在窗边，面前的桌上整齐地摆着几份文件和一个精致的矿石标本。"

    $ hide_all_chars("countess_stein_img")
    show countess_stein_img at left with dissolve

    countess_stein "请坐。我不喜欢绕弯子，所以直说了。"

    countess_stein "我知道你的领地盛产粮食。我的领地盛产铁矿和银矿。我们之间有天然的互补关系。"

    hide countess_stein_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你想提议一个贸易协定？"

    hide player_char_img
    $ hide_all_chars("countess_stein_img")
    show countess_stein_img at left with dissolve
    countess_stein "不只是贸易。"

    "她从抽屉里取出一封信，推到你面前。"

    countess_stein "我丈夫去世后，我的领地看起来像一块肥肉。北边有蛮族，南边有维尔纳家族虎视眈眈。我需要一个可靠的盟友。"

    countess_stein "你也需要。你是新任领主，根基未稳。我们联手，才能在这张棋盘上站稳脚跟。"

    hide countess_stein_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你的条件是什么？"

    hide player_char_img
    $ hide_all_chars("countess_stein_img")
    show countess_stein_img at left with dissolve
    countess_stein "很简单——我们签订互助条约。军事上互相支援，经济上优先通商。如果一方遭到攻击，另一方必须在十五日内出兵救援。"

    countess_stein "作为诚意，我愿意在未来一年以成本价向你供应铁矿。你的军队需要武器装备，我知道。"

    menu:
        "施泰因伯爵夫人的提议很有吸引力，但互助条约意味着承担义务。"

        "接受互助条约「结成正式同盟」":
            $ ch2_exp_stein_pact = True
            $ ch2_exp_stein_trust = True
            $ change_stat("power", 5)
            $ change_stat("wealth", 5)
            $ change_rel("rel_stein", 20)
            $ log_decision("第二章扩展", "与施泰因伯爵夫人结盟")

            hide countess_stein_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我接受。艾登堡与施泰因结盟，对双方都有利。"

            hide player_char_img
            $ hide_all_chars("countess_stein_img")
            show countess_stein_img at left with dissolve
            countess_stein "很好。你比我预想的果断。"

            "她取出一份早已拟好的条约，你仔细阅读后签上了自己的名字。"

            countess_stein "还有一件事——私下告诉你。"

            "她压低声音。"

            countess_stein "维尔纳公子的父亲正在秘密联络男爵，企图对你和我的领地形成夹击之势。他们可能会在明天的闭幕会议上突然发难。"

            hide countess_stein_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你是怎么知道的？"

            hide player_char_img
            $ hide_all_chars("countess_stein_img")
            show countess_stein_img at left with dissolve
            countess_stein "我有我的渠道。这就是我急着找你结盟的原因——单打独斗，我们都扛不住他们联手。"

            $ ch2_exp_secret_letter = True
            $ change_stat("intrigue", 5)

        "提出修改条件「只签贸易协议，暂不军事结盟」":
            $ change_stat("wealth", 5)
            $ change_rel("rel_stein", 8)
            $ log_decision("第二章扩展", "与施泰因伯爵夫人签署贸易协议")

            hide countess_stein_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "互助条约对我来说步子太大了。我的领地才刚刚稳定，现在就承诺军事义务，恐怕力不从心。"

            player "但贸易合作我完全赞成。先从经济上建立互信，军事结盟的事以后再谈。"

            hide player_char_img
            $ hide_all_chars("countess_stein_img")
            show countess_stein_img at left with dissolve
            countess_stein "也好。你比你父亲谨慎。谨慎不是坏事。"

            "你们签下了一份贸易协议。虽然不是正式同盟，但这已经是一个良好的开端。"

            countess_stein "不过我还是要提醒你——维尔纳家族对你并不友善。小心那个年轻人。"

    hide countess_stein_img with dissolve

    "你告辞离开，心中多了几分底气。"

    jump ch2_exp_private_choose

## ── 希尔达伯爵夫人 ──

label ch2_exp_meet_hilda:

    scene bg castle_hall with dissolve
    $ play_music("audio/music/campfire.ogg", fadein=2.0)

    "你在城堡的练武场找到了希尔达伯爵夫人。她正在观看自己的亲卫骑士操练。"

    "即使在会议间隙，她也没有放松对军队的关注。这就是一个边疆领主的习惯。"

    $ hide_all_chars("countess_hilda_img")
    show countess_hilda_img at left with dissolve

    countess_hilda "来了？"

    "她头也不回地说道，仿佛背后长了眼睛。"

    countess_hilda "你今天在会上的表现还不错。至少比那个维尔纳家的小子强。"

    hide countess_hilda_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "伯爵夫人过奖了。"

    hide player_char_img
    $ hide_all_chars("countess_hilda_img")
    show countess_hilda_img at left with dissolve
    countess_hilda "我不奖人。"

    "她转过身来，双臂交叉于胸前，冰蓝色的眼睛直视着你。"

    countess_hilda "你父亲和我算是旧交。他这个人，太圆滑了，但心不坏。"

    countess_hilda "你呢？我还看不透。"

    hide countess_hilda_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "也许我自己都还在摸索。"

    hide player_char_img
    $ hide_all_chars("countess_hilda_img")
    show countess_hilda_img at left with dissolve
    countess_hilda "至少你够诚实。"

    "她的手指在袖口上轻轻摩挲，像是在做某种决定。"

    countess_hilda "我有个请求。这件事不方便在会上提——它涉及我的私事。"

    hide countess_hilda_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "请说。"

    hide player_char_img
    $ hide_all_chars("countess_hilda_img")
    show countess_hilda_img at left with dissolve
    countess_hilda "我的儿子……你可能听说了，他三年前在战斗中受了重伤。至今半身不遂。"

    "铁石般的女人在提到儿子时，眼中闪过一丝不易察觉的脆弱。"

    countess_hilda "有人告诉我，南方有一位名医，能治好他的伤。但那位名医在维尔纳家族的领地上。"

    countess_hilda "维尔纳老伯爵拒绝了我的请求。他想用这件事来要挟我在会议上让步。"

    hide countess_hilda_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "这也太卑鄙了。"

    hide player_char_img
    $ hide_all_chars("countess_hilda_img")
    show countess_hilda_img at left with dissolve
    countess_hilda "权谋之庭里没有卑鄙，只有筹码。但我……不想拿北方将士的安全去换我儿子的健康。"

    countess_hilda "如果你有办法帮我把那位名医请到艾登堡——绕过维尔纳家族——我会记住这份恩情。"

    menu:
        "希尔达伯爵夫人罕见地展露了脆弱的一面。"

        "答应帮助她「承诺找到那位名医」":
            $ ch2_exp_hilda_alliance = True
            $ change_rel("rel_hilda", 20)
            $ change_stat("reputation", 5)
            $ change_courage(5)
            $ log_decision("第二章扩展", "答应帮助希尔达伯爵夫人")

            hide countess_hilda_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我答应你。回去之后我会想办法联系那位名医。"

            hide player_char_img
            $ hide_all_chars("countess_hilda_img")
            show countess_hilda_img at left with dissolve
            countess_hilda "你知道这意味着得罪维尔纳家族吗？"

            hide countess_hilda_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "在做正确的事和讨好所有人之间，我选择前者。"

            "希尔达伯爵夫人的目光在你脸上停了很久。"

            hide player_char_img
            $ hide_all_chars("countess_hilda_img")
            show countess_hilda_img at left with dissolve
            countess_hilda "好。我相信你。"

            "她伸出手——那是一只布满老茧的手，属于一个真正的战士。"

            countess_hilda "从今天起，北疆与艾登堡共进退。"

            "你握住了她的手。那一刻，你感受到了某种超越政治算计的东西。"

        "婉言推辞「表示会尽力但不做承诺」":
            $ change_rel("rel_hilda", 3)
            $ log_decision("第二章扩展", "未对希尔达伯爵夫人做出承诺")

            hide countess_hilda_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "伯爵夫人，我理解您的心情。但说实话，以艾登堡目前的实力，公开得罪维尔纳家族的风险太大。"

            player "我会尽力帮忙，但不能做出我可能无法兑现的承诺。"

            hide player_char_img
            $ hide_all_chars("countess_hilda_img")
            show countess_hilda_img at left with dissolve
            countess_hilda "……至少你没有骗我。"

            "她的表情恢复了冰冷。"

            countess_hilda "你和你父亲，倒是一个模子里刻出来的。"

            "你不确定这是褒义还是贬义。"

    hide countess_hilda_img with dissolve

    jump ch2_exp_private_choose

## ── 格雷伯爵 ──

label ch2_exp_meet_grey:

    scene bg study with dissolve
    $ play_music("audio/music/castle_calm.ogg", fadein=2.0)

    "格雷伯爵在哈伦堡的图书室里。偌大的房间只点着一盏油灯，老伯爵坐在扶手椅里，手中握着一卷泛黄的古籍。"

    $ hide_all_chars("count_grey_img")
    show count_grey_img at left with dissolve

    count_grey "哦，年轻人。进来坐。"

    "他放下书，用那双浑浊但深邃的眼睛打量着你。"

    count_grey "你今天在会上的发言让老夫印象深刻。不论你选择了哪种立场，至少你有自己的想法。"

    count_grey "这比那些只会附和别人的人强多了。"

    hide count_grey_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "格雷大人，晚辈有些事想请教。"

    hide player_char_img
    $ hide_all_chars("count_grey_img")
    show count_grey_img at left with dissolve
    count_grey "你想问什么？"

    hide count_grey_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我想知道——在这些领主中，谁是值得信任的？谁又需要提防？"

    "格雷伯爵缓缓摇头。"

    hide player_char_img
    $ hide_all_chars("count_grey_img")
    show count_grey_img at left with dissolve
    count_grey "年轻人，这个问题本身就问错了。在权力的游戏中，没有永远的朋友，也没有永远的敌人。今天的盟友明天可能就是对手。"

    count_grey "但老夫可以告诉你两件事。"

    count_grey "第一——威尔斯子爵虽然贪财，但他从不害人。他只想赚钱。相比之下，那些声称不图名利的人反而更危险。"

    count_grey "第二——维尔纳老伯爵让他儿子来参加会议，绝不是为了锻炼年轻人。他另有目的。"

    hide count_grey_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "什么目的？"

    hide player_char_img
    $ hide_all_chars("count_grey_img")
    show count_grey_img at left with dissolve
    count_grey "老夫暂时不能说。但你注意看——今晚宴会上维尔纳公子的举动。如果老夫没有猜错的话……"

    "他没有说完，而是从桌上取出一个密封的信封。"

    count_grey "这是你父亲在世时托我保管的东西。他说过——如果有一天他不在了，把这个交给他的继承人。"

    "你接过信封，心中一震。"

    hide count_grey_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "父亲的……遗物？"

    hide player_char_img
    $ hide_all_chars("count_grey_img")
    show count_grey_img at left with dissolve
    count_grey "打开看看。"

    $ hide_all_chars()
    "你小心翼翼地拆开信封。里面是一张薄薄的纸条，上面只有一行潦草的字迹——"

    "「信任奥尔德里克。远离百合花。」"

    "你的心猛地一沉。百合花——那不正是暗百合组织的标志吗？"

    $ ch2_exp_grey_secret = True
    $ ch2_exp_grey_favor = True
    $ change_stat("loyalty", 8)
    $ change_rel("rel_grey", 15)
    $ log_decision("第二章扩展", "从格雷伯爵处获得父亲遗物")

    hide count_grey_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "格雷大人……您知道暗百合吗？"

    "格雷伯爵端起酒杯，转了两圈，又放下了。"

    hide player_char_img
    $ hide_all_chars("count_grey_img")
    show count_grey_img at left with dissolve
    count_grey "知道。但今天不是谈那件事的时候。"

    count_grey "年轻人，你要记住——有些秘密，知道得越早越好。有些秘密，知道得越晚越安全。"

    count_grey "关于暗百合的事，属于前者。"

    "他站起身来，拍了拍你的肩膀。"

    count_grey "去吧。宴会快开始了。记住老夫的话——今晚，注意观察。"

    hide count_grey_img with dissolve

    jump ch2_exp_private_choose

## ── 威尔斯子爵 ──

label ch2_exp_meet_wells:

    scene bg castle_hall with dissolve
    $ play_music("audio/music/tavern_lively.ogg", fadein=2.0)

    "你在哈伦堡的酒窖里找到了威尔斯子爵。他正品鉴一桶新到的红酒，嘴里啧啧有声。"

    $ hide_all_chars("viscount_wells_img")
    show viscount_wells_img at left with dissolve

    viscount_wells "哟，艾登堡的小领主！来来来，尝尝这个——从东方运来的，路上就花了三个月。"

    "他热情地递过一杯深红色的酒液。你想起奥尔德里克的警告，但威尔斯子爵正在用期待的目光看着你。"

    menu:
        "威尔斯子爵递来了一杯酒。"

        "接过酒杯，但只是假装品尝":
            $ change_stat("intrigue", 3)

            "你举起酒杯，在嘴唇上轻轻碰了一下，然后放下。"

            hide viscount_wells_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "好酒。果然名不虚传。"

            hide player_char_img
            $ hide_all_chars("viscount_wells_img")
            show viscount_wells_img at left with dissolve
            viscount_wells "你这小子，一看就不是个酒鬼。来，坐坐。"

        "礼貌地拒绝":
            $ change_rel("rel_wells", -3)

            hide viscount_wells_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "子爵大人好意心领，但我下午还有事，不宜饮酒。"

            hide player_char_img
            $ hide_all_chars("viscount_wells_img")
            show viscount_wells_img at left with dissolve
            viscount_wells "哎，年轻人怎么这么无趣。算了算了，说正事吧。"

    viscount_wells "我知道你来找我干什么。无非是想打探我的底牌嘛。"

    "他大大咧咧地坐下来，金币在指间翻飞。"

    viscount_wells "我跟你说实话——我这个人很简单。谁能让我赚钱，我就跟谁。"

    viscount_wells "你的领地产粮食，我需要粮食来做贸易。你需要商路来卖粮食，我手里有最好的商路。"

    viscount_wells "咱们合作，很简单的买卖。"

    hide viscount_wells_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你和冯·哈根男爵不是姻亲吗？"

    hide player_char_img
    $ hide_all_chars("viscount_wells_img")
    show viscount_wells_img at left with dissolve
    viscount_wells "姻亲是姻亲，生意是生意。我那个大舅子只知道打打杀杀，满脑子都是领地扩张。跟他做生意？等着赔本吧。"

    viscount_wells "反而是你——上午在会上的发言，让我看出你是个务实的人。"

    "他从怀里掏出一份合同。"

    viscount_wells "这是一份粮食供应合同。你以优惠价给我提供粮食，我保证你的商品可以免费通过我的地盘。有效期三年。"

    viscount_wells "当然，如果你还想要更多——"

    "他凑近了一些，声音压得很低。"

    viscount_wells "我有一些……不太方便公开的信息。关于维尔纳家族的。"

    viscount_wells "但这些信息的价格不低。你需要再加一个条件——允许我的商队在你的领地上设立免税仓库。"

    menu:
        "威尔斯子爵的提议夹杂着利益和情报。"

        "签署合同并接受额外条件「获取维尔纳家族情报」":
            $ ch2_exp_wells_bribed = True
            $ change_stat("wealth", -5)
            $ change_stat("intrigue", 8)
            $ change_rel("rel_wells", 15)
            $ log_decision("第二章扩展", "与威尔斯子爵达成全面合作")

            hide viscount_wells_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "成交。但我要先看到情报。"

            hide player_char_img
            $ hide_all_chars("viscount_wells_img")
            show viscount_wells_img at left with dissolve
            viscount_wells "爽快！我喜欢跟爽快人做生意。"

            "他从靴筒里抽出一张折叠的纸条——显然早就准备好了。"

            viscount_wells "维尔纳老伯爵一个月前秘密购买了大量武器。数量远超他的领地军队所需。"

            viscount_wells "而且——这些武器的运输方向不是往南，而是往北。"

            "你皱起了眉头。武器往北运——那不是维尔纳的地盘，而是你和希尔达伯爵夫人的方向。"

            hide viscount_wells_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "他在武装什么人？"

            hide player_char_img
            $ hide_all_chars("viscount_wells_img")
            show viscount_wells_img at left with dissolve
            viscount_wells "这就不是我的合同范围了。但聪明人应该能猜到一二。"

            $ change_stat("power", 3)

        "只签基本合同「不做额外交易」":
            $ change_stat("wealth", 3)
            $ change_rel("rel_wells", 8)
            $ log_decision("第二章扩展", "与威尔斯子爵签署基本合同")

            hide viscount_wells_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "粮食合同我签。但免税仓库的事需要回去和管家商量。"

            hide player_char_img
            $ hide_all_chars("viscount_wells_img")
            show viscount_wells_img at left with dissolve
            viscount_wells "行吧，保守派。那情报的事就算了。"

            "他耸耸肩，收起了那张神秘的纸条。"

            viscount_wells "不过我还是劝你一句——注意维尔纳家族。那老狐狸在下一盘大棋。"

    hide viscount_wells_img with dissolve

    "你离开酒窖时，脑中不断回响着各种信息。这些领主之间的关系比你想象的还要复杂。"

    jump ch2_exp_private_choose

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

    "这是一场表面上的欢宴。但你知道，真正的较量往往在酒杯的碰撞声中展开。"

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
            player "我的祝词——敬真正有勇气站出来承担责任的人。不论年龄，不论出身。"

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

            player "我听说有个故事——一只老狐狸对一只年轻的狼说：'你只是靠了一副好牙齿。'年轻的狼回答说：'是啊，但至少我的牙齿还在。'"

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
        "走廊尽头传来轻微的声响。你必须立刻做出决定。"

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

                    count_grey "年轻人，你做了一个勇敢的决定。但不一定是一个聪明的决定。"

                    hide count_grey_img with dissolve

                    $ change_rel("rel_queen", -15)

            hide elena_img with dissolve

        "悄悄跟踪「暗中观察」":
            $ ch2_exp_night_choice = "follow"
            $ change_stat("intrigue", 10)
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

            "她从你身边不到两步的距离经过。黑暗中你只能看到她的眼睛——冰冷、空洞，像是一个没有感情的工具。"

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

    "它不只是一场关于税制和贸易的讨论——它是一张巨大的棋盘，而每个人都在扮演着自己的角色。"

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
    if ch2_exp_tax_stance == "reform" or (ch2_exp_tax_stance == "" and council_outcome == "反对"):
        count_grey "关于税制——我们将联名上书反对新税法，同时成立联合基金保障各领地的基本收入。"
    elif ch2_exp_tax_stance == "maintain" or (ch2_exp_tax_stance == "" and council_outcome == "支持"):
        count_grey "关于税制——各领地将配合王室推行新税法，但要求派遣监察官保障公正执行。"
    elif ch2_exp_tax_stance == "compromise" or (ch2_exp_tax_stance == "" and council_outcome == "折中"):
        count_grey "关于税制——有意愿的领地可以先行试点新税率，其余领地保留观望权。"
    else:
        count_grey "关于税制——各领地同意每年就税收问题进行一次协商。"

    if ch2_exp_border_stance == "military":
        count_grey "关于边防——各领地同意按比例分摊军费，组建联合军事委员会。"
    elif ch2_exp_border_stance == "diplomatic":
        count_grey "关于边防——在加强防御的同时，派出使者与北方部族接触，探索和平解决的可能。"
    elif ch2_exp_border_stance == "alliance":
        count_grey "关于边防——各领地的军队将实行轮值驻防制度，由希尔达伯爵夫人负责战术指导。"
    else:
        count_grey "关于边防——各领地同意加强巡逻，共享边境情报。"

    if ch2_exp_trade_stance == "free":
        count_grey "关于贸易——开辟黄金走廊，取消沿途关卡，建立统一通行证制度。"
    elif ch2_exp_trade_stance == "regulated":
        count_grey "关于贸易——在开放部分商路的同时，保留各领地对关键产业的保护权。"
    elif ch2_exp_trade_stance == "monopoly":
        count_grey "关于贸易——将贸易权利与军事义务挂钩，建立互惠的合作框架。"
    else:
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

    if ch2_exp_stein_pact:
        countess_stein "盟友。这个词我不轻易说出口。希望你不会让我失望。"
    else:
        countess_stein "你是个有潜力的年轻人。下次见面，也许我们可以谈更多。"

    "希尔达伯爵夫人骑着她的战马，在经过你身边时勒住了缰绳。"

    hide countess_stein_img with dissolve
    $ hide_all_chars("countess_hilda_img")
    show countess_hilda_img at left with dissolve

    if ch2_exp_hilda_alliance:
        countess_hilda "我的人很快会联系你，关于那件事。谢谢你。"
    else:
        countess_hilda "年轻人，你还有很长的路要走。别松懈。"

    "格雷伯爵最后一个离开。他坐在马车里，掀开帘子看了你一眼。"

    hide countess_hilda_img with dissolve
    $ hide_all_chars("count_grey_img")
    show count_grey_img at left with dissolve

    count_grey "记住老夫的话——远离百合花。"

    hide count_grey_img with dissolve

    $ hide_all_chars()
    "马车渐行渐远，消失在蜿蜒的山路上。"

    "你深深地吸了一口气。冬日的空气冷冽清新，但你心中的火焰比任何时候都烧得旺盛。"

    "这场领主会议，你不只是参与者——你已经成为了棋盘上一枚不可忽视的棋子。"

    "也许有一天，你会成为执棋之人。"

    ## 结算画面

    ## 属性变化总结
    if ch2_exp_stein_pact:
        "你与施泰因伯爵夫人结成了正式同盟。"
        $ change_stat("power", 3)

    if ch2_exp_hilda_alliance:
        "你赢得了希尔达伯爵夫人的信任。北疆与艾登堡共进退。"
        $ change_stat("loyalty", 5)

    if ch2_exp_grey_secret:
        "你从格雷伯爵手中获得了父亲的遗物。暗百合的阴影笼罩着一切。"

    if ch2_exp_wells_bribed:
        "你与威尔斯子爵达成了商业合作。维尔纳家族的秘密，你已经知晓了一部分。"

    if ch2_exp_secret_letter:
        "某些秘密文件落入了你的手中。它们将在未来发挥关键作用。"

    if ch2_exp_night_choice == "confront":
        "你在黑夜中正面面对了危险。无论结果如何，你的勇气已经得到了证明。"
    elif ch2_exp_night_choice == "follow":
        "你在暗中发现了惊人的秘密。暗百合的触手已经伸到了领主会议的心脏。"
    elif ch2_exp_night_choice == "ignore":
        "你选择了谨慎。但有些东西，如果你不去寻找，它们就会来找你。"

    $ change_stat("wealth", 3)
    $ change_stat("reputation", 3)
    $ log_decision("第二章扩展", "领主会议闭幕")

    return

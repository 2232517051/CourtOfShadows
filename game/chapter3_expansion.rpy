## ============================================================
## 第三章扩展：暗百合深层剧情
## chapter3_expansion.rpy
## 调查序列 / 森林探险 / 草药师支线 / 教团渗透 / 终局对峙
## ============================================================

## ── 扩展剧情标记 ──
default ch3_investigation_path = ""   # "diplomatic" / "forceful" / "cunning"
default ch3_forest_explored = False
default ch3_herbalist_met = False
default ch3_herbalist_romance = False
default ch3_cult_infiltrated = False
default ch3_cult_leader_fate = ""
default ch3_ancient_ruin_found = False
default ch3_antidote_learned = False
default ch3_witness_count = 0
default stein_origin_revealed = False

## ============================================================
## 第一部分：调查序列 — Investigation Sequence (~500行)
## ============================================================

label ch3_exp_investigation:

    scene bg castle_library with dissolve

    if lily_full_member:
        "你加入暗百合之后，更清楚这个组织的水远比表面深。影能告诉你的只是一部分——暗焰的渗透、外围的招募、那些还游离在组织边缘的盟友和敌人，都需要你自己去梳理。"

        "你在书房中铺开一张大羊皮纸，把接触过的所有信息一一写下：失踪的农民、倒置的百合符号、黑斗篷的陌生人、父亲的异常行为……"

        "每一条线索都还是碎片。身在局中，反而更需要一张看全局的图。"
    elif dark_lily_joined:
        "你与影卫订下对等之盟以后，能从他们那里拿到的情报比想象中多——但也只到他们愿意给的那一层。剩下的，得自己去摸。"

        "你在书房中铺开一张大羊皮纸，把接触过的所有信息一一写下：失踪的农民、倒置的百合符号、黑斗篷的陌生人、父亲的异常行为……"

        "影卫只肯给你他们那一层的情报，剩下的得你自己拼。两边对上，全局才看得清。"
    elif dark_lily_destroyed:
        "暗百合虽然已被你铲除，但缴获的档案和残余的网络里还有太多未解之谜。是时候把线索串起来了。"

        "你在书房中铺开一张大羊皮纸，把缴获和自己收集的信息一一写下：失踪的农民、倒置的百合符号、黑斗篷的陌生人、父亲的异常行为……"

        "每一条都需要重新定位。谁是真正的盟友，谁只是被牵连的卒子——你必须把棋盘重新看清。"
    else:
        "你决定系统性地调查暗百合组织。零散的线索太多，是时候把它们串联起来了。"

        "你在书房中铺开一张大羊皮纸，将目前掌握的所有信息一一写下：失踪的农民、倒置的百合符号、黑斗篷的陌生人、父亲的异常行为……"

        "线索零零散散，全貌你还看不清。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    if dark_lily_joined:
        aldric "少主，您打算从哪里切入？"
    elif dark_lily_destroyed:
        aldric "少主，接下来从哪里入手清理残局？"
    else:
        aldric "少主，您打算如何展开调查？"

    "你放下鹅毛笔，看着地图上标注的几个关键地点。"

    hide aldric_img
    show player_char_img at right with dissolve

    player "我们有三个方向可以切入。"

    if dark_lily_joined:
        player "第一，通过外交——借影的关系网，看看周边领地里哪些贵族已经在组织里。"

        player "第二，直接行动——带兵清查那些被暗焰叛徒渗透的据点，把内鬼揪出来。"

        player "第三，深入组织——进一步卷入核心圈，让影把她还没说的真相一并告诉我。"
    elif dark_lily_destroyed:
        player "第一，通过外交渠道——联系周边领地的领主，看看还有没有暗百合的残党藏身。"

        player "第二，直接行动——带兵清扫缴获档案里标注的可疑据点。"

        player "第三，暗中调查——派人伪装，潜入残党可能的藏身地，确保没有漏网之鱼。"
    else:
        player "第一，通过外交渠道——联系周边领地的领主，看看暗百合是否也渗透了他们的地盘。"

        player "第二，直接行动——带兵搜查已知的可疑地点，用武力逼迫暗百合现身。"

        player "第三，暗中渗透——伪装身份，潜入暗百合的外围组织，从内部获取情报。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "三种方式各有利弊。外交最安全但最慢，武力最快但可能打草惊蛇，渗透最危险但收获可能最大。"

    menu:
        "外交路线「联络周边领主」":
            $ ch3_investigation_path = "diplomatic"
            $ change_stat("reputation", 5)
            $ change_stat("loyalty", 3)
            $ log_decision("第三章扩展", "选择外交调查路线")
            "求周边领主借眼线、通消息，这种人情开了口就欠下了——日后他们要你回报，你推不掉。"
            jump ch3_exp_investigate_diplomatic

        "武力路线「雷霆扫穴」":
            $ ch3_investigation_path = "forceful"
            $ change_stat("power", 5)
            $ change_courage(5)
            $ change_stat("reputation", -5)
            $ log_decision("第三章扩展", "选择武力调查路线")
            "一百人压上去，村镇这几天别想安生。要是扑了空，弟兄白跑、百姓遭扰，怨气都得算到你头上。"
            jump ch3_exp_investigate_forceful

        "渗透路线「化暗为明」" if intrigue >= 45:
            $ ch3_investigation_path = "cunning"
            $ change_stat("intrigue", 8)
            $ change_stat("reputation", -2)
            $ log_decision("第三章扩展", "选择渗透调查路线")
            jump ch3_exp_investigate_cunning

## ── 外交调查路线 ──

label ch3_exp_investigate_diplomatic:

    scene bg castle_library with dissolve

    if dark_lily_joined:
        "你决定从外交入手。你不去直接碰暗百合，而是想从周边领主那里探出暗焰在别处的渗透范围。"

        "当天你便写了三封信，寄给格雷伯爵、威尔斯子爵和施泰因伯爵夫人。信里只字不提你和组织的关系，只询问他们领地里是否也出现了「异常失踪事件」。"
    elif dark_lily_destroyed:
        "你决定以外交手段追查残党。当天便写了三封信，寄给格雷伯爵、威尔斯子爵和施泰因伯爵夫人——询问他们领地里是否也有「异常失踪事件」的尾巴。"

        "信里措辞谨慎——你不想让任何人知道你已经亲手清空了暗百合的核心。"
    else:
        "你决定以外交手段展开调查。当天便写了三封信，分别寄给格雷伯爵、威尔斯子爵和施泰因伯爵夫人。"

        "信中你小心地措辞——没有直接提及暗百合，只是询问他们的领地是否也出现了「异常失踪事件」。"

    "五天后，回信陆续到来。"

    "格雷伯爵的信最先到达。他的语气谨慎，但字里行间透露出不安——他的领地也发现了类似的符号，而且他的一位顾问最近行为反常。"

    "威尔斯子爵的回信则更加直白：「那些倒置百合花的符号？我烧了整整一面墙才清理干净。有人在挑衅我。」"

    "最让你意外的是施泰因伯爵夫人的信。她没有回答你的问题，而是写道——"

    "「年轻的领主，你问的事情，比你想象的要复杂得多。如果你真心想了解，亲自来一趟。有些话，不能写在纸上。」"

    menu:
        "前往拜访施泰因伯爵夫人":
            $ change_stat("loyalty", 5)
            $ change_stat("reputation", 3)

            scene bg forest_path with dissolve

            "你骑马前往施泰因领地。路途不算远，但每一步都伴随着某种隐隐的紧张感。"

            "伯爵夫人在她的私人花园里接见了你。她年过五十，银发如霜，但一双眼睛锐利如鹰。"

            show countess_stein_img at right with dissolve

            countess_stein "你很勇敢，敢亲自来。"

            hide countess_stein_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve

            player "我需要真相。"

            hide player_char_img
            $ hide_all_chars("countess_stein_img")
            show countess_stein_img at left with dissolve
            countess_stein "真相？好吧。暗百合不是你想象中的邪教。它和这个王国一样古老。"

            "她从花园的石凳下取出一本泛黄的册子。"

            countess_stein "两百年前，暗百合是一个守护者组织——保护平民不受贵族暴政。但时过境迁，它分裂了。一部分坚持初心，另一部分……走上了另一条路。"

            countess_stein "你的父亲属于前者。而杀害你父亲的人，属于后者。"

            "你的心猛然一紧。"

            hide countess_stein_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你知道谁杀了我父亲？"

            hide player_char_img
            $ hide_all_chars("countess_stein_img")
            show countess_stein_img at left with dissolve
            countess_stein "我知道的不多。但我知道——凶手就在你身边。在你每天都能见到的人当中。"

            "她的话让你瞬间僵住。"

            $ stein_origin_revealed = True

            hide countess_stein_img with dissolve
            hide player_char_img with dissolve

            $ change_stat("faith", 10)
            $ ch3_witness_count += 1

        "联合三位领主共同调查" if reputation >= 45:
            $ change_stat("reputation", 8)
            $ change_stat("loyalty", 3)

            $ hide_all_chars()
            "你提出了一个大胆的方案——四个领地联合组建一支秘密调查队，共享暗百合的情报。"

            "格雷伯爵和威尔斯子爵同意了。施泰因伯爵夫人也勉强点头，但她的条件是——调查结果只在四人之间共享，不报告王廷。"

            "你同意了。联合调查队很快组建起来。"

            "第一批成果在两周后传来——调查队在三个领地的交界处发现了一条地下通道网络。这些通道连接着多处暗百合的秘密据点。"

            "暗百合的规模，远超你的想象。"

            $ ch3_witness_count += 2

        "保持通信往来「不轻举妄动」":
            $ change_stat("reputation", 5)

            "你选择保持谨慎的通信联络，不急于采取行动。"

            "接下来几周，你们四位领主互通了大量情报。进展慢，但你对暗百合摸得越来越清楚。"

            "暗百合的根扎在好几片领地，不止一处地方。"

            $ ch3_witness_count += 1

    jump ch3_exp_crime_scene

## ── 武力调查路线 ──

label ch3_exp_investigate_forceful:

    scene bg forest_path with dissolve
    $ play_music("audio/music/forest_ambient.ogg", fadein=2.0)

    "你叫来了雷恩。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve

    player "准备五十名精锐士兵。我们要搜查森林里的每一个角落。"

    hide player_char_img
    show captain_img at right with dissolve

    captain "大人，森林面积广大，五十人恐怕——"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    if dark_lily_joined:
        player "那就一百人。暗焰叛徒在我们眼皮底下活动了太久——我要把他们从组织内部连根拔起。"
    elif dark_lily_destroyed:
        player "那就一百人。残党还没清完，不能给他们喘息的机会。"
    else:
        player "那就一百人。暗百合在我们眼皮底下活动了太久，是时候让他们知道谁才是这片土地的主人。"

    hide player_char_img with dissolve
    hide captain_img with dissolve

    $ hide_all_chars()
    "第二天拂晓，你带一百名全副武装的士兵进了北部森林。"

    "搜了整整三天。森林里的小路和洞穴你们都翻过，废弃木屋也没漏。"

    "第一天，你们摸到三处刚撤掉的营地。帐篷烧了，地也扫过，但还有痕迹——脚印、灰里没烧尽的布片、一只落下的铜环。"

    "铜环上刻着倒置的百合花。"

    "第二天，你们在森林深处摸到一座石建筑，灌木丛严严实实盖在上面。"

    show captain_img at right with dissolve

    captain "大人，前方发现了一个……地下入口。"

    menu:
        "直接冲入「速战速决」" if power >= 45:
            $ change_stat("power", 8)
            $ change_stat("loyalty", -2)
            $ change_courage(5)

            $ hide_all_chars()
            "你拔出佩剑：「全军突入！」"

            "士兵们鱼贯而入。地下通道曲折幽暗，但你的人训练有素，队形丝毫不乱。"

            "通道尽头是一个巨大的地下厅堂。墙壁上刻满了百合花的图案，中央有一座石制祭坛。"

            "但厅堂是空的。暗百合的人提前撤了——这么大动静的搜查，早惊动他们了。"

            "不过有些东西他们没带走：仪式用的蜡烛、几本账本，还有一面旗帜——上面的百合花是金色，不是平时那种黑色。"

            "这颜色比黑色更高一级。"

            $ change_stat("reputation", 5)
            $ ch3_witness_count += 1

        "派先遣队侦察「谨慎行事」":
            $ change_stat("power", 5)
            $ change_stat("loyalty", 5)

            "你让雷恩挑选十名最精锐的斥候先行探路。"

            "半个时辰后，斥候回来了。"

            captain "大人，地下通道很长，至少延伸了数百步。里面没有守卫，但有很多陷阱——绊绳、落石机关、还有一段注满了水的区域。"

            captain "通道尽头有一个大厅。空的。但……"

            "雷恩的声音低了下去。"

            captain "我们在大厅的墙上发现了一幅壁画。上面画的人……很像您的父亲。"

            "你心中一震。"

            $ change_stat("loyalty", 8)
            $ ch3_witness_count += 2

    hide captain_img with dissolve

    jump ch3_exp_crime_scene

## ── 渗透调查路线 ──

label ch3_exp_investigate_cunning:

    scene bg tavern with dissolve

    if dark_lily_joined:
        "你选择了最危险也可能回报最大的路线——作为组织成员，悄悄摸清外围那些被暗焰拉拢的人底细。"

        "影能告诉你的是核心圈；外围已经变质的那些，你得自己去探。"

        "你想起了那个在地窖中死去的报信刺客，以及他说的话：「花园里的人。」"

        "你决定从酒馆开始——暗焰的爪牙一定混迹在城镇的底层社会中。"
    elif dark_lily_destroyed:
        "你选择了最危险也可能回报最大的路线——追踪残党。"

        "核心虽已清空，底层那些被暗百合雇来的爪牙还在。你要确保每一个都被揪出来。"

        "你想起了那个在地窖中死去的报信刺客，以及他说的话：「花园里的人。」"

        "你决定从酒馆开始。这类人一定混迹在城镇的底层社会中。"
    else:
        "你选择了最危险、也可能回报最大的路线——渗透。"

        "第一步，你需要一个切入点。暗百合不接受陌生人——你需要一个介绍人。"

        "你想起了那个在地窖中死去的报信刺客，以及他说的话：「花园里的人。」"

        "你决定从酒馆开始。暗百合的外围人员一定混迹在城镇的底层社会中。"

    "你换上朴素的衣服，遮住佩剑上的家族纹章，独自走进了城镇最混乱的酒馆——「断头斧」。"

    "酒馆里烟雾弥漫，各色人等混杂其中。你找了个角落坐下，点了一杯最便宜的麦酒，开始观察。"

    "连续三个晚上，你都来到这里。第三天晚上，你终于注意到了一个细节——角落里那个总是独自喝酒的蒙面男人，他的杯子旁边放着一枚铜币。"

    "铜币上面刻着一朵百合花。"

    menu:
        "主动接近「套取情报」" if intrigue >= 45:
            $ change_stat("intrigue", 8)
            $ change_stat("faith", -2)  ## balance pass 修法 1: 伪装身份+套话换情报, 信仰受损

            "你端着酒杯走过去，在他对面坐下。"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve

            player "这里有人吗？"

            "蒙面人抬起头，打量了你一番。他的眼神警觉而锐利。"

            hide player_char_img
            show assassin_char_img at right with dissolve

            assassin "你是谁？"

            hide assassin_char_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "一个对百合花感兴趣的人。"

            $ hide_all_chars()
            "远处酒馆里传来一阵笑声，又迅速被夜色吞没。"

            "然后他低声说：「月落时分——」"

            "你想起了某处听到的暗号，冒险接上：「花开无声。」"

            "蒙面人的眼神变了。他重新审视了你一番，然后微微点头。"

            hide player_char_img
            $ hide_all_chars("assassin_char_img")
            show assassin_char_img at left with dissolve
            assassin "你是播种者的人？"

            "你不知道正确的回答是什么，但你赌了一把。"

            hide assassin_char_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "播种者已经不在了。他让我来接替他。"

            ## 渗透路线判定 #1 (栀子 2026-05-02 backlog: 渗透缺判定)
            $ trigger_crisis("intrigue", 6,
                "蒙面人的手在桌沿下按住了什么东西。这一刻——你的谎要圆得没有缝，眼神不能有半分闪躲。",
                "ch3exp_bluff_win", "ch3exp_bluff_lose",
                courage_cost=15)
            call crisis_encounter from _call_crisis_ch3exp_bluff

        "暗中跟踪「看他去哪里」":
            $ change_stat("intrigue", 5)
            $ change_stat("faith", -2)  ## 暗中跟踪的代价: 信仰侵蚀 (balance pass 修法 1)

            "你没有打草惊蛇，而是在蒙面人离开酒馆后悄悄跟上。"

            ## 渗透路线判定 #2
            $ trigger_crisis("intrigue", 5,
                "他在第三条巷口突然停步回头。这一刻——你得在他的目光扫过来之前，变成一个恰好路过的醉汉。",
                "ch3exp_tail_win", "ch3exp_tail_lose",
                courage_cost=10)
            call crisis_encounter from _call_crisis_ch3exp_tail

    jump ch3_exp_crime_scene

## ── 渗透判定分支 (crisis 落点) ──

label ch3exp_bluff_win:

    "蒙面人盯着你看了三息。然后从怀中取出一张纸条推向你。"

    $ hide_all_chars("assassin_char_img")
    show assassin_char_img at left with dissolve
    assassin "三天后，旧磨坊。别迟到。"

    $ hide_all_chars()
    "他站起身，走到拐角处头也没回。你低头看纸条——上面画着一朵百合花和一个地点的简图。"

    "你成功打入了暗百合的外围。"

    $ ch3_witness_count += 2

    jump ch3_exp_crime_scene

label ch3exp_bluff_lose:

    "蒙面人又低声问了一句：「种子落在哪里？」"

    "这一句你接不上。停顿只有半息——够了。"

    $ hide_all_chars()
    "他起身离开，脚步不快，杯子都没有碰响。你追出门时，巷子里只剩下雨声。"

    "三天后你派人盯住旧磨坊。那里空了——连地上的草料都被清走。酒馆这条线，断了。"

    $ change_stat("intrigue", -6)

    jump ch3_exp_crime_scene

label ch3exp_tail_win:

    "他穿过了几条弯弯曲曲的小巷，最终进入了一间废弃的仓库。你在对面的屋顶上伏了两个时辰。"

    "在这段时间里，又有三个人先后进入仓库。他们都戴着面罩，走路的姿态刻意变换，以避免被认出。"

    "最后一个进去的人身形高大，走路带着微微的跛足。这个特征你见过——在男爵的领地。"

    "暗百合和男爵之间，果然有联系。"

    "你记下了仓库的位置和每个人到达的时间。这些情报以后会派上用场。"

    $ ch3_witness_count += 1

    jump ch3_exp_crime_scene

label ch3exp_tail_lose:

    "你装醉靠墙的那一下慢了。他的目光在你身上停了一瞬，然后若无其事地继续走。"

    "再拐过两个弯，人不见了。巷子是死的，墙头的浮灰没有蹬痕——他从哪出去的，你没看见。"

    "第二天你让人把那片巷子翻了一遍。什么都没有。对方知道有人跟过他，这一片的据点只会换得更深。"

    $ change_stat("intrigue", -4)

    jump ch3_exp_crime_scene

## ── 犯罪现场调查 ──

label ch3_exp_crime_scene:

    scene bg forest_path with dissolve

    "无论你选择了哪条路线，有一件事是必须做的——回到最初失踪事件的现场。"

    "你来到了铁匠最后出现的森林边缘。"

    "经过仔细搜查，你发现了几样东西：地上的拖拽痕迹、一块沾了黑色液体的布片、以及树干上新刻的记号。"

    "黑色液体散发着苦涩的气味。你用手帕小心包好——这很可能是某种药物。"

    "拖拽痕迹指向森林深处。你沿着痕迹走了一段，来到了一块空地。"

    "空地中央有一个用石头围成的圆圈。圆圈内的泥土被翻动过，还有烧灼的痕迹。"

    "这是某种仪式的遗址。"

    menu:
        "仔细勘查仪式遗址":
            $ change_stat("reputation", 5)

            "你蹲下身，仔细检查了圆圈内的每一寸土地。"

            "在灰烬中，你找到了一块没有完全烧毁的羊皮纸碎片。上面残留着几个拉丁文单词：「purificatio per umbram」——通过暗影进行净化。"

            "这不是邪教仪式——更像是某种古老的入会仪式。暗百合在用这种方式接纳新成员。"

            "失踪的农民们，很可能不是被绑架的——他们是自愿加入的。"

            "这个发现让你对暗百合的认知发生了根本性的转变。"

        "采集黑色液体样本「带回去化验」":
            $ change_stat("reputation", 3)
            $ change_stat("wealth", -3)

            "你小心翼翼地采集了黑色液体的样本，带回城堡交给医师。"

            "医师经过一天的研究后告诉你：「这是一种由多种草药混合而成的迷药。服用后会产生强烈的幻觉和极度的顺从感。效果持续约三个时辰。」"

            "「制作这种迷药需要非常专业的草药学知识，」医师补充道，「普通人做不出来。」"

            "你想到了一个人——森林里的那位草药师。也许你该去拜访一下她。"

            $ ch3_herbalist_met = False

        "标记位置后离开「以后再来」":
            $ change_stat("power", 2)

            "你在心中记下了这个位置的坐标，然后悄悄离开。"

            "过早惊动暗百合不是明智之举。你需要更多的准备。"

    "回到城堡后，你将所有发现汇总在羊皮纸上。拼图的轮廓正在逐渐清晰。"

    "但拼图上还有太多空白。每一条线索都指向更深的迷雾。"

    jump ch3_exp_forest_expedition

## ============================================================
## 第二部分：森林探险 — Forest Expedition (~400行)
## ============================================================

label ch3_exp_forest_expedition:

    scene bg forest_path with dissolve
    $ play_music("audio/music/forest_ambient.ogg", fadein=2.0)

    "你决定深入北部森林——那片被迷雾和传说笼罩的古老林地。"

    "所有的线索都指向那里。失踪的农民、暗百合的据点、废弃的修道院……森林藏着太多秘密。"

    show captain_img at right with dissolve

    captain "大人，北部深林已经数十年无人涉足。老猎人说里面有狼群和毒蛇，还有……一些说不清的东西。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve

    player "什么说不清的东西？"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "据说是前朝留下的遗迹。有些猎人曾远远看到过石柱和废墙，但没有人敢靠近。"

    menu:
        "带上雷恩和精锐小队「安全第一」":
            $ change_stat("power", 3)

            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "挑十名最好的士兵，我们明天出发。"

            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "遵命。我亲自带队。"

            "次日清晨，你们踏入了森林的深处。"

        "只带艾琳娜「人少目标小」":
            $ change_stat("loyalty", 5)
            $ change_stat("rel_elena", 5)

            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "太多人反而引人注目。艾琳娜，你跟我来。"

            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve

            elena "领主大人……您确定吗？"

            hide elena_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你对草药和森林比任何士兵都熟悉。我需要你的眼睛。"

            "艾琳娜点了点头。"

            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "那请跟紧我。森林里的路，不是用眼睛看的。"

            hide elena_img with dissolve

        "独自前往「只有一个人才能看到真相」" if power >= 45:
            $ change_stat("power", 8)
            $ change_courage(10)

            $ hide_all_chars()
            "你拒绝了所有人的陪同，只带了一把剑、一壶水和地图，独自走进了森林。"

            "这也许是你做过的最鲁莽的决定。但你的直觉告诉你——暗百合不会伤害一个独自前来的人。"

            "他们要的不是你的命。他们要的……是你本人。"

    hide captain_img with dissolve

    ## ── 森林深处 ──

    scene bg forest_path with dissolve

    "你在森林中走了大半天。阳光被层层叠叠的树冠遮挡，脚下的落叶越来越厚。"

    "空气中弥漫着腐殖土和苔藓的气息。偶尔有鸟叫声划破寂静，但更多的时候，只有你自己的脚步声。"

    "渐渐地，你注意到了一些不自然的痕迹——树干上刻着箭头状的记号，指引着一条看不见的小路。"

    "你顺着记号走了约一个时辰，突然——"

    "眼前豁然开朗。"

    scene bg_ancient_ruins with dissolve

    "一座古老的石头遗迹出现在你面前。"

    "残破的石柱高耸入云端，上面爬满了常春藤。一座半倒塌的拱门矗立在中央，门楣上刻着已经风化得难以辨认的文字。"

    "但在所有的石柱上，都刻着同一个符号——百合花。不是倒置的，而是正立的。"

    "这是暗百合的发源地。"

    $ ch3_ancient_ruin_found = True

    "你小心翼翼地走入遗迹。脚下的石板路虽然被杂草覆盖，但仍然完整。"

    $ play_music("audio/music/ritual.ogg", fadein=2.0)
    "遗迹的中心是一座圆形的祭坛，用白色大理石砌成。祭坛中央嵌着一块黑色的石碑。"

    "石碑上刻着文字——这次你能读懂了。那是中世纪的拉丁文："

    "「吾等以百合为誓，守护弱者，对抗暴政。\n　当权力腐化时，吾等是暗夜中的利刃。」"

    "「当信仰堕落时，吾等是黎明前的烛火。\n　百合虽暗，心向光明。」"

    "你站在石碑前，感到一种奇异的庄严感。"

    if stein_origin_revealed:
        "暗百合的初心——守护弱者，对抗暴政。和施泰因伯爵夫人说的一样。"
    else:
        "暗百合的初心——守护弱者，对抗暴政。石碑上的字句让那些在你脑中盘旋多时的碎片第一次有了形状。"

    "那么，是什么让它走到了今天这一步？"

    menu:
        "仔细搜查遗迹「寻找更多线索」" if reputation >= 45:
            $ change_stat("reputation", 8)

            "你在遗迹中搜查了两个时辰。在一座半倒塌的建筑中，你发现了一间保存得还算完好的密室。"

            "密室的墙壁上画着暗百合的历史——从创立、壮大、分裂，到最终的衰落。"

            "在最后一幅画中，你看到了两个对立的人影——一个手持百合花，一个手持匕首。"

            "画旁的文字写道：「当守护者成为猎人，百合便不再纯洁。」"

            "在密室的地板下，你还发现了一个暗格。里面有一枚铜章——上面刻着「第七任守望者」几个字。"

            "第七任守望者……这是暗百合内部的某种职位。你把铜章收入怀中。"

            $ change_stat("intrigue", 5)

        "在祭坛前冥想「感受这个地方的力量」" if faith >= 45:
            $ change_stat("faith", 8)
            $ change_courage(5)

            "你在祭坛前坐下，闭上眼睛。"

            "风穿过残破的石柱，发出低沉的呜咽声。树叶沙沙作响。"

            "你不知道自己坐了多久。当你睁开眼睛时，夕阳已经将整个遗迹染成了金红色。"

            "暗百合既不是善，也不是恶。它是为了对抗黑暗而被造出来的，但同样的力量也能伤人。"
            "你没有动手去翻那片废墟。藏在断墙暗格里的东西，今天你是看不成了——你选了静坐，就放下了搜寻。"


        "标记遗迹位置后迅速撤离「这里不安全」":
            $ change_stat("power", 3)
            $ change_stat("faith", -6)

            "这是父亲守过的地方，你却连一炷香的工夫都没留。脚步迈出拱门时，心里有什么东西轻轻沉了一下。"

            "直觉告诉你不宜久留。你在地图上标记了遗迹的位置，然后沿原路返回。"

            "果然，在你离开后不到半个时辰，你听到了身后传来的脚步声。"

            "有人在跟踪你。但当你回头时，只看到了树叶在风中摇曳。"

            "你加快了脚步。暗百合知道你来过了。"

    $ ch3_forest_explored = True

    "太阳落山前，你回到了安全的地方。"

    "今天的发现彻底改变了你对暗百合的认知。它不仅仅是一个秘密组织——它是一段被遗忘的历史。"

    "而你的父亲，是这段历史中的重要角色。"

    jump ch3_exp_herbalist

## ============================================================
## 第三部分：草药师支线 — Herbalist Quest (~400行)
## ============================================================

label ch3_exp_herbalist:

    scene bg forest_path with dissolve

    "你在森林边缘的一条岔路上看到了一个路标——一块木板上画着草药和药钵的图案。箭头指向一条几乎被灌木淹没的小径。"

    "这是森林草药师的住处。传说中，她是方圆百里最懂草药的人。"

    "你沿着小径走了约一刻钟，来到了一座被花圃和药圃环绕的小木屋。"

    "屋前晾着一排排干燥的草药，散发着浓烈而复杂的香气。一缕青烟从烟囱中升起。"

    "你敲了敲门。"

    "门开了。一个约三十岁的女子出现在门口——她有一头如瀑的黑发，穿着朴素的亚麻长裙，手上沾着绿色的汁液。"

    "她的眼睛是你见过的最奇特的颜色——琥珀色，像是凝固了的蜂蜜。"

    show herbalist_vera_img at right with dissolve

    herbalist_vera "您是……领主大人？"

    "你有些惊讶。这不是艾琳娜——但她的声音和艾琳娜有几分相似。"

    hide herbalist_vera_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve

    player "你认识我？"

    "她微微一笑。"

    hide player_char_img
    $ hide_all_chars("herbalist_vera_img")
    show herbalist_vera_img at left with dissolve
    herbalist_vera "森林里没有秘密。何况，您的佩剑上有家族纹章。请进吧——我煮了新鲜的薄荷茶。"

    "你走进小屋。屋内的每一面墙上都挂着药草，架子上摆满了装着各色粉末和液体的瓶瓶罐罐。空气中弥漫着草药特有的清苦芬芳。"

    $ ch3_herbalist_met = True

    herbalist_vera "我叫薇拉。草药师。或者如村民们称呼的——女巫。"

    "她自嘲地笑了笑。"

    hide herbalist_vera_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我不信巫术。但我需要你的知识。"

    "你从怀中取出那块沾了黑色液体的布片。"

    player "你能告诉我这是什么吗？"

    "薇拉接过布片，嗅了嗅，又用手指蘸了一点黑色液体尝了尝。你几乎要出声阻止，但她已经吐了出来。"

    hide player_char_img
    $ hide_all_chars("herbalist_vera_img")
    show herbalist_vera_img at left with dissolve
    herbalist_vera "曼陀罗、乌头、夜影草，以及……一种我很少见到的东西。暗百合精华。"

    hide herbalist_vera_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你知道暗百合？"

    hide player_char_img
    $ hide_all_chars("herbalist_vera_img")
    show herbalist_vera_img at left with dissolve
    herbalist_vera "我说的，是这花。"

    "她走到架子前，取下一个装着紫黑色花瓣的玻璃瓶。"

    herbalist_vera "暗百合——学名 Lilium Tenebris。一种只在深林中生长的稀有百合花。它的花粉有极强的致幻效果，提炼后可以制成……"

    hide herbalist_vera_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "迷药。"

    hide player_char_img
    $ hide_all_chars("herbalist_vera_img")
    show herbalist_vera_img at left with dissolve
    herbalist_vera "比迷药更可怕。高浓度的暗百合精华会完全摧毁一个人的意志。服用者在清醒后，会无条件服从给药者的命令。"

    "你的心沉了下去。这解释了为什么失踪的农民们——如果他们还活着——会如此驯服地跟随暗百合。"

    menu:
        "请薇拉制作解药":
            $ change_stat("wealth", 5)
            $ change_stat("wealth", -5)
            $ ch3_antidote_learned = True

            hide herbalist_vera_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "如果暗百合精华有这种效果，那一定有解药。"

            hide player_char_img
            $ hide_all_chars("herbalist_vera_img")
            show herbalist_vera_img at left with dissolve
            herbalist_vera "有。但制作很复杂，需要几种稀有材料。"

            "她列了一张清单——白松露、雪莲花露、银鱼肝油，以及一小块月光石。"

            herbalist_vera "给我三天时间和这些材料。我可以制作出足以解除十人药效的解药。"

            hide herbalist_vera_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你的报酬呢？"

            hide player_char_img
            $ hide_all_chars("herbalist_vera_img")
            show herbalist_vera_img at left with dissolve
            herbalist_vera "不要钱。但有一个条件——如果您找到了活着的失踪者，让我见见他们。我需要研究暗百合精华对人体的长期影响。"

            $ hide_all_chars()
            "你同意了。"

            "三天后，薇拉如约交付了一小瓶碧绿色的解药。她还教了你一个简单的急救方法——如果有人被暗百合精华迷晕，用冷水浇头加上薰衣草精油可以暂时恢复神志。"

        "请教更多关于毒药的知识" if intrigue >= 45:
            $ change_stat("intrigue", 8)
            $ change_stat("faith", -3)

            hide herbalist_vera_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我想更系统地了解毒药学。不仅是暗百合——所有常见的毒药和解药。"

            "薇拉看了你一眼，琥珀色的眼睛里闪过一丝好奇。"

            hide player_char_img
            $ hide_all_chars("herbalist_vera_img")
            show herbalist_vera_img at left with dissolve
            herbalist_vera "学毒药学的领主……有意思。"

            "在接下来的一个下午，薇拉给你上了一堂毒药学速成课。你学会了辨认十几种常见毒药的气味和症状，以及对应的急救方法。"

            herbalist_vera "记住最重要的一条——大多数毒药都有气味。如果你的酒闻起来有杏仁味，不要喝。"

            "这些知识你牢牢记住了。在这样的宫廷里，多懂一点毒药，多一分活命的机会。"

        "询问她是否知道暗百合组织的事":
            $ change_stat("loyalty", 5)
            $ change_stat("rel_elena", 3)

            hide herbalist_vera_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你说你只知道暗百合这种植物，不知道暗百合组织。但我不完全相信你。"

            "薇拉停下了手中的动作，安静地看着你。"

            hide player_char_img
            $ hide_all_chars("herbalist_vera_img")
            show herbalist_vera_img at left with dissolve
            herbalist_vera "您很敏锐。"

            herbalist_vera "好吧。我确实知道一些。我的母亲曾经是暗百合的成员——她是一名治疗师。组织内部称她为「花匠」。"

            herbalist_vera "但那是很久以前的事了。母亲在暗百合分裂后就离开了。她说……组织变质了。新的领导者不再保护弱者，而是利用弱者。"

            herbalist_vera "母亲在我十五岁时去世。临终前她告诉我——如果有一天艾登堡的领主来找我，告诉他：「你父亲是好人。」"

            "你的喉咙一阵哽塞。"

            hide herbalist_vera_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你母亲认识我父亲？"

            hide player_char_img
            $ hide_all_chars("herbalist_vera_img")
            show herbalist_vera_img at left with dissolve
            herbalist_vera "我想是的。不过她从不愿意多说。她只是反复叮嘱我——把草药学好，总有一天会用得上。"

            $ hide_all_chars()
            "也许那一天，就是今天。"

    ## ── 草药师浪漫支线（可选） ──

    "临走时，薇拉送你到门口。夕阳透过树叶洒下斑驳的光影，落在她琥珀色的眼睛上。"

    "她递给你一小束干燥的薰衣草。"

    hide player_char_img
    show herbalist_vera_img at right with dissolve

    herbalist_vera "放在枕头下面。可以帮助安眠。"

    "你们的手指在交接薰衣草时短暂地碰到了一起。"

    menu:
        "「谢谢。我还会再来的。」":
            $ change_stat("loyalty", 2)
            $ ch3_herbalist_romance = True

            "薇拉的眼睛弯了弯。"

            herbalist_vera "我知道。"

            "她转身走回屋里，但在门口停了一下。"

            herbalist_vera "下次来，我教您泡一种很特别的茶。只有我和……故人知道配方。"

            $ hide_all_chars()
            "你的心跳快了半拍。不知道是因为她的话，还是因为「故人」这个词暗含的意味。"

            "你带着薰衣草和满腹的新知识回到了城堡。"

        "「多谢。保重。」":
            $ change_stat("faith", 2)

            "你接过薰衣草，礼貌地告别。"

            "回城的路上，你脑子里只有暗百合精华和解药的事。没空想什么浪漫。"

    hide herbalist_vera_img with dissolve
    hide player_char_img with dissolve

    if ch3_dark_lily_visited or dark_lily_joined:
        jump ch3_exp_skip_to_end
    jump ch3_exp_cult_infiltration

## ============================================================
## 第四部分：教团渗透 — Cult Infiltration (~400行)
## 仅在主线未访问暗百合时执行，避免重复
## ============================================================

label ch3_exp_cult_infiltration:

    ## 二次守卫：如果玩家已加入暗百合，跳过渗透段落
    if dark_lily_joined:
        jump ch3_exp_skip_to_end

    scene bg forest_path with dissolve
    $ play_music("audio/music/conspiracy.ogg", fadein=2.0)

    "根据之前获得的情报，你确定了暗百合下一次集会的时间和地点——月圆之夜，旧磨坊。"

    "这是一个千载难逢的机会。如果你能潜入集会，就能亲眼看到暗百合的真面目。"

    "但风险同样巨大。一旦身份暴露，你可能永远走不出那座磨坊。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "少主，我必须再次劝阻您。这太危险了。"

    hide aldric_img
    show player_char_img at right with dissolve

    player "我知道。但我别无选择。信件和传闻永远无法告诉我真相。我必须亲眼看到。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "那至少……让我教您几个暗百合内部的暗号和手势。这些是……你父亲曾经告诉我的。"

    $ hide_all_chars()
    "老管家的话让你心中一紧。他果然知道更多。"

    "在接下来的一个时辰里，奥尔德里克教了你六个暗号、三种手势，以及一段用于进入集会的口令。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "记住——进去后不要说话，不要摘掉面罩，不要主动接近任何人。观察，记忆，然后安全撤离。"

    hide aldric_img with dissolve
    hide player_char_img with dissolve

    ## ── 月圆之夜 ──

    scene bg_crypt with dissolve

    "月圆之夜。你穿上黑色斗篷，戴上面罩，独自来到了旧磨坊。"

    "磨坊看上去已经废弃多年，但当你走到门前时，一个声音从阴影中传来。"

    show assassin_char_img at right with dissolve

    assassin "暗号。"

    hide assassin_char_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve

    player "月落时分，花开无声。"

    hide assassin_char_img with dissolve
    hide player_char_img with dissolve

    $ hide_all_chars()
    "门开了。你走入黑暗之中。"

    "磨坊的地下有一条长长的通道。通道尽头是一个用蜡烛照亮的地下大厅。"

    "大厅里已经聚集了约三十人，全部穿着黑色斗篷，戴着面罩。他们围坐成一个半圆，面朝正前方的一座石台。"

    "你悄悄混入人群，找到了一个靠近边缘的位置坐下。"

    "心跳声震耳欲聋，但你努力保持平静。"

    "等了约半个时辰，一个人出现在石台上。"

    "他的斗篷是深紫色的——与其他人的黑色不同。他的面罩上雕刻着一朵带刺的铁百合花。"

    $ hide_all_chars("lily_master_img")
    show lily_master_img at left with dissolve

    lily_master "同胞们。"

    "他的声音低沉而富有感染力，在地下大厅中回荡。这不是影主的声音——这是另一个人。"

    lily_master "花园即将迎来新的季节。旧的枝叶必须修剪，新的种子必须播种。"

    lily_master "两百年来，我们在暗中守护这片土地。但守护的方式……需要改变。"

    "他顿了顿，环视众人。"

    lily_master "温和的手段已经不够了。那些贪婪的领主和腐败的教会，不会因为我们的善意而改变。"

    lily_master "我们需要更……直接的手段。"

    $ hide_all_chars()
    "你感到背脊发凉。这不是暗百合的正式集会——这是铁刺派的秘密会议，一个从暗百合分裂出来的激进派系。"

    "接下来的内容更加令人震惊——铁刺派首领谈到了一个计划：在下个月的领主会议上制造混乱，趁机暗杀几位「阻碍正义」的贵族。"

    "而你的名字，赫然在列。"

    hide lily_master_img with dissolve

    menu:
        "继续潜伏「获取更多情报」" if intrigue >= 55:
            $ change_stat("intrigue", 10)
            $ change_stat("reputation", -3)
            $ change_courage(8)
            $ log_decision("第三章扩展", "在暗百合集会中继续潜伏")

            "你强压下心中的惊恐，继续坐在原处。"

            "在接下来的集会中，你记住了每一个细节——计划的时间表、参与者的代号、行动的路线。"

            "你还注意到，并非所有人都同意铁刺派首领的计划。坐在前排的几个人明显流露出不安。铁刺派内部也并非铁板一块。"

            "集会结束时，你随人群缓缓退出。就在你即将走出通道的那一刻——"

            "一只手搭上了你的肩膀。"

            show assassin_char_img at right with dissolve

            assassin "你。"

            "你的血液几乎凝固。"

            assassin "你的斗篷绑带松了。"

            "他帮你系好了绑带，转身挤进了人群，几步就和黑袍的人影混在了一起。"

            hide assassin_char_img with dissolve

            "你差点当场瘫软。"

            $ ch3_cult_infiltrated = True

        "趁乱留下记号「标记几个关键人物」" if intrigue >= 45:
            $ change_stat("intrigue", 8)
            $ change_stat("faith", -2)  ## balance pass 修法 1: 用药物在他人身上做暗号, 欺骗换情报

            $ hide_all_chars()
            "你悄悄从口袋里取出事先准备的荧光粉末——一种薇拉给你的特殊草药粉，在月光下会发出微弱的绿光。"

            "在人们起身移动时，你装作不经意地将粉末撒在了几个关键人物的斗篷上。"

            "铁刺派首领、他左右的两个副手、以及那个你怀疑是内奸的跛足男人。"

            "集会结束后的深夜，你让雷恩带人在磨坊附近暗中监视。四个被标记的人在月光下留下了微弱的绿色轨迹。"

            "你不需要知道他们的脸——只需要知道他们回去的方向。"

            $ ch3_cult_infiltrated = True

        "中途撤离「风险太大」":
            $ change_stat("intrigue", 5)
            $ change_courage(-3)
            $ log_decision("第三章扩展", "从暗百合集会中提前撤离")

            "你的直觉告诉你不能再待下去了。你趁人群骚动的间隙，悄悄从侧通道溜了出去。"

            "虽然没有获得全部情报，但你已经知道了最关键的事——暗百合计划在领主会议上动手，而且你是目标之一。"

            "这足够让你做出准备了。"

    "你回到城堡时，东方的天空已经泛白。"

    "你没有去睡觉，而是直接走进书房，将今夜的所见所闻一字不落地记录下来。"

    "暗百合铁刺派的真面目——已经完全暴露在你面前。这个从暗百合分裂出的激进派系，比本体更加危险。"

    "问题是：你打算怎么做？"

    jump ch3_exp_confrontation

## ============================================================
## 第五部分：终局对峙 — Confrontation (~300行)
## ============================================================

label ch3_exp_confrontation:

    scene bg castle_library with dissolve

    "你召集了最信任的人——雷恩、奥尔德里克，以及（如果你去过草药师那里的话）薇拉。"

    "你把掌握的所有情报铺在桌上：暗百合的据点地图、集会的记录、毒药的分析报告、父亲的笔记。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve

    player "暗百合的铁刺派计划在下次领主会议上对多位贵族下手。我们必须在那之前采取行动。"

    hide player_char_img with dissolve
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "您打算怎么做？"

    hide aldric_img
    show captain_img at right with dissolve

    captain "如果您一声令下，我可以在三天内带兵突袭旧磨坊。把他们一网打尽。"

    hide captain_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "武力不一定是最好的选择。铁刺派的根基深入多个领地，斩草不除根，春风吹又生。"

    "你看着桌上的情报，陷入了沉思。"

    menu:
        "军事打击「正面摧毁暗百合」":
            $ change_stat("power", 10)
            $ change_stat("loyalty", -3)
            $ change_courage(8)
            $ log_decision("第三章扩展", "以军事手段正面摧毁暗百合")

            hide captain_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve

            player "雷恩，准备行动。铁刺派必须连根拔除。"

            hide player_char_img
            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "是！"

            hide aldric_img with dissolve
            hide captain_img with dissolve
            hide player_char_img with dissolve

            scene bg forest_path with dissolve

            "三天后的黎明，你率领一百五十名精锐士兵突袭了铁刺派的三处据点——旧磨坊、森林中的地下大厅、以及城镇里的秘密仓库。"

            "行动迅速而果断。铁刺派的成员在睡梦中被惊醒，大多数人来不及反抗就被制服。"
            "行动干净利落。但消息传开后，几位中立的小领主对你避而不见——他们怕的不是铁刺派，是一个说动手就动手、连审都不审的邻居。"

            "但铁刺派首领不在旧磨坊里。"

            "你在地下大厅的深处找到了他——紫色斗篷，铁百合面罩。他独自站在祭坛前，背对着你。"

            show lily_master_img at right with dissolve

            lily_master "你来了。"

            "他转过身。你看不到他的脸，但从他的声音中听不出恐惧。"

            lily_master "你的父亲，用了二十年也没能阻止我，你三个月就做到了。该说你勇敢，还是鲁莽？"

            hide lily_master_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve

            player "把面罩摘下来。"

            $ hide_all_chars()
            "然后，他慢慢摘下了铁百合的面罩。"

            "你看到了那张脸，心猛然一沉。"

            "那是一张你不认识的脸——疤痕累累，冷酷而苍老。但他的眼睛……和你的眼睛有着某种相似之处。"

            hide player_char_img
            $ hide_all_chars("lily_master_img")
            show lily_master_img at left with dissolve
            lily_master "我叫艾德蒙。你父亲的兄弟。你的……叔叔。铁刺派——是我从暗百合中分裂出来的。影主的路线太软弱了。"

            "你脑子一片空白。"

            $ change_stat("power", 10)
            $ change_stat("reputation", 3)
            $ ch3_cult_leader_fate = "captured"

        "政治手段「向王廷举报」" if reputation >= 55:
            $ change_stat("reputation", 10)
            $ change_stat("loyalty", 5)
            $ log_decision("第三章扩展", "通过政治手段揭发暗百合")

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve

            player "我们不能独自行动。这件事涉及多个领地，需要王廷的介入。"

            hide aldric_img with dissolve
            hide captain_img with dissolve
            hide player_char_img with dissolve

            scene bg castle_library with dissolve

            "你写了一封详尽的密报，连同所有证据一起，派最可靠的信使送往王都。"

            "两周后，王廷的回复到了——王后派出了一支皇家调查团，由一位资深的法官率领。"

            "调查团的到来让铁刺派陷入了前所未有的恐慌。他们的据点被逐一搜查，成员被一个个揪出。"
            "皇家调查团带走了所有缴获的档案，也带走了对铁刺派的处置权。你守住了规矩，却把这股力量拱手让给了王都——往后它姓王，不姓你。"

            "铁刺派首领试图逃跑，但在边境被皇家骑士截获。"

            "他被押回你面前时，面罩已经被摘下。"

            "你看到了一张陌生而苍老的脸。但他的眼睛……让你感到一阵不安的熟悉。"

            $ hide_all_chars("lily_master_img")
            show lily_master_img at left with dissolve

            lily_master "你赢了，侄子。"

            "侄子？"

            lily_master "你父亲从来没告诉过你吧？他有一个被家族除名的兄弟。我从暗百合中拉出了铁刺派——因为影主的手段太温吞了。"

            "这个真相比任何阴谋都要残酷。"

            $ change_stat("loyalty", 8)
            $ ch3_cult_leader_fate = "arrested"

        "谈判策略「分化瓦解暗百合」" if intrigue >= 58:
            $ change_stat("intrigue", 12)
            ## 选择深度 pass: 分化瓦解=操弄手段, 走漏即损名, 不该+声望
            $ change_stat("reputation", -5)
            $ log_decision("第三章扩展", "尝试分化瓦解暗百合")

            hide lily_master_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve

            player "铁刺派内部本就有分歧。我要利用这一点。"

            hide aldric_img with dissolve
            hide captain_img with dissolve
            hide player_char_img with dissolve

            scene bg tavern with dissolve

            "你通过在集会上观察到的线索，秘密联系上了铁刺派中的温和派成员——那些对艾德蒙的极端路线心存不满的人。"

            "你的提议很简单：帮助他们推翻铁刺派首领，作为交换，他们回归暗百合正统，与你的领地达成互不侵犯的协议。"

            "温和派犹豫了很久。但当你向他们展示了首领的暗杀计划——包括对几位温和派成员的清洗名单——之后，他们同意了。"

            scene bg_crypt with dissolve

            "在下一次集会上，温和派突然发难。他们控制了大厅的出入口，将铁刺派首领和他的亲信团团包围。"

            "你走入大厅，摘下了自己的面罩。"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve

            player "游戏结束了。"

            $ hide_all_chars()
            "铁刺派首领看着你，慢慢摘下了自己的铁百合面罩。"

            "他的脸你不认识，但他的下一句话击碎了你所有的心理防线。"

            hide player_char_img
            show lily_master_img at right with dissolve

            lily_master "你和你父亲一样聪明。不愧是我的侄子。"

            $ hide_all_chars()
            "叔叔。铁刺派的首领是你的叔叔。"

            "你感到世界在脚下崩塌。"

            $ change_stat("intrigue", 8)
            $ ch3_cult_leader_fate = "negotiated"

        "暗中接管「取代首领的位置」" if intrigue >= 60:
            $ change_stat("intrigue", 10)  ## 厚度: 原+15过厚, 政变非无代价
            $ change_stat("reputation", -3)  ## balance pass 修法 1: 冒名顶替阴谋, 一旦走漏名声崩
            $ change_stat("loyalty", -6)  ## 厚度: 你靠把柄而非人心驾驭一群旧首领的人, 连奥尔德里克都被你的手段惊到
            $ change_rel("rel_aldric", -10)  ## 接管=做了你父亲毕生阻止艾德蒙做的事, 老臣奥尔德里克心生芥蒂
            $ change_courage(10)
            $ log_decision("第三章扩展", "试图暗中接管暗百合")

            hide lily_master_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve

            player "摧毁暗百合会留下权力真空。但如果我能控制它……"

            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "少主！您不是认真的吧？"

            hide aldric_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "铁刺派有数百名成员，渗透到社会的每一个角落。与其消灭它，不如驾驭它。"

            hide aldric_img with dissolve
            hide captain_img with dissolve
            hide player_char_img with dissolve

            scene bg_crypt with dissolve

            "你精心策划了一场政变。利用铁刺派内部的矛盾，你在关键时刻向温和派提供了首领暗杀计划的铁证。"

            "温和派在你的暗中操纵下发起了兵变。铁刺派首领被自己的人拿下。"

            "但与其他方案不同的是——你没有现身。你让温和派以为这是他们自己的行动。"

            "然后，你通过一系列精心安排的中间人，逐步将铁刺派残余势力收编为己用。"

            "三个月后，铁刺派的实际控制权，不知不觉间落入了你的手中。"

            "但你收编的这些人，三个月前还效忠着此刻关在你地牢里的那个人。他们听你的令，是因为你捏着他们的把柄，不是因为他们服你。"

            "从今往后这群人就在你手下做事。你得时时提防他们当中有人反咬一口。"

            "没有人知道艾登堡的年轻领主已经成了铁刺派的幕后操控者。"
            "奥尔德里克没再多说什么，但接下来几天他对你公事公办，不像从前那样事事先替你想一步。他跟了你父亲一辈子——而你父亲一辈子都在阻止他弟弟做的，正是你刚做的事。"

            "当你终于与前任铁刺派首领面对面时，他已经被关在了你城堡的地牢里。"

            show lily_master_img at right with dissolve
            hide lily_master_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve

            hide player_char_img
            $ hide_all_chars("lily_master_img")
            show lily_master_img at left with dissolve
            lily_master "呵……你比你父亲更可怕。他只是暗百合的成员。你，却要成为铁刺派的主人。"

            lily_master "但你知道我是谁吗？"

            hide lily_master_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "告诉我。"

            hide player_char_img
            $ hide_all_chars("lily_master_img")
            show lily_master_img at left with dissolve
            lily_master "我是艾德蒙。你父亲的弟弟。我从暗百合中拉出了铁刺派——因为影主太优柔寡断。你们一家人……都与百合花脱不了干系。"

            $ change_stat("intrigue", 5)
            $ dark_lily_joined = True
            $ ch3_cult_leader_fate = "replaced"

    ## ── 真相揭晓 ──

    scene bg castle_library with dissolve

    "不管你以何种方式处理了铁刺派的危机，一个核心的真相已经浮出水面——"

    "你的父亲有一个被家族除名的弟弟。"

    "这个弟弟因为理念的分歧而被流放，最终从暗百合中分裂出铁刺派，成为了这个激进派系的领袖。他与暗百合正统领袖影主决裂，认为她的手段过于温和。"

    "而你的父亲，一生都在暗中试图阻止自己的弟弟走向极端。"

    "「他不是为你死的，」你在心中想，「他是为了守护他心中的正义而死的。」"

    "你站在窗前，看着远方的森林。铁刺派的谜团已经揭开了大半。"

    "但铁刺派倒下后留下的真空，迟早要有人来填——"

    "你将如何面对你的叔叔？"
    "你将如何处置铁刺派的残余力量？"
    if father_poisoned_known:
        "而那个始终悬而未决的谜题——到底是谁在你父亲的酒中下了毒？"
    else:
        "而那个始终悬而未决的谜题——父亲的死因，到底是什么？"

    "答案就在那双与你相似的眼睛之后。"

    "但今天，你累了。"

    "你放下鹅毛笔，走向卧室。枕头下面，薰衣草的清香在安静地弥漫。"

    "明天，又是新的一天。"

    $ true_killer_known = True

    return

## ============================================================
## 跳过标签：主线已访问暗百合时，跳过重复的教团渗透和对峙
## ============================================================

label ch3_exp_skip_to_end:

    "你回顾了这几天的调查成果。森林中的发现、草药师的情报——每一条线索都与之前在暗百合总部了解到的信息相互印证。"

    "拼图越来越完整。但距离真相，还差最后几步。"

    return

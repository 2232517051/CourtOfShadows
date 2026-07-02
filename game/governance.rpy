## ============================================================
## 治理系统 — governance.rpy
## 王国治理/民生系统：税收改革、饥荒应对、建设工程、瘟疫、节日、商会
## ============================================================

################################################################################
## 1. 角色定义
################################################################################

define tax_collector = Character("税务官菲利普", color="#8b8682")
define farmer_rep = Character("农民代表米勒", color="#8b7355")
define merchant_guild = Character("商会会长克劳斯", color="#daa520")
define healer = Character("医师玛格丽特", color="#98fb98")

################################################################################
## 2. 治理变量
################################################################################

default governance_prosperity = 50
default governance_health = 50
default governance_education = 0
default governance_infrastructure = 50
default governance_tax_policy = "normal"
default governance_events_seen = []
default built_school = False
default built_clinic = False
default built_granary = False
default built_watchtower = False
default famine_prevented = False
default gov_merchant_outcome = ""  ## "monopoly"/"regulated"/"reject" — 克劳斯商会谈判结果, interlude/ch5 回响用

################################################################################
## 3. 治理辅助函数
################################################################################

init python:
    def change_prosperity(amount):
        store.governance_prosperity = max(0, min(100, store.governance_prosperity + amount))

    def change_health(amount):
        store.governance_health = max(0, min(100, store.governance_health + amount))

    def change_education(amount):
        store.governance_education = max(0, min(100, store.governance_education + amount))

    def change_infrastructure(amount):
        store.governance_infrastructure = max(0, min(100, store.governance_infrastructure + amount))

    def get_prosperity_desc():
        p = store.governance_prosperity
        if p >= 80:
            return "繁荣昌盛"
        elif p >= 60:
            return "安居乐业"
        elif p >= 40:
            return "勉强维持"
        elif p >= 20:
            return "民生凋敝"
        else:
            return "哀鸿遍野"

    def get_health_desc():
        h = store.governance_health
        if h >= 80:
            return "强健"
        elif h >= 60:
            return "良好"
        elif h >= 40:
            return "一般"
        elif h >= 20:
            return "虚弱"
        else:
            return "岌岌可危"

    def get_governance_bar(value, max_val=100):
        filled = int(value / max_val * 20)
        empty = 20 - filled
        return "█" * filled + "░" * empty + " " + str(value) + "/" + str(max_val)

################################################################################
## 4. Part 1: 税务改革 (gov_tax_reform)
################################################################################

label gov_tax_reform:
    if "tax_reform" in governance_events_seen:
        return

    $ _ch1_tax = getattr(store, "ch1_exp_tax_decision", None)
    if _ch1_tax == "restructure":
        jump gov_tax_restructure_followup
    elif _ch1_tax == "raise":
        jump gov_tax_raise_followup
    elif _ch1_tax == "lower":
        jump gov_tax_lower_intro

    ## D 分支（None / "" / 老存档）：fall through 到原流程
    scene bg great_hall with dissolve
    play music "audio/music/tension.ogg" fadeout 1.0 fadein 1.0 if_changed

    "一场关于税收的御前会议在大厅中召开。"
    "艾登堡的财政状况——这个枯燥却关乎存亡的话题，终于被摆上了议事桌。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "领主大人，我们必须讨论一个紧迫的问题。"
    aldric "现行的税制已经维持了三十年。在您父亲的时代，它或许还算公平……"
    aldric "但如今，它已经成为一颗随时可能引爆的炸弹。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "具体是什么情况？"

    hide aldric_img
    hide player_char_img
    show elena_img at right with dissolve

    elena "我在市场上听到了越来越多的怨言。农民们说，他们辛苦一年，收成的四成都要上缴。"
    elena "而某些贵族的庄园，缴纳的税赋甚至不如一个普通铁匠。"

    hide elena_img with dissolve

    $ hide_all_chars()
    "一名身着灰色外套的中年男人走入大厅，手中抱着厚厚的账册。"
    "他的手指上沾着墨迹，目光锐利而疲惫——这是一个与数字打了半辈子交道的人。"

    $ hide_all_chars("tax_collector_img")
    show tax_collector_img at left with dissolve
    tax_collector "领主大人，在下菲利普，负责艾登堡的税务登记与征收。"
    tax_collector "请容我直言——我们的税制已经到了不改不行的地步。"

    hide tax_collector_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "说下去。"

    hide player_char_img
    $ hide_all_chars("tax_collector_img")
    show tax_collector_img at left with dissolve
    tax_collector "目前的问题有三。"
    tax_collector "其一，税率不均。农民承担的实际税率是贵族的三到五倍。"
    tax_collector "其二，逃税严重。某些领地利用古老的豁免特权，几乎不缴任何税赋。"
    tax_collector "其三，征收成本高昂。我们需要大量人手去各村镇逐户征收，效率极低。"

    "菲利普翻开账册，指着一行行数字。"

    tax_collector "以去年为例——农民贡献了总税收的七成，贵族仅占一成五，商人占一成五。"
    tax_collector "但若论实际财富占比，贵族拥有全领地近半数的土地和产出。"

    "这些数字比任何控诉都更有说服力。在场的几个贵族不自在地挪了挪身子。"

    hide tax_collector_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "问题很清楚。但改革的方向，需要您来决定。"
    aldric "每一种方案都有支持者和反对者。这不仅是经济问题，更是政治问题。"

    "一个衣衫朴素的中年农夫被带了进来。他紧张地搓着手，向你行礼。"

    hide aldric_img
    $ hide_all_chars("farmer_rep_img")
    show farmer_rep_img at left with dissolve
    farmer_rep "领……领主大人，小人米勒，代表河谷一带的农户。"
    farmer_rep "恕小人斗胆直言——我们实在活不下去了。"
    farmer_rep "去年歉收，交完税后，余粮还不够撑到开春。"
    farmer_rep "好几户人家的孩子都饿出了病……"

    "米勒的声音越来越小，最后低下了头。"

    hide farmer_rep_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你的话我听到了，米勒。你不必害怕，今天就是要解决这个问题。"

    hide player_char_img
    $ hide_all_chars("farmer_rep_img")
    show farmer_rep_img at left with dissolve
    farmer_rep "谢……谢领主大人。"

    hide aldric_img with dissolve

    "菲利普清了清嗓子，展开三份不同的方案。"

    hide farmer_rep_img
    $ hide_all_chars("tax_collector_img")
    show tax_collector_img at left with dissolve
    tax_collector "领主大人，我拟定了三套改革方案，请您定夺。"

    tax_collector "方案一：累进税制。"
    tax_collector "依据土地和财产的多寡，分级征税。拥有越多，税率越高。"
    tax_collector "农民的税率将大幅降低，贵族的负担会显著增加。"
    tax_collector "预计短期内税收会略有减少，但长远来看，民心稳定，经济会更健康。"

    tax_collector "方案二：统一税制。"
    tax_collector "所有人一视同仁，缴纳相同比例的税赋。"
    tax_collector "看似公平，但对穷人而言，即便比例相同，负担依然沉重。"
    tax_collector "不过，这种方案的阻力最小——毕竟谁也不能说它不公正。"

    tax_collector "方案三：商贸税制。"
    tax_collector "将税收重心从土地转向贸易。对过境货物和商业交易征收额外关税。"
    tax_collector "农民和贵族的负担都会减轻，但商人……恐怕不会高兴。"

label gov_tax_reform_choice:
    "三份方案摆在面前，每一份都意味着不同的未来。"

    menu:
        "这是关乎艾登堡未来的抉择。"

        "推行累进税制——让富者多担，贫者得息":
            $ governance_tax_policy = "progressive"
            jump gov_tax_progressive

        "实行统一税制——人人平等，一视同仁":
            $ governance_tax_policy = "flat"
            jump gov_tax_flat

        "改征商贸税——让贸易的利润为领地服务":
            $ governance_tax_policy = "trade"
            jump gov_tax_trade

label gov_tax_progressive:
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "推行累进税制。拥有越多的人，理应承担更多的责任。"

    hide player_char_img
    $ hide_all_chars("farmer_rep_img")
    show farmer_rep_img at left with dissolve
    farmer_rep "领主大人……"
    "米勒激动得双手颤抖，几乎要跪下去。"
    farmer_rep "感谢您！感谢您听见了我们的声音！"

    hide farmer_rep_img
    $ hide_all_chars("tax_collector_img")
    show tax_collector_img at left with dissolve
    tax_collector "英明的决断。我会立即着手拟定细则。"
    tax_collector "不过……贵族们恐怕不会善罢甘休。"

    $ hide_all_chars()
    "果然，消息传出后，几位拥有大片庄园的小贵族联名写了抗议书。"

    "几天后，边境商队传来消息：冯·哈根男爵在他自己的宴席上，把艾登堡的新税制称为「荒唐的闹剧」。"
    "他没有任何法理渠道干预你的内政，但他已经在贵族圈里散布这个说法——「艾登堡今天敢对自己的贵族动手，明天就敢对别人动手」。"
    "几位原本与艾登堡保持中立的贵族，开始重新考虑他们的立场。"

    hide tax_collector_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "不过……这确实是正确的做法。您父亲若在天之灵，应该会感到欣慰。"

    hide aldric_img with dissolve

    $ hide_all_chars()
    "消息像春风一样传遍了每个村庄。"
    "在河谷、在磨坊、在田间地头，农民们第一次觉得——这位新领主，或许真的不一样。"

    $ change_stat("reputation", 10)
    $ change_stat("loyalty", 10)
    $ change_stat("wealth", -8)
    $ change_prosperity(15)
    $ change_rel("rel_baron", -15)

    "声望提升。忠诚提升。短期财政略有损耗，但民心所向。"
    "贵族圈的敌意正在暗中酝酿……"

    $ governance_events_seen.append("tax_reform")
    jump gov_tax_reform_end

label gov_tax_flat:
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "统一税制。法律面前，人人平等。无论贵贱，缴纳相同比例。"

    hide player_char_img
    $ hide_all_chars("tax_collector_img")
    show tax_collector_img at left with dissolve
    tax_collector "这是最不容易引起争议的方案。我会按照统一标准重新核算。"

    "米勒的表情有些复杂。"

    hide tax_collector_img
    $ hide_all_chars("farmer_rep_img")
    show farmer_rep_img at left with dissolve
    farmer_rep "这……比以前好一些，但……"
    farmer_rep "小人不敢多言。领主大人做的决定，一定有道理。"

    "他的话里藏着失望，但他没有勇气说出来。"

    hide farmer_rep_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "折中之策。不会有人太满意，但也不会有人太愤怒。"
    aldric "这或许是最安全的选择——但「安全」有时意味着「平庸」。"

    hide aldric_img with dissolve

    $ hide_all_chars()
    "统一税制推行后，贵族虽有不满但尚能接受。"
    "农民的负担略有减轻，但远不及他们期望的程度。"
    "街头巷尾，人们对新领主的评价是——不好不坏，中规中矩。"

    $ change_stat("reputation", 5)
    $ change_prosperity(5)

    "声望略有提升。局势维持稳定，但缺乏亮点。"

    $ governance_events_seen.append("tax_reform")
    jump gov_tax_reform_end

label gov_tax_trade:
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "将税收重心转向贸易。让每一笔交易都为艾登堡的发展贡献一份力。"

    hide player_char_img
    $ hide_all_chars("tax_collector_img")
    show tax_collector_img at left with dissolve
    tax_collector "商贸税制……大胆的选择。短期内会带来丰厚的税收。"
    tax_collector "但商人们很可能会减少途经我们领地的贸易量，或者把成本转嫁给消费者。"

    "米勒长出一口气，露出如释重负的表情。"

    hide tax_collector_img
    $ hide_all_chars("farmer_rep_img")
    show farmer_rep_img at left with dissolve
    farmer_rep "只要不再从我们身上刮油，怎么都好……"

    $ hide_all_chars()
    "然而，商会的反应来得比预想的更快。"
    "一封措辞犀利的信件在当天下午就送到了你的书桌上。"

    "信上写着：「尊敬的领主，商贸是艾登堡的命脉。对命脉课以重税，无异于自断经络。」"
    "署名是商会会长克劳斯。"

    hide farmer_rep_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "商会不是好惹的对手。克劳斯控制着大半条贸易通道。"
    aldric "如果他决定绕道……我们的市场会迅速萎缩。"

    hide aldric_img with dissolve

    $ hide_all_chars()
    "尽管如此，短期内，关税带来的收入确实可观。"
    "金库充盈了许多，但市场上的货物开始涨价——这是商人们无声的抗议。"

    $ change_stat("wealth", 15)
    $ change_stat("reputation", -5)
    $ change_prosperity(5)

    "财富大幅增加。但商人们的抵制正在暗中展开……"

    $ governance_events_seen.append("tax_reform")
    jump gov_tax_reform_end


################################################################################
## 4b. ch1_exp_tax_decision 后续分支
################################################################################

label gov_tax_restructure_followup:
    scene bg great_hall with dissolve
    play music "audio/music/tension.ogg" fadeout 1.0 fadein 1.0 if_changed

    "自您下令税改至今，已是一月有余。"
    "田亩与商户的普查在您约定的时限内勉强结题——艾登堡的每一片庄园、每一个商户，都被重新登记造册。"
    "新制按收成比例征收，刚刚在中小户里铺开。粮市的物价稳了一些，村里的逃户也比上个月少了几户。"

    $ hide_all_chars("tax_collector_img")
    show tax_collector_img at left with dissolve
    tax_collector "领主大人，新制在小户和市集里推得很顺。"
    tax_collector "但有几位大贵族——尤其是西境与北境的几个老姓氏——他们的庄园账目至今没交上来。"
    tax_collector "找的理由层出不穷：「账册水浸了」、「老管家病了」、「还没来得及核对」。"

    hide tax_collector_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "他们在拖。"
    aldric "贵族圈里都在看您的态度——是把改革推到底，还是给老姓氏留点情面。"

    hide aldric_img with dissolve

    menu:
        "改革已推行至此，下一步如何决断？"

        "全力推行——大贵族也不能例外":
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "拖延就是抗令。把那几家庄园列出来——税务官随卫队同行复核，三日内必须交账。"
            player "如果有谁敢拒绝，就以违逆领主名义查封庄园账房。"

            hide player_char_img with dissolve

            $ hide_all_chars()
            "命令一下，西境最大的两家联署抗议，并把抗议书递到了王都。"
            "几日后传回消息：冯·哈根男爵在边境酒会上说——「艾登堡这是要把贵族的脖子按到泥里」。"
            "贵族圈的敌意已经从暗流变成明潮。但同样的一封信里也写着——艾登堡的国库账目，整整齐齐。"

            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "少主，您做的是对的事——但您该做好被孤立的准备。"
            aldric "我跟随您父亲三十年，我不喜欢看您走得这么险。"

            hide aldric_img with dissolve

            $ change_stat("reputation", 6)
            $ change_stat("loyalty", 12)
            $ change_stat("wealth", -10)
            $ change_prosperity(15)
            $ change_rel("rel_baron", -18)
            $ change_rel("rel_aldric", -3)

            "改革落地，民心高涨。但贵族圈的反扑已在路上。"

        "温和推行——给大贵族一段缓冲期":
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "新制先在中小户里夯实，大贵族那一档暂缓半年。"
            player "给他们时间整理账册，但条件是——半年内必须交齐，否则照查不误。"

            hide player_char_img
            $ hide_all_chars("tax_collector_img")
            show tax_collector_img at left with dissolve
            tax_collector "明智的安排。贵族要面子，给他们一个台阶，他们多半会顺势下来。"

            hide tax_collector_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "这才是该有的步调。"
            aldric "您父亲若在世，也会这样做——改革不靠一时的硬，靠的是持之以恒的稳。"

            hide aldric_img with dissolve

            $ hide_all_chars()
            "改革放缓了一拍，但每一寸都踏在结实地上。"
            "新制在大半个领地落地，民心稳定，市集兴旺。"
            "那几家观望的大贵族最终交上了账册——虽然个别项目仍有水分，但已经不再公开抵抗。"

            $ change_stat("reputation", 4)
            $ change_stat("loyalty", 6)
            $ change_stat("wealth", -3)
            $ change_prosperity(8)
            $ change_rel("rel_baron", -8)
            $ change_rel("rel_aldric", 5)

            "改革稳步推进。贵族圈不再公开对抗，但暗中不满仍在。"

    # 修 bug: 选了 ch1_exp_tax_decision = "restructure" 跳到这条 followup 的玩家, 之前没设 governance_tax_policy
    # 导致治理报告读不到任何改革标记, 显示"税收制度尚未改革"。restructure 剧情对应"按收成比例征收, 大户多交"= 累进税制。
    $ governance_tax_policy = "progressive"
    $ governance_events_seen.append("tax_reform")
    jump gov_tax_reform_end


label gov_tax_raise_followup:
    scene bg great_hall with dissolve
    play music "audio/music/tension.ogg" fadeout 1.0 fadein 1.0 if_changed

    "自您下令加税至今，已是一月有余——农业税二十、商业税十二。"
    "金库确实有了起色：城墙缺口开始修补，卫队的薪饷也按时发放。"
    "但代价正以另一种方式显现：粮价比新政之前涨了不少，最近三个村庄报来逃户名单，城外开始出现流民。"

    $ hide_all_chars("tax_collector_img")
    show tax_collector_img at left with dissolve
    tax_collector "领主大人，这一季的赋税大致征齐了，但下一季——"
    tax_collector "几个村子已经交不出来。是要派卫队去强征，还是另寻出路？"

    hide tax_collector_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "粮价、流民、逃户——都是同一件事的不同名字。"
    aldric "高税的代价已经显现，且还在累加。"

    hide aldric_img with dissolve

    menu:
        "高税之策已行月余，是否再走下去？"

        "亲自下村——以民望让百姓自愿撑过这段" if reputation >= 50:
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我亲自去村里。让他们看到——这笔银子不是运到我的金库里囤着，是修城墙、买军械、护艾登堡。"
            player "三天，七个村。每一个粮仓我亲自查账，每一个税官我当面训规矩。"

            hide player_char_img with dissolve

            $ hide_all_chars()
            "你做到了。村长们没有少缴税——但抱着账本回家时，表情比上个月轻了一些。"
            "这不是减税。这是「领主自己来扛」的姿态。声望换出来的，就是这种姿态的可信度。"

            $ change_stat("reputation", 3)
            $ change_stat("loyalty", 3)
            $ change_stat("wealth", 3)
            $ change_prosperity(2)
            $ change_rel("rel_aldric", 3)

            "金库未损，民心反增。声望是这次的关键筹码。"

        "维持高税率——艾登堡的安全比一时民怨更重要":
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "维持现状。城墙未修完，卫队未补齐——现在松手，前面这一个多月的代价就白付了。"
            player "派税务官随卫队下村，能征的征齐，征不到的——记下名单，秋后再算。"

            hide player_char_img with dissolve

            $ hide_all_chars()
            "高税继续。金库一日比一日厚，但村庄一日比一日空。"
            "民间开始流传一句话——「艾登堡的银子是用领民的骨头堆出来的」。"
            "奥尔德里克在记录这些消息时一句话也没说，只是把卷宗合上后久久没有抬头。"

            $ change_stat("reputation", -5)
            $ change_stat("loyalty", -10)
            $ change_stat("wealth", 5)
            $ change_prosperity(-10)
            $ change_rel("rel_baron", -3)
            $ change_rel("rel_aldric", -5)

            "金库丰盈。代价是民心渐失。"

        "部分减免——小户先松手":
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "小户的农业税回调到十六，商业税里——年流水五十金以下的小摊贩免一年。"
            player "大户和大商人维持原税率，他们撑得住。"
            player "金库会少些进项，但这是必须付的代价。"

            hide player_char_img
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "您终于愿意松手了。"
            aldric "这一调，逃户会回来，流民会散去——民心比银子更难赚回，也更值得赚回来。"

            hide aldric_img with dissolve

            $ hide_all_chars()
            "减税令颁布之后，村庄的炊烟重新升起。"
            "粮价应声回落，第二个月就有逃户开始返村。"
            "金库的进项虽然少了，但城里城外的气氛松弛了下来。"

            $ change_stat("reputation", 5)
            $ change_stat("loyalty", 6)
            $ change_stat("wealth", -5)
            $ change_prosperity(5)
            $ change_rel("rel_aldric", 5)

            "民心略复。金库稍损，但根基稳了。"

    $ governance_events_seen.append("tax_reform")
    jump gov_tax_reform_end


label gov_tax_lower_intro:
    scene bg great_hall with dissolve
    play music "audio/music/tension.ogg" fadeout 1.0 fadein 1.0 if_changed

    "您节流已是月余。城墙北面与东面已修，西南两面缺口仍在；卫队新兵薪资减半，老兵勉强按时发饷。"
    "节流能省的都省了，再砍下去就要砍到骨头里。"

    $ hide_all_chars("tax_collector_img")
    show tax_collector_img at left with dissolve
    tax_collector "领主大人，光节流是不够的——艾登堡需要一个长期、稳定的税制。"

    hide tax_collector_img with dissolve

    jump gov_tax_reform_choice


label gov_tax_reform_end:
    scene bg study with dissolve

    "回到书房，你独自坐在父亲留下的橡木书桌前。"
    "烛火摇曳，映照着桌上堆积如山的文书。"

    if prologue_study_focus == "commerce":
        "你习惯性地翻开账册，目光扫过每一行数字——修道院那个犹太裔学者教的那些东西，终于派上了用场。"
        if karl_met:
            "凭着对货币流通的敏锐直觉，你很快发现了几处可以优化的环节：一批积压的羊毛可以趁价高出手，卡尔提过的那两条闲置商路可以重新启用。"
        else:
            "凭着对货币流通的敏锐直觉，你很快发现了几处可以优化的环节：一批积压的羊毛可以趁价高出手，两条闲置的贸易通道可以重新启用。"
        "这些「小钱」加起来，足以让金库多喘一口气。"
        $ change_stat("wealth", 5)

    "治理一个领地，远比想象中复杂。"
    "每一个决定都牵动着千百人的命运——这种分量，足以压垮任何轻率的心灵。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "父亲，你当年是怎么做的？"

    $ hide_all_chars()
    "沉默中，似乎能听见远处村庄里传来的犬吠声。"
    "夜很深了。明天还有更多的决定等着你。"

    hide player_char_img with dissolve
    return

################################################################################
## 5. Part 2: 饥荒危机 (gov_famine_crisis)
################################################################################

label gov_famine_crisis:
    if "famine_crisis" in governance_events_seen:
        return

    scene bg village with dissolve
    play music "audio/music/sad.ogg" fadeout 1.0 fadein 1.0 if_changed

    "入秋以来，雨水就断了。"
    "田地龟裂，庄稼枯萎，河流瘦成了一条浑浊的细线。"
    "这是十五年来最严重的旱灾。"

    "你骑马巡视领地，所见之处触目惊心。"

    "干裂的土地上，枯黄的麦穗耷拉着头，像是在无声地哀求。"
    "一个老农蹲在田埂上，双手捧着一把干土，泪流满面。"

    scene bg great_hall with dissolve

    "回到城堡后，你立即召集会议。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "情况比我们预想的更糟。"
    aldric "照目前的估算，今年的收成最多只有往年的三成。"

    if built_granary:
        aldric "好在山上那座新粮仓建成了。五千石存粮一粒未动——省着吃，够全领地撑到开春。"
        "（由于粮仓储备充足，危机就地化解。）"

        hide aldric_img with dissolve

        $ hide_all_chars()
        "你当天就下令开仓。各村按户领粮，凭里正画押，每十日一次。"
        "粮价没有涨起来，也没有人抢仓。头一批领到粮的，是河谷那几个受灾最重的村子。"

        $ hide_all_chars("farmer_rep_img")
        show farmer_rep_img at left with dissolve
        farmer_rep "领主大人，河谷的人让我给您带句话——"
        farmer_rep "您在山上动工的时候，还有人嘀咕这是乱花钱。现在没人说了。"

        $ hide_all_chars()
        "旱情一直拖到开春才缓。但艾登堡没有饿死一个人。"

        $ change_stat("loyalty", 8)
        $ change_stat("reputation", 5)
        $ change_prosperity(5)
        $ famine_prevented = True
        $ governance_events_seen.append("famine_crisis")
        return
    elif governance_prosperity >= 60:
        aldric "不过，由于您之前的治理有方，我们的粮仓还有相当的储备。"
        aldric "至少……不至于饿死人。但我们仍需谨慎行事。"
        "（由于繁荣度较高，危机的烈度有所降低。）"
    else:
        aldric "更要命的是，我们的粮仓储备也严重不足。"
        aldric "如果不能在入冬前找到粮食来源，恐怕会有人饿死。"

    hide aldric_img with dissolve

    show captain_img at right with dissolve

    captain "边境的几个村子已经开始出现骚动了。"
    captain "有人在抢夺邻居的存粮，还有人试图闯入地主的谷仓。"
    captain "如果不尽快采取行动，局势会迅速恶化。"

    hide captain_img with dissolve

    $ hide_all_chars("farmer_rep_img")
    show farmer_rep_img at left with dissolve
    farmer_rep "领主大人！"
    "米勒满头大汗地跑进大厅，扑通一声跪下。"
    farmer_rep "河谷的人已经开始吃草根和树皮了！"
    farmer_rep "求您救救他们！再过半个月，就真的来不及了！"

    "你捏了下眉心。每一条路都有代价，但不做选择也是一种选择——最糟糕的那种。"

    hide farmer_rep_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "我们有几个方案——"

    aldric "第一，向外地商人购买粮食。但旱灾波及面广，粮价已经飞涨。"
    aldric "花费巨大，但能最快解决问题。"

    aldric "第二，实行严格的口粮配给。按人头分配，一粒粮食都不浪费。"
    aldric "能撑更久，但百姓会怨声载道——饥饿中的人，耐心是最少的。"

    aldric "第三，开放城堡自己的粮库。您的存粮……分给百姓。"
    aldric "这会赢得巨大的民心，但城堡的防御力会受到影响——"
    aldric "饥饿的守军无法战斗。"

    hide aldric_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "还有第四种办法。"

    show captain_img at right with dissolve

    captain "我的探子报告说，男爵的运粮队伍后天会经过鸦岭。"
    captain "那批粮食足够我们撑过整个冬天。"
    captain "当然……这意味着和男爵撕破脸。"

    hide captain_img
    hide aldric_img with dissolve

    menu:
        "粮仓只剩两周的存量。"

        "亲自下村组织自救——你的话能让百姓愿意撑" if loyalty >= 60:
            $ change_stat("loyalty", 8)
            $ change_stat("reputation", 5)
            $ change_stat("wealth", -3)
            $ change_prosperity(3)
            $ governance_events_seen.append("famine")

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我去村里。每一个粮仓我亲自看过， 每一户人家我亲自走过。"
            $ hide_all_chars()
            "你不发新政， 不强制配给。你只是站在人群中间。"
            "你跟村长一起喝过苦水。在丧子的母亲面前坐过半天。把自己的口粮分给最瘦的孩子。"
            "村民们没有抢仓， 也没有逃。因为他们知道——领主在挨饿。"
            "三周后春雨来了， 田里冒了第一茬绿。最严酷的两个月被熬过去了——靠的不是粮食， 是人没散。"
            return

        "购买粮食——花钱买平安，用金币换性命":
            jump gov_famine_buy

        "严格配给——勒紧裤腰带，共渡难关":
            jump gov_famine_ration

        "开放城堡粮库——与民同甘共苦":
            jump gov_famine_castle

        "劫夺男爵的运粮队——铤而走险":
            jump gov_famine_raid

label gov_famine_buy:
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "派人去南方的粮商那里，不惜代价购买粮食。"
    player "钱没了可以再赚，人死了就什么都没了。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "明智的决定。我会立即安排。"
    aldric "不过……这笔开销会让我们的金库见底。"

    hide aldric_img with dissolve

    $ hide_all_chars()
    "三天后，满载粮食的马车队缓缓驶入艾登堡。"
    "村民们围在路边，看着那些沉甸甸的麻袋，眼中闪着泪光。"

    $ hide_all_chars("farmer_rep_img")
    show farmer_rep_img at left with dissolve
    farmer_rep "粮食来了！粮食来了！"

    $ hide_all_chars()
    "米勒跑遍了每个村庄，亲手帮忙分发。"
    "孩子们抱着分到的面包，笑容比秋日的阳光还要灿烂。"

    "危机暂时化解了——但账本上的数字，触目惊心。"

    if governance_prosperity >= 60:
        if prologue_study_focus == "commerce":
            $ change_stat("wealth", -8)
            if gov_merchant_outcome in ("monopoly", "regulated"):
                "凭借你对粮食市场的了解，加上克劳斯商会给的「合作价」，实际花费比预想的少得多。商会的门路，这一次帮了大忙。"
            else:
                "凭借你对粮食市场的了解，你找到了报价最合理的供货商，还谈下了分期付款。实际花费比预想的少得多。"
        else:
            $ change_stat("wealth", -10)
            "由于此前的储备充足，实际花费比预想的少一些。"
    else:
        if prologue_study_focus == "commerce":
            $ change_stat("wealth", -15)
            "支出巨大，但你对粮价行情的判断帮你避开了最离谱的溢价——否则情况会更糟。"
        else:
            $ change_stat("wealth", -20)
            "巨额的支出让金库几乎空了。接下来的很长一段时间，你都需要精打细算。"

    $ change_prosperity(10)
    $ change_stat("loyalty", 5)
    $ famine_prevented = True

    jump gov_famine_end

label gov_famine_ration:
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "实行口粮配给制度。按人头分配，任何人不得多占。"
    player "包括贵族——这一次，没有特权。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "公平的配给……在理论上是可行的。"
    aldric "但执行起来会非常困难。饥饿会让人变得疯狂。"

    hide aldric_img with dissolve

    $ hide_all_chars()
    "配给制推行后，每家每户只能领到勉强维持生存的口粮。"
    "街上的人们面色蜡黄，脚步虚浮。活着，仅仅是活着。"

    "然而，不满的声音像地下的火焰一样蔓延。"

    $ hide_all_chars("farmer_rep_img")
    show farmer_rep_img at left with dissolve
    farmer_rep "领主大人……配给的量实在太少了。"
    farmer_rep "孩子们整天哭着喊饿，老人们瘦得只剩骨头……"

    $ hide_all_chars()
    "更糟的是，开始有人偷抢别人的配给。"
    "一场为了半袋面粉的斗殴导致两人受伤。"

    show captain_img at right with dissolve

    captain "治安在恶化。我已经加强了巡逻，但兵力有限。"

    hide captain_img with dissolve

    $ hide_all_chars()
    "漫长的冬天终于过去。勉强撑了过来，但代价是深重的民怨。"

    $ change_stat("loyalty", -10)
    $ change_prosperity(-5)
    $ famine_prevented = True

    "忠诚下降。饥饿没有杀死人，却杀死了一些信任。"

    jump gov_famine_end

label gov_famine_castle:
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "打开城堡的粮库。我的粮食，就是百姓的粮食。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "领主大人……这个决定需要极大的勇气。"
    aldric "城堡的存粮本是用于支撑守军和应对围城的。"
    aldric "如果在此期间遭到攻击……"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "如果百姓饿死了，这座城堡守给谁看？"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "……您说得对。"

    hide aldric_img with dissolve

    $ hide_all_chars()
    "城堡的粮库大门打开的那一刻，守卫们面面相觑。"
    "但当他们看见第一批百姓——那些瘦骨嶙峋的老人、面黄肌瘦的孩子——"
    "没有一个人提出异议。"

    $ hide_all_chars("farmer_rep_img")
    show farmer_rep_img at left with dissolve
    farmer_rep "领主大人……"
    "米勒跪在地上，泣不成声。"
    farmer_rep "老天爷派来了一个好人……一个真正的好人啊……"

    $ hide_all_chars()
    "消息传遍了整个领地。"
    "人们口口相传——「新领主把自己的粮食分给了我们。」"
    "在所有关于权谋和阴谋的故事里，这个简单的善举，像一束光照进了黑暗。"

    $ change_stat("loyalty", 15)
    $ change_stat("reputation", 10)
    $ change_prosperity(10)
    $ famine_prevented = True

    show captain_img at right with dissolve

    captain "领主大人，城堡的粮食储备已经降到危险水平。"
    captain "如果遭遇围城，我们最多只能坚持五天。"

    hide captain_img with dissolve

    $ hide_all_chars()
    "这是你做出的交换——用军事安全换民心。"
    "但愿在粮食补充之前，不会有敌人来敲门。"

    $ change_stat("power", -5)

    jump gov_famine_end

label gov_famine_raid:
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "……队长，你说的那批运粮队，有多少护卫？"

    hide player_char_img
    show captain_img at right with dissolve

    captain "大约二十人。我们可以出动五十人在鸦岭设伏。"
    captain "以我们的训练水平，应该可以在不造成太多伤亡的情况下拿下。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "那就去做。"

    hide player_char_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "遵命。不过……我必须提醒您，这等于向男爵宣战。"

    hide captain_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "他囤积粮食看着百姓饿死，这算什么贵族的担当？"

    hide captain_img with dissolve

    $ hide_all_chars()
    "两天后的清晨，雷恩队长率五十名精锐伏击了运粮队。"
    "战斗很快就结束了——男爵的护卫在意料之外的攻势面前几乎没有抵抗。"

    "满满十二车粮食被带回了艾登堡。"
    "够整个领地撑过冬天，绰绰有余。"

    $ hide_all_chars("farmer_rep_img")
    show farmer_rep_img at left with dissolve
    farmer_rep "这些粮食是从哪里来的？"

    hide farmer_rep_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你不需要知道来源。只需要知道——没有人会饿死。"

    "百姓们欢天喜地，但明白内情的人都知道——这笔债迟早要还。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "男爵的信使已经来了。措辞很……激烈。"
    aldric "他称这是「公然的强盗行为」，并要求立即归还粮食和赔偿损失。"
    aldric "否则……他将诉诸武力。"

    hide aldric_img with dissolve

    $ change_stat("power", 10)
    $ change_stat("reputation", -5)
    $ change_prosperity(15)
    $ change_rel("rel_baron", -25)
    $ famine_prevented = True

    $ hide_all_chars()
    "粮食问题解决了，但一场更大的风暴正在酝酿。"
    "男爵不会忘记这个羞辱。"

    jump gov_famine_end

label gov_famine_end:
    scene bg study with dissolve

    "饥荒的阴影终于退去，但它留下的痕迹不会轻易消失。"
    "那些饥饿的面孔、绝望的眼神——它们会永远刻在你的记忆里。"
    "提醒你，一个领主的责任不仅仅是坐在高位上发号施令。"

    if prologue_study_focus == "commerce":
        "危机过后，你利用对供需关系的理解，从周边领地低价收购了一批灾后贱卖的种子和农具。"
        "这笔交易几乎不花什么钱，但明年开春播种时会省下一大笔。"
        $ change_stat("wealth", 5)
    else:
        "危机过后，流离的农民陆续回到土地上。恢复耕种的田地虽然减产，但至少有了收入。"
        $ change_stat("wealth", 2)

    $ governance_events_seen.append("famine_crisis")
    return

################################################################################
## 6. Part 3: 建设工程 (gov_building)
################################################################################

label gov_building:
    scene bg village with dissolve
    play music "audio/music/castle_calm.ogg" fadeout 1.0 fadein 1.0 if_changed

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "领主大人，是时候讨论一下本季度的建设计划了。"
    aldric "领地的发展不能只靠应对危机——我们需要主动投资未来。"

    hide aldric_img with dissolve

    "你翻开工程规划书，几个方案映入眼帘。"

    $ hide_all_chars()
    menu:
        "本季度的建设重点是——"

        "建造学堂——教化百姓，开启民智" if not built_school:
            jump gov_build_school

        "建造诊所——治病救人，保障民生" if not built_clinic:
            jump gov_build_clinic

        "建造粮仓——广积粮草，以备不时之需" if not built_granary:
            jump gov_build_granary

        "建造望楼——加强防御，预警敌袭" if not built_watchtower:
            jump gov_build_watchtower

        "暂不建设——把人手和石料留到下一季":
            $ hide_all_chars("aldric_img")
            show aldric_img at left with dissolve
            aldric "也好。工程一旦开了头，人手就抽不回来了。等局势明朗些再动工，不迟。"
            hide aldric_img with dissolve
            return

label gov_build_school:
    $ built_school = True

    scene bg village with dissolve

    show player_char_img at left with dissolve
    player "建一座学堂。让孩子们学会读写，让农夫们懂得算术。"
    player "一个愚昧的领地，永远不可能真正强大。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "这是……着眼长远的决定。许多领主只关心眼前的利益。"
    aldric "您却愿意为十年后投资。令人钦佩。"

    hide aldric_img with dissolve

    $ hide_all_chars()
    "学堂选址在村子中央的一块空地上。"
    "工匠们忙碌起来——搬运石材、架设房梁、铺设屋顶。"
    "村里的孩子们好奇地围在工地外面，叽叽喳喳地议论着。"

    "一个月后，一座朴素但坚固的石砌建筑拔地而起。"
    "门楣上刻着四个字——「明德学堂」。"

    "你从城里请来了一位退休的文书做先生。"
    "开学那天，二十多个孩子坐在崭新的木凳上，眼睛里闪着从未有过的光芒。"

    if ch1_deep_widow_verdict == "work":

        $ hide_all_chars()
        "人群散去时，你注意到教室最后一排，还有个少年在慢慢整理残留的木板和石笔。"

        "那是当年被你判做工的少年汉斯。这些月来他一直留在城堡做杂务，今日是他主动请缨来帮忙布置学堂。"

        "他比半年前瘦削挺拔了些。搬运木板时动作还不熟练，但每一次都很认真。"

        "他把最后一支石笔摆正，像是在摆一件庄重的东西。"

        "「先生，这本书放这儿可以吗？」他朝管家问道，声音里没有当初法庭上的颤抖。"

        "你没有走过去。只是站在门口看了一会儿，然后去看别的。"

    $ hide_all_chars("farmer_rep_img")
    show farmer_rep_img at left with dissolve
    farmer_rep "领主大人，我……我一辈子不识字。"
    farmer_rep "但我的儿子——他昨天回来，给我念了一段书。"
    farmer_rep "我听不太懂，但那一刻，我觉得……一切辛苦都值了。"

    $ hide_all_chars()
    "一个能读会写的农民，一个懂得记账的商贩，一个知晓战术的士兵——"
    "教育的种子一旦播下，它的回报将远超任何人的想象。"

    $ change_education(20)
    $ change_stat("reputation", 5)
    $ change_prosperity(5)
    $ change_stat("wealth", -3)

    "教育水平提升。声望提升。这笔投资的回报，将在未来的岁月中慢慢显现。"

    hide farmer_rep_img with dissolve
    return

label gov_build_clinic:
    $ built_clinic = True

    scene bg village with dissolve

    show player_char_img at left with dissolve
    player "建一座诊所。百姓们生了病，不应该只能听天由命。"

    "消息传出后，一位名叫玛格丽特的女医师主动找上了门。"

    hide player_char_img
    $ hide_all_chars("healer_img")
    show healer_img at left with dissolve
    healer "领主大人，在下玛格丽特，曾在南方的修道院学习医术十年。"
    healer "听说您要建诊所，我想毛遂自荐。"

    hide healer_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你有什么本事？"

    hide player_char_img
    $ hide_all_chars("healer_img")
    show healer_img at left with dissolve
    healer "我能辨认三百种草药，会接骨、缝合伤口、配制退烧药剂。"
    healer "还精通产科——在修道院时，我接生过上百个婴儿，无一夭折。"

    hide healer_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我们需要你这样的人。诊所的事就交给你了。"

    hide player_char_img
    $ hide_all_chars("healer_img")
    show healer_img at left with dissolve
    healer "谢领主大人的信任！我不会让您失望的。"

    $ hide_all_chars()
    "诊所选在城中心一处敞亮的石屋里——原本是一间久未启用的仓房。"
    "玛格丽特亲自监督施工，对每一个细节都要求严格。"

    $ hide_all_chars("healer_img")
    show healer_img at left with dissolve
    healer "窗户要开大一些，通风很重要。"
    healer "药房要和病房隔开，避免交叉感染。"
    healer "还需要一口深井——干净的水源是治病的基础。"

    $ hide_all_chars()
    "诊所落成后，玛格丽特开始了她的工作。"
    "第一周就接诊了三十多人——骨折的、发烧的、难产的、被蛇咬的。"
    "在此之前，这些人的选择只有「扛着」或者「等死」。"

    "一个患了肺热的老人被家人抬来，已经奄奄一息。"
    "三天后，他竟然自己走着出了诊所的门。"

    hide healer_img
    $ hide_all_chars("farmer_rep_img")
    show farmer_rep_img at left with dissolve
    farmer_rep "这是神迹啊！玛格丽特大夫简直是上天派来的！"

    hide farmer_rep_img
    $ hide_all_chars("healer_img")
    show healer_img at left with dissolve
    healer "不是神迹，是医术。是知识。"
    healer "将来若能在艾登堡办一所学堂，我还想教几个年轻人学医。"
    healer "一个人救不了所有人——但十个人、一百个人就可以。"

    $ change_health(20)
    $ change_stat("loyalty", 10)
    $ change_prosperity(5)
    $ change_stat("wealth", -3)

    "公共健康大幅改善。忠诚提升。百姓的感激之情溢于言表。"

    hide healer_img with dissolve
    return

label gov_build_granary:
    $ built_granary = True

    scene bg village with dissolve

    show player_char_img at left with dissolve
    player "建一座大型粮仓。丰年存粮，荒年取用。"
    player "未雨绸缪，胜过亡羊补牢。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "实用主义的选择。不那么引人注目，但关键时刻能救命。"

    hide aldric_img with dissolve

    $ hide_all_chars()
    "粮仓建在地势较高的山丘上，远离河道——防止洪水浸泡。"
    "石基、木架、通风口、防鼠板——每一处设计都经过了深思熟虑。"

    $ hide_all_chars("tax_collector_img")
    show tax_collector_img at left with dissolve
    tax_collector "按照规划，这座粮仓可以储存五千石粮食。"
    tax_collector "足以让整个领地在完全断粮的情况下支撑三个月。"

    $ hide_all_chars()
    "粮仓落成后，你下令在每次收获后将一部分粮食存入。"
    "农民们起初有些不情愿——毕竟那是他们辛苦种出来的。"
    "但米勒帮你做了说服工作。"

    hide tax_collector_img
    $ hide_all_chars("farmer_rep_img")
    show farmer_rep_img at left with dissolve
    farmer_rep "乡亲们，听我说一句！"
    farmer_rep "你们还记得上次大旱吗？那年饿死了多少人？"
    farmer_rep "现在领主大人帮我们建了粮仓，就是不想让那种事再发生！"
    farmer_rep "每家多交一点，关键时刻能救全村人的命！"

    $ hide_all_chars()
    "在米勒的劝说下，大部分农户接受了存粮的安排。"
    "望着逐渐填满的粮仓，你心中有了一丝踏实。"

    $ change_prosperity(10)
    $ change_infrastructure(10)
    $ change_stat("wealth", -3)

    "繁荣度提升。基础设施改善。一个看似平凡的决定，却可能在未来挽救无数生命。"

    hide farmer_rep_img with dissolve
    return

label gov_build_watchtower:
    $ built_watchtower = True

    scene bg village with dissolve

    show player_char_img at left with dissolve
    player "在边境建造望楼。知己知彼，百战不殆。"
    player "再好的城墙，也比不上提前一天的预警。"

    hide player_char_img
    show captain_img at right with dissolve

    captain "英明的决策！我早就想提议了。"
    captain "有了望楼，敌人的一举一动都逃不过我们的眼睛。"

    hide captain_img with dissolve

    $ hide_all_chars()
    "望楼建在艾登堡北面的高岗上，那里视野开阔，可以远眺数十里。"
    "石造的塔身高三十尺，顶部设有瞭望台和烽火架。"

    "工程进展很快——毕竟士兵们对这种建筑有天然的热情。"
    "他们亲手搬运石块、涂抹灰泥，干劲比任何工匠都足。"

    show captain_img at right with dissolve

    captain "望楼已经完工！我安排了两组人轮班瞭望，日夜不间断。"
    captain "白天用旗语，夜间用烽火。从发现敌情到城堡收到警报，不超过一刻钟。"

    hide captain_img with dissolve

    $ hide_all_chars()
    "第一次发挥作用是在一个月后的深夜——"
    "望楼的烽火突然亮起，紧接着旗语传来：北方有一队不明骑兵正在接近。"

    "守军迅速集结，弓箭手就位。"
    "那队骑兵最终在城墙外停下，发现艾登堡已有准备后，掉头往来路退去。巡逻兵的脚步声在城头上来回走了一整夜。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "如果没有望楼，等我们发现他们的时候，恐怕已经来不及了。"

    $ change_stat("power", 5)
    $ change_infrastructure(10)
    $ change_stat("wealth", -3)

    "军事力量提升。基础设施改善。在这个充满敌意的世界里，警觉是最好的盔甲。"

    hide captain_img with dissolve
    return

################################################################################
## 7. Part 4: 瘟疫恐慌 (gov_plague)
################################################################################

label gov_plague:
    if "plague" in governance_events_seen:
        return

    scene bg village with dissolve
    play music "audio/music/tension.ogg" fadeout 1.0 fadein 1.0 if_changed

    "坏消息像冬天的寒风一样席卷而来。"

    show captain_img at right with dissolve

    captain "领主大人，南边的两个村子出现了怪病。"
    captain "高烧不退、全身溃烂、咳血……三天内已经死了十几个人。"

    hide captain_img with dissolve

    $ hide_all_chars()
    "两个字像铁锤一样砸在每个人的心上——"
    "瘟疫。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "如果是瘟疫……我们必须立即采取行动。"
    aldric "这种东西一旦蔓延开来，死的就不是十几个人了。"

    hide aldric_img with dissolve

    $ hide_all_chars()
    "恐慌比瘟疫本身传播得更快。"
    "市场上的人一夜之间少了大半。"
    "有人开始抢购食物和药材，有人连夜带着家人逃离。"
    "还有人跪在教堂前彻夜祈祷，认为这是上天的惩罚。"

    if built_clinic:
        jump gov_plague_clinic
    else:
        jump gov_plague_no_clinic

label gov_plague_clinic:
    "但你有一张底牌——玛格丽特和她的诊所。"

    $ hide_all_chars("healer_img")
    show healer_img at left with dissolve
    healer "领主大人，我已经检查了几名病患的症状。"
    healer "好消息是，这不是真正的黑死病。它更像是一种严重的伤寒。"
    healer "虽然危险，但可以治疗。"

    hide healer_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你需要什么？"

    hide player_char_img
    $ hide_all_chars("healer_img")
    show healer_img at left with dissolve
    healer "第一，隔离所有感染者。我需要一个独立的空间。"
    healer "第二，大量的新鲜草药——特别是柳树皮和薄荷。"
    healer "第三，干净的水源。感染者必须大量饮水。"
    healer "第四——也是最重要的——给我时间。我能控制住。"

    hide healer_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你需要的一切，我都会提供。雷恩，全力配合玛格丽特。"

    hide player_char_img
    show captain_img at right with dissolve

    captain "遵命！"

    hide captain_img with dissolve

    $ hide_all_chars()
    "接下来的两周是一场与死神的赛跑。"
    "玛格丽特几乎不眠不休，在隔离棚里穿梭、诊治、配药。"
    "她的手因为反复清洗而皲裂流血，但她连包扎的时间都不肯浪费。"

    "终于，在第十五天，好消息传来——"
    "没有新的感染者。已感染的病人中，八成以上正在康复。"

    $ hide_all_chars("healer_img")
    show healer_img at left with dissolve
    healer "控制住了。"
    $ hide_all_chars()
    "玛格丽特说完这三个字，身体一软，差点倒在地上。"
    "她已经连续工作了四十个小时。"

    hide healer_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "送玛格丽特回去休息。从今天起，她的俸禄翻倍。"

    $ hide_all_chars()
    "这场瘟疫恐慌的最终死亡人数——七人。"
    "在一个没有诊所的领地，这个数字可能是七十、七百。"
    "建诊所的决定，在此刻获得了最沉重也最珍贵的回报。"

    $ change_health(10)
    $ change_stat("faith", 5)
    $ change_stat("loyalty", 10)
    $ change_prosperity(5)

    "公共健康改善。忠诚提升。玛格丽特的名字将被艾登堡的百姓世代铭记。"

    hide player_char_img with dissolve
    $ governance_events_seen.append("plague")
    return

label gov_plague_no_clinic:
    "没有诊所，没有医师——你几乎是赤手空拳面对这场灾难。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "我们没有专业的医师，只有几个乡间的草药婆。"
    aldric "在这种情况下，我们必须做出艰难的选择。"

    hide aldric_img with dissolve

    menu:
        "瘟疫在蔓延，你必须立即行动。"

        "亲自带教会修士进疫区祷告 + 救治——你的虔信能稳住人心" if faith >= 60:
            $ change_stat("faith", 5)
            $ change_stat("loyalty", 5)
            $ change_stat("reputation", 3)
            $ change_health(-3)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我和修士一起进村。我跪在祭坛前祈祷， 让他们看到——我没有逃。"
            $ hide_all_chars()
            "你穿了一身朴素的灰袍， 跟修士们一起进了疫区。每天清晨在教堂祷告， 白天分发草药和食物。"
            "村民们一开始畏缩， 但你跪着喂第一个老人喝水的那一刻——人群里有人哭出声。"
            "瘟疫没有立刻停。但每一个濒死的人都知道——领主在身边。"
            "三周后疫情消退。死亡人数比你预想的少了一半——不是因为药， 是因为人没乱。"
            $ governance_events_seen.append("plague")
            return

        "封锁隔离——虽然残忍，但能阻止扩散":
            jump gov_plague_quarantine

        "派人前往救治——哪怕冒着被感染的风险":
            jump gov_plague_healers

        "向教会求助——或许神的力量能拯救众生":
            jump gov_plague_prayer

        "烧毁感染村庄——用烈火斩断瘟疫的根源":
            jump gov_plague_burn

label gov_plague_quarantine:
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "封锁那两个村子。任何人不得进出。"
    player "同时给他们送去食物和水——但人，不能放出来。"

    hide player_char_img
    show captain_img at right with dissolve

    captain "明白。我会在村子周围设置封锁线。"

    hide captain_img with dissolve

    $ hide_all_chars()
    "封锁线建立后，村里传出了绝望的呼喊。"
    "有人试图翻越栅栏，被士兵推了回去。"
    "一个母亲抱着发烧的孩子，跪在封锁线外哭嚎——"
    "「求求你们！让我的孩子出去！他会死在里面的！」"

    "士兵们红着眼睛，但没有让步。"
    "你站在远处，拳头攥得咯吱作响。"

    "封锁持续了三周。"
    "当最后一个感染者痊愈或死亡后，封锁线终于撤除。"

    "最终的死亡人数——三十二人。"
    "如果没有封锁，这个数字可能是数百。"
    "但那三十二条命的重量，你此生都无法放下。"

    $ change_health(-10)
    $ change_stat("loyalty", -5)
    $ change_prosperity(-5)

    "这是残忍的正确。人们会记住你的果断——但也会记住封锁线内的哭声。"

    $ governance_events_seen.append("plague")
    return

label gov_plague_healers:
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "组织志愿者进入疫区救治。我们不能见死不救。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "领主大人……这意味着那些志愿者也可能感染。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我知道。但我不会下令让任何人去——只接受自愿。"

    hide player_char_img with dissolve

    $ hide_all_chars()
    "出乎意料的是，自愿者比预想的多得多。"
    "几个草药婆、两个退伍的军医、甚至一些普通农妇——"
    "她们抱着草药和干净的布匹，走进了那个人人避之不及的地方。"

    "两周后，疫情终于被控制住了。"
    "但代价是惨痛的——五名志愿者感染，其中两人没能挺过来。"

    "你为牺牲的志愿者举行了庄严的葬礼。"
    "全村人都来了。人们默默垂泪。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "她们是英雄。她们的名字将刻在艾登堡的纪念碑上。"

    $ change_stat("faith", 5)
    $ change_health(-5)
    $ change_stat("loyalty", 5)
    $ change_stat("reputation", 5)

    "信仰提升。忠诚提升。这个领地有了自己的英雄。"

    $ governance_events_seen.append("plague")
    return

label gov_plague_prayer:
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "请主教派遣神职人员前往疫区，为病人祈祷和净化。"

    hide player_char_img
    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve

    bishop "主会指引我们。我将亲自带领修士们前往。"
    bishop "瘟疫是对信仰的考验——而我们不会退缩。"

    hide bishop_img with dissolve

    $ hide_all_chars()
    "主教带着十二名修士进入了疫区。"
    "他们日夜诵经、为病人擦拭身体、分发圣水和面包。"
    "与其说是医疗，不如说是一种精神上的抚慰。"

    "奇妙的是，疫情确实在两周后开始消退。"
    "是祈祷的力量？还是疾病本身到了尾声？没人说得清。"
    "但教会的声望空前高涨。"

    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve
    bishop "主听到了我们的祈祷。这是祂的恩典。"

    $ hide_all_chars()
    "死亡人数——二十六人。不是最好的结果，也不是最坏的。"
    "但教会在这场危机中树立了崇高的形象。"

    $ change_stat("faith", 15)
    $ change_health(-5)
    $ change_rel("rel_bishop", 10)

    "信仰大幅提升。主教的影响力进一步扩大——这是好事还是坏事，只有时间知道。"

    hide bishop_img with dissolve
    $ governance_events_seen.append("plague")
    return

label gov_plague_burn:
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "……烧掉它。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "领主大人——？"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "把感染的村庄烧掉。连同里面所有可能携带病毒的东西。"
    player "先把活着的人转移出来。但房屋、牲畜、粮食——全部烧毁。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "……这是极端的手段。但如果能阻止瘟疫……"

    hide aldric_img with dissolve

    $ hide_all_chars()
    "火焰在夜空中升起，将两个村庄吞没。"
    "浓烟遮蔽了星空，空气中弥漫着焦糊的味道。"

    "被转移出来的村民们站在远处，呆呆地看着自己的家化为灰烬。"
    "有人嚎啕大哭，有人一言不发，有人直直地跪了下去。"

    $ hide_all_chars("farmer_rep_img")
    show farmer_rep_img at left with dissolve
    farmer_rep "我们的家……我们一辈子的心血……"

    $ hide_all_chars()
    "瘟疫确实被彻底消灭了。"
    "但那两个村庄——连同村民们所有的财产、记忆、生活——也一起消失了。"

    "死亡人数——八人。是所有方案中最少的。"
    "但失去家园的一百多户人家，他们眼中的恨意，不比死亡温和多少。"

    $ change_stat("power", 5)
    $ change_stat("loyalty", -15)
    $ change_stat("reputation", -10)
    $ change_health(10)
    $ change_prosperity(-10)

    "瘟疫被消灭了。但民心也被烧掉了一部分。"
    "在权力的棋盘上，你多了一颗筹码——但也少了一些灵魂。"

    hide farmer_rep_img with dissolve
    $ governance_events_seen.append("plague")
    return

################################################################################
## 8. Part 5: 开春庆典 (gov_festival)
################################################################################

label gov_festival:
    if "festival" in governance_events_seen:
        return
    if governance_prosperity < 60:
        return

    scene bg marketplace with dissolve
    play music "audio/music/tavern_lively.ogg" fadeout 1.0 fadein 1.0 if_changed

    "初春的暖阳洒在艾登堡的集市广场上，积雪已经化尽，泥土散发着解冻的气息。"
    "这个冬天格外漫长，但领地熬过来了——粮仓还有余粮，牲畜没有冻死，没有人饿肚子。"
    "人们决定举办一场开春庆典，庆祝这来之不易的安稳。"

    "广场被装扮一新。彩旗飘扬，花环遍地。"
    "卖烤肉的小贩支起了摊子，啤酒桶一字排开。"
    "孩子们在人群中穿梭追逐，笑声像银铃一样清脆。"

    "一个老琴师坐在角落里拉着手风琴，旋律悠扬而温暖。"
    "年轻的姑娘和小伙子们手拉手围成圆圈，跳着古老的迎春舞。"

    "你和奥尔德里克并肩走过热闹的人群。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "看看这些笑脸。有多久没见过了？"
    aldric "自从老领主过世后……这大概是艾登堡最欢乐的一天了。"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "是他们应得的。熬过了这个冬天，值得好好庆祝。"

    hide aldric_img with dissolve

    hide player_char_img
    $ hide_all_chars("farmer_rep_img")
    show farmer_rep_img at left with dissolve
    farmer_rep "领主大人！您来啦！"
    "米勒跑过来，满脸通红——显然已经喝了不少。"
    farmer_rep "快来尝尝我媳妇做的苹果馅饼！整个艾登堡最好吃的！"

    hide farmer_rep_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "那我可不能错过。"

    $ hide_all_chars()
    "你接过一块馅饼咬了一口。酥脆的面皮下是甜蜜温热的苹果馅——确实好吃。"

    "米勒得意地笑了，随即又一脸认真地说——"

    hide player_char_img
    $ hide_all_chars("farmer_rep_img")
    show farmer_rep_img at left with dissolve
    farmer_rep "领主大人，我代表所有的乡亲们，谢谢您。"
    farmer_rep "这些日子……虽然不容易，但我们都觉得，日子在变好。"
    farmer_rep "有您在，我们心里踏实。"

    $ hide_all_chars()
    "一个小女孩怯生生地走过来，递给你一束野花。"
    "她的脸蛋红扑扑的，眼睛明亮得像两颗星星。"

    hide farmer_rep_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "谢谢你，小姑娘。这是我收到过最好的礼物。"

    $ hide_all_chars()
    "小女孩羞涩地笑了，然后一溜烟跑回了母亲身边。"

    "夕阳西下时，人们围坐在广场中央，等待你的讲话。"
    "篝火点燃了，橘红色的火光映照着一张张期待的面庞。"

    "你站在临时搭建的台子上，望着下面黑压压的人群。"
    "他们是你的百姓。他们的命运，系在你的每一个决定上。"

    menu:
        "你决定说些什么。"

        "谦逊地感谢百姓——没有你们，就没有今天的丰收":
            jump gov_festival_humble

        "描绘宏伟蓝图——艾登堡的未来将更加辉煌":
            jump gov_festival_vision

        "缅怀逝者——为了那些没能看到今天的人":
            jump gov_festival_honor

label gov_festival_humble:
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "乡亲们！"
    "广场上安静了下来。"

    player "今天的丰收，不是我的功劳。"
    player "是你们——每一个起早贪黑的农夫，每一个风里来雨里去的牧人——"
    player "是你们的汗水浇灌了这片土地，你们的双手创造了这一切。"

    player "我只是做了一个领主该做的事。"
    player "但你们——你们做的比任何领主都多。"

    player "今晚，不分贵贱，不论长幼。"
    player "吃饱喝足，尽情欢乐！"
    player "因为你们值得！"

    $ hide_all_chars()
    "欢呼声如雷鸣般炸响。有人吹起口哨，有人抛起帽子。"
    "一个老妇人悄悄抹了抹眼泪。"

    $ change_stat("loyalty", 10)
    $ change_prosperity(5)

    jump gov_festival_end

label gov_festival_vision:
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "乡亲们！"
    "广场上安静了下来。"

    player "今年的丰收只是开始！"
    player "我要让艾登堡成为这片大陆上最富足、最安全的地方！"
    player "我要修更多的路，建更大的市场，让每个孩子都能读书识字！"

    player "五年之内，艾登堡的名字将传遍整个王国！"
    player "十年之内，没有人再会饿肚子、没有人再会看不起病！"

    player "这是我的承诺——一个领主对他的子民的承诺！"

    $ hide_all_chars()
    "掌声雷动。人们的眼中闪烁着希望的光芒。"
    "不知道这些承诺能否实现——但在这个瞬间，每个人都选择了相信。"

    $ change_stat("reputation", 10)
    $ change_prosperity(5)

    jump gov_festival_end

label gov_festival_honor:
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "乡亲们！"
    "广场上安静了下来。"

    player "在我们举杯庆贺之前，我想请大家记住一些人。"
    player "那些在旱灾中没能撑过来的邻居，那些在疫病中离开的亲人——"
    player "还有我的父亲，这片土地曾经的守护者。"

    "广场上变得极为安静。有人低下了头。"

    player "他们没能看到今天的丰收。但我相信——"
    player "如果他们在天之灵能看到此刻的景象，一定会感到欣慰。"

    player "所以今晚的第一杯酒，敬他们。"
    player "敬所有离开的人。愿他们在另一个世界，也有丰收和欢笑。"

    $ hide_all_chars()
    "你举起酒杯，一饮而尽。"
    "广场上千百人同时举杯——那一刻的沉默，比任何欢呼都更有力量。"

    "然后，不知是谁，轻轻唱起了一首古老的安魂歌。"
    "越来越多的人加入，歌声在篝火的光芒中升腾，融入夜空。"

    $ change_stat("faith", 10)
    $ change_prosperity(5)

    jump gov_festival_end

label gov_festival_end:
    "节日的夜晚漫长而温暖。"
    "人们唱歌、跳舞、喝酒、讲故事，直到月亮高悬。"
    "孩子们在父母怀里沉沉睡去，脸上还挂着幸福的笑容。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "好久没见过这样的景象了。"
    aldric "在所有的阴谋、危机和算计之间……偶尔也该提醒自己——"
    aldric "这些普通人的笑容，才是我们守护的东西。"

    hide aldric_img with dissolve

    $ hide_all_chars()
    "你独自走在回城堡的路上，身后是渐渐安静的广场。"
    "秋风拂面，带着谷物和篝火的香气。"

    "这一刻，你觉得自己不是什么领主、不是什么政治家。"
    "只是一个和千百人一起庆祝丰收的……普通人。"
    "而这种感觉，比任何权力都要珍贵。"

    $ governance_events_seen.append("festival")
    return

################################################################################
## 9. Part 6: 商会谈判 (gov_merchant)
################################################################################

label gov_merchant:
    if "merchant_negotiation" in governance_events_seen:
        return

    scene bg great_hall with dissolve
    play music "audio/music/tension.ogg" fadeout 1.0 fadein 1.0 if_changed

    "一阵沉稳的脚步声响起——那是只有走过无数商路的人才有的节奏。"

    "商会会长克劳斯走进大厅。他身着考究的深棕色外套，手指上戴着一枚刻有天平图案的金戒指。"
    "他五十多岁，头发已经灰白，但目光锐利如鹰。"

    $ hide_all_chars("merchant_guild_img")
    show merchant_guild_img at left with dissolve
    merchant_guild "尊敬的领主大人，感谢您拨冗接见。"
    merchant_guild "在下克劳斯·范德贝格，艾登堡商会会长。"
    merchant_guild "今天前来，是想和您谈一桩对双方都有利的……生意。"

    hide merchant_guild_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "请说。"

    hide player_char_img
    $ hide_all_chars("merchant_guild_img")
    show merchant_guild_img at left with dissolve
    merchant_guild "直说吧——商会希望获得艾登堡贸易通道的独家经营权。"
    merchant_guild "具体来说：所有经过我们领地的货物，由商会统一调度和管理。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "独家经营权？这可不是小事。"

    hide aldric_img
    $ hide_all_chars("merchant_guild_img")
    show merchant_guild_img at left with dissolve
    merchant_guild "当然不是小事，所以回报也不会小。"

    hide aldric_img with dissolve

    merchant_guild "作为交换，商会每年向领主缴纳固定的经营税——"
    merchant_guild "数目是目前贸易税收的两倍。"
    merchant_guild "此外，商会承担道路维护和商队安全的全部费用。"

    merchant_guild "算一笔账：您不需要花一分钱维护商路，还能拿到双倍的钱。"
    merchant_guild "怎么看都是稳赚不赔的买卖。"

    hide merchant_guild_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "听起来确实诱人。但——"
    aldric "独家经营意味着垄断。垄断意味着他们可以随意定价。"
    aldric "长远来看，吃亏的是普通百姓。"

    hide aldric_img with dissolve

    show elena_img at right with dissolve

    elena "我在市场上打听过了。商会控制的地方，物价普遍比自由市场高出三到四成。"
    elena "克劳斯许诺的那些钱，最终还是从百姓口袋里掏出来的。"

    hide elena_img with dissolve

    $ hide_all_chars("merchant_guild_img")
    show merchant_guild_img at left with dissolve
    merchant_guild "女士的说法有些偏颇。商会带来的是秩序和效率。"
    merchant_guild "没有商会的管理，散兵游勇般的小商贩只会让市场陷入混乱。"

    "你在心里盘算着各方的利弊。"

    menu:
        "这是关于经济命脉的抉择。"

        "授予垄断权——真金白银才是硬道理":
            jump gov_merchant_monopoly

        "有限合作——设立监管，允许商会经营但限制价格":
            jump gov_merchant_regulated

        "拒绝并推行自由贸易——市场属于所有人":
            jump gov_merchant_reject

label gov_merchant_monopoly:
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "商会的提案……我接受了。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "领主大人，您确定？"

    hide aldric_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我们现在需要钱。有了钱，才能建设，才能养兵，才能应对未来的挑战。"

    hide aldric_img with dissolve

    $ hide_all_chars("merchant_guild_img")
    show merchant_guild_img at left with dissolve
    merchant_guild "英明的决断！领主大人，您不会后悔的。"
    merchant_guild "这份协议将为艾登堡带来前所未有的繁荣。"

    $ hide_all_chars()
    "克劳斯心满意足地离开了。他的脚步轻快——显然，这笔买卖的赢家是他。"

    "协议签署后，商会迅速接管了所有贸易通道。"
    "效率确实提高了——道路修好了，商队增多了，税收也如约翻倍。"

    "但三个月后，市场上的物价开始悄悄上涨。"
    "面粉贵了两成，布匹贵了三成，铁器贵了四成。"

    hide merchant_guild_img
    $ hide_all_chars("farmer_rep_img")
    show farmer_rep_img at left with dissolve
    farmer_rep "领主大人，这日子……又开始难过了。"
    farmer_rep "东西越来越贵，可我们赚的又没多。"

    $ hide_all_chars()
    "金库是满了，但民心在流失。"
    "这就是垄断的代价——你卖了市场，买了金子，但贴进去的是百姓的信任。"

    $ change_stat("wealth", 25)
    $ change_stat("loyalty", -10)
    $ change_prosperity(-5)

    $ gov_merchant_outcome = "monopoly"
    $ governance_events_seen.append("merchant_negotiation")
    jump gov_merchant_end

label gov_merchant_regulated:
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "商会可以参与经营，但不是垄断。"
    player "我会设立一个贸易监管署，核定最高价格，防止哄抬物价。"
    player "商会享有优先经营权，但其他商人也可以自由贸易。"

    hide player_char_img
    $ hide_all_chars("merchant_guild_img")
    show merchant_guild_img at left with dissolve
    merchant_guild "这……领主大人，监管会大大降低商会的利润空间。"

    hide merchant_guild_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "利润是你们的，但市场是所有人的。"
    player "这是我的底线。"

    "克劳斯的手指无意识地转着那枚金戒指，转了一圈又一圈。"

    hide player_char_img
    $ hide_all_chars("merchant_guild_img")
    show merchant_guild_img at left with dissolve
    merchant_guild "……好吧。商会接受这个方案。"
    merchant_guild "不过我希望领主大人记住——商人也是这个领地的一份子。"
    merchant_guild "善待我们，对大家都好。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "这是平衡之策。不完美，但可能是最好的选择。"

    hide aldric_img with dissolve

    $ hide_all_chars()
    "监管贸易推行后，市场保持了相对的活力。"
    "物价稳定，商人们虽有怨言但尚能接受。"
    "普通百姓几乎感受不到什么变化——这或许就是最好的治理：润物细无声。"

    $ change_stat("wealth", 12)
    $ change_stat("reputation", 5)
    $ change_prosperity(5)

    $ gov_merchant_outcome = "regulated"
    $ governance_events_seen.append("merchant_negotiation")
    jump gov_merchant_end

label gov_merchant_reject:
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "我拒绝。"

    hide player_char_img
    $ hide_all_chars("merchant_guild_img")
    show merchant_guild_img at left with dissolve
    merchant_guild "领主大人——"

    hide merchant_guild_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "贸易通道是公共资源，不能成为任何人的私产。"
    player "从今天起，我将推行自由贸易政策。任何人都可以在艾登堡做买卖。"
    player "商会可以参与竞争，但不享有任何特权。"

    "克劳斯的脸色变了。那种变化很微妙——像一潭深水下暗流涌动。"

    hide player_char_img
    $ hide_all_chars("merchant_guild_img")
    show merchant_guild_img at left with dissolve
    merchant_guild "领主大人，我尊重您的决定。"
    merchant_guild "但我必须提醒您——商会控制着从南方到北方的整条供应链。"
    merchant_guild "如果我们决定不再经过艾登堡……"
    merchant_guild "您想想，那会是什么后果？"

    hide merchant_guild_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "那就是你们自己的损失。路不止一条，走你们这条的也不止你们一家。"

    $ hide_all_chars()
    "克劳斯微微一躬身，转身离开了。他没有再说话。"
    "但那个背影传达的信息很明确——这事没完。"

    hide player_char_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "您得罪了一个很有势力的人。"
    aldric "但……自由贸易确实更有利于百姓。"

    hide aldric_img with dissolve

    $ hide_all_chars()
    "自由贸易政策推行后，小商贩们如雨后春笋般涌现。"
    "市场比以前更热闹了，竞争让物价下降了一些。"
    "但商会果然开始搞小动作——部分供应链被切断，某些商品一时断了货。"

    $ change_stat("wealth", -3)
    $ change_stat("loyalty", 10)
    $ change_stat("reputation", 5)
    $ change_prosperity(5)

    "短期内财富略有损耗。但民心所向，自由贸易为长远发展奠定了基础。"

    $ gov_merchant_outcome = "reject"
    $ governance_events_seen.append("merchant_negotiation")
    jump gov_merchant_end

label gov_merchant_end:
    scene bg study with dissolve

    "经济——这个看似枯燥的话题，实际上比任何剑术都更致命。"
    "谁控制了贸易，谁就控制了人心。"
    "而控制人心的人……才是真正的王者。"

    return

################################################################################
## 10. Part 7: 治理报告 (gov_report)
################################################################################

label gov_report:
    scene bg study with dissolve
    play music "audio/music/castle_calm.ogg" fadeout 1.0 fadein 1.0 if_changed

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "领主大人，这是本季度的治理报告。"
    aldric "请您过目。"

    "奥尔德里克展开一卷写满数字和图表的羊皮纸。"

    python:
        _pros_bar = get_governance_bar(governance_prosperity)
        _health_bar = get_governance_bar(governance_health)
        _edu_bar = get_governance_bar(governance_education)
        _infra_bar = get_governance_bar(governance_infrastructure)
        _pros_desc = get_prosperity_desc()
        _health_desc = get_health_desc()

    aldric "首先是繁荣度——"
    aldric "民生状况：[_pros_desc]"
    aldric "[_pros_bar]"

    aldric "公共健康——"
    aldric "百姓体质：[_health_desc]"
    aldric "[_health_bar]"

    aldric "教育水平——"
    aldric "[_edu_bar]"

    aldric "基础设施——"
    aldric "[_infra_bar]"

    # 繁荣度评价
    if governance_prosperity >= 80:
        aldric "繁荣度令人瞩目。百姓安居乐业，市场繁荣兴旺。"
        aldric "艾登堡正在成为周边地区的典范。继续保持这个势头！"
    elif governance_prosperity >= 60:
        aldric "繁荣度尚可。百姓的生活在改善，但还有提升空间。"
        aldric "建议继续投资基础设施和民生工程。"
    elif governance_prosperity >= 40:
        aldric "繁荣度平平。百姓能勉强度日，但谈不上富足。"
        aldric "需要更积极的政策来刺激经济发展。"
    elif governance_prosperity >= 20:
        aldric "繁荣度堪忧。许多家庭挣扎在温饱线上。"
        aldric "如果不尽快改善，恐怕会出现社会动荡。"
    else:
        aldric "繁荣度……触目惊心。百姓已经到了绝望的边缘。"
        aldric "必须立即采取紧急措施，否则后果不堪设想。"

    # 健康评价
    if governance_health >= 70:
        aldric "百姓的健康状况良好。这要归功于我们在卫生方面的投入。"
    elif governance_health >= 40:
        aldric "健康状况一般。疾病时有发生，但尚在控制范围内。"
    else:
        aldric "健康状况令人担忧。疾病频发，百姓体质虚弱。"
        aldric "强烈建议尽快建立医疗设施。"

    # 教育评价
    if governance_education >= 50:
        aldric "教育方面取得了显著进展。识字率在提升，百姓的素养也在提高。"
        aldric "这对长远发展至关重要。"
    elif governance_education >= 20:
        aldric "教育刚刚起步，但已经能看到变化。"
        aldric "更多的投入会带来更大的回报。"
    elif governance_education > 0:
        aldric "教育水平偏低。大部分百姓不识字，容易被谣言蛊惑。"
    else:
        aldric "目前没有任何教育设施。这是一个需要填补的空白。"

    # 基础设施评价
    if governance_infrastructure >= 70:
        aldric "基础设施建设良好。道路畅通，城防坚固，粮仓充实。"
    elif governance_infrastructure >= 40:
        aldric "基础设施尚可。基本的需求能满足，但有改进余地。"
    else:
        aldric "基础设施薄弱。道路破损，城防不足，需要大力投入。"

    # 税收政策评价
    if governance_tax_policy == "progressive":
        aldric "税收政策方面——累进税制运行顺利。"
        aldric "农民的负担减轻了，虽然贵族有些不满，但整体向好。"
    elif governance_tax_policy == "flat":
        aldric "统一税制维持着基本的公平，但缺乏灵活性。"
    elif governance_tax_policy == "trade":
        aldric "商贸税制带来了可观的收入，但需要警惕商人的反弹。"
    else:
        aldric "税收制度尚未改革。旧制度的弊端日益显现。"
        aldric "建议尽快进行税务改革。"

    # 建设评价
    python:
        _buildings = []
        if built_school:
            _buildings.append("学堂")
        if built_clinic:
            _buildings.append("诊所")
        if built_granary:
            _buildings.append("粮仓")
        if built_watchtower:
            _buildings.append("望楼")
        _building_count = len(_buildings)

    if _building_count >= 3:
        aldric "建设方面成就斐然，已建成[_building_count]项工程。"
        aldric "这些设施正在深刻地改变着艾登堡。"
    elif _building_count >= 1:
        python:
            _built_str = "、".join(_buildings)
        aldric "已建成：[_built_str]。"
        aldric "每一项建设都在发挥着作用。建议在条件允许时继续投入。"
    else:
        aldric "目前尚未启动任何建设项目。"
        aldric "领主大人，基础建设是发展的根基。不可忽视啊。"

    # 综合建议
    aldric "总结来说——"

    python:
        _total_score = governance_prosperity + governance_health + governance_education + governance_infrastructure
        _avg_score = _total_score // 4

    if _avg_score >= 70:
        aldric "艾登堡的治理水平在同级别的领地中堪称翘楚。"
        aldric "您正在成为一位令人敬仰的领主。但不可掉以轻心——"
        aldric "越是繁荣之时，越容易生出隐患。"
    elif _avg_score >= 50:
        aldric "治理水平中等偏上。您做得不错，但还有很大的进步空间。"
        aldric "专注于最薄弱的环节，往往能事半功倍。"
    elif _avg_score >= 30:
        aldric "坦白说……情况不太乐观。"
        aldric "多个领域都需要改善。建议集中精力解决最紧迫的问题。"
    else:
        aldric "领主大人……恕我直言，如果再这样下去……"
        aldric "百姓可能会失去对您的信任。甚至……可能出现更糟的情况。"
        aldric "我们需要立即行动。"

    hide aldric_img with dissolve

    $ hide_all_chars()
    "你合上了报告，陷入沉思。"
    "数字冰冷无情——它们不会说谎，也不会安慰你。"
    "但正因如此，它们比任何谄媚的话语都更有价值。"

    "治国如烹小鲜——每一步都要审慎，每一刻都要清醒。"

    return

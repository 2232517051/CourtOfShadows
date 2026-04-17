## ============================================================
## 新随机事件集 - New Random Events
## random_events_new.rpy
## 9个独立随机事件：流浪诗人、瘟疫医生、算命婆、走私商人、
## 古地图、鬼故事之夜、孤儿的请求、决斗挑战、丰收或歉收
## ============================================================

## ── 事件追踪变量 ──
default re_wanderer_met = False
default re_plague_doctor_met = False
default re_fortune_told = False
default re_smuggler_met = False
default re_old_map_found = False
default re_ghost_story_heard = False
default re_orphan_met = False
default re_duel_met = False
default re_harvest_done = False

## ============================================================
## 事件 1: 流浪诗人 (The Wandering Poet)
## ============================================================

label re_wandering_poet:
    if re_wanderer_met:
        return

    scene bg castle_exterior with dissolve

    "暮色四合之际，城门守卫来报，说有一个衣着破旧却神采飞扬的男人，自称是游历四方的诗人，请求进入城堡借宿一晚。"

    "守卫犹豫不决——此人虽看上去无害，但这年头，谁也说不准一个陌生人肚子里装着什么心思。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "大人，那个诗人在城门口弹着琴唱歌，把半个城的人都引来了。"

    aldric "他唱的是……关于王国北方战事的歌谣。歌词里提到了一些……我们尚未听闻的消息。"

    "你来到城墙上，俯瞰城门。果然，一个瘦高的男人正坐在石阶上，手指灵活地拨弄着一把破旧的鲁特琴。"

    "他的歌声浑厚悠远，带着一种走过千山万水的沧桑感。围观的百姓越来越多，有人鼓掌，有人落泪。"

    "歌声隐约传来——"

    "{i}「……北风呼啸过焦土，白骨堆里长新芽。谁家少年提长枪，血染征袍不还家……」{/i}"

    "这个诗人显然走过很多地方，见过很多事。他可能是个无害的吟游者，也可能是某些势力的眼线。"

    menu:
        "你决定如何处置这位流浪诗人？"

        "请他进城，聆听他的歌与远方的消息":
            jump re_wandering_poet_listen

        "雇佣他作为行走各地的密探":
            jump re_wandering_poet_spy

        "赠他食物和路费，礼送出境":
            jump re_wandering_poet_send

label re_wandering_poet_listen:

    scene bg great_hall with dissolve

    "你请诗人进入大厅，命人为他备上热汤和面包。他狼吞虎咽地吃完，擦了擦嘴，郑重地向你行了一礼。"

    "「多谢领主大人的慷慨。在下名叫加文，以歌为生，以路为家。」"

    "「您想听什么？英雄的史诗？亡国的哀歌？还是……」他身体微微前倾，压低了嗓音，「{b}各地的秘闻？{/b}」"

    "你选择了后者。加文清了清嗓子，压低了声音。"

    "「我从南方来。哈根男爵的领地，最近频频调动兵马。他对外声称是剿匪，但据我所知，那些'匪'都是他自己花钱雇的。」"

    "「他在演戏给王后看，想证明自己是个值得倚重的人。」"

    "这个消息让你心中一凛。哈根男爵的野心，比你想象的更大。"

    "加文又说：「还有一件事——东部边境的商路上出现了一批来历不明的雇佣兵。他们不抢劫，但会拦住过路人打听各地领主的情况。」"

    "「有人说他们是王后的密探，也有人说他们来自更远的地方。」"

    "你将这些情报一一记在心中。一个流浪诗人的消息未必全然可信，不过窥探外界的窗户已经打开了。"

    $ change_stat("intrigue", 5)
    $ change_stat("reputation", 3)
    $ re_wanderer_met = True

    "加文在城堡住了一夜，第二天清晨便告辞离去。临走前，他在城门口唱了一首赞美艾登堡的歌——你的名声，将随着他的脚步传播到更远的地方。"

    return

label re_wandering_poet_spy:

    scene bg study with dissolve

    "你将诗人单独带到书房，屏退左右。"

    "「你走过很多地方，见过很多人。」你开门见山地说，「我需要一双在外行走的眼睛。」"

    "诗人挑了挑眉，似乎并不意外。他放下琴，正色道："

    "「领主大人果然目光如炬。在下确实不只是个唱歌的——要在这乱世活下来，光靠嗓子可不够。」"

    "「条件呢？」他问。"

    "「每月十枚银币，外加一枚为特别消息支付的金币。你继续四处游历，但每到一个重要的地方，就把见闻写成暗语送回来。」"

    "加文沉思片刻，伸出手来。「成交。不过有一个条件——如果我被抓了，你得设法捞我出来。」"

    "你握住他的手。「一言为定。」"

    $ change_stat("intrigue", 8)
    $ change_stat("wealth", -3)
    $ re_wanderer_met = True

    "从这天起，你的情报网多了一条无人注意的暗线——一个走遍天下的吟游诗人。"

    return

label re_wandering_poet_send:

    "你命人准备了一篮食物和几枚铜币，派侍从送到城门口。"

    "「告诉他，艾登堡感谢他的歌声，但我们不留外人过夜。祝他一路平安。」"

    hide aldric_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "大人英明。这年头，陌生人还是少接触为好。"

    "诗人收下食物，冲你举了举手中的干粮算是道谢，转身走向暮色中的远方。"

    "山道上很快空无一人。风把他留下的脚印一点点抹平。那些远方的消息、那些未知的故事——像是从未来过一样。"

    "但你的百姓记住了你的善意。一个连流浪者都愿意施舍食物的领主，不会太差。"

    hide captain_img with dissolve

    $ change_stat("loyalty", 5)
    $ change_stat("reputation", 3)
    $ re_wanderer_met = True

    return


## ============================================================
## 事件 2: 瘟疫医生 (The Plague Doctor)
## ============================================================

label re_plague_doctor:
    if re_plague_doctor_met:
        return

    scene bg marketplace with dissolve

    "市集上忽然起了骚动。人群纷纷退让，为一个黑衣人让出一条路来。"

    "那是一个戴着鸟嘴面具的高大身影，身披漆黑的长袍，手持一根雕刻着蛇纹的手杖。他的每一步都带着一种不属于此地的阴沉气息。"

    "——瘟疫医生。"

    "百姓们低声议论着，既恐惧又好奇。有人说他是从疫区逃来的江湖郎中，也有人说他是被教廷驱逐的异端。"

    "他径直走到城堡大门前，摘下面具——露出一张苍白消瘦、却目光锐利的面孔。"

    "「在下维克多，行医三十年。听闻此地最近有疫病苗头，特来毛遂自荐。」"

    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve

    bishop "大人，此人身上的气息……令人不安。他那鸟嘴面具里塞的草药，据说是用来驱赶瘴气的，但谁知道里面有没有异端的邪物？"

    bishop "教会的立场是：{b}正统的医术来自神的恩典{/b}，而非这种……来路不明的旁门左道。"

    hide bishop_img with dissolve

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "话是这么说，但城外的几个村子确实有人开始发烧和咳血了。如果真的爆发瘟疫……"

    captain "我们没有足够的医师。"

    hide captain_img with dissolve

    "维克多站在城门前，不卑不亢地等待着你的决定。"

    menu:
        "你如何处置这位瘟疫医生？"

        "聘用他，让他立刻开始诊治病患":
            jump re_plague_doctor_hire

        "婉言谢绝，请他离开":
            jump re_plague_doctor_refuse

        "先在囚犯身上试验他的医术":
            jump re_plague_doctor_test

label re_plague_doctor_hire:

    scene bg village with dissolve

    "你不顾主教的反对，下令让维克多进入领地行医。"

    "他的手段确实……令人难以直视。放血、水蛭、用硫磺和醋熏蒸病房、给患者灌下散发恶臭的黑色药剂——每一样都让围观者退避三舍。"

    "但不可否认的是——他的方法有效。三天之内，最严重的几个病人退了烧；一周之后，村子里再没有新增病例。"

    "百姓们对他的态度从恐惧变成了敬畏。有人开始称他为「黑衣圣人」，这让主教非常不满。"

    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve

    bishop "大人，您看到了吗？百姓们在向一个异端膜拜！长此以往，教会的权威何在？"

    hide bishop_img with dissolve

    "你安抚了主教，同时允许维克多留下来担任领地医师。疫病被扼杀在了萌芽中，但教会与民间信仰之间的裂痕，似乎又深了一些。"

    $ change_stat("loyalty", 5)
    $ change_stat("faith", -5)
    $ change_stat("reputation", 5)
    $ re_plague_doctor_met = True

    return

label re_plague_doctor_refuse:

    scene bg castle_exterior with dissolve

    "你客气但坚定地拒绝了维克多的提议。"

    "「感谢你的好意，但我们暂时不需要外来的医师。艾登堡有教会的祝福，足以应对一切。」"

    "维克多重新戴上了他的鸟嘴面具。面具后传出闷闷的声音："

    "「领主大人，瘟疫不会因为你的拒绝而止步。当它真正来临的时候……希望祈祷比药剂更管用。」"

    "他转身离去，黑色的背影渐渐消融在暮色之中。"

    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve

    bishop "大人做了正确的选择。我会加派修士前往各村祈福驱疫。"

    hide bishop_img with dissolve

    "你望着维克多消失的方向，心中微微不安。但愿主教是对的。"

    $ change_stat("faith", 5)
    $ change_stat("reputation", -3)
    $ re_plague_doctor_met = True

    return

label re_plague_doctor_test:

    scene bg castle_exterior with dissolve

    "你目光幽深地看着维克多，缓缓开口："

    "「你的医术，我需要亲眼验证。地牢里有几个判了死刑的囚犯，其中两个已经感染了热病。」"

    "「如果你能治好他们，我就信你。」"

    "维克多的手指缩了一下，随即恢复如常——那个瞬间的犹豫，是厌恶？理解？还是同类之间的某种默契？"

    "「……可以。」他最终说道。"

    "三天后，你来到地牢。两个原本奄奄一息的囚犯已经能够站起来了，虽然面色仍然苍白，但热病的症状已经完全消退。"

    "而另一间牢房里，维克多正在记录着什么。他的笔记本上画满了密密麻麻的人体图和药方。"

    "「满意了吗，领主大人？」他头也不抬地问。"

    "你没有回答。你在思考一个更深层的问题——一个愿意在囚犯身上试药的医生，和一个愿意用囚犯来试药的领主，本质上有什么区别？"

    "你最终聘用了维克多，但为此付出的代价不仅仅是金钱。消息传开后，有人说你冷酷无情，也有人说你务实果断。"

    $ change_stat("intrigue", 8)
    $ change_stat("loyalty", -3)
    $ change_stat("reputation", -3)
    $ re_plague_doctor_met = True

    "不管怎样，你有了一个能力出众的医师——以及一个了解你阴暗面的人。"

    return


## ============================================================
## 事件 3: 算命婆 (The Fortune Teller)
## ============================================================

label re_fortune_teller:
    if re_fortune_told:
        return

    scene bg marketplace with dissolve

    "你微服走访市集的时候，注意到一个不寻常的角落。"

    "在两个摊位之间的阴影里，一个佝偻的老妇人坐在一张破旧的矮桌后面。桌上铺着一块绣满星辰图案的黑布，上面散落着骨片、水晶和干枯的花瓣。"

    "她的头发灰白如乱草，面容沟壑纵横，但那双眼睛——浑浊中透着一种令人不安的清明。"

    "当你从她面前经过时，她忽然开口了。"

    "「年轻的领主……」"

    "你停下脚步。你今天穿的是便装，没有任何领主的标识。她怎么知道的？"

    "老妇人嘿嘿笑了笑，露出所剩无几的牙齿。"

    "「老身看的不是衣裳，是命格。你身上有龙气缠绕，有血光笼罩……」"

    "她忽然抬起手，指向东方。"

    "「{b}王座之上将溅血，东方将燃起烈火。{/b}」"

    "「这是天机。老身不该说的——但你是个好人，老身不忍心看你蒙在鼓里。」"

    "周围的行人似乎都没有注意到这一幕。嘈杂的市集声仿佛被一堵无形的墙隔绝在外。"

    menu:
        "你如何回应这个老妇人的预言？"

        "相信她的话，追问更多细节":
            jump re_fortune_teller_believe

        "嗤之以鼻，不过是江湖骗术":
            jump re_fortune_teller_dismiss

        "问她关于父亲的死":
            jump re_fortune_teller_father

label re_fortune_teller_believe:

    "你在她面前坐下，认真地看着她的眼睛。"

    "「告诉我更多。」"

    "老妇人伸出枯槁的手，抓住你的手腕。她的手指冰冷如蛇，但你没有退缩。"

    "她闭上眼睛，嘴里念念有词。过了许久，她睁开眼，目光比方才更加凝重。"

    "「三个月之内，王都将有大变。有人想坐上不属于他的椅子，有人想点燃不该烧的火。」"

    "「你会被卷入其中——不是因为你想，而是因为你躲不掉。」"

    "「当群鸦飞过城堡上空的时候……{b}不要相信送花的人{/b}。」"

    "她松开你的手，疲惫地靠回椅背上，仿佛刚才的占卜耗尽了她所有的力气。"

    "「走吧，年轻人。该来的终究会来。但至少……你不再是蒙着眼走进暴风雨的人了。」"

    "你起身离开，心中翻涌着复杂的情绪。这些话也许只是老妇人的胡言乱语，但如果——如果她说的是真的呢？"

    "「不要相信送花的人。」这句话像一根刺，深深扎进你的脑海。"

    $ change_stat("intrigue", 5)
    $ change_stat("faith", 3)
    $ re_fortune_told = True

    return

label re_fortune_teller_dismiss:

    "你冷笑一声。「王座溅血，东方烈火？这种话每个赶集日都能听到一打。」"

    "老妇人不怒反笑。「年轻人不信老人言，这也是命数。」"

    "「不过……」她的声音忽然变得幽远，「等你想起老身的话时，但愿一切还来得及。」"

    "你转身离去，把这个小插曲抛在了脑后。市集依旧喧嚣，太阳依旧明亮，一切都是平凡的一天。"

    "只是当你回头看时——那个角落空空如也。桌子、黑布、老妇人，全都不见了。"

    "仿佛从来不曾存在过。"

    "你愣了一瞬，然后摇了摇头。一定是看错了。"

    $ change_stat("reputation", 2)
    $ re_fortune_told = False

    "……对吧？"

    return

label re_fortune_teller_father:

    "你用一种连自己都觉得陌生的声音问道："

    "「你能看到过去吗？」"

    "老妇人的表情变了。她慢慢收起脸上的嬉笑，换上了一种近乎怜悯的神色。"

    "「你想问的，是你父亲的事。」"

    "不是疑问，是陈述。你的心猛地一紧。"

    "「他的死……不是意外。」老妇人的声音低得像风中的叹息，「也不是病。」"

    "「{b}他被最信任的人背叛了。{/b}」"

    "「那个人……曾经与你父亲同吃同住，同饮一壶酒，同披一件甲。你父亲把后背交给他——而他在那后背上插了一把刀。」"

    "你感觉血液在一瞬间凝固了。"

    "「那个人……是谁？」"

    "老妇人摇了摇头。「这个答案，不在老身的骨片里。它在你身边——在你每天都会见到的人之中。」"

    "「去翻你父亲的旧物。他留了线索……他知道有人要害他，但他来不及说出口。」"

    "她疲惫地闭上眼睛。「走吧。真相会让你痛苦，但谎言会让你送命。」"

    "你站起来的时候，双腿微微发软。父亲……被最信任的人背叛？"

    "那个人，现在是否还在你身边？"

    $ change_stat("intrigue", 8)
    $ change_stat("faith", 5)
    $ change_stat("loyalty", -3)
    $ re_fortune_told = True

    "你带着一肚子疑问和寒意，离开了市集。从今天起，你看每一个人的目光，都将不再一样。"

    return


## ============================================================
## 事件 4: 走私商人 (The Smuggler)
## ============================================================

label re_smuggler:
    if re_smuggler_met:
        return

    scene bg marketplace with dissolve

    "深夜。一个神秘的商人悄悄找到你的侍从，声称有一批「极为划算」的货物想要出售。"

    "侍从不敢擅自做主，将消息报了上来。你决定亲自去看看。"

    scene bg forest_path with dissolve

    "在城外林间的一处隐蔽空地上，三辆蒙着黑布的马车静静停着。一个戴着兜帽的男人迎了上来。"

    "「领主大人亲临，小人荣幸之至。」他压低声音，掀开了马车上的黑布。"

    "车上堆满了上等的丝绸、香料、葡萄酒和精钢武器——每一样都价值不菲。"

    "「这些东西，市价的三成就卖给您。」"

    "你皱起眉头。「这么便宜？哪来的货？」"

    "商人犹豫了一下，然后诚实得令人意外："

    "「王后运往北方军营的补给车队……在途经黑森林的时候，被我的人截了一部分。」"

    "「现在这些东西是烫手山芋，我需要尽快脱手。您买到就是赚到——只要别声张就行。」"

    "你的心中迅速盘算着利弊。这些货物确实诱人，但它们的来源……如果被查出来，那可是截劫王室物资的重罪。"

    menu:
        "你如何处理这批走私货物？"

        "买下货物，充实领地储备":
            jump re_smuggler_buy

        "逮捕走私商人，上交货物":
            jump re_smuggler_arrest

        "不买货物，但收编此人为情报来源":
            jump re_smuggler_recruit

label re_smuggler_buy:

    "你思忖再三，最终点了头。"

    "「成交。但货物运进城的时候，走地下通道。我不想让任何人看到。」"

    "商人笑得像只老狐狸。「领主大人果然是做大事的人。」"

    "三辆马车的货物在天亮之前全部转移到了城堡的秘密仓库里。丝绸和香料可以慢慢出售，精钢武器正好补充军备的不足。"

    "一笔划算的买卖。但你知道，从你接下这批货物的那一刻起，你就和一个走私犯绑在了同一条绳子上。"

    $ change_stat("wealth", 10)
    $ change_stat("power", 3)
    $ change_stat("reputation", -5)
    $ re_smuggler_met = True

    "如果有一天东窗事发……你最好确保这个商人永远闭嘴。"

    return

label re_smuggler_arrest:

    scene bg castle_exterior with dissolve

    "你给出了一个暗号，埋伏在四周的侍卫立刻冲出，将走私商人和他的手下团团围住。"

    "商人脸色大变。「领主大人——您不讲规矩！」"

    "「规矩？」你冷冷地看着他，「截劫王室补给的人，跟我谈规矩？」"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "全部拿下！搜查马车，清点货物！"

    hide captain_img with dissolve

    "走私商人和他的同伙被投入地牢，货物被封存。你修书一封，将此事上报王都——截获走私物资、缉拿盗匪，这是一笔不小的功劳。"

    "几日后，王后的回信到了。信中对你的忠诚大加赞赏，并赏赐了一笔可观的奖金。"

    $ change_stat("reputation", 8)
    $ change_stat("loyalty", 3)
    $ change_stat("wealth", 3)
    $ re_smuggler_met = True

    "你做了正确的事。至少，在纸面上是这样。"

    return

label re_smuggler_recruit:

    "你没有买他的货，也没有叫人来抓他。你只是平静地说了一句话："

    "「你的货我不感兴趣。但你的消息——值多少钱？」"

    "商人愣住了。显然，他没想到会遇到这种谈判方式。"

    "「一个能在王后补给线上动手的人，一定对各条商路上的动向了如指掌。」你继续说道，「我需要的不是丝绸和香料——我需要情报。」"

    "「谁在运什么货，走哪条路，有没有异常的兵力调动……这些东西，比任何丝绸都值钱。」"

    "走私商人摘下兜帽，露出一张精明的、布满风霜的面孔。"

    "「领主大人，您是我这辈子见过的最危险的买家。」"

    "「……成交。」"

    $ change_stat("intrigue", 10)
    $ change_stat("wealth", -2)
    $ re_smuggler_met = True

    "从那天起，每隔半个月，就会有一封用暗语写成的信件，通过秘密渠道送到你的书房。"

    "走私商人的情报网络覆盖了半个王国的商路——这是用金子也买不到的资源。"

    return


## ============================================================
## 事件 5: 古地图 (The Old Map)
## ============================================================

label re_old_map:
    if re_old_map_found:
        return

    scene bg castle_exterior with dissolve

    "城堡西墙年久失修，你下令进行翻修。工匠们拆除一面砖墙时，发现了一个被封死的暗格。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "大人，您最好来看看这个。"

    hide captain_img with dissolve

    "你赶到现场，只见暗格中放着一个锈迹斑斑的铁盒。打开铁盒，里面是一张泛黄的羊皮纸地图，以及一封密封的书信。"

    "地图上画的是城堡的地下结构——但比你所知的要复杂得多。在城堡的东翼地基下方，赫然标注着一条{b}通往城外森林的秘密通道{/b}。"

    "通道的入口标记在酒窖深处的某面墙壁后面，出口则在城堡以北约一里地的一棵老橡树下。"

    "那封书信已经被岁月侵蚀得残缺不全，但你依稀辨认出开头几行字——"

    "「……吾儿，若你发现此图，说明城堡已经到了最危急的时刻。这条密道是你曾祖父留下的退路。密道尽头有……」"

    "后面的字迹模糊难辨。但「密道尽头有」后面的几个字隐约像是「先祖之物」。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "大人，这张地图看起来有上百年的历史了。如果这条密道真的存在……它可以是逃生通道，也可以是敌人入侵的路线。"

    hide aldric_img with dissolve

    menu:
        "你如何处理这张古地图和秘密通道？"

        "立刻组织人手探索密道":
            jump re_old_map_explore

        "封死入口，确保安全":
            jump re_old_map_seal

        "只告诉最信任的几个人":
            jump re_old_map_secret

label re_old_map_explore:

    scene bg castle_exterior with dissolve

    "你按捺不住好奇心，带着雷恩和几名精锐侍卫，提着火把来到酒窖深处。"

    "按照地图的标注，你们找到了那面看似普通的石墙。仔细检查后发现，一块石砖可以向内推动——一个隐藏的机关。"

    "沉重的石门缓缓打开，露出一条黑暗的通道。空气中弥漫着数百年的陈腐气息。"

    "你们小心翼翼地前进。通道比预想的宽敞，可以并排走两个人。两壁上偶尔出现古旧的火把架和已经锈穿的铁环。"

    "走了约莫半炷香的时间，通道分出了一个岔路。主道继续通往森林方向，而岔路通向一个小型的地下室。"

    "地下室里放着两个大箱子和一副铠甲架。箱子打开后，里面是一些古旧的金币、一把保存完好的宝剑，以及一卷密封在蜡管中的羊皮纸。"

    "羊皮纸上记载着你家族早年的秘史——原来，你的曾祖父并非仅仅是一个小领主，而是曾在旧王朝覆灭时扮演过关键角色。"

    $ change_stat("wealth", 8)
    $ change_stat("power", 5)
    $ change_stat("intrigue", 5)
    $ re_old_map_found = True
    $ secret_passage_found = True
    $ aldric_knows_passage = True

    "你带着宝物和秘密返回地面，心中激荡不已。这条密道不仅是退路，更是一段被遗忘的历史。"

    "而那把古剑……也许有一天会派上用场。"

    return

label re_old_map_seal:

    scene bg castle_exterior with dissolve

    "你沉思片刻，做出了谨慎的决定。"

    "「封死它。用三层砖墙加固，再在外面砌上新的石面。不留任何痕迹。」"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "明白。我亲自监督施工，不让工匠知道里面是什么。"

    hide captain_img with dissolve

    "密道入口被牢牢封死了。你将地图和书信锁进书房的保险箱，以防将来需要。"

    "这意味着你放弃了可能存在的宝藏和退路，但也确保了没有人能通过这条通道偷偷潜入城堡。"

    "安全，永远是第一位的。"

    $ change_stat("power", 5)
    $ change_stat("loyalty", 3)
    $ re_old_map_found = True

    return

label re_old_map_secret:

    scene bg study with dissolve

    "你将地图仔细收好，只把这件事告诉了三个人——奥尔德里克、雷恩队长，以及你自己。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "大人英明。这条密道既是筹码也是隐患。知道的人越少越好。"

    hide aldric_img with dissolve

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "我会安排两名最可靠的侍卫，暗中监视酒窖那面墙壁。任何人靠近都会被记录。"

    hide captain_img with dissolve

    "你点了点头。密道暂时不探索，但也不封死——它是一张底牌，等到最关键的时刻再翻开。"

    $ change_stat("intrigue", 8)
    $ change_stat("loyalty", 3)
    $ re_old_map_found = True
    $ secret_passage_found = True
    $ aldric_knows_passage = True

    "三个人，一个秘密。在这座城堡里，这可能是保密效果最好的数字了。"

    return


## ============================================================
## 事件 6: 鬼故事之夜 (Ghost Story Night)
## ============================================================

label re_ghost_night:
    if re_ghost_story_heard:
        return

    scene bg castle_exterior with dissolve

    "一场猛烈的暴风雨在毫无征兆的情况下袭击了艾登堡。狂风呼啸着掠过城垛，暴雨如倾盆倒下。"

    "随着一道震耳欲聋的雷鸣，城堡里所有的蜡烛几乎同时熄灭了。"

    "黑暗中，侍从们慌乱地四处寻找火折子，走廊里传来叮叮咣咣的碰撞声和惊叫声。"

    "然后——守卫的报告来了。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "大人……北塔的守卫说他们看到了……一个白色的影子。"

    captain "在闪电的光芒中，它站在走廊尽头，然后一转眼就消失了。"

    captain "三个守卫都看到了。他们发誓不是在开玩笑。"

    hide captain_img with dissolve

    "很快，更多的报告涌来。有人看到白影飘过大厅，有人听到墙壁里传来低语，有人在地窖里发现了不属于任何人的脚印。"

    "城堡里弥漫着一种不安的气氛。年纪大的仆人开始念叨起古老的传说——据说艾登堡建在一座更古老的堡垒遗址上，那里曾经发生过一场惨烈的屠杀。"

    "「是冤魂回来索命了！」一个老仆哆嗦着说。"

    "你站在漆黑的大厅中央，听着四面八方传来的恐慌低语。蜡烛终于重新点燃，但每个人脸上跳动的火光只让气氛更加诡异。"

    menu:
        "你决定怎么做？"

        "提起火把，亲自前往北塔调查":
            jump re_ghost_night_investigate

        "利用「鬼魂」来鼓舞士气":
            jump re_ghost_night_morale

        "前往礼拜堂祈祷驱邪":
            jump re_ghost_night_pray

label re_ghost_night_investigate:

    scene bg castle_exterior with dissolve

    "你从侍卫手中接过火把，带上雷恩和两名侍卫，大步走向北塔。"

    "走廊里安静得不正常。你们的脚步声在石壁间回荡，像是有什么东西在模仿你们的步伐。"

    "到达北塔的走廊时，你看到了——地板上有一层薄薄的白色粉末。"

    "你蹲下来，用手指沾了一点放到鼻下。石灰粉。"

    "「不是鬼。」你站起身，声音冷硬如铁。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "大人的意思是……"

    "「有人在城堡里制造恐慌。白色粉末洒在衣服上，在闪电中看起来就像是发光的白影。」"

    hide captain_img with dissolve

    "你沿着粉末的痕迹追踪，最终在北塔的一间废弃储藏室里，找到了一个瑟瑟发抖的人——穿着仆人的衣服，身上还残留着白色的粉末。"

    "审问之后，真相浮出水面：此人是哈根男爵安插在城堡中的眼线。他趁暴风雨之夜制造鬼魂恐慌，目的是在混乱中溜进你的书房窃取文件。"

    "你将他送入地牢，同时在全城堡进行了一次彻底的人员清查。"

    $ change_stat("power", 8)
    $ change_stat("intrigue", 5)
    $ change_stat("reputation", 5)
    $ re_ghost_story_heard = True

    "这一夜，你用行动证明了一件事——在这座城堡里，没有鬼比活人更可怕。"

    return

label re_ghost_night_morale:

    scene bg great_hall with dissolve

    "你没有去追查什么「鬼魂」。相反，你走到大厅中央，让所有人安静下来。"

    "「都给我听好了！」你的声音在黑暗中回荡，「这座城堡已经屹立了三百年。在它的石壁之下，埋葬着无数忠勇的先辈。」"

    "「如果他们的亡魂真的还在——那不是诅咒，是{b}守护{/b}！」"

    "「连死去的人都站在我们这一边，活着的人还有什么好怕的？」"

    "大厅里安静了一瞬，然后——不知是谁带头鼓起了掌。很快，掌声变成了欢呼，欢呼变成了齐声高喊："

    "「艾登堡！艾登堡！」"

    "恐惧被热血取代，动摇被信念填满。你不知道那个白影到底是什么——也许是风吹动了白帘，也许真的是某些不安的灵魂。"

    "但无所谓了。今夜之后，这座城堡的每一个人都相信：连鬼魂都是他们的战友。"

    $ change_stat("loyalty", 10)
    $ change_stat("reputation", 5)
    $ re_ghost_story_heard = True

    "这个故事在民间流传开来，成为了艾登堡最著名的传说之一。"

    return

label re_ghost_night_pray:

    scene bg church with dissolve

    "你走进城堡的礼拜堂，点燃了祭坛前的每一根蜡烛。温暖的烛光驱散了黑暗，也驱散了一些恐惧。"

    $ hide_all_chars("bishop_img")
    show bishop_img at left with dissolve

    bishop "大人，您来了。在这样的夜晚，信仰是最好的盾牌。"

    "你和主教一起跪在祭坛前，诵读了一段古老的驱邪祈祷文。声音庄严肃穆，在空旷的礼拜堂中回荡。"

    "不知过了多久，暴风雨渐渐平息了。当你走出礼拜堂时，外面的走廊安静而祥和——再也没有人报告看到白影。"

    bishop "看，神的力量从不辜负虔诚的心。"

    hide bishop_img with dissolve

    "也许是巧合，也许是信仰的力量。但有一点是确定的——主教因为今晚的事对你更加信任了。而你的百姓也看到了一个敬畏神灵的领主。"

    $ change_stat("faith", 10)
    $ change_stat("loyalty", 3)
    $ change_stat("reputation", 3)
    $ re_ghost_story_heard = True

    "那个白影到底是什么？这个问题，也许永远没有答案。有些谜团，就让它留在风雨之夜吧。"

    return


## ============================================================
## 事件 7: 孤儿的请求 (The Orphan's Plea)
## ============================================================

label re_orphan:
    if re_orphan_met:
        return

    scene bg castle_exterior with dissolve

    "一个阴冷的清晨，城门守卫来报：城门外聚集了一群孩子。"

    "你登上城墙望去——约莫二十几个衣衫褴褛的孩子蜷缩在城门口，最大的不过十二三岁，最小的还在吃手指。"

    "他们的眼睛又大又空洞，像是见过了太多不属于他们年纪的东西。"

    "其中最大的孩子——一个面容坚毅、满脸污垢的女孩——跪在地上，双手高举着一块破布条。上面歪歪扭扭地写着："

    "「{b}求领主大人收留我们。我们的村子被烧了。爹娘都死了。{/b}」"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "大人……这些孩子很可能来自南方边境的冲突区。最近的战事波及了不少村庄。"

    aldric "但我必须提醒您——我们的粮仓并不充裕。收留他们意味着更多的支出和更重的负担。"

    hide aldric_img with dissolve

    "你看着城门下那些瘦弱的身影。有几个孩子已经冻得发抖，相互依偎着取暖。"

    menu:
        "你如何处置这些战争孤儿？"

        "打开城门，全部收留":
            jump re_orphan_shelter

        "为他们寻找村里的寄养家庭":
            jump re_orphan_foster

        "给些食物，但不能留":
            jump re_orphan_turn_away

label re_orphan_shelter:

    scene bg great_hall with dissolve

    "你下令打开城门。孩子们被领进了城堡的大厅——他们中的大多数还是第一次走进这么大的建筑，瞪大了眼睛东张西望。"

    "你命人烧了热水，让他们洗澡、换上干净的衣服、吃了一顿饱饭。那个带头的女孩吃着面包，眼泪无声地流了下来。"

    "「大人……谢谢您。」她的声音沙哑而倔强，「我们不白吃饭。我们什么活都能干。」"

    "你安排了城堡的空房间给他们住，并让管家制定了一套教育和劳动的方案——年纪大的学手艺，年纪小的上学堂。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "大人，这些孩子里有几个身手不错。如果加以训练，将来能成为忠心的侍卫。"

    hide captain_img with dissolve

    "消息传开后，百姓们对你的评价空前地高。在这个冷酷的世道里，一个愿意收留孤儿的领主，值得追随。"

    $ change_stat("loyalty", 10)
    $ change_stat("reputation", 8)
    $ change_stat("wealth", -3)
    $ re_orphan_met = True

    "粮仓的压力增大了一些。但看着那些孩子渐渐恢复笑容的脸庞，你觉得这笔账划得来。"

    return

label re_orphan_foster:

    scene bg village with dissolve

    "你召集了周边村庄的长老，说明情况，请求他们为这些孩子寻找寄养家庭。"

    "起初，村民们有些犹豫——多一张嘴就多一份开销。但你承诺，领主府会为每个收养孤儿的家庭提供补贴和减税。"

    "这个方案得到了大多数人的支持。几天之内，二十多个孩子被分散安置到了各个村庄的家庭里。"

    "那个带头的女孩被铁匠一家收养了。铁匠的妻子没有孩子，对她视如己出。"

    "你看着孩子们被各自的新家庭领走，心中感到一种温和的满足。这也许不是最轰轰烈烈的决定，但它是对的。"

    $ change_stat("loyalty", 5)
    $ change_stat("reputation", 5)
    $ change_stat("wealth", -3)
    $ re_orphan_met = True

    "善意，有时候不需要英雄壮举。一碗热粥、一间暖屋、一个愿意拉你一把的人——这就够了。"

    return

label re_orphan_turn_away:

    scene bg castle_exterior with dissolve

    "你闭上眼睛，做出了最难的决定。"

    "「给他们准备三天的干粮和毯子。」你的声音平静而坚定，「然后……送他们去王都。那里有教会的孤儿院，比我们更有能力照顾他们。」"

    "侍从们沉默地执行了命令。孩子们拿到食物时，脸上没有多少感激——他们已经习惯了被拒绝。"

    "那个带头的女孩接过干粮袋，抬头看了你一眼。她的目光平静得不像一个孩子。"

    "「我记住您了，领主大人。」她说，「谢谢您的面包。」"

    "这句话不知为何让你如芒在背。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "大人做了理性的选择。我们确实无力承担更多人口。"

    hide aldric_img with dissolve

    "你转身走回城堡，没有再回头。"

    $ change_stat("power", 3)
    $ change_stat("reputation", -8)
    $ change_stat("wealth", 2)
    $ re_orphan_met = True

    "理性的选择。你在心里重复了一遍这句话。但那个女孩的眼神，在之后的很多个夜晚，都会出现在你的梦里。"

    return


## ============================================================
## 事件 8: 决斗挑战 (The Duel Challenge)
## ============================================================

label re_duel_challenge:
    if re_duel_met:
        return

    scene bg castle_exterior with dissolve

    "午后时分，一个身披银色铠甲的骑士骑着高头大马来到城堡前。他的盾牌上绘着一只展翅的雄鹰——你不认识这个纹章。"

    "骑士摘下头盔，露出一张英俊而傲慢的面孔。他的声音洪亮如钟，传遍了整个城门广场。"

    "「我是银鹰骑士团的塞德里克！听闻艾登堡的新领主是个文弱书生，特来讨教一二！」"

    "「领主大人！我以骑士之名向您发起决斗——若您获胜，我的剑将永远为您效力。若您落败……」他笑了笑，「不过是输了面子而已。」"

    "广场上围观的百姓越来越多，议论纷纷。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "大人，银鹰骑士团是北方的自由骑士组织，实力不容小觑。这个塞德里克……看他的气势，绝非等闲之辈。"

    captain "不过，我怀疑他此行的真正目的不是决斗——而是考察。银鹰骑士团向来只投效他们认为值得的主君。"

    hide captain_img with dissolve

    "塞德里克仍然骑在马上，傲然等待着你的回应。阳光照在他的银色铠甲上，刺得人睁不开眼。"

    menu:
        "你如何回应这个决斗挑战？"

        "接受挑战，亲自上阵":
            jump re_duel_accept

        "以智慧而非蛮力回应":
            jump re_duel_decline_wisely

        "让雷恩队长代为出战":
            jump re_duel_proxy

label re_duel_accept:

    scene bg castle_exterior with dissolve

    "你走下台阶，接过侍从递来的剑和盾牌。广场上顿时安静下来——所有人都屏住了呼吸。"

    "塞德里克翻身下马，拔出一把装饰华丽的长剑。「有胆量。」他点了点头，「来吧。」"

    "铛！"

    "第一剑交锋，你就感受到了对方压倒性的力量。塞德里克的剑法凌厉精准，每一击都带着千锤百炼的底蕴。"

    "你被逼得连连后退，肩膀上挨了一剑——铠甲挡住了锋刃，但冲击力让你踉跄了两步。"

    "观众中有人发出了惊叫。"

    if power >= 40:
        jump re_duel_win
    else:
        jump re_duel_lose

label re_duel_win:

    "但你咬紧牙关，稳住了脚步。父亲生前教给你的剑术——在这一刻全部涌上了心头。"

    "你开始反击。不靠蛮力，靠的是对节奏的精准把控。你看到了塞德里克出剑时的一个微小破绽——左肩在大力劈砍后会有一瞬间的滞涩。"

    "你等了三个回合，终于等到了那个瞬间。一个突刺，剑尖停在了塞德里克的咽喉前。"

    "广场上爆发出震耳欲聋的欢呼。"

    "塞德里克低头看了看你的剑尖，然后——大笑出声。"

    "「好！好剑法！」他退后一步，单膝跪地，「我塞德里克以骑士之名起誓——银鹰骑士团，愿为艾登堡效力！」"

    $ change_stat("power", 10)
    $ change_stat("reputation", 8)
    $ re_duel_met = True

    "你赢了。不仅赢了一场决斗，还赢了一个强大的盟友。"

    return

label re_duel_lose:

    "差距太大了。不到二十个回合，你的剑就被挑飞了。你重重地摔倒在地，胸口传来一阵闷痛。"

    "塞德里克的剑尖停在你面前。整个广场鸦雀无声。"

    "但你没有求饶。你撑着地面站起来，拍了拍身上的土，直视塞德里克的眼睛。"

    "「再来。」"

    "塞德里克愣了一下。你徒手站在他面前，手臂在微微发抖，但目光毫无退缩。"

    "他收剑入鞘。"

    "「我见过很多人在我的剑下跪地求饶。」他的声音低沉了许多，「但像你这样站起来的……不多。」"

    "「你输了决斗，但没有输掉尊严。」他伸出手来，「塞德里克，银鹰骑士团。如果你需要朋友——我就在北方。」"

    $ change_stat("reputation", 8)
    $ change_stat("power", 3)
    $ re_duel_met = True

    "你没有赢得他的剑，但赢得了他的尊重。在这个世界上，有时候后者比前者更珍贵。"

    return

label re_duel_decline_wisely:

    scene bg great_hall with dissolve

    "你没有急于回应。你慢慢走下台阶，在塞德里克面前站定，然后——做了一件出乎所有人意料的事。"

    "你向他深深鞠了一躬。"

    "广场上一片哗然。一个领主向一个外来骑士鞠躬？"

    "「塞德里克爵士，」你从容地说，「您的武勇远近闻名，我自知不是对手。若我贸然应战，不过是拿自己的颜面给您当磨刀石——这对我们双方都是浪费。」"

    "「但如果您愿意赏光，今晚请在我的大厅中饮酒叙话。我虽无法在剑术上与您匹敌，但在棋盘上——也许能让您领教一二。」"

    "塞德里克愣了好几秒钟，然后放声大笑。"

    "「哈哈哈！有意思！比那些头铁上来送死的莽夫有意思多了！」"

    "那天晚上，你和塞德里克在火炉旁下了三盘棋。你赢了两盘，输了一盘。你们聊了整夜——战争、政治、理想、还有各自亏欠过的人。"

    "天亮时分，塞德里克拍了拍你的肩膀。「你是我见过最聪明的领主。银鹰骑士团不缺剑手——但缺一个值得辅佐的智者。」"

    $ change_stat("intrigue", 8)
    $ change_stat("reputation", 5)
    $ re_duel_met = True

    "有时候，放下剑比拿起剑更需要勇气。"

    return

label re_duel_proxy:

    scene bg castle_exterior with dissolve

    "你转头看向身边的雷恩。他微微点头——不需要多说，你们之间的默契已经足够。"

    "「塞德里克爵士，」你高声说道，「在我们这里，领主的剑就是他麾下将士的剑。代我出战的，是我最信任的人——雷恩队长。」"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "在下雷恩，艾登堡护卫队长。请指教。"

    hide captain_img with dissolve

    "塞德里克打量了雷恩一番，眼中掠过一丝赞赏。「好。」"

    "两人的决斗比你预想的更加精彩。雷恩的剑法质朴刚猛，没有花哨的技巧，每一剑都是战场上磨砺出来的杀招。"

    "而塞德里克则剑走偏锋，华丽而多变。两种截然不同的风格碰撞在一起，火花四溅。"

    "三十个回合后，两人同时收手。雷恩的肩膀被划开一道口子，而塞德里克的手腕也被蹭出了血。"

    "「平手。」塞德里克喘着气说，脸上却带着由衷的笑容，「你手下有这样的猛将，不愧是一方领主。」"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "承让了。"

    "雷恩沉默地行了一礼，但你注意到他收拳的时候攥得格外紧——不是紧张，是满意。这是极其罕见的表现。"

    hide captain_img with dissolve

    $ change_stat("reputation", 5)
    $ change_stat("loyalty", 5)
    $ change_stat("power", 3)
    $ re_duel_met = True

    "塞德里克带着满意离去了。而雷恩在之后的日子里，话虽然还是一样少，但你分明感觉到他的脊背挺得更直了。"

    "——你信任他。在这座充满猜疑的城堡里，这比任何赏赐都重。"

    return


## ============================================================
## 事件 9: 丰收或歉收 (Harvest Outcome)
## ============================================================

label re_harvest:
    if re_harvest_done:
        return

    scene bg village with dissolve

    "秋天到了。田野里的麦穗沉甸甸地低着头，果园里的苹果压弯了枝条——至少表面上看起来是这样。"

    "每年的这个时候，管家都会递交一份年度收成报告。这份报告决定了领地在接下来一整个冬天的命运。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "大人，今年的收成报告出来了。"

    hide aldric_img with dissolve

    # 根据治理状况决定丰歉
    python:
        import random as _py_random
        _harvest_score = _py_random.randint(1, 100)
        # 高声望和忠诚意味着更好的治理
        if reputation >= 50:
            _harvest_score += 20
        if loyalty >= 50:
            _harvest_score += 15
        if wealth >= 50:
            _harvest_score += 10

    if _harvest_score >= 70:
        jump re_harvest_good
    else:
        jump re_harvest_bad

label re_harvest_good:

    scene bg village with dissolve

    "好消息！今年是一个丰收年！"

    "小麦产量比去年增加了三成，果园的苹果和葡萄也是大获丰收。连牲畜都比往年肥壮了许多。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "大人，数字非常好看。按照目前的储量，即使今年冬天格外严寒，我们也能撑过去——而且还有余粮可以出售或赈济。"

    hide aldric_img with dissolve

    "你下令举办丰收庆典。整个领地张灯结彩，百姓们载歌载舞，烤肉的香气弥漫在每一条街巷。"

    scene bg great_hall with dissolve

    "大厅里摆满了丰收的果实——金黄的麦穗编成花环挂在墙上，长桌上堆着各种瓜果蔬菜和新酿的啤酒。"

    "你举起酒杯，对着满堂的百姓和官员说："

    "「这不是我一个人的功劳——是你们每一个人辛勤劳作的结果。今晚，敞开肚子吃喝！」"

    "欢呼声几乎掀翻了屋顶。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "大人，丰收年对士气的提升比任何演讲都管用。士兵们吃饱了肚子，训练时都格外卖力。"

    hide captain_img with dissolve

    $ change_stat("wealth", 10)
    $ change_stat("loyalty", 8)
    $ change_stat("reputation", 5)
    $ re_harvest_done = True

    "仓廪实而知礼节。一个吃饱了的领地，才是一个安定的领地。"

    return

label re_harvest_bad:

    scene bg village with dissolve

    "坏消息。今年的收成远低于预期。"

    "春天的一场倒春寒冻死了大片麦苗，夏天的旱情又让存活下来的庄稼长势不佳。果园的产量也只有往年的六成。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "大人，按照目前的储量，我们的粮食只够撑到明年二月。如果冬天来得早或者持续得久……情况会非常严峻。"

    aldric "我们需要做出一些艰难的决定。"

    hide aldric_img with dissolve

    "你沉默地看着报告上触目惊心的数字。这不仅仅是数字——每一个缺口背后，都是可能饿死的人。"

    menu:
        "你如何应对歉收危机？"

        "实行配给制度，公平分配":
            jump re_harvest_ration

        "向周边领地购买粮食":
            jump re_harvest_buy

        "减少军队口粮，优先保障百姓":
            jump re_harvest_civilian

label re_harvest_ration:

    "你颁布了严格的粮食配给法令。每家每户按人口分配定量口粮，禁止囤积和倒卖。"

    "同时，你带头缩减了城堡的伙食标准——领主的餐桌上也只有粗粮和咸菜。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "大人以身作则，百姓们虽然日子苦了些，但没有人抱怨不公。"

    hide aldric_img with dissolve

    "冬天比预想的漫长，但配给制度运转良好。到春天来临的时候，虽然家家户户都瘦了一圈，但没有一个人饿死。"

    $ change_stat("loyalty", 8)
    $ change_stat("reputation", 5)
    $ change_stat("wealth", -5)
    $ re_harvest_done = True

    "你自己也瘦了。但看着领地里的百姓在春风中重新露出笑容，你觉得值了。"

    return

label re_harvest_buy:

    "你动用了领地金库的储备，紧急向邻近的几个富庶领地购买粮食。"

    "价格不便宜——歉收年的粮价总是被哄抬得离谱。但你别无选择。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve

    aldric "大人，粮食已经运到了。但我们的金库……几乎见底了。"

    hide aldric_img with dissolve

    "钱花出去了，百姓有了过冬的口粮。经济上的窟窿需要很长时间才能填补。不过这个冬天，没有人会饿死。"

    $ change_stat("wealth", -8)
    $ change_stat("loyalty", 5)
    $ change_stat("reputation", 3)
    $ re_harvest_done = True

    "治国如治家——有时候，花钱买的不是东西，是人心。"

    return

label re_harvest_civilian:

    "你做出了一个让雷恩皱起眉头的决定。"

    "「削减军队口粮两成。省下来的粮食全部分配给百姓，优先保障老弱妇孺。」"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve

    captain "大人，士兵们已经在抱怨伙食太差了。再削减的话……"

    "「我知道。」你打断了他，「但如果百姓饿死了，我们保卫的又是什么？」"

    captain "……属下明白了。我会和弟兄们解释的。"

    hide captain_img with dissolve

    "这个冬天很难熬。士兵们的训练强度被迫降低，军营里的抱怨声此起彼伏。但百姓们知道——是军人让出了自己嘴里的粮食来养活他们。"

    "开春之后，参军报名处排起了前所未有的长队。那些曾经被军粮养活的年轻人，如今要亲手拿起武器回报这份恩情。"

    $ change_stat("loyalty", 10)
    $ change_stat("power", -5)
    $ change_stat("reputation", 8)
    $ re_harvest_done = True

    "你失去了一些战力，但收获了民心。而民心，在最黑暗的时刻，往往比刀剑更有力量。"

    return

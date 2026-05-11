## ============================================================
## 第四章：王子诀别场景 + 王子深层线
## chapter4_prince.rpy
## 修复叙事断裂：王子为何从逃亡变成软禁
## ============================================================

## ============================================================
## 营救后的诀别 — 解释王子为何主动返回王都
## ============================================================

label ch4_prince_farewell:

    $ play_music("audio/music/campfire.ogg", fadein=2.0)
    scene bg forest_path with dissolve

    "岔路口。一条路向北，通往艾登堡。另一条路向南，通往王都。"

    "天边已经泛起鱼肚白。逃亡的夜晚即将结束。"

    "王子从马上翻下来，踉跄了一下——伤还没有好。雷恩伸手扶住了他。"

    $ hide_all_chars("prince_img")
    show prince_img at left with dissolve

    prince "到这里就好了。"

    hide prince_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "什么意思？"

    hide player_char_img
    $ hide_all_chars("prince_img")
    show prince_img at left with dissolve
    prince "我不跟你去艾登堡。"

    "你愣住了。"

    hide prince_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "你在说什么？你现在回去就是送死。"

    hide player_char_img
    show prince_img sad at left

    prince "不。如果我跟你走——那才是送死。送我们两个人的死。"

    "他靠在路边一棵老橡树上，喘了口气。伤口在渗血，但他的眼神异常清醒。"

    prince "你想想。一个逃犯王子，躲在一个边境领主的城堡里。"

    prince "母后需要多久才能找到借口发兵？三天？五天？"

    prince "到时候不只是你和我——艾登堡的每一个人都会成为靶子。"

    hide prince_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "那你打算怎么办？"

    hide player_char_img
    $ hide_all_chars("prince_img")
    show prince_img at left with dissolve
    prince "回去。"

    hide prince_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "回去？回那个差点杀了你的地方？"

    "王子笑了。那个笑容里有疲惫，有苦涩，但也有一种你之前没见过的东西——决心。"

    hide player_char_img with dissolve
    $ hide_all_chars("prince_img")
    show prince_img at left

    prince "听我说。母后关我，是因为她怀疑我。但她不会杀我——至少现在不会。"

    prince "我是唯一的王位继承人。杀了我，她就失去了合法性。"

    prince "贵族们再怎么怕她，也不会支持一个弑子的王后。"

    prince "所以她最多软禁我。让我消失在公众的视线里。"

    $ prince_imprisoned_known = True

    hide prince_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "软禁也不是什么好下场。"

    hide player_char_img
    $ hide_all_chars("prince_img")
    show prince_img at left with dissolve
    prince "比死强。而且——"

    "他压低了声音，环顾四周确认没有其他人能听到。"

    prince "我在宫里还有自己的人。三个侍女，两个文官，一个御厨。"

    prince "都是跟了我十年以上的人。母后不知道他们效忠于我。"

    prince "只要我在宫里，这张网就还在。我被关着，但我的眼睛和耳朵没有被关住。"

    prince "我需要从内部收集证据——母后篡改遗诏的原始文件，当年参与谋杀你父亲的人的证词。"

    if not testament_forged_known:
        "篡改遗诏——你第一次听到这个说法，但王子说得如此笃定，不像是猜测。"
        $ testament_forged_known = True
    if not father_poisoned_known:
        "谋杀？你一直以为父亲是病死的。王子的话像一把利刃刺穿了你心中最后的侥幸。"
        $ father_poisoned_known = True

    prince "这些东西只存在于王宫深处。只有我能接触到。"

    menu:
        "理解他的计划，但担心他的安全":
            $ change_rel("rel_prince", 8)
            $ prince_trust_deep = True
            hide prince_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你考虑得比我周全。但你确定你能撑住？"
            hide player_char_img
            $ hide_all_chars("prince_img")
            show prince_img at left with dissolve
            prince "十二年的宫廷生活教会了我一件事——"
            prince "最安全的地方，就是敌人认为你已经被驯服的地方。"
            prince "我会装作一个悔过的、顺从的王子。她会相信的。因为她太骄傲了，她相信所有人最终都会屈服于她。"
            hide prince_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "如果她不信呢？"
            hide player_char_img
            $ hide_all_chars("prince_img")
            show prince_img at left with dissolve
            prince "那你就当我已经死了。继续做你该做的事。"
            $ hide_all_chars()
            "他说得很平静。像是在说一件与自己无关的事。"
            "但你注意到他握着缰绳的手在微微发抖。"

        "试图劝阻——这太危险了":
            $ change_rel("rel_prince", 5)
            hide prince_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "不行。这太冒险了。你跟我走，我们可以联合北方的领主——"
            hide player_char_img
            $ hide_all_chars("prince_img")
            show prince_img at left with dissolve
            prince "联合北方？你觉得男爵会帮我？"
            prince "男爵想要的是自己当王，不是拥立一个年轻的王子。"
            prince "我回去，至少还能从内部牵制母后。让她分心，让她不敢全力对付你。"
            prince "而你在外面，联合愿意追随正义的人。"
            prince "里应外合。这是唯一的胜算。"
            "他说得有道理——比你愿意承认的更有道理。"

        "直接问他是否还有其他原因":
            $ change_stat("intrigue", 5)
            $ change_rel("rel_prince", 10)
            $ prince_trust_deep = True
            hide prince_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "弗雷德里克。我们刚从地牢里死里逃生。你不会仅仅因为'战略考量'就要回去。"
            player "告诉我真正的原因。"
            $ hide_all_chars()
            "王子沉默了很久。长到你以为他不会回答了。"
            "然后他开口了，声音很低。"
            hide player_char_img
            $ hide_all_chars("prince_img")
            show prince_img at left with dissolve
            prince "宫里还有一个人。"
            prince "我的妹妹。"
            hide prince_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你有妹妹？"
            hide player_char_img
            $ hide_all_chars("prince_img")
            show prince_img at left with dissolve
            prince "同父异母。母后从来不承认她的存在。她是父王和一个侍女的女儿。"
            prince "母后把她养在后宫最偏僻的院子里。没有名字，没有身份。像一只笼子里的鸟。"
            prince "她今年十四岁。如果我不回去……就没有人保护她了。"
            $ hide_all_chars()
            "你感到一阵刺痛。这个年轻人背负的东西比你想象的多得多。"

    $ prince_returned_willingly = True

    "你们沉默地站在岔路口。晨光穿过树冠，在地上洒下斑驳的光影。"

    hide prince_img
    show captain_img at right with dissolve

    captain "领主大人，天快亮了。我们必须在天亮前赶过猎人岭，否则王后的斥候会发现我们的踪迹。"

    hide captain_img with dissolve

    "时间不多了。你看着王子，心中有千言万语，最终只说了一句。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "活着。"

    hide player_char_img
    $ hide_all_chars("prince_img")
    show prince_img at left with dissolve
    prince "你也是。"

    "他从怀里掏出一枚小小的银质徽章——一只展翅的隼鸟，是弗雷德里克家族的私印。"

    prince "拿着。如果有一天你需要证明我们之间的盟约——这就是凭证。"

    prince "任何看到这枚徽章的人都会知道，持有者是弗雷德里克王子唯一信任的人。"

    $ hide_all_chars()
    "你接过徽章。银子在晨光中闪着微弱的光。"

    "它很轻。但你知道它代表的东西，比你见过的任何金银都要沉重。"

    hide prince_img with dissolve

    "王子翻身上马——动作因为伤势而有些笨拙。"

    "他没有回头。"

    "你看着他的身影沿着南边的路渐渐远去，朝阳把他的影子拖得很长，直到和路面融为一体。"

    "一个浑身是伤的年轻人，骑着一匹偷来的马，独自走向一座试图杀死他的城市。"

    "因为那里有他必须守护的东西。"

    "你转过头，望向北方。艾登堡在那里等着你。"

    "你的战场在北方。他的战场在南方。"

    "但你们的敌人，是同一个人。"

    $ play_sound("audio/sfx/horse_gallop.ogg")

    "你策马北行。冬天的晨风刮在脸上，像刀一样。"

    "但你心里烧着一团火。"

    jump ch4_end

## ============================================================
## 第五章扩展：王子来信（替换原有简短版本）
## 从 chapter5.rpy 中的 prince_ally 分支调用
## ============================================================

label ch5_prince_letter:

    scene bg study with dissolve
    $ unlock_gallery("bg_study")

    "一个衣衫褴褛的少年出现在城门口，自称是王都来的信使。"

    "守卫搜了他的身，在他鞋底的夹层里找到了一封信——用王子的私印蜡封。"

    "你在书房里拆开了信。"

    $ hide_all_chars("prince_img")
    show prince_img at left with dissolve
    $ unlock_gallery("prince")

    prince "致艾登堡领主——我的兄弟："

    if not prince_imprisoned_known:
        prince "如你所料，我回到王宫后被软禁了。母后没有对外公布我出逃的事——"

        prince "因为承认王子越狱，比假装什么都没发生更丢人。"

        prince "所以在外界看来，王子殿下只是'偶感风寒，闭门养病'。"

        $ prince_imprisoned_known = True
    else:
        prince "我果然被软禁了，和我们预料的一样。母后对外只说我'偶感风寒'。"

    if prince_trust_deep:
        prince "我们那晚谈的事——我没有忘记。她很安全。我已经把她转移到了更隐蔽的地方。"
    else:
        prince "有些事我暂时不能多说。但请相信我，我回来不仅仅是为了自己。"

    prince "宫里的情况比我预想的更糟。母后已经决定用武力解决一切。"

    prince "她的心腹蒙塔古伯爵正在集结军队。三千人，也许更多。"

    prince "但军中不是铁板一块。我的人传来消息——至少有三个营的士兵对这场'平叛'战争心存疑虑。"

    prince "他们中很多人的家就在北方。他们不想对自己的乡亲动刀。"

    if testament_forged_known:
        prince "我能做的不多。但我已经安排人在军中散布真相——遗诏被篡改的事。"
    else:
        prince "我能做的不多。但我已经安排人在军中散布一些……关于母后的真相。"
        $ testament_forged_known = True

    prince "种子已经种下。它会在合适的时候发芽。"

    prince "还有一件事——我在母后的书房里找到了一份文件。"

    prince "是二十年前那场'意外'的详细记录。你父亲的名字在上面。"

    prince "我没法把原件带出来，但我把关键内容抄录在了这封信的背面。"

    prince "用它。在最需要的时候。"

    $ hide_all_chars()
    "你翻过信纸。背面密密麻麻地写满了蝇头小楷——日期、人名、命令、剂量。"

    "触目惊心。"

    $ true_killer_known = True

    menu:
        "回信：请他在最关键的时刻公开表态":
            $ change_rel("rel_prince", 3)  ## batch 14 #7 王子好感: 5→3 减弱小加成累加
            hide prince_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "殿下，当战争到来的那一天，我需要你站出来。不是为了我，是为了这个国家。"
            $ hide_all_chars()
            "你写了一封简短但坚定的回信。"
            "少年信使把信藏在鞋底，还没等你说完就走了。"

        "回信：让他千万保重，不要冒险":
            $ change_rel("rel_prince", 1)  ## batch 14 #7 王子好感: 3→1 减弱小加成累加
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你已经做得够多了。保护好自己。等一切尘埃落定，我们再见面。"
            $ hide_all_chars()
            "你犹豫了一下，又加了一句：'活着。这是命令。'"

        "不回信——信使可能被跟踪" if intrigue >= 60:
            $ change_stat("intrigue", 5)
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "信使，你来的路上有没有被人跟踪？"
            $ hide_all_chars("servant_generic_img")
            show servant_generic_img at left with dissolve
            young_man "我……我不确定。出城的时候有人盯了我一会儿……"
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "那就不回信了。回去告诉殿下三个字：'知道了。'"
            player "越短越安全。如果他们截获了这封空口信，也什么都查不到。"
            $ hide_all_chars()
            "少年点点头，迅速离开了。"
            "你将信纸上的内容仔细抄录了一份，然后把原件放在烛火上烧成了灰烬。"

    hide prince_img with dissolve
    hide player_char_img with dissolve

    return

## ============================================================
## 第五章：王子的背叛分支
## 当 prince_ally 为真但好感度过低时，王子在最终对决中反水
## ============================================================

label ch5_prince_betrayal:

    ## 这个 label 在最终对决场景中被调用
    ## 条件：prince_ally and not prince_betrayed and rel_prince < 25

    show prince_img at right with dissolve

    prince "够了，母后。"

    hide prince_img
    $ hide_all_chars("queen_img")
    show queen_img at left with dissolve
    queen "弗雷德里克——"

    hide queen_img
    $ hide_all_chars("prince_img")
    show prince_img at left with dissolve
    prince "我有话要说。"

    $ hide_all_chars()
    "王子从人群中走出来。他穿着一身白色的礼服，脸上的表情平静而庄重。"

    "你松了一口气。王子终于站出来了。"

    "但接下来的话——"

    $ hide_all_chars("prince_img")
    show prince_img at left with dissolve
    prince "我要在圣母面前，在所有人面前——"

    prince "告发一个叛逆者。"

    $ hide_all_chars()
    "他转向你。"

    "你的血液凝固了。"

    $ hide_all_chars("prince_img")
    show prince_img at left with dissolve
    prince "这个人——艾登堡领主——在王都期间密谋推翻王后。"

    prince "他利用我对王国的忧虑，诱导我参与他的阴谋。"

    prince "我一时糊涂，差点酿成大错。"

    "大厅里一片哗然。你感觉脚下的地面在崩塌。"

    hide queen_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "弗雷德里克……你在干什么？"

    $ hide_all_chars()
    "王子看着你。他的眼神很复杂——不是胜利者的得意，也不是背叛者的愧疚。"

    "而是一种深深的、无奈的疲倦。"

    hide player_char_img
    $ hide_all_chars("prince_img")
    show prince_img at left with dissolve
    prince "（低声，只有你能听到）对不起。"

    prince "（低声）但我没有选择。她知道了一切。如果我不这么做——不只是我，还有很多人会死。"

    hide prince_img
    $ hide_all_chars("queen_img")
    show queen_img at left with dissolve
    queen "弗雷德里克，你做了正确的选择。"

    "王后的脸上浮现出一个微笑。不是冰冷的那种——而是一种母亲看到浪子回头的……满足。"

    queen "看到了吗，各位？连我自己的儿子都差点被这个人蛊惑。"

    queen "可见此人的野心何等危险。"

    menu:
        "愤怒地揭露王子的虚伪":
            $ change_stat("power", 5)
            $ change_rel("rel_prince", -30)
            hide queen_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "好一出戏！殿下的演技比宫廷的伶人还要出色。"
            player "你们在地牢里跟我说的那些话——关于公平、正义、新的王国——"
            player "全是谎言吗？"
            "王子没有回答。但你看到他的手在微微发抖。"
            hide player_char_img
            $ hide_all_chars("prince_img")
            show prince_img at left with dissolve
            prince "你信什么就是什么。"

        "冷静分析——这不像是自愿的":
            $ change_stat("intrigue", 8)
            hide prince_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "（低声对身边的人）看他的手。他在发抖。这不是自愿的。"
            "艾琳娜凑过来。"
            hide player_char_img
            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "（低声）你说得对。他的眼睛在看左上角——宫廷审讯的标准姿态。他在背诵排练好的台词。"
            elena "他被迫的。但这不改变结果。"
            hide elena_img with dissolve
            "不管王子是被迫还是自愿——他的话已经说出口了。在场的所有人都听到了。"

        "沉默。不给他们更多弹药":
            $ change_stat("intrigue", 5)
            $ hide_all_chars()
            "你一言不发。只是看着王子，看了很久。"
            "你在他的眼睛里寻找那个在月光下跟你说'你是我的兄弟'的人。"
            "也许还在。也许已经不在了。"
            "但现在不是追究这件事的时候。"

    "王子的倒戈让局势急转直下。原本开始动摇的贵族们又缩了回去。"

    "你必须在没有王子支持的情况下，独自面对王后。"

    $ prince_ally = False

    hide prince_img with dissolve

    return

## ============================================================
## 第五章：王子最终对决加强版
## 替换原有的简单对话，增加情感深度
## ============================================================

label ch5_prince_confronts_queen:

    show prince_img at right with dissolve

    prince "够了，母后。"

    hide prince_img
    $ hide_all_chars("queen_img")
    show queen_img at left with dissolve
    queen "弗雷德里克——"

    $ hide_all_chars()
    "王子从人群的后方走出来。"

    "他穿着一身白色的礼服——不是华贵的宫廷款式，而是素净、简朴的骑士制服。"

    "左胸口别着一枚银质隼鸟徽章。和你怀里那枚一模一样。"

    hide queen_img
    $ hide_all_chars("prince_img")
    show prince_img at left with dissolve
    prince "我爱你，母后。你是给我生命的人。这一点永远不会改变。"

    "他的声音平静而坚定。十二年的隐忍，凝聚在这一刻。"

    prince "但你做错了。"

    prince "二十年来，你用谎言统治这个国家。用恐惧代替信任，用阴谋代替正义。"

    if prince_mentor_known:
        prince "你杀了西里尔。那个教我骑马、教我读书的老人。因为他给了我一本记载真相的书。"
        prince "你杀了他的父亲。一个只想做好领主的好人。因为他发现了你的秘密。"
        prince "你把你自己的女儿关在后宫最阴暗的角落里。因为她的存在提醒着你犯过的错。"
        "王后的脸色终于变了。不是愤怒——而是震惊。"
        hide prince_img
        $ hide_all_chars("queen_img")
        show queen_img at left with dissolve
        queen "你……你怎么知道那些事？"
        hide queen_img
        $ hide_all_chars("prince_img")
        show prince_img at left with dissolve
        prince "因为你低估了一个假装十二年的人能做到什么。"
    else:
        prince "一个好人因为你的谎言而死。他的儿子从小失去了父亲。"
        prince "这不是一个王后应该做的事。这不是一个母亲应该做的事。"

    prince "是时候结束了。"

    $ hide_all_chars()
    "王后看着自己的儿子，眼中第一次出现了脆弱。"

    "那个精明强干、不可一世的女人，在儿子的话语面前崩塌了——哪怕只是一瞬间。"

    hide prince_img
    $ hide_all_chars("queen_img")
    show queen_img at left with dissolve
    queen "你也要背叛我吗……"

    hide queen_img
    $ hide_all_chars("prince_img")
    show prince_img at left with dissolve
    prince "这不是背叛，母后。这是拯救。"

    prince "拯救这个国家——也拯救你。"

    "他顿了一下。"

    prince "我来的时候经过了你的花园。那里的花开了。"

    prince "你还记得吗？小时候你带我在那里种过一棵玫瑰。你说，'照顾好它，就像照顾一个王国。'"

    prince "那棵玫瑰还在。但花园的主人，已经忘了当初的心意。"

    $ hide_all_chars()
    "王后的嘴唇在颤抖。你从未见过她这个样子。"

    "整个大厅鸦雀无声。"

    hide prince_img with dissolve

    return

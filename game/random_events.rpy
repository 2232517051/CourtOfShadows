## ============================================================
## 随机事件系统 - Random Events
## random_events.rpy
## 在章节过渡、休息、探索时触发随机事件
## ============================================================

## ── 事件追踪变量 ──
default random_events_seen = set()
default last_event_result = ""
default random_event_cooldown = 0

init python:
    import random as _py_random

    ## ================================================================
    ## 事件数据库
    ## ================================================================

    _random_events = {

        ## ────────────────────────────────────────
        ## 1. 战斗遭遇 (Combat Encounters)
        ## ────────────────────────────────────────

        "road_bandits": {
            "id": "road_bandits",
            "title": "路遇山贼",
            "category": "combat",
            "icon": "剑",
            "icon_color": "#e74c3c",
            "rarity": 30,  # 越高越常见
            "min_chapter": 1,
            "max_chapter": 5,
            "conditions": {},  # 无额外条件
            "context": ["travel", "explore"],
            "description": "一行人穿过林间小道时，前方突然倒下一棵大树，堵住了去路。\n\n树丛中传来粗野的笑声，七八个衣衫褴褛的山贼手持柴刀和短矛，从两侧包围了你们。\n\n为首的秃头大汉咧嘴一笑：「留下财物，饶你们不死！」",
            "choices": [
                {
                    "text": "拔剑迎战「以武力驱散山贼」",
                    "stat_req": ("power", 25),
                    "success": {
                        "narration": "你拔出佩剑，寒光一闪。领头的山贼还没反应过来，你已经踏步上前，一剑削断了他手中的柴刀。\n\n「艾登堡领主在此，尔等速速退去！」\n\n山贼们见你剑法凌厉，又听到「领主」二字，顿时面如土色，丢下武器四散奔逃。",
                        "effects": [("stat", "power", 3), ("stat", "reputation", 5)],
                    },
                    "failure": {
                        "narration": "你抽出佩剑，但手腕一阵发软——你毕竟不是久经沙场的战士。\n\n秃头大汉一棒打飞你的剑，众山贼哄堂大笑。所幸你的随从及时上前护驾，在一番混战后才将山贼赶跑，但你也因此丢了些财物。",
                        "effects": [("stat", "wealth", -5), ("stat", "power", 1)],
                    },
                },
                {
                    "text": "用金币打发「花钱消灾」",
                    "stat_req": None,
                    "success": {
                        "narration": "你从马车里取出一袋银币，抛向山贼头目。\n\n「拿去，别挡道。」\n\n秃头大汉接过钱袋，掂了掂重量，满意地点头：「识相！弟兄们，让路！」\n\n山贼们搬开倒木，让你的马车通过。虽然破了些财，但省去了不少麻烦。",
                        "effects": [("stat", "wealth", -8)],
                    },
                    "failure": None,
                },
                {
                    "text": "智取山贼「用计谋化解」",
                    "stat_req": ("intrigue", 30),
                    "success": {
                        "narration": "你不慌不忙地从马车上走下来，打量了一圈周围的地形。\n\n「你们的人数我已经数清楚了，七个人。但你们注意到后面树丛里我的弓箭手了吗？」\n\n你朝身后做了个手势。树丛中恰好有鸟群受惊飞起，发出窸窣之声。\n\n山贼们面面相觑，脸色大变。秃头大汉犹豫了一下，喝令手下撤退。\n\n——当然，树丛里什么人也没有。",
                        "effects": [("stat", "intrigue", 3), ("stat", "reputation", 3)],
                    },
                    "failure": {
                        "narration": "你试图虚张声势，但那秃头大汉是个老江湖，一眼就看穿了你的把戏。\n\n「少唬人！弟兄们，上！」\n\n一番混战后，你虽然脱了身，但行李被翻了个遍。",
                        "effects": [("stat", "wealth", -10), ("stat", "intrigue", 2)],
                    },
                },
            ],
        },

        "night_assassin": {
            "id": "night_assassin",
            "title": "暗夜刺客",
            "category": "combat",
            "icon": "刃",
            "icon_color": "#2d1b4e",
            "rarity": 8,
            "min_chapter": 3,
            "max_chapter": 5,
            "conditions": {"intrigue_min": 30},
            "context": ["rest"],
            "description": "深夜，你在书房中翻阅文件，烛火摇曳。\n\n突然，一阵不属于风的气流掠过你的后颈。你的本能让你在那一瞬间低下了头——\n\n一柄淬了毒的匕首擦着你的头皮飞过，深深嵌入身后的书架。\n\n黑衣人从阴影中现身，面罩下的双眼冷若寒冰。",
            "choices": [
                {
                    "text": "正面交锋「与刺客搏斗」",
                    "stat_req": ("power", 40),
                    "success": {
                        "narration": "你掀翻桌案作为屏障，顺势抄起墙上的装饰剑。\n\n刺客身法极快，几次攻击都险象环生。但你抓住他换招的空隙，一脚踢翻烛台。在黑暗中，你凭借对书房地形的熟悉，一剑刺中了刺客的肩膀。\n\n刺客吃痛，翻窗而逃。你在他遗落的匕首上发现了一个奇怪的标记——一朵黑色的百合花。",
                        "effects": [("stat", "power", 5), ("stat", "intrigue", 3), ("flag", "assassination_survived", True)],
                    },
                    "failure": {
                        "narration": "你试图反抗，但刺客的身手远在你之上。几个回合后，你被逼入墙角。\n\n幸好侍卫听到动静赶来，刺客见势不妙，摔了一颗烟雾弹翻窗而逃，等烟散了已经没了踪影。你的手臂被划了一道口子，伤口隐隐发黑——是毒。\n\n经过一夜的紧急处理，你捡回了一条命。",
                        "effects": [("stat", "power", -3), ("stat", "wealth", -5), ("flag", "assassination_survived", True)],
                    },
                },
                {
                    "text": "呼叫侍卫「紧急求援」",
                    "stat_req": None,
                    "success": {
                        "narration": "你大声呼叫侍卫，同时掀翻书桌挡在身前。\n\n刺客显然不想被人发现身份，犹豫了一瞬。门外传来急促的脚步声和甲胄碰撞声——侍卫们冲了进来。\n\n刺客冷哼一声，打碎窗户跳了出去，等你冲到窗边往下看时，地上只有一片碎玻璃。你虽然安全了，但那个身影……你总觉得似曾相识。",
                        "effects": [("stat", "loyalty", 3), ("flag", "assassination_survived", True)],
                    },
                    "failure": None,
                },
                {
                    "text": "以言相试「质问刺客身份」",
                    "stat_req": ("intrigue", 50),
                    "success": {
                        "narration": "你镇定地坐回椅子，看着刺客手中的匕首。\n\n「暗百合的人？还是男爵的？」你平静地说，「杀了我，对你的主人并没有好处。」\n\n刺客微微一愣。你抓住这个机会继续说：「我知道你们要什么。坐下来谈谈，也许我们能达成共识。」\n\n刺客收起匕首，从怀中取出一封信放在桌上，然后无声无息地消失了。\n\n信上只有一句话：「暴风将至，你只有两条路。」",
                        "effects": [("stat", "intrigue", 4), ("stat", "reputation", 3), ("flag", "assassination_survived", True)],
                    },
                    "failure": {
                        "narration": "你试图与刺客对话，但对方显然没有交谈的意思。\n\n匕首再次袭来，你勉强躲开，大声呼救。侍卫破门而入时，刺客已经消失。\n\n你只在地上找到一片黑色的花瓣。",
                        "effects": [("stat", "intrigue", 2), ("flag", "assassination_survived", True)],
                    },
                },
            ],
        },

        "duel_challenge": {
            "id": "duel_challenge",
            "title": "决斗挑战",
            "category": "combat",
            "icon": "剑",
            "icon_color": "#c0392b",
            "rarity": 15,
            "min_chapter": 2,
            "max_chapter": 5,
            "conditions": {"reputation_min": 50},
            "context": ["travel", "explore"],
            "description": "一位身穿铠甲的骑士拦住了你的去路。他摘下头盔，露出一张年轻而傲慢的面孔。\n\n「你就是艾登堡的新领主？」他冷笑道，「我是北境布雷格家的三子，埃里克·布雷格。听闻你声名远扬，今日特来讨教。」\n\n他拔出长剑，在阳光下划了一道弧线：「堂堂正正地决斗，敢不敢？」",
            "choices": [
                {
                    "text": "接受决斗「用实力证明自己」",
                    "stat_req": ("power", 45),
                    "success": {
                        "narration": "你翻身下马，拔出佩剑。\n\n埃里克的剑法凌厉而富有攻击性，但你很快发现了他的弱点——右侧防守空隙。你佯攻左方，在他格挡的瞬间转向右侧，剑尖抵住了他的咽喉。\n\n「承让。」\n\n埃里克瞪大了眼睛，随即哈哈大笑：「好！名不虚传！」他收剑行礼，「日后若有需要，布雷格家愿为你效力。」",
                        "effects": [("stat", "power", 5), ("stat", "reputation", 8)],
                    },
                    "failure": {
                        "narration": "你接受了挑战，但埃里克的剑术确实高超。几个回合后，你的剑被击飞，跪倒在地。\n\n「不过如此。」埃里克失望地摇头，转身离去。\n\n这次失败让你在随从面前颜面尽失。",
                        "effects": [("stat", "reputation", -8), ("stat", "power", 2)],
                    },
                },
                {
                    "text": "婉言拒绝「不必用武力解决」",
                    "stat_req": None,
                    "success": {
                        "narration": "你微微一笑：「布雷格家的勇名我素有耳闻。不过，真正的强者不在于剑术，而在于治国之策。若阁下有兴趣，不妨到艾登堡做客，我们以棋论道如何？」\n\n埃里克愣了一下，似乎没想到你会这样回答。他沉思片刻，收起长剑：「有意思。也许我会去的。」",
                        "effects": [("stat", "reputation", -2), ("stat", "intrigue", 3)],
                    },
                    "failure": None,
                },
                {
                    "text": "设定条件「提出赌注」",
                    "stat_req": ("intrigue", 35),
                    "success": {
                        "narration": "「决斗可以，但总得有个彩头。」你不紧不慢地说。\n\n「我若胜，布雷格家与艾登堡签订贸易协定，三年内粮食半价供应。你若胜，我赠你一匹艾登堡最好的战马。」\n\n埃里克眼前一亮——他是出了名的爱马之人。\n\n决斗开始后，你并不急于进攻，而是不断消耗他的体力。最终，埃里克气喘吁吁地举手认输。\n\n「好个心机领主……」他苦笑道，但还是信守了承诺。",
                        "effects": [("stat", "wealth", 18), ("stat", "intrigue", 3), ("stat", "reputation", 5)],
                    },
                    "failure": {
                        "narration": "你提出了赌注条件，但在决斗中落了下风。不得不信守承诺，送出了一匹好马。\n\n不过，埃里克对你的气度颇为赞赏，临走时说了句：「你这人，有意思。」",
                        "effects": [("stat", "wealth", -5), ("stat", "reputation", 2)],
                    },
                },
            ],
        },

        "deserter_ambush": {
            "id": "deserter_ambush",
            "title": "逃兵伏击",
            "category": "combat",
            "icon": "剑",
            "icon_color": "#7f8c8d",
            "rarity": 25,
            "min_chapter": 2,
            "max_chapter": 5,
            "conditions": {},
            "context": ["travel"],
            "description": "道路旁的沟壑中传来微弱的呻吟声。你循声望去，发现一个浑身是血的士兵趴在草丛中。\n\n但你敏锐地注意到——他的伤口已经干涸，这不像是刚受的伤。而且，前方的灌木丛中似乎有金属的反光……\n\n这很可能是逃兵设下的陷阱。",
            "choices": [
                {
                    "text": "识破陷阱「绕路前进」",
                    "stat_req": ("intrigue", 20),
                    "success": {
                        "narration": "你下令队伍停下，派出斥候从侧翼包抄。\n\n果然，灌木丛中埋伏着十余名逃兵。被包围后，他们放下了武器。\n\n审讯后得知，这些人原是男爵麾下的士兵，因欠饷而逃。你将他们收编，让他们为领地效力。",
                        "effects": [("stat", "intrigue", 3), ("stat", "power", 5), ("stat", "loyalty", 3)],
                    },
                    "failure": {
                        "narration": "你让队伍绕路，但逃兵们显然设了不止一处埋伏。绕路时你们踏入了另一个陷阱，几名随从受伤。\n\n不过，你的果断决策避免了更大的损失。",
                        "effects": [("stat", "power", -2), ("stat", "intrigue", 2)],
                    },
                },
                {
                    "text": "上前救助「也许真有伤兵」",
                    "stat_req": None,
                    "success": {
                        "narration": "你不顾随从的劝阻，亲自走近查看。\n\n趴在地上的「伤兵」突然跳起，但你早有防备，一脚踢飞了他手中的匕首。从灌木丛中冲出的逃兵被你的随从迎头痛击。\n\n虽然中了埋伏，但你方损失不大。那些逃兵在你的威势下跪地求饶。",
                        "effects": [("stat", "power", 3), ("stat", "wealth", -3)],
                    },
                    "failure": None,
                },
                {
                    "text": "以仁感化「喊话招降」",
                    "stat_req": ("loyalty", 40),
                    "success": {
                        "narration": "你停下马车，朝灌木丛的方向大声喊道：\n\n「我知道你们在那里。你们是逃兵，不是匪徒。放下武器出来，我保证不追究。艾登堡需要士兵，你们需要一口饭吃。何必刀口舔血？」\n\n过了很久。终于，一个接一个，十几名逃兵从藏身处走了出来，扔下武器，跪在路边。\n\n你信守了承诺，将他们编入领地守备队。从此，这条路上再也没有出现过劫匪。",
                        "effects": [("stat", "loyalty", 8), ("stat", "power", 3), ("stat", "reputation", 5)],
                    },
                    "failure": {
                        "narration": "你试图招降，但逃兵们并不信任贵族的承诺。\n\n「少骗人了！」一阵乱箭射来，你的随从举盾护驾。一番混战后，逃兵被击退，但你方也有数人受伤。",
                        "effects": [("stat", "power", -3), ("stat", "loyalty", 2)],
                    },
                },
            ],
        },

        ## ────────────────────────────────────────
        ## 2. 交易机会 (Trade Opportunities)
        ## ────────────────────────────────────────

        "wandering_merchant": {
            "id": "wandering_merchant",
            "title": "流浪商人",
            "category": "trade",
            "icon": "金",
            "icon_color": "#f39c12",
            "rarity": 28,
            "min_chapter": 1,
            "max_chapter": 5,
            "conditions": {},
            "context": ["travel", "explore", "rest"],
            "description": "一辆装饰华丽的马车停在路边。车帘掀开，露出一张圆脸——是个来自南方的行商。\n\n他热情地招呼你：「尊贵的领主！我这里有些好东西，保证您在别处见不到。来看看？」\n\n他的货物琳琅满目，但价格不菲。",
            "choices": [
                {
                    "text": "购买药草「采购药材物资」",
                    "stat_req": None,
                    "success": {
                        "narration": "你挑选了一批品质上乘的药草和绷带。商人还附赠了一小瓶香料——「老客户的福利！」\n\n这些物资在未来的日子里会很有用。",
                        "effects": [("stat", "wealth", -5), ("stat", "loyalty", 2)],
                    },
                    "failure": None,
                },
                {
                    "text": "购买铁矿石「强化军备」",
                    "stat_req": None,
                    "success": {
                        "narration": "商人压低声音：「这批铁矿是从东方矿山偷偷运出来的，品质极佳。用来打造武器再好不过。」\n\n你仔细检查了成色，确实不错。谈好价格后成交。",
                        "effects": [("stat", "wealth", -8), ("stat", "power", 3)],
                    },
                    "failure": None,
                },
                {
                    "text": "讨价还价「用口才压价」",
                    "stat_req": ("intrigue", 25),
                    "success": {
                        "narration": "你漫不经心地翻看货物，指出几处瑕疵。商人脸色微变。\n\n「这品质，不值你开的价。」你又补了一句，「当然，我是个长期客户。以后你走这条路，都可以到艾登堡歇脚。」\n\n商人权衡了一番，同意以七折成交。你以极低的价格买到了一批上好的物资。",
                        "effects": [("stat", "wealth", -3), ("stat", "intrigue", 2), ("stat", "power", 2), ("stat", "faith", 1)],
                    },
                    "failure": {
                        "narration": "你试图压价，但这个商人显然也是个老手。一番唇枪舌剑后，他寸步不让。\n\n最终你不得不按原价购买了一些物资。",
                        "effects": [("stat", "wealth", -6), ("stat", "loyalty", 1)],
                    },
                },
                {
                    "text": "不买了「继续赶路」",
                    "stat_req": None,
                    "success": {
                        "narration": "你礼貌地婉拒了商人的推销。他虽然有些失望，但还是笑着说：「下次再会！」\n\n有时候，最好的买卖就是不买。",
                        "effects": [],
                    },
                    "failure": None,
                },
            ],
        },

        "gambling_invitation": {
            "id": "gambling_invitation",
            "title": "赌博邀请",
            "category": "trade",
            "icon": "金",
            "icon_color": "#e67e22",
            "rarity": 15,
            "min_chapter": 1,
            "max_chapter": 5,
            "conditions": {},
            "context": ["rest", "explore"],
            "description": "在城镇的酒馆中，一桌衣着考究的人正在掷骰子。\n\n其中一人注意到了你，举起酒杯：「领主大人，来一把？赌注不大，助助兴而已。」\n\n桌上堆着金币——赌注看起来可不小。",
            "choices": [
                {
                    "text": "参与赌博「碰碰运气」",
                    "stat_req": None,
                    "success": {
                        "narration": "骰子在桌上滚动，停下时露出六点——满堂彩！\n\n桌上的人倒吸一口冷气。你不动声色地将金币收入囊中。\n\n「今晚的酒，我请了。」",
                        "effects": [("stat", "wealth", 18)],
                    },
                    "failure": {
                        "narration": "连续几把下来，你的金币越来越少。对面那个笑眯眯的人似乎手气好得不正常……\n\n你意识到可能被做了手脚时，已经输了不少。只好苦笑着离席。",
                        "effects": [("stat", "wealth", -10)],
                    },
                },
                {
                    "text": "识破骗局「用谋略揭穿」",
                    "stat_req": ("intrigue", 40),
                    "success": {
                        "narration": "你注意到庄家的手法——换骰子的动作极其隐蔽，但你的眼力捕捉到了。\n\n你不动声色地坐下，等庄家再次换骰时猛地抓住他的手腕，在众人面前抖出了藏在袖中的灌铅骰子。\n\n「作弊可不好。」\n\n庄家脸色惨白。围观的赌客们纷纷要求退钱。混乱中，你不仅拿回了本金，还额外获得了一笔「封口费」。",
                        "effects": [("stat", "wealth", 18), ("stat", "intrigue", 3), ("stat", "reputation", 3)],
                    },
                    "failure": {
                        "narration": "你怀疑有诈，但没能找到确凿证据。犹豫间，已经输了几把。\n\n最终你以身体不适为由退出。虽然损失不大，但总觉得意难平。",
                        "effects": [("stat", "wealth", -5), ("stat", "intrigue", 2)],
                    },
                },
                {
                    "text": "拒绝参与「赌博非君子所为」",
                    "stat_req": None,
                    "success": {
                        "narration": "你举起酒杯回敬：「多谢好意。不过身为领主，当以身作则。赌博之事，还是免了。」\n\n酒馆里有人低声称赞你的自制力。",
                        "effects": [("stat", "reputation", 3), ("stat", "faith", 6)],
                    },
                    "failure": None,
                },
            ],
        },

        "smuggler": {
            "id": "smuggler",
            "title": "走私贩子",
            "category": "trade",
            "icon": "刃",
            "icon_color": "#34495e",
            "rarity": 10,
            "min_chapter": 2,
            "max_chapter": 5,
            "conditions": {},
            "context": ["explore", "rest"],
            "description": "深夜，一个蒙面人在后巷拦住了你的去路。\n\n「别紧张，领主大人。我有些……特殊的货物，也许你会感兴趣。」\n\n他掀开斗篷一角，露出几个精致的瓶子和一包暗色的粉末。价格只有市价的三分之一，但来路显然不正。",
            "choices": [
                {
                    "text": "购买走私货「便宜不占白不占」",
                    "stat_req": None,
                    "success": {
                        "narration": "你仔细检查了货物的品质——确实是好东西。毒药提取物、圣水、上好的皮革，这些在市面上很难买到。\n\n你付了钱，蒙面人拐了个弯就不见了。\n\n虽然来路不正，但实用就好。",
                        "effects": [("stat", "wealth", -3), ("stat", "intrigue", 4), ("stat", "power", 2)],
                    },
                    "failure": {
                        "narration": "你掏钱买下了货物，回去打开一看——圣水是掺了盐的井水，毒药提取物不过是研碎的草药。\n\n你被骗了。那个蒙面人早已不知去向。",
                        "effects": [("stat", "wealth", -5), ("stat", "intrigue", 1)],
                    },
                },
                {
                    "text": "逮捕走私贩「维护法律」",
                    "stat_req": ("power", 30),
                    "success": {
                        "narration": "你一把抓住蒙面人的手腕，大声呼叫侍卫。\n\n蒙面人挣扎着想逃，但你死死扣住不放。侍卫赶到后将其制服。\n\n搜查后发现他身上携带的货物数量不少，全部充公。你下令将此事公之于众，以儆效尤。",
                        "effects": [("stat", "reputation", 5), ("stat", "power", 3), ("stat", "loyalty", 3), ("stat", "wealth", 3)],
                    },
                    "failure": {
                        "narration": "你试图抓住蒙面人，但他身法极快，一个翻身跃上矮墙，几步就和石墙的颜色混在了一起。\n\n你只来得及捡起他掉落的一小包货物。",
                        "effects": [("stat", "power", 1), ("stat", "wealth", 1)],
                    },
                },
                {
                    "text": "视而不见「当作没看到」",
                    "stat_req": None,
                    "success": {
                        "narration": "你摇摇头，转身离开。\n\n有些事情，眼不见为净。领主也不是什么都要管的。",
                        "effects": [],
                    },
                    "failure": None,
                },
            ],
        },

        "refugee_plea": {
            "id": "refugee_plea",
            "title": "难民求助",
            "category": "trade",
            "icon": "心",
            "icon_color": "#3498db",
            "rarity": 22,
            "min_chapter": 1,
            "max_chapter": 5,
            "conditions": {},
            "context": ["travel", "rest"],
            "description": "城门口聚集了一群衣衫褴褛的人。他们是从邻近领地逃来的难民——男爵的征税让他们失去了一切。\n\n一位年迈的妇人跪在你面前，声泪俱下：「大人，求您收留我们！我们愿意做牛做马，只求一口饭吃……」\n\n她身后的难民们都跪了下来，数十双绝望的眼睛看着你。",
            "choices": [
                {
                    "text": "慷慨收留「安置难民」",
                    "stat_req": None,
                    "success": {
                        "narration": "你下令打开粮仓，拿出布匹和食物分给难民。你在领地西侧划出一片荒地，让他们开垦定居。\n\n「从今天起，你们就是艾登堡的子民。」\n\n难民们痛哭失声，叩头不止。这个冬天，因为你的善举，数十条人命得以延续。\n\n消息传开后，越来越多的人称赞你是一位仁慈的领主。",
                        "effects": [("stat", "wealth", -10), ("stat", "loyalty", 10), ("stat", "faith", 15), ("stat", "reputation", 8)],
                    },
                    "failure": None,
                },
                {
                    "text": "有限帮助「给些食物但不收留」",
                    "stat_req": None,
                    "success": {
                        "narration": "你让人拿出一些食物和旧衣物分给难民，但解释说领地目前无力接纳这么多人。\n\n「去南方吧，那里冬天不会太冷。这些食物够你们走上几天。」\n\n难民们虽然失望，但还是感激地道了谢。你既没有耗费太多资源，也没有完全袖手旁观。",
                        "effects": [("stat", "wealth", -3), ("stat", "loyalty", 3), ("stat", "faith", 6)],
                    },
                    "failure": None,
                },
                {
                    "text": "驱赶难民「领地不能容纳更多人」",
                    "stat_req": None,
                    "success": {
                        "narration": "你冷着脸下令：「艾登堡的粮食只够养活自己的子民。让他们走。」\n\n侍卫将难民驱散。老妇人被推倒在地，绝望地哭喊。你转过身去，不再看那些恳求的眼神。\n\n有时候，做领主就意味着做艰难的选择。但你心里明白，这个选择会留下代价。",
                        "effects": [("stat", "loyalty", -5), ("stat", "faith", -5), ("stat", "reputation", -8)],
                    },
                    "failure": None,
                },
            ],
        },

        ## ────────────────────────────────────────
        ## 3. 情报事件 (Intelligence Events)
        ## ────────────────────────────────────────

        "tavern_rumors": {
            "id": "tavern_rumors",
            "title": "酒馆传闻",
            "category": "intelligence",
            "icon": "刃",
            "icon_color": "#8e44ad",
            "rarity": 25,
            "min_chapter": 1,
            "max_chapter": 5,
            "conditions": {},
            "context": ["rest", "explore"],
            "description": "你在酒馆角落里坐下，要了一杯麦酒。\n\n酒馆里嘈杂热闹，各种消息在酒杯之间流转。你竖起耳朵，听到了几段有趣的对话……\n\n一个喝醉的商人在高谈阔论，旁边桌上两个穿斗篷的人在低声密谈。",
            "choices": [
                {
                    "text": "偷听商人「商业情报」",
                    "stat_req": None,
                    "success": {
                        "narration": "那个喝醉的商人在吹嘘自己如何在东方港口赚了一笔。\n\n你从他的醉话中拼凑出有用的信息——东方的丝绸之路近期会开通新的贸易线。如果提前布局，可以大赚一笔。\n\n你暗暗记下了这个情报。",
                        "effects": [("stat", "wealth", 20), ("stat", "intrigue", 3)],
                    },
                    "failure": None,
                },
                {
                    "text": "偷听密谈「政治情报」",
                    "stat_req": ("intrigue", 25),
                    "success": {
                        "narration": "你装作漫不经心地移到了两个斗篷人附近。\n\n断断续续的对话中，你听到了几个关键词：「王后」「密约」「北境」「春天之前」。\n\n这些人显然在讨论一个秘密计划。你记住了他们的面容，以备将来之用。",
                        "effects": [("stat", "intrigue", 4), ("stat", "reputation", 2)],
                    },
                    "failure": {
                        "narration": "你试图靠近偷听，但那两个人警觉地看了你一眼，立刻起身离开了。\n\n你只捕捉到了一个词——「暗百合」。具体含义不得而知。",
                        "effects": [("stat", "intrigue", 3)],
                    },
                },
                {
                    "text": "主动套话「与酒客交谈」",
                    "stat_req": ("reputation", 30),
                    "success": {
                        "narration": "你以旅人的身份坐到了一桌老手那中间，买了一轮酒。\n\n酒过三巡，话匣子打开了。他们告诉你：男爵最近在秘密招兵，教会派了密使去王都，北方的部落蠢蠢欲动。\n\n这些零碎的消息串联起来，构成了一幅令人不安的画面。",
                        "effects": [("stat", "intrigue", 3), ("stat", "wealth", -2)],
                    },
                    "failure": {
                        "narration": "你买了几轮酒，但这些老油条嘴比蚌还紧。你只得到了一些无关紧要的八卦。\n\n白花了酒钱。",
                        "effects": [("stat", "wealth", -3), ("stat", "intrigue", 1)],
                    },
                },
            ],
        },

        "intercepted_letter": {
            "id": "intercepted_letter",
            "title": "密信截获",
            "category": "intelligence",
            "icon": "卷",
            "icon_color": "#9b59b6",
            "rarity": 12,
            "min_chapter": 2,
            "max_chapter": 5,
            "conditions": {"intrigue_min": 40},
            "context": ["rest", "explore"],
            "description": "你的斥候截获了一名信使，从他身上搜出一封用蜡封的密信。\n\n封蜡上的印记你不认识——既不是男爵家的鸢尾花，也不是教会的十字架。\n\n打开还是不打开？这是个问题。拆开他人密信是严重的违规行为，但这封信可能包含重要情报。",
            "choices": [
                {
                    "text": "拆开密信「情报优先」",
                    "stat_req": None,
                    "success": {
                        "narration": "你小心地用热刀融化封蜡，取出信纸。\n\n信是用暗语写的，但你凭借在修道院学到的密码学知识，花了半个时辰破译了大部分内容。\n\n信中提到了一个计划——有人打算在下次领主会议上对你发难，指控你侵吞教会财产。\n\n你将信重新封好，派人将信使放走。有了这个情报，你可以提前做好准备。",
                        "effects": [("stat", "intrigue", 3), ("stat", "reputation", -3)],
                    },
                    "failure": None,
                },
                {
                    "text": "转交教会「交给主教处理」",
                    "stat_req": None,
                    "success": {
                        "narration": "你原封不动地将密信送到主教马修斯手中。\n\n主教沉吟良久，最终向你透露：「这封信来自王都的某个势力。感谢你的忠诚，[player_name]。作为回报，我告诉你一件事——男爵最近在秘密与北方部落接触。」\n\n这个情报比那封信本身更有价值。",
                        "effects": [("stat", "faith", 15), ("stat", "intrigue", 3), ("rel", "rel_bishop", 8)],
                    },
                    "failure": None,
                },
                {
                    "text": "销毁密信「此事不宜介入」",
                    "stat_req": None,
                    "success": {
                        "narration": "你将密信投入火中，看着它化为灰烬。\n\n「什么也没有截获。」你对斥候说，「放那个信使走。」\n\n有些秘密，知道得越少越安全。",
                        "effects": [("stat", "intrigue", 2)],
                    },
                    "failure": None,
                },
            ],
        },

        "dark_lily_clue": {
            "id": "dark_lily_clue",
            "title": "暗百合线索",
            "category": "intelligence",
            "icon": "刃",
            "icon_color": "#2d1b4e",
            "rarity": 7,
            "min_chapter": 3,
            "max_chapter": 5,
            "conditions": {},
            "context": ["explore", "rest"],
            "description": "你在城堡地下室整理旧物时，发现了一个暗格。里面放着一本泛黄的笔记本。\n\n翻开一看，你的心猛然一紧——这是你父亲的笔迹。\n\n笔记本上记录着一些零碎的信息：日期、人名、地点，还有一个反复出现的符号——一朵六瓣的黑色百合花。",
            "choices": [
                {
                    "text": "仔细研究「破译笔记」",
                    "stat_req": ("intrigue", 35),
                    "success": {
                        "narration": "你花了整整一夜研究父亲的笔记。\n\n笔记中提到了一个叫「花园」的组织，以及几个化名——「园丁」「浇水人」「修剪者」。这些代号对应的真实身份，父亲似乎只破解了一部分。\n\n但最后几页的内容让你不寒而栗：「若我遭遇不测，去找修道院院长。他知道真相的一半。」\n\n父亲早已预感到了危险。",
                        "effects": [("stat", "intrigue", 3), ("flag", "father_letters_found", True)],
                    },
                    "failure": {
                        "narration": "你仔细阅读了笔记，但父亲使用了太多暗语和缩写，你只能理解其中的片段。\n\n不过，有一段话很清楚：「暗百合不是敌人，也不是朋友。它是一面镜子。」\n\n这句话的含义，你需要时间去理解。",
                        "effects": [("stat", "intrigue", 3)],
                    },
                },
                {
                    "text": "告诉奥尔德里克「让管家看看」",
                    "stat_req": None,
                    "success": {
                        "narration": "奥尔德里克接过笔记本，老手微微颤抖。\n\n「这确实是老领主的笔迹……」他的老手微微颤抖。然后他抬头看着你，眼中有泪光，「少主，你父亲……他在调查一件危险的事。请你务必小心。」\n\n他没有说更多，但你感觉到他知道的比他说的多。",
                        "effects": [("stat", "intrigue", 3), ("rel", "rel_aldric", 8)],
                    },
                    "failure": None,
                },
                {
                    "text": "锁回暗格「时机未到」",
                    "stat_req": None,
                    "success": {
                        "narration": "你将笔记本放回暗格，重新封好。\n\n有些真相需要在正确的时机揭开。现在，你还没有足够的力量来应对可能的后果。\n\n但你记住了暗格的位置。",
                        "effects": [("stat", "intrigue", 2)],
                    },
                    "failure": None,
                },
            ],
        },

        "spy_exposed": {
            "id": "spy_exposed",
            "title": "间谍暴露",
            "category": "intelligence",
            "icon": "刃",
            "icon_color": "#c0392b",
            "rarity": 13,
            "min_chapter": 2,
            "max_chapter": 5,
            "conditions": {"flag_spy_network": True},
            "context": ["rest"],
            "description": "你收到了间谍网络的紧急密报：你安插在男爵领地的一名眼线身份暴露了。\n\n男爵的人已经抓住了他，正在严刑逼供。如果他供出你的间谍网络，后果不堪设想。",
            "choices": [
                {
                    "text": "营救间谍「派人劫狱」",
                    "stat_req": ("power", 35),
                    "success": {
                        "narration": "你紧急派出一支精锐小队，在夜间潜入男爵的城堡，成功救出了你的间谍。\n\n虽然行动惊动了男爵的守卫，但你的人成功脱身。你的间谍重伤但还活着，而且——他没有供出任何人。\n\n「少主……我没有背叛您。」他虚弱地说。\n\n你的间谍网络安然无恙。",
                        "effects": [("stat", "intrigue", 3), ("stat", "power", 3), ("stat", "loyalty", 5), ("rel", "rel_baron", -10)],
                    },
                    "failure": {
                        "narration": "营救行动失败了。你的人被男爵的守卫发现并击退。\n\n更糟糕的是，男爵现在知道你在他的领地安插了间谍。虽然你的间谍至死没有供出更多人，但关系已经恶化。",
                        "effects": [("stat", "power", -5), ("stat", "intrigue", -3), ("rel", "rel_baron", -15)],
                    },
                },
                {
                    "text": "切断联系「壮士断腕」",
                    "stat_req": None,
                    "success": {
                        "narration": "你咬紧牙关，下令切断与那名间谍的一切联系，销毁所有相关证据。\n\n那个人……将独自承受一切。\n\n三天后，你听说男爵领地处决了一名「窃贼」。你默默地记住了这个名字。\n\n间谍网络的其余部分得以保全。代价是一个忠诚的人和你心头永远的愧疚。",
                        "effects": [("stat", "intrigue", 3), ("stat", "loyalty", -5)],
                    },
                    "failure": None,
                },
                {
                    "text": "外交斡旋「以谈判解决」",
                    "stat_req": ("intrigue", 50),
                    "success": {
                        "narration": "你主动派使者前往男爵领地，声称抓到的人是你的一名逃跑的家仆，请求交还。\n\n你还附上了一份「赔礼」——一箱上好的葡萄酒和一封措辞得体的信。\n\n男爵虽然心存疑虑，但没有确凿证据证明那人是间谍。在利益和体面的考量下，他同意将人交还。\n\n你的间谍回来了，间谍网络安然无恙，而男爵还觉得你「很有诚意」。",
                        "effects": [("stat", "intrigue", 4), ("stat", "wealth", -5), ("stat", "reputation", 3)],
                    },
                    "failure": {
                        "narration": "你的外交手段没能说服男爵。他冷笑着拒绝了你的使者：「间谍就是间谍，别以为我不知道。」\n\n虽然他没有进一步追查，但你和男爵的关系更加紧张了。",
                        "effects": [("stat", "wealth", -3), ("stat", "intrigue", 2), ("rel", "rel_baron", -8)],
                    },
                },
            ],
        },

        ## ────────────────────────────────────────
        ## 4. 角色事件 (Character Events)
        ## ────────────────────────────────────────

        "aldric_memory": {
            "id": "aldric_memory",
            "title": "奥尔德里克的回忆",
            "category": "character",
            "icon": "心",
            "icon_color": "#8b0000",
            "rarity": 14,
            "min_chapter": 1,
            "max_chapter": 5,
            "conditions": {"rel_aldric_min": 30},
            "context": ["rest"],
            "description": "深夜，你路过大厅时，发现奥尔德里克独自坐在壁炉前。\n\n火光映照着他苍老的面容，他手中握着一枚旧银币，眼中有些迷离。\n\n他似乎在回忆什么遥远的事情。",
            "choices": [
                {
                    "text": "坐下聆听「听他讲述往事」",
                    "stat_req": None,
                    "success": {
                        "narration": "你在他身旁坐下。奥尔德里克愣了一下，然后露出一个苦涩的微笑。\n\n「少主……你父亲年轻时，也常在这个位置坐着。」\n\n他开始讲述你父亲年轻时的故事——那个骑着马、挥着剑、意气风发的年轻领主。他讲到你父亲如何在一场大雪中徒步走了三天去救一个被困的农夫，讲到你父亲第一次上战场时吓得发抖但还是冲了上去。\n\n「他不是天生的强者，」奥尔德里克的声音颤抖了，「但他选择成为一个好人。这比天赋更难。」\n\n你们在壁炉旁坐了很久，直到火焰熄灭。",
                        "effects": [("stat", "loyalty", 5), ("rel", "rel_aldric", 10)],
                    },
                    "failure": None,
                },
                {
                    "text": "询问父亲「追问父亲的秘密」",
                    "stat_req": ("intrigue", 30),
                    "success": {
                        "narration": "你直接问道：「奥尔德里克，我父亲……是否有什么事瞒着所有人？」\n\n壁炉里的柴火发出噼啪声。\n\n终于，他低声说：「你父亲在去世前几个月，行为变得很奇怪。他经常深夜一个人去书房，有时候天亮才出来。他让我准备了一个暗格……还让我记住一个词——'花园的钥匙在修道院'。」\n\n他看着你：「少主，我不知道这意味着什么。但你父亲说过，如果他出了事，要把这句话告诉你。」",
                        "effects": [("stat", "intrigue", 4), ("rel", "rel_aldric", 5)],
                    },
                    "failure": {
                        "narration": "奥尔德里克摇了摇头：「有些事……时候未到，少主。请再给老臣一些时间。」\n\n他起身离去，留你独自面对渐渐熄灭的壁炉。",
                        "effects": [("rel", "rel_aldric", 3)],
                    },
                },
                {
                    "text": "默默离开「给他独处的空间」",
                    "stat_req": None,
                    "success": {
                        "narration": "你悄悄退了出去，没有打扰他。\n\n每个人都有需要独自面对的回忆。作为领主，你也理解孤独的重量。",
                        "effects": [("rel", "rel_aldric", 3)],
                    },
                    "failure": None,
                },
            ],
        },

        "elena_secret": {
            "id": "elena_secret",
            "title": "艾琳娜的秘密",
            "category": "character",
            "icon": "心",
            "icon_color": "#9370db",
            "rarity": 8,
            "min_chapter": 2,
            "max_chapter": 5,
            "conditions": {"rel_elena_min": 40},
            "context": ["rest", "explore"],
            "description": "你在花园中散步时，发现艾琳娜正蹲在一丛玫瑰前，小心翼翼地为一只受伤的雏鸟包扎翅膀。\n\n她没有注意到你的到来。你看到她的眼神异常温柔——与平时那个冷静、精明的侍女判若两人。\n\n雏鸟在她手心安静下来，似乎感受到了她的善意。",
            "choices": [
                {
                    "text": "走近搭话「你很擅长照顾弱小」",
                    "stat_req": None,
                    "success": {
                        "narration": "艾琳娜吃了一惊，差点弄掉手中的雏鸟。她迅速恢复了平日的从容，但你捕捉到了她脸上一闪而过的红晕。\n\n「只是……看到了就忍不住。」她低声说。\n\n你在她身旁坐下，帮她稳住雏鸟。你们的手指不经意间触碰了一下。\n\n「你知道吗，」她突然说，「我小时候也是一只受伤的鸟。是你的父亲把我从泥泞中捡了起来。所以……」\n\n她没有说完，但你懂了。",
                        "effects": [("rel", "rel_elena", 10), ("stat", "loyalty", 3)],
                    },
                    "failure": None,
                },
                {
                    "text": "静静观察「不打扰她」",
                    "stat_req": None,
                    "success": {
                        "narration": "你倚在柱子旁，默默看着她。\n\n阳光穿过花园的藤蔓，洒在她的肩头。这一刻，你看到的不是那个在阴影中穿梭的侍女，而是一个柔软的、真实的人。\n\n她将雏鸟放到鸟巢中，转身时终于发现了你。她的目光与你对视了一瞬，然后微微点头，脸上带着一抹淡淡的笑意——你从未在她脸上见过这样的笑。\n\n她走过你身旁时低声说了句：「谢谢你没有打扰。」",
                        "effects": [("rel", "rel_elena", 8)],
                    },
                    "failure": None,
                },
                {
                    "text": "直接询问「你的过去是什么」",
                    "stat_req": ("intrigue", 45),
                    "success": {
                        "narration": "你走过去，直接问道：「艾琳娜，你到底是谁？一个侍女不该有你这样的眼神。」\n\n她的手停在半空中，眼中闪过一丝警惕——然后是释然。\n\n「你果然看出来了。」她站起身，直视着你。\n\n「我不是普通的侍女。在来到艾登堡之前，我是暗百合培养的探子。你的父亲知道这件事，他说——'留在我身边，比留在暗影中安全。'」\n\n「我欠你父亲一条命。所以我现在守护你。」\n\n她的坦白让你对她的了解又深了一层。",
                        "effects": [("rel", "rel_elena", 15), ("stat", "intrigue", 3)],
                    },
                    "failure": {
                        "narration": "你的直接让艾琳娜警觉了。她脸上的柔软瞬间消失，取而代之的是一堵无形的墙。\n\n「我只是一个侍女。」她冷冷地说，转身离去。\n\n雏鸟在花丛中孤零零地叫着。",
                        "effects": [("rel", "rel_elena", -3)],
                    },
                },
            ],
        },

        "captain_training": {
            "id": "captain_training",
            "title": "队长训练",
            "category": "character",
            "icon": "剑",
            "icon_color": "#4682b4",
            "rarity": 20,
            "min_chapter": 1,
            "max_chapter": 5,
            "conditions": {"power_min": 30},
            "context": ["rest"],
            "description": "清晨，你经过练武场时，看到队长雷恩正在指导新兵训练。\n\n他的动作干脆利落，每一招都带着实战的杀气。看到你来了，他停下动作，朝你点头致意。\n\n「领主大人，要不要来比划两下？」他的眼中带着期待。",
            "choices": [
                {
                    "text": "接受训练「与队长切磋」",
                    "stat_req": None,
                    "success": {
                        "narration": "你脱下外衣，拿起一柄训练用木剑。\n\n雷恩毫不留情——他的攻击又快又重，你几次差点被打中要害。但在他的指点下，你的脚步渐渐稳了下来，出剑的时机也越来越精准。\n\n一个时辰后，你浑身酸痛，但确实进步了不少。\n\n雷恩满意地点头：「领主大人的进步很快。再练三个月，可以上战场了。」\n\n新兵们在旁边看得目瞪口呆——他们的领主亲自下场训练，这份气魄让他们士气大振。",
                        "effects": [("stat", "power", 8), ("rel", "rel_captain", 5), ("stat", "loyalty", 3)],
                    },
                    "failure": None,
                },
                {
                    "text": "观看训练「学习指挥」",
                    "stat_req": None,
                    "success": {
                        "narration": "你站在一旁，仔细观察雷恩的训练方法。\n\n他将士兵分成小队，让他们反复演练阵型变换。你注意到他特别注重士兵之间的配合——「一个人的力量有限，」他说，「但一支训练有素的队伍，可以击败十倍的敌人。」\n\n你从中学到了不少用兵之道。",
                        "effects": [("stat", "power", 3), ("stat", "intrigue", 3), ("rel", "rel_captain", 3)],
                    },
                    "failure": None,
                },
            ],
        },

        "bishop_blessing": {
            "id": "bishop_blessing",
            "title": "主教祝福",
            "category": "character",
            "icon": "十",
            "icon_color": "#ffd700",
            "rarity": 15,
            "min_chapter": 1,
            "max_chapter": 5,
            "conditions": {"faith_min": 40},
            "context": ["rest"],
            "description": "你前往教堂做晚祷时，发现主教马修斯正独自跪在圣坛前。\n\n听到你的脚步声，他缓缓起身，转过身来。他的面容比平时更加慈祥，仿佛刚刚与神完成了一次对话。\n\n「孩子，你来了。」他微笑着说，「也许这是天主的安排。」",
            "choices": [
                {
                    "text": "请求祝福「寻求精神上的指引」",
                    "stat_req": None,
                    "success": {
                        "narration": "你跪在主教面前。他将手轻轻放在你的头顶，口中念诵着古老的祈祷文。\n\n一股温暖从头顶蔓延到全身，你感到疲惫和焦虑都在逐渐消散。\n\n「天主会指引你走正确的路。」马修斯说，「但你必须记住——权力是为了守护，不是为了征服。」\n\n你站起身来，感觉焕然一新。",
                        "effects": [("stat", "faith", 12), ("rel", "rel_bishop", 5), ("stat", "loyalty", 3)],
                    },
                    "failure": None,
                },
                {
                    "text": "倾诉困惑「向主教诉说烦恼」",
                    "stat_req": None,
                    "success": {
                        "narration": "你坐在教堂的长椅上，将心中的迷茫和困惑倾诉给主教。\n\n关于父亲的死，关于领地的困境，关于那些你必须做出但永远不知道是否正确的选择。\n\n马修斯耐心地听完。\n\n「我不能告诉你什么是对的，」他说，「但我可以告诉你——你的父亲也曾有过同样的困惑。能够困惑的人，说明他还在思考。不再困惑的人……才真正危险。」\n\n简单的话，却给了你莫大的安慰。",
                        "effects": [("stat", "faith", 15), ("rel", "rel_bishop", 8), ("stat", "intrigue", 2)],
                    },
                    "failure": None,
                },
                {
                    "text": "恭敬告退「不打扰主教祈祷」",
                    "stat_req": None,
                    "success": {
                        "narration": "你行了一礼，悄然退出了教堂。\n\n有些安宁只属于信仰。",
                        "effects": [("stat", "faith", 6), ("rel", "rel_bishop", 2)],
                    },
                    "failure": None,
                },
            ],
        },

        ## ────────────────────────────────────────
        ## 5. 危机事件 (Crisis Events)
        ## ────────────────────────────────────────

        "plague_outbreak": {
            "id": "plague_outbreak",
            "title": "瘟疫来袭",
            "category": "crisis",
            "icon": "!",
            "icon_color": "#e74c3c",
            "rarity": 6,
            "min_chapter": 2,
            "max_chapter": 5,
            "conditions": {},
            "context": ["rest"],
            "description": "「领主大人！大事不好！」\n\n侍从冲进大厅，脸色惨白：「村庄里爆发了瘟疫！已有数十人发病，三人死亡。村民们恐慌至极，有人已经开始逃亡！」\n\n瘟疫——这个可怕的词语让大厅里所有人都沉默了。\n\n如何应对这场灾难，将考验你作为领主的智慧和决断。",
            "choices": [
                {
                    "text": "倾全力救治「动用财富抗疫」",
                    "stat_req": None,
                    "success": {
                        "narration": "你立即下令：封锁病区、征用药材、雇请所有能找到的医师。你从自己的金库中拿出大笔资金购买药物和食物。\n\n你甚至亲自前往病区视察，给病人们带去了极大的鼓舞。\n\n在你的全力以赴下，瘟疫在两周内得到了控制。虽然付出了巨大的经济代价，但你挽救了数百条人命。\n\n「领主大人是天使！」幸存者们含泪说道。",
                        "effects": [("stat", "wealth", -15), ("stat", "loyalty", 15), ("stat", "faith", 15), ("stat", "reputation", 10)],
                    },
                    "failure": None,
                },
                {
                    "text": "祈求教会「请主教举行祈祷」",
                    "stat_req": ("faith", 40),
                    "success": {
                        "narration": "你前往教堂请求主教的帮助。马修斯立即行动，组织教会的治愈修士前往病区。\n\n修士们精通草药学，他们配制的药方很快见了效。同时，主教在大教堂举行了盛大的祈祷仪式，安抚了恐慌的民心。\n\n虽然你需要向教会捐献一笔不菲的「感恩奉献」，但这场瘟疫最终被控制住了。教会的声望在领地中大大提高。",
                        "effects": [("stat", "wealth", -8), ("stat", "faith", 15), ("stat", "loyalty", 8), ("rel", "rel_bishop", 10)],
                    },
                    "failure": {
                        "narration": "主教派来了修士，但瘟疫的凶猛超出了预期。仅靠祈祷和草药难以完全控制。\n\n最终，你不得不追加投入更多资金才勉强控制住疫情。",
                        "effects": [("stat", "wealth", -12), ("stat", "faith", 15), ("stat", "loyalty", 5), ("rel", "rel_bishop", 5)],
                    },
                },
                {
                    "text": "封锁隔离「牺牲少数保全多数」",
                    "stat_req": None,
                    "success": {
                        "narration": "你做出了残酷但可能最理性的决定：彻底封锁病区，禁止任何人进出。\n\n哭喊声从封锁线内传来，病区里的人拍打着栅栏求救。你的士兵们面色铁青，但执行了你的命令。\n\n十天后，病区内的感染者不再增加。瘟疫被困在了那片区域里，最终消亡。代价是病区内三十多人全部死亡。\n\n你保全了大多数人的性命，但那些死者的家属，可能永远不会原谅你。",
                        "effects": [("stat", "loyalty", -10), ("stat", "reputation", -8), ("stat", "intrigue", 3), ("stat", "power", 5)],
                    },
                    "failure": None,
                },
            ],
        },

        "rebellion_signs": {
            "id": "rebellion_signs",
            "title": "叛乱苗头",
            "category": "crisis",
            "icon": "!",
            "icon_color": "#e67e22",
            "rarity": 12,
            "min_chapter": 2,
            "max_chapter": 5,
            "conditions": {"loyalty_max": 40},
            "context": ["rest"],
            "description": "队长雷恩匆匆赶来，神色严峻：\n\n「领主大人，我们截获情报——领地南部的农民正在秘密集会。有人在煽动他们，说您的统治不配为领主。」\n\n「他们还没有公开行动，但照这个势头发展下去，恐怕不出一月就会爆发叛乱。」\n\n你必须在事态扩大之前做出反应。",
            "choices": [
                {
                    "text": "安抚民心「减税并发放粮食」",
                    "stat_req": None,
                    "success": {
                        "narration": "你立即宣布减免今年的赋税，并打开粮仓向南部村庄发放救济粮。\n\n你还亲自前往南部，走访了几个村庄。你蹲在田间地头，听农民们诉说生活的艰辛。\n\n「我知道我做得不够好，」你站在村民面前说，「但请给我时间。我父亲守护这片土地三十年，我也会的。」\n\n你的诚意感动了大部分人。集会渐渐散去，叛乱的种子被扼杀在了萌芽中。",
                        "effects": [("stat", "wealth", -10), ("stat", "loyalty", 12), ("stat", "reputation", 5)],
                    },
                    "failure": None,
                },
                {
                    "text": "铁腕镇压「抓捕煽动者」",
                    "stat_req": ("power", 40),
                    "success": {
                        "narration": "你派出士兵，在夜间突袭了秘密集会的地点，逮捕了三名主要煽动者。\n\n经审讯发现，其中一人竟然是男爵安插的密探，专门来制造混乱。你将此事公之于众，民怨转为对男爵的愤怒。\n\n煽动者被处以流放，叛乱的苗头被彻底铲除。但你高压手段的名声也传了开去。",
                        "effects": [("stat", "power", 8), ("stat", "loyalty", 3), ("stat", "reputation", -5), ("stat", "intrigue", 3)],
                    },
                    "failure": {
                        "narration": "你的镇压行动不够迅速——煽动者提前得到了风声，四散逃走。\n\n虽然集会被驱散，但那些种子已经撒下。你的高压姿态反而让更多人心生不满。",
                        "effects": [("stat", "power", 3), ("stat", "loyalty", -5), ("stat", "reputation", -3)],
                    },
                },
                {
                    "text": "暗中调查「找出幕后黑手」",
                    "stat_req": ("intrigue", 40),
                    "success": {
                        "narration": "你没有急于行动，而是派出间谍混入集会，摸清幕后的真相。\n\n调查结果让你大吃一惊：煽动者并非来自外部，而是领地内一个不满你的小贵族——曾在你父亲手下任职的骑士长。他认为自己更有资格继承领地。\n\n你私下约见了这位骑士长，将他的阴谋一一揭穿。在威逼利诱下，他被迫效忠于你，并亲自出面平息了农民的不满。\n\n「从今以后，你为我所用。」你冷冷地说。",
                        "effects": [("stat", "intrigue", 3), ("stat", "loyalty", 5), ("stat", "power", 3)],
                    },
                    "failure": {
                        "narration": "调查进展缓慢，而叛乱的苗头每天都在生长。\n\n你不得不在调查未果的情况下采取行动，同时安抚和施压，勉强稳住了局面。但幕后黑手仍然逍遥法外。",
                        "effects": [("stat", "intrigue", 3), ("stat", "loyalty", 2), ("stat", "wealth", -5)],
                    },
                },
            ],
        },

        "assassination_warning": {
            "id": "assassination_warning",
            "title": "暗杀警告",
            "category": "crisis",
            "icon": "!",
            "icon_color": "#2d1b4e",
            "rarity": 6,
            "min_chapter": 4,
            "max_chapter": 5,
            "conditions": {},
            "context": ["rest"],
            "description": "深夜，一张纸条被人从窗缝塞进你的房间。\n\n上面只有一行字：「三日内，有人要取你性命。信此言者，活。不信者，死。——一个不愿看到你死的人」\n\n你无法判断这是真是假，但也无法无视它。",
            "choices": [
                {
                    "text": "加强防卫「全面戒备」",
                    "stat_req": None,
                    "success": {
                        "narration": "你立即召集队长雷恩，命令加强城堡防卫，所有出入口增设哨兵，你的寝室更换到隐蔽的位置。\n\n第二天夜里，果然有人潜入了你原来的寝室。等待他们的是雷恩和十名精锐卫兵的埋伏。\n\n刺客被当场擒获。审讯后发现，幕后主使竟然是……一个你意想不到的人。\n\n那张纸条救了你的命。",
                        "effects": [("stat", "power", 5), ("stat", "intrigue", 3), ("stat", "loyalty", 3), ("rel", "rel_captain", 5)],
                    },
                    "failure": None,
                },
                {
                    "text": "设下陷阱「将计就计」",
                    "stat_req": ("intrigue", 55),
                    "success": {
                        "narration": "你不动声色地做了两手准备：表面上一切如常，暗中却布下了天罗地网。\n\n你故意在饮食中「暴露」了一个破绽，引诱暗杀者在你的晚宴上下手。当侍者端上一杯被下了毒的酒时，你当众揭露了这一阴谋。\n\n在场的所有人都被你的冷静和智慧震撼了。暗杀者的同伙在混乱中暴露，被你的人一网打尽。\n\n「在我的地盘上动手？」你举起干净的酒杯，「太天真了。」",
                        "effects": [("stat", "intrigue", 6), ("stat", "reputation", 8), ("stat", "power", 5)],
                    },
                    "failure": {
                        "narration": "你布下了陷阱，但暗杀者比你想象的更加小心。他们识破了你的计划，改用了另一种方式。\n\n所幸你的防备并非全无用处——侍卫及时挡住了偷袭。你只是受了轻伤，但暗杀者趁乱逃脱。",
                        "effects": [("stat", "intrigue", 3), ("stat", "power", -3)],
                    },
                },
                {
                    "text": "追查线索「寻找纸条的来源」",
                    "stat_req": ("intrigue", 45),
                    "success": {
                        "narration": "你仔细检查纸条——纸张的质地、墨水的气味、折叠的方式。\n\n这种纸只有教堂的抄写室使用。墨水中带有一丝薰衣草的香气——那是只有一个人才会用的香料。\n\n艾琳娜。\n\n你找到她时，她只是静静地看着你：「我说过，我会守护你。」\n\n你没有追问更多。但从这一刻起，你知道了一件事——在这座城堡里，至少有一个人是真心站在你这边的。",
                        "effects": [("stat", "intrigue", 4), ("rel", "rel_elena", 10)],
                    },
                    "failure": {
                        "narration": "你花了很多时间追查线索，但纸条的来源如同石沉大海。\n\n三天过去了，暗杀并没有发生。也许那只是一场虚惊——又或者，你的追查本身就吓退了暗杀者。",
                        "effects": [("stat", "intrigue", 3)],
                    },
                },
            ],
        },

        "border_skirmish": {
            "id": "border_skirmish",
            "title": "边境冲突",
            "category": "crisis",
            "icon": "剑",
            "icon_color": "#e74c3c",
            "rarity": 20,
            "min_chapter": 2,
            "max_chapter": 5,
            "conditions": {},
            "context": ["travel", "rest"],
            "description": "前线传来急报：男爵的巡逻队越过了边境线，与你的守军发生了冲突。双方各有伤亡。\n\n「男爵声称是我们的巡逻队先越界的，」队长雷恩汇报道，「但据我方士兵说，是男爵的人先动的手。」\n\n局势一触即发。如何处理这件事，将影响你与男爵的关系，也可能影响整个领地的安全。",
            "choices": [
                {
                    "text": "强硬回应「增兵边境」",
                    "stat_req": ("power", 35),
                    "success": {
                        "narration": "你下令将边境守军增加一倍，并派出斥候严密监视男爵的动向。\n\n同时，你通过外交渠道发出警告：「再有越界行为，后果自负。」\n\n男爵显然没想到你会如此强硬。他的巡逻队悄悄撤回了边境线以内。短期内，边境恢复了平静。\n\n但你知道，这只是暂时的。",
                        "effects": [("stat", "power", 8), ("stat", "wealth", -5), ("rel", "rel_baron", -8), ("stat", "reputation", 3)],
                    },
                    "failure": {
                        "narration": "你的增兵行动反而激化了冲突。男爵也增加了边境兵力，双方在边境线上剑拔弩张。\n\n虽然最终没有爆发大规模战斗，但紧张的局势消耗了你大量的资源。",
                        "effects": [("stat", "power", 3), ("stat", "wealth", -8), ("rel", "rel_baron", -12)],
                    },
                },
                {
                    "text": "外交解决「派遣使者谈判」",
                    "stat_req": ("reputation", 35),
                    "success": {
                        "narration": "你派出了一位能言善辩的使者，携带你的亲笔信前往男爵领地。\n\n信中你提议：双方各退一步，在边境线设立共同巡逻机制，避免类似冲突再次发生。\n\n出人意料的是，男爵同意了。也许他也不想在这个时候开战。\n\n双方在边境镇召开了一次会面，签订了临时停火协议。不是长久之计，不过喘息的时间争取到了。",
                        "effects": [("stat", "reputation", 8), ("stat", "intrigue", 3), ("rel", "rel_baron", 5)],
                    },
                    "failure": {
                        "narration": "你的使者被男爵冷落了三天才见到面。谈判毫无成果——男爵态度傲慢，要求你公开道歉并赔偿损失。\n\n使者只好空手而返。外交手段暂时失败了。",
                        "effects": [("stat", "reputation", -3), ("rel", "rel_baron", -5)],
                    },
                },
                {
                    "text": "按兵不动「冷处理」",
                    "stat_req": None,
                    "success": {
                        "narration": "你决定不做任何公开回应，只是悄悄加强了边防。\n\n没有激烈的反应，男爵也找不到继续挑衅的借口。冲突像一阵风一样，来得快去得也快。\n\n但你的一些将领对这种「软弱」的态度颇有微词。",
                        "effects": [("stat", "loyalty", -3), ("stat", "intrigue", 3)],
                    },
                    "failure": None,
                },
            ],
        },

        ## ────────────────────────────────────────
        ## 7. 政治风波 (Political Events)
        ## ────────────────────────────────────────

        "noble_petition": {
            "id": "noble_petition",
            "title": "贵族请愿",
            "category": "political",
            "icon": "书",
            "icon_color": "#8b4513",
            "rarity": 22,
            "min_chapter": 2,
            "max_chapter": 5,
            "conditions": {},
            "context": ["rest", "explore"],
            "description": "三位小贵族联名上书，请求你裁决一桩土地纠纷。两家都声称祖上曾获得同一片林地的封赐，拿出的文书各执一词。\n\n他们已经闹了三代人了。你父亲在世时一直搁置不理，现在他们把希望寄托在了新领主身上。",
            "choices": [
                {
                    "text": "判给实际耕种的一方「尊重事实」",
                    "stat_req": None,
                    "success": {
                        "narration": "你仔细调查后发现，虽然文书争议不断，但实际上只有布伦家族在这片土地上耕种了三十年。\n\n你当众裁定土地归布伦家族所有，但要求他们每年向另一方支付一笔补偿金。\n\n两家虽都不完全满意，但这个判决被其他领主认为公正合理。",
                        "effects": [("stat", "reputation", 8), ("stat", "loyalty", 3)],
                    },
                    "failure": None,
                },
                {
                    "text": "平分土地「各退一步」",
                    "stat_req": None,
                    "success": {
                        "narration": "你将林地一分为二，两家各得一半。\n\n看似公平的判决，却让两方都不满意——都觉得自己才是合法的全部所有者。你的随从私下告诉你，两家都在背后说你「和稀泥」。",
                        "effects": [("stat", "reputation", -3), ("stat", "loyalty", -2)],
                    },
                    "failure": None,
                },
                {
                    "text": "收归领主直辖「谁都别争了」",
                    "stat_req": ("power", 40),
                    "success": {
                        "narration": "你宣布这片争议林地收归领主直辖，由城堡统一管理，收益归入公库。\n\n两家贵族面面相觑，却不敢反对。你用铁腕手段终结了三代人的争端，虽然树了敌，但也展示了权威。",
                        "effects": [("stat", "power", 5), ("stat", "wealth", 20), ("stat", "loyalty", -5)],
                    },
                    "failure": {
                        "narration": "你试图将林地收归直辖，但两家联合起来抵制你的命令。其他小贵族也暗中声援，担心自己的领地被下一个征收。\n\n你不得不收回命令，颜面大失。",
                        "effects": [("stat", "reputation", -8), ("stat", "power", -3)],
                    },
                },
            ],
        },

        "tax_evasion": {
            "id": "tax_evasion",
            "title": "偷税案发",
            "category": "political",
            "icon": "金",
            "icon_color": "#c0392b",
            "rarity": 18,
            "min_chapter": 2,
            "max_chapter": 5,
            "conditions": {"wealth_min": 30},
            "context": ["rest"],
            "description": "你的税务官发现，领地内最大的粮商一直在做假账，三年来偷逃了大量税款。\n\n这个粮商与城里半数商户都有生意往来，动他牵一发动全身。更棘手的是，有人暗示这个粮商是男爵的人。",
            "choices": [
                {
                    "text": "依法严惩「抄家补税」",
                    "stat_req": ("power", 35),
                    "success": {
                        "narration": "你下令查封粮商的仓库，追缴全部欠税，并处以双倍罚金。\n\n粮商哭天喊地，但你的士兵执法如山。从他的密室里还搜出了与男爵通信的书信——果然有猫腻。\n\n这次行动充实了国库，也让领民看到了新领主的决心。",
                        "effects": [("stat", "wealth", 20), ("stat", "power", 5), ("stat", "reputation", 5), ("stat", "loyalty", 3)],
                    },
                    "failure": {
                        "narration": "你下令抄查，但粮商早已得到风声，连夜转移了大部分财产。你的士兵只查到了一些空账本。\n\n粮商随后逃往男爵领地，还带走了几个重要的商业合作伙伴。领地的粮价应声上涨。",
                        "effects": [("stat", "wealth", -5), ("stat", "reputation", -3)],
                    },
                },
                {
                    "text": "私下谈判「要求他补缴并效忠」",
                    "stat_req": ("intrigue", 30),
                    "success": {
                        "narration": "你私下约见粮商，亮出证据后给了他两条路：要么补缴税款并成为你的眼线，要么交给官府处理。\n\n粮商是个聪明人，当即选择了前者。他不仅补缴了全部税款，还主动交出了男爵安排给他的任务清单。\n\n你多了一个潜伏在商界的棋子。",
                        "effects": [("stat", "wealth", 20), ("stat", "intrigue", 4), ("stat", "loyalty", -2)],
                    },
                    "failure": {
                        "narration": "你试图招安粮商，但他是个死硬分子，转头就把你的提议告诉了男爵。\n\n男爵借此大做文章，指责你私下勒索商人。你不得不公开澄清，但效果有限。",
                        "effects": [("stat", "reputation", -5), ("stat", "intrigue", 2)],
                    },
                },
                {
                    "text": "睁一只眼闭一只眼「维持现状」",
                    "stat_req": None,
                    "success": {
                        "narration": "你让税务官「再查查」，实际上是搁置此事。\n\n粮商松了口气，偷偷送来了一笔「孝敬」。但你的税务官很失望，其他商户也开始有样学样。\n\n有些事，不处理就是态度。",
                        "effects": [("stat", "wealth", 18), ("stat", "loyalty", -5), ("stat", "reputation", -3)],
                    },
                    "failure": None,
                },
            ],
        },

        "foreign_envoy": {
            "id": "foreign_envoy",
            "title": "异国使者",
            "category": "political",
            "icon": "旗",
            "icon_color": "#3498db",
            "rarity": 12,
            "min_chapter": 3,
            "max_chapter": 5,
            "conditions": {"reputation_min": 40},
            "context": ["rest"],
            "description": "一位自称来自海峡彼岸布列塔尼的使者求见。他带来了布列塔尼公爵的亲笔信，提议建立贸易通道。\n\n信中承诺提供葡萄酒和香料，交换你的铁矿和木材。条件优厚得有些可疑。\n\n艾琳娜提醒你，布列塔尼公爵与王后素有嫌隙。",
            "choices": [
                {
                    "text": "接受合作「打开新贸易路线」",
                    "stat_req": None,
                    "success": {
                        "narration": "你与使者签订了初步的贸易协议。第一批货物在两周后抵达——品质上乘的葡萄酒和东方香料。\n\n你的集市因此繁荣了起来，税收也水涨船高。不过，王后那边可能会有些想法……",
                        "effects": [("stat", "wealth", 18), ("stat", "reputation", 5), ("rel", "rel_queen", -8)],
                    },
                    "failure": None,
                },
                {
                    "text": "婉拒合作「不宜得罪王后」",
                    "stat_req": None,
                    "success": {
                        "narration": "你以「本领地资源有限」为由婉拒了使者。使者虽然失望，但表示理解。\n\n你将此事密报王后。王后回信称赞你的忠诚，并暗示将来会有回报。",
                        "effects": [("rel", "rel_queen", 10), ("stat", "reputation", 3)],
                    },
                    "failure": None,
                },
                {
                    "text": "两面下注「暗中合作，表面拒绝」",
                    "stat_req": ("intrigue", 45),
                    "success": {
                        "narration": "你公开拒绝了使者的提议，但在私下通过暗百合的渠道建立了秘密贸易线。\n\n货物以「走私」名义小批量进入，既赚了钱，又没有得罪王后。只要不被发现，这是最好的选择。",
                        "effects": [("stat", "wealth", 18), ("stat", "intrigue", 3), ("rel", "rel_queen", 3)],
                    },
                    "failure": {
                        "narration": "你试图两面下注，但秘密贸易线被男爵的探子发现了。\n\n男爵在领主会议上当众揭露此事，让你颜面扫地。王后也对你产生了怀疑。",
                        "effects": [("stat", "reputation", -10), ("rel", "rel_queen", -10), ("stat", "intrigue", 2)],
                    },
                },
            ],
        },

        ## ────────────────────────────────────────
        ## 8. 民生危机 (Civilian Crises)
        ## ────────────────────────────────────────

        "well_poisoned": {
            "id": "well_poisoned",
            "title": "水井投毒",
            "category": "crisis",
            "icon": "毒",
            "icon_color": "#27ae60",
            "rarity": 10,
            "min_chapter": 2,
            "max_chapter": 5,
            "conditions": {},
            "context": ["rest"],
            "description": "城东的公共水井被人投了毒！已有十余人上吐下泻，两个老人情况危急。\n\n村民们群情激愤，有人指认是一个外来的流浪汉干的，也有人怀疑是男爵的阴谋。\n\n真相还不清楚，但必须马上做出决定。",
            "choices": [
                {
                    "text": "先救人「全力救治中毒者」",
                    "stat_req": None,
                    "success": {
                        "narration": "你下令打开城堡药库，所有草药师和教堂修士全部投入救治。你亲自到井边监督清洗和消毒。\n\n经过一夜的紧张救治，所有中毒者脱离了危险。村民们感激涕零，一位老妇人拉着你的手，泪流满面。\n\n至于凶手……侍卫队已经开始调查了。",
                        "effects": [("stat", "loyalty", 10), ("stat", "wealth", -5), ("stat", "faith", 12)],
                    },
                    "failure": None,
                },
                {
                    "text": "先抓人「立刻逮捕嫌疑人」",
                    "stat_req": ("power", 30),
                    "success": {
                        "narration": "你下令全城戒严，封锁城门，搜捕所有可疑人员。\n\n在城南的一间废弃马厩里，你的士兵找到了那个流浪汉——他身上藏着一小瓶残余的毒药，瓶底刻着男爵家的纹章。\n\n铁证如山。你将此事公之于众，男爵的阴谋昭然若揭。",
                        "effects": [("stat", "power", 5), ("stat", "reputation", 8), ("rel", "rel_baron", -10)],
                    },
                    "failure": {
                        "narration": "你下令搜捕，但折腾了一整天也没找到确凿的嫌疑人。\n\n那个流浪汉被抓后死不承认，而你在没有充分证据的情况下关押了他，引来一些议论。",
                        "effects": [("stat", "reputation", -3), ("stat", "power", 2)],
                    },
                },
                {
                    "text": "暗中调查「不打草惊蛇」",
                    "stat_req": ("intrigue", 35),
                    "success": {
                        "narration": "你表面上只是下令救治伤者、清洗水井，但暗中让艾琳娜追查毒药来源。\n\n三天后，艾琳娜查到毒药是通过一个小贩流入的，而小贩的上线是男爵安插在城中的探子。\n\n你没有声张，而是将这个探子变成了你的双面间谍。这比简单地抓人有价值得多。",
                        "effects": [("stat", "intrigue", 3), ("stat", "loyalty", 3), ("rel", "rel_elena", 5)],
                    },
                    "failure": {
                        "narration": "你暗中调查，但线索在关键节点断了——有人提前灭口了那个小贩。\n\n你虽然没有打草惊蛇，但也没能查出真相。这件事就这样不了了之。",
                        "effects": [("stat", "intrigue", 3), ("stat", "loyalty", -3)],
                    },
                },
            ],
        },

        "famine_threat": {
            "id": "famine_threat",
            "title": "粮荒将至",
            "category": "crisis",
            "icon": "粮",
            "icon_color": "#e67e22",
            "rarity": 15,
            "min_chapter": 2,
            "max_chapter": 5,
            "conditions": {},
            "context": ["rest"],
            "description": "连续的暴雨毁了今年大半的庄稼。仓库里的存粮只够撑两个月，而下一季收成还要等四个月。\n\n管家焦急地报告：「如果不采取措施，入冬前领地将爆发饥荒。」\n\n你望着窗外连绵的阴雨，心沉如铁。",
            "choices": [
                {
                    "text": "高价采购粮食「用金钱解决」",
                    "stat_req": ("wealth", 40),
                    "success": {
                        "narration": "你派商队从南方紧急采购了大批粮食。虽然价格比平时贵了三倍，但总算填上了缺口。\n\n你还组织了「以工代赈」——让受灾农民修缮道路和水渠，换取每日口粮。\n\n领民们虽然日子紧巴巴的，但没有人挨饿。",
                        "effects": [("stat", "wealth", -15), ("stat", "loyalty", 10), ("stat", "reputation", 5)],
                    },
                    "failure": {
                        "narration": "你试图购粮，但南方的粮价也在涨，而你的国库不够充裕。最终只买到了杯水车薪的一点粮食。\n\n部分村庄开始出现饥饿的迹象。",
                        "effects": [("stat", "wealth", -10), ("stat", "loyalty", -5)],
                    },
                },
                {
                    "text": "向教会求援「借用教堂粮仓」",
                    "stat_req": ("faith", 35),
                    "success": {
                        "narration": "你亲自前往教堂，向主教马修斯说明情况。老主教捏着念珠想了很久，最终点了点头。\n\n「教堂的粮仓为神的子民而设。」他说，「我会开放储备，但你要承诺——来年丰收时，双倍归还。」\n\n教堂的粮食缓解了燃眉之急，而你与教会的关系也因此更加紧密。",
                        "effects": [("stat", "faith", 12), ("stat", "loyalty", 8), ("rel", "rel_bishop", 10)],
                    },
                    "failure": {
                        "narration": "你向教会求助，但主教认为教堂的储备也很紧张，只象征性地捐了一点。\n\n「神会保佑我们的，」他说，「但粮食不会从天上掉下来。」",
                        "effects": [("stat", "faith", -3), ("stat", "loyalty", -3)],
                    },
                },
                {
                    "text": "征收富户余粮「强制均平」",
                    "stat_req": ("power", 40),
                    "success": {
                        "narration": "你下令所有大户和贵族必须按比例上交存粮，由领主府统一分配。\n\n富户们怨声载道，但在你的铁腕面前无人敢违抗。普通领民则拍手称快——「终于有人管了！」\n\n这是一个得罪贵族、收买民心的决定。",
                        "effects": [("stat", "power", 5), ("stat", "loyalty", 12), ("stat", "reputation", -5)],
                    },
                    "failure": {
                        "narration": "你试图强征粮食，但几个大户联合起来抵制，甚至威胁要向男爵求援。\n\n你不得不退让，只征到了原计划一半的粮食。你的权威受到了挑战。",
                        "effects": [("stat", "power", -5), ("stat", "loyalty", 3)],
                    },
                },
            ],
        },

        "mysterious_death": {
            "id": "mysterious_death",
            "title": "蹊跷命案",
            "category": "crisis",
            "icon": "骷",
            "icon_color": "#2c3e50",
            "rarity": 10,
            "min_chapter": 3,
            "max_chapter": 5,
            "conditions": {},
            "context": ["rest"],
            "description": "清晨，侍卫在城堡护城河中发现了一具尸体。死者是你手下的一名文书官，负责管理领地的人口登记和赋税记录。\n\n尸体上没有外伤，但嘴唇发黑——这是中毒的特征。\n\n更令人不安的是，他的办公室被翻了个底朝天，几份重要文件不翼而飞。",
            "choices": [
                {
                    "text": "让奥尔德里克主持调查「走正规路子」",
                    "stat_req": None,
                    "success": {
                        "narration": "老骑士奥尔德里克带人封锁了现场，逐一盘问城堡内的所有人。\n\n三天后，他找到了关键证据——毒药是藏在文书官的茶壶里的，而能接触到他茶壶的只有三个人。\n\n经过审讯，一名新来的仆人供出了实情：他是男爵的人，奉命窃取领地的人口和军力数据。毒杀文书官只是灭口。",
                        "effects": [("stat", "power", 5), ("rel", "rel_aldric", 8), ("stat", "intrigue", 3)],
                    },
                    "failure": None,
                },
                {
                    "text": "让艾琳娜暗中追查「用间谍手段」",
                    "stat_req": ("intrigue", 30),
                    "success": {
                        "narration": "艾琳娜用了一种更隐蔽的方法——她不调查谁杀了文书官，而是追踪那些失窃文件的去向。\n\n她发现文件被复制后通过一条秘密渠道送往男爵领地。更重要的是，她顺藤摸瓜，发现了城堡内还有另外两名男爵的内应。\n\n你没有打草惊蛇，而是开始向这些内应喂送假情报。",
                        "effects": [("stat", "intrigue", 3), ("rel", "rel_elena", 8), ("stat", "power", 3)],
                    },
                    "failure": {
                        "narration": "艾琳娜暗中调查，但对方也不是省油的灯。在她接近真相时，有人向她投了一封警告信——「再查下去，你也会浮在护城河里。」\n\n你不得不暂停调查，加强了城堡的安保。",
                        "effects": [("stat", "intrigue", 3), ("rel", "rel_elena", 3)],
                    },
                },
                {
                    "text": "公开悬赏线索「发动群众」",
                    "stat_req": ("loyalty", 40),
                    "success": {
                        "narration": "你在城中张贴告示，悬赏百枚金币缉拿凶手。领民们议论纷纷，各种线索如雪片般飞来。\n\n虽然大部分线索没有价值，但一个卖菜的老妇人提供了关键信息——她在案发当晚看到一个陌生人从城堡侧门溜出，手里拿着一个皮卷筒。\n\n根据她的描述，你的人在城外的一个驿站抓住了那个逃走的间谍。",
                        "effects": [("stat", "wealth", -8), ("stat", "loyalty", 5), ("stat", "reputation", 5)],
                    },
                    "failure": {
                        "narration": "悬赏告示贴出后，各种假线索蜂拥而至。你的人查了上百条线索，全是死胡同。\n\n花了不少钱，却什么也没查到。凶手早已远遁。",
                        "effects": [("stat", "wealth", -8), ("stat", "reputation", -3)],
                    },
                },
            ],
        },

        ## ────────────────────────────────────────
        ## 9. 奇遇 (Special Encounters)
        ## ────────────────────────────────────────

        "ghost_sighting": {
            "id": "ghost_sighting",
            "title": "城堡幽灵",
            "category": "encounter",
            "icon": "幽",
            "icon_color": "#9b59b6",
            "rarity": 8,
            "min_chapter": 2,
            "max_chapter": 5,
            "conditions": {},
            "context": ["rest"],
            "description": "连续几个夜晚，侍卫报告在城堡西塔看到了模糊的人影。有人说那是你父亲的亡灵，也有人说是闹鬼。\n\n今夜，你决定亲自去看看。\n\n西塔的旋梯上布满灰尘，月光从破窗洒进来。在塔顶的房间里，你看到了摇曳的烛光——确实有什么东西在那里。",
            "choices": [
                {
                    "text": "推门进去「直面未知」",
                    "stat_req": ("power", 20),
                    "success": {
                        "narration": "你握紧剑柄，推开了房门。\n\n烛光映照下，你看到的不是鬼魂，而是一个衣衫褴褛的少女。她蜷缩在角落里，怀中抱着一叠发黄的文件。\n\n她声称自己是前任管家的女儿，一直藏在西塔里。这些文件——是你父亲的私人日记。\n\n日记中记载了许多领地的秘密，包括一些你从未知道的事情。",
                        "effects": [("stat", "intrigue", 4), ("stat", "loyalty", 3)],
                    },
                    "failure": None,
                },
                {
                    "text": "让主教来驱邪「以信仰之力」",
                    "stat_req": ("faith", 30),
                    "success": {
                        "narration": "你请主教马修斯带着圣水和十字架来到西塔。老主教念了一段经文，然后推开了房门。\n\n里面的「幽灵」被吓得惊叫出声——原来是一个藏匿的逃犯。他是从男爵的矿山逃出来的奴工，偷偷躲在这里已经几个月了。\n\n他供出了男爵矿山里使用奴隶劳工的秘密。这是一个有价值的把柄。",
                        "effects": [("stat", "faith", 15), ("stat", "intrigue", 3), ("rel", "rel_bishop", 5)],
                    },
                    "failure": None,
                },
                {
                    "text": "封锁西塔「眼不见心不烦」",
                    "stat_req": None,
                    "success": {
                        "narration": "你下令封锁西塔入口，禁止任何人接近。\n\n「幽灵」传闻渐渐平息了，但侍卫们私下议论，说你是因为害怕才封塔的。你的威严受到了一些影响。\n\n也许那里面真的有什么值得一探的秘密，被你错过了。",
                        "effects": [("stat", "reputation", -5), ("stat", "loyalty", -2)],
                    },
                    "failure": None,
                },
            ],
        },

        "traveling_troupe": {
            "id": "traveling_troupe",
            "title": "流浪剧团",
            "category": "encounter",
            "icon": "戏",
            "icon_color": "#e91e63",
            "rarity": 20,
            "min_chapter": 1,
            "max_chapter": 5,
            "conditions": {},
            "context": ["rest", "explore"],
            "description": "一个由六人组成的流浪剧团来到你的领地，请求在集市广场演出三天。\n\n他们的节目单上有一出戏引起了你的注意——《暴君的末日》，讲的是一个残暴领主被推翻的故事。\n\n这出戏是纯粹的娱乐，还是有人在借戏讽刺？",
            "choices": [
                {
                    "text": "允许演出「海纳百川」",
                    "stat_req": None,
                    "success": {
                        "narration": "你大方地允许了剧团的演出，甚至亲自去观看。\n\n那出《暴君的末日》确实辛辣，但你在观众席上哈哈大笑，丝毫不以为忤。\n\n领民们见你如此大度，反而更加敬重你。剧团团长在临别时悄悄告诉你：「大人，南方有人在散播对您不利的谣言。我们一路走来都听到了。」\n\n这条情报价值连城。",
                        "effects": [("stat", "reputation", 8), ("stat", "loyalty", 5), ("stat", "intrigue", 3)],
                    },
                    "failure": None,
                },
                {
                    "text": "审查剧本「删改敏感内容」",
                    "stat_req": None,
                    "success": {
                        "narration": "你要求先审查剧本，删掉了几段最尖锐的台词后才允许演出。\n\n剧团勉强接受了。演出效果平平，观众觉得少了些味道。倒是没有引发什么骚动。\n\n不过，剧团私下把你的「审查」行为传了出去，周围几个领地的人都知道了。",
                        "effects": [("stat", "reputation", -5), ("stat", "loyalty", -2), ("stat", "power", 2)],
                    },
                    "failure": None,
                },
                {
                    "text": "驱逐剧团「宁杀错不放过」",
                    "stat_req": None,
                    "success": {
                        "narration": "你以「扰乱社会秩序」为由驱逐了剧团。\n\n领民们虽然失去了一次娱乐机会，但也没有太多怨言。毕竟，你是领主。\n\n不过，剧团后来把这件事编成了一出新戏——《小心翼翼的领主》。据说在其他领地演出时，笑得观众前仰后合。",
                        "effects": [("stat", "reputation", -8), ("stat", "power", 3), ("stat", "loyalty", -3)],
                    },
                    "failure": None,
                },
            ],
        },

        "old_veterans_plea": {
            "id": "old_veterans_plea",
            "title": "老兵请命",
            "category": "encounter",
            "icon": "盾",
            "icon_color": "#795548",
            "rarity": 15,
            "min_chapter": 2,
            "max_chapter": 5,
            "conditions": {},
            "context": ["rest", "explore"],
            "description": "一群白发苍苍的老兵聚集在城堡门前，为首的是一个独臂老人。他们都是你父亲麾下的老部下。\n\n独臂老人跪在地上：「少主，我们跟着老领主打了一辈子仗。如今老了，腿脚不利索了，庄稼也种不动了。」\n\n「老领主在世时，每月给我们发抚恤粮。可他走后，管家以'开支紧张'为由停了。」\n\n他们的眼神中既有恳求，也有不甘。",
            "choices": [
                {
                    "text": "恢复抚恤「父亲的承诺我来兑现」",
                    "stat_req": None,
                    "success": {
                        "narration": "你当即下令恢复所有老兵的抚恤，并追补了拖欠的部分。\n\n独臂老人老泪纵横：「少主像老领主一样，是个好人。」\n\n消息传开后，那些还在服役的士兵士气大振——他们知道，即使将来老了残了，领主也不会抛弃他们。\n\n奥尔德里克也私下找到你，深深鞠了一躬：「做得好，少主。这才是艾登堡的风骨。」",
                        "effects": [("stat", "wealth", -8), ("stat", "loyalty", 12), ("stat", "power", 5), ("rel", "rel_aldric", 8)],
                    },
                    "failure": None,
                },
                {
                    "text": "安排他们到庄园养老「给个体面的归宿」",
                    "stat_req": ("wealth", 30),
                    "success": {
                        "narration": "你将城堡附近的一座闲置庄园拨给老兵们居住，安排人定期送去粮食和柴火。\n\n虽然不是恢复抚恤，但这个安排更加体面。老兵们互相照顾，还自发组织了巡逻队，保护周边村庄的安全。\n\n这支「老兵巡逻队」虽然不能上阵杀敌，但在维护治安方面发挥了意想不到的作用。",
                        "effects": [("stat", "wealth", -5), ("stat", "loyalty", 8), ("stat", "power", 3)],
                    },
                    "failure": None,
                },
                {
                    "text": "解释财政困难「暂时无力承担」",
                    "stat_req": None,
                    "success": {
                        "narration": "你坦诚地告诉老兵们，目前领地确实财力紧张，一时无法恢复全额抚恤。\n\n「但我承诺，」你说，「只要领地财政好转，第一件事就是恢复你们的抚恤。」\n\n老兵们沉默着离开了。独臂老人走出大门前回头看了你一眼——那个眼神里，有失望，但也有一丝理解。\n\n你身边的士兵们交换了几个意味深长的眼神。",
                        "effects": [("stat", "loyalty", -8), ("stat", "power", -3), ("rel", "rel_aldric", -5)],
                    },
                    "failure": None,
                },
            ],
        },

        "witch_trial": {
            "id": "witch_trial",
            "title": "女巫审判",
            "category": "encounter",
            "icon": "火",
            "icon_color": "#ff5722",
            "rarity": 12,
            "min_chapter": 2,
            "max_chapter": 5,
            "conditions": {},
            "context": ["rest", "explore"],
            "description": "领地里出了大事——村民们抓住了一个「女巫」，要求你下令处以火刑。\n\n这个被指控的女人其实是村子里的草药师，平时为人治病。但最近几个孩子莫名发烧后，有人开始说她「用邪术诅咒了孩子们」。\n\n愤怒的村民已经在广场上堆起了柴堆。主教马修斯正在试图安抚人群，但效果有限。",
            "choices": [
                {
                    "text": "调查真相「先查清孩子生病的原因」",
                    "stat_req": ("intrigue", 25),
                    "success": {
                        "narration": "你命令暂停一切审判，派人调查孩子们生病的真正原因。\n\n两天后，你的调查员发现——孩子们是喝了村东小溪的水才生病的。溪水被上游一座新建的染坊污染了。\n\n你公布了调查结果，为草药师洗清了冤屈。她含泪感谢你，并且成为了你最忠诚的支持者。\n\n你还借此机会整治了染坊的排污问题。",
                        "effects": [("stat", "intrigue", 3), ("stat", "loyalty", 8), ("stat", "reputation", 8)],
                    },
                    "failure": {
                        "narration": "你试图调查，但村民们的情绪太激动了，不愿意等待。\n\n虽然你最终控制了局面，但草药师在混乱中被人扔石头砸伤了。她后来离开了村子，再也没有回来。\n\n村子里再也没有人会治病了。",
                        "effects": [("stat", "loyalty", -5), ("stat", "reputation", 3)],
                    },
                },
                {
                    "text": "让主教主持公正审判「以信仰之名」",
                    "stat_req": ("faith", 30),
                    "success": {
                        "narration": "你将此事交给主教马修斯。老主教设下「神判」——让草药师手持烧红的铁棒走过教堂。\n\n但马修斯提前偷偷涂了一层药膏在铁棒上——他相信草药师是无辜的。\n\n草药师安然走过，村民们跪下祈祷：「神证明了她的清白！」\n\n事后马修斯对你说：「有时候，信仰需要一点帮助。」",
                        "effects": [("stat", "faith", 12), ("stat", "loyalty", 5), ("rel", "rel_bishop", 8)],
                    },
                    "failure": None,
                },
                {
                    "text": "顺应民意「处死女巫」",
                    "stat_req": None,
                    "success": {
                        "narration": "你选择了最容易的路——宣判草药师有罪。\n\n柴堆燃起，火焰吞噬了一个无辜的女人。村民们欢呼，觉得灾厄已经被驱散。\n\n但你心里知道真相。那天晚上，你一夜没有合眼。\n\n更糟糕的是，孩子们还在继续生病。",
                        "effects": [("stat", "loyalty", 5), ("stat", "faith", -10), ("stat", "reputation", -8), ("rel", "rel_bishop", -10)],
                    },
                    "failure": None,
                },
            ],
        },
    }

    ## ================================================================
    ## 物品系统 — 由 inventory.rpy 提供
    ## add_item(), remove_item(), has_item() 等函数来自 inventory.rpy
    ## ================================================================

    ## 物品数据仅用于随机事件中的物品名称显示
    _item_data = {
        "medicinal_herbs":   ("药草", "material", "草", "常见的治疗用草药"),
        "waterskin":         ("水袋", "material", "水", "装满清水的皮水袋"),
        "holy_water":        ("圣水", "material", "十", "经过祝福的圣水"),
        "dark_lily_extract": ("暗百合提取物", "material", "毒", "稀有的毒性植物提取物"),
        "leather_scraps":    ("皮革碎片", "material", "革", "可用于制作的皮革"),
        "iron_ore":          ("铁矿石", "material", "铁", "品质良好的铁矿"),
        "health_potion":     ("治疗药水", "consumable", "药", "恢复生命值的药水"),
        "stamina_potion":    ("耐力药水", "consumable", "耐", "恢复耐力的药水"),
        "antidote":          ("解毒药", "consumable", "解", "解除中毒状态"),
        "bandage":           ("绷带", "consumable", "绷", "简易的伤口包扎材料"),
        "war_paint":         ("战争涂料", "consumable", "战", "涂抹后暂时提升战斗力"),
        "smoke_bomb":        ("烟雾弹", "consumable", "烟", "用于逃跑或制造混乱"),
        "gambeson":          ("棉甲", "equipment", "甲", "轻便的棉质护甲"),
        "chainmail":         ("锁子甲", "equipment", "锁", "坚固的铁环编织甲"),
        "blessed_mace":      ("祝福战锤", "equipment", "锤", "经过祝福的战锤"),
        "potent_medicine":   ("强效药剂", "consumable", "强", "效果强大的特制药剂"),
    }

    ## ================================================================
    ## 物品背包
    ## ================================================================

    ## add_item / remove_item / has_item / get_item_count
    ## 这些函数由 inventory.rpy 定义，此处不重复定义

    ## ================================================================
    ## 随机事件核心逻辑
    ## ================================================================

    def _get_current_chapter_num():
        """获取当前章节数字，根据当前label名判断"""
        try:
            label = renpy.get_filename_line()[0]
            if "prologue" in label:
                return 0
            elif "chapter5" in label:
                return 5
            elif "chapter4" in label:
                return 4
            elif "chapter3" in label:
                return 3
            elif "chapter2" in label:
                return 2
            else:
                return 1
        except Exception:
            return 1

    def _check_event_conditions(event):
        """检查事件触发条件"""
        ch = _get_current_chapter_num()
        if ch < event.get("min_chapter", 1) or ch > event.get("max_chapter", 5):
            return False
        conds = event.get("conditions", {})
        for key, val in conds.items():
            if key.endswith("_min"):
                stat = key[:-4]
                if getattr(store, stat, 0) < val:
                    return False
            elif key.endswith("_max"):
                stat = key[:-4]
                if getattr(store, stat, 100) > val:
                    return False
            elif key.startswith("flag_"):
                flag = key[5:]
                if getattr(store, flag, False) != val:
                    return False
        return True

    def get_available_events(context="travel"):
        """获取当前可用的事件列表"""
        available = []
        for eid, ev in _random_events.items():
            if eid in store.random_events_seen:
                continue
            if context not in ev.get("context", []):
                continue
            if not _check_event_conditions(ev):
                continue
            available.append(ev)
        return available

    def _pick_weighted_event(events):
        """根据稀有度权重随机选择事件"""
        if not events:
            return None
        total = sum(e["rarity"] for e in events)
        roll = renpy.random.randint(1, total)
        running = 0
        for ev in events:
            running += ev["rarity"]
            if roll <= running:
                return ev
        return events[-1]

    def _check_choice_success(choice):
        """检查选项是否成功"""
        req = choice.get("stat_req")
        if req is None:
            return True  # 无条件选项总是成功
        stat_name, threshold = req
        current = getattr(store, stat_name, 0)
        ## 基础成功率: 属性越高越容易成功
        if current >= threshold:
            ## 满足要求: 80-100% 成功率
            rate = 80 + min(20, (current - threshold))
        else:
            ## 不满足要求: 20-60% 成功率
            diff = threshold - current
            rate = max(20, 60 - diff * 2)
        return renpy.random.randint(1, 100) <= rate

    def _apply_effects(effects):
        """应用事件效果"""
        for eff in effects:
            if eff[0] == "stat":
                change_stat(eff[1], eff[2])
            elif eff[0] == "rel":
                change_rel(eff[1], eff[2])
            elif eff[0] == "flag":
                setattr(store, eff[1], eff[2])
            elif eff[0] == "item":
                if eff[2] > 0:
                    add_item(eff[1], eff[2])
                else:
                    remove_item(eff[1], abs(eff[2]))

    def trigger_random_event(context="travel"):
        """
        触发随机事件。在剧本中调用:
            $ event_result = trigger_random_event("travel")
        返回 True 如果事件触发并完成，否则 False。
        """
        ## 冷却检查
        if store.random_event_cooldown > 0:
            store.random_event_cooldown -= 1
            return False

        ## 30% 概率不触发事件（给玩家喘息空间）
        if renpy.random.randint(1, 100) <= 30:
            return False

        available = get_available_events(context)
        if not available:
            return False

        event = _pick_weighted_event(available)
        if event is None:
            return False

        ## 设置冷却 (至少间隔2次调用)
        store.random_event_cooldown = 2
        store.random_events_seen.add(event["id"])

        ## 显示事件界面
        renpy.call_in_new_context("_random_event_handler", event_data=event)
        return True


## ── 物品通知由 inventory.rpy 的 item_notify screen 提供 ──



## ================================================================
## 随机事件主界面
## ================================================================

screen random_event_screen(event_data=None):
    zorder 300
    modal True

    ## 暗色遮罩
    add Solid("#0a0812ee")

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 0
        ypadding 0
        if renpy.variant("small"):
            xsize 0.95
            ymaximum 0.9
        else:
            xsize 700
            ymaximum 620

        background Solid("#0f0d1af8")

        vbox:
            spacing 0

            ## ── 标题栏 ──
            frame:
                xfill True
                ysize 60
                background Solid("#1a1528")
                xpadding 24

                hbox:
                    yalign 0.5
                    xfill True

                    hbox:
                        spacing 10
                        ## 事件图标
                        frame:
                            xsize 36
                            ysize 36
                            background Solid(event_data["icon_color"] + "30")
                            text event_data["icon"] xalign 0.5 yalign 0.5 size 18 color event_data["icon_color"]

                        vbox:
                            text event_data["title"] size 22 color "#d4a942" font "msyh.ttf" bold True
                            ## 分类标签
                            $ _cat_names = {"combat": "战斗遭遇", "trade": "交易机会", "intelligence": "情报事件", "character": "角色事件", "crisis": "危机事件"}
                            $ _cat_name = _cat_names.get(event_data.get("category", ""), "随机事件")
                            text _cat_name size 11 color "#6a5e48"

            ## 分隔线
            add Solid("#d4a94240") xsize 1.0 ysize 1

            ## ── 可滚动内容 ──
            viewport:
                xfill True
                yfill True
                mousewheel True
                draggable True

                frame:
                    background None
                    xpadding 28
                    ypadding 20
                    xfill True

                    vbox:
                        spacing 16

                        ## 事件描述
                        text event_data["description"] size 16 color "#c8b890" font "msyh.ttf" line_spacing 8

                        add Solid("#d4a94220") xsize 1.0 ysize 1

                        ## 选项标题
                        text "如何应对？" size 18 color "#d4a942" font "msyh.ttf"

                        ## 选项按钮
                        for _ci, _choice in enumerate(event_data["choices"]):
                            $ _c_req = _choice.get("stat_req")
                            $ _c_req_met = True
                            $ _c_req_text = ""
                            if _c_req is not None:
                                $ _c_stat_names = {"power": "权力", "wealth": "财富", "faith": "信仰", "loyalty": "忠诚", "reputation": "声望", "intrigue": "谋略"}
                                $ _c_current = getattr(store, _c_req[0], 0)
                                $ _c_needed = _c_req[1]
                                $ _c_req_text = "需要%s %d（当前 %d）" % (_c_stat_names.get(_c_req[0], _c_req[0]), _c_needed, _c_current)
                                if _c_current < _c_needed:
                                    $ _c_req_met = False

                            button:
                                xfill True
                                xpadding 16
                                ypadding 12
                                if _c_req_met:
                                    background Solid("#1a152860")
                                    hover_background Solid("#1a1528a0")
                                else:
                                    background Solid("#1a152830")
                                    hover_background Solid("#1a152850")

                                action Return(("choice", _ci))

                                vbox:
                                    spacing 4
                                    text _choice["text"] size 16 color ("#e0d8c8" if _c_req_met else "#6a5e48") font "msyh.ttf"
                                    if _c_req_text:
                                        if _c_req_met:
                                            text "V [_c_req_text]" size 12 color "#2ecc71"
                                        else:
                                            text "! [_c_req_text]（成功率降低）" size 12 color "#e67e22"


## ================================================================
## 事件结果界面
## ================================================================

screen random_event_result_screen(event_title="", narration="", effects=None, is_success=True):
    zorder 300
    modal True

    add Solid("#0a0812ee")

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 0
        ypadding 0
        if renpy.variant("small"):
            xsize 0.95
            ymaximum 0.85
        else:
            xsize 650
            ymaximum 550

        background Solid("#0f0d1af8")

        vbox:
            spacing 0

            ## 标题
            frame:
                xfill True
                ysize 50
                background Solid("#1a1528")
                xpadding 24

                hbox:
                    yalign 0.5
                    xfill True
                    $ _res_icon = ">" if is_success else "!"
                    $ _res_color = "#2ecc71" if is_success else "#e67e22"
                    $ _res_text = "成功" if is_success else "失败"

                    hbox:
                        spacing 8
                        text _res_icon size 20 color _res_color yalign 0.5
                        text event_title size 20 color "#d4a942" font "msyh.ttf" bold True yalign 0.5
                        text "— [_res_text]" size 16 color _res_color yalign 0.5

            add Solid("#d4a94240") xsize 1.0 ysize 1

            viewport:
                xfill True
                yfill True
                mousewheel True
                draggable True

                frame:
                    background None
                    xpadding 28
                    ypadding 20
                    xfill True

                    vbox:
                        spacing 16

                        ## 结果叙述
                        text narration size 16 color "#c8b890" font "msyh.ttf" line_spacing 8

                        if effects:
                            add Solid("#d4a94220") xsize 1.0 ysize 1

                            text "* 影响" size 16 color "#d4a942" font "msyh.ttf"

                            for _eff in effects:
                                if _eff[0] == "stat":
                                    $ _eff_stat_names = {"power": "权力", "wealth": "财富", "faith": "信仰", "loyalty": "忠诚", "reputation": "声望", "intrigue": "谋略"}
                                    $ _eff_name = _eff_stat_names.get(_eff[1], _eff[1])
                                    $ _eff_sign = "+" if _eff[2] > 0 else ""
                                    $ _eff_color = "#2ecc71" if _eff[2] > 0 else "#e74c3c"
                                    text "  [_eff_name] [_eff_sign][_eff[2]]" size 14 color _eff_color
                                elif _eff[0] == "rel":
                                    $ _eff_rel_names = {"rel_aldric": "奥尔德里克", "rel_elena": "艾琳娜", "rel_bishop": "主教", "rel_baron": "男爵", "rel_captain": "队长", "rel_queen": "王后", "rel_prince": "王子", "rel_lily": "暗百合"}
                                    $ _eff_name = _eff_rel_names.get(_eff[1], _eff[1])
                                    $ _eff_sign = "+" if _eff[2] > 0 else ""
                                    $ _eff_color = "#2ecc71" if _eff[2] > 0 else "#e74c3c"
                                    text "  [_eff_name]好感 [_eff_sign][_eff[2]]" size 14 color _eff_color
                                elif _eff[0] == "item":
                                    if _eff[1] in _item_data:
                                        $ _eff_item_name = _item_data[_eff[1]][0]
                                        $ _eff_qty_sign = "+" if _eff[2] > 0 else ""
                                        $ _eff_item_color = "#d4a942" if _eff[2] > 0 else "#e74c3c"
                                        text "  获得 [_eff_item_name] x[_eff[2]]" size 14 color _eff_item_color

                        null height 8

                        ## 继续按钮
                        textbutton "继续":
                            xalign 0.5
                            text_size 20
                            text_color "#d4a942"
                            text_hover_color "#ffd866"
                            text_font "msyh.ttf"
                            action Return("continue")


## ================================================================
## 事件处理流程 (覆写 _random_event_handler 以支持完整流程)
## ================================================================

label _random_event_handler(event_data=None):
    if event_data is None:
        return

    ## 显示事件界面
    call screen random_event_screen(event_data=event_data)

    ## 处理玩家选择
    $ _re_result = _return
    if isinstance(_re_result, tuple) and _re_result[0] == "choice":
        $ _re_choice_idx = _re_result[1]
        $ _re_choice = event_data["choices"][_re_choice_idx]

        ## 判定成功/失败
        $ _re_success = _check_choice_success(_re_choice)

        if _re_success and _re_choice.get("success"):
            $ _re_outcome = _re_choice["success"]
            $ _re_is_success = True
        elif not _re_success and _re_choice.get("failure"):
            $ _re_outcome = _re_choice["failure"]
            $ _re_is_success = False
        elif _re_choice.get("success"):
            ## 没有失败分支，默认成功
            $ _re_outcome = _re_choice["success"]
            $ _re_is_success = True
        else:
            return

        ## 应用效果
        $ _apply_effects(_re_outcome.get("effects", []))

        ## 记录结果
        $ store.last_event_result = event_data["title"] + (" 成功" if _re_is_success else " 失败")

        ## 显示结果界面
        call screen random_event_result_screen(event_title=event_data["title"], narration=_re_outcome["narration"], effects=_re_outcome.get("effects", []), is_success=_re_is_success)

    return


## ================================================================
## 物品背包界面
## ================================================================

## 物品背包界面和 I 键绑定由 inventory.rpy 提供

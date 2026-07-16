## ============================================================
## 北境游记 DLC — 第二弹《盐路与雪原》  [骨架 / WIP]
## ------------------------------------------------------------
## 与本体的连接(本弹核心目标):
##   ① 回指: 希尔达伯爵夫人(本体北疆议会)登场; 赛琳/渡鸦号顺"北上盐路"客串。
##   ② 读档分支: DLC 从主菜单进、跑独立小档, 读不到"当前这局"过程 flag,
##      只能读 persistent ——
##        persistent.endings_seen        玩家历史通关过的本体结局(8 个 key)
##        persistent.southern_endings_seen 第一弹南境结局
##      据此定北境对你的初始态度 / 盐路状况 / 赛琳是敌是友。
##   ③ 回流本体: 北境结局 set persistent.northern_* , 本体侧加 if 钩子(资源/成就)。
##      ★ TODO: ③ 动本体数值平衡, 等南境反馈 + balance_pending 一起做, 暂留钩子。
##
## 钩子来源: 南境 fall 结局赛琳原话 "原来你北上那条盐路, 比这一港的人都重"。
## ============================================================

## ─── 北境 DLC 专用变量 ───
default northern_visited = False
default northern_quest_stage = 0
## rel_hilda 本体已 default(希尔达好感), 直接复用, 不重复声明
default rel_skadi = 0                        # 雪原向导斯卡蒂好感
default salt_route_secured = False           # 盐路是否打通
default council_stance = ""                  # 北疆议会对你的立场 "fear"/"respect"/"scorn"
default southern_backer = ""                 # 南境靠山 "ruler"/"ally"/"none"(由②推出)
default northern_first_impression = ""
default met_skadi = False
default north_insight = 0                     # 对北疆/议会/马匪的了解度
default persistent.northern_dlc_progress = 0
## DLC 结局单独成 set, 不混进主线 persistent.endings_seen
default persistent.northern_endings_seen = set()

## ─── ② 读档态度推导(只读 persistent, 不依赖当前档过程 flag) ───
init python:
    def northern_seed_attitude():
        """据玩家历史通关记录, 定北境议会立场 + 南境靠山。在入口处调一次。"""
        seen = persistent.endings_seen or set()
        south = persistent.southern_endings_seen or set()

        # 议会立场: 铁腕→忌惮; 民心/真相→敬重; 失势→轻视; 都没有→中立观望
        if "iron_lord" in seen or "shadow_king" in seen:
            store.council_stance = "fear"
        elif "peoples_lord" in seen or "truth" in seen or "holy_guardian" in seen:
            store.council_stance = "respect"
        elif "vassal" in seen or "fall" in seen:
            store.council_stance = "scorn"
        else:
            store.council_stance = "neutral"

        # 南境靠山: 第一弹掌控港口→强靠山; 促和/自由→赛琳可援; 覆灭→孤立
        if "southern_ruler" in south:
            store.southern_backer = "ruler"
        elif "southern_free" in south or "southern_outwit" in south:
            store.southern_backer = "ally"
        else:
            store.southern_backer = "none"

## ─── 北境 DLC 角色 ───
## 希尔达伯爵夫人: 本体北疆议会话事人, 直接复用本体 define(prologue.rpy 已声明)
## 雪原向导斯卡蒂: 北境新角色, 边民猎手, 认路也认人
define skadi = Character("斯卡蒂", color="#6a8aa8", image="storyteller")
## 北疆议会对手领主
define lord_north = Character("沃尔德领主", color="#7a6a5a", image="noble_werner")
## 盐队管事(你派出的北上盐队头目)
define salt_lead = Character("盐队管事", color="#8a7a5a", image="merchant_karl")
## 雪原马匪头领
define raider_chief = Character("断牙", color="#5a5a4a", image="old_guard")
## 北境通用配角
define north_villager = Character("边民", color="#8a8a8a", image="servant_generic")
define north_soldier = Character("议会卫兵", color="#7a7a6a", image="soldier_generic")


## ============================================================
## 入口
## ============================================================
## 【本文件当前不可达】2026-07-16
## 主菜单的「北境游记 ◆（开发中）」入口已随南境并入主线一并移除(screens.rpy 原 459-467)。
## 那个入口本来就锁在 config.developer 后面、无 else 分支, 正式版玩家从来看不见, 所以删掉
## 零可见变化; 开发者仍可 shift+O 控制台 jump northern_dlc_start。
##
## 为什么不并入主线(与南境不同): 它是骨架不是游戏 —— 218 行(南境 2900 行的 7.6%), 6 个 label
## 里 4 个是「【北境第二弹第一幕正文待扩写】」占位符, 计划的 5 个结局实装 0 个, 结局路由只有
## TODO 注释 + 无条件 jump northern_ending_stub, 7 个变量声明后从未读写, 回流本体零实装。
## 去掉 developer 门 = 占位符进正式版。按南境量级写完约需 2600 行新正文。
##
## 正文写完后要挂回主线时, 下面这些**已知问题**要一并处理(本轮不修, 因为它们既不会被玩家
## 遇到、也不会被弄坏, 修了反而增加未落地内容的维护面):
##   · :50/:52 拿成就 id("southern_ruler"等)去匹配 persistent.southern_endings_seen 里的
##     结局**裸 key**("ruler"等) → southern_backer 恒为 "none", :116-122 整段南境回指是死枝
##   · :40-47 漏判第 8 个主线结局 borgia(chapter5.rpy) → 落进 else 当成没通关
##   · :163 `show storyteller_img at right` 违反 CANON.md「立绘默认 at left」
##   · :216 "感谢试玩。完整北境内容即将到来。" 是 DLC 试玩包装 —— 南境那套本轮已去掉
##     (它现在是主线目录里的「外章」), 北境挂回时同样不该再用
##   · 结局名/描述若沿用南境口径, 注意本轮已把三个南境结局降级改名, 别抄旧的

label northern_dlc_start:

    $ northern_visited = True
    $ quick_menu = True

    ## 同南境: 给已立足的属性基线, 而非主线开局新丁数值
    python:
        power = 50
        wealth = 50
        faith = 45
        loyalty = 50
        reputation = 50
        intrigue = 45
        northern_seed_attitude()   ## ② 据 persistent 定 council_stance / southern_backer

    scene black with fade
    pause 0.5

    centered "{size=+8}北境游记{/size}"
    pause 1.2
    centered "{size=+4}第二弹 · 盐路与雪原{/size}"
    pause 1.5
    scene black with dissolve

    ## ── 框架: 北上盐路出事 ──  (接南境赛琳那句"你北上那条盐路")
    play music "audio/music/tension.ogg" fadeout 1.0 fadein 2.0 if_changed

    $ hide_all_chars()
    show aldric_img at left with dissolve
    aldric "大人。北边的盐队，三天没消息了。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "走北疆那条新盐路的那一队？"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "正是。最后一封信发自雪线脚下的灰隘口。信里只来得及写四个字——'路上有人'。"

    ## ① 回指南境: 据第一弹结局, 这条盐路的来历不同
    if southern_backer == "ruler":
        aldric "这条路是您拿下潮汐港之后才铺起来的。南边的货走海，北边的盐走陆，两头都攥在您手里。断一头，另一头也悬。"
    elif southern_backer == "ally":
        aldric "南边那位渡鸦船长托人捎过话，说北路不太平，让您当心。她的人也在往北走。"
    else:
        aldric "南边的门路断了之后，这条北盐路是您手里仅剩的活钱。它再一断……"
        aldric "恕我直言，府库撑不过这个冬天。"

    aldric "北疆议会那边，希尔达伯爵夫人下了帖子，请您亲自去一趟灰隘口。"

    ## ② 读档分支: 议会对你的态度, 决定希尔达这封帖子的口气
    if council_stance == "fear":
        aldric "帖子的措辞……客气得有点过头。像是怕您，又像是在试探您带不带兵来。"
    elif council_stance == "respect":
        aldric "夫人在帖子里提了您当年的名声。北边的人记仇，也记恩。这趟，您面子上不吃亏。"
    elif council_stance == "scorn":
        aldric "帖子很短。短得近乎敷衍。北疆议会大概没把您这位领主太当回事——这趟，得您自己挣回来。"
    else:
        aldric "夫人没见过您，帖子里客客气气，分量却没下定。北疆认实力，不认头衔。"

    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "备马。我亲自走一趟。"

    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "雪线上冷。我让人多备了两件皮裘，还有……一个向导。北疆的路，外人走不得。"

    scene black with dissolve
    pause 0.5
    "三日后。灰隘口。"

    jump northern_act1


## ============================================================
## 第一幕 · 灰隘口  [开场已写, 内容待扩]
## ============================================================

label northern_act1:

    # TODO(正文): 灰隘口初探 — 斯卡蒂引路 + 盐队失踪现场 + 希尔达议会初见
    #   ① 希尔达登场(复用 countess_hilda); ② council_stance 改变她的接待
    #   参照南境第一幕"港口初探"的多点探索结构(explored_* / north_insight)

    scene black with dissolve
    $ hide_all_chars()
    show storyteller_img at right with dissolve
    skadi "再往上，马就不肯走了。剩下的路，靠腿。"
    skadi "你那队盐贩子，最后是在这片雪坡下面没的影。雪没埋住车辙——说明出事那天没下雪。"
    skadi "没下雪，车却停了。那就是人停的，不是天停的。"

    "【北境第二弹第一幕正文待扩写】"
    "—— 灰隘口探查、盐队失踪现场、希尔达议会初见，将在此展开。"

    jump northern_act2


## ============================================================
## 第二幕 · 议会与雪原  [占位]
## ============================================================

label northern_act2:

    # TODO(正文): 北疆议会博弈(希尔达 vs 沃尔德领主) + 雪原马匪"断牙"接触
    #   ② southern_backer 决定你谈判筹码; 赛琳援军(ally 时)在此兑现
    "【北境第二弹第二幕正文待扩写】"
    jump northern_act3


## ============================================================
## 第三幕 · 盐路归属  [占位]
## ============================================================

label northern_act3:

    # TODO(正文): 盐路最终归属 — 收编马匪 / 联合议会 / 武力夺路 / 撤出北疆
    "【北境第二弹第三幕正文待扩写】"
    jump northern_ending_router


## ============================================================
## 结局路由  [占位 — 5 结局对齐南境结构]
## ============================================================

label northern_ending_router:
    # TODO(正文+balance): 据 salt_route_secured / rel_hilda / council_stance 等分流
    #   预计 5 结局: 盐路独占 / 议会共治 / 雪原同盟 / 撤退止损 / 北疆陷落
    jump northern_ending_stub

label northern_ending_stub:
    scene black with dissolve
    centered "{size=+4}—— 北境游记 第二弹 ——{/size}\n{size=-2}骨架演示结局 · 正文建设中{/size}"
    pause 2.0

    $ persistent.northern_endings_seen.add("northern_stub")
    ## ★ TODO(③ 回流本体): 此处据北境结局 set persistent.northern_salt_*,
    ##    本体 chapter / 结局侧加 if 钩子给海军/边军资源或跨档成就。
    ##    动本体数值平衡, 等南境反馈后统一做。

    centered "感谢试玩。完整北境内容即将到来。"
    pause 2.0
    return

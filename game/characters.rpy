## ============================================================
## 角色定义
## ============================================================

## 主角 - 新任艾登堡领主
define player = Character("[player_name]", color="#c8b06b", image="player_char")

## 核心角色
define aldric = Character("奥尔德里克", color="#8b0000", image="aldric")
define elena = Character("艾琳娜", color="#9370db", image="elena")
define bishop = Character("主教马修斯", color="#ffd700", image="bishop")
define baron = Character("冯·哈根男爵", color="#2f4f4f", image="baron")
define captain = Character("队长雷恩", color="#4682b4", image="captain")
define queen = Character("伊莎贝拉王后", color="#800080", image="queen")
define merchant = Character("商人卡尔", color="#d2691e", image="merchant_karl")

## 第二章新增角色
define assassin = Character("???", color="#333333", image="assassin_char")

## 第三章新增角色
define lily_master = Character("暗百合首领", color="#2d1b4e", image="lily_master")

## 第四章新增角色
define prince = Character("弗雷德里克王子", color="#4169e1", image="prince")

## 第二章会前交际角色
define count_grey = Character("格雷伯爵", color="#6b8e6b", image="count_grey")
define viscount_wells = Character("威尔斯子爵", color="#b8860b", image="viscount_wells")
define countess_stein = Character("施泰因伯爵夫人", color="#708090", image="countess_stein")
define storyteller = Character("说书人", color="#c8b890", image="storyteller")

## 序章特殊角色
define bertrand = Character("伯特兰爵士", color="#8b7355", image="bertrand")

## 通用角色
define servant = Character("侍从", color="#a9a9a9", image="servant_generic")
define maid = Character("侍女", color="#a9a9a9", image="servant_marta")

## 通用角色 - 身份特化（拆分自泛用 servant，Character 名更清晰）
define accountant = Character("账房", color="#a9a9a9", image="servant_generic")
define caravan_hand = Character("车夫", color="#a9a9a9", image="servant_generic")
define herald = Character("司仪", color="#a9a9a9", image="herald")
define queen_envoy = Character("王后特使", color="#9370db", image="queen_envoy")
## 药铺老妇人 = 暗百合联络人"根"，三个 Character 是同一个人的不同身份阶段：
##   apothecary (柜台问客) → lily_interviewer (审问) → lily_root (揭示真名)
## 共用同一张老妇人立绘
define apothecary = Character("药铺老妇人", color="#8a7a6a", image="lily_root")
define lily_interviewer = Character("老妇人", color="#6a5a5a", image="lily_root")
define lily_root = Character("根", color="#5a6b5a", image="lily_root")
define messenger = Character("信使", color="#a9a9a9", image="servant_generic")
define beggar = Character("乞丐", color="#a9a9a9", image="beggar")
define court_herald = Character("司礼官", color="#daa520", image="court_herald")
define stable_boy = Character("马厩学徒", color="#a9a9a9", image="stable_boy")
define herbalist_vera = Character("草药师薇拉", color="#7a8b6a", image="herbalist_vera")
define scholar = Character("老学者", color="#a9a9a9", image="servant_generic")
define refugee = Character("难民", color="#a9a9a9", image="servant_generic")
define scout = Character("斥候", color="#a9a9a9", image="servant_generic")
define heinrich = Character("海因里希", color="#708090", image="soldier_generic")
define court_poet = Character("宫廷诗人", color="#8b3a3a", image="court_poet")
define soldier = Character("士兵", color="#708090", image="soldier_generic")
define deserter = Character("逃兵", color="#7a6a5a", image="soldier_generic")
define crowd = Character("众人", color="#a9a9a9")
define old_woman = Character("老妇人", color="#b8a898", image="old_woman")
define farmer = Character("农民", color="#a89878", image="farmer_rep")
define old_farmer = Character("老农", color="#8b7355", image="farmer_rep")
define young_blacksmith = Character("铁匠", color="#6a5a4a", image="soldier_generic")
define woman_refugee = Character("妇人", color="#c4a882", image="blacksmith_wife")
define martin = Character("马丁", color="#8b7355", image="servant_generic")
define young_soldier = Character("年轻士兵", color="#708090", image="soldier_generic")
define baron_envoy = Character("男爵密使", color="#556677", image="servant_generic")
define envoy = Character("特使", color="#9088a0", image="servant_generic")
define retired_steward = Character("退休管家", color="#8b7355", image="servant_generic")
define vanguard = Character("先锋官", color="#556677", image="soldier_generic")
define carlos = Character("卡洛斯", color="#6a5a4a", image="soldier_generic")
define servant_common = Character("仆人", color="#a9a9a9", image="servant_generic")
define veteran = Character("老兵", color="#6a5a4a", image="soldier_generic")
define little_girl = Character("小女孩", color="#e8d0b8", image="blacksmith_wife")
define old_man = Character("老人", color="#8b7355", image="farmer_rep")
define queen_rep = Character("王后方代表", color="#9370db", image="noble_werner")
define baron_rep = Character("男爵方代表", color="#2f4f4f", image="noble_werner")
define young_man = Character("少年", color="#a89878", image="servant_generic")
define enemy_general = Character("敌将", color="#8b0000", image="soldier_generic")
define young_mother = Character("年轻母亲", color="#c4a882", image="blacksmith_wife")
define commander = Character("指挥官", color="#556677", image="soldier_generic")
define wounded_man = Character("受伤男人", color="#6a5a4a", image="soldier_generic")
define guard = Character("侍卫", color="#708090", image="soldier_generic")
define blacksmith_wife = Character("铁匠之妻", color="#c4a882", image="blacksmith_wife")
define noble_lady = Character("贵族女子", color="#e8d098", image="noble_lady")
define housekeeper = Character("玛格丽特", color="#c4a882", image="servant_marta")

## ============================================================
## 数值系统
## ============================================================

default player_name = "亚瑟"

# 核心属性 (0-100)
default power = 30
default wealth = 40
default faith = 50
default loyalty = 50
default reputation = 40
default intrigue = 20

# 角色好感度 (-100 到 100)
default rel_aldric = 60
default rel_elena = 0
default rel_bishop = 30
default rel_baron = -10
default rel_captain = 50
default rel_queen = 20
default rel_prince = 0
default rel_lily = 0

# 勇气系统
default courage = 50
default max_courage = 100

# 路线印记系统
default path_marks_martial = 0
default path_marks_scheme = 0
default path_marks_faith = 0
default path_marks_diplomacy = 0
default path_active_martial = False
default path_active_scheme = False
default path_active_faith = False
default path_active_diplomacy = False

# 高属性代价标记（防止重复触发）
default power_too_high = False
default intrigue_too_high = False
default wealth_too_high = False
default faith_too_high = False

# 第一章剧情标记
default father_death_known = False
default secret_passage_found = False
default spy_network = False
default first_decree = ""

default dark_lily_first_contact = False
default dark_lily_field_intel = False

# 第二章剧情标记
default alliance_baron = False
default alliance_church = False
default merchant_deal = False
default assassination_survived = False
default council_outcome = ""

# 信息揭示标记（"已知"flag体系）
default testament_forged_known = False
default ferein_role_known = False
default matthias_has_testament_known = False
default testament_original_obtained = False
## 区分获取路径: True = 主教亲手交皮卷筒 (chapter4); False = 钥匙开假墙自取 (npc_sidelines 选项 2)
default testament_from_bishop_hand = False
default ch4_rescue_partial = False
default ch5_clash_silent = False
default ch3_prepared_first = False
default father_was_regent_known = False
default queen_poisoned_king_known = False
default father_poisoned_known = False
default elena_spy_known = False
default elena_identity_exposed_known = False
default baron_is_darkflame_known = False
default darkflame_known = False          # 知道"暗焰"这个派系的存在
default dark_lily_exists_known = False
default prince_imprisoned_known = False
default captain_truth_known = False  # 雷恩是否已从主角处得知真相（遗诏/毒杀）
default truth_declined_regency = False  # 真相结局: 婉拒首席摄政官任命, 回艾登堡 (跳过 ending_truth_epilogue 王都段)

# 第三章剧情标记
default dark_lily_joined = False  ## 任意路径"接触"影卫: 加入/铁刺/合作 都 True (剧情解锁用)
default lily_full_member = False  ## 仅"加入影卫/铁刺"为 True; "合作"分支为 False. 用于 gate 入会仪式/身份台词 (批 20 bug 修复 2026-05-26)
default dark_lily_destroyed = False
default shadow_guard_asset_revealed = False  # ch5 影卫王后女官眼线伏笔回收 (ch4_exp:1551 → ch5:1474)
default true_killer_known = False
default father_letters_found = False
default ch3_dark_lily_visited = False
default aldric_knows_passage = False
## 主角立绘版本切换 (chapter3 遇刺后 = True, 切换 player_char_scarred 立绘)
default player_scarred = False
default captain_knows_passage = False
default passage_re_opened = False
default poison_evidence = False

# 第四章剧情标记
default queen_trust = False
## 月光疾风反馈 v3.12 (2026-05-11): truth ending 王后自请退位分支
## 条件 rel_queen>=50 + prince_ally + not prince_betrayed → 私下夜谈 → 修道院静修 (非审判)
default queen_reconciled = False
default prince_ally = False
default prince_betrayed = False
default prince_returned_willingly = False
default prince_mentor_known = False
default prince_trust_deep = False
default elena_romance = False
default court_faction = ""

# 第五章/结局标记
default ending_type = ""
default iron_battle_outcome = "decisive"  # 铁腕线战役结果 (decisive 决定性胜利 / pyrrhic 惨胜) — 由左翼危机 crisis 决定
default iron_war_score = 0  # 铁腕线战力分 (花露水反馈): power/intrigue/loyalty + 领主好感 + 战前准备 累加, 决定会战成败

## ============================================================
## 持久化数据（跨存档）
## ============================================================

default persistent.chapters_completed = set()
default persistent.endings_seen = set()
default persistent.gallery_unlocked = set()
default persistent.achievements = set()

## ============================================================
## 成就系统
## ============================================================

init python:
    ## 成就数据: (名称, 描述, 隐藏?, 未解锁提示)
    achievement_data = {
        "first_steps":      ("初登大位", "完成第一章", False, "完成第一章即可解锁"),
        "diplomat":         ("舌战群雄", "通过外交解决边境危机", False, "在第一章尝试外交手段"),
        "warrior":          ("铁血领主", "通过军事手段击退男爵", False, "在第一章尝试军事手段"),
        "holy_man":         ("虔诚之心", "寻求教会帮助解决危机", False, "在第一章尝试寻求教会帮助"),
        "spy_master_ch1":   ("暗影之主", "建立间谍网络", False, "在第一章探索城堡的秘密"),
        "council_master":   ("纵横捭阖", "在领主会议中获得最佳结果", False, "在第二章领主会议中表现出色"),
        "truth_seeker":     ("真相猎人", "发现父亲死因的全部真相", False, "在第三章深入调查"),
        "secret_passage":   ("密道探索者", "发现城堡密道", False, "仔细探索城堡"),
        "village_patrol":   ("巡视村庄", "在第一章亲自走遍领地的村庄，听百姓的声音", False, "在第一章扩展剧情里完整走完巡视村庄"),
        "iron_lord":        ("铁腕领主", "达成铁腕领主结局", False, "以武力统一天下"),
        "shadow_king":      ("影中之王", "达成影中之王结局", False, "在阴影中掌控一切"),
        "holy_guardian":    ("圣光守护", "达成圣光守护结局", False, "以信仰之光照亮大地"),
        "peoples_lord":     ("人民领主", "达成人民领主结局", False, "守护最平凡的幸福"),
        "truth_ending":     ("真相大白", "达成真相大白结局", False, "追寻真相直到终点"),
        "borgia_ending":    ("毒药公爵", "达成毒药公爵坏结局", False, "童年记得母亲的狼毒草, 长大后用了它"),
        "vassal_ending":    ("附庸领主", "达成附庸领主妥协结局", False, "保住了城堡, 失去了自主"),
        "fall_ending":      ("艾登堡陷落", "达成艾登堡陷落失败结局", False, "什么都没做的代价"),
        "completionist":    ("全能领主", "解锁所有八个结局", False, "达成全部八个结局"),
        "max_stat":         ("登峰造极", "任一属性达到100", False, "将任一属性提升至最高"),
        ## 南境游记 DLC
        "southern_act1":    ("初探潮汐港", "在南境游记第一弹中作出你的抉择", False, "进入南境游记并走完第一幕"),
        "southern_free":    ("自由港", "让潮汐港作为自由港存续", False, "促成两派联合，逼退王军"),
        "southern_ruler":   ("港口新主", "掌控潮汐港，却让它失去自由", False, "倒向一方，武力守住港口"),
        "southern_fall":    ("潮汐港陷落", "潮汐港落入王廷之手", False, "与王军私下交易，出卖港口"),
        "southern_lover":   ("渡鸦与你", "与渡鸦船长赛琳缔结情谊", True, "渡 隐藏成就"),
        "southern_outwit":  ("螳螂捕蝉", "以谋略反制王廷，兵不血刃保住潮汐港", True, "谋 隐藏成就"),
        "southern_vassal":  ("王旗下的港", "促成潮汐港归附王廷，保住自治", False, "归附王廷换自治"),
        ## 隐藏成就 — 未解锁前不显示名称和描述
        "romeo":            ("权谋情圣", "与艾琳娜达成浪漫关系", True, "心 隐藏成就"),
        "betrayer":         ("背信弃义", "背叛弗雷德里克王子", True, "! 隐藏成就"),
        "merchant_prince":  ("商业巨擘", "财富达到100且与商人卡尔合作", True, "金 隐藏成就"),
        "lone_wolf":        ("独行之狼", "不与任何势力结盟通关", True, "狼 隐藏成就"),
        "silver_tongue":    ("银舌如蛇", "谋略达到100", True, "刃 隐藏成就"),
        "all_friends":      ("八面玲珑", "所有角色好感度达到60以上", True, "* 隐藏成就"),
        "dark_path":        ("深渊凝视", "加入暗百合且谋略大于80", True, "暗 隐藏成就"),
        "pacifist":         ("和平使者", "不使用军事手段通关", True, "和 隐藏成就"),
    }

    ## 属性预警阈值
    STAT_DANGER_LOW = 15
    STAT_DANGER_HIGH = 90
    STAT_WARNING_MESSAGES = {
        "power":      ("权力过低，男爵可能发动进攻！", "权力极高，引起了王后的警惕..."),
        "wealth":     ("财库将尽，领地运转困难！", "富可敌国，有人在觊觎你的财富..."),
        "faith":      ("信仰不足，教会对你心存不满！", "虔诚至极，主教视你为圣人"),
        "loyalty":    ("民心涣散，叛乱一触即发！", "忠诚无双，领民誓死追随"),
        "reputation": ("声名扫地，无人愿与你合作！", "声名远扬，天下皆知你的大名"),
        "intrigue":   ("谋略不足，容易被人暗算！", "深不可测，所有人都忌惮你"),
    }

    ## 属性变化历史（用于趋势箭头）
    _stat_history = {}

    def unlock_achievement(name):
        if name not in persistent.achievements:
            persistent.achievements.add(name)
            if name in achievement_data:
                renpy.show_screen("achievement_popup", ach_name=achievement_data[name][0], ach_desc=achievement_data[name][1])
                renpy.play("audio/sfx/ui_confirm.ogg", channel="sound")

    def check_max_stat():
        for val in [power, wealth, faith, loyalty, reputation, intrigue]:
            if val >= 100:
                unlock_achievement("max_stat")
                return

    def check_hidden_achievements():
        """检查隐藏成就条件"""
        if store.elena_romance:
            unlock_achievement("romeo")
        if store.prince_betrayed:
            unlock_achievement("betrayer")
        if store.wealth >= 100 and store.merchant_deal:
            unlock_achievement("merchant_prince")
        if store.intrigue >= 100:
            unlock_achievement("silver_tongue")
        if store.dark_lily_joined and store.intrigue > 80:
            unlock_achievement("dark_path")
        ## 八面玲珑：所有关系>=60
        all_rels = [store.rel_aldric, store.rel_elena, store.rel_bishop,
                    store.rel_baron, store.rel_captain, store.rel_queen]
        if all(r >= 60 for r in all_rels):
            unlock_achievement("all_friends")

    def get_stat_trend(stat_name):
        """获取属性趋势： 「up」， 「down」， 「stable」"""
        history = _stat_history.get(stat_name, [])
        if len(history) < 2:
            return "stable"
        recent = history[-3:] if len(history) >= 3 else history
        diff = recent[-1] - recent[0]
        if diff > 0:
            return "up"
        elif diff < 0:
            return "down"
        return "stable"

    def record_stat(stat_name, value):
        """记录属性变化历史"""
        if stat_name not in _stat_history:
            _stat_history[stat_name] = []
        _stat_history[stat_name].append(value)
        if len(_stat_history[stat_name]) > 10:
            _stat_history[stat_name] = _stat_history[stat_name][-10:]

    def get_stat_warning(stat_name):
        """获取属性预警信息，返回 None 或警告文本"""
        val = getattr(store, stat_name, 50)
        msgs = STAT_WARNING_MESSAGES.get(stat_name)
        if not msgs:
            return None
        if val <= STAT_DANGER_LOW:
            return msgs[0]
        if val >= STAT_DANGER_HIGH:
            return msgs[1]
        return None

    ## clamp_stats() 已移至 attr_system.rpy，此处不再重复定义。

## ============================================================
## 存档兼容性处理
## save_compat.rpy
## 确保旧版存档在新版本中正确加载
## ============================================================


################################################################################
## 0. 老档迁移：南境游记并入主线目录
################################################################################
## 「南境游记」原本是主菜单上单开的一栏(screens.rpy 原 443-467), 现已并入「章节选择」
## 的「外章」。章节选择的解锁判据是 `ch_id in persistent.chapters_completed`
## (gallery.rpy:426), 而 chapters_completed 的 6 个写点(prologue.rpy / script.rpy /
## chapter2-5)没有一个写过 "southern" —— 老档里这个 key 永远为空。
##
## 后果: 已通关南境的老玩家, 结局图鉴里明明记着 5/5, 却因为主菜单入口被删、章节选择又
## 判他没通关, 而**永久失去重玩南境的途径**。同一行也兜住音乐室的 6 首南境 BGM
## (gallery.rpy 的 southern_* 解锁条件本次由 None 改成 "southern")。
##
## **必须放 init python, 不能放下面的 after_load** —— after_load 只在读档时跑, 而章节
## 选择和音乐室是主菜单上的 persistent 驱动界面, 玩家盯着主菜单时它根本不触发。
init python:
    if persistent.southern_endings_seen:
        if persistent.chapters_completed is None:
            persistent.chapters_completed = set()
        persistent.chapters_completed.add("southern")

    def legacy_true_implies_mastermind(
            legacy_true_killer_known,
            prince_ally=False,
            prince_answer_pending=False,
            ch3_dark_lily_visited=False,
            decisions=None):
        """旧 true flag 只有带可靠第四/五章来源时才能升级为幕后主使认知。"""
        if not legacy_true_killer_known:
            return False
        if prince_ally or prince_answer_pending:
            return True
        for decision in decisions or ():
            if (len(decision) >= 2
                    and decision[0] == "第五章"
                    and decision[1] in (
                        "战前答复王子，结成同盟",
                        "战前回绝王子",
                    )):
                return True
        ## ch3_dark_lily_visited 特意不构成幕后主使来源。
        return False


################################################################################
## 1. after_load 标签 — 旧存档加载后初始化缺失的变量
################################################################################

label after_load:
    ## 初始化新版本添加的 persistent 变量（旧存档可能缺少）
    if not hasattr(persistent, 'collectibles_found') or persistent.collectibles_found is None:
        $ persistent.collectibles_found = set()
    if not hasattr(persistent, 'ng_plus_unlocked') or persistent.ng_plus_unlocked is None:
        $ persistent.ng_plus_unlocked = False
    if not hasattr(persistent, 'ng_plus_bonus_power'):
        $ persistent.ng_plus_bonus_power = 0
    if not hasattr(persistent, 'ng_plus_bonus_wealth'):
        $ persistent.ng_plus_bonus_wealth = 0
    if not hasattr(persistent, 'ng_plus_bonus_intrigue'):
        $ persistent.ng_plus_bonus_intrigue = 0
    if not hasattr(persistent, 'difficulty') or persistent.difficulty is None:
        $ persistent.difficulty = "normal"
    if not hasattr(persistent, 'text_size_offset'):
        $ persistent.text_size_offset = 0
    if not hasattr(persistent, 'high_contrast'):
        $ persistent.high_contrast = False
    if not hasattr(persistent, 'rel_events_triggered') or persistent.rel_events_triggered is None:
        $ persistent.rel_events_triggered = set()
    if not hasattr(persistent, 'chapters_completed') or persistent.chapters_completed is None:
        $ persistent.chapters_completed = set()
    if not hasattr(persistent, 'endings_seen') or persistent.endings_seen is None:
        $ persistent.endings_seen = set()
    if not hasattr(persistent, 'gallery_unlocked') or persistent.gallery_unlocked is None:
        $ persistent.gallery_unlocked = set()
    if not hasattr(persistent, 'achievements') or persistent.achievements is None:
        $ persistent.achievements = set()
    if not hasattr(persistent, 'tutorial_seen'):
        $ persistent.tutorial_seen = False
    if not hasattr(persistent, 'rating_asked'):
        $ persistent.rating_asked = False

    ## ================================================================
    ## 存档迁移：追溯补设"信息已知"flag（11个）
    ## 问题：老存档在这些flag添加前已过揭示点，flag始终为False，
    ##       导致后续守卫检查永远不触发"已知态"文本
    ## 策略：根据玩家当前进度（章节完成记录 + 剧情标记）推断
    ##       哪些信息应已获知，兜底补设。新存档不受影响。
    ## ================================================================
    python:
        _ch = persistent.chapters_completed if persistent.chapters_completed else set()

        ## 3.9.2 将父亲遇害证据拆成三层；先补缺失字段，再按可信度递增迁移。
        if not hasattr(store, "father_poison_method_known"):
            father_poison_method_known = False
        if not hasattr(store, "father_poison_executor_known"):
            father_poison_executor_known = False
        if not hasattr(store, "father_murder_mastermind_known"):
            father_murder_mastermind_known = False

        ## 推断章节进度（兼容缺少 chapters_completed 的极老存档）
        ## save_compat 的职责就是兜底老存档 —— 任何裸变量访问都可能 NameError
        _past_ch2 = (
            ("chapter1" in _ch)
            or getattr(store, "father_death_known", False)
            or getattr(store, "alliance_baron", False)
            or getattr(store, "alliance_church", False)
            or getattr(store, "assassination_survived", False)
        )
        ## 修复：("chapter2" in _ch) 仅说明完成了第二章，玩家可能在第三章日记场景之前
        ## 使用 father_letters_found 或 ("chapter3" in _ch) 确保日记已读
        _past_ch3 = (
            ("chapter3" in _ch)
            or getattr(store, "father_letters_found", False)
            or getattr(store, "dark_lily_joined", False)
            or getattr(store, "dark_lily_destroyed", False)
            or getattr(store, "true_killer_known", False)
            or getattr(store, "ch3_dark_lily_visited", False)
        )
        ## 修复：王子被软禁是第五章揭示，需要完成第四章才确保已知
        _past_ch4 = (
            ("chapter4" in _ch)
            or getattr(store, "prince_ally", False)
            or getattr(store, "prince_betrayed", False)
        )

        ## ---- 第二章揭示 ----
        ## 父亲被毒杀（条件：调查过商人Karl，已有 poison_evidence）
        if _past_ch2 and (getattr(store, "father_death_known", False) or getattr(store, "poison_evidence", False)):
            father_poisoned_known = True

        ## ---- 父亲遇害证据链迁移（保守、幂等） ----
        if (getattr(store, "poison_evidence", False)
                or getattr(store, "father_poisoned_known", False)):
            father_poison_method_known = True

        _legacy_true = getattr(store, "true_killer_known", False)
        _hq_disclosure_complete = (
            getattr(store, "dark_lily_joined", False)
            or getattr(store, "dark_lily_destroyed", False)
        )
        if _legacy_true and _hq_disclosure_complete:
            father_poison_executor_known = True

        if legacy_true_implies_mastermind(
                _legacy_true,
                prince_ally=getattr(store, "prince_ally", False),
                prince_answer_pending=getattr(store, "prince_answer_pending", False),
                ch3_dark_lily_visited=getattr(store, "ch3_dark_lily_visited", False),
                decisions=getattr(store, "_decisions", ())):
            father_murder_mastermind_known = True

        ## ---- 第三章主线揭示（父亲日记解读，必经剧情） ----
        if _past_ch3:
            testament_forged_known = True       # 遗诏被篡改
            ferein_role_known = True             # 费雷恩销毁原件
            father_was_regent_known = True       # 父亲本应是摄政者
            queen_poisoned_king_known = True     # 王后毒杀先王
            dark_lily_exists_known = True        # 暗百合组织存在
            matthias_has_testament_known = True  # 马修斯持有遗诏线索
            if not hasattr(store, 'ch3_prepared_first'):
                ch3_prepared_first = False

        ## ---- 第三章条件揭示（暗百合线路） ----
        ## elena身份 + 男爵暗焰身份在暗百合剧情中揭示
        if _past_ch3 and (
            getattr(store, "dark_lily_joined", False)
            or getattr(store, "dark_lily_destroyed", False)
            or getattr(store, "ch3_dark_lily_visited", False)
        ):
            elena_spy_known = True              # 艾琳娜是三重间谍
            elena_identity_exposed_known = True # 艾琳娜身份暴露
            baron_is_darkflame_known = True     # 男爵是暗焰首领
            darkflame_known = True              # 知道暗焰派系存在

        ## elena身份也可能通过高好感随机事件揭示（interludes.rpy）
        if _past_ch2 and getattr(store, "rel_elena", 0) >= 40:
            elena_spy_known = True
            elena_identity_exposed_known = True

        ## elena 身份通过 npc_elena_past 支线揭露 (npc_sidelines.rpy L458+)
        ## 该支线末尾必然 set elena_spy_known=True；老存档若走过此支线但 flag 丢失，兜底
        if getattr(store, "elena_dark_past_done", False):
            elena_spy_known = True
            elena_identity_exposed_known = True
            dusk_dew_known = True  # 支线里艾琳娜也提及遗诏/暮色之露/教会秘密

        ## 注：不以 "_past_ch3 + rel_elena >= 20" 作为追溯条件——chapter3 有多条分支，
        ## 只有暗百合/主动对峙/高好感随机事件等特定路径才触发揭露。用户可能只
        ## 读过父亲日记、好感度增长到 20 就被误判；过宽兜底反而制造"玩家不知道
        ## 却被说成已知"的错觉。仅在明确证据的分支下才追溯。

        ## ---- 第四章揭示 ----
        if _past_ch4:
            prince_imprisoned_known = True      # 王子被软禁

        ## ---- 领主初见标记追溯 ----
        ## wells_met/grey_met/steinfurt_met 在领主会议(chapter2.rpy L1541+)首次 set=True
        ## 老存档加载新版本时这些 flag 可能残留 False, 导致"重复初见"台词
        ## 任何 chapter2 之后的进度都保证三位领主已见过
        if _past_ch2 or getattr(store, "council_outcome", ""):
            wells_met = True
            grey_met = True
            steinfurt_met = True
            ## 商人卡尔在 chapter2 会后集市偶遇(ch2_after_council L2052+)是强制剧情
            ## 因此 past_ch2 必然见过卡尔
            karl_met = True
            ## 主教马修斯在 chapter1 主教来访(script.rpy L466+)是必经剧情
            ## past_ch2 必然见过主教
            bishop_met = True
            ## chapter2 开头 L56 强制 call npc_captain_past (城墙雷恩往事)
            ## past_ch2 必然听过完整的格伦瓦德往事
            captain_past_done = True

        ## ---- 纵横捭阖成就追授 ----
        ## 修复 bug：该成就原无任何 unlock_achievement 调用点，
        ## 已走过"折中"分支的老存档需要补发
        if getattr(store, 'council_outcome', '') == "折中":
            if 'council_master' not in persistent.achievements:
                persistent.achievements.add('council_master')

        ## ---- 王子弗雷德里克初见追溯 ----
        ## prince 在 chapter4 王都宴会(chapter4.rpy L1277)才首次登场
        if _past_ch4:
            prince_met = True

        ## ---- 遗诏原件持有追溯 ----
        ## 主教醉酒忏悔里给了地下室钥匙 (bishop_gave_key=True)，
        ## 或 chapter4 主教直接交出皮卷筒 (testament_original_obtained=True)
        ## 都说明玩家实际持有原件。若老存档因版本旧丢失 flag，追溯补设。
        if getattr(store, "bishop_gave_key", False):
            testament_original_obtained = True
            matthias_has_testament_known = True

        ## ---- 暮色之露认知追溯 ----
        ## 多条路径可触发首次接触: 卡尔情报(ch2_after_council)、暗百合磨坊(ch2_end)、
        ## 父亲日记(ch3)、暗百合首领揭秘(ch3)、艾琳娜坦白(ch3)
        ## 任一毒药相关 flag 为 True 都说明玩家必然已接触过"暮色之露"这个词
        if (getattr(store, "poison_evidence", False)
                or getattr(store, "father_poisoned_known", False)
                or getattr(store, "queen_poisoned_king_known", False)
                or getattr(store, "dark_lily_first_contact", False)
                or _past_ch3):
            dusk_dew_known = True

        ## ---- 密道知情追溯（栀子 T+7 反馈） ----
        ## chapter1_deepening 「告诉奥尔德里克和雷恩」选项叙事承诺告知两人，
        ## 老版本只设 ch1_deep_cellar_choice="tell"，未同步 aldric/captain knows flag
        ## random_events_new.rpy re_old_map_secret/shared 也承诺告知雷恩，
        ## 老版本只设 aldric_knows_passage=True，未同步 captain_knows_passage
        if getattr(store, "ch1_deep_cellar_choice", "") == "tell":
            aldric_knows_passage = True
            captain_knows_passage = True
        if getattr(store, "aldric_knows_passage", False):
            captain_knows_passage = True

    ## ================================================================
    ## 立绘叠加清理：旧存档保存时 layer 上可能堆了多个立绘
    ## Ren'Py 存档会序列化 layer 状态, 加载后 hide_all_chars 是运行时调用,
    ## 对已存档的 layer 残留无追溯效果 —— 必须在 after_load 主动清一次
    ##
    ## 代价：若存档点正好卡在双人同屏(at left + at right)对话中，
    ##       加载后会暂时缺失一侧立绘，下一次 show 指令会补回来
    ## 收益：彻底解决旧存档立绘重合/堆叠现象
    ## ================================================================
    $ hide_all_chars()

    return


################################################################################
## 2. init python — 处理旧存档中缺失的 store 变量
################################################################################

init 999 python:
    ## 使用高优先级确保在所有其他 init 之后执行

    def _compat_init_store_vars():
        """
        检查并初始化旧存档可能缺少的 store 变量。
        在 after_load 时由引擎自动处理 default 声明的变量，
        但某些动态添加的变量需要手动检查。
        """

        ## 第一章基本变量
        _store_defaults = {
            ## 核心属性
            "player_name": "亚瑟",
            "power": 30,
            "wealth": 40,
            "faith": 50,
            "loyalty": 50,
            "reputation": 40,
            "intrigue": 20,

            ## 角色好感度
            "rel_aldric": 60,
            "rel_elena": 0,
            "rel_bishop": 30,
            "rel_baron": -10,
            "rel_captain": 50,
            "rel_queen": 20,
            "rel_prince": 0,
            "rel_lily": 0,

            ## 第一章剧情标记
            "father_death_known": False,
            "secret_passage_found": False,
            "spy_network": False,
            "first_decree": "",

            ## 第二章剧情标记
            "alliance_baron": False,
            "alliance_church": False,
            "merchant_deal": False,
            "assassination_survived": False,
            "council_outcome": "",
            "wells_met": False,
            "grey_met": False,
            "steinfurt_met": False,
            "karl_met": False,
            "bishop_met": False,
            "prince_met": False,
            "dusk_dew_known": False,
            "dark_lily_first_contact": False,
            "dark_lily_field_intel": False,
            "captain_past_done": False,
            "lily_trial_passed": False,
            "bishop_gave_key": False,
            "bishop_confession_done": False,
            "testament_original_obtained": False,
            "testament_from_bishop_hand": False,
            "matthias_has_testament_known": False,
            "stein_origin_revealed": False,
            "ch4_rescue_partial": False,
            "ch5_clash_silent": False,

            ## 第三章剧情标记
            "dark_lily_joined": False,
            "dark_lily_destroyed": False,
            "father_poison_method_known": False,
            "father_poison_executor_known": False,
            "father_murder_mastermind_known": False,
            "true_killer_known": False,
            "father_letters_found": False,
            "ch3_dark_lily_visited": False,
            "aldric_knows_passage": False,
            "captain_knows_passage": False,
            "passage_re_opened": False,
            "poison_evidence": False,
            "elena_spy_known": False,
            "elena_identity_exposed_known": False,
            "elena_dark_past_done": False,
            "elena_trust_deep": False,

            ## 第四章剧情标记
            "queen_trust": False,
            "prince_ally": False,
            "prince_betrayed": False,
            "elena_romance": False,
            "court_faction": "",

            ## 第五章/结局标记
            "ending_type": "",
        }

        for var_name, default_val in _store_defaults.items():
            if not hasattr(store, var_name):
                setattr(store, var_name, default_val)

    ## 注册到 after_load 回调链中
    ## 这样即使 label after_load 之外也能确保变量完整
    config.after_load_callbacks.append(_compat_init_store_vars)

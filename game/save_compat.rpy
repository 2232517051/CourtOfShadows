## ============================================================
## 存档兼容性处理
## save_compat.rpy
## 确保旧版存档在新版本中正确加载
## ============================================================


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

        ## 推断章节进度（兼容缺少 chapters_completed 的极老存档）
        _past_ch2 = ("chapter1" in _ch) or father_death_known or alliance_baron or alliance_church or assassination_survived
        _past_ch3 = ("chapter2" in _ch) or dark_lily_joined or dark_lily_destroyed or true_killer_known or father_letters_found or ch3_dark_lily_visited
        _past_ch4 = ("chapter3" in _ch) or queen_trust or prince_ally or prince_betrayed

        ## ---- 第二章揭示 ----
        ## 父亲被毒杀（条件：调查过商人Karl，已有 poison_evidence）
        if _past_ch2 and (father_death_known or poison_evidence):
            father_poisoned_known = True

        ## ---- 第三章主线揭示（父亲日记解读，必经剧情） ----
        if _past_ch3:
            testament_forged_known = True       # 遗诏被篡改
            ferein_role_known = True             # 费雷恩销毁原件
            father_was_regent_known = True       # 父亲本应是摄政者
            queen_poisoned_king_known = True     # 王后毒杀先王
            dark_lily_exists_known = True        # 暗百合组织存在
            matthias_has_testament_known = True  # 马修斯持有遗诏线索

        ## ---- 第三章条件揭示（暗百合线路） ----
        ## elena身份 + 男爵暗焰身份在暗百合剧情中揭示
        if _past_ch3 and (dark_lily_joined or dark_lily_destroyed or ch3_dark_lily_visited):
            elena_spy_known = True              # 艾琳娜是三重间谍
            elena_identity_exposed_known = True # 艾琳娜身份暴露
            baron_is_darkflame_known = True     # 男爵是暗焰首领
            darkflame_known = True              # 知道暗焰派系存在

        ## elena身份也可能通过高好感随机事件揭示（interludes.rpy）
        if _past_ch2 and rel_elena >= 40:
            elena_spy_known = True
            elena_identity_exposed_known = True

        ## ---- 第四章揭示 ----
        if _past_ch4:
            prince_imprisoned_known = True      # 王子被软禁

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

            ## 第三章剧情标记
            "dark_lily_joined": False,
            "dark_lily_destroyed": False,
            "true_killer_known": False,
            "father_letters_found": False,
            "ch3_dark_lily_visited": False,
            "aldric_knows_passage": False,
            "poison_evidence": False,

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

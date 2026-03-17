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

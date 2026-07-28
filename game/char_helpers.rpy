## ════════════════════════════════════════════════════════════
## char_helpers.rpy — 立绘叠加防御性清理
##
## 设计目的:
##   之前的立绘管理靠"手动 hide X → show Y"配对. 当 menu 分支漏写 hide,
##   或从存档中段加载时, 残留立绘会叠加在新角色下方.
##
## 使用方式 (推荐):
##   在切到新 NPC 前调一次 $ hide_all_chars()
##   然后 show new_npc_img at left with dissolve
##
## 也可以指定不 hide 某个 tag:
##   $ hide_all_chars("player_char_img")  # 只保留玩家立绘
## ════════════════════════════════════════════════════════════

init python:

    CHAR_IMG_TAGS = [
        "aldric_img", "assassin_char_img", "baron_img", "beggar_img",
        "bertrand_img", "bishop_img", "blacksmith_wife_img", "bully_kid_img",
        "captain_img", "count_grey_img", "countess_hilda_img",
        "countess_stein_img", "court_herald_img", "court_poet_img",
        "edmund_img", "edmund_masked_img", "elena_img",
        "farmer_rep_img", "father_img", "friend_marcus_img", "healer_img",
        "herald_img", "herbalist_vera_img",
        ## ingrid: 2026-07-24 玩家 bjhhfdffffddd 报"王都见英格丽后立绘卡住不走" —— 她的
        ## 会面戏靠段尾 hide_all_chars() 清场, 而这个 tag 一直没注册, 遍历不到清不掉,
        ## 一路残留到艾琳娜出场(chapter4:1127)。联姻线在 ch4/ch5/endings 共 26 处 show,
        ## 全是同一雷。这正是 CLAUDE.md 立绘规范第 2 条要求"四处对齐"的原因。
        "ingrid_img",
        "lily_master_img", "lily_root_img",
        "merchant_guild_img", "merchant_karl_img", "mother_img",
        "noble_lady_img", "noble_werner_img", "old_guard_img", "old_woman_img",
        "player_char_img", "player_child_img", "player_teen_img",
        "player_young_img", "priest_thomas_img", "prince_img", "queen_img",
        "queen_envoy_img", "servant_generic_img", "servant_marta_img",
        "soldier_generic_img", "stable_boy_img", "storyteller_img",
        "tax_collector_img", "tutor_img", "village_elder_img",
        "viscount_wells_img",
        ## 南境游记 DLC
        "corsair_img", "guild_master_img", "ship_boy_img", "dockhand_img",
        "old_salt_img", "sea_dog_img", "chen_captain_img",
        "harbor_master_img", "tavern_keeper_img", "royal_admiral_img",
    ]

    def hide_all_chars(*except_tags):
        """Hide all known character sprites. Pass tag names to keep them.

        Example:
            hide_all_chars()                     # 清全部
            hide_all_chars("captain_img")        # 保留 captain
            hide_all_chars("captain_img", "bishop_img")
        """
        except_set = set(except_tags)
        for img_tag in CHAR_IMG_TAGS:
            if img_tag in except_set:
                continue
            # renpy.hide 接受 tag 名 (不带 _img 后缀也能, 但 image 定义里完整名是 foo_img)
            try:
                renpy.hide(img_tag)
            except Exception:
                pass

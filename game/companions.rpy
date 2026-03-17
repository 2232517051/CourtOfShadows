## ============================================================
## 同伴系统 - Companion / Squad System
## companions.rpy
## NPC可作为战斗同伴加入队伍
## ============================================================

## ── 同伴追踪变量 ──
default recruited_companions = set()
default active_companions = [None, None]  # 最多2个战斗槽位
default companion_equipment = {}  # {comp_id: {"weapon": item_id, "armor": item_id}}
default companion_injuries = {}  # {comp_id: int} 受伤减益
default companion_skill_used = set()  # 本场战斗已使用技能的同伴

init python:

    ## ================================================================
    ## 同伴数据库
    ## ================================================================

    companion_data = {
        "comp_aldric": {
            "name": "奥尔德里克",
            "title": "忠诚骑士",
            "char_color": "#8b0000",
            "rel_var": "rel_aldric",
            "loyalty_req": 40,
            "base_hp": 120,
            "base_attack": 35,
            "base_defense": 30,
            "base_dodge": 10,
            "base_stamina": 90,
            "role": "tank",  # tank / dps / support
            "skill": ("坚守防线", "defend_ally", "为领主挡下一次攻击，自身承受50%伤害"),
            "recruit_chapter": 1,
            "desc": "你父亲的老管家，曾是一名骁勇的骑士。虽然年事已高，但剑术不减当年。他对你的忠诚超越了主仆之情。",
        },
        "comp_captain": {
            "name": "队长雷恩",
            "title": "卫队长",
            "char_color": "#4682b4",
            "rel_var": "rel_captain",
            "loyalty_req": 30,
            "base_hp": 100,
            "base_attack": 40,
            "base_defense": 20,
            "base_dodge": 20,
            "base_stamina": 100,
            "role": "dps",
            "skill": ("精准打击", "precise_strike", "忽视敌方30%防御的精准攻击"),
            "recruit_chapter": 1,
            "desc": "艾登堡卫队的队长，身经百战的职业军人。作战风格冷静而高效，是你最可靠的武力后盾。",
        },
        "comp_elena": {
            "name": "艾琳娜",
            "title": "暗影侍女",
            "char_color": "#9370db",
            "rel_var": "rel_elena",
            "loyalty_req": 50,
            "base_hp": 70,
            "base_attack": 25,
            "base_defense": 10,
            "base_dodge": 35,
            "base_stamina": 80,
            "role": "dps",
            "skill": ("毒刃", "poison_strike", "附带毒素的攻击，3回合内持续造成伤害"),
            "recruit_chapter": 2,
            "desc": "你的侍女，但她的身手远非普通女仆。暗百合的训练让她精通暗杀与潜伏，是暗影中最致命的利刃。",
        },
        "comp_bishop_knight": {
            "name": "圣骑士马库斯",
            "title": "主教卫士",
            "char_color": "#ffd700",
            "rel_var": "rel_bishop",
            "loyalty_req": 45,
            "base_hp": 110,
            "base_attack": 30,
            "base_defense": 35,
            "base_dodge": 5,
            "base_stamina": 85,
            "role": "support",
            "skill": ("神圣祝福", "holy_bless", "治疗全队20HP，并移除一个负面状态"),
            "recruit_chapter": 2,
            "desc": "主教马修斯的贴身护卫，虔诚的圣骑士。擅长防御和治疗，信仰是他最强大的武器。",
        },
        "comp_lily_agent": {
            "name": "影",
            "title": "暗百合密探",
            "char_color": "#2d1b4e",
            "rel_var": "rel_lily",
            "loyalty_req": 30,
            "base_hp": 60,
            "base_attack": 45,
            "base_defense": 5,
            "base_dodge": 40,
            "base_stamina": 70,
            "role": "dps",
            "skill": ("暗杀", "assassinate", "对生命值低于30%的敌人造成三倍伤害"),
            "recruit_chapter": 3,
            "desc": "暗百合组织派来协助你的密探，真名不详。身法诡异，攻击致命，但生命力脆弱，一击即溃。",
        },
    }

    ## ================================================================
    ## 装备加成数据
    ## ================================================================

    _equipment_bonuses = {
        ## 武器 (增加攻击力)
        "blessed_mace":  {"attack": 15, "defense": 0, "name": "祝福战锤"},
        "war_paint":     {"attack": 8,  "defense": 0, "name": "战争涂料"},
        ## 防具 (增加防御力)
        "gambeson":      {"attack": 0,  "defense": 10, "name": "棉甲"},
        "chainmail":     {"attack": 0,  "defense": 20, "name": "锁子甲"},
        "bandage":       {"attack": 0,  "defense": 3,  "name": "绷带"},
    }

    _weapon_items = {"blessed_mace", "war_paint"}
    _armor_items = {"gambeson", "chainmail", "bandage"}

    ## ================================================================
    ## 同伴核心函数
    ## ================================================================

    def is_companion_available(comp_id):
        """检查同伴是否可招募（章节 + 好感度）"""
        data = companion_data.get(comp_id)
        if not data:
            return False
        ## 主菜单/游戏未开始时不可招募
        if store.main_menu or not getattr(store, 'first_decree', ''):
            return False
        ch = _get_current_chapter_num()
        if ch < data["recruit_chapter"]:
            return False
        rel_val = getattr(store, data["rel_var"], 0)
        if rel_val < data["loyalty_req"]:
            return False
        return True

    def recruit_companion(comp_id):
        """招募同伴"""
        if comp_id not in companion_data:
            return False
        if comp_id in store.recruited_companions:
            return False
        if not is_companion_available(comp_id):
            return False
        store.recruited_companions.add(comp_id)
        ## 初始化装备槽
        if comp_id not in store.companion_equipment:
            store.companion_equipment[comp_id] = {"weapon": None, "armor": None}
        ## 显示招募通知
        name = companion_data[comp_id]["name"]
        renpy.show_screen("companion_toast", comp_name=name, is_recruit=True)
        return True

    def dismiss_companion(comp_id):
        """解散同伴"""
        if comp_id in store.recruited_companions:
            store.recruited_companions.discard(comp_id)
            ## 从激活槽移除
            for idx in range(len(store.active_companions)):
                if store.active_companions[idx] == comp_id:
                    store.active_companions[idx] = None
            ## 卸下装备归还背包
            if comp_id in store.companion_equipment:
                equip = store.companion_equipment[comp_id]
                if equip.get("weapon"):
                    add_item(equip["weapon"], 1)
                if equip.get("armor"):
                    add_item(equip["armor"], 1)
                del store.companion_equipment[comp_id]
            name = companion_data[comp_id]["name"]
            renpy.show_screen("companion_toast", comp_name=name, is_recruit=False)
            return True
        return False

    def get_recruited_companions():
        """获取所有已招募的同伴ID列表"""
        return [cid for cid in companion_data if cid in store.recruited_companions]

    def get_active_companions():
        """获取当前激活的战斗同伴ID列表"""
        return [cid for cid in store.active_companions if cid is not None]

    def set_active_companion(comp_id, slot):
        """设置战斗槽位（slot: 0 或 1）"""
        if slot < 0 or slot > 1:
            return False
        if comp_id is not None and comp_id not in store.recruited_companions:
            return False
        ## 如果同伴已在另一个槽位，先移除
        if comp_id is not None:
            for idx in range(len(store.active_companions)):
                if store.active_companions[idx] == comp_id:
                    store.active_companions[idx] = None
        store.active_companions[slot] = comp_id
        return True

    def get_companion_morale(comp_id):
        """获取同伴士气。基于好感度。"""
        data = companion_data.get(comp_id)
        if not data:
            return 0
        rel_val = getattr(store, data["rel_var"], 0)
        if rel_val > 60:
            return "high"      # 高昂: +10% 全属性
        elif rel_val >= 20:
            return "normal"    # 正常
        elif rel_val >= -20:
            return "low"       # 低落: -20% 全属性
        else:
            return "desert"    # 可能叛逃

    def get_morale_label(morale):
        """士气文本"""
        labels = {
            "high": ("士气高昂", "#2ecc71"),
            "normal": ("士气正常", "#8a7e60"),
            "low": ("士气低落", "#e67e22"),
            "desert": ("可能叛逃", "#e74c3c"),
        }
        return labels.get(morale, ("未知", "#6a5e48"))

    def get_companion_stats(comp_id):
        """获取同伴当前战斗属性（含装备和士气加成）"""
        data = companion_data.get(comp_id)
        if not data:
            return {}

        stats = {
            "hp": data["base_hp"],
            "attack": data["base_attack"],
            "defense": data["base_defense"],
            "dodge": data["base_dodge"],
            "stamina": data["base_stamina"],
        }

        ## 装备加成
        equip = store.companion_equipment.get(comp_id, {})
        for slot_key in ["weapon", "armor"]:
            item_id = equip.get(slot_key)
            if item_id and item_id in _equipment_bonuses:
                bonus = _equipment_bonuses[item_id]
                stats["attack"] += bonus.get("attack", 0)
                stats["defense"] += bonus.get("defense", 0)

        ## 士气加成
        morale = get_companion_morale(comp_id)
        if morale == "high":
            for k in stats:
                stats[k] = int(stats[k] * 1.1)
        elif morale == "low":
            for k in stats:
                stats[k] = int(stats[k] * 0.8)
        elif morale == "desert":
            for k in stats:
                stats[k] = int(stats[k] * 0.6)

        ## 受伤减益
        injury = store.companion_injuries.get(comp_id, 0)
        if injury > 0:
            stats["hp"] = max(10, stats["hp"] - injury)

        return stats

    def equip_companion(comp_id, item_id, slot="weapon"):
        """给同伴装备物品。slot: weapon / armor"""
        if comp_id not in store.recruited_companions:
            return False
        if not has_item(item_id):
            return False
        if slot == "weapon" and item_id not in _weapon_items:
            return False
        if slot == "armor" and item_id not in _armor_items:
            return False

        equip = store.companion_equipment.get(comp_id, {"weapon": None, "armor": None})

        ## 卸下当前装备
        old_item = equip.get(slot)
        if old_item:
            add_item(old_item, 1)

        ## 装备新物品
        remove_item(item_id, 1)
        equip[slot] = item_id
        store.companion_equipment[comp_id] = equip
        return True

    def unequip_companion(comp_id, slot="weapon"):
        """卸下同伴装备"""
        if comp_id not in store.recruited_companions:
            return False
        equip = store.companion_equipment.get(comp_id, {"weapon": None, "armor": None})
        old_item = equip.get(slot)
        if old_item:
            add_item(old_item, 1)
            equip[slot] = None
            store.companion_equipment[comp_id] = equip
            return True
        return False

    def companion_take_turn(comp_id, enemy_hp, enemy_max_hp, enemy_defense=10):
        """
        AI战斗回合。返回 (action_name, damage_dealt, description)
        """
        data = companion_data.get(comp_id)
        if not data:
            return ("idle", 0, "无法行动")

        stats = get_companion_stats(comp_id)
        morale = get_companion_morale(comp_id)
        role = data["role"]
        skill_name, skill_id, skill_desc = data["skill"]

        ## 士气极低可能拒绝行动
        if morale == "desert":
            if renpy.random.randint(1, 100) <= 40:
                return ("refuse", 0, "%s 拒绝了你的命令！" % data["name"])

        ## 检查是否可以使用技能（每场战斗只能用一次）
        can_use_skill = comp_id not in store.companion_skill_used

        ## AI决策逻辑
        if role == "support" and can_use_skill:
            ## 支援型：优先使用技能
            store.companion_skill_used.add(comp_id)
            return ("skill", 20, "%s 使用了「%s」—— %s" % (data["name"], skill_name, skill_desc))

        elif role == "tank":
            if can_use_skill and renpy.random.randint(1, 100) <= 50:
                ## 坦克型：50%概率使用防御技能
                store.companion_skill_used.add(comp_id)
                return ("skill", 0, "%s 使用了「%s」—— %s" % (data["name"], skill_name, skill_desc))
            else:
                ## 普通攻击
                dmg = max(1, stats["attack"] - enemy_defense // 2)
                dmg = int(dmg * (renpy.random.randint(80, 120) / 100.0))
                return ("attack", dmg, "%s 发起攻击，造成 %d 点伤害！" % (data["name"], dmg))

        elif role == "dps":
            ## DPS型：敌人血量低时使用技能
            enemy_pct = enemy_hp / max(1, enemy_max_hp)
            if can_use_skill and skill_id == "assassinate" and enemy_pct < 0.3:
                store.companion_skill_used.add(comp_id)
                dmg = stats["attack"] * 3
                return ("skill", dmg, "%s 使用了「%s」—— 致命一击！造成 %d 点伤害！" % (data["name"], skill_name, dmg))
            elif can_use_skill and skill_id == "poison_strike" and renpy.random.randint(1, 100) <= 60:
                store.companion_skill_used.add(comp_id)
                dmg = max(1, stats["attack"] - enemy_defense // 3)
                return ("skill", dmg, "%s 使用了「%s」—— 毒素蔓延！造成 %d 点伤害，并施加中毒！" % (data["name"], skill_name, dmg))
            elif can_use_skill and skill_id == "precise_strike" and renpy.random.randint(1, 100) <= 50:
                store.companion_skill_used.add(comp_id)
                dmg = max(1, stats["attack"] - int(enemy_defense * 0.7) // 2)
                dmg = int(dmg * 1.3)
                return ("skill", dmg, "%s 使用了「%s」—— 精准打击！造成 %d 点伤害！" % (data["name"], skill_name, dmg))
            else:
                dmg = max(1, stats["attack"] - enemy_defense // 2)
                dmg = int(dmg * (renpy.random.randint(80, 120) / 100.0))
                return ("attack", dmg, "%s 发起攻击，造成 %d 点伤害！" % (data["name"], dmg))

        ## 默认普通攻击
        dmg = max(1, stats["attack"] - enemy_defense // 2)
        dmg = int(dmg * (renpy.random.randint(80, 120) / 100.0))
        return ("attack", dmg, "%s 发起攻击，造成 %d 点伤害！" % (data["name"], dmg))

    def reset_companion_skills():
        """重置所有同伴技能（每场战斗开始时调用）"""
        store.companion_skill_used = set()

    def check_companion_desertion():
        """检查是否有同伴叛逃。在章节过渡时调用。"""
        deserted = []
        for comp_id in list(store.recruited_companions):
            morale = get_companion_morale(comp_id)
            if morale == "desert":
                if renpy.random.randint(1, 100) <= 30:
                    name = companion_data[comp_id]["name"]
                    dismiss_companion(comp_id)
                    deserted.append(name)
        return deserted


## ── 同伴招募/离开通知 ──
screen companion_toast(comp_name="", is_recruit=True):
    zorder 260
    $ _ct_color = "#d4a942" if is_recruit else "#e74c3c"
    $ _ct_icon = "+" if is_recruit else "-"
    $ _ct_text = "加入了队伍" if is_recruit else "离开了队伍"

    frame at stat_toast_anim:
        xalign 0.5
        ypos 100
        background Solid("#0f0d1aee")
        xpadding 24
        ypadding 10

        hbox:
            spacing 8
            text _ct_icon size 18 color _ct_color yalign 0.5
            text comp_name size 16 color "#e0d8c8" font "msyh.ttf" bold True yalign 0.5
            text _ct_text size 14 color _ct_color font "msyh.ttf" yalign 0.5

    timer 3.0 action Hide("companion_toast")


## ================================================================
## 同伴管理界面
## ================================================================

screen companions_screen():
    tag menu
    modal True
    zorder 150

    default selected_companion = None
    default equip_mode = None  # None / "weapon" / "armor"

    add Solid("#000000aa") at stats_overlay_show
    key "K_ESCAPE" action Hide("companions_screen")
    key "K_c" action Hide("companions_screen")
    key "game_menu" action Hide("companions_screen")

    frame at stats_panel_show:
        xalign 0.5
        yalign 0.5
        xpadding 0
        ypadding 0
        if renpy.variant("small"):
            xsize 0.98
            ysize 0.92
        else:
            xsize 850
            ysize 620

        background Solid("#0f0d1af0")

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
                        text "盾" size 22 color "#d4a942" yalign 0.5
                        text "同伴管理" size 24 color "#d4a942" font "msyh.ttf" bold True yalign 0.5

                    hbox:
                        xalign 1.0
                        spacing 12

                        ## 激活同伴数
                        $ _active_n = len(get_active_companions())
                        text "出战: [_active_n]/2" size 14 color "#8a7e60" yalign 0.5

                        textbutton "X":
                            text_size 20
                            text_color "#6a5e48"
                            text_hover_color "#d4a942"
                            action Hide("companions_screen")

            add Solid("#d4a94230") xsize 1.0 ysize 2

            ## ── 主内容: 左右分栏 ──
            hbox:
                spacing 0
                xfill True

                ## ════════════════════════════════
                ## 左栏: 同伴列表
                ## ════════════════════════════════
                frame:
                    if renpy.variant("small"):
                        xsize 0.38
                    else:
                        xsize 300
                    yfill True
                    background None
                    xpadding 0
                    ypadding 0

                    vbox:
                        spacing 0

                        ## 已招募同伴
                        frame:
                            xfill True
                            ysize 32
                            xpadding 16
                            background Solid("#1a152830")
                            text "已招募同伴" size 13 color "#8a7e60" font "msyh.ttf" yalign 0.5

                        viewport:
                            xfill True
                            yfill True
                            mousewheel True
                            draggable True

                            frame:
                                background None
                                xpadding 8
                                ypadding 8

                                vbox:
                                    spacing 2

                                    $ _recruited = get_recruited_companions()

                                    if not _recruited:
                                        null height 30
                                        text "暂无同伴" size 14 color "#6a5e48" font "msyh.ttf" xalign 0.5
                                        text "满足好感度条件后\n可招募角色为同伴" size 11 color "#4a4030" xalign 0.5 text_align 0.5

                                    for _cid in _recruited:
                                        $ _cdata = companion_data[_cid]
                                        $ _c_morale = get_companion_morale(_cid)
                                        $ _c_morale_label, _c_morale_color = get_morale_label(_c_morale)
                                        $ _c_is_active = _cid in store.active_companions
                                        $ _c_selected = (selected_companion == _cid)

                                        button:
                                            xfill True
                                            xpadding 10
                                            ypadding 10
                                            if _c_selected:
                                                background Solid("#d4a94220")
                                            else:
                                                background Solid("#1a152820")
                                            hover_background Solid("#1a152860")
                                            action SetScreenVariable("selected_companion", _cid)

                                            hbox:
                                                spacing 8
                                                yalign 0.5
                                                xfill True

                                                ## 名称和职称
                                                vbox:
                                                    spacing 2
                                                    hbox:
                                                        spacing 6
                                                        text _cdata["name"] size 15 color _cdata["char_color"] font "msyh.ttf" bold True
                                                        if _c_is_active:
                                                            text "出战" size 10 color "#d4a942" yalign 0.5

                                                    text _cdata["title"] size 11 color "#6a5e48"

                                                ## 士气
                                                text "*" size 12 color _c_morale_color xalign 1.0 yalign 0.5

                                    ## 可招募但未招募的同伴提示
                                    null height 12
                                    $ _unrecruited = [cid for cid in companion_data if cid not in store.recruited_companions]
                                    if _unrecruited:
                                        text "* 可招募" size 13 color "#6a5e4880" font "msyh.ttf"
                                        null height 4

                                        for _ucid in _unrecruited:
                                            $ _ucdata = companion_data[_ucid]
                                            $ _uc_avail = is_companion_available(_ucid)
                                            $ _uc_rel = getattr(store, _ucdata["rel_var"], 0)

                                            frame:
                                                xfill True
                                                xpadding 10
                                                ypadding 6
                                                background Solid("#1a152810")

                                                vbox:
                                                    spacing 2
                                                    text _ucdata["name"] size 13 color ("#6a5e48" if not _uc_avail else "#d4a942") font "msyh.ttf"
                                                    if not _uc_avail:
                                                        $ _uc_ch_ok = _get_current_chapter_num() >= _ucdata["recruit_chapter"]
                                                        if not _uc_ch_ok:
                                                            text "需要: 第[_ucdata['recruit_chapter']]章" size 10 color "#4a4030"
                                                        else:
                                                            text "好感度: [_uc_rel]/[_ucdata['loyalty_req']]" size 10 color "#4a4030"
                                                    else:
                                                        textbutton "招募":
                                                            text_size 12
                                                            text_color "#d4a942"
                                                            text_hover_color "#ffd866"
                                                            action [Function(recruit_companion, _ucid), SetScreenVariable("selected_companion", _ucid)]

                ## 分隔线
                add Solid("#d4a94220") xsize 1 ysize 1.0

                ## ════════════════════════════════
                ## 右栏: 同伴详情
                ## ════════════════════════════════
                frame:
                    xfill True
                    yfill True
                    background None
                    xpadding 0
                    ypadding 0

                    if selected_companion is None or selected_companion not in store.recruited_companions:
                        vbox:
                            xalign 0.5
                            yalign 0.5
                            spacing 8
                            text "盾" size 40 color "#1a1528" xalign 0.5
                            text "选择一个同伴" size 16 color "#6a5e48" font "msyh.ttf" xalign 0.5
                            text "查看详细信息" size 12 color "#4a4030" xalign 0.5
                    else:
                        $ _sc = companion_data[selected_companion]
                        $ _sc_stats = get_companion_stats(selected_companion)
                        $ _sc_morale = get_companion_morale(selected_companion)
                        $ _sc_morale_label, _sc_morale_color = get_morale_label(_sc_morale)
                        $ _sc_rel = getattr(store, _sc["rel_var"], 0)
                        $ _sc_equip = store.companion_equipment.get(selected_companion, {"weapon": None, "armor": None})
                        $ _sc_is_active = selected_companion in store.active_companions
                        $ _sc_role_names = {"tank": "坦克", "dps": "输出", "support": "辅助"}

                        viewport:
                            xfill True
                            yfill True
                            mousewheel True
                            draggable True
                            scrollbars "vertical"

                            frame:
                                background None
                                xpadding 20
                                ypadding 16
                                xfill True

                                vbox:
                                    spacing 10

                                    ## 名称与职称
                                    hbox:
                                        spacing 12

                                        frame:
                                            xsize 50
                                            ysize 50
                                            background Solid(_sc["char_color"] + "30")
                                            text _sc["name"][:1] xalign 0.5 yalign 0.5 size 26 color _sc["char_color"] font "msyh.ttf" bold True

                                        vbox:
                                            text _sc["name"] size 24 color _sc["char_color"] font "msyh.ttf" bold True
                                            hbox:
                                                spacing 8
                                                text _sc["title"] size 13 color "#8a7e60"
                                                text "([_sc_role_names.get(_sc['role'], '未知')])" size 12 color "#6a5e48"

                                    ## 描述
                                    text _sc["desc"] size 13 color "#c8b890" font "msyh.ttf" line_spacing 4

                                    add Solid("#d4a94220") xsize 1.0 ysize 1

                                    ## ── 士气与好感 ──
                                    hbox:
                                        spacing 20

                                        vbox:
                                            spacing 2
                                            text "士气" size 12 color "#8a7e60"
                                            text _sc_morale_label size 15 color _sc_morale_color bold True

                                        vbox:
                                            spacing 2
                                            text "好感度" size 12 color "#8a7e60"
                                            text "[_sc_rel]" size 15 color _sc["char_color"] bold True

                                    ## 好感度条
                                    $ _sc_rel_pct = (_sc_rel + 100) / 200.0
                                    bar:
                                        value StaticValue(_sc_rel_pct, 1.0)
                                        xfill True
                                        ysize 6
                                        left_bar Solid(_sc["char_color"])
                                        right_bar Solid("#1a1528")

                                    add Solid("#d4a94220") xsize 1.0 ysize 1

                                    ## ── 战斗属性 ──
                                    text "* 战斗属性" size 15 color "#d4a942" font "msyh.ttf"

                                    grid 3 2:
                                        spacing 8
                                        xfill True

                                        for _skey, _slabel, _scolor in [("hp", "生命", "#2ecc71"), ("attack", "攻击", "#e74c3c"), ("defense", "防御", "#3498db"), ("dodge", "闪避", "#9b59b6"), ("stamina", "耐力", "#f39c12")]:
                                            frame:
                                                xsize 140
                                                xpadding 8
                                                ypadding 6
                                                background Solid("#1a152830")

                                                vbox:
                                                    spacing 2
                                                    text _slabel size 11 color "#8a7e60"
                                                    text str(_sc_stats.get(_skey, 0)) size 16 color _scolor bold True

                                        ## 空白填充grid
                                        null

                                    add Solid("#d4a94220") xsize 1.0 ysize 1

                                    ## ── 特殊技能 ──
                                    text "* 特殊技能" size 15 color "#d4a942" font "msyh.ttf"

                                    frame:
                                        xfill True
                                        xpadding 12
                                        ypadding 10
                                        background Solid("#1a152840")

                                        vbox:
                                            spacing 4
                                            text _sc["skill"][0] size 16 color _sc["char_color"] font "msyh.ttf" bold True
                                            text _sc["skill"][2] size 13 color "#c8b890" font "msyh.ttf"
                                            text "每场战斗可使用一次" size 11 color "#6a5e48"

                                    add Solid("#d4a94220") xsize 1.0 ysize 1

                                    ## ── 装备 ──
                                    text "* 装备" size 15 color "#d4a942" font "msyh.ttf"

                                    ## 武器槽
                                    frame:
                                        xfill True
                                        xpadding 12
                                        ypadding 8
                                        background Solid("#1a152830")

                                        hbox:
                                            spacing 10
                                            yalign 0.5
                                            xfill True

                                            text "武器:" size 13 color "#8a7e60" yalign 0.5 xsize 50

                                            if _sc_equip.get("weapon"):
                                                $ _w_name = _equipment_bonuses.get(_sc_equip["weapon"], {}).get("name", "未知")
                                                $ _w_atk = _equipment_bonuses.get(_sc_equip["weapon"], {}).get("attack", 0)
                                                text "[_w_name] (+[_w_atk]攻击)" size 14 color "#e0d8c8" font "msyh.ttf" yalign 0.5

                                                textbutton "卸下":
                                                    xalign 1.0
                                                    text_size 12
                                                    text_color "#e74c3c"
                                                    text_hover_color "#ff6b6b"
                                                    action [Function(unequip_companion, selected_companion, "weapon"), renpy.restart_interaction]
                                            else:
                                                text "空" size 13 color "#4a4030" yalign 0.5

                                                ## 可装备的武器列表
                                                $ _avail_weapons = [wid for wid in _weapon_items if has_item(wid)]
                                                if _avail_weapons:
                                                    for _wid in _avail_weapons:
                                                        $ _w_name = _equipment_bonuses.get(_wid, {}).get("name", _wid)
                                                        textbutton "装备[_w_name]":
                                                            xalign 1.0
                                                            text_size 11
                                                            text_color "#d4a942"
                                                            text_hover_color "#ffd866"
                                                            action [Function(equip_companion, selected_companion, _wid, "weapon"), renpy.restart_interaction]

                                    ## 护甲槽
                                    frame:
                                        xfill True
                                        xpadding 12
                                        ypadding 8
                                        background Solid("#1a152830")

                                        hbox:
                                            spacing 10
                                            yalign 0.5
                                            xfill True

                                            text "护甲:" size 13 color "#8a7e60" yalign 0.5 xsize 50

                                            if _sc_equip.get("armor"):
                                                $ _a_name = _equipment_bonuses.get(_sc_equip["armor"], {}).get("name", "未知")
                                                $ _a_def = _equipment_bonuses.get(_sc_equip["armor"], {}).get("defense", 0)
                                                text "[_a_name] (+[_a_def]防御)" size 14 color "#e0d8c8" font "msyh.ttf" yalign 0.5

                                                textbutton "卸下":
                                                    xalign 1.0
                                                    text_size 12
                                                    text_color "#e74c3c"
                                                    text_hover_color "#ff6b6b"
                                                    action [Function(unequip_companion, selected_companion, "armor"), renpy.restart_interaction]
                                            else:
                                                text "空" size 13 color "#4a4030" yalign 0.5

                                                $ _avail_armors = [aid for aid in _armor_items if has_item(aid)]
                                                if _avail_armors:
                                                    for _aid in _avail_armors:
                                                        $ _a_name = _equipment_bonuses.get(_aid, {}).get("name", _aid)
                                                        textbutton "装备[_a_name]":
                                                            xalign 1.0
                                                            text_size 11
                                                            text_color "#d4a942"
                                                            text_hover_color "#ffd866"
                                                            action [Function(equip_companion, selected_companion, _aid, "armor"), renpy.restart_interaction]

                                    add Solid("#d4a94220") xsize 1.0 ysize 1

                                    ## ── 出战控制 ──
                                    text "* 出战管理" size 15 color "#d4a942" font "msyh.ttf"

                                    hbox:
                                        spacing 10

                                        ## 槽位1
                                        $ _slot0 = store.active_companions[0]
                                        $ _slot0_name = companion_data[_slot0]["name"] if _slot0 else "空"
                                        $ _slot0_is_this = (_slot0 == selected_companion)

                                        frame:
                                            xsize 200
                                            xpadding 12
                                            ypadding 8
                                            background Solid("#d4a94215" if _slot0_is_this else "#1a152830")

                                            vbox:
                                                spacing 4
                                                text "槽位 1" size 12 color "#8a7e60"
                                                text _slot0_name size 14 color ("#d4a942" if _slot0 else "#4a4030") font "msyh.ttf"
                                                if not _slot0_is_this:
                                                    textbutton "设为槽位1":
                                                        text_size 12
                                                        text_color "#d4a942"
                                                        text_hover_color "#ffd866"
                                                        action [Function(set_active_companion, selected_companion, 0), renpy.restart_interaction]
                                                else:
                                                    textbutton "移除":
                                                        text_size 12
                                                        text_color "#e74c3c"
                                                        text_hover_color "#ff6b6b"
                                                        action [Function(set_active_companion, None, 0), renpy.restart_interaction]

                                        ## 槽位2
                                        $ _slot1 = store.active_companions[1]
                                        $ _slot1_name = companion_data[_slot1]["name"] if _slot1 else "空"
                                        $ _slot1_is_this = (_slot1 == selected_companion)

                                        frame:
                                            xsize 200
                                            xpadding 12
                                            ypadding 8
                                            background Solid("#d4a94215" if _slot1_is_this else "#1a152830")

                                            vbox:
                                                spacing 4
                                                text "槽位 2" size 12 color "#8a7e60"
                                                text _slot1_name size 14 color ("#d4a942" if _slot1 else "#4a4030") font "msyh.ttf"
                                                if not _slot1_is_this:
                                                    textbutton "设为槽位2":
                                                        text_size 12
                                                        text_color "#d4a942"
                                                        text_hover_color "#ffd866"
                                                        action [Function(set_active_companion, selected_companion, 1), renpy.restart_interaction]
                                                else:
                                                    textbutton "移除":
                                                        text_size 12
                                                        text_color "#e74c3c"
                                                        text_hover_color "#ff6b6b"
                                                        action [Function(set_active_companion, None, 1), renpy.restart_interaction]

                                    null height 8

                                    ## ── 解散按钮 ──
                                    textbutton "解散同伴":
                                        xalign 0.5
                                        text_size 14
                                        text_color "#e74c3c80"
                                        text_hover_color "#e74c3c"
                                        action [Function(dismiss_companion, selected_companion), SetScreenVariable("selected_companion", None), renpy.restart_interaction]


## ================================================================
## 快捷键: C 打开同伴管理
## ================================================================

init python:
    def toggle_companions():
        if renpy.get_screen("companions_screen"):
            renpy.hide_screen("companions_screen")
        else:
            renpy.show_screen("companions_screen")
        renpy.restart_interaction()

    config.underlay.append(renpy.Keymap(c=toggle_companions))


## ================================================================
## 同伴叛逃事件标签
## ================================================================

label check_companion_desertion_event:
    $ _deserted_list = check_companion_desertion()
    if _deserted_list:
        $ _deserted_msg = "、".join(_deserted_list)
        "你收到消息：[_deserted_msg]因为对你失望透顶，已经悄然离开了队伍。"
        "也许你应该更加关注同伴的感受。"
    return


## ================================================================
## 同伴招募快捷标签 (供剧本调用)
## ================================================================
## 用法:
##     $ recruit_companion("comp_aldric")
##     $ recruit_companion("comp_captain")
##
## 或在剧情中:
##     call try_recruit_companion("comp_elena")

label try_recruit_companion(comp_id=""):
    if comp_id == "":
        return

    $ _tr_data = companion_data.get(comp_id, None)
    if _tr_data is None:
        return

    if comp_id in recruited_companions:
        "[_tr_data['name']]已经是你的同伴了。"
        return

    if not is_companion_available(comp_id):
        $ _tr_rel = getattr(store, _tr_data["rel_var"], 0)
        "你还没有赢得[_tr_data['name']]足够的信任（好感度 [_tr_rel]/[_tr_data['loyalty_req']]）。"
        return

    $ recruit_companion(comp_id)
    "[_tr_data['name']]加入了你的队伍！"
    "[_tr_data['name']] —— [_tr_data['title']]"
    "特殊技能：「[_tr_data['skill'][0]]」—— [_tr_data['skill'][2]]"
    return

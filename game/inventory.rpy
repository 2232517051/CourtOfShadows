## ============================================================
## 物品与装备系统 — inventory.rpy
## 权谋之庭 (Court of Shadows)
## 按 I 键打开背包 / 商店通过剧情调用
## ============================================================


################################################################################
## 1. 物品数据库
################################################################################

init python:

    ## 稀有度配置: (颜色, 中文标签)
    RARITY_CONFIG = {
        "common":    ("#b8a878", "普通"),
        "rare":      ("#9370db", "稀有"),
        "legendary": ("#ffd700", "传说"),
    }

    ## 物品类型图标
    ITEM_TYPE_ICONS = {
        "weapon":     "剑",
        "armor":      "甲",
        "trinket":    "饰",
        "consumable": "药",
        "material":   "材",
    }

    ## 武器子类型图标
    WEAPON_SUBTYPE_ICONS = {
        "sword":  "剑",
        "axe":    "斧",
        "mace":   "锤",
        "spear":  "矛",
        "dagger": "刃",
    }

    ## ──────────────────────────────────────────────
    ## 物品数据库
    ## 格式: item_id -> {
    ##   "name": 中文名,
    ##   "type": weapon/armor/trinket/consumable/material,
    ##   "subtype": (武器子类型, 可选),
    ##   "stats": {属性字典},
    ##   "price": 购买价格(金币),
    ##   "rarity": common/rare/legendary,
    ##   "desc": 描述文字,
    ## }
    ## ──────────────────────────────────────────────

    items_database = {

        ## ═══ 剑类 (平衡型) ═══
        "iron_sword": {
            "name": "铁剑", "type": "weapon", "subtype": "sword",
            "stats": {"damage": 5, "accuracy": 5},
            "price": 20, "rarity": "common",
            "desc": "一把普通的铁剑，可靠耐用。",
        },
        "knight_sword": {
            "name": "骑士长剑", "type": "weapon", "subtype": "sword",
            "stats": {"damage": 10, "accuracy": 8, "crit": 5},
            "price": 80, "rarity": "rare",
            "desc": "精心打造的骑士佩剑，剑刃上刻着家族纹章。",
        },
        "royal_blade": {
            "name": "王室之刃", "type": "weapon", "subtype": "sword",
            "stats": {"damage": 15, "accuracy": 10, "crit": 10},
            "price": 200, "rarity": "legendary",
            "desc": "曾属于一位伟大国王的传世名剑。",
        },

        ## ═══ 斧类 (高伤害, 低命中) ═══
        "battle_axe": {
            "name": "战斧", "type": "weapon", "subtype": "axe",
            "stats": {"damage": 12, "accuracy": -5, "armor_break": 10},
            "price": 35, "rarity": "common",
            "desc": "沉重的战斧，能轻易劈开盾牌。",
        },
        "executioner_axe": {
            "name": "行刑之斧", "type": "weapon", "subtype": "axe",
            "stats": {"damage": 18, "accuracy": -8, "crit": 15},
            "price": 120, "rarity": "rare",
            "desc": "刽子手的专用武器，令人胆寒。",
        },

        ## ═══ 锤类 (反甲) ═══
        "iron_mace": {
            "name": "铁锤", "type": "weapon", "subtype": "mace",
            "stats": {"damage": 8, "accuracy": 0, "armor_break": 15},
            "price": 25, "rarity": "common",
            "desc": "沉重的铁锤，对付重甲敌人的利器。",
        },
        "blessed_mace": {
            "name": "祝福战锤", "type": "weapon", "subtype": "mace",
            "stats": {"damage": 12, "accuracy": 3, "armor_break": 20, "faith_req": 40},
            "price": 150, "rarity": "rare",
            "desc": "由主教亲自祝福的圣战锤。",
        },

        ## ═══ 矛类 (高命中, 先手) ═══
        "hunting_spear": {
            "name": "猎矛", "type": "weapon", "subtype": "spear",
            "stats": {"damage": 6, "accuracy": 12, "first_strike": True},
            "price": 18, "rarity": "common",
            "desc": "猎人用的长矛，攻击距离远。",
        },
        "halberd": {
            "name": "戟", "type": "weapon", "subtype": "spear",
            "stats": {"damage": 14, "accuracy": 8, "first_strike": True},
            "price": 100, "rarity": "rare",
            "desc": "兼具刺击和劈砍的长柄武器。",
        },

        ## ═══ 匕首类 (高暴击) ═══
        "dagger": {
            "name": "匕首", "type": "weapon", "subtype": "dagger",
            "stats": {"damage": 3, "accuracy": 15, "crit": 20},
            "price": 15, "rarity": "common",
            "desc": "轻巧的匕首，适合暗杀。",
        },
        "assassin_blade": {
            "name": "刺客之刃", "type": "weapon", "subtype": "dagger",
            "stats": {"damage": 8, "accuracy": 12, "crit": 30},
            "price": 160, "rarity": "rare",
            "desc": "暗百合组织使用的特制短刃。",
        },

        ## ═══ 护甲 ═══
        "leather_armor": {
            "name": "皮甲", "type": "armor",
            "stats": {"defense": 8, "dodge": -2},
            "price": 15, "rarity": "common",
            "desc": "柔软的皮革护甲，提供基本防护。",
        },
        "gambeson": {
            "name": "棉甲", "type": "armor",
            "stats": {"defense": 10, "dodge": -3},
            "price": 25, "rarity": "common",
            "desc": "厚实的棉质护甲，性价比极高。",
        },
        "chainmail": {
            "name": "锁子甲", "type": "armor",
            "stats": {"defense": 15, "dodge": -8},
            "price": 60, "rarity": "rare",
            "desc": "精细的锁子甲，骑士的标配。",
        },
        "shadow_cloak": {
            "name": "暗影斗篷", "type": "armor",
            "stats": {"defense": 5, "dodge": 15},
            "price": 140, "rarity": "rare",
            "desc": "暗百合的特制斗篷，轻如鸿毛。",
        },
        "plate_armor": {
            "name": "板甲", "type": "armor",
            "stats": {"defense": 25, "dodge": -15},
            "price": 180, "rarity": "legendary",
            "desc": "全身板甲，几乎刀枪不入。",
        },

        ## ═══ 饰品 ═══
        "lucky_coin": {
            "name": "幸运金币", "type": "trinket",
            "stats": {"crit": 8, "wealth_bonus": 3},
            "price": 30, "rarity": "common",
            "desc": "据说能带来好运的古老金币。",
        },
        "war_medal": {
            "name": "战功勋章", "type": "trinket",
            "stats": {"damage": 5, "power_bonus": 3},
            "price": 50, "rarity": "rare",
            "desc": "战场上赢得的荣誉勋章。",
        },
        "holy_cross": {
            "name": "圣十字架", "type": "trinket",
            "stats": {"defense": 5, "faith_bonus": 5},
            "price": 45, "rarity": "rare",
            "desc": "教会赐予的护身圣物。",
        },
        "spy_ring": {
            "name": "密探戒指", "type": "trinket",
            "stats": {"crit": 12, "intrigue_bonus": 5},
            "price": 70, "rarity": "rare",
            "desc": "暗百合的身份信物，内藏毒针。",
        },
        "royal_signet": {
            "name": "王室印戒", "type": "trinket",
            "stats": {"defense": 3, "reputation_bonus": 8},
            "price": 100, "rarity": "legendary",
            "desc": "王室赐予的权力象征。",
        },
        "rabbit_foot": {
            "name": "兔足挂坠", "type": "trinket",
            "stats": {"dodge": 10, "luck": 20},
            "price": 35, "rarity": "common",
            "desc": "毛茸茸的兔足，据说能逢凶化吉。",
        },
        "torture_mask": {
            "name": "苦行面具", "type": "trinket",
            "stats": {"defense": 10, "hp_bonus": 20, "dodge": -10},
            "price": 90, "rarity": "rare",
            "desc": "苦修者的面具，承受痛苦换取坚韧。",
        },

        ## ═══ 消耗品 ═══
        "health_potion": {
            "name": "治疗药水", "type": "consumable",
            "stats": {"heal": 30},
            "price": 10, "rarity": "common",
            "desc": "能恢复体力的草药药水。",
        },
        "stamina_potion": {
            "name": "耐力药水", "type": "consumable",
            "stats": {"stamina_restore": 40},
            "price": 12, "rarity": "common",
            "desc": "提振精神的浓缩药剂。",
        },
        "antidote": {
            "name": "解毒药", "type": "consumable",
            "stats": {"cure_poison": True},
            "price": 15, "rarity": "common",
            "desc": "能解除大部分毒素。",
        },
        "bandage": {
            "name": "绷带", "type": "consumable",
            "stats": {"heal": 15, "cure_bleed": True},
            "price": 5, "rarity": "common",
            "desc": "简单的止血绷带。",
        },
        "war_paint": {
            "name": "战争涂料", "type": "consumable",
            "stats": {"buff_damage": 10, "buff_turns": 3},
            "price": 20, "rarity": "rare",
            "desc": "涂抹后提升战斗力的特殊颜料。",
        },
        "smoke_bomb": {
            "name": "烟雾弹", "type": "consumable",
            "stats": {"guaranteed_flee": True},
            "price": 25, "rarity": "rare",
            "desc": "点燃后能掩护撤退的烟雾装置。",
        },

        ## ═══ 制作材料 ═══
        "iron_ore": {
            "name": "铁矿石", "type": "material",
            "stats": {},
            "price": 5, "rarity": "common",
            "desc": "艾登堡铁矿产出的矿石。",
        },
        "medicinal_herbs": {
            "name": "药草", "type": "material",
            "stats": {},
            "price": 3, "rarity": "common",
            "desc": "山间采集的药用植物。",
        },
        "leather_scraps": {
            "name": "皮革碎片", "type": "material",
            "stats": {},
            "price": 4, "rarity": "common",
            "desc": "制甲剩余的皮革。",
        },
        "holy_water": {
            "name": "圣水", "type": "material",
            "stats": {},
            "price": 8, "rarity": "rare",
            "desc": "教堂祝福过的清水。",
        },
        "dark_lily_extract": {
            "name": "暗百合精华", "type": "material",
            "stats": {},
            "price": 15, "rarity": "rare",
            "desc": "暗百合花提炼的神秘液体。",
        },
        "waterskin": {
            "name": "水袋", "type": "material",
            "stats": {},
            "price": 2, "rarity": "common",
            "desc": "装水用的皮袋。",
        },
    }

    ## 属性中文名映射 (用于UI显示)
    STAT_DISPLAY_NAMES = {
        "damage": "伤害",
        "accuracy": "命中",
        "crit": "暴击",
        "armor_break": "破甲",
        "first_strike": "先手",
        "defense": "防御",
        "dodge": "闪避",
        "heal": "恢复",
        "stamina_restore": "耐力恢复",
        "cure_poison": "解毒",
        "cure_bleed": "止血",
        "buff_damage": "伤害增益",
        "buff_turns": "持续回合",
        "guaranteed_flee": "必定逃脱",
        "hp_bonus": "生命加成",
        "luck": "幸运",
        "faith_req": "信仰需求",
        ## 角色属性加成
        "power_bonus": "权力加成",
        "wealth_bonus": "财富加成",
        "faith_bonus": "信仰加成",
        "loyalty_bonus": "忠诚加成",
        "reputation_bonus": "声望加成",
        "intrigue_bonus": "谋略加成",
    }


################################################################################
## 2. 游戏变量
################################################################################

## 背包: 列表，每个元素为 [item_id, quantity]
default inventory_items = []

## 装备槽
default equipped_weapon = None
default equipped_armor = None
default equipped_trinket = None

## 背包选中项 (UI用)
default _inv_selected = None

## 商店库存 (由剧情设置)
default _shop_stock = []

## 商店名称
default _shop_name = "商店"

## 金币 (基于 wealth 属性: gold = wealth * 5)
## 额外金币存储 (超出 wealth 计算的部分)
default extra_gold = 0


################################################################################
## 3. 背包核心函数
################################################################################

init python:

    def get_gold():
        """获取当前金币总数（下限为0，永不为负）"""
        return max(0, store.wealth * 5 + store.extra_gold)

    def set_gold(amount):
        """设置金币数量 (调整 extra_gold)"""
        store.extra_gold = amount - store.wealth * 5

    def modify_gold(delta):
        """增减金币（扣减后保证总金币不低于0）"""
        store.extra_gold += delta
        # 确保金币总数不为负
        if store.wealth * 5 + store.extra_gold < 0:
            store.extra_gold = -(store.wealth * 5)

    def get_max_inventory_slots():
        """背包最大容量： 20 + power // 15"""
        return 20 + store.power // 15

    def get_inventory_count():
        """当前背包中不同物品的种类数"""
        return len(store.inventory_items)

    def get_inventory():
        """返回背包字典 {item_id: qty}，供 crafting 等模块使用"""
        return {iid: qty for iid, qty in store.inventory_items}

    def _find_inv_index(item_id):
        """查找物品在背包中的索引，找不到返回 -1"""
        for i, (iid, qty) in enumerate(store.inventory_items):
            if iid == item_id:
                return i
        return -1

    def add_item(item_id, qty=1):
        """
        将物品添加到背包。
        返回 True 表示成功, False 表示背包已满。
        """
        if item_id not in items_database:
            return False

        idx = _find_inv_index(item_id)
        if idx >= 0:
            ## 已有该物品，增加数量
            store.inventory_items[idx] = (item_id, store.inventory_items[idx][1] + qty)
            return True
        else:
            ## 新物品，检查背包空间
            if get_inventory_count() >= get_max_inventory_slots():
                return False
            store.inventory_items.append((item_id, qty))
            return True

    def remove_item(item_id, qty=1):
        """
        从背包移除物品。
        返回 True 表示成功, False 表示数量不足。
        """
        idx = _find_inv_index(item_id)
        if idx < 0:
            return False

        current_qty = store.inventory_items[idx][1]
        if current_qty < qty:
            return False

        if current_qty == qty:
            store.inventory_items.pop(idx)
        else:
            store.inventory_items[idx] = (item_id, current_qty - qty)
        return True

    def has_item(item_id, qty=1):
        """检查是否持有指定数量的物品"""
        idx = _find_inv_index(item_id)
        if idx < 0:
            return False
        return store.inventory_items[idx][1] >= qty

    def get_item_qty(item_id):
        """获取物品持有数量"""
        idx = _find_inv_index(item_id)
        if idx < 0:
            return 0
        return store.inventory_items[idx][1]

    get_item_count = get_item_qty

    def equip_item(item_id):
        """
        装备物品。自动卸下同槽位旧装备放回背包。
        返回 True 成功, False 失败 (不在背包/类型不对/需求不满足)。
        """
        if not has_item(item_id):
            return False

        info = items_database.get(item_id)
        if not info:
            return False

        item_type = info["type"]
        stats = info["stats"]

        ## 检查信仰需求
        if "faith_req" in stats and store.faith < stats["faith_req"]:
            return False

        ## 确定槽位
        if item_type == "weapon":
            slot = "equipped_weapon"
        elif item_type == "armor":
            slot = "equipped_armor"
        elif item_type == "trinket":
            slot = "equipped_trinket"
        else:
            return False  ## 消耗品和材料不能装备

        ## 卸下旧装备
        old_item = getattr(store, slot)
        if old_item is not None:
            add_item(old_item, 1)

        ## 装备新物品
        remove_item(item_id, 1)
        setattr(store, slot, item_id)
        return True

    def unequip_slot(slot):
        """
        卸下指定槽位装备放回背包。
        slot: "weapon" / "armor" / "trinket"
        返回 True 成功, False 槽位为空或背包满。
        """
        attr_name = "equipped_" + slot
        current = getattr(store, attr_name, None)
        if current is None:
            return False

        ## 检查背包空间
        if _find_inv_index(current) < 0 and get_inventory_count() >= get_max_inventory_slots():
            return False

        add_item(current, 1)
        setattr(store, attr_name, None)
        return True

    def get_equipped(slot):
        """获取指定槽位的装备ID，None表示空"""
        return getattr(store, "equipped_" + slot, None)

    def get_equipment_bonuses():
        """
        计算所有已装备物品的属性加成总和。
        返回字典, 例如 {"damage": 10, "defense": 8, "crit": 5, ...}
        供 combat.rpy 调用。
        """
        bonuses = {}
        for slot in ["equipped_weapon", "equipped_armor", "equipped_trinket"]:
            item_id = getattr(store, slot, None)
            if item_id and item_id in items_database:
                stats = items_database[item_id]["stats"]
                for k, v in stats.items():
                    if isinstance(v, (int, float)):
                        bonuses[k] = bonuses.get(k, 0) + v
                    elif isinstance(v, bool) and v:
                        bonuses[k] = True
        return bonuses

    def use_consumable(item_id):
        """
        使用消耗品。返回效果描述文字，失败返回 None。
        """
        if not has_item(item_id):
            return None

        info = items_database.get(item_id)
        if not info or info["type"] != "consumable":
            return None

        stats = info["stats"]
        effects = []

        if "heal" in stats:
            effects.append("恢复了 %d 点生命" % stats["heal"])
        if "stamina_restore" in stats:
            effects.append("恢复了 %d 点耐力" % stats["stamina_restore"])
        if stats.get("cure_poison"):
            effects.append("解除了中毒状态")
        if stats.get("cure_bleed"):
            effects.append("止住了流血")
        if "buff_damage" in stats:
            effects.append("伤害提升 %d，持续 %d 回合" % (stats["buff_damage"], stats.get("buff_turns", 1)))
        if stats.get("guaranteed_flee"):
            effects.append("烟雾弥漫，可以安全撤退")

        remove_item(item_id, 1)

        if effects:
            return "使用了%s: %s。" % (info["name"], "，".join(effects))
        return "使用了%s。" % info["name"]

    def get_sell_price(item_id):
        """售出价格 = 买入价 * 60%"""
        info = items_database.get(item_id)
        if not info:
            return 0
        return int(info["price"] * 0.6)

    def buy_item(item_id):
        """
        购买物品。扣除金币并添加到背包。
        返回: "ok" / "no_gold" / "bag_full" / "invalid"
        """
        info = items_database.get(item_id)
        if not info:
            return "invalid"

        price = info["price"]
        if get_gold() < price:
            return "no_gold"

        ## 检查背包空间
        if _find_inv_index(item_id) < 0 and get_inventory_count() >= get_max_inventory_slots():
            return "bag_full"

        modify_gold(-price)
        add_item(item_id, 1)
        return "ok"

    def sell_item(item_id):
        """
        出售物品。从背包移除并获得金币。
        返回: "ok" / "no_item" / "invalid"
        """
        info = items_database.get(item_id)
        if not info:
            return "invalid"

        if not has_item(item_id):
            return "no_item"

        sell_price = get_sell_price(item_id)
        remove_item(item_id, 1)
        modify_gold(sell_price)
        return "ok"

    def get_item_icon(item_id):
        """获取物品显示图标字符"""
        info = items_database.get(item_id)
        if not info:
            return "？"
        if info["type"] == "weapon":
            return WEAPON_SUBTYPE_ICONS.get(info.get("subtype", ""), "剑")
        return ITEM_TYPE_ICONS.get(info["type"], "?")

    def get_rarity_color(item_id):
        """获取物品稀有度颜色"""
        info = items_database.get(item_id)
        if not info:
            return "#b8a878"
        return RARITY_CONFIG.get(info["rarity"], ("#b8a878", "普通"))[0]

    def get_rarity_label(item_id):
        """获取物品稀有度中文标签"""
        info = items_database.get(item_id)
        if not info:
            return "普通"
        return RARITY_CONFIG.get(info["rarity"], ("#b8a878", "普通"))[1]

    def init_starting_inventory():
        """初始化起始背包 (游戏开始时调用)"""
        store.inventory_items = []
        store.equipped_weapon = None
        store.equipped_armor = None
        store.equipped_trinket = None
        store.extra_gold = 0
        add_item("iron_sword", 1)
        add_item("leather_armor", 1)
        add_item("health_potion", 2)
        add_item("bandage", 2)

    def open_shop(shop_name, stock_list):
        """
        打开商店界面。
        shop_name: 商店名称 (字符串)
        stock_list: 商品ID列表, 例如 ["iron_sword", "leather_armor", ...]
        """
        store._shop_name = shop_name
        store._shop_stock = list(stock_list)
        store._inv_selected = None
        renpy.show_screen("shop_screen")

    def get_items_by_type(item_type):
        """获取背包中指定类型的所有物品"""
        result = []
        for item_id, qty in store.inventory_items:
            info = items_database.get(item_id)
            if info and info["type"] == item_type:
                result.append((item_id, qty))
        return result


################################################################################
## 4. 动画变换
################################################################################

transform inv_panel_show:
    on show:
        alpha 0.0 yoffset 20
        ease 0.3 alpha 1.0 yoffset 0
    on hide:
        ease 0.2 alpha 0.0 yoffset 20

transform inv_overlay_show:
    on show:
        alpha 0.0
        ease 0.2 alpha 1.0
    on hide:
        ease 0.15 alpha 0.0

transform inv_item_hover:
    on idle:
        linear 0.15 zoom 1.0
    on hover:
        linear 0.15 zoom 1.05


################################################################################
## 5. 样式定义
################################################################################

style inv_button is default:
    xpadding 10
    ypadding 6

style inv_button_text is default:
    font "msyh.ttf"
    size 14
    color "#e0d8c8"
    hover_color "#ffd866"

style inv_title_text is default:
    font "msyh.ttf"
    size 22
    color "#d4a942"
    bold True
    outlines [(2, "#000000cc", 0, 0)]

style inv_label_text is default:
    font "msyh.ttf"
    size 14
    color "#e0d8c8"

style inv_desc_text is default:
    font "msyh.ttf"
    size 13
    color "#8a7e60"

style inv_stat_text is default:
    font "msyh.ttf"
    size 13

style inv_section_text is default:
    font "msyh.ttf"
    size 16
    color "#d4a942"


################################################################################
## 6. 背包界面 (按 I 键打开)
################################################################################

screen inventory_screen():
    modal True
    zorder 150

    default _inv_selected = None

    ## 暗色遮罩 — 点击遮罩区域关闭
    button:
        background Solid("#000000bb")
        xfill True
        yfill True
        action Hide("inventory_screen")
        at inv_overlay_show
    key "K_ESCAPE" action Hide("inventory_screen")
    key "K_i" action Hide("inventory_screen")
    key "game_menu" action Hide("inventory_screen")

    frame at inv_panel_show:
        xalign 0.5
        yalign 0.5
        xpadding 0
        ypadding 0
        if renpy.variant("small"):
            xsize 1.0
            ysize 1.0
        else:
            xsize 820
            ysize 620
        background Solid("#0f0d1af5")

        vbox:
            spacing 0

            ## ═══ 标题栏 ═══
            frame:
                xfill True
                ysize 56
                background Solid("#1a1528")
                xpadding 24
                ypadding 0

                hbox:
                    yalign 0.5
                    xfill True

                    hbox:
                        spacing 8
                        text "*" size 20 color "#d4a942" yalign 0.5
                        text "背包" style "inv_title_text"
                        ## 容量
                        $ _inv_count = get_inventory_count()
                        $ _inv_max = get_max_inventory_slots()
                        text "([_inv_count]/[_inv_max])" size 14 color "#6a5e48" yalign 0.5

                    hbox:
                        xalign 1.0
                        yalign 0.5
                        spacing 16

                        ## 金币显示
                        hbox:
                            spacing 4
                            text "金" size 16 color "#ffd700" yalign 0.5
                            $ _gold = get_gold()
                            text "[_gold]" size 16 color "#ffd866" bold True font "msyh.ttf" yalign 0.5

                        textbutton "X":
                            text_size 20
                            text_color "#6a5e48"
                            text_hover_color "#d4a942"
                            action Hide("inventory_screen")

            add Solid("#d4a94230") xsize 1.0 ysize 2

            ## ═══ 主体内容 ═══
            hbox:
                spacing 0

                ## ─── 左侧: 装备栏 + 物品网格 ─── ##
                viewport:
                    xsize 520
                    ysize 558
                    mousewheel True
                    draggable True
                    scrollbars "vertical"

                    frame:
                        background None
                        xpadding 16
                        ypadding 12
                        xfill True

                        vbox:
                            spacing 8

                            ## ── 装备栏 ── ##
                            text "已装备" style "inv_section_text"
                            null height 2

                            hbox:
                                spacing 10
                                xalign 0.0

                                ## 武器槽
                                $ _eq_w = store.equipped_weapon
                                $ _eq_w_info = items_database.get(_eq_w, None) if _eq_w else None
                                $ _eq_w_color = get_rarity_color(_eq_w) if _eq_w else "#6a5e48"
                                button:
                                    xsize 150
                                    ysize 64
                                    action If(_eq_w, SetScreenVariable("_inv_selected", _eq_w), NullAction())
                                    if _eq_w:
                                        background Solid("#1a1528")
                                        hover_background Solid("#2a2338")
                                        frame:
                                            background None
                                            xpadding 8
                                            ypadding 6
                                            vbox:
                                                spacing 2
                                                hbox:
                                                    spacing 4
                                                    text get_item_icon(_eq_w) size 16 color _eq_w_color yalign 0.5
                                                    text _eq_w_info["name"] size 13 color _eq_w_color font "msyh.ttf" bold True
                                                text "武器" size 10 color "#6a5e48" font "msyh.ttf"
                                    else:
                                        background Solid("#0f0d1a80")
                                        hover_background Solid("#1a1528")
                                        frame:
                                            background None
                                            xpadding 8
                                            ypadding 6
                                            xfill True
                                            yfill True
                                            vbox:
                                                xalign 0.5
                                                yalign 0.5
                                                text "剑" size 20 color "#2a2338" xalign 0.5
                                                text "武器槽" size 11 color "#2a2338" font "msyh.ttf" xalign 0.5

                                ## 护甲槽
                                $ _eq_a = store.equipped_armor
                                $ _eq_a_info = items_database.get(_eq_a, None) if _eq_a else None
                                $ _eq_a_color = get_rarity_color(_eq_a) if _eq_a else "#6a5e48"
                                button:
                                    xsize 150
                                    ysize 64
                                    action If(_eq_a, SetScreenVariable("_inv_selected", _eq_a), NullAction())
                                    if _eq_a:
                                        background Solid("#1a1528")
                                        hover_background Solid("#2a2338")
                                        frame:
                                            background None
                                            xpadding 8
                                            ypadding 6
                                            vbox:
                                                spacing 2
                                                hbox:
                                                    spacing 4
                                                    text "甲" size 16 color _eq_a_color yalign 0.5
                                                    text _eq_a_info["name"] size 13 color _eq_a_color font "msyh.ttf" bold True
                                                text "护甲" size 10 color "#6a5e48" font "msyh.ttf"
                                    else:
                                        background Solid("#0f0d1a80")
                                        hover_background Solid("#1a1528")
                                        frame:
                                            background None
                                            xpadding 8
                                            ypadding 6
                                            xfill True
                                            yfill True
                                            vbox:
                                                xalign 0.5
                                                yalign 0.5
                                                text "甲" size 20 color "#2a2338" xalign 0.5
                                                text "护甲槽" size 11 color "#2a2338" font "msyh.ttf" xalign 0.5

                                ## 饰品槽
                                $ _eq_t = store.equipped_trinket
                                $ _eq_t_info = items_database.get(_eq_t, None) if _eq_t else None
                                $ _eq_t_color = get_rarity_color(_eq_t) if _eq_t else "#6a5e48"
                                button:
                                    xsize 150
                                    ysize 64
                                    action If(_eq_t, SetScreenVariable("_inv_selected", _eq_t), NullAction())
                                    if _eq_t:
                                        background Solid("#1a1528")
                                        hover_background Solid("#2a2338")
                                        frame:
                                            background None
                                            xpadding 8
                                            ypadding 6
                                            vbox:
                                                spacing 2
                                                hbox:
                                                    spacing 4
                                                    text "饰" size 16 color _eq_t_color yalign 0.5
                                                    text _eq_t_info["name"] size 13 color _eq_t_color font "msyh.ttf" bold True
                                                text "饰品" size 10 color "#6a5e48" font "msyh.ttf"
                                    else:
                                        background Solid("#0f0d1a80")
                                        hover_background Solid("#1a1528")
                                        frame:
                                            background None
                                            xpadding 8
                                            ypadding 6
                                            xfill True
                                            yfill True
                                            vbox:
                                                xalign 0.5
                                                yalign 0.5
                                                text "饰" size 20 color "#2a2338" xalign 0.5
                                                text "饰品槽" size 11 color "#2a2338" font "msyh.ttf" xalign 0.5

                            null height 6
                            add Solid("#d4a94220") xsize 1.0 ysize 1
                            null height 6

                            ## ── 物品列表 ── ##
                            text "物品" style "inv_section_text"
                            null height 4

                            if len(store.inventory_items) == 0:
                                null height 20
                                text "背包为空" size 14 color "#4a4030" font "msyh.ttf" xalign 0.5

                            ## 物品网格 (每行4个)
                            $ _items_list = list(store.inventory_items)
                            $ _grid_cols = 4
                            $ _total = len(_items_list)
                            $ _grid_rows = (_total + _grid_cols - 1) // _grid_cols if _total > 0 else 0
                            $ _grid_cells = _grid_cols * _grid_rows

                            if _total > 0:
                                grid _grid_cols _grid_rows:
                                    spacing 6
                                    xalign 0.0

                                    for _idx in range(_grid_cells):
                                        if _idx < _total:
                                            $ _item_id = _items_list[_idx][0]
                                            $ _item_qty = _items_list[_idx][1]
                                            $ _item_info = items_database.get(_item_id, {})
                                            $ _item_rcolor = get_rarity_color(_item_id)
                                            $ _is_selected = (_inv_selected == _item_id)

                                            button:
                                                xsize 112
                                                ysize 80
                                                action SetScreenVariable("_inv_selected", _item_id)
                                                if _is_selected:
                                                    background Solid("#d4a94230")
                                                else:
                                                    background Solid("#1a1528")
                                                hover_background Solid("#2a2338")

                                                frame:
                                                    background None
                                                    xpadding 6
                                                    ypadding 4
                                                    xfill True
                                                    yfill True

                                                    vbox:
                                                        spacing 1
                                                        ## 图标行
                                                        hbox:
                                                            xfill True
                                                            text get_item_icon(_item_id) size 18 color _item_rcolor
                                                            if _item_qty > 1:
                                                                text "x[_item_qty]" size 11 color "#8a7e60" xalign 1.0 yalign 0.5

                                                        ## 物品名
                                                        text _item_info.get("name", "?") size 11 color _item_rcolor font "msyh.ttf"

                                                        ## 稀有度标签
                                                        text get_rarity_label(_item_id) size 9 color _item_rcolor

                                                    ## 选中边框
                                                    if _is_selected:
                                                        add Solid(_item_rcolor + "40") xsize 2 ysize 1.0 xalign 0.0 yalign 0.0
                                                        add Solid(_item_rcolor + "40") xsize 2 ysize 1.0 xalign 1.0 yalign 0.0
                                        else:
                                            ## 填充空位
                                            null xsize 112 ysize 80

                ## ─── 右侧: 物品详情 ─── ##
                frame:
                    xsize 300
                    ysize 558
                    background Solid("#12101e")
                    xpadding 16
                    ypadding 16

                    if _inv_selected and _inv_selected in items_database:
                        $ _sel_info = items_database[_inv_selected]
                        $ _sel_rcolor = get_rarity_color(_inv_selected)
                        $ _sel_type = _sel_info["type"]

                        vbox:
                            spacing 8

                            ## 物品名称与图标
                            hbox:
                                spacing 8
                                frame:
                                    xsize 44
                                    ysize 44
                                    background Solid(_sel_rcolor + "25")
                                    text get_item_icon(_inv_selected) xalign 0.5 yalign 0.5 size 24 color _sel_rcolor

                                vbox:
                                    spacing 2
                                    text _sel_info["name"] size 18 color _sel_rcolor font "msyh.ttf" bold True
                                    hbox:
                                        spacing 8
                                        text get_rarity_label(_inv_selected) size 12 color _sel_rcolor
                                        if _sel_type == "weapon":
                                            text "武器" size 12 color "#6a5e48" font "msyh.ttf"
                                        elif _sel_type == "armor":
                                            text "护甲" size 12 color "#6a5e48" font "msyh.ttf"
                                        elif _sel_type == "trinket":
                                            text "饰品" size 12 color "#6a5e48" font "msyh.ttf"
                                        elif _sel_type == "consumable":
                                            text "消耗品" size 12 color "#6a5e48" font "msyh.ttf"
                                        elif _sel_type == "material":
                                            text "材料" size 12 color "#6a5e48" font "msyh.ttf"

                            add Solid("#d4a94220") xsize 1.0 ysize 1

                            ## 描述
                            text _sel_info["desc"] style "inv_desc_text"

                            ## 属性
                            if _sel_info["stats"]:
                                null height 2
                                text "属性：" size 13 color "#d4a942" font "msyh.ttf"
                                for _sk, _sv in _sel_info["stats"].items():
                                    $ _sname = STAT_DISPLAY_NAMES.get(_sk, _sk)
                                    if isinstance(_sv, bool):
                                        if _sv:
                                            text "  [_sname]" size 13 color "#2ecc71" font "msyh.ttf"
                                    elif isinstance(_sv, (int, float)):
                                        $ _scolor = "#2ecc71" if _sv > 0 else "#e74c3c"
                                        $ _ssign = "+" if _sv > 0 else ""
                                        text "  [_sname] [_ssign][_sv]" size 13 color _scolor font "msyh.ttf"

                            ## 价格
                            null height 4
                            hbox:
                                spacing 8
                                text "买入：" size 12 color "#6a5e48" font "msyh.ttf"
                                text "[_sel_info[\"price\"]]金" size 12 color "#ffd866" font "msyh.ttf"
                                text "卖出：" size 12 color "#6a5e48" font "msyh.ttf"
                                $ _sell_p = get_sell_price(_inv_selected)
                                text "[_sell_p]金" size 12 color "#ffd866" font "msyh.ttf"

                            ## 持有数量
                            $ _sel_qty = get_item_qty(_inv_selected)
                            if _sel_qty > 0:
                                text "持有： [_sel_qty]" size 12 color "#8a7e60" font "msyh.ttf"

                            null height 8
                            add Solid("#d4a94220") xsize 1.0 ysize 1
                            null height 8

                            ## ── 操作按钮 ── ##

                            ## 装备按钮 (武器/护甲/饰品)
                            if _sel_type in ("weapon", "armor", "trinket") and _sel_qty > 0:
                                ## 检查是否已装备此物品
                                $ _is_equipped = (_inv_selected == store.equipped_weapon or _inv_selected == store.equipped_armor or _inv_selected == store.equipped_trinket)
                                if not _is_equipped:
                                    ## 信仰需求检查
                                    if "faith_req" in _sel_info["stats"] and store.faith < _sel_info["stats"]["faith_req"]:
                                        textbutton "信仰不足，无法装备":
                                            xfill True
                                            text_size 14
                                            text_color "#e74c3c60"
                                            text_font "msyh.ttf"
                                            sensitive False
                                    else:
                                        textbutton "装备":
                                            xfill True
                                            xpadding 0
                                            ypadding 8
                                            text_size 14
                                            text_color "#e0d8c8"
                                            text_hover_color "#ffd866"
                                            text_font "msyh.ttf"
                                            text_xalign 0.5
                                            background Solid("#d4a94220")
                                            hover_background Solid("#d4a94240")
                                            action [Function(equip_item, _inv_selected), SetScreenVariable("_inv_selected", None)]
                                else:
                                    ## 卸下按钮
                                    textbutton "卸下":
                                        xfill True
                                        xpadding 0
                                        ypadding 8
                                        text_size 14
                                        text_color "#e0d8c8"
                                        text_hover_color "#ffd866"
                                        text_font "msyh.ttf"
                                        text_xalign 0.5
                                        background Solid("#d4a94220")
                                        hover_background Solid("#d4a94240")
                                        action [Function(unequip_slot, _sel_type), SetScreenVariable("_inv_selected", None)]

                            ## 使用按钮 (消耗品)
                            if _sel_type == "consumable" and _sel_qty > 0:
                                textbutton "使用":
                                    xfill True
                                    xpadding 0
                                    ypadding 8
                                    text_size 14
                                    text_color "#e0d8c8"
                                    text_hover_color "#2ecc71"
                                    text_font "msyh.ttf"
                                    text_xalign 0.5
                                    background Solid("#2ecc7120")
                                    hover_background Solid("#2ecc7140")
                                    action [Function(use_consumable, _inv_selected), SetScreenVariable("_inv_selected", None)]

                            ## 丢弃按钮
                            if _sel_qty > 0:
                                null height 4
                                textbutton "丢弃":
                                    xfill True
                                    xpadding 0
                                    ypadding 8
                                    text_size 14
                                    text_color "#6a5e48"
                                    text_hover_color "#e74c3c"
                                    text_font "msyh.ttf"
                                    text_xalign 0.5
                                    background Solid("#e74c3c10")
                                    hover_background Solid("#e74c3c25")
                                    action [Function(remove_item, _inv_selected, 1), SetScreenVariable("_inv_selected", None)]

                    else:
                        ## 未选中物品
                        vbox:
                            xalign 0.5
                            yalign 0.5
                            spacing 8
                            text "*" size 32 color "#1a1528" xalign 0.5
                            text "选择物品查看详情" size 14 color "#4a4030" font "msyh.ttf" xalign 0.5

            ## ═══ 底部装备加成汇总 ═══
            frame:
                xfill True
                ysize 4
                background Solid("#d4a94230")


################################################################################
## 7. 商店界面
################################################################################

screen shop_screen():
    ## 去掉 tag menu — 避免与Ren'Py内置游戏菜单冲突
    modal True
    zorder 150

    default _inv_selected = None

    ## 暗色遮罩 — 点击关闭
    button:
        background Solid("#000000cc")
        xfill True
        yfill True
        action [Hide("shop_screen"), Return()]
        at inv_overlay_show
    key "K_ESCAPE" action [Hide("shop_screen"), Return()]
    key "game_menu" action [Hide("shop_screen"), Return()]

    ## 商店提示变量
    default _shop_msg = ""
    default _shop_msg_color = "#8a7e60"
    default _shop_tab = "buy"

    frame at inv_panel_show:
        xalign 0.5
        yalign 0.5
        xpadding 0
        ypadding 0
        if renpy.variant("small"):
            xsize 1.0
            ysize 1.0
        else:
            xsize 880
            ysize 620
        background Solid("#0f0d1af5")

        vbox:
            spacing 0

            ## ═══ 标题栏 ═══
            frame:
                xfill True
                ysize 56
                background Solid("#1a1528")
                xpadding 24
                ypadding 0

                hbox:
                    yalign 0.5
                    xfill True

                    hbox:
                        spacing 8
                        text "*" size 20 color "#d4a942" yalign 0.5
                        text _shop_name style "inv_title_text"

                    hbox:
                        xalign 1.0
                        yalign 0.5
                        spacing 16

                        hbox:
                            spacing 4
                            text "金" size 16 color "#ffd700" yalign 0.5
                            $ _s_gold = get_gold()
                            text "[_s_gold]" size 16 color "#ffd866" bold True font "msyh.ttf" yalign 0.5

                        textbutton "X":
                            text_size 20
                            text_color "#6a5e48"
                            text_hover_color "#d4a942"
                            action [Hide("shop_screen"), Return()]

            add Solid("#d4a94230") xsize 1.0 ysize 2

            ## ═══ 标签切换 ═══
            frame:
                xfill True
                ysize 40
                background Solid("#12101e")
                xpadding 24
                ypadding 0

                hbox:
                    yalign 0.5
                    spacing 20

                    textbutton "购买":
                        text_size 15
                        text_font "msyh.ttf"
                        if _shop_tab == "buy":
                            text_color "#d4a942"
                            text_bold True
                        else:
                            text_color "#6a5e48"
                            text_hover_color "#ffd866"
                        action SetScreenVariable("_shop_tab", "buy")

                    textbutton "出售":
                        text_size 15
                        text_font "msyh.ttf"
                        if _shop_tab == "sell":
                            text_color "#d4a942"
                            text_bold True
                        else:
                            text_color "#6a5e48"
                            text_hover_color "#ffd866"
                        action SetScreenVariable("_shop_tab", "sell")

                    ## 提示信息
                    if _shop_msg:
                        text _shop_msg size 13 color _shop_msg_color font "msyh.ttf" xalign 1.0 yalign 0.5

            add Solid("#d4a94215") xsize 1.0 ysize 1

            ## ═══ 商品列表 ═══
            hbox:
                spacing 0

                ## ─── 左侧: 商品/背包列表 ─── ##
                viewport:
                    xsize 540
                    ysize 518
                    mousewheel True
                    draggable True
                    scrollbars "vertical"

                    frame:
                        background None
                        xpadding 16
                        ypadding 12
                        xfill True

                        vbox:
                            spacing 4

                            if _shop_tab == "buy":
                                ## ── 购买标签: 显示商店库存 ── ##
                                for _s_item_id in _shop_stock:
                                    if _s_item_id in items_database:
                                        $ _s_info = items_database[_s_item_id]
                                        $ _s_rcolor = get_rarity_color(_s_item_id)
                                        $ _s_price = _s_info["price"]
                                        $ _s_can_buy = (get_gold() >= _s_price)
                                        $ _s_is_sel = (_inv_selected == _s_item_id)

                                        button:
                                            xfill True
                                            ysize 56
                                            action SetScreenVariable("_inv_selected", _s_item_id)
                                            if _s_is_sel:
                                                background Solid("#d4a94220")
                                            else:
                                                background Solid("#1a152800")
                                            hover_background Solid("#1a1528")

                                            hbox:
                                                spacing 10
                                                yalign 0.5
                                                xfill True

                                                ## 图标
                                                frame:
                                                    xsize 36
                                                    ysize 36
                                                    background Solid(_s_rcolor + "20")
                                                    text get_item_icon(_s_item_id) xalign 0.5 yalign 0.5 size 18 color _s_rcolor

                                                ## 名称和类型
                                                vbox:
                                                    spacing 1
                                                    text _s_info["name"] size 14 color _s_rcolor font "msyh.ttf" bold True
                                                    hbox:
                                                        spacing 6
                                                        text get_rarity_label(_s_item_id) size 10 color _s_rcolor
                                                        ## 持有数量
                                                        $ _s_have = get_item_qty(_s_item_id)
                                                        if _s_have > 0:
                                                            text "持有：[_s_have]" size 10 color "#6a5e48" font "msyh.ttf"

                                                ## 价格和购买按钮
                                                hbox:
                                                    xalign 1.0
                                                    yalign 0.5
                                                    spacing 10

                                                    text "[_s_price]金" size 14 color ("#ffd866" if _s_can_buy else "#e74c3c60") font "msyh.ttf" yalign 0.5

                                                    if _s_can_buy:
                                                        textbutton "购买":
                                                            text_size 13
                                                            text_color "#e0d8c8"
                                                            text_hover_color "#2ecc71"
                                                            text_font "msyh.ttf"
                                                            yalign 0.5
                                                            action [Function(buy_item, _s_item_id), SetScreenVariable("_shop_msg", "购买成功!"), SetScreenVariable("_shop_msg_color", "#2ecc71")]
                                                    else:
                                                        text "金币不足" size 12 color "#e74c3c60" font "msyh.ttf" yalign 0.5

                            else:
                                ## ── 出售标签: 显示玩家背包 ── ##
                                if len(store.inventory_items) == 0:
                                    null height 40
                                    text "背包为空" size 14 color "#4a4030" font "msyh.ttf" xalign 0.5

                                for _s_item_id, _s_qty in store.inventory_items:
                                    if _s_item_id in items_database:
                                        $ _s_info = items_database[_s_item_id]
                                        $ _s_rcolor = get_rarity_color(_s_item_id)
                                        $ _s_sell_price = get_sell_price(_s_item_id)
                                        $ _s_is_sel = (_inv_selected == _s_item_id)

                                        button:
                                            xfill True
                                            ysize 56
                                            action SetScreenVariable("_inv_selected", _s_item_id)
                                            if _s_is_sel:
                                                background Solid("#d4a94220")
                                            else:
                                                background Solid("#1a152800")
                                            hover_background Solid("#1a1528")

                                            hbox:
                                                spacing 10
                                                yalign 0.5
                                                xfill True

                                                ## 图标
                                                frame:
                                                    xsize 36
                                                    ysize 36
                                                    background Solid(_s_rcolor + "20")
                                                    text get_item_icon(_s_item_id) xalign 0.5 yalign 0.5 size 18 color _s_rcolor

                                                ## 名称
                                                vbox:
                                                    spacing 1
                                                    hbox:
                                                        spacing 6
                                                        text _s_info["name"] size 14 color _s_rcolor font "msyh.ttf" bold True
                                                        if _s_qty > 1:
                                                            text "x[_s_qty]" size 12 color "#8a7e60" font "msyh.ttf" yalign 0.5
                                                    text get_rarity_label(_s_item_id) size 10 color _s_rcolor

                                                ## 售价和出售按钮
                                                hbox:
                                                    xalign 1.0
                                                    yalign 0.5
                                                    spacing 10

                                                    text "[_s_sell_price]金" size 14 color "#ffd866" font "msyh.ttf" yalign 0.5

                                                    textbutton "出售":
                                                        text_size 13
                                                        text_color "#e0d8c8"
                                                        text_hover_color "#ffd866"
                                                        text_font "msyh.ttf"
                                                        yalign 0.5
                                                        action [Function(sell_item, _s_item_id), SetScreenVariable("_shop_msg", "出售成功!"), SetScreenVariable("_shop_msg_color", "#ffd866")]

                ## ─── 右侧: 物品详情 ─── ##
                frame:
                    xsize 340
                    ysize 518
                    background Solid("#12101e")
                    xpadding 16
                    ypadding 16

                    if _inv_selected and _inv_selected in items_database:
                        $ _sel_info = items_database[_inv_selected]
                        $ _sel_rcolor = get_rarity_color(_inv_selected)

                        vbox:
                            spacing 8

                            ## 物品名
                            hbox:
                                spacing 8
                                frame:
                                    xsize 44
                                    ysize 44
                                    background Solid(_sel_rcolor + "25")
                                    text get_item_icon(_inv_selected) xalign 0.5 yalign 0.5 size 24 color _sel_rcolor

                                vbox:
                                    spacing 2
                                    text _sel_info["name"] size 18 color _sel_rcolor font "msyh.ttf" bold True
                                    text get_rarity_label(_inv_selected) size 12 color _sel_rcolor

                            add Solid("#d4a94220") xsize 1.0 ysize 1

                            ## 描述
                            text _sel_info["desc"] style "inv_desc_text"

                            ## 属性
                            if _sel_info["stats"]:
                                null height 2
                                text "属性：" size 13 color "#d4a942" font "msyh.ttf"
                                for _sk, _sv in _sel_info["stats"].items():
                                    $ _sname = STAT_DISPLAY_NAMES.get(_sk, _sk)
                                    if isinstance(_sv, bool):
                                        if _sv:
                                            text "  [_sname]" size 13 color "#2ecc71" font "msyh.ttf"
                                    elif isinstance(_sv, (int, float)):
                                        $ _scolor = "#2ecc71" if _sv > 0 else "#e74c3c"
                                        $ _ssign = "+" if _sv > 0 else ""
                                        text "  [_sname] [_ssign][_sv]" size 13 color _scolor font "msyh.ttf"

                    else:
                        vbox:
                            xalign 0.5
                            yalign 0.5
                            spacing 8
                            text "*" size 32 color "#1a1528" xalign 0.5
                            text "选择物品查看详情" size 14 color "#4a4030" font "msyh.ttf" xalign 0.5


################################################################################
## 8. 物品获取通知弹幕
################################################################################

screen item_notify(item_id, qty=1):
    zorder 200
    $ _n_info = items_database.get(item_id, {})
    $ _n_name = _n_info.get("name", "???")
    $ _n_rcolor = get_rarity_color(item_id)
    $ _n_icon = get_item_icon(item_id)

    frame:
        xalign 0.5
        ypos 80
        background Solid("#0f0d1aee")
        xpadding 20
        ypadding 10

        hbox:
            spacing 8
            yalign 0.5
            text _n_icon size 18 color _n_rcolor yalign 0.5
            text "获得" size 14 color "#e0d8c8" font "msyh.ttf" yalign 0.5
            text "[_n_name]" size 16 color _n_rcolor font "msyh.ttf" bold True yalign 0.5
            if qty > 1:
                text "x[qty]" size 14 color "#8a7e60" font "msyh.ttf" yalign 0.5

    timer 2.5 action Hide("item_notify")


################################################################################
## 9. 装备加成汇总界面 (嵌入到 stats_screen 或独立查看)
################################################################################

screen equipment_summary():
    ## 显示当前装备的所有属性加成
    $ _bonuses = get_equipment_bonuses()

    frame:
        background Solid("#12101e")
        xpadding 16
        ypadding 12

        vbox:
            spacing 4
            text "装备加成" size 14 color "#d4a942" font "msyh.ttf"

            if _bonuses:
                for _bk, _bv in _bonuses.items():
                    $ _bname = STAT_DISPLAY_NAMES.get(_bk, _bk)
                    if isinstance(_bv, bool):
                        if _bv:
                            text "  [_bname]" size 12 color "#2ecc71" font "msyh.ttf"
                    elif isinstance(_bv, (int, float)):
                        $ _bcolor = "#2ecc71" if _bv > 0 else "#e74c3c"
                        $ _bsign = "+" if _bv > 0 else ""
                        text "  [_bname] [_bsign][_bv]" size 12 color _bcolor font "msyh.ttf"
            else:
                text "  无" size 12 color "#4a4030" font "msyh.ttf"


################################################################################
## 10. 快捷键绑定
################################################################################

init python:

    def _toggle_inventory():
        """I 键打开/关闭背包"""
        if renpy.get_screen("inventory_screen"):
            renpy.hide_screen("inventory_screen")
        else:
            store._inv_selected = None
            renpy.show_screen("inventory_screen")
        renpy.restart_interaction()

    # config.underlay.append(renpy.Keymap(K_i=_toggle_inventory))  # 已移除：背包UI入口暂不开放


################################################################################
## 11. 辅助 label (供剧情脚本调用)
################################################################################

## 给予物品 (带通知动画)
## 调用: call give_item("iron_sword", 1)
label give_item(item_id, qty=1):
    $ _give_ok = add_item(item_id, qty)
    if _give_ok:
        show screen item_notify(item_id, qty)
        pause 1.0
    else:
        "背包已满，无法获得新物品。"
    return

## 打开商店
## 调用: call open_market("集市", ["iron_sword", "leather_armor", ...])
label open_market(name, stock):
    $ store._shop_name = name
    $ store._shop_stock = list(stock)
    $ store._inv_selected = None
    call screen shop_screen
    return

## 初始化背包 (游戏开始时调用)
## 在 script.rpy 的 label start 中: call init_inventory
label init_inventory:
    $ init_starting_inventory()
    return

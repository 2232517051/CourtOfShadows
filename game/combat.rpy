## ============================================================
## 战斗系统 — 回合制战斗 (Heads Will Roll 风格)
## combat.rpy
## 用法: $ start_combat("bandit") 或 call combat_start("bandit")
## ============================================================


################################################################################
## 1. 战斗变量 (default)
################################################################################

## 当前战斗状态
default combat_active = False
default combat_enemy_id = "bandit"
default combat_turn = 0
default combat_phase = "player"  ## "player", "enemy", "victory", "defeat"

## 玩家战斗属性
default combat_player_hp = 100
default combat_player_max_hp = 100
default combat_player_stamina = 100
default combat_player_max_stamina = 100
default combat_player_attack = 0
default combat_player_defense = 0
default combat_player_dodge = 0
default combat_player_crit = 0

## 敌人战斗属性
default combat_enemy_name = ""
default combat_enemy_hp = 100
default combat_enemy_max_hp = 100
default combat_enemy_stamina = 100
default combat_enemy_attack = 0
default combat_enemy_defense = 0
default combat_enemy_dodge = 0
default combat_enemy_crit = 0
default combat_enemy_desc = ""
default combat_enemy_difficulty = ""

## 战斗效果/状态
default combat_dodge_bonus = 0          ## 闪避姿态加成
default combat_defend_active = False    ## 防御状态
default combat_enemy_dodge_bonus = 0
default combat_enemy_defend_active = False

## 战斗增益
default combat_buff_damage = 0
default combat_buff_turns = 0
default combat_guaranteed_flee = False

## 战斗日志
default combat_log = []
default combat_result = ""              ## "victory" / "defeat" / "retreat"

## 身体部位选择
default combat_targeting = False
default combat_attack_type = ""         ## "slash" / "heavy"

## 受伤系统 (章节内持续)
default injury_head = 0     ## 头部创伤剩余章节数
default injury_body = 0     ## 躯干重伤剩余章节数
default injury_limb = 0     ## 肢体受伤剩余章节数

## 战斗奖励
default combat_reward_power = 0
default combat_reward_wealth = 0
default combat_reward_reputation = 0
default combat_reward_text = ""

## ── 姿态系统 (HWR风格 OFF/DEF) ──
default combat_stance = "balanced"       ## "offensive" / "defensive" / "balanced"

## ── 流血状态 ──
default combat_player_bleed_turns = 0    ## 玩家流血剩余回合
default combat_player_bleed_dmg = 0      ## 每回合流血伤害
default combat_enemy_bleed_turns = 0     ## 敌人流血剩余回合
default combat_enemy_bleed_dmg = 0       ## 每回合流血伤害

## ── 眩晕 ──
default combat_player_stunned = False    ## 玩家下回合被眩晕
default combat_enemy_stunned = False     ## 敌人下回合被眩晕

## ── 连击/恢复 ──
default combat_combo_count = 0           ## 连续命中次数
default combat_respite_stacks = 0        ## 恢复能量（命中累积，可消耗恢复体力）

## 动画控制
default combat_hit_flash = False
default combat_enemy_hit_flash = False
default combat_show_damage = False
default combat_damage_text = ""
default combat_damage_pos = "enemy"     ## "enemy" / "player"


################################################################################
## 2. 敌人数据库
################################################################################

init python:

    ENEMY_DATABASE = {

        ## ── 简单 ──
        ## ── 简单 ──
        "bandit": {
            "name": "流寇",
            "desc": "游荡在艾登堡外的亡命之徒",
            "difficulty": "简单",
            "hp": 60,
            "attack": 12,
            "defense": 4,
            "dodge": 8,
            "crit": 5,
            "stamina": 80,
            "ai": "aggressive",
            "has_shield": False,
            "armor_coverage": {"head": 0, "neck": 0, "body": 20, "limbs": 0},
            "loot_power": (3, 5),
            "loot_wealth": (2, 4),
            "loot_reputation": (1, 2),
            "loot_desc": "你从流寇身上搜到了一些铜币和一把生锈的匕首。",
        },
        "bandit_leader": {
            "name": "流寇头目",
            "desc": "统领一群盗匪的悍将",
            "difficulty": "简单",
            "hp": 80,
            "attack": 16,
            "defense": 6,
            "dodge": 10,
            "crit": 8,
            "stamina": 90,
            "ai": "aggressive",
            "has_shield": True,
            "armor_coverage": {"head": 10, "neck": 0, "body": 30, "limbs": 10},
            "loot_power": (4, 6),
            "loot_wealth": (3, 6),
            "loot_reputation": (2, 3),
            "loot_desc": "头目的藏匿处有不少值钱的赃物。",
        },

        ## ── 中等 ──
        "baron_soldier": {
            "name": "男爵士兵",
            "desc": "冯·哈根男爵的正规军，训练有素",
            "difficulty": "中等",
            "hp": 90,
            "attack": 18,
            "defense": 10,
            "dodge": 6,
            "crit": 5,
            "stamina": 100,
            "ai": "balanced",
            "has_shield": True,
            "armor_coverage": {"head": 30, "neck": 10, "body": 60, "limbs": 30},
            "loot_power": (4, 6),
            "loot_wealth": (2, 4),
            "loot_reputation": (2, 3),
            "loot_desc": "士兵的制式装备质量不错。",
        },
        "mercenary": {
            "name": "佣兵",
            "desc": "为金币而战的雇佣兵，经验丰富",
            "difficulty": "中等",
            "hp": 85,
            "attack": 20,
            "defense": 8,
            "dodge": 12,
            "crit": 10,
            "stamina": 90,
            "ai": "aggressive",
            "has_shield": False,
            "armor_coverage": {"head": 20, "neck": 5, "body": 40, "limbs": 15},
            "loot_power": (3, 6),
            "loot_wealth": (4, 7),
            "loot_reputation": (1, 3),
            "loot_desc": "佣兵的钱袋里有不少金币。",
        },

        ## ── 困难 ──
        "dark_lily_assassin": {
            "name": "暗百合刺客",
            "desc": "暗百合组织训练的精英杀手",
            "difficulty": "困难",
            "hp": 75,
            "attack": 24,
            "defense": 6,
            "dodge": 22,
            "crit": 20,
            "stamina": 100,
            "ai": "aggressive",
            "has_shield": False,
            "armor_coverage": {"head": 10, "neck": 0, "body": 25, "limbs": 10},
            "loot_power": (5, 8),
            "loot_wealth": (3, 5),
            "loot_reputation": (2, 4),
            "loot_desc": "刺客身上的暗器精巧而致命。",
        },
        "church_knight": {
            "name": "教会骑士",
            "desc": "以圣光之名挥剑的虔诚战士",
            "difficulty": "困难",
            "hp": 110,
            "attack": 20,
            "defense": 16,
            "dodge": 5,
            "crit": 8,
            "stamina": 100,
            "ai": "defensive",
            "has_shield": True,
            "armor_coverage": {"head": 50, "neck": 20, "body": 80, "limbs": 40},
            "loot_power": (5, 7),
            "loot_wealth": (2, 4),
            "loot_reputation": (3, 5),
            "loot_desc": "教会骑士的盔甲和圣徽价值不菲。",
        },
        "baron_elite": {
            "name": "男爵精锐",
            "desc": "男爵麾下最精锐的卫队成员",
            "difficulty": "困难",
            "hp": 100,
            "attack": 22,
            "defense": 14,
            "dodge": 8,
            "crit": 10,
            "stamina": 100,
            "ai": "balanced",
            "has_shield": True,
            "armor_coverage": {"head": 40, "neck": 15, "body": 70, "limbs": 35},
            "loot_power": (5, 8),
            "loot_wealth": (3, 6),
            "loot_reputation": (2, 4),
            "loot_desc": "精锐的装备是一笔可观的战利品。",
        },

        ## ── 极难 ──
        "royal_guard": {
            "name": "王室禁卫",
            "desc": "守护王室血脉的不朽之盾",
            "difficulty": "极难",
            "hp": 130,
            "attack": 24,
            "defense": 18,
            "dodge": 10,
            "crit": 12,
            "stamina": 100,
            "ai": "defensive",
            "has_shield": True,
            "armor_coverage": {"head": 60, "neck": 30, "body": 90, "limbs": 50},
            "loot_power": (6, 8),
            "loot_wealth": (4, 6),
            "loot_reputation": (3, 5),
            "loot_desc": "禁卫军的佩剑上刻着王室纹章。",
        },

        ## ── BOSS ──
        "baron_boss": {
            "name": "冯·哈根男爵",
            "desc": "野心勃勃的男爵亲自出马，身经百战",
            "difficulty": "首领",
            "hp": 150,
            "attack": 26,
            "defense": 16,
            "dodge": 10,
            "crit": 12,
            "stamina": 100,
            "ai": "balanced",
            "has_shield": True,
            "armor_coverage": {"head": 50, "neck": 25, "body": 85, "limbs": 45},
            "loot_power": (8, 12),
            "loot_wealth": (6, 10),
            "loot_reputation": (5, 8),
            "loot_desc": "击败男爵后，你缴获了他的家传宝剑和男爵领的财务记录。",
        },
        "lily_leader": {
            "name": "暗百合首领",
            "desc": "隐藏在暗影中的暗百合组织领袖",
            "difficulty": "首领",
            "hp": 120,
            "attack": 28,
            "defense": 10,
            "dodge": 20,
            "crit": 22,
            "stamina": 100,
            "ai": "aggressive",
            "has_shield": False,
            "armor_coverage": {"head": 20, "neck": 5, "body": 35, "limbs": 15},
            "loot_power": (7, 10),
            "loot_wealth": (5, 8),
            "loot_reputation": (4, 7),
            "loot_desc": "暗百合首领的密信中包含了大量情报。",
        },
        "duel_champion": {
            "name": "决斗冠军",
            "desc": "王国决斗场上不败的传奇剑士",
            "difficulty": "首领",
            "hp": 140,
            "attack": 30,
            "defense": 12,
            "dodge": 15,
            "crit": 18,
            "stamina": 100,
            "ai": "aggressive",
            "has_shield": False,
            "armor_coverage": {"head": 35, "neck": 15, "body": 55, "limbs": 30},
            "loot_power": (8, 12),
            "loot_wealth": (5, 8),
            "loot_reputation": (6, 10),
            "loot_desc": "你击败了决斗冠军！这一壮举将传遍整个王国。",
        },
    }

    ## 难度颜色
    DIFFICULTY_COLORS = {
        "简单": "#2ecc71",
        "中等": "#f39c12",
        "困难": "#e74c3c",
        "极难": "#9b59b6",
        "首领": "#d4a942",
    }


################################################################################
## 3. 战斗核心函数
################################################################################

init python:
    import random as _combat_random

    ## ──────────────── 装备接口（从 inventory.rpy 获取） ────────────────
    def get_weapon_bonus():
        """武器攻击力加成"""
        try:
            bonuses = get_equipment_bonuses()
            return bonuses.get("damage", 0)
        except Exception:
            return 0

    def get_armor_bonus():
        """护甲防御力加成"""
        try:
            bonuses = get_equipment_bonuses()
            return bonuses.get("defense", 0)
        except Exception:
            return 0

    def get_accessory_bonus():
        """饰品特殊加成"""
        try:
            bonuses = get_equipment_bonuses()
            return bonuses.get("crit", 0)
        except Exception:
            return 0

    def get_combat_items():
        """获取背包中可用的战斗消耗品
        返回: [(item_id, name, desc, effect_type, effect_value), ...]
        """
        result = []
        try:
            combat_consumables = {
                "health_potion": ("治疗药水", "恢复 30 HP", "heal", 30),
                "stamina_potion": ("耐力药水", "恢复 40 体力", "stamina", 40),
                "bandage": ("绷带", "恢复 15 HP 并止血", "heal", 15),
                "antidote": ("解毒药", "解除毒素", "cure", 0),
                "war_paint": ("战争涂料", "3回合伤害+10", "buff_damage", 10),
                "smoke_bomb": ("烟雾弹", "确保撤退成功", "guaranteed_flee", 0),
                "potent_medicine": ("强效药剂", "恢复 50 HP", "heal", 50),
            }
            for item_id, (name, desc, etype, eval) in combat_consumables.items():
                if has_item(item_id):
                    result.append((item_id, name, desc, etype, eval))
        except Exception:
            pass
        return result

    ## ──────────────── 疲劳系统 ────────────────

    def get_fatigue_level(stamina):
        """根据体力值返回疲劳等级 (1-5)"""
        if stamina >= 80:
            return 1
        elif stamina >= 60:
            return 2
        elif stamina >= 40:
            return 3
        elif stamina >= 20:
            return 4
        else:
            return 5

    def get_fatigue_name(level):
        """疲劳等级中文名"""
        names = {1: "精力充沛", 2: "略感疲惫", 3: "疲劳", 4: "极度疲劳", 5: "力竭"}
        return names.get(level, "未知")

    def get_fatigue_color(level):
        """疲劳等级颜色"""
        colors = {1: "#2ecc71", 2: "#a8d86a", 3: "#f39c12", 4: "#e67e22", 5: "#e74c3c"}
        return colors.get(level, "#e0d8c8")

    def get_fatigue_penalties(stamina):
        """返回 (hit_penalty, dodge_penalty, damage_mult)"""
        level = get_fatigue_level(stamina)
        if level == 1:
            return (0, 0, 1.0)
        elif level == 2:
            return (5, 0, 1.0)
        elif level == 3:
            return (10, 5, 1.0)
        elif level == 4:
            return (20, 15, 1.0)
        else:
            return (30, 25, 0.8)

    ## ──────────────── 伤害计算 ────────────────

    def get_injury_penalties():
        """获取当前受伤对属性的影响"""
        penalties = {"intrigue": 0, "power": 0, "loyalty": 0, "dodge": 0}
        if store.injury_head > 0:
            penalties["intrigue"] = -10
        if store.injury_body > 0:
            penalties["power"] = -5
            penalties["loyalty"] = -5
        if store.injury_limb > 0:
            penalties["dodge"] = -10
        return penalties

    def calc_player_combat_stats():
        """根据当前属性计算玩家战斗数值"""
        penalties = get_injury_penalties()
        p = max(0, store.power + penalties.get("power", 0))
        i = max(0, store.intrigue + penalties.get("intrigue", 0))
        f = store.faith
        r = store.reputation

        atk = int(p * 0.6 + i * 0.2) + get_weapon_bonus()
        dfn = int(p * 0.3 + f * 0.2) + get_armor_bonus()
        dodge = int(i * 0.4 + r * 0.1) + penalties.get("dodge", 0)
        crit = int(i * 0.3)
        max_hp = int(100 + p * 0.5)

        return {
            "attack": max(1, atk),
            "defense": max(0, dfn),
            "dodge": max(0, min(80, dodge)),
            "crit": max(0, min(60, crit)),
            "max_hp": max(50, max_hp),
        }

    ## ──────────────── 初始化战斗 ────────────────

    def init_combat(enemy_id):
        """初始化战斗数据"""
        enemy = ENEMY_DATABASE.get(enemy_id)
        if not enemy:
            return False

        ## 玩家属性计算
        stats = calc_player_combat_stats()
        store.combat_player_attack = stats["attack"]
        store.combat_player_defense = stats["defense"]
        store.combat_player_dodge = stats["dodge"]
        store.combat_player_crit = stats["crit"]
        store.combat_player_max_hp = stats["max_hp"]
        store.combat_player_hp = stats["max_hp"]
        store.combat_player_stamina = 100
        store.combat_player_max_stamina = 100

        ## 敌人数据
        store.combat_enemy_id = enemy_id
        store.combat_enemy_name = enemy["name"]
        store.combat_enemy_desc = enemy["desc"]
        store.combat_enemy_difficulty = enemy["difficulty"]
        store.combat_enemy_max_hp = enemy["hp"]
        store.combat_enemy_hp = enemy["hp"]
        store.combat_enemy_attack = enemy["attack"]
        store.combat_enemy_defense = enemy["defense"]
        store.combat_enemy_dodge = enemy["dodge"]
        store.combat_enemy_crit = enemy["crit"]
        store.combat_enemy_stamina = enemy.get("stamina", 100)

        ## 状态重置
        store.combat_active = True
        store.combat_turn = 1
        store.combat_phase = "player"
        store.combat_log = []
        store.combat_result = ""
        store.combat_dodge_bonus = 0
        store.combat_defend_active = False
        store.combat_enemy_dodge_bonus = 0
        store.combat_enemy_defend_active = False
        store.combat_targeting = False
        store.combat_attack_type = ""
        store.combat_hit_flash = False
        store.combat_enemy_hit_flash = False
        store.combat_show_damage = False
        store.combat_damage_text = ""

        ## 新系统重置
        store.combat_stance = "balanced"
        store.combat_player_bleed_turns = 0
        store.combat_player_bleed_dmg = 0
        store.combat_enemy_bleed_turns = 0
        store.combat_enemy_bleed_dmg = 0
        store.combat_player_stunned = False
        store.combat_enemy_stunned = False
        store.combat_combo_count = 0
        store.combat_respite_stacks = 0

        ## 初始化奖励
        store.combat_reward_power = 0
        store.combat_reward_wealth = 0
        store.combat_reward_reputation = 0
        store.combat_reward_text = ""

        add_combat_log("—— 战斗开始 ——")
        add_combat_log("你面对的是: %s" % enemy["name"])

        return True

    ## ──────────────── 战斗日志 ────────────────

    def add_combat_log(msg):
        """添加战斗日志，保留最近6条"""
        store.combat_log.append(msg)
        if len(store.combat_log) > 6:
            store.combat_log = store.combat_log[-6:]

    ## ──────────────── 命中判定 ────────────────

    def roll_hit(base_accuracy, target_dodge, fatigue_hit_penalty, fatigue_dodge_penalty):
        """判定是否命中
        返回: (hit, is_crit, actual_accuracy)
        """
        accuracy = max(5, base_accuracy - fatigue_hit_penalty)
        effective_dodge = max(0, target_dodge - fatigue_dodge_penalty)
        hit_chance = max(10, min(95, accuracy - effective_dodge))
        roll = _combat_random.randint(1, 100)
        return (roll <= hit_chance, False, hit_chance)

    def roll_crit(crit_chance):
        """判定是否暴击"""
        return _combat_random.randint(1, 100) <= max(0, min(60, crit_chance))

    ## ──────────────── 身体部位修正 ────────────────

    def get_body_part_mod(part):
        """返回 (damage_mult, accuracy_mod, injury_type)"""
        if part == "head":
            return (1.5, -15, "head")
        elif part == "neck":
            return (2.0, -25, "neck")
        elif part == "body":
            return (1.0, 0, "body")
        elif part == "limbs":
            return (0.75, 10, "limbs")
        return (1.0, 0, "body")

    def get_body_part_name(part):
        names = {"head": "头部", "neck": "颈部", "body": "躯干", "limbs": "四肢"}
        return names.get(part, "躯干")

    ## ──────────────── 姿态系统 ────────────────

    def get_stance_mods():
        """返回当前姿态的修正值 (dmg_mult, dodge_mod, stamina_cost_mod, stamina_regen)"""
        stance = store.combat_stance
        if stance == "offensive":
            return (1.20, -10, 5, 0)       ## +20%伤害, -10闪避, +5体力消耗, 无回合回复
        elif stance == "defensive":
            return (0.80, 15, -5, 8)        ## -20%伤害, +15闪避, -5体力消耗, 每回合+8体力
        else:  ## balanced
            return (1.0, 0, 0, 3)           ## 标准, 每回合+3体力

    def get_stance_name():
        names = {"offensive": "攻势", "defensive": "守势", "balanced": "均衡"}
        return names.get(store.combat_stance, "均衡")

    def get_stance_color():
        colors = {"offensive": "#e74c3c", "defensive": "#3498db", "balanced": "#d4a942"}
        return colors.get(store.combat_stance, "#d4a942")

    ## ──────────────── 流血系统 ────────────────

    def apply_bleed_tick():
        """回合开始时处理流血伤害"""
        if store.combat_player_bleed_turns > 0:
            store.combat_player_hp = max(0, store.combat_player_hp - store.combat_player_bleed_dmg)
            store.combat_player_bleed_turns -= 1
            add_combat_log("你正在流血！失去 %d HP（剩余%d回合）" % (store.combat_player_bleed_dmg, store.combat_player_bleed_turns))
        if store.combat_enemy_bleed_turns > 0:
            store.combat_enemy_hp = max(0, store.combat_enemy_hp - store.combat_enemy_bleed_dmg)
            store.combat_enemy_bleed_turns -= 1
            add_combat_log("%s 正在流血！失去 %d HP" % (store.combat_enemy_name, store.combat_enemy_bleed_dmg))

    def inflict_bleed(target, dmg, turns):
        """给目标施加流血 target=「player」/「enemy」"""
        if target == "player":
            store.combat_player_bleed_dmg = dmg
            store.combat_player_bleed_turns = turns
        else:
            store.combat_enemy_bleed_dmg = dmg
            store.combat_enemy_bleed_turns = turns

    ## ──────────────── 护甲覆盖 ────────────────

    def check_armor_coverage(enemy_id, body_part):
        """检查护甲是否激活（按部位覆盖率），返回True=护甲生效"""
        enemy = ENEMY_DATABASE.get(enemy_id, {})
        coverage = enemy.get("armor_coverage", {})
        cover_pct = coverage.get(body_part, 0)
        return _combat_random.randint(1, 100) <= cover_pct

    ## ──────────────── 恢复机制 (Respite) ────────────────

    def gain_respite(amount):
        """获得恢复能量（命中/击杀时触发）"""
        store.combat_respite_stacks = min(9, store.combat_respite_stacks + amount)

    def use_respite():
        """消耗恢复能量恢复体力（自动在每回合开始触发）"""
        if store.combat_respite_stacks >= 3:
            recover = store.combat_respite_stacks * 3
            store.combat_player_stamina = min(store.combat_player_max_stamina, store.combat_player_stamina + recover)
            add_combat_log("恢复能量释放！+%d 体力" % recover)
            store.combat_respite_stacks = 0

    ## ──────────────── 玩家攻击 ────────────────

    def player_attack(attack_type, body_part):
        """
        执行玩家攻击
        attack_type: "slash" / "heavy"
        body_part: "head" / "body" / "limbs" / "neck"
        """
        ## 姿态修正
        stance_dmg, stance_dodge, stance_stamina, _ = get_stance_mods()

        ## 消耗体力（姿态影响）
        stamina_cost = 10 if attack_type == "slash" else 20
        stamina_cost = max(5, stamina_cost + stance_stamina)
        store.combat_player_stamina = max(0, store.combat_player_stamina - stamina_cost)

        ## 清除上回合防御/闪避状态
        store.combat_defend_active = False

        ## 疲劳惩罚
        hit_pen, dodge_pen, dmg_mult = get_fatigue_penalties(store.combat_player_stamina)

        ## 攻击名称
        atk_name = "斩击" if attack_type == "slash" else "猛击"
        part_name = get_body_part_name(body_part)

        ## 身体部位修正
        part_dmg_mult, part_acc_mod, injury_type = get_body_part_mod(body_part)

        ## 基础命中率
        base_accuracy = 85 if attack_type == "slash" else 70
        base_accuracy += part_acc_mod

        ## 敌人闪避（含闪避姿态加成）——被眩晕时闪避为0
        if store.combat_enemy_stunned:
            enemy_dodge = 0
        else:
            enemy_dodge = store.combat_enemy_dodge + store.combat_enemy_dodge_bonus

        ## 命中判定
        hit_chance = max(10, min(95, base_accuracy - hit_pen - enemy_dodge))
        roll = _combat_random.randint(1, 100)
        hit = roll <= hit_chance

        if not hit:
            add_combat_log("你对%s使用%s —— 未命中！(%d%%)" % (part_name, atk_name, hit_chance))
            store.combat_enemy_dodge_bonus = 0
            store.combat_combo_count = 0  ## 连击中断
            return False

        ## 伤害计算（含姿态加成）
        base_dmg = store.combat_player_attack
        if attack_type == "heavy":
            base_dmg = int(base_dmg * 1.5)
        base_dmg = int(base_dmg * part_dmg_mult * dmg_mult * stance_dmg)

        ## 暴击
        is_crit = roll_crit(store.combat_player_crit)
        if is_crit:
            base_dmg = int(base_dmg * 1.8)

        ## 护甲覆盖检查——护甲激活则额外减伤
        armor_blocked = check_armor_coverage(store.combat_enemy_id, body_part)

        ## 敌人防御
        reduction = store.combat_enemy_defense
        if store.combat_enemy_defend_active:
            reduction = int(reduction * 2)
        if armor_blocked:
            reduction = int(reduction * 1.5)  ## 护甲激活，防御力×1.5

        final_dmg = max(1, base_dmg - reduction)

        ## 随机浮动 +-15%
        variance = _combat_random.randint(-15, 15)
        final_dmg = max(1, int(final_dmg * (100 + variance) / 100))

        ## 造成伤害
        store.combat_enemy_hp = max(0, store.combat_enemy_hp - final_dmg)

        ## ── 恢复机制 (Respite) ──
        store.combat_combo_count += 1
        gain_respite(2)  ## 每次命中+2恢复能量

        ## ── 流血判定：颈部攻击30%概率，头部猛击15%概率 ──
        bleed_chance = 0
        if body_part == "neck":
            bleed_chance = 30
        elif body_part == "head" and attack_type == "heavy":
            bleed_chance = 15
        elif is_crit:
            bleed_chance = 10

        if bleed_chance > 0 and _combat_random.randint(1, 100) <= bleed_chance:
            bleed_dmg = max(2, final_dmg // 4)
            inflict_bleed("enemy", bleed_dmg, 3)
            add_combat_log("造成流血！每回合 %d 伤害，持续3回合" % bleed_dmg)

        ## ── 眩晕判定：头部猛击20%概率 ──
        if body_part == "head" and attack_type == "heavy" and not store.combat_enemy_stunned:
            if _combat_random.randint(1, 100) <= 20:
                store.combat_enemy_stunned = True
                add_combat_log("%s 被击晕了！下回合无法行动！" % store.combat_enemy_name)

        ## 动画标记
        store.combat_enemy_hit_flash = True
        store.combat_show_damage = True
        store.combat_damage_text = str(final_dmg)
        store.combat_damage_pos = "enemy"

        ## 日志
        crit_text = "【暴击！】" if is_crit else ""
        armor_text = "(护甲减免)" if armor_blocked else ""
        defend_text = "(防御中)" if store.combat_enemy_defend_active else ""
        add_combat_log("你%s攻击%s%s —— %d伤害 %s%s" % (atk_name, part_name, crit_text, final_dmg, armor_text, defend_text))

        ## 清除敌人防御/闪避状态
        store.combat_enemy_dodge_bonus = 0
        store.combat_enemy_defend_active = False

        return True

    ## ──────────────── 盾击 ────────────────

    def player_shield_bash():
        """盾击：消耗15体力，造成轻伤害，削减敌人体力，概率眩晕"""
        store.combat_player_stamina = max(0, store.combat_player_stamina - 15)
        store.combat_defend_active = False

        ## 轻微伤害（攻击力的30%）
        bash_dmg = max(1, int(store.combat_player_attack * 0.3))
        store.combat_enemy_hp = max(0, store.combat_enemy_hp - bash_dmg)

        ## 削减敌人体力
        stamina_drain = _combat_random.randint(10, 20)
        store.combat_enemy_stamina = max(0, store.combat_enemy_stamina - stamina_drain)

        ## 眩晕判定 (30%)
        stunned = _combat_random.randint(1, 100) <= 30
        if stunned:
            store.combat_enemy_stunned = True

        ## 动画
        store.combat_enemy_hit_flash = True
        store.combat_show_damage = True
        store.combat_damage_text = str(bash_dmg)
        store.combat_damage_pos = "enemy"

        ## 日志
        stun_text = "眩晕！" if stunned else ""
        add_combat_log("盾击！造成%d伤害，削减%d体力 %s" % (bash_dmg, stamina_drain, stun_text))

        ## 恢复能量
        gain_respite(1)

        store.combat_enemy_dodge_bonus = 0

    ## ──────────────── 玩家防御 ────────────────

    def player_defend():
        """玩家选择防御（守势下额外恢复）"""
        store.combat_defend_active = True
        recover = 15
        if store.combat_stance == "defensive":
            recover = 22  ## 守势防御恢复更多
        store.combat_player_stamina = min(store.combat_player_max_stamina, store.combat_player_stamina + recover)
        add_combat_log("你举盾防御，恢复 %d 体力（伤害减半）" % recover)

    ## ──────────────── 玩家闪避姿态 ────────────────

    def player_dodge_stance():
        """玩家进入闪避姿态"""
        store.combat_player_stamina = max(0, store.combat_player_stamina - 5)
        store.combat_dodge_bonus = 30
        add_combat_log("你进入闪避姿态（下回合闪避+30%）")

    ## ──────────────── 使用物品 ────────────────

    def use_combat_item(item_id):
        """使用战斗物品并从背包中移除"""
        items = get_combat_items()
        for iid, name, desc, etype, evalue in items:
            if iid == item_id:
                if etype == "heal":
                    store.combat_player_hp = min(store.combat_player_max_hp, store.combat_player_hp + evalue)
                    add_combat_log("使用 %s —— 恢复 %d HP" % (name, evalue))
                elif etype == "stamina":
                    store.combat_player_stamina = min(store.combat_player_max_stamina, store.combat_player_stamina + evalue)
                    add_combat_log("使用 %s —— 恢复 %d 体力" % (name, evalue))
                elif etype == "buff_damage":
                    store.combat_buff_damage = evalue
                    store.combat_buff_turns = 3
                    add_combat_log("使用 %s —— 伤害提升 %d（3回合）" % (name, evalue))
                elif etype == "guaranteed_flee":
                    add_combat_log("使用 %s —— 烟雾弥漫！" % name)
                    store.combat_guaranteed_flee = True
                elif etype == "cure":
                    add_combat_log("使用 %s —— 毒素已清除" % name)
                ## 从背包移除消耗品
                try:
                    remove_item(item_id, 1)
                except Exception:
                    pass
                return True
        return False

    ## ──────────────── 撤退 ────────────────

    def attempt_retreat():
        """尝试撤退，返回是否成功"""
        chance = min(90, 60 + int(store.intrigue * 0.3))
        roll = _combat_random.randint(1, 100)
        if roll <= chance:
            add_combat_log("你成功撤退了！(成功率 %d%%)" % chance)
            return True
        else:
            add_combat_log("撤退失败！敌人挡住了去路。(成功率 %d%%)" % chance)
            return False

    ## ──────────────── 敌人AI回合 ────────────────

    def enemy_turn():
        """执行敌人回合"""
        enemy = ENEMY_DATABASE.get(store.combat_enemy_id, {})
        ai_type = enemy.get("ai", "balanced")
        has_shield = enemy.get("has_shield", False)

        ## ── 眩晕检查 ──
        if store.combat_enemy_stunned:
            store.combat_enemy_stunned = False
            add_combat_log("%s 处于眩晕状态，无法行动！" % store.combat_enemy_name)
            return

        ## 清除敌人上回合的防御/闪避
        store.combat_enemy_defend_active = False

        ## AI决策（增加盾击选项）
        if store.combat_enemy_stamina <= 15:
            action = "defend"
        elif ai_type == "aggressive":
            roll = _combat_random.randint(1, 100)
            if store.combat_enemy_hp < store.combat_enemy_max_hp * 0.3:
                if roll <= 30:
                    action = "defend"
                elif roll <= 50:
                    action = "heavy"
                else:
                    action = "slash"
            elif has_shield and roll <= 15:
                action = "shield_bash"
            elif roll <= 30:
                action = "heavy"
            elif roll <= 45:
                action = "dodge_stance"
            else:
                action = "slash"
        elif ai_type == "defensive":
            roll = _combat_random.randint(1, 100)
            if has_shield and roll <= 20:
                action = "shield_bash"
            elif roll <= 40:
                action = "defend"
            elif roll <= 55:
                action = "dodge_stance"
            elif roll <= 75:
                action = "slash"
            else:
                action = "heavy"
        else:  ## balanced
            roll = _combat_random.randint(1, 100)
            if roll <= 15:
                action = "defend"
            elif has_shield and roll <= 25:
                action = "shield_bash"
            elif roll <= 35:
                action = "dodge_stance"
            elif roll <= 60:
                action = "slash"
            else:
                action = "heavy"

        ## ── 执行敌方行动 ──
        if action == "defend":
            store.combat_enemy_defend_active = True
            store.combat_enemy_stamina = min(100, store.combat_enemy_stamina + 15)
            add_combat_log("%s 摆出防御姿态，恢复体力。" % store.combat_enemy_name)
            return

        if action == "dodge_stance":
            store.combat_enemy_stamina = max(0, store.combat_enemy_stamina - 5)
            store.combat_enemy_dodge_bonus = 30
            add_combat_log("%s 进入闪避姿态。" % store.combat_enemy_name)
            return

        if action == "shield_bash":
            store.combat_enemy_stamina = max(0, store.combat_enemy_stamina - 15)
            bash_dmg = max(1, int(store.combat_enemy_attack * 0.3))
            store.combat_player_hp = max(0, store.combat_player_hp - bash_dmg)
            stamina_drain = _combat_random.randint(8, 16)
            store.combat_player_stamina = max(0, store.combat_player_stamina - stamina_drain)
            stun_roll = _combat_random.randint(1, 100) <= 25
            if stun_roll:
                store.combat_player_stunned = True
            store.combat_hit_flash = True
            store.combat_show_damage = True
            store.combat_damage_text = str(bash_dmg)
            store.combat_damage_pos = "player"
            stun_txt = "你被击晕了！" if stun_roll else ""
            add_combat_log("%s 盾击！%d伤害，削%d体力 %s" % (store.combat_enemy_name, bash_dmg, stamina_drain, stun_txt))
            store.combat_defend_active = False
            return

        ## 攻击动作
        is_heavy = (action == "heavy")
        stamina_cost = 20 if is_heavy else 10
        store.combat_enemy_stamina = max(0, store.combat_enemy_stamina - stamina_cost)

        hit_pen, _, dmg_mult = get_fatigue_penalties(store.combat_enemy_stamina)
        base_accuracy = 70 if is_heavy else 85

        ## 随机选择攻击部位（新增颈部5%）
        part_roll = _combat_random.randint(1, 100)
        if part_roll <= 5:
            body_part = "neck"
        elif part_roll <= 18:
            body_part = "head"
        elif part_roll <= 75:
            body_part = "body"
        else:
            body_part = "limbs"

        part_dmg_mult, part_acc_mod, injury_type = get_body_part_mod(body_part)
        base_accuracy += part_acc_mod

        ## 玩家闪避（含姿态加成和闪避姿态）
        _, stance_dodge_mod, _, _ = get_stance_mods()
        player_dodge = store.combat_player_dodge + store.combat_dodge_bonus + stance_dodge_mod
        _, dodge_pen, _ = get_fatigue_penalties(store.combat_player_stamina)

        hit_chance = max(10, min(95, base_accuracy - hit_pen - max(0, player_dodge - dodge_pen)))
        roll = _combat_random.randint(1, 100)

        part_name = get_body_part_name(body_part)
        atk_name = "猛击" if is_heavy else "斩击"

        ## 消耗玩家闪避加成
        store.combat_dodge_bonus = 0

        if roll > hit_chance:
            add_combat_log("%s %s你的%s —— 闪避！(%d%%)" % (store.combat_enemy_name, atk_name, part_name, hit_chance))
            ## ── 反击判定：守势+防御状态下25%概率反击 ──
            if store.combat_stance == "defensive" and store.combat_defend_active:
                if _combat_random.randint(1, 100) <= 25:
                    counter_dmg = max(1, int(store.combat_player_attack * 0.5))
                    store.combat_enemy_hp = max(0, store.combat_enemy_hp - counter_dmg)
                    add_combat_log("反击！你趁机造成 %d 伤害！" % counter_dmg)
                    store.combat_enemy_hit_flash = True
            return

        ## 计算伤害
        base_dmg = store.combat_enemy_attack
        if is_heavy:
            base_dmg = int(base_dmg * 1.5)
        base_dmg = int(base_dmg * part_dmg_mult * dmg_mult)

        ## 暴击
        is_crit = roll_crit(store.combat_enemy_crit)
        if is_crit:
            base_dmg = int(base_dmg * 1.8)

        ## 玩家防御
        reduction = store.combat_player_defense
        if store.combat_defend_active:
            reduction = int(reduction * 2)
            base_dmg = int(base_dmg * 0.5)

        final_dmg = max(1, base_dmg - reduction)

        ## 随机浮动
        variance = _combat_random.randint(-15, 15)
        final_dmg = max(1, int(final_dmg * (100 + variance) / 100))

        ## 造成伤害
        store.combat_player_hp = max(0, store.combat_player_hp - final_dmg)

        ## ── 流血判定（颈部攻击25%概率）──
        if body_part == "neck" and _combat_random.randint(1, 100) <= 25:
            bleed_dmg = max(2, final_dmg // 4)
            inflict_bleed("player", bleed_dmg, 3)
            add_combat_log("你被割伤了颈部！流血 %d/回合" % bleed_dmg)

        ## ── 眩晕判定（头部猛击15%概率）──
        if body_part == "head" and is_heavy and _combat_random.randint(1, 100) <= 15:
            store.combat_player_stunned = True
            add_combat_log("你被击晕了！下回合无法行动！")

        ## 受伤判定（20%概率）
        if body_part != "body" or is_heavy:
            if _combat_random.randint(1, 100) <= 20:
                if injury_type == "head" and store.injury_head == 0:
                    store.injury_head = 1
                    add_combat_log("头部创伤！（-10谋略，持续1章）")
                elif injury_type == "neck" and store.injury_head == 0:
                    store.injury_head = 1
                    add_combat_log("颈部割伤！（-10谋略，持续1章）")
                elif injury_type == "limbs" and store.injury_limb == 0:
                    store.injury_limb = 1
                    add_combat_log("四肢受伤！（-10闪避，持续1章）")
                elif injury_type == "body" and store.injury_body == 0:
                    store.injury_body = 1
                    add_combat_log("躯干重伤！（-5权力,-5忠诚，持续1章）")

        ## 动画标记
        store.combat_hit_flash = True
        store.combat_show_damage = True
        store.combat_damage_text = str(final_dmg)
        store.combat_damage_pos = "player"

        ## 日志
        crit_text = "【暴击！】" if is_crit else ""
        defend_text = "(防御中)" if store.combat_defend_active else ""
        add_combat_log("%s %s你的%s%s —— %d伤害 %s" % (store.combat_enemy_name, atk_name, part_name, crit_text, final_dmg, defend_text))

        ## 清除玩家防御状态
        store.combat_defend_active = False

    ## ──────────────── 战斗结算 ────────────────

    def calc_combat_rewards():
        """计算战斗奖励"""
        enemy = ENEMY_DATABASE.get(store.combat_enemy_id, {})
        lp = enemy.get("loot_power", (3, 5))
        lw = enemy.get("loot_wealth", (2, 4))
        lr = enemy.get("loot_reputation", (1, 3))

        store.combat_reward_power = _combat_random.randint(lp[0], lp[1])
        store.combat_reward_wealth = _combat_random.randint(lw[0], lw[1])
        store.combat_reward_reputation = _combat_random.randint(lr[0], lr[1])
        store.combat_reward_text = enemy.get("loot_desc", "你获得了战利品。")

    def apply_combat_victory():
        """应用胜利奖励到主属性"""
        change_stat("power", store.combat_reward_power)
        change_stat("wealth", store.combat_reward_wealth)
        change_stat("reputation", store.combat_reward_reputation)

    def apply_combat_defeat():
        """应用失败惩罚"""
        change_stat("power", -2)
        change_stat("loyalty", -3)
        ## 随机受伤
        injury_roll = _combat_random.randint(1, 3)
        if injury_roll == 1 and store.injury_head == 0:
            store.injury_head = 1
        elif injury_roll == 2 and store.injury_body == 0:
            store.injury_body = 1
        elif injury_roll == 3 and store.injury_limb == 0:
            store.injury_limb = 1

    def tick_injuries():
        """章节结束时调用，减少受伤持续时间"""
        if store.injury_head > 0:
            store.injury_head -= 1
        if store.injury_body > 0:
            store.injury_body -= 1
        if store.injury_limb > 0:
            store.injury_limb -= 1

    ## ──────────────── 便捷入口 ────────────────

    def start_combat(enemy_id):
        """从剧情中启动战斗。用法： $ start_combat("bandit")"""
        if init_combat(enemy_id):
            renpy.call("combat_start_internal")


################################################################################
## 4. 动画 Transform
################################################################################

transform combat_screen_show:
    on show:
        alpha 0.0
        ease 0.5 alpha 1.0
    on hide:
        ease 0.4 alpha 0.0

transform combat_slide_up:
    on show:
        alpha 0.0 yoffset 30
        ease 0.35 alpha 1.0 yoffset 0
    on hide:
        ease 0.25 alpha 0.0 yoffset 20

transform combat_shake:
    xoffset 0
    ease 0.04 xoffset 8
    ease 0.04 xoffset -6
    ease 0.04 yoffset 4
    ease 0.04 xoffset 4
    ease 0.04 yoffset -3
    ease 0.04 xoffset -2
    ease 0.04 xoffset 0 yoffset 0

transform combat_hit_red:
    alpha 0.6
    ease 0.4 alpha 0.0

transform combat_damage_float:
    on show:
        alpha 1.0 yoffset 0
        ease 0.8 alpha 0.0 yoffset -60

transform combat_enemy_shake:
    xoffset 0
    ease 0.03 xoffset -10
    ease 0.03 xoffset 8
    ease 0.03 xoffset -6
    ease 0.03 xoffset 4
    ease 0.03 xoffset -2
    ease 0.03 xoffset 0

transform combat_pulse_hp:
    block:
        ease 0.5 alpha 0.7
        ease 0.5 alpha 1.0
        repeat

transform combat_body_btn_hover:
    on idle:
        alpha 0.7
    on hover:
        alpha 1.0

transform combat_victory_zoom:
    on show:
        alpha 0.0 zoom 0.8
        ease 0.6 alpha 1.0 zoom 1.0

transform combat_log_entry:
    on show:
        alpha 0.0 xoffset -10
        ease 0.2 alpha 1.0 xoffset 0


################################################################################
## 5. 主战斗界面
################################################################################

screen combat_screen():
    tag combat
    zorder 300
    modal True

    ## 全屏战斗背景
    add Solid("#0a0812") at combat_screen_show

    ## 暗纹装饰（顶部和底部渐变）
    add Solid("#d4a94208") ysize 120 yalign 0.0
    add Solid("#0f0d1a80") ysize 200 yalign 1.0

    ## ═══════════════════════════════════════════
    ## 顶部：敌人信息区
    ## ═══════════════════════════════════════════

    frame:
        xalign 0.5
        ypos 20
        xpadding 30
        ypadding 18
        xminimum 500
        xmaximum 600
        background Solid("#1a152890")

        vbox:
            spacing 6

            ## 敌人名称 + 难度标签
            hbox:
                xfill True
                yalign 0.5

                hbox:
                    spacing 10
                    text "剑" size 20 color "#e74c3c" yalign 0.5
                    text combat_enemy_name size 22 color "#e0d8c8" font "msyh.ttf" bold True yalign 0.5

                ## 难度徽章
                $ _diff_c = DIFFICULTY_COLORS.get(combat_enemy_difficulty, "#6a5e48")
                frame:
                    xalign 1.0
                    xpadding 10
                    ypadding 3
                    background Solid(_diff_c + "30")
                    text combat_enemy_difficulty size 13 color _diff_c font "msyh.ttf"

            ## 敌人描述
            text combat_enemy_desc size 13 color "#6a5e48" font "msyh.ttf"

            ## 敌人HP条
            hbox:
                spacing 10
                xfill True
                yalign 0.5

                text "HP" size 14 color "#e74c3c" yalign 0.5 xsize 30
                bar:
                    value AnimatedValue(combat_enemy_hp, combat_enemy_max_hp, delay=0.4)
                    xfill True
                    ysize 14
                    left_bar Solid("#c0392b")
                    right_bar Solid("#1a1528")
                text "[combat_enemy_hp]/[combat_enemy_max_hp]" size 13 color "#c8b890" yalign 0.5 xsize 80 text_align 1.0

            ## 敌人体力条
            hbox:
                spacing 10
                xfill True
                yalign 0.5

                text "体力" size 12 color "#3498db" yalign 0.5 xsize 30 font "msyh.ttf"
                bar:
                    value AnimatedValue(combat_enemy_stamina, 100, delay=0.3)
                    xfill True
                    ysize 8
                    left_bar Solid("#2980b9")
                    right_bar Solid("#1a1528")
                $ _enemy_fatigue = get_fatigue_level(combat_enemy_stamina)
                $ _enemy_fatigue_c = get_fatigue_color(_enemy_fatigue)
                text get_fatigue_name(_enemy_fatigue) size 11 color _enemy_fatigue_c yalign 0.5 xsize 80 text_align 1.0 font "msyh.ttf"

            ## 敌人状态标记
            hbox:
                spacing 8
                if combat_enemy_defend_active:
                    frame:
                        xpadding 6
                        ypadding 2
                        background Solid("#3498db30")
                        text "盾 防御中" size 11 color "#3498db" font "msyh.ttf"
                if combat_enemy_dodge_bonus > 0:
                    frame:
                        xpadding 6
                        ypadding 2
                        background Solid("#2ecc7130")
                        text "风 闪避姿态" size 11 color "#2ecc71" font "msyh.ttf"
                if combat_enemy_bleed_turns > 0:
                    frame:
                        xpadding 6
                        ypadding 2
                        background Solid("#e7283c30")
                        text "血 流血[combat_enemy_bleed_turns]" size 11 color "#e7283c" font "msyh.ttf"
                if combat_enemy_stunned:
                    frame:
                        xpadding 6
                        ypadding 2
                        background Solid("#f39c1230")
                        text "晕 眩晕" size 11 color "#f39c12" font "msyh.ttf"


    ## ═══════════════════════════════════════════
    ## 中央：战斗日志
    ## ═══════════════════════════════════════════

    frame:
        xalign 0.5
        yalign 0.42
        xpadding 24
        ypadding 16
        xminimum 550
        xmaximum 620
        yminimum 160
        background Solid("#0f0d1acc")

        vbox:
            spacing 3

            ## 回合标题
            hbox:
                spacing 8
                text "—" size 12 color "#d4a94260" yalign 0.5
                text "第 [combat_turn] 回合" size 14 color "#d4a942" font "msyh.ttf" yalign 0.5
                text "—" size 12 color "#d4a94260" yalign 0.5

            null height 4

            ## 日志内容
            for _log_idx, _log_msg in enumerate(combat_log):
                $ _log_alpha = 0.4 + 0.12 * _log_idx  ## 越新的越亮
                $ _log_color = "#c8b890" if _log_idx == len(combat_log) - 1 else ("#8a7e60%02x" % int(min(255, _log_alpha * 255)))
                text _log_msg:
                    size 14
                    color ("#c8b890" if _log_idx >= len(combat_log) - 2 else "#6a5e48")
                    font "msyh.ttf"


    ## ═══════════════════════════════════════════
    ## 受击闪红特效
    ## ═══════════════════════════════════════════

    if combat_hit_flash:
        add Solid("#ff000040") at combat_hit_red
        timer 0.4 action SetVariable("combat_hit_flash", False)

    if combat_enemy_hit_flash:
        timer 0.4 action SetVariable("combat_enemy_hit_flash", False)

    ## 浮动伤害数字
    if combat_show_damage:
        $ _dmg_y = 130 if combat_damage_pos == "enemy" else 460
        $ _dmg_color = "#ffd866" if combat_damage_pos == "enemy" else "#e74c3c"
        text combat_damage_text:
            xalign 0.5
            ypos _dmg_y
            size 36
            color _dmg_color
            bold True
            outlines [(3, "#000000cc", 0, 0)]
            at combat_damage_float
        timer 0.9 action SetVariable("combat_show_damage", False)


    ## ═══════════════════════════════════════════
    ## 底部左侧：玩家信息
    ## ═══════════════════════════════════════════

    frame:
        xpos 20
        yalign 0.98
        xpadding 20
        ypadding 14
        xminimum 280
        xmaximum 320
        background Solid("#1a152890")

        vbox:
            spacing 5

            ## 玩家名
            hbox:
                spacing 8
                text "盾" size 18 color "#d4a942" yalign 0.5
                text "[player_name]" size 18 color "#d4a942" font "msyh.ttf" bold True yalign 0.5

            ## HP条
            hbox:
                spacing 8
                xfill True
                text "HP" size 13 color "#e74c3c" yalign 0.5 xsize 30

                $ _hp_pct = combat_player_hp * 100 // max(1, combat_player_max_hp)
                $ _hp_color = "#c0392b" if _hp_pct <= 25 else ("#e67e22" if _hp_pct <= 50 else "#27ae60")

                bar:
                    value AnimatedValue(combat_player_hp, combat_player_max_hp, delay=0.4)
                    xfill True
                    ysize 14
                    left_bar Solid(_hp_color)
                    right_bar Solid("#1a1528")

                text "[combat_player_hp]/[combat_player_max_hp]" size 12 color "#c8b890" yalign 0.5 xsize 70 text_align 1.0

            ## 体力条
            hbox:
                spacing 8
                xfill True
                text "体力" size 11 color "#3498db" font "msyh.ttf" yalign 0.5 xsize 30

                bar:
                    value AnimatedValue(combat_player_stamina, combat_player_max_stamina, delay=0.3)
                    xfill True
                    ysize 10
                    left_bar Solid("#2980b9")
                    right_bar Solid("#1a1528")

                text "[combat_player_stamina]/[combat_player_max_stamina]" size 11 color "#8a7e60" yalign 0.5 xsize 70 text_align 1.0

            ## 疲劳 + 姿态
            $ _p_fatigue = get_fatigue_level(combat_player_stamina)
            $ _p_fatigue_c = get_fatigue_color(_p_fatigue)
            $ _p_fatigue_n = get_fatigue_name(_p_fatigue)
            hbox:
                spacing 8
                text "疲劳：" size 12 color "#6a5e48" font "msyh.ttf" yalign 0.5
                text _p_fatigue_n size 13 color _p_fatigue_c font "msyh.ttf" bold True yalign 0.5
                text "|" size 12 color "#4a403060" yalign 0.5
                $ _stance_n = get_stance_name()
                $ _stance_c = get_stance_color()
                text _stance_n size 13 color _stance_c font "msyh.ttf" bold True yalign 0.5

            ## 战斗属性一览
            hbox:
                spacing 10
                text "攻[combat_player_attack]" size 11 color "#e74c3c"
                text "防[combat_player_defense]" size 11 color "#3498db"
                text "闪[combat_player_dodge]%" size 11 color "#2ecc71"
                text "暴[combat_player_crit]%" size 11 color "#f39c12"
                if combat_respite_stacks > 0:
                    text "气[combat_respite_stacks]" size 11 color "#9b59b6"

            ## 状态标记
            hbox:
                spacing 6
                if combat_defend_active:
                    frame:
                        xpadding 5
                        ypadding 2
                        background Solid("#3498db30")
                        text "盾 防御" size 11 color "#3498db" font "msyh.ttf"
                if combat_dodge_bonus > 0:
                    frame:
                        xpadding 5
                        ypadding 2
                        background Solid("#2ecc7130")
                        text "风 闪避" size 11 color "#2ecc71" font "msyh.ttf"
                if combat_player_bleed_turns > 0:
                    frame:
                        xpadding 5
                        ypadding 2
                        background Solid("#e7283c30")
                        text "血 流血[combat_player_bleed_turns]" size 11 color "#e7283c" font "msyh.ttf"
                if combat_player_stunned:
                    frame:
                        xpadding 5
                        ypadding 2
                        background Solid("#f39c1230")
                        text "晕 眩晕" size 11 color "#f39c12" font "msyh.ttf"
                if injury_head > 0:
                    frame:
                        xpadding 5
                        ypadding 2
                        background Solid("#e74c3c30")
                        text "头伤" size 11 color "#e74c3c" font "msyh.ttf"
                if injury_body > 0:
                    frame:
                        xpadding 5
                        ypadding 2
                        background Solid("#e74c3c30")
                        text "躯伤" size 11 color "#e74c3c" font "msyh.ttf"
                if injury_limb > 0:
                    frame:
                        xpadding 5
                        ypadding 2
                        background Solid("#e74c3c30")
                        text "肢伤" size 11 color "#e74c3c" font "msyh.ttf"


    ## ═══════════════════════════════════════════
    ## 底部右侧：行动按钮
    ## ═══════════════════════════════════════════

    if combat_phase == "player" and not combat_targeting:
        frame at combat_slide_up:
            xalign 0.98
            yalign 0.98
            xpadding 16
            ypadding 14
            background Solid("#1a152890")

            vbox:
                spacing 6

                ## 行动标题 + 姿态切换
                hbox:
                    spacing 12
                    text "* 行动" size 15 color "#d4a942" font "msyh.ttf" yalign 0.5

                    ## 姿态切换按钮（不消耗回合）
                    $ _st_c = get_stance_color()
                    $ _st_n = get_stance_name()
                    button:
                        xsize 80
                        ysize 26
                        background Solid(_st_c + "30")
                        hover_background Solid(_st_c + "50")
                        action Function(toggle_stance)
                        vbox:
                            xalign 0.5
                            yalign 0.5
                            text _st_n size 13 color _st_c font "msyh.ttf" xalign 0.5

                grid 2 4:
                    spacing 6

                    ## 斩击
                    button:
                        xsize 135
                        ysize 48
                        background Solid("#2a1f3c")
                        hover_background Solid("#3a2f50")
                        action [SetVariable("combat_attack_type", "slash"), SetVariable("combat_targeting", True)]
                        sensitive (combat_player_stamina >= 10)

                        vbox:
                            xalign 0.5
                            yalign 0.5
                            text "剑 斩击" size 14 color "#e0d8c8" font "msyh.ttf" xalign 0.5
                            text "消耗10体力" size 9 color "#6a5e48" xalign 0.5

                    ## 猛击
                    button:
                        xsize 135
                        ysize 48
                        background Solid("#2a1f3c")
                        hover_background Solid("#3a2f50")
                        action [SetVariable("combat_attack_type", "heavy"), SetVariable("combat_targeting", True)]
                        sensitive (combat_player_stamina >= 20)

                        vbox:
                            xalign 0.5
                            yalign 0.5
                            text "锤 猛击" size 14 color "#e0d8c8" font "msyh.ttf" xalign 0.5
                            text "1.5x伤 消耗20" size 9 color "#6a5e48" xalign 0.5

                    ## 盾击（新增！）
                    button:
                        xsize 135
                        ysize 48
                        background Solid("#2a2a1a")
                        hover_background Solid("#3a3a2a")
                        action Function(shield_bash_and_next)
                        sensitive (combat_player_stamina >= 15)

                        vbox:
                            xalign 0.5
                            yalign 0.5
                            text "盾 盾击" size 14 color "#f1c40f" font "msyh.ttf" xalign 0.5
                            text "削体+晕 消耗15" size 9 color "#6a5e48" xalign 0.5

                    ## 防御
                    button:
                        xsize 135
                        ysize 48
                        background Solid("#1a2a3c")
                        hover_background Solid("#2a3a50")
                        action Function(player_defend_and_next)

                        vbox:
                            xalign 0.5
                            yalign 0.5
                            text "盾 防御" size 14 color "#3498db" font "msyh.ttf" xalign 0.5
                            text "减伤50% +体力" size 9 color "#6a5e48" xalign 0.5

                    ## 闪避姿态
                    button:
                        xsize 135
                        ysize 48
                        background Solid("#1a3c2a")
                        hover_background Solid("#2a503a")
                        action Function(dodge_stance_and_next)
                        sensitive (combat_player_stamina >= 5)

                        vbox:
                            xalign 0.5
                            yalign 0.5
                            text "风 闪避" size 14 color "#2ecc71" font "msyh.ttf" xalign 0.5
                            text "闪避+30% 消耗5" size 9 color "#6a5e48" xalign 0.5

                    ## 使用物品
                    button:
                        xsize 135
                        ysize 48
                        background Solid("#3c2a1a")
                        hover_background Solid("#503a2a")
                        action Show("combat_items_panel")

                        vbox:
                            xalign 0.5
                            yalign 0.5
                            text "药 物品" size 14 color "#f39c12" font "msyh.ttf" xalign 0.5
                            text "使用物品" size 9 color "#6a5e48" xalign 0.5

                    ## 撤退
                    button:
                        xsize 135
                        ysize 48
                        background Solid("#3c1a1a")
                        hover_background Solid("#501a1a")
                        action Function(retreat_and_check)

                        vbox:
                            xalign 0.5
                            yalign 0.5
                            $ _retreat_pct = min(90, 60 + int(intrigue * 0.3))
                            text "退 撤退" size 14 color "#e74c3c" font "msyh.ttf" xalign 0.5
                            text "成功率[_retreat_pct]%" size 9 color "#6a5e48" xalign 0.5

                    ## 占位（2x4 grid需要8个元素）
                    null


    ## ═══════════════════════════════════════════
    ## 身体部位选择面板
    ## ═══════════════════════════════════════════

    if combat_targeting:
        frame at combat_slide_up:
            xalign 0.5
            yalign 0.75
            xpadding 24
            ypadding 18
            background Solid("#1a1528ee")

            vbox:
                spacing 10
                xalign 0.5

                text "选择攻击部位" size 18 color "#d4a942" font "msyh.ttf" xalign 0.5

                grid 2 2:
                    spacing 10
                    xalign 0.5

                    ## 头部
                    button:
                        xsize 130
                        ysize 75
                        background Solid("#3c1a1a")
                        hover_background Solid("#501a1a")
                        action Function(execute_player_attack, body_part="head")

                        vbox:
                            xalign 0.5
                            yalign 0.5
                            spacing 2
                            text "头部" size 15 color "#e74c3c" font "msyh.ttf" xalign 0.5 bold True
                            text "1.5x伤 -15%命中" size 10 color "#c8b890" xalign 0.5
                            text "可眩晕" size 10 color "#f39c12" xalign 0.5

                    ## 颈部（新增！）
                    button:
                        xsize 130
                        ysize 75
                        background Solid("#4a1a2a")
                        hover_background Solid("#601a2a")
                        action Function(execute_player_attack, body_part="neck")

                        vbox:
                            xalign 0.5
                            yalign 0.5
                            spacing 2
                            text "颈部" size 15 color "#ff6b6b" font "msyh.ttf" xalign 0.5 bold True
                            text "2.0x伤 -25%命中" size 10 color "#c8b890" xalign 0.5
                            text "可流血" size 10 color "#e7283c" xalign 0.5

                    ## 躯干
                    button:
                        xsize 130
                        ysize 75
                        background Solid("#2a2a3c")
                        hover_background Solid("#3a3a50")
                        action Function(execute_player_attack, body_part="body")

                        vbox:
                            xalign 0.5
                            yalign 0.5
                            spacing 2
                            text "躯干" size 15 color "#e0d8c8" font "msyh.ttf" xalign 0.5 bold True
                            text "1.0x伤 标准命中" size 10 color "#c8b890" xalign 0.5
                            text "最稳妥" size 10 color "#8a7e60" xalign 0.5

                    ## 四肢
                    button:
                        xsize 130
                        ysize 75
                        background Solid("#1a3c2a")
                        hover_background Solid("#2a503a")
                        action Function(execute_player_attack, body_part="limbs")

                        vbox:
                            xalign 0.5
                            yalign 0.5
                            spacing 2
                            text "四肢" size 15 color "#2ecc71" font "msyh.ttf" xalign 0.5 bold True
                            text "0.75x伤 +10%命中" size 10 color "#c8b890" xalign 0.5
                            text "高命中" size 10 color "#2ecc71" xalign 0.5

                ## 取消按钮
                textbutton "取消":
                    xalign 0.5
                    text_size 14
                    text_color "#6a5e48"
                    text_hover_color "#c8b890"
                    action [SetVariable("combat_targeting", False), SetVariable("combat_attack_type", "")]


    ## ═══════════════════════════════════════════
    ## 等待敌人回合指示
    ## ═══════════════════════════════════════════

    if combat_phase == "enemy":
        frame:
            xalign 0.5
            yalign 0.85
            xpadding 30
            ypadding 12
            background Solid("#1a152890")
            text "%s 的回合..." % combat_enemy_name size 16 color "#e74c3c" font "msyh.ttf" at combat_pulse_hp


################################################################################
## 6. 物品选择面板
################################################################################

screen combat_items_panel():
    zorder 310
    modal True

    add Solid("#00000088")

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 24
        xminimum 400
        background Solid("#0f0d1af5")

        vbox:
            spacing 12

            text "* 物品" size 20 color "#d4a942" font "msyh.ttf" xalign 0.5

            add Solid("#d4a94230") xsize 300 ysize 1 xalign 0.5

            $ _items = get_combat_items()

            if len(_items) == 0:
                text "没有可用的物品" size 15 color "#6a5e48" font "msyh.ttf" xalign 0.5
            else:
                for _item_id, _item_name, _item_desc, _item_type, _item_val in _items:
                    button:
                        xfill True
                        xpadding 16
                        ypadding 10
                        background Solid("#1a152840")
                        hover_background Solid("#1a152880")
                        action [Function(use_item_and_next, item_id=_item_id), Hide("combat_items_panel")]

                        hbox:
                            spacing 12
                            yalign 0.5

                            $ _item_icon = "药" if _item_type == "heal" else "草"
                            $ _item_color = "#2ecc71" if _item_type == "heal" else "#3498db"
                            frame:
                                xsize 36
                                ysize 36
                                background Solid(_item_color + "25")
                                text _item_icon xalign 0.5 yalign 0.5 size 18 color _item_color

                            vbox:
                                spacing 2
                                text _item_name size 16 color "#e0d8c8" font "msyh.ttf"
                                text _item_desc size 12 color "#8a7e60"

            null height 6

            textbutton "返回":
                xalign 0.5
                text_size 16
                text_color "#6a5e48"
                text_hover_color "#c8b890"
                text_font "msyh.ttf"
                action Hide("combat_items_panel")


################################################################################
## 7. 胜利界面
################################################################################

screen combat_victory():
    tag combat_result
    zorder 310
    modal True

    add Solid("#0a0812ee")

    frame at combat_victory_zoom:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 40
        xminimum 500
        background Solid("#0f0d1af8")

        vbox:
            spacing 14
            xalign 0.5

            ## 标题
            text "* 战斗胜利 *" size 36 color "#d4a942" font "msyh.ttf" xalign 0.5 outlines [(3, "#000000cc", 0, 0), (5, "#d4a94220", 0, 0)]

            add Solid("#d4a94240") xsize 350 ysize 1 xalign 0.5

            ## 击败敌人
            hbox:
                xalign 0.5
                spacing 8
                text "击败：" size 16 color "#8a7e60" font "msyh.ttf" yalign 0.5
                text combat_enemy_name size 20 color "#e0d8c8" font "msyh.ttf" bold True yalign 0.5

            null height 8

            ## 战利品描述
            frame:
                xalign 0.5
                xpadding 20
                ypadding 12
                background Solid("#1a152840")
                xminimum 380
                text combat_reward_text size 14 color "#c8b890" font "msyh.ttf" xalign 0.5

            null height 6

            ## 奖励明细
            text "—— 获得 ——" size 14 color "#6a5e48" xalign 0.5

            hbox:
                spacing 24
                xalign 0.5

                if combat_reward_power > 0:
                    hbox:
                        spacing 4
                        text "剑" size 16 color "#e74c3c"
                        text "权力 +[combat_reward_power]" size 16 color "#e74c3c" font "msyh.ttf"

                if combat_reward_wealth > 0:
                    hbox:
                        spacing 4
                        text "金" size 16 color "#f39c12"
                        text "财富 +[combat_reward_wealth]" size 16 color "#f39c12" font "msyh.ttf"

                if combat_reward_reputation > 0:
                    hbox:
                        spacing 4
                        text "*" size 16 color "#2ecc71"
                        text "声望 +[combat_reward_reputation]" size 16 color "#2ecc71" font "msyh.ttf"

            null height 6

            ## 战斗统计
            frame:
                xalign 0.5
                xpadding 20
                ypadding 10
                background Solid("#1a152830")
                xminimum 350

                vbox:
                    spacing 4
                    $ _hp_remain_pct = combat_player_hp * 100 // max(1, combat_player_max_hp)
                    hbox:
                        xfill True
                        text "剩余HP" size 13 color "#6a5e48" font "msyh.ttf"
                        text "[combat_player_hp]/[combat_player_max_hp] ([_hp_remain_pct]%)" size 13 color "#c8b890" xalign 1.0
                    hbox:
                        xfill True
                        text "回合数" size 13 color "#6a5e48" font "msyh.ttf"
                        text "[combat_turn]" size 13 color "#c8b890" xalign 1.0
                    hbox:
                        xfill True
                        text "最长连击" size 13 color "#6a5e48" font "msyh.ttf"
                        text "[combat_combo_count]" size 13 color "#c8b890" xalign 1.0

            null height 10
            add Solid("#d4a94230") xsize 350 ysize 1 xalign 0.5
            null height 6

            ## 确认按钮
            textbutton "继续":
                xalign 0.5
                text_size 22
                text_color "#d4a942"
                text_hover_color "#ffd866"
                text_font "msyh.ttf"
                action Return("victory_done")


################################################################################
## 8. 失败界面
################################################################################

screen combat_defeat():
    tag combat_result
    zorder 310
    modal True

    add Solid("#0a0812ee")

    frame at combat_victory_zoom:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 40
        xminimum 500
        background Solid("#1a0a0af8")

        vbox:
            spacing 14
            xalign 0.5

            ## 标题
            text "—— 战斗失败 ——" size 32 color "#e74c3c" font "msyh.ttf" xalign 0.5 outlines [(3, "#000000cc", 0, 0)]

            add Solid("#e74c3c40") xsize 350 ysize 1 xalign 0.5

            text "你被 [combat_enemy_name] 击败了" size 18 color "#c8b890" font "msyh.ttf" xalign 0.5

            null height 8

            ## 惩罚说明
            frame:
                xalign 0.5
                xpadding 20
                ypadding 12
                background Solid("#1a152840")
                xminimum 380

                vbox:
                    spacing 6
                    text "战败的代价" size 16 color "#e74c3c" font "msyh.ttf"
                    hbox:
                        spacing 6
                        text "•" size 14 color "#6a5e48"
                        text "权力 -2，忠诚 -3" size 14 color "#e67e22" font "msyh.ttf"
                    hbox:
                        spacing 6
                        text "•" size 14 color "#6a5e48"
                        text "可能留下持续伤势" size 14 color "#e67e22" font "msyh.ttf"
                    hbox:
                        spacing 6
                        text "•" size 14 color "#6a5e48"
                        text "但你的故事还未结束..." size 14 color "#8a7e60" font "msyh.ttf"

            null height 10
            add Solid("#e74c3c30") xsize 350 ysize 1 xalign 0.5
            null height 6

            textbutton "忍辱负重，继续前行":
                xalign 0.5
                text_size 20
                text_color "#d4a942"
                text_hover_color "#ffd866"
                text_font "msyh.ttf"
                action Return("defeat_done")


################################################################################
## 9. 撤退结果界面
################################################################################

screen combat_retreat():
    tag combat_result
    zorder 310
    modal True

    add Solid("#0a0812ee")

    frame at combat_victory_zoom:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 40
        xminimum 450
        background Solid("#0f0d1af8")

        vbox:
            spacing 14
            xalign 0.5

            text "—— 成功撤退 ——" size 28 color "#f39c12" font "msyh.ttf" xalign 0.5 outlines [(2, "#000000cc", 0, 0)]

            add Solid("#f39c1230") xsize 300 ysize 1 xalign 0.5

            text "你见机行事，从战场上撤退了。" size 16 color "#c8b890" font "msyh.ttf" xalign 0.5
            text "虽然没有获得战利品，但保全了性命。" size 14 color "#8a7e60" font "msyh.ttf" xalign 0.5

            null height 10

            textbutton "继续":
                xalign 0.5
                text_size 20
                text_color "#d4a942"
                text_hover_color "#ffd866"
                text_font "msyh.ttf"
                action Return("retreat_done")


################################################################################
## 10. 战斗行动函数 (UI回调)
################################################################################

init python:

    def execute_player_attack(body_part="body"):
        """执行玩家攻击后切换到敌人回合"""
        store.combat_targeting = False
        player_attack(store.combat_attack_type, body_part)
        store.combat_attack_type = ""

        ## 检查敌人是否被击败
        if store.combat_enemy_hp <= 0:
            store.combat_phase = "victory"
            gain_respite(5)  ## 击杀+5恢复能量
        else:
            store.combat_phase = "enemy"

        renpy.restart_interaction()

    def player_defend_and_next():
        """玩家防御后切换到敌人回合"""
        player_defend()
        store.combat_phase = "enemy"
        renpy.restart_interaction()

    def dodge_stance_and_next():
        """玩家闪避姿态后切换到敌人回合"""
        player_dodge_stance()
        store.combat_phase = "enemy"
        renpy.restart_interaction()

    def shield_bash_and_next():
        """盾击后切换到敌人回合"""
        player_shield_bash()
        if store.combat_enemy_hp <= 0:
            store.combat_phase = "victory"
        else:
            store.combat_phase = "enemy"
        renpy.restart_interaction()

    def toggle_stance():
        """切换姿态： balanced -> offensive -> defensive -> balanced"""
        if store.combat_stance == "balanced":
            store.combat_stance = "offensive"
            add_combat_log("切换至【攻势】: +20%伤害, -10闪避")
        elif store.combat_stance == "offensive":
            store.combat_stance = "defensive"
            add_combat_log("切换至【守势】: +15闪避, -20%伤害, 可反击")
        else:
            store.combat_stance = "balanced"
            add_combat_log("切换至【均衡】: 标准战斗状态")
        renpy.restart_interaction()

    def use_item_and_next(item_id):
        """使用物品后切换到敌人回合"""
        use_combat_item(item_id)
        store.combat_phase = "enemy"
        renpy.restart_interaction()

    def retreat_and_check():
        """尝试撤退"""
        if attempt_retreat():
            store.combat_phase = "retreat"
        else:
            store.combat_phase = "enemy"
        renpy.restart_interaction()


################################################################################
## 11. 战斗主流程 (label)
################################################################################

label combat_start_internal:
    ## 播放战斗音乐
    if renpy.loadable("audio/music/battle_prepare.ogg"):
        play music "audio/music/battle_prepare.ogg" fadein 1.0

    show screen combat_screen
    with dissolve

    ## 主循环
    label .combat_loop:

        ## ── 回合开始：流血结算 ──
        $ apply_bleed_tick()

        ## 流血致死检查
        if combat_enemy_hp <= 0:
            $ combat_phase = "victory"
            jump .combat_victory
        if combat_player_hp <= 0:
            $ combat_phase = "defeat"
            jump .combat_defeat

        ## ── 姿态体力自动回复 ──
        $ _s_dmg, _s_dodge, _s_cost, _s_regen = get_stance_mods()
        $ combat_player_stamina = min(combat_player_max_stamina, combat_player_stamina + _s_regen)

        ## ── 恢复机制自动触发 ──
        $ use_respite()

        ## ── 眩晕检查：玩家被眩晕则跳过行动 ──
        if combat_player_stunned:
            $ combat_player_stunned = False
            $ add_combat_log("你处于眩晕状态，无法行动！")
            $ combat_phase = "enemy"

        ## 等待玩家行动
        if combat_phase == "player":
            $ ui.interact()

        ## 检查战斗结束条件
        if combat_phase == "victory":
            jump .combat_victory

        if combat_phase == "retreat":
            jump .combat_retreat

        ## 敌人回合
        if combat_phase == "enemy":
            $ renpy.pause(0.6, hard=True)
            $ enemy_turn()

            ## 检查玩家是否被击败
            if combat_player_hp <= 0:
                $ combat_phase = "defeat"
                jump .combat_defeat

            ## 回合结束，回到玩家回合
            $ combat_turn += 1
            $ combat_phase = "player"
            $ renpy.restart_interaction()

        jump .combat_loop

    ## ── 胜利结算 ──
    label .combat_victory:
        if renpy.loadable("audio/music/victory.ogg"):
            play music "audio/music/victory.ogg" fadein 0.5
        $ calc_combat_rewards()
        hide screen combat_screen
        show screen combat_victory
        $ _result = ui.interact()
        hide screen combat_victory
        $ apply_combat_victory()
        $ combat_active = False
        $ combat_result = "victory"
        return

    ## ── 失败结算 ──
    label .combat_defeat:
        hide screen combat_screen
        show screen combat_defeat
        $ _result = ui.interact()
        hide screen combat_defeat
        $ apply_combat_defeat()
        $ combat_active = False
        $ combat_result = "defeat"
        return

    ## ── 撤退结算 ──
    label .combat_retreat:
        hide screen combat_screen
        show screen combat_retreat
        $ _result = ui.interact()
        hide screen combat_retreat
        $ combat_active = False
        $ combat_result = "retreat"
        return


################################################################################
## 12. 便捷调用 label (可从剧情直接 call)
################################################################################

label combat_start(enemy_id="bandit"):
    $ _combat_ok = init_combat(enemy_id)
    if _combat_ok:
        call combat_start_internal from _call_combat_start_internal
    else:
        "（错误：未找到敌人数据 [enemy_id]）"
    return


################################################################################
## 13. 受伤状态显示（可挂在 say screen 上作为持续提醒）
################################################################################

screen combat_injury_indicator():
    zorder 100

    if injury_head > 0 or injury_body > 0 or injury_limb > 0:
        frame:
            xalign 1.0
            yalign 0.0
            xoffset -10
            yoffset 50
            xpadding 12
            ypadding 8
            background Solid("#1a0a0acc")

            vbox:
                spacing 3
                text "伤势" size 12 color "#e74c3c" font "msyh.ttf"
                if injury_head > 0:
                    text "头部创伤 (谋略-10)" size 11 color "#e67e22" font "msyh.ttf"
                if injury_body > 0:
                    text "躯干重伤 (权力-5,忠诚-5)" size 11 color "#e67e22" font "msyh.ttf"
                if injury_limb > 0:
                    text "肢体受伤 (闪避-10)" size 11 color "#e67e22" font "msyh.ttf"


################################################################################
## 14. 战斗预览界面（可选：战斗前查看敌人信息）
################################################################################

screen combat_preview(enemy_id="bandit"):
    zorder 305
    modal True

    add Solid("#0a0812dd")

    $ _prev_enemy = ENEMY_DATABASE.get(enemy_id, {})
    $ _prev_stats = calc_player_combat_stats()

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 40
        ypadding 30
        xminimum 550
        background Solid("#0f0d1af5")

        vbox:
            spacing 14
            xalign 0.5

            text "* 战斗即将开始" size 26 color "#d4a942" font "msyh.ttf" xalign 0.5 outlines [(2, "#000000cc", 0, 0)]

            add Solid("#d4a94230") xsize 400 ysize 1 xalign 0.5

            ## 对手信息
            frame:
                xfill True
                xpadding 20
                ypadding 14
                background Solid("#1a152840")

                vbox:
                    spacing 6
                    hbox:
                        spacing 10
                        text "对手：" size 16 color "#8a7e60" font "msyh.ttf" yalign 0.5
                        text _prev_enemy.get("name", "???") size 20 color "#e0d8c8" font "msyh.ttf" bold True yalign 0.5
                        $ _pd_c = DIFFICULTY_COLORS.get(_prev_enemy.get("difficulty", ""), "#6a5e48")
                        frame:
                            xpadding 8
                            ypadding 2
                            background Solid(_pd_c + "30")
                            text _prev_enemy.get("difficulty", "") size 12 color _pd_c font "msyh.ttf"

                    text _prev_enemy.get("desc", "") size 14 color "#8a7e60" font "msyh.ttf"

                    null height 4

                    hbox:
                        spacing 16
                        text "HP: %d" % _prev_enemy.get("hp", 0) size 13 color "#e74c3c"
                        text "攻： %d" % _prev_enemy.get("attack", 0) size 13 color "#e67e22"
                        text "防： %d" % _prev_enemy.get("defense", 0) size 13 color "#3498db"
                        text "闪： %d%%" % _prev_enemy.get("dodge", 0) size 13 color "#2ecc71"

            ## 你的战力
            frame:
                xfill True
                xpadding 20
                ypadding 14
                background Solid("#1a152840")

                vbox:
                    spacing 6
                    text "你的战力" size 16 color "#d4a942" font "msyh.ttf"
                    hbox:
                        spacing 16
                        text "HP: %d" % _prev_stats["max_hp"] size 13 color "#e74c3c"
                        text "攻： %d" % _prev_stats["attack"] size 13 color "#e67e22"
                        text "防： %d" % _prev_stats["defense"] size 13 color "#3498db"
                        text "闪： %d%%" % _prev_stats["dodge"] size 13 color "#2ecc71"
                        text "暴： %d%%" % _prev_stats["crit"] size 13 color "#f39c12"

                    ## 受伤警告
                    if injury_head > 0 or injury_body > 0 or injury_limb > 0:
                        hbox:
                            spacing 6
                            text "！" size 14 color "#e74c3c" yalign 0.5
                            text "你身上有未痊愈的伤势，战斗力会受影响！" size 13 color "#e74c3c" font "msyh.ttf" yalign 0.5

            null height 6
            add Solid("#d4a94220") xsize 400 ysize 1 xalign 0.5
            null height 4

            ## 按钮
            hbox:
                spacing 24
                xalign 0.5

                textbutton "迎战":
                    text_size 22
                    text_color "#d4a942"
                    text_hover_color "#ffd866"
                    text_font "msyh.ttf"
                    action [Hide("combat_preview"), Return("fight")]

                textbutton "查看属性":
                    text_size 18
                    text_color "#6a5e48"
                    text_hover_color "#c8b890"
                    text_font "msyh.ttf"
                    action Show("stats_screen")


################################################################################
## 15. 带预览的战斗入口（推荐用法）
################################################################################

label combat_with_preview(enemy_id="bandit"):
    show screen combat_preview(enemy_id)
    $ _preview_result = ui.interact()
    if _preview_result == "fight":
        call combat_start(enemy_id) from _call_combat_start
    return

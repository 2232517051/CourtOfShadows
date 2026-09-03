# -*- coding: utf-8 -*-
"""铁血线会战平衡验证 (世界的尽头批遗留: 完胜/惨胜比例未 playtest)
3.9.3 收紧(晨曦反馈"数值一点用没有"): 目标 normal 随机玩家完胜 45-55%、战败<=10%, 最优>=85%;
  hard 随机完胜 25-40%、战败<=20%, 最优>=70%。参数见 COEF/TH/WAR_TH_MOD, 判定见 main() 末尾。
管线 1:1 复刻自:
  chapter5.rpy ending_iron_lord  iron_war_score 基础分 (属性 + 治理 + 盟友/战备旗标)
  chapter5.rpy 2478       战前谋略 menu   (+4/+6[+3]/+6/+8)
  chapter5.rpy 2631       前锋 menu       (+0/+3)
  chapter5.rpy 2690       弃村 menu       (+0/-3/+0)
  chapter5.rpy 决战 menu 4 档阈值 30/26/24/24 + get_war_threshold_mod()
  difficulty.rpy          阈值难度修正 normal 0 / hard +4; change_stat 双层缩放
  attr_system.rpy 214     change_stat 原始层 (0.4 增益 * 高位衰减 / 0.6 代价, wealth 0.4)
战中 crisis 掷骰 (trigger_crisis) 与 war_score 无关, 不在本模拟范围。
用法: python sim_ironline_war.py  → 控制台 + Tools/report_ironline_war.txt (UTF-8)
"""
import io
import random
import statistics
import sys

random.seed(20260711)
N = 40000

# 可调参数 (与 chapter5.rpy 铁腕会战一一对应; 由 sweep 脚本覆盖后再跑 main)
COEF = {"power": 3, "intrigue": 5, "loyalty": 6}      # (stat-30)//COEF   (3.9.3 前: 4/6/8)
TH = {"assault": 50, "flank": 46, "defend": 44, "grind": 44, "pyrrhic": 32}   # (3.9.3 前: 30/26/24/24/18)

# ────────────────────────────────────────────────────────────────
# change_stat 双层管线 (difficulty.rpy change_stat_with_difficulty
#                        → attr_system.rpy change_stat)
# ────────────────────────────────────────────────────────────────
_DIFF_MULT = {"easy": (1.5, 0.5), "normal": (1.0, 1.0), "hard": (0.7, 1.5)}
WAR_TH_MOD = {"easy": -6, "normal": 0, "hard": 3}


def change_stat(stats, name, delta, difficulty):
    pos_m, neg_m = _DIFF_MULT[difficulty]
    # 第一层: 难度倍率
    if delta > 0:
        adjusted = int(delta * pos_m)
    elif delta < 0:
        adjusted = int(delta * neg_m)
    else:
        adjusted = 0
    if adjusted == 0 and delta != 0:
        adjusted = 1 if delta > 0 else -1
    # 第一层: 递减收益 (仅正向)
    current = stats[name]
    if adjusted > 0:
        if current >= 80:
            adjusted = max(1, int(adjusted * 0.2))
        elif current >= 60:
            adjusted = max(1, int(adjusted * 0.4))
        elif current >= 40:
            adjusted = max(1, int(adjusted * 0.7))
    # 第二层: attr_system 原始 change_stat (0.4 * 高位衰减 / 0.6 代价)
    d = adjusted
    if d != 0:
        sign = 1 if d > 0 else -1
        old = current
        if d > 0:
            decay = max(0.25, 1.0 - (old / 100.0) ** 1.5)
            scaled = abs(d) * 0.4 * decay
            d = sign * (int(round(scaled)) if old >= 80 else max(1, int(round(scaled))))
        else:
            cost_scale = 0.4 if name == "wealth" else 0.6
            d = sign * max(1, int(round(abs(d) * cost_scale)))
    stats[name] = max(0, min(100, current + d))


# ────────────────────────────────────────────────────────────────
# 会战全流程 (端口 ending_iron_lord 2357-2833)
# ────────────────────────────────────────────────────────────────
def base_score(st, fl):
    s = 0
    s += max(0, st["power"] - 30) // COEF["power"]
    s += max(0, st["intrigue"] - 30) // COEF["intrigue"]
    s += max(0, st["loyalty"] - 30) // COEF["loyalty"]
    if st["wealth"] < 15:
        s -= 3
    else:
        s += max(0, st["wealth"] - 30) // 15
    if st["reputation"] < 20:
        s -= 2
    if fl["alliance_baron"]:
        s += 10
    elif fl["rel_baron_pos"]:
        s += 4
    if fl["prince_ally"]:
        s += 5
    if fl["captain60"]:
        s += 3
    if fl["pension"]:
        s += 3
    if fl["marriage"]:
        s += 5
    if fl["iron_thorn"]:
        s += 3
    s += min(6, fl["defender_bonus"] // 3)
    if fl["skirmish"] == "victory":
        s += 3
    elif fl["casualties"] >= 7:
        s -= 1
    if fl["enemy_morale_hit"]:
        s += 2
    if fl["deserter_intel"]:
        s += 2
    if fl["famine_prevented"]:
        s += 2
    if fl["granary"]:
        s += 2
    if fl["prosperous"]:
        s += 2
    if fl["north_unified"]:
        s += 6
    return s


def prep_options(st, fl):
    """战前谋略 menu: (id, war_score增量, [(stat,delta),...])"""
    opts = []
    if st["faith"] >= 60:
        opts.append(("pray", 4, [("faith", 5), ("loyalty", 3)]))
    cut = 6 + (3 if fl["intel"] else 0)
    opts.append(("cut_supply", cut, [("intrigue", 5), ("reputation", -8), ("loyalty", -4)]))
    if st["wealth"] >= 40:
        opts.append(("bribe", 6, [("wealth", -10), ("intrigue", 3), ("reputation", -5)]))
    if st["power"] >= 55:
        opts.append(("flank_prep", 8, [("power", 3), ("intrigue", 3)]))
    return opts


VANGUARD = [
    ("lead_self", 0, [("power", 5), ("reputation", 3)]),
    ("delegate_ren", 3, [("intrigue", 3), ("power", 2)]),
]


def village_options(st):
    opts = []
    if st["loyalty"] >= 70:
        opts.append(("kneel", 0, [("loyalty", 5), ("reputation", 5), ("power", -6)]))
    opts.append(("leave_guards", -3, [("loyalty", 3), ("power", -1)]))
    opts.append(("move_on", 0, [("power", 2), ("loyalty", -5)]))
    return opts


def tactic_options(st):
    """决战 menu: (id, 阈值基数). 硬拼仅当 _iron_prepared 为假."""
    opts = []
    if st["power"] >= 60:
        opts.append(("assault", TH["assault"]))
    if st["intrigue"] >= 55:
        opts.append(("flank", TH["flank"]))
    if st["intrigue"] >= 45 and st["loyalty"] >= 50:
        opts.append(("defend", TH["defend"]))
    if not opts:
        opts.append(("grind", TH["grind"]))
    return opts


def pick(policy, opts, rng):
    """policy: optimal=分数最高 / random=均匀 / rp_cost=非最优里均匀(带代价叙事向)"""
    if policy == "optimal":
        return max(opts, key=lambda o: o[1])
    if policy == "random":
        return rng.choice(opts)
    # rp_cost: 让出分数的叙事选项
    best = max(o[1] for o in opts)
    sub = [o for o in opts if o[1] < best]
    return rng.choice(sub) if sub else opts[0]


def play_war(st, fl, persona, difficulty, rng):
    """返回 (最终score, 阈值档带, 实际结局)"""
    st = dict(st)
    score = base_score(st, fl)

    # ch5:2396 兵力盘点
    if st["power"] >= 70:
        change_stat(st, "power", 3, difficulty)

    # ── 战前谋略 menu ──
    opts = prep_options(st, fl)
    if persona == "optimal":
        choice = pick("optimal", opts, rng)
    elif persona == "random":
        choice = pick("random", opts, rng)
    else:  # roleplay: 50% 叙事代价 / 50% 拿分
        choice = pick("rp_cost" if rng.random() < 0.5 else "optimal", opts, rng)
    score += choice[1]
    for s_name, d in choice[2]:
        if s_name in st:
            change_stat(st, s_name, d, difficulty)

    # ── 前锋 menu ──
    if persona == "optimal":
        choice = VANGUARD[1]                       # 让雷恩 +3
    elif persona == "random":
        choice = rng.choice(VANGUARD)
    else:
        choice = VANGUARD[0] if rng.random() < 0.5 else VANGUARD[1]  # 亲自冲锋是叙事向
    score += choice[1]
    for s_name, d in choice[2]:
        if s_name in st:
            change_stat(st, s_name, d, difficulty)

    # ── 弃村 menu ──
    opts = village_options(st)
    if persona == "optimal":
        choice = opts[-1]                          # move_on +0 且 power+2
    elif persona == "random":
        choice = rng.choice(opts)
    else:
        if rng.random() < 0.5:                     # 叙事: 下跪(若可) 否则留兵
            choice = opts[0] if opts[0][0] == "kneel" else opts[-2]
        else:
            choice = opts[-1]
    score += choice[1]
    for s_name, d in choice[2]:
        if s_name in st:
            change_stat(st, s_name, d, difficulty)

    # ── 决战 menu ──
    mod = WAR_TH_MOD[difficulty]
    topts = tactic_options(st)
    if persona == "optimal":
        tid, th = min(topts, key=lambda o: o[1])
    else:                                          # random / roleplay: 均匀选可见战术
        tid, th = rng.choice(topts)

    if tid == "assault" and fl["war_strategy"] == "attack":
        score += 2
    elif tid == "flank" and (
        fl["formation"] == "hidden_blade" or fl["war_strategy"] == "divide"
    ):
        score += 3
    elif tid == "defend" and (
        fl["formation"] in ("iron_wall", "peoples_bastion", "holy_shield")
        or fl["war_strategy"] == "defend"
    ):
        score += 3

    # 阈值档带 (以最终 score 对 4 档基准)
    if score >= TH["assault"] + mod:
        band = BANDS[0]
    elif score >= TH["flank"] + mod:
        band = BANDS[1]
    elif score >= TH["defend"] + mod:
        band = BANDS[2]
    elif score >= TH["pyrrhic"] + mod:
        band = BANDS[3]
    else:
        band = BANDS[4]

    # 实际结局
    if tid == "grind":
        outcome = "惨胜" if score >= TH["grind"] + mod else "战败"
    else:
        if score >= th + mod:
            outcome = "完胜"
        elif score >= TH["pyrrhic"] + mod:
            outcome = "惨胜"
        else:
            outcome = "战败"
    return score, band, outcome


# ────────────────────────────────────────────────────────────────
# 三种玩家画像 × 难度: 入场状态采样
# 入场门槛 (chapter5.rpy 2163-2175): normal primary=65/fallback=55;
# hard primary=72 无保底; resist 路 rel_baron>=0(normal)/>=30(hard)
# ────────────────────────────────────────────────────────────────
def coin(rng, p):
    return rng.random() < p


def sample_entry(persona, difficulty, rng):
    if persona == "optimal":
        if difficulty == "hard":
            st = {"power": rng.randint(72, 82), "intrigue": rng.randint(40, 62),
                  "loyalty": rng.randint(40, 58), "faith": rng.randint(15, 40),
                  "wealth": rng.randint(40, 68)}
            p_all, p_bar, p_pri, p_cap, p_pen, p_mar, p_int = .80, .90, .60, .70, .80, .40, .60
        else:
            st = {"power": rng.randint(72, 85), "intrigue": rng.randint(48, 70),
                  "loyalty": rng.randint(45, 65), "faith": rng.randint(20, 50),
                  "wealth": rng.randint(50, 75)}
            p_all, p_bar, p_pri, p_cap, p_pen, p_mar, p_int = .85, .90, .70, .80, .90, .50, .70
    elif persona == "roleplay":
        if difficulty == "hard":
            # 50% primary(power>=72 专精) / 50% resist 路入场(rel_baron 好, power 中低)
            if coin(rng, 0.5):
                st = {"power": rng.randint(72, 78), "intrigue": rng.randint(30, 52),
                      "loyalty": rng.randint(38, 60)}
                resist = False
            else:
                st = {"power": rng.randint(55, 70), "intrigue": rng.randint(30, 52),
                      "loyalty": rng.randint(38, 60)}
                resist = True
            st["faith"] = rng.randint(20, 50)
            st["wealth"] = rng.randint(25, 58)
            p_all, p_bar, p_pri, p_cap, p_pen, p_mar, p_int = .35, .65, .30, .45, .40, .30, .30
            if resist:
                p_bar = 1.0     # resist 入场 hard 需 rel_baron>=30
        else:
            st = {"power": rng.randint(58, 74), "intrigue": rng.randint(35, 58),
                  "loyalty": rng.randint(42, 68), "faith": rng.randint(25, 60),
                  "wealth": rng.randint(30, 65)}
            p_all, p_bar, p_pri, p_cap, p_pen, p_mar, p_int = .40, .70, .40, .50, .50, .35, .35
    else:  # random
        if difficulty == "hard":
            if coin(rng, 0.5):
                st = {"power": rng.randint(72, 80)}
            else:
                st = {"power": rng.randint(50, 70)}    # resist 入场
            st.update({"intrigue": rng.randint(28, 60), "loyalty": rng.randint(32, 60),
                       "faith": rng.randint(15, 60), "wealth": rng.randint(20, 60)})
            p_all, p_bar, p_pri, p_cap, p_pen, p_mar, p_int = .45, .50, .45, .50, .50, .30, .40
        else:
            st = {"power": rng.randint(55, 80), "intrigue": rng.randint(30, 65),
                  "loyalty": rng.randint(35, 65), "faith": rng.randint(20, 65),
                  "wealth": rng.randint(25, 70)}
            p_all, p_bar, p_pri, p_cap, p_pen, p_mar, p_int = .50, .50, .50, .50, .50, .30, .40
    st["reputation"] = rng.randint(30, 70)

    fl = {}
    fl["alliance_baron"] = coin(rng, p_all)
    fl["rel_baron_pos"] = True if fl["alliance_baron"] else coin(rng, p_bar)
    fl["prince_ally"] = coin(rng, p_pri)
    fl["captain60"] = coin(rng, p_cap)
    # 抚恤: ch5:939 需 wealth>=60 当场, 花掉 wealth (normal 实扣 -6)
    fl["pension"] = st["wealth"] >= 60 and coin(rng, p_pen)
    if fl["pension"]:
        change_stat(st, "wealth", -15, difficulty)
    fl["marriage"] = coin(rng, p_mar)
    fl["intel"] = coin(rng, p_int)
    fl["iron_thorn"] = coin(rng, 0.25)
    fl["defender_bonus"] = rng.randint(4, 22)
    fl["skirmish"] = rng.choice(("victory", "pyrrhic", "retreat"))
    fl["casualties"] = {"victory": 3, "pyrrhic": 7, "retreat": 0}[fl["skirmish"]]
    fl["enemy_morale_hit"] = fl["skirmish"] == "victory"
    fl["deserter_intel"] = fl["skirmish"] == "victory"
    fl["famine_prevented"] = coin(rng, 0.65)
    fl["granary"] = coin(rng, 0.55)
    fl["prosperous"] = coin(rng, 0.45)
    fl["north_unified"] = fl["skirmish"] == "victory" and coin(rng, 0.45)
    fl["war_strategy"] = rng.choice(("defend", "attack", "divide", "diplomacy"))
    fl["formation"] = rng.choice(("iron_wall", "hidden_blade", "holy_shield", "peoples_bastion"))
    return st, fl


# ────────────────────────────────────────────────────────────────
# 主循环 + 报告
# ────────────────────────────────────────────────────────────────
BANDS = ["强攻完胜档", "迂回档", "防守档", "惨胜档", "更差"]
OUTCOMES = ["完胜", "惨胜", "战败"]
PERSONA_NAMES = {"optimal": "最优玩家", "random": "均匀随机玩家", "roleplay": "角色扮演中间玩家"}

lines = []


def emit(s=""):
    lines.append(s)
    print(s)


def median_band(counter_scores, mod):
    m = statistics.median(counter_scores)
    if m >= TH["assault"] + mod:
        return "强攻完胜档", m
    if m >= TH["flank"] + mod:
        return "迂回档", m
    if m >= TH["defend"] + mod:
        return "防守档", m
    if m >= TH["pyrrhic"] + mod:
        return "惨胜档", m
    return "更差", m


def main():
    rng = random.Random(20260711)
    emit("=" * 78)
    emit("铁血线会战 平衡模拟  (N=%d / 画像×难度)   阈值: 强攻%d/迂回%d/防守%d/硬拼%d/惨胜线%d" % (
        N, TH["assault"], TH["flank"], TH["defend"], TH["grind"], TH["pyrrhic"]))
    emit("属性系数: (power-30)//%d  (intrigue-30)//%d  (loyalty-30)//%d   难度修正: normal +%d / hard +%d" % (
        COEF["power"], COEF["intrigue"], COEF["loyalty"], WAR_TH_MOD["normal"], WAR_TH_MOD["hard"]))
    emit("=" * 78)

    results = {}
    for difficulty in ("normal", "hard"):
        mod = WAR_TH_MOD[difficulty]
        emit("")
        emit("#### 难度 %s (阈值 %d/%d/%d/%d) ####" % (
            difficulty, TH["assault"] + mod, TH["flank"] + mod, TH["defend"] + mod, TH["grind"] + mod))
        for persona in ("optimal", "random", "roleplay"):
            band_ct = {b: 0 for b in BANDS}
            out_ct = {o: 0 for o in OUTCOMES}
            scores = []
            for _ in range(N):
                st, fl = sample_entry(persona, difficulty, rng)
                sc, band, outcome = play_war(st, fl, persona, difficulty, rng)
                band_ct[band] += 1
                out_ct[outcome] += 1
                scores.append(sc)
            scores.sort()
            p10 = scores[N // 10]
            p50 = statistics.median(scores)
            p90 = scores[N * 9 // 10]
            mb, _ = median_band(scores, mod)
            results[(difficulty, persona)] = (band_ct, out_ct, p10, p50, p90, mb)

            emit("")
            emit("-- %s --" % PERSONA_NAMES[persona])
            emit("  score p10/中位/p90 = %d / %.0f / %d    中位落档: %s" % (p10, p50, p90, mb))
            emit("  阈值档带分布: " + "  ".join(
                "%s %.1f%%" % (b, 100.0 * band_ct[b] / N) for b in BANDS))
            emit("  实际结局分布: " + "  ".join(
                "%s %.1f%%" % (o, 100.0 * out_ct[o] / N) for o in OUTCOMES))

    # ── 判定 ──
    emit("")
    emit("=" * 78)
    emit("判定检查")
    emit("=" * 78)
    checks = []
    # 3.9.3 目标: normal 随机完胜 45-55% / 战败<=10% / 最优>=85%, 扮演型完胜不低于随机-3;
    #            hard   随机完胜 25-40% / 战败<=20% / 最优>=70%
    TARGET = {"normal": (45, 55, 10, 85), "hard": (25, 40, 20, 70)}
    # 扮演型画像在 hard 的盟友先验更低(p_all .35 vs .45), 允许比随机低 8 个点; normal 允许 3 个点
    RP_TOL = {"normal": 3, "hard": 8}
    for difficulty in ("normal", "hard"):
        lo, hi, max_lose, min_opt = TARGET[difficulty]
        _, r_out, _, _, _, r_mb = results[(difficulty, "random")]
        _, p_out, _, _, _, p_mb = results[(difficulty, "roleplay")]
        _, o_out, _, _, _, _ = results[(difficulty, "optimal")]
        r_win, r_lose = 100.0 * r_out["完胜"] / N, 100.0 * r_out["战败"] / N
        p_win, p_lose = 100.0 * p_out["完胜"] / N, 100.0 * p_out["战败"] / N
        o_win = 100.0 * o_out["完胜"] / N
        ok_r = lo <= r_win <= hi and r_lose <= max_lose
        ok_p = p_win >= r_win - RP_TOL[difficulty] and p_lose <= max_lose
        ok_o = o_win >= min_opt
        checks.append(("random/" + difficulty, ok_r))
        checks.append(("roleplay/" + difficulty, ok_p))
        checks.append(("optimal/" + difficulty, ok_o))
        emit("[随机玩家/%s] 完胜%.1f%% (目标 %d-%d) 战败%.1f%% (<=%d) 中位落档=%s → %s" % (
            difficulty, r_win, lo, hi, r_lose, max_lose, r_mb, "通过" if ok_r else "不通过"))
        emit("[中间玩家/%s] 完胜%.1f%% (不低于随机-%d) 战败%.1f%% 中位落档=%s → %s" % (
            difficulty, p_win, RP_TOL[difficulty], p_lose, p_mb, "通过" if ok_p else "不通过"))
        emit("[最优玩家/%s] 完胜%.1f%% (>=%d) → %s" % (difficulty, o_win, min_opt, "通过" if ok_o else "不通过"))

    # ── 敏感性: 固定画像 × 盟友组合 (不依赖旗标先验概率), 角色扮演策略 ──
    emit("")
    emit("=" * 78)
    emit("敏感性: 固定中间画像 × 盟友组合 (roleplay 策略, N=20000/格)")
    emit("=" * 78)
    profiles = [
        ("中庸铁腕 65/45/50", {"power": 65, "intrigue": 45, "loyalty": 50, "faith": 30, "wealth": 40}),
        ("低配铁腕 60/40/45", {"power": 60, "intrigue": 40, "loyalty": 45, "faith": 30, "wealth": 30}),
        ("联姻分散 62/42/55", {"power": 62, "intrigue": 42, "loyalty": 55, "faith": 35, "wealth": 35}),
        ("resist低power 58/48/55", {"power": 58, "intrigue": 48, "loyalty": 55, "faith": 30, "wealth": 35}),
    ]
    ally_sets = [
        ("盟约+王子+雷恩+抚恤", dict(alliance_baron=True, rel_baron_pos=True, prince_ally=True,
                                     captain60=True, pension=True, marriage=False, intel=True)),
        ("男爵友好+雷恩", dict(alliance_baron=False, rel_baron_pos=True, prince_ally=False,
                               captain60=True, pension=False, marriage=False, intel=False)),
        ("仅联姻卫队", dict(alliance_baron=False, rel_baron_pos=False, prince_ally=False,
                            captain60=False, pension=False, marriage=True, intel=False)),
        ("无任何盟友/旗标", dict(alliance_baron=False, rel_baron_pos=False, prince_ally=False,
                                 captain60=False, pension=False, marriage=False, intel=False)),
    ]
    prep_defaults = dict(
        iron_thorn=False,
        defender_bonus=12,
        skirmish="pyrrhic",
        casualties=7,
        enemy_morale_hit=False,
        deserter_intel=False,
        famine_prevented=True,
        granary=False,
        prosperous=False,
        north_unified=False,
        war_strategy="defend",
        formation="iron_wall",
    )
    NS = 20000
    worst = []
    for difficulty in ("normal", "hard"):
        mod = WAR_TH_MOD[difficulty]
        emit("")
        emit("[%s] %-24s %-20s %6s %6s %6s  中位score" % (
            difficulty, "画像", "盟友组合", "完胜", "惨胜", "战败"))
        for pname, pst in profiles:
            for aname, afl in ally_sets:
                afl = {**prep_defaults, **afl}
                out_ct = {o: 0 for o in OUTCOMES}
                scs = []
                for _ in range(NS):
                    st = dict(pst)
                    st["reputation"] = 50
                    sc, band, outcome = play_war(st, dict(afl), "roleplay", difficulty, rng)
                    out_ct[outcome] += 1
                    scs.append(sc)
                med = statistics.median(scs)
                pw, pp, pl = (100.0 * out_ct[o] / NS for o in OUTCOMES)
                worst.append((difficulty, pname, aname, pw, pp, pl, med))
                emit("[%s] %-24s %-20s %5.1f%% %5.1f%% %5.1f%%  %.0f" % (
                    difficulty, pname, aname, pw, pp, pl, med))

    all_ok = all(ok for _, ok in checks)
    emit("")
    emit("总判定: " + ("fair — 阈值无需调整" if all_ok else "adjust — 见上方不通过项"))
    return all_ok


if __name__ == "__main__":
    ok = main()
    with io.open(__file__.replace("sim_ironline_war.py", "report_ironline_war.txt"),
                 "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    sys.exit(0 if ok else 1)

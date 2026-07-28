# -*- coding: utf-8 -*-
"""批31 平衡验证: ①ch2 粮仓化解饥荒 ②marriage_route 铁腕会战 +5
公式 1:1 复刻自真实链条 difficulty.rpy change_stat_with_difficulty →
_diminishing_returns → effects.rpy change_stat (2026-07-28 对齐;
旧版曾复刻 attr_system.rpy 的死代码公式, 数字全不作数)"""
import itertools

_DIFF_MULT = {
    "easy":   (1.5, 0.5),
    "normal": (1.0, 1.0),
    "hard":   (0.7, 1.5),
}

def eff(old, d, stat="x", difficulty="normal"):
    """change_stat 实际变化量(含 clamp)。逐字复刻:
    - get_difficulty_multiplier: int(d*mult) 截断; 结果为0且d≠0取±1
    - _diminishing_returns: 仅正增益, >=80:20% >=60:40% >=40:70%, 各档 max(1,int(·))
    - effects.change_stat: clamp(old+delta, 0, 100)"""
    pos, neg = _DIFF_MULT[difficulty]
    if d > 0:
        adj = int(d * pos)
    elif d < 0:
        adj = int(d * neg)
    else:
        return 0
    if adj == 0:
        adj = 1 if d > 0 else -1
    if adj > 0:
        if old >= 80:
            adj = max(1, int(adj * 0.2))
        elif old >= 60:
            adj = max(1, int(adj * 0.4))
        elif old >= 40:
            adj = max(1, int(adj * 0.7))
    return max(0, min(100, old + adj)) - old

# ---------- A. 饥荒六路对比 ----------
print("=" * 76)
print("A. ch2 饥荒各路线实际收益 (change_stat 缩放后) — 按当前属性基线 30/45/60")
print("=" * 76)
hdr = f"{'路线':<22}{'忠诚':>6}{'声望':>6}{'财富':>6}{'权力':>6}{'繁荣':>6}  备注"
for base in (30, 45, 60):
    print(f"\n--- 属性基线 {base} ---")
    print(hdr)
    rows = []
    # 粮仓路: 建造(wealth-3, prosperity+10, infra+10) + 化解(loyalty+8, rep+5, pros+5)
    rows.append(("粮仓(建+化解)", eff(base,8), eff(base,5), eff(base,-3,"wealth"), 0, 15,
                 "占用ch2建设槽(弃诊所/学堂/望楼); famine_prevented✓; +10infra"))
    # 亲自下村 (loyalty>=60): loyalty+8 rep+5 wealth-3 pros+3
    note = "需忠诚≥60" + ("(可用)" if base >= 60 else "(不可用!)")
    rows.append(("亲自下村", eff(base,8), eff(base,5), eff(base,-3,"wealth"), 0, 3, note+"; 无famine_prevented"))
    # 购买: wealth-10(普通高繁荣)/-20(低繁荣) + pros+10 loyalty+5 ; end +2 wealth
    for cost_w, tag in ((-10, "高繁荣"), (-20, "低繁荣")):
        rows.append((f"购买粮食({tag})", eff(base,5), 0, eff(base,cost_w,"wealth")+eff(base,2,"wealth"), 0, 10, "famine_prevented✓"))
    rows.append(("严格配给", eff(base,-10), 0, 0, 0, -5, "famine_prevented✓"))
    rows.append(("开放城堡粮库", eff(base,15), eff(base,10), 0, eff(base,-5), 10, "famine_prevented✓"))
    rows.append(("劫男爵运粮队", 0, eff(base,-5), 0, eff(base,10), 15, "rel_baron-25; famine_prevented✓"))
    for name, lo, re, we, po, pr, note in rows:
        print(f"{name:<22}{lo:>+6}{re:>+6}{we:>+6}{po:>+6}{pr:>+6}  {note}")

# ---------- B. 铁腕会战 ----------
print()
print("=" * 76)
print("B. iron_war_score 分布: marriage_route +5 对首回合 完胜/惨胜 的影响")
print("=" * 76)

def base_score(power, intrigue, loyalty, baron, prince, captain60, pension, marriage):
    s = max(0, power-30)//4 + max(0, intrigue-30)//6 + max(0, loyalty-30)//8
    if baron == "alliance": s += 10
    elif baron == "friendly": s += 4
    if prince: s += 5
    if captain60: s += 3
    if pension: s += 3
    if marriage: s += 5
    # iron_thorn_controlled (总部可选化·接管线) 未纳入形参: 该线玩家极少数,
    # 网格里按无此加成保守估计; 需要时手动 +3
    return s

def best_prep(power, intrigue, loyalty, faith, wealth, baron_supply_intel=False):
    """战前准备菜单取玩家可选最优"""
    opts = []
    if faith >= 60: opts.append(4)
    opts.append(6 + (3 if baron_supply_intel else 0))   # 截断补给 无门槛
    if wealth >= 40: opts.append(6)
    if power >= 55: opts.append(8)
    return max(opts)

def best_tactic_threshold(power, intrigue, loyalty):
    """总攻菜单: 玩家可选项里阈值最低的 (最优策略)"""
    ths = []
    if power >= 60: ths.append(20)
    if intrigue >= 55: ths.append(16)
    if intrigue >= 45 and loyalty >= 50: ths.append(14)
    return min(ths) if ths else 12   # 只剩硬拼(12, 且成功也是惨胜)

def outcome(power, intrigue, loyalty, faith, wealth, baron, prince, captain60, pension, marriage,
            vanguard_ren=True, village_guard=False):
    s = base_score(power, intrigue, loyalty, baron, prince, captain60, pension, marriage)
    s += best_prep(power, intrigue, loyalty, faith, wealth)
    if vanguard_ren: s += 3
    if village_guard: s -= 3
    th = best_tactic_threshold(power, intrigue, loyalty)
    if th == 12:
        return "战败" if s < 12 else "惨胜(硬拼)"
    return "完胜" if s >= th else "惨胜"

profiles = [
    # (名字, power, intrigue, loyalty, faith, wealth)
    ("满配老玩家",    80, 65, 60, 40, 60),
    ("标准铁腕(专精)", 72, 50, 50, 30, 45),
    ("中庸铁腕",      65, 45, 50, 30, 40),
    ("低配铁腕",      60, 40, 45, 30, 30),
    ("勉强够门槛",    58, 35, 40, 25, 25),
    ("联姻分散型",    62, 42, 55, 30, 35),   # 走联姻的玩家通常点了社交/忠诚
]
ally_sets = [
    ("男爵盟约+王子+雷恩+抚恤", "alliance", True, True, True),
    ("男爵友好+雷恩",          "friendly", False, True, False),
    ("男爵友好+抚恤",          "friendly", False, False, True),
    ("无盟友",                 "none", False, False, False),
]
print(f"\n{'玩家画像':<14}{'盟友组合':<24}{'无联姻':<12}{'有联姻':<12} 分数(无/有)")
flips = 0; total = 0
for (pname, p, i, l, f, w) in profiles:
    for (aname, baron, prince, cap, pen) in ally_sets:
        o0 = outcome(p, i, l, f, w, baron, prince, cap, pen, False)
        o1 = outcome(p, i, l, f, w, baron, prince, cap, pen, True)
        s0 = base_score(p,i,l,baron,prince,cap,pen,False) + best_prep(p,i,l,f,w) + 3
        s1 = s0 + 5
        total += 1
        mark = ""
        if o0 != o1: flips += 1; mark = "  ← 翻转"
        print(f"{pname:<14}{aname:<24}{o0:<12}{o1:<12} {s0}/{s1}{mark}")
print(f"\n翻转率: {flips}/{total}")

# 全网格扫描: 铁腕路线可达画像空间里 完胜率 变化
grid_p = range(58, 82, 2); grid_i = range(30, 70, 4); grid_l = range(35, 65, 4)
def rate(marriage, baron, prince, cap, pen):
    win = n = 0
    for p, i, l in itertools.product(grid_p, grid_i, grid_l):
        n += 1
        if outcome(p, i, l, 30, 40, baron, prince, cap, pen, marriage) == "完胜":
            win += 1
    return win / n
print("\n全网格完胜率 (power 58-80 × intrigue 30-66 × loyalty 35-61, 最优策略):")
for (aname, baron, prince, cap, pen) in ally_sets:
    r0, r1 = rate(False, baron, prince, cap, pen), rate(True, baron, prince, cap, pen)
    print(f"  {aname:<24} 无联姻 {r0:5.1%} → 有联姻 {r1:5.1%}  (Δ {r1-r0:+.1%})")

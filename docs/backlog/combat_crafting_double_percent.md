# Backlog: combat.rpy + crafting.rpy 双百分号显示 bug

> **来源**: 修栀子 T+8 反馈 bug 6 (crisis 检定面板 "成功率 90%%" 双百分号) 时, grep 全项目发现同类 bug 还在 combat / crafting 两文件未修
> **优先级**: 中 — 玩家可见但栀子未明确反馈, 战斗 / 制作系统每场战斗都看得到
> **状态**: 待修 (留下次单独 commit)

---

## 背景

Ren'Py 的 `[var]` substitution **不走** Python `%` formatting,所以 `text "[var]%%"` 写法里 `%%` 不会被转义成 `%`,字面渲染成 `90%%`。crisis.rpy 已修 (3 处),combat / crafting 两文件还有同类问题。

### 两类 `%%` 用法区分

**类别 A: Python `%` formatting 上下文 (合法 — 不要动)**
```python
add_combat_log("...(成功率 %d%%)" % chance)   # ← 右边有 % chance, %% 被 Python 转义成 %
text "%d%%" % stat                            # ← 同上
```

**类别 B: Ren'Py `[var]` substitution + `%%` (跟 crisis 同 bug)**
```python
text "[var]%%"                  # ← 没 % chance, [var] 是 Ren'Py 替换, %% 字面输出
add_combat_log("...30%%伤害")    # ← 字符串拼接, 没参数化, %% 字面输出
```

---

## 待修位置清单 (12 处)

### combat.rpy

| 行号 | 当前代码 | 修复 | 玩家可见性 |
|---|---|---|---|
| 1425 | `text "闪[combat_player_dodge]%%"` | `text "闪[combat_player_dodge]%"` | 战斗 UI 闪避数值, 每场战斗 |
| 1426 | `text "暴[combat_player_crit]%%"` | `text "暴[combat_player_crit]%"` | 战斗 UI 暴击数值, 每场战斗 |
| 1615 | `text "成功率[_retreat_pct]%%"` | `text "成功率[_retreat_pct]%"` | 撤退按钮提示 |
| 1656 | `text "1.5x伤 -15%%命中"` | `text "1.5x伤 -15%命中"` | 重击姿态切换提示 |
| 1672 | `text "2.0x伤 -25%%命中"` | `text "2.0x伤 -25%命中"` | 致命一击姿态切换提示 |
| 1704 | `text "0.75x伤 +10%%命中"` | `text "0.75x伤 +10%命中"` | 速攻姿态切换提示 |
| 1886 | `text "[..]/[..] ([_hp_remain_pct]%%)"` | `text "[..]/[..] ([_hp_remain_pct]%)"` | 玩家 HP 百分比, 每回合显示 |
| 2066 | `add_combat_log("切换至【攻势】: +20%%伤害, -10闪避")` | `add_combat_log("切换至【攻势】: +20%伤害, -10闪避")` | 切换姿态 log |
| 2069 | `add_combat_log("切换至【守势】: +15闪避, -20%%伤害, 可反击")` | `add_combat_log("切换至【守势】: +15闪避, -20%伤害, 可反击")` | 切换姿态 log |

### crafting.rpy

| 行号 | 当前代码 | 修复 | 玩家可见性 |
|---|---|---|---|
| 385 | `text "成功率 [_r_rate]%%"` | `text "成功率 [_r_rate]%"` | 制作配方列表的成功率 |
| 503 | `text "[_sel_rate]%%"` | `text "[_sel_rate]%"` | 选中配方的成功率 |
| 527 | `text "技能 > 30 时有 10%% 概率暴击..."` | `text "技能 > 30 时有 10% 概率暴击..."` | 制作 UI 帮助文字 |

---

## 不要动的合法用法 (类别 A, 共 7 处)

```
combat.rpy:675   add_combat_log("...(%d%%)" % (...))          ✓ Python %
combat.rpy:843   add_combat_log("...(成功率 %d%%)" % chance)  ✓ Python %
combat.rpy:846   add_combat_log("...(成功率 %d%%)" % chance)  ✓ Python %
combat.rpy:979   add_combat_log("...(%d%%)" % (...))          ✓ Python %
combat.rpy:2292  text "闪: %d%%" % _prev_enemy.get(...)       ✓ Python %
combat.rpy:2309  text "闪: %d%%" % _prev_stats["dodge"]       ✓ Python %
combat.rpy:2310  text "暴: %d%%" % _prev_stats["crit"]        ✓ Python %
```

这 7 处右侧都有 `% (...)` Python 格式化, `%%` 是 Python 转义的合法用法,**勿动**。

---

## 修复方案

每处单字符替换 `%%` → `%`, 共 12 处。无逻辑改动,无 lint 风险。

## 验证方式

修后跑:
```bash
grep -nE 'text "\[[^\]]+\]%%"' game/*.rpy        # 期望: 0 命中 (类别 B 类型 1)
grep -nE 'add_combat_log\("[^"]*%%' game/*.rpy   # 期望: 仅类别 A 命中 (右边有 %)
```

Ren'Py 跑游戏检查:
- 战斗 UI 闪避 / 暴击 / HP 百分比 显示 `30%` 而非 `30%%`
- 撤退按钮成功率显示正常
- 制作 UI 成功率显示正常

## 优先级理由

- **可见性高**: 战斗系统每场战斗每回合都显示, HP / 闪避 / 暴击 都有
- **数量小**: 12 处单字符替换, 半小时改完
- **无栀子明确反馈**: 但栀子那条"成功率 90%%"截图证明问题真实存在, 玩家迟早会再报
- **建议下次单独 commit**: tag `v3.x-combat-crafting-double-percent-fix` 或类似

---

## 历史

- 2026-04-25: 修 crisis.rpy 3 处 (栀子 T+8 commit 1) 时 grep 发现, 列入 backlog

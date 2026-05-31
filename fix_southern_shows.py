# -*- coding: utf-8 -*-
"""
安全补全南境 DLC 缺失的说话人 show 立绘。
复用 fix_missing_portraits.py 的缺失定位(active 追踪 + menu 分支 indent-aware),
插入 `$ hide_all_chars(自己[, 对峙搭档]) + show 自己 at 站位`:
  - 普通角色独占(hide 其他, 避免同 side 叠加)
  - guild_master(维斯帕) 与 corsair(赛琳) 互为对峙搭档, 互相保留 → 双人同屏不被拆

  python fix_southern_shows.py           # dry-run
  python fix_southern_shows.py --apply
"""
import os, sys
import fix_missing_portraits as F

TARGET = os.path.join(os.path.dirname(__file__), "game", "southern_expansion.rpy")

SIDE = {
    "player_char_img": "left", "player_young_img": "left",
    "player_teen_img": "left", "player_child_img": "left",
    "aldric_img": "left", "guild_master_img": "left",
    "corsair_img": "right", "ship_boy_img": "right", "dockhand_img": "right",
}
## 对峙搭档: show 时一并保留, 不 hide
KEEP = {
    "guild_master_img": ["corsair_img"],
    "corsair_img": ["guild_master_img"],
}

def main(apply):
    char_map = F.collect_character_defs()
    insertions, lines = F.plan_insertions(TARGET, char_map)
    insertions.sort(key=lambda x: x[0])

    print(f"将插入 {len(insertions)} 处:")
    for line_idx, indent, tag in insertions:
        side = SIDE.get(tag, "right")
        keeps = [tag] + KEEP.get(tag, [])
        ctx = lines[line_idx].strip()[:34] if line_idx < len(lines) else ""
        print(f"  L{line_idx+1:<5} keep[{'+'.join(keeps)}] show {tag} at {side}")

    if not apply:
        print("\n(dry-run; 加 --apply 写入)")
        return

    for line_idx, indent, tag in sorted(insertions, reverse=True):
        side = SIDE.get(tag, "right")
        keeps = [tag] + KEEP.get(tag, [])
        args = ", ".join('"%s"' % k for k in keeps)
        block = [
            f'{indent}$ hide_all_chars({args})\n',
            f'{indent}show {tag} at {side} with dissolve\n',
        ]
        lines[line_idx:line_idx] = block
    with open(TARGET, "w", encoding="utf-8", newline="\n") as f:
        f.writelines(lines)
    print(f"\n[已写入] {len(insertions)} 处")

if __name__ == "__main__":
    main("--apply" in sys.argv)

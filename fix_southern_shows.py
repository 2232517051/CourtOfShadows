# -*- coding: utf-8 -*-
"""
安全补全南境 DLC 缺失的说话人 show 立绘（side-aware 版）。
复用 fix_missing_portraits.py 的缺失定位（active 追踪 + menu 分支 indent-aware），
插入时按角色固定站位 show，并 hide 同侧其他立绘、保留对侧全部 —— 不破坏双人同屏，
也不会出现 player 说话清掉同屏 NPC 的问题。
  LEFT  = 主角/管家/维斯帕（左侧轮流位）
  RIGHT = 其余配角（右侧对话方，默认）
用法:
  python fix_southern_shows.py          # dry-run
  python fix_southern_shows.py --apply
"""
import os, sys
import fix_missing_portraits as F

TARGET = os.path.join(os.path.dirname(__file__), "game", "southern_expansion.rpy")

LEFT_TAGS = ["player_char_img", "player_young_img", "player_teen_img",
             "player_child_img", "aldric_img", "guild_master_img",
             "old_salt_img", "sea_dog_img", "chen_captain_img", "blacksmith_wife_img"]
# 只保留真正固定在右侧的主要对话角色；通用立绘(soldier_generic 等)不保留，
# 因为它们在不同场景可能 show 在左侧，保留会和左侧主角叠加。
RIGHT_TAGS = ["corsair_img", "ship_boy_img", "dockhand_img",
              "harbor_master_img", "tavern_keeper_img", "royal_admiral_img"]

def side_of(tag):
    return "left" if tag in LEFT_TAGS else "right"

def keep_for(tag):
    # 保留自己 + 对侧全部（hide 同侧其他，避免叠加；护双人同屏）
    if side_of(tag) == "left":
        return [tag] + RIGHT_TAGS
    return [tag] + LEFT_TAGS

def main(apply):
    char_map = F.collect_character_defs()
    insertions, lines = F.plan_insertions(TARGET, char_map)
    insertions.sort(key=lambda x: x[0])
    print(f"将插入 {len(insertions)} 处:")
    for line_idx, indent, tag in insertions:
        print(f"  L{line_idx+1:<5} show {tag} at {side_of(tag)}")
    if not apply:
        print("\n(dry-run; --apply 写入)")
        return
    for line_idx, indent, tag in sorted(insertions, reverse=True):
        side = side_of(tag)
        args = ", ".join('"%s"' % k for k in keep_for(tag))
        block = [f'{indent}$ hide_all_chars({args})\n',
                 f'{indent}show {tag} at {side} with dissolve\n']
        lines[line_idx:line_idx] = block
    with open(TARGET, "w", encoding="utf-8", newline="\n") as f:
        f.writelines(lines)
    print(f"\n[已写入] {len(insertions)} 处")

if __name__ == "__main__":
    main("--apply" in sys.argv)

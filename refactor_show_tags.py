"""
把拆分后用过的 servant_generic_img / healer_img 改为新专属 tag。
按文件 + 行号区间精确替换。
"""
import re
from pathlib import Path

GAME = Path("game")

# (file, line_range, old_tag, new_tag)
# 仅替换 servant_generic_img / healer_img 为新 tag；
# 其他保留（保留身份用 servant_generic 的角色）
REPLACEMENTS = [
    # chapter3.rpy - lily_root L1623-1634
    ("chapter3.rpy", (1623, 1635), "servant_generic_img", "lily_root_img"),
    # chapter4.rpy - beggar L283-292
    ("chapter4.rpy", (283, 295), "servant_generic_img", "beggar_img"),
    # chapter4.rpy - court_herald L986-997
    ("chapter4.rpy", (986, 1000), "servant_generic_img", "court_herald_img"),
    # script.rpy - stable_boy L215-226
    ("script.rpy", (215, 230), "servant_generic_img", "stable_boy_img"),
    # chapter3_expansion.rpy - herbalist_vera 全文件 (healer_img -> herbalist_vera_img)
    ("chapter3_expansion.rpy", None, "healer_img", "herbalist_vera_img"),
]


def apply_range(fname, range_or_none, old, new):
    p = GAME / fname
    lines = p.read_text(encoding="utf-8").splitlines(keepends=True)
    changed = 0
    if range_or_none is None:
        # 全文件替换
        for i, line in enumerate(lines):
            if old in line:
                lines[i] = line.replace(old, new)
                changed += 1
    else:
        lo, hi = range_or_none
        for i in range(lo - 1, min(hi, len(lines))):
            if old in lines[i]:
                lines[i] = lines[i].replace(old, new)
                changed += 1
    p.write_text("".join(lines), encoding="utf-8")
    rng = "all" if range_or_none is None else f"L{range_or_none[0]}-{range_or_none[1]}"
    print(f"{fname} {rng}: {old} -> {new}  {changed} replaced")


for rep in REPLACEMENTS:
    apply_range(*rep)

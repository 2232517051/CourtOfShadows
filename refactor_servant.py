"""
将被 servant Character 共用的多个 NPC 拆成独立身份。
按行号精确替换 speaker（和必要的 show 指令）。
"""
import re
from pathlib import Path

GAME = Path("game")

# 每项: (文件, 要替换的行号列表, old_speaker, new_speaker)
# 行号基于当前状态 (截图前用户报告问题时的状态)
SPEAKER_REPLACEMENTS = [
    # chapter1_expansion.rpy - 账房
    ("chapter1_expansion.rpy", [783, 785, 787], "servant", "accountant"),
    # chapter2.rpy - 车夫 / 司仪 / 王后特使
    ("chapter2.rpy", [482, 484], "servant", "caravan_hand"),
    ("chapter2.rpy", [1664, 1666], "servant", "herald"),
    ("chapter2.rpy", [1738, 1740], "servant", "queen_envoy"),
    # chapter3.rpy - 药店伙计/暗百合审问者/联络人根/信使
    ("chapter3.rpy", [1198, 1576], "servant", "apothecary"),
    ("chapter3.rpy", [1279, 1289, 1301, 1311, 1315, 1378, 1419, 1456, 1492, 1494],
     "servant", "lily_interviewer"),
    ("chapter3.rpy", [1625, 1635, 1639, 1641, 1643, 1645], "servant", "lily_root"),
    ("chapter3.rpy", [4465], "servant", "messenger"),
    # chapter3_expansion.rpy - 草药师薇拉
    ("chapter3_expansion.rpy", [649, 655, 673, 683, 687, 697, 804],
     "servant", "herbalist_vera"),
    # chapter4.rpy - 乞丐 / 王都司礼官
    ("chapter4.rpy", [285], "servant", "beggar"),
    ("chapter4.rpy", [988], "servant", "court_herald"),
    # script.rpy - 马厩学徒汤米
    ("script.rpy", [217], "servant", "stable_boy"),
]

# 整文件全替换 (薇拉场景独占 chapter3_expansion.rpy 的 servant_generic_img)
FULL_FILE_REPLACEMENTS = [
    ("chapter3_expansion.rpy", "servant_generic_img", "healer_img"),
]


def apply_speaker(fname, lines_1based, old, new):
    p = GAME / fname
    lines = p.read_text(encoding="utf-8").splitlines(keepends=True)
    changed = 0
    for ln in lines_1based:
        idx = ln - 1
        if idx < 0 or idx >= len(lines):
            print(f"  {fname}:L{ln} out of range")
            continue
        orig = lines[idx]
        # 只替换行首第一个出现的 old 单词（讲者 id 后跟空白+引号）
        new_line = re.sub(
            rf'^(\s*){re.escape(old)}(\s+")',
            rf'\1{new}\2',
            orig, count=1,
        )
        if new_line == orig:
            print(f"  {fname}:L{ln} NO MATCH  {orig[:60]!r}")
            continue
        lines[idx] = new_line
        changed += 1
    p.write_text("".join(lines), encoding="utf-8")
    print(f"{fname}: {old} -> {new}  {changed}/{len(lines_1based)} replaced")


def apply_full_file(fname, old, new):
    p = GAME / fname
    text = p.read_text(encoding="utf-8")
    count = text.count(old)
    text = text.replace(old, new)
    p.write_text(text, encoding="utf-8")
    print(f"{fname}: {old} -> {new}  {count} occurrences")


def main():
    print("=== Speaker replacements ===")
    for rep in SPEAKER_REPLACEMENTS:
        apply_speaker(*rep)
    print("\n=== Full-file replacements ===")
    for rep in FULL_FILE_REPLACEMENTS:
        apply_full_file(*rep)


if __name__ == "__main__":
    main()

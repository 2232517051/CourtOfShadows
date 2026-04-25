"""
第二轮 refactor —— 补齐上次漏掉的 servant 延续行。
按行号范围组合精确替换。
"""
import re
from pathlib import Path

GAME = Path("game")

# (文件, 行号列表, new_speaker)
SPEAKER_REPLACEMENTS = [
    # chapter2.rpy - 车夫感谢延续 (L502, L510)
    ("chapter2.rpy", [502, 510], "caravan_hand"),
    # chapter2.rpy - 图书馆老学者 (L649, L657-L659)
    ("chapter2.rpy", [649, 657, 658, 659], "scholar"),
    # chapter2.rpy - 北方难民 (L677, L685, L686, L695)
    ("chapter2.rpy", [677, 685, 686, 695], "refugee"),
    # chapter3.rpy - 男爵使者 (L579) 复用 messenger
    ("chapter3.rpy", [579], "messenger"),
    # chapter3.rpy - 药店伙计初接触 (L1210, L1219, L1232, L1243, L1254)
    ("chapter3.rpy", [1210, 1219, 1232, 1243, 1254], "apothecary"),
    # chapter3.rpy - 暗百合审问者 "桥" (L1326-L1490)
    ("chapter3.rpy",
     [1326, 1328, 1342, 1350, 1364, 1373, 1374, 1389, 1399, 1407, 1417,
      1431, 1442, 1454, 1468, 1479, 1490],
     "lily_interviewer"),
    # chapter3.rpy - 药店密道入口接触 (L1590-L1616)
    ("chapter3.rpy", [1590, 1599, 1607, 1616], "apothecary"),
    # chapter1_expansion.rpy - 登记员 (L903) 复用 accountant
    ("chapter1_expansion.rpy", [903], "accountant"),
    # chapter1_expansion.rpy - 斥候 (L746) 新 scout
    ("chapter1_expansion.rpy", [746], "scout"),
    # chapter1_expansion.rpy - 顾问 (L832) 复用 accountant (都是财务相关)
    ("chapter1_expansion.rpy", [832], "accountant"),
]

# chapter3_expansion.rpy 薇拉场景内所有 speaker "servant" 全替换为 herbalist_vera
VERA_LINES_CHAP3EXP = [
    715, 719, 729, 750, 754, 772, 774, 776, 778, 790, 815, 819,
]
SPEAKER_REPLACEMENTS.append(
    ("chapter3_expansion.rpy", VERA_LINES_CHAP3EXP, "herbalist_vera")
)


def apply_speaker(fname, lines_1based, new, old="servant"):
    p = GAME / fname
    lines = p.read_text(encoding="utf-8").splitlines(keepends=True)
    changed = 0
    for ln in lines_1based:
        idx = ln - 1
        if idx < 0 or idx >= len(lines):
            print(f"  {fname}:L{ln} OUT OF RANGE")
            continue
        orig = lines[idx]
        new_line = re.sub(
            rf'^(\s*){re.escape(old)}(\s+")',
            rf'\1{new}\2',
            orig, count=1,
        )
        if new_line == orig:
            print(f"  {fname}:L{ln} NO MATCH  {orig[:80]!r}")
            continue
        lines[idx] = new_line
        changed += 1
    p.write_text("".join(lines), encoding="utf-8")
    print(f"{fname}: -> {new}  {changed}/{len(lines_1based)}")


for rep in SPEAKER_REPLACEMENTS:
    apply_speaker(*rep)

"""
批量在连续旁白块 (>=2 行) 前插入 $ hide_all_chars()。

使用 scan_narration_overlap.py 的逻辑找出位置，按反向行号插入保留行号有效。
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from scan_narration_overlap import scan_file, GAME_DIR


def apply_fix(fname):
    path = os.path.join(GAME_DIR, fname)
    if not os.path.isfile(path):
        print(f"[skip] not found: {path}")
        return 0

    sugs = scan_file(path)
    if not sugs:
        print(f"{fname}: 0 处需修复")
        return 0

    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # 反向插入保留行号
    for s in sorted(sugs, key=lambda x: -x["line"]):
        line_idx = s["line"] - 1  # 0-indexed 插入位置
        indent = s["indent"]
        new_line = f"{indent}$ hide_all_chars()\n"
        lines.insert(line_idx, new_line)

    with open(path, "w", encoding="utf-8") as f:
        f.writelines(lines)

    print(f"{fname}: 插入 {len(sugs)} 处")
    return len(sugs)


def main():
    files = sys.argv[1:] if len(sys.argv) > 1 else ["chapter2.rpy", "chapter2_expansion.rpy"]
    total = 0
    for f in files:
        total += apply_fix(f)
    print(f"\nTOTAL: {total} 处已插入")


if __name__ == "__main__":
    main()

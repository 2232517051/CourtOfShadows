"""
一键字体子集化 — 每次改完剧本打包前必跑一次。

工作流:
1. 递归扫描 game/ 下所有 .rpy/.rpym/.py/.txt/.json 的每一个字符
2. 叠加 ASCII printable + CJK 标点 (U+3000-303F) + 全角 (U+FF00-FFEF) 兜底
3. 从 C:\Windows\Fonts\msyh.ttc[0] (全量 29905 字形) 子集化
4. 覆盖写入 game/msyh.ttf
5. 二次验证 — 若仍有非符号缺字，非零退出

用法: python subset_font.py
"""
import glob
import os
import sys
import io

# Windows 中文 stdout
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from fontTools.ttLib import TTFont, TTCollection
from fontTools.subset import Subsetter

# ──────────────────────────────────────────────
# 配置
# ──────────────────────────────────────────────
GAME_DIR = "game"
OUTPUT_FONT = "game/msyh.ttf"
SOURCE_TTC = r"C:\Windows\Fonts\msyh.ttc"
SOURCE_TTC_INDEX = 0          # msyh 常规体

# 扫描模式
SCAN_PATTERNS = [
    f"{GAME_DIR}/**/*.rpy",
    f"{GAME_DIR}/**/*.rpym",
    f"{GAME_DIR}/**/*.py",
    f"{GAME_DIR}/**/*.txt",
    f"{GAME_DIR}/**/*.json",
]

# 字体本身不含的装饰符号 — 不算"缺字"
KNOWN_UNAVAILABLE = {0x2591, 0x25B6, 0x2715}   # ░ ▶ ✕


def collect_used_chars():
    used = set()
    n_files = 0
    for pat in SCAN_PATTERNS:
        for path in glob.glob(pat, recursive=True):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    used.update(f.read())
                n_files += 1
            except Exception as e:
                print(f"[!] 跳过 {path}: {e}")
    print(f"[*] 扫描 {n_files} 个文件, 唯一字符 {len(used)}")
    return used


def build_codepoint_set(used):
    cps = {ord(c) for c in used if ord(c) > 0}
    # ASCII printable
    for cp in range(0x20, 0x7F):
        cps.add(cp)
    # CJK 标点
    for cp in range(0x3000, 0x3040):
        cps.add(cp)
    # 全角符号/ASCII 全角
    for cp in range(0xFF00, 0xFFF0):
        cps.add(cp)
    return cps


def subset(codepoints):
    print(f"[*] 从 {SOURCE_TTC} (font {SOURCE_TTC_INDEX}) 子集化")
    tc = TTCollection(SOURCE_TTC)
    src = tc.fonts[SOURCE_TTC_INDEX]
    print(f"    源字形数: {len(src.getBestCmap())}")

    subsetter = Subsetter()
    subsetter.populate(unicodes=sorted(codepoints))
    subsetter.subset(src)
    src.flavor = None
    src.save(OUTPUT_FONT)
    print(f"[OK] 输出: {OUTPUT_FONT} ({os.path.getsize(OUTPUT_FONT)/1024:.1f} KB)")


def verify(used):
    font = TTFont(OUTPUT_FONT)
    cmap = font.getBestCmap()
    missing = sorted(
        c for c in used
        if ord(c) not in cmap
        and ord(c) not in KNOWN_UNAVAILABLE
        and c.isprintable()
        and not c.isspace()
    )
    print(f"[*] 验证: 字体 {len(cmap)} 字形, 缺字 {len(missing)}")
    if missing:
        print("[X] 以下字符仍缺失:")
        for c in missing:
            print(f"    {c}  U+{ord(c):04X}")
        return False
    print("[OK] 全部字符已覆盖 (已排除已知不可得符号 ░▶✕)")
    return True


def main():
    if not os.path.exists(SOURCE_TTC):
        print(f"[X] 找不到源字体 {SOURCE_TTC}")
        print("    在 Mac/Linux 上请改 SOURCE_TTC 指向系统里任一全量中文字体")
        sys.exit(2)

    used = collect_used_chars()
    cps = build_codepoint_set(used)
    print(f"[*] 目标 codepoints: {len(cps)}")

    subset(cps)
    ok = verify(used)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()

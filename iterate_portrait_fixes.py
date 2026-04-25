"""
全文件立绘修复迭代工具 —— 对所有 .rpy 跑
- scan_narration_overlap + fix_narration_overlap
- scan_missing_portraits + fix_missing_portraits
来回迭代到两者都归零。
"""
import os
import sys
import subprocess

BASE = os.path.dirname(os.path.abspath(__file__))
GAME_DIR = os.path.join(BASE, "game")

# 排除的框架文件（不含叙事剧本逻辑）
EXCLUDE = {
    "attr_system.rpy", "audio_config.rpy", "audio_safe.rpy", "balance.rpy",
    "changelog.rpy", "char_helpers.rpy", "characters.rpy",
    "companions.rpy", "courage.rpy", "crafting.rpy", "difficulty.rpy",
    "effects.rpy", "extras.rpy", "gallery.rpy", "gui.rpy",
    "images_def.rpy", "inventory.rpy", "options.rpy", "save_compat.rpy",
    "screens.rpy", "screens_custom.rpy", "test_game.rpy",
    "voice_config.rpy", "weather.rpy",
}


def list_narrative_files():
    return sorted(
        f for f in os.listdir(GAME_DIR)
        if f.endswith(".rpy") and f not in EXCLUDE
    )


def run_scan(script, files):
    """返回总 finding 数（解析 stdout）"""
    cmd = [sys.executable, os.path.join(BASE, script)] + files
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    out = r.stdout + r.stderr
    # scan_narration_overlap: "TOTAL: N"
    # scan_missing_portraits: "Total findings: N"
    import re
    m = re.search(r"TOTAL:\s*(\d+)", out)
    if m:
        return int(m.group(1))
    m = re.search(r"Total findings:\s*(\d+)", out)
    if m:
        return int(m.group(1))
    return -1


def run_fix(script, files):
    cmd = [sys.executable, os.path.join(BASE, script)] + files
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    # 不回传输出，避免 Windows console GBK 编码问题
    return r.returncode


def main():
    files = list_narrative_files()
    print(f"[init] 叙事文件 {len(files)} 个")
    for f in files:
        print(f"   - {f}")
    print()

    MAX_ITER = 40
    for i in range(1, MAX_ITER + 1):
        print(f"=== iteration {i} ===")
        nov = run_scan("scan_narration_overlap.py", files)
        # scan_missing_portraits.py 不支持多文件参数，用默认全扫游戏目录
        miss = run_scan("scan_missing_portraits.py", [])
        print(f"  narration_overlap: {nov}   missing_portraits: {miss}")
        if nov == 0 and miss == 0:
            print(f"\n两项归零，完成（迭代 {i} 轮）")
            return

        if nov > 0:
            print(f"  -> fix_narration_overlap ({nov} findings)")
            run_fix("fix_narration_overlap.py", files)
        if miss > 0:
            print(f"  -> fix_missing_portraits ({miss} findings)")
            run_fix("fix_missing_portraits.py", [])

    print(f"\n达到最大迭代 ({MAX_ITER})，最终状态未归零")


if __name__ == "__main__":
    main()

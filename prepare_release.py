"""
发布前必跑 — 确保 game/msyh.ttf 和当前 .rpy 内容字符集一致。

用法 (任何 build/wx 打包之前):
  python prepare_release.py

退出码:
  0 = 字体已最新, 可以 build
  1 = 字体有更新, 已重新生成, 请重新发起 build
  2 = subset_font.py 失败

为什么需要这一步:
  pre-commit hook 只在 commit 时刷字体. 但如果 build 流程是从 working
  tree 直接打包 (例如 wx 第三方工具), 而最近一次没有触发 commit, 字体
  可能不是最新. 玩家就会看到方框/缺字 (栀子 2026-05-01 反馈正是此因).
"""
import shutil
import subprocess
import sys
from pathlib import Path

from fontTools.ttLib import TTFont

FONT = Path("game/msyh.ttf")


def cmap_set(p: Path) -> frozenset:
    return frozenset(TTFont(str(p)).getBestCmap().keys())


def main() -> int:
    if not FONT.exists():
        print(f"[X] {FONT} 不存在")
        return 2

    backup = FONT.with_suffix(".ttf.prerelease_check")
    shutil.copy2(FONT, backup)
    before_chars = cmap_set(backup)

    try:
        rc = subprocess.call([sys.executable, "subset_font.py"])
        if rc != 0:
            print(f"[X] subset_font.py 失败 (exit {rc})")
            shutil.copy2(backup, FONT)
            return 2

        after_chars = cmap_set(FONT)
        added = after_chars - before_chars
        removed = before_chars - after_chars

        if not added and not removed:
            # 字符集相同; 二进制可能因 fontTools 非确定性微差异, 回滚到 backup 保持 git clean
            shutil.copy2(backup, FONT)
            print(f"[OK] 字体已最新 ({len(after_chars)} 字符), 可以 build")
            return 0
        else:
            if added:
                sample = ''.join(chr(c) for c in sorted(added)[:20])
                print(f"[!] 字体新增 {len(added)} 字符 (前20: {sample})")
            if removed:
                sample = ''.join(chr(c) for c in sorted(removed)[:20])
                print(f"[!] 字体移除 {len(removed)} 字符 (前20: {sample})")
            print("    .rpy 引入新字, 已自动重生成 game/msyh.ttf")
            print("    请 commit 后重新 build")
            return 1
    finally:
        backup.unlink(missing_ok=True)


if __name__ == "__main__":
    sys.exit(main())

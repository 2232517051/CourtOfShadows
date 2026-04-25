# -*- coding: utf-8 -*-
"""扫描超长台词/旁白：中文字符 >= 100 或包含 >= 2 个换行符"""
import re
from pathlib import Path
LONG_RE = re.compile(r'^\s*(?:\w+\s+)?"((?:[^"\\]|\\.)*)"\s*$')
for f in sorted(Path("game").glob("*.rpy")):
    lines = f.read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines, 1):
        m = LONG_RE.match(line)
        if not m: continue
        text = m.group(1)
        c = sum(1 for ch in text if '\u4e00' <= ch <= '\u9fff')
        nl_count = text.count("\\n")
        if c >= 100 or nl_count >= 2:
            marker = []
            if c >= 100: marker.append(f"{c}zh")
            if nl_count >= 2: marker.append(f"\\n*{nl_count}")
            print(f"{f.name}:L{i}  [{','.join(marker)}]  {text[:40]}...")

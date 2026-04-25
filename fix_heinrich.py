# -*- coding: utf-8 -*-
"""Replace '"海因里希 \\"...\\""' format with 'heinrich "..."'"""
import re
from pathlib import Path

p = Path("game/npc_sidelines.rpy")
lines = p.read_text(encoding="utf-8").splitlines(keepends=True)
count = 0
# pattern: leading whitespace, then "海因里希 \"content\"" (outer quotes + escaped inner)
PAT = re.compile(r'^(\s*)"海因里希\s+\\"(.*)\\""\s*$')
for i, line in enumerate(lines):
    m = PAT.match(line.rstrip("\n"))
    if m:
        indent, content = m.group(1), m.group(2)
        lines[i] = f'{indent}heinrich "{content}"\n'
        count += 1
p.write_text("".join(lines), encoding="utf-8")
print(f"replaced {count} heinrich lines")

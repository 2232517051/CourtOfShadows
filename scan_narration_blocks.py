"""
Scan for long consecutive narrator-only blocks (4+ lines of "..." strings
with no character dialogue, menu, show, scene, jump, call, $, if/elif/else,
label, return, pass).

These are high-risk zones for 'verbose/empty' AI text — environmental description
that goes on without advancing plot or introducing action.

Output: file:line_start-line_end  count=N
"""
import re
from pathlib import Path

# indented narrator line: starts with spaces, then " (but not a character dialogue)
NARRATOR_RE = re.compile(r'^\s+"[^"]')
# structural lines that break a narrator block
BREAK_RE = re.compile(r'^\s*(#|menu:|show |scene |hide |play |stop |jump |call |label |return|pass|\$|if |elif |else|default |python)')
# character dialogue: starts with spaces, then a word (char id), then space and "
CHAR_DIALOG_RE = re.compile(r'^\s+[a-zA-Z_][\w]*\s+"')
# blank line
BLANK_RE = re.compile(r'^\s*$')

files = sorted(Path('game').glob('*.rpy'))

results = []  # (path, start, end, count)

for path in files:
    if 'gui' in path.name or 'options' in path.name or 'screens' in path.name:
        continue
    try:
        lines = path.read_text(encoding='utf-8').splitlines()
    except UnicodeDecodeError:
        continue
    block_start = None
    block_count = 0
    for i, line in enumerate(lines):
        if NARRATOR_RE.match(line) and not CHAR_DIALOG_RE.match(line):
            if block_start is None:
                block_start = i
                block_count = 1
            else:
                block_count += 1
        elif BLANK_RE.match(line):
            # blank line extends the block (neighborhood)
            continue
        else:
            # block ends
            if block_start is not None and block_count >= 4:
                results.append((str(path), block_start + 1, i, block_count))
            block_start = None
            block_count = 0
    # tail
    if block_start is not None and block_count >= 4:
        results.append((str(path), block_start + 1, len(lines), block_count))

# sort by count desc
results.sort(key=lambda r: -r[3])

print(f"=== {len(results)} narrator blocks with 4+ consecutive lines ===\n")
for path, start, end, cnt in results[:40]:
    print(f"{path}:L{start}-L{end}  count={cnt}")
print(f"\nTotal: {len(results)}")
print(f"Blocks ≥6 lines: {sum(1 for r in results if r[3] >= 6)}")
print(f"Blocks ≥8 lines: {sum(1 for r in results if r[3] >= 8)}")

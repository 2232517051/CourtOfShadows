"""
扫 CoS .rpy dialogue 行内的未转义内嵌双引号 — Ren'Py 会把它误解成 image attribute 报错.

示例 bug:
  "你说出"圣·尤里安"四个字"   ← 报错: Say has image attributes ('圣·尤里安',)

修法:
  改用 中文引号「」或者转义 \\"圣·尤里安\\"

用法:
  cd CourtOfShadows
  python Tools/scan_nested_quotes.py
"""
import os, re, sys, io, glob
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

os.chdir(os.path.join(os.path.dirname(__file__), '..'))

SKIP = {'changelog.rpy', 'attr_system.rpy', 'images_def.rpy',
        'screens.rpy', 'options.rpy', 'gui.rpy', '_developer.rpy',
        'audio_safe.rpy', 'balance.rpy', 'screens_custom.rpy',
        'random_events.rpy', 'test_game.rpy',
        # 含大量 screens UI (text "...") 误报
        'inventory.rpy', 'combat.rpy', 'characters.rpy', 'char_helpers.rpy',
        'cinematics.rpy', 'effects.rpy'}

# dialogue 行: (可选 character) "..."
DIALOGUE_RE = re.compile(r'^(\s*)((?:[a-zA-Z_]\w*\s+)?)"(.+)"\s*(?:#.*)?$')

# 白名单: 只扫剧情文件 (排除 UI / screens / 系统)
NARRATIVE_PREFIXES = ('chapter', 'script', 'prologue', 'npc', 'endings', 'chapters_')

issues = 0
in_python_block = False
for f in sorted(glob.glob('game/*.rpy')):
    base = os.path.basename(f)
    if base in SKIP: continue
    if not any(base.startswith(p) for p in NARRATIVE_PREFIXES): continue
    in_python_block = False
    with open(f, encoding='utf-8') as fh: lines = fh.readlines()
    for ln, line in enumerate(lines, 1):
        stripped = line.rstrip('\n').rstrip('\r')
        s = stripped.strip()
        if s.startswith('#'): continue
        # 跳过 Python 块
        if re.match(r'^(init\s+(python|-?\d+\s+python)|python:|python\s+early)', s):
            in_python_block = True; continue
        if in_python_block and (stripped and not stripped[0].isspace()):
            in_python_block = False
        if in_python_block: continue
        # 跳过 docstring
        if '"""' in s: continue
        # 跳过字典字面值 ("key": "value" 形式)
        if re.search(r'"[一-鿿\w]+":\s*[#"]', s): continue
        # 跳过 "speaker_string" "dialogue_string" 两段字符串 say 形式 (合法语法)
        if re.match(r'^\s*"[^"]*(?:\\"[^"]*)*"\s+"', stripped): continue
        m = DIALOGUE_RE.match(stripped)
        if not m: continue
        body = m.group(3)
        cleaned = body.replace('\\"', '')
        if '"' in cleaned:
            print(f'{f.replace(chr(92), "/")}:{ln}  {stripped.strip()[:130]}')
            issues += 1

print(f'\n=== 共 {issues} 处未转义内嵌双引号 (会触发 Renpy "Say has image attributes" 报错) ===')
print('修法: 内嵌部分改用中文引号「」, 或者用 \\\\" 转义')

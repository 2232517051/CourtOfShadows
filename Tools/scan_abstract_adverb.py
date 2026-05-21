"""
扫 CoS 所有 .rpy 文件里的"动作 + 得/太 + 程度字"抽象结构。
端口自铁与誓同名脚本。

抽象副词字: 深 远 久 紧 沉 淡 狠 重 轻 厚 薄 满 慢 透 死 实 严
排除: 物理可观测词不抓 (快 响 亮 红 黑 白)
跳过: 注释行 (#开头), python 块, init python 块

输出: file:line + 上下文 + 高频汇总
"""
import re, os, sys, io, glob
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

os.chdir(os.path.join(os.path.dirname(__file__), '..'))

ABSTRACT_ADJ = '深远久紧沉淡狠重轻厚薄满慢透死实严'

PATTERN = re.compile(
    rf'([一-鿿]{{1,2}})'
    rf'(得太|得很|得有些|得|太)'
    rf'([{ABSTRACT_ADJ}])'
    rf'(?![一-鿿])'
)

WHITELIST_SUBSTR = [
    '走得快', '走得慢',
    '哭得响', '笑得响',
]

# 跳过这些 .rpy 文件 (非剧本)
SKIP_FILES = {
    'screens.rpy', 'options.rpy', 'gui.rpy',
    'attr_system.rpy', 'balance.rpy', 'achievements.rpy',
}


def is_dialogue_line(line):
    """判断这行是不是叙事/对话文本 (含中文双引号或中文内容的引号字符串)"""
    stripped = line.lstrip()
    if stripped.startswith('#'):
        return False
    if stripped.startswith('$') or stripped.startswith('python') or stripped.startswith('init'):
        return False
    if stripped.startswith('if ') or stripped.startswith('elif ') or stripped.startswith('else'):
        return False
    if stripped.startswith('default ') or stripped.startswith('define '):
        return False
    if stripped.startswith('label ') or stripped.startswith('menu') or stripped.startswith('jump ') or stripped.startswith('call '):
        return False
    if stripped.startswith('scene ') or stripped.startswith('show ') or stripped.startswith('hide ') or stripped.startswith('play ') or stripped.startswith('stop '):
        return False
    # 有引号且至少一个中文字 → 视为叙事
    if ('"' in line or '"' in line or '"' in line) and re.search(r'[一-鿿]', line):
        return True
    return False


def scan_file(path):
    hits = []
    try:
        with open(path, encoding='utf-8') as f:
            lines = f.readlines()
    except:
        return hits
    in_python_block = False
    python_indent = 0
    for i, line in enumerate(lines, 1):
        stripped = line.lstrip()
        # python block 检测
        if stripped.startswith('python:') or stripped.startswith('init python:') or stripped.startswith('init -') and 'python' in stripped:
            in_python_block = True
            python_indent = len(line) - len(stripped)
            continue
        if in_python_block:
            cur_indent = len(line) - len(stripped) if stripped else 999
            if stripped and cur_indent <= python_indent:
                in_python_block = False
            else:
                continue
        if not is_dialogue_line(line):
            continue
        for m in PATTERN.finditer(line):
            phrase = m.group(0)
            if any(w in phrase for w in WHITELIST_SUBSTR):
                continue
            hits.append((i, phrase, line.strip()[:140]))
    return hits


def main():
    files = sorted(glob.glob('game/**/*.rpy', recursive=True))
    files = [f for f in files if os.path.basename(f) not in SKIP_FILES]
    total = 0
    by_phrase = {}
    file_hits = []
    for f in files:
        hits = scan_file(f)
        if not hits: continue
        file_hits.append((f, hits))
        for line, phrase, ctx in hits:
            by_phrase[phrase] = by_phrase.get(phrase, 0) + 1
            total += 1
    for f, hits in file_hits:
        rel = f.replace('\\', '/')
        print(f'\n== {rel} ({len(hits)} 处) ==')
        for line, phrase, ctx in hits:
            print(f'  {line}: [{phrase}]  {ctx}')

    print('\n' + '=' * 60)
    print(f'共 {total} 处, 按高频排序:')
    for phrase, n in sorted(by_phrase.items(), key=lambda x: -x[1]):
        if n >= 2:
            print(f'  {phrase}  x{n}')


if __name__ == '__main__':
    main()

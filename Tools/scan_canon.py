"""
扫描 CoS canon 错误 — 主要抓"角色 / 物品 / 事件首次出现前的提前引用"和"重名混用"。

用法:
    cd CourtOfShadows
    python Tools/scan_canon.py

输出: 文件:行号 [类型] 原文

注意: 粗筛工具, 误报多. 人工核对 CANON.md 后再判断。
"""
import os
import re
import sys
import io
import glob

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# ============ CANON 触发词 (出现这些词时, 检查上下文) ============
# 写新场景如果出现下列词, 应该 grep 全项目确认现有 canon
CANON_TRIGGER_WORDS = [
    # 神 / 称号 / 头衔
    '永恒者', '圣安德烈', '圣徒', '教士',
    '领主大人', '殿下', '陛下', '公爵',
    # 家族 / 纹章
    '金鹰', '铁锤', '双纹章', '灰隼', '苍鹰',
    # 物品 / 毒药
    '暮色之露', '暗百合', '旧约', '影月草',
    # 重名预警
    '托马斯', '玛格丽特', '西里尔', '伯爵夫人',
    # 人物
    '雷恩', '艾琳娜', '伊蕾娜', '奥德', '康拉德', '胡伯特',
]

# ============ 反逻辑短语 (栀子类 bug) ============
# 主角刚见到 NPC 不应该说"我已经考察过 / 我之前问过 / 我了解过"
ANTI_LOGIC_PHRASES = [
    (r'我替你考察过', 'C 反逻辑: 主角"我替你考察过"'),
    (r'我之前问过.{1,8}了', 'C 反逻辑: "我之前问过 X 了"'),
    (r'我了解过.{1,8}的', 'C 反逻辑: "我了解过 X 的"'),
    (r'我打听过.{1,8}的', 'C 反逻辑: "我打听过 X 的"'),
    (r'你的事情我都听说过', 'C 反逻辑: "你的事情我都听说过"'),
    # 时间跨度: 主线 30 天 / 5 章, 不该出现"这一年""去年""半年前"等长跨度
    # (有些 NPC 提自己往事可以, 但谈主角处境时不行 — 误报由人工排除)
    (r'你这一年', 'C 时间线: "你这一年" — 主线只跨 30 天'),
    (r'这一年来', 'C 时间线: "这一年来" — 主线跨度不到一年'),
    (r'你这半年', 'C 时间线: "你这半年" — 主线跨度不到半年'),
    (r'继任.{0,4}(半年|一年)', 'C 时间线: 继任跨度跟主线不符'),
]

# ============ 错别字 / canon 偏差 (memory 记录) ============
# 这些都是 canon 已定但容易写错的
TYPO_PATTERNS = [
    (r'灰隼|苍鹰', 'D 错纹章: 应是"金鹰"'),
    # 银鹰骑士团是 CANON.md"非主角鹰白名单"里的合法组织(北方自由骑士, 塞德里克所属),
    # 不是错纹章。原规则 r'神鹰|银鹰' 把它全判成错, 在 random_events_new.rpy 造成 6 处
    # 常驻误报 —— 加负向先行, 只放过"银鹰骑士团"这个白名单词。
    (r'神鹰|银鹰(?!骑士团)', 'D 错纹章: 应是"金鹰"(注: "银鹰骑士团"是白名单, 见 CANON.md)'),
    (r'家族徽章.{0,8}(?<!金)鹰', 'D 检查"鹰" 前后是否加"金"'),
]

# ============ 术语统一 ============
# 主线五章零使用"王军/王师", 规范说法是"王室军队"(chapter5.rpy:47)。
# 批40 统一南境时**只扫了 southern_expansion.rpy**, 漏了 characters.rpy 的成就 hint 和
# gallery.rpy 的鉴赏/音乐室条目名 —— "找到一张表就收工"这个毛病本轮犯了两次, 下沉到扫描。
# 例外: 特使/主帅正式发言里自称"王师"是官腔(正义之师), 与旁白的中立叙述分野, 那 5 处保留。
TERM_PATTERNS = [
    (r'王军', 'T 术语: 主线规范是"王室军队"(chapter5.rpy:47), 全项目零使用"王军"'),
]

# ============ 艾登堡地理 (CANON.md 二·B) ============
# 艾登堡是内陆领地: 不靠海、无海港、无码头栈桥, 附近只有渡口(浅滩)。
# 去南方海路要"先四天陆路翻两道山, 到王国南边的海港城换船"(southern_expansion.rpy:265)。
# 这条已经被写错三次(原作者的"盐船驶进艾登堡的港湾"、外章并入时的五段返程 coda),
# 靠人记显然不管用, 所以下沉到扫描里。
GEO_PATTERNS = [
    (r'船(?:到|抵|进)艾登堡', 'G 地理: 艾登堡不靠海, 船开不到 (回程应是 海港城下船 → 四天陆路)'),
    (r'艾登堡的(?:码头|港湾|港口|栈桥|河道)', 'G 地理: 艾登堡不靠海, 没有码头/港湾/栈桥'),
    # 只认"船"驶入 —— 车队/马车队驶入艾登堡是对的(盐正是海路→河港→车运进城门),
    # 早先写成 (?:驶进|驶入|开进)艾登堡 会把 governance.rpy:762「满载粮食的马车队缓缓驶入
    # 艾登堡」这类正确句子一起报掉。
    (r'[船舰艇](?:队)?[^。；\n]{0,6}(?:驶进|驶入|驶抵|开进)艾登堡', 'G 地理: 艾登堡不靠海, 船开不进'),
    (r'艾登堡.{0,6}(?:靠岸|下船|登船)', 'G 地理: 艾登堡不靠海'),
]

DIALOGUE_RE = re.compile(r'(?:^|\s)(?:[a-zA-Z_][a-zA-Z_0-9]*\s+)?"([^"\n]{6,})"')

SKIP_FILE_NAMES = {
    'changelog.rpy', 'attr_system.rpy', 'images_def.rpy',
    'screens.rpy', 'options.rpy', 'gui.rpy', '_developer.rpy',
}


def scan_raw_lines(path, patterns):
    """扫原始行, 不走 DIALOGUE_RE。返回 [(line_num, name, snippet)].

    为什么要单开一个: DIALOGUE_RE 只认引号内 >=6 字的串, 所以像
    gallery.rpy:32 ("bg_tideport_fleet", "王军压境") 这种 4 字条目名
    **从来不在任何 canon 规则的视野里** —— 批40 漏掉鉴赏/音乐室的"王军"就是这么漏的。
    术语类检查(名字/条目名/成就名, 通常很短)必须扫原始行。
    """
    hits = []
    try:
        with open(path, encoding='utf-8') as f:
            lines = f.readlines()
    except Exception:
        return hits
    for ln, line in enumerate(lines, 1):
        if line.strip().startswith('#'):
            continue          # 跳过注释, 免得注释里举例的错词自己报自己
        for pat, name in patterns:
            if re.search(pat, line):
                t = line.strip()
                hits.append((ln, name, t if len(t) <= 120 else t[:117] + '...'))
    return hits


def scan_file_for_patterns(path, patterns):
    """返回 [(line_num, name, snippet)]."""
    hits = []
    try:
        with open(path, encoding='utf-8') as f:
            lines = f.readlines()
    except: return hits

    for ln, line in enumerate(lines, 1):
        if line.strip().startswith('#'): continue
        for m in DIALOGUE_RE.finditer(line):
            text = m.group(1)
            for pat, name in patterns:
                if re.search(pat, text):
                    snippet = text if len(text) <= 120 else text[:117] + '...'
                    hits.append((ln, name, snippet))
                    break
    return hits


def collect_canon_word_occurrences(files):
    """对每个 CANON_TRIGGER_WORDS 词, 收集每次出现位置 (file, line) — 输出报告让人工核对一致性."""
    word_locs = {w: [] for w in CANON_TRIGGER_WORDS}
    for path in files:
        try:
            with open(path, encoding='utf-8') as f:
                content = f.read()
        except: continue
        rel = os.path.relpath(path).replace('\\', '/')
        for ln, line in enumerate(content.split('\n'), 1):
            if line.strip().startswith('#'): continue
            for w in CANON_TRIGGER_WORDS:
                if w in line:
                    word_locs[w].append((rel, ln))
    return word_locs


def main():
    root = os.path.join(os.path.dirname(__file__), '..', 'game')
    files = glob.glob(os.path.join(root, '*.rpy'))
    files = [f for f in files if os.path.basename(f) not in SKIP_FILE_NAMES]

    # 1. 反逻辑短语扫描
    print('=' * 60)
    print('反逻辑短语 (主角不可能知道却写知道):')
    print('=' * 60)
    total_anti = 0
    for path in sorted(files):
        for ln, name, snip in scan_file_for_patterns(path, ANTI_LOGIC_PHRASES):
            print(f'{os.path.relpath(path).replace(chr(92), "/")}:{ln}  [{name}]  {snip}')
            total_anti += 1
    print(f'  → {total_anti} 处')

    # 1.5 艾登堡地理 (CANON.md 二·B)
    print()
    print('=' * 60)
    print('艾登堡地理 (内陆领地, 不靠海):')
    print('=' * 60)
    total_geo = 0
    for path in sorted(files):
        for ln, name, snip in scan_file_for_patterns(path, GEO_PATTERNS):
            print(f'{os.path.relpath(path).replace(chr(92), "/")}:{ln}  [{name}]  {snip}')
            total_geo += 1
    print(f'  → {total_geo} 处')

    # 1.6 术语统一
    print()
    print('=' * 60)
    print('术语统一 (王军 → 王室军队):')
    print('=' * 60)
    total_term = 0
    for path in sorted(files):
        for ln, name, snip in scan_raw_lines(path, TERM_PATTERNS):
            print(f'{os.path.relpath(path).replace(chr(92), "/")}:{ln}  [{name}]  {snip}')
            total_term += 1
    print(f'  → {total_term} 处')

    # 2. canon 词偏差 (错别字 / 错纹章)
    print()
    print('=' * 60)
    print('canon 偏差 (错别字 / 错纹章):')
    print('=' * 60)
    total_typo = 0
    for path in sorted(files):
        for ln, name, snip in scan_file_for_patterns(path, TYPO_PATTERNS):
            print(f'{os.path.relpath(path).replace(chr(92), "/")}:{ln}  [{name}]  {snip}')
            total_typo += 1
    print(f'  → {total_typo} 处')

    # 3. canon 触发词出现次数报告 (人工核对一致性)
    print()
    print('=' * 60)
    print('canon 触发词出现频次 (人工对照 CANON.md 检查):')
    print('=' * 60)
    word_locs = collect_canon_word_occurrences(files)
    for w in CANON_TRIGGER_WORDS:
        locs = word_locs[w]
        if not locs: continue
        print(f'  {w}: {len(locs)} 处')
        # 仅前 5 处作样本
        for rel, ln in locs[:5]:
            print(f'    {rel}:{ln}')
        if len(locs) > 5:
            print(f'    ... +{len(locs) - 5} more')

    print()
    print(f'=== 总结: {total_anti} 反逻辑 + {total_typo} canon 偏差 ===')
    print('对照 CANON.md 修. 改不动的加注释 # canon-ok: <理由>')


if __name__ == '__main__':
    main()

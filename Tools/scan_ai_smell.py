"""
扫描 CoS 全部 .rpy 文件的台词 / 旁白，输出历史启发式命中。

这份报告含有大量误报，只用于诊断，不是文风通过门槛。

用法:
    cd CourtOfShadows
    python Tools/scan_ai_smell.py
    python Tools/scan_ai_smell.py game/chapter1.rpy

输出: 文件:行号 [模式名] 原文 (前 120 字)
"""
import os
import re
import sys
import io
import glob

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# Historical heuristic patterns retained for optional diagnostics.
PATTERNS = [
    # ── A. 句式层 ──
    # A1 排比 3 段同结构
    (r'。\s*[^。\n]{2,12}。\s*[^。\n]{2,12}。\s*[^。\n]{2,12}。', 'A1 排比 3 段'),
    # A2 反转金句
    (r'我以为.{1,30}(其实|后来|最终)', 'A2 反转金句'),
    (r'.{2,12}—+\s*其实', 'A2 反转金句'),
    # A3 比喻金句 "像 X" 末尾
    (r'像[^,，。\n]{2,15}[。\n]', 'A3 比喻金句"像..."'),
    # A4 物品拟人
    (r'(瓶|罐|锅|茶壶|围裙|抽屉|地毯|柜|架|火|墙|窗|门|椅|桌|镜|盒|金币|账本|剑|盾)[^,，。\n]{0,8}(记得|喜欢|不喜欢|知道|想念|希望|愿意|讨厌)', 'A4 物品拟人'),
    # A5 顶针 (前末 = 后首)
    (r'([一-龥]{2,4})[。,，]\s*\1', 'A5 顶针'),
    # A6 普遍化
    (r'就是这样', 'A6 普遍化'),
    (r'都会.{1,10}的', 'A6 普遍化'),
    # A7 抽象升华 "X 就一直是 / 一段没说完 / 改变了你和"
    (r'一段没说完的话', 'A7 抽象升华'),
    (r'改变了你和.{1,8}的关系', 'A7 抽象升华'),

    # ── B. 词汇层 ──
    # B1 单字名词 (周围没双字组合)
    (r'(?<![繁星辰空月色光风波雨水雪花炉篝晨晚夜])[星月风雨雪火](?![空辰光色风波水花炉篝晨晚夜])', 'B1 单字名词'),
    # B3 自创四字短语
    (r'(礼数|守心|心如|凝霜|静观|寂如|岁月|时光|风雪|血誓|铁腕|金心)[一-龥]{2}', 'B3 可能自创四字'),
    # B4 信念名词化引号 ("那套'X'的Y")
    (r'那套\s*[\'"“‘][^\'"”’]+[\'"”’]', 'B4 信念名词化"那套X"'),
    # B5 概念抽象动词
    (r'(做出|面对|承担|接纳|拥抱|放下)(选择|抉择|真相|责任|过去|未来)', 'B5 概念抽象动词'),
    # B6 抽象空泛短语 (设计文档常见)
    (r'(让|把).{1,8}(走多远|走得|拉进|感受到)', 'B6 抽象空泛'),
    (r'(这才是|真正的)[一-龥]{1,10}(核心|意义|价值|应该)', 'B6 "这才是 / 真正的"'),
    # B7 "X 很 Y, 很 Z" 双形容词对仗
    (r'[一-龥]{1,3}很[一-龥]{1,3},\s*很[一-龥]{1,3}', 'B7 双形容词对仗'),
    (r'[一-龥]{1,3}很[一-龥]{1,3},\s*很[一-龥]{1,3}', 'B7 双形容词对仗(全角)'),
    # B8 抽象"躲" 当回避道德责任
    (r'你没躲', 'B8 抽象"躲"(改"逃避")'),
    (r'躲不开', 'B8 抽象"躲"(改"逃避")'),

    # ── C. AI 说教味 ──
    # C2 旁白评价"勇敢的选择"
    (r'这是一个.{0,4}(勇敢|正确|艰难|沉重|温柔|残酷)的(决定|选择|抉择)', 'C2 旁白评价"勇敢的选择"'),
    # C3 反派话太正确
    (r'我理解你的(反对|愤怒|不满)', 'C3 反派"我理解你"'),
    (r'也许我们都(不对|错了)', 'C3 反派"都不对"'),

    # ── D. qu-ai-wei 净新增 (翻译腔 / 弱动词 / 名词化 / filler / 抽象升华) ──
    # D1 翻译腔被动 "被X的Y" (单发可疑)
    (r'被[一-龥]{1,8}的[一-龥]', 'D1 翻译腔被动"被X的Y"'),
    # D2 同一行内 2+ 个"被" (双/三被动堆叠, 最确诊)
    (r'被[一-龥]+.{0,15}被[一-龥]+', 'D2 双被动连发'),
    # D3 弱动词 "进行/展开/开展 + V"
    (r'(进行了?|展开了?|开展了?)[一-龥]{2,6}', 'D3 弱动词"进行/展开"'),
    # D4 弱动词 "持续了/持续着" + 时间
    (r'持续[了着][一-龥]{0,3}[一二三四五六七八九十0-9]', 'D4 弱动词"持续了 N 天"'),
    # D5 名词化 "X 化/性 的 Y"
    (r'[一-龥][化性]的[一-龥]{2}', 'D5 名词化"X化/性的Y"'),
    # D6 filler 软化词
    (r'(实际上|一定程度上|某种程度上|某种意义上|在某种)', 'D6 filler 软化词'),
    # D7 filler "一些" 跟在弱动词后
    (r'(留下了?|还有|有了?|多了|存在着?)\s*一些', 'D7 filler"留下了一些"'),
    # D8 的的不休 (3+ 的, 每段间隔 ≤ 8 字)
    (r'的[^的\n]{1,8}的[^的\n]{1,8}的[^的\n]{1,15}', 'D8 的的不休 3+'),
    # D9 双重否定 "不可能不 / 不得不 + 不 / 不能不"
    (r'(不可能不|不得不[一-龥]+不|不能不)[一-龥]', 'D9 双重否定'),
    # D10 客服腔预告 "一个/一种 X 正在/开始 Y"
    (r'(一个|一种)[一-龥]{2,8}(正在|开始)[一-龥]{2}', 'D10 客服腔预告'),
    # D11 抽象升华尾 "...的象征 / 意味 / 启示 / 缩影 / 印记"
    (r'[一-龥]{2,8}的(象征|意味|启示|觉悟|印记|缩影|本质|写照)[。"\n!?]', 'D11 抽象升华尾'),
    # D12 historical reversal pattern
    (r'不是[一-龥]{1,20}[,，][\s]?而是[一-龥]', 'D12 反转"不是X,而是Y"'),
    (r'不是[一-龥]{1,20}—+[一-龥]{0,8}而是', 'D12 反转"不是X—而是Y"'),
]

# 提取台词的正则: Ren'Py 台词形式
#   "narration text"
#   character "dialogue"
#   menu choice "...":
DIALOGUE_RE = re.compile(r'(?:^|\s)(?:[a-zA-Z_][a-zA-Z_0-9]*\s+)?"([^"\n]{6,})"')


def scan_file(path):
    """扫单个 .rpy 文件, 返回 [(line_num, pattern_name, snippet)]."""
    hits = []
    try:
        with open(path, encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        print(f'[!] cannot read {path}: {e}')
        return hits

    for ln, line in enumerate(lines, 1):
        # 跳过注释行
        stripped = line.strip()
        if stripped.startswith('#'): continue
        # 抽出 "..." 字符串内容
        for m in DIALOGUE_RE.finditer(line):
            text = m.group(1)
            if len(text) < 6: continue
            # 跑所有模式
            for pat, name in PATTERNS:
                if re.search(pat, text):
                    snippet = text if len(text) <= 120 else text[:117] + '...'
                    hits.append((ln, name, snippet))
                    break  # 一行只报最早匹配, 避免噪音
    return hits


# 跳过非剧情文件 (数据 / changelog / 系统)
SKIP_FILE_NAMES = {
    'changelog.rpy',       # 更新日志, 中文有大量"单字名词"误报
    'attr_system.rpy',     # 属性阶位定义, 含"铁腕领主"等数据
    'images_def.rpy',      # 图片定义
    'screens.rpy',         # UI 屏幕
    'options.rpy',         # Ren'Py 设置
    'gui.rpy',             # GUI 配置
    '_developer.rpy',      # 开发工具
}


def main():
    args = sys.argv[1:]
    if args:
        files = []
        for a in args:
            if os.path.isdir(a):
                files.extend(glob.glob(os.path.join(a, '**', '*.rpy'), recursive=True))
            else:
                files.append(a)
    else:
        # 默认: game/ 下所有 .rpy
        root = os.path.join(os.path.dirname(__file__), '..', 'game')
        files = glob.glob(os.path.join(root, '*.rpy'))

    # 过滤 skip 列表
    files = [f for f in files if os.path.basename(f) not in SKIP_FILE_NAMES]

    if not files:
        print('No .rpy files found.')
        return

    total = 0
    for path in sorted(files):
        hits = scan_file(path)
        if not hits: continue
        rel = os.path.relpath(path).replace('\\', '/')
        for ln, name, snip in hits:
            print(f'{rel}:{ln}  [{name}]  {snip}')
        total += len(hits)

    print()
    print(f'=== 共 {total} 处历史启发式命中（含误报）===')
    print('以上结果不作为文风通过门槛。')
    print('文风以 docs/writing-style/INDEX.md 中经用户确认的正例为准。')


if __name__ == '__main__':
    main()

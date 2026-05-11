"""
扫描 Ch2-Ch5 menu, 用启发式找"应该有 1d10 检定"的高张力候选节点。

评分维度:
  + 选项含动作动词 (说服/对峙/识破/潜入/追问/揭穿/反驳/拒绝/抢救/暗算)
  + menu 周围有紧张关键词 (危机/暗杀/阴谋/对峙/揭穿/谋反/兵临/夜袭)
  + chapter 是 ch3/ch4/ch5 (后期)
  - 选项数 > 4 (太多支选项, 倾向于纯叙事分支不适合检定)
"""
import re
from pathlib import Path

GAME_DIR = Path(r'C:\Users\22325\Desktop\renpy-8.5.2-sdk\CourtOfShadows\game')

# 高张力动作动词 (选项里出现 → 加分)
ACTION_KEYWORDS = [
    '说服', '劝说', '谈判', '对峙', '抗议', '反驳', '驳斥', '拒绝',
    '识破', '揭穿', '揭露', '当场', '公开质问', '公开',
    '潜入', '偷', '暗算', '突袭', '夜袭', '暗杀', '埋伏',
    '试探', '追问', '套话', '诱', '逼问', '审问',
    '抢救', '救援', '夺回', '夺取',
    '强闯', '强行', '硬闯', '威胁', '恫吓',
    '查', '搜查', '查证', '搜', '盯梢',
    '装作', '伪装', '假扮',
]

# menu 周围窗口 (前 30 行) 出现的紧张关键词
TENSION_KEYWORDS = [
    '危机', '阴谋', '暗杀', '谋反', '叛乱', '兵临', '夜袭', '刺客',
    '毒', '杀', '死', '陷阱', '诡计',
    '对峙', '当面', '揭穿', '罪证',
    '生死', '存亡', '危险',
]


def scan_chapter(path: Path):
    text = path.read_text(encoding='utf-8')
    lines = text.split('\n')

    # 找所有 menu: 起始行
    candidates = []
    for i, line in enumerate(lines):
        if not re.match(r'^\s*menu:\s*$', line):
            continue

        # 收集这个 menu 的选项 (后续 50 行内 quoted strings 接 :)
        opts = []
        end = min(i + 50, len(lines))
        for j in range(i + 1, end):
            l = lines[j]
            # 选项格式: 缩进 + "...":
            m = re.match(r'^\s+"([^"]+)"\s*:?\s*$', l)
            if m:
                opts.append(m.group(1))
            elif re.match(r'^\s*menu:|^label\s+', l):
                break
            elif l and not l.startswith(' ') and not l.startswith('\t'):
                break

        if not opts: continue

        # 评分
        score = 0
        action_hits = []
        for opt in opts:
            for kw in ACTION_KEYWORDS:
                if kw in opt:
                    score += 2
                    action_hits.append(kw)

        # 上下文 30 行
        ctx_start = max(0, i - 30)
        ctx_end = min(len(lines), i + 30)
        ctx = '\n'.join(lines[ctx_start:ctx_end])
        tension_hits = [kw for kw in TENSION_KEYWORDS if kw in ctx]
        score += len(tension_hits)

        # 选项数惩罚
        if len(opts) > 4: score -= 1
        if len(opts) <= 2: score += 1

        if score >= 3:
            candidates.append({
                'file': path.name,
                'line': i + 1,
                'score': score,
                'opts': opts[:5],
                'actions': list(set(action_hits)),
                'tensions': list(set(tension_hits))[:5],
            })
    return candidates


def main():
    files = [
        'chapter2.rpy', 'chapter2_expansion.rpy',
        'chapter3.rpy',
        'chapter4.rpy', 'chapter4_expansion.rpy', 'chapter4_prince.rpy',
        'chapter5.rpy',
    ]
    all_candidates = []
    for f in files:
        all_candidates.extend(scan_chapter(GAME_DIR / f))

    all_candidates.sort(key=lambda c: -c['score'])

    print(f'共 {len(all_candidates)} 个候选高张力 menu (score >= 3)\n')
    for i, c in enumerate(all_candidates[:25], 1):
        print(f"#{i}  [{c['score']}]  {c['file']}:L{c['line']}")
        print(f"  动作: {' '.join(c['actions']) if c['actions'] else '-'}")
        print(f"  气氛: {' '.join(c['tensions']) if c['tensions'] else '-'}")
        for o in c['opts']:
            print(f"    · {o[:60]}")
        print()


if __name__ == '__main__':
    main()

"""
扫描所有"初见式"台词 — 候选清单生成工具

搜索两类正则：
1. 台词内出现"初见关键词"（鄙人/在下/久仰/幸会/等）
2. 该角色是否已有 met flag 守卫（default {char}_met = ...）

输出按 Character 分组，标注：
- [已守卫]: 已有 {char}_met flag + if 守卫
- [缺守卫]: 有初见台词但无 flag 或守卫
- [无需]: 台词无初见特征（不输出）

输出供人工审核，不自动插入守卫（守卫台词需针对性改写）。
"""
import os
import re
import sys
from collections import defaultdict

GAME_DIR = os.path.join(os.path.dirname(__file__), "game")

# 初见关键词 —— 台词里出现这些，视为"可能是初见自我介绍"
FIRST_MEET_KEYWORDS = [
    "鄙人", "在下", "鄙名", "小人", "小的",
    "久仰", "幸会", "初次", "第一次见",
    "行走四方", "行商", "走南闯北", "游方",
    "敢问", "不才", "有礼了", "初来乍到",
    "素未谋面", "素昧平生",
    "见过领主大人", "拜见",
    "我的名字叫", "我叫", "在下名叫",
    "你就是", "您就是", "您是新",
    "年轻的领主", "新来的领主", "新任领主",
    "令尊", "令父", "您父亲",  # 提到父亲常在初见时说
]

# Character 定义
CHAR_DEF_RE = re.compile(r'^\s*define\s+(\w+)\s*=\s*Character\s*\((.*)\)\s*$')
CHAR_NAME_RE = re.compile(r'Character\s*\(\s*["\']([^"\']+)["\']')

# 台词行
DIALOGUE_RE = re.compile(r'^\s*(\w+)\s+"((?:[^"\\]|\\.)*)"')

# 流程控制
DEFAULT_RE = re.compile(r'^default\s+(\w+_met)\s*=')
IF_MET_RE = re.compile(r'if\s+(\w+_met)\s*:')


def collect_chars():
    """采集所有 Character 定义 -> {id: display_name}"""
    chars = {}
    for fname in sorted(os.listdir(GAME_DIR)):
        if not fname.endswith(".rpy"):
            continue
        p = os.path.join(GAME_DIR, fname)
        with open(p, "r", encoding="utf-8") as f:
            for line in f:
                m = CHAR_DEF_RE.match(line)
                if not m:
                    continue
                cid, args = m.group(1), m.group(2)
                nm = CHAR_NAME_RE.search(line)
                chars[cid] = nm.group(1) if nm else "?"
    return chars


def collect_met_flags():
    """采集所有 default XXX_met 定义"""
    flags = set()
    for fname in sorted(os.listdir(GAME_DIR)):
        if not fname.endswith(".rpy"):
            continue
        p = os.path.join(GAME_DIR, fname)
        with open(p, "r", encoding="utf-8") as f:
            for line in f:
                m = DEFAULT_RE.match(line)
                if m:
                    flags.add(m.group(1))
    return flags


def contains_meet_keyword(text):
    """检查台词是否含初见关键词，返回命中的关键词"""
    hits = []
    for kw in FIRST_MEET_KEYWORDS:
        if kw in text:
            hits.append(kw)
    return hits


def scan_dialogue(chars):
    """扫描所有台词行，找出含初见关键词的。返回 [(char_id, display, file, line, text, keywords)]"""
    results = []
    for fname in sorted(os.listdir(GAME_DIR)):
        if not fname.endswith(".rpy"):
            continue
        p = os.path.join(GAME_DIR, fname)
        with open(p, "r", encoding="utf-8") as f:
            lines = f.readlines()
        for i, line in enumerate(lines, 1):
            m = DIALOGUE_RE.match(line)
            if not m:
                continue
            speaker, text = m.group(1), m.group(2)
            if speaker not in chars:
                continue  # 非 Character 讲者 (narrator / 随机 id)
            kws = contains_meet_keyword(text)
            if not kws:
                continue
            results.append({
                "speaker": speaker,
                "display": chars[speaker],
                "file": fname,
                "line": i,
                "text": text[:100],
                "keywords": kws,
            })
    return results


def check_guard_status(speaker, file, line, met_flags):
    """检查该台词所在位置前 20 行内是否有 if X_met: 守卫"""
    expected_flag = f"{speaker}_met"
    has_flag = expected_flag in met_flags
    # 读该文件，往前找 if
    p = os.path.join(GAME_DIR, file)
    with open(p, "r", encoding="utf-8") as f:
        lines = f.readlines()
    guard_found = None
    for i in range(line - 1, max(line - 25, 0), -1):
        m = IF_MET_RE.search(lines[i])
        if m:
            guard_found = m.group(1)
            break
    return has_flag, guard_found


def main():
    chars = collect_chars()
    met_flags = collect_met_flags()
    print(f"Character 定义: {len(chars)} 个")
    print(f"现有 met flags: {sorted(met_flags)}")
    print("=" * 70)

    findings = scan_dialogue(chars)
    print(f"\n含初见关键词的台词总数: {len(findings)}")

    grouped = defaultdict(list)
    for f in findings:
        grouped[f["speaker"]].append(f)

    # 分类
    guarded = []       # 有 met flag + 台词前有 if 守卫
    has_flag_only = [] # 有 met flag 但台词前无 if 守卫 (遗漏)
    no_flag = []       # 无 met flag

    for speaker, items in grouped.items():
        expected_flag = f"{speaker}_met"
        has_flag = expected_flag in met_flags
        for item in items:
            _, guard = check_guard_status(
                item["speaker"], item["file"], item["line"], met_flags
            )
            item["has_flag"] = has_flag
            item["guard"] = guard
            if has_flag and guard == expected_flag:
                guarded.append(item)
            elif has_flag:
                has_flag_only.append(item)
            else:
                no_flag.append(item)

    # 输出
    print(f"\n[已守卫] {len(guarded)} 处 — 有 flag + 前 25 行内 if 守卫")
    for item in guarded:
        print(f"  {item['display']:<10}  {item['file']}:L{item['line']}  [{item['guard']}]")

    print(f"\n[有 flag 无守卫] {len(has_flag_only)} 处 — flag 存在但台词未被守卫（可能遗漏）")
    for item in has_flag_only:
        kw = ",".join(item["keywords"][:3])
        print(f"  {item['display']:<10}  {item['file']}:L{item['line']}  [{kw}]  {item['text'][:60]!r}")

    print(f"\n[无 flag] {len(no_flag)} 处 — 角色无 _met flag 定义")
    # 按 speaker 分组输出
    by_speaker = defaultdict(list)
    for item in no_flag:
        by_speaker[item["speaker"]].append(item)
    for speaker, items in sorted(by_speaker.items(), key=lambda x: -len(x[1])):
        display = chars[speaker]
        print(f"\n  === {display} ({speaker}, {len(items)} 处) ===")
        for item in items[:10]:  # 每角色最多10处
            kw = ",".join(item["keywords"][:3])
            print(f"    {item['file']}:L{item['line']}  [{kw}]  {item['text'][:80]!r}")
        if len(items) > 10:
            print(f"    ... +{len(items) - 10} more")


if __name__ == "__main__":
    main()

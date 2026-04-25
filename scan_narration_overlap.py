"""
扫描立绘叠加盲区：连续旁白段前残留立绘

检测规则：
- "旁白行" = 以纯双引号开头的纯叙述行（不带讲者标识）
- 触发条件：紧接 show/台词 之后出现 >= 2 行连续旁白
- 建议：在旁白段前插入 $ hide_all_chars() 清场

输出 A 类（建议修复位置）+ 统计。
"""
import os
import re
import sys

GAME_DIR = os.path.join(os.path.dirname(__file__), "game")

# 行类型正则
LABEL_RE = re.compile(r'^(\s*)label\s+(\w+)')
SCENE_RE = re.compile(r'^(\s*)scene\b')
SHOW_RE = re.compile(r'^(\s*)show\s+(\w+_img)\b')
HIDE_RE = re.compile(r'^(\s*)hide\s+(\w+_img)')
HIDE_ALL_RE = re.compile(r'^(\s*)\$\s*hide_all_chars\s*\(')
# 旁白：行首是 " 或者 centered " 或者 extend ..." 起始
NARRATION_RE = re.compile(r'^(\s*)("|centered\s+"|narrator\s+")')
# 对话：讲者 id 开头
DIALOGUE_RE = re.compile(r'^(\s*)(\w+)\s+"')
# 菜单选项、menu:、if/else 等
# 兼容带 guard 的选项: "选项" if <expr>:
MENU_OPT_RE = re.compile(r'^(\s*)"[^"]*"(?:\s+if\s+.*)?:\s*$')
MENU_KW_RE = re.compile(r'^(\s*)menu\s*:')
IF_RE = re.compile(r'^(\s*)(if|elif|else)\b')
COMMENT_RE = re.compile(r'^\s*#')
EMPTY_RE = re.compile(r'^\s*$')

TARGET_FILES_DEFAULT = ["chapter2.rpy", "chapter2_expansion.rpy"]


def classify(line):
    if COMMENT_RE.match(line) or EMPTY_RE.match(line):
        return "skip"
    if LABEL_RE.match(line):
        return "label"
    if SCENE_RE.match(line):
        return "scene"
    if HIDE_ALL_RE.match(line):
        return "hide_all"
    if SHOW_RE.match(line):
        return "show"
    if HIDE_RE.match(line):
        return "hide"
    if MENU_KW_RE.match(line):
        return "menu"
    if MENU_OPT_RE.match(line):
        return "menu_opt"
    if IF_RE.match(line):
        return "branch"
    # dialogue 必须先于 narration 判断（因为 narrator "..." 也是 DIALOGUE_RE 匹配）
    if DIALOGUE_RE.match(line) and not NARRATION_RE.match(line):
        return "dialogue"
    if NARRATION_RE.match(line):
        return "narration"
    return "other"


def scan_file(path, min_narration_block=2):
    """
    找出所有需要插入 hide_all_chars 的位置。

    触发条件：
    - 存在 active_show（非 None）
    - 遇到连续 >= min_narration_block 行旁白
    - 旁白块中无 hide_all/scene/show/dialogue
    返回插入建议列表 [(行号1-indexed, 缩进, 触发原因)]。
    """
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    suggestions = []
    active_show = None          # 当前 active 的立绘 tag
    narration_start = None      # 连续旁白起始行 (0-indexed)
    narration_indent = None     # 连续旁白的缩进
    menu_indent_stack = []      # menu 块缩进栈；栈非空时处于 menu 块内

    def line_indent(line):
        return len(line) - len(line.lstrip())

    i = 0
    while i < len(lines):
        line = lines[i]
        kind = classify(line)

        # 退出 menu 块：当前行缩进 <= 栈顶 menu 缩进
        if menu_indent_stack and kind not in ("skip",):
            cur_ind = line_indent(line)
            while menu_indent_stack and cur_ind <= menu_indent_stack[-1]:
                menu_indent_stack.pop()

        if kind == "scene":
            active_show = None
            narration_start = None
        elif kind == "hide_all":
            active_show = None
            narration_start = None
        elif kind == "show":
            m = SHOW_RE.match(line)
            active_show = m.group(2)
            narration_start = None
        elif kind == "hide":
            # 可能 hide 的就是 active；保守假设 active 被清
            narration_start = None
            # 不改 active_show — 某些 hide 只是清特定
        elif kind == "dialogue":
            narration_start = None
        elif kind == "label":
            active_show = None
            narration_start = None
            menu_indent_stack.clear()
        elif kind == "menu":
            narration_start = None
            # 记录 menu: 这行的缩进，其块内行缩进必然 > 此值
            menu_indent_stack.append(line_indent(line))
        elif kind == "menu_opt" or kind == "branch":
            narration_start = None
        elif kind == "narration":
            # menu 块内的字符串行（menu caption / 带 guard 的选项变体）不算旁白
            if menu_indent_stack:
                narration_start = None
                i += 1
                continue
            m = NARRATION_RE.match(line)
            indent = m.group(1)
            if narration_start is None:
                narration_start = i
                narration_indent = indent
                narration_count = 1
            else:
                narration_count += 1
                if narration_count == min_narration_block and active_show is not None:
                    # 触发：在 narration_start 行前插入 hide_all_chars
                    suggestions.append({
                        "line": narration_start + 1,  # 1-indexed
                        "indent": narration_indent,
                        "active_tag": active_show,
                        "preview": lines[narration_start].strip()[:80],
                        "block_size": 0,  # 后面补
                    })
                    # 标记已建议过这一段，避免同块重复触发
                    # 把 active_show 清空表示本块已处理
                    active_show = None

        # kind == "skip" / "other" : 不改状态
        i += 1

    return suggestions


def main():
    files = sys.argv[1:] if len(sys.argv) > 1 else TARGET_FILES_DEFAULT
    total = 0
    for fname in files:
        path = os.path.join(GAME_DIR, fname)
        if not os.path.isfile(path):
            print(f"[skip] not found: {path}")
            continue
        sugs = scan_file(path)
        print(f"\n=== {fname}: {len(sugs)} 处建议 ===")
        for s in sugs:
            print(f"  L{s['line']}  (after show {s['active_tag']})  {s['preview']!r}")
        total += len(sugs)
    print(f"\nTOTAL: {total} 处")


if __name__ == "__main__":
    main()

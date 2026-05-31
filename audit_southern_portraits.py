# -*- coding: utf-8 -*-
"""
南境 DLC 立绘状态机审计(只报告, 不改文件)。
精确解析 scene / hide_all_chars(参数) / hide / show ... at <side>, 追踪每个立绘的站位,
对每句对话检查:
  [缺show]  说话人立绘不在屏(会显示残留/张冠李戴)
  [重合]    同一侧(left/right)同时挂着 >1 个立绘(叠加)
注意: 不精确处理 menu/if 分支(顺序扫描), 分支处可能有少量误报, 已尽量标注。
"""
import os, re
import fix_missing_portraits as F

TARGET = os.path.join(os.path.dirname(__file__), "game", "southern_expansion.rpy")
char_map = F.collect_character_defs()  # speaker -> img_tag (例如 player->player_char_img)

SCENE_RE   = re.compile(r'^\s*scene\b')
HIDEALL_RE = re.compile(r'hide_all_chars\(([^)]*)\)')
HIDE1_RE   = re.compile(r'^\s*hide\s+(\w+_img)\b')
SHOW_RE    = re.compile(r'^\s*show\s+(\w+_img)\b')
AT_RE      = re.compile(r'\bat\s+(\w+)')
DIALOG_RE  = re.compile(r'^(\s*)([a-z_]\w*)\s+"')

def speaker_tag(speaker):
    v = char_map.get(speaker)
    if not v:
        return None
    img = v[0] if isinstance(v, (list, tuple)) else v
    return img if img.endswith("_img") else img + "_img"

with open(TARGET, encoding="utf-8") as f:
    lines = f.readlines()

onscreen = {}   # tag -> side
issues = []

for i, line in enumerate(lines, 1):
    if SCENE_RE.match(line):
        onscreen = {}
        continue
    m = HIDEALL_RE.search(line)
    if m:
        keep = set(re.findall(r'"(\w+_img)"', m.group(1)))
        onscreen = {t: s for t, s in onscreen.items() if t in keep} if keep else {}
        continue
    m = HIDE1_RE.match(line)
    if m:
        onscreen.pop(m.group(1), None)
        continue
    m = SHOW_RE.match(line)
    if m:
        at = AT_RE.search(line)
        onscreen[m.group(1)] = at.group(1) if at else "center"
        continue
    m = DIALOG_RE.match(line)
    if m:
        speaker = m.group(2)
        tag = speaker_tag(speaker)
        if not tag:
            continue
        if tag not in onscreen:
            issues.append((i, "缺show/残留", speaker, "屏上: " + (", ".join(onscreen) or "空")))
        sides = {}
        for t, s in onscreen.items():
            sides.setdefault(s, []).append(t)
        for s, ts in sides.items():
            if len(ts) > 1:
                issues.append((i, f"同[{s}]重合", speaker, " + ".join(ts)))

print(f"=== 审计结果: {len(issues)} 处疑似问题 ===\n")
for lineno, kind, speaker, detail in issues:
    txt = lines[lineno-1].strip()[:30]
    print(f"L{lineno:<5} [{kind}] 说话人={speaker}  {detail}")
    print(f"       > {txt}")

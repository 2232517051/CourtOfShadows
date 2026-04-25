# CourtOfShadows — 开发规范

## 立绘 show 指令规范（强制）

每新增一处 `show XXX_img at left` 都必须**同时完成**：

1. **前面紧跟 `$ hide_all_chars("XXX_img")`** — 防叠加。
   唯一例外：前一行已是 `scene bg ...`（scene 会清所有立绘）。
2. **CHAR_IMG_TAGS 里有 `XXX_img`**（`game/char_helpers.rpy`）— 否则 `hide_all_chars` 遍历不到，清不掉它。
3. **Character 的 image 参数与 img tag 对齐**（`game/characters.rpy`）— `Character(..., image="XXX")` 必须让 `XXX_img` 存在于 `images_def.rpy`，且该角色所有台词位置都是 show 的同一个 tag。不要让 Character 期望 tag A，代码 show tag B。

双人同屏例外：`show ... at right` 不加 `hide_all_chars`（全项目 121 处 at right，其中 14 处是 A+B 同屏对话，callback 方案会毁它们）。详见 `feedback_cos_hide_all_chars` 记忆。

## 每次改完剧本必跑（强制，不能跳过）

**无论改动多小**（加一行叙事文本、改一个台词、插一段选项），完成后都必须跑下面三步，全部归零才算完成：

1. **`python scan_missing_portraits.py`** — 检查"对话行缺 show"。期望 `Total findings: 0`。有遗漏跑 `python fix_missing_portraits.py` 自动补，再跑 scan 确认。

2. **`python scan_narration_overlap.py`** — 检查"show 之后紧跟 ≥2 行连续旁白导致前一角色立绘残留"。期望 `TOTAL: 0`。有遗漏跑 `python fix_narration_overlap.py` 自动在旁白段前插入 `$ hide_all_chars()`。**注意**：插入 hide 后，原"同说话人继续说"的位置会变成缺 show —— 必须**重跑步骤 1 + 2 一轮**（先跑 scan_missing_portraits，有结果就 fix_missing_portraits；再跑 scan_narration_overlap，有结果就 fix_narration_overlap；来回迭代直到两者都 0）。

3. **手工扫 show 前防叠加覆盖** — 上两个工具不覆盖的兜底。用这段 Python 跑一遍改动过的文件：

```python
import re
from pathlib import Path
for path in ["game/xxx.rpy"]:  # 改成实际改过的文件
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines):
        m = re.match(r'^(\s*)show\s+(\w+_img)\s+at\s+left\b', line)
        if not m: continue
        j = i - 1
        while j >= 0 and (not lines[j].strip() or lines[j].strip().startswith("#")): j -= 1
        prev = lines[j].strip() if j >= 0 else ""
        if not re.match(r'^(\$\s*hide_all_chars\s*\(|scene\s+bg\b|hide\s+\w+_img)', prev):
            print(f"{path}:L{i+1}  show {m.group(2)}  prev={prev!r}")
```

期望无输出。

## 为什么三步都要跑

- `scan_missing_portraits` 查"该 show 没 show"（演员没上台）
- `scan_narration_overlap` 查"show 之后连续旁白没清场"（演员下台了但立绘还挂在墙上）
- 手工扫描查"show 前没清场"（新演员压在旧演员身上）

三者是正交问题，只跑其中一个会漏。典型 bug：ch2_council 里"男爵说完话 → 两行旁白描述其他领主反应 → 男爵立绘仍在"——这正是 `scan_narration_overlap` 捕获的盲区。

## 改了 Character / 立绘资源 / CHAR_IMG_TAGS 时额外补一步

- 新增/改名角色立绘：同步更新 `CHAR_IMG_TAGS`（`char_helpers.rpy`）、`images_def.rpy` 的 image 声明、`_all_portrait_chars` 列表、`characters.rpy` 的 `image=` 参数——四处必须对齐。scan 脚本的 `MANUAL_IMG_TAG` 字典如涉及也要加。

## 不要做

- 不要用 `config.all_character_callbacks` 自动清立绘 — 毁双人同屏。
- 不要在 `at right` 前加无 except 的 `hide_all_chars()` — 会清掉 at left 的对方。

# CourtOfShadows — 开发规范

## 写新剧情前必读（强制）

任何写新章节 / 改对话 / 加旁白 / 设计选项前，先读这两份：

1. **`CANON.md`** — 人物 / 时空 / 物品 / 跨作品事实表。重名角色、家族徽章、毒药名、卫队兵力、跨作品时间轴。
2. **`FORBIDDEN_PHRASES.md`** — A/B/C/D/E 五大类禁用句式 + 写前/写后自检清单。

**新剧情写完后必须跑两个扫描**（跟改完剧本必跑那三步并列）：

```bash
python Tools/scan_ai_smell.py   # 扫 AI 味 (粗筛, 误报多, 对照 FORBIDDEN_PHRASES.md 人工确认)
python Tools/scan_canon.py      # 扫反逻辑 + canon 偏差 + 触发词频次
```

玩家每抓一个新模式 / canon 错误，按 `CANON.md` 和 `FORBIDDEN_PHRASES.md` 末尾"加新条目"格式追加。**清单只增不减**。

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

## 发布 / 打包 / wx build 之前必跑（强制）

**`python prepare_release.py`** — 验证 `game/msyh.ttf` 字符集与当前 .rpy 内容一致。

- exit 0 = 字体已最新, 可以 build
- exit 1 = 有新字, 已自动重生成, 必须 commit `game/msyh.ttf` 后重新 build
- exit 2 = subset_font.py 失败, 排查后再试

**Why**: pre-commit hook 只在 commit 时刷字体。如果 build 流程从 working tree 直接打包（典型: 第三方 wx 转换工具），最近一次没 commit 触发就漏了——玩家会看到方框/缺字（栀子 2026-05-01 反馈正是此因，"踞"字旧字体没有）。

## 改了 Character / 立绘资源 / CHAR_IMG_TAGS 时额外补一步

- 新增/改名角色立绘：同步更新 `CHAR_IMG_TAGS`（`char_helpers.rpy`）、`images_def.rpy` 的 image 声明、`_all_portrait_chars` 列表、`characters.rpy` 的 `image=` 参数——四处必须对齐。scan 脚本的 `MANUAL_IMG_TAG` 字典如涉及也要加。

## 不要做

- 不要用 `config.all_character_callbacks` 自动清立绘 — 毁双人同屏。
- 不要在 `at right` 前加无 except 的 `hide_all_chars()` — 会清掉 at left 的对方。

## Claude Code 工作流强制约束

**2026-07-11 用户新令（覆盖旧的"先报告等审"模式）: "之后有问题直接修，不进待修。"**

1. **发现问题直接修, 不积压 backlog / 待修清单**。修完必须: 跑上面的三步扫描 + lint → 当场 commit → 在回复里报告改了什么和为什么。
2. **例外仍要先问用户**: 破坏性操作（删内容/重做系统）、方向二择（两种改法差异大）、需要真机 playtest 才能定的数值手感。
3. **每次落盘后立即跑 `git status`**, 发现工作区累积超过 1 个未 commit 主题立即停下来 commit 或报告拆分。
4. **"调研不改代码"指令必须严格遵守** — 用户明确说只调研时, 任何"我顺手修了"都视为越界。

（历史背景: 旧规则源自栀子 T+8 批的失控教训——积压 7 件未 commit、6 项 bug 未审 diff。新令解决的是反向问题: 待修清单越积越长。核心不变: 小步 commit、修完可追溯、报告透明。）

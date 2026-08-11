# 终章崩盘战死修复设计

日期：2026-08-11

## 背景与目标

玩家反馈指出：即使一路选择背叛、独断、耗尽钱财并失去支持，主角仍可能凭一项较高的权力值进入“铁腕领主”，甚至用几百人赢下统一战争；玩家无法通过这种明确的自毁路线让主角死亡。

现有行为由两个互相独立的规则造成：

1. 普通难度允许最高主属性达到 55 时开放保底主路线，因而 `power=55` 足以显示铁腕路线。
2. 铁腕会战把 `power >= 60` 等同于“准备充分”，准备分支即使分数不足也只会惨胜；财富、军心和实际支援同时崩盘不会否决这个结果。

死亡又只由危机系统累计三次伤势触发。终章会战失败进入的 `fall` 结局只写“领主下落不明”，没有确认主角死亡。

本次修复的目标是：**残暴不是自动死刑，但资源、军心和援军同时崩盘后仍强行开战，必须战败；艾登堡陷落结局必须明确主角死亡。**

## 不在本次范围内

- 不增加“恶行值”或新的道德惩罚系统。
- 不全面重平衡四项主属性、九个结局门槛或所有会战分数。
- 不改变 `fall` 的持久化结局键、成就 ID、画廊入口或结局数量。
- 不把终章战死写入 `crisis_injuries`，也不改变危机系统的三伤死亡规则。
- 不重写整个铁腕结局或扩展尾声。
- 不更新商店页、版本号或发布公告；这些留到实际发版流程处理。

## 方案比较

### 方案 A：增加“终末崩盘”硬门槛（采用）

在会战规则中加入一个纯判定：财富与忠诚都低于最低生存线，并且没有任何可执行的组织、后勤或外部保障时，军队已经失去继续作战的物质与组织基础。权力值、临时战术分或“准备充分”不能覆盖这个状态。

优点是直接对应玩家反馈，改动集中，并保留“残暴但经营有方”的铁腕路线。缺点是存在明确边界，因此必须用临界值测试锁定。

### 方案 B：全面重算战争分数

给低财富、低忠诚和关系破裂加入连续扣分，并让所有战术都使用统一胜负阈值。曲线更平滑，但会改变大量既有存档的可达结局，需要重新调试整套终章平衡，不适合作为这次玩家反馈的窄修。

### 方案 C：累计“最差选择”或恶行次数

记录背叛、贪婪和鲁莽选择，达到次数后强制死亡。它能直接惩罚“每次都选最坏”，但会把道德判断重复编码在新系统里，也会误伤有意识扮演暴君但经营成功的玩家，因此不采用。

## 行为合同

### 终末崩盘判定

新增纯函数 `is_terminal_resistance_collapse(...)`。只有以下条件全部成立时返回真：

- `wealth < 20`；
- `loyalty < 20`；
- 没有建成能让全领地储粮、让城堡继续支撑两至三个月的谷仓：`built_granary` 为假；
- 没有男爵正式盟约：`alliance_baron` 为假；
- 玩家没有在当前终章选择让男爵实际加入会战：`baron_joined` 为假；
- 没有仍然有效的王子盟友：`prince_ally and not prince_betrayed` 为假；
- 雷恩关系不足以形成精锐死忠：`rel_captain < 60`；
- 没有提前发放阵亡抚恤：`ch5_pay_advance_pension` 为假；
- 没有北疆婚约卫队：`marriage_route` 为假；
- 没有掌控铁刺网：`iron_thorn_controlled` 为假。

`baron_supply_intel` 只代表一条情报，不是能够维持军队的成建制支援，因此不能单独解除崩盘。`built_granary` 只解除这条硬性崩盘否决，不直接增加战争分数，也不保证获胜。

这是一条与难度无关的逻辑底线：简单难度仍会放宽属性变化和普通会战阈值，但不会让一支同时断粮、失去军心且无人支援的军队凭领主个人权势自动获胜。

### 路线与会战

- `get_finale_route_availability()` 保持不变。符合现有权力门槛的玩家仍能看见并选择铁腕路线；选择不会被系统悄悄隐藏。
- `get_resistance_battle_outcomes()` 在枚举每个最终会战状态时调用纯崩盘判定。它必须让每个计划状态携带 `rel_captain`：山路绕后先应用 `-10`，随后亲自率领前锋再应用 `-12` 或委派雷恩应用 `+4`。这些变化使用独立的纯关系变更助手，精确复现 `change_rel` 的难度倍率、非零补偿与 `[-100, 100]` 钳制，但不套用属性专用的递减收益。
- 纯推演显式接收 `built_granary`、`prince_betrayed`、`iron_route_available` 与 `resist_route_available`。只在 `iron_route_available=True` 时枚举 `baron_joined=False` 的直接铁腕入口，只在 `resist_route_available=True` 时枚举 `baron_joined=True` 的男爵入口；两者都可见时才合并两类可达结果，不能虚构正式菜单没有显示的入口。正式会战与纯推演原有的王子战争分数也统一改为只在 `prince_ally and not prince_betrayed` 时生效。崩盘状态只能产生 `fall=True`，不能产生 `iron_lord=True`。
- `get_finale_ending_availability()` 必须区分“战斗路线可见”和“战斗结局可达”。只要 `iron_lord` 或 `resist` 路线可见，映射器就以 `resistance_outcomes` 作为 `iron_lord` 与战斗失败 `fall` 的唯一裁决；可见的 `routes["iron_lord"]` 本身不再直接产生铁腕结局。
- 战斗路线可见但调用者没有提供 `resistance_outcomes` 时，映射器抛出明确的 `ValueError`，而不是按路线可见性返回假阳性。没有战斗路线时，非战斗结局映射仍可省略该参数。
- 正式剧情在第一次打开最终战术菜单前，用同一个当前状态包装函数计算并锁定 `iron_terminal_collapse_snapshot`。此时已经包含此前“亲征/委派”等选择造成的状态变化，但尚未包含最终战术自身对 `loyalty` 或 `rel_captain` 的增减。
- 崩盘时不显示三项“准备充分”战术，只显示“硬拼——你没有更好的选择了”。每个最终战术分支还必须在写入本分支的忠诚/关系变化之前，以“尚未锁定则计算”的方式取得该值；取得后若为真就立即跳到 `ironlord_battle_lost`，不能先播放该准备战术的胜利文本。这样兼容直接恢复在旧版菜单上的存档。
- 玩家点击“硬拼”后，锁定的崩盘状态优先于 `iron_war_score`，直接进入 `ironlord_battle_lost`。临时加出的分数不能覆盖崩盘。
- 所有战术分支汇合后、进入胜利正文前再执行一次共同守卫；值为真时跳败，值为假时继续，且不得用最终战术造成的新忠诚/关系值重新分类。旧存档若已经越过新增的分支前锁定点而使值仍为 `None`，守卫保留该存档已经选择的旧版结果而不重新裁决；这是为了避免在无法恢复准确菜单前状态时误杀本来不崩盘的旧档。新流程与停在旧菜单的存档都必须在抵达汇合点前得到非 `None` 值。
- 非崩盘状态继续使用现有 `_iron_prepared` 与战争分数规则，不调整各战术阈值。

### 失败与死亡

所有进入 `ending_fall` 的路径都使用同一个明确结局：城堡大厅被攻破，主角持父亲的剑作最后抵抗并在大厅内战死。

- 删除“领主下落不明”的歧义结果。
- 保留标题“艾登堡陷落”、`fall_ending` 成就和 `persistent.endings_seen.add("fall")`。
- 不设置 `crisis_injuries=3`，因为这次死亡来自终章战败，不是危机伤势累计。
- 新增普通存档字段 `fall_cause`，只区分三种正文入口：主动放弃抵抗写入 `"inaction"`，终章会战惨败写入 `"battle"`，旧存档缺失或空值使用不指责玩家动机的中性版本。它不是 persistent 字段，也不改变结局键。
- `ending_fall` 与 `game_ending` 的结局摘要按 `fall_cause` 选择经批准的短文本：`inaction` 可以保留“本可做得更多”的责问，`battle` 必须描述强行发动绝望战争后的失败，空值不得虚构玩家“什么也没做”。
- 仍然执行现有第三人称的 `ending_fall_epilogue`；进入 `fall` 后不再执行通用 `ending_side_characters_fate`，避免主角已经战死后又出现“你后来听说、保留物件或打听消息”等活人视角行为。

## 组件与数据流

### `game/difficulty.rpy`

该文件继续作为终章可达性和纯会战推演的事实来源：

1. `is_terminal_resistance_collapse(...)` 只读取显式参数，不读取 `store`。
2. `is_current_terminal_resistance_collapse()` 用 `getattr(store, ..., safe_default)` 收集当前存档状态，并以实际 `resist_route` 作为 `baron_joined`，再调用纯函数。
3. `get_resistance_battle_outcomes(...)` 复用纯函数并携带每一步关系变化，只按 `iron_route_available`/`resist_route_available` 枚举正式菜单真实显示的入口，保证开发者结局预览与正式剧情一致。
4. `get_current_resistance_battle_outcomes()` 先取得当前路线映射，再把 `routes["iron_lord"]` 与 `routes["resist"]` 分别传给纯推演，避免用男爵关系猜测玩家能否直接进入铁腕路线或是否真的选择了并肩作战。
5. `get_finale_ending_availability(...)` 把路线视为入口、把会战结果视为战斗结局事实；战斗路线存在而结果缺失时明确失败。

### `game/chapter5.rpy`

正式会战只调用 `is_current_terminal_resistance_collapse()`，不复制条件列表。非保留名的普通存档字段 `default iron_terminal_collapse_snapshot = None` 表示本次最终战术尚未锁定；每次进入本场会战的新流程时先重置为 `None`，第一次显示最终战术菜单前计算一次，各分支在修改忠诚/关系前执行同一“缺失才计算、崩盘则立即跳败”的动作，汇合后的胜利前守卫只读取锁定值。直接铁腕路线中 `rel_baron > 0` 的现有可见对白改为男爵保持中立、不会背刺，不再声称已带近四百人参战；原有 `+4` 中立收益保留，但不解除硬崩盘。`ironlord_battle_lost` 写入 `fall_cause = "battle"`，主动放弃抵抗的既有入口写入 `fall_cause = "inaction"`。`game_ending` 保留 fall 专属尾声，但从通用角色命运段落的调用条件中排除 `fall`。

### `game/test_game.rpy`

测试同时覆盖纯结果图和真实 Ren'Py 菜单跳转。玩家反馈中的普通难度路线必须成为稳定回归用例，而不是只测试原有的“困难、权力为零”失败夹具。

## 旧存档兼容

- 不删除或重命名任何 label。
- 新增的都是非保留名普通 `default` 存档字段：`iron_terminal_collapse_snapshot = None` 与 `fall_cause = ""`；不新增 persistent 字段或结局键。旧存档缺少字段时按这两个默认值工作。
- 当前状态包装函数对其他可选字段继续使用 `getattr(store, ..., safe_default)`；永久回归测试必须临时删除并恢复这些可选字段，证明旧存档不会因缺少新增或历史变量而崩溃。
- 旧存档可能直接恢复在最终战术菜单，因此不能只依赖菜单前赋值。兼容验证分成两层：一次性本地证据在基线提交上用隔离 `SaveDir` 和 Ren'Py 自带 testcase 自动生成真实旧版存档（停在最终战术菜单、带旧 `_iron_prepared=True`，但资源与支援满足终末崩盘），记录基线提交、存档哈希、可复现步骤与改后加载结果；该二进制和运行记录只作 git-ignored 证据，不进入常规测试或提交。可提交的永久回归则用 testsuite 夹具模拟相同恢复状态：`_iron_prepared=True`、`iron_terminal_collapse_snapshot=None`，选择准备分支后必须在播放胜利文本前进入 `fall`。
- 对已经保存在准备分支正文内部、因而越过新增锁定点的旧档，只承诺可加载且维持它已选择的旧版胜负，不做无法可靠重建菜单前忠诚/关系值的追溯判死。永久夹具必须覆盖“汇合点收到 `None` 时不崩溃、不重新分类”；完成标准中的旧存档兼容只指无崩溃、旧菜单选择可被新规则拦截，不宣称分支中途存档会被追溯改判。
- 已经进入 `game_ending` 或已经解锁的 `fall`/`iron_lord` 记录不回滚。

### 无桌面接管的一次性旧档门禁

一次性旧档门禁不能使用 `Run-RenPySuite.ps1 -StageLegacyFixtures`，因为该开关只搬运仓库内 winter manifest；也不能调用 Computer Use、发送真实鼠标或键盘事件、抢占前台窗口，或在后台失败后回退为人工桌面操作。实施计划必须给出并保存以下同等严格的本地步骤。

1. **基线生成器。** 在修复前精确基线提交的独立 detached worktree 中，只临时新增一个 `game/zz_terminal_collapse_legacy_fixture.rpy`，不得修改生产脚本。使用仓库外、玩家存档外的唯一空 `SaveDir`；worktree 内的 `game/saves` 也必须不存在或是本轮任务拥有的空目录，否则停止，防止 Ren'Py 在多个 save location 之间选错文件。生成与回载保持同一个本机用户和 Ren'Py save-token 身份，不改 `RENPY_PATH_TO_SAVES`。临时 testcase 先写入计划锁定的原始 primitive 状态，再以 `run Start("ending_iron_lord")` 让生产 label 成为顶层游戏执行流；禁止用 `call`、`call_in_new_context` 或夹具 driver label 给存档留下临时返回点。
2. **真实分支推进。** testcase 通过 Ren'Py 引擎自己的 `click`/`advance` 依次选择“截断补给线——让他们饿三天再打”“亲自率领前锋出击”“记住这一切，继续前进”，不得直接写入这三项选择的结果状态。停在最终战术 `screen choice` 且尚未选择最终战术时，必须断言 `intrigue == 55`、`power == 60`、`_iron_prepared is True`，并从 `screen choice` 的实际 `items` 中证明“正面强攻”和“迂回”各出现一次、硬拼不出现。
3. **执行栈与存档。** 保存前必须断言当前是顶层 context、`return_stack` 为空、当前脚本位置属于 `game/chapter5.rpy` 的最终战术 Menu，而不是 testcase 或 `zz` 文件；随后才调用 `renpy.save("1-1", ...)`。退出后要求恰有一个 `1-1-*.save`，并核对 slot JSON 的基线提交、三项选择、菜单位置和状态标记。
4. **零可见窗口。** 生成、干净回载和改后双分支回放的子进程都只在各自进程环境中设置 `SDL_VIDEODRIVER=dummy`、`SDL_AUDIODRIVER=dummy` 与 `RENPY_RENDERER=sw`。启动器必须分别捕获 stdout/stderr、PID、真实退出码，并在整个生命周期检查该进程树没有可见顶层窗口。dummy 后端不能渲染真实 choice、检测到任何可见窗口、需要未知 save-token 确认或出现其他交互时，立即停止本次门禁并报告 `NEEDS_CONTEXT`；不得改用桌面控制继续。
5. **干净基线回载。** 在第二个精确基线 detached worktree 中确保生成器 `zz` 文件不存在，只允许一个不写游戏状态的临时验证观察器，并对其 `game/saves` 执行同样的不存在/任务自有空目录断言。把候选 slot 复制到新的唯一空 `SaveDir`，复核复制前后哈希，并以正常 `run`（不是 `test`）配合 `RENPY_AUTO_LOAD=1-1` 自动加载。观察器只在正式 choice interaction 出现后核对当前文件/菜单、空返回栈、上述状态、两个最终战术选项，以及当前 slot JSON 中候选独有的 provenance marker；然后写出结果并退出。任何未知 label、incompatible script、未知 token、确认框、夹具依赖或 marker 不匹配都使候选作废。
6. **冻结与改后回放。** 只有干净基线正常回载通过后，才把原始引擎文件复制成只读的 git-ignored 证据母本，并记录基线提交、引擎版本、文件字节数与 SHA-256。改后验证绝不直接打开母本，而是为“正面强攻”和“迂回”各建一个仓库外唯一空 `SaveDir`，分别以引擎原始文件名复制同一母本并再次核对源/两份副本哈希相等；每个回放 worktree 的 `game/saves` 同样必须不存在或为任务自有空目录。两个 dummy-mode testcase 分别加载一个副本，先核对 provenance marker，再选择对应分支，并证明都在胜利文本前进入 `fall`。
7. **证据与清理。** 保存生成、干净回载和两次改后回放的日志、环境、PID、窗口检查、退出码、状态断言与结果说明。只有确认目标位于本轮任务拥有的临时根、相关进程树全部退出后，才能清理 disposable worktree 和副本 `SaveDir`；ignored 母本与证据保留到设计复审结束。中断或失败尝试的日志与存档不得被后续尝试覆盖或冒充通过证据。

## 正文生成与审批边界

死亡段落、`fall_cause` 三种入口摘要、为避免战死后活人视角而调整的衔接句，以及直接铁腕路线中把“男爵带兵联手”更正为“保持中立、不背刺”的对白，都属于新的可见游戏正文，必须遵守现有游戏文案流程：

1. 在实施阶段读取 `CANON.md`、当前 `ending_fall` 连续上下文、写作风格索引及与终章死亡场景直接相关的已批准样本。
2. 因当前文风库仍处于 seed 阶段且没有活动正例，分别启动三个彼此隔离的全新 Claude Code 会话并锁定 `/model claude-opus-4-6`。每个会话只收到同一份当前场景事实、角色状态和必须明确死亡的结果，不提供 Codex 草稿、其他候选或被拒绝文本。
3. 分别保存并核验三份原始 Opus 输出及各自模型元数据；候选生成完成前不得让任何会话看到另外两份文本，也不得由 Codex 混写或润色。
4. 随机打乱三份候选并用不暴露模型、生成顺序的中性编号完整展示给用户盲选；用户可以选择一份或全部拒绝。在改动 `game/chapter5.rpy` 前必须取得明确批准。
5. 只把用户批准候选中的短段落与入口变体原样接入现有 `ending_fall`/`game_ending`；不得拼接不同候选，也不借机重写整段结局或安全的 `ending_fall_epilogue`。

## 测试策略

严格执行红灯到绿灯：先让玩家反馈路线在当前实现下失败，再修改生产逻辑。

### 纯规则测试

- 普通难度、`power=55`、`wealth=0`、`loyalty=0`、男爵敌对且所有支援为假时，铁腕路线仍可见，但可达结局必须是 `iron_lord=False, fall=True`。
- 现有 `primary_routes_use_configured_thresholds` 与 `easy_normal_hard_boundary_route_sets_are_identical` 等测试拆开“路线门槛”和“结局可达”断言：权力达到门槛只证明铁腕入口可见；铁腕最终可达必须同时传入对应的会战结果。
- 用 `rg -n "get_finale_ending_availability\(" -g '*.rpy' -g '*.py' .` 审计并迁移所有调用者：任何可能传入可见 `iron_lord`/`resist` 路线的单参数调用都必须补充会战结果，不能只修一个已知测试；确认只映射非战斗特殊路线的调用才可继续省略。
- 用 `rg -n "get_resistance_battle_outcomes\(" -g '*.rpy' -g '*.py' .` 审计并迁移所有纯会战调用者。新增的 `iron_route_available` 与 `resist_route_available` 是必填关键字参数，不提供会静默返回空结果的宽松默认；从结局映射进入的调用必须传对应 route map，独立会战夹具也必须显式声明自己模拟的是直接铁腕、男爵加入或两者并存。
- 战斗路线可见但省略 `resistance_outcomes` 时必须抛出 `ValueError`；非战斗路线的既有映射保持可用。
- `wealth=20` 或 `loyalty=20` 任一达到边界时，不得被“终末崩盘”强制判死；其余会战规则照常决定胜负。
- 财富与忠诚都低时，`built_granary`、正式男爵盟约、实际选择男爵并肩、未背叛的王子盟友、雷恩精锐、提前抚恤、北疆婚约卫队或铁刺网控制中任一项可以解除硬性崩盘，但不保证必胜，仍需满足原有战争分数规则。
- `prince_ally=True, prince_betrayed=True` 不得解除崩盘，也不得获得原有的王子战争分数。
- `rel_baron == 0` 且只有男爵抵抗路线可见时，纯推演只能枚举 `baron_joined=True` 的男爵入口；只有铁腕路线可见时只能枚举 `baron_joined=False` 的直接入口；两条路线同时可见时才合并两类结果。正式包装函数仍只在当前 `resist_route=True` 时把实际会战判定为 `baron_joined=True`。
- `rel_baron > 0` 本身也不等于成建制支援；在没有正式盟约且玩家未实际加入男爵路线时，不能单靠好感解除崩盘。
- 只有 `baron_supply_intel=True` 时仍属于崩盘。
- `built_granary=True` 解除硬崩盘但不自动增加战争分数，并用低分夹具证明仍可能按原规则失败。
- 山路绕后、亲自率领前锋与委派雷恩造成的难度调整后 `rel_captain` 变化必须按发生顺序进入纯推演；在阈值两侧设置夹具，证明独立关系助手与正式 `change_rel` 使用相同的难度倍率、非零补偿和钳制，且崩盘使用相同的菜单前状态。
- 最终战术自身造成的 `loyalty`/`rel_captain` 变化发生在锁定之后，不能把同一场会战从崩盘重新分类为非崩盘，或反向重新分类。
- 简单、普通、困难三档使用同一崩盘逻辑。

### 真实剧情测试

在 `test_resistance_battle_transition` 中增加普通难度玩家反馈夹具并执行精确路线：

1. 截断补给线；
2. 亲自率领前锋；
3. 记住这一切，继续前进；
4. 硬拼。

测试必须证明最终菜单没有准备分支、点击硬拼后进入 `ending_type == "fall"`，并且不会继续到铁腕胜利段落。另保留现有困难难度低分失败测试，并增加可提交的旧菜单状态夹具：分别以 `_iron_prepared=True`、`iron_terminal_collapse_snapshot=None` 进入可与崩盘同时存在的“正面强攻”和“迂回”准备分支，必须在该分支写状态或播放胜利文本之前跳到 `ironlord_battle_lost`；汇合处共同守卫仍作为第二道断言。真实二进制旧存档只在前述一次性兼容门禁中加载，不作为干净检出的常规测试依赖。

新增真实 Ren'Py testsuite `test_terminal_collapse_ending`，从上述会战路线推进到 `ending_fall` 中用户批准的唯一死亡句，证明实际 label 跳转而不只是提前看到 `ending_type == "fall"`。setup 先快照 `persistent.gallery_unlocked` 并预置 `bg_battlefield`，避免进入铁腕会战时既有 `unlock_gallery` 产生无关增量；测试在死亡句之后、`unlock_achievement("fall_ending")` 与 `jump game_ending` 之前停止，因此 achievements、endings、chapters、NG+ 与 rating 均不得增加，也不能出现铁腕胜利副作用。setup/teardown 必须快照并恢复相关 store 字段、`persistent.achievements`、`persistent.endings_seen`、`persistent.chapters_completed`、`persistent.gallery_unlocked`、难度、NG+ 字段与 `rating_asked`，最后返回主菜单并恢复持久化状态。

### 正文合同测试

- `ending_fall` 不再包含“领主下落不明”。
- 批准的死亡句必须只在 `ending_fall` 的结局收束位置出现一次。
- `fall_ending` 成就、`fall` 持久化键和 `game_ending` 跳转保持不变。
- `fall_cause` 的 `inaction`、`battle` 与旧存档空值分别命中已批准的责问、战败和中性文本；战死路线不得再进入包含活人第二人称行为的通用 `ending_side_characters_fate`，但必须保留安全的 `ending_fall_epilogue`。
- 直接铁腕且仅 `rel_baron > 0` 的部署段不得再出现“联手、近四百人、北坡汇合”等实际增兵陈述；批准的新文本只能表达男爵中立或不背刺，并保留原 `+4` 中立收益的语义。

## 验证范围

实施完成后至少执行：

- 新增的纯规则聚焦测试；
- `python -B -m unittest discover -s Tools -v`，并核对非零发现数、唯一 `Ran N tests`、终态 `OK` 与真实退出码；
- `python scan_missing_portraits.py`；
- `python scan_narration_overlap.py`；
- 改动段落的 `show ... at left` 前置清场检查；
- `python Tools/scan_ai_smell.py`；
- `python Tools/scan_canon.py`；
- `python Tools/test_release_regressions.py`；
- 仓库根目录的 `python prepare_release.py`；
- `git diff --check`；
- 测试后确认没有遗留 Ren'Py/Python 子进程，工作树只包含计划授权路径。

Ren'Py 门禁必须从仓库根目录在 Windows PowerShell 中按下列完整形态执行；`New-TerminalCollapseSaveDir` 每次只返回一个仓库外、玩家存档外且尚不存在的唯一路径，因此五次调用互不复用：

```powershell
$ProjectRoot = (Resolve-Path -LiteralPath '.').Path
function New-TerminalCollapseSaveDir([string]$Name) {
    return Join-Path ([IO.Path]::GetTempPath()) ("cos-terminal-collapse-{0}-{1}" -f $Name, [Guid]::NewGuid().ToString('N'))
}

& powershell.exe -NoProfile -File .\Tools\Run-RenPySuite.ps1 -ProjectRoot $ProjectRoot -SaveDir (New-TerminalCollapseSaveDir 'catalog') -Mode Suite -Suite test_ending_catalog -Expect PASSED -TimeoutSeconds 120
if ($LASTEXITCODE -ne 0) { throw 'test_ending_catalog failed.' }

& powershell.exe -NoProfile -File .\Tools\Run-RenPySuite.ps1 -ProjectRoot $ProjectRoot -SaveDir (New-TerminalCollapseSaveDir 'transition') -Mode Suite -Suite test_resistance_battle_transition -Expect PASSED -TimeoutSeconds 180
if ($LASTEXITCODE -ne 0) { throw 'test_resistance_battle_transition failed.' }

& powershell.exe -NoProfile -File .\Tools\Run-RenPySuite.ps1 -ProjectRoot $ProjectRoot -SaveDir (New-TerminalCollapseSaveDir 'ending') -Mode Suite -Suite test_terminal_collapse_ending -Expect PASSED -TimeoutSeconds 180
if ($LASTEXITCODE -ne 0) { throw 'test_terminal_collapse_ending failed.' }

& powershell.exe -NoProfile -File .\Tools\Run-RenPySuite.ps1 -ProjectRoot $ProjectRoot -SaveDir (New-TerminalCollapseSaveDir 'full') -Mode Full -Expect PASSED -TimeoutSeconds 1800
if ($LASTEXITCODE -ne 0) { throw 'RenPy Full gate failed.' }

& powershell.exe -NoProfile -File .\Tools\Run-RenPySuite.ps1 -ProjectRoot $ProjectRoot -SaveDir (New-TerminalCollapseSaveDir 'lint') -Mode Lint -TimeoutSeconds 300
if ($LASTEXITCODE -ne 0) { throw 'RenPy lint failed.' }
```

每条命令都要保留 runner 生成的证据路径并核对真实退出码；不得在同一最终 SHA 上为了取得好看的结果重复长门禁。确认对应 PID 已退出后，才可按已验证的临时绝对路径清理各 `SaveDir`。

## 资源与包体

- 美术：不需要新增。继续使用 `castle_exterior`、`battlefield` 和黑场。
- 音乐：不需要新增。继续使用现有 `war_drums.ogg`。
- 音效：不要求新增；若批准正文需要撞门或兵刃声，只能优先复用现有音效，并由实现计划明确列出。
- 动画与 UI：不需要新增；复用现有淡入、黑场和 centered 结局卡。
- 字体：先让批准文案优先使用现有字形，再运行仓库根目录的 `python prepare_release.py` 验证。若 Opus 批准文本含当前子集缺失字形，允许按既有流程重新生成受跟踪的 `game/msyh.ttf`；在验证前不宣称字体零变化。
- 包体：不新增美术、音乐、音效、动画或 UI 二进制资源；唯一可能的二进制变化是字体子集。实施完成时必须测量并报告实际包体影响，而不是预先写成零。

## 完成标准

- 玩家反馈的普通难度自毁路线稳定进入艾登堡陷落，不能再达成铁腕领主。
- 只要财富、忠诚或一项组织性保障越过崩盘边界，系统就回到现有会战分数规则，不把残暴本身当作死刑。
- 路线可见性不再冒充结局可达性；开发者结局预览、正式菜单和实际跳转使用同一会战结果与崩盘事实来源。
- `ending_fall` 明确确认主角战死，同时保留原结局键、成就和旧存档兼容性。
- 新正文经过新鲜 Claude Opus 原稿展示与用户批准后才进入项目。
- 所有规定门禁取得本轮新鲜通过证据；美术、音乐、音效、动画和 UI 没有新增依赖，字体与最终包体变化以 `prepare_release.py` 和实际产物测量为准并明确报告。

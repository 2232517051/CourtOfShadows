# 终末崩盘旧存档生成器 Recovery v4：JSON-real 合同与全局单次准入设计

日期：2026-08-15

## 背景与目标

Recovery v3 已完成 controller、approval lock 与 Task 0，但 Task 1 在任何 generator/observer ledger、helper 或 Ren'Py 启动前终止。终止点位于 POST_PATCH 的静态正向控制：Windows PowerShell 5.1 把已封存 v2 `generator-state.json` 中 `_ctime` 与 `_game_runtime` 解析为 `System.Decimal`，而 P3 的 validator 错误地只接受 `System.Double`。P3 的人工正向样本又显式构造了 `[double]1.0`，因此没有在补丁前发现这个收窄错误。

同一次 v3 历史还包含一个 authority 异常：PRE_PATCH checkpoint 的 PTY ANSI 换行重绘被宿主辅助逻辑错误地拼成 65 位字符串并报告 `FAIL`，随后控制器改用物理 RED hash 继续。物理 RED seal 是明确的，但该恢复动作越过了 v3 retry authority 的“target 启动后首个 mismatch 即终止”边界。因此 v3 的 RED、补丁后 fixture 与报告只能作为失败历史封存，不能成为 v4 的执行源或被追认为干净 continuation。

Recovery v4 的目标是：

1. 冻结 P3/v3 的完整失败谱系，不改写、不清理、不提升；
2. 以新 S4、P4、M4、L4 和 `recovery-v4/` 命名空间建立全新 authority；
3. 修正 JSON real 的类型接口，并在任何 fixture patch 前用物理 v2 state 和独立 mutation controls 证明它；
4. 把显式用户执行授权与全局 Task 1 一次性机会合并成一个 prelaunch admission ledger，消除“尚未创建 process ledger，因此可以临时重试”的缝隙；
5. 在全新 worktree、SaveDir、ledger 与 evidence root 中各运行一次 generator 和 observer；
6. 成功后只从 v4 谱系冻结 mother，并把 Task 2、Task 3 与 Phase B 迁移到 v4 authority。

本规格只批准设计与后续计划编写。它不批准创建 M4/L4、执行 Task 0/1、启动 helper/Ren'Py/Opus、创建临时 worktree/SaveDir、修改 game 文件或清理任何旧路径。

## 已冻结事实

提交与树：

- P2：`25c2ea674948ad89e8b48befb89643a8687648a4`；
- S3：`5fa8fb14792e095e066c3e9f698eda9ea4380854`，直接父提交 P2；
- P3：`7365ae61c8d12dd0f34651a4bd727528cd9059d4`，直接父提交 S3；
- P2、S3、P3 的 `game` tree 均为 `fa7a398e9d989731b24e3c1642f3e2e33ce846ff`；
- S3 spec 为 41,497 bytes，SHA-256 `978116FE22B8C65578B78E800EF6039053284EA7E674271646D130BBB4BBF470`；
- P3 plan 为 866,433 bytes，SHA-256 `A8575EE1222E4A47A63C6FCBF9D0FE4EFDF5F78D7DD75DDDF17E40276E9432EF`。

v3 authority：

- L3：`.superpowers/sdd/terminal-collapse-ending/approved-plan-lock-v3.json`，2,354 bytes，SHA-256 `59D44AFD5562C735B81DE5429A9518E39754F6900EF8231F7B2C11C9653D626C`；
- M3：`.superpowers/sdd/terminal-collapse-ending/recovery-v3/predecessor-evidence.json`，45,507 bytes，SHA-256 `6DE89AAD17FFC00EB35FE5378444227BA5C8E1BCBF0C4657C9E1BF1FD55D2FBB`；
- M3 的 115 个 current artifact 全部仍匹配，catalog 为 24,660 bytes，SHA-256 `9694E728A82F6DDC743DA5E83967EAC7EE02FFA62FA53E21F4A2374F27DDDA24`；
- M3 的 115 项由早期 83 项、v2 authority/evidence 12 项、v2 worktree authority 8 项和 v2 SaveDir authority 12 项组成；
- v2 worktree 的 61 个 excluded cache leaf 与 SaveDir 的 0 个 excluded cache leaf 仍仅是 metadata inventory，不是 authority artifact，Task 1/2/3 不得读取、存在性探测或哈希它们。

v3 Task 1 失败现场：

- RED：`.superpowers/sdd/terminal-collapse-ending/recovery-v3/generator-contract-red.json`，2,693 bytes，SHA-256 `3FBC01339AD85FFA30D5CE3249501FD3A604EA499F9F56E6C9882AFD3A53476B`，只读；
- detached worktree：`E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-generator-recovery-v3`，HEAD=P3，唯一 untracked leaf 为 `game/zz_terminal_collapse_legacy_fixture.rpy`；
- 当前补丁后 fixture 为 8,845 bytes，SHA-256 `A0D2A8B0589CC64F9479CE8E5B3315760001AA965502D1D740D35C6A2D558381`；
- RED 中记录的是同一路径补丁前 8,749-byte fixture seal，因此 RED 是历史记录，不能拿其 input seal 去否定当前补丁后 leaf；
- Task 1 brief：`.superpowers/sdd/recovery-v3-task-1-brief.md`，375,208 bytes，SHA-256 `28324B08F0EBCE0C4A8FFBABEF220682EDA5AE409E5CD20BDB84553ABE0A0787`；
- retry authority：`.superpowers/sdd/recovery-v3-task-1-retry-authority.md`，2,315 bytes，SHA-256 `7595B856A4B6777DBDB42F6DD55C09490A3A698687341215C807257C5E5BA3FB`；
- 合并失败报告：`.superpowers/sdd/recovery-v3-task-1-report.md`，15,156 bytes，SHA-256 `7BE3F80E98DC121ADE9FC3D3AB5A06F5058E4834317FF8FAB6EDB69A5C1B2485`；
- v3 GREEN、generator/observer ledger、process evidence、state、SaveDir、completion、mother、baseline、Task 1 completion 与 rules 均不存在；
- v3 generator/observer invocation 为 0/0，helper 与 Ren'Py launch 为 0/0，没有 v3 candidate save。

受保护主 worktree 状态仍只能是未跟踪 winter plan：

`docs/superpowers/plans/2026-08-09-winter-interlude-narrative-delivery.md`

其 SHA-256 必须保持 `0F39B5F5ACE1D4666DD146863CABDF398B031F5666C29AE337CEB89796E4276C`。它不进入 M4 或 Task 1 artifact union。

## 根因与 JSON-real 术语

Windows PowerShell 5.1 `ConvertFrom-Json` 对物理 v2 state 中：

- `_ctime=1786694425.3440957` 产生 `System.Decimal`；
- `_game_runtime=15.528505802154541` 产生 `System.Decimal`。

同一 parser 对 JSON `1.0`/`0.0` 产生 `Decimal`，对 `1e0`/`0e0` 产生 `Double`。所以“JSON real”不能被错误等同为某一个 CLR 类型。

本规格的 JSON-real 定义是：反序列化后的值必须精确为 `System.Decimal`，或为 finite `System.Double`。`Double` 的 NaN、正 Infinity 与负 Infinity 均不是可接受值。任何整数类型、`Single`、字符串、布尔、null 或仅仅“可转换成数字”的对象都不是 JSON real。

数值范围固定为：

- `_ctime > 0`；
- `_game_runtime >= 0`；
- `+0` 和 `-0` 都按零处理，仅对 `_game_runtime` 可接受；
- 不增加日期上限或其他人为上限；
- Decimal 与 Double 必须在各自原生分支比较，禁止先 cast 到另一类型再判断。

## 不在本次范围内

- 不修改 S3、P3、L3、M3、v3 RED、v3 brief、retry authority、失败报告或补丁后 fixture；
- 不恢复、删除、移动、重命名、chmod 或清理 v3 worktree；
- 不从 v3 fixture 复制内容到 v4 worktree；P4 必须从自身已审核 appendix 重建批准 fixture；
- 不把 legacy、v2 或 v3 candidate/fixture 当作 mother、observer source、fallback 或运行输入；
- 不重新运行 full helper selftest 或 version probe；继续复用已封存通过证据；
- 不改变 dedicated-host helper、private-desktop wrapper、SafetyEnvelope、实际 exit 三方映射、窗口检测、Job drain、timeout 或 no-input 合同；
- 不改变 Task 2 的九次 invocation、14-field receipt 或 56-file union；
- 不改游戏文案、数值规则、剧情、UI、字体、图片、音乐、音效、动画、包体或存档格式；
- 不执行 Computer Use，不截图，不接管桌面，不发送真实输入。

## 方案比较与选择

### 方案 A：新 S4/P4/M4/L4 与全新 v4 namespace（采用）

优点是 authority、一次性机会、证据所有权与失败边界完全可审计；v3 现场保持原样，JSON-real 修复可在任何 patch/运行前 TDD。代价是需要新 spec、plan、manifest、lock 和一次新的明确用户执行授权。

### 方案 B：热补 P3 并复用 L3（拒绝）

P3 bytes 已由 L3 锁定。修改 P3 或仅在运行时替换 validator 都会使已审核 plan 与实际执行字节分离，并隐藏 v3 checkpoint anomaly。

### 方案 C：沿用 v3 RED 或补丁后 fixture 继续（拒绝）

这会把已越过首个 mismatch 的历史包装成干净 continuation，并让 v3 worktree 成为 v4 source。即使 generator invocation 仍为 0，也不允许复用。

### 方案 D：只接受 Decimal（拒绝）

它能通过当前物理 v2 普通小数，却会错误拒绝 WinPS5.1 对科学计数 JSON real 产生的 finite Double。

### 方案 E：先 cast 再比较，或接受所有数值类型（拒绝）

这会把整数、Single、字符串或 NaN/Infinity 等错误输入带回合同，并使实际类型错误被隐式转换掩盖。

## 提交与 authority 拓扑

提交必须形成单线直接父链：

```text
P2  25c2ea674948ad89e8b48befb89643a8687648a4
 |
S3  5fa8fb14792e095e066c3e9f698eda9ea4380854
 |
P3  7365ae61c8d12dd0f34651a4bd727528cd9059d4
 |
S4  Recovery v4 spec commit，只新增本规格
 |
P4  Recovery v4 plan commit，只新增对应 plan
 |
R4  Task 2 rules commit，只修改三个既定 game 路径
```

- `S4^=P3`，S4 subject 必须为 `docs: specify terminal collapse generator recovery v4`；
- S4 只新增 `docs/superpowers/specs/2026-08-15-terminal-collapse-generator-recovery-v4-design.md`；
- `P4^=S4`，P4 subject 必须为 `docs: plan terminal collapse generator recovery v4`；
- P4 只新增 `docs/superpowers/plans/2026-08-15-terminal-collapse-generator-recovery-v4.md`；
- `R4^=P4`，R4 subject 保持 `fix: enforce terminal resistance collapse rules`；
- R4 只修改 `game/balance.rpy`、`game/difficulty.rpy`、`game/test_game.rpy`；
- P2、S3、P3、S4、P4 的 `game` tree 都必须为 `fa7a398e9d989731b24e3c1642f3e2e33ce846ff`；
- 在 v4 Task 1 completion 成功前，R4 不得创建；
- 任一 merge、中间提交、额外 path、hook 附带文件、index 残留或 winter 漂移都停止。

S4 提交后必须先由用户审阅本规格。没有新的明确批准，不得开始 P4。P4 完成并独立复审后，仍不得把“计划 READY”解释为 M4/L4 或 Task 1 执行授权。

## M4 前任证据 manifest

固定路径：

`.superpowers/sdd/terminal-collapse-ending/recovery-v4/predecessor-evidence.json`

M4 以 CreateNew、strict UTF-8、无 BOM、单一末尾 LF、`Flush(true)`、strict 重读和只读方式创建，schema 固定为 3。顶层属性顺序和集合恰为 17 项：

`schema_version,purpose,predecessor_plan_commit,predecessor_spec_commit,predecessor_lock_path,predecessor_lock_bytes,predecessor_lock_sha256,predecessor_manifest_path,predecessor_manifest_bytes,predecessor_manifest_sha256,artifact_count,catalog_bytes,catalog_sha256,artifacts,terminal_failure,source_inventories,created_utc`

固定语义：

- `schema_version=3`；
- `purpose="terminal-collapse-generator-recovery-v4-predecessor"`；
- `predecessor_plan_commit=P3`；
- `predecessor_spec_commit=S3`；
- predecessor lock 精确绑定 L3 path/2,354 bytes/`59D44AFD...626C`；
- predecessor manifest 精确绑定 M3 path/45,507 bytes/`6DE89AAD...2FBB`；
- `artifact_count=124`；
- `catalog_bytes=26703`；
- `catalog_sha256="AFAD4D1F6EB1808DC79E45B506A152CC4D62FE0AB6DB6238C2474A039AB4D589"`；
- `created_utc` 必须是可 round-trip 的 UTC 字符串。

124 个唯一 leaf 的组成精确为：

1. M3 的 115 个 artifact，path/bytes/hash 逐项不变；
2. S3 spec；
3. P3 plan；
4. L3；
5. M3；
6. v3 RED；
7. v3 补丁后 fixture；
8. v3 Task 1 brief；
9. v3 retry authority；
10. v3 合并失败报告。

第 2–10 项的 seal 必须精确等于“已冻结事实”中的九项。`.superpowers/sdd/progress.md` 是可变跨任务摘要，不进入 M4；protected winter 也不进入 M4。

catalog 使用绝对规范路径、Ordinal 排序、OrdinalIgnoreCase 判重；每行精确为 `<path><TAB><decimal bytes><TAB><UPPERCASE SHA256><LF>`。封存时必须从 124 个物理 leaf 重建 exact 26,703-byte catalog 与固定 SHA；不匹配即停止，不能按现场漂移静默更新。

`artifacts` 每项属性顺序和集合恰为 `path,bytes,sha256`，逐行对应 catalog。M4 创建后必须从 strict 反序列化对象再次重建相同 catalog，才可设为只读。

### terminal_failure

`terminal_failure` 属性顺序和集合恰为：

`classification,program_outcome,reason,final_status,final_failure_stage,attempts,checkpoint_anomaly,helper_launch_count,renpy_launch_count,generator_invocation_count,observer_invocation_count,generated_save_count,generator_ledger_present,observer_ledger_present,green_present,mother_present,task1_completion_present,red,patched_fixture,brief,retry_authority,report,worktree_path,worktree_head_commit,worktree_game_tree,worktree_status_rows,artifact_disposition,candidate_save_disposition`

固定值与关系：

- `classification="STATIC_CONTRACT_FAILURE"`；
- `program_outcome="NOT_INVOKED"`；
- `reason="JSON_REAL_TYPE_MISMATCH"`；
- `final_status="NEEDS_CONTEXT"`；
- `final_failure_stage="POST_PATCH_PRE_GREEN"`；
- helper、Ren'Py、generator、observer 与 generated-save count 全为 0；
- 两个 ledger、GREEN、mother、Task 1 completion 的 present 布尔值全为 false；
- `artifact_disposition="preserved_not_used"`；
- `candidate_save_disposition="not_created"`；
- worktree path 为固定 v3 generator worktree，HEAD=P3，game tree 为固定 baseline；
- `worktree_status_rows` 恰为一个字符串：`?? game/zz_terminal_collapse_legacy_fixture.rpy`。

`attempts` 恰有两个有序对象；每项属性顺序和集合恰为：

`id,authorization,stage,outcome,reason,target_scope_count,helper_launch_count,renpy_launch_count,generator_invocation_count,observer_invocation_count,disposition`

第一个对象固定为：`id="initial_task1_transport"`、`authorization="initial_v3_task1_authority"`、`stage="HOST_PRELAUNCH"`、`outcome="NEEDS_CONTEXT"`、`reason="HOST_FIRST_LINE_MISMATCH"`、target scope 0、全部 launch/invocation 0、`disposition="non_authoritative_preserved"`。第二个对象固定为：`id="authorized_task1_retry"`、`authorization="user_approved_v3_task1_retry"`、`stage="POST_PATCH_PRE_GREEN"`、`outcome="NEEDS_CONTEXT"`、reason 精确为 `physical frozen v2 generator state positive control did not ACCEPT`、target scope 2、全部 launch/invocation 0、`disposition="terminal_preserved_not_used"`。

`checkpoint_anomaly` 属性顺序和集合恰为 `observed,stage,reason,authority_effect,disposition`，固定值为 `true`、`PREPATCH_HOST_HANDOFF`、`ANSI_CURSOR_WRAP_RECONSTRUCTION_MISMATCH`、`INVALIDATES_CLEAN_V3_CONTINUATION`、`preserved_not_used`。

`red`、`patched_fixture`、`brief`、`retry_authority`、`report` 每项属性恰为 `path,bytes,sha256`，精确绑定九项新增 leaf 中相应文件。RED 作为历史记录读取；任何消费者不得要求 RED 内的 pre-patch fixture seal 与当前 patched fixture 相等。

### source_inventories

`source_inventories` 恰有三个有序对象：

1. `v2_generator_worktree_task_owned`；
2. `v2_generator_savedir`；
3. `v3_generator_worktree_task_owned`。

每项属性顺序和集合恰为 `id,root_path,authority_file_count,authority_files,excluded_cache_count,excluded_cache_files`。两个 files 数组的元素属性均恰为 `relative_path,bytes,sha256`，以 Ordinal relative path 排序并以 OrdinalIgnoreCase 判重。

前两个 inventory 的 metadata 必须与 M3 对应值逐项、同序、同类型相等：authority 8/12，excluded 61/0。第三个 inventory 只含补丁后 fixture 一个 authority leaf，excluded count=0。

M4 controller 与独立 reviewer 必须在封存时用 non-following、`-Force`、逐路径组件 reparse 检查验证 v3 worktree：HEAD=P3、game tree baseline、tracked index/worktree clean、唯一 task-owned ordinary file 为 fixture、没有额外目录/leaf/reparse/case-fold collision。Task 0/1/2/3 后续只允许读取三个 inventory 的 metadata，并对 M4 124 个已声明 authority leaf 做 current seal；不得读取或存在性探测 61 个 excluded cache leaf。遇到未知 path 时只能报告 path 并停止，不能打开或提升它。

M4 必须经过独立只读复审。reviewer 返回 exact uppercase physical M4 SHA-256 作为带外值；泛化 `READY` 不能替代 hash。没有该值不得创建 L4。

## L4 approval lock

固定路径：

`.superpowers/sdd/terminal-collapse-ending/approved-plan-lock-v4.json`

L4 只在 S4、P4、M4 全部完成独立复审后创建。它使用 CreateNew、strict UTF-8、无 BOM、单一末尾 LF、`Flush(true)`、strict 重读与只读；路径必须 Git-ignored。物理 SHA-256 通过带外 `$ApprovalLockSha256` 传给每个 fresh Task 0/1/2/3 与 Phase B context。

L4 schema 固定为 4，顶层属性顺序和集合恰为 39 项：

`schema_version,purpose,approved_plan_path,approved_plan_commit,plan_bytes,plan_sha256,spec_path,spec_commit,spec_bytes,spec_sha256,predecessor_plan_commit,predecessor_spec_commit,predecessor_lock_path,predecessor_lock_bytes,predecessor_lock_sha256,predecessor_manifest_path,predecessor_manifest_bytes,predecessor_manifest_sha256,predecessor_artifact_count,predecessor_catalog_bytes,predecessor_catalog_sha256,baseline_game_tree,execution_strategy,superseded_namespace,superseded_disposition,superseded_failure_report_path,superseded_failure_report_bytes,superseded_failure_report_sha256,task1_admission_ledger_path,task1_admission_limit,generator_attempt_ledger_path,generator_attempt_limit,observer_attempt_ledger_path,observer_attempt_limit,test_result_stream,engine_log_role,state_real_number_policy,execution_authorization_required,task1_admission_schema`

固定值与关系：

- `schema_version=4`、`purpose="terminal-collapse-generator-recovery-v4"`；
- plan path/commit/bytes/hash 绑定 P4 物理 bytes 与 raw Git blob；
- spec path/commit/bytes/hash 绑定 S4 物理 bytes 与 raw Git blob；
- predecessor plan/spec 为 P3/S3；
- predecessor lock 绑定 L3；
- predecessor manifest 绑定 M4 的 physical bytes/hash；
- predecessor artifact/catalog 固定为 124/26,703/`AFAD...D589`；
- baseline game tree 为 `fa7a398e9d989731b24e3c1642f3e2e33ce846ff`；
- `execution_strategy="fresh_namespace_global_one_shot"`；
- `superseded_namespace` 为 recovery-v3 规范绝对路径；
- `superseded_disposition="preserved_not_used"`；
- superseded failure report 绑定固定 v3 report path/15,156 bytes/`7BE3...2485`；
- `task1_admission_ledger_path` 为 `recovery-v4/task1-admission/attempt.json` 规范绝对路径；
- `task1_admission_limit=1`、`task1_admission_schema=1`；
- generator/observer ledger path 分别为 `recovery-v4/generator-attempt` 与 `recovery-v4/observer-attempt` 规范绝对路径；
- generator/observer attempt limit 均为 1；
- `test_result_stream="helper_stdout"`；
- `engine_log_role="diagnostic_only"`；
- `state_real_number_policy="decimal_or_finite_double"`；
- `execution_authorization_required=true`。

所有 fresh context 的第一个项目 leaf access 必须是 L4 的存在检查和 physical SHA 比对；只允许为读取该叶本身所需的路径存在检查先于 hash。SHA 通过后才能检查 read-only/ignored、字节、编码、duplicate keys、schema、类型、值、路径、Git topology 或其他项目 leaf。

## v4 命名空间与临时路径

除 L4、S4、P4 外，所有 v4 持久运行证据只写入：

`.superpowers/sdd/terminal-collapse-ending/recovery-v4/`

固定核心路径：

- `predecessor-evidence.json`；
- `task1-admission/attempt.json`；
- `generator-contract-red.json`；
- `generator-contract-green.json`；
- `generator-attempt/attempt.json|completion.json`；
- `generator-process/request.json|stdout.txt|stderr.txt|result.json`；
- `generator-state.json`；
- `generator-fixture.rpy`；
- `generator-engine-log.txt`；
- `observer-attempt/attempt.json|completion.json`；
- `observer-process/request.json|stdout.txt|stderr.txt|result.json`；
- `observer-state.json`；
- `observer-fixture.rpy`；
- `observer-engine-log.txt`；
- `mother/1-1-*.save`；
- `baseline-evidence.md`；
- `task1-completion.json`；
- `rules/` 下游证据。

固定临时路径：

- generator worktree：`E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-generator-recovery-v4`；
- generator SaveDir：`E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-generator-save-recovery-v4`；
- observer worktree：`E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-observer-recovery-v4`；
- observer SaveDir：`E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-observer-save-recovery-v4`。

四个路径和全部 v4 runtime/ledger leaf 必须在 admission 前不存在。不得通过新 GUID、后缀、别名、junction 或 alternate evidence root 规避 fixed-path 消费语义。

## 全局 Task 1 admission

S4、P4、M4、L4、Task 0 PASS 与独立复审只批准静态验证，不批准 Task 1。

用户必须在这些步骤完成后再次明确批准一次 Recovery v4 Task 1。控制器收到该授权后，在任何 Task 1 target session、RED、worktree、fixture、host patch、helper 或 Ren'Py 之前，创建固定 `task1-admission/attempt.json`。该文件同时是用户授权记录与全局一次性机会；不另建可漂移的旁路 authorization file。

admission 使用 CreateNew、strict UTF-8、无 BOM、单一末尾 LF、`Flush(true)`、strict 重读与只读。顶层属性顺序和集合恰为 10 项：

`schema_version,purpose,attempt_id,authorized_utc,authorization,approval_lock_sha256,approved_plan_commit,predecessor_manifest_sha256,max_task1_admissions,retry_allowed`

固定语义：

- `schema_version=1`；
- `purpose="terminal-collapse-generator-recovery-v4-task1-admission"`；
- attempt ID 为 32 位小写十六进制；
- `authorized_utc` 为可 round-trip UTC 字符串；
- `authorization="user_approved_recovery_v4_task1_once"`；
- 绑定 L4 SHA、P4、M4 SHA；
- `max_task1_admissions=1`；
- `retry_allowed=false`。

admission 目录或 leaf 一旦创建即表示 v4 Task 1 机会已消费，即使 target 尚未启动、transport 失败或后续任何静态 gate 失败。控制器把 admission physical SHA 作为第二个带外值传入唯一 Task 1 target。Task 1 的第一个项目 leaf 是 L4，第二个项目 leaf 是 admission；随后才可读取 P4/M4 或其他项目状态。

admission 后任一 host extraction、transport、PowerShell scope、TDD、patch、ledger、helper、Ren'Py、state、save、observer、mother、cleanup、baseline 或 completion 失败都必须保留现场并终止。恢复需要新的 S5/P5/M5/L5；禁止 retry、替换 ledger、换 GUID、alternate transport、复用 RED/fixture 或追认 checkpoint。

## JSON-real 静态 TDD 合同

P4 必须提供一个中央、纯对象、无文件写入、无 process launch 的 JSON-real range validator。接口语义固定为：

```text
Test-V4JsonRealRange(value, allow_zero) -> ACCEPT | REJECT
```

- value 为 Decimal：在 Decimal 分支原生比较；
- value 为 Double：先拒绝 NaN/正负 Infinity，再在 Double 分支原生比较；
- `allow_zero=false` 时严格 `>0`；
- `allow_zero=true` 时 `>=0`；
- 其他类型全部 REJECT；
- 禁止先 cast、字符串 parse、truthiness 或默认值。

固定调用为 `_ctime` 使用 `allow_zero=false`，`_game_runtime` 使用 `allow_zero=true`。

新增 `json_real_gate`，但不得调用 exact-42 的 `Add-Mutation`，因此 exact-42 的名称、顺序和计数完全不变。gate 精确包含 8 个有序 positive：

1. `decimal_ctime_physical_v2`；
2. `decimal_runtime_physical_v2`；
3. `decimal_ctime_min_positive`；
4. `decimal_runtime_zero`；
5. `double_ctime_scientific_one`；
6. `double_runtime_scientific_zero`；
7. `double_ctime_max_finite`；
8. `double_runtime_negative_zero`。

以及 18 个有序 negative：

1. `ctime_decimal_zero`；
2. `ctime_decimal_negative`；
3. `ctime_double_negative_zero`；
4. `ctime_double_negative`；
5. `runtime_decimal_negative`；
6. `runtime_double_negative`；
7. `ctime_double_nan`；
8. `runtime_double_nan`；
9. `ctime_double_positive_infinity`；
10. `runtime_double_positive_infinity`；
11. `ctime_double_negative_infinity`；
12. `runtime_double_negative_infinity`；
13. `ctime_int32_positive`；
14. `runtime_int64_positive`；
15. `ctime_single_positive`；
16. `runtime_string_zero`；
17. `ctime_bool_true`；
18. `runtime_null`。

scientific positive 必须由 WinPS5.1 `ConvertFrom-Json` 解析 `1e0`/`0e0` 产生，不能直接 cast。物理 v2 positive 必须 strict 读取 M4 已封存的 v2 `generator-state.json`，同时证明 path/bytes/hash 与 M4 row 一致；这是唯一获准反序列化的失败谱系 state control，不得打开 candidate save。其他 predecessor runtime leaf 只允许 manifest-directed current seal。

每个 persisted case 属性恰为 `name,input_type,allow_zero,expected,actual`。`json_real_gate` 属性顺序和集合恰为 `contract,positive_count,negative_count,positive_cases,negative_cases,verdict`，固定 `contract="decimal_or_finite_double"`、8/18、`verdict="PASS"`。NaN/Infinity 本身不得序列化进 JSON；record 只保存 case name、input type 与结果。

该 gate 必须在 host patch 前先 PASS，并在 GREEN 中用同一 production validator 再 PASS。任一 control 数量、顺序、类型、expected/actual 或 verdict 漂移都终止，且 admission 已消费。

## RED、GREEN 与 exact-42

RED/ GREEN schema 升为 4，顶层属性顺序和集合恰为：

`schema_version,verdict,fixture_gate,stream_gate,json_real_gate,inputs,mutations,created_utc`

两者都绑定同一个 PASS `json_real_gate`。

- RED：`verdict="EXPECTED_RED"`，旧 selector/fixture 继续证明退出结构与日志选择器的预期失败，`mutations=[]`；
- GREEN：`verdict="PASS"`，fixture 退出结构 PASS、双日志合同 PASS、JSON-real gate PASS，并持久化 exact-42；
- RED/ GREEN 均 CreateNew、Flush(true)、strict 重读、只读；
- RED 必须在全局 admission 后、任何 worktree 或 patch 前，从 authenticated P4 appendix 中提取的旧 fixture bytes 做静态检查并创建；它不能读取 v3 fixture；
- GREEN 必须在全新 v4 worktree 中只应用 P4 批准 patch 后创建；
- v3 RED 与 patched fixture 只能在 M4 integrity 中哈希，不能成为 v4 RED/GREEN 的 source。

exact-42 的名称与顺序固定为：

1. stdout 缺少 PASSED；
2. stdout 有两条 PASSED；
3. PASSED 改为 FAILED；
4. 增加第二条任意 Status；
5. stdout 为空；
6. stdout 带 UTF-8 BOM；
7. stdout 含非法 UTF-8；
8. stdout 含 NUL；
9. stdout 含孤立 CR；
10. 非空 stdout 缺末尾 LF；
11. stdout path 指向 engine log；
12. request/result stdout path 不一致；
13. testcase identity 行缺失；
14. testcase identity 行重复；
15. summary 标题缺失；
16. summary 标题重复；
17. stderr 写入一个字节；
18. PASSED 只出现在 engine log；
19. engine log 缺失；
20. engine log 为空；
21. engine log 带 BOM；
22. engine log 含非法 UTF-8；
23. engine log 含 NUL；
24. generator engine log 出现任意 rpytest 行；
25. engine log 注入 traceback；
26. engine log 注入 Ren'Py uncaught-exception 标题；
27. engine-log evidence 改动一个字节；
28. generator completion 的 stdout bytes/hash 漂移；
29. request seal 漂移；
30. stderr seal 漂移；
31. generator completion 缺字段、加字段或乱序；
32. request environment 缺键；
33. request environment 加键；
34. request environment 重复键；
35. request environment 乱序；
36. observer state 为 FAIL，但日志中伪造 PASSED；
37. observer stdout 非空；
38. observer stderr 非空；
39. observer engine log 出现任意 rpytest 行；
40. observer completion missing、extra、reordered、wrong-type 四个 control 全部 REJECT；
41. 正向接受成功 stdout 中的 `[rpytest] [exc]`；
42. 正向接受 dummy renderer fallback 的 `error(...)` 文本。

名称、顺序、expected/actual 与隔离要求全部原样继承，不增删、不改名、不改序。case 9/10/11/27/34/36 必须维持已审核的隔离语义。JSON-real 的 8+18 不计入 42。

P4 的人工 metadata positive 不得再直接构造 `[double]1.0`；普通小数 positive 必须由 `ConvertFrom-Json` 生成 Decimal，科学计数 positive 必须由 `ConvertFrom-Json` 生成 Double，并先断言实际 CLR 类型。

## 唯一 v4 generator 与 observer

除 authority 标识、v4 marker/path 和 admission 连接外，generator/observer 的 request/result/state/log/save 合同继承 S3 的已审核接口：

- generator/observer attempt schema 3，分别为 exact 19/20 fields；
- generator/observer completion schema 3，分别为 exact 43/42 fields；
- request schema 1，顶层 9 fields；generator environment exact 11，observer exact 12；
- helper result exact 38-field schema v2；
- generator timeout 180000 ms，observer timeout 120000 ms；
- SafetyEnvelope 要求 COMPLETED、actual/persisted helper exit 0、integral non-null root exit 0、no timeout、visible window 0、Job drain/monitor/cleanup 全 PASS、host termination false；
- helper stdout 是 generator rpytest test_report，恰一条 PASSED；stderr 0-byte；worktree log 是 diagnostic engine_boot_log，不从其中要求 PASSED；
- observer stdout/stderr 均 0-byte，observer engine log 无 rpytest 行；
- generator target 恰为 external root、external sync、local `game/saves` 三份相同 save；
- observer 启动前只有 external root replay 一份 target，运行后不得产生 sync/local shadow target；
- full physical save inventory 必须用 `-Force`、non-following traversal、逐组件 reparse 拒绝、Ordinal 排序与统一 OrdinalIgnoreCase file/dir collision set 重建；
- AppData backup 只做 S3 已定义的两条 exact metadata-only bounded before/after observation，不是 authority leaf，不进入 union，不清理；
- generator/observer 各调用恰一次；ledger directory 一旦存在即消费对应机会；
- fixture 必须由 authenticated P4 appendix 在全新 v4 worktree 中重建，禁止读取或复制 v3 fixture 内容。

generator attempt 的 exact 19 fields 为：

`schema_version,attempt_id,started_utc,approval_lock_sha256,task1_admission_sha256,approved_plan_commit,predecessor_manifest_sha256,red_record_path,red_record_sha256,green_record_path,green_record_sha256,worktree_path,savedir_path,process_evidence_dir,state_path,fixture_path,fixture_sha256,max_generator_invocations,retry_allowed`

generator completion 的 exact 43 fields 为：

`schema_version,attempt_id,attempt_path,attempt_sha256,approval_lock_sha256,task1_admission_sha256,approved_plan_commit,predecessor_manifest_sha256,red_record_sha256,green_record_sha256,worktree_path,savedir_path,process_evidence_dir,fixture_path,fixture_sha256,fixture_evidence_path,fixture_evidence_sha256,request_path,request_bytes,request_sha256,result_path,result_bytes,result_sha256,state_path,state_bytes,state_sha256,rpytest_stdout_path,rpytest_stdout_bytes,rpytest_stdout_sha256,stderr_path,stderr_bytes,stderr_sha256,engine_log_evidence_path,engine_log_evidence_sha256,external_save_path,sync_save_path,local_save_path,target_copy_count,save_name,save_bytes,save_sha256,save_inventory,finished_utc`

observer attempt 的 exact 20 fields 为：

`schema_version,attempt_id,started_utc,approval_lock_sha256,task1_admission_sha256,approved_plan_commit,generator_completion_path,generator_completion_sha256,worktree_path,savedir_path,process_evidence_dir,state_path,fixture_path,fixture_sha256,source_save_path,source_save_bytes,source_save_sha256,replay_save_path,max_observer_invocations,retry_allowed`

observer completion 的 exact 42 fields 为：

`schema_version,attempt_id,attempt_path,attempt_sha256,approval_lock_sha256,task1_admission_sha256,approved_plan_commit,generator_completion_sha256,worktree_path,savedir_path,process_evidence_dir,fixture_path,fixture_sha256,fixture_evidence_path,fixture_evidence_sha256,request_path,request_bytes,request_sha256,result_path,result_bytes,result_sha256,state_path,state_bytes,state_sha256,stdout_path,stdout_bytes,stdout_sha256,stderr_path,stderr_bytes,stderr_sha256,engine_log_evidence_path,engine_log_evidence_sha256,source_save_path,source_save_bytes,source_save_sha256_before,source_save_sha256_after,replay_save_path,replay_save_bytes,replay_save_sha256_before,replay_save_sha256_after,save_inventory,finished_utc`

四份 record 的 `task1_admission_sha256` 必须精确等于 target reentry 前带外冻结并重新哈希的 admission SHA。generator completion 必须等于 generator attempt 中的值；observer attempt 同时绑定 generator completion，并复验其 admission SHA；observer completion 必须等于 observer attempt 与 generator completion 中的同一值。任一缺失、重排、类型漂移或不等即停止，禁止把 admission 与运行结果事后并列拼接。

generator environment name 的 exact Ordinal 顺序为：

`RENPY_NO_REDIRECT_STDIO,RENPY_PATH_TO_SAVES,RENPY_RENDERER,SDL_AUDIODRIVER,SDL_VIDEODRIVER,TC_EXPECTED_BASELINE_COMMIT,TC_EXPECTED_FIXTURE_SHA256,TC_EXPECTED_GAME_TREE,TC_EXPECTED_MARKER,TC_EXPECTED_SAVEDIR,TC_GENERATOR_RESULT`

observer environment name 的 exact Ordinal 顺序为：

`RENPY_AUTO_LOAD,RENPY_NO_REDIRECT_STDIO,RENPY_PATH_TO_SAVES,RENPY_RENDERER,SDL_AUDIODRIVER,SDL_VIDEODRIVER,TC_EXPECTED_BASELINE_COMMIT,TC_EXPECTED_FIXTURE_SHA256,TC_EXPECTED_GAME_TREE,TC_EXPECTED_MARKER,TC_EXPECTED_SAVEDIR,TC_OBSERVER_RESULT`

对应值必须按 S3 语义改绑 P4、v4 fixture SHA、baseline game tree、v4 marker、fixed v4 SaveDir/state path；`RENPY_PATH_TO_SAVES` 仍为 null，renderer/audio/video 与 `RENPY_NO_REDIRECT_STDIO` 保持批准值。

generator/observer 的两个 attempt 与两个 completion 均必须以 CreateNew、strict UTF-8、无 BOM、单一末尾 LF、`Flush(true)`、strict reread和只读方式发布；对应 ledger directory 一旦存在即消费机会。任一目标 leaf 预先存在、发布失败、strict reread 不等或只读冻结失败都终止，禁止覆盖写、删除后重建或换目录。

P4 必须完整重述这些字段集合、关系、central validators、host apply_patch seam、四个 fresh lock-first scope、bounded AST child、private desktop wrapper、mother 与 cleanup 程序，不能只写“同 v3”。本规格允许设计层继承，执行计划必须自包含。

## v4 durable leaves 与 Task 1 completion

除 Task 1 completion 自身外，v4 新 durable leaf 固定为 27 项。

`recovery-v4/` 外三项：

1. L4；
2. S4 spec；
3. P4 plan。

`recovery-v4/` 内 24 项：

1. M4；
2. Task 1 admission；
3. RED；
4. GREEN；
5–13. generator attempt/completion、process 四件、state、fixture evidence、engine-log evidence；
14–22. observer attempt/completion、process 四件、state、fixture evidence、engine-log evidence；
23. 唯一 mother；
24. baseline evidence。

helper stdout 已是 process 四件之一，不复制。Task 1 completion 自身为避免自引用不进入 union。

成功前 `recovery-v4/` 的 exact durable tree 为 24 leaves、6 directories；成功写入 Task 1 completion 后为 25 leaves、6 directories。六个目录恰为 `task1-admission`、`generator-attempt`、`generator-process`、`observer-attempt`、`observer-process`、`mother`；`rules/` 必须仍不存在。任何额外 hidden/system leaf、目录、reparse 或 case-fold alias 都失败。

Task 1 completion 位于 `recovery-v4/task1-completion.json`，schema 固定为 4。它必须以 CreateNew、strict UTF-8、无 BOM、单一末尾 LF、`Flush(true)`、strict reread和只读方式发布；path 预先存在、发布/flush/reread/只读任一步失败都终止，禁止覆盖或重建。顶层属性顺序和集合恰为 16 项：

`schema_version,verdict,approval,task1_admission,predecessor,baseline_game_tree,full_selftest,version_probe,generator,observer,mother,artifact_count,artifacts,cleanup,finished_utc,lineage_status`

`lineage_status` 放在最后，固定为 `fresh_v4_only`；它不是含糊备注，而是 exact schema field。

嵌套属性顺序和集合固定为：

- `approval`：`lock_path,lock_bytes,lock_sha256,plan_path,plan_commit,plan_bytes,plan_sha256,spec_path,spec_commit,spec_bytes,spec_sha256`；
- `task1_admission`：`path,bytes,sha256,schema_version,purpose,attempt_id,authorized_utc,authorization,approval_lock_sha256,approved_plan_commit,predecessor_manifest_sha256,max_task1_admissions,retry_allowed`；
- `predecessor`：`manifest_path,manifest_bytes,manifest_sha256,artifact_count,catalog_bytes,catalog_sha256,terminal_failure,source_inventories`；
- `full_selftest`：`reused,attempt_path,attempt_bytes,attempt_sha256,completion_path,completion_bytes,completion_sha256,root_path`；
- `version_probe`：`reused,evidence_dir,request_sha256,stdout_sha256,stderr_sha256,result_sha256`；
- `generator`：沿用 S3 nested set并加入 `task1_admission_sha256`，因此恰为 28 fields；`source="fresh_generator_v4"`、invocation count=1，所有 path/marker/commit 改绑 v4/P4；
- `observer`：沿用 S3 nested set并加入 `task1_admission_sha256`，因此恰为 17 fields；invocation count=1并改绑 v4；
- `mother`：`path,bytes,sha256,read_only`；
- `cleanup`：`generator_worktree_removed,generator_savedir_removed,observer_worktree_removed,observer_savedir_removed`；
- `artifacts` 每项：`path,bytes,sha256`。

`generator` 的 exact 28 fields 为：

`source,invocation_count,task1_admission_sha256,red_record_path,red_record_sha256,green_record_path,green_record_sha256,attempt_path,attempt_sha256,completion_path,completion_sha256,evidence_dir,request_sha256,result_sha256,state_path,state_sha256,rpytest_stdout_path,rpytest_stdout_bytes,rpytest_stdout_sha256,stderr_sha256,fixture_evidence_path,fixture_evidence_sha256,engine_log_evidence_path,engine_log_evidence_sha256,save_name,save_bytes,save_sha256,target_copy_count`

`observer` 的 exact 17 fields 为：

`invocation_count,task1_admission_sha256,attempt_path,attempt_sha256,completion_path,completion_sha256,evidence_dir,request_sha256,result_sha256,state_path,state_sha256,stdout_sha256,stderr_sha256,fixture_evidence_path,fixture_evidence_sha256,engine_log_evidence_path,engine_log_evidence_sha256`

固定语义：

- `verdict="PASS"`；
- approval 绑定 L4/P4/S4 物理 bytes/hash/raw blob；
- admission 绑定唯一只读 admission physical seal，且 approval lock/P4/M4 关系已在其 strict reader 中验证；
- predecessor 绑定 M4 schema3、124/26,703/固定 catalog SHA、terminal failure 与三个 source inventory；
- full selftest/version probe `reused=true`，禁止重跑；
- generator/observer 只绑定 v4 invocation；
- mother 只来自 v4 generator external-root target，并与三份 generator target 和 observer source/replay before/after 全部 byte-equal；
- cleanup 四项全 true；
- `artifact_count=151` 且等于 artifacts length。

151-file required union 双向精确等于：

1. M4 的 124 个 current artifact；
2. 本节列出的 27 个 v4 durable leaf。

union 使用规范绝对路径、Ordinal 排序、OrdinalIgnoreCase 判重，并在 completion 创建前、strict 重读后、四路径 cleanup 后独立重建 current seals。M4 中 legacy/v2/v3 leaf 只可按 manifest row 流式哈希；除本规格明确授权的 v2 state JSON-real control外，不得解析、复制或用作 source。

baseline 必须逐谱系记录：legacy generator 1；v2 generator 1/observer 0；v3 generator 0/observer 0；v4 generator 1/observer 1；v4 Task 1 admission 1。必须记录 v3 没有 candidate save、v3 disposition `preserved_not_used`、v4 source `fresh_generator_v4`。

唯一成功顺序：admission 已冻结 → RED → fresh generator worktree + patch → GREEN → generator ledger/run/completion → fresh observer worktree + patch → observer ledger/run/completion → mother → fresh cleanup scope 严格重读两份 completion → 只删除四个 v4 临时路径 → baseline → 151-union → Task 1 completion。

## Task 2、Task 3 与 Phase B

P4 必须完整重述下游消费者：

- Task 2 fresh context 第一个项目 leaf 验证 L4；随后 strict 读取 Task 1 schema4 completion，并重哈希 exact 151 current artifacts，才能开始 RED；
- R4 必须是 P4 直接子提交，exact subject 与三个 game path 如 topology 所列；
- Task 2 仍为九次 invocation、14-field receipt schema1、exact 56 artifacts；
- 四个固定 authority seal 改为 L4、Task 1 schema4 completion、P4 plan、S4 spec；
- Task 2 completion 升为 schema4，沿用 exact 16-field top-level set，绑定 P4/S4/R4、Task 1 schema4 physical hash、9 receipts 与 56 artifacts；
- Task 3 在创建 copy/run root 前及每次三次 Opus 前，重验 L4、完整 P2→S3→P3→S4→P4→R4、Task 1 schema4/151、Task 2 schema4/9 receipts/56；
- Phase B 每个 fresh replay context 同样重验这些 authority，并只使用 v4 mother；
- Task 3 继续要求 fixed launcher/module pre/post seals、copy/run non-reparse exact namespace、strict summary/metadata/result、CreateNew blind map 与 fresh A/B/C reread；
- Task 2 的 combined canon/show、exact 9/14/56、无 global worktree prune、excluded-cache metadata-only 合同全部保留；
- legacy、v2、v3 只能在 mandatory manifest-directed integrity 中哈希；不能成为 source、fallback、candidate probe、Opus 输入或 replay。

Task 2 completion 的 exact 16 fields 为：

`schema_version,verdict,approved_plan_lock_sha256,task1_completion_path,task1_completion_sha256,approved_plan_commit,approved_spec_commit,rules_commit,rules_parent_commit,rules_subject,rules_paths,invocation_count,invocations,artifact_count,artifacts,finished_utc`

其固定语义为 schema4、PASS、P4/S4/R4、rules parent=P4、exact subject/三路径、invocation count=9、artifact count=56。receipt 与 invocation nested schema 必须在 P4 中逐字冻结，不能依赖宽松 JSON object 或现状重基线化。

Task 2 completion 同样必须以 CreateNew、strict UTF-8、无 BOM、单一末尾 LF、`Flush(true)`、strict reread和只读方式发布；其自身不以覆盖写、删除重建或 mutable Markdown 作为 authority。

成功 cleanup 后四个 v4 worktree/SaveDir 已不存在。Task 2/3/Phase B 只能验证 completion 中的历史 path/seal 关系与 151 个持久 artifact，不能要求被删除的临时 path 当前存在。

## 执行、失败与清理边界

- M4/L4 创建、Task 0 与 Task 1 都需要独立且明确的后续用户授权；本设计批准不包含这些动作；
- Task 0 仅静态、0 helper、0 Ren'Py；它的第一个 leaf 是 L4，并验证 M4 124、topology、raw blobs、winter/index/status，以及除 M4 外所有 v4 runtime/admission path absent；
- admission 只在用户明确批准一次 v4 Task 1 后由 controller prelaunch 创建；
- admission 后任何失败都 terminal，无 retry；
- generator completion 缺失时禁止 observer；observer completion 缺失时禁止 mother；Task 1 completion 缺失时禁止 Task 2；
- 所有 Ren'Py entrypoint 必须通过已审核 dedicated-host private-desktop wrapper；任意可见窗口、真实输入、UI takeover、timeout、launch error 或 SafetyEnvelope failure 都停止；
- host patch 只允许内建 `apply_patch`，绝对目标必须是 fixed v4 worktree；不得使用 shell `apply_patch.bat`；
- bounded AST child 必须异步 drain stdout/stderr，bounded wait、kill、exit reproof、bounded drain、finally dispose；禁止 parameterless `WaitForExit()` 或同步双管道死锁；
- cleanup 只允许从 fresh strict completion reread 推导四个 fixed v4 path，并与 hard allowlist exact 比较；
- cleanup 前进程为 0、worktree registration 精确、path 全组件 ordinary/non-reparse、durable evidence/mother 已冻结；
- 只执行两个 exact `git worktree remove --force` 与两个 exact SaveDir removal；禁止全局 `git worktree prune`；
- v1/v2/v3 worktree、SaveDir、lock、manifest、candidate、RED、fixture、brief、retry/report 永不进入 cleanup；
- AppData 两个 bounded observation root 永不进入 authority、union 或 cleanup；
- 任何 material delete 后报告 exact path 与不可恢复性，但成功临时 cleanup 是 P4 明确授权的既定步骤。

## 验收合同

设计与计划：

1. S4/P4 direct-parent、single-path、raw blob、physical bytes 与 game tree 全部精确；
2. P4 是自包含可执行 plan，不依赖“同 v3”省略字段、代码或门禁；
3. P4 所有 WinPS5.1 fence 静态 parse 0 error，内嵌 Python AST 静态 PASS；
4. 无待补标记、schema 自相矛盾、未定义跨 scope 变量或无界 wait；
5. S4/P4 完成独立 Standards/Spec/exec review，Critical=0、Important=0。

M4/L4/Task 0：

1. M4 exact schema3、124 current leaves、26,703-byte catalog 与固定 SHA；
2. terminal failure、两个 attempts、checkpoint anomaly、三个 source inventories 全部 exact；
3. L4 exact schema4/39 fields，lock-first 与 raw-blob topology gate PASS；
4. Task 0 证明 admission/v4 runtime 全 absent，dynamic launch count 0；
5. M4/L4 physical hash 由独立 reviewer 带外返回并在每个 fresh context 绑定。

Task 1 静态与运行：

1. 用户明确批准后，唯一 admission 在 target launch 前 CreateNew/Flush/read-only；
2. JSON-real 8 positive/18 negative exact gate 在 patch 前 PASS，物理 v2 Decimal control ACCEPT，scientific finite Double controls ACCEPT，错误类型与 non-finite 全 REJECT；
3. GREEN schema4 持久化 json_real_gate，exact-42 仍恰为 42；四份 runtime attempt/completion 均为 schema3 并直接绑定 admission SHA；
4. v4 fixture 从 P4 重建，绝不从 v3 复制；
5. generator/observer 各一次，SafetyEnvelope、state、双日志、save inventory、mother 全 PASS；
6. cleanup 仅四个 v4 临时 path；
7. exact pre-completion tree 24 leaves/6 dirs、post-completion 25/6；
8. Task 1 schema4 completion exact 151 current artifacts，lineage `fresh_v4_only`。

下游：

1. Task 2 schema4、9 invocations、14-field receipts、56 artifacts 与 R4 exact commit；
2. Task 3 三次 Opus 每次前完整复验；
3. Phase B 每个 fresh replay 完整复验并只使用 v4 mother；
4. 任一旧谱系 candidate/fixture 不被读取为 source、fallback 或候选。

## 资产与包体

- 美术：不需要；
- 音乐：不需要；
- 音效：不需要；
- 动画：不需要；
- UI/字体：不需要；
- 现有资产复用：无新增要求；
- 包体影响：0 bytes；
- 本规格只新增治理文档。后续 P4、M4、L4 与测试证据也不得修改 shipped assets 或增加包体。

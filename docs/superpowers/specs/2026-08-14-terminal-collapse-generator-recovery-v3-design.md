# 终末崩盘旧存档生成器日志契约与 Recovery v3 设计

日期：2026-08-14

## 背景与目标

Recovery v2 已修正 testcase 退出路径，并完成一次真实、无界面、正常退出的 generator 调用。该调用的 helper、安全 envelope、fixture state 与三份 MultiLocation 目标存档均通过；流程随后在日志门禁停止，因为已批准计划把 worktree `log.txt` 错当成 rpytest 结果流。

Recovery v3 的目标不是追认 v2 候选存档，而是：

1. 把 rpytest 结果流与 Ren'Py 引擎启动日志拆成两个明确接口；
2. 原位封存 v1、v2 的完整失败谱系，并将 v2 候选标为“保留但禁用”；
3. 在全新的 v3 authority 下只执行一次新 generator；
4. 仅在 generator completion 冻结后执行一次独立普通 `run` observer；
5. 只从 v3 新存档建立只读 mother；
6. 让 Task 2、Task 3 与 Phase B 只信任 v3 lock、v3 completion 和 v3 mother。

## 已确认的 v2 事实

- 当前 Recovery v2 plan commit（P2）为 `25c2ea674948ad89e8b48befb89643a8687648a4`；其 `game/` tree 为 `fa7a398e9d989731b24e3c1642f3e2e33ce846ff`。
- v2 lock 位于 `.superpowers/sdd/terminal-collapse-ending/approved-plan-lock-v2.json`，恰为 1,957 bytes，SHA-256 为 `592E9F1FD5C4996A8612005BE9A33A35721A63228AAB43811208099265AECF8B`。
- v2 predecessor manifest 位于 `.superpowers/sdd/terminal-collapse-ending/recovery-v2/predecessor-evidence.json`，恰为 33,555 bytes，SHA-256 为 `903E1F66E476EA3B2E0AA60103E2230B45A500EF46C8EF6418A87084F426F9EB`，并封存 83 个更早的 authority/evidence leaf。
- v2 generator attempt 已消费且 `retry_allowed=false`；attempt 为 2,020 bytes，SHA-256 为 `6C6D597580E80A448C0CE55A80C0955988970C2A6332854049420B8693D38DF0`。
- v2 generator helper result 为 `COMPLETED`、`helper_exit_code=0`、`root_exit_code=0`、`timed_out=false`、`visible_windows=[]`、`job_drained=true`、`cleanup_complete=true`；result SHA-256 为 `12955539EC45CB4B3FA5490393EF511A851BD7CA3800F7835EBACAFFFF69D94F`。
- v2 generator state 为 `PASS`，全部菜单、state、metadata 与保存后检查均通过；state SHA-256 为 `43EDEB6BDFD217A7E9CDD969564A29B472D6D0258CF83ABD106F568A5B29D652`。
- v2 helper stdout 为 1,074 bytes，SHA-256 为 `BD3B00124C6134FD0DAE737B293C20F68BF76F02ECDC69E77797C883FA5208CE`，恰有一条 `[rpytest] Status: PASSED`；stderr 为 0 bytes，SHA-256 为 `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855`。
- v2 worktree `log.txt` 为 1,860 bytes，SHA-256 为 `FE52BE91013D21B51AAF2CCDCF796289906EB4D12FA08EB1912A196B4F076A81`，只有引擎初始化与 dummy renderer fallback 诊断，rpytest `PASSED` 计数为 0。
- v2 生成了三份逐字节相同的 `1-1-LT1.save`：外部 SaveDir 根目录、外部 `sync/`、worktree `game/saves/`。三者均为 726,209 bytes，SHA-256 为 `A817BBDE9A00B82A044E27C9AF93F27D99E1F106AABDE2230FFD5E8A1FAF19D7`。
- v2 没有 generator completion，没有 observer attempt，没有 mother，没有 baseline，也没有 Task 1 completion。v2 generator 调用数永久为 1，observer 调用数永久为 0。
- v2 终止原因精确为 `GOVERNANCE_CONTRACT_FAILURE / LOG_CONTRACT_MISMATCH`：程序运行成功，但已批准的日志来源门禁错误。三份候选 save 的 disposition 固定为 `preserved_not_used`。

上述事实只证明 v2 失败现场当前自洽，不授权把 v2 候选晋升为 mother。

## 根因与术语

generator request 显式设置 `RENPY_NO_REDIRECT_STDIO=1`。Ren'Py 8.5.2 的 rpytest `ConsoleReporter` 通过标准输出打印测试结论；该环境变量同时禁止把 stdout 镜像进 worktree `log.txt`。因此正确的数据流是：

```text
rpytest 测试结论  -> helper generator-process/stdout.txt  -> test_report（权威）
fixture 游戏状态  -> generator-state.json                -> state_report（权威）
Ren'Py 初始化诊断 -> worktree log.txt                     -> engine_boot_log（非权威诊断）
```

本规格固定以下术语：

- `test_report`：helper 捕获的 generator stdout；是 rpytest 成败的唯一权威来源。
- `state_report`：fixture 原子发布的 generator/observer state JSON；是菜单、状态、metadata 与实际 auto-load 的权威来源。
- `engine_boot_log`：worktree `log.txt`；只用于发现高特异性致命启动异常，不能作为 rpytest 结果来源。
- `program_success`：helper、安全 envelope、root exit 与 state/test report 均通过。
- `governance_success`：`program_success` 之外，authority、一次性账本、证据封存、observer、mother 与下游 completion 全部通过。

v2 满足部分 `program_success` 事实，但不满足 `governance_success`。

## 不在本次范围内

- 不采纳、复制、改名、移动、删除或清理 legacy TIMEOUT candidate 与 v2 log-contract-mismatch candidate。
- 不把 v2 helper `COMPLETED` 或 state `PASS` 补写成 v2 generator completion。
- 不重跑 private-desktop helper full selftest 或 Ren'Py 版本探针；v3 只复用并重哈希既有通过证据。
- 不修改旧 design、旧 plan、旧 lock、旧 manifest、旧 attempt 或任一失败现场。
- 不修改 `game/` 生产脚本、文本、数值、结局键、成就、字体、资源或包元数据。
- 不改变 private-desktop helper 的 C#、PowerShell wrapper 或 selftest 源码。
- 不放宽 TIMEOUT、可见窗口、非零 helper/target exit、未 drain、未 cleanup、缺失证据或 schema 漂移的 fail-closed 语义。

## 方案选择

### 方案 A：全新 v3 generator（采用）

创建独立 spec、plan、lock、predecessor manifest、命名空间和一次性账本。v2 现场只作为冻结的失败前序；v3 用修正后的日志契约产生一份全新的 save，再由独立 observer 验证。

该方案不洗白任何旧失败，authority 边界最清楚，因此采用。

### 方案 B：直接提升 v2 候选（拒绝）

该方案会在 v2 generator completion 缺失且部分文件未于运行结束时立即只读封存的情况下追认候选，违反 v2 的 terminal failure 合同。

### 方案 C：离线重验 v2 后只跑 observer（拒绝）

新 observer 只能证明候选当前可加载，不能补回 v2 运行当时的封存与 completion 缺口；仍属于追认旧失败产物。

## 提交与 authority 拓扑

提交必须形成单线直接父链：

```text
P2  25c2ea674948ad89e8b48befb89643a8687648a4  Recovery v2 plan
 |
S3  Recovery v3 spec commit，只新增本规格
 |
P3  Recovery v3 plan commit，只新增对应 plan
 |
R3  Task 2 rules commit，只修改三个既定 game 路径
```

- `S3^` 必须精确等于 P2；`P3^` 必须精确等于 S3；`R3^` 必须精确等于 P3。
- S3 只新增 `docs/superpowers/specs/2026-08-14-terminal-collapse-generator-recovery-v3-design.md`。
- P3 只新增 `docs/superpowers/plans/2026-08-14-terminal-collapse-generator-recovery-v3.md`。
- `P3:game` 必须仍为 `fa7a398e9d989731b24e3c1642f3e2e33ce846ff`。
- R3 只修改 `game/balance.rpy`、`game/difficulty.rpy`、`game/test_game.rpy`。
- 任何 merge、中间提交、额外 path、hook 附带文件、索引残留或受保护 winter plan 漂移均停止。

## Recovery v3 前任证据

新 manifest 路径固定为：

`.superpowers/sdd/terminal-collapse-ending/recovery-v3/predecessor-evidence.json`

它以 CreateNew、strict UTF-8、无 BOM、末尾 LF、`Flush(true)`、strict 重读与只读方式创建，schema 固定为 2。顶层属性顺序和集合恰为：

`schema_version,purpose,predecessor_plan_commit,predecessor_lock_sha256,artifact_count,catalog_bytes,catalog_sha256,artifacts,failures,source_inventories,created_utc`

固定语义：

- `purpose="terminal-collapse-generator-recovery-v3-predecessor"`；
- `predecessor_plan_commit=P2`；
- `predecessor_lock_sha256=592E9F1FD5C4996A8612005BE9A33A35721A63228AAB43811208099265AECF8B`；
- `artifact_count=115`；
- `catalog_bytes=24660`；
- `catalog_sha256="9694E728A82F6DDC743DA5E83967EAC7EE02FFA62FA53E21F4A2374F27DDDA24"`。

115 个唯一 leaf 的组成必须精确为：

1. v2 predecessor manifest 中原有的 83 个 artifact；
2. 12 个 v2 新 authority/evidence leaf：v2 lock、v2 spec、v2 plan、v2 predecessor manifest、RED、GREEN、generator attempt、generator state、generator process 的 request/stdout/stderr/result；
3. 20 个 v2 runtime leaf：v2 worktree 的 fixture 与 engine log 两项、worktree `game/saves` 六项、外部 SaveDir 根与 `sync/` 共十二项。

catalog 继续使用绝对规范路径、Ordinal 排序、OrdinalIgnoreCase 判重；每行精确为 `<path><TAB><decimal bytes><TAB><UPPERCASE SHA256><LF>`。控制器封存时必须从物理文件重新构建并精确得到上述 count/bytes/hash；这些数值是不可漂移的设计基线，不得按“当前看到的新值”静默更新。

`artifacts` 每项属性恰为 `path,bytes,sha256`，顺序和值与 catalog 逐行一致。manifest 创建后必须从 JSON 反序列化结果重建 catalog，并再次得到同一 count/bytes/hash，才可设为只读。

`failures` 恰有两个有序元素。每个元素属性顺序和集合恰为：

`id,classification,program_outcome,reason,generator_invocation_count,observer_invocation_count,attempt_path,attempt_sha256,result_path,result_bytes,result_sha256,state_path,state_bytes,state_sha256,test_report_path,test_report_bytes,test_report_sha256,engine_log_path,engine_log_bytes,engine_log_sha256,target_copies,candidate_save_disposition`

`target_copies` 每项属性恰为 `role,path,bytes,sha256`；缺失的 legacy attempt 字段必须显式为 null，不能省略或转换为空字符串。两个元素的固定语义为：

1. legacy generator：`classification="TIMEOUT"`、`program_outcome="TIMEOUT"`、candidate disposition `preserved_not_used`；
2. v2 generator：`classification="GOVERNANCE_CONTRACT_FAILURE"`、`program_outcome="COMPLETED"`、`reason="LOG_CONTRACT_MISMATCH"`、generator invocation count 1、observer invocation count 0、candidate disposition `preserved_not_used`，并绑定 v2 attempt/result/state/stdout/engine-log/三份 target save 的 path、bytes 与 SHA-256。

每个 failure 的类型、规范路径与 seal 必须精确；禁止由宽松对象转换、缺省值或当前目录枚举推断。

`source_inventories` 恰有两个有序元素：`v2_generator_worktree_task_owned` 与 `v2_generator_savedir`。每个元素属性顺序和集合恰为 `id,root_path,authority_file_count,authority_files,excluded_cache_count,excluded_cache_files`；两个 files 数组的元素属性均恰为 `relative_path,bytes,sha256`，以 Ordinal relative path 排序并以 OrdinalIgnoreCase 判重。

- worktree 的 `authority_files` 恰为 fixture、engine log 与 `game/saves` 六项，共 8 项；
- 外部 SaveDir 的 `authority_files` 恰为根与 `sync/` 各六项，共 12 项；
- `.rpyc`、`game/cache` 等派生缓存只能出现在 worktree 的 `excluded_cache_files`，其 exact relative path/bytes/hash 由批准 plan 冻结；它们不是 115 个 authority leaf，不进入 mother lineage、不被 Task 1/2/3 读取，也不得由 v3 cleanup 删除。

Git-tracked 基线由 P2 tree 证明。任一额外 task-owned 普通文件、reparse point、大小写别名、数组计数不符或路径越界均停止并修订设计，不能扩充 115 基线。

## Recovery v3 approval lock

新 lock 路径固定为：

`.superpowers/sdd/terminal-collapse-ending/approved-plan-lock-v3.json`

它只在 S3、P3 与 predecessor manifest 完成独立复审后，由控制器以 CreateNew、strict UTF-8、无 BOM、末尾 LF、`Flush(true)` 和只读方式创建，并必须被 Git ignore。其物理 SHA-256 通过带外 `$ApprovalLockSha256` 传给每个 fresh Task 0/1/2/3 与 Phase B replay。

lock schema 固定为 3，顶层属性顺序和集合恰为 26 项：

`schema_version,purpose,approved_plan_path,approved_plan_commit,plan_sha256,spec_path,spec_commit,spec_sha256,predecessor_plan_commit,predecessor_lock_path,predecessor_lock_bytes,predecessor_lock_sha256,predecessor_manifest_path,predecessor_manifest_bytes,predecessor_manifest_sha256,baseline_game_tree,generator_strategy,superseded_generator_attempt_path,superseded_generator_attempt_sha256,superseded_generator_disposition,generator_attempt_ledger_path,generator_attempt_limit,observer_attempt_ledger_path,observer_attempt_limit,test_result_stream,engine_log_role`

固定值与关系：

- `purpose="terminal-collapse-generator-recovery-v3"`；
- `approved_plan_path`、`approved_plan_commit`、`plan_sha256` 绑定 P3 的物理 bytes 与 raw Git blob；
- `spec_path`、`spec_commit`、`spec_sha256` 绑定本规格的 S3 物理 bytes 与 raw Git blob；
- `predecessor_plan_commit=P2`；
- `predecessor_lock_path` 为 v2 lock 的规范绝对路径，bytes=1,957，SHA-256=`592E9F1FD5C4996A8612005BE9A33A35721A63228AAB43811208099265AECF8B`；
- `predecessor_manifest_path` 为 v3 predecessor manifest 的规范绝对路径，并绑定其 bytes/hash；
- `baseline_game_tree="fa7a398e9d989731b24e3c1642f3e2e33ce846ff"`；
- `generator_strategy="fresh_one_shot"`；
- `superseded_generator_attempt_path` 为 v2 attempt 规范绝对路径，SHA-256=`6C6D597580E80A448C0CE55A80C0955988970C2A6332854049420B8693D38DF0`；
- `superseded_generator_disposition="preserved_not_adopted_log_contract_mismatch"`；
- 两个 ledger path 分别指向 `recovery-v3/generator-attempt` 与 `recovery-v3/observer-attempt` 的规范绝对路径；
- `generator_attempt_limit=1`、`observer_attempt_limit=1`；
- `test_result_stream="helper_stdout"`；
- `engine_log_role="diagnostic_only"`。

所有任务的第一个项目动作必须先验证带外 lock SHA，再拒绝 BOM、非法 UTF-8、重复键、额外/缺失/乱序键、类型漂移、路径非规范、40/64 位十六进制格式错误和 Git 拓扑漂移。旧 lock 永不修改、替换或删除。

## v3 证据命名空间与持久叶

除 v3 lock、S3 spec 与 P3 plan 外，所有新运行时持久证据只写入：

`.superpowers/sdd/terminal-collapse-ending/recovery-v3/`

核心路径：

- `predecessor-evidence.json`
- `generator-contract-red.json`
- `generator-contract-green.json`
- `generator-attempt/attempt.json`
- `generator-attempt/completion.json`
- `generator-process/request.json|stdout.txt|stderr.txt|result.json`
- `generator-state.json`
- `generator-fixture.rpy`
- `generator-engine-log.txt`
- `observer-attempt/attempt.json`
- `observer-attempt/completion.json`
- `observer-process/request.json|stdout.txt|stderr.txt|result.json`
- `observer-state.json`
- `observer-fixture.rpy`
- `observer-engine-log.txt`
- `mother/1-1-*.save`
- `baseline-evidence.md`
- `task1-completion.json`
- `rules/` 下游证据

除 Task 1 completion 自身外，Task 1 新增的 durable leaf 固定为 26 项：v3 lock、v3 spec、v3 plan、predecessor manifest、RED、GREEN、generator attempt/completion、generator 四件 process evidence、generator state、generator fixture evidence、generator engine-log evidence、observer attempt/completion、observer 四件 process evidence、observer state、observer fixture evidence、observer engine-log evidence、唯一 mother、baseline evidence。

helper stdout 已是 generator 四件套中的持久 leaf，不得再复制一份。字段增加不改变 durable leaf 数量。

## 静态 TDD 合同

v3 不新增第三个测试记录；复用两个固定槽，并升级语义：

- `generator-contract-red.json`：同时证明旧 fixture 退出结构为 RED，以及旧日志选择器在已封存 v2 现场中读取 engine log 得到 0 条 PASSED、而 stdout 得到 1 条 PASSED。
- `generator-contract-green.json`：同时证明修复后 fixture 退出结构为 GREEN，以及新双通道验证器通过离线 mutation suite。

退出结构仍要求 generator Python helper 不调用 `renpy.quit()`；四个结束分支返回 0/41/42/43；证据发布失败返回 97；testcase 尾部通过 `$ _tc_generator_status = ...`、`assert eval (...)`、原生 `exit` 结束。

mutation suite 必须恰好按以下顺序覆盖 42 个 mutation/control：

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
31. completion 缺字段、加字段或乱序；
32. request environment 缺键；
33. request environment 加键；
34. request environment 重复键；
35. request environment 乱序；
36. observer state 为 FAIL，但日志中伪造 PASSED；
37. observer stdout 非空；
38. observer stderr 非空；
39. observer engine log 出现任意 rpytest 行；
40. observer completion 的字段数、顺序或类型错误；
41. 正向接受成功 stdout 中的 `[rpytest] [exc]`；
42. 正向接受 dummy renderer fallback 的 `error(...)` 文本。

RED、GREEN 顶层属性顺序和集合均恰为 `schema_version,verdict,fixture_gate,stream_gate,inputs,mutations,created_utc`，`schema_version=3`。`inputs` 每项属性恰为 `role,path,bytes,sha256`；`mutations` 每项属性恰为 `name,expected,actual,verdict`。

- RED 固定 `verdict="EXPECTED_RED"`，`fixture_gate` 属性恰为 `expected,observed,quit_call_count,returned_finish_codes,returns_97,returns_code,native_tail`，`stream_gate` 属性恰为 `selector,test_report_status_count,engine_log_status_count,expected_failure`，`mutations=[]`。
- GREEN 固定 `verdict="PASS"`，`fixture_gate` 使用同一属性集合且全部满足新结构，`stream_gate` 属性恰为 `selector,test_report_status_count,engine_log_rpytest_line_count,verdict`，`mutations` 恰有上述 42 个同序 PASS 元素。

RED、GREEN 均以 CreateNew、strict UTF-8、`Flush(true)`、strict 重读和只读方式发布。RED 必须先失败于预期旧契约，GREEN 必须后通过；二者都不能启动 Ren'Py、helper child 或 UI。

## generator test_report 合同

`generator-process/stdout.txt` 是唯一 rpytest 结果源，必须：

- 由 helper 以 CREATE_NEW 创建；
- 路径同时等于预声明路径、request `stdout_path` 与 result `stdout_path`；
- bytes > 0；
- strict UTF-8、无 BOM、无 NUL；
- 允许 LF 或 CRLF，不允许孤立 CR，非空文本必须以 LF 结束；
- 对物理 bytes 直接计算 bytes/SHA-256，不做换行归一化。

下列 .NET regex 按顺序分别表示：任意 Status 行、PASS Status 行、目标 testsuite 行、summary 标题、Python traceback 标题、fixture 证据写入失败标记：

```regex
(?m)^\[rpytest\] Status:[^\r\n]*\r?$
(?m)^\[rpytest\] Status:[ \t]+PASSED[ \t]*\r?$
(?m)^\[rpytest\] \[log\] - global\.terminal_collapse_legacy_generator[ \t]*\r?$
(?m)^\[rpytest\] Test outcomes \(Summary\)[ \t]*\r?$
(?m)^Traceback \(most recent call last\):[ \t]*\r?$
(?m)^TC_GENERATOR_EVIDENCE_WRITE_FAILURE[ \t]*\r?$
```

前四个 pattern 的匹配数必须各恰为 1，后两个必须各为 0。

不得把 `[rpytest] [exc]` 当作失败。`generator-process/stderr.txt` 必须恰为 0 bytes，并匹配空文件 SHA-256。

## generator engine_boot_log 合同

worktree `log.txt` 只作为 `engine_boot_log`：

- 必须存在、非空、strict UTF-8、无 BOM、无 NUL；
- 任意 `(?m)^\[rpytest\]` 行的匹配数必须为 0，以证明通道未混合；
- 以下三个高特异性致命 pattern 的匹配数必须各为 0：`(?m)^Traceback \(most recent call last\):[ \t]*\r?$`、`(?m)^I'm sorry, but an uncaught exception occurred\.[ \t]*\r?$`、`(?m)^TC_GENERATOR_EVIDENCE_WRITE_FAILURE[ \t]*\r?$`；
- 不得笼统拒绝 `error`，因为 dummy renderer 正常 fallback 含 `error('OpenGL support...')`；
- generator completion 前，以 CreateNew 逐字节复制到 `recovery-v3/generator-engine-log.txt`，核对 bytes/hash 后设为只读。

engine log 永远不能单独证明 rpytest PASS。

## 唯一 v3 generator attempt

v3 使用全新的、事先不存在的 worktree、外部 SaveDir、process evidence dir 与 attempt ledger。路径由 P3 固定，不能复用或别名到 v1/v2 目录。

`generator-attempt/attempt.json` 在任何 v3 generator entrypoint 启动前以 CreateNew、`Flush(true)`、strict 重读和只读方式创建。顶层属性顺序和集合恰为 18 项：

`schema_version,attempt_id,started_utc,approval_lock_sha256,approved_plan_commit,predecessor_manifest_sha256,red_record_path,red_record_sha256,green_record_path,green_record_sha256,worktree_path,savedir_path,process_evidence_dir,state_path,fixture_path,fixture_sha256,max_generator_invocations,retry_allowed`

固定语义为 schema 2、32 位小写十六进制 attempt ID、可 round-trip UTC 时间、v3 lock/P3/manifest/RED/GREEN 的当前 seal、全新规范绝对路径、`max_generator_invocations=1`、`retry_allowed=false`。

ledger 目录一旦存在即表示 v3 generator 权限已消费。任意 parse、transport、helper、Ren'Py、test report、state、save、completion 或证据封存失败都禁止删除 ledger、换 GUID、换 evidence root 或再次调用 generator。

generator request schema 维持 1，但必须精确验证：

- 9 个顶层字段、完整 argv、working directory、180000 ms timeout、stdout/stderr/result 绝对路径；
- `environment_overrides` 恰有 11 个元素；每项属性恰为 `name,value`，name 不重复；
- name 的 Ordinal 顺序恰为：`RENPY_NO_REDIRECT_STDIO,RENPY_PATH_TO_SAVES,RENPY_RENDERER,SDL_AUDIODRIVER,SDL_VIDEODRIVER,TC_EXPECTED_BASELINE_COMMIT,TC_EXPECTED_FIXTURE_SHA256,TC_EXPECTED_GAME_TREE,TC_EXPECTED_MARKER,TC_EXPECTED_SAVEDIR,TC_GENERATOR_RESULT`；
- 对应值依次为 `"1"`、null、`"sw"`、`"dummy"`、`"dummy"`、P3、fixture SHA、game tree、v3 marker、SaveDir 规范绝对路径、state 规范绝对路径；
- 任一缺失、额外、重复或乱序键均失败。

helper result 继续使用 exact 38-field schema v2，并通过中央 SafetyEnvelope：`classification=COMPLETED`、actual helper exit=0、persisted helper exit=0、root exit 为 integral 且等于 0、无 timeout、无可见窗口、Job drain/monitor/cleanup 全部通过、host-termination=false。PID/accounting 字段只作诊断，不参与 PASS。

state_report 顶层属性顺序和集合恰为 `actual,checks,failures,post_save_checks,reason,schema,slot_metadata,verdict`，固定 schema 1、`verdict="PASS"`、空 failures；它必须证明 native testcase、生产最终 Menu、chapter5.rpy:2807、空 return stack、顶层 context、真实三项选择路径、`intrigue=55`、`power=60`、`_iron_prepared=true`、两个准备战术可见、硬拼不可见、slot metadata 与 v3 marker/P3/game tree 完全一致。

## generator MultiLocation 合同

generator 成功后，递归查找目标 basename `1-1-*.save`，必须恰有三份：

1. 外部 SaveDir 根目录；
2. 同一外部 SaveDir 的 `sync/`；
3. generator worktree 的 `game/saves/` 根目录。

三份 target 的 basename、bytes、SHA-256、逐字节内容与 slot metadata 必须完全相同。autosave 与 persistent 是允许的非目标副产物，但必须记录并验证 exact relative inventory；不能声称 SaveDir 只有一个文件。

v2 的三份 target 与 v3 的三份 target 属于不同谱系。即使 SHA 偶然相同，v2 target 也不得成为 v3 completion、observer source 或 mother 的来源。

## generator completion schema v2

成功 generator completion 位于 `recovery-v3/generator-attempt/completion.json`。它必须在 request/result/stdout/stderr/state、fixture evidence、engine-log evidence 与三份 target 全部验证并设为只读后，才以 CreateNew、`Flush(true)`、strict 重读和只读方式创建。

顶层属性顺序和集合恰为 42 项：

`schema_version,attempt_id,attempt_path,attempt_sha256,approval_lock_sha256,approved_plan_commit,predecessor_manifest_sha256,red_record_sha256,green_record_sha256,worktree_path,savedir_path,process_evidence_dir,fixture_path,fixture_sha256,fixture_evidence_path,fixture_evidence_sha256,request_path,request_bytes,request_sha256,result_path,result_bytes,result_sha256,state_path,state_bytes,state_sha256,rpytest_stdout_path,rpytest_stdout_bytes,rpytest_stdout_sha256,stderr_path,stderr_bytes,stderr_sha256,engine_log_evidence_path,engine_log_evidence_sha256,external_save_path,sync_save_path,local_save_path,target_copy_count,save_name,save_bytes,save_sha256,save_inventory,finished_utc`

固定关系：

- `schema_version=2`、`target_copy_count=3`；
- `request_*` 精确绑定 strict 校验并只读封存的 helper request；
- `rpytest_stdout_*` 精确绑定 helper 持久 stdout；
- `stderr_*` 精确绑定 0-byte helper stderr；
- `engine_log_evidence_*` 精确绑定 worktree log 的 CreateNew 副本；
- 三个 save path 对应规定的 root/sync/local 位置，且 `save_*` 同时代表三份完全相同的 target；
- `save_inventory` 属性顺序和集合恰为 `roots,directories,files,target_count`。`roots` 属性恰为 `external_savedir,local_savedir`；`directories` 每项属性恰为 `root_role,relative_path`；`files` 每项属性恰为 `root_role,relative_path,kind,bytes,sha256`，以 `<root_role><TAB><relative_path>` 的 Ordinal 复合键排序并以 OrdinalIgnoreCase 判重。它必须逐项覆盖外部 SaveDir 与 local `game/saves` 的全部普通文件，`kind` 只能为 `target,autosave,persistent`，`target_count=3`，且三个 target 与 completion 顶层 path/seal 双向一致；
- 所有 bytes 字段先证明为 integral，再按 Int64 比较；不得用 `[int]$null`、字符串强转或缺省值通过；
- `finished_utc` 是可 round-trip 的 UTC 时间字符串。

任一失败都禁止 completion、observer、mother 与 cleanup。

## clean observer 与 mother

只有只读 generator completion 通过 strict 重读后，才能创建一个全新的 clean detached worktree、observer 外部 SaveDir、process evidence dir 与一次性 observer ledger。observer 是状态只读临时 `zz` 文件，通过普通 `run` 和 `RENPY_AUTO_LOAD=1-1` 加载 v3 save，不得进入 test 模式。

observer attempt schema 固定为 2，顶层属性顺序和集合恰为 19 项：

`schema_version,attempt_id,started_utc,approval_lock_sha256,approved_plan_commit,generator_completion_path,generator_completion_sha256,worktree_path,savedir_path,process_evidence_dir,state_path,fixture_path,fixture_sha256,source_save_path,source_save_bytes,source_save_sha256,replay_save_path,max_observer_invocations,retry_allowed`

它绑定 v3 lock、P3、generator completion、全新规范绝对路径、fixture hash、source v3 external-root target、replay 根目录 save，固定 `max_observer_invocations=1`、`retry_allowed=false`。ledger 创建与失败语义与 generator 相同。

observer 启动前必须递归证明：

- observer 外部 SaveDir 只有根目录中的一个目标 `1-1-*.save`；
- `sync/` 不含目标 slot；
- clean worktree `game/saves/` 不含目标 slot；
- replay copy 与 v3 generator 三份 target 逐字节相同。

observer request schema 维持 1，9 个顶层字段、完整 argv、120000 ms timeout 与三条 evidence path 必须精确。`environment_overrides` 恰有 12 个元素；每项属性恰为 `name,value`，name 不重复；name 的 Ordinal 顺序恰为：`RENPY_AUTO_LOAD,RENPY_NO_REDIRECT_STDIO,RENPY_PATH_TO_SAVES,RENPY_RENDERER,SDL_AUDIODRIVER,SDL_VIDEODRIVER,TC_EXPECTED_BASELINE_COMMIT,TC_EXPECTED_FIXTURE_SHA256,TC_EXPECTED_GAME_TREE,TC_EXPECTED_MARKER,TC_EXPECTED_SAVEDIR,TC_OBSERVER_RESULT`。对应值必须精确绑定 `"1-1"`、`"1"`、null、`"sw"`、两个 `"dummy"`、P3、observer fixture SHA、game tree、v3 marker、SaveDir 与 state 规范绝对路径；任一缺失、额外、重复或乱序键均失败。

observer state_report 顶层属性顺序和集合恰为 `actual,checks,failures,loaded,reason,schema,verdict`，固定 schema 1、`verdict="PASS"`、`loaded=true`、空 failures；它必须证明普通 `run`、非 test、autoload 已实际发生且 `actual.auto_load_value="1-1"`、生产最终 Menu、state、两个可见战术、空 return stack、slot metadata 与 marker 全部正确。仅 request 声称设置了 `RENPY_AUTO_LOAD` 不能替代进程内证明。

observer 成功路径要求：

- helper result 通过与 generator 相同的中央 SafetyEnvelope，root/helper exit 均为 0；
- helper stdout 与 stderr 均恰为 0 bytes；
- observer engine log 存在且非空，只执行 engine_boot_log 高特异性致命门禁，并要求任意 rpytest 行计数为 0；
- engine log 清理前逐字节复制为 `observer-engine-log.txt` 并设为只读；
- replay 根目录 save 在运行前后 bytes/hash 不变；
- 运行后 `sync/` 与 local 均未出现目标 `1-1`；允许 persistent 与空 `sync/` 目录；
- source、replay before/after 与 generator 的三份 target 全部逐字节一致。

observer completion schema 固定为 2，顶层属性顺序和集合恰为 41 项：

`schema_version,attempt_id,attempt_path,attempt_sha256,approval_lock_sha256,approved_plan_commit,generator_completion_sha256,worktree_path,savedir_path,process_evidence_dir,fixture_path,fixture_sha256,fixture_evidence_path,fixture_evidence_sha256,request_path,request_bytes,request_sha256,result_path,result_bytes,result_sha256,state_path,state_bytes,state_sha256,stdout_path,stdout_bytes,stdout_sha256,stderr_path,stderr_bytes,stderr_sha256,engine_log_evidence_path,engine_log_evidence_sha256,source_save_path,source_save_bytes,source_save_sha256_before,source_save_sha256_after,replay_save_path,replay_save_bytes,replay_save_sha256_before,replay_save_sha256_after,save_inventory,finished_utc`

request/result/stdout/stderr 均绑定同一只读 process evidence；stdout 与 stderr 都必须绑定 0-byte 空文件 seal；engine-log evidence 只作诊断。`save_inventory` 使用与 generator 相同的 exact nested schema，覆盖 observer 外部 SaveDir 与 local `game/saves` 的全部普通文件和相关目录；顶层 target_count=1，唯一 target 必须是未变的 external-root replay，任何 external-sync/local target 都失败，非目标 kind 只允许 `persistent`。其余字段连接 attempt、lock、P3、generator completion、worktree、SaveDir、fixture evidence、state、source/replay before/after seal 与完成时间。所有 bytes 字段先证明为 integral，再按 Int64 比较。

只有 observer completion 冻结后，才能把 v3 generator 的外部根 target 复制到 `recovery-v3/mother/`。mother 必须与 generator root/sync/local 三份 target、observer source/replay before/after 全部 basename、bytes、SHA-256 和逐字节一致，并设为只读。legacy 与 v2 candidate 永远不参与此步骤。

## Task 1 completion schema v3

新 completion 位于 `.superpowers/sdd/terminal-collapse-ending/recovery-v3/task1-completion.json`，以 CreateNew、strict UTF-8、无 BOM、末尾 LF、`Flush(true)`、strict 重读和只读方式创建。

顶层属性顺序和集合恰为：

`schema_version,verdict,approval,predecessor,baseline_game_tree,full_selftest,version_probe,generator,observer,mother,artifact_count,artifacts,cleanup,finished_utc`

嵌套属性顺序和集合固定为：

- `approval`：`lock_path,lock_bytes,lock_sha256,plan_path,plan_commit,plan_bytes,plan_sha256,spec_path,spec_commit,spec_bytes,spec_sha256`；
- `predecessor`：`manifest_path,manifest_bytes,manifest_sha256,artifact_count,catalog_bytes,catalog_sha256,failures,source_inventories`；其两个数组必须与 manifest 中对应值逐项、同序、同类型相等；
- `full_selftest`：`reused,attempt_path,attempt_bytes,attempt_sha256,completion_path,completion_bytes,completion_sha256,root_path`；
- `version_probe`：`reused,evidence_dir,request_sha256,stdout_sha256,stderr_sha256,result_sha256`；
- `generator`：`source,invocation_count,red_record_path,red_record_sha256,green_record_path,green_record_sha256,attempt_path,attempt_sha256,completion_path,completion_sha256,evidence_dir,request_sha256,result_sha256,state_path,state_sha256,rpytest_stdout_path,rpytest_stdout_bytes,rpytest_stdout_sha256,stderr_sha256,fixture_evidence_path,fixture_evidence_sha256,engine_log_evidence_path,engine_log_evidence_sha256,save_name,save_bytes,save_sha256,target_copy_count`；
- `observer`：`invocation_count,attempt_path,attempt_sha256,completion_path,completion_sha256,evidence_dir,request_sha256,result_sha256,state_path,state_sha256,stdout_sha256,stderr_sha256,fixture_evidence_path,fixture_evidence_sha256,engine_log_evidence_path,engine_log_evidence_sha256`；
- `mother`：`path,bytes,sha256,read_only`；
- `cleanup`：`generator_worktree_removed,generator_savedir_removed,observer_worktree_removed,observer_savedir_removed`；
- `artifacts` 每项：`path,bytes,sha256`。

固定语义：

- `schema_version=3`、`verdict="PASS"`；
- `approval` 绑定 v3 lock、P3 plan 与 S3 spec 的 path/commit/bytes/hash/raw blob；
- `predecessor` 绑定 schema-v2 manifest、`artifact_count=115`、catalog bytes/hash，以及 legacy/v2 两个 failure 的 exact classification/disposition；
- `full_selftest.reused=true`、`version_probe.reused=true`，并绑定既有冻结证据，禁止重跑；
- `generator.source="fresh_generator_v3"`、`invocation_count=1`，绑定 RED/GREEN、attempt/completion、result/state、test_report、fixture/engine-log evidence 与三份 target；
- `observer.invocation_count=1`，绑定 attempt/completion、result/state、空 stdout/stderr、fixture/engine-log evidence 与 save before/after；
- `mother` 绑定唯一只读 v3 mother；
- `cleanup` 只描述四个 v3 临时 worktree/SaveDir 的受控移除，四项成功时均为 true。

`artifact_count` 固定为 141，且必须等于 `artifacts.Length`。required union 双向精确相等：

1. predecessor manifest 的 115 个 current artifact，逐项 bytes/hash 不变；
2. 本规格“v3 证据命名空间与持久叶”中列出的 26 个新 durable leaf。

`artifacts` 使用规范绝对 path、Ordinal 排序、OrdinalIgnoreCase 判重，每项属性恰为 `path,bytes,sha256`。Task 1 completion 自身为避免自引用不在 141 项中。创建 completion 前、strict 重读后、清理后都必须重新证明 exact union 与 current physical seals。

`baseline-evidence.md` 必须明确记录各谱系调用数：legacy generator 1、v2 generator 1/v2 observer 0、v3 generator 1/v3 observer 1；只有 v3 generator/observer 产物可成为 mother。不得使用含糊的总 `generator_invocation_count=1`。

唯一允许的成功顺序固定为：冻结 generator completion → 冻结 observer completion → 冻结只读 mother → 受控清理四个 v3 临时路径 → 创建并冻结 baseline evidence → 重建 141-file union → 创建并冻结 Task 1 completion。Task 1 completion 的四个 cleanup 布尔值必须因此全部为 true。

## Task 2、Task 3 与 Phase B 迁移

Recovery v3 plan 必须完整重述下游 authority 消费者，禁止回退到 v1/v2 路径或 schema。

- Task 2 fresh context 的第一个项目动作先验证带外 v3 lock；随后 strict 读取 Task 1 schema-v3 completion，自身重哈希并逐项重哈希 exact 141 current artifact，才可开始 RED。
- Task 2 rules commit R3 必须是 P3 的直接子提交，只修改三个既定 game 路径。
- Task 2 的九次 invocation、14 字段 receipt schema v1 与 56 文件 exact union 保持不变；四个固定 authority seal 改为 v3 lock、Task 1 schema-v3 completion、P3 plan、S3 spec。
- Task 2 completion 升为 schema 3，顶层属性顺序和集合恰为 16 项：`schema_version,verdict,approved_plan_lock_sha256,task1_completion_path,task1_completion_sha256,approved_plan_commit,approved_spec_commit,rules_commit,rules_parent_commit,rules_subject,rules_paths,invocation_count,invocations,artifact_count,artifacts,finished_utc`。它绑定 P3/S3/R3、Task 1 schema-v3 physical hash、9 invocations/receipts 和 exact 56 artifacts。
- Task 3 在创建任一 Opus run 目录前及三次 Opus 的每一次前，重新验证带外 v3 lock、完整 P2→S3→P3→R3 直接父链、Task 1 schema-v3 completion/141 current artifacts、Task 2 schema-v3 completion/9 receipts/56 current artifacts；会话内固定两份 completion hash。
- Phase B 每个 fresh replay context 都必须重新验证带外 v3 lock、完整 P2→S3→P3→R3、Task 1 schema-v3 completion/141 current artifacts、Task 2 schema-v3 completion/9 receipts/56 current artifacts，并在会话内固定两份 completion hash；随后验证 mother current seal/read-only 与 completion 中冻结的 generator/observer lineage。不得读取、复制、探测或 fallback 到 legacy TIMEOUT candidate 与 v2 log-contract-mismatch candidate。
- Phase B replay 的 SaveDir 也使用递归 target cardinality：启动前只有母档根目录副本，启动后无 sync/local shadow target，允许 persistent 与空 sync。
- v3 generator/observer 的临时 worktree、SaveDir、source/replay target 在成功 cleanup 后已不存在。Task 2、Task 3 与 Phase B 只能验证 completion 中的历史 path/seal 关系和 141 个持久 artifact，不得要求这些已删除路径当前存在。

## 执行边界、失败与清理

- v3 generator 与 observer 各只有一次 invocation；任一失败即 terminal NEEDS_CONTEXT，不重试。
- generator completion 缺失时禁止 observer；observer completion 缺失时禁止 mother；Task 1 completion 缺失时禁止 Task 2。
- 所有 Ren'Py entrypoint 都必须通过已审核的 dedicated-host private-desktop wrapper；任意可见顶层窗口、用户交互、Computer Use、真实输入或 manual fallback 都停止。
- generator/observer 的 process filter 必须把外层 Win32_Process 对象保存到命名变量，并排除当前 `$PID`；禁止嵌套 `Where-Object` 复用 `$_` 导致属性错绑。
- E: worktree 的唯一补丁只能调用宿主 `apply_patch` 工具并使用精确绝对目标；不得通过已出现 `Access is denied` 的 `apply_patch.bat` shell 路径，也不得采用其他写文件后门。
- Task 1 不得再声称所有动作发生于单一 PowerShell session。宿主补丁边界前后必须以不可变 seal 与显式 checkpoint 连接；任何跨会话授权例外必须写入 handoff/baseline，不能伪装成逐字执行旧合同。
- 成功 cleanup 只能移除 v3 的 generator worktree、generator SaveDir、observer worktree 与 observer SaveDir。删除前重新读取冻结的 result/completion，不依赖会话临时变量；规范化并证明路径位于批准的 task-owned E: 根、Git worktree registration 匹配、相关进程为 0、证据副本和 mother 已冻结。
- v1/v2 lock、manifest、attempt、worktree、SaveDir、candidate、stdout、engine log 与所有失败证据永不进入 v3 cleanup 白名单。
- Ren'Py 在 AppData 写出的 backup 属于允许的非包体运行时副作用，不是 authority leaf；计划必须限定其路径和观察方式，不得把它误判成共享仓库漂移或主动删除。

## 验收合同

静态阶段必须证明：

- 新 spec/plan 分别是单路径直接父提交，P3 game tree 未变；
- predecessor manifest 只能重建出 exact 115 artifacts、24,660 catalog bytes 与固定 catalog SHA；
- v3 lock schema 3 的 26 个字段、路径、类型、拓扑和带外 hash 全部严格；
- RED 对旧日志选择器失败，GREEN 对新双通道验证器及上述 exact 42 个 mutation/control 通过；
- 所有 PowerShell fence 通过 Windows PowerShell 5.1 parser，所有 Python fence 通过 AST parse；
- generator/observer completion 与 Task 1/2 completion 的 exact schema、bytes integral gate、重复键拒绝、path relation、seal relation 与 artifact union 可由 fresh context 重建。

执行阶段必须证明：

- v3 generator ledger 在唯一调用前已冻结，调用恰为 1，helper 与双通道日志/state/三份 target 全部通过；
- v3 generator completion 已冻结后 observer 才启动，observer 调用恰为 1；
- observer 是普通 `run`，进程内证明 `RENPY_AUTO_LOAD=1-1`，save 不变且无 shadow target；
- mother 只来源于 v3，read-only，并与 generator/observer 所有 target seal 一致；
- Task 1 schema-v3 completion 能由 fresh Task 2 重哈希 exact 141 artifacts；
- Task 2 schema-v3 completion 能由 fresh Task 3 重哈希 exact 56 artifacts；
- 共享 `game/` tree 在 Task 2 前仍等于基线，protected winter plan 未变，索引与提交范围精确。

## 资产与包体

本设计只增加规格、计划与仓库外/ignored 治理证据，不需要美术、音乐、音效、动画、UI 或字体改动。helper、fixture 与证据不进入游戏包；Recovery v3 在 Task 2 之前对包体影响为 0。

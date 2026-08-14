# 终末崩盘旧存档生成器退出恢复设计

日期：2026-08-14

## 背景与目标

Phase A 已经完成一次通过的 private-desktop helper full selftest 和一次通过的 Ren'Py 版本探针。随后，旧存档生成器在真实最终战术菜单写出了 `generator-state.json` 和两份逐字节相同的 `1-1-LT1.save`，但 Ren'Py 根进程没有正常退出，180 秒后由 helper 安全终止。

本次恢复的目标是：**修正 testcase 的退出方式，在不改动或洗白任何旧证据的前提下，用一次全新的 generator 调用生成可正常退出的旧存档；再通过独立普通 `run` 回载，才冻结新的只读 mother，并让后续 Task 2、Task 3 和 Phase B 只信任新版证据链。**

## 已确认的失败事实

- 旧 Phase-A plan commit 是 `4c4bd4a1deae2f0f5f6fb8c76ca0d1a3de088aab`；其 `game/` tree 是 `fa7a398e9d989731b24e3c1642f3e2e33ce846ff`。
- 旧 approval lock 位于 `.superpowers/sdd/terminal-collapse-ending/approved-plan-lock.json`，恰为 327 bytes，SHA-256 为 `284B639B47ED716B1EBF706B939E1A2E9BC224261351390DF45DCAD9A900D46C`。
- full selftest 只调用过一次并通过；attempt 为 623 bytes、SHA-256 `65DB315FE280720B6DD98489D652A48A3204A2956B1A67BBEAD0AF5505805B08`，completion 为 1,839 bytes、SHA-256 `E22F9CC759EC30B73A0EB00089835FE184C75F8B6F58CABCF93AACAE0F19162D`。
- 版本探针只调用过一次并通过；其 helper result 为 1,658 bytes、SHA-256 `90A4A70292E68373B7AB1834CFDD61C73F842290CF59D96E934A22C9098ABDB4`。
- 失败 generator 的 helper result 为 `TIMEOUT`、`helper_exit_code=21`、`timed_out=true`，SHA-256 为 `65A789696D25390CFC827FAA7A2C19D150B67A3EC2161AC44DFD79ADBEE57D13`。
- 失败 generator 的 state 文件虽为 `PASS`，SHA-256 为 `82014869E02AEB3E18B7F7D6230C6789BDA05955A345AF4B9348C13D283E79ED`，但它不能覆盖 helper 的 TIMEOUT。
- 失败 worktree 的 fixture SHA-256 为 `497064A9DFCA721D1A6ED3A941A9DB0DC8DB92C489AD22F4E1ECF58A74E4CCC3`；外部与本地 save 均为 733,069 bytes、SHA-256 `E24D04A5F71BBBC13086D68EA09C4F746A2CE2DB1C9D5865BB7769C1DF9036DB`。
- helper 在超时后证明 `job_active_processes_final=0`、`job_drained=true`、`cleanup_complete=true`、零可见窗口；这证明安全终止成功，不证明 generator 正常完成。

## 根因

失败 fixture 在 testcase 的 Python 节点 `$ _tc_generate_legacy_save()` 内调用 `renpy.quit()`。

Ren'Py 8.5.2 的 `testast.Python.execute()` 只有在 Python 代码正常返回后才推进到下一个测试节点。`renpy.quit()` 先让测试执行器进入 `EndPhase`，再抛出 `QuitException`；`NodeExecutor.execute()` 只有在当前测试节点本身是原生 `Exit` 时才重新抛出该异常。当前节点是 `Python`，异常因此被吞掉，测试停在生产 choice screen，根进程继续存活直到 helper 超时。

原生 testcase `exit` 节点会正确传播 `QuitException`，由 test reporter 把通过或失败映射为操作系统退出码 0 或 1。本次修复必须使用这一条 SDK 原生路径，不得用 `os._exit()`、`SystemExit`、直接杀进程或延长 timeout 掩盖问题。

## 不在本次范围内

- 不接纳、复制、改名或晋升本次 TIMEOUT 调用生成的 save。
- 不重跑 helper full selftest或版本探针。
- 不修改旧 design、旧 Phase-A plan、旧 approval lock 或任何旧失败证据。
- 不修改 `game/` 生产脚本、可见文案、数值、结局键、成就、字体、资产或包元数据。
- 不改变 private-desktop helper 的 C#、wrapper 或 selftest 源码。
- 不放宽 TIMEOUT、可见窗口、非零退出或不完整 cleanup 的 fail-closed 语义。

## 方案比较

### 方案 A：原地修改旧 spec 与旧 plan

文件更少，但会让旧 approval lock 不再认证其原始物理字节，也要在一份接近八千行的计划中迁移所有 authority 字段。遗漏任何一处都会让 Task 2 或 Task 3 回退到旧证据链，因此不采用。

### 方案 B：新增独立 recovery spec、plan 与 lock（采用）

旧 spec、plan、lock 和失败证据保持逐字不变。新恢复链显式引用前任 authority，使用新证据命名空间和一次性调用 ledger；Task 1 completion、Task 2 与 Task 3 只接受新版 authority。文件略多，但审计边界最清楚。

### 方案 C：直接接纳现有 save

最省时间，但现有 helper outcome 是 TIMEOUT，且尚无正常 `run` observer、只读 mother 或 Task 1 completion。接纳它会把失败诊断证据洗成通过证据，因此禁止。

## 提交与 authority 拓扑

提交必须是单线直接父链：

```text
P1  4c4bd4a1deae2f0f5f6fb8c76ca0d1a3de088aab  旧 Phase-A plan
 |
S2  recovery spec commit，只新增本文件
 |
P2  recovery plan commit，只新增 recovery plan
 |
R   Task 2 rules commit，只修改 game/balance.rpy、game/difficulty.rpy、game/test_game.rpy
```

- `S2^` 必须等于 P1；`P2^` 必须等于 S2；`R^` 必须等于 P2。
- `P2:game` 必须仍为 `fa7a398e9d989731b24e3c1642f3e2e33ce846ff`。
- 新 recovery plan 位于 `docs/superpowers/plans/2026-08-14-terminal-collapse-generator-recovery.md`。
- 旧 spec 与旧 plan 继续由旧 lock 认证；新 spec 与新 plan 由新 lock 认证。

## 前任证据清单

在创建新 lock 前，控制器以 CreateNew、strict UTF-8、无 BOM、末尾 LF、`Flush(true)` 和只读方式创建：

`.superpowers/sdd/terminal-collapse-ending/recovery-v2/predecessor-evidence.json`

顶层属性顺序和集合恰为：

1. `schema_version=1`
2. `purpose="terminal-collapse-generator-recovery-predecessor"`
3. `predecessor_plan_commit`
4. `predecessor_lock_sha256`
5. `artifact_count`
6. `catalog_bytes`
7. `catalog_sha256`
8. `artifacts`
9. `failed_generator`
10. `created_utc`

不得从“执行时当前还存在的文件”重新建立基线。创建 manifest 之前，控制器必须从下列 **13 个固定叶文件**与 **7 个固定递归根**重建唯一候选集合；任何缺失、额外成员、reparse point、大小写别名或重复绝对路径都停止：

固定叶文件：

1. `$ProjectRoot\.superpowers\sdd\terminal-collapse-ending\approved-plan-lock.json`
2. `$ProjectRoot\docs\superpowers\plans\2026-08-11-terminal-collapse-ending-phase-a.md`
3. `$ProjectRoot\docs\superpowers\specs\2026-08-11-terminal-collapse-ending-design.md`
4. `$ProjectRoot\.superpowers\sdd\terminal-collapse-ending\helpers\PrivateDesktopRunner.cs`
5. `$ProjectRoot\.superpowers\sdd\terminal-collapse-ending\helpers\Invoke-PrivateDesktopProcess.ps1`
6. `$ProjectRoot\.superpowers\sdd\terminal-collapse-ending\helpers\Test-PrivateDesktopRunner.ps1`
7. `E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-private-desktop-selftest-d37d19e4adfc4b5fb3622abcc8a53212\short-lived-pid-coverage\result.json`
8. `$ProjectRoot\.superpowers\sdd\terminal-collapse-ending\helper-v2-full-selftest-attempt\attempt.json`
9. `$ProjectRoot\.superpowers\sdd\terminal-collapse-ending\helper-v2-full-selftest-attempt\completion.json`
10. `$ProjectRoot\.superpowers\sdd\terminal-collapse-ending\legacy\generator-state.json`
11. `E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-generator-c2958b40c6044ce598e56263855c071d\game\zz_terminal_collapse_legacy_fixture.rpy`
12. `E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-generator-c2958b40c6044ce598e56263855c071d\log.txt`
13. `$ProjectRoot\.superpowers\sdd\terminal-collapse-task-1-report-v2.md`

固定递归根及其精确普通文件数：

1. `E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-private-desktop-selftest-409c3edd2e2c412e8e5221f4774e2448`：35
2. `$ProjectRoot\.superpowers\sdd\terminal-collapse-ending\legacy\renpy-version-process`：4
3. `$ProjectRoot\.superpowers\sdd\terminal-collapse-ending\legacy\generator-process`：4
4. `E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-generator-c2958b40c6044ce598e56263855c071d\game\saves`：6
5. `E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-generator-save-44f1b1204d3f4222a019a2a41335d6a6`：12
6. `$ProjectRoot\.superpowers\sdd\terminal-collapse-ending\legacy\interrupted-attempt`：1
7. `E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-old-save-1f027ab224b74d8890172376314ea3b1`：8

控制器把 83 个绝对规范路径用 `[StringComparer]::Ordinal` 排序。每行精确为 `<path><TAB><decimal bytes><TAB><UPPERCASE SHA256><LF>`，整份 catalog 使用 strict UTF-8、无 BOM、末尾 LF。重建结果必须精确满足：

- `artifact_count=83`；
- `catalog_bytes=17959`；
- `catalog_sha256="4358AFED212D66C3F0BD50F26F01DEC37BF4061139C5A22EEF79FA38948C80D6"`。

`artifacts` 必须与这 83 行逐项、同序、同值对应；每项属性恰为 `path,bytes,sha256`。路径以 Ordinal 排序，并以 OrdinalIgnoreCase 判重；`artifact_count` 必须同时等于数组长度与 83。manifest 创建后还要 strict 重读、重建 catalog 并再次得到同一 bytes/hash，随后才设为只读。

下列关键 seal 还必须独立精确验证，不能只依赖 catalog 总哈希：旧 lock `284B639B47ED716B1EBF706B939E1A2E9BC224261351390DF45DCAD9A900D46C`；旧 plan `87D14B4C03B5F935B3FB5A36E1AE8D446337E592AAD6FAF668DB33168AFCF757`；旧 spec `F7C833952D0F783A922FFF18F6F0A2B9F44BA8F1BF31520917FA6B1237B1A232`；三份 helper `E0393DB1E113FDB8C35097978AA73B7D33AFDD5788499002B6423D883DEED4E8`、`73A3F9C43CF994E08F004E0A1266122A3EC5E0EAF065C63E6D9439CF0B0E1880`、`20198B669F70E51E51F71BD01E6D06D1949D300F43CE9A94FB0190A47D781A15`；d37d result `300515E17B8EDD6B0CD99C268E685DCAE6770BC664B5C28F231F231F03E9F27B`；full attempt/completion `65DB315FE280720B6DD98489D652A48A3204A2956B1A67BBEAD0AF5505805B08` / `E22F9CC759EC30B73A0EB00089835FE184C75F8B6F58CABCF93AACAE0F19162D`；version result `90A4A70292E68373B7AB1834CFDD61C73F842290CF59D96E934A22C9098ABDB4`；TIMEOUT result/state `65A789696D25390CFC827FAA7A2C19D150B67A3EC2161AC44DFD79ADBEE57D13` / `82014869E02AEB3E18B7F7D6230C6789BDA05955A345AF4B9348C13D283E79ED`；旧 fixture `497064A9DFCA721D1A6ED3A941A9DB0DC8DB92C489AD22F4E1ECF58A74E4CCC3`；interrupted report/log `0312AC00D64A9C43CA5B67A42F0170F411222B8C91962A556EC1AF4B6F674D27` / `EA0799C53B982E25B8E6E19111EDC2982D5B1225F7793D5562D8E4AA02ABA595`。

`failed_generator` 的属性顺序和集合恰为 `classification,helper_exit_code,result_path,result_sha256,state_path,state_sha256,candidate_save_disposition`；固定值为 `TIMEOUT`、21、上述 result/state 路径与 hash、`preserved_not_used`。manifest 不得移动、复制或删除任何来源文件，也不得把 TIMEOUT save 列为新 mother 的来源。

## 新 approval lock

新 lock 路径固定为：

`.superpowers/sdd/terminal-collapse-ending/approved-plan-lock-v2.json`

它以 CreateNew、strict UTF-8、无 BOM、末尾 LF、`Flush(true)` 和只读方式创建，并必须被 Git ignore。其 SHA-256 由控制器在每个 fresh Task 1/2/3 上下文中通过 `$ApprovalLockSha256` 带外传入。

顶层属性顺序和集合恰为：

1. `schema_version`
2. `purpose`
3. `approved_plan_path`
4. `approved_plan_commit`
5. `plan_sha256`
6. `spec_path`
7. `spec_commit`
8. `spec_sha256`
9. `predecessor_plan_commit`
10. `predecessor_lock_path`
11. `predecessor_lock_bytes`
12. `predecessor_lock_sha256`
13. `predecessor_manifest_path`
14. `predecessor_manifest_bytes`
15. `predecessor_manifest_sha256`
16. `baseline_game_tree`
17. `generator_attempt_ledger_path`
18. `generator_attempt_limit`
19. `observer_attempt_ledger_path`
20. `observer_attempt_limit`

固定语义：

- `schema_version=2`；
- `purpose="terminal-collapse-generator-recovery"`；
- `predecessor_plan_commit` 等于 P1；
- `predecessor_lock_bytes=327`；
- `predecessor_lock_sha256` 等于 `284B639B47ED716B1EBF706B939E1A2E9BC224261351390DF45DCAD9A900D46C`；
- `baseline_game_tree="fa7a398e9d989731b24e3c1642f3e2e33ce846ff"`；
- `generator_attempt_ledger_path` 等于 `.superpowers/sdd/terminal-collapse-ending/recovery-v2/generator-attempt` 的绝对规范路径；
- `generator_attempt_limit=1`；
- `observer_attempt_ledger_path` 等于 `.superpowers/sdd/terminal-collapse-ending/recovery-v2/observer-attempt` 的绝对规范路径；
- `observer_attempt_limit=1`。

所有消费者必须拒绝重复键、额外键、字段乱序、类型转换、非法 UTF-8、BOM、大小写漂移、物理/提交 blob 不一致，以及任一 predecessor seal 漂移。

## 退出修复的测试先行合同

动态 generator 之前必须运行一个不启动 Ren'Py 的纯 Python AST/结构 gate。

### RED

对旧失败 fixture 运行 gate，必须精确证明：

- 生成函数内 `.quit()` 调用数为 2；
- 以 `return` 语句调用 `finish` 的状态码集合为空；
- `finish()` 没有 `return 97`；
- `finish()` 没有 `return code`；
- testcase 尾部不是“赋值状态、断言、原生 exit”。

RED 输出必须绑定旧 fixture 的 8,749 bytes 和 SHA-256 `497064A9DFCA721D1A6ED3A941A9DB0DC8DB92C489AD22F4E1ECF58A74E4CCC3`。错误原因必须是退出结构缺失，而不是解析错误。

### GREEN

新 fixture 的 `finish()` 只负责原子发布结果并返回状态：

```renpy
def finish(verdict, reason, payload, code):
    payload.update({"schema": 1, "verdict": verdict, "reason": reason})
    try:
        if (not result_path) or (not o.path.isabs(result_path)):
            raise Exception("TC_GENERATOR_RESULT must be absolute")
        temp = result_path + ".tmp-" + str(o.getpid())
        raw = (j.dumps(payload, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
        with open(temp, "xb") as stream:
            stream.write(raw)
            stream.flush()
            o.fsync(stream.fileno())
        o.rename(temp, result_path)
    except Exception:
        print("TC_GENERATOR_EVIDENCE_WRITE_FAILURE")
        print(tb.format_exc())
        return 97
    return code
```

四个终止分支调用 `finish` 时，最后一个位置参数必须分别为 41、42、0 和 43，并把其返回值直接 `return`。testcase 尾部必须精确为：

```renpy
$ _tc_generator_status = _tc_generate_legacy_save()
assert eval (_tc_generator_status == 0)
exit
```

GREEN gate 必须精确证明：

- 生成函数内 `.quit()` 调用数为 0；
- `finish()` 同时含 `return 97` 和 `return code`；
- 以 `return` 语句调用 `finish` 的状态码集合恰为 `[0, 41, 42, 43]`；
- testcase 最后三条语句与上述结构一致。

状态 0 写 PASS，断言通过，再由原生 `exit` 产生 OS 0。状态 41、42、43 或 97 让断言失败，再由原生 `exit` 产生 OS 1。不得在 Python test node 内调用 `renpy.quit()`。

### RED/GREEN 持久证据

RED 与 GREEN 不能只留在控制台，也不能在后续阶段重新计算后冒充调用时结果。控制器须分别以 CreateNew、strict UTF-8、无 BOM、末尾 LF、`Flush(true)`、strict 重读和只读方式创建：

- `.superpowers/sdd/terminal-collapse-ending/recovery-v2/generator-structure-red.json`
- `.superpowers/sdd/terminal-collapse-ending/recovery-v2/generator-structure-green.json`

两份记录的顶层属性顺序和集合恰为 `schema_version,phase,verdict,fixture_path,fixture_bytes,fixture_sha256,parse_error_count,quit_call_count,returned_finish_codes,finish_returns_97,finish_returns_code,native_tail,created_utc`。字段必须是原生 JSON 类型，不允许字符串强转为数字或布尔值。

- RED 固定为 `schema_version=1`、`phase="RED"`、`verdict="EXPECTED_FAILURE"`、`fixture_bytes=8749`、旧 fixture hash、`parse_error_count=0`、`quit_call_count=2`、`returned_finish_codes=[]`、三个布尔值均为 false。
- GREEN 固定为 `schema_version=1`、`phase="GREEN"`、`verdict="PASS"`、新 fixture 的调用时 path/bytes/hash、`parse_error_count=0`、`quit_call_count=0`、`returned_finish_codes=[0,41,42,43]`、三个布尔值均为 true。

两份记录的 physical bytes/hash 必须在 generator attempt 创建前冻结；GREEN 的 `fixture_sha256` 必须与 attempt、实际 worktree fixture、helper request 和 generator completion 中的 fixture seal 完全相同。

## 新 recovery 证据命名空间

新版链只能写入 `.superpowers/sdd/terminal-collapse-ending/recovery-v2/`：

```text
recovery-v2/
├── predecessor-evidence.json
├── generator-structure-red.json
├── generator-structure-green.json
├── generator-attempt/
│   ├── attempt.json
│   └── completion.json
├── generator-process/
├── generator-state.json
├── generator-fixture.rpy
├── generator-log.txt
├── observer-attempt/
│   ├── attempt.json
│   └── completion.json
├── observer-process/
├── observer-state.json
├── observer-fixture.rpy
├── observer-log.txt
├── mother/
├── baseline-evidence.md
├── task1-completion.json
└── rules/
```

旧 `legacy/generator-process/`、`legacy/generator-state.json`、失败 worktree、失败 SaveDir、旧 full/version 证据和旧 lock 永不覆盖、移动或清理。

## 唯一 generator attempt

新 generator 启动前必须 CreateNew、`Flush(true)` 并设为只读：

`.superpowers/sdd/terminal-collapse-ending/recovery-v2/generator-attempt/attempt.json`

顶层属性顺序和集合恰为：

1. `schema_version=1`
2. `attempt_id`：32 位小写十六进制
3. `started_utc`
4. `approval_lock_sha256`
5. `approved_plan_commit`
6. `predecessor_manifest_sha256`
7. `red_record_path`
8. `red_record_sha256`
9. `green_record_path`
10. `green_record_sha256`
11. `worktree_path`
12. `savedir_path`
13. `process_evidence_dir`
14. `state_path`
15. `fixture_path`
16. `fixture_sha256`
17. `max_generator_invocations=1`
18. `retry_allowed=false`

所有 path 均为事先声明的绝对规范路径，且必须位于各自批准的 recovery-v2 或 repository-external 临时根。attempt 的 RED/GREEN path/hash 必须等于两份只读结构记录；fixture path/hash 必须等于 GREEN 记录。`generator-attempt/` 一旦存在就表示唯一机会已经消费。不得删除目录、换 GUID、覆盖 attempt 或创建第二个 generator evidence root。

新 generator 必须使用全新的 detached worktree、外部 SaveDir、fixture、state 路径和 helper evidence 路径。以下条件全部成立后，才允许 CreateNew、flush、只读 `completion.json`：

- wrapper classification 为 `COMPLETED`；
- `helper_exit_code=0`、非空且为整数的 `root_exit_code=0`；
- `timed_out=false`、`host_termination_required=false`；
- private-desktop、Job、monitor、drain 和 cleanup 全部安全门通过；
- `visible_windows=[]`；
- generator state 为 PASS；
- 外部与 worktree-local `1-1-*.save` 各恰有一份，文件名、字节数、SHA-256 和逐字节内容相同；
- Ren'Py log 非空，并且恰有一个该 testcase 的 `PASSED` 结果，不含 FAILED、ERROR、traceback 或 timeout。

成功时创建的 `generator-attempt/completion.json` 顶层属性顺序和集合恰为：

`schema_version,attempt_id,attempt_path,attempt_sha256,approval_lock_sha256,approved_plan_commit,predecessor_manifest_sha256,red_record_sha256,green_record_sha256,worktree_path,savedir_path,process_evidence_dir,fixture_path,fixture_sha256,fixture_evidence_path,fixture_evidence_sha256,result_path,result_bytes,result_sha256,state_path,state_bytes,state_sha256,log_path,log_bytes,log_sha256,log_evidence_path,log_evidence_sha256,external_save_path,local_save_path,save_name,save_bytes,save_sha256,finished_utc`

它必须逐字段连接到同一次 attempt 的既定路径和 seal，并满足：

- `attempt_id`、attempt path/hash、approval/new-plan/predecessor authority 与 attempt 完全相同；
- RED/GREEN seal 与 attempt 完全相同，实际 fixture 的 current bytes/hash 等于 GREEN 与 completion；
- result/state/log path 分别位于 attempt 声明的 process evidence、state 与 worktree；其 bytes/hash 是动态调用结束后首次严格验证的值；实际 fixture 与 log 还须在清理前以 CreateNew 复制到固定的 `generator-fixture.rpy` / `generator-log.txt`，逐字节相等后写入 evidence path/hash；
- `external_save_path` 与 `local_save_path` 分别位于 attempt 声明的外部 SaveDir 和 worktree `game/saves`，basename 均等于 `save_name`，且 bytes/hash/逐字节内容相同；
- completion 只能在完整 helper、state、log 和双 save gate 通过后 CreateNew、`Flush(true)`、strict 重读并设为只读。

若新 generator 返回 TIMEOUT、NEEDS_CONTEXT、LAUNCH_ERROR、非零 root exit、可见窗口、state FAIL 或日志不完整，即使又写出了 save/state，也必须停止；不得启动 observer、建立 mother、写 Task 1 completion、清理失败 worktree/SaveDir 或重试。

## clean observer 与 mother

只有新 generator completion 通过后，才能创建全新的 clean detached worktree 和外部 SaveDir。observer 必须是状态只读的临时 `zz` 文件，通过普通 `run` 和 `RENPY_AUTO_LOAD=1-1` 加载新 save，且不得进入 test 模式。

observer 也有独立的一次性账本。启动前须 CreateNew、`Flush(true)`、strict 重读并设为只读：

`.superpowers/sdd/terminal-collapse-ending/recovery-v2/observer-attempt/attempt.json`

其顶层属性顺序和集合恰为：

`schema_version,attempt_id,started_utc,approval_lock_sha256,approved_plan_commit,generator_completion_path,generator_completion_sha256,worktree_path,savedir_path,process_evidence_dir,state_path,fixture_path,fixture_sha256,source_save_path,source_save_bytes,source_save_sha256,replay_save_path,max_observer_invocations,retry_allowed`

固定语义为 `schema_version=1`、32 位小写十六进制 attempt ID、`max_observer_invocations=1`、`retry_allowed=false`。所有 path 事先声明；source save 必须是 generator completion 中的外部 save，replay save 必须是 observer 专属外部 SaveDir 中的同 basename 副本。`observer-attempt/` 一旦存在就表示机会已消费，不得删除、覆盖、换 GUID 或使用第二个 evidence root。

observer 必须重新证明：

- provenance marker、P2 commit、game tree、三项真实选择路径和最终菜单位置准确；
- `intrigue=55`、`power=60`、`_iron_prepared=True`；
- context/return stack/node 仍是生产最终战术 Menu；
- 两个准备战术可见，硬拼不可见；
- helper 为 `COMPLETED`、root 0、零窗口、无超时、完整 drain/cleanup；
- 外部候选 save 在 observer 前后字节和 SHA-256 不变；
- clean worktree 不产生本地 `1-1-*.save`。

成功时创建的 `observer-attempt/completion.json` 顶层属性顺序和集合恰为：

`schema_version,attempt_id,attempt_path,attempt_sha256,approval_lock_sha256,approved_plan_commit,generator_completion_sha256,worktree_path,savedir_path,process_evidence_dir,fixture_path,fixture_sha256,fixture_evidence_path,fixture_evidence_sha256,result_path,result_bytes,result_sha256,state_path,state_bytes,state_sha256,log_path,log_bytes,log_sha256,log_evidence_path,log_evidence_sha256,source_save_path,source_save_bytes,source_save_sha256_before,source_save_sha256_after,replay_save_path,replay_save_bytes,replay_save_sha256_before,replay_save_sha256_after,finished_utc`

completion 必须逐字段连接到 observer attempt；source 与 replay 的 before/after hash 四者均等于 generator completion 的 `save_sha256`，bytes 相等，且调用结束后逐字节比较仍一致。实际 observer fixture 与 log 在清理前以 CreateNew 复制到固定的 `observer-fixture.rpy` / `observer-log.txt`，逐字节相等后写入 evidence path/hash。只有 helper、安全 envelope、普通 `run` state、log、无本地 slot 和 save 不变性全部通过后，才允许 CreateNew、`Flush(true)`、strict 重读并设为只读。任何失败均保留现场、禁止 mother、禁止 Task 1 completion、禁止重试。

只有 observer completion 通过后，才把新 generator 的外部引擎文件复制到 `recovery-v2/mother/`，再次核对 generator source、observer replay 与 mother 三者 basename、bytes、SHA-256 和逐字节内容相同，并把 mother 设为只读。TIMEOUT attempt 的 save 永远不参与这一步。

## Task 1 completion schema v2

新 completion 位于：

`.superpowers/sdd/terminal-collapse-ending/recovery-v2/task1-completion.json`

它以 CreateNew、strict UTF-8、无 BOM、末尾 LF、`Flush(true)` 和只读方式创建。顶层属性顺序和集合恰为：

1. `schema_version=2`
2. `verdict="PASS"`
3. `approval`
4. `predecessor`
5. `baseline_game_tree`
6. `full_selftest`
7. `version_probe`
8. `generator`
9. `observer`
10. `mother`
11. `artifact_count`
12. `artifacts`
13. `cleanup`
14. `finished_utc`

嵌套属性集合：

- `approval`：`lock_path,lock_bytes,lock_sha256,plan_path,plan_commit,plan_bytes,plan_sha256,spec_path,spec_commit,spec_bytes,spec_sha256`；
- `predecessor`：`manifest_path,manifest_bytes,manifest_sha256,artifact_count,catalog_bytes,catalog_sha256,failed_generator_classification,failed_generator_result_sha256,failed_generator_state_sha256,candidate_save_disposition`；
- `full_selftest`：`reused,attempt_path,attempt_bytes,attempt_sha256,completion_path,completion_bytes,completion_sha256,root_path`，其中 `reused=true`；
- `version_probe`：`reused,evidence_dir,request_sha256,stdout_sha256,stderr_sha256,result_sha256`，其中 `reused=true`；
- `generator`：`source,invocation_count,red_record_path,red_record_sha256,green_record_path,green_record_sha256,attempt_path,attempt_sha256,completion_path,completion_sha256,evidence_dir,result_sha256,state_path,state_sha256,fixture_evidence_path,fixture_evidence_sha256,log_evidence_path,log_evidence_sha256,save_name,save_bytes,save_sha256`，其中 `source="fresh_generator_v2"`、`invocation_count=1`；
- `observer`：`invocation_count,attempt_path,attempt_sha256,completion_path,completion_sha256,evidence_dir,result_sha256,state_path,state_sha256,fixture_evidence_path,fixture_evidence_sha256,log_evidence_path,log_evidence_sha256`，其中 `invocation_count=1`；
- `mother`：`path,bytes,sha256,read_only`；
- `cleanup`：`generator_worktree_removed,generator_savedir_removed,observer_worktree_removed,observer_savedir_removed`，四项均为 true；
- `artifacts`：每项属性恰为 `path,bytes,sha256`。

`candidate_save_disposition` 必须等于 `preserved_not_used`。completion 的 mother 只能来自 `fresh_generator_v2`，且 `mother.sha256` 必须等于 generator `save_sha256` 与 observer completion 的四个 before/after save hash。

`artifact_count` 不是说明性数字。它必须等于 `artifacts.Length`，且固定为 109。`artifacts` 使用绝对规范 path，以 `[StringComparer]::Ordinal` 排序，以 OrdinalIgnoreCase 判重，并与下列 required union 做双向 exact set equality：

1. predecessor manifest 中精确 83 个 artifact path，且 current bytes/hash 仍与 predecessor seal 相同；
2. 下列精确 26 个持久叶文件：新版 lock、新 recovery spec、新 recovery plan、predecessor manifest、RED record、GREEN record、generator attempt、generator completion、generator `request.json/stdout.txt/stderr.txt/result.json`、generator state、generator fixture evidence、generator log evidence、observer attempt、observer completion、observer `request.json/stdout.txt/stderr.txt/result.json`、observer state、observer fixture evidence、observer log evidence、唯一 mother、`baseline-evidence.md`。

`task1-completion.json` 本身为避免自引用不在 109 项中。创建 completion 前必须逐项重哈希 109 个 current leaf；创建并 Flush 后 strict 重读，重新证明 schema、`artifact_count=109`、排序、唯一性、exact union、嵌套 seal 与每个 current file 一致，再设为只读。成功 worktree/SaveDir 只有在其 fixture/log 已复制到固定 evidence leaf、generator/observer completion 已冻结、mother 已冻结后才能清理；清理后这 109 个持久文件仍须全部存在并可供 fresh Task 2 重哈希。

## Task 2、Task 3 与 Phase B 迁移

recovery plan 必须完整重述后续 Task 2、Task 3 和 Phase B 的 authority 消费者，不得让执行者回退到旧 Phase-A plan 的硬编码路径。

- Task 2 fresh context 的第一个项目动作必须用带外 `$ApprovalLockSha256` 验新版 lock；随后 strict 读取 `recovery-v2/task1-completion.json` schema v2，拒绝重复/额外/乱序键和类型转换，重新计算 completion 自身 seal，并逐项重哈希其精确 109 个 artifact。缺一项或多一项都不得开始 RED。
- Task 2 rules commit R 必须是 P2 的直接子提交，仍只修改 `game/balance.rpy`、`game/difficulty.rpy`、`game/test_game.rpy`。
- Task 2 的九次 invocation、14 字段 receipt schema v1、调用时 seal 和完成时 56 文件 exact union 保持原行为。
- 四个固定 authority seal 改为“新 lock、Task 1 schema v2 completion、新 recovery plan、新 recovery spec”，因此 union 仍为 56，不得增减。
- Task 2 completion 升为 schema v2；顶层属性顺序和集合恰为 `schema_version,verdict,approved_plan_lock_sha256,task1_completion_path,task1_completion_sha256,approved_plan_commit,approved_spec_commit,rules_commit,rules_parent_commit,rules_subject,rules_paths,invocation_count,invocations,artifact_count,artifacts,finished_utc`。它固定 `schema_version=2`、`verdict="PASS"`、P2、S2、新 lock 与 Task 1 schema v2 physical hash，且仍要求 9 invocations、9 receipts、56 exact artifacts。CreateNew、`Flush(true)`、strict 重读和只读合同不变。
- Task 3 fresh context 在创建任一 Opus run 目录之前，并在三次 Opus 的每一次之前，都必须重新验证带外新版 lock、P2→R、Task 1 schema v2 completion 自身 seal及其全部 109 个 current artifact、Task 2 schema v2 completion 自身 seal、九张 receipt 和 exact 56 union；会话内固定 Task 1/Task 2 completion hash，任一漂移立即 hard stop。
- Phase B 的每一个 fresh replay context 都必须接收同一个带外新版 lock hash，strict 验 lock、Task 1 schema v2 completion、109 个 current artifact、mother current bytes/hash/read-only 与 generator/observer lineage，然后才从新版 mother 创建各自副本。不得读取、复制或探测 TIMEOUT candidate；不得以旧 lock 或旧 Task 1 路径 fallback。

## 失败处理与清理

- 所有 helper/Ren'Py/Opus 调用保持 one-shot；任一失败不重试。
- 不使用 Computer Use、真实鼠标键盘、当前桌面、可切换桌面或手工 fallback。
- 失败时保留本次 worktree、SaveDir、state、logs、request/stdout/stderr/result 和 ledger。
- 只在 generator 与 observer 均成功、证据已封存后，才清理这两个成功的 recovery worktree/SaveDir。
- predecessor manifest、两个 lock、所有旧失败证据、full/version 证据、新 mother 和 completion 永不清理。
- 共享仓库 index 必须为空；除受保护的 winter narrative plan 外，不允许额外未跟踪或已修改文件。

## 验收合同

设计与计划阶段：

- recovery spec 与 plan 各自为单文件提交，父链和 game tree 精确；
- 所有 PowerShell fence 由 Windows PowerShell 5.1 parser 通过；
- 所有 Python fence可由 AST 解析；
- 退出结构 gate 对旧 fixture 先 RED，对计划内新 fixture 再 GREEN，两份调用时记录均 CreateNew、Flush、只读并由 generator attempt 封存；
- predecessor manifest 只能由固定 83 文件目录生成，catalog 精确为 17,959 bytes / `4358AFED212D66C3F0BD50F26F01DEC37BF4061139C5A22EEF79FA38948C80D6`；
- 新 lock、manifest、generator/observer attempt 与 completion 的 schema、重复键、类型、路径、bytes 和 SHA-256 有机械验证；
- Task 1 completion 的 109 文件 exact union、Task 2 的 56 文件 exact union及下游逐项 current rehash 均能由 fresh context 重建。

执行阶段：

- full selftest 新调用数为 0；版本探针新调用数为 0；
- 新 generator 调用数恰为 1；observer 调用数在 generator 成功后恰为 1；
- generator 正常退出并满足完整安全 envelope、状态、日志与双 save 合同；
- observer 通过普通 `run` 证明无 fixture 依赖；
- mother 只读且来源、observer 副本和 recorded seal 一致；
- generator 与 observer 的一次性 ledger 各只有一个 attempt 和一个成功 completion；
- Task 1 completion schema v2 可由 fresh Task 2 严格消费并重哈希全部 109 个持久 artifact；
- 共享 `game/` tree 在 Task 2 前仍为原始 tree。

## 资产与包体

本恢复只新增文档、ignored evidence 和临时 fixture，不新增或修改美术、音乐、音效、动画、UI、字体或 shipping game 文件。Task 1 完成前包体影响为 0；后续规则修复仍只涉及既定三个 `.rpy` 文件，资产需求继续为无。

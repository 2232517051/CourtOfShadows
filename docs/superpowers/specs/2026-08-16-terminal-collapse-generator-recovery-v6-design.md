# Terminal Collapse Generator Recovery v6 Design

Date: 2026-08-16

Status: approved design for a future independently reviewed P6; this document creates no runtime authority and authorizes no recovery execution.

## Decision

Recovery v6 is the sole recovery path after the failed v5 preapproval ceremony. S6 is a direct child of S5 and adds only this file. Its commit subject is exactly:

`docs: specify terminal collapse generator recovery v6`

The lineage is fresh and append-only:

```text
S5  failed governing v5 specification; P5 never existed
 |
S6  this design, sole-path commit
 |
P6  future recovery-v6 plan, sole-path commit
 |
R6  future Task 2 rules commit
```

The only permitted S6 path is:

`docs/superpowers/specs/2026-08-16-terminal-collapse-generator-recovery-v6-design.md`

P6 has fixed path and subject:

- `docs/superpowers/plans/2026-08-16-terminal-collapse-generator-recovery-v6.md`;
- `docs: plan terminal collapse generator recovery v6`.

`P6^=S6`. R6 cannot exist before successful v6 Task 1 completion. `R6^=P6`, its subject is exactly `fix: enforce terminal resistance collapse rules`, and it changes exactly the three Task 2 paths frozen below.

Recovery v6 ends when the Task 2 completion leaf has authenticated R6 and the complete 9/14/56 evidence union. It has no Task 3 and no continuation phase. Copy generation, comparison, selection, and replay belong to a later, separate spec/plan/lock lineage created after R6.

## Frozen repository facts

### S5 and the last sealed authority

S5 is commit `2e1aa2b5c3a0618a8e4b4c6fcde4a1278437a651`, with subject `docs: specify terminal collapse generator recovery v5`. It is the direct child of P4 commit `dccc785595f8551392c23db4a3a8d517fc6ef528`.

The committed S5 leaf is:

- path `docs/superpowers/specs/2026-08-15-terminal-collapse-generator-recovery-v5-design.md`;
- 125,148 bytes;
- SHA-256 `9C9021157556FF97BEAC753F99E9F0749750568972EA14FF7908B9087862C3A1`;
- Git blob `6650234bdaf5b024d08e9f1b8abc1c2fb8d55c44`.

P4 remains:

- 1,008,828 bytes;
- SHA-256 `E6F296A527C0A5247F5A87AFB7B47829C91C29D864A140B5344E33BFC3AFED09`;
- Git blob `3cbf0fc952e47a2239e1b07e468682cd6feae42c`.

The baseline `game` tree is still `fa7a398e9d989731b24e3c1642f3e2e33ce846ff`. The protected winter plan is `docs/superpowers/plans/2026-08-09-winter-interlude-narrative-delivery.md`, SHA-256 `0F39B5F5ACE1D4666DD146863CABDF398B031F5666C29AE337CEB89796E4276C`.

The last genuinely sealed execution authority remains P3/S3/L3/M3. S4/P4 and S5 are preserved failure-history artifacts, not retroactive children of L3. M6 carries the exact S4 v3 `terminal_failure`, the exact v5 P4 `controller_failure`, and the new v5 `preapproval_failure` as three distinct objects.

### P5, M5, and L5 never existed

There is no P5 plan leaf or P5 commit. The planned path was:

`docs/superpowers/plans/2026-08-15-terminal-collapse-generator-recovery-v5.md`

It is physically absent. The fixed M5 path `.superpowers/sdd/terminal-collapse-ending/recovery-v5/predecessor-evidence.json`, the fixed L5 path `.superpowers/sdd/terminal-collapse-ending/approved-plan-lock-v5.json`, and the entire `recovery-v5` runtime root are absent. No v5 admission, RED, GREEN, attempt, process, state, completion, mother, baseline, rules, copy, or result authority exists.

The failed preapproval did not authorize or consume an M5, L5, Task 0, or Task 1 opportunity. It did permanently invalidate the S5-to-P5 design route: S5 may be preserved as history but may never be completed by publishing P5.

### P4 terminal prepublication failure

P4 remains a terminal prepublication failure with no M4, L4, recovery-v4 root, helper launch, Ren'Py launch, generator invocation, observer invocation, or candidate save. Its ordered defects remain:

1. `GET_FILEHASH_COMMAND_UNAVAILABLE_IN_FRESH_WINPS51_SCOPE`;
2. `GIT_LS_FILES_TEXT_QUOTED_EIGHT_UTF8_PATHS`;
3. `GIT_EXIT_STATUS_NOT_CHECKED_BEFORE_ZERO_RESULT_INTERPRETATION`.

No attempt transcript, stdout/stderr capture, or physical P4 failure report exists. M6 must not invent one.

## Failed v5 preapproval ceremony

### Exact observed compiler failure

The ignored preapproval package attempted one and only one seed compiler invocation. It made zero A invocations and zero B invocations. The compiler observation was:

- executable `C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe`;
- 2,569,832 bytes;
- SHA-256 `46809206887326D2D24DB1EFF1F3064DE972C3451ABE766B49111450A5E08E00`;
- file/product version `4.8.9221.0`;
- working directory `C:\Users\22325\AppData\Local\Temp\CourtOfShadows-P5-Preapproval-Seed`;
- `UseShellExecute=false`;
- `CreateNoWindow=true`;
- environment names exactly `ComSpec,SystemRoot,TEMP,TMP,windir`;
- exit code `1`;
- wrapper failure `P5_PREAPPROVAL_SEED_EXIT:1`.

The exact arguments were:

```text
"/nologo" "/noconfig" "/nostdlib+" "/deterministic+" "/debug-" "/optimize+" "/target:library" "/platform:anycpu" "/filealign:512" "/codepage:65001" "/utf8output" "/pathmap:C:\Users\22325\AppData\Local\Temp\CourtOfShadows-P5-Preapproval-Seed=X:\p5" "/reference:C:\Windows\Microsoft.NET\Framework64\v4.0.30319\mscorlib.dll" "/reference:C:\Windows\Microsoft.NET\Framework64\v4.0.30319\System.dll" "/reference:C:\Windows\Microsoft.NET\Framework64\v4.0.30319\System.Core.dll" "/out:C:\Users\22325\AppData\Local\Temp\CourtOfShadows-P5-Preapproval-Seed\P5NativeAdapter.dll" "C:\Users\22325\AppData\Local\Temp\CourtOfShadows-P5-Preapproval-Seed\P5NativeAdapter.cs"
```

Stdout and stderr were not redirected. Their exact bytes and text are therefore unknown, not empty. No compiler diagnostic artifact exists. The selected classic .NET Framework compiler did not advertise the `/deterministic` or `/pathmap` option strings while the invocation required both. The strongest supported diagnosis is command-option rejection before source compilation. No C# source line is proven to have failed and S6 does not fabricate one.

No assembly was accepted, no seed bytes became authority, and no source, compiler, closure, or adapter fact from this ceremony is an input to v6.

### Ignored nonauthority source seals

The following four ignored leaves are recorded only as failure chronology:

| Path | Bytes | SHA-256 |
|---|---:|---|
| `.superpowers/sdd/terminal-collapse-ending/p5-preapproval/IMPLEMENTATION_PLAN.md` | 8,096 | `EAEC12BF0A64CBFE5B0FF659A60FFAF0B965B3D85211466E5484350F8EF84B3B` |
| `.superpowers/sdd/terminal-collapse-ending/p5-preapproval/tests/Test-P5Preapproval.ps1` | 3,387 | `CB98B46D521030864CA3172CA8A7E9F0B17E3058125E4A3534E61F12A6E15D57` |
| `.superpowers/sdd/terminal-collapse-ending/p5-preapproval/scripts/Invoke-P5Preapproval.ps1` | 27,467 | `D9A4120E84339D7370D73D29CF4D66EEC91BA55377CD757348C7E43B0D442686` |
| `.superpowers/sdd/terminal-collapse-ending/p5-preapproval/src/P5NativeAdapter.cs` | 20,532 | `E86FBE2ADCAA5696349DE42691B56D1718CB4F8F732B6C2469C83DD65C74B827` |

They are not M6 artifacts, do not enter the 127-row catalog, do not become L6 or runtime authority, and are not subject to a v6 freeze or read-only requirement. M6 publication, L6 publication, and every v6 task must not open or depend on them. Later deletion or drift of an ignored leaf does not change v6 authority.

The independent nonauthority inventory observed exactly 4 leaves totaling 59,482 bytes. Its 390-byte content catalog has SHA-256 `CCDD3A17255ADA9B7A01EFFE43B21222D0078693D5841DD0940D3CDD0DDD51DC`. It observed exactly six directories; `facts`, `evidence`, and `appendix` existed but were empty. These counts and seals describe failure chronology only. P6, M6, L6, their independent reviewers, and every later v6 scope are permanently forbidden to read any package leaf or use this package inventory as current-state authority.

### Cleanup observations

After the failed invocation, no compiler process remained and all five explicitly named temporary roots were proved absent:

1. `C:\Users\22325\AppData\Local\Temp\CourtOfShadows-P5-Preapproval-Seed`;
2. `C:\Users\22325\AppData\Local\Temp\CourtOfShadows-P5-Preapproval-A`;
3. `C:\Users\22325\AppData\Local\Temp\CourtOfShadows-P5-Preapproval-B`;
4. `C:\Users\22325\AppData\Local\Temp\CourtOfShadows-P5-Preapproval-Closure-A`;
5. `C:\Users\22325\AppData\Local\Temp\CourtOfShadows-P5-Preapproval-Closure-B`.

These are preserved observations, not reusable roots. Recovery v6 names none of them. The only v6 compilation scratch is the separately named, nonproject, transient `PrivateDesktopRunnerV6` scratch table below; it is not a recovery namespace or authority root.

## Commit and namespace topology

The v6 namespace is:

`.superpowers/sdd/terminal-collapse-ending/recovery-v6/`

The fixed M6 and L6 paths are:

- M6: `.superpowers/sdd/terminal-collapse-ending/recovery-v6/predecessor-evidence.json`;
- L6: `.superpowers/sdd/terminal-collapse-ending/approved-plan-lock-v6.json`.

Except for S6, P6, and L6, every new persistent recovery leaf is inside `recovery-v6`. No v4 or v5 path may be adopted, repaired, renamed, copied, deleted as cleanup, or used as fallback. Every v6 path is distinct from every earlier path.

S6, P6, and R6 each have the one-path or exact-three-path topology defined here. S6 and P6 preserve the baseline `game` tree. R6 is the first permitted v6 commit to change `game`.

This design approval creates neither M6 nor L6 and does not authorize P6 publication, controller execution, helper execution, Ren'Py, generator, observer, or rules work.

## M6 predecessor manifest

M6 is published only after independent review has authenticated S6, P6, the current one-path commit topology, the last sealed authority, all 127 known artifact paths, and the absent-or-exactly-empty ordinary `recovery-v6` root. The fresh publisher receives the reviewed uppercase physical P6 SHA plus the independently reviewed bootstrap bytes/SHA. P6 is its first and only pre-body project leaf: the bootstrap checks P6 existence and its .NET stream SHA before it extracts or executes the uniquely marked M6-publisher block. Before that comparison succeeds it may not read S6, Git, an earlier authority, or any other project leaf. The authenticated block then revalidates S6, topology, the last sealed authority, and the complete current-state contract before any write.

The controller excludes concurrent project or recovery-root writers for this publication. It creates the fixed directory only as an empty ordinary non-reparse setup container, proves the exact empty child set immediately before the leaf operation, and opens M6 through `FileStream(FileMode.CreateNew)`. Successful CreateNew of `predecessor-evidence.json`, not idempotent directory creation, consumes the M6 publication opportunity. Strict UTF-8 without BOM, LF-only with exactly one terminal LF, durable flush, strict duplicate-key-aware reread, and read-only freeze are mandatory. Any subsequent failure preserves the root and created state, forbids retry/delete/recreate/alternate root, and requires another append-only lineage. A failure before M6 CreateNew consumes no M6 opportunity; it may leave only the exact empty setup root. A later separately authorized continuation may accept that root only after proving it ordinary, non-reparse, identity-stable, and exactly empty under the same no-concurrent-writer premise. It never deletes, renames, or adopts a nonempty or unproved root.

M6 schema is 5. Its exact 22 ordered top-level fields are:

`schema_version,purpose,last_sealed_plan_commit,last_sealed_spec_commit,last_sealed_lock_path,last_sealed_lock_bytes,last_sealed_lock_sha256,last_sealed_manifest_path,last_sealed_manifest_bytes,last_sealed_manifest_sha256,immediate_failed_spec_commit,missing_plan_path,missing_plan_present,artifact_count,catalog_bytes,catalog_sha256,artifacts,terminal_failure,controller_failure,preapproval_failure,source_inventories,created_utc`

Fixed relations are:

- `schema_version=5`;
- `purpose="terminal-collapse-generator-recovery-v6-predecessor"`;
- last-sealed plan/spec/lock/manifest bind P3/S3/L3/M3 at their exact physical seals;
- `immediate_failed_spec_commit=2e1aa2b5c3a0618a8e4b4c6fcde4a1278437a651`;
- `missing_plan_path="docs/superpowers/plans/2026-08-15-terminal-collapse-generator-recovery-v5.md"`;
- `missing_plan_present=false`;
- `artifact_count=127`;
- `catalog_bytes=27437`;
- `catalog_sha256="082B7B01E93437173FB97BD3764D14D8290ACE05F6E9CE48667F2D51921CA13F"`;
- `created_utc` is a round-trippable UTC string.

### Exact 127-artifact union

The union is exactly the 126 physical artifacts frozen by S5 plus the committed S5 spec leaf. The prior 126 are M3's 115 rows plus S3, P3, L3, M3, the v3 RED, patched fixture, Task 1 brief, retry authority, merged v3 failure report, S4, and P4. The 127th member is S5.

Catalog rows are exact `<canonical absolute path><TAB><decimal bytes><TAB><UPPERCASE SHA256><LF>`, sorted with `StringComparer.Ordinal` and rejected on an OrdinalIgnoreCase collision. `artifacts` rows have exact ordered fields `path,bytes,sha256`. Review authenticates the M6 leaf, exact schema, exact known allowlist, count, and catalog constants before opening any path declared by M6. Only after the allowlist passes may it stream-hash all 127 leaves and rebuild 27,437/`082B7B01E93437173FB97BD3764D14D8290ACE05F6E9CE48667F2D51921CA13F`. The ignored preapproval leaves and 61 excluded v2 cache leaves are never probed or promoted.

### M6 failure objects

`terminal_failure` is the exact S4 v3 terminal-failure object with its exact 28-field schema, two historical attempts, checkpoint anomaly, frozen seals/topology, zero generator/observer invocation counts, `artifact_disposition="preserved_not_used"`, and `candidate_save_disposition="not_created"`.

`controller_failure` is the exact 19-field P4 object, ordered:

`classification,program_outcome,reason,final_status,final_failure_stage,failed_plan_commit,failed_spec_commit,defects,m4_path,m4_present,l4_path,l4_present,recovery_root_present,helper_launch_count,renpy_launch_count,generator_invocation_count,observer_invocation_count,artifact_disposition,candidate_save_disposition`

It retains `CONTROLLER_STATIC_CONTRACT_FAILURE`, `NOT_INVOKED`, `PREPUBLICATION_CONTROLLER_CONTRACT_INVALID`, `NEEDS_CONTEXT`, `M4_PREPUBLICATION`, P4/S4, the ordered three defects, absent M4/L4/root, all four launch/invocation counts zero, `preserved_terminal_prepublication`, and `not_created`.

`preapproval_failure` has exactly these 22 ordered fields:

`classification,program_outcome,reason,final_status,final_failure_stage,governing_spec_commit,planned_plan_path,planned_plan_present,p5_commit_present,m5_path,m5_present,l5_path,l5_present,recovery_root_present,seed_invocation_count,seed_exit_code,authoritative_build_a_invocation_count,authoritative_build_b_invocation_count,diagnostic_capture,diagnostic_artifact_present,accepted_adapter_disposition,namespace_disposition`

Its fixed values and relations are:

- `classification="PREAPPROVAL_BUILD_CONTRACT_FAILURE"`;
- `program_outcome="SEED_INVOKED_FAILED"`;
- `reason="V5_SEED_EXIT_1_WITHOUT_DIAGNOSTIC_CAPTURE"`;
- `final_status="NEEDS_CONTEXT"`;
- `final_failure_stage="P5_PREAPPROVAL_SEED_BUILD"`;
- `governing_spec_commit` is S5;
- `planned_plan_path` is the missing P5 path and `planned_plan_present=false`;
- `p5_commit_present=false`;
- M5/L5 paths are their fixed v5 paths and both present flags are false;
- `recovery_root_present=false`;
- seed/A/B invocation counts are 1/0/0 and `seed_exit_code=1`;
- `diagnostic_capture="not_configured_by_v5_seed_exception"`;
- `diagnostic_artifact_present=false`;
- `accepted_adapter_disposition="not_admitted"`;
- `namespace_disposition="never_created"`.

The object records the program outcome, not imagined compiler diagnostics. The four ignored leaf seals and five absent-root observations remain prose-level nonauthority chronology and are not inserted into the M6 artifact union.

### Source inventories

`source_inventories` retains exactly the three ordered sealed inventories from S5: v2 generator worktree task-owned 8/61, v2 generator SaveDir 12/0, and v3 generator worktree task-owned 1/0 containing only the 8,845-byte patched fixture with SHA-256 `A0D2A8B0589CC64F9479CE8E5B3315760001AA965502D1D740D35C6A2D558381`.

Each inventory has exact fields `id,root_path,authority_file_count,authority_files,excluded_cache_count,excluded_cache_files`; each leaf has `relative_path,bytes,sha256`. Ordering is Ordinal and paths are OrdinalIgnoreCase-unique. No v4 or v5 source inventory exists.

## L6 approval lock

L6 is created only after independent C0/I0 review of S6, P6, and M6. The fresh publisher receives the reviewed uppercase physical M6 SHA as authority and the separately reviewed uppercase physical P6 SHA as literal-transport binding. Its first project-leaf operation is the M6 existence check followed immediately by a .NET stream SHA comparison. P6 is the second allowed project leaf and must match the transport binding before the reviewed body is executed. A word such as `READY` cannot replace either hash.

L6 uses CreateNew, strict UTF-8 without BOM, LF-only with one terminal LF, durable flush, strict duplicate-key-aware reread, and read-only freeze. Its reviewed uppercase physical SHA is the first-leaf authority supplied out of band to each later fresh Task 1 or Task 2 scope.

L6 schema is 6. Its exact 42 ordered fields are:

`schema_version,purpose,approved_plan_path,approved_plan_commit,plan_bytes,plan_sha256,spec_path,spec_commit,spec_bytes,spec_sha256,immediate_predecessor_commit,missing_plan_path,missing_plan_present,last_sealed_plan_commit,last_sealed_spec_commit,last_sealed_lock_path,last_sealed_lock_bytes,last_sealed_lock_sha256,predecessor_manifest_path,predecessor_manifest_bytes,predecessor_manifest_sha256,predecessor_artifact_count,predecessor_catalog_bytes,predecessor_catalog_sha256,baseline_game_tree,execution_strategy,superseded_namespace,superseded_disposition,preserved_failure_report_path,preserved_failure_report_bytes,preserved_failure_report_sha256,task1_admission_ledger_path,task1_admission_limit,generator_attempt_ledger_path,generator_attempt_limit,observer_attempt_ledger_path,observer_attempt_limit,test_result_stream,engine_log_role,state_real_number_policy,execution_authorization_required,task1_admission_schema`

Fixed relations are:

- `schema_version=6`, `purpose="terminal-collapse-generator-recovery-v6"`;
- approved plan/spec bind P6/S6 paths, commits, physical bytes/SHA, and raw Git blobs;
- `immediate_predecessor_commit=S5`;
- the missing predecessor plan is the P5 path and is absent;
- last-sealed plan/spec/lock bind P3/S3/L3;
- predecessor manifest binds physical M6 at exact 127/27,437/`082B7B01E93437173FB97BD3764D14D8290ACE05F6E9CE48667F2D51921CA13F`;
- baseline game tree is `fa7a398e9d989731b24e3c1642f3e2e33ce846ff`;
- `execution_strategy="literal_encoded_winps51_dotnet_sha_fresh_namespace_global_one_shot"`;
- superseded namespace is the absent canonical `recovery-v5` path and `superseded_disposition="not_created_preapproval"`;
- preserved failure report fields bind only the actual v3 merged report;
- admission and attempt paths point only into `recovery-v6`;
- all three limits are 1 and `task1_admission_schema=1`;
- `test_result_stream="helper_stdout"`;
- `engine_log_role="diagnostic_only"`;
- `state_real_number_policy="decimal_or_finite_double"`;
- `execution_authorization_required=true`.

M6 publication does not authorize L6. L6 publication does not authorize Task 1. Task 1 and Task 2 require their own explicit user authorization.

## Task 0 static admission review

Task 0 is a separately authorized, fresh static review after L6 publication and independent L6 review. Its first project leaf is L6 and its second project leaf is P6, each authenticated from the reviewed physical hash exactly as later task scopes require. It may use the fixed Git byte seam only for read-only topology and current-seal queries; it creates no project or recovery leaf and performs no Git mutation.

Task 0 proves the complete `P2→S3→P3→S4→P4→S5→S6→P6` topology, the S6/P6 sole-path commits, the baseline game tree, the protected winter seal, M6 schema 5/22/127 and L6 schema 6/42, the absent P5/M5/L5/recovery-v5 lineage, and the absent v6 admission/runtime/temporary roots. It lexically verifies that the four ignored preapproval leaves are excluded nonauthority chronology and does not open them. P6 freezes an exact closed count and order of read-only Git operation rows for this proof; Task 0 must launch exactly that many authenticated `git.exe` roots and no other Git row. Helper, Ren'Py, Python, scanner, Claude, and Opus launch counts and the durable-write count are all zero. A mismatch stops without repair, cleanup, retry, or Task 1 authorization.

Task 0 success is a typed static review result delivered to the authorizing controller; it is not a new durable authority leaf and does not consume the Task 1 opportunity. Repeating Task 0 requires a new explicit external authorization and the byte-identical P6 transport, but no executable body contains an automatic retry branch. Task 0 success does not authorize Task 1.

## P6 controller boundary

### Abolished v5 machinery and versioned private-desktop boundary

P6 contains no precompiled adapter, embedded assembly, seed build, A/B build, deterministic-build attestation, general controller compiler, Roslyn, Task 3, Claude or Opus launcher, setup token, credential capability, blind map, selection input, replay body, or Phase B phase table/vector. These are deletions from the design, not substitutions with another general compiler or launcher.

The two previously sealed helper files remain authenticated historical artifacts but are not executable v6 transport:

- `.superpowers/sdd/terminal-collapse-ending/helpers/PrivateDesktopRunner.cs`, 82,334 bytes, SHA-256 `E0393DB1E113FDB8C35097978AA73B7D33AFDD5788499002B6423D883DEED4E8`;
- `.superpowers/sdd/terminal-collapse-ending/helpers/Invoke-PrivateDesktopProcess.ps1`, 24,229 bytes, SHA-256 `73A3F9C43CF994E08F004E0A1266122A3EC5E0EAF065C63E6D9439CF0B0E1880`.

P6 must not dot-source or invoke either file. Their PATH-sensitive `Get-Command powershell.exe`, nested `-File` host, inherited environment, target stdout/stderr `CREATE_NEW` disk handles without an active byte cap, and unbounded `ReadAllText(result.json)` cannot satisfy the v6 boundary.

P6 instead contains exactly one uniquely marked strict-UTF-8 C# source block and one PowerShell adapter block for `PrivateDesktopRunnerV6`. Their exact bytes, SHA-256 values, markers, public surface, referenced assemblies, compiler executable/input-file seals/single-root trust classification, nonproject compile-scratch inventory, and result schema are frozen by P6. The only compile-scratch roots are `C:\Users\22325\AppData\Local\Temp\CourtOfShadows-V6-PrivateDesktop-Review`, `C:\Users\22325\AppData\Local\Temp\CourtOfShadows-V6-PrivateDesktop-Task1`, and `C:\Users\22325\AppData\Local\Temp\CourtOfShadows-V6-PrivateDesktop-Task2`, selected only by the matching phase and all required absent before P6 approval.

The sole compilation route is an immutable `Invoke-V6Process` operation row for the already recorded `C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe`, 2,569,832 bytes/SHA-256 `46809206887326D2D24DB1EFF1F3064DE972C3451ABE766B49111450A5E08E00`. P6 independently freezes the ordinary/non-reparse executable, its config/startup input files, the three exact reference assemblies, clean environment, working directory, finite deadline, stdout/stderr caps, allowed exit, and complete argv. It makes no runtime loaded-module claim. The argv uses only P6-listed classic-csc-supported switches; it explicitly omits unsupported `/deterministic` and `/pathmap`, response/config defaults, and debug output, and it never reuses the v5 argv wholesale. Reusing an individually reviewed supported switch or one of the same framework references is not described as reusing the failed ceremony.

After P6 authority succeeds, the controller creates its phase scratch, writes only authenticated `PrivateDesktopRunnerV6.cs` through CreateNew, and invokes the bounded compiler row to produce only `PrivateDesktopRunnerV6.dll`. Exact hash-pinned classic csc with this closed argv is a narrowly declared single-root trust assumption, not a Job/debug proof of zero short-lived descendants or loaded modules. P6 review must explicitly accept that assumption, exercise the row under poisoned nonproject inputs, and prove the observed root-only production interface; runtime acceptance depends only on root exit, both clean EOF states, allowed exit, exact scratch/output child set, fixed input post-seals, and absence of any surviving related process in the bounded pre/post census. Timeout, overflow, an unexpected surviving process/write, input drift, or unproved root exit/EOF/census returns no loadable bytes and stops `NEEDS_CONTEXT`. No statement infers unobserved short-lived-child or module facts from `ProcessStartInfo`.

Before Task 1 admission or a Task 2 RED, the controller requires the runner type absent, opens the bounded DLL through the same ordinary/non-reparse deny-write/delete FileStream discipline, validates its PE/CLR/public-surface constraints, and loads only that byte array with `System.Reflection.Assembly.Load(byte[])`. The exact type must then be present with the reviewed public surface. Source and DLL are deleted non-followingly only after compiler exit is proved; the scratch is proved absent before recovery continues, and the exact six-key controller environment is re-proved. Compilation/load failure, a preloaded type, or cleanup uncertainty is terminal with no second source, cached assembly, `Add-Type`, nonprivate fallback, or retry. The compiled assembly bytes are ephemeral execution material, never M6/L6/checkpoint authority. P6 review uses the review scratch and the same bounded compiler row before M6/L6 exist; Task 1 and Task 2 use their own roots only after L6/P6 authority.

The v6 runner creates a fresh private desktop and Job, captures target stdout and stderr through two anonymous pipes, starts both finite cap-enforcing readers before the sole resume, and atomically admits the suspended target to the Job with an exact handle list. Cap-plus-one, reader fault, timeout, visible window, unexpected process, or result-schema fault terminates the Job and permits no parseable output. PASS requires target exit, both clean EOF states, Job ActiveProcesses zero, exact process accounting, window-monitor completion, desktop cleanup, bounded byte buffers, and the reviewed SafetyEnvelope. It never gives the target a stdout/stderr disk handle and never uses `ReadToEnd`, `ReadAllText`, PATH discovery, `-File`, an inherited semantic environment, or a second PowerShell host. Only after the in-memory result and bounded streams pass may the controller create the fixed evidence leaves. P6 review may compile and exercise this source only with nonproject synthetic clean/overflow/timeout/window/descendant fixtures; it does not run recovery, Ren'Py, generator, observer, scanner, release preparation, Claude, or Opus.

### Literal Windows PowerShell transport

Every controller scope uses the absolute native 64-bit image `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe`, Desktop PowerShell 5.1, `-NoLogo -NoProfile -NonInteractive -EncodedCommand`, and one independently reviewed small bootstrap. The bootstrap is strict UTF-16LE without BOM, NUL, or unpaired surrogate; base64 is canonical and padded; its decoded bytes/SHA, encoded length, six-token argv order, quote round trip, and complete command-line length including terminal NUL are frozen by P6 and must fit the 32,767-UTF-16-code-unit CreateProcess boundary. The bootstrap is not a compressed full task body.

Dynamic authority values and phase-typed inputs are canonical bounded data, never interpolated code. `-Command`, `-File`, temporary scripts, stdin script text, here-string transport, shell expansion, alternate encoding, fallback launcher, and retry transport are forbidden. The initial program uses PowerShell language and .NET only. Module autoload is set to `None` and inherited `PSModulePath` is cleared before project access.

If a later reviewed body needs a Utility cmdlet, it imports only the absolute native Desktop manifest `$PSHOME\Modules\Microsoft.PowerShell.Utility\Microsoft.PowerShell.Utility.psd1` after the first-leaf authority and second-leaf transport gates. It verifies the provider/module/assembly against P6's fixed table before use. No other module import is implicit. `Get-FileHash` is forbidden everywhere.

The controller computes SHA-256 only through `System.Security.Cryptography.SHA256` over a `FileStream` opened from the exact canonical ordinary non-reparse leaf. `Open-V6AuthenticatedLeaf` performs one bounded read under a retained read-only handle whose sharing denies write and delete, returns the immutable content buffer plus identity/length/hash metadata, and keeps that same handle live through parsing/body completion; authority bytes are never hash-then-reopened. Length, EOF, identity, share mode, uppercase formatting, disposal, and a second metadata reproof are explicit. Hashing has no cmdlet dependency.

The bootstrap reads only a bounded canonical ASCII data frame before project access. P6 freezes the exact frame cap, phase names, authority/transport SHA fields, block names/SHA values, input-vector names/types/caps, terminal marker, and rejection grammar. Frame content is data and is never interpreted as code.

Project-leaf order is phase-specific. M6 publication uses P6 as its first and aliased authority/transport leaf. L6 publication uses M6 first and P6 second as specified above. Every post-L6 Task 0, Task 1, or Task 2 scope receives the reviewed uppercase L6 physical SHA as authority and the separately reviewed uppercase P6 physical SHA as transport binding; L6 is first and P6 second. Before the phase's first-leaf .NET hash matches, no other project leaf or Git operation is allowed. Only after P6 matches may the bootstrap extract the exact shared and phase blocks from the already authenticated P6 byte buffer through unique byte markers, verify their P6-frozen bytes/SHA and strict UTF-8 round trip, and execute them in memory with `ScriptBlock.Create`. The bootstrap never reopens P6, reads an ambient script, uses `-File`, treats frame data as code, or accepts an unlisted block. P6 freezes and tests the complete extraction/signature/duplicate-marker/oversize/mutated-block and 32,767-versus-32,768 command-line boundary controls.

### Fixed Git binary and five-DLL closure

P6 uses no PATH discovery and no `cmd\git.exe` shim. Its sole Git executable is:

- `C:\Users\22325\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\git\mingw64\bin\git.exe`;
- 4,344,704 bytes;
- SHA-256 `C115A66A1BEDE6694B513AF420CC90F8775BE03666A54D1ECB82D6196B929FE9`;
- version `git version 2.53.0.windows.3`.

The fixed non-system application-directory closure is exactly:

| Leaf | Bytes | SHA-256 |
|---|---:|---|
| `libiconv-2.dll` | 1,136,529 | `FF31FA811F9C07CC7FDAA68C9E8BCA3A7B4FDF6E0A079A58175EA58BA139C7AE` |
| `libintl-8.dll` | 298,731 | `0537C3DD2378218508EBE3CC416D72A99EE2D24AE1C5525E23458F32544EF861` |
| `libpcre2-8-0.dll` | 717,955 | `C135A87ED0F11EAE8FFC4CB469671FF0B3F5D71FAB5FB024E9B1E7241CA25B52` |
| `libwinpthread-1.dll` | 64,931 | `D66B00E4A4385344BF2BE54B03446EA19CED654C78A18A024A0B43971D68459B` |
| `zlib1.dll` | 120,814 | `CB7AB3788D10940DF874ACD97B1821BBB5EE4A91F3EEC11982BB5BF7A3C96443` |

Each fresh Git call rehashes the executable and all five DLLs with the .NET SHA seam before launch and rechecks them after exit. Missing, extra, reparse, case-fold collision, or seal drift is terminal. P6 retains the fixed repository config, exclude, attributes, alternates, linked-worktree `.git`/`commondir`/`gitdir`, exact-admin, and post-mutation topology tables required by S5, but implements their reads through the v6 byte seam.

### Bounded `ProcessStartInfo` byte seam

P6 defines one closed `Invoke-V6Process` implementation in pure Windows PowerShell and .NET. A phase selects an immutable operation-table row; callers cannot override executable, argv prefix/suffix grammar, working directory, environment, timeout, stdout/stderr caps, allowed exits, or stderr policy.

The implementation requires `UseShellExecute=false`, `CreateNoWindow=true`, redirected stdin/stdout/stderr, an environment built from an empty case-insensitive map, explicit absolute executable, exact working directory, and the complete Windows argv quoting algorithm. It closes stdin immediately unless the operation row provides one bounded canonical byte frame. Stdout and stderr are drained concurrently from their `BaseStream` objects into bounded byte buffers using fixed-size reads. It never uses `ReadToEnd`, line events, one-pipe-first draining, localized text as authority, or an unbounded wait.

The process has one finite operation deadline. Timeout or cap overflow attempts the single reviewed root termination path, waits only within the remaining cleanup allowance, records whether root exit and both EOF states were proved, and returns no parseable bytes. `Invoke-V6Process` and `ProcessStartInfo` alone make no Job, debug-event, loaded-module, private-desktop, or descendant-containment claim. The separately authenticated `PrivateDesktopRunnerV6` result may establish only its reviewed private-desktop, Job-membership, Job-drain, window, bounded-stream, and cleanup fields for that one invocation after the controller matches the actual call/result and accepts the SafetyEnvelope. Except for the exact classic-csc row governed solely by the explicit single-root trust contract above, every other operation table row must either be a sealed single-process command or explicitly declare its known child relation and pre/post process census. Child-absence proof is required only when that row's declared contract includes it; the csc row instead requires exactly its root-exit/EOF/allowed-exit/scratch/post-seal/no-surviving-related-process facts. If a row's required termination, child relation, or stream closure cannot be proved, the lineage stops `NEEDS_CONTEXT`; it performs no cleanup, retry, mutation continuation, or later Git call.

Git uses this seam with its fixed executable, five-DLL leases, clean 17-key environment, fixed global argv prefix, fixed operation classes, finite deadlines, and byte caps. Repository selection is only `-C <canonical repository root>`. Every Git operation whose stdout can carry a path list or path records uses the call-site's supported `-z`/NUL form. Fixed path argv values are separate canonical tokens; single-root and single-OID outputs that do not support `-z` use their own strict unique byte grammar and exact terminator. stdout remains raw bytes until all of the following are true:

1. the root exited within the deadline;
2. the exit code was obtained and is allowed for the operation class;
3. both bounded readers reached clean EOF without fault or overflow;
4. stderr satisfies the operation row;
5. the fixed executable and five DLL post-seals still match.

Exit validation is before parsing. A valid-looking zero-length or NUL-framed stdout with a disallowed exit is failure. `$LASTEXITCODE`, direct `& git`, text-mode Git path output, `Start-Process`, parse-before-exit, and fallback Git are forbidden.

P6 freezes separate strict byte parsers for single OID, single root, NUL path list, NUL worktree records, `--name-status -z`, and other exact call-site formats. UTF-8 decoding is strict, BOM is forbidden, final NUL/count/record grammar is exact, canonical relative paths reject absolute/drive/traversal forms, and Ordinal/OrdinalIgnoreCase contracts are enforced after raw framing.

Non-Git operations outside `PrivateDesktopRunnerV6` use the same bounded process-result discipline and their own fixed rows. Private Ren'Py and scanner rows use the v6 runner's in-memory bounded streams and helper-specific result contract, not the historical helper or ordinary `Invoke-V6Process` containment claims. Their stdout is not authority until exit/EOF/cap/schema checks pass. Engine logs remain diagnostic only. P6 does not claim that `ProcessStartInfo` itself establishes a security sandbox.

### Controller controls

Before M6 creation, P6's independent review runs production interfaces against clean and poisoned nonproject inputs. It must prove:

- .NET SHA positive controls and length/EOF/identity failures;
- canonical `-EncodedCommand` round trip and rejection of altered bytes/base64/argv/order;
- module-autoload/poisoned-`PSModulePath` resistance and absolute Utility provenance when used;
- exact Git executable/five-DLL seals and rejection of one-byte/path/case/reparse drift;
- valid NUL records, invalid UTF-8, BOM, missing/double final NUL, malformed records, quoted/octal text output, and path traversal rejection;
- valid stdout plus disallowed exit rejection, and exit-before-parse instrumentation;
- concurrent cap-plus-one stdout/stderr overflow, timeout, reader failure, and unproved-cleanup terminal paths;
- poisoned PATH, Git environment/config/pager/editor/askpass/attributes/excludes/alternates, and linked-worktree redirection rejection;
- all 42 named Task 1 mutations reject while the clean production path passes;
- no adapter, embedded assembly, general controller compiler, seed/A/B, Roslyn, Task 3, Claude, Opus, setup-token, blind-map, Phase B, or `Add-Type` token appears in an executable v6 body; the sole compiler operation is the exact bounded classic-csc `PrivateDesktopRunnerV6` row above.

Static review treats a direct Git launch, text Git parser, ignored exit, unbounded read/wait, parse-before-exit, inherited semantic environment, unknown process row, cleanup retry, or path fallback as Critical.

## Task 1 contract

### Admission and one-shot rule

Task 1 remains globally one-shot. Its admission leaf is schema 1 with the exact 10 fields and max/retry values carried from the sealed contract, but every path and binding names L6/P6/M6 and `recovery-v6`. The controller excludes concurrent recovery-root writers, creates `task1-admission` only as an empty ordinary non-reparse setup directory, immediately proves its exact empty child set, and opens `attempt.json` through `FileStream(FileMode.CreateNew)`. Successful CreateNew of that fixed leaf consumes the sole Task 1 opportunity; idempotent directory creation does not. A failure before leaf CreateNew may leave only the exact empty setup directory and consumes no opportunity; a later separately authorized continuation may accept it only after the same identity/empty/no-concurrent-writer proof. Any failure after leaf CreateNew is terminal; there is no retry, new GUID, alternate SaveDir/worktree, or delete/recreate.

RED and GREEN remain schema 4 with exact ordered fields:

`schema_version,verdict,fixture_gate,stream_gate,json_real_gate,inputs,mutations,created_utc`

The JSON-real gate retains exactly 8 positive and 18 negative cases. An accepted real is native `System.Decimal` or finite native `System.Double`, with the exact per-case type and zero-policy descriptors frozen by P6; values typed as `Int32`, `Int64`, `Single`, string, Boolean, or null, plus NaN and either infinity, reject. No branch casts an input before its native-type/range check. The old-runtime parse exception remains limited to the M6-directed physical v2 generator state used by the Decimal/finite-Double positive control. Other legacy leaves are stream-hash-only.

The mutation suite remains exactly 42 named mutations in the order frozen by P6. Each mutation changes one relation and must reject without durable output or attempt consumption; the unmodified production interface must pass. P6 must restate every mutation name and expected failure rather than point to executable shorthand in S5.

Generator and observer each retain:

- exactly one admission opportunity and one attempt ledger;
- exact fresh worktree and SaveDir roots unique to v6;
- non-following pre/post inventories and bounded AppData observation;
- authenticated fixture and P6-embedded `PrivateDesktopRunnerV6` inputs, with the historical helper pair forbidden;
- generator attempt schema 3 exact 19 fields and completion schema 3 exact 43 fields;
- observer attempt schema 3 exact 20 fields and completion schema 3 exact 42 fields;
- no engine-log verdict substitution;
- candidate generation and observation only through the approved one-shot order.

The internal nested schemas remain: admission 13 fields, generator 28, observer 17, full-selftest 8, version-probe 6, mother 4, cleanup 4, and artifact row 3. P6 must reproduce their exact ordered fields, types, counts, path grammar, and value relations.

### Durable topology and completion

The 27 new durable leaves excluding Task 1 completion are:

- outside `recovery-v6`: S6, P6, and L6;
- inside `recovery-v6`: M6, admission, RED, GREEN, nine generator leaves, nine observer leaves, mother, and baseline.

Before Task 1 completion, `recovery-v6` contains exactly 24 leaves and six directories. After completion it contains exactly 25 leaves and six directories. The directories are exactly `task1-admission`, `generator-attempt`, `generator-process`, `observer-attempt`, `observer-process`, and `mother`; `rules` is absent until Task 2.

The complete Task 1 authority union is `127 + 27 = 154` unique leaves. Task 1 completion is schema 6 with these exact 16 ordered fields:

`schema_version,verdict,approval,task1_admission,predecessor,baseline_game_tree,full_selftest,version_probe,generator,observer,mother,artifact_count,artifacts,cleanup,finished_utc,lineage_status`

Its fixed relations include:

- `schema_version=6`, success verdict, and `lineage_status="fresh_v6_only"`;
- approval binds L6/P6/S6;
- predecessor binds M6 and its 127/27,437/catalog SHA plus all three failure objects and source inventories;
- generator and observer invocation counts are exactly one each;
- `artifact_count=154` and rows are the exact Ordinal-sorted union;
- cleanup proves only the four v6 Task 1 temporary worktree/SaveDir paths absent;
- baseline proves the pre-R6 game tree remains `fa7a398e9d989731b24e3c1642f3e2e33ce846ff`.

The unique success sequence is admission, RED, fresh generator worktree/patch, GREEN, generator ledger/run/completion, fresh observer worktree/patch, observer ledger/run/completion, mother, cleanup reread, deletion of only four v6 temporary Task 1 paths, baseline, 154-union reproof, then Task 1 completion.

## Task 2 and R6

Task 2 begins in a fresh scope with L6 as first project leaf and P6 as second. It strict-reads Task 1 schema 6 and rehashes all 154 current artifacts before RED.

R6 changes exactly:

1. `game/balance.rpy`;
2. `game/difficulty.rpy`;
3. `game/test_game.rpy`.

Task 2 invokes exactly nine gates in this order:

1. `rules-red`;
2. `rules-green`;
3. `catalog-green`;
4. `balance-green`;
5. `winter-invariance-green`;
6. `missing-portraits-green`;
7. `narration-overlap-green`;
8. `show-before-green`;
9. `lint-green`.

Each invocation has one schema-1 receipt with these exact 14 ordered fields:

`schema_version,name,kind,expected,actual,verdict,helper_evidence_dir,helper_artifacts,helper_result,runner_or_scanner_evidence_dir,direct_evidence,source_evidence,assertions,created_utc`

The complete Task 2 union is exactly 56 artifacts. Task 2 completion is schema 6 with these exact 16 ordered fields:

`schema_version,verdict,approved_plan_lock_sha256,task1_completion_path,task1_completion_sha256,approved_plan_commit,approved_spec_commit,rules_commit,rules_parent_commit,rules_subject,rules_paths,invocation_count,invocations,artifact_count,artifacts,finished_utc`

It binds L6, P6, S6, R6, the schema-6 Task 1 completion, exact nine receipts, exact 14-field receipt grammar, and exact 56-artifact union. It is CreateNew, strict UTF-8/no BOM/one LF, durably flushed, strictly reread, and read-only frozen.

### Release-font gate

`show-before-green` retains the mandatory release-font gate before R6 commit. P6 must freeze the full current Python source inventory and synthetic runtime construction facts, including the 2,551-file base slice, 355-file fontTools slice, exact 2,908-leaf pre-run runtime, 218 directories, exact 58-path/1,240-byte scan catalog with SHA-256 `AA5433C2D931CEE1052244AFCE0CAFC0C773FBA5F14285871B9B6841DF1DD7A3`, exact scanner/release/subset inputs, and the authenticated source/font pre/post seals.

Python is launched only through the bounded P6 operation table; P6 does not invoke Python while being authored or reviewed. At Task 2 execution the transient runtime must begin absent, be built non-followingly from authenticated ordinary source leaves, run the canonical scanner/show/release sequence with byte-bounded results, preserve `game/msyh.ttf` byte-for-byte, contain no cache/backup residue, and be deleted non-followingly only after every process/stream/input/output/post-seal check succeeds. A timeout or unproved descendant/cleanup state is terminal and the controller must not claim the runtime absent.

Only after the release-font gate passes may the fixed Git call commit with `--no-verify --no-gpg-sign --cleanup=verbatim` and the exact R6 subject. The bypass is authorized only for that call because the repository-prescribed release gate has just passed inside the bounded seam. Post-commit parent, subject, game-tree, exact three changed paths, status, index, and every protected seal are revalidated.

Successful creation and independent review of the Task 2 completion leaf is the Recovery v6 endpoint. No recovery-v6 scope launches copy generation or awaits a selection.

## Post-R6 copy lineage

After R6, copy work requires a new append-only copy specification, plan, and approval lock. That lineage is not S6/P6/L6 and cannot reuse a hidden P6 body or ambient selection. It must independently authenticate R6 plus the v6 Task 1 and Task 2 completions before any drafting call.

The future copy lineage must:

1. explicitly use the installed `invoke-opus-4-6` skill;
2. start three fresh isolated Opus sessions with no session reuse or cross-draft context;
3. provide only the independently reviewed current canon/scene/constraint bundle;
4. preserve three raw, unedited outputs as A, B, and C with exact bytes/SHA and provenance;
5. present the raw A/B/C candidates to the user and wait for an explicit user selection;
6. create post-selection authority only after that choice, binding the selected raw result and selection record;
7. run the selected replay/review from the newly approved post-selection plan and lock, never from ambient chat state.

S6 makes no claim about current Claude setup, tokens, credentials, retry environment, or availability. Those are future-lineage admission facts. No Opus call, copy file, blind map, selection, or replay is authorized by Recovery v6.

## Failure and authorization boundary

- S6 publication changes documentation only. It does not create P6, M6, L6, R6, or any runtime leaf.
- P6 publication requires independent review and a separate commit authorization. P6 review runs only nonproject controller and synthetic `PrivateDesktopRunnerV6` controls; it does not run either historical helper, recovery, Ren'Py, generator, observer, scanner, release preparation, Python, Claude, or Opus.
- M6 creation, M6 review, L6 creation, L6 review, Task 0 authorization, Task 1 authorization, and Task 2 authorization are separate gates.
- A failure before M6-leaf CreateNew may leave the namespace absent or the exact empty ordinary setup root described above and consumes no M6 opportunity. Successful CreateNew of M6 consumes publication; a later failure preserves the site and is terminal for v6.
- Successful CreateNew of `task1-admission/attempt.json` consumes the single Task 1 opportunity. An earlier failure may leave only the exact empty ordinary admission setup directory; any later Task 1 failure is terminal for v6.
- A process timeout, cap overflow, nonzero/disallowed exit, malformed result, unproved root/child exit, unproved EOF, drifted input, or cleanup uncertainty is terminal. Valid-looking stdout never overrides it.
- A failed mutation may be followed only by the exact containment/topology reproof allowed by P6. If containment is unproved, no further project or Git operation is permitted.
- No v4/v5 path, ignored preapproval source, alternate Git, general compiler/adapter, retry root, or manually repaired artifact may enter authority. The sole bounded classic-csc v6 helper compilation is ephemeral behavior from authenticated P6 source and never an authority artifact.
- Task 2 completion closes Recovery v6. Any copy action requires the post-R6 lineage and its own explicit authorization.

## Testing and acceptance contract

S6/P6 acceptance requires:

1. `S6^=S5`, exact S6 subject, one changed S6 path, and unchanged game/winter trees;
2. `P6^=S6`, exact P6 subject, one changed P6 path, and unchanged game/winter trees;
3. P5 commit/leaf, M5, L5, and `recovery-v5` all absent;
4. the failed seed facts, four nonauthority leaf seals, and five absent-root observations represented exactly without promotion into M6;
5. no v6 adapter/general-controller-compiler/seed/A/B/Roslyn/Task3/Claude/setup-token/blind-map/Phase-B executable path; the historical helper pair is non-executable, and only the authenticated, bounded-csc, cap-enforcing `PrivateDesktopRunnerV6` source/compile/load contract is excepted;
6. literal encoded WinPS 5.1 transport, .NET SHA, absolute Utility-only import rule, fixed Git+five-DLL table, bounded byte pipes, NUL parsers, and exit-before-parse controls fully specified;
7. P6 is self-contained: every schema field, mutation, operation row, path, cap, timeout, parser, process result, cleanup rule, and body/input seal is reproduced exactly.

Task 0 acceptance requires L6-first/P6-second authentication, exact topology and absence reproof, exactly the P6-frozen closed count/order of read-only Git launches, zero non-Git helper/Ren'Py/Python/scanner/Claude/Opus launch, zero durable write, no ignored-preapproval leaf read, and no Task 1 opportunity consumption.

M6/L6 acceptance requires:

1. M6 schema 5 exact 22, exact 127 artifacts, 27,437-byte catalog, and `082B7B01E93437173FB97BD3764D14D8290ACE05F6E9CE48667F2D51921CA13F`;
2. M6 exact terminal/controller/preapproval failure objects and three source inventories;
3. independent metadata-first/allowlist-first physical rehash of all 127 artifacts;
4. L6 schema 6 exact 42 and exact S5-versus-missing-P5-versus-last-sealed lineage;
5. M6-leaf CreateNew as the sole publication-consumption point, L6 CreateNew, durable flush, strict reread, read-only behavior, and out-of-band physical M6/L6 hashes;
6. no access to ignored preapproval leaves during publication or review.

Task 1 acceptance requires:

1. admission schema 1 exact 10, global limit 1, and successful CreateNew of fixed `task1-admission/attempt.json` as the sole Task 1 consumption point;
2. RED/GREEN schema 4 exact 8;
3. JSON-real exact 8 positive/18 negative and mutation suite exact 42;
4. generator schemas 3 exact 19/43 and observer schemas 3 exact 20/42;
5. exact 24-to-25 runtime topology, six directories, one generator and one observer invocation;
6. Task 1 completion schema 6 exact 16 and exact 154-artifact union;
7. baseline game tree unchanged and only four v6 temporary Task 1 paths deleted.

Task 2 acceptance requires:

1. exact R6 parent, subject, and three changed paths;
2. exact nine invocation order, each receipt schema 1 exact 14, and exact 56 artifacts;
3. authenticated release-font gate with exact 2,908/218 runtime, 58/1,240/scan SHA, byte-identical font, and zero cache/backup/runtime residue;
4. Task 2 completion schema 6 exact 16;
5. no Task 3 or copy/candidate/selection/replay leaf in `recovery-v6`;
6. Recovery v6 terminates immediately after independent Task 2 completion review.

## Asset and package impact

S6 and the future P6/M6/L6 governance leaves add no game asset and change no package content. Required new art: none. Required music: none. Required sound effects: none. Required animation: none. Required UI or font asset: none.

Task 1 produces evidence and a candidate save only inside its governed transient/runtime boundaries; it does not add packaged media. Task 2 changes only the three named `.rpy` files. The release-font gate must prove the existing `game/msyh.ttf` is byte-identical before and after, so Recovery v6 adds zero asset or font payload bytes. Existing assets are reused. The compiled-script/archive package delta is expected to be negligible but is not declared zero; it must be measured from the actual release build and package before shipment. Any later copy-lineage text change has its own asset-impact review and is outside Recovery v6.

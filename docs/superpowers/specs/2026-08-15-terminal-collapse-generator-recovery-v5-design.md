# Terminal Collapse Generator Recovery v5 Design

**Date:** 2026-08-15
**Status:** approved design checkpoint under the user's 2026-08-15 standing approval; implementation and execution remain separately scoped
**Scope:** append-only recovery after the terminal P4 prepublication controller failure

## Decision

Recovery v5 is a new append-only authority lineage. It does not patch, amend, replay, or retroactively bless P4. It preserves S4/P4 as a terminal prepublication failure, leaves `recovery-v4/`, M4, L4, every v4 admission/runtime leaf, and every v4 temporary root absent, and starts a fresh S5/P5/M5/L5 namespace.

The selected topology is:

```text
P2  25c2ea674948ad89e8b48befb89643a8687648a4
 |
S3  5fa8fb14792e095e066c3e9f698eda9ea4380854
 |
P3  7365ae61c8d12dd0f34651a4bd727528cd9059d4
 |
S4  f0ed56aaceb5cf8a0ff38fe2b888c13c3614ae98
 |
P4  dccc785595f8551392c23db4a3a8d517fc6ef528   terminal prepublication failure
 |
S5  Recovery v5 spec commit
 |
P5  Recovery v5 plan commit
 |
R5  Task 2 rules commit
```

Rejected alternatives:

1. injecting `PSModulePath`, `GIT_CONFIG_*`, `core.quotepath=false`, or another ambient overlay into the committed P4 procedure;
2. amending or replacing P4 in place;
3. creating M4/L4 after the failure and describing the run as a continuation;
4. reusing `recovery-v4/`, a v4 ledger, or a v4 temporary root;
5. treating a diagnostic command that made P4 Step 1 pass as authority.

Those alternatives either change execution semantics that P4 never approved, erase the failure history, or create a false sealed lineage.

## Frozen facts

### Current topology and content

- P4 is `dccc785595f8551392c23db4a3a8d517fc6ef528`.
- P4's direct parent is S4 `f0ed56aaceb5cf8a0ff38fe2b888c13c3614ae98`.
- S4's direct parent is P3 `7365ae61c8d12dd0f34651a4bd727528cd9059d4`.
- S3 is `5fa8fb14792e095e066c3e9f698eda9ea4380854`; P2 is `25c2ea674948ad89e8b48befb89643a8687648a4`.
- P2, S3, P3, S4, and P4 all have `game` tree `fa7a398e9d989731b24e3c1642f3e2e33ce846ff`.
- S4 physical spec is 46,470 bytes, SHA-256 `137799D91454F52E2B652AD9A1C452D0983D9A762519D5367E99841E27DACFDD`, raw Git blob `3194bc806e08dbadd77701ba730dcbed7388066e`.
- P4 physical plan is 1,008,828 bytes, SHA-256 `E6F296A527C0A5247F5A87AFB7B47829C91C29D864A140B5344E33BFC3AFED09`, raw Git blob `3cbf0fc952e47a2239e1b07e468682cd6feae42c`.
- The protected winter plan remains the only main-worktree status row and has SHA-256 `0F39B5F5ACE1D4666DD146863CABDF398B031F5666C29AE337CEB89796E4276C`.
- The index and tracked working tree are clean.

### Last genuinely sealed authority

- L3 is `.superpowers/sdd/terminal-collapse-ending/approved-plan-lock-v3.json`, 2,354 bytes, SHA-256 `59D44AFD5562C735B81DE5429A9518E39754F6900EF8231F7B2C11C9653D626C`.
- M3 is `.superpowers/sdd/terminal-collapse-ending/recovery-v3/predecessor-evidence.json`, 45,507 bytes, SHA-256 `6DE89AAD17FFC00EB35FE5378444227BA5C8E1BCBF0C4657C9E1BF1FD55D2FBB`.
- M3 has exactly 115 current authority artifacts. Its catalog is 24,660 bytes with SHA-256 `9694E728A82F6DDC743DA5E83967EAC7EE02FFA62FA53E21F4A2374F27DDDA24`.
- The v3 terminal Task 1 evidence, patched v3 fixture, brief, retry authority, and report remain as frozen by S4. The v3 generator/observer invocation counts remain 0/0 and its candidate-save disposition remains `not_created`.

### P4 prepublication terminal state

The following paths are absent and must remain absent until the corresponding v5 authority explicitly creates a v5 path:

- `.superpowers/sdd/terminal-collapse-ending/recovery-v4/`;
- `.superpowers/sdd/terminal-collapse-ending/approved-plan-lock-v4.json`;
- the M4 path under `recovery-v4/`;
- the v4 Task 1 admission;
- every v4 RED/GREEN, attempt, process, state, completion, mother, baseline, Task 1 completion, and rules leaf;
- all four fixed v4 generator/observer worktree and SaveDir roots.

No M4 or L4 was published. No helper, Ren'Py, generator, observer, Task 0, or Task 1 runtime was invoked under v4. No save was generated. No one-shot runtime or admission opportunity was consumed.

The controller defects that supersede P4 are exact and independently reprovable from P4 plus the frozen machine boundary:

1. `GET_FILEHASH_COMMAND_UNAVAILABLE_IN_FRESH_WINPS51_SCOPE` — P4 calls `Get-FileHash`, but inherited module discovery can select a Core-only Utility manifest before the native Desktop manifest, leaving the command unavailable in a fresh WinPS 5.1 target.
2. `GIT_LS_FILES_TEXT_QUOTED_EIGHT_UTF8_PATHS` — P4 parses line-oriented `git ls-files --cached`; the v3 index contains eight non-ASCII paths, and the inherited Git presentation emits quoted/octal text that P4 passes to `GetFullPath` as a literal path.
3. `GIT_EXIT_STATUS_NOT_CHECKED_BEFORE_ZERO_RESULT_INTERPRETATION` — multiple P4 zero-result Git gates can interpret empty stdout as success without first proving the command exit code.

The earlier host-side marker interpolation error and later read-only diagnostic probes are chronology, not durable authority. M5 must not invent an attempt transcript, raw console log, or physical report that does not exist.

## Commit topology

- `S5^=P4`.
- S5 subject is exactly `docs: specify terminal collapse generator recovery v5`.
- S5 adds only `docs/superpowers/specs/2026-08-15-terminal-collapse-generator-recovery-v5-design.md`.
- `P5^=S5`.
- P5 subject is exactly `docs: plan terminal collapse generator recovery v5`.
- P5 adds only `docs/superpowers/plans/2026-08-15-terminal-collapse-generator-recovery-v5.md`.
- `R5^=P5`.
- R5 subject remains exactly `fix: enforce terminal resistance collapse rules`.
- R5 modifies only `game/balance.rpy`, `game/difficulty.rpy`, and `game/test_game.rpy`.
- S5 and P5 preserve the baseline `game` tree.
- R5 cannot exist before successful v5 Task 1 completion.
- Merge commits, intermediate commits, additional paths, hook-added paths, a dirty index, tracked drift, or winter drift are terminal.

This design approval does not create M5/L5 and does not authorize Task 0 or Task 1. Those are later execution actions with their own exact authority boundary.

## M5 predecessor manifest

M5 has fixed path:

`.superpowers/sdd/terminal-collapse-ending/recovery-v5/predecessor-evidence.json`

After every prepublication authority/current-state check passes, M5 publication non-followingly proves the fixed `recovery-v5` root absent with ordinary ancestors, then calls the audited `CreateDirectoryW` exactly once. Native success atomically consumes the M5 publication opportunity; `ERROR_ALREADY_EXISTS`, a competing creation, another error, or post-create identity/reparse mismatch is terminal and the root is never adopted. Only inside that newly created root does M5 use CreateNew, strict UTF-8 without BOM, LF-only with exactly one terminal LF, `Flush(true)`, strict duplicate-key-aware reread, and read-only freeze. Any failure after root creation preserves the root and whatever CreateNew state exists, forbids rollback/delete-recreate/alternate directory/retry, and requires another append-only lineage. Before root creation, a host-only/prepublication failure may stop with the namespace absent under the literal-transport retry rule.

M5 schema is 4. Its exact 20 ordered top-level fields are:

`schema_version,purpose,predecessor_plan_commit,predecessor_spec_commit,predecessor_lock_path,predecessor_lock_bytes,predecessor_lock_sha256,predecessor_manifest_path,predecessor_manifest_bytes,predecessor_manifest_sha256,superseded_spec_commit,superseded_plan_commit,artifact_count,catalog_bytes,catalog_sha256,artifacts,terminal_failure,controller_failure,source_inventories,created_utc`

Fixed meanings:

- `schema_version=4`;
- `purpose="terminal-collapse-generator-recovery-v5-predecessor"`;
- `predecessor_plan_commit=P3`, `predecessor_spec_commit=S3`;
- predecessor lock is the physical L3 path/bytes/hash;
- predecessor manifest is the physical M3 path/bytes/hash;
- `superseded_spec_commit=S4`, `superseded_plan_commit=P4`;
- `artifact_count=126`;
- `catalog_bytes=27190`;
- `catalog_sha256="DF69BBAA504E6BA0649F1358532951E6CF2A9FEEF703EBEED20D542C6F0A6910"`;
- `created_utc` is an invariant round-trippable UTC string.

Calling P3/S3/L3/M3 the last sealed authority is deliberate. L3/M3 never sealed S4/P4. S4/P4 are first-class preserved artifacts and the immediate failed plan lineage, not retroactive children of L3.

### Exact 126-artifact union

The 126 unique physical leaves are exactly:

1. M3's 115 artifact rows, unchanged in path/bytes/hash;
2. S3 spec;
3. P3 plan;
4. L3;
5. M3;
6. v3 RED;
7. the current patched v3 fixture;
8. the v3 Task 1 brief;
9. the v3 retry authority;
10. the merged v3 Task 1 failure report;
11. S4 spec;
12. P4 plan.

Items 2–10 reproduce the nine S4-frozen additions that produced the independently revalidated 124-row candidate catalog. Items 11–12 add S4/P4. The exact 124-row candidate subset must first rebuild independently to 26,703 bytes and `AFAD4D1F6EB1808DC79E45B506A152CC4D62FE0AB6DB6238C2474A039AB4D589`; only then may S4/P4 be unioned with that subset and all 126 rows be re-sorted before checking 27,190/`DF69BBAA504E6BA0649F1358532951E6CF2A9FEEF703EBEED20D542C6F0A6910`. The 124 rows are not asserted to be a physical prefix of the final Ordinal-sorted catalog.

Catalog rows are exact `<canonical absolute path><TAB><decimal bytes><TAB><UPPERCASE SHA256><LF>`, sorted with `StringComparer.Ordinal` and rejected on `StringComparer.OrdinalIgnoreCase` collision. `artifacts` rows have exact ordered fields `path,bytes,sha256`. M5 publication and independent review use metadata/allowlist-first sequencing: authenticate M5's physical bytes/hash, strict encoding/duplicate-key/schema/value contracts, exact 126-row count, fixed catalog metadata, and exact known 126 canonical paths before opening any artifact path declared inside M5. Only after that allowlist passes may the reviewer stream-hash the 126 current physical leaves and rebuild the same catalog. An unexpected/tampered row is reported lexically and stops without probing that path. The 61 excluded v2 cache leaves are never probed, opened, or promoted into authority.

### `terminal_failure`

`terminal_failure` is the exact S4 v3 terminal failure object, including its exact 28-field schema, two historical attempts, checkpoint anomaly, RED/fixture/brief/retry/report seals, P3 worktree topology, zero v3 invocation counts, `artifact_disposition="preserved_not_used"`, and `candidate_save_disposition="not_created"`. P5 must restate the full schema and values; it cannot use “same as S4” as executable shorthand.

### `controller_failure`

`controller_failure` has exactly 19 ordered fields:

`classification,program_outcome,reason,final_status,final_failure_stage,failed_plan_commit,failed_spec_commit,defects,m4_path,m4_present,l4_path,l4_present,recovery_root_present,helper_launch_count,renpy_launch_count,generator_invocation_count,observer_invocation_count,artifact_disposition,candidate_save_disposition`

Fixed values:

- `classification="CONTROLLER_STATIC_CONTRACT_FAILURE"`;
- `program_outcome="NOT_INVOKED"`;
- `reason="PREPUBLICATION_CONTROLLER_CONTRACT_INVALID"`;
- `final_status="NEEDS_CONTEXT"`;
- `final_failure_stage="M4_PREPUBLICATION"`;
- failed plan/spec are P4/S4;
- `defects` is the ordered three-string list above;
- M4 and L4 paths are their canonical v4 paths and both present flags are false;
- `recovery_root_present=false`;
- helper, Ren'Py, generator, and observer counts are all 0;
- `artifact_disposition="preserved_terminal_prepublication"`;
- `candidate_save_disposition="not_created"`.

The object deliberately has no attempt array, timestamp reconstruction, stdout/stderr, or report seal. Those would turn conversational history into fabricated physical evidence.

### `source_inventories`

`source_inventories` contains exactly three ordered objects:

1. `v2_generator_worktree_task_owned` — authority/excluded counts 8/61;
2. `v2_generator_savedir` — 12/0;
3. `v3_generator_worktree_task_owned` — 1/0, containing only the patched 8,845-byte fixture with SHA-256 `A0D2A8B0589CC64F9479CE8E5B3315760001AA965502D1D740D35C6A2D558381`.

Each inventory has exact fields `id,root_path,authority_file_count,authority_files,excluded_cache_count,excluded_cache_files`; each leaf has exact fields `relative_path,bytes,sha256`. Relative paths are Ordinal-sorted and OrdinalIgnoreCase-unique.

Metadata catalog constants remain:

- v2 worktree authority: 777 bytes / `37976165E24FA53CC4DE33AC8D0B9B3DA0545925184FD3D4F088039292FE1723`;
- v2 worktree excluded: 5,732 bytes / `D7E59DED729100143D7763ABEA1A90DD1632E55B7EB3AEB1D26F968AF0C9A99B`;
- v2 SaveDir authority: 1,066 bytes / `DD3A6C77E61922681CE3788E6BBA0883B681461A10F628D4AA3CE66E033747A4`;
- empty excluded list: 1 byte / `01BA4719C80B6FE911B091A7C05124B64EEECE964E09C058EF8F9805DACA546B`;
- v3 worktree authority: 115 bytes / `62F549A266FBB3A6AD759841F29A5E23BD5DFEEF7A3A5CC4020365DCBCD527BF`.

No v4 source inventory exists because no v4 namespace, authority leaf, worktree, SaveDir, or candidate was created.

## L5 approval lock

L5 has fixed path:

`.superpowers/sdd/terminal-collapse-ending/approved-plan-lock-v5.json`

L5 is published only after S5, P5, and M5 have each passed independent C0/I0 review. M5's reviewer returns the exact uppercase physical M5 SHA out of band; P5's reviewer separately returns the exact uppercase physical P5 SHA as a transport binding; a word such as `READY` is not a substitute for either value. The fresh L5-publisher scope receives exactly those two values: M5 SHA is its authority input and P5 SHA authenticates only the framed body transport. Its first project-leaf access is the M5 leaf existence check followed immediately by the .NET physical hash comparison; before that comparison succeeds it may not read M5 bytes/schema, S5, P5, L3, Git state, or any other project leaf. After the M5 SHA passes, P5 is the second allowed project leaf and must match the separately reviewed P5 SHA before the loader extracts or executes the publisher body. The authenticated body then strict-reads and fully revalidates M5/current topology before CreateNew L5. L5 uses CreateNew, strict UTF-8/no BOM/one LF, `Flush(true)`, strict reread, and read-only freeze. Its physical SHA is supplied out of band to every later fresh scope.

L5 schema is 5. Its exact 41 ordered fields are:

`schema_version,purpose,approved_plan_path,approved_plan_commit,plan_bytes,plan_sha256,spec_path,spec_commit,spec_bytes,spec_sha256,predecessor_plan_commit,predecessor_spec_commit,last_sealed_plan_commit,last_sealed_spec_commit,last_sealed_lock_path,last_sealed_lock_bytes,last_sealed_lock_sha256,predecessor_manifest_path,predecessor_manifest_bytes,predecessor_manifest_sha256,predecessor_artifact_count,predecessor_catalog_bytes,predecessor_catalog_sha256,baseline_game_tree,execution_strategy,superseded_namespace,superseded_disposition,preserved_failure_report_path,preserved_failure_report_bytes,preserved_failure_report_sha256,task1_admission_ledger_path,task1_admission_limit,generator_attempt_ledger_path,generator_attempt_limit,observer_attempt_ledger_path,observer_attempt_limit,test_result_stream,engine_log_role,state_real_number_policy,execution_authorization_required,task1_admission_schema`

Fixed relations:

- `schema_version=5`, `purpose="terminal-collapse-generator-recovery-v5"`;
- approved plan/spec bind P5/S5 physical bytes/hash, commits, and raw Git blobs;
- immediate predecessor plan/spec are P4/S4;
- last sealed plan/spec/lock are P3/S3/L3;
- predecessor manifest is physical M5 with exact 126/27,190/`DF69BBAA504E6BA0649F1358532951E6CF2A9FEEF703EBEED20D542C6F0A6910`;
- baseline game tree is `fa7a398e9d989731b24e3c1642f3e2e33ce846ff`;
- `execution_strategy="hermetic_byte_transport_fresh_namespace_global_one_shot"`;
- superseded namespace is the canonical absent `recovery-v4` path;
- `superseded_disposition="not_created_prepublication"`;
- the preserved failure report fields continue to bind the actual v3 report, the only durable merged failure report;
- admission and attempt paths point only into `recovery-v5`;
- all limits are 1, `task1_admission_schema=1`;
- `test_result_stream="helper_stdout"`;
- `engine_log_role="diagnostic_only"`;
- `state_real_number_policy="decimal_or_finite_double"`;
- `execution_authorization_required=true`.

Every fresh Task 0/1/2/3 scope receives the reviewed uppercase L5 physical SHA as authority plus the separately reviewed uppercase P5 physical SHA as transport binding, followed only by that phase's closed typed checkpoint/handoff vector defined below. L5 is its first project leaf. Before L5 physical SHA matches the authority value, only the leaf existence check and its .NET stream hash are permitted. P5 is the second allowed project leaf and must match the transport value before the loader extracts or executes any task body or shared helper block. P5 never substitutes for L5 authority, and no unlisted handoff is allowed. P5 contains no Phase B phase-table row, body, vector, or launch authority: the user-selected result and blind map do not exist when P5 is frozen, so post-selection replay requires a new separately reviewed append-only spec/plan/lock lineage and cannot discover or inject a selection through ambient state.

## Hermetic WinPS 5.1 I/O boundary

P5 must expose exactly one external-Git byte boundary and one .NET SHA-256 boundary. Fixing only P4's first `ls-files` call is forbidden.

### Bootstrap

Each executable WinPS scope proves Desktop PowerShell major 5 and uses only PowerShell language plus .NET for the initial L5 existence/hash gate. The hashing/Git seam must not call `Get-FileHash`, `New-Object`, `Start-Process`, or any cmdlet that depends on module autoload.

If later code needs Utility or Management commands, it imports each native Desktop manifest by absolute `$PSHOME` path only after the phase's authority/binding leaf order passes. P5 freezes one closed provider table for every executable command name: exact `CommandType=Cmdlet` or reviewed native Desktop function, module name/base/manifest, implementing assembly path/bytes/SHA/identity, and module-qualified invocation form where available. Immediately before first use and at each fresh scope, provider lookup must match that table; alias, unreviewed function, nested binary/module, duplicate provider, autoload, or path outside the sealed `$PSHOME` closure is terminal. An inherited or poisoned `PSModulePath` cannot select a Core-only manifest. `Get-FileHash` remains forbidden everywhere, including after native imports.

### Literal host-to-WinPS transport

P5 freezes one source-delivery mechanism for every fresh controller/Task scope; shell interpolation, `-Command`, here-string transport, temporary script/assembly files, alternate stdin formats, and transport fallback are forbidden. Independent P5 review returns one out-of-band transport bundle containing the exact P5 physical SHA, the stage-0 bootstrap's UTF-16LE bytes/canonical base64/SHA, the stage-1 loader's strict-UTF-8 bytes/canonical base64/SHA, a deterministic in-memory host-launcher adapter's source and assembly bytes/base64/SHA/metadata, the closed phase table, and every marked body bytes/SHA. That reviewed bundle never contains an Opus credential or credential-derived hash. The orchestration host receives the bundle plus the action's phase-typed reviewed bindings and, for Task 3 only, the separately authorized host-only setup-token capability described below; it does not read P5, Git, or any project leaf before target launch. The already-authorized orchestration host is the transport root of trust; it loads the reviewed adapter directly from the supplied byte array once, never from disk, rejects a preloaded matching identity, and exposes no general process-launch method. Before any path, file, module, or process access, the adapter requires a 64-bit OS, `Environment.Is64BitProcess=true`, and `IntPtr.Size=8`; it then proves that native machine/final-path queries identify the 64-bit System32 image rather than a WOW64-redirection result. A 32-bit host stops host-only with no Sysnative, relaunch, or fallback. P5 freezes x64 struct sizes/offsets and includes a 32-bit-harness RED plus a 64-bit final-path GREEN.

The host launcher derives canonical Windows and System32 with `GetWindowsDirectoryW`/`GetSystemDirectoryW`, not inherited environment strings. The current independently rehashed native 64-bit `System32\WindowsPowerShell\v1.0\powershell.exe` is exactly 454,656 bytes/SHA-256 `7600FFE12DA441FE89D035B13801E8E91D064BC544A27B19A5CF49F6AB8B18F5`, file version `10.0.26100.8875`; a fresh target reports Desktop PowerShell `5.1.26100.9168`. The earlier `0FF6F2C94BC7E2833A5F7E16DE1622E5DBA70396F31C7D5F56381870317E8C46` executable seal and every closure catalog derived from it are invalid after the 2026-08-15 system update and must not be copied into P5. Before P5 approval, two independent read-only builders must freshly enumerate and agree on the complete ordinary/non-reparse WinPS 5.1 startup resource, managed-assembly, CLR, and native-module closure used before the loader's first project-leaf gate; P5 freezes every resulting canonical path/bytes/SHA plus exact path/content catalogs and the clean loaded set. The adapter holds the executable and every non-system closure leaf with read/no-write/no-delete sharing, uses `PROCESS_CREATION_MITIGATION_POLICY_IMAGE_LOAD_PREFER_SYSTEM32_ALWAYS_ON`, and P5's clean CONTROL validates the exact canonical loaded module/assembly paths and hashes before project access. Missing/extra/drifted resources, app-directory collision, profiler/diagnostic injection, a non-System32 system image, an unexpected assembly/module, disagreement between the two closure builders, or drift from the S5-frozen executable bytes/version is terminal before P5 approval. The complete closure becomes authority only after both builders agree and independent P5 review approves its exact catalog; from that P5 seal onward any closure drift requires a new lineage, and S5 makes no claim to detect an otherwise-unbound closure change before that snapshot.

The target environment is built from empty rather than inherited state and contains exactly six case-insensitive-unique keys with P5-frozen native values: `ComSpec`, `Path`, `PATHEXT`, `SystemDrive`, `SystemRoot`, and `windir`. `Path` contains only canonical System32 and WinPS `$PSHOME`. No `COR_*`, `COMPLUS_*`, `DOTNET_*`, `PSModulePath`, PowerShell policy/debug/profile variable, drive-current-directory entry, user/module/cache path, Git variable, or unknown key survives. `lpCurrentDirectory` is canonical `$PSHOME`. The loader's first instructions set module autoloading to `None`, clear WinPS's synthesized `PSModulePath`, set strict UTF-8 console encodings, and validate Desktop PowerShell 5.1 plus the frozen pre-project closure before reading stdin or a project leaf.

The host serializes one exact six-element argv vector `[powershell.exe,'-NoLogo','-NoProfile','-NonInteractive','-EncodedCommand',stage0_base64]` with the same complete Windows 2n/2n+1 quote algorithm required below. `lpApplicationName` is the authenticated absolute PowerShell executable, argv[0] is that same path, `lpCurrentDirectory` is canonical `$PSHOME`, and `-EncodedCommand` plus its value are final. `-ExecutionPolicy`, `-EncodedArguments`, `-File`, an abbreviated switch, an extra token, or an inherited profile/interactive mode is forbidden. Stage 0 has exact P5-frozen text and terminal-LF policy, strict UTF-16LE without BOM/U+0000/unpaired surrogate, canonical padded base64 without whitespace, and exact bytes/SHA/base64-character/full-command-line counts. Checked arithmetic proves the mutable command line plus terminal NUL is at most 32,767 UTF-16 code units before allocation or launch. P5's boundary controls accept 32,767 including NUL and reject 32,768, and also reject altered byte/hash/base64/argv/order/profile flags or a failed `CommandLineToArgvW` six-element round trip.

Stage 0 is the only code supplied by argv. Its own embedded table freezes the exact stage-1 UTF-8 bytes/SHA/base64 length/chunk count and global frame caps. Using only PowerShell language plus .NET and a fixed-size reader, it reads and authenticates the bounded stage-1 record from stdin before creating one in-memory scriptblock; stage 1 then consumes the remaining canonical phase frame from the same stream. No project leaf is opened and no framed action body executes before stage 1 is authenticated. P5 freezes the exact stage-0 UTF-16LE byte count, encoded-character count, and complete command-line code-unit count, so command-line feasibility is a reviewed property rather than an aspirational cap. Every fixed inner WinPS root uses the same exact executable/argv/environment and stage-0/stage-1 transport; its stdin is another closed P5 phase frame, never raw script text. Each inner phase repeats L5 as first project leaf, P5 as second, and its closed dynamic-leaf order from independently forwarded reviewed bindings; the outer scope retains its own authority/P5 leases until inner completion but does not substitute those buffers for the inner proof.

The host adapter first records `IsProcessInJob(GetCurrentProcess(),NULL)` and, when present, the queryable immediate ambient limits as non-authority diagnostics. It does not require an unjobbed host and never asks a child to break away. Before any outer pipe/thread/Job/root setup it starts the single monotonic phase deadline. It creates a fresh outer Job with exactly `JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE`; active-process, breakaway, silent-breakaway, and UI limits are absent. It then launches exactly one target through `CreateProcessW` with `CREATE_SUSPENDED | CREATE_UNICODE_ENVIRONMENT | CREATE_NO_WINDOW | EXTENDED_STARTUPINFO_PRESENT`, never `CREATE_BREAKAWAY_FROM_JOB`. `STARTUPINFOEXW` has exactly three attributes: the three child stdio handles, the fresh outer Job, and the prefer-System32 mitigation. Only stdin-read/stdout-write/stderr-write are inheritable. Setup, synchronous `CreateProcessW` return, frame write, reader/writer readiness, admission/query, sole resume, root/descendant exit, Job reproof, and both drains consume the same remaining budget and never reset it; a synchronously stuck kernel call is a terminal native-call boundary, not permission to start another clock. The host concurrently runs one bounded stdin writer and two bounded `ReadFile` drains; each captured output cap is 4,194,304 bytes. It proves atomic outer-Job admission, root membership, `ActiveProcesses=1`, `TotalProcesses=1`, reader readiness, and one successful resume under that deadline. Windows 10+ nested-Job inheritance keeps every later descendant in this host-owned outer Job as well as any deeper reviewed inner Job. An inherited ambient Job may only tighten limits or fail an operation; it is never authority, fallback, or a reason to weaken an owned limit.

P5 has exactly three closed child-launch profiles: Git; bounded-tool/private-desktop, which explicitly includes the Task 1 CPython AST control and every private-desktop operation; and Opus. Each approved root is created suspended with no breakaway flag, inherits the outer Job, and is atomically added through `PROC_THREAD_ATTRIBUTE_JOB_LIST` to one new phase-specific nested inner Job whose handle is owned only by the target adapter and is never inherited. The Git and Opus inner Jobs each have exactly `JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE | JOB_OBJECT_LIMIT_ACTIVE_PROCESS`, `ActiveProcessLimit=1`, no breakaway/UI limit, and `DEBUG_ONLY_THIS_PROCESS`; an attempted descendant is atomically denied, and successful completion independently requires `ActiveProcesses=0` plus final `TotalProcesses=1`. Bounded-tool/private-desktop inner Jobs are kill-on-close with exact P5-frozen per-operation active/total limits and no breakaway or UI limit; they use `DEBUG_PROCESS` so every allowed root/descendant create/load event stops before user entry. P5's closed operation table freezes executable paths/seals/module closures, argv, cwd, environment, maximum active/total counts, stream caps, and deadline, and the adapter validates every permitted event before continue. No executable body can request an arbitrary operation or launch method. The authenticated `claude.exe` Opus root alone receives the exact setup-token environment; no Opus descendant may be created or inherit it. Inner Job completion, process-event inventory, EOF, result schema, and `ActiveProcesses=0` are required before its handle is released and the outer target proceeds.

Every adapter-created root uses one shared handle-inheritance helper and process-wide launch mutex inside a dedicated single-purpose launcher process that has no non-adapter `CreateProcess` path. Before the mutex all pipe handles are non-inheritable. While holding it, the helper makes exactly the three child stdio ends inheritable, builds the matching HANDLE_LIST, calls `CreateProcessW`, and in one `finally` immediately clears inheritability and closes the parent's copies of the child ends on success or failure before releasing the mutex. Parent ends, Jobs, process/thread/debug handles, attribute memory, authenticated leases, and every unrelated handle are never inheritable. The same helper is used by the orchestration-host outer launch and all target-adapter profile launches. A concurrent adversarial launch control must block on the same mutex and inherit zero test handles; a create failure must leave zero inheritable handles and allow reader/writer termination.

The thread that calls a debug-enabled `CreateProcessW` is the sole debug-event pump for that root; pipe readers only drain bytes and never call a debug API. The creator thread calls and checks `DebugSetProcessKillOnExit(TRUE)` after the connection exists, then uses `WaitForDebugEventEx` only in finite slices bounded by the same remaining monotonic deadline, never `INFINITE`, a task, APC, or another thread. P5 freezes a total event state machine: the first CREATE_PROCESS is the expected adapter-created root, whose exact argv is already known to the creator; DEBUG_PROCESS descendants must match the closed expected process order, unique PID, executable/module seals, and inner membership before continue, while their argv semantics are carried only by the sealed parent binary/source plus its exact input/environment and are not falsely claimed as runtime-observed; CREATE_THREAD/EXIT_THREAD and CREATE_PROCESS/EXIT_PROCESS handles follow the documented system-close-after-exit-continue ownership and never alias PROCESS_INFORMATION handles; each nonnull CREATE_PROCESS/LOAD_DLL `hFile` is identity/seal-checked and closed exactly once by the debugger, while a null file handle uses the frozen mapped-module query; LOAD/UNLOAD relations are balanced; OUTPUT_DEBUG_STRING and first/second-chance exception code/count/disposition are exact per operation; RIP or an unknown event is terminal. `ContinueDebugEvent` uses only the table's exact `DBG_CONTINUE`/`DBG_EXCEPTION_NOT_HANDLED` disposition.

If an abort is selected while an event is pending, the pump records one cause, switches to the immutable shared cleanup cutoff supplied by the host, closes any event-owned file handle, calls `TerminateJobObject(inner)`, continues that event exactly once, and keeps pumping finite slices through the required EXIT events under `min(fault_qpc+5 seconds,shared_cleanup_cutoff_qpc)`. It never waits for root/Job zero while leaving a debuggee stopped. Event, process, thread, and DLL-handle controls cover unknown child/DLL, first- and second-chance exceptions, timeout with a pending event, and creator-thread death; cleanup must end with the required exit inventory and no uncontinued event.

The sealed private-desktop and Opus wrappers are provenance for their external argument/result contracts only; neither wrapper's runtime `Add-Type`, `ProcessStartInfo`, `Start-Process`, disk redirection, `taskkill`, or inherited-environment implementation executes. P5 replaces them with marked native-profile bodies that load only the P5-embedded precompiled runner/validator bytes, preserve the already-reviewed external schemas, and invoke a closed operation row. The new implementation builds every root and permitted descendant environment from an exact per-row, case-insensitive-unique table rather than cloning/subtracting the parent; uses anonymous stdin/stdout/stderr pipes with concurrent byte caps; and publishes fixed evidence leaves with CreateNew only after process, Job, debug, stream, and schema PASS. Each row owns one fresh non-project scratch root; `TEMP`, `TMP`, cache, application-data, config, and profile variables all point only inside that root or are absent. P5 freezes the exact writable leaf/directory closure, performs non-following pre/post inventories, rejects any outside/extra write, and non-followingly deletes and proves each scratch root absent after its last allowed read. The workflow creates or permits no application-controlled credential/config/history/scratch file containing the setup-token capability. Windows-managed paging, hibernation, WER/LocalDumps or other OS crash capture, the ancestor launcher's injection storage, and the remote authentication service's TLS/server-side processing are explicit external trust boundaries; S5 makes no physical-zero-disk or remote-memory-erasure claim about them. Within the reviewed application boundary every adapter-created mutable secret buffer is overwritten as specified, and a failure preserves only the already-declared nonsecret evidence/failure paths.

The CPython AST row uses the authenticated interpreter with `-B`, an empty semantic environment, operation-owned TEMP/TMP, and exact zero pyc/cache/temp residue. The Opus row launches the fixed authenticated `claude.exe` directly; the launcher/module remain sealed provenance for validation semantics and are not process sources. `lpApplicationName` and argv[0] are the authenticated canonical executable; there is no `ClaudeExecutable` environment key and no APPDATA/PATH executable discovery. Its ordered argv after argv[0] is exactly `--safe-mode,--name,invoke-opus-4-6,--system-prompt,"Answer the user directly.",--prompt-suggestions,false,--model,claude-opus-4-6,--effort,max,--setting-sources,"",--strict-mcp-config,--mcp-config,"{}",--tools,"",--no-session-persistence,-p,--input-format,text,--output-format,stream-json,--include-partial-messages,--verbose`, with the prompt delivered only through the bounded stdin pipe and the same strict stream/result validation formerly supplied by the provenance pair. The authenticated target binary's frozen option table proves that `--prompt-suggestions` accepts the separate value `false`; P5's argv parser/control requires those two exact tokens and zero `prompt_suggestion` stream message. The child environment is built from exactly 33 case-insensitive-unique keys: the six native transport keys; the eight scratch keys `APPDATA,LOCALAPPDATA,USERPROFILE,HOME,TEMP,TMP,CLAUDE_CONFIG_DIR,CLAUDE_CODE_TMPDIR`; the exact 18 policy keys `CLAUDE_CODE_NO_MODEL_FALLBACK=1,CLAUDE_CODE_MAX_RETRIES=0,CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1,CLAUDE_CODE_DISABLE_OFFICIAL_MARKETPLACE_AUTOINSTALL=1,ENABLE_CLAUDEAI_MCP_SERVERS=false,DISABLE_UPDATES=1,DISABLE_TELEMETRY=1,DISABLE_ERROR_REPORTING=1,DO_NOT_TRACK=1,CLAUDE_CODE_DISABLE_AUTO_MEMORY=1,CLAUDE_CODE_DISABLE_CLAUDE_MDS=1,CLAUDE_CODE_DISABLE_ATTACHMENTS=1,CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1,CLAUDE_CODE_DISABLE_CRON=1,CLAUDE_CODE_DISABLE_BUNDLED_SKILLS=1,CLAUDE_CODE_DISABLE_POLICY_SKILLS=1,CLAUDE_CODE_DISABLE_WORKFLOWS=1,CLAUDE_CODE_SKIP_PROMPT_HISTORY=1`; and the one sensitive `CLAUDE_CODE_OAUTH_TOKEN` value supplied from the Task-3 sensitive binding. No API key, refresh token, endpoint, proxy, provider, credential path, or inherited Claude/Anthropic variable is fabricated or copied. `APPDATA`, `LOCALAPPDATA`, both home variables, `CLAUDE_CONFIG_DIR`, and `CLAUDE_CODE_TMPDIR` resolve only below the fresh operation scratch root. The authenticated binary's unconditional global `numStartups` write and every config/history/lock/temp/atomic-replace row are therefore confined to that exact scratch writable closure and are deleted with the root; the token itself is never an allowed file value.

The only supported subscription credential seam is an official Claude Code setup-token capability produced separately by `claude setup-token` and supplied under the exact host-only name `RECOVERY_V5_CLAUDE_OAUTH_TOKEN`. It is a one-year inference-only subscription capability for `CLAUDE_CODE_OAUTH_TOKEN`, not an Anthropic API key, and is never derived from `.claude.json`, `.credentials.json`, a registry value, guessed fields, or current process state. The user-supplied nonsecret Task-3 account attestation is canonical strict-UTF-8 JSON with exact ordered fields `schema_version,purpose,approved_plan_commit,approved_spec_commit,provider,account_class,managed_settings_disposition,credential_use_authorized` and exact values `1,"recovery-v5-opus-account",P5,S5,"claude-ai-setup-token","personal-unmanaged","unsupported-for-this-account",true`. It is transported only as the Task-3 frame's bounded base64-plus-SHA binding, is not durable authority, and contains no credential material. Generating or supplying the setup token is a later explicit execution prerequisite; S5/P5 design review neither invokes `claude setup-token` nor reads a credential.

The orchestration host accepts the setup-token capability only when a fresh user-launched, single-purpose execution host with no concurrent environment writer receives `RECOVERY_V5_CLAUDE_OAUTH_TOKEN` as one process-private environment entry. Before target launch and before any project leaf, the reviewed native adapter makes exactly one `GetEnvironmentVariableW` call into a pinned `WCHAR[4097]` buffer. It checks the native return and last-error contract, unchanged canary, one terminating NUL, length 1-4,096, and strict ASCII with no embedded NUL/CR/LF; a zero or required-size-overflow result is invalid. In one `finally` it calls `SetEnvironmentVariableW(name,NULL)` for every present or possibly present value and accepts only logical deletion or the exact already-absent error, without claiming that Windows erased the old environment-block backing allocation. Missing, empty, malformed, oversize, or logically undeletable input stops host-only before target launch, every Task-3 root remains absent, and Opus invocation count remains zero. The adapter never prints, hashes, fingerprints, compares to a literal, returns, or persists the value. Writer/frame temporary arrays are overwritten immediately after their last write, but one pinned matcher set is intentionally retained until all outer stream/result and target-scratch leak scans finish; a single host `finally` then overwrites every remaining matcher/value array on success, launch/write failure, or abort. This contract does not pretend to clear an ancestor process environment: the user-owned launcher must inject the capability only into the fresh execution host.

After L5, P5, Task-1 completion, and Task-2 completion authenticate, but before creating any Task-3 copy root, run root, prompt leaf, Opus scratch root, or other durable/ephemeral namespace, Task 3 strict-validates the account attestation, proves every Task-3 target root absent, and only then permits decoding the already-buffered sensitive binding. The host writes canonical base64 directly from a temporary mutable writer array to the anonymous pipe; the fixed-buffer target parser decodes and canonical-reencodes directly from mutable character arrays, so the accepted bytes are exactly the bytes transported by that sole writer without a secret hash or echo. Writer/frame temporaries are overwritten after write, while the host retains pinned matchers for exact ASCII bytes, exact UTF-16LE bytes, canonical base64 of ASCII, and canonical base64 of UTF-16LE until all leak scans finish. The target body constructs each exact child environment block directly in pinned mutable memory, copies the same token only to `CLAUDE_CODE_OAUTH_TOKEN`, and overwrites that per-call block immediately after `CreateProcessW` returns. The target overwrites the raw sensitive-character array immediately after decode and on every pre-decode authority/parser failure; its same four-representation matcher set and master token buffer survive only through the three serial calls and final scratch scan, then are overwritten on third-call completion or any failure. No adapter/loader managed `String`, application-controlled durable file, environment snapshot, frame echo, result field, checkpoint, diagnostic, hash, or later phase may contain the capability; only each single-process authenticated `claude.exe` child environment/memory and the remote authentication path may receive it during that call. P5 statically binds the sealed CLI path by which `CLAUDE_CODE_OAUTH_TOKEN` supplies authentication and proves that this path never passes the token to application config, credential, history, telemetry, or application crash-report persistence; a dummy executable validates the environment/zeroization contract without exposing the dummy value. Raw stdout/stderr remain sensitive until strict validation; rejected or unparsed buffers are overwritten without printing. P5 approval uses only that synthetic dummy capability and dummy executable and performs zero `claude.exe`, network, auth, or model calls. The later Recovery-v5 execution authority must explicitly cover setup-token use; at this S5 checkpoint the host capability is absent, so current Task 3 is honestly `NEEDS_CONTEXT` before any root and Opus count remains zero.

That same pre-root preflight requires the local managed-settings surfaces to be absent: `HKLM\SOFTWARE\Policies\ClaudeCode`, `HKCU\SOFTWARE\Policies\ClaudeCode`, `C:\Program Files\ClaudeCode\managed-settings.json`, the entire `C:\Program Files\ClaudeCode\managed-settings.d` drop-in directory, `C:\Program Files\ClaudeCode\managed-mcp.json`, and `C:\Program Files\ClaudeCode\CLAUDE.md`. The single-controller/no-external-writer execution precondition explicitly covers those registry/file surfaces for the complete Task-3 scope, and the body re-proves all six absences immediately before and after each real call; no directory handle is falsely claimed to lease absence. Any drift is terminal and no output is accepted. The personal-unmanaged account attestation is the explicit trust boundary for the otherwise unobservable server-managed tier; a Team/Enterprise/unknown account, a missing attestation, or any later evidence of managed policy stops before roots or terminates the call and requires a new authority decision. The operation cwd is its empty scratch root; empty setting sources, strict empty MCP config, tools-empty mode, the exact disable table, and the exact profile/config boundary prevent user/project/local hooks, skills, MCP, plugin, memory, update, and session sources from becoming executable inputs under that stated sequential threat model. P5 approval performs zero `claude.exe`, network, auth, or model calls. P5 statically proves that the sealed CLI parses exact `CLAUDE_CODE_MAX_RETRIES=0` as a zero API-retry budget; a missing, noncanonical, altered, or nonzero value is RED, and strict stream validation rejects every `system/api_retry` event. Missing/altered fallback key is RED, both observed-model collections must contain only `claude-opus-4-6`, and the stream contains zero `prompt_suggestion` message. Real authentication/model success is tested only by the exact three Task 3 Opus invocations; any failure stops without internal or controller retry.

Every bounded-tool/private-desktop and Opus row also freezes a window policy. Private operations and Opus run on a fresh private desktop created before process creation, with a P5-frozen unique name/ACL and that exact name in each root's `STARTUPINFO.lpDesktop`. A dedicated monitor thread calls and checks `SetThreadDesktop(hDesktop)` before creating any window/hook, creates its message queue, pins callback delegates, installs the out-of-context PID/Job-scoped WinEvent hook, and runs a finite event/message pump; a ready handshake must complete before root creation/resume, and each debug CREATE_PROCESS PID is registered before continue. `MsgWaitForMultipleObjectsEx` and `PeekMessageW(PM_REMOVE)` consume only finite slices of the operation deadline on the normal path and the same immutable shared cleanup cutoff after an abort; one private stop event plus `PostThreadMessageW` supplies bounded wakeup. The pump records every show/create event and serializes/rejects callback reentrancy. After inner `ActiveProcesses=0`, hooks remain armed while the monitor owner thread drains to a P5-frozen queue/quiescence barrier, performs final `EnumDesktopWindows`, unhooks, runs one final queue/error check, stores its typed result, and returns. The adapter thread consumes the same remaining cutoff to finite-join that monitor from outside; only after a successful join and result check does the unique desktop-handle owner call `CloseDesktop` last. The monitor never joins itself or closes a handle owned by another thread. Uncertain pending delivery is terminal. Any visible top-level window, short-lived flash, monitor/callback/pump fault, unknown desktop/window/PID, nonzero final enumeration, join failure, or close failure terminates the inner Job. A GUI-dummy descendant that opens and closes a window at process exit is RED, and console-only execution is GREEN. `CREATE_NO_WINDOW` or final enumeration alone is never accepted as visible-window proof.

P5 freezes exact action deadlines in its phase table and none exceeds 21,600,000 ms. Before any setup, the host reads one QPC frequency/start, computes in checked arithmetic the immutable `operation_cutoff_qpc=start+phase_budget` and `shared_cleanup_cutoff_qpc=operation_cutoff_qpc+5 seconds`, and supplies those canonical integers in the authenticated transport context to every target/inner adapter. The launcher uses the operation cutoff for frame write, root exit, inner/outer Job state, debug inventory, window monitoring, and both drains; the orchestration layer polls or yields at least once per 60 seconds without changing it. An early inner fault may use only `min(fault_qpc+5 seconds,shared_cleanup_cutoff_qpc)`; an outer takeover uses only the remaining time to that same absolute cleanup cutoff. No process starts a local replacement clock. An inner-operation fault calls `TerminateJobObject(inner)` while retaining its handle and uses that cutoff to prove the inner root signaled, inner `ActiveProcesses=0`, required debug termination events, window-pump/barrier/unhook/join completion, and both reader completions. A target/transport timeout, cap, read/write, query, or root failure calls `TerminateJobObject(outer)` while the host retains the outer handle; nested-Job termination covers the target and every inner descendant. The same absolute cutoff must then show the target root signaled, outer `ActiveProcesses=0`, stdin writer completion, both reader threads completed, window/debug pumps joined, and every pipe end reached its single owner-close state. Each reader result is exactly `clean_eof`, `overflow`, `read_fault`, or `forced_close`; only normal PASS permits two `clean_eof` values. P5 freezes cap-plus-one handling as overflow followed by bounded discard-drain to EOF without growing or exposing the buffer. A hard read fault or forced close can still accompany proven process containment, but sets `stream_valid=false` and forbids parsing/forwarding; it is never mislabeled EOF. Only the outer root/Job/handle convergence may set `containment_proven=true`, independently of stream validity. Closing either final Job handle is a finally fallback, never the termination or proof mechanism. On normal completion the target exit must be 0, both pipes clean EOF, outer `ActiveProcesses=0`, and outer `TotalProcesses` must equal the exact phase-observed root-plus-descendant count rather than a hard-coded one. A failed target exposes no checkpoint/handoff bytes to the next phase. Timeout controls combine a pending debug event, queued SHOW notification, and saturated pipe, and require both processes to echo the identical cutoff values while total wall clock remains at most the operation budget plus five seconds.

The loader and phase table impose hard pre-authentication bounds: total ASCII frame at most 16,777,216 bytes; decoded body at most 8,388,608 bytes; body base64 at most 11,184,812 characters and 2,731 chunks; each base64 chunk at most 4,096 characters; aggregate decoded opaque handoffs at most 2,097,152 bytes and each at most 1,048,576 bytes; one sensitive binding at most 4,096 decoded ASCII bytes, 5,464 base64 characters, and two chunks; metadata line at most 256 ASCII characters. A fixed-buffer byte/character reader enforces per-line and aggregate caps before string concatenation, decimal conversion, allocation, or base64 decode; `[Console]::ReadLine()`/`ReadToEnd()` are forbidden. For each phase the loader embeds the exact body bytes/SHA/base64 length/chunk count, exact ordered binding names/kinds/count/caps, first executable line, parameter signature, primary authority kind/path, and project-leaf order. All nonfinal body chunks are exactly 4,096 canonical base64 characters; the final chunk is 1–4,096; EOF follows one fixed end marker. Sensitive characters are accumulated only in pinned mutable arrays, never a `String`, and are not decoded before the phase's dynamic nonsecret authority gates pass.

The ASCII frame contains fixed magic/version, exact phase, separate uppercase reviewed P5 SHA, the phase's primary uppercase authority SHA or literal `NONE`, then canonical unsigned-decimal `qpc_frequency,phase_start_qpc,operation_cutoff_qpc,shared_cleanup_cutoff_qpc`, its closed ordered typed binding vector, and the exact body metadata/chunks/end marker. The loader validates positive frequency, checked monotonic arithmetic, the phase-table budget relation, and exactly five seconds from operation to cleanup cutoff before any value becomes a wait bound; target output echoes all four values and the host requires byte-identical canonical decimals. The only binding kinds are `SHA256` (one uppercase digest), `OPAQUE_BASE64_SHA256` (canonical base64 plus its paired uppercase digest), and `SENSITIVE_BASE64` (canonical base64 with no digest/fingerprint/echo). A sensitive binding is external capability data, never authority; its name/count/cap are frozen but its value is not. No free-form string, path, code, or ordinary environment binding exists. Task 1 vectors are exact: admission publication has none; PRE_PATCH has admission SHA; POST_PATCH has admission then RED SHA; POST_OBSERVER_PATCH has admission SHA, generator-completion SHA, generator-AppData SHA, then bounded generator-AppData base64; CLEANUP has admission, generator-completion, observer-completion, mother, generator-AppData SHA/base64, then observer-AppData SHA/base64. Task 2 has Task-1-completion SHA. Task 3 has Task-1-completion SHA, Task-2-completion SHA, account-attestation SHA, bounded account-attestation base64, then exactly one `SENSITIVE_BASE64` setup-token capability. Every non-Task-3 vector contains zero sensitive bindings. P5 freezes every other admitted phase as an explicit zero-or-closed vector, explicitly rejects the phase name `PHASE_B`, and contains no selection/result/blind-map binding kind; no scope discovers a dynamic checkpoint from ambient state.

After bounded frame/EOF/parser validation, the loader performs the phase-defined first project-leaf gate with `Open-V5AuthenticatedLeaf`: P5 for M5 publication; M5 for L5 publication; L5 for Task 0/1/2/3. Before that gate succeeds it opens no other project leaf and executes no framed code. It then opens P5 as the second allowed leaf where distinct, retains both leases/buffers, extracts the uniquely marked body only from authenticated P5 `content_bytes`, and requires byte equality with the framed body plus exact table metadata, strict UTF-8 round trip, unique markers, signature, first line, and zero nested markers. M5 publication aliases primary/P5 to the same one read/lease. The loader invokes the body with one authenticated context containing the phase, immutable authority/P5 byte buffers and live leases, body identity, and typed nonsecret bindings, plus a separate guarded sensitive-buffer capability only for Task 3. The body may neither reopen nor replace authorities, expose the sensitive buffer through reflection/serialization, nor retain it beyond the one Task-3 action.

Within each Task body, dynamic authority leaves precede P5 raw-Git identity, M5/topology, or any unrelated project access. PRE_PATCH authenticates admission as the third project leaf. POST_PATCH authenticates admission third and RED fourth. POST_OBSERVER_PATCH authenticates admission third and generator completion fourth. CLEANUP authenticates admission, generator completion, observer completion, and mother in that order. Task 2 authenticates Task 1 completion third. Task 3 authenticates Task 1 then Task 2 completion, strict-validates the nonsecret account attestation, and completes the setup-token-capability/managed-settings preflight before any Task-3 root. Opaque AppData bytes are decoded only after their preceding SHA/checkpoint leaves pass. The admission-creation, Task 0, and publication bodies have their own P5-frozen exact order. Source/static controls reject a body that reaches Git, M5, topology, an opaque decode, or another leaf early; a Phase B marker, body, branch, or selection reader is a static failure.

Each body returns exactly one P5-frozen ASCII result frame and no other stdout; stderr is bounded diagnostic-only. The output table freezes phase/status, exact ordered checkpoint SHA names, exact opaque handoff names/types/caps, and canonical encoding. No output grammar has a sensitive field. Before either matcher set is overwritten, the target scans every application-controlled scratch leaf and the host scans outer stdout/stderr/result/checkpoint/diagnostic buffers for exactly four representations: raw ASCII token bytes, raw UTF-16LE token bytes, canonical base64 of the ASCII bytes, and canonical base64 of the UTF-16LE bytes. A match rejects without reporting the matched bytes; evidence records only representation kind, owning surface, and bounded offset. The host forwards a nonsecret value only after exit 0, outer containment PASS, empty-or-approved diagnostic stderr, exact output grammar, expected phase, both leak scans PASS, and `status=PASS`; values remain in controller memory and are copied only into the next closed input vector, never environment/source/temp files. Failure output is not authority and cannot be forwarded.

P5 includes transport RED/GREEN controls for the historical interpolation failure; altered phase/P5/authority/binding/body/hash/length; altered/noncanonical/overflowed QPC fields or cutoff relation; reordered/missing/extra binding; oversized metadata/body/chunk/frame/opaque/sensitive value; noncanonical base64; premature end; extra post-frame byte; parser/signature/first-line/marker mismatch; target echo/result mismatch; wrong first/second/dynamic project leaf; authority or P5 swap/write/delete during a retained lease; and framed-body-versus-P5 mismatch. Sensitive controls reject a missing/empty/oversize/non-ASCII/CR/LF/NUL/logically-undeletable host capability, any concurrent host environment writer, any sensitive binding outside Task 3, any digest/fingerprint/echo/log/checkpoint or adapter/loader managed-String conversion, a missing/extra/drifted `CLAUDE_CODE_OAUTH_TOKEN` child key, each of the four sensitive representations in streams/results/scratch, any credential-file open/write, premature matcher destruction, failure to overwrite each buffer/environment block, and a Task-3 root created before all nonsecret gates PASS. Task-3 controls also reject missing/false/reordered/account-or-commit-drifted attestation, Team/Enterprise/unknown account class, every local managed-settings source, config/profile writes outside scratch, any Opus descendant attempt, final Opus `TotalProcesses` other than one, a missing/noncanonical/nonzero/drifted `CLAUDE_CODE_MAX_RETRIES` key, any `system/api_retry` event, a Phase B phase/body/vector/reader, and any `prompt_suggestion` stream message. The absent-capability CONTROL must end with every Task-3 root absent and Opus count zero; the synthetic three-call CONTROL proves the same pinned dummy token reaches all three single-process dummy children, never a real Claude process, all four matchers remain usable through final scans, and every copy is overwritten after call three or the first fault. Process controls cover poisoned inherited CLR/PowerShell variables, a profiler request, wrong SystemRoot, app-directory DLL collision, closure drift, pipe saturation, timeout, any production breakaway flag/limit, an unknown child stopped at its debug event, nested pipe-less survival, inner-Job handle loss, and outer-Job whole-tree termination/reproof. Controls run once with no ambient Job and once inside a benign nonbreakaway ambient Job. A synthetic ambient hierarchy/UI/active-process condition that rejects the outer `CreateProcessW` must prove no root/resume/project access. A descendant denial or post-resume time/memory/CPU termination follows the ordinary inner/outer fault path only while the launch host remains alive. The ambient-time negative control uses an outside supervisor, a disposable ambient launch-host, and the outer target: if the ambient Job terminates the launch-host itself, the supervisor proves the disposable host and its ambient Job reach zero; the host's outer-handle loss supplies kill-on-close fail-safe containment, but no missing host may fabricate `containment_proven=true` or forward output. Every such failure is terminal if a one-shot leaf already exists. Ambient state is never authority or success evidence. A dedicated `CONTROL` phase uses only authenticated synthetic bytes and round-trips every executable body through a fresh clean target without project access.

A host-only extraction/control failure before target launch creates nothing and stops; there is no automatic retry. Once any target is launched, every transport/bootstrap/body mismatch is terminal for that authorized action and no fresh process, alternate framing, corrected wrapper, or fallback is allowed. A later explicit retry may use only the identical frozen P5 transport and exact phase table, and only if its named action's own durable one-shot leaf/root is still absent; a Task-3 retry additionally requires a newly launched execution host and a fresh one-time injection of the separately authorized setup-token capability, never a cached value or the cleared/zeroed prior host. Changing any loader/launcher/environment/frame/body contract requires a new append-only spec/plan lineage.

### SHA interfaces

P5 defines only:

```text
Get-V5Sha256ForBytes(bytes) -> uppercase_sha256
Get-V5FileSeal(path) -> path,bytes,sha256
Open-V5AuthenticatedLeaf(path,max_bytes,expected_sha256) -> path,bytes,sha256,content_bytes,lease
```

`Get-V5FileSeal` opens one canonical ordinary non-reparse leaf with `FileMode.Open`, `FileAccess.Read`, `FileShare.Read`, hashes the same stream with `System.Security.Cryptography.SHA256`, proves length before/after and EOF, and disposes in `finally`. Path-component and leaf reparse checks occur both before and after the stream. Every former `Get-FileHash` use migrates; executable PowerShell AST scans must find zero `Get-FileHash` commands.

First-leaf authority and second-leaf P5 transport never use a hash-then-reopen pattern. `Open-V5AuthenticatedLeaf` opens the fixed canonical leaf once with the same non-reparse checks and `FileShare.Read` only, rejects a length above its P5-frozen per-leaf cap before allocation, reads/hashes into one bounded byte buffer from that handle, requires the supplied uppercase SHA and exact expected length where fixed, and retains both the buffer and no-write/no-delete lease through every dependent parse, extraction, publication, or task action in that scope. Strict JSON and P5 marked-body extraction consume only `content_bytes`; the path is never reopened as authority. A finally block rechecks handle length/position and path identity before releasing the lease. Because Windows share access is enforced on the file object across hardlink aliases, the retained no-write/no-delete lease is the byte-stability primitive; the pre-authentication loader does not invent a native hardlink-count API. Swap, write, delete, reparse, stale-buffer, and hash-then-reopen controls must reject.

### Git executable and process interface

P5 does not discover Git from PATH. It freezes and uses only this canonical ordinary non-reparse executable:

- path `C:\Users\22325\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\git\mingw64\bin\git.exe`;
- 4,344,704 bytes;
- SHA-256 `C115A66A1BEDE6694B513AF420CC90F8775BE03666A54D1ECB82D6196B929FE9`;
- exact version text `git version 2.53.0.windows.3`.

The 46,464-byte `cmd\git.exe` shim and every PATH-selected Git are forbidden. Each fresh scope revalidates the fixed executable path/bytes/hash/version before use; poisoning PATH before or after that gate cannot change the selected program. The executable's complete non-system import closure in the same application directory is also frozen: `libiconv-2.dll` 1,136,529/`FF31FA811F9C07CC7FDAA68C9E8BCA3A7B4FDF6E0A079A58175EA58BA139C7AE`, `libintl-8.dll` 298,731/`0537C3DD2378218508EBE3CC416D72A99EE2D24AE1C5525E23458F32544EF861`, `libpcre2-8-0.dll` 717,955/`C135A87ED0F11EAE8FFC4CB469671FF0B3F5D71FAB5FB024E9B1E7241CA25B52`, `libwinpthread-1.dll` 64,931/`D66B00E4A4385344BF2BE54B03446EA19CED654C78A18A024A0B43971D68459B`, and `zlib1.dll` 120,814/`CB7AB3788D10940DF874ACD97B1821BBB5EE4A91F3EEC11982BB5BF7A3C96443`. P5 freezes and validates the recursive PE import table: these are the only non-system modules; every other import is an exact system DLL basename resolved from `%SystemRoot%\System32`. The process interface is:

```text
Invoke-V5GitProcess(
  repository_root,
  operation_class,
  subcommand_arguments
) -> exit_code,stdout_bytes,stderr_bytes
```

Input order and output order are fixed. `operation_class` is a closed P5 enum whose reviewed table derives read/mutation mode, allowed exit codes, timeout, both byte caps, and `empty` versus `capture_not_authority` stderr policy. A caller cannot supply or override those values; an argument vector inconsistent with its class is rejected before any native handle is created.

Implementation requirements:

- P5 embeds the complete reviewed C# source and one matching precompiled AnyCPU .NET Framework assembly for each closed native adapter as canonical base64. For each, P5 freezes source encoding/bytes/SHA, decoded assembly bytes/SHA, PE/CLR identity, module MVID, assembly/type/interface names, exact public-method surface, P/Invoke import table, reference identities, and build provenance. The preapproval dependency graph is acyclic: one disposable seed adapter is produced first from the same frozen source with the same sealed compiler closure and arguments in a third empty non-project root. This seed build is the sole preapproval compilation/launch-containment/stream exception. A dedicated x64 builder uses one direct `ProcessStartInfo`/`Process.Start`, `UseShellExecute=false`, `CreateNoWindow=true`, no redirected streams, and exactly two finite wait call sites: the normal/initial `WaitForExit(timeout)` and, only if it expires, one root `Kill` followed by a fixed at-most-five-second post-kill `WaitForExit` plus `HasExited`, exit-time, and process-handle reproof. It trusts the sealed compiler not to spawn a child and therefore makes no false Job, descendant, or byte-cap claim. A failed post-kill reproof stops without deleting the seed root or starting A/B. It still uses an empty environment, root-local TEMP/TMP, exact root/process pre/post census, fixed write allowlist, and non-following pre/post inventories, and never becomes authority or embedded bytes. After strict source/PE/import/metadata validation, the seed is loaded only in that disposable builder and launches exactly two authoritative csc builds A/B through the production CreateProcessW/JOB_LIST/HANDLE_LIST/drain seam in independent active-process-one Jobs. A, B, and seed must be byte-identical; only the independently reviewed A/B-equal bytes may be embedded. P5 freezes `csc.exe`, its config/runtime state, managed compiler/GAC/reference assemblies with physical paths/bytes/SHA/identities, native startup/import/loaded-module closure, exact `/noconfig`, no-response-file, no-shared-compiler, deterministic, no-PDB, explicit-reference, target/platform/output arguments, and prefer-System32/debug validation. MSBuild, dotnet, compiler server, implicit config/reference, response file, extra child/temp/output, drifted compiler/config/GAC/native module, and unrecoverable cleanup are forbidden. The seed and both build roots are non-followingly deleted and proved absent before P5 approval. Static controls require the exact seed-to-A/B DAG, exactly three compiler invocations, seed bytes never admitted, A=B=seed, and zero residual roots. At execution the controller strictly decodes/re-encodes and hashes embedded bytes with the .NET hash seam, rejects any preloaded assembly/type identity, loads exactly once with `[Reflection.Assembly]::Load([byte[]])`, and revalidates frozen metadata. Runtime/executable-body compilation, `Add-Type`, temp source/assembly files, disk assembly loading, a second load, or an unexpected referenced assembly is terminal;
- except for the one offline nonauthority seed csc launch above, no `System.Diagnostics.ProcessStartInfo` or `Process.Start` launch is permitted. P5 freezes Windows 10+/Server 2016+ and defines one audited Win32 interop layer around `GetWindowsDirectoryW`, `GetSystemDirectoryW`, exactly one `GetEnvironmentVariableW`, `SetEnvironmentVariableW`, native machine/WOW64 queries, `CommandLineToArgvW` plus its exact `LocalFree` ownership, `CreatePipe`, `SetHandleInformation`, `CreateFileW`, `CreateDirectoryW`, final-path/file-identity queries, `CreateJobObjectW`, `SetInformationJobObject`, `InitializeProcThreadAttributeList`, `UpdateProcThreadAttribute`, `DeleteProcThreadAttributeList`, `CreateProcessW`, `GetCurrentProcess`, `GetCurrentThreadId`, `IsProcessInJob`, `ResumeThread`, `TerminateJobObject`, `TerminateProcess`, `QueryInformationJobObject`, `GetExitCodeProcess`, `WaitForSingleObject`, `WaitForDebugEventEx`, `ContinueDebugEvent`, `DebugSetProcessKillOnExit`, `CreateDesktopW`, `SetThreadDesktop`, `CloseDesktop`, `SetWinEventHook`, `UnhookWinEvent`, `MsgWaitForMultipleObjectsEx`, `PeekMessageW`, `GetMessageW`, `TranslateMessage`, `DispatchMessageW`, `PostThreadMessageW`, `EnumDesktopWindows`, `GetWindowThreadProcessId`, `IsWindowVisible`, blocking `ReadFile`/`WriteFile`, mapped-module/path/identity queries, and the required close APIs. Exact structs, delegates, enums, access/share/creation/debug/window/message flags, event unions and dispositions, error handling, buffer arithmetic, callback lifetime, ownership, and x64 layout are frozen; `CommandLineToArgvW` output count/pointers are validated before copying and its allocation is released exactly once even on mismatch. The credential-capability path permits only the two named environment APIs, uses the fixed 4,097-WCHAR call shape, mutable pinned arrays, native last-error capture, canary/NUL checks, logical environment deletion, and explicit full-array overwrite postconditions, and never materializes the value as an adapter/loader managed `String`. There is no older-OS or later-`AssignProcessToJobObject` fallback;
- before any Git child, the host has already proved target membership in the exact outer Job before resume and still solely owns that outer handle; the target receives no Job handle. The target re-queries its immediate inherited Job with the null-Job form of `QueryInformationJobObject` and requires kill-on-close with no active-process, breakaway, silent-breakaway, or UI limit, while that shape plus the host's retained-handle proof supplies the cross-process relation. `CreateProcessW` then receives null process/thread security attributes, `CREATE_SUSPENDED | CREATE_UNICODE_ENVIRONMENT | CREATE_NO_WINDOW | EXTENDED_STARTUPINFO_PRESENT | DEBUG_ONLY_THIS_PROCESS`, a mutable command-line buffer, the exact sorted/double-NUL UTF-16 environment block below, `bInheritHandles=true`, and `STARTUPINFOEXW`; `CREATE_BREAKAWAY_FROM_JOB` is forbidden. Its attribute list has exactly three entries: `PROC_THREAD_ATTRIBUTE_HANDLE_LIST` with child stdin-read/stdout-write/stderr-write, `PROC_THREAD_ATTRIBUTE_JOB_LIST` with the already-created fresh inner Git Job, and `PROC_THREAD_ATTRIBUTE_MITIGATION_POLICY` with prefer-System32. `STARTF_USESTDHANDLES` binds the same three handles. The parent pipe ends, process/thread, Jobs, debug-event, attribute-list, and every unrelated handle are non-inheritable and absent from the child allowlist;
- `lpApplicationName` is the exact canonical Git executable and `lpCurrentDirectory` is its sealed canonical `mingw64\bin` application directory, never a repository-controlled directory. Repository selection occurs only through the fixed `-C <canonical repository root>` argv pair. The executable and all five non-system DLLs are opened with `Open-V5AuthenticatedLeaf`; the same authenticated streams/buffers remain the no-write/no-delete leases through process/debug completion and post-reproof. The mutable `lpCommandLine` contains that executable as argv[0] followed by the ordered `string[]` arguments, encoded with the complete Windows `CommandLineToArgvW` reverse 2n/2n+1 backslash-and-quote algorithm. Null entries, U+0000, unpaired UTF-16 surrogates, and a buffer over 32,767 UTF-16 code units including its terminal NUL are rejected;
- P5 freezes the recursive normal/delay import graph and the exact per-operation loaded-module allowlist. A debug-event loop validates the main image and every `LOAD_DLL` event's canonical path, ordinary/non-reparse identity, bytes/hash, and expected System32-versus-sealed-application classification before `ContinueDebugEvent`; the module's entry point cannot run first. The current normal-import system basenames are exactly `ADVAPI32.dll,KERNEL32.dll,msvcrt.dll,ntdll.dll,USER32.dll,WS2_32.dll`; the audited dynamic-load candidate set adds exactly `bcrypt.dll,kernelbase.dll,psapi.dll,secur32.dll,ucrtbase.dll`. The only non-system modules are the five sealed DLLs above, and no delay import exists. P5 proves every listed system basename absent from the Git application directory and present at the authenticated System32 identity, proves every non-system DLL absent from System32, and requires each operation's observed module subset to equal its closed row. Prefer-System32 plus exact event validation rejects app-directory system-name poisoning and any dynamic extra module;
- a process-wide launch mutex covers the complete interval in which inheritable child pipe handles exist. Immediately after successful creation the parent closes its copies of all three child ends and closes the non-inheritable stdin-write end, delivering EOF so Git cannot consume real input;
- the two anonymous output pipes are drained concurrently by dedicated background threads using blocking `ReadFile` with fixed 65,536-byte scratch buffers. `ERROR_BROKEN_PIPE` is clean EOF; every other read failure is a reader fault. Each capture retains at most its class cap, detects the first cap-plus-one byte without integer wrap, marks overflow, then discard-drains under the unchanged deadline without growing or exposing the partial buffer. No `Process.StandardOutput`, `BaseStream`, `FileStream` overlapped mode, `ReadToEnd`, line event, or one-pipe-first drain exists;
- the inner Git Job is configured before `CreateProcessW` with exactly `JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE | JOB_OBJECT_LIMIT_ACTIVE_PROCESS`, `ActiveProcessLimit=1`, and no breakaway/UI flag. Successful creation atomically adds the root to this inner Job while ordinary nested-Job inheritance keeps it in the outer Job and any ambient ancestors: after the single child-end close in the preceding step and before the sole `ResumeThread`, both drains report ready, `IsProcessInJob(root,inner)` is true, and the inner Job reports exactly one active process. `ResumeThread` is called exactly once and must return one. Any Git child-process attempt is denied before it can execute, while final inner `TotalProcesses=1` remains an independent proof; outer accounting includes this root until it exits;
- before any Git pipe/thread/Job/root setup, the adapter reads `git_start_qpc` and derives in checked arithmetic `git_operation_cutoff_qpc=min(host_operation_cutoff_qpc,git_start_qpc+class_budget)`: read 30 seconds, index add/reset and commit 60 seconds, and worktree add/remove 120 seconds. This is a bounded child cutoff under the host's immutable QPC context, not a new `Stopwatch` or reset. Setup, `CreateProcessW` return, reader readiness, the initial debug event, admission/query, sole resume, root/descendant exit, EOF, and reproof all consume its remaining ticks; abort work uses only `min(fault_qpc+5 seconds,host_shared_cleanup_cutoff_qpc)`. A synchronously stuck kernel call is a terminal native-call boundary, not permission to start another clock. Clock-injection controls stall before cutoff derivation, reader-ready, pre-resume query, and initial debug event; late-start/overflow/drifted-frequency cases must take the same abort/reproof path. There is no extra unbounded final drain;
- stdout is not exposed to a parser until, within that one deadline, the root handle is signaled, `GetExitCodeProcess` succeeds, `QueryInformationJobObject(inner Git Job)` proves `ActiveProcesses=0` and `TotalProcesses=1`, both readers ended at clean EOF without fault/overflow, exit code is allowed, and stderr policy passes. Any descendant creation, even one that exits before the root, is terminal; a root that exits while a pipe-less descendant remains is not success;
- failure cleanup is stage-exact. Before create, pipe/attribute/Job setup failure has no root and must prove inner `ActiveProcesses=0`; `CreateProcessW=false` likewise has no process/thread handle. After successful atomic creation, the suspended root is necessarily in the inner Job; admission/query/debug/resume failure first calls `TerminateJobObject`, and uses `TerminateProcess` only as the explicitly recorded root-handle fallback if Job containment/termination cannot be proved. After resume, timeout, capture overflow, debug/module rejection, reader fault, wait/query failure, or exit mismatch selects one terminal abort cause and calls `TerminateJobObject` exactly once while retaining the Job handle. Every post-create failure consumes the remaining time to the same host-supplied `shared_cleanup_cutoff_qpc` for root signaled, inner `ActiveProcesses=0`, required debug termination events, window monitor completion where present, both reader-thread terminal results, and every pipe owner's close state; no subsystem starts another cleanup clock. Clean EOF is required only for a nonfaulting stream, while overflow/read-fault/forced-close remains invalid data but does not masquerade as missing containment. `JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE` is a final `finally` fault-containment fallback, not the primary termination or reproof mechanism;
- every native return code and `GetLastWin32Error` is checked; attribute-list memory, child/parent pipe ends, primary thread, process, reader, and Job handles have one explicit owner and are released exactly once in reverse order only after the required reproof;
- a failed call exposes no stream bytes to an authority parser. Its typed result contains one exact failure code and native Boolean `containment_proven`; localized Win32 messages are diagnostic only and numeric `GetLastWin32Error` is captured immediately. Kill failure, descendant/process-handle/pipe reproof failure, malformed output, or disallowed exit is terminal `NEEDS_CONTEXT`, with no alternate transport and no retry;
- after a failed mutation, callers may run topology/index/status reproof only when `containment_proven=true`. Otherwise they issue no further Git command, preserve the site, and stop.

The Git child environment is built from empty and has exactly 17 case-insensitive-unique keys; it never snapshots or subtracts from the inherited environment. Native Windows/System32 values are the same authenticated values used by the transport launcher. The exact set is:

```text
ComSpec=<canonical System32>\cmd.exe
GIT_CONFIG_NOSYSTEM=1
GIT_CONFIG_GLOBAL=NUL
GIT_ATTR_NOSYSTEM=1
GIT_TERMINAL_PROMPT=0
GCM_INTERACTIVE=Never
GIT_PAGER=cat
PAGER=cat
LC_ALL=C
LANG=C
LANGUAGE=C
NO_COLOR=1
Path=<sealed mingw64\bin>;<canonical System32>;<canonical SystemRoot>
PATHEXT=.COM;.EXE;.BAT;.CMD
SystemDrive=<canonical Windows drive>
SystemRoot=<canonical Windows directory>
windir=<canonical Windows directory>
```

Entries are sorted with `StringComparer.OrdinalIgnoreCase` and serialized without locale dependence as UTF-16 `name=value<NUL>` records plus one final NUL. Invalid names/values, NUL, a hidden drive entry, unknown/duplicate key, inherited HOME/XDG/TEMP/editor/askpass/MSYS/CYGWIN/loader/profiler variable, or count other than 17 is terminal. The immutable buffer remains alive through `CreateProcessW` and is then zeroed/freed. The exact application/current directory, authenticated module leases, prefer-System32 mitigation, debug-event module allowlist, fixed Path, and System32-only system-module rule close the DLL search boundary. The root executable remains fixed by `lpApplicationName`; arbitrary descendants are atomically denied by the inner active-process limit.

Every invocation begins with this exact ordered global argv prefix:

```text
--no-pager
--literal-pathspecs
--no-replace-objects
-c core.quotepath=false
-c core.autocrlf=false
-c core.eol=lf
-c core.safecrlf=true
-c color.ui=false
-c core.pager=cat
-c core.hooksPath=NUL
-c core.excludesFile=NUL
-c core.attributesFile=NUL
-c core.fsmonitor=false
-c core.untrackedCache=false
-c maintenance.auto=false
-c gc.auto=0
-c gc.autoPackLimit=0
-c diff.external=
-c diff.trustExitCode=false
-c i18n.logOutputEncoding=UTF-8
-c i18n.commitEncoding=UTF-8
-C <canonical repository root>
```

Read mode inserts `--no-optional-locks` immediately after `--no-pager`. No call may add, omit, reorder, or override a common entry. External diff and textconv options are also passed at the relevant diff call site. Within the closed operation table and the repository-local authority contract below, system/global Git config, inherited variables, replacement refs, pager, hooks, aliases, global exclude/attribute files, fsmonitor, auto-maintenance, and untracked cache cannot alter the reviewed built-in call semantics; PATH cannot select the root executable. No broader claim is made for an arbitrary Git subcommand or descendant process, and neither is permitted.

### Repository-local Git authority

Git's repository-local inputs are authority, not ambient implementation detail. P5 freezes the current common repository administration paths and exact states:

- common config `E:\Projects\renpy-8.5.2-sdk\CourtOfShadows\.git\config`: 346 bytes/SHA-256 `F4FCFFC0799917C07FFA924F575025863934E6A7C0BE5E82732647E18A933087`;
- common `info/exclude`: 254 bytes/SHA-256 `2F1E1A7B050053E565FC8228BAD79BA0A8D38C7DA1FBE91A149B96260247AD82`, whose only active rule is `.superpowers/`;
- common `info/attributes` absent;
- per-worktree `config.worktree` absent and common `extensions.worktreeConfig` absent;
- common `objects/info/alternates`, `info/grafts`, `shallow`, and `modules/` absent;
- tracked `.gitattributes` and `.gitmodules` absent from P2/S3/P3/S4/P4/S5/P5 and the working tree; R5's fixed three-path mutation cannot add them;
- `refs/replace/` empty and no submodule gitlink in any approved tree.

Repository selection is also authority. Every allowed `repository_root` belongs to a closed P5 table and must resolve through one authenticated linked-worktree identity into the same canonical common directory `E:\Projects\renpy-8.5.2-sdk\CourtOfShadows\.git`. The three pre-existing rows are exact:

- approved P5 root `C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\work\CourtOfShadows-governance-winter`: `.git` 99 bytes/`2FD45D1EFB8DFB8D7358A3643490F30581A685667C0C769D63099020E0511B07`, admin directory `E:\Projects\renpy-8.5.2-sdk\CourtOfShadows\.git\worktrees\CourtOfShadows-governance-winter`, admin `commondir` 6 bytes/`340DDCB67A6204F742CD1E28E5B462622DDE7DAAA8EE36001897196AACDC6D47`, and admin `gitdir` 96 bytes/`C9C39E333672083050997BD640DB5EDD92CA82E6D61F1C828DBFC27C13FB5A17`;
- preserved v2 root `E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-generator-recovery-v2`: `.git` 110 bytes/`7BAD00019EAA71C38EE4750CBCB7AB9E2FEADA7E32AB951B62F4F37181795340`, admin directory `E:\Projects\renpy-8.5.2-sdk\CourtOfShadows\.git\worktrees\cos-terminal-collapse-generator-recovery-v2`, the same exact 6-byte `commondir`, and admin `gitdir` 100 bytes/`4951C7FDEC323ACFD4FB09AA321BC8197B122D7A3D2356B7AEFDF638475848EC`;
- preserved v3 root `E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-generator-recovery-v3`: `.git` 110 bytes/`C039F3633FADF7F9BA2B821B3DF787F6A81501E79133FA4B86413C117A3E0D58`, admin directory `E:\Projects\renpy-8.5.2-sdk\CourtOfShadows\.git\worktrees\cos-terminal-collapse-generator-recovery-v3`, the same exact 6-byte `commondir`, and admin `gitdir` 100 bytes/`4C7A8FDBD654D7EF072E92821FC943D1CA3AE86149B21ED5AE9A11C7A0697582`.

P5 freezes the exact UTF-8/no-BOM/one-LF contents behind those seals: each root `.git` is one `gitdir: <absolute-forward-slash-admin-path>` line, each `commondir` is exactly `../..`, and each admin `gitdir` is the exact absolute-forward-slash back-pointer to that root's `.git` leaf. Before any Git call, all path components are canonical ordinary non-reparse paths; the root `.git` is an ordinary leaf; the admin directory is an ordinary direct child of the expected common `worktrees` directory; the strict pointer resolves to that one admin directory; `commondir` resolves to the expected common directory; and `gitdir` resolves back to the same root `.git`. Absolute/relative-format drift, another common directory, an extra indirection, case-fold alias, symlink/junction/reparse component, missing/extra line, CR/BOM, or path mismatch is terminal before Git launch.

Before every Git process, P5 uses `Open-V5AuthenticatedLeaf` on the two present common files plus the selected repository identity triple; their original authenticated streams/buffers are the leases, not later reopened handles. Before native launch it also re-proves every filesystem-level required absence listed above: info/config-worktree/alternate/graft/shallow/modules/replace paths, working-tree `.gitattributes`/`.gitmodules`, and selected root/admin relations. It holds the five leaf leases plus no-delete directory handles for the canonical repository root, admin directory, common directory, and common `worktrees` directory through process/Job/debug/read completion while allowing ordinary read/write access within those directories. The exact config is strict-parsed as the frozen benign key/value set: no include/includeIf, alias, filter, diff/textconv command, merge driver, hook path, maintenance, credential helper, signing program, pager, fsmonitor, worktreeConfig, worktree redirect, sparse/split index, or unknown key is accepted. The exact exclude file is metadata for status/ignore only and never becomes an artifact source. The execution threat model requires one controller and no external concurrent writer to the selected worktree/common-admin trees during a Git operation; the pre/post gates detect drift for result acceptance but do not falsely claim that directory handles prevent creation of new children. Any observed concurrent drift is terminal and no output is authority.

Tracked/index facts use one explicit noncircular discovery seam. After the .NET physical/identity gates, the only Git call allowed without prior fresh index evidence is a fixed read-only `repository_authority_probe` class: exact `ls-files --cached --stage -z`, no pathspec, no mutation, no filters/textconv/submodule recursion, and the read-mode common prefix. Its strict NUL parser returns exact `mode,oid,stage,path` records, requires stage zero, rejects `.gitattributes`, `.gitmodules`, mode `160000`, duplicate/case-fold paths, unknown mode, and malformed bytes, and binds the complete current index path/mode/OID set. That builtin does not consume attributes, filters, hooks, or submodule execution. Every later Git consumer or mutation is immediately preceded by fresh physical gates plus this probe, with no intervening controller project operation; after the call the same physical facts and mutation-specific index/tree/topology state are reproved before leases are released. Under the explicit single-controller/no-external-writer precondition, those gates bind accepted results; if pre/post facts differ, the result is rejected and the site is preserved. They are not described as an oplock against an adversarial concurrent filesystem writer.

Every fixed v5 worktree or mirror has one P5-frozen target root and one exact expected direct admin-directory path under the common `worktrees` directory. Both must be absent and their nearest existing ancestors ordinary/non-reparse before `worktree add --detach --no-checkout`. That mutation runs only through an already-authenticated existing row. On success, before any command uses the new root, P5 authenticates its newly created `.git`/`commondir`/`gitdir` triple with the same strict grammar and exact bidirectional/root/common relations, requires the exact expected admin directory rather than accepting a Git-selected suffix, and establishes the same leases. Immediately before exact `worktree remove`, the target triple is revalidated, then only the target identity-file/directory leases that would prevent deletion are released; no intervening project operation is permitted. Success requires the exact root and exact admin directory absent, the common authority unchanged, and a fresh authenticated worktree-list/topology reproof. Global prune and an alternate admin name are forbidden.

Negative controls use a disposable synthetic repository to prove rejection of local/global include, `filter.*.clean`/`smudge`/`process`, info/tracked attributes, external diff/textconv, hook, alias, maintenance, replacement-ref, submodule, and config/attributes drift before mutation. Successful Git operations must retain inner Git Job `TotalProcesses=1`; outer transport accounting remains the phase-observed aggregate. A synthetic filter, maintenance process, hook, or child Git proves descendant creation is rejected even if it exits quickly.

The repository's ordinary pre-commit hook is not executed by R5 commit. Its bare `sh → python → nested git` dependency chain would violate the one-Git-boundary and bounded job-tree contracts. Instead P5 folds the repository's mandatory `prepare_release.py` gate into the already-approved eighth invocation, `show-before-green`, whose private-desktop host already combines canon/show work. The ninth invocation remains `lint-green`; invocation/receipt/artifact counts remain 9/14/56:

- the common Git prefix fixes `core.autocrlf=false`, `core.eol=lf`, and `core.safecrlf=true`; Task 2 mirrors therefore materialize these two tracked scripts as their exact LF Git-blob bytes rather than inheriting this machine's system-level CRLF checkout policy;
- tracked `prepare_release.py` in the mirror must equal P5-tree blob `c575e44bcdba093d1b19c9a3810eebe99e3cca9f`, 2,305 bytes, SHA-256 `77F4DFA832A4E811145E303756C8E10E3FF53F400F8A465F58B13FA8519CF7F5`;
- tracked `subset_font.py` in the mirror must equal P5-tree blob `82ccd67bd157ee965c9704401a53eee9c3e84731`, 3,717 bytes, SHA-256 `E2C19CCA9AA65FFC830650DBE26DADD9B15C68CC68654E028EEB85E9F7D51F10`;
- source `C:\Windows\Fonts\msyh.ttc` must be 19,704,352 bytes with SHA-256 `D79C55E68B1131EEA0CC1C47BE4F572D964F28C682E143DB2AD09C1E4CB07A3F`;
- before the eighth invocation is admitted, P5 authenticates and copies one exact transient Python runtime into the scanner mirror at the sole hard-allowlisted path `.recovery-v5-python`. It never invokes the ambient installation directly. The source is `C:\Users\22325\AppData\Local\Programs\Python\Python311`, Python is exactly `3.11.9`, `python.exe` is 103,192 bytes/SHA-256 `5F7B89A612C9B8AF1D6456CDFCD1DBE5CA630849E79AEBCED9BEE9A6694952EC`, and `python311.dll` is 5,800,216 bytes/SHA-256 `0817A2A657A24C0D5FBB60DF56960F42FC66B3039D522EC952DAB83E2D869364`;
- P5 embeds the complete ordered source rows, not merely these two exemplar seals. The base slice is the fixed 15 release root binaries plus every non-`__pycache__` ordinary file below `Lib` except the entire `Lib/site-packages` subtree, and every non-`__pycache__` ordinary file below `DLLs`: exact 2,551 files/158,162,670 bytes, path catalog 82,459 bytes/SHA-256 `B046F198D1B54E8C009E6B68691979CE7B17C00702BB66D1519D776E29D7E928`, content catalog 261,347 bytes/SHA-256 `B7447CA504E3B1A2B344897EC4FE76F64218AA0973473FB221B1A87CBA71D39C`, and 185 directories with a 5,252-byte catalog/SHA-256 `105F5016371225B2A589391D596266B0BA1FBC7C97035BA5E4EDCF2F0C6E683E`;
- the only copied site distribution is `fontTools` `4.62.1`: exact `fontTools` plus `fonttools-4.62.1.dist-info` non-`__pycache__` trees, 355 files/11,009,871 bytes, path catalog 11,209 bytes/SHA-256 `07EAE0ED4611136201160CE5FE30D42BA5A2518AFEC797D55384AD8F19668734`, content catalog 36,086 bytes/SHA-256 `B885310396F647E5930E2DF80B016A3C69C036D17E50F8CB5D7B13318927B28D`, and 32 directories with a 625-byte catalog/SHA-256 `9ECD3FB27A1358CD87065EFF6965FBFBD2BDB3DDA46EC7659065FD9F1DEDCE8D`. Its `METADATA` is 119,789 bytes/SHA-256 `87F32B4AD7EE5EAA774203BFCF5E6C9F9D36BE280BB13B210B44B8921CDBDCE5`; its `RECORD` is 51,498 bytes/SHA-256 `D7118C9730FCF2895EEA9A307020E30D20C340140A27AEEAEED8DDFA84F9F3AD`;
- the catalog formats are frozen: path/dir catalogs are Ordinal-sorted normalized `/` relative paths plus LF; content rows are `relative_path<TAB>decimal_bytes<TAB>UPPERCASE_SHA256<LF>`. Before any source content is opened, P5 performs a non-following metadata traversal, rejects reparse/case-fold collisions, and exact-compares the allowed non-cache path and directory catalogs. It then opens each allowed source leaf once with read-only sharing, hashes and copies from that same stream into one CreateNew target leaf, proves source length/EOF/reparse state, and rehashes the completed target; no path is reopened as copy authority. Any ordinary `__pycache__` directory is excluded without reading or copying descendants and cannot become authority;
- P5 adds exactly two authenticated synthetic leaves. Root `python311._pth` is 39 bytes/SHA-256 `196E6BCBD6EB474F46B1F705B1C7141E5B1464998528C8F37B154ECDC0D04D64` and contains exact LF text `Lib`, `DLLs`, `Lib\site-packages`, `import site`, each on its own line with one final LF. `Lib/site-packages/sitecustomize.py` is the exact 1,683-byte LF appendix frozen below and in P5, SHA-256 `B6AC412C1C6710D05C926515671E367DBDF7DC72738DF2C134EFE34F25C4FC17`; it requires isolated/ignore-environment/no-user-site flags, exact three-entry canonical `sys.path`, and runtime-local prefix, sets `sys.dont_write_bytecode=true`, narrowly rewrites only the exact release parent's one positional `[sys.executable,"subset_font.py"]` subprocess call to `[sys.executable,"-B","subset_font.py"]`, reconfigures the existing stdout/stderr wrappers to strict UTF-8 without replacing or closing their shared buffers, retains native Windows CRLF translation, and calls `os._exit(120)` on any mismatch;

The exact `sitecustomize.py` preimage, including one final LF and no BOM, is:

```python
import os
import sys


def _fatal(message):
    try:
        os.write(2, ("V5_PYTHON_RUNTIME:" + message + "\n").encode("utf-8", "strict"))
    finally:
        os._exit(120)


try:
    _root = os.path.dirname(os.path.abspath(sys.executable))
    _expected = [
        os.path.normcase(os.path.join(_root, "Lib")),
        os.path.normcase(os.path.join(_root, "DLLs")),
        os.path.normcase(os.path.join(_root, "Lib", "site-packages")),
    ]
    _actual = [os.path.normcase(os.path.abspath(value)) for value in sys.path]
    if _actual != _expected:
        _fatal("sys.path")
    if not (sys.flags.isolated and sys.flags.ignore_environment and sys.flags.no_user_site):
        _fatal("flags")
    if os.path.normcase(os.path.abspath(sys.prefix)) != os.path.normcase(_root):
        _fatal("prefix")
    sys.dont_write_bytecode = True
    if sys.argv == ["prepare_release.py"]:
        import subprocess as _subprocess

        _subprocess_call = _subprocess.call

        def _call_with_subset_no_bytecode(*args, **kwargs):
            if (
                len(args) == 1
                and not kwargs
                and type(args[0]) is list
                and args[0] == [sys.executable, "subset_font.py"]
            ):
                return _subprocess_call([sys.executable, "-B", "subset_font.py"])
            return _subprocess_call(*args, **kwargs)

        _subprocess.call = _call_with_subset_no_bytecode
    sys.stdout.reconfigure(encoding="utf-8", errors="strict", newline=None, write_through=True)
    sys.stderr.reconfigure(encoding="utf-8", errors="strict", newline=None, write_through=True)
except BaseException as _error:
    _fatal(type(_error).__name__)
```

- the copied pre-run runtime is therefore exact 2,908 files/169,174,263 bytes, path catalog 100,108 bytes/SHA-256 `D1E5B76AAFF7F1B45ECCF342D738A2969EC7BCA80E658FC91C359118BEE4E304`, content catalog 304,011 bytes/SHA-256 `1EB58C2D8003F178C63EC9A15549ADE30041CE0995CAFFC5B785DEAD5A13D15A`, and 218 directories with a 6,471-byte catalog/SHA-256 `CEFE042C7650B5939A92E93C531CF0F264089F48F417035767CE5C47C22C6173`. Its `Lib/site-packages` contains only fontTools, its dist-info, and that one sitecustomize leaf; registry paths, ambient site-packages, `.pth` execution, usercustomize, pre-existing pyc, reparse points, and extra leaves are impossible;
- the eighth private-desktop job launches only the transient `python.exe -B <reviewed show-before host>`. Its freshly constructed environment removes every inherited case-insensitive `PYTHON*` name and adds no Python semantic override; isolation and UTF-8 are supplied only by the authenticated `_pth`/sitecustomize pair. The host, canon scanner, and release parent all start with `-B`; the authenticated sitecustomize shim permits only the release parent's exact one-positional list call and injects `-B` into its exact `subset_font.py` child. The host, `prepare_release.py`, and that child all use the same sealed runtime. Because sitecustomize reconfigures rather than replaces the original wrappers, tracked `subset_font.py` may safely install its own UTF-8 stdout wrapper over the still-open shared buffer. The single-controller/no-external-writer execution precondition plus `-B`, `sys.dont_write_bytecode`, the zero-cache prelaunch inventory, and the complete runtime/input leases require zero `__pycache__` directory or `.pyc` leaf before, during, and after every Python process; no cache leaf is ever executable input, permitted output, metadata exception, or deletion-only residue;
- that host runs the canon child, inline show scan, and exact `python.exe -B prepare_release.py` child in that order. Release is the final Python child: after it exits, no Python process or import occurs before the PowerShell caller verifies and deletes the transient runtime. Canon retains its 90-second child timeout, release has a 300-second child timeout, and the outer private-desktop timeout is exactly 420 seconds. Every descendant remains in the same kill-on-close private-desktop Job;
- immediately before launch and again after release exit, P5 non-followingly rebuilds the exact `subset_font.py` scan set from the fresh scanner mirror: 58 Ordinal-sorted tracked relative paths (57 `.rpy`, one `.py`), 1,240 catalog bytes, SHA-256 `AA5433C2D931CEE1052244AFCE0CAFC0C773FBA5F14285871B9B6841DF1DD7A3`. The main worktree's ignored `game/cache/shaders.txt` and `game/saves/navigation.json` are not present in, copied to, or authority for that detached mirror. The catalog format is normalized `/` path plus LF; directories, reparse points, missing paths, extra matches, case-fold collisions, or drift terminate. Existing mirror/tree seals remain the content authority, so this adds no durable leaf. In the final prelaunch pass, the verifier opens every one of the 2,908 transient-runtime leaves, all 58 scan-input leaves, and the exact `prepare_release.py`, `subset_font.py`, `Tools/scan_canon.py`, and show-host code inputs from the same authenticated handles used for their final seals, with read-only/no-write/no-delete sharing; it also retains non-delete identity handles for the runtime root and key module/script directories. Those leases remain continuously held through every Python descendant exit and the post-run catalog/seal checks. `game/msyh.ttf` is the single controlled writable output and is excluded from the read-only set, following its separate before/write/after state machine. The already-authenticated `C:\Windows\Fonts\msyh.ttc` is likewise opened once before launch with read access and `FileShare.Read` only and retained through the complete private-desktop Job and post-run seal recheck. Only after all descendants are gone and every postcheck passes are the input leases released in fixed reverse order; the transient-runtime leases are released immediately before its non-following deletion with no intervening process or project operation. Swap/write/delete controls at precheck-to-create and create-to-module-load boundaries must reject before any substituted code/input can execute;
- the strict one-line outer stdout is canonical strict UTF-8 JSON followed by exactly one CRLF and becomes schema 2 with exact ordered fields `schema_version,canon_executable,canon_arguments,canon_working_directory,canon_exit_code,canon_stdout_base64,canon_stderr_base64,show_exit_code,show_stdout_base64,show_stderr_base64,release_executable,release_arguments,release_working_directory,release_timeout_seconds,release_exit_code,release_stdout_base64,release_stderr_base64,runtime_path_catalog_sha256,runtime_content_catalog_sha256,font_before_sha256,font_after_sha256,backup_absent`. Integer/string/array/bool native types, exact executable/arguments/working-directory relations, canonical base64, uppercase hashes, and direct physical seals are all checked by the same validator at live receipt creation and final completion reread;
- both executable fields equal the canonical transient `python.exe`; arguments are exactly `['-B','Tools/scan_canon.py']` and `['-B','prepare_release.py']`; both working directories equal the canonical scanner mirror; `release_timeout_seconds` is integral `300`; catalog hashes equal the frozen transient catalogs; both font hashes equal `49A50578EF9B2853066A7FAB4CB79F97D5856EFDB83023E7A3D32902C2061135`; and `backup_absent` is native Boolean true. Any timeout/exception produces a failed private-desktop result, not a forged schema-2 PASS payload;
- release stdout is canonical strict UTF-8 with only paired CRLF line endings and exactly one terminal CRLF. It has exactly eight lines and no others, in this order: anchored scan-58/unique-character integers; anchored target-codepoint integer; exact source `C:\Windows\Fonts\msyh.ttc`/font-0 line; exact source-glyph count 29,905; anchored output `game/msyh.ttf` with one positive one-decimal KiB value; exact verification glyph count 3,709/missing count 0; exact coverage-success sentence; exact font-latest count 3,709 sentence. The scan/target integers are independently recomputed from the 58 authenticated strict-UTF-8 inputs and fixed ASCII/CJK/fullwidth ranges, and every captured integer uses canonical decimal form. There are zero `[!] 跳过 `, `[X]`, `[!] 字体新增`, or `[!] 字体移除` prefixes. Release stderr is empty. Exit 0 without this complete grammar is failure;
- exit code must be exactly 0. Exit 1 means the font changed, creating a terminal forbidden fourth changed path that is preserved for diagnosis; exit 2 or another exit is terminal tool failure. The transient `.ttf.prerelease_check` backup must be absent after success;
- before and after the operation, `game/msyh.ttf` must equal the P5-tree blob `4103d095775d89291a0987745083570c2a0b69c8`, 2,641,192 bytes, SHA-256 `49A50578EF9B2853066A7FAB4CB79F97D5856EFDB83023E7A3D32902C2061135`;
- on success the 2,908 authenticated leaves and 218 directories must still equal their complete pre-run path/content/directory catalogs, with zero additional leaf or directory and specifically zero `__pycache__`/`.pyc` path. The whole hard-allowlisted runtime is then deleted non-followingly, proved absent, and only then may the unchanged 14-field invocation receipt be created. Runtime preparation, verification, and deletion are folded into `show-before-green`'s existing `runner_or_scanner` assertion, so they add no receipt field or durable artifact;
- the full mirror tree/index/status is then reproved and may still contain only the exact three approved rules paths; a changed font, leftover backup, transient-runtime residue, or any other side effect stops before commit and is preserved;
- only after this mandatory release-font gate does central Git run the exact call-site suffix `-c user.name=2232517051 -c user.email=2232517051@qq.com commit --no-verify --no-gpg-sign --cleanup=verbatim -m <exact R5 subject>`. No author/committer environment variable survives the clean Git environment; both identities therefore resolve to those two explicit call-site values. The bypass is approved only because the repository-prescribed release gate has just run in the bounded reviewed seam and proved byte-identical. Post-commit topology and changed-path reproof remains mandatory.

No other hook exception exists. Other Git mutations also use `core.hooksPath=NUL` and cannot launch hook descendants.

Executable fences may not invoke Git through PowerShell's native-command adapter, contain an `& git`/bare `git` command, consume `$LASTEXITCODE`, or parse line-oriented Git paths.

### Exact Git output classes

P5 freezes distinct parsers:

1. `Read-V5GitOid`: exactly 40 lowercase ASCII hex bytes plus one LF; no `Trim`, CR, uppercase, or extra LF.
2. `Read-V5GitSubject`: `log -1 --format=format:%s%x00`; strict UTF-8, one nonempty field, one final NUL.
3. `Read-V5GitBlob`: only fixed `show <commit>:<path>` call sites; exit 0, stderr 0, stdout at most 8,388,608 opaque bytes. It never text-decodes, trims, or normalizes. Only after process/Job/debug/EOF PASS may the caller compare exact byte count/SHA and byte-for-byte equality with the retained authenticated physical buffer. Missing/extra/oversized bytes, disallowed exit, or stderr rejects.
4. `Read-V5GitPathList`: only `-z`; empty is zero bytes, nonempty ends in one NUL; strict UTF-8 decode/re-encode; no BOM, empty item, absolute path, drive prefix, backslash, `.`/`..`, exact duplicate, or case-fold collision. The parser preserves raw record order and never normalizes an unordered authority input into acceptance. A call site with declared set semantics may copy the accepted records, Ordinal-sort the copy, and compare that derived set explicitly.
5. `Read-V5GitIndexEntries`: only exact `ls-files --cached --stage -z`; each NUL record is strict ASCII mode, one space, 40 lowercase hex OID, one space, decimal stage, one tab, then one strict-UTF-8 path. It requires stage 0 and only ordinary reviewed modes, preserves raw order, and rejects malformed separators/widths, `.gitattributes`, `.gitmodules`, gitlink mode `160000`, duplicate/case-fold path, or invalid path by the same path contract.
6. `Read-V5GitNameStatus`: only `--no-renames --name-status -z`; exact records `status,score,path,original_path`. The parser recognizes only single-character `A,D,M,T,U,X,B`; score and original path must be null. Call sites then require exact raw records: S5 is `A` plus only the S5 spec path, P5 is `A` plus only the P5 plan path, and R5 is three `M` records for `game/balance.rpy`, `game/difficulty.rpy`, and `game/test_game.rpy` in exact Git order. Earlier S/P nodes likewise use their frozen one-path status/path pair.
7. `Read-V5GitStatus`: only `status --porcelain=v1 -z --no-renames --untracked-files=all --ignore-submodules=none`; exact records `xy,path,original_path`.
8. `Read-V5GitWorktreeList`: only `worktree list --porcelain -z`; exact fields `worktree,head,state,ref,locked,prunable`. Each entry begins with one worktree and one HEAD, contains exactly one `branch <ref>` or `detached` state, rejects `bare`, unknown/duplicate keys, lock/prunable reasons, and extra fields, and uses a double-NUL entry terminator. Call sites project the closed current/v2/v3/fixed-v5 selected roots and require each expected selected row exactly once, unlocked and nonprunable. Other pre-existing sibling rows are parsed but remain opaque non-authority: their raw records are snapshotted and must be byte-identical across a selected mutation, and their paths are never opened. Add/remove transitions admit exactly the one fixed target/admin row and preserve every sibling raw record; a global exact-worktree-set assumption is forbidden.
9. Exit-only readers: `check-ignore -q`, `diff --quiet --no-ext-diff --no-textconv`, and `diff --check` declare exact allowed exits and require the specified empty streams.
10. Mutations: `worktree add/remove`, `reset`, `add`, and `commit` use the same process boundary; their captured presentation output is never authority, and success is followed by independent read-mode topology/status reproof. `worktree add` is always exact `--detach --no-checkout`; checkout is a separate fixed-root `reset --hard --no-recurse-submodules` operation after repository-local authority reproof. This removes worktree-add's implicit child Git. `add` receives only the exact reviewed tracked paths after `--`; commit has `maintenance.auto=false`, explicit identity/message, `--no-verify`, `--no-gpg-sign`, and no editor.

All P4 Git classes migrate: `rev-parse`, `show/log`, `hash-object`, both `diff-tree` forms, every `ls-files`, status, diff, check-ignore, worktree list/add/remove, reset, add, and commit. No task or phase is exempt.

Exact byte caps are part of the contract, not caller-selected defaults:

- OID stdout 41 bytes, stderr 0;
- Git version stdout 256 bytes, stderr 0;
- subject stdout 4,096 bytes, stderr 0;
- raw blob stdout 8,388,608 bytes, stderr 0;
- path-list, index-entry, status, name-status, and worktree stdout 16,777,216 bytes, stderr 0;
- exit-only stdout/stderr 0;
- mutation stdout and stderr 4,194,304 bytes each, with both streams captured as non-authority diagnostics;
- any larger stream is overflow and triggers the job-tree termination contract.

### Transport contract controls

Before any M5 CreateNew, the P5 controller runs the same production interfaces under clean and poisoned parent environments. Positive controls include the fixed SHA-256 of ASCII `abc`, P4/S4 current file seals, exact P4 topology, and the v3 NUL-framed tracked inventory.

The v3 positive inventory has exactly 1,081 records. Its non-ASCII subset is exactly these eight paths:

```text
TapTap_v3.5_更新公告.md
TapTap_v3.6_更新公告.md
TapTap_v3.7_更新公告.md
TapTap_v3.8_更新公告.md
TapTap_v3.9_更新公告.md
TapTap_回归声明.md
docs/原声带歌单.md
事件时间线审计报告.md
```

The exact raw `ls-files --cached -z` control is frozen here as 36,261 bytes with SHA-256 `8ED751106E8A82CE35FA60C99D3114C039C75B768A8E3B8D6B75DD7836E976DA`, exit 0, and empty stderr. P5 plan review independently recomputes rather than rebaselining those values. The plan's controls prove all eight paths, the full 1,081-record count, raw-byte seal, strict UTF-8 round trip, preserved raw order, and Ordinal/case-fold set contracts.

Required negative controls include line-oriented quoted/octal output, invalid UTF-8, BOM, missing final NUL, double NUL, duplicate/case-fold path, absolute/drive/traversal path, valid stdout with disallowed exit, exit 0 with forbidden stderr, malformed OID/status/name-status/worktree records, stdout/stderr cap overflow, poisoned `PSModulePath`, poisoned repository-selection/config/pager variables, poisoned PATH after executable resolution, mutated/missing Git executable or one of its five non-system DLLs, unexpected PE import, repository config/exclude/attribute/alternate drift, and root `.git`/admin `commondir`/admin `gitdir` redirection, reparse, case-fold alias, seal, or bidirectional-relation drift. Disposable-worktree controls also reject a pre-existing target/admin path, a Git-selected suffixed admin name, an unexpected common directory, and incomplete root/admin removal. Process-boundary controls additionally cover `CreateProcessW` failure, admission/query failure, a root that exits while a descendant closes stdio and remains alive, any short-lived child process, a descendant that retains a pipe handle, implicit worktree checkout child, filter/hook/maintenance child, forced timeout, forced capture overflow, abort-time `TerminateJobObject`, five-second root/reader/`ActiveProcesses=0` reproof, and exact three-handle inheritance. No control can pass by merely closing the final Job handle.

Argv controls round-trip through `CommandLineToArgvW`: empty string, space, tab, quote, Chinese text, zero through eight backslashes before a quote and at end, 32,767-code-unit boundary, rejected overlength, NUL, and isolated surrogate. Environment controls cover mixed-case duplicate/poisoned `GIT_*`, PATH/MSYS variables, exact fixed-key uniqueness, OrdinalIgnoreCase order, and double-NUL termination. Dual writers exceed the anonymous-pipe buffer concurrently; exact cap passes, cap-plus-one and declared zero cap fail without deadlock or parser entry.

The release-font control independently mutates one source catalog path, one source byte, one copied-runtime path, one copied-runtime byte, the `fontTools` version/`METADATA`/`RECORD`, each schema-2 payload field/type/order/base64 relation, pre/post font seal, backup state, runtime residue, and private-desktop timeout. Every single mutation must reject without creating a receipt; the clean control must leave the runtime absent and preserve the 9/14/56 counts.

Static review treats any remaining direct Git adapter call, `$LASTEXITCODE`, `Get-FileHash`, runtime/executable-body `Add-Type` or compiler invocation outside the one explicit precompiled-runner load, disk assembly load, unreviewed `ProcessStartInfo`/`Process.Start`/`Start-Process`, `AssignProcessToJobObject`, `BaseStream`, `ReadToEnd`, `WaitForExit`, unbounded line reader/pipe, parse-before-exit, incomplete argv quoting, `worktree add` without `--no-checkout`, mutation without post-reproof, or retry branch as Critical. The only compiler exceptions are the one offline nonauthority seed build and the two offline preapproval deterministic A/B attestation builds under the exact build fence above; compiler tokens in P5 executable bodies/loader are zero. Source/PE/AST controls require the host-created outer root and every adapter-created profile root to use exactly HANDLE_LIST/JOB_LIST/MITIGATION attributes and zero `CREATE_BREAKAWAY_FROM_JOB`; a closed-table descendant created inside a sealed profile may use its frozen native launcher but must be admitted by the profile's `DEBUG_PROCESS` event gate and remain in both outer and inner Jobs. The outer Job is exactly kill-on-close with no active-process/breakaway/UI limits, every inner Job is kill-on-close with no breakaway/UI limit, and Git and Opus additionally enforce active-process-one plus final `TotalProcesses=1`. Production source has zero `JOB_OBJECT_LIMIT_BREAKAWAY_OK`, `JOB_OBJECT_LIMIT_SILENT_BREAKAWAY_OK`, or breakaway creation flag outside named negative-control literals. Adapter-created roots require exact three-handle inheritance, `EXTENDED_STARTUPINFO_PRESENT`, exact six-element WinPS argv where applicable, debug/loaded-module validation where specified, staged inner/outer abort proofs, outer whole-tree `ActiveProcesses=0`, and no unclassified process path.

For static compiler/process counting, the preceding prohibition explicitly excludes one and only one offline seed path containing `ProcessStartInfo`, `Process.Start`, the initial finite `WaitForExit(timeout)`, and, only on timeout, one root `Kill` plus one finite post-kill `WaitForExit`. AST controls require one start, exactly two finite wait call sites with the second dominated by the failed first wait and Kill, zero parameterless wait, and those tokens nowhere else. There are exactly three compiler invocations before approval: one nonauthority seed plus authoritative A/B. Runtime, loader, controller-action, and Task bodies contain zero compiler or `Add-Type` invocation.

## Recovery v5 namespace and runtime contracts

Except for L5, S5, and P5, every new persistent v5 runtime leaf is inside:

`.superpowers/sdd/terminal-collapse-ending/recovery-v5/`

The fixed core paths mirror the approved v4 layout with `v5` substituted: M5, admission, RED/GREEN, generator/observer attempt and process directories, states, fixture/log evidence, mother, baseline, Task 1 completion, and later rules evidence. Four fresh temporary roots likewise use unique fixed v5 generator/observer worktree and SaveDir paths. Every v4 path remains absent and is forbidden as a fallback or cleanup target.

### Admission, RED/GREEN, and one-shot execution

- Task 1 admission stays schema 1 with the same exact 10 fields and max/retry values, but binds L5/P5/M5 and the v5 path.
- Admission is CreateNew/Flush/strict-reread/read-only in its dedicated authenticated publisher target before the first Task 1 worker/PRE_PATCH target. After a non-following absent-root/ordinary-ancestor proof, the publisher calls the audited `CreateDirectoryW` exactly once on the fixed admission directory and accepts only native success; `ERROR_ALREADY_EXISTS`, another error, a competing creation, or post-create identity/reparse mismatch is terminal and the directory is never adopted. Launching that publisher before this atomic call succeeds does not consume the opportunity; successful directory creation consumes it, and any later leaf/write/flush/reread/read-only failure is terminal without rollback, delete/recreate, alternate directory, or retry. The admission directory itself is the single Task 1 opportunity.
- RED/GREEN retain schema 4 and the exact eight top-level fields `schema_version,verdict,fixture_gate,stream_gate,json_real_gate,inputs,mutations,created_utc`.
- The JSON-real 8-positive/18-negative gate, exact-42 mutation names/order/count, authenticated P5 fixture appendix, synthetic stream controls, bounded AST process, non-following inventories, bounded AppData observations, and private-desktop envelope remain mandatory.
- The sole old-runtime parse exception remains the M5-directed physical v2 generator state used by the Decimal/finite-Double positive control. Other legacy/v2/v3 leaves are stream-hash-only.
- Generator attempt/completion remain schema 3 with exact 19/43 fields; observer attempt/completion remain schema 3 with exact 20/42 fields. Every record directly binds the v5 admission SHA.
- Generator and observer are each invoked exactly once. A missing generator completion forbids observer; a missing observer completion forbids mother.
- Source is only `fresh_generator_v5`; legacy/v2/v3/v4 cannot be source, candidate, fallback, replay input, or Opus input.

### Durable leaves and Task 1 completion

The 27 new durable leaves, excluding Task 1 completion itself, are:

- outside `recovery-v5/`: L5, S5, P5;
- inside `recovery-v5/`: M5, admission, RED, GREEN, nine generator leaves, nine observer leaves, one mother, and one baseline.

Before Task 1 completion, `recovery-v5/` has exactly 24 leaves and six directories. After completion it has exactly 25 leaves and six directories. The directories are exactly `task1-admission`, `generator-attempt`, `generator-process`, `observer-attempt`, `observer-process`, and `mother`; `rules/` remains absent. Hidden/system extras, reparse points, unexpected directories/leaves, and case-fold aliases fail.

Task 1 completion is schema 5 with the same exact 16 ordered top-level fields:

`schema_version,verdict,approval,task1_admission,predecessor,baseline_game_tree,full_selftest,version_probe,generator,observer,mother,artifact_count,artifacts,cleanup,finished_utc,lineage_status`

Changes from v4:

- `lineage_status="fresh_v5_only"`;
- approval binds L5/P5/S5;
- predecessor has exact fields `manifest_path,manifest_bytes,manifest_sha256,artifact_count,catalog_bytes,catalog_sha256,terminal_failure,controller_failure,source_inventories`;
- generator source is `fresh_generator_v5`;
- artifact count is exactly `126 + 27 = 153`.

The other nested schemas remain exact: admission 13 fields, generator 28, observer 17, full-selftest 8, version-probe 6, mother 4, cleanup 4, and artifact rows 3. Completion uses CreateNew/strict UTF-8/one LF/Flush/strict reread/read-only, never overwrite. The 153-row union is independently rebuilt before publication, after strict reread, and after cleanup; completion excludes itself.

The unique success sequence is admission → RED → fresh generator worktree/patch → GREEN → generator ledger/run/completion → fresh observer worktree/patch → observer ledger/run/completion → mother → fresh cleanup reread → delete only four v5 temporary paths → baseline → 153-union → Task 1 completion.

Cleanup derives four paths only from fresh strict completion rereads, exact-compares a hard allowlist, proves process/registration/reparse state, performs exactly two worktree removes and two SaveDir removals, and never performs global `git worktree prune`. It never touches any v1/v2/v3/v4 path or the AppData observation roots. After material deletion, the executor reports each exact resolved path and that the deletion is not recoverable from this workflow.

## Task 2, Task 3, and the post-selection boundary

- Task 2's first project leaf is L5. It then strict-reads Task 1 schema 5 and rehashes exact 153 current artifacts before RED.
- R5 is P5's direct child with the exact subject and three game paths.
- Task 2 remains exactly nine invocations in this order: `rules-red,rules-green,catalog-green,balance-green,winter-invariance-green,missing-portraits-green,narration-overlap-green,show-before-green,lint-green`. Each invocation has one schema-1 receipt with the exact ordered 14 fields `schema_version,name,kind,expected,actual,verdict,helper_evidence_dir,helper_artifacts,helper_result,runner_or_scanner_evidence_dir,direct_evidence,source_evidence,assertions,created_utc`; the union remains exactly 56 artifacts.
- Task 2 completion is schema 5 with these exact 16 ordered top-level fields: `schema_version,verdict,approved_plan_lock_sha256,task1_completion_path,task1_completion_sha256,approved_plan_commit,approved_spec_commit,rules_commit,rules_parent_commit,rules_subject,rules_paths,invocation_count,invocations,artifact_count,artifacts,finished_utc`. It binds P5/S5/R5, the Task 1 schema-5 seal, nine receipts, and 56 artifacts, and uses CreateNew/strict UTF-8/one LF/Flush/strict reread/read-only.
- The combined canon/show gate, approved copy provenance, exact mirror unregister, no global prune, and metadata-only excluded-cache policy remain unchanged.
- The single R5 commit uses the reviewed release-font gate plus the explicit `--no-verify` boundary above and must still contain exactly three paths; no pre-commit hook executes.
- Task 3 validates L5, the complete `P2→S3→P3→S4→P4→S5→P5→R5` chain, Task 1 schema 5/153, and Task 2 schema 5/9/14/56 before creating roots and before each of three Opus calls.
- Task 3 retains fixed launcher/module pre/post seals, hardened copy/run namespaces, strict summary/metadata/result readers, CreateNew read-only blind map, and fresh-only A/B/C handoff. Recovery v5 stops after that handoff: it records no selection, creates no selected-copy plan, and launches no replay.
- Phase B is deliberately outside S5/P5. Only after the user selects A/B/C may a new append-only, independently reviewed spec/plan/lock lineage bind the selected result SHA, exact blind-map SHA, v5 mother, replay body, and first-leaf authority order. That future lineage must make its selected-copy-specific plan the authenticated source; it may not reuse a hidden P5 body, accept an ambient selection, or describe P5's Task-1/Task-2-only vector as sufficient.
- No legacy/v2/v3/v4 candidate, fixture, save, report, or mutable summary becomes source or fallback.

## Failure and authorization boundary

- S5/P5 design and review do not create M5/L5 and do not execute Task 0 or Task 1.
- M5 creation, independent M5 review, L5 creation, independent L5 review, Task 0, and Task 1 are distinct actions.
- A transport or controller exception before the atomic M5 root-creation boundary preserves the absent namespace and stops under the literal-transport retry rules above. Successful `CreateDirectoryW(recovery-v5)` consumes M5 publication; any subsequent M5 write/flush/reread/freeze failure preserves that root and is terminal for v5. No ambient overlay, automatic retry, rollback, delete/recreate, or alternate transport is allowed.
- M5 publication does not authorize L5. L5 publication does not authorize Task 0 or Task 1.
- Task 0 is static and launches no helper, Ren'Py, Python, scanner, observer, Opus, or UI.
- Task 1 admission is globally one-shot. After admission, every failure is terminal and no retry/new GUID/new root is allowed without another append-only spec/plan lineage.
- Any visible window, real input, UI takeover, timeout, launch error, nonzero result, SafetyEnvelope failure, state failure, log failure, inventory failure, or completion failure stops at once.
- Diagnostic success can explain a defect but cannot replace an approved plan step or become authority.

## Acceptance contract

S5/P5:

1. exact direct-parent/single-path topology and unchanged game tree;
2. physical S5/P5 bytes/hash equal raw Git blobs;
3. P5 is self-contained and contains no v4 shorthand or missing cross-scope definitions;
4. every WinPS 5.1 fence parses; embedded Python AST parses;
5. one .NET hash seam and one Git byte seam; zero `Get-FileHash`, direct Git adapter, `$LASTEXITCODE`, line-oriented path parsing, unbounded waits, or retry branches;
6. literal host-to-WinPS body transport, the eight Chinese-path control, framing mutations, poisoned environments, and timeout/kill contracts pass;
7. Git executable plus five-DLL closure, repository-local config/attributes/alternates authority, linked-worktree `.git`/`commondir`/`gitdir` identity and leases, exact-admin `--no-checkout` worktree transitions, exact-one-process success, and post-mutation reproof pass;
8. independent Standards, Spec, and executable-plan reviews return C0/I0.

M5/L5/Task 0:

1. M5 schema 4/20, exact 126 artifacts, 27,190-byte catalog, fixed SHA;
2. exact v3 terminal failure, v4 controller failure, and 8/61, 12/0, 1/0 inventories;
3. M4/L4/recovery-v4/runtime remain absent;
4. L5 schema 5/41 and exact immediate-vs-last-sealed lineage;
5. Task 0 proves v5 admission/runtime absent and dynamic launch count 0;
6. independent reviewers return exact physical M5/L5 hashes out of band.

Task 1:

1. one admission, one generator, one observer;
2. unchanged JSON-real 8+18 and exact-42 gates;
3. runtime schemas 19/43 and 20/42, admission-linked;
4. synthetic P5 stream controls and sole v2-state parse exception;
5. exact 24→25 leaves/six directories;
6. four-path-only cleanup;
7. schema-5 completion with exact 153 artifacts and `fresh_v5_only`.

Downstream:

1. Task 2 schema 5 with exact 9/14/56 and exact R5 commit;
2. Task 3 three fresh Opus calls, each preceded by full authority reproof and each with `CLAUDE_CODE_MAX_RETRIES=0`, zero `system/api_retry` events, and no retry;
3. P5 contains zero Phase B body/vector/branch, and Recovery v5 stops after the fresh A/B/C handoff pending a new post-selection authority lineage;
4. no failed-lineage source, fallback, or candidate probe.

## Asset and package impact

This recovery design changes governance documents and future execution procedure only. It requires no new or modified art, music, sound effects, animation, UI, fonts, or game package content. Suitable existing assets remain untouched, and design-stage package-size impact is 0 bytes.

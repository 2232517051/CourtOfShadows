# Terminal Collapse Ending Phase A Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Freeze a real pre-change final-tactics save, implement the route-aware terminal-collapse rule with focused regression coverage, and present three verified isolated Claude Opus 4.6 copy bundles for blind user selection before any visible finale prose changes.

**Architecture:** `game/difficulty.rpy` remains the sole pure source of finale routes, terminal-collapse classification, and reachable battle outcomes; `game/balance.rpy` consumes that source without inventing reachability; `game/test_game.rpy` locks the pure result graph and legacy-safe wrappers. A separate ignored evidence lane preserves the real old save and three raw model outputs. This phase deliberately stops before `game/chapter5.rpy` or `game/endings_expansion.rpy` changes; after the user selects one raw bundle, a second exact-literal plan will integrate runtime guards, death copy, save migration checks, and final release gates.

**Tech Stack:** Ren'Py 8.5.2 / Python 3, Ren'Py testsuites, Windows PowerShell 5.1, Git, Claude Code locked to `claude-opus-4-6` through the verified local launcher.

## Global Constraints

- The approved written design is `docs/superpowers/specs/2026-08-11-terminal-collapse-ending-design.md`, physical SHA-256 `F7C833952D0F783A922FFF18F6F0A2B9F44BA8F1BF31520917FA6B1237B1A232`, committed in its final host-teardown form at `98ff5ca351806732f435b977c7b3b445d586bf6b`. Its exact history is `98ff5ca` (dedicated-host teardown binding) -> `51d089f` (catastrophic cleanup) -> `babfcb9` (monitor lifetime) -> `bdebe79` (coverage-v2 contract) -> `3d67be6` (headless Phase A plan) -> `22ce7cf` (headless legacy-save specification) -> `168c3f2` (original Phase A plan) -> `bdad1441` (original design).
- The unrelated untracked plan `docs/superpowers/plans/2026-08-09-winter-interlude-narrative-delivery.md` must remain byte-identical at SHA-256 `0F39B5F5ACE1D4666DD146863CABDF398B031F5666C29AE337CEB89796E4276C`; never stage, edit, delete, or incorporate it.
- In the shared implementation worktree, Phase A may modify exactly `game/difficulty.rpy`, `game/balance.rpy`, and `game/test_game.rpy`. Task 1's generator worktree may carry only one temporary `game/zz_terminal_collapse_legacy_fixture.rpy`; its clean-replay worktree may carry only one distinct state-read-only observer `zz` file that never assigns game state, and neither Task 1 worktree may modify a production script. Each Task 2 test invocation uses a fresh detached mirror whose only source differences are the exact current allowed RED or GREEN files copied byte-for-byte from the shared worktree; its local `game/saves` starts absent and is removed only with that verified task-owned mirror after the run drains. Neither the shared nor disposable worktrees may modify `game/chapter5.rpy`, `game/endings_expansion.rpy`, any visible production prose, persistent ending key, achievement ID, asset, font, store copy, version, or package metadata.
- The intermediate rules commit is not shippable or merge-ready by itself: it intentionally precedes the runtime guard and approved death copy. Do not run Final, build a release, merge, or advertise the player bug as fixed at the Phase A hard stop.
- Generate the old save before the first tracked game-file edit. Generate it from the exact final Phase A plan commit in a disposable detached worktree after proving that commit's `game/` tree is byte-identical to the original design commit. Use a unique external save directory. Never regenerate it from changed code.
- All evidence under `.superpowers/sdd/terminal-collapse-ending/` must be ignored, must never be staged, and must survive through Phase B review. Do not clean or overwrite evidence to obtain a better result.
- Before the plan is executed, the controller creates exactly one ignored, create-new approval lock at `.superpowers/sdd/terminal-collapse-ending/approved-plan-lock.json`, then never modifies or deletes it. Its exact case-sensitive schema is `schema_version=1`, `approved_plan_commit` (lowercase 40-hex), `plan_sha256` (uppercase 64-hex), `spec_commit=98ff5ca351806732f435b977c7b3b445d586bf6b`, and `spec_sha256=F7C833952D0F783A922FFF18F6F0A2B9F44BA8F1BF31520917FA6B1237B1A232`; no sixth property, duplicate property, BOM, invalid UTF-8, or type coercion is allowed. The controller supplies the same physical lock SHA-256 to every fresh Task 0/1/2/3 context out of band as mandatory parameter `$ApprovalLockSha256`; this plan deliberately does not self-embed the eventual plan commit, physical plan hash, or lock hash. Each task's first project action validates the out-of-band hash, exact JSON contract, physical plan hash, raw plan blob at `approved_plan_commit`, and physical/raw committed specification. Task 0, Task 1, and pre-commit Task 2 additionally require `HEAD == approved_plan_commit`; Task 2 later proves its rules commit is the exact direct child; Task 3 repeats that topology before each Opus invocation. Any lock failure is `NEEDS_CONTEXT` with no retry. Every cleanup target must be proven disjoint from the lock, and the lock must remain ignored and byte-identical through Phase B.
- Task 0 does not execute `renpy.exe`, the SDK Python, `renpy.py`, or any other Ren'Py entrypoint. It only verifies the trusted SDK files and exact `renpy/vc_version.py` bytes statically. After the sole full helper self-test has passed and its completion record has been create-new written and `Flush(true)` has returned, Task 1 runs exactly one version probe through the reviewed private-desktop wrapper, with dummy SDL/renderer variables and fixed create-new evidence, and requires exact stdout plus the complete reusable safety/outcome envelope.
- Every Ren'Py engine `test` or `run` launch uses a unique external `SaveDir` and applies the task-specific local `game/saves` preflight. Every `Run-RenPySuite.ps1` host, the post-selftest version probe, and every Task 2 Python scanner must run exactly once through `.superpowers/sdd/terminal-collapse-ending/helpers/Invoke-PrivateDesktopProcess.ps1` on its never-switched private desktop, with process-local `SDL_VIDEODRIVER=dummy`, `SDL_AUDIODRIVER=dummy`, and `RENPY_RENDERER=sw`, and with child `RENPY_PATH_TO_SAVES` removed. The wrapper launches one new noninteractive PowerShell helper host for each invocation, proves its actual process exit, and validates that exit against the C#-persisted `helper_exit_code` and the exact `COMPLETED=0` / `NEEDS_CONTEXT=20` / `TIMEOUT=21` / `LAUNCH_ERROR=22` mapping. A missing, truncated, still-running, catastrophically terminated, or mismatched result is `NEEDS_CONTEXT` with no retry. Every returned reusable result must pass `Assert-PrivateDesktopSafetyEnvelope`; callers then separately require `COMPLETED`, integral non-null `root_exit_code` equal to the declared expected value, zero visible windows, no timeout, and `helper_exit_code=0`. `job_total_processes`, `observed_distinct_process_id_count`, `process_diagnostic_errors`, and the three PID arrays are diagnostic only and never classify or satisfy cleanup. Preserve all helper and runner evidence; any failed envelope or caller gate is `NEEDS_CONTEXT` and must not be retried or replaced with a direct/manual launch.
- Preserve the failed v1 evidence root `E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-private-desktop-selftest-d37d19e4adfc4b5fb3622abcc8a53212` unchanged; its `short-lived-pid-coverage\result.json` SHA-256 is `300515E17B8EDD6B0CD99C268E685DCAE6770BC664B5C28F231F231F03E9F27B`. Contract-only validator/static checks launch no helper child and do not consume the retry. Task 1 Step 3 may run exactly one full result-schema-v2 helper self-test in one new unique evidence root. Any failure stops without another self-test, Ren'Py, generator, observer, or manual fallback.
- No remaining Phase A task and no later Phase B replay may invoke Computer Use, send real mouse/keyboard input, create or focus a window on the user's current or any switchable desktop, or fall back to manual UI. The sole detector-only exception is Task 1 Step 3's short-lived sentinel Form on a never-switched private desktop: the helper must classify it `NEEDS_CONTEXT`, capture `EVENT_OBJECT_SHOW`, and fully drain and clean its Job before the self-test can pass. No Ren'Py generator, observer, suite, or Phase B replay is allowed any visible window even on its private desktop. Those runs use process-local SDL dummy drivers plus a pre-armed process-tree window monitor; any visible window or interaction requirement is `NEEDS_CONTEXT`, not permission to take over the desktop.
- Each numbered task starts a new agent context. Re-establish every path/hash input at the task's first step. Tasks 0, 1, and 3 must each keep one explicit persistent Windows PowerShell 5.1 session open for all of that task's PowerShell fences; no variable is allowed to leak from a previous task.
- The copy stage uses three fresh, mutually isolated Claude Code sessions. Each receives identical prompt bytes, sees no Codex draft or sibling candidate, and is accepted only if the final launcher metadata proves `claude-opus-4-6`. No fallback, retry under another model, synthesis, or Codex polishing is allowed.
- User approval is the only prose-quality gate. Randomize the three verified raw results to neutral labels A/B/C and display them in full without model/order clues. Stop if the user rejects all three or has not selected one.
- After every tracked change, report assets explicitly: art, music, sound effects, animation, and UI are not required in Phase A; package impact is zero because Phase A adds no shipping binary. Font/package measurement is deferred until approved Phase B text exists.

---

## Task 0: Lock the executable starting point

**Files:**

- Read: `docs/superpowers/specs/2026-08-11-terminal-collapse-ending-design.md`
- Preserve: `docs/superpowers/plans/2026-08-09-winter-interlude-narrative-delivery.md`
- Read: `Tools/Run-RenPySuite.ps1`
- Create ignored evidence only under: `.superpowers/sdd/terminal-collapse-ending/`

- [ ] **Step 1: Verify plan topology and exact starting scope**

Run from the repository root:

```powershell
$ErrorActionPreference = 'Stop'
$ProjectRoot = (Resolve-Path -LiteralPath '.').Path
$ThisPlan = 'docs/superpowers/plans/2026-08-11-terminal-collapse-ending-phase-a.md'
$DesignPath = 'docs/superpowers/specs/2026-08-11-terminal-collapse-ending-design.md'
$ApprovalLockPath = Join-Path $ProjectRoot '.superpowers\sdd\terminal-collapse-ending\approved-plan-lock.json'
$ApprovalLockVariable = Get-Variable -Name ApprovalLockSha256 -Scope 0 -ErrorAction SilentlyContinue
if ($null -eq $ApprovalLockVariable -or
    $ApprovalLockVariable.Value -isnot [string] -or
    [string]$ApprovalLockVariable.Value -cnotmatch '^[0-9A-F]{64}$') {
    throw 'NEEDS_CONTEXT: controller did not bind the out-of-band ApprovalLockSha256 parameter.'
}
$ApprovalLockSha256 = [string]$ApprovalLockVariable.Value
$StrictUtf8 = New-Object System.Text.UTF8Encoding($false, $true)
if (-not (Test-Path -LiteralPath $ApprovalLockPath -PathType Leaf)) {
    throw 'NEEDS_CONTEXT: approved-plan lock is missing.'
}
git check-ignore -q -- $ApprovalLockPath
if ($LASTEXITCODE -ne 0) { throw 'NEEDS_CONTEXT: approved-plan lock is not ignored.' }
$ApprovalLockBytes = [IO.File]::ReadAllBytes($ApprovalLockPath)
if ($ApprovalLockBytes.Length -eq 0 -or
    ($ApprovalLockBytes.Length -ge 3 -and $ApprovalLockBytes[0] -eq 0xEF -and
     $ApprovalLockBytes[1] -eq 0xBB -and $ApprovalLockBytes[2] -eq 0xBF)) {
    throw 'NEEDS_CONTEXT: approved-plan lock is empty or has a BOM.'
}
$ApprovalLockText = $StrictUtf8.GetString($ApprovalLockBytes)
if ($ApprovalLockText.Contains([char]0xFFFD)) {
    throw 'NEEDS_CONTEXT: approved-plan lock is not strict UTF-8.'
}
if ((Get-FileHash -LiteralPath $ApprovalLockPath -Algorithm SHA256).Hash -cne $ApprovalLockSha256) {
    throw 'NEEDS_CONTEXT: approved-plan lock does not match the out-of-band hash.'
}
$ApprovalExpectedProperties = @('schema_version', 'approved_plan_commit', 'plan_sha256', 'spec_commit', 'spec_sha256')
$ApprovalRawProperties = @(
    [regex]::Matches($ApprovalLockText, '"([^"\\]+)"\s*:') |
        ForEach-Object { $_.Groups[1].Value }
)
if ($ApprovalRawProperties.Count -ne $ApprovalExpectedProperties.Count -or
    (Compare-Object $ApprovalExpectedProperties $ApprovalRawProperties -CaseSensitive)) {
    throw 'NEEDS_CONTEXT: approved-plan lock has an inexact or duplicate raw property set.'
}
$ApprovalRecord = $ApprovalLockText | ConvertFrom-Json -ErrorAction Stop
$ApprovalActualProperties = @($ApprovalRecord.PSObject.Properties.Name)
if ($ApprovalRecord -isnot [pscustomobject] -or
    $ApprovalActualProperties.Count -ne $ApprovalExpectedProperties.Count -or
    (Compare-Object $ApprovalExpectedProperties $ApprovalActualProperties -CaseSensitive) -or
    $ApprovalRecord.schema_version -isnot [int] -or [int]$ApprovalRecord.schema_version -ne 1 -or
    $ApprovalRecord.approved_plan_commit -isnot [string] -or
    [string]$ApprovalRecord.approved_plan_commit -cnotmatch '^[0-9a-f]{40}$' -or
    $ApprovalRecord.plan_sha256 -isnot [string] -or
    [string]$ApprovalRecord.plan_sha256 -cnotmatch '^[0-9A-F]{64}$' -or
    $ApprovalRecord.spec_commit -isnot [string] -or
    [string]$ApprovalRecord.spec_commit -cne '98ff5ca351806732f435b977c7b3b445d586bf6b' -or
    $ApprovalRecord.spec_sha256 -isnot [string] -or
    [string]$ApprovalRecord.spec_sha256 -cne 'F7C833952D0F783A922FFF18F6F0A2B9F44BA8F1BF31520917FA6B1237B1A232') {
    throw 'NEEDS_CONTEXT: approved-plan lock schema, types, or values are invalid.'
}
if ((Get-FileHash -LiteralPath $ThisPlan -Algorithm SHA256).Hash -cne [string]$ApprovalRecord.plan_sha256) {
    throw 'NEEDS_CONTEXT: physical Phase A plan hash differs from the approval lock.'
}
$PhysicalPlanBlob = (& git hash-object --no-filters -- $ThisPlan).Trim()
$CommittedPlanBlob = (& git rev-parse ([string]$ApprovalRecord.approved_plan_commit + ':' + $ThisPlan)).Trim()
if ($LASTEXITCODE -ne 0 -or $PhysicalPlanBlob -cne $CommittedPlanBlob) {
    throw 'NEEDS_CONTEXT: physical Phase A plan is not the raw approved commit blob.'
}
if ((Get-FileHash -LiteralPath $DesignPath -Algorithm SHA256).Hash -cne [string]$ApprovalRecord.spec_sha256) {
    throw 'NEEDS_CONTEXT: physical specification hash differs from the approval lock.'
}
$PhysicalSpecBlob = (& git hash-object --no-filters -- $DesignPath).Trim()
$CommittedSpecBlob = (& git rev-parse ([string]$ApprovalRecord.spec_commit + ':' + $DesignPath)).Trim()
if ($LASTEXITCODE -ne 0 -or $PhysicalSpecBlob -cne $CommittedSpecBlob) {
    throw 'NEEDS_CONTEXT: physical specification is not the raw approved commit blob.'
}
if ((& git rev-parse HEAD).Trim() -cne [string]$ApprovalRecord.approved_plan_commit) {
    throw 'NEEDS_CONTEXT: Task 0 HEAD is not the approval-locked plan commit.'
}
$OriginalDesignCommit = 'bdad1441d9731fbfac3e1b90654dbe888f354296'
$OriginalPlanCommit = '168c3f2f6440628fc580e6eeb79065d2ae1439a5'
$LegacySaveSpecCommit = '22ce7cf48aa6f9a0062a697d9cbf954881c60245'
$HeadlessPlanCommit = '3d67be6ba5df0ce7df0445988306bc603d3a69e4'
$CoverageContractCommit = 'bdebe79f3411927496df29ea34a0abbc0a13bfad'
$MonitorLifetimeCommit = 'babfcb9372f3005decc7caf5e014511677c9da8c'
$CatastrophicCleanupCommit = '51d089fe76f7be9cc2535f47b6a83db5e006a6e8'
$ApprovedSpecCommit = '98ff5ca351806732f435b977c7b3b445d586bf6b'
$DesignSha256 = 'F7C833952D0F783A922FFF18F6F0A2B9F44BA8F1BF31520917FA6B1237B1A232'
$UnrelatedPlan = 'docs/superpowers/plans/2026-08-09-winter-interlude-narrative-delivery.md'
$UnrelatedSha256 = '0F39B5F5ACE1D4666DD146863CABDF398B031F5666C29AE337CEB89796E4276C'

if ((git log -1 --format=%s) -cne 'docs: plan terminal collapse coverage v2 retry') {
    throw 'HEAD is not the approved Phase A plan commit.'
}
if ((git rev-parse HEAD^) -cne $ApprovedSpecCommit) {
    throw 'Phase A plan parent is not the final approved coverage-v2 specification commit.'
}
$PlanCommitPaths = @(git diff-tree --no-commit-id --name-only -r HEAD)
if ($PlanCommitPaths.Count -ne 1 -or $PlanCommitPaths[0] -cne $ThisPlan) {
    throw 'Phase A plan commit scope is not exactly the plan file.'
}
$ExpectedHistory = @(
    [pscustomobject]@{ Commit = $ApprovedSpecCommit; Parent = $CatastrophicCleanupCommit; Subject = 'docs: bind terminal collapse host teardown contract'; Path = $DesignPath },
    [pscustomobject]@{ Commit = $CatastrophicCleanupCommit; Parent = $MonitorLifetimeCommit; Subject = 'docs: harden terminal collapse catastrophic cleanup'; Path = $DesignPath },
    [pscustomobject]@{ Commit = $MonitorLifetimeCommit; Parent = $CoverageContractCommit; Subject = 'docs: clarify terminal collapse monitor lifetime'; Path = $DesignPath },
    [pscustomobject]@{ Commit = $CoverageContractCommit; Parent = $HeadlessPlanCommit; Subject = 'docs: correct terminal collapse process evidence contract'; Path = $DesignPath },
    [pscustomobject]@{ Commit = $HeadlessPlanCommit; Parent = $LegacySaveSpecCommit; Subject = 'docs: update terminal collapse phase one for headless evidence'; Path = $ThisPlan },
    [pscustomobject]@{ Commit = $LegacySaveSpecCommit; Parent = $OriginalPlanCommit; Subject = 'docs: require headless legacy save evidence'; Path = $DesignPath },
    [pscustomobject]@{ Commit = $OriginalPlanCommit; Parent = $OriginalDesignCommit; Subject = 'docs: plan terminal collapse phase one'; Path = $ThisPlan }
)
foreach ($HistoryEntry in $ExpectedHistory) {
    if ((git log -1 --format=%s $HistoryEntry.Commit) -cne $HistoryEntry.Subject -or
        (git rev-parse ($HistoryEntry.Commit + '^')) -cne $HistoryEntry.Parent) {
        throw ('Approved history topology drifted at ' + $HistoryEntry.Commit)
    }
    $HistoryPaths = @(git diff-tree --no-commit-id --name-only -r $HistoryEntry.Commit)
    if ($HistoryPaths.Count -ne 1 -or $HistoryPaths[0] -cne $HistoryEntry.Path) {
        throw ('Approved history scope drifted at ' + $HistoryEntry.Commit)
    }
}
if ((Get-FileHash -Algorithm SHA256 $DesignPath).Hash -cne $DesignSha256) {
    throw 'Approved design bytes drifted.'
}
$OriginalGameTree = git rev-parse ($OriginalDesignCommit + ':game')
if ($LASTEXITCODE -ne 0) { throw 'Could not resolve the original design game tree.' }
$PlanGameTree = git rev-parse 'HEAD:game'
if ($LASTEXITCODE -ne 0) { throw 'Could not resolve the executable-plan game tree.' }
if ($PlanGameTree -cne $OriginalGameTree) {
    throw 'The executable plan commit does not preserve the original pre-fix game tree.'
}
if ((Get-FileHash -Algorithm SHA256 $UnrelatedPlan).Hash -cne $UnrelatedSha256) {
    throw 'Unrelated narrative-delivery plan drifted.'
}
if (@(git diff --cached --name-only).Count -ne 0) {
    throw 'Index must be empty at Phase A start.'
}
$Status = @(git status --short --untracked-files=all)
if ($Status.Count -ne 1 -or $Status[0] -cne ('?? ' + $UnrelatedPlan)) {
    throw ('Unexpected starting status: ' + ($Status -join '; '))
}
```

Expected: HEAD is the new coverage-v2 plan-only commit whose parent is `98ff5ca`; every commit and parent in the exact chain through `51d089f`, `babfcb9`, `bdebe79`, `3d67be6`, `22ce7cf`, `168c3f2`, and `bdad1441` has the expected one-file scope and subject; the current specification hash is exact; HEAD's `game/` tree object equals the original design commit's pre-fix `game/` tree; the index is empty; and the only status entry is the preserved unrelated plan.

- [ ] **Step 2: Verify the trusted SDK and runner parser before evidence work**

```powershell
$TrustedSdkRoot = 'E:\Projects\renpy-8.5.2-sdk'
$ConfiguredSdkRoot = [Environment]::GetEnvironmentVariable('RENPY_SDK', 'Process')
if (-not [string]::IsNullOrWhiteSpace($ConfiguredSdkRoot) -and
    -not [IO.Path]::GetFullPath($ConfiguredSdkRoot).TrimEnd('\').Equals($TrustedSdkRoot, [StringComparison]::OrdinalIgnoreCase)) {
    throw 'Process RENPY_SDK points somewhere other than the approved RenPy 8.5.2 SDK.'
}
$RenPyExe = Join-Path $TrustedSdkRoot 'renpy.exe'
if (-not (Test-Path -LiteralPath $RenPyExe -PathType Leaf)) {
    throw 'RENPY_SDK does not contain renpy.exe.'
}
$ParserTokens = $null
$ParserErrors = $null
[System.Management.Automation.Language.Parser]::ParseFile(
    (Join-Path $ProjectRoot 'Tools\Run-RenPySuite.ps1'),
    [ref]$ParserTokens,
    [ref]$ParserErrors
) | Out-Null
if ($ParserErrors.Count -ne 0) {
    throw ('Run-RenPySuite.ps1 parse errors: ' + ($ParserErrors.Message -join '; '))
}
# Task 0 is static-only. Do not execute renpy.exe, the SDK Python, renpy.py, or
# any other Ren'Py entrypoint before the sole full helper selftest has passed.
$RenPyConsole = Join-Path $TrustedSdkRoot 'lib\py3-windows-x86_64\python.exe'
$RenPyEntry = Join-Path $TrustedSdkRoot 'renpy.py'
$RenPyVersionFile = Join-Path $TrustedSdkRoot 'renpy\vc_version.py'
foreach ($RequiredSdkFile in @($RenPyConsole, $RenPyEntry, $RenPyVersionFile)) {
    if (-not (Test-Path -LiteralPath $RequiredSdkFile -PathType Leaf)) {
        throw ('Trusted SDK static input is missing: ' + $RequiredSdkFile)
    }
}
if ((Get-Item -LiteralPath $RenPyVersionFile).Length -ne 106 -or
    (Get-FileHash -LiteralPath $RenPyVersionFile -Algorithm SHA256).Hash -cne 'A0DD836920B6EAA68758C1FC6BCF722313152C09F7773654BC565209F545CBE7') {
    throw 'Trusted SDK vc_version.py byte count or hash drifted.'
}
$VersionSource = [IO.File]::ReadAllText($RenPyVersionFile, $StrictUtf8)
$ExpectedVersionSource = "branch = 'fix'`nnightly = False`nofficial = True`nversion = '8.5.2.26010301'`nversion_name = 'In Good Health'`n"
if ($VersionSource -cne $ExpectedVersionSource) {
    throw 'RenPy vc_version.py bytes do not exactly declare the approved official version.'
}
```

Expected: Windows PowerShell parser errors `0`; no Ren'Py entrypoint or child process is launched; `renpy.exe`, the SDK Python, and `renpy.py` exist; and `renpy/vc_version.py` is exactly the fixed-hash 106-byte official `8.5.2.26010301` declaration. Runtime version evidence is deliberately deferred until Task 1, after the sole full helper selftest completion record has been durably flushed.

- [ ] **Step 3: Establish the ignored evidence root without touching tracked scope**

```powershell
$EvidenceRoot = Join-Path $ProjectRoot '.superpowers\sdd\terminal-collapse-ending'
$IgnoreProbe = '.superpowers/sdd/terminal-collapse-ending/ignore-probe.txt'
git check-ignore -q $IgnoreProbe
if ($LASTEXITCODE -ne 0) { throw 'Terminal-collapse evidence root is not ignored.' }
[IO.Directory]::CreateDirectory($EvidenceRoot) | Out-Null
```

Do not stage the directory. Any small human-authored evidence manifest or helper source must be created with `apply_patch`; engine logs, stdout/stderr captures, process-tree/window-monitor reports, binary saves, and launcher outputs may be copied/generated by their owning tools.

---

## Task 1: Preserve a real pre-change final-tactics save

**Files:**

- Create from the committed exact appendix and execute ignored helper: `.superpowers/sdd/terminal-collapse-ending/helpers/PrivateDesktopRunner.cs`
- Create from the committed exact appendix and execute ignored helper: `.superpowers/sdd/terminal-collapse-ending/helpers/Invoke-PrivateDesktopProcess.ps1`
- Create from the committed exact appendix and execute ignored helper: `.superpowers/sdd/terminal-collapse-ending/helpers/Test-PrivateDesktopRunner.ps1`
- Temporary-only create in generator worktree: `game/zz_terminal_collapse_legacy_fixture.rpy`
- Temporary-only create in clean-replay worktree: `game/zz_terminal_collapse_legacy_observer.rpy`
- Preserve ignored binary master: `.superpowers/sdd/terminal-collapse-ending/legacy/mother/1-1-*.save`
- Preserve ignored evidence: `.superpowers/sdd/terminal-collapse-ending/legacy/baseline-evidence.md`
- Preserve ignored machine evidence: `.superpowers/sdd/terminal-collapse-ending/legacy/generator-state.json`, `.superpowers/sdd/terminal-collapse-ending/legacy/observer-state.json`, and the helper-owned evidence directories

This task is fully headless and fail-closed. Do not use Computer Use, `Start-Process`, a manually opened terminal or game window, synthetic desktop input, or a manual fallback. Every Ren'Py invocation, including a testcase invocation, must go through `Invoke-PrivateDesktopProcess`. `NEEDS_CONTEXT`, `TIMEOUT`, `LAUNCH_ERROR`, any visible window, a confirmation/consent screen, or missing evidence stops the task and preserves all new worktrees, save directories, logs, and reports for diagnosis.

For this task, the global local-save isolation rule is a pre-launch rule: `game/saves` must be absent before both runs. After the generator, Ren'Py 8.5.2 `MultiLocation` is expected to create exactly one local `1-1` mirror whose filename and bytes match the external save. After the clean normal-run autoload, a local directory and `persistent` are permitted, but no local `1-1` candidate is permitted.

Three points must be proven by disposable prototypes before their output is trusted: the independent-desktop helper and its visible-descendant detector; Ren'Py 8.5.2's native testcase click/save behavior, including its `MultiLocation` local mirror; and ordinary `run` autoload callback timing. The steps below are those prototypes. A failure is evidence, not permission to change production code or take over the desktop.

- [ ] **Step 0: Validate the immutable approval lock before creating helpers or reading other project inputs**

The controller must provide `$ApprovalLockSha256` out of band when it opens this fresh persistent Windows PowerShell 5.1 session. This is Task 1's first project action. Do not create either helper, inspect the interrupted attempt, or read any other repository/SDK input until this fence passes; keep the same session open for all later Task 1 PowerShell fences:

```powershell
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$ProjectRoot = (Resolve-Path -LiteralPath '.').Path
$ThisPlan = 'docs/superpowers/plans/2026-08-11-terminal-collapse-ending-phase-a.md'
$DesignPath = 'docs/superpowers/specs/2026-08-11-terminal-collapse-ending-design.md'
$ApprovalLockPath = Join-Path $ProjectRoot '.superpowers\sdd\terminal-collapse-ending\approved-plan-lock.json'
$ApprovalLockVariable = Get-Variable -Name ApprovalLockSha256 -Scope 0 -ErrorAction SilentlyContinue
if ($null -eq $ApprovalLockVariable -or $ApprovalLockVariable.Value -isnot [string] -or
    [string]$ApprovalLockVariable.Value -cnotmatch '^[0-9A-F]{64}$') {
    throw 'NEEDS_CONTEXT: Task 1 controller did not bind the out-of-band ApprovalLockSha256 parameter.'
}
$ApprovalLockSha256 = [string]$ApprovalLockVariable.Value
$StrictUtf8 = New-Object System.Text.UTF8Encoding($false, $true)
if (-not (Test-Path -LiteralPath $ApprovalLockPath -PathType Leaf)) { throw 'NEEDS_CONTEXT: approved-plan lock is missing.' }
git check-ignore -q -- $ApprovalLockPath
if ($LASTEXITCODE -ne 0) { throw 'NEEDS_CONTEXT: approved-plan lock is not ignored.' }
$ApprovalLockBytes = [IO.File]::ReadAllBytes($ApprovalLockPath)
if ($ApprovalLockBytes.Length -eq 0 -or
    ($ApprovalLockBytes.Length -ge 3 -and $ApprovalLockBytes[0] -eq 0xEF -and
     $ApprovalLockBytes[1] -eq 0xBB -and $ApprovalLockBytes[2] -eq 0xBF)) {
    throw 'NEEDS_CONTEXT: approved-plan lock is empty or has a BOM.'
}
$ApprovalLockText = $StrictUtf8.GetString($ApprovalLockBytes)
if ($ApprovalLockText.Contains([char]0xFFFD) -or
    (Get-FileHash -LiteralPath $ApprovalLockPath -Algorithm SHA256).Hash -cne $ApprovalLockSha256) {
    throw 'NEEDS_CONTEXT: approved-plan lock UTF-8 or out-of-band hash validation failed.'
}
$ApprovalExpectedProperties = @('schema_version', 'approved_plan_commit', 'plan_sha256', 'spec_commit', 'spec_sha256')
$ApprovalRawProperties = @([regex]::Matches($ApprovalLockText, '"([^"\\]+)"\s*:') | ForEach-Object { $_.Groups[1].Value })
if ($ApprovalRawProperties.Count -ne 5 -or
    (Compare-Object $ApprovalExpectedProperties $ApprovalRawProperties -CaseSensitive)) {
    throw 'NEEDS_CONTEXT: approved-plan lock has an inexact or duplicate raw property set.'
}
$ApprovalRecord = $ApprovalLockText | ConvertFrom-Json -ErrorAction Stop
$ApprovalActualProperties = @($ApprovalRecord.PSObject.Properties.Name)
if ($ApprovalRecord -isnot [pscustomobject] -or $ApprovalActualProperties.Count -ne 5 -or
    (Compare-Object $ApprovalExpectedProperties $ApprovalActualProperties -CaseSensitive) -or
    $ApprovalRecord.schema_version -isnot [int] -or [int]$ApprovalRecord.schema_version -ne 1 -or
    $ApprovalRecord.approved_plan_commit -isnot [string] -or [string]$ApprovalRecord.approved_plan_commit -cnotmatch '^[0-9a-f]{40}$' -or
    $ApprovalRecord.plan_sha256 -isnot [string] -or [string]$ApprovalRecord.plan_sha256 -cnotmatch '^[0-9A-F]{64}$' -or
    $ApprovalRecord.spec_commit -isnot [string] -or [string]$ApprovalRecord.spec_commit -cne '98ff5ca351806732f435b977c7b3b445d586bf6b' -or
    $ApprovalRecord.spec_sha256 -isnot [string] -or [string]$ApprovalRecord.spec_sha256 -cne 'F7C833952D0F783A922FFF18F6F0A2B9F44BA8F1BF31520917FA6B1237B1A232') {
    throw 'NEEDS_CONTEXT: approved-plan lock schema, types, or values are invalid.'
}
if ((Get-FileHash -LiteralPath $ThisPlan -Algorithm SHA256).Hash -cne [string]$ApprovalRecord.plan_sha256 -or
    (& git hash-object --no-filters -- $ThisPlan).Trim() -cne
        (& git rev-parse ([string]$ApprovalRecord.approved_plan_commit + ':' + $ThisPlan)).Trim()) {
    throw 'NEEDS_CONTEXT: physical Phase A plan is not the approval-locked raw commit blob.'
}
if ((Get-FileHash -LiteralPath $DesignPath -Algorithm SHA256).Hash -cne [string]$ApprovalRecord.spec_sha256 -or
    (& git hash-object --no-filters -- $DesignPath).Trim() -cne
        (& git rev-parse ([string]$ApprovalRecord.spec_commit + ':' + $DesignPath)).Trim()) {
    throw 'NEEDS_CONTEXT: physical specification is not the approval-locked raw commit blob.'
}
if ((& git rev-parse HEAD).Trim() -cne [string]$ApprovalRecord.approved_plan_commit) {
    throw 'NEEDS_CONTEXT: Task 1 HEAD is not the approval-locked plan commit.'
}
$ApprovalLockHashAtTask1Start = (Get-FileHash -LiteralPath $ApprovalLockPath -Algorithm SHA256).Hash
```

Only after Step 0 passes, use `apply_patch` to create the three ignored helper files from Appendices A, B, and C of this plan, byte for byte. Do not copy either exploratory `plan-draft` or `independent-draft`, and do not substitute another launcher. Appendices A-C and their fixed SHA-256 values are part of the committed executable plan; a missing file, a pre-existing different file, or a hash mismatch is `NEEDS_CONTEXT`, not permission to regenerate helper code during execution.

- [ ] **Step 1: Re-establish the exact baseline commit, trusted paths, and task-owned temporary root**

Continue in the same approval-validated PowerShell session:

```powershell
$OriginalDesignCommit = 'bdad1441d9731fbfac3e1b90654dbe888f354296'
$ApprovedSpecCommit = '98ff5ca351806732f435b977c7b3b445d586bf6b'
$CatastrophicCleanupCommit = '51d089fe76f7be9cc2535f47b6a83db5e006a6e8'
$MonitorLifetimeCommit = 'babfcb9372f3005decc7caf5e014511677c9da8c'
$CoverageContractCommit = 'bdebe79f3411927496df29ea34a0abbc0a13bfad'
$HeadlessPlanCommit = '3d67be6ba5df0ce7df0445988306bc603d3a69e4'
$LegacySaveSpecCommit = '22ce7cf48aa6f9a0062a697d9cbf954881c60245'
$OriginalPlanCommit = '168c3f2f6440628fc580e6eeb79065d2ae1439a5'
$ExpectedPlanSubject = 'docs: plan terminal collapse coverage v2 retry'
$ExpectedGameTree = 'fa7a398e9d989731b24e3c1642f3e2e33ce846ff'
$DesignSha256 = 'F7C833952D0F783A922FFF18F6F0A2B9F44BA8F1BF31520917FA6B1237B1A232'
$UnrelatedPlan = 'docs/superpowers/plans/2026-08-09-winter-interlude-narrative-delivery.md'
$UnrelatedSha256 = '0F39B5F5ACE1D4666DD146863CABDF398B031F5666C29AE337CEB89796E4276C'
$EvidenceRoot = Join-Path $ProjectRoot '.superpowers\sdd\terminal-collapse-ending'
$HelperRoot = Join-Path $EvidenceRoot 'helpers'
$LegacyRoot = Join-Path $EvidenceRoot 'legacy'
$RunnerSource = Join-Path $HelperRoot 'PrivateDesktopRunner.cs'
$HeadlessWrapper = Join-Path $HelperRoot 'Invoke-PrivateDesktopProcess.ps1'
$HeadlessSelfTest = Join-Path $HelperRoot 'Test-PrivateDesktopRunner.ps1'
$FailedV1SelfTestRoot = 'E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-private-desktop-selftest-d37d19e4adfc4b5fb3622abcc8a53212'
$FailedV1CoverageResult = Join-Path $FailedV1SelfTestRoot 'short-lived-pid-coverage\result.json'
$FailedV1CoverageResultSha256 = '300515E17B8EDD6B0CD99C268E685DCAE6770BC664B5C28F231F231F03E9F27B'
$ExpectedHelperPayloads = [ordered]@{
    'PrivateDesktopRunner.cs' = [pscustomobject]@{ Bytes = 82334; Sha256 = 'E0393DB1E113FDB8C35097978AA73B7D33AFDD5788499002B6423D883DEED4E8' }
    'Invoke-PrivateDesktopProcess.ps1' = [pscustomobject]@{ Bytes = 24229; Sha256 = '73A3F9C43CF994E08F004E0A1266122A3EC5E0EAF065C63E6D9439CF0B0E1880' }
    'Test-PrivateDesktopRunner.ps1' = [pscustomobject]@{ Bytes = 53188; Sha256 = '20198B669F70E51E51F71BD01E6D06D1949D300F43CE9A94FB0190A47D781A15' }
}
$TrustedSdkRoot = 'E:\Projects\renpy-8.5.2-sdk'
$RenPyConsole = Join-Path $TrustedSdkRoot 'lib\py3-windows-x86_64\python.exe'
$RenPyEntry = Join-Path $TrustedSdkRoot 'renpy.py'
$RenPyVersionFile = Join-Path $TrustedSdkRoot 'renpy\vc_version.py'
$VersionProcessEvidence = Join-Path $LegacyRoot 'renpy-version-process'
$Task1CompletionRecord = Join-Path $LegacyRoot 'task1-completion.json'
$ConfiguredSdkRoot = [Environment]::GetEnvironmentVariable('RENPY_SDK', 'Process')
if (-not [string]::IsNullOrWhiteSpace($ConfiguredSdkRoot) -and
    -not [IO.Path]::GetFullPath($ConfiguredSdkRoot).TrimEnd('\').Equals($TrustedSdkRoot, [StringComparison]::OrdinalIgnoreCase)) {
    throw 'Process RENPY_SDK points somewhere other than the approved RenPy 8.5.2 SDK.'
}
$RenPyExe = Join-Path $TrustedSdkRoot 'renpy.exe'
$BaselineCommit = (& git rev-parse HEAD).Trim()

if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($BaselineCommit)) {
    throw 'Could not resolve the executable-plan HEAD.'
}
if ($BaselineCommit -cne [string]$ApprovalRecord.approved_plan_commit) {
    throw 'The dynamic Task 1 baseline does not equal the approval-locked plan commit.'
}
if ((git log -1 --format=%s) -cne $ExpectedPlanSubject) {
    throw 'HEAD is not the approved final Phase A plan commit.'
}
if ((git rev-parse HEAD^) -cne $ApprovedSpecCommit) {
    throw 'The final Phase A plan commit does not directly follow the approved coverage-v2 specification.'
}
$PlanPaths = @(git diff-tree --no-commit-id --name-only -r $BaselineCommit)
if ($PlanPaths.Count -ne 1 -or $PlanPaths[0] -cne $ThisPlan) {
    throw 'The final Phase A plan commit is not plan-only.'
}
if ((Get-FileHash -LiteralPath $DesignPath -Algorithm SHA256).Hash -cne $DesignSha256) {
    throw 'The approved written specification drifted.'
}
$BaselineGameTree = (& git rev-parse ($BaselineCommit + ':game')).Trim()
$OriginalGameTree = (& git rev-parse ($OriginalDesignCommit + ':game')).Trim()
if ($BaselineGameTree -cne $ExpectedGameTree -or $OriginalGameTree -cne $ExpectedGameTree) {
    throw 'The executable-plan game tree is not the original pre-change game tree.'
}
if ((Get-FileHash -LiteralPath $UnrelatedPlan -Algorithm SHA256).Hash -cne $UnrelatedSha256) {
    throw 'The unrelated narrative-delivery plan drifted.'
}
if (@(git diff --cached --name-only).Count -ne 0) { throw 'The shared index is not empty.' }
$SharedStatus = @(git status --short --untracked-files=all)
if ($SharedStatus.Count -ne 1 -or $SharedStatus[0] -cne ('?? ' + $UnrelatedPlan)) {
    throw ('Unexpected shared worktree status: ' + ($SharedStatus -join '; '))
}
foreach ($RequiredPath in @($RenPyExe, $RenPyConsole, $RenPyEntry, $RenPyVersionFile, $RunnerSource, $HeadlessWrapper, $HeadlessSelfTest)) {
    if (-not (Test-Path -LiteralPath $RequiredPath -PathType Leaf)) {
        throw ('Required Task 1 input is missing: ' + $RequiredPath)
    }
}
if ((Get-Item -LiteralPath $RenPyVersionFile).Length -ne 106 -or
    (Get-FileHash -LiteralPath $RenPyVersionFile -Algorithm SHA256).Hash -cne 'A0DD836920B6EAA68758C1FC6BCF722313152C09F7773654BC565209F545CBE7') {
    throw 'Trusted SDK vc_version.py byte count or hash drifted before Task 1.'
}
$VersionSource = [IO.File]::ReadAllText($RenPyVersionFile, $StrictUtf8)
$ExpectedVersionSource = "branch = 'fix'`nnightly = False`nofficial = True`nversion = '8.5.2.26010301'`nversion_name = 'In Good Health'`n"
if ($VersionSource -cne $ExpectedVersionSource) { throw 'Trusted SDK vc_version.py bytes drifted.' }
foreach ($CreateNewTask1Path in @($VersionProcessEvidence, $Task1CompletionRecord)) {
    if (Test-Path -LiteralPath $CreateNewTask1Path) {
        throw ('Task 1 create-new path already exists; do not rerun or overwrite: ' + $CreateNewTask1Path)
    }
}
if (-not (Test-Path -LiteralPath $FailedV1SelfTestRoot -PathType Container) -or
    -not (Test-Path -LiteralPath $FailedV1CoverageResult -PathType Leaf) -or
    (Get-FileHash -LiteralPath $FailedV1CoverageResult -Algorithm SHA256).Hash -cne $FailedV1CoverageResultSha256) {
    throw 'Preserved d37d v1 failure evidence is missing or drifted.'
}
foreach ($HelperName in $ExpectedHelperPayloads.Keys) {
    $HelperPath = Join-Path $HelperRoot $HelperName
    $ExpectedPayload = $ExpectedHelperPayloads[$HelperName]
    $ObservedItem = Get-Item -LiteralPath $HelperPath -ErrorAction Stop
    $ObservedHash = (Get-FileHash -LiteralPath $HelperPath -Algorithm SHA256).Hash
    if ($ObservedItem.Length -ne [long]$ExpectedPayload.Bytes -or
        $ObservedHash -cne [string]$ExpectedPayload.Sha256) {
        throw ('Helper does not match its committed appendix: ' + $HelperName)
    }
}
foreach ($IgnoredPath in @($RunnerSource, $HeadlessWrapper, $HeadlessSelfTest)) {
    git check-ignore -q $IgnoredPath
    if ($LASTEXITCODE -ne 0) { throw ('Helper appendix is not ignored: ' + $IgnoredPath) }
}

function Get-CanonicalPath([string]$Path) {
    return [IO.Path]::GetFullPath($Path).TrimEnd([IO.Path]::DirectorySeparatorChar, [IO.Path]::AltDirectorySeparatorChar)
}
function Test-SameOrChildPath([string]$Candidate, [string]$Parent) {
    $ChildPath = Get-CanonicalPath $Candidate
    $ParentPath = Get-CanonicalPath $Parent
    return $ChildPath.Equals($ParentPath, [StringComparison]::OrdinalIgnoreCase) -or
        $ChildPath.StartsWith($ParentPath + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)
}

$ExplicitTaskTempRoot = [Environment]::GetEnvironmentVariable('TC_TASK_TEMP_ROOT', 'Process')
if (-not [string]::IsNullOrWhiteSpace($ExplicitTaskTempRoot)) {
    $TaskTempRoot = Get-CanonicalPath $ExplicitTaskTempRoot
} elseif (Test-Path -LiteralPath 'E:\' -PathType Container) {
    $TaskTempRoot = 'E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp'
} else {
    throw 'Set TC_TASK_TEMP_ROOT to an explicit repository-external task directory; no E: drive is available.'
}
[IO.Directory]::CreateDirectory($TaskTempRoot) | Out-Null
$TaskTempRoot = (Resolve-Path -LiteralPath $TaskTempRoot).Path
if ((Test-SameOrChildPath $TaskTempRoot $ProjectRoot) -or (Test-SameOrChildPath $ProjectRoot $TaskTempRoot)) {
    throw 'Task temporary root must be outside and must not contain the repository.'
}
$OriginalTempEnvironment = [Environment]::GetEnvironmentVariable('TEMP', 'Process')
$OriginalTmpEnvironment = [Environment]::GetEnvironmentVariable('TMP', 'Process')
$env:TEMP = $TaskTempRoot
$env:TMP = $TaskTempRoot
```

Expected: `$BaselineCommit` is the dynamic SHA of the final plan-only commit, not `bdad1441d9731fbfac3e1b90654dbe888f354296`; both its `game/` tree and the original design's `game/` tree are exactly `fa7a398e9d989731b24e3c1642f3e2e33ce846ff`. The selected temporary root is explicit and repository-external. Do not use `[IO.Path]::GetTempPath()` for a worktree or save path outside the helper's own self-test.

- [ ] **Step 2: Preserve the interrupted attempt, then remove only its exact verified worktree**

The previous UI-based attempt is failed evidence, not a usable legacy save. Preserve its report, external save directory, artifacts, and copied log. Only its exact registered worktree may be removed after all guards pass:

```powershell
$InterruptedWorktree = 'E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-baseline-34e7c2d874ff4075b243e4b5949f7b78'
$InterruptedSaveDir = 'E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-old-save-1f027ab224b74d8890172376314ea3b1'
$InterruptedPid = 90932
$InterruptedCommit = 'bdad1441d9731fbfac3e1b90654dbe888f354296'
$InterruptedLogHash = 'EA0799C53B982E25B8E6E19111EDC2982D5B1225F7793D5562D8E4AA02ABA595'
$InterruptedReport = Join-Path $ProjectRoot '.superpowers\sdd\terminal-collapse-task-1-report-v2.md'
$InterruptedReportExpectedHash = '0312AC00D64A9C43CA5B67A42F0170F411222B8C91962A556EC1AF4B6F674D27'
$InterruptedArchive = Join-Path $LegacyRoot 'interrupted-attempt'
$ExpectedInterruptedFiles = [ordered]@{
    'quick-1-LT1.save' = 'F04B0614CEDFC4E8C7AAEFBDE8EACEEBEF1BB9064CC9CE6831DAAF0B2FA1F4B3'
    'auto-1-LT1.save' = 'CC59436C6D19E518143D4860F9BC83C54694D414678A8B73474289021C39A3B9'
    'auto-2-LT1.save' = '27028A705C441F1EEECB424F3A6FAD7EEDC543F0453A6B36AAAEF90CB7BC54E2'
    'persistent' = '0E810763707C70DF37039BD0DAEB180DAE791C15BD53A650740DAAC38D4A7B99'
}

foreach ($FixedSha in @($InterruptedLogHash, $InterruptedReportExpectedHash) + @($ExpectedInterruptedFiles.Values)) {
    if ([string]$FixedSha -cnotmatch '^[0-9A-F]{64}$') {
        throw ('Malformed fixed interrupted-evidence SHA-256: ' + [string]$FixedSha)
    }
}

if (-not (Test-Path -LiteralPath $InterruptedReport -PathType Leaf)) {
    throw 'Interrupted-attempt report is missing; do not clean its worktree.'
}
if ((Get-FileHash -LiteralPath $InterruptedReport -Algorithm SHA256).Hash -cne $InterruptedReportExpectedHash -or
    (Get-Content -LiteralPath $InterruptedReport -Encoding UTF8 -TotalCount 1) -cne 'STATUS: NEEDS_CONTEXT') {
    throw 'Interrupted-attempt report drifted; do not clean its worktree.'
}
if (-not (Test-Path -LiteralPath $InterruptedSaveDir -PathType Container)) {
    throw 'Interrupted-attempt SaveDir is missing; do not clean its worktree.'
}
$ObservedInterruptedFiles = @(Get-ChildItem -LiteralPath $InterruptedSaveDir -File)
if ($ObservedInterruptedFiles.Count -ne $ExpectedInterruptedFiles.Count) {
    throw 'Interrupted SaveDir file count drifted; preserve everything and stop.'
}
foreach ($Name in $ExpectedInterruptedFiles.Keys) {
    $Path = Join-Path $InterruptedSaveDir $Name
    if (-not (Test-Path -LiteralPath $Path -PathType Leaf) -or
        (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash -cne $ExpectedInterruptedFiles[$Name]) {
        throw ('Interrupted SaveDir evidence drifted: ' + $Name)
    }
}
if (@($ObservedInterruptedFiles | Where-Object { $_.Name -like '1-1-*.save' }).Count -ne 0) {
    throw 'Interrupted attempt unexpectedly contains a page-1/slot-1 save; preserve and investigate.'
}
if (-not (Test-Path -LiteralPath $InterruptedWorktree -PathType Container)) {
    throw 'Expected interrupted worktree is missing; preserve evidence and stop.'
}
if ((git -C $InterruptedWorktree rev-parse HEAD) -cne $InterruptedCommit) {
    throw 'Interrupted worktree commit drifted.'
}
$ExpectedInterruptedStatus = @(' M game/script.rpy', '?? game/zz_terminal_collapse_legacy_fixture.rpy')
$ObservedInterruptedStatus = @(git -C $InterruptedWorktree status --short --untracked-files=all)
if (Compare-Object ($ExpectedInterruptedStatus | Sort-Object) ($ObservedInterruptedStatus | Sort-Object)) {
    throw ('Interrupted worktree status drifted: ' + ($ObservedInterruptedStatus -join '; '))
}
$InterruptedLog = Join-Path $InterruptedWorktree 'log.txt'
if (-not (Test-Path -LiteralPath $InterruptedLog -PathType Leaf) -or
    (Get-FileHash -LiteralPath $InterruptedLog -Algorithm SHA256).Hash -cne $InterruptedLogHash) {
    throw 'Interrupted worktree log drifted.'
}
$RegisteredWorktrees = @(
    git worktree list --porcelain |
        Where-Object { $_.StartsWith('worktree ', [StringComparison]::Ordinal) } |
        ForEach-Object { Get-CanonicalPath $_.Substring(9) }
)
if ($RegisteredWorktrees -notcontains (Get-CanonicalPath $InterruptedWorktree)) {
    throw 'Interrupted worktree is not the exact registered worktree.'
}
if (Get-Process -Id $InterruptedPid -ErrorAction SilentlyContinue) {
    throw 'Interrupted RenPy PID is still alive.'
}
$InterruptedReferences = @(
    Get-CimInstance Win32_Process -ErrorAction Stop | Where-Object {
        ($null -ne $_.ExecutablePath -and $_.ExecutablePath.StartsWith($InterruptedWorktree, [StringComparison]::OrdinalIgnoreCase)) -or
        ($null -ne $_.CommandLine -and $_.CommandLine.IndexOf($InterruptedWorktree, [StringComparison]::OrdinalIgnoreCase) -ge 0)
    }
)
if ($InterruptedReferences.Count -ne 0) {
    throw 'A live process still references the interrupted worktree.'
}
if (Test-Path -LiteralPath $InterruptedArchive) {
    throw 'Interrupted-attempt archive already exists; do not overwrite evidence.'
}
[IO.Directory]::CreateDirectory($InterruptedArchive) | Out-Null
[IO.File]::Copy($InterruptedLog, (Join-Path $InterruptedArchive 'log.txt'), $false)
$InterruptedReportHash = (Get-FileHash -LiteralPath $InterruptedReport -Algorithm SHA256).Hash
if ((Get-FileHash -LiteralPath (Join-Path $InterruptedArchive 'log.txt') -Algorithm SHA256).Hash -cne $InterruptedLogHash) {
    throw 'Interrupted log archive hash mismatch.'
}
git check-ignore -q (Join-Path $InterruptedArchive 'log.txt')
if ($LASTEXITCODE -ne 0) { throw 'Interrupted log archive is not ignored.' }

$ApprovedInterruptedRoot = 'E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp'
if (-not (Test-SameOrChildPath $InterruptedWorktree $ApprovedInterruptedRoot) -or
    (Get-CanonicalPath $InterruptedWorktree).Equals((Get-CanonicalPath $ApprovedInterruptedRoot), [StringComparison]::OrdinalIgnoreCase)) {
    throw 'Refusing to remove an interrupted worktree outside its exact approved root.'
}
git worktree remove --force $InterruptedWorktree
if ($LASTEXITCODE -ne 0) { throw 'Could not remove the exact interrupted worktree.' }
git worktree prune
if (Test-Path -LiteralPath $InterruptedWorktree) {
    throw 'Interrupted worktree remains after guarded removal.'
}
```

Do not delete or alter `$InterruptedSaveDir`, `$InterruptedReport`, `$InterruptedArchive`, or their contents. Record `$InterruptedReportHash` in the final evidence manifest.

- [ ] **Step 3: Parse, compile, and exercise the independent-desktop helper appendices**

The selected helper contract is fixed: dot-source `.superpowers/sdd/terminal-collapse-ending/helpers/Invoke-PrivateDesktopProcess.ps1`, then call `Invoke-PrivateDesktopProcess -FilePath <absolute executable> -ArgumentList <string[]> -WorkingDirectory <absolute directory> -EnvironmentOverrides <hashtable> -TimeoutSeconds <1..86400> -EvidenceDirectory <new absent directory> [-RunnerSource <absolute PrivateDesktopRunner.cs>]`. A `$null` environment value removes that variable from the target child. Each public invocation writes request schema v1 with create-new semantics, starts exactly one new hidden/noninteractive `powershell.exe` helper host, waits boundedly for that actual host process to exit, reads strict UTF-8 `result.json`, and validates the actual host exit against the C#-persisted `helper_exit_code` and classification. Result schema v2 has exactly `schema_version`, `classification`, `detail`, `started`, `root_pid`, `root_exit_code`, `timed_out`, `job_drained`, `desktop_name`, `process_ids`, `new_process_ids`, `active_snapshot_process_ids`, `job_total_processes`, `observed_distinct_process_id_count`, `process_id_accounting_kind`, `process_diagnostic_errors`, `private_desktop_initially_empty`, `monitor_armed_before_create`, `monitor_armed_before_resume`, `monitor_armed_utc`, `process_created_utc`, `resumed_utc`, `root_assigned_to_job_before_resume`, `job_kill_on_close_verified`, `job_breakaway_forbidden`, `job_handle_non_inheritable`, `job_active_processes_final`, `monitor_completed_after_job_drain`, `host_termination_required`, `cleanup_complete`, `cleanup_errors`, `visible_windows`, `started_utc`, `finished_utc`, `elapsed_milliseconds`, `stdout_path`, `stderr_path`, and `helper_exit_code`; legacy `process_coverage_complete` is forbidden. The helper exit mapping is exactly `COMPLETED=0`, `NEEDS_CONTEXT=20`, `TIMEOUT=21`, and `LAUNCH_ERROR=22`; `root_exit_code` is independent and a signaled target exit of `259` remains the legitimate value `259`.

Before `ResumeThread`, a dedicated watcher binds the never-switched private desktop, creates its queue, arms create/show hooks, proves the desktop initially empty, and records `armed <= created <= resumed`. `PROC_THREAD_ATTRIBUTE_JOB_LIST` atomically creates the suspended root inside a no-breakaway Job whose kill-on-close flag has been set and queried back; `IsProcessInJob` proves membership, and the Job handle is non-inheritable, never duplicated, absent from the inherited handle list, and owned only by that helper host. Every visible private-desktop top-level window is `NEEDS_CONTEXT`; transient SHOW remains fail-closed evidence even when later PID or `GetAncestor` resolution fails. Watcher hooks remain active through all Job termination/drain work and stop only after `ActiveProcesses=0` is proven. If drain cannot be proven or watcher join times out, C# persists and flushes a create-new v2 result with `host_termination_required=true`, `classification=NEEDS_CONTEXT`, `helper_exit_code=20`, `cleanup_complete=false`, and `monitor_completed_after_job_drain=false`, preserves Job/completion-port/watcher/desktop ownership, and immediately terminates that one-shot host. The parent rejects such a result as a safety PASS and never retries. `job_total_processes`, all PID arrays, `observed_distinct_process_id_count`, and bounded/deduplicated `process_diagnostic_errors` are type-checked diagnostics only: no count, equality, minimum, or diagnostic-error-content rule may classify the result or satisfy cleanup. Do not substitute a different launcher.

```powershell
$StrictUtf8 = New-Object System.Text.UTF8Encoding($false, $true)
$HelperHashes = [ordered]@{}
foreach ($PowerShellPath in @($HeadlessWrapper, $HeadlessSelfTest)) {
    $Tokens = $null
    $Errors = $null
    [Management.Automation.Language.Parser]::ParseFile($PowerShellPath, [ref]$Tokens, [ref]$Errors) | Out-Null
    if ($Errors.Count -ne 0) {
        throw ('Helper parse failure in ' + $PowerShellPath + ': ' + ($Errors.Message -join '; '))
    }
    $HelperName = Split-Path $PowerShellPath -Leaf
    $HelperHashes[$HelperName] = (Get-FileHash -LiteralPath $PowerShellPath -Algorithm SHA256).Hash
    if ($HelperHashes[$HelperName] -cne [string]$ExpectedHelperPayloads[$HelperName].Sha256 -or
        (Get-Item -LiteralPath $PowerShellPath).Length -ne [long]$ExpectedHelperPayloads[$HelperName].Bytes) {
        throw ('PowerShell helper drifted from its committed appendix: ' + $HelperName)
    }
}
$RunnerText = [IO.File]::ReadAllText($RunnerSource, $StrictUtf8)
if ([string]::IsNullOrWhiteSpace($RunnerText) -or $RunnerText.Contains([char]0xFFFD)) {
    throw 'PrivateDesktopRunner.cs is empty or invalid UTF-8.'
}
$RunnerName = Split-Path $RunnerSource -Leaf
$HelperHashes[$RunnerName] = (Get-FileHash -LiteralPath $RunnerSource -Algorithm SHA256).Hash
if ($HelperHashes[$RunnerName] -cne [string]$ExpectedHelperPayloads[$RunnerName].Sha256 -or
    (Get-Item -LiteralPath $RunnerSource).Length -ne [long]$ExpectedHelperPayloads[$RunnerName].Bytes) {
    throw 'C# helper drifted from its committed appendix.'
}

# Contract-only validation is pure PowerShell/static source inspection. It
# returns before Add-Type, fixture creation, Invoke-PrivateDesktopProcess, or
# any child launch and therefore does not consume the one full-test attempt.
$ContractOnlyOutput = @(& $HeadlessSelfTest -ContractOnly)
if ($ContractOnlyOutput.Count -ne 1) {
    throw 'Contract-only helper validation did not return exactly one result.'
}
$ContractOnlyResult = $ContractOnlyOutput[0]
if ([string]$ContractOnlyResult.verdict -cne 'PASS' -or
    [string]$ContractOnlyResult.mode -cne 'CONTRACT_ONLY' -or
    [int]$ContractOnlyResult.accepted_job_total_processes -ne 66 -or
    [int]$ContractOnlyResult.accepted_observed_distinct_process_id_count -ne 63 -or
    [int]$ContractOnlyResult.rejected_mutations -ne 27 -or
    [int]$ContractOnlyResult.rejected_parent_host_mutations -ne 7) {
    throw 'Contract-only v2 mutation contract failed.'
}
foreach ($ContractPass in @(
    'catastrophic_parent_validation', 'dedicated_host_architecture',
    'atomic_job_assignment', 'root_exit_259_contract',
    'ascii_source_contract', 'static_source_contract'
)) {
    if ([string]$ContractOnlyResult.$ContractPass -cne 'PASS') {
        throw ('Contract-only validation did not prove ' + $ContractPass + '.')
    }
}

# This fixed create-new ledger is written before the only authorized full v2
# self-test. If the session or any case fails, the directory remains and every
# later session must stop instead of choosing a new root or retrying.
$SelfTestAttemptLedger = Join-Path $EvidenceRoot 'helper-v2-full-selftest-attempt'
if (Test-Path -LiteralPath $SelfTestAttemptLedger) {
    throw 'The one full v2 helper self-test attempt has already been consumed; do not retry.'
}
[IO.Directory]::CreateDirectory($SelfTestAttemptLedger) | Out-Null
git check-ignore -q $SelfTestAttemptLedger
if ($LASTEXITCODE -ne 0) { throw 'Full helper self-test attempt ledger is not ignored.' }
$SelfTestAttemptRecord = Join-Path $SelfTestAttemptLedger 'attempt.json'
$SelfTestAttemptPayload = [ordered]@{
    schema_version = 1
    attempt_id = [Guid]::NewGuid().ToString('N')
    started_utc = [DateTimeOffset]::UtcNow.ToString('o')
    helper_sha256 = $HelperHashes
    full_selftest_retry_allowed = $false
}
$SelfTestAttemptBytes = $StrictUtf8.GetBytes(($SelfTestAttemptPayload | ConvertTo-Json -Depth 4) + "`n")
$SelfTestAttemptStream = [IO.File]::Open($SelfTestAttemptRecord, [IO.FileMode]::CreateNew, [IO.FileAccess]::Write, [IO.FileShare]::Read)
try {
    $SelfTestAttemptStream.Write($SelfTestAttemptBytes, 0, $SelfTestAttemptBytes.Length)
    $SelfTestAttemptStream.Flush($true)
} finally {
    $SelfTestAttemptStream.Dispose()
}

try {
    # Sole full invocation. It compiles fixtures and exercises dedicated hosts.
    $SelfTestOutput = @(& $HeadlessSelfTest -IncludeVisibleWindowTest)
} catch {
    throw ('NEEDS_CONTEXT: the sole full v2 helper self-test failed; preserve its attempt ledger/task-temp evidence and do not retry or launch RenPy. ' + $_.Exception.Message)
}
if ($SelfTestOutput.Count -ne 1) {
    throw 'NEEDS_CONTEXT: the sole full v2 helper self-test did not return exactly one result; preserve evidence and do not retry.'
}
$SelfTestResult = $SelfTestOutput[0]
foreach ($SelfTestProperty in @(
    'verdict', 'contract_v2', 'no_window_exit7', 'timeout_tree_drain',
    'short_lived_process_accounting', 'argv_roundtrip', 'environment_isolation',
    'preexisting_evidence_rejection', 'banned_api_scan', 'visible_descendant'
)) {
    if ($null -eq $SelfTestResult.PSObject.Properties[$SelfTestProperty] -or
        [string]$SelfTestResult.$SelfTestProperty -cne 'PASS') {
        throw ('NEEDS_CONTEXT: the sole full v2 helper self-test did not prove ' + $SelfTestProperty + '; do not retry.')
    }
}
$SelfTestRoot = [string]$SelfTestResult.test_root
if ([string]::IsNullOrWhiteSpace($SelfTestRoot) -or
    -not (Test-Path -LiteralPath $SelfTestRoot -PathType Container) -or
    -not (Test-SameOrChildPath $SelfTestRoot $TaskTempRoot)) {
    throw 'NEEDS_CONTEXT: private-desktop self-test evidence is not under the task-owned temporary root; do not retry.'
}
$SelfTestCompletionRecord = Join-Path $SelfTestAttemptLedger 'completion.json'
$SelfTestCompletionPayload = [ordered]@{
    schema_version = 1
    verdict = 'PASS'
    finished_utc = [DateTimeOffset]::UtcNow.ToString('o')
    test_root = $SelfTestRoot
    contract_only = $ContractOnlyResult
    full_selftest = $SelfTestResult
}
$SelfTestCompletionBytes = $StrictUtf8.GetBytes(($SelfTestCompletionPayload | ConvertTo-Json -Depth 8) + "`n")
$SelfTestCompletionStream = [IO.File]::Open($SelfTestCompletionRecord, [IO.FileMode]::CreateNew, [IO.FileAccess]::Write, [IO.FileShare]::Read)
try {
    $SelfTestCompletionStream.Write($SelfTestCompletionBytes, 0, $SelfTestCompletionBytes.Length)
    $SelfTestCompletionStream.Flush($true)
} finally {
    $SelfTestCompletionStream.Dispose()
}
$SelfTestAttemptHash = (Get-FileHash -LiteralPath $SelfTestAttemptRecord -Algorithm SHA256).Hash
$SelfTestCompletionHash = (Get-FileHash -LiteralPath $SelfTestCompletionRecord -Algorithm SHA256).Hash

. $HeadlessWrapper
if (-not (Get-Command Invoke-PrivateDesktopProcess -CommandType Function -ErrorAction SilentlyContinue)) {
    throw 'Invoke-PrivateDesktopProcess was not defined by the selected wrapper.'
}
function New-PrivateRenPyEnvironment([hashtable]$Additional) {
    $Values = @{
        'SDL_VIDEODRIVER' = 'dummy'
        'SDL_AUDIODRIVER' = 'dummy'
        'RENPY_RENDERER' = 'sw'
        'RENPY_NO_REDIRECT_STDIO' = '1'
        'RENPY_PATH_TO_SAVES' = $null
    }
    foreach ($Key in $Additional.Keys) { $Values[$Key] = $Additional[$Key] }
    return $Values
}
function Assert-PrivateDesktopCompletion([object]$Result, [int]$ExpectedRootExitCode, [string]$Context) {
    if ($null -eq $Result) { throw ($Context + ' returned no private-desktop result.') }
    try {
        Assert-PrivateDesktopSafetyEnvelope -Result $Result
    } catch {
        throw ($Context + ' failed the reusable schema-v2 safety envelope: ' + $_.Exception.Message)
    }
    if (-not (Test-PrivateDesktopIntegralValue $Result.root_exit_code)) {
        throw ($Context + ' returned a null or non-integral root_exit_code.')
    }
    if ([string]$Result.classification -cne 'COMPLETED' -or
        [int]$Result.helper_exit_code -ne 0 -or [bool]$Result.timed_out -or
        @($Result.visible_windows).Count -ne 0 -or
        [int64]$Result.root_exit_code -ne [int64]$ExpectedRootExitCode) {
        throw ($Context + ' failed private-desktop completion gates. Classification=' + [string]$Result.classification + '; detail=' + [string]$Result.detail)
    }
    foreach ($EvidencePath in @($Result.stdout_path, $Result.stderr_path)) {
        if (-not [IO.Path]::IsPathRooted([string]$EvidencePath) -or -not (Test-Path -LiteralPath $EvidencePath -PathType Leaf)) {
            throw ($Context + ' has missing process evidence: ' + [string]$EvidencePath)
        }
    }
}

# Task 0 was static-only. This is the sole runtime version probe, and it is
# ordered strictly after completion.json was create-new written and Flush(true)
# returned. It consumes a fixed evidence path and therefore cannot be retried.
$PersistedSelfTestCompletion = [IO.File]::ReadAllText($SelfTestCompletionRecord, $StrictUtf8) | ConvertFrom-Json -ErrorAction Stop
if ([string]$PersistedSelfTestCompletion.verdict -cne 'PASS' -or
    [string]$PersistedSelfTestCompletion.full_selftest.verdict -cne 'PASS') {
    throw 'NEEDS_CONTEXT: durably persisted full-selftest completion did not re-read as PASS; do not run the version probe.'
}
$VersionRun = Invoke-PrivateDesktopProcess `
    -FilePath $RenPyConsole `
    -ArgumentList @($RenPyEntry, '--version') `
    -WorkingDirectory $TrustedSdkRoot `
    -EnvironmentOverrides (New-PrivateRenPyEnvironment @{}) `
    -TimeoutSeconds 30 `
    -EvidenceDirectory $VersionProcessEvidence `
    -RunnerSource $RunnerSource
Assert-PrivateDesktopCompletion $VersionRun 0 'trusted RenPy version probe'
$VersionStdoutPath = [string]$VersionRun.stdout_path
$VersionStderrPath = [string]$VersionRun.stderr_path
$VersionStdoutBytes = [IO.File]::ReadAllBytes($VersionStdoutPath)
$VersionStderrBytes = [IO.File]::ReadAllBytes($VersionStderrPath)
$VersionStdoutText = $StrictUtf8.GetString($VersionStdoutBytes)
$VersionStderrText = $StrictUtf8.GetString($VersionStderrBytes)
if ($VersionStdoutText.Contains([char]0xFFFD) -or $VersionStderrText.Contains([char]0xFFFD) -or
    $VersionStdoutText -cne "Ren'Py 8.5.2.26010301`r`n" -or
    $VersionStderrText -cne '') {
    throw ('NEEDS_CONTEXT: private version probe output was not exact; preserve ' + $VersionProcessEvidence + ' and do not retry.')
}
$VersionArtifactHashes = [ordered]@{}
foreach ($VersionArtifactName in @('request.json', 'stdout.txt', 'stderr.txt', 'result.json')) {
    $VersionArtifactPath = Join-Path $VersionProcessEvidence $VersionArtifactName
    if (-not (Test-Path -LiteralPath $VersionArtifactPath -PathType Leaf)) {
        throw ('NEEDS_CONTEXT: private version probe evidence is incomplete: ' + $VersionArtifactPath)
    }
    git check-ignore -q -- $VersionArtifactPath
    if ($LASTEXITCODE -ne 0) { throw ('NEEDS_CONTEXT: version evidence is not ignored: ' + $VersionArtifactPath) }
    $VersionArtifactHashes[$VersionArtifactName] = (Get-FileHash -LiteralPath $VersionArtifactPath -Algorithm SHA256).Hash
}
```

Expected: both PowerShell appendices parse; the pure contract-only v2 mutation/static suite returns its single PASS without `Add-Type` or a child; then the create-new ledger permits exactly one full self-test, whose nine named behavior fields and overall verdict are `PASS`, including the throwing exit-259 fixture gate and opt-in visible Form sentinel. Only after the flushed completion record re-reads as PASS does one private dummy-driver version probe run; it passes the central envelope and separate classification/helper/no-timeout/zero-window/non-null-integral-root-exit-0 gates and emits exactly `Ren'Py 8.5.2.26010301` plus CRLF on stdout and zero stderr bytes. The full test's unique root, both ledger records, and four fixed version artifacts remain preserved for the sealed completion record. The three physical helper files must remain exactly 82,334 / 24,229 / 53,188 bytes with SHA-256 `E0393DB1E113FDB8C35097978AA73B7D33AFDD5788499002B6423D883DEED4E8`, `73A3F9C43CF994E08F004E0A1266122A3EC5E0EAF065C63E6D9439CF0B0E1880`, and `20198B669F70E51E51F71BD01E6D06D1949D300F43CE9A94FB0190A47D781A15`. Any full-test or version-probe failure preserves the fixed ledger/root/evidence and stops before generator Ren'Py with no retry. If cross-review changes helper source, update the appendices and fixed hashes through a new reviewed plan revision before execution; never accept dynamic schema or source drift.

- [ ] **Step 4: Create a detached generator worktree and add only the native testcase fixture**

```powershell
$GeneratorRoot = Join-Path $TaskTempRoot ('cos-terminal-collapse-generator-' + [Guid]::NewGuid().ToString('N'))
$GeneratorSaveDir = Join-Path $TaskTempRoot ('cos-terminal-collapse-generator-save-' + [Guid]::NewGuid().ToString('N'))
$GeneratorProcessEvidence = Join-Path $LegacyRoot 'generator-process'
$GeneratorStateResult = Join-Path $LegacyRoot 'generator-state.json'
foreach ($AbsentPath in @($GeneratorRoot, $GeneratorSaveDir, $GeneratorProcessEvidence, $GeneratorStateResult)) {
    if (Test-Path -LiteralPath $AbsentPath) { throw ('Create-new generator path already exists: ' + $AbsentPath) }
}
git worktree add --detach $GeneratorRoot $BaselineCommit
if ($LASTEXITCODE -ne 0) { throw 'Could not create the detached generator worktree.' }
if ((git -C $GeneratorRoot rev-parse HEAD) -cne $BaselineCommit -or
    (git -C $GeneratorRoot rev-parse 'HEAD:game') -cne $ExpectedGameTree -or
    @(git -C $GeneratorRoot status --short --untracked-files=all).Count -ne 0) {
    throw 'Detached generator worktree is not the exact clean executable baseline.'
}
$GeneratorLocalSaves = Join-Path $GeneratorRoot 'game\saves'
if (Test-Path -LiteralPath $GeneratorLocalSaves) {
    throw 'Generator game/saves must be absent before the first engine run.'
}
```

With `apply_patch`, create only `$GeneratorRoot\game\zz_terminal_collapse_legacy_fixture.rpy` with exactly:

```renpy
init -1000 python:
    import json as _tc_json
    import os as _tc_os
    import traceback as _tc_traceback

    def _tc_generate_legacy_save():
        r = renpy
        j = _tc_json
        o = _tc_os
        tb = _tc_traceback
        result_path = o.environ.get("TC_GENERATOR_RESULT", "")
        expected_marker = o.environ.get("TC_EXPECTED_MARKER", "")
        expected_commit = o.environ.get("TC_EXPECTED_BASELINE_COMMIT", "")
        expected_game_tree = o.environ.get("TC_EXPECTED_GAME_TREE", "")
        expected_savedir = o.environ.get("TC_EXPECTED_SAVEDIR", "")
        expected_choices = [u"截断补给线——让他们饿三天再打", u"亲自率领前锋出击", u"记住这一切，继续前进"]
        expected_menu = [u"正面强攻，以气势压倒对方", u"采用迂回战术，先攻击敌军侧翼"]

        def canon(value):
            return o.path.normcase(o.path.realpath(o.path.abspath(value)))

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
                r.quit(status=97)
            r.quit(status=code)

        try:
            ctx = r.game.context()
            node = r.game.script.namemap.get(ctx.current, None)
            file_line = r.get_filename_line()
            items = list(r.get_screen_variable("items", screen="choice"))
            raw_captions = [i.caption for i in items if getattr(i, "action", None) is not None]
            display_captions = [r.substitute(value).split("|", 1)[0] for value in raw_captions]
            return_stack = r.get_return_stack()
            state = {
                "intrigue": getattr(r.store, "intrigue", None),
                "power": getattr(r.store, "power", None),
                "iron_prepared": getattr(r.store, "_iron_prepared", None),
            }
            actual = {
                "command": getattr(r.game.args, "command", None),
                "is_in_test": bool(r.is_in_test()),
                "configured_savedir": r.config.savedir,
                "argument_savedir": getattr(r.game.args, "savedir", None),
                "path_to_saves_env_present": "RENPY_PATH_TO_SAVES" in o.environ,
                "context_count": len(r.game.contexts),
                "is_top_context": len(r.game.contexts) == 1 and ctx is r.game.contexts[0],
                "return_stack": [repr(value) for value in return_stack],
                "context_current": repr(ctx.current),
                "node_type": None if node is None else type(node).__name__,
                "node_file": None if node is None else node.filename.replace("\\", "/"),
                "node_line": None if node is None else node.linenumber,
                "filename_line": [file_line[0].replace("\\", "/"), file_line[1]],
                "statement_name": r.get_statement_name(),
                "raw_captions": raw_captions,
                "display_captions": display_captions,
                "state": state,
            }
            checks = {
                "native_test": actual["command"] == "test" and actual["is_in_test"],
                "savedir": bool(expected_savedir) and canon(r.config.savedir) == canon(expected_savedir) and canon(r.game.args.savedir) == canon(expected_savedir),
                "path_to_saves_absent": not actual["path_to_saves_env_present"],
                "top_context": actual["is_top_context"],
                "empty_return_stack": return_stack == [],
                "production_menu_node": node is not None and type(node).__name__ == "Menu" and actual["node_file"].lower().endswith("game/chapter5.rpy") and actual["node_line"] == 2807 and actual["filename_line"] == [actual["node_file"], actual["node_line"]] and actual["statement_name"] == "menu",
                "state": state == {"intrigue": 55, "power": 60, "iron_prepared": True},
                "menu_items": display_captions == expected_menu and u"硬拼——你没有更好的选择了" not in display_captions,
                "marker_inputs": bool(expected_marker) and bool(expected_commit) and bool(expected_game_tree),
            }
            failures = sorted([name for name, passed in checks.items() if not passed])
            if failures:
                finish("FAIL", "pre-save generator assertions failed", {"checks": checks, "failures": failures, "actual": actual}, 41)

            r.store.terminal_collapse_legacy_marker = expected_marker
            metadata = {
                "tc_legacy_schema": 1,
                "tc_legacy_marker": expected_marker,
                "tc_baseline_commit": expected_commit,
                "tc_game_tree": expected_game_tree,
                "tc_choice_path": expected_choices,
                "tc_menu_file": "game/chapter5.rpy",
                "tc_menu_line": 2807,
                "tc_state": state,
            }
            r.save("1-1", include_screenshot=False, extra_json=metadata)
            slot_metadata = r.slot_json("1-1") or {}
            post_save_checks = {
                "can_load": bool(r.can_load("1-1")),
                "store_marker": getattr(r.store, "terminal_collapse_legacy_marker", None) == expected_marker,
                "slot_marker": slot_metadata.get("tc_legacy_schema") == 1 and slot_metadata.get("tc_legacy_marker") == expected_marker,
                "slot_commit": slot_metadata.get("tc_baseline_commit") == expected_commit,
                "slot_game_tree": slot_metadata.get("tc_game_tree") == expected_game_tree,
                "slot_choices": slot_metadata.get("tc_choice_path") == expected_choices,
                "slot_menu": slot_metadata.get("tc_menu_file") == "game/chapter5.rpy" and slot_metadata.get("tc_menu_line") == 2807,
                "slot_state": slot_metadata.get("tc_state") == {"intrigue": 55, "power": 60, "iron_prepared": True},
            }
            post_failures = sorted([name for name, passed in post_save_checks.items() if not passed])
            payload = {"checks": checks, "post_save_checks": post_save_checks, "failures": post_failures, "actual": actual, "slot_metadata": slot_metadata}
            if post_failures:
                finish("FAIL", "post-save generator assertions failed", payload, 42)
            finish("PASS", "native testcase saved the unchanged production final tactics Menu", payload, 0)
        except r.game.QuitException:
            raise
        except Exception:
            finish("FAIL", "generator internal exception", {"traceback": tb.format_exc()}, 43)


testsuite terminal_collapse_legacy_generator:
    before testcase:
        $ _test.timeout = 30.0
        $ persistent.privacy_agreed = True
        $ persistent.tutorial_seen = True
        $ persistent.difficulty = "normal"
        $ power = 56
        $ intrigue = 52
        $ faith = 0
        $ loyalty = 0
        $ wealth = 0
        $ reputation = 0
        $ rel_baron = -1
        $ rel_queen = -1
        $ rel_captain = 20
        $ alliance_baron = False
        $ prince_ally = False
        $ prince_betrayed = False
        $ built_granary = False
        $ ch5_pay_advance_pension = False
        $ marriage_route = False
        $ iron_thorn_controlled = False
        $ baron_supply_intel = False
        $ resist_route = False
        $ iron_war_score = 0
        $ iron_battle_outcome = "decisive"
        $ ending_type = ""

    testcase generate_final_tactics_slot:
        run Start("ending_iron_lord") until screen "say" timeout 4.0
        advance until screen "choice" timeout 30.0
        pause 1.0
        click "截断补给线——让他们饿三天再打"
        pause 0.5
        advance until screen "choice" timeout 30.0
        pause 1.0
        click "亲自率领前锋出击"
        pause 0.5
        advance until screen "choice" timeout 30.0
        pause 1.0
        click "记住这一切，继续前进"
        pause 0.5
        advance until screen "choice" timeout 30.0
        pause 1.0
        assert screen "choice"
        assert eval ((intrigue, power, _iron_prepared) == (55, 60, True))
        $ _tc_generate_legacy_save()
```

This fixture calls the production `Start("ending_iron_lord")`, performs three real engine-native `click` commands against the three real menus, and stops on the production `Menu` at `game/chapter5.rpy:2807`. It neither replaces a production label nor edits a production script. Before running it, prove its worktree scope:

```powershell
$GeneratorFixture = 'game/zz_terminal_collapse_legacy_fixture.rpy'
$GeneratorStatus = @(git -C $GeneratorRoot status --short --untracked-files=all)
if ($GeneratorStatus.Count -ne 1 -or $GeneratorStatus[0] -cne ('?? ' + $GeneratorFixture)) {
    throw ('Generator worktree scope is not exactly its temporary fixture: ' + ($GeneratorStatus -join '; '))
}
```

- [ ] **Step 5: Run the generator privately and bind both `MultiLocation` save copies**

The marker is unique to the exact executable baseline and choice path:

```powershell
$LegacyMarker = 'terminal-collapse-legacy-v1:' + $BaselineCommit + ':supply-vanguard-remember:final-menu'
if (Test-Path -LiteralPath $GeneratorSaveDir) {
    throw 'Generator external SaveDir must be absent before launch.'
}
if (Test-Path -LiteralPath $GeneratorLocalSaves) {
    throw 'Generator game/saves must be absent before launch.'
}
$GeneratorEnvironment = New-PrivateRenPyEnvironment @{
    'TC_GENERATOR_RESULT' = $GeneratorStateResult
    'TC_EXPECTED_MARKER' = $LegacyMarker
    'TC_EXPECTED_BASELINE_COMMIT' = $BaselineCommit
    'TC_EXPECTED_GAME_TREE' = $BaselineGameTree
    'TC_EXPECTED_SAVEDIR' = $GeneratorSaveDir
}
$GeneratorRun = Invoke-PrivateDesktopProcess `
    -FilePath $RenPyExe `
    -ArgumentList @($GeneratorRoot, 'test', 'terminal_collapse_legacy_generator', '--savedir', $GeneratorSaveDir) `
    -WorkingDirectory $GeneratorRoot `
    -EnvironmentOverrides $GeneratorEnvironment `
    -TimeoutSeconds 180 `
    -EvidenceDirectory $GeneratorProcessEvidence `
    -RunnerSource $RunnerSource
Assert-PrivateDesktopCompletion $GeneratorRun 0 'legacy generator'

if (-not (Test-Path -LiteralPath $GeneratorStateResult -PathType Leaf)) {
    throw 'Generator state result is missing.'
}
$GeneratorState = [IO.File]::ReadAllText($GeneratorStateResult, $StrictUtf8) | ConvertFrom-Json -ErrorAction Stop
if ([string]$GeneratorState.verdict -cne 'PASS' -or @($GeneratorState.failures).Count -ne 0) {
    throw ('Generator state assertions failed: ' + [string]$GeneratorState.reason)
}
foreach ($Property in $GeneratorState.checks.PSObject.Properties) {
    if (-not [bool]$Property.Value) { throw ('Generator pre-save check failed: ' + $Property.Name) }
}
foreach ($Property in $GeneratorState.post_save_checks.PSObject.Properties) {
    if (-not [bool]$Property.Value) { throw ('Generator post-save check failed: ' + $Property.Name) }
}
if (-not (Test-Path -LiteralPath $GeneratorSaveDir -PathType Container)) {
    throw 'Generator external SaveDir was not created.'
}
if (-not (Test-Path -LiteralPath $GeneratorLocalSaves -PathType Container)) {
    throw 'RenPy MultiLocation did not create the expected local game/saves mirror.'
}
$ExternalCandidates = @(Get-ChildItem -LiteralPath $GeneratorSaveDir -File | Where-Object { $_.Name -like '1-1-*.save' })
$LocalCandidates = @(Get-ChildItem -LiteralPath $GeneratorLocalSaves -File | Where-Object { $_.Name -like '1-1-*.save' })
if ($ExternalCandidates.Count -ne 1 -or $LocalCandidates.Count -ne 1) {
    throw ('Expected one external and one local page-1/slot-1 save; found external=' + $ExternalCandidates.Count + ', local=' + $LocalCandidates.Count)
}
$ExternalSave = $ExternalCandidates[0]
$LocalSave = $LocalCandidates[0]
if ($ExternalSave.Name -cne $LocalSave.Name -or $ExternalSave.Length -ne $LocalSave.Length) {
    throw 'MultiLocation save filename or byte count differs between external and local copies.'
}
$ExternalHash = (Get-FileHash -LiteralPath $ExternalSave.FullName -Algorithm SHA256).Hash
$LocalHash = (Get-FileHash -LiteralPath $LocalSave.FullName -Algorithm SHA256).Hash
if ($ExternalHash -cne $LocalHash -or
    [Convert]::ToBase64String([IO.File]::ReadAllBytes($ExternalSave.FullName)) -cne [Convert]::ToBase64String([IO.File]::ReadAllBytes($LocalSave.FullName))) {
    throw 'MultiLocation external and local save bytes are not identical.'
}

Add-Type -AssemblyName System.IO.Compression
function Read-RenPySaveJson([string]$SavePath) {
    $Stream = [IO.File]::Open($SavePath, [IO.FileMode]::Open, [IO.FileAccess]::Read, [IO.FileShare]::Read)
    try {
        $Archive = New-Object IO.Compression.ZipArchive -ArgumentList @($Stream, [IO.Compression.ZipArchiveMode]::Read, $false)
        try {
            $Entry = $Archive.GetEntry('json')
            if ($null -eq $Entry) { throw ('Save has no json entry: ' + $SavePath) }
            $EntryStream = $Entry.Open()
            try {
                $Reader = New-Object IO.StreamReader -ArgumentList @($EntryStream, $StrictUtf8, $true, 1024, $true)
                try { $JsonText = $Reader.ReadToEnd() } finally { $Reader.Dispose() }
            } finally {
                $EntryStream.Dispose()
            }
        } finally {
            $Archive.Dispose()
        }
    } finally {
        $Stream.Dispose()
    }
    return ($JsonText | ConvertFrom-Json -ErrorAction Stop)
}
$ExternalMetadata = Read-RenPySaveJson $ExternalSave.FullName
$LocalMetadata = Read-RenPySaveJson $LocalSave.FullName
foreach ($Metadata in @($ExternalMetadata, $LocalMetadata)) {
    if ([int]$Metadata.tc_legacy_schema -ne 1 -or
        [string]$Metadata.tc_legacy_marker -cne $LegacyMarker -or
        [string]$Metadata.tc_baseline_commit -cne $BaselineCommit -or
        [string]$Metadata.tc_game_tree -cne $BaselineGameTree -or
        [string]$Metadata.tc_menu_file -cne 'game/chapter5.rpy' -or [int]$Metadata.tc_menu_line -ne 2807 -or
        [int]$Metadata.tc_state.intrigue -ne 55 -or [int]$Metadata.tc_state.power -ne 60 -or
        -not [bool]$Metadata.tc_state.iron_prepared -or
        (@($Metadata.tc_choice_path) -join "`n") -cne (@('截断补给线——让他们饿三天再打', '亲自率领前锋出击', '记住这一切，继续前进') -join "`n")) {
        throw 'Generator save metadata does not bind the approved legacy state.'
    }
}
$GeneratorLog = Join-Path $GeneratorRoot 'log.txt'
$GeneratorLogEvidence = Join-Path $GeneratorProcessEvidence 'renpy-log.txt'
if (-not (Test-Path -LiteralPath $GeneratorLog -PathType Leaf) -or (Test-Path -LiteralPath $GeneratorLogEvidence)) {
    throw 'Generator log is missing or its create-new evidence path already exists.'
}
[IO.File]::Copy($GeneratorLog, $GeneratorLogEvidence, $false)
$GeneratorLogHash = (Get-FileHash -LiteralPath $GeneratorLogEvidence -Algorithm SHA256).Hash
$GeneratorLogText = [IO.File]::ReadAllText($GeneratorLogEvidence, $StrictUtf8)
$GeneratorStatusMatches = [regex]::Matches($GeneratorLogText, '(?m)^\[rpytest\] Status:\s+([A-Z ]+?)\s*$')
if ($GeneratorStatusMatches.Count -ne 1 -or
    $GeneratorStatusMatches[0].Groups[1].Value.Trim() -cne 'PASSED') {
    throw 'Generator log does not contain exactly one terminal rpytest PASSED status.'
}
```

Stage the external copy, not the local mirror, at the future mother path. The local copy is corroborating evidence only. This is still a writable candidate: do not mark it read-only or call it frozen until the clean normal-run proof passes in Step 7.

```powershell
$MotherDir = Join-Path $LegacyRoot 'mother'
if (Test-Path -LiteralPath $MotherDir) {
    if ($null -ne (Get-ChildItem -LiteralPath $MotherDir -Force | Select-Object -First 1)) {
        throw 'Mother directory is not empty; never overwrite legacy evidence.'
    }
} else {
    [IO.Directory]::CreateDirectory($MotherDir) | Out-Null
}
$MotherSave = Join-Path $MotherDir $ExternalSave.Name
if (Test-Path -LiteralPath $MotherSave) { throw 'Mother save already exists.' }
[IO.File]::Copy($ExternalSave.FullName, $MotherSave, $false)
$MotherHash = (Get-FileHash -LiteralPath $MotherSave -Algorithm SHA256).Hash
$MotherLength = (Get-Item -LiteralPath $MotherSave).Length
if ($MotherHash -cne $ExternalHash -or $MotherLength -ne $ExternalSave.Length) {
    throw 'Candidate mother copy does not match the engine-generated external save.'
}
git check-ignore -q $MotherSave
if ($LASTEXITCODE -ne 0) { throw 'Candidate mother save is not ignored.' }
```

- [ ] **Step 6: Create a second clean baseline worktree with only a state-read-only observer**

```powershell
$CleanRoot = Join-Path $TaskTempRoot ('cos-terminal-collapse-clean-' + [Guid]::NewGuid().ToString('N'))
$CleanSaveDir = Join-Path $TaskTempRoot ('cos-terminal-collapse-clean-save-' + [Guid]::NewGuid().ToString('N'))
$ObserverProcessEvidence = Join-Path $LegacyRoot 'observer-process'
$ObserverStateResult = Join-Path $LegacyRoot 'observer-state.json'
foreach ($AbsentPath in @($CleanRoot, $CleanSaveDir, $ObserverProcessEvidence, $ObserverStateResult)) {
    if (Test-Path -LiteralPath $AbsentPath) { throw ('Create-new observer path already exists: ' + $AbsentPath) }
}
git worktree add --detach $CleanRoot $BaselineCommit
if ($LASTEXITCODE -ne 0) { throw 'Could not create the detached clean-replay worktree.' }
if ((git -C $CleanRoot rev-parse HEAD) -cne $BaselineCommit -or
    (git -C $CleanRoot rev-parse 'HEAD:game') -cne $ExpectedGameTree -or
    @(git -C $CleanRoot status --short --untracked-files=all).Count -ne 0) {
    throw 'Clean-replay worktree is not the exact clean executable baseline.'
}
$CleanLocalSaves = Join-Path $CleanRoot 'game\saves'
if (Test-Path -LiteralPath $CleanLocalSaves) {
    throw 'Clean-replay game/saves must be absent before the normal run.'
}
```

With `apply_patch`, create only `$CleanRoot\game\zz_terminal_collapse_legacy_observer.rpy` with exactly:

```renpy
init -1000 python:
    import json as _tc_json
    import os as _tc_os
    import traceback as _tc_traceback

    def _tc_install_observer():
        r = renpy
        j = _tc_json
        o = _tc_os
        tb = _tc_traceback
        loaded = [False]
        done = [False]
        result_path = o.environ.get("TC_OBSERVER_RESULT", "")
        expected_marker = o.environ.get("TC_EXPECTED_MARKER", "")
        expected_commit = o.environ.get("TC_EXPECTED_BASELINE_COMMIT", "")
        expected_game_tree = o.environ.get("TC_EXPECTED_GAME_TREE", "")
        expected_savedir = o.environ.get("TC_EXPECTED_SAVEDIR", "")
        expected_choices = [u"截断补给线——让他们饿三天再打", u"亲自率领前锋出击", u"记住这一切，继续前进"]
        expected_menu = [u"正面强攻，以气势压倒对方", u"采用迂回战术，先攻击敌军侧翼"]

        def canon(value):
            return o.path.normcase(o.path.realpath(o.path.abspath(value)))

        def finish(verdict, reason, payload, code):
            if done[0]:
                return
            done[0] = True
            payload.update({"schema": 1, "verdict": verdict, "reason": reason})
            try:
                if (not result_path) or (not o.path.isabs(result_path)):
                    raise Exception("TC_OBSERVER_RESULT must be absolute")
                temp = result_path + ".tmp-" + str(o.getpid())
                raw = (j.dumps(payload, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
                with open(temp, "xb") as stream:
                    stream.write(raw)
                    stream.flush()
                    o.fsync(stream.fileno())
                o.rename(temp, result_path)
            except Exception:
                print("TC_OBSERVER_EVIDENCE_WRITE_FAILURE")
                print(tb.format_exc())
                r.quit(status=97)
            r.quit(status=code)

        def after_load():
            loaded[0] = True

        def interact_body():
            blockers = [name for name in ("confirm", "yesno_prompt", "privacy_policy_screen") if r.get_screen(name) is not None]
            if blockers:
                finish("FAIL", "unexpected confirmation or consent interaction", {"loaded": loaded[0], "blocking_screens": blockers}, 42)
            if not loaded[0]:
                return
            if r.get_screen("choice") is None:
                return

            ctx = r.game.context()
            node = r.game.script.namemap.get(ctx.current, None)
            file_line = r.get_filename_line()
            items = list(r.get_screen_variable("items", screen="choice"))
            raw_captions = [i.caption for i in items if getattr(i, "action", None) is not None]
            display_captions = [r.substitute(value).split("|", 1)[0] for value in raw_captions]
            metadata = r.slot_json("1-1") or {}
            return_stack = r.get_return_stack()
            state = {
                "intrigue": getattr(r.store, "intrigue", None),
                "power": getattr(r.store, "power", None),
                "iron_prepared": getattr(r.store, "_iron_prepared", None),
            }
            actual = {
                "command": getattr(r.game.args, "command", None),
                "is_in_test": bool(r.is_in_test()),
                "configured_savedir": r.config.savedir,
                "argument_savedir": getattr(r.game.args, "savedir", None),
                "path_to_saves_env_present": "RENPY_PATH_TO_SAVES" in o.environ,
                "context_count": len(r.game.contexts),
                "is_top_context": len(r.game.contexts) == 1 and ctx is r.game.contexts[0],
                "return_stack": [repr(value) for value in return_stack],
                "context_current": repr(ctx.current),
                "node_type": None if node is None else type(node).__name__,
                "node_file": None if node is None else node.filename.replace("\\", "/"),
                "node_line": None if node is None else node.linenumber,
                "filename_line": [file_line[0].replace("\\", "/"), file_line[1]],
                "statement_name": r.get_statement_name(),
                "raw_captions": raw_captions,
                "display_captions": display_captions,
                "state": state,
                "store_marker": getattr(r.store, "terminal_collapse_legacy_marker", None),
                "slot_metadata": metadata,
            }
            checks = {
                "normal_run": actual["command"] == "run" and not actual["is_in_test"],
                "savedir": bool(expected_savedir) and canon(r.config.savedir) == canon(expected_savedir) and canon(r.game.args.savedir) == canon(expected_savedir),
                "path_to_saves_absent": not actual["path_to_saves_env_present"],
                "top_context": actual["is_top_context"],
                "empty_return_stack": return_stack == [],
                "production_menu_node": node is not None and type(node).__name__ == "Menu" and actual["node_file"].lower().endswith("game/chapter5.rpy") and actual["node_line"] == 2807 and actual["filename_line"] == [actual["node_file"], actual["node_line"]] and actual["statement_name"] == "menu",
                "state": state == {"intrigue": 55, "power": 60, "iron_prepared": True},
                "menu_items": display_captions == expected_menu and u"硬拼——你没有更好的选择了" not in display_captions,
                "store_marker": bool(expected_marker) and actual["store_marker"] == expected_marker,
                "slot_marker": metadata.get("tc_legacy_schema") == 1 and metadata.get("tc_legacy_marker") == expected_marker,
                "slot_commit": bool(expected_commit) and metadata.get("tc_baseline_commit") == expected_commit,
                "slot_game_tree": bool(expected_game_tree) and metadata.get("tc_game_tree") == expected_game_tree,
                "slot_choices": metadata.get("tc_choice_path") == expected_choices,
                "slot_menu": metadata.get("tc_menu_file") == "game/chapter5.rpy" and metadata.get("tc_menu_line") == 2807,
                "slot_state": metadata.get("tc_state") == {"intrigue": 55, "power": 60, "iron_prepared": True},
            }
            failures = sorted([name for name, passed in checks.items() if not passed])
            payload = {"loaded": True, "checks": checks, "failures": failures, "actual": actual}
            if failures:
                finish("FAIL", "observer assertions failed", payload, 41)
            finish("PASS", "clean baseline normal-run autoload reached the production final tactics menu", payload, 0)

        def interact():
            try:
                interact_body()
            except r.game.QuitException:
                raise
            except Exception:
                finish("FAIL", "observer internal exception", {"loaded": loaded[0], "traceback": tb.format_exc()}, 43)

        return after_load, interact

    _tc_after_load_observer, _tc_interact_observer = _tc_install_observer()
    config.after_load_callbacks.append(_tc_after_load_observer)
    config.interact_callbacks.append(_tc_interact_observer)
```

`init -1000` is deliberately later than the SDK's `init -1600` callback-list reset. The observer changes only its closure flags and writes external evidence; it never assigns game state. Prove its worktree scope, then create the unique clean external SaveDir and copy—not move—the read-only mother under its exact engine filename:

```powershell
$ObserverFixture = 'game/zz_terminal_collapse_legacy_observer.rpy'
$CleanStatus = @(git -C $CleanRoot status --short --untracked-files=all)
if ($CleanStatus.Count -ne 1 -or $CleanStatus[0] -cne ('?? ' + $ObserverFixture)) {
    throw ('Clean-replay worktree scope is not exactly its observer: ' + ($CleanStatus -join '; '))
}
if (Test-Path -LiteralPath $CleanSaveDir) { throw 'Clean external SaveDir must start absent.' }
[IO.Directory]::CreateDirectory($CleanSaveDir) | Out-Null
$CleanInputSave = Join-Path $CleanSaveDir (Split-Path $MotherSave -Leaf)
[IO.File]::Copy($MotherSave, $CleanInputSave, $false)
$CleanInputHashBefore = (Get-FileHash -LiteralPath $CleanInputSave -Algorithm SHA256).Hash
if ($CleanInputHashBefore -cne $MotherHash -or (Get-Item -LiteralPath $CleanInputSave).Length -ne $MotherLength) {
    throw 'Clean replay copy does not match the mother.'
}
if (@(Get-ChildItem -LiteralPath $CleanSaveDir -File).Count -ne 1 -or (Test-Path -LiteralPath $CleanLocalSaves)) {
    throw 'Clean replay isolation drifted before normal run.'
}
```

- [ ] **Step 7: Prove an ordinary headless `run` autoloads the frozen slot at the exact production Menu**

```powershell
$ObserverEnvironment = New-PrivateRenPyEnvironment @{
    'RENPY_AUTO_LOAD' = '1-1'
    'TC_OBSERVER_RESULT' = $ObserverStateResult
    'TC_EXPECTED_MARKER' = $LegacyMarker
    'TC_EXPECTED_BASELINE_COMMIT' = $BaselineCommit
    'TC_EXPECTED_GAME_TREE' = $BaselineGameTree
    'TC_EXPECTED_SAVEDIR' = $CleanSaveDir
}
$ObserverRun = Invoke-PrivateDesktopProcess `
    -FilePath $RenPyExe `
    -ArgumentList @($CleanRoot, 'run', '--savedir', $CleanSaveDir) `
    -WorkingDirectory $CleanRoot `
    -EnvironmentOverrides $ObserverEnvironment `
    -TimeoutSeconds 120 `
    -EvidenceDirectory $ObserverProcessEvidence `
    -RunnerSource $RunnerSource
Assert-PrivateDesktopCompletion $ObserverRun 0 'clean normal-run observer'

if (-not (Test-Path -LiteralPath $ObserverStateResult -PathType Leaf)) {
    throw 'Observer state result is missing.'
}
$ObserverState = [IO.File]::ReadAllText($ObserverStateResult, $StrictUtf8) | ConvertFrom-Json -ErrorAction Stop
if ([string]$ObserverState.verdict -cne 'PASS' -or -not [bool]$ObserverState.loaded -or @($ObserverState.failures).Count -ne 0) {
    throw ('Clean normal-run observer failed: ' + [string]$ObserverState.reason)
}
foreach ($Property in $ObserverState.checks.PSObject.Properties) {
    if (-not [bool]$Property.Value) { throw ('Observer check failed: ' + $Property.Name) }
}
if ([string]$ObserverState.actual.command -cne 'run' -or [bool]$ObserverState.actual.is_in_test) {
    throw 'The second proof was not an ordinary RenPy run.'
}
$CleanInputHashAfter = (Get-FileHash -LiteralPath $CleanInputSave -Algorithm SHA256).Hash
if ($CleanInputHashAfter -cne $MotherHash -or (Get-Item -LiteralPath $CleanInputSave).Length -ne $MotherLength) {
    throw 'Normal-run autoload changed the replay save copy.'
}
$CleanExternalCandidates = @(Get-ChildItem -LiteralPath $CleanSaveDir -File | Where-Object { $_.Name -like '1-1-*.save' })
if ($CleanExternalCandidates.Count -ne 1 -or $CleanExternalCandidates[0].Name -cne (Split-Path $MotherSave -Leaf)) {
    throw 'Clean external SaveDir no longer contains exactly the copied legacy slot.'
}
if (Test-Path -LiteralPath $CleanLocalSaves -PathType Container) {
    $CleanLocalCandidates = @(Get-ChildItem -LiteralPath $CleanLocalSaves -File | Where-Object { $_.Name -like '1-1-*.save' })
    if ($CleanLocalCandidates.Count -ne 0) {
        throw 'Ordinary autoload unexpectedly wrote a local page-1/slot-1 candidate.'
    }
} else {
    $CleanLocalCandidates = @()
}
$ObserverLog = Join-Path $CleanRoot 'log.txt'
$ObserverLogEvidence = Join-Path $ObserverProcessEvidence 'renpy-log.txt'
if (-not (Test-Path -LiteralPath $ObserverLog -PathType Leaf) -or (Test-Path -LiteralPath $ObserverLogEvidence)) {
    throw 'Observer log is missing or its create-new evidence path already exists.'
}
[IO.File]::Copy($ObserverLog, $ObserverLogEvidence, $false)
$ObserverLogHash = (Get-FileHash -LiteralPath $ObserverLogEvidence -Algorithm SHA256).Hash

if ((Get-FileHash -LiteralPath $MotherSave -Algorithm SHA256).Hash -cne $MotherHash -or
    (Get-Item -LiteralPath $MotherSave).Length -ne $MotherLength) {
    throw 'Candidate mother drifted during the independent clean replay.'
}
(Get-Item -LiteralPath $MotherSave).IsReadOnly = $true
if (-not (Get-Item -LiteralPath $MotherSave).IsReadOnly) {
    throw 'Mother save did not become read-only after the clean normal-run proof.'
}
```

The post-run local rule is intentionally different from the generator rule. Ren'Py may create `$CleanRoot\game\saves` and a local `persistent` during ordinary startup, but it must not create any local `1-1-*.save`; the only loaded slot remains the exact unchanged external copy. Only now is the ignored mother frozen read-only.

- [ ] **Step 8: Write and re-read the literal baseline evidence before cleanup**

Create `.superpowers/sdd/terminal-collapse-ending/legacy/baseline-evidence.md` with `apply_patch`. It must contain literal, non-placeholder values for every item below:

- `verdict=PASS`, `renpy_version=Ren'Py 8.5.2.26010301`, and the UTC evidence time;
- `baseline_commit=$BaselineCommit`, `baseline_game_tree=fa7a398e9d989731b24e3c1642f3e2e33ce846ff`, `original_design_commit=bdad1441d9731fbfac3e1b90654dbe888f354296`, `legacy_save_spec_commit=22ce7cf48aa6f9a0062a697d9cbf954881c60245`, `approved_spec_commit=98ff5ca351806732f435b977c7b3b445d586bf6b`, and `approved_spec_sha256=F7C833952D0F783A922FFF18F6F0A2B9F44BA8F1BF31520917FA6B1237B1A232`;
- the fixed approval-lock path, `$ApprovalLockHashAtTask1Start`, locked plan commit/hash, and `approval_lock_validation=PASS`;
- all three fixed helper byte counts and SHA-256 values, the preserved d37d v1 root/result SHA-256, the contract-only 66/63 PASS and mutation counts, `$SelfTestAttemptLedger`, `$SelfTestAttemptHash`, `$SelfTestCompletionHash`, `$SelfTestRoot`, the ten full-output `PASS` properties (overall verdict plus nine named behavior fields), and all preserved full-selftest evidence hashes;
- the private version helper's complete schema-v2 hard gates, `root_exit_code=0`, exact stdout text/byte count, empty stderr, `$VersionProcessEvidence`, and the hashes/byte counts of its fixed `request.json`, `stdout.txt`, `stderr.txt`, and `result.json`;
- `$InterruptedReport`, `$InterruptedReportHash`, `$InterruptedSaveDir`, the four preserved interrupted artifact hashes, and `$InterruptedLogHash`;
- `$GeneratorRoot`, `$GeneratorSaveDir`, generator helper `schema_version=2`, `root_pid`, diagnostic `process_ids` / `new_process_ids` / `active_snapshot_process_ids`, nullable diagnostic `job_total_processes`, diagnostic `observed_distinct_process_id_count`, `process_id_accounting_kind=diagnostic_distinct_pid`, bounded `process_diagnostic_errors`, `private_desktop_initially_empty=True`, both monitor-before-create/resume gates and all three ordered timestamps, `root_assigned_to_job_before_resume=True`, `job_kill_on_close_verified=True`, `job_breakaway_forbidden=True`, `job_handle_non_inheritable=True`, `job_active_processes_final=0`, `job_drained=True`, `monitor_completed_after_job_drain=True`, `host_termination_required=False`, `cleanup_complete=True`, `cleanup_errors=0`, `desktop_name`, `root_exit_code=0`, `classification=COMPLETED`, `helper_exit_code=0`, `parent_host_validation=PASS`, `visible_windows=0`, and hashes for its four helper files, state JSON, and copied Ren'Py log; do not describe PID/count diagnostics as complete coverage;
- physical engine filename, logical slot `1-1`, `$MotherLength`, `$MotherHash`, external/local generator filenames, lengths, SHA-256 values, and `multilocation_bytes_equal=PASS`;
- `choice_path=截断补给线——让他们饿三天再打 -> 亲自率领前锋出击 -> 记住这一切，继续前进`;
- `menu_node=game/chapter5.rpy:2807`, `context_count=1`, `return_stack=[]`, `intrigue=55`, `power=60`, `_iron_prepared=True`, both exact visible final choices, and hard-grind absent;
- `$CleanRoot`, `$CleanSaveDir`, observer helper `schema_version=2`, `root_pid`, the same diagnostic-only PID/count/error fields, all private-desktop/create/resume/Job ownership/drain/monitor/cleanup hard gates, `job_active_processes_final=0`, `host_termination_required=False`, `root_exit_code=0`, `classification=COMPLETED`, `helper_exit_code=0`, `parent_host_validation=PASS`, `visible_windows=0`, and hashes for its four helper files, state JSON, and copied Ren'Py log; do not assert diagnostic count equality or completeness;
- `observer_command=run`, `observer_is_in_test=False`, `RENPY_AUTO_LOAD=1-1`, `RENPY_PATH_TO_SAVES=absent`, the store marker, every slot metadata field, `clean_external_hash_unchanged=PASS`, and `clean_local_1-1_count=0`;
- the exact generator/clean worktree and SaveDir paths, followed later by their successful cleanup status. Do not include or copy the save payload itself into Markdown.

Then bind the manifest and all preserved evidence before deleting any successful temporary copy:

```powershell
$BaselineEvidence = Join-Path $LegacyRoot 'baseline-evidence.md'
if (-not (Test-Path -LiteralPath $BaselineEvidence -PathType Leaf)) {
    throw 'Literal baseline evidence manifest is missing.'
}
$BaselineEvidenceText = [IO.File]::ReadAllText($BaselineEvidence, $StrictUtf8)
foreach ($RequiredLiteral in @(
    'verdict=PASS',
    ('baseline_commit=' + $BaselineCommit),
    ('baseline_game_tree=' + $BaselineGameTree),
    ('approved_spec_commit=' + $ApprovedSpecCommit),
    ('selftest_attempt_sha256=' + $SelfTestAttemptHash),
    ('selftest_completion_sha256=' + $SelfTestCompletionHash),
    ('engine_filename=' + (Split-Path $MotherSave -Leaf)),
    ('sha256=' + $MotherHash),
    ('marker=' + $LegacyMarker),
    'observer_command=run',
    "renpy_version=Ren'Py 8.5.2.26010301",
    ('approval_lock_sha256=' + $ApprovalLockHashAtTask1Start),
    ('version_evidence_dir=' + $VersionProcessEvidence),
    'clean_local_1-1_count=0',
    'parent_host_validation=PASS',
    'host_termination_required=False',
    'visible_windows=0'
)) {
    if (-not $BaselineEvidenceText.Contains($RequiredLiteral)) {
        throw ('Baseline evidence omits required literal: ' + $RequiredLiteral)
    }
}
$BaselineEvidenceHash = (Get-FileHash -LiteralPath $BaselineEvidence -Algorithm SHA256).Hash
$GeneratorStateHash = (Get-FileHash -LiteralPath $GeneratorStateResult -Algorithm SHA256).Hash
$ObserverStateHash = (Get-FileHash -LiteralPath $ObserverStateResult -Algorithm SHA256).Hash
foreach ($EvidencePath in @(
    $ApprovalLockPath,
    $BaselineEvidence,
    $SelfTestAttemptRecord,
    $SelfTestCompletionRecord,
    (Join-Path $VersionProcessEvidence 'request.json'),
    (Join-Path $VersionProcessEvidence 'stdout.txt'),
    (Join-Path $VersionProcessEvidence 'stderr.txt'),
    (Join-Path $VersionProcessEvidence 'result.json'),
    $GeneratorStateResult,
    $ObserverStateResult,
    (Join-Path $GeneratorProcessEvidence 'request.json'),
    (Join-Path $GeneratorProcessEvidence 'stdout.txt'),
    (Join-Path $GeneratorProcessEvidence 'stderr.txt'),
    (Join-Path $GeneratorProcessEvidence 'result.json'),
    (Join-Path $ObserverProcessEvidence 'request.json'),
    (Join-Path $ObserverProcessEvidence 'stdout.txt'),
    (Join-Path $ObserverProcessEvidence 'stderr.txt'),
    (Join-Path $ObserverProcessEvidence 'result.json'),
    $GeneratorLogEvidence,
    $ObserverLogEvidence,
    $MotherSave
)) {
    if (-not (Test-Path -LiteralPath $EvidencePath -PathType Leaf)) { throw ('Evidence file is missing: ' + $EvidencePath) }
    git check-ignore -q $EvidencePath
    if ($LASTEXITCODE -ne 0) { throw ('Evidence file is not ignored: ' + $EvidencePath) }
}
if ((Get-FileHash -LiteralPath $MotherSave -Algorithm SHA256).Hash -cne $MotherHash -or
    -not (Get-Item -LiteralPath $MotherSave).IsReadOnly) {
    throw 'Read-only mother drifted before cleanup.'
}
```

- [ ] **Step 9: Clean only successful disposable copies; preserve every failure and all durable evidence**

Do not run this step if any prior check failed or either helper classification was not `COMPLETED`. Do not clean `$SelfTestRoot`, the interrupted SaveDir/report/archive, the read-only mother, either helper evidence directory, either state JSON, either copied log, or the baseline manifest.

```powershell
function Assert-NoProcessReference([string[]]$Paths) {
    $References = @(
        Get-CimInstance Win32_Process -ErrorAction Stop | Where-Object {
            $Process = $_
            @($Paths | Where-Object {
                ($null -ne $Process.ExecutablePath -and $Process.ExecutablePath.StartsWith($_, [StringComparison]::OrdinalIgnoreCase)) -or
                ($null -ne $Process.CommandLine -and $Process.CommandLine.IndexOf($_, [StringComparison]::OrdinalIgnoreCase) -ge 0)
            }).Count -gt 0
        }
    )
    if ($References.Count -ne 0) {
        throw ('A live process still references a cleanup target: ' + (($References | ForEach-Object { $_.ProcessId }) -join ','))
    }
}
function Remove-VerifiedTaskDirectory([string]$Path, [string]$RequiredPrefix) {
    $ResolvedPath = Get-CanonicalPath $Path
    $ResolvedTaskRoot = Get-CanonicalPath $TaskTempRoot
    if (-not (Test-SameOrChildPath $ResolvedPath $ResolvedTaskRoot) -or
        $ResolvedPath.Equals($ResolvedTaskRoot, [StringComparison]::OrdinalIgnoreCase) -or
        -not (Split-Path $ResolvedPath -Leaf).StartsWith($RequiredPrefix, [StringComparison]::Ordinal)) {
        throw ('Refusing recursive removal of unverified path: ' + $ResolvedPath)
    }
    Remove-Item -LiteralPath $ResolvedPath -Recurse -Force
    if (Test-Path -LiteralPath $ResolvedPath) { throw ('Cleanup target remains: ' + $ResolvedPath) }
}

if ([string]$GeneratorRun.classification -cne 'COMPLETED' -or [string]$ObserverRun.classification -cne 'COMPLETED') {
    throw 'Refusing cleanup because both private runs were not successful.'
}
if ((Get-FileHash -LiteralPath $ApprovalLockPath -Algorithm SHA256).Hash -cne $ApprovalLockHashAtTask1Start) {
    throw 'NEEDS_CONTEXT: approval lock drifted before cleanup; preserve all evidence and stop.'
}
foreach ($CleanupTarget in @($GeneratorRoot, $GeneratorSaveDir, $CleanRoot, $CleanSaveDir)) {
    if ((Test-SameOrChildPath $ApprovalLockPath $CleanupTarget) -or
        (Test-SameOrChildPath $CleanupTarget (Split-Path $ApprovalLockPath -Parent))) {
        throw ('NEEDS_CONTEXT: cleanup target is not disjoint from the approval lock: ' + $CleanupTarget)
    }
}
Assert-NoProcessReference @($GeneratorRoot, $GeneratorSaveDir, $CleanRoot, $CleanSaveDir)
foreach ($Worktree in @($GeneratorRoot, $CleanRoot)) {
    if ((git -C $Worktree rev-parse HEAD) -cne $BaselineCommit) { throw ('Cleanup worktree commit drifted: ' + $Worktree) }
}
$GeneratorFinalStatus = @(git -C $GeneratorRoot status --short --untracked-files=all)
$CleanFinalStatus = @(git -C $CleanRoot status --short --untracked-files=all)
if ($GeneratorFinalStatus.Count -ne 1 -or $GeneratorFinalStatus[0] -cne ('?? ' + $GeneratorFixture) -or
    $CleanFinalStatus.Count -ne 1 -or $CleanFinalStatus[0] -cne ('?? ' + $ObserverFixture)) {
    throw 'A disposable worktree changed outside its one permitted zz fixture; preserve and stop.'
}

git worktree remove --force $GeneratorRoot
if ($LASTEXITCODE -ne 0) { throw 'Could not remove verified generator worktree.' }
git worktree remove --force $CleanRoot
if ($LASTEXITCODE -ne 0) { throw 'Could not remove verified clean-replay worktree.' }
git worktree prune
Remove-VerifiedTaskDirectory $GeneratorSaveDir 'cos-terminal-collapse-generator-save-'
Remove-VerifiedTaskDirectory $CleanSaveDir 'cos-terminal-collapse-clean-save-'

if ($null -eq $OriginalTempEnvironment) { Remove-Item Env:TEMP -ErrorAction SilentlyContinue } else { $env:TEMP = $OriginalTempEnvironment }
if ($null -eq $OriginalTmpEnvironment) { Remove-Item Env:TMP -ErrorAction SilentlyContinue } else { $env:TMP = $OriginalTmpEnvironment }
```

Use `apply_patch` once more to append the literal four cleanup results to `baseline-evidence.md`: generator worktree removed, generator SaveDir removed, clean worktree removed, clean SaveDir removed. Re-read it and refresh its recorded manifest SHA-256 if the manifest records its own digest outside itself.

- [ ] **Step 10: Prove the shared repository and durable mother are unchanged**

```powershell
if ((git rev-parse HEAD) -cne $BaselineCommit -or (git rev-parse 'HEAD:game') -cne $ExpectedGameTree) {
    throw 'Shared HEAD or game tree changed during legacy-save generation.'
}
if ((Get-FileHash -LiteralPath $ApprovalLockPath -Algorithm SHA256).Hash -cne $ApprovalLockHashAtTask1Start -or
    $ApprovalLockHashAtTask1Start -cne $ApprovalLockSha256) {
    throw 'Approval lock changed during Task 1.'
}
if (@(git diff --cached --name-only).Count -ne 0) { throw 'Shared index changed during Task 1.' }
$FinalSharedStatus = @(git status --short --untracked-files=all)
if ($FinalSharedStatus.Count -ne 1 -or $FinalSharedStatus[0] -cne ('?? ' + $UnrelatedPlan)) {
    throw ('Unexpected final shared status: ' + ($FinalSharedStatus -join '; '))
}
if ((Get-FileHash -LiteralPath $UnrelatedPlan -Algorithm SHA256).Hash -cne $UnrelatedSha256) {
    throw 'Unrelated narrative-delivery plan changed during Task 1.'
}
if ((Get-FileHash -LiteralPath $MotherSave -Algorithm SHA256).Hash -cne $MotherHash -or
    (Get-Item -LiteralPath $MotherSave).Length -ne $MotherLength -or
    -not (Get-Item -LiteralPath $MotherSave).IsReadOnly) {
    throw 'Durable mother save is no longer the exact read-only engine artifact.'
}
if (-not (Test-Path -LiteralPath $SelfTestRoot -PathType Container) -or
    -not (Test-Path -LiteralPath $SelfTestAttemptRecord -PathType Leaf) -or
    -not (Test-Path -LiteralPath $SelfTestCompletionRecord -PathType Leaf) -or
    (Get-FileHash -LiteralPath $SelfTestAttemptRecord -Algorithm SHA256).Hash -cne $SelfTestAttemptHash -or
    (Get-FileHash -LiteralPath $SelfTestCompletionRecord -Algorithm SHA256).Hash -cne $SelfTestCompletionHash -or
    -not (Test-Path -LiteralPath $InterruptedSaveDir -PathType Container) -or
    -not (Test-Path -LiteralPath $InterruptedReport -PathType Leaf) -or
    -not (Test-Path -LiteralPath $FailedV1CoverageResult -PathType Leaf) -or
    (Get-FileHash -LiteralPath $FailedV1CoverageResult -Algorithm SHA256).Hash -cne $FailedV1CoverageResultSha256) {
    throw 'Required helper or interrupted-attempt evidence was removed.'
}
$FinalBaselineEvidenceHash = (Get-FileHash -LiteralPath $BaselineEvidence -Algorithm SHA256).Hash

# Seal one strict machine-readable Task 1 completion record. Task 2 consumes
# this record directly and never treats baseline-evidence.md as an authority.
$Task1ArtifactPathMap = @{}
function Add-Task1ArtifactPath([string]$Path) {
    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        throw ('Cannot seal missing Task 1 artifact: ' + $Path)
    }
    $FullPath = (Resolve-Path -LiteralPath $Path).Path
    $Task1ArtifactPathMap[$FullPath] = $FullPath
}
foreach ($FixedArtifact in @(
    $ApprovalLockPath, $ThisPlan, $DesignPath,
    $RunnerSource, $HeadlessWrapper, $HeadlessSelfTest,
    $RenPyConsole, $RenPyEntry, $RenPyVersionFile,
    $FailedV1CoverageResult, $SelfTestAttemptRecord, $SelfTestCompletionRecord,
    $InterruptedReport, (Join-Path $InterruptedArchive 'log.txt'),
    $MotherSave, $BaselineEvidence,
    $GeneratorStateResult, $ObserverStateResult,
    (Join-Path $GeneratorProcessEvidence 'request.json'),
    (Join-Path $GeneratorProcessEvidence 'stdout.txt'),
    (Join-Path $GeneratorProcessEvidence 'stderr.txt'),
    (Join-Path $GeneratorProcessEvidence 'result.json'),
    $GeneratorLogEvidence,
    (Join-Path $ObserverProcessEvidence 'request.json'),
    (Join-Path $ObserverProcessEvidence 'stdout.txt'),
    (Join-Path $ObserverProcessEvidence 'stderr.txt'),
    (Join-Path $ObserverProcessEvidence 'result.json'),
    $ObserverLogEvidence,
    (Join-Path $VersionProcessEvidence 'request.json'),
    (Join-Path $VersionProcessEvidence 'stdout.txt'),
    (Join-Path $VersionProcessEvidence 'stderr.txt'),
    (Join-Path $VersionProcessEvidence 'result.json')
)) {
    Add-Task1ArtifactPath $FixedArtifact
}
foreach ($ArtifactDirectory in @($SelfTestRoot, $InterruptedSaveDir)) {
    foreach ($ArtifactFile in @(Get-ChildItem -LiteralPath $ArtifactDirectory -Recurse -File | Sort-Object FullName)) {
        Add-Task1ArtifactPath $ArtifactFile.FullName
    }
}
$Task1ArtifactEntries = @(
    foreach ($ArtifactPath in @($Task1ArtifactPathMap.Keys | Sort-Object)) {
        $ArtifactItem = Get-Item -LiteralPath $ArtifactPath -ErrorAction Stop
        [pscustomobject][ordered]@{
            path = $ArtifactItem.FullName
            bytes = [long]$ArtifactItem.Length
            sha256 = (Get-FileHash -LiteralPath $ArtifactItem.FullName -Algorithm SHA256).Hash
        }
    }
)
if ($Task1ArtifactEntries.Count -lt 30) {
    throw 'Task 1 sealed artifact set is unexpectedly small.'
}
$Task1CompletionPayload = [ordered]@{
    schema_version = 1
    verdict = 'PASS'
    approved_plan_lock_sha256 = $ApprovalLockHashAtTask1Start
    approved_plan_commit = $BaselineCommit
    plan_sha256 = [string]$ApprovalRecord.plan_sha256
    spec_commit = [string]$ApprovalRecord.spec_commit
    spec_sha256 = [string]$ApprovalRecord.spec_sha256
    baseline_game_tree = $BaselineGameTree
    full_selftest_attempt_sha256 = $SelfTestAttemptHash
    full_selftest_completion_sha256 = $SelfTestCompletionHash
    full_selftest_root = $SelfTestRoot
    mother_path = $MotherSave
    mother_sha256 = $MotherHash
    mother_bytes = [long]$MotherLength
    mother_read_only = $true
    artifact_count = [int]$Task1ArtifactEntries.Count
    artifacts = $Task1ArtifactEntries
    cleanup = [ordered]@{
        generator_worktree_removed = -not (Test-Path -LiteralPath $GeneratorRoot)
        generator_savedir_removed = -not (Test-Path -LiteralPath $GeneratorSaveDir)
        observer_worktree_removed = -not (Test-Path -LiteralPath $CleanRoot)
        observer_savedir_removed = -not (Test-Path -LiteralPath $CleanSaveDir)
    }
    finished_utc = [DateTimeOffset]::UtcNow.ToString('o')
}
$Task1CompletionBytes = $StrictUtf8.GetBytes(($Task1CompletionPayload | ConvertTo-Json -Depth 8) + "`n")
$Task1CompletionStream = [IO.File]::Open($Task1CompletionRecord, [IO.FileMode]::CreateNew, [IO.FileAccess]::Write, [IO.FileShare]::Read)
try {
    $Task1CompletionStream.Write($Task1CompletionBytes, 0, $Task1CompletionBytes.Length)
    $Task1CompletionStream.Flush($true)
} finally {
    $Task1CompletionStream.Dispose()
}
git check-ignore -q -- $Task1CompletionRecord
if ($LASTEXITCODE -ne 0) { throw 'Task 1 sealed completion record is not ignored.' }
$SealedTask1Bytes = [IO.File]::ReadAllBytes($Task1CompletionRecord)
if ($SealedTask1Bytes.Length -eq 0 -or
    ($SealedTask1Bytes.Length -ge 3 -and $SealedTask1Bytes[0] -eq 0xEF -and
     $SealedTask1Bytes[1] -eq 0xBB -and $SealedTask1Bytes[2] -eq 0xBF)) {
    throw 'Task 1 sealed completion record is empty or has a BOM.'
}
$SealedTask1Text = $StrictUtf8.GetString($SealedTask1Bytes)
if ($SealedTask1Text.Contains([char]0xFFFD)) { throw 'Task 1 sealed completion record is not strict UTF-8.' }
$SealedTask1 = $SealedTask1Text | ConvertFrom-Json -ErrorAction Stop
$ExpectedTask1CompletionProperties = @(
    'schema_version', 'verdict', 'approved_plan_lock_sha256', 'approved_plan_commit',
    'plan_sha256', 'spec_commit', 'spec_sha256', 'baseline_game_tree',
    'full_selftest_attempt_sha256', 'full_selftest_completion_sha256', 'full_selftest_root',
    'mother_path', 'mother_sha256', 'mother_bytes', 'mother_read_only',
    'artifact_count', 'artifacts', 'cleanup', 'finished_utc'
)
if ($SealedTask1 -isnot [pscustomobject] -or
    (Compare-Object $ExpectedTask1CompletionProperties @($SealedTask1.PSObject.Properties.Name) -CaseSensitive) -or
    $SealedTask1.schema_version -isnot [int] -or [int]$SealedTask1.schema_version -ne 1 -or
    [string]$SealedTask1.verdict -cne 'PASS' -or
    [int]$SealedTask1.artifact_count -ne @($SealedTask1.artifacts).Count -or
    -not [bool]$SealedTask1.mother_read_only) {
    throw 'Task 1 sealed completion record failed its exact top-level contract.'
}
foreach ($CleanupProperty in $SealedTask1.cleanup.PSObject.Properties) {
    if ($CleanupProperty.Value -isnot [bool] -or -not [bool]$CleanupProperty.Value) {
        throw ('Task 1 sealed cleanup proof failed: ' + $CleanupProperty.Name)
    }
}
foreach ($Artifact in @($SealedTask1.artifacts)) {
    if ($Artifact -isnot [pscustomobject] -or
        (Compare-Object @('path', 'bytes', 'sha256') @($Artifact.PSObject.Properties.Name) -CaseSensitive) -or
        $Artifact.path -isnot [string] -or -not [IO.Path]::IsPathRooted([string]$Artifact.path) -or
        -not (Test-PrivateDesktopIntegralValue $Artifact.bytes) -or [int64]$Artifact.bytes -lt 0 -or
        $Artifact.sha256 -isnot [string] -or [string]$Artifact.sha256 -cnotmatch '^[0-9A-F]{64}$' -or
        -not (Test-Path -LiteralPath ([string]$Artifact.path) -PathType Leaf) -or
        (Get-Item -LiteralPath ([string]$Artifact.path)).Length -ne [long]$Artifact.bytes -or
        (Get-FileHash -LiteralPath ([string]$Artifact.path) -Algorithm SHA256).Hash -cne [string]$Artifact.sha256) {
        throw ('Task 1 sealed artifact validation failed: ' + [string]$Artifact.path)
    }
}
(Get-Item -LiteralPath $Task1CompletionRecord).IsReadOnly = $true
if (-not (Get-Item -LiteralPath $Task1CompletionRecord).IsReadOnly) {
    throw 'Task 1 completion record could not be sealed read-only.'
}
$Task1CompletionHash = (Get-FileHash -LiteralPath $Task1CompletionRecord -Algorithm SHA256).Hash
"baseline_commit=$BaselineCommit"
"baseline_game_tree=$BaselineGameTree"
"mother=$MotherSave"
"mother_sha256=$MotherHash"
"baseline_evidence_sha256=$FinalBaselineEvidenceHash"
"task1_completion=$Task1CompletionRecord"
"task1_completion_sha256=$Task1CompletionHash"
```

Expected: the durable game-state artifact is the ignored, read-only mother save, backed by generator and clean-normal-run evidence. A second ignored, read-only, strict machine record seals the approval lock, plan/spec identity, full-selftest attempt/completion, d37d failure, helper sources and full evidence tree, version probe, interrupted attempt, mother, generator, observer, and baseline-manifest artifacts with literal byte counts and SHA-256 values. The shared `game/` tree is still the original pre-change tree. Art, music, sound effects, animation, and UI changes are not required; no shipping asset or package byte has been added.

---

## Task 2: Implement the pure collapse rule and route-aware reachability

**Files:**

- Modify: `game/difficulty.rpy:101-338`
- Modify: `game/balance.rpy:15-98`
- Test: `game/test_game.rpy:127-254`
- Test migration: `game/test_game.rpy:894-968`

- [ ] **Step 0: Validate the immutable approval lock before the first RED edit**

The controller must provide `$ApprovalLockSha256` out of band when it opens this fresh persistent Windows PowerShell 5.1 session. This is Task 2's first project action. Do not read or edit `game/test_game.rpy`, create the `rules` ledger, or inspect Task 1 evidence until this fence passes; keep the same session open through Step 11:

```powershell
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$StrictUtf8 = New-Object System.Text.UTF8Encoding($false, $true)
$ProjectRoot = (Resolve-Path -LiteralPath '.').Path
$ThisPlan = 'docs/superpowers/plans/2026-08-11-terminal-collapse-ending-phase-a.md'
$DesignPath = 'docs/superpowers/specs/2026-08-11-terminal-collapse-ending-design.md'
$EvidenceRoot = Join-Path $ProjectRoot '.superpowers\sdd\terminal-collapse-ending'
$ApprovalLockPath = Join-Path $EvidenceRoot 'approved-plan-lock.json'
$ApprovalLockVariable = Get-Variable -Name ApprovalLockSha256 -Scope 0 -ErrorAction SilentlyContinue
if ($null -eq $ApprovalLockVariable -or $ApprovalLockVariable.Value -isnot [string] -or
    [string]$ApprovalLockVariable.Value -cnotmatch '^[0-9A-F]{64}$') {
    throw 'NEEDS_CONTEXT: Task 2 controller did not bind the out-of-band ApprovalLockSha256 parameter.'
}
$ApprovalLockSha256 = [string]$ApprovalLockVariable.Value
if (-not (Test-Path -LiteralPath $ApprovalLockPath -PathType Leaf)) { throw 'NEEDS_CONTEXT: approved-plan lock is missing.' }
git check-ignore -q -- $ApprovalLockPath
if ($LASTEXITCODE -ne 0) { throw 'NEEDS_CONTEXT: approved-plan lock is not ignored.' }
$ApprovalLockBytes = [IO.File]::ReadAllBytes($ApprovalLockPath)
if ($ApprovalLockBytes.Length -eq 0 -or
    ($ApprovalLockBytes.Length -ge 3 -and $ApprovalLockBytes[0] -eq 0xEF -and
     $ApprovalLockBytes[1] -eq 0xBB -and $ApprovalLockBytes[2] -eq 0xBF)) {
    throw 'NEEDS_CONTEXT: approved-plan lock is empty or has a BOM.'
}
$ApprovalLockText = $StrictUtf8.GetString($ApprovalLockBytes)
if ($ApprovalLockText.Contains([char]0xFFFD) -or
    (Get-FileHash -LiteralPath $ApprovalLockPath -Algorithm SHA256).Hash -cne $ApprovalLockSha256) {
    throw 'NEEDS_CONTEXT: approved-plan lock UTF-8 or out-of-band hash validation failed.'
}
$ApprovalExpectedProperties = @('schema_version', 'approved_plan_commit', 'plan_sha256', 'spec_commit', 'spec_sha256')
$ApprovalRawProperties = @([regex]::Matches($ApprovalLockText, '"([^"\\]+)"\s*:') | ForEach-Object { $_.Groups[1].Value })
if ($ApprovalRawProperties.Count -ne 5 -or
    (Compare-Object $ApprovalExpectedProperties $ApprovalRawProperties -CaseSensitive)) {
    throw 'NEEDS_CONTEXT: approved-plan lock has an inexact or duplicate raw property set.'
}
$ApprovalRecord = $ApprovalLockText | ConvertFrom-Json -ErrorAction Stop
if ($ApprovalRecord -isnot [pscustomobject] -or
    (Compare-Object $ApprovalExpectedProperties @($ApprovalRecord.PSObject.Properties.Name) -CaseSensitive) -or
    $ApprovalRecord.schema_version -isnot [int] -or [int]$ApprovalRecord.schema_version -ne 1 -or
    $ApprovalRecord.approved_plan_commit -isnot [string] -or [string]$ApprovalRecord.approved_plan_commit -cnotmatch '^[0-9a-f]{40}$' -or
    $ApprovalRecord.plan_sha256 -isnot [string] -or [string]$ApprovalRecord.plan_sha256 -cnotmatch '^[0-9A-F]{64}$' -or
    $ApprovalRecord.spec_commit -isnot [string] -or [string]$ApprovalRecord.spec_commit -cne '98ff5ca351806732f435b977c7b3b445d586bf6b' -or
    $ApprovalRecord.spec_sha256 -isnot [string] -or [string]$ApprovalRecord.spec_sha256 -cne 'F7C833952D0F783A922FFF18F6F0A2B9F44BA8F1BF31520917FA6B1237B1A232') {
    throw 'NEEDS_CONTEXT: approved-plan lock schema, types, or values are invalid.'
}
if ((Get-FileHash -LiteralPath $ThisPlan -Algorithm SHA256).Hash -cne [string]$ApprovalRecord.plan_sha256 -or
    (& git hash-object --no-filters -- $ThisPlan).Trim() -cne
        (& git rev-parse ([string]$ApprovalRecord.approved_plan_commit + ':' + $ThisPlan)).Trim() -or
    (Get-FileHash -LiteralPath $DesignPath -Algorithm SHA256).Hash -cne [string]$ApprovalRecord.spec_sha256 -or
    (& git hash-object --no-filters -- $DesignPath).Trim() -cne
        (& git rev-parse ([string]$ApprovalRecord.spec_commit + ':' + $DesignPath)).Trim()) {
    throw 'NEEDS_CONTEXT: physical plan/spec are not the approval-locked raw commit blobs.'
}
if ((& git rev-parse HEAD).Trim() -cne [string]$ApprovalRecord.approved_plan_commit) {
    throw 'NEEDS_CONTEXT: pre-commit Task 2 HEAD is not the approval-locked plan commit.'
}
$ApprovalLockHashAtTask2Start = (Get-FileHash -LiteralPath $ApprovalLockPath -Algorithm SHA256).Hash
```

- [ ] **Step 1: Add the complete failing pure-rule suite**

Insert this suite after `testsuite test_ending_catalog` and before the balance-report suite:

```renpy
testsuite test_terminal_collapse_rules:
    testcase exact_collapse_predicate_and_boundaries:
        parameter (boundary_name, boundary_value) = [
            ("wealth", 20),
            ("loyalty", 20),
        ]

        python:
            _terminal_base = {
                "wealth": 0,
                "loyalty": 0,
                "built_granary": False,
                "alliance_baron": False,
                "baron_joined": False,
                "prince_ally": False,
                "prince_betrayed": False,
                "rel_captain": 59,
                "ch5_pay_advance_pension": False,
                "marriage_route": False,
                "iron_thorn_controlled": False,
            }
        assert eval (is_terminal_resistance_collapse(**_terminal_base))

        python:
            _boundary_state = dict(_terminal_base)
            _boundary_state[boundary_name] = boundary_value

        assert eval (not is_terminal_resistance_collapse(**_boundary_state))

    testcase every_organizational_support_breaks_the_hard_collapse:
        parameter support_override = [
            {"built_granary": True},
            {"alliance_baron": True},
            {"baron_joined": True},
            {"prince_ally": True},
            {"rel_captain": 60},
            {"ch5_pay_advance_pension": True},
            {"marriage_route": True},
            {"iron_thorn_controlled": True},
        ]

        python:
            _terminal_base = {
                "wealth": 0,
                "loyalty": 0,
                "built_granary": False,
                "alliance_baron": False,
                "baron_joined": False,
                "prince_ally": False,
                "prince_betrayed": False,
                "rel_captain": 59,
                "ch5_pay_advance_pension": False,
                "marriage_route": False,
                "iron_thorn_controlled": False,
            }
            _supported_state = dict(_terminal_base)
            _supported_state.update(support_override)

        assert eval (not is_terminal_resistance_collapse(**_supported_state))

    testcase betrayed_prince_does_not_break_collapse:
        python:
            _betrayed_prince_state = {
                "wealth": 0,
                "loyalty": 0,
                "built_granary": False,
                "alliance_baron": False,
                "baron_joined": False,
                "prince_ally": True,
                "prince_betrayed": True,
                "rel_captain": 59,
                "ch5_pay_advance_pension": False,
                "marriage_route": False,
                "iron_thorn_controlled": False,
            }
        assert eval (is_terminal_resistance_collapse(**_betrayed_prince_state))

    testcase relation_projection_matches_formal_change_rel_multiplier_fallback_and_clamp:
        parameter (difficulty_name, current_value, raw_delta, expected_value) = [
            ("easy", 0, 1, 1),
            ("easy", 0, -1, -1),
            ("hard", 0, 1, 1),
            ("easy", 54, 4, 60),
            ("normal", 56, 4, 60),
            ("hard", 58, 4, 60),
            ("normal", 90, 4, 94),
            ("normal", 99, 4, 100),
            ("hard", -99, -4, -100),
        ]

        python:
            _old_difficulty = persistent.difficulty
            _old_rel_captain = getattr(store, "rel_captain", 0)
            _captain_met_existed = hasattr(store, "captain_met")
            _old_captain_met = getattr(store, "captain_met", None)
            _old_show_stat_toast = store._show_stat_toast
            _old_check_hidden_achievements = store.check_hidden_achievements
            _old_check_rel_events = store.check_rel_events
            try:
                persistent.difficulty = difficulty_name
                store.rel_captain = current_value
                store._show_stat_toast = lambda *args, **kwargs: None
                store.check_hidden_achievements = lambda: None
                store.check_rel_events = lambda: None
                _projected_rel_captain = _difficulty_adjusted_rel_value(
                    current_value,
                    raw_delta,
                    difficulty_name,
                )
                change_rel("rel_captain", raw_delta)
                _formal_rel_captain = store.rel_captain
            finally:
                persistent.difficulty = _old_difficulty
                store.rel_captain = _old_rel_captain
                store._show_stat_toast = _old_show_stat_toast
                store.check_hidden_achievements = _old_check_hidden_achievements
                store.check_rel_events = _old_check_rel_events
                renpy.hide_screen("rel_threshold_popup")
                if _captain_met_existed:
                    store.captain_met = _old_captain_met
                elif hasattr(store, "captain_met"):
                    delattr(store, "captain_met")

        assert eval (_projected_rel_captain == expected_value)
        assert eval (_formal_rel_captain == expected_value)
        assert eval (_projected_rel_captain == _formal_rel_captain)

    testcase mountain_then_vanguard_relation_changes_are_sequential:
        parameter (difficulty_name, initial_value, expected_after_mountain, expected_personal, expected_delegate) = [
            ("easy", 80, 75, 69, 81),
            ("normal", 80, 70, 58, 74),
            ("hard", 80, 65, 47, 67),
        ]

        $ _after_mountain = _difficulty_adjusted_rel_value(initial_value, -10, difficulty_name)
        $ _after_personal = _difficulty_adjusted_rel_value(_after_mountain, -12, difficulty_name)
        $ _after_delegate = _difficulty_adjusted_rel_value(_after_mountain, 4, difficulty_name)
        assert eval ((_after_mountain, _after_personal, _after_delegate) == (expected_after_mountain, expected_personal, expected_delegate))

    testcase delegate_relation_threshold_changes_the_enumerated_result:
        parameter (difficulty_name, releasing_start, collapsing_start) = [
            ("easy", 54, 53),
            ("normal", 56, 55),
            ("hard", 58, 57),
        ]

        python:
            _releasing_outcomes = get_resistance_battle_outcomes(
                intrigue=60,
                loyalty=0,
                wealth=0,
                rel_captain=releasing_start,
                difficulty=difficulty_name,
                iron_route_available=True,
                resist_route_available=False,
            )
            _collapsing_outcomes = get_resistance_battle_outcomes(
                intrigue=60,
                loyalty=0,
                wealth=0,
                rel_captain=collapsing_start,
                difficulty=difficulty_name,
                iron_route_available=True,
                resist_route_available=False,
            )
        assert eval (_releasing_outcomes == {"iron_lord": True, "fall": True})
        assert eval (_collapsing_outcomes == {"iron_lord": False, "fall": True})

    testcase route_flags_enumerate_only_real_battle_entries:
        parameter (iron_visible, resist_visible, expected_outcomes) = [
            (True, False, {"iron_lord": False, "fall": True}),
            (False, True, {"iron_lord": True, "fall": False}),
            (True, True, {"iron_lord": True, "fall": True}),
        ]

        python:
            _entry_outcomes = get_resistance_battle_outcomes(
                intrigue=60,
                loyalty=0,
                wealth=0,
                rel_baron=0,
                iron_route_available=iron_visible,
                resist_route_available=resist_visible,
            )
        assert eval (_entry_outcomes == expected_outcomes)

    testcase baron_goodwill_and_supply_intel_are_not_organized_support:
        python:
            _intel_only_outcomes = get_resistance_battle_outcomes(
                intrigue=60,
                loyalty=0,
                wealth=0,
                rel_baron=10,
                baron_supply_intel=True,
                iron_route_available=True,
                resist_route_available=False,
            )
        assert eval (_intel_only_outcomes == {"iron_lord": False, "fall": True})

    testcase granary_breaks_collapse_but_does_not_grant_a_win:
        python:
            _granary_outcomes = get_resistance_battle_outcomes(
                loyalty=0,
                wealth=0,
                built_granary=True,
                iron_route_available=True,
                resist_route_available=False,
            )
        assert eval (_granary_outcomes == {"iron_lord": False, "fall": True})

    testcase betrayed_prince_neither_supports_nor_scores:
        python:
            _loyal_prince_outcomes = get_resistance_battle_outcomes(
                loyalty=0,
                wealth=0,
                prince_ally=True,
                prince_betrayed=False,
                iron_route_available=True,
                resist_route_available=False,
            )
            _betrayed_prince_outcomes = get_resistance_battle_outcomes(
                loyalty=0,
                wealth=0,
                prince_ally=True,
                prince_betrayed=True,
                iron_route_available=True,
                resist_route_available=False,
            )
        assert eval (_loyal_prince_outcomes == {"iron_lord": True, "fall": True})
        assert eval (_betrayed_prince_outcomes == {"iron_lord": False, "fall": True})

    testcase collapse_is_identical_at_all_difficulties:
        parameter difficulty_name = ["easy", "normal", "hard"]

        python:
            _difficulty_outcomes = get_resistance_battle_outcomes(
                power=55,
                loyalty=0,
                wealth=0,
                difficulty=difficulty_name,
                iron_route_available=True,
                resist_route_available=False,
            )
        assert eval (_difficulty_outcomes == {"iron_lord": False, "fall": True})

    testcase player_feedback_route_stays_visible_but_only_fall_is_reachable:
        python:
            _feedback_routes = get_finale_route_availability(
                power=55,
                loyalty=0,
                difficulty="normal",
                rel_baron=-1,
                rel_queen=-1,
            )
            _feedback_battle = get_resistance_battle_outcomes(
                power=55,
                loyalty=0,
                wealth=0,
                difficulty="normal",
                iron_route_available=_feedback_routes["iron_lord"],
                resist_route_available=_feedback_routes["resist"],
            )
            _feedback_endings = get_finale_ending_availability(
                _feedback_routes,
                _feedback_battle,
            )
        assert eval (_feedback_routes["iron_lord"])
        assert eval (not _feedback_routes["resist"])
        assert eval (_feedback_battle == {"iron_lord": False, "fall": True})
        assert eval (not _feedback_endings["iron_lord"])
        assert eval (_feedback_endings["fall"])

    testcase visible_battle_route_requires_outcomes_but_nonbattle_map_does_not:
        python:
            _mapper_error = ""
            try:
                get_finale_ending_availability({"iron_lord": True, "resist": False})
            except ValueError as exc:
                _mapper_error = str(exc)

        assert eval (_mapper_error == "resistance_outcomes is required when an iron_lord or resist route is visible")

        $ _nonbattle_routes = get_finale_route_availability(difficulty="hard", southern_outcome="free")
        $ _nonbattle_endings = get_finale_ending_availability(_nonbattle_routes)
        assert eval (not _nonbattle_routes["iron_lord"] and not _nonbattle_routes["resist"])
        assert eval (_nonbattle_endings["sea"])

    testcase current_wrappers_tolerate_missing_legacy_support_fields:
        python:
            _optional_names = (
                "built_granary",
                "alliance_baron",
                "resist_route",
                "prince_ally",
                "prince_betrayed",
                "rel_captain",
                "ch5_pay_advance_pension",
                "marriage_route",
                "iron_thorn_controlled",
                "baron_supply_intel",
            )
            _optional_snapshot = {
                name: (hasattr(store, name), getattr(store, name, None))
                for name in _optional_names
            }
            try:
                for name in _optional_names:
                    if hasattr(store, name):
                        delattr(store, name)
                _legacy_routes = get_current_finale_route_availability()
                _legacy_battle = get_current_resistance_battle_outcomes()
                _legacy_collapse = is_current_terminal_resistance_collapse()
            finally:
                for name, (existed, value) in _optional_snapshot.items():
                    if existed:
                        setattr(store, name, value)
                    elif hasattr(store, name):
                        delattr(store, name)

        assert eval (set(_legacy_battle) == {"iron_lord", "fall"})
        assert eval (set(_legacy_routes) == {"iron_lord", "shadow_king", "holy_guardian", "peoples_lord", "truth", "borgia", "vassal", "resist", "sea", "fall"})
        assert eval (isinstance(_legacy_collapse, bool))
```

- [ ] **Step 2: Run and preserve the exact RED**

Continue in the same approval-validated Task 2 PowerShell session. Re-bind the ignored helper sources to Task 1's sealed machine evidence before any Ren'Py process starts; do not reconstruct this state after a failed invocation.

```powershell
$HelperRoot = Join-Path $EvidenceRoot 'helpers'
$RunnerSource = Join-Path $HelperRoot 'PrivateDesktopRunner.cs'
$HeadlessWrapper = Join-Path $HelperRoot 'Invoke-PrivateDesktopProcess.ps1'
$HeadlessSelfTest = Join-Path $HelperRoot 'Test-PrivateDesktopRunner.ps1'
$ExpectedTask2HelperHashes = [ordered]@{
    'PrivateDesktopRunner.cs' = [pscustomobject]@{ Bytes = 82334; Sha256 = 'E0393DB1E113FDB8C35097978AA73B7D33AFDD5788499002B6423D883DEED4E8' }
    'Invoke-PrivateDesktopProcess.ps1' = [pscustomobject]@{ Bytes = 24229; Sha256 = '73A3F9C43CF994E08F004E0A1266122A3EC5E0EAF065C63E6D9439CF0B0E1880' }
    'Test-PrivateDesktopRunner.ps1' = [pscustomobject]@{ Bytes = 53188; Sha256 = '20198B669F70E51E51F71BD01E6D06D1949D300F43CE9A94FB0190A47D781A15' }
}
$BaselineEvidence = Join-Path $EvidenceRoot 'legacy\baseline-evidence.md'
$Task1CompletionRecord = Join-Path $EvidenceRoot 'legacy\task1-completion.json'
$RunnerTemplatePath = Join-Path $ProjectRoot 'Tools\Run-RenPySuite.ps1'
$TrustedSdkRoot = 'E:\Projects\renpy-8.5.2-sdk'
$RenPyExe = Join-Path $TrustedSdkRoot 'renpy.exe'
$ConfiguredSdkRoot = [Environment]::GetEnvironmentVariable('RENPY_SDK', 'Process')
if (-not [string]::IsNullOrWhiteSpace($ConfiguredSdkRoot) -and
    -not [IO.Path]::GetFullPath($ConfiguredSdkRoot).TrimEnd('\').Equals($TrustedSdkRoot, [StringComparison]::OrdinalIgnoreCase)) {
    throw 'Process RENPY_SDK points somewhere other than the approved RenPy 8.5.2 SDK.'
}
$PowerShellExe = (Get-Command powershell.exe -CommandType Application -ErrorAction Stop).Source
$Task2BaselineCommit = (& git rev-parse HEAD).Trim()
$ExpectedPlanSubject = 'docs: plan terminal collapse coverage v2 retry'
if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($Task2BaselineCommit) -or
    (git log -1 --format=%s) -cne $ExpectedPlanSubject) {
    throw 'Task 2 did not start from the final executable-plan commit.'
}
if ($Task2BaselineCommit -cne [string]$ApprovalRecord.approved_plan_commit) {
    throw 'Task 2 baseline is not the approval-locked plan commit.'
}
$Task2EvidenceRoot = Join-Path $EvidenceRoot 'rules'
$ExplicitTaskTempRoot = [Environment]::GetEnvironmentVariable('TC_TASK_TEMP_ROOT', 'Process')
if (-not [string]::IsNullOrWhiteSpace($ExplicitTaskTempRoot)) {
    $TaskTempRoot = [IO.Path]::GetFullPath($ExplicitTaskTempRoot)
} else {
    $TaskTempRoot = 'E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp'
}
if (-not (Test-Path -LiteralPath $TaskTempRoot -PathType Container)) {
    throw ('Task 2 temp root must already exist outside the repository: ' + $TaskTempRoot)
}
$TaskTempRoot = (Resolve-Path -LiteralPath $TaskTempRoot).Path
$Task2SaveRoot = Join-Path $TaskTempRoot ('cos-terminal-collapse-task2-' + [Guid]::NewGuid().ToString('N'))

foreach ($RequiredFile in @($RunnerSource, $HeadlessWrapper, $HeadlessSelfTest, $BaselineEvidence, $Task1CompletionRecord, $RunnerTemplatePath, $RenPyExe, $PowerShellExe)) {
    if (-not (Test-Path -LiteralPath $RequiredFile -PathType Leaf)) {
        throw ('Task 2 prerequisite is missing: ' + $RequiredFile)
    }
}
$RunnerTemplateHash = (Get-FileHash -LiteralPath $RunnerTemplatePath -Algorithm SHA256).Hash
if ([string]::IsNullOrWhiteSpace($RunnerTemplateHash) -or
    @(git diff --name-only -- Tools/Run-RenPySuite.ps1).Count -ne 0) {
    throw 'Task 2 runner is not the unchanged file from the executable-plan baseline.'
}
git check-ignore -q -- $Task1CompletionRecord
if ($LASTEXITCODE -ne 0 -or -not (Get-Item -LiteralPath $Task1CompletionRecord).IsReadOnly) {
    throw 'Task 1 sealed completion record is not ignored and read-only.'
}
function Test-Task2IntegralValue($Value) {
    return ($Value -is [byte] -or $Value -is [sbyte] -or
        $Value -is [int16] -or $Value -is [uint16] -or
        $Value -is [int32] -or $Value -is [uint32] -or
        $Value -is [int64] -or $Value -is [uint64])
}
$Task1CompletionBytes = [IO.File]::ReadAllBytes($Task1CompletionRecord)
if ($Task1CompletionBytes.Length -eq 0 -or
    ($Task1CompletionBytes.Length -ge 3 -and $Task1CompletionBytes[0] -eq 0xEF -and
     $Task1CompletionBytes[1] -eq 0xBB -and $Task1CompletionBytes[2] -eq 0xBF)) {
    throw 'Task 1 sealed completion record is empty or has a BOM.'
}
$Task1CompletionText = $StrictUtf8.GetString($Task1CompletionBytes)
if ($Task1CompletionText.Contains([char]0xFFFD)) { throw 'Task 1 sealed completion record is not strict UTF-8.' }
$Task1Completion = $Task1CompletionText | ConvertFrom-Json -ErrorAction Stop
$ExpectedTask1CompletionProperties = @(
    'schema_version', 'verdict', 'approved_plan_lock_sha256', 'approved_plan_commit',
    'plan_sha256', 'spec_commit', 'spec_sha256', 'baseline_game_tree',
    'full_selftest_attempt_sha256', 'full_selftest_completion_sha256', 'full_selftest_root',
    'mother_path', 'mother_sha256', 'mother_bytes', 'mother_read_only',
    'artifact_count', 'artifacts', 'cleanup', 'finished_utc'
)
if ($Task1Completion -isnot [pscustomobject] -or
    (Compare-Object $ExpectedTask1CompletionProperties @($Task1Completion.PSObject.Properties.Name) -CaseSensitive) -or
    $Task1Completion.schema_version -isnot [int] -or [int]$Task1Completion.schema_version -ne 1 -or
    $Task1Completion.verdict -isnot [string] -or [string]$Task1Completion.verdict -cne 'PASS' -or
    $Task1Completion.approved_plan_lock_sha256 -isnot [string] -or
    [string]$Task1Completion.approved_plan_lock_sha256 -cne $ApprovalLockSha256 -or
    $Task1Completion.approved_plan_commit -isnot [string] -or
    [string]$Task1Completion.approved_plan_commit -cne [string]$ApprovalRecord.approved_plan_commit -or
    $Task1Completion.plan_sha256 -isnot [string] -or
    [string]$Task1Completion.plan_sha256 -cne [string]$ApprovalRecord.plan_sha256 -or
    $Task1Completion.spec_commit -isnot [string] -or
    [string]$Task1Completion.spec_commit -cne [string]$ApprovalRecord.spec_commit -or
    $Task1Completion.spec_sha256 -isnot [string] -or
    [string]$Task1Completion.spec_sha256 -cne [string]$ApprovalRecord.spec_sha256 -or
    $Task1Completion.baseline_game_tree -isnot [string] -or
    [string]$Task1Completion.baseline_game_tree -cne 'fa7a398e9d989731b24e3c1642f3e2e33ce846ff' -or
    $Task1Completion.full_selftest_attempt_sha256 -isnot [string] -or
    [string]$Task1Completion.full_selftest_attempt_sha256 -cnotmatch '^[0-9A-F]{64}$' -or
    $Task1Completion.full_selftest_completion_sha256 -isnot [string] -or
    [string]$Task1Completion.full_selftest_completion_sha256 -cnotmatch '^[0-9A-F]{64}$' -or
    $Task1Completion.full_selftest_root -isnot [string] -or
    -not [IO.Path]::IsPathRooted([string]$Task1Completion.full_selftest_root) -or
    -not (Test-Path -LiteralPath ([string]$Task1Completion.full_selftest_root) -PathType Container) -or
    $Task1Completion.mother_path -isnot [string] -or
    -not [IO.Path]::IsPathRooted([string]$Task1Completion.mother_path) -or
    $Task1Completion.mother_sha256 -isnot [string] -or
    [string]$Task1Completion.mother_sha256 -cnotmatch '^[0-9A-F]{64}$' -or
    -not (Test-Task2IntegralValue $Task1Completion.mother_bytes) -or [int64]$Task1Completion.mother_bytes -le 0 -or
    $Task1Completion.mother_read_only -isnot [bool] -or -not [bool]$Task1Completion.mother_read_only -or
    -not (Test-Task2IntegralValue $Task1Completion.artifact_count) -or [int64]$Task1Completion.artifact_count -lt 30 -or
    [int64]$Task1Completion.artifact_count -ne @($Task1Completion.artifacts).Count -or
    $Task1Completion.finished_utc -isnot [string]) {
    throw 'Task 1 sealed completion record failed its exact Task 2 top-level contract.'
}
$ExpectedCleanupProperties = @(
    'generator_worktree_removed', 'generator_savedir_removed',
    'observer_worktree_removed', 'observer_savedir_removed'
)
if ($Task1Completion.cleanup -isnot [pscustomobject] -or
    (Compare-Object $ExpectedCleanupProperties @($Task1Completion.cleanup.PSObject.Properties.Name) -CaseSensitive)) {
    throw 'Task 1 sealed cleanup property set is inexact.'
}
foreach ($CleanupProperty in $Task1Completion.cleanup.PSObject.Properties) {
    if ($CleanupProperty.Value -isnot [bool] -or -not [bool]$CleanupProperty.Value) {
        throw ('Task 1 sealed cleanup proof failed: ' + $CleanupProperty.Name)
    }
}
$Task1ArtifactLookup = @{}
foreach ($Artifact in @($Task1Completion.artifacts)) {
    if ($Artifact -isnot [pscustomobject] -or
        (Compare-Object @('path', 'bytes', 'sha256') @($Artifact.PSObject.Properties.Name) -CaseSensitive) -or
        $Artifact.path -isnot [string] -or -not [IO.Path]::IsPathRooted([string]$Artifact.path) -or
        -not (Test-Task2IntegralValue $Artifact.bytes) -or [int64]$Artifact.bytes -lt 0 -or
        $Artifact.sha256 -isnot [string] -or [string]$Artifact.sha256 -cnotmatch '^[0-9A-F]{64}$') {
        throw ('Task 1 sealed artifact has an invalid schema: ' + [string]$Artifact.path)
    }
    $ArtifactKey = [IO.Path]::GetFullPath([string]$Artifact.path).TrimEnd('\')
    if ($Task1ArtifactLookup.ContainsKey($ArtifactKey)) {
        throw ('Task 1 sealed artifact path is duplicated: ' + $ArtifactKey)
    }
    if (-not (Test-Path -LiteralPath $ArtifactKey -PathType Leaf) -or
        (Get-Item -LiteralPath $ArtifactKey).Length -ne [int64]$Artifact.bytes -or
        (Get-FileHash -LiteralPath $ArtifactKey -Algorithm SHA256).Hash -cne [string]$Artifact.sha256) {
        throw ('Task 1 sealed artifact is missing or drifted: ' + $ArtifactKey)
    }
    $Task1ArtifactLookup[$ArtifactKey] = $Artifact
}
function Assert-Task1SealedArtifact([string]$Path, [string]$ExpectedSha256 = '') {
    $ArtifactKey = [IO.Path]::GetFullPath($Path).TrimEnd('\')
    if (-not $Task1ArtifactLookup.ContainsKey($ArtifactKey)) {
        throw ('Task 1 completion does not seal required artifact: ' + $ArtifactKey)
    }
    if (-not [string]::IsNullOrWhiteSpace($ExpectedSha256) -and
        [string]$Task1ArtifactLookup[$ArtifactKey].sha256 -cne $ExpectedSha256) {
        throw ('Task 1 completion seals the wrong hash for: ' + $ArtifactKey)
    }
}
$FailedV1CoverageResult = 'E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-private-desktop-selftest-d37d19e4adfc4b5fb3622abcc8a53212\short-lived-pid-coverage\result.json'
$SelfTestAttemptRecord = Join-Path $EvidenceRoot 'helper-v2-full-selftest-attempt\attempt.json'
$SelfTestCompletionRecord = Join-Path $EvidenceRoot 'helper-v2-full-selftest-attempt\completion.json'
$InterruptedSaveDir = 'E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-old-save-1f027ab224b74d8890172376314ea3b1'
foreach ($RequiredSealedArtifact in @(
    $ApprovalLockPath, (Join-Path $ProjectRoot $ThisPlan), (Join-Path $ProjectRoot $DesignPath),
    $RunnerSource, $HeadlessWrapper, $HeadlessSelfTest, $BaselineEvidence,
    $FailedV1CoverageResult, $SelfTestAttemptRecord, $SelfTestCompletionRecord,
    (Join-Path $EvidenceRoot 'legacy\generator-state.json'),
    (Join-Path $EvidenceRoot 'legacy\observer-state.json'),
    (Join-Path $EvidenceRoot 'legacy\generator-process\request.json'),
    (Join-Path $EvidenceRoot 'legacy\generator-process\stdout.txt'),
    (Join-Path $EvidenceRoot 'legacy\generator-process\stderr.txt'),
    (Join-Path $EvidenceRoot 'legacy\generator-process\result.json'),
    (Join-Path $EvidenceRoot 'legacy\generator-process\renpy-log.txt'),
    (Join-Path $EvidenceRoot 'legacy\observer-process\request.json'),
    (Join-Path $EvidenceRoot 'legacy\observer-process\stdout.txt'),
    (Join-Path $EvidenceRoot 'legacy\observer-process\stderr.txt'),
    (Join-Path $EvidenceRoot 'legacy\observer-process\result.json'),
    (Join-Path $EvidenceRoot 'legacy\observer-process\renpy-log.txt'),
    (Join-Path $EvidenceRoot 'legacy\renpy-version-process\request.json'),
    (Join-Path $EvidenceRoot 'legacy\renpy-version-process\stdout.txt'),
    (Join-Path $EvidenceRoot 'legacy\renpy-version-process\stderr.txt'),
    (Join-Path $EvidenceRoot 'legacy\renpy-version-process\result.json'),
    [string]$Task1Completion.mother_path
)) {
    Assert-Task1SealedArtifact $RequiredSealedArtifact
}
Assert-Task1SealedArtifact $ApprovalLockPath $ApprovalLockSha256
Assert-Task1SealedArtifact $FailedV1CoverageResult '300515E17B8EDD6B0CD99C268E685DCAE6770BC664B5C28F231F231F03E9F27B'
Assert-Task1SealedArtifact $SelfTestAttemptRecord ([string]$Task1Completion.full_selftest_attempt_sha256)
Assert-Task1SealedArtifact $SelfTestCompletionRecord ([string]$Task1Completion.full_selftest_completion_sha256)
Assert-Task1SealedArtifact ([string]$Task1Completion.mother_path) ([string]$Task1Completion.mother_sha256)
if ((Get-Item -LiteralPath ([string]$Task1Completion.mother_path)).Length -ne [int64]$Task1Completion.mother_bytes -or
    -not (Get-Item -LiteralPath ([string]$Task1Completion.mother_path)).IsReadOnly) {
    throw 'Task 1 mother no longer matches its sealed size/read-only contract.'
}
foreach ($RecursiveSealedFile in @(
    @(Get-ChildItem -LiteralPath ([string]$Task1Completion.full_selftest_root) -Recurse -File) +
    @(Get-ChildItem -LiteralPath $InterruptedSaveDir -Recurse -File)
)) {
    Assert-Task1SealedArtifact $RecursiveSealedFile.FullName
}
$Task1CompletionHashAtTask2Start = (Get-FileHash -LiteralPath $Task1CompletionRecord -Algorithm SHA256).Hash
$Task2HelperHashes = [ordered]@{}
foreach ($HelperPath in @($RunnerSource, $HeadlessWrapper, $HeadlessSelfTest)) {
    git check-ignore -q -- $HelperPath
    if ($LASTEXITCODE -ne 0) { throw ('Helper is not ignored: ' + $HelperPath) }
    $HelperHash = (Get-FileHash -LiteralPath $HelperPath -Algorithm SHA256).Hash
    $HelperName = Split-Path $HelperPath -Leaf
    $ExpectedHelper = $ExpectedTask2HelperHashes[$HelperName]
    if ($HelperHash -cne [string]$ExpectedHelper.Sha256 -or
        (Get-Item -LiteralPath $HelperPath).Length -ne [long]$ExpectedHelper.Bytes -or
        [string]$Task1ArtifactLookup[[IO.Path]::GetFullPath($HelperPath).TrimEnd('\')].sha256 -cne $HelperHash) {
        throw ('Helper hash is not bound by the Task 1 sealed completion: ' + $HelperPath)
    }
    $Task2HelperHashes[$HelperName] = $HelperHash
}
. $HeadlessWrapper
if ($null -eq (Get-Command Invoke-PrivateDesktopProcess -CommandType Function -ErrorAction SilentlyContinue)) {
    throw 'Invoke-PrivateDesktopProcess was not imported.'
}
foreach ($NewRoot in @($Task2EvidenceRoot, $Task2SaveRoot)) {
    if (Test-Path -LiteralPath $NewRoot) { throw ('Task 2 root unexpectedly exists: ' + $NewRoot) }
    New-Item -ItemType Directory -Path $NewRoot -ErrorAction Stop | Out-Null
}
git check-ignore -q -- $Task2EvidenceRoot
if ($LASTEXITCODE -ne 0) { throw 'Task 2 evidence root is not ignored.' }

# The stable ignored `rules` directory is the create-new attempt ledger for
# the entire task. If this session is lost or any invocation fails, a future
# session sees the directory and stops above; it must not choose a new root or
# replay a RED/GREEN without explicit new user authorization.
$ProjectPrefix = $ProjectRoot.TrimEnd('\') + '\'
$TaskTempPrefix = $TaskTempRoot.TrimEnd('\') + '\'
$SavePrefix = ([IO.Path]::GetFullPath($Task2SaveRoot)).TrimEnd('\') + '\'
if ($TaskTempPrefix.StartsWith($ProjectPrefix, [StringComparison]::OrdinalIgnoreCase) -or
    $ProjectPrefix.StartsWith($TaskTempPrefix, [StringComparison]::OrdinalIgnoreCase) -or
    $SavePrefix.StartsWith($ProjectPrefix, [StringComparison]::OrdinalIgnoreCase) -or
    $ProjectPrefix.StartsWith($SavePrefix, [StringComparison]::OrdinalIgnoreCase)) {
    throw 'Task 2 temp and SaveDir roots must be external to and disjoint from ProjectRoot.'
}

function New-Task2TestMirror {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)][ValidatePattern('^[A-Za-z0-9_.-]+$')][string]$Name,
        [Parameter(Mandatory = $true)][ValidateNotNullOrEmpty()][string[]]$ExpectedPaths
    )

    $ExpectedSorted = @($ExpectedPaths | Sort-Object)
    $SharedDiffPaths = @(git diff --name-only | Sort-Object)
    if (Compare-Object $ExpectedSorted $SharedDiffPaths) {
        throw ('NEEDS_CONTEXT: shared RED/GREEN scope is not the exact mirror input for ' + $Name + ': ' + ($SharedDiffPaths -join ', '))
    }
    if (@(git diff --cached --name-only).Count -ne 0) {
        throw 'NEEDS_CONTEXT: shared index is not empty before creating a Task 2 test mirror.'
    }

    $MirrorRoot = Join-Path $TaskTempRoot ('cos-terminal-collapse-task2-mirror-' + $Name + '-' + [Guid]::NewGuid().ToString('N'))
    if (Test-Path -LiteralPath $MirrorRoot) {
        throw ('NEEDS_CONTEXT: Task 2 mirror path already exists: ' + $MirrorRoot)
    }
    git worktree add --detach $MirrorRoot $Task2BaselineCommit
    if ($LASTEXITCODE -ne 0) { throw ('NEEDS_CONTEXT: could not create Task 2 mirror: ' + $MirrorRoot) }
    if ((git -C $MirrorRoot rev-parse HEAD) -cne $Task2BaselineCommit -or
        @(git -C $MirrorRoot status --short --untracked-files=all).Count -ne 0) {
        throw ('NEEDS_CONTEXT: fresh Task 2 mirror is not the exact clean plan baseline: ' + $MirrorRoot)
    }
    if (Test-Path -LiteralPath (Join-Path $MirrorRoot 'game\saves')) {
        throw ('NEEDS_CONTEXT: fresh Task 2 mirror unexpectedly contains game/saves: ' + $MirrorRoot)
    }

    foreach ($RelativePath in $ExpectedSorted) {
        if (-not $RelativePath.StartsWith('game/', [StringComparison]::Ordinal) -or
            $RelativePath.Contains('..') -or -not $RelativePath.EndsWith('.rpy', [StringComparison]::Ordinal)) {
            throw ('NEEDS_CONTEXT: invalid Task 2 mirror source path: ' + $RelativePath)
        }
        $SourcePath = Join-Path $ProjectRoot ($RelativePath.Replace('/', '\'))
        $DestinationPath = Join-Path $MirrorRoot ($RelativePath.Replace('/', '\'))
        if (-not (Test-Path -LiteralPath $SourcePath -PathType Leaf) -or
            -not (Test-Path -LiteralPath $DestinationPath -PathType Leaf)) {
            throw ('NEEDS_CONTEXT: Task 2 mirror source or destination is missing: ' + $RelativePath)
        }
        [IO.File]::Copy($SourcePath, $DestinationPath, $true)
        if ((Get-FileHash -LiteralPath $SourcePath -Algorithm SHA256).Hash -cne
            (Get-FileHash -LiteralPath $DestinationPath -Algorithm SHA256).Hash) {
            throw ('NEEDS_CONTEXT: byte copy into Task 2 mirror failed: ' + $RelativePath)
        }
    }

    $ExpectedStatus = @($ExpectedSorted | ForEach-Object { ' M ' + $_ })
    $MirrorStatus = @(git -C $MirrorRoot status --short --untracked-files=all | Sort-Object)
    if (Compare-Object $ExpectedStatus $MirrorStatus) {
        throw ('NEEDS_CONTEXT: Task 2 mirror scope drifted: ' + ($MirrorStatus -join '; '))
    }
    git -C $MirrorRoot diff --check -- @ExpectedSorted
    if ($LASTEXITCODE -ne 0) { throw ('NEEDS_CONTEXT: Task 2 mirror diff check failed: ' + $MirrorRoot) }
    return $MirrorRoot
}

function Remove-VerifiedTask2Mirror {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)][string]$MirrorRoot,
        [Parameter(Mandatory = $true)][ValidateNotNullOrEmpty()][string[]]$ExpectedPaths
    )

    $MirrorFull = [IO.Path]::GetFullPath($MirrorRoot).TrimEnd('\')
    $TempFull = [IO.Path]::GetFullPath($TaskTempRoot).TrimEnd('\')
    if (-not $MirrorFull.StartsWith($TempFull + '\', [StringComparison]::OrdinalIgnoreCase) -or
        -not (Split-Path $MirrorFull -Leaf).StartsWith('cos-terminal-collapse-task2-mirror-', [StringComparison]::Ordinal)) {
        throw ('NEEDS_CONTEXT: refusing to remove unverified Task 2 mirror: ' + $MirrorFull)
    }
    if ((git -C $MirrorFull rev-parse HEAD) -cne $Task2BaselineCommit) {
        throw ('NEEDS_CONTEXT: Task 2 mirror HEAD drifted before cleanup: ' + $MirrorFull)
    }
    $ExpectedStatus = @($ExpectedPaths | Sort-Object | ForEach-Object { ' M ' + $_ })
    $ObservedStatus = @(git -C $MirrorFull status --short --untracked-files=all | Sort-Object)
    if (Compare-Object $ExpectedStatus $ObservedStatus) {
        throw ('NEEDS_CONTEXT: Task 2 mirror scope drifted before cleanup: ' + ($ObservedStatus -join '; '))
    }
    $RegisteredRoots = @(
        git worktree list --porcelain |
            Where-Object { $_.StartsWith('worktree ', [StringComparison]::Ordinal) } |
            ForEach-Object { [IO.Path]::GetFullPath($_.Substring(9)).TrimEnd('\') }
    )
    if ($RegisteredRoots -notcontains $MirrorFull) {
        throw ('NEEDS_CONTEXT: Task 2 mirror is not the exact registered worktree: ' + $MirrorFull)
    }
    git worktree remove --force $MirrorFull
    if ($LASTEXITCODE -ne 0) { throw ('NEEDS_CONTEXT: verified Task 2 mirror cleanup failed: ' + $MirrorFull) }
    git worktree prune
    if (Test-Path -LiteralPath $MirrorFull) {
        throw ('NEEDS_CONTEXT: verified Task 2 mirror remains after cleanup: ' + $MirrorFull)
    }
}

function Write-Task2CreateNewUtf8 {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)][string]$Path,
        [Parameter(Mandatory = $true)][AllowEmptyString()][string]$Text
    )

    $Bytes = $StrictUtf8.GetBytes($Text)
    $Stream = [IO.File]::Open($Path, [IO.FileMode]::CreateNew, [IO.FileAccess]::Write, [IO.FileShare]::None)
    try {
        $Stream.Write($Bytes, 0, $Bytes.Length)
        $Stream.Flush($true)
    } finally {
        $Stream.Dispose()
    }
}

function New-Task2FileSeal([string]$Path) {
    if (-not [IO.Path]::IsPathRooted($Path) -or -not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        throw ('NEEDS_CONTEXT: invocation receipt source is missing or non-absolute: ' + $Path)
    }
    $FullPath = (Resolve-Path -LiteralPath $Path).Path
    $Item = Get-Item -LiteralPath $FullPath -ErrorAction Stop
    return [pscustomobject][ordered]@{
        path = $FullPath
        bytes = [long]$Item.Length
        sha256 = (Get-FileHash -LiteralPath $FullPath -Algorithm SHA256).Hash
    }
}

function Test-Task2FileSealIdentity($Left, $Right) {
    return (
        $Left -is [pscustomobject] -and $Right -is [pscustomobject] -and
        [string]$Left.path -ceq [string]$Right.path -and
        [int64]$Left.bytes -eq [int64]$Right.bytes -and
        [string]$Left.sha256 -ceq [string]$Right.sha256
    )
}

function New-Task2InvocationReceipt {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)][ValidatePattern('^[A-Za-z0-9_.-]+$')][string]$Name,
        [Parameter(Mandatory = $true)][ValidateSet('suite','scanner','lint')][string]$Kind,
        [Parameter(Mandatory = $true)][string]$Expected,
        [Parameter(Mandatory = $true)][string]$Actual,
        [Parameter(Mandatory = $true)][string]$HelperEvidenceDir,
        [Parameter(Mandatory = $true)][string]$RunnerOrScannerEvidenceDir,
        [Parameter(Mandatory = $true)][ValidateNotNullOrEmpty()][string[]]$DirectEvidencePaths,
        [Parameter()][string[]]$SourceEvidencePaths = @()
    )

    if ($Expected -cne $Actual) {
        throw ('NEEDS_CONTEXT: refusing to seal a non-PASS invocation receipt: ' + $Name)
    }
    if (-not [IO.Path]::IsPathRooted($HelperEvidenceDir) -or
        -not (Test-Path -LiteralPath $HelperEvidenceDir -PathType Container) -or
        -not [IO.Path]::IsPathRooted($RunnerOrScannerEvidenceDir) -or
        -not (Test-Path -LiteralPath $RunnerOrScannerEvidenceDir -PathType Container)) {
        throw ('NEEDS_CONTEXT: receipt evidence directory is missing or non-absolute: ' + $Name)
    }
    $HelperFull = (Resolve-Path -LiteralPath $HelperEvidenceDir).Path
    $RunnerOrScannerFull = (Resolve-Path -LiteralPath $RunnerOrScannerEvidenceDir).Path
    $HelperArtifacts = @(
        New-Task2FileSeal (Join-Path $HelperFull 'request.json')
        New-Task2FileSeal (Join-Path $HelperFull 'stdout.txt')
        New-Task2FileSeal (Join-Path $HelperFull 'stderr.txt')
        New-Task2FileSeal (Join-Path $HelperFull 'result.json')
    )
    $HelperResult = $HelperArtifacts[3]
    $DirectEvidence = @($DirectEvidencePaths | ForEach-Object { New-Task2FileSeal $_ })
    $SourceEvidence = @($SourceEvidencePaths | ForEach-Object { New-Task2FileSeal $_ })

    $ExpectedDirectCount = if ($Name -ceq 'show-before-green') { 3 } elseif ($Kind -ceq 'scanner') { 2 } else { 1 }
    $ExpectedSourceCount = if ($Name -ceq 'show-before-green') { 1 } else { 0 }
    if ($DirectEvidence.Count -ne $ExpectedDirectCount -or $SourceEvidence.Count -ne $ExpectedSourceCount) {
        throw ('NEEDS_CONTEXT: receipt direct/source cardinality failed: ' + $Name)
    }
    if ($Kind -ceq 'scanner') {
        if ($RunnerOrScannerFull -cne $HelperFull -or
            -not (Test-Task2FileSealIdentity $DirectEvidence[0] $HelperArtifacts[1]) -or
            -not (Test-Task2FileSealIdentity $DirectEvidence[1] $HelperArtifacts[2])) {
            throw ('NEEDS_CONTEXT: scanner stdout/stderr receipt relation failed: ' + $Name)
        }
    } else {
        $ExpectedRunnerExtension = if ($Kind -ceq 'suite') { '.log' } else { '.txt' }
        if ([IO.Path]::GetDirectoryName([string]$DirectEvidence[0].path) -cne $RunnerOrScannerFull -or
            [IO.Path]::GetExtension([string]$DirectEvidence[0].path) -cne $ExpectedRunnerExtension) {
            throw ('NEEDS_CONTEXT: suite/lint direct evidence relation failed: ' + $Name)
        }
    }
    if ($Name -ceq 'show-before-green' -and
        ($Kind -cne 'scanner' -or -not (Test-Task2FileSealIdentity $DirectEvidence[2] $SourceEvidence[0]))) {
        throw 'NEEDS_CONTEXT: show-before source is not exactly direct_evidence[2].'
    }
    $ReceiptPath = Join-Path $HelperFull 'invocation-receipt.json'
    $ReceiptPayload = [ordered]@{
        schema_version = 1
        name = $Name
        kind = $Kind
        expected = $Expected
        actual = $Actual
        verdict = 'PASS'
        helper_evidence_dir = $HelperFull
        helper_artifacts = $HelperArtifacts
        helper_result = $HelperResult
        runner_or_scanner_evidence_dir = $RunnerOrScannerFull
        direct_evidence = $DirectEvidence
        source_evidence = $SourceEvidence
        assertions = [ordered]@{
            central_safety_envelope = 'PASS'
            outcome_gates = 'PASS'
            runner_or_scanner = 'PASS'
        }
        created_utc = [DateTimeOffset]::UtcNow.ToString('o')
    }
    Write-Task2CreateNewUtf8 -Path $ReceiptPath -Text (($ReceiptPayload | ConvertTo-Json -Depth 10) + "`n")
    $ReceiptRaw = [IO.File]::ReadAllBytes($ReceiptPath)
    if ($ReceiptRaw.Length -eq 0 -or
        ($ReceiptRaw.Length -ge 3 -and $ReceiptRaw[0] -eq 0xEF -and
         $ReceiptRaw[1] -eq 0xBB -and $ReceiptRaw[2] -eq 0xBF)) {
        throw ('NEEDS_CONTEXT: invocation receipt is empty or has a BOM: ' + $Name)
    }
    [void]$StrictUtf8.GetString($ReceiptRaw)
    return [pscustomobject][ordered]@{
        path = (Resolve-Path -LiteralPath $ReceiptPath).Path
        bytes = [long]$ReceiptRaw.Length
        sha256 = (Get-FileHash -LiteralPath $ReceiptPath -Algorithm SHA256).Hash
    }
}

function Invoke-HeadlessTerminalCollapseSuite {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)][ValidatePattern('^[A-Za-z0-9_.-]+$')][string]$EvidenceName,
        [Parameter()][ValidateSet('Suite', 'Lint')][string]$Mode = 'Suite',
        [Parameter()][string]$Suite,
        [Parameter()][ValidateSet('PASSED', 'FAILED')][string]$Expect,
        [Parameter()][string]$ExpectedPattern,
        [Parameter(Mandatory = $true)][ValidateRange(1, 1800)][int]$TimeoutSeconds,
        [Parameter(Mandatory = $true)][ValidateNotNullOrEmpty()][string[]]$ExpectedPaths
    )

    if ($Mode -ceq 'Suite') {
        if ([string]::IsNullOrWhiteSpace($Suite) -or [string]::IsNullOrWhiteSpace($Expect)) {
            throw 'Suite mode requires Suite and Expect.'
        }
        if ($Expect -ceq 'FAILED' -and [string]::IsNullOrWhiteSpace($ExpectedPattern)) {
            throw 'A FAILED suite expectation requires ExpectedPattern.'
        }
    } elseif ($PSBoundParameters.ContainsKey('Suite') -or
        $PSBoundParameters.ContainsKey('Expect') -or
        $PSBoundParameters.ContainsKey('ExpectedPattern')) {
        throw 'Lint mode forbids Suite, Expect, and ExpectedPattern.'
    }
    foreach ($HelperPath in @($RunnerSource, $HeadlessWrapper)) {
        $CurrentHash = (Get-FileHash -LiteralPath $HelperPath -Algorithm SHA256).Hash
        $ExpectedHash = [string]$Task2HelperHashes[(Split-Path $HelperPath -Leaf)]
        $ExpectedBytes = [long]$ExpectedTask2HelperHashes[(Split-Path $HelperPath -Leaf)].Bytes
        if ($CurrentHash -cne $ExpectedHash -or (Get-Item -LiteralPath $HelperPath).Length -ne $ExpectedBytes) {
            throw ('NEEDS_CONTEXT: helper drifted after Task 2 binding; do not launch or retry: ' + $HelperPath)
        }
    }

    $InvocationId = $EvidenceName
    $MirrorRoot = New-Task2TestMirror -Name $EvidenceName -ExpectedPaths $ExpectedPaths
    $RunnerPath = Join-Path $MirrorRoot 'Tools\Run-RenPySuite.ps1'
    if (-not (Test-Path -LiteralPath $RunnerPath -PathType Leaf) -or
        (Get-FileHash -LiteralPath $RunnerPath -Algorithm SHA256).Hash -cne $RunnerTemplateHash -or
        (Get-FileHash -LiteralPath $RunnerTemplatePath -Algorithm SHA256).Hash -cne $RunnerTemplateHash -or
        (Test-Path -LiteralPath (Join-Path $MirrorRoot 'game\saves'))) {
        throw ('NEEDS_CONTEXT: Task 2 mirror runner or local-save preflight failed: ' + $MirrorRoot)
    }
    $SaveDir = Join-Path $Task2SaveRoot ('save-' + $InvocationId)
    $HelperEvidenceDir = Join-Path $Task2EvidenceRoot ('private-desktop-' + $InvocationId)
    $RunnerEvidenceDir = Join-Path $Task2EvidenceRoot ('renpy-runner-' + $InvocationId)
    foreach ($FreshPath in @($SaveDir, $HelperEvidenceDir, $RunnerEvidenceDir)) {
        if (Test-Path -LiteralPath $FreshPath) {
            throw ('NEEDS_CONTEXT: unique invocation path already exists; do not overwrite or retry: ' + $FreshPath)
        }
    }

    $Arguments = New-Object 'System.Collections.Generic.List[string]'
    foreach ($Argument in @(
        '-NoLogo',
        '-NoProfile',
        '-NonInteractive',
        '-ExecutionPolicy', 'Bypass',
        '-File', $RunnerPath,
        '-ProjectRoot', $MirrorRoot,
        '-SaveDir', $SaveDir,
        '-Mode', $Mode,
        '-EvidenceDir', $RunnerEvidenceDir,
        '-TimeoutSeconds', [string]$TimeoutSeconds
    )) {
        [void]$Arguments.Add([string]$Argument)
    }
    if ($Mode -ceq 'Suite') {
        [void]$Arguments.Add('-Suite')
        [void]$Arguments.Add($Suite)
        [void]$Arguments.Add('-Expect')
        [void]$Arguments.Add($Expect)
        if (-not [string]::IsNullOrWhiteSpace($ExpectedPattern)) {
            [void]$Arguments.Add('-ExpectedPattern')
            [void]$Arguments.Add($ExpectedPattern)
        }
    }

    $ParentHadSaveOverride = Test-Path Env:RENPY_PATH_TO_SAVES
    $ParentSaveOverride = if ($ParentHadSaveOverride) { $env:RENPY_PATH_TO_SAVES } else { $null }
    try {
        $Result = Invoke-PrivateDesktopProcess `
            -FilePath $PowerShellExe `
            -ArgumentList $Arguments.ToArray() `
            -WorkingDirectory $MirrorRoot `
            -EnvironmentOverrides @{
                SDL_VIDEODRIVER = 'dummy'
                SDL_AUDIODRIVER = 'dummy'
                RENPY_RENDERER = 'sw'
                RENPY_SDK = $TrustedSdkRoot
                RENPY_PATH_TO_SAVES = $null
                TEMP = $TaskTempRoot
                TMP = $TaskTempRoot
            } `
            -TimeoutSeconds ($TimeoutSeconds + 60) `
            -EvidenceDirectory $HelperEvidenceDir `
            -RunnerSource $RunnerSource
    } catch {
        throw ('NEEDS_CONTEXT: private-desktop launch failed; preserve ' + $HelperEvidenceDir + ' and do not retry. ' + $_.Exception.Message)
    }

    $ParentStillHasSaveOverride = Test-Path Env:RENPY_PATH_TO_SAVES
    if ($ParentStillHasSaveOverride -ne $ParentHadSaveOverride -or
        ($ParentHadSaveOverride -and $env:RENPY_PATH_TO_SAVES -cne $ParentSaveOverride)) {
        throw 'NEEDS_CONTEXT: child environment isolation changed the parent RENPY_PATH_TO_SAVES; do not retry.'
    }
    if ($null -eq $Result) {
        throw ('NEEDS_CONTEXT: private-desktop wrapper returned no result; preserve ' + $HelperEvidenceDir + ' and do not retry.')
    }
    try {
        Assert-PrivateDesktopSafetyEnvelope -Result $Result
    } catch {
        throw ('NEEDS_CONTEXT: reusable schema-v2 safety envelope failed; preserve ' + $HelperEvidenceDir + ' and do not retry. ' + $_.Exception.Message)
    }
    if (-not (Test-PrivateDesktopIntegralValue $Result.root_exit_code)) {
        throw ('NEEDS_CONTEXT: headless suite returned null/non-integral root_exit_code; preserve ' + $HelperEvidenceDir + ' and do not retry.')
    }
    if ([string]$Result.classification -cne 'COMPLETED' -or
        [int]$Result.helper_exit_code -ne 0 -or [bool]$Result.timed_out -or
        @($Result.visible_windows).Count -ne 0 -or [int64]$Result.root_exit_code -ne 0) {
        throw ('NEEDS_CONTEXT: headless suite gates failed; preserve ' + $HelperEvidenceDir + ' and ' + $RunnerEvidenceDir + '; do not retry. Classification=' + [string]$Result.classification + '; detail=' + [string]$Result.detail)
    }

    $HelperArtifacts = @(
        (Join-Path $HelperEvidenceDir 'request.json'),
        (Join-Path $HelperEvidenceDir 'stdout.txt'),
        (Join-Path $HelperEvidenceDir 'stderr.txt'),
        (Join-Path $HelperEvidenceDir 'result.json')
    )
    foreach ($EvidencePath in $HelperArtifacts) {
        if (-not (Test-Path -LiteralPath $EvidencePath -PathType Leaf)) {
            throw ('NEEDS_CONTEXT: helper evidence is incomplete; preserve the invocation and do not retry: ' + $EvidencePath)
        }
        git check-ignore -q -- $EvidencePath
        if ($LASTEXITCODE -ne 0) { throw ('NEEDS_CONTEXT: helper evidence is not ignored: ' + $EvidencePath) }
    }
    $Request = [IO.File]::ReadAllText($HelperArtifacts[0], $StrictUtf8) | ConvertFrom-Json -ErrorAction Stop
    $ExpectedChildEnvironment = [ordered]@{
        SDL_VIDEODRIVER = 'dummy'
        SDL_AUDIODRIVER = 'dummy'
        RENPY_RENDERER = 'sw'
        RENPY_SDK = $TrustedSdkRoot
        RENPY_PATH_TO_SAVES = $null
        TEMP = $TaskTempRoot
        TMP = $TaskTempRoot
    }
    foreach ($EnvironmentName in $ExpectedChildEnvironment.Keys) {
        $EnvironmentRows = @($Request.environment_overrides | Where-Object { [string]$_.name -ceq $EnvironmentName })
        if ($EnvironmentRows.Count -ne 1) {
            throw ('NEEDS_CONTEXT: request evidence does not contain exactly one ' + $EnvironmentName + ' override; do not retry.')
        }
        $ExpectedValue = $ExpectedChildEnvironment[$EnvironmentName]
        if (($null -eq $ExpectedValue -and $null -ne $EnvironmentRows[0].value) -or
            ($null -ne $ExpectedValue -and [string]$EnvironmentRows[0].value -cne [string]$ExpectedValue)) {
            throw ('NEEDS_CONTEXT: request evidence has the wrong ' + $EnvironmentName + ' value; do not retry.')
        }
    }
    $RunnerExtension = if ($Mode -ceq 'Suite') { '*.log' } else { '*.txt' }
    $RunnerOutputs = @(Get-ChildItem -LiteralPath $RunnerEvidenceDir -File -Filter $RunnerExtension)
    if ($RunnerOutputs.Count -ne 1) {
        throw ('NEEDS_CONTEXT: expected exactly one preserved ' + $Mode + ' output; preserve the invocation and do not retry: ' + $RunnerEvidenceDir)
    }
    $InvocationKind = if ($Mode -ceq 'Suite') { 'suite' } else { 'lint' }
    $InvocationExpected = if ($Mode -ceq 'Suite') { $Expect } else { 'PASS' }
    $InvocationActual = 'PASS'
    if ($Mode -ceq 'Suite') {
        $RunnerOutputText = [IO.File]::ReadAllText($RunnerOutputs[0].FullName, $StrictUtf8)
        $StatusMatches = [regex]::Matches($RunnerOutputText, '(?m)^\[rpytest\] Status:\s+([A-Z ]+?)\s*$')
        if ($StatusMatches.Count -ne 1) {
            throw ('NEEDS_CONTEXT: preserved runner output has no unique status; do not retry: ' + $RunnerOutputs[0].FullName)
        }
        $InvocationActual = $StatusMatches[0].Groups[1].Value.Trim()
        if ($InvocationActual -cne $Expect) {
            throw ('NEEDS_CONTEXT: preserved runner status does not match ' + $Expect + '; do not retry: ' + $RunnerOutputs[0].FullName)
        }
    }
    foreach ($EvidencePath in @($RunnerEvidenceDir, $RunnerOutputs[0].FullName)) {
        git check-ignore -q -- $EvidencePath
        if ($LASTEXITCODE -ne 0) { throw ('NEEDS_CONTEXT: runner evidence is not ignored: ' + $EvidencePath) }
    }

    $EvidenceHashes = [ordered]@{}
    foreach ($EvidencePath in @($HelperArtifacts + $RunnerOutputs[0].FullName)) {
        $EvidenceHashes[$EvidencePath] = (Get-FileHash -LiteralPath $EvidencePath -Algorithm SHA256).Hash
    }

    # The helper has proved the complete process tree drained. Only now remove
    # the exact task-owned mirror, including its engine-created local saves.
    Remove-VerifiedTask2Mirror -MirrorRoot $MirrorRoot -ExpectedPaths $ExpectedPaths

    # Seal the facts while this invocation's validated files are still the
    # exact bytes just observed. Later steps consume this receipt; they do not
    # reconstruct actual/verdict values from in-memory assumptions.
    $Receipt = New-Task2InvocationReceipt `
        -Name $EvidenceName `
        -Kind $InvocationKind `
        -Expected $InvocationExpected `
        -Actual $InvocationActual `
        -HelperEvidenceDir $HelperEvidenceDir `
        -RunnerOrScannerEvidenceDir $RunnerEvidenceDir `
        -DirectEvidencePaths @($RunnerOutputs[0].FullName)

    $Result | Add-Member -NotePropertyName invocation_name -NotePropertyValue $EvidenceName
    $Result | Add-Member -NotePropertyName test_mirror_path -NotePropertyValue $MirrorRoot
    $Result | Add-Member -NotePropertyName test_mirror_removed -NotePropertyValue $true
    $Result | Add-Member -NotePropertyName save_dir -NotePropertyValue $SaveDir
    $Result | Add-Member -NotePropertyName helper_evidence_dir -NotePropertyValue $HelperEvidenceDir
    $Result | Add-Member -NotePropertyName runner_evidence_dir -NotePropertyValue $RunnerEvidenceDir
    $Result | Add-Member -NotePropertyName runner_output -NotePropertyValue $RunnerOutputs[0].FullName
    $Result | Add-Member -NotePropertyName runner_output_sha256 -NotePropertyValue $EvidenceHashes[$RunnerOutputs[0].FullName]
    $Result | Add-Member -NotePropertyName evidence_sha256 -NotePropertyValue $EvidenceHashes
    $Result | Add-Member -NotePropertyName receipt_path -NotePropertyValue $Receipt.path
    $Result | Add-Member -NotePropertyName receipt_bytes -NotePropertyValue $Receipt.bytes
    $Result | Add-Member -NotePropertyName receipt_sha256 -NotePropertyValue $Receipt.sha256
    return $Result
}

$RedResult = Invoke-HeadlessTerminalCollapseSuite `
    -EvidenceName 'rules-red' `
    -Suite 'test_terminal_collapse_rules' `
    -Expect 'FAILED' `
    -ExpectedPattern 'is_terminal_resistance_collapse' `
    -TimeoutSeconds 120 `
    -ExpectedPaths @('game/test_game.rpy')
$RedResult | Format-List invocation_name, classification, helper_exit_code, root_pid, root_exit_code, job_total_processes, observed_distinct_process_id_count, process_id_accounting_kind, process_diagnostic_errors, private_desktop_initially_empty, monitor_armed_before_create, monitor_armed_before_resume, root_assigned_to_job_before_resume, job_kill_on_close_verified, job_breakaway_forbidden, job_handle_non_inheritable, job_active_processes_final, job_drained, monitor_completed_after_job_drain, host_termination_required, cleanup_complete, visible_windows, desktop_name, test_mirror_path, test_mirror_removed, save_dir, helper_evidence_dir, runner_evidence_dir, runner_output, runner_output_sha256
```

Expected: the Ren'Py suite fails for the missing `is_terminal_resistance_collapse` helper, while the runner root exits `0` because that exact RED was required. `$RedResult` must pass the reusable schema-v2 safety envelope and the separate `COMPLETED` / no-timeout / zero-window / expected-root-exit gates. Its PID/count/error values remain diagnostics and may not be called complete coverage. Preserve its create-new helper request/stdout/stderr/result report, unique external save directory, and unique runner evidence directory exactly where recorded; hash the runner log and do not edit, copy, rerun, or replace it.

- [ ] **Step 3: Replace the mapper and current-state wrappers in `game/difficulty.rpy`**

Replace `get_finale_ending_availability`, `get_current_finale_route_availability`, and `get_current_resistance_battle_outcomes` with this complete block; place the two collapse helpers between the mapper and current-route wrapper:

```python
    def get_finale_ending_availability(routes, resistance_outcomes=None):
        """Map visible routes to persistent outcomes the player can actually reach."""
        battle_route_visible = bool(routes.get("iron_lord") or routes.get("resist"))
        if battle_route_visible and resistance_outcomes is None:
            raise ValueError(
                "resistance_outcomes is required when an iron_lord or resist route is visible"
            )

        resistance_outcomes = resistance_outcomes or {}
        return {
            "iron_lord": bool(
                battle_route_visible and resistance_outcomes.get("iron_lord")
            ),
            "shadow_king": bool(routes.get("shadow_king")),
            "holy_guardian": bool(routes.get("holy_guardian")),
            "peoples_lord": bool(routes.get("peoples_lord")),
            "truth": bool(routes.get("truth")),
            "borgia": bool(routes.get("borgia")),
            "vassal": bool(routes.get("vassal")),
            "fall": bool(routes.get("fall") or (
                battle_route_visible and resistance_outcomes.get("fall")
            )),
            "sea": bool(routes.get("sea")),
        }

    def is_terminal_resistance_collapse(
            wealth, loyalty, built_granary,
            alliance_baron, baron_joined,
            prince_ally, prince_betrayed, rel_captain,
            ch5_pay_advance_pension, marriage_route,
            iron_thorn_controlled):
        """Pure hard floor for a materially and organizationally collapsed army."""
        return bool(
            wealth < 20
            and loyalty < 20
            and not built_granary
            and not alliance_baron
            and not baron_joined
            and not (prince_ally and not prince_betrayed)
            and rel_captain < 60
            and not ch5_pay_advance_pension
            and not marriage_route
            and not iron_thorn_controlled
        )

    def get_current_finale_route_availability():
        """用当前存档状态调用统一终章路线判定。"""
        return get_finale_route_availability(
            power=getattr(store, "power", 0),
            intrigue=getattr(store, "intrigue", 0),
            faith=getattr(store, "faith", 0),
            loyalty=getattr(store, "loyalty", 0),
            difficulty=persistent.difficulty or "normal",
            lily_full_member=getattr(store, "lily_full_member", False),
            rel_queen=getattr(store, "rel_queen", 0),
            rel_baron=getattr(store, "rel_baron", 0),
            father_poison_method_known=getattr(store, "father_poison_method_known", False),
            father_poison_executor_known=getattr(store, "father_poison_executor_known", False),
            father_murder_mastermind_known=getattr(store, "father_murder_mastermind_known", False),
            testament_original_obtained=getattr(store, "testament_original_obtained", False),
            deep_mother_herb=getattr(store, "deep_mother_herb", ""),
            poison_evidence=getattr(store, "poison_evidence", False),
            southern_outcome=getattr(store, "southern_outcome", "none"),
        )

    def is_current_terminal_resistance_collapse():
        """Evaluate the current save through the pure terminal-collapse rule."""
        return is_terminal_resistance_collapse(
            wealth=getattr(store, "wealth", 0),
            loyalty=getattr(store, "loyalty", 0),
            built_granary=getattr(store, "built_granary", False),
            alliance_baron=getattr(store, "alliance_baron", False),
            baron_joined=getattr(store, "resist_route", False),
            prince_ally=getattr(store, "prince_ally", False),
            prince_betrayed=getattr(store, "prince_betrayed", False),
            rel_captain=getattr(store, "rel_captain", 0),
            ch5_pay_advance_pension=getattr(store, "ch5_pay_advance_pension", False),
            marriage_route=getattr(store, "marriage_route", False),
            iron_thorn_controlled=getattr(store, "iron_thorn_controlled", False),
        )

    def get_current_resistance_battle_outcomes():
        """Evaluate reachable resistance outcomes from the current save."""
        routes = get_current_finale_route_availability()
        return get_resistance_battle_outcomes(
            power=getattr(store, "power", 0),
            intrigue=getattr(store, "intrigue", 0),
            faith=getattr(store, "faith", 0),
            loyalty=getattr(store, "loyalty", 0),
            wealth=getattr(store, "wealth", 0),
            difficulty=persistent.difficulty or "normal",
            built_granary=getattr(store, "built_granary", False),
            alliance_baron=getattr(store, "alliance_baron", False),
            rel_baron=getattr(store, "rel_baron", 0),
            prince_ally=getattr(store, "prince_ally", False),
            prince_betrayed=getattr(store, "prince_betrayed", False),
            rel_captain=getattr(store, "rel_captain", 0),
            ch5_pay_advance_pension=getattr(store, "ch5_pay_advance_pension", False),
            marriage_route=getattr(store, "marriage_route", False),
            iron_thorn_controlled=getattr(store, "iron_thorn_controlled", False),
            baron_supply_intel=getattr(store, "baron_supply_intel", False),
            iron_route_available=routes["iron_lord"],
            resist_route_available=routes["resist"],
        )
```

- [ ] **Step 4: Add the pure relationship projection and replace the battle enumerator**

Place `_difficulty_adjusted_rel_value` immediately after `_difficulty_adjusted_stat_value`, then replace `get_resistance_battle_outcomes` completely:

```python
    def _difficulty_adjusted_rel_value(current, delta, difficulty):
        """Pure equivalent of one change_rel call at a specified difficulty."""
        cfg = _difficulty_config.get(
            difficulty or "normal",
            _difficulty_config["normal"],
        )
        if delta > 0:
            adjusted = int(delta * cfg["positive"])
        elif delta < 0:
            adjusted = int(delta * cfg["negative"])
        else:
            adjusted = 0

        if adjusted == 0 and delta != 0:
            adjusted = 1 if delta > 0 else -1
        return max(-100, min(100, current + adjusted))

    def get_resistance_battle_outcomes(
            power=0, intrigue=0, faith=0, loyalty=0, wealth=0,
            difficulty="normal", built_granary=False,
            alliance_baron=False, rel_baron=0,
            prince_ally=False, prince_betrayed=False, rel_captain=0,
            ch5_pay_advance_pension=False, marriage_route=False,
            iron_thorn_controlled=False, baron_supply_intel=False,
            *, iron_route_available, resist_route_available):
        """Purely enumerate reachable win/loss outcomes of the chapter-five battle."""
        difficulty = difficulty or "normal"
        score = (
            max(0, power - 30) // 4
            + max(0, intrigue - 30) // 6
            + max(0, loyalty - 30) // 8
        )
        if alliance_baron:
            score += 10
        elif rel_baron > 0:
            score += 4
        if prince_ally and not prince_betrayed:
            score += 5
        if rel_captain >= 60:
            score += 3
        if ch5_pay_advance_pension:
            score += 3
        if marriage_route:
            score += 5
        if iron_thorn_controlled:
            score += 3

        if power >= 70:
            power = _difficulty_adjusted_stat_value(power, 3, difficulty)

        plans = []
        if faith >= 60:
            plans.append((
                power,
                intrigue,
                _difficulty_adjusted_stat_value(faith, 5, difficulty),
                _difficulty_adjusted_stat_value(loyalty, 3, difficulty),
                wealth,
                rel_captain,
                score + 4,
            ))

        plans.append((
            power,
            _difficulty_adjusted_stat_value(intrigue, 5, difficulty),
            faith,
            _difficulty_adjusted_stat_value(loyalty, -4, difficulty),
            wealth,
            rel_captain,
            score + 6 + (3 if baron_supply_intel else 0),
        ))

        if wealth >= 40:
            plans.append((
                power,
                _difficulty_adjusted_stat_value(intrigue, 3, difficulty),
                faith,
                loyalty,
                _difficulty_adjusted_stat_value(wealth, -10, difficulty),
                rel_captain,
                score + 6,
            ))

        if power >= 55:
            plans.append((
                _difficulty_adjusted_stat_value(power, 3, difficulty),
                _difficulty_adjusted_stat_value(intrigue, 3, difficulty),
                faith,
                loyalty,
                wealth,
                _difficulty_adjusted_rel_value(rel_captain, -10, difficulty),
                score + 8,
            ))

        baron_joined_states = []
        if iron_route_available:
            baron_joined_states.append(False)
        if resist_route_available:
            baron_joined_states.append(True)

        outcomes = {"iron_lord": False, "fall": False}
        grind_threshold = 12 + _war_threshold_mod.get(difficulty, 0)

        for (
                plan_power,
                plan_intrigue,
                _plan_faith,
                plan_loyalty,
                plan_wealth,
                plan_rel_captain,
                plan_score) in plans:
            skirmishes = [
                (
                    _difficulty_adjusted_stat_value(plan_power, 5, difficulty),
                    plan_intrigue,
                    plan_loyalty,
                    plan_wealth,
                    _difficulty_adjusted_rel_value(
                        plan_rel_captain,
                        -12,
                        difficulty,
                    ),
                    plan_score,
                ),
                (
                    _difficulty_adjusted_stat_value(plan_power, 2, difficulty),
                    _difficulty_adjusted_stat_value(plan_intrigue, 3, difficulty),
                    plan_loyalty,
                    plan_wealth,
                    _difficulty_adjusted_rel_value(
                        plan_rel_captain,
                        4,
                        difficulty,
                    ),
                    plan_score + 3,
                ),
            ]

            for (
                    skirmish_power,
                    skirmish_intrigue,
                    skirmish_loyalty,
                    skirmish_wealth,
                    skirmish_rel_captain,
                    skirmish_score) in skirmishes:
                villages = []
                if skirmish_loyalty >= 70:
                    villages.append((
                        _difficulty_adjusted_stat_value(
                            skirmish_power,
                            -6,
                            difficulty,
                        ),
                        skirmish_intrigue,
                        _difficulty_adjusted_stat_value(
                            skirmish_loyalty,
                            5,
                            difficulty,
                        ),
                        skirmish_wealth,
                        skirmish_rel_captain,
                        skirmish_score,
                    ))

                villages.extend([
                    (
                        _difficulty_adjusted_stat_value(
                            skirmish_power,
                            -1,
                            difficulty,
                        ),
                        skirmish_intrigue,
                        _difficulty_adjusted_stat_value(
                            skirmish_loyalty,
                            3,
                            difficulty,
                        ),
                        skirmish_wealth,
                        skirmish_rel_captain,
                        skirmish_score - 3,
                    ),
                    (
                        _difficulty_adjusted_stat_value(
                            skirmish_power,
                            2,
                            difficulty,
                        ),
                        skirmish_intrigue,
                        _difficulty_adjusted_stat_value(
                            skirmish_loyalty,
                            -5,
                            difficulty,
                        ),
                        skirmish_wealth,
                        skirmish_rel_captain,
                        skirmish_score,
                    ),
                ])

                for (
                        final_power,
                        final_intrigue,
                        final_loyalty,
                        final_wealth,
                        final_rel_captain,
                        final_score) in villages:
                    prepared = (
                        final_power >= 60
                        or final_intrigue >= 55
                        or (
                            final_intrigue >= 45
                            and final_loyalty >= 50
                        )
                    )

                    for baron_joined in baron_joined_states:
                        collapsed = is_terminal_resistance_collapse(
                            wealth=final_wealth,
                            loyalty=final_loyalty,
                            built_granary=built_granary,
                            alliance_baron=alliance_baron,
                            baron_joined=baron_joined,
                            prince_ally=prince_ally,
                            prince_betrayed=prince_betrayed,
                            rel_captain=final_rel_captain,
                            ch5_pay_advance_pension=ch5_pay_advance_pension,
                            marriage_route=marriage_route,
                            iron_thorn_controlled=iron_thorn_controlled,
                        )
                        if collapsed:
                            outcomes["fall"] = True
                        elif prepared or final_score >= grind_threshold:
                            outcomes["iron_lord"] = True
                        else:
                            outcomes["fall"] = True

                        if outcomes["iron_lord"] and outcomes["fall"]:
                            return outcomes

        return outcomes
```

- [ ] **Step 5: Migrate the ending catalog without weakening route visibility**

Replace `ending_availability_is_an_exact_nine_key_outcome_map` completely:

```renpy
    testcase ending_availability_is_an_exact_nine_key_outcome_map:
        parameter (route_kwargs, resistance_kwargs, expected_endings) = [
            (
                {"difficulty": "hard", "power": 72},
                {"difficulty": "hard", "power": 72, "wealth": 20, "iron_route_available": True, "resist_route_available": False},
                {"iron_lord": True, "shadow_king": False, "holy_guardian": False, "peoples_lord": False, "truth": False, "borgia": False, "vassal": False, "fall": False, "sea": False},
            ),
            (
                {"difficulty": "normal", "power": 55, "rel_baron": -1, "rel_queen": -1},
                {"difficulty": "normal", "power": 55, "rel_baron": -1, "iron_route_available": True, "resist_route_available": False},
                {"iron_lord": False, "shadow_king": False, "holy_guardian": False, "peoples_lord": False, "truth": False, "borgia": False, "vassal": False, "fall": True, "sea": False},
            ),
            (
                {"difficulty": "hard", "rel_baron": 30},
                {"difficulty": "hard", "rel_baron": 30, "iron_route_available": False, "resist_route_available": True},
                {"iron_lord": False, "shadow_king": False, "holy_guardian": False, "peoples_lord": False, "truth": False, "borgia": False, "vassal": False, "fall": True, "sea": False},
            ),
            (
                {"difficulty": "hard", "rel_baron": 30},
                {"difficulty": "hard", "rel_baron": 30, "alliance_baron": True, "baron_supply_intel": True, "iron_route_available": False, "resist_route_available": True},
                {"iron_lord": True, "shadow_king": False, "holy_guardian": False, "peoples_lord": False, "truth": False, "borgia": False, "vassal": False, "fall": False, "sea": False},
            ),
            (
                {"difficulty": "hard", "power": 72, "rel_baron": -1, "rel_queen": -1},
                {"difficulty": "hard", "power": 72, "rel_baron": -1, "baron_supply_intel": True, "iron_route_available": True, "resist_route_available": False},
                {"iron_lord": False, "shadow_king": False, "holy_guardian": False, "peoples_lord": False, "truth": False, "borgia": False, "vassal": False, "fall": True, "sea": False},
            ),
            (
                {"difficulty": "hard", "southern_outcome": "free"},
                None,
                {"iron_lord": False, "shadow_king": False, "holy_guardian": False, "peoples_lord": False, "truth": False, "borgia": False, "vassal": False, "fall": True, "sea": True},
            ),
        ]

        $ _exact_routes = get_finale_route_availability(**route_kwargs)
        $ _resistance_outcomes = None if resistance_kwargs is None else get_resistance_battle_outcomes(**resistance_kwargs)
        $ _exact_endings = get_finale_ending_availability(_exact_routes, _resistance_outcomes)
        assert eval (_exact_endings == expected_endings)
        assert eval (set(_exact_endings.keys()) == set(_ending_keys))
```

Replace `primary_routes_use_configured_thresholds` so it proves visibility only:

```renpy
    testcase primary_routes_use_configured_thresholds:
        parameter (difficulty_name, stat_name, ending_id) = [
            ("easy", "power", "iron_lord"),
            ("easy", "intrigue", "shadow_king"),
            ("easy", "faith", "holy_guardian"),
            ("easy", "loyalty", "peoples_lord"),
            ("normal", "power", "iron_lord"),
            ("normal", "intrigue", "shadow_king"),
            ("normal", "faith", "holy_guardian"),
            ("normal", "loyalty", "peoples_lord"),
            ("hard", "power", "iron_lord"),
            ("hard", "intrigue", "shadow_king"),
            ("hard", "faith", "holy_guardian"),
            ("hard", "loyalty", "peoples_lord"),
        ]

        $ _threshold = _ending_threshold_config[difficulty_name]["primary"]
        $ _route_kwargs = {"difficulty": difficulty_name, stat_name: _threshold}
        $ _ending_routes = get_finale_route_availability(**_route_kwargs)
        assert eval (_ending_routes[ending_id])
```

Keep `special_routes_map_to_real_endings` as a legitimate one-argument mapper test: its hard-difficulty rows expose no `iron_lord` or `resist` battle route.

- [ ] **Step 6: Migrate the winter invariance callers with explicit route flags**

In `every_core_and_delegated_result_preserves_forbidden_state`, replace the route/battle setup with:

```renpy
        $ _winter_route_kwargs = {"difficulty": "hard", "power": 72, "father_murder_mastermind_known": True, "testament_original_obtained": True, "southern_outcome": "free"}
        $ _winter_routes_before = get_finale_route_availability(**_winter_route_kwargs)
        python:
            _winter_battle_kwargs = {
                "difficulty": "hard",
                "power": 72,
                "built_granary": False,
                "alliance_baron": True,
                "rel_baron": 30,
                "prince_betrayed": False,
                "baron_supply_intel": True,
                "iron_route_available": _winter_routes_before["iron_lord"],
                "resist_route_available": _winter_routes_before["resist"],
            }
        $ _winter_battle_before = get_resistance_battle_outcomes(**_winter_battle_kwargs)
        $ _winter_endings_before = get_finale_ending_availability(_winter_routes_before, _winter_battle_before)
```

Keep its later route, battle, and ending equality assertions. Do not add `built_granary` to `_test_winter_capture_invariance().resistance_inputs`: winter delivery is authorized to change that variable, and the purpose of this test is to prove that the selected non-collapse fixture keeps its result graph stable.

Replace `easy_normal_hard_boundary_route_sets_are_identical` completely:

```renpy
    testcase easy_normal_hard_boundary_route_sets_are_identical:
        parameter (difficulty_name, main_value) = [
            ("easy", 54), ("easy", 55), ("easy", 56),
            ("normal", 64), ("normal", 65), ("normal", 66),
            ("hard", 71), ("hard", 72), ("hard", 73),
        ]

        $ _winter_route_kwargs = {"difficulty": difficulty_name, "power": main_value}
        $ _winter_routes_before = get_finale_route_availability(**_winter_route_kwargs)
        $ finalize_winter_interlude("ration", "feed_now", ("village", "granary"))
        assert eval (get_finale_route_availability(**_winter_route_kwargs) == _winter_routes_before)
```

Keep `truth_lily_borgia_sea_fall_sets_are_identical` unchanged: every row lacks an iron/resist battle route and is a valid one-argument mapper use.

Replace `resistance_battle_outcomes_are_identical` completely:

```renpy
    testcase resistance_battle_outcomes_are_identical:
        parameter battle_kwargs = [
            {"difficulty": "easy", "power": 40, "intrigue": 35, "loyalty": 35, "built_granary": False, "prince_betrayed": False, "iron_route_available": False, "resist_route_available": True},
            {"difficulty": "normal", "power": 55, "intrigue": 45, "loyalty": 50, "built_granary": False, "prince_betrayed": False, "iron_route_available": True, "resist_route_available": True},
            {"difficulty": "hard", "power": 72, "built_granary": False, "prince_betrayed": False, "iron_route_available": True, "resist_route_available": False},
            {"difficulty": "hard", "rel_baron": 30, "built_granary": False, "prince_betrayed": False, "iron_route_available": False, "resist_route_available": True},
            {"difficulty": "hard", "alliance_baron": True, "rel_baron": 30, "baron_supply_intel": True, "built_granary": False, "prince_betrayed": False, "iron_route_available": False, "resist_route_available": True},
            {"difficulty": "hard", "prince_ally": True, "prince_betrayed": False, "rel_captain": 60, "ch5_pay_advance_pension": True, "marriage_route": True, "iron_thorn_controlled": True, "built_granary": False, "iron_route_available": True, "resist_route_available": False},
        ]

        $ _winter_battle_before = get_resistance_battle_outcomes(**battle_kwargs)
        $ finalize_winter_interlude("trade", "feed_now", ("market", "granary"))
        assert eval (get_resistance_battle_outcomes(**battle_kwargs) == _winter_battle_before)
```

- [ ] **Step 7: Align the developer balance report with reachable outcomes**

In `game/balance.rpy`, replace the `iron_lord` requirement literal only:

```renpy
        "iron_lord": {
            "name": "铁腕领主",
            "icon": "剑",
            "color": "#e74c3c",
            "desc": "以武力征服一切",
            "requirement": "铁腕或抵抗路线可选，且会战存在胜利路径",
            "stat": "power",
        },
```

In `test_balance_ending_report`, replace the store-name and default assignments with:

```renpy
        $ _test.balance_report_store_names = ("power", "intrigue", "faith", "loyalty", "wealth", "built_granary", "rel_baron", "rel_queen", "lily_full_member", "father_poison_method_known", "father_poison_executor_known", "father_murder_mastermind_known", "testament_original_obtained", "deep_mother_herb", "poison_evidence", "southern_outcome", "alliance_baron", "prince_ally", "prince_betrayed", "rel_captain", "ch5_pay_advance_pension", "marriage_route", "iron_thorn_controlled", "baron_supply_intel")
        $ _test.balance_report_defaults = {"power": 0, "intrigue": 0, "faith": 0, "loyalty": 0, "wealth": 0, "built_granary": False, "rel_baron": -1, "rel_queen": -1, "lily_full_member": False, "father_poison_method_known": False, "father_poison_executor_known": False, "father_murder_mastermind_known": False, "testament_original_obtained": False, "deep_mother_herb": "", "poison_evidence": False, "southern_outcome": "none", "alliance_baron": False, "prince_ally": False, "prince_betrayed": False, "rel_captain": 0, "ch5_pay_advance_pension": False, "marriage_route": False, "iron_thorn_controlled": False, "baron_supply_intel": False}
```

Replace the old normal direct-iron report testcase:

```renpy
    testcase normal_direct_iron_collapse_report_has_only_loss:
        $ persistent.difficulty = "normal"
        $ power = 55
        $ _balance_report = {row[0]: row for row in check_ending_reachability()}
        assert eval (not _balance_report["iron_lord"][2])
        assert eval (_balance_report["fall"][2])
        assert eval (_balance_report["iron_lord"][3] == "铁腕会战当前没有胜利路径")
        assert eval (_balance_report["fall"][3] == "已满足条件")
        assert eval (_ending_requirements["iron_lord"]["requirement"] == "铁腕或抵抗路线可选，且会战存在胜利路径")
        assert eval (_ending_requirements["fall"]["desc"] == "未能守住艾登堡（失败结局）")
        assert eval (_ending_requirements["fall"]["requirement"] == "没有其他核心路线可选，或铁腕会战存在战败路径")
```

- [ ] **Step 8: Prove every API caller has an explicit disposition**

```powershell
$MapperCalls = @(rg -n "get_finale_ending_availability\(" -g '*.rpy' -g '*.py' .)
$BattleCalls = @(rg -n "get_resistance_battle_outcomes\(" -g '*.rpy' -g '*.py' .)
if ($MapperCalls.Count -ne 12) { throw "Expected 12 mapper references after migration, found $($MapperCalls.Count)." }
if ($BattleCalls.Count -ne 17) { throw "Expected 17 battle references after migration, found $($BattleCalls.Count)." }
$MapperCalls
$BattleCalls
```

The exact disposition is:

- `game/balance.rpy`: passes current route-aware battle outcomes.
- `game/difficulty.rpy`: one definition; current wrapper supplies `built_granary`, `prince_betrayed`, and both route flags.
- `test_terminal_collapse_rules`: three mapper references and nine direct battle references encode the new public contract.
- `game/test_game.rpy` ending catalog: non-`None` battle dictionaries carry both flags.
- `primary_routes_use_configured_thresholds`: no mapper call; it proves route visibility only.
- `special_routes_map_to_real_endings`: one-argument mapper remains valid because those hard fixtures expose no battle route.
- `_test_winter_capture_invariance`: passes current route-aware battle outcomes.
- winter core/delegated invariance: both direct battle calls use `_winter_battle_kwargs` with flags derived from `_winter_routes_before`.
- winter boundary route test: no mapper call; it proves route invariance only.
- winter truth/lily/Borgia/sea/fall test: one-argument mapper remains valid because those fixtures expose no iron/resist route.
- winter battle invariance: both direct battle calls receive required flags in each parameter dictionary.
- There is no `.py` caller in the starting tree.

Do not weaken required flags with defaults to make an omitted caller pass.

- [ ] **Step 9: Run the focused GREEN suites, mandatory script scans, and lint once each**

```powershell
if ($null -eq (Get-Command Invoke-HeadlessTerminalCollapseSuite -CommandType Function -ErrorAction SilentlyContinue)) {
    throw 'NEEDS_CONTEXT: the bound Task 2 headless session is gone; do not launch or rerun any suite.'
}

$GreenPaths = @('game/balance.rpy', 'game/difficulty.rpy', 'game/test_game.rpy')
$RulesGreen = Invoke-HeadlessTerminalCollapseSuite -EvidenceName 'rules-green' -Suite 'test_terminal_collapse_rules' -Expect 'PASSED' -TimeoutSeconds 120 -ExpectedPaths $GreenPaths
$CatalogGreen = Invoke-HeadlessTerminalCollapseSuite -EvidenceName 'catalog-green' -Suite 'test_ending_catalog' -Expect 'PASSED' -TimeoutSeconds 120 -ExpectedPaths $GreenPaths
$BalanceGreen = Invoke-HeadlessTerminalCollapseSuite -EvidenceName 'balance-green' -Suite 'test_balance_ending_report' -Expect 'PASSED' -TimeoutSeconds 120 -ExpectedPaths $GreenPaths
$WinterGreen = Invoke-HeadlessTerminalCollapseSuite -EvidenceName 'winter-invariance-green' -Suite 'test_winter_interlude_ending_invariance' -Expect 'PASSED' -TimeoutSeconds 180 -ExpectedPaths $GreenPaths

foreach ($GreenResult in @($RulesGreen, $CatalogGreen, $BalanceGreen, $WinterGreen)) {
    $GreenResult | Format-List invocation_name, classification, helper_exit_code, root_pid, root_exit_code, job_total_processes, observed_distinct_process_id_count, process_id_accounting_kind, process_diagnostic_errors, private_desktop_initially_empty, monitor_armed_before_create, monitor_armed_before_resume, root_assigned_to_job_before_resume, job_kill_on_close_verified, job_breakaway_forbidden, job_handle_non_inheritable, job_active_processes_final, job_drained, monitor_completed_after_job_drain, host_termination_required, cleanup_complete, visible_windows, desktop_name, test_mirror_path, test_mirror_removed, save_dir, helper_evidence_dir, runner_evidence_dir, runner_output, runner_output_sha256
}

function Invoke-Task2ConsoleScanner {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)][ValidatePattern('^[A-Za-z0-9_.-]+$')][string]$Name,
        [Parameter(Mandatory = $true)][string]$MirrorRoot,
        [Parameter(Mandatory = $true)][string]$ScriptPath,
        [Parameter()][string]$ExpectedStdoutPattern,
        [Parameter()][string]$ForbiddenStdoutPattern,
        [Parameter()][switch]$RequireEmptyStdout,
        [Parameter()][string[]]$SourceEvidencePaths = @()
    )

    if (-not (Test-Path -LiteralPath $ScriptPath -PathType Leaf) -or $ScriptPath.Contains('"')) {
        throw ('NEEDS_CONTEXT: scanner path is missing or cannot be quoted safely: ' + $ScriptPath)
    }
    $ScannerEvidence = Join-Path $Task2EvidenceRoot ('scanner-' + $Name)
    if (Test-Path -LiteralPath $ScannerEvidence) {
        throw ('NEEDS_CONTEXT: scanner evidence already exists; do not overwrite or retry: ' + $ScannerEvidence)
    }
    git check-ignore -q -- $ScannerEvidence
    if ($LASTEXITCODE -ne 0) { throw ('NEEDS_CONTEXT: scanner evidence is not ignored: ' + $ScannerEvidence) }

    try {
        $ScannerRun = Invoke-PrivateDesktopProcess `
            -FilePath $Task2Python `
            -ArgumentList @('-B', $ScriptPath) `
            -WorkingDirectory $MirrorRoot `
            -EnvironmentOverrides @{
                PYTHONDONTWRITEBYTECODE = '1'
                PYTHONIOENCODING = 'utf-8'
                PYTHONUTF8 = '1'
                SDL_VIDEODRIVER = 'dummy'
                SDL_AUDIODRIVER = 'dummy'
                RENPY_RENDERER = 'sw'
                RENPY_PATH_TO_SAVES = $null
                TEMP = $TaskTempRoot
                TMP = $TaskTempRoot
            } `
            -TimeoutSeconds 120 `
            -EvidenceDirectory $ScannerEvidence `
            -RunnerSource $RunnerSource
    } catch {
        throw ('NEEDS_CONTEXT: private scanner launch failed; preserve evidence and do not retry: ' + $Name + '. ' + $_.Exception.Message)
    }
    try {
        Assert-PrivateDesktopSafetyEnvelope -Result $ScannerRun
    } catch {
        throw ('NEEDS_CONTEXT: scanner safety envelope failed; preserve evidence and do not retry: ' + $Name + '. ' + $_.Exception.Message)
    }
    if (-not (Test-PrivateDesktopIntegralValue $ScannerRun.root_exit_code)) {
        throw ('NEEDS_CONTEXT: scanner returned null/non-integral root_exit_code; preserve evidence and do not retry: ' + $Name)
    }
    if ([string]$ScannerRun.classification -cne 'COMPLETED' -or
        [int]$ScannerRun.helper_exit_code -ne 0 -or [bool]$ScannerRun.timed_out -or
        @($ScannerRun.visible_windows).Count -ne 0 -or [int64]$ScannerRun.root_exit_code -ne 0) {
        throw ('NEEDS_CONTEXT: scanner private completion gates failed; preserve evidence and do not retry: ' + $Name)
    }
    $StdoutPath = [string]$ScannerRun.stdout_path
    $StderrPath = [string]$ScannerRun.stderr_path
    $Stdout = [IO.File]::ReadAllText($StdoutPath, $StrictUtf8)
    $Stderr = [IO.File]::ReadAllText($StderrPath, $StrictUtf8)
    if (-not [string]::IsNullOrEmpty($Stderr) -or
        ($RequireEmptyStdout -and -not [string]::IsNullOrEmpty($Stdout)) -or
        (-not [string]::IsNullOrWhiteSpace($ExpectedStdoutPattern) -and
            [regex]::Matches($Stdout, $ExpectedStdoutPattern).Count -ne 1) -or
        (-not [string]::IsNullOrWhiteSpace($ForbiddenStdoutPattern) -and
            [regex]::IsMatch($Stdout, $ForbiddenStdoutPattern))) {
        throw ('NEEDS_CONTEXT: mandatory script scanner failed; preserve mirror and evidence and do not retry: ' + $Name)
    }

    $ScannerActual = 'PASS'
    $ReceiptDirectPaths = @($StdoutPath, $StderrPath) + @($SourceEvidencePaths)
    $Receipt = New-Task2InvocationReceipt `
        -Name $Name `
        -Kind 'scanner' `
        -Expected 'PASS' `
        -Actual $ScannerActual `
        -HelperEvidenceDir $ScannerEvidence `
        -RunnerOrScannerEvidenceDir $ScannerEvidence `
        -DirectEvidencePaths $ReceiptDirectPaths `
        -SourceEvidencePaths $SourceEvidencePaths

    return [pscustomobject]@{
        name = $Name
        process_id = $ScannerRun.root_pid
        exit_code = $ScannerRun.root_exit_code
        evidence_dir = $ScannerEvidence
        stdout_path = $StdoutPath
        stderr_path = $StderrPath
        result_sha256 = (Get-FileHash -LiteralPath (Join-Path $ScannerEvidence 'result.json') -Algorithm SHA256).Hash
        receipt_path = $Receipt.path
        receipt_bytes = $Receipt.bytes
        receipt_sha256 = $Receipt.sha256
    }
}

$Task2Python = Join-Path $TrustedSdkRoot 'lib\py3-windows-x86_64\python.exe'
if (-not (Test-Path -LiteralPath $Task2Python -PathType Leaf)) {
    throw ('NEEDS_CONTEXT: trusted SDK Python is missing: ' + $Task2Python)
}
$ScannerMirror = New-Task2TestMirror -Name 'script-scanners-green' -ExpectedPaths $GreenPaths
$MissingPortraitResult = Invoke-Task2ConsoleScanner `
    -Name 'missing-portraits-green' `
    -MirrorRoot $ScannerMirror `
    -ScriptPath (Join-Path $ScannerMirror 'scan_missing_portraits.py') `
    -ExpectedStdoutPattern '(?m)^=== Total findings: 0 ===\s*$' `
    -ForbiddenStdoutPattern '(?m)^!!'
$NarrationOverlapResult = Invoke-Task2ConsoleScanner `
    -Name 'narration-overlap-green' `
    -MirrorRoot $ScannerMirror `
    -ScriptPath (Join-Path $ScannerMirror 'scan_narration_overlap.py') `
    -ExpectedStdoutPattern '(?m)^TOTAL:\s+0\b.*$'

$ShowScanSourceDir = Join-Path $Task2EvidenceRoot 'scanner-show-before-source'
if (Test-Path -LiteralPath $ShowScanSourceDir) {
    throw ('NEEDS_CONTEXT: show-scan source already exists; do not overwrite or retry: ' + $ShowScanSourceDir)
}
New-Item -ItemType Directory -Path $ShowScanSourceDir -ErrorAction Stop | Out-Null
git check-ignore -q -- $ShowScanSourceDir
if ($LASTEXITCODE -ne 0) { throw ('NEEDS_CONTEXT: show-scan source is not ignored: ' + $ShowScanSourceDir) }
$ShowScanPath = Join-Path $ShowScanSourceDir 'show-before-scan.py'
$ShowScanSource = @'
import re
from pathlib import Path
for path in ["game/balance.rpy", "game/difficulty.rpy", "game/test_game.rpy"]:
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines):
        m = re.match(r'^(\s*)show\s+(\w+_img)\s+at\s+left\b', line)
        if not m: continue
        j = i - 1
        while j >= 0 and (not lines[j].strip() or lines[j].strip().startswith("#")): j -= 1
        prev = lines[j].strip() if j >= 0 else ""
        if not re.match(r'^(\$\s*hide_all_chars\s*\(|scene\s+bg\b|hide\s+\w+_img)', prev):
            print(f"{path}:L{i+1}  show {m.group(2)}  prev={prev!r}")
'@
Write-Task2CreateNewUtf8 -Path $ShowScanPath -Text ($ShowScanSource.Replace("`r`n", "`n") + "`n")
$ShowBeforeResult = Invoke-Task2ConsoleScanner `
    -Name 'show-before-green' `
    -MirrorRoot $ScannerMirror `
    -ScriptPath $ShowScanPath `
    -RequireEmptyStdout `
    -SourceEvidencePaths @($ShowScanPath)

foreach ($ScannerResult in @($MissingPortraitResult, $NarrationOverlapResult, $ShowBeforeResult)) {
    $ScannerResult | Format-List name, process_id, exit_code, evidence_dir, result_sha256
}
Remove-VerifiedTask2Mirror -MirrorRoot $ScannerMirror -ExpectedPaths $GreenPaths

$LintGreen = Invoke-HeadlessTerminalCollapseSuite `
    -EvidenceName 'lint-green' `
    -Mode 'Lint' `
    -TimeoutSeconds 180 `
    -ExpectedPaths $GreenPaths
$LintGreen | Format-List invocation_name, classification, helper_exit_code, root_pid, root_exit_code, job_total_processes, observed_distinct_process_id_count, process_id_accounting_kind, process_diagnostic_errors, private_desktop_initially_empty, monitor_armed_before_create, monitor_armed_before_resume, root_assigned_to_job_before_resume, job_kill_on_close_verified, job_breakaway_forbidden, job_handle_non_inheritable, job_active_processes_final, job_drained, monitor_completed_after_job_drain, host_termination_required, cleanup_complete, visible_windows, desktop_name, test_mirror_path, test_mirror_removed, save_dir, helper_evidence_dir, runner_evidence_dir, runner_output, runner_output_sha256
```

Expected: each of the four focused suites is launched exactly once, has a non-null integral root exit code `0`, reports `PASSED`, passes the reusable schema-v2 safety envelope plus the separate `COMPLETED` / helper-0 / no-timeout / zero-window gates, and retains unique helper request/stdout/stderr/result reports plus a unique runner log and external `SaveDir`. PID/count/error fields are recorded only as diagnostics, without equality or minimum assertions. On a fifth fresh mirror, each of the two mandatory repository scanners and the exact three-file show-before scanner runs through its own one-shot private helper host, gets the same full envelope/outcome gates, and leaves create-new request/stdout/stderr/result evidence; zero findings/empty show output are then asserted from the helper-owned streams. No direct `System.Diagnostics.Process` or unbounded `WaitForExit()` scanner path exists. Finally, a sixth fresh mirror runs lint exactly once through the same dedicated-host private-desktop helper. Stop immediately on the first `NEEDS_CONTEXT`; preserve every completed and failed invocation directory and mirror, and never repeat a scanner, suite, or lint on the same bytes.

- [ ] **Step 10: Check exact scope and commit the rules slice**

```powershell
$UnrelatedPlan = 'docs/superpowers/plans/2026-08-09-winter-interlude-narrative-delivery.md'
$UnrelatedSha256 = '0F39B5F5ACE1D4666DD146863CABDF398B031F5666C29AE337CEB89796E4276C'
$ExpectedPaths = @('game/balance.rpy', 'game/difficulty.rpy', 'game/test_game.rpy')
$ActualPaths = @(git diff --name-only | Sort-Object)
if (Compare-Object $ExpectedPaths $ActualPaths) {
    throw ('Unexpected rules-slice paths: ' + ($ActualPaths -join ', '))
}
git diff --check -- game/difficulty.rpy game/balance.rpy game/test_game.rpy
if ($LASTEXITCODE -ne 0) { throw 'Rules-slice diff check failed.' }
if ((Get-FileHash -Algorithm SHA256 $UnrelatedPlan).Hash -cne $UnrelatedSha256) {
    throw 'Unrelated narrative-delivery plan drifted during rules work.'
}
git add -- game/difficulty.rpy game/balance.rpy game/test_game.rpy
$CachedPaths = @(git diff --cached --name-only | Sort-Object)
if (Compare-Object $ExpectedPaths $CachedPaths) {
    throw ('Unexpected staged rules paths: ' + ($CachedPaths -join ', '))
}
git commit -m "fix: enforce terminal resistance collapse rules"
if ($LASTEXITCODE -ne 0) { throw 'Rules-slice commit failed.' }
if (@(git diff --cached --name-only).Count -ne 0) { throw 'Index not empty after rules commit.' }
$RulesCommit = (& git rev-parse HEAD).Trim()
if ((git rev-parse HEAD^) -cne $Task2BaselineCommit -or
    (git log -1 --format=%s) -cne 'fix: enforce terminal resistance collapse rules') {
    throw 'NEEDS_CONTEXT: rules commit topology or subject is wrong.'
}
$CommittedPaths = @(git diff-tree --no-commit-id --name-only -r $RulesCommit | Sort-Object)
if (Compare-Object $ExpectedPaths $CommittedPaths) {
    throw ('NEEDS_CONTEXT: a hook or commit step added unexpected paths: ' + ($CommittedPaths -join ', '))
}
if ((Get-FileHash -Algorithm SHA256 $UnrelatedPlan).Hash -cne $UnrelatedSha256) {
    throw 'NEEDS_CONTEXT: unrelated narrative-delivery plan drifted during commit.'
}
$ExpectedStatus = @('?? ' + $UnrelatedPlan)
$ObservedStatus = @(git status --short --untracked-files=all)
if (Compare-Object $ExpectedStatus $ObservedStatus) {
    throw ('NEEDS_CONTEXT: worktree is not exact after the rules commit: ' + ($ObservedStatus -join '; '))
}
if ((git rev-parse ($RulesCommit + '^')) -cne [string]$ApprovalRecord.approved_plan_commit -or
    (git log -1 --format=%s $RulesCommit) -cne 'fix: enforce terminal resistance collapse rules' -or
    (Get-FileHash -LiteralPath $ApprovalLockPath -Algorithm SHA256).Hash -cne $ApprovalLockHashAtTask2Start -or
    (Get-FileHash -LiteralPath $Task1CompletionRecord -Algorithm SHA256).Hash -cne $Task1CompletionHashAtTask2Start) {
    throw 'NEEDS_CONTEXT: approval-locked P -> exact rules R topology or sealed evidence drifted after commit.'
}
$RulesCommitPaths = @(git diff-tree --no-commit-id --name-only -r $RulesCommit | Sort-Object)
if (Compare-Object @('game/balance.rpy', 'game/difficulty.rpy', 'game/test_game.rpy') $RulesCommitPaths) {
    throw 'NEEDS_CONTEXT: rules commit is not the exact approved three-path child of P.'
}
```

Expected: the successful commit is a direct child of the executable-plan baseline, has the exact subject above, and contains exactly the three text `.rpy` paths. This post-commit check is mandatory because the repository pre-commit hook may update and stage `game/msyh.ttf`; any fourth path is `NEEDS_CONTEXT`, and the rules slice must not be described as complete. The index is empty and the only remaining status row is the protected unrelated plan.

- [ ] **Step 11: Seal the exact nine-invocation Task 2 completion record**

Only after Step 10 has proved the exact P-to-R commit may this create-new record be written. It is the sole machine authority consumed by Task 3; Markdown output is not a substitute.

```powershell
$Task2CompletionRecord = Join-Path $Task2EvidenceRoot 'task2-completion.json'
if (Test-Path -LiteralPath $Task2CompletionRecord) {
    throw 'NEEDS_CONTEXT: Task 2 completion record already exists; do not overwrite or replay Task 2.'
}
if ((Get-FileHash -LiteralPath $ApprovalLockPath -Algorithm SHA256).Hash -cne $ApprovalLockHashAtTask2Start -or
    (Get-FileHash -LiteralPath $Task1CompletionRecord -Algorithm SHA256).Hash -cne $Task1CompletionHashAtTask2Start -or
    (git rev-parse HEAD) -cne $RulesCommit -or
    (git rev-parse ($RulesCommit + '^')) -cne [string]$ApprovalRecord.approved_plan_commit) {
    throw 'NEEDS_CONTEXT: approval, Task 1, or P-to-R state drifted before Task 2 sealing.'
}
$ExpectedRulesPaths = @('game/balance.rpy', 'game/difficulty.rpy', 'game/test_game.rpy')
if (Compare-Object $ExpectedRulesPaths @(git diff-tree --no-commit-id --name-only -r $RulesCommit | Sort-Object)) {
    throw 'NEEDS_CONTEXT: rules commit paths drifted before Task 2 sealing.'
}
$Task2InvocationSpecs = @(
    [pscustomobject]@{ name='rules-red'; kind='suite'; expected='FAILED'; value=$RedResult },
    [pscustomobject]@{ name='rules-green'; kind='suite'; expected='PASSED'; value=$RulesGreen },
    [pscustomobject]@{ name='catalog-green'; kind='suite'; expected='PASSED'; value=$CatalogGreen },
    [pscustomobject]@{ name='balance-green'; kind='suite'; expected='PASSED'; value=$BalanceGreen },
    [pscustomobject]@{ name='winter-invariance-green'; kind='suite'; expected='PASSED'; value=$WinterGreen },
    [pscustomobject]@{ name='missing-portraits-green'; kind='scanner'; expected='PASS'; value=$MissingPortraitResult },
    [pscustomobject]@{ name='narration-overlap-green'; kind='scanner'; expected='PASS'; value=$NarrationOverlapResult },
    [pscustomobject]@{ name='show-before-green'; kind='scanner'; expected='PASS'; value=$ShowBeforeResult },
    [pscustomobject]@{ name='lint-green'; kind='lint'; expected='PASS'; value=$LintGreen }
)
$ExpectedTask2InvocationNames = @(
    'rules-red', 'rules-green', 'catalog-green', 'balance-green',
    'winter-invariance-green', 'missing-portraits-green',
    'narration-overlap-green', 'show-before-green', 'lint-green'
)
if ($Task2InvocationSpecs.Count -ne 9 -or
    (Compare-Object $ExpectedTask2InvocationNames @($Task2InvocationSpecs.name) -CaseSensitive)) {
    throw 'NEEDS_CONTEXT: Task 2 did not produce the exact nine named invocations.'
}
$ReceiptProperties = @(
    'schema_version','name','kind','expected','actual','verdict','helper_evidence_dir',
    'helper_artifacts','helper_result','runner_or_scanner_evidence_dir','direct_evidence',
    'source_evidence','assertions','created_utc'
)
$FileSealProperties = @('path','bytes','sha256')
$AssertionProperties = @('central_safety_envelope','outcome_gates','runner_or_scanner')
$ExpectedTask2InvocationContract = [ordered]@{
    'rules-red' = [pscustomobject]@{ kind='suite'; expected='FAILED'; direct_count=1; source_count=0 }
    'rules-green' = [pscustomobject]@{ kind='suite'; expected='PASSED'; direct_count=1; source_count=0 }
    'catalog-green' = [pscustomobject]@{ kind='suite'; expected='PASSED'; direct_count=1; source_count=0 }
    'balance-green' = [pscustomobject]@{ kind='suite'; expected='PASSED'; direct_count=1; source_count=0 }
    'winter-invariance-green' = [pscustomobject]@{ kind='suite'; expected='PASSED'; direct_count=1; source_count=0 }
    'missing-portraits-green' = [pscustomobject]@{ kind='scanner'; expected='PASS'; direct_count=2; source_count=0 }
    'narration-overlap-green' = [pscustomobject]@{ kind='scanner'; expected='PASS'; direct_count=2; source_count=0 }
    'show-before-green' = [pscustomobject]@{ kind='scanner'; expected='PASS'; direct_count=3; source_count=1 }
    'lint-green' = [pscustomobject]@{ kind='lint'; expected='PASS'; direct_count=1; source_count=0 }
}

function Assert-Task2FileSealStrict($Seal, [string]$Context) {
    if ($Seal -isnot [pscustomobject] -or
        (@($Seal.PSObject.Properties.Name) -join '|') -cne ($FileSealProperties -join '|') -or
        $Seal.path -isnot [string] -or -not [IO.Path]::IsPathRooted([string]$Seal.path) -or
        -not (Test-Path -LiteralPath ([string]$Seal.path) -PathType Leaf) -or
        -not (Test-PrivateDesktopIntegralValue $Seal.bytes) -or [int64]$Seal.bytes -lt 0 -or
        $Seal.sha256 -isnot [string] -or [string]$Seal.sha256 -cnotmatch '^[0-9A-F]{64}$') {
        throw ('NEEDS_CONTEXT: invalid Task 2 file seal: ' + $Context)
    }
    $ResolvedPath = (Resolve-Path -LiteralPath ([string]$Seal.path)).Path
    if ($ResolvedPath -cne [string]$Seal.path -or
        (Get-Item -LiteralPath $ResolvedPath).Length -ne [int64]$Seal.bytes -or
        (Get-FileHash -LiteralPath $ResolvedPath -Algorithm SHA256).Hash -cne [string]$Seal.sha256) {
        throw ('NEEDS_CONTEXT: Task 2 sealed artifact drifted: ' + $Context)
    }
}

function Read-Task2StrictUtf8Json([string]$Path, [string]$Context) {
    $RawBytes = [IO.File]::ReadAllBytes($Path)
    if ($RawBytes.Length -eq 0 -or
        ($RawBytes.Length -ge 3 -and $RawBytes[0] -eq 0xEF -and
         $RawBytes[1] -eq 0xBB -and $RawBytes[2] -eq 0xBF)) {
        throw ('NEEDS_CONTEXT: JSON is empty or has a BOM: ' + $Context)
    }
    $RawText = $StrictUtf8.GetString($RawBytes)
    if ($RawText.Contains([char]0xFFFD)) {
        throw ('NEEDS_CONTEXT: JSON is not strict UTF-8: ' + $Context)
    }
    return ($RawText | ConvertFrom-Json -ErrorAction Stop)
}

function Assert-Task2ReceiptRawPropertyCounts(
    [string]$ReceiptText,
    [int]$DirectCount,
    [int]$SourceCount,
    [string]$Context
) {
    $SealObjectCount = 5 + $DirectCount + $SourceCount
    $ExpectedRawCounts = [ordered]@{
        schema_version=1; name=1; kind=1; expected=1; actual=1; verdict=1
        helper_evidence_dir=1; helper_artifacts=1; helper_result=1
        runner_or_scanner_evidence_dir=1; direct_evidence=1; source_evidence=1
        assertions=1; created_utc=1
        path=$SealObjectCount; bytes=$SealObjectCount; sha256=$SealObjectCount
        central_safety_envelope=1; outcome_gates=1; runner_or_scanner=1
    }
    $RawKeys = @([regex]::Matches($ReceiptText, '"([^"\\]+)"\s*:') | ForEach-Object { $_.Groups[1].Value })
    $ExpectedRows = @($ExpectedRawCounts.GetEnumerator() | ForEach-Object {
        [string]$_.Key + '=' + [string]$_.Value
    } | Sort-Object)
    $ObservedRows = @($RawKeys | Group-Object -CaseSensitive | ForEach-Object {
        [string]$_.Name + '=' + [string]$_.Count
    } | Sort-Object)
    if (Compare-Object $ExpectedRows $ObservedRows -CaseSensitive) {
        throw ('NEEDS_CONTEXT: receipt has duplicate, missing, or extra raw properties: ' + $Context)
    }
}

function Read-Task2InvocationReceiptStrict($Spec) {
    $Contract = $ExpectedTask2InvocationContract[[string]$Spec.name]
    if ($null -eq $Contract -or [string]$Spec.kind -cne [string]$Contract.kind -or
        [string]$Spec.expected -cne [string]$Contract.expected) {
        throw ('NEEDS_CONTEXT: invocation specification is outside the fixed contract: ' + [string]$Spec.name)
    }
    if ($Spec.value.receipt_path -isnot [string] -or
        -not [IO.Path]::IsPathRooted([string]$Spec.value.receipt_path) -or
        -not (Test-PrivateDesktopIntegralValue $Spec.value.receipt_bytes) -or [int64]$Spec.value.receipt_bytes -le 0 -or
        $Spec.value.receipt_sha256 -isnot [string] -or [string]$Spec.value.receipt_sha256 -cnotmatch '^[0-9A-F]{64}$') {
        throw ('NEEDS_CONTEXT: invocation-time receipt locator is invalid: ' + [string]$Spec.name)
    }
    $ReceiptSeal = [pscustomobject][ordered]@{
        path = [string]$Spec.value.receipt_path
        bytes = [long]$Spec.value.receipt_bytes
        sha256 = [string]$Spec.value.receipt_sha256
    }
    $null = Assert-Task2FileSealStrict $ReceiptSeal ('receipt locator ' + [string]$Spec.name)
    git check-ignore -q -- $ReceiptSeal.path
    if ($LASTEXITCODE -ne 0) {
        throw ('NEEDS_CONTEXT: invocation receipt is not ignored: ' + [string]$Spec.name)
    }

    $ReceiptBytes = [IO.File]::ReadAllBytes($ReceiptSeal.path)
    if ($ReceiptBytes.Length -eq 0 -or
        ($ReceiptBytes.Length -ge 3 -and $ReceiptBytes[0] -eq 0xEF -and
         $ReceiptBytes[1] -eq 0xBB -and $ReceiptBytes[2] -eq 0xBF)) {
        throw ('NEEDS_CONTEXT: invocation receipt is empty or has a BOM: ' + [string]$Spec.name)
    }
    $ReceiptText = $StrictUtf8.GetString($ReceiptBytes)
    if ($ReceiptText.Contains([char]0xFFFD)) {
        throw ('NEEDS_CONTEXT: invocation receipt is not strict UTF-8: ' + [string]$Spec.name)
    }
    $null = Assert-Task2ReceiptRawPropertyCounts `
        $ReceiptText ([int]$Contract.direct_count) ([int]$Contract.source_count) ([string]$Spec.name)
    $Receipt = $ReceiptText | ConvertFrom-Json -ErrorAction Stop

    if ($Receipt -isnot [pscustomobject] -or
        (@($Receipt.PSObject.Properties.Name) -join '|') -cne ($ReceiptProperties -join '|') -or
        $Receipt.schema_version -isnot [int] -or [int]$Receipt.schema_version -ne 1 -or
        $Receipt.name -isnot [string] -or [string]$Receipt.name -cne [string]$Spec.name -or
        $Receipt.kind -isnot [string] -or [string]$Receipt.kind -cne [string]$Contract.kind -or
        $Receipt.expected -isnot [string] -or [string]$Receipt.expected -cne [string]$Contract.expected -or
        $Receipt.actual -isnot [string] -or [string]$Receipt.actual -cne [string]$Receipt.expected -or
        $Receipt.verdict -isnot [string] -or [string]$Receipt.verdict -cne 'PASS' -or
        $Receipt.helper_evidence_dir -isnot [string] -or
        $Receipt.runner_or_scanner_evidence_dir -isnot [string] -or
        $Receipt.assertions -isnot [pscustomobject] -or
        (@($Receipt.assertions.PSObject.Properties.Name) -join '|') -cne ($AssertionProperties -join '|') -or
        @($Receipt.assertions.PSObject.Properties.Value | Where-Object { $_ -isnot [string] -or $_ -cne 'PASS' }).Count -ne 0 -or
        $Receipt.created_utc -isnot [string]) {
        throw ('NEEDS_CONTEXT: invocation receipt canonical contract failed: ' + [string]$Spec.name)
    }
    try {
        [void][DateTimeOffset]::ParseExact(
            [string]$Receipt.created_utc,
            'o',
            [Globalization.CultureInfo]::InvariantCulture,
            [Globalization.DateTimeStyles]::RoundtripKind
        )
    } catch {
        throw ('NEEDS_CONTEXT: invocation receipt created_utc is not round-trip format: ' + [string]$Spec.name)
    }

    if (-not [IO.Path]::IsPathRooted([string]$Receipt.helper_evidence_dir) -or
        -not (Test-Path -LiteralPath ([string]$Receipt.helper_evidence_dir) -PathType Container) -or
        -not [IO.Path]::IsPathRooted([string]$Receipt.runner_or_scanner_evidence_dir) -or
        -not (Test-Path -LiteralPath ([string]$Receipt.runner_or_scanner_evidence_dir) -PathType Container)) {
        throw ('NEEDS_CONTEXT: receipt evidence directory contract failed: ' + [string]$Spec.name)
    }
    $HelperEvidenceFull = (Resolve-Path -LiteralPath ([string]$Receipt.helper_evidence_dir)).Path
    $RunnerOrScannerFull = (Resolve-Path -LiteralPath ([string]$Receipt.runner_or_scanner_evidence_dir)).Path
    if ([string]$Receipt.helper_evidence_dir -cne $HelperEvidenceFull -or
        [string]$Receipt.runner_or_scanner_evidence_dir -cne $RunnerOrScannerFull -or
        [string]$ReceiptSeal.path -cne [IO.Path]::GetFullPath((Join-Path $HelperEvidenceFull 'invocation-receipt.json'))) {
        throw ('NEEDS_CONTEXT: receipt path/directory canonicalization failed: ' + [string]$Spec.name)
    }

    if (@($Receipt.helper_artifacts).Count -ne 4 -or
        @($Receipt.direct_evidence).Count -ne [int]$Contract.direct_count -or
        @($Receipt.source_evidence).Count -ne [int]$Contract.source_count) {
        throw ('NEEDS_CONTEXT: receipt evidence cardinality failed: ' + [string]$Spec.name)
    }
    $AllReceiptSeals = @($Receipt.helper_artifacts) + @($Receipt.helper_result) +
        @($Receipt.direct_evidence) + @($Receipt.source_evidence)
    foreach ($Seal in $AllReceiptSeals) {
        $null = Assert-Task2FileSealStrict $Seal ('receipt artifact ' + [string]$Spec.name)
    }

    $ExpectedHelperArtifactPaths = @(
        [IO.Path]::GetFullPath((Join-Path $HelperEvidenceFull 'request.json'))
        [IO.Path]::GetFullPath((Join-Path $HelperEvidenceFull 'stdout.txt'))
        [IO.Path]::GetFullPath((Join-Path $HelperEvidenceFull 'stderr.txt'))
        [IO.Path]::GetFullPath((Join-Path $HelperEvidenceFull 'result.json'))
    )
    for ($HelperIndex = 0; $HelperIndex -lt 4; $HelperIndex++) {
        if ([string]$Receipt.helper_artifacts[$HelperIndex].path -cne $ExpectedHelperArtifactPaths[$HelperIndex]) {
            throw ('NEEDS_CONTEXT: helper artifact order/path failed: ' + [string]$Spec.name)
        }
    }
    if (-not (Test-Task2FileSealIdentity $Receipt.helper_result $Receipt.helper_artifacts[3])) {
        throw ('NEEDS_CONTEXT: helper_result is not exactly helper_artifacts[3]: ' + [string]$Spec.name)
    }

    if ([string]$Contract.kind -ceq 'scanner') {
        if ($RunnerOrScannerFull -cne $HelperEvidenceFull -or
            -not (Test-Task2FileSealIdentity $Receipt.direct_evidence[0] $Receipt.helper_artifacts[1]) -or
            -not (Test-Task2FileSealIdentity $Receipt.direct_evidence[1] $Receipt.helper_artifacts[2])) {
            throw ('NEEDS_CONTEXT: scanner receipt stdout/stderr relation failed: ' + [string]$Spec.name)
        }
    } else {
        $ExpectedRunnerExtension = if ([string]$Contract.kind -ceq 'suite') { '.log' } else { '.txt' }
        if ([IO.Path]::GetDirectoryName([string]$Receipt.direct_evidence[0].path) -cne $RunnerOrScannerFull -or
            [IO.Path]::GetExtension([string]$Receipt.direct_evidence[0].path) -cne $ExpectedRunnerExtension) {
            throw ('NEEDS_CONTEXT: suite/lint direct evidence relation failed: ' + [string]$Spec.name)
        }
    }
    if ([string]$Spec.name -ceq 'show-before-green') {
        if (-not (Test-Path -LiteralPath $ShowScanPath -PathType Leaf) -or
            [string]$Receipt.source_evidence[0].path -cne (Resolve-Path -LiteralPath $ShowScanPath).Path -or
            -not (Test-Task2FileSealIdentity $Receipt.source_evidence[0] $Receipt.direct_evidence[2])) {
            throw 'NEEDS_CONTEXT: show-before source/direct relation failed.'
        }
    }

    $HelperResult = Read-Task2StrictUtf8Json $Receipt.helper_result.path ('helper result ' + [string]$Spec.name)
    $null = Assert-PrivateDesktopSafetyEnvelope -Result $HelperResult
    if (-not (Test-PrivateDesktopIntegralValue $HelperResult.root_exit_code) -or
        [int64]$HelperResult.root_exit_code -ne 0 -or
        [string]$HelperResult.classification -cne 'COMPLETED' -or
        $HelperResult.helper_exit_code -isnot [int] -or [int]$HelperResult.helper_exit_code -ne 0 -or
        $HelperResult.timed_out -isnot [bool] -or [bool]$HelperResult.timed_out -or
        @($HelperResult.visible_windows).Count -ne 0 -or
        [string]$HelperResult.stdout_path -cne [string]$Receipt.helper_artifacts[1].path -or
        [string]$HelperResult.stderr_path -cne [string]$Receipt.helper_artifacts[2].path) {
        throw ('NEEDS_CONTEXT: sealed helper result outcome failed: ' + [string]$Spec.name)
    }

    if ([string]$Contract.kind -ceq 'suite') {
        $RunnerText = [IO.File]::ReadAllText([string]$Receipt.direct_evidence[0].path, $StrictUtf8)
        $Matches = [regex]::Matches($RunnerText, '(?m)^\[rpytest\] Status:\s+([A-Z ]+?)\s*$')
        if ($Matches.Count -ne 1 -or $Matches[0].Groups[1].Value.Trim() -cne [string]$Receipt.actual) {
            throw ('NEEDS_CONTEXT: sealed suite status contradicts its receipt: ' + [string]$Spec.name)
        }
    } elseif ([string]$Contract.kind -ceq 'scanner') {
        $ScannerOut = [IO.File]::ReadAllText([string]$Receipt.direct_evidence[0].path, $StrictUtf8)
        $ScannerErr = [IO.File]::ReadAllText([string]$Receipt.direct_evidence[1].path, $StrictUtf8)
        if ($ScannerErr.Length -ne 0 -or
            ([string]$Spec.name -ceq 'show-before-green' -and $ScannerOut.Length -ne 0) -or
            ([string]$Spec.name -ceq 'missing-portraits-green' -and
             [regex]::Matches($ScannerOut, '(?m)^=== Total findings: 0 ===\s*$').Count -ne 1) -or
            ([string]$Spec.name -ceq 'narration-overlap-green' -and
             [regex]::Matches($ScannerOut, '(?m)^TOTAL:\s+0\b.*$').Count -ne 1)) {
            throw ('NEEDS_CONTEXT: sealed scanner output contradicts its receipt: ' + [string]$Spec.name)
        }
    }

    return [pscustomobject][ordered]@{
        receipt = $ReceiptSeal
        record = $Receipt
    }
}

function New-Task2ExternallyBoundSeal([string]$Path, [string]$ExpectedSha256) {
    if ($ExpectedSha256 -cnotmatch '^[0-9A-F]{64}$') {
        throw ('NEEDS_CONTEXT: invalid externally bound artifact hash: ' + $Path)
    }
    $FullPath = (Resolve-Path -LiteralPath $Path).Path
    $Item = Get-Item -LiteralPath $FullPath -ErrorAction Stop
    if ((Get-FileHash -LiteralPath $FullPath -Algorithm SHA256).Hash -cne $ExpectedSha256) {
        throw ('NEEDS_CONTEXT: externally bound Task 2 artifact drifted: ' + $FullPath)
    }
    return [pscustomobject][ordered]@{
        path = $FullPath
        bytes = [long]$Item.Length
        sha256 = $ExpectedSha256
    }
}

$Task2ArtifactLookup = New-Object 'System.Collections.Generic.Dictionary[string,object]' ([StringComparer]::OrdinalIgnoreCase)
function Add-Task2CompletionArtifactSeal($Seal, [string]$Context) {
    $null = Assert-Task2FileSealStrict $Seal $Context
    if ($Task2ArtifactLookup.ContainsKey([string]$Seal.path)) {
        if (-not (Test-Task2FileSealIdentity $Task2ArtifactLookup[[string]$Seal.path] $Seal)) {
            throw ('NEEDS_CONTEXT: conflicting Task 2 seals for one path: ' + [string]$Seal.path)
        }
        return
    }
    $StoredSeal = [pscustomobject][ordered]@{
        path = [string]$Seal.path
        bytes = [long]$Seal.bytes
        sha256 = [string]$Seal.sha256
    }
    $Task2ArtifactLookup.Add($StoredSeal.path, $StoredSeal)
}

$FixedTask2Seals = @(
    New-Task2ExternallyBoundSeal $ApprovalLockPath $ApprovalLockHashAtTask2Start
    New-Task2ExternallyBoundSeal $Task1CompletionRecord $Task1CompletionHashAtTask2Start
    New-Task2ExternallyBoundSeal $ThisPlan ([string]$ApprovalRecord.plan_sha256)
    New-Task2ExternallyBoundSeal $DesignPath ([string]$ApprovalRecord.spec_sha256)
)
foreach ($FixedSeal in $FixedTask2Seals) {
    Add-Task2CompletionArtifactSeal $FixedSeal 'fixed Task 2 authority'
}

$Task2InvocationEntries = @()
foreach ($Spec in $Task2InvocationSpecs) {
    $InvocationEntry = Read-Task2InvocationReceiptStrict $Spec
    Add-Task2CompletionArtifactSeal $InvocationEntry.receipt ('receipt ' + [string]$Spec.name)
    foreach ($Seal in @($InvocationEntry.record.helper_artifacts)) {
        Add-Task2CompletionArtifactSeal $Seal ('helper artifact ' + [string]$Spec.name)
    }
    foreach ($Seal in @($InvocationEntry.record.direct_evidence)) {
        Add-Task2CompletionArtifactSeal $Seal ('direct evidence ' + [string]$Spec.name)
    }
    foreach ($Seal in @($InvocationEntry.record.source_evidence)) {
        Add-Task2CompletionArtifactSeal $Seal ('source evidence ' + [string]$Spec.name)
    }
    $Task2InvocationEntries += $InvocationEntry
}
$Task2Artifacts = @($Task2ArtifactLookup.Values | Sort-Object path)
if ($Task2Artifacts.Count -ne 56) {
    throw ('NEEDS_CONTEXT: exact Task 2 artifact union must contain 56 files; found ' + [string]$Task2Artifacts.Count)
}
$Task2CompletionPayload = [ordered]@{
    schema_version = 1
    verdict = 'PASS'
    approved_plan_lock_sha256 = $ApprovalLockHashAtTask2Start
    task1_completion_path = (Resolve-Path -LiteralPath $Task1CompletionRecord).Path
    task1_completion_sha256 = $Task1CompletionHashAtTask2Start
    approved_plan_commit = [string]$ApprovalRecord.approved_plan_commit
    rules_commit = $RulesCommit
    rules_parent_commit = (git rev-parse ($RulesCommit + '^')).Trim()
    rules_subject = 'fix: enforce terminal resistance collapse rules'
    rules_paths = $ExpectedRulesPaths
    invocation_count = 9
    invocations = $Task2InvocationEntries
    artifact_count = [int]$Task2Artifacts.Count
    artifacts = $Task2Artifacts
    finished_utc = [DateTimeOffset]::UtcNow.ToString('o')
}
Write-Task2CreateNewUtf8 -Path $Task2CompletionRecord -Text (($Task2CompletionPayload | ConvertTo-Json -Depth 10) + "`n")
$Task2CompletionCheck = Read-Task2StrictUtf8Json $Task2CompletionRecord 'Task 2 completion record'
$ExpectedTask2CompletionProperties = @(
    'schema_version','verdict','approved_plan_lock_sha256','task1_completion_path',
    'task1_completion_sha256','approved_plan_commit','rules_commit','rules_parent_commit',
    'rules_subject','rules_paths','invocation_count','invocations','artifact_count','artifacts','finished_utc'
)
if ($Task2CompletionCheck -isnot [pscustomobject] -or
    (@($Task2CompletionCheck.PSObject.Properties.Name) -join '|') -cne ($ExpectedTask2CompletionProperties -join '|') -or
    $Task2CompletionCheck.schema_version -isnot [int] -or [int]$Task2CompletionCheck.schema_version -ne 1 -or
    $Task2CompletionCheck.verdict -isnot [string] -or $Task2CompletionCheck.verdict -cne 'PASS' -or
    $Task2CompletionCheck.approved_plan_lock_sha256 -isnot [string] -or $Task2CompletionCheck.approved_plan_lock_sha256 -cne $ApprovalLockHashAtTask2Start -or
    $Task2CompletionCheck.task1_completion_path -isnot [string] -or $Task2CompletionCheck.task1_completion_path -cne (Resolve-Path -LiteralPath $Task1CompletionRecord).Path -or
    $Task2CompletionCheck.task1_completion_sha256 -isnot [string] -or $Task2CompletionCheck.task1_completion_sha256 -cne $Task1CompletionHashAtTask2Start -or
    $Task2CompletionCheck.approved_plan_commit -isnot [string] -or $Task2CompletionCheck.approved_plan_commit -cne [string]$ApprovalRecord.approved_plan_commit -or
    $Task2CompletionCheck.rules_commit -isnot [string] -or $Task2CompletionCheck.rules_commit -cne $RulesCommit -or
    $Task2CompletionCheck.rules_parent_commit -isnot [string] -or $Task2CompletionCheck.rules_parent_commit -cne [string]$ApprovalRecord.approved_plan_commit -or
    $Task2CompletionCheck.rules_subject -isnot [string] -or $Task2CompletionCheck.rules_subject -cne 'fix: enforce terminal resistance collapse rules' -or
    @($Task2CompletionCheck.rules_paths | Where-Object { $_ -isnot [string] }).Count -ne 0 -or
    (@($Task2CompletionCheck.rules_paths) -join '|') -cne ($ExpectedRulesPaths -join '|') -or
    $Task2CompletionCheck.invocation_count -isnot [int] -or $Task2CompletionCheck.invocation_count -ne 9 -or @($Task2CompletionCheck.invocations).Count -ne 9 -or
    $Task2CompletionCheck.artifact_count -isnot [int] -or $Task2CompletionCheck.artifact_count -ne 56 -or @($Task2CompletionCheck.artifacts).Count -ne 56 -or
    $Task2CompletionCheck.finished_utc -isnot [string] -or
    (@($Task2CompletionCheck.invocations.record.name) -join '|') -cne ($ExpectedTask2InvocationNames -join '|')) {
    throw 'Task 2 completion record failed strict top-level reread.'
}
try {
    [void][DateTimeOffset]::ParseExact(
        [string]$Task2CompletionCheck.finished_utc,
        'o',
        [Globalization.CultureInfo]::InvariantCulture,
        [Globalization.DateTimeStyles]::RoundtripKind
    )
} catch {
    throw 'Task 2 completion record finished_utc is not round-trip format.'
}
$Task2CompletionInvocationArray = @($Task2CompletionCheck.invocations)
for ($InvocationIndex = 0; $InvocationIndex -lt 9; $InvocationIndex++) {
    $Invocation = $Task2CompletionInvocationArray[$InvocationIndex]
    $ExpectedInvocationEntry = $Task2InvocationEntries[$InvocationIndex]
    if ($Invocation -isnot [pscustomobject] -or
        (@($Invocation.PSObject.Properties.Name) -join '|') -cne 'receipt|record' -or
        $Invocation.receipt -isnot [pscustomobject] -or
        -not (Test-Task2FileSealIdentity $Invocation.receipt $ExpectedInvocationEntry.receipt) -or
        $Invocation.record -isnot [pscustomobject] -or
        ($Invocation.record | ConvertTo-Json -Depth 10 -Compress) -cne
            ($ExpectedInvocationEntry.record | ConvertTo-Json -Depth 10 -Compress)) {
        throw ('Task 2 completion invocation failed strict reread: ' + [string]$Invocation.record.name)
    }
    $null = Assert-Task2FileSealStrict $Invocation.receipt ('completion receipt ' + [string]$Invocation.record.name)
}
$Task2CompletionArtifactArray = @($Task2CompletionCheck.artifacts)
for ($ArtifactIndex = 0; $ArtifactIndex -lt 56; $ArtifactIndex++) {
    $Artifact = $Task2CompletionArtifactArray[$ArtifactIndex]
    if (-not (Test-Task2FileSealIdentity $Artifact $Task2Artifacts[$ArtifactIndex])) {
        throw ('Task 2 completion artifact union changed at index ' + [string]$ArtifactIndex)
    }
    $null = Assert-Task2FileSealStrict $Artifact ('completion artifact index ' + [string]$ArtifactIndex)
}
git check-ignore -q -- $Task2CompletionRecord
if ($LASTEXITCODE -ne 0) { throw 'Task 2 completion record is not ignored.' }
(Get-Item -LiteralPath $Task2CompletionRecord).IsReadOnly = $true
if (-not (Get-Item -LiteralPath $Task2CompletionRecord).IsReadOnly) { throw 'Task 2 completion record is not read-only.' }
$Task2CompletionHash = (Get-FileHash -LiteralPath $Task2CompletionRecord -Algorithm SHA256).Hash
```

Expected: the strict read-only record binds the immutable approval lock, Task 1 completion hash, exact P-to-R ancestry/subject/three paths, exactly nine named PASS invocations (one RED, four GREEN suites, three scanners, one lint), their expected and actual outcomes, helper evidence/result, and runner/scanner direct evidence. Its exact 56-file union is the four externally bound authorities, nine invocation-time receipt locators, 36 helper artifacts, six distinct suite/lint runner outputs, and one distinct show-before source; scanner stdout/stderr alias helper artifacts, `helper_result` aliases the fourth helper artifact, and the show source aliases its third direct evidence, so none is counted twice. Every duplicate path must carry the identical pre-existing seal, and the completion reread compares every invocation and sorted artifact row to the pre-write structures rather than re-baselining current bytes. Neither the lock nor either completion record is a cleanup target.

Asset report for this commit: art `not required`, music `not required`, sound effects `not required`, animation `not required`, UI `not required`; no binary or package-size change. The post-commit tree check proves the font was not changed or added by the hook.

---

## Task 3: Generate three isolated raw Opus copy bundles

**Files:**

- Read: `CANON.md`
- Read: `CLAUDE.md`
- Read: `docs/writing-style/INDEX.md`
- Read: `docs/writing-style/guidance.md`
- Read context only: `game/chapter5.rpy:2387-2469, 6068-6194, 6396-6505`
- Read context only: `game/endings_expansion.rpy:204-249`
- Create ignored prompts/results only: `.superpowers/sdd/terminal-collapse-ending/copy/run-01/`, `run-02/`, `run-03/`
- Create ignored blind map only: `.superpowers/sdd/terminal-collapse-ending/copy/blind-map.md`

- [ ] **Step 0: Validate the immutable approval lock and exact P-to-R topology before reading project inputs**

The controller must provide `$ApprovalLockSha256` out of band when it opens this fresh persistent Windows PowerShell 5.1 session. This is Task 3's first project action. Do not read `CANON.md`, guidance, prose context, Task 1/2 evidence, or any other repository file before this approval lock and P-to-R topology gate passes:

```powershell
$ErrorActionPreference = 'Stop'
$ProjectRoot = (Resolve-Path -LiteralPath '.').Path
$EvidenceRoot = Join-Path $ProjectRoot '.superpowers\sdd\terminal-collapse-ending'
$StrictUtf8 = New-Object System.Text.UTF8Encoding($false, $true)
$ThisPlan = 'docs/superpowers/plans/2026-08-11-terminal-collapse-ending-phase-a.md'
$DesignPath = 'docs/superpowers/specs/2026-08-11-terminal-collapse-ending-design.md'
$UnrelatedPlan = 'docs/superpowers/plans/2026-08-09-winter-interlude-narrative-delivery.md'
$UnrelatedPlanHash = '0F39B5F5ACE1D4666DD146863CABDF398B031F5666C29AE337CEB89796E4276C'
$ApprovalLockPath = Join-Path $EvidenceRoot 'approved-plan-lock.json'
$ApprovalLockVariable = Get-Variable -Name ApprovalLockSha256 -Scope 0 -ErrorAction SilentlyContinue
if ($null -eq $ApprovalLockVariable -or $ApprovalLockVariable.Value -isnot [string] -or
    [string]$ApprovalLockVariable.Value -cnotmatch '^[0-9A-F]{64}$') {
    throw 'NEEDS_CONTEXT: Task 3 controller did not bind the out-of-band ApprovalLockSha256 parameter.'
}
$ApprovalLockSha256 = [string]$ApprovalLockVariable.Value
if (-not (Test-Path -LiteralPath $ApprovalLockPath -PathType Leaf)) { throw 'NEEDS_CONTEXT: approved-plan lock is missing.' }
git check-ignore -q -- $ApprovalLockPath
if ($LASTEXITCODE -ne 0) { throw 'NEEDS_CONTEXT: approved-plan lock is not ignored.' }
$ApprovalLockBytes = [IO.File]::ReadAllBytes($ApprovalLockPath)
if ($ApprovalLockBytes.Length -eq 0 -or
    ($ApprovalLockBytes.Length -ge 3 -and $ApprovalLockBytes[0] -eq 0xEF -and
     $ApprovalLockBytes[1] -eq 0xBB -and $ApprovalLockBytes[2] -eq 0xBF)) {
    throw 'NEEDS_CONTEXT: approved-plan lock is empty or has a BOM.'
}
$ApprovalLockText = $StrictUtf8.GetString($ApprovalLockBytes)
$ApprovalExpectedProperties = @('schema_version', 'approved_plan_commit', 'plan_sha256', 'spec_commit', 'spec_sha256')
$ApprovalRawProperties = @([regex]::Matches($ApprovalLockText, '"([^"\\]+)"\s*:') | ForEach-Object { $_.Groups[1].Value })
if ($ApprovalLockText.Contains([char]0xFFFD) -or
    (Get-FileHash -LiteralPath $ApprovalLockPath -Algorithm SHA256).Hash -cne $ApprovalLockSha256 -or
    $ApprovalRawProperties.Count -ne 5 -or
    (Compare-Object $ApprovalExpectedProperties $ApprovalRawProperties -CaseSensitive)) {
    throw 'NEEDS_CONTEXT: approved-plan lock encoding, hash, or raw property contract failed.'
}
$ApprovalRecord = $ApprovalLockText | ConvertFrom-Json -ErrorAction Stop
if ($ApprovalRecord -isnot [pscustomobject] -or
    (Compare-Object $ApprovalExpectedProperties @($ApprovalRecord.PSObject.Properties.Name) -CaseSensitive) -or
    $ApprovalRecord.schema_version -isnot [int] -or [int]$ApprovalRecord.schema_version -ne 1 -or
    $ApprovalRecord.approved_plan_commit -isnot [string] -or [string]$ApprovalRecord.approved_plan_commit -cnotmatch '^[0-9a-f]{40}$' -or
    $ApprovalRecord.plan_sha256 -isnot [string] -or [string]$ApprovalRecord.plan_sha256 -cnotmatch '^[0-9A-F]{64}$' -or
    $ApprovalRecord.spec_commit -isnot [string] -or [string]$ApprovalRecord.spec_commit -cne '98ff5ca351806732f435b977c7b3b445d586bf6b' -or
    $ApprovalRecord.spec_sha256 -isnot [string] -or [string]$ApprovalRecord.spec_sha256 -cne 'F7C833952D0F783A922FFF18F6F0A2B9F44BA8F1BF31520917FA6B1237B1A232') {
    throw 'NEEDS_CONTEXT: approved-plan lock schema, types, or values are invalid.'
}
$ExpectedRulesCommit = (& git rev-parse HEAD).Trim()
function Assert-Task3ApprovalState([string]$Context) {
    if ((Get-FileHash -LiteralPath $ApprovalLockPath -Algorithm SHA256).Hash -cne $ApprovalLockSha256 -or
        (Get-FileHash -LiteralPath $ThisPlan -Algorithm SHA256).Hash -cne [string]$ApprovalRecord.plan_sha256 -or
        (& git hash-object --no-filters -- $ThisPlan).Trim() -cne
            (& git rev-parse ([string]$ApprovalRecord.approved_plan_commit + ':' + $ThisPlan)).Trim() -or
        (Get-FileHash -LiteralPath $DesignPath -Algorithm SHA256).Hash -cne [string]$ApprovalRecord.spec_sha256 -or
        (& git hash-object --no-filters -- $DesignPath).Trim() -cne
            (& git rev-parse ([string]$ApprovalRecord.spec_commit + ':' + $DesignPath)).Trim()) {
        throw ('NEEDS_CONTEXT: approval lock, plan, or specification drifted ' + $Context + '; do not invoke Opus.')
    }
    if ((& git rev-parse HEAD).Trim() -cne $ExpectedRulesCommit -or
        (& git rev-parse ($ExpectedRulesCommit + '^')).Trim() -cne [string]$ApprovalRecord.approved_plan_commit -or
        (git log -1 --format=%s $ExpectedRulesCommit) -cne 'fix: enforce terminal resistance collapse rules') {
        throw ('NEEDS_CONTEXT: exact P -> R ancestry/subject drifted ' + $Context + '; do not invoke Opus.')
    }
    $RulesPaths = @(git diff-tree --no-commit-id --name-only -r $ExpectedRulesCommit | Sort-Object)
    if (Compare-Object @('game/balance.rpy', 'game/difficulty.rpy', 'game/test_game.rpy') $RulesPaths) {
        throw ('NEEDS_CONTEXT: exact three-path rules commit drifted ' + $Context + '; do not invoke Opus.')
    }
    if (@(git diff --cached --name-only).Count -ne 0) {
        throw ('NEEDS_CONTEXT: index is not empty ' + $Context + '; do not invoke Opus.')
    }
    $Task3Status = @(git status --short --untracked-files=all)
    if ($Task3Status.Count -ne 1 -or $Task3Status[0] -cne ('?? ' + $UnrelatedPlan) -or
        (Get-FileHash -LiteralPath $UnrelatedPlan -Algorithm SHA256).Hash -cne $UnrelatedPlanHash) {
        throw ('NEEDS_CONTEXT: protected worktree/winter state drifted ' + $Context + '; do not invoke Opus.')
    }
}
Assert-Task3ApprovalState 'at Task 3 start'
$Task1CompletionRecord = Join-Path $EvidenceRoot 'legacy\task1-completion.json'
$Task2CompletionRecord = Join-Path $EvidenceRoot 'rules\task2-completion.json'
foreach ($CompletionPath in @($Task1CompletionRecord, $Task2CompletionRecord)) {
    if (-not (Test-Path -LiteralPath $CompletionPath -PathType Leaf) -or
        -not (Get-Item -LiteralPath $CompletionPath).IsReadOnly) {
        throw ('NEEDS_CONTEXT: sealed completion record is missing or not read-only: ' + $CompletionPath)
    }
    git check-ignore -q -- $CompletionPath
    if ($LASTEXITCODE -ne 0) { throw ('NEEDS_CONTEXT: sealed completion record is not ignored: ' + $CompletionPath) }
}
$Task1CompletionSha256 = (Get-FileHash -LiteralPath $Task1CompletionRecord -Algorithm SHA256).Hash
$Task2CompletionSha256 = (Get-FileHash -LiteralPath $Task2CompletionRecord -Algorithm SHA256).Hash
function Get-Task3RawJsonObjectKeys([string]$Json, [string]$Context) {
    $Stack = New-Object 'System.Collections.Generic.Stack[object]'
    $Keys = New-Object 'System.Collections.Generic.List[string]'
    for ($Index = 0; $Index -lt $Json.Length; $Index++) {
        $Character = $Json[$Index]
        if ($Character -eq '{') {
            $Stack.Push((New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::Ordinal)))
        } elseif ($Character -eq '[') {
            $Stack.Push($null)
        } elseif ($Character -eq '}' -or $Character -eq ']') {
            if ($Stack.Count -eq 0) { throw ('NEEDS_CONTEXT: unbalanced raw JSON ' + $Context) }
            [void]$Stack.Pop()
        } elseif ($Character -eq '"') {
            $Start = $Index
            $Escaped = $false
            do {
                $Index++
                if ($Index -ge $Json.Length) { throw ('NEEDS_CONTEXT: unterminated JSON string ' + $Context) }
                if ($Escaped) { $Escaped = $false; continue }
                if ($Json[$Index] -eq '\') { $Escaped = $true; continue }
            } while ($Json[$Index] -ne '"')
            $After = $Index + 1
            while ($After -lt $Json.Length -and [char]::IsWhiteSpace($Json[$After])) { $After++ }
            if ($After -lt $Json.Length -and $Json[$After] -eq ':') {
                if ($Stack.Count -eq 0 -or $null -eq $Stack.Peek()) { throw ('NEEDS_CONTEXT: JSON key outside object ' + $Context) }
                $RawToken = $Json.Substring($Start, $Index - $Start + 1)
                $Key = [string]($RawToken | ConvertFrom-Json -ErrorAction Stop)
                if (-not $Stack.Peek().Add($Key)) { throw ('NEEDS_CONTEXT: duplicate JSON object key ' + $Key + ' ' + $Context) }
                [void]$Keys.Add($Key)
            }
        }
    }
    if ($Stack.Count -ne 0) { throw ('NEEDS_CONTEXT: unbalanced raw JSON containers ' + $Context) }
    return $Keys.ToArray()
}
function Get-Task3ParsedJsonObjectKeys($Value) {
    $Keys = New-Object 'System.Collections.Generic.List[string]'
    if ($Value -is [pscustomobject]) {
        foreach ($Property in $Value.PSObject.Properties) {
            [void]$Keys.Add($Property.Name)
            foreach ($Nested in @(Get-Task3ParsedJsonObjectKeys $Property.Value)) { [void]$Keys.Add($Nested) }
        }
    } elseif ($Value -is [Array]) {
        foreach ($Element in $Value) {
            foreach ($Nested in @(Get-Task3ParsedJsonObjectKeys $Element)) { [void]$Keys.Add($Nested) }
        }
    }
    return $Keys.ToArray()
}
function Get-Task3KeyCountRows([string[]]$Keys) {
    $Counts = New-Object 'System.Collections.Generic.Dictionary[string,int]' ([StringComparer]::Ordinal)
    foreach ($Key in @($Keys)) {
        if ($Counts.ContainsKey($Key)) {
            $Counts[$Key] = $Counts[$Key] + 1
        } else {
            $Counts.Add($Key, 1)
        }
    }
    return @($Counts.GetEnumerator() | ForEach-Object { $_.Key + '=' + [string]$_.Value })
}
function Read-Task3StrictJsonObject([string]$Path, [string]$Context) {
    $Raw = [IO.File]::ReadAllBytes($Path)
    if ($Raw.Length -eq 0 -or
        ($Raw.Length -ge 3 -and $Raw[0] -eq 0xEF -and $Raw[1] -eq 0xBB -and $Raw[2] -eq 0xBF)) {
        throw ('NEEDS_CONTEXT: JSON is empty or has a BOM ' + $Context + '; do not invoke Opus.')
    }
    $Text = $StrictUtf8.GetString($Raw)
    if ($Text.Contains([char]0xFFFD)) {
        throw ('NEEDS_CONTEXT: JSON is not strict UTF-8 ' + $Context + '; do not invoke Opus.')
    }
    $RawPropertyKeys = @(Get-Task3RawJsonObjectKeys $Text $Context)
    $Record = $Text | ConvertFrom-Json -ErrorAction Stop
    $ParsedPropertyKeys = @(Get-Task3ParsedJsonObjectKeys $Record)
    $RawPropertyCounts = @(Get-Task3KeyCountRows $RawPropertyKeys)
    $ParsedPropertyCounts = @(Get-Task3KeyCountRows $ParsedPropertyKeys)
    if (Compare-Object $ParsedPropertyCounts $RawPropertyCounts -CaseSensitive) {
        throw ('NEEDS_CONTEXT: raw JSON property-token counts do not exactly match parsed properties ' + $Context)
    }
    return $Record
}
function Test-Task3IntegralValue($Value) {
    return ($Value -is [sbyte] -or $Value -is [byte] -or
        $Value -is [int16] -or $Value -is [uint16] -or
        $Value -is [int] -or $Value -is [uint32] -or
        $Value -is [long] -or $Value -is [uint64])
}
function Assert-Task3FileSealStrict($Seal, [string]$Context) {
    $ExpectedProperties = @('path','bytes','sha256')
    if ($Seal -isnot [pscustomobject] -or
        (@($Seal.PSObject.Properties.Name) -join '|') -cne ($ExpectedProperties -join '|') -or
        $Seal.path -isnot [string] -or -not [IO.Path]::IsPathRooted([string]$Seal.path) -or
        -not (Test-Path -LiteralPath ([string]$Seal.path) -PathType Leaf) -or
        -not (Test-Task3IntegralValue $Seal.bytes) -or [int64]$Seal.bytes -lt 0 -or
        $Seal.sha256 -isnot [string] -or [string]$Seal.sha256 -cnotmatch '^[0-9A-F]{64}$') {
        throw ('NEEDS_CONTEXT: invalid Task 2 file seal ' + $Context + '; do not invoke Opus.')
    }
    $ResolvedPath = (Resolve-Path -LiteralPath ([string]$Seal.path)).Path
    if ($ResolvedPath -cne [string]$Seal.path -or
        (Get-Item -LiteralPath $ResolvedPath).Length -ne [int64]$Seal.bytes -or
        (Get-FileHash -LiteralPath $ResolvedPath -Algorithm SHA256).Hash -cne [string]$Seal.sha256) {
        throw ('NEEDS_CONTEXT: Task 2 sealed artifact drifted ' + $Context + '; do not invoke Opus.')
    }
}
function Test-Task3FileSealIdentity($Left, $Right) {
    return ($Left -is [pscustomobject] -and $Right -is [pscustomobject] -and
        [string]$Left.path -ceq [string]$Right.path -and
        (Test-Task3IntegralValue $Left.bytes) -and (Test-Task3IntegralValue $Right.bytes) -and
        [int64]$Left.bytes -eq [int64]$Right.bytes -and
        [string]$Left.sha256 -ceq [string]$Right.sha256)
}
function New-Task3ExternallyBoundSeal([string]$Path, [string]$ExpectedSha256) {
    if ($ExpectedSha256 -cnotmatch '^[0-9A-F]{64}$') {
        throw ('NEEDS_CONTEXT: invalid externally bound hash for ' + $Path)
    }
    $FullPath = (Resolve-Path -LiteralPath $Path).Path
    $Item = Get-Item -LiteralPath $FullPath -ErrorAction Stop
    if ((Get-FileHash -LiteralPath $FullPath -Algorithm SHA256).Hash -cne $ExpectedSha256) {
        throw ('NEEDS_CONTEXT: externally bound artifact drifted ' + $FullPath + '; do not invoke Opus.')
    }
    return [pscustomobject][ordered]@{
        path = $FullPath
        bytes = [long]$Item.Length
        sha256 = $ExpectedSha256
    }
}
function Add-Task3ArtifactSeal($Lookup, $Seal, [string]$Context) {
    $null = Assert-Task3FileSealStrict $Seal $Context
    if ($Lookup.ContainsKey([string]$Seal.path)) {
        if (-not (Test-Task3FileSealIdentity $Lookup[[string]$Seal.path] $Seal)) {
            throw ('NEEDS_CONTEXT: conflicting Task 2 artifact seals for ' + [string]$Seal.path)
        }
        return
    }
    $Lookup.Add([string]$Seal.path, [pscustomobject][ordered]@{
        path = [string]$Seal.path
        bytes = [long]$Seal.bytes
        sha256 = [string]$Seal.sha256
    })
}
function Assert-Task3Task2Completion([string]$Context) {
    if (-not (Get-Item -LiteralPath $Task1CompletionRecord).IsReadOnly -or
        -not (Get-Item -LiteralPath $Task2CompletionRecord).IsReadOnly -or
        (Get-FileHash -LiteralPath $Task1CompletionRecord -Algorithm SHA256).Hash -cne $Task1CompletionSha256 -or
        (Get-FileHash -LiteralPath $Task2CompletionRecord -Algorithm SHA256).Hash -cne $Task2CompletionSha256) {
        throw ('NEEDS_CONTEXT: Task 1/2 completion hash drifted ' + $Context + '; do not invoke Opus.')
    }
    $Record = Read-Task3StrictJsonObject $Task2CompletionRecord ('Task 2 completion ' + $Context)
    $ExpectedProperties = @(
        'schema_version','verdict','approved_plan_lock_sha256','task1_completion_path',
        'task1_completion_sha256','approved_plan_commit','rules_commit','rules_parent_commit',
        'rules_subject','rules_paths','invocation_count','invocations','artifact_count','artifacts','finished_utc'
    )
    $ExpectedNames = @(
        'rules-red','rules-green','catalog-green','balance-green','winter-invariance-green',
        'missing-portraits-green','narration-overlap-green','show-before-green','lint-green'
    )
    $ExpectedRulesPaths = @('game/balance.rpy','game/difficulty.rpy','game/test_game.rpy')
    $ExpectedInvocationContract = [ordered]@{
        'rules-red' = [pscustomobject]@{ kind='suite'; expected='FAILED'; direct_count=1; source_count=0 }
        'rules-green' = [pscustomobject]@{ kind='suite'; expected='PASSED'; direct_count=1; source_count=0 }
        'catalog-green' = [pscustomobject]@{ kind='suite'; expected='PASSED'; direct_count=1; source_count=0 }
        'balance-green' = [pscustomobject]@{ kind='suite'; expected='PASSED'; direct_count=1; source_count=0 }
        'winter-invariance-green' = [pscustomobject]@{ kind='suite'; expected='PASSED'; direct_count=1; source_count=0 }
        'missing-portraits-green' = [pscustomobject]@{ kind='scanner'; expected='PASS'; direct_count=2; source_count=0 }
        'narration-overlap-green' = [pscustomobject]@{ kind='scanner'; expected='PASS'; direct_count=2; source_count=0 }
        'show-before-green' = [pscustomobject]@{ kind='scanner'; expected='PASS'; direct_count=3; source_count=1 }
        'lint-green' = [pscustomobject]@{ kind='lint'; expected='PASS'; direct_count=1; source_count=0 }
    }
    if ($Record -isnot [pscustomobject] -or
        (@($Record.PSObject.Properties.Name) -join '|') -cne ($ExpectedProperties -join '|') -or
        $Record.schema_version -isnot [int] -or [int]$Record.schema_version -ne 1 -or
        $Record.verdict -isnot [string] -or [string]$Record.verdict -cne 'PASS' -or
        $Record.approved_plan_lock_sha256 -isnot [string] -or [string]$Record.approved_plan_lock_sha256 -cne $ApprovalLockSha256 -or
        $Record.task1_completion_path -isnot [string] -or [string]$Record.task1_completion_path -cne (Resolve-Path -LiteralPath $Task1CompletionRecord).Path -or
        $Record.task1_completion_sha256 -isnot [string] -or [string]$Record.task1_completion_sha256 -cne $Task1CompletionSha256 -or
        $Record.approved_plan_commit -isnot [string] -or [string]$Record.approved_plan_commit -cne [string]$ApprovalRecord.approved_plan_commit -or
        $Record.rules_commit -isnot [string] -or [string]$Record.rules_commit -cne $ExpectedRulesCommit -or
        $Record.rules_parent_commit -isnot [string] -or [string]$Record.rules_parent_commit -cne [string]$ApprovalRecord.approved_plan_commit -or
        $Record.rules_subject -isnot [string] -or [string]$Record.rules_subject -cne 'fix: enforce terminal resistance collapse rules' -or
        $Record.rules_paths -isnot [Array] -or @($Record.rules_paths | Where-Object { $_ -isnot [string] }).Count -ne 0 -or
        (@($Record.rules_paths) -join '|') -cne ($ExpectedRulesPaths -join '|') -or
        $Record.invocation_count -isnot [int] -or [int]$Record.invocation_count -ne 9 -or
        $Record.invocations -isnot [Array] -or @($Record.invocations).Count -ne 9 -or
        (@($Record.invocations.record.name) -join '|') -cne ($ExpectedNames -join '|') -or
        $Record.artifact_count -isnot [int] -or [int]$Record.artifact_count -ne 56 -or
        $Record.artifacts -isnot [Array] -or @($Record.artifacts).Count -ne 56 -or
        $Record.finished_utc -isnot [string]) {
        throw ('NEEDS_CONTEXT: Task 2 completion top-level contract failed ' + $Context + '; do not invoke Opus.')
    }
    try {
        [void][DateTimeOffset]::ParseExact(
            [string]$Record.finished_utc,
            'o',
            [Globalization.CultureInfo]::InvariantCulture,
            [Globalization.DateTimeStyles]::RoundtripKind
        )
    } catch {
        throw ('NEEDS_CONTEXT: Task 2 completion timestamp failed ' + $Context + '; do not invoke Opus.')
    }

    $ArtifactLookup = New-Object 'System.Collections.Generic.Dictionary[string,object]' ([StringComparer]::OrdinalIgnoreCase)
    foreach ($FixedSeal in @(
        (New-Task3ExternallyBoundSeal $ApprovalLockPath $ApprovalLockSha256),
        (New-Task3ExternallyBoundSeal $Task1CompletionRecord $Task1CompletionSha256),
        (New-Task3ExternallyBoundSeal $ThisPlan ([string]$ApprovalRecord.plan_sha256)),
        (New-Task3ExternallyBoundSeal $DesignPath ([string]$ApprovalRecord.spec_sha256))
    )) {
        Add-Task3ArtifactSeal $ArtifactLookup $FixedSeal 'fixed Task 2 authority'
    }

    $ReceiptProperties = @(
        'schema_version','name','kind','expected','actual','verdict','helper_evidence_dir',
        'helper_artifacts','helper_result','runner_or_scanner_evidence_dir','direct_evidence',
        'source_evidence','assertions','created_utc'
    )
    $AssertionProperties = @('central_safety_envelope','outcome_gates','runner_or_scanner')
    $InvocationArray = @($Record.invocations)
    for ($InvocationIndex = 0; $InvocationIndex -lt 9; $InvocationIndex++) {
        $Invocation = $InvocationArray[$InvocationIndex]
        $ExpectedName = $ExpectedNames[$InvocationIndex]
        $Contract = $ExpectedInvocationContract[$ExpectedName]
        if ($Invocation -isnot [pscustomobject] -or
            (@($Invocation.PSObject.Properties.Name) -join '|') -cne 'receipt|record' -or
            $Invocation.receipt -isnot [pscustomobject] -or
            $Invocation.record -isnot [pscustomobject]) {
            throw ('NEEDS_CONTEXT: Task 2 invocation wrapper failed at index ' + [string]$InvocationIndex)
        }
        $null = Assert-Task3FileSealStrict $Invocation.receipt ('receipt ' + $ExpectedName)
        $Receipt = $Invocation.record
        if ((@($Receipt.PSObject.Properties.Name) -join '|') -cne ($ReceiptProperties -join '|') -or
            $Receipt.schema_version -isnot [int] -or [int]$Receipt.schema_version -ne 1 -or
            $Receipt.name -isnot [string] -or [string]$Receipt.name -cne $ExpectedName -or
            $Receipt.kind -isnot [string] -or [string]$Receipt.kind -cne [string]$Contract.kind -or
            $Receipt.expected -isnot [string] -or [string]$Receipt.expected -cne [string]$Contract.expected -or
            $Receipt.actual -isnot [string] -or [string]$Receipt.actual -cne [string]$Contract.expected -or
            $Receipt.verdict -isnot [string] -or [string]$Receipt.verdict -cne 'PASS' -or
            $Receipt.helper_evidence_dir -isnot [string] -or
            $Receipt.helper_artifacts -isnot [Array] -or
            $Receipt.helper_result -isnot [pscustomobject] -or
            $Receipt.runner_or_scanner_evidence_dir -isnot [string] -or
            $Receipt.direct_evidence -isnot [Array] -or
            $Receipt.source_evidence -isnot [Array] -or
            $Receipt.assertions -isnot [pscustomobject] -or
            (@($Receipt.assertions.PSObject.Properties.Name) -join '|') -cne ($AssertionProperties -join '|') -or
            @($Receipt.assertions.PSObject.Properties.Value | Where-Object { $_ -isnot [string] -or [string]$_ -cne 'PASS' }).Count -ne 0 -or
            $Receipt.created_utc -isnot [string]) {
            throw ('NEEDS_CONTEXT: Task 2 invocation receipt contract failed for ' + $ExpectedName)
        }
        try {
            [void][DateTimeOffset]::ParseExact(
                [string]$Receipt.created_utc,
                'o',
                [Globalization.CultureInfo]::InvariantCulture,
                [Globalization.DateTimeStyles]::RoundtripKind
            )
        } catch {
            throw ('NEEDS_CONTEXT: receipt timestamp failed for ' + $ExpectedName)
        }
        if (-not [IO.Path]::IsPathRooted([string]$Receipt.helper_evidence_dir) -or
            -not (Test-Path -LiteralPath ([string]$Receipt.helper_evidence_dir) -PathType Container) -or
            -not [IO.Path]::IsPathRooted([string]$Receipt.runner_or_scanner_evidence_dir) -or
            -not (Test-Path -LiteralPath ([string]$Receipt.runner_or_scanner_evidence_dir) -PathType Container)) {
            throw ('NEEDS_CONTEXT: receipt directory contract failed for ' + $ExpectedName)
        }
        $HelperFull = (Resolve-Path -LiteralPath ([string]$Receipt.helper_evidence_dir)).Path
        $RunnerOrScannerFull = (Resolve-Path -LiteralPath ([string]$Receipt.runner_or_scanner_evidence_dir)).Path
        if ([string]$Receipt.helper_evidence_dir -cne $HelperFull -or
            [string]$Receipt.runner_or_scanner_evidence_dir -cne $RunnerOrScannerFull -or
            [string]$Invocation.receipt.path -cne [IO.Path]::GetFullPath((Join-Path $HelperFull 'invocation-receipt.json'))) {
            throw ('NEEDS_CONTEXT: receipt path/directory relation failed for ' + $ExpectedName)
        }
        if (@($Receipt.helper_artifacts).Count -ne 4 -or
            @($Receipt.direct_evidence).Count -ne [int]$Contract.direct_count -or
            @($Receipt.source_evidence).Count -ne [int]$Contract.source_count) {
            throw ('NEEDS_CONTEXT: receipt cardinality failed for ' + $ExpectedName)
        }
        foreach ($Seal in @($Receipt.helper_artifacts) + @($Receipt.helper_result) +
            @($Receipt.direct_evidence) + @($Receipt.source_evidence)) {
            $null = Assert-Task3FileSealStrict $Seal ('receipt artifact ' + $ExpectedName)
        }
        $ExpectedHelperPaths = @(
            [IO.Path]::GetFullPath((Join-Path $HelperFull 'request.json'))
            [IO.Path]::GetFullPath((Join-Path $HelperFull 'stdout.txt'))
            [IO.Path]::GetFullPath((Join-Path $HelperFull 'stderr.txt'))
            [IO.Path]::GetFullPath((Join-Path $HelperFull 'result.json'))
        )
        for ($HelperIndex = 0; $HelperIndex -lt 4; $HelperIndex++) {
            if ([string]$Receipt.helper_artifacts[$HelperIndex].path -cne $ExpectedHelperPaths[$HelperIndex]) {
                throw ('NEEDS_CONTEXT: helper artifact order/path failed for ' + $ExpectedName)
            }
        }
        if (-not (Test-Task3FileSealIdentity $Receipt.helper_result $Receipt.helper_artifacts[3])) {
            throw ('NEEDS_CONTEXT: helper_result relation failed for ' + $ExpectedName)
        }
        if ([string]$Contract.kind -ceq 'scanner') {
            if ($RunnerOrScannerFull -cne $HelperFull -or
                -not (Test-Task3FileSealIdentity $Receipt.direct_evidence[0] $Receipt.helper_artifacts[1]) -or
                -not (Test-Task3FileSealIdentity $Receipt.direct_evidence[1] $Receipt.helper_artifacts[2])) {
                throw ('NEEDS_CONTEXT: scanner stdout/stderr relation failed for ' + $ExpectedName)
            }
        } else {
            $ExpectedExtension = if ([string]$Contract.kind -ceq 'suite') { '.log' } else { '.txt' }
            if ([IO.Path]::GetDirectoryName([string]$Receipt.direct_evidence[0].path) -cne $RunnerOrScannerFull -or
                [IO.Path]::GetExtension([string]$Receipt.direct_evidence[0].path) -cne $ExpectedExtension) {
                throw ('NEEDS_CONTEXT: suite/lint evidence relation failed for ' + $ExpectedName)
            }
        }
        if ($ExpectedName -ceq 'show-before-green') {
            $ExpectedShowSource = [IO.Path]::GetFullPath((Join-Path $EvidenceRoot 'rules\scanner-show-before-source\show-before-scan.py'))
            if ([string]$Receipt.source_evidence[0].path -cne $ExpectedShowSource -or
                -not (Test-Task3FileSealIdentity $Receipt.source_evidence[0] $Receipt.direct_evidence[2])) {
                throw 'NEEDS_CONTEXT: show-before exact source/direct relation failed.'
            }
        }

        $PhysicalReceipt = Read-Task3StrictJsonObject ([string]$Invocation.receipt.path) ('physical receipt ' + $ExpectedName)
        if ($PhysicalReceipt -isnot [pscustomobject] -or
            ($PhysicalReceipt | ConvertTo-Json -Depth 10 -Compress) -cne
                ($Receipt | ConvertTo-Json -Depth 10 -Compress)) {
            throw ('NEEDS_CONTEXT: physical receipt differs from embedded record for ' + $ExpectedName)
        }

        Add-Task3ArtifactSeal $ArtifactLookup $Invocation.receipt ('receipt ' + $ExpectedName)
        foreach ($Seal in @($Receipt.helper_artifacts)) {
            Add-Task3ArtifactSeal $ArtifactLookup $Seal ('helper artifact ' + $ExpectedName)
        }
        foreach ($Seal in @($Receipt.direct_evidence)) {
            Add-Task3ArtifactSeal $ArtifactLookup $Seal ('direct evidence ' + $ExpectedName)
        }
        foreach ($Seal in @($Receipt.source_evidence)) {
            Add-Task3ArtifactSeal $ArtifactLookup $Seal ('source evidence ' + $ExpectedName)
        }
    }

    $ExpectedArtifacts = @($ArtifactLookup.Values | Sort-Object path)
    if ($ExpectedArtifacts.Count -ne 56) {
        throw ('NEEDS_CONTEXT: exact Task 2 artifact union must contain 56 files; found ' + [string]$ExpectedArtifacts.Count)
    }
    $ObservedArtifacts = @($Record.artifacts)
    for ($ArtifactIndex = 0; $ArtifactIndex -lt 56; $ArtifactIndex++) {
        $null = Assert-Task3FileSealStrict $ObservedArtifacts[$ArtifactIndex] ('completion artifact index ' + [string]$ArtifactIndex)
        if (-not (Test-Task3FileSealIdentity $ObservedArtifacts[$ArtifactIndex] $ExpectedArtifacts[$ArtifactIndex])) {
            throw ('NEEDS_CONTEXT: Task 2 artifact union differs at index ' + [string]$ArtifactIndex + ' ' + $Context)
        }
    }
}
Assert-Task3Task2Completion 'at Task 3 start'
```

- [ ] **Step 1: Reconfirm the mandatory three-candidate branch**

Only after Step 0 passes, read `CANON.md`, `CLAUDE.md`, `docs/writing-style/INDEX.md`, and `docs/writing-style/guidance.md` in full. Assert that the style index still reports seed maturity and no active approved examples, and that the guidance table has no active row. If an active approved corpus or guidance row now exists, stop and revise this plan before generating anything; do not silently switch workflows or omit approved guidance from the prompts.

Continue in the same session and verify that `game/chapter5.rpy` and `game/endings_expansion.rpy` remain unmodified:

```powershell
$GuidancePath = Join-Path $ProjectRoot 'docs\writing-style\guidance.md'
if (-not (Test-Path -LiteralPath $GuidancePath -PathType Leaf)) {
    throw 'Writing-style guidance is missing.'
}
$GuidanceLines = [IO.File]::ReadAllLines($GuidancePath, $StrictUtf8)
$GuidanceHeaderIndexes = @(
    for ($Index = 0; $Index -lt $GuidanceLines.Count; $Index++) {
        if ($GuidanceLines[$Index].Trim().StartsWith('| guidance_id |', [StringComparison]::Ordinal)) {
            $Index
        }
    }
)
if ($GuidanceHeaderIndexes.Count -ne 1) {
    throw 'Writing-style guidance does not contain exactly one canonical table header.'
}
$GuidanceHeaderIndex = [int]$GuidanceHeaderIndexes[0]
if ($GuidanceHeaderIndex + 1 -ge $GuidanceLines.Count -or
    $GuidanceLines[$GuidanceHeaderIndex + 1].Trim() -notmatch '^\|(?:\s*:?-+:?\s*\|)+$') {
    throw 'Writing-style guidance table separator is malformed.'
}
$ActiveGuidanceRows = @(
    for ($Index = $GuidanceHeaderIndex + 2; $Index -lt $GuidanceLines.Count; $Index++) {
        if (-not [string]::IsNullOrWhiteSpace($GuidanceLines[$Index])) {
            $GuidanceLines[$Index]
        }
    }
)
if ($ActiveGuidanceRows.Count -ne 0) {
    throw 'Active approved guidance now exists; stop and revise all three prompts before invoking Opus.'
}
if (@(git status --short -- game/chapter5.rpy game/endings_expansion.rpy).Count -ne 0) {
    throw 'Visible finale prose changed before raw-copy approval.'
}
$CopyRoot = Join-Path $EvidenceRoot 'copy'
$RunRoots = @(
    (Join-Path $CopyRoot 'run-01'),
    (Join-Path $CopyRoot 'run-02'),
    (Join-Path $CopyRoot 'run-03')
)
foreach ($RunRoot in $RunRoots) {
    if (Test-Path -LiteralPath $RunRoot) {
        throw "Copy run directory already exists: $RunRoot"
    }
    [IO.Directory]::CreateDirectory($RunRoot) | Out-Null
}
```

- [ ] **Step 2: Create three byte-identical self-contained prompts with `apply_patch`**

Use `apply_patch` separately to create `prompt.txt` in each of the three run directories. Each file must contain exactly the following UTF-8 text and end with one newline:

```text
为中文 Ren'Py 政治剧情游戏《权谋之庭》写一份终章失败结局候选文案包。只输出一个 JSON 对象，不要 Markdown，不要解释，不要代码围栏。

任务背景：
- 玩家可能一路耗尽财富、失去军心、失去所有组织性援助，却仍因个人权力达到普通难度保底门槛而进入铁腕路线。
- 新规则会让这种军队在强行开战后战败，退回艾登堡；城堡大厅最终被攻破。
- 主角必须拿着父亲留下的剑在大厅作最后抵抗，并在大厅内明确战死。不能写“下落不明”、失踪、可能生还或开放式结局。
- 这是失败结局“艾登堡陷落”；现有结局键、成就和后续第三人称尾声保持不变。
- 主角战死后不再播放任何“你后来听说、你保存物件、你打听消息”之类的活人第二人称角色命运段落。新文案要自然收束到第三人称的“城破之后”尾声。

入口事实：
- fall_cause="inaction"：玩家在最终选择中主动放弃抵抗。可以保留“本可做得更多”的责问。
- fall_cause="battle"：玩家发动了一场明知资源与军心都已经崩盘的绝望战争，战败后退守城堡。必须写成强行开战后的失败，不能说“什么也没做”。
- fall_cause=""：旧存档或未知入口。使用中性陈述，不虚构玩家动机。

男爵对白修正事实：
- 直接铁腕路线中 rel_baron>0 只代表男爵保持中立、至少不背刺。
- 男爵没有带兵加入，没有“近四百人”，也没有“北坡汇合”。
- 需要两句简短对白：雷恩报告中立事实，主角回应。

现有场景连续上下文：
- 城破前：王后军从南边压来，男爵军在北边保持自己的行动；艾登堡守军极少。
- 大厅着火。艾琳娜、英格丽或赛琳的既有条件段已经处理她们是否离开/在海上，不能新增或改写她们的命运。
- 主角已经抓起父亲的剑，站在桌子后面；门外脚步越来越近；门随后被踹开。
- 现有安全尾声从主角死后的第三人称世界开始：大火烧三天，雪压熄余火，军队撤走，幸存者返乡，最后落到史书的一行记录。不要重写这段尾声。

人物事实：
- 主角是年轻领主。
- 雷恩是老兵队长。
- 不新增世界观、人名、军队、神器、地点、资产、音效或未给出的角色命运。
- 使用简体中文。字符串中不要包含未转义的 ASCII 双引号。

输出必须是以下精确 JSON 结构，键不得增删：
{
  "baron_neutral_exchange": [
    {"speaker": "captain", "text": "雷恩的一句报告"},
    {"speaker": "player", "text": "主角的一句回应"}
  ],
  "fall_reflections": {
    "inaction": "主动放弃入口的一句短反思",
    "battle": "绝望会战失败入口的一句短反思",
    "neutral": "未知入口的一句中性短反思"
  },
  "death_sequence": [
    {"speaker": "narrator 或 player 或 centered", "text": "逐条可直接接入 Ren'Py 的可见文本"}
  ],
  "fall_cause_cards": {
    "inaction": "死亡确认后的主动放弃收束句",
    "battle": "死亡确认后的会战失败收束句",
    "neutral": "死亡确认后的中性收束句"
  },
  "game_ending_summaries": {
    "inaction": "通用结算页的一句主动放弃摘要",
    "battle": "通用结算页的一句会战失败摘要",
    "neutral": "通用结算页的一句中性摘要"
  },
  "epilogue_bridge": "从明确战死转入第三人称城破尾声的一句桥接文本"
}

额外硬约束：
- baron_neutral_exchange 必须恰好 2 项，speaker 顺序必须是 captain、player。
- death_sequence 必须 8 至 14 项；只允许 speaker=narrator、player、centered。
- death_sequence 必须明确写出主角被杀或停止呼吸，读者不能合理理解为生还。
- death_sequence 不得决定雷恩、奥尔德里克、艾琳娜、英格丽或赛琳的最终命运。
- 三个 cause 变体必须语义不同；battle 不能出现“什么也没做”，neutral 不能责怪玩家主动放弃。
- 所有值都必须是最终候选文本，不要使用括号说明、TODO、占位符或备选写法。
```

After all three `apply_patch` operations, verify strict UTF-8, no BOM/replacement character, nonempty bytes, and identical SHA-256:

```powershell
$StrictUtf8 = New-Object System.Text.UTF8Encoding($false, $true)
$PromptHashes = @()
foreach ($RunRoot in $RunRoots) {
    $PromptPath = Join-Path $RunRoot 'prompt.txt'
    $Bytes = [IO.File]::ReadAllBytes($PromptPath)
    if ($Bytes.Length -eq 0) { throw "Empty prompt: $PromptPath" }
    if ($Bytes.Length -ge 3 -and $Bytes[0] -eq 0xEF -and $Bytes[1] -eq 0xBB -and $Bytes[2] -eq 0xBF) {
        throw "Prompt has UTF-8 BOM: $PromptPath"
    }
    $Decoded = $StrictUtf8.GetString($Bytes)
    if ($Decoded.Contains([char]0xFFFD)) { throw "Prompt has replacement character: $PromptPath" }
    $PromptHashes += (Get-FileHash -Algorithm SHA256 $PromptPath).Hash
}
if (@($PromptHashes | Select-Object -Unique).Count -ne 1) {
    throw 'The three candidate prompts are not byte-identical.'
}
```

- [ ] **Step 3: Invoke three fresh Opus sessions sequentially with no fallback**

```powershell
$Launcher = 'C:\Users\22325\.codex\skills\invoke-opus-4-6\scripts\invoke-opus.ps1'
if (-not (Test-Path -LiteralPath $Launcher -PathType Leaf)) {
    throw 'Verified Opus launcher is missing.'
}

$VerifiedRuns = @()
function Assert-ExactJsonProperties([object]$Value, [string[]]$Expected, [string]$Context) {
    if ($Value -isnot [pscustomobject]) { throw "$Context must be one JSON object." }
    $Actual = @($Value.PSObject.Properties.Name | Sort-Object)
    $SortedExpected = @($Expected | Sort-Object)
    if (Compare-Object $SortedExpected $Actual) { throw "$Context has an inexact property set." }
}
function Assert-NonemptyJsonString([object]$Value, [string]$Context) {
    if ($Value -isnot [string] -or [string]::IsNullOrWhiteSpace([string]$Value)) {
        throw "$Context must be a nonempty JSON string."
    }
}
foreach ($RunRoot in $RunRoots) {
    Assert-Task3ApprovalState ('immediately before Opus invocation for ' + $RunRoot)
    Assert-Task3Task2Completion ('immediately before Opus invocation for ' + $RunRoot)
    $PromptPath = Join-Path $RunRoot 'prompt.txt'
    try {
        $SummaryText = (& $Launcher -PromptFile $PromptPath -OutputDirectory $RunRoot -ErrorAction Stop | Out-String).Trim()
    } catch {
        throw "Opus launcher failed for $RunRoot. Do not retry or continue. $($_.Exception.Message)"
    }
    if ([string]::IsNullOrWhiteSpace($SummaryText)) { throw "Opus launcher returned no summary: $RunRoot" }
    try {
        $Summary = $SummaryText | ConvertFrom-Json -ErrorAction Stop
    } catch {
        throw "Launcher did not emit one valid JSON summary for $RunRoot. Do not continue."
    }
    $MetadataPath = [string]$Summary.metadata_path
    $ResultPath = [string]$Summary.result_path
    if (-not (Test-Path -LiteralPath $MetadataPath -PathType Leaf)) { throw "Missing metadata: $MetadataPath" }
    if (-not (Test-Path -LiteralPath $ResultPath -PathType Leaf)) { throw "Missing result: $ResultPath" }
    $Metadata = Get-Content -LiteralPath $MetadataPath -Raw -Encoding UTF8 | ConvertFrom-Json
    if ($Metadata.success -isnot [bool] -or -not $Metadata.success) { throw "Run is not successful: $RunRoot" }
    if ([string]$Metadata.model -cne 'claude-opus-4-6') { throw "Wrong model: $RunRoot" }
    if ([string]$Metadata.expected_model -cne 'claude-opus-4-6') { throw "Wrong expected model: $RunRoot" }
    $Observed = @($Metadata.observed_models)
    $UsageModels = @($Metadata.result_model_usage_models)
    if ($Observed.Count -ne 1 -or [string]$Observed[0] -cne 'claude-opus-4-6') { throw "Observed-model proof failed: $RunRoot" }
    if ($UsageModels.Count -ne 1 -or [string]$UsageModels[0] -cne 'claude-opus-4-6') { throw "Result-usage proof failed: $RunRoot" }

    $ResultBytes = [IO.File]::ReadAllBytes($ResultPath)
    if ($ResultBytes.Length -eq 0) { throw "Empty terminal result: $RunRoot" }
    $ResultText = $StrictUtf8.GetString($ResultBytes)
    if ($ResultText.Contains([char]0xFFFD)) { throw "Invalid UTF-8 terminal result: $RunRoot" }
    try {
        $Document = $ResultText | ConvertFrom-Json -ErrorAction Stop
    } catch {
        throw "Terminal result is not the required JSON object: $RunRoot"
    }
    $ExpectedKeys = @('baron_neutral_exchange', 'death_sequence', 'epilogue_bridge', 'fall_cause_cards', 'fall_reflections', 'game_ending_summaries')
    Assert-ExactJsonProperties $Document $ExpectedKeys "$RunRoot top level"
    if (@($Document.baron_neutral_exchange).Count -ne 2) { throw "Baron exchange count drift: $RunRoot" }
    for ($EntryIndex = 0; $EntryIndex -lt 2; $EntryIndex++) {
        $Entry = $Document.baron_neutral_exchange[$EntryIndex]
        Assert-ExactJsonProperties $Entry @('speaker', 'text') "$RunRoot baron entry $EntryIndex"
        Assert-NonemptyJsonString $Entry.speaker "$RunRoot baron speaker $EntryIndex"
        Assert-NonemptyJsonString $Entry.text "$RunRoot baron text $EntryIndex"
    }
    if ($Document.baron_neutral_exchange[0].speaker -cne 'captain' -or $Document.baron_neutral_exchange[1].speaker -cne 'player') { throw "Baron exchange speaker order drift: $RunRoot" }
    foreach ($MapName in @('fall_reflections', 'fall_cause_cards', 'game_ending_summaries')) {
        $Map = $Document.$MapName
        Assert-ExactJsonProperties $Map @('inaction', 'battle', 'neutral') "$RunRoot $MapName"
        foreach ($Cause in @('inaction', 'battle', 'neutral')) {
            Assert-NonemptyJsonString $Map.$Cause "$RunRoot $MapName.$Cause"
        }
    }
    Assert-NonemptyJsonString $Document.epilogue_bridge "$RunRoot epilogue_bridge"
    if (@($Document.death_sequence).Count -lt 8 -or @($Document.death_sequence).Count -gt 14) { throw "Death sequence count drift: $RunRoot" }
    $DeathTexts = @()
    foreach ($Entry in @($Document.death_sequence)) {
        Assert-ExactJsonProperties $Entry @('speaker', 'text') "$RunRoot death entry"
        Assert-NonemptyJsonString $Entry.speaker "$RunRoot death speaker"
        Assert-NonemptyJsonString $Entry.text "$RunRoot death text"
        if (@('narrator', 'player', 'centered') -cnotcontains [string]$Entry.speaker) { throw "Illegal death-sequence speaker: $RunRoot" }
        $DeathTexts += [string]$Entry.text
    }
    $DeathText = $DeathTexts -join ''
    if ($DeathText -notmatch '战死|死在|停止.{0,4}呼吸|没了呼吸|断了气|咽下.{0,4}气|心跳.{0,4}停') {
        throw "Death sequence does not explicitly confirm death: $RunRoot"
    }
    if ([string]$Document.fall_reflections.battle -match '什么也没做' -or [string]$Document.fall_cause_cards.battle -match '什么也没做' -or [string]$Document.game_ending_summaries.battle -match '什么也没做') {
        throw "Battle cause falsely claims inaction: $RunRoot"
    }
    if ($ResultText.Contains('TODO') -or $ResultText.Contains('占位') -or $ResultText.Contains('领主下落不明')) {
        throw "Candidate contains forbidden placeholder or ambiguous-death text: $RunRoot"
    }

    $VerifiedRuns += [pscustomobject][ordered]@{
        run_root = $RunRoot
        prompt_sha256 = (Get-FileHash -Algorithm SHA256 $PromptPath).Hash
        metadata_path = $MetadataPath
        metadata_sha256 = (Get-FileHash -Algorithm SHA256 $MetadataPath).Hash
        result_path = $ResultPath
        result_sha256 = (Get-FileHash -Algorithm SHA256 $ResultPath).Hash
        result_text = $ResultText
    }
}
if ($VerifiedRuns.Count -ne 3) { throw 'Exactly three verified runs are required.' }
if (@($VerifiedRuns.result_sha256 | Select-Object -Unique).Count -lt 2) {
    throw 'Candidate generation produced no meaningful independent variation; stop for review rather than retrying.'
}
```

Run sequentially. If any invocation or provenance check fails, stop immediately, preserve every artifact path, report the failure, and wait for explicit user authorization. Do not retry the failed run in this task.

Before randomization, read each verified JSON result in full and perform a fact-only acceptance check. Do not rank prose quality or edit any candidate. Each candidate must satisfy all of the following:

- it introduces no new named person, army, artifact, place, world rule, art, music, sound effect, or animation;
- it does not decide the fate of Ren, Aldric, Elena, Ingrid, or Selene;
- its neutral cause does not accuse the player of voluntary inaction;
- its battle cause describes failure after the player forces a hopeless battle, never simple passivity;
- its baron exchange says only that the baron remains neutral and supplies no troops, rendezvous, or invented headcount;
- its death sequence unambiguously kills the player character in the burning hall and transitions to the existing third-person aftermath.

For each passing run, create a separate `fact-review.txt` with `apply_patch` in that run directory. It must contain exactly these eight nonempty `key=value` lines in this order: `verdict=PASS`; `result_sha256=` immediately followed by the literal observed hash; `no_new_canon_or_assets=PASS`; `no_side_character_fate=PASS`; `neutral_cause_is_neutral=PASS`; `battle_cause_is_failed_battle=PASS`; `baron_is_neutral_without_troops=PASS`; and `explicit_hall_death_to_epilogue=PASS`. Do not modify the launcher-owned metadata or terminal result. Re-read and bind the review files:

```powershell
$FactKeys = @(
    'no_new_canon_or_assets',
    'no_side_character_fate',
    'neutral_cause_is_neutral',
    'battle_cause_is_failed_battle',
    'baron_is_neutral_without_troops',
    'explicit_hall_death_to_epilogue'
)
foreach ($Run in $VerifiedRuns) {
    $FactPath = Join-Path $Run.run_root 'fact-review.txt'
    $FactBytes = [IO.File]::ReadAllBytes($FactPath)
    $FactText = $StrictUtf8.GetString($FactBytes)
    $FactLines = @($FactText.TrimEnd("`r", "`n").Split("`n") | ForEach-Object { $_.TrimEnd("`r") })
    if ($FactLines.Count -ne 8 -or $FactLines[0] -cne 'verdict=PASS') {
        throw "Fact review shape or verdict failed: $FactPath"
    }
    if ($FactLines[1] -cne ('result_sha256=' + $Run.result_sha256)) {
        throw "Fact review result hash mismatch: $FactPath"
    }
    for ($Index = 0; $Index -lt $FactKeys.Count; $Index++) {
        if ($FactLines[$Index + 2] -cne ($FactKeys[$Index] + '=PASS')) {
            throw "Fact review criterion failed: $FactPath"
        }
    }
    git check-ignore -q $FactPath
    if ($LASTEXITCODE -ne 0) { throw "Fact review is not ignored: $FactPath" }
    $Run | Add-Member -NotePropertyName fact_review_sha256 -NotePropertyValue ((Get-FileHash -Algorithm SHA256 $FactPath).Hash)
}
```

If any candidate fails a fact check, instead record the literal rejection reason in its separate `fact-review.txt`, preserve all three run directories, and stop. Do not retry, replace, rewrite, or silently omit that candidate without explicit user authorization.

- [ ] **Step 4: Randomize candidates and create the ignored blind map with `apply_patch`**

Use a Fisher-Yates shuffle driven by `RandomNumberGenerator`:

```powershell
$Random = [Security.Cryptography.RandomNumberGenerator]::Create()
try {
    $Order = [Collections.Generic.List[int]]::new()
    0..2 | ForEach-Object { $Order.Add($_) }
    for ($Index = $Order.Count - 1; $Index -gt 0; $Index--) {
        $Buffer = New-Object byte[] 4
        $Random.GetBytes($Buffer)
        $Swap = [BitConverter]::ToUInt32($Buffer, 0) % ($Index + 1)
        $Temporary = $Order[$Index]
        $Order[$Index] = $Order[$Swap]
        $Order[$Swap] = $Temporary
    }
} finally {
    $Random.Dispose()
}
$BlindLabels = @('A', 'B', 'C')
$BlindRows = for ($Index = 0; $Index -lt 3; $Index++) {
    $Run = $VerifiedRuns[$Order[$Index]]
    [pscustomobject][ordered]@{
        label = $BlindLabels[$Index]
        run_root = $Run.run_root
        prompt_sha256 = $Run.prompt_sha256
        metadata_sha256 = $Run.metadata_sha256
        result_sha256 = $Run.result_sha256
        fact_review_sha256 = $Run.fact_review_sha256
    }
}
$BlindRows | Format-Table -AutoSize
```

Create `.superpowers/sdd/terminal-collapse-ending/copy/blind-map.md` with `apply_patch`, recording those literal rows and the rules-commit HEAD. This file is reviewer provenance only; never reveal `run_root` or generation order in the user-facing candidate labels.

- [ ] **Step 5: Present the three raw candidates and hard stop**

First prove that Phase A did not drift outside its committed rules slice:

```powershell
$ExpectedRulesSubject = 'fix: enforce terminal resistance collapse rules'
$UnrelatedPlan = 'docs/superpowers/plans/2026-08-09-winter-interlude-narrative-delivery.md'
$UnrelatedPlanHash = '0F39B5F5ACE1D4666DD146863CABDF398B031F5666C29AE337CEB89796E4276C'
if ((git log -1 --format=%s) -cne $ExpectedRulesSubject) {
    throw 'Phase A rules commit subject drifted.'
}
if (@(git diff --cached --name-only).Count -ne 0) { throw 'Index is not empty at the Phase A hard stop.' }
$Status = @(git status --short --untracked-files=all)
if ($Status.Count -ne 1 -or [string]$Status[0] -cne "?? $UnrelatedPlan") {
    throw 'Unexpected tracked or untracked worktree state at the Phase A hard stop.'
}
if ((Get-FileHash -Algorithm SHA256 -LiteralPath $UnrelatedPlan).Hash -cne $UnrelatedPlanHash) {
    throw 'Unrelated winter narrative plan drifted.'
}
if (@(git status --short -- game/chapter5.rpy game/endings_expansion.rpy).Count -ne 0) {
    throw 'Visible finale prose changed before candidate approval.'
}
foreach ($Run in $VerifiedRuns) {
    foreach ($Path in @($Run.metadata_path, $Run.result_path)) {
        git check-ignore -q $Path
        if ($LASTEXITCODE -ne 0) { throw "Candidate evidence is not ignored: $Path" }
    }
}
```

Return a single user message containing:

1. Candidate A's complete verified terminal JSON result.
2. Candidate B's complete verified terminal JSON result.
3. Candidate C's complete verified terminal JSON result.
4. A concise request to select A, B, C, or reject all three.
5. Provenance summary: three successful `claude-opus-4-6` runs and the three anonymous result SHA-256 values, without mapping them to chronological run order.

Do not rank, summarize, rewrite, combine, trim, or recommend a candidate. Do not modify `game/chapter5.rpy`, `game/endings_expansion.rpy`, copy tests, or any shipping asset before the user responds.

**HARD STOP:** Phase A ends here. A user selection is required before any Phase B plan or implementation.

---

## Phase B Continuation Contract (not executable until selection)

After the user selects exactly one raw candidate, first bind its literal `result_sha256` and create `docs/superpowers/plans/2026-08-11-terminal-collapse-ending-phase-b.md`. That second plan must contain complete, selected-copy-specific code and no prose placeholders. It must cover:

- `game/endings_expansion.rpy`: non-reserved `default iron_terminal_collapse_snapshot = None` and `default fall_cause = ""`; leave `ending_fall_epilogue` text unchanged.
- `game/chapter5.rpy`: reset/lock collapse snapshot; branch-entry and post-join guards; collapsed-menu visibility; hard-grind override; `prince_ally and not prince_betrayed` score; `fall_cause` entry writes; approved neutral-baron exchange; approved death sequence and three cause variants; skip `ending_side_characters_fate` for fall while retaining the fall epilogue.
- `game/test_game.rpy`: ordinary-difficulty player-feedback path; prepared frontal/flanking old-menu guards before any branch mutation; `None` mid-branch preservation; exact approved-copy/source contracts; a new `test_terminal_collapse_ending` reaching the unique approved death sentence while restoring persistent state.
- Real old-save validation: every fresh Phase B controller first consumes the same out-of-band `$ApprovalLockSha256`, strictly revalidates the immutable approval lock and the physical/raw plan/spec blobs, then strictly parses `.superpowers/sdd/terminal-collapse-ending/legacy/task1-completion.json` and re-hashes every sealed artifact before trusting the mother or helper. Never infer completion from Markdown. Never open the read-only mother directly. Create one repository-external unique empty `SaveDir` for each frontal/flanking replay, assert each replay worktree's `game/saves` is absent or a task-owned empty directory, copy the mother under its engine filename, and verify mother/source/two-copy SHA-256 equality. Bind the exact ignored helpers under `.superpowers/sdd/terminal-collapse-ending/helpers/` to the 82,334 / 24,229 / 53,188 byte payloads and SHA-256 values `E0393DB1E113FDB8C35097978AA73B7D33AFDD5788499002B6423D883DEED4E8`, `73A3F9C43CF994E08F004E0A1266122A3EC5E0EAF065C63E6D9439CF0B0E1880`, and `20198B669F70E51E51F71BD01E6D06D1949D300F43CE9A94FB0190A47D781A15`. Launch each replay through one fresh dedicated helper host with process-local `SDL_VIDEODRIVER=dummy`, `SDL_AUDIODRIVER=dummy`, and `RENPY_RENDERER=sw`; require parent actual-host-exit/result mapping validation, then `Assert-PrivateDesktopSafetyEnvelope`, then explicitly require `Test-PrivateDesktopIntegralValue(result.root_exit_code)`, non-null root exit equal to the declared expected code, `COMPLETED`, helper-0, zero-window, and no-timeout. Capture stdout/stderr, schema-v2 Job/window diagnostics, provenance marker, and state assertions without treating PID/count diagnostics as coverage. Every other Phase B helper call with an expected target exit uses the same integral/non-null-before-compare gate. Each engine-native testcase must load its own copy, select exactly its named real choice, and prove `fall` occurs before any victory text or branch mutation. Missing/truncated/mismatched evidence, catastrophic host termination, any visible window, confirmation or interaction requirement, unknown token or label, fixture/marker mismatch, null/non-integral root exit, approval-lock drift, or sealed-artifact drift is `NEEDS_CONTEXT`; preserve the create-new attempt and never retry, use Computer Use, send real input, take screenshots, or use manual fallback.
- Final tests exactly once on the final tracked SHA: focused suites, `python -B -m unittest discover -s Tools -v`, portrait/narration/show/canon/AI-smell/release/font checks, `test_terminal_collapse_ending`, Full, Lint, process cleanup, diff scope, and independent Spec/Standards review.
- Final asset report: no new art/music/SFX/animation/UI; reuse existing `castle_exterior`, `battlefield`, black scene, and `war_drums.ogg`; measure actual font/package delta after approved text enters.

Phase B must end with the last tracked implementation commit before Final and independent reviews; no tracked evidence commit may follow those gates.

---

## Appendix A — `PrivateDesktopRunner.cs`

Exact committed helper payload: **82,334 bytes**; **SHA-256 `E0393DB1E113FDB8C35097978AA73B7D33AFDD5788499002B6423D883DEED4E8`**. The fenced body below is the complete UTF-8, no-BOM source and includes its final LF.

```csharp
using System;
using System.Collections;
using System.Collections.Generic;
using System.ComponentModel;
using System.Diagnostics;
using System.IO;
using System.Runtime.InteropServices;
using System.Runtime.Serialization;
using System.Runtime.Serialization.Json;
using System.Text;
using System.Threading;

namespace CourtOfShadows.Headless
{
    [DataContract]
    public sealed class EnvironmentEntry
    {
        [DataMember(Name = "name", Order = 1, IsRequired = true)]
        public string Name;

        [DataMember(Name = "value", Order = 2, EmitDefaultValue = true)]
        public string Value;
    }

    [DataContract]
    public sealed class RunRequest
    {
        [DataMember(Name = "schema_version", Order = 1, IsRequired = true)]
        public int SchemaVersion;

        [DataMember(Name = "executable", Order = 2, IsRequired = true)]
        public string Executable;

        [DataMember(Name = "arguments", Order = 3, IsRequired = true)]
        public string[] Arguments;

        [DataMember(Name = "working_directory", Order = 4, IsRequired = true)]
        public string WorkingDirectory;

        [DataMember(Name = "environment_overrides", Order = 5, IsRequired = true)]
        public EnvironmentEntry[] EnvironmentOverrides;

        [DataMember(Name = "timeout_milliseconds", Order = 6, IsRequired = true)]
        public int TimeoutMilliseconds;

        [DataMember(Name = "stdout_path", Order = 7, IsRequired = true)]
        public string StdoutPath;

        [DataMember(Name = "stderr_path", Order = 8, IsRequired = true)]
        public string StderrPath;

        [DataMember(Name = "result_path", Order = 9, IsRequired = true)]
        public string ResultPath;
    }

    [DataContract]
    public sealed class WindowEvidence
    {
        [DataMember(Name = "pid", Order = 1)]
        public int Pid;

        [DataMember(Name = "hwnd", Order = 2)]
        public string Hwnd;

        [DataMember(Name = "event", Order = 3)]
        public string Event;

        [DataMember(Name = "title", Order = 4)]
        public string Title;

        [DataMember(Name = "class_name", Order = 5)]
        public string ClassName;

        [DataMember(Name = "desktop", Order = 6)]
        public string Desktop;

        [DataMember(Name = "observed_utc", Order = 7)]
        public string ObservedUtc;
    }

    [DataContract]
    public sealed class RunResult
    {
        [DataMember(Name = "schema_version", Order = 1)]
        public int SchemaVersion;

        [DataMember(Name = "classification", Order = 2)]
        public string Classification;

        [DataMember(Name = "detail", Order = 3)]
        public string Detail;

        [DataMember(Name = "started", Order = 4)]
        public bool Started;

        [DataMember(Name = "root_pid", Order = 5, EmitDefaultValue = true)]
        public int? RootPid;

        [DataMember(Name = "root_exit_code", Order = 6, EmitDefaultValue = true)]
        public int? RootExitCode;

        [DataMember(Name = "timed_out", Order = 7)]
        public bool TimedOut;

        [DataMember(Name = "job_drained", Order = 8)]
        public bool JobDrained;

        [DataMember(Name = "desktop_name", Order = 9)]
        public string DesktopName;

        [DataMember(Name = "process_ids", Order = 10)]
        public int[] ProcessIds;

        [DataMember(Name = "new_process_ids", Order = 11)]
        public int[] NewProcessIds;

        [DataMember(Name = "active_snapshot_process_ids", Order = 12)]
        public int[] ActiveSnapshotProcessIds;

        [DataMember(Name = "job_total_processes", Order = 13, EmitDefaultValue = true)]
        public int? JobTotalProcesses;

        [DataMember(Name = "observed_distinct_process_id_count", Order = 14)]
        public int ObservedDistinctProcessIdCount;

        [DataMember(Name = "process_id_accounting_kind", Order = 15)]
        public string ProcessIdAccountingKind;

        [DataMember(Name = "process_diagnostic_errors", Order = 34)]
        public string[] ProcessDiagnosticErrors;

        [DataMember(Name = "host_termination_required", Order = 35)]
        public bool HostTerminationRequired;

        [DataMember(Name = "helper_exit_code", Order = 36)]
        public int HelperExitCode;

        [DataMember(Name = "job_kill_on_close_verified", Order = 37)]
        public bool JobKillOnCloseVerified;

        [DataMember(Name = "job_handle_non_inheritable", Order = 38)]
        public bool JobHandleNonInheritable;

        [DataMember(Name = "private_desktop_initially_empty", Order = 16)]
        public bool PrivateDesktopInitiallyEmpty;

        [DataMember(Name = "monitor_armed_before_create", Order = 17)]
        public bool MonitorArmedBeforeCreate;

        [DataMember(Name = "monitor_armed_before_resume", Order = 18)]
        public bool MonitorArmedBeforeResume;

        [DataMember(Name = "monitor_armed_utc", Order = 19, EmitDefaultValue = true)]
        public string MonitorArmedUtc;

        [DataMember(Name = "process_created_utc", Order = 20, EmitDefaultValue = true)]
        public string ProcessCreatedUtc;

        [DataMember(Name = "resumed_utc", Order = 21, EmitDefaultValue = true)]
        public string ResumedUtc;

        [DataMember(Name = "root_assigned_to_job_before_resume", Order = 22)]
        public bool RootAssignedToJobBeforeResume;

        [DataMember(Name = "job_breakaway_forbidden", Order = 23)]
        public bool JobBreakawayForbidden;

        [DataMember(Name = "job_active_processes_final", Order = 24, EmitDefaultValue = true)]
        public int? JobActiveProcessesFinal;

        [DataMember(Name = "monitor_completed_after_job_drain", Order = 25)]
        public bool MonitorCompletedAfterJobDrain;

        [DataMember(Name = "cleanup_complete", Order = 26)]
        public bool CleanupComplete;

        [DataMember(Name = "cleanup_errors", Order = 27)]
        public string[] CleanupErrors;

        [DataMember(Name = "visible_windows", Order = 28)]
        public WindowEvidence[] VisibleWindows;

        [DataMember(Name = "started_utc", Order = 29)]
        public string StartedUtc;

        [DataMember(Name = "finished_utc", Order = 30)]
        public string FinishedUtc;

        [DataMember(Name = "elapsed_milliseconds", Order = 31)]
        public long ElapsedMilliseconds;

        [DataMember(Name = "stdout_path", Order = 32)]
        public string StdoutPath;

        [DataMember(Name = "stderr_path", Order = 33)]
        public string StderrPath;
    }

    public static class PrivateDesktopRunner
    {
        private const uint CREATE_SUSPENDED = 0x00000004;
        private const uint CREATE_UNICODE_ENVIRONMENT = 0x00000400;
        private const uint CREATE_NEW_PROCESS_GROUP = 0x00000200;
        private const uint CREATE_NO_WINDOW = 0x08000000;
        private const uint EXTENDED_STARTUPINFO_PRESENT = 0x00080000;
        private const uint STARTF_USESTDHANDLES = 0x00000100;
        private const uint PROC_THREAD_ATTRIBUTE_HANDLE_LIST = 0x00020002;
        private const uint PROC_THREAD_ATTRIBUTE_JOB_LIST = 0x0002000D;
        private const uint JOB_OBJECT_LIMIT_BREAKAWAY_OK = 0x00000800;
        private const uint JOB_OBJECT_LIMIT_SILENT_BREAKAWAY_OK = 0x00001000;
        private const uint JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE = 0x00002000;
        private const uint JobObjectBasicAccountingInformation = 1;
        private const uint JobObjectAssociateCompletionPortInformation = 7;
        private const uint JobObjectExtendedLimitInformation = 9;
        private const uint JobObjectBasicProcessIdList = 3;
        private const uint JOB_OBJECT_MSG_NEW_PROCESS = 6;
        private const uint JOB_OBJECT_MSG_EXIT_PROCESS = 7;
        private const uint JOB_OBJECT_MSG_ABNORMAL_EXIT_PROCESS = 8;
        private const uint JOB_OBJECT_MSG_ACTIVE_PROCESS_ZERO = 4;
        private const uint WAIT_OBJECT_0 = 0;
        private const uint WAIT_TIMEOUT = 258;
        private const uint STILL_ACTIVE = 259;
        private const uint GENERIC_READ = 0x80000000;
        private const uint GENERIC_WRITE = 0x40000000;
        private const uint FILE_SHARE_READ = 0x00000001;
        private const uint FILE_SHARE_WRITE = 0x00000002;
        private const uint CREATE_NEW = 1;
        private const uint OPEN_EXISTING = 3;
        private const uint FILE_ATTRIBUTE_NORMAL = 0x00000080;
        private const uint DESKTOP_READOBJECTS = 0x0001;
        private const uint DESKTOP_CREATEWINDOW = 0x0002;
        private const uint DESKTOP_CREATEMENU = 0x0004;
        private const uint DESKTOP_ENUMERATE = 0x0040;
        private const uint DESKTOP_WRITEOBJECTS = 0x0080;
        private const uint EVENT_OBJECT_CREATE = 0x8000;
        private const uint EVENT_OBJECT_SHOW = 0x8002;
        private const uint WINEVENT_OUTOFCONTEXT = 0x0000;
        private const int OBJID_WINDOW = 0;
        private const int CHILDID_SELF = 0;
        private const uint GA_ROOT = 2;
        private const uint PM_NOREMOVE = 0x0000;
        private const uint PM_REMOVE = 0x0001;
        private const uint HANDLE_FLAG_INHERIT = 0x00000001;
        private const int MAX_PROCESS_DIAGNOSTIC_ERRORS = 8;
        private const int MAX_PROCESS_DIAGNOSTIC_ERROR_CHARACTERS = 2048;
        private static readonly IntPtr INVALID_HANDLE_VALUE = new IntPtr(-1);

        private static readonly object ObservationLock = new object();
        private static readonly HashSet<int> EverOwnedPids = new HashSet<int>();
        private static readonly HashSet<int> NewProcessPids = new HashSet<int>();
        private static readonly HashSet<int> ActiveSnapshotPids = new HashSet<int>();

        public static int RunRequestFile(string requestPath)
        {
            RunRequest request = null;
            RunResult result = null;
            string resultPath = null;
            try
            {
                request = ReadRequest(requestPath);
                resultPath = request.ResultPath;
                ValidateRequest(request, requestPath);
                result = Execute(request);
            }
            catch (Exception ex)
            {
                result = FailureResult(request, ex);
                if (resultPath == null && request != null)
                    resultPath = request.ResultPath;
            }

            if (String.IsNullOrEmpty(resultPath))
                throw new InvalidOperationException("No usable result_path was available; " + result.Detail);

            int helperExitCode = MapResultExitCode(result);
            result.HelperExitCode = helperExitCode;
            if (result.HostTerminationRequired)
            {
                PersistResultAndTerminateHost(resultPath, result, helperExitCode);
                throw new InvalidOperationException("Environment.Exit returned after catastrophic helper termination.");
            }

            WriteJsonCreateNew(resultPath, result);
            return helperExitCode;
        }

        private static void PersistResultAndTerminateHost(string resultPath, RunResult result, int helperExitCode)
        {
            try
            {
                WriteJsonCreateNew(resultPath, result);
            }
            finally
            {
                Environment.Exit(helperExitCode);
            }
        }

        private static int MapResultExitCode(RunResult result)
        {
            if (String.Equals(result.Classification, "COMPLETED", StringComparison.Ordinal)) return 0;
            if (String.Equals(result.Classification, "NEEDS_CONTEXT", StringComparison.Ordinal)) return 20;
            if (String.Equals(result.Classification, "TIMEOUT", StringComparison.Ordinal)) return 21;
            if (String.Equals(result.Classification, "LAUNCH_ERROR", StringComparison.Ordinal)) return 22;
            throw new InvalidOperationException("Unknown helper classification: " + result.Classification);
        }

        public static string QuoteWindowsArgument(string value)
        {
            if (value == null) throw new ArgumentNullException("value");
            if (value.Length == 0) return "\"\"";
            bool needsQuotes = false;
            for (int i = 0; i < value.Length; i++)
            {
                char c = value[i];
                if (Char.IsWhiteSpace(c) || c == '"') { needsQuotes = true; break; }
            }
            if (!needsQuotes) return value;

            StringBuilder output = new StringBuilder(value.Length + 2);
            output.Append('"');
            int slashCount = 0;
            for (int i = 0; i < value.Length; i++)
            {
                char c = value[i];
                if (c == '\\')
                {
                    slashCount++;
                    continue;
                }
                if (c == '"')
                {
                    output.Append('\\', slashCount * 2 + 1);
                    output.Append('"');
                    slashCount = 0;
                    continue;
                }
                output.Append('\\', slashCount);
                slashCount = 0;
                output.Append(c);
            }
            output.Append('\\', slashCount * 2);
            output.Append('"');
            return output.ToString();
        }

        private static RunResult Execute(RunRequest request)
        {
            ResetObservationState();
            DateTime startedUtc = DateTime.UtcNow;
            Stopwatch stopwatch = Stopwatch.StartNew();
            RunResult result = NewBaseResult(request, startedUtc);
            IntPtr desktop = IntPtr.Zero;
            IntPtr job = IntPtr.Zero;
            IntPtr completionPort = IntPtr.Zero;
            IntPtr stdoutHandle = INVALID_HANDLE_VALUE;
            IntPtr stderrHandle = INVALID_HANDLE_VALUE;
            IntPtr stdinHandle = INVALID_HANDLE_VALUE;
            IntPtr attributeList = IntPtr.Zero;
            IntPtr handleListMemory = IntPtr.Zero;
            IntPtr jobListMemory = IntPtr.Zero;
            IntPtr environmentMemory = IntPtr.Zero;
            PROCESS_INFORMATION processInfo = new PROCESS_INFORMATION();
            bool processCreated = false;
            bool rootExitProven = false;
            bool rootJobMembershipProven = false;
            bool jobTerminated = false;
            bool attributeListInitialized = false;
            List<string> cleanupErrors = new List<string>();
            List<string> processDiagnosticErrors = new List<string>();
            PrivateDesktopWatcher watcher = null;

            try
            {
                string desktopName = "CosHeadless_" + Guid.NewGuid().ToString("N");
                uint desktopAccess = DESKTOP_READOBJECTS | DESKTOP_CREATEWINDOW | DESKTOP_CREATEMENU |
                                     DESKTOP_ENUMERATE | DESKTOP_WRITEOBJECTS;
                desktop = CreateDesktopW(desktopName, null, IntPtr.Zero, 0, desktopAccess, IntPtr.Zero);
                if (desktop == IntPtr.Zero) ThrowLastWin32("CreateDesktopW");
                result.DesktopName = "WinSta0\\" + desktopName;

                job = CreateJobObjectW(IntPtr.Zero, null);
                if (job == IntPtr.Zero) ThrowLastWin32("CreateJobObjectW");
                ConfigureKillOnClose(job);
                VerifyKillOnCloseAndNoBreakaway(job);
                result.JobKillOnCloseVerified = true;
                result.JobBreakawayForbidden = true;
                result.JobHandleNonInheritable = VerifyHandleNonInheritable(job);

                completionPort = CreateIoCompletionPort(INVALID_HANDLE_VALUE, IntPtr.Zero, UIntPtr.Zero, 1);
                if (completionPort == IntPtr.Zero) ThrowLastWin32("CreateIoCompletionPort");
                AssociateJobCompletionPort(job, completionPort);

                watcher = new PrivateDesktopWatcher(desktop, desktopName);
                watcher.StartAndWaitUntilArmed(5000);
                result.PrivateDesktopInitiallyEmpty = watcher.InitiallyEmpty;
                result.MonitorArmedUtc = FormatUtc(watcher.ArmedUtc);

                SECURITY_ATTRIBUTES inheritable = new SECURITY_ATTRIBUTES();
                inheritable.nLength = Marshal.SizeOf(typeof(SECURITY_ATTRIBUTES));
                inheritable.bInheritHandle = true;
                stdoutHandle = CreateFileW(request.StdoutPath, GENERIC_WRITE, FILE_SHARE_READ,
                    ref inheritable, CREATE_NEW, FILE_ATTRIBUTE_NORMAL, IntPtr.Zero);
                if (stdoutHandle == INVALID_HANDLE_VALUE) ThrowLastWin32("CreateFileW(stdout, CREATE_NEW)");
                stderrHandle = CreateFileW(request.StderrPath, GENERIC_WRITE, FILE_SHARE_READ,
                    ref inheritable, CREATE_NEW, FILE_ATTRIBUTE_NORMAL, IntPtr.Zero);
                if (stderrHandle == INVALID_HANDLE_VALUE) ThrowLastWin32("CreateFileW(stderr, CREATE_NEW)");
                stdinHandle = CreateFileW("NUL", GENERIC_READ, FILE_SHARE_READ | FILE_SHARE_WRITE,
                    ref inheritable, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, IntPtr.Zero);
                if (stdinHandle == INVALID_HANDLE_VALUE) ThrowLastWin32("CreateFileW(NUL)");

                STARTUPINFOEX startup = new STARTUPINFOEX();
                startup.StartupInfo.cb = Marshal.SizeOf(typeof(STARTUPINFOEX));
                startup.StartupInfo.lpDesktop = result.DesktopName;
                startup.StartupInfo.dwFlags = STARTF_USESTDHANDLES;
                startup.StartupInfo.hStdInput = stdinHandle;
                startup.StartupInfo.hStdOutput = stdoutHandle;
                startup.StartupInfo.hStdError = stderrHandle;

                UIntPtr attributeBytes = UIntPtr.Zero;
                InitializeProcThreadAttributeList(IntPtr.Zero, 2, 0, ref attributeBytes);
                int initError = Marshal.GetLastWin32Error();
                if (attributeBytes == UIntPtr.Zero || initError != 122)
                    throw new Win32Exception(initError, "InitializeProcThreadAttributeList(size) failed");
                attributeList = Marshal.AllocHGlobal(CheckedUIntPtrToInt(attributeBytes));
                if (!InitializeProcThreadAttributeList(attributeList, 2, 0, ref attributeBytes))
                    ThrowLastWin32("InitializeProcThreadAttributeList");
                attributeListInitialized = true;
                startup.lpAttributeList = attributeList;

                IntPtr[] inheritedHandles = new IntPtr[] { stdinHandle, stdoutHandle, stderrHandle };
                handleListMemory = Marshal.AllocHGlobal(IntPtr.Size * inheritedHandles.Length);
                Marshal.Copy(inheritedHandles, 0, handleListMemory, inheritedHandles.Length);
                if (!UpdateProcThreadAttribute(attributeList, 0, new UIntPtr(PROC_THREAD_ATTRIBUTE_HANDLE_LIST),
                    handleListMemory, new UIntPtr((uint)(IntPtr.Size * inheritedHandles.Length)),
                    IntPtr.Zero, IntPtr.Zero))
                    ThrowLastWin32("UpdateProcThreadAttribute(HANDLE_LIST)");

                jobListMemory = Marshal.AllocHGlobal(IntPtr.Size);
                Marshal.WriteIntPtr(jobListMemory, job);
                if (!UpdateProcThreadAttribute(attributeList, 0, new UIntPtr(PROC_THREAD_ATTRIBUTE_JOB_LIST),
                    jobListMemory, new UIntPtr((uint)IntPtr.Size), IntPtr.Zero, IntPtr.Zero))
                    ThrowLastWin32("UpdateProcThreadAttribute(JOB_LIST)");

                environmentMemory = BuildUnicodeEnvironmentBlock(request.EnvironmentOverrides);
                StringBuilder commandLine = BuildCommandLine(request.Executable, request.Arguments);
                uint creationFlags = CREATE_SUSPENDED | CREATE_UNICODE_ENVIRONMENT |
                                     CREATE_NEW_PROCESS_GROUP | CREATE_NO_WINDOW | EXTENDED_STARTUPINFO_PRESENT;
                if (!CreateProcessW(request.Executable, commandLine, IntPtr.Zero, IntPtr.Zero, true,
                    creationFlags, environmentMemory, request.WorkingDirectory, ref startup, out processInfo))
                    ThrowLastWin32("CreateProcessW");
                DateTime processCreatedUtc = DateTime.UtcNow;
                processCreated = true;
                result.Started = true;
                result.RootPid = unchecked((int)processInfo.dwProcessId);
                result.ProcessCreatedUtc = FormatUtc(processCreatedUtc);
                result.MonitorArmedBeforeCreate = watcher.ArmedUtc <= processCreatedUtc;

                bool rootInJob;
                if (!IsProcessInJob(processInfo.hProcess, job, out rootInJob))
                    ThrowLastWin32("IsProcessInJob(root before ResumeThread)");
                if (!rootInJob)
                    throw new InvalidOperationException("PROC_THREAD_ATTRIBUTE_JOB_LIST did not place the suspended root in the private Job.");
                rootJobMembershipProven = true;
                result.RootAssignedToJobBeforeResume = true;
                AddOwnedPid(unchecked((int)processInfo.dwProcessId));
                TryPumpJobMessages(completionPort, processDiagnosticErrors);
                TryRefreshOwnedPidsFromJob(job, processDiagnosticErrors);
                watcher.ThrowIfFailed();
                watcher.Reconcile();
                if (watcher.HasAcceptedWindows)
                    throw new InvalidOperationException("A visible top-level window existed on the private desktop before resume.");

                uint resumeResult = ResumeThread(processInfo.hThread);
                if (resumeResult == UInt32.MaxValue) ThrowLastWin32("ResumeThread");
                DateTime resumedUtc = DateTime.UtcNow;
                result.ResumedUtc = FormatUtc(resumedUtc);
                result.MonitorArmedBeforeResume = watcher.ArmedUtc <= resumedUtc;

                bool activeZero = false;
                while (true)
                {
                    watcher.ThrowIfFailed();
                    TryPumpJobMessages(completionPort, processDiagnosticErrors);
                    TryRefreshOwnedPidsFromJob(job, processDiagnosticErrors);
                    watcher.Reconcile();

                    if (watcher.HasAcceptedWindows)
                    {
                        result.Classification = "NEEDS_CONTEXT";
                        result.Detail = "A visible top-level window was observed on the private desktop; desktop interaction is forbidden.";
                        TerminateJobOrThrow(job, 0xEC000001, "TerminateJobObject(visible window)");
                        jobTerminated = true;
                        break;
                    }

                    uint rootWait = WaitForSingleObject(processInfo.hProcess, 0);
                    if (rootWait == WAIT_OBJECT_0) rootExitProven = true;
                    else if (rootWait != WAIT_TIMEOUT) ThrowLastWin32("WaitForSingleObject(root)");

                    activeZero = QueryActiveProcessCount(job) == 0;
                    if (rootExitProven && activeZero)
                    {
                        result.Classification = "COMPLETED";
                        result.Detail = "The complete job process tree exited without a visible top-level window.";
                        result.JobDrained = true;
                        break;
                    }

                    if (stopwatch.ElapsedMilliseconds >= request.TimeoutMilliseconds)
                    {
                        result.Classification = "TIMEOUT";
                        result.Detail = "The complete job process tree did not drain before timeout.";
                        result.TimedOut = true;
                        TerminateJobOrThrow(job, 0xEC000002, "TerminateJobObject(timeout)");
                        jobTerminated = true;
                        break;
                    }
                    Thread.Sleep(10);
                }

                if (jobTerminated)
                    result.JobDrained = DrainTerminatedJob(job, completionPort, 5000, processDiagnosticErrors);

                if (result.JobDrained && !rootExitProven)
                {
                    uint drainedRootWait = WaitForSingleObject(processInfo.hProcess, 0);
                    if (drainedRootWait == WAIT_OBJECT_0) rootExitProven = true;
                    else if (drainedRootWait != WAIT_TIMEOUT) ThrowLastWin32("WaitForSingleObject(root after Job drain)");
                }
                TryCaptureRootExitCode(result, processInfo.hProcess, rootExitProven);

                watcher.ThrowIfFailed();
                TryPumpJobMessages(completionPort, processDiagnosticErrors);
                TryRefreshOwnedPidsFromJob(job, processDiagnosticErrors);
                watcher.Reconcile();
                if (watcher.HasAcceptedWindows && !String.Equals(result.Classification, "NEEDS_CONTEXT", StringComparison.Ordinal))
                {
                    result.Classification = "NEEDS_CONTEXT";
                    result.Detail = "A visible top-level window was observed on the private desktop during final reconciliation.";
                    if (!jobTerminated)
                    {
                        TerminateJobOrThrow(job, 0xEC000003, "TerminateJobObject(final window)");
                        jobTerminated = true;
                    }
                    result.JobDrained = DrainTerminatedJob(job, completionPort, 5000, processDiagnosticErrors);
                }
            }
            catch (Exception ex)
            {
                result.Classification = "LAUNCH_ERROR";
                result.Detail = ex.GetType().FullName + ": " + ex.Message;
                if (processCreated && processInfo.hProcess != IntPtr.Zero)
                    TryCaptureRootExitCode(result, processInfo.hProcess, rootExitProven);
            }
            finally
            {
                if (job != IntPtr.Zero)
                {
                    try
                    {
                        TryPumpJobMessages(completionPort, processDiagnosticErrors);
                        TryRefreshOwnedPidsFromJob(job, processDiagnosticErrors);
                        if (QueryActiveProcessCount(job) != 0)
                        {
                            if (!TerminateJobObject(job, 0xEC000006))
                                throw new Win32Exception(Marshal.GetLastWin32Error(), "TerminateJobObject(final cleanup) failed");
                            jobTerminated = true;
                            result.JobDrained = DrainTerminatedJob(job, completionPort, 5000, processDiagnosticErrors);
                        }
                        else
                        {
                            result.JobDrained = true;
                        }
                        uint finalActiveProcesses = QueryActiveProcessCount(job);
                        result.JobActiveProcessesFinal = checked((int)finalActiveProcesses);
                        if (!result.JobDrained || finalActiveProcesses != 0)
                            throw new InvalidOperationException("Job process tree did not drain during final cleanup.");
                        TryPumpJobMessages(completionPort, processDiagnosticErrors);
                        TryRefreshOwnedPidsFromJob(job, processDiagnosticErrors);
                        TryFinalizeProcessAccounting(result, job, processDiagnosticErrors);
                    }
                    catch (Exception jobCleanupError)
                    {
                        cleanupErrors.Add("job drain: " + jobCleanupError.GetType().FullName + ": " + jobCleanupError.Message);
                        if (rootJobMembershipProven &&
                            (!result.JobDrained || !result.JobActiveProcessesFinal.HasValue || result.JobActiveProcessesFinal.Value != 0))
                        {
                            try
                            {
                                if (!jobTerminated)
                                {
                                    TerminateJobOrThrow(job, 0xEC000007, "TerminateJobObject(recovery cleanup)");
                                    jobTerminated = true;
                                }
                                result.JobDrained = DrainTerminatedJob(job, completionPort, 5000, processDiagnosticErrors);
                                uint recoveredActiveProcesses = QueryActiveProcessCount(job);
                                result.JobActiveProcessesFinal = checked((int)recoveredActiveProcesses);
                                if (!result.JobDrained || recoveredActiveProcesses != 0)
                                    throw new InvalidOperationException("Job process tree did not drain during recovery cleanup.");
                                TryPumpJobMessages(completionPort, processDiagnosticErrors);
                                TryRefreshOwnedPidsFromJob(job, processDiagnosticErrors);
                                TryFinalizeProcessAccounting(result, job, processDiagnosticErrors);
                            }
                            catch (Exception recoveryError)
                            {
                                cleanupErrors.Add("job recovery drain: " + recoveryError.GetType().FullName + ": " + recoveryError.Message);
                            }
                        }
                    }
                }

                bool drainProven = result.JobDrained && result.JobActiveProcessesFinal.HasValue &&
                    result.JobActiveProcessesFinal.Value == 0;
                if (processCreated && processInfo.hProcess != IntPtr.Zero && drainProven && !rootExitProven)
                {
                    try
                    {
                        uint cleanupRootWait = WaitForSingleObject(processInfo.hProcess, 0);
                        if (cleanupRootWait == WAIT_OBJECT_0) rootExitProven = true;
                        else if (cleanupRootWait != WAIT_TIMEOUT) ThrowLastWin32("WaitForSingleObject(root after final Job drain)");
                    }
                    catch (Exception rootSignalError)
                    {
                        cleanupErrors.Add("root exit signal after Job drain: " + rootSignalError.GetType().FullName + ": " + rootSignalError.Message);
                    }
                }
                if (job != IntPtr.Zero && !drainProven)
                {
                    cleanupErrors.Add("final Job ActiveProcesses=0 was not proven after all termination/drain attempts");
                    result.HostTerminationRequired = true;
                }

                bool watcherJoinSucceeded = false;
                bool watcherCompletionSucceeded = false;
                if (watcher != null && drainProven)
                {
                    try
                    {
                        watcher.StopAndJoin(5000);
                        watcherJoinSucceeded = true;
                    }
                    catch (Exception watcherError)
                    {
                        cleanupErrors.Add("watcher stop/unhook/join: " + watcherError.GetType().FullName + ": " + watcherError.Message);
                        result.HostTerminationRequired = true;
                    }

                    if (watcherJoinSucceeded)
                    {
                        try
                        {
                            watcher.ThrowIfFailed();
                            watcherCompletionSucceeded = true;
                        }
                        catch (Exception watcherCompletionError)
                        {
                            cleanupErrors.Add("watcher completion: " + watcherCompletionError.GetType().FullName + ": " + watcherCompletionError.Message);
                        }
                    }
                }

                if (watcher != null)
                {
                    try
                    {
                        watcher.Reconcile();
                        if (watcher.HasAcceptedWindows)
                        {
                            string priorClassification = result.Classification;
                            string priorDetail = result.Detail;
                            result.Classification = "NEEDS_CONTEXT";
                            result.Detail = "A visible top-level window was observed on the private desktop before watcher shutdown." +
                                " Previous classification=" + priorClassification + "; previous detail=" + priorDetail;
                        }
                    }
                    catch (Exception reconciliationError)
                    {
                        cleanupErrors.Add("watcher final reconciliation: " + reconciliationError.GetType().FullName + ": " + reconciliationError.Message);
                    }

                    if (drainProven && watcherJoinSucceeded && watcherCompletionSucceeded)
                        result.MonitorCompletedAfterJobDrain = true;

                    if (watcherJoinSucceeded)
                    {
                        try
                        {
                            watcher.DisposeEventsAfterJoin();
                        }
                        catch (Exception disposeError)
                        {
                            cleanupErrors.Add("watcher event disposal: " + disposeError.GetType().FullName + ": " + disposeError.Message);
                        }
                    }
                }

                PopulateObservationResult(result, watcher);
                result.ProcessDiagnosticErrors = processDiagnosticErrors.ToArray();
                if (processCreated && processInfo.hProcess != IntPtr.Zero && !result.RootExitCode.HasValue)
                    TryCaptureRootExitCode(result, processInfo.hProcess, rootExitProven);

                if (!result.HostTerminationRequired)
                {
                    processInfo.hThread = CloseKernelHandleForCleanup(processInfo.hThread, "root thread", cleanupErrors);
                    processInfo.hProcess = CloseKernelHandleForCleanup(processInfo.hProcess, "root process", cleanupErrors);
                    stdinHandle = CloseKernelHandleForCleanup(stdinHandle, "stdin NUL", cleanupErrors);
                    stdoutHandle = CloseKernelHandleForCleanup(stdoutHandle, "stdout", cleanupErrors);
                    stderrHandle = CloseKernelHandleForCleanup(stderrHandle, "stderr", cleanupErrors);

                    if (attributeList != IntPtr.Zero)
                    {
                        if (attributeListInitialized) DeleteProcThreadAttributeList(attributeList);
                        Marshal.FreeHGlobal(attributeList);
                        attributeList = IntPtr.Zero;
                    }
                    if (handleListMemory != IntPtr.Zero) { Marshal.FreeHGlobal(handleListMemory); handleListMemory = IntPtr.Zero; }
                    if (jobListMemory != IntPtr.Zero) { Marshal.FreeHGlobal(jobListMemory); jobListMemory = IntPtr.Zero; }
                    if (environmentMemory != IntPtr.Zero) { Marshal.FreeHGlobal(environmentMemory); environmentMemory = IntPtr.Zero; }

                    job = CloseKernelHandleForCleanup(job, "job", cleanupErrors);
                    completionPort = CloseKernelHandleForCleanup(completionPort, "completion port", cleanupErrors);
                    if (desktop != IntPtr.Zero)
                    {
                        if (!CloseDesktop(desktop))
                            cleanupErrors.Add("CloseDesktop: " + new Win32Exception(Marshal.GetLastWin32Error()).Message);
                        desktop = IntPtr.Zero;
                    }
                }

                if ((String.Equals(result.Classification, "COMPLETED", StringComparison.Ordinal) ||
                     String.Equals(result.Classification, "NEEDS_CONTEXT", StringComparison.Ordinal) ||
                     String.Equals(result.Classification, "TIMEOUT", StringComparison.Ordinal)) &&
                    (!result.PrivateDesktopInitiallyEmpty || !result.MonitorArmedBeforeCreate ||
                     !result.MonitorArmedBeforeResume || !result.RootAssignedToJobBeforeResume ||
                     !result.JobKillOnCloseVerified || !result.JobBreakawayForbidden ||
                     !result.JobHandleNonInheritable || !result.JobDrained ||
                     !result.JobActiveProcessesFinal.HasValue || result.JobActiveProcessesFinal.Value != 0 ||
                     !result.MonitorCompletedAfterJobDrain))
                {
                    cleanupErrors.Add("one or more private-desktop infrastructure safety gates were not proven");
                }

                result.CleanupErrors = cleanupErrors.ToArray();
                result.CleanupComplete = cleanupErrors.Count == 0;
                bool visibleWindowObserved = result.VisibleWindows != null && result.VisibleWindows.Length != 0;
                if (visibleWindowObserved)
                {
                    string priorClassification = result.Classification;
                    string priorDetail = result.Detail;
                    result.Classification = "NEEDS_CONTEXT";
                    result.Detail = "A visible top-level window was observed on the private desktop.";
                    if (!result.CleanupComplete)
                        result.Detail += " Cleanup also failed: " + String.Join(" | ", cleanupErrors.ToArray()) + ".";
                    result.Detail += " Previous classification=" + priorClassification + "; previous detail=" + priorDetail;
                }
                else if (!result.CleanupComplete)
                {
                    string priorClassification = result.Classification;
                    string priorDetail = result.Detail;
                    result.Classification = "LAUNCH_ERROR";
                    result.Detail = "Cleanup failed: " + String.Join(" | ", cleanupErrors.ToArray()) +
                        ". Previous classification=" + priorClassification + "; previous detail=" + priorDetail;
                }

                if (result.HostTerminationRequired)
                {
                    string priorClassification = result.Classification;
                    string priorDetail = result.Detail;
                    result.MonitorCompletedAfterJobDrain = false;
                    result.CleanupComplete = false;
                    result.Classification = "NEEDS_CONTEXT";
                    result.Detail = "Catastrophic helper-host termination is required." +
                        " Previous classification=" + priorClassification + "; previous detail=" + priorDetail;
                }
            }

            stopwatch.Stop();
            result.FinishedUtc = FormatUtc(DateTime.UtcNow);
            result.ElapsedMilliseconds = stopwatch.ElapsedMilliseconds;
            return result;
        }

        private static void TryCaptureRootExitCode(RunResult result, IntPtr processHandle, bool rootExitProven)
        {
            uint exitCode;
            if (!GetExitCodeProcess(processHandle, out exitCode)) return;
            if (exitCode == STILL_ACTIVE && !rootExitProven) return;
            result.RootExitCode = unchecked((int)exitCode);
        }

        private static void ValidateRequest(RunRequest request, string requestPath)
        {
            if (request == null) throw new InvalidDataException("Request JSON was null.");
            if (request.SchemaVersion != 1) throw new InvalidDataException("schema_version must be exactly 1.");
            RequireAbsoluteExistingFile(request.Executable, "executable");
            RequireAbsoluteExistingDirectory(request.WorkingDirectory, "working_directory");
            RequireAbsoluteNewFile(request.StdoutPath, "stdout_path");
            RequireAbsoluteNewFile(request.StderrPath, "stderr_path");
            RequireAbsoluteNewFile(request.ResultPath, "result_path");
            if (request.Arguments == null) throw new InvalidDataException("arguments must be an array.");
            for (int i = 0; i < request.Arguments.Length; i++)
            {
                if (request.Arguments[i] == null) throw new InvalidDataException("arguments may not contain null.");
                RejectNul(request.Arguments[i], "arguments[" + i + "]");
            }
            if (request.EnvironmentOverrides == null) throw new InvalidDataException("environment_overrides must be an array.");
            HashSet<string> envNames = new HashSet<string>(StringComparer.OrdinalIgnoreCase);
            for (int i = 0; i < request.EnvironmentOverrides.Length; i++)
            {
                EnvironmentEntry entry = request.EnvironmentOverrides[i];
                if (entry == null || String.IsNullOrEmpty(entry.Name)) throw new InvalidDataException("environment override name is empty.");
                RejectNul(entry.Name, "environment override name");
                if (entry.Name.IndexOf('=') >= 0) throw new InvalidDataException("environment override names may not contain '='.");
                if (!envNames.Add(entry.Name)) throw new InvalidDataException("duplicate environment override: " + entry.Name);
                if (entry.Value != null) RejectNul(entry.Value, "environment override value");
            }
            if (request.TimeoutMilliseconds < 1 || request.TimeoutMilliseconds > 86400000)
                throw new InvalidDataException("timeout_milliseconds must be between 1 and 86400000.");
            RejectNul(request.Executable, "executable");
            RejectNul(request.WorkingDirectory, "working_directory");
            string[] paths = new string[] { requestPath, request.StdoutPath, request.StderrPath, request.ResultPath };
            for (int i = 0; i < paths.Length; i++)
                for (int j = i + 1; j < paths.Length; j++)
                    if (String.Equals(Path.GetFullPath(paths[i]), Path.GetFullPath(paths[j]), StringComparison.OrdinalIgnoreCase))
                        throw new InvalidDataException("request/stdout/stderr/result paths must be distinct.");
        }

        private static void RequireAbsoluteExistingFile(string path, string name)
        {
            if (String.IsNullOrWhiteSpace(path) || !Path.IsPathRooted(path)) throw new InvalidDataException(name + " must be absolute.");
            if (!File.Exists(path)) throw new FileNotFoundException(name + " does not exist.", path);
        }

        private static void RequireAbsoluteExistingDirectory(string path, string name)
        {
            if (String.IsNullOrWhiteSpace(path) || !Path.IsPathRooted(path)) throw new InvalidDataException(name + " must be absolute.");
            if (!Directory.Exists(path)) throw new DirectoryNotFoundException(name + " does not exist: " + path);
        }

        private static void RequireAbsoluteNewFile(string path, string name)
        {
            if (String.IsNullOrWhiteSpace(path) || !Path.IsPathRooted(path)) throw new InvalidDataException(name + " must be absolute.");
            string parent = Path.GetDirectoryName(Path.GetFullPath(path));
            if (!Directory.Exists(parent)) throw new DirectoryNotFoundException(name + " parent does not exist: " + parent);
            if (File.Exists(path) || Directory.Exists(path)) throw new IOException(name + " already exists; evidence is append-only: " + path);
        }

        private static void RejectNul(string value, string name)
        {
            if (value.IndexOf('\0') >= 0) throw new InvalidDataException(name + " contains NUL.");
        }

        private static RunRequest ReadRequest(string path)
        {
            RequireAbsoluteExistingFile(path, "request_path");
            DataContractJsonSerializer serializer = new DataContractJsonSerializer(typeof(RunRequest));
            using (FileStream stream = new FileStream(path, FileMode.Open, FileAccess.Read, FileShare.Read))
                return (RunRequest)serializer.ReadObject(stream);
        }

        private static void WriteJsonCreateNew(string path, object value)
        {
            string parent = Path.GetDirectoryName(Path.GetFullPath(path));
            if (!Directory.Exists(parent)) throw new DirectoryNotFoundException("result parent does not exist: " + parent);
            DataContractJsonSerializer serializer = new DataContractJsonSerializer(value.GetType());
            using (FileStream stream = new FileStream(path, FileMode.CreateNew, FileAccess.Write, FileShare.Read))
            {
                serializer.WriteObject(stream, value);
                stream.Flush(true);
            }
        }

        private static RunResult FailureResult(RunRequest request, Exception ex)
        {
            DateTime now = DateTime.UtcNow;
            return new RunResult {
                SchemaVersion = 2, Classification = "LAUNCH_ERROR",
                Detail = ex.GetType().FullName + ": " + ex.Message,
                Started = false, RootPid = null, RootExitCode = null,
                TimedOut = false, JobDrained = true, DesktopName = null,
                ProcessIds = new int[0], NewProcessIds = new int[0],
                ActiveSnapshotProcessIds = new int[0], JobTotalProcesses = null,
                ObservedDistinctProcessIdCount = 0, ProcessIdAccountingKind = "diagnostic_distinct_pid",
                ProcessDiagnosticErrors = new string[0],
                PrivateDesktopInitiallyEmpty = false, MonitorArmedBeforeCreate = false,
                MonitorArmedBeforeResume = false, MonitorArmedUtc = null,
                ProcessCreatedUtc = null, ResumedUtc = null,
                RootAssignedToJobBeforeResume = false, JobKillOnCloseVerified = false,
                JobBreakawayForbidden = false, JobHandleNonInheritable = false,
                JobActiveProcessesFinal = null, MonitorCompletedAfterJobDrain = false,
                HostTerminationRequired = false, HelperExitCode = 22,
                CleanupComplete = true,
                CleanupErrors = new string[0], VisibleWindows = new WindowEvidence[0],
                StartedUtc = FormatUtc(now), FinishedUtc = FormatUtc(now), ElapsedMilliseconds = 0,
                StdoutPath = request == null ? null : request.StdoutPath,
                StderrPath = request == null ? null : request.StderrPath
            };
        }

        private static RunResult NewBaseResult(RunRequest request, DateTime startedUtc)
        {
            return new RunResult {
                SchemaVersion = 2, Classification = "LAUNCH_ERROR", Detail = "Execution did not complete.",
                Started = false, RootPid = null, RootExitCode = null, TimedOut = false,
                JobDrained = false, DesktopName = null, ProcessIds = new int[0],
                NewProcessIds = new int[0], ActiveSnapshotProcessIds = new int[0],
                JobTotalProcesses = null, ObservedDistinctProcessIdCount = 0,
                ProcessIdAccountingKind = "diagnostic_distinct_pid",
                ProcessDiagnosticErrors = new string[0],
                PrivateDesktopInitiallyEmpty = false, MonitorArmedBeforeCreate = false,
                MonitorArmedBeforeResume = false, MonitorArmedUtc = null,
                ProcessCreatedUtc = null, ResumedUtc = null,
                RootAssignedToJobBeforeResume = false, JobKillOnCloseVerified = false,
                JobBreakawayForbidden = false, JobHandleNonInheritable = false,
                JobActiveProcessesFinal = null, MonitorCompletedAfterJobDrain = false,
                HostTerminationRequired = false, HelperExitCode = 22,
                CleanupComplete = false, CleanupErrors = new string[0],
                VisibleWindows = new WindowEvidence[0], StartedUtc = FormatUtc(startedUtc),
                FinishedUtc = null, ElapsedMilliseconds = 0,
                StdoutPath = request.StdoutPath, StderrPath = request.StderrPath
            };
        }

        private static string FormatUtc(DateTime value)
        {
            return value.ToUniversalTime().ToString("yyyy-MM-dd'T'HH:mm:ss.fff'Z'", System.Globalization.CultureInfo.InvariantCulture);
        }

        private static StringBuilder BuildCommandLine(string executable, string[] arguments)
        {
            StringBuilder line = new StringBuilder();
            line.Append(QuoteWindowsArgument(executable));
            for (int i = 0; i < arguments.Length; i++)
            {
                line.Append(' ');
                line.Append(QuoteWindowsArgument(arguments[i]));
            }
            return line;
        }

        private static IntPtr BuildUnicodeEnvironmentBlock(EnvironmentEntry[] overrides)
        {
            SortedDictionary<string, string> environment = new SortedDictionary<string, string>(StringComparer.OrdinalIgnoreCase);
            IDictionary inherited = Environment.GetEnvironmentVariables();
            foreach (DictionaryEntry pair in inherited)
                environment[(string)pair.Key] = (string)pair.Value;
            for (int i = 0; i < overrides.Length; i++)
            {
                EnvironmentEntry entry = overrides[i];
                if (entry.Value == null) environment.Remove(entry.Name);
                else environment[entry.Name] = entry.Value;
            }
            StringBuilder block = new StringBuilder();
            foreach (KeyValuePair<string, string> pair in environment)
            {
                block.Append(pair.Key);
                block.Append('=');
                block.Append(pair.Value);
                block.Append('\0');
            }
            block.Append('\0');
            char[] chars = block.ToString().ToCharArray();
            IntPtr memory = Marshal.AllocHGlobal(chars.Length * 2);
            Marshal.Copy(chars, 0, memory, chars.Length);
            return memory;
        }

        private static void ConfigureKillOnClose(IntPtr job)
        {
            JOBOBJECT_EXTENDED_LIMIT_INFORMATION info = new JOBOBJECT_EXTENDED_LIMIT_INFORMATION();
            info.BasicLimitInformation.LimitFlags = JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE;
            int size = Marshal.SizeOf(typeof(JOBOBJECT_EXTENDED_LIMIT_INFORMATION));
            IntPtr memory = Marshal.AllocHGlobal(size);
            try
            {
                Marshal.StructureToPtr(info, memory, false);
                if (!SetInformationJobObject(job, JobObjectExtendedLimitInformation, memory, (uint)size))
                    ThrowLastWin32("SetInformationJobObject(KILL_ON_JOB_CLOSE)");
            }
            finally { Marshal.FreeHGlobal(memory); }
        }

        private static void VerifyKillOnCloseAndNoBreakaway(IntPtr job)
        {
            int size = Marshal.SizeOf(typeof(JOBOBJECT_EXTENDED_LIMIT_INFORMATION));
            IntPtr memory = Marshal.AllocHGlobal(size);
            try
            {
                uint returned;
                if (!QueryInformationJobObject(job, JobObjectExtendedLimitInformation, memory, (uint)size, out returned))
                    ThrowLastWin32("QueryInformationJobObject(ExtendedLimitInformation)");
                JOBOBJECT_EXTENDED_LIMIT_INFORMATION info =
                    (JOBOBJECT_EXTENDED_LIMIT_INFORMATION)Marshal.PtrToStructure(
                        memory, typeof(JOBOBJECT_EXTENDED_LIMIT_INFORMATION));
                uint flags = info.BasicLimitInformation.LimitFlags;
                bool killOnClose = (flags & JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE) != 0;
                bool breakawayForbidden =
                    (flags & (JOB_OBJECT_LIMIT_BREAKAWAY_OK | JOB_OBJECT_LIMIT_SILENT_BREAKAWAY_OK)) == 0;
                if (!killOnClose || !breakawayForbidden)
                    throw new InvalidOperationException("The private Job did not preserve kill-on-close with breakaway forbidden.");
            }
            finally { Marshal.FreeHGlobal(memory); }
        }

        private static bool VerifyHandleNonInheritable(IntPtr handle)
        {
            uint flags;
            if (!GetHandleInformation(handle, out flags)) ThrowLastWin32("GetHandleInformation(Job)");
            if ((flags & HANDLE_FLAG_INHERIT) != 0)
                throw new InvalidOperationException("The private Job handle is inheritable.");
            return true;
        }

        private static void AssociateJobCompletionPort(IntPtr job, IntPtr completionPort)
        {
            JOBOBJECT_ASSOCIATE_COMPLETION_PORT association = new JOBOBJECT_ASSOCIATE_COMPLETION_PORT();
            association.CompletionKey = job;
            association.CompletionPort = completionPort;
            int size = Marshal.SizeOf(typeof(JOBOBJECT_ASSOCIATE_COMPLETION_PORT));
            IntPtr memory = Marshal.AllocHGlobal(size);
            try
            {
                Marshal.StructureToPtr(association, memory, false);
                if (!SetInformationJobObject(job, JobObjectAssociateCompletionPortInformation, memory, (uint)size))
                    ThrowLastWin32("SetInformationJobObject(CompletionPort)");
            }
            finally { Marshal.FreeHGlobal(memory); }
        }

        private static void TryPumpJobMessages(IntPtr port, List<string> diagnosticErrors)
        {
            try { PumpJobMessages(port); }
            catch (Exception ex) { RecordProcessDiagnosticError(diagnosticErrors, "completion-port messages", ex); }
        }

        private static void TryRefreshOwnedPidsFromJob(IntPtr job, List<string> diagnosticErrors)
        {
            try { RefreshOwnedPidsFromJob(job); }
            catch (Exception ex) { RecordProcessDiagnosticError(diagnosticErrors, "active PID snapshot", ex); }
        }

        private static void TryFinalizeProcessAccounting(RunResult result, IntPtr job, List<string> diagnosticErrors)
        {
            try { FinalizeProcessAccounting(result, job); }
            catch (Exception ex) { RecordProcessDiagnosticError(diagnosticErrors, "final Job process accounting", ex); }
        }

        private static void RecordProcessDiagnosticError(List<string> diagnosticErrors, string operation, Exception ex)
        {
            string message = operation + ": " + ex.GetType().FullName + ": " + ex.Message;
            if (message.Length > MAX_PROCESS_DIAGNOSTIC_ERROR_CHARACTERS)
                message = message.Substring(0, MAX_PROCESS_DIAGNOSTIC_ERROR_CHARACTERS);
            if (diagnosticErrors.Contains(message) || diagnosticErrors.Count >= MAX_PROCESS_DIAGNOSTIC_ERRORS)
                return;
            diagnosticErrors.Add(message);
        }

        private static void PumpJobMessages(IntPtr port)
        {
            if (port == IntPtr.Zero) return;
            while (true)
            {
                uint message;
                UIntPtr key;
                IntPtr overlapped;
                bool ok = GetQueuedCompletionStatus(port, out message, out key, out overlapped, 0);
                if (!ok)
                {
                    int error = Marshal.GetLastWin32Error();
                    if (error == 258) return;
                    throw new Win32Exception(error, "GetQueuedCompletionStatus failed");
                }
                if (message == JOB_OBJECT_MSG_NEW_PROCESS)
                {
                    int pid = unchecked((int)overlapped.ToInt64());
                    AddOwnedPid(pid);
                    lock (ObservationLock) NewProcessPids.Add(pid);
                }
            }
        }

        private static void RefreshOwnedPidsFromJob(IntPtr job)
        {
            int capacity = 64;
            while (capacity <= 65536)
            {
                int headerSize = 8;
                int size = headerSize + capacity * IntPtr.Size;
                IntPtr memory = Marshal.AllocHGlobal(size);
                try
                {
                    uint returned;
                    if (!QueryInformationJobObject(job, JobObjectBasicProcessIdList, memory, (uint)size, out returned))
                    {
                        int error = Marshal.GetLastWin32Error();
                        if (error == 234) { capacity *= 2; continue; }
                        throw new Win32Exception(error, "QueryInformationJobObject(ProcessIdList) failed");
                    }
                    uint assigned = unchecked((uint)Marshal.ReadInt32(memory, 0));
                    uint count = unchecked((uint)Marshal.ReadInt32(memory, 4));
                    if (assigned > count && capacity < assigned) { capacity = checked((int)assigned); continue; }
                    int offset = 8;
                    for (uint i = 0; i < count; i++)
                    {
                        int pid = unchecked((int)Marshal.ReadIntPtr(memory, offset + checked((int)i) * IntPtr.Size).ToInt64());
                        AddOwnedPid(pid);
                        lock (ObservationLock) ActiveSnapshotPids.Add(pid);
                    }
                    return;
                }
                finally { Marshal.FreeHGlobal(memory); }
            }
            throw new InvalidOperationException("Job process list exceeded the supported size.");
        }

        private static uint QueryActiveProcessCount(IntPtr job)
        {
            return QueryJobAccounting(job).ActiveProcesses;
        }

        private static JOBOBJECT_BASIC_ACCOUNTING_INFORMATION QueryJobAccounting(IntPtr job)
        {
            int size = Marshal.SizeOf(typeof(JOBOBJECT_BASIC_ACCOUNTING_INFORMATION));
            IntPtr memory = Marshal.AllocHGlobal(size);
            try
            {
                uint returned;
                if (!QueryInformationJobObject(job, JobObjectBasicAccountingInformation, memory, (uint)size, out returned))
                    ThrowLastWin32("QueryInformationJobObject(Accounting)");
                return (JOBOBJECT_BASIC_ACCOUNTING_INFORMATION)Marshal.PtrToStructure(
                    memory, typeof(JOBOBJECT_BASIC_ACCOUNTING_INFORMATION));
            }
            finally { Marshal.FreeHGlobal(memory); }
        }

        private static bool DrainTerminatedJob(IntPtr job, IntPtr port, int milliseconds,
            List<string> diagnosticErrors)
        {
            Stopwatch drain = Stopwatch.StartNew();
            while (drain.ElapsedMilliseconds < milliseconds)
            {
                TryPumpJobMessages(port, diagnosticErrors);
                TryRefreshOwnedPidsFromJob(job, diagnosticErrors);
                if (QueryActiveProcessCount(job) == 0) return true;
                Thread.Sleep(10);
            }
            return QueryActiveProcessCount(job) == 0;
        }

        private static void AddOwnedPid(int pid)
        {
            if (pid <= 0) return;
            lock (ObservationLock) EverOwnedPids.Add(pid);
        }

        private static void ResetObservationState()
        {
            lock (ObservationLock)
            {
                EverOwnedPids.Clear();
                NewProcessPids.Clear();
                ActiveSnapshotPids.Clear();
            }
        }

        private static int[] SortedPidArray(HashSet<int> source)
        {
            int[] values = new int[source.Count];
            source.CopyTo(values);
            Array.Sort(values);
            return values;
        }

        private static void PopulateObservationResult(RunResult result, PrivateDesktopWatcher watcher)
        {
            lock (ObservationLock)
            {
                result.ProcessIds = SortedPidArray(EverOwnedPids);
                result.NewProcessIds = SortedPidArray(NewProcessPids);
                result.ActiveSnapshotProcessIds = SortedPidArray(ActiveSnapshotPids);
                result.ObservedDistinctProcessIdCount = EverOwnedPids.Count;
            }
            result.VisibleWindows = watcher == null ? new WindowEvidence[0] : watcher.SnapshotWindows();
        }

        private static void FinalizeProcessAccounting(RunResult result, IntPtr job)
        {
            JOBOBJECT_BASIC_ACCOUNTING_INFORMATION accounting = QueryJobAccounting(job);
            int total = checked((int)accounting.TotalProcesses);
            int observed;
            lock (ObservationLock) observed = EverOwnedPids.Count;
            result.JobTotalProcesses = total;
            result.ObservedDistinctProcessIdCount = observed;
        }

        private sealed class PrivateDesktopWatcher
        {
            private readonly IntPtr desktopHandle;
            private readonly string desktopName;
            private readonly object stateLock = new object();
            private readonly List<WindowCandidate> candidates = new List<WindowCandidate>();
            private readonly Dictionary<string, WindowEvidence> accepted =
                new Dictionary<string, WindowEvidence>(StringComparer.Ordinal);
            private readonly ManualResetEvent armed = new ManualResetEvent(false);
            private readonly ManualResetEvent stop = new ManualResetEvent(false);
            private Thread thread;
            private Exception failure;
            private uint nativeThreadId;
            private bool initiallyEmpty;
            private DateTime armedUtc;
            private WinEventDelegate winEventCallback;
            private EnumDesktopWindowsDelegate enumDesktopCallback;

            public PrivateDesktopWatcher(IntPtr desktopHandle, string desktopName)
            {
                this.desktopHandle = desktopHandle;
                this.desktopName = desktopName;
            }

            public bool HasAcceptedWindows
            {
                get { lock (stateLock) return accepted.Count != 0; }
            }

            public DateTime ArmedUtc
            {
                get { lock (stateLock) return armedUtc; }
            }

            public bool InitiallyEmpty
            {
                get { lock (stateLock) return initiallyEmpty; }
            }

            public void StartAndWaitUntilArmed(int milliseconds)
            {
                thread = new Thread(ThreadMain);
                thread.IsBackground = true;
                thread.Name = "CosPrivateDesktopWatcher";
                thread.Start();
                if (!armed.WaitOne(milliseconds))
                    throw new TimeoutException("Private-desktop watcher did not arm before launch.");
                ThrowIfFailed();
            }

            public void ThrowIfFailed()
            {
                Exception observed;
                lock (stateLock) observed = failure;
                if (observed != null)
                    throw new InvalidOperationException("Private-desktop watcher failed: " + observed.Message, observed);
            }

            public void StopAndJoin(int milliseconds)
            {
                if (thread == null) return;
                stop.Set();
                if (!thread.Join(milliseconds))
                    throw new TimeoutException("Private-desktop watcher did not stop.");
            }

            public void DisposeEventsAfterJoin()
            {
                if (thread != null && thread.IsAlive)
                    throw new InvalidOperationException("Cannot dispose watcher events while its thread is alive.");
                armed.Dispose();
                stop.Dispose();
            }

            public void Reconcile()
            {
                lock (stateLock) ReconcilePendingCandidates();
            }

            private void ReconcilePendingCandidates()
            {
                for (int i = 0; i < candidates.Count; i++)
                {
                    WindowCandidate item = candidates[i];
                    string key = item.Pid.ToString(System.Globalization.CultureInfo.InvariantCulture) + ":" +
                        item.Hwnd.ToInt64().ToString("X", System.Globalization.CultureInfo.InvariantCulture);
                    WindowEvidence evidence = new WindowEvidence {
                        Pid = item.Pid,
                        Hwnd = "0x" + item.Hwnd.ToInt64().ToString("X", System.Globalization.CultureInfo.InvariantCulture),
                        Event = item.Source,
                        Title = item.Title,
                        ClassName = item.ClassName,
                        Desktop = desktopName,
                        ObservedUtc = FormatUtc(item.ObservedUtc)
                    };
                    WindowEvidence existing;
                    if (accepted.TryGetValue(key, out existing))
                    {
                        if (item.PrivateShowProof && !String.Equals(existing.Event, "EVENT_OBJECT_SHOW", StringComparison.Ordinal))
                            accepted[key] = evidence;
                        continue;
                    }
                    accepted[key] = evidence;
                }
            }

            public WindowEvidence[] SnapshotWindows()
            {
                lock (stateLock)
                {
                    ReconcilePendingCandidates();
                    List<WindowEvidence> values = new List<WindowEvidence>(accepted.Values);
                    values.Sort(delegate(WindowEvidence left, WindowEvidence right) {
                        int pidOrder = left.Pid.CompareTo(right.Pid);
                        return pidOrder != 0 ? pidOrder : String.CompareOrdinal(left.Hwnd, right.Hwnd);
                    });
                    return values.ToArray();
                }
            }

            private void ThreadMain()
            {
                IntPtr createHook = IntPtr.Zero;
                IntPtr showHook = IntPtr.Zero;
                try
                {
                    if (!SetThreadDesktop(desktopHandle)) ThrowLastWin32("SetThreadDesktop(private watcher)");
                    nativeThreadId = GetCurrentThreadId();
                    MSG queueProbe;
                    PeekMessageW(out queueProbe, IntPtr.Zero, 0, 0, PM_NOREMOVE);
                    winEventCallback = OnWinEvent;
                    enumDesktopCallback = OnEnumDesktopWindow;
                    createHook = SetWinEventHook(EVENT_OBJECT_CREATE, EVENT_OBJECT_CREATE, IntPtr.Zero,
                        winEventCallback, 0, 0, WINEVENT_OUTOFCONTEXT);
                    if (createHook == IntPtr.Zero) ThrowLastWin32("SetWinEventHook(EVENT_OBJECT_CREATE)");
                    showHook = SetWinEventHook(EVENT_OBJECT_SHOW, EVENT_OBJECT_SHOW, IntPtr.Zero,
                        winEventCallback, 0, 0, WINEVENT_OUTOFCONTEXT);
                    if (showHook == IntPtr.Zero) ThrowLastWin32("SetWinEventHook(EVENT_OBJECT_SHOW)");

                    EnumeratePrivateDesktop("prelaunch-enumeration");
                    lock (stateLock)
                    {
                        if (candidates.Count != 0)
                            throw new InvalidOperationException("A newly created private desktop was not empty.");
                        initiallyEmpty = true;
                        armedUtc = DateTime.UtcNow;
                    }
                    armed.Set();

                    while (!stop.WaitOne(2))
                    {
                        PumpWindowMessages();
                        EnumeratePrivateDesktop("desktop-enumeration");
                    }
                    PumpWindowMessages();
                    EnumeratePrivateDesktop("final-enumeration");
                }
                catch (Exception ex)
                {
                    RecordFailure(ex);
                    armed.Set();
                }
                finally
                {
                    if (showHook != IntPtr.Zero && !UnhookWinEvent(showHook))
                        RecordFailure(new Win32Exception(Marshal.GetLastWin32Error(), "UnhookWinEvent(SHOW) failed"));
                    if (createHook != IntPtr.Zero && !UnhookWinEvent(createHook))
                        RecordFailure(new Win32Exception(Marshal.GetLastWin32Error(), "UnhookWinEvent(CREATE) failed"));
                    armed.Set();
                }
            }

            private void RecordFailure(Exception ex)
            {
                lock (stateLock) if (failure == null) failure = ex;
            }

            private void OnWinEvent(IntPtr hook, uint eventType, IntPtr hwnd, int idObject,
                int idChild, uint eventThread, uint eventTime)
            {
                if (hwnd == IntPtr.Zero || idObject != OBJID_WINDOW || idChild != CHILDID_SELF) return;
                try
                {
                    CaptureVisibleTopLevel(hwnd,
                        eventType == EVENT_OBJECT_SHOW ? "EVENT_OBJECT_SHOW" : "EVENT_OBJECT_CREATE",
                        eventType == EVENT_OBJECT_SHOW);
                }
                catch (Exception ex) { RecordFailure(ex); }
            }

            private bool OnEnumDesktopWindow(IntPtr hwnd, IntPtr parameter)
            {
                try
                {
                    string source = Marshal.PtrToStringUni(parameter);
                    CaptureVisibleTopLevel(hwnd, source == null ? "EnumDesktopWindows" : source, false);
                    return true;
                }
                catch (Exception ex)
                {
                    RecordFailure(ex);
                    return false;
                }
            }

            private void EnumeratePrivateDesktop(string source)
            {
                IntPtr sourceMemory = Marshal.StringToHGlobalUni(source);
                try
                {
                    SetLastError(0);
                    if (!EnumDesktopWindows(desktopHandle, enumDesktopCallback, sourceMemory))
                    {
                        int error = Marshal.GetLastWin32Error();
                        if (error != 0) throw new Win32Exception(error, "EnumDesktopWindows failed");
                        ThrowIfFailed();
                    }
                }
                finally { Marshal.FreeHGlobal(sourceMemory); }
            }

            private void CaptureVisibleTopLevel(IntPtr hwnd, string source, bool privateShowProof)
            {
                if (GetCurrentThreadId() != nativeThreadId)
                    throw new InvalidOperationException("A window candidate arrived outside the dedicated watcher thread.");
                bool windowAlive = IsWindow(hwnd);
                if (!privateShowProof)
                {
                    if (!windowAlive || !IsWindowVisible(hwnd) || GetAncestor(hwnd, GA_ROOT) != hwnd) return;
                }
                else if (windowAlive)
                {
                    IntPtr root = GetAncestor(hwnd, GA_ROOT);
                    if (root != IntPtr.Zero && root != hwnd) return;
                }

                uint pid = 0;
                uint windowThread = windowAlive ? GetWindowThreadProcessId(hwnd, out pid) : 0;
                if (windowThread == 0) pid = 0;

                WindowCandidate candidate = new WindowCandidate();
                candidate.Pid = unchecked((int)pid);
                candidate.Hwnd = hwnd;
                candidate.Source = source;
                candidate.Title = windowAlive ? ReadWindowText(hwnd) : "";
                candidate.ClassName = windowAlive ? ReadClassName(hwnd) : "";
                candidate.PrivateShowProof = privateShowProof;
                candidate.ObservedUtc = DateTime.UtcNow;
                lock (stateLock) candidates.Add(candidate);
            }

            private static void PumpWindowMessages()
            {
                MSG message;
                while (PeekMessageW(out message, IntPtr.Zero, 0, 0, PM_REMOVE))
                {
                    TranslateMessage(ref message);
                    DispatchMessageW(ref message);
                }
            }
        }

        private static string ReadWindowText(IntPtr hwnd)
        {
            int length = GetWindowTextLengthW(hwnd);
            StringBuilder text = new StringBuilder(Math.Max(length + 1, 2));
            GetWindowTextW(hwnd, text, text.Capacity);
            return text.ToString();
        }

        private static string ReadClassName(IntPtr hwnd)
        {
            StringBuilder text = new StringBuilder(512);
            int count = GetClassNameW(hwnd, text, text.Capacity);
            return count > 0 ? text.ToString() : "";
        }

        private static int CheckedUIntPtrToInt(UIntPtr value)
        {
            ulong raw = value.ToUInt64();
            if (raw > Int32.MaxValue) throw new OverflowException("Native allocation exceeds Int32.MaxValue.");
            return (int)raw;
        }

        private static IntPtr CloseKernelHandleForCleanup(IntPtr handle, string name, List<string> cleanupErrors)
        {
            if (handle != IntPtr.Zero && handle != INVALID_HANDLE_VALUE && !CloseHandle(handle))
                cleanupErrors.Add("CloseHandle(" + name + "): " +
                    new Win32Exception(Marshal.GetLastWin32Error()).Message);
            return IntPtr.Zero;
        }

        private static void TerminateJobOrThrow(IntPtr job, uint exitCode, string operation)
        {
            if (!TerminateJobObject(job, exitCode)) ThrowLastWin32(operation);
        }

        private static void ThrowLastWin32(string operation)
        {
            int error = Marshal.GetLastWin32Error();
            throw new Win32Exception(error, operation + " failed");
        }

        private sealed class WindowCandidate
        {
            public int Pid;
            public IntPtr Hwnd;
            public string Source;
            public string Title;
            public string ClassName;
            public bool PrivateShowProof;
            public DateTime ObservedUtc;
        }

        [StructLayout(LayoutKind.Sequential, CharSet = CharSet.Unicode)]
        private struct STARTUPINFO
        {
            public int cb; public string lpReserved; public string lpDesktop; public string lpTitle;
            public int dwX; public int dwY; public int dwXSize; public int dwYSize;
            public int dwXCountChars; public int dwYCountChars; public int dwFillAttribute;
            public uint dwFlags; public short wShowWindow; public short cbReserved2;
            public IntPtr lpReserved2; public IntPtr hStdInput; public IntPtr hStdOutput; public IntPtr hStdError;
        }

        [StructLayout(LayoutKind.Sequential)]
        private struct STARTUPINFOEX { public STARTUPINFO StartupInfo; public IntPtr lpAttributeList; }

        [StructLayout(LayoutKind.Sequential)]
        private struct PROCESS_INFORMATION
        {
            public IntPtr hProcess; public IntPtr hThread; public uint dwProcessId; public uint dwThreadId;
        }

        [StructLayout(LayoutKind.Sequential)]
        private struct SECURITY_ATTRIBUTES
        {
            public int nLength; public IntPtr lpSecurityDescriptor;
            [MarshalAs(UnmanagedType.Bool)] public bool bInheritHandle;
        }

        [StructLayout(LayoutKind.Sequential)]
        private struct JOBOBJECT_BASIC_LIMIT_INFORMATION
        {
            public long PerProcessUserTimeLimit; public long PerJobUserTimeLimit; public uint LimitFlags;
            public UIntPtr MinimumWorkingSetSize; public UIntPtr MaximumWorkingSetSize;
            public uint ActiveProcessLimit; public UIntPtr Affinity; public uint PriorityClass; public uint SchedulingClass;
        }

        [StructLayout(LayoutKind.Sequential)]
        private struct IO_COUNTERS
        {
            public ulong ReadOperationCount; public ulong WriteOperationCount; public ulong OtherOperationCount;
            public ulong ReadTransferCount; public ulong WriteTransferCount; public ulong OtherTransferCount;
        }

        [StructLayout(LayoutKind.Sequential)]
        private struct JOBOBJECT_EXTENDED_LIMIT_INFORMATION
        {
            public JOBOBJECT_BASIC_LIMIT_INFORMATION BasicLimitInformation; public IO_COUNTERS IoInfo;
            public UIntPtr ProcessMemoryLimit; public UIntPtr JobMemoryLimit;
            public UIntPtr PeakProcessMemoryUsed; public UIntPtr PeakJobMemoryUsed;
        }

        [StructLayout(LayoutKind.Sequential)]
        private struct JOBOBJECT_ASSOCIATE_COMPLETION_PORT
        {
            public IntPtr CompletionKey; public IntPtr CompletionPort;
        }

        [StructLayout(LayoutKind.Sequential)]
        private struct JOBOBJECT_BASIC_ACCOUNTING_INFORMATION
        {
            public long TotalUserTime; public long TotalKernelTime; public long ThisPeriodTotalUserTime;
            public long ThisPeriodTotalKernelTime; public uint TotalPageFaultCount;
            public uint TotalProcesses; public uint ActiveProcesses; public uint TotalTerminatedProcesses;
        }

        [StructLayout(LayoutKind.Sequential)]
        private struct POINT { public int x; public int y; }

        [StructLayout(LayoutKind.Sequential)]
        private struct MSG
        {
            public IntPtr hwnd; public uint message; public UIntPtr wParam; public IntPtr lParam;
            public uint time; public POINT pt;
        }

        private delegate void WinEventDelegate(IntPtr hook, uint eventType, IntPtr hwnd, int idObject,
            int idChild, uint eventThread, uint eventTime);
        private delegate bool EnumDesktopWindowsDelegate(IntPtr hwnd, IntPtr parameter);

        [DllImport("user32.dll", CharSet = CharSet.Unicode, SetLastError = true)]
        private static extern IntPtr CreateDesktopW(string desktop, string device, IntPtr devmode,
            uint flags, uint desiredAccess, IntPtr securityAttributes);
        [DllImport("user32.dll", SetLastError = true)] private static extern bool CloseDesktop(IntPtr desktop);
        [DllImport("user32.dll", SetLastError = true)] private static extern bool EnumDesktopWindows(IntPtr desktop, EnumDesktopWindowsDelegate callback, IntPtr parameter);
        [DllImport("user32.dll", SetLastError = true)] private static extern IntPtr SetWinEventHook(uint eventMin, uint eventMax, IntPtr module, WinEventDelegate callback, uint process, uint thread, uint flags);
        [DllImport("user32.dll", SetLastError = true)] private static extern bool UnhookWinEvent(IntPtr hook);
        [DllImport("user32.dll")] private static extern bool IsWindow(IntPtr hwnd);
        [DllImport("user32.dll")] private static extern bool IsWindowVisible(IntPtr hwnd);
        [DllImport("user32.dll")] private static extern IntPtr GetAncestor(IntPtr hwnd, uint flags);
        [DllImport("user32.dll", SetLastError = true)] private static extern uint GetWindowThreadProcessId(IntPtr hwnd, out uint processId);
        [DllImport("user32.dll", CharSet = CharSet.Unicode)] private static extern int GetWindowTextLengthW(IntPtr hwnd);
        [DllImport("user32.dll", CharSet = CharSet.Unicode)] private static extern int GetWindowTextW(IntPtr hwnd, StringBuilder text, int count);
        [DllImport("user32.dll", CharSet = CharSet.Unicode)] private static extern int GetClassNameW(IntPtr hwnd, StringBuilder text, int count);
        [DllImport("user32.dll", SetLastError = true)] private static extern bool SetThreadDesktop(IntPtr desktop);
        [DllImport("user32.dll")] private static extern bool PeekMessageW(out MSG message, IntPtr hwnd, uint min, uint max, uint remove);
        [DllImport("user32.dll")] private static extern bool TranslateMessage(ref MSG message);
        [DllImport("user32.dll")] private static extern IntPtr DispatchMessageW(ref MSG message);

        [DllImport("kernel32.dll", CharSet = CharSet.Unicode, SetLastError = true)]
        private static extern bool CreateProcessW(string applicationName, StringBuilder commandLine,
            IntPtr processAttributes, IntPtr threadAttributes, bool inheritHandles, uint creationFlags,
            IntPtr environment, string currentDirectory, ref STARTUPINFOEX startupInfo,
            out PROCESS_INFORMATION processInformation);
        [DllImport("kernel32.dll", SetLastError = true)] private static extern uint ResumeThread(IntPtr thread);
        [DllImport("kernel32.dll", SetLastError = true)] private static extern uint WaitForSingleObject(IntPtr handle, uint milliseconds);
        [DllImport("kernel32.dll", SetLastError = true)] private static extern bool GetExitCodeProcess(IntPtr process, out uint exitCode);
        [DllImport("kernel32.dll", SetLastError = true)] private static extern bool CloseHandle(IntPtr handle);
        [DllImport("kernel32.dll", SetLastError = true)] private static extern bool GetHandleInformation(IntPtr handle, out uint flags);
        [DllImport("kernel32.dll")] private static extern uint GetCurrentThreadId();
        [DllImport("kernel32.dll", SetLastError = true)] private static extern bool IsProcessInJob(IntPtr process, IntPtr job, out bool result);
        [DllImport("kernel32.dll", CharSet = CharSet.Unicode, SetLastError = true)]
        private static extern IntPtr CreateFileW(string name, uint access, uint share, ref SECURITY_ATTRIBUTES security,
            uint creation, uint flags, IntPtr template);
        [DllImport("kernel32.dll", SetLastError = true)] private static extern bool InitializeProcThreadAttributeList(IntPtr list, int count, int flags, ref UIntPtr size);
        [DllImport("kernel32.dll", SetLastError = true)] private static extern bool UpdateProcThreadAttribute(IntPtr list, uint flags, UIntPtr attribute, IntPtr value, UIntPtr size, IntPtr previous, IntPtr returnedSize);
        [DllImport("kernel32.dll")] private static extern void DeleteProcThreadAttributeList(IntPtr list);
        [DllImport("kernel32.dll", CharSet = CharSet.Unicode, SetLastError = true)] private static extern IntPtr CreateJobObjectW(IntPtr attributes, string name);
        [DllImport("kernel32.dll", SetLastError = true)] private static extern bool SetInformationJobObject(IntPtr job, uint infoClass, IntPtr info, uint length);
        [DllImport("kernel32.dll", SetLastError = true)] private static extern bool QueryInformationJobObject(IntPtr job, uint infoClass, IntPtr info, uint length, out uint returnedLength);
        [DllImport("kernel32.dll", SetLastError = true)] private static extern bool TerminateJobObject(IntPtr job, uint exitCode);
        [DllImport("kernel32.dll", SetLastError = true)] private static extern IntPtr CreateIoCompletionPort(IntPtr file, IntPtr existingPort, UIntPtr completionKey, uint threads);
        [DllImport("kernel32.dll", SetLastError = true)] private static extern bool GetQueuedCompletionStatus(IntPtr port, out uint bytes, out UIntPtr key, out IntPtr overlapped, uint milliseconds);
        [DllImport("kernel32.dll")] private static extern void SetLastError(uint errorCode);
    }
}
```

## Appendix B — `Invoke-PrivateDesktopProcess.ps1`

Exact committed helper payload: **24,229 bytes**; **SHA-256 `73A3F9C43CF994E08F004E0A1266122A3EC5E0EAF065C63E6D9439CF0B0E1880`**. The fenced body below is the complete UTF-8, no-BOM source and includes its final LF.

```powershell
[CmdletBinding()]
param(
    [switch]$PrivateDesktopInternalHostMode,
    [string]$PrivateDesktopInternalRequestPath,
    [string]$PrivateDesktopInternalRunnerSource
)

$PrivateDesktopWrapperScriptPath = [IO.Path]::GetFullPath($PSCommandPath)

function Write-NewUtf8File {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)][string]$LiteralPath,
        [Parameter(Mandatory = $true)][string]$Text
    )
    $Encoding = New-Object System.Text.UTF8Encoding($false, $true)
    $Stream = New-Object System.IO.FileStream(
        $LiteralPath,
        [IO.FileMode]::CreateNew,
        [IO.FileAccess]::Write,
        [IO.FileShare]::Read
    )
    try {
        $Writer = New-Object System.IO.StreamWriter($Stream, $Encoding)
        try {
            $Writer.Write($Text)
            $Writer.Flush()
            $Stream.Flush($true)
        } finally {
            $Writer.Dispose()
        }
    } finally {
        $Stream.Dispose()
    }
}

function ConvertTo-PrivateDesktopHostArgument {
    [CmdletBinding()]
    param([Parameter(Mandatory = $true)][AllowEmptyString()][string]$Value)

    if ($Value.Length -eq 0) { return '""' }
    if ($Value -notmatch '[\s"]') { return $Value }

    $Builder = New-Object System.Text.StringBuilder
    [void]$Builder.Append([char]34)
    $SlashCount = 0
    foreach ($Character in $Value.ToCharArray()) {
        if ($Character -eq [char]92) {
            $SlashCount++
            continue
        }
        if ($Character -eq [char]34) {
            [void]$Builder.Append([char]92, ($SlashCount * 2) + 1)
            [void]$Builder.Append([char]34)
            $SlashCount = 0
            continue
        }
        [void]$Builder.Append([char]92, $SlashCount)
        $SlashCount = 0
        [void]$Builder.Append($Character)
    }
    [void]$Builder.Append([char]92, $SlashCount * 2)
    [void]$Builder.Append([char]34)
    return $Builder.ToString()
}

function Invoke-PrivateDesktopHostFailClosedTeardown {
    [CmdletBinding()]
    param([Parameter(Mandatory = $true)][System.Diagnostics.Process]$Process)

    $KillIssued = $false
    $KillError = $null
    try {
        $Process.Kill()
        $KillIssued = $true
    } catch {
        $KillError = $_.Exception.Message
    }

    $ExitProven = $false
    $ExitProofError = $null
    try {
        $BoundedWaitCompleted = $Process.WaitForExit(5000)
        if ($BoundedWaitCompleted) {
            $ExitProven = $Process.HasExited
        }
    } catch {
        $ExitProofError = $_.Exception.Message
    }

    return [pscustomobject][ordered]@{
        kill_issued = $KillIssued
        kill_error = $KillError
        exit_proven = $ExitProven
        exit_proof_error = $ExitProofError
    }
}

function Test-PrivateDesktopIntegralValue {
    [CmdletBinding()]
    param($Value)

    return ($Value -is [byte] -or $Value -is [sbyte] -or
        $Value -is [int16] -or $Value -is [uint16] -or
        $Value -is [int32] -or $Value -is [uint32] -or
        $Value -is [int64] -or $Value -is [uint64])
}

function Get-PrivateDesktopMappedHelperExitCode {
    [CmdletBinding()]
    param([Parameter(Mandatory = $true)][string]$Classification)

    if ($Classification -ceq 'COMPLETED') { return 0 }
    if ($Classification -ceq 'NEEDS_CONTEXT') { return 20 }
    if ($Classification -ceq 'TIMEOUT') { return 21 }
    if ($Classification -ceq 'LAUNCH_ERROR') { return 22 }
    throw "Unknown private desktop helper classification: $Classification"
}

function Assert-PrivateDesktopResultDocument {
    [CmdletBinding()]
    param([Parameter(Mandatory = $true)]$Result)

    if ($null -eq $Result) { throw 'Private desktop result was null.' }
    if ($Result.PSObject.Properties.Match('process_coverage_complete').Count -ne 0) {
        throw 'Legacy process_coverage_complete is forbidden in result schema v2.'
    }
    $ExpectedProperties = @(
        'schema_version', 'classification', 'detail', 'started', 'root_pid', 'root_exit_code',
        'timed_out', 'job_drained', 'desktop_name', 'process_ids', 'new_process_ids',
        'active_snapshot_process_ids', 'job_total_processes', 'observed_distinct_process_id_count',
        'process_id_accounting_kind', 'process_diagnostic_errors', 'private_desktop_initially_empty',
        'monitor_armed_before_create', 'monitor_armed_before_resume', 'monitor_armed_utc',
        'process_created_utc', 'resumed_utc', 'root_assigned_to_job_before_resume',
        'job_kill_on_close_verified', 'job_breakaway_forbidden',
        'job_handle_non_inheritable', 'job_active_processes_final',
        'monitor_completed_after_job_drain', 'host_termination_required',
        'cleanup_complete', 'cleanup_errors', 'visible_windows', 'started_utc', 'finished_utc',
        'elapsed_milliseconds', 'stdout_path', 'stderr_path', 'helper_exit_code'
    )
    $ExpectedSignature = (@($ExpectedProperties | Sort-Object) -join "`n")
    $ActualSignature = (@($Result.PSObject.Properties.Name | Sort-Object) -join "`n")
    if ($ActualSignature -cne $ExpectedSignature) {
        throw 'Private desktop result does not have the exact schema-v2 property set.'
    }
    if (-not (Test-PrivateDesktopIntegralValue $Result.schema_version) -or [int64]$Result.schema_version -ne 2) {
        throw 'Private desktop helper result schema must be exactly 2.'
    }
    if ($Result.classification -isnot [string]) {
        throw 'Private desktop classification must be a string.'
    }
    $MappedHelperExitCode = Get-PrivateDesktopMappedHelperExitCode -Classification $Result.classification
    if (-not (Test-PrivateDesktopIntegralValue $Result.helper_exit_code) -or
        @(0, 20, 21, 22) -notcontains [int64]$Result.helper_exit_code -or
        [int64]$Result.helper_exit_code -ne $MappedHelperExitCode) {
        throw 'Persisted helper_exit_code is missing, unknown, or inconsistent with classification.'
    }
    foreach ($BooleanField in @(
        'started', 'timed_out', 'job_drained', 'private_desktop_initially_empty',
        'monitor_armed_before_create', 'monitor_armed_before_resume',
        'root_assigned_to_job_before_resume', 'job_kill_on_close_verified',
        'job_breakaway_forbidden', 'job_handle_non_inheritable',
        'monitor_completed_after_job_drain', 'host_termination_required', 'cleanup_complete'
    )) {
        if ($Result.$BooleanField -isnot [bool]) {
            throw "Private desktop result field must be Boolean: $BooleanField"
        }
    }
    if ($null -ne $Result.root_pid -and
        (-not (Test-PrivateDesktopIntegralValue $Result.root_pid) -or [int64]$Result.root_pid -le 0)) {
        throw 'root_pid must be null or a positive integer.'
    }
    if ($null -ne $Result.root_exit_code -and -not (Test-PrivateDesktopIntegralValue $Result.root_exit_code)) {
        throw 'root_exit_code must be null or an integer.'
    }
    if ($null -ne $Result.job_active_processes_final -and
        (-not (Test-PrivateDesktopIntegralValue $Result.job_active_processes_final) -or
         [int64]$Result.job_active_processes_final -lt 0)) {
        throw 'job_active_processes_final must be null or a nonnegative integer.'
    }
    if ([string]$Result.process_id_accounting_kind -cne 'diagnostic_distinct_pid') {
        throw 'process_id_accounting_kind must be diagnostic_distinct_pid.'
    }
    foreach ($PidField in @('process_ids', 'new_process_ids', 'active_snapshot_process_ids')) {
        if ($Result.$PidField -isnot [System.Array]) {
            throw ($PidField + ' must be present as a diagnostic PID array.')
        }
        foreach ($ProcessId in @($Result.$PidField)) {
            if (-not (Test-PrivateDesktopIntegralValue $ProcessId) -or [int64]$ProcessId -le 0) {
                throw ($PidField + ' contains a non-positive or non-integral PID.')
            }
        }
    }
    if (-not (Test-PrivateDesktopIntegralValue $Result.observed_distinct_process_id_count) -or
        [int64]$Result.observed_distinct_process_id_count -lt 0) {
        throw 'observed_distinct_process_id_count must be a nonnegative diagnostic integer.'
    }
    if ($null -ne $Result.job_total_processes -and
        (-not (Test-PrivateDesktopIntegralValue $Result.job_total_processes) -or
         [int64]$Result.job_total_processes -lt 0)) {
        throw 'job_total_processes must be null or a nonnegative diagnostic integer.'
    }
    if ($Result.process_diagnostic_errors -isnot [System.Array]) {
        throw 'process_diagnostic_errors must be present as an array.'
    }
    foreach ($DiagnosticError in @($Result.process_diagnostic_errors)) {
        if ($DiagnosticError -isnot [string]) {
            throw 'process_diagnostic_errors contains a non-string value.'
        }
    }
    if ($Result.cleanup_errors -isnot [System.Array]) {
        throw 'cleanup_errors must be present as an array.'
    }
    foreach ($CleanupError in @($Result.cleanup_errors)) {
        if ($CleanupError -isnot [string]) { throw 'cleanup_errors contains a non-string value.' }
    }
    if ($Result.visible_windows -isnot [System.Array]) {
        throw 'visible_windows must be present as an array.'
    }
    if (@($Result.visible_windows).Count -ne 0 -and $Result.classification -cne 'NEEDS_CONTEXT') {
        throw 'Visible-window evidence requires NEEDS_CONTEXT classification.'
    }
}

function Test-PrivateDesktopParentHostResult {
    [CmdletBinding()]
    [OutputType([bool])]
    param(
        [Parameter(Mandatory = $true)]$Result,
        [Parameter(Mandatory = $true)]$ActualHostExitCode
    )

    Assert-PrivateDesktopResultDocument -Result $Result
    if (-not (Test-PrivateDesktopIntegralValue $ActualHostExitCode) -or
        @(0, 20, 21, 22) -notcontains [int64]$ActualHostExitCode -or
        [int64]$ActualHostExitCode -ne [int64]$Result.helper_exit_code) {
        throw 'Actual PowerShell host exit does not match persisted helper_exit_code.'
    }
    if (-not $Result.host_termination_required) {
        Assert-PrivateDesktopSafetyEnvelope -Result $Result
        return $true
    }
    if ($Result.classification -cne 'NEEDS_CONTEXT' -or [int64]$Result.helper_exit_code -ne 20) {
        throw 'Catastrophic helper-host termination must be NEEDS_CONTEXT with exit 20.'
    }
    if ($Result.cleanup_complete -or $Result.monitor_completed_after_job_drain) {
        throw 'Catastrophic helper-host termination cannot claim cleanup or monitor completion.'
    }
    return $false
}

function Assert-PrivateDesktopSafetyEnvelope {
    [CmdletBinding()]
    param([Parameter(Mandatory = $true)]$Result)

    Assert-PrivateDesktopResultDocument -Result $Result

    if ($null -eq $Result) { throw 'Private desktop result was null.' }
    if ($Result.PSObject.Properties.Match('process_coverage_complete').Count -ne 0) {
        throw 'Legacy process_coverage_complete is forbidden in result schema v2.'
    }

    $ExpectedProperties = @(
        'schema_version', 'classification', 'detail', 'started', 'root_pid', 'root_exit_code',
        'timed_out', 'job_drained', 'desktop_name', 'process_ids', 'new_process_ids',
        'active_snapshot_process_ids', 'job_total_processes', 'observed_distinct_process_id_count',
        'process_id_accounting_kind', 'process_diagnostic_errors', 'private_desktop_initially_empty',
        'monitor_armed_before_create', 'monitor_armed_before_resume', 'monitor_armed_utc',
        'process_created_utc', 'resumed_utc', 'root_assigned_to_job_before_resume',
        'job_kill_on_close_verified', 'job_breakaway_forbidden',
        'job_handle_non_inheritable', 'job_active_processes_final',
        'monitor_completed_after_job_drain', 'host_termination_required',
        'cleanup_complete', 'cleanup_errors',
        'visible_windows', 'started_utc', 'finished_utc', 'elapsed_milliseconds',
        'stdout_path', 'stderr_path', 'helper_exit_code'
    )
    $ExpectedSignature = (@($ExpectedProperties | Sort-Object) -join "`n")
    $ActualSignature = (@($Result.PSObject.Properties.Name | Sort-Object) -join "`n")
    if ($ActualSignature -cne $ExpectedSignature) {
        throw 'Private desktop result does not have the exact schema-v2 property set.'
    }
    if (-not (Test-PrivateDesktopIntegralValue $Result.schema_version) -or [int64]$Result.schema_version -ne 2) {
        throw 'Private desktop helper result schema must be exactly 2.'
    }
    if ($Result.started -isnot [bool] -or -not $Result.started) {
        throw 'Safety-envelope validation requires a started helper result.'
    }
    if (-not (Test-PrivateDesktopIntegralValue $Result.root_pid) -or [int64]$Result.root_pid -le 0) {
        throw 'Started helper result has no valid root_pid.'
    }
    if (-not (Test-PrivateDesktopIntegralValue $Result.helper_exit_code) -or
        @(0, 20, 21, 22) -notcontains [int64]$Result.helper_exit_code) {
        throw 'Persisted helper_exit_code is missing, non-integral, or unknown.'
    }
    $MappedHelperExitCode = Get-PrivateDesktopMappedHelperExitCode -Classification ([string]$Result.classification)
    if ([int64]$Result.helper_exit_code -ne $MappedHelperExitCode) {
        throw 'Persisted helper_exit_code does not match classification.'
    }

    foreach ($Gate in @(
        'private_desktop_initially_empty',
        'monitor_armed_before_create',
        'monitor_armed_before_resume',
        'root_assigned_to_job_before_resume',
        'job_kill_on_close_verified',
        'job_breakaway_forbidden',
        'job_handle_non_inheritable',
        'job_drained',
        'monitor_completed_after_job_drain',
        'cleanup_complete'
    )) {
        if ($Result.$Gate -isnot [bool] -or -not $Result.$Gate) {
            throw "Private desktop safety gate failed: $Gate"
        }
    }
    if ($Result.host_termination_required -isnot [bool] -or $Result.host_termination_required) {
        throw 'Reusable helper result requires host_termination_required=false.'
    }
    if ($null -eq $Result.cleanup_errors -or @($Result.cleanup_errors).Count -ne 0) {
        throw 'Private desktop helper reported cleanup errors.'
    }
    if (-not (Test-PrivateDesktopIntegralValue $Result.job_active_processes_final) -or
        [int64]$Result.job_active_processes_final -ne 0) {
        throw 'Final Job ActiveProcesses must be exactly zero.'
    }
    if ([string]$Result.process_id_accounting_kind -cne 'diagnostic_distinct_pid') {
        throw 'process_id_accounting_kind must be diagnostic_distinct_pid.'
    }
    foreach ($PidField in @('process_ids', 'new_process_ids', 'active_snapshot_process_ids')) {
        if ($Result.$PidField -isnot [System.Array]) {
            throw ($PidField + ' must be present as a diagnostic PID array.')
        }
        foreach ($ProcessId in @($Result.$PidField)) {
            if (-not (Test-PrivateDesktopIntegralValue $ProcessId) -or [int64]$ProcessId -le 0) {
                throw ($PidField + ' contains a non-positive or non-integral PID.')
            }
        }
    }
    if (-not (Test-PrivateDesktopIntegralValue $Result.observed_distinct_process_id_count) -or
        [int64]$Result.observed_distinct_process_id_count -lt 0) {
        throw 'observed_distinct_process_id_count must be a nonnegative diagnostic integer.'
    }
    if ($null -ne $Result.job_total_processes -and
        (-not (Test-PrivateDesktopIntegralValue $Result.job_total_processes) -or
         [int64]$Result.job_total_processes -lt 0)) {
        throw 'job_total_processes must be null or a nonnegative diagnostic integer.'
    }
    if ($Result.process_diagnostic_errors -isnot [System.Array]) {
        throw 'process_diagnostic_errors must be present as an array.'
    }
    foreach ($DiagnosticError in @($Result.process_diagnostic_errors)) {
        if ($DiagnosticError -isnot [string]) {
            throw 'process_diagnostic_errors contains a non-string value.'
        }
    }

    $Invariant = [Globalization.CultureInfo]::InvariantCulture
    $Armed = [DateTimeOffset]::Parse([string]$Result.monitor_armed_utc, $Invariant)
    $Created = [DateTimeOffset]::Parse([string]$Result.process_created_utc, $Invariant)
    $Resumed = [DateTimeOffset]::Parse([string]$Result.resumed_utc, $Invariant)
    if ($Armed -gt $Created -or $Created -gt $Resumed) {
        throw 'Private desktop timestamps must satisfy armed <= created <= resumed.'
    }
}

function Import-PrivateDesktopRunner {
    [CmdletBinding()]
    param([Parameter(Mandatory = $true)][string]$SourcePath)

    if ('CourtOfShadows.Headless.PrivateDesktopRunner' -as [type]) { return }
    $ResolvedSource = (Resolve-Path -LiteralPath $SourcePath).Path
    Add-Type -Path $ResolvedSource -ReferencedAssemblies @(
        'System.dll',
        'System.Core.dll',
        'System.Runtime.Serialization.dll',
        'System.Xml.dll'
    ) -ErrorAction Stop
}

function Invoke-PrivateDesktopProcess {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)][string]$FilePath,
        [Parameter()][AllowEmptyCollection()][string[]]$ArgumentList = @(),
        [Parameter(Mandatory = $true)][string]$WorkingDirectory,
        [Parameter()][hashtable]$EnvironmentOverrides = @{},
        [Parameter(Mandatory = $true)][ValidateRange(1, 86400)][int]$TimeoutSeconds,
        [Parameter(Mandatory = $true)][string]$EvidenceDirectory,
        [Parameter()][string]$RunnerSource = (Join-Path $PSScriptRoot 'PrivateDesktopRunner.cs')
    )

    $ResolvedExe = (Resolve-Path -LiteralPath $FilePath).Path
    $ResolvedWorkingDirectory = (Resolve-Path -LiteralPath $WorkingDirectory).Path
    if (Test-Path -LiteralPath $EvidenceDirectory) {
        throw "EvidenceDirectory already exists; refusing to reuse or overwrite evidence: $EvidenceDirectory"
    }
    $EvidenceFullPath = [IO.Path]::GetFullPath($EvidenceDirectory)
    [IO.Directory]::CreateDirectory($EvidenceFullPath) | Out-Null

    $RequestPath = Join-Path $EvidenceFullPath 'request.json'
    $StdoutPath = Join-Path $EvidenceFullPath 'stdout.txt'
    $StderrPath = Join-Path $EvidenceFullPath 'stderr.txt'
    $ResultPath = Join-Path $EvidenceFullPath 'result.json'

    $EnvironmentRows = @(
        foreach ($Key in @($EnvironmentOverrides.Keys | Sort-Object { [string]$_ })) {
            $Name = [string]$Key
            if ([string]::IsNullOrEmpty($Name) -or $Name.Contains("`0") -or $Name.Contains('=')) {
                throw "Invalid environment variable name: $Name"
            }
            $RawValue = $EnvironmentOverrides[$Key]
            if ($null -eq $RawValue) {
                [ordered]@{ name = $Name; value = $null }
            } else {
                $Value = [string]$RawValue
                if ($Value.Contains("`0")) { throw "Environment value contains NUL: $Name" }
                [ordered]@{ name = $Name; value = $Value }
            }
        }
    )

    $Request = [ordered]@{
        schema_version = 1
        executable = $ResolvedExe
        arguments = @($ArgumentList)
        working_directory = $ResolvedWorkingDirectory
        environment_overrides = $EnvironmentRows
        timeout_milliseconds = [int]($TimeoutSeconds * 1000)
        stdout_path = $StdoutPath
        stderr_path = $StderrPath
        result_path = $ResultPath
    }
    $Json = ConvertTo-Json -InputObject $Request -Depth 6 -Compress
    Write-NewUtf8File -LiteralPath $RequestPath -Text $Json

    $ResolvedRunnerSource = (Resolve-Path -LiteralPath $RunnerSource).Path
    $PowerShellHost = (Get-Command powershell.exe -ErrorAction Stop).Source
    $HostArguments = @(
        '-NoLogo', '-NoProfile', '-NonInteractive', '-ExecutionPolicy', 'Bypass',
        '-File', $PrivateDesktopWrapperScriptPath,
        '-PrivateDesktopInternalHostMode',
        '-PrivateDesktopInternalRequestPath', $RequestPath,
        '-PrivateDesktopInternalRunnerSource', $ResolvedRunnerSource
    )
    $StartInfo = New-Object System.Diagnostics.ProcessStartInfo
    $StartInfo.FileName = $PowerShellHost
    $StartInfo.Arguments = (@($HostArguments | ForEach-Object {
        ConvertTo-PrivateDesktopHostArgument -Value ([string]$_)
    }) -join ' ')
    $StartInfo.WorkingDirectory = $EvidenceFullPath
    $StartInfo.UseShellExecute = $false
    $StartInfo.CreateNoWindow = $true

    $HostProcess = New-Object System.Diagnostics.Process
    $HostProcess.StartInfo = $StartInfo
    $HostWaitMilliseconds = [int](($TimeoutSeconds * 1000) + 30000)
    $ActualHostExitCode = $null
    $HostStarted = $false
    $HostExitAndCodeProven = $false
    $HostObservationError = $null
    $HostFailClosedTeardown = $null
    try {
        try {
            $HostStarted = $HostProcess.Start()
            if (-not $HostStarted) {
                throw 'Dedicated PowerShell helper host did not report a successful start.'
            }
            if (-not $HostProcess.WaitForExit($HostWaitMilliseconds)) {
                throw 'Dedicated PowerShell helper host exceeded the bounded wait.'
            }
            if (-not $HostProcess.HasExited) {
                throw 'Dedicated PowerShell helper host completed its wait without proving exit.'
            }
            $ActualHostExitCode = $HostProcess.ExitCode
            $HostExitAndCodeProven = $true
        } catch {
            $HostObservationError = $_.Exception.Message
        } finally {
            if ($HostStarted -and -not $HostExitAndCodeProven) {
                $HostFailClosedTeardown = Invoke-PrivateDesktopHostFailClosedTeardown -Process $HostProcess
            }
        }
    } finally {
        $HostProcess.Dispose()
    }

    if (-not $HostExitAndCodeProven) {
        if (-not $HostStarted) {
            throw "NEEDS_CONTEXT: dedicated PowerShell helper host start was not proven; no retry is permitted. Observation detail: $HostObservationError"
        }
        if ($null -eq $HostFailClosedTeardown) {
            throw "NEEDS_CONTEXT: dedicated PowerShell helper host exit observation failed and fail-closed teardown produced no proof; no retry is permitted. Observation detail: $HostObservationError"
        }
        throw ("NEEDS_CONTEXT: dedicated PowerShell helper host exit observation failed; no retry is permitted. " +
            "Observation detail: $HostObservationError; " +
            "fail_closed_kill_issued=$($HostFailClosedTeardown.kill_issued); " +
            "exit_proven_after_teardown=$($HostFailClosedTeardown.exit_proven); " +
            "kill_error=$($HostFailClosedTeardown.kill_error); " +
            "exit_proof_error=$($HostFailClosedTeardown.exit_proof_error)")
    }

    if (-not (Test-Path -LiteralPath $ResultPath -PathType Leaf)) {
        throw 'NEEDS_CONTEXT: dedicated PowerShell helper host exited without result.json; no retry is permitted.'
    }
    $StrictUtf8 = New-Object System.Text.UTF8Encoding($false, $true)
    try {
        $ResultText = [IO.File]::ReadAllText($ResultPath, $StrictUtf8)
        $Result = $ResultText | ConvertFrom-Json -ErrorAction Stop
        Assert-PrivateDesktopResultDocument -Result $Result
    } catch {
        throw "NEEDS_CONTEXT: result.json was missing, truncated, non-UTF-8, or structurally invalid: $($_.Exception.Message)"
    }
    try {
        $SafeToReuse = Test-PrivateDesktopParentHostResult -Result $Result -ActualHostExitCode $ActualHostExitCode
    } catch {
        throw "NEEDS_CONTEXT: actual helper-host exit and persisted result validation failed: $($_.Exception.Message)"
    }
    if (-not $SafeToReuse) {
        throw 'NEEDS_CONTEXT: helper host required catastrophic termination; the result is preserved but cannot be treated as a reusable safety PASS.'
    }
    return $Result
}

if ($PrivateDesktopInternalHostMode) {
    try {
        if ([string]::IsNullOrWhiteSpace($PrivateDesktopInternalRequestPath) -or
            [string]::IsNullOrWhiteSpace($PrivateDesktopInternalRunnerSource)) {
            throw 'PrivateDesktopInternalHostMode requires internal request and runner paths.'
        }
        Import-PrivateDesktopRunner -SourcePath $PrivateDesktopInternalRunnerSource
        $InternalHelperExitCode = [CourtOfShadows.Headless.PrivateDesktopRunner]::RunRequestFile($PrivateDesktopInternalRequestPath)
    } catch {
        [Console]::Error.WriteLine($_.Exception.ToString())
        [Environment]::Exit(22)
    }
    [Environment]::Exit($InternalHelperExitCode)
}
```

## Appendix C — `Test-PrivateDesktopRunner.ps1`

Exact committed helper payload: **53,188 bytes**; **SHA-256 `20198B669F70E51E51F71BD01E6D06D1949D300F43CE9A94FB0190A47D781A15`**. The fenced body below is the complete UTF-8, no-BOM source and includes its final LF.

```powershell
[CmdletBinding()]
param(
    [switch]$IncludeVisibleWindowTest,
    [switch]$ContractOnly
)

Set-StrictMode -Version 2.0
$ErrorActionPreference = 'Stop'
$PrivateDesktopSelfTestScriptPath = $PSCommandPath
. (Join-Path $PSScriptRoot 'Invoke-PrivateDesktopProcess.ps1')
$SelfTestSource = [IO.File]::ReadAllText($PrivateDesktopSelfTestScriptPath)
if ([regex]::IsMatch($SelfTestSource, '[^\x00-\x7F]')) {
    throw 'Test-PrivateDesktopRunner.ps1 must remain ASCII so Windows PowerShell 5.1 cannot misdecode literals.'
}

function Assert-Equal($Actual, $Expected, [string]$Context) {
    if ($Actual -cne $Expected) { throw "$Context expected <$Expected>, actual <$Actual>." }
}

function Copy-ContractPayload($Payload) {
    return ($Payload | ConvertTo-Json -Depth 8 -Compress | ConvertFrom-Json -ErrorAction Stop)
}

function Assert-ContractRejected($Payload, [string]$Context, [scriptblock]$Mutate) {
    $Candidate = Copy-ContractPayload $Payload
    & $Mutate $Candidate
    $Rejected = $false
    try {
        Assert-PrivateDesktopSafetyEnvelope -Result $Candidate
    } catch {
        $Rejected = $true
    }
    Assert-Equal $Rejected $true $Context
}

function Assert-ParentHostContractRejected($Payload, [int]$ActualHostExitCode, [string]$Context, [scriptblock]$Mutate) {
    $Candidate = Copy-ContractPayload $Payload
    & $Mutate $Candidate
    $Rejected = $false
    try {
        Test-PrivateDesktopParentHostResult -Result $Candidate -ActualHostExitCode $ActualHostExitCode | Out-Null
    } catch {
        $Rejected = $true
    }
    Assert-Equal $Rejected $true $Context
}

function New-ValidContractPayload {
    $ProcessIds = @(1..63)
    return [pscustomobject][ordered]@{
        schema_version = 2
        classification = 'COMPLETED'
        detail = 'Synthetic contract-only result.'
        started = $true
        root_pid = 1
        root_exit_code = 7
        timed_out = $false
        job_drained = $true
        desktop_name = 'WinSta0\CosHeadless_contract_only'
        process_ids = $ProcessIds
        new_process_ids = $ProcessIds
        active_snapshot_process_ids = @()
        job_total_processes = 66
        observed_distinct_process_id_count = 63
        process_id_accounting_kind = 'diagnostic_distinct_pid'
        process_diagnostic_errors = @()
        private_desktop_initially_empty = $true
        monitor_armed_before_create = $true
        monitor_armed_before_resume = $true
        monitor_armed_utc = '2026-08-11T00:00:01.0000000Z'
        process_created_utc = '2026-08-11T00:00:02.0000000Z'
        resumed_utc = '2026-08-11T00:00:03.0000000Z'
        root_assigned_to_job_before_resume = $true
        job_kill_on_close_verified = $true
        job_breakaway_forbidden = $true
        job_handle_non_inheritable = $true
        job_active_processes_final = 0
        monitor_completed_after_job_drain = $true
        host_termination_required = $false
        cleanup_complete = $true
        cleanup_errors = @()
        visible_windows = @()
        started_utc = '2026-08-11T00:00:00.0000000Z'
        finished_utc = '2026-08-11T00:00:04.0000000Z'
        elapsed_milliseconds = 4000
        stdout_path = 'C:\contract-only\stdout.txt'
        stderr_path = 'C:\contract-only\stderr.txt'
        helper_exit_code = 0
    }
}

function Assert-PrivateDesktopRunnerSourceContract {
    param([Parameter(Mandatory = $true)][string]$SourcePath)

    $Source = [IO.File]::ReadAllText($SourcePath)
    foreach ($Banned in @('SwitchDesktop(', 'OpenInputDesktop(', 'SendInput(', 'mouse_event(', 'keybd_event(', 'SetForegroundWindow(')) {
        if ($Source.Contains($Banned)) { throw "Banned desktop/input API appears in helper source: $Banned" }
    }
    if (-not $Source.Contains('SetThreadDesktop(')) { throw 'Dedicated private-desktop watcher does not bind its thread desktop.' }
    if (-not $Source.Contains('CREATE_NO_WINDOW')) { throw 'CREATE_NO_WINDOW is absent from the helper.' }
    if (-not $Source.Contains('private sealed class PrivateDesktopWatcher')) { throw 'Dedicated private-desktop watcher type is absent.' }
    if ($Source.Contains('ReadDesktopName(')) { throw 'Window classification still relies on a separately queried desktop-name field.' }
    if ($Source.Contains('process_coverage_complete') -or $Source.Contains('ProcessCoverageComplete')) {
        throw 'Legacy process coverage is still present in the C# result contract.'
    }
    if ([regex]::Matches($Source, 'SchemaVersion = 2').Count -ne 2 -or $Source.Contains('SchemaVersion = 1')) {
        throw 'C# result constructors do not exclusively emit schema v2.'
    }
    if ([regex]::Matches($Source, '!SetThreadDesktop\(desktopHandle\)').Count -ne 1 -or
        [regex]::Matches($Source, 'extern bool SetThreadDesktop\(IntPtr desktop\)').Count -ne 1) {
        throw 'SetThreadDesktop must have exactly one watcher call and one P/Invoke declaration.'
    }

    $WatcherBind = $Source.IndexOf('if (!SetThreadDesktop(desktopHandle))', [StringComparison]::Ordinal)
    $QueueReady = $Source.IndexOf('PeekMessageW(out queueProbe, IntPtr.Zero, 0, 0, PM_NOREMOVE);', $WatcherBind, [StringComparison]::Ordinal)
    $WatcherHook = $Source.IndexOf('createHook = SetWinEventHook(', $WatcherBind, [StringComparison]::Ordinal)
    $WatcherArm = $Source.IndexOf('armed.Set();', $WatcherHook, [StringComparison]::Ordinal)
    if ($WatcherBind -lt 0 -or $QueueReady -le $WatcherBind -or $WatcherHook -le $QueueReady -or $WatcherArm -le $WatcherHook) {
        throw 'Watcher bind/queue/hook/arm ordering is not explicit.'
    }

    $SetJobLimit = $Source.IndexOf('ConfigureKillOnClose(job);', [StringComparison]::Ordinal)
    $QueryJobLimit = $Source.IndexOf('VerifyKillOnCloseAndNoBreakaway(job);', $SetJobLimit, [StringComparison]::Ordinal)
    $RecordKillOnClose = $Source.IndexOf('result.JobKillOnCloseVerified = true;', $QueryJobLimit, [StringComparison]::Ordinal)
    $RecordBreakaway = $Source.IndexOf('result.JobBreakawayForbidden = true;', $RecordKillOnClose, [StringComparison]::Ordinal)
    $RecordNonInheritable = $Source.IndexOf('result.JobHandleNonInheritable = VerifyHandleNonInheritable(job);', $RecordBreakaway, [StringComparison]::Ordinal)
    $WaitForArm = $Source.IndexOf('watcher.StartAndWaitUntilArmed(5000);', $RecordNonInheritable, [StringComparison]::Ordinal)
    $InitialEmptyProof = $Source.IndexOf('result.PrivateDesktopInitiallyEmpty = watcher.InitiallyEmpty;', $WaitForArm, [StringComparison]::Ordinal)
    $JobListAttribute = $Source.IndexOf('new UIntPtr(PROC_THREAD_ATTRIBUTE_JOB_LIST)', $InitialEmptyProof, [StringComparison]::Ordinal)
    $CreateSuspended = $Source.IndexOf('if (!CreateProcessW(', $JobListAttribute, [StringComparison]::Ordinal)
    $CreatedTimestamp = $Source.IndexOf('DateTime processCreatedUtc = DateTime.UtcNow;', $CreateSuspended, [StringComparison]::Ordinal)
    $RecordCreated = $Source.IndexOf('result.ProcessCreatedUtc = FormatUtc(processCreatedUtc);', $CreatedTimestamp, [StringComparison]::Ordinal)
    $RecordArmedBeforeCreate = $Source.IndexOf('result.MonitorArmedBeforeCreate = watcher.ArmedUtc <= processCreatedUtc;', $RecordCreated, [StringComparison]::Ordinal)
    $VerifyRoot = $Source.IndexOf('if (!IsProcessInJob(processInfo.hProcess, job, out rootInJob))', $RecordArmedBeforeCreate, [StringComparison]::Ordinal)
    $RecordAssigned = $Source.IndexOf('result.RootAssignedToJobBeforeResume = true;', $VerifyRoot, [StringComparison]::Ordinal)
    $ResumeSuspended = $Source.IndexOf('uint resumeResult = ResumeThread(', $RecordAssigned, [StringComparison]::Ordinal)
    $ResumedTimestamp = $Source.IndexOf('DateTime resumedUtc = DateTime.UtcNow;', $ResumeSuspended, [StringComparison]::Ordinal)
    $RecordResumed = $Source.IndexOf('result.ResumedUtc = FormatUtc(resumedUtc);', $ResumedTimestamp, [StringComparison]::Ordinal)
    $RecordArmedBeforeResume = $Source.IndexOf('result.MonitorArmedBeforeResume = watcher.ArmedUtc <= resumedUtc;', $RecordResumed, [StringComparison]::Ordinal)
    if ($SetJobLimit -lt 0 -or $QueryJobLimit -le $SetJobLimit -or
        $RecordKillOnClose -le $QueryJobLimit -or $RecordBreakaway -le $RecordKillOnClose -or
        $RecordNonInheritable -le $RecordBreakaway -or $WaitForArm -le $RecordNonInheritable -or
        $InitialEmptyProof -le $WaitForArm -or $JobListAttribute -le $InitialEmptyProof -or
        $CreateSuspended -le $JobListAttribute -or $CreatedTimestamp -le $CreateSuspended -or
        $RecordCreated -le $CreatedTimestamp -or $RecordArmedBeforeCreate -le $RecordCreated -or
        $VerifyRoot -le $RecordArmedBeforeCreate -or
        $RecordAssigned -le $VerifyRoot -or $ResumeSuspended -le $RecordAssigned -or
        $ResumedTimestamp -le $ResumeSuspended -or $RecordResumed -le $ResumedTimestamp -or
        $RecordArmedBeforeResume -le $RecordResumed) {
        throw 'Private-desktop v2 hard-field assignment order is not explicit.'
    }
    if ($Source.Contains('DuplicateHandle(') -or $Source.Contains('AssignProcessToJobObject(') -or
        $Source.Contains('unassigned root') -or
        -not $Source.Contains('private const uint PROC_THREAD_ATTRIBUTE_JOB_LIST = 0x0002000D;') -or
        -not $Source.Contains('InitializeProcThreadAttributeList(IntPtr.Zero, 2, 0, ref attributeBytes);') -or
        -not $Source.Contains('InitializeProcThreadAttributeList(attributeList, 2, 0, ref attributeBytes)') -or
        -not $Source.Contains('Marshal.WriteIntPtr(jobListMemory, job);') -or
        -not $Source.Contains('job = CreateJobObjectW(IntPtr.Zero, null);') -or
        -not $Source.Contains('IntPtr[] inheritedHandles = new IntPtr[] { stdinHandle, stdoutHandle, stderrHandle };') -or
        -not $Source.Contains('if (!GetHandleInformation(handle, out flags))') -or
        -not $Source.Contains('if ((flags & HANDLE_FLAG_INHERIT) != 0)')) {
        throw 'Atomic Job-list assignment or unique non-inheritable Job-handle ownership is not proven.'
    }

    if ($Source.Contains('TryIsProcessInJobAtObservation') -or $Source.Contains('InJobAtObservation') -or
        $Source.Contains('Reconcile(HashSet<int>') -or $Source.Contains('pid == 0 && !privateShowProof') -or
        $Source.Contains('GetProcessIdForEventThread') -or $Source.Contains('OpenThread(') -or
        $Source.Contains('GetProcessIdOfThread')) {
        throw 'Visible-window acceptance still contains PID/Job filtering.'
    }
    $ReconcileStart = $Source.IndexOf('public void Reconcile()', [StringComparison]::Ordinal)
    $ReconcileEnd = $Source.IndexOf('public WindowEvidence[] SnapshotWindows()', $ReconcileStart, [StringComparison]::Ordinal)
    $CandidateStart = $Source.IndexOf('WindowCandidate item = candidates[i];', $ReconcileStart, [StringComparison]::Ordinal)
    $EvidenceKey = $Source.IndexOf('string key = item.Pid.ToString(', $CandidateStart, [StringComparison]::Ordinal)
    if ($ReconcileStart -lt 0 -or $ReconcileEnd -le $ReconcileStart -or
        $CandidateStart -le $ReconcileStart -or $EvidenceKey -le $CandidateStart) {
        throw 'PID-independent visible-window reconciliation is absent.'
    }
    $PreKeyReconcile = $Source.Substring($CandidateStart, $EvidenceKey - $CandidateStart)
    if ($PreKeyReconcile.Contains('continue') -or $PreKeyReconcile.Contains('ownedPid') -or
        $PreKeyReconcile.Contains('InJob')) {
        throw 'A private-desktop visible-window candidate can still be filtered before acceptance.'
    }
    if (-not $Source.Contains('if (!windowAlive || !IsWindowVisible(hwnd) || GetAncestor(hwnd, GA_ROOT) != hwnd) return;') -or
        -not $Source.Contains('IntPtr root = GetAncestor(hwnd, GA_ROOT);') -or
        -not $Source.Contains('if (root != IntPtr.Zero && root != hwnd) return;') -or
        $Source.Contains('else if (windowAlive && GetAncestor(hwnd, GA_ROOT) != hwnd)') -or
        -not $Source.Contains('candidate.PrivateShowProof = privateShowProof;') -or
        -not $Source.Contains('item.PrivateShowProof')) {
        throw 'CREATE/enumeration visibility or fail-closed transient SHOW evidence semantics drifted.'
    }

    $AccountingStart = $Source.IndexOf('private static void FinalizeProcessAccounting(', [StringComparison]::Ordinal)
    $AccountingEnd = $Source.IndexOf('private sealed class PrivateDesktopWatcher', $AccountingStart, [StringComparison]::Ordinal)
    if ($AccountingStart -lt 0 -or $AccountingEnd -le $AccountingStart) {
        throw 'Diagnostic process-accounting method is absent.'
    }
    $AccountingBody = $Source.Substring($AccountingStart, $AccountingEnd - $AccountingStart)
    if ($AccountingBody.Contains('Classification') -or $AccountingBody.Contains('Detail') -or
        $AccountingBody.Contains('CleanupErrors') -or $AccountingBody.Contains('cleanupErrors') -or
        $AccountingBody.Contains('ProcessCoverageComplete') -or
        -not $AccountingBody.Contains('result.JobTotalProcesses = total;') -or
        -not $AccountingBody.Contains('result.ObservedDistinctProcessIdCount = observed;')) {
        throw 'PID/accounting diagnostics can still classify the result or are not recorded.'
    }
    $DiagnosticBoundaryStart = $Source.IndexOf('private static void TryPumpJobMessages(', [StringComparison]::Ordinal)
    $DiagnosticBoundaryEnd = $Source.IndexOf('private static uint QueryActiveProcessCount(', $DiagnosticBoundaryStart, [StringComparison]::Ordinal)
    $DiagnosticBoundary = $Source.Substring($DiagnosticBoundaryStart, $DiagnosticBoundaryEnd - $DiagnosticBoundaryStart)
    if ($DiagnosticBoundaryStart -lt 0 -or $DiagnosticBoundaryEnd -le $DiagnosticBoundaryStart -or
        $DiagnosticBoundary.Contains('Classification') -or $DiagnosticBoundary.Contains('Detail') -or
        $DiagnosticBoundary.Contains('CleanupErrors') -or $DiagnosticBoundary.Contains('cleanupErrors')) {
        throw 'Best-effort process diagnostic collection can still alter outcome or cleanup state.'
    }
    $DiagnosticRecordStart = $Source.IndexOf('private static void RecordProcessDiagnosticError(', [StringComparison]::Ordinal)
    $DiagnosticRecordEnd = $Source.IndexOf('private static void PumpJobMessages(', $DiagnosticRecordStart, [StringComparison]::Ordinal)
    $DiagnosticRecordBody = $Source.Substring($DiagnosticRecordStart, $DiagnosticRecordEnd - $DiagnosticRecordStart)
    if ($DiagnosticRecordStart -lt 0 -or $DiagnosticRecordEnd -le $DiagnosticRecordStart -or
        -not $Source.Contains('private const int MAX_PROCESS_DIAGNOSTIC_ERRORS = 8;') -or
        -not $Source.Contains('private const int MAX_PROCESS_DIAGNOSTIC_ERROR_CHARACTERS = 2048;') -or
        -not $DiagnosticRecordBody.Contains('diagnosticErrors.Contains(message)') -or
        -not $DiagnosticRecordBody.Contains('diagnosticErrors.Count >= MAX_PROCESS_DIAGNOSTIC_ERRORS') -or
        -not $DiagnosticRecordBody.Contains('message.Substring(0, MAX_PROCESS_DIAGNOSTIC_ERROR_CHARACTERS)')) {
        throw 'Process diagnostic errors are not explicitly deduplicated and bounded by count and characters.'
    }

    $ExecuteStart = $Source.IndexOf('private static RunResult Execute(', [StringComparison]::Ordinal)
    $ExecuteEnd = $Source.IndexOf('private static void ValidateRequest(', $ExecuteStart, [StringComparison]::Ordinal)
    $ExecuteBody = $Source.Substring($ExecuteStart, $ExecuteEnd - $ExecuteStart)
    if ([regex]::IsMatch($ExecuteBody, '(?m)^\s*PumpJobMessages\(') -or
        [regex]::IsMatch($ExecuteBody, '(?m)^\s*RefreshOwnedPidsFromJob\(') -or
        [regex]::IsMatch($ExecuteBody, '(?m)^\s*FinalizeProcessAccounting\(') -or
        -not $ExecuteBody.Contains('result.ProcessDiagnosticErrors = processDiagnosticErrors.ToArray();')) {
        throw 'Process diagnostics can still escape their best-effort recording boundary.'
    }

    $DrainProven = $Source.IndexOf('bool drainProven = result.JobDrained && result.JobActiveProcessesFinal.HasValue &&', [StringComparison]::Ordinal)
    $DrainFailure = $Source.IndexOf('if (job != IntPtr.Zero && !drainProven)', $DrainProven, [StringComparison]::Ordinal)
    $DrainHostTermination = $Source.IndexOf('result.HostTerminationRequired = true;', $DrainFailure, [StringComparison]::Ordinal)
    $WatcherDrainGate = $Source.IndexOf('if (watcher != null && drainProven)', $DrainHostTermination, [StringComparison]::Ordinal)
    $WatcherStop = $Source.IndexOf('watcher.StopAndJoin(5000);', $WatcherDrainGate, [StringComparison]::Ordinal)
    $JoinHostTermination = $Source.IndexOf('result.HostTerminationRequired = true;', $WatcherStop, [StringComparison]::Ordinal)
    $MonitorCondition = $Source.IndexOf('if (drainProven && watcherJoinSucceeded && watcherCompletionSucceeded)', $WatcherStop, [StringComparison]::Ordinal)
    $MonitorComplete = $Source.IndexOf('result.MonitorCompletedAfterJobDrain = true;', $MonitorCondition, [StringComparison]::Ordinal)
    $ReusableCleanupGate = $Source.IndexOf('if (!result.HostTerminationRequired)', $MonitorComplete, [StringComparison]::Ordinal)
    $CloseJob = $Source.IndexOf('job = CloseKernelHandleForCleanup(job, "job", cleanupErrors);', $ReusableCleanupGate, [StringComparison]::Ordinal)
    $CloseCompletionPort = $Source.IndexOf('completionPort = CloseKernelHandleForCleanup(completionPort, "completion port", cleanupErrors);', $CloseJob, [StringComparison]::Ordinal)
    $ClosePrivateDesktop = $Source.IndexOf('if (!CloseDesktop(desktop))', $CloseCompletionPort, [StringComparison]::Ordinal)
    if ($DrainProven -lt 0 -or $DrainFailure -le $DrainProven -or
        $DrainHostTermination -le $DrainFailure -or $WatcherDrainGate -le $DrainHostTermination -or
        $WatcherStop -le $WatcherDrainGate -or $JoinHostTermination -le $WatcherStop -or
        $MonitorCondition -le $WatcherStop -or $MonitorComplete -le $MonitorCondition -or
        $ReusableCleanupGate -le $MonitorComplete -or $CloseJob -le $ReusableCleanupGate -or
        $CloseCompletionPort -le $CloseJob -or $ClosePrivateDesktop -le $CloseCompletionPort) {
        throw 'Catastrophic host termination and drain-gated watcher shutdown ordering is not explicit.'
    }
    $DrainFailureBody = $Source.Substring($DrainFailure, $WatcherDrainGate - $DrainFailure)
    if ($DrainFailureBody.Contains('StopAndJoin(') -or
        -not $DrainFailureBody.Contains('result.HostTerminationRequired = true;')) {
        throw 'Unproven Job drain can still stop the watcher or avoid catastrophic host termination.'
    }
    if (-not $Source.Contains('watcher.DisposeEventsAfterJoin();') -or
        -not $Source.Contains('if (thread != null && thread.IsAlive)')) {
        throw 'Watcher events are not disposed only after a proven normal join.'
    }

    $RunRequestStart = $Source.IndexOf('public static int RunRequestFile(', [StringComparison]::Ordinal)
    $RunRequestEnd = $Source.IndexOf('public static string QuoteWindowsArgument(', $RunRequestStart, [StringComparison]::Ordinal)
    $RunRequestBody = $Source.Substring($RunRequestStart, $RunRequestEnd - $RunRequestStart)
    if ($RunRequestStart -lt 0 -or $RunRequestEnd -le $RunRequestStart -or
        -not $Source.Contains('[DataMember(Name = "helper_exit_code", Order = 36)]') -or
        -not $RunRequestBody.Contains('result.HelperExitCode = helperExitCode;') -or
        -not $RunRequestBody.Contains('if (result.HostTerminationRequired)') -or
        -not $RunRequestBody.Contains('PersistResultAndTerminateHost(resultPath, result, helperExitCode);')) {
        throw 'RunRequestFile does not persist the mapped helper exit or route catastrophic results to host termination.'
    }
    $PersistHostStart = $Source.IndexOf('private static void PersistResultAndTerminateHost(', [StringComparison]::Ordinal)
    $PersistHostEnd = $Source.IndexOf('private static int MapResultExitCode(', $PersistHostStart, [StringComparison]::Ordinal)
    $PersistHostBody = $Source.Substring($PersistHostStart, $PersistHostEnd - $PersistHostStart)
    $PersistWrite = $PersistHostBody.IndexOf('WriteJsonCreateNew(resultPath, result);', [StringComparison]::Ordinal)
    $TerminateHost = $PersistHostBody.IndexOf('Environment.Exit(helperExitCode);', [StringComparison]::Ordinal)
    if ($PersistHostStart -lt 0 -or $PersistHostEnd -le $PersistHostStart -or
        $PersistWrite -lt 0 -or $TerminateHost -le $PersistWrite -or
        -not $PersistHostBody.Contains('finally')) {
        throw 'Catastrophic result is not persisted before unconditional dedicated-host termination.'
    }
    $MapExitStart = $PersistHostEnd
    $MapExitEnd = $Source.IndexOf('public static string QuoteWindowsArgument(', $MapExitStart, [StringComparison]::Ordinal)
    $MapExitBody = $Source.Substring($MapExitStart, $MapExitEnd - $MapExitStart)
    if ($MapExitEnd -le $MapExitStart -or
        -not $MapExitBody.Contains('"COMPLETED", StringComparison.Ordinal)) return 0;') -or
        -not $MapExitBody.Contains('"NEEDS_CONTEXT", StringComparison.Ordinal)) return 20;') -or
        -not $MapExitBody.Contains('"TIMEOUT", StringComparison.Ordinal)) return 21;') -or
        -not $MapExitBody.Contains('"LAUNCH_ERROR", StringComparison.Ordinal)) return 22;') -or
        -not $MapExitBody.Contains('throw new InvalidOperationException("Unknown helper classification: "')) {
        throw 'C# helper classification-to-host-exit mapping is not exact and fail-closed.'
    }
    $SnapshotStart = $Source.IndexOf('public WindowEvidence[] SnapshotWindows()', $WatcherStop, [StringComparison]::Ordinal)
    if ($SnapshotStart -lt 0) {
        $SnapshotStart = $Source.IndexOf('public WindowEvidence[] SnapshotWindows()', [StringComparison]::Ordinal)
    }
    $SnapshotEnd = $Source.IndexOf('private void ThreadMain()', $SnapshotStart, [StringComparison]::Ordinal)
    $SnapshotBody = $Source.Substring($SnapshotStart, $SnapshotEnd - $SnapshotStart)
    if ($SnapshotStart -lt 0 -or $SnapshotEnd -le $SnapshotStart -or
        -not $SnapshotBody.Contains('ReconcilePendingCandidates();')) {
        throw 'Pending visible-window candidates can be lost when watcher shutdown reports failure.'
    }
    $VisiblePrecedence = $Source.IndexOf('bool visibleWindowObserved = result.VisibleWindows != null && result.VisibleWindows.Length != 0;', [StringComparison]::Ordinal)
    $NeedsContextFinal = $Source.IndexOf('result.Classification = "NEEDS_CONTEXT";', $VisiblePrecedence, [StringComparison]::Ordinal)
    $NoWindowLaunchError = $Source.IndexOf('result.Classification = "LAUNCH_ERROR";', $NeedsContextFinal, [StringComparison]::Ordinal)
    if ($VisiblePrecedence -lt 0 -or $NeedsContextFinal -le $VisiblePrecedence -or
        $NoWindowLaunchError -le $NeedsContextFinal) {
        throw 'Visible-window NEEDS_CONTEXT precedence over cleanup failure is not explicit.'
    }
    $CatastrophicResultGate = $Source.IndexOf('if (result.HostTerminationRequired)', $NoWindowLaunchError, [StringComparison]::Ordinal)
    $CatastrophicResultEnd = $Source.IndexOf('stopwatch.Stop();', $CatastrophicResultGate, [StringComparison]::Ordinal)
    $CatastrophicResultBody = $Source.Substring($CatastrophicResultGate, $CatastrophicResultEnd - $CatastrophicResultGate)
    if ($CatastrophicResultGate -lt 0 -or $CatastrophicResultEnd -le $CatastrophicResultGate -or
        -not $CatastrophicResultBody.Contains('result.MonitorCompletedAfterJobDrain = false;') -or
        -not $CatastrophicResultBody.Contains('result.CleanupComplete = false;') -or
        -not $CatastrophicResultBody.Contains('result.Classification = "NEEDS_CONTEXT";') -or
        -not $CatastrophicResultBody.Contains('Previous classification=') -or
        $CatastrophicResultBody.Contains('if (String.Equals(result.Classification, "COMPLETED"')) {
        throw 'Catastrophic results can still claim reusable cleanup/monitoring or a weaker conditional classification.'
    }
    if (-not $Source.Contains('bool attributeListInitialized = false;') -or
        -not $Source.Contains('if (attributeListInitialized) DeleteProcThreadAttributeList(attributeList);')) {
        throw 'Attribute-list initialization is not guarded during cleanup.'
    }

    $ExitCaptureStart = $Source.IndexOf('private static void TryCaptureRootExitCode(', [StringComparison]::Ordinal)
    $ExitCaptureEnd = $Source.IndexOf('private static void ValidateRequest(', $ExitCaptureStart, [StringComparison]::Ordinal)
    $ExitCaptureBody = $Source.Substring($ExitCaptureStart, $ExitCaptureEnd - $ExitCaptureStart)
    if ($ExitCaptureStart -lt 0 -or $ExitCaptureEnd -le $ExitCaptureStart -or
        -not $Source.Contains('bool rootExitProven = false;') -or
        -not $Source.Contains('if (rootWait == WAIT_OBJECT_0) rootExitProven = true;') -or
        -not $Source.Contains('if (drainedRootWait == WAIT_OBJECT_0) rootExitProven = true;') -or
        -not $ExitCaptureBody.Contains('if (exitCode == STILL_ACTIVE && !rootExitProven) return;') -or
        -not $ExitCaptureBody.Contains('result.RootExitCode = unchecked((int)exitCode);') -or
        $Source.Contains('exitCode != STILL_ACTIVE') -or
        $Source.Contains('finalRootExitCode != STILL_ACTIVE')) {
        throw 'A signaled root process can still lose the legitimate exit code 259.'
    }
}

$Payload = New-ValidContractPayload
Assert-Equal (ConvertTo-PrivateDesktopHostArgument -Value '') '""' 'dedicated host empty argument quoting'
Assert-Equal (ConvertTo-PrivateDesktopHostArgument -Value 'plain') 'plain' 'dedicated host plain argument quoting'
Assert-Equal (ConvertTo-PrivateDesktopHostArgument -Value 'white space') '"white space"' 'dedicated host whitespace argument quoting'
Assert-Equal (ConvertTo-PrivateDesktopHostArgument -Value 'quote"inside') '"quote\"inside"' 'dedicated host embedded-quote argument quoting'
Assert-Equal (ConvertTo-PrivateDesktopHostArgument -Value 'trailing slash\') '"trailing slash\\"' 'dedicated host trailing-slash argument quoting'
Assert-PrivateDesktopSafetyEnvelope -Result $Payload
Assert-Equal (Test-PrivateDesktopParentHostResult -Result $Payload -ActualHostExitCode 0) $true 'reusable parent-host validation'

$OutcomeNeutral = Copy-ContractPayload $Payload
$OutcomeNeutral.classification = 'NEEDS_CONTEXT'
$OutcomeNeutral.helper_exit_code = 20
$OutcomeNeutral.timed_out = $true
$OutcomeNeutral.root_exit_code = 99
$OutcomeNeutral.visible_windows = @([pscustomobject]@{
    pid = 0
    hwnd = '0x1'
    event = 'EVENT_OBJECT_SHOW'
    title = 'synthetic'
    class_name = 'synthetic'
    desktop = 'CosHeadless_contract_only'
    observed_utc = '2026-08-11T00:00:02.5000000Z'
})
Assert-PrivateDesktopSafetyEnvelope -Result $OutcomeNeutral

$DiagnosticNeutral = Copy-ContractPayload $Payload
$DiagnosticNeutral.job_total_processes = $null
$DiagnosticNeutral.process_diagnostic_errors = @('synthetic completion-port diagnostic')
Assert-PrivateDesktopSafetyEnvelope -Result $DiagnosticNeutral
$DiagnosticMismatch = Copy-ContractPayload $Payload
$DiagnosticMismatch.job_total_processes = 62
$DiagnosticMismatch.observed_distinct_process_id_count = 64
Assert-PrivateDesktopSafetyEnvelope -Result $DiagnosticMismatch

$Catastrophic = Copy-ContractPayload $Payload
$Catastrophic.classification = 'NEEDS_CONTEXT'
$Catastrophic.helper_exit_code = 20
$Catastrophic.host_termination_required = $true
$Catastrophic.cleanup_complete = $false
$Catastrophic.cleanup_errors = @('synthetic unproven Job drain')
$Catastrophic.monitor_completed_after_job_drain = $false
Assert-Equal (Test-PrivateDesktopParentHostResult -Result $Catastrophic -ActualHostExitCode 20) $false 'catastrophic parent-host disposition'
$CatastrophicSafetyRejected = $false
try {
    Assert-PrivateDesktopSafetyEnvelope -Result $Catastrophic
} catch {
    $CatastrophicSafetyRejected = $true
}
Assert-Equal $CatastrophicSafetyRejected $true 'catastrophic result cannot pass reusable safety envelope'

Assert-ParentHostContractRejected $Catastrophic 20 'parent missing/truncated result-field rejection' {
    param($Item)
    $Item.PSObject.Properties.Remove('finished_utc')
}
Assert-ParentHostContractRejected $Catastrophic 22 'parent actual host exit mismatch rejection' { param($Item) }
Assert-ParentHostContractRejected $Catastrophic 20 'parent persisted mapping mismatch rejection' { param($Item) $Item.helper_exit_code = 22 }
Assert-ParentHostContractRejected $Catastrophic 22 'parent catastrophic non-NEEDS_CONTEXT rejection' {
    param($Item)
    $Item.classification = 'LAUNCH_ERROR'
    $Item.helper_exit_code = 22
}
Assert-ParentHostContractRejected $Catastrophic 0 'parent catastrophic zero/COMPLETED rejection' {
    param($Item)
    $Item.classification = 'COMPLETED'
    $Item.helper_exit_code = 0
}
Assert-ParentHostContractRejected $Catastrophic 20 'parent catastrophic cleanup claim rejection' { param($Item) $Item.cleanup_complete = $true }
Assert-ParentHostContractRejected $Catastrophic 20 'parent catastrophic monitor claim rejection' { param($Item) $Item.monitor_completed_after_job_drain = $true }

Assert-ContractRejected $Payload 'schema v1 rejection' { param($Item) $Item.schema_version = 1 }
Assert-ContractRejected $Payload 'legacy coverage property rejection' {
    param($Item)
    $Item | Add-Member -NotePropertyName process_coverage_complete -NotePropertyValue $true
}
Assert-ContractRejected $Payload 'private desktop initially empty gate' { param($Item) $Item.private_desktop_initially_empty = $false }
Assert-ContractRejected $Payload 'monitor armed before create gate' { param($Item) $Item.monitor_armed_before_create = $false }
Assert-ContractRejected $Payload 'monitor armed before resume gate' { param($Item) $Item.monitor_armed_before_resume = $false }
Assert-ContractRejected $Payload 'root assigned before resume gate' { param($Item) $Item.root_assigned_to_job_before_resume = $false }
Assert-ContractRejected $Payload 'Job kill-on-close verification gate' { param($Item) $Item.job_kill_on_close_verified = $false }
Assert-ContractRejected $Payload 'Job breakaway forbidden gate' { param($Item) $Item.job_breakaway_forbidden = $false }
Assert-ContractRejected $Payload 'Job handle non-inheritable gate' { param($Item) $Item.job_handle_non_inheritable = $false }
Assert-ContractRejected $Payload 'Job drained gate' { param($Item) $Item.job_drained = $false }
Assert-ContractRejected $Payload 'final Job active-process count gate' { param($Item) $Item.job_active_processes_final = 1 }
Assert-ContractRejected $Payload 'monitor completion after Job drain gate' { param($Item) $Item.monitor_completed_after_job_drain = $false }
Assert-ContractRejected $Payload 'catastrophic host termination gate' { param($Item) $Item.host_termination_required = $true }
Assert-ContractRejected $Payload 'cleanup complete gate' { param($Item) $Item.cleanup_complete = $false }
Assert-ContractRejected $Payload 'cleanup errors gate' { param($Item) $Item.cleanup_errors = @('synthetic cleanup error') }
Assert-ContractRejected $Payload 'armed/create timestamp ordering' { param($Item) $Item.process_created_utc = '2026-08-11T00:00:00.5000000Z' }
Assert-ContractRejected $Payload 'create/resume timestamp ordering' { param($Item) $Item.resumed_utc = '2026-08-11T00:00:01.5000000Z' }
Assert-ContractRejected $Payload 'accounting kind rejection' { param($Item) $Item.process_id_accounting_kind = 'complete_pid_history' }
Assert-ContractRejected $Payload 'negative observed PID count rejection' { param($Item) $Item.observed_distinct_process_id_count = -1 }
Assert-ContractRejected $Payload 'negative Job total rejection' { param($Item) $Item.job_total_processes = -1 }
Assert-ContractRejected $Payload 'process_ids scalar rejection' { param($Item) $Item.process_ids = 1 }
Assert-ContractRejected $Payload 'new_process_ids scalar rejection' { param($Item) $Item.new_process_ids = 1 }
Assert-ContractRejected $Payload 'active_snapshot_process_ids scalar rejection' { param($Item) $Item.active_snapshot_process_ids = 1 }
Assert-ContractRejected $Payload 'process diagnostic errors scalar rejection' { param($Item) $Item.process_diagnostic_errors = 'synthetic scalar' }
Assert-ContractRejected $Payload 'visible window with non-NEEDS_CONTEXT rejection' {
    param($Item)
    $Item.visible_windows = @([pscustomobject]@{ pid = 0; hwnd = '0x2'; event = 'EVENT_OBJECT_SHOW' })
}
Assert-ContractRejected $Payload 'helper exit classification mapping rejection' { param($Item) $Item.helper_exit_code = 20 }
Assert-ContractRejected $Payload 'unknown helper exit rejection' { param($Item) $Item.helper_exit_code = 99 }
Assert-PrivateDesktopRunnerSourceContract -SourcePath (Join-Path $PSScriptRoot 'PrivateDesktopRunner.cs')
$WrapperSource = [IO.File]::ReadAllText((Join-Path $PSScriptRoot 'Invoke-PrivateDesktopProcess.ps1'))
$InvokeWrapperStart = $WrapperSource.IndexOf('function Invoke-PrivateDesktopProcess', [StringComparison]::Ordinal)
$InternalHostStart = $WrapperSource.IndexOf('if ($PrivateDesktopInternalHostMode)', $InvokeWrapperStart, [StringComparison]::Ordinal)
$InvokeWrapperBody = $WrapperSource.Substring($InvokeWrapperStart, $InternalHostStart - $InvokeWrapperStart)
$InternalHostBody = $WrapperSource.Substring($InternalHostStart)
$HostObservationStart = $InvokeWrapperBody.IndexOf('$HostExitAndCodeProven = $false', [StringComparison]::Ordinal)
$HostInitialWait = $InvokeWrapperBody.IndexOf('$HostProcess.WaitForExit($HostWaitMilliseconds)', $HostObservationStart, [StringComparison]::Ordinal)
$HostInitialHasExited = $InvokeWrapperBody.IndexOf('$HostProcess.HasExited', $HostInitialWait, [StringComparison]::Ordinal)
$HostInitialExitCode = $InvokeWrapperBody.IndexOf('$ActualHostExitCode = $HostProcess.ExitCode', $HostInitialHasExited, [StringComparison]::Ordinal)
$HostObservationProven = $InvokeWrapperBody.IndexOf('$HostExitAndCodeProven = $true', $HostInitialExitCode, [StringComparison]::Ordinal)
$HostObservationCatch = $InvokeWrapperBody.IndexOf('$HostObservationError = $_.Exception.Message', $HostObservationProven, [StringComparison]::Ordinal)
$HostObservationFinally = $InvokeWrapperBody.IndexOf('} finally {', $HostObservationCatch, [StringComparison]::Ordinal)
$HostTeardownGate = $InvokeWrapperBody.IndexOf('if ($HostStarted -and -not $HostExitAndCodeProven)', $HostObservationFinally, [StringComparison]::Ordinal)
$HostTeardownCall = $InvokeWrapperBody.IndexOf('Invoke-PrivateDesktopHostFailClosedTeardown -Process $HostProcess', $HostTeardownGate, [StringComparison]::Ordinal)
if ($InvokeWrapperStart -lt 0 -or $InternalHostStart -le $InvokeWrapperStart -or
    $InvokeWrapperBody.Contains('Import-PrivateDesktopRunner') -or
    $InvokeWrapperBody.Contains('::RunRequestFile(') -or
    $InvokeWrapperBody.Contains('Add-Type') -or
    -not $InvokeWrapperBody.Contains('New-Object System.Diagnostics.ProcessStartInfo') -or
    -not $InvokeWrapperBody.Contains('$StartInfo.UseShellExecute = $false') -or
    -not $InvokeWrapperBody.Contains('$StartInfo.CreateNoWindow = $true') -or
    -not $InvokeWrapperBody.Contains('$HostProcess.WaitForExit($HostWaitMilliseconds)') -or
    -not $InvokeWrapperBody.Contains('$HostProcess.HasExited') -or
    -not $InvokeWrapperBody.Contains('$HostExitAndCodeProven = $true') -or
    -not $InvokeWrapperBody.Contains('if ($HostStarted -and -not $HostExitAndCodeProven)') -or
    -not $InvokeWrapperBody.Contains('Invoke-PrivateDesktopHostFailClosedTeardown -Process $HostProcess') -or
    -not $InvokeWrapperBody.Contains('$ActualHostExitCode = $HostProcess.ExitCode') -or
    -not $InvokeWrapperBody.Contains('Test-PrivateDesktopParentHostResult') -or
    $HostObservationStart -lt 0 -or $HostInitialWait -le $HostObservationStart -or
    $HostInitialHasExited -le $HostInitialWait -or $HostInitialExitCode -le $HostInitialHasExited -or
    $HostObservationProven -le $HostInitialExitCode -or $HostObservationCatch -le $HostObservationProven -or
    $HostObservationFinally -le $HostObservationCatch -or $HostTeardownGate -le $HostObservationFinally -or
    $HostTeardownCall -le $HostTeardownGate -or
    [regex]::Matches($InvokeWrapperBody, '\$HostProcess\.Start\(\)').Count -ne 1) {
    throw 'Parent wrapper does not launch and validate exactly one dedicated noninteractive PowerShell helper host.'
}
$HostTeardownStart = $WrapperSource.IndexOf('function Invoke-PrivateDesktopHostFailClosedTeardown', [StringComparison]::Ordinal)
$HostTeardownEnd = $WrapperSource.IndexOf('function Test-PrivateDesktopIntegralValue', $HostTeardownStart, [StringComparison]::Ordinal)
$HostTeardownBody = $WrapperSource.Substring($HostTeardownStart, $HostTeardownEnd - $HostTeardownStart)
if ($HostTeardownStart -lt 0 -or $HostTeardownEnd -le $HostTeardownStart -or
    -not $HostTeardownBody.Contains('$Process.Kill()') -or
    -not $HostTeardownBody.Contains('$Process.WaitForExit(5000)') -or
    -not $HostTeardownBody.Contains('$Process.HasExited') -or
    -not $HostTeardownBody.Contains('kill_issued = $KillIssued') -or
    -not $HostTeardownBody.Contains('exit_proven = $ExitProven') -or
    -not $InvokeWrapperBody.Contains('no retry is permitted') -or
    $InvokeWrapperBody.Contains('parent termination was issued and exit was then proven')) {
    throw 'Parent wrapper can lose ownership after host observation failure or overstate termination proof.'
}
if (-not $InternalHostBody.Contains('Import-PrivateDesktopRunner') -or
    -not $InternalHostBody.Contains('::RunRequestFile(') -or
    -not $InternalHostBody.Contains('[Environment]::Exit($InternalHelperExitCode)')) {
    throw 'Internal helper-host mode does not own C# loading and terminal normal-path host exit.'
}
$ScriptParameterStart = $WrapperSource.IndexOf('param(', [StringComparison]::Ordinal)
$ScriptParameterEnd = $WrapperSource.IndexOf('function Write-NewUtf8File', $ScriptParameterStart, [StringComparison]::Ordinal)
$ScriptParameterBlock = $WrapperSource.Substring($ScriptParameterStart, $ScriptParameterEnd - $ScriptParameterStart)
if ($ScriptParameterBlock.Contains('[string]$RequestPath') -or
    $ScriptParameterBlock.Contains('[string]$RunnerSource') -or
    -not $ScriptParameterBlock.Contains('$PrivateDesktopInternalHostMode') -or
    -not $ScriptParameterBlock.Contains('$PrivateDesktopInternalRequestPath') -or
    -not $ScriptParameterBlock.Contains('$PrivateDesktopInternalRunnerSource')) {
    throw 'Dot-sourcing the wrapper can still overwrite generic caller variables.'
}
if ($WrapperSource.Contains('Add-Member -NotePropertyName helper_exit_code') -or
    -not $WrapperSource.Contains('function Test-PrivateDesktopParentHostResult') -or
    -not $WrapperSource.Contains('Actual PowerShell host exit does not match persisted helper_exit_code.')) {
    throw 'Parent result validation does not compare actual host exit with the C#-persisted mapping.'
}
$ContractOnlyMarker = 'if ($' + 'ContractOnly) {'
$FullSelfTestMarker = '$' + 'RunnerSource = Join-Path $PSScriptRoot'
$ContractOnlyBoundary = $SelfTestSource.IndexOf($ContractOnlyMarker, [StringComparison]::Ordinal)
$FullSelfTestStart = $SelfTestSource.IndexOf($FullSelfTestMarker, $ContractOnlyBoundary, [StringComparison]::Ordinal)
$FullSelfTestBody = $SelfTestSource.Substring($FullSelfTestStart)
if ($ContractOnlyBoundary -lt 0 -or $FullSelfTestStart -le $ContractOnlyBoundary -or
    -not $FullSelfTestBody.Contains('public static class Exit259Fixture') -or
    -not $FullSelfTestBody.Contains("return 259;") -or
    -not $FullSelfTestBody.Contains("-FilePath (Join-Path `$TestRoot 'Exit259Fixture.exe')") -or
    -not $FullSelfTestBody.Contains("Assert-Equal `$Exit259.root_exit_code 259 'exit-259 root exit code'")) {
    throw 'Full selftest does not preserve a caller-level exit-code-259 regression case.'
}

if ($ContractOnly) {
    [pscustomobject][ordered]@{
        verdict = 'PASS'
        mode = 'CONTRACT_ONLY'
        accepted_job_total_processes = 66
        accepted_observed_distinct_process_id_count = 63
        rejected_mutations = 27
        rejected_parent_host_mutations = 7
        catastrophic_parent_validation = 'PASS'
        dedicated_host_architecture = 'PASS'
        atomic_job_assignment = 'PASS'
        root_exit_259_contract = 'PASS'
        ascii_source_contract = 'PASS'
        static_source_contract = 'PASS'
    }
    return
}

$RunnerSource = Join-Path $PSScriptRoot 'PrivateDesktopRunner.cs'
$CSharp5 = New-Object System.CodeDom.Compiler.CompilerParameters
$CSharp5.CompilerOptions = '/langversion:5'
foreach ($Reference in @('System.dll', 'System.Core.dll', 'System.Runtime.Serialization.dll', 'System.Xml.dll')) {
    [void]$CSharp5.ReferencedAssemblies.Add($Reference)
}
Add-Type -Path $RunnerSource -CompilerParameters $CSharp5 -ErrorAction Stop

$TestRoot = Join-Path ([IO.Path]::GetTempPath()) ('cos-private-desktop-selftest-' + [Guid]::NewGuid().ToString('N'))
[IO.Directory]::CreateDirectory($TestRoot) | Out-Null
$PowerShell = (Get-Command powershell.exe -ErrorAction Stop).Source

function Assert-MonitorAndCleanup($Result, [string]$Context) {
    Assert-Equal $Result.started $true "$Context started"
    Assert-PrivateDesktopSafetyEnvelope -Result $Result
}

try {
    Add-Type -TypeDefinition @'
using System;
using System.Diagnostics;
using System.Reflection;
using System.Threading;

public static class TimeoutTreeFixture {
    public static int Main(string[] args) {
        if (args.Length == 1 && args[0] == "child") {
            Thread.Sleep(60000);
            return 0;
        }
        ProcessStartInfo start = new ProcessStartInfo();
        start.FileName = Assembly.GetExecutingAssembly().Location;
        start.Arguments = "child";
        start.UseShellExecute = false;
        start.CreateNoWindow = true;
        Process.Start(start);
        Thread.Sleep(60000);
        return 0;
    }
}
'@ -ReferencedAssemblies @('System.dll') -OutputAssembly (Join-Path $TestRoot 'TimeoutTreeFixture.exe') -OutputType ConsoleApplication

    Add-Type -TypeDefinition @'
using System;
using System.Diagnostics;
using System.Reflection;

public static class CoverageBurstFixture {
    public static int Main(string[] args) {
        if (args.Length == 1 && args[0] == "child") return 0;
        for (int i = 0; i < 32; i++) {
            ProcessStartInfo start = new ProcessStartInfo();
            start.FileName = Assembly.GetExecutingAssembly().Location;
            start.Arguments = "child";
            start.UseShellExecute = false;
            start.CreateNoWindow = true;
            using (Process child = Process.Start(start)) child.WaitForExit();
        }
        return 0;
    }
}
'@ -ReferencedAssemblies @('System.dll') -OutputAssembly (Join-Path $TestRoot 'CoverageBurstFixture.exe') -OutputType ConsoleApplication

    Add-Type -TypeDefinition @'
using System;
using System.Text;

public static class ArgvProbeFixture {
    public static int Main(string[] args) {
        for (int i = 0; i < args.Length; i++) {
            Console.WriteLine(Convert.ToBase64String(Encoding.UTF8.GetBytes(args[i])));
        }
        return 0;
    }
}
'@ -ReferencedAssemblies @('System.dll') -OutputAssembly (Join-Path $TestRoot 'ArgvProbeFixture.exe') -OutputType ConsoleApplication

    Add-Type -TypeDefinition @'
using System;

public static class EnvironmentProbeFixture {
    public static int Main(string[] args) {
        string setValue = Environment.GetEnvironmentVariable(args[0], EnvironmentVariableTarget.Process);
        string removedValue = Environment.GetEnvironmentVariable(args[1], EnvironmentVariableTarget.Process);
        Console.Write((setValue ?? "<NULL>") + "|" + (removedValue ?? "<NULL>"));
        return 0;
    }
}
'@ -ReferencedAssemblies @('System.dll') -OutputAssembly (Join-Path $TestRoot 'EnvironmentProbeFixture.exe') -OutputType ConsoleApplication

    Add-Type -TypeDefinition @'
public static class Exit259Fixture {
    public static int Main(string[] args) {
        return 259;
    }
}
'@ -ReferencedAssemblies @('System.dll') -OutputAssembly (Join-Path $TestRoot 'Exit259Fixture.exe') -OutputType ConsoleApplication

    $NoWindowDir = Join-Path $TestRoot 'no-window-exit7'
    $NoWindow = Invoke-PrivateDesktopProcess -FilePath $PowerShell `
        -ArgumentList @('-NoProfile', '-NonInteractive', '-Command', '[Console]::Out.Write("out"); [Console]::Error.Write("err"); exit 7') `
        -WorkingDirectory $TestRoot -EnvironmentOverrides @{ COS_CHILD_ONLY = 'yes' } `
        -TimeoutSeconds 20 -EvidenceDirectory $NoWindowDir
    Assert-Equal $NoWindow.classification 'COMPLETED' 'no-window classification'
    Assert-Equal $NoWindow.root_exit_code 7 'no-window exit code'
    Assert-Equal @($NoWindow.visible_windows).Count 0 'no-window visible count'
    Assert-Equal $NoWindow.timed_out $false 'no-window timeout flag'
    Assert-MonitorAndCleanup $NoWindow 'no-window'
    Assert-Equal ([IO.File]::ReadAllText((Join-Path $NoWindowDir 'stdout.txt'))) 'out' 'stdout capture'
    Assert-Equal ([IO.File]::ReadAllText((Join-Path $NoWindowDir 'stderr.txt'))) 'err' 'stderr capture'

    $Exit259Dir = Join-Path $TestRoot 'exit-259'
    $Exit259 = Invoke-PrivateDesktopProcess -FilePath (Join-Path $TestRoot 'Exit259Fixture.exe') `
        -WorkingDirectory $TestRoot -TimeoutSeconds 20 -EvidenceDirectory $Exit259Dir
    Assert-Equal $Exit259.classification 'COMPLETED' 'exit-259 classification'
    Assert-Equal $Exit259.root_exit_code 259 'exit-259 root exit code'
    Assert-Equal $Exit259.timed_out $false 'exit-259 timeout flag'
    Assert-Equal @($Exit259.visible_windows).Count 0 'exit-259 visible count'
    Assert-MonitorAndCleanup $Exit259 'exit-259'

    $TimeoutDir = Join-Path $TestRoot 'timeout-tree-drain'
    $Timeout = Invoke-PrivateDesktopProcess -FilePath (Join-Path $TestRoot 'TimeoutTreeFixture.exe') `
        -WorkingDirectory $TestRoot -TimeoutSeconds 1 -EvidenceDirectory $TimeoutDir
    Assert-Equal $Timeout.classification 'TIMEOUT' 'timeout classification'
    Assert-Equal $Timeout.timed_out $true 'timeout flag'
    Assert-Equal @($Timeout.visible_windows).Count 0 'timeout visible count'
    Assert-MonitorAndCleanup $Timeout 'timeout'

    $CoverageDir = Join-Path $TestRoot 'short-lived-pid-coverage'
    $Coverage = Invoke-PrivateDesktopProcess -FilePath (Join-Path $TestRoot 'CoverageBurstFixture.exe') `
        -WorkingDirectory $TestRoot -TimeoutSeconds 20 -EvidenceDirectory $CoverageDir
    Assert-Equal $Coverage.classification 'COMPLETED' 'short-lived coverage classification'
    Assert-Equal $Coverage.root_exit_code 0 'short-lived coverage exit code'
    Assert-Equal $Coverage.timed_out $false 'short-lived coverage timeout flag'
    Assert-Equal @($Coverage.visible_windows).Count 0 'short-lived coverage visible count'
    Assert-MonitorAndCleanup $Coverage 'short-lived coverage'

    $UnicodeArgument = -join @([char]0x4E2D, [char]0x6587, [char]0x20, [char]0x7A7A, [char]0x683C)
    $ComplexArguments = @('', 'plain', 'white space', 'quote"inside', 'trailing\', 'slashes\\before"quote', $UnicodeArgument, "tab`tvalue")
    $ArgvDir = Join-Path $TestRoot 'argv-roundtrip'
    $ArgvResult = Invoke-PrivateDesktopProcess -FilePath (Join-Path $TestRoot 'ArgvProbeFixture.exe') `
        -ArgumentList $ComplexArguments -WorkingDirectory $TestRoot -TimeoutSeconds 20 -EvidenceDirectory $ArgvDir
    Assert-Equal $ArgvResult.classification 'COMPLETED' 'argv classification'
    Assert-Equal $ArgvResult.root_exit_code 0 'argv exit code'
    Assert-Equal $ArgvResult.timed_out $false 'argv timeout flag'
    Assert-Equal @($ArgvResult.visible_windows).Count 0 'argv visible count'
    Assert-MonitorAndCleanup $ArgvResult 'argv'
    $ArgvLines = [IO.File]::ReadAllLines((Join-Path $ArgvDir 'stdout.txt'))
    Assert-Equal $ArgvLines.Count $ComplexArguments.Count 'argv count'
    for ($Index = 0; $Index -lt $ComplexArguments.Count; $Index++) {
        $Decoded = [Text.Encoding]::UTF8.GetString([Convert]::FromBase64String($ArgvLines[$Index]))
        Assert-Equal $Decoded $ComplexArguments[$Index] ("argv[$Index]")
    }
    Assert-Equal $ArgvLines[6] '5Lit5paHIOepuuagvA==' 'unicode argv UTF-8 base64'

    $SetName = 'COS_PRIVATE_DESKTOP_SET_' + [Guid]::NewGuid().ToString('N')
    $RemoveName = 'COS_PRIVATE_DESKTOP_REMOVE_' + [Guid]::NewGuid().ToString('N')
    [Environment]::SetEnvironmentVariable($SetName, 'parent-set', 'Process')
    [Environment]::SetEnvironmentVariable($RemoveName, 'parent-remove', 'Process')
    try {
        $EnvironmentDir = Join-Path $TestRoot 'environment-isolation'
        $EnvironmentResult = Invoke-PrivateDesktopProcess -FilePath (Join-Path $TestRoot 'EnvironmentProbeFixture.exe') `
            -ArgumentList @($SetName, $RemoveName) -WorkingDirectory $TestRoot `
            -EnvironmentOverrides @{ $SetName = 'child-set'; $RemoveName = $null } `
            -TimeoutSeconds 20 -EvidenceDirectory $EnvironmentDir
        Assert-Equal $EnvironmentResult.classification 'COMPLETED' 'environment classification'
        Assert-Equal $EnvironmentResult.root_exit_code 0 'environment exit code'
        Assert-Equal $EnvironmentResult.timed_out $false 'environment timeout flag'
        Assert-Equal @($EnvironmentResult.visible_windows).Count 0 'environment visible count'
        Assert-MonitorAndCleanup $EnvironmentResult 'environment'
        Assert-Equal ([IO.File]::ReadAllText((Join-Path $EnvironmentDir 'stdout.txt'))) 'child-set|<NULL>' 'child environment set/remove'
        Assert-Equal ([Environment]::GetEnvironmentVariable($SetName, 'Process')) 'parent-set' 'parent set variable unchanged'
        Assert-Equal ([Environment]::GetEnvironmentVariable($RemoveName, 'Process')) 'parent-remove' 'parent removed variable unchanged'
    } finally {
        [Environment]::SetEnvironmentVariable($SetName, $null, 'Process')
        [Environment]::SetEnvironmentVariable($RemoveName, $null, 'Process')
    }

    $ExistingDir = Join-Path $TestRoot 'preexisting-evidence'
    [IO.Directory]::CreateDirectory($ExistingDir) | Out-Null
    [IO.File]::WriteAllText((Join-Path $ExistingDir 'sentinel.txt'), 'do-not-overwrite')
    $Rejected = $false
    try {
        Invoke-PrivateDesktopProcess -FilePath $PowerShell -ArgumentList @('-NoProfile', '-Command', 'exit 0') `
            -WorkingDirectory $TestRoot -TimeoutSeconds 5 -EvidenceDirectory $ExistingDir | Out-Null
    } catch {
        $Rejected = $_.Exception.Message -like 'EvidenceDirectory already exists*'
    }
    Assert-Equal $Rejected $true 'preexisting evidence rejection'
    Assert-Equal ([IO.File]::ReadAllText((Join-Path $ExistingDir 'sentinel.txt'))) 'do-not-overwrite' 'preexisting sentinel'

    Assert-PrivateDesktopRunnerSourceContract -SourcePath $RunnerSource

    if ($IncludeVisibleWindowTest) {
        Add-Type -TypeDefinition @'
using System;
using System.Diagnostics;
using System.Reflection;
using System.Threading;
using System.Windows.Forms;
public static class VisibleDescendantFixture {
    public static void Main(string[] args) {
        if (args.Length == 1 && args[0] == "child") {
            using (Form form = new Form()) {
                form.Text = "private desktop sentinel";
                form.Show();
                Application.DoEvents();
                Thread.Sleep(25);
                form.Close();
                Application.DoEvents();
            }
            return;
        }
        ProcessStartInfo start = new ProcessStartInfo();
        start.FileName = Assembly.GetExecutingAssembly().Location;
        start.Arguments = "child";
        start.UseShellExecute = false;
        start.CreateNoWindow = true;
        Process.Start(start);
        Thread.Sleep(30000);
    }
}
'@ -ReferencedAssemblies @('System.dll', 'System.Windows.Forms.dll') -OutputAssembly (Join-Path $TestRoot 'VisibleDescendantFixture.exe') -OutputType ConsoleApplication
        $VisibleDir = Join-Path $TestRoot 'visible-descendant'
        $Visible = Invoke-PrivateDesktopProcess -FilePath (Join-Path $TestRoot 'VisibleDescendantFixture.exe') `
            -WorkingDirectory $TestRoot -TimeoutSeconds 20 -EvidenceDirectory $VisibleDir
        Assert-Equal $Visible.classification 'NEEDS_CONTEXT' 'visible descendant classification'
        Assert-Equal $Visible.timed_out $false 'visible descendant timeout flag'
        Assert-MonitorAndCleanup $Visible 'visible descendant'
        if (@($Visible.visible_windows).Count -lt 1) { throw 'visible descendant evidence is empty.' }
        $Sentinels = @($Visible.visible_windows | Where-Object { $_.title -ceq 'private desktop sentinel' })
        if ($Sentinels.Count -lt 1) { throw 'visible descendant did not record the actual private-desktop Form.' }
        if (@($Sentinels | Where-Object { $_.event -ceq 'EVENT_OBJECT_SHOW' }).Count -lt 1) {
            throw 'visible descendant Form was not preserved from the SHOW hook.'
        }
        if (@($Visible.visible_windows | Where-Object { $_.class_name -ceq 'PseudoConsoleWindow' }).Count -ne 0) {
            throw 'visible descendant was classified from a PseudoConsoleWindow instead of the private Form.'
        }
    }

    [pscustomobject][ordered]@{
        verdict = 'PASS'
        test_root = $TestRoot
        contract_v2 = 'PASS'
        no_window_exit7 = 'PASS'
        timeout_tree_drain = 'PASS'
        short_lived_process_accounting = 'PASS'
        argv_roundtrip = 'PASS'
        environment_isolation = 'PASS'
        preexisting_evidence_rejection = 'PASS'
        banned_api_scan = 'PASS'
        visible_descendant = $(if ($IncludeVisibleWindowTest) { 'PASS' } else { 'NOT_RUN' })
    }
} catch {
    Write-Error $_
    throw
}
```

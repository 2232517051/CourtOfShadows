# Terminal Collapse Generator Recovery v3 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Seal the two prior failed generator lineages, run one fresh headless generator under the corrected two-stream log contract, prove its save through one ordinary-run observer, freeze the only eligible mother, and continue the approved terminal-collapse rules and narrative workflow from v3 authority only.

**Architecture:** A controller-created out-of-band lock authenticates the reviewed S3/P3 document chain and a schema-v2 manifest of 115 immutable predecessor artifacts. Task 1 consumes separate one-shot generator and observer ledgers, treats helper stdout as the sole rpytest report and Ren'Py `log.txt` as diagnostic-only, then publishes a schema-v3 Task 1 completion over an exact 141-file union. Task 2, Task 3, and Phase B revalidate that authority before every irreversible or model-external action.

**Tech Stack:** Windows PowerShell 5.1, Git, Ren'Py 8.5.2.26010301, strict UTF-8 JSON, SHA-256, private Windows desktop/Job Object helper, Python AST checks, Ren'Py testsuite, Claude Opus 4.6.

## Global Constraints

- Authority topology is exact and linear: P2 `25c2ea674948ad89e8b48befb89643a8687648a4` → S3 `5fa8fb14792e095e066c3e9f698eda9ea4380854` → future plan-only P3 → future exact three-file rules commit R3. `P3:game` and every earlier node's `game/` tree must be `fa7a398e9d989731b24e3c1642f3e2e33ce846ff`.
- The approved specification is `docs/superpowers/specs/2026-08-14-terminal-collapse-generator-recovery-v3-design.md`, physical SHA-256 `978116FE22B8C65578B78E800EF6039053284EA7E674271646D130BBB4BBF470`, raw Git blob `4c753503ab76484a546c8313c03914dd633a8902`, and commit S3. The approved plan path is `docs/superpowers/plans/2026-08-14-terminal-collapse-generator-recovery-v3.md`. P3 is resolved dynamically only after review and the single-plan commit; this plan must not self-embed P3, its physical SHA-256, raw blob, or the approval-lock hash.
- P3 must have subject `docs: plan terminal collapse generator recovery v3`, direct parent S3, and exactly the one plan path above. S3 must have direct parent P2 and exactly the one v3 spec path. Any merge, intermediate commit, additional path, index residue, hook side effect, or `game/` tree drift stops sealing.
- The controller creates `.superpowers/sdd/terminal-collapse-ending/recovery-v3/predecessor-evidence.json` first and `.superpowers/sdd/terminal-collapse-ending/approved-plan-lock-v3.json` second, only after P3 passes independent Spec and Standards review. Both are CreateNew, strict UTF-8 without BOM, LF-only with final LF, `Flush(true)`, strict reread, and read-only. There is no partial-authority mode: if manifest publication succeeds but lock publication fails, stop with `NEEDS_CONTEXT` and preserve the manifest; do not delete it or try a replacement namespace.
- Every fresh Task 0/1/2/3 and every Phase B replay receives the uppercase physical lock SHA-256 out of band as `$ApprovalLockSha256`. Its first project action is lock validation. No task may derive that authority from the lock's contents, a plan paragraph, a previous shell variable, or a chat transcript.
- The predecessor manifest schema is 2 and contains exactly 115 current authority/evidence leaves. Its catalog is exactly 24,660 UTF-8 bytes with SHA-256 `9694E728A82F6DDC743DA5E83967EAC7EE02FFA62FA53E21F4A2374F27DDDA24`: 83 leaves from the v2 predecessor manifest, 12 v2 authority/evidence leaves, and 20 v2 runtime leaves. These values are a frozen gate, not a baseline that may be silently updated.
- The v3 approval lock schema is 3 with exactly 26 ordered fields. It binds P3/S3/P2, the v2 lock, the schema-v2 predecessor manifest, the unchanged game tree, fresh-one-shot strategy, the consumed v2 attempt and its non-adoption disposition, both v3 attempt-ledger paths and limits, `helper_stdout` as `test_result_stream`, and `diagnostic_only` as `engine_log_role`.
- Legacy generator outcome remains `TIMEOUT / HELPER_TIMEOUT / preserved_not_used`. Recovery v2 remains `GOVERNANCE_CONTRACT_FAILURE / COMPLETED / LOG_CONTRACT_MISMATCH / preserved_not_used`, with generator count 1 and observer count 0. Neither candidate may be read as a source, copied, promoted, renamed, moved, deleted, cleaned, or used as fallback.
- All v1/v2 locks, manifests, attempts, worktrees, SaveDirs, candidates, stdout, engine logs, ledgers, and failure evidence remain byte-for-byte in place. Recovery v3 cleanup never includes any v1/v2 path. The 61 explicitly sealed v2 worktree cache files are diagnostic exclusions, not authority leaves, and are never read by Task 1/2/3 or removed by v3 cleanup.
- All new durable runtime evidence is rooted only at `.superpowers/sdd/terminal-collapse-ending/recovery-v3/`, except the sibling v3 approval lock. The generator and observer each have one CreateNew ledger and an attempt limit of 1. Directory existence consumes that authority. Any parse, static contract, transport, helper, Ren'Py, stdout/stderr, state, save, completion, observer, mother, or cleanup failure is terminal `NEEDS_CONTEXT`: no retry, GUID change, alternate evidence root, timeout increase, direct launch, manual fallback, or ledger deletion.
- Before Task 1, total new v3 Ren'Py/helper/Python/scanner invocations are exactly zero. The controller ceremony and Task 0 use only Windows PowerShell 5.1 and read-only Git inspection; they do not launch helper, Ren'Py, Python, scanners, repository tests, lint, full tests, observers, fixtures, or UI.
- The old helper full selftest and version probe remain reused frozen evidence and are not rerun. The three helper sources remain exactly 82,334 / 24,229 / 53,188 bytes with SHA-256 `E0393DB1E113FDB8C35097978AA73B7D33AFDD5788499002B6423D883DEED4E8`, `73A3F9C43CF994E08F004E0A1266122A3EC5E0EAF065C63E6D9439CF0B0E1880`, and `20198B669F70E51E51F71BD01E6D06D1949D300F43CE9A94FB0190A47D781A15`.
- Every later Ren'Py `test` or ordinary `run`, repository scanner, Lint, Full, and replay must use the audited dedicated-host private-desktop wrapper with process-local dummy video/audio/software renderer and child `RENPY_PATH_TO_SAVES` removed. No Computer Use, user desktop, real input, screenshot, visible/switchable desktop, privacy prompt, or manual UI is authorized.
- The corrected generator contract has three distinct authorities: helper `generator-process/stdout.txt` is the only rpytest `test_report`; fixture `generator-state.json` is the state authority; copied worktree `log.txt` is diagnostic-only `engine_boot_log`. A PASSED line in the engine log is invalid channel mixing, while benign `[rpytest] [exc]` in stdout and dummy-renderer `error(...)` in the engine log are accepted by their exact gates.
- A fresh generator may start only after its frozen ledger and static RED/GREEN contract records exist. A fresh observer may start only after the generator completion is frozen and strictly reread. Mother creation requires frozen observer completion and may source only the v3 external-root target. Task 1 completion requires successful controlled cleanup and the exact 115 + 26 = 141 durable-leaf union.
- Shared index must be empty. Before Task 2, shared status is exactly the protected untracked `docs/superpowers/plans/2026-08-09-winter-interlude-narrative-delivery.md`, SHA-256 `0F39B5F5ACE1D4666DD146863CABDF398B031F5666C29AE337CEB89796E4276C`. Never edit, stage, delete, chmod, move, or include it.
- Task 1 modifies no tracked project file. The only E: generator fixture patch is performed by the host `apply_patch` tool against the exact approved absolute path at its explicit checkpoint; no `apply_patch.bat`, shell write, alternate writer, or claim of a single uninterrupted PowerShell session is allowed. Cross-session state is carried only by frozen seals and explicit checkpoint records.
- Task 2 may modify exactly `game/balance.rpy`, `game/difficulty.rpy`, and `game/test_game.rpy`; R3 must be P3's direct child. Task 2 completion schema 3 still binds exactly 9 invocations, 9 schema-v1 14-field receipts, and an exact 56-file union. Task 3 and every Phase B replay validate P2→S3→P3→R3 plus Task 1's 141 and Task 2's 56 current seals before acting.
- JSON authorities reject BOM, invalid UTF-8, replacement characters, NUL where prohibited, duplicate keys at any nesting depth, missing/extra/reordered properties, scalar/array collapse, type coercion, nonintegral byte fields, noncanonical or out-of-root paths, malformed 40/64-hex values, current file drift, and physical/committed blob mismatch.
- Art, music, sound effects, animation, UI, fonts, and package metadata are unchanged during controller sealing, Task 0, Task 1, and Task 2; package impact before Task 2 is zero. Report all six categories and package impact after every tracked change.

## File and Interface Map

- Existing reviewed authority: `docs/superpowers/specs/2026-08-14-terminal-collapse-generator-recovery-v3-design.md` — S3 specification and exact schema/lineage contract; never modified by this plan.
- Create tracked: `docs/superpowers/plans/2026-08-14-terminal-collapse-generator-recovery-v3.md` — reviewed executable authority P3; the controller dynamically binds its commit, physical SHA-256, and raw Git blob.
- Create ignored: `.superpowers/sdd/terminal-collapse-ending/recovery-v3/predecessor-evidence.json` — schema-v2 exact 115-leaf predecessor seal, two ordered failure records, and exact source inventories.
- Create ignored: `.superpowers/sdd/terminal-collapse-ending/approved-plan-lock-v3.json` — schema-v3 26-field lock; its physical SHA-256 is the only out-of-band task authorization.
- Create ignored in Task 1: `.superpowers/sdd/terminal-collapse-ending/recovery-v3/generator-contract-red.json` and `generator-contract-green.json` — static fixture/log-channel RED and exact 42-case GREEN mutation evidence; no process launch.
- Create ignored in Task 1: `recovery-v3/generator-attempt/{attempt,completion}.json`, `generator-process/{request.json,stdout.txt,stderr.txt,result.json}`, `generator-state.json`, `generator-fixture.rpy`, and `generator-engine-log.txt` — the only v3 generator ledger, transport, state, immutable fixture/log evidence, and completion lineage.
- Create temporary in Task 1: `E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-generator-recovery-v3` and `E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-generator-save-recovery-v3` — one detached generator worktree and one external SaveDir; removable only by the successful four-path cleanup ceremony.
- Create ignored in Task 1: `recovery-v3/observer-attempt/{attempt,completion}.json`, `observer-process/{request.json,stdout.txt,stderr.txt,result.json}`, `observer-state.json`, `observer-fixture.rpy`, and `observer-engine-log.txt` — the only ordinary-run observer ledger, transport, state, immutable fixture/log evidence, and completion lineage.
- Create temporary in Task 1: `E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-observer-recovery-v3` and `E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-observer-save-recovery-v3` — one clean detached observer worktree and one replay SaveDir; removable only by successful cleanup.
- Create ignored in Task 1: `recovery-v3/mother/1-1-*.save`, `baseline-evidence.md`, and `task1-completion.json` — the sole read-only v3 mother, explicit four-lineage invocation baseline, and schema-v3 Task 1 authority over exactly 141 current durable leaves.
- Modify in Task 2 only: `game/balance.rpy`, `game/difficulty.rpy`, and `game/test_game.rpy` — the pure terminal-collapse rule, reachability helpers, and regression coverage; no other product path may enter R3.
- Create ignored in Task 2: `recovery-v3/rules/` evidence and `task2-completion.json` — 9 dedicated-host invocations, 9 exact receipts, exact 56-file union, and schema-v3 R3 authority consumed by Task 3/Phase B.
- Create ignored in Task 3: `recovery-v3/copy/run-01`, `run-02`, and `run-03` — three isolated raw Opus bundles. Task 3 stops for user selection; Phase B consumes only the selected bundle after independently revalidating both completions and the v3 mother.

---

## Controller-only sealing ceremony (after plan review and P3 commit)

This ceremony is performed once by the controller, never by a task worker. It creates the schema-v2 predecessor manifest and then the schema-v3 approval lock before Task 0. It launches no helper, Ren'Py, Python, scanner, fixture, observer, or UI. Run every seal step in the same fresh Windows PowerShell 5.1 Desktop session; any exception is terminal `NEEDS_CONTEXT`, and no created authority is deleted or replaced.

- [ ] **Seal Step 1: Bind P2 → S3 → P3, immutable project inputs, and create-new boundaries**

Run from the shared project root after the independently reviewed plan-only P3 commit:

```powershell
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
if ($PSVersionTable.PSEdition -cne 'Desktop' -or $PSVersionTable.PSVersion.Major -ne 5) {
    throw 'NEEDS_CONTEXT: controller sealing requires Windows PowerShell 5.1 Desktop.'
}

$StrictUtf8 = New-Object System.Text.UTF8Encoding($false, $true)
$ProjectRoot = (Resolve-Path -LiteralPath '.').Path
$P2 = '25c2ea674948ad89e8b48befb89643a8687648a4'
$S3 = '5fa8fb14792e095e066c3e9f698eda9ea4380854'
$GameTree = 'fa7a398e9d989731b24e3c1642f3e2e33ce846ff'
$PlanPath = 'docs/superpowers/plans/2026-08-14-terminal-collapse-generator-recovery-v3.md'
$SpecPath = 'docs/superpowers/specs/2026-08-14-terminal-collapse-generator-recovery-v3-design.md'
$SpecBytes = [int64]41497
$SpecSha256 = '978116FE22B8C65578B78E800EF6039053284EA7E674271646D130BBB4BBF470'
$SpecBlob = '4c753503ab76484a546c8313c03914dd633a8902'
$WinterPlan = 'docs/superpowers/plans/2026-08-09-winter-interlude-narrative-delivery.md'
$WinterSha256 = '0F39B5F5ACE1D4666DD146863CABDF398B031F5666C29AE337CEB89796E4276C'
$EvidenceRoot = Join-Path $ProjectRoot '.superpowers\sdd\terminal-collapse-ending'
$V2Root = Join-Path $EvidenceRoot 'recovery-v2'
$RecoveryRoot = Join-Path $EvidenceRoot 'recovery-v3'
$V2LockPath = Join-Path $EvidenceRoot 'approved-plan-lock-v2.json'
$V2ManifestPath = Join-Path $V2Root 'predecessor-evidence.json'
$ManifestPath = Join-Path $RecoveryRoot 'predecessor-evidence.json'
$ApprovalLockPath = Join-Path $EvidenceRoot 'approved-plan-lock-v3.json'
$GeneratorLedgerPath = Join-Path $RecoveryRoot 'generator-attempt'
$ObserverLedgerPath = Join-Path $RecoveryRoot 'observer-attempt'
$V2GeneratorWorktree = 'E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-generator-recovery-v2'
$V2GeneratorSaveDir = 'E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-generator-save-recovery-v2'
$P3 = (& git rev-parse HEAD).Trim()
if ($LASTEXITCODE -ne 0 -or $P3 -cnotmatch '^[0-9a-f]{40}$') {
    throw 'NEEDS_CONTEXT: could not resolve P3.'
}

function Get-RecoveryCanonicalPath([string]$Path) {
    return [IO.Path]::GetFullPath($Path).TrimEnd(
        [IO.Path]::DirectorySeparatorChar,
        [IO.Path]::AltDirectorySeparatorChar
    )
}
function Assert-RecoveryNoReparsePathComponents([string]$Path, [string]$Context) {
    $Full = [IO.Path]::GetFullPath($Path)
    $VolumeRoot = [IO.Path]::GetPathRoot($Full)
    if ([string]::IsNullOrWhiteSpace($VolumeRoot)) {
        throw ('NEEDS_CONTEXT: path has no volume root: ' + $Context)
    }
    $RootItem = Get-Item -LiteralPath $VolumeRoot -Force -ErrorAction Stop
    if (($RootItem.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
        throw ('NEEDS_CONTEXT: volume root is a reparse point: ' + $Context)
    }
    $Current = $VolumeRoot
    $Tail = $Full.Substring($VolumeRoot.Length)
    $Segments = $Tail.Split(
        [char[]]@([IO.Path]::DirectorySeparatorChar, [IO.Path]::AltDirectorySeparatorChar),
        [StringSplitOptions]::RemoveEmptyEntries
    )
    foreach ($Segment in $Segments) {
        $Current = Join-Path $Current $Segment
        $Item = Get-Item -LiteralPath $Current -Force -ErrorAction Stop
        if (($Item.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
            throw ('NEEDS_CONTEXT: reparse path component: ' + $Context + ': ' + $Current)
        }
    }
    return $Full
}
function Get-RecoveryNonFollowingTree([string]$RootPath, [string]$Context) {
    $Root = Get-RecoveryCanonicalPath $RootPath
    [void](Assert-RecoveryNoReparsePathComponents $Root $Context)
    $RootItem = Get-Item -LiteralPath $Root -Force -ErrorAction Stop
    if (-not $RootItem.PSIsContainer) {
        throw ('NEEDS_CONTEXT: non-following tree root is not a directory: ' + $Context)
    }
    $Directories = New-Object 'System.Collections.Generic.List[string]'
    $Files = New-Object 'System.Collections.Generic.List[string]'
    $Pending = New-Object 'System.Collections.Generic.Stack[string]'
    $Directories.Add($Root)
    $Pending.Push($Root)
    $Prefix = $Root + [IO.Path]::DirectorySeparatorChar
    while ($Pending.Count -gt 0) {
        $DirectoryPath = $Pending.Pop()
        $DirectoryItem = Get-Item -LiteralPath $DirectoryPath -Force -ErrorAction Stop
        if (-not $DirectoryItem.PSIsContainer -or
            (($DirectoryItem.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0)) {
            throw ('NEEDS_CONTEXT: unsafe directory reached before enumeration: ' + $Context + ': ' + $DirectoryPath)
        }
        $Children = @(Get-ChildItem -LiteralPath $DirectoryPath -Force -ErrorAction Stop)
        foreach ($Child in $Children) {
            $ChildFull = Get-RecoveryCanonicalPath $Child.FullName
            if (-not $ChildFull.StartsWith($Prefix, [StringComparison]::OrdinalIgnoreCase) -or
                (($Child.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0)) {
                throw ('NEEDS_CONTEXT: out-of-root or reparse child: ' + $Context + ': ' + $ChildFull)
            }
            if ($Child.PSIsContainer) {
                $Directories.Add($ChildFull)
                $Pending.Push($ChildFull)
            } else {
                $Files.Add($ChildFull)
            }
        }
    }
    return [pscustomobject]@{
        root = $Root
        directories = [string[]]$Directories.ToArray()
        files = [string[]]$Files.ToArray()
    }
}
function Test-RecoveryIntegral($Value) {
    return ($Value -is [sbyte] -or $Value -is [byte] -or
        $Value -is [int16] -or $Value -is [uint16] -or
        $Value -is [int] -or $Value -is [uint32] -or
        $Value -is [long] -or $Value -is [uint64])
}
function Assert-RecoveryExactProperties($Value, [string[]]$Expected, [string]$Context) {
    if ($Value -isnot [pscustomobject] -or
        (@($Value.PSObject.Properties.Name) -join '|') -cne ($Expected -join '|')) {
        throw ('NEEDS_CONTEXT: exact property contract failed: ' + $Context)
    }
}
function Get-RecoveryRawJsonObjectKeys([string]$Json, [string]$Context) {
    $Stack = New-Object 'System.Collections.Generic.Stack[object]'
    $Keys = New-Object 'System.Collections.Generic.List[string]'
    for ($Index = 0; $Index -lt $Json.Length; $Index++) {
        $Character = $Json[$Index]
        if ($Character -eq '{') {
            $Stack.Push((New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::Ordinal)))
        } elseif ($Character -eq '[') {
            $Stack.Push($null)
        } elseif ($Character -eq '}' -or $Character -eq ']') {
            if ($Stack.Count -eq 0) { throw ('NEEDS_CONTEXT: unbalanced JSON ' + $Context) }
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
                if ($Stack.Count -eq 0 -or $null -eq $Stack.Peek()) {
                    throw ('NEEDS_CONTEXT: key outside object ' + $Context)
                }
                $Token = $Json.Substring($Start, $Index - $Start + 1)
                $Key = [string]($Token | ConvertFrom-Json -ErrorAction Stop)
                if (-not $Stack.Peek().Add($Key)) {
                    throw ('NEEDS_CONTEXT: duplicate JSON key ' + $Key + ' ' + $Context)
                }
                [void]$Keys.Add($Key)
            }
        }
    }
    if ($Stack.Count -ne 0) { throw ('NEEDS_CONTEXT: unbalanced JSON containers ' + $Context) }
    return $Keys.ToArray()
}
function Read-RecoveryStrictJson([string]$Path, [string]$Context) {
    [void](Assert-RecoveryNoReparsePathComponents $Path ('strict JSON ' + $Context))
    $Item = Get-Item -LiteralPath $Path -Force -ErrorAction Stop
    if ($Item.PSIsContainer -or (($Item.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0)) {
        throw ('NEEDS_CONTEXT: JSON is not an ordinary file: ' + $Context)
    }
    $Raw = [IO.File]::ReadAllBytes($Item.FullName)
    if ($Raw.Length -eq 0 -or
        ($Raw.Length -ge 3 -and $Raw[0] -eq 0xEF -and $Raw[1] -eq 0xBB -and $Raw[2] -eq 0xBF)) {
        throw ('NEEDS_CONTEXT: empty/BOM JSON ' + $Context)
    }
    $Text = $StrictUtf8.GetString($Raw)
    if ($Text.Contains([char]0xFFFD) -or $Text.Contains([char]0) -or
        $Text.Contains("`r") -or -not $Text.EndsWith("`n", [StringComparison]::Ordinal)) {
        throw ('NEEDS_CONTEXT: noncanonical UTF-8/LF JSON ' + $Context)
    }
    [void](Get-RecoveryRawJsonObjectKeys $Text $Context)
    return ($Text | ConvertFrom-Json -ErrorAction Stop)
}
function New-RecoveryCreateOnlyUtf8File([string]$Path, [string]$Text) {
    if (-not $Text.EndsWith("`n", [StringComparison]::Ordinal) -or $Text.Contains("`r")) {
        throw ('NEEDS_CONTEXT: create-only text is not LF-only with final LF: ' + $Path)
    }
    $Payload = $StrictUtf8.GetBytes($Text)
    $Stream = New-Object IO.FileStream -ArgumentList @(
        $Path, [IO.FileMode]::CreateNew, [IO.FileAccess]::Write,
        [IO.FileShare]::None, 4096, [IO.FileOptions]::WriteThrough
    )
    try {
        $Stream.Write($Payload, 0, $Payload.Length)
        $Stream.Flush($true)
    } finally {
        $Stream.Dispose()
    }
}
function New-RecoveryFileSeal([string]$Path) {
    $Full = Get-RecoveryCanonicalPath $Path
    [void](Assert-RecoveryNoReparsePathComponents $Full 'file seal')
    $Item = Get-Item -LiteralPath $Full -Force -ErrorAction Stop
    if ($Item.PSIsContainer -or (($Item.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0)) {
        throw ('NEEDS_CONTEXT: expected ordinary leaf: ' + $Full)
    }
    return [pscustomobject][ordered]@{
        path = $Full
        bytes = [int64]$Item.Length
        sha256 = (Get-FileHash -LiteralPath $Full -Algorithm SHA256).Hash
    }
}
function Get-RecoverySha256ForBytes([byte[]]$Bytes) {
    $Hasher = [Security.Cryptography.SHA256]::Create()
    try {
        return [BitConverter]::ToString($Hasher.ComputeHash($Bytes)).Replace('-', '')
    } finally {
        $Hasher.Dispose()
    }
}

if ((& git rev-parse HEAD^).Trim() -cne $S3 -or
    (& git rev-parse ($S3 + '^')).Trim() -cne $P2 -or
    (git log -1 --format=%s) -cne 'docs: plan terminal collapse generator recovery v3') {
    throw 'NEEDS_CONTEXT: P2 -> S3 -> P3 direct-parent topology failed.'
}
$P3Paths = @(git diff-tree --no-commit-id --name-only -r $P3)
$S3Paths = @(git diff-tree --no-commit-id --name-only -r $S3)
if ($P3Paths.Count -ne 1 -or $P3Paths[0] -cne $PlanPath -or
    $S3Paths.Count -ne 1 -or $S3Paths[0] -cne $SpecPath) {
    throw 'NEEDS_CONTEXT: S3 or P3 is not an exact single-path commit.'
}
foreach ($Commit in @($P2, $S3, $P3)) {
    if ((& git rev-parse ($Commit + ':game')).Trim() -cne $GameTree) {
        throw ('NEEDS_CONTEXT: game tree drifted at ' + $Commit)
    }
}
$PlanItem = Get-Item -LiteralPath $PlanPath -Force -ErrorAction Stop
$SpecItem = Get-Item -LiteralPath $SpecPath -Force -ErrorAction Stop
$PlanSha256 = (Get-FileHash -LiteralPath $PlanPath -Algorithm SHA256).Hash
$PlanBlob = (& git hash-object --no-filters -- $PlanPath).Trim()
$CommittedPlanBlob = (& git rev-parse ($P3 + ':' + $PlanPath)).Trim()
$PhysicalSpecBlob = (& git hash-object --no-filters -- $SpecPath).Trim()
$CommittedSpecBlob = (& git rev-parse ($S3 + ':' + $SpecPath)).Trim()
if ($PlanItem.Length -le 0 -or $PlanSha256 -cnotmatch '^[0-9A-F]{64}$' -or
    $PlanBlob -cne $CommittedPlanBlob -or
    $SpecItem.Length -ne $SpecBytes -or
    (Get-FileHash -LiteralPath $SpecPath -Algorithm SHA256).Hash -cne $SpecSha256 -or
    $PhysicalSpecBlob -cne $SpecBlob -or $CommittedSpecBlob -cne $SpecBlob) {
    throw 'NEEDS_CONTEXT: physical plan/spec bytes do not equal reviewed Git blobs.'
}
if ((Get-FileHash -LiteralPath $WinterPlan -Algorithm SHA256).Hash -cne $WinterSha256 -or
    @(git diff --cached --name-only).Count -ne 0 -or
    (@(git status --short --untracked-files=all) -join '|') -cne ('?? ' + $WinterPlan)) {
    throw 'NEEDS_CONTEXT: protected shared worktree state drifted before sealing.'
}
if (Test-Path -LiteralPath $RecoveryRoot) {
    throw 'NEEDS_CONTEXT: recovery-v3 root already exists; preserve it and do not retry.'
}
if (Test-Path -LiteralPath $ApprovalLockPath) {
    throw 'NEEDS_CONTEXT: v3 approval lock already exists; preserve it and do not retry.'
}
if (-not (Test-Path -LiteralPath $V2LockPath -PathType Leaf) -or
    (Get-Item -LiteralPath $V2LockPath -Force).Length -ne 1957 -or
    (Get-FileHash -LiteralPath $V2LockPath -Algorithm SHA256).Hash -cne '592E9F1FD5C4996A8612005BE9A33A35721A63228AAB43811208099265AECF8B' -or
    -not (Get-Item -LiteralPath $V2LockPath -Force).IsReadOnly) {
    throw 'NEEDS_CONTEXT: immutable v2 lock seal drifted.'
}

[pscustomobject]@{
    status = 'PASS'
    authority_chain = ($P2 + ' -> ' + $S3 + ' -> ' + $P3)
    plan_bytes = [int64]$PlanItem.Length
    plan_sha256 = $PlanSha256
    helper_or_renpy_launches = 0
}
```

Expected: `PASS`; P3 is the reviewed single-plan child of S3, S3 is the single-spec child of P2, all three `game/` trees match, the protected winter file is the only shared status entry, and both v3 authority paths are absent. No execution ledger or process is created.

- [ ] **Seal Step 2: Reconstruct, publish, and freeze the exact schema-v2 115-leaf predecessor manifest**

Continue in the same controller session. The three catalog digests below freeze every relative path, byte count, and SHA-256 in the two v2 runtime inventories; they are not values to update from current enumeration.

```powershell
function Get-RecoveryRelativeSeal([string]$Root, [string]$RelativePath) {
    $CanonicalRoot = Get-RecoveryCanonicalPath $Root
    if ([IO.Path]::IsPathRooted($RelativePath) -or
        [string]::IsNullOrWhiteSpace($RelativePath) -or
        $RelativePath.Contains('/') -or $RelativePath.Contains([char]0)) {
        throw ('NEEDS_CONTEXT: invalid relative inventory path: ' + $RelativePath)
    }
    $Full = Get-RecoveryCanonicalPath (Join-Path $CanonicalRoot $RelativePath)
    $Prefix = $CanonicalRoot + [IO.Path]::DirectorySeparatorChar
    if (-not $Full.StartsWith($Prefix, [StringComparison]::OrdinalIgnoreCase) -or
        $Full.Substring($Prefix.Length) -cne $RelativePath) {
        throw ('NEEDS_CONTEXT: noncanonical or out-of-root inventory path: ' + $RelativePath)
    }
    [void](Assert-RecoveryNoReparsePathComponents $Full ('relative inventory leaf ' + $RelativePath))
    $Seal = New-RecoveryFileSeal $Full
    return [pscustomobject][ordered]@{
        relative_path = $RelativePath
        bytes = [int64]$Seal.bytes
        sha256 = [string]$Seal.sha256
    }
}
function Sort-RecoveryStringsOrdinal([string[]]$Values) {
    $Copy = [string[]]$Values.Clone()
    [Array]::Sort($Copy, [StringComparer]::Ordinal)
    return $Copy
}
function Get-RecoveryRelativeCatalog($Entries) {
    $Rows = New-Object 'System.Collections.Generic.List[string]'
    foreach ($Entry in @($Entries)) {
        Assert-RecoveryExactProperties $Entry @('relative_path','bytes','sha256') 'relative inventory leaf'
        $Rows.Add(([string]$Entry.relative_path + [char]9 + [string]$Entry.bytes + [char]9 + [string]$Entry.sha256))
    }
    $Text = ($Rows -join "`n") + "`n"
    $Bytes = $StrictUtf8.GetBytes($Text)
    return [pscustomobject]@{
        count = @($Entries).Count
        bytes = $Bytes.Length
        sha256 = Get-RecoverySha256ForBytes $Bytes
    }
}
function Assert-RecoveryCurrentRelativeInventory(
    [string]$Root,
    $Entries,
    [int]$ExpectedCount,
    [int]$ExpectedCatalogBytes,
    [string]$ExpectedCatalogSha256,
    [string]$Context
) {
    if (@($Entries).Count -ne $ExpectedCount) {
        throw ('NEEDS_CONTEXT: inventory count failed: ' + $Context)
    }
    $Seen = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
    $Paths = New-Object 'System.Collections.Generic.List[string]'
    foreach ($Entry in @($Entries)) {
        Assert-RecoveryExactProperties $Entry @('relative_path','bytes','sha256') $Context
        if ($Entry.relative_path -isnot [string] -or
            -not $Seen.Add([string]$Entry.relative_path) -or
            -not (Test-RecoveryIntegral $Entry.bytes) -or [int64]$Entry.bytes -lt 0 -or
            $Entry.sha256 -isnot [string] -or $Entry.sha256 -cnotmatch '^[0-9A-F]{64}$') {
            throw ('NEEDS_CONTEXT: inventory shape failed: ' + $Context)
        }
        $Current = Get-RecoveryRelativeSeal $Root ([string]$Entry.relative_path)
        if ([int64]$Current.bytes -ne [int64]$Entry.bytes -or
            [string]$Current.sha256 -cne [string]$Entry.sha256) {
            throw ('NEEDS_CONTEXT: inventory seal drifted: ' + [string]$Entry.relative_path)
        }
        $Paths.Add([string]$Entry.relative_path)
    }
    $SortedPaths = Sort-RecoveryStringsOrdinal $Paths.ToArray()
    if (($SortedPaths -join "`n") -cne ($Paths.ToArray() -join "`n")) {
        throw ('NEEDS_CONTEXT: inventory is not Ordinal-sorted: ' + $Context)
    }
    $Catalog = Get-RecoveryRelativeCatalog $Entries
    if ($Catalog.count -ne $ExpectedCount -or $Catalog.bytes -ne $ExpectedCatalogBytes -or
        $Catalog.sha256 -cne $ExpectedCatalogSha256) {
        throw ('NEEDS_CONTEXT: frozen inventory catalog failed: ' + $Context)
    }
}

# Strictly reuse the already-frozen 83-leaf v2 predecessor manifest.
if (-not (Test-Path -LiteralPath $V2ManifestPath -PathType Leaf) -or
    (Get-Item -LiteralPath $V2ManifestPath -Force).Length -ne 33555 -or
    (Get-FileHash -LiteralPath $V2ManifestPath -Algorithm SHA256).Hash -cne '903E1F66E476EA3B2E0AA60103E2230B45A500EF46C8EF6418A87084F426F9EB' -or
    -not (Get-Item -LiteralPath $V2ManifestPath -Force).IsReadOnly) {
    throw 'NEEDS_CONTEXT: v2 predecessor manifest seal drifted.'
}
$V2Manifest = Read-RecoveryStrictJson $V2ManifestPath 'v2 predecessor manifest'
Assert-RecoveryExactProperties $V2Manifest @(
    'schema_version','purpose','predecessor_plan_commit','predecessor_lock_sha256',
    'artifact_count','catalog_bytes','catalog_sha256','artifacts','failed_generator','created_utc'
) 'v2 predecessor manifest'
if ($V2Manifest.schema_version -isnot [int] -or $V2Manifest.schema_version -ne 1 -or
    $V2Manifest.artifact_count -isnot [int] -or $V2Manifest.artifact_count -ne 83 -or
    @($V2Manifest.artifacts).Count -ne 83 -or
    $V2Manifest.catalog_bytes -isnot [int] -or $V2Manifest.catalog_bytes -ne 17959 -or
    $V2Manifest.catalog_sha256 -isnot [string] -or
    $V2Manifest.catalog_sha256 -cne '4358AFED212D66C3F0BD50F26F01DEC37BF4061139C5A22EEF79FA38948C80D6') {
    throw 'NEEDS_CONTEXT: v2 predecessor manifest top-level contract failed.'
}
$V2ArtifactPaths = New-Object 'System.Collections.Generic.List[string]'
$V2CatalogRows = New-Object 'System.Collections.Generic.List[string]'
$V2Seen = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
foreach ($Artifact in @($V2Manifest.artifacts)) {
    Assert-RecoveryExactProperties $Artifact @('path','bytes','sha256') 'v2 predecessor artifact'
    $ArtifactPath = if ($Artifact.path -is [string]) { [string]$Artifact.path } else { '' }
    if (-not [IO.Path]::IsPathRooted($ArtifactPath) -or
        (Get-RecoveryCanonicalPath $ArtifactPath) -cne $ArtifactPath -or
        -not $V2Seen.Add($ArtifactPath) -or
        -not (Test-RecoveryIntegral $Artifact.bytes) -or [int64]$Artifact.bytes -lt 0 -or
        $Artifact.sha256 -isnot [string] -or $Artifact.sha256 -cnotmatch '^[0-9A-F]{64}$') {
        throw ('NEEDS_CONTEXT: v2 predecessor artifact shape failed: ' + $ArtifactPath)
    }
    $Current = New-RecoveryFileSeal $ArtifactPath
    if ([int64]$Current.bytes -ne [int64]$Artifact.bytes -or
        [string]$Current.sha256 -cne [string]$Artifact.sha256) {
        throw ('NEEDS_CONTEXT: v2 predecessor artifact drifted: ' + $ArtifactPath)
    }
    $V2ArtifactPaths.Add($ArtifactPath)
    $V2CatalogRows.Add(($ArtifactPath + [char]9 + [string]$Artifact.bytes + [char]9 + [string]$Artifact.sha256))
}
$V2SortedPaths = Sort-RecoveryStringsOrdinal $V2ArtifactPaths.ToArray()
if (($V2SortedPaths -join "`n") -cne ($V2ArtifactPaths.ToArray() -join "`n")) {
    throw 'NEEDS_CONTEXT: v2 predecessor artifacts are not Ordinal-sorted.'
}
$V2CatalogBytes = $StrictUtf8.GetBytes(($V2CatalogRows -join "`n") + "`n")
if ($V2CatalogBytes.Length -ne 17959 -or
    (Get-RecoverySha256ForBytes $V2CatalogBytes) -cne '4358AFED212D66C3F0BD50F26F01DEC37BF4061139C5A22EEF79FA38948C80D6') {
    throw 'NEEDS_CONTEXT: v2 predecessor catalog reconstruction failed.'
}

# Prove and freeze the exact v2 generator worktree task-owned inventory.
$V2WorktreeTree = Get-RecoveryNonFollowingTree $V2GeneratorWorktree 'v2 generator worktree'
$V2WorktreeDirectorySet = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
$V2WorktreeFileSet = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
foreach ($Path in $V2WorktreeTree.directories) { [void]$V2WorktreeDirectorySet.Add($Path) }
foreach ($Path in $V2WorktreeTree.files) { [void]$V2WorktreeFileSet.Add($Path) }
$V2GamePath = Get-RecoveryCanonicalPath (Join-Path $V2GeneratorWorktree 'game')
$V2SavesPath = Get-RecoveryCanonicalPath (Join-Path $V2GamePath 'saves')
$V2CachePath = Get-RecoveryCanonicalPath (Join-Path $V2GamePath 'cache')
foreach ($Path in @($V2GamePath, $V2SavesPath, $V2CachePath)) {
    [void](Assert-RecoveryNoReparsePathComponents $Path 'v2 task-owned intermediate directory')
    if (-not $V2WorktreeDirectorySet.Contains($Path)) {
        throw ('NEEDS_CONTEXT: v2 task-owned intermediate directory is missing: ' + $Path)
    }
}
foreach ($DirectoryPath in $V2WorktreeTree.directories) {
    if ($DirectoryPath.StartsWith($V2SavesPath + '\', [StringComparison]::OrdinalIgnoreCase) -or
        $DirectoryPath.StartsWith($V2CachePath + '\', [StringComparison]::OrdinalIgnoreCase)) {
        throw ('NEEDS_CONTEXT: extra directory appeared below a task-owned subtree: ' + $DirectoryPath)
    }
}
if ((& git -C $V2GeneratorWorktree rev-parse HEAD).Trim() -cne $P2 -or
    (& git -C $V2GeneratorWorktree rev-parse HEAD:game).Trim() -cne $GameTree) {
    throw 'NEEDS_CONTEXT: preserved v2 generator worktree topology drifted.'
}
& git -C $V2GeneratorWorktree diff --quiet --
if ($LASTEXITCODE -ne 0) { throw 'NEEDS_CONTEXT: v2 generator worktree tracked files drifted.' }
& git -C $V2GeneratorWorktree diff --cached --quiet --
if ($LASTEXITCODE -ne 0) { throw 'NEEDS_CONTEXT: v2 generator worktree index is not empty.' }
$V2Untracked = @(& git -C $V2GeneratorWorktree ls-files --others --exclude-standard)
if ($LASTEXITCODE -ne 0 -or ($V2Untracked -join '|') -cne 'game/zz_terminal_collapse_legacy_fixture.rpy') {
    throw 'NEEDS_CONTEXT: v2 generator worktree untracked inventory drifted.'
}
$WorktreeAuthorityRelative = [string[]]@(
    'game\saves\1-1-LT1.save',
    'game\saves\auto-1-LT1.save',
    'game\saves\auto-2-LT1.save',
    'game\saves\auto-3-LT1.save',
    'game\saves\auto-4-LT1.save',
    'game\saves\persistent',
    'game\zz_terminal_collapse_legacy_fixture.rpy',
    'log.txt'
)
$WorktreeAuthorityRelative = Sort-RecoveryStringsOrdinal $WorktreeAuthorityRelative
$WorktreeAuthorityFiles = New-Object 'System.Collections.Generic.List[object]'
foreach ($Relative in $WorktreeAuthorityRelative) {
    $WorktreeAuthorityFiles.Add((Get-RecoveryRelativeSeal $V2GeneratorWorktree $Relative))
}
Assert-RecoveryCurrentRelativeInventory $V2GeneratorWorktree $WorktreeAuthorityFiles.ToArray() 8 777 '37976165E24FA53CC4DE33AC8D0B9B3DA0545925184FD3D4F088039292FE1723' 'v2 worktree authority'

$IgnoredRelative = New-Object 'System.Collections.Generic.List[string]'
foreach ($GitRelative in @(& git -C $V2GeneratorWorktree ls-files --others --ignored --exclude-standard)) {
    $IgnoredRelative.Add(([string]$GitRelative).Replace('/', '\'))
}
if ($LASTEXITCODE -ne 0) { throw 'NEEDS_CONTEXT: could not enumerate v2 ignored runtime files.' }
$ExpectedIgnoredAuthority = [string[]]@(
    'game\saves\1-1-LT1.save','game\saves\auto-1-LT1.save','game\saves\auto-2-LT1.save',
    'game\saves\auto-3-LT1.save','game\saves\auto-4-LT1.save','game\saves\persistent','log.txt'
)
$ExpectedIgnoredSet = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
foreach ($Relative in $ExpectedIgnoredAuthority) { [void]$ExpectedIgnoredSet.Add($Relative) }
$ExcludedRelative = New-Object 'System.Collections.Generic.List[string]'
foreach ($Relative in $IgnoredRelative) {
    if (-not $ExpectedIgnoredSet.Contains($Relative)) { $ExcludedRelative.Add($Relative) }
}
$ExcludedSorted = Sort-RecoveryStringsOrdinal $ExcludedRelative.ToArray()
if ($IgnoredRelative.Count -ne 68 -or $ExcludedSorted.Count -ne 61) {
    throw 'NEEDS_CONTEXT: v2 ignored authority/cache cardinality drifted.'
}
foreach ($Relative in $ExcludedSorted) {
    $IsRpyc = $Relative.StartsWith('game\', [StringComparison]::Ordinal) -and
        $Relative.EndsWith('.rpyc', [StringComparison]::Ordinal)
    $IsCache = $Relative.StartsWith('game\cache\', [StringComparison]::Ordinal) -and
        $Relative.EndsWith('.rpyb', [StringComparison]::Ordinal)
    if (-not ($IsRpyc -or $IsCache)) {
        throw ('NEEDS_CONTEXT: non-cache file appeared in excluded inventory: ' + $Relative)
    }
}
$WorktreeExcludedFiles = New-Object 'System.Collections.Generic.List[object]'
foreach ($Relative in $ExcludedSorted) {
    $WorktreeExcludedFiles.Add((Get-RecoveryRelativeSeal $V2GeneratorWorktree $Relative))
}
Assert-RecoveryCurrentRelativeInventory $V2GeneratorWorktree $WorktreeExcludedFiles.ToArray() 61 5732 'D7E59DED729100143D7763ABEA1A90DD1632E55B7EB3AEB1D26F968AF0C9A99B' 'v2 worktree excluded cache'
foreach ($Leaf in @($WorktreeAuthorityFiles.ToArray()) + @($WorktreeExcludedFiles.ToArray())) {
    $Full = Get-RecoveryCanonicalPath (Join-Path $V2GeneratorWorktree ([string]$Leaf.relative_path))
    [void](Assert-RecoveryNoReparsePathComponents $Full 'v2 task-owned inventory leaf')
    if (-not $V2WorktreeFileSet.Contains($Full)) {
        throw ('NEEDS_CONTEXT: task-owned inventory leaf is absent from safe non-following traversal: ' + $Full)
    }
}
$ExpectedTaskOwnedSubtreeFiles = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
foreach ($Leaf in @($WorktreeAuthorityFiles.ToArray()) + @($WorktreeExcludedFiles.ToArray())) {
    $Full = Get-RecoveryCanonicalPath (Join-Path $V2GeneratorWorktree ([string]$Leaf.relative_path))
    if ($Full.StartsWith($V2SavesPath + '\', [StringComparison]::OrdinalIgnoreCase) -or
        $Full.StartsWith($V2CachePath + '\', [StringComparison]::OrdinalIgnoreCase)) {
        [void]$ExpectedTaskOwnedSubtreeFiles.Add($Full)
    }
}
$ActualTaskOwnedSubtreeFiles = @($V2WorktreeTree.files | Where-Object {
    $_.StartsWith($V2SavesPath + '\', [StringComparison]::OrdinalIgnoreCase) -or
    $_.StartsWith($V2CachePath + '\', [StringComparison]::OrdinalIgnoreCase)
})
if ($ActualTaskOwnedSubtreeFiles.Count -ne $ExpectedTaskOwnedSubtreeFiles.Count) {
    throw 'NEEDS_CONTEXT: extra or missing leaf appeared below a v2 task-owned subtree.'
}
foreach ($Full in $ActualTaskOwnedSubtreeFiles) {
    if (-not $ExpectedTaskOwnedSubtreeFiles.Contains($Full)) {
        throw ('NEEDS_CONTEXT: extra leaf appeared below a v2 task-owned subtree: ' + $Full)
    }
}

# Prove and freeze the exact v2 external SaveDir inventory.
$V2SaveTree = Get-RecoveryNonFollowingTree $V2GeneratorSaveDir 'v2 generator SaveDir'
$V2SaveDirectories = @($V2SaveTree.directories | Where-Object { $_ -cne (Get-RecoveryCanonicalPath $V2GeneratorSaveDir) })
$V2SaveFiles = [string[]]$V2SaveTree.files
if ($V2SaveDirectories.Count -ne 1 -or
    $V2SaveDirectories[0].Substring($V2GeneratorSaveDir.Length + 1) -cne 'sync' -or
    $V2SaveFiles.Count -ne 12) {
    throw 'NEEDS_CONTEXT: v2 generator SaveDir structure drifted.'
}
$SaveRelative = New-Object 'System.Collections.Generic.List[string]'
foreach ($File in $V2SaveFiles) {
    $SaveRelative.Add($File.Substring($V2GeneratorSaveDir.Length + 1))
}
$SaveSorted = Sort-RecoveryStringsOrdinal $SaveRelative.ToArray()
$SaveAuthorityFiles = New-Object 'System.Collections.Generic.List[object]'
foreach ($Relative in $SaveSorted) {
    $SaveAuthorityFiles.Add((Get-RecoveryRelativeSeal $V2GeneratorSaveDir $Relative))
}
Assert-RecoveryCurrentRelativeInventory $V2GeneratorSaveDir $SaveAuthorityFiles.ToArray() 12 1066 'DD3A6C77E61922681CE3788E6BBA0883B681461A10F628D4AA3CE66E033747A4' 'v2 external SaveDir authority'

$SourceInventories = [object[]]@(
    [pscustomobject][ordered]@{
        id = 'v2_generator_worktree_task_owned'
        root_path = Get-RecoveryCanonicalPath $V2GeneratorWorktree
        authority_file_count = 8
        authority_files = [object[]]$WorktreeAuthorityFiles.ToArray()
        excluded_cache_count = 61
        excluded_cache_files = [object[]]$WorktreeExcludedFiles.ToArray()
    },
    [pscustomobject][ordered]@{
        id = 'v2_generator_savedir'
        root_path = Get-RecoveryCanonicalPath $V2GeneratorSaveDir
        authority_file_count = 12
        authority_files = [object[]]$SaveAuthorityFiles.ToArray()
        excluded_cache_count = 0
        excluded_cache_files = [object[]]@()
    }
)

# Add the exact 12 v2 authority/evidence leaves and 20 v2 runtime leaves to the inherited 83.
$V2AuthorityPaths = [string[]]@(
    (Join-Path $EvidenceRoot 'approved-plan-lock-v2.json'),
    (Join-Path $ProjectRoot 'docs\superpowers\specs\2026-08-14-terminal-collapse-generator-recovery-design.md'),
    (Join-Path $ProjectRoot 'docs\superpowers\plans\2026-08-14-terminal-collapse-generator-recovery.md'),
    (Join-Path $V2Root 'predecessor-evidence.json'),
    (Join-Path $V2Root 'generator-structure-red.json'),
    (Join-Path $V2Root 'generator-structure-green.json'),
    (Join-Path $V2Root 'generator-attempt\attempt.json'),
    (Join-Path $V2Root 'generator-state.json'),
    (Join-Path $V2Root 'generator-process\request.json'),
    (Join-Path $V2Root 'generator-process\stdout.txt'),
    (Join-Path $V2Root 'generator-process\stderr.txt'),
    (Join-Path $V2Root 'generator-process\result.json')
)
$CandidatePaths = New-Object 'System.Collections.Generic.List[string]'
foreach ($Artifact in @($V2Manifest.artifacts)) { $CandidatePaths.Add([string]$Artifact.path) }
foreach ($Path in $V2AuthorityPaths) { $CandidatePaths.Add((Get-RecoveryCanonicalPath $Path)) }
foreach ($Entry in $WorktreeAuthorityFiles) {
    $CandidatePaths.Add((Get-RecoveryCanonicalPath (Join-Path $V2GeneratorWorktree ([string]$Entry.relative_path))))
}
foreach ($Entry in $SaveAuthorityFiles) {
    $CandidatePaths.Add((Get-RecoveryCanonicalPath (Join-Path $V2GeneratorSaveDir ([string]$Entry.relative_path))))
}
if ($CandidatePaths.Count -ne 115) {
    throw ('NEEDS_CONTEXT: predecessor candidate count is not 115: ' + $CandidatePaths.Count)
}
$CandidateSeen = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
foreach ($Path in $CandidatePaths) {
    if (-not $CandidateSeen.Add($Path)) { throw ('NEEDS_CONTEXT: duplicate predecessor path: ' + $Path) }
}
$SortedCandidatePaths = Sort-RecoveryStringsOrdinal $CandidatePaths.ToArray()
$ArtifactObjects = New-Object 'System.Collections.Generic.List[object]'
$CatalogRows = New-Object 'System.Collections.Generic.List[string]'
foreach ($Path in $SortedCandidatePaths) {
    $Seal = New-RecoveryFileSeal $Path
    $ArtifactObjects.Add($Seal)
    $CatalogRows.Add(([string]$Seal.path + [char]9 + [string]$Seal.bytes + [char]9 + [string]$Seal.sha256))
}
$CatalogBytes = $StrictUtf8.GetBytes(($CatalogRows -join "`n") + "`n")
$CatalogHash = Get-RecoverySha256ForBytes $CatalogBytes
if ($CatalogBytes.Length -ne 24660 -or
    $CatalogHash -cne '9694E728A82F6DDC743DA5E83967EAC7EE02FFA62FA53E21F4A2374F27DDDA24') {
    throw ('NEEDS_CONTEXT: 115-leaf catalog drifted: ' + $CatalogBytes.Length + '/' + $CatalogHash)
}

# Freeze both failed generator lineages. Null legacy attempt fields are intentional and mandatory.
$LegacyRoot = 'E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-generator-c2958b40c6044ce598e56263855c071d'
$LegacySaveDir = 'E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-generator-save-44f1b1204d3f4222a019a2a41335d6a6'
$LegacyFailure = [pscustomobject][ordered]@{
    id = 'legacy_generator'
    classification = 'TIMEOUT'
    program_outcome = 'TIMEOUT'
    reason = 'HELPER_TIMEOUT'
    generator_invocation_count = 1
    observer_invocation_count = 0
    attempt_path = $null
    attempt_sha256 = $null
    result_path = Get-RecoveryCanonicalPath (Join-Path $EvidenceRoot 'legacy\generator-process\result.json')
    result_bytes = [int64]1716
    result_sha256 = '65A789696D25390CFC827FAA7A2C19D150B67A3EC2161AC44DFD79ADBEE57D13'
    state_path = Get-RecoveryCanonicalPath (Join-Path $EvidenceRoot 'legacy\generator-state.json')
    state_bytes = [int64]2570
    state_sha256 = '82014869E02AEB3E18B7F7D6230C6789BDA05955A345AF4B9348C13D283E79ED'
    test_report_path = Get-RecoveryCanonicalPath (Join-Path $EvidenceRoot 'legacy\generator-process\stdout.txt')
    test_report_bytes = [int64]0
    test_report_sha256 = 'E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855'
    engine_log_path = Get-RecoveryCanonicalPath (Join-Path $LegacyRoot 'log.txt')
    engine_log_bytes = [int64]0
    engine_log_sha256 = 'E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855'
    target_copies = [object[]]@(
        [pscustomobject][ordered]@{ role = 'external_root'; path = Get-RecoveryCanonicalPath (Join-Path $LegacySaveDir '1-1-LT1.save'); bytes = [int64]733069; sha256 = 'E24D04A5F71BBBC13086D68EA09C4F746A2CE2DB1C9D5865BB7769C1DF9036DB' },
        [pscustomobject][ordered]@{ role = 'external_sync'; path = Get-RecoveryCanonicalPath (Join-Path $LegacySaveDir 'sync\1-1-LT1.save'); bytes = [int64]733069; sha256 = 'E24D04A5F71BBBC13086D68EA09C4F746A2CE2DB1C9D5865BB7769C1DF9036DB' },
        [pscustomobject][ordered]@{ role = 'worktree_local'; path = Get-RecoveryCanonicalPath (Join-Path $LegacyRoot 'game\saves\1-1-LT1.save'); bytes = [int64]733069; sha256 = 'E24D04A5F71BBBC13086D68EA09C4F746A2CE2DB1C9D5865BB7769C1DF9036DB' }
    )
    candidate_save_disposition = 'preserved_not_used'
}
$V2Failure = [pscustomobject][ordered]@{
    id = 'v2_generator'
    classification = 'GOVERNANCE_CONTRACT_FAILURE'
    program_outcome = 'COMPLETED'
    reason = 'LOG_CONTRACT_MISMATCH'
    generator_invocation_count = 1
    observer_invocation_count = 0
    attempt_path = Get-RecoveryCanonicalPath (Join-Path $V2Root 'generator-attempt\attempt.json')
    attempt_sha256 = '6C6D597580E80A448C0CE55A80C0955988970C2A6332854049420B8693D38DF0'
    result_path = Get-RecoveryCanonicalPath (Join-Path $V2Root 'generator-process\result.json')
    result_bytes = [int64]1734
    result_sha256 = '12955539EC45CB4B3FA5490393EF511A851BD7CA3800F7835EBACAFFFF69D94F'
    state_path = Get-RecoveryCanonicalPath (Join-Path $V2Root 'generator-state.json')
    state_bytes = [int64]2528
    state_sha256 = '43EDEB6BDFD217A7E9CDD969564A29B472D6D0258CF83ABD106F568A5B29D652'
    test_report_path = Get-RecoveryCanonicalPath (Join-Path $V2Root 'generator-process\stdout.txt')
    test_report_bytes = [int64]1074
    test_report_sha256 = 'BD3B00124C6134FD0DAE737B293C20F68BF76F02ECDC69E77797C883FA5208CE'
    engine_log_path = Get-RecoveryCanonicalPath (Join-Path $V2GeneratorWorktree 'log.txt')
    engine_log_bytes = [int64]1860
    engine_log_sha256 = 'FE52BE91013D21B51AAF2CCDCF796289906EB4D12FA08EB1912A196B4F076A81'
    target_copies = [object[]]@(
        [pscustomobject][ordered]@{ role = 'external_root'; path = Get-RecoveryCanonicalPath (Join-Path $V2GeneratorSaveDir '1-1-LT1.save'); bytes = [int64]726209; sha256 = 'A817BBDE9A00B82A044E27C9AF93F27D99E1F106AABDE2230FFD5E8A1FAF19D7' },
        [pscustomobject][ordered]@{ role = 'external_sync'; path = Get-RecoveryCanonicalPath (Join-Path $V2GeneratorSaveDir 'sync\1-1-LT1.save'); bytes = [int64]726209; sha256 = 'A817BBDE9A00B82A044E27C9AF93F27D99E1F106AABDE2230FFD5E8A1FAF19D7' },
        [pscustomobject][ordered]@{ role = 'worktree_local'; path = Get-RecoveryCanonicalPath (Join-Path $V2GeneratorWorktree 'game\saves\1-1-LT1.save'); bytes = [int64]726209; sha256 = 'A817BBDE9A00B82A044E27C9AF93F27D99E1F106AABDE2230FFD5E8A1FAF19D7' }
    )
    candidate_save_disposition = 'preserved_not_used'
}

function Assert-RecoveryCurrentAuthorityPrepublication(
    [ValidateSet('manifest','lock')][string]$Phase,
    [string]$ReviewedManifestSha256 = ''
) {
    if ($PSVersionTable.PSEdition -cne 'Desktop' -or $PSVersionTable.PSVersion.Major -ne 5) {
        throw ('NEEDS_CONTEXT: current-authority gate requires Windows PowerShell 5.1 Desktop: ' + $Phase)
    }
    if ((& git rev-parse HEAD).Trim() -cne $P3 -or
        (& git rev-parse HEAD^).Trim() -cne $S3 -or
        (& git rev-parse ($S3 + '^')).Trim() -cne $P2 -or
        (git log -1 --format=%s) -cne 'docs: plan terminal collapse generator recovery v3' -or
        (@(git diff-tree --no-commit-id --name-only -r $P3) -join '|') -cne $PlanPath -or
        (@(git diff-tree --no-commit-id --name-only -r $S3) -join '|') -cne $SpecPath) {
        throw ('NEEDS_CONTEXT: current-authority topology failed before ' + $Phase + ' publication.')
    }
    foreach ($Commit in @($P2, $S3, $P3)) {
        if ((& git rev-parse ($Commit + ':game')).Trim() -cne $GameTree) {
            throw ('NEEDS_CONTEXT: current-authority game tree drifted before ' + $Phase + ': ' + $Commit)
        }
    }
    [void](Assert-RecoveryNoReparsePathComponents $PlanPath ('pre-' + $Phase + ' physical plan'))
    [void](Assert-RecoveryNoReparsePathComponents $SpecPath ('pre-' + $Phase + ' physical spec'))
    $CurrentPlanItem = Get-Item -LiteralPath $PlanPath -Force -ErrorAction Stop
    $CurrentPlanSha256 = (Get-FileHash -LiteralPath $PlanPath -Algorithm SHA256).Hash
    $CurrentPlanBlob = (& git hash-object --no-filters -- $PlanPath).Trim()
    $CommittedPlanBlob = (& git rev-parse ($P3 + ':' + $PlanPath)).Trim()
    $CurrentSpecBlob = (& git hash-object --no-filters -- $SpecPath).Trim()
    $CommittedSpecBlob = (& git rev-parse ($S3 + ':' + $SpecPath)).Trim()
    if ($CurrentPlanItem.Length -ne $PlanItem.Length -or $CurrentPlanSha256 -cne $PlanSha256 -or
        $CurrentPlanBlob -cne $PlanBlob -or $CommittedPlanBlob -cne $PlanBlob -or
        (Get-Item -LiteralPath $SpecPath -Force).Length -ne $SpecBytes -or
        (Get-FileHash -LiteralPath $SpecPath -Algorithm SHA256).Hash -cne $SpecSha256 -or
        $CurrentSpecBlob -cne $SpecBlob -or $CommittedSpecBlob -cne $SpecBlob) {
        throw ('NEEDS_CONTEXT: current physical/raw plan or spec drifted before ' + $Phase + ' publication.')
    }

    $ExpectedGateHelpers = [ordered]@{
        (Join-Path $EvidenceRoot 'helpers\PrivateDesktopRunner.cs') = [pscustomobject]@{ Bytes = [int64]82334; Sha256 = 'E0393DB1E113FDB8C35097978AA73B7D33AFDD5788499002B6423D883DEED4E8' }
        (Join-Path $EvidenceRoot 'helpers\Invoke-PrivateDesktopProcess.ps1') = [pscustomobject]@{ Bytes = [int64]24229; Sha256 = '73A3F9C43CF994E08F004E0A1266122A3EC5E0EAF065C63E6D9439CF0B0E1880' }
        (Join-Path $EvidenceRoot 'helpers\Test-PrivateDesktopRunner.ps1') = [pscustomobject]@{ Bytes = [int64]53188; Sha256 = '20198B669F70E51E51F71BD01E6D06D1949D300F43CE9A94FB0190A47D781A15' }
    }
    foreach ($Entry in $ExpectedGateHelpers.GetEnumerator()) {
        [void](Assert-RecoveryNoReparsePathComponents ([string]$Entry.Key) ('pre-' + $Phase + ' helper'))
        $Seal = New-RecoveryFileSeal ([string]$Entry.Key)
        if ([int64]$Seal.bytes -ne [int64]$Entry.Value.Bytes -or
            [string]$Seal.sha256 -cne [string]$Entry.Value.Sha256) {
            throw ('NEEDS_CONTEXT: helper drifted before ' + $Phase + ' publication: ' + [string]$Entry.Key)
        }
    }
    [void](Assert-RecoveryNoReparsePathComponents $V2LockPath ('pre-' + $Phase + ' v2 lock'))
    [void](Assert-RecoveryNoReparsePathComponents $V2ManifestPath ('pre-' + $Phase + ' v2 manifest'))
    if (-not (Test-Path -LiteralPath $V2LockPath -PathType Leaf) -or
        (Get-Item -LiteralPath $V2LockPath -Force).Length -ne 1957 -or
        (Get-FileHash -LiteralPath $V2LockPath -Algorithm SHA256).Hash -cne
            '592E9F1FD5C4996A8612005BE9A33A35721A63228AAB43811208099265AECF8B' -or
        -not (Get-Item -LiteralPath $V2LockPath -Force).IsReadOnly -or
        -not (Test-Path -LiteralPath $V2ManifestPath -PathType Leaf) -or
        (Get-Item -LiteralPath $V2ManifestPath -Force).Length -ne 33555 -or
        (Get-FileHash -LiteralPath $V2ManifestPath -Algorithm SHA256).Hash -cne
            '903E1F66E476EA3B2E0AA60103E2230B45A500EF46C8EF6418A87084F426F9EB' -or
        -not (Get-Item -LiteralPath $V2ManifestPath -Force).IsReadOnly) {
        throw ('NEEDS_CONTEXT: v2 lock/manifest input drifted before ' + $Phase + ' publication.')
    }

    $GateWorktreeTree = Get-RecoveryNonFollowingTree $V2GeneratorWorktree ('pre-' + $Phase + ' v2 worktree')
    $GateWorktreeDirectorySet = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
    $GateWorktreeFileSet = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
    foreach ($Path in $GateWorktreeTree.directories) { [void]$GateWorktreeDirectorySet.Add($Path) }
    foreach ($Path in $GateWorktreeTree.files) { [void]$GateWorktreeFileSet.Add($Path) }
    foreach ($Path in @($V2GamePath, $V2SavesPath, $V2CachePath)) {
        [void](Assert-RecoveryNoReparsePathComponents $Path ('pre-' + $Phase + ' task-owned intermediate'))
        if (-not $GateWorktreeDirectorySet.Contains($Path)) {
            throw ('NEEDS_CONTEXT: task-owned intermediate missing before ' + $Phase + ': ' + $Path)
        }
    }
    foreach ($DirectoryPath in $GateWorktreeTree.directories) {
        if ($DirectoryPath.StartsWith($V2SavesPath + '\', [StringComparison]::OrdinalIgnoreCase) -or
            $DirectoryPath.StartsWith($V2CachePath + '\', [StringComparison]::OrdinalIgnoreCase)) {
            throw ('NEEDS_CONTEXT: extra task-owned directory before ' + $Phase + ': ' + $DirectoryPath)
        }
    }
    if ((& git -C $V2GeneratorWorktree rev-parse HEAD).Trim() -cne $P2 -or
        (& git -C $V2GeneratorWorktree rev-parse HEAD:game).Trim() -cne $GameTree) {
        throw ('NEEDS_CONTEXT: v2 worktree topology drifted before ' + $Phase + ' publication.')
    }
    & git -C $V2GeneratorWorktree diff --quiet --
    if ($LASTEXITCODE -ne 0) {
        throw ('NEEDS_CONTEXT: v2 worktree tracked files drifted before ' + $Phase + ' publication.')
    }
    & git -C $V2GeneratorWorktree diff --cached --quiet --
    if ($LASTEXITCODE -ne 0) {
        throw ('NEEDS_CONTEXT: v2 worktree index drifted before ' + $Phase + ' publication.')
    }
    $GateUntracked = @(& git -C $V2GeneratorWorktree ls-files --others --exclude-standard)
    if ($LASTEXITCODE -ne 0 -or
        ($GateUntracked -join '|') -cne 'game/zz_terminal_collapse_legacy_fixture.rpy') {
        throw ('NEEDS_CONTEXT: v2 worktree untracked inventory drifted before ' + $Phase + ' publication.')
    }
    $GateExpectedIgnored = New-Object 'System.Collections.Generic.List[string]'
    foreach ($Leaf in @($WorktreeAuthorityFiles.ToArray())) {
        if ([string]$Leaf.relative_path -cne 'game\zz_terminal_collapse_legacy_fixture.rpy') {
            $GateExpectedIgnored.Add(([string]$Leaf.relative_path).Replace('\', '/'))
        }
    }
    foreach ($Leaf in @($WorktreeExcludedFiles.ToArray())) {
        $GateExpectedIgnored.Add(([string]$Leaf.relative_path).Replace('\', '/'))
    }
    $GateExpectedIgnoredSorted = Sort-RecoveryStringsOrdinal $GateExpectedIgnored.ToArray()
    $GateActualIgnored = [string[]]@(& git -C $V2GeneratorWorktree ls-files --others --ignored --exclude-standard)
    if ($LASTEXITCODE -ne 0) {
        throw ('NEEDS_CONTEXT: v2 ignored inventory enumeration failed before ' + $Phase + ' publication.')
    }
    $GateActualIgnored = Sort-RecoveryStringsOrdinal $GateActualIgnored
    if ($GateActualIgnored.Count -ne 68 -or
        ($GateActualIgnored -join "`n") -cne ($GateExpectedIgnoredSorted -join "`n")) {
        throw ('NEEDS_CONTEXT: v2 ignored authority/cache set drifted before ' + $Phase + ' publication.')
    }
    Assert-RecoveryCurrentRelativeInventory $V2GeneratorWorktree $WorktreeAuthorityFiles.ToArray() 8 777 '37976165E24FA53CC4DE33AC8D0B9B3DA0545925184FD3D4F088039292FE1723' ('pre-' + $Phase + ' v2 worktree authority')
    Assert-RecoveryCurrentRelativeInventory $V2GeneratorWorktree $WorktreeExcludedFiles.ToArray() 61 5732 'D7E59DED729100143D7763ABEA1A90DD1632E55B7EB3AEB1D26F968AF0C9A99B' ('pre-' + $Phase + ' v2 worktree excluded cache')
    foreach ($Leaf in @($WorktreeAuthorityFiles.ToArray()) + @($WorktreeExcludedFiles.ToArray())) {
        $Full = Get-RecoveryCanonicalPath (Join-Path $V2GeneratorWorktree ([string]$Leaf.relative_path))
        if (-not $GateWorktreeFileSet.Contains($Full)) {
            throw ('NEEDS_CONTEXT: safe worktree traversal lost task-owned leaf before ' + $Phase + ': ' + $Full)
        }
    }
    $GateExpectedTaskOwnedFiles = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
    foreach ($Leaf in @($WorktreeAuthorityFiles.ToArray()) + @($WorktreeExcludedFiles.ToArray())) {
        $Full = Get-RecoveryCanonicalPath (Join-Path $V2GeneratorWorktree ([string]$Leaf.relative_path))
        if ($Full.StartsWith($V2SavesPath + '\', [StringComparison]::OrdinalIgnoreCase) -or
            $Full.StartsWith($V2CachePath + '\', [StringComparison]::OrdinalIgnoreCase)) {
            [void]$GateExpectedTaskOwnedFiles.Add($Full)
        }
    }
    $GateActualTaskOwnedFiles = @($GateWorktreeTree.files | Where-Object {
        $_.StartsWith($V2SavesPath + '\', [StringComparison]::OrdinalIgnoreCase) -or
        $_.StartsWith($V2CachePath + '\', [StringComparison]::OrdinalIgnoreCase)
    })
    if ($GateActualTaskOwnedFiles.Count -ne $GateExpectedTaskOwnedFiles.Count) {
        throw ('NEEDS_CONTEXT: extra or missing task-owned leaf before ' + $Phase + ' publication.')
    }
    foreach ($Full in $GateActualTaskOwnedFiles) {
        if (-not $GateExpectedTaskOwnedFiles.Contains($Full)) {
            throw ('NEEDS_CONTEXT: extra task-owned leaf before ' + $Phase + ': ' + $Full)
        }
    }
    $GateSaveTree = Get-RecoveryNonFollowingTree $V2GeneratorSaveDir ('pre-' + $Phase + ' v2 SaveDir')
    $GateSaveDirectories = @($GateSaveTree.directories | Where-Object { $_ -cne (Get-RecoveryCanonicalPath $V2GeneratorSaveDir) })
    if ($GateSaveDirectories.Count -ne 1 -or
        $GateSaveDirectories[0].Substring($V2GeneratorSaveDir.Length + 1) -cne 'sync' -or
        $GateSaveTree.files.Count -ne 12) {
        throw ('NEEDS_CONTEXT: v2 SaveDir safe structure drifted before ' + $Phase + ' publication.')
    }
    Assert-RecoveryCurrentRelativeInventory $V2GeneratorSaveDir $SaveAuthorityFiles.ToArray() 12 1066 'DD3A6C77E61922681CE3788E6BBA0883B681461A10F628D4AA3CE66E033747A4' ('pre-' + $Phase + ' v2 SaveDir authority')
    $GateExpectedSaveRelative = [string[]]@($SaveAuthorityFiles.ToArray() | ForEach-Object { [string]$_.relative_path })
    $GateActualSaveRelative = [string[]]@($GateSaveTree.files | ForEach-Object {
        $_.Substring($V2GeneratorSaveDir.Length + 1)
    })
    $GateExpectedSaveRelative = Sort-RecoveryStringsOrdinal $GateExpectedSaveRelative
    $GateActualSaveRelative = Sort-RecoveryStringsOrdinal $GateActualSaveRelative
    if (($GateActualSaveRelative -join "`n") -cne ($GateExpectedSaveRelative -join "`n")) {
        throw ('NEEDS_CONTEXT: v2 SaveDir exact leaf set drifted before ' + $Phase + ' publication.')
    }

    $GateRows = New-Object 'System.Collections.Generic.List[string]'
    $GateSeen = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
    if ($SortedCandidatePaths.Count -ne 115) {
        throw ('NEEDS_CONTEXT: current candidate cardinality failed before ' + $Phase + ' publication.')
    }
    foreach ($Path in $SortedCandidatePaths) {
        $Seal = New-RecoveryFileSeal $Path
        if (-not $GateSeen.Add([string]$Seal.path)) {
            throw ('NEEDS_CONTEXT: duplicate current candidate before ' + $Phase + ': ' + [string]$Seal.path)
        }
        $GateRows.Add(([string]$Seal.path + [char]9 + [string]$Seal.bytes + [char]9 + [string]$Seal.sha256))
    }
    $GateCatalog = $StrictUtf8.GetBytes(($GateRows -join "`n") + "`n")
    if ($GateCatalog.Length -ne 24660 -or
        (Get-RecoverySha256ForBytes $GateCatalog) -cne
            '9694E728A82F6DDC743DA5E83967EAC7EE02FFA62FA53E21F4A2374F27DDDA24') {
        throw ('NEEDS_CONTEXT: current 115-leaf catalog failed before ' + $Phase + ' publication.')
    }

    [void](Assert-RecoveryNoReparsePathComponents $WinterPlan ('pre-' + $Phase + ' protected winter plan'))
    if ((Get-FileHash -LiteralPath $WinterPlan -Algorithm SHA256).Hash -cne $WinterSha256 -or
        @(git diff --cached --name-only).Count -ne 0 -or
        (@(git status --short --untracked-files=all) -join '|') -cne ('?? ' + $WinterPlan)) {
        throw ('NEEDS_CONTEXT: winter/index/status drifted before ' + $Phase + ' publication.')
    }
    [void](Assert-RecoveryNoReparsePathComponents $EvidenceRoot ('pre-' + $Phase + ' evidence root'))
    foreach ($Destination in @($ManifestPath, $ApprovalLockPath)) {
        & git check-ignore -q -- $Destination
        if ($LASTEXITCODE -ne 0) {
            throw ('NEEDS_CONTEXT: ignored destination gate failed before ' + $Phase + ': ' + $Destination)
        }
    }
    if (Test-Path -LiteralPath $ApprovalLockPath) {
        throw ('NEEDS_CONTEXT: approval lock exists before its ' + $Phase + ' prepublication gate.')
    }

    if ($Phase -ceq 'manifest') {
        if (Test-Path -LiteralPath $ManifestPath) {
            throw 'NEEDS_CONTEXT: predecessor manifest exists before manifest CreateNew.'
        }
        $EmptyRecoveryTree = Get-RecoveryNonFollowingTree $RecoveryRoot 'pre-manifest empty recovery-v3 root'
        if ($EmptyRecoveryTree.directories.Count -ne 1 -or $EmptyRecoveryTree.files.Count -ne 0) {
            throw 'NEEDS_CONTEXT: recovery-v3 root is not empty before manifest CreateNew.'
        }
        return
    }

    [void](Assert-RecoveryNoReparsePathComponents $ManifestPath 'pre-lock predecessor manifest')
    if ($ReviewedManifestSha256 -cnotmatch '^[0-9A-F]{64}$' -or
        $ReviewedManifestSha256 -cne $ManifestSha256 -or
        -not (Test-Path -LiteralPath $ManifestPath -PathType Leaf) -or
        (Get-Item -LiteralPath $ManifestPath -Force).Length -ne $ManifestBytes -or
        (Get-FileHash -LiteralPath $ManifestPath -Algorithm SHA256).Hash -cne $ReviewedManifestSha256 -or
        -not (Get-Item -LiteralPath $ManifestPath -Force).IsReadOnly) {
        throw 'NEEDS_CONTEXT: independently reviewed manifest seal/read-only gate failed before lock CreateNew.'
    }
    $LockRecoveryTree = Get-RecoveryNonFollowingTree $RecoveryRoot 'pre-lock recovery-v3 root'
    if ($LockRecoveryTree.directories.Count -ne 1 -or $LockRecoveryTree.files.Count -ne 1 -or
        [string]$LockRecoveryTree.files[0] -cne (Get-RecoveryCanonicalPath $ManifestPath)) {
        throw 'NEEDS_CONTEXT: recovery-v3 root contains more than the reviewed manifest before lock CreateNew.'
    }
    $GateManifest = Read-RecoveryStrictJson $ManifestPath 'pre-lock reviewed predecessor manifest'
    Assert-RecoveryExactProperties $GateManifest @(
        'schema_version','purpose','predecessor_plan_commit','predecessor_lock_sha256',
        'artifact_count','catalog_bytes','catalog_sha256','artifacts','failures','source_inventories','created_utc'
    ) 'pre-lock reviewed predecessor manifest'
    if ($GateManifest.schema_version -isnot [int] -or $GateManifest.schema_version -ne 2 -or
        $GateManifest.purpose -isnot [string] -or
        $GateManifest.purpose -cne 'terminal-collapse-generator-recovery-v3-predecessor' -or
        $GateManifest.predecessor_plan_commit -isnot [string] -or
        $GateManifest.predecessor_plan_commit -cne $P2 -or
        $GateManifest.predecessor_lock_sha256 -isnot [string] -or
        $GateManifest.predecessor_lock_sha256 -cne
            '592E9F1FD5C4996A8612005BE9A33A35721A63228AAB43811208099265AECF8B' -or
        $GateManifest.artifact_count -isnot [int] -or $GateManifest.artifact_count -ne 115 -or
        @($GateManifest.artifacts).Count -ne 115 -or
        $GateManifest.catalog_bytes -isnot [int] -or $GateManifest.catalog_bytes -ne 24660 -or
        $GateManifest.catalog_sha256 -isnot [string] -or
        $GateManifest.catalog_sha256 -cne '9694E728A82F6DDC743DA5E83967EAC7EE02FFA62FA53E21F4A2374F27DDDA24' -or
        @($GateManifest.failures).Count -ne 2 -or @($GateManifest.source_inventories).Count -ne 2 -or
        $GateManifest.created_utc -isnot [string] -or
        [string]$GateManifest.created_utc -cne [string]$ManifestRoundTrip.created_utc -or
        ([object[]]@($GateManifest.failures) | ConvertTo-Json -Depth 8 -Compress) -cne $ExpectedFailuresJson -or
        ([object[]]@($GateManifest.source_inventories) | ConvertTo-Json -Depth 8 -Compress) -cne $ExpectedInventoriesJson) {
        throw 'NEEDS_CONTEXT: reviewed manifest content drifted before lock CreateNew.'
    }
    $GateManifestRows = New-Object 'System.Collections.Generic.List[string]'
    $GateManifestPaths = New-Object 'System.Collections.Generic.List[string]'
    $GateManifestSeen = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
    foreach ($Artifact in @($GateManifest.artifacts)) {
        Assert-RecoveryExactProperties $Artifact @('path','bytes','sha256') 'pre-lock reviewed manifest artifact'
        $ArtifactPath = if ($Artifact.path -is [string]) { [string]$Artifact.path } else { '' }
        if (-not [IO.Path]::IsPathRooted($ArtifactPath) -or
            (Get-RecoveryCanonicalPath $ArtifactPath) -cne $ArtifactPath -or
            -not $GateManifestSeen.Add($ArtifactPath) -or
            -not (Test-RecoveryIntegral $Artifact.bytes) -or [int64]$Artifact.bytes -lt 0 -or
            $Artifact.sha256 -isnot [string] -or $Artifact.sha256 -cnotmatch '^[0-9A-F]{64}$') {
            throw ('NEEDS_CONTEXT: reviewed manifest artifact shape failed before lock CreateNew: ' + $ArtifactPath)
        }
        [void](Assert-RecoveryNoReparsePathComponents $ArtifactPath 'pre-lock reviewed manifest artifact')
        $Current = New-RecoveryFileSeal $ArtifactPath
        if ([int64]$Current.bytes -ne [int64]$Artifact.bytes -or
            [string]$Current.sha256 -cne [string]$Artifact.sha256) {
            throw ('NEEDS_CONTEXT: reviewed manifest artifact drifted before lock CreateNew: ' + $ArtifactPath)
        }
        $GateManifestPaths.Add($ArtifactPath)
        $GateManifestRows.Add(($ArtifactPath + [char]9 + [string]$Artifact.bytes + [char]9 + [string]$Artifact.sha256))
    }
    $GateManifestSorted = Sort-RecoveryStringsOrdinal $GateManifestPaths.ToArray()
    if (($GateManifestSorted -join "`n") -cne ($GateManifestPaths.ToArray() -join "`n")) {
        throw 'NEEDS_CONTEXT: reviewed manifest artifact order drifted before lock CreateNew.'
    }
    $GateManifestCatalog = $StrictUtf8.GetBytes(($GateManifestRows -join "`n") + "`n")
    if ($GateManifestCatalog.Length -ne 24660 -or
        (Get-RecoverySha256ForBytes $GateManifestCatalog) -cne
            '9694E728A82F6DDC743DA5E83967EAC7EE02FFA62FA53E21F4A2374F27DDDA24') {
        throw 'NEEDS_CONTEXT: reviewed physical 115-leaf catalog drifted before lock CreateNew.'
    }
}

$ManifestObject = [pscustomobject][ordered]@{
    schema_version = 2
    purpose = 'terminal-collapse-generator-recovery-v3-predecessor'
    predecessor_plan_commit = $P2
    predecessor_lock_sha256 = '592E9F1FD5C4996A8612005BE9A33A35721A63228AAB43811208099265AECF8B'
    artifact_count = 115
    catalog_bytes = 24660
    catalog_sha256 = '9694E728A82F6DDC743DA5E83967EAC7EE02FFA62FA53E21F4A2374F27DDDA24'
    artifacts = [object[]]$ArtifactObjects.ToArray()
    failures = [object[]]@($LegacyFailure, $V2Failure)
    source_inventories = [object[]]$SourceInventories
    created_utc = [DateTimeOffset]::UtcNow.ToString('o', [Globalization.CultureInfo]::InvariantCulture)
}

$ManifestJson = ($ManifestObject | ConvertTo-Json -Depth 12 -Compress) + "`n"
[IO.Directory]::CreateDirectory($RecoveryRoot) | Out-Null
[void](Assert-RecoveryNoReparsePathComponents $RecoveryRoot 'new recovery-v3 authority root')
Assert-RecoveryCurrentAuthorityPrepublication -Phase 'manifest'
New-RecoveryCreateOnlyUtf8File $ManifestPath $ManifestJson
$ManifestRoundTrip = Read-RecoveryStrictJson $ManifestPath 'recovery-v3 predecessor manifest'
Assert-RecoveryExactProperties $ManifestRoundTrip @(
    'schema_version','purpose','predecessor_plan_commit','predecessor_lock_sha256',
    'artifact_count','catalog_bytes','catalog_sha256','artifacts','failures','source_inventories','created_utc'
) 'recovery-v3 predecessor manifest'
if ($ManifestRoundTrip.schema_version -isnot [int] -or $ManifestRoundTrip.schema_version -ne 2 -or
    $ManifestRoundTrip.purpose -isnot [string] -or $ManifestRoundTrip.purpose -cne 'terminal-collapse-generator-recovery-v3-predecessor' -or
    $ManifestRoundTrip.predecessor_plan_commit -isnot [string] -or $ManifestRoundTrip.predecessor_plan_commit -cne $P2 -or
    $ManifestRoundTrip.predecessor_lock_sha256 -isnot [string] -or
    $ManifestRoundTrip.predecessor_lock_sha256 -cne '592E9F1FD5C4996A8612005BE9A33A35721A63228AAB43811208099265AECF8B' -or
    $ManifestRoundTrip.artifact_count -isnot [int] -or $ManifestRoundTrip.artifact_count -ne 115 -or
    @($ManifestRoundTrip.artifacts).Count -ne 115 -or
    $ManifestRoundTrip.catalog_bytes -isnot [int] -or $ManifestRoundTrip.catalog_bytes -ne 24660 -or
    $ManifestRoundTrip.catalog_sha256 -isnot [string] -or
    $ManifestRoundTrip.catalog_sha256 -cne '9694E728A82F6DDC743DA5E83967EAC7EE02FFA62FA53E21F4A2374F27DDDA24' -or
    @($ManifestRoundTrip.failures).Count -ne 2 -or @($ManifestRoundTrip.source_inventories).Count -ne 2) {
    throw 'NEEDS_CONTEXT: recovery-v3 predecessor manifest strict reread failed.'
}
$RoundTripRows = New-Object 'System.Collections.Generic.List[string]'
$RoundTripPaths = New-Object 'System.Collections.Generic.List[string]'
$RoundTripSeen = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
foreach ($Artifact in @($ManifestRoundTrip.artifacts)) {
    Assert-RecoveryExactProperties $Artifact @('path','bytes','sha256') 'manifest round-trip artifact'
    if ($Artifact.path -isnot [string] -or -not $RoundTripSeen.Add([string]$Artifact.path) -or
        -not (Test-RecoveryIntegral $Artifact.bytes) -or [int64]$Artifact.bytes -lt 0 -or
        $Artifact.sha256 -isnot [string] -or $Artifact.sha256 -cnotmatch '^[0-9A-F]{64}$') {
        throw 'NEEDS_CONTEXT: manifest round-trip artifact shape failed.'
    }
    $Current = New-RecoveryFileSeal ([string]$Artifact.path)
    if ([int64]$Current.bytes -ne [int64]$Artifact.bytes -or
        [string]$Current.sha256 -cne [string]$Artifact.sha256) {
        throw ('NEEDS_CONTEXT: manifest round-trip artifact drifted: ' + [string]$Artifact.path)
    }
    $RoundTripPaths.Add([string]$Artifact.path)
    $RoundTripRows.Add(([string]$Artifact.path + [char]9 + [string]$Artifact.bytes + [char]9 + [string]$Artifact.sha256))
}
$RoundTripSorted = Sort-RecoveryStringsOrdinal $RoundTripPaths.ToArray()
if (($RoundTripSorted -join "`n") -cne ($RoundTripPaths.ToArray() -join "`n")) {
    throw 'NEEDS_CONTEXT: manifest round-trip artifacts are not Ordinal-sorted.'
}
$RoundTripCatalogBytes = $StrictUtf8.GetBytes(($RoundTripRows -join "`n") + "`n")
if ($RoundTripCatalogBytes.Length -ne 24660 -or
    (Get-RecoverySha256ForBytes $RoundTripCatalogBytes) -cne '9694E728A82F6DDC743DA5E83967EAC7EE02FFA62FA53E21F4A2374F27DDDA24') {
    throw 'NEEDS_CONTEXT: manifest round-trip catalog failed.'
}
$ManifestCreatedUtc = [DateTimeOffset]::MinValue
if ($ManifestRoundTrip.created_utc -isnot [string] -or
    -not [DateTimeOffset]::TryParseExact(
        [string]$ManifestRoundTrip.created_utc, 'o',
        [Globalization.CultureInfo]::InvariantCulture,
        [Globalization.DateTimeStyles]::RoundtripKind,
        [ref]$ManifestCreatedUtc
    ) -or $ManifestCreatedUtc.Offset -ne [TimeSpan]::Zero) {
    throw 'NEEDS_CONTEXT: manifest created_utc is not round-trip UTC.'
}
(Get-Item -LiteralPath $ManifestPath -Force).IsReadOnly = $true
$ManifestBytes = [int64](Get-Item -LiteralPath $ManifestPath -Force).Length
$ManifestSha256 = (Get-FileHash -LiteralPath $ManifestPath -Algorithm SHA256).Hash
if ($ManifestBytes -le 0 -or $ManifestSha256 -cnotmatch '^[0-9A-F]{64}$') {
    throw 'NEEDS_CONTEXT: predecessor manifest physical seal failed.'
}

[pscustomobject]@{
    status = 'PASS'
    predecessor_manifest_bytes = $ManifestBytes
    predecessor_manifest_sha256 = $ManifestSha256
    predecessor_artifacts = 115
    catalog_bytes = 24660
    helper_or_renpy_launches = 0
}
```

Expected: `PASS`; one read-only ignored schema-v2 manifest exists, its 115 current leaves reconstruct the fixed 24,660-byte catalog, both failures are preserved without promotion, and the v2 source inventories seal 8 authority + 61 excluded cache files and 12 SaveDir authority files. The v3 lock is still absent.

Pause here and keep the controller session open. Before Seal Step 3, an independent reviewer must read and hash the physical manifest, confirm its exact printed byte count and uppercase SHA-256, strict schema-v2/read-only/ignored encoding, and independently rebuild all 115 current artifact seals plus the 24,660-byte catalog SHA-256 `9694E728A82F6DDC743DA5E83967EAC7EE02FFA62FA53E21F4A2374F27DDDA24`. The reviewer must validate both ordered failure records with exactly these 22 fields and exact types/values: `id`, `classification`, `program_outcome`, `reason`, `generator_invocation_count`, `observer_invocation_count`, `attempt_path`, `attempt_sha256`, `result_path`, `result_bytes`, `result_sha256`, `state_path`, `state_bytes`, `state_sha256`, `test_report_path`, `test_report_bytes`, `test_report_sha256`, `engine_log_path`, `engine_log_bytes`, `engine_log_sha256`, `target_copies`, and `candidate_save_disposition`. For each record, the reviewer must validate every target as the exact four-field `role` / canonical `path` / integral `bytes` / uppercase `sha256` seal, re-hash all six current target copies, and confirm both dispositions are exactly `preserved_not_used`. The reviewer must also independently validate both ordered source inventories: worktree authority 8 / 777-byte catalog / `37976165E24FA53CC4DE33AC8D0B9B3DA0545925184FD3D4F088039292FE1723`, worktree excluded 61 / 5,732-byte catalog / `D7E59DED729100143D7763ABEA1A90DD1632E55B7EB3AEB1D26F968AF0C9A99B`, SaveDir authority 12 / 1,066-byte catalog / `DD3A6C77E61922681CE3788E6BBA0883B681461A10F628D4AA3CE66E033747A4`, and SaveDir excluded 0 / one-final-LF-byte catalog / `01BA4719C80B6FE911B091A7C05124B64EEECE964E09C058EF8F9805DACA546B`. That review includes the exact two inventory IDs and root paths, exact six-field inventory and three-field leaf schemas, Ordinal ordering, uniqueness, canonical in-root relative paths, every path component, a non-following traversal of `game`, `game\saves`, `game\cache`, and the external SaveDir, and rejection of every extra directory, leaf, or reparse point. The reviewer returns the exact uppercase physical manifest SHA-256 out of band—not a generic `READY` token—and the controller binds only that returned value as the existing scope-0 string variable `$ReviewedManifestSha256`. A missing/different result stops sealing and preserves the manifest without a lock.

- [ ] **Seal Step 3: Validate nested predecessor lineage and publish the exact 26-field schema-v3 lock**

Continue in the same controller session only after the independent predecessor-manifest reviewer has returned that exact physical manifest SHA-256 out of band and it exists as scope-0 `$ReviewedManifestSha256`:

```powershell
$ReviewedManifestVariable = Get-Variable -Name 'ReviewedManifestSha256' -Scope 0 -ErrorAction SilentlyContinue
if ($null -eq $ReviewedManifestVariable -or $ReviewedManifestVariable.Value -isnot [string]) {
    throw 'NEEDS_CONTEXT: independently reviewed manifest SHA-256 is absent from scope 0.'
}
$ReviewedManifestSha256 = [string]$ReviewedManifestVariable.Value
if ($ReviewedManifestSha256 -cnotmatch '^[0-9A-F]{64}$') {
    throw 'NEEDS_CONTEXT: independently reviewed manifest SHA-256 is not exact uppercase 64-hex.'
}
if (-not (Test-Path -LiteralPath $ManifestPath -PathType Leaf)) {
    throw 'NEEDS_CONTEXT: independently reviewed predecessor manifest is absent.'
}
[void](Assert-RecoveryNoReparsePathComponents $ManifestPath 'independently reviewed predecessor manifest')
$ReviewedManifestItem = Get-Item -LiteralPath $ManifestPath -Force -ErrorAction Stop
$CurrentReviewedManifestSha256 = (Get-FileHash -LiteralPath $ManifestPath -Algorithm SHA256).Hash
if ($ReviewedManifestSha256 -cne $ManifestSha256 -or
    $CurrentReviewedManifestSha256 -cne $ManifestSha256 -or
    [int64]$ReviewedManifestItem.Length -ne $ManifestBytes -or
    -not $ReviewedManifestItem.IsReadOnly) {
    throw 'NEEDS_CONTEXT: out-of-band, frozen, or current predecessor-manifest seal differs.'
}

$FailureProperties = [string[]]@(
    'id','classification','program_outcome','reason','generator_invocation_count',
    'observer_invocation_count','attempt_path','attempt_sha256','result_path','result_bytes',
    'result_sha256','state_path','state_bytes','state_sha256','test_report_path',
    'test_report_bytes','test_report_sha256','engine_log_path','engine_log_bytes',
    'engine_log_sha256','target_copies','candidate_save_disposition'
)
$TargetProperties = [string[]]@('role','path','bytes','sha256')
$InventoryProperties = [string[]]@(
    'id','root_path','authority_file_count','authority_files',
    'excluded_cache_count','excluded_cache_files'
)
$InventoryLeafProperties = [string[]]@('relative_path','bytes','sha256')
foreach ($Failure in @($ManifestRoundTrip.failures)) {
    Assert-RecoveryExactProperties $Failure $FailureProperties 'predecessor failure'
    if ($Failure.id -isnot [string] -or $Failure.classification -isnot [string] -or
        $Failure.program_outcome -isnot [string] -or $Failure.reason -isnot [string] -or
        $Failure.generator_invocation_count -isnot [int] -or
        $Failure.observer_invocation_count -isnot [int] -or
        $Failure.result_path -isnot [string] -or
        -not (Test-RecoveryIntegral $Failure.result_bytes) -or [int64]$Failure.result_bytes -lt 0 -or
        $Failure.result_sha256 -isnot [string] -or $Failure.result_sha256 -cnotmatch '^[0-9A-F]{64}$' -or
        $Failure.state_path -isnot [string] -or
        -not (Test-RecoveryIntegral $Failure.state_bytes) -or [int64]$Failure.state_bytes -lt 0 -or
        $Failure.state_sha256 -isnot [string] -or $Failure.state_sha256 -cnotmatch '^[0-9A-F]{64}$' -or
        $Failure.test_report_path -isnot [string] -or
        -not (Test-RecoveryIntegral $Failure.test_report_bytes) -or [int64]$Failure.test_report_bytes -lt 0 -or
        $Failure.test_report_sha256 -isnot [string] -or $Failure.test_report_sha256 -cnotmatch '^[0-9A-F]{64}$' -or
        $Failure.engine_log_path -isnot [string] -or
        -not (Test-RecoveryIntegral $Failure.engine_log_bytes) -or [int64]$Failure.engine_log_bytes -lt 0 -or
        $Failure.engine_log_sha256 -isnot [string] -or $Failure.engine_log_sha256 -cnotmatch '^[0-9A-F]{64}$' -or
        $Failure.candidate_save_disposition -isnot [string] -or
        @($Failure.target_copies).Count -ne 3) {
        throw 'NEEDS_CONTEXT: predecessor failure types failed.'
    }
    foreach ($Target in @($Failure.target_copies)) {
        Assert-RecoveryExactProperties $Target $TargetProperties 'failure target copy'
        if ($Target.role -isnot [string] -or $Target.path -isnot [string] -or
            -not (Test-RecoveryIntegral $Target.bytes) -or [int64]$Target.bytes -lt 0 -or
            $Target.sha256 -isnot [string] -or $Target.sha256 -cnotmatch '^[0-9A-F]{64}$') {
            throw 'NEEDS_CONTEXT: failure target-copy types failed.'
        }
    }
}
$ExpectedFailuresJson = ([object[]]@($LegacyFailure, $V2Failure) | ConvertTo-Json -Depth 8 -Compress)
$ActualFailuresJson = ([object[]]@($ManifestRoundTrip.failures) | ConvertTo-Json -Depth 8 -Compress)
if ($ActualFailuresJson -cne $ExpectedFailuresJson -or
    $ManifestRoundTrip.failures[0].attempt_path -ne $null -or
    $ManifestRoundTrip.failures[0].attempt_sha256 -ne $null) {
    throw 'NEEDS_CONTEXT: ordered legacy/v2 failure lineage failed exact comparison.'
}

foreach ($Inventory in @($ManifestRoundTrip.source_inventories)) {
    Assert-RecoveryExactProperties $Inventory $InventoryProperties 'source inventory'
    if ($Inventory.id -isnot [string] -or $Inventory.root_path -isnot [string] -or
        $Inventory.authority_file_count -isnot [int] -or
        $Inventory.excluded_cache_count -isnot [int] -or
        @($Inventory.authority_files).Count -ne $Inventory.authority_file_count -or
        @($Inventory.excluded_cache_files).Count -ne $Inventory.excluded_cache_count) {
        throw 'NEEDS_CONTEXT: source inventory shape failed.'
    }
    foreach ($Leaf in @($Inventory.authority_files) + @($Inventory.excluded_cache_files)) {
        Assert-RecoveryExactProperties $Leaf $InventoryLeafProperties 'source inventory leaf'
    }
}
$ExpectedInventoriesJson = ([object[]]$SourceInventories | ConvertTo-Json -Depth 8 -Compress)
$ActualInventoriesJson = ([object[]]@($ManifestRoundTrip.source_inventories) | ConvertTo-Json -Depth 8 -Compress)
if ($ActualInventoriesJson -cne $ExpectedInventoriesJson) {
    throw 'NEEDS_CONTEXT: source inventories failed exact comparison.'
}

$ManifestArtifactSet = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
foreach ($Artifact in @($ManifestRoundTrip.artifacts)) { [void]$ManifestArtifactSet.Add([string]$Artifact.path) }
foreach ($Inventory in @($ManifestRoundTrip.source_inventories)) {
    foreach ($Leaf in @($Inventory.authority_files)) {
        $Full = Get-RecoveryCanonicalPath (Join-Path ([string]$Inventory.root_path) ([string]$Leaf.relative_path))
        if (-not $ManifestArtifactSet.Contains($Full)) {
            throw ('NEEDS_CONTEXT: authority inventory leaf missing from 115 union: ' + $Full)
        }
    }
    foreach ($Leaf in @($Inventory.excluded_cache_files)) {
        $Full = Get-RecoveryCanonicalPath (Join-Path ([string]$Inventory.root_path) ([string]$Leaf.relative_path))
        if ($ManifestArtifactSet.Contains($Full)) {
            throw ('NEEDS_CONTEXT: excluded cache entered 115 union: ' + $Full)
        }
    }
}
foreach ($Failure in @($ManifestRoundTrip.failures)) {
    foreach ($SealField in @(
        [pscustomobject]@{ Path = [string]$Failure.result_path; Bytes = [int64]$Failure.result_bytes; Sha256 = [string]$Failure.result_sha256 },
        [pscustomobject]@{ Path = [string]$Failure.state_path; Bytes = [int64]$Failure.state_bytes; Sha256 = [string]$Failure.state_sha256 },
        [pscustomobject]@{ Path = [string]$Failure.test_report_path; Bytes = [int64]$Failure.test_report_bytes; Sha256 = [string]$Failure.test_report_sha256 },
        [pscustomobject]@{ Path = [string]$Failure.engine_log_path; Bytes = [int64]$Failure.engine_log_bytes; Sha256 = [string]$Failure.engine_log_sha256 }
    )) {
        $Seal = New-RecoveryFileSeal $SealField.Path
        if ([int64]$Seal.bytes -ne $SealField.Bytes -or [string]$Seal.sha256 -cne $SealField.Sha256 -or
            -not $ManifestArtifactSet.Contains([string]$Seal.path)) {
            throw ('NEEDS_CONTEXT: failure evidence is not a current manifest leaf: ' + $SealField.Path)
        }
    }
    foreach ($Target in @($Failure.target_copies)) {
        $Seal = New-RecoveryFileSeal ([string]$Target.path)
        if ([int64]$Seal.bytes -ne [int64]$Target.bytes -or
            [string]$Seal.sha256 -cne [string]$Target.sha256 -or
            -not $ManifestArtifactSet.Contains([string]$Seal.path)) {
            throw ('NEEDS_CONTEXT: failure target is not a current manifest leaf: ' + [string]$Target.path)
        }
    }
}

if (Test-Path -LiteralPath $ApprovalLockPath) {
    throw 'NEEDS_CONTEXT: v3 lock path was created before lock publication.'
}
$ApprovalLockObject = [pscustomobject][ordered]@{
    schema_version = 3
    purpose = 'terminal-collapse-generator-recovery-v3'
    approved_plan_path = $PlanPath
    approved_plan_commit = $P3
    plan_sha256 = $PlanSha256
    spec_path = $SpecPath
    spec_commit = $S3
    spec_sha256 = $SpecSha256
    predecessor_plan_commit = $P2
    predecessor_lock_path = Get-RecoveryCanonicalPath $V2LockPath
    predecessor_lock_bytes = [int64]1957
    predecessor_lock_sha256 = '592E9F1FD5C4996A8612005BE9A33A35721A63228AAB43811208099265AECF8B'
    predecessor_manifest_path = Get-RecoveryCanonicalPath $ManifestPath
    predecessor_manifest_bytes = $ManifestBytes
    predecessor_manifest_sha256 = $ManifestSha256
    baseline_game_tree = $GameTree
    generator_strategy = 'fresh_one_shot'
    superseded_generator_attempt_path = Get-RecoveryCanonicalPath (Join-Path $V2Root 'generator-attempt\attempt.json')
    superseded_generator_attempt_sha256 = '6C6D597580E80A448C0CE55A80C0955988970C2A6332854049420B8693D38DF0'
    superseded_generator_disposition = 'preserved_not_adopted_log_contract_mismatch'
    generator_attempt_ledger_path = Get-RecoveryCanonicalPath $GeneratorLedgerPath
    generator_attempt_limit = 1
    observer_attempt_ledger_path = Get-RecoveryCanonicalPath $ObserverLedgerPath
    observer_attempt_limit = 1
    test_result_stream = 'helper_stdout'
    engine_log_role = 'diagnostic_only'
}
$ApprovalLockJson = ($ApprovalLockObject | ConvertTo-Json -Depth 6 -Compress) + "`n"
Assert-RecoveryCurrentAuthorityPrepublication -Phase 'lock' -ReviewedManifestSha256 $ReviewedManifestSha256
New-RecoveryCreateOnlyUtf8File $ApprovalLockPath $ApprovalLockJson
$Approval = Read-RecoveryStrictJson $ApprovalLockPath 'approval lock v3'
$ApprovalLockProperties = [string[]]@(
    'schema_version','purpose','approved_plan_path','approved_plan_commit','plan_sha256',
    'spec_path','spec_commit','spec_sha256','predecessor_plan_commit','predecessor_lock_path',
    'predecessor_lock_bytes','predecessor_lock_sha256','predecessor_manifest_path',
    'predecessor_manifest_bytes','predecessor_manifest_sha256','baseline_game_tree',
    'generator_strategy','superseded_generator_attempt_path','superseded_generator_attempt_sha256',
    'superseded_generator_disposition','generator_attempt_ledger_path','generator_attempt_limit',
    'observer_attempt_ledger_path','observer_attempt_limit','test_result_stream','engine_log_role'
)
Assert-RecoveryExactProperties $Approval $ApprovalLockProperties 'approval lock v3'
if ($Approval.schema_version -isnot [int] -or $Approval.schema_version -ne 3 -or
    $Approval.purpose -isnot [string] -or $Approval.purpose -cne 'terminal-collapse-generator-recovery-v3' -or
    $Approval.approved_plan_path -isnot [string] -or $Approval.approved_plan_path -cne $PlanPath -or
    $Approval.approved_plan_commit -isnot [string] -or $Approval.approved_plan_commit -cne $P3 -or
    $Approval.plan_sha256 -isnot [string] -or $Approval.plan_sha256 -cne $PlanSha256 -or
    $Approval.spec_path -isnot [string] -or $Approval.spec_path -cne $SpecPath -or
    $Approval.spec_commit -isnot [string] -or $Approval.spec_commit -cne $S3 -or
    $Approval.spec_sha256 -isnot [string] -or $Approval.spec_sha256 -cne $SpecSha256 -or
    $Approval.predecessor_plan_commit -isnot [string] -or $Approval.predecessor_plan_commit -cne $P2 -or
    $Approval.predecessor_lock_path -isnot [string] -or
    $Approval.predecessor_lock_path -cne (Get-RecoveryCanonicalPath $V2LockPath) -or
    -not (Test-RecoveryIntegral $Approval.predecessor_lock_bytes) -or [int64]$Approval.predecessor_lock_bytes -ne 1957 -or
    $Approval.predecessor_lock_sha256 -isnot [string] -or
    $Approval.predecessor_lock_sha256 -cne '592E9F1FD5C4996A8612005BE9A33A35721A63228AAB43811208099265AECF8B' -or
    $Approval.predecessor_manifest_path -isnot [string] -or
    $Approval.predecessor_manifest_path -cne (Get-RecoveryCanonicalPath $ManifestPath) -or
    -not (Test-RecoveryIntegral $Approval.predecessor_manifest_bytes) -or
    [int64]$Approval.predecessor_manifest_bytes -ne $ManifestBytes -or
    $Approval.predecessor_manifest_sha256 -isnot [string] -or
    $Approval.predecessor_manifest_sha256 -cne $ManifestSha256 -or
    $Approval.baseline_game_tree -isnot [string] -or $Approval.baseline_game_tree -cne $GameTree -or
    $Approval.generator_strategy -isnot [string] -or $Approval.generator_strategy -cne 'fresh_one_shot' -or
    $Approval.superseded_generator_attempt_path -isnot [string] -or
    $Approval.superseded_generator_attempt_path -cne (Get-RecoveryCanonicalPath (Join-Path $V2Root 'generator-attempt\attempt.json')) -or
    $Approval.superseded_generator_attempt_sha256 -isnot [string] -or
    $Approval.superseded_generator_attempt_sha256 -cne '6C6D597580E80A448C0CE55A80C0955988970C2A6332854049420B8693D38DF0' -or
    $Approval.superseded_generator_disposition -isnot [string] -or
    $Approval.superseded_generator_disposition -cne 'preserved_not_adopted_log_contract_mismatch' -or
    $Approval.generator_attempt_ledger_path -isnot [string] -or
    $Approval.generator_attempt_ledger_path -cne (Get-RecoveryCanonicalPath $GeneratorLedgerPath) -or
    $Approval.generator_attempt_limit -isnot [int] -or $Approval.generator_attempt_limit -ne 1 -or
    $Approval.observer_attempt_ledger_path -isnot [string] -or
    $Approval.observer_attempt_ledger_path -cne (Get-RecoveryCanonicalPath $ObserverLedgerPath) -or
    $Approval.observer_attempt_limit -isnot [int] -or $Approval.observer_attempt_limit -ne 1 -or
    $Approval.test_result_stream -isnot [string] -or $Approval.test_result_stream -cne 'helper_stdout' -or
    $Approval.engine_log_role -isnot [string] -or $Approval.engine_log_role -cne 'diagnostic_only') {
    throw 'NEEDS_CONTEXT: approval lock v3 schema/types/values failed strict reread.'
}
(Get-Item -LiteralPath $ApprovalLockPath -Force).IsReadOnly = $true
$ApprovalLockBytes = [int64](Get-Item -LiteralPath $ApprovalLockPath -Force).Length
$ApprovalLockSha256 = (Get-FileHash -LiteralPath $ApprovalLockPath -Algorithm SHA256).Hash
if ($ApprovalLockBytes -le 0 -or $ApprovalLockSha256 -cnotmatch '^[0-9A-F]{64}$' -or
    -not (Get-Item -LiteralPath $ApprovalLockPath -Force).IsReadOnly) {
    throw 'NEEDS_CONTEXT: approval lock v3 physical seal failed.'
}
& git check-ignore -q -- $ApprovalLockPath
if ($LASTEXITCODE -ne 0) { throw 'NEEDS_CONTEXT: approval lock v3 is not ignored.' }
if ((Get-FileHash -LiteralPath $WinterPlan -Algorithm SHA256).Hash -cne $WinterSha256 -or
    @(git diff --cached --name-only).Count -ne 0 -or
    (@(git status --short --untracked-files=all) -join '|') -cne ('?? ' + $WinterPlan)) {
    throw 'NEEDS_CONTEXT: shared worktree drifted during controller sealing.'
}

[pscustomobject]@{
    status = 'PASS'
    approved_plan_commit = $P3
    plan_sha256 = $PlanSha256
    predecessor_manifest_bytes = $ManifestBytes
    predecessor_manifest_sha256 = $ManifestSha256
    approval_lock_bytes = $ApprovalLockBytes
    approval_lock_sha256 = $ApprovalLockSha256
    helper_or_renpy_launches = 0
}
```

Expected: `PASS`; the manifest and lock are both read-only and ignored, the lock has exactly 26 schema-v3 fields, and the printed uppercase `approval_lock_sha256` is not copied into this plan. Stop the controller session. An independent reviewer must verify the physical lock/manifest seals, the P2→S3→P3 chain, plan/spec blobs, 115-leaf catalog, both failure/source-inventory records, protected winter state, helper seals, and empty index before supplying only that printed lock SHA-256 out of band to Task 0/1/2/3 and Phase B.

---

## Task 0: Validate the sealed Recovery v3 authority without launching anything

**Files:**

- Read: `docs/superpowers/plans/2026-08-14-terminal-collapse-generator-recovery-v3.md`
- Read: `docs/superpowers/specs/2026-08-14-terminal-collapse-generator-recovery-v3-design.md`
- Read ignored: `.superpowers/sdd/terminal-collapse-ending/approved-plan-lock-v3.json`
- Read ignored: `.superpowers/sdd/terminal-collapse-ending/recovery-v3/predecessor-evidence.json`
- Read preserved: `.superpowers/sdd/terminal-collapse-ending/approved-plan-lock-v2.json`, `recovery-v2/*`, the v2 generator worktree, and the v2 generator SaveDir only for current-seal verification.

**Interfaces:**

- Consumes: controller-supplied uppercase `$ApprovalLockSha256`, sealed P2→S3→P3, schema-v3 26-field lock, and schema-v2 115-leaf predecessor manifest.
- Produces: an in-session static `PASS` proving the launch-free execution baseline. It creates no file, attempt directory, process evidence, fixture, ledger, helper child, Ren'Py/Python process, completion, or cleanup authority.

- [ ] **Step 0: Open one fresh persistent Windows PowerShell 5.1 Desktop session and bind only the out-of-band hash**

The controller binds `$ApprovalLockSha256` as a scriptblock parameter when creating the fresh session. Do not assign it from the lock, plan, manifest, console history, or chat. This is the first code executed in the task scope:

```powershell
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
if ($PSVersionTable.PSEdition -cne 'Desktop' -or $PSVersionTable.PSVersion.Major -ne 5) {
    throw 'NEEDS_CONTEXT: Task 0 requires Windows PowerShell 5.1 Desktop.'
}
$ApprovalVariable = Get-Variable -Name ApprovalLockSha256 -Scope 0 -ErrorAction SilentlyContinue
if ($null -eq $ApprovalVariable -or $ApprovalVariable.Value -isnot [string] -or
    [string]$ApprovalVariable.Value -cnotmatch '^[0-9A-F]{64}$') {
    throw 'NEEDS_CONTEXT: controller did not bind the out-of-band approval_lock_sha256.'
}
$ApprovalLockSha256 = [string]$ApprovalVariable.Value
$StrictUtf8 = New-Object System.Text.UTF8Encoding($false, $true)
$ProjectRoot = (Resolve-Path -LiteralPath '.').Path
```

Expected: Desktop PowerShell 5.1 and one externally bound uppercase lock hash; no project leaf has been read or written and no process has been launched.

- [ ] **Step 1: Validate the physical v3 lock before any other project leaf**

Continue in the same Task 0 session:

```powershell
function Get-Task0CanonicalPath([string]$Path) {
    return [IO.Path]::GetFullPath($Path).TrimEnd(
        [IO.Path]::DirectorySeparatorChar,
        [IO.Path]::AltDirectorySeparatorChar
    )
}
function Assert-Task0NoReparsePathComponents([string]$Path, [string]$Context) {
    $Full = [IO.Path]::GetFullPath($Path)
    $VolumeRoot = [IO.Path]::GetPathRoot($Full)
    if ([string]::IsNullOrWhiteSpace($VolumeRoot)) {
        throw ('NEEDS_CONTEXT: path has no volume root: ' + $Context)
    }
    $RootItem = Get-Item -LiteralPath $VolumeRoot -Force -ErrorAction Stop
    if (($RootItem.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
        throw ('NEEDS_CONTEXT: volume root is a reparse point: ' + $Context)
    }
    $Current = $VolumeRoot
    $Tail = $Full.Substring($VolumeRoot.Length)
    $Segments = $Tail.Split(
        [char[]]@([IO.Path]::DirectorySeparatorChar, [IO.Path]::AltDirectorySeparatorChar),
        [StringSplitOptions]::RemoveEmptyEntries
    )
    foreach ($Segment in $Segments) {
        $Current = Join-Path $Current $Segment
        $Item = Get-Item -LiteralPath $Current -Force -ErrorAction Stop
        if (($Item.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
            throw ('NEEDS_CONTEXT: reparse path component: ' + $Context + ': ' + $Current)
        }
    }
    return $Full
}
function Get-Task0NonFollowingTree([string]$RootPath, [string]$Context) {
    $Root = Get-Task0CanonicalPath $RootPath
    [void](Assert-Task0NoReparsePathComponents $Root $Context)
    $RootItem = Get-Item -LiteralPath $Root -Force -ErrorAction Stop
    if (-not $RootItem.PSIsContainer) {
        throw ('NEEDS_CONTEXT: non-following tree root is not a directory: ' + $Context)
    }
    $Directories = New-Object 'System.Collections.Generic.List[string]'
    $Files = New-Object 'System.Collections.Generic.List[string]'
    $Pending = New-Object 'System.Collections.Generic.Stack[string]'
    $Directories.Add($Root)
    $Pending.Push($Root)
    $Prefix = $Root + [IO.Path]::DirectorySeparatorChar
    while ($Pending.Count -gt 0) {
        $DirectoryPath = $Pending.Pop()
        $DirectoryItem = Get-Item -LiteralPath $DirectoryPath -Force -ErrorAction Stop
        if (-not $DirectoryItem.PSIsContainer -or
            (($DirectoryItem.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0)) {
            throw ('NEEDS_CONTEXT: unsafe directory reached before enumeration: ' + $Context + ': ' + $DirectoryPath)
        }
        $Children = @(Get-ChildItem -LiteralPath $DirectoryPath -Force -ErrorAction Stop)
        foreach ($Child in $Children) {
            $ChildFull = Get-Task0CanonicalPath $Child.FullName
            if (-not $ChildFull.StartsWith($Prefix, [StringComparison]::OrdinalIgnoreCase) -or
                (($Child.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0)) {
                throw ('NEEDS_CONTEXT: out-of-root or reparse child: ' + $Context + ': ' + $ChildFull)
            }
            if ($Child.PSIsContainer) {
                $Directories.Add($ChildFull)
                $Pending.Push($ChildFull)
            } else {
                $Files.Add($ChildFull)
            }
        }
    }
    return [pscustomobject]@{
        root = $Root
        directories = [string[]]$Directories.ToArray()
        files = [string[]]$Files.ToArray()
    }
}
function Test-Task0Integral($Value) {
    return ($Value -is [sbyte] -or $Value -is [byte] -or
        $Value -is [int16] -or $Value -is [uint16] -or
        $Value -is [int] -or $Value -is [uint32] -or
        $Value -is [long] -or $Value -is [uint64])
}
function Assert-Task0ExactProperties($Value, [string[]]$Expected, [string]$Context) {
    if ($Value -isnot [pscustomobject] -or
        (@($Value.PSObject.Properties.Name) -join '|') -cne ($Expected -join '|')) {
        throw ('NEEDS_CONTEXT: exact property contract failed: ' + $Context)
    }
}
function Get-Task0RawJsonObjectKeys([string]$Json, [string]$Context) {
    $Stack = New-Object 'System.Collections.Generic.Stack[object]'
    $Keys = New-Object 'System.Collections.Generic.List[string]'
    for ($Index = 0; $Index -lt $Json.Length; $Index++) {
        $Character = $Json[$Index]
        if ($Character -eq '{') {
            $Stack.Push((New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::Ordinal)))
        } elseif ($Character -eq '[') {
            $Stack.Push($null)
        } elseif ($Character -eq '}' -or $Character -eq ']') {
            if ($Stack.Count -eq 0) { throw ('NEEDS_CONTEXT: unbalanced JSON ' + $Context) }
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
                if ($Stack.Count -eq 0 -or $null -eq $Stack.Peek()) {
                    throw ('NEEDS_CONTEXT: key outside object ' + $Context)
                }
                $Token = $Json.Substring($Start, $Index - $Start + 1)
                $Key = [string]($Token | ConvertFrom-Json -ErrorAction Stop)
                if (-not $Stack.Peek().Add($Key)) {
                    throw ('NEEDS_CONTEXT: duplicate JSON key ' + $Key + ' ' + $Context)
                }
                [void]$Keys.Add($Key)
            }
        }
    }
    if ($Stack.Count -ne 0) { throw ('NEEDS_CONTEXT: unbalanced JSON containers ' + $Context) }
    return $Keys.ToArray()
}
function Read-Task0StrictJson([string]$Path, [string]$Context) {
    [void](Assert-Task0NoReparsePathComponents $Path ('strict JSON ' + $Context))
    $Item = Get-Item -LiteralPath $Path -Force -ErrorAction Stop
    if ($Item.PSIsContainer -or (($Item.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0)) {
        throw ('NEEDS_CONTEXT: JSON is not an ordinary file: ' + $Context)
    }
    $Raw = [IO.File]::ReadAllBytes($Item.FullName)
    if ($Raw.Length -eq 0 -or
        ($Raw.Length -ge 3 -and $Raw[0] -eq 0xEF -and $Raw[1] -eq 0xBB -and $Raw[2] -eq 0xBF)) {
        throw ('NEEDS_CONTEXT: empty/BOM JSON ' + $Context)
    }
    $Text = $StrictUtf8.GetString($Raw)
    if ($Text.Contains([char]0xFFFD) -or $Text.Contains([char]0) -or
        $Text.Contains("`r") -or -not $Text.EndsWith("`n", [StringComparison]::Ordinal)) {
        throw ('NEEDS_CONTEXT: noncanonical UTF-8/LF JSON ' + $Context)
    }
    [void](Get-Task0RawJsonObjectKeys $Text $Context)
    return ($Text | ConvertFrom-Json -ErrorAction Stop)
}
function Get-Task0Sha256ForBytes([byte[]]$Bytes) {
    $Hasher = [Security.Cryptography.SHA256]::Create()
    try {
        return [BitConverter]::ToString($Hasher.ComputeHash($Bytes)).Replace('-', '')
    } finally {
        $Hasher.Dispose()
    }
}
function Get-Task0FileSeal([string]$Path) {
    $Full = Get-Task0CanonicalPath $Path
    [void](Assert-Task0NoReparsePathComponents $Full 'file seal')
    $Item = Get-Item -LiteralPath $Full -Force -ErrorAction Stop
    if ($Item.PSIsContainer -or (($Item.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0)) {
        throw ('NEEDS_CONTEXT: expected ordinary leaf: ' + $Full)
    }
    return [pscustomobject]@{
        path = $Full
        bytes = [int64]$Item.Length
        sha256 = (Get-FileHash -LiteralPath $Full -Algorithm SHA256).Hash
    }
}

$P2 = '25c2ea674948ad89e8b48befb89643a8687648a4'
$S3 = '5fa8fb14792e095e066c3e9f698eda9ea4380854'
$GameTree = 'fa7a398e9d989731b24e3c1642f3e2e33ce846ff'
$PlanPath = 'docs/superpowers/plans/2026-08-14-terminal-collapse-generator-recovery-v3.md'
$SpecPath = 'docs/superpowers/specs/2026-08-14-terminal-collapse-generator-recovery-v3-design.md'
$SpecSha256 = '978116FE22B8C65578B78E800EF6039053284EA7E674271646D130BBB4BBF470'
$SpecBlob = '4c753503ab76484a546c8313c03914dd633a8902'
$EvidenceRoot = Join-Path $ProjectRoot '.superpowers\sdd\terminal-collapse-ending'
$RecoveryRoot = Join-Path $EvidenceRoot 'recovery-v3'
$V2Root = Join-Path $EvidenceRoot 'recovery-v2'
$ApprovalLockPath = Join-Path $EvidenceRoot 'approved-plan-lock-v3.json'
$ExpectedV2LockPath = Get-Task0CanonicalPath (Join-Path $EvidenceRoot 'approved-plan-lock-v2.json')
$ExpectedManifestPath = Get-Task0CanonicalPath (Join-Path $RecoveryRoot 'predecessor-evidence.json')
$ExpectedV2AttemptPath = Get-Task0CanonicalPath (Join-Path $V2Root 'generator-attempt\attempt.json')
$ExpectedGeneratorLedgerPath = Get-Task0CanonicalPath (Join-Path $RecoveryRoot 'generator-attempt')
$ExpectedObserverLedgerPath = Get-Task0CanonicalPath (Join-Path $RecoveryRoot 'observer-attempt')

# This is the first project leaf access in Task 0.
[void](Assert-Task0NoReparsePathComponents $ApprovalLockPath 'approval lock v3')
if (-not (Test-Path -LiteralPath $ApprovalLockPath -PathType Leaf) -or
    (Get-FileHash -LiteralPath $ApprovalLockPath -Algorithm SHA256).Hash -cne $ApprovalLockSha256 -or
    -not (Get-Item -LiteralPath $ApprovalLockPath -Force).IsReadOnly) {
    throw 'NEEDS_CONTEXT: v3 approval lock is missing, writable, or differs from the out-of-band hash.'
}
$Approval = Read-Task0StrictJson $ApprovalLockPath 'approval lock v3'
$ApprovalProperties = [string[]]@(
    'schema_version','purpose','approved_plan_path','approved_plan_commit','plan_sha256',
    'spec_path','spec_commit','spec_sha256','predecessor_plan_commit','predecessor_lock_path',
    'predecessor_lock_bytes','predecessor_lock_sha256','predecessor_manifest_path',
    'predecessor_manifest_bytes','predecessor_manifest_sha256','baseline_game_tree',
    'generator_strategy','superseded_generator_attempt_path','superseded_generator_attempt_sha256',
    'superseded_generator_disposition','generator_attempt_ledger_path','generator_attempt_limit',
    'observer_attempt_ledger_path','observer_attempt_limit','test_result_stream','engine_log_role'
)
Assert-Task0ExactProperties $Approval $ApprovalProperties 'approval lock v3'
if ($Approval.schema_version -isnot [int] -or $Approval.schema_version -ne 3 -or
    $Approval.purpose -isnot [string] -or $Approval.purpose -cne 'terminal-collapse-generator-recovery-v3' -or
    $Approval.approved_plan_path -isnot [string] -or $Approval.approved_plan_path -cne $PlanPath -or
    $Approval.approved_plan_commit -isnot [string] -or $Approval.approved_plan_commit -cnotmatch '^[0-9a-f]{40}$' -or
    $Approval.plan_sha256 -isnot [string] -or $Approval.plan_sha256 -cnotmatch '^[0-9A-F]{64}$' -or
    $Approval.spec_path -isnot [string] -or $Approval.spec_path -cne $SpecPath -or
    $Approval.spec_commit -isnot [string] -or $Approval.spec_commit -cne $S3 -or
    $Approval.spec_sha256 -isnot [string] -or $Approval.spec_sha256 -cne $SpecSha256 -or
    $Approval.predecessor_plan_commit -isnot [string] -or $Approval.predecessor_plan_commit -cne $P2 -or
    $Approval.predecessor_lock_path -isnot [string] -or $Approval.predecessor_lock_path -cne $ExpectedV2LockPath -or
    -not (Test-Task0Integral $Approval.predecessor_lock_bytes) -or [int64]$Approval.predecessor_lock_bytes -ne 1957 -or
    $Approval.predecessor_lock_sha256 -isnot [string] -or
    $Approval.predecessor_lock_sha256 -cne '592E9F1FD5C4996A8612005BE9A33A35721A63228AAB43811208099265AECF8B' -or
    $Approval.predecessor_manifest_path -isnot [string] -or
    $Approval.predecessor_manifest_path -cne $ExpectedManifestPath -or
    -not (Test-Task0Integral $Approval.predecessor_manifest_bytes) -or
    [int64]$Approval.predecessor_manifest_bytes -le 0 -or
    $Approval.predecessor_manifest_sha256 -isnot [string] -or
    $Approval.predecessor_manifest_sha256 -cnotmatch '^[0-9A-F]{64}$' -or
    $Approval.baseline_game_tree -isnot [string] -or $Approval.baseline_game_tree -cne $GameTree -or
    $Approval.generator_strategy -isnot [string] -or $Approval.generator_strategy -cne 'fresh_one_shot' -or
    $Approval.superseded_generator_attempt_path -isnot [string] -or
    $Approval.superseded_generator_attempt_path -cne $ExpectedV2AttemptPath -or
    $Approval.superseded_generator_attempt_sha256 -isnot [string] -or
    $Approval.superseded_generator_attempt_sha256 -cne '6C6D597580E80A448C0CE55A80C0955988970C2A6332854049420B8693D38DF0' -or
    $Approval.superseded_generator_disposition -isnot [string] -or
    $Approval.superseded_generator_disposition -cne 'preserved_not_adopted_log_contract_mismatch' -or
    $Approval.generator_attempt_ledger_path -isnot [string] -or
    $Approval.generator_attempt_ledger_path -cne $ExpectedGeneratorLedgerPath -or
    $Approval.generator_attempt_limit -isnot [int] -or $Approval.generator_attempt_limit -ne 1 -or
    $Approval.observer_attempt_ledger_path -isnot [string] -or
    $Approval.observer_attempt_ledger_path -cne $ExpectedObserverLedgerPath -or
    $Approval.observer_attempt_limit -isnot [int] -or $Approval.observer_attempt_limit -ne 1 -or
    $Approval.test_result_stream -isnot [string] -or $Approval.test_result_stream -cne 'helper_stdout' -or
    $Approval.engine_log_role -isnot [string] -or $Approval.engine_log_role -cne 'diagnostic_only') {
    throw 'NEEDS_CONTEXT: v3 approval lock schema/types/values failed.'
}
& git check-ignore -q -- $ApprovalLockPath
if ($LASTEXITCODE -ne 0) { throw 'NEEDS_CONTEXT: v3 approval lock is not ignored.' }
$P3 = [string]$Approval.approved_plan_commit
$ManifestPath = [string]$Approval.predecessor_manifest_path
```

Expected: the first project leaf read is the read-only lock whose physical SHA-256 equals the out-of-band value; its exact 26-field schema and all fixed v3 semantics pass before plan, spec, manifest, Git topology, or preserved runtime evidence is read.

- [ ] **Step 2: Prove P2 → S3 → P3 and rebuild all 115 current artifact seals**

Continue in the same Task 0 session:

```powershell
if ((& git rev-parse HEAD).Trim() -cne $P3 -or
    (& git rev-parse HEAD^).Trim() -cne $S3 -or
    (& git rev-parse ($S3 + '^')).Trim() -cne $P2 -or
    (git log -1 --format=%s) -cne 'docs: plan terminal collapse generator recovery v3') {
    throw 'NEEDS_CONTEXT: P2 -> S3 -> P3 direct-parent topology failed.'
}
$P3Paths = @(git diff-tree --no-commit-id --name-only -r $P3)
$S3Paths = @(git diff-tree --no-commit-id --name-only -r $S3)
if ($P3Paths.Count -ne 1 -or $P3Paths[0] -cne $PlanPath -or
    $S3Paths.Count -ne 1 -or $S3Paths[0] -cne $SpecPath) {
    throw 'NEEDS_CONTEXT: S3/P3 single-path contract failed.'
}
foreach ($Commit in @($P2, $S3, $P3)) {
    if ((& git rev-parse ($Commit + ':game')).Trim() -cne $GameTree) {
        throw ('NEEDS_CONTEXT: game tree drifted at ' + $Commit)
    }
}
$PlanBlob = (& git hash-object --no-filters -- $PlanPath).Trim()
$CommittedPlanBlob = (& git rev-parse ($P3 + ':' + $PlanPath)).Trim()
$PhysicalSpecBlob = (& git hash-object --no-filters -- $SpecPath).Trim()
$CommittedSpecBlob = (& git rev-parse ($S3 + ':' + $SpecPath)).Trim()
if ((Get-FileHash -LiteralPath $PlanPath -Algorithm SHA256).Hash -cne [string]$Approval.plan_sha256 -or
    $PlanBlob -cne $CommittedPlanBlob -or
    (Get-Item -LiteralPath $SpecPath -Force).Length -ne 41497 -or
    (Get-FileHash -LiteralPath $SpecPath -Algorithm SHA256).Hash -cne $SpecSha256 -or
    $PhysicalSpecBlob -cne $SpecBlob -or $CommittedSpecBlob -cne $SpecBlob) {
    throw 'NEEDS_CONTEXT: physical/committed plan or spec drifted.'
}
if (-not (Test-Path -LiteralPath $ExpectedV2LockPath -PathType Leaf) -or
    (Get-Item -LiteralPath $ExpectedV2LockPath -Force).Length -ne 1957 -or
    (Get-FileHash -LiteralPath $ExpectedV2LockPath -Algorithm SHA256).Hash -cne
        '592E9F1FD5C4996A8612005BE9A33A35721A63228AAB43811208099265AECF8B' -or
    -not (Get-Item -LiteralPath $ExpectedV2LockPath -Force).IsReadOnly) {
    throw 'NEEDS_CONTEXT: v2 predecessor lock drifted.'
}
if (-not (Test-Path -LiteralPath $ManifestPath -PathType Leaf) -or
    (Get-Item -LiteralPath $ManifestPath -Force).Length -ne [int64]$Approval.predecessor_manifest_bytes -or
    (Get-FileHash -LiteralPath $ManifestPath -Algorithm SHA256).Hash -cne
        [string]$Approval.predecessor_manifest_sha256 -or
    -not (Get-Item -LiteralPath $ManifestPath -Force).IsReadOnly) {
    throw 'NEEDS_CONTEXT: schema-v2 predecessor manifest seal drifted.'
}
$Manifest = Read-Task0StrictJson $ManifestPath 'recovery-v3 predecessor manifest'
Assert-Task0ExactProperties $Manifest @(
    'schema_version','purpose','predecessor_plan_commit','predecessor_lock_sha256',
    'artifact_count','catalog_bytes','catalog_sha256','artifacts','failures','source_inventories','created_utc'
) 'recovery-v3 predecessor manifest'
$ManifestCreatedUtc = [DateTimeOffset]::MinValue
if ($Manifest.schema_version -isnot [int] -or $Manifest.schema_version -ne 2 -or
    $Manifest.purpose -isnot [string] -or
    $Manifest.purpose -cne 'terminal-collapse-generator-recovery-v3-predecessor' -or
    $Manifest.predecessor_plan_commit -isnot [string] -or $Manifest.predecessor_plan_commit -cne $P2 -or
    $Manifest.predecessor_lock_sha256 -isnot [string] -or
    $Manifest.predecessor_lock_sha256 -cne '592E9F1FD5C4996A8612005BE9A33A35721A63228AAB43811208099265AECF8B' -or
    $Manifest.artifact_count -isnot [int] -or $Manifest.artifact_count -ne 115 -or
    @($Manifest.artifacts).Count -ne 115 -or
    $Manifest.catalog_bytes -isnot [int] -or $Manifest.catalog_bytes -ne 24660 -or
    $Manifest.catalog_sha256 -isnot [string] -or
    $Manifest.catalog_sha256 -cne '9694E728A82F6DDC743DA5E83967EAC7EE02FFA62FA53E21F4A2374F27DDDA24' -or
    @($Manifest.failures).Count -ne 2 -or @($Manifest.source_inventories).Count -ne 2 -or
    $Manifest.created_utc -isnot [string] -or
    -not [DateTimeOffset]::TryParseExact(
        [string]$Manifest.created_utc, 'o',
        [Globalization.CultureInfo]::InvariantCulture,
        [Globalization.DateTimeStyles]::RoundtripKind,
        [ref]$ManifestCreatedUtc
    ) -or $ManifestCreatedUtc.Offset -ne [TimeSpan]::Zero) {
    throw 'NEEDS_CONTEXT: predecessor manifest top-level contract failed.'
}
$ManifestPaths = New-Object 'System.Collections.Generic.List[string]'
$ManifestRows = New-Object 'System.Collections.Generic.List[string]'
$ManifestArtifactSet = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
foreach ($Artifact in @($Manifest.artifacts)) {
    Assert-Task0ExactProperties $Artifact @('path','bytes','sha256') 'predecessor artifact'
    $ArtifactPath = if ($Artifact.path -is [string]) { [string]$Artifact.path } else { '' }
    if (-not [IO.Path]::IsPathRooted($ArtifactPath) -or
        (Get-Task0CanonicalPath $ArtifactPath) -cne $ArtifactPath -or
        -not $ManifestArtifactSet.Add($ArtifactPath) -or
        -not (Test-Task0Integral $Artifact.bytes) -or [int64]$Artifact.bytes -lt 0 -or
        $Artifact.sha256 -isnot [string] -or $Artifact.sha256 -cnotmatch '^[0-9A-F]{64}$') {
        throw ('NEEDS_CONTEXT: predecessor artifact shape failed: ' + $ArtifactPath)
    }
    $Current = Get-Task0FileSeal $ArtifactPath
    if ([int64]$Current.bytes -ne [int64]$Artifact.bytes -or
        [string]$Current.sha256 -cne [string]$Artifact.sha256) {
        throw ('NEEDS_CONTEXT: predecessor artifact drifted: ' + $ArtifactPath)
    }
    $ManifestPaths.Add($ArtifactPath)
    $ManifestRows.Add(($ArtifactPath + [char]9 + [string]$Artifact.bytes + [char]9 + [string]$Artifact.sha256))
}
$SortedManifestPaths = [string[]]$ManifestPaths.ToArray()
[Array]::Sort($SortedManifestPaths, [StringComparer]::Ordinal)
if (($SortedManifestPaths -join "`n") -cne ($ManifestPaths.ToArray() -join "`n")) {
    throw 'NEEDS_CONTEXT: predecessor artifact paths are not Ordinal-sorted.'
}
$CatalogBytes = $StrictUtf8.GetBytes(($ManifestRows -join "`n") + "`n")
$CatalogSha256 = Get-Task0Sha256ForBytes $CatalogBytes
if ($CatalogBytes.Length -ne 24660 -or
    $CatalogSha256 -cne '9694E728A82F6DDC743DA5E83967EAC7EE02FFA62FA53E21F4A2374F27DDDA24') {
    throw ('NEEDS_CONTEXT: 115-leaf catalog reconstruction failed: ' + $CatalogBytes.Length + '/' + $CatalogSha256)
}
```

Expected: P2→S3→P3, exact single-file commits, physical/committed blobs, unchanged game tree, v2 lock, v3 manifest, and all 115 current artifact seals pass; the reconstructed catalog remains exactly 24,660 bytes with the fixed SHA-256.

- [ ] **Step 3: Verify both failed lineages and both exact v2 source inventories**

Continue in the same Task 0 session:

```powershell
$FailureProperties = [string[]]@(
    'id','classification','program_outcome','reason','generator_invocation_count',
    'observer_invocation_count','attempt_path','attempt_sha256','result_path','result_bytes',
    'result_sha256','state_path','state_bytes','state_sha256','test_report_path',
    'test_report_bytes','test_report_sha256','engine_log_path','engine_log_bytes',
    'engine_log_sha256','target_copies','candidate_save_disposition'
)
$TargetProperties = [string[]]@('role','path','bytes','sha256')
$InventoryProperties = [string[]]@(
    'id','root_path','authority_file_count','authority_files',
    'excluded_cache_count','excluded_cache_files'
)
$InventoryLeafProperties = [string[]]@('relative_path','bytes','sha256')
$V2GeneratorWorktree = 'E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-generator-recovery-v2'
$V2GeneratorSaveDir = 'E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-generator-save-recovery-v2'
$Legacy = $Manifest.failures[0]
$V2Failure = $Manifest.failures[1]
Assert-Task0ExactProperties $Legacy $FailureProperties 'legacy failure'
Assert-Task0ExactProperties $V2Failure $FailureProperties 'v2 failure'
if ($Legacy.id -isnot [string] -or $Legacy.id -cne 'legacy_generator' -or
    $Legacy.classification -isnot [string] -or $Legacy.classification -cne 'TIMEOUT' -or
    $Legacy.program_outcome -isnot [string] -or $Legacy.program_outcome -cne 'TIMEOUT' -or
    $Legacy.reason -isnot [string] -or $Legacy.reason -cne 'HELPER_TIMEOUT' -or
    $Legacy.generator_invocation_count -isnot [int] -or $Legacy.generator_invocation_count -ne 1 -or
    $Legacy.observer_invocation_count -isnot [int] -or $Legacy.observer_invocation_count -ne 0 -or
    $null -ne $Legacy.attempt_path -or $null -ne $Legacy.attempt_sha256 -or
    $Legacy.result_path -isnot [string] -or
    $Legacy.result_path -cne (Get-Task0CanonicalPath (Join-Path $EvidenceRoot 'legacy\generator-process\result.json')) -or
    -not (Test-Task0Integral $Legacy.result_bytes) -or [int64]$Legacy.result_bytes -ne 1716 -or
    $Legacy.result_sha256 -isnot [string] -or
    $Legacy.result_sha256 -cne '65A789696D25390CFC827FAA7A2C19D150B67A3EC2161AC44DFD79ADBEE57D13' -or
    $Legacy.state_path -isnot [string] -or
    $Legacy.state_path -cne (Get-Task0CanonicalPath (Join-Path $EvidenceRoot 'legacy\generator-state.json')) -or
    -not (Test-Task0Integral $Legacy.state_bytes) -or [int64]$Legacy.state_bytes -ne 2570 -or
    $Legacy.state_sha256 -isnot [string] -or
    $Legacy.state_sha256 -cne '82014869E02AEB3E18B7F7D6230C6789BDA05955A345AF4B9348C13D283E79ED' -or
    $Legacy.test_report_path -isnot [string] -or
    $Legacy.test_report_path -cne (Get-Task0CanonicalPath (Join-Path $EvidenceRoot 'legacy\generator-process\stdout.txt')) -or
    -not (Test-Task0Integral $Legacy.test_report_bytes) -or [int64]$Legacy.test_report_bytes -ne 0 -or
    $Legacy.test_report_sha256 -isnot [string] -or
    $Legacy.test_report_sha256 -cne 'E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855' -or
    $Legacy.engine_log_path -isnot [string] -or
    $Legacy.engine_log_path -cne 'E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-generator-c2958b40c6044ce598e56263855c071d\log.txt' -or
    -not (Test-Task0Integral $Legacy.engine_log_bytes) -or [int64]$Legacy.engine_log_bytes -ne 0 -or
    $Legacy.engine_log_sha256 -isnot [string] -or
    $Legacy.engine_log_sha256 -cne 'E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855' -or
    $Legacy.candidate_save_disposition -isnot [string] -or
    $Legacy.candidate_save_disposition -cne 'preserved_not_used') {
    throw 'NEEDS_CONTEXT: legacy TIMEOUT lineage failed.'
}
if ($V2Failure.id -isnot [string] -or $V2Failure.id -cne 'v2_generator' -or
    $V2Failure.classification -isnot [string] -or
    $V2Failure.classification -cne 'GOVERNANCE_CONTRACT_FAILURE' -or
    $V2Failure.program_outcome -isnot [string] -or $V2Failure.program_outcome -cne 'COMPLETED' -or
    $V2Failure.reason -isnot [string] -or $V2Failure.reason -cne 'LOG_CONTRACT_MISMATCH' -or
    $V2Failure.generator_invocation_count -isnot [int] -or $V2Failure.generator_invocation_count -ne 1 -or
    $V2Failure.observer_invocation_count -isnot [int] -or $V2Failure.observer_invocation_count -ne 0 -or
    $V2Failure.attempt_path -isnot [string] -or $V2Failure.attempt_path -cne $ExpectedV2AttemptPath -or
    $V2Failure.attempt_sha256 -isnot [string] -or
    $V2Failure.attempt_sha256 -cne '6C6D597580E80A448C0CE55A80C0955988970C2A6332854049420B8693D38DF0' -or
    $V2Failure.result_path -isnot [string] -or
    $V2Failure.result_path -cne (Get-Task0CanonicalPath (Join-Path $V2Root 'generator-process\result.json')) -or
    -not (Test-Task0Integral $V2Failure.result_bytes) -or [int64]$V2Failure.result_bytes -ne 1734 -or
    $V2Failure.result_sha256 -isnot [string] -or
    $V2Failure.result_sha256 -cne '12955539EC45CB4B3FA5490393EF511A851BD7CA3800F7835EBACAFFFF69D94F' -or
    $V2Failure.state_path -isnot [string] -or
    $V2Failure.state_path -cne (Get-Task0CanonicalPath (Join-Path $V2Root 'generator-state.json')) -or
    -not (Test-Task0Integral $V2Failure.state_bytes) -or [int64]$V2Failure.state_bytes -ne 2528 -or
    $V2Failure.state_sha256 -isnot [string] -or
    $V2Failure.state_sha256 -cne '43EDEB6BDFD217A7E9CDD969564A29B472D6D0258CF83ABD106F568A5B29D652' -or
    $V2Failure.test_report_path -isnot [string] -or
    $V2Failure.test_report_path -cne (Get-Task0CanonicalPath (Join-Path $V2Root 'generator-process\stdout.txt')) -or
    -not (Test-Task0Integral $V2Failure.test_report_bytes) -or [int64]$V2Failure.test_report_bytes -ne 1074 -or
    $V2Failure.test_report_sha256 -isnot [string] -or
    $V2Failure.test_report_sha256 -cne 'BD3B00124C6134FD0DAE737B293C20F68BF76F02ECDC69E77797C883FA5208CE' -or
    $V2Failure.engine_log_path -isnot [string] -or
    $V2Failure.engine_log_path -cne (Get-Task0CanonicalPath (Join-Path $V2GeneratorWorktree 'log.txt')) -or
    -not (Test-Task0Integral $V2Failure.engine_log_bytes) -or [int64]$V2Failure.engine_log_bytes -ne 1860 -or
    $V2Failure.engine_log_sha256 -isnot [string] -or
    $V2Failure.engine_log_sha256 -cne 'FE52BE91013D21B51AAF2CCDCF796289906EB4D12FA08EB1912A196B4F076A81' -or
    $V2Failure.candidate_save_disposition -isnot [string] -or
    $V2Failure.candidate_save_disposition -cne 'preserved_not_used') {
    throw 'NEEDS_CONTEXT: v2 log-contract-mismatch lineage failed.'
}

$ExpectedLegacyTargets = [object[]]@(
    [pscustomobject]@{ role = 'external_root'; path = 'E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-generator-save-44f1b1204d3f4222a019a2a41335d6a6\1-1-LT1.save'; bytes = [int64]733069; sha256 = 'E24D04A5F71BBBC13086D68EA09C4F746A2CE2DB1C9D5865BB7769C1DF9036DB' },
    [pscustomobject]@{ role = 'external_sync'; path = 'E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-generator-save-44f1b1204d3f4222a019a2a41335d6a6\sync\1-1-LT1.save'; bytes = [int64]733069; sha256 = 'E24D04A5F71BBBC13086D68EA09C4F746A2CE2DB1C9D5865BB7769C1DF9036DB' },
    [pscustomobject]@{ role = 'worktree_local'; path = 'E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-generator-c2958b40c6044ce598e56263855c071d\game\saves\1-1-LT1.save'; bytes = [int64]733069; sha256 = 'E24D04A5F71BBBC13086D68EA09C4F746A2CE2DB1C9D5865BB7769C1DF9036DB' }
)
$ExpectedV2Targets = [object[]]@(
    [pscustomobject]@{ role = 'external_root'; path = (Join-Path $V2GeneratorSaveDir '1-1-LT1.save'); bytes = [int64]726209; sha256 = 'A817BBDE9A00B82A044E27C9AF93F27D99E1F106AABDE2230FFD5E8A1FAF19D7' },
    [pscustomobject]@{ role = 'external_sync'; path = (Join-Path $V2GeneratorSaveDir 'sync\1-1-LT1.save'); bytes = [int64]726209; sha256 = 'A817BBDE9A00B82A044E27C9AF93F27D99E1F106AABDE2230FFD5E8A1FAF19D7' },
    [pscustomobject]@{ role = 'worktree_local'; path = (Join-Path $V2GeneratorWorktree 'game\saves\1-1-LT1.save'); bytes = [int64]726209; sha256 = 'A817BBDE9A00B82A044E27C9AF93F27D99E1F106AABDE2230FFD5E8A1FAF19D7' }
)
function Assert-Task0FailureTargets($ActualTargets, $ExpectedTargets, [string]$Context) {
    if (@($ActualTargets).Count -ne 3 -or @($ExpectedTargets).Count -ne 3) {
        throw ('NEEDS_CONTEXT: target cardinality failed: ' + $Context)
    }
    for ($Index = 0; $Index -lt 3; $Index++) {
        $Actual = $ActualTargets[$Index]
        $Expected = $ExpectedTargets[$Index]
        Assert-Task0ExactProperties $Actual $TargetProperties ($Context + ' target')
        $ExpectedPath = Get-Task0CanonicalPath ([string]$Expected.path)
        if ($Actual.role -isnot [string] -or $Actual.role -cne [string]$Expected.role -or
            $Actual.path -isnot [string] -or $Actual.path -cne $ExpectedPath -or
            -not (Test-Task0Integral $Actual.bytes) -or [int64]$Actual.bytes -ne [int64]$Expected.bytes -or
            $Actual.sha256 -isnot [string] -or $Actual.sha256 -cne [string]$Expected.sha256) {
            throw ('NEEDS_CONTEXT: target contract failed: ' + $Context)
        }
        $Current = Get-Task0FileSeal $ExpectedPath
        if ([int64]$Current.bytes -ne [int64]$Expected.bytes -or
            [string]$Current.sha256 -cne [string]$Expected.sha256 -or
            -not $ManifestArtifactSet.Contains($ExpectedPath)) {
            throw ('NEEDS_CONTEXT: target physical seal failed: ' + $ExpectedPath)
        }
    }
}
Assert-Task0FailureTargets @($Legacy.target_copies) $ExpectedLegacyTargets 'legacy'
Assert-Task0FailureTargets @($V2Failure.target_copies) $ExpectedV2Targets 'v2'

foreach ($Failure in @($Legacy, $V2Failure)) {
    foreach ($Evidence in @(
        [pscustomobject]@{ path = [string]$Failure.result_path; bytes = [int64]$Failure.result_bytes; sha256 = [string]$Failure.result_sha256 },
        [pscustomobject]@{ path = [string]$Failure.state_path; bytes = [int64]$Failure.state_bytes; sha256 = [string]$Failure.state_sha256 },
        [pscustomobject]@{ path = [string]$Failure.test_report_path; bytes = [int64]$Failure.test_report_bytes; sha256 = [string]$Failure.test_report_sha256 },
        [pscustomobject]@{ path = [string]$Failure.engine_log_path; bytes = [int64]$Failure.engine_log_bytes; sha256 = [string]$Failure.engine_log_sha256 }
    )) {
        $Current = Get-Task0FileSeal $Evidence.path
        if ([int64]$Current.bytes -ne $Evidence.bytes -or [string]$Current.sha256 -cne $Evidence.sha256 -or
            -not $ManifestArtifactSet.Contains([string]$Current.path)) {
            throw ('NEEDS_CONTEXT: failure evidence physical seal failed: ' + $Evidence.path)
        }
    }
}
$V2AttemptSeal = Get-Task0FileSeal $ExpectedV2AttemptPath
if ($V2AttemptSeal.bytes -ne 2020 -or
    $V2AttemptSeal.sha256 -cne '6C6D597580E80A448C0CE55A80C0955988970C2A6332854049420B8693D38DF0' -or
    -not $ManifestArtifactSet.Contains($ExpectedV2AttemptPath)) {
    throw 'NEEDS_CONTEXT: superseded v2 attempt seal failed.'
}

# Re-prove the specific two-channel root cause without treating generic engine-log "error" text as fatal.
$V2StdoutRaw = [IO.File]::ReadAllBytes([string]$V2Failure.test_report_path)
$V2EngineRaw = [IO.File]::ReadAllBytes([string]$V2Failure.engine_log_path)
$V2StdoutText = $StrictUtf8.GetString($V2StdoutRaw)
$V2EngineText = $StrictUtf8.GetString($V2EngineRaw)
if (($V2StdoutRaw.Length -ge 3 -and $V2StdoutRaw[0] -eq 0xEF -and $V2StdoutRaw[1] -eq 0xBB -and $V2StdoutRaw[2] -eq 0xBF) -or
    $V2StdoutText.Contains([char]0xFFFD) -or $V2StdoutText.Contains([char]0) -or
    [regex]::Matches($V2StdoutText, '(?m)^\[rpytest\] Status:[^\r\n]*\r?$').Count -ne 1 -or
    [regex]::Matches($V2StdoutText, '(?m)^\[rpytest\] Status:[ \t]+PASSED[ \t]*\r?$').Count -ne 1 -or
    ($V2EngineRaw.Length -ge 3 -and $V2EngineRaw[0] -eq 0xEF -and $V2EngineRaw[1] -eq 0xBB -and $V2EngineRaw[2] -eq 0xBF) -or
    $V2EngineText.Contains([char]0xFFFD) -or $V2EngineText.Contains([char]0) -or
    [regex]::Matches($V2EngineText, '(?m)^\[rpytest\] Status:[^\r\n]*\r?$').Count -ne 0) {
    throw 'NEEDS_CONTEXT: sealed v2 stdout/engine-log channel mismatch facts drifted.'
}

function Assert-Task0RelativeInventory(
    $Inventory,
    [int]$ExpectedAuthorityCount,
    [int]$ExpectedExcludedCount,
    [int]$ExpectedAuthorityCatalogBytes,
    [string]$ExpectedAuthorityCatalogSha256,
    [int]$ExpectedExcludedCatalogBytes,
    [string]$ExpectedExcludedCatalogSha256
) {
    Assert-Task0ExactProperties $Inventory $InventoryProperties 'source inventory'
    if ($Inventory.id -isnot [string] -or $Inventory.root_path -isnot [string] -or
        -not [IO.Path]::IsPathRooted([string]$Inventory.root_path) -or
        (Get-Task0CanonicalPath ([string]$Inventory.root_path)) -cne [string]$Inventory.root_path -or
        $Inventory.authority_file_count -isnot [int] -or
        $Inventory.authority_file_count -ne $ExpectedAuthorityCount -or
        @($Inventory.authority_files).Count -ne $ExpectedAuthorityCount -or
        $Inventory.excluded_cache_count -isnot [int] -or
        $Inventory.excluded_cache_count -ne $ExpectedExcludedCount -or
        @($Inventory.excluded_cache_files).Count -ne $ExpectedExcludedCount) {
        throw ('NEEDS_CONTEXT: source inventory top-level contract failed: ' + [string]$Inventory.id)
    }
    foreach ($Pair in @(
        [pscustomobject]@{ Entries = @($Inventory.authority_files); Count = $ExpectedAuthorityCount; Bytes = $ExpectedAuthorityCatalogBytes; Sha256 = $ExpectedAuthorityCatalogSha256; IsAuthority = $true },
        [pscustomobject]@{ Entries = @($Inventory.excluded_cache_files); Count = $ExpectedExcludedCount; Bytes = $ExpectedExcludedCatalogBytes; Sha256 = $ExpectedExcludedCatalogSha256; IsAuthority = $false }
    )) {
        $Rows = New-Object 'System.Collections.Generic.List[string]'
        $Paths = New-Object 'System.Collections.Generic.List[string]'
        $Seen = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
        foreach ($Leaf in $Pair.Entries) {
            Assert-Task0ExactProperties $Leaf $InventoryLeafProperties 'source inventory leaf'
            $Relative = if ($Leaf.relative_path -is [string]) { [string]$Leaf.relative_path } else { '' }
            $Full = Get-Task0CanonicalPath (Join-Path ([string]$Inventory.root_path) $Relative)
            $Prefix = [string]$Inventory.root_path + [IO.Path]::DirectorySeparatorChar
            if ([IO.Path]::IsPathRooted($Relative) -or $Relative.Contains('/') -or
                -not $Full.StartsWith($Prefix, [StringComparison]::OrdinalIgnoreCase) -or
                $Full.Substring($Prefix.Length) -cne $Relative -or
                -not $Seen.Add($Relative) -or
                -not (Test-Task0Integral $Leaf.bytes) -or [int64]$Leaf.bytes -lt 0 -or
                $Leaf.sha256 -isnot [string] -or $Leaf.sha256 -cnotmatch '^[0-9A-F]{64}$') {
                throw ('NEEDS_CONTEXT: source inventory leaf shape failed: ' + $Relative)
            }
            [void](Assert-Task0NoReparsePathComponents $Full ('source inventory leaf ' + $Relative))
            $Current = Get-Task0FileSeal $Full
            if ([int64]$Current.bytes -ne [int64]$Leaf.bytes -or
                [string]$Current.sha256 -cne [string]$Leaf.sha256 -or
                ($Pair.IsAuthority -and -not $ManifestArtifactSet.Contains($Full)) -or
                (-not $Pair.IsAuthority -and $ManifestArtifactSet.Contains($Full))) {
                throw ('NEEDS_CONTEXT: source inventory physical/authority relation failed: ' + $Relative)
            }
            $Paths.Add($Relative)
            $Rows.Add(($Relative + [char]9 + [string]$Leaf.bytes + [char]9 + [string]$Leaf.sha256))
        }
        $Sorted = [string[]]$Paths.ToArray()
        [Array]::Sort($Sorted, [StringComparer]::Ordinal)
        if (($Sorted -join "`n") -cne ($Paths.ToArray() -join "`n")) {
            throw 'NEEDS_CONTEXT: source inventory is not Ordinal-sorted.'
        }
        $Catalog = $StrictUtf8.GetBytes(($Rows -join "`n") + "`n")
        if ($Pair.Entries.Count -ne $Pair.Count -or $Catalog.Length -ne $Pair.Bytes -or
            (Get-Task0Sha256ForBytes $Catalog) -cne $Pair.Sha256) {
            throw 'NEEDS_CONTEXT: source inventory frozen catalog failed.'
        }
    }
}

$WorktreeInventory = $Manifest.source_inventories[0]
$SaveDirInventory = $Manifest.source_inventories[1]
if ($WorktreeInventory.id -isnot [string] -or
    $WorktreeInventory.id -cne 'v2_generator_worktree_task_owned' -or
    $WorktreeInventory.root_path -isnot [string] -or
    $WorktreeInventory.root_path -cne (Get-Task0CanonicalPath $V2GeneratorWorktree) -or
    $SaveDirInventory.id -isnot [string] -or $SaveDirInventory.id -cne 'v2_generator_savedir' -or
    $SaveDirInventory.root_path -isnot [string] -or
    $SaveDirInventory.root_path -cne (Get-Task0CanonicalPath $V2GeneratorSaveDir)) {
    throw 'NEEDS_CONTEXT: ordered source-inventory identities failed.'
}
$V2WorktreeTree = Get-Task0NonFollowingTree $V2GeneratorWorktree 'v2 generator worktree'
$V2SaveTree = Get-Task0NonFollowingTree $V2GeneratorSaveDir 'v2 generator SaveDir'
$V2WorktreeDirectorySet = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
$V2WorktreeFileSet = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
foreach ($Path in $V2WorktreeTree.directories) { [void]$V2WorktreeDirectorySet.Add($Path) }
foreach ($Path in $V2WorktreeTree.files) { [void]$V2WorktreeFileSet.Add($Path) }
$V2GamePath = Get-Task0CanonicalPath (Join-Path $V2GeneratorWorktree 'game')
$V2SavesPath = Get-Task0CanonicalPath (Join-Path $V2GamePath 'saves')
$V2CachePath = Get-Task0CanonicalPath (Join-Path $V2GamePath 'cache')
foreach ($Path in @($V2GamePath, $V2SavesPath, $V2CachePath)) {
    [void](Assert-Task0NoReparsePathComponents $Path 'v2 task-owned intermediate directory')
    if (-not $V2WorktreeDirectorySet.Contains($Path)) {
        throw ('NEEDS_CONTEXT: v2 task-owned intermediate directory is missing: ' + $Path)
    }
}
foreach ($DirectoryPath in $V2WorktreeTree.directories) {
    if ($DirectoryPath.StartsWith($V2SavesPath + '\', [StringComparison]::OrdinalIgnoreCase) -or
        $DirectoryPath.StartsWith($V2CachePath + '\', [StringComparison]::OrdinalIgnoreCase)) {
        throw ('NEEDS_CONTEXT: extra directory appeared below a task-owned subtree: ' + $DirectoryPath)
    }
}
Assert-Task0RelativeInventory $WorktreeInventory 8 61 777 '37976165E24FA53CC4DE33AC8D0B9B3DA0545925184FD3D4F088039292FE1723' 5732 'D7E59DED729100143D7763ABEA1A90DD1632E55B7EB3AEB1D26F968AF0C9A99B'
Assert-Task0RelativeInventory $SaveDirInventory 12 0 1066 'DD3A6C77E61922681CE3788E6BBA0883B681461A10F628D4AA3CE66E033747A4' 1 '01BA4719C80B6FE911B091A7C05124B64EEECE964E09C058EF8F9805DACA546B'
foreach ($Leaf in @($WorktreeInventory.authority_files) + @($WorktreeInventory.excluded_cache_files)) {
    $Full = Get-Task0CanonicalPath (Join-Path $V2GeneratorWorktree ([string]$Leaf.relative_path))
    if (-not $V2WorktreeFileSet.Contains($Full)) {
        throw ('NEEDS_CONTEXT: task-owned inventory leaf is absent from safe non-following traversal: ' + $Full)
    }
}
$ExpectedTaskOwnedSubtreeFiles = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
foreach ($Leaf in @($WorktreeInventory.authority_files) + @($WorktreeInventory.excluded_cache_files)) {
    $Full = Get-Task0CanonicalPath (Join-Path $V2GeneratorWorktree ([string]$Leaf.relative_path))
    if ($Full.StartsWith($V2SavesPath + '\', [StringComparison]::OrdinalIgnoreCase) -or
        $Full.StartsWith($V2CachePath + '\', [StringComparison]::OrdinalIgnoreCase)) {
        [void]$ExpectedTaskOwnedSubtreeFiles.Add($Full)
    }
}
$ActualTaskOwnedSubtreeFiles = @($V2WorktreeTree.files | Where-Object {
    $_.StartsWith($V2SavesPath + '\', [StringComparison]::OrdinalIgnoreCase) -or
    $_.StartsWith($V2CachePath + '\', [StringComparison]::OrdinalIgnoreCase)
})
if ($ActualTaskOwnedSubtreeFiles.Count -ne $ExpectedTaskOwnedSubtreeFiles.Count) {
    throw 'NEEDS_CONTEXT: extra or missing leaf appeared below a v2 task-owned subtree.'
}
foreach ($Full in $ActualTaskOwnedSubtreeFiles) {
    if (-not $ExpectedTaskOwnedSubtreeFiles.Contains($Full)) {
        throw ('NEEDS_CONTEXT: extra leaf appeared below a v2 task-owned subtree: ' + $Full)
    }
}

# The empty excluded array serializes to an empty relative catalog with one final LF byte.
if ((& git -C $V2GeneratorWorktree rev-parse HEAD).Trim() -cne $P2 -or
    (& git -C $V2GeneratorWorktree rev-parse HEAD:game).Trim() -cne $GameTree) {
    throw 'NEEDS_CONTEXT: v2 worktree topology drifted.'
}
& git -C $V2GeneratorWorktree diff --quiet --
if ($LASTEXITCODE -ne 0) { throw 'NEEDS_CONTEXT: v2 worktree tracked files drifted.' }
& git -C $V2GeneratorWorktree diff --cached --quiet --
if ($LASTEXITCODE -ne 0) { throw 'NEEDS_CONTEXT: v2 worktree index drifted.' }
$Untracked = @(& git -C $V2GeneratorWorktree ls-files --others --exclude-standard)
if ($LASTEXITCODE -ne 0 -or ($Untracked -join '|') -cne 'game/zz_terminal_collapse_legacy_fixture.rpy') {
    throw 'NEEDS_CONTEXT: v2 worktree untracked inventory drifted.'
}
$ExpectedIgnored = New-Object 'System.Collections.Generic.List[string]'
foreach ($Leaf in @($WorktreeInventory.authority_files)) {
    if ([string]$Leaf.relative_path -cne 'game\zz_terminal_collapse_legacy_fixture.rpy') {
        $ExpectedIgnored.Add(([string]$Leaf.relative_path).Replace('\', '/'))
    }
}
foreach ($Leaf in @($WorktreeInventory.excluded_cache_files)) {
    $ExpectedIgnored.Add(([string]$Leaf.relative_path).Replace('\', '/'))
}
$ActualIgnored = [string[]]@(& git -C $V2GeneratorWorktree ls-files --others --ignored --exclude-standard)
if ($LASTEXITCODE -ne 0) { throw 'NEEDS_CONTEXT: v2 worktree ignored enumeration failed.' }
$ExpectedIgnoredSorted = [string[]]$ExpectedIgnored.ToArray()
[Array]::Sort($ExpectedIgnoredSorted, [StringComparer]::Ordinal)
[Array]::Sort($ActualIgnored, [StringComparer]::Ordinal)
if ($ActualIgnored.Count -ne 68 -or
    ($ActualIgnored -join "`n") -cne ($ExpectedIgnoredSorted -join "`n")) {
    throw 'NEEDS_CONTEXT: v2 worktree ignored authority/cache inventory drifted.'
}

$SaveDirectories = @($V2SaveTree.directories | Where-Object { $_ -cne (Get-Task0CanonicalPath $V2GeneratorSaveDir) })
$SaveFiles = [string[]]$V2SaveTree.files
if ($SaveDirectories.Count -ne 1 -or
    $SaveDirectories[0].Substring($V2GeneratorSaveDir.Length + 1) -cne 'sync' -or
    $SaveFiles.Count -ne 12) {
    throw 'NEEDS_CONTEXT: v2 SaveDir exact structure drifted.'
}
$ExpectedSaveRelative = [string[]]@($SaveDirInventory.authority_files | ForEach-Object { [string]$_.relative_path })
$ActualSaveRelative = [string[]]@($SaveFiles | ForEach-Object { $_.Substring($V2GeneratorSaveDir.Length + 1) })
[Array]::Sort($ExpectedSaveRelative, [StringComparer]::Ordinal)
[Array]::Sort($ActualSaveRelative, [StringComparer]::Ordinal)
if (($ActualSaveRelative -join "`n") -cne ($ExpectedSaveRelative -join "`n")) {
    throw 'NEEDS_CONTEXT: v2 SaveDir relative-file set drifted.'
}
```

Expected: both ordered failure records and all six preserved candidates match their current seals, the v2 stdout still contains exactly one PASSED while its engine log contains zero Status lines, and the exact 8/61 worktree plus 12/0 SaveDir inventories remain unchanged. Neither failed save lineage is opened, copied, promoted, or altered.

- [ ] **Step 4: Prove the zero-launch/create-new boundary and close Task 0**

Continue in the same Task 0 session:

```powershell
$ExpectedHelpers = [ordered]@{
    'PrivateDesktopRunner.cs' = [pscustomobject]@{
        Bytes = [int64]82334
        Sha256 = 'E0393DB1E113FDB8C35097978AA73B7D33AFDD5788499002B6423D883DEED4E8'
    }
    'Invoke-PrivateDesktopProcess.ps1' = [pscustomobject]@{
        Bytes = [int64]24229
        Sha256 = '73A3F9C43CF994E08F004E0A1266122A3EC5E0EAF065C63E6D9439CF0B0E1880'
    }
    'Test-PrivateDesktopRunner.ps1' = [pscustomobject]@{
        Bytes = [int64]53188
        Sha256 = '20198B669F70E51E51F71BD01E6D06D1949D300F43CE9A94FB0190A47D781A15'
    }
}
$HelperRoot = Join-Path $EvidenceRoot 'helpers'
foreach ($Name in $ExpectedHelpers.Keys) {
    $Path = Join-Path $HelperRoot $Name
    $Seal = Get-Task0FileSeal $Path
    if ([int64]$Seal.bytes -ne [int64]$ExpectedHelpers[$Name].Bytes -or
        [string]$Seal.sha256 -cne [string]$ExpectedHelpers[$Name].Sha256 -or
        -not $ManifestArtifactSet.Contains([string]$Seal.path)) {
        throw ('NEEDS_CONTEXT: helper seal drifted: ' + $Name)
    }
}

$WinterPlan = 'docs/superpowers/plans/2026-08-09-winter-interlude-narrative-delivery.md'
if ((Get-FileHash -LiteralPath $WinterPlan -Algorithm SHA256).Hash -cne
        '0F39B5F5ACE1D4666DD146863CABDF398B031F5666C29AE337CEB89796E4276C' -or
    @(git diff --cached --name-only).Count -ne 0 -or
    (@(git status --short --untracked-files=all) -join '|') -cne ('?? ' + $WinterPlan)) {
    throw 'NEEDS_CONTEXT: protected shared worktree state drifted.'
}

$RecoveryTree = Get-Task0NonFollowingTree $RecoveryRoot 'pre-Task1 recovery-v3 namespace'
if ($RecoveryTree.directories.Count -ne 1 -or $RecoveryTree.files.Count -ne 1 -or
    [string]$RecoveryTree.files[0] -cne $ExpectedManifestPath) {
    throw 'NEEDS_CONTEXT: Task 1 durable path exists before Task 1 authorization.'
}
$ForbiddenCreateNew = [string[]]@(
    (Join-Path $RecoveryRoot 'generator-contract-red.json'),
    (Join-Path $RecoveryRoot 'generator-contract-green.json'),
    $ExpectedGeneratorLedgerPath,
    (Join-Path $RecoveryRoot 'generator-process'),
    (Join-Path $RecoveryRoot 'generator-state.json'),
    (Join-Path $RecoveryRoot 'generator-fixture.rpy'),
    (Join-Path $RecoveryRoot 'generator-engine-log.txt'),
    $ExpectedObserverLedgerPath,
    (Join-Path $RecoveryRoot 'observer-process'),
    (Join-Path $RecoveryRoot 'observer-state.json'),
    (Join-Path $RecoveryRoot 'observer-fixture.rpy'),
    (Join-Path $RecoveryRoot 'observer-engine-log.txt'),
    (Join-Path $RecoveryRoot 'mother'),
    (Join-Path $RecoveryRoot 'baseline-evidence.md'),
    (Join-Path $RecoveryRoot 'task1-completion.json')
)
$TemporaryRoots = [string[]]@(
    'E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-generator-recovery-v3',
    'E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-generator-save-recovery-v3',
    'E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-observer-recovery-v3',
    'E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-observer-save-recovery-v3'
)
foreach ($Path in @($ForbiddenCreateNew) + @($TemporaryRoots)) {
    if (Test-Path -LiteralPath $Path) {
        throw ('NEEDS_CONTEXT: create-new Task 1 path already exists: ' + $Path)
    }
}

# Save the outer Win32_Process object in a named variable and exclude this PowerShell PID.
# Do not use nested Where-Object blocks that reuse $_.
$V3ProcessNeedles = [string[]]@(
    'cos-terminal-collapse-generator-recovery-v3',
    'cos-terminal-collapse-generator-save-recovery-v3',
    'cos-terminal-collapse-observer-recovery-v3',
    'cos-terminal-collapse-observer-save-recovery-v3',
    '\recovery-v3\generator-process',
    '\recovery-v3\observer-process'
)
$BlockedProcesses = New-Object 'System.Collections.Generic.List[object]'
$ProcessSnapshot = @(Get-WmiObject -Class Win32_Process -ErrorAction Stop)
foreach ($ProcessRecord in $ProcessSnapshot) {
    if ([int64]$ProcessRecord.ProcessId -eq [int64]$PID) { continue }
    $CommandLine = if ($null -eq $ProcessRecord.CommandLine) { '' } else { [string]$ProcessRecord.CommandLine }
    foreach ($Needle in $V3ProcessNeedles) {
        if ($CommandLine.IndexOf($Needle, [StringComparison]::OrdinalIgnoreCase) -ge 0) {
            $BlockedProcesses.Add([pscustomobject]@{
                process_id = [int64]$ProcessRecord.ProcessId
                name = [string]$ProcessRecord.Name
                matched = $Needle
            })
            break
        }
    }
}
if ($BlockedProcesses.Count -ne 0) {
    throw 'NEEDS_CONTEXT: a v3 Task 1 process exists before Task 1 authorization.'
}

[pscustomobject]@{
    status = 'PASS'
    task = 0
    approved_plan_commit = $P3
    approval_lock_sha256 = $ApprovalLockSha256
    lock_schema = 3
    lock_fields = 26
    predecessor_schema = 2
    predecessor_artifacts = 115
    catalog_bytes = 24660
    generator_invocations_v3 = 0
    observer_invocations_v3 = 0
    helper_or_renpy_launches = 0
    files_created_by_task0 = 0
}
```

Expected: one static `PASS`; helper sources, protected winter file, empty shared index, manifest-only v3 runtime namespace, absent ledgers/temp roots, and no matching v3 process all pass. Close this session. Do not continue Task 1 in it, and do not create a Task 0 completion file.

---

Controller sealing and Task 0 are complete only when every checkbox above passes in its prescribed session and the independent reviewer has supplied the lock SHA-256 out of band. Task 1 begins in a different fresh Windows PowerShell 5.1 Desktop session and must repeat lock-first validation before creating any RED/GREEN record or one-shot ledger.
## Task 1: Generate, observe, and seal one fresh Recovery v3 final-tactics save

**Files:**

- Read only: `.superpowers/sdd/terminal-collapse-ending/approved-plan-lock-v3.json`
- Read only: `.superpowers/sdd/terminal-collapse-ending/recovery-v3/predecessor-evidence.json`
- Read only: `.superpowers/sdd/terminal-collapse-ending/recovery-v2/generator-process/stdout.txt`
- Read only: the v2 generator worktree `log.txt`
- Read only: `.superpowers/sdd/terminal-collapse-ending/helpers/PrivateDesktopRunner.cs`
- Read only: `.superpowers/sdd/terminal-collapse-ending/helpers/Invoke-PrivateDesktopProcess.ps1`
- Read only: `E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-generator-c2958b40c6044ce598e56263855c071d\game\zz_terminal_collapse_legacy_fixture.rpy`
- Temporary create: `E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-generator-recovery-v3\game\zz_terminal_collapse_legacy_fixture.rpy`
- Temporary create: `E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-observer-recovery-v3\game\zz_terminal_collapse_legacy_observer.rpy`
- Create ignored: `.superpowers/sdd/terminal-collapse-ending/recovery-v3/generator-contract-red.json` — also the immutable pre-patch checkpoint
- Create ignored: `.superpowers/sdd/terminal-collapse-ending/recovery-v3/generator-contract-green.json` — exact 42-case offline stream/fixture contract
- Create ignored: `.superpowers/sdd/terminal-collapse-ending/recovery-v3/generator-attempt/attempt.json`
- Create ignored: `.superpowers/sdd/terminal-collapse-ending/recovery-v3/generator-attempt/completion.json`
- Create ignored: `.superpowers/sdd/terminal-collapse-ending/recovery-v3/generator-process/{request.json,stdout.txt,stderr.txt,result.json}`
- Create ignored: `.superpowers/sdd/terminal-collapse-ending/recovery-v3/generator-state.json`
- Create ignored: `.superpowers/sdd/terminal-collapse-ending/recovery-v3/generator-fixture.rpy`
- Create ignored: `.superpowers/sdd/terminal-collapse-ending/recovery-v3/generator-engine-log.txt`
- Create ignored: `.superpowers/sdd/terminal-collapse-ending/recovery-v3/observer-attempt/attempt.json`
- Create ignored: `.superpowers/sdd/terminal-collapse-ending/recovery-v3/observer-attempt/completion.json`
- Create ignored: `.superpowers/sdd/terminal-collapse-ending/recovery-v3/observer-process/{request.json,stdout.txt,stderr.txt,result.json}`
- Create ignored: `.superpowers/sdd/terminal-collapse-ending/recovery-v3/observer-state.json`
- Create ignored: `.superpowers/sdd/terminal-collapse-ending/recovery-v3/observer-fixture.rpy`
- Create ignored: `.superpowers/sdd/terminal-collapse-ending/recovery-v3/observer-engine-log.txt`
- Create ignored: `.superpowers/sdd/terminal-collapse-ending/recovery-v3/mother/1-1-*.save`
- Create ignored: `.superpowers/sdd/terminal-collapse-ending/recovery-v3/baseline-evidence.md`
- Create ignored: `.superpowers/sdd/terminal-collapse-ending/recovery-v3/task1-completion.json`

**Interfaces:**

- Consumes: controller-supplied uppercase `$ApprovalLockSha256`; after PRE_PATCH, the controller-carried uppercase `$GeneratorRedCheckpointSha256`; after the generator, the carried uppercase generator-completion checkpoint for the observer host patch; after the observer/mother, the carried uppercase generator-completion, observer-completion, and mother checkpoints for cleanup; the exact P2→S3→P3 authority; the read-only schema-v2 115-file predecessor manifest; the unchanged private-desktop wrapper; reused full-selftest/version evidence; Ren'Py 8.5.2; the old 8,749-byte fixture and frozen v2 stdout/engine log only as offline RED inputs.
- Produces: immutable schema-v3 RED/GREEN contract records; exactly one schema-v2 generator and one schema-v2 observer attempt/completion; one read-only mother derived only from the fresh v3 generator; schema-v3 `task1-completion.json` with an exact 115+26=141-file current union.
- Non-authority handoff clarification: the generator-to-observer seam additionally carries the bounded generator AppData observation base64/SHA; the observer-to-cleanup seam carries that generator SHA and the bounded complete AppData observation base64/SHA. These sealed aggregates are never authority, artifacts, package inputs, or new durable leaves.

Task 1 deliberately crosses two host-tool seams and four fresh Windows PowerShell 5.1 scopes. PRE_PATCH authenticates authority, creates the detached generator worktree, freezes RED, prints its uppercase checkpoint, and ends. The host applies the generator fixture exactly once. POST_PATCH authenticates lock+RED authority hashes, freezes GREEN, runs the sole generator, prepares a clean observer worktree, prints the generator-completion checkpoint plus a bounded non-authority AppData observation handoff, and ends. The host applies the observer fixture exactly once. POST_OBSERVER_PATCH authenticates the authority checkpoints before decoding the hash-sealed non-authority observation, reconstructs the exact fixture bytes from the authenticated plan, runs the sole observer, fresh-rereads both completions, freezes the mother, prints the cleanup checkpoints plus the complete AppData observation handoff, and ends. CLEANUP authenticates the explicit authority checkpoints before decoding the observation, strictly rebuilds every authority input from physical evidence, removes exactly four hard-allowlisted completion-derived paths, and builds baseline/Task 1 completion. Any failed check is terminal: preserve every path created by the task and do not retry, replace a GUID, create another evidence root, start the observer after a generator failure, create the mother before observer completion, or clean a failed worktree/SaveDir. Neither the old full selftest nor the old version probe is invoked. No code uses Computer Use, real input, or a visible desktop.

Ren'Py may update its ordinary backup area during either invocation. Observe only the two exact canonical paths `C:\Users\22325\AppData\Roaming\RenPy\backups\cos-terminal-collapse-generator-recovery-v3` and `...\cos-terminal-collapse-observer-recovery-v3`, immediately before and after their respective one-shot launches. Each metadata-only traversal is read-only, `-Force`, non-following, Ordinal, capped at 4,096 descendants, 4 MiB of canonical catalog bytes, and 10 seconds; any reparse point, case-fold collision, or bound breach is terminal. Carry only hash-sealed aggregate snapshots across fresh scopes and record every snapshot field in the existing baseline. These paths are non-authority, never part of the 141-leaf union, and never deleted or cleaned. Any tracked/shared-repository drift remains terminal.

- [ ] **Step 0: Validate the complete v3 lock-first authority and declare every one-shot path before creating a file**

The controller binds `$ApprovalLockSha256` as a scriptblock parameter when it creates the first fresh scope. This is the first project action in that scope:

```powershell
$Task1BootstrapPhase = 'PRE_PATCH'
# TASK1_V3_BOOTSTRAP_BEGIN
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
if ($PSVersionTable.PSEdition -cne 'Desktop' -or $PSVersionTable.PSVersion.Major -ne 5) {
    throw 'NEEDS_CONTEXT: Task 1 requires Windows PowerShell 5.1 Desktop.'
}
$ApprovalVariable = Get-Variable -Name ApprovalLockSha256 -Scope 0 -ErrorAction SilentlyContinue
if ($null -eq $ApprovalVariable -or $ApprovalVariable.Value -isnot [string] -or
    [string]$ApprovalVariable.Value -cnotmatch '^[0-9A-F]{64}$') {
    throw 'NEEDS_CONTEXT: controller did not bind the out-of-band approval_lock_sha256.'
}
$ApprovalLockSha256 = [string]$ApprovalVariable.Value
$KnownApprovalLockPath = 'C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\work\CourtOfShadows-governance-winter\.superpowers\sdd\terminal-collapse-ending\approved-plan-lock-v3.json'
if (-not (Test-Path -LiteralPath $KnownApprovalLockPath -PathType Leaf)) {
    throw 'NEEDS_CONTEXT: known approval lock leaf is missing.'
}
if ((Get-FileHash -LiteralPath $KnownApprovalLockPath -Algorithm SHA256).Hash -cne $ApprovalLockSha256) {
    throw 'NEEDS_CONTEXT: out-of-band approval lock hash authentication failed.'
}
$StrictUtf8 = New-Object System.Text.UTF8Encoding($false, $true)
$ProjectRoot = (Resolve-Path -LiteralPath '.').Path

function Get-RecoveryRawJsonObjectKeys([string]$Json, [string]$Context) {
    $Stack = New-Object 'System.Collections.Generic.Stack[object]'
    $Keys = New-Object 'System.Collections.Generic.List[string]'
    for ($Index = 0; $Index -lt $Json.Length; $Index++) {
        $Character = $Json[$Index]
        if ($Character -eq '{') {
            $Stack.Push((New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::Ordinal)))
        } elseif ($Character -eq '[') {
            $Stack.Push($null)
        } elseif ($Character -eq '}' -or $Character -eq ']') {
            if ($Stack.Count -eq 0) { throw ('NEEDS_CONTEXT: unbalanced JSON ' + $Context) }
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
                if ($Stack.Count -eq 0 -or $null -eq $Stack.Peek()) { throw ('NEEDS_CONTEXT: key outside object ' + $Context) }
                $Token = $Json.Substring($Start, $Index - $Start + 1)
                $Key = [string]($Token | ConvertFrom-Json -ErrorAction Stop)
                if (-not $Stack.Peek().Add($Key)) { throw ('NEEDS_CONTEXT: duplicate JSON key ' + $Key + ' ' + $Context) }
                [void]$Keys.Add($Key)
            }
        }
    }
    if ($Stack.Count -ne 0) { throw ('NEEDS_CONTEXT: unbalanced JSON containers ' + $Context) }
    return $Keys.ToArray()
}
function Read-RecoveryStrictJson([string]$Path, [string]$Context) {
    $Raw = [IO.File]::ReadAllBytes($Path)
    if ($Raw.Length -eq 0 -or
        ($Raw.Length -ge 3 -and $Raw[0] -eq 0xEF -and $Raw[1] -eq 0xBB -and $Raw[2] -eq 0xBF)) {
        throw ('NEEDS_CONTEXT: empty/BOM JSON ' + $Context)
    }
    $Text = $StrictUtf8.GetString($Raw)
    if ($Text.Contains([char]0xFFFD) -or -not $Text.EndsWith("`n", [StringComparison]::Ordinal) -or $Text.Contains("`r")) {
        throw ('NEEDS_CONTEXT: noncanonical UTF-8/LF JSON ' + $Context)
    }
    [void](Get-RecoveryRawJsonObjectKeys $Text $Context)
    return ($Text | ConvertFrom-Json -ErrorAction Stop)
}
function Read-HelperJson([string]$Path, [string]$Context) {
    $Raw = [IO.File]::ReadAllBytes($Path)
    if ($Raw.Length -eq 0 -or
        ($Raw.Length -ge 3 -and $Raw[0] -eq 0xEF -and $Raw[1] -eq 0xBB -and $Raw[2] -eq 0xBF)) {
        throw ('NEEDS_CONTEXT: empty/BOM helper JSON ' + $Context)
    }
    $Text = $StrictUtf8.GetString($Raw)
    if ($Text.Contains([char]0xFFFD)) { throw ('NEEDS_CONTEXT: invalid helper JSON UTF-8 ' + $Context) }
    [void](Get-RecoveryRawJsonObjectKeys $Text $Context)
    return ($Text | ConvertFrom-Json -ErrorAction Stop)
}
function Test-RecoveryIntegral($Value) {
    return ($Value -is [sbyte] -or $Value -is [byte] -or $Value -is [int16] -or
        $Value -is [uint16] -or $Value -is [int] -or $Value -is [uint32] -or
        $Value -is [long] -or $Value -is [uint64])
}
function Test-RoundtripUtc($Value) {
    if ($Value -isnot [string]) { return $false }
    $Parsed = [DateTimeOffset]::MinValue
    return [DateTimeOffset]::TryParseExact(
        [string]$Value,'o',[Globalization.CultureInfo]::InvariantCulture,
        [Globalization.DateTimeStyles]::RoundtripKind,[ref]$Parsed
    ) -and $Parsed.Offset -eq [TimeSpan]::Zero
}
function Assert-ExactProperties([object]$Object, [string[]]$Expected, [string]$Context) {
    if ($Object -isnot [pscustomobject] -or
        (@($Object.PSObject.Properties.Name) -join '|') -cne ($Expected -join '|')) {
        throw ('NEEDS_CONTEXT: inexact or reordered properties ' + $Context)
    }
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
function New-CreateOnlyUtf8File([string]$Path, [string]$Text) {
    if (-not $Text.EndsWith("`n", [StringComparison]::Ordinal) -or $Text.Contains("`r")) {
        throw ('Noncanonical LF payload: ' + $Path)
    }
    $Payload = $StrictUtf8.GetBytes($Text)
    $Stream = New-Object IO.FileStream -ArgumentList @(
        $Path, [IO.FileMode]::CreateNew, [IO.FileAccess]::Write, [IO.FileShare]::None,
        4096, [IO.FileOptions]::WriteThrough
    )
    try {
        $Stream.Write($Payload, 0, $Payload.Length)
        $Stream.Flush($true)
    } finally {
        $Stream.Dispose()
    }
}
function New-ReadOnlyJsonRecord([string]$Path, [System.Collections.Specialized.OrderedDictionary]$Payload, [string[]]$ExpectedProperties, [string]$Context) {
    $Text = (($Payload | ConvertTo-Json -Depth 16) -replace "`r`n", "`n") + "`n"
    New-CreateOnlyUtf8File $Path $Text
    $RoundTrip = Read-RecoveryStrictJson $Path $Context
    Assert-ExactProperties $RoundTrip $ExpectedProperties $Context
    (Get-Item -LiteralPath $Path).IsReadOnly = $true
    if (-not (Get-Item -LiteralPath $Path).IsReadOnly) { throw ('Could not make record read-only: ' + $Path) }
    return $RoundTrip
}
function New-FileSeal([string]$Path) {
    $Full = Get-CanonicalPath $Path
    $Item = Get-Item -LiteralPath $Full -Force -ErrorAction Stop
    if ($Item.PSIsContainer -or (($Item.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0)) {
        throw ('Expected ordinary leaf file: ' + $Full)
    }
    return [pscustomobject][ordered]@{
        path = $Full
        bytes = [int64]$Item.Length
        sha256 = (Get-FileHash -LiteralPath $Full -Algorithm SHA256).Hash
    }
}
function Get-RecoveryNonFollowingTree([string]$Root,[bool]$AllowMissing,[string]$Context) {
    $CanonicalRoot = Get-CanonicalPath $Root
    if (-not (Test-Path -LiteralPath $CanonicalRoot)) {
        if (-not $AllowMissing) { throw ('NEEDS_CONTEXT: inventory root is missing ' + $Context) }
        return [pscustomobject][ordered]@{
            root=$CanonicalRoot; exists=$false; directories=[string[]]@(); files=[string[]]@()
        }
    }
    $RootItem = Get-Item -LiteralPath $CanonicalRoot -Force -ErrorAction Stop
    if (-not $RootItem.PSIsContainer -or
        ($RootItem.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
        throw ('NEEDS_CONTEXT: inventory root is not an ordinary directory ' + $Context)
    }
    $DirectoryList = New-Object 'System.Collections.Generic.List[string]'
    $FileList = New-Object 'System.Collections.Generic.List[string]'
    $AllPathSet = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
    $Pending = New-Object 'System.Collections.Generic.Stack[string]'
    $Pending.Push($CanonicalRoot)
    while ($Pending.Count -gt 0) {
        $Current = $Pending.Pop()
        $ChildPaths = [string[]]@(
            Get-ChildItem -LiteralPath $Current -Force -ErrorAction Stop |
                ForEach-Object { Get-CanonicalPath $_.FullName }
        )
        [Array]::Sort($ChildPaths,[StringComparer]::Ordinal)
        foreach ($ChildPath in $ChildPaths) {
            $Child = Get-Item -LiteralPath $ChildPath -Force -ErrorAction Stop
            if (-not $AllPathSet.Add($ChildPath)) {
                throw ('NEEDS_CONTEXT: inventory tree contains a file/directory case-fold collision ' +
                    $Context + ': ' + $ChildPath)
            }
            if (($Child.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
                throw ('NEEDS_CONTEXT: inventory tree contains a reparse point ' + $Context + ': ' + $ChildPath)
            }
            if ($Child.PSIsContainer) {
                [void]$DirectoryList.Add($ChildPath)
                $Pending.Push($ChildPath)
            } else {
                [void]$FileList.Add($ChildPath)
            }
        }
    }
    $Directories = [string[]]$DirectoryList.ToArray()
    $Files = [string[]]$FileList.ToArray()
    [Array]::Sort($Directories,[StringComparer]::Ordinal)
    [Array]::Sort($Files,[StringComparer]::Ordinal)
    return [pscustomobject][ordered]@{
        root=$CanonicalRoot; exists=$true; directories=$Directories; files=$Files
    }
}
function Assert-RecoveryExactPhysicalTree(
    [string]$Root,[string[]]$ExpectedFiles,[string[]]$ExpectedDirectories,[string]$Context
) {
    $CanonicalRoot = Get-CanonicalPath $Root
    $Tree = Get-RecoveryNonFollowingTree $CanonicalRoot $false $Context
    $ExpectedFileSet = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
    $ExpectedDirectorySet = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
    $ActualFileSet = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
    $ActualDirectorySet = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
    $ExpectedFilePaths = New-Object 'System.Collections.Generic.List[string]'
    $ExpectedDirectoryPaths = New-Object 'System.Collections.Generic.List[string]'
    foreach ($ExpectedFile in $ExpectedFiles) {
        $Canonical = Get-CanonicalPath $ExpectedFile
        if ($ExpectedFile -cne $Canonical -or -not (Test-SameOrChildPath $Canonical $CanonicalRoot) -or
            $Canonical.Equals($CanonicalRoot,[StringComparison]::OrdinalIgnoreCase) -or
            -not $ExpectedFileSet.Add($Canonical)) {
            throw ('NEEDS_CONTEXT: expected physical file is noncanonical/outside/duplicate ' + $Context)
        }
        [void]$ExpectedFilePaths.Add($Canonical)
    }
    foreach ($ExpectedDirectory in $ExpectedDirectories) {
        $Canonical = Get-CanonicalPath $ExpectedDirectory
        if ($ExpectedDirectory -cne $Canonical -or -not (Test-SameOrChildPath $Canonical $CanonicalRoot) -or
            $Canonical.Equals($CanonicalRoot,[StringComparison]::OrdinalIgnoreCase) -or
            -not $ExpectedDirectorySet.Add($Canonical)) {
            throw ('NEEDS_CONTEXT: expected physical directory is noncanonical/outside/duplicate ' + $Context)
        }
        [void]$ExpectedDirectoryPaths.Add($Canonical)
    }
    foreach ($ActualFile in $Tree.files) {
        if (-not $ActualFileSet.Add([string]$ActualFile)) {
            throw ('NEEDS_CONTEXT: physical files contain a case-fold collision ' + $Context)
        }
    }
    foreach ($ActualDirectory in $Tree.directories) {
        if (-not $ActualDirectorySet.Add([string]$ActualDirectory)) {
            throw ('NEEDS_CONTEXT: physical directories contain a case-fold collision ' + $Context)
        }
    }
    $ExpectedFileArray = [string[]]$ExpectedFilePaths.ToArray()
    $ExpectedDirectoryArray = [string[]]$ExpectedDirectoryPaths.ToArray()
    $ActualFileArray = [string[]]$Tree.files
    $ActualDirectoryArray = [string[]]$Tree.directories
    [Array]::Sort($ExpectedFileArray,[StringComparer]::Ordinal)
    [Array]::Sort($ExpectedDirectoryArray,[StringComparer]::Ordinal)
    [Array]::Sort($ActualFileArray,[StringComparer]::Ordinal)
    [Array]::Sort($ActualDirectoryArray,[StringComparer]::Ordinal)
    if ($ActualFileArray.Count -ne $ExpectedFileArray.Count -or
        ($ActualFileArray -join "`n") -cne ($ExpectedFileArray -join "`n") -or
        $ActualDirectoryArray.Count -ne $ExpectedDirectoryArray.Count -or
        ($ActualDirectoryArray -join "`n") -cne ($ExpectedDirectoryArray -join "`n")) {
        throw ('NEEDS_CONTEXT: physical tree differs from the exact leaf/directory closure ' + $Context)
    }
    return $Tree
}

$P2 = '25c2ea674948ad89e8b48befb89643a8687648a4'
$S3 = '5fa8fb14792e095e066c3e9f698eda9ea4380854'
$S3SpecSha256 = '978116FE22B8C65578B78E800EF6039053284EA7E674271646D130BBB4BBF470'
$GameTree = 'fa7a398e9d989731b24e3c1642f3e2e33ce846ff'
$PlanPath = 'docs/superpowers/plans/2026-08-14-terminal-collapse-generator-recovery-v3.md'
$SpecPath = 'docs/superpowers/specs/2026-08-14-terminal-collapse-generator-recovery-v3-design.md'
$WinterPlan = 'docs/superpowers/plans/2026-08-09-winter-interlude-narrative-delivery.md'
$WinterSha256 = '0F39B5F5ACE1D4666DD146863CABDF398B031F5666C29AE337CEB89796E4276C'
$EvidenceRoot = Join-Path $ProjectRoot '.superpowers\sdd\terminal-collapse-ending'
$RecoveryRoot = Join-Path $EvidenceRoot 'recovery-v3'
$ApprovalLockPath = Join-Path $EvidenceRoot 'approved-plan-lock-v3.json'
if ([IO.Path]::GetFullPath($ApprovalLockPath).TrimEnd('\') -cne
    [IO.Path]::GetFullPath($KnownApprovalLockPath).TrimEnd('\')) {
    throw 'NEEDS_CONTEXT: authenticated lock path does not equal the bootstrap-derived lock path.'
}
$PredecessorLockPath = Join-Path $EvidenceRoot 'approved-plan-lock-v2.json'
$ManifestPath = Join-Path $RecoveryRoot 'predecessor-evidence.json'
$RunnerSource = Join-Path $EvidenceRoot 'helpers\PrivateDesktopRunner.cs'
$HeadlessWrapper = Join-Path $EvidenceRoot 'helpers\Invoke-PrivateDesktopProcess.ps1'
$TrustedSdkRoot = 'E:\Projects\renpy-8.5.2-sdk'
$RenPyExe = Join-Path $TrustedSdkRoot 'renpy.exe'
$TaskTempRoot = Join-Path $TrustedSdkRoot 'terminal-collapse-temp'
$OldGeneratorRoot = Join-Path $TaskTempRoot 'cos-terminal-collapse-generator-c2958b40c6044ce598e56263855c071d'
$OldFixturePath = Join-Path $OldGeneratorRoot 'game\zz_terminal_collapse_legacy_fixture.rpy'
$GeneratorRoot = Join-Path $TaskTempRoot 'cos-terminal-collapse-generator-recovery-v3'
$GeneratorSaveDir = Join-Path $TaskTempRoot 'cos-terminal-collapse-generator-save-recovery-v3'
$ObserverRoot = Join-Path $TaskTempRoot 'cos-terminal-collapse-observer-recovery-v3'
$ObserverSaveDir = Join-Path $TaskTempRoot 'cos-terminal-collapse-observer-save-recovery-v3'
$AppDataRoamingRoot = Get-CanonicalPath 'C:\Users\22325\AppData\Roaming'
$AppDataBackupRoot = Get-CanonicalPath 'C:\Users\22325\AppData\Roaming\RenPy\backups'
$GeneratorAppDataBackupPath = Get-CanonicalPath (Join-Path $AppDataBackupRoot (Split-Path $GeneratorRoot -Leaf))
$ObserverAppDataBackupPath = Get-CanonicalPath (Join-Path $AppDataBackupRoot (Split-Path $ObserverRoot -Leaf))
if ($env:APPDATA -isnot [string] -or -not [IO.Path]::IsPathRooted([string]$env:APPDATA) -or
    (Get-CanonicalPath ([string]$env:APPDATA)) -cne $AppDataRoamingRoot -or
    (Get-CanonicalPath (Split-Path $AppDataBackupRoot -Parent)) -cne
        (Get-CanonicalPath (Join-Path $AppDataRoamingRoot 'RenPy')) -or
    (Get-CanonicalPath (Split-Path $GeneratorAppDataBackupPath -Parent)) -cne $AppDataBackupRoot -or
    (Get-CanonicalPath (Split-Path $ObserverAppDataBackupPath -Parent)) -cne $AppDataBackupRoot) {
    throw 'NEEDS_CONTEXT: exact AppData backup observation paths are not canonical/current-user scoped.'
}
$RedRecordPath = Join-Path $RecoveryRoot 'generator-contract-red.json'
$GreenRecordPath = Join-Path $RecoveryRoot 'generator-contract-green.json'
$GeneratorAttemptDir = Join-Path $RecoveryRoot 'generator-attempt'
$GeneratorAttemptPath = Join-Path $GeneratorAttemptDir 'attempt.json'
$GeneratorCompletionPath = Join-Path $GeneratorAttemptDir 'completion.json'
$GeneratorProcessEvidence = Join-Path $RecoveryRoot 'generator-process'
$GeneratorStatePath = Join-Path $RecoveryRoot 'generator-state.json'
$GeneratorFixtureEvidence = Join-Path $RecoveryRoot 'generator-fixture.rpy'
$GeneratorLogEvidence = Join-Path $RecoveryRoot 'generator-engine-log.txt'
$ObserverAttemptDir = Join-Path $RecoveryRoot 'observer-attempt'
$ObserverAttemptPath = Join-Path $ObserverAttemptDir 'attempt.json'
$ObserverCompletionPath = Join-Path $ObserverAttemptDir 'completion.json'
$ObserverProcessEvidence = Join-Path $RecoveryRoot 'observer-process'
$ObserverStatePath = Join-Path $RecoveryRoot 'observer-state.json'
$ObserverFixtureEvidence = Join-Path $RecoveryRoot 'observer-fixture.rpy'
$ObserverLogEvidence = Join-Path $RecoveryRoot 'observer-engine-log.txt'
$MotherDir = Join-Path $RecoveryRoot 'mother'
$BaselineEvidencePath = Join-Path $RecoveryRoot 'baseline-evidence.md'
$Task1CompletionPath = Join-Path $RecoveryRoot 'task1-completion.json'
$V2RecoveryRoot = Join-Path $EvidenceRoot 'recovery-v2'
$V2AttemptPath = Join-Path $V2RecoveryRoot 'generator-attempt\attempt.json'
$V2StdoutPath = Join-Path $V2RecoveryRoot 'generator-process\stdout.txt'
$V2EngineLogPath = Join-Path $TaskTempRoot 'cos-terminal-collapse-generator-recovery-v2\log.txt'

if (-not (Test-Path -LiteralPath $ApprovalLockPath -PathType Leaf) -or
    (Get-FileHash -LiteralPath $ApprovalLockPath -Algorithm SHA256).Hash -cne $ApprovalLockSha256 -or
    -not (Get-Item -LiteralPath $ApprovalLockPath).IsReadOnly) {
    throw 'NEEDS_CONTEXT: v3 approval lock is missing, writable, or differs from the out-of-band hash.'
}
git check-ignore -q -- $ApprovalLockPath
if ($LASTEXITCODE -ne 0) { throw 'NEEDS_CONTEXT: v3 approval lock is not ignored.' }
$Approval = Read-RecoveryStrictJson $ApprovalLockPath 'approval lock v3'
$ExpectedLockProperties = @(
    'schema_version','purpose','approved_plan_path','approved_plan_commit','plan_sha256',
    'spec_path','spec_commit','spec_sha256','predecessor_plan_commit','predecessor_lock_path',
    'predecessor_lock_bytes','predecessor_lock_sha256','predecessor_manifest_path',
    'predecessor_manifest_bytes','predecessor_manifest_sha256','baseline_game_tree',
    'generator_strategy','superseded_generator_attempt_path','superseded_generator_attempt_sha256',
    'superseded_generator_disposition','generator_attempt_ledger_path','generator_attempt_limit',
    'observer_attempt_ledger_path','observer_attempt_limit','test_result_stream','engine_log_role'
)
Assert-ExactProperties $Approval $ExpectedLockProperties 'approval lock v3'
if ($Approval.schema_version -isnot [int] -or $Approval.schema_version -ne 3 -or
    $Approval.purpose -isnot [string] -or $Approval.purpose -cne 'terminal-collapse-generator-recovery-v3' -or
    $Approval.approved_plan_path -isnot [string] -or $Approval.approved_plan_path -cne $PlanPath -or
    $Approval.approved_plan_commit -isnot [string] -or $Approval.approved_plan_commit -cnotmatch '^[0-9a-f]{40}$' -or
    $Approval.plan_sha256 -isnot [string] -or $Approval.plan_sha256 -cnotmatch '^[0-9A-F]{64}$' -or
    $Approval.spec_path -isnot [string] -or $Approval.spec_path -cne $SpecPath -or
    $Approval.spec_commit -isnot [string] -or $Approval.spec_commit -cne $S3 -or
    $Approval.spec_sha256 -isnot [string] -or $Approval.spec_sha256 -cne $S3SpecSha256 -or
    $Approval.predecessor_plan_commit -isnot [string] -or $Approval.predecessor_plan_commit -cne $P2 -or
    $Approval.predecessor_lock_path -isnot [string] -or
    -not [IO.Path]::IsPathRooted([string]$Approval.predecessor_lock_path) -or
    [string]$Approval.predecessor_lock_path -cne (Get-CanonicalPath ([string]$Approval.predecessor_lock_path)) -or
    [string]$Approval.predecessor_lock_path -cne (Get-CanonicalPath $PredecessorLockPath) -or
    -not (Test-RecoveryIntegral $Approval.predecessor_lock_bytes) -or [int64]$Approval.predecessor_lock_bytes -ne 1957 -or
    $Approval.predecessor_lock_sha256 -isnot [string] -or
    $Approval.predecessor_lock_sha256 -cne '592E9F1FD5C4996A8612005BE9A33A35721A63228AAB43811208099265AECF8B' -or
    $Approval.predecessor_manifest_path -isnot [string] -or
    -not [IO.Path]::IsPathRooted([string]$Approval.predecessor_manifest_path) -or
    [string]$Approval.predecessor_manifest_path -cne (Get-CanonicalPath ([string]$Approval.predecessor_manifest_path)) -or
    [string]$Approval.predecessor_manifest_path -cne (Get-CanonicalPath $ManifestPath) -or
    -not (Test-RecoveryIntegral $Approval.predecessor_manifest_bytes) -or [int64]$Approval.predecessor_manifest_bytes -le 0 -or
    $Approval.predecessor_manifest_sha256 -isnot [string] -or $Approval.predecessor_manifest_sha256 -cnotmatch '^[0-9A-F]{64}$' -or
    $Approval.baseline_game_tree -isnot [string] -or $Approval.baseline_game_tree -cne $GameTree -or
    $Approval.generator_strategy -isnot [string] -or $Approval.generator_strategy -cne 'fresh_one_shot' -or
    $Approval.superseded_generator_attempt_path -isnot [string] -or
    -not [IO.Path]::IsPathRooted([string]$Approval.superseded_generator_attempt_path) -or
    [string]$Approval.superseded_generator_attempt_path -cne (Get-CanonicalPath ([string]$Approval.superseded_generator_attempt_path)) -or
    [string]$Approval.superseded_generator_attempt_path -cne (Get-CanonicalPath $V2AttemptPath) -or
    $Approval.superseded_generator_attempt_sha256 -isnot [string] -or
    $Approval.superseded_generator_attempt_sha256 -cne '6C6D597580E80A448C0CE55A80C0955988970C2A6332854049420B8693D38DF0' -or
    $Approval.superseded_generator_disposition -isnot [string] -or
    $Approval.superseded_generator_disposition -cne 'preserved_not_adopted_log_contract_mismatch' -or
    $Approval.generator_attempt_ledger_path -isnot [string] -or
    -not [IO.Path]::IsPathRooted([string]$Approval.generator_attempt_ledger_path) -or
    [string]$Approval.generator_attempt_ledger_path -cne (Get-CanonicalPath ([string]$Approval.generator_attempt_ledger_path)) -or
    [string]$Approval.generator_attempt_ledger_path -cne (Get-CanonicalPath $GeneratorAttemptDir) -or
    $Approval.generator_attempt_limit -isnot [int] -or $Approval.generator_attempt_limit -ne 1 -or
    $Approval.observer_attempt_ledger_path -isnot [string] -or
    -not [IO.Path]::IsPathRooted([string]$Approval.observer_attempt_ledger_path) -or
    [string]$Approval.observer_attempt_ledger_path -cne (Get-CanonicalPath ([string]$Approval.observer_attempt_ledger_path)) -or
    [string]$Approval.observer_attempt_ledger_path -cne (Get-CanonicalPath $ObserverAttemptDir) -or
    $Approval.observer_attempt_limit -isnot [int] -or $Approval.observer_attempt_limit -ne 1 -or
    $Approval.test_result_stream -isnot [string] -or $Approval.test_result_stream -cne 'helper_stdout' -or
    $Approval.engine_log_role -isnot [string] -or $Approval.engine_log_role -cne 'diagnostic_only') {
    throw 'NEEDS_CONTEXT: v3 approval lock schema/types/values failed.'
}
$P3 = [string]$Approval.approved_plan_commit
if ((& git rev-parse HEAD).Trim() -cne $P3 -or (& git rev-parse HEAD^).Trim() -cne $S3 -or
    (& git rev-parse ($S3 + '^')).Trim() -cne $P2 -or
    (git log -1 --format=%s) -cne 'docs: plan terminal collapse generator recovery v3' -or
    (@(git diff-tree --no-commit-id --name-only -r $P3) -join '|') -cne $PlanPath -or
    (@(git diff-tree --no-commit-id --name-only -r $S3) -join '|') -cne $SpecPath -or
    (& git rev-parse ($P3 + ':game')).Trim() -cne $GameTree) {
    throw 'NEEDS_CONTEXT: P2 -> S3 -> P3 topology failed.'
}
if ((Get-FileHash -LiteralPath $PlanPath -Algorithm SHA256).Hash -cne [string]$Approval.plan_sha256 -or
    (& git hash-object --no-filters -- $PlanPath).Trim() -cne (& git rev-parse ($P3 + ':' + $PlanPath)).Trim() -or
    (Get-FileHash -LiteralPath $SpecPath -Algorithm SHA256).Hash -cne [string]$Approval.spec_sha256 -or
    (& git hash-object --no-filters -- $SpecPath).Trim() -cne (& git rev-parse ($S3 + ':' + $SpecPath)).Trim()) {
    throw 'NEEDS_CONTEXT: physical/committed plan or spec drifted.'
}
if ((Get-FileHash -LiteralPath $WinterPlan -Algorithm SHA256).Hash -cne $WinterSha256 -or
    @(git diff --cached --name-only).Count -ne 0 -or
    (@(git status --short --untracked-files=all) -join '|') -cne ('?? ' + $WinterPlan)) {
    throw 'NEEDS_CONTEXT: protected shared worktree state drifted.'
}
if (-not (Test-Path -LiteralPath $ManifestPath -PathType Leaf) -or
    (Get-CanonicalPath ([string]$Approval.predecessor_manifest_path)) -cne (Get-CanonicalPath $ManifestPath) -or
    (Get-Item -LiteralPath $ManifestPath).Length -ne [int64]$Approval.predecessor_manifest_bytes -or
    (Get-FileHash -LiteralPath $ManifestPath -Algorithm SHA256).Hash -cne [string]$Approval.predecessor_manifest_sha256 -or
    -not (Get-Item -LiteralPath $ManifestPath).IsReadOnly) {
    throw 'NEEDS_CONTEXT: predecessor manifest seal drifted.'
}
$Manifest = Read-RecoveryStrictJson $ManifestPath 'predecessor manifest'
$ExpectedManifestProperties = @(
    'schema_version','purpose','predecessor_plan_commit','predecessor_lock_sha256',
    'artifact_count','catalog_bytes','catalog_sha256','artifacts','failures','source_inventories','created_utc'
)
Assert-ExactProperties $Manifest $ExpectedManifestProperties 'predecessor manifest'
$ManifestCreatedUtc = [DateTimeOffset]::MinValue
if ($Manifest.schema_version -isnot [int] -or $Manifest.schema_version -ne 2 -or
    $Manifest.purpose -isnot [string] -or $Manifest.purpose -cne 'terminal-collapse-generator-recovery-v3-predecessor' -or
    $Manifest.predecessor_plan_commit -isnot [string] -or $Manifest.predecessor_plan_commit -cne $P2 -or
    $Manifest.predecessor_lock_sha256 -isnot [string] -or $Manifest.predecessor_lock_sha256 -cne [string]$Approval.predecessor_lock_sha256 -or
    $Manifest.artifact_count -isnot [int] -or $Manifest.artifact_count -ne 115 -or
    $Manifest.catalog_bytes -isnot [int] -or $Manifest.catalog_bytes -ne 24660 -or
    $Manifest.catalog_sha256 -isnot [string] -or
    $Manifest.catalog_sha256 -cne '9694E728A82F6DDC743DA5E83967EAC7EE02FFA62FA53E21F4A2374F27DDDA24' -or
    @($Manifest.artifacts).Count -ne 115 -or @($Manifest.failures).Count -ne 2 -or
    @($Manifest.source_inventories).Count -ne 2 -or
    $Manifest.created_utc -isnot [string] -or
    -not [DateTimeOffset]::TryParseExact(
        [string]$Manifest.created_utc, 'o', [Globalization.CultureInfo]::InvariantCulture,
        [Globalization.DateTimeStyles]::RoundtripKind, [ref]$ManifestCreatedUtc
    )) {
    throw 'NEEDS_CONTEXT: predecessor manifest top-level contract failed.'
}
$FailureProperties = @(
    'id','classification','program_outcome','reason','generator_invocation_count','observer_invocation_count',
    'attempt_path','attempt_sha256','result_path','result_bytes','result_sha256','state_path','state_bytes',
    'state_sha256','test_report_path','test_report_bytes','test_report_sha256','engine_log_path',
    'engine_log_bytes','engine_log_sha256','target_copies','candidate_save_disposition'
)
for ($FailureIndex = 0; $FailureIndex -lt 2; $FailureIndex++) {
    $Failure = @($Manifest.failures)[$FailureIndex]
    Assert-ExactProperties $Failure $FailureProperties ('predecessor failure ' + $FailureIndex)
    if ($Failure.id -isnot [string] -or $Failure.classification -isnot [string] -or
        $Failure.program_outcome -isnot [string] -or
        ($null -ne $Failure.reason -and $Failure.reason -isnot [string]) -or
        $Failure.generator_invocation_count -isnot [int] -or $Failure.generator_invocation_count -ne 1 -or
        $Failure.observer_invocation_count -isnot [int] -or $Failure.observer_invocation_count -ne 0 -or
        $Failure.candidate_save_disposition -isnot [string] -or
        $Failure.candidate_save_disposition -cne 'preserved_not_used') {
        throw ('NEEDS_CONTEXT: predecessor failure types/lineage failed at index ' + $FailureIndex)
    }
    foreach ($Triple in @(
        @('result_path','result_bytes','result_sha256'),@('state_path','state_bytes','state_sha256'),
        @('test_report_path','test_report_bytes','test_report_sha256'),
        @('engine_log_path','engine_log_bytes','engine_log_sha256')
    )) {
        $PathValue = $Failure.($Triple[0])
        $BytesValue = $Failure.($Triple[1])
        $HashValue = $Failure.($Triple[2])
        if ($null -eq $PathValue) {
            if ($null -ne $BytesValue -or $null -ne $HashValue) {
                throw ('NEEDS_CONTEXT: partial null predecessor failure triple ' + $Triple[0])
            }
        } else {
            if ($PathValue -isnot [string] -or (Get-CanonicalPath ([string]$PathValue)) -cne [string]$PathValue -or
                -not (Test-RecoveryIntegral $BytesValue) -or [int64]$BytesValue -lt 0 -or
                $HashValue -isnot [string] -or $HashValue -cnotmatch '^[0-9A-F]{64}$') {
                throw ('NEEDS_CONTEXT: malformed predecessor failure triple ' + $Triple[0])
            }
            $FailureSeal = New-FileSeal ([string]$PathValue)
            if ($FailureSeal.bytes -ne [int64]$BytesValue -or $FailureSeal.sha256 -cne [string]$HashValue) {
                throw ('NEEDS_CONTEXT: predecessor failure leaf drifted ' + [string]$PathValue)
            }
        }
    }
    foreach ($TargetCopy in @($Failure.target_copies)) {
        Assert-ExactProperties $TargetCopy @('role','path','bytes','sha256') 'predecessor target copy'
        if ($TargetCopy.role -isnot [string] -or $TargetCopy.path -isnot [string] -or
            (Get-CanonicalPath ([string]$TargetCopy.path)) -cne [string]$TargetCopy.path -or
            -not (Test-RecoveryIntegral $TargetCopy.bytes) -or [int64]$TargetCopy.bytes -le 0 -or
            $TargetCopy.sha256 -isnot [string] -or $TargetCopy.sha256 -cnotmatch '^[0-9A-F]{64}$') {
            throw 'NEEDS_CONTEXT: malformed predecessor target copy.'
        }
        $TargetSeal = New-FileSeal ([string]$TargetCopy.path)
        if ($TargetSeal.bytes -ne [int64]$TargetCopy.bytes -or $TargetSeal.sha256 -cne [string]$TargetCopy.sha256) {
            throw ('NEEDS_CONTEXT: predecessor target copy drifted ' + [string]$TargetCopy.path)
        }
    }
}
$LegacyFailure = @($Manifest.failures)[0]
$V2Failure = @($Manifest.failures)[1]
if ($LegacyFailure.id -cne 'legacy_generator' -or $LegacyFailure.classification -cne 'TIMEOUT' -or
    $LegacyFailure.program_outcome -cne 'TIMEOUT' -or $null -ne $LegacyFailure.attempt_path -or
    $null -ne $LegacyFailure.attempt_sha256 -or
    $V2Failure.id -cne 'v2_generator' -or
    $V2Failure.classification -cne 'GOVERNANCE_CONTRACT_FAILURE' -or
    $V2Failure.program_outcome -cne 'COMPLETED' -or $V2Failure.reason -cne 'LOG_CONTRACT_MISMATCH' -or
    (Get-CanonicalPath ([string]$V2Failure.attempt_path)) -cne (Get-CanonicalPath $V2AttemptPath) -or
    $V2Failure.attempt_sha256 -cne '6C6D597580E80A448C0CE55A80C0955988970C2A6332854049420B8693D38DF0' -or
    [int64]$V2Failure.result_bytes -ne 1734 -or
    $V2Failure.result_sha256 -cne '12955539EC45CB4B3FA5490393EF511A851BD7CA3800F7835EBACAFFFF69D94F' -or
    [int64]$V2Failure.state_bytes -ne 2528 -or
    $V2Failure.state_sha256 -cne '43EDEB6BDFD217A7E9CDD969564A29B472D6D0258CF83ABD106F568A5B29D652' -or
    (Get-CanonicalPath ([string]$V2Failure.test_report_path)) -cne (Get-CanonicalPath $V2StdoutPath) -or
    [int64]$V2Failure.test_report_bytes -ne 1074 -or
    $V2Failure.test_report_sha256 -cne 'BD3B00124C6134FD0DAE737B293C20F68BF76F02ECDC69E77797C883FA5208CE' -or
    (Get-CanonicalPath ([string]$V2Failure.engine_log_path)) -cne (Get-CanonicalPath $V2EngineLogPath) -or
    [int64]$V2Failure.engine_log_bytes -ne 1860 -or
    $V2Failure.engine_log_sha256 -cne 'FE52BE91013D21B51AAF2CCDCF796289906EB4D12FA08EB1912A196B4F076A81' -or
    @($V2Failure.target_copies).Count -ne 3) {
    throw 'NEEDS_CONTEXT: ordered legacy/v2 failure semantics drifted.'
}
$SeenManifestPaths = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
$ManifestRows = New-Object 'System.Collections.Generic.List[string]'
$PreviousManifestPath = $null
foreach ($Artifact in @($Manifest.artifacts)) {
    Assert-ExactProperties $Artifact @('path','bytes','sha256') 'predecessor artifact'
    if ($Artifact.path -isnot [string] -or -not [IO.Path]::IsPathRooted([string]$Artifact.path) -or
        (Get-CanonicalPath ([string]$Artifact.path)) -cne [string]$Artifact.path -or
        -not (Test-RecoveryIntegral $Artifact.bytes) -or [int64]$Artifact.bytes -lt 0 -or
        $Artifact.sha256 -isnot [string] -or $Artifact.sha256 -cnotmatch '^[0-9A-F]{64}$' -or
        -not $SeenManifestPaths.Add([string]$Artifact.path) -or
        ($null -ne $PreviousManifestPath -and [StringComparer]::Ordinal.Compare($PreviousManifestPath, [string]$Artifact.path) -ge 0)) {
        throw ('NEEDS_CONTEXT: predecessor artifact schema/order/uniqueness failed: ' + [string]$Artifact.path)
    }
    $Current = New-FileSeal ([string]$Artifact.path)
    if ($Current.bytes -ne [int64]$Artifact.bytes -or $Current.sha256 -cne [string]$Artifact.sha256) {
        throw ('NEEDS_CONTEXT: predecessor artifact drifted: ' + [string]$Artifact.path)
    }
    [void]$ManifestRows.Add(([string]$Artifact.path + [char]9 + [string]$Artifact.bytes + [char]9 + [string]$Artifact.sha256))
    $PreviousManifestPath = [string]$Artifact.path
}
$ManifestCatalogBytes = $StrictUtf8.GetBytes(($ManifestRows -join "`n") + "`n")
$ManifestCatalogSha = [Security.Cryptography.SHA256]::Create()
try {
    $ManifestCatalogHash = [BitConverter]::ToString($ManifestCatalogSha.ComputeHash($ManifestCatalogBytes)).Replace('-', '')
} finally {
    $ManifestCatalogSha.Dispose()
}
if ($ManifestCatalogBytes.Length -ne 24660 -or
    $ManifestCatalogHash -cne '9694E728A82F6DDC743DA5E83967EAC7EE02FFA62FA53E21F4A2374F27DDDA24') {
    throw 'NEEDS_CONTEXT: predecessor catalog reconstruction failed.'
}
$InventoryProperties = @(
    'id','root_path','authority_file_count','authority_files','excluded_cache_count','excluded_cache_files'
)
$ExpectedInventoryIds = @('v2_generator_worktree_task_owned','v2_generator_savedir')
$ExpectedAuthorityCounts = @(8,12)
for ($InventoryIndex = 0; $InventoryIndex -lt 2; $InventoryIndex++) {
    $Inventory = @($Manifest.source_inventories)[$InventoryIndex]
    Assert-ExactProperties $Inventory $InventoryProperties ('source inventory ' + $InventoryIndex)
    if ($Inventory.id -isnot [string] -or $Inventory.id -cne $ExpectedInventoryIds[$InventoryIndex] -or
        $Inventory.root_path -isnot [string] -or
        (Get-CanonicalPath ([string]$Inventory.root_path)) -cne [string]$Inventory.root_path -or
        $Inventory.authority_file_count -isnot [int] -or
        $Inventory.authority_file_count -ne $ExpectedAuthorityCounts[$InventoryIndex] -or
        @($Inventory.authority_files).Count -ne $ExpectedAuthorityCounts[$InventoryIndex] -or
        $Inventory.excluded_cache_count -isnot [int] -or $Inventory.excluded_cache_count -lt 0 -or
        @($Inventory.excluded_cache_files).Count -ne $Inventory.excluded_cache_count) {
        throw ('NEEDS_CONTEXT: source inventory header drifted at index ' + $InventoryIndex)
    }
    $RelativeSeen = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
    foreach ($Kind in @('authority_files','excluded_cache_files')) {
        $PreviousRelative = $null
        foreach ($InventoryFile in @($Inventory.$Kind)) {
            Assert-ExactProperties $InventoryFile @('relative_path','bytes','sha256') ('source inventory ' + $Kind)
            if ($InventoryFile.relative_path -isnot [string] -or
                [IO.Path]::IsPathRooted([string]$InventoryFile.relative_path) -or
                [string]$InventoryFile.relative_path -match '(^|[\\/])\.\.([\\/]|$)' -or
                -not $RelativeSeen.Add([string]$InventoryFile.relative_path) -or
                ($null -ne $PreviousRelative -and
                    [StringComparer]::Ordinal.Compare($PreviousRelative,[string]$InventoryFile.relative_path) -ge 0) -or
                -not (Test-RecoveryIntegral $InventoryFile.bytes) -or [int64]$InventoryFile.bytes -lt 0 -or
                $InventoryFile.sha256 -isnot [string] -or $InventoryFile.sha256 -cnotmatch '^[0-9A-F]{64}$') {
                throw ('NEEDS_CONTEXT: source inventory file malformed ' + [string]$InventoryFile.relative_path)
            }
            $InventoryPath = Get-CanonicalPath (Join-Path ([string]$Inventory.root_path) ([string]$InventoryFile.relative_path))
            if (-not (Test-SameOrChildPath $InventoryPath ([string]$Inventory.root_path))) {
                throw ('NEEDS_CONTEXT: source inventory path escaped root ' + $InventoryPath)
            }
            $IsAuthority = $Kind -ceq 'authority_files'
            if ($SeenManifestPaths.Contains($InventoryPath) -ne $IsAuthority) {
                throw ('NEEDS_CONTEXT: source inventory authority membership mismatch ' + $InventoryPath)
            }
            $PreviousRelative = [string]$InventoryFile.relative_path
        }
    }
    foreach ($AuthorityFile in @($Inventory.authority_files)) {
        $AuthorityPath = Get-CanonicalPath `
            (Join-Path ([string]$Inventory.root_path) ([string]$AuthorityFile.relative_path))
        $AuthoritySeal = New-FileSeal $AuthorityPath
        if ($AuthoritySeal.bytes -ne [int64]$AuthorityFile.bytes -or
            $AuthoritySeal.sha256 -cne [string]$AuthorityFile.sha256) {
            throw ('NEEDS_CONTEXT: source inventory authority leaf drifted ' + $AuthorityPath)
        }
    }
}
# Spec 145: Task 0/controller owns the sealed extra-file and excluded-cache
# namespace proof. Task 1 validates excluded_cache_files metadata only and must
# not enumerate, traverse, Test-Path, Get-Item, or hash any current excluded leaf.
function Assert-RecoveryAuthorityUnchanged([string]$Context) {
    if (-not (Test-Path -LiteralPath $ApprovalLockPath -PathType Leaf) -or
        -not (Get-Item -LiteralPath $ApprovalLockPath).IsReadOnly -or
        (Get-FileHash -LiteralPath $ApprovalLockPath -Algorithm SHA256).Hash -cne $ApprovalLockSha256 -or
        -not (Test-Path -LiteralPath $ManifestPath -PathType Leaf) -or
        -not (Get-Item -LiteralPath $ManifestPath).IsReadOnly -or
        (Get-FileHash -LiteralPath $ManifestPath -Algorithm SHA256).Hash -cne [string]$Approval.predecessor_manifest_sha256 -or
        (Get-FileHash -LiteralPath $PlanPath -Algorithm SHA256).Hash -cne [string]$Approval.plan_sha256 -or
        (Get-FileHash -LiteralPath $SpecPath -Algorithm SHA256).Hash -cne [string]$Approval.spec_sha256 -or
        (& git rev-parse HEAD).Trim() -cne $P3 -or
        (& git rev-parse 'HEAD:game').Trim() -cne $GameTree -or
        @(git diff --cached --name-only).Count -ne 0 -or
        (@(git status --short --untracked-files=all) -join '|') -cne ('?? ' + $WinterPlan) -or
        (Get-FileHash -LiteralPath $WinterPlan -Algorithm SHA256).Hash -cne $WinterSha256) {
        throw ('NEEDS_CONTEXT: recovery authority drifted ' + $Context)
    }
    foreach ($SealedArtifact in @($Manifest.artifacts)) {
        $CurrentArtifact = New-FileSeal ([string]$SealedArtifact.path)
        if ($CurrentArtifact.bytes -ne [int64]$SealedArtifact.bytes -or
            $CurrentArtifact.sha256 -cne [string]$SealedArtifact.sha256) {
            throw ('NEEDS_CONTEXT: predecessor artifact drifted ' + $Context + ': ' + [string]$SealedArtifact.path)
        }
    }
}
Assert-RecoveryAuthorityUnchanged 'at Task 1 start'
foreach ($HelperSeal in @(
    [pscustomobject]@{ Path = $RunnerSource; Bytes = 82334; Hash = 'E0393DB1E113FDB8C35097978AA73B7D33AFDD5788499002B6423D883DEED4E8' },
    [pscustomobject]@{ Path = $HeadlessWrapper; Bytes = 24229; Hash = '73A3F9C43CF994E08F004E0A1266122A3EC5E0EAF065C63E6D9439CF0B0E1880' }
)) {
    if ((Get-Item -LiteralPath $HelperSeal.Path).Length -ne [int64]$HelperSeal.Bytes -or
        (Get-FileHash -LiteralPath $HelperSeal.Path -Algorithm SHA256).Hash -cne [string]$HelperSeal.Hash) {
        throw ('NEEDS_CONTEXT: helper source drifted: ' + [string]$HelperSeal.Path)
    }
}
foreach ($RequiredExternal in @($RenPyExe, $TaskTempRoot, $OldFixturePath)) {
    if (-not (Test-Path -LiteralPath $RequiredExternal)) { throw ('NEEDS_CONTEXT: required external input missing: ' + $RequiredExternal) }
}
if ((Get-Item -LiteralPath $OldFixturePath).Length -ne 8749 -or
    (Get-FileHash -LiteralPath $OldFixturePath -Algorithm SHA256).Hash -cne '497064A9DFCA721D1A6ED3A941A9DB0DC8DB92C489AD22F4E1ECF58A74E4CCC3') {
    throw 'NEEDS_CONTEXT: fixed RED fixture drifted.'
}
if ((Get-Item -LiteralPath $V2StdoutPath).Length -ne 1074 -or
    (Get-FileHash -LiteralPath $V2StdoutPath -Algorithm SHA256).Hash -cne
        'BD3B00124C6134FD0DAE737B293C20F68BF76F02ECDC69E77797C883FA5208CE' -or
    (Get-Item -LiteralPath $V2EngineLogPath).Length -ne 1860 -or
    (Get-FileHash -LiteralPath $V2EngineLogPath -Algorithm SHA256).Hash -cne
        'FE52BE91013D21B51AAF2CCDCF796289906EB4D12FA08EB1912A196B4F076A81') {
    throw 'NEEDS_CONTEXT: frozen v2 stream RED inputs drifted.'
}
$InitialRecoveryEntries = @(Get-ChildItem -LiteralPath $RecoveryRoot -Force)
$ExpectedInitialRecoveryPaths = @((Get-CanonicalPath $ManifestPath))
$ExpectedInitialContainerPaths = @()
if ($Task1BootstrapPhase -ceq 'PRE_PATCH') {
    # predecessor manifest only
} elseif ($Task1BootstrapPhase -ceq 'POST_PATCH') {
    $ExpectedInitialRecoveryPaths += @((Get-CanonicalPath $RedRecordPath))
} elseif ($Task1BootstrapPhase -ceq 'POST_OBSERVER_PATCH') {
    $ExpectedInitialRecoveryPaths += @(
        (Get-CanonicalPath $RedRecordPath),(Get-CanonicalPath $GreenRecordPath),
        (Get-CanonicalPath $GeneratorAttemptDir),(Get-CanonicalPath $GeneratorProcessEvidence),
        (Get-CanonicalPath $GeneratorStatePath),(Get-CanonicalPath $GeneratorFixtureEvidence),
        (Get-CanonicalPath $GeneratorLogEvidence)
    )
    $ExpectedInitialContainerPaths = @(
        (Get-CanonicalPath $GeneratorAttemptDir),(Get-CanonicalPath $GeneratorProcessEvidence)
    )
} elseif ($Task1BootstrapPhase -ceq 'CLEANUP') {
    $ExpectedInitialRecoveryPaths += @(
        (Get-CanonicalPath $RedRecordPath),(Get-CanonicalPath $GreenRecordPath),
        (Get-CanonicalPath $GeneratorAttemptDir),(Get-CanonicalPath $GeneratorProcessEvidence),
        (Get-CanonicalPath $GeneratorStatePath),(Get-CanonicalPath $GeneratorFixtureEvidence),
        (Get-CanonicalPath $GeneratorLogEvidence),(Get-CanonicalPath $ObserverAttemptDir),
        (Get-CanonicalPath $ObserverProcessEvidence),(Get-CanonicalPath $ObserverStatePath),
        (Get-CanonicalPath $ObserverFixtureEvidence),(Get-CanonicalPath $ObserverLogEvidence),
        (Get-CanonicalPath $MotherDir)
    )
    $ExpectedInitialContainerPaths = @(
        (Get-CanonicalPath $GeneratorAttemptDir),(Get-CanonicalPath $GeneratorProcessEvidence),
        (Get-CanonicalPath $ObserverAttemptDir),(Get-CanonicalPath $ObserverProcessEvidence),
        (Get-CanonicalPath $MotherDir)
    )
} else {
    throw 'NEEDS_CONTEXT: invalid Task1 bootstrap phase.'
}
$ActualInitialRecoveryPaths = @($InitialRecoveryEntries | ForEach-Object { Get-CanonicalPath $_.FullName })
$ActualInitialContainerPaths = @($InitialRecoveryEntries | Where-Object { $_.PSIsContainer } | ForEach-Object {
    Get-CanonicalPath $_.FullName
})
[Array]::Sort($ExpectedInitialRecoveryPaths,[StringComparer]::Ordinal)
[Array]::Sort($ActualInitialRecoveryPaths,[StringComparer]::Ordinal)
[Array]::Sort($ExpectedInitialContainerPaths,[StringComparer]::Ordinal)
[Array]::Sort($ActualInitialContainerPaths,[StringComparer]::Ordinal)
if (($ActualInitialRecoveryPaths -join '|') -cne ($ExpectedInitialRecoveryPaths -join '|') -or
    ($ActualInitialContainerPaths -join '|') -cne ($ExpectedInitialContainerPaths -join '|') -or
    @($InitialRecoveryEntries | Where-Object {
        ($_.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0
    }).Count -ne 0) {
    throw ('NEEDS_CONTEXT: recovery-v3 initial entries failed phase ' + $Task1BootstrapPhase)
}
$AlwaysAbsentPaths = @($BaselineEvidencePath,$Task1CompletionPath)
$RequiredPresentPaths = @($ManifestPath)
if ($Task1BootstrapPhase -ceq 'PRE_PATCH') {
    $AlwaysAbsentPaths += @(
        $RedRecordPath,$GreenRecordPath,$GeneratorAttemptDir,$GeneratorProcessEvidence,$GeneratorStatePath,
        $GeneratorFixtureEvidence,$GeneratorLogEvidence,$ObserverAttemptDir,$ObserverProcessEvidence,
        $ObserverStatePath,$ObserverFixtureEvidence,$ObserverLogEvidence,$MotherDir,
        $GeneratorRoot,$GeneratorSaveDir,$ObserverRoot,$ObserverSaveDir
    )
} elseif ($Task1BootstrapPhase -ceq 'POST_PATCH') {
    $RequiredPresentPaths += @($RedRecordPath,$GeneratorRoot)
    $AlwaysAbsentPaths += @(
        $GreenRecordPath,$GeneratorAttemptDir,$GeneratorProcessEvidence,$GeneratorStatePath,
        $GeneratorFixtureEvidence,$GeneratorLogEvidence,$ObserverAttemptDir,$ObserverProcessEvidence,
        $ObserverStatePath,$ObserverFixtureEvidence,$ObserverLogEvidence,$MotherDir,
        $GeneratorSaveDir,$ObserverRoot,$ObserverSaveDir
    )
} elseif ($Task1BootstrapPhase -ceq 'POST_OBSERVER_PATCH') {
    $RequiredPresentPaths += @(
        $RedRecordPath,$GreenRecordPath,$GeneratorAttemptDir,$GeneratorProcessEvidence,
        $GeneratorStatePath,$GeneratorFixtureEvidence,$GeneratorLogEvidence,$GeneratorRoot,
        $GeneratorSaveDir,$ObserverRoot
    )
    $AlwaysAbsentPaths += @(
        $ObserverAttemptDir,$ObserverProcessEvidence,$ObserverStatePath,$ObserverFixtureEvidence,
        $ObserverLogEvidence,$MotherDir,$ObserverSaveDir
    )
} else {
    $RequiredPresentPaths += @(
        $RedRecordPath,$GreenRecordPath,$GeneratorAttemptDir,$GeneratorProcessEvidence,
        $GeneratorStatePath,$GeneratorFixtureEvidence,$GeneratorLogEvidence,$ObserverAttemptDir,
        $ObserverProcessEvidence,$ObserverStatePath,$ObserverFixtureEvidence,$ObserverLogEvidence,
        $MotherDir,$GeneratorRoot,$GeneratorSaveDir,$ObserverRoot,$ObserverSaveDir
    )
}
foreach ($PresentPath in $RequiredPresentPaths) {
    if (-not (Test-Path -LiteralPath $PresentPath)) {
        throw ('NEEDS_CONTEXT: required Task 1 checkpoint path is missing: ' + $PresentPath)
    }
}
foreach ($AbsentPath in $AlwaysAbsentPaths) {
    if (Test-Path -LiteralPath $AbsentPath) { throw ('NEEDS_CONTEXT: create-new Task 1 path already exists: ' + $AbsentPath) }
}
if ((Test-SameOrChildPath $TaskTempRoot $ProjectRoot) -or (Test-SameOrChildPath $ProjectRoot $TaskTempRoot)) {
    throw 'NEEDS_CONTEXT: task temp root and repository must be disjoint.'
}
# TASK1_V3_BOOTSTRAP_END
```

Expected: the out-of-band v3 lock, exact P2→S3→P3 direct-parent chain, physical P3/S3 blobs, schema-v2 manifest, exact 115 current predecessor seals, both ordered failure lineages and source inventories, helper hashes, frozen v2 RED streams, empty index, protected winter file, and every create-new path pass. No Python, helper, or Ren'Py process has started.

- [ ] **Step 1: Run the offline AST and old-selector RED gates without creating a record**

Continue in the first scope. The AST gate runs with system CPython, never the Ren'Py SDK interpreter, and launches no Ren'Py code:

```powershell
# TASK1_V3_OFFLINE_GATE_BEGIN
$SystemPythonCommand = @(Get-Command python.exe -All -CommandType Application -ErrorAction Stop | Where-Object {
    -not [string]::IsNullOrWhiteSpace([string]$_.Source) -and
    (Test-Path -LiteralPath ([string]$_.Source) -PathType Leaf) -and
    -not (Get-CanonicalPath ([string]$_.Source)).StartsWith((Get-CanonicalPath $TrustedSdkRoot) + '\', [StringComparison]::OrdinalIgnoreCase)
} | Select-Object -First 1)
if ($SystemPythonCommand.Count -ne 1) {
    throw 'NEEDS_CONTEXT: no repository-external system CPython executable is available.'
}
$SystemPython = [string]$SystemPythonCommand[0].Source
if ((Get-CanonicalPath $SystemPython).StartsWith((Get-CanonicalPath $TrustedSdkRoot) + '\', [StringComparison]::OrdinalIgnoreCase)) {
    throw 'NEEDS_CONTEXT: AST gate must use system CPython, not the RenPy SDK interpreter.'
}
$AstGateSource = @'
import ast
import json
import os
import pathlib
import sys
import textwrap

path = pathlib.Path(os.environ["TC_AST_FIXTURE"])
raw = path.read_bytes()
text = raw.decode("utf-8-sig")
start_marker = "init -1000 python:\n"
end_marker = "\n\ntestsuite terminal_collapse_legacy_generator:"
parse_error_count = 0
try:
    start = text.index(start_marker) + len(start_marker)
    end = text.index(end_marker, start)
    source = textwrap.dedent(text[start:end])
    tree = ast.parse(source, filename=str(path))
except (SyntaxError, ValueError):
    parse_error_count = 1
    tree = ast.Module(body=[], type_ignores=[])

generator = next(
    (node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "_tc_generate_legacy_save"),
    None,
)
finish = None if generator is None else next(
    (node for node in generator.body if isinstance(node, ast.FunctionDef) and node.name == "finish"),
    None,
)
quit_call_count = 0
returned_finish_codes = []
if generator is not None:
    for node in ast.walk(generator):
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and node.func.attr == "quit"
        ):
            quit_call_count += 1
        if (
            isinstance(node, ast.Return)
            and isinstance(node.value, ast.Call)
            and isinstance(node.value.func, ast.Name)
            and node.value.func.id == "finish"
            and node.value.args
            and isinstance(node.value.args[-1], ast.Constant)
            and type(node.value.args[-1].value) is int
        ):
            returned_finish_codes.append(node.value.args[-1].value)

finish_returns_97 = False
finish_returns_code = False
if finish is not None:
    for node in ast.walk(finish):
        if isinstance(node, ast.Return) and isinstance(node.value, ast.Constant) and node.value.value == 97:
            finish_returns_97 = True
        if isinstance(node, ast.Return) and isinstance(node.value, ast.Name) and node.value.id == "code":
            finish_returns_code = True

logical_lines = [line.strip() for line in text.splitlines() if line.strip()]
native_tail = logical_lines[-3:] == [
    "$ _tc_generator_status = _tc_generate_legacy_save()",
    "assert eval (_tc_generator_status == 0)",
    "exit",
]
result = {
    "parse_error_count": parse_error_count,
    "quit_call_count": quit_call_count,
    "returned_finish_codes": sorted(returned_finish_codes),
    "finish_returns_97": finish_returns_97,
    "finish_returns_code": finish_returns_code,
    "native_tail": native_tail,
}
sys.stdout.write(json.dumps(result, ensure_ascii=True, separators=(",", ":")))
'@
function Invoke-GeneratorStructureGate([string]$FixturePath) {
    $SourceBase64 = [Convert]::ToBase64String($StrictUtf8.GetBytes($AstGateSource))
    $StartInfo = New-Object Diagnostics.ProcessStartInfo
    $StartInfo.FileName = $SystemPython
    $StartInfo.Arguments = '-c "import base64;exec(base64.b64decode(''' + $SourceBase64 + '''))"'
    $StartInfo.UseShellExecute = $false
    $StartInfo.CreateNoWindow = $true
    $StartInfo.RedirectStandardOutput = $true
    $StartInfo.RedirectStandardError = $true
    $StartInfo.EnvironmentVariables['TC_AST_FIXTURE'] = (Get-CanonicalPath $FixturePath)
    $AstGateTimeoutMilliseconds = 30000
    $AstGateTerminationMilliseconds = 10000
    $AstGateDrainMilliseconds = 10000
    $Process = New-Object Diagnostics.Process
    $Process.StartInfo = $StartInfo
    $StdoutTask = $null
    $StderrTask = $null
    $Stdout = ''
    $Stderr = ''
    $ExitCode = $null
    try {
        if (-not $Process.Start()) { throw 'System CPython AST gate did not start.' }
        $StdoutTask = $Process.StandardOutput.ReadToEndAsync()
        $StderrTask = $Process.StandardError.ReadToEndAsync()
        if (-not $Process.WaitForExit([int]$AstGateTimeoutMilliseconds)) {
            $KillError = ''
            try {
                $Process.Kill()
            } catch {
                $KillError = $_.Exception.Message
            }
            $ExitedAfterKill = $false
            try {
                $ExitedAfterKill = $Process.WaitForExit([int]$AstGateTerminationMilliseconds)
            } catch {
                if ([string]::IsNullOrEmpty($KillError)) { $KillError = $_.Exception.Message }
                else { $KillError += '; ' + $_.Exception.Message }
            }
            $HasExitedAfterKill = $false
            try {
                $HasExitedAfterKill = [bool]$Process.HasExited
            } catch {
                if ([string]::IsNullOrEmpty($KillError)) { $KillError = $_.Exception.Message }
                else { $KillError += '; ' + $_.Exception.Message }
            }
            $DrainedAfterKill = $false
            if ($null -ne $StdoutTask -and $null -ne $StderrTask) {
                try {
                    $DrainedAfterKill = [Threading.Tasks.Task]::WaitAll(
                        [Threading.Tasks.Task[]]@($StdoutTask,$StderrTask),
                        [int]$AstGateDrainMilliseconds
                    )
                } catch {
                    if ([string]::IsNullOrEmpty($KillError)) { $KillError = 'drain=' + $_.Exception.Message }
                    else { $KillError += '; drain=' + $_.Exception.Message }
                }
            }
            if (-not $ExitedAfterKill -or -not $HasExitedAfterKill) {
                throw ('NEEDS_CONTEXT: AST gate timed out and could not prove termination. detail=' + $KillError)
            }
            throw ('NEEDS_CONTEXT: AST gate exceeded 30000 ms and was terminated. drained=' +
                $DrainedAfterKill + '; detail=' + $KillError)
        }
        if (-not $Process.WaitForExit([int]$AstGateTerminationMilliseconds) -or
            -not [bool]$Process.HasExited) {
            throw 'NEEDS_CONTEXT: AST gate exit could not be re-proved after the bounded wait.'
        }
        try {
            $PipesDrained = [Threading.Tasks.Task]::WaitAll(
                [Threading.Tasks.Task[]]@($StdoutTask,$StderrTask),
                [int]$AstGateDrainMilliseconds
            )
        } catch {
            throw ('NEEDS_CONTEXT: AST gate pipe drain faulted: ' + $_.Exception.Message)
        }
        if (-not $PipesDrained) { throw 'NEEDS_CONTEXT: AST gate pipe drain exceeded 10000 ms.' }
        $Stdout = [string]$StdoutTask.Result
        $Stderr = [string]$StderrTask.Result
        $ExitCode = [int]$Process.ExitCode
    } finally {
        $Process.Dispose()
    }
    if ($ExitCode -ne 0 -or $Stderr -cne '' -or [string]::IsNullOrWhiteSpace($Stdout)) {
        throw ('NEEDS_CONTEXT: AST gate process failed. exit=' + $ExitCode + '; stderr=' + $Stderr)
    }
    return ($Stdout | ConvertFrom-Json -ErrorAction Stop)
}
$RedGate = Invoke-GeneratorStructureGate $OldFixturePath
Assert-ExactProperties $RedGate @(
    'parse_error_count','quit_call_count','returned_finish_codes','finish_returns_97','finish_returns_code','native_tail'
) 'RED AST result'
if ($RedGate.parse_error_count -isnot [int] -or $RedGate.parse_error_count -ne 0 -or
    $RedGate.quit_call_count -isnot [int] -or $RedGate.quit_call_count -ne 2 -or
    @($RedGate.returned_finish_codes).Count -ne 0 -or
    $RedGate.finish_returns_97 -isnot [bool] -or $RedGate.finish_returns_97 -or
    $RedGate.finish_returns_code -isnot [bool] -or $RedGate.finish_returns_code -or
    $RedGate.native_tail -isnot [bool] -or $RedGate.native_tail) {
    throw 'NEEDS_CONTEXT: RED did not fail for the exact approved exit-structure reason.'
}
function Read-StrictStreamText([string]$Path, [bool]$RequireNonEmpty, [bool]$RequireTerminalLf, [string]$Context) {
    $Bytes = [IO.File]::ReadAllBytes($Path)
    if (($RequireNonEmpty -and $Bytes.Length -eq 0) -or
        ($Bytes.Length -ge 3 -and $Bytes[0] -eq 0xEF -and $Bytes[1] -eq 0xBB -and $Bytes[2] -eq 0xBF)) {
        throw ('NEEDS_CONTEXT: empty/BOM stream ' + $Context)
    }
    $Text = $StrictUtf8.GetString($Bytes)
    if ($Text.IndexOf([char]0) -ge 0 -or $Text.IndexOf([char]0xFFFD) -ge 0 -or
        [regex]::IsMatch($Text,"`r(?!`n)")) {
        throw ('NEEDS_CONTEXT: NUL/invalid UTF-8/isolated CR stream ' + $Context)
    }
    if ($RequireTerminalLf -and $Bytes.Length -gt 0 -and $Bytes[$Bytes.Length - 1] -ne 0x0A) {
        throw ('NEEDS_CONTEXT: stream lacks terminal LF ' + $Context)
    }
    return $Text
}
$AnyStatusPattern = '(?m)^\[rpytest\] Status:[^\r\n]*\r?$'
$PassStatusPattern = '(?m)^\[rpytest\] Status:[ \t]+PASSED[ \t]*\r?$'
$SuitePattern = '(?m)^\[rpytest\] \[log\] - global\.terminal_collapse_legacy_generator[ \t]*\r?$'
$SummaryPattern = '(?m)^\[rpytest\] Test outcomes \(Summary\)[ \t]*\r?$'
$RpytestLinePattern = '(?m)^\[rpytest\]'
$V2TestReportText = Read-StrictStreamText $V2StdoutPath $true $true 'v2 test_report RED input'
$V2EngineLogText = Read-StrictStreamText $V2EngineLogPath $true $false 'v2 engine_boot_log RED input'
$V2TestReportStatusCount = [regex]::Matches($V2TestReportText,$PassStatusPattern).Count
$V2EngineLogStatusCount = [regex]::Matches($V2EngineLogText,$PassStatusPattern).Count
if ($V2TestReportStatusCount -ne 1 -or $V2EngineLogStatusCount -ne 0) {
    throw 'NEEDS_CONTEXT: frozen v2 streams no longer demonstrate the old selector mismatch.'
}
$RedFixtureGate = [ordered]@{
    expected = 'no_quit_returned_finish_native_exit'
    observed = 'two_quit_calls_no_returned_finish_no_native_exit'
    quit_call_count = 2
    returned_finish_codes = [object[]]@()
    returns_97 = $false
    returns_code = $false
    native_tail = $false
}
$RedStreamGate = [ordered]@{
    selector = 'engine_boot_log'
    test_report_status_count = 1
    engine_log_status_count = 0
    expected_failure = 'LOG_CONTRACT_MISMATCH'
}
# TASK1_V3_OFFLINE_GATE_END
```

Expected: parse errors are zero; the old generator has two `.quit()` calls, no returned `finish` calls, neither required `finish` return, and no native three-line tail. The frozen v2 helper stdout has one PASSED line while the v2 engine log has zero. This step creates no file and starts no Ren'Py/helper process.

The authenticated plan also owns one reusable production-validator block. These
functions are pure: they accept already-read objects/byte arrays and never open a
process, create a file, mutate a file, or inspect a process table. The offline
mutation suite and every live generator/observer/fresh-reread path call these same
functions; only the small envelope builders outside this block perform I/O:

```powershell
# TASK1_V3_PRODUCTION_VALIDATORS_BEGIN
$StrictUtf8 = New-Object System.Text.UTF8Encoding($false, $true)
$AnyStatusPattern = '(?m)^\[rpytest\] Status:[^\r\n]*\r?$'
$PassStatusPattern = '(?m)^\[rpytest\] Status:[ \t]+PASSED[ \t]*\r?$'
$SuitePattern = '(?m)^\[rpytest\] \[log\] - global\.terminal_collapse_legacy_generator[ \t]*\r?$'
$SummaryPattern = '(?m)^\[rpytest\] Test outcomes \(Summary\)[ \t]*\r?$'
$RpytestLinePattern = '(?m)^\[rpytest\]'
$GeneratorCompletionProperties = @(
    'schema_version','attempt_id','attempt_path','attempt_sha256','approval_lock_sha256',
    'approved_plan_commit','predecessor_manifest_sha256','red_record_sha256','green_record_sha256',
    'worktree_path','savedir_path','process_evidence_dir','fixture_path','fixture_sha256',
    'fixture_evidence_path','fixture_evidence_sha256','request_path','request_bytes','request_sha256',
    'result_path','result_bytes','result_sha256','state_path','state_bytes','state_sha256',
    'rpytest_stdout_path','rpytest_stdout_bytes','rpytest_stdout_sha256','stderr_path','stderr_bytes',
    'stderr_sha256','engine_log_evidence_path','engine_log_evidence_sha256','external_save_path',
    'sync_save_path','local_save_path','target_copy_count','save_name','save_bytes','save_sha256',
    'save_inventory','finished_utc'
)
$GeneratorAttemptProperties = @(
    'schema_version','attempt_id','started_utc','approval_lock_sha256','approved_plan_commit',
    'predecessor_manifest_sha256','red_record_path','red_record_sha256','green_record_path',
    'green_record_sha256','worktree_path','savedir_path','process_evidence_dir','state_path',
    'fixture_path','fixture_sha256','max_generator_invocations','retry_allowed'
)
$ObserverCompletionProperties = @(
    'schema_version','attempt_id','attempt_path','attempt_sha256','approval_lock_sha256',
    'approved_plan_commit','generator_completion_sha256','worktree_path','savedir_path',
    'process_evidence_dir','fixture_path','fixture_sha256','fixture_evidence_path',
    'fixture_evidence_sha256','request_path','request_bytes','request_sha256','result_path',
    'result_bytes','result_sha256','state_path','state_bytes','state_sha256','stdout_path',
    'stdout_bytes','stdout_sha256','stderr_path','stderr_bytes','stderr_sha256',
    'engine_log_evidence_path','engine_log_evidence_sha256','source_save_path','source_save_bytes',
    'source_save_sha256_before','source_save_sha256_after','replay_save_path','replay_save_bytes',
    'replay_save_sha256_before','replay_save_sha256_after','save_inventory','finished_utc'
)
$ObserverAttemptProperties = @(
    'schema_version','attempt_id','started_utc','approval_lock_sha256','approved_plan_commit',
    'generator_completion_path','generator_completion_sha256','worktree_path','savedir_path',
    'process_evidence_dir','state_path','fixture_path','fixture_sha256','source_save_path',
    'source_save_bytes','source_save_sha256','replay_save_path','max_observer_invocations','retry_allowed'
)
$GeneratorEnvironmentNames = @(
    'RENPY_NO_REDIRECT_STDIO','RENPY_PATH_TO_SAVES','RENPY_RENDERER','SDL_AUDIODRIVER',
    'SDL_VIDEODRIVER','TC_EXPECTED_BASELINE_COMMIT','TC_EXPECTED_FIXTURE_SHA256',
    'TC_EXPECTED_GAME_TREE','TC_EXPECTED_MARKER','TC_EXPECTED_SAVEDIR','TC_GENERATOR_RESULT'
)
$ObserverEnvironmentNames = @(
    'RENPY_AUTO_LOAD','RENPY_NO_REDIRECT_STDIO','RENPY_PATH_TO_SAVES','RENPY_RENDERER',
    'SDL_AUDIODRIVER','SDL_VIDEODRIVER','TC_EXPECTED_BASELINE_COMMIT',
    'TC_EXPECTED_FIXTURE_SHA256','TC_EXPECTED_GAME_TREE','TC_EXPECTED_MARKER',
    'TC_EXPECTED_SAVEDIR','TC_OBSERVER_RESULT'
)
$GeneratorStateActualProperties = @(
    'argument_savedir','command','configured_savedir','context_count','context_current',
    'display_captions','filename_line','is_in_test','is_top_context','node_file','node_line',
    'node_type','path_to_saves_env_present','raw_captions','return_stack','state','statement_name'
)
$GeneratorStateCheckProperties = @(
    'empty_return_stack','marker_inputs','menu_items','native_test','path_to_saves_absent',
    'production_menu_node','savedir','state','top_context'
)
$GeneratorPostSaveCheckProperties = @(
    'can_load','slot_choices','slot_commit','slot_game_tree','slot_marker','slot_menu','slot_state','store_marker'
)
$ObserverStateActualProperties = @(
    'argument_savedir','auto_load_value','command','configured_savedir','context_count',
    'context_current','display_captions','filename_line','is_in_test','is_top_context','node_file',
    'node_line','node_type','path_to_saves_env_present','raw_captions','return_stack',
    'slot_metadata','state','statement_name','store_marker'
)
$ObserverStateCheckProperties = @(
    'auto_load','empty_return_stack','menu_items','normal_run','path_to_saves_absent',
    'production_menu_node','savedir','slot_choices','slot_commit','slot_game_tree','slot_marker',
    'slot_menu','slot_state','state','store_marker','top_context'
)
$SlotMetadataProperties = @(
    '_ctime','_game_runtime','_renpy_version','_save_name','_version','tc_baseline_commit',
    'tc_choice_path','tc_game_tree','tc_legacy_marker','tc_legacy_schema','tc_menu_file',
    'tc_menu_line','tc_state'
)
$ExpectedChoicePath = @(
    '截断补给线——让他们饿三天再打','亲自率领前锋出击','记住这一切，继续前进'
)
$ExpectedDisplayCaptions = @('正面强攻，以气势压倒对方','采用迂回战术，先攻击敌军侧翼')
$ExpectedRawCaptions = @('正面强攻，以气势压倒对方|需权力≥60','采用迂回战术，先攻击敌军侧翼|需谋略≥55')
$EmptyFileSha256 = 'E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855'

function Test-V3ExactProperties([object]$Object,[string[]]$Expected) {
    return ($Object -is [pscustomobject] -and
        (@($Object.PSObject.Properties.Name) -join '|') -ceq ($Expected -join '|'))
}
function Test-V3ExactStringArray([object]$Actual,[string[]]$Expected) {
    if ($Actual -isnot [Array] -or @($Actual).Count -ne $Expected.Count) { return $false }
    for ($Index = 0; $Index -lt $Expected.Count; $Index++) {
        if (@($Actual)[$Index] -isnot [string] -or [string]@($Actual)[$Index] -cne $Expected[$Index]) {
            return $false
        }
    }
    return $true
}
function Test-V3FilenameLine([object]$Actual) {
    return ($Actual -is [Array] -and @($Actual).Count -eq 2 -and
        @($Actual)[0] -is [string] -and [string]@($Actual)[0] -ceq 'game/chapter5.rpy' -and
        (Test-RecoveryIntegral @($Actual)[1]) -and [int64]@($Actual)[1] -eq 2807)
}
function Test-V3EmptyArray([object]$Actual) {
    return ($null -ne $Actual -and $Actual -is [Array] -and @($Actual).Count -eq 0)
}
function Test-V3CanonicalExpectedPath([object]$Actual,[string]$Expected) {
    try {
        return ($Actual -is [string] -and [IO.Path]::IsPathRooted([string]$Actual) -and
            [string]$Actual -ceq (Get-CanonicalPath ([string]$Actual)) -and
            [string]$Actual -ceq (Get-CanonicalPath $Expected))
    } catch { return $false }
}
function Get-V3BytesSha256([byte[]]$Bytes) {
    $Hasher = [Security.Cryptography.SHA256]::Create()
    try { $Digest = $Hasher.ComputeHash($Bytes) } finally { $Hasher.Dispose() }
    return ([BitConverter]::ToString($Digest).Replace('-',''))
}
function Test-V3Hash([object]$Actual,[string]$Expected) {
    return ($Actual -is [string] -and [string]$Actual -cmatch '^[0-9A-F]{64}$' -and
        [string]$Actual -ceq $Expected)
}
function Test-V3SealContract([object]$Seal,[string]$ExpectedPath,[int64]$ExpectedBytes,[string]$ExpectedHash) {
    if (-not (Test-V3ExactProperties $Seal @('path','bytes','sha256'))) { return $false }
    return ((Test-V3CanonicalExpectedPath $Seal.path $ExpectedPath) -and
        (Test-RecoveryIntegral $Seal.bytes) -and [int64]$Seal.bytes -eq $ExpectedBytes -and
        (Test-V3Hash $Seal.sha256 $ExpectedHash))
}
function Test-V3OrderedBoolObject([object]$Object,[string[]]$ExpectedProperties) {
    if (-not (Test-V3ExactProperties $Object $ExpectedProperties)) { return $false }
    foreach ($Name in $ExpectedProperties) {
        if ($Object.$Name -isnot [bool] -or -not [bool]$Object.$Name) { return $false }
    }
    return $true
}
function Test-V3StateValue([object]$State) {
    return ((Test-V3ExactProperties $State @('intrigue','iron_prepared','power')) -and
        $State.intrigue -is [int] -and $State.intrigue -eq 55 -and
        $State.iron_prepared -is [bool] -and [bool]$State.iron_prepared -and
        $State.power -is [int] -and $State.power -eq 60)
}
function Test-V3SlotMetadataContract(
    [object]$Metadata,[string]$ExpectedMarker,[string]$ExpectedCommit,[string]$ExpectedGameTree
) {
    if (-not (Test-V3ExactProperties $Metadata $SlotMetadataProperties) -or
        $Metadata._ctime -isnot [double] -or [double]$Metadata._ctime -le 0 -or
        $Metadata._game_runtime -isnot [double] -or [double]$Metadata._game_runtime -lt 0 -or
        $Metadata._renpy_version -isnot [Array] -or @($Metadata._renpy_version).Count -ne 4 -or
        @($Metadata._renpy_version | Where-Object { $_ -isnot [int] }).Count -ne 0 -or
        (@($Metadata._renpy_version) -join ',') -cne '8,5,2,26010301' -or
        $Metadata._save_name -isnot [string] -or $Metadata._save_name -cne '' -or
        $Metadata._version -isnot [string] -or $Metadata._version -cne '3.10' -or
        $Metadata.tc_baseline_commit -isnot [string] -or $Metadata.tc_baseline_commit -cne $ExpectedCommit -or
        -not (Test-V3ExactStringArray $Metadata.tc_choice_path $ExpectedChoicePath) -or
        $Metadata.tc_game_tree -isnot [string] -or $Metadata.tc_game_tree -cne $ExpectedGameTree -or
        $Metadata.tc_legacy_marker -isnot [string] -or $Metadata.tc_legacy_marker -cne $ExpectedMarker -or
        $Metadata.tc_legacy_schema -isnot [int] -or $Metadata.tc_legacy_schema -ne 1 -or
        $Metadata.tc_menu_file -isnot [string] -or $Metadata.tc_menu_file -cne 'game/chapter5.rpy' -or
        $Metadata.tc_menu_line -isnot [int] -or $Metadata.tc_menu_line -ne 2807 -or
        -not (Test-V3StateValue $Metadata.tc_state)) { return $false }
    return $true
}
function Test-V3GeneratorStateContract(
    [object]$State,[string]$ExpectedSavedir,[string]$ExpectedMarker,
    [string]$ExpectedCommit,[string]$ExpectedGameTree
) {
    try {
        if (-not (Test-V3ExactProperties $State @(
                'actual','checks','failures','post_save_checks','reason','schema','slot_metadata','verdict'
            )) -or $State.schema -isnot [int] -or $State.schema -ne 1 -or
            $State.verdict -isnot [string] -or $State.verdict -cne 'PASS' -or
            $State.reason -isnot [string] -or
            $State.reason -cne 'native testcase saved the unchanged production final tactics Menu' -or
            -not (Test-V3EmptyArray $State.failures) -or
            -not (Test-V3ExactProperties $State.actual $GeneratorStateActualProperties) -or
            -not (Test-V3OrderedBoolObject $State.checks $GeneratorStateCheckProperties) -or
            -not (Test-V3OrderedBoolObject $State.post_save_checks $GeneratorPostSaveCheckProperties) -or
            -not (Test-V3SlotMetadataContract $State.slot_metadata $ExpectedMarker $ExpectedCommit $ExpectedGameTree)) {
            return 'REJECT'
        }
        $Actual = $State.actual
        if (-not (Test-V3CanonicalExpectedPath $Actual.argument_savedir $ExpectedSavedir) -or
            -not (Test-V3CanonicalExpectedPath $Actual.configured_savedir $ExpectedSavedir) -or
            $Actual.command -isnot [string] -or $Actual.command -cne 'test' -or
            $Actual.context_count -isnot [int] -or $Actual.context_count -ne 1 -or
            $Actual.context_current -isnot [string] -or
            $Actual.context_current -cnotmatch "^\('game/chapter5\.rpy', [0-9]+, [0-9]+\)$" -or
            -not (Test-V3ExactStringArray $Actual.display_captions $ExpectedDisplayCaptions) -or
            -not (Test-V3FilenameLine $Actual.filename_line) -or
            $Actual.is_in_test -isnot [bool] -or -not [bool]$Actual.is_in_test -or
            $Actual.is_top_context -isnot [bool] -or -not [bool]$Actual.is_top_context -or
            $Actual.node_file -isnot [string] -or $Actual.node_file -cne 'game/chapter5.rpy' -or
            $Actual.node_line -isnot [int] -or $Actual.node_line -ne 2807 -or
            $Actual.node_type -isnot [string] -or $Actual.node_type -cne 'Menu' -or
            $Actual.path_to_saves_env_present -isnot [bool] -or [bool]$Actual.path_to_saves_env_present -or
            -not (Test-V3ExactStringArray $Actual.raw_captions $ExpectedRawCaptions) -or
            -not (Test-V3EmptyArray $Actual.return_stack) -or -not (Test-V3StateValue $Actual.state) -or
            $Actual.statement_name -isnot [string] -or $Actual.statement_name -cne 'menu') { return 'REJECT' }
        return 'ACCEPT'
    } catch { return 'REJECT' }
}
function Test-V3ObserverStateContract(
    [object]$State,[string]$ExpectedSavedir,[string]$ExpectedMarker,
    [string]$ExpectedCommit,[string]$ExpectedGameTree,[object]$ExpectedSlotMetadata
) {
    try {
        if (-not (Test-V3ExactProperties $State @('actual','checks','failures','loaded','reason','schema','verdict')) -or
            $State.schema -isnot [int] -or $State.schema -ne 1 -or
            $State.verdict -isnot [string] -or $State.verdict -cne 'PASS' -or
            $State.loaded -isnot [bool] -or -not [bool]$State.loaded -or
            $State.reason -isnot [string] -or
            $State.reason -cne 'clean baseline normal-run autoload reached the production final tactics menu' -or
            -not (Test-V3EmptyArray $State.failures) -or
            -not (Test-V3ExactProperties $State.actual $ObserverStateActualProperties) -or
            -not (Test-V3OrderedBoolObject $State.checks $ObserverStateCheckProperties)) { return 'REJECT' }
        $Actual = $State.actual
        if (-not (Test-V3CanonicalExpectedPath $Actual.argument_savedir $ExpectedSavedir) -or
            -not (Test-V3CanonicalExpectedPath $Actual.configured_savedir $ExpectedSavedir) -or
            $Actual.auto_load_value -isnot [string] -or $Actual.auto_load_value -cne '1-1' -or
            $Actual.command -isnot [string] -or $Actual.command -cne 'run' -or
            $Actual.context_count -isnot [int] -or $Actual.context_count -ne 1 -or
            $Actual.context_current -isnot [string] -or
            $Actual.context_current -cnotmatch "^\('game/chapter5\.rpy', [0-9]+, [0-9]+\)$" -or
            -not (Test-V3ExactStringArray $Actual.display_captions $ExpectedDisplayCaptions) -or
            -not (Test-V3FilenameLine $Actual.filename_line) -or
            $Actual.is_in_test -isnot [bool] -or [bool]$Actual.is_in_test -or
            $Actual.is_top_context -isnot [bool] -or -not [bool]$Actual.is_top_context -or
            $Actual.node_file -isnot [string] -or $Actual.node_file -cne 'game/chapter5.rpy' -or
            $Actual.node_line -isnot [int] -or $Actual.node_line -ne 2807 -or
            $Actual.node_type -isnot [string] -or $Actual.node_type -cne 'Menu' -or
            $Actual.path_to_saves_env_present -isnot [bool] -or [bool]$Actual.path_to_saves_env_present -or
            -not (Test-V3ExactStringArray $Actual.raw_captions $ExpectedRawCaptions) -or
            -not (Test-V3EmptyArray $Actual.return_stack) -or -not (Test-V3StateValue $Actual.state) -or
            $Actual.statement_name -isnot [string] -or $Actual.statement_name -cne 'menu' -or
            $Actual.store_marker -isnot [string] -or $Actual.store_marker -cne $ExpectedMarker -or
            -not (Test-V3SlotMetadataContract $Actual.slot_metadata $ExpectedMarker $ExpectedCommit $ExpectedGameTree) -or
            (($Actual.slot_metadata | ConvertTo-Json -Depth 16 -Compress) -cne
                ($ExpectedSlotMetadata | ConvertTo-Json -Depth 16 -Compress))) { return 'REJECT' }
        return 'ACCEPT'
    } catch { return 'REJECT' }
}
function Test-V3RequestContract([string]$Mode,[object]$Request,[object]$Expected) {
    try {
        if ($Mode -cne 'generator' -and $Mode -cne 'observer') { return 'REJECT' }
        if (-not (Test-V3ExactProperties $Request @(
                'schema_version','executable','arguments','working_directory','environment_overrides',
                'timeout_milliseconds','stdout_path','stderr_path','result_path'
            )) -or -not (Test-V3ExactProperties $Expected @(
                'executable','arguments','working_directory','environment_names','environment_values',
                'timeout_milliseconds','stdout_path','stderr_path','result_path'
            )) -or $Request.schema_version -isnot [int] -or $Request.schema_version -ne 1 -or
            -not (Test-V3CanonicalExpectedPath $Request.executable ([string]$Expected.executable)) -or
            -not (Test-V3CanonicalExpectedPath $Request.working_directory ([string]$Expected.working_directory)) -or
            -not (Test-V3CanonicalExpectedPath $Request.stdout_path ([string]$Expected.stdout_path)) -or
            -not (Test-V3CanonicalExpectedPath $Request.stderr_path ([string]$Expected.stderr_path)) -or
            -not (Test-V3CanonicalExpectedPath $Request.result_path ([string]$Expected.result_path)) -or
            -not (Test-V3ExactStringArray $Request.arguments ([string[]]@($Expected.arguments))) -or
            -not (Test-RecoveryIntegral $Request.timeout_milliseconds) -or
            [int64]$Request.timeout_milliseconds -ne [int64]$Expected.timeout_milliseconds) { return 'REJECT' }
        $Entries = @($Request.environment_overrides)
        if ($Entries.Count -ne @($Expected.environment_names).Count -or
            $Entries.Count -ne @($Expected.environment_values).Count) { return 'REJECT' }
        $Seen = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::Ordinal)
        for ($Index = 0; $Index -lt $Entries.Count; $Index++) {
            $Entry = $Entries[$Index]
            if (-not (Test-V3ExactProperties $Entry @('name','value')) -or
                $Entry.name -isnot [string] -or
                ($null -ne $Entry.value -and $Entry.value -isnot [string])) { return 'REJECT' }
            if (-not $Seen.Add([string]$Entry.name)) { return 'REJECT' }
            if ([string]$Entry.name -cne [string]@($Expected.environment_names)[$Index]) { return 'REJECT' }
            $ExpectedValue = @($Expected.environment_values)[$Index]
            if ($null -eq $ExpectedValue) {
                if ($null -ne $Entry.value) { return 'REJECT' }
            } elseif ($ExpectedValue -isnot [string] -or $Entry.value -isnot [string] -or
                [string]$Entry.value -cne [string]$ExpectedValue) { return 'REJECT' }
        }
        return 'ACCEPT'
    } catch { return 'REJECT' }
}
function Test-V3ChannelContract([string]$Mode,[object]$Envelope) {
    try {
        if (($Mode -cne 'generator' -and $Mode -cne 'observer') -or
            -not (Test-V3ExactProperties $Envelope @(
                'stdout_exists','stdout_path','request_stdout_path','result_stdout_path','stdout_bytes',
                'stderr_exists','stderr_bytes','engine_exists','engine_source_path','engine_bytes','engine_evidence_seal'
            )) -or $Envelope.stdout_exists -isnot [bool] -or -not [bool]$Envelope.stdout_exists -or
            $Envelope.stderr_exists -isnot [bool] -or -not [bool]$Envelope.stderr_exists -or
            $Envelope.engine_exists -isnot [bool] -or -not [bool]$Envelope.engine_exists -or
            $Envelope.stdout_bytes -isnot [byte[]] -or $Envelope.stderr_bytes -isnot [byte[]] -or
            $Envelope.engine_bytes -isnot [byte[]] -or
            -not (Test-V3CanonicalExpectedPath $Envelope.stdout_path ([string]$Envelope.request_stdout_path)) -or
            -not (Test-V3CanonicalExpectedPath $Envelope.stdout_path ([string]$Envelope.result_stdout_path)) -or
            $Envelope.engine_source_path -isnot [string] -or
            -not [IO.Path]::IsPathRooted([string]$Envelope.engine_source_path) -or
            [string]$Envelope.engine_source_path -cne (Get-CanonicalPath ([string]$Envelope.engine_source_path)) -or
            [string]$Envelope.stdout_path -ceq [string]$Envelope.engine_source_path -or
            -not (Test-V3ExactProperties $Envelope.engine_evidence_seal @('path','bytes','sha256')) -or
            $Envelope.engine_evidence_seal.path -isnot [string] -or
            -not [IO.Path]::IsPathRooted([string]$Envelope.engine_evidence_seal.path) -or
            [string]$Envelope.engine_evidence_seal.path -cne
                (Get-CanonicalPath ([string]$Envelope.engine_evidence_seal.path)) -or
            -not (Test-RecoveryIntegral $Envelope.engine_evidence_seal.bytes) -or
            [int64]$Envelope.engine_evidence_seal.bytes -ne [int64]$Envelope.engine_bytes.Length -or
            -not (Test-V3Hash $Envelope.engine_evidence_seal.sha256 `
                (Get-V3BytesSha256 ([byte[]]$Envelope.engine_bytes))) -or
            $Envelope.stderr_bytes.Length -ne 0 -or $Envelope.engine_bytes.Length -eq 0) { return 'REJECT' }
        foreach ($Bytes in @($Envelope.stdout_bytes,$Envelope.engine_bytes)) {
            if ($Bytes.Length -ge 3 -and $Bytes[0] -eq 0xEF -and $Bytes[1] -eq 0xBB -and $Bytes[2] -eq 0xBF) {
                return 'REJECT'
            }
        }
        $EngineText = $StrictUtf8.GetString([byte[]]$Envelope.engine_bytes)
        if ($EngineText.IndexOf([char]0) -ge 0 -or $EngineText.IndexOf([char]0xFFFD) -ge 0 -or
            [regex]::IsMatch($EngineText,"`r(?!`n)") -or
            [regex]::Matches($EngineText,$RpytestLinePattern).Count -ne 0 -or
            [regex]::Matches($EngineText,'(?m)^Traceback \(most recent call last\):[ \t]*\r?$').Count -ne 0 -or
            [regex]::Matches($EngineText,"(?m)^I'm sorry, but an uncaught exception occurred\.[ \t]*\r?$").Count -ne 0 -or
            [regex]::Matches($EngineText,'(?m)^TC_GENERATOR_EVIDENCE_WRITE_FAILURE[ \t]*\r?$').Count -ne 0 -or
            [regex]::Matches($EngineText,'(?m)^TC_OBSERVER_EVIDENCE_WRITE_FAILURE[ \t]*\r?$').Count -ne 0) {
            return 'REJECT'
        }
        if ($Mode -ceq 'observer') {
            if ($Envelope.stdout_bytes.Length -ne 0) { return 'REJECT' }
        } else {
            if ($Envelope.stdout_bytes.Length -eq 0 -or
                ($Envelope.stdout_bytes.Length -ge 3 -and $Envelope.stdout_bytes[0] -eq 0xEF -and
                    $Envelope.stdout_bytes[1] -eq 0xBB -and $Envelope.stdout_bytes[2] -eq 0xBF)) { return 'REJECT' }
            $StdoutText = $StrictUtf8.GetString([byte[]]$Envelope.stdout_bytes)
            if ($StdoutText.IndexOf([char]0) -ge 0 -or $StdoutText.IndexOf([char]0xFFFD) -ge 0 -or
                [regex]::IsMatch($StdoutText,"`r(?!`n)") -or
                $Envelope.stdout_bytes[$Envelope.stdout_bytes.Length - 1] -ne 0x0A -or
                [regex]::Matches($StdoutText,$AnyStatusPattern).Count -ne 1 -or
                [regex]::Matches($StdoutText,$PassStatusPattern).Count -ne 1 -or
                [regex]::Matches($StdoutText,$SuitePattern).Count -ne 1 -or
                [regex]::Matches($StdoutText,$SummaryPattern).Count -ne 1 -or
                [regex]::Matches($StdoutText,'(?m)^Traceback \(most recent call last\):[ \t]*\r?$').Count -ne 0 -or
                [regex]::Matches($StdoutText,'(?m)^TC_GENERATOR_EVIDENCE_WRITE_FAILURE[ \t]*\r?$').Count -ne 0) {
                return 'REJECT'
            }
        }
        return 'ACCEPT'
    } catch { return 'REJECT' }
}
function Test-V3SaveInventoryContract(
    [object]$Inventory,[int]$ExpectedTargetCount,[string[]]$ExpectedTargetPaths,
    [int64]$ExpectedTargetBytes,[string]$ExpectedTargetHash,[bool]$ObserverMode
) {
    try {
        if (-not (Test-V3ExactProperties $Inventory @('roots','directories','files','target_count')) -or
            -not (Test-V3ExactProperties $Inventory.roots @('external_savedir','local_savedir')) -or
            -not (Test-V3CanonicalExpectedPath $Inventory.roots.external_savedir ([string]$Inventory.roots.external_savedir)) -or
            -not (Test-V3CanonicalExpectedPath $Inventory.roots.local_savedir ([string]$Inventory.roots.local_savedir)) -or
            $Inventory.target_count -isnot [int] -or $Inventory.target_count -ne $ExpectedTargetCount) { return $false }
        $Previous = $null
        foreach ($Directory in @($Inventory.directories)) {
            if (-not (Test-V3ExactProperties $Directory @('root_role','relative_path'))) { return $false }
            $Key = [string]$Directory.root_role + [char]9 + [string]$Directory.relative_path
            if ($Directory.root_role -isnot [string] -or [string]$Directory.root_role -notin @('external','local') -or
                $Directory.relative_path -isnot [string] -or [IO.Path]::IsPathRooted([string]$Directory.relative_path) -or
                [string]$Directory.relative_path -match '(^|[\\/])\.\.([\\/]|$)' -or
                ($null -ne $Previous -and [StringComparer]::Ordinal.Compare($Previous,$Key) -ge 0)) { return $false }
            $Previous = $Key
        }
        $Seen = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
        $Previous = $null
        $ActualTargetPaths = New-Object 'System.Collections.Generic.List[string]'
        foreach ($File in @($Inventory.files)) {
            if (-not (Test-V3ExactProperties $File @('root_role','relative_path','kind','bytes','sha256'))) { return $false }
            $Key = [string]$File.root_role + [char]9 + [string]$File.relative_path
            if ($File.root_role -isnot [string] -or [string]$File.root_role -notin @('external','local') -or
                $File.relative_path -isnot [string] -or [IO.Path]::IsPathRooted([string]$File.relative_path) -or
                [string]$File.relative_path -match '(^|[\\/])\.\.([\\/]|$)' -or
                $File.kind -isnot [string] -or [string]$File.kind -notin @('target','autosave','persistent') -or
                ($ObserverMode -and [string]$File.kind -eq 'autosave') -or
                -not (Test-RecoveryIntegral $File.bytes) -or [int64]$File.bytes -lt 0 -or
                $File.sha256 -isnot [string] -or $File.sha256 -cnotmatch '^[0-9A-F]{64}$' -or
                -not $Seen.Add($Key) -or
                ($null -ne $Previous -and [StringComparer]::Ordinal.Compare($Previous,$Key) -ge 0)) { return $false }
            $Previous = $Key
            if ([string]$File.kind -ceq 'target') {
                $Root = if ([string]$File.root_role -ceq 'external') {
                    [string]$Inventory.roots.external_savedir
                } else { [string]$Inventory.roots.local_savedir }
                $TargetPath = Get-CanonicalPath (Join-Path $Root ([string]$File.relative_path))
                if (-not (Test-SameOrChildPath $TargetPath $Root) -or
                    [int64]$File.bytes -ne $ExpectedTargetBytes -or
                    [string]$File.sha256 -cne $ExpectedTargetHash) { return $false }
                [void]$ActualTargetPaths.Add($TargetPath)
            }
        }
        $ExpectedCanonical = [string[]]@($ExpectedTargetPaths | ForEach-Object { Get-CanonicalPath $_ })
        $ActualCanonical = [string[]]$ActualTargetPaths.ToArray()
        [Array]::Sort($ExpectedCanonical,[StringComparer]::Ordinal)
        [Array]::Sort($ActualCanonical,[StringComparer]::Ordinal)
        return ($ActualCanonical.Count -eq $ExpectedTargetCount -and
            ($ActualCanonical -join '|') -ceq ($ExpectedCanonical -join '|'))
    } catch { return $false }
}
function Test-V3GeneratorCompletionContract([object]$Completion,[object]$Expected) {
    try {
        if (-not (Test-V3ExactProperties $Completion $GeneratorCompletionProperties) -or
            -not (Test-V3ExactProperties $Expected @(
                'attempt_id','attempt_seal','approval_lock_sha256','approved_plan_commit',
                'predecessor_manifest_sha256','red_record_sha256','green_record_sha256','worktree_path',
                'savedir_path','process_evidence_dir','fixture_seal','fixture_evidence_seal','request_seal',
                'result_seal','state_seal','stdout_seal','stderr_seal','engine_log_evidence_seal',
                'target_seals','save_name','save_inventory'
            )) -or $Completion.schema_version -isnot [int] -or $Completion.schema_version -ne 2 -or
            $Completion.attempt_id -isnot [string] -or $Completion.attempt_id -cnotmatch '^[0-9a-f]{32}$' -or
            $Completion.attempt_id -cne [string]$Expected.attempt_id -or
            -not (Test-V3CanonicalExpectedPath $Completion.attempt_path ([string]$Expected.attempt_seal.path)) -or
            -not (Test-V3Hash $Completion.attempt_sha256 ([string]$Expected.attempt_seal.sha256)) -or
            -not (Test-V3Hash $Completion.approval_lock_sha256 ([string]$Expected.approval_lock_sha256)) -or
            $Completion.approved_plan_commit -isnot [string] -or $Completion.approved_plan_commit -cne [string]$Expected.approved_plan_commit -or
            -not (Test-V3Hash $Completion.predecessor_manifest_sha256 ([string]$Expected.predecessor_manifest_sha256)) -or
            -not (Test-V3Hash $Completion.red_record_sha256 ([string]$Expected.red_record_sha256)) -or
            -not (Test-V3Hash $Completion.green_record_sha256 ([string]$Expected.green_record_sha256)) -or
            -not (Test-V3CanonicalExpectedPath $Completion.worktree_path ([string]$Expected.worktree_path)) -or
            -not (Test-V3CanonicalExpectedPath $Completion.savedir_path ([string]$Expected.savedir_path)) -or
            -not (Test-V3CanonicalExpectedPath $Completion.process_evidence_dir ([string]$Expected.process_evidence_dir)) -or
            -not (Test-V3CanonicalExpectedPath $Completion.fixture_path ([string]$Expected.fixture_seal.path)) -or
            -not (Test-V3Hash $Completion.fixture_sha256 ([string]$Expected.fixture_seal.sha256)) -or
            -not (Test-V3CanonicalExpectedPath $Completion.fixture_evidence_path ([string]$Expected.fixture_evidence_seal.path)) -or
            -not (Test-V3Hash $Completion.fixture_evidence_sha256 ([string]$Expected.fixture_evidence_seal.sha256)) -or
            -not (Test-V3CanonicalExpectedPath $Completion.request_path ([string]$Expected.request_seal.path)) -or
            -not (Test-RecoveryIntegral $Completion.request_bytes) -or [int64]$Completion.request_bytes -ne [int64]$Expected.request_seal.bytes -or
            -not (Test-V3Hash $Completion.request_sha256 ([string]$Expected.request_seal.sha256)) -or
            -not (Test-V3CanonicalExpectedPath $Completion.result_path ([string]$Expected.result_seal.path)) -or
            -not (Test-RecoveryIntegral $Completion.result_bytes) -or [int64]$Completion.result_bytes -ne [int64]$Expected.result_seal.bytes -or
            -not (Test-V3Hash $Completion.result_sha256 ([string]$Expected.result_seal.sha256)) -or
            -not (Test-V3CanonicalExpectedPath $Completion.state_path ([string]$Expected.state_seal.path)) -or
            -not (Test-RecoveryIntegral $Completion.state_bytes) -or [int64]$Completion.state_bytes -ne [int64]$Expected.state_seal.bytes -or
            -not (Test-V3Hash $Completion.state_sha256 ([string]$Expected.state_seal.sha256)) -or
            -not (Test-V3CanonicalExpectedPath $Completion.rpytest_stdout_path ([string]$Expected.stdout_seal.path)) -or
            -not (Test-RecoveryIntegral $Completion.rpytest_stdout_bytes) -or [int64]$Completion.rpytest_stdout_bytes -ne [int64]$Expected.stdout_seal.bytes -or
            -not (Test-V3Hash $Completion.rpytest_stdout_sha256 ([string]$Expected.stdout_seal.sha256)) -or
            -not (Test-V3CanonicalExpectedPath $Completion.stderr_path ([string]$Expected.stderr_seal.path)) -or
            -not (Test-RecoveryIntegral $Completion.stderr_bytes) -or [int64]$Completion.stderr_bytes -ne [int64]$Expected.stderr_seal.bytes -or
            -not (Test-V3Hash $Completion.stderr_sha256 ([string]$Expected.stderr_seal.sha256)) -or
            -not (Test-V3CanonicalExpectedPath $Completion.engine_log_evidence_path ([string]$Expected.engine_log_evidence_seal.path)) -or
            -not (Test-V3Hash $Completion.engine_log_evidence_sha256 ([string]$Expected.engine_log_evidence_seal.sha256)) -or
            @($Expected.target_seals).Count -ne 3 -or $Completion.target_copy_count -isnot [int] -or
            $Completion.target_copy_count -ne 3 -or $Completion.save_name -isnot [string] -or
            $Completion.save_name -cne [string]$Expected.save_name -or
            -not (Test-RecoveryIntegral $Completion.save_bytes) -or
            [int64]$Completion.save_bytes -ne [int64]@($Expected.target_seals)[0].bytes -or
            -not (Test-V3Hash $Completion.save_sha256 ([string]@($Expected.target_seals)[0].sha256)) -or
            -not (Test-RoundtripUtc $Completion.finished_utc)) { return 'REJECT' }
        $SaveFields = @('external_save_path','sync_save_path','local_save_path')
        for ($Index = 0; $Index -lt 3; $Index++) {
            $Seal = @($Expected.target_seals)[$Index]
            if (-not (Test-V3SealContract $Seal ([string]$Seal.path) ([int64]$Completion.save_bytes) ([string]$Completion.save_sha256)) -or
                -not (Test-V3CanonicalExpectedPath $Completion.($SaveFields[$Index]) ([string]$Seal.path))) { return 'REJECT' }
        }
        if (-not (Test-V3SaveInventoryContract $Completion.save_inventory 3 `
                ([string[]]@($Expected.target_seals | ForEach-Object { [string]$_.path })) `
                ([int64]$Completion.save_bytes) ([string]$Completion.save_sha256) $false) -or
            (($Completion.save_inventory | ConvertTo-Json -Depth 16 -Compress) -cne
                ($Expected.save_inventory | ConvertTo-Json -Depth 16 -Compress))) { return 'REJECT' }
        return 'ACCEPT'
    } catch { return 'REJECT' }
}
function Test-V3ObserverCompletionContract([object]$Completion,[object]$Expected) {
    try {
        if (-not (Test-V3ExactProperties $Completion $ObserverCompletionProperties) -or
            -not (Test-V3ExactProperties $Expected @(
                'attempt_id','attempt_seal','approval_lock_sha256','approved_plan_commit',
                'generator_completion_sha256','worktree_path','savedir_path','process_evidence_dir',
                'fixture_seal','fixture_evidence_seal','request_seal','result_seal','state_seal',
                'stdout_seal','stderr_seal','engine_log_evidence_seal','source_before_seal',
                'source_after_seal','replay_before_seal','replay_after_seal','save_inventory'
            )) -or $Completion.schema_version -isnot [int] -or $Completion.schema_version -ne 2 -or
            $Completion.attempt_id -isnot [string] -or $Completion.attempt_id -cnotmatch '^[0-9a-f]{32}$' -or
            $Completion.attempt_id -cne [string]$Expected.attempt_id -or
            -not (Test-V3CanonicalExpectedPath $Completion.attempt_path ([string]$Expected.attempt_seal.path)) -or
            -not (Test-V3Hash $Completion.attempt_sha256 ([string]$Expected.attempt_seal.sha256)) -or
            -not (Test-V3Hash $Completion.approval_lock_sha256 ([string]$Expected.approval_lock_sha256)) -or
            $Completion.approved_plan_commit -isnot [string] -or $Completion.approved_plan_commit -cne [string]$Expected.approved_plan_commit -or
            -not (Test-V3Hash $Completion.generator_completion_sha256 ([string]$Expected.generator_completion_sha256)) -or
            -not (Test-V3CanonicalExpectedPath $Completion.worktree_path ([string]$Expected.worktree_path)) -or
            -not (Test-V3CanonicalExpectedPath $Completion.savedir_path ([string]$Expected.savedir_path)) -or
            -not (Test-V3CanonicalExpectedPath $Completion.process_evidence_dir ([string]$Expected.process_evidence_dir)) -or
            -not (Test-V3CanonicalExpectedPath $Completion.fixture_path ([string]$Expected.fixture_seal.path)) -or
            -not (Test-V3Hash $Completion.fixture_sha256 ([string]$Expected.fixture_seal.sha256)) -or
            -not (Test-V3CanonicalExpectedPath $Completion.fixture_evidence_path ([string]$Expected.fixture_evidence_seal.path)) -or
            -not (Test-V3Hash $Completion.fixture_evidence_sha256 ([string]$Expected.fixture_evidence_seal.sha256)) -or
            -not (Test-V3CanonicalExpectedPath $Completion.request_path ([string]$Expected.request_seal.path)) -or
            -not (Test-RecoveryIntegral $Completion.request_bytes) -or [int64]$Completion.request_bytes -ne [int64]$Expected.request_seal.bytes -or
            -not (Test-V3Hash $Completion.request_sha256 ([string]$Expected.request_seal.sha256)) -or
            -not (Test-V3CanonicalExpectedPath $Completion.result_path ([string]$Expected.result_seal.path)) -or
            -not (Test-RecoveryIntegral $Completion.result_bytes) -or [int64]$Completion.result_bytes -ne [int64]$Expected.result_seal.bytes -or
            -not (Test-V3Hash $Completion.result_sha256 ([string]$Expected.result_seal.sha256)) -or
            -not (Test-V3CanonicalExpectedPath $Completion.state_path ([string]$Expected.state_seal.path)) -or
            -not (Test-RecoveryIntegral $Completion.state_bytes) -or [int64]$Completion.state_bytes -ne [int64]$Expected.state_seal.bytes -or
            -not (Test-V3Hash $Completion.state_sha256 ([string]$Expected.state_seal.sha256)) -or
            -not (Test-V3CanonicalExpectedPath $Completion.stdout_path ([string]$Expected.stdout_seal.path)) -or
            -not (Test-RecoveryIntegral $Completion.stdout_bytes) -or [int64]$Completion.stdout_bytes -ne [int64]$Expected.stdout_seal.bytes -or
            -not (Test-V3Hash $Completion.stdout_sha256 ([string]$Expected.stdout_seal.sha256)) -or
            -not (Test-V3CanonicalExpectedPath $Completion.stderr_path ([string]$Expected.stderr_seal.path)) -or
            -not (Test-RecoveryIntegral $Completion.stderr_bytes) -or [int64]$Completion.stderr_bytes -ne [int64]$Expected.stderr_seal.bytes -or
            -not (Test-V3Hash $Completion.stderr_sha256 ([string]$Expected.stderr_seal.sha256)) -or
            -not (Test-V3CanonicalExpectedPath $Completion.engine_log_evidence_path ([string]$Expected.engine_log_evidence_seal.path)) -or
            -not (Test-V3Hash $Completion.engine_log_evidence_sha256 ([string]$Expected.engine_log_evidence_seal.sha256)) -or
            -not (Test-RoundtripUtc $Completion.finished_utc)) { return 'REJECT' }
        foreach ($Pair in @(
            @('source_save_path','source_save_bytes','source_save_sha256_before','source_before_seal'),
            @('source_save_path','source_save_bytes','source_save_sha256_after','source_after_seal'),
            @('replay_save_path','replay_save_bytes','replay_save_sha256_before','replay_before_seal'),
            @('replay_save_path','replay_save_bytes','replay_save_sha256_after','replay_after_seal')
        )) {
            $Seal = $Expected.($Pair[3])
            if (-not (Test-V3CanonicalExpectedPath $Completion.($Pair[0]) ([string]$Seal.path)) -or
                -not (Test-RecoveryIntegral $Completion.($Pair[1])) -or
                [int64]$Completion.($Pair[1]) -ne [int64]$Seal.bytes -or
                -not (Test-V3Hash $Completion.($Pair[2]) ([string]$Seal.sha256))) { return 'REJECT' }
        }
        if ((@(
                [string]$Completion.source_save_sha256_before,[string]$Completion.source_save_sha256_after,
                [string]$Completion.replay_save_sha256_before,[string]$Completion.replay_save_sha256_after
            ) | Select-Object -Unique).Count -ne 1 -or
            -not (Test-V3SaveInventoryContract $Completion.save_inventory 1 `
                ([string[]]@([string]$Completion.replay_save_path)) ([int64]$Completion.replay_save_bytes) `
                ([string]$Completion.replay_save_sha256_after) $true) -or
            (($Completion.save_inventory | ConvertTo-Json -Depth 16 -Compress) -cne
                ($Expected.save_inventory | ConvertTo-Json -Depth 16 -Compress))) { return 'REJECT' }
        return 'ACCEPT'
    } catch { return 'REJECT' }
}
function Test-V3GeneratorRuntimeEvidenceContract([object]$Channel,[object]$Completion,[object]$Expected) {
    if ((Test-V3ChannelContract 'generator' $Channel) -cne 'ACCEPT' -or
        (Test-V3GeneratorCompletionContract $Completion $Expected) -cne 'ACCEPT' -or
        -not (Test-V3CanonicalExpectedPath $Channel.engine_evidence_seal.path `
            ([string]$Completion.engine_log_evidence_path)) -or
        -not (Test-V3CanonicalExpectedPath $Channel.engine_evidence_seal.path `
            ([string]$Expected.engine_log_evidence_seal.path)) -or
        [string]$Completion.engine_log_evidence_sha256 -cne [string]$Channel.engine_evidence_seal.sha256 -or
        [int64]$Completion.rpytest_stdout_bytes -ne [int64]$Channel.stdout_bytes.Length -or
        [string]$Completion.rpytest_stdout_sha256 -cne (Get-V3BytesSha256 ([byte[]]$Channel.stdout_bytes)) -or
        [int64]$Completion.stderr_bytes -ne [int64]$Channel.stderr_bytes.Length -or
        [string]$Completion.stderr_sha256 -cne (Get-V3BytesSha256 ([byte[]]$Channel.stderr_bytes))) {
        return 'REJECT'
    }
    return 'ACCEPT'
}
function Test-V3ObserverRuntimeEvidenceContract([object]$Channel,[object]$Completion,[object]$Expected) {
    if ((Test-V3ChannelContract 'observer' $Channel) -cne 'ACCEPT' -or
        (Test-V3ObserverCompletionContract $Completion $Expected) -cne 'ACCEPT' -or
        -not (Test-V3CanonicalExpectedPath $Channel.engine_evidence_seal.path `
            ([string]$Completion.engine_log_evidence_path)) -or
        -not (Test-V3CanonicalExpectedPath $Channel.engine_evidence_seal.path `
            ([string]$Expected.engine_log_evidence_seal.path)) -or
        [string]$Completion.engine_log_evidence_sha256 -cne [string]$Channel.engine_evidence_seal.sha256 -or
        [int64]$Completion.stdout_bytes -ne [int64]$Channel.stdout_bytes.Length -or
        [string]$Completion.stdout_sha256 -cne (Get-V3BytesSha256 ([byte[]]$Channel.stdout_bytes)) -or
        [int64]$Completion.stderr_bytes -ne [int64]$Channel.stderr_bytes.Length -or
        [string]$Completion.stderr_sha256 -cne (Get-V3BytesSha256 ([byte[]]$Channel.stderr_bytes))) {
        return 'REJECT'
    }
    return 'ACCEPT'
}
# TASK1_V3_PRODUCTION_VALIDATORS_END
```

- [ ] **Step 2: Create the detached generator worktree and freeze RED as the host-patch checkpoint**

Continue in the same session:

```powershell
git worktree add --detach $GeneratorRoot $P3
if ($LASTEXITCODE -ne 0) { throw 'Could not create the one recovery generator worktree.' }
if ((& git -C $GeneratorRoot rev-parse HEAD).Trim() -cne $P3 -or
    (& git -C $GeneratorRoot rev-parse 'HEAD:game').Trim() -cne $GameTree -or
    @(git -C $GeneratorRoot status --short --untracked-files=all).Count -ne 0) {
    throw 'Generator worktree is not the exact clean P3 baseline.'
}
$GeneratorFixturePath = Join-Path $GeneratorRoot 'game\zz_terminal_collapse_legacy_fixture.rpy'
$GeneratorLocalSaves = Join-Path $GeneratorRoot 'game\saves'
if (Test-Path -LiteralPath $GeneratorLocalSaves) { throw 'Generator game/saves must start absent.' }
[IO.File]::Copy($OldFixturePath, $GeneratorFixturePath, $false)
if ((Get-Item -LiteralPath $GeneratorFixturePath).Length -ne 8749 -or
    (Get-FileHash -LiteralPath $GeneratorFixturePath -Algorithm SHA256).Hash -cne '497064A9DFCA721D1A6ED3A941A9DB0DC8DB92C489AD22F4E1ECF58A74E4CCC3') {
    throw 'The copied generator fixture is not the frozen RED source.'
}
$GeneratorFixtureRelative = 'game/zz_terminal_collapse_legacy_fixture.rpy'
$GeneratorStatus = @(git -C $GeneratorRoot status --short --untracked-files=all)
if ($GeneratorStatus.Count -ne 1 -or $GeneratorStatus[0] -cne ('?? ' + $GeneratorFixtureRelative) -or
    @(git -C $GeneratorRoot diff --name-only).Count -ne 0 -or
    (Test-Path -LiteralPath $GeneratorLocalSaves)) {
    throw ('Generator worktree scope is not exactly its temporary fixture: ' + ($GeneratorStatus -join '; '))
}
$RedInputs = @(
    [ordered]@{ role='legacy_fixture'; path=(Get-CanonicalPath $OldFixturePath); bytes=[int64]8749; sha256='497064A9DFCA721D1A6ED3A941A9DB0DC8DB92C489AD22F4E1ECF58A74E4CCC3' },
    [ordered]@{ role='generator_worktree_fixture_before_patch'; path=(Get-CanonicalPath $GeneratorFixturePath); bytes=[int64]8749; sha256='497064A9DFCA721D1A6ED3A941A9DB0DC8DB92C489AD22F4E1ECF58A74E4CCC3' },
    [ordered]@{ role='v2_test_report'; path=(Get-CanonicalPath $V2StdoutPath); bytes=[int64]1074; sha256='BD3B00124C6134FD0DAE737B293C20F68BF76F02ECDC69E77797C883FA5208CE' },
    [ordered]@{ role='v2_engine_boot_log'; path=(Get-CanonicalPath $V2EngineLogPath); bytes=[int64]1860; sha256='FE52BE91013D21B51AAF2CCDCF796289906EB4D12FA08EB1912A196B4F076A81' }
)
$ContractProperties = @('schema_version','verdict','fixture_gate','stream_gate','inputs','mutations','created_utc')
$RedPayload = [ordered]@{
    schema_version = 3
    verdict = 'EXPECTED_RED'
    fixture_gate = $RedFixtureGate
    stream_gate = $RedStreamGate
    inputs = $RedInputs
    mutations = [object[]]@()
    created_utc = [DateTime]::UtcNow.ToString('o',[Globalization.CultureInfo]::InvariantCulture)
}
$RedRecord = New-ReadOnlyJsonRecord $RedRecordPath $RedPayload $ContractProperties 'generator contract RED'
Assert-ExactProperties $RedRecord.fixture_gate @(
    'expected','observed','quit_call_count','returned_finish_codes','returns_97','returns_code','native_tail'
) 'RED fixture_gate'
Assert-ExactProperties $RedRecord.stream_gate @(
    'selector','test_report_status_count','engine_log_status_count','expected_failure'
) 'RED stream_gate'
if ($RedRecord.schema_version -isnot [int] -or $RedRecord.schema_version -ne 3 -or
    $RedRecord.verdict -isnot [string] -or $RedRecord.verdict -cne 'EXPECTED_RED' -or
    @($RedRecord.inputs).Count -ne 4 -or @($RedRecord.mutations).Count -ne 0 -or
    -not (Test-RoundtripUtc $RedRecord.created_utc)) {
    throw 'NEEDS_CONTEXT: persisted RED checkpoint schema/types failed.'
}
foreach ($Input in @($RedRecord.inputs)) {
    Assert-ExactProperties $Input @('role','path','bytes','sha256') 'RED input'
    $InputSeal = New-FileSeal ([string]$Input.path)
    if ($InputSeal.bytes -ne [int64]$Input.bytes -or $InputSeal.sha256 -cne [string]$Input.sha256) {
        throw ('NEEDS_CONTEXT: RED checkpoint input drifted ' + [string]$Input.path)
    }
}
$RedRecordSha256 = (Get-FileHash -LiteralPath $RedRecordPath -Algorithm SHA256).Hash
Assert-RecoveryAuthorityUnchanged 'before host apply_patch checkpoint'
Write-Output ('HOST_APPLY_PATCH_CHECKPOINT=' + $RedRecordSha256)
```

Expected: the old file remains unchanged; the new P3 worktree contains exactly one untracked byte-identical copy. The read-only RED record binds that copy plus the v2 stdout/engine-log mismatch and prints one uppercase checkpoint SHA. The controller retains that exact value as `$GeneratorRedCheckpointSha256`, then ends this PowerShell scope; no generator authority has been consumed.

- [ ] **Step 3: Apply the one approved fixture patch through the host tool**

The host must call its native `apply_patch` tool once, with the exact absolute v3 worktree target. Do not invoke `apply_patch.bat`, PowerShell file writes, Python writes, or any other fallback:

```diff
*** Begin Patch
*** Update File: E:/Projects/renpy-8.5.2-sdk/terminal-collapse-temp/cos-terminal-collapse-generator-recovery-v3/game/zz_terminal_collapse_legacy_fixture.rpy
@@
-                r.quit(status=97)
-            r.quit(status=code)
+                return 97
+            return code
@@
-                finish("FAIL", "pre-save generator assertions failed", {"checks": checks, "failures": failures, "actual": actual}, 41)
+                return finish("FAIL", "pre-save generator assertions failed", {"checks": checks, "failures": failures, "actual": actual}, 41)
@@
-                finish("FAIL", "post-save generator assertions failed", payload, 42)
-            finish("PASS", "native testcase saved the unchanged production final tactics Menu", payload, 0)
+                return finish("FAIL", "post-save generator assertions failed", payload, 42)
+            return finish("PASS", "native testcase saved the unchanged production final tactics Menu", payload, 0)
@@
-            finish("FAIL", "generator internal exception", {"traceback": tb.format_exc()}, 43)
+            return finish("FAIL", "generator internal exception", {"traceback": tb.format_exc()}, 43)
@@
-        $ _tc_generate_legacy_save()
+        $ _tc_generator_status = _tc_generate_legacy_save()
+        assert eval (_tc_generator_status == 0)
+        exit
*** End Patch
```

Expected: the host reports exactly one successful patch to the absolute v3 fixture. It does not touch the repository, v1/v2 paths, evidence, SaveDirs, or any other E: path. Do not start Ren'Py.

- [ ] **Step 4: Re-enter through a fresh lock-first scope and freeze GREEN with exactly 42 offline cases**

The controller opens a second fresh Windows PowerShell 5.1 scope and binds the same out-of-band `$ApprovalLockSha256` plus the exact uppercase `$GeneratorRedCheckpointSha256` printed by PRE_PATCH. The first fence authenticates the lock and the physical P3 plan before extracting the two uniquely marked, already-reviewed bootstrap blocks from that authenticated plan. It dot-sources them into the new scope with `POST_PATCH`; no session variable is imported from the ended scope:

```powershell
# TASK1_V3_POST_PATCH_REENTRY_BEGIN
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
if ($PSVersionTable.PSEdition -cne 'Desktop' -or $PSVersionTable.PSVersion.Major -ne 5) {
    throw 'NEEDS_CONTEXT: post-patch Task 1 requires Windows PowerShell 5.1 Desktop.'
}
$ApprovalVariable = Get-Variable -Name ApprovalLockSha256 -Scope 0 -ErrorAction SilentlyContinue
if ($null -eq $ApprovalVariable -or $ApprovalVariable.Value -isnot [string] -or
    [string]$ApprovalVariable.Value -cnotmatch '^[0-9A-F]{64}$') {
    throw 'NEEDS_CONTEXT: controller did not bind the post-patch out-of-band lock SHA.'
}
$ApprovalLockSha256 = [string]$ApprovalVariable.Value
$CheckpointVariable = Get-Variable -Name GeneratorRedCheckpointSha256 -Scope 0 -ErrorAction SilentlyContinue
if ($null -eq $CheckpointVariable -or $CheckpointVariable.Value -isnot [string] -or
    [string]$CheckpointVariable.Value -cnotmatch '^[0-9A-F]{64}$') {
    throw 'NEEDS_CONTEXT: controller did not bind the PRE_PATCH RED checkpoint SHA.'
}
$GeneratorRedCheckpointSha256 = [string]$CheckpointVariable.Value
$BootstrapLockPath = 'C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\work\CourtOfShadows-governance-winter\.superpowers\sdd\terminal-collapse-ending\approved-plan-lock-v3.json'
if (-not (Test-Path -LiteralPath $BootstrapLockPath -PathType Leaf)) {
    throw 'NEEDS_CONTEXT: post-patch known approval lock leaf is missing.'
}
if ((Get-FileHash -LiteralPath $BootstrapLockPath -Algorithm SHA256).Hash -cne $ApprovalLockSha256) {
    throw 'NEEDS_CONTEXT: post-patch out-of-band lock hash authentication failed.'
}
$StrictUtf8 = New-Object Text.UTF8Encoding($false,$true)
$BootstrapLockBytes = [IO.File]::ReadAllBytes($BootstrapLockPath)
if (($BootstrapLockBytes.Length -ge 3 -and $BootstrapLockBytes[0] -eq 0xEF -and
        $BootstrapLockBytes[1] -eq 0xBB -and $BootstrapLockBytes[2] -eq 0xBF) -or
    -not (Get-Item -LiteralPath $BootstrapLockPath).IsReadOnly) {
    throw 'NEEDS_CONTEXT: authenticated post-patch lock has invalid bytes or mutability.'
}
$BootstrapLockText = $StrictUtf8.GetString($BootstrapLockBytes)
$BootstrapApproval = $BootstrapLockText | ConvertFrom-Json -ErrorAction Stop
$ProjectRoot = (Resolve-Path -LiteralPath '.').Path
$ExpectedProjectRoot = Split-Path (Split-Path (Split-Path (Split-Path $BootstrapLockPath -Parent) -Parent) -Parent) -Parent
if ([IO.Path]::GetFullPath($ProjectRoot).TrimEnd('\') -cne [IO.Path]::GetFullPath($ExpectedProjectRoot).TrimEnd('\')) {
    throw 'NEEDS_CONTEXT: post-patch current directory is not the lock-owned repository.'
}
git check-ignore -q -- $BootstrapLockPath
if ($LASTEXITCODE -ne 0) { throw 'NEEDS_CONTEXT: authenticated post-patch lock is not ignored.' }
$BootstrapPlanPath = Join-Path $ProjectRoot 'docs\superpowers\plans\2026-08-14-terminal-collapse-generator-recovery-v3.md'
if ($BootstrapApproval.plan_sha256 -isnot [string] -or
    (Get-FileHash -LiteralPath $BootstrapPlanPath -Algorithm SHA256).Hash -cne [string]$BootstrapApproval.plan_sha256) {
    throw 'NEEDS_CONTEXT: cannot authenticate the plan that carries the post-patch bootstrap.'
}
$BootstrapPlanBytes = [IO.File]::ReadAllBytes($BootstrapPlanPath)
if ($BootstrapPlanBytes.Length -ge 3 -and $BootstrapPlanBytes[0] -eq 0xEF -and
    $BootstrapPlanBytes[1] -eq 0xBB -and $BootstrapPlanBytes[2] -eq 0xBF) {
    throw 'NEEDS_CONTEXT: authenticated plan unexpectedly has a BOM.'
}
$BootstrapPlanText = $StrictUtf8.GetString($BootstrapPlanBytes)
function Get-AuthenticatedPlanBlock([string]$BeginMarker,[string]$EndMarker) {
    $BeginToken = '# ' + $BeginMarker
    $EndToken = '# ' + $EndMarker
    $Begin = $BootstrapPlanText.IndexOf($BeginToken,[StringComparison]::Ordinal)
    $End = $BootstrapPlanText.IndexOf($EndToken,[StringComparison]::Ordinal)
    if ($Begin -lt 0 -or $End -le $Begin -or
        $BootstrapPlanText.IndexOf($BeginToken,$Begin + $BeginToken.Length,[StringComparison]::Ordinal) -ge 0 -or
        $BootstrapPlanText.IndexOf($EndToken,$End + $EndToken.Length,[StringComparison]::Ordinal) -ge 0) {
        throw ('NEEDS_CONTEXT: authenticated plan block markers are not unique: ' + $BeginMarker)
    }
    $SourceStart = $Begin + $BeginToken.Length
    return $BootstrapPlanText.Substring($SourceStart,$End - $SourceStart)
}
$Task1BootstrapPhase = 'POST_PATCH'
$BootstrapSource = Get-AuthenticatedPlanBlock 'TASK1_V3_BOOTSTRAP_BEGIN' 'TASK1_V3_BOOTSTRAP_END'
. ([ScriptBlock]::Create($BootstrapSource))
$OfflineGateSource = Get-AuthenticatedPlanBlock 'TASK1_V3_OFFLINE_GATE_BEGIN' 'TASK1_V3_OFFLINE_GATE_END'
. ([ScriptBlock]::Create($OfflineGateSource))
$ProductionValidatorSource = Get-AuthenticatedPlanBlock 'TASK1_V3_PRODUCTION_VALIDATORS_BEGIN' 'TASK1_V3_PRODUCTION_VALIDATORS_END'
. ([ScriptBlock]::Create($ProductionValidatorSource))
Assert-RecoveryAuthorityUnchanged 'post-patch fresh scope'
# TASK1_V3_POST_PATCH_REENTRY_END

$ContractProperties = @('schema_version','verdict','fixture_gate','stream_gate','inputs','mutations','created_utc')
$RedRecord = Read-RecoveryStrictJson $RedRecordPath 'post-patch RED checkpoint'
Assert-ExactProperties $RedRecord @(
    'schema_version','verdict','fixture_gate','stream_gate','inputs','mutations','created_utc'
) 'post-patch RED checkpoint'
$RedRecordSha256 = (Get-FileHash -LiteralPath $RedRecordPath -Algorithm SHA256).Hash
if (-not (Get-Item -LiteralPath $RedRecordPath).IsReadOnly -or
    $RedRecordSha256 -cne $GeneratorRedCheckpointSha256 -or
    $RedRecord.schema_version -isnot [int] -or $RedRecord.schema_version -ne 3 -or
    $RedRecord.verdict -cne 'EXPECTED_RED' -or @($RedRecord.mutations).Count -ne 0) {
    throw 'NEEDS_CONTEXT: immutable RED checkpoint did not survive the host seam.'
}
foreach ($Input in @($RedRecord.inputs)) {
    Assert-ExactProperties $Input @('role','path','bytes','sha256') 'post-patch RED input'
    if ([string]$Input.role -ceq 'generator_worktree_fixture_before_patch') { continue }
    $InputSeal = New-FileSeal ([string]$Input.path)
    if ($InputSeal.bytes -ne [int64]$Input.bytes -or $InputSeal.sha256 -cne [string]$Input.sha256) {
        throw ('NEEDS_CONTEXT: immutable RED input drifted across host seam ' + [string]$Input.path)
    }
}
$GeneratorFixturePath = Join-Path $GeneratorRoot 'game\zz_terminal_collapse_legacy_fixture.rpy'
$GeneratorLocalSaves = Join-Path $GeneratorRoot 'game\saves'
$GeneratorFixtureRelative = 'game/zz_terminal_collapse_legacy_fixture.rpy'
$GeneratorStatus = @(git -C $GeneratorRoot status --short --untracked-files=all)
if ((& git -C $GeneratorRoot rev-parse HEAD).Trim() -cne $P3 -or
    (& git -C $GeneratorRoot rev-parse 'HEAD:game').Trim() -cne $GameTree -or
    $GeneratorStatus.Count -ne 1 -or $GeneratorStatus[0] -cne ('?? ' + $GeneratorFixtureRelative) -or
    @(git -C $GeneratorRoot diff --name-only).Count -ne 0 -or
    (Test-Path -LiteralPath $GeneratorLocalSaves)) {
    throw 'NEEDS_CONTEXT: generator worktree drifted across the host apply_patch seam.'
}
$GreenGate = Invoke-GeneratorStructureGate $GeneratorFixturePath
Assert-ExactProperties $GreenGate @(
    'parse_error_count','quit_call_count','returned_finish_codes','finish_returns_97','finish_returns_code','native_tail'
) 'GREEN AST result'
$GreenCodes = @($GreenGate.returned_finish_codes | ForEach-Object {
    if (-not (Test-RecoveryIntegral $_)) { throw 'NEEDS_CONTEXT: GREEN returned_finish_codes contains a non-integral value.' }
    [int]$_
})
if ($GreenGate.parse_error_count -isnot [int] -or $GreenGate.parse_error_count -ne 0 -or
    $GreenGate.quit_call_count -isnot [int] -or $GreenGate.quit_call_count -ne 0 -or
    ($GreenCodes -join ',') -cne '0,41,42,43' -or
    $GreenGate.finish_returns_97 -isnot [bool] -or -not $GreenGate.finish_returns_97 -or
    $GreenGate.finish_returns_code -isnot [bool] -or -not $GreenGate.finish_returns_code -or
    $GreenGate.native_tail -isnot [bool] -or -not $GreenGate.native_tail) {
    throw 'NEEDS_CONTEXT: repaired fixture did not satisfy the exact GREEN exit structure.'
}
$GreenFixtureSeal = New-FileSeal $GeneratorFixturePath
$GoodStdout = [IO.File]::ReadAllBytes($V2StdoutPath)
$GoodEngine = [IO.File]::ReadAllBytes($V2EngineLogPath)
$EmptyBytes = New-Object byte[] 0
# TASK1_V3_MUTATION_SUITE_BEGIN
function Invoke-V3ChannelControl(
    [byte[]]$StdoutBytes,[byte[]]$StderrBytes,[byte[]]$EngineBytes,
    [string]$DeclaredStdoutPath,[string]$RequestStdoutPath,[string]$ResultStdoutPath,
    [bool]$ObserverMode
) {
    $EngineEvidenceSeal = [pscustomobject][ordered]@{
        path = Get-CanonicalPath 'C:\v3-control\engine-evidence.txt'
        bytes = [int64]$EngineBytes.Length
        sha256 = Get-V3BytesSha256 $EngineBytes
    }
    $Envelope = [pscustomobject][ordered]@{
        stdout_exists=$true; stdout_path=$DeclaredStdoutPath; request_stdout_path=$RequestStdoutPath
        result_stdout_path=$ResultStdoutPath; stdout_bytes=$StdoutBytes
        stderr_exists=$true; stderr_bytes=$StderrBytes; engine_exists=$true
        engine_source_path=(Get-CanonicalPath $V2EngineLogPath)
        engine_bytes=$EngineBytes; engine_evidence_seal=$EngineEvidenceSeal
    }
    $Mode = if ($ObserverMode) { 'observer' } else { 'generator' }
    return (Test-V3ChannelContract $Mode $Envelope)
}
function Convert-TextBytes([string]$Text) { return $StrictUtf8.GetBytes($Text) }
$GoodStdoutText = $StrictUtf8.GetString($GoodStdout)
$GoodEngineText = $StrictUtf8.GetString($GoodEngine)
$Declared = Get-CanonicalPath (Join-Path $GeneratorProcessEvidence 'stdout.txt')
$Mutations = New-Object 'System.Collections.Generic.List[object]'
function Add-Mutation([string]$Name,[string]$Expected,[string]$Actual) {
    $Verdict = if ($Expected -ceq $Actual) { 'PASS' } else { 'FAIL' }
    [void]$Mutations.Add([ordered]@{ name=$Name; expected=$Expected; actual=$Actual; verdict=$Verdict })
    if ($Verdict -cne 'PASS') { throw ('NEEDS_CONTEXT: offline mutation failed ' + $Name) }
}
function Invoke-V3EnvironmentControl([object[]]$Entries,[string[]]$ExpectedNames) {
    $ControlRoot = Get-CanonicalPath 'C:\v3-control\generator'
    $ExpectedValues = [object[]]@($ExpectedNames | ForEach-Object { 'x' })
    $Request = [pscustomobject][ordered]@{
        schema_version=1; executable=(Get-CanonicalPath 'C:\v3-control\renpy.exe')
        arguments=[object[]]@($ControlRoot,'test','terminal_collapse_legacy_generator','--savedir',(Get-CanonicalPath 'C:\v3-control\generator-save'))
        working_directory=$ControlRoot; environment_overrides=[object[]]$Entries
        timeout_milliseconds=[int64]180000; stdout_path=(Get-CanonicalPath 'C:\v3-control\stdout.txt')
        stderr_path=(Get-CanonicalPath 'C:\v3-control\stderr.txt'); result_path=(Get-CanonicalPath 'C:\v3-control\result.json')
    }
    $Expected = [pscustomobject][ordered]@{
        executable=$Request.executable; arguments=[object[]]$Request.arguments; working_directory=$ControlRoot
        environment_names=[object[]]$ExpectedNames; environment_values=$ExpectedValues
        timeout_milliseconds=[int64]180000; stdout_path=$Request.stdout_path
        stderr_path=$Request.stderr_path; result_path=$Request.result_path
    }
    return (Test-V3RequestContract 'generator' $Request $Expected)
}
$ControlGeneratorEnvironmentNames = [string[]]$GeneratorEnvironmentNames.Clone()
$GoodControlEnvironment = @($ControlGeneratorEnvironmentNames | ForEach-Object {
    [pscustomobject][ordered]@{ name=$_; value='x' }
})
function Replace-First([string]$Text,[string]$Pattern,[string]$Replacement) {
    return [regex]::Replace($Text,$Pattern,$Replacement,1)
}
$NoPass = Convert-TextBytes (Replace-First $GoodStdoutText $PassStatusPattern '')
$TwoPass = Convert-TextBytes ($GoodStdoutText + '[rpytest] Status: PASSED ' + "`n")
$Failed = Convert-TextBytes (Replace-First $GoodStdoutText 'PASSED' 'FAILED')
$SecondStatus = Convert-TextBytes ($GoodStdoutText + '[rpytest] Status: SKIPPED' + "`n")
$BomStdout = [byte[]](@(0xEF,0xBB,0xBF) + @($GoodStdout))
$InvalidUtf8 = [byte[]]@(0xC3,0x28,0x0A)
$NulStdout = [byte[]](@($GoodStdout[0..9]) + @(0) + @($GoodStdout[10..($GoodStdout.Length-1)]))
$IsolatedCr = [byte[]]@(
    @($GoodStdout[0..($GoodStdout.Length - 3)]) + @(0x0D) +
    @($GoodStdout[($GoodStdout.Length - 2)..($GoodStdout.Length - 1)])
)
if ($GoodStdout.Length -eq 0 -or $GoodStdout[$GoodStdout.Length - 1] -ne 0x0A) {
    throw 'NEEDS_CONTEXT: no-terminal-LF positive control must end in LF.'
}
$NoFinalLf = New-Object byte[] ($GoodStdout.Length + 1)
[Array]::Copy($GoodStdout,$NoFinalLf,$GoodStdout.Length)
$NoFinalLf[$GoodStdout.Length] = [byte]0x78
$NoFinalLfText = $StrictUtf8.GetString($NoFinalLf)
if ($NoFinalLf[$NoFinalLf.Length - 1] -eq 0x0A -or
    [regex]::IsMatch($NoFinalLfText,"`r(?!`n)")) {
    throw 'NEEDS_CONTEXT: no-terminal-LF mutation is not isolated.'
}
$NoSuite = Convert-TextBytes (Replace-First $GoodStdoutText $SuitePattern '')
$TwoSuite = Convert-TextBytes ($GoodStdoutText + '[rpytest] [log] - global.terminal_collapse_legacy_generator' + "`n")
$NoSummary = Convert-TextBytes (Replace-First $GoodStdoutText $SummaryPattern '')
$TwoSummary = Convert-TextBytes ($GoodStdoutText + '[rpytest] Test outcomes (Summary)' + "`n")
$PassOnlyEngine = Convert-TextBytes ($GoodEngineText + '[rpytest] Status: PASSED' + "`n")
$BomEngine = [byte[]](@(0xEF,0xBB,0xBF) + @($GoodEngine))
$NulEngine = [byte[]](@($GoodEngine) + @(0))
$EngineRpytest = Convert-TextBytes ($GoodEngineText + '[rpytest] diagnostic' + "`n")
$EngineTraceback = Convert-TextBytes ($GoodEngineText + 'Traceback (most recent call last):' + "`n")
$EngineUncaught = Convert-TextBytes ($GoodEngineText + "I'm sorry, but an uncaught exception occurred." + "`n")
Add-Mutation 'stdout_missing_passed' 'REJECT' (Invoke-V3ChannelControl $NoPass $EmptyBytes $GoodEngine $Declared $Declared $Declared $false)
Add-Mutation 'stdout_duplicate_passed' 'REJECT' (Invoke-V3ChannelControl $TwoPass $EmptyBytes $GoodEngine $Declared $Declared $Declared $false)
Add-Mutation 'stdout_failed_status' 'REJECT' (Invoke-V3ChannelControl $Failed $EmptyBytes $GoodEngine $Declared $Declared $Declared $false)
Add-Mutation 'stdout_second_any_status' 'REJECT' (Invoke-V3ChannelControl $SecondStatus $EmptyBytes $GoodEngine $Declared $Declared $Declared $false)
Add-Mutation 'stdout_empty' 'REJECT' (Invoke-V3ChannelControl $EmptyBytes $EmptyBytes $GoodEngine $Declared $Declared $Declared $false)
Add-Mutation 'stdout_bom' 'REJECT' (Invoke-V3ChannelControl $BomStdout $EmptyBytes $GoodEngine $Declared $Declared $Declared $false)
Add-Mutation 'stdout_invalid_utf8' 'REJECT' (Invoke-V3ChannelControl $InvalidUtf8 $EmptyBytes $GoodEngine $Declared $Declared $Declared $false)
Add-Mutation 'stdout_nul' 'REJECT' (Invoke-V3ChannelControl $NulStdout $EmptyBytes $GoodEngine $Declared $Declared $Declared $false)
Add-Mutation 'stdout_isolated_cr' 'REJECT' (Invoke-V3ChannelControl $IsolatedCr $EmptyBytes $GoodEngine $Declared $Declared $Declared $false)
Add-Mutation 'stdout_no_terminal_lf' 'REJECT' (Invoke-V3ChannelControl $NoFinalLf $EmptyBytes $GoodEngine $Declared $Declared $Declared $false)
$EngineSourceControlPath = Get-CanonicalPath $V2EngineLogPath
Add-Mutation 'stdout_path_is_engine_log' 'REJECT' (Invoke-V3ChannelControl $GoodStdout $EmptyBytes $GoodEngine `
    $EngineSourceControlPath $EngineSourceControlPath $EngineSourceControlPath $false)
Add-Mutation 'request_result_stdout_mismatch' 'REJECT' (Invoke-V3ChannelControl $GoodStdout $EmptyBytes $GoodEngine $Declared $Declared ($Declared + '.other') $false)
Add-Mutation 'suite_identity_missing' 'REJECT' (Invoke-V3ChannelControl $NoSuite $EmptyBytes $GoodEngine $Declared $Declared $Declared $false)
Add-Mutation 'suite_identity_duplicate' 'REJECT' (Invoke-V3ChannelControl $TwoSuite $EmptyBytes $GoodEngine $Declared $Declared $Declared $false)
Add-Mutation 'summary_missing' 'REJECT' (Invoke-V3ChannelControl $NoSummary $EmptyBytes $GoodEngine $Declared $Declared $Declared $false)
Add-Mutation 'summary_duplicate' 'REJECT' (Invoke-V3ChannelControl $TwoSummary $EmptyBytes $GoodEngine $Declared $Declared $Declared $false)
Add-Mutation 'stderr_one_byte' 'REJECT' (Invoke-V3ChannelControl $GoodStdout ([byte[]]@(0x78)) $GoodEngine $Declared $Declared $Declared $false)
Add-Mutation 'passed_only_in_engine_log' 'REJECT' (Invoke-V3ChannelControl $NoPass $EmptyBytes $PassOnlyEngine $Declared $Declared $Declared $false)
$MissingEngineEnvelope = [pscustomobject][ordered]@{
    stdout_exists=$true; stdout_path=$Declared; request_stdout_path=$Declared; result_stdout_path=$Declared
    stdout_bytes=$GoodStdout; stderr_exists=$true; stderr_bytes=$EmptyBytes; engine_exists=$false
    engine_source_path=(Get-CanonicalPath $V2EngineLogPath)
    engine_bytes=$GoodEngine; engine_evidence_seal=[pscustomobject][ordered]@{
        path=(Get-CanonicalPath 'C:\v3-control\engine-evidence.txt'); bytes=[int64]$GoodEngine.Length
        sha256=(Get-V3BytesSha256 $GoodEngine)
    }
}
Add-Mutation 'engine_log_missing' 'REJECT' (Test-V3ChannelContract 'generator' $MissingEngineEnvelope)
Add-Mutation 'engine_log_empty' 'REJECT' (Invoke-V3ChannelControl $GoodStdout $EmptyBytes $EmptyBytes $Declared $Declared $Declared $false)
Add-Mutation 'engine_log_bom' 'REJECT' (Invoke-V3ChannelControl $GoodStdout $EmptyBytes $BomEngine $Declared $Declared $Declared $false)
Add-Mutation 'engine_log_invalid_utf8' 'REJECT' (Invoke-V3ChannelControl $GoodStdout $EmptyBytes $InvalidUtf8 $Declared $Declared $Declared $false)
Add-Mutation 'engine_log_nul' 'REJECT' (Invoke-V3ChannelControl $GoodStdout $EmptyBytes $NulEngine $Declared $Declared $Declared $false)
Add-Mutation 'generator_engine_log_rpytest_line' 'REJECT' (Invoke-V3ChannelControl $GoodStdout $EmptyBytes $EngineRpytest $Declared $Declared $Declared $false)
Add-Mutation 'engine_log_traceback' 'REJECT' (Invoke-V3ChannelControl $GoodStdout $EmptyBytes $EngineTraceback $Declared $Declared $Declared $false)
Add-Mutation 'engine_log_uncaught_exception' 'REJECT' (Invoke-V3ChannelControl $GoodStdout $EmptyBytes $EngineUncaught $Declared $Declared $Declared $false)
function Copy-V3ControlObject([object]$Value) {
    return (($Value | ConvertTo-Json -Depth 16 -Compress) | ConvertFrom-Json -ErrorAction Stop)
}
function New-V3ControlSeal([string]$Path,[byte[]]$Bytes) {
    return [pscustomobject][ordered]@{
        path=(Get-CanonicalPath $Path); bytes=[int64]$Bytes.Length; sha256=(Get-V3BytesSha256 $Bytes)
    }
}
$V2Attempt = Read-RecoveryStrictJson $V2AttemptPath 'physical v2 completion control attempt'
$V2RequestPath = Join-Path $V2RecoveryRoot 'generator-process\request.json'
$V2ResultPath = Join-Path $V2RecoveryRoot 'generator-process\result.json'
$V2StderrPath = Join-Path $V2RecoveryRoot 'generator-process\stderr.txt'
$V2StatePath = Join-Path $V2RecoveryRoot 'generator-state.json'
$V2FixturePath = Get-CanonicalPath ([string]$V2Attempt.fixture_path)
$ControlExternalRoot = Get-CanonicalPath ([string]$V2Attempt.savedir_path)
$ControlLocalRoot = Get-CanonicalPath (Join-Path ([string]$V2Attempt.worktree_path) 'game\saves')
$V2GeneratorStateControl = Read-RecoveryStrictJson $V2StatePath `
    'physical frozen v2 generator state positive control'
$V2ControlMarker = 'terminal-collapse-legacy-v2:' + $P2 + ':supply-vanguard-remember:final-menu'
if ((Get-CanonicalPath ([string]$V2Attempt.state_path)) -cne (Get-CanonicalPath $V2StatePath) -or
    (Test-V3GeneratorStateContract $V2GeneratorStateControl $ControlExternalRoot `
        $V2ControlMarker $P2 $GameTree) -cne 'ACCEPT') {
    throw 'NEEDS_CONTEXT: physical frozen v2 generator state positive control did not ACCEPT.'
}
$ControlAttemptSeal = New-FileSeal $V2AttemptPath
$ControlFixtureSeal = New-FileSeal $V2FixturePath
$ControlFixtureEvidenceSeal = $ControlFixtureSeal
$ControlRequestSeal = New-FileSeal $V2RequestPath
$ControlResultSeal = New-FileSeal $V2ResultPath
$ControlStateSeal = New-FileSeal $V2StatePath
$ControlStdoutSeal = New-FileSeal $V2StdoutPath
$ControlStderrSeal = New-FileSeal $V2StderrPath
$ControlEngineEvidenceSeal = New-FileSeal $V2EngineLogPath
$V2RequestControl = Read-HelperJson $V2RequestPath 'physical v2 runtime request control'
$V2ResultControl = Read-HelperJson $V2ResultPath 'physical v2 runtime result control'
$V2ExternalTree = Get-RecoveryNonFollowingTree $ControlExternalRoot $false 'physical v2 external control'
$V2LocalTree = Get-RecoveryNonFollowingTree $ControlLocalRoot $false 'physical v2 local control'
$V2TargetPaths = [string[]]@(
    @($V2ExternalTree.files | Where-Object { (Split-Path $_ -Leaf) -like '1-1-*.save' }) +
    @($V2LocalTree.files | Where-Object { (Split-Path $_ -Leaf) -like '1-1-*.save' })
)
[Array]::Sort($V2TargetPaths,[StringComparer]::Ordinal)
$V2AllTargets = @($V2TargetPaths | ForEach-Object { Get-Item -LiteralPath $_ -Force -ErrorAction Stop })
$V2ExternalTarget = @($V2AllTargets | Where-Object {
    (Get-CanonicalPath $_.DirectoryName) -ceq $ControlExternalRoot
})
$V2SyncTarget = @($V2AllTargets | Where-Object {
    (Get-CanonicalPath $_.DirectoryName) -ceq (Get-CanonicalPath (Join-Path $ControlExternalRoot 'sync'))
})
$V2LocalTarget = @($V2AllTargets | Where-Object {
    (Get-CanonicalPath $_.DirectoryName) -ceq $ControlLocalRoot
})
if ($V2AllTargets.Count -ne 3 -or $V2ExternalTarget.Count -ne 1 -or
    $V2SyncTarget.Count -ne 1 -or $V2LocalTarget.Count -ne 1) {
    throw 'NEEDS_CONTEXT: physical v2 completion control does not have exact root/sync/local targets.'
}
$ControlTargetSeals = [object[]]@(
    (New-FileSeal $V2ExternalTarget[0].FullName),(New-FileSeal $V2SyncTarget[0].FullName),
    (New-FileSeal $V2LocalTarget[0].FullName)
)
$ControlSaveName = [string]$V2ExternalTarget[0].Name
$ControlTargetBytes = [IO.File]::ReadAllBytes([string]$ControlTargetSeals[0].path)
function New-V3PhysicalControlInventory([string]$ExternalRoot,[string]$LocalRoot) {
    $Directories = New-Object 'System.Collections.Generic.List[object]'
    $Files = New-Object 'System.Collections.Generic.List[object]'
    foreach ($RootSpec in @(
        [pscustomobject]@{role='external';path=(Get-CanonicalPath $ExternalRoot)},
        [pscustomobject]@{role='local';path=(Get-CanonicalPath $LocalRoot)}
    )) {
        $PhysicalTree = Get-RecoveryNonFollowingTree $RootSpec.path $false `
            ('physical v2 control ' + [string]$RootSpec.role)
        [void]$Directories.Add([pscustomobject][ordered]@{root_role=$RootSpec.role;relative_path='.'})
        foreach ($DirectoryPath in $PhysicalTree.directories) {
            $Relative = $DirectoryPath.Substring($RootSpec.path.Length).TrimStart('\').Replace('\','/')
            [void]$Directories.Add([pscustomobject][ordered]@{root_role=$RootSpec.role;relative_path=$Relative})
        }
        foreach ($FilePath in $PhysicalTree.files) {
            $File = Get-Item -LiteralPath $FilePath -Force -ErrorAction Stop
            $Relative = $FilePath.Substring($RootSpec.path.Length).TrimStart('\').Replace('\','/')
            $Kind = if ($File.Name -like '1-1-*.save') {'target'} elseif ($File.Name -like 'auto-*.save') {
                'autosave'
            } elseif ($File.Name -ceq 'persistent') {'persistent'} else {
                throw ('NEEDS_CONTEXT: unexpected physical v2 control file ' + $File.FullName)
            }
            $Seal = New-FileSeal $File.FullName
            [void]$Files.Add([pscustomobject][ordered]@{
                root_role=$RootSpec.role;relative_path=$Relative;kind=$Kind
                bytes=[int64]$Seal.bytes;sha256=[string]$Seal.sha256
            })
        }
    }
    return [pscustomobject][ordered]@{
        roots=[pscustomobject][ordered]@{external_savedir=(Get-CanonicalPath $ExternalRoot);local_savedir=(Get-CanonicalPath $LocalRoot)}
        directories=[object[]]$Directories.ToArray()
        files=[object[]]$Files.ToArray()
        target_count=3
    }
}
$ControlInventory = New-V3PhysicalControlInventory $ControlExternalRoot $ControlLocalRoot
$ControlAttemptId = [string]$V2Attempt.attempt_id
$ControlLockHash = [string]$V2Attempt.approval_lock_sha256
$ControlManifestHash = [string]$V2Attempt.predecessor_manifest_sha256
$ControlRedHash = [string]$V2Attempt.red_record_sha256
$ControlGreenHash = [string]$V2Attempt.green_record_sha256
$ControlGeneratorExpected = [pscustomobject][ordered]@{
    attempt_id=$ControlAttemptId; attempt_seal=$ControlAttemptSeal; approval_lock_sha256=$ControlLockHash
    approved_plan_commit=[string]$V2Attempt.approved_plan_commit
    predecessor_manifest_sha256=$ControlManifestHash; red_record_sha256=$ControlRedHash
    green_record_sha256=$ControlGreenHash; worktree_path=(Get-CanonicalPath ([string]$V2Attempt.worktree_path))
    savedir_path=$ControlExternalRoot; process_evidence_dir=(Get-CanonicalPath ([string]$V2Attempt.process_evidence_dir))
    fixture_seal=$ControlFixtureSeal; fixture_evidence_seal=$ControlFixtureEvidenceSeal
    request_seal=$ControlRequestSeal; result_seal=$ControlResultSeal; state_seal=$ControlStateSeal
    stdout_seal=$ControlStdoutSeal; stderr_seal=$ControlStderrSeal
    engine_log_evidence_seal=$ControlEngineEvidenceSeal; target_seals=[object[]]$ControlTargetSeals
    save_name=$ControlSaveName; save_inventory=$ControlInventory
}
$ControlGeneratorCompletion = [pscustomobject][ordered]@{
    schema_version=2; attempt_id=$ControlAttemptId; attempt_path=[string]$ControlAttemptSeal.path
    attempt_sha256=[string]$ControlAttemptSeal.sha256; approval_lock_sha256=$ControlLockHash
    approved_plan_commit=[string]$ControlGeneratorExpected.approved_plan_commit
    predecessor_manifest_sha256=$ControlManifestHash; red_record_sha256=$ControlRedHash; green_record_sha256=$ControlGreenHash
    worktree_path=[string]$ControlGeneratorExpected.worktree_path; savedir_path=$ControlExternalRoot
    process_evidence_dir=[string]$ControlGeneratorExpected.process_evidence_dir
    fixture_path=[string]$ControlFixtureSeal.path; fixture_sha256=[string]$ControlFixtureSeal.sha256
    fixture_evidence_path=[string]$ControlFixtureEvidenceSeal.path; fixture_evidence_sha256=[string]$ControlFixtureEvidenceSeal.sha256
    request_path=[string]$ControlRequestSeal.path; request_bytes=[int64]$ControlRequestSeal.bytes; request_sha256=[string]$ControlRequestSeal.sha256
    result_path=[string]$ControlResultSeal.path; result_bytes=[int64]$ControlResultSeal.bytes; result_sha256=[string]$ControlResultSeal.sha256
    state_path=[string]$ControlStateSeal.path; state_bytes=[int64]$ControlStateSeal.bytes; state_sha256=[string]$ControlStateSeal.sha256
    rpytest_stdout_path=[string]$ControlStdoutSeal.path; rpytest_stdout_bytes=[int64]$ControlStdoutSeal.bytes
    rpytest_stdout_sha256=[string]$ControlStdoutSeal.sha256; stderr_path=[string]$ControlStderrSeal.path
    stderr_bytes=[int64]$ControlStderrSeal.bytes; stderr_sha256=[string]$ControlStderrSeal.sha256
    engine_log_evidence_path=[string]$ControlEngineEvidenceSeal.path; engine_log_evidence_sha256=[string]$ControlEngineEvidenceSeal.sha256
    external_save_path=[string]$ControlTargetSeals[0].path; sync_save_path=[string]$ControlTargetSeals[1].path
    local_save_path=[string]$ControlTargetSeals[2].path; target_copy_count=3; save_name=$ControlSaveName
    save_bytes=[int64]$ControlTargetBytes.Length; save_sha256=[string]$ControlTargetSeals[0].sha256
    save_inventory=$ControlInventory; finished_utc='2026-08-14T00:00:00.0000000+00:00'
}
if ((Test-V3GeneratorCompletionContract $ControlGeneratorCompletion $ControlGeneratorExpected) -cne 'ACCEPT') {
    throw 'NEEDS_CONTEXT: unmutated generator completion control did not ACCEPT.'
}
$ControlGeneratorEnvelope = [pscustomobject][ordered]@{
    stdout_exists=$true; stdout_path=[string]$ControlStdoutSeal.path
    request_stdout_path=(Get-CanonicalPath ([string]$V2RequestControl.stdout_path))
    result_stdout_path=(Get-CanonicalPath ([string]$V2ResultControl.stdout_path))
    stdout_bytes=$GoodStdout; stderr_exists=$true; stderr_bytes=$EmptyBytes; engine_exists=$true
    engine_source_path=(Get-CanonicalPath $V2EngineLogPath)
    engine_bytes=$GoodEngine; engine_evidence_seal=$ControlEngineEvidenceSeal
}
if ((Test-V3GeneratorRuntimeEvidenceContract $ControlGeneratorEnvelope `
        $ControlGeneratorCompletion $ControlGeneratorExpected) -cne 'ACCEPT') {
    throw 'NEEDS_CONTEXT: unmutated physical v2 full runtime control did not ACCEPT.'
}
$DriftEngineBytes = [byte[]]$GoodEngine.Clone()
$DriftAsciiIndex = [Array]::IndexOf($DriftEngineBytes,[byte]0x20)
if ($DriftAsciiIndex -lt 0) { throw 'NEEDS_CONTEXT: physical v2 engine control has no ASCII space to mutate.' }
$DriftEngineBytes[$DriftAsciiIndex] = [byte]0x21
$DriftEngineSeal = [pscustomobject][ordered]@{
    path=[string]$ControlEngineEvidenceSeal.path; bytes=[int64]$DriftEngineBytes.Length
    sha256=(Get-V3BytesSha256 $DriftEngineBytes)
}
$EngineSealDriftEnvelope = [pscustomobject][ordered]@{
    stdout_exists=$true; stdout_path=[string]$ControlStdoutSeal.path
    request_stdout_path=(Get-CanonicalPath ([string]$V2RequestControl.stdout_path))
    result_stdout_path=(Get-CanonicalPath ([string]$V2ResultControl.stdout_path))
    stdout_bytes=$GoodStdout; stderr_exists=$true; stderr_bytes=$EmptyBytes; engine_exists=$true
    engine_source_path=(Get-CanonicalPath $V2EngineLogPath)
    engine_bytes=$DriftEngineBytes; engine_evidence_seal=$DriftEngineSeal
}
Add-Mutation 'engine_log_evidence_byte_drift' 'REJECT' (Test-V3GeneratorRuntimeEvidenceContract `
    $EngineSealDriftEnvelope $ControlGeneratorCompletion $ControlGeneratorExpected)
$StdoutSealDriftCompletion = Copy-V3ControlObject $ControlGeneratorCompletion
$StdoutSealDriftPrefix = if ([string]$StdoutSealDriftCompletion.rpytest_stdout_sha256 -cmatch '^A') {'B'} else {'A'}
$StdoutSealDriftCompletion.rpytest_stdout_sha256 = ($StdoutSealDriftPrefix + [string]$StdoutSealDriftCompletion.rpytest_stdout_sha256.Substring(1))
Add-Mutation 'generator_completion_stdout_seal_drift' 'REJECT' (Test-V3GeneratorCompletionContract $StdoutSealDriftCompletion $ControlGeneratorExpected)
$RequestSealDriftCompletion = Copy-V3ControlObject $ControlGeneratorCompletion
$RequestSealDriftCompletion.request_bytes = [int64]$RequestSealDriftCompletion.request_bytes + 1
Add-Mutation 'request_seal_drift' 'REJECT' (Test-V3GeneratorCompletionContract $RequestSealDriftCompletion $ControlGeneratorExpected)
$StderrSealDriftCompletion = Copy-V3ControlObject $ControlGeneratorCompletion
$StderrSealDriftCompletion.stderr_bytes = [int64]1
Add-Mutation 'stderr_seal_drift' 'REJECT' (Test-V3GeneratorCompletionContract $StderrSealDriftCompletion $ControlGeneratorExpected)
$MissingCompletion = Copy-V3ControlObject $ControlGeneratorCompletion
$MissingCompletion.PSObject.Properties.Remove('finished_utc')
$ExtraCompletion = Copy-V3ControlObject $ControlGeneratorCompletion
$ExtraCompletion | Add-Member -MemberType NoteProperty -Name extra -Value 'x'
$ReorderedNames = [string[]]$GeneratorCompletionProperties.Clone()
$Swap = $ReorderedNames[0]; $ReorderedNames[0] = $ReorderedNames[1]; $ReorderedNames[1] = $Swap
$ReorderedTable = [ordered]@{}
foreach ($ReorderedName in $ReorderedNames) { $ReorderedTable[$ReorderedName] = $ControlGeneratorCompletion.$ReorderedName }
$ReorderedCompletion = [pscustomobject]$ReorderedTable
$CompletionShapeActual = @(
    (Test-V3GeneratorCompletionContract $MissingCompletion $ControlGeneratorExpected),
    (Test-V3GeneratorCompletionContract $ExtraCompletion $ControlGeneratorExpected),
    (Test-V3GeneratorCompletionContract $ReorderedCompletion $ControlGeneratorExpected)
) -join '/'
Add-Mutation 'completion_shape_drift' 'REJECT/REJECT/REJECT' $CompletionShapeActual
Add-Mutation 'request_environment_missing_key' 'REJECT' (Invoke-V3EnvironmentControl $GoodControlEnvironment[0..9] $ControlGeneratorEnvironmentNames)
$ExtraEnvironment = @($GoodControlEnvironment + [pscustomobject][ordered]@{name='ZZ_EXTRA';value='x'})
Add-Mutation 'request_environment_extra_key' 'REJECT' (Invoke-V3EnvironmentControl $ExtraEnvironment $ControlGeneratorEnvironmentNames)
$DuplicateEnvironment = @($GoodControlEnvironment)
$DuplicateEnvironment[$DuplicateEnvironment.Count - 1] = $GoodControlEnvironment[0]
if ($DuplicateEnvironment.Count -ne 11) { throw 'NEEDS_CONTEXT: duplicate-key control lost exact 11-entry cardinality.' }
Add-Mutation 'request_environment_duplicate_key' 'REJECT' (Invoke-V3EnvironmentControl $DuplicateEnvironment $ControlGeneratorEnvironmentNames)
$ReorderedEnvironment = @($GoodControlEnvironment)
$EnvironmentSwap = $ReorderedEnvironment[0]; $ReorderedEnvironment[0] = $ReorderedEnvironment[1]; $ReorderedEnvironment[1] = $EnvironmentSwap
Add-Mutation 'request_environment_reordered_key' 'REJECT' (Invoke-V3EnvironmentControl $ReorderedEnvironment $ControlGeneratorEnvironmentNames)
$ControlMarker = 'terminal-collapse-legacy-v3:0123456789abcdef0123456789abcdef01234567:supply-vanguard-remember:final-menu'
$ControlMetadata = [pscustomobject][ordered]@{
    _ctime=[double]1.0; _game_runtime=[double]1.0; _renpy_version=[object[]]@(8,5,2,26010301)
    _save_name=''; _version='3.10'; tc_baseline_commit=[string]$ControlGeneratorExpected.approved_plan_commit
    tc_choice_path=[object[]]$ExpectedChoicePath; tc_game_tree='0123456789abcdef0123456789abcdef01234567'
    tc_legacy_marker=$ControlMarker; tc_legacy_schema=1; tc_menu_file='game/chapter5.rpy'; tc_menu_line=2807
    tc_state=[pscustomobject][ordered]@{intrigue=55;iron_prepared=$true;power=60}
}
$ControlObserverActual = [pscustomobject][ordered]@{
    argument_savedir=(Get-CanonicalPath 'C:\v3-control\observer-save'); auto_load_value='1-1'; command='run'
    configured_savedir=(Get-CanonicalPath 'C:\v3-control\observer-save'); context_count=1
    context_current="('game/chapter5.rpy', 1297438219, 9756)"; display_captions=[object[]]$ExpectedDisplayCaptions
    filename_line=[object[]]@('game/chapter5.rpy',2807); is_in_test=$false; is_top_context=$true
    node_file='game/chapter5.rpy'; node_line=2807; node_type='Menu'; path_to_saves_env_present=$false
    raw_captions=[object[]]$ExpectedRawCaptions; return_stack=[object[]]@(); slot_metadata=$ControlMetadata
    state=[pscustomobject][ordered]@{intrigue=55;iron_prepared=$true;power=60}; statement_name='menu'; store_marker=$ControlMarker
}
$ControlObserverChecksTable = [ordered]@{}
foreach ($CheckName in $ObserverStateCheckProperties) { $ControlObserverChecksTable[$CheckName] = $true }
$ControlObserverState = [pscustomobject][ordered]@{
    actual=$ControlObserverActual; checks=[pscustomobject]$ControlObserverChecksTable; failures=[object[]]@()
    loaded=$true; reason='clean baseline normal-run autoload reached the production final tactics menu'
    schema=1; verdict='PASS'
}
if ((Test-V3ObserverStateContract $ControlObserverState (Get-CanonicalPath 'C:\v3-control\observer-save') `
        $ControlMarker ([string]$ControlGeneratorExpected.approved_plan_commit) `
        '0123456789abcdef0123456789abcdef01234567' $ControlMetadata) -cne 'ACCEPT') {
    throw 'NEEDS_CONTEXT: unmutated observer state control did not ACCEPT.'
}
$BadObserverState = Copy-V3ControlObject $ControlObserverState
$BadObserverState.verdict = 'FAIL'
$BadObserverState.failures = [object[]]@('forged_log_cannot_override_failed_state')
$ForgedObserverEngine = Convert-TextBytes ($GoodEngineText + 'forged observer Status: PASSED' + "`n")
$ForgedObserverChannelVerdict = Invoke-V3ChannelControl $EmptyBytes $EmptyBytes $ForgedObserverEngine `
    $Declared $Declared $Declared $true
$ForgedObserverStateVerdict = Test-V3ObserverStateContract $BadObserverState `
    (Get-CanonicalPath 'C:\v3-control\observer-save') $ControlMarker `
    ([string]$ControlGeneratorExpected.approved_plan_commit) '0123456789abcdef0123456789abcdef01234567' $ControlMetadata
Add-Mutation 'observer_state_fail_fake_passed' 'ACCEPT/REJECT' `
    ($ForgedObserverChannelVerdict + '/' + $ForgedObserverStateVerdict)
Add-Mutation 'observer_stdout_nonempty' 'REJECT' (Invoke-V3ChannelControl ([byte[]]@(0x78)) $EmptyBytes $GoodEngine $Declared $Declared $Declared $true)
Add-Mutation 'observer_stderr_nonempty' 'REJECT' (Invoke-V3ChannelControl $EmptyBytes ([byte[]]@(0x78)) $GoodEngine $Declared $Declared $Declared $true)
Add-Mutation 'observer_engine_log_rpytest_line' 'REJECT' (Invoke-V3ChannelControl $EmptyBytes $EmptyBytes $EngineRpytest $Declared $Declared $Declared $true)
$ControlObserverAttemptSeal = New-V3ControlSeal 'C:\v3-control\observer-attempt\attempt.json' (Convert-TextBytes "observer-attempt`n")
$ControlObserverFixtureSeal = New-V3ControlSeal 'C:\v3-control\observer\game\zz_terminal_collapse_legacy_observer.rpy' (Convert-TextBytes "observer-fixture`n")
$ControlObserverFixtureEvidenceSeal = New-V3ControlSeal 'C:\v3-control\observer-fixture.rpy' (Convert-TextBytes "observer-fixture`n")
$ControlObserverRequestSeal = New-V3ControlSeal 'C:\v3-control\observer-process\request.json' (Convert-TextBytes "observer-request`n")
$ControlObserverResultSeal = New-V3ControlSeal 'C:\v3-control\observer-process\result.json' (Convert-TextBytes "observer-result`n")
$ControlObserverStateSeal = New-V3ControlSeal 'C:\v3-control\observer-state.json' (Convert-TextBytes "observer-state`n")
$ControlObserverStdoutSeal = New-V3ControlSeal 'C:\v3-control\observer-process\stdout.txt' $EmptyBytes
$ControlObserverStderrSeal = New-V3ControlSeal 'C:\v3-control\observer-process\stderr.txt' $EmptyBytes
$ControlObserverEngineSeal = New-V3ControlSeal 'C:\v3-control\observer-engine-log.txt' $GoodEngine
$ControlReplayRoot = Get-CanonicalPath 'C:\v3-control\observer-save'
$ControlObserverLocalRoot = Get-CanonicalPath 'C:\v3-control\observer\game\saves'
$ControlReplaySeal = New-V3ControlSeal (Join-Path $ControlReplayRoot $ControlSaveName) $ControlTargetBytes
$ControlSourceSeal = $ControlTargetSeals[0]
$ControlObserverInventory = [pscustomobject][ordered]@{
    roots=[pscustomobject][ordered]@{external_savedir=$ControlReplayRoot;local_savedir=$ControlObserverLocalRoot}
    directories=[object[]]@(
        [pscustomobject][ordered]@{root_role='external';relative_path='.'},
        [pscustomobject][ordered]@{root_role='local';relative_path='.'}
    )
    files=[object[]]@(
        [pscustomobject][ordered]@{root_role='external';relative_path=$ControlSaveName;kind='target';bytes=[int64]$ControlReplaySeal.bytes;sha256=[string]$ControlReplaySeal.sha256}
    )
    target_count=1
}
$ControlObserverExpected = [pscustomobject][ordered]@{
    attempt_id='fedcba9876543210fedcba9876543210'; attempt_seal=$ControlObserverAttemptSeal
    approval_lock_sha256=$ControlLockHash; approved_plan_commit=[string]$ControlGeneratorExpected.approved_plan_commit
    generator_completion_sha256=(Get-V3BytesSha256 (Convert-TextBytes 'generator-completion'))
    worktree_path=(Get-CanonicalPath 'C:\v3-control\observer'); savedir_path=$ControlReplayRoot
    process_evidence_dir=(Get-CanonicalPath 'C:\v3-control\observer-process')
    fixture_seal=$ControlObserverFixtureSeal; fixture_evidence_seal=$ControlObserverFixtureEvidenceSeal
    request_seal=$ControlObserverRequestSeal; result_seal=$ControlObserverResultSeal; state_seal=$ControlObserverStateSeal
    stdout_seal=$ControlObserverStdoutSeal; stderr_seal=$ControlObserverStderrSeal
    engine_log_evidence_seal=$ControlObserverEngineSeal; source_before_seal=$ControlSourceSeal
    source_after_seal=$ControlSourceSeal; replay_before_seal=$ControlReplaySeal; replay_after_seal=$ControlReplaySeal
    save_inventory=$ControlObserverInventory
}
$ControlObserverCompletion = [pscustomobject][ordered]@{
    schema_version=2; attempt_id=[string]$ControlObserverExpected.attempt_id; attempt_path=[string]$ControlObserverAttemptSeal.path
    attempt_sha256=[string]$ControlObserverAttemptSeal.sha256; approval_lock_sha256=$ControlLockHash
    approved_plan_commit=[string]$ControlObserverExpected.approved_plan_commit
    generator_completion_sha256=[string]$ControlObserverExpected.generator_completion_sha256
    worktree_path=[string]$ControlObserverExpected.worktree_path; savedir_path=$ControlReplayRoot
    process_evidence_dir=[string]$ControlObserverExpected.process_evidence_dir
    fixture_path=[string]$ControlObserverFixtureSeal.path; fixture_sha256=[string]$ControlObserverFixtureSeal.sha256
    fixture_evidence_path=[string]$ControlObserverFixtureEvidenceSeal.path; fixture_evidence_sha256=[string]$ControlObserverFixtureEvidenceSeal.sha256
    request_path=[string]$ControlObserverRequestSeal.path; request_bytes=[int64]$ControlObserverRequestSeal.bytes; request_sha256=[string]$ControlObserverRequestSeal.sha256
    result_path=[string]$ControlObserverResultSeal.path; result_bytes=[int64]$ControlObserverResultSeal.bytes; result_sha256=[string]$ControlObserverResultSeal.sha256
    state_path=[string]$ControlObserverStateSeal.path; state_bytes=[int64]$ControlObserverStateSeal.bytes; state_sha256=[string]$ControlObserverStateSeal.sha256
    stdout_path=[string]$ControlObserverStdoutSeal.path; stdout_bytes=[int64]$ControlObserverStdoutSeal.bytes; stdout_sha256=[string]$ControlObserverStdoutSeal.sha256
    stderr_path=[string]$ControlObserverStderrSeal.path; stderr_bytes=[int64]$ControlObserverStderrSeal.bytes; stderr_sha256=[string]$ControlObserverStderrSeal.sha256
    engine_log_evidence_path=[string]$ControlObserverEngineSeal.path; engine_log_evidence_sha256=[string]$ControlObserverEngineSeal.sha256
    source_save_path=[string]$ControlSourceSeal.path; source_save_bytes=[int64]$ControlSourceSeal.bytes
    source_save_sha256_before=[string]$ControlSourceSeal.sha256; source_save_sha256_after=[string]$ControlSourceSeal.sha256
    replay_save_path=[string]$ControlReplaySeal.path; replay_save_bytes=[int64]$ControlReplaySeal.bytes
    replay_save_sha256_before=[string]$ControlReplaySeal.sha256; replay_save_sha256_after=[string]$ControlReplaySeal.sha256
    save_inventory=$ControlObserverInventory; finished_utc='2026-08-14T00:00:00.0000000+00:00'
}
if ((Test-V3ObserverCompletionContract $ControlObserverCompletion $ControlObserverExpected) -cne 'ACCEPT') {
    throw 'NEEDS_CONTEXT: unmutated observer completion control did not ACCEPT.'
}
$MissingObserverCompletion = Copy-V3ControlObject $ControlObserverCompletion
$MissingObserverCompletion.PSObject.Properties.Remove('finished_utc')
$ExtraObserverCompletion = Copy-V3ControlObject $ControlObserverCompletion
$ExtraObserverCompletion | Add-Member -MemberType NoteProperty -Name extra -Value 'x'
$ReorderedObserverNames = [string[]]$ObserverCompletionProperties.Clone()
$ObserverSwap = $ReorderedObserverNames[0]
$ReorderedObserverNames[0] = $ReorderedObserverNames[1]
$ReorderedObserverNames[1] = $ObserverSwap
$ReorderedObserverTable = [ordered]@{}
foreach ($ReorderedObserverName in $ReorderedObserverNames) {
    $ReorderedObserverTable[$ReorderedObserverName] = $ControlObserverCompletion.$ReorderedObserverName
}
$ReorderedObserverCompletion = [pscustomobject]$ReorderedObserverTable
$WrongTypeObserverCompletion = Copy-V3ControlObject $ControlObserverCompletion
$WrongTypeObserverCompletion.stdout_bytes = '0'
$ObserverCompletionShapeActual = @(
    (Test-V3ObserverCompletionContract $MissingObserverCompletion $ControlObserverExpected),
    (Test-V3ObserverCompletionContract $ExtraObserverCompletion $ControlObserverExpected),
    (Test-V3ObserverCompletionContract $ReorderedObserverCompletion $ControlObserverExpected),
    (Test-V3ObserverCompletionContract $WrongTypeObserverCompletion $ControlObserverExpected)
) -join '/'
Add-Mutation 'observer_completion_shape_type_drift' 'REJECT/REJECT/REJECT/REJECT' `
    $ObserverCompletionShapeActual
Add-Mutation 'accept_rpytest_exc' 'ACCEPT' (Invoke-V3ChannelControl (Convert-TextBytes ($GoodStdoutText + '[rpytest] [exc] expected assertion detail' + "`n")) $EmptyBytes $GoodEngine $Declared $Declared $Declared $false)
Add-Mutation 'accept_dummy_renderer_error' 'ACCEPT' (Invoke-V3ChannelControl $GoodStdout $EmptyBytes (Convert-TextBytes ($GoodEngineText + "error('OpenGL support unavailable')" + "`n")) $Declared $Declared $Declared $false)
# TASK1_V3_MUTATION_SUITE_END
if ($Mutations.Count -ne 42 -or @($Mutations | Where-Object { $_.verdict -cne 'PASS' }).Count -ne 0) {
    throw 'NEEDS_CONTEXT: GREEN mutation suite is not exact 42/42 PASS.'
}
$GreenFixtureGate = [ordered]@{
    expected = 'no_quit_returned_finish_native_exit'
    observed = 'no_quit_returned_finish_native_exit'
    quit_call_count = 0
    returned_finish_codes = [int[]]@(0,41,42,43)
    returns_97 = $true
    returns_code = $true
    native_tail = $true
}
$GreenStreamGate = [ordered]@{
    selector = 'helper_stdout'
    test_report_status_count = 1
    engine_log_rpytest_line_count = 0
    verdict = 'PASS'
}
$GreenInputs = @(
    [ordered]@{ role='patched_generator_fixture'; path=[string]$GreenFixtureSeal.path; bytes=[int64]$GreenFixtureSeal.bytes; sha256=[string]$GreenFixtureSeal.sha256 },
    [ordered]@{ role='v2_test_report_control'; path=(Get-CanonicalPath $V2StdoutPath); bytes=[int64]1074; sha256='BD3B00124C6134FD0DAE737B293C20F68BF76F02ECDC69E77797C883FA5208CE' },
    [ordered]@{ role='v2_engine_boot_log_control'; path=(Get-CanonicalPath $V2EngineLogPath); bytes=[int64]1860; sha256='FE52BE91013D21B51AAF2CCDCF796289906EB4D12FA08EB1912A196B4F076A81' }
)
$GreenPayload = [ordered]@{
    schema_version = 3
    verdict = 'PASS'
    fixture_gate = $GreenFixtureGate
    stream_gate = $GreenStreamGate
    inputs = $GreenInputs
    mutations = $Mutations.ToArray()
    created_utc = [DateTime]::UtcNow.ToString('o',[Globalization.CultureInfo]::InvariantCulture)
}
$GreenRecord = New-ReadOnlyJsonRecord $GreenRecordPath $GreenPayload $ContractProperties 'generator contract GREEN'
Assert-ExactProperties $GreenRecord.fixture_gate @(
    'expected','observed','quit_call_count','returned_finish_codes','returns_97','returns_code','native_tail'
) 'GREEN fixture_gate'
Assert-ExactProperties $GreenRecord.stream_gate @(
    'selector','test_report_status_count','engine_log_rpytest_line_count','verdict'
) 'GREEN stream_gate'
if ($GreenRecord.schema_version -isnot [int] -or $GreenRecord.schema_version -ne 3 -or
    $GreenRecord.verdict -cne 'PASS' -or @($GreenRecord.inputs).Count -ne 3 -or
    @($GreenRecord.mutations).Count -ne 42 -or
    -not (Test-RoundtripUtc $GreenRecord.created_utc) -or
    (@($GreenRecord.mutations | ForEach-Object { [string]$_.name }) -join '|') -cne
        'stdout_missing_passed|stdout_duplicate_passed|stdout_failed_status|stdout_second_any_status|stdout_empty|stdout_bom|stdout_invalid_utf8|stdout_nul|stdout_isolated_cr|stdout_no_terminal_lf|stdout_path_is_engine_log|request_result_stdout_mismatch|suite_identity_missing|suite_identity_duplicate|summary_missing|summary_duplicate|stderr_one_byte|passed_only_in_engine_log|engine_log_missing|engine_log_empty|engine_log_bom|engine_log_invalid_utf8|engine_log_nul|generator_engine_log_rpytest_line|engine_log_traceback|engine_log_uncaught_exception|engine_log_evidence_byte_drift|generator_completion_stdout_seal_drift|request_seal_drift|stderr_seal_drift|completion_shape_drift|request_environment_missing_key|request_environment_extra_key|request_environment_duplicate_key|request_environment_reordered_key|observer_state_fail_fake_passed|observer_stdout_nonempty|observer_stderr_nonempty|observer_engine_log_rpytest_line|observer_completion_shape_type_drift|accept_rpytest_exc|accept_dummy_renderer_error') {
    throw 'NEEDS_CONTEXT: persisted GREEN exact-42 schema/order failed.'
}
$ExpectedGreenRoles = [string[]]@(
    'patched_generator_fixture','v2_test_report_control','v2_engine_boot_log_control'
)
$ExpectedGreenPaths = [string[]]@(
    (Get-CanonicalPath $GeneratorFixturePath),(Get-CanonicalPath $V2StdoutPath),(Get-CanonicalPath $V2EngineLogPath)
)
if ((@($GreenRecord.inputs | ForEach-Object { [string]$_.role }) -join '|') -cne ($ExpectedGreenRoles -join '|')) {
    throw 'NEEDS_CONTEXT: persisted GREEN input roles/order failed.'
}
for ($GreenInputIndex = 0; $GreenInputIndex -lt 3; $GreenInputIndex++) {
    $GreenInput = @($GreenRecord.inputs)[$GreenInputIndex]
    Assert-ExactProperties $GreenInput @('role','path','bytes','sha256') 'GREEN input'
    if ($GreenInput.role -isnot [string] -or [string]$GreenInput.role -cne $ExpectedGreenRoles[$GreenInputIndex] -or
        $GreenInput.path -isnot [string] -or -not [IO.Path]::IsPathRooted([string]$GreenInput.path) -or
        [string]$GreenInput.path -cne (Get-CanonicalPath ([string]$GreenInput.path)) -or
        [string]$GreenInput.path -cne $ExpectedGreenPaths[$GreenInputIndex] -or
        -not (Test-RecoveryIntegral $GreenInput.bytes) -or
        $GreenInput.sha256 -isnot [string] -or
        [string]$GreenInput.sha256 -cnotmatch '^[0-9A-F]{64}$') {
        throw ('NEEDS_CONTEXT: GREEN input schema/path failed ' + $ExpectedGreenRoles[$GreenInputIndex])
    }
    $GreenInputSeal = New-FileSeal $ExpectedGreenPaths[$GreenInputIndex]
    if ($GreenInputSeal.path -cne [string]$GreenInput.path -or
        $GreenInputSeal.bytes -ne [int64]$GreenInput.bytes -or
        $GreenInputSeal.sha256 -cne [string]$GreenInput.sha256) {
        throw ('NEEDS_CONTEXT: GREEN input current seal failed ' + $ExpectedGreenRoles[$GreenInputIndex])
    }
}
foreach ($GreenMutation in @($GreenRecord.mutations)) {
    Assert-ExactProperties $GreenMutation @('name','expected','actual','verdict') 'GREEN mutation'
    if ($GreenMutation.name -isnot [string] -or $GreenMutation.expected -isnot [string] -or
        $GreenMutation.actual -isnot [string] -or $GreenMutation.verdict -isnot [string] -or
        $GreenMutation.verdict -cne 'PASS') {
        throw ('NEEDS_CONTEXT: persisted GREEN mutation type/verdict failed ' + [string]$GreenMutation.name)
    }
}
$GreenRecordSha256 = (Get-FileHash -LiteralPath $GreenRecordPath -Algorithm SHA256).Hash
$GreenFixtureSha256 = [string]@($GreenRecord.inputs)[0].sha256
if ((Get-FileHash -LiteralPath $RedRecordPath -Algorithm SHA256).Hash -cne $RedRecordSha256 -or
    (Get-FileHash -LiteralPath $GeneratorFixturePath -Algorithm SHA256).Hash -cne $GreenFixtureSha256) {
    throw 'NEEDS_CONTEXT: RED or GREEN fixture seal drifted before attempt creation.'
}
```

Expected: the fresh scope proves the immutable RED checkpoint, exact P3 worktree scope, zero `.quit()` calls, returned codes `[0,41,42,43]`, both finish returns, native tail, and the ordered 42/42 offline mutation/control suite. RED and GREEN are read-only before any generator ledger or Ren'Py invocation.

- [ ] **Step 5: Consume the only generator opportunity with an 18-field create-new ledger**

```powershell
if (Test-Path -LiteralPath $GeneratorAttemptDir) {
    throw 'NEEDS_CONTEXT: the only recovery generator opportunity is already consumed; do not retry.'
}
Assert-RecoveryAuthorityUnchanged 'before generator attempt ledger'
[IO.Directory]::CreateDirectory($GeneratorAttemptDir) | Out-Null
git check-ignore -q -- $GeneratorAttemptDir
if ($LASTEXITCODE -ne 0) { throw 'Generator attempt ledger is not ignored.' }
$GeneratorAttemptId = [Guid]::NewGuid().ToString('N')
if ($GeneratorAttemptId -cnotmatch '^[0-9a-f]{32}$') { throw 'Generator attempt ID shape failed.' }
$GeneratorAttemptProperties = @(
    'schema_version','attempt_id','started_utc','approval_lock_sha256','approved_plan_commit',
    'predecessor_manifest_sha256','red_record_path','red_record_sha256','green_record_path',
    'green_record_sha256','worktree_path','savedir_path','process_evidence_dir','state_path',
    'fixture_path','fixture_sha256','max_generator_invocations','retry_allowed'
)
$GeneratorAttemptPayload = [ordered]@{
    schema_version = 2
    attempt_id = $GeneratorAttemptId
    started_utc = [DateTime]::UtcNow.ToString('o', [Globalization.CultureInfo]::InvariantCulture)
    approval_lock_sha256 = $ApprovalLockSha256
    approved_plan_commit = $P3
    predecessor_manifest_sha256 = [string]$Approval.predecessor_manifest_sha256
    red_record_path = Get-CanonicalPath $RedRecordPath
    red_record_sha256 = $RedRecordSha256
    green_record_path = Get-CanonicalPath $GreenRecordPath
    green_record_sha256 = $GreenRecordSha256
    worktree_path = Get-CanonicalPath $GeneratorRoot
    savedir_path = Get-CanonicalPath $GeneratorSaveDir
    process_evidence_dir = Get-CanonicalPath $GeneratorProcessEvidence
    state_path = Get-CanonicalPath $GeneratorStatePath
    fixture_path = Get-CanonicalPath $GeneratorFixturePath
    fixture_sha256 = $GreenFixtureSha256
    max_generator_invocations = 1
    retry_allowed = $false
}
$GeneratorAttempt = New-ReadOnlyJsonRecord $GeneratorAttemptPath $GeneratorAttemptPayload $GeneratorAttemptProperties 'generator attempt'
if ($GeneratorAttempt.schema_version -isnot [int] -or $GeneratorAttempt.schema_version -ne 2 -or
    $GeneratorAttempt.attempt_id -isnot [string] -or $GeneratorAttempt.attempt_id -cne $GeneratorAttemptId -or
    -not (Test-RoundtripUtc $GeneratorAttempt.started_utc) -or
    $GeneratorAttempt.max_generator_invocations -isnot [int] -or $GeneratorAttempt.max_generator_invocations -ne 1 -or
    $GeneratorAttempt.retry_allowed -isnot [bool] -or $GeneratorAttempt.retry_allowed -or
    $GeneratorAttempt.fixture_sha256 -isnot [string] -or $GeneratorAttempt.fixture_sha256 -cne $GreenFixtureSha256) {
    throw 'NEEDS_CONTEXT: generator attempt strict reread failed.'
}
$GeneratorAttemptSha256 = (Get-FileHash -LiteralPath $GeneratorAttemptPath -Algorithm SHA256).Hash
```

Expected: `generator-attempt/` exists exactly once, `attempt.json` is flushed and read-only, and its RED/GREEN/fixture seals equal the current immutable records. From this point, any failure preserves the worktree and SaveDir and permanently forbids a second generator.

- [ ] **Step 6: Launch the repaired generator exactly once through the private-desktop wrapper**

Continue in the same session. Dot-source the already-sealed wrapper; do not run its selftest or the old version probe:

```powershell
. $HeadlessWrapper
if (-not (Get-Command Invoke-PrivateDesktopProcess -CommandType Function -ErrorAction SilentlyContinue)) {
    throw 'NEEDS_CONTEXT: selected wrapper did not define Invoke-PrivateDesktopProcess.'
}
# TASK1_V3_RUNTIME_HELPERS_CORE_BEGIN
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
        [bool]$Result.host_termination_required -or -not [bool]$Result.job_drained -or
        -not [bool]$Result.cleanup_complete -or [int64]$Result.job_active_processes_final -ne 0 -or
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
function Copy-CreateOnlyFile([string]$Source, [string]$Destination) {
    $InputStream = New-Object IO.FileStream -ArgumentList @(
        $Source, [IO.FileMode]::Open, [IO.FileAccess]::Read, [IO.FileShare]::Read
    )
    try {
        $OutputStream = New-Object IO.FileStream -ArgumentList @(
            $Destination, [IO.FileMode]::CreateNew, [IO.FileAccess]::Write, [IO.FileShare]::None,
            81920, [IO.FileOptions]::WriteThrough
        )
        try {
            $InputStream.CopyTo($OutputStream)
            $OutputStream.Flush($true)
        } finally {
            $OutputStream.Dispose()
        }
    } finally {
        $InputStream.Dispose()
    }
}
function Assert-ByteEqual([string]$Left, [string]$Right, [string]$Context) {
    $LeftBytes = [IO.File]::ReadAllBytes($Left)
    $RightBytes = [IO.File]::ReadAllBytes($Right)
    if ($LeftBytes.Length -ne $RightBytes.Length -or
        [Convert]::ToBase64String($LeftBytes) -cne [Convert]::ToBase64String($RightBytes)) {
        throw ('NEEDS_CONTEXT: byte comparison failed ' + $Context)
    }
}
function Get-V3BoundedAppDataBackupSnapshot([string]$Path,[string]$Context) {
    $EntryLimit = 4096
    $CatalogByteLimit = 4194304
    $TimeoutMilliseconds = 10000
    $CanonicalPath = Get-CanonicalPath $Path
    $RenPyAppDataRoot = Get-CanonicalPath (Join-Path $AppDataRoamingRoot 'RenPy')
    if ($Path -cne $CanonicalPath -or -not [IO.Path]::IsPathRooted($CanonicalPath) -or
        (Get-CanonicalPath (Split-Path $CanonicalPath -Parent)) -cne $AppDataBackupRoot -or
        ($CanonicalPath -cne $GeneratorAppDataBackupPath -and
            $CanonicalPath -cne $ObserverAppDataBackupPath)) {
        throw ('NEEDS_CONTEXT: AppData observation path is outside the exact two-path allowlist ' + $Context)
    }
    foreach ($ChainPath in @($AppDataRoamingRoot,$RenPyAppDataRoot,$AppDataBackupRoot)) {
        if (Test-Path -LiteralPath $ChainPath) {
            $ChainItem = Get-Item -LiteralPath $ChainPath -Force -ErrorAction Stop
            if (-not $ChainItem.PSIsContainer -or
                ($ChainItem.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
                throw ('NEEDS_CONTEXT: AppData observation path chain is not an ordinary directory ' + $Context)
            }
        }
    }
    $StartedUtc = [DateTime]::UtcNow
    $DeadlineUtc = $StartedUtc.AddMilliseconds($TimeoutMilliseconds)
    $Exists = Test-Path -LiteralPath $CanonicalPath
    $DirectoryCount = [int64]0
    $FileCount = [int64]0
    $TotalFileBytes = [int64]0
    $CatalogByPath = New-Object 'System.Collections.Generic.Dictionary[string,object]' ([StringComparer]::Ordinal)
    $CaseFoldPaths = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
    if ($Exists) {
        $RootItem = Get-Item -LiteralPath $CanonicalPath -Force -ErrorAction Stop
        if (-not $RootItem.PSIsContainer -or
            ($RootItem.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
            throw ('NEEDS_CONTEXT: AppData observation target is not an ordinary directory ' + $Context)
        }
        [void]$CaseFoldPaths.Add('.')
        $CatalogByPath.Add('.', [pscustomobject][ordered]@{
            kind='directory'; relative_path='.'; attributes=[int64]$RootItem.Attributes
            last_write_utc_ticks=[int64]$RootItem.LastWriteTimeUtc.Ticks; bytes=$null
        })
        $Pending = New-Object 'System.Collections.Generic.Stack[string]'
        $Pending.Push($CanonicalPath)
        $DescendantCount = 0
        while ($Pending.Count -gt 0) {
            if ([DateTime]::UtcNow -gt $DeadlineUtc) {
                throw ('NEEDS_CONTEXT: AppData observation exceeded 10000 ms ' + $Context)
            }
            $Current = $Pending.Pop()
            $ChildPaths = [string[]]@(
                Get-ChildItem -LiteralPath $Current -Force -ErrorAction Stop |
                    ForEach-Object { Get-CanonicalPath $_.FullName }
            )
            if ($DescendantCount + $ChildPaths.Count -gt $EntryLimit) {
                throw ('NEEDS_CONTEXT: AppData observation exceeded 4096 entries ' + $Context)
            }
            [Array]::Sort($ChildPaths,[StringComparer]::Ordinal)
            foreach ($ChildPath in $ChildPaths) {
                if ([DateTime]::UtcNow -gt $DeadlineUtc -or
                    -not (Test-SameOrChildPath $ChildPath $CanonicalPath)) {
                    throw ('NEEDS_CONTEXT: AppData observation deadline/path relation failed ' + $Context)
                }
                $DescendantCount++
                $Child = Get-Item -LiteralPath $ChildPath -Force -ErrorAction Stop
                if (($Child.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
                    throw ('NEEDS_CONTEXT: AppData observation refuses a reparse point ' + $Context + ': ' + $ChildPath)
                }
                $Relative = $ChildPath.Substring($CanonicalPath.Length).TrimStart('\').Replace('\','/')
                if ([string]::IsNullOrEmpty($Relative) -or -not $CaseFoldPaths.Add($Relative)) {
                    throw ('NEEDS_CONTEXT: AppData observation has an empty/case-fold-colliding path ' + $Context)
                }
                if ($Child.PSIsContainer) {
                    $DirectoryCount++
                    $Pending.Push($ChildPath)
                    $Row = [pscustomobject][ordered]@{
                        kind='directory'; relative_path=$Relative; attributes=[int64]$Child.Attributes
                        last_write_utc_ticks=[int64]$Child.LastWriteTimeUtc.Ticks; bytes=$null
                    }
                } else {
                    $FileLength = [int64]$Child.Length
                    if ($FileLength -lt 0 -or $TotalFileBytes -gt ([int64]::MaxValue - $FileLength)) {
                        throw ('NEEDS_CONTEXT: AppData observation file-byte total overflowed ' + $Context)
                    }
                    $FileCount++
                    $TotalFileBytes += $FileLength
                    $Row = [pscustomobject][ordered]@{
                        kind='file'; relative_path=$Relative; attributes=[int64]$Child.Attributes
                        last_write_utc_ticks=[int64]$Child.LastWriteTimeUtc.Ticks; bytes=$FileLength
                    }
                }
                $CatalogByPath.Add($Relative,$Row)
            }
        }
    }
    $CatalogKeys = [string[]]$CatalogByPath.Keys
    [Array]::Sort($CatalogKeys,[StringComparer]::Ordinal)
    $CatalogRows = New-Object 'System.Collections.Generic.List[object]'
    foreach ($CatalogKey in $CatalogKeys) { [void]$CatalogRows.Add($CatalogByPath[$CatalogKey]) }
    $CatalogText = (ConvertTo-Json -InputObject ([object[]]$CatalogRows.ToArray()) -Depth 4 -Compress) + "`n"
    $CatalogBytes = $StrictUtf8.GetBytes($CatalogText)
    if ($CatalogBytes.Length -gt $CatalogByteLimit -or [DateTime]::UtcNow -gt $DeadlineUtc) {
        throw ('NEEDS_CONTEXT: AppData observation exceeded its byte/time bound ' + $Context)
    }
    return [pscustomobject][ordered]@{
        schema_version=1; path=$CanonicalPath; exists=[bool]$Exists
        directory_count=$DirectoryCount; file_count=$FileCount; total_file_bytes=$TotalFileBytes
        catalog_bytes=[int64]$CatalogBytes.Length; catalog_sha256=(Get-V3BytesSha256 $CatalogBytes)
        entry_limit=$EntryLimit; catalog_byte_limit=$CatalogByteLimit
        timeout_milliseconds=$TimeoutMilliseconds
        captured_utc=[DateTime]::UtcNow.ToString('o',[Globalization.CultureInfo]::InvariantCulture)
    }
}
function Assert-V3AppDataBackupSnapshot([object]$Snapshot,[string]$ExpectedPath,[string]$Context) {
    Assert-ExactProperties $Snapshot @(
        'schema_version','path','exists','directory_count','file_count','total_file_bytes',
        'catalog_bytes','catalog_sha256','entry_limit','catalog_byte_limit','timeout_milliseconds','captured_utc'
    ) ($Context + ' AppData snapshot')
    if ($Snapshot.schema_version -isnot [int] -or $Snapshot.schema_version -ne 1 -or
        $Snapshot.path -isnot [string] -or [string]$Snapshot.path -cne (Get-CanonicalPath $ExpectedPath) -or
        [string]$Snapshot.path -cne (Get-CanonicalPath ([string]$Snapshot.path)) -or
        $Snapshot.exists -isnot [bool] -or
        -not (Test-RecoveryIntegral $Snapshot.directory_count) -or [int64]$Snapshot.directory_count -lt 0 -or
        -not (Test-RecoveryIntegral $Snapshot.file_count) -or [int64]$Snapshot.file_count -lt 0 -or
        -not (Test-RecoveryIntegral $Snapshot.total_file_bytes) -or [int64]$Snapshot.total_file_bytes -lt 0 -or
        -not (Test-RecoveryIntegral $Snapshot.catalog_bytes) -or [int64]$Snapshot.catalog_bytes -lt 3 -or
        [int64]$Snapshot.catalog_bytes -gt 4194304 -or
        $Snapshot.catalog_sha256 -isnot [string] -or $Snapshot.catalog_sha256 -cnotmatch '^[0-9A-F]{64}$' -or
        $Snapshot.entry_limit -isnot [int] -or $Snapshot.entry_limit -ne 4096 -or
        $Snapshot.catalog_byte_limit -isnot [int] -or $Snapshot.catalog_byte_limit -ne 4194304 -or
        $Snapshot.timeout_milliseconds -isnot [int] -or $Snapshot.timeout_milliseconds -ne 10000 -or
        -not (Test-RoundtripUtc $Snapshot.captured_utc) -or
        (-not [bool]$Snapshot.exists -and
            ([int64]$Snapshot.directory_count -ne 0 -or [int64]$Snapshot.file_count -ne 0 -or
                [int64]$Snapshot.total_file_bytes -ne 0))) {
        throw ('NEEDS_CONTEXT: AppData snapshot shape/value failed ' + $Context)
    }
}
function New-V3SealedJsonHandoff([object]$Payload,[string]$Context) {
    $Text = (ConvertTo-Json -InputObject $Payload -Depth 16 -Compress) + "`n"
    $Bytes = $StrictUtf8.GetBytes($Text)
    if ($Bytes.Length -eq 0 -or $Bytes.Length -gt 65536 -or $Text.Contains("`r")) {
        throw ('NEEDS_CONTEXT: sealed handoff exceeded its canonical byte bound ' + $Context)
    }
    return [pscustomobject][ordered]@{
        base64=[Convert]::ToBase64String($Bytes); sha256=(Get-V3BytesSha256 $Bytes)
    }
}
function Read-V3SealedJsonHandoff([string]$Base64,[string]$Sha256,[string]$Context) {
    if ($Sha256 -cnotmatch '^[0-9A-F]{64}$' -or [string]::IsNullOrEmpty($Base64) -or
        $Base64.Length -gt 131072 -or ($Base64.Length % 4) -ne 0 -or
        $Base64 -cnotmatch '^[A-Za-z0-9+/]+={0,2}$') {
        throw ('NEEDS_CONTEXT: sealed handoff arguments are malformed ' + $Context)
    }
    try { $Bytes = [Convert]::FromBase64String($Base64) } catch {
        throw ('NEEDS_CONTEXT: sealed handoff base64 is invalid ' + $Context)
    }
    if ($Bytes.Length -eq 0 -or $Bytes.Length -gt 65536 -or
        (Get-V3BytesSha256 $Bytes) -cne $Sha256) {
        throw ('NEEDS_CONTEXT: sealed handoff bytes/hash failed ' + $Context)
    }
    $Text = $StrictUtf8.GetString($Bytes)
    if ($Text.Contains("`r") -or -not $Text.EndsWith("`n",[StringComparison]::Ordinal)) {
        throw ('NEEDS_CONTEXT: sealed handoff is not canonical LF JSON ' + $Context)
    }
    [void](Get-RecoveryRawJsonObjectKeys $Text $Context)
    return ($Text | ConvertFrom-Json -ErrorAction Stop)
}
function Assert-V3GeneratorAppDataObservation([object]$Observation,[string]$Context) {
    Assert-ExactProperties $Observation @(
        'schema_version','backup_root','generator_path','generator_before','generator_after',
        'read_only','authority','cleanup_performed'
    ) ($Context + ' generator AppData observation')
    if ($Observation.schema_version -isnot [int] -or $Observation.schema_version -ne 1 -or
        $Observation.backup_root -isnot [string] -or
        [string]$Observation.backup_root -cne $AppDataBackupRoot -or
        $Observation.generator_path -isnot [string] -or
        [string]$Observation.generator_path -cne $GeneratorAppDataBackupPath -or
        $Observation.read_only -isnot [bool] -or -not [bool]$Observation.read_only -or
        $Observation.authority -isnot [bool] -or [bool]$Observation.authority -or
        $Observation.cleanup_performed -isnot [bool] -or [bool]$Observation.cleanup_performed) {
        throw ('NEEDS_CONTEXT: generator AppData observation scalar contract failed ' + $Context)
    }
    Assert-V3AppDataBackupSnapshot $Observation.generator_before $GeneratorAppDataBackupPath ($Context + ' generator before')
    Assert-V3AppDataBackupSnapshot $Observation.generator_after $GeneratorAppDataBackupPath ($Context + ' generator after')
}
function Assert-V3AppDataObservation([object]$Observation,[string]$ExpectedGeneratorHandoffSha256,[string]$Context) {
    Assert-ExactProperties $Observation @(
        'schema_version','backup_root','generator_path','generator_before','generator_after',
        'generator_handoff_sha256','observer_path','observer_before','observer_after',
        'read_only','authority','cleanup_performed'
    ) ($Context + ' complete AppData observation')
    if ($Observation.schema_version -isnot [int] -or $Observation.schema_version -ne 1 -or
        $Observation.backup_root -isnot [string] -or
        [string]$Observation.backup_root -cne $AppDataBackupRoot -or
        $Observation.generator_path -isnot [string] -or
        [string]$Observation.generator_path -cne $GeneratorAppDataBackupPath -or
        $Observation.generator_handoff_sha256 -isnot [string] -or
        [string]$Observation.generator_handoff_sha256 -cne $ExpectedGeneratorHandoffSha256 -or
        $Observation.observer_path -isnot [string] -or
        [string]$Observation.observer_path -cne $ObserverAppDataBackupPath -or
        $Observation.read_only -isnot [bool] -or -not [bool]$Observation.read_only -or
        $Observation.authority -isnot [bool] -or [bool]$Observation.authority -or
        $Observation.cleanup_performed -isnot [bool] -or [bool]$Observation.cleanup_performed) {
        throw ('NEEDS_CONTEXT: complete AppData observation scalar contract failed ' + $Context)
    }
    Assert-V3AppDataBackupSnapshot $Observation.generator_before $GeneratorAppDataBackupPath ($Context + ' generator before')
    Assert-V3AppDataBackupSnapshot $Observation.generator_after $GeneratorAppDataBackupPath ($Context + ' generator after')
    Assert-V3AppDataBackupSnapshot $Observation.observer_before $ObserverAppDataBackupPath ($Context + ' observer before')
    Assert-V3AppDataBackupSnapshot $Observation.observer_after $ObserverAppDataBackupPath ($Context + ' observer after')
}
# TASK1_V3_RUNTIME_HELPERS_CORE_END

$PersistedGeneratorAttempt = Read-RecoveryStrictJson $GeneratorAttemptPath 'generator attempt before launch'
Assert-ExactProperties $PersistedGeneratorAttempt $GeneratorAttemptProperties 'generator attempt before launch'
if (-not (Get-Item -LiteralPath $GeneratorAttemptPath).IsReadOnly -or
    (Get-FileHash -LiteralPath $GeneratorAttemptPath -Algorithm SHA256).Hash -cne $GeneratorAttemptSha256 -or
    (Get-FileHash -LiteralPath $RedRecordPath -Algorithm SHA256).Hash -cne [string]$PersistedGeneratorAttempt.red_record_sha256 -or
    (Get-FileHash -LiteralPath $GreenRecordPath -Algorithm SHA256).Hash -cne [string]$PersistedGeneratorAttempt.green_record_sha256 -or
    (Get-FileHash -LiteralPath $GeneratorFixturePath -Algorithm SHA256).Hash -cne [string]$PersistedGeneratorAttempt.fixture_sha256 -or
    (Test-Path -LiteralPath $GeneratorSaveDir) -or (Test-Path -LiteralPath $GeneratorLocalSaves) -or
    (Test-Path -LiteralPath $GeneratorProcessEvidence) -or (Test-Path -LiteralPath $GeneratorStatePath)) {
    throw 'NEEDS_CONTEXT: generator launch preconditions drifted after ledger creation.'
}
Assert-RecoveryAuthorityUnchanged 'before the sole generator launch'
$LegacyMarker = 'terminal-collapse-legacy-v3:' + $P3 + ':supply-vanguard-remember:final-menu'
$GeneratorEnvironment = New-PrivateRenPyEnvironment @{
    'TC_GENERATOR_RESULT' = Get-CanonicalPath $GeneratorStatePath
    'TC_EXPECTED_MARKER' = $LegacyMarker
    'TC_EXPECTED_BASELINE_COMMIT' = $P3
    'TC_EXPECTED_GAME_TREE' = $GameTree
    'TC_EXPECTED_SAVEDIR' = Get-CanonicalPath $GeneratorSaveDir
    'TC_EXPECTED_FIXTURE_SHA256' = $GreenFixtureSha256
}

# Sole generator invocation. A thrown exception or any non-PASS result consumes
# the ledger permanently and stops Task 1 without observer, mother, or cleanup.
$GeneratorAppDataBefore = Get-V3BoundedAppDataBackupSnapshot `
    $GeneratorAppDataBackupPath 'immediately before sole generator invocation'
$GeneratorRun = Invoke-PrivateDesktopProcess `
    -FilePath $RenPyExe `
    -ArgumentList @($GeneratorRoot, 'test', 'terminal_collapse_legacy_generator', '--savedir', $GeneratorSaveDir) `
    -WorkingDirectory $GeneratorRoot `
    -EnvironmentOverrides $GeneratorEnvironment `
    -TimeoutSeconds 180 `
    -EvidenceDirectory $GeneratorProcessEvidence `
    -RunnerSource $RunnerSource
Assert-PrivateDesktopCompletion $GeneratorRun 0 'recovery generator'
$GeneratorAppDataAfter = Get-V3BoundedAppDataBackupSnapshot `
    $GeneratorAppDataBackupPath 'immediately after sole generator invocation'
```

Expected: this fence contains the only generator invocation in the entire recovery. It returns `COMPLETED`, helper/root exit 0, no timeout, no host termination, zero windows, drained Job, zero active processes, and complete cleanup. Any other result is final failure evidence.

- [ ] **Step 7: Validate test_report/engine_boot_log, exact three-save inventory, and freeze the 42-field generator completion**

```powershell
$GeneratorRequestPath = Join-Path $GeneratorProcessEvidence 'request.json'
$GeneratorStdoutPath = Join-Path $GeneratorProcessEvidence 'stdout.txt'
$GeneratorStderrPath = Join-Path $GeneratorProcessEvidence 'stderr.txt'
$GeneratorResultPath = Join-Path $GeneratorProcessEvidence 'result.json'
foreach ($HelperLeaf in @($GeneratorRequestPath,$GeneratorStdoutPath,$GeneratorStderrPath,$GeneratorResultPath)) {
    if (-not (Test-Path -LiteralPath $HelperLeaf -PathType Leaf)) {
        throw ('NEEDS_CONTEXT: generator helper evidence is incomplete: ' + $HelperLeaf)
    }
}
$PersistedGeneratorResult = Read-HelperJson $GeneratorResultPath 'generator helper result'
Assert-ExactProperties $PersistedGeneratorResult @(
    'schema_version','classification','detail','started','root_pid','root_exit_code','timed_out',
    'job_drained','desktop_name','process_ids','new_process_ids','active_snapshot_process_ids',
    'job_total_processes','observed_distinct_process_id_count','process_id_accounting_kind',
    'private_desktop_initially_empty','monitor_armed_before_create','monitor_armed_before_resume',
    'monitor_armed_utc','process_created_utc','resumed_utc','root_assigned_to_job_before_resume',
    'job_breakaway_forbidden','job_active_processes_final','monitor_completed_after_job_drain',
    'cleanup_complete','cleanup_errors','visible_windows','started_utc','finished_utc',
    'elapsed_milliseconds','stdout_path','stderr_path','process_diagnostic_errors',
    'host_termination_required','helper_exit_code','job_kill_on_close_verified','job_handle_non_inheritable'
) 'generator helper result schema v2'
Assert-PrivateDesktopCompletion $PersistedGeneratorResult 0 'persisted recovery generator'
if ((Get-CanonicalPath ([string]$PersistedGeneratorResult.stdout_path)) -cne (Get-CanonicalPath $GeneratorStdoutPath) -or
    (Get-CanonicalPath ([string]$PersistedGeneratorResult.stderr_path)) -cne (Get-CanonicalPath $GeneratorStderrPath)) {
    throw 'NEEDS_CONTEXT: generator helper result points outside its declared evidence root.'
}
$GeneratorRequest = Read-HelperJson $GeneratorRequestPath 'generator helper request'
Assert-ExactProperties $GeneratorRequest @(
    'schema_version','executable','arguments','working_directory','environment_overrides',
    'timeout_milliseconds','stdout_path','stderr_path','result_path'
) 'generator helper request'
$GeneratorRequestExpected = [pscustomobject][ordered]@{
    executable=(Get-CanonicalPath $RenPyExe)
    arguments=[object[]]@((Get-CanonicalPath $GeneratorRoot),'test','terminal_collapse_legacy_generator','--savedir',(Get-CanonicalPath $GeneratorSaveDir))
    working_directory=(Get-CanonicalPath $GeneratorRoot)
    environment_names=[object[]]$GeneratorEnvironmentNames
    environment_values=[object[]]@(
        '1',$null,'sw','dummy','dummy',$P3,$GreenFixtureSha256,$GameTree,$LegacyMarker,
        (Get-CanonicalPath $GeneratorSaveDir),(Get-CanonicalPath $GeneratorStatePath)
    )
    timeout_milliseconds=[int64]180000; stdout_path=(Get-CanonicalPath $GeneratorStdoutPath)
    stderr_path=(Get-CanonicalPath $GeneratorStderrPath); result_path=(Get-CanonicalPath $GeneratorResultPath)
}
if ((Test-V3RequestContract 'generator' $GeneratorRequest $GeneratorRequestExpected) -cne 'ACCEPT') {
    throw 'NEEDS_CONTEXT: helper request did not bind the attempt fixture and isolated generator launch.'
}

if (-not (Test-Path -LiteralPath $GeneratorStatePath -PathType Leaf)) {
    throw 'NEEDS_CONTEXT: generator state result is missing.'
}
$GeneratorState = Read-RecoveryStrictJson $GeneratorStatePath 'generator state'
if ((Test-V3GeneratorStateContract $GeneratorState (Get-CanonicalPath $GeneratorSaveDir) `
        $LegacyMarker $P3 $GameTree) -cne 'ACCEPT') {
    throw ('NEEDS_CONTEXT: generator state assertions failed: ' + [string]$GeneratorState.reason)
}
(Get-Item -LiteralPath $GeneratorStatePath).IsReadOnly = $true
if (-not (Get-Item -LiteralPath $GeneratorStatePath).IsReadOnly) { throw 'Could not freeze generator state.' }

$GeneratorLogPath = Join-Path $GeneratorRoot 'log.txt'
if (-not (Test-Path -LiteralPath $GeneratorLogPath -PathType Leaf)) {
    throw 'NEEDS_CONTEXT: generator engine_boot_log is missing.'
}

if (-not (Test-Path -LiteralPath $GeneratorSaveDir -PathType Container) -or
    -not (Test-Path -LiteralPath $GeneratorLocalSaves -PathType Container)) {
    throw 'NEEDS_CONTEXT: generator did not create both expected MultiLocation roots.'
}
$GeneratorExternalTree = Get-RecoveryNonFollowingTree $GeneratorSaveDir $false 'generator external targets'
$GeneratorLocalTree = Get-RecoveryNonFollowingTree $GeneratorLocalSaves $false 'generator local targets'
$AllTargetPaths = [string[]]@(
    @($GeneratorExternalTree.files | Where-Object { (Split-Path $_ -Leaf) -like '1-1-*.save' }) +
    @($GeneratorLocalTree.files | Where-Object { (Split-Path $_ -Leaf) -like '1-1-*.save' })
)
[Array]::Sort($AllTargetPaths,[StringComparer]::Ordinal)
$AllTargetCandidates = @($AllTargetPaths | ForEach-Object { Get-Item -LiteralPath $_ -Force -ErrorAction Stop })
$ExternalRootTargets = @($AllTargetCandidates | Where-Object {
    (Get-CanonicalPath $_.DirectoryName) -ceq (Get-CanonicalPath $GeneratorSaveDir)
})
$ExternalSyncTargets = @($AllTargetCandidates | Where-Object {
    (Get-CanonicalPath $_.DirectoryName) -ceq (Get-CanonicalPath (Join-Path $GeneratorSaveDir 'sync'))
})
$LocalRootTargets = @($AllTargetCandidates | Where-Object {
    (Get-CanonicalPath $_.DirectoryName) -ceq (Get-CanonicalPath $GeneratorLocalSaves)
})
if ($AllTargetCandidates.Count -ne 3 -or $ExternalRootTargets.Count -ne 1 -or
    $ExternalSyncTargets.Count -ne 1 -or $LocalRootTargets.Count -ne 1) {
    throw 'NEEDS_CONTEXT: recursive generator target cardinality is not root/sync/local = 1/1/1.'
}
$ExternalSave = $ExternalRootTargets[0]
$SyncSave = $ExternalSyncTargets[0]
$LocalSave = $LocalRootTargets[0]
$TargetFiles = @($ExternalSave,$SyncSave,$LocalSave)
$TargetNames = @($TargetFiles | ForEach-Object { $_.Name } | Select-Object -Unique)
$TargetLengths = @($TargetFiles | ForEach-Object { [int64]$_.Length } | Select-Object -Unique)
$TargetHashes = @($TargetFiles | ForEach-Object { (Get-FileHash -LiteralPath $_.FullName -Algorithm SHA256).Hash } | Select-Object -Unique)
if ($TargetNames.Count -ne 1 -or $TargetLengths.Count -ne 1 -or $TargetHashes.Count -ne 1) {
    throw 'NEEDS_CONTEXT: three generator targets differ by basename, bytes, or SHA-256.'
}
Assert-ByteEqual $ExternalSave.FullName $SyncSave.FullName 'generator external-root/external-sync targets'
Assert-ByteEqual $ExternalSave.FullName $LocalSave.FullName 'generator external-root/local targets'
$ExternalHash = [string]$TargetHashes[0]
foreach ($TargetFile in $TargetFiles) {
    (Get-Item -LiteralPath $TargetFile.FullName).IsReadOnly = $true
    if (-not (Get-Item -LiteralPath $TargetFile.FullName).IsReadOnly) {
        throw ('Could not freeze generator target save: ' + $TargetFile.FullName)
    }
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
foreach ($Metadata in @(
    (Read-RenPySaveJson $ExternalSave.FullName),
    (Read-RenPySaveJson $SyncSave.FullName),
    (Read-RenPySaveJson $LocalSave.FullName)
)) {
    if ($Metadata.tc_legacy_schema -isnot [int] -or $Metadata.tc_legacy_schema -ne 1 -or
        $Metadata.tc_legacy_marker -isnot [string] -or $Metadata.tc_legacy_marker -cne $LegacyMarker -or
        $Metadata.tc_baseline_commit -isnot [string] -or $Metadata.tc_baseline_commit -cne $P3 -or
        $Metadata.tc_game_tree -isnot [string] -or $Metadata.tc_game_tree -cne $GameTree -or
        $Metadata.tc_menu_file -isnot [string] -or $Metadata.tc_menu_file -cne 'game/chapter5.rpy' -or
        $Metadata.tc_menu_line -isnot [int] -or $Metadata.tc_menu_line -ne 2807 -or
        $Metadata.tc_state.intrigue -isnot [int] -or $Metadata.tc_state.intrigue -ne 55 -or
        $Metadata.tc_state.power -isnot [int] -or $Metadata.tc_state.power -ne 60 -or
        $Metadata.tc_state.iron_prepared -isnot [bool] -or -not $Metadata.tc_state.iron_prepared -or
        (@($Metadata.tc_choice_path) -join "`n") -cne (@(
            '截断补给线——让他们饿三天再打','亲自率领前锋出击','记住这一切，继续前进'
        ) -join "`n")) {
        throw 'NEEDS_CONTEXT: generator save metadata does not bind the approved pre-change state.'
    }
}

Copy-CreateOnlyFile $GeneratorFixturePath $GeneratorFixtureEvidence
Copy-CreateOnlyFile $GeneratorLogPath $GeneratorLogEvidence
Assert-ByteEqual $GeneratorFixturePath $GeneratorFixtureEvidence 'generator fixture durable copy'
Assert-ByteEqual $GeneratorLogPath $GeneratorLogEvidence 'generator log durable copy'
foreach ($FrozenCopy in @($GeneratorFixtureEvidence,$GeneratorLogEvidence)) {
    (Get-Item -LiteralPath $FrozenCopy).IsReadOnly = $true
    if (-not (Get-Item -LiteralPath $FrozenCopy).IsReadOnly) { throw ('Could not freeze durable generator evidence: ' + $FrozenCopy) }
}
$GeneratorFixtureEvidenceHash = (Get-FileHash -LiteralPath $GeneratorFixtureEvidence -Algorithm SHA256).Hash
$GeneratorLogHash = (Get-FileHash -LiteralPath $GeneratorLogPath -Algorithm SHA256).Hash
$GeneratorLogEvidenceHash = (Get-FileHash -LiteralPath $GeneratorLogEvidence -Algorithm SHA256).Hash
if ($GeneratorFixtureEvidenceHash -cne $GreenFixtureSha256 -or
    $GeneratorLogEvidenceHash -cne $GeneratorLogHash) {
    throw 'NEEDS_CONTEXT: durable generator fixture/log seals differ from their runtime sources.'
}
foreach ($FrozenHelperLeaf in @(
    $GeneratorRequestPath,$GeneratorStdoutPath,$GeneratorStderrPath,$GeneratorResultPath,$GeneratorStatePath
)) {
    (Get-Item -LiteralPath $FrozenHelperLeaf).IsReadOnly = $true
    if (-not (Get-Item -LiteralPath $FrozenHelperLeaf).IsReadOnly) {
        throw ('Could not freeze generator process/state evidence: ' + $FrozenHelperLeaf)
    }
}
# TASK1_V3_RUNTIME_HELPERS_INVENTORY_BEGIN
function New-SaveInventory([string]$ExternalRoot,[string]$LocalRoot,[int]$ExpectedTargetCount) {
    $DirectoryRows = New-Object 'System.Collections.Generic.List[object]'
    $FileRows = New-Object 'System.Collections.Generic.List[object]'
    foreach ($RootSpec in @(
        [pscustomobject]@{ role='external'; path=(Get-CanonicalPath $ExternalRoot) },
        [pscustomobject]@{ role='local'; path=(Get-CanonicalPath $LocalRoot) }
    )) {
        $PhysicalTree = Get-RecoveryNonFollowingTree $RootSpec.path $true `
            ('save inventory ' + [string]$RootSpec.role)
        if (-not $PhysicalTree.exists) { continue }
        [void]$DirectoryRows.Add([ordered]@{ root_role=$RootSpec.role; relative_path='.' })
        foreach ($DirectoryPath in $PhysicalTree.directories) {
            $Relative = $DirectoryPath.Substring($RootSpec.path.Length).TrimStart('\').Replace('\','/')
            [void]$DirectoryRows.Add([ordered]@{ root_role=$RootSpec.role; relative_path=$Relative })
        }
        foreach ($FilePath in $PhysicalTree.files) {
            $File = Get-Item -LiteralPath $FilePath -Force -ErrorAction Stop
            $Relative = $FilePath.Substring($RootSpec.path.Length).TrimStart('\').Replace('\','/')
            $Kind = if ($File.Name -like '1-1-*.save') {
                'target'
            } elseif ($File.Name -like 'auto-*.save') {
                'autosave'
            } elseif ($File.Name -ceq 'persistent') {
                'persistent'
            } else {
                throw ('NEEDS_CONTEXT: unexpected generator save inventory file ' + $File.FullName)
            }
            $Seal = New-FileSeal $File.FullName
            [void]$FileRows.Add([ordered]@{
                root_role=$RootSpec.role; relative_path=$Relative; kind=$Kind;
                bytes=[int64]$Seal.bytes; sha256=[string]$Seal.sha256
            })
        }
    }
    $SortedDirectories = [object[]]$DirectoryRows.ToArray()
    $SortedFiles = [object[]]$FileRows.ToArray()
    $CompoundSeen = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
    foreach ($Row in $SortedFiles) {
        Assert-ExactProperties ([pscustomobject]$Row) @('root_role','relative_path','kind','bytes','sha256') 'save inventory file'
        if (-not $CompoundSeen.Add([string]$Row.root_role + [char]9 + [string]$Row.relative_path)) {
            throw 'NEEDS_CONTEXT: duplicate save inventory compound key.'
        }
    }
    if (@($SortedFiles | Where-Object { $_.kind -ceq 'target' }).Count -ne $ExpectedTargetCount) {
        throw 'NEEDS_CONTEXT: save inventory target count failed.'
    }
    return [ordered]@{
        roots = [ordered]@{ external_savedir=(Get-CanonicalPath $ExternalRoot); local_savedir=(Get-CanonicalPath $LocalRoot) }
        directories = $SortedDirectories
        files = $SortedFiles
        target_count = $ExpectedTargetCount
    }
}
function Assert-SaveInventoryRecord([object]$Inventory,[int]$ExpectedTargetCount,[string]$Context) {
    Assert-ExactProperties $Inventory @('roots','directories','files','target_count') ($Context + ' save_inventory')
    Assert-ExactProperties $Inventory.roots @('external_savedir','local_savedir') ($Context + ' roots')
    if ($Inventory.roots.external_savedir -isnot [string] -or
        (Get-CanonicalPath ([string]$Inventory.roots.external_savedir)) -cne [string]$Inventory.roots.external_savedir -or
        $Inventory.roots.local_savedir -isnot [string] -or
        (Get-CanonicalPath ([string]$Inventory.roots.local_savedir)) -cne [string]$Inventory.roots.local_savedir -or
        $Inventory.target_count -isnot [int] -or $Inventory.target_count -ne $ExpectedTargetCount) {
        throw ('NEEDS_CONTEXT: ' + $Context + ' target_count failed.')
    }
    $PreviousDirectoryKey = $null
    foreach ($Directory in @($Inventory.directories)) {
        Assert-ExactProperties $Directory @('root_role','relative_path') ($Context + ' directory')
        $DirectoryKey = [string]$Directory.root_role + [char]9 + [string]$Directory.relative_path
        if ($Directory.root_role -isnot [string] -or
            ([string]$Directory.root_role -cne 'external' -and [string]$Directory.root_role -cne 'local') -or
            $Directory.relative_path -isnot [string] -or
            [IO.Path]::IsPathRooted([string]$Directory.relative_path) -or
            [string]$Directory.relative_path -match '(^|[\\/])\.\.([\\/]|$)' -or
            ($null -ne $PreviousDirectoryKey -and
                [StringComparer]::Ordinal.Compare($PreviousDirectoryKey,$DirectoryKey) -ge 0)) {
            throw ('NEEDS_CONTEXT: ' + $Context + ' directory order/type failed.')
        }
        $PreviousDirectoryKey = $DirectoryKey
    }
    $PreviousFileKey = $null
    foreach ($File in @($Inventory.files)) {
        Assert-ExactProperties $File @('root_role','relative_path','kind','bytes','sha256') ($Context + ' file')
        $FileKey = [string]$File.root_role + [char]9 + [string]$File.relative_path
        if ($File.root_role -isnot [string] -or
            ([string]$File.root_role -cne 'external' -and [string]$File.root_role -cne 'local') -or
            $File.relative_path -isnot [string] -or
            [IO.Path]::IsPathRooted([string]$File.relative_path) -or
            [string]$File.relative_path -match '(^|[\\/])\.\.([\\/]|$)' -or
            $File.kind -isnot [string] -or
            [string]$File.kind -notin @('target','autosave','persistent') -or
            -not (Test-RecoveryIntegral $File.bytes) -or [int64]$File.bytes -lt 0 -or
            $File.sha256 -isnot [string] -or $File.sha256 -cnotmatch '^[0-9A-F]{64}$' -or
            ($null -ne $PreviousFileKey -and
                [StringComparer]::Ordinal.Compare($PreviousFileKey,$FileKey) -ge 0)) {
            throw ('NEEDS_CONTEXT: ' + $Context + ' file order/type failed.')
        }
        $PreviousFileKey = $FileKey
    }
    if (@($Inventory.files | Where-Object { $_.kind -ceq 'target' }).Count -ne $ExpectedTargetCount) {
        throw ('NEEDS_CONTEXT: ' + $Context + ' nested target count failed.')
    }
}
function Assert-SaveInventoryTargets(
    [object]$Inventory,[string[]]$ExpectedPaths,[int64]$ExpectedBytes,
    [string]$ExpectedSha256,[bool]$RequirePhysical,[string]$Context
) {
    $ActualPaths = New-Object 'System.Collections.Generic.List[string]'
    foreach ($Target in @($Inventory.files | Where-Object { $_.kind -ceq 'target' })) {
        $Root = if ([string]$Target.root_role -ceq 'external') {
            [string]$Inventory.roots.external_savedir
        } elseif ([string]$Target.root_role -ceq 'local') {
            [string]$Inventory.roots.local_savedir
        } else {
            throw ('NEEDS_CONTEXT: ' + $Context + ' target has an unknown root role.')
        }
        $TargetPath = Get-CanonicalPath (Join-Path $Root ([string]$Target.relative_path))
        if (-not (Test-SameOrChildPath $TargetPath $Root) -or
            -not (Test-RecoveryIntegral $Target.bytes) -or [int64]$Target.bytes -ne $ExpectedBytes -or
            $Target.sha256 -isnot [string] -or [string]$Target.sha256 -cne $ExpectedSha256) {
            throw ('NEEDS_CONTEXT: ' + $Context + ' target inventory seal/relation failed: ' + $TargetPath)
        }
        if ($RequirePhysical) {
            $Physical = New-FileSeal $TargetPath
            if ($Physical.bytes -ne $ExpectedBytes -or $Physical.sha256 -cne $ExpectedSha256) {
                throw ('NEEDS_CONTEXT: ' + $Context + ' physical target drifted: ' + $TargetPath)
            }
        }
        [void]$ActualPaths.Add($TargetPath)
    }
    $ExpectedCanonical = [string[]]@($ExpectedPaths | ForEach-Object { Get-CanonicalPath $_ })
    $ActualCanonical = [string[]]$ActualPaths.ToArray()
    [Array]::Sort($ExpectedCanonical,[StringComparer]::Ordinal)
    [Array]::Sort($ActualCanonical,[StringComparer]::Ordinal)
    if ($ActualCanonical.Count -ne $ExpectedCanonical.Count -or
        ($ActualCanonical -join '|') -cne ($ExpectedCanonical -join '|')) {
        throw ('NEEDS_CONTEXT: ' + $Context + ' target paths are not the exact top-level set.')
    }
}
function Get-V3CurrentSaveInventoryExact(
    [object]$RecordedInventory,[string]$ExternalRoot,[string]$LocalRoot,
    [int]$ExpectedTargetCount,[bool]$ObserverMode,[string]$Context
) {
    if (-not (Test-Path -LiteralPath $ExternalRoot -PathType Container)) {
        throw ('NEEDS_CONTEXT: current external SaveDir is missing ' + $Context)
    }
    if (Test-Path -LiteralPath $LocalRoot) {
        if (-not (Test-Path -LiteralPath $LocalRoot -PathType Container)) {
            throw ('NEEDS_CONTEXT: current local save root is not a directory ' + $Context)
        }
    } elseif (-not $ObserverMode) {
        throw ('NEEDS_CONTEXT: current generator local save root is missing ' + $Context)
    }
    $CurrentTable = New-SaveInventory $ExternalRoot $LocalRoot $ExpectedTargetCount
    $CurrentJson = ConvertTo-Json -InputObject $CurrentTable -Depth 16 -Compress
    $CurrentInventory = $CurrentJson | ConvertFrom-Json -ErrorAction Stop
    Assert-SaveInventoryRecord $RecordedInventory $ExpectedTargetCount ($Context + ' recorded')
    Assert-SaveInventoryRecord $CurrentInventory $ExpectedTargetCount ($Context + ' current')
    if (-not (Test-V3CanonicalExpectedPath $RecordedInventory.roots.external_savedir $ExternalRoot) -or
        -not (Test-V3CanonicalExpectedPath $RecordedInventory.roots.local_savedir $LocalRoot)) {
        throw ('NEEDS_CONTEXT: recorded save inventory roots drifted ' + $Context)
    }
    if ($ObserverMode -and @($CurrentInventory.files | Where-Object {
        $_.kind -cne 'target' -and $_.kind -cne 'persistent'
    }).Count -ne 0) {
        throw ('NEEDS_CONTEXT: current observer inventory contains a forbidden kind ' + $Context)
    }
    $RecordedJson = ConvertTo-Json -InputObject $RecordedInventory -Depth 16 -Compress
    if ($CurrentJson -cne $RecordedJson) {
        throw ('NEEDS_CONTEXT: full physical save inventory differs from completion ' + $Context)
    }
    return $CurrentInventory
}
# TASK1_V3_RUNTIME_HELPERS_INVENTORY_END
# TASK1_V3_RUNTIME_READERS_BEGIN
function Get-V3FrozenSeal([string]$Path,[string]$ExpectedPath,[int64]$ExpectedBytes,[string]$ExpectedHash,[string]$Context) {
    if (-not (Test-Path -LiteralPath $Path -PathType Leaf) -or -not (Get-Item -LiteralPath $Path).IsReadOnly) {
        throw ('NEEDS_CONTEXT: frozen leaf is missing or writable ' + $Context)
    }
    $Seal = New-FileSeal $Path
    if ($Seal.path -cne (Get-CanonicalPath $ExpectedPath) -or $Seal.bytes -ne $ExpectedBytes -or
        $Seal.sha256 -cne $ExpectedHash) {
        throw ('NEEDS_CONTEXT: frozen leaf seal drifted ' + $Context)
    }
    return $Seal
}
function Read-V3GeneratorSnapshot([string]$ExpectedCompletionSha256) {
    if ($ExpectedCompletionSha256 -cnotmatch '^[0-9A-F]{64}$') {
        throw 'NEEDS_CONTEXT: generator snapshot checkpoint is not uppercase SHA-256.'
    }
    $CompletionSeal = Get-V3FrozenSeal $GeneratorCompletionPath $GeneratorCompletionPath `
        ([int64](Get-Item -LiteralPath $GeneratorCompletionPath).Length) $ExpectedCompletionSha256 'generator completion'
    $Completion = Read-RecoveryStrictJson $GeneratorCompletionPath 'strict generator snapshot completion'
    Assert-ExactProperties $Completion $GeneratorCompletionProperties 'strict generator snapshot completion'

    $AttemptSeal = New-FileSeal ([string]$Completion.attempt_path)
    [void](Get-V3FrozenSeal ([string]$Completion.attempt_path) $GeneratorAttemptPath `
        ([int64]$AttemptSeal.bytes) ([string]$Completion.attempt_sha256) 'generator attempt')
    $Attempt = Read-RecoveryStrictJson $GeneratorAttemptPath 'strict generator snapshot attempt'
    Assert-ExactProperties $Attempt $GeneratorAttemptProperties 'strict generator snapshot attempt'
    if ($Attempt.schema_version -isnot [int] -or $Attempt.schema_version -ne 2 -or
        $Attempt.attempt_id -isnot [string] -or $Attempt.attempt_id -cne [string]$Completion.attempt_id -or
        -not (Test-RoundtripUtc $Attempt.started_utc) -or
        $Attempt.approval_lock_sha256 -isnot [string] -or $Attempt.approval_lock_sha256 -cne $ApprovalLockSha256 -or
        $Attempt.approved_plan_commit -isnot [string] -or $Attempt.approved_plan_commit -cne $P3 -or
        $Attempt.predecessor_manifest_sha256 -isnot [string] -or
        $Attempt.predecessor_manifest_sha256 -cne [string]$Approval.predecessor_manifest_sha256 -or
        $Attempt.max_generator_invocations -isnot [int] -or $Attempt.max_generator_invocations -ne 1 -or
        $Attempt.retry_allowed -isnot [bool] -or [bool]$Attempt.retry_allowed) {
        throw 'NEEDS_CONTEXT: generator attempt contract drifted during strict snapshot.'
    }

    $RedSeal = New-FileSeal $RedRecordPath
    $GreenSeal = New-FileSeal $GreenRecordPath
    [void](Get-V3FrozenSeal $RedRecordPath $RedRecordPath ([int64]$RedSeal.bytes) `
        ([string]$Completion.red_record_sha256) 'generator RED')
    [void](Get-V3FrozenSeal $GreenRecordPath $GreenRecordPath ([int64]$GreenSeal.bytes) `
        ([string]$Completion.green_record_sha256) 'generator GREEN')
    $Green = Read-RecoveryStrictJson $GreenRecordPath 'strict generator snapshot GREEN'
    Assert-ExactProperties $Green @('schema_version','verdict','fixture_gate','stream_gate','inputs','mutations','created_utc') `
        'strict generator snapshot GREEN'
    if ($Green.schema_version -isnot [int] -or $Green.schema_version -ne 3 -or $Green.verdict -cne 'PASS' -or
        @($Green.inputs).Count -ne 3 -or @($Green.mutations).Count -ne 42) {
        throw 'NEEDS_CONTEXT: strict generator GREEN summary drifted.'
    }
    $ExpectedGreenRoles = @('patched_generator_fixture','v2_test_report_control','v2_engine_boot_log_control')
    $ExpectedGreenPaths = @(
        (Get-CanonicalPath (Join-Path $GeneratorRoot 'game\zz_terminal_collapse_legacy_fixture.rpy')),
        (Get-CanonicalPath $V2StdoutPath),(Get-CanonicalPath $V2EngineLogPath)
    )
    for ($Index = 0; $Index -lt 3; $Index++) {
        $Input = @($Green.inputs)[$Index]
        Assert-ExactProperties $Input @('role','path','bytes','sha256') ('strict GREEN input ' + $Index)
        if ($Input.role -isnot [string] -or [string]$Input.role -cne $ExpectedGreenRoles[$Index] -or
            $Input.path -isnot [string] -or -not [IO.Path]::IsPathRooted([string]$Input.path) -or
            [string]$Input.path -cne (Get-CanonicalPath ([string]$Input.path)) -or
            [string]$Input.path -cne $ExpectedGreenPaths[$Index]) {
            throw ('NEEDS_CONTEXT: strict GREEN input role/path drifted at index ' + $Index)
        }
        $InputSeal = New-FileSeal ([string]$Input.path)
        if (-not (Test-RecoveryIntegral $Input.bytes) -or [int64]$Input.bytes -ne [int64]$InputSeal.bytes -or
            $Input.sha256 -isnot [string] -or [string]$Input.sha256 -cne [string]$InputSeal.sha256) {
            throw ('NEEDS_CONTEXT: strict GREEN input current seal drifted at index ' + $Index)
        }
    }

    $FixturePath = Get-CanonicalPath (Join-Path $GeneratorRoot 'game\zz_terminal_collapse_legacy_fixture.rpy')
    $FixtureSeal = New-FileSeal $FixturePath
    $FixtureEvidenceSeal = New-FileSeal $GeneratorFixtureEvidence
    if ($FixtureSeal.sha256 -cne [string]@($Green.inputs)[0].sha256 -or
        $FixtureEvidenceSeal.sha256 -cne $FixtureSeal.sha256 -or
        $FixtureEvidenceSeal.bytes -ne $FixtureSeal.bytes -or
        -not (Get-Item -LiteralPath $GeneratorFixtureEvidence).IsReadOnly) {
        throw 'NEEDS_CONTEXT: generator fixture/evidence no longer equals strict GREEN.'
    }

    $RequestSeal = New-FileSeal ([string]$Completion.request_path)
    $ResultSeal = New-FileSeal ([string]$Completion.result_path)
    $StateSeal = New-FileSeal ([string]$Completion.state_path)
    $StdoutSeal = New-FileSeal ([string]$Completion.rpytest_stdout_path)
    $StderrSeal = New-FileSeal ([string]$Completion.stderr_path)
    $EngineSeal = New-FileSeal ([string]$Completion.engine_log_evidence_path)
    foreach ($Durable in @(
        [pscustomobject]@{ seal=$RequestSeal; path=(Join-Path $GeneratorProcessEvidence 'request.json'); bytes=$Completion.request_bytes; hash=$Completion.request_sha256; label='request' },
        [pscustomobject]@{ seal=$ResultSeal; path=(Join-Path $GeneratorProcessEvidence 'result.json'); bytes=$Completion.result_bytes; hash=$Completion.result_sha256; label='result' },
        [pscustomobject]@{ seal=$StateSeal; path=$GeneratorStatePath; bytes=$Completion.state_bytes; hash=$Completion.state_sha256; label='state' },
        [pscustomobject]@{ seal=$StdoutSeal; path=(Join-Path $GeneratorProcessEvidence 'stdout.txt'); bytes=$Completion.rpytest_stdout_bytes; hash=$Completion.rpytest_stdout_sha256; label='stdout' },
        [pscustomobject]@{ seal=$StderrSeal; path=(Join-Path $GeneratorProcessEvidence 'stderr.txt'); bytes=$Completion.stderr_bytes; hash=$Completion.stderr_sha256; label='stderr' },
        [pscustomobject]@{ seal=$EngineSeal; path=$GeneratorLogEvidence; bytes=$EngineSeal.bytes; hash=$Completion.engine_log_evidence_sha256; label='engine log' }
    )) {
        [void](Get-V3FrozenSeal ([string]$Durable.seal.path) ([string]$Durable.path) `
            ([int64]$Durable.bytes) ([string]$Durable.hash) ('generator ' + [string]$Durable.label))
    }
    $Request = Read-HelperJson ([string]$RequestSeal.path) 'strict generator snapshot request'
    $Result = Read-HelperJson ([string]$ResultSeal.path) 'strict generator snapshot result'
    Assert-PrivateDesktopCompletion $Result 0 'strict generator snapshot result'
    $State = Read-RecoveryStrictJson ([string]$StateSeal.path) 'strict generator snapshot state'
    $RawEngineSeal = New-FileSeal (Join-Path $GeneratorRoot 'log.txt')
    if ($RawEngineSeal.bytes -ne $EngineSeal.bytes -or $RawEngineSeal.sha256 -cne $EngineSeal.sha256) {
        throw 'NEEDS_CONTEXT: current generator engine source differs from durable evidence.'
    }
    $Marker = 'terminal-collapse-legacy-v3:' + $P3 + ':supply-vanguard-remember:final-menu'
    $RequestExpected = [pscustomobject][ordered]@{
        executable=(Get-CanonicalPath $RenPyExe)
        arguments=[object[]]@((Get-CanonicalPath $GeneratorRoot),'test','terminal_collapse_legacy_generator','--savedir',(Get-CanonicalPath $GeneratorSaveDir))
        working_directory=(Get-CanonicalPath $GeneratorRoot)
        environment_names=[object[]]$GeneratorEnvironmentNames
        environment_values=[object[]]@('1',$null,'sw','dummy','dummy',$P3,[string]$FixtureSeal.sha256,$GameTree,$Marker,
            (Get-CanonicalPath $GeneratorSaveDir),(Get-CanonicalPath $GeneratorStatePath))
        timeout_milliseconds=[int64]180000; stdout_path=[string]$StdoutSeal.path
        stderr_path=[string]$StderrSeal.path; result_path=[string]$ResultSeal.path
    }
    if ((Test-V3RequestContract 'generator' $Request $RequestExpected) -cne 'ACCEPT' -or
        (Test-V3GeneratorStateContract $State (Get-CanonicalPath $GeneratorSaveDir) $Marker $P3 $GameTree) -cne 'ACCEPT') {
        throw 'NEEDS_CONTEXT: generator request/state failed the shared production validators during strict snapshot.'
    }
    if ((Get-CanonicalPath ([string]$Result.stdout_path)) -cne [string]$StdoutSeal.path -or
        (Get-CanonicalPath ([string]$Result.stderr_path)) -cne [string]$StderrSeal.path) {
        throw 'NEEDS_CONTEXT: generator result stream paths drifted during strict snapshot.'
    }
    $Channel = [pscustomobject][ordered]@{
        stdout_exists=$true; stdout_path=[string]$StdoutSeal.path; request_stdout_path=[string]$Request.stdout_path
        result_stdout_path=[string]$Result.stdout_path; stdout_bytes=[IO.File]::ReadAllBytes([string]$StdoutSeal.path)
        stderr_exists=$true; stderr_bytes=[IO.File]::ReadAllBytes([string]$StderrSeal.path)
        engine_exists=$true; engine_source_path=[string]$RawEngineSeal.path
        engine_bytes=[IO.File]::ReadAllBytes([string]$RawEngineSeal.path)
        engine_evidence_seal=$EngineSeal
    }
    if ((Test-V3ChannelContract 'generator' $Channel) -cne 'ACCEPT') {
        throw 'NEEDS_CONTEXT: generator channels failed the shared production validator during strict snapshot.'
    }

    $ExpectedTargetPaths = [string[]]@(
        (Get-CanonicalPath (Join-Path $GeneratorSaveDir ([string]$Completion.save_name))),
        (Get-CanonicalPath (Join-Path (Join-Path $GeneratorSaveDir 'sync') ([string]$Completion.save_name))),
        (Get-CanonicalPath (Join-Path (Join-Path $GeneratorRoot 'game\saves') ([string]$Completion.save_name)))
    )
    $CurrentGeneratorInventory = Get-V3CurrentSaveInventoryExact `
        $Completion.save_inventory $GeneratorSaveDir (Join-Path $GeneratorRoot 'game\saves') `
        3 $false 'strict generator snapshot'
    $TargetSeals = [object[]]@($ExpectedTargetPaths | ForEach-Object { New-FileSeal $_ })
    $Expected = [pscustomobject][ordered]@{
        attempt_id=[string]$Attempt.attempt_id; attempt_seal=$AttemptSeal; approval_lock_sha256=$ApprovalLockSha256
        approved_plan_commit=$P3; predecessor_manifest_sha256=[string]$Approval.predecessor_manifest_sha256
        red_record_sha256=[string]$RedSeal.sha256; green_record_sha256=[string]$GreenSeal.sha256
        worktree_path=(Get-CanonicalPath $GeneratorRoot); savedir_path=(Get-CanonicalPath $GeneratorSaveDir)
        process_evidence_dir=(Get-CanonicalPath $GeneratorProcessEvidence); fixture_seal=$FixtureSeal
        fixture_evidence_seal=$FixtureEvidenceSeal; request_seal=$RequestSeal; result_seal=$ResultSeal
        state_seal=$StateSeal; stdout_seal=$StdoutSeal; stderr_seal=$StderrSeal
        engine_log_evidence_seal=$EngineSeal; target_seals=$TargetSeals
        save_name=[string]$Completion.save_name; save_inventory=$CurrentGeneratorInventory
    }
    if ((Test-V3GeneratorCompletionContract $Completion $Expected) -cne 'ACCEPT' -or
        (Test-V3GeneratorRuntimeEvidenceContract $Channel $Completion $Expected) -cne 'ACCEPT') {
        throw 'NEEDS_CONTEXT: generator completion/current evidence failed shared production validators.'
    }
    Assert-SaveInventoryTargets -Inventory $CurrentGeneratorInventory -ExpectedPaths $ExpectedTargetPaths `
        -ExpectedBytes ([int64]$Completion.save_bytes) -ExpectedSha256 ([string]$Completion.save_sha256) `
        -RequirePhysical $true -Context 'strict generator snapshot'
    return [pscustomobject][ordered]@{
        completion=$Completion; completion_seal=$CompletionSeal; attempt=$Attempt; attempt_seal=$AttemptSeal
        request=$Request; result=$Result; state=$State; expected=$Expected; channel=$Channel
        marker=$Marker; fixture_seal=$FixtureSeal; target_seals=$TargetSeals
    }
}
function Read-V3ObserverSnapshot([string]$ExpectedCompletionSha256,[object]$GeneratorSnapshot) {
    if ($ExpectedCompletionSha256 -cnotmatch '^[0-9A-F]{64}$' -or $null -eq $GeneratorSnapshot) {
        throw 'NEEDS_CONTEXT: observer snapshot checkpoint/generator snapshot is invalid.'
    }
    $CompletionSeal = Get-V3FrozenSeal $ObserverCompletionPath $ObserverCompletionPath `
        ([int64](Get-Item -LiteralPath $ObserverCompletionPath).Length) $ExpectedCompletionSha256 'observer completion'
    $Completion = Read-RecoveryStrictJson $ObserverCompletionPath 'strict observer snapshot completion'
    Assert-ExactProperties $Completion $ObserverCompletionProperties 'strict observer snapshot completion'
    $AttemptSeal = New-FileSeal ([string]$Completion.attempt_path)
    [void](Get-V3FrozenSeal ([string]$Completion.attempt_path) $ObserverAttemptPath `
        ([int64]$AttemptSeal.bytes) ([string]$Completion.attempt_sha256) 'observer attempt')
    $Attempt = Read-RecoveryStrictJson $ObserverAttemptPath 'strict observer snapshot attempt'
    Assert-ExactProperties $Attempt $ObserverAttemptProperties 'strict observer snapshot attempt'
    if ($Attempt.schema_version -isnot [int] -or $Attempt.schema_version -ne 2 -or
        $Attempt.attempt_id -isnot [string] -or $Attempt.attempt_id -cne [string]$Completion.attempt_id -or
        -not (Test-RoundtripUtc $Attempt.started_utc) -or $Attempt.approval_lock_sha256 -cne $ApprovalLockSha256 -or
        $Attempt.approved_plan_commit -cne $P3 -or $Attempt.generator_completion_sha256 -cne
            [string]$GeneratorSnapshot.completion_seal.sha256 -or
        $Attempt.max_observer_invocations -isnot [int] -or $Attempt.max_observer_invocations -ne 1 -or
        $Attempt.retry_allowed -isnot [bool] -or [bool]$Attempt.retry_allowed) {
        throw 'NEEDS_CONTEXT: observer attempt contract drifted during strict snapshot.'
    }
    $FixtureSeal = New-FileSeal (Join-Path $ObserverRoot 'game\zz_terminal_collapse_legacy_observer.rpy')
    $FixtureEvidenceSeal = New-FileSeal $ObserverFixtureEvidence
    if ($FixtureEvidenceSeal.bytes -ne $FixtureSeal.bytes -or $FixtureEvidenceSeal.sha256 -cne $FixtureSeal.sha256 -or
        -not (Get-Item -LiteralPath $ObserverFixtureEvidence).IsReadOnly) {
        throw 'NEEDS_CONTEXT: observer fixture/evidence relation drifted.'
    }
    $RequestSeal = New-FileSeal ([string]$Completion.request_path)
    $ResultSeal = New-FileSeal ([string]$Completion.result_path)
    $StateSeal = New-FileSeal ([string]$Completion.state_path)
    $StdoutSeal = New-FileSeal ([string]$Completion.stdout_path)
    $StderrSeal = New-FileSeal ([string]$Completion.stderr_path)
    $EngineSeal = New-FileSeal ([string]$Completion.engine_log_evidence_path)
    foreach ($Durable in @(
        [pscustomobject]@{ seal=$RequestSeal; path=(Join-Path $ObserverProcessEvidence 'request.json'); bytes=$Completion.request_bytes; hash=$Completion.request_sha256; label='request' },
        [pscustomobject]@{ seal=$ResultSeal; path=(Join-Path $ObserverProcessEvidence 'result.json'); bytes=$Completion.result_bytes; hash=$Completion.result_sha256; label='result' },
        [pscustomobject]@{ seal=$StateSeal; path=$ObserverStatePath; bytes=$Completion.state_bytes; hash=$Completion.state_sha256; label='state' },
        [pscustomobject]@{ seal=$StdoutSeal; path=(Join-Path $ObserverProcessEvidence 'stdout.txt'); bytes=$Completion.stdout_bytes; hash=$Completion.stdout_sha256; label='stdout' },
        [pscustomobject]@{ seal=$StderrSeal; path=(Join-Path $ObserverProcessEvidence 'stderr.txt'); bytes=$Completion.stderr_bytes; hash=$Completion.stderr_sha256; label='stderr' },
        [pscustomobject]@{ seal=$EngineSeal; path=$ObserverLogEvidence; bytes=$EngineSeal.bytes; hash=$Completion.engine_log_evidence_sha256; label='engine log' }
    )) {
        [void](Get-V3FrozenSeal ([string]$Durable.seal.path) ([string]$Durable.path) `
            ([int64]$Durable.bytes) ([string]$Durable.hash) ('observer ' + [string]$Durable.label))
    }
    $Request = Read-HelperJson ([string]$RequestSeal.path) 'strict observer snapshot request'
    $Result = Read-HelperJson ([string]$ResultSeal.path) 'strict observer snapshot result'
    Assert-PrivateDesktopCompletion $Result 0 'strict observer snapshot result'
    $State = Read-RecoveryStrictJson ([string]$StateSeal.path) 'strict observer snapshot state'
    $RawEngineSeal = New-FileSeal (Join-Path $ObserverRoot 'log.txt')
    if ($RawEngineSeal.bytes -ne $EngineSeal.bytes -or $RawEngineSeal.sha256 -cne $EngineSeal.sha256) {
        throw 'NEEDS_CONTEXT: current observer engine source differs from durable evidence.'
    }
    $RequestExpected = [pscustomobject][ordered]@{
        executable=(Get-CanonicalPath $RenPyExe)
        arguments=[object[]]@((Get-CanonicalPath $ObserverRoot),'run','--savedir',(Get-CanonicalPath $ObserverSaveDir))
        working_directory=(Get-CanonicalPath $ObserverRoot); environment_names=[object[]]$ObserverEnvironmentNames
        environment_values=[object[]]@('1','1',$null,'sw','dummy','dummy',$P3,[string]$FixtureSeal.sha256,$GameTree,
            [string]$GeneratorSnapshot.marker,(Get-CanonicalPath $ObserverSaveDir),(Get-CanonicalPath $ObserverStatePath))
        timeout_milliseconds=[int64]120000; stdout_path=[string]$StdoutSeal.path
        stderr_path=[string]$StderrSeal.path; result_path=[string]$ResultSeal.path
    }
    if ((Test-V3RequestContract 'observer' $Request $RequestExpected) -cne 'ACCEPT' -or
        (Test-V3ObserverStateContract $State (Get-CanonicalPath $ObserverSaveDir) `
            ([string]$GeneratorSnapshot.marker) $P3 $GameTree $GeneratorSnapshot.state.slot_metadata) -cne 'ACCEPT') {
        throw 'NEEDS_CONTEXT: observer request/state failed shared production validators during strict snapshot.'
    }
    if ((Get-CanonicalPath ([string]$Result.stdout_path)) -cne [string]$StdoutSeal.path -or
        (Get-CanonicalPath ([string]$Result.stderr_path)) -cne [string]$StderrSeal.path) {
        throw 'NEEDS_CONTEXT: observer result stream paths drifted during strict snapshot.'
    }
    $Channel = [pscustomobject][ordered]@{
        stdout_exists=$true; stdout_path=[string]$StdoutSeal.path; request_stdout_path=[string]$Request.stdout_path
        result_stdout_path=[string]$Result.stdout_path; stdout_bytes=[IO.File]::ReadAllBytes([string]$StdoutSeal.path)
        stderr_exists=$true; stderr_bytes=[IO.File]::ReadAllBytes([string]$StderrSeal.path)
        engine_exists=$true; engine_source_path=[string]$RawEngineSeal.path
        engine_bytes=[IO.File]::ReadAllBytes([string]$RawEngineSeal.path)
        engine_evidence_seal=$EngineSeal
    }
    if ((Test-V3ChannelContract 'observer' $Channel) -cne 'ACCEPT') {
        throw 'NEEDS_CONTEXT: observer channels failed shared production validator during strict snapshot.'
    }
    $SourceSeal = New-FileSeal ([string]$GeneratorSnapshot.completion.external_save_path)
    $ReplayPath = Get-CanonicalPath (Join-Path $ObserverSaveDir ([string]$GeneratorSnapshot.completion.save_name))
    $CurrentObserverInventory = Get-V3CurrentSaveInventoryExact `
        $Completion.save_inventory $ObserverSaveDir (Join-Path $ObserverRoot 'game\saves') `
        1 $true 'strict observer snapshot'
    $ReplaySeal = New-FileSeal $ReplayPath
    $Expected = [pscustomobject][ordered]@{
        attempt_id=[string]$Attempt.attempt_id; attempt_seal=$AttemptSeal; approval_lock_sha256=$ApprovalLockSha256
        approved_plan_commit=$P3; generator_completion_sha256=[string]$GeneratorSnapshot.completion_seal.sha256
        worktree_path=(Get-CanonicalPath $ObserverRoot); savedir_path=(Get-CanonicalPath $ObserverSaveDir)
        process_evidence_dir=(Get-CanonicalPath $ObserverProcessEvidence); fixture_seal=$FixtureSeal
        fixture_evidence_seal=$FixtureEvidenceSeal; request_seal=$RequestSeal; result_seal=$ResultSeal
        state_seal=$StateSeal; stdout_seal=$StdoutSeal; stderr_seal=$StderrSeal
        engine_log_evidence_seal=$EngineSeal; source_before_seal=$SourceSeal; source_after_seal=$SourceSeal
        replay_before_seal=$ReplaySeal; replay_after_seal=$ReplaySeal; save_inventory=$CurrentObserverInventory
    }
    if ((Test-V3ObserverCompletionContract $Completion $Expected) -cne 'ACCEPT' -or
        (Test-V3ObserverRuntimeEvidenceContract $Channel $Completion $Expected) -cne 'ACCEPT') {
        throw 'NEEDS_CONTEXT: observer completion/current evidence failed shared production validators.'
    }
    Assert-SaveInventoryTargets -Inventory $CurrentObserverInventory -ExpectedPaths ([string[]]@($ReplayPath)) `
        -ExpectedBytes ([int64]$Completion.replay_save_bytes) `
        -ExpectedSha256 ([string]$Completion.replay_save_sha256_after) -RequirePhysical $true `
        -Context 'strict observer snapshot'
    return [pscustomobject][ordered]@{
        completion=$Completion; completion_seal=$CompletionSeal; attempt=$Attempt; attempt_seal=$AttemptSeal
        request=$Request; result=$Result; state=$State; expected=$Expected; channel=$Channel
        fixture_seal=$FixtureSeal; source_seal=$SourceSeal; replay_seal=$ReplaySeal
    }
}
# TASK1_V3_RUNTIME_READERS_END
$GeneratorSaveInventory = New-SaveInventory $GeneratorSaveDir $GeneratorLocalSaves 3
Assert-ExactProperties ([pscustomobject]$GeneratorSaveInventory) @('roots','directories','files','target_count') 'generator save inventory'
Assert-ExactProperties ([pscustomobject]$GeneratorSaveInventory.roots) @('external_savedir','local_savedir') 'generator save inventory roots'

$GeneratorRequestSeal = New-FileSeal $GeneratorRequestPath
$GeneratorStdoutSeal = New-FileSeal $GeneratorStdoutPath
$GeneratorStderrSeal = New-FileSeal $GeneratorStderrPath
$GeneratorResultSeal = New-FileSeal $GeneratorResultPath
$GeneratorStateSeal = New-FileSeal $GeneratorStatePath
$GeneratorAttemptSeal = New-FileSeal $GeneratorAttemptPath
$GeneratorFixtureSeal = New-FileSeal $GeneratorFixturePath
$GeneratorFixtureEvidenceSeal = New-FileSeal $GeneratorFixtureEvidence
$GeneratorLogEvidenceSeal = New-FileSeal $GeneratorLogEvidence
$GeneratorChannelEnvelope = [pscustomobject][ordered]@{
    stdout_exists=$true; stdout_path=(Get-CanonicalPath $GeneratorStdoutPath)
    request_stdout_path=(Get-CanonicalPath ([string]$GeneratorRequest.stdout_path)
    ); result_stdout_path=(Get-CanonicalPath ([string]$PersistedGeneratorResult.stdout_path)
    ); stdout_bytes=[IO.File]::ReadAllBytes($GeneratorStdoutPath)
    stderr_exists=$true; stderr_bytes=[IO.File]::ReadAllBytes($GeneratorStderrPath)
    engine_exists=$true; engine_source_path=(Get-CanonicalPath $GeneratorLogPath)
    engine_bytes=[IO.File]::ReadAllBytes($GeneratorLogPath)
    engine_evidence_seal=$GeneratorLogEvidenceSeal
}
if ((Test-V3ChannelContract 'generator' $GeneratorChannelEnvelope) -cne 'ACCEPT') {
    throw 'NEEDS_CONTEXT: live generator channel contract rejected current process/log evidence.'
}
$GeneratorCompletionPayload = [ordered]@{
    schema_version = 2
    attempt_id = $GeneratorAttemptId
    attempt_path = Get-CanonicalPath $GeneratorAttemptPath
    attempt_sha256 = $GeneratorAttemptSha256
    approval_lock_sha256 = $ApprovalLockSha256
    approved_plan_commit = $P3
    predecessor_manifest_sha256 = [string]$Approval.predecessor_manifest_sha256
    red_record_sha256 = $RedRecordSha256
    green_record_sha256 = $GreenRecordSha256
    worktree_path = Get-CanonicalPath $GeneratorRoot
    savedir_path = Get-CanonicalPath $GeneratorSaveDir
    process_evidence_dir = Get-CanonicalPath $GeneratorProcessEvidence
    fixture_path = Get-CanonicalPath $GeneratorFixturePath
    fixture_sha256 = $GreenFixtureSha256
    fixture_evidence_path = [string]$GeneratorFixtureEvidenceSeal.path
    fixture_evidence_sha256 = [string]$GeneratorFixtureEvidenceSeal.sha256
    request_path = [string]$GeneratorRequestSeal.path
    request_bytes = [int64]$GeneratorRequestSeal.bytes
    request_sha256 = [string]$GeneratorRequestSeal.sha256
    result_path = [string]$GeneratorResultSeal.path
    result_bytes = [int64]$GeneratorResultSeal.bytes
    result_sha256 = [string]$GeneratorResultSeal.sha256
    state_path = [string]$GeneratorStateSeal.path
    state_bytes = [int64]$GeneratorStateSeal.bytes
    state_sha256 = [string]$GeneratorStateSeal.sha256
    rpytest_stdout_path = [string]$GeneratorStdoutSeal.path
    rpytest_stdout_bytes = [int64]$GeneratorStdoutSeal.bytes
    rpytest_stdout_sha256 = [string]$GeneratorStdoutSeal.sha256
    stderr_path = [string]$GeneratorStderrSeal.path
    stderr_bytes = [int64]$GeneratorStderrSeal.bytes
    stderr_sha256 = [string]$GeneratorStderrSeal.sha256
    engine_log_evidence_path = [string]$GeneratorLogEvidenceSeal.path
    engine_log_evidence_sha256 = [string]$GeneratorLogEvidenceSeal.sha256
    external_save_path = Get-CanonicalPath $ExternalSave.FullName
    sync_save_path = Get-CanonicalPath $SyncSave.FullName
    local_save_path = Get-CanonicalPath $LocalSave.FullName
    target_copy_count = 3
    save_name = [string]$ExternalSave.Name
    save_bytes = [int64]$ExternalSave.Length
    save_sha256 = $ExternalHash
    save_inventory = $GeneratorSaveInventory
    finished_utc = [DateTime]::UtcNow.ToString('o', [Globalization.CultureInfo]::InvariantCulture)
}
$GeneratorTargetSeals = [object[]]@(
    (New-FileSeal $ExternalSave.FullName),(New-FileSeal $SyncSave.FullName),(New-FileSeal $LocalSave.FullName)
)
$GeneratorCompletionExpected = [pscustomobject][ordered]@{
    attempt_id=$GeneratorAttemptId; attempt_seal=$GeneratorAttemptSeal; approval_lock_sha256=$ApprovalLockSha256
    approved_plan_commit=$P3; predecessor_manifest_sha256=[string]$Approval.predecessor_manifest_sha256
    red_record_sha256=$RedRecordSha256; green_record_sha256=$GreenRecordSha256
    worktree_path=(Get-CanonicalPath $GeneratorRoot); savedir_path=(Get-CanonicalPath $GeneratorSaveDir)
    process_evidence_dir=(Get-CanonicalPath $GeneratorProcessEvidence); fixture_seal=$GeneratorFixtureSeal
    fixture_evidence_seal=$GeneratorFixtureEvidenceSeal; request_seal=$GeneratorRequestSeal
    result_seal=$GeneratorResultSeal; state_seal=$GeneratorStateSeal; stdout_seal=$GeneratorStdoutSeal
    stderr_seal=$GeneratorStderrSeal; engine_log_evidence_seal=$GeneratorLogEvidenceSeal
    target_seals=$GeneratorTargetSeals; save_name=[string]$ExternalSave.Name; save_inventory=$GeneratorSaveInventory
}
if ((Test-V3GeneratorCompletionContract ([pscustomobject]$GeneratorCompletionPayload) $GeneratorCompletionExpected) -cne 'ACCEPT') {
    throw 'NEEDS_CONTEXT: prospective generator completion failed the central 42-field contract.'
}
Assert-RecoveryAuthorityUnchanged 'before generator completion'
$GeneratorCompletion = New-ReadOnlyJsonRecord $GeneratorCompletionPath $GeneratorCompletionPayload $GeneratorCompletionProperties 'generator completion'
Assert-SaveInventoryRecord $GeneratorCompletion.save_inventory 3 'generator completion'
Assert-SaveInventoryTargets -Inventory $GeneratorCompletion.save_inventory `
    -ExpectedPaths ([string[]]@($ExternalSave.FullName,$SyncSave.FullName,$LocalSave.FullName)) `
    -ExpectedBytes ([int64]$ExternalSave.Length) -ExpectedSha256 $ExternalHash `
    -RequirePhysical $true -Context 'generator completion'
if ((Test-V3GeneratorCompletionContract $GeneratorCompletion $GeneratorCompletionExpected) -cne 'ACCEPT') {
    throw 'NEEDS_CONTEXT: generator completion strict reread failed the central 42-field contract.'
}
if ((Test-V3GeneratorRuntimeEvidenceContract $GeneratorChannelEnvelope $GeneratorCompletion `
        $GeneratorCompletionExpected) -cne 'ACCEPT') {
    throw 'NEEDS_CONTEXT: generator completion/channel consumer relation failed.'
}
$GeneratorCompletionSha256 = (Get-FileHash -LiteralPath $GeneratorCompletionPath -Algorithm SHA256).Hash
```

Expected: request schema 1 has exactly nine fields and the ordered 11-entry environment; result schema 2 has exactly 38 fields and passes the safety envelope. Helper stdout is the sole test_report and has exactly one target PASSED; stderr is the empty-file seal. `log.txt` is diagnostic-only engine_boot_log with zero rpytest lines and no high-specificity fatal marker; generic dummy-renderer `error(...)` remains allowed. The external root, external `sync/`, and local root targets are exactly three byte-identical saves, while all autosave/persistent byproducts are represented in the exact inventory. Every process/state/fixture/engine-log leaf is read-only before the exact 42-field schema-v2 generator completion is CreateNew and frozen. Only now may observer preparation begin.

- [ ] **Step 8: Create a clean detached observer worktree and its complete state-read-only fixture**

```powershell
if (-not (Get-Item -LiteralPath $GeneratorCompletionPath).IsReadOnly -or
    (Get-FileHash -LiteralPath $GeneratorCompletionPath -Algorithm SHA256).Hash -cne $GeneratorCompletionSha256) {
    throw 'NEEDS_CONTEXT: generator completion is not frozen; observer is forbidden.'
}
$GeneratorAppDataObservation = [pscustomobject][ordered]@{
    schema_version=1; backup_root=$AppDataBackupRoot
    generator_path=$GeneratorAppDataBackupPath
    generator_before=$GeneratorAppDataBefore; generator_after=$GeneratorAppDataAfter
    read_only=$true; authority=$false; cleanup_performed=$false
}
Assert-V3GeneratorAppDataObservation $GeneratorAppDataObservation 'generator-scope handoff'
$GeneratorAppDataHandoff = New-V3SealedJsonHandoff $GeneratorAppDataObservation `
    'generator AppData observation'
$GeneratorAppDataObservationBase64 = [string]$GeneratorAppDataHandoff.base64
$GeneratorAppDataObservationSha256 = [string]$GeneratorAppDataHandoff.sha256
$PersistedGeneratorCompletion = Read-RecoveryStrictJson $GeneratorCompletionPath 'generator completion before observer'
Assert-ExactProperties $PersistedGeneratorCompletion $GeneratorCompletionProperties 'generator completion before observer'
if ($PersistedGeneratorCompletion.save_sha256 -isnot [string] -or
    $PersistedGeneratorCompletion.save_sha256 -cne $ExternalHash -or
    (Get-CanonicalPath ([string]$PersistedGeneratorCompletion.external_save_path)) -cne (Get-CanonicalPath $ExternalSave.FullName) -or
    (Get-FileHash -LiteralPath ([string]$PersistedGeneratorCompletion.external_save_path) -Algorithm SHA256).Hash -cne $ExternalHash) {
    throw 'NEEDS_CONTEXT: generator source save lineage drifted before observer setup.'
}
git worktree add --detach $ObserverRoot $P3
if ($LASTEXITCODE -ne 0) { throw 'Could not create the one recovery observer worktree.' }
if ((& git -C $ObserverRoot rev-parse HEAD).Trim() -cne $P3 -or
    (& git -C $ObserverRoot rev-parse 'HEAD:game').Trim() -cne $GameTree -or
    @(git -C $ObserverRoot status --short --untracked-files=all).Count -ne 0) {
    throw 'Observer worktree is not the exact clean P3 baseline.'
}
$ObserverFixturePath = Join-Path $ObserverRoot 'game\zz_terminal_collapse_legacy_observer.rpy'
$ObserverLocalSaves = Join-Path $ObserverRoot 'game\saves'
if (Test-Path -LiteralPath $ObserverLocalSaves) { throw 'Observer game/saves must start absent.' }
$ObserverPatchCheckpointSha256 = (Get-FileHash -LiteralPath $GeneratorCompletionPath -Algorithm SHA256).Hash
if ($ObserverPatchCheckpointSha256 -cne $GeneratorCompletionSha256 -or
    -not (Get-Item -LiteralPath $GeneratorCompletionPath).IsReadOnly) {
    throw 'NEEDS_CONTEXT: observer host-patch checkpoint is not the frozen generator completion.'
}
Assert-RecoveryAuthorityUnchanged 'at observer host apply_patch checkpoint'
Write-Output ('TASK1_V3_OBSERVER_HOST_APPLY_PATCH_CHECKPOINT_PATH=' + (Get-CanonicalPath $GeneratorCompletionPath))
Write-Output ('TASK1_V3_OBSERVER_HOST_APPLY_PATCH_CHECKPOINT_SHA256=' + $ObserverPatchCheckpointSha256)
Write-Output ('TASK1_V3_OBSERVER_HOST_APPLY_PATCH_CHECKPOINT_P3=' + $P3)
Write-Output ('TASK1_V3_OBSERVER_HOST_APPLY_PATCH_CHECKPOINT_GAME_TREE=' + $GameTree)
Write-Output ('TASK1_V3_OBSERVER_HOST_APPLY_PATCH_WORKTREE=' + (Get-CanonicalPath $ObserverRoot))
Write-Output ('TASK1_V3_GENERATOR_APPDATA_OBSERVATION_BASE64=' + $GeneratorAppDataObservationBase64)
Write-Output ('TASK1_V3_GENERATOR_APPDATA_OBSERVATION_SHA256=' + $GeneratorAppDataObservationSha256)
```

The second Windows PowerShell process ends at that printed checkpoint. The controller carries the original uppercase lock SHA, the exact uppercase observer-patch checkpoint SHA, and the bounded generator AppData observation's base64 plus uppercase SHA to the next process. The AppData handoff is non-authority and hash-sealed; it imports no unsealed PowerShell object or path authority. Using the frozen generator completion as the checkpoint, call the host's native `apply_patch` tool exactly once and add exactly this absolute v3 observer fixture. Do not call `apply_patch.bat` or a shell write fallback:

<!-- TASK1_V3_OBSERVER_PATCH_BEGIN -->
```diff
*** Begin Patch
*** Add File: E:/Projects/renpy-8.5.2-sdk/terminal-collapse-temp/cos-terminal-collapse-observer-recovery-v3/game/zz_terminal_collapse_legacy_observer.rpy
+init -1000 python:
+    import json as _tc_json
+    import os as _tc_os
+    import traceback as _tc_traceback
+
+    def _tc_install_observer():
+        r = renpy
+        j = _tc_json
+        o = _tc_os
+        tb = _tc_traceback
+        loaded = [False]
+        done = [False]
+        result_path = o.environ.get("TC_OBSERVER_RESULT", "")
+        expected_marker = o.environ.get("TC_EXPECTED_MARKER", "")
+        expected_commit = o.environ.get("TC_EXPECTED_BASELINE_COMMIT", "")
+        expected_game_tree = o.environ.get("TC_EXPECTED_GAME_TREE", "")
+        expected_savedir = o.environ.get("TC_EXPECTED_SAVEDIR", "")
+        expected_choices = [u"截断补给线——让他们饿三天再打", u"亲自率领前锋出击", u"记住这一切，继续前进"]
+        expected_menu = [u"正面强攻，以气势压倒对方", u"采用迂回战术，先攻击敌军侧翼"]
+
+        def canon(value):
+            return o.path.normcase(o.path.realpath(o.path.abspath(value)))
+
+        def finish(verdict, reason, payload, code):
+            if done[0]:
+                return
+            done[0] = True
+            payload.update({"schema": 1, "verdict": verdict, "reason": reason})
+            try:
+                if (not result_path) or (not o.path.isabs(result_path)):
+                    raise Exception("TC_OBSERVER_RESULT must be absolute")
+                temp = result_path + ".tmp-" + str(o.getpid())
+                raw = (j.dumps(payload, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
+                with open(temp, "xb") as stream:
+                    stream.write(raw)
+                    stream.flush()
+                    o.fsync(stream.fileno())
+                o.rename(temp, result_path)
+            except Exception:
+                print("TC_OBSERVER_EVIDENCE_WRITE_FAILURE")
+                print(tb.format_exc())
+                r.quit(status=97)
+            r.quit(status=code)
+
+        def after_load():
+            loaded[0] = True
+
+        def interact_body():
+            blockers = [name for name in ("confirm", "yesno_prompt", "privacy_policy_screen") if r.get_screen(name) is not None]
+            if blockers:
+                finish("FAIL", "unexpected confirmation or consent interaction", {"loaded": loaded[0], "blocking_screens": blockers}, 42)
+            if not loaded[0]:
+                return
+            if r.get_screen("choice") is None:
+                return
+
+            ctx = r.game.context()
+            node = r.game.script.namemap.get(ctx.current, None)
+            file_line = r.get_filename_line()
+            items = list(r.get_screen_variable("items", screen="choice"))
+            raw_captions = [i.caption for i in items if getattr(i, "action", None) is not None]
+            display_captions = [r.substitute(value).split("|", 1)[0] for value in raw_captions]
+            metadata = r.slot_json("1-1") or {}
+            return_stack = r.get_return_stack()
+            state = {
+                "intrigue": getattr(r.store, "intrigue", None),
+                "power": getattr(r.store, "power", None),
+                "iron_prepared": getattr(r.store, "_iron_prepared", None),
+            }
+            actual = {
+                "command": getattr(r.game.args, "command", None),
+                "is_in_test": bool(r.is_in_test()),
+                "configured_savedir": r.config.savedir,
+                "argument_savedir": getattr(r.game.args, "savedir", None),
+                "path_to_saves_env_present": "RENPY_PATH_TO_SAVES" in o.environ,
+                "auto_load_value": o.environ.get("RENPY_AUTO_LOAD"),
+                "context_count": len(r.game.contexts),
+                "is_top_context": len(r.game.contexts) == 1 and ctx is r.game.contexts[0],
+                "return_stack": [repr(value) for value in return_stack],
+                "context_current": repr(ctx.current),
+                "node_type": None if node is None else type(node).__name__,
+                "node_file": None if node is None else node.filename.replace("\\", "/"),
+                "node_line": None if node is None else node.linenumber,
+                "filename_line": [file_line[0].replace("\\", "/"), file_line[1]],
+                "statement_name": r.get_statement_name(),
+                "raw_captions": raw_captions,
+                "display_captions": display_captions,
+                "state": state,
+                "store_marker": getattr(r.store, "terminal_collapse_legacy_marker", None),
+                "slot_metadata": metadata,
+            }
+            checks = {
+                "normal_run": actual["command"] == "run" and not actual["is_in_test"],
+                "auto_load": actual["auto_load_value"] == "1-1",
+                "savedir": bool(expected_savedir) and canon(r.config.savedir) == canon(expected_savedir) and canon(r.game.args.savedir) == canon(expected_savedir),
+                "path_to_saves_absent": not actual["path_to_saves_env_present"],
+                "top_context": actual["is_top_context"],
+                "empty_return_stack": return_stack == [],
+                "production_menu_node": node is not None and type(node).__name__ == "Menu" and actual["node_file"].lower().endswith("game/chapter5.rpy") and actual["node_line"] == 2807 and actual["filename_line"] == [actual["node_file"], actual["node_line"]] and actual["statement_name"] == "menu",
+                "state": state == {"intrigue": 55, "power": 60, "iron_prepared": True},
+                "menu_items": display_captions == expected_menu and u"硬拼——你没有更好的选择了" not in display_captions,
+                "store_marker": bool(expected_marker) and actual["store_marker"] == expected_marker,
+                "slot_marker": metadata.get("tc_legacy_schema") == 1 and metadata.get("tc_legacy_marker") == expected_marker,
+                "slot_commit": bool(expected_commit) and metadata.get("tc_baseline_commit") == expected_commit,
+                "slot_game_tree": bool(expected_game_tree) and metadata.get("tc_game_tree") == expected_game_tree,
+                "slot_choices": metadata.get("tc_choice_path") == expected_choices,
+                "slot_menu": metadata.get("tc_menu_file") == "game/chapter5.rpy" and metadata.get("tc_menu_line") == 2807,
+                "slot_state": metadata.get("tc_state") == {"intrigue": 55, "power": 60, "iron_prepared": True},
+            }
+            failures = sorted([name for name, passed in checks.items() if not passed])
+            payload = {"loaded": True, "checks": checks, "failures": failures, "actual": actual}
+            if failures:
+                finish("FAIL", "observer assertions failed", payload, 41)
+            finish("PASS", "clean baseline normal-run autoload reached the production final tactics menu", payload, 0)
+
+        def interact():
+            try:
+                interact_body()
+            except r.game.QuitException:
+                raise
+            except Exception:
+                finish("FAIL", "observer internal exception", {"loaded": loaded[0], "traceback": tb.format_exc()}, 43)
+
+        return after_load, interact
+
+    _tc_after_load_observer, _tc_interact_observer = _tc_install_observer()
+    config.after_load_callbacks.append(_tc_after_load_observer)
+    config.interact_callbacks.append(_tc_interact_observer)
*** End Patch
```
<!-- TASK1_V3_OBSERVER_PATCH_END -->

The observer writes only its external result and closure flags. It never assigns production state. Start a third, genuinely fresh Windows PowerShell 5.1 process. The controller binds `$ApprovalLockSha256`, `$ObserverPatchCheckpointSha256`, and the generator AppData observation's bounded base64/SHA pair; no unsealed object, function, or authority path from the ended generator process is imported. Authenticate the known lock leaf before reading its bytes, resolving the repository, reading the plan, or decoding the non-authority observation. Then extract the reviewed bootstrap/validator/runtime blocks from the authenticated physical P3 plan, strictly reread the frozen generator completion, validate the hash-sealed observation, authenticate the exact host-written fixture bytes from the plan's patch block, and only then create its one external SaveDir or observer ledger:

```powershell
# TASK1_V3_OBSERVER_REENTRY_BEGIN
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
if ($PSVersionTable.PSEdition -cne 'Desktop' -or $PSVersionTable.PSVersion.Major -ne 5) {
    throw 'NEEDS_CONTEXT: observer post-patch scope requires Windows PowerShell 5.1 Desktop.'
}
$LockVariable = Get-Variable -Name ApprovalLockSha256 -Scope 0 -ErrorAction SilentlyContinue
$ObserverCheckpointVariable = Get-Variable -Name ObserverPatchCheckpointSha256 -Scope 0 -ErrorAction SilentlyContinue
$GeneratorAppDataBase64Variable = Get-Variable -Name GeneratorAppDataObservationBase64 -Scope 0 -ErrorAction SilentlyContinue
$GeneratorAppDataShaVariable = Get-Variable -Name GeneratorAppDataObservationSha256 -Scope 0 -ErrorAction SilentlyContinue
if ($null -eq $LockVariable -or $LockVariable.Value -isnot [string] -or
    [string]$LockVariable.Value -cnotmatch '^[0-9A-F]{64}$' -or
    $null -eq $ObserverCheckpointVariable -or $ObserverCheckpointVariable.Value -isnot [string] -or
    [string]$ObserverCheckpointVariable.Value -cnotmatch '^[0-9A-F]{64}$' -or
    $null -eq $GeneratorAppDataBase64Variable -or
    $GeneratorAppDataBase64Variable.Value -isnot [string] -or
    [string]$GeneratorAppDataBase64Variable.Value -cnotmatch '^[A-Za-z0-9+/]+={0,2}$' -or
    ([string]$GeneratorAppDataBase64Variable.Value).Length -gt 131072 -or
    $null -eq $GeneratorAppDataShaVariable -or $GeneratorAppDataShaVariable.Value -isnot [string] -or
    [string]$GeneratorAppDataShaVariable.Value -cnotmatch '^[0-9A-F]{64}$') {
    throw 'NEEDS_CONTEXT: observer post-patch out-of-band checkpoints are absent or malformed.'
}
$ApprovalLockSha256 = [string]$LockVariable.Value
$ObserverPatchCheckpointSha256 = [string]$ObserverCheckpointVariable.Value
$GeneratorAppDataObservationBase64 = [string]$GeneratorAppDataBase64Variable.Value
$GeneratorAppDataObservationSha256 = [string]$GeneratorAppDataShaVariable.Value
$ObserverBootstrapLockPath = 'C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\work\CourtOfShadows-governance-winter\.superpowers\sdd\terminal-collapse-ending\approved-plan-lock-v3.json'
if (-not (Test-Path -LiteralPath $ObserverBootstrapLockPath -PathType Leaf)) {
    throw 'NEEDS_CONTEXT: observer post-patch known approval lock leaf is missing.'
}
if ((Get-FileHash -LiteralPath $ObserverBootstrapLockPath -Algorithm SHA256).Hash -cne $ApprovalLockSha256) {
    throw 'NEEDS_CONTEXT: observer post-patch out-of-band lock authentication failed.'
}
$StrictUtf8 = New-Object Text.UTF8Encoding($false,$true)
$ObserverBootstrapLockBytes = [IO.File]::ReadAllBytes($ObserverBootstrapLockPath)
if (($ObserverBootstrapLockBytes.Length -ge 3 -and $ObserverBootstrapLockBytes[0] -eq 0xEF -and
        $ObserverBootstrapLockBytes[1] -eq 0xBB -and $ObserverBootstrapLockBytes[2] -eq 0xBF) -or
    -not (Get-Item -LiteralPath $ObserverBootstrapLockPath).IsReadOnly) {
    throw 'NEEDS_CONTEXT: authenticated observer post-patch lock has invalid bytes or mutability.'
}
$ObserverBootstrapLockText = $StrictUtf8.GetString($ObserverBootstrapLockBytes)
$ObserverBootstrapApproval = $ObserverBootstrapLockText | ConvertFrom-Json -ErrorAction Stop
$ProjectRoot = (Resolve-Path -LiteralPath '.').Path
$ObserverExpectedProjectRoot = Split-Path (Split-Path (Split-Path (Split-Path $ObserverBootstrapLockPath -Parent) -Parent) -Parent) -Parent
if ([IO.Path]::GetFullPath($ProjectRoot).TrimEnd('\') -cne [IO.Path]::GetFullPath($ObserverExpectedProjectRoot).TrimEnd('\')) {
    throw 'NEEDS_CONTEXT: observer post-patch current directory is not the lock-owned repository.'
}
git check-ignore -q -- $ObserverBootstrapLockPath
if ($LASTEXITCODE -ne 0) { throw 'NEEDS_CONTEXT: authenticated observer post-patch lock is not ignored.' }
$ObserverBootstrapPlanPath = Join-Path $ProjectRoot 'docs\superpowers\plans\2026-08-14-terminal-collapse-generator-recovery-v3.md'
if ($ObserverBootstrapApproval.plan_sha256 -isnot [string] -or
    (Get-FileHash -LiteralPath $ObserverBootstrapPlanPath -Algorithm SHA256).Hash -cne
        [string]$ObserverBootstrapApproval.plan_sha256) {
    throw 'NEEDS_CONTEXT: cannot authenticate the plan carrying observer post-patch code.'
}
$ObserverBootstrapPlanBytes = [IO.File]::ReadAllBytes($ObserverBootstrapPlanPath)
if ($ObserverBootstrapPlanBytes.Length -ge 3 -and $ObserverBootstrapPlanBytes[0] -eq 0xEF -and
    $ObserverBootstrapPlanBytes[1] -eq 0xBB -and $ObserverBootstrapPlanBytes[2] -eq 0xBF) {
    throw 'NEEDS_CONTEXT: authenticated observer post-patch plan unexpectedly has a BOM.'
}
$BootstrapPlanText = $StrictUtf8.GetString($ObserverBootstrapPlanBytes)
function Get-AuthenticatedPlanBlock([string]$BeginMarker,[string]$EndMarker) {
    $BeginToken = '# ' + $BeginMarker
    $EndToken = '# ' + $EndMarker
    $Begin = $BootstrapPlanText.IndexOf($BeginToken,[StringComparison]::Ordinal)
    $End = $BootstrapPlanText.IndexOf($EndToken,[StringComparison]::Ordinal)
    if ($Begin -lt 0 -or $End -le $Begin -or
        $BootstrapPlanText.IndexOf($BeginToken,$Begin + $BeginToken.Length,[StringComparison]::Ordinal) -ge 0 -or
        $BootstrapPlanText.IndexOf($EndToken,$End + $EndToken.Length,[StringComparison]::Ordinal) -ge 0) {
        throw ('NEEDS_CONTEXT: authenticated observer plan block markers are not unique: ' + $BeginMarker)
    }
    return $BootstrapPlanText.Substring($Begin + $BeginToken.Length,$End - ($Begin + $BeginToken.Length))
}
$Task1BootstrapPhase = 'POST_OBSERVER_PATCH'
. ([ScriptBlock]::Create((Get-AuthenticatedPlanBlock 'TASK1_V3_BOOTSTRAP_BEGIN' 'TASK1_V3_BOOTSTRAP_END')))
. ([ScriptBlock]::Create((Get-AuthenticatedPlanBlock 'TASK1_V3_PRODUCTION_VALIDATORS_BEGIN' 'TASK1_V3_PRODUCTION_VALIDATORS_END')))
. $HeadlessWrapper
if (-not (Get-Command Invoke-PrivateDesktopProcess -CommandType Function -ErrorAction SilentlyContinue)) {
    throw 'NEEDS_CONTEXT: sealed wrapper is unavailable in observer post-patch scope.'
}
. ([ScriptBlock]::Create((Get-AuthenticatedPlanBlock 'TASK1_V3_RUNTIME_HELPERS_CORE_BEGIN' 'TASK1_V3_RUNTIME_HELPERS_CORE_END')))
. ([ScriptBlock]::Create((Get-AuthenticatedPlanBlock 'TASK1_V3_RUNTIME_HELPERS_INVENTORY_BEGIN' 'TASK1_V3_RUNTIME_HELPERS_INVENTORY_END')))
. ([ScriptBlock]::Create((Get-AuthenticatedPlanBlock 'TASK1_V3_RUNTIME_READERS_BEGIN' 'TASK1_V3_RUNTIME_READERS_END')))
Assert-RecoveryAuthorityUnchanged 'observer post-patch fresh scope'
$GeneratorAppDataObservation = Read-V3SealedJsonHandoff $GeneratorAppDataObservationBase64 `
    $GeneratorAppDataObservationSha256 'observer-scope generator AppData observation'
Assert-V3GeneratorAppDataObservation $GeneratorAppDataObservation 'observer-scope generator handoff'

$GeneratorSnapshot = Read-V3GeneratorSnapshot $ObserverPatchCheckpointSha256
$PersistedGeneratorCompletion = $GeneratorSnapshot.completion
$GeneratorCompletionSha256 = [string]$GeneratorSnapshot.completion_seal.sha256
$GeneratorAttemptSha256 = [string]$GeneratorSnapshot.attempt_seal.sha256
$LegacyMarker = [string]$GeneratorSnapshot.marker
$ExternalHash = [string]$PersistedGeneratorCompletion.save_sha256
$ObserverFixturePath = Join-Path $ObserverRoot 'game\zz_terminal_collapse_legacy_observer.rpy'
$ObserverFixtureRelative = 'game/zz_terminal_collapse_legacy_observer.rpy'
$ObserverLocalSaves = Join-Path $ObserverRoot 'game\saves'
if ((& git -C $ObserverRoot rev-parse HEAD).Trim() -cne $P3 -or
    (& git -C $ObserverRoot rev-parse 'HEAD:game').Trim() -cne $GameTree) {
    throw 'NEEDS_CONTEXT: observer worktree baseline drifted across host apply_patch.'
}
$ObserverStatus = @(git -C $ObserverRoot status --short --untracked-files=all)
if ($ObserverStatus.Count -ne 1 -or $ObserverStatus[0] -cne ('?? ' + $ObserverFixtureRelative) -or
    @(git -C $ObserverRoot diff --name-only).Count -ne 0 -or
    (Test-Path -LiteralPath $ObserverLocalSaves) -or (Test-Path -LiteralPath $ObserverSaveDir)) {
    throw ('Observer worktree scope is not exactly its state-read-only fixture: ' + ($ObserverStatus -join '; '))
}
$PatchBeginToken = '<!-- TASK1_V3_OBSERVER_PATCH_' + 'BEGIN -->'
$PatchEndToken = '<!-- TASK1_V3_OBSERVER_PATCH_' + 'END -->'
$PatchBegin = $BootstrapPlanText.IndexOf($PatchBeginToken,[StringComparison]::Ordinal)
$PatchEnd = $BootstrapPlanText.IndexOf($PatchEndToken,[StringComparison]::Ordinal)
if ($PatchBegin -lt 0 -or $PatchEnd -le $PatchBegin -or
    $BootstrapPlanText.IndexOf($PatchBeginToken,$PatchBegin + $PatchBeginToken.Length,[StringComparison]::Ordinal) -ge 0 -or
    $BootstrapPlanText.IndexOf($PatchEndToken,$PatchEnd + $PatchEndToken.Length,[StringComparison]::Ordinal) -ge 0) {
    throw 'NEEDS_CONTEXT: authenticated observer fixture patch markers are not unique.'
}
$PatchSlice = $BootstrapPlanText.Substring($PatchBegin + $PatchBeginToken.Length,
    $PatchEnd - ($PatchBegin + $PatchBeginToken.Length))
$ExpectedObserverFixtureLines = @($PatchSlice -split "`r?`n" | Where-Object {
    $_.StartsWith('+',[StringComparison]::Ordinal)
} | ForEach-Object { $_.Substring(1) })
if ($ExpectedObserverFixtureLines.Count -lt 100 -or $ExpectedObserverFixtureLines[0] -cne 'init -1000 python:') {
    throw 'NEEDS_CONTEXT: authenticated plan did not yield the reviewed observer fixture payload.'
}
$ExpectedObserverFixtureBytes = $StrictUtf8.GetBytes(($ExpectedObserverFixtureLines -join "`n") + "`n")
$CurrentObserverFixtureBytes = [IO.File]::ReadAllBytes($ObserverFixturePath)
if ($CurrentObserverFixtureBytes.Length -ne $ExpectedObserverFixtureBytes.Length -or
    [Convert]::ToBase64String($CurrentObserverFixtureBytes) -cne
        [Convert]::ToBase64String($ExpectedObserverFixtureBytes)) {
    throw 'NEEDS_CONTEXT: host apply_patch bytes differ from the authenticated observer fixture payload.'
}
$ObserverFixtureSeal = New-FileSeal $ObserverFixturePath
if ($ObserverFixtureSeal.sha256 -cne (Get-V3BytesSha256 $ExpectedObserverFixtureBytes)) {
    throw 'NEEDS_CONTEXT: observer fixture seal differs from authenticated payload bytes.'
}
[IO.Directory]::CreateDirectory($ObserverSaveDir) | Out-Null
$ReplaySavePath = Join-Path $ObserverSaveDir ([string]$PersistedGeneratorCompletion.save_name)
Copy-CreateOnlyFile ([string]$PersistedGeneratorCompletion.external_save_path) $ReplaySavePath
$SourceSavePath = Get-CanonicalPath ([string]$PersistedGeneratorCompletion.external_save_path)
$SourceSaveBytes = [int64](Get-Item -LiteralPath $SourceSavePath).Length
$SourceSaveHashBefore = (Get-FileHash -LiteralPath $SourceSavePath -Algorithm SHA256).Hash
$ReplaySaveBytes = [int64](Get-Item -LiteralPath $ReplaySavePath).Length
$ReplaySaveHashBefore = (Get-FileHash -LiteralPath $ReplaySavePath -Algorithm SHA256).Hash
$ObserverPreRunTree = Get-RecoveryNonFollowingTree $ObserverSaveDir $false 'observer pre-run targets'
$ObserverPreRunTargetPaths = [string[]]@($ObserverPreRunTree.files | Where-Object {
    (Split-Path $_ -Leaf) -like '1-1-*.save'
})
[Array]::Sort($ObserverPreRunTargetPaths,[StringComparer]::Ordinal)
if ($SourceSaveBytes -ne [int64]$PersistedGeneratorCompletion.save_bytes -or
    $ReplaySaveBytes -ne $SourceSaveBytes -or
    $SourceSaveHashBefore -cne [string]$PersistedGeneratorCompletion.save_sha256 -or
    $ReplaySaveHashBefore -cne $SourceSaveHashBefore -or
    $ObserverPreRunTargetPaths.Count -ne 1 -or
    (Get-CanonicalPath (Split-Path $ObserverPreRunTargetPaths[0] -Parent)) -cne
        (Get-CanonicalPath $ObserverSaveDir) -or
    (Test-Path -LiteralPath $ObserverLocalSaves)) {
    throw 'NEEDS_CONTEXT: observer replay copy is not the exact fresh generator source.'
}
Assert-ByteEqual $SourceSavePath $ReplaySavePath 'generator source/observer replay before run'
# TASK1_V3_OBSERVER_REENTRY_END
```

Expected: a clean P3 observer worktree contains only the exact state-read-only `zz` fixture. Its external SaveDir recursively contains one root target, no `sync/` shadow target, and local `game/saves` has no target. The replay is byte-identical to all three fresh v3 generator targets; legacy/v2 candidates are never read or copied.

- [ ] **Step 9: Consume the only observer opportunity with its create-new ledger**

```powershell
if (Test-Path -LiteralPath $ObserverAttemptDir) {
    throw 'NEEDS_CONTEXT: the only recovery observer opportunity is already consumed; do not retry.'
}
Assert-RecoveryAuthorityUnchanged 'before observer attempt ledger'
[IO.Directory]::CreateDirectory($ObserverAttemptDir) | Out-Null
git check-ignore -q -- $ObserverAttemptDir
if ($LASTEXITCODE -ne 0) { throw 'Observer attempt ledger is not ignored.' }
$ObserverAttemptId = [Guid]::NewGuid().ToString('N')
if ($ObserverAttemptId -cnotmatch '^[0-9a-f]{32}$') { throw 'Observer attempt ID shape failed.' }
$ObserverAttemptProperties = @(
    'schema_version','attempt_id','started_utc','approval_lock_sha256','approved_plan_commit',
    'generator_completion_path','generator_completion_sha256','worktree_path','savedir_path',
    'process_evidence_dir','state_path','fixture_path','fixture_sha256','source_save_path',
    'source_save_bytes','source_save_sha256','replay_save_path','max_observer_invocations','retry_allowed'
)
$ObserverAttemptPayload = [ordered]@{
    schema_version = 2
    attempt_id = $ObserverAttemptId
    started_utc = [DateTime]::UtcNow.ToString('o', [Globalization.CultureInfo]::InvariantCulture)
    approval_lock_sha256 = $ApprovalLockSha256
    approved_plan_commit = $P3
    generator_completion_path = Get-CanonicalPath $GeneratorCompletionPath
    generator_completion_sha256 = $GeneratorCompletionSha256
    worktree_path = Get-CanonicalPath $ObserverRoot
    savedir_path = Get-CanonicalPath $ObserverSaveDir
    process_evidence_dir = Get-CanonicalPath $ObserverProcessEvidence
    state_path = Get-CanonicalPath $ObserverStatePath
    fixture_path = Get-CanonicalPath $ObserverFixturePath
    fixture_sha256 = [string]$ObserverFixtureSeal.sha256
    source_save_path = $SourceSavePath
    source_save_bytes = $SourceSaveBytes
    source_save_sha256 = $SourceSaveHashBefore
    replay_save_path = Get-CanonicalPath $ReplaySavePath
    max_observer_invocations = 1
    retry_allowed = $false
}
$ObserverAttempt = New-ReadOnlyJsonRecord $ObserverAttemptPath $ObserverAttemptPayload $ObserverAttemptProperties 'observer attempt'
if ($ObserverAttempt.schema_version -isnot [int] -or $ObserverAttempt.schema_version -ne 2 -or
    $ObserverAttempt.attempt_id -isnot [string] -or $ObserverAttempt.attempt_id -cne $ObserverAttemptId -or
    -not (Test-RoundtripUtc $ObserverAttempt.started_utc) -or
    $ObserverAttempt.max_observer_invocations -isnot [int] -or $ObserverAttempt.max_observer_invocations -ne 1 -or
    $ObserverAttempt.retry_allowed -isnot [bool] -or $ObserverAttempt.retry_allowed -or
    $ObserverAttempt.generator_completion_sha256 -isnot [string] -or
    $ObserverAttempt.generator_completion_sha256 -cne $GeneratorCompletionSha256 -or
    $ObserverAttempt.source_save_sha256 -isnot [string] -or $ObserverAttempt.source_save_sha256 -cne $ExternalHash) {
    throw 'NEEDS_CONTEXT: observer attempt strict reread failed.'
}
$ObserverAttemptSha256 = (Get-FileHash -LiteralPath $ObserverAttemptPath -Algorithm SHA256).Hash
```

Expected: `observer-attempt/` exists exactly once and its flushed read-only attempt binds the generator completion, clean worktree, source/replay paths, source bytes/hash, and invocation limit one. From this point any observer failure is terminal and preserves all recovery paths.

- [ ] **Step 10: Launch the ordinary `run` observer exactly once**

```powershell
$PersistedObserverAttempt = Read-RecoveryStrictJson $ObserverAttemptPath 'observer attempt before launch'
Assert-ExactProperties $PersistedObserverAttempt $ObserverAttemptProperties 'observer attempt before launch'
if (-not (Get-Item -LiteralPath $ObserverAttemptPath).IsReadOnly -or
    (Get-FileHash -LiteralPath $ObserverAttemptPath -Algorithm SHA256).Hash -cne $ObserverAttemptSha256 -or
    (Get-FileHash -LiteralPath $GeneratorCompletionPath -Algorithm SHA256).Hash -cne [string]$PersistedObserverAttempt.generator_completion_sha256 -or
    (Get-FileHash -LiteralPath $ObserverFixturePath -Algorithm SHA256).Hash -cne [string]$PersistedObserverAttempt.fixture_sha256 -or
    (Get-FileHash -LiteralPath $SourceSavePath -Algorithm SHA256).Hash -cne [string]$PersistedObserverAttempt.source_save_sha256 -or
    (Get-FileHash -LiteralPath $ReplaySavePath -Algorithm SHA256).Hash -cne [string]$PersistedObserverAttempt.source_save_sha256 -or
    (Test-Path -LiteralPath $ObserverProcessEvidence) -or (Test-Path -LiteralPath $ObserverStatePath) -or
    (Test-Path -LiteralPath $ObserverLocalSaves)) {
    throw 'NEEDS_CONTEXT: observer launch preconditions drifted after ledger creation.'
}
Assert-RecoveryAuthorityUnchanged 'before the sole observer launch'
$ObserverEnvironment = New-PrivateRenPyEnvironment @{
    'RENPY_AUTO_LOAD' = '1-1'
    'TC_OBSERVER_RESULT' = Get-CanonicalPath $ObserverStatePath
    'TC_EXPECTED_MARKER' = $LegacyMarker
    'TC_EXPECTED_BASELINE_COMMIT' = $P3
    'TC_EXPECTED_GAME_TREE' = $GameTree
    'TC_EXPECTED_SAVEDIR' = Get-CanonicalPath $ObserverSaveDir
    'TC_EXPECTED_FIXTURE_SHA256' = [string]$ObserverAttempt.fixture_sha256
}

# Sole observer invocation. This is an ordinary run, never test mode.
$ObserverAppDataBefore = Get-V3BoundedAppDataBackupSnapshot `
    $ObserverAppDataBackupPath 'immediately before sole observer invocation'
$ObserverRun = Invoke-PrivateDesktopProcess `
    -FilePath $RenPyExe `
    -ArgumentList @($ObserverRoot, 'run', '--savedir', $ObserverSaveDir) `
    -WorkingDirectory $ObserverRoot `
    -EnvironmentOverrides $ObserverEnvironment `
    -TimeoutSeconds 120 `
    -EvidenceDirectory $ObserverProcessEvidence `
    -RunnerSource $RunnerSource
Assert-PrivateDesktopCompletion $ObserverRun 0 'recovery normal-run observer'
$ObserverAppDataAfter = Get-V3BoundedAppDataBackupSnapshot `
    $ObserverAppDataBackupPath 'immediately after sole observer invocation'
```

Expected: this is the only observer invocation. It is `run`, not `test`, and passes the same private-desktop safety envelope with helper/root exit 0, no timeout, zero windows, full drain, and cleanup. Any other outcome forbids mother creation and cleanup.

- [ ] **Step 11: Validate immutable replay, state, log, request seal, and observer completion**

```powershell
$ObserverRequestPath = Join-Path $ObserverProcessEvidence 'request.json'
$ObserverStdoutPath = Join-Path $ObserverProcessEvidence 'stdout.txt'
$ObserverStderrPath = Join-Path $ObserverProcessEvidence 'stderr.txt'
$ObserverResultPath = Join-Path $ObserverProcessEvidence 'result.json'
foreach ($HelperLeaf in @($ObserverRequestPath,$ObserverStdoutPath,$ObserverStderrPath,$ObserverResultPath)) {
    if (-not (Test-Path -LiteralPath $HelperLeaf -PathType Leaf)) {
        throw ('NEEDS_CONTEXT: observer helper evidence is incomplete: ' + $HelperLeaf)
    }
}
$PersistedObserverResult = Read-HelperJson $ObserverResultPath 'observer helper result'
Assert-ExactProperties $PersistedObserverResult @(
    'schema_version','classification','detail','started','root_pid','root_exit_code','timed_out',
    'job_drained','desktop_name','process_ids','new_process_ids','active_snapshot_process_ids',
    'job_total_processes','observed_distinct_process_id_count','process_id_accounting_kind',
    'private_desktop_initially_empty','monitor_armed_before_create','monitor_armed_before_resume',
    'monitor_armed_utc','process_created_utc','resumed_utc','root_assigned_to_job_before_resume',
    'job_breakaway_forbidden','job_active_processes_final','monitor_completed_after_job_drain',
    'cleanup_complete','cleanup_errors','visible_windows','started_utc','finished_utc',
    'elapsed_milliseconds','stdout_path','stderr_path','process_diagnostic_errors',
    'host_termination_required','helper_exit_code','job_kill_on_close_verified','job_handle_non_inheritable'
) 'observer helper result schema v2'
Assert-PrivateDesktopCompletion $PersistedObserverResult 0 'persisted recovery observer'
if ((Get-CanonicalPath ([string]$PersistedObserverResult.stdout_path)) -cne (Get-CanonicalPath $ObserverStdoutPath) -or
    (Get-CanonicalPath ([string]$PersistedObserverResult.stderr_path)) -cne (Get-CanonicalPath $ObserverStderrPath)) {
    throw 'NEEDS_CONTEXT: observer helper result points outside its evidence root.'
}
$ObserverRequest = Read-HelperJson $ObserverRequestPath 'observer helper request'
Assert-ExactProperties $ObserverRequest @(
    'schema_version','executable','arguments','working_directory','environment_overrides',
    'timeout_milliseconds','stdout_path','stderr_path','result_path'
) 'observer helper request'
$ObserverRequestExpected = [pscustomobject][ordered]@{
    executable=(Get-CanonicalPath $RenPyExe)
    arguments=[object[]]@((Get-CanonicalPath $ObserverRoot),'run','--savedir',(Get-CanonicalPath $ObserverSaveDir))
    working_directory=(Get-CanonicalPath $ObserverRoot); environment_names=[object[]]$ObserverEnvironmentNames
    environment_values=[object[]]@(
        '1-1','1',$null,'sw','dummy','dummy',$P3,[string]$ObserverAttempt.fixture_sha256,
        $GameTree,$LegacyMarker,(Get-CanonicalPath $ObserverSaveDir),(Get-CanonicalPath $ObserverStatePath)
    )
    timeout_milliseconds=[int64]120000; stdout_path=(Get-CanonicalPath $ObserverStdoutPath)
    stderr_path=(Get-CanonicalPath $ObserverStderrPath); result_path=(Get-CanonicalPath $ObserverResultPath)
}
if ((Test-V3RequestContract 'observer' $ObserverRequest $ObserverRequestExpected) -cne 'ACCEPT') {
    throw 'NEEDS_CONTEXT: helper request did not bind the attempt fixture and isolated normal run.'
}

if (-not (Test-Path -LiteralPath $ObserverStatePath -PathType Leaf)) {
    throw 'NEEDS_CONTEXT: observer state result is missing.'
}
$ObserverState = Read-RecoveryStrictJson $ObserverStatePath 'observer state'
$FreshGeneratorStateForObserver = Read-RecoveryStrictJson ([string]$PersistedGeneratorCompletion.state_path) `
    'generator state for observer state comparison'
if ((Test-V3GeneratorStateContract $FreshGeneratorStateForObserver `
        ([string]$PersistedGeneratorCompletion.savedir_path) $LegacyMarker $P3 $GameTree) -cne 'ACCEPT' -or
    (Test-V3ObserverStateContract $ObserverState (Get-CanonicalPath $ObserverSaveDir) `
        $LegacyMarker $P3 $GameTree $FreshGeneratorStateForObserver.slot_metadata) -cne 'ACCEPT') {
    throw ('NEEDS_CONTEXT: ordinary-run observer state failed: ' + [string]$ObserverState.reason)
}
(Get-Item -LiteralPath $ObserverStatePath).IsReadOnly = $true
if (-not (Get-Item -LiteralPath $ObserverStatePath).IsReadOnly) { throw 'Could not freeze observer state.' }
$SourceSaveHashAfter = (Get-FileHash -LiteralPath $SourceSavePath -Algorithm SHA256).Hash
$ReplaySaveHashAfter = (Get-FileHash -LiteralPath $ReplaySavePath -Algorithm SHA256).Hash
if ((Get-Item -LiteralPath $SourceSavePath).Length -ne $SourceSaveBytes -or
    (Get-Item -LiteralPath $ReplaySavePath).Length -ne $ReplaySaveBytes -or
    $SourceSaveHashAfter -cne $SourceSaveHashBefore -or
    $ReplaySaveHashAfter -cne $ReplaySaveHashBefore -or
    $SourceSaveHashAfter -cne $ReplaySaveHashAfter) {
    throw 'NEEDS_CONTEXT: source or replay save changed during observer run.'
}
Assert-ByteEqual $SourceSavePath $ReplaySavePath 'generator source/observer replay after run'
$ObserverExternalTree = Get-RecoveryNonFollowingTree $ObserverSaveDir $false 'observer external targets'
$ObserverLocalTree = Get-RecoveryNonFollowingTree $ObserverLocalSaves $true 'observer local targets'
$ObserverTargetPaths = [string[]]@(
    @($ObserverExternalTree.files | Where-Object { (Split-Path $_ -Leaf) -like '1-1-*.save' }) +
    @($ObserverLocalTree.files | Where-Object { (Split-Path $_ -Leaf) -like '1-1-*.save' })
)
[Array]::Sort($ObserverTargetPaths,[StringComparer]::Ordinal)
$ObserverAllTargets = @($ObserverTargetPaths | ForEach-Object { Get-Item -LiteralPath $_ -Force -ErrorAction Stop })
if ($ObserverAllTargets.Count -ne 1 -or
    (Get-CanonicalPath $ObserverAllTargets[0].FullName) -cne (Get-CanonicalPath $ReplaySavePath) -or
    (Get-CanonicalPath $ObserverAllTargets[0].DirectoryName) -cne (Get-CanonicalPath $ObserverSaveDir)) {
    throw 'NEEDS_CONTEXT: observer must retain exactly one external-root replay and no sync/local target.'
}

$ObserverLogPath = Join-Path $ObserverRoot 'log.txt'
$ObserverStdoutSeal = New-FileSeal $ObserverStdoutPath
$ObserverStderrSeal = New-FileSeal $ObserverStderrPath
if (-not (Test-Path -LiteralPath $ObserverLogPath -PathType Leaf)) {
    throw 'NEEDS_CONTEXT: observer engine_boot_log is missing.'
}
Copy-CreateOnlyFile $ObserverFixturePath $ObserverFixtureEvidence
Copy-CreateOnlyFile $ObserverLogPath $ObserverLogEvidence
Assert-ByteEqual $ObserverFixturePath $ObserverFixtureEvidence 'observer fixture durable copy'
Assert-ByteEqual $ObserverLogPath $ObserverLogEvidence 'observer log durable copy'
foreach ($FrozenCopy in @($ObserverFixtureEvidence,$ObserverLogEvidence)) {
    (Get-Item -LiteralPath $FrozenCopy).IsReadOnly = $true
    if (-not (Get-Item -LiteralPath $FrozenCopy).IsReadOnly) { throw ('Could not freeze durable observer evidence: ' + $FrozenCopy) }
}
$ObserverFixtureEvidenceHash = (Get-FileHash -LiteralPath $ObserverFixtureEvidence -Algorithm SHA256).Hash
$ObserverLogHash = (Get-FileHash -LiteralPath $ObserverLogPath -Algorithm SHA256).Hash
$ObserverLogEvidenceHash = (Get-FileHash -LiteralPath $ObserverLogEvidence -Algorithm SHA256).Hash
if ($ObserverFixtureEvidenceHash -cne [string]$ObserverAttempt.fixture_sha256 -or
    $ObserverLogEvidenceHash -cne $ObserverLogHash) {
    throw 'NEEDS_CONTEXT: durable observer fixture/log seals differ from runtime sources.'
}
$ObserverSaveInventory = New-SaveInventory $ObserverSaveDir $ObserverLocalSaves 1
if (@($ObserverSaveInventory.files | Where-Object {
    $_.kind -cne 'target' -and $_.kind -cne 'persistent'
}).Count -ne 0 -or
    @($ObserverSaveInventory.files | Where-Object { $_.kind -ceq 'target' }).Count -ne 1) {
    throw 'NEEDS_CONTEXT: observer save inventory contains autosave/unexpected byproducts or wrong target count.'
}
(Get-Item -LiteralPath $ReplaySavePath).IsReadOnly = $true
if (-not (Get-Item -LiteralPath $ReplaySavePath).IsReadOnly -or
    (Get-FileHash -LiteralPath $ReplaySavePath -Algorithm SHA256).Hash -cne $ReplaySaveHashAfter) {
    throw 'NEEDS_CONTEXT: observer replay did not freeze with its before/after seal.'
}
foreach ($FrozenObserverLeaf in @(
    $ObserverRequestPath,$ObserverStdoutPath,$ObserverStderrPath,$ObserverResultPath,$ObserverStatePath
)) {
    (Get-Item -LiteralPath $FrozenObserverLeaf).IsReadOnly = $true
    if (-not (Get-Item -LiteralPath $FrozenObserverLeaf).IsReadOnly) {
        throw ('Could not freeze observer process/state evidence: ' + $FrozenObserverLeaf)
    }
}
$ObserverRequestSeal = New-FileSeal $ObserverRequestPath
$ObserverResultSeal = New-FileSeal $ObserverResultPath
$ObserverStateSeal = New-FileSeal $ObserverStatePath
$ObserverAttemptSeal = New-FileSeal $ObserverAttemptPath
$ObserverFixtureSeal = New-FileSeal $ObserverFixturePath
$ObserverFixtureEvidenceSeal = New-FileSeal $ObserverFixtureEvidence
$ObserverLogEvidenceSeal = New-FileSeal $ObserverLogEvidence
$ObserverChannelEnvelope = [pscustomobject][ordered]@{
    stdout_exists=$true; stdout_path=(Get-CanonicalPath $ObserverStdoutPath)
    request_stdout_path=(Get-CanonicalPath ([string]$ObserverRequest.stdout_path)
    ); result_stdout_path=(Get-CanonicalPath ([string]$PersistedObserverResult.stdout_path)
    ); stdout_bytes=[IO.File]::ReadAllBytes($ObserverStdoutPath)
    stderr_exists=$true; stderr_bytes=[IO.File]::ReadAllBytes($ObserverStderrPath)
    engine_exists=$true; engine_source_path=(Get-CanonicalPath $ObserverLogPath)
    engine_bytes=[IO.File]::ReadAllBytes($ObserverLogPath)
    engine_evidence_seal=$ObserverLogEvidenceSeal
}
if ((Test-V3ChannelContract 'observer' $ObserverChannelEnvelope) -cne 'ACCEPT') {
    throw 'NEEDS_CONTEXT: live observer channel contract rejected current process/log evidence.'
}
$ObserverCompletionPayload = [ordered]@{
    schema_version = 2
    attempt_id = $ObserverAttemptId
    attempt_path = Get-CanonicalPath $ObserverAttemptPath
    attempt_sha256 = $ObserverAttemptSha256
    approval_lock_sha256 = $ApprovalLockSha256
    approved_plan_commit = $P3
    generator_completion_sha256 = $GeneratorCompletionSha256
    worktree_path = Get-CanonicalPath $ObserverRoot
    savedir_path = Get-CanonicalPath $ObserverSaveDir
    process_evidence_dir = Get-CanonicalPath $ObserverProcessEvidence
    fixture_path = Get-CanonicalPath $ObserverFixturePath
    fixture_sha256 = [string]$ObserverAttempt.fixture_sha256
    fixture_evidence_path = [string]$ObserverFixtureEvidenceSeal.path
    fixture_evidence_sha256 = [string]$ObserverFixtureEvidenceSeal.sha256
    request_path = [string]$ObserverRequestSeal.path
    request_bytes = [int64]$ObserverRequestSeal.bytes
    request_sha256 = [string]$ObserverRequestSeal.sha256
    result_path = [string]$ObserverResultSeal.path
    result_bytes = [int64]$ObserverResultSeal.bytes
    result_sha256 = [string]$ObserverResultSeal.sha256
    state_path = [string]$ObserverStateSeal.path
    state_bytes = [int64]$ObserverStateSeal.bytes
    state_sha256 = [string]$ObserverStateSeal.sha256
    stdout_path = [string]$ObserverStdoutSeal.path
    stdout_bytes = [int64]$ObserverStdoutSeal.bytes
    stdout_sha256 = [string]$ObserverStdoutSeal.sha256
    stderr_path = [string]$ObserverStderrSeal.path
    stderr_bytes = [int64]$ObserverStderrSeal.bytes
    stderr_sha256 = [string]$ObserverStderrSeal.sha256
    engine_log_evidence_path = [string]$ObserverLogEvidenceSeal.path
    engine_log_evidence_sha256 = [string]$ObserverLogEvidenceSeal.sha256
    source_save_path = $SourceSavePath
    source_save_bytes = $SourceSaveBytes
    source_save_sha256_before = $SourceSaveHashBefore
    source_save_sha256_after = $SourceSaveHashAfter
    replay_save_path = Get-CanonicalPath $ReplaySavePath
    replay_save_bytes = $ReplaySaveBytes
    replay_save_sha256_before = $ReplaySaveHashBefore
    replay_save_sha256_after = $ReplaySaveHashAfter
    save_inventory = $ObserverSaveInventory
    finished_utc = [DateTime]::UtcNow.ToString('o', [Globalization.CultureInfo]::InvariantCulture)
}
$ObserverSourceSeal = New-FileSeal $SourceSavePath
$ObserverReplaySeal = New-FileSeal $ReplaySavePath
$ObserverCompletionExpected = [pscustomobject][ordered]@{
    attempt_id=$ObserverAttemptId; attempt_seal=$ObserverAttemptSeal; approval_lock_sha256=$ApprovalLockSha256
    approved_plan_commit=$P3; generator_completion_sha256=$GeneratorCompletionSha256
    worktree_path=(Get-CanonicalPath $ObserverRoot); savedir_path=(Get-CanonicalPath $ObserverSaveDir)
    process_evidence_dir=(Get-CanonicalPath $ObserverProcessEvidence); fixture_seal=$ObserverFixtureSeal
    fixture_evidence_seal=$ObserverFixtureEvidenceSeal; request_seal=$ObserverRequestSeal
    result_seal=$ObserverResultSeal; state_seal=$ObserverStateSeal; stdout_seal=$ObserverStdoutSeal
    stderr_seal=$ObserverStderrSeal; engine_log_evidence_seal=$ObserverLogEvidenceSeal
    source_before_seal=$ObserverSourceSeal; source_after_seal=$ObserverSourceSeal
    replay_before_seal=$ObserverReplaySeal; replay_after_seal=$ObserverReplaySeal
    save_inventory=$ObserverSaveInventory
}
if ((Test-V3ObserverCompletionContract ([pscustomobject]$ObserverCompletionPayload) $ObserverCompletionExpected) -cne 'ACCEPT') {
    throw 'NEEDS_CONTEXT: prospective observer completion failed the central 41-field contract.'
}
Assert-RecoveryAuthorityUnchanged 'before observer completion'
$ObserverCompletion = New-ReadOnlyJsonRecord $ObserverCompletionPath $ObserverCompletionPayload $ObserverCompletionProperties 'observer completion'
Assert-SaveInventoryRecord $ObserverCompletion.save_inventory 1 'observer completion'
Assert-SaveInventoryTargets -Inventory $ObserverCompletion.save_inventory `
    -ExpectedPaths ([string[]]@($ReplaySavePath)) -ExpectedBytes $ReplaySaveBytes `
    -ExpectedSha256 $ReplaySaveHashAfter -RequirePhysical $true -Context 'observer completion'
if (@($ObserverCompletion.save_inventory.files | Where-Object {
    $_.kind -cne 'target' -and $_.kind -cne 'persistent'
}).Count -ne 0) {
    throw 'NEEDS_CONTEXT: persisted observer inventory contains a forbidden non-target kind.'
}
if ((Test-V3ObserverCompletionContract $ObserverCompletion $ObserverCompletionExpected) -cne 'ACCEPT' -or
    (Test-V3ObserverRuntimeEvidenceContract $ObserverChannelEnvelope $ObserverCompletion `
        $ObserverCompletionExpected) -cne 'ACCEPT') {
    throw 'NEEDS_CONTEXT: observer completion strict reread/runtime channel relation failed.'
}
$ObserverCompletionSha256 = (Get-FileHash -LiteralPath $ObserverCompletionPath -Algorithm SHA256).Hash
```

Expected: request schema 1 has exactly nine fields and the ordered 12-entry environment; result schema 2 has exactly 38 fields and passes the safety envelope. State proves ordinary `run`, `loaded=true`, process-internal `actual.auto_load_value="1-1"`, P3/game-tree/marker/metadata, the production final Menu, state values, and two prepared tactics. Both helper streams are exactly empty; engine_boot_log has zero rpytest lines and no high-specificity fatal marker. Source/replay hashes are unchanged, the replay is frozen read-only, and recursive inventory has only that external-root target plus optional persistent files, never sync/local targets or autosaves. The exact 41-field schema-v2 observer completion is frozen.

- [ ] **Step 12: Create the only mother from the fresh generator after observer completion**

```powershell
Assert-RecoveryAuthorityUnchanged 'before mother creation'
$MotherGeneratorSnapshot = Read-V3GeneratorSnapshot $GeneratorCompletionSha256
$MotherObserverSnapshot = Read-V3ObserverSnapshot $ObserverCompletionSha256 $MotherGeneratorSnapshot
$PersistedGeneratorCompletion = $MotherGeneratorSnapshot.completion
$PersistedObserverCompletion = $MotherObserverSnapshot.completion
if ((@(
        [string]$PersistedObserverCompletion.source_save_sha256_before,
        [string]$PersistedObserverCompletion.source_save_sha256_after,
        [string]$PersistedObserverCompletion.replay_save_sha256_before,
        [string]$PersistedObserverCompletion.replay_save_sha256_after,
        [string]$PersistedGeneratorCompletion.save_sha256
) | Select-Object -Unique).Count -ne 1) {
    throw 'NEEDS_CONTEXT: generator/observer save lineage is not singular.'
}
if (Test-Path -LiteralPath $MotherDir) { throw 'NEEDS_CONTEXT: mother directory already exists; never overwrite it.' }
[IO.Directory]::CreateDirectory($MotherDir) | Out-Null
git check-ignore -q -- $MotherDir
if ($LASTEXITCODE -ne 0) { throw 'Mother directory is not ignored.' }
$MotherPath = Join-Path $MotherDir ([string]$PersistedGeneratorCompletion.save_name)
$MotherSourcePath = Get-CanonicalPath ([string]$PersistedGeneratorCompletion.external_save_path)
$MotherReplayPath = Get-CanonicalPath ([string]$PersistedObserverCompletion.replay_save_path)
Copy-CreateOnlyFile $MotherSourcePath $MotherPath
$MotherSeal = New-FileSeal $MotherPath
$MotherPhysicalTree = Get-RecoveryNonFollowingTree $MotherDir $false 'single mother physical tree'
if ($MotherSeal.bytes -ne [int64]$PersistedGeneratorCompletion.save_bytes -or
    $MotherSeal.sha256 -cne [string]$PersistedGeneratorCompletion.save_sha256 -or
    (Split-Path $MotherPath -Leaf) -cne (Split-Path $MotherReplayPath -Leaf) -or
    @($MotherPhysicalTree.files).Count -ne 1 -or
    [string]@($MotherPhysicalTree.files)[0] -cne (Get-CanonicalPath $MotherPath) -or
    @($MotherPhysicalTree.directories).Count -ne 0) {
    throw 'NEEDS_CONTEXT: mother basename/bytes/hash do not match the fresh generator and replay.'
}
Assert-ByteEqual $MotherSourcePath $MotherReplayPath 'source/replay before mother freeze'
Assert-ByteEqual ([string]$PersistedGeneratorCompletion.external_save_path) ([string]$PersistedGeneratorCompletion.sync_save_path) 'generator root/sync before mother freeze'
Assert-ByteEqual ([string]$PersistedGeneratorCompletion.external_save_path) ([string]$PersistedGeneratorCompletion.local_save_path) 'generator root/local before mother freeze'
Assert-ByteEqual $MotherSourcePath $MotherPath 'source/mother'
Assert-ByteEqual $MotherReplayPath $MotherPath 'replay/mother'
Assert-ByteEqual ([string]$PersistedGeneratorCompletion.sync_save_path) $MotherPath 'generator sync/mother'
Assert-ByteEqual ([string]$PersistedGeneratorCompletion.local_save_path) $MotherPath 'generator local/mother'
(Get-Item -LiteralPath $MotherPath).IsReadOnly = $true
if (-not (Get-Item -LiteralPath $MotherPath).IsReadOnly -or
    (Get-FileHash -LiteralPath $MotherPath -Algorithm SHA256).Hash -cne [string]$PersistedGeneratorCompletion.save_sha256) {
    throw 'NEEDS_CONTEXT: mother did not freeze read-only with the approved save seal.'
}
$GeneratorCompletionCheckpointSha256 = [string]$MotherGeneratorSnapshot.completion_seal.sha256
$ObserverCompletionCheckpointSha256 = [string]$MotherObserverSnapshot.completion_seal.sha256
$MotherCheckpointSha256 = (Get-FileHash -LiteralPath $MotherPath -Algorithm SHA256).Hash
$AppDataObservation = [pscustomobject][ordered]@{
    schema_version=1; backup_root=$AppDataBackupRoot
    generator_path=$GeneratorAppDataBackupPath
    generator_before=$GeneratorAppDataObservation.generator_before
    generator_after=$GeneratorAppDataObservation.generator_after
    generator_handoff_sha256=$GeneratorAppDataObservationSha256
    observer_path=$ObserverAppDataBackupPath
    observer_before=$ObserverAppDataBefore; observer_after=$ObserverAppDataAfter
    read_only=$true; authority=$false; cleanup_performed=$false
}
Assert-V3AppDataObservation $AppDataObservation $GeneratorAppDataObservationSha256 `
    'observer-to-cleanup AppData handoff'
$AppDataHandoff = New-V3SealedJsonHandoff $AppDataObservation 'complete AppData observation'
$AppDataObservationBase64 = [string]$AppDataHandoff.base64
$AppDataObservationSha256 = [string]$AppDataHandoff.sha256
Write-Output ('TASK1_V3_CLEANUP_GENERATOR_COMPLETION_SHA256=' + $GeneratorCompletionCheckpointSha256)
Write-Output ('TASK1_V3_CLEANUP_OBSERVER_COMPLETION_SHA256=' + $ObserverCompletionCheckpointSha256)
Write-Output ('TASK1_V3_CLEANUP_MOTHER_SHA256=' + $MotherCheckpointSha256)
Write-Output ('TASK1_V3_CLEANUP_GENERATOR_APPDATA_OBSERVATION_SHA256=' + $GeneratorAppDataObservationSha256)
Write-Output ('TASK1_V3_CLEANUP_APPDATA_OBSERVATION_BASE64=' + $AppDataObservationBase64)
Write-Output ('TASK1_V3_CLEANUP_APPDATA_OBSERVATION_SHA256=' + $AppDataObservationSha256)
```

Expected: `mother/` contains exactly one read-only save whose basename, bytes, SHA-256, and byte stream equal both the fresh generator source and observer replay. No path from the old TIMEOUT attempt participates.

- [ ] **Step 13: Remove only the four verified successful temporary paths**

The observer process ends after printing the three durable uppercase cleanup checkpoints and the bounded AppData observation handoff. Start a fourth, genuinely fresh Windows PowerShell 5.1 process. The controller binds `$ApprovalLockSha256`, `$GeneratorCompletionCheckpointSha256`, `$ObserverCompletionCheckpointSha256`, `$MotherCheckpointSha256`, the generator-observation SHA, and the complete observation base64/SHA pair. Authenticate the fixed lock leaf before reading lock bytes, resolving the repository, reading the physical plan, or decoding that non-authority observation. Run this step only after both strict completion rereads and the mother are read-only and all four durable fixture/log copies are sealed. A failed generator or observer never reaches this step.

```powershell
# TASK1_V3_CLEANUP_REENTRY_BEGIN
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
if ($PSVersionTable.PSEdition -cne 'Desktop' -or $PSVersionTable.PSVersion.Major -ne 5) {
    throw 'NEEDS_CONTEXT: cleanup scope requires Windows PowerShell 5.1 Desktop.'
}
$CleanupLockVariable = Get-Variable -Name ApprovalLockSha256 -Scope 0 -ErrorAction SilentlyContinue
$CleanupGeneratorVariable = Get-Variable -Name GeneratorCompletionCheckpointSha256 -Scope 0 -ErrorAction SilentlyContinue
$CleanupObserverVariable = Get-Variable -Name ObserverCompletionCheckpointSha256 -Scope 0 -ErrorAction SilentlyContinue
$CleanupMotherVariable = Get-Variable -Name MotherCheckpointSha256 -Scope 0 -ErrorAction SilentlyContinue
$CleanupGeneratorAppDataShaVariable = Get-Variable -Name GeneratorAppDataObservationSha256 -Scope 0 -ErrorAction SilentlyContinue
$CleanupAppDataBase64Variable = Get-Variable -Name AppDataObservationBase64 -Scope 0 -ErrorAction SilentlyContinue
$CleanupAppDataShaVariable = Get-Variable -Name AppDataObservationSha256 -Scope 0 -ErrorAction SilentlyContinue
foreach ($CheckpointSpec in @(
    [pscustomobject]@{ value=$CleanupLockVariable; label='approval lock' },
    [pscustomobject]@{ value=$CleanupGeneratorVariable; label='generator completion' },
    [pscustomobject]@{ value=$CleanupObserverVariable; label='observer completion' },
    [pscustomobject]@{ value=$CleanupMotherVariable; label='mother' },
    [pscustomobject]@{ value=$CleanupGeneratorAppDataShaVariable; label='generator AppData observation' },
    [pscustomobject]@{ value=$CleanupAppDataShaVariable; label='complete AppData observation' }
)) {
    if ($null -eq $CheckpointSpec.value -or $CheckpointSpec.value.Value -isnot [string] -or
        [string]$CheckpointSpec.value.Value -cnotmatch '^[0-9A-F]{64}$') {
        throw ('NEEDS_CONTEXT: cleanup out-of-band checkpoint is absent or malformed: ' + $CheckpointSpec.label)
    }
}
if ($null -eq $CleanupAppDataBase64Variable -or
    $CleanupAppDataBase64Variable.Value -isnot [string] -or
    [string]::IsNullOrEmpty([string]$CleanupAppDataBase64Variable.Value) -or
    ([string]$CleanupAppDataBase64Variable.Value).Length -gt 131072 -or
    [string]$CleanupAppDataBase64Variable.Value -cnotmatch '^[A-Za-z0-9+/]+={0,2}$') {
    throw 'NEEDS_CONTEXT: cleanup AppData observation base64 is absent or malformed.'
}
$ApprovalLockSha256 = [string]$CleanupLockVariable.Value
$GeneratorCompletionCheckpointSha256 = [string]$CleanupGeneratorVariable.Value
$ObserverCompletionCheckpointSha256 = [string]$CleanupObserverVariable.Value
$MotherCheckpointSha256 = [string]$CleanupMotherVariable.Value
$GeneratorAppDataObservationSha256 = [string]$CleanupGeneratorAppDataShaVariable.Value
$AppDataObservationBase64 = [string]$CleanupAppDataBase64Variable.Value
$AppDataObservationSha256 = [string]$CleanupAppDataShaVariable.Value
$CleanupBootstrapLockPath = 'C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\work\CourtOfShadows-governance-winter\.superpowers\sdd\terminal-collapse-ending\approved-plan-lock-v3.json'
if (-not (Test-Path -LiteralPath $CleanupBootstrapLockPath -PathType Leaf)) {
    throw 'NEEDS_CONTEXT: cleanup known approval lock leaf is missing.'
}
if ((Get-FileHash -LiteralPath $CleanupBootstrapLockPath -Algorithm SHA256).Hash -cne $ApprovalLockSha256) {
    throw 'NEEDS_CONTEXT: cleanup out-of-band lock authentication failed.'
}
$StrictUtf8 = New-Object Text.UTF8Encoding($false,$true)
$CleanupBootstrapLockBytes = [IO.File]::ReadAllBytes($CleanupBootstrapLockPath)
if (($CleanupBootstrapLockBytes.Length -ge 3 -and $CleanupBootstrapLockBytes[0] -eq 0xEF -and
        $CleanupBootstrapLockBytes[1] -eq 0xBB -and $CleanupBootstrapLockBytes[2] -eq 0xBF) -or
    -not (Get-Item -LiteralPath $CleanupBootstrapLockPath).IsReadOnly) {
    throw 'NEEDS_CONTEXT: authenticated cleanup lock has invalid bytes or mutability.'
}
$CleanupBootstrapLockText = $StrictUtf8.GetString($CleanupBootstrapLockBytes)
$CleanupBootstrapApproval = $CleanupBootstrapLockText | ConvertFrom-Json -ErrorAction Stop
$ProjectRoot = (Resolve-Path -LiteralPath '.').Path
$CleanupExpectedProjectRoot = Split-Path (Split-Path (Split-Path (Split-Path $CleanupBootstrapLockPath -Parent) -Parent) -Parent) -Parent
if ([IO.Path]::GetFullPath($ProjectRoot).TrimEnd('\') -cne [IO.Path]::GetFullPath($CleanupExpectedProjectRoot).TrimEnd('\')) {
    throw 'NEEDS_CONTEXT: cleanup current directory is not the lock-owned repository.'
}
git check-ignore -q -- $CleanupBootstrapLockPath
if ($LASTEXITCODE -ne 0) { throw 'NEEDS_CONTEXT: authenticated cleanup lock is not ignored.' }
$CleanupBootstrapPlanPath = Join-Path $ProjectRoot 'docs\superpowers\plans\2026-08-14-terminal-collapse-generator-recovery-v3.md'
if ($CleanupBootstrapApproval.plan_sha256 -isnot [string] -or
    (Get-FileHash -LiteralPath $CleanupBootstrapPlanPath -Algorithm SHA256).Hash -cne
        [string]$CleanupBootstrapApproval.plan_sha256) {
    throw 'NEEDS_CONTEXT: cannot authenticate the plan carrying cleanup code.'
}
$CleanupBootstrapPlanBytes = [IO.File]::ReadAllBytes($CleanupBootstrapPlanPath)
if ($CleanupBootstrapPlanBytes.Length -ge 3 -and $CleanupBootstrapPlanBytes[0] -eq 0xEF -and
    $CleanupBootstrapPlanBytes[1] -eq 0xBB -and $CleanupBootstrapPlanBytes[2] -eq 0xBF) {
    throw 'NEEDS_CONTEXT: authenticated cleanup plan unexpectedly has a BOM.'
}
$BootstrapPlanText = $StrictUtf8.GetString($CleanupBootstrapPlanBytes)
function Get-AuthenticatedPlanBlock([string]$BeginMarker,[string]$EndMarker) {
    $BeginToken = '# ' + $BeginMarker
    $EndToken = '# ' + $EndMarker
    $Begin = $BootstrapPlanText.IndexOf($BeginToken,[StringComparison]::Ordinal)
    $End = $BootstrapPlanText.IndexOf($EndToken,[StringComparison]::Ordinal)
    if ($Begin -lt 0 -or $End -le $Begin -or
        $BootstrapPlanText.IndexOf($BeginToken,$Begin + $BeginToken.Length,[StringComparison]::Ordinal) -ge 0 -or
        $BootstrapPlanText.IndexOf($EndToken,$End + $EndToken.Length,[StringComparison]::Ordinal) -ge 0) {
        throw ('NEEDS_CONTEXT: authenticated cleanup plan block markers are not unique: ' + $BeginMarker)
    }
    return $BootstrapPlanText.Substring($Begin + $BeginToken.Length,$End - ($Begin + $BeginToken.Length))
}
$Task1BootstrapPhase = 'CLEANUP'
. ([ScriptBlock]::Create((Get-AuthenticatedPlanBlock 'TASK1_V3_BOOTSTRAP_BEGIN' 'TASK1_V3_BOOTSTRAP_END')))
. ([ScriptBlock]::Create((Get-AuthenticatedPlanBlock 'TASK1_V3_PRODUCTION_VALIDATORS_BEGIN' 'TASK1_V3_PRODUCTION_VALIDATORS_END')))
. $HeadlessWrapper
if (-not (Get-Command Assert-PrivateDesktopSafetyEnvelope -CommandType Function -ErrorAction SilentlyContinue)) {
    throw 'NEEDS_CONTEXT: sealed wrapper is unavailable in cleanup scope.'
}
. ([ScriptBlock]::Create((Get-AuthenticatedPlanBlock 'TASK1_V3_RUNTIME_HELPERS_CORE_BEGIN' 'TASK1_V3_RUNTIME_HELPERS_CORE_END')))
. ([ScriptBlock]::Create((Get-AuthenticatedPlanBlock 'TASK1_V3_RUNTIME_HELPERS_INVENTORY_BEGIN' 'TASK1_V3_RUNTIME_HELPERS_INVENTORY_END')))
. ([ScriptBlock]::Create((Get-AuthenticatedPlanBlock 'TASK1_V3_RUNTIME_READERS_BEGIN' 'TASK1_V3_RUNTIME_READERS_END')))
Assert-RecoveryAuthorityUnchanged 'cleanup fresh scope'
$CleanupAppDataObservation = Read-V3SealedJsonHandoff $AppDataObservationBase64 `
    $AppDataObservationSha256 'cleanup-scope complete AppData observation'
Assert-V3AppDataObservation $CleanupAppDataObservation $GeneratorAppDataObservationSha256 `
    'cleanup-scope complete AppData handoff'

$CleanupGeneratorSnapshot = Read-V3GeneratorSnapshot $GeneratorCompletionCheckpointSha256
$CleanupObserverSnapshot = Read-V3ObserverSnapshot $ObserverCompletionCheckpointSha256 $CleanupGeneratorSnapshot
$CleanupGeneratorCompletion = $CleanupGeneratorSnapshot.completion
$CleanupObserverCompletion = $CleanupObserverSnapshot.completion
$CleanupMotherPath = Get-CanonicalPath (Join-Path $MotherDir ([string]$CleanupGeneratorCompletion.save_name))
$CleanupMotherSeal = Get-V3FrozenSeal $CleanupMotherPath $CleanupMotherPath `
    ([int64]$CleanupGeneratorCompletion.save_bytes) $MotherCheckpointSha256 'mother'
if ($CleanupMotherSeal.sha256 -cne [string]$CleanupGeneratorCompletion.save_sha256 -or
    (@(
        [string]$CleanupGeneratorCompletion.save_sha256,
        [string]$CleanupObserverCompletion.source_save_sha256_before,
        [string]$CleanupObserverCompletion.source_save_sha256_after,
        [string]$CleanupObserverCompletion.replay_save_sha256_before,
        [string]$CleanupObserverCompletion.replay_save_sha256_after,
        [string]$CleanupMotherSeal.sha256
    ) | Select-Object -Unique).Count -ne 1) {
    throw 'NEEDS_CONTEXT: fresh cleanup completion/mother lineage is not singular.'
}
$CleanupTargets = [pscustomobject][ordered]@{
    generator_worktree = [string]$CleanupGeneratorCompletion.worktree_path
    generator_savedir = [string]$CleanupGeneratorCompletion.savedir_path
    observer_worktree = [string]$CleanupObserverCompletion.worktree_path
    observer_savedir = [string]$CleanupObserverCompletion.savedir_path
}
$CleanupHardAllowlist = [pscustomobject][ordered]@{
    generator_worktree = 'E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-generator-recovery-v3'
    generator_savedir = 'E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-generator-save-recovery-v3'
    observer_worktree = 'E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-observer-recovery-v3'
    observer_savedir = 'E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-observer-save-recovery-v3'
}
Assert-ExactProperties $CleanupTargets @('generator_worktree','generator_savedir','observer_worktree','observer_savedir') `
    'completion-derived cleanup targets'
Assert-ExactProperties $CleanupHardAllowlist @('generator_worktree','generator_savedir','observer_worktree','observer_savedir') `
    'literal cleanup hard allowlist'
$CleanupTargetSet = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
foreach ($Role in @('generator_worktree','generator_savedir','observer_worktree','observer_savedir')) {
    $Candidate = $CleanupTargets.$Role
    $Allowed = $CleanupHardAllowlist.$Role
    if ($Candidate -isnot [string] -or -not [IO.Path]::IsPathRooted([string]$Candidate) -or
        [string]$Candidate -cne (Get-CanonicalPath ([string]$Candidate)) -or
        [string]$Candidate -cne (Get-CanonicalPath ([string]$Allowed)) -or
        -not $CleanupTargetSet.Add([string]$Candidate) -or
        (Get-CanonicalPath (Split-Path ([string]$Candidate) -Parent)) -cne (Get-CanonicalPath $TaskTempRoot) -or
        (Test-SameOrChildPath ([string]$Candidate) $AppDataRoamingRoot)) {
        throw ('NEEDS_CONTEXT: completion-derived cleanup target failed fixed hard allowlist: ' + $Role)
    }
}
# TASK1_V3_CLEANUP_REENTRY_END
function Assert-NoProcessReference([string[]]$Paths) {
    $References = @(
        Get-CimInstance Win32_Process -ErrorAction Stop | Where-Object {
            $Process = $_
            ([int64]$Process.ProcessId -ne [int64]$PID) -and
                (@($Paths | Where-Object {
                    ($null -ne $Process.ExecutablePath -and $Process.ExecutablePath.StartsWith($_, [StringComparison]::OrdinalIgnoreCase)) -or
                    ($null -ne $Process.CommandLine -and $Process.CommandLine.IndexOf($_, [StringComparison]::OrdinalIgnoreCase) -ge 0)
                }).Count -gt 0)
        }
    )
    if ($References.Count -ne 0) {
        throw ('A live process still references a cleanup target: ' + (($References | ForEach-Object { $_.ProcessId }) -join ','))
    }
}
function Remove-VerifiedSaveDirectory([string]$Path, [string]$ExpectedLeaf) {
    $ResolvedPath = Get-CanonicalPath $Path
    $ResolvedParent = Get-CanonicalPath (Split-Path $ResolvedPath -Parent)
    if ($ResolvedParent -cne (Get-CanonicalPath $TaskTempRoot) -or
        (Split-Path $ResolvedPath -Leaf) -cne $ExpectedLeaf -or
        -not (Test-Path -LiteralPath $ResolvedPath -PathType Container)) {
        throw ('Refusing recursive removal of unverified SaveDir: ' + $ResolvedPath)
    }

    # Prove that neither the target's path chain nor anything below it can
    # redirect recursive deletion through a junction or symbolic link.
    $TargetDirectory = Get-Item -LiteralPath $ResolvedPath -Force -ErrorAction Stop
    $PathChainItem = $TargetDirectory
    while ($null -ne $PathChainItem) {
        if (($PathChainItem.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
            throw ('Refusing recursive removal through a reparse-point path component: ' + $PathChainItem.FullName)
        }
        $PathChainItem = $PathChainItem.Parent
    }
    $PendingDirectories = New-Object 'System.Collections.Generic.Stack[System.IO.DirectoryInfo]'
    $PendingDirectories.Push([IO.DirectoryInfo]$TargetDirectory)
    while ($PendingDirectories.Count -gt 0) {
        $Directory = $PendingDirectories.Pop()
        foreach ($Child in $Directory.GetFileSystemInfos()) {
            if (($Child.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
                throw ('Refusing recursive removal because a descendant is a reparse point: ' + $Child.FullName)
            }
            if (($Child.Attributes -band [IO.FileAttributes]::Directory) -ne 0) {
                $PendingDirectories.Push([IO.DirectoryInfo]$Child)
            }
        }
    }
    Remove-Item -LiteralPath $ResolvedPath -Recurse -Force
    if (Test-Path -LiteralPath $ResolvedPath) { throw ('SaveDir remains after cleanup: ' + $ResolvedPath) }
}

foreach ($FrozenEvidence in @(
    $GeneratorAttemptPath,$GeneratorCompletionPath,$GeneratorFixtureEvidence,$GeneratorLogEvidence,
    $ObserverAttemptPath,$ObserverCompletionPath,$ObserverFixtureEvidence,$ObserverLogEvidence,$CleanupMotherPath
)) {
    if (-not (Test-Path -LiteralPath $FrozenEvidence -PathType Leaf) -or
        -not (Get-Item -LiteralPath $FrozenEvidence).IsReadOnly) {
        throw ('NEEDS_CONTEXT: fresh cleanup prerequisite is not frozen: ' + $FrozenEvidence)
    }
}
if ([string]$CleanupGeneratorSnapshot.result.classification -cne 'COMPLETED' -or
    [string]$CleanupObserverSnapshot.result.classification -cne 'COMPLETED') {
    throw 'NEEDS_CONTEXT: strict current helper results are not COMPLETED.'
}
$GeneratorFinalStatus = @(git -C ([string]$CleanupTargets.generator_worktree) status --short --untracked-files=all)
$ObserverFinalStatus = @(git -C ([string]$CleanupTargets.observer_worktree) status --short --untracked-files=all)
if ($GeneratorFinalStatus.Count -ne 1 -or
    $GeneratorFinalStatus[0] -cne '?? game/zz_terminal_collapse_legacy_fixture.rpy' -or
    $ObserverFinalStatus.Count -ne 1 -or
    $ObserverFinalStatus[0] -cne '?? game/zz_terminal_collapse_legacy_observer.rpy' -or
    (& git -C ([string]$CleanupTargets.generator_worktree) rev-parse HEAD).Trim() -cne $P3 -or
    (& git -C ([string]$CleanupTargets.generator_worktree) rev-parse 'HEAD:game').Trim() -cne $GameTree -or
    (& git -C ([string]$CleanupTargets.observer_worktree) rev-parse HEAD).Trim() -cne $P3 -or
    (& git -C ([string]$CleanupTargets.observer_worktree) rev-parse 'HEAD:game').Trim() -cne $GameTree) {
    throw 'NEEDS_CONTEXT: a completion-derived disposable worktree changed outside its permitted fixture.'
}
function Assert-NoReparseTree([string]$Path,[string]$Context) {
    $RootItem = Get-Item -LiteralPath $Path -Force -ErrorAction Stop
    $ChainItem = $RootItem
    while ($null -ne $ChainItem) {
        if (($ChainItem.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
            throw ('NEEDS_CONTEXT: reparse point in cleanup path chain ' + $Context + ': ' + $ChainItem.FullName)
        }
        $ChainItem = $ChainItem.Parent
    }
    if ($RootItem.PSIsContainer) { [void](Get-RecoveryNonFollowingTree $Path $false ('cleanup ' + $Context)) }
}
foreach ($Role in @('generator_worktree','generator_savedir','observer_worktree','observer_savedir')) {
    Assert-NoReparseTree ([string]$CleanupTargets.$Role) $Role
}
$RegisteredWorktrees = @(
    git worktree list --porcelain |
        Where-Object { $_.StartsWith('worktree ', [StringComparison]::Ordinal) } |
        ForEach-Object { Get-CanonicalPath $_.Substring(9) }
)
foreach ($RequiredWorktree in @(
    [string]$CleanupTargets.generator_worktree,[string]$CleanupTargets.observer_worktree
)) {
    if ($RegisteredWorktrees -notcontains $RequiredWorktree) {
        throw ('NEEDS_CONTEXT: cleanup target is not the exact registered worktree: ' + $RequiredWorktree)
    }
}
Assert-NoProcessReference @(
    [string]$CleanupTargets.generator_worktree,[string]$CleanupTargets.generator_savedir,
    [string]$CleanupTargets.observer_worktree,[string]$CleanupTargets.observer_savedir
)
Assert-RecoveryAuthorityUnchanged 'immediately before completion-derived cleanup'
# TASK1_V3_CLEANUP_DELETE_BEGIN
git worktree remove --force ([string]$CleanupTargets.generator_worktree)
if ($LASTEXITCODE -ne 0) { throw 'Could not remove the verified generator worktree.' }
git worktree remove --force ([string]$CleanupTargets.observer_worktree)
if ($LASTEXITCODE -ne 0) { throw 'Could not remove the verified observer worktree.' }
Remove-VerifiedSaveDirectory ([string]$CleanupTargets.generator_savedir) 'cos-terminal-collapse-generator-save-recovery-v3'
Remove-VerifiedSaveDirectory ([string]$CleanupTargets.observer_savedir) 'cos-terminal-collapse-observer-save-recovery-v3'
# TASK1_V3_CLEANUP_DELETE_END
$CleanupPostState = [pscustomobject][ordered]@{
    generator_worktree_removed = -not (Test-Path -LiteralPath ([string]$CleanupTargets.generator_worktree))
    generator_savedir_removed = -not (Test-Path -LiteralPath ([string]$CleanupTargets.generator_savedir))
    observer_worktree_removed = -not (Test-Path -LiteralPath ([string]$CleanupTargets.observer_worktree))
    observer_savedir_removed = -not (Test-Path -LiteralPath ([string]$CleanupTargets.observer_savedir))
}
if (@($CleanupPostState.PSObject.Properties.Value | Where-Object { $_ -isnot [bool] -or -not [bool]$_ }).Count -ne 0) {
    throw 'NEEDS_CONTEXT: verified successful temporary cleanup is incomplete.'
}
$RegisteredAfterCleanup = @(
    git worktree list --porcelain |
        Where-Object { $_.StartsWith('worktree ', [StringComparison]::Ordinal) } |
        ForEach-Object { Get-CanonicalPath $_.Substring(9) }
)
if ($RegisteredAfterCleanup -contains [string]$CleanupTargets.generator_worktree -or
    $RegisteredAfterCleanup -contains [string]$CleanupTargets.observer_worktree) {
    throw 'NEEDS_CONTEXT: a completion-derived worktree remains registered after cleanup.'
}
```

Expected: only the four schema-bound v3 temporary paths are removed after frozen result/completion rereads, zero process references, exact registration and reparse-point checks. No global worktree prune runs. Legacy TIMEOUT and v2 log-contract-mismatch worktrees, SaveDirs, candidates, locks, manifests, attempts, streams, and every failure leaf remain untouched.

- [ ] **Step 14: Freeze a literal baseline evidence leaf after cleanup**

```powershell
$BaselineApproval = Read-RecoveryStrictJson $ApprovalLockPath 'baseline fresh approval reread'
$BaselineManifest = Read-RecoveryStrictJson $ManifestPath 'baseline fresh predecessor reread'
$BaselineRed = Read-RecoveryStrictJson $RedRecordPath 'baseline fresh RED reread'
$BaselineGreen = Read-RecoveryStrictJson $GreenRecordPath 'baseline fresh GREEN reread'
$BaselineGeneratorAttempt = Read-RecoveryStrictJson $GeneratorAttemptPath 'baseline fresh generator attempt reread'
$BaselineGeneratorCompletion = Read-RecoveryStrictJson $GeneratorCompletionPath 'baseline fresh generator completion reread'
$BaselineObserverAttempt = Read-RecoveryStrictJson $ObserverAttemptPath 'baseline fresh observer attempt reread'
$BaselineObserverCompletion = Read-RecoveryStrictJson $ObserverCompletionPath 'baseline fresh observer completion reread'
Assert-ExactProperties $BaselineGeneratorAttempt $GeneratorAttemptProperties 'baseline generator attempt'
Assert-ExactProperties $BaselineGeneratorCompletion $GeneratorCompletionProperties 'baseline generator completion'
Assert-ExactProperties $BaselineObserverAttempt $ObserverAttemptProperties 'baseline observer attempt'
Assert-ExactProperties $BaselineObserverCompletion $ObserverCompletionProperties 'baseline observer completion'
$BaselineGeneratorWorktreePath = Get-CanonicalPath ([string]$BaselineGeneratorCompletion.worktree_path)
$BaselineGeneratorSaveDirPath = Get-CanonicalPath ([string]$BaselineGeneratorCompletion.savedir_path)
$BaselineObserverWorktreePath = Get-CanonicalPath ([string]$BaselineObserverCompletion.worktree_path)
$BaselineObserverSaveDirPath = Get-CanonicalPath ([string]$BaselineObserverCompletion.savedir_path)
$BaselineRegisteredWorktrees = @(
    git worktree list --porcelain |
        Where-Object { $_.StartsWith('worktree ', [StringComparison]::Ordinal) } |
        ForEach-Object { Get-CanonicalPath $_.Substring(9) }
)
$BaselineCleanupState = [pscustomobject][ordered]@{
    generator_worktree_removed =
        -not (Test-Path -LiteralPath $BaselineGeneratorWorktreePath) -and
        -not ($BaselineRegisteredWorktrees -contains $BaselineGeneratorWorktreePath)
    generator_savedir_removed = -not (Test-Path -LiteralPath $BaselineGeneratorSaveDirPath)
    observer_worktree_removed =
        -not (Test-Path -LiteralPath $BaselineObserverWorktreePath) -and
        -not ($BaselineRegisteredWorktrees -contains $BaselineObserverWorktreePath)
    observer_savedir_removed = -not (Test-Path -LiteralPath $BaselineObserverSaveDirPath)
}
Assert-ExactProperties $BaselineCleanupState @(
    'generator_worktree_removed','generator_savedir_removed',
    'observer_worktree_removed','observer_savedir_removed'
) 'baseline cleanup state from fresh completion rereads'
$BaselineApprovalSeal = New-FileSeal $ApprovalLockPath
$BaselineManifestSeal = New-FileSeal $ManifestPath
$BaselineRedSeal = New-FileSeal $RedRecordPath
$BaselineGreenSeal = New-FileSeal $GreenRecordPath
$BaselineGeneratorAttemptSeal = New-FileSeal $GeneratorAttemptPath
$BaselineGeneratorCompletionSeal = New-FileSeal $GeneratorCompletionPath
$BaselineObserverAttemptSeal = New-FileSeal $ObserverAttemptPath
$BaselineObserverCompletionSeal = New-FileSeal $ObserverCompletionPath
$BaselineMotherPath = Get-CanonicalPath (Join-Path $MotherDir ([string]$BaselineGeneratorCompletion.save_name))
$BaselineMotherSeal = New-FileSeal $BaselineMotherPath
if ($BaselineApprovalSeal.sha256 -cne $ApprovalLockSha256 -or
    $BaselineManifestSeal.sha256 -cne [string]$BaselineApproval.predecessor_manifest_sha256 -or
    $BaselineGeneratorCompletionSeal.sha256 -cne $GeneratorCompletionCheckpointSha256 -or
    $BaselineObserverCompletionSeal.sha256 -cne $ObserverCompletionCheckpointSha256 -or
    $BaselineMotherSeal.sha256 -cne $MotherCheckpointSha256 -or
    $BaselineMotherSeal.sha256 -cne [string]$BaselineGeneratorCompletion.save_sha256 -or
    @($BaselineCleanupState.PSObject.Properties.Value | Where-Object { $_ -isnot [bool] -or -not [bool]$_ }).Count -ne 0) {
    throw 'NEEDS_CONTEXT: baseline fresh rereads/checkpoints/cleanup state drifted.'
}
$OldFullAttemptPath = Join-Path $EvidenceRoot 'helper-v2-full-selftest-attempt\attempt.json'
$OldFullCompletionPath = Join-Path $EvidenceRoot 'helper-v2-full-selftest-attempt\completion.json'
$OldFullRoot = Join-Path $TaskTempRoot 'cos-private-desktop-selftest-409c3edd2e2c412e8e5221f4774e2448'
$OldVersionEvidence = Join-Path $EvidenceRoot 'legacy\renpy-version-process'
$OldVersionRequestPath = Join-Path $OldVersionEvidence 'request.json'
$OldVersionStdoutPath = Join-Path $OldVersionEvidence 'stdout.txt'
$OldVersionStderrPath = Join-Path $OldVersionEvidence 'stderr.txt'
$OldVersionResultPath = Join-Path $OldVersionEvidence 'result.json'
foreach ($ReusedLeaf in @(
    $OldFullAttemptPath,$OldFullCompletionPath,$OldVersionRequestPath,$OldVersionStdoutPath,
    $OldVersionStderrPath,$OldVersionResultPath
)) {
    if (-not (Test-Path -LiteralPath $ReusedLeaf -PathType Leaf)) { throw ('Reused predecessor leaf missing: ' + $ReusedLeaf) }
}
if ((Get-FileHash -LiteralPath $OldFullAttemptPath -Algorithm SHA256).Hash -cne '65DB315FE280720B6DD98489D652A48A3204A2956B1A67BBEAD0AF5505805B08' -or
    (Get-FileHash -LiteralPath $OldFullCompletionPath -Algorithm SHA256).Hash -cne 'E22F9CC759EC30B73A0EB00089835FE184C75F8B6F58CABCF93AACAE0F19162D' -or
    (Get-FileHash -LiteralPath $OldVersionResultPath -Algorithm SHA256).Hash -cne '90A4A70292E68373B7AB1834CFDD61C73F842290CF59D96E934A22C9098ABDB4') {
    throw 'NEEDS_CONTEXT: reused full-selftest or version evidence drifted.'
}
$GeneratorAppDataChanged =
    ([bool]$CleanupAppDataObservation.generator_before.exists -ne
        [bool]$CleanupAppDataObservation.generator_after.exists) -or
    ([string]$CleanupAppDataObservation.generator_before.catalog_sha256 -cne
        [string]$CleanupAppDataObservation.generator_after.catalog_sha256)
$ObserverAppDataChanged =
    ([bool]$CleanupAppDataObservation.observer_before.exists -ne
        [bool]$CleanupAppDataObservation.observer_after.exists) -or
    ([string]$CleanupAppDataObservation.observer_before.catalog_sha256 -cne
        [string]$CleanupAppDataObservation.observer_after.catalog_sha256)
$BaselineLines = [string[]]@(
    'schema_version=3',
    'verdict=PASS',
    ('finished_utc=' + [DateTime]::UtcNow.ToString('o', [Globalization.CultureInfo]::InvariantCulture)),
    ('approval_lock_path=' + (Get-CanonicalPath $ApprovalLockPath)),
    ('approval_lock_sha256=' + $ApprovalLockSha256),
    ('approved_plan_commit=' + $P3),
    ('approved_plan_sha256=' + [string]$BaselineApproval.plan_sha256),
    ('approved_spec_commit=' + $S3),
    ('approved_spec_sha256=' + [string]$BaselineApproval.spec_sha256),
    ('baseline_game_tree=' + $GameTree),
    ('predecessor_manifest_path=' + (Get-CanonicalPath $ManifestPath)),
    ('predecessor_manifest_sha256=' + [string]$BaselineApproval.predecessor_manifest_sha256),
    'predecessor_artifact_count=115',
    'predecessor_catalog_bytes=24660',
    'predecessor_catalog_sha256=9694E728A82F6DDC743DA5E83967EAC7EE02FFA62FA53E21F4A2374F27DDDA24',
    'legacy_generator_invocation_count=1',
    'legacy_observer_invocation_count=0',
    'legacy_generator_classification=TIMEOUT',
    'legacy_candidate_save_disposition=preserved_not_used',
    'v2_generator_invocation_count=1',
    'v2_observer_invocation_count=0',
    'v2_generator_classification=GOVERNANCE_CONTRACT_FAILURE',
    'v2_generator_reason=LOG_CONTRACT_MISMATCH',
    'v2_candidate_save_disposition=preserved_not_used',
    'full_selftest_reused=True',
    ('full_selftest_attempt_sha256=' + (Get-FileHash -LiteralPath $OldFullAttemptPath -Algorithm SHA256).Hash),
    ('full_selftest_completion_sha256=' + (Get-FileHash -LiteralPath $OldFullCompletionPath -Algorithm SHA256).Hash),
    ('full_selftest_root=' + (Get-CanonicalPath $OldFullRoot)),
    'new_full_selftest_invocations=0',
    'version_probe_reused=True',
    ('version_result_sha256=' + (Get-FileHash -LiteralPath $OldVersionResultPath -Algorithm SHA256).Hash),
    'new_version_probe_invocations=0',
    ('red_record_path=' + (Get-CanonicalPath $RedRecordPath)),
    ('red_record_sha256=' + [string]$BaselineRedSeal.sha256),
    ('generator_host_apply_patch_checkpoint_path=' + (Get-CanonicalPath $RedRecordPath)),
    ('generator_host_apply_patch_checkpoint_sha256=' + [string]$BaselineRedSeal.sha256),
    ('observer_host_apply_patch_checkpoint_path=' + (Get-CanonicalPath $GeneratorCompletionPath)),
    ('observer_host_apply_patch_checkpoint_sha256=' + [string]$BaselineGeneratorCompletionSeal.sha256),
    'observer_post_patch_fresh_scope=True',
    'cleanup_fresh_scope=True',
    'cross_scope_volatile_state_imported=False',
    'cross_scope_non_authority_appdata_handoff=True',
    'cleanup_targets_from_strict_completion_rereads=True',
    'cleanup_hard_allowlist_count=4',
    'task1_nested_from_fresh_strict_rereads=True',
    ('appdata_backup_root=' + [string]$CleanupAppDataObservation.backup_root),
    'appdata_observed_path_count=2',
    ('appdata_generator_path=' + [string]$CleanupAppDataObservation.generator_path),
    ('appdata_observer_path=' + [string]$CleanupAppDataObservation.observer_path),
    ('appdata_generator_handoff_sha256=' + $GeneratorAppDataObservationSha256),
    ('appdata_observation_handoff_sha256=' + $AppDataObservationSha256),
    'appdata_observation_read_only=True',
    'appdata_observation_authority=False',
    'appdata_cleanup_performed=False',
    ('appdata_generator_changed=' + [string]$GeneratorAppDataChanged),
    ('appdata_observer_changed=' + [string]$ObserverAppDataChanged),
    ('appdata_generator_before_schema_version=' + [string]$CleanupAppDataObservation.generator_before.schema_version),
    ('appdata_generator_before_exists=' + [string]$CleanupAppDataObservation.generator_before.exists),
    ('appdata_generator_before_directory_count=' + [string]$CleanupAppDataObservation.generator_before.directory_count),
    ('appdata_generator_before_file_count=' + [string]$CleanupAppDataObservation.generator_before.file_count),
    ('appdata_generator_before_total_file_bytes=' + [string]$CleanupAppDataObservation.generator_before.total_file_bytes),
    ('appdata_generator_before_catalog_bytes=' + [string]$CleanupAppDataObservation.generator_before.catalog_bytes),
    ('appdata_generator_before_catalog_sha256=' + [string]$CleanupAppDataObservation.generator_before.catalog_sha256),
    ('appdata_generator_before_entry_limit=' + [string]$CleanupAppDataObservation.generator_before.entry_limit),
    ('appdata_generator_before_catalog_byte_limit=' + [string]$CleanupAppDataObservation.generator_before.catalog_byte_limit),
    ('appdata_generator_before_timeout_milliseconds=' + [string]$CleanupAppDataObservation.generator_before.timeout_milliseconds),
    ('appdata_generator_before_captured_utc=' + [string]$CleanupAppDataObservation.generator_before.captured_utc),
    ('appdata_generator_after_schema_version=' + [string]$CleanupAppDataObservation.generator_after.schema_version),
    ('appdata_generator_after_exists=' + [string]$CleanupAppDataObservation.generator_after.exists),
    ('appdata_generator_after_directory_count=' + [string]$CleanupAppDataObservation.generator_after.directory_count),
    ('appdata_generator_after_file_count=' + [string]$CleanupAppDataObservation.generator_after.file_count),
    ('appdata_generator_after_total_file_bytes=' + [string]$CleanupAppDataObservation.generator_after.total_file_bytes),
    ('appdata_generator_after_catalog_bytes=' + [string]$CleanupAppDataObservation.generator_after.catalog_bytes),
    ('appdata_generator_after_catalog_sha256=' + [string]$CleanupAppDataObservation.generator_after.catalog_sha256),
    ('appdata_generator_after_entry_limit=' + [string]$CleanupAppDataObservation.generator_after.entry_limit),
    ('appdata_generator_after_catalog_byte_limit=' + [string]$CleanupAppDataObservation.generator_after.catalog_byte_limit),
    ('appdata_generator_after_timeout_milliseconds=' + [string]$CleanupAppDataObservation.generator_after.timeout_milliseconds),
    ('appdata_generator_after_captured_utc=' + [string]$CleanupAppDataObservation.generator_after.captured_utc),
    ('appdata_observer_before_schema_version=' + [string]$CleanupAppDataObservation.observer_before.schema_version),
    ('appdata_observer_before_exists=' + [string]$CleanupAppDataObservation.observer_before.exists),
    ('appdata_observer_before_directory_count=' + [string]$CleanupAppDataObservation.observer_before.directory_count),
    ('appdata_observer_before_file_count=' + [string]$CleanupAppDataObservation.observer_before.file_count),
    ('appdata_observer_before_total_file_bytes=' + [string]$CleanupAppDataObservation.observer_before.total_file_bytes),
    ('appdata_observer_before_catalog_bytes=' + [string]$CleanupAppDataObservation.observer_before.catalog_bytes),
    ('appdata_observer_before_catalog_sha256=' + [string]$CleanupAppDataObservation.observer_before.catalog_sha256),
    ('appdata_observer_before_entry_limit=' + [string]$CleanupAppDataObservation.observer_before.entry_limit),
    ('appdata_observer_before_catalog_byte_limit=' + [string]$CleanupAppDataObservation.observer_before.catalog_byte_limit),
    ('appdata_observer_before_timeout_milliseconds=' + [string]$CleanupAppDataObservation.observer_before.timeout_milliseconds),
    ('appdata_observer_before_captured_utc=' + [string]$CleanupAppDataObservation.observer_before.captured_utc),
    ('appdata_observer_after_schema_version=' + [string]$CleanupAppDataObservation.observer_after.schema_version),
    ('appdata_observer_after_exists=' + [string]$CleanupAppDataObservation.observer_after.exists),
    ('appdata_observer_after_directory_count=' + [string]$CleanupAppDataObservation.observer_after.directory_count),
    ('appdata_observer_after_file_count=' + [string]$CleanupAppDataObservation.observer_after.file_count),
    ('appdata_observer_after_total_file_bytes=' + [string]$CleanupAppDataObservation.observer_after.total_file_bytes),
    ('appdata_observer_after_catalog_bytes=' + [string]$CleanupAppDataObservation.observer_after.catalog_bytes),
    ('appdata_observer_after_catalog_sha256=' + [string]$CleanupAppDataObservation.observer_after.catalog_sha256),
    ('appdata_observer_after_entry_limit=' + [string]$CleanupAppDataObservation.observer_after.entry_limit),
    ('appdata_observer_after_catalog_byte_limit=' + [string]$CleanupAppDataObservation.observer_after.catalog_byte_limit),
    ('appdata_observer_after_timeout_milliseconds=' + [string]$CleanupAppDataObservation.observer_after.timeout_milliseconds),
    ('appdata_observer_after_captured_utc=' + [string]$CleanupAppDataObservation.observer_after.captured_utc),
    ('green_record_path=' + (Get-CanonicalPath $GreenRecordPath)),
    ('green_record_sha256=' + [string]$BaselineGreenSeal.sha256),
    'generator_source=fresh_generator_v3',
    'v3_generator_invocation_count=1',
    ('generator_attempt_sha256=' + [string]$BaselineGeneratorAttemptSeal.sha256),
    ('generator_completion_sha256=' + [string]$BaselineGeneratorCompletionSeal.sha256),
    ('generator_result_sha256=' + [string]$BaselineGeneratorCompletion.result_sha256),
    ('generator_state_sha256=' + [string]$BaselineGeneratorCompletion.state_sha256),
    ('generator_fixture_evidence_sha256=' + [string]$BaselineGeneratorCompletion.fixture_evidence_sha256),
    ('generator_rpytest_stdout_sha256=' + [string]$BaselineGeneratorCompletion.rpytest_stdout_sha256),
    ('generator_engine_log_evidence_sha256=' + [string]$BaselineGeneratorCompletion.engine_log_evidence_sha256),
    'generator_target_copy_count=3',
    ('save_name=' + [string]$BaselineGeneratorCompletion.save_name),
    ('save_bytes=' + [string]$BaselineGeneratorCompletion.save_bytes),
    ('save_sha256=' + [string]$BaselineGeneratorCompletion.save_sha256),
    'v3_observer_invocation_count=1',
    ('observer_attempt_sha256=' + [string]$BaselineObserverAttemptSeal.sha256),
    ('observer_completion_sha256=' + [string]$BaselineObserverCompletionSeal.sha256),
    ('observer_result_sha256=' + [string]$BaselineObserverCompletion.result_sha256),
    ('observer_state_sha256=' + [string]$BaselineObserverCompletion.state_sha256),
    ('observer_fixture_evidence_sha256=' + [string]$BaselineObserverCompletion.fixture_evidence_sha256),
    ('observer_stdout_sha256=' + [string]$BaselineObserverCompletion.stdout_sha256),
    ('observer_stderr_sha256=' + [string]$BaselineObserverCompletion.stderr_sha256),
    ('observer_engine_log_evidence_sha256=' + [string]$BaselineObserverCompletion.engine_log_evidence_sha256),
    'observer_command=run',
    'observer_is_in_test=False',
    'RENPY_AUTO_LOAD=1-1',
    'RENPY_PATH_TO_SAVES=absent',
    'menu_node=game/chapter5.rpy:2807',
    'choice_path=截断补给线——让他们饿三天再打 -> 亲自率领前锋出击 -> 记住这一切，继续前进',
    'intrigue=55',
    'power=60',
    '_iron_prepared=True',
    'visible_final_choices=正面强攻，以气势压倒对方 | 采用迂回战术，先攻击敌军侧翼',
    'hard_grind_visible=False',
    ('mother_path=' + [string]$BaselineMotherSeal.path),
    ('mother_bytes=' + [string]$BaselineMotherSeal.bytes),
    ('mother_sha256=' + [string]$BaselineMotherSeal.sha256),
    'mother_read_only=True',
    ('generator_worktree_removed=' + [string]$BaselineCleanupState.generator_worktree_removed),
    ('generator_savedir_removed=' + [string]$BaselineCleanupState.generator_savedir_removed),
    ('observer_worktree_removed=' + [string]$BaselineCleanupState.observer_worktree_removed),
    ('observer_savedir_removed=' + [string]$BaselineCleanupState.observer_savedir_removed),
    'art_required=False',
    'music_required=False',
    'sound_effects_required=False',
    'animation_required=False',
    'ui_required=False',
    'font_required=False',
    'package_byte_impact=0'
)
New-CreateOnlyUtf8File $BaselineEvidencePath (($BaselineLines -join "`n") + "`n")
$BaselineEvidenceText = [IO.File]::ReadAllText($BaselineEvidencePath, $StrictUtf8)
foreach ($RequiredLiteral in @(
    'verdict=PASS',('approved_plan_commit=' + $P3),('approval_lock_sha256=' + $ApprovalLockSha256),
    'predecessor_artifact_count=115','legacy_candidate_save_disposition=preserved_not_used',
    'v2_candidate_save_disposition=preserved_not_used','new_full_selftest_invocations=0',
    'new_version_probe_invocations=0',
    ('generator_host_apply_patch_checkpoint_sha256=' + [string]$BaselineRedSeal.sha256),
    ('observer_host_apply_patch_checkpoint_sha256=' + [string]$BaselineGeneratorCompletionSeal.sha256),
    'observer_post_patch_fresh_scope=True','cleanup_fresh_scope=True',
    'cross_scope_volatile_state_imported=False','cross_scope_non_authority_appdata_handoff=True',
    'cleanup_hard_allowlist_count=4',
    ('appdata_backup_root=' + $AppDataBackupRoot),'appdata_observed_path_count=2',
    ('appdata_generator_path=' + $GeneratorAppDataBackupPath),
    ('appdata_observer_path=' + $ObserverAppDataBackupPath),
    ('appdata_generator_handoff_sha256=' + $GeneratorAppDataObservationSha256),
    ('appdata_observation_handoff_sha256=' + $AppDataObservationSha256),
    'appdata_observation_read_only=True','appdata_observation_authority=False',
    'appdata_cleanup_performed=False',
    'v3_generator_invocation_count=1',
    'v3_observer_invocation_count=1','observer_command=run',('mother_sha256=' + [string]$BaselineMotherSeal.sha256),
    'generator_worktree_removed=True','observer_savedir_removed=True','package_byte_impact=0'
)) {
    if (-not $BaselineEvidenceText.Contains($RequiredLiteral)) {
        throw ('NEEDS_CONTEXT: baseline evidence omits required literal: ' + $RequiredLiteral)
    }
}
(Get-Item -LiteralPath $BaselineEvidencePath).IsReadOnly = $true
if (-not (Get-Item -LiteralPath $BaselineEvidencePath).IsReadOnly) { throw 'Could not freeze baseline evidence.' }
$BaselineEvidenceSha256 = (Get-FileHash -LiteralPath $BaselineEvidencePath -Algorithm SHA256).Hash
```

Expected: one strict LF-only, no-BOM, read-only schema-v3 baseline records legacy generator 1/observer 0, v2 generator 1/observer 0, v3 generator 1/observer 1, both preserved-not-used predecessor dispositions, reused full/version evidence, RED/GREEN, dual log channels, three v3 generator targets, observer autoload, mother, cleanup, all four bounded read-only AppData snapshots and their sealed handoffs, and zero asset/package impact. AppData remains outside authority, cleanup, package impact, and the 141-leaf union.

- [ ] **Step 15: Build the exact 115+26 union and freeze schema-v3 Task 1 completion**

```powershell
Assert-RecoveryAuthorityUnchanged 'before Task 1 completion'
$LockFirstScopeSpecs = @(
    [pscustomobject]@{ begin='TASK1_V3_BOOTSTRAP_BEGIN'; end='TASK1_V3_BOOTSTRAP_END'; path='$KnownApprovalLockPath ='; exists='Test-Path -LiteralPath $KnownApprovalLockPath'; hash='Get-FileHash -LiteralPath $KnownApprovalLockPath' },
    [pscustomobject]@{ begin='TASK1_V3_POST_PATCH_REENTRY_BEGIN'; end='TASK1_V3_POST_PATCH_REENTRY_END'; path='$BootstrapLockPath ='; exists='Test-Path -LiteralPath $BootstrapLockPath'; hash='Get-FileHash -LiteralPath $BootstrapLockPath' },
    [pscustomobject]@{ begin='TASK1_V3_OBSERVER_REENTRY_BEGIN'; end='TASK1_V3_OBSERVER_REENTRY_END'; path='$ObserverBootstrapLockPath ='; exists='Test-Path -LiteralPath $ObserverBootstrapLockPath'; hash='Get-FileHash -LiteralPath $ObserverBootstrapLockPath' },
    [pscustomobject]@{ begin='TASK1_V3_CLEANUP_REENTRY_BEGIN'; end='TASK1_V3_CLEANUP_REENTRY_END'; path='$CleanupBootstrapLockPath ='; exists='Test-Path -LiteralPath $CleanupBootstrapLockPath'; hash='Get-FileHash -LiteralPath $CleanupBootstrapLockPath' }
)
foreach ($ScopeSpec in $LockFirstScopeSpecs) {
    $ScopeSource = Get-AuthenticatedPlanBlock ([string]$ScopeSpec.begin) ([string]$ScopeSpec.end)
    $PathIndex = $ScopeSource.IndexOf([string]$ScopeSpec.path,[StringComparison]::Ordinal)
    $ExistenceIndex = $ScopeSource.IndexOf([string]$ScopeSpec.exists,[StringComparison]::Ordinal)
    $HashIndex = $ScopeSource.IndexOf([string]$ScopeSpec.hash,[StringComparison]::Ordinal)
    if ($PathIndex -lt 0 -or $ExistenceIndex -le $PathIndex -or $HashIndex -le $ExistenceIndex) {
        throw ('NEEDS_CONTEXT: fresh scope lock-first source order failed: ' + [string]$ScopeSpec.begin)
    }
    $BeforeHash = $ScopeSource.Substring(0,$HashIndex)
    if ($BeforeHash.IndexOf('ReadAllBytes',[StringComparison]::Ordinal) -ge 0 -or
        $BeforeHash.IndexOf('Resolve-Path',[StringComparison]::Ordinal) -ge 0 -or
        $BeforeHash.IndexOf('ConvertFrom-Json',[StringComparison]::Ordinal) -ge 0 -or
        $BeforeHash.IndexOf('git ',[StringComparison]::Ordinal) -ge 0) {
        throw ('NEEDS_CONTEXT: fresh scope performs project/lock reads before out-of-band hash: ' + [string]$ScopeSpec.begin)
    }
}
$CleanupDeleteSource = Get-AuthenticatedPlanBlock 'TASK1_V3_CLEANUP_DELETE_BEGIN' 'TASK1_V3_CLEANUP_DELETE_END'
if ([regex]::Matches($CleanupDeleteSource,'(?m)^git worktree remove --force \(\[string\]\$CleanupTargets\.').Count -ne 2 -or
    [regex]::Matches($CleanupDeleteSource,'(?m)^Remove-VerifiedSaveDirectory \(\[string\]\$CleanupTargets\.').Count -ne 2 -or
    $CleanupDeleteSource.IndexOf('AppData',[StringComparison]::OrdinalIgnoreCase) -ge 0 -or
    $CleanupDeleteSource.IndexOf('RecoveryRoot',[StringComparison]::Ordinal) -ge 0 -or
    $CleanupDeleteSource.IndexOf('BaselineEvidencePath',[StringComparison]::Ordinal) -ge 0 -or
    $CleanupDeleteSource.IndexOf('Task1CompletionPath',[StringComparison]::Ordinal) -ge 0) {
    throw 'NEEDS_CONTEXT: cleanup deletion source is not exactly two completion-derived worktrees plus two SaveDirs.'
}
if ((& git rev-parse HEAD).Trim() -cne $P3 -or (& git rev-parse 'HEAD:game').Trim() -cne $GameTree -or
    @(git diff --cached --name-only).Count -ne 0 -or
    (@(git status --short --untracked-files=all) -join '|') -cne ('?? ' + $WinterPlan) -or
    (Get-FileHash -LiteralPath $WinterPlan -Algorithm SHA256).Hash -cne $WinterSha256) {
    throw 'NEEDS_CONTEXT: shared repository drifted before Task 1 completion.'
}
$FinalApproval = Read-RecoveryStrictJson $ApprovalLockPath 'final approval reread'
$FinalManifest = Read-RecoveryStrictJson $ManifestPath 'final predecessor reread'
$FinalRed = Read-RecoveryStrictJson $RedRecordPath 'final RED reread'
$FinalGreen = Read-RecoveryStrictJson $GreenRecordPath 'final GREEN reread'
$FinalGeneratorAttempt = Read-RecoveryStrictJson $GeneratorAttemptPath 'final generator attempt reread'
$FinalGeneratorCompletion = Read-RecoveryStrictJson $GeneratorCompletionPath 'final generator completion reread'
$FinalObserverAttempt = Read-RecoveryStrictJson $ObserverAttemptPath 'final observer attempt reread'
$FinalObserverCompletion = Read-RecoveryStrictJson $ObserverCompletionPath 'final observer completion reread'
Assert-ExactProperties $FinalApproval $ExpectedLockProperties 'final approval reread'
Assert-ExactProperties $FinalManifest $ExpectedManifestProperties 'final predecessor reread'
Assert-ExactProperties $FinalRed @('schema_version','verdict','fixture_gate','stream_gate','inputs','mutations','created_utc') `
    'final RED reread'
Assert-ExactProperties $FinalGreen @('schema_version','verdict','fixture_gate','stream_gate','inputs','mutations','created_utc') `
    'final GREEN reread'
Assert-ExactProperties $FinalGeneratorAttempt $GeneratorAttemptProperties 'generator attempt final recheck'
Assert-ExactProperties $FinalGeneratorCompletion $GeneratorCompletionProperties 'generator completion final recheck'
Assert-ExactProperties $FinalObserverAttempt $ObserverAttemptProperties 'observer attempt final recheck'
Assert-ExactProperties $FinalObserverCompletion $ObserverCompletionProperties 'observer completion final recheck'
$FinalGeneratorAttemptSeal = New-FileSeal $GeneratorAttemptPath
$FinalGeneratorCompletionSeal = New-FileSeal $GeneratorCompletionPath
$FinalObserverAttemptSeal = New-FileSeal $ObserverAttemptPath
$FinalObserverCompletionSeal = New-FileSeal $ObserverCompletionPath
$FinalRedSeal = New-FileSeal $RedRecordPath
$FinalGreenSeal = New-FileSeal $GreenRecordPath
$FinalGeneratorRequestSeal = New-FileSeal ([string]$FinalGeneratorCompletion.request_path)
$FinalGeneratorResultSeal = New-FileSeal ([string]$FinalGeneratorCompletion.result_path)
$FinalGeneratorStateSeal = New-FileSeal ([string]$FinalGeneratorCompletion.state_path)
$FinalGeneratorStdoutSeal = New-FileSeal ([string]$FinalGeneratorCompletion.rpytest_stdout_path)
$FinalGeneratorStderrSeal = New-FileSeal ([string]$FinalGeneratorCompletion.stderr_path)
$FinalGeneratorFixtureEvidenceSeal = New-FileSeal ([string]$FinalGeneratorCompletion.fixture_evidence_path)
$FinalGeneratorEngineSeal = New-FileSeal ([string]$FinalGeneratorCompletion.engine_log_evidence_path)
$FinalObserverRequestSeal = New-FileSeal ([string]$FinalObserverCompletion.request_path)
$FinalObserverResultSeal = New-FileSeal ([string]$FinalObserverCompletion.result_path)
$FinalObserverStateSeal = New-FileSeal ([string]$FinalObserverCompletion.state_path)
$FinalObserverStdoutSeal = New-FileSeal ([string]$FinalObserverCompletion.stdout_path)
$FinalObserverStderrSeal = New-FileSeal ([string]$FinalObserverCompletion.stderr_path)
$FinalObserverFixtureEvidenceSeal = New-FileSeal ([string]$FinalObserverCompletion.fixture_evidence_path)
$FinalObserverEngineSeal = New-FileSeal ([string]$FinalObserverCompletion.engine_log_evidence_path)
$FinalMotherPath = Get-CanonicalPath (Join-Path $MotherDir ([string]$FinalGeneratorCompletion.save_name))
$FinalMotherSeal = New-FileSeal $FinalMotherPath
$FinalExpectedGeneratorWorktree = Get-CanonicalPath 'E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-generator-recovery-v3'
$FinalExpectedGeneratorSaveDir = Get-CanonicalPath 'E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-generator-save-recovery-v3'
$FinalExpectedObserverWorktree = Get-CanonicalPath 'E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-observer-recovery-v3'
$FinalExpectedObserverSaveDir = Get-CanonicalPath 'E:\Projects\renpy-8.5.2-sdk\terminal-collapse-temp\cos-terminal-collapse-observer-save-recovery-v3'
$FinalExpectedGeneratorTargets = [string[]]@(
    (Get-CanonicalPath (Join-Path $FinalExpectedGeneratorSaveDir ([string]$FinalGeneratorCompletion.save_name))),
    (Get-CanonicalPath (Join-Path (Join-Path $FinalExpectedGeneratorSaveDir 'sync') ([string]$FinalGeneratorCompletion.save_name))),
    (Get-CanonicalPath (Join-Path (Join-Path $FinalExpectedGeneratorWorktree 'game\saves') ([string]$FinalGeneratorCompletion.save_name)))
)
if ((New-FileSeal $ApprovalLockPath).sha256 -cne $ApprovalLockSha256 -or
    (New-FileSeal $ManifestPath).sha256 -cne [string]$FinalApproval.predecessor_manifest_sha256 -or
    $FinalGeneratorCompletionSeal.sha256 -cne $GeneratorCompletionCheckpointSha256 -or
    $FinalObserverCompletionSeal.sha256 -cne $ObserverCompletionCheckpointSha256 -or
    $FinalMotherSeal.sha256 -cne $MotherCheckpointSha256 -or
    -not (Get-Item -LiteralPath $FinalMotherPath).IsReadOnly -or
    [string]$FinalGeneratorCompletion.worktree_path -cne $FinalExpectedGeneratorWorktree -or
    [string]$FinalGeneratorCompletion.savedir_path -cne $FinalExpectedGeneratorSaveDir -or
    [string]$FinalObserverCompletion.worktree_path -cne $FinalExpectedObserverWorktree -or
    [string]$FinalObserverCompletion.savedir_path -cne $FinalExpectedObserverSaveDir -or
    [string]$FinalGeneratorCompletion.external_save_path -cne $FinalExpectedGeneratorTargets[0] -or
    [string]$FinalGeneratorCompletion.sync_save_path -cne $FinalExpectedGeneratorTargets[1] -or
    [string]$FinalGeneratorCompletion.local_save_path -cne $FinalExpectedGeneratorTargets[2] -or
    [string]$FinalObserverCompletion.source_save_path -cne $FinalExpectedGeneratorTargets[0] -or
    [string]$FinalObserverCompletion.replay_save_path -cne
        (Get-CanonicalPath (Join-Path $FinalExpectedObserverSaveDir ([string]$FinalGeneratorCompletion.save_name)))) {
    throw 'NEEDS_CONTEXT: final authority/completion/mother checkpoints drifted.'
}

$FinalGeneratorRequest = Read-HelperJson ([string]$FinalGeneratorRequestSeal.path) 'final generator request'
$FinalGeneratorResult = Read-HelperJson ([string]$FinalGeneratorResultSeal.path) 'final generator result'
$FinalGeneratorState = Read-RecoveryStrictJson ([string]$FinalGeneratorStateSeal.path) 'final generator state'
$FinalObserverRequest = Read-HelperJson ([string]$FinalObserverRequestSeal.path) 'final observer request'
$FinalObserverResult = Read-HelperJson ([string]$FinalObserverResultSeal.path) 'final observer result'
$FinalObserverState = Read-RecoveryStrictJson ([string]$FinalObserverStateSeal.path) 'final observer state'
Assert-PrivateDesktopCompletion $FinalGeneratorResult 0 'final generator result'
Assert-PrivateDesktopCompletion $FinalObserverResult 0 'final observer result'
$FinalMarker = 'terminal-collapse-legacy-v3:' + $P3 + ':supply-vanguard-remember:final-menu'
$FinalGeneratorRequestExpected = [pscustomobject][ordered]@{
    executable=(Get-CanonicalPath $RenPyExe)
    arguments=[object[]]@((Get-CanonicalPath ([string]$FinalGeneratorCompletion.worktree_path)),'test',
        'terminal_collapse_legacy_generator','--savedir',(Get-CanonicalPath ([string]$FinalGeneratorCompletion.savedir_path)))
    working_directory=(Get-CanonicalPath ([string]$FinalGeneratorCompletion.worktree_path))
    environment_names=[object[]]$GeneratorEnvironmentNames
    environment_values=[object[]]@('1',$null,'sw','dummy','dummy',$P3,[string]$FinalGeneratorCompletion.fixture_sha256,
        $GameTree,$FinalMarker,(Get-CanonicalPath ([string]$FinalGeneratorCompletion.savedir_path)),
        (Get-CanonicalPath ([string]$FinalGeneratorCompletion.state_path)))
    timeout_milliseconds=[int64]180000; stdout_path=[string]$FinalGeneratorStdoutSeal.path
    stderr_path=[string]$FinalGeneratorStderrSeal.path; result_path=[string]$FinalGeneratorResultSeal.path
}
$FinalObserverRequestExpected = [pscustomobject][ordered]@{
    executable=(Get-CanonicalPath $RenPyExe)
    arguments=[object[]]@((Get-CanonicalPath ([string]$FinalObserverCompletion.worktree_path)),'run','--savedir',
        (Get-CanonicalPath ([string]$FinalObserverCompletion.savedir_path)))
    working_directory=(Get-CanonicalPath ([string]$FinalObserverCompletion.worktree_path))
    environment_names=[object[]]$ObserverEnvironmentNames
    environment_values=[object[]]@('1','1',$null,'sw','dummy','dummy',$P3,
        [string]$FinalObserverCompletion.fixture_sha256,$GameTree,$FinalMarker,
        (Get-CanonicalPath ([string]$FinalObserverCompletion.savedir_path)),
        (Get-CanonicalPath ([string]$FinalObserverCompletion.state_path)))
    timeout_milliseconds=[int64]120000; stdout_path=[string]$FinalObserverStdoutSeal.path
    stderr_path=[string]$FinalObserverStderrSeal.path; result_path=[string]$FinalObserverResultSeal.path
}
if ((Test-V3RequestContract 'generator' $FinalGeneratorRequest $FinalGeneratorRequestExpected) -cne 'ACCEPT' -or
    (Test-V3GeneratorStateContract $FinalGeneratorState ([string]$FinalGeneratorCompletion.savedir_path) `
        $FinalMarker $P3 $GameTree) -cne 'ACCEPT' -or
    (Test-V3RequestContract 'observer' $FinalObserverRequest $FinalObserverRequestExpected) -cne 'ACCEPT' -or
    (Test-V3ObserverStateContract $FinalObserverState ([string]$FinalObserverCompletion.savedir_path) `
        $FinalMarker $P3 $GameTree $FinalGeneratorState.slot_metadata) -cne 'ACCEPT') {
    throw 'NEEDS_CONTEXT: final request/state evidence failed shared production validators.'
}
$FinalGeneratorChannel = [pscustomobject][ordered]@{
    stdout_exists=$true; stdout_path=[string]$FinalGeneratorStdoutSeal.path
    request_stdout_path=[string]$FinalGeneratorRequest.stdout_path; result_stdout_path=[string]$FinalGeneratorResult.stdout_path
    stdout_bytes=[IO.File]::ReadAllBytes([string]$FinalGeneratorStdoutSeal.path)
    stderr_exists=$true; stderr_bytes=[IO.File]::ReadAllBytes([string]$FinalGeneratorStderrSeal.path); engine_exists=$true
    engine_source_path=(Get-CanonicalPath (Join-Path ([string]$FinalGeneratorCompletion.worktree_path) 'log.txt'))
    engine_bytes=[IO.File]::ReadAllBytes([string]$FinalGeneratorEngineSeal.path); engine_evidence_seal=$FinalGeneratorEngineSeal
}
$FinalObserverChannel = [pscustomobject][ordered]@{
    stdout_exists=$true; stdout_path=[string]$FinalObserverStdoutSeal.path
    request_stdout_path=[string]$FinalObserverRequest.stdout_path; result_stdout_path=[string]$FinalObserverResult.stdout_path
    stdout_bytes=[IO.File]::ReadAllBytes([string]$FinalObserverStdoutSeal.path)
    stderr_exists=$true; stderr_bytes=[IO.File]::ReadAllBytes([string]$FinalObserverStderrSeal.path); engine_exists=$true
    engine_source_path=(Get-CanonicalPath (Join-Path ([string]$FinalObserverCompletion.worktree_path) 'log.txt'))
    engine_bytes=[IO.File]::ReadAllBytes([string]$FinalObserverEngineSeal.path); engine_evidence_seal=$FinalObserverEngineSeal
}
$FinalGeneratorTargetSeals = [object[]]@(
    [pscustomobject][ordered]@{path=[string]$FinalGeneratorCompletion.external_save_path;bytes=[int64]$FinalGeneratorCompletion.save_bytes;sha256=[string]$FinalGeneratorCompletion.save_sha256},
    [pscustomobject][ordered]@{path=[string]$FinalGeneratorCompletion.sync_save_path;bytes=[int64]$FinalGeneratorCompletion.save_bytes;sha256=[string]$FinalGeneratorCompletion.save_sha256},
    [pscustomobject][ordered]@{path=[string]$FinalGeneratorCompletion.local_save_path;bytes=[int64]$FinalGeneratorCompletion.save_bytes;sha256=[string]$FinalGeneratorCompletion.save_sha256}
)
$FinalGeneratorFixtureSeal = [pscustomobject][ordered]@{
    path=[string]$FinalGeneratorCompletion.fixture_path;bytes=[int64]$FinalGeneratorFixtureEvidenceSeal.bytes
    sha256=[string]$FinalGeneratorFixtureEvidenceSeal.sha256
}
$FinalGeneratorExpected = [pscustomobject][ordered]@{
    attempt_id=[string]$FinalGeneratorAttempt.attempt_id; attempt_seal=$FinalGeneratorAttemptSeal
    approval_lock_sha256=$ApprovalLockSha256; approved_plan_commit=$P3
    predecessor_manifest_sha256=[string]$FinalApproval.predecessor_manifest_sha256
    red_record_sha256=[string]$FinalRedSeal.sha256; green_record_sha256=[string]$FinalGreenSeal.sha256
    worktree_path=[string]$FinalGeneratorCompletion.worktree_path; savedir_path=[string]$FinalGeneratorCompletion.savedir_path
    process_evidence_dir=(Get-CanonicalPath $GeneratorProcessEvidence); fixture_seal=$FinalGeneratorFixtureSeal
    fixture_evidence_seal=$FinalGeneratorFixtureEvidenceSeal; request_seal=$FinalGeneratorRequestSeal
    result_seal=$FinalGeneratorResultSeal; state_seal=$FinalGeneratorStateSeal; stdout_seal=$FinalGeneratorStdoutSeal
    stderr_seal=$FinalGeneratorStderrSeal; engine_log_evidence_seal=$FinalGeneratorEngineSeal
    target_seals=$FinalGeneratorTargetSeals; save_name=[string]$FinalGeneratorCompletion.save_name
    save_inventory=$FinalGeneratorCompletion.save_inventory
}
$FinalObserverFixtureSeal = [pscustomobject][ordered]@{
    path=[string]$FinalObserverCompletion.fixture_path;bytes=[int64]$FinalObserverFixtureEvidenceSeal.bytes
    sha256=[string]$FinalObserverFixtureEvidenceSeal.sha256
}
$FinalSourceSeal = [pscustomobject][ordered]@{
    path=[string]$FinalObserverCompletion.source_save_path;bytes=[int64]$FinalObserverCompletion.source_save_bytes
    sha256=[string]$FinalObserverCompletion.source_save_sha256_before
}
$FinalReplaySeal = [pscustomobject][ordered]@{
    path=[string]$FinalObserverCompletion.replay_save_path;bytes=[int64]$FinalObserverCompletion.replay_save_bytes
    sha256=[string]$FinalObserverCompletion.replay_save_sha256_before
}
$FinalObserverExpected = [pscustomobject][ordered]@{
    attempt_id=[string]$FinalObserverAttempt.attempt_id; attempt_seal=$FinalObserverAttemptSeal
    approval_lock_sha256=$ApprovalLockSha256; approved_plan_commit=$P3
    generator_completion_sha256=[string]$FinalGeneratorCompletionSeal.sha256
    worktree_path=[string]$FinalObserverCompletion.worktree_path; savedir_path=[string]$FinalObserverCompletion.savedir_path
    process_evidence_dir=(Get-CanonicalPath $ObserverProcessEvidence); fixture_seal=$FinalObserverFixtureSeal
    fixture_evidence_seal=$FinalObserverFixtureEvidenceSeal; request_seal=$FinalObserverRequestSeal
    result_seal=$FinalObserverResultSeal; state_seal=$FinalObserverStateSeal; stdout_seal=$FinalObserverStdoutSeal
    stderr_seal=$FinalObserverStderrSeal; engine_log_evidence_seal=$FinalObserverEngineSeal
    source_before_seal=$FinalSourceSeal; source_after_seal=$FinalSourceSeal
    replay_before_seal=$FinalReplaySeal; replay_after_seal=$FinalReplaySeal
    save_inventory=$FinalObserverCompletion.save_inventory
}
if ((Test-V3GeneratorRuntimeEvidenceContract $FinalGeneratorChannel $FinalGeneratorCompletion `
        $FinalGeneratorExpected) -cne 'ACCEPT' -or
    (Test-V3ObserverRuntimeEvidenceContract $FinalObserverChannel $FinalObserverCompletion `
        $FinalObserverExpected) -cne 'ACCEPT') {
    throw 'NEEDS_CONTEXT: final completion/current durable evidence failed shared production validators.'
}
if ((@(
        [string]$FinalGeneratorCompletion.save_sha256,
        [string]$FinalObserverCompletion.source_save_sha256_before,
        [string]$FinalObserverCompletion.source_save_sha256_after,
        [string]$FinalObserverCompletion.replay_save_sha256_before,
        [string]$FinalObserverCompletion.replay_save_sha256_after,
        [string]$FinalMotherSeal.sha256
    ) | Select-Object -Unique).Count -ne 1) {
    throw 'NEEDS_CONTEXT: final generator/observer/mother lineage diverged.'
}
$FinalBaselineBytes = [IO.File]::ReadAllBytes($BaselineEvidencePath)
$FinalBaselineText = $StrictUtf8.GetString($FinalBaselineBytes)
if ($FinalBaselineBytes.Length -eq 0 -or
    ($FinalBaselineBytes.Length -ge 3 -and $FinalBaselineBytes[0] -eq 0xEF -and
        $FinalBaselineBytes[1] -eq 0xBB -and $FinalBaselineBytes[2] -eq 0xBF) -or
    $FinalBaselineText.Contains("`r") -or -not $FinalBaselineText.EndsWith("`n",[StringComparison]::Ordinal) -or
    -not $FinalBaselineText.Contains('task1_nested_from_fresh_strict_rereads=True') -or
    -not (Get-Item -LiteralPath $BaselineEvidencePath).IsReadOnly) {
    throw 'NEEDS_CONTEXT: final baseline strict byte reread failed.'
}

$NewDurableLeaves = [string[]]@(
    $ApprovalLockPath,
    (Join-Path $ProjectRoot $SpecPath),
    (Join-Path $ProjectRoot $PlanPath),
    $ManifestPath,
    $RedRecordPath,
    $GreenRecordPath,
    $GeneratorAttemptPath,
    $GeneratorCompletionPath,
    [string]$FinalGeneratorCompletion.request_path,
    [string]$FinalGeneratorCompletion.rpytest_stdout_path,
    [string]$FinalGeneratorCompletion.stderr_path,
    [string]$FinalGeneratorCompletion.result_path,
    [string]$FinalGeneratorCompletion.state_path,
    [string]$FinalGeneratorCompletion.fixture_evidence_path,
    [string]$FinalGeneratorCompletion.engine_log_evidence_path,
    $ObserverAttemptPath,
    $ObserverCompletionPath,
    [string]$FinalObserverCompletion.request_path,
    [string]$FinalObserverCompletion.stdout_path,
    [string]$FinalObserverCompletion.stderr_path,
    [string]$FinalObserverCompletion.result_path,
    [string]$FinalObserverCompletion.state_path,
    [string]$FinalObserverCompletion.fixture_evidence_path,
    [string]$FinalObserverCompletion.engine_log_evidence_path,
    $FinalMotherPath,
    $BaselineEvidencePath
)
if ($NewDurableLeaves.Count -ne 26) { throw 'NEEDS_CONTEXT: new durable leaf list is not exactly 26.' }
$RecoveryPersistentLeaves = [string[]]@(
    (Get-CanonicalPath $ManifestPath),
    (Get-CanonicalPath $RedRecordPath),
    (Get-CanonicalPath $GreenRecordPath),
    (Get-CanonicalPath $GeneratorAttemptPath),
    (Get-CanonicalPath $GeneratorCompletionPath),
    (Get-CanonicalPath ([string]$FinalGeneratorCompletion.request_path)),
    (Get-CanonicalPath ([string]$FinalGeneratorCompletion.rpytest_stdout_path)),
    (Get-CanonicalPath ([string]$FinalGeneratorCompletion.stderr_path)),
    (Get-CanonicalPath ([string]$FinalGeneratorCompletion.result_path)),
    (Get-CanonicalPath ([string]$FinalGeneratorCompletion.state_path)),
    (Get-CanonicalPath ([string]$FinalGeneratorCompletion.fixture_evidence_path)),
    (Get-CanonicalPath ([string]$FinalGeneratorCompletion.engine_log_evidence_path)),
    (Get-CanonicalPath $ObserverAttemptPath),
    (Get-CanonicalPath $ObserverCompletionPath),
    (Get-CanonicalPath ([string]$FinalObserverCompletion.request_path)),
    (Get-CanonicalPath ([string]$FinalObserverCompletion.stdout_path)),
    (Get-CanonicalPath ([string]$FinalObserverCompletion.stderr_path)),
    (Get-CanonicalPath ([string]$FinalObserverCompletion.result_path)),
    (Get-CanonicalPath ([string]$FinalObserverCompletion.state_path)),
    (Get-CanonicalPath ([string]$FinalObserverCompletion.fixture_evidence_path)),
    (Get-CanonicalPath ([string]$FinalObserverCompletion.engine_log_evidence_path)),
    (Get-CanonicalPath $FinalMotherPath),
    (Get-CanonicalPath $BaselineEvidencePath)
)
$RecoveryPersistentDirectories = [string[]]@(
    (Get-CanonicalPath $GeneratorAttemptDir),
    (Get-CanonicalPath $GeneratorProcessEvidence),
    (Get-CanonicalPath $ObserverAttemptDir),
    (Get-CanonicalPath $ObserverProcessEvidence),
    (Get-CanonicalPath $MotherDir)
)
$OutsideRecoveryLeaves = [string[]]@(
    (Get-CanonicalPath $ApprovalLockPath),
    (Get-CanonicalPath (Join-Path $ProjectRoot $SpecPath)),
    (Get-CanonicalPath (Join-Path $ProjectRoot $PlanPath))
)
$NewLeafPartition = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
foreach ($PartitionLeaf in @($OutsideRecoveryLeaves + $RecoveryPersistentLeaves)) {
    if (-not $NewLeafPartition.Add($PartitionLeaf)) {
        throw ('NEEDS_CONTEXT: v3 3+23 durable-leaf partition contains a duplicate: ' + $PartitionLeaf)
    }
}
$CanonicalNewLeaves = [string[]]@($NewDurableLeaves | ForEach-Object { Get-CanonicalPath $_ })
$CanonicalPartitionLeaves = [string[]]@($OutsideRecoveryLeaves + $RecoveryPersistentLeaves)
[Array]::Sort($CanonicalNewLeaves,[StringComparer]::Ordinal)
[Array]::Sort($CanonicalPartitionLeaves,[StringComparer]::Ordinal)
if ($RecoveryPersistentLeaves.Count -ne 23 -or $RecoveryPersistentDirectories.Count -ne 5 -or
    $OutsideRecoveryLeaves.Count -ne 3 -or $NewLeafPartition.Count -ne 26 -or
    ($CanonicalNewLeaves -join "`n") -cne ($CanonicalPartitionLeaves -join "`n") -or
    (Test-Path -LiteralPath (Join-Path $RecoveryRoot 'rules'))) {
    throw 'NEEDS_CONTEXT: exact new-leaf 3-outside + 23-recovery partition or rules absence failed.'
}
$PreCompletionRecoveryTree = Assert-RecoveryExactPhysicalTree $RecoveryRoot `
    $RecoveryPersistentLeaves $RecoveryPersistentDirectories `
    'pre-Task1-completion recovery-v3 tree (23 leaves, five directories)'
if (@($PreCompletionRecoveryTree.files).Count -ne 23 -or
    @($PreCompletionRecoveryTree.directories).Count -ne 5) {
    throw 'NEEDS_CONTEXT: pre-completion recovery-v3 physical cardinality is not 23 leaves/five directories.'
}
foreach ($RuntimeDurableLeaf in @(
    $ApprovalLockPath,$ManifestPath,$RedRecordPath,$GreenRecordPath,
    $GeneratorAttemptPath,$GeneratorCompletionPath,[string]$FinalGeneratorCompletion.request_path,
    [string]$FinalGeneratorCompletion.rpytest_stdout_path,[string]$FinalGeneratorCompletion.stderr_path,
    [string]$FinalGeneratorCompletion.result_path,[string]$FinalGeneratorCompletion.state_path,
    [string]$FinalGeneratorCompletion.fixture_evidence_path,[string]$FinalGeneratorCompletion.engine_log_evidence_path,
    $ObserverAttemptPath,$ObserverCompletionPath,[string]$FinalObserverCompletion.request_path,
    [string]$FinalObserverCompletion.stdout_path,[string]$FinalObserverCompletion.stderr_path,
    [string]$FinalObserverCompletion.result_path,[string]$FinalObserverCompletion.state_path,
    [string]$FinalObserverCompletion.fixture_evidence_path,[string]$FinalObserverCompletion.engine_log_evidence_path,
    $FinalMotherPath,$BaselineEvidencePath
)) {
    if (-not (Get-Item -LiteralPath $RuntimeDurableLeaf).IsReadOnly) {
        throw ('NEEDS_CONTEXT: v3 runtime durable leaf is writable ' + $RuntimeDurableLeaf)
    }
}
$RequiredTask1Paths = New-Object 'System.Collections.Generic.List[string]'
foreach ($PredecessorArtifact in @($FinalManifest.artifacts)) {
    [void]$RequiredTask1Paths.Add((Get-CanonicalPath ([string]$PredecessorArtifact.path)))
}
foreach ($NewLeaf in $NewDurableLeaves) { [void]$RequiredTask1Paths.Add((Get-CanonicalPath $NewLeaf)) }
if ($RequiredTask1Paths.Count -ne 141) { throw ('NEEDS_CONTEXT: required Task 1 union is not 141: ' + $RequiredTask1Paths.Count) }
$RequiredPathSet = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
foreach ($RequiredPath in $RequiredTask1Paths) {
    if (-not $RequiredPathSet.Add($RequiredPath)) { throw ('NEEDS_CONTEXT: duplicate Task 1 union path: ' + $RequiredPath) }
}
$SortedRequiredPaths = [string[]]$RequiredTask1Paths.ToArray()
[Array]::Sort($SortedRequiredPaths, [StringComparer]::Ordinal)
if ($SortedRequiredPaths -contains (Get-CanonicalPath $Task1CompletionPath)) {
    throw 'NEEDS_CONTEXT: Task 1 completion must not self-reference.'
}
if ($RequiredPathSet.Contains($GeneratorAppDataBackupPath) -or
    $RequiredPathSet.Contains($ObserverAppDataBackupPath) -or
    @($SortedRequiredPaths | Where-Object {
        Test-SameOrChildPath $_ $AppDataBackupRoot
    }).Count -ne 0) {
    throw 'NEEDS_CONTEXT: non-authority AppData observation leaked into the 141-leaf union.'
}
$Task1Artifacts = New-Object 'System.Collections.Generic.List[object]'
foreach ($RequiredPath in $SortedRequiredPaths) {
    [void]$Task1Artifacts.Add((New-FileSeal $RequiredPath))
}
if ($Task1Artifacts.Count -ne 141) { throw 'NEEDS_CONTEXT: sealed Task 1 artifact list is not 141.' }
$IndependentTask1PhysicalSeals = New-Object 'System.Collections.Generic.List[object]'
for ($IndependentIndex = 0; $IndependentIndex -lt 141; $IndependentIndex++) {
    $IndependentSeal = New-FileSeal $SortedRequiredPaths[$IndependentIndex]
    $PayloadSeal = @($Task1Artifacts)[$IndependentIndex]
    if ($IndependentSeal.path -cne [string]$PayloadSeal.path -or
        $IndependentSeal.bytes -ne [int64]$PayloadSeal.bytes -or
        $IndependentSeal.sha256 -cne [string]$PayloadSeal.sha256) {
        throw ('NEEDS_CONTEXT: independent 141-leaf physical seal rebuild drifted: ' + $IndependentSeal.path)
    }
    [void]$IndependentTask1PhysicalSeals.Add($IndependentSeal)
}
if ($IndependentTask1PhysicalSeals.Count -ne 141) {
    throw 'NEEDS_CONTEXT: independent current physical artifact union is not exactly 141.'
}

$OldVersionRequestHash = (Get-FileHash -LiteralPath $OldVersionRequestPath -Algorithm SHA256).Hash
$OldVersionStdoutHash = (Get-FileHash -LiteralPath $OldVersionStdoutPath -Algorithm SHA256).Hash
$OldVersionStderrHash = (Get-FileHash -LiteralPath $OldVersionStderrPath -Algorithm SHA256).Hash
$OldVersionResultHash = (Get-FileHash -LiteralPath $OldVersionResultPath -Algorithm SHA256).Hash
$ApprovalNested = [ordered]@{
    lock_path = [string](New-FileSeal $ApprovalLockPath).path
    lock_bytes = [int64](New-FileSeal $ApprovalLockPath).bytes
    lock_sha256 = [string](New-FileSeal $ApprovalLockPath).sha256
    plan_path = Get-CanonicalPath (Join-Path $ProjectRoot $PlanPath)
    plan_commit = $P3
    plan_bytes = [int64](Get-Item -LiteralPath $PlanPath).Length
    plan_sha256 = [string]$FinalApproval.plan_sha256
    spec_path = Get-CanonicalPath (Join-Path $ProjectRoot $SpecPath)
    spec_commit = $S3
    spec_bytes = [int64](Get-Item -LiteralPath $SpecPath).Length
    spec_sha256 = [string]$FinalApproval.spec_sha256
}
$PredecessorNested = [ordered]@{
    manifest_path = Get-CanonicalPath $ManifestPath
    manifest_bytes = [int64](Get-Item -LiteralPath $ManifestPath).Length
    manifest_sha256 = [string]$FinalApproval.predecessor_manifest_sha256
    artifact_count = 115
    catalog_bytes = 24660
    catalog_sha256 = '9694E728A82F6DDC743DA5E83967EAC7EE02FFA62FA53E21F4A2374F27DDDA24'
    failures = [object[]]@($FinalManifest.failures)
    source_inventories = [object[]]@($FinalManifest.source_inventories)
}
$FullSelftestNested = [ordered]@{
    reused = $true
    attempt_path = Get-CanonicalPath $OldFullAttemptPath
    attempt_bytes = [int64](Get-Item -LiteralPath $OldFullAttemptPath).Length
    attempt_sha256 = (Get-FileHash -LiteralPath $OldFullAttemptPath -Algorithm SHA256).Hash
    completion_path = Get-CanonicalPath $OldFullCompletionPath
    completion_bytes = [int64](Get-Item -LiteralPath $OldFullCompletionPath).Length
    completion_sha256 = (Get-FileHash -LiteralPath $OldFullCompletionPath -Algorithm SHA256).Hash
    root_path = Get-CanonicalPath $OldFullRoot
}
$VersionProbeNested = [ordered]@{
    reused = $true
    evidence_dir = Get-CanonicalPath $OldVersionEvidence
    request_sha256 = $OldVersionRequestHash
    stdout_sha256 = $OldVersionStdoutHash
    stderr_sha256 = $OldVersionStderrHash
    result_sha256 = $OldVersionResultHash
}
$GeneratorNested = [ordered]@{
    source = 'fresh_generator_v3'
    invocation_count = 1
    red_record_path = Get-CanonicalPath $RedRecordPath
    red_record_sha256 = [string]$FinalRedSeal.sha256
    green_record_path = Get-CanonicalPath $GreenRecordPath
    green_record_sha256 = [string]$FinalGreenSeal.sha256
    attempt_path = Get-CanonicalPath $GeneratorAttemptPath
    attempt_sha256 = [string]$FinalGeneratorAttemptSeal.sha256
    completion_path = Get-CanonicalPath $GeneratorCompletionPath
    completion_sha256 = [string]$FinalGeneratorCompletionSeal.sha256
    evidence_dir = Get-CanonicalPath $GeneratorProcessEvidence
    request_sha256 = [string]$FinalGeneratorCompletion.request_sha256
    result_sha256 = [string]$FinalGeneratorCompletion.result_sha256
    state_path = [string]$FinalGeneratorCompletion.state_path
    state_sha256 = [string]$FinalGeneratorCompletion.state_sha256
    rpytest_stdout_path = [string]$FinalGeneratorCompletion.rpytest_stdout_path
    rpytest_stdout_bytes = [int64]$FinalGeneratorCompletion.rpytest_stdout_bytes
    rpytest_stdout_sha256 = [string]$FinalGeneratorCompletion.rpytest_stdout_sha256
    stderr_sha256 = [string]$FinalGeneratorCompletion.stderr_sha256
    fixture_evidence_path = [string]$FinalGeneratorCompletion.fixture_evidence_path
    fixture_evidence_sha256 = [string]$FinalGeneratorCompletion.fixture_evidence_sha256
    engine_log_evidence_path = [string]$FinalGeneratorCompletion.engine_log_evidence_path
    engine_log_evidence_sha256 = [string]$FinalGeneratorCompletion.engine_log_evidence_sha256
    save_name = [string]$FinalGeneratorCompletion.save_name
    save_bytes = [int64]$FinalGeneratorCompletion.save_bytes
    save_sha256 = [string]$FinalGeneratorCompletion.save_sha256
    target_copy_count = 3
}
$ObserverNested = [ordered]@{
    invocation_count = 1
    attempt_path = Get-CanonicalPath $ObserverAttemptPath
    attempt_sha256 = [string]$FinalObserverAttemptSeal.sha256
    completion_path = Get-CanonicalPath $ObserverCompletionPath
    completion_sha256 = [string]$FinalObserverCompletionSeal.sha256
    evidence_dir = Get-CanonicalPath $ObserverProcessEvidence
    request_sha256 = [string]$FinalObserverCompletion.request_sha256
    result_sha256 = [string]$FinalObserverCompletion.result_sha256
    state_path = [string]$FinalObserverCompletion.state_path
    state_sha256 = [string]$FinalObserverCompletion.state_sha256
    stdout_sha256 = [string]$FinalObserverCompletion.stdout_sha256
    stderr_sha256 = [string]$FinalObserverCompletion.stderr_sha256
    fixture_evidence_path = [string]$FinalObserverCompletion.fixture_evidence_path
    fixture_evidence_sha256 = [string]$FinalObserverCompletion.fixture_evidence_sha256
    engine_log_evidence_path = [string]$FinalObserverCompletion.engine_log_evidence_path
    engine_log_evidence_sha256 = [string]$FinalObserverCompletion.engine_log_evidence_sha256
}
$MotherNested = [ordered]@{
    path = [string]$FinalMotherSeal.path
    bytes = [int64]$FinalMotherSeal.bytes
    sha256 = [string]$FinalMotherSeal.sha256
    read_only = $true
}
$FinalRegisteredWorktrees = @(
    git worktree list --porcelain |
        Where-Object { $_.StartsWith('worktree ',[StringComparison]::Ordinal) } |
        ForEach-Object { Get-CanonicalPath $_.Substring(9) }
)
if ((Test-Path -LiteralPath ([string]$FinalGeneratorCompletion.worktree_path)) -or
    (Test-Path -LiteralPath ([string]$FinalGeneratorCompletion.savedir_path)) -or
    (Test-Path -LiteralPath ([string]$FinalObserverCompletion.worktree_path)) -or
    (Test-Path -LiteralPath ([string]$FinalObserverCompletion.savedir_path)) -or
    $FinalRegisteredWorktrees -contains [string]$FinalGeneratorCompletion.worktree_path -or
    $FinalRegisteredWorktrees -contains [string]$FinalObserverCompletion.worktree_path) {
    throw 'NEEDS_CONTEXT: final fresh cleanup absence/registration reread failed.'
}
$CleanupNested = [ordered]@{
    generator_worktree_removed = $true
    generator_savedir_removed = $true
    observer_worktree_removed = $true
    observer_savedir_removed = $true
}
$Task1CompletionProperties = @(
    'schema_version','verdict','approval','predecessor','baseline_game_tree','full_selftest',
    'version_probe','generator','observer','mother','artifact_count','artifacts','cleanup','finished_utc'
)
$Task1CompletionPayload = [ordered]@{
    schema_version = 3
    verdict = 'PASS'
    approval = $ApprovalNested
    predecessor = $PredecessorNested
    baseline_game_tree = $GameTree
    full_selftest = $FullSelftestNested
    version_probe = $VersionProbeNested
    generator = $GeneratorNested
    observer = $ObserverNested
    mother = $MotherNested
    artifact_count = 141
    artifacts = [object[]]$Task1Artifacts.ToArray()
    cleanup = $CleanupNested
    finished_utc = [DateTime]::UtcNow.ToString('o', [Globalization.CultureInfo]::InvariantCulture)
}
$Task1Completion = New-ReadOnlyJsonRecord $Task1CompletionPath $Task1CompletionPayload $Task1CompletionProperties 'Task 1 completion schema v3'
git check-ignore -q -- $Task1CompletionPath
if ($LASTEXITCODE -ne 0) { throw 'Task 1 completion is not ignored.' }
$PostCompletionRecoveryLeaves = [string[]]@(
    $RecoveryPersistentLeaves + (Get-CanonicalPath $Task1CompletionPath)
)
$PostCompletionRecoveryTree = Assert-RecoveryExactPhysicalTree $RecoveryRoot `
    $PostCompletionRecoveryLeaves $RecoveryPersistentDirectories `
    'post-Task1-completion recovery-v3 tree (23 durable leaves plus completion)'
if (@($PostCompletionRecoveryTree.files).Count -ne 24 -or
    @($PostCompletionRecoveryTree.directories).Count -ne 5 -or
    $RequiredPathSet.Contains((Get-CanonicalPath $Task1CompletionPath)) -or
    (Test-Path -LiteralPath (Join-Path $RecoveryRoot 'rules'))) {
    throw 'NEEDS_CONTEXT: post-completion recovery-v3 tree is not exact 24 leaves/five directories with self excluded.'
}

Assert-ExactProperties $Task1Completion.approval @(
    'lock_path','lock_bytes','lock_sha256','plan_path','plan_commit','plan_bytes','plan_sha256',
    'spec_path','spec_commit','spec_bytes','spec_sha256'
) 'Task 1 approval'
Assert-ExactProperties $Task1Completion.predecessor @(
    'manifest_path','manifest_bytes','manifest_sha256','artifact_count','catalog_bytes','catalog_sha256',
    'failures','source_inventories'
) 'Task 1 predecessor'
Assert-ExactProperties $Task1Completion.full_selftest @(
    'reused','attempt_path','attempt_bytes','attempt_sha256','completion_path','completion_bytes','completion_sha256','root_path'
) 'Task 1 full selftest'
Assert-ExactProperties $Task1Completion.version_probe @(
    'reused','evidence_dir','request_sha256','stdout_sha256','stderr_sha256','result_sha256'
) 'Task 1 version probe'
Assert-ExactProperties $Task1Completion.generator @(
    'source','invocation_count','red_record_path','red_record_sha256','green_record_path','green_record_sha256',
    'attempt_path','attempt_sha256','completion_path','completion_sha256','evidence_dir','request_sha256',
    'result_sha256','state_path','state_sha256','rpytest_stdout_path','rpytest_stdout_bytes',
    'rpytest_stdout_sha256','stderr_sha256','fixture_evidence_path','fixture_evidence_sha256',
    'engine_log_evidence_path','engine_log_evidence_sha256','save_name','save_bytes','save_sha256',
    'target_copy_count'
) 'Task 1 generator'
Assert-ExactProperties $Task1Completion.observer @(
    'invocation_count','attempt_path','attempt_sha256','completion_path','completion_sha256','evidence_dir',
    'request_sha256','result_sha256','state_path','state_sha256','stdout_sha256','stderr_sha256',
    'fixture_evidence_path','fixture_evidence_sha256','engine_log_evidence_path',
    'engine_log_evidence_sha256'
) 'Task 1 observer'
Assert-ExactProperties $Task1Completion.mother @('path','bytes','sha256','read_only') 'Task 1 mother'
Assert-ExactProperties $Task1Completion.cleanup @(
    'generator_worktree_removed','generator_savedir_removed','observer_worktree_removed','observer_savedir_removed'
) 'Task 1 cleanup'
if ($Task1Completion.schema_version -isnot [int] -or $Task1Completion.schema_version -ne 3 -or
    $Task1Completion.verdict -isnot [string] -or $Task1Completion.verdict -cne 'PASS' -or
    $Task1Completion.baseline_game_tree -isnot [string] -or $Task1Completion.baseline_game_tree -cne $GameTree -or
    $Task1Completion.artifact_count -isnot [int] -or $Task1Completion.artifact_count -ne 141 -or
    @($Task1Completion.artifacts).Count -ne 141 -or
    -not (Test-RoundtripUtc $Task1Completion.finished_utc) -or
    -not (Test-RecoveryIntegral $Task1Completion.approval.lock_bytes) -or
    -not (Test-RecoveryIntegral $Task1Completion.approval.plan_bytes) -or
    -not (Test-RecoveryIntegral $Task1Completion.approval.spec_bytes) -or
    -not (Test-RecoveryIntegral $Task1Completion.predecessor.manifest_bytes) -or
    -not (Test-RecoveryIntegral $Task1Completion.predecessor.catalog_bytes) -or
    -not (Test-RecoveryIntegral $Task1Completion.full_selftest.attempt_bytes) -or
    -not (Test-RecoveryIntegral $Task1Completion.full_selftest.completion_bytes) -or
    -not (Test-RecoveryIntegral $Task1Completion.generator.rpytest_stdout_bytes) -or
    -not (Test-RecoveryIntegral $Task1Completion.generator.save_bytes) -or
    -not (Test-RecoveryIntegral $Task1Completion.mother.bytes) -or
    $Task1Completion.full_selftest.reused -isnot [bool] -or -not $Task1Completion.full_selftest.reused -or
    $Task1Completion.version_probe.reused -isnot [bool] -or -not $Task1Completion.version_probe.reused -or
    $Task1Completion.generator.source -isnot [string] -or $Task1Completion.generator.source -cne 'fresh_generator_v3' -or
    $Task1Completion.generator.invocation_count -isnot [int] -or $Task1Completion.generator.invocation_count -ne 1 -or
    $Task1Completion.generator.target_copy_count -isnot [int] -or $Task1Completion.generator.target_copy_count -ne 3 -or
    $Task1Completion.observer.invocation_count -isnot [int] -or $Task1Completion.observer.invocation_count -ne 1 -or
    $Task1Completion.mother.read_only -isnot [bool] -or -not $Task1Completion.mother.read_only -or
    @($Task1Completion.predecessor.failures).Count -ne 2 -or
    [string]@($Task1Completion.predecessor.failures)[0].candidate_save_disposition -cne 'preserved_not_used' -or
    [string]@($Task1Completion.predecessor.failures)[1].candidate_save_disposition -cne 'preserved_not_used') {
    throw 'NEEDS_CONTEXT: Task 1 schema-v3 scalar contract failed.'
}
$ManifestFailuresCanonical = ConvertTo-Json -InputObject @($FinalManifest.failures) -Depth 16 -Compress
$CompletionFailuresCanonical = ConvertTo-Json -InputObject @($Task1Completion.predecessor.failures) -Depth 16 -Compress
$ManifestInventoriesCanonical = ConvertTo-Json -InputObject @($FinalManifest.source_inventories) -Depth 16 -Compress
$CompletionInventoriesCanonical = ConvertTo-Json -InputObject @($Task1Completion.predecessor.source_inventories) -Depth 16 -Compress
if ($CompletionFailuresCanonical -cne $ManifestFailuresCanonical -or
    $CompletionInventoriesCanonical -cne $ManifestInventoriesCanonical) {
    throw 'NEEDS_CONTEXT: Task 1 predecessor arrays differ in value, order, or type from the manifest.'
}
foreach ($CleanupProperty in $Task1Completion.cleanup.PSObject.Properties) {
    if ($CleanupProperty.Value -isnot [bool] -or -not $CleanupProperty.Value) {
        throw ('NEEDS_CONTEXT: Task 1 cleanup proof failed: ' + $CleanupProperty.Name)
    }
}
$SeenCompletionPaths = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
$PreviousCompletionPath = $null
for ($ArtifactIndex = 0; $ArtifactIndex -lt 141; $ArtifactIndex++) {
    $Artifact = @($Task1Completion.artifacts)[$ArtifactIndex]
    Assert-ExactProperties $Artifact @('path','bytes','sha256') ('Task 1 artifact ' + $ArtifactIndex)
    if ($Artifact.path -isnot [string] -or [string]$Artifact.path -cne $SortedRequiredPaths[$ArtifactIndex] -or
        -not $SeenCompletionPaths.Add([string]$Artifact.path) -or
        ($null -ne $PreviousCompletionPath -and [StringComparer]::Ordinal.Compare($PreviousCompletionPath, [string]$Artifact.path) -ge 0) -or
        -not (Test-RecoveryIntegral $Artifact.bytes) -or [int64]$Artifact.bytes -lt 0 -or
        $Artifact.sha256 -isnot [string] -or $Artifact.sha256 -cnotmatch '^[0-9A-F]{64}$') {
        throw ('NEEDS_CONTEXT: Task 1 artifact schema/order/exact-union failed: ' + [string]$Artifact.path)
    }
    $CurrentSeal = New-FileSeal ([string]$Artifact.path)
    if ($CurrentSeal.bytes -ne [int64]$Artifact.bytes -or $CurrentSeal.sha256 -cne [string]$Artifact.sha256) {
        throw ('NEEDS_CONTEXT: Task 1 current artifact drifted: ' + [string]$Artifact.path)
    }
    $PreviousCompletionPath = [string]$Artifact.path
}
if (-not (Get-Item -LiteralPath $Task1CompletionPath).IsReadOnly -or
    $SeenCompletionPaths.Contains((Get-CanonicalPath $Task1CompletionPath))) {
    throw 'NEEDS_CONTEXT: Task 1 completion is writable or self-referential.'
}
$Task1CompletionSha256 = (Get-FileHash -LiteralPath $Task1CompletionPath -Algorithm SHA256).Hash
[pscustomobject]@{
    verdict = 'PASS'
    approved_plan_commit = $P3
    approval_lock_sha256 = $ApprovalLockSha256
    predecessor_artifacts = 115
    new_durable_leaves = 26
    artifact_count = 141
    generator_invocations = 1
    observer_invocations = 1
    mother_sha256 = [string]$FinalMotherSeal.sha256
    task1_completion_sha256 = $Task1CompletionSha256
}
```

Expected: `task1-completion.json` is strict LF-only UTF-8 without BOM, rejects duplicate/extra/reordered fields through the shared reader, and is read-only. Its sorted unique artifacts are exactly the 115 manifest leaves plus the enumerated 26 new durable leaves, every current bytes/hash value revalidates, `artifact_count=141`, and the completion itself is excluded. Full selftest/version are explicitly reused with zero new invocations; generator and observer counts are exactly one; mother lineage is `fresh_generator_v3`; all cleanup booleans are true. Art, music, sound effects, animation, UI, fonts, and package metadata are unchanged, so every asset need is false and package-byte impact is zero.

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
if ($PSVersionTable.PSEdition -cne 'Desktop' -or $PSVersionTable.PSVersion.Major -ne 5) {
    throw 'NEEDS_CONTEXT: Task 2 requires Windows PowerShell 5.1 Desktop.'
}
$ApprovalVariable = Get-Variable -Name ApprovalLockSha256 -Scope 0 -ErrorAction SilentlyContinue
if ($null -eq $ApprovalVariable -or $ApprovalVariable.Value -isnot [string] -or
    [string]$ApprovalVariable.Value -cnotmatch '^[0-9A-F]{64}$') {
    throw 'NEEDS_CONTEXT: controller did not bind the out-of-band approval_lock_sha256.'
}
$ApprovalLockSha256 = [string]$ApprovalVariable.Value
$StrictUtf8 = New-Object System.Text.UTF8Encoding($false, $true)
$ProjectRoot = (Resolve-Path -LiteralPath '.').Path

function Get-RecoveryRawJsonObjectKeys([string]$Json, [string]$Context) {
    $Stack = New-Object 'System.Collections.Generic.Stack[object]'
    $Keys = New-Object 'System.Collections.Generic.List[string]'
    for ($Index = 0; $Index -lt $Json.Length; $Index++) {
        $Character = $Json[$Index]
        if ($Character -eq '{') {
            $Stack.Push((New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::Ordinal)))
        } elseif ($Character -eq '[') {
            $Stack.Push($null)
        } elseif ($Character -eq '}' -or $Character -eq ']') {
            if ($Stack.Count -eq 0) { throw ('NEEDS_CONTEXT: unbalanced JSON ' + $Context) }
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
                if ($Stack.Count -eq 0 -or $null -eq $Stack.Peek()) { throw ('NEEDS_CONTEXT: key outside object ' + $Context) }
                $Token = $Json.Substring($Start, $Index - $Start + 1)
                $Key = [string]($Token | ConvertFrom-Json -ErrorAction Stop)
                if (-not $Stack.Peek().Add($Key)) { throw ('NEEDS_CONTEXT: duplicate JSON key ' + $Key + ' ' + $Context) }
                [void]$Keys.Add($Key)
            }
        }
    }
    if ($Stack.Count -ne 0) { throw ('NEEDS_CONTEXT: unbalanced JSON containers ' + $Context) }
    return $Keys.ToArray()
}
function Read-RecoveryStrictJson([string]$Path, [string]$Context) {
    $Raw = [IO.File]::ReadAllBytes($Path)
    if ($Raw.Length -eq 0 -or
        ($Raw.Length -ge 3 -and $Raw[0] -eq 0xEF -and $Raw[1] -eq 0xBB -and $Raw[2] -eq 0xBF)) {
        throw ('NEEDS_CONTEXT: empty/BOM JSON ' + $Context)
    }
    $Text = $StrictUtf8.GetString($Raw)
    if ($Text.Contains([char]0xFFFD) -or -not $Text.EndsWith("`n", [StringComparison]::Ordinal) -or $Text.Contains("`r")) {
        throw ('NEEDS_CONTEXT: noncanonical UTF-8/LF JSON ' + $Context)
    }
    [void](Get-RecoveryRawJsonObjectKeys $Text $Context)
    return ($Text | ConvertFrom-Json -ErrorAction Stop)
}
function Test-RecoveryIntegral($Value) {
    return ($Value -is [sbyte] -or $Value -is [byte] -or $Value -is [int16] -or
        $Value -is [uint16] -or $Value -is [int] -or $Value -is [uint32] -or
        $Value -is [long] -or $Value -is [uint64])
}

$P2 = '25c2ea674948ad89e8b48befb89643a8687648a4'
$S3 = '5fa8fb14792e095e066c3e9f698eda9ea4380854'
$SpecSha256 = '978116FE22B8C65578B78E800EF6039053284EA7E674271646D130BBB4BBF470'
$PlanPath = 'docs/superpowers/plans/2026-08-14-terminal-collapse-generator-recovery-v3.md'
$SpecPath = 'docs/superpowers/specs/2026-08-14-terminal-collapse-generator-recovery-v3-design.md'
$WinterPlan = 'docs/superpowers/plans/2026-08-09-winter-interlude-narrative-delivery.md'
$WinterSha256 = '0F39B5F5ACE1D4666DD146863CABDF398B031F5666C29AE337CEB89796E4276C'
$EvidenceRoot = Join-Path $ProjectRoot '.superpowers\sdd\terminal-collapse-ending'
$RecoveryRoot = Join-Path $EvidenceRoot 'recovery-v3'
$ApprovalLockPath = Join-Path $EvidenceRoot 'approved-plan-lock-v3.json'
function Get-RecoveryCanonicalPath([string]$Path) {
    return [IO.Path]::GetFullPath($Path).TrimEnd([IO.Path]::DirectorySeparatorChar, [IO.Path]::AltDirectorySeparatorChar)
}
$ExpectedPredecessorLockPath = Get-RecoveryCanonicalPath (Join-Path $EvidenceRoot 'approved-plan-lock-v2.json')
$ExpectedPredecessorManifestPath = Get-RecoveryCanonicalPath (Join-Path $RecoveryRoot 'predecessor-evidence.json')
$ExpectedSupersededAttemptPath = Get-RecoveryCanonicalPath (Join-Path $EvidenceRoot 'recovery-v2\generator-attempt\attempt.json')
$ExpectedGeneratorLedgerPath = Get-RecoveryCanonicalPath (Join-Path $RecoveryRoot 'generator-attempt')
$ExpectedObserverLedgerPath = Get-RecoveryCanonicalPath (Join-Path $RecoveryRoot 'observer-attempt')
if (-not (Test-Path -LiteralPath $ApprovalLockPath -PathType Leaf) -or
    (Get-FileHash -LiteralPath $ApprovalLockPath -Algorithm SHA256).Hash -cne $ApprovalLockSha256 -or
    -not (Get-Item -LiteralPath $ApprovalLockPath).IsReadOnly) {
    throw 'NEEDS_CONTEXT: v3 approval lock is missing, writable, or differs from the out-of-band hash.'
}
git check-ignore -q -- $ApprovalLockPath
if ($LASTEXITCODE -ne 0) { throw 'NEEDS_CONTEXT: v3 approval lock is not ignored.' }
$Approval = Read-RecoveryStrictJson $ApprovalLockPath 'approval lock v3'
$ExpectedLockProperties = @(
    'schema_version','purpose','approved_plan_path','approved_plan_commit','plan_sha256',
    'spec_path','spec_commit','spec_sha256','predecessor_plan_commit','predecessor_lock_path',
    'predecessor_lock_bytes','predecessor_lock_sha256','predecessor_manifest_path',
    'predecessor_manifest_bytes','predecessor_manifest_sha256','baseline_game_tree','generator_strategy',
    'superseded_generator_attempt_path','superseded_generator_attempt_sha256','superseded_generator_disposition',
    'generator_attempt_ledger_path','generator_attempt_limit','observer_attempt_ledger_path','observer_attempt_limit',
    'test_result_stream','engine_log_role'
)
if ($Approval -isnot [pscustomobject] -or
    (@($Approval.PSObject.Properties.Name) -join '|') -cne ($ExpectedLockProperties -join '|') -or
    $Approval.schema_version -isnot [int] -or $Approval.schema_version -ne 3 -or
    $Approval.purpose -isnot [string] -or $Approval.purpose -cne 'terminal-collapse-generator-recovery-v3' -or
    $Approval.approved_plan_path -isnot [string] -or $Approval.approved_plan_path -cne $PlanPath -or
    $Approval.approved_plan_commit -isnot [string] -or $Approval.approved_plan_commit -cnotmatch '^[0-9a-f]{40}$' -or
    $Approval.plan_sha256 -isnot [string] -or $Approval.plan_sha256 -cnotmatch '^[0-9A-F]{64}$' -or
    $Approval.spec_path -isnot [string] -or $Approval.spec_path -cne $SpecPath -or
    $Approval.spec_commit -isnot [string] -or $Approval.spec_commit -cne $S3 -or
    $Approval.spec_sha256 -isnot [string] -or $Approval.spec_sha256 -cne $SpecSha256 -or
    $Approval.predecessor_plan_commit -isnot [string] -or $Approval.predecessor_plan_commit -cne $P2 -or
    $Approval.predecessor_lock_path -isnot [string] -or $Approval.predecessor_lock_path -cne $ExpectedPredecessorLockPath -or
    -not (Test-RecoveryIntegral $Approval.predecessor_lock_bytes) -or [int64]$Approval.predecessor_lock_bytes -ne 1957 -or
    $Approval.predecessor_lock_sha256 -isnot [string] -or $Approval.predecessor_lock_sha256 -cne '592E9F1FD5C4996A8612005BE9A33A35721A63228AAB43811208099265AECF8B' -or
    $Approval.predecessor_manifest_path -isnot [string] -or $Approval.predecessor_manifest_path -cne $ExpectedPredecessorManifestPath -or
    -not (Test-RecoveryIntegral $Approval.predecessor_manifest_bytes) -or [int64]$Approval.predecessor_manifest_bytes -le 0 -or
    $Approval.predecessor_manifest_sha256 -isnot [string] -or $Approval.predecessor_manifest_sha256 -cnotmatch '^[0-9A-F]{64}$' -or
    $Approval.baseline_game_tree -isnot [string] -or $Approval.baseline_game_tree -cne 'fa7a398e9d989731b24e3c1642f3e2e33ce846ff' -or
    $Approval.generator_strategy -isnot [string] -or $Approval.generator_strategy -cne 'fresh_one_shot' -or
    $Approval.superseded_generator_attempt_path -isnot [string] -or $Approval.superseded_generator_attempt_path -cne $ExpectedSupersededAttemptPath -or
    $Approval.superseded_generator_attempt_sha256 -isnot [string] -or $Approval.superseded_generator_attempt_sha256 -cne '6C6D597580E80A448C0CE55A80C0955988970C2A6332854049420B8693D38DF0' -or
    $Approval.superseded_generator_disposition -isnot [string] -or $Approval.superseded_generator_disposition -cne 'preserved_not_adopted_log_contract_mismatch' -or
    $Approval.generator_attempt_ledger_path -isnot [string] -or $Approval.generator_attempt_ledger_path -cne $ExpectedGeneratorLedgerPath -or
    $Approval.generator_attempt_limit -isnot [int] -or $Approval.generator_attempt_limit -ne 1 -or
    $Approval.observer_attempt_ledger_path -isnot [string] -or $Approval.observer_attempt_ledger_path -cne $ExpectedObserverLedgerPath -or
    $Approval.observer_attempt_limit -isnot [int] -or $Approval.observer_attempt_limit -ne 1 -or
    $Approval.test_result_stream -isnot [string] -or $Approval.test_result_stream -cne 'helper_stdout' -or
    $Approval.engine_log_role -isnot [string] -or $Approval.engine_log_role -cne 'diagnostic_only') {
    throw 'NEEDS_CONTEXT: v3 approval lock schema/types/values failed.'
}
$P3 = [string]$Approval.approved_plan_commit
$ManifestPath = $ExpectedPredecessorManifestPath
if ((& git rev-parse HEAD).Trim() -cne $P3 -or (& git rev-parse HEAD^).Trim() -cne $S3 -or
    (git log -1 --format=%s) -cne 'docs: plan terminal collapse generator recovery v3' -or
    (@(git diff-tree --no-commit-id --name-only -r $P3) -join '|') -cne $PlanPath -or
    (& git rev-parse ($P3 + ':game')).Trim() -cne [string]$Approval.baseline_game_tree -or
    (& git rev-parse ($S3 + '^')).Trim() -cne $P2 -or
    (git log -1 --format=%s $S3) -cne 'docs: specify terminal collapse generator recovery v3' -or
    (@(git diff-tree --no-commit-id --name-only -r $S3) -join '|') -cne $SpecPath) {
    throw 'NEEDS_CONTEXT: P2 -> S3 -> P3 topology failed.'
}
if ((Get-FileHash -LiteralPath $PlanPath -Algorithm SHA256).Hash -cne [string]$Approval.plan_sha256 -or
    (& git hash-object --no-filters -- $PlanPath).Trim() -cne (& git rev-parse ($P3 + ':' + $PlanPath)).Trim() -or
    (Get-FileHash -LiteralPath $SpecPath -Algorithm SHA256).Hash -cne [string]$Approval.spec_sha256 -or
    (& git hash-object --no-filters -- $SpecPath).Trim() -cne (& git rev-parse ($S3 + ':' + $SpecPath)).Trim()) {
    throw 'NEEDS_CONTEXT: physical/committed v3 plan or spec drifted.'
}
if (-not (Test-Path -LiteralPath $ManifestPath -PathType Leaf) -or
    (Get-Item -LiteralPath $ManifestPath).Length -ne [int64]$Approval.predecessor_manifest_bytes -or
    (Get-FileHash -LiteralPath $ManifestPath -Algorithm SHA256).Hash -cne [string]$Approval.predecessor_manifest_sha256 -or
    -not (Get-Item -LiteralPath $ManifestPath).IsReadOnly) {
    throw 'NEEDS_CONTEXT: predecessor manifest seal drifted.'
}

$Manifest = Read-RecoveryStrictJson $ManifestPath 'predecessor manifest'
$ManifestCreatedUtc = [DateTimeOffset]::MinValue
$ExpectedManifestProperties = @(
    'schema_version','purpose','predecessor_plan_commit','predecessor_lock_sha256',
    'artifact_count','catalog_bytes','catalog_sha256','artifacts','failures','source_inventories','created_utc'
)
if ($Manifest -isnot [pscustomobject] -or
    (@($Manifest.PSObject.Properties.Name) -join '|') -cne ($ExpectedManifestProperties -join '|') -or
    $Manifest.schema_version -isnot [int] -or $Manifest.schema_version -ne 2 -or
    $Manifest.purpose -isnot [string] -or $Manifest.purpose -cne 'terminal-collapse-generator-recovery-v3-predecessor' -or
    $Manifest.predecessor_plan_commit -isnot [string] -or $Manifest.predecessor_plan_commit -cne $P2 -or
    $Manifest.predecessor_lock_sha256 -isnot [string] -or $Manifest.predecessor_lock_sha256 -cne '592E9F1FD5C4996A8612005BE9A33A35721A63228AAB43811208099265AECF8B' -or
    $Manifest.artifact_count -isnot [int] -or $Manifest.artifact_count -ne 115 -or
    @($Manifest.artifacts).Count -ne 115 -or
    $Manifest.catalog_bytes -isnot [int] -or $Manifest.catalog_bytes -ne 24660 -or
    $Manifest.catalog_sha256 -isnot [string] -or $Manifest.catalog_sha256 -cne '9694E728A82F6DDC743DA5E83967EAC7EE02FFA62FA53E21F4A2374F27DDDA24' -or
    $Manifest.created_utc -isnot [string] -or
    -not [DateTimeOffset]::TryParseExact([string]$Manifest.created_utc, 'o', [Globalization.CultureInfo]::InvariantCulture, [Globalization.DateTimeStyles]::RoundtripKind, [ref]$ManifestCreatedUtc)) {
    throw 'NEEDS_CONTEXT: predecessor manifest top-level contract failed.'
}
$Paths = New-Object 'System.Collections.Generic.List[string]'
$Rows = New-Object 'System.Collections.Generic.List[string]'
$Seen = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
foreach ($Artifact in @($Manifest.artifacts)) {
    $ArtifactPath = if ($Artifact -is [pscustomobject] -and $Artifact.path -is [string]) { [string]$Artifact.path } else { '' }
    $ArtifactItem = if (-not [string]::IsNullOrWhiteSpace($ArtifactPath) -and (Test-Path -LiteralPath $ArtifactPath -PathType Leaf)) { Get-Item -LiteralPath $ArtifactPath -Force } else { $null }
    if ($Artifact -isnot [pscustomobject] -or
        (@($Artifact.PSObject.Properties.Name) -join '|') -cne 'path|bytes|sha256' -or
        $Artifact.path -isnot [string] -or -not [IO.Path]::IsPathRooted($ArtifactPath) -or
        (Get-RecoveryCanonicalPath $ArtifactPath) -cne $ArtifactPath -or
        -not (Test-RecoveryIntegral $Artifact.bytes) -or [int64]$Artifact.bytes -lt 0 -or
        $Artifact.sha256 -isnot [string] -or $Artifact.sha256 -cnotmatch '^[0-9A-F]{64}$' -or
        -not $Seen.Add($ArtifactPath) -or $null -eq $ArtifactItem -or
        (($ArtifactItem.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) -or
        $ArtifactItem.Length -ne [int64]$Artifact.bytes -or
        (Get-FileHash -LiteralPath $ArtifactPath -Algorithm SHA256).Hash -cne [string]$Artifact.sha256) {
        throw ('NEEDS_CONTEXT: predecessor artifact drifted: ' + $ArtifactPath)
    }
    $Paths.Add($ArtifactPath)
    $Rows.Add(($ArtifactPath + [char]9 + [string]$Artifact.bytes + [char]9 + [string]$Artifact.sha256))
}
$Sorted = [string[]]$Paths.ToArray()
[Array]::Sort($Sorted, [StringComparer]::Ordinal)
if (($Sorted -join "`n") -cne ($Paths.ToArray() -join "`n")) { throw 'NEEDS_CONTEXT: predecessor paths are not Ordinal-sorted.' }
$Catalog = ($Rows -join "`n") + "`n"
$CatalogBytes = $StrictUtf8.GetBytes($Catalog)
$Hasher = [Security.Cryptography.SHA256]::Create()
try { $CatalogHash = [BitConverter]::ToString($Hasher.ComputeHash($CatalogBytes)).Replace('-', '') } finally { $Hasher.Dispose() }
if ($CatalogBytes.Length -ne 24660 -or $CatalogHash -cne [string]$Manifest.catalog_sha256) {
    throw 'NEEDS_CONTEXT: v3 predecessor 115-file catalog reconstruction failed.'
}
$FailureProperties = @(
    'id','classification','program_outcome','reason','generator_invocation_count','observer_invocation_count',
    'attempt_path','attempt_sha256','result_path','result_bytes','result_sha256','state_path','state_bytes',
    'state_sha256','test_report_path','test_report_bytes','test_report_sha256','engine_log_path',
    'engine_log_bytes','engine_log_sha256','target_copies','candidate_save_disposition'
)
$TargetCopyProperties = @('role','path','bytes','sha256')
$Failures = @($Manifest.failures)
if ($Failures.Count -ne 2) { throw 'NEEDS_CONTEXT: predecessor manifest must contain exactly two failures.' }
for ($FailureIndex = 0; $FailureIndex -lt 2; $FailureIndex++) {
    $Failure = $Failures[$FailureIndex]
    if ($Failure -isnot [pscustomobject] -or
        (@($Failure.PSObject.Properties.Name) -join '|') -cne ($FailureProperties -join '|') -or
        $Failure.id -isnot [string] -or $Failure.classification -isnot [string] -or
        $Failure.program_outcome -isnot [string] -or $Failure.reason -isnot [string] -or
        -not (Test-RecoveryIntegral $Failure.generator_invocation_count) -or
        -not (Test-RecoveryIntegral $Failure.observer_invocation_count) -or
        $Failure.candidate_save_disposition -isnot [string] -or
        $Failure.candidate_save_disposition -cne 'preserved_not_used') {
        throw ('NEEDS_CONTEXT: predecessor failure schema/type contract failed at index ' + [string]$FailureIndex)
    }
    foreach ($SealPrefix in @('result','state','test_report','engine_log')) {
        $PathProperty = $SealPrefix + '_path'
        $BytesProperty = $SealPrefix + '_bytes'
        $HashProperty = $SealPrefix + '_sha256'
        if ($Failure.$PathProperty -isnot [string] -or
            -not (Test-RecoveryIntegral $Failure.$BytesProperty) -or [int64]$Failure.$BytesProperty -lt 0 -or
            $Failure.$HashProperty -isnot [string] -or [string]$Failure.$HashProperty -cnotmatch '^[0-9A-F]{64}$') {
            throw ('NEEDS_CONTEXT: predecessor failure seal types failed: ' + $Failure.id + '/' + $SealPrefix)
        }
        $FailureSealPath = [string]$Failure.$PathProperty
        if (-not [IO.Path]::IsPathRooted($FailureSealPath) -or
            (Get-RecoveryCanonicalPath $FailureSealPath) -cne $FailureSealPath -or
            -not $Seen.Contains($FailureSealPath)) {
            throw ('NEEDS_CONTEXT: predecessor failure seal is not a catalog artifact: ' + $Failure.id + '/' + $SealPrefix)
        }
    }
    foreach ($Copy in @($Failure.target_copies)) {
        if ($Copy -isnot [pscustomobject] -or
            (@($Copy.PSObject.Properties.Name) -join '|') -cne ($TargetCopyProperties -join '|') -or
            $Copy.role -isnot [string] -or $Copy.path -isnot [string] -or
            -not (Test-RecoveryIntegral $Copy.bytes) -or [int64]$Copy.bytes -le 0 -or
            $Copy.sha256 -isnot [string] -or $Copy.sha256 -cnotmatch '^[0-9A-F]{64}$' -or
            -not [IO.Path]::IsPathRooted([string]$Copy.path) -or
            (Get-RecoveryCanonicalPath ([string]$Copy.path)) -cne [string]$Copy.path -or
            -not $Seen.Contains([string]$Copy.path)) {
            throw ('NEEDS_CONTEXT: predecessor target-copy contract failed: ' + $Failure.id)
        }
    }
}
if ($Failures[0].id -cne 'legacy_generator' -or
    $Failures[0].classification -cne 'TIMEOUT' -or
    $Failures[0].program_outcome -cne 'TIMEOUT' -or
    [int64]$Failures[0].generator_invocation_count -ne 1 -or
    [int64]$Failures[0].observer_invocation_count -ne 0 -or
    $null -ne $Failures[0].attempt_path -or $null -ne $Failures[0].attempt_sha256 -or
    $Failures[1].id -cne 'v2_generator' -or
    $Failures[1].classification -cne 'GOVERNANCE_CONTRACT_FAILURE' -or
    $Failures[1].program_outcome -cne 'COMPLETED' -or
    $Failures[1].reason -cne 'LOG_CONTRACT_MISMATCH' -or
    [int64]$Failures[1].generator_invocation_count -ne 1 -or
    [int64]$Failures[1].observer_invocation_count -ne 0 -or
    $Failures[1].attempt_path -isnot [string] -or
    [string]$Failures[1].attempt_path -cne $ExpectedSupersededAttemptPath -or
    $Failures[1].attempt_sha256 -isnot [string] -or
    [string]$Failures[1].attempt_sha256 -cne '6C6D597580E80A448C0CE55A80C0955988970C2A6332854049420B8693D38DF0' -or
    @($Failures[1].target_copies).Count -ne 3) {
    throw 'NEEDS_CONTEXT: legacy/v2 failure classifications or preserved dispositions drifted.'
}

$InventoryProperties = @(
    'id','root_path','authority_file_count','authority_files','excluded_cache_count','excluded_cache_files'
)
$InventoryFileProperties = @('relative_path','bytes','sha256')
$Inventories = @($Manifest.source_inventories)
if ($Inventories.Count -ne 2 -or
    $Inventories[0].id -cne 'v2_generator_worktree_task_owned' -or
    $Inventories[1].id -cne 'v2_generator_savedir') {
    throw 'NEEDS_CONTEXT: predecessor source-inventory identities/order drifted.'
}
for ($InventoryIndex = 0; $InventoryIndex -lt 2; $InventoryIndex++) {
    $Inventory = $Inventories[$InventoryIndex]
    $ExpectedAuthorityCount = if ($InventoryIndex -eq 0) { 8 } else { 12 }
    $ExpectedExcludedCount = if ($InventoryIndex -eq 0) { 61 } else { 0 }
    if ($Inventory -isnot [pscustomobject] -or
        (@($Inventory.PSObject.Properties.Name) -join '|') -cne ($InventoryProperties -join '|') -or
        $Inventory.id -isnot [string] -or
        $Inventory.root_path -isnot [string] -or
        -not [IO.Path]::IsPathRooted([string]$Inventory.root_path) -or
        (Get-RecoveryCanonicalPath ([string]$Inventory.root_path)) -cne [string]$Inventory.root_path -or
        -not (Test-Path -LiteralPath ([string]$Inventory.root_path) -PathType Container) -or
        -not (Test-RecoveryIntegral $Inventory.authority_file_count) -or
        [int64]$Inventory.authority_file_count -ne $ExpectedAuthorityCount -or
        $Inventory.authority_files -isnot [Array] -or
        @($Inventory.authority_files).Count -ne $ExpectedAuthorityCount -or
        -not (Test-RecoveryIntegral $Inventory.excluded_cache_count) -or
        [int64]$Inventory.excluded_cache_count -ne $ExpectedExcludedCount -or
        $Inventory.excluded_cache_files -isnot [Array] -or
        @($Inventory.excluded_cache_files).Count -ne $ExpectedExcludedCount) {
        throw ('NEEDS_CONTEXT: predecessor source-inventory contract failed at index ' + [string]$InventoryIndex)
    }

    $AllRelativeSeen = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
    $AuthorityRelativePaths = New-Object 'System.Collections.Generic.List[string]'
    foreach ($InventoryFile in @($Inventory.authority_files)) {
        if ($InventoryFile -isnot [pscustomobject] -or
            (@($InventoryFile.PSObject.Properties.Name) -join '|') -cne ($InventoryFileProperties -join '|') -or
            $InventoryFile.relative_path -isnot [string] -or
            [IO.Path]::IsPathRooted([string]$InventoryFile.relative_path) -or
            [string]$InventoryFile.relative_path -match '(^|[\\/])\.\.([\\/]|$)' -or
            -not $AllRelativeSeen.Add([string]$InventoryFile.relative_path) -or
            -not (Test-RecoveryIntegral $InventoryFile.bytes) -or [int64]$InventoryFile.bytes -lt 0 -or
            $InventoryFile.sha256 -isnot [string] -or $InventoryFile.sha256 -cnotmatch '^[0-9A-F]{64}$') {
            throw ('NEEDS_CONTEXT: predecessor authority inventory metadata failed: ' + $Inventory.id)
        }
        $InventoryAbsolutePath = Get-RecoveryCanonicalPath (
            Join-Path ([string]$Inventory.root_path) ([string]$InventoryFile.relative_path)
        )
        if (-not $InventoryAbsolutePath.StartsWith(
                ([string]$Inventory.root_path + [IO.Path]::DirectorySeparatorChar),
                [StringComparison]::OrdinalIgnoreCase
            ) -or
            -not (Test-Path -LiteralPath $InventoryAbsolutePath -PathType Leaf) -or
            (Get-Item -LiteralPath $InventoryAbsolutePath).Length -ne [int64]$InventoryFile.bytes -or
            (Get-FileHash -LiteralPath $InventoryAbsolutePath -Algorithm SHA256).Hash -cne [string]$InventoryFile.sha256 -or
            -not $Seen.Contains($InventoryAbsolutePath)) {
            throw ('NEEDS_CONTEXT: predecessor authority inventory/current-115 relation failed: ' + $Inventory.id + '/' + $InventoryFile.relative_path)
        }
        [void]$AuthorityRelativePaths.Add([string]$InventoryFile.relative_path)
    }
    $AuthorityRelativeSorted = [string[]]$AuthorityRelativePaths.ToArray().Clone()
    [Array]::Sort($AuthorityRelativeSorted, [StringComparer]::Ordinal)
    if (($AuthorityRelativePaths.ToArray() -join ([char]10)) -cne
        ($AuthorityRelativeSorted -join ([char]10))) {
        throw ('NEEDS_CONTEXT: predecessor authority inventory is not Ordinal-sorted: ' + $Inventory.id)
    }

    # excluded_cache_files are manifest metadata only. Task 2 validates their
    # sealed schema, exact count, order, and uniqueness without joining them to
    # root_path, resolving them, testing existence, reading bytes, or hashing.
    $ExcludedRelativePaths = New-Object 'System.Collections.Generic.List[string]'
    foreach ($InventoryFile in @($Inventory.excluded_cache_files)) {
        if ($InventoryFile -isnot [pscustomobject] -or
            (@($InventoryFile.PSObject.Properties.Name) -join '|') -cne ($InventoryFileProperties -join '|') -or
            $InventoryFile.relative_path -isnot [string] -or
            [IO.Path]::IsPathRooted([string]$InventoryFile.relative_path) -or
            [string]$InventoryFile.relative_path -match '(^|[\\/])\.\.([\\/]|$)' -or
            -not $AllRelativeSeen.Add([string]$InventoryFile.relative_path) -or
            -not (Test-RecoveryIntegral $InventoryFile.bytes) -or [int64]$InventoryFile.bytes -lt 0 -or
            $InventoryFile.sha256 -isnot [string] -or $InventoryFile.sha256 -cnotmatch '^[0-9A-F]{64}$') {
            throw ('NEEDS_CONTEXT: predecessor excluded-cache metadata failed: ' + $Inventory.id)
        }
        [void]$ExcludedRelativePaths.Add([string]$InventoryFile.relative_path)
    }
    $ExcludedRelativeSorted = [string[]]$ExcludedRelativePaths.ToArray().Clone()
    [Array]::Sort($ExcludedRelativeSorted, [StringComparer]::Ordinal)
    if (($ExcludedRelativePaths.ToArray() -join ([char]10)) -cne
        ($ExcludedRelativeSorted -join ([char]10))) {
        throw ('NEEDS_CONTEXT: predecessor excluded-cache metadata is not Ordinal-sorted: ' + $Inventory.id)
    }
}
function Assert-RecoveryExactProperties($Value, [string[]]$Expected, [string]$Context) {
    if ($Value -isnot [pscustomobject] -or
        (@($Value.PSObject.Properties.Name) -join '|') -cne ($Expected -join '|')) {
        throw ('NEEDS_CONTEXT: exact ordered property contract failed: ' + $Context)
    }
}
function Assert-RecoveryCanonicalLeaf([string]$Path, [string]$Context) {
    if ([string]::IsNullOrWhiteSpace($Path) -or -not [IO.Path]::IsPathRooted($Path) -or
        (Get-RecoveryCanonicalPath $Path) -cne $Path -or
        -not (Test-Path -LiteralPath $Path -PathType Leaf) -or
        (Resolve-Path -LiteralPath $Path).Path -cne $Path) {
        throw ('NEEDS_CONTEXT: missing or noncanonical leaf: ' + $Context)
    }
}
function Assert-RecoveryCanonicalDirectory([string]$Path, [string]$Context) {
    if ([string]::IsNullOrWhiteSpace($Path) -or -not [IO.Path]::IsPathRooted($Path) -or
        (Get-RecoveryCanonicalPath $Path) -cne $Path -or
        -not (Test-Path -LiteralPath $Path -PathType Container) -or
        (Get-RecoveryCanonicalPath (Resolve-Path -LiteralPath $Path).Path) -cne $Path) {
        throw ('NEEDS_CONTEXT: missing or noncanonical directory: ' + $Context)
    }
}
function Assert-RecoveryCurrentFile([string]$Path, $Bytes, [string]$Sha256, [string]$Context) {
    Assert-RecoveryCanonicalLeaf $Path $Context
    if (-not (Test-RecoveryIntegral $Bytes) -or [int64]$Bytes -lt 0 -or
        $Sha256 -cnotmatch '^[0-9A-F]{64}$' -or
        (Get-Item -LiteralPath $Path).Length -ne [int64]$Bytes -or
        (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash -cne $Sha256) {
        throw ('NEEDS_CONTEXT: current file seal failed: ' + $Context)
    }
}
function Assert-RecoveryTask1CompletionCurrent([string]$Context) {
    $Task1Path = Get-RecoveryCanonicalPath (Join-Path $RecoveryRoot 'task1-completion.json')
    if (-not (Test-Path -LiteralPath $Task1Path -PathType Leaf) -or
        -not (Get-Item -LiteralPath $Task1Path).IsReadOnly) {
        throw ('NEEDS_CONTEXT: Task 1 completion is missing or writable: ' + $Context)
    }
    git check-ignore -q -- $Task1Path
    if ($LASTEXITCODE -ne 0) { throw ('NEEDS_CONTEXT: Task 1 completion is not ignored: ' + $Context) }
    $Task1 = Read-RecoveryStrictJson $Task1Path ('Task 1 completion ' + $Context)
    $Task1Properties = @(
        'schema_version','verdict','approval','predecessor','baseline_game_tree','full_selftest',
        'version_probe','generator','observer','mother','artifact_count','artifacts','cleanup','finished_utc'
    )
    Assert-RecoveryExactProperties $Task1 $Task1Properties ('Task 1 completion ' + $Context)
    if ($Task1.schema_version -isnot [int] -or $Task1.schema_version -ne 3 -or
        $Task1.verdict -isnot [string] -or $Task1.verdict -cne 'PASS' -or
        $Task1.baseline_game_tree -isnot [string] -or $Task1.baseline_game_tree -cne [string]$Approval.baseline_game_tree -or
        $Task1.artifact_count -isnot [int] -or $Task1.artifact_count -ne 141 -or
        $Task1.artifacts -isnot [Array] -or @($Task1.artifacts).Count -ne 141 -or
        $Task1.finished_utc -isnot [string]) {
        throw ('NEEDS_CONTEXT: Task 1 top-level schema/value contract failed: ' + $Context)
    }
    try {
        [void][DateTimeOffset]::ParseExact(
            [string]$Task1.finished_utc, 'o', [Globalization.CultureInfo]::InvariantCulture,
            [Globalization.DateTimeStyles]::RoundtripKind)
    } catch { throw ('NEEDS_CONTEXT: Task 1 finished_utc failed: ' + $Context) }

    $ApprovalProperties = @(
        'lock_path','lock_bytes','lock_sha256','plan_path','plan_commit','plan_bytes','plan_sha256',
        'spec_path','spec_commit','spec_bytes','spec_sha256'
    )
    $PredecessorProperties = @(
        'manifest_path','manifest_bytes','manifest_sha256','artifact_count','catalog_bytes','catalog_sha256',
        'failures','source_inventories'
    )
    $FullSelftestProperties = @(
        'reused','attempt_path','attempt_bytes','attempt_sha256','completion_path','completion_bytes',
        'completion_sha256','root_path'
    )
    $VersionProbeProperties = @(
        'reused','evidence_dir','request_sha256','stdout_sha256','stderr_sha256','result_sha256'
    )
    $GeneratorProperties = @(
        'source','invocation_count','red_record_path','red_record_sha256','green_record_path','green_record_sha256',
        'attempt_path','attempt_sha256','completion_path','completion_sha256','evidence_dir','request_sha256',
        'result_sha256','state_path','state_sha256','rpytest_stdout_path','rpytest_stdout_bytes',
        'rpytest_stdout_sha256','stderr_sha256','fixture_evidence_path','fixture_evidence_sha256',
        'engine_log_evidence_path','engine_log_evidence_sha256','save_name','save_bytes','save_sha256',
        'target_copy_count'
    )
    $ObserverProperties = @(
        'invocation_count','attempt_path','attempt_sha256','completion_path','completion_sha256','evidence_dir',
        'request_sha256','result_sha256','state_path','state_sha256','stdout_sha256','stderr_sha256',
        'fixture_evidence_path','fixture_evidence_sha256','engine_log_evidence_path','engine_log_evidence_sha256'
    )
    $MotherProperties = @('path','bytes','sha256','read_only')
    $CleanupProperties = @(
        'generator_worktree_removed','generator_savedir_removed','observer_worktree_removed','observer_savedir_removed'
    )
    Assert-RecoveryExactProperties $Task1.approval $ApprovalProperties 'Task 1 approval'
    Assert-RecoveryExactProperties $Task1.predecessor $PredecessorProperties 'Task 1 predecessor'
    Assert-RecoveryExactProperties $Task1.full_selftest $FullSelftestProperties 'Task 1 full selftest'
    Assert-RecoveryExactProperties $Task1.version_probe $VersionProbeProperties 'Task 1 version probe'
    Assert-RecoveryExactProperties $Task1.generator $GeneratorProperties 'Task 1 generator'
    Assert-RecoveryExactProperties $Task1.observer $ObserverProperties 'Task 1 observer'
    Assert-RecoveryExactProperties $Task1.mother $MotherProperties 'Task 1 mother'
    Assert-RecoveryExactProperties $Task1.cleanup $CleanupProperties 'Task 1 cleanup'

    $PlanFullPath = Get-RecoveryCanonicalPath (Join-Path $ProjectRoot $PlanPath)
    $SpecFullPath = Get-RecoveryCanonicalPath (Join-Path $ProjectRoot $SpecPath)
    $LockFullPath = Get-RecoveryCanonicalPath $ApprovalLockPath
    $ManifestFullPath = Get-RecoveryCanonicalPath $ManifestPath
    if ($Task1.approval.lock_path -isnot [string] -or $Task1.approval.lock_path -cne $LockFullPath -or
        -not (Test-RecoveryIntegral $Task1.approval.lock_bytes) -or
        [int64]$Task1.approval.lock_bytes -ne (Get-Item -LiteralPath $LockFullPath).Length -or
        $Task1.approval.lock_sha256 -isnot [string] -or $Task1.approval.lock_sha256 -cne $ApprovalLockSha256 -or
        $Task1.approval.plan_path -isnot [string] -or $Task1.approval.plan_path -cne $PlanFullPath -or
        $Task1.approval.plan_commit -isnot [string] -or $Task1.approval.plan_commit -cne [string]$Approval.approved_plan_commit -or
        -not (Test-RecoveryIntegral $Task1.approval.plan_bytes) -or
        [int64]$Task1.approval.plan_bytes -ne (Get-Item -LiteralPath $PlanFullPath).Length -or
        $Task1.approval.plan_sha256 -isnot [string] -or $Task1.approval.plan_sha256 -cne [string]$Approval.plan_sha256 -or
        $Task1.approval.spec_path -isnot [string] -or $Task1.approval.spec_path -cne $SpecFullPath -or
        $Task1.approval.spec_commit -isnot [string] -or $Task1.approval.spec_commit -cne [string]$Approval.spec_commit -or
        -not (Test-RecoveryIntegral $Task1.approval.spec_bytes) -or
        [int64]$Task1.approval.spec_bytes -ne (Get-Item -LiteralPath $SpecFullPath).Length -or
        $Task1.approval.spec_sha256 -isnot [string] -or $Task1.approval.spec_sha256 -cne [string]$Approval.spec_sha256) {
        throw ('NEEDS_CONTEXT: Task 1 approval lineage failed: ' + $Context)
    }
    if ($Task1.predecessor.manifest_path -isnot [string] -or $Task1.predecessor.manifest_path -cne $ManifestFullPath -or
        -not (Test-RecoveryIntegral $Task1.predecessor.manifest_bytes) -or
        [int64]$Task1.predecessor.manifest_bytes -ne (Get-Item -LiteralPath $ManifestFullPath).Length -or
        $Task1.predecessor.manifest_sha256 -isnot [string] -or
        $Task1.predecessor.manifest_sha256 -cne [string]$Approval.predecessor_manifest_sha256 -or
        $Task1.predecessor.artifact_count -isnot [int] -or $Task1.predecessor.artifact_count -ne 115 -or
        $Task1.predecessor.catalog_bytes -isnot [int] -or $Task1.predecessor.catalog_bytes -ne 24660 -or
        $Task1.predecessor.catalog_sha256 -isnot [string] -or
        $Task1.predecessor.catalog_sha256 -cne '9694E728A82F6DDC743DA5E83967EAC7EE02FFA62FA53E21F4A2374F27DDDA24' -or
        $Task1.predecessor.failures -isnot [Array] -or
        ($Task1.predecessor.failures | ConvertTo-Json -Depth 100 -Compress) -cne
            ($Manifest.failures | ConvertTo-Json -Depth 100 -Compress) -or
        $Task1.predecessor.source_inventories -isnot [Array] -or
        ($Task1.predecessor.source_inventories | ConvertTo-Json -Depth 100 -Compress) -cne
            ($Manifest.source_inventories | ConvertTo-Json -Depth 100 -Compress)) {
        throw ('NEEDS_CONTEXT: Task 1 predecessor lineage failed: ' + $Context)
    }

    if ($Task1.full_selftest.reused -isnot [bool] -or -not $Task1.full_selftest.reused -or
        $Task1.version_probe.reused -isnot [bool] -or -not $Task1.version_probe.reused -or
        $Task1.generator.source -isnot [string] -or $Task1.generator.source -cne 'fresh_generator_v3' -or
        $Task1.generator.invocation_count -isnot [int] -or $Task1.generator.invocation_count -ne 1 -or
        $Task1.generator.target_copy_count -isnot [int] -or $Task1.generator.target_copy_count -ne 3 -or
        $Task1.observer.invocation_count -isnot [int] -or $Task1.observer.invocation_count -ne 1 -or
        $Task1.mother.read_only -isnot [bool] -or -not $Task1.mother.read_only -or
        @($Task1.cleanup.PSObject.Properties.Value | Where-Object { $_ -isnot [bool] -or -not $_ }).Count -ne 0) {
        throw ('NEEDS_CONTEXT: Task 1 reused/invocation/cleanup contract failed: ' + $Context)
    }
    Assert-RecoveryCurrentFile ([string]$Task1.full_selftest.attempt_path) $Task1.full_selftest.attempt_bytes ([string]$Task1.full_selftest.attempt_sha256) 'full-selftest attempt'
    Assert-RecoveryCurrentFile ([string]$Task1.full_selftest.completion_path) $Task1.full_selftest.completion_bytes ([string]$Task1.full_selftest.completion_sha256) 'full-selftest completion'
    Assert-RecoveryCanonicalDirectory ([string]$Task1.full_selftest.root_path) 'full-selftest root'
    Assert-RecoveryCanonicalDirectory ([string]$Task1.version_probe.evidence_dir) 'version-probe evidence dir'
    foreach ($VersionName in @('request','stdout','stderr','result')) {
        $VersionPath = Get-RecoveryCanonicalPath (Join-Path ([string]$Task1.version_probe.evidence_dir) ($VersionName + $(if ($VersionName -ceq 'request' -or $VersionName -ceq 'result') { '.json' } else { '.txt' })))
        $VersionHashProperty = $VersionName + '_sha256'
        Assert-RecoveryCanonicalLeaf $VersionPath ('version-probe ' + $VersionName)
        if ($Task1.version_probe.$VersionHashProperty -isnot [string] -or
            (Get-FileHash -LiteralPath $VersionPath -Algorithm SHA256).Hash -cne [string]$Task1.version_probe.$VersionHashProperty) {
            throw ('NEEDS_CONTEXT: version-probe seal failed: ' + $VersionName)
        }
    }

    foreach ($Pair in @(
        [pscustomobject]@{ Path=$Task1.generator.red_record_path; Hash=$Task1.generator.red_record_sha256; Name='generator RED' },
        [pscustomobject]@{ Path=$Task1.generator.green_record_path; Hash=$Task1.generator.green_record_sha256; Name='generator GREEN' },
        [pscustomobject]@{ Path=$Task1.generator.attempt_path; Hash=$Task1.generator.attempt_sha256; Name='generator attempt' },
        [pscustomobject]@{ Path=$Task1.generator.completion_path; Hash=$Task1.generator.completion_sha256; Name='generator completion' },
        [pscustomobject]@{ Path=(Join-Path ([string]$Task1.generator.evidence_dir) 'request.json'); Hash=$Task1.generator.request_sha256; Name='generator request' },
        [pscustomobject]@{ Path=(Join-Path ([string]$Task1.generator.evidence_dir) 'result.json'); Hash=$Task1.generator.result_sha256; Name='generator result' },
        [pscustomobject]@{ Path=$Task1.generator.rpytest_stdout_path; Hash=$Task1.generator.rpytest_stdout_sha256; Name='generator rpytest stdout' },
        [pscustomobject]@{ Path=$Task1.generator.state_path; Hash=$Task1.generator.state_sha256; Name='generator state' },
        [pscustomobject]@{ Path=$Task1.generator.fixture_evidence_path; Hash=$Task1.generator.fixture_evidence_sha256; Name='generator fixture evidence' },
        [pscustomobject]@{ Path=$Task1.generator.engine_log_evidence_path; Hash=$Task1.generator.engine_log_evidence_sha256; Name='generator engine-log evidence' },
        [pscustomobject]@{ Path=$Task1.observer.attempt_path; Hash=$Task1.observer.attempt_sha256; Name='observer attempt' },
        [pscustomobject]@{ Path=$Task1.observer.completion_path; Hash=$Task1.observer.completion_sha256; Name='observer completion' },
        [pscustomobject]@{ Path=(Join-Path ([string]$Task1.observer.evidence_dir) 'request.json'); Hash=$Task1.observer.request_sha256; Name='observer request' },
        [pscustomobject]@{ Path=(Join-Path ([string]$Task1.observer.evidence_dir) 'result.json'); Hash=$Task1.observer.result_sha256; Name='observer result' },
        [pscustomobject]@{ Path=$Task1.observer.state_path; Hash=$Task1.observer.state_sha256; Name='observer state' },
        [pscustomobject]@{ Path=$Task1.observer.fixture_evidence_path; Hash=$Task1.observer.fixture_evidence_sha256; Name='observer fixture evidence' },
        [pscustomobject]@{ Path=$Task1.observer.engine_log_evidence_path; Hash=$Task1.observer.engine_log_evidence_sha256; Name='observer engine-log evidence' }
    )) {
        Assert-RecoveryCanonicalLeaf ([string]$Pair.Path) ([string]$Pair.Name)
        if ($Pair.Hash -isnot [string] -or [string]$Pair.Hash -cnotmatch '^[0-9A-F]{64}$' -or
            (Get-FileHash -LiteralPath ([string]$Pair.Path) -Algorithm SHA256).Hash -cne [string]$Pair.Hash) {
            throw ('NEEDS_CONTEXT: Task 1 nested hash failed: ' + [string]$Pair.Name)
        }
    }
    Assert-RecoveryCanonicalDirectory ([string]$Task1.generator.evidence_dir) 'generator evidence dir'
    Assert-RecoveryCanonicalDirectory ([string]$Task1.observer.evidence_dir) 'observer evidence dir'
    Assert-RecoveryCurrentFile ([string]$Task1.mother.path) $Task1.mother.bytes ([string]$Task1.mother.sha256) 'Task 1 mother'
    if (-not (Get-Item -LiteralPath ([string]$Task1.mother.path)).IsReadOnly -or
        -not (Test-RecoveryIntegral $Task1.generator.save_bytes) -or [int64]$Task1.generator.save_bytes -le 0 -or
        $Task1.generator.save_name -isnot [string] -or $Task1.generator.save_name -cnotmatch '^1-1-.+\.save$' -or
        $Task1.generator.save_sha256 -isnot [string] -or $Task1.generator.save_sha256 -cne [string]$Task1.mother.sha256 -or
        [int64]$Task1.generator.save_bytes -ne [int64]$Task1.mother.bytes -or
        [IO.Path]::GetFileName([string]$Task1.mother.path) -cne [string]$Task1.generator.save_name) {
        throw ('NEEDS_CONTEXT: Task 1 mother/generator save relation failed: ' + $Context)
    }

    $GeneratorCompletion = Read-RecoveryStrictJson ([string]$Task1.generator.completion_path) 'generator completion'
    $GeneratorCompletionProperties = @(
        'schema_version','attempt_id','attempt_path','attempt_sha256','approval_lock_sha256','approved_plan_commit',
        'predecessor_manifest_sha256','red_record_sha256','green_record_sha256','worktree_path','savedir_path',
        'process_evidence_dir','fixture_path','fixture_sha256','fixture_evidence_path','fixture_evidence_sha256',
        'request_path','request_bytes','request_sha256','result_path','result_bytes','result_sha256',
        'state_path','state_bytes','state_sha256','rpytest_stdout_path','rpytest_stdout_bytes',
        'rpytest_stdout_sha256','stderr_path','stderr_bytes','stderr_sha256','engine_log_evidence_path',
        'engine_log_evidence_sha256','external_save_path','sync_save_path','local_save_path','target_copy_count',
        'save_name','save_bytes','save_sha256','save_inventory','finished_utc'
    )
    Assert-RecoveryExactProperties $GeneratorCompletion $GeneratorCompletionProperties 'generator completion'
    if ($GeneratorCompletion.schema_version -isnot [int] -or $GeneratorCompletion.schema_version -ne 2 -or
        $GeneratorCompletion.attempt_path -cne [string]$Task1.generator.attempt_path -or
        $GeneratorCompletion.attempt_sha256 -cne [string]$Task1.generator.attempt_sha256 -or
        $GeneratorCompletion.approval_lock_sha256 -cne $ApprovalLockSha256 -or
        $GeneratorCompletion.approved_plan_commit -cne [string]$Approval.approved_plan_commit -or
        $GeneratorCompletion.predecessor_manifest_sha256 -cne [string]$Approval.predecessor_manifest_sha256 -or
        $GeneratorCompletion.red_record_sha256 -cne [string]$Task1.generator.red_record_sha256 -or
        $GeneratorCompletion.green_record_sha256 -cne [string]$Task1.generator.green_record_sha256 -or
        $GeneratorCompletion.process_evidence_dir -cne [string]$Task1.generator.evidence_dir -or
        $GeneratorCompletion.request_sha256 -cne [string]$Task1.generator.request_sha256 -or
        $GeneratorCompletion.result_sha256 -cne [string]$Task1.generator.result_sha256 -or
        $GeneratorCompletion.state_path -cne [string]$Task1.generator.state_path -or
        $GeneratorCompletion.state_sha256 -cne [string]$Task1.generator.state_sha256 -or
        $GeneratorCompletion.fixture_evidence_path -cne [string]$Task1.generator.fixture_evidence_path -or
        $GeneratorCompletion.fixture_evidence_sha256 -cne [string]$Task1.generator.fixture_evidence_sha256 -or
        $GeneratorCompletion.rpytest_stdout_path -cne [string]$Task1.generator.rpytest_stdout_path -or
        -not (Test-RecoveryIntegral $GeneratorCompletion.rpytest_stdout_bytes) -or
        [int64]$GeneratorCompletion.rpytest_stdout_bytes -ne [int64]$Task1.generator.rpytest_stdout_bytes -or
        $GeneratorCompletion.rpytest_stdout_sha256 -cne [string]$Task1.generator.rpytest_stdout_sha256 -or
        -not (Test-RecoveryIntegral $GeneratorCompletion.stderr_bytes) -or
        [int64]$GeneratorCompletion.stderr_bytes -ne 0 -or
        $GeneratorCompletion.stderr_sha256 -cne [string]$Task1.generator.stderr_sha256 -or
        $GeneratorCompletion.engine_log_evidence_path -cne [string]$Task1.generator.engine_log_evidence_path -or
        $GeneratorCompletion.engine_log_evidence_sha256 -cne [string]$Task1.generator.engine_log_evidence_sha256 -or
        $GeneratorCompletion.target_copy_count -isnot [int] -or $GeneratorCompletion.target_copy_count -ne 3 -or
        $GeneratorCompletion.save_name -cne [string]$Task1.generator.save_name -or
        -not (Test-RecoveryIntegral $GeneratorCompletion.save_bytes) -or
        [int64]$GeneratorCompletion.save_bytes -ne [int64]$Task1.generator.save_bytes -or
        $GeneratorCompletion.save_sha256 -cne [string]$Task1.generator.save_sha256) {
        throw ('NEEDS_CONTEXT: generator completion lineage failed: ' + $Context)
    }
    $ObserverCompletion = Read-RecoveryStrictJson ([string]$Task1.observer.completion_path) 'observer completion'
    $ObserverCompletionProperties = @(
        'schema_version','attempt_id','attempt_path','attempt_sha256','approval_lock_sha256','approved_plan_commit',
        'generator_completion_sha256','worktree_path','savedir_path','process_evidence_dir','fixture_path','fixture_sha256',
        'fixture_evidence_path','fixture_evidence_sha256','request_path','request_bytes','request_sha256',
        'result_path','result_bytes','result_sha256','state_path','state_bytes','state_sha256','stdout_path',
        'stdout_bytes','stdout_sha256','stderr_path','stderr_bytes','stderr_sha256','engine_log_evidence_path',
        'engine_log_evidence_sha256','source_save_path','source_save_bytes','source_save_sha256_before',
        'source_save_sha256_after','replay_save_path','replay_save_bytes','replay_save_sha256_before',
        'replay_save_sha256_after','save_inventory','finished_utc'
    )
    Assert-RecoveryExactProperties $ObserverCompletion $ObserverCompletionProperties 'observer completion'
    if ($ObserverCompletion.schema_version -isnot [int] -or $ObserverCompletion.schema_version -ne 2 -or
        $ObserverCompletion.attempt_path -cne [string]$Task1.observer.attempt_path -or
        $ObserverCompletion.attempt_sha256 -cne [string]$Task1.observer.attempt_sha256 -or
        $ObserverCompletion.approval_lock_sha256 -cne $ApprovalLockSha256 -or
        $ObserverCompletion.approved_plan_commit -cne [string]$Approval.approved_plan_commit -or
        $ObserverCompletion.generator_completion_sha256 -cne [string]$Task1.generator.completion_sha256 -or
        $ObserverCompletion.process_evidence_dir -cne [string]$Task1.observer.evidence_dir -or
        $ObserverCompletion.request_sha256 -cne [string]$Task1.observer.request_sha256 -or
        $ObserverCompletion.result_sha256 -cne [string]$Task1.observer.result_sha256 -or
        $ObserverCompletion.state_path -cne [string]$Task1.observer.state_path -or
        $ObserverCompletion.state_sha256 -cne [string]$Task1.observer.state_sha256 -or
        $ObserverCompletion.fixture_evidence_path -cne [string]$Task1.observer.fixture_evidence_path -or
        $ObserverCompletion.fixture_evidence_sha256 -cne [string]$Task1.observer.fixture_evidence_sha256 -or
        -not (Test-RecoveryIntegral $ObserverCompletion.stdout_bytes) -or
        [int64]$ObserverCompletion.stdout_bytes -ne 0 -or
        $ObserverCompletion.stdout_sha256 -cne [string]$Task1.observer.stdout_sha256 -or
        -not (Test-RecoveryIntegral $ObserverCompletion.stderr_bytes) -or
        [int64]$ObserverCompletion.stderr_bytes -ne 0 -or
        $ObserverCompletion.stderr_sha256 -cne [string]$Task1.observer.stderr_sha256 -or
        $ObserverCompletion.engine_log_evidence_path -cne [string]$Task1.observer.engine_log_evidence_path -or
        $ObserverCompletion.engine_log_evidence_sha256 -cne [string]$Task1.observer.engine_log_evidence_sha256 -or
        -not (Test-RecoveryIntegral $ObserverCompletion.source_save_bytes) -or
        -not (Test-RecoveryIntegral $ObserverCompletion.replay_save_bytes) -or
        [int64]$ObserverCompletion.source_save_bytes -ne [int64]$Task1.mother.bytes -or
        [int64]$ObserverCompletion.replay_save_bytes -ne [int64]$Task1.mother.bytes -or
        @(@(
            [string]$ObserverCompletion.source_save_sha256_before,
            [string]$ObserverCompletion.source_save_sha256_after,
            [string]$ObserverCompletion.replay_save_sha256_before,
            [string]$ObserverCompletion.replay_save_sha256_after
        ) | Where-Object { $_ -cne [string]$Task1.mother.sha256 }).Count -ne 0) {
        throw ('NEEDS_CONTEXT: observer completion lineage failed: ' + $Context)
    }

    $ArtifactLookup = New-Object 'System.Collections.Generic.Dictionary[string,object]' ([StringComparer]::OrdinalIgnoreCase)
    $ObservedPaths = New-Object 'System.Collections.Generic.List[string]'
    foreach ($Artifact in @($Task1.artifacts)) {
        Assert-RecoveryExactProperties $Artifact @('path','bytes','sha256') 'Task 1 artifact'
        if ($Artifact.path -isnot [string] -or -not (Test-RecoveryIntegral $Artifact.bytes) -or
            $Artifact.sha256 -isnot [string]) {
            throw ('NEEDS_CONTEXT: Task 1 artifact native types failed: ' + $Context)
        }
        Assert-RecoveryCurrentFile ([string]$Artifact.path) $Artifact.bytes ([string]$Artifact.sha256) 'Task 1 artifact'
        if ($ArtifactLookup.ContainsKey([string]$Artifact.path)) {
            throw ('NEEDS_CONTEXT: duplicate Task 1 artifact path: ' + [string]$Artifact.path)
        }
        $ArtifactLookup.Add([string]$Artifact.path, $Artifact)
        [void]$ObservedPaths.Add([string]$Artifact.path)
    }
    $ObservedSorted = [string[]]$ObservedPaths.ToArray().Clone()
    [Array]::Sort($ObservedSorted, [StringComparer]::Ordinal)
    if (($ObservedPaths.ToArray() -join "`n") -cne ($ObservedSorted -join "`n")) {
        throw ('NEEDS_CONTEXT: Task 1 artifacts are not Ordinal-sorted: ' + $Context)
    }
    $RequiredPaths = New-Object 'System.Collections.Generic.List[string]'
    foreach ($Artifact in @($Manifest.artifacts)) { [void]$RequiredPaths.Add([string]$Artifact.path) }
    foreach ($Path in @(
        $LockFullPath, $SpecFullPath, $PlanFullPath, $ManifestFullPath,
        [string]$Task1.generator.red_record_path, [string]$Task1.generator.green_record_path,
        [string]$Task1.generator.attempt_path, [string]$Task1.generator.completion_path,
        (Join-Path ([string]$Task1.generator.evidence_dir) 'request.json'),
        (Join-Path ([string]$Task1.generator.evidence_dir) 'stdout.txt'),
        (Join-Path ([string]$Task1.generator.evidence_dir) 'stderr.txt'),
        (Join-Path ([string]$Task1.generator.evidence_dir) 'result.json'),
        [string]$Task1.generator.state_path, [string]$Task1.generator.fixture_evidence_path,
        [string]$Task1.generator.engine_log_evidence_path, [string]$Task1.observer.attempt_path,
        [string]$Task1.observer.completion_path,
        (Join-Path ([string]$Task1.observer.evidence_dir) 'request.json'),
        (Join-Path ([string]$Task1.observer.evidence_dir) 'stdout.txt'),
        (Join-Path ([string]$Task1.observer.evidence_dir) 'stderr.txt'),
        (Join-Path ([string]$Task1.observer.evidence_dir) 'result.json'),
        [string]$Task1.observer.state_path, [string]$Task1.observer.fixture_evidence_path,
        [string]$Task1.observer.engine_log_evidence_path, [string]$Task1.mother.path,
        (Join-Path $RecoveryRoot 'baseline-evidence.md')
    )) { [void]$RequiredPaths.Add((Get-RecoveryCanonicalPath $Path)) }
    $RequiredSeen = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
    foreach ($RequiredPath in $RequiredPaths) {
        if (-not $RequiredSeen.Add($RequiredPath)) {
            throw ('NEEDS_CONTEXT: Task 1 required union contains a duplicate: ' + $RequiredPath)
        }
    }
    if ($RequiredPaths.Count -ne 141 -or $RequiredSeen.Count -ne 141 -or
        $ArtifactLookup.ContainsKey($Task1Path)) {
        throw ('NEEDS_CONTEXT: Task 1 required union is not exact 115 plus 26: ' + $Context)
    }
    $RequiredSorted = [string[]]$RequiredPaths.ToArray().Clone()
    [Array]::Sort($RequiredSorted, [StringComparer]::Ordinal)
    if (($RequiredSorted -join "`n") -cne ($ObservedSorted -join "`n")) {
        throw ('NEEDS_CONTEXT: Task 1 exact 141-path union failed: ' + $Context)
    }
    return [pscustomobject][ordered]@{
        record = $Task1
        artifact_lookup = $ArtifactLookup
        completion_path = $Task1Path
        completion_sha256 = (Get-FileHash -LiteralPath $Task1Path -Algorithm SHA256).Hash
    }
}

$ApprovalLockHashAtTask2Start = (Get-FileHash -LiteralPath $ApprovalLockPath -Algorithm SHA256).Hash
$ApprovalRecord = $Approval
$Task1Authority = Assert-RecoveryTask1CompletionCurrent 'before the first Task 2 RED edit'
$Task1CompletionRecord = [string]$Task1Authority.completion_path
$Task1CompletionHashAtTask2Start = [string]$Task1Authority.completion_sha256
$Task1Completion = $Task1Authority.record
$Task1ArtifactLookup = $Task1Authority.artifact_lookup
if ((Get-FileHash -LiteralPath $WinterPlan -Algorithm SHA256).Hash -cne $WinterSha256 -or
    @(git diff --cached --name-only).Count -ne 0 -or
    (@(git status --short --untracked-files=all) -join '|') -cne ('?? ' + $WinterPlan)) {
    throw 'NEEDS_CONTEXT: shared worktree is not exact before the first Task 2 RED edit.'
}

function Read-Task2StrictTextLeaf([string]$RelativePath, [string]$Context) {
    $FullPath = [IO.Path]::GetFullPath((Join-Path $ProjectRoot $RelativePath.Replace('/', '\')))
    if (-not $FullPath.StartsWith($ProjectRoot.TrimEnd('\') + '\', [StringComparison]::OrdinalIgnoreCase) -or
        -not (Test-Path -LiteralPath $FullPath -PathType Leaf)) {
        throw ('NEEDS_CONTEXT: required Task 2 reading is missing or outside ProjectRoot: ' + $Context)
    }
    $Raw = [IO.File]::ReadAllBytes($FullPath)
    if ($Raw.Length -eq 0 -or
        ($Raw.Length -ge 3 -and $Raw[0] -eq 0xEF -and $Raw[1] -eq 0xBB -and $Raw[2] -eq 0xBF)) {
        throw ('NEEDS_CONTEXT: required Task 2 reading is empty or has a BOM: ' + $Context)
    }
    $Text = $StrictUtf8.GetString($Raw)
    if ($Text.Contains([char]0) -or $Text.Contains([char]0xFFFD)) {
        throw ('NEEDS_CONTEXT: required Task 2 reading is not strict text: ' + $Context)
    }
    return $Text
}

function Get-Task2ByteSequenceCount([byte[]]$Haystack, [byte[]]$Needle) {
    if ($Needle.Length -eq 0) { throw 'NEEDS_CONTEXT: empty approval-provenance byte sequence.' }
    [int]$Count = 0
    for ([int]$Offset = 0; $Offset -le $Haystack.Length - $Needle.Length; $Offset++) {
        $Matches = $true
        for ([int]$NeedleIndex = 0; $NeedleIndex -lt $Needle.Length; $NeedleIndex++) {
            if ($Haystack[$Offset + $NeedleIndex] -ne $Needle[$NeedleIndex]) {
                $Matches = $false
                break
            }
        }
        if ($Matches) {
            $Count++
            $Offset += $Needle.Length - 1
        }
    }
    return $Count
}

function Get-Task2MarkdownTableRows(
    [string]$Text,
    [string]$HeaderPrefix,
    [string]$Context
) {
    $Lines = [regex]::Split($Text, '\r?\n')
    $HeaderIndexes = @(
        for ($LineIndex = 0; $LineIndex -lt $Lines.Count; $LineIndex++) {
            if ($Lines[$LineIndex].StartsWith($HeaderPrefix, [StringComparison]::Ordinal)) {
                $LineIndex
            }
        }
    )
    if ($HeaderIndexes.Count -ne 1) {
        throw ('NEEDS_CONTEXT: expected exactly one writing table header: ' + $Context)
    }
    $HeaderIndex = [int]$HeaderIndexes[0]
    if ($HeaderIndex + 1 -ge $Lines.Count -or
        $Lines[$HeaderIndex + 1].Trim() -notmatch '^\|(?:\s*:?-+:?\s*\|)+$') {
        throw ('NEEDS_CONTEXT: malformed writing table separator: ' + $Context)
    }
    $Rows = New-Object 'System.Collections.Generic.List[string]'
    for ($LineIndex = $HeaderIndex + 2; $LineIndex -lt $Lines.Count; $LineIndex++) {
        $Line = $Lines[$LineIndex]
        if ([string]::IsNullOrWhiteSpace($Line) -or $Line.StartsWith('## ', [StringComparison]::Ordinal)) {
            break
        }
        [void]$Rows.Add($Line)
    }
    return $Rows.ToArray()
}

# Full mandatory readings. game/balance.rpy:15-98 is also isolated below as
# the exact continuous context for the only visible literal replacement.
$CanonText = Read-Task2StrictTextLeaf 'CANON.md' 'CANON.md'
$BalanceText = Read-Task2StrictTextLeaf 'game/balance.rpy' 'complete current balance source'
$StyleIndexText = Read-Task2StrictTextLeaf 'docs/writing-style/INDEX.md' 'writing-style index'
$GuidanceText = Read-Task2StrictTextLeaf 'docs/writing-style/guidance.md' 'current approved guidance rows'
if ([string]::IsNullOrWhiteSpace($CanonText)) {
    throw 'NEEDS_CONTEXT: CANON.md reading unexpectedly became empty.'
}
$BalanceLines = [IO.File]::ReadAllLines((Join-Path $ProjectRoot 'game\balance.rpy'), $StrictUtf8)
if ($BalanceLines.Count -lt 98 -or
    $BalanceLines[14].Trim() -cne '_ending_requirements = {' -or
    $BalanceLines[97].Trim() -cne 'endings = get_finale_ending_availability(routes, battle_outcomes)') {
    throw 'NEEDS_CONTEXT: exact continuous game/balance.rpy:15-98 context drifted before the RED edit.'
}
$BalanceContext = ($BalanceLines[14..97] -join "`n")

$IndexRows = @(Get-Task2MarkdownTableRows $StyleIndexText '| ID |' 'docs/writing-style/INDEX.md')
$GuidanceRows = @(Get-Task2MarkdownTableRows $GuidanceText '| guidance_id |' 'docs/writing-style/guidance.md')
if ([regex]::Matches($StyleIndexText, '(?m)^maturity_stage:\s*seed\s*$').Count -ne 1 -or
    $IndexRows.Count -ne 0 -or $GuidanceRows.Count -ne 0) {
    throw 'NEEDS_CONTEXT: current seed index/guidance state drifted; revise approval provenance before editing visible copy.'
}

# The v3 lock authenticated predecessor_plan_commit=P2 above. P2 itself is the
# user-approved predecessor plan-only commit, and this tracked path is proved
# byte-identical to its raw Git blob before its literal can be reused.
$ApprovedP2PlanPath = 'docs/superpowers/plans/2026-08-14-terminal-collapse-generator-recovery.md'
$ApprovedP2PlanBlob = '276e950f0332498947c2e7b492fa04310289b4cc'
$P2ChangedPaths = @(git diff-tree --no-commit-id --name-only -r $P2)
if ((git log -1 --format=%s $P2) -cne 'docs: plan terminal collapse generator recovery' -or
    $P2ChangedPaths.Count -ne 1 -or $P2ChangedPaths[0] -cne $ApprovedP2PlanPath -or
    (& git rev-parse ($P2 + ':' + $ApprovedP2PlanPath)).Trim() -cne $ApprovedP2PlanBlob -or
    (& git rev-parse ($P3 + ':' + $ApprovedP2PlanPath)).Trim() -cne $ApprovedP2PlanBlob -or
    (& git hash-object --no-filters -- $ApprovedP2PlanPath).Trim() -cne $ApprovedP2PlanBlob) {
    throw 'NEEDS_CONTEXT: user-approved P2 balance-copy provenance is not the exact authenticated plan blob.'
}

$ApprovedP2PlanBytes = [IO.File]::ReadAllBytes(
    [IO.Path]::GetFullPath((Join-Path $ProjectRoot $ApprovedP2PlanPath.Replace('/', '\')))
)
$CurrentV3PlanBytes = [IO.File]::ReadAllBytes(
    [IO.Path]::GetFullPath((Join-Path $ProjectRoot $PlanPath.Replace('/', '\')))
)
$InheritedBalanceRequirementBytes = [Convert]::FromBase64String(
    '6ZOB6IWV5oiW5oq15oqX6Lev57q/5Y+v6YCJ77yM5LiU5Lya5oiY5a2Y5Zyo6IOc5Yip6Lev5b6E'
)
$P2RequirementInstructionBytes = [Convert]::FromBase64String(
    'SW4gYGdhbWUvYmFsYW5jZS5ycHlgLCByZXBsYWNlIHRoZSBgaXJvbl9sb3JkYCByZXF1aXJlbWVudCBsaXRlcmFsIG9ubHk6'
)
$OldBalanceRequirement = $StrictUtf8.GetString([Convert]::FromBase64String(
    '5p2D5Yqb6Lev57q/5Y+v6YCJ77yM5oiW6ZOB6IWV5Lya5oiY5a2Y5Zyo6IOc5Yip6Lev5b6E'
))
$InheritedBalanceRequirement = $StrictUtf8.GetString($InheritedBalanceRequirementBytes)
if ((@($InheritedBalanceRequirement.ToCharArray() | ForEach-Object { [int][char]$_ }) -join ',') -cne
        '38081,33109,25110,25269,25239,36335,32447,21487,36873,65292,19988,20250,25112,23384,22312,32988,21033,36335,24452' -or
    (@($OldBalanceRequirement.ToCharArray() | ForEach-Object { [int][char]$_ }) -join ',') -cne
        '26435,21147,36335,32447,21487,36873,65292,25110,38081,33109,20250,25112,23384,22312,32988,21033,36335,24452') {
    throw 'NEEDS_CONTEXT: approved/new balance requirement base64 did not decode to the exact reviewed literals.'
}
if ((Get-Task2ByteSequenceCount $ApprovedP2PlanBytes $InheritedBalanceRequirementBytes) -ne 2 -or
    (Get-Task2ByteSequenceCount $ApprovedP2PlanBytes $P2RequirementInstructionBytes) -ne 1 -or
    (Get-Task2ByteSequenceCount $CurrentV3PlanBytes $InheritedBalanceRequirementBytes) -ne 2 -or
    [regex]::Matches($BalanceContext, [regex]::Escape($OldBalanceRequirement)).Count -ne 1 -or
    [regex]::Matches($BalanceContext, [regex]::Escape($InheritedBalanceRequirement)).Count -ne 0) {
    throw 'NEEDS_CONTEXT: byte-for-byte P2 requirement inheritance or pre-edit balance context failed.'
}

$Task2CopyApprovalProvenance = [pscustomobject][ordered]@{
    source = 'authenticated_user_approved_P2_plan'
    source_commit = $P2
    source_path = $ApprovedP2PlanPath
    source_blob = $ApprovedP2PlanBlob
    inherited_literal_occurrences_in_source = 2
    inherited_literal_occurrences_in_v3_plan = 2
    canon_read = $true
    continuous_balance_context = 'game/balance.rpy:15-98'
    style_index_read = $true
    current_guidance_read = $true
    calibration_status = 'not_applicable_exact_user_approved_inheritance'
    new_drafting_or_seed_candidates_authorized = $false
}
$Task2CopyApprovalProvenance | Format-List
```

Expected: the exact 26-field schema-v3 lock, P2→S3→P3 authority chain, predecessor 115-file current catalog, metadata-only 61/0 excluded-cache inventories, both failed candidates classified `preserved_not_used`, Task 1 schema-v3 exact 115+26=141 current-artifact union, empty index, protected winter hash, and sole expected winter status row all pass before the first RED edit; no excluded-cache leaf is resolved, existence-probed, read, or hashed. The same pre-edit fence then reads `CANON.md`, the full current balance source plus exact continuous `game/balance.rpy:15-98`, `docs/writing-style/INDEX.md`, and all current guidance rows; it proves the seed tables are empty and the visible requirement occurs byte-for-byte twice in both the authenticated user-approved P2 plan blob and the authenticated v3 plan, while the pre-edit balance context still contains the old value exactly once. No prose model, Opus call, candidate, or style-library mutation is authorized. No cleaned v3 generator/observer worktree, SaveDir, source, or replay path is required to exist. Any missing, extra, reordered, duplicated, mistyped, noncanonical, writable, drifted, or extra worktree state hard-stops Task 2 without creating `recovery-v3/rules`.

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
$BaselineEvidence = Join-Path $RecoveryRoot 'baseline-evidence.md'
$Task1CompletionRecord = Join-Path $RecoveryRoot 'task1-completion.json'
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
$ExpectedPlanSubject = 'docs: plan terminal collapse generator recovery v3'
if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($Task2BaselineCommit) -or
    (git log -1 --format=%s) -cne $ExpectedPlanSubject) {
    throw 'Task 2 did not start from the final executable-plan commit.'
}
if ($Task2BaselineCommit -cne [string]$ApprovalRecord.approved_plan_commit) {
    throw 'Task 2 baseline is not the approval-locked plan commit.'
}
$Task2EvidenceRoot = Join-Path $RecoveryRoot 'rules'
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
$Task1AuthorityBeforeRed = Assert-RecoveryTask1CompletionCurrent 'immediately before the Task 2 RED invocation'
if ([string]$Task1AuthorityBeforeRed.completion_path -cne $Task1CompletionRecord -or
    [string]$Task1AuthorityBeforeRed.completion_sha256 -cne $Task1CompletionHashAtTask2Start) {
    throw 'NEEDS_CONTEXT: Task 1 completion drifted between the pre-edit gate and the RED launch.'
}
$Task1Completion = $Task1AuthorityBeforeRed.record
$Task1ArtifactLookup = $Task1AuthorityBeforeRed.artifact_lookup
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
    $RegisteredRows = @(git worktree list --porcelain)
    if ($LASTEXITCODE -ne 0) {
        throw ('NEEDS_CONTEXT: could not enumerate registered worktrees before exact mirror removal: ' + $MirrorFull)
    }
    $RegisteredRoots = @(
        $RegisteredRows |
            Where-Object { $_.StartsWith('worktree ', [StringComparison]::Ordinal) } |
            ForEach-Object { [IO.Path]::GetFullPath($_.Substring(9)).TrimEnd('\') }
    )
    if ($RegisteredRoots -notcontains $MirrorFull) {
        throw ('NEEDS_CONTEXT: Task 2 mirror is not the exact registered worktree: ' + $MirrorFull)
    }
    git worktree remove --force $MirrorFull
    if ($LASTEXITCODE -ne 0) {
        throw ('NEEDS_CONTEXT: verified Task 2 mirror cleanup failed: ' + $MirrorFull)
    }
    $RegisteredRowsAfterRemove = @(git worktree list --porcelain)
    if ($LASTEXITCODE -ne 0) {
        throw ('NEEDS_CONTEXT: could not enumerate registered worktrees after exact mirror removal: ' + $MirrorFull)
    }
    $RegisteredRootsAfterRemove = @(
        $RegisteredRowsAfterRemove |
            Where-Object { $_.StartsWith('worktree ', [StringComparison]::Ordinal) } |
            ForEach-Object { [IO.Path]::GetFullPath($_.Substring(9)).TrimEnd('\') }
    )
    if ((Test-Path -LiteralPath $MirrorFull) -or $RegisteredRootsAfterRemove -contains $MirrorFull) {
        throw ('NEEDS_CONTEXT: exact Task 2 mirror path or registration remains after cleanup: ' + $MirrorFull)
    }
}

function Write-Task2CreateNewUtf8 {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)][string]$Path,
        [Parameter(Mandatory = $true)][AllowEmptyString()][string]$Text
    )

    # Windows PowerShell 5.1 ConvertTo-Json emits CRLF. Every sealed record is
    # canonical LF-only, including receipts and the Task 2 completion.
    $CanonicalText = $Text.Replace("`r`n", "`n").Replace("`r", "`n")
    $Bytes = $StrictUtf8.GetBytes($CanonicalText)
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

In `game/balance.rpy`, replace the `iron_lord` requirement literal only with the byte-for-byte value already bound by `$Task2CopyApprovalProvenance` to the authenticated user-approved P2 plan. This is implementation of approved predecessor copy, not new drafting: do not generate, ask Opus for, or select seed/blind alternatives in Task 2.

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

- [ ] **Step 9: Run the focused GREEN suites, mandatory canon/portrait/narration/show scans, and lint once each**

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

function ConvertFrom-Task2CanonicalBase64([object]$Value, [string]$Context) {
    if ($Value -isnot [string]) {
        throw ('NEEDS_CONTEXT: combined canon/show field is not a base64 string: ' + $Context)
    }
    try {
        [byte[]]$Decoded = [Convert]::FromBase64String([string]$Value)
    } catch {
        throw ('NEEDS_CONTEXT: combined canon/show field is invalid base64: ' + $Context)
    }
    if ([Convert]::ToBase64String($Decoded) -cne [string]$Value) {
        throw ('NEEDS_CONTEXT: combined canon/show field is noncanonical base64: ' + $Context)
    }
    return ,$Decoded
}

function Assert-Task2CombinedCanonShowOutput(
    [string]$StdoutPath,
    [string]$StderrPath,
    [string]$ExpectedWorkingDirectory,
    [string]$Context
) {
    $OuterStderr = [IO.File]::ReadAllBytes($StderrPath)
    $OuterStdout = [IO.File]::ReadAllBytes($StdoutPath)
    if ($OuterStderr.Length -ne 0 -or $OuterStdout.Length -eq 0 -or
        ($OuterStdout.Length -ge 3 -and $OuterStdout[0] -eq 0xEF -and
         $OuterStdout[1] -eq 0xBB -and $OuterStdout[2] -eq 0xBF)) {
        throw ('NEEDS_CONTEXT: combined canon/show outer stream contract failed: ' + $Context)
    }
    $OuterText = $StrictUtf8.GetString($OuterStdout)
    if ($OuterText.Contains([char]0) -or $OuterText.Contains([char]0xFFFD)) {
        throw ('NEEDS_CONTEXT: combined canon/show outer stdout is not strict UTF-8: ' + $Context)
    }
    $NormalizedOuterText = $OuterText.Replace("`r`n", "`n")
    if ($NormalizedOuterText.Contains("`r") -or
        -not $NormalizedOuterText.EndsWith("`n", [StringComparison]::Ordinal) -or
        [regex]::Matches($NormalizedOuterText, "`n").Count -ne 1) {
        throw ('NEEDS_CONTEXT: combined canon/show stdout is not one canonical JSON line: ' + $Context)
    }
    $PayloadText = $NormalizedOuterText.Substring(0, $NormalizedOuterText.Length - 1)
    [void](Get-RecoveryRawJsonObjectKeys $PayloadText ('combined canon/show payload ' + $Context))
    $Payload = $PayloadText | ConvertFrom-Json -ErrorAction Stop
    $ExpectedProperties = @(
        'schema_version','canon_executable','canon_arguments','canon_working_directory',
        'canon_exit_code','canon_stdout_base64','canon_stderr_base64',
        'show_exit_code','show_stdout_base64','show_stderr_base64'
    )
    if ($Payload -isnot [pscustomobject] -or
        (@($Payload.PSObject.Properties.Name) -join '|') -cne ($ExpectedProperties -join '|') -or
        $Payload.schema_version -isnot [int] -or [int]$Payload.schema_version -ne 1 -or
        $Payload.canon_executable -isnot [string] -or
        -not [IO.Path]::IsPathRooted([string]$Payload.canon_executable) -or
        -not [string]::Equals(
            [IO.Path]::GetFullPath([string]$Payload.canon_executable),
            [IO.Path]::GetFullPath($Task2Python),
            [StringComparison]::OrdinalIgnoreCase
        ) -or
        $Payload.canon_arguments -isnot [Array] -or
        @($Payload.canon_arguments).Count -ne 2 -or
        $Payload.canon_arguments[0] -isnot [string] -or [string]$Payload.canon_arguments[0] -cne '-B' -or
        $Payload.canon_arguments[1] -isnot [string] -or [string]$Payload.canon_arguments[1] -cne 'Tools/scan_canon.py' -or
        $Payload.canon_working_directory -isnot [string] -or
        -not [string]::Equals(
            [IO.Path]::GetFullPath([string]$Payload.canon_working_directory).TrimEnd('\'),
            [IO.Path]::GetFullPath($ExpectedWorkingDirectory).TrimEnd('\'),
            [StringComparison]::OrdinalIgnoreCase
        ) -or
        -not (Test-RecoveryIntegral $Payload.canon_exit_code) -or
        -not (Test-RecoveryIntegral $Payload.show_exit_code)) {
        throw ('NEEDS_CONTEXT: combined canon/show schema, command, or working-directory contract failed: ' + $Context)
    }

    [byte[]]$CanonStdoutBytes = ConvertFrom-Task2CanonicalBase64 $Payload.canon_stdout_base64 ($Context + '/canon stdout')
    [byte[]]$CanonStderrBytes = ConvertFrom-Task2CanonicalBase64 $Payload.canon_stderr_base64 ($Context + '/canon stderr')
    [byte[]]$ShowStdoutBytes = ConvertFrom-Task2CanonicalBase64 $Payload.show_stdout_base64 ($Context + '/show stdout')
    [byte[]]$ShowStderrBytes = ConvertFrom-Task2CanonicalBase64 $Payload.show_stderr_base64 ($Context + '/show stderr')
    if ([int64]$Payload.canon_exit_code -ne 0 -or $CanonStderrBytes.Length -ne 0 -or
        [int64]$Payload.show_exit_code -ne 0 -or $ShowStdoutBytes.Length -ne 0 -or
        $ShowStderrBytes.Length -ne 0 -or $CanonStdoutBytes.Length -eq 0) {
        throw ('NEEDS_CONTEXT: separate canon or show exit/output contract failed: ' + $Context)
    }
    $CanonText = $StrictUtf8.GetString($CanonStdoutBytes)
    if ($CanonText.Contains([char]0) -or $CanonText.Contains([char]0xFFFD) -or
        -not $CanonText.EndsWith("`n", [StringComparison]::Ordinal) -or
        [regex]::Matches(
            $CanonText,
            '(?m)^=== 总结: [0-9]+ 反逻辑 \+ [0-9]+ canon 偏差 ===\r?$'
        ).Count -ne 1) {
        throw ('NEEDS_CONTEXT: canon stdout is not one complete scan report with one summary: ' + $Context)
    }
    return [pscustomobject][ordered]@{
        canon_exit_code = [int64]$Payload.canon_exit_code
        canon_summary = [regex]::Match(
            $CanonText,
            '(?m)^=== 总结: [0-9]+ 反逻辑 \+ [0-9]+ canon 偏差 ===\r?$'
        ).Value.TrimEnd("`r")
        show_exit_code = [int64]$Payload.show_exit_code
        show_findings = 0
    }
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
        [Parameter()][string[]]$SourceEvidencePaths = @(),
        [Parameter()][switch]$CombinedCanonAndShow
    )

    if (-not (Test-Path -LiteralPath $ScriptPath -PathType Leaf) -or $ScriptPath.Contains('"')) {
        throw ('NEEDS_CONTEXT: scanner path is missing or cannot be quoted safely: ' + $ScriptPath)
    }
    if ([bool]$CombinedCanonAndShow -ne ($Name -ceq 'show-before-green') -or
        ($CombinedCanonAndShow -and
         ($RequireEmptyStdout -or
          -not [string]::IsNullOrWhiteSpace($ExpectedStdoutPattern) -or
          -not [string]::IsNullOrWhiteSpace($ForbiddenStdoutPattern)))) {
        throw ('NEEDS_CONTEXT: combined canon/show mode is reserved for show-before-green and has its own strict output contract: ' + $Name)
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
    $CombinedCanonShowContract = $null
    if ($CombinedCanonAndShow) {
        $CombinedCanonShowContract = Assert-Task2CombinedCanonShowOutput `
            -StdoutPath $StdoutPath `
            -StderrPath $StderrPath `
            -ExpectedWorkingDirectory $MirrorRoot `
            -Context $Name
    } elseif (-not [string]::IsNullOrEmpty($Stderr) -or
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
        scanner_working_directory = [IO.Path]::GetFullPath($MirrorRoot).TrimEnd('\')
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
import base64
import json
import re
import subprocess
import sys
import traceback
from pathlib import Path


def encode_bytes(value):
    return base64.b64encode(value).decode("ascii")


# Exact mandatory command: python -B Tools/scan_canon.py
canon_command = [sys.executable, "-B", "Tools/scan_canon.py"]
try:
    canon = subprocess.run(
        canon_command,
        cwd=str(Path.cwd()),
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        timeout=90,
    )
    canon_exit_code = canon.returncode
    canon_stdout = canon.stdout
    canon_stderr = canon.stderr
except subprocess.TimeoutExpired as error:
    canon_exit_code = 124
    canon_stdout = error.stdout or b""
    canon_stderr = (error.stderr or b"") + b"canon scan timed out\n"
except Exception:
    canon_exit_code = 125
    canon_stdout = b""
    canon_stderr = traceback.format_exc().encode("utf-8")

show_exit_code = 0
show_findings = []
show_stderr = b""
try:
    for path in ["game/balance.rpy", "game/difficulty.rpy", "game/test_game.rpy"]:
        lines = Path(path).read_text(encoding="utf-8", errors="strict").splitlines()
        for i, line in enumerate(lines):
            match = re.match(r'^(\s*)show\s+(\w+_img)\s+at\s+left\b', line)
            if not match:
                continue
            j = i - 1
            while j >= 0 and (not lines[j].strip() or lines[j].strip().startswith("#")):
                j -= 1
            previous = lines[j].strip() if j >= 0 else ""
            if not re.match(r'^(\$\s*hide_all_chars\s*\(|scene\s+bg\b|hide\s+\w+_img)', previous):
                show_findings.append(
                    f"{path}:L{i + 1}  show {match.group(2)}  prev={previous!r}"
                )
except Exception:
    show_exit_code = 1
    show_stderr = traceback.format_exc().encode("utf-8")

show_stdout = (
    ("\n".join(show_findings) + "\n").encode("utf-8")
    if show_findings
    else b""
)
payload = {
    "schema_version": 1,
    "canon_executable": sys.executable,
    "canon_arguments": ["-B", "Tools/scan_canon.py"],
    "canon_working_directory": str(Path.cwd().resolve()),
    "canon_exit_code": canon_exit_code,
    "canon_stdout_base64": encode_bytes(canon_stdout),
    "canon_stderr_base64": encode_bytes(canon_stderr),
    "show_exit_code": show_exit_code,
    "show_stdout_base64": encode_bytes(show_stdout),
    "show_stderr_base64": encode_bytes(show_stderr),
}
sys.stdout.write(json.dumps(payload, ensure_ascii=True, separators=(",", ":")) + "\n")
'@
Write-Task2CreateNewUtf8 -Path $ShowScanPath -Text ($ShowScanSource.Replace("`r`n", "`n") + "`n")
$CanonScriptPath = Join-Path $ScannerMirror 'Tools\scan_canon.py'
$CanonScriptBlob = (& git rev-parse ($Task2BaselineCommit + ':Tools/scan_canon.py')).Trim()
if ($CanonScriptBlob -cnotmatch '^[0-9a-f]{40}$' -or
    -not (Test-Path -LiteralPath $CanonScriptPath -PathType Leaf) -or
    (& git -C $ScannerMirror hash-object --no-filters -- 'Tools/scan_canon.py').Trim() -cne $CanonScriptBlob) {
    throw 'NEEDS_CONTEXT: exact tracked Tools/scan_canon.py baseline is not present in the scanner mirror.'
}
$ShowBeforeResult = Invoke-Task2ConsoleScanner `
    -Name 'show-before-green' `
    -MirrorRoot $ScannerMirror `
    -ScriptPath $ShowScanPath `
    -CombinedCanonAndShow `
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

Expected: each of the four focused suites is launched exactly once, has a non-null integral root exit code `0`, reports `PASSED`, passes the reusable schema-v2 safety envelope plus the separate `COMPLETED` / helper-0 / no-timeout / zero-window gates, and retains unique helper request/stdout/stderr/result reports plus a unique runner log and external `SaveDir`. PID/count/error fields are diagnostics only. On a fifth fresh mirror, `missing-portraits-green` and `narration-overlap-green` each run once through their existing one-shot helper hosts. The existing `show-before-green` invocation remains one helper/receipt but its reviewed `show-before-scan.py` host sequentially runs the exact trusted-Python equivalent of `python -B Tools/scan_canon.py` and then the exact three-file show-before scan. Its one helper-owned stdout is a strict one-line JSON envelope containing separate canon/show exit codes and lossless base64 streams: canon must exit 0 with empty stderr and exactly one complete summary; show must exit 0 with empty stdout/stderr. The outer host also exits 0 with empty stderr and the full private-desktop envelope. No new invocation, receipt field, durable leaf, or process-evidence directory is added. Finally, a sixth fresh mirror runs lint exactly once. Stop immediately on the first `NEEDS_CONTEXT`; preserve completed and failed invocation evidence and never repeat an invocation on the same bytes.

- [ ] **Step 10: Check exact scope and commit the rules slice**

```powershell
$UnrelatedPlan = 'docs/superpowers/plans/2026-08-09-winter-interlude-narrative-delivery.md'
$UnrelatedSha256 = '0F39B5F5ACE1D4666DD146863CABDF398B031F5666C29AE337CEB89796E4276C'
$ExpectedPaths = @('game/balance.rpy', 'game/difficulty.rpy', 'game/test_game.rpy')
$Task1AuthorityBeforeRulesCommit = Assert-RecoveryTask1CompletionCurrent 'before the Task 2 rules commit'
if ([string]$Task1AuthorityBeforeRulesCommit.completion_sha256 -cne $Task1CompletionHashAtTask2Start) {
    throw 'NEEDS_CONTEXT: Task 1 completion or one of its exact 141 current artifacts drifted before commit.'
}
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
    throw 'NEEDS_CONTEXT: approval-locked P3 -> exact rules R3 topology or sealed evidence drifted after commit.'
}
$RulesCommitPaths = @(git diff-tree --no-commit-id --name-only -r $RulesCommit | Sort-Object)
if (Compare-Object @('game/balance.rpy', 'game/difficulty.rpy', 'game/test_game.rpy') $RulesCommitPaths) {
    throw 'NEEDS_CONTEXT: R3 is not the exact approved three-path child of P3.'
}
```

Expected: the successful commit is a direct child of the executable-plan baseline, has the exact subject above, and contains exactly the three text `.rpy` paths. This post-commit check is mandatory because the repository pre-commit hook may update and stage `game/msyh.ttf`; any fourth path is `NEEDS_CONTEXT`, and the rules slice must not be described as complete. The index is empty and the only remaining status row is the protected unrelated plan.

- [ ] **Step 11: Seal the exact nine-invocation Task 2 completion record**

Only after Step 10 has proved the exact P2→S3→P3→R3 chain may this create-new record be written. It is the sole machine authority consumed by Task 3; Markdown output is not a substitute.

```powershell
$Task2CompletionRecord = Join-Path $Task2EvidenceRoot 'task2-completion.json'
if (Test-Path -LiteralPath $Task2CompletionRecord) {
    throw 'NEEDS_CONTEXT: Task 2 completion record already exists; do not overwrite or replay Task 2.'
}
$Task1AuthorityBeforeTask2Seal = Assert-RecoveryTask1CompletionCurrent 'before Task 2 completion sealing'
if ((Get-FileHash -LiteralPath $ApprovalLockPath -Algorithm SHA256).Hash -cne $ApprovalLockHashAtTask2Start -or
    [string]$Task1AuthorityBeforeTask2Seal.completion_sha256 -cne $Task1CompletionHashAtTask2Start -or
    (git rev-parse HEAD) -cne $RulesCommit -or
    (git rev-parse ($RulesCommit + '^')) -cne [string]$ApprovalRecord.approved_plan_commit) {
    throw 'NEEDS_CONTEXT: approval, Task 1, or P2-to-R3 state drifted before Task 2 sealing.'
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
        if ([string]$Spec.name -ceq 'show-before-green') {
            $null = Assert-Task2CombinedCanonShowOutput `
                -StdoutPath ([string]$Receipt.direct_evidence[0].path) `
                -StderrPath ([string]$Receipt.direct_evidence[1].path) `
                -ExpectedWorkingDirectory ([string]$Spec.value.scanner_working_directory) `
                -Context ('sealed receipt ' + [string]$Spec.name)
        } else {
            $ScannerOut = [IO.File]::ReadAllText([string]$Receipt.direct_evidence[0].path, $StrictUtf8)
            $ScannerErr = [IO.File]::ReadAllText([string]$Receipt.direct_evidence[1].path, $StrictUtf8)
            if ($ScannerErr.Length -ne 0 -or
                ([string]$Spec.name -ceq 'missing-portraits-green' -and
                 [regex]::Matches($ScannerOut, '(?m)^=== Total findings: 0 ===\s*$').Count -ne 1) -or
                ([string]$Spec.name -ceq 'narration-overlap-green' -and
                 [regex]::Matches($ScannerOut, '(?m)^TOTAL:\s+0\b.*$').Count -ne 1)) {
                throw ('NEEDS_CONTEXT: sealed scanner output contradicts its receipt: ' + [string]$Spec.name)
            }
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
    New-Task2ExternallyBoundSeal $PlanPath ([string]$ApprovalRecord.plan_sha256)
    New-Task2ExternallyBoundSeal $SpecPath ([string]$ApprovalRecord.spec_sha256)
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
    schema_version = 3
    verdict = 'PASS'
    approved_plan_lock_sha256 = $ApprovalLockHashAtTask2Start
    task1_completion_path = (Resolve-Path -LiteralPath $Task1CompletionRecord).Path
    task1_completion_sha256 = $Task1CompletionHashAtTask2Start
    approved_plan_commit = [string]$ApprovalRecord.approved_plan_commit
    approved_spec_commit = [string]$ApprovalRecord.spec_commit
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
$Task2CompletionCheck = Read-RecoveryStrictJson $Task2CompletionRecord 'Task 2 completion record'
$ExpectedTask2CompletionProperties = @(
    'schema_version','verdict','approved_plan_lock_sha256','task1_completion_path',
    'task1_completion_sha256','approved_plan_commit','approved_spec_commit','rules_commit','rules_parent_commit',
    'rules_subject','rules_paths','invocation_count','invocations','artifact_count','artifacts','finished_utc'
)
if ($Task2CompletionCheck -isnot [pscustomobject] -or
    (@($Task2CompletionCheck.PSObject.Properties.Name) -join '|') -cne ($ExpectedTask2CompletionProperties -join '|') -or
    $Task2CompletionCheck.schema_version -isnot [int] -or [int]$Task2CompletionCheck.schema_version -ne 3 -or
    $Task2CompletionCheck.verdict -isnot [string] -or $Task2CompletionCheck.verdict -cne 'PASS' -or
    $Task2CompletionCheck.approved_plan_lock_sha256 -isnot [string] -or $Task2CompletionCheck.approved_plan_lock_sha256 -cne $ApprovalLockHashAtTask2Start -or
    $Task2CompletionCheck.task1_completion_path -isnot [string] -or $Task2CompletionCheck.task1_completion_path -cne (Resolve-Path -LiteralPath $Task1CompletionRecord).Path -or
    $Task2CompletionCheck.task1_completion_sha256 -isnot [string] -or $Task2CompletionCheck.task1_completion_sha256 -cne $Task1CompletionHashAtTask2Start -or
    $Task2CompletionCheck.approved_plan_commit -isnot [string] -or $Task2CompletionCheck.approved_plan_commit -cne [string]$ApprovalRecord.approved_plan_commit -or
    $Task2CompletionCheck.approved_spec_commit -isnot [string] -or $Task2CompletionCheck.approved_spec_commit -cne [string]$ApprovalRecord.spec_commit -or
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

Expected: the strict read-only schema-v3 record binds the immutable v3 approval lock, Task 1 schema-v3 completion hash, exact P2→S3→P3→R3 ancestry/subject/three paths, exactly nine named PASS invocations (one RED, four GREEN suites, three scanners, one lint), their expected and actual outcomes, helper evidence/result, and runner/scanner direct evidence. Its exact 56-file union is the four externally bound authorities, nine invocation-time receipt locators, 36 helper artifacts, six distinct suite/lint runner outputs, and one distinct show-before source; scanner stdout/stderr alias helper artifacts, `helper_result` aliases the fourth helper artifact, and the show source aliases its third direct evidence, so none is counted twice. Every duplicate path must carry the identical pre-existing seal, and the completion reread compares every invocation and sorted artifact row to the pre-write structures rather than re-baselining current bytes. Neither the lock nor either completion record is a cleanup target. The `show-before-green` stdout seal is re-parsed with the same combined-output validator, proving the exact canon command and the show scan independently without changing the receipt schema or 56-file union.

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
- Create ignored prompts/results only: `.superpowers/sdd/terminal-collapse-ending/recovery-v3/copy/run-01/`, `run-02/`, `run-03/`
- Create ignored blind map only: `.superpowers/sdd/terminal-collapse-ending/recovery-v3/copy/blind-map.md`

- [ ] **Step 0: Validate the immutable v3 approval lock and exact P2-to-R3 topology before reading project inputs**

The controller must provide `$ApprovalLockSha256` out of band when it opens this fresh persistent Windows PowerShell 5.1 session. This is Task 3's first project action. Do not read `CANON.md`, guidance, prose context, Task 1/2 evidence, or any other repository file before this approval lock and P2→S3→P3→R3 topology gate passes:

```powershell
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
if ($PSVersionTable.PSEdition -cne 'Desktop' -or $PSVersionTable.PSVersion.Major -ne 5) {
    throw 'NEEDS_CONTEXT: Task 3 requires Windows PowerShell 5.1 Desktop.'
}
$ApprovalLockVariable = Get-Variable -Name ApprovalLockSha256 -Scope 0 -ErrorAction SilentlyContinue
if ($null -eq $ApprovalLockVariable -or $ApprovalLockVariable.Value -isnot [string] -or
    [string]$ApprovalLockVariable.Value -cnotmatch '^[0-9A-F]{64}$') {
    throw 'NEEDS_CONTEXT: Task 3 controller did not bind the out-of-band ApprovalLockSha256 parameter.'
}
$ApprovalLockSha256 = [string]$ApprovalLockVariable.Value
$Scope0Location = Get-Location
if ($Scope0Location.Provider.Name -cne 'FileSystem') {
    throw 'NEEDS_CONTEXT: Task 3 Scope0 must start in a filesystem location.'
}
$Scope0ProjectRoot = [IO.Path]::GetFullPath([string]$Scope0Location.Path)
$ApprovalLockPath = [IO.Path]::GetFullPath(
    [IO.Path]::Combine($Scope0ProjectRoot, '.superpowers\sdd\terminal-collapse-ending\approved-plan-lock-v3.json'))
if (-not (Test-Path -LiteralPath $ApprovalLockPath -PathType Leaf)) {
    throw 'NEEDS_CONTEXT: approval lock v3 is missing.'
}
$ApprovalLockPhysicalSha256 = (Get-FileHash -LiteralPath $ApprovalLockPath -Algorithm SHA256).Hash
if ($ApprovalLockPhysicalSha256 -cne $ApprovalLockSha256) {
    throw 'NEEDS_CONTEXT: approval lock v3 differs from the out-of-band physical SHA-256.'
}

$ProjectRoot = (Resolve-Path -LiteralPath '.').Path
if (-not $ProjectRoot.Equals($Scope0ProjectRoot, [StringComparison]::OrdinalIgnoreCase)) {
    throw 'NEEDS_CONTEXT: Task 3 project root changed after Scope0 lock authentication.'
}
$EvidenceRoot = Join-Path $ProjectRoot '.superpowers\sdd\terminal-collapse-ending'
$StrictUtf8 = New-Object System.Text.UTF8Encoding($false, $true)
$ThisPlan = 'docs/superpowers/plans/2026-08-14-terminal-collapse-generator-recovery-v3.md'
$DesignPath = 'docs/superpowers/specs/2026-08-14-terminal-collapse-generator-recovery-v3-design.md'
$P2 = '25c2ea674948ad89e8b48befb89643a8687648a4'
$S3 = '5fa8fb14792e095e066c3e9f698eda9ea4380854'
$SpecSha256 = '978116FE22B8C65578B78E800EF6039053284EA7E674271646D130BBB4BBF470'
$UnrelatedPlan = 'docs/superpowers/plans/2026-08-09-winter-interlude-narrative-delivery.md'
$UnrelatedPlanHash = '0F39B5F5ACE1D4666DD146863CABDF398B031F5666C29AE337CEB89796E4276C'
$RecoveryRoot = Join-Path $EvidenceRoot 'recovery-v3'
$ExpectedPredecessorLockPath = [IO.Path]::GetFullPath((Join-Path $EvidenceRoot 'approved-plan-lock-v2.json')).TrimEnd('\')
$ExpectedPredecessorManifestPath = [IO.Path]::GetFullPath((Join-Path $RecoveryRoot 'predecessor-evidence.json')).TrimEnd('\')
$ExpectedSupersededAttemptPath = [IO.Path]::GetFullPath((Join-Path $EvidenceRoot 'recovery-v2\generator-attempt\attempt.json')).TrimEnd('\')
$ExpectedGeneratorLedgerPath = [IO.Path]::GetFullPath((Join-Path $RecoveryRoot 'generator-attempt')).TrimEnd('\')
$ExpectedObserverLedgerPath = [IO.Path]::GetFullPath((Join-Path $RecoveryRoot 'observer-attempt')).TrimEnd('\')
if (-not (Get-Item -LiteralPath $ApprovalLockPath).IsReadOnly) {
    throw 'NEEDS_CONTEXT: approval lock v3 is writable.'
}
git check-ignore -q -- $ApprovalLockPath
if ($LASTEXITCODE -ne 0) { throw 'NEEDS_CONTEXT: approval lock v3 is not ignored.' }
$ApprovalLockBytes = [IO.File]::ReadAllBytes($ApprovalLockPath)
if ($ApprovalLockBytes.Length -eq 0 -or
    ($ApprovalLockBytes.Length -ge 3 -and $ApprovalLockBytes[0] -eq 0xEF -and
     $ApprovalLockBytes[1] -eq 0xBB -and $ApprovalLockBytes[2] -eq 0xBF)) {
    throw 'NEEDS_CONTEXT: approved-plan lock is empty or has a BOM.'
}
$ApprovalLockText = $StrictUtf8.GetString($ApprovalLockBytes)
$ApprovalExpectedProperties = @(
    'schema_version','purpose','approved_plan_path','approved_plan_commit','plan_sha256',
    'spec_path','spec_commit','spec_sha256','predecessor_plan_commit','predecessor_lock_path',
    'predecessor_lock_bytes','predecessor_lock_sha256','predecessor_manifest_path',
    'predecessor_manifest_bytes','predecessor_manifest_sha256','baseline_game_tree','generator_strategy',
    'superseded_generator_attempt_path','superseded_generator_attempt_sha256','superseded_generator_disposition',
    'generator_attempt_ledger_path','generator_attempt_limit','observer_attempt_ledger_path','observer_attempt_limit',
    'test_result_stream','engine_log_role'
)
$ApprovalRawProperties = @([regex]::Matches($ApprovalLockText, '"([^"\\]+)"\s*:') | ForEach-Object { $_.Groups[1].Value })
if ($ApprovalLockText.Contains([char]0xFFFD) -or
    -not $ApprovalLockText.EndsWith("`n", [StringComparison]::Ordinal) -or $ApprovalLockText.Contains("`r") -or
    $ApprovalRawProperties.Count -ne 26 -or
    ($ApprovalRawProperties -join '|') -cne ($ApprovalExpectedProperties -join '|')) {
    throw 'NEEDS_CONTEXT: approval lock v3 encoding or exact raw property contract failed.'
}
$ApprovalRecord = $ApprovalLockText | ConvertFrom-Json -ErrorAction Stop
if ($ApprovalRecord -isnot [pscustomobject] -or
    (@($ApprovalRecord.PSObject.Properties.Name) -join '|') -cne ($ApprovalExpectedProperties -join '|') -or
    $ApprovalRecord.schema_version -isnot [int] -or [int]$ApprovalRecord.schema_version -ne 3 -or
    $ApprovalRecord.purpose -isnot [string] -or [string]$ApprovalRecord.purpose -cne 'terminal-collapse-generator-recovery-v3' -or
    $ApprovalRecord.approved_plan_path -isnot [string] -or [string]$ApprovalRecord.approved_plan_path -cne $ThisPlan -or
    $ApprovalRecord.approved_plan_commit -isnot [string] -or [string]$ApprovalRecord.approved_plan_commit -cnotmatch '^[0-9a-f]{40}$' -or
    $ApprovalRecord.plan_sha256 -isnot [string] -or [string]$ApprovalRecord.plan_sha256 -cnotmatch '^[0-9A-F]{64}$' -or
    $ApprovalRecord.spec_path -isnot [string] -or [string]$ApprovalRecord.spec_path -cne $DesignPath -or
    $ApprovalRecord.spec_commit -isnot [string] -or [string]$ApprovalRecord.spec_commit -cne $S3 -or
    $ApprovalRecord.spec_sha256 -isnot [string] -or [string]$ApprovalRecord.spec_sha256 -cne $SpecSha256 -or
    $ApprovalRecord.predecessor_plan_commit -isnot [string] -or [string]$ApprovalRecord.predecessor_plan_commit -cne $P2 -or
    $ApprovalRecord.predecessor_lock_path -isnot [string] -or [string]$ApprovalRecord.predecessor_lock_path -cne $ExpectedPredecessorLockPath -or
    $ApprovalRecord.predecessor_lock_bytes -isnot [int] -or [int]$ApprovalRecord.predecessor_lock_bytes -ne 1957 -or
    $ApprovalRecord.predecessor_lock_sha256 -isnot [string] -or [string]$ApprovalRecord.predecessor_lock_sha256 -cne '592E9F1FD5C4996A8612005BE9A33A35721A63228AAB43811208099265AECF8B' -or
    $ApprovalRecord.predecessor_manifest_path -isnot [string] -or [string]$ApprovalRecord.predecessor_manifest_path -cne $ExpectedPredecessorManifestPath -or
    -not ($ApprovalRecord.predecessor_manifest_bytes -is [int] -or $ApprovalRecord.predecessor_manifest_bytes -is [long]) -or
    [int64]$ApprovalRecord.predecessor_manifest_bytes -le 0 -or
    $ApprovalRecord.predecessor_manifest_sha256 -isnot [string] -or [string]$ApprovalRecord.predecessor_manifest_sha256 -cnotmatch '^[0-9A-F]{64}$' -or
    $ApprovalRecord.baseline_game_tree -isnot [string] -or [string]$ApprovalRecord.baseline_game_tree -cne 'fa7a398e9d989731b24e3c1642f3e2e33ce846ff' -or
    $ApprovalRecord.generator_strategy -isnot [string] -or [string]$ApprovalRecord.generator_strategy -cne 'fresh_one_shot' -or
    $ApprovalRecord.superseded_generator_attempt_path -isnot [string] -or [string]$ApprovalRecord.superseded_generator_attempt_path -cne $ExpectedSupersededAttemptPath -or
    $ApprovalRecord.superseded_generator_attempt_sha256 -isnot [string] -or [string]$ApprovalRecord.superseded_generator_attempt_sha256 -cne '6C6D597580E80A448C0CE55A80C0955988970C2A6332854049420B8693D38DF0' -or
    $ApprovalRecord.superseded_generator_disposition -isnot [string] -or [string]$ApprovalRecord.superseded_generator_disposition -cne 'preserved_not_adopted_log_contract_mismatch' -or
    $ApprovalRecord.generator_attempt_ledger_path -isnot [string] -or [string]$ApprovalRecord.generator_attempt_ledger_path -cne $ExpectedGeneratorLedgerPath -or
    $ApprovalRecord.generator_attempt_limit -isnot [int] -or [int]$ApprovalRecord.generator_attempt_limit -ne 1 -or
    $ApprovalRecord.observer_attempt_ledger_path -isnot [string] -or [string]$ApprovalRecord.observer_attempt_ledger_path -cne $ExpectedObserverLedgerPath -or
    $ApprovalRecord.observer_attempt_limit -isnot [int] -or [int]$ApprovalRecord.observer_attempt_limit -ne 1 -or
    $ApprovalRecord.test_result_stream -isnot [string] -or [string]$ApprovalRecord.test_result_stream -cne 'helper_stdout' -or
    $ApprovalRecord.engine_log_role -isnot [string] -or [string]$ApprovalRecord.engine_log_role -cne 'diagnostic_only') {
    throw 'NEEDS_CONTEXT: approval lock v3 exact schema, native types, or values are invalid.'
}
$ExpectedRulesCommit = (& git rev-parse HEAD).Trim()
function Assert-Task3ApprovalState([string]$Context) {
    if (-not (Get-Item -LiteralPath $ApprovalLockPath).IsReadOnly -or
        (Get-FileHash -LiteralPath $ApprovalLockPath -Algorithm SHA256).Hash -cne $ApprovalLockSha256 -or
        (Get-FileHash -LiteralPath $ThisPlan -Algorithm SHA256).Hash -cne [string]$ApprovalRecord.plan_sha256 -or
        (& git hash-object --no-filters -- $ThisPlan).Trim() -cne
            (& git rev-parse ([string]$ApprovalRecord.approved_plan_commit + ':' + $ThisPlan)).Trim() -or
        (Get-FileHash -LiteralPath $DesignPath -Algorithm SHA256).Hash -cne [string]$ApprovalRecord.spec_sha256 -or
        (& git hash-object --no-filters -- $DesignPath).Trim() -cne
            (& git rev-parse ([string]$ApprovalRecord.spec_commit + ':' + $DesignPath)).Trim()) {
        throw ('NEEDS_CONTEXT: approval lock, plan, or specification drifted ' + $Context + '; do not invoke Opus.')
    }
    if ((& git rev-parse ([string]$ApprovalRecord.approved_plan_commit + '^')).Trim() -cne $S3 -or
        (& git rev-parse ($S3 + '^')).Trim() -cne $P2 -or
        (git log -1 --format=%s $S3) -cne 'docs: specify terminal collapse generator recovery v3' -or
        (@(git diff-tree --no-commit-id --name-only -r $S3) -join '|') -cne $DesignPath -or
        (git log -1 --format=%s ([string]$ApprovalRecord.approved_plan_commit)) -cne 'docs: plan terminal collapse generator recovery v3' -or
        (@(git diff-tree --no-commit-id --name-only -r ([string]$ApprovalRecord.approved_plan_commit)) -join '|') -cne $ThisPlan -or
        (& git rev-parse ([string]$ApprovalRecord.approved_plan_commit + ':game')).Trim() -cne [string]$ApprovalRecord.baseline_game_tree -or
        (& git rev-parse HEAD).Trim() -cne $ExpectedRulesCommit -or
        (& git rev-parse ($ExpectedRulesCommit + '^')).Trim() -cne [string]$ApprovalRecord.approved_plan_commit -or
        (git log -1 --format=%s $ExpectedRulesCommit) -cne 'fix: enforce terminal resistance collapse rules') {
        throw ('NEEDS_CONTEXT: exact P2 -> S3 -> P3 -> R3 ancestry/subject/tree drifted ' + $Context + '; do not invoke Opus.')
    }
    if (-not (Test-Path -LiteralPath $ExpectedPredecessorManifestPath -PathType Leaf) -or
        -not (Get-Item -LiteralPath $ExpectedPredecessorManifestPath).IsReadOnly -or
        (Get-Item -LiteralPath $ExpectedPredecessorManifestPath).Length -ne [int64]$ApprovalRecord.predecessor_manifest_bytes -or
        (Get-FileHash -LiteralPath $ExpectedPredecessorManifestPath -Algorithm SHA256).Hash -cne [string]$ApprovalRecord.predecessor_manifest_sha256) {
        throw ('NEEDS_CONTEXT: predecessor manifest seal drifted ' + $Context + '; do not invoke Opus.')
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
$Task1CompletionRecord = Join-Path $RecoveryRoot 'task1-completion.json'
$Task2CompletionRecord = Join-Path $RecoveryRoot 'rules\task2-completion.json'
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
    if ($Text.Contains([char]0xFFFD) -or
        -not $Text.EndsWith("`n", [StringComparison]::Ordinal) -or $Text.Contains("`r")) {
        throw ('NEEDS_CONTEXT: JSON is not canonical strict UTF-8/LF ' + $Context + '; do not invoke Opus.')
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
function Get-Task3CanonicalPath([string]$Path) {
    return [IO.Path]::GetFullPath($Path).TrimEnd([IO.Path]::DirectorySeparatorChar, [IO.Path]::AltDirectorySeparatorChar)
}
function Assert-Task3ExactProperties($Value, [string[]]$Expected, [string]$Context) {
    if ($Value -isnot [pscustomobject] -or
        (@($Value.PSObject.Properties.Name) -join '|') -cne ($Expected -join '|')) {
        throw ('NEEDS_CONTEXT: exact ordered properties failed ' + $Context + '; do not invoke Opus.')
    }
}
function Assert-Task3Task1Completion([string]$Context) {
    if (-not (Get-Item -LiteralPath $Task1CompletionRecord).IsReadOnly -or
        (Get-FileHash -LiteralPath $Task1CompletionRecord -Algorithm SHA256).Hash -cne $Task1CompletionSha256) {
        throw ('NEEDS_CONTEXT: Task 1 completion seal drifted ' + $Context + '; do not invoke Opus.')
    }
    $Task1 = Read-Task3StrictJsonObject $Task1CompletionRecord ('Task 1 completion ' + $Context)
    $TopProperties = @(
        'schema_version','verdict','approval','predecessor','baseline_game_tree','full_selftest',
        'version_probe','generator','observer','mother','artifact_count','artifacts','cleanup','finished_utc'
    )
    Assert-Task3ExactProperties $Task1 $TopProperties 'Task 1 completion'
    if ($Task1.schema_version -isnot [int] -or $Task1.schema_version -ne 3 -or
        $Task1.verdict -isnot [string] -or $Task1.verdict -cne 'PASS' -or
        $Task1.baseline_game_tree -isnot [string] -or $Task1.baseline_game_tree -cne [string]$ApprovalRecord.baseline_game_tree -or
        $Task1.artifact_count -isnot [int] -or $Task1.artifact_count -ne 141 -or
        $Task1.artifacts -isnot [Array] -or @($Task1.artifacts).Count -ne 141 -or
        $Task1.finished_utc -isnot [string]) {
        throw ('NEEDS_CONTEXT: Task 1 top-level contract failed ' + $Context + '; do not invoke Opus.')
    }
    try {
        [void][DateTimeOffset]::ParseExact(
            [string]$Task1.finished_utc, 'o', [Globalization.CultureInfo]::InvariantCulture,
            [Globalization.DateTimeStyles]::RoundtripKind)
    } catch { throw ('NEEDS_CONTEXT: Task 1 timestamp failed ' + $Context + '; do not invoke Opus.') }

    $ApprovalProperties = @(
        'lock_path','lock_bytes','lock_sha256','plan_path','plan_commit','plan_bytes','plan_sha256',
        'spec_path','spec_commit','spec_bytes','spec_sha256'
    )
    $PredecessorProperties = @(
        'manifest_path','manifest_bytes','manifest_sha256','artifact_count','catalog_bytes','catalog_sha256',
        'failures','source_inventories'
    )
    $FullSelftestProperties = @(
        'reused','attempt_path','attempt_bytes','attempt_sha256','completion_path','completion_bytes',
        'completion_sha256','root_path'
    )
    $VersionProbeProperties = @('reused','evidence_dir','request_sha256','stdout_sha256','stderr_sha256','result_sha256')
    $GeneratorProperties = @(
        'source','invocation_count','red_record_path','red_record_sha256','green_record_path','green_record_sha256',
        'attempt_path','attempt_sha256','completion_path','completion_sha256','evidence_dir','request_sha256',
        'result_sha256','state_path','state_sha256','rpytest_stdout_path','rpytest_stdout_bytes',
        'rpytest_stdout_sha256','stderr_sha256','fixture_evidence_path','fixture_evidence_sha256',
        'engine_log_evidence_path','engine_log_evidence_sha256','save_name','save_bytes','save_sha256',
        'target_copy_count'
    )
    $ObserverProperties = @(
        'invocation_count','attempt_path','attempt_sha256','completion_path','completion_sha256','evidence_dir',
        'request_sha256','result_sha256','state_path','state_sha256','stdout_sha256','stderr_sha256',
        'fixture_evidence_path','fixture_evidence_sha256','engine_log_evidence_path','engine_log_evidence_sha256'
    )
    Assert-Task3ExactProperties $Task1.approval $ApprovalProperties 'Task 1 approval'
    Assert-Task3ExactProperties $Task1.predecessor $PredecessorProperties 'Task 1 predecessor'
    Assert-Task3ExactProperties $Task1.full_selftest $FullSelftestProperties 'Task 1 full selftest'
    Assert-Task3ExactProperties $Task1.version_probe $VersionProbeProperties 'Task 1 version probe'
    Assert-Task3ExactProperties $Task1.generator $GeneratorProperties 'Task 1 generator'
    Assert-Task3ExactProperties $Task1.observer $ObserverProperties 'Task 1 observer'
    Assert-Task3ExactProperties $Task1.mother @('path','bytes','sha256','read_only') 'Task 1 mother'
    Assert-Task3ExactProperties $Task1.cleanup @(
        'generator_worktree_removed','generator_savedir_removed','observer_worktree_removed','observer_savedir_removed'
    ) 'Task 1 cleanup'

    $LockFull = Get-Task3CanonicalPath $ApprovalLockPath
    $PlanFull = Get-Task3CanonicalPath (Join-Path $ProjectRoot $ThisPlan)
    $SpecFull = Get-Task3CanonicalPath (Join-Path $ProjectRoot $DesignPath)
    $ManifestFull = Get-Task3CanonicalPath $ExpectedPredecessorManifestPath
    if ($Task1.approval.lock_path -isnot [string] -or $Task1.approval.lock_path -cne $LockFull -or
        -not (Test-Task3IntegralValue $Task1.approval.lock_bytes) -or
        [int64]$Task1.approval.lock_bytes -ne (Get-Item -LiteralPath $LockFull).Length -or
        $Task1.approval.lock_sha256 -isnot [string] -or $Task1.approval.lock_sha256 -cne $ApprovalLockSha256 -or
        $Task1.approval.plan_path -isnot [string] -or $Task1.approval.plan_path -cne $PlanFull -or
        $Task1.approval.plan_commit -isnot [string] -or $Task1.approval.plan_commit -cne [string]$ApprovalRecord.approved_plan_commit -or
        -not (Test-Task3IntegralValue $Task1.approval.plan_bytes) -or
        [int64]$Task1.approval.plan_bytes -ne (Get-Item -LiteralPath $PlanFull).Length -or
        $Task1.approval.plan_sha256 -isnot [string] -or $Task1.approval.plan_sha256 -cne [string]$ApprovalRecord.plan_sha256 -or
        $Task1.approval.spec_path -isnot [string] -or $Task1.approval.spec_path -cne $SpecFull -or
        $Task1.approval.spec_commit -isnot [string] -or $Task1.approval.spec_commit -cne [string]$ApprovalRecord.spec_commit -or
        -not (Test-Task3IntegralValue $Task1.approval.spec_bytes) -or
        [int64]$Task1.approval.spec_bytes -ne (Get-Item -LiteralPath $SpecFull).Length -or
        $Task1.approval.spec_sha256 -isnot [string] -or $Task1.approval.spec_sha256 -cne [string]$ApprovalRecord.spec_sha256) {
        throw ('NEEDS_CONTEXT: Task 1 approval lineage failed ' + $Context + '; do not invoke Opus.')
    }
    if ($Task1.predecessor.manifest_path -isnot [string] -or $Task1.predecessor.manifest_path -cne $ManifestFull -or
        -not (Test-Task3IntegralValue $Task1.predecessor.manifest_bytes) -or
        [int64]$Task1.predecessor.manifest_bytes -ne [int64]$ApprovalRecord.predecessor_manifest_bytes -or
        $Task1.predecessor.manifest_sha256 -isnot [string] -or
        $Task1.predecessor.manifest_sha256 -cne [string]$ApprovalRecord.predecessor_manifest_sha256 -or
        $Task1.predecessor.artifact_count -isnot [int] -or $Task1.predecessor.artifact_count -ne 115 -or
        $Task1.predecessor.catalog_bytes -isnot [int] -or $Task1.predecessor.catalog_bytes -ne 24660 -or
        $Task1.predecessor.catalog_sha256 -isnot [string] -or
        $Task1.predecessor.catalog_sha256 -cne '9694E728A82F6DDC743DA5E83967EAC7EE02FFA62FA53E21F4A2374F27DDDA24' -or
        $Task1.predecessor.failures -isnot [Array] -or @($Task1.predecessor.failures).Count -ne 2 -or
        $Task1.predecessor.source_inventories -isnot [Array] -or @($Task1.predecessor.source_inventories).Count -ne 2) {
        throw ('NEEDS_CONTEXT: Task 1 predecessor lineage failed ' + $Context + '; do not invoke Opus.')
    }
    if ($Task1.full_selftest.reused -isnot [bool] -or -not $Task1.full_selftest.reused -or
        $Task1.version_probe.reused -isnot [bool] -or -not $Task1.version_probe.reused -or
        $Task1.generator.source -isnot [string] -or $Task1.generator.source -cne 'fresh_generator_v3' -or
        $Task1.generator.invocation_count -isnot [int] -or $Task1.generator.invocation_count -ne 1 -or
        $Task1.generator.target_copy_count -isnot [int] -or $Task1.generator.target_copy_count -ne 3 -or
        $Task1.observer.invocation_count -isnot [int] -or $Task1.observer.invocation_count -ne 1 -or
        $Task1.mother.read_only -isnot [bool] -or -not $Task1.mother.read_only -or
        @($Task1.cleanup.PSObject.Properties.Value | Where-Object { $_ -isnot [bool] -or -not $_ }).Count -ne 0) {
        throw ('NEEDS_CONTEXT: Task 1 reuse/invocation/cleanup contract failed ' + $Context + '; do not invoke Opus.')
    }

    $Manifest = Read-Task3StrictJsonObject $ManifestFull ('predecessor manifest ' + $Context)
    Assert-Task3ExactProperties $Manifest @(
        'schema_version','purpose','predecessor_plan_commit','predecessor_lock_sha256','artifact_count',
        'catalog_bytes','catalog_sha256','artifacts','failures','source_inventories','created_utc'
    ) 'predecessor manifest'
    if ($Manifest.schema_version -isnot [int] -or $Manifest.schema_version -ne 2 -or
        $Manifest.purpose -isnot [string] -or $Manifest.purpose -cne 'terminal-collapse-generator-recovery-v3-predecessor' -or
        $Manifest.predecessor_plan_commit -isnot [string] -or $Manifest.predecessor_plan_commit -cne $P2 -or
        $Manifest.predecessor_lock_sha256 -isnot [string] -or
        $Manifest.predecessor_lock_sha256 -cne '592E9F1FD5C4996A8612005BE9A33A35721A63228AAB43811208099265AECF8B' -or
        $Manifest.artifact_count -isnot [int] -or $Manifest.artifact_count -ne 115 -or
        $Manifest.artifacts -isnot [Array] -or @($Manifest.artifacts).Count -ne 115 -or
        $Manifest.catalog_bytes -isnot [int] -or $Manifest.catalog_bytes -ne 24660 -or
        $Manifest.catalog_sha256 -isnot [string] -or
        $Manifest.catalog_sha256 -cne '9694E728A82F6DDC743DA5E83967EAC7EE02FFA62FA53E21F4A2374F27DDDA24' -or
        $Manifest.failures -isnot [Array] -or @($Manifest.failures).Count -ne 2 -or
        $Manifest.source_inventories -isnot [Array] -or @($Manifest.source_inventories).Count -ne 2 -or
        ($Manifest.failures | ConvertTo-Json -Depth 100 -Compress) -cne
            ($Task1.predecessor.failures | ConvertTo-Json -Depth 100 -Compress) -or
        ($Manifest.source_inventories | ConvertTo-Json -Depth 100 -Compress) -cne
            ($Task1.predecessor.source_inventories | ConvertTo-Json -Depth 100 -Compress) -or
        $Manifest.failures[0].classification -cne 'TIMEOUT' -or
        $Manifest.failures[0].candidate_save_disposition -cne 'preserved_not_used' -or
        $Manifest.failures[1].classification -cne 'GOVERNANCE_CONTRACT_FAILURE' -or
        $Manifest.failures[1].reason -cne 'LOG_CONTRACT_MISMATCH' -or
        $Manifest.failures[1].candidate_save_disposition -cne 'preserved_not_used') {
        throw ('NEEDS_CONTEXT: predecessor manifest contract failed ' + $Context + '; do not invoke Opus.')
    }
    $FailureProperties = @(
        'id','classification','program_outcome','reason','generator_invocation_count','observer_invocation_count',
        'attempt_path','attempt_sha256','result_path','result_bytes','result_sha256','state_path','state_bytes',
        'state_sha256','test_report_path','test_report_bytes','test_report_sha256','engine_log_path',
        'engine_log_bytes','engine_log_sha256','target_copies','candidate_save_disposition'
    )
    foreach ($Failure in @($Manifest.failures)) {
        Assert-Task3ExactProperties $Failure $FailureProperties ('predecessor failure ' + [string]$Failure.id)
        if ($Failure.candidate_save_disposition -isnot [string] -or
            $Failure.candidate_save_disposition -cne 'preserved_not_used' -or
            -not (Test-Task3IntegralValue $Failure.generator_invocation_count) -or
            -not (Test-Task3IntegralValue $Failure.observer_invocation_count)) {
            throw ('NEEDS_CONTEXT: predecessor failure type/disposition drifted ' + $Context + '; do not invoke Opus.')
        }
        foreach ($TargetCopy in @($Failure.target_copies)) {
            Assert-Task3ExactProperties $TargetCopy @('role','path','bytes','sha256') ('failure target copy ' + [string]$Failure.id)
            $null = Assert-Task3FileSealStrict $TargetCopy ('failure target copy ' + [string]$Failure.id)
        }
    }
    if ($Manifest.failures[0].id -cne 'legacy_generator' -or
        $Manifest.failures[0].classification -cne 'TIMEOUT' -or
        $Manifest.failures[1].id -cne 'v2_generator' -or
        $Manifest.failures[1].classification -cne 'GOVERNANCE_CONTRACT_FAILURE' -or
        $Manifest.failures[1].reason -cne 'LOG_CONTRACT_MISMATCH') {
        throw ('NEEDS_CONTEXT: ordered dual-failure identity drifted ' + $Context + '; do not invoke Opus.')
    }
    $InventoryProperties = @(
        'id','root_path','authority_file_count','authority_files','excluded_cache_count','excluded_cache_files'
    )
    foreach ($Inventory in @($Manifest.source_inventories)) {
        Assert-Task3ExactProperties $Inventory $InventoryProperties ('source inventory ' + [string]$Inventory.id)
        if (-not (Test-Task3IntegralValue $Inventory.authority_file_count) -or
            -not (Test-Task3IntegralValue $Inventory.excluded_cache_count) -or
            [int64]$Inventory.authority_file_count -ne @($Inventory.authority_files).Count -or
            [int64]$Inventory.excluded_cache_count -ne @($Inventory.excluded_cache_files).Count) {
            throw ('NEEDS_CONTEXT: source-inventory counts drifted ' + $Context + '; do not invoke Opus.')
        }
        foreach ($InventoryFile in @($Inventory.authority_files) + @($Inventory.excluded_cache_files)) {
            Assert-Task3ExactProperties $InventoryFile @('relative_path','bytes','sha256') ('source inventory file ' + [string]$Inventory.id)
            if ($InventoryFile.relative_path -isnot [string] -or
                -not (Test-Task3IntegralValue $InventoryFile.bytes) -or
                $InventoryFile.sha256 -isnot [string] -or $InventoryFile.sha256 -cnotmatch '^[0-9A-F]{64}$') {
                throw ('NEEDS_CONTEXT: source-inventory file types drifted ' + $Context + '; do not invoke Opus.')
            }
        }
    }
    if ($Manifest.source_inventories[0].id -cne 'v2_generator_worktree_task_owned' -or
        [int64]$Manifest.source_inventories[0].authority_file_count -ne 8 -or
        $Manifest.source_inventories[1].id -cne 'v2_generator_savedir' -or
        [int64]$Manifest.source_inventories[1].authority_file_count -ne 12) {
        throw ('NEEDS_CONTEXT: ordered source-inventory identity/count drifted ' + $Context + '; do not invoke Opus.')
    }

    $ArtifactLookup = New-Object 'System.Collections.Generic.Dictionary[string,object]' ([StringComparer]::OrdinalIgnoreCase)
    $ObservedPaths = New-Object 'System.Collections.Generic.List[string]'
    foreach ($Artifact in @($Task1.artifacts)) {
        $null = Assert-Task3FileSealStrict $Artifact 'Task 1 artifact'
        if ($ArtifactLookup.ContainsKey([string]$Artifact.path)) {
            throw ('NEEDS_CONTEXT: duplicate Task 1 artifact path ' + [string]$Artifact.path + '; do not invoke Opus.')
        }
        $ArtifactLookup.Add([string]$Artifact.path, $Artifact)
        [void]$ObservedPaths.Add([string]$Artifact.path)
    }
    $ObservedSorted = [string[]]$ObservedPaths.ToArray().Clone()
    [Array]::Sort($ObservedSorted, [StringComparer]::Ordinal)
    if (($ObservedPaths.ToArray() -join "`n") -cne ($ObservedSorted -join "`n")) {
        throw ('NEEDS_CONTEXT: Task 1 artifacts are not Ordinal-sorted ' + $Context + '; do not invoke Opus.')
    }
    $RequiredPaths = New-Object 'System.Collections.Generic.List[string]'
    foreach ($PredecessorSeal in @($Manifest.artifacts)) {
        $null = Assert-Task3FileSealStrict $PredecessorSeal 'predecessor artifact'
        if (-not $ArtifactLookup.ContainsKey([string]$PredecessorSeal.path) -or
            -not (Test-Task3FileSealIdentity $ArtifactLookup[[string]$PredecessorSeal.path] $PredecessorSeal)) {
            throw ('NEEDS_CONTEXT: Task 1/predecessor seal relation failed ' + [string]$PredecessorSeal.path)
        }
        [void]$RequiredPaths.Add([string]$PredecessorSeal.path)
    }
    foreach ($Path in @(
        $LockFull,$SpecFull,$PlanFull,$ManifestFull,
        [string]$Task1.generator.red_record_path,[string]$Task1.generator.green_record_path,
        [string]$Task1.generator.attempt_path,[string]$Task1.generator.completion_path,
        (Join-Path ([string]$Task1.generator.evidence_dir) 'request.json'),
        (Join-Path ([string]$Task1.generator.evidence_dir) 'stdout.txt'),
        (Join-Path ([string]$Task1.generator.evidence_dir) 'stderr.txt'),
        (Join-Path ([string]$Task1.generator.evidence_dir) 'result.json'),
        [string]$Task1.generator.state_path,[string]$Task1.generator.fixture_evidence_path,[string]$Task1.generator.engine_log_evidence_path,
        [string]$Task1.observer.attempt_path,[string]$Task1.observer.completion_path,
        (Join-Path ([string]$Task1.observer.evidence_dir) 'request.json'),
        (Join-Path ([string]$Task1.observer.evidence_dir) 'stdout.txt'),
        (Join-Path ([string]$Task1.observer.evidence_dir) 'stderr.txt'),
        (Join-Path ([string]$Task1.observer.evidence_dir) 'result.json'),
        [string]$Task1.observer.state_path,[string]$Task1.observer.fixture_evidence_path,[string]$Task1.observer.engine_log_evidence_path,
        [string]$Task1.mother.path,(Join-Path $RecoveryRoot 'baseline-evidence.md')
    )) { [void]$RequiredPaths.Add((Get-Task3CanonicalPath $Path)) }
    $RequiredSeen = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
    foreach ($RequiredPath in $RequiredPaths) {
        if (-not $RequiredSeen.Add($RequiredPath)) {
            throw ('NEEDS_CONTEXT: duplicate required Task 1 artifact ' + $RequiredPath + '; do not invoke Opus.')
        }
    }
    $RequiredSorted = [string[]]$RequiredPaths.ToArray().Clone()
    [Array]::Sort($RequiredSorted, [StringComparer]::Ordinal)
    if ($RequiredPaths.Count -ne 141 -or $RequiredSeen.Count -ne 141 -or
        $ArtifactLookup.ContainsKey((Get-Task3CanonicalPath $Task1CompletionRecord)) -or
        ($RequiredSorted -join "`n") -cne ($ObservedSorted -join "`n")) {
        throw ('NEEDS_CONTEXT: Task 1 exact 115 plus 26 artifact union failed ' + $Context + '; do not invoke Opus.')
    }

    foreach ($ReusedSeal in @(
        [pscustomobject][ordered]@{
            path=[string]$Task1.full_selftest.attempt_path
            bytes=$Task1.full_selftest.attempt_bytes
            sha256=[string]$Task1.full_selftest.attempt_sha256
        },
        [pscustomobject][ordered]@{
            path=[string]$Task1.full_selftest.completion_path
            bytes=$Task1.full_selftest.completion_bytes
            sha256=[string]$Task1.full_selftest.completion_sha256
        }
    )) {
        $ReusedPath = Get-Task3CanonicalPath ([string]$ReusedSeal.path)
        if (-not $ArtifactLookup.ContainsKey($ReusedPath) -or
            -not (Test-Task3FileSealIdentity $ArtifactLookup[$ReusedPath] $ReusedSeal)) {
            throw ('NEEDS_CONTEXT: reused full-selftest seal failed ' + $ReusedPath + '; do not invoke Opus.')
        }
    }
    $FullSelftestRoot = Get-Task3CanonicalPath ([string]$Task1.full_selftest.root_path)
    $VersionEvidenceDir = Get-Task3CanonicalPath ([string]$Task1.version_probe.evidence_dir)
    if (-not (Test-Path -LiteralPath $FullSelftestRoot -PathType Container) -or
        (Resolve-Path -LiteralPath $FullSelftestRoot).Path.TrimEnd('\') -cne $FullSelftestRoot -or
        -not (Test-Path -LiteralPath $VersionEvidenceDir -PathType Container) -or
        (Resolve-Path -LiteralPath $VersionEvidenceDir).Path.TrimEnd('\') -cne $VersionEvidenceDir) {
        throw ('NEEDS_CONTEXT: reused evidence directory contract failed ' + $Context + '; do not invoke Opus.')
    }
    foreach ($VersionName in @('request','stdout','stderr','result')) {
        $VersionExtension = if ($VersionName -ceq 'request' -or $VersionName -ceq 'result') { '.json' } else { '.txt' }
        $VersionPath = Get-Task3CanonicalPath (Join-Path $VersionEvidenceDir ($VersionName + $VersionExtension))
        $VersionHashProperty = $VersionName + '_sha256'
        if (-not $ArtifactLookup.ContainsKey($VersionPath) -or
            $Task1.version_probe.$VersionHashProperty -isnot [string] -or
            [string]$ArtifactLookup[$VersionPath].sha256 -cne [string]$Task1.version_probe.$VersionHashProperty) {
            throw ('NEEDS_CONTEXT: version-probe nested seal failed ' + $VersionName + '; do not invoke Opus.')
        }
    }

    foreach ($NestedSeal in @(
        [pscustomobject]@{ path=$Task1.generator.red_record_path; sha256=$Task1.generator.red_record_sha256 },
        [pscustomobject]@{ path=$Task1.generator.green_record_path; sha256=$Task1.generator.green_record_sha256 },
        [pscustomobject]@{ path=$Task1.generator.attempt_path; sha256=$Task1.generator.attempt_sha256 },
        [pscustomobject]@{ path=$Task1.generator.completion_path; sha256=$Task1.generator.completion_sha256 },
        [pscustomobject]@{ path=(Join-Path ([string]$Task1.generator.evidence_dir) 'request.json'); sha256=$Task1.generator.request_sha256 },
        [pscustomobject]@{ path=(Join-Path ([string]$Task1.generator.evidence_dir) 'result.json'); sha256=$Task1.generator.result_sha256 },
        [pscustomobject]@{ path=$Task1.generator.rpytest_stdout_path; sha256=$Task1.generator.rpytest_stdout_sha256 },
        [pscustomobject]@{ path=$Task1.generator.state_path; sha256=$Task1.generator.state_sha256 },
        [pscustomobject]@{ path=$Task1.generator.fixture_evidence_path; sha256=$Task1.generator.fixture_evidence_sha256 },
        [pscustomobject]@{ path=$Task1.generator.engine_log_evidence_path; sha256=$Task1.generator.engine_log_evidence_sha256 },
        [pscustomobject]@{ path=$Task1.observer.attempt_path; sha256=$Task1.observer.attempt_sha256 },
        [pscustomobject]@{ path=$Task1.observer.completion_path; sha256=$Task1.observer.completion_sha256 },
        [pscustomobject]@{ path=(Join-Path ([string]$Task1.observer.evidence_dir) 'request.json'); sha256=$Task1.observer.request_sha256 },
        [pscustomobject]@{ path=(Join-Path ([string]$Task1.observer.evidence_dir) 'result.json'); sha256=$Task1.observer.result_sha256 },
        [pscustomobject]@{ path=$Task1.observer.state_path; sha256=$Task1.observer.state_sha256 },
        [pscustomobject]@{ path=$Task1.observer.fixture_evidence_path; sha256=$Task1.observer.fixture_evidence_sha256 },
        [pscustomobject]@{ path=$Task1.observer.engine_log_evidence_path; sha256=$Task1.observer.engine_log_evidence_sha256 }
    )) {
        $NestedPath = Get-Task3CanonicalPath ([string]$NestedSeal.path)
        if (-not $ArtifactLookup.ContainsKey($NestedPath) -or $NestedSeal.sha256 -isnot [string] -or
            [string]$ArtifactLookup[$NestedPath].sha256 -cne [string]$NestedSeal.sha256) {
            throw ('NEEDS_CONTEXT: Task 1 nested artifact seal failed ' + $NestedPath + '; do not invoke Opus.')
        }
    }
    $MotherPath = Get-Task3CanonicalPath ([string]$Task1.mother.path)
    if (-not $ArtifactLookup.ContainsKey($MotherPath) -or -not (Get-Item -LiteralPath $MotherPath).IsReadOnly -or
        -not (Test-Task3IntegralValue $Task1.mother.bytes) -or [int64]$Task1.mother.bytes -le 0 -or
        $Task1.mother.sha256 -isnot [string] -or [string]$ArtifactLookup[$MotherPath].sha256 -cne [string]$Task1.mother.sha256 -or
        $Task1.generator.save_name -isnot [string] -or [IO.Path]::GetFileName($MotherPath) -cne [string]$Task1.generator.save_name -or
        -not (Test-Task3IntegralValue $Task1.generator.save_bytes) -or [int64]$Task1.generator.save_bytes -ne [int64]$Task1.mother.bytes -or
        $Task1.generator.save_sha256 -isnot [string] -or [string]$Task1.generator.save_sha256 -cne [string]$Task1.mother.sha256) {
        throw ('NEEDS_CONTEXT: Task 1 mother/generator lineage failed ' + $Context + '; do not invoke Opus.')
    }
    $GeneratorCompletion = Read-Task3StrictJsonObject ([string]$Task1.generator.completion_path) ('generator completion ' + $Context)
    $GeneratorCompletionProperties = @(
        'schema_version','attempt_id','attempt_path','attempt_sha256','approval_lock_sha256','approved_plan_commit',
        'predecessor_manifest_sha256','red_record_sha256','green_record_sha256','worktree_path','savedir_path',
        'process_evidence_dir','fixture_path','fixture_sha256','fixture_evidence_path','fixture_evidence_sha256',
        'request_path','request_bytes','request_sha256','result_path','result_bytes','result_sha256',
        'state_path','state_bytes','state_sha256','rpytest_stdout_path','rpytest_stdout_bytes',
        'rpytest_stdout_sha256','stderr_path','stderr_bytes','stderr_sha256','engine_log_evidence_path',
        'engine_log_evidence_sha256','external_save_path','sync_save_path','local_save_path','target_copy_count',
        'save_name','save_bytes','save_sha256','save_inventory','finished_utc'
    )
    Assert-Task3ExactProperties $GeneratorCompletion $GeneratorCompletionProperties 'generator completion'
    if ($GeneratorCompletion.schema_version -isnot [int] -or $GeneratorCompletion.schema_version -ne 2 -or
        $GeneratorCompletion.attempt_path -isnot [string] -or
        $GeneratorCompletion.attempt_path -cne [string]$Task1.generator.attempt_path -or
        $GeneratorCompletion.attempt_sha256 -isnot [string] -or
        $GeneratorCompletion.attempt_sha256 -cne [string]$Task1.generator.attempt_sha256 -or
        $GeneratorCompletion.approval_lock_sha256 -isnot [string] -or
        $GeneratorCompletion.approval_lock_sha256 -cne $ApprovalLockSha256 -or
        $GeneratorCompletion.approved_plan_commit -isnot [string] -or
        $GeneratorCompletion.approved_plan_commit -cne [string]$ApprovalRecord.approved_plan_commit -or
        $GeneratorCompletion.predecessor_manifest_sha256 -isnot [string] -or
        $GeneratorCompletion.predecessor_manifest_sha256 -cne [string]$ApprovalRecord.predecessor_manifest_sha256 -or
        $GeneratorCompletion.red_record_sha256 -isnot [string] -or
        $GeneratorCompletion.red_record_sha256 -cne [string]$Task1.generator.red_record_sha256 -or
        $GeneratorCompletion.green_record_sha256 -isnot [string] -or
        $GeneratorCompletion.green_record_sha256 -cne [string]$Task1.generator.green_record_sha256 -or
        $GeneratorCompletion.process_evidence_dir -isnot [string] -or
        $GeneratorCompletion.process_evidence_dir -cne [string]$Task1.generator.evidence_dir -or
        $GeneratorCompletion.request_sha256 -isnot [string] -or
        $GeneratorCompletion.request_sha256 -cne [string]$Task1.generator.request_sha256 -or
        $GeneratorCompletion.result_sha256 -isnot [string] -or
        $GeneratorCompletion.result_sha256 -cne [string]$Task1.generator.result_sha256 -or
        $GeneratorCompletion.state_path -isnot [string] -or
        $GeneratorCompletion.state_path -cne [string]$Task1.generator.state_path -or
        $GeneratorCompletion.state_sha256 -isnot [string] -or
        $GeneratorCompletion.state_sha256 -cne [string]$Task1.generator.state_sha256 -or
        $GeneratorCompletion.fixture_evidence_path -isnot [string] -or
        $GeneratorCompletion.fixture_evidence_path -cne [string]$Task1.generator.fixture_evidence_path -or
        $GeneratorCompletion.fixture_evidence_sha256 -isnot [string] -or
        $GeneratorCompletion.fixture_evidence_sha256 -cne [string]$Task1.generator.fixture_evidence_sha256 -or
        $GeneratorCompletion.rpytest_stdout_path -isnot [string] -or
        $GeneratorCompletion.rpytest_stdout_path -cne [string]$Task1.generator.rpytest_stdout_path -or
        -not (Test-Task3IntegralValue $GeneratorCompletion.rpytest_stdout_bytes) -or
        [int64]$GeneratorCompletion.rpytest_stdout_bytes -ne [int64]$Task1.generator.rpytest_stdout_bytes -or
        $GeneratorCompletion.rpytest_stdout_sha256 -isnot [string] -or
        $GeneratorCompletion.rpytest_stdout_sha256 -cne [string]$Task1.generator.rpytest_stdout_sha256 -or
        -not (Test-Task3IntegralValue $GeneratorCompletion.stderr_bytes) -or
        [int64]$GeneratorCompletion.stderr_bytes -ne 0 -or
        $GeneratorCompletion.stderr_sha256 -isnot [string] -or
        $GeneratorCompletion.stderr_sha256 -cne [string]$Task1.generator.stderr_sha256 -or
        $GeneratorCompletion.engine_log_evidence_path -isnot [string] -or
        $GeneratorCompletion.engine_log_evidence_path -cne [string]$Task1.generator.engine_log_evidence_path -or
        $GeneratorCompletion.engine_log_evidence_sha256 -isnot [string] -or
        $GeneratorCompletion.engine_log_evidence_sha256 -cne [string]$Task1.generator.engine_log_evidence_sha256 -or
        $GeneratorCompletion.target_copy_count -isnot [int] -or $GeneratorCompletion.target_copy_count -ne 3 -or
        $GeneratorCompletion.save_name -isnot [string] -or
        $GeneratorCompletion.save_name -cne [string]$Task1.generator.save_name -or
        -not (Test-Task3IntegralValue $GeneratorCompletion.save_bytes) -or
        [int64]$GeneratorCompletion.save_bytes -ne [int64]$Task1.mother.bytes -or
        $GeneratorCompletion.save_sha256 -isnot [string] -or
        $GeneratorCompletion.save_sha256 -cne [string]$Task1.mother.sha256) {
        throw ('NEEDS_CONTEXT: generator completion/mother lineage failed ' + $Context + '; do not invoke Opus.')
    }
    $ObserverCompletion = Read-Task3StrictJsonObject ([string]$Task1.observer.completion_path) ('observer completion ' + $Context)
    $ObserverCompletionProperties = @(
        'schema_version','attempt_id','attempt_path','attempt_sha256','approval_lock_sha256','approved_plan_commit',
        'generator_completion_sha256','worktree_path','savedir_path','process_evidence_dir','fixture_path','fixture_sha256',
        'fixture_evidence_path','fixture_evidence_sha256','request_path','request_bytes','request_sha256',
        'result_path','result_bytes','result_sha256','state_path','state_bytes','state_sha256','stdout_path',
        'stdout_bytes','stdout_sha256','stderr_path','stderr_bytes','stderr_sha256','engine_log_evidence_path',
        'engine_log_evidence_sha256','source_save_path','source_save_bytes','source_save_sha256_before',
        'source_save_sha256_after','replay_save_path','replay_save_bytes','replay_save_sha256_before',
        'replay_save_sha256_after','save_inventory','finished_utc'
    )
    Assert-Task3ExactProperties $ObserverCompletion $ObserverCompletionProperties 'observer completion'
    if ($ObserverCompletion.schema_version -isnot [int] -or $ObserverCompletion.schema_version -ne 2 -or
        $ObserverCompletion.attempt_path -isnot [string] -or
        $ObserverCompletion.attempt_path -cne [string]$Task1.observer.attempt_path -or
        $ObserverCompletion.attempt_sha256 -isnot [string] -or
        $ObserverCompletion.attempt_sha256 -cne [string]$Task1.observer.attempt_sha256 -or
        $ObserverCompletion.approval_lock_sha256 -isnot [string] -or $ObserverCompletion.approval_lock_sha256 -cne $ApprovalLockSha256 -or
        $ObserverCompletion.approved_plan_commit -isnot [string] -or $ObserverCompletion.approved_plan_commit -cne [string]$ApprovalRecord.approved_plan_commit -or
        $ObserverCompletion.generator_completion_sha256 -isnot [string] -or
        $ObserverCompletion.generator_completion_sha256 -cne [string]$Task1.generator.completion_sha256 -or
        $ObserverCompletion.process_evidence_dir -isnot [string] -or
        $ObserverCompletion.process_evidence_dir -cne [string]$Task1.observer.evidence_dir -or
        $ObserverCompletion.request_sha256 -isnot [string] -or
        $ObserverCompletion.request_sha256 -cne [string]$Task1.observer.request_sha256 -or
        $ObserverCompletion.result_sha256 -isnot [string] -or
        $ObserverCompletion.result_sha256 -cne [string]$Task1.observer.result_sha256 -or
        $ObserverCompletion.state_path -isnot [string] -or
        $ObserverCompletion.state_path -cne [string]$Task1.observer.state_path -or
        $ObserverCompletion.state_sha256 -isnot [string] -or
        $ObserverCompletion.state_sha256 -cne [string]$Task1.observer.state_sha256 -or
        $ObserverCompletion.fixture_evidence_path -isnot [string] -or
        $ObserverCompletion.fixture_evidence_path -cne [string]$Task1.observer.fixture_evidence_path -or
        $ObserverCompletion.fixture_evidence_sha256 -isnot [string] -or
        $ObserverCompletion.fixture_evidence_sha256 -cne [string]$Task1.observer.fixture_evidence_sha256 -or
        -not (Test-Task3IntegralValue $ObserverCompletion.stdout_bytes) -or
        [int64]$ObserverCompletion.stdout_bytes -ne 0 -or
        $ObserverCompletion.stdout_sha256 -isnot [string] -or
        $ObserverCompletion.stdout_sha256 -cne [string]$Task1.observer.stdout_sha256 -or
        -not (Test-Task3IntegralValue $ObserverCompletion.stderr_bytes) -or
        [int64]$ObserverCompletion.stderr_bytes -ne 0 -or
        $ObserverCompletion.stderr_sha256 -isnot [string] -or
        $ObserverCompletion.stderr_sha256 -cne [string]$Task1.observer.stderr_sha256 -or
        $ObserverCompletion.engine_log_evidence_path -isnot [string] -or
        $ObserverCompletion.engine_log_evidence_path -cne [string]$Task1.observer.engine_log_evidence_path -or
        $ObserverCompletion.engine_log_evidence_sha256 -isnot [string] -or
        $ObserverCompletion.engine_log_evidence_sha256 -cne [string]$Task1.observer.engine_log_evidence_sha256 -or
        -not (Test-Task3IntegralValue $ObserverCompletion.source_save_bytes) -or
        -not (Test-Task3IntegralValue $ObserverCompletion.replay_save_bytes) -or
        [int64]$ObserverCompletion.source_save_bytes -ne [int64]$Task1.mother.bytes -or
        [int64]$ObserverCompletion.replay_save_bytes -ne [int64]$Task1.mother.bytes -or
        @(@(
            [string]$ObserverCompletion.source_save_sha256_before,
            [string]$ObserverCompletion.source_save_sha256_after,
            [string]$ObserverCompletion.replay_save_sha256_before,
            [string]$ObserverCompletion.replay_save_sha256_after
        ) | Where-Object { $_ -cne [string]$Task1.mother.sha256 }).Count -ne 0) {
        throw ('NEEDS_CONTEXT: observer/mother four-hash lineage failed ' + $Context + '; do not invoke Opus.')
    }
    return $Task1
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
        'task1_completion_sha256','approved_plan_commit','approved_spec_commit','rules_commit','rules_parent_commit',
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
        $Record.schema_version -isnot [int] -or [int]$Record.schema_version -ne 3 -or
        $Record.verdict -isnot [string] -or [string]$Record.verdict -cne 'PASS' -or
        $Record.approved_plan_lock_sha256 -isnot [string] -or [string]$Record.approved_plan_lock_sha256 -cne $ApprovalLockSha256 -or
        $Record.task1_completion_path -isnot [string] -or [string]$Record.task1_completion_path -cne (Resolve-Path -LiteralPath $Task1CompletionRecord).Path -or
        $Record.task1_completion_sha256 -isnot [string] -or [string]$Record.task1_completion_sha256 -cne $Task1CompletionSha256 -or
        $Record.approved_plan_commit -isnot [string] -or [string]$Record.approved_plan_commit -cne [string]$ApprovalRecord.approved_plan_commit -or
        $Record.approved_spec_commit -isnot [string] -or [string]$Record.approved_spec_commit -cne [string]$ApprovalRecord.spec_commit -or
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
            $ExpectedShowSource = [IO.Path]::GetFullPath((Join-Path $RecoveryRoot 'rules\scanner-show-before-source\show-before-scan.py'))
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
$null = Assert-Task3Task1Completion 'at Task 3 start'
Assert-Task3Task2Completion 'at Task 3 start'
```

Expected: before any project input or copy-run directory is read or created, Task 3 proves the exact 26-field schema-v3 lock and P2→S3→P3→R3 topology, freezes the Task 1/2 completion hashes for this session, re-hashes Task 1's exact 141 current files, and strictly reconstructs Task 2 schema-v3's nine receipts and exact 56-file current union. Legacy TIMEOUT and v2 log-contract-mismatch candidates remain `preserved_not_used`; neither is a copy source. The same three gates run again immediately before each of the three Opus invocations.

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
function Get-Task3FixedCanonicalPath([string]$Path, [string]$Context) {
    if ([string]::IsNullOrWhiteSpace($Path) -or -not [IO.Path]::IsPathRooted($Path)) {
        throw ('NEEDS_CONTEXT: path is not rooted ' + $Context + '; do not write or invoke Opus.')
    }
    $FullPath = [IO.Path]::GetFullPath($Path).TrimEnd(
        [IO.Path]::DirectorySeparatorChar, [IO.Path]::AltDirectorySeparatorChar)
    if ($FullPath -notmatch '^[A-Za-z]:\\') {
        throw ('NEEDS_CONTEXT: path is outside the canonical drive namespace ' + $Context + '; do not write or invoke Opus.')
    }
    return $FullPath
}
function Assert-Task3OrdinaryDirectoryChain([string]$Path, [string]$Context) {
    $FullPath = Get-Task3FixedCanonicalPath $Path $Context
    $RootPath = [IO.Path]::GetPathRoot($FullPath)
    if ([string]::IsNullOrWhiteSpace($RootPath) -or $RootPath -notmatch '^[A-Za-z]:\\$') {
        throw ('NEEDS_CONTEXT: invalid directory root ' + $Context + '; do not write or invoke Opus.')
    }
    $RootItem = Get-Item -LiteralPath $RootPath -Force -ErrorAction Stop
    if (-not $RootItem.PSIsContainer -or
        ($RootItem.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
        throw ('NEEDS_CONTEXT: volume root is not an ordinary directory ' + $Context + '; do not write or invoke Opus.')
    }
    $CurrentPath = $RootPath
    $Segments = $FullPath.Substring($RootPath.Length).Split(
        [char[]]@('\\','/'), [StringSplitOptions]::RemoveEmptyEntries)
    foreach ($Segment in $Segments) {
        $CurrentPath = [IO.Path]::Combine($CurrentPath, $Segment)
        $CurrentFull = Get-Task3FixedCanonicalPath $CurrentPath ($Context + ' component')
        $Item = Get-Item -LiteralPath $CurrentFull -Force -ErrorAction Stop
        if (-not $Item.PSIsContainer -or
            ($Item.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
            throw ('NEEDS_CONTEXT: directory component is missing, non-directory, or reparse-backed ' +
                $CurrentFull + ' ' + $Context + '; do not write or invoke Opus.')
        }
        $ResolvedFull = Get-Task3FixedCanonicalPath ((Resolve-Path -LiteralPath $CurrentFull -ErrorAction Stop).Path) ($Context + ' resolved component')
        if (-not $ResolvedFull.Equals($CurrentFull, [StringComparison]::OrdinalIgnoreCase)) {
            throw ('NEEDS_CONTEXT: directory component does not resolve to its fixed path ' +
                $CurrentFull + ' ' + $Context + '; do not write or invoke Opus.')
        }
    }
    return $FullPath
}
function Assert-Task3AbsentDirectNamespace([string]$ParentPath, [string]$LeafName, [string]$Context) {
    $ParentFull = Assert-Task3OrdinaryDirectoryChain $ParentPath ($Context + ' parent')
    if ([string]::IsNullOrWhiteSpace($LeafName) -or
        [IO.Path]::GetFileName($LeafName) -cne $LeafName -or
        $LeafName.IndexOfAny([IO.Path]::GetInvalidFileNameChars()) -ge 0 -or
        $LeafName.TrimEnd([char[]]@(' ','.')) -cne $LeafName) {
        throw ('NEEDS_CONTEXT: invalid fixed leaf name ' + $Context + '; do not write or invoke Opus.')
    }
    $Matches = @([IO.Directory]::GetFileSystemEntries($ParentFull) | Where-Object {
        $ObservedLeaf = [IO.Path]::GetFileName([string]$_)
        $ObservedLeaf.TrimEnd([char[]]@(' ','.')).Equals($LeafName, [StringComparison]::OrdinalIgnoreCase)
    })
    if ($Matches.Count -ne 0) {
        throw ('NEEDS_CONTEXT: fixed namespace already exists ' + $LeafName + ' ' +
            $Context + '; preserve it and do not retry.')
    }
}
function Assert-Task3OrdinaryDirectFile(
    [string]$Path,
    [string]$ExpectedParent,
    [string]$ExpectedName,
    [string]$Context
) {
    $ParentFull = Assert-Task3OrdinaryDirectoryChain $ExpectedParent ($Context + ' parent')
    $FullPath = Get-Task3FixedCanonicalPath $Path $Context
    if ($Path -cne $FullPath -or
        -not ([IO.Path]::GetDirectoryName($FullPath)).Equals($ParentFull, [StringComparison]::OrdinalIgnoreCase) -or
        [IO.Path]::GetFileName($FullPath) -cne $ExpectedName) {
        throw ('NEEDS_CONTEXT: file is not the exact canonical direct child ' + $Context + '; do not read it.')
    }
    $Item = Get-Item -LiteralPath $FullPath -Force -ErrorAction Stop
    if ($Item.PSIsContainer -or
        ($Item.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
        throw ('NEEDS_CONTEXT: file is a directory or reparse-backed ' + $Context + '; do not read it.')
    }
    $ResolvedFull = Get-Task3FixedCanonicalPath ((Resolve-Path -LiteralPath $FullPath -ErrorAction Stop).Path) ($Context + ' resolved file')
    if (-not $ResolvedFull.Equals($FullPath, [StringComparison]::OrdinalIgnoreCase)) {
        throw ('NEEDS_CONTEXT: file does not resolve to its fixed path ' + $Context + '; do not read it.')
    }
    return $Item
}
function Assert-Task3ExactDirectEntries(
    [string]$DirectoryPath,
    [string[]]$ExpectedPaths,
    [string]$Context
) {
    $DirectoryFull = Assert-Task3OrdinaryDirectoryChain $DirectoryPath $Context
    $ExpectedSet = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
    foreach ($ExpectedPath in @($ExpectedPaths)) {
        $ExpectedFull = Get-Task3FixedCanonicalPath $ExpectedPath ($Context + ' expected entry')
        if (-not ([IO.Path]::GetDirectoryName($ExpectedFull)).Equals($DirectoryFull, [StringComparison]::OrdinalIgnoreCase) -or
            -not $ExpectedSet.Add($ExpectedFull)) {
            throw ('NEEDS_CONTEXT: expected direct-entry set is noncanonical or non-unique ' + $Context + '.')
        }
    }
    $ObservedPaths = @([IO.Directory]::GetFileSystemEntries($DirectoryFull))
    if ($ObservedPaths.Count -ne $ExpectedSet.Count) {
        throw ('NEEDS_CONTEXT: direct-entry count differs ' + $Context + '; do not write, read candidate evidence, or invoke Opus.')
    }
    foreach ($ObservedPath in $ObservedPaths) {
        $ObservedFull = Get-Task3FixedCanonicalPath $ObservedPath ($Context + ' observed entry')
        if (-not $ExpectedSet.Contains($ObservedFull)) {
            throw ('NEEDS_CONTEXT: unexpected direct entry ' + $ObservedFull + ' ' + $Context + '.')
        }
        $ObservedItem = Get-Item -LiteralPath $ObservedFull -Force -ErrorAction Stop
        if (($ObservedItem.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
            throw ('NEEDS_CONTEXT: reparse-backed direct entry ' + $ObservedFull + ' ' + $Context + '.')
        }
    }
}

$RecoveryRootCanonical = Assert-Task3OrdinaryDirectoryChain $RecoveryRoot 'before creating the copy namespace'
$CopyRoot = Get-Task3FixedCanonicalPath ([IO.Path]::Combine($RecoveryRootCanonical, 'copy')) 'fixed copy root'
if (-not ([IO.Path]::GetDirectoryName($CopyRoot)).Equals($RecoveryRootCanonical, [StringComparison]::OrdinalIgnoreCase) -or
    [IO.Path]::GetFileName($CopyRoot) -cne 'copy') {
    throw 'NEEDS_CONTEXT: fixed copy-root layout drifted; do not write or invoke Opus.'
}
$RunNames = @('run-01', 'run-02', 'run-03')
$RunRoots = @(
    foreach ($RunName in $RunNames) {
        Get-Task3FixedCanonicalPath ([IO.Path]::Combine($CopyRoot, $RunName)) ('fixed ' + $RunName)
    }
)
for ($RunIndex = 0; $RunIndex -lt 3; $RunIndex++) {
    if (-not ([IO.Path]::GetDirectoryName($RunRoots[$RunIndex])).Equals($CopyRoot, [StringComparison]::OrdinalIgnoreCase) -or
        [IO.Path]::GetFileName($RunRoots[$RunIndex]) -cne $RunNames[$RunIndex]) {
        throw 'NEEDS_CONTEXT: fixed run-root layout drifted; do not write or invoke Opus.'
    }
}

$null = Assert-Task3ApprovalState 'immediately before creating the copy namespace'
$null = Assert-Task3Task1Completion 'immediately before creating the copy namespace'
Assert-Task3Task2Completion 'immediately before creating the copy namespace'
Assert-Task3AbsentDirectNamespace $RecoveryRootCanonical 'copy' 'before the first Task 3 write'
foreach ($IntendedIgnoredRoot in @($CopyRoot) + @($RunRoots)) {
    git check-ignore -q -- $IntendedIgnoredRoot
    if ($LASTEXITCODE -ne 0) {
        throw ('NEEDS_CONTEXT: fixed Task 3 root is not ignored; no write was made: ' + $IntendedIgnoredRoot)
    }
}
$null = Assert-Task3OrdinaryDirectoryChain $RecoveryRootCanonical 'immediately before creating the copy root'
Assert-Task3AbsentDirectNamespace $RecoveryRootCanonical 'copy' 'immediately before creating the copy root'
[IO.Directory]::CreateDirectory($CopyRoot) | Out-Null
$null = Assert-Task3OrdinaryDirectoryChain $CopyRoot 'new copy root'
if ([IO.Directory]::GetFileSystemEntries($CopyRoot).Count -ne 0) {
    throw 'NEEDS_CONTEXT: new copy root is not empty; preserve it and do not retry.'
}
for ($RunIndex = 0; $RunIndex -lt 3; $RunIndex++) {
    $null = Assert-Task3OrdinaryDirectoryChain $CopyRoot ('before creating ' + $RunNames[$RunIndex])
    $ExpectedExistingRunRoots = @()
    if ($RunIndex -gt 0) {
        $ExpectedExistingRunRoots = @($RunRoots[0..($RunIndex - 1)])
    }
    Assert-Task3ExactDirectEntries $CopyRoot $ExpectedExistingRunRoots ('copy namespace before creating ' + $RunNames[$RunIndex])
    Assert-Task3AbsentDirectNamespace $CopyRoot $RunNames[$RunIndex] ('before creating ' + $RunNames[$RunIndex])
    [IO.Directory]::CreateDirectory($RunRoots[$RunIndex]) | Out-Null
    $null = Assert-Task3OrdinaryDirectoryChain $RunRoots[$RunIndex] ('new ' + $RunNames[$RunIndex])
    if ([IO.Directory]::GetFileSystemEntries($RunRoots[$RunIndex]).Count -ne 0) {
        throw ('NEEDS_CONTEXT: new run root is not empty: ' + $RunRoots[$RunIndex])
    }
}
Assert-Task3ExactDirectEntries $CopyRoot $RunRoots 'fixed copy-root layout after creation'
foreach ($IgnoredRoot in @($CopyRoot) + @($RunRoots)) {
    git check-ignore -q -- $IgnoredRoot
    if ($LASTEXITCODE -ne 0) {
        throw ('NEEDS_CONTEXT: structurally validated Task 3 root is not ignored: ' + $IgnoredRoot)
    }
}
```

Expected: before the first write, the exact canonical `copy` namespace is absent and every existing parent component from the drive root through `recovery-v3` is an ordinary non-reparse directory. Task 3 then creates exactly one ordinary `copy` root with exactly the three fixed ordinary direct-child directories `run-01`, `run-02`, and `run-03`; no other leaf, directory, or reparse point is accepted. `git check-ignore` is checked only after canonical containment and ordinary-file-system identity have passed, so ignore status is never used as a containment proof. Any pre-existing or partially created namespace is preserved and is not retried.

- [ ] **Step 2: Create three byte-identical self-contained prompts with `apply_patch`**

```powershell
function Assert-Task3PromptWriteReady([int]$RunIndex) {
    if ($RunIndex -lt 0 -or $RunIndex -ge 3) {
        throw 'NEEDS_CONTEXT: prompt-write index must be 0, 1, or 2.'
    }
    $RunRoot = [string]$RunRoots[$RunIndex]
    $null = Assert-Task3ApprovalState ('immediately before prompt write for ' + $RunRoot)
    $null = Assert-Task3Task1Completion ('immediately before prompt write for ' + $RunRoot)
    Assert-Task3Task2Completion ('immediately before prompt write for ' + $RunRoot)
    Assert-Task3ExactDirectEntries $CopyRoot $RunRoots ('copy namespace before prompt write for ' + $RunRoot)
    $null = Assert-Task3OrdinaryDirectoryChain $RunRoot ('run root before prompt write for ' + $RunRoot)
    Assert-Task3ExactDirectEntries $RunRoot @() ('empty run root before prompt write for ' + $RunRoot)
    Assert-Task3AbsentDirectNamespace $RunRoot 'prompt.txt' ('immediately before prompt write for ' + $RunRoot)
    $PromptPath = Get-Task3FixedCanonicalPath ([IO.Path]::Combine($RunRoot, 'prompt.txt')) ('intended prompt for ' + $RunRoot)
    git check-ignore -q -- $PromptPath
    if ($LASTEXITCODE -ne 0) {
        throw ('NEEDS_CONTEXT: fixed prompt path is not ignored; no prompt was written: ' + $PromptPath)
    }
}
```

Run `Assert-Task3PromptWriteReady 0` immediately before the `run-01/prompt.txt` `apply_patch`; after that single write, run `Assert-Task3PromptWriteReady 1` immediately before the `run-02/prompt.txt` `apply_patch`; after that single write, run `Assert-Task3PromptWriteReady 2` immediately before the `run-03/prompt.txt` `apply_patch`. Do not batch the three pre-write checks ahead of their writes. Each check requires the selected run root to be the exact allowed existing empty parent and rejects every unexpected leaf, directory, or reparse point before `apply_patch` runs.

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
- 不加载或调用 `writing-game-copy`，不读取任何候选间共享的草稿、历史失败稿或未批准样本文库；三个 fresh 会话只能看到本 prompt。
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
Assert-Task3ExactDirectEntries $CopyRoot $RunRoots 'copy-root layout before prompt validation'
foreach ($RunRoot in $RunRoots) {
    $PromptPath = Get-Task3FixedCanonicalPath ([IO.Path]::Combine($RunRoot, 'prompt.txt')) ('prompt for ' + $RunRoot)
    $PromptItem = Assert-Task3OrdinaryDirectFile $PromptPath $RunRoot 'prompt.txt' ('prompt for ' + $RunRoot)
    Assert-Task3ExactDirectEntries $RunRoot @($PromptPath) ('prompt-only run root ' + $RunRoot)
    git check-ignore -q -- $PromptPath
    if ($LASTEXITCODE -ne 0) { throw ('Structurally validated prompt is not ignored: ' + $PromptPath) }
    $Bytes = [IO.File]::ReadAllBytes($PromptPath)
    if ($Bytes.Length -eq 0) { throw ('Empty prompt: ' + $PromptPath) }
    if ($Bytes.Length -ge 3 -and $Bytes[0] -eq 0xEF -and $Bytes[1] -eq 0xBB -and $Bytes[2] -eq 0xBF) {
        throw ('Prompt has UTF-8 BOM: ' + $PromptPath)
    }
    $Decoded = $StrictUtf8.GetString($Bytes)
    if ($Decoded.Contains([char]0xFFFD) -or $Decoded.Contains("`r") -or
        $Bytes[$Bytes.Length - 1] -ne 0x0A -or
        ($Bytes.Length -ge 2 -and $Bytes[$Bytes.Length - 2] -eq 0x0A)) {
        throw ('Prompt is not strict UTF-8 with exactly one final LF: ' + $PromptPath)
    }
    $PromptHashes += (Get-FileHash -LiteralPath $PromptPath -Algorithm SHA256).Hash
}
if (@($PromptHashes | Select-Object -Unique).Count -ne 1) {
    throw 'The three candidate prompts are not byte-identical.'
}
$PromptSha256 = [string]$PromptHashes[0]
```

- [ ] **Step 3: Invoke three fresh Opus sessions sequentially with no fallback**

```powershell
$Launcher = Get-Task3FixedCanonicalPath 'C:\Users\22325\.codex\skills\invoke-opus-4-6\scripts\invoke-opus.ps1' 'fixed Opus launcher'
$ValidationModule = Get-Task3FixedCanonicalPath 'C:\Users\22325\.codex\skills\invoke-opus-4-6\scripts\OpusValidation.psm1' 'fixed Opus validation module'
if ($Launcher -cne 'C:\Users\22325\.codex\skills\invoke-opus-4-6\scripts\invoke-opus.ps1' -or
    $ValidationModule -cne 'C:\Users\22325\.codex\skills\invoke-opus-4-6\scripts\OpusValidation.psm1' -or
    -not ([IO.Path]::GetDirectoryName($Launcher)).Equals([IO.Path]::GetDirectoryName($ValidationModule), [StringComparison]::OrdinalIgnoreCase) -or
    [IO.Path]::GetFileName($Launcher) -cne 'invoke-opus.ps1' -or
    [IO.Path]::GetFileName($ValidationModule) -cne 'OpusValidation.psm1') {
    throw 'NEEDS_CONTEXT: exact launcher/module layout drifted; do not invoke Opus.'
}
$LauncherBytes = [int64]19070
$LauncherSha256 = '002B294ACCB44D0B93ECBCA10AF7ABACC93D9A123AAB57621EDEA775B6D39874'
$ValidationModuleBytes = [int64]23849
$ValidationModuleSha256 = '0E1F62FAFDB750AD576A96F2231C93C026BCE3EA17E1D528EFEAFF12F2078DC0'

function Assert-ExactJsonProperties([object]$Value, [string[]]$Expected, [string]$Context) {
    if ($Value -isnot [pscustomobject]) { throw ($Context + ' must be one JSON object.') }
    $Actual = @($Value.PSObject.Properties.Name | Sort-Object)
    $SortedExpected = @($Expected | Sort-Object)
    if (Compare-Object $SortedExpected $Actual -CaseSensitive) {
        throw ($Context + ' has an inexact property set.')
    }
}
function Assert-NonemptyJsonString([object]$Value, [string]$Context) {
    if ($Value -isnot [string] -or [string]::IsNullOrWhiteSpace([string]$Value)) {
        throw ($Context + ' must be a nonempty JSON string.')
    }
}
function Assert-Task3ExternalToolSeal(
    [string]$Path,
    [int64]$ExpectedBytes,
    [string]$ExpectedSha256,
    [string]$Context
) {
    $ExpectedParent = Get-Task3FixedCanonicalPath ([IO.Path]::GetDirectoryName($Path)) ($Context + ' parent')
    $Item = Assert-Task3OrdinaryDirectFile $Path $ExpectedParent ([IO.Path]::GetFileName($Path)) $Context
    if ($ExpectedBytes -le 0 -or $ExpectedSha256 -cnotmatch '^[0-9A-F]{64}$' -or
        [int64]$Item.Length -ne $ExpectedBytes -or
        (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash -cne $ExpectedSha256) {
        throw ('NEEDS_CONTEXT: external Opus tool seal drifted ' + $Context + '; do not invoke Opus.')
    }
}
function ConvertFrom-Task3StrictLauncherSummary([string]$SummaryText, [string]$Context) {
    $ExpectedProperties = @(
        'success','exit_code','model','expected_model','observed_models',
        'result_model_usage_models','stream_path','stderr_path','result_path','metadata_path'
    )
    if ([string]::IsNullOrWhiteSpace($SummaryText) -or $SummaryText.Trim() -cne $SummaryText -or
        $SummaryText.Contains("`r") -or $SummaryText.Contains("`n") -or
        $SummaryText[0] -cne '{' -or $SummaryText[$SummaryText.Length - 1] -cne '}') {
        throw ('Launcher did not emit exactly one compact JSON object ' + $Context + '; do not read candidate evidence.')
    }
    $RawKeys = @(Get-Task3RawJsonObjectKeys $SummaryText ('launcher summary ' + $Context))
    if (($RawKeys -join '|') -cne ($ExpectedProperties -join '|')) {
        throw ('Launcher summary raw schema is inexact ' + $Context + '; do not read candidate evidence.')
    }
    try {
        $Summary = $SummaryText | ConvertFrom-Json -ErrorAction Stop
    } catch {
        throw ('Launcher summary is not one valid JSON object ' + $Context + '; do not read candidate evidence.')
    }
    Assert-Task3ExactProperties $Summary $ExpectedProperties ('launcher summary ' + $Context)
    if ($Summary.success -isnot [bool] -or -not $Summary.success -or
        $Summary.exit_code -isnot [int] -or [int]$Summary.exit_code -ne 0 -or
        $Summary.model -isnot [string] -or [string]$Summary.model -cne 'claude-opus-4-6' -or
        $Summary.expected_model -isnot [string] -or [string]$Summary.expected_model -cne 'claude-opus-4-6' -or
        $Summary.observed_models -isnot [object[]] -or @($Summary.observed_models).Count -ne 1 -or
        $Summary.observed_models[0] -isnot [string] -or [string]$Summary.observed_models[0] -cne 'claude-opus-4-6' -or
        $Summary.result_model_usage_models -isnot [object[]] -or @($Summary.result_model_usage_models).Count -ne 1 -or
        $Summary.result_model_usage_models[0] -isnot [string] -or
        [string]$Summary.result_model_usage_models[0] -cne 'claude-opus-4-6') {
        throw ('Launcher summary native type or provenance contract failed ' + $Context + '; do not read candidate evidence.')
    }
    foreach ($PathProperty in @('stream_path','stderr_path','result_path','metadata_path')) {
        if ($Summary.$PathProperty -isnot [string] -or
            [string]::IsNullOrWhiteSpace([string]$Summary.$PathProperty)) {
            throw ('Launcher summary path type failed for ' + $PathProperty + ' ' + $Context + '.')
        }
    }
    return $Summary
}
function Assert-Task3LauncherRunLayout(
    [string]$RunRoot,
    [string]$PromptPath,
    $Summary,
    [string]$Context
) {
    $BoundRunRoot = Get-Task3FixedCanonicalPath $RunRoot ($Context + ' run root')
    if ($RunRoot -cne $BoundRunRoot) {
        throw ('NEEDS_CONTEXT: run root is not its fixed canonical string ' + $Context + '.')
    }
    $MetadataFileName = [IO.Path]::GetFileName([string]$Summary.metadata_path)
    $PrefixMatch = [regex]::Match(
        $MetadataFileName,
        '^(opus-4-6-[0-9]{8}-[0-9]{6}-[0-9]{3}-[0-9a-f]{32})\.metadata\.json$',
        [Text.RegularExpressions.RegexOptions]::CultureInvariant)
    if (-not $PrefixMatch.Success) {
        throw ('Launcher metadata filename is not exact ' + $Context + '; do not read candidate evidence.')
    }
    $RunPrefix = $PrefixMatch.Groups[1].Value
    $ExpectedOutputPaths = [ordered]@{
        stream_path = Get-Task3FixedCanonicalPath ([IO.Path]::Combine($BoundRunRoot, $RunPrefix + '.stream.jsonl')) ($Context + ' expected stream')
        stderr_path = Get-Task3FixedCanonicalPath ([IO.Path]::Combine($BoundRunRoot, $RunPrefix + '.stderr.txt')) ($Context + ' expected stderr')
        result_path = Get-Task3FixedCanonicalPath ([IO.Path]::Combine($BoundRunRoot, $RunPrefix + '.result.txt')) ($Context + ' expected result')
        metadata_path = Get-Task3FixedCanonicalPath ([IO.Path]::Combine($BoundRunRoot, $RunPrefix + '.metadata.json')) ($Context + ' expected metadata')
    }
    $UniqueOutputPaths = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
    foreach ($PathProperty in @('stream_path','stderr_path','result_path','metadata_path')) {
        $ObservedPath = [string]$Summary.$PathProperty
        $ObservedFull = Get-Task3FixedCanonicalPath $ObservedPath ($Context + ' ' + $PathProperty)
        if ($ObservedPath -cne $ObservedFull -or
            $ObservedFull -cne [string]$ExpectedOutputPaths[$PathProperty] -or
            -not ([IO.Path]::GetDirectoryName($ObservedFull)).Equals($BoundRunRoot, [StringComparison]::OrdinalIgnoreCase) -or
            -not $UniqueOutputPaths.Add($ObservedFull)) {
            throw ('Launcher path is noncanonical, non-unique, outside the current run root, or misnamed: ' +
                $PathProperty + ' ' + $Context + '; do not read candidate evidence.')
        }
    }
    if (-not ([string]$Summary.metadata_path).Equals([string]$ExpectedOutputPaths.metadata_path, [StringComparison]::Ordinal) -or
        -not ([string]$Summary.result_path).Equals([string]$ExpectedOutputPaths.result_path, [StringComparison]::Ordinal) -or
        ([string]$Summary.metadata_path).Equals([string]$Summary.result_path, [StringComparison]::OrdinalIgnoreCase)) {
        throw ('Launcher metadata/result direct-child identity failed ' + $Context + '; do not read candidate evidence.')
    }
    $WorkRoot = Get-Task3FixedCanonicalPath ([IO.Path]::Combine($BoundRunRoot, $RunPrefix + '.work')) ($Context + ' expected work root')
    $ExpectedEntries = @(
        $PromptPath,
        [string]$ExpectedOutputPaths.stream_path,
        [string]$ExpectedOutputPaths.stderr_path,
        [string]$ExpectedOutputPaths.result_path,
        [string]$ExpectedOutputPaths.metadata_path,
        $WorkRoot
    )
    Assert-Task3ExactDirectEntries $BoundRunRoot $ExpectedEntries ($Context + ' exact post-launch namespace')
    $null = Assert-Task3OrdinaryDirectFile $PromptPath $BoundRunRoot 'prompt.txt' ($Context + ' prompt')
    foreach ($PathProperty in @('stream_path','stderr_path','result_path','metadata_path')) {
        $ExpectedPath = [string]$ExpectedOutputPaths[$PathProperty]
        $null = Assert-Task3OrdinaryDirectFile $ExpectedPath $BoundRunRoot ([IO.Path]::GetFileName($ExpectedPath)) ($Context + ' ' + $PathProperty)
    }
    $ObservedWorkRoot = Assert-Task3OrdinaryDirectoryChain $WorkRoot ($Context + ' launcher work root')
    if ($ObservedWorkRoot -cne $WorkRoot -or
        -not ([IO.Path]::GetDirectoryName($ObservedWorkRoot)).Equals($BoundRunRoot, [StringComparison]::OrdinalIgnoreCase) -or
        [IO.Path]::GetFileName($ObservedWorkRoot) -cne ($RunPrefix + '.work')) {
        throw ('Launcher work-root identity failed ' + $Context + '; do not read candidate evidence.')
    }
    return [pscustomobject][ordered]@{
        stream_path = [string]$ExpectedOutputPaths.stream_path
        stderr_path = [string]$ExpectedOutputPaths.stderr_path
        result_path = [string]$ExpectedOutputPaths.result_path
        metadata_path = [string]$ExpectedOutputPaths.metadata_path
        work_root = $WorkRoot
    }
}
function Read-Task3StrictOpusMetadata(
    [string]$MetadataPath,
    [string]$ExpectedWorkRoot,
    [string]$Context
) {
    $ExpectedProperties = @(
        'success','model','expected_model','observed_models','result_model_usage_models','session_name',
        'model_fallback_disabled','exit_code','working_directory','init_count','assistant_count',
        'message_start_count','result_count','successful_result_count','tool_use_count',
        'server_tool_request_count','init_tools_count','init_mcp_servers_count','stderr_bytes'
    )
    $MetadataBytes = [IO.File]::ReadAllBytes($MetadataPath)
    if ($MetadataBytes.Length -eq 0 -or
        ($MetadataBytes.Length -ge 3 -and $MetadataBytes[0] -eq 0xEF -and
         $MetadataBytes[1] -eq 0xBB -and $MetadataBytes[2] -eq 0xBF)) {
        throw ('Opus metadata is empty or has a BOM ' + $Context + '.')
    }
    $MetadataText = $StrictUtf8.GetString($MetadataBytes)
    if ($MetadataText.Contains([char]0xFFFD) -or $MetadataText.Contains("`r") -or $MetadataText.Contains("`n")) {
        throw ('Opus metadata is not one strict compact UTF-8 JSON object ' + $Context + '.')
    }
    $RawKeys = @(Get-Task3RawJsonObjectKeys $MetadataText ('Opus metadata ' + $Context))
    if (($RawKeys -join '|') -cne ($ExpectedProperties -join '|')) {
        throw ('Opus metadata raw schema is inexact ' + $Context + '.')
    }
    try {
        $Metadata = $MetadataText | ConvertFrom-Json -ErrorAction Stop
    } catch {
        throw ('Opus metadata is not valid JSON ' + $Context + '.')
    }
    Assert-Task3ExactProperties $Metadata $ExpectedProperties ('Opus metadata ' + $Context)
    $CountProperties = @(
        'exit_code','init_count','assistant_count','message_start_count','result_count',
        'successful_result_count','tool_use_count','server_tool_request_count',
        'init_tools_count','init_mcp_servers_count','stderr_bytes'
    )
    foreach ($CountProperty in $CountProperties) {
        if ($Metadata.$CountProperty -isnot [int]) {
            throw ('Opus metadata native integer type failed for ' + $CountProperty + ' ' + $Context + '.')
        }
    }
    if ($Metadata.success -isnot [bool] -or -not $Metadata.success -or
        $Metadata.model -isnot [string] -or [string]$Metadata.model -cne 'claude-opus-4-6' -or
        $Metadata.expected_model -isnot [string] -or [string]$Metadata.expected_model -cne 'claude-opus-4-6' -or
        $Metadata.observed_models -isnot [object[]] -or @($Metadata.observed_models).Count -ne 1 -or
        $Metadata.observed_models[0] -isnot [string] -or [string]$Metadata.observed_models[0] -cne 'claude-opus-4-6' -or
        $Metadata.result_model_usage_models -isnot [object[]] -or
        @($Metadata.result_model_usage_models).Count -ne 1 -or
        $Metadata.result_model_usage_models[0] -isnot [string] -or
        [string]$Metadata.result_model_usage_models[0] -cne 'claude-opus-4-6' -or
        $Metadata.session_name -isnot [string] -or [string]$Metadata.session_name -cne 'invoke-opus-4-6' -or
        $Metadata.model_fallback_disabled -isnot [bool] -or -not $Metadata.model_fallback_disabled -or
        [int]$Metadata.exit_code -ne 0 -or [int]$Metadata.init_count -ne 1 -or
        [int]$Metadata.assistant_count -lt 1 -or [int]$Metadata.message_start_count -lt 1 -or
        [int]$Metadata.result_count -ne 1 -or [int]$Metadata.successful_result_count -ne 1 -or
        [int]$Metadata.tool_use_count -ne 0 -or [int]$Metadata.server_tool_request_count -ne 0 -or
        [int]$Metadata.init_tools_count -ne 0 -or [int]$Metadata.init_mcp_servers_count -ne 0 -or
        [int]$Metadata.stderr_bytes -ne 0 -or
        $Metadata.working_directory -isnot [string]) {
        throw ('Opus metadata exact native type/value contract failed ' + $Context + '.')
    }
    $WorkingDirectoryFull = Get-Task3FixedCanonicalPath ([string]$Metadata.working_directory) ($Context + ' metadata working directory')
    if ([string]$Metadata.working_directory -cne $WorkingDirectoryFull -or
        $WorkingDirectoryFull -cne $ExpectedWorkRoot) {
        throw ('Opus metadata working-directory identity failed ' + $Context + '.')
    }
    return $Metadata
}
function Get-Task3ByteArraySha256([byte[]]$Bytes, [string]$Context) {
    if ($null -eq $Bytes) { throw ('NEEDS_CONTEXT: null byte array ' + $Context + '.') }
    $Hasher = [Security.Cryptography.SHA256]::Create()
    try {
        $Digest = $Hasher.ComputeHash($Bytes)
    } finally {
        $Hasher.Dispose()
    }
    return ([BitConverter]::ToString($Digest)).Replace('-', '')
}
function Read-Task3StrictCandidateResult(
    [string]$ResultPath,
    [string]$RunRoot,
    [AllowNull()][string]$ExpectedSha256,
    [string]$Context
) {
    $BoundRunRoot = Get-Task3FixedCanonicalPath $RunRoot ($Context + ' result run root')
    $ResultFull = Get-Task3FixedCanonicalPath $ResultPath ($Context + ' result path')
    $ResultName = [IO.Path]::GetFileName($ResultFull)
    if ($ResultPath -cne $ResultFull -or
        -not ([IO.Path]::GetDirectoryName($ResultFull)).Equals($BoundRunRoot, [StringComparison]::OrdinalIgnoreCase) -or
        $ResultName -cnotmatch '^opus-4-6-[0-9]{8}-[0-9]{6}-[0-9]{3}-[0-9a-f]{32}\.result\.txt$') {
        throw ('Candidate result path identity failed ' + $Context + '.')
    }
    $null = Assert-Task3OrdinaryDirectFile $ResultFull $BoundRunRoot $ResultName ($Context + ' result file')
    $ResultBytes = [IO.File]::ReadAllBytes($ResultFull)
    if ($ResultBytes.Length -eq 0 -or
        ($ResultBytes.Length -ge 3 -and $ResultBytes[0] -eq 0xEF -and
         $ResultBytes[1] -eq 0xBB -and $ResultBytes[2] -eq 0xBF)) {
        throw ('Empty or BOM-prefixed terminal result ' + $Context + '.')
    }
    $ResultBytesSha256 = Get-Task3ByteArraySha256 $ResultBytes ($Context + ' exact result bytes')
    if ($null -ne $ExpectedSha256 -and
        ($ExpectedSha256 -cnotmatch '^[0-9A-F]{64}$' -or $ResultBytesSha256 -cne $ExpectedSha256)) {
        throw ('Candidate result exact-byte hash failed ' + $Context + '.')
    }
    $ResultText = $StrictUtf8.GetString($ResultBytes)
    if ($ResultText.Contains([char]0xFFFD)) { throw ('Invalid UTF-8 terminal result ' + $Context + '.') }
    $null = @(Get-Task3RawJsonObjectKeys $ResultText ('terminal result ' + $Context))
    try {
        $Document = $ResultText | ConvertFrom-Json -ErrorAction Stop
    } catch {
        throw ('Terminal result is not the required JSON object ' + $Context + '.')
    }
    $ExpectedKeys = @(
        'baron_neutral_exchange','death_sequence','epilogue_bridge',
        'fall_cause_cards','fall_reflections','game_ending_summaries'
    )
    Assert-ExactJsonProperties $Document $ExpectedKeys ($Context + ' top level')
    if ($Document.baron_neutral_exchange -isnot [object[]] -or
        @($Document.baron_neutral_exchange).Count -ne 2) {
        throw ('Baron exchange native array/count drift ' + $Context + '.')
    }
    for ($EntryIndex = 0; $EntryIndex -lt 2; $EntryIndex++) {
        $Entry = $Document.baron_neutral_exchange[$EntryIndex]
        Assert-ExactJsonProperties $Entry @('speaker', 'text') ($Context + ' baron entry ' + $EntryIndex)
        Assert-NonemptyJsonString $Entry.speaker ($Context + ' baron speaker ' + $EntryIndex)
        Assert-NonemptyJsonString $Entry.text ($Context + ' baron text ' + $EntryIndex)
    }
    if ($Document.baron_neutral_exchange[0].speaker -cne 'captain' -or
        $Document.baron_neutral_exchange[1].speaker -cne 'player') {
        throw ('Baron exchange speaker order drift ' + $Context + '.')
    }
    foreach ($MapName in @('fall_reflections', 'fall_cause_cards', 'game_ending_summaries')) {
        $Map = $Document.$MapName
        Assert-ExactJsonProperties $Map @('inaction', 'battle', 'neutral') ($Context + ' ' + $MapName)
        foreach ($Cause in @('inaction', 'battle', 'neutral')) {
            Assert-NonemptyJsonString $Map.$Cause ($Context + ' ' + $MapName + '.' + $Cause)
        }
    }
    Assert-NonemptyJsonString $Document.epilogue_bridge ($Context + ' epilogue_bridge')
    if ($Document.death_sequence -isnot [object[]] -or
        @($Document.death_sequence).Count -lt 8 -or @($Document.death_sequence).Count -gt 14) {
        throw ('Death sequence native array/count drift ' + $Context + '.')
    }
    $DeathTexts = @()
    foreach ($Entry in @($Document.death_sequence)) {
        Assert-ExactJsonProperties $Entry @('speaker', 'text') ($Context + ' death entry')
        Assert-NonemptyJsonString $Entry.speaker ($Context + ' death speaker')
        Assert-NonemptyJsonString $Entry.text ($Context + ' death text')
        if (@('narrator', 'player', 'centered') -cnotcontains [string]$Entry.speaker) {
            throw ('Illegal death-sequence speaker ' + $Context + '.')
        }
        $DeathTexts += [string]$Entry.text
    }
    $DeathText = $DeathTexts -join ''
    if ($DeathText -notmatch '战死|死在|停止.{0,4}呼吸|没了呼吸|断了气|咽下.{0,4}气|心跳.{0,4}停') {
        throw ('Death sequence does not explicitly confirm death ' + $Context + '.')
    }
    if ([string]$Document.fall_reflections.battle -match '什么也没做' -or
        [string]$Document.fall_cause_cards.battle -match '什么也没做' -or
        [string]$Document.game_ending_summaries.battle -match '什么也没做') {
        throw ('Battle cause falsely claims inaction ' + $Context + '.')
    }
    if ($ResultText.Contains('TODO') -or $ResultText.Contains('占位') -or $ResultText.Contains('领主下落不明')) {
        throw ('Candidate contains forbidden placeholder or ambiguous-death text ' + $Context + '.')
    }
    return [pscustomobject][ordered]@{
        text = $ResultText
        sha256 = $ResultBytesSha256
    }
}

$VerifiedRuns = @()
foreach ($RunRoot in $RunRoots) {
    $null = Assert-Task3ApprovalState ('immediately before Opus invocation for ' + $RunRoot)
    $null = Assert-Task3Task1Completion ('immediately before Opus invocation for ' + $RunRoot)
    Assert-Task3Task2Completion ('immediately before Opus invocation for ' + $RunRoot)
    Assert-Task3ExactDirectEntries $CopyRoot $RunRoots ('copy-root layout before Opus invocation for ' + $RunRoot)
    $PromptPath = Get-Task3FixedCanonicalPath ([IO.Path]::Combine($RunRoot, 'prompt.txt')) ('prompt before Opus invocation for ' + $RunRoot)
    $null = Assert-Task3OrdinaryDirectFile $PromptPath $RunRoot 'prompt.txt' ('prompt before Opus invocation for ' + $RunRoot)
    Assert-Task3ExactDirectEntries $RunRoot @($PromptPath) ('fresh prompt-only namespace before Opus invocation for ' + $RunRoot)
    if ((Get-FileHash -LiteralPath $PromptPath -Algorithm SHA256).Hash -cne $PromptSha256) {
        throw ('Prompt drifted before Opus invocation: ' + $PromptPath)
    }
    git check-ignore -q -- $PromptPath
    if ($LASTEXITCODE -ne 0) { throw ('Structurally validated prompt is not ignored: ' + $PromptPath) }
    Assert-Task3ExternalToolSeal $Launcher $LauncherBytes $LauncherSha256 ('launcher immediately before ' + $RunRoot)
    Assert-Task3ExternalToolSeal $ValidationModule $ValidationModuleBytes $ValidationModuleSha256 ('validation module immediately before ' + $RunRoot)
    $SummaryRecords = @()
    $InvocationFailure = $null
    $LauncherPostSealFailure = $null
    $ModulePostSealFailure = $null
    try {
        $SummaryRecords = @(& $Launcher -PromptFile $PromptPath -OutputDirectory $RunRoot -ErrorAction Stop)
    } catch {
        $InvocationFailure = $_.Exception.Message
    }
    try {
        Assert-Task3ExternalToolSeal $Launcher $LauncherBytes $LauncherSha256 ('launcher immediately after ' + $RunRoot)
    } catch {
        $LauncherPostSealFailure = $_.Exception.Message
    }
    try {
        Assert-Task3ExternalToolSeal $ValidationModule $ValidationModuleBytes $ValidationModuleSha256 ('validation module immediately after ' + $RunRoot)
    } catch {
        $ModulePostSealFailure = $_.Exception.Message
    }
    $InvocationFailures = @()
    if ($null -ne $InvocationFailure) {
        $InvocationFailures += ('invocation=' + [string]$InvocationFailure)
    }
    if ($null -ne $LauncherPostSealFailure) {
        $InvocationFailures += ('launcher_post_seal=' + [string]$LauncherPostSealFailure)
    }
    if ($null -ne $ModulePostSealFailure) {
        $InvocationFailures += ('module_post_seal=' + [string]$ModulePostSealFailure)
    }
    if ($InvocationFailures.Count -ne 0) {
        throw ('Opus invocation/post-seal gate failed for ' + $RunRoot + '. Do not retry or read summary/candidate artifacts. ' +
            ($InvocationFailures -join ' | '))
    }
    if ($SummaryRecords.Count -ne 1 -or $SummaryRecords[0] -isnot [string]) {
        throw ('Opus launcher returned other than one string summary: ' + $RunRoot)
    }
    $SummaryText = [string]$SummaryRecords[0]
    $Summary = ConvertFrom-Task3StrictLauncherSummary $SummaryText $RunRoot
    $RunPaths = Assert-Task3LauncherRunLayout $RunRoot $PromptPath $Summary $RunRoot
    foreach ($EvidencePath in @(
        $PromptPath,$RunPaths.stream_path,$RunPaths.stderr_path,$RunPaths.result_path,
        $RunPaths.metadata_path,$RunPaths.work_root
    )) {
        git check-ignore -q -- $EvidencePath
        if ($LASTEXITCODE -ne 0) {
            throw ('Structurally validated candidate artifact is not ignored: ' + $EvidencePath)
        }
    }

    $Metadata = Read-Task3StrictOpusMetadata $RunPaths.metadata_path $RunPaths.work_root $RunRoot
    $StreamItem = Get-Item -LiteralPath $RunPaths.stream_path -Force -ErrorAction Stop
    $StderrItem = Get-Item -LiteralPath $RunPaths.stderr_path -Force -ErrorAction Stop
    if ([int64]$StreamItem.Length -le 0 -or
        [int64]$StderrItem.Length -ne [int64]$Metadata.stderr_bytes) {
        throw ('Launcher stream/stderr physical evidence contract failed: ' + $RunRoot)
    }

    $null = Read-Task3StrictCandidateResult $RunPaths.result_path $RunRoot $null ('Step 3 initial validation ' + $RunRoot)

    $VerifiedRuns += [pscustomobject][ordered]@{
        run_root = $RunRoot
        prompt_path = $PromptPath
        prompt_sha256 = $PromptSha256
        stream_path = [string]$RunPaths.stream_path
        stream_sha256 = (Get-FileHash -LiteralPath $RunPaths.stream_path -Algorithm SHA256).Hash
        stderr_path = [string]$RunPaths.stderr_path
        stderr_sha256 = (Get-FileHash -LiteralPath $RunPaths.stderr_path -Algorithm SHA256).Hash
        metadata_path = [string]$RunPaths.metadata_path
        metadata_sha256 = (Get-FileHash -LiteralPath $RunPaths.metadata_path -Algorithm SHA256).Hash
        result_path = [string]$RunPaths.result_path
        result_sha256 = (Get-FileHash -LiteralPath $RunPaths.result_path -Algorithm SHA256).Hash
        work_root = [string]$RunPaths.work_root
    }
}
if ($VerifiedRuns.Count -ne 3) { throw 'Exactly three verified runs are required.' }
if (@($VerifiedRuns.result_sha256 | Select-Object -Unique).Count -lt 2) {
    throw 'Candidate generation produced no meaningful independent variation; stop for review rather than retrying.'
}
```

Run sequentially. If any invocation or provenance check fails, stop immediately, preserve every artifact path, report the failure, and wait for explicit user authorization. Do not retry the failed run in this task. For each call, both fixed external tool files are revalidated immediately before invocation. The invocation exception is captured instead of thrown immediately, then launcher and module post-seals are attempted independently in separate `try` blocks even when invocation failed; failure of either post-seal never suppresses the other attempt. Invocation and both post-seal failures are aggregated, and any failure stops without retry before a summary or candidate artifact is read. Only after that aggregate gate passes may the single stdout summary undergo its exact ordered schema/native-type contract and the returned paths plus exact six-entry run-root namespace undergo canonical direct-child, expected-filename, uniqueness, ordinary/non-reparse, and no-extra-entry checks. Step 3 discards the strict result reader's returned text object after validation and never stores `result_text` in `$VerifiedRuns`; user-facing text is reconstructed only during the final blind handoff.

Before randomization, read each verified JSON result in full and perform a fact-only acceptance check. Do not rank prose quality or edit any candidate. Each candidate must satisfy all of the following:

- it introduces no new named person, army, artifact, place, world rule, art, music, sound effect, or animation;
- it does not decide the fate of Ren, Aldric, Elena, Ingrid, or Selene;
- its neutral cause does not accuse the player of voluntary inaction;
- its battle cause describes failure after the player forces a hopeless battle, never simple passivity;
- its baron exchange says only that the baron remains neutral and supplies no troops, rendezvous, or invented headcount;
- its death sequence unambiguously kills the player character in the burning hall and transitions to the existing third-person aftermath.

```powershell
function Assert-Task3FactReviewWriteReady($Run) {
    if ($Run -isnot [pscustomobject] -or
        (@($VerifiedRuns | Where-Object { [object]::ReferenceEquals($_, $Run) })).Count -ne 1) {
        throw 'NEEDS_CONTEXT: fact-review write must bind exactly one verified run.'
    }
    $RunRoot = [string]$Run.run_root
    $null = Assert-Task3ApprovalState ('immediately before fact-review write for ' + $RunRoot)
    $null = Assert-Task3Task1Completion ('immediately before fact-review write for ' + $RunRoot)
    Assert-Task3Task2Completion ('immediately before fact-review write for ' + $RunRoot)
    Assert-Task3ExactDirectEntries $CopyRoot $RunRoots ('copy namespace before fact-review write for ' + $RunRoot)
    $ExpectedPreReviewEntries = @(
        [string]$Run.prompt_path,[string]$Run.stream_path,[string]$Run.stderr_path,
        [string]$Run.result_path,[string]$Run.metadata_path,[string]$Run.work_root
    )
    Assert-Task3ExactDirectEntries $RunRoot $ExpectedPreReviewEntries ('pre-review run namespace for ' + $RunRoot)
    $CurrentWorkRoot = Assert-Task3OrdinaryDirectoryChain ([string]$Run.work_root) ('pre-review work root for ' + $RunRoot)
    if ($CurrentWorkRoot -cne [string]$Run.work_root -or
        -not ([IO.Path]::GetDirectoryName($CurrentWorkRoot)).Equals($RunRoot, [StringComparison]::OrdinalIgnoreCase)) {
        throw ('NEEDS_CONTEXT: pre-review work-root identity drifted for ' + $RunRoot)
    }
    $PreReviewSeals = @(
        [pscustomobject][ordered]@{ path=[string]$Run.prompt_path; sha256=[string]$Run.prompt_sha256 },
        [pscustomobject][ordered]@{ path=[string]$Run.stream_path; sha256=[string]$Run.stream_sha256 },
        [pscustomobject][ordered]@{ path=[string]$Run.stderr_path; sha256=[string]$Run.stderr_sha256 },
        [pscustomobject][ordered]@{ path=[string]$Run.result_path; sha256=[string]$Run.result_sha256 },
        [pscustomobject][ordered]@{ path=[string]$Run.metadata_path; sha256=[string]$Run.metadata_sha256 }
    )
    foreach ($PreReviewSeal in $PreReviewSeals) {
        $null = Assert-Task3OrdinaryDirectFile ([string]$PreReviewSeal.path) $RunRoot ([IO.Path]::GetFileName([string]$PreReviewSeal.path)) ('pre-review evidence ' + [string]$PreReviewSeal.path)
        if ([string]$PreReviewSeal.sha256 -cnotmatch '^[0-9A-F]{64}$' -or
            (Get-FileHash -LiteralPath ([string]$PreReviewSeal.path) -Algorithm SHA256).Hash -cne [string]$PreReviewSeal.sha256) {
            throw ('NEEDS_CONTEXT: candidate evidence drifted before fact-review write: ' + [string]$PreReviewSeal.path)
        }
    }
    Assert-Task3AbsentDirectNamespace $RunRoot 'fact-review.txt' ('immediately before fact-review write for ' + $RunRoot)
    $FactPath = Get-Task3FixedCanonicalPath ([IO.Path]::Combine($RunRoot, 'fact-review.txt')) ('intended fact review for ' + $RunRoot)
    git check-ignore -q -- $FactPath
    if ($LASTEXITCODE -ne 0) {
        throw ('NEEDS_CONTEXT: fixed fact-review path is not ignored; no review was written: ' + $FactPath)
    }
}
```

For each verified run in order, call `Assert-Task3FactReviewWriteReady $VerifiedRuns[0]` immediately before only that run's `fact-review.txt` `apply_patch`, then repeat with indexes `1` and `2`. Do not preflight all three writes in advance. The same gate applies when the fact-only verdict is a rejection: write the literal rejection once, preserve all three run roots, and stop without retry.

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
    $FactPath = Get-Task3FixedCanonicalPath ([IO.Path]::Combine([string]$Run.run_root, 'fact-review.txt')) ('fact review for ' + [string]$Run.run_root)
    $null = Assert-Task3OrdinaryDirectFile $FactPath ([string]$Run.run_root) 'fact-review.txt' ('fact review for ' + [string]$Run.run_root)
    $ExpectedRunEntries = @(
        [string]$Run.prompt_path,[string]$Run.stream_path,[string]$Run.stderr_path,
        [string]$Run.result_path,[string]$Run.metadata_path,[string]$Run.work_root,$FactPath
    )
    Assert-Task3ExactDirectEntries ([string]$Run.run_root) $ExpectedRunEntries ('fact-review namespace for ' + [string]$Run.run_root)
    $FactBytes = [IO.File]::ReadAllBytes($FactPath)
    if ($FactBytes.Length -eq 0 -or
        ($FactBytes.Length -ge 3 -and $FactBytes[0] -eq 0xEF -and
         $FactBytes[1] -eq 0xBB -and $FactBytes[2] -eq 0xBF)) {
        throw ('Fact review is empty or has a BOM: ' + $FactPath)
    }
    $FactText = $StrictUtf8.GetString($FactBytes)
    if ($FactText.Contains([char]0xFFFD) -or $FactText.Contains("`r") -or
        $FactBytes[$FactBytes.Length - 1] -ne 0x0A -or
        ($FactBytes.Length -ge 2 -and $FactBytes[$FactBytes.Length - 2] -eq 0x0A)) {
        throw ('Fact review is not strict UTF-8 with exactly one final LF: ' + $FactPath)
    }
    $FactLines = @($FactText.Substring(0, $FactText.Length - 1).Split("`n"))
    if ($FactLines.Count -ne 8 -or $FactLines[0] -cne 'verdict=PASS') {
        throw ('Fact review shape or verdict failed: ' + $FactPath)
    }
    if ($FactLines[1] -cne ('result_sha256=' + [string]$Run.result_sha256)) {
        throw ('Fact review result hash mismatch: ' + $FactPath)
    }
    for ($Index = 0; $Index -lt $FactKeys.Count; $Index++) {
        if ($FactLines[$Index + 2] -cne ($FactKeys[$Index] + '=PASS')) {
            throw ('Fact review criterion failed: ' + $FactPath)
        }
    }
    git check-ignore -q -- $FactPath
    if ($LASTEXITCODE -ne 0) { throw ('Structurally validated fact review is not ignored: ' + $FactPath) }
    $Run | Add-Member -NotePropertyName fact_review_path -NotePropertyValue $FactPath
$Run | Add-Member -NotePropertyName fact_review_sha256 -NotePropertyValue ((Get-FileHash -LiteralPath $FactPath -Algorithm SHA256).Hash)
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
        label = [string]$BlindLabels[$Index]
        run_root = [string]$Run.run_root
        prompt_path = [string]$Run.prompt_path
        prompt_sha256 = [string]$Run.prompt_sha256
        stream_path = [string]$Run.stream_path
        stream_sha256 = [string]$Run.stream_sha256
        stderr_path = [string]$Run.stderr_path
        stderr_sha256 = [string]$Run.stderr_sha256
        metadata_path = [string]$Run.metadata_path
        metadata_sha256 = [string]$Run.metadata_sha256
        result_path = [string]$Run.result_path
        result_sha256 = [string]$Run.result_sha256
        work_root = [string]$Run.work_root
        fact_review_path = [string]$Run.fact_review_path
        fact_review_sha256 = [string]$Run.fact_review_sha256
    }
}$BlindRows | Format-Table -AutoSize
```

```powershell
function Test-Task3ByteArrayEqual([byte[]]$Left, [byte[]]$Right) {
    if ($null -eq $Left -or $null -eq $Right -or $Left.Length -ne $Right.Length) {
        return $false
    }
    for ($ByteIndex = 0; $ByteIndex -lt $Left.Length; $ByteIndex++) {
        if ($Left[$ByteIndex] -ne $Right[$ByteIndex]) { return $false }
    }
    return $true
}
function Read-Task3StrictBlindMap(
    [string]$Path,
    [string]$ExpectedSha256,
    [AllowNull()][byte[]]$ExpectedBytes,
    [string]$Context
) {
    $TopProperties = @('schema_version','purpose','rules_commit','candidate_count','candidates')
    $RowProperties = @(
        'label','run_root','prompt_path','prompt_sha256','stream_path','stream_sha256',
        'stderr_path','stderr_sha256','metadata_path','metadata_sha256','result_path','result_sha256',
        'work_root','fact_review_path','fact_review_sha256'
    )
    $ExpectedPath = Get-Task3FixedCanonicalPath ([IO.Path]::Combine($CopyRoot, 'blind-map.md')) ($Context + ' expected blind map')
    if ($Path -cne $ExpectedPath -or $ExpectedSha256 -cnotmatch '^[0-9A-F]{64}$') {
        throw ('NEEDS_CONTEXT: blind-map path/hash binding failed ' + $Context + '.')
    }
    $Item = Assert-Task3OrdinaryDirectFile $Path $CopyRoot 'blind-map.md' ($Context + ' blind map')
    if (-not $Item.IsReadOnly) {
        throw ('NEEDS_CONTEXT: blind-map read-only seal failed ' + $Context + '.')
    }
    Assert-Task3ExactDirectEntries $CopyRoot (@($RunRoots) + @($Path)) ($Context + ' copy namespace')
    $Bytes = [IO.File]::ReadAllBytes($Path)
    $ReadBytesSha256 = Get-Task3ByteArraySha256 $Bytes ($Context + ' blind-map exact bytes')
    if ($Bytes.Length -eq 0 -or
        ($Bytes.Length -ge 3 -and $Bytes[0] -eq 0xEF -and $Bytes[1] -eq 0xBB -and $Bytes[2] -eq 0xBF) -or
        $Bytes[$Bytes.Length - 1] -ne 0x0A -or
        ($Bytes.Length -ge 2 -and $Bytes[$Bytes.Length - 2] -eq 0x0A) -or
        $ReadBytesSha256 -cne $ExpectedSha256 -or
        (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash -cne $ExpectedSha256 -or
        ($null -ne $ExpectedBytes -and -not (Test-Task3ByteArrayEqual $Bytes $ExpectedBytes))) {
        throw ('NEEDS_CONTEXT: blind-map exact bytes failed ' + $Context + '.')
    }
    $Text = $StrictUtf8.GetString($Bytes)
    if ($Text.Contains([char]0xFFFD) -or $Text.Contains("`r")) {
        throw ('NEEDS_CONTEXT: blind-map encoding failed ' + $Context + '.')
    }
    $JsonText = $Text.Substring(0, $Text.Length - 1)
    $ExpectedRawKeys = @($TopProperties)
    for ($RawRowIndex = 0; $RawRowIndex -lt 3; $RawRowIndex++) {
        $ExpectedRawKeys += $RowProperties
    }
    $RawKeys = @(Get-Task3RawJsonObjectKeys $JsonText ('blind map ' + $Context))
    if (($RawKeys -join '|') -cne ($ExpectedRawKeys -join '|')) {
        throw ('NEEDS_CONTEXT: blind-map raw ordered schema failed ' + $Context + '.')
    }
    try {
        $Record = $JsonText | ConvertFrom-Json -ErrorAction Stop
    } catch {
        throw ('NEEDS_CONTEXT: blind map is not one valid JSON object ' + $Context + '.')
    }
    Assert-Task3ExactProperties $Record $TopProperties ('blind map ' + $Context)
    if ($Record.schema_version -isnot [int] -or [int]$Record.schema_version -ne 1 -or
        $Record.purpose -isnot [string] -or [string]$Record.purpose -cne 'terminal-collapse-copy-blind-map' -or
        $Record.rules_commit -isnot [string] -or [string]$Record.rules_commit -cne $ExpectedRulesCommit -or
        $Record.candidate_count -isnot [int] -or [int]$Record.candidate_count -ne 3 -or
        $Record.candidates -isnot [object[]] -or @($Record.candidates).Count -ne 3) {
        throw ('NEEDS_CONTEXT: blind-map top-level native type/value contract failed ' + $Context + '.')
    }
    $ExpectedLabels = @('A','B','C')
    $ObservedRunRoots = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
    for ($RowIndex = 0; $RowIndex -lt 3; $RowIndex++) {
        $Row = $Record.candidates[$RowIndex]
        Assert-Task3ExactProperties $Row $RowProperties ('blind-map row ' + $RowIndex + ' ' + $Context)
        foreach ($StringProperty in $RowProperties) {
            if ($Row.$StringProperty -isnot [string] -or
                [string]::IsNullOrWhiteSpace([string]$Row.$StringProperty)) {
                throw ('NEEDS_CONTEXT: blind-map row string type failed for ' + $StringProperty + ' ' + $Context + '.')
            }
        }
        if ([string]$Row.label -cne $ExpectedLabels[$RowIndex]) {
            throw ('NEEDS_CONTEXT: blind-map label order failed ' + $Context + '.')
        }
        foreach ($HashProperty in @(
            'prompt_sha256','stream_sha256','stderr_sha256','metadata_sha256',
            'result_sha256','fact_review_sha256'
        )) {
            if ([string]$Row.$HashProperty -cnotmatch '^[0-9A-F]{64}$') {
                throw ('NEEDS_CONTEXT: blind-map hash shape failed for ' + $HashProperty + ' ' + $Context + '.')
            }
        }
        $RunRoot = Get-Task3FixedCanonicalPath ([string]$Row.run_root) ('blind-map run root ' + $Context)
        if ([string]$Row.run_root -cne $RunRoot -or
            @($RunRoots | Where-Object { $_.Equals($RunRoot, [StringComparison]::OrdinalIgnoreCase) }).Count -ne 1 -or
            -not $ObservedRunRoots.Add($RunRoot)) {
            throw ('NEEDS_CONTEXT: blind-map run-root permutation failed ' + $Context + '.')
        }
        $MetadataName = [IO.Path]::GetFileName([string]$Row.metadata_path)
        $PrefixMatch = [regex]::Match(
            $MetadataName,
            '^(opus-4-6-[0-9]{8}-[0-9]{6}-[0-9]{3}-[0-9a-f]{32})\.metadata\.json$',
            [Text.RegularExpressions.RegexOptions]::CultureInvariant)
        if (-not $PrefixMatch.Success) {
            throw ('NEEDS_CONTEXT: blind-map metadata filename failed ' + $Context + '.')
        }
        $Prefix = $PrefixMatch.Groups[1].Value
        $ExpectedPaths = [ordered]@{
            prompt_path = Get-Task3FixedCanonicalPath ([IO.Path]::Combine($RunRoot, 'prompt.txt')) ('blind-map expected prompt ' + $Context)
            stream_path = Get-Task3FixedCanonicalPath ([IO.Path]::Combine($RunRoot, $Prefix + '.stream.jsonl')) ('blind-map expected stream ' + $Context)
            stderr_path = Get-Task3FixedCanonicalPath ([IO.Path]::Combine($RunRoot, $Prefix + '.stderr.txt')) ('blind-map expected stderr ' + $Context)
            metadata_path = Get-Task3FixedCanonicalPath ([IO.Path]::Combine($RunRoot, $Prefix + '.metadata.json')) ('blind-map expected metadata ' + $Context)
            result_path = Get-Task3FixedCanonicalPath ([IO.Path]::Combine($RunRoot, $Prefix + '.result.txt')) ('blind-map expected result ' + $Context)
            work_root = Get-Task3FixedCanonicalPath ([IO.Path]::Combine($RunRoot, $Prefix + '.work')) ('blind-map expected work root ' + $Context)
            fact_review_path = Get-Task3FixedCanonicalPath ([IO.Path]::Combine($RunRoot, 'fact-review.txt')) ('blind-map expected fact review ' + $Context)
        }
        foreach ($PathProperty in $ExpectedPaths.Keys) {
            if ([string]$Row.$PathProperty -cne [string]$ExpectedPaths[$PathProperty]) {
                throw ('NEEDS_CONTEXT: blind-map canonical direct-child path failed for ' + $PathProperty + ' ' + $Context + '.')
            }
        }
        $ExpectedRunEntries = @(
            [string]$Row.prompt_path,[string]$Row.stream_path,[string]$Row.stderr_path,
            [string]$Row.result_path,[string]$Row.metadata_path,[string]$Row.work_root,
            [string]$Row.fact_review_path
        )
        Assert-Task3ExactDirectEntries $RunRoot $ExpectedRunEntries ('blind-map run namespace ' + $Context)
        $CurrentWorkRoot = Assert-Task3OrdinaryDirectoryChain ([string]$Row.work_root) ('blind-map work root ' + $Context)
        if ($CurrentWorkRoot -cne [string]$Row.work_root -or
            -not ([IO.Path]::GetDirectoryName($CurrentWorkRoot)).Equals($RunRoot, [StringComparison]::OrdinalIgnoreCase)) {
            throw ('NEEDS_CONTEXT: blind-map work-root identity failed ' + $Context + '.')
        }
        $FileSeals = @(
            [pscustomobject][ordered]@{ path=[string]$Row.prompt_path; sha256=[string]$Row.prompt_sha256 },
            [pscustomobject][ordered]@{ path=[string]$Row.stream_path; sha256=[string]$Row.stream_sha256 },
            [pscustomobject][ordered]@{ path=[string]$Row.stderr_path; sha256=[string]$Row.stderr_sha256 },
            [pscustomobject][ordered]@{ path=[string]$Row.metadata_path; sha256=[string]$Row.metadata_sha256 },
            [pscustomobject][ordered]@{ path=[string]$Row.result_path; sha256=[string]$Row.result_sha256 },
            [pscustomobject][ordered]@{ path=[string]$Row.fact_review_path; sha256=[string]$Row.fact_review_sha256 }
        )
        foreach ($FileSeal in $FileSeals) {
            $null = Assert-Task3OrdinaryDirectFile ([string]$FileSeal.path) $RunRoot ([IO.Path]::GetFileName([string]$FileSeal.path)) ('blind-map sealed file ' + $Context)
            if ((Get-FileHash -LiteralPath ([string]$FileSeal.path) -Algorithm SHA256).Hash -cne [string]$FileSeal.sha256) {
                throw ('NEEDS_CONTEXT: blind-map current file seal failed for ' + [string]$FileSeal.path + ' ' + $Context + '.')
            }
            git check-ignore -q -- ([string]$FileSeal.path)
            if ($LASTEXITCODE -ne 0) {
                throw ('NEEDS_CONTEXT: structurally validated blind-map artifact is not ignored: ' + [string]$FileSeal.path)
            }
        }
        git check-ignore -q -- ([string]$Row.work_root)
        if ($LASTEXITCODE -ne 0) {
            throw ('NEEDS_CONTEXT: structurally validated blind-map work root is not ignored: ' + [string]$Row.work_root)
        }
    }
    if ($ObservedRunRoots.Count -ne 3) {
        throw ('NEEDS_CONTEXT: blind map is not an exact three-run permutation ' + $Context + '.')
    }
    foreach ($ExpectedRunRoot in $RunRoots) {
        if (-not $ObservedRunRoots.Contains([string]$ExpectedRunRoot)) {
            throw ('NEEDS_CONTEXT: blind map omits a fixed run root ' + $Context + '.')
        }
    }
    git check-ignore -q -- $Path
    if ($LASTEXITCODE -ne 0) {
        throw ('NEEDS_CONTEXT: structurally validated blind map is not ignored ' + $Context + '.')
    }
    return $Record
}

$null = Assert-Task3ApprovalState 'immediately before blind-map write'
$null = Assert-Task3Task1Completion 'immediately before blind-map write'
Assert-Task3Task2Completion 'immediately before blind-map write'
Assert-Task3ExactDirectEntries $CopyRoot $RunRoots 'copy namespace immediately before blind-map write'
foreach ($Run in $VerifiedRuns) {
    $ExpectedReviewedEntries = @(
        [string]$Run.prompt_path,[string]$Run.stream_path,[string]$Run.stderr_path,
        [string]$Run.result_path,[string]$Run.metadata_path,[string]$Run.work_root,
        [string]$Run.fact_review_path
    )
    Assert-Task3ExactDirectEntries ([string]$Run.run_root) $ExpectedReviewedEntries ('reviewed run before blind-map write ' + [string]$Run.run_root)
    $CurrentWorkRoot = Assert-Task3OrdinaryDirectoryChain ([string]$Run.work_root) ('work root before blind-map write ' + [string]$Run.run_root)
    if ($CurrentWorkRoot -cne [string]$Run.work_root -or
        -not ([IO.Path]::GetDirectoryName($CurrentWorkRoot)).Equals([string]$Run.run_root, [StringComparison]::OrdinalIgnoreCase)) {
        throw ('NEEDS_CONTEXT: work-root identity drifted before blind-map write: ' + [string]$Run.work_root)
    }
    $ReviewedSeals = @(
        [pscustomobject][ordered]@{ path=[string]$Run.prompt_path; sha256=[string]$Run.prompt_sha256 },
        [pscustomobject][ordered]@{ path=[string]$Run.stream_path; sha256=[string]$Run.stream_sha256 },
        [pscustomobject][ordered]@{ path=[string]$Run.stderr_path; sha256=[string]$Run.stderr_sha256 },
        [pscustomobject][ordered]@{ path=[string]$Run.result_path; sha256=[string]$Run.result_sha256 },
        [pscustomobject][ordered]@{ path=[string]$Run.metadata_path; sha256=[string]$Run.metadata_sha256 },
        [pscustomobject][ordered]@{ path=[string]$Run.fact_review_path; sha256=[string]$Run.fact_review_sha256 }
    )
    foreach ($ReviewedSeal in $ReviewedSeals) {
        $null = Assert-Task3OrdinaryDirectFile ([string]$ReviewedSeal.path) ([string]$Run.run_root) ([IO.Path]::GetFileName([string]$ReviewedSeal.path)) ('pre-blind-map evidence ' + [string]$ReviewedSeal.path)
        if ([string]$ReviewedSeal.sha256 -cnotmatch '^[0-9A-F]{64}$' -or
            (Get-FileHash -LiteralPath ([string]$ReviewedSeal.path) -Algorithm SHA256).Hash -cne [string]$ReviewedSeal.sha256) {
            throw ('NEEDS_CONTEXT: evidence drifted before blind-map write: ' + [string]$ReviewedSeal.path)
        }
    }
}
$BlindMapPath = Get-Task3FixedCanonicalPath ([IO.Path]::Combine($CopyRoot, 'blind-map.md')) 'intended Task 3 blind map'
Assert-Task3AbsentDirectNamespace $CopyRoot 'blind-map.md' 'immediately before blind-map write'
git check-ignore -q -- $BlindMapPath
if ($LASTEXITCODE -ne 0) {
    throw 'NEEDS_CONTEXT: fixed blind-map path is not ignored; no blind map was written.'
}
$BlindMapRecord = [ordered]@{
    schema_version = [int]1
    purpose = 'terminal-collapse-copy-blind-map'
    rules_commit = [string]$ExpectedRulesCommit
    candidate_count = [int]3
    candidates = @(
        foreach ($BlindRow in $BlindRows) {
            [ordered]@{
                label = [string]$BlindRow.label
                run_root = [string]$BlindRow.run_root
                prompt_path = [string]$BlindRow.prompt_path
                prompt_sha256 = [string]$BlindRow.prompt_sha256
                stream_path = [string]$BlindRow.stream_path
                stream_sha256 = [string]$BlindRow.stream_sha256
                stderr_path = [string]$BlindRow.stderr_path
                stderr_sha256 = [string]$BlindRow.stderr_sha256
                metadata_path = [string]$BlindRow.metadata_path
                metadata_sha256 = [string]$BlindRow.metadata_sha256
                result_path = [string]$BlindRow.result_path
                result_sha256 = [string]$BlindRow.result_sha256
                work_root = [string]$BlindRow.work_root
                fact_review_path = [string]$BlindRow.fact_review_path
                fact_review_sha256 = [string]$BlindRow.fact_review_sha256
            }
        }
    )
}
$BlindMapText = ($BlindMapRecord | ConvertTo-Json -Compress -Depth 8) + "`n"
if ($BlindMapText.Contains("`r") -or $BlindMapText.Contains([char]0xFFFD) -or
    -not $BlindMapText.EndsWith("`n", [StringComparison]::Ordinal) -or
    $BlindMapText.EndsWith("`n`n", [StringComparison]::Ordinal)) {
    throw 'NEEDS_CONTEXT: deterministic blind-map text construction failed; no file was written.'
}
$BlindMapBytes = $StrictUtf8.GetBytes($BlindMapText)
Assert-Task3ExactDirectEntries $CopyRoot $RunRoots 'copy namespace at blind-map CreateNew boundary'
Assert-Task3AbsentDirectNamespace $CopyRoot 'blind-map.md' 'at blind-map CreateNew boundary'
$BlindMapStream = New-Object IO.FileStream -ArgumentList @(
    $BlindMapPath,
    [IO.FileMode]::CreateNew,
    [IO.FileAccess]::Write,
    [IO.FileShare]::None,
    4096,
    [IO.FileOptions]::WriteThrough
)
try {
    $BlindMapStream.Write($BlindMapBytes, 0, $BlindMapBytes.Length)
    $BlindMapStream.Flush($true)
} finally {
    $BlindMapStream.Dispose()
}
(Get-Item -LiteralPath $BlindMapPath -Force -ErrorAction Stop).IsReadOnly = $true
if (-not (Get-Item -LiteralPath $BlindMapPath -Force -ErrorAction Stop).IsReadOnly) {
    throw 'NEEDS_CONTEXT: blind map could not be frozen read-only; preserve it and stop.'
}
$ObservedBlindMapSha256 = (Get-FileHash -LiteralPath $BlindMapPath -Algorithm SHA256).Hash
$null = Read-Task3StrictBlindMap $BlindMapPath $ObservedBlindMapSha256 $BlindMapBytes 'immediately after create-new write'
if ($null -ne (Get-Variable -Name BlindMapSha256 -Scope 0 -ErrorAction SilentlyContinue)) {
    throw 'NEEDS_CONTEXT: BlindMapSha256 was already bound; preserve the blind map and stop.'
}
Set-Variable -Name BlindMapSha256 -Scope 0 -Option ReadOnly -Value $ObservedBlindMapSha256
$BlindMapVariable = Get-Variable -Name BlindMapSha256 -Scope 0 -ErrorAction Stop
if ($BlindMapVariable.Value -isnot [string] -or
    [string]$BlindMapVariable.Value -cne $ObservedBlindMapSha256 -or
    ($BlindMapVariable.Options -band [Management.Automation.ScopedItemOptions]::ReadOnly) -eq 0) {
    throw 'NEEDS_CONTEXT: frozen blind-map SHA-256 binding failed; preserve the blind map and stop.'
}
```

Expected: the blind map is one create-new, read-only, strict UTF-8 compact JSON object plus exactly one final LF. Its exact ordered schema is five top-level fields and three ordered 15-field candidate rows. The rows are labels `A`, `B`, `C` and an exact permutation of `run-01` through `run-03`; every canonical path, current artifact hash, and exact run-root namespace is reconstructed and checked. The strict reread must be byte-identical to the bytes constructed from `$BlindRows`, after which the physical uppercase hash is frozen in the read-only scope-0 variable `$BlindMapSha256`. Any write, schema, permutation, path, seal, or freeze failure preserves the create-new file and stops without retry.

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
$BlindMapPath = Get-Task3FixedCanonicalPath ([IO.Path]::Combine($CopyRoot, 'blind-map.md')) 'Task 3 blind map'
$null = Assert-Task3ApprovalState 'immediately before final blind handoff'
$null = Assert-Task3Task1Completion 'immediately before final blind handoff'
Assert-Task3Task2Completion 'immediately before final blind handoff'
$BlindMapVariable = Get-Variable -Name BlindMapSha256 -Scope 0 -ErrorAction Stop
if ($BlindMapVariable.Value -isnot [string] -or
    [string]$BlindMapVariable.Value -cnotmatch '^[0-9A-F]{64}$' -or
    [string]$BlindMapVariable.Value -cne [string]$BlindMapSha256 -or
    ($BlindMapVariable.Options -band [Management.Automation.ScopedItemOptions]::ReadOnly) -eq 0) {
    throw 'Frozen blind-map SHA-256 binding drifted before final handoff.'
}
$FreshBlindMap = Read-Task3StrictBlindMap $BlindMapPath ([string]$BlindMapSha256) $null 'initial final handoff reread'
$FreshCandidateTexts = [ordered]@{}
$FreshResultSha256s = [ordered]@{}
foreach ($CandidateRow in @($FreshBlindMap.candidates)) {
    $Label = [string]$CandidateRow.label
    $MetadataHashBefore = (Get-FileHash -LiteralPath ([string]$CandidateRow.metadata_path) -Algorithm SHA256).Hash
    if ($MetadataHashBefore -cne [string]$CandidateRow.metadata_sha256) {
        throw ('Candidate metadata drifted before fresh provenance reread: ' + $Label)
    }
    $FreshMetadata = Read-Task3StrictOpusMetadata `
        ([string]$CandidateRow.metadata_path) `
        ([string]$CandidateRow.work_root) `
        ('final handoff provenance for candidate ' + $Label)
    $StreamItem = Get-Item -LiteralPath ([string]$CandidateRow.stream_path) -Force -ErrorAction Stop
    $StderrItem = Get-Item -LiteralPath ([string]$CandidateRow.stderr_path) -Force -ErrorAction Stop
    if ([int64]$StreamItem.Length -le 0 -or
        [int64]$StderrItem.Length -ne [int64]$FreshMetadata.stderr_bytes -or
        (Get-FileHash -LiteralPath ([string]$CandidateRow.metadata_path) -Algorithm SHA256).Hash -cne
            [string]$CandidateRow.metadata_sha256) {
        throw ('Candidate provenance evidence drifted during fresh reread: ' + $Label)
    }
    $ResultHashBefore = (Get-FileHash -LiteralPath ([string]$CandidateRow.result_path) -Algorithm SHA256).Hash
    if ($ResultHashBefore -cne [string]$CandidateRow.result_sha256) {
        throw ('Candidate result drifted before fresh strict reread: ' + $Label)
    }
    $FreshResult = Read-Task3StrictCandidateResult `
        ([string]$CandidateRow.result_path) `
        ([string]$CandidateRow.run_root) `
        ([string]$CandidateRow.result_sha256) `
        ('final handoff result for candidate ' + $Label)
    $ResultHashAfter = (Get-FileHash -LiteralPath ([string]$CandidateRow.result_path) -Algorithm SHA256).Hash
    if ($ResultHashAfter -cne [string]$CandidateRow.result_sha256 -or
        $ResultHashAfter -cne $ResultHashBefore -or
        $FreshResult -isnot [pscustomobject] -or
        (@($FreshResult.PSObject.Properties.Name) -join '|') -cne 'text|sha256' -or
        $FreshResult.text -isnot [string] -or
        $FreshResult.sha256 -isnot [string] -or
        [string]$FreshResult.sha256 -cne [string]$CandidateRow.result_sha256) {
        throw ('Candidate result drifted during fresh strict reread: ' + $Label)
    }
    $FreshCandidateTexts.Add($Label, [string]$FreshResult.text)
    $FreshResultSha256s.Add($Label, $ResultHashAfter)
}
if ((@($FreshCandidateTexts.Keys) -join '|') -cne 'A|B|C' -or
    (@($FreshResultSha256s.Keys) -join '|') -cne 'A|B|C') {
    throw 'Final blind handoff did not reconstruct exactly candidates A, B, and C in label order.'
}
$null = Read-Task3StrictBlindMap $BlindMapPath ([string]$BlindMapSha256) $null 'final byte/hash reread before user display'
```

The Step 5 user-facing output must now use only `$FreshCandidateTexts['A']`, `$FreshCandidateTexts['B']`, and `$FreshCandidateTexts['C']`, in that order. Its anonymous provenance hashes must come only from `$FreshResultSha256s['A']`, `['B']`, and `['C']`. Do not use `$VerifiedRuns`, `$BlindRows`, generation order, or any Step 3 text variable when composing the message. Perform no read, write, generation, shuffle, or transformation after the final blind-map reread and before sending the complete raw texts. The remaining hard stop is unchanged: request selection, do not rank or edit, and stop before Phase B.

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

After the user selects exactly one raw candidate, first bind its literal `result_sha256` and create `docs/superpowers/plans/2026-08-14-terminal-collapse-ending-phase-b.md`. That second plan must contain complete, selected-copy-specific code and no prose placeholders. It must cover:

- `game/endings_expansion.rpy`: non-reserved `default iron_terminal_collapse_snapshot = None` and `default fall_cause = ""`; leave `ending_fall_epilogue` text unchanged.
- `game/chapter5.rpy`: reset/lock collapse snapshot; branch-entry and post-join guards; collapsed-menu visibility; hard-grind override; `prince_ally and not prince_betrayed` score; `fall_cause` entry writes; approved neutral-baron exchange; approved death sequence and three cause variants; skip `ending_side_characters_fate` for fall while retaining the fall epilogue.
- `game/test_game.rpy`: ordinary-difficulty player-feedback path; prepared frontal/flanking old-menu guards before any branch mutation; `None` mid-branch preservation; exact approved-copy/source contracts; a new `test_terminal_collapse_ending` reaching the unique approved death sentence while restoring persistent state.
- Real old-save validation: every fresh Phase B replay controller first consumes the same out-of-band `$ApprovalLockSha256`; strictly validates the exact ordered 26-field approval lock schema v3 with native JSON types, the complete direct-parent chain P2→S3→P3→R3, and the physical/raw v3 recovery plan/spec blobs. In that same fresh context it must strictly parse `.superpowers/sdd/terminal-collapse-ending/recovery-v3/task1-completion.json` schema v3 and `.superpowers/sdd/terminal-collapse-ending/recovery-v3/rules/task2-completion.json` schema v3, fix both physical completion hashes for the replay, re-hash the Task 1 exact 115+26=141 current-artifact union, and re-read all nine 14-field receipts plus the Task 2 exact 56 current-artifact union before it may trust the mother or helper. The replay controller must prove the mother is read-only and its basename/bytes/hash equal the `fresh_generator_v3` save, the generator completion's three target-copy lineage values, and all four clean-observer source/replay before/after hashes. The cleaned v3 generator/observer worktrees, SaveDirs, source target, and replay target are historical completion fields and must not be required to exist after successful Task 1 cleanup.
- Candidate isolation is absolute: the mandatory manifest-directed 141-union integrity pass may stream each predeclared artifact only to confirm its frozen bytes/hash row; it may not expose, copy, deserialize, select, or use either failed candidate. Outside that single union check, Phase B must not read, copy, hash-probe, enumerate as fallback, or otherwise touch either the legacy TIMEOUT candidate or the v2 `LOG_CONTRACT_MISMATCH` candidate. Both remain `preserved_not_used`; only `recovery-v3/mother/1-1-*.save` may seed a replay. Never infer completion from Markdown and never open the mother directly.
- Replay cardinality is recursive. Create one repository-external unique empty `SaveDir` and one fresh detached replay worktree for each frontal/flanking path; assert the worktree's `game/saves` is absent or task-owned empty, copy the mother under its exact engine filename to the external SaveDir root, then prove exactly one `1-1-*.save` exists recursively before launch, located at the external root. The external `sync/` and local `game/saves/` roots must contain no target slot before launch. After launch the same root replay must be byte-identical and there must still be no sync/local shadow target; `persistent` and an empty `sync/` directory are allowed non-target byproducts. Verify mother/source/replay-before/replay-after byte streams and SHA-256 values, not only filenames.
- Bind the exact ignored helpers under `.superpowers/sdd/terminal-collapse-ending/helpers/` to the 82,334 / 24,229 / 53,188 byte payloads and SHA-256 values `E0393DB1E113FDB8C35097978AA73B7D33AFDD5788499002B6423D883DEED4E8`, `73A3F9C43CF994E08F004E0A1266122A3EC5E0EAF065C63E6D9439CF0B0E1880`, and `20198B669F70E51E51F71BD01E6D06D1949D300F43CE9A94FB0190A47D781A15`. Launch each replay through one fresh dedicated helper host with process-local `SDL_VIDEODRIVER=dummy`, `SDL_AUDIODRIVER=dummy`, and `RENPY_RENDERER=sw`; require parent actual-host-exit/result mapping validation, then `Assert-PrivateDesktopSafetyEnvelope`, then explicitly require `Test-PrivateDesktopIntegralValue(result.root_exit_code)`, non-null root exit equal to the declared expected code, `COMPLETED`, helper-0, zero-window, and no-timeout. Capture stdout/stderr, helper-result schema-v2 Job/window diagnostics, provenance marker, and state assertions without treating PID/count diagnostics as coverage. Every other Phase B helper call with an expected target exit uses the same integral/non-null-before-compare gate. Each engine-native testcase must load its own copy, select exactly its named real choice, and prove `fall` occurs before any victory text or branch mutation. Missing/truncated/mismatched evidence, catastrophic host termination, any visible window, confirmation or interaction requirement, unknown token or label, fixture/marker mismatch, null/non-integral root exit, approval-lock drift, or sealed-artifact drift is `NEEDS_CONTEXT`; preserve the create-new attempt and never retry, use Computer Use, send real input, take screenshots, or use manual fallback.
- Final tests exactly once on the final tracked SHA: focused suites, `python -B -m unittest discover -s Tools -v`, portrait/narration/show/canon/AI-smell/release/font checks, `test_terminal_collapse_ending`, Full, Lint, process cleanup, diff scope, and independent Spec/Standards review.
- Final asset report: no new art/music/SFX/animation/UI; reuse existing `castle_exterior`, `battlefield`, black scene, and `war_drums.ogg`; measure actual font/package delta after approved text enters.

Phase B must end with the last tracked implementation commit before Final and independent reviews; no tracked evidence commit may follow those gates.

---

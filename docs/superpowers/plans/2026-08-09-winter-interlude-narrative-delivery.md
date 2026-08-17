# Winter Interlude Narrative Delivery Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deliver the approved winter interlude as user-approved Chinese prose, backed by six real fail-closed machine-JSON producers, a non-hard-coded capability gate, per-scene Batch proof, final-only copy contracts, one Final proof, and two fresh independent reviews.

**Architecture:** Keep `Tools/Run-WinterInterludeGate.ps1` as the sole public orchestrator and preserve its existing nine-step Narrative manifest, Job Object, dependency-lease, evidence-reservation, strict-JSON, and publication boundaries. Add two deep Python modules: `Tools/winter_narrative_json.py` owns the inherited-handle and standalone-create-new writer contract for all six JSON producers, while `Tools/winter_narrative_inputs.py` owns strict parsing and before/after membership validation for the tracked `Tools/winter_narrative_inputs.txt` inventory. Canon and portrait consume only its immutable inventory result; neither discovers evidence inputs with a glob or directory iterator. Extend the opaque native dependency lease with one four-argument inventory adapter that reads the inventory only through its already-leased handle and retains the inventory plus every listed Ren'Py input through child drain; all non-inventory steps keep the old two-argument interface. Each producer owns only its scanner and schema adapter. `Tools/check_winter_narrative_capabilities.py` computes every capability by running named real contract tests against the current project; it never hard-codes success. Prose delivery remains a separate human-approval workflow: each atomic scene uses isolated candidates, exactly one fresh verified `claude-opus-4-6` session, blind presentation of all three raw candidates, mechanical insertion of the same approved legacy spans into all three at the same anchors, blind presentation of all three complete composites, explicit user selection of one exact composite or rejection of all three, one atomic integration, and an immediate real Narrative Batch gate. Final-only length, reuse, semantic, placeholder, and literal-copy contracts are installed only after every scene is approved.

**Tech Stack:** Python 3 `argparse`/`ctypes`/`json`/`unittest`; Windows PowerShell 5.1; embedded C# 5 and existing Win32 gate primitives; Ren'Py 8.5.2 testsuite; Git; the local `invoke-opus-4-6` skill; SHA-256 evidence.

## Global Constraints

1. Start from the clean Task 7.5 implementation commit `cd26d62cda05e40dbcd6c953bd2e620a65d59c0c`. The dedicated-plan commit must have that exact parent, touch only this plan, and use subject `docs: plan winter interlude narrative delivery`.
2. Before implementation, verify that this plan has received two fresh independent reviews, one Spec and one Standards, both reporting exactly `Critical 0 / Important 0 - READY`. Reviewers must not read one another's decision.
3. Do not edit game prose, scanners, tests, the capability checker, the font, old-game files, assets, or shipping sources while authoring or reviewing this plan. The first implementation edit begins only after the plan commit and both READY decisions.
4. Execute every slice test-first. Preserve the raw behavior-specific RED, require `ERRORS=0` unless the slice explicitly tests process setup failure, apply only the named minimal GREEN, and rerun the focused command with an immediate real-exit guard.
5. Never manufacture a RED by changing an assertion after production is already green. Mutation REDs use a temporary copy or in-memory source, must record the immutable base blob and exact mutation, and must leave the tracked tree untouched.
6. `WINTER_GATE_STRUCTURED_OUTPUT_HANDLE` is the sole gate-mode write authority for all six producers. Gate mode never opens, creates, replaces, reopens, or falls back to `--output` by path. Standalone mode exists only when the variable is absent and uses exclusive `CREATE_NEW` without overwrite.
7. The shared writer accepts only one JSON object and emits strict UTF-8 without BOM. It rejects output above 1,048,576 UTF-8 bytes or 1,048,576 UTF-16 code units, container depth above 64, number tokens above 128 characters, non-finite numbers, unsupported values, and unpaired surrogates. It uses deterministic compact serialization and cannot emit duplicate keys. The separate input module exposes one immutable inventory through one validated context-manager interface; it accepts strict UTF-8 without BOM, normalizes CRLF to LF, rejects standalone CR, requires one terminal LF, enforces bounded canonical counts and strict Ordinal ordering, and requires the actual direct Ren'Py and PNG member sets to equal the inventory both before and after scanning.
8. In gate mode, parse one positive decimal handle, require its final path to equal the exact `--output` path with Windows `OrdinalIgnoreCase` semantics, clear handle inheritance, seek to zero, truncate, write all bytes, durably flush, and close the child duplicate. Missing, malformed, mismatched, or unwritable handles exit nonzero without a valid document.
9. Preserve the gate's existing reservation marker, share-mode-zero owner, exact direct-parent guard, fourth inherited JSON handle, three-handle non-JSON list, child-environment scrub, Job `ActiveProcesses == 0` boundary, owner-handle freeze/read, result and summary publication order, and outer-finally release. Task 8 may add dependency files to the Narrative manifest but must not weaken those boundaries. The inventory-aware lease first retains the inventory, parses it from that exact read handle without reopening its path, deduplicates fixed and listed dependencies with Windows `OrdinalIgnoreCase`, retains deny-write/delete handles for every listed Ren'Py input, and keeps the complete opaque lease alive through the existing child-drain and publication lifecycle.
10. Portrait evidence remains the sole nested structured output. Its `--output` must have exactly one registered direct parent matched with `OrdinalIgnoreCase`; prefix matching and `StartsWith` are forbidden. `--output-dir` is forbidden.
11. All producer documents must satisfy the schemas already enforced by `Get-GateJsonOutcome`. Canon JSON scans only inventory-listed Ren'Py inputs after applying its established skip list. Portrait JSON derives character definitions only from inventory-listed Ren'Py inputs and portrait stems only from inventory-listed PNG names. Temporary or unlisted direct Ren'Py/PNG members are stable-input drift and exit 2 without valid evidence; they never silently participate in output. Canon blocking count is exactly the sum of anti-logic, geography, terminology, and canon-deviation findings; trigger occurrences are informational and nonblocking. Common scanner count is exactly `len(findings)` and `scanned_files` must include `game/governance_winter_interlude.rpy`.
12. Capability booleans come from real named tests. Breaking any producer's schema, negative mutation, target coverage, structured-handle linkage, no-path-reopen rule, or no-fallback rule must make the corresponding capability false, `ready=false`, checker exit nonzero, and the real Narrative gate fail at ordinal 1.
13. Automated gates never approve prose. The user is the sole prose-quality authority. No approved scene text may be written to `game/governance_winter_interlude.rpy` until all three raw candidates have been shown unchanged in blind A/B/C order, the same approved legacy spans have been mechanically inserted into all three at the same anchors, all three complete composites have been shown in that same blind order, and the user explicitly selects one exact composite. Provenance remains hidden until that decision.
14. The writing-style library is currently `maturity_stage: seed` with no active examples or guidance. For each atomic scene, create three candidates in isolated contexts that cannot see one another. Exactly one candidate comes from one fresh verified `claude-opus-4-6` session for that scene; the other two are isolated controls. Randomize A/B/C and do not reveal provenance before the user's choice. A rejected scene starts fresh contexts and receives no rejected draft as input.
15. The Opus prompt contains only the current scene's complete fact card, continuous entry/exit context, characters present, known/unknown information, approved canon, required benefit/burden/bearer/action/follow-up facts, and requested plain-text blocks. It contains no local paths, Ren'Py syntax, prior output, rejected prose, historical archives, unapproved style summaries, or invocation/provenance instructions.
16. Invoke only `C:\Users\22325\.codex\skills\invoke-opus-4-6\scripts\invoke-opus.ps1`. Require metadata `success=true`, `model=expected_model=claude-opus-4-6`, and exactly that model in both observed-model arrays before reading the nonempty UTF-8 terminal result. Never use an API, fallback model, partial stream, or retry without a new user-directed scene loop.
17. Preserve every Task 7 label, call, jump, state write, menu key and visibility rule, investigation/policy/priority identifier, outcome contract, and cleanup path. Codex may fix only objective canon or Ren'Py integration errors; any material prose rewrite returns to a fresh candidate loop.
18. The six visible semantic expectations are coordinated test-owned literals: four omitted-report sentences, one shared-cause sentence, and one neutral-delegation sentence. Change a literal only in the same atomic scene commit after explicit approval, update production plus both independent expectations in `Tools/test_governance_winter_interlude.py` and `game/test_game.rpy`, preserve all six opposite-semantic mutations and real `_history` checks, then run the route matrix including delegation.
19. After each approved atomic scene commit, run the public Batch gate exactly once on that commit. Do not combine multiple scenes before a Batch proof. If Batch fails, fix only that scene or its already-approved tooling, rerun the focused failing step, amend the same scene commit, then run one fresh Batch gate on the amended SHA.
20. Install final-only contracts only after all scene commits are approved and Batch-green. Those tests must use the approved literal facts then present in the repository; they must not contain hypothetical or model-generated future prose.
21. Keep `game/msyh.ttf` unchanged until final text is integrated. Run `prepare_release.py` twice only in the final transition; the first exit may be 0 or 1, the second must be 0. If the font changes, include its exact byte delta in the final prose commit.
22. Never modify `game/governance.rpy` or delete legacy prose. Reuse is verbatim only: source substring hash, target occurrence, and Chinese-character count must agree. Any adapted wording is new prose and is excluded from the reuse numerator.
23. Do not add art, music, SFX, portraits, animation, or UI in Task 8. Reuse the existing backgrounds and `winter_wind`, `market_bustle`, `tension`, and `castle_calm`. The `bg study` granary mismatch remains the already-declared temporary Task 10 art debt. Report font and package deltas; other asset/package impact must remain zero.
24. Every commit stages an exact allowlist, runs `git diff --cached --check`, verifies the index paths, and checks tracked status immediately afterward. Never stage ignored evidence, unrelated user changes, old-game output, or generated reports.
25. Long gates are single-use per exact SHA. Capture stdout and stderr separately, require real exit 0, exactly one `Ran N tests` line, exactly one terminal `OK`, the planned count, unchanged tracked hashes, and owned PID count zero. Do not repeat a successful long gate on the same SHA.

## Task 8 Authorization and Hard Stop

The initial Spec and Standards READY decisions authorize only the complete
pre-prose tooling tasks written literally in this plan. They do not authorize
any prose integration.

Every scene identifier is enumerated literally in the Scene Order section. An
unnamed "next scene", a variable scene identifier, or any equivalent
metavariable is forbidden. A scene becomes executable only after its exact
addendum contains the complete approved literal test body, production patch,
anchors, commands, allowlist, approved raw SHA-256, approved composite SHA-256,
legacy-ledger bindings, and fresh independent Spec and Standards READY
decisions bound to that exact plan byte sequence.

Task 8 is complete only when every enumerated scene is explicitly
user-approved, each scene implementation has one green Batch proof on its exact
commit, all final-only literal contracts are installed, the one Final proof is
green on the final SHA, the frozen test counts match, both fresh final
implementation reviews report `Critical 0 / Important 0 - READY`, the index
and tracked tree are clean, and the asset/package audit is recorded.

Then STOP. Do not start umbrella Task 9, edit downstream consumers, build, package,
publish, or infer release authorization.

## Resolved Governance Decisions

1. **Task 7 authority is satisfied.** The accepted structural baseline is the clean Task 7.5 implementation at `cd26d62cda05e40dbcd6c953bd2e620a65d59c0c`, including its fresh independent Spec and Standards `Critical 0 / Important 0 - READY` decisions. Task 8 does not reopen Task 7 control-flow design; it adds only the narrowly test-owned prose/presentation seam specified below.
2. **Three candidates means one Opus candidate plus two isolated controls per scene.** Candidate O comes from one fresh process launched only through `invoke-opus.ps1`, locked to `claude-opus-4-6`. Candidates C1 and C2 come from two fresh isolated Codex writer agents. All three receive the same fact card, no candidate may see another candidate or the writing-style corpus, their A/B/C order is randomized, and provenance is revealed only after the user selects or rejects them. The raw A/B/C display and the later full-composite A/B/C display use the same hidden mapping. Thus every scene has exactly one fresh Opus session and still satisfies the repository's three-draft blind workflow.
3. **Rejected prose is transient.** Candidate prose is created only beneath three distinct validated task-owned temporary directories. The Opus directory includes its prompt, stream, metadata, and result; each control writer has a separate directory. After the user's decision, copy only the selected exact raw candidate and its mechanically assembled full composite to ignored evidence. Delete each rejected candidate's entire directory after resolving and verifying that its absolute path remains beneath the task-owned temporary root. A rejected-candidate record may retain only at most 200 Chinese characters of non-prose failure metadata permitted by `AGENTS.md`; it may not retain text or a recoverable excerpt. If all three are rejected, delete all three directories and start a new isolated round only on a new explicit user request.
4. **Approved prose enters through a reviewed literal scene addendum.** For the next literal scene in Scene Order, show all three raw candidates unchanged in their randomized blind A/B/C order. Mechanically insert the same scene-specific, user-approved legacy-ledger spans into all three candidates at the same predeclared anchors without changing any raw or reused byte. Show all three complete composites in the same blind order. The user either selects one exact complete composite or rejects all three; reveal candidate provenance only after that decision. Append a scene addendum named with that literal ID to this tracked plan. It records the fact-card SHA-256, verified Opus provenance, all three raw SHA-256 values, blind mapping, selected raw SHA-256, all three composite SHA-256 values, selected composite SHA-256, user-approval evidence, selected reuse IDs and hashes, the complete literal source test, complete literal production patch, exact unique target anchors, reversible raw-to-Ren'Py escaping/page-tag mapping, focused RED/GREEN command, Batch command, and exact commit allowlist. Commit only this plan change using the literal subject listed in the Scene Order section; obtain fresh independent Spec and Standards READY decisions on that exact plan byte sequence; only then implement the scene. Any addendum byte or player-visible prose change invalidates both review decisions and the user approval. This staged addendum is the only resolution of the impossibility of writing unknown future prose into the initial plan.
5. **Runtime literal ownership stays narrow.** Non-semantic scenes use independent Python source contracts plus the existing real route-matrix runtime suite. `game/test_game.rpy` changes only for the six coordinated visible semantic expectations or a separately approved runtime defect; scene integration approval alone does not authorize additional runtime literal mirrors.
6. **The control-signature migration is test-owned and precedes prose.** `_task7_control_signature` continues to own every Python statement, condition, menu, choice condition, call, jump, return, state write, and every interpolation AST. It accepts only bare literal say text or one static speaker identifier followed by one literal string; calls, assignments, named expressions, malformed interpolations, dynamic speakers, and nonliteral text remain invalid. A new `_task8_presentation_signature` independently records every `scene`, `show`, `hide`, `play`, `stop`, `with`, and `window` statement in exact order. Existing Task 7 presentation remains exact test-owned input; each reviewed addendum may add only its complete literal presentation sequence. Dynamic images, labels, audio, missing hides, wrong tags/positions, and reordered statements fail closed.
7. **The shared structured writer and immutable input inventory are approved dependencies.** `Tools/winter_narrative_json.py`, `Tools/winter_narrative_inputs.py`, and `Tools/winter_narrative_inputs.txt` are Task 8 owned paths. Each producer activation slice adds its helper modules and test-owned probe dependencies to the corresponding Narrative fixed dependencies. Capability, canon, and portrait additionally select the tracked inventory through `InventoryPath`; the native opaque lease pins the inventory and every listed Ren'Py input through child drain. The final linkage slice proves all six leases preserve their applicable helper, probe, inventory, and listed-input contracts. Producers never copy or bypass either deep module.
8. **Integration approval and corpus enrollment are distinct.** After a scene is integrated and Batch-green, show the clean selected text and ask the exact corpus-enrollment question required by `AGENTS.md`. Only an explicit qualifying reply authorizes a separate allowlisted writing-style commit. A corpus commit is outside the Task 8 implementation range unless the user separately authorizes it; absence of enrollment never blocks scene delivery.
9. **Task 9's stale batch reference is a hand-off, not Task 8 scope.** Task 8 records the approved closure scene plus the future downstream scene set as the replacement input for Task 9's obsolete `approved Opus batch 6` wording. Task 8 does not edit Task 9 consumers.

## Baseline and Owned Paths

The planning baseline is:

- HEAD: `cd26d62cda05e40dbcd6c953bd2e620a65d59c0c`
- public gate module: 87 tests
- governance module: 49 tests
- explicit `Tools` discovery: 339 tests (`Tools` has no `__init__.py`, so root
  discovery is forbidden because it reports a false-green zero tests)
- current Narrative behavior: Batch and Final both stop honestly at the absent capability checker before any child or scanner starts
- current winter prose: Task 7 structural placeholders only
- current canon blocking findings: zero

## Literal Scene Order

The only prose integration order is:

1. `S01-crisis-brief` — commit subject `docs: bind winter scene S01 crisis brief approved copy`
2. `S02-neutral-delegation` — `docs: bind winter scene S02 neutral delegation approved copy`
3. `S03-market-life` — `docs: bind winter scene S03 market life approved copy`
4. `S04-emergency-council` — `docs: bind winter scene S04 emergency council approved copy`
5. `S05-selected-market-investigation` — `docs: bind winter scene S05 selected market investigation approved copy`
6. `S06-selected-village-investigation` — `docs: bind winter scene S06 selected village investigation approved copy`
7. `S07-selected-granary-investigation` — `docs: bind winter scene S07 selected granary investigation approved copy`
8. `S08-selected-route-investigation` — `docs: bind winter scene S08 selected route investigation approved copy`
9. `S09-omitted-report-bundle` — `docs: bind winter scene S09 omitted report bundle approved copy`
10. `S10-crisis-escalation` — `docs: bind winter scene S10 crisis escalation approved copy`
11. `S11-two-layer-decision` — `docs: bind winter scene S11 two layer decision approved copy`
12. `S12-trade-preserve-consequence` — `docs: bind winter scene S12 trade preserve consequence approved copy`
13. `S13-trade-feed-now-consequence` — `docs: bind winter scene S13 trade feed now consequence approved copy`
14. `S14-ration-preserve-consequence` — `docs: bind winter scene S14 ration preserve consequence approved copy`
15. `S15-ration-feed-now-consequence` — `docs: bind winter scene S15 ration feed now consequence approved copy`
16. `S16-requisition-preserve-consequence` — `docs: bind winter scene S16 requisition preserve consequence approved copy`
17. `S17-requisition-feed-now-consequence` — `docs: bind winter scene S17 requisition feed now consequence approved copy`
18. `S18-closure-to-chapter2` — `docs: bind winter scene S18 closure to chapter2 approved copy`

No later scene starts until the preceding implementation commit is Batch-green.

Task 8 owns only these tracked paths:

- `docs/superpowers/plans/2026-08-09-winter-interlude-narrative-delivery.md` (approved scene addenda only)
- `Tools/winter_narrative_json.py` (new deep writer module)
- `Tools/winter_narrative_inputs.py` (new deep immutable-input module)
- `Tools/winter_narrative_inputs.txt` (tracked literal R/P inventory)
- `Tools/check_winter_narrative_capabilities.py`
- `Tools/scan_canon.py`
- `scan_missing_portraits.py`
- `scan_narration_overlap.py`
- `Tools/scan_show_before_prevention.py`
- `Tools/scan_nested_quotes.py`
- `Tools/test_winter_narrative_capabilities.py`
- `Tools/test_governance_winter_interlude.py`
- `Tools/test_winter_interlude_gate.py`
- `Tools/Run-WinterInterludeGate.ps1`
- `docs/development/winter-interlude-content-ledger.md`
- `game/governance_winter_interlude.rpy`
- `game/test_game.rpy`
- `game/msyh.ttf` only if `prepare_release.py` changes it after final approved copy

No Task 8 commit may contain any other tracked path.

## Commit Map

1. `test: specify winter narrative json transport`
2. `feat: add winter narrative capability gate`
3. `feat: publish strict canon evidence`
4. `feat: publish scoped portrait evidence`
5. `feat: publish narration overlap evidence`
6. `feat: scan winter show prevention`
7. `feat: publish scoped nested quote evidence`
8. `test: bind winter capabilities to real producers`
9. `test: open the winter prose integration seam`
10. `docs: bind winter legacy reuse contract`
11. `docs: ledger approved winter source passages`
12. the 18 literal plan-only addendum subjects listed in Scene Order, each followed only after fresh dual READY by the matching implementation subject `feat: write winter scene S01` through `feat: write winter scene S18`
13. `docs: bind winter final narrative contracts`
14. `feat: finalize winter interlude prose`

The final implementation range begins after the dedicated-plan commit and ends
at `feat: finalize winter interlude prose`. All tracked ledgers and delivery
evidence must already be folded into their owning implementation commit before
the final proof; no tracked write or commit may follow it. Do not squash scene
approvals: their one-scene/one-Batch provenance is part of the delivery
contract.

---

## Task 0: Verify the approved plan-only starting point

**Files:**

- Read: docs/superpowers/plans/2026-08-09-winter-interlude-narrative-delivery.md
- Read: .superpowers/sdd/task8-plan-review-input.json
- Read: .superpowers/sdd/task8-plan-spec-review.json
- Read: .superpowers/sdd/task8-plan-standards-review.json

The plan-review input has exactly five properties:
schema_version, baseline, plan_head, plan_path, and plan_canonical_sha256.
Each decision has exactly nine properties: schema_version, review_axis,
reviewer_id, review_input_sha256, head, critical_count, important_count,
verdict, and raw_report.

- [ ] **Step 1: Run the exact plan/start validator before editing any implementation file**

```powershell
$ErrorActionPreference = 'Stop'
$baseline = 'cd26d62cda05e40dbcd6c953bd2e620a65d59c0c'
$planPath = 'docs/superpowers/plans/2026-08-09-winter-interlude-narrative-delivery.md'
$inputPath = '.superpowers/sdd/task8-plan-review-input.json'
$specPath = '.superpowers/sdd/task8-plan-spec-review.json'
$standardsPath = '.superpowers/sdd/task8-plan-standards-review.json'

function Get-CanonicalTextSha256 {
    param([Parameter(Mandatory = $true)][string]$Path)

    $bytes = [IO.File]::ReadAllBytes((Resolve-Path -LiteralPath $Path).Path)
    if ($bytes.Length -ge 3 -and
        $bytes[0] -eq 0xEF -and
        $bytes[1] -eq 0xBB -and
        $bytes[2] -eq 0xBF) {
        throw "UTF-8 BOM is forbidden: $Path"
    }
    $strictUtf8 = New-Object Text.UTF8Encoding($false, $true)
    $text = $strictUtf8.GetString($bytes).Replace("`r`n", "`n")
    if ($text.Contains("`r")) {
        throw "Standalone CR is forbidden: $Path"
    }
    $canonical = $strictUtf8.GetBytes($text)
    $sha = [Security.Cryptography.SHA256]::Create()
    try {
        -join ($sha.ComputeHash($canonical) | ForEach-Object { $_.ToString('X2') })
    } finally {
        $sha.Dispose()
    }
}

$head = (git rev-parse HEAD).Trim()
$parent = (git rev-parse HEAD^).Trim()
if ($parent -cne $baseline) { throw "Task 8 plan parent drifted: $parent" }
if ((git log -1 --pretty=%s).Trim() -cne 'docs: plan winter interlude narrative delivery') {
    throw 'Task 8 plan commit subject is wrong.'
}
$commitPaths = [string[]]@(git diff-tree --no-commit-id --name-only -r HEAD)
if ($commitPaths.Count -ne 1 -or $commitPaths[0] -cne $planPath) {
    throw "Task 8 plan commit scope is wrong: $($commitPaths -join ', ')"
}
git diff --check HEAD^ HEAD
if ($LASTEXITCODE -ne 0) { throw 'Task 8 plan commit failed diff-check.' }
if (git status --short) { throw 'Task 8 implementation did not start clean.' }

$inputBytesHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $inputPath).Hash
$input = Get-Content -LiteralPath $inputPath -Raw -Encoding UTF8 | ConvertFrom-Json
$expectedInputProperties = [string[]]@(
    'schema_version',
    'baseline',
    'plan_head',
    'plan_path',
    'plan_canonical_sha256'
)
$actualInputProperties = [string[]]@($input.PSObject.Properties.Name)
if (@(Compare-Object ($expectedInputProperties | Sort-Object) ($actualInputProperties | Sort-Object)).Count -ne 0) {
    throw 'Task 8 plan review input properties are not exact.'
}
if (-not ($input.schema_version -is [int]) -or $input.schema_version -ne 1) {
    throw 'Task 8 plan review input schema_version is not strict integer 1.'
}
if (-not ($input.baseline -is [string]) -or $input.baseline -cne $baseline -or
    -not ($input.plan_head -is [string]) -or $input.plan_head -cne $head -or
    -not ($input.plan_path -is [string]) -or $input.plan_path -cne $planPath) {
    throw 'Task 8 plan review input is bound to the wrong commit or path.'
}
$planCanonical = Get-CanonicalTextSha256 -Path $planPath
if (-not ($input.plan_canonical_sha256 -is [string]) -or
    $input.plan_canonical_sha256 -cne $planCanonical) {
    throw 'Task 8 plan canonical hash does not match review input.'
}

$decisions = @()
foreach ($entry in @(
    [pscustomobject]@{ Path = $specPath; Axis = 'Spec' },
    [pscustomobject]@{ Path = $standardsPath; Axis = 'Standards' }
)) {
    $parsed = @(Get-Content -LiteralPath $entry.Path -Raw -Encoding UTF8 | ConvertFrom-Json)
    if ($parsed.Count -ne 1) { throw "$($entry.Axis) decision is not one object." }
    $decision = $parsed[0]
    $expectedDecisionProperties = [string[]]@(
        'schema_version',
        'review_axis',
        'reviewer_id',
        'review_input_sha256',
        'head',
        'critical_count',
        'important_count',
        'verdict',
        'raw_report'
    )
    $actualDecisionProperties = [string[]]@($decision.PSObject.Properties.Name)
    if (@(Compare-Object ($expectedDecisionProperties | Sort-Object) ($actualDecisionProperties | Sort-Object)).Count -ne 0) {
        throw "$($entry.Axis) decision properties are not exact."
    }
    if (-not ($decision.schema_version -is [int]) -or $decision.schema_version -ne 1 -or
        -not ($decision.critical_count -is [int]) -or $decision.critical_count -ne 0 -or
        -not ($decision.important_count -is [int]) -or $decision.important_count -ne 0) {
        throw "$($entry.Axis) decision counts are not strict zero integers."
    }
    if (-not ($decision.review_axis -is [string]) -or $decision.review_axis -cne $entry.Axis -or
        -not ($decision.reviewer_id -is [string]) -or [string]::IsNullOrWhiteSpace($decision.reviewer_id) -or
        -not ($decision.review_input_sha256 -is [string]) -or $decision.review_input_sha256 -cne $inputBytesHash -or
        -not ($decision.head -is [string]) -or $decision.head -cne $head -or
        -not ($decision.verdict -is [string]) -or $decision.verdict -cne 'READY' -or
        -not ($decision.raw_report -is [string]) -or
        $decision.raw_report -notmatch '(?m)^Critical 0 / Important 0 - READY$' -or
        $decision.raw_report -match '(?i)\bNOT\s+READY\b') {
        throw "$($entry.Axis) decision is not READY on the exact plan input."
    }
    $decisions += $decision
}
if ($decisions[0].reviewer_id -ceq $decisions[1].reviewer_id) {
    throw 'Spec and Standards plan reviewers are not independent.'
}
```

Expected: no output and exit 0. Any plan byte, topology, subject, path, decision
count, reviewer, or readiness mismatch stops Task 8 before an implementation
file is touched.

- [ ] **Step 2: Reproduce the literal inventory bytes from the approved tree**

Run this read-only preflight before Task 1. It does not require the tracked
inventory to exist yet; it proves the approved tree still reproduces the exact
Task 2 literal body.

```powershell
$rpy = [string[]]@(
    Get-ChildItem -LiteralPath game -File |
        Where-Object { $_.Extension -ieq '.rpy' } |
        ForEach-Object { 'game/' + $_.Name }
)
$png = [string[]]@(
    Get-ChildItem -LiteralPath game/images -File |
        Where-Object { $_.Extension -ieq '.png' } |
        ForEach-Object { $_.Name }
)
[Array]::Sort($rpy, [StringComparer]::Ordinal)
[Array]::Sort($png, [StringComparer]::Ordinal)
if ($rpy.Count -ne 57 -or $png.Count -ne 197) {
    throw "Winter inventory count drift: R=$($rpy.Count), P=$($png.Count)"
}
foreach ($entry in $rpy) {
    if ($entry -cnotmatch '^game/[a-z0-9_]+[.]rpy$') {
        throw "Invalid direct Ren'Py inventory member: $entry"
    }
}
foreach ($entry in $png) {
    if ($entry -cnotmatch '^[a-z0-9_]+[.]png$') {
        throw "Invalid direct portrait inventory member: $entry"
    }
}
$lines = New-Object 'System.Collections.Generic.List[string]'
$lines.Add("WINTER_NARRATIVE_INPUTS_V1`tR=$($rpy.Count)`tP=$($png.Count)")
foreach ($entry in $rpy) { $lines.Add("R`t$entry") }
foreach ($entry in $png) { $lines.Add("P`t$entry") }
$strictUtf8 = New-Object Text.UTF8Encoding($false, $true)
$bytes = $strictUtf8.GetBytes(($lines -join "`n") + "`n")
$sha = [Security.Cryptography.SHA256]::Create()
try {
    $actual = -join (
        $sha.ComputeHash($bytes) |
            ForEach-Object { $_.ToString('X2') }
    )
} finally {
    $sha.Dispose()
}
if ($bytes.Length -ne 5456 -or
    $actual -cne '55776C4387F7648A5713EE87D929F3C7D6BC310811F60490DDD390FED240A9CF') {
    throw "Winter inventory literal drift: bytes=$($bytes.Length), sha=$actual"
}
```

Expected: exit 0, `R=57`, `P=197`, 5,456 canonical bytes, and the exact
SHA-256 shown above. Any direct member change requires a separately reviewed
inventory update; do not regenerate it opportunistically during Task 8.

---

## Task 1: Specify and implement the shared structured-output writer

**Files:**

- Create: `Tools/winter_narrative_json.py`
- Create: `Tools/test_winter_narrative_capabilities.py`

### Interface

The deep module exposes only:

```python
STRUCTURED_OUTPUT_ENV = "WINTER_GATE_STRUCTURED_OUTPUT_HANDLE"
WINTER_GATE_JOB_ENV = "WINTER_GATE_JOB_NAME"

class StructuredOutputError(RuntimeError):
    """Structured-output contract violation."""

class StructuredJsonSink:
    @classmethod
    def claim(cls, output_path: str) -> "StructuredJsonSink":
        """Claim and de-inherit the gate handle, or reserve standalone CREATE_NEW."""

    def write(self, document: dict[str, object]) -> None:
        """Write one document through the already-claimed descriptor."""

    def close(self) -> None:
        """Close the claimed descriptor without reopening its path."""

def encode_json_document(document: dict[str, object]) -> bytes:
    """Return one bounded strict UTF-8 JSON object without BOM."""

def write_json_document(document: dict[str, object], output_path: str) -> None:
    """Write through the inherited gate handle or standalone CREATE_NEW."""
```

Producers catch `StructuredOutputError`, `OSError`, `UnicodeError`, `TypeError`, and `ValueError`, print one diagnostic to stderr, and exit 2. They never receive a file object and never implement their own output fallback.

- [ ] **Step 1: Add the writer test catalog and prove the missing-module RED**

Create `Tools/test_winter_narrative_capabilities.py` with exactly this initial body:

```python
import ctypes
import json
import os
import subprocess
import sys
import tempfile
import unittest
from ctypes import wintypes
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WRITER = ROOT / "Tools" / "winter_narrative_json.py"
PYTHON = Path(sys.executable).resolve()
HANDLE_ENV = "WINTER_GATE_STRUCTURED_OUTPUT_HANDLE"
JOB_ENV = "WINTER_GATE_JOB_NAME"


class _ShareZeroFile:
    GENERIC_READ = 0x80000000
    GENERIC_WRITE = 0x40000000
    CREATE_NEW = 1
    FILE_ATTRIBUTE_NORMAL = 0x00000080
    HANDLE_FLAG_INHERIT = 0x00000001
    OPEN_EXISTING = 3

    def __init__(
        self,
        path: Path,
        *,
        access: int | None = None,
        disposition: int | None = None,
    ) -> None:
        self.path = path
        self.kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
        create_file = self.kernel32.CreateFileW
        create_file.argtypes = (
            wintypes.LPCWSTR,
            wintypes.DWORD,
            wintypes.DWORD,
            ctypes.c_void_p,
            wintypes.DWORD,
            wintypes.DWORD,
            wintypes.HANDLE,
        )
        create_file.restype = wintypes.HANDLE
        handle = create_file(
            str(path),
            access if access is not None else self.GENERIC_READ | self.GENERIC_WRITE,
            0,
            None,
            disposition if disposition is not None else self.CREATE_NEW,
            self.FILE_ATTRIBUTE_NORMAL,
            None,
        )
        if not handle or int(handle) == ctypes.c_void_p(-1).value:
            raise ctypes.WinError(ctypes.get_last_error())
        self.handle = int(handle)
        set_handle_information = self.kernel32.SetHandleInformation
        set_handle_information.argtypes = (
            wintypes.HANDLE,
            wintypes.DWORD,
            wintypes.DWORD,
        )
        set_handle_information.restype = wintypes.BOOL
        if not set_handle_information(
            wintypes.HANDLE(self.handle),
            self.HANDLE_FLAG_INHERIT,
            self.HANDLE_FLAG_INHERIT,
        ):
            self.close()
            raise ctypes.WinError(ctypes.get_last_error())

    def write_bytes(self, content: bytes) -> None:
        write_file = self.kernel32.WriteFile
        write_file.argtypes = (
            wintypes.HANDLE,
            ctypes.c_void_p,
            wintypes.DWORD,
            ctypes.POINTER(wintypes.DWORD),
            ctypes.c_void_p,
        )
        write_file.restype = wintypes.BOOL
        buffer = ctypes.create_string_buffer(content)
        written = wintypes.DWORD()
        if not write_file(
            wintypes.HANDLE(self.handle),
            buffer,
            len(content),
            ctypes.byref(written),
            None,
        ):
            raise ctypes.WinError(ctypes.get_last_error())
        if int(written.value) != len(content):
            raise OSError("marker write was incomplete")
        flush = self.kernel32.FlushFileBuffers
        flush.argtypes = (wintypes.HANDLE,)
        flush.restype = wintypes.BOOL
        if not flush(wintypes.HANDLE(self.handle)):
            raise ctypes.WinError(ctypes.get_last_error())

    def close(self) -> None:
        if self.handle is None:
            return
        handle, self.handle = self.handle, None
        close_handle = self.kernel32.CloseHandle
        close_handle.argtypes = (wintypes.HANDLE,)
        close_handle.restype = wintypes.BOOL
        if not close_handle(wintypes.HANDLE(handle)):
            raise ctypes.WinError(ctypes.get_last_error())

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()


def _run_writer_child(
    output_path: Path,
    handle_value: str,
    document: dict[str, object] | None = None,
) -> subprocess.CompletedProcess[str]:
    payload = (
        {"schema_version": 1, "value": "owned"}
        if document is None
        else document
    )
    code = (
        "import ctypes,json,msvcrt,sys; "
        "from ctypes import wintypes; "
        "from Tools.winter_narrative_json import StructuredJsonSink; "
        "sink=StructuredJsonSink.claim(sys.argv[2]); "
        "handle=msvcrt.get_osfhandle(sink._fd); "
        "kernel32=ctypes.WinDLL('kernel32',use_last_error=True); "
        "get_info=kernel32.GetHandleInformation; "
        "get_info.argtypes=(wintypes.HANDLE,ctypes.POINTER(wintypes.DWORD)); "
        "get_info.restype=wintypes.BOOL; "
        "flags=wintypes.DWORD(); "
        "assert get_info(wintypes.HANDLE(handle),ctypes.byref(flags)); "
        "print(int(flags.value)); "
        "sink.write(json.loads(sys.argv[1])); sink.close()"
    )
    environment = os.environ.copy()
    environment[HANDLE_ENV] = handle_value
    return subprocess.run(
        [
            str(PYTHON),
            "-B",
            "-c",
            code,
            json.dumps(payload, ensure_ascii=False),
            str(output_path),
        ],
        cwd=ROOT,
        env=environment,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="strict",
        close_fds=False,
        check=False,
    )


class WinterStructuredJsonWriterTests(unittest.TestCase):
    def test_writer_module_exists_with_exact_public_surface(self) -> None:
        self.assertTrue(WRITER.is_file())
        from Tools import winter_narrative_json

        self.assertEqual(
            winter_narrative_json.__all__,
            (
                "STRUCTURED_OUTPUT_ENV",
                "WINTER_GATE_JOB_ENV",
                "StructuredOutputError",
                "StructuredJsonSink",
                "encode_json_document",
                "write_json_document",
            ),
        )
        source = WRITER.read_text(encoding="utf-8")
        self.assertEqual(source.count("WINTER_GATE_STRUCTURED_OUTPUT_HANDLE"), 1)
        self.assertEqual(source.count("class StructuredJsonSink:"), 1)
        self.assertEqual(source.count("def encode_json_document("), 1)
        self.assertEqual(source.count("def write_json_document("), 1)
        self.assertEqual(source.count("CompareStringOrdinal"), 1)

    def test_encoder_enforces_utf8_utf16_depth_number_and_value_limits(self) -> None:
        from Tools.winter_narrative_json import (
            StructuredOutputError,
            encode_json_document,
        )

        fixed = len('{"value":""}')
        exact_text = "x" * (1_048_576 - fixed)
        exact = encode_json_document({"value": exact_text})
        self.assertEqual(len(exact), 1_048_576)
        self.assertFalse(exact.startswith(b"\xef\xbb\xbf"))
        self.assertEqual(
            encode_json_document({"b": 1, "a": 2}),
            b'{"a":2,"b":1}',
        )
        with self.assertRaisesRegex(StructuredOutputError, "utf8_too_long"):
            encode_json_document({"value": exact_text + "x"})

        astral = "😀" * (((1_048_576 - fixed) // 2) + 1)
        with self.assertRaisesRegex(StructuredOutputError, "utf16_too_long"):
            encode_json_document({"value": astral})

        depth64: object = None
        for _ in range(63):
            depth64 = {"value": depth64}
        encode_json_document({"value": depth64})
        with self.assertRaisesRegex(StructuredOutputError, "depth_exceeded"):
            encode_json_document({"value": {"value": depth64}})

        encode_json_document({"value": int("9" * 128)})
        with self.assertRaisesRegex(StructuredOutputError, "number_too_long"):
            encode_json_document({"value": int("9" * 129)})

        for invalid in (
            {"value": float("nan")},
            {"value": float("inf")},
            {"value": {1, 2}},
            {"value": "\ud800"},
        ):
            with self.subTest(invalid=repr(invalid)):
                with self.assertRaises((StructuredOutputError, UnicodeError)):
                    encode_json_document(invalid)

    def test_standalone_mode_is_create_new_and_never_overwrites(self) -> None:
        from Tools.winter_narrative_json import write_json_document

        with tempfile.TemporaryDirectory(prefix="winter-json-standalone-") as raw:
            output = Path(raw) / "evidence.json"
            previous_handle = os.environ.pop(HANDLE_ENV, None)
            previous_job = os.environ.pop(JOB_ENV, None)
            try:
                write_json_document({"schema_version": 1}, str(output))
                first = output.read_bytes()
                with self.assertRaises(FileExistsError):
                    write_json_document({"schema_version": 2}, str(output))
                self.assertEqual(output.read_bytes(), first)
            finally:
                os.environ.pop(HANDLE_ENV, None)
                os.environ.pop(JOB_ENV, None)
                if previous_handle is not None:
                    os.environ[HANDLE_ENV] = previous_handle
                if previous_job is not None:
                    os.environ[JOB_ENV] = previous_job

    def test_gate_mode_uses_the_exact_inherited_handle_and_clears_inheritance(self) -> None:
        with tempfile.TemporaryDirectory(prefix="winter-json-handle-") as raw:
            output = Path(raw) / "owned.json"
            with _ShareZeroFile(output) as owner:
                owner.write_bytes(b"WINTER_GATE_RESERVED_V1:must-be-truncated")
                completed = _run_writer_child(
                    Path(str(output).upper()),
                    str(owner.handle),
                )
                self.assertEqual(completed.returncode, 0, completed.stderr)
                self.assertEqual(completed.stdout.strip(), "0")
            self.assertEqual(
                json.loads(output.read_text(encoding="utf-8")),
                {"schema_version": 1, "value": "owned"},
            )

    def test_gate_mode_rejects_missing_malformed_and_mismatched_handles_without_fallback(self) -> None:
        with tempfile.TemporaryDirectory(prefix="winter-json-reject-") as raw:
            root = Path(raw)
            missing = root / "missing-handle.json"
            environment = os.environ.copy()
            environment.pop(HANDLE_ENV, None)
            environment[JOB_ENV] = "Local\\WinterGate-test"
            code = (
                "from Tools.winter_narrative_json import write_json_document; "
                "write_json_document({'schema_version':1}, "
                + repr(str(missing))
                + ")"
            )
            completed = subprocess.run(
                [str(PYTHON), "-B", "-c", code],
                cwd=ROOT,
                env=environment,
                stdin=subprocess.DEVNULL,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding="utf-8",
                errors="strict",
                check=False,
            )
            self.assertNotEqual(completed.returncode, 0)
            self.assertFalse(missing.exists())

            for value in ("", "0", "-1", "+5", " 5", "five"):
                with self.subTest(handle=value):
                    output = root / ("malformed-" + str(len(list(root.iterdir()))) + ".json")
                    completed = _run_writer_child(output, value)
                    self.assertNotEqual(completed.returncode, 0)
                    self.assertFalse(output.exists())

            owned = root / "owned.json"
            wrong = root / "wrong.json"
            with _ShareZeroFile(owned) as owner:
                completed = _run_writer_child(wrong, str(owner.handle))
                self.assertNotEqual(completed.returncode, 0)
                self.assertFalse(wrong.exists())
            self.assertEqual(owned.read_bytes(), b"")

            read_only = root / "read-only.json"
            read_only.write_bytes(b"unchanged")
            with _ShareZeroFile(
                read_only,
                access=_ShareZeroFile.GENERIC_READ,
                disposition=_ShareZeroFile.OPEN_EXISTING,
            ) as owner:
                completed = _run_writer_child(read_only, str(owner.handle))
                self.assertNotEqual(completed.returncode, 0)
            self.assertEqual(read_only.read_bytes(), b"unchanged")
```

Run the single behavior RED:

```powershell
$red = & python -m unittest `
  Tools.test_winter_narrative_capabilities.WinterStructuredJsonWriterTests.test_writer_module_exists_with_exact_public_surface `
  -v 2>&1
$redExit = $LASTEXITCODE
$red | Set-Content -LiteralPath .superpowers/sdd/task8-writer-red.txt -Encoding UTF8
if ($redExit -eq 0) { throw 'Writer RED unexpectedly passed.' }
$joined = $red -join "`n"
if ($joined -notmatch 'Ran 1 test' -or
    $joined -notmatch 'FAILED \(failures=1\)' -or
    $joined -match '(?m)^ERROR:') {
  throw 'Writer RED did not fail only on the missing deep module.'
}
```

Expected RED: `Ran 1 test`, one assertion failure because `Tools/winter_narrative_json.py` is absent, and no import, syntax, or environment error.

- [ ] **Step 2: Add the complete deep writer module**

Create `Tools/winter_narrative_json.py` with exactly:

```python
from __future__ import annotations

import ctypes
import json
import math
import msvcrt
import os
import re
from ctypes import wintypes


STRUCTURED_OUTPUT_ENV = "WINTER_GATE_STRUCTURED_OUTPUT_HANDLE"
WINTER_GATE_JOB_ENV = "WINTER_GATE_JOB_NAME"
_MAXIMUM_UTF8_BYTES = 1_048_576
_MAXIMUM_UTF16_UNITS = 1_048_576
_MAXIMUM_CONTAINER_DEPTH = 64
_MAXIMUM_NUMBER_TOKEN = 128
_DECIMAL_HANDLE = re.compile(r"[1-9][0-9]*\Z")
_HANDLE_FLAG_INHERIT = 0x00000001
_FINAL_PATH_BUFFER = 32_768

__all__ = (
    "STRUCTURED_OUTPUT_ENV",
    "WINTER_GATE_JOB_ENV",
    "StructuredOutputError",
    "StructuredJsonSink",
    "encode_json_document",
    "write_json_document",
)


class StructuredOutputError(RuntimeError):
    """Structured-output contract violation."""


def _number_token(value: int | float) -> str:
    if isinstance(value, float) and not math.isfinite(value):
        raise StructuredOutputError("non_finite_number")
    try:
        token = json.dumps(value, allow_nan=False, separators=(",", ":"))
    except (TypeError, ValueError) as error:
        raise StructuredOutputError("invalid_number") from error
    if len(token) > _MAXIMUM_NUMBER_TOKEN:
        raise StructuredOutputError("number_too_long")
    return token


def _validate_value(value: object, depth: int) -> None:
    if value is None or isinstance(value, (str, bool)):
        return
    if isinstance(value, int) and not isinstance(value, bool):
        _number_token(value)
        return
    if isinstance(value, float):
        _number_token(value)
        return
    if isinstance(value, dict):
        if depth > _MAXIMUM_CONTAINER_DEPTH:
            raise StructuredOutputError("depth_exceeded")
        for key, item in value.items():
            if not isinstance(key, str):
                raise StructuredOutputError("non_string_property")
            _validate_value(item, depth + 1)
        return
    if isinstance(value, list):
        if depth > _MAXIMUM_CONTAINER_DEPTH:
            raise StructuredOutputError("depth_exceeded")
        for item in value:
            _validate_value(item, depth + 1)
        return
    raise StructuredOutputError("unsupported_json_value")


def encode_json_document(document: dict[str, object]) -> bytes:
    if type(document) is not dict:
        raise StructuredOutputError("root_not_object")
    _validate_value(document, 1)
    try:
        text = json.dumps(
            document,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        encoded = text.encode("utf-8", errors="strict")
        utf16_units = len(text.encode("utf-16-le", errors="strict")) // 2
    except UnicodeError as error:
        raise StructuredOutputError("invalid_surrogate") from error
    if utf16_units > _MAXIMUM_UTF16_UNITS:
        raise StructuredOutputError("utf16_too_long")
    if len(encoded) > _MAXIMUM_UTF8_BYTES:
        raise StructuredOutputError("utf8_too_long")
    return encoded


def _normalize_windows_path(path: str) -> str:
    normalized = path
    if normalized.startswith("\\\\?\\UNC\\"):
        normalized = "\\\\" + normalized[8:]
    elif normalized.startswith("\\\\?\\"):
        normalized = normalized[4:]
    return os.path.normpath(os.path.abspath(normalized))


def _same_windows_path(left: str, right: str) -> bool:
    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    compare_ordinal = kernel32.CompareStringOrdinal
    compare_ordinal.argtypes = (
        wintypes.LPCWSTR,
        ctypes.c_int,
        wintypes.LPCWSTR,
        ctypes.c_int,
        wintypes.BOOL,
    )
    compare_ordinal.restype = ctypes.c_int
    result = int(compare_ordinal(left, -1, right, -1, True))
    if result == 0:
        raise ctypes.WinError(ctypes.get_last_error())
    return result == 2


def _final_path(handle: int) -> str:
    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    get_final_path = kernel32.GetFinalPathNameByHandleW
    get_final_path.argtypes = (
        wintypes.HANDLE,
        wintypes.LPWSTR,
        wintypes.DWORD,
        wintypes.DWORD,
    )
    get_final_path.restype = wintypes.DWORD
    buffer = ctypes.create_unicode_buffer(_FINAL_PATH_BUFFER)
    length = int(
        get_final_path(
            wintypes.HANDLE(handle),
            buffer,
            len(buffer),
            0,
        )
    )
    if length == 0:
        raise ctypes.WinError(ctypes.get_last_error())
    if length >= len(buffer):
        raise StructuredOutputError("final_path_too_long")
    return buffer.value


def _clear_inheritance(handle: int) -> None:
    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    set_handle_information = kernel32.SetHandleInformation
    set_handle_information.argtypes = (
        wintypes.HANDLE,
        wintypes.DWORD,
        wintypes.DWORD,
    )
    set_handle_information.restype = wintypes.BOOL
    if not set_handle_information(
        wintypes.HANDLE(handle),
        _HANDLE_FLAG_INHERIT,
        0,
    ):
        raise ctypes.WinError(ctypes.get_last_error())


def _close_windows_handle(handle: int) -> None:
    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    close_handle = kernel32.CloseHandle
    close_handle.argtypes = (wintypes.HANDLE,)
    close_handle.restype = wintypes.BOOL
    if not close_handle(wintypes.HANDLE(handle)):
        raise ctypes.WinError(ctypes.get_last_error())


def _write_fd(fd: int, content: bytes) -> None:
    os.lseek(fd, 0, os.SEEK_SET)
    os.ftruncate(fd, 0)
    view = memoryview(content)
    while view:
        written = os.write(fd, view)
        if written <= 0:
            raise OSError("structured output write made no progress")
        view = view[written:]
    os.fsync(fd)


class StructuredJsonSink:
    def __init__(self, fd: int) -> None:
        self._fd = fd
        self._written = False

    @classmethod
    def claim(cls, output_path: str) -> "StructuredJsonSink":
        if not isinstance(output_path, str) or not output_path:
            raise StructuredOutputError("missing_output_path")
        if STRUCTURED_OUTPUT_ENV in os.environ:
            raw_value = os.environ[STRUCTURED_OUTPUT_ENV]
            if _DECIMAL_HANDLE.fullmatch(raw_value) is None:
                raise StructuredOutputError("invalid_inherited_handle")
            handle = int(raw_value, 10)
            converted = False
            try:
                actual = _normalize_windows_path(_final_path(handle))
                expected = _normalize_windows_path(output_path)
                if not _same_windows_path(actual, expected):
                    raise StructuredOutputError(
                        "inherited_handle_path_mismatch"
                    )
                _clear_inheritance(handle)
                fd = msvcrt.open_osfhandle(handle, os.O_RDWR | os.O_BINARY)
                converted = True
                return cls(fd)
            finally:
                if not converted:
                    try:
                        _close_windows_handle(handle)
                    except OSError as error:
                        raise StructuredOutputError(
                            "inherited_handle_close_failed"
                        ) from error
        if WINTER_GATE_JOB_ENV in os.environ:
            raise StructuredOutputError("missing_inherited_handle_in_gate_job")
        fd = os.open(
            output_path,
            os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_BINARY,
            0o600,
        )
        return cls(fd)

    def write(self, document: dict[str, object]) -> None:
        if self._fd is None:
            raise StructuredOutputError("sink_closed")
        if self._written:
            raise StructuredOutputError("document_already_written")
        _write_fd(self._fd, encode_json_document(document))
        self._written = True

    def close(self) -> None:
        if self._fd is None:
            return
        fd, self._fd = self._fd, None
        os.close(fd)

    def __enter__(self) -> "StructuredJsonSink":
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.close()


def write_json_document(document: dict[str, object], output_path: str) -> None:
    with StructuredJsonSink.claim(output_path) as sink:
        sink.write(document)
```

- [ ] **Step 3: Run the writer GREEN and commit**

```powershell
python -m unittest `
  Tools.test_winter_narrative_capabilities.WinterStructuredJsonWriterTests `
  -v
if ($LASTEXITCODE -ne 0) { throw 'Structured JSON writer GREEN failed.' }
@'
import unittest

module_loader = unittest.TestLoader()
module_suite = module_loader.loadTestsFromName(
    "Tools.test_winter_narrative_capabilities"
)
repository_loader = unittest.TestLoader()
repository_suite = repository_loader.discover(start_dir="Tools")
if module_loader.errors != [] or repository_loader.errors != []:
    raise SystemExit(
        "static unittest loading errors: "
        + repr(module_loader.errors + repository_loader.errors)
    )
counts = (module_suite.countTestCases(), repository_suite.countTestCases())
expected = (5, 344)
if counts != expected:
    raise SystemExit(f"unexpected static unittest counts: {counts!r}")
print({"capability": counts[0], "discovery": counts[1], "loader_errors": 0})
'@ | python -
if ($LASTEXITCODE -ne 0) { throw 'Writer static test catalog failed.' }
git diff --cached --quiet
if ($LASTEXITCODE -ne 0) { throw 'Writer slice started with a nonempty index.' }
git add -- Tools/winter_narrative_json.py Tools/test_winter_narrative_capabilities.py
$writerPaths = [string[]]@(git diff --cached --name-only)
$expectedWriterPaths = [string[]]@(
  'Tools/test_winter_narrative_capabilities.py',
  'Tools/winter_narrative_json.py'
)
if (@(Compare-Object ($expectedWriterPaths | Sort-Object) ($writerPaths | Sort-Object)).Count -ne 0) {
  throw "Unexpected writer slice paths: $($writerPaths -join ', ')"
}
git diff --cached --check
if ($LASTEXITCODE -ne 0) { throw 'Writer slice staged diff check failed.' }
git commit -m "test: specify winter narrative json transport"
if ($LASTEXITCODE -ne 0) { throw 'Writer slice commit failed.' }
$subject = (git log -1 --pretty=%s).Trim()
if ($subject -cne 'test: specify winter narrative json transport') {
  throw "Unexpected writer commit subject: $subject"
}
$writerCommitPaths = [string[]]@(git diff-tree --no-commit-id --name-only -r HEAD)
if (@(Compare-Object ($expectedWriterPaths | Sort-Object) ($writerCommitPaths | Sort-Object)).Count -ne 0) {
  throw "Unexpected writer commit paths: $($writerCommitPaths -join ', ')"
}
if (git status --short) { throw 'Writer commit left a dirty worktree.' }
```

Expected focused GREEN: `Ran 5 tests`, `OK`, exit 0. Expected static catalog:
capability module 5 methods, `Tools` discovery 344 methods, and both loader error
lists exactly empty. No cumulative module or repository test body runs at this
intermediate SHA. The exact UTF-8/UTF-16/depth/number limits and deterministic
key order pass; standalone collision is create-new; the reservation marker is
replaced only after seek-to-zero plus truncate; the inherited flag is observed
as zero; malformed, missing, mismatched, and unwritable handles fail without
fallback; and the unwritable file remains byte-for-byte unchanged. No scanner
or gate behavior changes yet.

**Asset audit:** Tooling only. Art, music, SFX, portrait, animation, UI, font, old-game, shipping source, and package size are unchanged.

---

## Task 2: Add the real capability producer and its first fail-closed project boundary

**Files:**

- Create: Tools/winter_narrative_inputs.txt
- Create: Tools/winter_narrative_inputs.py
- Create: Tools/check_winter_narrative_capabilities.py
- Modify: Tools/test_winter_narrative_capabilities.py
- Modify: Tools/test_winter_interlude_gate.py
- Modify: Tools/Run-WinterInterludeGate.ps1

The capability producer claims its structured output before importing or running
any probe. Its children receive neither WINTER_GATE_STRUCTURED_OUTPUT_HANDLE nor
WINTER_GATE_JOB_NAME. Every Boolean is the result of an exact named unittest
invocation with a nonzero expected test count; no code path assigns readiness
from file existence or a literal success constant. The same slice freezes the
current direct narrative inputs behind one immutable Python interface and one
opaque native lease; only capability, canon, and portrait opt into that
inventory seam.

- [ ] **Step 1: Specify the immutable inventory and capability catalog, then take the inventory RED**

Add these imports to `Tools/test_winter_narrative_capabilities.py`:

```python
import hashlib
import shutil
from unittest import mock
```

Immediately after the existing writer constants, add:

```python
INPUTS = ROOT / "Tools" / "winter_narrative_inputs.txt"
INPUTS_MODULE = ROOT / "Tools" / "winter_narrative_inputs.py"


def _inventory_text(
    rpy_names: tuple[str, ...],
    portrait_names: tuple[str, ...],
) -> str:
    ordered_rpy = tuple(sorted(rpy_names))
    ordered_portraits = tuple(sorted(portrait_names))
    lines = [
        "WINTER_NARRATIVE_INPUTS_V1"
        f"\tR={len(ordered_rpy)}\tP={len(ordered_portraits)}"
    ]
    lines.extend(f"R\tgame/{name}" for name in ordered_rpy)
    lines.extend(f"P\t{name}" for name in ordered_portraits)
    return "\n".join(lines) + "\n"


def _write_test_inventory(project: Path) -> Path:
    game = project / "game"
    images = game / "images"
    rpy_names = tuple(
        sorted(
            path.name
            for path in game.iterdir()
            if path.is_file() and path.suffix.lower() == ".rpy"
        )
    )
    portrait_names = tuple(
        sorted(
            path.name
            for path in images.iterdir()
            if path.is_file() and path.suffix.lower() == ".png"
        )
    ) if images.is_dir() else ()
    target = project / "Tools" / "winter_narrative_inputs.txt"
    target.write_text(
        _inventory_text(rpy_names, portrait_names),
        encoding="utf-8",
        newline="\n",
    )
    return target
```

Append these exact classes:

```python
class WinterCapabilityProbeEnvironmentTests(unittest.TestCase):
    def test_probe_child_has_no_gate_output_authority(self) -> None:
        self.assertNotIn(HANDLE_ENV, os.environ)
        self.assertNotIn(JOB_ENV, os.environ)


class WinterNarrativeCapabilityCheckerTests(unittest.TestCase):
    def test_checker_module_exists_with_named_probe_catalog(self) -> None:
        self.assertTrue(INPUTS_MODULE.is_file())
        self.assertTrue(INPUTS.is_file())
        self.assertEqual(INPUTS.stat().st_size, 5456)
        self.assertEqual(
            hashlib.sha256(INPUTS.read_bytes()).hexdigest().upper(),
            "55776C4387F7648A5713EE87D929F3C7D6BC310811F60490DDD390FED240A9CF",
        )
        from Tools.winter_narrative_inputs import (
            WinterNarrativeInputError,
            validated_winter_narrative_inputs,
        )

        with validated_winter_narrative_inputs(INPUTS, ROOT) as inventory:
            self.assertIs(type(inventory.rpy_files), tuple)
            self.assertIs(type(inventory.portrait_files), tuple)
            self.assertEqual(len(inventory.rpy_files), 57)
            self.assertEqual(len(inventory.portrait_files), 197)
            self.assertEqual(
                tuple(path.name for path in inventory.rpy_files),
                tuple(
                    sorted(
                        path.name
                        for path in (ROOT / "game").iterdir()
                        if path.is_file() and path.suffix.lower() == ".rpy"
                    )
                ),
            )
            self.assertEqual(
                tuple(path.name for path in inventory.portrait_files),
                tuple(
                    sorted(
                        path.name
                        for path in (ROOT / "game" / "images").iterdir()
                        if path.is_file() and path.suffix.lower() == ".png"
                    )
                ),
            )
            with self.assertRaises(AttributeError):
                inventory.rpy_files = ()

        with tempfile.TemporaryDirectory(
            prefix="winter-inventory-contract-"
        ) as raw:
            project = Path(raw)
            tools = project / "Tools"
            game = project / "game"
            images = game / "images"
            tools.mkdir()
            images.mkdir(parents=True)
            for name in ("a.rpy", "b.rpy"):
                (game / name).write_text(
                    f"# {name}\n",
                    encoding="utf-8",
                    newline="\n",
                )
            (images / "portrait.png").write_bytes(b"portrait")
            inventory_path = tools / "winter_narrative_inputs.txt"
            valid_text = _inventory_text(
                ("a.rpy", "b.rpy"),
                ("portrait.png",),
            )
            valid_bytes = valid_text.encode("utf-8")
            inventory_path.write_bytes(valid_bytes)
            with validated_winter_narrative_inputs(
                inventory_path,
                project,
            ) as parsed:
                self.assertEqual(
                    parsed.rpy_files,
                    (game / "a.rpy", game / "b.rpy"),
                )
                self.assertEqual(
                    parsed.portrait_files,
                    (images / "portrait.png",),
                )

            inventory_path.write_bytes(valid_bytes.replace(b"\n", b"\r\n"))
            with validated_winter_narrative_inputs(
                inventory_path,
                project,
            ) as parsed_crlf:
                self.assertEqual(len(parsed_crlf.rpy_files), 2)

            invalid_payloads = {
                "bom": b"\xef\xbb\xbf" + valid_bytes,
                "standalone-cr": valid_bytes.replace(b"\n", b"\r", 1),
                "missing-terminal-lf": valid_bytes[:-1],
                "unordered": (
                    "WINTER_NARRATIVE_INPUTS_V1\tR=2\tP=1\n"
                    "R\tgame/b.rpy\n"
                    "R\tgame/a.rpy\n"
                    "P\tportrait.png\n"
                ).encode("utf-8"),
                "duplicate": (
                    "WINTER_NARRATIVE_INPUTS_V1\tR=2\tP=1\n"
                    "R\tgame/a.rpy\n"
                    "R\tgame/a.rpy\n"
                    "P\tportrait.png\n"
                ).encode("utf-8"),
                "count-mismatch": valid_bytes.replace(b"R=2", b"R=3"),
                "rpy-bound": b"WINTER_NARRATIVE_INPUTS_V1\tR=129\tP=0\n",
                "portrait-bound": b"WINTER_NARRATIVE_INPUTS_V1\tR=1\tP=513\n",
                "uppercase": valid_bytes.replace(b"game/a.rpy", b"game/A.rpy"),
                "invalid-utf8": valid_bytes + b"\x80",
            }
            for name, payload in invalid_payloads.items():
                with self.subTest(inventory_mutation=name):
                    inventory_path.write_bytes(payload)
                    with self.assertRaises(WinterNarrativeInputError):
                        with validated_winter_narrative_inputs(
                            inventory_path,
                            project,
                        ) as rejected:
                            self.assertIsNotNone(rejected)

            inventory_path.write_bytes(valid_bytes)
            with self.assertRaises(WinterNarrativeInputError):
                with validated_winter_narrative_inputs(
                    inventory_path,
                    project,
                ) as stable_inventory:
                    self.assertEqual(len(stable_inventory.rpy_files), 2)
                    inventory_path.write_bytes(
                        valid_bytes.replace(b"R=2", b"R=3")
                    )
            inventory_path.write_bytes(valid_bytes)

            additions = (
                game / "new_input.rpy",
                images / "new_portrait.png",
            )
            for addition in additions:
                with self.subTest(stable_member=addition.name):
                    with self.assertRaises(WinterNarrativeInputError):
                        with validated_winter_narrative_inputs(
                            inventory_path,
                            project,
                        ) as stable_inventory:
                            self.assertEqual(len(stable_inventory.rpy_files), 2)
                            addition.write_bytes(b"temporary")
                    addition.unlink()

        checker = ROOT / "Tools" / "check_winter_narrative_capabilities.py"
        self.assertTrue(checker.is_file())
        source = checker.read_text(encoding="utf-8")
        self.assertEqual(
            source.count("CAPABILITY_TEST_IDS: dict[str, tuple[str, ...]] = {"),
            1,
        )
        self.assertEqual(
            source.count("BATCH_CONTRACT_TEST_IDS: tuple[str, ...] = ("),
            1,
        )
        self.assertEqual(
            source.count("FINAL_CONTRACT_TEST_IDS: tuple[str, ...] = ("),
            1,
        )
        self.assertEqual(source.count("StructuredJsonSink.claim("), 1)
        self.assertNotIn('"ready": True', source)
        self.assertNotIn("CapabilityLinkageMutationTests", source)

    def test_batch_and_final_documents_are_exact_and_phase_sensitive(self) -> None:
        from Tools.check_winter_narrative_capabilities import (
            BATCH_CONTRACT_TEST_IDS,
            CAPABILITY_TEST_IDS,
            FINAL_CONTRACT_TEST_IDS,
            build_document,
            evaluate_capabilities,
        )

        observed: list[tuple[str, ...]] = []

        def batch_runner(test_ids: tuple[str, ...]) -> bool:
            observed.append(test_ids)
            return test_ids != FINAL_CONTRACT_TEST_IDS

        batch = evaluate_capabilities("batch", batch_runner)
        self.assertEqual(
            observed,
            list(CAPABILITY_TEST_IDS.values())
            + [BATCH_CONTRACT_TEST_IDS, FINAL_CONTRACT_TEST_IDS],
        )
        batch_document = build_document("batch", batch)
        self.assertEqual(
            set(batch_document),
            {"schema_version", "tool", "phase", "ready", "capabilities"},
        )
        self.assertIs(type(batch_document["schema_version"]), int)
        self.assertEqual(batch_document["schema_version"], 1)
        self.assertEqual(
            batch_document["tool"],
            "winter_narrative_capabilities",
        )
        self.assertEqual(batch_document["phase"], "batch")
        self.assertIs(batch_document["ready"], True)
        self.assertIs(batch["final_contracts"], False)
        self.assertEqual(
            set(batch),
            {
                "canon_json",
                "portrait_json",
                "overlap_json",
                "show_before_json",
                "nested_quote_json",
                "batch_contracts",
                "final_contracts",
            },
        )
        for name, ids in (
            list(CAPABILITY_TEST_IDS.items())
            + [
                ("batch_contracts", BATCH_CONTRACT_TEST_IDS),
                ("final_contracts", FINAL_CONTRACT_TEST_IDS),
            ]
        ):
            with self.subTest(name=name):
                self.assertGreater(len(ids), 0)
                self.assertEqual(len(ids), len(set(ids)))
                self.assertTrue(
                    all(
                        isinstance(test_id, str)
                        and test_id.startswith("Tools.test_")
                        and ".test_" in test_id
                        for test_id in ids
                    )
                )
                self.assertFalse(
                    any("test_public_gate_" in test_id for test_id in ids)
                )

        final_false = build_document(
            "final",
            evaluate_capabilities("final", batch_runner),
        )
        self.assertIs(final_false["ready"], False)

        def all_green(test_ids: tuple[str, ...]) -> bool:
            return bool(test_ids)

        final_true = build_document(
            "final",
            evaluate_capabilities("final", all_green),
        )
        self.assertIs(final_true["ready"], True)

    def test_cli_claims_before_probes_and_writes_not_ready_evidence(self) -> None:
        from Tools.check_winter_narrative_capabilities import main

        with tempfile.TemporaryDirectory(
            prefix="winter-capability-cli-"
        ) as raw:
            root = Path(raw)
            occupied = root / "occupied.json"
            occupied.write_bytes(b"sentinel")
            called = False

            def forbidden_runner(test_ids: tuple[str, ...]) -> bool:
                nonlocal called
                called = True
                return True

            exit_code = main(
                [
                    "--phase",
                    "batch",
                    "--format",
                    "json",
                    "--output",
                    str(occupied),
                ],
                forbidden_runner,
            )
            self.assertEqual(exit_code, 2)
            self.assertFalse(called)
            self.assertEqual(occupied.read_bytes(), b"sentinel")

            output = root / "not-ready.json"

            def one_failure(test_ids: tuple[str, ...]) -> bool:
                return test_ids[0].find("CanonJsonProducerTests") < 0

            exit_code = main(
                [
                    "--phase",
                    "batch",
                    "--format",
                    "json",
                    "--output",
                    str(output),
                ],
                one_failure,
            )
            self.assertEqual(exit_code, 1)
            document = json.loads(output.read_text(encoding="utf-8"))
            self.assertIs(document["ready"], False)
            self.assertIs(document["capabilities"]["canon_json"], False)
            self.assertIs(document["capabilities"]["batch_contracts"], True)

            class CloseFailureSink:
                def __init__(self) -> None:
                    self.document: dict[str, object] | None = None
                    self.close_calls = 0

                def write(self, document: dict[str, object]) -> None:
                    self.document = document

                def close(self) -> None:
                    self.close_calls += 1
                    raise OSError("forced capability sink close failure")

            close_sink = CloseFailureSink()
            close_output = root / "close-failure.json"
            with mock.patch(
                "Tools.check_winter_narrative_capabilities.StructuredJsonSink.claim",
                return_value=close_sink,
            ):
                try:
                    close_exit = main(
                        [
                            "--phase",
                            "batch",
                            "--format",
                            "json",
                            "--output",
                            str(close_output),
                        ],
                        lambda test_ids: bool(test_ids),
                    )
                except OSError:
                    close_exit = -1
            self.assertEqual(close_exit, 2)
            self.assertEqual(close_sink.close_calls, 2)
            self.assertIsNotNone(close_sink.document)

    def test_probe_runner_scrubs_gate_handle_and_job_environment(self) -> None:
        from Tools.check_winter_narrative_capabilities import run_test_ids

        probe = (
            "Tools.test_winter_narrative_capabilities."
            "WinterCapabilityProbeEnvironmentTests."
            "test_probe_child_has_no_gate_output_authority"
        )
        with mock.patch.dict(
            os.environ,
            {
                HANDLE_ENV: "999999",
                JOB_ENV: "Local\\WinterGate-hostile-parent",
            },
            clear=False,
        ):
            self.assertTrue(run_test_ids((probe,)))
```

Run only the first missing deep-module behavior RED:

```powershell
$red = & python -m unittest Tools.test_winter_narrative_capabilities.WinterNarrativeCapabilityCheckerTests.test_checker_module_exists_with_named_probe_catalog -v 2>&1
$redExit = $LASTEXITCODE
$red | Set-Content -LiteralPath .superpowers/sdd/task8-input-inventory-red.txt -Encoding UTF8
if ($redExit -eq 0) { throw 'Input inventory RED unexpectedly passed.' }
$joined = $red -join [Environment]::NewLine
if ($joined -notmatch 'Ran 1 test' -or
    $joined -notmatch 'FAILED \(failures=1\)' -or
    $joined -match '(?m)^ERROR:') {
  throw 'Input inventory RED did not fail only on the absent deep module.'
}
```

Expected RED: Ran 1 test, one assertion failure because
`Tools/winter_narrative_inputs.py` is absent, and no import, syntax, setup, or
environment error.

- [ ] **Step 2: Create the tracked literal inventory and deep input module**

Create `Tools/winter_narrative_inputs.txt` with exactly these 255 LF-terminated lines. The file is strict UTF-8 without BOM; do not generate or sort it during implementation.

```text
WINTER_NARRATIVE_INPUTS_V1	R=57	P=197
R	game/attr_system.rpy
R	game/audio_config.rpy
R	game/audio_safe.rpy
R	game/balance.rpy
R	game/changelog.rpy
R	game/chapter1_deepening.rpy
R	game/chapter1_expansion.rpy
R	game/chapter2.rpy
R	game/chapter2_expansion.rpy
R	game/chapter3.rpy
R	game/chapter3_expansion.rpy
R	game/chapter4.rpy
R	game/chapter4_expansion.rpy
R	game/chapter4_prince.rpy
R	game/chapter5.rpy
R	game/chapter5_expansion.rpy
R	game/chapters_deepening.rpy
R	game/char_helpers.rpy
R	game/characters.rpy
R	game/cinematics.rpy
R	game/combat.rpy
R	game/companions.rpy
R	game/courage.rpy
R	game/crafting.rpy
R	game/crisis.rpy
R	game/difficulty.rpy
R	game/effects.rpy
R	game/endings_expansion.rpy
R	game/extras.rpy
R	game/gallery.rpy
R	game/governance.rpy
R	game/governance_winter_interlude.rpy
R	game/gui.rpy
R	game/images_def.rpy
R	game/interludes.rpy
R	game/inventory.rpy
R	game/new_run.rpy
R	game/northern_expansion.rpy
R	game/npc_depth.rpy
R	game/npc_sidelines.rpy
R	game/options.rpy
R	game/prologue.rpy
R	game/prologue_deepening.rpy
R	game/pv.rpy
R	game/random_events.rpy
R	game/random_events_expansion.rpy
R	game/random_events_new.rpy
R	game/replay.rpy
R	game/save_compat.rpy
R	game/screens.rpy
R	game/screens_custom.rpy
R	game/script.rpy
R	game/soft_check.rpy
R	game/southern_expansion.rpy
R	game/test_game.rpy
R	game/voice_config.rpy
R	game/weather.rpy
P	aldric.png
P	aldric_angry.png
P	aldric_happy.png
P	aldric_sad.png
P	assassin_char.png
P	assassin_char_angry.png
P	assassin_char_happy.png
P	assassin_char_sad.png
P	baron.png
P	baron_angry.png
P	baron_happy.png
P	baron_sad.png
P	beggar.png
P	bertrand.png
P	bertrand_angry.png
P	bertrand_happy.png
P	bertrand_sad.png
P	bishop.png
P	bishop_angry.png
P	bishop_happy.png
P	bishop_sad.png
P	blacksmith_wife.png
P	blacksmith_wife_angry.png
P	blacksmith_wife_happy.png
P	blacksmith_wife_sad.png
P	bully_kid.png
P	bully_kid_angry.png
P	bully_kid_happy.png
P	bully_kid_sad.png
P	captain.png
P	captain_angry.png
P	captain_happy.png
P	captain_sad.png
P	chancellor.png
P	chen_captain.png
P	corsair.png
P	corsair_angry.png
P	corsair_happy.png
P	corsair_intimate.png
P	corsair_sad.png
P	count_grey.png
P	count_grey_angry.png
P	count_grey_happy.png
P	count_grey_sad.png
P	countess_hilda.png
P	countess_hilda_angry.png
P	countess_hilda_happy.png
P	countess_hilda_sad.png
P	countess_stein.png
P	countess_stein_angry.png
P	countess_stein_happy.png
P	countess_stein_sad.png
P	court_herald.png
P	court_poet.png
P	dockhand.png
P	edmund.png
P	edmund_masked.png
P	elena.png
P	elena_angry.png
P	elena_happy.png
P	elena_intimate.png
P	elena_sad.png
P	farmer_rep.png
P	farmer_rep_angry.png
P	farmer_rep_happy.png
P	farmer_rep_sad.png
P	father.png
P	father_angry.png
P	father_happy.png
P	father_sad.png
P	friend_marcus.png
P	friend_marcus_angry.png
P	friend_marcus_happy.png
P	friend_marcus_sad.png
P	guild_master.png
P	harbor_master.png
P	healer.png
P	healer_angry.png
P	healer_happy.png
P	healer_sad.png
P	herald.png
P	herbalist_vera.png
P	ingrid.png
P	ingrid_angry.png
P	ingrid_happy.png
P	ingrid_sad.png
P	king_aldwin.png
P	knight_commander.png
P	lily_master.png
P	lily_master_angry.png
P	lily_master_happy.png
P	lily_master_sad.png
P	lily_root.png
P	logo.png
P	masked_man.png
P	merchant_guild.png
P	merchant_guild_angry.png
P	merchant_guild_happy.png
P	merchant_guild_sad.png
P	merchant_karl.png
P	merchant_karl_angry.png
P	merchant_karl_happy.png
P	merchant_karl_sad.png
P	mother.png
P	mother_angry.png
P	mother_happy.png
P	mother_sad.png
P	mysterious_lady.png
P	noble_lady.png
P	noble_lady_angry.png
P	noble_lady_happy.png
P	noble_lady_sad.png
P	noble_werner.png
P	noble_werner_angry.png
P	noble_werner_happy.png
P	noble_werner_sad.png
P	old_guard.png
P	old_guard_angry.png
P	old_guard_happy.png
P	old_guard_sad.png
P	old_salt.png
P	old_servant_ch4.png
P	old_woman.png
P	player_char.png
P	player_char_angry.png
P	player_char_happy.png
P	player_char_sad.png
P	player_char_scarred.png
P	player_char_scarred_angry.png
P	player_char_scarred_happy.png
P	player_char_scarred_sad.png
P	player_child.png
P	player_child_angry.png
P	player_child_happy.png
P	player_child_sad.png
P	player_teen.png
P	player_teen_angry.png
P	player_teen_happy.png
P	player_teen_sad.png
P	player_young.png
P	player_young_angry.png
P	player_young_happy.png
P	player_young_sad.png
P	priest_thomas.png
P	priest_thomas_angry.png
P	priest_thomas_happy.png
P	priest_thomas_sad.png
P	prince.png
P	prince_angry.png
P	prince_happy.png
P	prince_sad.png
P	protocol_officer.png
P	queen.png
P	queen_angry.png
P	queen_envoy.png
P	queen_happy.png
P	queen_sad.png
P	rival_duke.png
P	royal_admiral.png
P	royal_guard.png
P	sea_dog.png
P	servant_generic.png
P	servant_generic_angry.png
P	servant_generic_happy.png
P	servant_generic_sad.png
P	servant_marta.png
P	servant_marta_angry.png
P	servant_marta_happy.png
P	servant_marta_sad.png
P	ship_boy.png
P	soldier_generic.png
P	soldier_generic_angry.png
P	soldier_generic_happy.png
P	soldier_generic_sad.png
P	stable_boy.png
P	storyteller.png
P	storyteller_angry.png
P	storyteller_happy.png
P	storyteller_sad.png
P	tavern_keeper.png
P	tax_collector.png
P	tax_collector_angry.png
P	tax_collector_happy.png
P	tax_collector_sad.png
P	tournament_herald.png
P	tutor.png
P	tutor_angry.png
P	tutor_happy.png
P	tutor_sad.png
P	village_elder.png
P	village_elder_angry.png
P	village_elder_happy.png
P	village_elder_sad.png
P	viscount_wells.png
P	viscount_wells_angry.png
P	viscount_wells_happy.png
P	viscount_wells_sad.png
```


Create Tools/winter_narrative_inputs.py with exactly:

```python
from __future__ import annotations

import os
import re
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path
from typing import NamedTuple


__all__ = (
    "WinterNarrativeInputError",
    "WinterNarrativeInputs",
    "validated_winter_narrative_inputs",
)

_HEADER = re.compile(
    r"WINTER_NARRATIVE_INPUTS_V1\tR=([0-9]+)\tP=([0-9]+)"
)
_RPY_ENTRY = re.compile(r"R\t(game/[a-z0-9_]+[.]rpy)")
_PORTRAIT_ENTRY = re.compile(r"P\t([a-z0-9_]+[.]png)")
_MAX_INVENTORY_BYTES = 65536
_MAX_RPY_FILES = 128
_MAX_PORTRAIT_FILES = 512


class WinterNarrativeInputError(ValueError):
    """The pinned winter narrative input inventory is invalid or unstable."""


class WinterNarrativeInputs(NamedTuple):
    rpy_files: tuple[Path, ...]
    portrait_files: tuple[Path, ...]


def _fail(message: str) -> WinterNarrativeInputError:
    return WinterNarrativeInputError(message)


def _read_inventory(path: Path) -> tuple[bytes, tuple[str, ...], tuple[str, ...]]:
    try:
        raw = path.read_bytes()
    except OSError as error:
        raise _fail(f"cannot read narrative inventory: {error}") from error
    if not raw or len(raw) > _MAX_INVENTORY_BYTES:
        raise _fail("narrative inventory byte count is outside bounds")
    if raw.startswith(b"\xef\xbb\xbf"):
        raise _fail("narrative inventory must not contain a UTF-8 BOM")
    try:
        text = raw.decode("utf-8", errors="strict")
    except UnicodeError as error:
        raise _fail("narrative inventory is not strict UTF-8") from error
    normalized = text.replace("\r\n", "\n")
    if "\r" in normalized:
        raise _fail("narrative inventory contains a standalone CR")
    if not normalized.endswith("\n"):
        raise _fail("narrative inventory must end with LF")
    lines = normalized[:-1].split("\n")
    if not lines or any(line == "" for line in lines):
        raise _fail("narrative inventory contains an empty line")
    header = _HEADER.fullmatch(lines[0])
    if header is None:
        raise _fail("narrative inventory header is invalid")
    rpy_count = int(header.group(1))
    portrait_count = int(header.group(2))
    if not 1 <= rpy_count <= _MAX_RPY_FILES:
        raise _fail("narrative R count is outside bounds")
    if not 0 <= portrait_count <= _MAX_PORTRAIT_FILES:
        raise _fail("narrative P count is outside bounds")
    if len(lines) != 1 + rpy_count + portrait_count:
        raise _fail("narrative inventory count does not match its entries")

    rpy_lines = lines[1 : 1 + rpy_count]
    portrait_lines = lines[1 + rpy_count :]
    rpy_entries: list[str] = []
    portrait_entries: list[str] = []
    for line in rpy_lines:
        match = _RPY_ENTRY.fullmatch(line)
        if match is None:
            raise _fail("narrative inventory contains an invalid R entry")
        rpy_entries.append(match.group(1))
    for line in portrait_lines:
        match = _PORTRAIT_ENTRY.fullmatch(line)
        if match is None:
            raise _fail("narrative inventory contains an invalid P entry")
        portrait_entries.append(match.group(1))

    if rpy_entries != sorted(rpy_entries) or len(rpy_entries) != len(
        set(rpy_entries)
    ):
        raise _fail("narrative R entries must be unique Ordinal order")
    if portrait_entries != sorted(portrait_entries) or len(
        portrait_entries
    ) != len(set(portrait_entries)):
        raise _fail("narrative P entries must be unique Ordinal order")
    return raw, tuple(rpy_entries), tuple(portrait_entries)


def _direct_members(directory: Path, suffix: str) -> frozenset[str]:
    try:
        children = tuple(directory.iterdir())
    except OSError as error:
        raise _fail(f"cannot enumerate narrative input directory: {error}") from error
    members: set[str] = set()
    for child in children:
        if child.suffix.lower() != suffix:
            continue
        try:
            regular = child.is_file()
            symbolic = child.is_symlink()
        except OSError as error:
            raise _fail(f"cannot inspect narrative input: {error}") from error
        if not regular or symbolic:
            raise _fail("narrative input members must be regular non-symlink files")
        members.add(child.name)
    return frozenset(members)


def _membership_snapshot(project: Path) -> tuple[frozenset[str], frozenset[str]]:
    return (
        _direct_members(project / "game", ".rpy"),
        _direct_members(project / "game" / "images", ".png"),
    )


def _assert_exact_membership(
    project: Path,
    rpy_entries: tuple[str, ...],
    portrait_entries: tuple[str, ...],
) -> None:
    actual_rpy, actual_portraits = _membership_snapshot(project)
    expected_rpy = frozenset(Path(entry).name for entry in rpy_entries)
    expected_portraits = frozenset(portrait_entries)
    if actual_rpy != expected_rpy or actual_portraits != expected_portraits:
        raise _fail("narrative input membership differs from the pinned inventory")


@contextmanager
def validated_winter_narrative_inputs(
    inputs_path: str | os.PathLike[str],
    project_root: str | os.PathLike[str],
) -> Iterator[WinterNarrativeInputs]:
    inputs = Path(inputs_path)
    project = Path(project_root)
    if not inputs.is_absolute() or not project.is_absolute():
        raise _fail("narrative inventory and project root must be absolute")
    expected_inputs = project / "Tools" / "winter_narrative_inputs.txt"
    if inputs != expected_inputs:
        raise _fail("narrative inventory must be the tracked project input path")
    if inputs.is_symlink():
        raise _fail("narrative inventory must not be a symlink")

    original, rpy_entries, portrait_entries = _read_inventory(inputs)
    _assert_exact_membership(project, rpy_entries, portrait_entries)
    inventory = WinterNarrativeInputs(
        tuple(project / entry for entry in rpy_entries),
        tuple(project / "game" / "images" / entry for entry in portrait_entries),
    )
    try:
        yield inventory
    finally:
        current, current_rpy, current_portraits = _read_inventory(inputs)
        if current != original:
            raise _fail("narrative inventory bytes changed during the scan")
        if current_rpy != rpy_entries or current_portraits != portrait_entries:
            raise _fail("narrative inventory entries changed during the scan")
        _assert_exact_membership(project, rpy_entries, portrait_entries)
```

Run the same named test again after creating both inventory files and before
creating the capability checker:

```powershell
$red = & python -m unittest Tools.test_winter_narrative_capabilities.WinterNarrativeCapabilityCheckerTests.test_checker_module_exists_with_named_probe_catalog -v 2>&1
$redExit = $LASTEXITCODE
$red | Set-Content -LiteralPath .superpowers/sdd/task8-capability-checker-red.txt -Encoding UTF8
if ($redExit -eq 0) { throw 'Capability checker RED unexpectedly passed.' }
$joined = $red -join [Environment]::NewLine
if ($joined -notmatch 'Ran 1 test' -or
    $joined -notmatch 'FAILED \(failures=1\)' -or
    $joined -match '(?m)^ERROR:') {
  throw 'Capability checker RED did not fail only on the absent checker.'
}
```

Expected second RED: Ran 1 test, one assertion failure because
Tools/check_winter_narrative_capabilities.py is absent. The inventory parser,
immutable tuple, CRLF normalization, malformed-input matrix, and both stable
membership mutations are GREEN inside that same method.

- [ ] **Step 3: Specify and implement the opaque native inventory lease**

In Tools/test_winter_interlude_gate.py insert this probe beside the existing
native executable-access probe:

```python
NATIVE_INVENTORY_LEASE_PROBE_SOURCE = r'''
using System;

internal static class NativeInventoryLeaseProbe
{
    public static int Main(string[] arguments)
    {
        if (arguments.Length != 3)
        {
            Console.Error.WriteLine(
                "executable, inventory, and project are required");
            return 2;
        }
        try
        {
            WinterGate.PathIdentity projectIdentity =
                WinterGate.Native.GetPathIdentity(
                    arguments[2],
                    WinterGate.PathKind.Directory,
                    true);
            using (WinterGate.Native.StepDependencyLease lease =
                WinterGate.Native.AcquireStepDependencyLease(
                    arguments[0],
                    new string[0],
                    arguments[1],
                    projectIdentity))
            {
                lease.AssertStable();
            }
            return 0;
        }
        catch (Exception exception)
        {
            Console.Error.WriteLine(exception.ToString());
            return 91;
        }
    }
}
'''


def compile_native_inventory_lease_probe(
    build: Path,
    native_source: str,
) -> Path:
    build.mkdir(parents=True)
    native_cs = build / "WinterGate.Native.cs"
    native_dll = build / "WinterGate.Native.dll"
    probe_cs = build / "NativeInventoryLeaseProbe.cs"
    probe_exe = build / "NativeInventoryLeaseProbe.exe"
    native_cs.write_text(native_source, encoding="utf-8")
    probe_cs.write_text(
        NATIVE_INVENTORY_LEASE_PROBE_SOURCE,
        encoding="utf-8",
    )
    for arguments in (
        ("/target:library", f"/out:{native_dll}", str(native_cs)),
        (
            "/target:exe",
            f"/out:{probe_exe}",
            f"/reference:{native_dll}",
            str(probe_cs),
        ),
    ):
        completed = subprocess.run(
            [str(framework_csc()), "/nologo", *arguments],
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=60,
            check=False,
        )
        if completed.returncode != 0:
            raise AssertionError(
                "native inventory lease probe compilation failed:\n"
                + completed.stdout
            )
    return probe_exe


def assert_native_inventory_lease_source_contract(
    case: unittest.TestCase,
    source: str,
) -> None:
    signature = (
        "public static StepDependencyLease AcquireStepDependencyLease(\n"
        "        string executable,\n"
        "        string[] fixedRequiredFiles,\n"
        "        string inventoryPath,\n"
        "        PathIdentity projectIdentity)"
    )
    case.assertEqual(source.count(signature), 1)
    overload_start = source.index(signature)
    overload_end = source.index(
        "public static string ReadVerifiedUtf8TextFile(",
        overload_start,
    )
    overload = source[overload_start:overload_end]
    helpers_start = source.index(
        "private static void AssertStepDependencyProjectStable("
    )
    helpers_end = source.index(
        "private static StepDependencyFile AcquireStepDependencyFile(",
        helpers_start,
    )
    helpers = source[helpers_start:helpers_end]
    case.assertIn(
        "StepDependencyFile inventoryFile =\n"
        "                AcquireUniqueStepDependencyFile(\n"
        "                    inventoryPath,\n"
        "                    false,\n"
        "                    acquiredByPath,\n"
        "                    acquiredRequiredFiles);",
        overload,
    )
    case.assertIn(
        "string inventoryText = ReadStepDependencyUtf8Text(\n"
        "                inventoryFile,\n"
        "                MaximumNarrativeInventoryBytes);",
        overload,
    )
    case.assertNotIn("ReadVerifiedUtf8TextFile(", overload)
    case.assertIn(
        "index < inventory.RpyRelativePaths.Length;",
        overload,
    )
    case.assertIn(
        "AcquireUniqueStepDependencyFile(\n"
        "                    requiredPath,\n"
        "                    false,\n"
        "                    acquiredByPath,\n"
        "                    acquiredRequiredFiles);",
        overload,
    )
    case.assertIn(
        "new SafeFileHandle(\n"
        "            dependency.ReadHandle,\n"
        "            false)",
        helpers,
    )
    case.assertIn("acquiredFiles.Add(acquired);", helpers)
    case.assertIn("MaximumNarrativeRpyInputs", source)
    case.assertIn("MaximumNarrativePortraitInputs", source)
    case.assertIn("String.CompareOrdinal(previousRpy, value) >= 0", helpers)
    case.assertIn(
        "String.CompareOrdinal(previousPortrait, value) >= 0",
        helpers,
    )
```

Append this complete block to the existing
test_executable_identity_uses_readable_full_chain_api method; do not add a new
test method:

```python
        assert_native_inventory_lease_source_contract(self, source)
        self.assertIn(
            "[Parameter(Position = 7)]\n"
            "        [AllowNull()]\n"
            "        [string]$InventoryPath = $null",
            builder,
        )
        self.assertIn(
            "[WinterGate.Native]::AcquireStepDependencyLease(\n"
            "                    $Executable,\n"
            "                    [string[]]$RequiredFiles.Clone(),\n"
            "                    $InventoryPath,\n"
            "                    $script:ProjectIdentity)",
            builder,
        )

        same_handle_call = (
            "string inventoryText = ReadStepDependencyUtf8Text(\n"
            "                inventoryFile,\n"
            "                MaximumNarrativeInventoryBytes);"
        )
        inventory_retention_call = (
            "StepDependencyFile inventoryFile =\n"
            "                AcquireUniqueStepDependencyFile(\n"
            "                    inventoryPath,\n"
            "                    false,\n"
            "                    acquiredByPath,\n"
            "                    acquiredRequiredFiles);"
        )
        rpy_lease_call = (
            "AcquireUniqueStepDependencyFile(\n"
            "                    requiredPath,\n"
            "                    false,\n"
            "                    acquiredByPath,\n"
            "                    acquiredRequiredFiles);"
        )
        source_mutants = {
            "path-reopen": source.replace(
                same_handle_call,
                (
                    "string inventoryText = ReadVerifiedUtf8TextFile(\n"
                    "                inventoryPath,\n"
                    "                inventoryFile.CreationIdentity,\n"
                    "                MaximumNarrativeInventoryBytes);"
                ),
                1,
            ),
            "inventory-not-retained": source.replace(
                inventory_retention_call,
                (
                    "StepDependencyFile inventoryFile =\n"
                    "                AcquireStepDependencyFile(\n"
                    "                    inventoryPath,\n"
                    "                    false);"
                ),
                1,
            ),
            "rpy-not-leased": source.replace(
                rpy_lease_call,
                (
                    "if (String.IsNullOrEmpty(requiredPath))\n"
                    "                {\n"
                    "                    throw new InvalidDataException(\n"
                    "                        \"empty R path\");\n"
                    "                }"
                ),
                1,
            ),
        }
        for name, mutant in source_mutants.items():
            with self.subTest(native_inventory_mutant=name):
                self.assertNotEqual(source, mutant)
                with self.assertRaises(AssertionError):
                    assert_native_inventory_lease_source_contract(
                        self,
                        mutant,
                    )

        with tempfile.TemporaryDirectory(
            prefix="winter-native-inventory-"
        ) as raw:
            base = Path(raw)
            project = base / "project"
            tools = project / "Tools"
            game = project / "game"
            images = game / "images"
            tools.mkdir(parents=True)
            images.mkdir(parents=True)
            for name in ("a.rpy", "b.rpy"):
                (game / name).write_text(
                    f"# {name}\n",
                    encoding="utf-8",
                    newline="\n",
                )
            (images / "portrait.png").write_bytes(b"portrait")
            inventory = tools / "winter_narrative_inputs.txt"
            valid = (
                "WINTER_NARRATIVE_INPUTS_V1\tR=2\tP=1\n"
                "R\tgame/a.rpy\n"
                "R\tgame/b.rpy\n"
                "P\tportrait.png\n"
            ).encode("utf-8")
            probe = compile_native_inventory_lease_probe(
                base / "build",
                extract_native_source(),
            )

            def invoke_inventory_probe(
                payload: bytes,
            ) -> subprocess.CompletedProcess[str]:
                inventory.write_bytes(payload)
                return subprocess.run(
                    [
                        str(probe),
                        str(probe),
                        str(inventory),
                        str(project),
                    ],
                    cwd=project,
                    stdin=subprocess.DEVNULL,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    encoding="utf-8",
                    errors="replace",
                    timeout=30,
                    check=False,
                )

            accepted = invoke_inventory_probe(valid)
            self.assertEqual(accepted.returncode, 0, accepted.stderr)
            accepted_crlf = invoke_inventory_probe(
                valid.replace(b"\n", b"\r\n")
            )
            self.assertEqual(
                accepted_crlf.returncode,
                0,
                accepted_crlf.stderr,
            )
            invalid_payloads = {
                "bom": b"\xef\xbb\xbf" + valid,
                "standalone-cr": valid.replace(b"\n", b"\r", 1),
                "missing-terminal-lf": valid[:-1],
                "unordered": (
                    "WINTER_NARRATIVE_INPUTS_V1\tR=2\tP=1\n"
                    "R\tgame/b.rpy\n"
                    "R\tgame/a.rpy\n"
                    "P\tportrait.png\n"
                ).encode("utf-8"),
                "duplicate": (
                    "WINTER_NARRATIVE_INPUTS_V1\tR=2\tP=1\n"
                    "R\tgame/a.rpy\n"
                    "R\tgame/a.rpy\n"
                    "P\tportrait.png\n"
                ).encode("utf-8"),
                "count-mismatch": valid.replace(b"R=2", b"R=3"),
                "rpy-lower-bound": (
                    b"WINTER_NARRATIVE_INPUTS_V1\tR=0\tP=0\n"
                ),
                "rpy-upper-bound": (
                    b"WINTER_NARRATIVE_INPUTS_V1\tR=129\tP=0\n"
                ),
                "portrait-upper-bound": (
                    b"WINTER_NARRATIVE_INPUTS_V1\tR=1\tP=513\n"
                ),
                "uppercase": valid.replace(
                    b"game/a.rpy",
                    b"game/A.rpy",
                ),
                "invalid-utf8": valid + b"\x80",
            }
            for name, payload in invalid_payloads.items():
                with self.subTest(native_inventory_payload=name):
                    rejected = invoke_inventory_probe(payload)
                    self.assertEqual(
                        rejected.returncode,
                        91,
                        rejected.stderr,
                    )
```

Run this one-method native RED before changing the gate:

```powershell
$red = & python -m unittest Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_executable_identity_uses_readable_full_chain_api -v 2>&1
$redExit = $LASTEXITCODE
$red | Set-Content -LiteralPath .superpowers/sdd/task8-native-inventory-lease-red.txt -Encoding UTF8
if ($redExit -eq 0) { throw 'Native inventory lease RED unexpectedly passed.' }
$joined = $red -join [Environment]::NewLine
if ($joined -notmatch 'Ran 1 test' -or
    $joined -notmatch 'FAILED \(failures=1\)' -or
    $joined -match '(?m)^ERROR:') {
  throw 'Native inventory lease RED did not fail only on the missing native seam.'
}
```

Expected native RED: Ran 1 test, one assertion failure on the absent
four-argument overload; no compilation, import, or setup error.

In the C# source embedded by Tools/Run-WinterInterludeGate.ps1, add these
constants immediately after ERROR_PATH_NOT_FOUND:

```csharp
        private const int MaximumNarrativeInventoryBytes = 65536;
        private const int MaximumNarrativeRpyInputs = 128;
        private const int MaximumNarrativePortraitInputs = 512;
```

Add this private holder immediately after StepDependencyFile and before
StepDependencyLease:

```csharp
        private sealed class NarrativeInputInventory
        {
            internal readonly string[] RpyRelativePaths;
            internal readonly string[] PortraitNames;

            internal NarrativeInputInventory(
                string[] rpyRelativePaths,
                string[] portraitNames)
            {
                RpyRelativePaths = rpyRelativePaths;
                PortraitNames = portraitNames;
            }
        }
```

Insert this overload immediately after the existing two-argument overload;
leave the old overload byte-for-byte unchanged:

```csharp
    public static StepDependencyLease AcquireStepDependencyLease(
        string executable,
        string[] fixedRequiredFiles,
        string inventoryPath,
        PathIdentity projectIdentity)
    {
        if (fixedRequiredFiles == null)
        {
            throw new ArgumentNullException("fixedRequiredFiles");
        }
        if (projectIdentity == null)
        {
            throw new ArgumentNullException("projectIdentity");
        }

        AssertStepDependencyProjectStable(projectIdentity);
        RequirePlainAbsoluteFilePath(inventoryPath, "inventoryPath");
        string expectedInventoryPath = NormalizeComparableFinalPath(
            Path.Combine(
                projectIdentity.FinalPath,
                "Tools",
                "winter_narrative_inputs.txt"));
        string suppliedInventoryPath =
            NormalizeComparableFinalPath(inventoryPath);
        if (!String.Equals(
            expectedInventoryPath,
            suppliedInventoryPath,
            StringComparison.OrdinalIgnoreCase))
        {
            throw new WinterGatePathIdentityException(
                "path identity: narrative inventory is not the exact tracked " +
                "project input: " + inventoryPath);
        }

        StepDependencyFile executableFile = null;
        List<StepDependencyFile> acquiredRequiredFiles =
            new List<StepDependencyFile>();
        Dictionary<string, StepDependencyFile> acquiredByPath =
            new Dictionary<string, StepDependencyFile>(
                StringComparer.OrdinalIgnoreCase);
        try
        {
            StepDependencyFile inventoryFile =
                AcquireUniqueStepDependencyFile(
                    inventoryPath,
                    false,
                    acquiredByPath,
                    acquiredRequiredFiles);
            string inventoryText = ReadStepDependencyUtf8Text(
                inventoryFile,
                MaximumNarrativeInventoryBytes);
            NarrativeInputInventory inventory =
                ParseNarrativeInputInventory(inventoryText);

            executableFile = AcquireStepDependencyFile(executable, false);
            string firstMissingRequiredFilePath = null;
            for (int index = 0; index < fixedRequiredFiles.Length; index++)
            {
                StepDependencyFile required =
                    AcquireUniqueStepDependencyFile(
                        fixedRequiredFiles[index],
                        true,
                        acquiredByPath,
                        acquiredRequiredFiles);
                if (required == null &&
                    firstMissingRequiredFilePath == null)
                {
                    firstMissingRequiredFilePath =
                        fixedRequiredFiles[index];
                }
            }

            for (int index = 0;
                 index < inventory.RpyRelativePaths.Length;
                 index++)
            {
                string requiredPath = Path.GetFullPath(
                    Path.Combine(
                        projectIdentity.FinalPath,
                        inventory.RpyRelativePaths[index].Replace(
                            '/',
                            Path.DirectorySeparatorChar)));
                AcquireUniqueStepDependencyFile(
                    requiredPath,
                    false,
                    acquiredByPath,
                    acquiredRequiredFiles);
            }

            AssertStepDependencyProjectStable(projectIdentity);
            StepDependencyLease lease = new StepDependencyLease(
                executableFile,
                acquiredRequiredFiles.ToArray(),
                firstMissingRequiredFilePath);
            executableFile = null;
            acquiredRequiredFiles.Clear();
            acquiredByPath.Clear();
            return lease;
        }
        finally
        {
            for (int index = acquiredRequiredFiles.Count - 1;
                 index >= 0;
                 index--)
            {
                acquiredRequiredFiles[index].Dispose();
            }
            if (executableFile != null)
            {
                executableFile.Dispose();
            }
        }
    }
```

Insert these complete helpers immediately before
AcquireStepDependencyFile:

```csharp
    private static void AssertStepDependencyProjectStable(
        PathIdentity projectIdentity)
    {
        if (projectIdentity == null)
        {
            throw new ArgumentNullException("projectIdentity");
        }
        PathIdentity currentIdentity = GetPathIdentity(
            projectIdentity.FinalPath,
            PathKind.Directory,
            true);
        if ((currentIdentity.Attributes & FileAttributes.ReparsePoint) != 0 ||
            !SameStablePath(projectIdentity, currentIdentity))
        {
            throw new WinterGatePathIdentityException(
                "path identity: ProjectRoot changed while narrative " +
                "dependencies were acquired.");
        }
    }

    private static StepDependencyFile AcquireUniqueStepDependencyFile(
        string path,
        bool missingReturnsNull,
        IDictionary<string, StepDependencyFile> acquiredByPath,
        IList<StepDependencyFile> acquiredFiles)
    {
        if (acquiredByPath == null)
        {
            throw new ArgumentNullException("acquiredByPath");
        }
        if (acquiredFiles == null)
        {
            throw new ArgumentNullException("acquiredFiles");
        }
        RequirePlainAbsoluteFilePath(path, "path");
        string key = NormalizeComparableFinalPath(path);
        StepDependencyFile existing;
        if (acquiredByPath.TryGetValue(key, out existing))
        {
            return existing;
        }
        StepDependencyFile acquired = AcquireStepDependencyFile(
            path,
            missingReturnsNull);
        if (acquired == null)
        {
            return null;
        }
        acquiredByPath.Add(key, acquired);
        acquiredFiles.Add(acquired);
        return acquired;
    }

    private static string ReadStepDependencyUtf8Text(
        StepDependencyFile dependency,
        int maximumBytes)
    {
        if (dependency == null)
        {
            throw new ArgumentNullException("dependency");
        }
        if (maximumBytes < 1)
        {
            throw new ArgumentOutOfRangeException("maximumBytes");
        }
        PathIdentity beforeReadIdentity = GetPathIdentityFromOpenHandle(
            dependency.ReadHandle,
            PathKind.File);
        if (!SameStablePath(
            dependency.CreationIdentity,
            beforeReadIdentity))
        {
            throw new WinterGatePathIdentityException(
                "path identity: retained narrative inventory changed " +
                "before its same-handle read.");
        }

        byte[] content;
        using (SafeFileHandle borrowed = new SafeFileHandle(
            dependency.ReadHandle,
            false))
        using (FileStream stream = new FileStream(
            borrowed,
            FileAccess.Read))
        {
            if (stream.Length > maximumBytes)
            {
                throw new InvalidDataException(
                    "Narrative inventory exceeds its size limit.");
            }
            content = new byte[checked((int)stream.Length)];
            stream.Position = 0;
            int totalRead = 0;
            while (totalRead < content.Length)
            {
                int read = stream.Read(
                    content,
                    totalRead,
                    content.Length - totalRead);
                if (read == 0)
                {
                    throw new EndOfStreamException(
                        "Narrative inventory ended before its reported length.");
                }
                totalRead += read;
            }
        }
        PathIdentity afterReadIdentity = GetPathIdentityFromOpenHandle(
            dependency.ReadHandle,
            PathKind.File);
        if (!SameStablePath(
            dependency.CreationIdentity,
            afterReadIdentity))
        {
            throw new WinterGatePathIdentityException(
                "path identity: retained narrative inventory changed " +
                "during its same-handle read.");
        }
        if (content.Length >= 3 &&
            content[0] == 0xEF &&
            content[1] == 0xBB &&
            content[2] == 0xBF)
        {
            throw new InvalidDataException(
                "Narrative inventory must not contain a UTF-8 BOM.");
        }
        return new UTF8Encoding(false, true).GetString(content);
    }

    private static NarrativeInputInventory ParseNarrativeInputInventory(
        string text)
    {
        if (text == null)
        {
            throw new ArgumentNullException("text");
        }
        StringBuilder normalized = new StringBuilder(text.Length);
        for (int index = 0; index < text.Length; index++)
        {
            char current = text[index];
            if (current == '\r')
            {
                if (index + 1 >= text.Length ||
                    text[index + 1] != '\n')
                {
                    throw new InvalidDataException(
                        "Narrative inventory contains a standalone CR.");
                }
                normalized.Append('\n');
                index++;
            }
            else
            {
                normalized.Append(current);
            }
        }
        if (normalized.Length == 0 ||
            normalized[normalized.Length - 1] != '\n')
        {
            throw new InvalidDataException(
                "Narrative inventory must end in exactly one LF.");
        }
        string[] lines = normalized.ToString().Split(
            new char[] { '\n' });
        if (lines.Length < 2 ||
            lines[lines.Length - 1].Length != 0)
        {
            throw new InvalidDataException(
                "Narrative inventory has an invalid terminal line.");
        }
        string[] header = lines[0].Split(new char[] { '\t' });
        if (header.Length != 3 ||
            !String.Equals(
                header[0],
                "WINTER_NARRATIVE_INPUTS_V1",
                StringComparison.Ordinal) ||
            !header[1].StartsWith("R=", StringComparison.Ordinal) ||
            !header[2].StartsWith("P=", StringComparison.Ordinal))
        {
            throw new InvalidDataException(
                "Narrative inventory header is not canonical.");
        }
        int rpyCount = ParseCanonicalNarrativeCount(
            header[1].Substring(2),
            1,
            MaximumNarrativeRpyInputs,
            "R");
        int portraitCount = ParseCanonicalNarrativeCount(
            header[2].Substring(2),
            0,
            MaximumNarrativePortraitInputs,
            "P");
        int expectedLineCount = checked(1 + rpyCount + portraitCount);
        if (lines.Length - 1 != expectedLineCount)
        {
            throw new InvalidDataException(
                "Narrative inventory count does not match its entries.");
        }

        string[] rpyRelativePaths = new string[rpyCount];
        string previousRpy = null;
        for (int index = 0; index < rpyCount; index++)
        {
            string value = ParseNarrativeInventoryEntry(
                lines[index + 1],
                'R');
            if (previousRpy != null &&
                String.CompareOrdinal(previousRpy, value) >= 0)
            {
                throw new InvalidDataException(
                    "Narrative R entries must be unique and strictly " +
                    "Ordinal-sorted.");
            }
            rpyRelativePaths[index] = value;
            previousRpy = value;
        }
        string[] portraitNames = new string[portraitCount];
        string previousPortrait = null;
        for (int index = 0; index < portraitCount; index++)
        {
            string value = ParseNarrativeInventoryEntry(
                lines[1 + rpyCount + index],
                'P');
            if (previousPortrait != null &&
                String.CompareOrdinal(previousPortrait, value) >= 0)
            {
                throw new InvalidDataException(
                    "Narrative P entries must be unique and strictly " +
                    "Ordinal-sorted.");
            }
            portraitNames[index] = value;
            previousPortrait = value;
        }
        return new NarrativeInputInventory(
            rpyRelativePaths,
            portraitNames);
    }

    private static int ParseCanonicalNarrativeCount(
        string token,
        int minimum,
        int maximum,
        string label)
    {
        int value;
        if (String.IsNullOrEmpty(token) ||
            !Int32.TryParse(
                token,
                NumberStyles.None,
                CultureInfo.InvariantCulture,
                out value) ||
            !String.Equals(
                token,
                value.ToString(CultureInfo.InvariantCulture),
                StringComparison.Ordinal) ||
            value < minimum ||
            value > maximum)
        {
            throw new InvalidDataException(
                "Narrative inventory " + label +
                " count is not canonical or is outside its bound.");
        }
        return value;
    }

    private static string ParseNarrativeInventoryEntry(
        string line,
        char expectedKind)
    {
        string[] fields = line.Split(new char[] { '\t' });
        if (fields.Length != 2 ||
            fields[0].Length != 1 ||
            fields[0][0] != expectedKind)
        {
            throw new InvalidDataException(
                "Narrative inventory entry kind is invalid.");
        }
        string value = fields[1];
        if (expectedKind == 'R')
        {
            const string prefix = "game/";
            const string suffix = ".rpy";
            if (!value.StartsWith(prefix, StringComparison.Ordinal) ||
                !value.EndsWith(suffix, StringComparison.Ordinal) ||
                !IsLowerAsciiInventoryStem(
                    value.Substring(
                        prefix.Length,
                        value.Length - prefix.Length - suffix.Length)))
            {
                throw new InvalidDataException(
                    "Narrative R entry is not a lower-ASCII direct game path.");
            }
        }
        else
        {
            const string suffix = ".png";
            if (!value.EndsWith(suffix, StringComparison.Ordinal) ||
                !IsLowerAsciiInventoryStem(
                    value.Substring(0, value.Length - suffix.Length)))
            {
                throw new InvalidDataException(
                    "Narrative P entry is not a lower-ASCII PNG leaf.");
            }
        }
        return value;
    }

    private static bool IsLowerAsciiInventoryStem(string value)
    {
        if (String.IsNullOrEmpty(value))
        {
            return false;
        }
        for (int index = 0; index < value.Length; index++)
        {
            char current = value[index];
            if (!((current >= 'a' && current <= 'z') ||
                  (current >= '0' && current <= '9') ||
                  current == '_'))
            {
                return false;
            }
        }
        return true;
    }
```

Replace the complete New-GateStep function with:

```powershell
function New-GateStep {
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [ValidatePattern('^[a-z0-9][a-z0-9-]*$')]
        [string]$Name,
        [Parameter(Mandatory = $true, Position = 1)]
        [ValidateSet('Python', 'RenPySuite')]
        [string]$Kind,
        [Parameter(Mandatory = $true, Position = 2)]
        [string]$Executable,
        [Parameter(Mandatory = $true, Position = 3)]
        [AllowEmptyCollection()]
        [string[]]$Arguments,
        [Parameter(Mandatory = $true, Position = 4)]
        [ValidateRange(1, 1860)]
        [int]$TimeoutSeconds,
        [Parameter(Mandatory = $true, Position = 5)]
        [ValidateSet(
            'exit-zero', 'runner-passed', 'capability-json', 'canon-json',
            'manual-review', 'portrait-json', 'overlap-json',
            'show-before-json', 'nested-quote-json'
        )]
        [string]$Postcondition,
        [Parameter(Position = 6)]
        [string[]]$RequiredFiles = @(),
        [Parameter(Position = 7)]
        [AllowNull()]
        [string]$InventoryPath = $null
    )
    if (-not [IO.Path]::IsPathRooted($Executable)) {
        throw "Step '$Name' executable must be absolute."
    }
    foreach ($argument in $Arguments) {
        if ($null -eq $argument) {
            throw "Step '$Name' has a null process argument."
        }
    }
    foreach ($required in $RequiredFiles) {
        if (-not [IO.Path]::IsPathRooted($required)) {
            throw "Step '$Name' required file must be absolute: $required"
        }
    }
    if ($null -ne $InventoryPath -and
        -not [IO.Path]::IsPathRooted($InventoryPath)) {
        throw "Step '$Name' inventory path must be absolute: $InventoryPath"
    }

    $dependencyLease = $null
    $leaseRegistered = $false
    try {
        if ($null -eq $InventoryPath) {
            $dependencyLease =
                [WinterGate.Native]::AcquireStepDependencyLease(
                    $Executable,
                    [string[]]$RequiredFiles.Clone())
        }
        else {
            $dependencyLease =
                [WinterGate.Native]::AcquireStepDependencyLease(
                    $Executable,
                    [string[]]$RequiredFiles.Clone(),
                    $InventoryPath,
                    $script:ProjectIdentity)
        }
        [void]$script:StepDependencyLeases.Add($dependencyLease)
        $leaseRegistered = $true
        [pscustomobject][ordered]@{
            Name = $Name
            Kind = $Kind
            Executable = $dependencyLease.ExecutablePath
            DependencyLease = $dependencyLease
            Arguments = [string[]]$Arguments.Clone()
            TimeoutSeconds = $TimeoutSeconds
            Postcondition = $Postcondition
            RequiredFiles = [string[]]$RequiredFiles.Clone()
        }
    }
    catch [WinterGate.WinterGatePathIdentityException] {
        throw [InvalidOperationException]::new(
            ("Manifest dependency is unsafe for step '$Name'. " +
             $_.Exception.Message),
            $_.Exception)
    }
    finally {
        if ($null -ne $dependencyLease -and -not $leaseRegistered) {
            $dependencyLease.Dispose()
        }
    }
}
```

InventoryPath is deliberately absent from the returned object and from every
result/evidence schema. Capability, canon, and portrait select the new overload;
all other steps continue through the old two-argument overload.

Append this exact block to the existing
test_future_runner_dependency_lease_denies_in_place_write_until_gate_exit
method after its current Structural assertions; do not add a test method:

```python
        narrative_fixture = self.make_project()
        self.addCleanup(narrative_fixture.close)
        narrative_ready = narrative_fixture.base / "inventory-r-ready"
        narrative_release = narrative_fixture.base / "inventory-r-release"
        listed_rpy = narrative_fixture.game / "inventory_lease_probe.rpy"
        listed_original = b"# inventory-only lease probe\n"
        listed_rpy.write_bytes(listed_original)
        narrative_inventory = (
            narrative_fixture.tools / "winter_narrative_inputs.txt"
        )
        narrative_inventory.write_bytes(
            (
                "WINTER_NARRATIVE_INPUTS_V1\tR=2\tP=0\n"
                "R\tgame/governance_winter_interlude.rpy\n"
                "R\tgame/inventory_lease_probe.rpy\n"
            ).encode("utf-8")
        )
        replacement = (
            narrative_fixture.base
            / "inventory-r-replacement"
            / listed_rpy.name
        )
        replacement.parent.mkdir()
        replacement.write_bytes(listed_original + b"# replacement\n")
        narrative_process = narrative_fixture.start_writer_race(
            narrative_ready,
            narrative_release,
            gate="Narrative",
            phase="Final",
            documents=passing_narrative_documents("final"),
        )

        def stop_narrative_process() -> None:
            if narrative_process.poll() is None:
                narrative_process.kill()
            narrative_process.communicate(timeout=10)

        self.addCleanup(stop_narrative_process)
        narrative_deadline = time.monotonic() + 15.0
        while (
            not narrative_ready.exists()
            and time.monotonic() < narrative_deadline
        ):
            time.sleep(0.01)
        if not narrative_ready.is_file():
            early_stdout, early_stderr = narrative_process.communicate(
                timeout=10
            )
            self.fail(
                "Narrative child did not reach the inventory lease barrier: "
                f"returncode={narrative_process.returncode}; "
                f"stdout={early_stdout!r}; stderr={early_stderr!r}"
            )

        listed_inode = listed_rpy.stat().st_ino
        listed_write_error: OSError | None = None
        listed_replace_error: OSError | None = None
        try:
            with listed_rpy.open("r+b", buffering=0) as stream:
                stream.seek(0)
                stream.write(listed_original + b"# in-place\n")
                stream.truncate()
                os.fsync(stream.fileno())
        except OSError as error:
            listed_write_error = error
        try:
            os.replace(replacement, listed_rpy)
        except OSError as error:
            listed_replace_error = error
        finally:
            narrative_release.write_text("release", encoding="utf-8")

        narrative_stdout, narrative_stderr = (
            narrative_process.communicate(timeout=65)
        )
        narrative_diagnostic = {
            "write_error": repr(listed_write_error),
            "replace_error": repr(listed_replace_error),
            "stdout": narrative_stdout,
            "stderr": narrative_stderr,
            "records": narrative_fixture.records(),
        }
        for blocked_error in (
            listed_write_error,
            listed_replace_error,
        ):
            self.assertIsInstance(
                blocked_error,
                PermissionError,
                narrative_diagnostic,
            )
            self.assertTrue(
                getattr(blocked_error, "winerror", None) in (5, 32, 33)
                or getattr(blocked_error, "errno", None) == 13,
                narrative_diagnostic,
            )
        self.assertEqual(listed_inode, listed_rpy.stat().st_ino)
        self.assertEqual(listed_original, listed_rpy.read_bytes())
        self.assertEqual(
            narrative_process.returncode,
            0,
            narrative_diagnostic,
        )
        self.assertEqual(
            len(narrative_diagnostic["records"]),
            9,
            narrative_diagnostic,
        )
        narrative_summary = narrative_fixture.summary()
        self.assertEqual(narrative_summary["status"], "passed")
        self.assertEqual(len(narrative_summary["steps"]), 9)

        os.replace(replacement, listed_rpy)
        with listed_rpy.open("r+b", buffering=0) as stream:
            stream.seek(0)
            stream.write(listed_original)
            stream.truncate()
            os.fsync(stream.fileno())
        self.assertEqual(listed_original, listed_rpy.read_bytes())
```

- [ ] **Step 4: Create the complete capability producer**

Create Tools/check_winter_narrative_capabilities.py with exactly:

```python
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from collections.abc import Callable, Sequence
from pathlib import Path

try:
    from Tools.winter_narrative_json import (
        STRUCTURED_OUTPUT_ENV,
        WINTER_GATE_JOB_ENV,
        StructuredJsonSink,
        StructuredOutputError,
    )
except ModuleNotFoundError:
    from winter_narrative_json import (
        STRUCTURED_OUTPUT_ENV,
        WINTER_GATE_JOB_ENV,
        StructuredJsonSink,
        StructuredOutputError,
    )


ROOT = Path(__file__).resolve().parents[1]

CAPABILITY_TEST_IDS: dict[str, tuple[str, ...]] = {
    "canon_json": (
        "Tools.test_winter_narrative_capabilities."
        "CanonJsonProducerTests.test_canon_json_cli_emits_exact_schema_and_scans_full_game",
        "Tools.test_winter_narrative_capabilities."
        "CanonJsonProducerTests.test_canon_each_blocking_category_has_positive_and_zero_case",
        "Tools.test_winter_narrative_capabilities."
        "CanonJsonProducerTests.test_canon_trigger_only_is_informational_and_nonblocking",
        "Tools.test_winter_narrative_capabilities."
        "CanonJsonProducerTests.test_canon_transport_and_cli_reject_mismatch_output_dir_and_collision",
        "Tools.test_winter_narrative_capabilities."
        "CanonJsonProducerTests.test_canon_no_argument_legacy_mode_is_text_and_fail_closed",
    ),
    "portrait_json": (
        "Tools.test_winter_narrative_capabilities."
        "PortraitJsonProducerTests.test_portrait_json_cli_emits_exact_scoped_schema",
        "Tools.test_winter_narrative_capabilities."
        "PortraitJsonProducerTests.test_portrait_missing_show_and_unregistered_tag_are_blocking",
        "Tools.test_winter_narrative_capabilities."
        "PortraitJsonProducerTests.test_portrait_json_mode_never_writes_repository_reports_or_accepts_output_dir",
        "Tools.test_winter_narrative_capabilities."
        "PortraitJsonProducerTests.test_portrait_missing_or_outside_target_fails_closed",
        "Tools.test_winter_narrative_capabilities."
        "PortraitJsonProducerTests.test_portrait_no_argument_legacy_mode_preserves_reports_and_exit_contract",
    ),
    "overlap_json": (
        "Tools.test_winter_narrative_capabilities."
        "NarrationOverlapJsonProducerTests.test_overlap_json_cli_emits_exact_clean_and_positive_schema",
        "Tools.test_winter_narrative_capabilities."
        "NarrationOverlapJsonProducerTests.test_overlap_missing_target_and_invalid_file_flags_fail_closed",
        "Tools.test_winter_narrative_capabilities."
        "NarrationOverlapJsonProducerTests.test_overlap_transport_rejects_mismatch_output_dir_and_collision",
        "Tools.test_winter_narrative_capabilities."
        "NarrationOverlapJsonProducerTests.test_overlap_no_argument_legacy_mode_is_preserved",
    ),
    "show_before_json": (
        "Tools.test_winter_narrative_capabilities."
        "ShowBeforePreventionJsonProducerTests.test_show_before_json_cli_emits_exact_scoped_schema",
        "Tools.test_winter_narrative_capabilities."
        "ShowBeforePreventionJsonProducerTests.test_show_before_rejects_removed_or_mismatched_prevention",
        "Tools.test_winter_narrative_capabilities."
        "ShowBeforePreventionJsonProducerTests.test_show_before_ignores_right_portraits_and_rejects_missing_targets",
        "Tools.test_winter_narrative_capabilities."
        "ShowBeforePreventionJsonProducerTests.test_show_before_transport_and_no_argument_mode_are_fail_closed",
    ),
    "nested_quote_json": (
        "Tools.test_winter_narrative_capabilities."
        "NestedQuoteJsonProducerTests.test_nested_quote_json_scopes_the_winter_governance_module",
        "Tools.test_winter_narrative_capabilities."
        "NestedQuoteJsonProducerTests.test_nested_quote_blocks_unescaped_but_accepts_escaped_and_chinese_quotes",
        "Tools.test_winter_narrative_capabilities."
        "NestedQuoteJsonProducerTests.test_nested_quote_import_has_no_cwd_or_scan_side_effect",
        "Tools.test_winter_narrative_capabilities."
        "NestedQuoteJsonProducerTests.test_nested_quote_transport_flags_and_missing_target_fail_closed",
        "Tools.test_winter_narrative_capabilities."
        "NestedQuoteJsonProducerTests.test_nested_quote_no_argument_legacy_mode_is_preserved",
    ),
}

BATCH_CONTRACT_TEST_IDS: tuple[str, ...] = (
    "Tools.test_governance_winter_interlude."
    "WinterStoryGraphContractTests."
    "test_complete_story_graph_labels_exist_exactly_once",
    "Tools.test_governance_winter_interlude."
    "WinterStoryGraphContractTests."
    "test_six_outcome_contracts_have_exact_nonempty_symbolic_slots",
    "Tools.test_governance_winter_interlude."
    "WinterStoryGraphContractTests."
    "test_qualitative_lines_assets_and_semantic_markers_are_structural",
    "Tools.test_governance_winter_interlude."
    "WinterStoryGraphContractTests."
    "test_all_task7_renpy_control_expressions_are_exact_and_guarded",
    "Tools.test_governance_winter_interlude."
    "WinterStoryGraphContractTests."
    "test_player_visible_semantics_are_independent_and_fail_closed",
)

FINAL_CONTRACT_TEST_IDS: tuple[str, ...] = (
    "Tools.test_governance_winter_interlude."
    "WinterNarrativeFinalContractTests."
    "test_active_paths_are_11000_to_14000_chinese_characters",
    "Tools.test_governance_winter_interlude."
    "WinterNarrativeFinalContractTests."
    "test_active_paths_match_user_approved_legacy_reuse_contract",
    "Tools.test_governance_winter_interlude."
    "WinterNarrativeFinalContractTests."
    "test_six_visible_semantics_are_literal_and_fail_closed",
    "Tools.test_governance_winter_interlude."
    "WinterNarrativeFinalContractTests."
    "test_player_visible_structural_placeholders_are_absent",
    "Tools.test_governance_winter_interlude."
    "WinterNarrativeFinalContractTests."
    "test_every_scene_has_approved_final_copy",
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--phase", required=True, choices=("batch", "final"))
    parser.add_argument("--format", required=True, choices=("json",))
    parser.add_argument("--output", required=True)
    return parser


def run_test_ids(test_ids: tuple[str, ...]) -> bool:
    if not test_ids or len(test_ids) != len(set(test_ids)):
        return False
    environment = os.environ.copy()
    environment.pop(STRUCTURED_OUTPUT_ENV, None)
    environment.pop(WINTER_GATE_JOB_ENV, None)
    try:
        completed = subprocess.run(
            [
                sys.executable,
                "-B",
                "-m",
                "unittest",
                *test_ids,
            ],
            cwd=ROOT,
            env=environment,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="strict",
            timeout=120,
            close_fds=True,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired):
        return False
    combined = completed.stdout + "\n" + completed.stderr
    ran = re.findall(r"(?m)^Ran ([0-9]+) tests? in ", combined)
    terminal_ok = re.findall(r"(?m)^OK$", combined)
    return (
        completed.returncode == 0
        and ran == [str(len(test_ids))]
        and terminal_ok == ["OK"]
    )


def evaluate_capabilities(
    phase: str,
    runner: Callable[[tuple[str, ...]], bool] = run_test_ids,
) -> dict[str, bool]:
    if phase not in ("batch", "final"):
        raise ValueError("unsupported narrative phase")
    capabilities = {
        name: bool(runner(test_ids))
        for name, test_ids in CAPABILITY_TEST_IDS.items()
    }
    capabilities["batch_contracts"] = bool(
        runner(BATCH_CONTRACT_TEST_IDS)
    )
    capabilities["final_contracts"] = bool(
        runner(FINAL_CONTRACT_TEST_IDS)
    )
    return capabilities


def build_document(
    phase: str,
    capabilities: dict[str, bool],
) -> dict[str, object]:
    expected = (
        set(CAPABILITY_TEST_IDS)
        | {"batch_contracts", "final_contracts"}
    )
    if set(capabilities) != expected:
        raise ValueError("capability property set is not exact")
    if any(type(value) is not bool for value in capabilities.values()):
        raise TypeError("capabilities must be strict booleans")
    required = [
        capabilities["canon_json"],
        capabilities["portrait_json"],
        capabilities["overlap_json"],
        capabilities["show_before_json"],
        capabilities["nested_quote_json"],
        capabilities["batch_contracts"],
    ]
    if phase == "final":
        required.append(capabilities["final_contracts"])
    return {
        "schema_version": 1,
        "tool": "winter_narrative_capabilities",
        "phase": phase,
        "ready": all(required),
        "capabilities": capabilities,
    }


def main(
    argv: Sequence[str] | None = None,
    runner: Callable[[tuple[str, ...]], bool] = run_test_ids,
) -> int:
    arguments = build_parser().parse_args(argv)
    if not os.path.isabs(arguments.output):
        print("winter capability evidence: --output must be absolute", file=sys.stderr)
        return 2
    sink: StructuredJsonSink | None = None
    try:
        sink = StructuredJsonSink.claim(arguments.output)
        capabilities = evaluate_capabilities(arguments.phase, runner)
        document = build_document(arguments.phase, capabilities)
        sink.write(document)
        return 0 if document["ready"] else 1
    except (
        OSError,
        StructuredOutputError,
        TypeError,
        UnicodeError,
        ValueError,
    ) as error:
        print(f"winter capability evidence: {error}", file=sys.stderr)
        return 2
    finally:
        if sink is not None:
            sink.close()


if __name__ == "__main__":
    raise SystemExit(main())
```

Take the close-failure RED against that initial checker body before changing its
tail:

```powershell
$red = & python -m unittest Tools.test_winter_narrative_capabilities.WinterNarrativeCapabilityCheckerTests.test_cli_claims_before_probes_and_writes_not_ready_evidence -v 2>&1
$redExit = $LASTEXITCODE
$red | Set-Content -LiteralPath .superpowers/sdd/task8-capability-close-red.txt -Encoding UTF8
if ($redExit -eq 0) { throw 'Capability close RED unexpectedly passed.' }
$joined = $red -join [Environment]::NewLine
if ($joined -notmatch 'Ran 1 test' -or
    $joined -notmatch 'FAILED \(failures=1\)' -or
    $joined -match '(?m)^ERROR:') {
  throw 'Capability close RED was not the one controlled assertion failure.'
}
```

Expected close RED: `Ran 1 test`, one assertion failure, zero errors. The
initial checker closes only from `finally`; an `OSError` therefore escapes
instead of returning the producer-contract exit 2.

Replace the complete `main` function with this parseable final body:

```python
def main(
    argv: Sequence[str] | None = None,
    runner: Callable[[tuple[str, ...]], bool] = run_test_ids,
) -> int:
    arguments = build_parser().parse_args(argv)
    if not os.path.isabs(arguments.output):
        print("winter capability evidence: --output must be absolute", file=sys.stderr)
        return 2
    sink: StructuredJsonSink | None = None
    try:
        sink = StructuredJsonSink.claim(arguments.output)
        capabilities = evaluate_capabilities(arguments.phase, runner)
        document = build_document(arguments.phase, capabilities)
        sink.write(document)
        sink.close()
        sink = None
        return 0 if document["ready"] else 1
    except (
        OSError,
        StructuredOutputError,
        TypeError,
        UnicodeError,
        ValueError,
    ) as error:
        print(f"winter capability evidence: {error}", file=sys.stderr)
        return 2
    finally:
        if sink is not None:
            try:
                sink.close()
            except OSError as close_error:
                print(
                    f"winter capability evidence close: {close_error}",
                    file=sys.stderr,
                )
```

The normal close now occurs before return; its failure is caught and returns 2.
The final cleanup is best effort, emits a diagnostic if it also fails, and never
adds a path fallback.

- [ ] **Step 5: Replace the temporary absent-checker boundary and register leases**

In Tools/test_winter_interlude_gate.py replace
test_real_project_is_capability_first_when_checker_is_absent with:

```python
class _Task8CapabilityBoundaryCatalog:
    def test_real_project_stops_at_missing_show_scanner_during_task8_bootstrap(
        self,
    ) -> None:
        self.assertTrue(
            (ROOT / "Tools" / "check_winter_narrative_capabilities.py").is_file()
        )
        self.assertFalse(
            (ROOT / "Tools" / "scan_show_before_prevention.py").exists()
        )
        for phase in ("Batch", "Final"):
            with self.subTest(phase=phase):
                with tempfile.TemporaryDirectory(
                    prefix="winter-real-missing-show-"
                ) as outside_text:
                    outside = Path(outside_text)
                    run_root = outside / f"run-{phase.lower()}"
                    appdata = outside / "appdata"
                    appdata.mkdir()
                    environment = os.environ.copy()
                    environment["APPDATA"] = str(appdata)
                    completed = run_gate(
                        "-Gate",
                        "Narrative",
                        "-NarrativePhase",
                        phase,
                        "-ProjectRoot",
                        str(ROOT),
                        "-RunRoot",
                        str(run_root),
                        env=environment,
                    )
                    self.assertEqual(completed.returncode, 1)
                    summary = json.loads(
                        (
                            run_root / "evidence" / "gate-summary.json"
                        ).read_text(encoding="utf-8-sig")
                    )
                    self.assertEqual(summary["status"], "failed")
                    self.assertEqual(summary["failure_kind"], "validation")
                    self.assertRegex(
                        summary["error"],
                        r"(?i)scan_show_before_prevention[.]py",
                    )
                    self.assertEqual(summary["steps"], [])
```

Copy only the method from the catalog class into the existing
WinterInterludeGateCapabilityTests class; do not add the catalog class itself.

In `_GateFixture.__init__`, replace the complete `fixed_files` tuple with:

```python
fixed_files = (
    "Tools/test_governance_winter_interlude.py",
    "Tools/test_winter_narrative_capabilities.py",
    "Tools/winter_narrative_json.py",
    "Tools/winter_narrative_inputs.py",
    "Tools/winter_narrative_inputs.txt",
    "Tools/check_winter_narrative_capabilities.py",
    "Tools/scan_canon.py",
    "Tools/scan_ai_smell.py",
    "scan_missing_portraits.py",
    "scan_narration_overlap.py",
    "Tools/scan_show_before_prevention.py",
    "Tools/scan_nested_quotes.py",
    "game/governance_winter_interlude.rpy",
)
```

Immediately after the generic fixed-file write loop, replace the generic
inventory content with the exact Task 2 fake membership:

```python
(self.tools / "winter_narrative_inputs.txt").write_bytes(
    (
        "WINTER_NARRATIVE_INPUTS_V1\tR=1\tP=0\n"
        "R\tgame/governance_winter_interlude.rpy\n"
    ).encode("utf-8")
)
```

The fake Narrative projects must contain every manifest dependency before
`New-GateStep` acquires its leases. These are fixed identity inputs only; the
recording child still owns fake-project process behavior.

In Get-NarrativeGateManifest, immediately after resolving checker, resolve:

```powershell
    $narrativeInputs = Get-ExpectedProjectFilePath `
        $project 'Tools\winter_narrative_inputs.txt'
    $narrativeInputsModule = Get-ExpectedProjectFilePath `
        $project 'Tools\winter_narrative_inputs.py'
    $structuredWriter = Get-ExpectedProjectFilePath `
        $project 'Tools\winter_narrative_json.py'
    $capabilityTests = Get-ExpectedProjectFilePath `
        $project 'Tools\test_winter_narrative_capabilities.py'
```

Immediately before the manifest's object-array expression, create this exact
array:

```powershell
    $capabilityRequiredFiles = [string[]]@(
        $checker,
        $structuredWriter,
        $narrativeInputsModule,
        $capabilityTests,
        $sourceContract,
        $target,
        $canon,
        $portrait,
        $overlap,
        $showBefore,
        $nestedQuotes
    )
```

Replace the complete capability entry with:

```powershell
        (New-GateStep 'narrative-capability' 'Python' `
            $script:PythonIdentity.FinalPath `
            ([string[]]@(
                '-B', $checker,
                '--phase', $phase,
                '--format', 'json',
                '--output', $capabilityJson
            )) $ToolTimeoutSeconds 'capability-json' `
            $capabilityRequiredFiles `
            -InventoryPath $narrativeInputs)
```

The checker receives no `--inputs` process argument. The inventory is a
dependency lease for every named probe it launches, not a checker CLI input.

Do not change any argument, timeout, postcondition, output stem, reservation,
or any of the remaining eight manifest entries.

- [ ] **Step 6: Run the nine-test GREEN and commit**

```powershell
python -m unittest Tools.test_winter_narrative_capabilities.WinterNarrativeCapabilityCheckerTests Tools.test_winter_narrative_capabilities.WinterCapabilityProbeEnvironmentTests Tools.test_winter_interlude_gate.WinterInterludeGateCapabilityTests.test_real_project_stops_at_missing_show_scanner_during_task8_bootstrap Tools.test_winter_interlude_gate.WinterInterludeGateCapabilityTests.test_valid_batch_capability_uses_full_stem_and_passes Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_executable_identity_uses_readable_full_chain_api Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_future_runner_dependency_lease_denies_in_place_write_until_gate_exit -v
if ($LASTEXITCODE -ne 0) { throw 'Capability checker GREEN failed.' }
python -m unittest Tools.test_winter_interlude_gate.WinterInterludeGateInterfaceTests.test_script_exists_and_parses_with_official_powershell_parser -v
if ($LASTEXITCODE -ne 0) { throw 'Capability gate parser check failed.' }
@'
import unittest

module_loader = unittest.TestLoader()
module_suite = module_loader.loadTestsFromName(
    "Tools.test_winter_narrative_capabilities"
)
repository_loader = unittest.TestLoader()
repository_suite = repository_loader.discover(start_dir="Tools")
if module_loader.errors != [] or repository_loader.errors != []:
    raise SystemExit(
        "static unittest loading errors: "
        + repr(module_loader.errors + repository_loader.errors)
    )
counts = (module_suite.countTestCases(), repository_suite.countTestCases())
expected = (10, 349)
if counts != expected:
    raise SystemExit(f"unexpected static unittest counts: {counts!r}")
print({"capability": counts[0], "discovery": counts[1], "loader_errors": 0})
'@ | python -
if ($LASTEXITCODE -ne 0) { throw 'Capability static test catalog failed.' }
$expected = [string[]]@(
  'Tools/Run-WinterInterludeGate.ps1',
  'Tools/check_winter_narrative_capabilities.py',
  'Tools/test_winter_interlude_gate.py',
  'Tools/test_winter_narrative_capabilities.py',
  'Tools/winter_narrative_inputs.py',
  'Tools/winter_narrative_inputs.txt'
)
git diff --cached --quiet
if ($LASTEXITCODE -ne 0) { throw 'Capability slice started with a nonempty index.' }
git add -- $expected
$actual = [string[]]@(git diff --cached --name-only)
if (@(Compare-Object ($expected | Sort-Object) ($actual | Sort-Object)).Count -ne 0) {
  throw "Unexpected capability slice paths: $($actual -join ', ')"
}
git diff --cached --check
if ($LASTEXITCODE -ne 0) { throw 'Capability staged diff check failed.' }
git commit -m "feat: add winter narrative capability gate"
if ($LASTEXITCODE -ne 0) { throw 'Capability slice commit failed.' }
$subject = (git log -1 --pretty=%s).Trim()
if ($subject -cne 'feat: add winter narrative capability gate') {
  throw "Unexpected capability commit subject: $subject"
}
if (git status --short) { throw 'Capability commit left a dirty worktree.' }
```

Expected focused GREEN: Ran 9 tests, OK. Expected static catalog: capability
module 10 methods, `Tools` discovery 349 methods, and both loader error lists
exactly empty; no cumulative module or repository test body runs at this
intermediate SHA. The seventh focused test constructs the real
`_GateFixture` fake project and proves the expanded capability leases survive
manifest validation; the final two retain the same-handle inventory plus its
listed R files, reject all parser and source mutants, and deny both in-place
write and replacement through child drain. The gate module remains exactly 87
tests because one temporary boundary method was replaced in place. Both real
Narrative phases still fail before launching a child, now specifically because
the show-before producer is absent.

**Asset audit:** Tooling only. Art, music, SFX, portrait, animation, UI, font,
old-game, shipping source, and package size are unchanged.

---

## Task 3: Add full-project canon JSON evidence

**Files:**

- Modify: `Tools/test_winter_narrative_capabilities.py`
- Modify: `Tools/test_winter_interlude_gate.py`
- Modify: `Tools/scan_canon.py`
- Modify: `Tools/Run-WinterInterludeGate.ps1`

This slice gives the existing canon scanner one strict machine contract without
weakening its no-argument human report. JSON mode scans every inventory-listed
direct game script except the established skip list and fails closed if actual
direct R/P membership drifts before or after the scan. Its four blocking arrays
are independent; trigger occurrences are always informational.

- [ ] **Step 1: Add the shared producer-test infrastructure and five canon tests**

Insert the following complete infrastructure immediately before the first
producer test class. Later producer slices reuse these functions unchanged.

```python
PRODUCERS = {
    "canon": ROOT / "Tools" / "scan_canon.py",
    "portrait": ROOT / "scan_missing_portraits.py",
    "overlap": ROOT / "scan_narration_overlap.py",
    "show_before": ROOT / "Tools" / "scan_show_before_prevention.py",
    "nested_quote": ROOT / "Tools" / "scan_nested_quotes.py",
}
COMMON_KEYS = {
    "schema_version", "tool", "scanned_files", "blocking_count", "findings"
}
FINDING_KEYS = {"path", "line", "rule", "message"}
CANON_KEYS = {
    "schema_version", "tool", "blocking_count", "anti_logic", "geography",
    "terminology", "canon_deviation", "informational_occurrences",
}
CANON_CATEGORIES = (
    "anti_logic", "geography", "terminology", "canon_deviation"
)
REPORT_NAMES = (
    "missing_portraits_A.txt",
    "missing_portraits_B.txt",
    "missing_portraits_full.json",
)


def _producer_environment(
    updates: dict[str, str] | None = None,
) -> dict[str, str]:
    environment = os.environ.copy()
    environment.pop(HANDLE_ENV, None)
    environment.pop(JOB_ENV, None)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    environment["PYTHONIOENCODING"] = "utf-8"
    environment["PYTHONUTF8"] = "1"
    if updates:
        environment.update(updates)
    return environment


def _make_producer_project(
    raw_root: str,
    producer_relative: str,
    game_files: dict[str, str],
    image_names: tuple[str, ...] = (),
) -> Path:
    project = Path(raw_root)
    (project / "Tools").mkdir(parents=True, exist_ok=True)
    (project / "game").mkdir(parents=True, exist_ok=True)
    source = ROOT / producer_relative
    destination = project / producer_relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, destination)
    shutil.copyfile(WRITER, project / "Tools" / "winter_narrative_json.py")
    shutil.copyfile(
        INPUTS_MODULE,
        project / "Tools" / "winter_narrative_inputs.py",
    )
    for name, content in game_files.items():
        target = project / "game" / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8", newline="\n")
    images = project / "game" / "images"
    images.mkdir(parents=True, exist_ok=True)
    for name in image_names:
        (images / name).write_bytes(b"")
    _write_test_inventory(project)
    return project


def _run_producer(
    project: Path,
    producer_relative: str,
    arguments: list[str],
    *,
    environment_updates: dict[str, str] | None = None,
    close_fds: bool = True,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            str(PYTHON),
            "-B",
            str(project / producer_relative),
            *arguments,
        ],
        cwd=project,
        env=_producer_environment(environment_updates),
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="strict",
        close_fds=close_fds,
        check=False,
    )


def _run_json_producer(
    project: Path,
    producer_relative: str,
    scanner_arguments: list[str],
    output: Path,
    *,
    inherited_handle: bool,
) -> subprocess.CompletedProcess[str]:
    inventory_arguments = (
        [
            "--inputs",
            str(project / "Tools" / "winter_narrative_inputs.txt"),
        ]
        if producer_relative in (
            "Tools/scan_canon.py",
            "scan_missing_portraits.py",
        )
        else []
    )
    arguments = [
        *scanner_arguments,
        *inventory_arguments,
        "--format",
        "json",
        "--output",
        str(output),
    ]
    if not inherited_handle:
        return _run_producer(project, producer_relative, arguments)
    with _ShareZeroFile(output) as owner:
        owner.write_bytes(b"WINTER_GATE_RESERVED_V1:test-marker")
        return _run_producer(
            project,
            producer_relative,
            arguments,
            environment_updates={HANDLE_ENV: str(owner.handle)},
            close_fds=False,
        )


def _exec_producer_source(
    path: Path,
    source: str,
    module_name: str,
) -> dict[str, object]:
    namespace: dict[str, object] = {
        "__file__": str(path),
        "__name__": module_name,
        "__package__": None,
    }
    exec(compile(source, str(path), "exec"), namespace)
    return namespace


def _assert_no_valid_json(case: unittest.TestCase, output: Path) -> None:
    if not output.exists():
        return
    try:
        decoded = output.read_text(encoding="utf-8")
        json.loads(decoded)
    except (UnicodeError, json.JSONDecodeError):
        return
    case.fail(f"unexpected valid JSON evidence at {output}")


def _assert_finding(
    case: unittest.TestCase,
    finding: dict[str, object],
) -> None:
    case.assertEqual(set(finding), FINDING_KEYS)
    case.assertIs(type(finding["path"]), str)
    case.assertTrue(str(finding["path"]).startswith("game/"))
    case.assertNotIn("\\", str(finding["path"]))
    case.assertIs(type(finding["line"]), int)
    case.assertGreater(int(finding["line"]), 0)
    case.assertIs(type(finding["rule"]), str)
    case.assertTrue(str(finding["rule"]).strip())
    case.assertIs(type(finding["message"]), str)
    case.assertTrue(str(finding["message"]).strip())


def _assert_common_document(
    case: unittest.TestCase,
    document: dict[str, object],
    *,
    tool: str,
    scanned_files: list[str],
) -> None:
    case.assertEqual(set(document), COMMON_KEYS)
    case.assertIs(type(document["schema_version"]), int)
    case.assertEqual(document["schema_version"], 1)
    case.assertEqual(document["tool"], tool)
    case.assertEqual(document["scanned_files"], scanned_files)
    case.assertIs(type(document["blocking_count"]), int)
    case.assertIs(type(document["findings"]), list)
    findings = document["findings"]
    case.assertEqual(document["blocking_count"], len(findings))
    for finding in findings:
        case.assertIs(type(finding), dict)
        _assert_finding(case, finding)


def _assert_canon_document(
    case: unittest.TestCase,
    document: dict[str, object],
) -> None:
    case.assertEqual(set(document), CANON_KEYS)
    case.assertIs(type(document["schema_version"]), int)
    case.assertEqual(document["schema_version"], 1)
    case.assertEqual(document["tool"], "canon")
    case.assertIs(type(document["blocking_count"]), int)
    total = 0
    for category in CANON_CATEGORIES:
        case.assertIs(type(document[category]), list)
        total += len(document[category])
        for finding in document[category]:
            case.assertIs(type(finding), dict)
            _assert_finding(case, finding)
    case.assertEqual(document["blocking_count"], total)
    case.assertIs(type(document["informational_occurrences"]), list)
    for occurrence in document["informational_occurrences"]:
        case.assertEqual(set(occurrence), {"term", "path", "line"})
        case.assertIs(type(occurrence["term"]), str)
        case.assertTrue(occurrence["term"])
        case.assertIs(type(occurrence["path"]), str)
        case.assertTrue(occurrence["path"].startswith("game/"))
        case.assertIs(type(occurrence["line"]), int)
        case.assertGreater(occurrence["line"], 0)


def _portrait_game_files(target_text: str) -> dict[str, str]:
    return {
        "characters.rpy": (
            'define alice = Character("Alice", image="alice")\n'
            'define bob = Character("Bob", image="bob")\n'
        ),
        "char_helpers.rpy": (
            "init python:\n"
            "    CHAR_IMG_TAGS = [\n"
            '        "alice_img",\n'
            '        "bob_img",\n'
            "    ]\n"
        ),
        "governance_winter_interlude.rpy": target_text,
    }
```

Append this complete class:

```python
class CanonJsonProducerTests(unittest.TestCase):
    def test_canon_json_cli_emits_exact_schema_and_scans_full_game(self) -> None:
        self.assertTrue(PRODUCERS["canon"].is_file())
        source = PRODUCERS["canon"].read_text(encoding="utf-8")
        with tempfile.TemporaryDirectory(prefix="winter-canon-schema-") as raw:
            project = _make_producer_project(
                raw,
                "Tools/scan_canon.py",
                {
                    "first.rpy": (
                        "label first:\n"
                        '    player "我替你考察过这名商人。"\n'
                    ),
                    "second.rpy": (
                        "label second:\n"
                        '    player "雷恩今天留在议事厅。"\n'
                    ),
                },
            )
            output = project / "canon.json"
            completed = _run_json_producer(
                project,
                "Tools/scan_canon.py",
                [],
                output,
                inherited_handle=True,
            )
            self.assertEqual(completed.returncode, 1, completed.stderr)
            self.assertTrue(output.is_file())
            document = json.loads(output.read_text(encoding="utf-8"))
            _assert_canon_document(self, document)
            self.assertEqual(document["blocking_count"], 1)
            self.assertEqual(
                [(item["path"], item["line"]) for item in document["anti_logic"]],
                [("game/first.rpy", 2)],
            )
            self.assertEqual(
                document["informational_occurrences"],
                [{"term": "雷恩", "path": "game/second.rpy", "line": 2}],
            )

            inventory_call = "document = build_document(inventory.rpy_files)"
            self.assertEqual(source.count(inventory_call), 1)
            glob_mutant = source.replace(
                inventory_call,
                "document = build_document()",
                1,
            )
            with self.assertRaises(AssertionError):
                self.assertEqual(glob_mutant.count(inventory_call), 1)

            real_namespace = _exec_producer_source(
                PRODUCERS["canon"],
                source,
                "_winter_canon_real",
            )
            real_namespace["ROOT"] = project
            real_namespace["GAME_DIR"] = project / "game"

            def assert_explicit_projection(
                namespace: dict[str, object],
            ) -> None:
                projected = namespace["build_document"](
                    (project / "game" / "first.rpy",)
                )
                self.assertEqual(
                    projected["informational_occurrences"],
                    [],
                )

            assert_explicit_projection(real_namespace)
            discovery_seam = "    files = _game_files(input_files)\n"
            self.assertEqual(source.count(discovery_seam), 1)
            executable_mutant = source.replace(
                discovery_seam,
                "    files = _game_files()\n",
                1,
            )
            mutant_namespace = _exec_producer_source(
                PRODUCERS["canon"],
                executable_mutant,
                "_winter_canon_glob_mutant",
            )
            mutant_namespace["ROOT"] = project
            mutant_namespace["GAME_DIR"] = project / "game"
            with self.assertRaises(AssertionError):
                assert_explicit_projection(mutant_namespace)

            (project / "game" / "unlisted.rpy").write_text(
                "label unlisted:\n    \"must not join evidence\"\n",
                encoding="utf-8",
                newline="\n",
            )
            drift_output = project / "canon-drift.json"
            drift = _run_json_producer(
                project,
                "Tools/scan_canon.py",
                [],
                drift_output,
                inherited_handle=False,
            )
            self.assertEqual(drift.returncode, 2)
            _assert_no_valid_json(self, drift_output)

    def test_canon_each_blocking_category_has_positive_and_zero_case(self) -> None:
        with tempfile.TemporaryDirectory(prefix="winter-canon-categories-") as raw:
            project = _make_producer_project(
                raw,
                "Tools/scan_canon.py",
                {
                    "issues.rpy": (
                        "label issues:\n"
                        '    player "我替你考察过这名商人。"\n'
                        '    player "那艘船抵艾登堡。"\n'
                        '    player "王军已经越过山口。"\n'
                        '    player "灰隼纹章挂在城门上。"\n'
                    )
                },
            )
            positive_output = project / "positive.json"
            positive = _run_json_producer(
                project,
                "Tools/scan_canon.py",
                [],
                positive_output,
                inherited_handle=False,
            )
            self.assertEqual(positive.returncode, 1, positive.stderr)
            self.assertTrue(positive_output.is_file())
            document = json.loads(positive_output.read_text(encoding="utf-8"))
            _assert_canon_document(self, document)
            self.assertEqual(document["blocking_count"], 4)
            expected_lines = {
                "anti_logic": 2,
                "geography": 3,
                "terminology": 4,
                "canon_deviation": 5,
            }
            for category, line in expected_lines.items():
                with self.subTest(category=category):
                    self.assertEqual(len(document[category]), 1)
                    self.assertEqual(document[category][0]["path"], "game/issues.rpy")
                    self.assertEqual(document[category][0]["line"], line)

            (project / "game" / "issues.rpy").write_text(
                "label clean:\n"
                '    player "冬天到了，众人守在议事厅。"\n',
                encoding="utf-8",
                newline="\n",
            )
            clean_output = project / "clean.json"
            clean = _run_json_producer(
                project,
                "Tools/scan_canon.py",
                [],
                clean_output,
                inherited_handle=False,
            )
            self.assertEqual(clean.returncode, 0, clean.stderr)
            clean_document = json.loads(clean_output.read_text(encoding="utf-8"))
            _assert_canon_document(self, clean_document)
            self.assertEqual(clean_document["blocking_count"], 0)
            for category in CANON_CATEGORIES:
                self.assertEqual(clean_document[category], [])

    def test_canon_trigger_only_is_informational_and_nonblocking(self) -> None:
        with tempfile.TemporaryDirectory(prefix="winter-canon-trigger-") as raw:
            project = _make_producer_project(
                raw,
                "Tools/scan_canon.py",
                {
                    "trigger.rpy": (
                        "label trigger:\n"
                        '    player "雷恩今天留在议事厅。"\n'
                    )
                },
            )
            output = project / "trigger.json"
            completed = _run_json_producer(
                project,
                "Tools/scan_canon.py",
                [],
                output,
                inherited_handle=False,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            document = json.loads(output.read_text(encoding="utf-8"))
            _assert_canon_document(self, document)
            self.assertEqual(document["blocking_count"], 0)
            self.assertEqual(
                document["informational_occurrences"],
                [{"term": "雷恩", "path": "game/trigger.rpy", "line": 2}],
            )

    def test_canon_transport_and_cli_reject_mismatch_output_dir_and_collision(self) -> None:
        with tempfile.TemporaryDirectory(prefix="winter-canon-transport-") as raw:
            project = _make_producer_project(
                raw,
                "Tools/scan_canon.py",
                {"clean.rpy": "label clean:\n    \"All quiet.\"\n"},
            )
            owned = project / "owned.json"
            wrong = project / "wrong.json"
            inputs = project / "Tools" / "winter_narrative_inputs.txt"
            marker = b"WINTER_GATE_RESERVED_V1:canon"
            with _ShareZeroFile(owned) as owner:
                owner.write_bytes(marker)
                mismatch = _run_producer(
                    project,
                    "Tools/scan_canon.py",
                    [
                        "--format", "json", "--output", str(wrong),
                        "--inputs", str(inputs),
                    ],
                    environment_updates={HANDLE_ENV: str(owner.handle)},
                    close_fds=False,
                )
                self.assertEqual(mismatch.returncode, 2)
                self.assertFalse(wrong.exists())
            self.assertEqual(owned.read_bytes(), marker)

            output_dir = project / "evidence"
            invalid_flag = _run_producer(
                project,
                "Tools/scan_canon.py",
                [
                    "--format", "json", "--output-dir", str(output_dir),
                    "--inputs", str(inputs),
                ],
            )
            self.assertEqual(invalid_flag.returncode, 2)
            self.assertFalse(output_dir.exists())

            relative = _run_producer(
                project,
                "Tools/scan_canon.py",
                [
                    "--format", "json", "--output", "relative.json",
                    "--inputs", str(inputs),
                ],
            )
            self.assertEqual(relative.returncode, 2)
            self.assertFalse((project / "relative.json").exists())

            collision = project / "collision.json"
            collision.write_bytes(b"sentinel")
            collided = _run_producer(
                project,
                "Tools/scan_canon.py",
                [
                    "--format", "json", "--output", str(collision),
                    "--inputs", str(inputs),
                ],
            )
            self.assertEqual(collided.returncode, 2)
            self.assertEqual(collision.read_bytes(), b"sentinel")

            missing_inputs_output = project / "missing-inputs.json"
            missing_inputs = _run_producer(
                project,
                "Tools/scan_canon.py",
                [
                    "--format", "json",
                    "--output", str(missing_inputs_output),
                ],
            )
            self.assertEqual(missing_inputs.returncode, 2)
            self.assertFalse(missing_inputs_output.exists())

            relative_inputs_output = project / "relative-inputs.json"
            relative_inputs = _run_producer(
                project,
                "Tools/scan_canon.py",
                [
                    "--format", "json",
                    "--output", str(relative_inputs_output),
                    "--inputs", "Tools/winter_narrative_inputs.txt",
                ],
            )
            self.assertEqual(relative_inputs.returncode, 2)
            self.assertFalse(relative_inputs_output.exists())

    def test_canon_no_argument_legacy_mode_is_text_and_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory(prefix="winter-canon-legacy-") as raw:
            project = _make_producer_project(
                raw,
                "Tools/scan_canon.py",
                {
                    "issues.rpy": (
                        "label issues:\n"
                        '    player "我替你考察过这名商人。"\n'
                    )
                },
            )
            completed = _run_producer(project, "Tools/scan_canon.py", [])
            self.assertEqual(completed.returncode, 1, completed.stderr)
            self.assertTrue(completed.stdout.strip())
            self.assertIn("game/issues.rpy:2", completed.stdout)
            with self.assertRaises(json.JSONDecodeError):
                json.loads(completed.stdout)
            self.assertEqual(list(project.glob("*.json")), [])
```

- [ ] **Step 2: Take the one-behavior canon RED**

```powershell
$red = & python -m unittest Tools.test_winter_narrative_capabilities.CanonJsonProducerTests.test_canon_json_cli_emits_exact_schema_and_scans_full_game -v 2>&1
$redExit = $LASTEXITCODE
$red | Set-Content -LiteralPath .superpowers/sdd/task8-canon-json-red.txt -Encoding UTF8
if ($redExit -eq 0) { throw 'Canon JSON RED unexpectedly passed.' }
$joined = $red -join [Environment]::NewLine
if ($joined -notmatch 'Ran 1 test' -or
    $joined -notmatch 'FAILED \(failures=1\)' -or
    $joined -match '(?m)^ERROR:') {
  throw 'Canon JSON RED did not fail only on the absent JSON behavior.'
}
```

Expected RED: `Ran 1 test`, one failure because the legacy scanner does not
create the reserved JSON document, zero errors.

- [ ] **Step 3: Replace `Tools/scan_canon.py` with the complete producer**

Replace the file with exactly the body below.

```python
from __future__ import annotations

import argparse
import os
import re
import sys
from collections.abc import Sequence
from pathlib import Path

try:
    from Tools.winter_narrative_json import StructuredJsonSink, StructuredOutputError
    from Tools.winter_narrative_inputs import (
        WinterNarrativeInputError,
        validated_winter_narrative_inputs,
    )
except ModuleNotFoundError:
    from winter_narrative_json import StructuredJsonSink, StructuredOutputError
    from winter_narrative_inputs import (
        WinterNarrativeInputError,
        validated_winter_narrative_inputs,
    )


ROOT = Path(__file__).resolve().parents[1]
GAME_DIR = ROOT / "game"
CANON_TRIGGER_WORDS = [
    "永恒者", "圣安德烈", "圣徒", "教士", "领主大人", "殿下", "陛下", "公爵",
    "金鹰", "铁锤", "双纹章", "灰隼", "苍鹰", "暮色之露", "暗百合", "旧约",
    "影月草", "托马斯", "玛格丽特", "西里尔", "伯爵夫人", "雷恩", "艾琳娜",
    "伊蕾娜", "奥德", "康拉德", "胡伯特",
]
ANTI_LOGIC_PHRASES = [
    (r"我替你考察过", 'C 反逻辑: 主角“我替你考察过”'),
    (r"我之前问过.{1,8}了", 'C 反逻辑: “我之前问过 X 了”'),
    (r"我了解过.{1,8}的", 'C 反逻辑: “我了解过 X 的”'),
    (r"我打听过.{1,8}的", 'C 反逻辑: “我打听过 X 的”'),
    (r"你的事情我都听说过", 'C 反逻辑: “你的事情我都听说过”'),
    (r"你这一年", 'C 时间线: “你这一年”不符合主线约四至五个月'),
    (r"这一年来", 'C 时间线: “这一年来”不符合主线跨度'),
    (r"你这半年", 'C 时间线: “你这半年”需人工复核'),
    (r"继任.{0,4}(半年|一年)", 'C 时间线: 继任跨度跟主线不符'),
]
TYPO_PATTERNS = [
    (r"灰隼|苍鹰", 'D 错纹章: 应为“金鹰”'),
    (r"神鹰|银鹰(?!骑士团)", 'D 错纹章: 应为“金鹰”'),
    (r"家族徽章.{0,8}(?<!金)鹰", 'D 检查“鹰”前后是否加“金”'),
]
TERM_PATTERNS = [(r"王军", 'T 术语: 主线规范为“王室军队”')]
GEO_PATTERNS = [
    (r"船(?:到|抵|进)艾登堡", 'G 地理: 艾登堡不靠海，船开不到'),
    (r"艾登堡的(?:码头|港湾|港口|栈桥|河道)", 'G 地理: 艾登堡没有海港设施'),
    (
        r"[船舰艇](?:队)?[^。；\n]{0,6}(?:驶进|驶入|驶抵|开进)艾登堡",
        'G 地理: 艾登堡不靠海，船开不进',
    ),
    (r"艾登堡.{0,6}(?:靠岸|下船|登船)", 'G 地理: 艾登堡不靠海'),
]
DIALOGUE_RE = re.compile(
    r'(?:^|\s)(?:[a-zA-Z_][a-zA-Z_0-9]*\s+)?"([^"\n]{6,})"'
)
SKIP_FILE_NAMES = {
    "changelog.rpy", "attr_system.rpy", "images_def.rpy", "screens.rpy",
    "options.rpy", "gui.rpy", "_developer.rpy",
}


def _game_files(files: Sequence[Path] | None = None) -> list[Path]:
    if not GAME_DIR.is_dir():
        raise OSError("game directory is missing")
    candidates = sorted(GAME_DIR.glob("*.rpy")) if files is None else list(files)
    return [
        path
        for path in candidates
        if path.name not in SKIP_FILE_NAMES
    ]


def _short(text: str) -> str:
    return text if len(text) <= 120 else text[:117] + "..."


def scan_raw_lines(
    path: str | os.PathLike[str],
    patterns: list[tuple[str, str]],
) -> list[tuple[int, str, str]]:
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    hits: list[tuple[int, str, str]] = []
    for line_number, line in enumerate(lines, 1):
        if line.strip().startswith("#") or "canon-ok" in line:
            continue
        for pattern, message in patterns:
            if re.search(pattern, line):
                hits.append((line_number, message, _short(line.strip())))
    return hits


def scan_file_for_patterns(
    path: str | os.PathLike[str],
    patterns: list[tuple[str, str]],
) -> list[tuple[int, str, str]]:
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    hits: list[tuple[int, str, str]] = []
    for line_number, line in enumerate(lines, 1):
        if line.strip().startswith("#") or "canon-ok" in line:
            continue
        for match in DIALOGUE_RE.finditer(line):
            text = match.group(1)
            for pattern, message in patterns:
                if re.search(pattern, text):
                    hits.append((line_number, message, _short(text)))
                    break
    return hits


def collect_canon_word_occurrences(
    files: Sequence[str | os.PathLike[str]],
) -> dict[str, list[tuple[str, int]]]:
    locations: dict[str, list[tuple[str, int]]] = {
        word: [] for word in CANON_TRIGGER_WORDS
    }
    for raw_path in files:
        path = Path(raw_path)
        relative = path.relative_to(ROOT).as_posix()
        for line_number, line in enumerate(
            path.read_text(encoding="utf-8").splitlines(),
            1,
        ):
            if line.strip().startswith("#"):
                continue
            for word in CANON_TRIGGER_WORDS:
                if word in line:
                    locations[word].append((relative, line_number))
    return locations


def _findings(
    files: Sequence[Path],
    patterns: list[tuple[str, str]],
    rule: str,
    *,
    raw_lines: bool,
) -> list[dict[str, object]]:
    findings: list[dict[str, object]] = []
    scanner = scan_raw_lines if raw_lines else scan_file_for_patterns
    for path in files:
        relative = path.relative_to(ROOT).as_posix()
        for line_number, message, snippet in scanner(path, patterns):
            findings.append(
                {
                    "path": relative,
                    "line": line_number,
                    "rule": rule,
                    "message": f"{message}: {snippet}",
                }
            )
    return findings


def build_document(
    input_files: Sequence[Path] | None = None,
) -> dict[str, object]:
    files = _game_files(input_files)
    anti_logic = _findings(
        files, ANTI_LOGIC_PHRASES, "canon_anti_logic", raw_lines=False
    )
    geography = _findings(
        files, GEO_PATTERNS, "canon_geography", raw_lines=False
    )
    terminology = _findings(
        files, TERM_PATTERNS, "canon_terminology", raw_lines=True
    )
    canon_deviation = _findings(
        files, TYPO_PATTERNS, "canon_deviation", raw_lines=False
    )
    word_locations = collect_canon_word_occurrences(files)
    informational_occurrences = [
        {"term": word, "path": path, "line": line_number}
        for word in CANON_TRIGGER_WORDS
        for path, line_number in word_locations[word]
    ]
    blocking_count = sum(
        len(values)
        for values in (anti_logic, geography, terminology, canon_deviation)
    )
    return {
        "schema_version": 1,
        "tool": "canon",
        "blocking_count": blocking_count,
        "anti_logic": anti_logic,
        "geography": geography,
        "terminology": terminology,
        "canon_deviation": canon_deviation,
        "informational_occurrences": informational_occurrences,
    }


def _legacy_main() -> int:
    try:
        document = build_document()
    except (OSError, UnicodeError) as error:
        print(f"canon scan: {error}", file=sys.stderr)
        return 2
    labels = {
        "anti_logic": "反逻辑短语",
        "geography": "艾登堡地理",
        "terminology": "术语统一",
        "canon_deviation": "canon 偏差",
    }
    for category in ("anti_logic", "geography", "terminology", "canon_deviation"):
        print("=" * 60)
        print(labels[category])
        print("=" * 60)
        for finding in document[category]:
            print(
                f"{finding['path']}:{finding['line']}  "
                f"[{finding['rule']}]  {finding['message']}"
            )
        print(f"  -> {len(document[category])} 处")
    print("=" * 60)
    print("canon 触发词出现频次")
    print("=" * 60)
    by_term: dict[str, list[dict[str, object]]] = {}
    for occurrence in document["informational_occurrences"]:
        by_term.setdefault(occurrence["term"], []).append(occurrence)
    for term in CANON_TRIGGER_WORDS:
        values = by_term.get(term, [])
        if not values:
            continue
        print(f"  {term}: {len(values)} 处")
        for occurrence in values[:5]:
            print(f"    {occurrence['path']}:{occurrence['line']}")
        if len(values) > 5:
            print(f"    additional occurrences: {len(values) - 5}")
    print(f"\n=== 总结: {document['blocking_count']} 处阻断 finding ===")
    return 1 if document["blocking_count"] else 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--format", choices=("json",))
    parser.add_argument("--output")
    parser.add_argument("--inputs")
    return parser


def _structured_main(output: str, inputs: str) -> int:
    sink: StructuredJsonSink | None = None
    try:
        if not os.path.isabs(output):
            raise ValueError("--output must be absolute")
        if not os.path.isabs(inputs):
            raise ValueError("--inputs must be absolute")
        sink = StructuredJsonSink.claim(output)
        with validated_winter_narrative_inputs(inputs, ROOT) as inventory:
            document = build_document(inventory.rpy_files)
        sink.write(document)
        sink.close()
        sink = None
        return 1 if document["blocking_count"] else 0
    except (
        OSError,
        StructuredOutputError,
        TypeError,
        UnicodeError,
        ValueError,
        WinterNarrativeInputError,
    ) as error:
        print(f"canon evidence: {error}", file=sys.stderr)
        return 2
    finally:
        if sink is not None:
            try:
                sink.close()
            except OSError as close_error:
                print(f"canon evidence close: {close_error}", file=sys.stderr)


def main(argv: Sequence[str] | None = None) -> int:
    arguments = build_parser().parse_args(argv)
    if (
        arguments.format is None
        and arguments.output is None
        and arguments.inputs is None
    ):
        return _legacy_main()
    if (
        arguments.format != "json"
        or arguments.output is None
        or arguments.inputs is None
    ):
        print(
            "canon evidence: JSON mode requires --format json --output ABS "
            "--inputs ABS",
            file=sys.stderr,
        )
        return 2
    return _structured_main(arguments.output, arguments.inputs)


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Select the immutable inventory for the canon step**

In `Get-NarrativeGateManifest`, replace the complete canon entry with:

```powershell
        (New-GateStep 'canon' 'Python' `
            $script:PythonIdentity.FinalPath `
            ([string[]]@(
                '-B', $canon,
                '--inputs', $narrativeInputs,
                '--format', 'json',
                '--output', $canonJson
            )) $ToolTimeoutSeconds 'canon-json' `
            ([string[]]@(
                $canon,
                $structuredWriter,
                $narrativeInputsModule
            )) -InventoryPath $narrativeInputs)
```

The JSON producer receives the absolute inventory path, while the native
four-argument overload retains that inventory and every listed R input through
child drain. The P entries are parsed and membership-checked but are not file
handles because portrait basenames, not PNG bytes, are canon evidence inputs.
Do not change the output path, timeout, or postcondition.

In `expected_narrative_arguments`, define:

```python
inputs = project / "Tools" / "winter_narrative_inputs.txt"
```

Replace its canon argv entry with:

```python
[
    "-B",
    str(project / "Tools" / "scan_canon.py"),
    "--inputs",
    str(inputs),
    "--format",
    "json",
    "--output",
    str(canon),
]
```

- [ ] **Step 5: Run focused GREEN, verify the static catalog, stage exactly, and commit**

```powershell
python -m unittest Tools.test_winter_narrative_capabilities.CanonJsonProducerTests -v
if ($LASTEXITCODE -ne 0) { throw 'Canon JSON focused GREEN failed.' }
@'
import unittest

module_loader = unittest.TestLoader()
module_suite = module_loader.loadTestsFromName(
    "Tools.test_winter_narrative_capabilities"
)
repository_loader = unittest.TestLoader()
repository_suite = repository_loader.discover(start_dir="Tools")
if module_loader.errors != [] or repository_loader.errors != []:
    raise SystemExit(
        "static unittest loading errors: "
        + repr(module_loader.errors + repository_loader.errors)
    )
counts = (module_suite.countTestCases(), repository_suite.countTestCases())
expected = (15, 354)
if counts != expected:
    raise SystemExit(f"unexpected static unittest counts: {counts!r}")
print({"capability": counts[0], "discovery": counts[1], "loader_errors": 0})
'@ | python -
if ($LASTEXITCODE -ne 0) { throw 'Canon static test catalog failed.' }
$expected = [string[]]@(
  'Tools/Run-WinterInterludeGate.ps1',
  'Tools/scan_canon.py',
  'Tools/test_winter_interlude_gate.py',
  'Tools/test_winter_narrative_capabilities.py'
)
git diff --cached --quiet
if ($LASTEXITCODE -ne 0) { throw 'Canon slice started with a nonempty index.' }
git add -- $expected
$actual = [string[]]@(git diff --cached --name-only)
if (@(Compare-Object ($expected | Sort-Object) ($actual | Sort-Object)).Count -ne 0) {
  throw "Unexpected canon slice paths: $($actual -join ', ')"
}
git diff --cached --check
if ($LASTEXITCODE -ne 0) { throw 'Canon staged diff check failed.' }
git commit -m "feat: publish strict canon evidence"
if ($LASTEXITCODE -ne 0) { throw 'Canon slice commit failed.' }
if ((git log -1 --pretty=%s).Trim() -cne 'feat: publish strict canon evidence') {
  throw 'Unexpected canon commit subject.'
}
if (git status --short) { throw 'Canon commit left a dirty worktree.' }
```

Expected focused GREEN: `Ran 5 tests`, `OK`. Expected static catalog:
capability module 15 methods, `Tools` discovery 354 methods, and both loader
error lists exactly empty; no cumulative module or repository test body runs at
this intermediate SHA. The public gate module remains 87 tests and the real
Narrative manifest still fails validation before launching a child because the
show-before producer does not yet exist.

**Asset audit:** Tooling only. Art, music, SFX, portraits, animation, UI,
font, old-game, shipping source, and package size are unchanged.

---

## Task 4: Add scoped portrait JSON without repository-report writes

**Files:**

- Modify: `Tools/test_winter_narrative_capabilities.py`
- Modify: `scan_missing_portraits.py`
- Modify: `Tools/Run-WinterInterludeGate.ps1`
- Modify: `Tools/test_winter_interlude_gate.py`

JSON mode scans exactly one existing direct child of `game`, reports missing
shows, missing assets, and unregistered shown tags, and writes only through the
shared sink. No-argument mode remains the only mode allowed to refresh the
three historical repository reports.

- [ ] **Step 1: Add the five complete portrait tests**

Append this class to `Tools/test_winter_narrative_capabilities.py`:

```python
class PortraitJsonProducerTests(unittest.TestCase):
    def test_portrait_json_cli_emits_exact_scoped_schema(self) -> None:
        self.assertTrue(PRODUCERS["portrait"].is_file())
        source = PRODUCERS["portrait"].read_text(encoding="utf-8")
        with tempfile.TemporaryDirectory(prefix="winter-portrait-schema-") as raw:
            game_files = _portrait_game_files(
                "label winter_fixture:\n"
                "    scene bg study\n"
                "    show alice_img at left\n"
                '    alice "Hello."\n'
            )
            game_files["intruder.rpy"] = (
                'define rogue = Character("Rogue", image="rogue")\n'
            )
            project = _make_producer_project(
                raw,
                "scan_missing_portraits.py",
                game_files,
                ("alice.png", "rogue.png"),
            )
            target = project / "game" / "governance_winter_interlude.rpy"
            output = project / "portrait.json"
            inputs = project / "Tools" / "winter_narrative_inputs.txt"
            completed = _run_json_producer(
                project,
                "scan_missing_portraits.py",
                ["--file", str(target)],
                output,
                inherited_handle=True,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertTrue(output.is_file())
            try:
                document = json.loads(output.read_text(encoding="utf-8"))
            except (UnicodeError, json.JSONDecodeError) as error:
                self.fail(f"portrait producer did not emit valid JSON: {error}")
            _assert_common_document(
                self,
                document,
                tool="missing_portraits",
                scanned_files=["game/governance_winter_interlude.rpy"],
            )
            self.assertEqual(document["blocking_count"], 0)

            inventory_call = (
                "portrait_files = list_portrait_files("
                "paths=inventory.portrait_files)"
            )
            self.assertEqual(source.count(inventory_call), 1)
            iterator_mutant = source.replace(
                inventory_call,
                "portrait_files = list_portrait_files()",
                1,
            )
            with self.assertRaises(AssertionError):
                self.assertEqual(iterator_mutant.count(inventory_call), 1)

            real_namespace = _exec_producer_source(
                PRODUCERS["portrait"],
                source,
                "_winter_portrait_real",
            )

            def assert_inventory_projections(
                namespace: dict[str, object],
            ) -> None:
                definitions = namespace["collect_character_defs"](
                    project / "game",
                    (project / "game" / "characters.rpy",),
                )
                self.assertEqual(set(definitions), {"alice", "bob"})
                portraits = namespace["list_portrait_files"](
                    project / "game" / "images",
                    (project / "game" / "images" / "alice.png",),
                )
                self.assertEqual(portraits, {"alice"})

            assert_inventory_projections(real_namespace)
            definition_seam = (
                '    sources = sorted(game_dir.glob("*.rpy")) '
                "if paths is None else list(paths)\n"
            )
            self.assertEqual(source.count(definition_seam), 1)
            definition_mutant = _exec_producer_source(
                PRODUCERS["portrait"],
                source.replace(
                    definition_seam,
                    '    sources = sorted(game_dir.glob("*.rpy"))\n',
                    1,
                ),
                "_winter_portrait_glob_mutant",
            )
            with self.assertRaises(AssertionError):
                assert_inventory_projections(definition_mutant)

            portrait_seam = (
                "    if paths is not None:\n"
                "        return {path.stem for path in paths}\n"
            )
            self.assertEqual(source.count(portrait_seam), 1)
            portrait_mutant = _exec_producer_source(
                PRODUCERS["portrait"],
                source.replace(
                    portrait_seam,
                    (
                        "    if paths is not None:\n"
                        "        return {\n"
                        "            path.stem for path in images_dir.iterdir()\n"
                        "            if path.is_file()\n"
                        "            and path.suffix.lower() == '.png'\n"
                        "        }\n"
                    ),
                    1,
                ),
                "_winter_portrait_iterdir_mutant",
            )
            with self.assertRaises(AssertionError):
                assert_inventory_projections(portrait_mutant)

            (project / "game" / "images" / "unlisted.png").write_bytes(
                b"temporary"
            )
            drift_output = project / "portrait-drift.json"
            drift = _run_json_producer(
                project,
                "scan_missing_portraits.py",
                ["--file", str(target)],
                drift_output,
                inherited_handle=False,
            )
            self.assertEqual(drift.returncode, 2)
            _assert_no_valid_json(self, drift_output)

    def test_portrait_missing_show_and_unregistered_tag_are_blocking(self) -> None:
        with tempfile.TemporaryDirectory(prefix="winter-portrait-findings-") as raw:
            project = _make_producer_project(
                raw,
                "scan_missing_portraits.py",
                _portrait_game_files(
                    "label winter_fixture:\n"
                    "    scene bg study\n"
                    '    alice "Missing show."\n'
                    '    bob "Missing asset."\n'
                    "    show rogue_img at left\n"
                ),
                ("alice.png",),
            )
            target = project / "game" / "governance_winter_interlude.rpy"
            output = project / "portrait-findings.json"
            completed = _run_json_producer(
                project,
                "scan_missing_portraits.py",
                ["--file", str(target)],
                output,
                inherited_handle=False,
            )
            self.assertEqual(completed.returncode, 1, completed.stderr)
            document = json.loads(output.read_text(encoding="utf-8"))
            _assert_common_document(
                self,
                document,
                tool="missing_portraits",
                scanned_files=["game/governance_winter_interlude.rpy"],
            )
            self.assertEqual(document["blocking_count"], 3)
            self.assertEqual(
                {(item["line"], item["rule"]) for item in document["findings"]},
                {
                    (3, "missing_portrait_show"),
                    (4, "missing_portrait_asset"),
                    (5, "unregistered_portrait_tag"),
                },
            )

    def test_portrait_json_mode_never_writes_repository_reports_or_accepts_output_dir(self) -> None:
        with tempfile.TemporaryDirectory(prefix="winter-portrait-reports-") as raw:
            project = _make_producer_project(
                raw,
                "scan_missing_portraits.py",
                _portrait_game_files(
                    "label winter_fixture:\n"
                    "    scene bg study\n"
                    '    alice "Missing show."\n'
                ),
                ("alice.png",),
            )
            sentinels: dict[Path, bytes] = {}
            for name in REPORT_NAMES:
                path = project / name
                content = ("sentinel:" + name).encode("utf-8")
                path.write_bytes(content)
                sentinels[path] = content
            target = project / "game" / "governance_winter_interlude.rpy"
            output = project / "portrait.json"
            inputs = project / "Tools" / "winter_narrative_inputs.txt"
            completed = _run_json_producer(
                project,
                "scan_missing_portraits.py",
                ["--file", str(target)],
                output,
                inherited_handle=False,
            )
            self.assertEqual(completed.returncode, 1, completed.stderr)
            for path, content in sentinels.items():
                self.assertEqual(path.read_bytes(), content)

            invalid = _run_producer(
                project,
                "scan_missing_portraits.py",
                [
                    "--file", str(target), "--format", "json",
                    "--output-dir", str(project / "evidence"),
                    "--inputs", str(inputs),
                ],
            )
            self.assertEqual(invalid.returncode, 2)
            self.assertFalse((project / "evidence").exists())
            for path, content in sentinels.items():
                self.assertEqual(path.read_bytes(), content)

            missing_inputs_output = project / "missing-inputs.json"
            missing_inputs = _run_producer(
                project,
                "scan_missing_portraits.py",
                [
                    "--file", str(target), "--format", "json",
                    "--output", str(missing_inputs_output),
                ],
            )
            self.assertEqual(missing_inputs.returncode, 2)
            self.assertFalse(missing_inputs_output.exists())

            relative_inputs_output = project / "relative-inputs.json"
            relative_inputs = _run_producer(
                project,
                "scan_missing_portraits.py",
                [
                    "--file", str(target), "--format", "json",
                    "--output", str(relative_inputs_output),
                    "--inputs", "Tools/winter_narrative_inputs.txt",
                ],
            )
            self.assertEqual(relative_inputs.returncode, 2)
            self.assertFalse(relative_inputs_output.exists())

    def test_portrait_missing_or_outside_target_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory(prefix="winter-portrait-scope-") as raw:
            project = _make_producer_project(
                raw,
                "scan_missing_portraits.py",
                _portrait_game_files("label clean:\n    scene bg study\n"),
                ("alice.png",),
            )
            outside = project / "outside.rpy"
            outside.write_text("label outside:\n", encoding="utf-8")
            prefixed_parent = project / "game-shadow"
            prefixed_parent.mkdir()
            prefixed = prefixed_parent / "outside.rpy"
            prefixed.write_text("label prefixed:\n", encoding="utf-8")
            targets = (
                project / "game" / "missing.rpy",
                outside,
                prefixed,
            )
            for index, target in enumerate(targets):
                with self.subTest(target=str(target)):
                    output = project / f"invalid-{index}.json"
                    completed = _run_json_producer(
                        project,
                        "scan_missing_portraits.py",
                        ["--file", str(target)],
                        output,
                        inherited_handle=False,
                    )
                    self.assertEqual(completed.returncode, 2)
                    _assert_no_valid_json(self, output)

    def test_portrait_no_argument_legacy_mode_preserves_reports_and_exit_contract(self) -> None:
        with tempfile.TemporaryDirectory(prefix="winter-portrait-legacy-") as raw:
            project = _make_producer_project(
                raw,
                "scan_missing_portraits.py",
                _portrait_game_files(
                    "label winter_fixture:\n"
                    "    scene bg study\n"
                    '    alice "Missing show."\n'
                    '    bob "Missing asset."\n'
                    "    show rogue_img at left\n"
                ),
                ("alice.png",),
            )
            completed = _run_producer(project, "scan_missing_portraits.py", [])
            self.assertEqual(completed.returncode, 1, completed.stderr)
            self.assertIn("Reports:", completed.stdout)
            for name in REPORT_NAMES:
                self.assertTrue((project / name).is_file(), name)
            legacy = json.loads(
                (project / "missing_portraits_full.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual(set(legacy), {"char_map", "class_a", "class_b"})
            self.assertEqual(
                {item["speaker"] for item in legacy["class_a"]},
                {"alice"},
            )
            self.assertEqual(
                {item["speaker"] for item in legacy["class_b"]},
                {"bob"},
            )
```

- [ ] **Step 2: Take the one-behavior portrait RED**

```powershell
$red = & python -m unittest Tools.test_winter_narrative_capabilities.PortraitJsonProducerTests.test_portrait_json_cli_emits_exact_scoped_schema -v 2>&1
$redExit = $LASTEXITCODE
$red | Set-Content -LiteralPath .superpowers/sdd/task8-portrait-json-red.txt -Encoding UTF8
if ($redExit -eq 0) { throw 'Portrait JSON RED unexpectedly passed.' }
$joined = $red -join [Environment]::NewLine
if ($joined -notmatch 'Ran 1 test' -or
    $joined -notmatch 'FAILED \(failures=1\)' -or
    $joined -match '(?m)^ERROR:') {
  throw 'Portrait JSON RED did not fail only on absent structured output.'
}
```

Expected RED: one failure because legacy mode ignores the JSON arguments and
does not create the reserved document; zero errors.

- [ ] **Step 3: Replace `scan_missing_portraits.py` with the complete dual-mode producer**

Replace the file with exactly:

```python
from __future__ import annotations

import argparse
import ctypes
import json
import os
import re
import sys
from collections import defaultdict
from collections.abc import Sequence
from ctypes import wintypes
from pathlib import Path

from Tools.winter_narrative_inputs import (
    WinterNarrativeInputError,
    WinterNarrativeInputs,
    validated_winter_narrative_inputs,
)
from Tools.winter_narrative_json import StructuredJsonSink, StructuredOutputError


ROOT = Path(__file__).resolve().parent
GAME_DIR = ROOT / "game"
IMAGES_DIR = GAME_DIR / "images"
SHOW_IMG_RE = re.compile(r"\bshow\s+(\w+_img)\b")
CHAR_DEF_RE = re.compile(r"^\s*define\s+(\w+)\s*=\s*Character\s*\((.*)\)\s*$")
IMAGE_PARAM_RE = re.compile(r"image\s*=\s*[\"']([\w_]+)[\"']")
MANUAL_IMG_TAG = {
    "tax_collector": "tax_collector",
    "farmer_rep": "farmer_rep",
    "merchant_guild": "merchant_guild",
    "healer": "healer",
    "village_elder": "village_elder",
}
PLAYER_TAGS = {
    "player_char_img", "player_child_img", "player_teen_img", "player_young_img"
}
NO_PORTRAIT_CHARS = {"crowd"}
LABEL_RE = re.compile(r"^(\s*)label\s+(\w+)\s*(\([^)]*\))?\s*:\s*$")
SCENE_RE = re.compile(r"^(\s*)scene\b")
SHOW_RE = re.compile(r"^(\s*)show\s+(\w+)(?:\s+(.*))?$")
HIDE_RE = re.compile(r"^(\s*)hide\s+(\w+)")
HIDE_ALL_RE = re.compile(r"^(\s*)\$\s*hide_all_chars\s*\((.*)\)")
COMMENT_RE = re.compile(r"^\s*#")
EMPTY_RE = re.compile(r"^\s*$")
DIALOGUE_RE = re.compile(r'^(\s*)(\w+)\s+"((?:[^"\\]|\\.)*)"(\s+.*)?$')
IF_RE = re.compile(r"^(\s*)if\s+.*:\s*(#.*)?$")
ELIF_RE = re.compile(r"^(\s*)elif\s+.*:\s*(#.*)?$")
ELSE_RE = re.compile(r"^(\s*)else\s*:\s*(#.*)?$")
MENU_RE = re.compile(r"^(\s*)menu\s*(\w+)?\s*:\s*(#.*)?$")
MENU_OPT_RE = re.compile(r'^(\s*)"((?:[^"\\]|\\.)*)"(\s*\([^)]*\))?\s*:\s*(#.*)?$')
LEADING_WS_RE = re.compile(r"^(\s*)")
REGISTRY_RE = re.compile(r"CHAR_IMG_TAGS\s*=\s*\[(.*?)\]", re.S)
REGISTRY_TAG_RE = re.compile(r"[\"'](\w+_img)[\"']")
REPORT_NAMES = (
    "missing_portraits_A.txt",
    "missing_portraits_B.txt",
    "missing_portraits_full.json",
)


def find_unregistered_shows(
    lines: Sequence[str],
    registered: set[str],
) -> list[tuple[int, str]]:
    bad: list[tuple[int, str]] = []
    for line_number, line in enumerate(lines, 1):
        if line.lstrip().startswith("#"):
            continue
        for tag in SHOW_IMG_RE.findall(line):
            if tag not in registered:
                bad.append((line_number, tag))
    return bad


def collect_character_defs(
    game_dir: Path = GAME_DIR,
    paths: Sequence[Path] | None = None,
) -> dict[str, tuple[str | None, str, int]]:
    definitions: dict[str, tuple[str | None, str, int]] = {}
    sources = sorted(game_dir.glob("*.rpy")) if paths is None else list(paths)
    for path in sources:
        if path.name.endswith(".bak"):
            continue
        with path.open("r", encoding="utf-8") as handle:
            for line_number, line in enumerate(handle, 1):
                match = CHAR_DEF_RE.match(line)
                if match is None:
                    continue
                short, arguments = match.group(1), match.group(2)
                image_match = IMAGE_PARAM_RE.search(arguments)
                if image_match is not None:
                    image_tag = image_match.group(1)
                elif short in MANUAL_IMG_TAG:
                    image_tag = MANUAL_IMG_TAG[short]
                else:
                    image_tag = None
                definitions[short] = (image_tag, path.name, line_number)
    return definitions


def list_portrait_files(
    images_dir: Path = IMAGES_DIR,
    paths: Sequence[Path] | None = None,
) -> set[str]:
    if paths is not None:
        return {path.stem for path in paths}
    if not images_dir.is_dir():
        return set()
    return {
        path.stem
        for path in images_dir.iterdir()
        if path.is_file() and path.suffix.lower() == ".png"
    }


def indent_of(line: str) -> int:
    match = LEADING_WS_RE.match(line)
    if match is None:
        return 0
    return len(match.group(1))


class State:
    def __init__(self) -> None:
        self.active: set[str] = set()

    def copy(self) -> "State":
        copied = State()
        copied.active = set(self.active)
        return copied


def _is_first_option(block: dict[str, object], current: State) -> bool:
    exits = block["branch_exit_states"]
    entry = block["entry_state"]
    return not exits and current.active == entry.active


def scan_file(
    path: str | os.PathLike[str],
    char_map: dict[str, tuple[str | None, str, int]],
) -> list[dict[str, object]]:
    with open(path, "r", encoding="utf-8") as handle:
        lines = handle.readlines()
    findings: list[dict[str, object]] = []
    current_label: str | None = None
    tracking = False
    state = State()
    block_stack: list[dict[str, object]] = []

    def close_blocks_up_to(target_indent: int) -> None:
        nonlocal state
        while block_stack and int(block_stack[-1]["indent"]) > target_indent:
            block = block_stack.pop()
            exits = block["branch_exit_states"]
            exits.append(state.copy())
            merged: set[str] = set()
            for exit_state in exits:
                merged |= exit_state.active
            if block["type"] == "if" and not block.get("has_else"):
                merged |= block["entry_state"].active
            state = State()
            state.active = merged

    for line_number, raw in enumerate(lines, 1):
        line = raw.rstrip("\n")
        if EMPTY_RE.match(line) or COMMENT_RE.match(line):
            continue
        current_indent = indent_of(line)
        close_blocks_up_to(current_indent)
        match = LABEL_RE.match(line)
        if match is not None:
            current_label = match.group(2)
            tracking = False
            state = State()
            block_stack = []
            continue
        match = IF_RE.match(line)
        if match is not None:
            header_indent = len(match.group(1))
            block_stack.append(
                {
                    "header_indent": header_indent,
                    "indent": header_indent + 1,
                    "type": "if",
                    "entry_state": state.copy(),
                    "branch_exit_states": [],
                    "has_else": False,
                }
            )
            continue
        match = ELIF_RE.match(line)
        if match is not None:
            if (
                block_stack
                and block_stack[-1]["type"] == "if"
                and block_stack[-1]["header_indent"] == len(match.group(1))
            ):
                block_stack[-1]["branch_exit_states"].append(state.copy())
                state = block_stack[-1]["entry_state"].copy()
            continue
        match = ELSE_RE.match(line)
        if match is not None:
            if (
                block_stack
                and block_stack[-1]["type"] == "if"
                and block_stack[-1]["header_indent"] == len(match.group(1))
            ):
                block_stack[-1]["branch_exit_states"].append(state.copy())
                state = block_stack[-1]["entry_state"].copy()
                block_stack[-1]["has_else"] = True
            continue
        match = MENU_RE.match(line)
        if match is not None:
            header_indent = len(match.group(1))
            block_stack.append(
                {
                    "header_indent": header_indent,
                    "indent": header_indent + 1,
                    "type": "menu",
                    "entry_state": state.copy(),
                    "branch_exit_states": [],
                    "has_else": True,
                }
            )
            continue
        match = MENU_OPT_RE.match(line)
        if match is not None and block_stack and block_stack[-1]["type"] == "menu":
            option_indent = len(match.group(1))
            if option_indent > int(block_stack[-1]["header_indent"]):
                if (
                    block_stack[-1]["branch_exit_states"]
                    or not _is_first_option(block_stack[-1], state)
                ):
                    block_stack[-1]["branch_exit_states"].append(state.copy())
                state = block_stack[-1]["entry_state"].copy()
                block_stack[-1]["indent"] = option_indent
                continue
        if SCENE_RE.match(line):
            tracking = True
            state.active = set()
            continue
        match = HIDE_ALL_RE.match(line)
        if match is not None:
            tracking = True
            keep = {
                token.strip().strip('"').strip("'")
                for token in match.group(2).split(",")
                if token.strip().strip('"').strip("'")
            }
            state.active &= keep
            continue
        match = SHOW_RE.match(line)
        if match is not None:
            tag = match.group(2)
            if tag not in {"screen", "black"} and not tag.startswith("bg"):
                tracking = True
                state.active.add(tag)
            continue
        match = HIDE_RE.match(line)
        if match is not None:
            tag = match.group(2)
            if tag != "screen":
                tracking = True
                state.active.discard(tag)
            continue
        match = DIALOGUE_RE.match(line)
        if match is None:
            continue
        speaker = match.group(2)
        text = match.group(3)
        if speaker not in char_map:
            continue
        expected_image = char_map[speaker][0]
        if expected_image is None or not tracking:
            continue
        if speaker == "player":
            if any(tag in state.active for tag in PLAYER_TAGS):
                continue
            expected_tag = "player_*_img"
        else:
            expected_tag = expected_image + "_img"
            if expected_tag in state.active:
                continue
        findings.append(
            {
                "file": Path(path).name,
                "line": line_number,
                "label": current_label,
                "speaker": speaker,
                "expected_tag": expected_tag,
                "text": text[:80],
            }
        )
    return findings


def _registered_tags(game_dir: Path = GAME_DIR) -> set[str]:
    source = (game_dir / "char_helpers.rpy").read_text(encoding="utf-8")
    match = REGISTRY_RE.search(source)
    if match is None:
        raise ValueError("CHAR_IMG_TAGS registry is missing")
    return set(REGISTRY_TAG_RE.findall(match.group(1)))


def _classify_findings(
    raw_findings: list[dict[str, object]],
    portrait_files: set[str],
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    class_a: list[dict[str, object]] = []
    class_b: list[dict[str, object]] = []
    for finding in raw_findings:
        expected = str(finding["expected_tag"])
        base = (
            "player_char"
            if "player_*" in expected
            else expected[:-4] if expected.endswith("_img") else expected
        )
        finding["has_file"] = base in portrait_files
        (class_a if finding["has_file"] else class_b).append(finding)
    return class_a, class_b


def _ordinal_ignore_case_equal(left: str, right: str) -> bool:
    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    compare = kernel32.CompareStringOrdinal
    compare.argtypes = (
        wintypes.LPCWSTR,
        ctypes.c_int,
        wintypes.LPCWSTR,
        ctypes.c_int,
        wintypes.BOOL,
    )
    compare.restype = ctypes.c_int
    result = int(compare(left, -1, right, -1, True))
    if result == 0:
        raise ctypes.WinError(ctypes.get_last_error())
    return result == 2


def _validate_direct_game_file(raw_path: str) -> tuple[Path, str]:
    if not os.path.isabs(raw_path):
        raise ValueError("--file must be absolute")
    game_dir = GAME_DIR.resolve(strict=True)
    target = Path(raw_path).resolve(strict=True)
    if not target.is_file() or target.suffix.lower() != ".rpy":
        raise ValueError("--file must name an existing regular .rpy file")
    if not _ordinal_ignore_case_equal(str(target.parent), str(game_dir)):
        raise ValueError("--file must have game as its exact direct parent")
    return target, f"game/{target.name}"


def _structured_document(
    target: Path,
    relative_path: str,
    inventory: WinterNarrativeInputs,
) -> dict[str, object]:
    char_map = collect_character_defs(paths=inventory.rpy_files)
    portrait_files = list_portrait_files(paths=inventory.portrait_files)
    raw_findings = scan_file(target, char_map)
    class_a, class_b = _classify_findings(raw_findings, portrait_files)
    findings: list[dict[str, object]] = []
    for finding in class_a:
        findings.append(
            {
                "path": relative_path,
                "line": int(finding["line"]),
                "rule": "missing_portrait_show",
                "message": (
                    f"speaker {finding['speaker']!r} requires active "
                    f"portrait {finding['expected_tag']!r}"
                ),
            }
        )
    for finding in class_b:
        findings.append(
            {
                "path": relative_path,
                "line": int(finding["line"]),
                "rule": "missing_portrait_asset",
                "message": (
                    f"speaker {finding['speaker']!r} has no portrait asset "
                    f"for {finding['expected_tag']!r}"
                ),
            }
        )
    registered = _registered_tags()
    lines = target.read_text(encoding="utf-8").splitlines()
    for line_number, tag in find_unregistered_shows(lines, registered):
        findings.append(
            {
                "path": relative_path,
                "line": line_number,
                "rule": "unregistered_portrait_tag",
                "message": f"shown portrait tag {tag!r} is absent from CHAR_IMG_TAGS",
            }
        )
    findings.sort(key=lambda item: (int(item["line"]), str(item["rule"])))
    return {
        "schema_version": 1,
        "tool": "missing_portraits",
        "scanned_files": [relative_path],
        "blocking_count": len(findings),
        "findings": findings,
    }


def check_char_img_registry(game_dir: Path = GAME_DIR) -> int:
    registered = _registered_tags(game_dir)
    bad: list[tuple[str, int, str]] = []
    for path in sorted(game_dir.glob("*.rpy")):
        lines = path.read_text(encoding="utf-8").splitlines()
        for line_number, tag in find_unregistered_shows(lines, registered):
            bad.append((path.name, line_number, tag))
    if bad:
        print("\n!! 未注册进 CHAR_IMG_TAGS 却被 show 的立绘:")
        for file_name, line_number, tag in bad:
            print(f"   {file_name}:{line_number}  {tag}")
    else:
        print("\nCHAR_IMG_TAGS 注册闸门: 0 处未注册")
    return len(bad)


def _legacy_main() -> int:
    try:
        char_map = collect_character_defs()
        portrait_files = list_portrait_files()
        all_findings: list[dict[str, object]] = []
        for path in sorted(GAME_DIR.glob("*.rpy")):
            all_findings.extend(scan_file(path, char_map))
        class_a, class_b = _classify_findings(all_findings, portrait_files)
        print(f"=== Total findings: {len(all_findings)} ===")
        print(f"Class A (has portrait file, missing show): {len(class_a)}")
        print(f"Class B (no portrait file):                {len(class_b)}")
        grouped: dict[tuple[str, object], list[dict[str, object]]] = defaultdict(list)
        for item in class_a:
            grouped[(str(item["file"]), item["label"])].append(item)
        with (ROOT / REPORT_NAMES[0]).open("w", encoding="utf-8", newline="\n") as handle:
            handle.write(f"A类 — 有立绘文件但缺show指令 ({len(class_a)}处)\n")
            handle.write("=" * 70 + "\n\n")
            ordered_groups = sorted(
                grouped.items(),
                key=lambda entry: (entry[0][0], str(entry[0][1])),
            )
            for (file_name, label), items in ordered_groups:
                handle.write(f"## {file_name} · label: {label}  ({len(items)}处)\n")
                for item in items:
                    handle.write(
                        f"  L{item['line']:<5} {item['speaker']} 需要 "
                        f"{item['expected_tag']}\n         > {item['text']}\n"
                    )
                handle.write("\n")
        with (ROOT / REPORT_NAMES[1]).open("w", encoding="utf-8", newline="\n") as handle:
            handle.write(f"B类 — 没有立绘文件 ({len(class_b)}处)\n")
            handle.write("=" * 70 + "\n")
            for item in class_b:
                handle.write(
                    f"{item['file']}:{item['line']}  [label: {item['label']}]  "
                    f"{item['speaker']} ({item['expected_tag']})\n"
                    f"    > {item['text']}\n"
                )
        with (ROOT / REPORT_NAMES[2]).open("w", encoding="utf-8", newline="\n") as handle:
            json.dump(
                {
                    "char_map": {
                        key: {"image_tag": value[0], "src": f"{value[1]}:{value[2]}"}
                        for key, value in char_map.items()
                    },
                    "class_a": class_a,
                    "class_b": class_b,
                },
                handle,
                ensure_ascii=False,
                indent=2,
            )
            handle.write("\n")
        print("\nReports: missing_portraits_A.txt, missing_portraits_B.txt, missing_portraits_full.json")
        unregistered = check_char_img_registry()
        return 1 if all_findings or unregistered else 0
    except (OSError, TypeError, UnicodeError, ValueError) as error:
        print(f"portrait scan: {error}", file=sys.stderr)
        return 2


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--file")
    parser.add_argument("--format", choices=("json",))
    parser.add_argument("--output")
    parser.add_argument("--inputs")
    return parser


def _structured_main(arguments: argparse.Namespace) -> int:
    sink: StructuredJsonSink | None = None
    try:
        if not os.path.isabs(arguments.output):
            raise ValueError("--output must be absolute")
        if not os.path.isabs(arguments.inputs):
            raise ValueError("--inputs must be absolute")
        target, relative_path = _validate_direct_game_file(arguments.file)
        sink = StructuredJsonSink.claim(arguments.output)
        with validated_winter_narrative_inputs(
            arguments.inputs,
            ROOT,
        ) as inventory:
            if target not in inventory.rpy_files:
                raise ValueError("--file is absent from the pinned inventory")
            document = _structured_document(target, relative_path, inventory)
        sink.write(document)
        sink.close()
        sink = None
        return 1 if document["blocking_count"] else 0
    except (
        OSError,
        StructuredOutputError,
        TypeError,
        UnicodeError,
        ValueError,
        WinterNarrativeInputError,
    ) as error:
        print(f"portrait evidence: {error}", file=sys.stderr)
        return 2
    finally:
        if sink is not None:
            try:
                sink.close()
            except OSError as close_error:
                print(f"portrait evidence close: {close_error}", file=sys.stderr)


def main(argv: Sequence[str] | None = None) -> int:
    arguments = build_parser().parse_args(argv)
    structured_values = (
        arguments.file,
        arguments.format,
        arguments.output,
        arguments.inputs,
    )
    if all(value is None for value in structured_values):
        return _legacy_main()
    if any(value is None for value in structured_values):
        print(
            "portrait evidence: JSON mode requires exactly "
            "--file ABS --format json --output ABS --inputs ABS",
            file=sys.stderr,
        )
        return 2
    return _structured_main(arguments)


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Register exact portrait runtime dependencies**

In `Get-NarrativeGateManifest`, immediately after resolving `$target`, add:

```powershell
    $characters = Get-ExpectedProjectFilePath $project 'game\characters.rpy'
    $charHelpers = Get-ExpectedProjectFilePath $project 'game\char_helpers.rpy'
```

Replace the complete portrait entry with:

```powershell
        (New-GateStep 'missing-portraits' 'Python' `
            $script:PythonIdentity.FinalPath `
            ([string[]]@(
                '-B', $portrait,
                '--file', $target,
                '--inputs', $narrativeInputs,
                '--format', 'json',
                '--output', $portraitJson
            )) $ToolTimeoutSeconds 'portrait-json' `
            ([string[]]@(
                $portrait,
                $structuredWriter,
                $narrativeInputsModule,
                $target,
                $characters,
                $charHelpers
            )) -InventoryPath $narrativeInputs)
```

Do not add `--output-dir`; the exact direct output file remains the registered
portrait child under gate evidence.

In `expected_narrative_arguments`, replace its portrait argv entry with:

```python
[
    "-B",
    str(project / "scan_missing_portraits.py"),
    "--file",
    str(target),
    "--inputs",
    str(inputs),
    "--format",
    "json",
    "--output",
    str(portrait),
]
```

In `_GateFixture.__init__`, replace the complete Task 2 `fixed_files` tuple
with:

```python
fixed_files = (
    "Tools/test_governance_winter_interlude.py",
    "Tools/test_winter_narrative_capabilities.py",
    "Tools/winter_narrative_json.py",
    "Tools/winter_narrative_inputs.py",
    "Tools/winter_narrative_inputs.txt",
    "Tools/check_winter_narrative_capabilities.py",
    "Tools/scan_canon.py",
    "Tools/scan_ai_smell.py",
    "scan_missing_portraits.py",
    "scan_narration_overlap.py",
    "Tools/scan_show_before_prevention.py",
    "Tools/scan_nested_quotes.py",
    "game/characters.rpy",
    "game/char_helpers.rpy",
    "game/governance_winter_interlude.rpy",
)
```

Immediately after the loop that writes those fixed files, overwrite the fake
inventory with its Task 4 direct membership:

```python
(self.tools / "winter_narrative_inputs.txt").write_text(
    "WINTER_NARRATIVE_INPUTS_V1\tR=3\tP=0\n"
    "R\tgame/char_helpers.rpy\n"
    "R\tgame/characters.rpy\n"
    "R\tgame/governance_winter_interlude.rpy\n",
    encoding="utf-8",
    newline="\n",
)
```

This fixture edit is part of the same lease change. Without it, every
fake-project Narrative test would fail manifest validation before its intended
child behavior.

- [ ] **Step 5: Run focused GREEN, verify the static catalog, stage exactly, and commit**

```powershell
python -m unittest Tools.test_winter_narrative_capabilities.PortraitJsonProducerTests Tools.test_player_feedback_regressions.PortraitContractTests.test_unregistered_show_gate_uses_real_word_boundaries Tools.test_winter_interlude_gate.WinterInterludeGateCapabilityTests.test_valid_batch_capability_uses_full_stem_and_passes -v
if ($LASTEXITCODE -ne 0) { throw 'Portrait JSON focused GREEN failed.' }
@'
import unittest

module_loader = unittest.TestLoader()
module_suite = module_loader.loadTestsFromName(
    "Tools.test_winter_narrative_capabilities"
)
repository_loader = unittest.TestLoader()
repository_suite = repository_loader.discover(start_dir="Tools")
if module_loader.errors != [] or repository_loader.errors != []:
    raise SystemExit(
        "static unittest loading errors: "
        + repr(module_loader.errors + repository_loader.errors)
    )
counts = (module_suite.countTestCases(), repository_suite.countTestCases())
expected = (20, 359)
if counts != expected:
    raise SystemExit(f"unexpected static unittest counts: {counts!r}")
print({"capability": counts[0], "discovery": counts[1], "loader_errors": 0})
'@ | python -
if ($LASTEXITCODE -ne 0) { throw 'Portrait static test catalog failed.' }
$expected = [string[]]@(
  'Tools/Run-WinterInterludeGate.ps1',
  'Tools/test_winter_interlude_gate.py',
  'Tools/test_winter_narrative_capabilities.py',
  'scan_missing_portraits.py'
)
git diff --cached --quiet
if ($LASTEXITCODE -ne 0) { throw 'Portrait slice started with a nonempty index.' }
git add -- $expected
$actual = [string[]]@(git diff --cached --name-only)
if (@(Compare-Object ($expected | Sort-Object) ($actual | Sort-Object)).Count -ne 0) {
  throw "Unexpected portrait slice paths: $($actual -join ', ')"
}
git diff --cached --check
if ($LASTEXITCODE -ne 0) { throw 'Portrait staged diff check failed.' }
git commit -m "feat: publish scoped portrait evidence"
if ($LASTEXITCODE -ne 0) { throw 'Portrait slice commit failed.' }
if ((git log -1 --pretty=%s).Trim() -cne 'feat: publish scoped portrait evidence') {
  throw 'Unexpected portrait commit subject.'
}
if (git status --short) { throw 'Portrait commit left a dirty worktree.' }
```

Expected focused GREEN: `Ran 7 tests`, `OK` (five new methods, the existing
word-boundary regression, and the fake-project lease regression). Expected
static catalog: capability module 20 methods, `Tools` discovery 359 methods, and
both loader error lists exactly empty; no cumulative module or repository test
body runs at this intermediate SHA. The real Narrative gate still fails manifest
validation before child launch because show-before is absent.

**Asset audit:** Tooling only. No art, music, SFX, portrait asset, animation,
UI, font, old-game, shipping source, or package-size change occurs. Empty PNGs
exist only inside temporary test directories.

---

## Task 5: Add scoped narration-overlap JSON evidence

**Files:**

- Modify: `Tools/test_winter_narrative_capabilities.py`
- Modify: `scan_narration_overlap.py`
- Modify: `Tools/Run-WinterInterludeGate.ps1`

The overlap contract defines a consecutive narration block as narration lines
separated only by blank or comment lines. Every meaningful non-narration line
terminates the current block. `hide active_tag` both terminates the block and
clears that active portrait; hiding another tag does not invent a clear.

- [ ] **Step 1: Add the four complete overlap tests**

Append this class:

```python
class NarrationOverlapJsonProducerTests(unittest.TestCase):
    def test_overlap_json_cli_emits_exact_clean_and_positive_schema(self) -> None:
        self.assertTrue(PRODUCERS["overlap"].is_file())
        with tempfile.TemporaryDirectory(prefix="winter-overlap-schema-") as raw:
            project = _make_producer_project(
                raw,
                "scan_narration_overlap.py",
                {
                    "governance_winter_interlude.rpy": (
                        "label overlap:\n"
                        "    show alice_img at left\n"
                        '    "First narration."\n'
                        '    "Second narration."\n'
                    ),
                    "clean.rpy": (
                        "label clean:\n"
                        "    show alice_img at left\n"
                        "    scene bg study\n"
                        '    "First narration."\n'
                        '    "Second narration."\n'
                    ),
                },
            )
            target = project / "game" / "governance_winter_interlude.rpy"
            positive_output = project / "positive.json"
            positive = _run_json_producer(
                project,
                "scan_narration_overlap.py",
                ["--file", str(target)],
                positive_output,
                inherited_handle=True,
            )
            self.assertEqual(positive.returncode, 1, positive.stderr)
            self.assertTrue(positive_output.is_file())
            document = json.loads(positive_output.read_text(encoding="utf-8"))
            _assert_common_document(
                self,
                document,
                tool="narration_overlap",
                scanned_files=["game/governance_winter_interlude.rpy"],
            )
            self.assertEqual(document["blocking_count"], 1)
            self.assertEqual(document["findings"][0]["line"], 3)
            self.assertEqual(document["findings"][0]["rule"], "narration_overlap")

            clean_target = project / "game" / "clean.rpy"
            clean_output = project / "clean.json"
            clean = _run_json_producer(
                project,
                "scan_narration_overlap.py",
                ["--file", str(clean_target)],
                clean_output,
                inherited_handle=False,
            )
            self.assertEqual(clean.returncode, 0, clean.stderr)
            clean_document = json.loads(clean_output.read_text(encoding="utf-8"))
            _assert_common_document(
                self,
                clean_document,
                tool="narration_overlap",
                scanned_files=["game/clean.rpy"],
            )
            self.assertEqual(clean_document["findings"], [])

            (project / "game" / "hide_clean.rpy").write_text(
                "label hide_clean:\n"
                "    show alice_img at left\n"
                "    hide alice_img\n"
                '    "First narration."\n'
                '    "Second narration."\n',
                encoding="utf-8",
                newline="\n",
            )
            hide_output = project / "hide-clean.json"
            hide_result = _run_json_producer(
                project,
                "scan_narration_overlap.py",
                ["--file", str(project / "game" / "hide_clean.rpy")],
                hide_output,
                inherited_handle=False,
            )
            self.assertEqual(hide_result.returncode, 0, hide_result.stderr)
            hide_document = json.loads(hide_output.read_text(encoding="utf-8"))
            _assert_common_document(
                self,
                hide_document,
                tool="narration_overlap",
                scanned_files=["game/hide_clean.rpy"],
            )
            self.assertEqual(hide_document["findings"], [])

            (project / "game" / "interrupted.rpy").write_text(
                "label interrupted:\n"
                "    show alice_img at left\n"
                '    "First narration."\n'
                "    $ renpy.pause(0.1)\n"
                '    "Second narration."\n',
                encoding="utf-8",
                newline="\n",
            )
            interrupted_output = project / "interrupted.json"
            interrupted = _run_json_producer(
                project,
                "scan_narration_overlap.py",
                ["--file", str(project / "game" / "interrupted.rpy")],
                interrupted_output,
                inherited_handle=False,
            )
            self.assertEqual(interrupted.returncode, 0, interrupted.stderr)
            interrupted_document = json.loads(
                interrupted_output.read_text(encoding="utf-8")
            )
            _assert_common_document(
                self,
                interrupted_document,
                tool="narration_overlap",
                scanned_files=["game/interrupted.rpy"],
            )
            self.assertEqual(interrupted_document["findings"], [])

    def test_overlap_missing_target_and_invalid_file_flags_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory(prefix="winter-overlap-target-") as raw:
            project = _make_producer_project(
                raw,
                "scan_narration_overlap.py",
                {"clean.rpy": "label clean:\n    scene bg study\n"},
            )
            outside = project / "outside.rpy"
            outside.write_text("label outside:\n", encoding="utf-8")
            for index, target in enumerate(
                (project / "game" / "missing.rpy", outside)
            ):
                with self.subTest(target=str(target)):
                    output = project / f"invalid-{index}.json"
                    completed = _run_json_producer(
                        project,
                        "scan_narration_overlap.py",
                        ["--file", str(target)],
                        output,
                        inherited_handle=False,
                    )
                    self.assertEqual(completed.returncode, 2)
                    _assert_no_valid_json(self, output)

            positional_output = project / "positional.json"
            positional = _run_producer(
                project,
                "scan_narration_overlap.py",
                [
                    "clean.rpy", "--format", "json",
                    "--output", str(positional_output),
                ],
            )
            self.assertEqual(positional.returncode, 2)
            _assert_no_valid_json(self, positional_output)

    def test_overlap_transport_rejects_mismatch_output_dir_and_collision(self) -> None:
        with tempfile.TemporaryDirectory(prefix="winter-overlap-transport-") as raw:
            project = _make_producer_project(
                raw,
                "scan_narration_overlap.py",
                {"clean.rpy": "label clean:\n    scene bg study\n"},
            )
            target = project / "game" / "clean.rpy"
            owned = project / "owned.json"
            wrong = project / "wrong.json"
            marker = b"WINTER_GATE_RESERVED_V1:overlap"
            with _ShareZeroFile(owned) as owner:
                owner.write_bytes(marker)
                mismatch = _run_producer(
                    project,
                    "scan_narration_overlap.py",
                    [
                        "--file", str(target), "--format", "json",
                        "--output", str(wrong),
                    ],
                    environment_updates={HANDLE_ENV: str(owner.handle)},
                    close_fds=False,
                )
                self.assertEqual(mismatch.returncode, 2)
                self.assertFalse(wrong.exists())
            self.assertEqual(owned.read_bytes(), marker)

            invalid_flag = _run_producer(
                project,
                "scan_narration_overlap.py",
                [
                    "--file", str(target), "--format", "json",
                    "--output-dir", str(project / "evidence"),
                ],
            )
            self.assertEqual(invalid_flag.returncode, 2)

            relative = _run_producer(
                project,
                "scan_narration_overlap.py",
                [
                    "--file", str(target), "--format", "json",
                    "--output", "relative.json",
                ],
            )
            self.assertEqual(relative.returncode, 2)
            self.assertFalse((project / "relative.json").exists())

            collision = project / "collision.json"
            collision.write_bytes(b"sentinel")
            collided = _run_producer(
                project,
                "scan_narration_overlap.py",
                [
                    "--file", str(target), "--format", "json",
                    "--output", str(collision),
                ],
            )
            self.assertEqual(collided.returncode, 2)
            self.assertEqual(collision.read_bytes(), b"sentinel")

    def test_overlap_no_argument_legacy_mode_is_preserved(self) -> None:
        with tempfile.TemporaryDirectory(prefix="winter-overlap-legacy-") as raw:
            project = _make_producer_project(
                raw,
                "scan_narration_overlap.py",
                {
                    "chapter2.rpy": (
                        "label overlap:\n"
                        "    show alice_img at left\n"
                        '    "First narration."\n'
                        '    "Second narration."\n'
                    ),
                    "chapter2_expansion.rpy": (
                        "label clean:\n    scene bg study\n"
                    ),
                },
            )
            completed = _run_producer(project, "scan_narration_overlap.py", [])
            self.assertEqual(completed.returncode, 1, completed.stderr)
            self.assertIn("chapter2.rpy", completed.stdout)
            self.assertIn("TOTAL: 1", completed.stdout)
            with self.assertRaises(json.JSONDecodeError):
                json.loads(completed.stdout)

            positional = _run_producer(
                project,
                "scan_narration_overlap.py",
                ["chapter2.rpy"],
            )
            self.assertEqual(positional.returncode, 1, positional.stderr)
            self.assertIn("TOTAL: 1", positional.stdout)
```

- [ ] **Step 2: Take the one-behavior overlap RED**

```powershell
$red = & python -m unittest Tools.test_winter_narrative_capabilities.NarrationOverlapJsonProducerTests.test_overlap_json_cli_emits_exact_clean_and_positive_schema -v 2>&1
$redExit = $LASTEXITCODE
$red | Set-Content -LiteralPath .superpowers/sdd/task8-overlap-json-red.txt -Encoding UTF8
if ($redExit -eq 0) { throw 'Overlap JSON RED unexpectedly passed.' }
$joined = $red -join [Environment]::NewLine
if ($joined -notmatch 'Ran 1 test' -or
    $joined -notmatch 'FAILED \(failures=1\)' -or
    $joined -match '(?m)^ERROR:') {
  throw 'Overlap RED did not fail only on absent JSON and corrected scan behavior.'
}
```

Expected RED: one failure and zero errors. The legacy positional scanner cannot
publish the exact scoped document and its old active-hide/other-line behavior
does not satisfy the new vectors.

- [ ] **Step 3: Replace `scan_narration_overlap.py` with the complete producer**

```python
from __future__ import annotations

import argparse
import os
import re
import sys
from collections.abc import Sequence
from pathlib import Path

from Tools.winter_narrative_json import StructuredJsonSink, StructuredOutputError


ROOT = Path(__file__).resolve().parent
GAME_DIR = ROOT / "game"
LABEL_RE = re.compile(r"^(\s*)label\s+(\w+)")
SCENE_RE = re.compile(r"^(\s*)scene\b")
SHOW_RE = re.compile(r"^(\s*)show\s+(\w+_img)\b")
HIDE_RE = re.compile(r"^(\s*)hide\s+(\w+_img)")
HIDE_ALL_RE = re.compile(r"^(\s*)\$\s*hide_all_chars\s*\(")
NARRATION_RE = re.compile(r'^(\s*)("|centered\s+"|narrator\s+")')
DIALOGUE_RE = re.compile(r'^(\s*)(\w+)\s+"')
MENU_OPT_RE = re.compile(r'^(\s*)"[^"]*"(?:\s+if\s+.*)?:\s*$')
MENU_KW_RE = re.compile(r"^(\s*)menu\s*:")
IF_RE = re.compile(r"^(\s*)(if|elif|else)\b")
COMMENT_RE = re.compile(r"^\s*#")
EMPTY_RE = re.compile(r"^\s*$")
TARGET_FILES_DEFAULT = ("chapter2.rpy", "chapter2_expansion.rpy")


def classify(line: str) -> str:
    if COMMENT_RE.match(line) or EMPTY_RE.match(line):
        return "skip"
    if LABEL_RE.match(line):
        return "label"
    if SCENE_RE.match(line):
        return "scene"
    if HIDE_ALL_RE.match(line):
        return "hide_all"
    if SHOW_RE.match(line):
        return "show"
    if HIDE_RE.match(line):
        return "hide"
    if MENU_KW_RE.match(line):
        return "menu"
    if MENU_OPT_RE.match(line):
        return "menu_opt"
    if IF_RE.match(line):
        return "branch"
    if DIALOGUE_RE.match(line) and not NARRATION_RE.match(line):
        return "dialogue"
    if NARRATION_RE.match(line):
        return "narration"
    return "other"


def scan_file(
    path: str | os.PathLike[str],
    min_narration_block: int = 2,
) -> list[dict[str, object]]:
    with open(path, "r", encoding="utf-8") as handle:
        lines = handle.readlines()
    suggestions: list[dict[str, object]] = []
    active_show: str | None = None
    narration_start: int | None = None
    narration_indent = ""
    narration_count = 0
    menu_indent_stack: list[int] = []

    def line_indent(line: str) -> int:
        return len(line) - len(line.lstrip())

    index = 0
    while index < len(lines):
        line = lines[index]
        kind = classify(line)
        if menu_indent_stack and kind != "skip":
            current_indent = line_indent(line)
            while menu_indent_stack and current_indent <= menu_indent_stack[-1]:
                menu_indent_stack.pop()
        if kind == "scene":
            active_show = None
            narration_start = None
            narration_count = 0
        elif kind == "hide_all":
            active_show = None
            narration_start = None
            narration_count = 0
        elif kind == "show":
            match = SHOW_RE.match(line)
            if match is None:
                raise RuntimeError("show classification lost its match")
            active_show = match.group(2)
            narration_start = None
            narration_count = 0
        elif kind == "hide":
            match = HIDE_RE.match(line)
            if match is None:
                raise RuntimeError("hide classification lost its match")
            if match.group(2) == active_show:
                active_show = None
            narration_start = None
            narration_count = 0
        elif kind == "dialogue":
            narration_start = None
            narration_count = 0
        elif kind == "label":
            active_show = None
            narration_start = None
            narration_count = 0
            menu_indent_stack.clear()
        elif kind == "menu":
            narration_start = None
            narration_count = 0
            menu_indent_stack.append(line_indent(line))
        elif kind in ("menu_opt", "branch"):
            narration_start = None
            narration_count = 0
        elif kind == "narration":
            if menu_indent_stack:
                narration_start = None
                narration_count = 0
                index += 1
                continue
            match = NARRATION_RE.match(line)
            if match is None:
                raise RuntimeError("narration classification lost its match")
            if narration_start is None:
                narration_start = index
                narration_indent = match.group(1)
                narration_count = 1
            else:
                narration_count += 1
                if narration_count == min_narration_block and active_show is not None:
                    suggestions.append(
                        {
                            "line": narration_start + 1,
                            "indent": narration_indent,
                            "active_tag": active_show,
                            "preview": lines[narration_start].strip()[:80],
                            "block_size": 0,
                        }
                    )
                    active_show = None
        elif kind == "other":
            narration_start = None
            narration_count = 0
        index += 1
    return suggestions


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("legacy_files", nargs="*")
    parser.add_argument("--file")
    parser.add_argument("--format", choices=("json",))
    parser.add_argument("--output")
    return parser


def _validate_direct_game_file(raw_path: str) -> tuple[Path, str]:
    if not os.path.isabs(raw_path):
        raise ValueError("--file must be absolute")
    game_dir = GAME_DIR.resolve(strict=True)
    target = Path(raw_path).resolve(strict=True)
    if not target.is_file():
        raise ValueError("--file must name an existing regular file")
    if target.parent != game_dir or target.suffix.lower() != ".rpy":
        raise ValueError("--file must be a direct .rpy child of game")
    return target, f"game/{target.name}"


def _legacy_main(files: Sequence[str]) -> int:
    selected = list(files) if files else list(TARGET_FILES_DEFAULT)
    total = 0
    for file_name in selected:
        path = GAME_DIR / file_name
        if not path.is_file():
            print(f"[skip] not found: {path}")
            continue
        suggestions = scan_file(path)
        print(f"\n=== {file_name}: {len(suggestions)} 处建议 ===")
        for suggestion in suggestions:
            print(
                f"  L{suggestion['line']}  "
                f"(after show {suggestion['active_tag']})  "
                f"{suggestion['preview']!r}"
            )
        total += len(suggestions)
    print(f"\nTOTAL: {total} 处")
    return 1 if total else 0


def _structured_main(arguments: argparse.Namespace) -> int:
    sink: StructuredJsonSink | None = None
    try:
        if not os.path.isabs(arguments.output):
            raise ValueError("--output must be absolute")
        target, relative_path = _validate_direct_game_file(arguments.file)
        sink = StructuredJsonSink.claim(arguments.output)
        suggestions = scan_file(target)
        findings = [
            {
                "path": relative_path,
                "line": int(suggestion["line"]),
                "rule": "narration_overlap",
                "message": (
                    "two or more consecutive narration lines follow active "
                    f"portrait {suggestion['active_tag']!r} without clearing it"
                ),
            }
            for suggestion in suggestions
        ]
        document: dict[str, object] = {
            "schema_version": 1,
            "tool": "narration_overlap",
            "scanned_files": [relative_path],
            "blocking_count": len(findings),
            "findings": findings,
        }
        sink.write(document)
        sink.close()
        sink = None
        return 1 if findings else 0
    except (
        OSError,
        RuntimeError,
        StructuredOutputError,
        TypeError,
        UnicodeError,
        ValueError,
    ) as error:
        print(f"narration overlap evidence: {error}", file=sys.stderr)
        return 2
    finally:
        if sink is not None:
            try:
                sink.close()
            except OSError as close_error:
                print(
                    f"narration overlap evidence close: {close_error}",
                    file=sys.stderr,
                )


def main(argv: Sequence[str] | None = None) -> int:
    arguments = build_parser().parse_args(argv)
    structured_values = (arguments.file, arguments.format, arguments.output)
    if all(value is None for value in structured_values):
        return _legacy_main(arguments.legacy_files)
    if arguments.legacy_files or any(value is None for value in structured_values):
        print(
            "narration overlap evidence: JSON mode requires exactly "
            "--file ABS --format json --output ABS",
            file=sys.stderr,
        )
        return 2
    return _structured_main(arguments)


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Lease the shared writer for overlap**

Replace only the overlap step RequiredFiles expression with:

```powershell
            ([string[]]@($overlap, $structuredWriter, $target))
```

- [ ] **Step 5: Run focused GREEN, verify the static catalog, stage exactly, and commit**

```powershell
python -m unittest Tools.test_winter_narrative_capabilities.NarrationOverlapJsonProducerTests -v
if ($LASTEXITCODE -ne 0) { throw 'Overlap JSON focused GREEN failed.' }
@'
import unittest

module_loader = unittest.TestLoader()
module_suite = module_loader.loadTestsFromName(
    "Tools.test_winter_narrative_capabilities"
)
repository_loader = unittest.TestLoader()
repository_suite = repository_loader.discover(start_dir="Tools")
if module_loader.errors != [] or repository_loader.errors != []:
    raise SystemExit(
        "static unittest loading errors: "
        + repr(module_loader.errors + repository_loader.errors)
    )
counts = (module_suite.countTestCases(), repository_suite.countTestCases())
expected = (24, 363)
if counts != expected:
    raise SystemExit(f"unexpected static unittest counts: {counts!r}")
print({"capability": counts[0], "discovery": counts[1], "loader_errors": 0})
'@ | python -
if ($LASTEXITCODE -ne 0) { throw 'Overlap static test catalog failed.' }
$expected = [string[]]@(
  'Tools/Run-WinterInterludeGate.ps1',
  'Tools/test_winter_narrative_capabilities.py',
  'scan_narration_overlap.py'
)
git diff --cached --quiet
if ($LASTEXITCODE -ne 0) { throw 'Overlap slice started with a nonempty index.' }
git add -- $expected
$actual = [string[]]@(git diff --cached --name-only)
if (@(Compare-Object ($expected | Sort-Object) ($actual | Sort-Object)).Count -ne 0) {
  throw "Unexpected overlap slice paths: $($actual -join ', ')"
}
git diff --cached --check
if ($LASTEXITCODE -ne 0) { throw 'Overlap staged diff check failed.' }
git commit -m "feat: publish narration overlap evidence"
if ($LASTEXITCODE -ne 0) { throw 'Overlap slice commit failed.' }
if ((git log -1 --pretty=%s).Trim() -cne 'feat: publish narration overlap evidence') {
  throw 'Unexpected overlap commit subject.'
}
if (git status --short) { throw 'Overlap commit left a dirty worktree.' }
```

Expected focused GREEN: `Ran 4 tests`, `OK`. Expected static catalog:
capability module 24 methods, `Tools` discovery 363 methods, and both loader
error lists exactly empty; no cumulative module or repository test body runs at
this intermediate SHA. The manifest still stops before child launch because
show-before is absent.

**Asset audit:** Tooling only. Art, music, SFX, portraits, animation, UI,
font, old-game, shipping source, and package size are unchanged.

---

## Task 6: Add scoped show-before-prevention JSON evidence

**Files:**

- Modify: `Tools/test_winter_narrative_capabilities.py`
- Create: `Tools/scan_show_before_prevention.py`
- Modify: `Tools/Run-WinterInterludeGate.ps1`
- Modify: `Tools/test_winter_interlude_gate.py`

This slice creates the previously absent scanner. A left-positioned portrait is
protected only when its immediately preceding effective line is either
`scene bg ...` or `$ hide_all_chars("the_same_tag")`. Blank and comment lines
do not change that predecessor. A different-tag clear, dialogue, Python,
control-flow, `hide`, or any other executable line is significant and does not
protect the later `show`. Right-positioned portraits are outside this rule.

- [ ] **Step 1: Add four complete show-before producer tests**

Append this class to `Tools/test_winter_narrative_capabilities.py`:

```python
class ShowBeforePreventionJsonProducerTests(unittest.TestCase):
    def test_show_before_json_cli_emits_exact_scoped_schema(self) -> None:
        self.assertTrue(PRODUCERS["show_before"].is_file())
        with tempfile.TemporaryDirectory(prefix="winter-show-schema-") as raw:
            project = _make_producer_project(
                raw,
                "Tools/scan_show_before_prevention.py",
                {
                    "governance_winter_interlude.rpy": (
                        "label winter:\n"
                        "    show alice_img at left with dissolve\n"
                    ),
                    "chapter_noise.rpy": (
                        "label noise:\n"
                        "    show bob_img at left with dissolve\n"
                    ),
                },
            )
            target = project / "game" / "governance_winter_interlude.rpy"
            output = project / "show-before.json"
            completed = _run_json_producer(
                project,
                "Tools/scan_show_before_prevention.py",
                ["--file", str(target)],
                output,
                inherited_handle=True,
            )
            self.assertEqual(completed.returncode, 1, completed.stderr)
            self.assertEqual(completed.stdout, "")
            document = json.loads(output.read_text(encoding="utf-8"))
            _assert_common_document(
                self,
                document,
                tool="show_before_prevention",
                scanned_files=["game/governance_winter_interlude.rpy"],
            )
            self.assertEqual(document["blocking_count"], 1)
            self.assertEqual(
                document["findings"],
                [
                    {
                        "path": "game/governance_winter_interlude.rpy",
                        "line": 2,
                        "rule": "show_before_prevention",
                        "message": (
                            "left-positioned portrait 'alice_img' is not "
                            "immediately preceded by scene bg or an exact-tag "
                            "hide_all_chars call"
                        ),
                    }
                ],
            )

    def test_show_before_rejects_removed_or_mismatched_prevention(self) -> None:
        with tempfile.TemporaryDirectory(prefix="winter-show-rules-") as raw:
            project = _make_producer_project(
                raw,
                "Tools/scan_show_before_prevention.py",
                {
                    "governance_winter_interlude.rpy": (
                        "label winter:\n"
                        "    scene bg council_hall\n"
                        "    show alice_img at left with dissolve\n"
                        '    $ hide_all_chars("alice_img")\n'
                        "    # comments do not erase prevention\n"
                        "\n"
                        "    show alice_img at left with dissolve\n"
                        '    $ hide_all_chars("bob_img")\n'
                        "    show alice_img at left with dissolve\n"
                        '    alice "The room changes."\n'
                        "    show alice_img at left with dissolve\n"
                    )
                },
            )
            target = project / "game" / "governance_winter_interlude.rpy"
            output = project / "rules.json"
            completed = _run_json_producer(
                project,
                "Tools/scan_show_before_prevention.py",
                ["--file", str(target)],
                output,
                inherited_handle=False,
            )
            self.assertEqual(completed.returncode, 1, completed.stderr)
            document = json.loads(output.read_text(encoding="utf-8"))
            _assert_common_document(
                self,
                document,
                tool="show_before_prevention",
                scanned_files=["game/governance_winter_interlude.rpy"],
            )
            self.assertEqual(
                [finding["line"] for finding in document["findings"]],
                [9, 11],
            )
            self.assertTrue(
                all(
                    finding["rule"] == "show_before_prevention"
                    for finding in document["findings"]
                )
            )

    def test_show_before_ignores_right_portraits_and_rejects_missing_targets(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory(prefix="winter-show-scope-") as raw:
            project = _make_producer_project(
                raw,
                "Tools/scan_show_before_prevention.py",
                {
                    "governance_winter_interlude.rpy": (
                        "label winter:\n"
                        "    show alice_img at right with dissolve # not at left\n"
                    )
                },
            )
            target = project / "game" / "governance_winter_interlude.rpy"
            clean_output = project / "right.json"
            clean = _run_json_producer(
                project,
                "Tools/scan_show_before_prevention.py",
                ["--file", str(target)],
                clean_output,
                inherited_handle=False,
            )
            self.assertEqual(clean.returncode, 0, clean.stderr)
            clean_document = json.loads(clean_output.read_text(encoding="utf-8"))
            _assert_common_document(
                self,
                clean_document,
                tool="show_before_prevention",
                scanned_files=["game/governance_winter_interlude.rpy"],
            )
            self.assertEqual(clean_document["blocking_count"], 0)
            self.assertEqual(clean_document["findings"], [])

            missing_output = project / "missing.json"
            missing = _run_json_producer(
                project,
                "Tools/scan_show_before_prevention.py",
                ["--file", str(project / "game" / "missing.rpy")],
                missing_output,
                inherited_handle=False,
            )
            self.assertEqual(missing.returncode, 2)
            _assert_no_valid_json(self, missing_output)

            outside_target = project / "outside.rpy"
            outside_target.write_text(
                "label outside:\n    show alice_img at left\n",
                encoding="utf-8",
                newline="\n",
            )
            outside_output = project / "outside.json"
            outside = _run_json_producer(
                project,
                "Tools/scan_show_before_prevention.py",
                ["--file", str(outside_target)],
                outside_output,
                inherited_handle=False,
            )
            self.assertEqual(outside.returncode, 2)
            _assert_no_valid_json(self, outside_output)

    def test_show_before_transport_and_no_argument_mode_are_fail_closed(
        self,
    ) -> None:
        marker = b"WINTER_GATE_RESERVED_V1:show-before-marker"
        with tempfile.TemporaryDirectory(prefix="winter-show-transport-") as raw:
            project = _make_producer_project(
                raw,
                "Tools/scan_show_before_prevention.py",
                {
                    "governance_winter_interlude.rpy": (
                        "label winter:\n"
                        "    show alice_img at left with dissolve\n"
                    )
                },
            )
            target = project / "game" / "governance_winter_interlude.rpy"

            owned = project / "owned.json"
            requested = project / "requested.json"
            with _ShareZeroFile(owned) as owner:
                owner.write_bytes(marker)
                mismatch = _run_producer(
                    project,
                    "Tools/scan_show_before_prevention.py",
                    [
                        "--file",
                        str(target),
                        "--format",
                        "json",
                        "--output",
                        str(requested),
                    ],
                    environment_updates={HANDLE_ENV: str(owner.handle)},
                    close_fds=False,
                )
                self.assertEqual(mismatch.returncode, 2)
            self.assertEqual(owned.read_bytes(), marker)
            _assert_no_valid_json(self, requested)

            output_dir_output = project / "output-dir.json"
            output_dir = _run_producer(
                project,
                "Tools/scan_show_before_prevention.py",
                [
                    "--file",
                    str(target),
                    "--format",
                    "json",
                    "--output",
                    str(output_dir_output),
                    "--output-dir",
                    str(project),
                ],
            )
            self.assertEqual(output_dir.returncode, 2)
            _assert_no_valid_json(self, output_dir_output)

            relative_output = project / "relative.json"
            relative = _run_producer(
                project,
                "Tools/scan_show_before_prevention.py",
                [
                    "--file",
                    str(target),
                    "--format",
                    "json",
                    "--output",
                    relative_output.name,
                ],
            )
            self.assertEqual(relative.returncode, 2)
            _assert_no_valid_json(self, relative_output)

            collision = project / "collision.json"
            collision.write_bytes(marker)
            collided = _run_json_producer(
                project,
                "Tools/scan_show_before_prevention.py",
                ["--file", str(target)],
                collision,
                inherited_handle=False,
            )
            self.assertEqual(collided.returncode, 2)
            self.assertEqual(collision.read_bytes(), marker)

            legacy = _run_producer(
                project,
                "Tools/scan_show_before_prevention.py",
                [],
            )
            self.assertEqual(legacy.returncode, 1, legacy.stderr)
            self.assertIn(
                "game/governance_winter_interlude.rpy:2",
                legacy.stdout.replace("\\", "/"),
            )
            with self.assertRaises(json.JSONDecodeError):
                json.loads(legacy.stdout)
```

- [ ] **Step 2: Run the behavior-specific RED**

```powershell
$red = & python -m unittest Tools.test_winter_narrative_capabilities.ShowBeforePreventionJsonProducerTests.test_show_before_json_cli_emits_exact_scoped_schema -v 2>&1
$redExit = $LASTEXITCODE
$red | Set-Content -LiteralPath .superpowers/sdd/task8-show-before-json-red.txt -Encoding UTF8
if ($redExit -eq 0) { throw 'Show-before JSON RED unexpectedly passed.' }
$joined = $red -join [Environment]::NewLine
if ($joined -notmatch 'Ran 1 test' -or
    $joined -notmatch 'FAILED \(failures=1\)' -or
    $joined -match '(?m)^ERROR:') {
  throw 'Show-before JSON RED did not fail only on the absent scanner.'
}
```

Expected RED: `FAILED (failures=1)`, because the scanner file does not exist.
There must be zero errors; the first assertion owns the failure.

- [ ] **Step 3: Create the complete show-before scanner**

Create `Tools/scan_show_before_prevention.py` with exactly:

```python
from __future__ import annotations

import argparse
import os
import re
import sys
from collections.abc import Sequence
from pathlib import Path

try:
    from Tools.winter_narrative_json import (
        StructuredJsonSink,
        StructuredOutputError,
    )
except ModuleNotFoundError:
    from winter_narrative_json import (
        StructuredJsonSink,
        StructuredOutputError,
    )


ROOT = Path(__file__).resolve().parents[1]
GAME_DIR = ROOT / "game"
LEGACY_TARGET = GAME_DIR / "governance_winter_interlude.rpy"
SHOW_LEFT_RE = re.compile(
    r"^\s*show\s+(?P<tag>[A-Za-z_]\w*)\b.*\bat\s+left\b"
)
SCENE_BACKGROUND_RE = re.compile(r"^\s*scene\s+bg(?:\s|$)")
HIDE_ALL_TAG_RE = re.compile(
    r"^\s*\$\s*hide_all_chars\(\s*"
    r"(?P<quote>['\"])(?P<tag>[A-Za-z_]\w*)(?P=quote)\s*\)"
    r"\s*(?:#.*)?$"
)


def _is_ignored_predecessor(line: str) -> bool:
    stripped = line.strip()
    return not stripped or stripped.startswith("#")


def _is_prevented(lines: list[str], index: int, tag: str) -> bool:
    predecessor = index - 1
    while predecessor >= 0 and _is_ignored_predecessor(lines[predecessor]):
        predecessor -= 1
    if predecessor < 0:
        return False
    effective = lines[predecessor]
    if SCENE_BACKGROUND_RE.match(effective):
        return True
    hidden = HIDE_ALL_TAG_RE.match(effective)
    return hidden is not None and hidden.group("tag") == tag


def scan_file(path: Path) -> list[dict[str, object]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    findings: list[dict[str, object]] = []
    for index, line in enumerate(lines):
        command = line.split("#", 1)[0]
        shown = SHOW_LEFT_RE.match(command)
        if shown is None:
            continue
        tag = shown.group("tag")
        if _is_prevented(lines, index, tag):
            continue
        findings.append(
            {
                "line": index + 1,
                "tag": tag,
                "preview": line.strip()[:160],
            }
        )
    return findings


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--file")
    parser.add_argument("--format", choices=("json",))
    parser.add_argument("--output")
    return parser


def _validate_direct_game_file(raw_path: str) -> tuple[Path, str]:
    if not os.path.isabs(raw_path):
        raise ValueError("--file must be absolute")
    game_dir = GAME_DIR.resolve(strict=True)
    target = Path(raw_path).resolve(strict=True)
    if not target.is_file():
        raise ValueError("--file must name an existing regular file")
    if target.parent != game_dir or target.suffix.lower() != ".rpy":
        raise ValueError("--file must be a direct .rpy child of game")
    return target, f"game/{target.name}"


def _legacy_main() -> int:
    try:
        target, relative_path = _validate_direct_game_file(str(LEGACY_TARGET))
        findings = scan_file(target)
    except (OSError, RuntimeError, UnicodeError, ValueError) as error:
        print(f"show-before prevention scan: {error}", file=sys.stderr)
        return 2
    for finding in findings:
        print(
            f"{relative_path}:{finding['line']}  "
            f"show {finding['tag']} at left lacks immediate prevention"
        )
    print(f"\nTOTAL: {len(findings)} show-before prevention findings")
    return 1 if findings else 0


def _structured_main(arguments: argparse.Namespace) -> int:
    sink: StructuredJsonSink | None = None
    try:
        if not os.path.isabs(arguments.output):
            raise ValueError("--output must be absolute")
        target, relative_path = _validate_direct_game_file(arguments.file)
        sink = StructuredJsonSink.claim(arguments.output)
        raw_findings = scan_file(target)
        findings = [
            {
                "path": relative_path,
                "line": int(finding["line"]),
                "rule": "show_before_prevention",
                "message": (
                    f"left-positioned portrait {finding['tag']!r} is not "
                    "immediately preceded by scene bg or an exact-tag "
                    "hide_all_chars call"
                ),
            }
            for finding in raw_findings
        ]
        document: dict[str, object] = {
            "schema_version": 1,
            "tool": "show_before_prevention",
            "scanned_files": [relative_path],
            "blocking_count": len(findings),
            "findings": findings,
        }
        sink.write(document)
        sink.close()
        sink = None
        return 1 if findings else 0
    except (
        OSError,
        RuntimeError,
        StructuredOutputError,
        TypeError,
        UnicodeError,
        ValueError,
    ) as error:
        print(f"show-before prevention evidence: {error}", file=sys.stderr)
        return 2
    finally:
        if sink is not None:
            try:
                sink.close()
            except OSError as close_error:
                print(
                    f"show-before prevention evidence close: {close_error}",
                    file=sys.stderr,
                )


def main(argv: Sequence[str] | None = None) -> int:
    arguments = build_parser().parse_args(argv)
    structured_values = (arguments.file, arguments.format, arguments.output)
    if all(value is None for value in structured_values):
        return _legacy_main()
    if any(value is None for value in structured_values):
        print(
            "show-before prevention evidence: JSON mode requires exactly "
            "--file ABS --format json --output ABS",
            file=sys.stderr,
        )
        return 2
    return _structured_main(arguments)


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Lease the scanner and migrate the real-gate bootstrap boundary**

In `Get-NarrativeGateManifest`, replace only the show-before step's current
RequiredFiles expression with:

```powershell
            ([string[]]@($showBefore, $structuredWriter, $target))
```

In `Tools/test_winter_interlude_gate.py`, replace
`test_real_project_stops_at_missing_show_scanner_during_task8_bootstrap` with
the following method. Copy only the method into the existing
`WinterInterludeGateCapabilityTests` class.

```python
def test_real_project_checker_runs_first_and_is_not_ready_until_nested_probes_land(
    self,
) -> None:
    self.assertTrue(
        (ROOT / "Tools" / "check_winter_narrative_capabilities.py").is_file()
    )
    self.assertTrue(
        (ROOT / "Tools" / "scan_show_before_prevention.py").is_file()
    )
    capability_tests = (
        ROOT / "Tools" / "test_winter_narrative_capabilities.py"
    ).read_text(encoding="utf-8")
    self.assertNotIn("class NestedQuoteJsonProducerTests", capability_tests)
    for phase in ("Batch", "Final"):
        with self.subTest(phase=phase):
            with tempfile.TemporaryDirectory(
                prefix="winter-real-missing-nested-probes-"
            ) as outside_text:
                outside = Path(outside_text)
                run_root = outside / f"run-{phase.lower()}"
                appdata = outside / "appdata"
                appdata.mkdir()
                environment = os.environ.copy()
                environment["APPDATA"] = str(appdata)
                completed = run_gate(
                    "-Gate",
                    "Narrative",
                    "-NarrativePhase",
                    phase,
                    "-ProjectRoot",
                    str(ROOT),
                    "-RunRoot",
                    str(run_root),
                    env=environment,
                    timeout=180,
                )
                self.assertEqual(completed.returncode, 1, completed.stderr)
                summary = json.loads(
                    (
                        run_root / "evidence" / "gate-summary.json"
                    ).read_text(encoding="utf-8-sig")
                )
                self.assertEqual(summary["status"], "failed")
                self.assertEqual(len(summary["steps"]), 1)
                failed = summary["steps"][0]
                self.assertEqual(failed["ordinal"], 1)
                self.assertEqual(failed["name"], "narrative-capability")
                self.assertTrue(failed["process_started"])
                self.assertEqual(failed["exit_code"], 1)
                self.assertEqual(failed["failure_kind"], "postcondition")
                output_index = failed["arguments"].index("--output") + 1
                capability_output = Path(failed["arguments"][output_index])
                document = json.loads(
                    capability_output.read_text(encoding="utf-8")
                )
                self.assertEqual(
                    set(document),
                    {
                        "schema_version",
                        "tool",
                        "phase",
                        "ready",
                        "capabilities",
                    },
                )
                self.assertEqual(document["schema_version"], 1)
                self.assertEqual(
                    document["tool"], "winter_narrative_capabilities"
                )
                self.assertEqual(document["phase"], phase.lower())
                self.assertIs(document["ready"], False)
                capabilities = document["capabilities"]
                self.assertEqual(
                    set(capabilities),
                    {
                        "canon_json",
                        "portrait_json",
                        "overlap_json",
                        "show_before_json",
                        "nested_quote_json",
                        "batch_contracts",
                        "final_contracts",
                    },
                )
                for capability in (
                    "canon_json",
                    "portrait_json",
                    "overlap_json",
                    "show_before_json",
                    "batch_contracts",
                ):
                    self.assertIs(capabilities[capability], True)
                self.assertIs(capabilities["nested_quote_json"], False)
```

At this boundary both phases now launch exactly one child. The checker owns the
failure: its named nested-quote test IDs do not yet resolve, so it publishes a
valid capability document with `nested_quote_json=false`, `ready=false`, and
exit 1. No gate test or checker catalog may use a `test_public_gate_...` ID;
the eighteen public-gate linkage mutations remain in the later linkage task.

- [ ] **Step 5: Run focused GREEN, verify the static catalog, stage exactly, and commit**

```powershell
python -m unittest Tools.test_winter_narrative_capabilities.ShowBeforePreventionJsonProducerTests Tools.test_winter_interlude_gate.WinterInterludeGateCapabilityTests.test_real_project_checker_runs_first_and_is_not_ready_until_nested_probes_land -v
if ($LASTEXITCODE -ne 0) { throw 'Show-before JSON focused GREEN failed.' }
@'
import unittest

module_loader = unittest.TestLoader()
module_suite = module_loader.loadTestsFromName(
    "Tools.test_winter_narrative_capabilities"
)
repository_loader = unittest.TestLoader()
repository_suite = repository_loader.discover(start_dir="Tools")
if module_loader.errors != [] or repository_loader.errors != []:
    raise SystemExit(
        "static unittest loading errors: "
        + repr(module_loader.errors + repository_loader.errors)
    )
counts = (module_suite.countTestCases(), repository_suite.countTestCases())
expected = (28, 367)
if counts != expected:
    raise SystemExit(f"unexpected static unittest counts: {counts!r}")
print({"capability": counts[0], "discovery": counts[1], "loader_errors": 0})
'@ | python -
if ($LASTEXITCODE -ne 0) { throw 'Show-before static test catalog failed.' }
$expected = [string[]]@(
  'Tools/Run-WinterInterludeGate.ps1',
  'Tools/scan_show_before_prevention.py',
  'Tools/test_winter_interlude_gate.py',
  'Tools/test_winter_narrative_capabilities.py'
)
git diff --cached --quiet
if ($LASTEXITCODE -ne 0) { throw 'Show-before slice started with a nonempty index.' }
git add -- $expected
$actual = [string[]]@(git diff --cached --name-only)
if (@(Compare-Object ($expected | Sort-Object) ($actual | Sort-Object)).Count -ne 0) {
  throw "Unexpected show-before slice paths: $($actual -join ', ')"
}
git diff --cached --check
if ($LASTEXITCODE -ne 0) { throw 'Show-before staged diff check failed.' }
git commit -m "feat: scan winter show prevention"
if ($LASTEXITCODE -ne 0) { throw 'Show-before slice commit failed.' }
if ((git log -1 --pretty=%s).Trim() -cne 'feat: scan winter show prevention') {
  throw 'Unexpected show-before commit subject.'
}
if (git status --short) { throw 'Show-before commit left a dirty worktree.' }
```

Expected focused GREEN: `Ran 5 tests`, `OK` (four producer tests plus the
replacement real-gate boundary). Expected static catalog: capability module 28
methods, `Tools` discovery 367 methods, and both loader error lists exactly
empty; no cumulative module or repository test body runs at this intermediate
SHA. The gate module remains `Ran 87 tests`; one named method was replaced, not
added.

**Asset audit:** Tooling only. Art, music, SFX, portraits, animation, UI,
font, old-game, shipping source, and package size are unchanged.

---

## Task 7: Publish scoped nested-quote JSON evidence

**Files:**

- Modify: `Tools/test_winter_narrative_capabilities.py`
- Modify: `Tools/scan_nested_quotes.py`
- Modify: `Tools/Run-WinterInterludeGate.ps1`
- Modify: `Tools/test_winter_interlude_gate.py`

This slice removes the legacy scanner's import-time `stdout` replacement,
`chdir`, and whole-project scan. JSON mode accepts one exact direct game file;
legacy no-argument mode keeps the narrative-prefix report and now includes the
governance module. An ASCII double quote inside the outer Ren'Py dialogue
literal is blocking exactly when it is preceded by an even number of
backslashes. Chinese quotation marks and odd-backslash escaped ASCII quotes
are valid.

- [ ] **Step 1: Add five complete nested-quote producer tests**

Append this class to `Tools/test_winter_narrative_capabilities.py`:

```python
class NestedQuoteJsonProducerTests(unittest.TestCase):
    def test_nested_quote_json_scopes_the_winter_governance_module(self) -> None:
        self.assertTrue(PRODUCERS["nested_quote"].is_file())
        with tempfile.TemporaryDirectory(prefix="winter-nested-schema-") as raw:
            project = _make_producer_project(
                raw,
                "Tools/scan_nested_quotes.py",
                {
                    "governance_winter_interlude.rpy": (
                        "label winter:\n"
                        '    alice "He said "winter" twice."\n'
                    ),
                    "chapter_noise.rpy": (
                        "label noise:\n"
                        '    bob "He said "summer" twice."\n'
                    ),
                },
            )
            target = project / "game" / "governance_winter_interlude.rpy"
            output = project / "nested.json"
            completed = _run_json_producer(
                project,
                "Tools/scan_nested_quotes.py",
                ["--file", str(target)],
                output,
                inherited_handle=True,
            )
            self.assertEqual(completed.returncode, 1, completed.stderr)
            self.assertEqual(completed.stdout, "")
            document = json.loads(output.read_text(encoding="utf-8"))
            _assert_common_document(
                self,
                document,
                tool="nested_quotes",
                scanned_files=["game/governance_winter_interlude.rpy"],
            )
            self.assertEqual(
                document["findings"],
                [
                    {
                        "path": "game/governance_winter_interlude.rpy",
                        "line": 2,
                        "rule": "nested_quote",
                        "message": (
                            "unescaped nested double quote can be parsed as "
                            "Ren'Py image attributes"
                        ),
                    }
                ],
            )

    def test_nested_quote_blocks_unescaped_but_accepts_escaped_and_chinese_quotes(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory(prefix="winter-nested-rules-") as raw:
            project = _make_producer_project(
                raw,
                "Tools/scan_nested_quotes.py",
                {
                    "governance_winter_interlude.rpy": (
                        "label winter:\n"
                        '    alice "He said "winter" twice."\n'
                        '    alice "He said \\"winter\\" twice."\n'
                        r'    alice "He said \\"winter\\" twice."' "\n"
                        '    alice "她说『冬天』两次。"\n'
                        "    python:\n"
                        '        sample = "a "dictionary" value"\n'
                        '    "narrator" "Two-string say syntax is valid."\n'
                    )
                },
            )
            target = project / "game" / "governance_winter_interlude.rpy"
            output = project / "rules.json"
            completed = _run_json_producer(
                project,
                "Tools/scan_nested_quotes.py",
                ["--file", str(target)],
                output,
                inherited_handle=False,
            )
            self.assertEqual(completed.returncode, 1, completed.stderr)
            document = json.loads(output.read_text(encoding="utf-8"))
            _assert_common_document(
                self,
                document,
                tool="nested_quotes",
                scanned_files=["game/governance_winter_interlude.rpy"],
            )
            self.assertEqual(document["blocking_count"], 2)
            self.assertEqual(
                [finding["line"] for finding in document["findings"]],
                [2, 4],
            )

    def test_nested_quote_import_has_no_cwd_or_scan_side_effect(self) -> None:
        with tempfile.TemporaryDirectory(prefix="winter-nested-import-") as raw:
            project = _make_producer_project(
                raw,
                "Tools/scan_nested_quotes.py",
                {
                    "governance_winter_interlude.rpy": (
                        "label winter:\n"
                        '    alice "He said "winter" twice."\n'
                    )
                },
            )
            game_dir = project / "game"
            code = (
                "import importlib.util,os,sys; "
                "print(os.getcwd()); "
                "sys.path.insert(0,sys.argv[1]); "
                "sys.path.insert(0,sys.argv[2]); "
                "spec=importlib.util.spec_from_file_location("
                "'winter_nested_import',sys.argv[3]); "
                "module=importlib.util.module_from_spec(spec); "
                "spec.loader.exec_module(module); "
                "print(os.getcwd())"
            )
            completed = subprocess.run(
                [
                    str(PYTHON),
                    "-B",
                    "-c",
                    code,
                    str(project),
                    str(project / "Tools"),
                    str(project / "Tools" / "scan_nested_quotes.py"),
                ],
                cwd=game_dir,
                env=_producer_environment(),
                stdin=subprocess.DEVNULL,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding="utf-8",
                errors="strict",
                close_fds=True,
                check=False,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertEqual(
                completed.stdout.splitlines(),
                [str(game_dir), str(game_dir)],
            )
            self.assertEqual(completed.stderr, "")

    def test_nested_quote_transport_flags_and_missing_target_fail_closed(
        self,
    ) -> None:
        marker = b"WINTER_GATE_RESERVED_V1:nested-quote-marker"
        with tempfile.TemporaryDirectory(prefix="winter-nested-transport-") as raw:
            project = _make_producer_project(
                raw,
                "Tools/scan_nested_quotes.py",
                {
                    "governance_winter_interlude.rpy": (
                        "label winter:\n"
                        '    alice "He said "winter" twice."\n'
                    )
                },
            )
            target = project / "game" / "governance_winter_interlude.rpy"

            owned = project / "owned.json"
            requested = project / "requested.json"
            with _ShareZeroFile(owned) as owner:
                owner.write_bytes(marker)
                mismatch = _run_producer(
                    project,
                    "Tools/scan_nested_quotes.py",
                    [
                        "--file",
                        str(target),
                        "--format",
                        "json",
                        "--output",
                        str(requested),
                    ],
                    environment_updates={HANDLE_ENV: str(owner.handle)},
                    close_fds=False,
                )
                self.assertEqual(mismatch.returncode, 2)
            self.assertEqual(owned.read_bytes(), marker)
            _assert_no_valid_json(self, requested)

            output_dir_output = project / "output-dir.json"
            output_dir = _run_producer(
                project,
                "Tools/scan_nested_quotes.py",
                [
                    "--file",
                    str(target),
                    "--format",
                    "json",
                    "--output",
                    str(output_dir_output),
                    "--output-dir",
                    str(project),
                ],
            )
            self.assertEqual(output_dir.returncode, 2)
            _assert_no_valid_json(self, output_dir_output)

            missing_output = project / "missing.json"
            missing = _run_json_producer(
                project,
                "Tools/scan_nested_quotes.py",
                ["--file", str(project / "game" / "missing.rpy")],
                missing_output,
                inherited_handle=False,
            )
            self.assertEqual(missing.returncode, 2)
            _assert_no_valid_json(self, missing_output)

            outside_target = project / "outside.rpy"
            outside_target.write_text(
                'label outside:\n    alice "He said "outside"."\n',
                encoding="utf-8",
                newline="\n",
            )
            outside_output = project / "outside.json"
            outside = _run_json_producer(
                project,
                "Tools/scan_nested_quotes.py",
                ["--file", str(outside_target)],
                outside_output,
                inherited_handle=False,
            )
            self.assertEqual(outside.returncode, 2)
            _assert_no_valid_json(self, outside_output)

            relative_output = project / "relative.json"
            relative = _run_producer(
                project,
                "Tools/scan_nested_quotes.py",
                [
                    "--file",
                    str(target),
                    "--format",
                    "json",
                    "--output",
                    relative_output.name,
                ],
            )
            self.assertEqual(relative.returncode, 2)
            _assert_no_valid_json(self, relative_output)

            collision = project / "collision.json"
            collision.write_bytes(marker)
            collided = _run_json_producer(
                project,
                "Tools/scan_nested_quotes.py",
                ["--file", str(target)],
                collision,
                inherited_handle=False,
            )
            self.assertEqual(collided.returncode, 2)
            self.assertEqual(collision.read_bytes(), marker)

    def test_nested_quote_no_argument_legacy_mode_is_preserved(self) -> None:
        with tempfile.TemporaryDirectory(prefix="winter-nested-legacy-") as raw:
            project = _make_producer_project(
                raw,
                "Tools/scan_nested_quotes.py",
                {
                    "governance_winter_interlude.rpy": (
                        "label winter:\n"
                        '    alice "He said "winter" twice."\n'
                    ),
                    "ui_noise.rpy": (
                        "label noise:\n"
                        '    bob "He said "interface" twice."\n'
                    ),
                },
            )
            completed = _run_producer(
                project,
                "Tools/scan_nested_quotes.py",
                [],
            )
            self.assertEqual(completed.returncode, 1, completed.stderr)
            normalized = completed.stdout.replace("\\", "/")
            self.assertIn("game/governance_winter_interlude.rpy:2", normalized)
            self.assertNotIn("ui_noise.rpy", normalized)
            with self.assertRaises(json.JSONDecodeError):
                json.loads(completed.stdout)
```

- [ ] **Step 2: Run the behavior-specific RED**

```powershell
$red = & python -m unittest Tools.test_winter_narrative_capabilities.NestedQuoteJsonProducerTests.test_nested_quote_json_scopes_the_winter_governance_module -v 2>&1
$redExit = $LASTEXITCODE
$red | Set-Content -LiteralPath .superpowers/sdd/task8-nested-quote-json-red.txt -Encoding UTF8
if ($redExit -eq 0) { throw 'Nested-quote JSON RED unexpectedly passed.' }
$joined = $red -join [Environment]::NewLine
if ($joined -notmatch 'Ran 1 test' -or
    $joined -notmatch 'FAILED \(failures=1\)' -or
    $joined -match '(?m)^ERROR:') {
  throw 'Nested-quote JSON RED did not fail only on absent JSON behavior.'
}
```

Expected RED: `FAILED (failures=1)` with zero errors. The legacy scanner exits
without accepting the JSON CLI and therefore cannot create the required
evidence document.

- [ ] **Step 3: Replace the scanner with this complete side-effect-free module**

Replace all of `Tools/scan_nested_quotes.py` with exactly:

```python
from __future__ import annotations

import argparse
import os
import re
import sys
from collections.abc import Sequence
from pathlib import Path

try:
    from Tools.winter_narrative_json import (
        StructuredJsonSink,
        StructuredOutputError,
    )
except ModuleNotFoundError:
    from winter_narrative_json import (
        StructuredJsonSink,
        StructuredOutputError,
    )


ROOT = Path(__file__).resolve().parents[1]
GAME_DIR = ROOT / "game"
SKIP = {
    "_developer.rpy",
    "attr_system.rpy",
    "audio_safe.rpy",
    "balance.rpy",
    "changelog.rpy",
    "char_helpers.rpy",
    "characters.rpy",
    "cinematics.rpy",
    "combat.rpy",
    "effects.rpy",
    "gui.rpy",
    "images_def.rpy",
    "inventory.rpy",
    "options.rpy",
    "random_events.rpy",
    "screens.rpy",
    "screens_custom.rpy",
    "test_game.rpy",
}
NARRATIVE_PREFIXES = (
    "chapter",
    "script",
    "prologue",
    "npc",
    "endings",
    "chapters_",
    "governance_",
)
DIALOGUE_RE = re.compile(
    r'^\s*(?:[A-Za-z_]\w*\s+)?"(?P<body>.*)"\s*(?:#.*)?$'
)
PYTHON_BLOCK_RE = re.compile(
    r"^(?:init(?:\s+-?\d+)?\s+python|python(?:\s+early)?):"
    r"(?:\s*#.*)?$"
)
DICTIONARY_LITERAL_RE = re.compile(r'^\s*"(?:[^"\\]|\\.)*"\s*:\s*')
TWO_STRING_SAY_RE = re.compile(r'^\s*"(?:[^"\\]|\\.)*"\s+"')


def _indent_width(line: str) -> int:
    return len(line) - len(line.lstrip(" \t"))


def _contains_unescaped_double_quote(body: str) -> bool:
    for index, character in enumerate(body):
        if character != '"':
            continue
        backslashes = 0
        predecessor = index - 1
        while predecessor >= 0 and body[predecessor] == "\\":
            backslashes += 1
            predecessor -= 1
        if backslashes % 2 == 0:
            return True
    return False


def scan_file(path: Path) -> list[dict[str, object]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    findings: list[dict[str, object]] = []
    python_indent: int | None = None
    for line_number, line in enumerate(lines, start=1):
        content = line.strip()
        if python_indent is not None:
            if not content or content.startswith("#"):
                continue
            if _indent_width(line) > python_indent:
                continue
            python_indent = None
        if PYTHON_BLOCK_RE.match(content):
            python_indent = _indent_width(line)
            continue
        if not content or content.startswith("#") or '"""' in content:
            continue
        if DICTIONARY_LITERAL_RE.match(line) or TWO_STRING_SAY_RE.match(line):
            continue
        dialogue = DIALOGUE_RE.match(line)
        if dialogue is None:
            continue
        if not _contains_unescaped_double_quote(dialogue.group("body")):
            continue
        findings.append(
            {
                "line": line_number,
                "preview": content[:160],
            }
        )
    return findings


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--file")
    parser.add_argument("--format", choices=("json",))
    parser.add_argument("--output")
    return parser


def _validate_direct_game_file(raw_path: str) -> tuple[Path, str]:
    if not os.path.isabs(raw_path):
        raise ValueError("--file must be absolute")
    game_dir = GAME_DIR.resolve(strict=True)
    target = Path(raw_path).resolve(strict=True)
    if not target.is_file():
        raise ValueError("--file must name an existing regular file")
    if target.parent != game_dir or target.suffix.lower() != ".rpy":
        raise ValueError("--file must be a direct .rpy child of game")
    return target, f"game/{target.name}"


def _legacy_candidates() -> list[Path]:
    return [
        path
        for path in sorted(GAME_DIR.glob("*.rpy"), key=lambda item: item.name)
        if path.name not in SKIP
        and path.name.startswith(NARRATIVE_PREFIXES)
    ]


def _legacy_main() -> int:
    try:
        total = 0
        for path in _legacy_candidates():
            relative_path = f"game/{path.name}"
            findings = scan_file(path)
            for finding in findings:
                print(
                    f"{relative_path}:{finding['line']}  "
                    f"{finding['preview']}"
                )
            total += len(findings)
    except (OSError, RuntimeError, UnicodeError, ValueError) as error:
        print(f"nested-quote scan: {error}", file=sys.stderr)
        return 2
    print(f"\nTOTAL: {total} unescaped nested double quotes")
    return 1 if total else 0


def _structured_main(arguments: argparse.Namespace) -> int:
    sink: StructuredJsonSink | None = None
    try:
        if not os.path.isabs(arguments.output):
            raise ValueError("--output must be absolute")
        target, relative_path = _validate_direct_game_file(arguments.file)
        sink = StructuredJsonSink.claim(arguments.output)
        raw_findings = scan_file(target)
        findings = [
            {
                "path": relative_path,
                "line": int(finding["line"]),
                "rule": "nested_quote",
                "message": (
                    "unescaped nested double quote can be parsed as "
                    "Ren'Py image attributes"
                ),
            }
            for finding in raw_findings
        ]
        document: dict[str, object] = {
            "schema_version": 1,
            "tool": "nested_quotes",
            "scanned_files": [relative_path],
            "blocking_count": len(findings),
            "findings": findings,
        }
        sink.write(document)
        sink.close()
        sink = None
        return 1 if findings else 0
    except (
        OSError,
        RuntimeError,
        StructuredOutputError,
        TypeError,
        UnicodeError,
        ValueError,
    ) as error:
        print(f"nested-quote evidence: {error}", file=sys.stderr)
        return 2
    finally:
        if sink is not None:
            try:
                sink.close()
            except OSError as close_error:
                print(
                    f"nested-quote evidence close: {close_error}",
                    file=sys.stderr,
                )


def main(argv: Sequence[str] | None = None) -> int:
    arguments = build_parser().parse_args(argv)
    structured_values = (arguments.file, arguments.format, arguments.output)
    if all(value is None for value in structured_values):
        return _legacy_main()
    if any(value is None for value in structured_values):
        print(
            "nested-quote evidence: JSON mode requires exactly "
            "--file ABS --format json --output ABS",
            file=sys.stderr,
        )
        return 2
    return _structured_main(arguments)


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Lease the scanner and migrate the real Final boundary**

In `Get-NarrativeGateManifest`, replace only the nested-quotes step's current
RequiredFiles expression with:

```powershell
            ([string[]]@($nestedQuotes, $structuredWriter, $target))
```

In `Tools/test_winter_interlude_gate.py`, replace
`test_real_project_checker_runs_first_and_is_not_ready_until_nested_probes_land`
with the following method. Copy only the method into the existing
`WinterInterludeGateCapabilityTests` class.

```python
def test_real_project_final_is_capability_first_until_final_contracts_land(
    self,
) -> None:
    capability_tests = (
        ROOT / "Tools" / "test_winter_narrative_capabilities.py"
    ).read_text(encoding="utf-8")
    self.assertIn("class NestedQuoteJsonProducerTests", capability_tests)
    for scanner in (
        ROOT / "Tools" / "scan_canon.py",
        ROOT / "scan_missing_portraits.py",
        ROOT / "scan_narration_overlap.py",
        ROOT / "Tools" / "scan_show_before_prevention.py",
        ROOT / "Tools" / "scan_nested_quotes.py",
    ):
        self.assertTrue(scanner.is_file(), scanner)
    with tempfile.TemporaryDirectory(
        prefix="winter-real-final-contract-boundary-"
    ) as outside_text:
        outside = Path(outside_text)
        run_root = outside / "run-final"
        appdata = outside / "appdata"
        appdata.mkdir()
        environment = os.environ.copy()
        environment["APPDATA"] = str(appdata)
        completed = run_gate(
            "-Gate",
            "Narrative",
            "-NarrativePhase",
            "Final",
            "-ProjectRoot",
            str(ROOT),
            "-RunRoot",
            str(run_root),
            env=environment,
            timeout=180,
        )
        self.assertEqual(completed.returncode, 1, completed.stderr)
        summary = json.loads(
            (run_root / "evidence" / "gate-summary.json").read_text(
                encoding="utf-8-sig"
            )
        )
        self.assertEqual(summary["status"], "failed")
        self.assertEqual(len(summary["steps"]), 1)
        failed = summary["steps"][0]
        self.assertEqual(failed["ordinal"], 1)
        self.assertEqual(failed["name"], "narrative-capability")
        self.assertTrue(failed["process_started"])
        self.assertEqual(failed["exit_code"], 1)
        self.assertEqual(failed["failure_kind"], "postcondition")
        output_index = failed["arguments"].index("--output") + 1
        capability_output = Path(failed["arguments"][output_index])
        document = json.loads(capability_output.read_text(encoding="utf-8"))
        self.assertEqual(
            set(document),
            {
                "schema_version",
                "tool",
                "phase",
                "ready",
                "capabilities",
            },
        )
        self.assertEqual(document["schema_version"], 1)
        self.assertEqual(document["tool"], "winter_narrative_capabilities")
        self.assertEqual(document["phase"], "final")
        self.assertIs(document["ready"], False)
        capabilities = document["capabilities"]
        self.assertEqual(
            set(capabilities),
            {
                "canon_json",
                "portrait_json",
                "overlap_json",
                "show_before_json",
                "nested_quote_json",
                "batch_contracts",
                "final_contracts",
            },
        )
        for capability in (
            "canon_json",
            "portrait_json",
            "overlap_json",
            "show_before_json",
            "nested_quote_json",
            "batch_contracts",
        ):
            self.assertIs(capabilities[capability], True)
        self.assertIs(capabilities["final_contracts"], False)
```

The Batch checker is now ready; Final still exits 1 before ordinal 2 because
the five final-only named contracts intentionally do not exist until the later
approved-copy transition. This is the last temporary boundary replacement.
The separate linkage task will add six public-gate mutation methods containing
exactly three subtests apiece: inherited-handle linkage, path reopen, and path
fallback. Those 18 mutations are not duplicated in these producer classes and
are not named checker probes, preventing gate recursion.

- [ ] **Step 5: Run focused GREEN, verify the static catalog, and commit exactly**

```powershell
python -m unittest Tools.test_winter_narrative_capabilities.NestedQuoteJsonProducerTests Tools.test_winter_interlude_gate.WinterInterludeGateCapabilityTests.test_real_project_final_is_capability_first_until_final_contracts_land -v
if ($LASTEXITCODE -ne 0) { throw 'Nested-quote JSON focused GREEN failed.' }
@'
import unittest

module_loader = unittest.TestLoader()
module_suite = module_loader.loadTestsFromName(
    "Tools.test_winter_narrative_capabilities"
)
repository_loader = unittest.TestLoader()
repository_suite = repository_loader.discover(start_dir="Tools")
if module_loader.errors != [] or repository_loader.errors != []:
    raise SystemExit(
        "static unittest loading errors: "
        + repr(module_loader.errors + repository_loader.errors)
    )
counts = (module_suite.countTestCases(), repository_suite.countTestCases())
expected = (33, 372)
if counts != expected:
    raise SystemExit(f"unexpected static unittest counts: {counts!r}")
print({"capability": counts[0], "discovery": counts[1], "loader_errors": 0})
'@ | python -
if ($LASTEXITCODE -ne 0) { throw 'Nested-quote static test catalog failed.' }
$expected = [string[]]@(
  'Tools/Run-WinterInterludeGate.ps1',
  'Tools/scan_nested_quotes.py',
  'Tools/test_winter_interlude_gate.py',
  'Tools/test_winter_narrative_capabilities.py'
)
git diff --cached --quiet
if ($LASTEXITCODE -ne 0) { throw 'Nested-quote slice started with a nonempty index.' }
git add -- $expected
$actual = [string[]]@(git diff --cached --name-only)
if (@(Compare-Object ($expected | Sort-Object) ($actual | Sort-Object)).Count -ne 0) {
  throw "Unexpected nested-quote slice paths: $($actual -join ', ')"
}
git diff --cached --check
if ($LASTEXITCODE -ne 0) { throw 'Nested-quote staged diff check failed.' }
git commit -m "feat: publish scoped nested quote evidence"
if ($LASTEXITCODE -ne 0) { throw 'Nested-quote slice commit failed.' }
if ((git log -1 --pretty=%s).Trim() -cne 'feat: publish scoped nested quote evidence') {
  throw 'Unexpected nested-quote commit subject.'
}
if (git status --short) { throw 'Nested-quote commit left a dirty worktree.' }
```

Expected focused GREEN: `Ran 6 tests`, `OK` (five producer tests plus the
replacement real-Final boundary). Expected static catalog: capability module 33
methods, `Tools` discovery 372 methods, and both loader error lists exactly
empty; no cumulative module, repository test body, or public Batch gate runs at
this intermediate SHA. The gate module remains `Ran 87 tests`. Task 8 raises
the capability module to 39 methods and `Tools` discovery to 378 methods; its
18 mutation subtests do not alter method counts, and it owns the one
authoritative committed discovery plus Batch proof.

**Asset audit:** Tooling only. Art, music, SFX, portraits, animation, UI,
font, old-game, shipping source, and package size are unchanged.

---

## Task 8: Bind all six structured producers to the real public gate

**Files:**

- Modify: `Tools/check_winter_narrative_capabilities.py`
- Modify: `Tools/test_winter_narrative_capabilities.py`
- Modify: `Tools/test_winter_interlude_gate.py`

**Interfaces:**

- Consumes: `StructuredJsonSink.claim(output_path)`, the six structured entry
  points installed by Tasks 2–7, the exact named capability catalogs, the
  four-argument
  `AcquireStepDependencyLease(executable, fixedRequiredFiles, inventoryPath,
  projectIdentity)` overload, and `New-GateStep -InventoryPath`.
- Produces: six public-gate regression methods named with the
  `test_public_gate_` prefix. Each method owns exactly three subtests named
  `handle-linkage`, `path-reopen`, and `path-fallback`. None of those methods is
  added to `CAPABILITY_TEST_IDS`, `BATCH_CONTRACT_TEST_IDS`, or
  `FINAL_CONTRACT_TEST_IDS`.

This is the final pre-prose tooling slice. It does not add another transport or
inventory abstraction. The real public gate remains the only process
orchestrator, the shared writer remains the only structured-output authority,
and the tracked inventory remains the only full-project R/P membership source.

The final runtime-input contract is:

| Producer | Fixed `RequiredFiles` | Inventory selection and runtime reads |
| --- | --- | --- |
| capability | checker, writer, input module, capability test catalog, governance source-contract test, target, and all five scanner files | selects the tracked inventory; native lease retains that inventory and every listed R file while the checker runs all named probes; checker receives no `--inputs` argument |
| canon | canon scanner, writer, input module | receives `--inputs`; scans only listed R files; native lease retains inventory plus every listed R file |
| portrait | portrait scanner, writer, input module, target, `characters.rpy`, and `char_helpers.rpy` | receives `--inputs`; character definitions come only from listed R files and portrait classification only from listed P basenames; native lease retains inventory plus every listed R file |
| overlap | overlap scanner, writer, target | no inventory; reads only the exact target |
| show-before | show-before scanner, writer, target | no inventory; reads only the exact target |
| nested-quote | nested-quote scanner, writer, target | no inventory; reads only the exact target |

The P entries are names, not PNG byte inputs. The portrait producer never opens
PNG contents. `validated_winter_narrative_inputs` compares actual direct R/P
membership with the immutable inventory before and after each inventory-backed
scan; stable or transient additions fail closed and never join evidence. The
native adapter reads the inventory through the same retained deny-write/delete
handle, keeps that handle and every listed R handle through child drain, and
never reopens the inventory path. This closes replacement and in-place-write
races without pretending that file handles can lock directory membership.

- [ ] **Step 1: Add the complete mutation harness and the two focused RED regressions**

In `Tools/test_winter_narrative_capabilities.py`, add these imports beside the
existing imports:

```python
import ast
import re
```

Immediately after the existing producer-test helpers and before the first
producer test class, add this complete body:

```python
PUBLIC_GATE = ROOT / "Tools" / "Run-WinterInterludeGate.ps1"
WINDOWS_POWERSHELL_51 = (
    Path(os.environ["SystemRoot"])
    / "System32"
    / "WindowsPowerShell"
    / "v1.0"
    / "powershell.exe"
)
LINKAGE_MUTATIONS = (
    "handle-linkage",
    "path-reopen",
    "path-fallback",
)
PUBLIC_GATE_LINKAGE_METHODS = (
    "test_public_gate_capability_checker_kills_handle_reopen_and_fallback_mutants",
    "test_public_gate_canon_kills_handle_reopen_and_fallback_mutants",
    "test_public_gate_portrait_kills_handle_reopen_and_fallback_mutants",
    "test_public_gate_overlap_kills_handle_reopen_and_fallback_mutants",
    "test_public_gate_show_before_kills_handle_reopen_and_fallback_mutants",
    "test_public_gate_nested_quote_kills_handle_reopen_and_fallback_mutants",
)
LINKAGE_PROJECT_FILES = (
    "Tools/Run-RenPySuite.ps1",
    "Tools/Run-WinterInterludeGate.ps1",
    "Tools/check_winter_narrative_capabilities.py",
    "Tools/scan_ai_smell.py",
    "Tools/scan_canon.py",
    "Tools/scan_nested_quotes.py",
    "Tools/scan_show_before_prevention.py",
    "Tools/test_governance_winter_interlude.py",
    "Tools/test_winter_narrative_capabilities.py",
    "Tools/winter_narrative_inputs.py",
    "Tools/winter_narrative_inputs.txt",
    "Tools/winter_narrative_json.py",
    "scan_missing_portraits.py",
    "scan_narration_overlap.py",
)
LINKAGE_CAPABILITY_NAMES = (
    "canon_json",
    "portrait_json",
    "overlap_json",
    "show_before_json",
    "nested_quote_json",
    "batch_contracts",
    "final_contracts",
)


def _assert_structured_transport_contract(
    case: unittest.TestCase,
    producer: Path,
    function_name: str,
    output_expression: str,
) -> None:
    source = producer.read_text(encoding="utf-8", errors="strict")
    tree = ast.parse(source, filename=str(producer))
    functions = [
        node
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and node.name == function_name
    ]
    case.assertEqual(len(functions), 1)
    function = functions[0]
    calls = [node for node in ast.walk(function) if isinstance(node, ast.Call)]
    claims = [
        call
        for call in calls
        if isinstance(call.func, ast.Attribute)
        and call.func.attr == "claim"
        and isinstance(call.func.value, ast.Name)
        and call.func.value.id == "StructuredJsonSink"
    ]
    writes = [
        call
        for call in calls
        if isinstance(call.func, ast.Attribute)
        and call.func.attr == "write"
        and isinstance(call.func.value, ast.Name)
        and call.func.value.id == "sink"
    ]
    closes = [
        call
        for call in calls
        if isinstance(call.func, ast.Attribute)
        and call.func.attr == "close"
        and isinstance(call.func.value, ast.Name)
        and call.func.value.id == "sink"
    ]
    case.assertEqual(len(claims), 1)
    case.assertEqual(len(writes), 1)
    case.assertEqual(len(closes), 2)
    case.assertEqual(len(claims[0].args), 1)
    expected_output = ast.parse(output_expression, mode="eval").body
    case.assertEqual(
        ast.dump(claims[0].args[0], include_attributes=False),
        ast.dump(expected_output, include_attributes=False),
    )
    case.assertLess(claims[0].lineno, writes[0].lineno)
    case.assertLess(writes[0].lineno, min(call.lineno for call in closes))

    environment_reads = [
        node
        for node in ast.walk(function)
        if isinstance(node, ast.Attribute)
        and node.attr == "environ"
        and isinstance(node.value, ast.Name)
        and node.value.id == "os"
    ]
    path_writers = []
    for call in calls:
        if isinstance(call.func, ast.Name) and call.func.id == "open":
            path_writers.append(call)
        if isinstance(call.func, ast.Attribute) and call.func.attr in {
            "open",
            "replace",
            "rename",
            "unlink",
            "write_bytes",
            "write_text",
        }:
            path_writers.append(call)
    case.assertEqual(environment_reads, [])
    case.assertEqual(path_writers, [])

    function_source = ast.get_source_segment(source, function)
    case.assertIsNotNone(function_source)
    assert function_source is not None
    case.assertNotIn("WINTER_GATE_STRUCTURED_OUTPUT_HANDLE", function_source)
    case.assertNotIn("WINTER_GATE_JOB_NAME", function_source)
    sink_none_assignments = []
    for node in ast.walk(function):
        if (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == "sink"
            and isinstance(node.value, ast.Constant)
            and node.value.value is None
        ):
            sink_none_assignments.append(node)
        if (
            isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name) and target.id == "sink"
                for target in node.targets
            )
            and isinstance(node.value, ast.Constant)
            and node.value.value is None
        ):
            sink_none_assignments.append(node)
    case.assertEqual(len(sink_none_assignments), 2)
    case.assertIn("OSError", function_source)
    case.assertIn("except OSError as close_error:", function_source)


def _assert_linkage_methods_are_not_named_probes(
    case: unittest.TestCase,
) -> None:
    from Tools.check_winter_narrative_capabilities import (
        BATCH_CONTRACT_TEST_IDS,
        CAPABILITY_TEST_IDS,
        FINAL_CONTRACT_TEST_IDS,
    )

    catalogued = {
        test_id
        for test_ids in CAPABILITY_TEST_IDS.values()
        for test_id in test_ids
    }
    catalogued.update(BATCH_CONTRACT_TEST_IDS)
    catalogued.update(FINAL_CONTRACT_TEST_IDS)
    expected_public_ids = {
        "Tools.test_winter_narrative_capabilities."
        "PublicGateProducerLinkageTests."
        + method
        for method in PUBLIC_GATE_LINKAGE_METHODS
    }
    case.assertTrue(expected_public_ids.isdisjoint(catalogued))
    case.assertFalse(
        any(".test_public_gate_" in test_id for test_id in catalogued)
    )


def _run_linkage_process(
    arguments: list[str],
    *,
    cwd: Path,
    environment: dict[str, str] | None = None,
    timeout: int = 60,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        arguments,
        cwd=cwd,
        env=environment,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="strict",
        timeout=timeout,
        close_fds=True,
        check=False,
    )


def _mutate_linkage_producer(
    path: Path,
    output_expression: str,
    mutation: str,
) -> None:
    source = path.read_text(encoding="utf-8", errors="strict")
    claim = (
        "        sink = StructuredJsonSink.claim("
        + output_expression
        + ")\n"
    )
    write = "        sink.write(document)\n"
    if source.count(claim) != 1 or source.count(write) != 1:
        raise AssertionError(f"unexpected structured seam in {path}")
    if mutation == "handle-linkage":
        replacement = (
            '        if "WINTER_GATE_JOB_NAME" in os.environ:\n'
            '            os.environ.pop("WINTER_GATE_STRUCTURED_OUTPUT_HANDLE", None)\n'
            + claim
        )
        mutant = source.replace(claim, replacement, 1)
    elif mutation == "path-reopen":
        replacement = (
            write
            + '        if "WINTER_GATE_JOB_NAME" in os.environ:\n'
            + "            with open("
            + output_expression
            + ', "ab") as linkage_stream:\n'
            + '                linkage_stream.write(b" ")\n'
        )
        mutant = source.replace(write, replacement, 1)
    elif mutation == "path-fallback":
        replacement = (
            '        if "WINTER_GATE_JOB_NAME" in os.environ:\n'
            '            os.environ["WINTER_GATE_STRUCTURED_OUTPUT_HANDLE"] = "0"\n'
            "        try:\n"
            + "    "
            + claim
            + "        except StructuredOutputError:\n"
            + '            if "WINTER_GATE_JOB_NAME" not in os.environ:\n'
            + "                raise\n"
            + "            with open("
            + output_expression
            + ', "wb") as linkage_stream:\n'
            + '                linkage_stream.write(b"{}")\n'
            + "            return 0\n"
        )
        mutant = source.replace(claim, replacement, 1)
    elif mutation in ("schema-version-bool", "schema-version-float"):
        schema_seam = '"schema_version": 1,'
        if source.count(schema_seam) != 1:
            raise AssertionError(f"unexpected schema seam in {path}")
        replacement = (
            '"schema_version": True,'
            if mutation == "schema-version-bool"
            else '"schema_version": 1.0,'
        )
        mutant = source.replace(
            schema_seam,
            replacement,
            1,
        )
    else:
        raise AssertionError(f"unknown linkage mutation: {mutation}")
    if mutant == source:
        raise AssertionError(f"mutation did not change {path}")
    compile(mutant, str(path), "exec")
    path.write_text(
        mutant,
        encoding="utf-8",
        errors="strict",
        newline="\n",
    )


def _copy_linkage_project(
    case: unittest.TestCase,
    outside: Path,
    producer_relative: str,
    output_expression: str,
    mutation: str,
) -> tuple[Path, str]:
    from Tools.winter_narrative_inputs import (
        validated_winter_narrative_inputs,
    )

    project = outside / "project"
    project.mkdir()
    for relative in LINKAGE_PROJECT_FILES:
        source = ROOT / relative
        case.assertTrue(source.is_file(), source)
        destination = project / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)

    with validated_winter_narrative_inputs(INPUTS, ROOT) as inventory:
        rpy_files = inventory.rpy_files
        portrait_files = inventory.portrait_files
    case.assertEqual(len(rpy_files), 57)
    case.assertEqual(len(portrait_files), 197)
    for source in rpy_files:
        relative = source.relative_to(ROOT)
        destination = project / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
    for source in portrait_files:
        relative = source.relative_to(ROOT)
        destination = project / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(b"")

    _mutate_linkage_producer(
        project / producer_relative,
        output_expression,
        mutation,
    )
    git_commands = (
        ["git", "init", "--quiet"],
        ["git", "config", "core.autocrlf", "false"],
        ["git", "config", "user.name", "Winter Linkage Fixture"],
        ["git", "config", "user.email", "winter-linkage@example.invalid"],
        ["git", "add", "--", "."],
        ["git", "commit", "--quiet", "-m", "fixture: public gate linkage"],
    )
    for command in git_commands:
        completed = _run_linkage_process(command, cwd=project)
        case.assertEqual(
            completed.returncode,
            0,
            {"command": command, "stdout": completed.stdout, "stderr": completed.stderr},
        )
    status = _run_linkage_process(
        ["git", "status", "--porcelain=v1", "--untracked-files=all"],
        cwd=project,
    )
    case.assertEqual(status.returncode, 0, status.stderr)
    case.assertEqual(status.stdout, "")
    head = _run_linkage_process(
        ["git", "rev-parse", "--verify", "HEAD"],
        cwd=project,
    )
    case.assertEqual(head.returncode, 0, head.stderr)
    head_sha = head.stdout.strip()
    case.assertRegex(head_sha, r"\A[0-9a-f]{40}\Z")
    return project, head_sha


def _run_public_linkage_gate(
    project: Path,
    outside: Path,
) -> tuple[subprocess.CompletedProcess[str], dict[str, object], Path]:
    run_root = outside / "run"
    appdata = outside / "appdata"
    appdata.mkdir()
    environment = os.environ.copy()
    for name in (HANDLE_ENV, JOB_ENV, "GIT_COMMIT"):
        environment.pop(name, None)
    environment["APPDATA"] = str(appdata)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    environment["PYTHONIOENCODING"] = "utf-8"
    environment["PYTHONUTF8"] = "1"
    completed = _run_linkage_process(
        [
            str(WINDOWS_POWERSHELL_51),
            "-NoLogo",
            "-NoProfile",
            "-NonInteractive",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            str(project / "Tools" / "Run-WinterInterludeGate.ps1"),
            "-Gate",
            "Narrative",
            "-NarrativePhase",
            "Batch",
            "-ProjectRoot",
            str(project),
            "-RunRoot",
            str(run_root),
        ],
        cwd=project,
        environment=environment,
        timeout=660,
    )
    summary_path = run_root / "evidence" / "gate-summary.json"
    if not summary_path.is_file():
        raise AssertionError(
            "public gate did not publish summary: "
            f"stdout={completed.stdout!r}; stderr={completed.stderr!r}"
        )
    summary = json.loads(
        summary_path.read_text(encoding="utf-8-sig", errors="strict")
    )
    return completed, summary, run_root


def _structured_output_from_step(
    step: dict[str, object],
) -> Path:
    arguments = step["arguments"]
    if not isinstance(arguments, list):
        raise AssertionError("step arguments are not a list")
    output_index = arguments.index("--output") + 1
    return Path(arguments[output_index])


def _assert_schema_version_type_mutants_fail_named_test(
    case: unittest.TestCase,
    *,
    outside: Path,
    producer_relative: str,
    output_expression: str,
    named_test_id: str,
    prove_public_gate_ordinal_one: bool,
) -> None:
    for schema_mutation in (
        "schema-version-bool",
        "schema-version-float",
    ):
        schema_outside = outside / schema_mutation
        schema_outside.mkdir()
        project, head_sha = _copy_linkage_project(
            case,
            schema_outside,
            producer_relative,
            output_expression,
            schema_mutation,
        )
        named = _run_linkage_process(
            [
                str(PYTHON),
                "-B",
                "-m",
                "unittest",
                named_test_id,
                "-v",
            ],
            cwd=project,
            environment=_producer_environment(),
            timeout=180,
        )
        combined = named.stdout + "\n" + named.stderr
        case.assertEqual(named.returncode, 1, combined)
        case.assertEqual(
            re.findall(r"(?m)^Ran ([0-9]+) tests? in ", combined),
            ["1"],
            combined,
        )
        case.assertEqual(
            re.findall(r"(?m)^FAILED \(failures=([0-9]+)\)$", combined),
            ["1"],
            combined,
        )
        case.assertNotRegex(combined, r"(?m)^ERROR:")

        if prove_public_gate_ordinal_one and schema_mutation == "schema-version-bool":
            completed, summary, run_root = _run_public_linkage_gate(
                project,
                schema_outside,
            )
            diagnostic = {
                "schema_mutation": schema_mutation,
                "stdout": completed.stdout,
                "stderr": completed.stderr,
                "summary": summary,
            }
            case.assertEqual(completed.returncode, 1, diagnostic)
            case.assertEqual(summary["head_token"], head_sha[:12], diagnostic)
            case.assertEqual(len(summary["steps"]), 1, diagnostic)
            failed = summary["steps"][0]
            case.assertEqual(failed["ordinal"], 1, diagnostic)
            case.assertEqual(failed["name"], "narrative-capability", diagnostic)
            case.assertEqual(failed["exit_code"], 1, diagnostic)
            case.assertEqual(
                failed["failure_kind"],
                "postcondition",
                diagnostic,
            )
            case.assertIs(failed["tree_drained"], True, diagnostic)
            case.assertIs(
                failed["had_live_descendants_after_root_exit"],
                False,
                diagnostic,
            )
            document = json.loads(
                _structured_output_from_step(failed).read_text(
                    encoding="utf-8",
                    errors="strict",
                )
            )
            case.assertIs(document["ready"], False, diagnostic)
            case.assertIs(
                document["capabilities"]["canon_json"],
                False,
                diagnostic,
            )
            for name in LINKAGE_CAPABILITY_NAMES:
                if name not in ("canon_json", "final_contracts"):
                    case.assertIs(
                        document["capabilities"][name],
                        True,
                        diagnostic,
                    )
            case.assertTrue(
                (run_root / "evidence" / "gate-summary.json").is_file()
            )

        status = _run_linkage_process(
            ["git", "status", "--porcelain=v1", "--untracked-files=all"],
            cwd=project,
        )
        case.assertEqual(status.returncode, 0, status.stderr)
        case.assertEqual(status.stdout, "")


def _assert_public_gate_linkage_mutants(
    case: unittest.TestCase,
    *,
    producer_relative: str,
    output_expression: str,
    capability_name: str | None,
    schema_named_test_id: str,
    prove_schema_public_gate: bool = False,
) -> None:
    _assert_linkage_methods_are_not_named_probes(case)
    case.assertTrue(PUBLIC_GATE.is_file())
    case.assertTrue(WINDOWS_POWERSHELL_51.is_file())
    for mutation in LINKAGE_MUTATIONS:
        with case.subTest(linkage_mutation=mutation):
            with tempfile.TemporaryDirectory(
                prefix="winter-public-linkage-"
            ) as raw:
                outside = Path(raw)
                project, head_sha = _copy_linkage_project(
                    case,
                    outside,
                    producer_relative,
                    output_expression,
                    mutation,
                )
                if mutation == "handle-linkage":
                    _assert_schema_version_type_mutants_fail_named_test(
                        case,
                        outside=outside,
                        producer_relative=producer_relative,
                        output_expression=output_expression,
                        named_test_id=schema_named_test_id,
                        prove_public_gate_ordinal_one=prove_schema_public_gate,
                    )
                completed, summary, run_root = _run_public_linkage_gate(
                    project,
                    outside,
                )
                diagnostic = {
                    "mutation": mutation,
                    "producer": producer_relative,
                    "stdout": completed.stdout,
                    "stderr": completed.stderr,
                    "summary": summary,
                }
                case.assertEqual(completed.returncode, 1, diagnostic)
                case.assertEqual(summary["gate"], "Narrative", diagnostic)
                case.assertEqual(summary["narrative_phase"], "Batch", diagnostic)
                case.assertEqual(summary["status"], "failed", diagnostic)
                case.assertEqual(summary["head_token"], head_sha[:12], diagnostic)
                host = summary["host"]
                case.assertEqual(host["edition"], "Desktop", diagnostic)
                case.assertTrue(host["version"].startswith("5.1."), diagnostic)
                steps = summary["steps"]
                case.assertEqual(len(steps), 1, diagnostic)
                failed = steps[0]
                case.assertEqual(failed["ordinal"], 1, diagnostic)
                case.assertEqual(failed["name"], "narrative-capability", diagnostic)
                case.assertIs(failed["process_started"], True, diagnostic)
                case.assertIs(failed["timed_out"], False, diagnostic)
                case.assertIs(failed["tree_drained"], True, diagnostic)
                case.assertIs(
                    failed["had_live_descendants_after_root_exit"],
                    False,
                    diagnostic,
                )

                if capability_name is None:
                    case.assertEqual(failed["exit_code"], 2, diagnostic)
                    case.assertEqual(failed["failure_kind"], "process", diagnostic)
                    if mutation == "handle-linkage":
                        stderr_artifact = run_root / Path(failed["stderr"])
                        stderr_text = stderr_artifact.read_text(
                            encoding="utf-8-sig",
                            errors="strict",
                        )
                        case.assertIn(
                            "missing_inherited_handle_in_gate_job",
                            stderr_text,
                            diagnostic,
                        )
                    if mutation == "path-reopen":
                        output = _structured_output_from_step(failed)
                        document = json.loads(
                            output.read_text(
                                encoding="utf-8",
                                errors="strict",
                            )
                        )
                        case.assertIs(document["ready"], True, diagnostic)
                else:
                    case.assertEqual(failed["exit_code"], 1, diagnostic)
                    case.assertEqual(
                        failed["failure_kind"],
                        "postcondition",
                        diagnostic,
                    )
                    output = _structured_output_from_step(failed)
                    document = json.loads(
                        output.read_text(encoding="utf-8", errors="strict")
                    )
                    case.assertIs(document["ready"], False, diagnostic)
                    capabilities = document["capabilities"]
                    case.assertEqual(
                        set(capabilities),
                        set(LINKAGE_CAPABILITY_NAMES),
                        diagnostic,
                    )
                    for name in LINKAGE_CAPABILITY_NAMES:
                        expected = name not in (capability_name, "final_contracts")
                        case.assertIs(capabilities[name], expected, diagnostic)

                status = _run_linkage_process(
                    [
                        "git",
                        "status",
                        "--porcelain=v1",
                        "--untracked-files=all",
                    ],
                    cwd=project,
                )
                case.assertEqual(status.returncode, 0, status.stderr)
                case.assertEqual(status.stdout, "", diagnostic)
```

Append this exact class at the end of
`Tools/test_winter_narrative_capabilities.py`:

```python
class PublicGateProducerLinkageTests(unittest.TestCase):
    def test_public_gate_capability_checker_kills_handle_reopen_and_fallback_mutants(
        self,
    ) -> None:
        _assert_public_gate_linkage_mutants(
            self,
            producer_relative="Tools/check_winter_narrative_capabilities.py",
            output_expression="arguments.output",
            capability_name=None,
            schema_named_test_id=(
                "Tools.test_winter_narrative_capabilities."
                "WinterNarrativeCapabilityCheckerTests."
                "test_batch_and_final_documents_are_exact_and_phase_sensitive"
            ),
        )

    def test_public_gate_canon_kills_handle_reopen_and_fallback_mutants(
        self,
    ) -> None:
        _assert_public_gate_linkage_mutants(
            self,
            producer_relative="Tools/scan_canon.py",
            output_expression="output",
            capability_name="canon_json",
            schema_named_test_id=(
                "Tools.test_winter_narrative_capabilities."
                "CanonJsonProducerTests."
                "test_canon_json_cli_emits_exact_schema_and_scans_full_game"
            ),
            prove_schema_public_gate=True,
        )

    def test_public_gate_portrait_kills_handle_reopen_and_fallback_mutants(
        self,
    ) -> None:
        _assert_public_gate_linkage_mutants(
            self,
            producer_relative="scan_missing_portraits.py",
            output_expression="arguments.output",
            capability_name="portrait_json",
            schema_named_test_id=(
                "Tools.test_winter_narrative_capabilities."
                "PortraitJsonProducerTests."
                "test_portrait_json_cli_emits_exact_scoped_schema"
            ),
        )

    def test_public_gate_overlap_kills_handle_reopen_and_fallback_mutants(
        self,
    ) -> None:
        _assert_public_gate_linkage_mutants(
            self,
            producer_relative="scan_narration_overlap.py",
            output_expression="arguments.output",
            capability_name="overlap_json",
            schema_named_test_id=(
                "Tools.test_winter_narrative_capabilities."
                "NarrationOverlapJsonProducerTests."
                "test_overlap_json_cli_emits_exact_clean_and_positive_schema"
            ),
        )

    def test_public_gate_show_before_kills_handle_reopen_and_fallback_mutants(
        self,
    ) -> None:
        _assert_public_gate_linkage_mutants(
            self,
            producer_relative="Tools/scan_show_before_prevention.py",
            output_expression="arguments.output",
            capability_name="show_before_json",
            schema_named_test_id=(
                "Tools.test_winter_narrative_capabilities."
                "ShowBeforePreventionJsonProducerTests."
                "test_show_before_json_cli_emits_exact_scoped_schema"
            ),
        )

    def test_public_gate_nested_quote_kills_handle_reopen_and_fallback_mutants(
        self,
    ) -> None:
        _assert_public_gate_linkage_mutants(
            self,
            producer_relative="Tools/scan_nested_quotes.py",
            output_expression="arguments.output",
            capability_name="nested_quote_json",
            schema_named_test_id=(
                "Tools.test_winter_narrative_capabilities."
                "NestedQuoteJsonProducerTests."
                "test_nested_quote_json_scopes_the_winter_governance_module"
            ),
        )
```

Each public method delegates to one loop over the exact three-value
`LINKAGE_MUTATIONS` tuple. Do not put another `subTest` in these methods or any
helper they call. Inside each method's existing `handle-linkage` subtest, the
helper also changes that producer's sole `schema_version` value from integer 1
to Boolean `True` and then float `1.0` in two separate clean-HEAD fixtures and
invokes the same exact named test for each mutation. The capability envelope
uses its independent checker test, canon uses its
independent schema assertion, and portrait/overlap/show-before/nested-quote use
the common-document assertion. Each exact named invocation must return false
with `Ran 1 test`, one failure, and zero errors. Canon alone also sends this
schema-only mutant through the public gate and proves fail-fast at capability
ordinal 1; the other five do not duplicate that expensive gate proof. These
extra assertions remain inside the existing handle-linkage subtest, so there
are still exactly three subtest labels per public method and 18 total.

The fixture copies both `Tools/winter_narrative_inputs.py` and
`Tools/winter_narrative_inputs.txt`, copies all 57 listed R files, materializes
all 197 listed P basenames as zero-byte files because PNG contents are not read,
mutates one producer, initializes a new Git repository, commits every fixture
input, proves a clean HEAD, and only then invokes the real public gate through
the trusted System-directory Windows PowerShell 5.1 host. RunRoot and APPDATA
remain outside that project.

Task 2 already appends the controlled close-failure regression to
`WinterNarrativeCapabilityCheckerTests.test_cli_claims_before_probes_and_writes_not_ready_evidence`,
takes its behavior-specific RED, and installs the fail-closed checker tail. Do
not duplicate that regression or reopen the completed transport fix here.

In the existing
`WinterStructuredJsonWriterTests.test_standalone_mode_is_create_new_and_never_overwrites`
method, append this block inside its temporary-directory context, after the
environment-restoration `finally` block:

```python
            close_output = Path(raw) / "close-error.json"
            real_close = os.close

            def close_then_fail(fd: int) -> None:
                real_close(fd)
                raise OSError("forced writer close failure")

            with mock.patch(
                "Tools.winter_narrative_json.os.close",
                side_effect=close_then_fail,
            ):
                with self.assertRaisesRegex(OSError, "forced writer close"):
                    write_json_document(
                        {"schema_version": 1},
                        str(close_output),
                    )
            self.assertEqual(
                json.loads(
                    close_output.read_text(
                        encoding="utf-8",
                        errors="strict",
                    )
                ),
                {"schema_version": 1},
            )
```

Take the public-linkage RED before adding any source guards:

```powershell
$red = & python -m unittest Tools.test_winter_narrative_capabilities.PublicGateProducerLinkageTests.test_public_gate_canon_kills_handle_reopen_and_fallback_mutants -v 2>&1
$redExit = $LASTEXITCODE
$red | Set-Content -LiteralPath .superpowers/sdd/task8-public-linkage-red.txt -Encoding UTF8
if ($redExit -eq 0) { throw 'Public linkage RED unexpectedly passed.' }
$joined = $red -join [Environment]::NewLine
if ($joined -notmatch 'Ran 1 test' -or
    $joined -notmatch 'FAILED \(failures=3\)' -or
    $joined -match '(?m)^ERROR:') {
  throw 'Public linkage RED did not kill exactly the three canon subtests.'
}
```

Expected public-linkage RED: `Ran 1 test`, `FAILED (failures=3)`, zero errors.
The three mutations are dormant when the named checker probe scrubs the Job and
structured-handle environment, so capability ordinal 1 passes and the mutated
canon child fails later at ordinal 2. The regression expects all three to be
killed by the named probe at ordinal 1 and therefore fails once per subtest.

- [ ] **Step 2: Install the named-probe source guards**

In
`WinterNarrativeCapabilityCheckerTests.test_checker_module_exists_with_named_probe_catalog`,
immediately after reading the checker source, add:

```python
        _assert_structured_transport_contract(
            self,
            checker,
            "main",
            "arguments.output",
        )
        _assert_linkage_methods_are_not_named_probes(self)
        self.assertNotIn("PublicGateProducerLinkageTests", source)
```

In each of the following already-catalogued methods, insert the matching call
immediately after its existing producer-exists assertion (and after the
existing `source = ...read_text(...)` line where that line already exists):

For
`CanonJsonProducerTests.test_canon_json_cli_emits_exact_schema_and_scans_full_game`:

```python
def test_canon_json_cli_emits_exact_schema_and_scans_full_game(self) -> None:
    self.assertTrue(PRODUCERS["canon"].is_file())
    source = PRODUCERS["canon"].read_text(encoding="utf-8")
    _assert_structured_transport_contract(
        self,
        PRODUCERS["canon"],
        "_structured_main",
        "output",
    )
    ...
```

For
`PortraitJsonProducerTests.test_portrait_json_cli_emits_exact_scoped_schema`:

```python
def test_portrait_json_cli_emits_exact_scoped_schema(self) -> None:
    self.assertTrue(PRODUCERS["portrait"].is_file())
    source = PRODUCERS["portrait"].read_text(encoding="utf-8")
    _assert_structured_transport_contract(
        self,
        PRODUCERS["portrait"],
        "_structured_main",
        "arguments.output",
    )
    ...
```

For
`NarrationOverlapJsonProducerTests.test_overlap_json_cli_emits_exact_clean_and_positive_schema`:

```python
def test_overlap_json_cli_emits_exact_clean_and_positive_schema(self) -> None:
    self.assertTrue(PRODUCERS["overlap"].is_file())
    _assert_structured_transport_contract(
        self,
        PRODUCERS["overlap"],
        "_structured_main",
        "arguments.output",
    )
    ...
```

For
`ShowBeforePreventionJsonProducerTests.test_show_before_json_cli_emits_exact_scoped_schema`:

```python
def test_show_before_json_cli_emits_exact_scoped_schema(self) -> None:
    self.assertTrue(PRODUCERS["show_before"].is_file())
    _assert_structured_transport_contract(
        self,
        PRODUCERS["show_before"],
        "_structured_main",
        "arguments.output",
    )
    ...
```

For
`NestedQuoteJsonProducerTests.test_nested_quote_json_scopes_the_winter_governance_module`:

```python
def test_nested_quote_json_scopes_the_winter_governance_module(self) -> None:
    self.assertTrue(PRODUCERS["nested_quote"].is_file())
    _assert_structured_transport_contract(
        self,
        PRODUCERS["nested_quote"],
        "_structured_main",
        "arguments.output",
    )
    ...
```

These five methods are already exact named capability probes. The AST guard
requires exactly one claim, one sink write, two close attempts, the exact output
expression, claim-before-write-before-close ordering, controlled `OSError`
cleanup, no structured environment access, and no path writer. It therefore
kills the three dormant mutations while the public methods themselves remain
outside every checker catalog. Do not add a source guard to any catalog tuple.

The checker already matches the other five producers after Task 2: a normal
successful close occurs before return; its failure is caught as `OSError` and
returns 2; cleanup gets one last best-effort close and cannot turn a controlled
failure into success. The new AST source guard must preserve that exact tail and
must not add a path fallback.

- [ ] **Step 3: Lock final RequiredFiles and native inventory linkage inside the existing 87-method gate suite**

In `Tools/test_winter_interlude_gate.py`, change only the two Task 2 inventory
probe subprocess calls in `compile_native_inventory_lease_probe` and the nested
`invoke_inventory_probe` helper from `errors="replace"` to
`errors="strict"`. Do not change unrelated historical subprocess helpers.

Add this complete helper beside
`assert_native_inventory_lease_source_contract`:

```python
def _narrative_manifest_step(source: str, name: str) -> str:
    manifest_start = source.index("function Get-NarrativeGateManifest {")
    manifest_end = source.index(
        "# END LOOP 3.3-P2 STEP AND PROVISIONAL MANIFEST BUILDERS",
        manifest_start,
    )
    manifest = source[manifest_start:manifest_end]
    marker = "(New-GateStep '" + name + "'"
    start = manifest.index(marker)
    next_start = manifest.find("(New-GateStep '", start + len(marker))
    return manifest[start:] if next_start < 0 else manifest[start:next_start]


def assert_narrative_producer_linkage_source_contract(
    case: unittest.TestCase,
    source: str,
) -> None:
    manifest_start = source.index("function Get-NarrativeGateManifest {")
    manifest_end = source.index(
        "# END LOOP 3.3-P2 STEP AND PROVISIONAL MANIFEST BUILDERS",
        manifest_start,
    )
    manifest = source[manifest_start:manifest_end]
    capability_required = (
        "    $capabilityRequiredFiles = [string[]]@(\n"
        "        $checker,\n"
        "        $structuredWriter,\n"
        "        $narrativeInputsModule,\n"
        "        $capabilityTests,\n"
        "        $sourceContract,\n"
        "        $target,\n"
        "        $canon,\n"
        "        $portrait,\n"
        "        $overlap,\n"
        "        $showBefore,\n"
        "        $nestedQuotes\n"
        "    )"
    )
    case.assertEqual(manifest.count(capability_required), 1)
    for declaration in (
        "$narrativeInputs = Get-ExpectedProjectFilePath",
        "$narrativeInputsModule = Get-ExpectedProjectFilePath",
        "$structuredWriter = Get-ExpectedProjectFilePath",
        "$capabilityTests = Get-ExpectedProjectFilePath",
        "$characters = Get-ExpectedProjectFilePath",
        "$charHelpers = Get-ExpectedProjectFilePath",
    ):
        case.assertEqual(manifest.count(declaration), 1)

    capability = _narrative_manifest_step(source, "narrative-capability")
    canon = _narrative_manifest_step(source, "canon")
    portrait = _narrative_manifest_step(source, "missing-portraits")
    overlap = _narrative_manifest_step(source, "narration-overlap")
    show_before = _narrative_manifest_step(source, "show-before")
    nested = _narrative_manifest_step(source, "nested-quotes")

    case.assertIn(
        "$capabilityRequiredFiles `\n"
        "            -InventoryPath $narrativeInputs)",
        capability,
    )
    case.assertNotIn("'--inputs'", capability)
    case.assertIn(
        "([string[]]@(\n"
        "                $canon,\n"
        "                $structuredWriter,\n"
        "                $narrativeInputsModule\n"
        "            )) -InventoryPath $narrativeInputs)",
        canon,
    )
    case.assertIn("'--inputs', $narrativeInputs", canon)
    case.assertIn(
        "([string[]]@(\n"
        "                $portrait,\n"
        "                $structuredWriter,\n"
        "                $narrativeInputsModule,\n"
        "                $target,\n"
        "                $characters,\n"
        "                $charHelpers\n"
        "            )) -InventoryPath $narrativeInputs)",
        portrait,
    )
    case.assertIn("'--inputs', $narrativeInputs", portrait)
    scoped = (
        (overlap, "([string[]]@($overlap, $structuredWriter, $target))"),
        (show_before, "([string[]]@($showBefore, $structuredWriter, $target))"),
        (nested, "([string[]]@($nestedQuotes, $structuredWriter, $target))"),
    )
    for block, required_files in scoped:
        case.assertIn(required_files, block)
        case.assertNotIn("-InventoryPath", block)
        case.assertNotIn("'--inputs'", block)
    case.assertEqual(manifest.count("-InventoryPath $narrativeInputs"), 3)
    case.assertEqual(manifest.count("'--inputs', $narrativeInputs"), 2)
```

Append this block to the existing
`WinterInterludeGateProcessTests.test_executable_identity_uses_readable_full_chain_api`
method, after Task 2's existing native inventory assertions and mutation loop:

```python
        assert_narrative_producer_linkage_source_contract(self, source)
        manifest_mutants = {
            "capability-drops-test-catalog": source.replace(
                "        $capabilityTests,\n",
                "",
                1,
            ),
            "canon-bypasses-inventory-overload": source.replace(
                "            )) -InventoryPath $narrativeInputs)",
                "            )))",
                1,
            ),
            "scoped-producer-drops-writer": source.replace(
                "([string[]]@($overlap, $structuredWriter, $target))",
                "([string[]]@($overlap, $target))",
                1,
            ),
        }
        for name, mutant in manifest_mutants.items():
            with self.subTest(narrative_linkage_mutant=name):
                self.assertNotEqual(source, mutant)
                with self.assertRaises(AssertionError):
                    assert_narrative_producer_linkage_source_contract(
                        self,
                        mutant,
                    )
```

Do not remove or weaken Task 2's existing call to
`assert_native_inventory_lease_source_contract` or its `path-reopen`,
`inventory-not-retained`, and `rpy-not-leased` source mutants. That existing
method now jointly proves: inventory is acquired into the retained lease before
parsing; parsing reads from `dependency.ReadHandle` through a non-owning
`SafeFileHandle`; no `ReadVerifiedUtf8TextFile` path reopen occurs; every parsed
R path enters the same retained lease; the four-argument overload receives
`$script:ProjectIdentity`; capability/canon/portrait alone select inventory;
and every producer's complete fixed runtime inputs remain in its manifest
entry. Because only helpers and assertions enter an existing method, the public
gate module remains exactly 87 methods.

- [ ] **Step 4: Run focused GREEN and static loader counts, then commit exactly**

Run the writer/checker/native-manifest focused GREEN:

```powershell
python -m unittest Tools.test_winter_narrative_capabilities.WinterStructuredJsonWriterTests.test_standalone_mode_is_create_new_and_never_overwrites Tools.test_winter_narrative_capabilities.WinterNarrativeCapabilityCheckerTests.test_checker_module_exists_with_named_probe_catalog Tools.test_winter_narrative_capabilities.WinterNarrativeCapabilityCheckerTests.test_cli_claims_before_probes_and_writes_not_ready_evidence Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_executable_identity_uses_readable_full_chain_api -v
if ($LASTEXITCODE -ne 0) { throw 'Linkage source-contract focused GREEN failed.' }
```

Expected: `Ran 4 tests`, `OK`.

Run the six real public-gate methods once before commit:

```powershell
python -m unittest Tools.test_winter_narrative_capabilities.PublicGateProducerLinkageTests -v
if ($LASTEXITCODE -ne 0) { throw 'Unified public-gate linkage GREEN failed.' }
```

Expected: `Ran 6 tests`, `OK`; each method reports exactly the three mutation
subtests. All six handle-linkage branches also prove both `schema_version=True`
and `schema_version=1.0` kill their exact named schema test; representative
canon additionally proves
the schema-only public gate stops at ordinal 1 rather than reaching canon at
ordinal 2. Capability-checker transport mutants fail at ordinal 1 with child exit 2 and
`failure_kind=process`. The handle-linkage diagnostic contains
`missing_inherited_handle_in_gate_job`; path-reopen may leave a valid ready=true
document, but the process failure still blocks publication. Scanner mutants are
killed by their named source probe, so the checker publishes a valid ready=false
document, exits 1, and the gate records ordinal 1
`failure_kind=postcondition`. Every process tree is drained with no live
descendant after root exit.

Use static unittest loading, not another full module or gate execution, to lock
the cumulative method counts:

```powershell
@'
import importlib
import unittest

capability = importlib.import_module(
    "Tools.test_winter_narrative_capabilities"
)
gate = importlib.import_module("Tools.test_winter_interlude_gate")
capability_loader = unittest.TestLoader()
gate_loader = unittest.TestLoader()
discovery_loader = unittest.TestLoader()
counts = {
    "capability": capability_loader.loadTestsFromModule(capability).countTestCases(),
    "gate": gate_loader.loadTestsFromModule(gate).countTestCases(),
    "discovery": discovery_loader.discover(start_dir="Tools").countTestCases(),
}
loader_errors = {
    "capability": capability_loader.errors,
    "gate": gate_loader.errors,
    "discovery": discovery_loader.errors,
}
if loader_errors != {"capability": [], "gate": [], "discovery": []}:
    raise SystemExit(f"unexpected unittest loader errors: {loader_errors!r}")
expected = {"capability": 39, "gate": 87, "discovery": 378}
if counts != expected:
    raise SystemExit(f"unexpected static unittest counts: {counts!r}")
print(counts)
'@ | python -
if ($LASTEXITCODE -ne 0) { throw 'Static linkage test-count check failed.' }
```

Expected: `{'capability': 39, 'gate': 87, 'discovery': 378}` with all three
loader error lists exactly empty. Static loading executes no test and launches
no gate. Discovery starts explicitly at `Tools` because the repository does not
define `Tools` as an import package for root-recursive discovery.

Stage and commit exactly the three linkage paths:

```powershell
$expected = [string[]]@(
  'Tools/check_winter_narrative_capabilities.py',
  'Tools/test_winter_interlude_gate.py',
  'Tools/test_winter_narrative_capabilities.py'
)
git diff --cached --quiet
if ($LASTEXITCODE -ne 0) { throw 'Linkage slice started with a nonempty index.' }
git add -- $expected
$actual = [string[]]@(git diff --cached --name-only)
if (@(Compare-Object ($expected | Sort-Object) ($actual | Sort-Object)).Count -ne 0) {
  throw "Unexpected linkage slice paths: $($actual -join ', ')"
}
git diff --cached --check
if ($LASTEXITCODE -ne 0) { throw 'Linkage staged diff check failed.' }
git commit -m "test: bind winter capabilities to real producers"
if ($LASTEXITCODE -ne 0) { throw 'Linkage slice commit failed.' }
if ((git log -1 --pretty=%s).Trim() -cne 'test: bind winter capabilities to real producers') {
  throw 'Unexpected linkage commit subject.'
}
$committed = [string[]]@(git diff-tree --no-commit-id --name-only -r HEAD)
if (@(Compare-Object ($expected | Sort-Object) ($committed | Sort-Object)).Count -ne 0) {
  throw "Unexpected linkage commit paths: $($committed -join ', ')"
}
if (git status --short) { throw 'Linkage commit left a dirty worktree.' }
```

- [ ] **Step 5: Execute one authoritative discovery and one real committed Batch proof**

After the commit, do not rerun the full capability module or the 87-test gate
module separately. Run the following fence once as a unit. It refuses to start
either child if any HEAD-bound capture already exists, captures each real exit
code directly from its process, retains complete stdout and stderr, hashes the
combined logs and Batch summary, records both child PIDs, rejects a surviving
PID, and proves that HEAD plus all three committed linkage files remain
byte-identical across both executions.

```powershell
$pythonCommand = Get-Command python.exe -CommandType Application -ErrorAction Stop |
  Select-Object -First 1
if ($null -eq $pythonCommand -or
    [string]::IsNullOrWhiteSpace([string]$pythonCommand.Source)) {
  throw 'python.exe did not resolve to an application.'
}
$gateHost = Join-Path `
  ([Environment]::SystemDirectory) `
  'WindowsPowerShell\v1.0\powershell.exe'
if (-not [IO.File]::Exists($gateHost)) {
  throw 'Trusted Windows PowerShell 5.1 host is missing.'
}
$winterGate = (
  Resolve-Path -LiteralPath Tools/Run-WinterInterludeGate.ps1 -ErrorAction Stop
).Path
$headBefore = (git rev-parse --verify HEAD).Trim()
if ($LASTEXITCODE -ne 0 -or $headBefore -notmatch '\A[0-9a-f]{40}\z') {
  throw 'Could not bind authoritative execution to a full HEAD SHA.'
}
if (git status --short) {
  throw 'Authoritative execution requires a clean committed worktree.'
}
$boundPaths = [string[]]@(
  'Tools/check_winter_narrative_capabilities.py',
  'Tools/test_winter_interlude_gate.py',
  'Tools/test_winter_narrative_capabilities.py'
)
$hashesBefore = @{}
foreach ($path in $boundPaths) {
  $hashesBefore[$path] = (
    Get-FileHash -Algorithm SHA256 -LiteralPath $path -ErrorAction Stop
  ).Hash
}
$captureDirectory = '.superpowers/sdd'
New-Item -ItemType Directory -Path $captureDirectory -Force | Out-Null
$captureToken = $headBefore.Substring(0, 12)
$discoveryBase = Join-Path `
  $captureDirectory `
  ("task8-linkage-discovery-378-$captureToken")
$batchBase = Join-Path `
  $captureDirectory `
  ("task8-linkage-batch-9-$captureToken")
$plannedCaptures = [string[]]@(
  "$discoveryBase.txt",
  "$discoveryBase.stdout.txt",
  "$discoveryBase.stderr.txt",
  "$batchBase.txt",
  "$batchBase.stdout.txt",
  "$batchBase.stderr.txt"
)
foreach ($capture in $plannedCaptures) {
  if (Test-Path -LiteralPath $capture) {
    throw "HEAD-bound authoritative capture already exists; do not rerun: $capture"
  }
}
$strictUtf8 = New-Object Text.UTF8Encoding($false, $true)

function Read-StrictUtf8Capture {
  param(
    [Parameter(Mandatory = $true)]
    [string]$Path
  )
  $bytes = [IO.File]::ReadAllBytes($Path)
  $offset = 0
  if ($bytes.Length -ge 3 -and
      $bytes[0] -eq 0xEF -and
      $bytes[1] -eq 0xBB -and
      $bytes[2] -eq 0xBF) {
    $offset = 3
  }
  $strictUtf8.GetString($bytes, $offset, $bytes.Length - $offset)
}

function Invoke-AuthoritativeCapture {
  [CmdletBinding()]
  param(
    [Parameter(Mandatory = $true)]
    [string]$Executable,
    [Parameter(Mandatory = $true)]
    [string[]]$Arguments,
    [Parameter(Mandatory = $true)]
    [string]$BasePath
  )
  $stdoutPath = "$BasePath.stdout.txt"
  $stderrPath = "$BasePath.stderr.txt"
  $combinedPath = "$BasePath.txt"
  foreach ($path in @($stdoutPath, $stderrPath, $combinedPath)) {
    if (Test-Path -LiteralPath $path) {
      throw "Authoritative capture path is already occupied: $path"
    }
  }
  $process = Start-Process `
    -FilePath $Executable `
    -ArgumentList $Arguments `
    -WorkingDirectory (Get-Location).Path `
    -WindowStyle Hidden `
    -RedirectStandardOutput $stdoutPath `
    -RedirectStandardError $stderrPath `
    -Wait `
    -PassThru
  $process.Refresh()
  $pidValue = [int]$process.Id
  $exitCode = [int]$process.ExitCode
  if ($pidValue -le 0 -or -not $process.HasExited) {
    throw 'Authoritative child did not expose a completed positive PID.'
  }
  if ($null -ne (Get-Process -Id $pidValue -ErrorAction SilentlyContinue)) {
    throw "Authoritative child PID survived Wait: $pidValue"
  }
  $stdoutText = Read-StrictUtf8Capture -Path $stdoutPath
  $stderrText = Read-StrictUtf8Capture -Path $stderrPath
  $separator = ''
  if ($stdoutText.Length -gt 0 -and $stderrText.Length -gt 0 -and
      -not $stdoutText.EndsWith("`n", [StringComparison]::Ordinal)) {
    $separator = [Environment]::NewLine
  }
  $combinedText = $stdoutText + $separator + $stderrText
  [IO.File]::WriteAllText(
    (Join-Path (Get-Location).Path $combinedPath),
    $combinedText,
    $strictUtf8
  )
  Get-Content -LiteralPath $combinedPath -ErrorAction Stop | Out-Host
  [pscustomobject][ordered]@{
    ExitCode = $exitCode
    ProcessId = $pidValue
    Text = $combinedText
    CombinedPath = $combinedPath
    CombinedSha256 = (
      Get-FileHash -Algorithm SHA256 -LiteralPath $combinedPath `
        -ErrorAction Stop
    ).Hash
    StdoutSha256 = (
      Get-FileHash -Algorithm SHA256 -LiteralPath $stdoutPath `
        -ErrorAction Stop
    ).Hash
    StderrSha256 = (
      Get-FileHash -Algorithm SHA256 -LiteralPath $stderrPath `
        -ErrorAction Stop
    ).Hash
  }
}

$environmentNames = [string[]]@(
  'APPDATA',
  'GIT_COMMIT',
  'PYTHONDONTWRITEBYTECODE',
  'PYTHONIOENCODING',
  'PYTHONUTF8',
  'WINTER_GATE_JOB_NAME',
  'WINTER_GATE_STRUCTURED_OUTPUT_HANDLE'
)
$previousEnvironment = @{}
foreach ($name in $environmentNames) {
  $previousEnvironment[$name] = [Environment]::GetEnvironmentVariable(
    $name,
    [EnvironmentVariableTarget]::Process
  )
}
$batchRunRoot = Join-Path `
  ([IO.Path]::GetTempPath()) `
  ("winter-task8-linkage-batch-" + [Guid]::NewGuid().ToString('N'))
$batchAppData = Join-Path `
  ([IO.Path]::GetTempPath()) `
  ("winter-task8-linkage-appdata-" + [Guid]::NewGuid().ToString('N'))
if (Test-Path -LiteralPath $batchRunRoot) {
  throw 'Fresh authoritative Batch RunRoot already exists.'
}
New-Item -ItemType Directory -Path $batchAppData -ErrorAction Stop | Out-Null
try {
  Remove-Item Env:\WINTER_GATE_JOB_NAME -ErrorAction SilentlyContinue
  Remove-Item Env:\WINTER_GATE_STRUCTURED_OUTPUT_HANDLE `
    -ErrorAction SilentlyContinue
  $env:PYTHONDONTWRITEBYTECODE = '1'
  $env:PYTHONIOENCODING = 'utf-8'
  $env:PYTHONUTF8 = '1'
  $env:GIT_COMMIT = $headBefore

  $discoveryRun = Invoke-AuthoritativeCapture `
    -Executable $pythonCommand.Source `
    -Arguments ([string[]]@(
      '-B', '-m', 'unittest', 'discover', '-s', 'Tools', '-v'
    )) `
    -BasePath $discoveryBase
  $discoveryRan = [regex]::Matches(
    $discoveryRun.Text,
    '(?m)^Ran ([0-9]+) tests? in [0-9]+(?:\.[0-9]+)?s\r?$'
  )
  $discoveryOk = [regex]::Matches(
    $discoveryRun.Text,
    '(?m)^OK\r?$'
  )
  $discoveryLines = [string[]]@(
    $discoveryRun.Text -split '\r?\n' |
      Where-Object { $_.Length -gt 0 }
  )
  if ($discoveryRun.ExitCode -ne 0 -or
      $discoveryRan.Count -ne 1 -or
      $discoveryRan[0].Groups[1].Value -cne '378' -or
      $discoveryOk.Count -ne 1 -or
      $discoveryLines.Count -eq 0 -or
      $discoveryLines[-1] -cne 'OK') {
    throw "Authoritative discovery was not exactly Ran 378 tests / OK: $($discoveryRun.CombinedPath)"
  }
  if (git status --short) {
    throw 'Authoritative discovery dirtied the worktree.'
  }

  $env:APPDATA = $batchAppData
  $batchRun = Invoke-AuthoritativeCapture `
    -Executable $gateHost `
    -Arguments ([string[]]@(
      '-NoLogo',
      '-NoProfile',
      '-NonInteractive',
      '-ExecutionPolicy',
      'Bypass',
      '-File',
      $winterGate,
      '-Gate',
      'Narrative',
      '-NarrativePhase',
      'Batch',
      '-ProjectRoot',
      (Get-Location).Path,
      '-RunRoot',
      $batchRunRoot
    )) `
    -BasePath $batchBase
  if ($batchRun.ExitCode -ne 0) {
    throw "Committed unified Narrative Batch gate failed: $($batchRun.CombinedPath)"
  }
  $summaryPath = Join-Path $batchRunRoot 'evidence\gate-summary.json'
  if (-not [IO.File]::Exists($summaryPath)) {
    throw 'Committed Batch proof did not publish gate-summary.json.'
  }
  $summary = (Read-StrictUtf8Capture -Path $summaryPath) | ConvertFrom-Json
  $steps = @($summary.steps)
  if ($summary.gate -cne 'Narrative' -or
      $summary.narrative_phase -cne 'Batch' -or
      $summary.status -cne 'passed' -or
      $summary.failure_kind -ne $null -or
      $summary.head_token -cne $headBefore.Substring(0, 12) -or
      $summary.host.edition -cne 'Desktop' -or
      -not ([string]$summary.host.version).StartsWith(
        '5.1.',
        [StringComparison]::Ordinal
      ) -or
      $steps.Count -ne 9 -or
      @($steps | Where-Object {
        $_.status -cne 'passed' -or
        -not $_.process_started -or
        -not $_.tree_drained -or
        $_.had_live_descendants_after_root_exit
      }).Count -ne 0) {
    throw 'Committed Batch summary is not the exact clean nine-step proof.'
  }
  if (git status --short) {
    throw 'Committed Batch proof dirtied the worktree.'
  }

  $headAfter = (git rev-parse --verify HEAD).Trim()
  if ($LASTEXITCODE -ne 0 -or $headAfter -cne $headBefore) {
    throw 'HEAD changed during authoritative discovery or Batch.'
  }
  foreach ($path in $boundPaths) {
    $after = (
      Get-FileHash -Algorithm SHA256 -LiteralPath $path -ErrorAction Stop
    ).Hash
    if ($after -cne $hashesBefore[$path]) {
      throw "Committed linkage input changed during evidence: $path"
    }
  }
  $summarySha256 = (
    Get-FileHash -Algorithm SHA256 -LiteralPath $summaryPath -ErrorAction Stop
  ).Hash
  Write-Output "AUTHORITATIVE_HEAD=$headAfter"
  Write-Output "DISCOVERY_PID=$($discoveryRun.ProcessId)"
  Write-Output "DISCOVERY_LOG=$($discoveryRun.CombinedPath)"
  Write-Output "DISCOVERY_LOG_SHA256=$($discoveryRun.CombinedSha256)"
  Write-Output "DISCOVERY_STDOUT_SHA256=$($discoveryRun.StdoutSha256)"
  Write-Output "DISCOVERY_STDERR_SHA256=$($discoveryRun.StderrSha256)"
  Write-Output "BATCH_PID=$($batchRun.ProcessId)"
  Write-Output "BATCH_LOG=$($batchRun.CombinedPath)"
  Write-Output "BATCH_LOG_SHA256=$($batchRun.CombinedSha256)"
  Write-Output "BATCH_STDOUT_SHA256=$($batchRun.StdoutSha256)"
  Write-Output "BATCH_STDERR_SHA256=$($batchRun.StderrSha256)"
  Write-Output "BATCH_RUN_ROOT=$batchRunRoot"
  Write-Output "BATCH_SUMMARY_SHA256=$summarySha256"
}
finally {
  foreach ($name in $environmentNames) {
    $previous = $previousEnvironment[$name]
    if ($null -eq $previous) {
      Remove-Item -LiteralPath "Env:\$name" -ErrorAction SilentlyContinue
    }
    else {
      [Environment]::SetEnvironmentVariable(
        $name,
        [string]$previous,
        [EnvironmentVariableTarget]::Process
      )
    }
  }
}
```

Expected authoritative discovery: one completed positive PID, exit 0, exactly
one `Ran 378 tests` line, exactly one terminal `OK`, complete strict-UTF-8 raw
captures, and printed SHA-256 values. Only after that succeeds does the fence
start the single real Batch child. Expected Batch: a completed positive PID,
Desktop Windows PowerShell 5.1, current clean HEAD, `passed`, all
nine steps, every tree drained, no live descendants, a preserved external
RunRoot, and printed log/summary hashes. Existing HEAD-bound captures make a
same-commit rerun fail before either child starts. Final intentionally remains
capability-first until the later literal final contracts are installed after
all approved prose.

**Final frozen counts:** dedicated capability module `Ran 39 tests`; repository
discovery `Ran 378 tests`; public gate module remains `Ran 87 tests`. The 18
mutation subtests alter no method count and never enter a checker named-ID
catalog, so the capability child cannot recurse into the public gate.

**Asset audit:** Test and tooling changes only. No art, music, SFX, portrait
bytes, animation, UI, font, old-game, shipping source, or package-size change is
required. The 197 zero-byte PNGs exist only under test-owned temporary
directories and are deleted with those directories.

---

## Task 9 (umbrella Task 8 internal slice): Open the approved-copy integration seam

**Files:**

- Modify: `Tools/check_winter_narrative_capabilities.py`
- Modify: `Tools/test_winter_narrative_capabilities.py`
- Modify: `Tools/test_governance_winter_interlude.py`
- Modify: `game/governance_winter_interlude.rpy`

**Interfaces:**

- Consumes: the clean Task 8 linkage commit with capability module 39, public
  gate module 87, governance module 49, repository discovery 378, the exact
  five-entry `BATCH_CONTRACT_TEST_IDS`, the Task 7 structural story graph, and
  Task 8's already-controlled checker close path.
- Produces: one production `WINTER_COPY_REGISTRY` covering `S01` through `S17`
  plus empty and unwired `S18`; one strict `winter_outcome_copy(policy,
  seed_priority, outcome)` seam; independent control and presentation
  signatures; exactly three new governance methods; and one stable aggregate
  Batch test ID which never enumerates future per-scene focused methods.

This is internal slice 9 of umbrella Task 8. It is not authorization to start
the downstream umbrella Task 9 named by the hard stop. It changes no approved
prose: every registry value is the exact player-visible structural text already
displayed by Task 7, with dynamic `first` and `second` values expanded into two
equivalent literals. It does not invoke Opus or either control writer. The
one-Opus-plus-two-isolated-controls workflow, transient rejected-draft rule,
raw-output presentation, and explicit user approval begin only in a reviewed
literal scene addendum.

- [ ] **Step 1: Verify the exact Task 8 parent and static baseline**

Run this read-only precondition before editing any of the four files:

```powershell
$expectedSubject = 'test: bind winter capabilities to real producers'
$baseline = 'cd26d62cda05e40dbcd6c953bd2e620a65d59c0c'
$head = (git rev-parse --verify HEAD).Trim()
if ($LASTEXITCODE -ne 0 -or $head -notmatch '\A[0-9a-f]{40}\z') {
  throw 'Task 9 could not resolve a full HEAD SHA.'
}
git merge-base --is-ancestor $baseline $head
if ($LASTEXITCODE -ne 0) {
  throw 'Task 9 HEAD is not descended from the accepted Task 7.5 baseline.'
}
if ((git log -1 --pretty=%s).Trim() -cne $expectedSubject) {
  throw 'Task 9 did not start immediately after the Task 8 linkage commit.'
}
if (git status --short) {
  throw 'Task 9 requires a clean tracked and untracked worktree.'
}

$preflight = @'
import importlib
import unittest
from pathlib import Path

from Tools.check_winter_narrative_capabilities import (
    BATCH_CONTRACT_TEST_IDS,
)

expected_counts = {
    "capability": 39,
    "gate": 87,
    "governance": 49,
    "discovery": 378,
}
counts = {}
for key, module_name in (
    ("capability", "Tools.test_winter_narrative_capabilities"),
    ("gate", "Tools.test_winter_interlude_gate"),
    ("governance", "Tools.test_governance_winter_interlude"),
):
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(importlib.import_module(module_name))
    if loader.errors:
        raise AssertionError(f"{key} loader errors: {loader.errors!r}")
    counts[key] = suite.countTestCases()

discovery_loader = unittest.TestLoader()
discovery_suite = discovery_loader.discover(start_dir="Tools")
if discovery_loader.errors:
    raise AssertionError(
        f"discovery loader errors: {discovery_loader.errors!r}"
    )
counts["discovery"] = discovery_suite.countTestCases()
if counts != expected_counts:
    raise AssertionError(f"unexpected Task 8 baseline counts: {counts!r}")

aggregate_id = (
    "Tools.test_governance_winter_interlude."
    "WinterStoryGraphContractTests."
    "test_task8_current_approved_scene_copy_contracts_are_exact"
)
if len(BATCH_CONTRACT_TEST_IDS) != 5:
    raise AssertionError(BATCH_CONTRACT_TEST_IDS)
if aggregate_id in BATCH_CONTRACT_TEST_IDS:
    raise AssertionError("Task 9 aggregate ID already exists")
batch_loader = unittest.TestLoader()
batch_suite = batch_loader.loadTestsFromNames(BATCH_CONTRACT_TEST_IDS)
if batch_loader.errors:
    raise AssertionError(f"Batch loader errors: {batch_loader.errors!r}")
if batch_suite.countTestCases() != len(BATCH_CONTRACT_TEST_IDS):
    raise AssertionError("Task 8 Batch IDs do not each resolve once")

checker = Path("Tools/check_winter_narrative_capabilities.py").read_text(
    encoding="utf-8"
)
capability_tests = Path(
    "Tools/test_winter_narrative_capabilities.py"
).read_text(encoding="utf-8")
for required in (
    "        sink.write(document)\n"
    "        sink.close()\n"
    "        sink = None\n"
    '        return 0 if document["ready"] else 1',
    "except OSError as close_error:",
    'f"winter capability evidence close: {close_error}"',
):
    if checker.count(required) != 1:
        raise AssertionError(f"Task 8 checker close repair missing: {required!r}")
for required in (
    'raise OSError("forced capability sink close failure")',
    "self.assertEqual(close_exit, 2)",
    "self.assertEqual(close_sink.close_calls, 2)",
):
    if capability_tests.count(required) != 1:
        raise AssertionError(f"Task 8 close regression missing: {required!r}")
print(counts)
'@
& python -B -c $preflight
if ($LASTEXITCODE -ne 0) {
  throw 'Task 9 static preflight failed.'
}
```

Expected: clean HEAD descended from Task 7.5, exact Task 8 subject, capability
39, gate 87, governance 49, discovery 378, all loader error lists empty, five
resolving Batch IDs, absent aggregate ID, and the completed Task 8 close repair.
Do not reproduce or edit that close repair in this task.

- [ ] **Step 2: Add the independent test-side registry, speaker, presentation, and symbolic contracts**

In `Tools/test_governance_winter_interlude.py`, immediately after
`TASK7_VISIBLE_SEMANTIC_CONTRACT`, add these independent test-owned constants.
They do not import or derive a value from production:

```python
_TASK8_ALLOWED_SPEAKERS = (
    "accountant",
    "aldric",
    "captain",
    "crowd",
    "farmer",
    "guard",
    "merchant",
    "player",
)
_TASK8_SCENE_ORDER = (
    "S01",
    "S02",
    "S03",
    "S04",
    "S05",
    "S06",
    "S07",
    "S08",
    "S09",
    "S10",
    "S11",
    "S12",
    "S13",
    "S14",
    "S15",
    "S16",
    "S17",
    "S18",
)
_TASK8_APPROVED_SCENE_IDS = ()
_TASK8_OUTCOME_SCENE_CONTRACT = {
    ("trade", "preserve"): "S12",
    ("trade", "feed_now"): "S13",
    ("ration", "preserve"): "S14",
    ("ration", "feed_now"): "S15",
    ("requisition", "preserve"): "S16",
    ("requisition", "feed_now"): "S17",
}
_TASK8_OUTCOME_SYMBOLIC_CONTRACT = {
    ("trade", "preserve"): {
        "benefit": "trade_preserved_seed",
        "beneficiary": "farmers_and_trade_route",
        "burden": "trade_repayment_and_tight_rations",
        "bearer": "treasury_and_townspeople",
        "action": "audited_purchase_contracts",
        "followup": "trade_preserve_recovery",
    },
    ("trade", "feed_now"): {
        "benefit": "trade_immediate_relief",
        "beneficiary": "town_relief_recipients",
        "burden": "trade_seed_shortfall",
        "bearer": "treasury_and_farmers",
        "action": "market_grain_distribution",
        "followup": "trade_feed_recovery",
    },
    ("ration", "preserve"): {
        "benefit": "ration_preserved_seed",
        "beneficiary": "smallholders_and_farmers",
        "burden": "ration_hunger_and_reserve_pressure",
        "bearer": "garrison_and_townspeople",
        "action": "published_ration_ledgers",
        "followup": "ration_preserve_recovery",
    },
    ("ration", "feed_now"): {
        "benefit": "ration_broad_relief",
        "beneficiary": "town_relief_recipients",
        "burden": "ration_reserve_and_seed_loss",
        "bearer": "garrison_and_farmers",
        "action": "open_granary_distribution",
        "followup": "ration_feed_recovery",
    },
    ("requisition", "preserve"): {
        "benefit": "requisition_preserved_seed",
        "beneficiary": "smallholders_and_farmers",
        "burden": "requisition_compensation_debt",
        "bearer": "estates_and_lordship",
        "action": "sealed_compensation_vouchers",
        "followup": "requisition_preserve_recovery",
    },
    ("requisition", "feed_now"): {
        "benefit": "requisition_immediate_relief",
        "beneficiary": "broad_relief_recipients",
        "burden": "requisition_debt_and_seed_shortfall",
        "bearer": "estates_lordship_and_farmers",
        "action": "requisition_wagons_and_vouchers",
        "followup": "requisition_feed_recovery",
    },
}
_TASK8_MITIGATION_KEYS = (
    "market_trade",
    "granary_ration",
    "village_preserve",
    "route_feed_now",
    "merchant_regulated_trade",
    "southern_trade_terms",
    "existing_granary_ration",
    "decree_security_trade",
    "decree_civic_ration",
    "decree_military_requisition",
    "wealth_trade",
    "loyalty_ration",
    "power_requisition",
    None,
)
_TASK8_SOUTHERN_KEYS = (
    "none",
    "free",
    "ruler",
    "vassal",
    "outwit",
    "fall",
)
_TASK8_STRUCTURAL_MITIGATION_CONTRACT = {
    "market_trade": (
        "【结构占位·单项缓解】market_trade；不删除负担或承担者。",
    ),
    "granary_ration": (
        "【结构占位·单项缓解】granary_ration；不删除负担或承担者。",
    ),
    "village_preserve": (
        "【结构占位·单项缓解】village_preserve；不删除负担或承担者。",
    ),
    "route_feed_now": (
        "【结构占位·单项缓解】route_feed_now；不删除负担或承担者。",
    ),
    "merchant_regulated_trade": (
        "【结构占位·单项缓解】merchant_regulated_trade；不删除负担或承担者。",
    ),
    "southern_trade_terms": (
        "【结构占位·单项缓解】southern_trade_terms；不删除负担或承担者。",
    ),
    "existing_granary_ration": (
        "【结构占位·单项缓解】existing_granary_ration；不删除负担或承担者。",
    ),
    "decree_security_trade": (
        "【结构占位·单项缓解】decree_security_trade；不删除负担或承担者。",
    ),
    "decree_civic_ration": (
        "【结构占位·单项缓解】decree_civic_ration；不删除负担或承担者。",
    ),
    "decree_military_requisition": (
        "【结构占位·单项缓解】decree_military_requisition；不删除负担或承担者。",
    ),
    "wealth_trade": (
        "【结构占位·单项缓解】wealth_trade；不删除负担或承担者。",
    ),
    "loyalty_ration": (
        "【结构占位·单项缓解】loyalty_ration；不删除负担或承担者。",
    ),
    "power_requisition": (
        "【结构占位·单项缓解】power_requisition；不删除负担或承担者。",
    ),
    None: (
        "【结构占位·单项缓解】none；保留完整负担与承担者。",
    ),
}
_TASK8_STRUCTURAL_SOUTHERN_CONTRACT = {
    "none": (
        "【结构占位·南境购粮条件】none；只改变购买条件。",
    ),
    "free": (
        "【结构占位·南境购粮条件】free；只改变购买条件。",
    ),
    "ruler": (
        "【结构占位·南境购粮条件】ruler；只改变购买条件。",
    ),
    "vassal": (
        "【结构占位·南境购粮条件】vassal；只改变购买条件。",
    ),
    "outwit": (
        "【结构占位·南境购粮条件】outwit；只改变购买条件。",
    ),
    "fall": (
        "【结构占位·南境购粮条件】fall；只改变购买条件。",
    ),
}
```

Immediately after those constants, add the complete independent registry,
semantic-binding, wiring, and presentation expectations:

```python
_TASK8_COPY_REGISTRY_CONTRACT = {
    "S01": {
        "crisis_brief": (
            "【结构占位·危机简报】粮价一周内翻倍；市场限售；账面库存与实际行情不符。",
        ),
    },
    "S02": {
        "delegation": (
            "【结构占位·委托结果】neutral_delegate；不声明任何政策收益，也不替你作出政策决定。",
        ),
    },
    "S03": {
        "market_life": (
            "【结构占位·粮市】排队、争执、空粮袋；各方只掌握部分事实。",
        ),
    },
    "S04": {
        "emergency_council": (
            "【结构占位·紧急议事】商人、农户、守军与账房陈述各自处境。",
        ),
        "status": ("粮价：高｜库存：不足｜民情：不安",),
    },
    "S05": {
        "selected": {
            "first": (
                "【结构占位·已调查·粮市账本·first】抬价、断路、护运和资金占用共同影响粮价。{#winter_selected_market}",
            ),
            "second": (
                "【结构占位·已调查·粮市账本·second】抬价、断路、护运和资金占用共同影响粮价。{#winter_selected_market}",
            ),
        },
    },
    "S06": {
        "selected": {
            "first": (
                "【结构占位·已调查·村庄种粮·first】农户保粮主要为明年春播，并非单纯抗命。{#winter_selected_village}",
            ),
            "second": (
                "【结构占位·已调查·村庄种粮·second】农户保粮主要为明年春播，并非单纯抗命。{#winter_selected_village}",
            ),
        },
    },
    "S07": {
        "selected": {
            "first": (
                "【结构占位·已调查·城堡粮仓·first】受潮粮、旧账和层层报喜高估可用库存。{#winter_selected_granary}",
            ),
            "second": (
                "【结构占位·已调查·城堡粮仓·second】受潮粮、旧账和层层报喜高估可用库存。{#winter_selected_granary}",
            ),
        },
    },
    "S08": {
        "selected": {
            "first": (
                "【结构占位·已调查·北方商路·first】路线图与货单显示冰雪、损耗和周边采购共同造成到货不足。{#winter_selected_route}",
            ),
            "second": (
                "【结构占位·已调查·北方商路·second】路线图与货单显示冰雪、损耗和周边采购共同造成到货不足。{#winter_selected_route}",
            ),
        },
    },
    "S09": {
        "omitted": {
            "market": (
                "【结构占位·低可信报告·粮市账本】抬价与运输成本并存；信息未现场核实。{#winter_omitted_market}",
            ),
            "village": (
                "【结构占位·低可信报告·村庄种粮】藏粮可能用于春播；信息未现场核实。{#winter_omitted_village}",
            ),
            "granary": (
                "【结构占位·低可信报告·城堡粮仓】受潮与旧账可能高估库存；信息未现场核实。{#winter_omitted_granary}",
            ),
            "route": (
                "【结构占位·低可信报告·北方商路】冰雪与运输损耗可能拖慢到货；信息未现场核实。{#winter_omitted_route}",
            ),
        },
    },
    "S10": {
        "shared_cause": (
            "【结构占位·共同原因】多项因素共同造成缺口；不存在单一责任方，也没有单一措施能够解决全部缺口。{#winter_shared_cause}",
        ),
        "escalation": (
            "【结构占位·危机升级】粮车未按时抵达；城内出现抢购。",
        ),
    },
    "S11": {
        "policy_prompt": ("粮价：高｜库存：不足｜民情：不安",),
        "policy_bridge": {
            "trade": ("粮价：高｜库存：不足｜民情：不安",),
            "ration": ("粮价：高｜库存：不足｜民情：不安",),
            "requisition": ("粮价：高｜库存：不足｜民情：不安",),
        },
    },
    "S12": {
        "outcome": (
            "【结构占位·收益】trade_preserved_seed",
            "【结构占位·受益者】farmers_and_trade_route",
            "【结构占位·负担】trade_repayment_and_tight_rations",
            "【结构占位·承担者】treasury_and_townspeople",
            "【结构占位·行动物件】audited_purchase_contracts",
            "【结构占位·后续回响】trade_preserve_recovery",
        ),
        "mitigation": {**_TASK8_STRUCTURAL_MITIGATION_CONTRACT},
        "southern": {**_TASK8_STRUCTURAL_SOUTHERN_CONTRACT},
    },
    "S13": {
        "outcome": (
            "【结构占位·收益】trade_immediate_relief",
            "【结构占位·受益者】town_relief_recipients",
            "【结构占位·负担】trade_seed_shortfall",
            "【结构占位·承担者】treasury_and_farmers",
            "【结构占位·行动物件】market_grain_distribution",
            "【结构占位·后续回响】trade_feed_recovery",
        ),
        "mitigation": {**_TASK8_STRUCTURAL_MITIGATION_CONTRACT},
        "southern": {**_TASK8_STRUCTURAL_SOUTHERN_CONTRACT},
    },
    "S14": {
        "outcome": (
            "【结构占位·收益】ration_preserved_seed",
            "【结构占位·受益者】smallholders_and_farmers",
            "【结构占位·负担】ration_hunger_and_reserve_pressure",
            "【结构占位·承担者】garrison_and_townspeople",
            "【结构占位·行动物件】published_ration_ledgers",
            "【结构占位·后续回响】ration_preserve_recovery",
        ),
        "mitigation": {**_TASK8_STRUCTURAL_MITIGATION_CONTRACT},
        "southern": {},
    },
    "S15": {
        "outcome": (
            "【结构占位·收益】ration_broad_relief",
            "【结构占位·受益者】town_relief_recipients",
            "【结构占位·负担】ration_reserve_and_seed_loss",
            "【结构占位·承担者】garrison_and_farmers",
            "【结构占位·行动物件】open_granary_distribution",
            "【结构占位·后续回响】ration_feed_recovery",
        ),
        "mitigation": {**_TASK8_STRUCTURAL_MITIGATION_CONTRACT},
        "southern": {},
    },
    "S16": {
        "outcome": (
            "【结构占位·收益】requisition_preserved_seed",
            "【结构占位·受益者】smallholders_and_farmers",
            "【结构占位·负担】requisition_compensation_debt",
            "【结构占位·承担者】estates_and_lordship",
            "【结构占位·行动物件】sealed_compensation_vouchers",
            "【结构占位·后续回响】requisition_preserve_recovery",
        ),
        "mitigation": {**_TASK8_STRUCTURAL_MITIGATION_CONTRACT},
        "southern": {},
    },
    "S17": {
        "outcome": (
            "【结构占位·收益】requisition_immediate_relief",
            "【结构占位·受益者】broad_relief_recipients",
            "【结构占位·负担】requisition_debt_and_seed_shortfall",
            "【结构占位·承担者】estates_lordship_and_farmers",
            "【结构占位·行动物件】requisition_wagons_and_vouchers",
            "【结构占位·后续回响】requisition_feed_recovery",
        ),
        "mitigation": {**_TASK8_STRUCTURAL_MITIGATION_CONTRACT},
        "southern": {},
    },
    "S18": (),
}

_TASK8_VISIBLE_SEMANTIC_BINDINGS = {
    "winter_investigate_market": (
        ("S09", "omitted", "market", 0),
        '"[WINTER_COPY_REGISTRY[\'S09\'][\'omitted\'][\'market\'][0]]"',
    ),
    "winter_investigate_village": (
        ("S09", "omitted", "village", 0),
        '"[WINTER_COPY_REGISTRY[\'S09\'][\'omitted\'][\'village\'][0]]"',
    ),
    "winter_investigate_granary": (
        ("S09", "omitted", "granary", 0),
        '"[WINTER_COPY_REGISTRY[\'S09\'][\'omitted\'][\'granary\'][0]]"',
    ),
    "winter_investigate_route": (
        ("S09", "omitted", "route", 0),
        '"[WINTER_COPY_REGISTRY[\'S09\'][\'omitted\'][\'route\'][0]]"',
    ),
    "winter_crisis_escalates": (
        ("S10", "shared_cause", 0),
        '"[WINTER_COPY_REGISTRY[\'S10\'][\'shared_cause\'][0]]"',
    ),
    "winter_interlude_delegate": (
        ("S02", "delegation", 0),
        '"[WINTER_COPY_REGISTRY[\'S02\'][\'delegation\'][0]]"',
    ),
}

_TASK8_COPY_WIRING = {
    "winter_interlude_brief": (
        '"[WINTER_COPY_REGISTRY[\'S01\'][\'crisis_brief\'][0]]"',
    ),
    "winter_interlude_delegate": (
        '"[WINTER_COPY_REGISTRY[\'S02\'][\'delegation\'][0]]"',
    ),
    "winter_market_and_council": (
        '"[WINTER_COPY_REGISTRY[\'S03\'][\'market_life\'][0]]"',
        '"[WINTER_COPY_REGISTRY[\'S04\'][\'emergency_council\'][0]]"',
    ),
    "winter_investigation_menu": (
        '"[WINTER_COPY_REGISTRY[\'S04\'][\'status\'][0]]"',
    ),
    "winter_investigate_market": (
        '"[WINTER_COPY_REGISTRY[\'S09\'][\'omitted\'][\'market\'][0]]"',
        '"[WINTER_COPY_REGISTRY[\'S05\'][\'selected\'][visit_order][0]]"',
    ),
    "winter_investigate_village": (
        '"[WINTER_COPY_REGISTRY[\'S09\'][\'omitted\'][\'village\'][0]]"',
        '"[WINTER_COPY_REGISTRY[\'S06\'][\'selected\'][visit_order][0]]"',
    ),
    "winter_investigate_granary": (
        '"[WINTER_COPY_REGISTRY[\'S09\'][\'omitted\'][\'granary\'][0]]"',
        '"[WINTER_COPY_REGISTRY[\'S07\'][\'selected\'][visit_order][0]]"',
    ),
    "winter_investigate_route": (
        '"[WINTER_COPY_REGISTRY[\'S09\'][\'omitted\'][\'route\'][0]]"',
        '"[WINTER_COPY_REGISTRY[\'S08\'][\'selected\'][visit_order][0]]"',
    ),
    "winter_crisis_escalates": (
        '"[WINTER_COPY_REGISTRY[\'S10\'][\'shared_cause\'][0]]"',
        '"[WINTER_COPY_REGISTRY[\'S10\'][\'escalation\'][0]]"',
    ),
    "winter_choose_policy": (
        '"[WINTER_COPY_REGISTRY[\'S11\'][\'policy_prompt\'][0]]"',
    ),
    "winter_choose_seed_priority": (
        '"[WINTER_COPY_REGISTRY[\'S11\'][\'policy_bridge\'][policy][0]]"',
    ),
    "winter_consequence": (
        '"[_winter_outcome_copy[1][0]]"',
        '"[_winter_outcome_copy[1][1]]"',
        '"[_winter_outcome_copy[1][2]]"',
        '"[_winter_outcome_copy[1][3]]"',
        '"[_winter_outcome_copy[1][4]]"',
        '"[_winter_outcome_copy[1][5]]"',
        '"[WINTER_COPY_REGISTRY[_winter_outcome_copy[0]][\'southern\'][immediate_inputs[1]][0]]"',
        '"[WINTER_COPY_REGISTRY[_winter_outcome_copy[0]][\'mitigation\'][mitigation][0]]"',
        '"[WINTER_COPY_REGISTRY[_winter_outcome_copy[0]][\'mitigation\'][None][0]]"',
    ),
}

_TASK8_PRESENTATION_SIGNATURES = {
    "winter_interlude_start": (),
    "winter_interlude_brief": (
        "scene bg study",
        'play music "audio/music/winter_wind.ogg" fadeout 1.0 fadein 1.0 if_changed',
    ),
    "winter_interlude_delegate": (),
    "winter_market_and_council": (
        "scene bg market",
        'play music "audio/music/market_bustle.ogg" fadeout 1.0 fadein 1.0 if_changed',
        "scene bg council_hall",
    ),
    "winter_investigation_menu": (),
    "winter_choose_second_investigation": (),
    "winter_investigate_market": ("scene bg market",),
    "winter_investigate_village": ("scene bg village",),
    "winter_investigate_granary": ("scene bg study",),
    "winter_investigate_route": ("scene bg study",),
    "winter_omitted_reports": ("scene bg council_hall",),
    "winter_crisis_escalates": (
        "scene bg great_hall",
        'play music "audio/music/tension.ogg" fadeout 1.0 fadein 1.0 if_changed',
    ),
    "winter_choose_policy": (),
    "winter_choose_seed_priority": (),
    "winter_resolve_outcome": (),
    "winter_consequence": (
        "scene bg great_hall",
        'play music "audio/music/castle_calm.ogg" fadeout 1.0 fadein 1.0 if_changed',
    ),
    "winter_interlude_exit": (),
    "winter_interlude_cleanup": (),
}
```

Immediately before `_task7_control_signature`, add these complete parsers and
registry helpers:

```python
_TASK8_SAY_LITERAL_RE = re.compile(
    r"(?:(?P<speaker>[A-Za-z_][A-Za-z0-9_]*)[ \t]+)?"
    r"(?P<literal>\"(?:\\.|[^\"\\])*\"|'(?:\\.|[^'\\])*')\Z"
)
_TASK8_SAY_CANDIDATE_RE = re.compile(
    r"^(?:[A-Za-z_][A-Za-z0-9_]*[ \t]+)?[\"']"
)
_TASK8_PRESENTATION_RE = re.compile(
    r"^(?:scene|show|hide|play|stop|with|window)\b"
)
_TASK8_FORBIDDEN_INTERPOLATION_NODES = (
    ast.Await,
    ast.Call,
    ast.DictComp,
    ast.GeneratorExp,
    ast.Lambda,
    ast.ListComp,
    ast.NamedExpr,
    ast.SetComp,
    ast.Yield,
    ast.YieldFrom,
)


def _task8_guarded_interpolation_ast(source: str) -> str:
    tree = ast.parse(source, mode="eval")
    if any(
        isinstance(node, _TASK8_FORBIDDEN_INTERPOLATION_NODES)
        for node in ast.walk(tree)
    ):
        raise ValueError("active interpolation expression")
    return ast.dump(tree, include_attributes=False)


def _task8_static_say_signature(
    stripped: str,
) -> tuple | None:
    if _TASK8_SAY_CANDIDATE_RE.match(stripped) is None:
        return None
    match = _TASK8_SAY_LITERAL_RE.fullmatch(stripped)
    if match is None:
        return (("invalid_dialogue", stripped),)
    speaker = match.group("speaker")
    signature = []
    if speaker is not None:
        if speaker not in _TASK8_ALLOWED_SPEAKERS:
            return (("invalid_speaker", speaker),)
        signature.append(("speaker", speaker))
    try:
        dialogue = ast.literal_eval(match.group("literal"))
    except (SyntaxError, ValueError):
        return (("invalid_dialogue", stripped),)
    if type(dialogue) is not str:
        return (("invalid_dialogue", stripped),)
    for expression in _task7_interpolation_expressions(dialogue):
        try:
            signature.append(
                (
                    "interpolation",
                    _task8_guarded_interpolation_ast(expression),
                )
            )
        except (SyntaxError, ValueError):
            signature.append(("invalid_interpolation", expression))
    return tuple(signature)


def _task8_presentation_signature(body: str) -> tuple[str, ...]:
    return tuple(
        stripped
        for raw_line in body.splitlines()
        if (stripped := raw_line.strip())
        and not stripped.startswith("#")
        and _TASK8_PRESENTATION_RE.match(stripped) is not None
    )


def _task8_presentation_contract_violations(
    module_source: str,
) -> list[str]:
    violations = []
    for label, expected in _TASK8_PRESENTATION_SIGNATURES.items():
        try:
            actual = _task8_presentation_signature(
                _label_body(module_source, label)
            )
        except AssertionError:
            violations.append(f"missing Task 8 presentation label: {label}")
            continue
        if actual != expected:
            violations.append(f"Task 8 presentation mismatch: {label}")
    return violations


def _task8_winter_namespace(module_source: str) -> dict[str, object]:
    fragments = [
        fragment
        for fragment in _renpy_python_fragments(module_source)
        if "WINTER_OUTCOME_CONTRACTS" in fragment
    ]
    if len(fragments) != 1:
        raise AssertionError("winter init fragment is not unique")
    namespace: dict[str, object] = {}
    exec(compile(fragments[0], str(WINTER_MODULE), "exec"), namespace)
    return namespace


def _task8_registry_value(
    registry: object,
    path: tuple[object, ...],
) -> object:
    value = registry
    for key in path:
        value = value[key]
    return value


def _task8_copy_strings(value: object) -> tuple[str, ...]:
    if type(value) is str:
        return (value,)
    if type(value) is tuple:
        return tuple(
            text
            for item in value
            for text in _task8_copy_strings(item)
        )
    if type(value) is dict:
        return tuple(
            text
            for item in value.values()
            for text in _task8_copy_strings(item)
        )
    raise AssertionError(f"unsupported copy-registry value: {type(value)!r}")


def _task8_copy_wiring_signature(body: str) -> tuple[str, ...]:
    signature = []
    for raw_line in body.splitlines():
        stripped = raw_line.strip()
        if (
            _TASK8_SAY_CANDIDATE_RE.match(stripped) is not None
            and (
                "WINTER_COPY_REGISTRY" in stripped
                or "_winter_outcome_copy" in stripped
            )
        ):
            signature.append(stripped)
    return tuple(signature)
```

Replace `_task7_control_signature` completely with this version. The
content-free presentation slot remains in the control signature because the
existing `omitted_report_visits_market` mutation moves a scene across a branch
without changing the presentation-only tuple:

```python
def _task7_control_signature(body: str) -> tuple:
    """Return every Python-bearing Task 7 Ren'Py control operation in order."""
    signature = []
    for raw_line in body.splitlines():
        stripped = raw_line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("$"):
            try:
                tree = ast.parse(stripped[1:].strip())
                signature.append(
                    ("python", ast.dump(tree, include_attributes=False))
                )
            except SyntaxError:
                signature.append(("invalid_python", stripped))
            continue
        conditional = re.fullmatch(r"(if|elif)\s+(.+):", stripped)
        if conditional:
            try:
                signature.append(
                    (
                        conditional.group(1),
                        _task7_eval_ast(conditional.group(2)),
                    )
                )
            except SyntaxError:
                signature.append(("invalid_condition", stripped))
            continue
        if stripped == "else:":
            signature.append(("else",))
            continue
        if stripped == "menu:":
            signature.append(("menu",))
            continue
        choice = re.fullmatch(
            r'''((["']).*\2)(?:\s+if\s+(.+))?:''',
            stripped,
        )
        if choice:
            try:
                choice_text = ast.literal_eval(choice.group(1))
            except (SyntaxError, ValueError):
                signature.append(("invalid_choice_text", stripped))
                continue
            for expression in _task7_interpolation_expressions(choice_text):
                try:
                    signature.append(
                        (
                            "interpolation",
                            _task8_guarded_interpolation_ast(expression),
                        )
                    )
                except (SyntaxError, ValueError):
                    signature.append(("invalid_interpolation", expression))
            condition = choice.group(3)
            if condition is None:
                signature.append(("choice", None))
            else:
                try:
                    signature.append(
                        ("choice", _task7_eval_ast(condition))
                    )
                except SyntaxError:
                    signature.append(("invalid_choice", stripped))
            continue
        call = re.fullmatch(
            r"call\s+([A-Za-z_][A-Za-z0-9_]*)"
            r"(?:\((.*)\))?"
            r"(?:\s+from\s+([A-Za-z_][A-Za-z0-9_]*))?",
            stripped,
        )
        if call:
            arguments = call.group(2)
            try:
                argument_ast = (
                    None
                    if arguments is None
                    else _task7_call_ast(arguments)
                )
            except SyntaxError:
                argument_ast = "<invalid>"
            signature.append(
                ("call", call.group(1), argument_ast, call.group(3))
            )
            continue
        if stripped.startswith("call "):
            signature.append(("invalid_call", stripped))
            continue
        jump = re.fullmatch(
            r"jump\s+([A-Za-z_][A-Za-z0-9_]*)",
            stripped,
        )
        if jump:
            signature.append(("jump", jump.group(1)))
            continue
        if stripped.startswith("jump "):
            signature.append(("invalid_jump", stripped))
            continue
        if stripped == "return":
            signature.append(("return",))
            continue
        if re.match(r"(?:while|for|python)\b", stripped):
            signature.append(("unapproved_control", stripped))
            continue
        say_signature = _task8_static_say_signature(stripped)
        if say_signature is not None:
            signature.extend(say_signature)
            continue
        if _TASK8_PRESENTATION_RE.match(stripped) is not None:
            signature.append(("presentation_slot",))
            continue
        signature.append(("unapproved_statement", stripped))
    return tuple(signature)
```

Replace `_task7_visible_semantic_contract_violations` completely. This keeps
the six expected texts independent while moving their production location into
the registry and pinning each exact label lookup:

```python
def _task7_visible_semantic_contract_violations(
    module_source: str,
) -> list[str]:
    """Check test-owned, player-visible Task 7 structural semantics."""
    violations = []
    try:
        namespace = _task8_winter_namespace(module_source)
        registry = namespace["WINTER_COPY_REGISTRY"]
    except (AssertionError, KeyError, SyntaxError, TypeError, ValueError) as error:
        return [f"Task 8 copy registry unavailable: {error}"]
    for label, expected_text in TASK7_VISIBLE_SEMANTIC_CONTRACT.items():
        path, exact_statement = _TASK8_VISIBLE_SEMANTIC_BINDINGS[label]
        try:
            actual_text = _task8_registry_value(registry, path)
            body = _label_body(module_source, label)
        except (AssertionError, KeyError, TypeError):
            violations.append(f"missing Task 7 semantic binding: {label}")
            continue
        if (
            type(actual_text) is not str
            or actual_text.count(expected_text) != 1
        ):
            violations.append(f"Task 7 visible semantic mismatch: {label}")
        if body.count(exact_statement) != 1:
            violations.append(f"Task 7 semantic wiring mismatch: {label}")
    return violations
```

Replace `_TASK7_LABEL_PYTHON` with the following complete mapping. This is the
only newly approved local assignment; the fragment total rises from five to
six:

```python
_TASK7_LABEL_PYTHON = {
    "winter_interlude_brief": ('winter_interlude_status = "active"',),
    "winter_market_and_council": ('set_weather("snow")',),
    "winter_omitted_reports": (
        "winter_investigations = normalize_winter_investigations((first, second))",
    ),
    "winter_resolve_outcome": (
        "immediate_inputs = (gov_merchant_outcome, southern_outcome, built_granary, first_decree, wealth, loyalty, power)",
        "mitigation = select_winter_mitigation(policy, seed_priority, winter_investigations, immediate_inputs)",
    ),
    "winter_consequence": (
        "_winter_outcome_copy = winter_outcome_copy(winter_policy, winter_seed_priority, outcome)",
    ),
}
```

Replace `_winter_module_write_violations` completely with the following
version. Its only behavioral addition is the independent presentation
contract; its existing top-level, AST write, approved-fragment, marker, control,
and visible-semantic enforcement remains literal:

```python
def _winter_module_write_violations(
    module_source: str,
    store_defaults: set[str],
    persistent_defaults: set[str],
) -> list[str]:
    """Return state writes forbidden inside the winter kernel."""
    del store_defaults, persistent_defaults
    violations = []
    allowed_defaults = {
        "winter_interlude_status",
        "winter_investigations",
        "winter_policy",
        "winter_seed_priority",
    }
    seen_defaults = set()
    init_block_count = 0
    for raw_line in module_source.splitlines():
        stripped = raw_line.strip()
        if not stripped or stripped.startswith("#") or raw_line != raw_line.lstrip():
            continue
        default_match = re.match(
            r"^default\s+([A-Za-z_][A-Za-z0-9_]*)\s*=",
            stripped,
        )
        if default_match and default_match.group(1) in allowed_defaults:
            name = default_match.group(1)
            if name in seen_defaults:
                violations.append(f"duplicate winter default: {name}")
            seen_defaults.add(name)
        elif re.fullmatch(r"init python:\s*(?:#.*)?", stripped):
            init_block_count += 1
            if init_block_count > 1:
                violations.append("more than one init python block")
        elif re.fullmatch(
            r"label\s+[A-Za-z_][A-Za-z0-9_]*(?:\([^)]*\))?\s*:",
            stripped,
        ):
            pass
        else:
            violations.append(
                f"unapproved top-level Ren'Py statement: {stripped}"
            )

    trees = []
    task5_fragment_counts = {}
    task7_fragment_counts = {}
    for label, fragment in _renpy_python_fragments_with_labels(module_source):
        try:
            tree = ast.parse(fragment)
        except SyntaxError as error:
            violations.append(f"Python parse failure: {error.msg}")
            continue
        if _is_approved_task5_label_fragment(label, tree):
            key = (label, ast.dump(tree, include_attributes=False))
            task5_fragment_counts[key] = task5_fragment_counts.get(key, 0) + 1
            if task5_fragment_counts[key] > 1:
                violations.append(
                    f"duplicate approved Task 5 label fragment: {label}"
                )
            continue
        if _is_approved_task7_label_fragment(label, tree):
            key = (label, ast.dump(tree, include_attributes=False))
            task7_fragment_counts[key] = task7_fragment_counts.get(key, 0) + 1
            if task7_fragment_counts[key] > 1:
                violations.append(
                    f"duplicate approved Task 7 label fragment: {label}"
                )
            continue
        trees.append(tree)
    defined_functions = {
        node.name
        for tree in trees
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    marker_appends = 0
    for tree in trees:
        visitor = _WinterWriteVisitor(defined_functions)
        visitor.visit(tree)
        violations.extend(visitor.violations)
        marker_appends += visitor.marker_appends
    if marker_appends > 1:
        violations.append("more than one governance marker append")
    if "label winter_interlude_brief:" in module_source:
        violations.extend(_task7_control_contract_violations(module_source))
        violations.extend(
            _task8_presentation_contract_violations(module_source)
        )
        violations.extend(
            _task7_visible_semantic_contract_violations(module_source)
        )
    return violations
```

Immediately before `_TASK7_CONTROL_SIGNATURES`, add these complete overrides
and apply them once. The original templates for the six unchanged control-only
labels remain intact; every label whose new registry lookup contributes an
interpolation AST is replaced here:

```python
_TASK8_CONTROL_TEMPLATE_OVERRIDES = {
    "winter_interlude_brief": '''
scene bg study
play music "audio/music/winter_wind.ogg" fadeout 1.0 fadein 1.0 if_changed
"[WINTER_COPY_REGISTRY['S01']['crisis_brief'][0]]"
menu:
    "active":
        $ winter_interlude_status = "active"
        call winter_market_and_council from _call_winter_market_and_council
    "delegate":
        call winter_interlude_delegate from _call_winter_interlude_delegate
return
''',
    "winter_interlude_delegate": '''
$ apply_winter_delegation()
"[WINTER_COPY_REGISTRY['S02']['delegation'][0]]"
return
''',
    "winter_market_and_council": '''
$ set_weather("snow")
scene bg market
play music "audio/music/market_bustle.ogg" fadeout 1.0 fadein 1.0 if_changed
"[WINTER_COPY_REGISTRY['S03']['market_life'][0]]"
scene bg council_hall
"[WINTER_COPY_REGISTRY['S04']['emergency_council'][0]]"
call winter_investigation_menu from _call_winter_investigation_menu
return
''',
    "winter_investigation_menu": '''
"[WINTER_COPY_REGISTRY['S04']['status'][0]]"
menu:
    "market":
        call winter_investigate_market("first") from _call_winter_first_market
        call winter_choose_second_investigation("market") from _call_winter_second_after_market
    "village":
        call winter_investigate_village("first") from _call_winter_first_village
        call winter_choose_second_investigation("village") from _call_winter_second_after_village
    "granary":
        call winter_investigate_granary("first") from _call_winter_first_granary
        call winter_choose_second_investigation("granary") from _call_winter_second_after_granary
    "route":
        call winter_investigate_route("first") from _call_winter_first_route
        call winter_choose_second_investigation("route") from _call_winter_second_after_route
return
''',
    "winter_investigate_market": '''
if visit_order == "omitted":
"[WINTER_COPY_REGISTRY['S09']['omitted']['market'][0]]"
else:
scene bg market
"[WINTER_COPY_REGISTRY['S05']['selected'][visit_order][0]]"
return
''',
    "winter_investigate_village": '''
if visit_order == "omitted":
"[WINTER_COPY_REGISTRY['S09']['omitted']['village'][0]]"
else:
scene bg village
"[WINTER_COPY_REGISTRY['S06']['selected'][visit_order][0]]"
return
''',
    "winter_investigate_granary": '''
if visit_order == "omitted":
"[WINTER_COPY_REGISTRY['S09']['omitted']['granary'][0]]"
else:
scene bg study
"[WINTER_COPY_REGISTRY['S07']['selected'][visit_order][0]]"
return
''',
    "winter_investigate_route": '''
if visit_order == "omitted":
"[WINTER_COPY_REGISTRY['S09']['omitted']['route'][0]]"
else:
scene bg study
"[WINTER_COPY_REGISTRY['S08']['selected'][visit_order][0]]"
return
''',
    "winter_crisis_escalates": '''
scene bg great_hall
play music "audio/music/tension.ogg" fadeout 1.0 fadein 1.0 if_changed
"[WINTER_COPY_REGISTRY['S10']['shared_cause'][0]]"
"[WINTER_COPY_REGISTRY['S10']['escalation'][0]]"
call winter_choose_policy from _call_winter_choose_policy
return
''',
    "winter_choose_policy": '''
"[WINTER_COPY_REGISTRY['S11']['policy_prompt'][0]]"
menu:
    "trade":
        call winter_choose_seed_priority("trade") from _call_winter_seed_trade
    "ration":
        call winter_choose_seed_priority("ration") from _call_winter_seed_ration
    "requisition":
        call winter_choose_seed_priority("requisition") from _call_winter_seed_requisition
return
''',
    "winter_choose_seed_priority": '''
"[WINTER_COPY_REGISTRY['S11']['policy_bridge'][policy][0]]"
menu:
    "preserve":
        call winter_resolve_outcome(policy, "preserve") from _call_winter_resolve_preserve
    "feed_now":
        call winter_resolve_outcome(policy, "feed_now") from _call_winter_resolve_feed_now
return
''',
    "winter_consequence": '''
scene bg great_hall
play music "audio/music/castle_calm.ogg" fadeout 1.0 fadein 1.0 if_changed
$ _winter_outcome_copy = winter_outcome_copy(winter_policy, winter_seed_priority, outcome)
"[_winter_outcome_copy[1][0]]"
"[_winter_outcome_copy[1][1]]"
"[_winter_outcome_copy[1][2]]"
"[_winter_outcome_copy[1][3]]"
"[_winter_outcome_copy[1][4]]"
"[_winter_outcome_copy[1][5]]"
if winter_policy == "trade" and immediate_inputs[1] not in ("", "delegated"):
"[WINTER_COPY_REGISTRY[_winter_outcome_copy[0]]['southern'][immediate_inputs[1]][0]]"
if mitigation is not None:
"[WINTER_COPY_REGISTRY[_winter_outcome_copy[0]]['mitigation'][mitigation][0]]"
else:
"[WINTER_COPY_REGISTRY[_winter_outcome_copy[0]]['mitigation'][None][0]]"
return
''',
}
_TASK7_CONTROL_TEMPLATES.update(_TASK8_CONTROL_TEMPLATE_OVERRIDES)
```

In the existing Task 7 control method, insert the following update immediately
after the closing brace of `mutation_probes` and before its existing length
assertion. Each candidate must differ from `self.source`, must make
`_task7_control_contract_violations` nonempty, and must make
`_winter_module_write_violations` nonempty through the method's existing loop:

```python
mutation_probes.update(
    {
        "outcome_copy_argument_call": self.source.replace(
            "$ _winter_outcome_copy = winter_outcome_copy(winter_policy, winter_seed_priority, outcome)",
            "$ _winter_outcome_copy = winter_outcome_copy(change_stat(1), winter_seed_priority, outcome)",
            1,
        ),
        "outcome_copy_named_expression": self.source.replace(
            "$ _winter_outcome_copy = winter_outcome_copy(winter_policy, winter_seed_priority, outcome)",
            "$ _winter_outcome_copy = winter_outcome_copy((winter_policy := 'trade'), winter_seed_priority, outcome)",
            1,
        ),
    }
)
```

In that method's existing mutation loop, replace the loop with this exact
version. `play_expression_mutator` deliberately preserves one content-free
presentation slot, so its exact-content failure belongs to the independent
presentation contract; every other existing mutation must still alter the
control signature:

```python
for name, candidate in mutation_probes.items():
    with self.subTest(mutation=name):
        self.assertNotEqual(candidate, self.source)
        control_violations = _task7_control_contract_violations(candidate)
        presentation_violations = (
            _task8_presentation_contract_violations(candidate)
        )
        if name == "play_expression_mutator":
            self.assertEqual(control_violations, [])
            self.assertTrue(presentation_violations)
        else:
            self.assertTrue(control_violations)
        store_defaults, persistent_defaults = _project_default_inventory()
        self.assertTrue(
            _winter_module_write_violations(
                candidate,
                store_defaults,
                persistent_defaults,
            )
        )
```

Replace `WinterStoryGraphContractTests._winter_kernel_namespace` with this
complete method so the class and the global semantic contract execute the same
unique init fragment:

```python
def _winter_kernel_namespace(self):
    return _task8_winter_namespace(self.source)
```

Replace only the local `signatures` tuple in
`WinterModuleContractTests.test_state_enum_and_public_helper_signatures_exist`
with this complete tuple:

```python
signatures = (
    "normalize_winter_investigations(values)",
    "resolve_winter_interlude_context(raw_snapshot, projection)",
    "get_winter_context(outside=True)",
    "apply_winter_delegation()",
    "finalize_winter_interlude(policy, seed_priority, investigations)",
    "mark_winter_legacy()",
    "migrate_winter_interlude_state()",
    "winter_legacy_famine_success()",
    "select_winter_mitigation(policy, seed_priority, investigations, immediate_inputs)",
    "winter_outcome_copy(policy, seed_priority, outcome)",
)
```

Replace
`WinterStoryGraphContractTests.test_qualitative_lines_assets_and_semantic_markers_are_structural`
completely. Registry source contains five current status literals, selected
markers occur once in each `first` and `second` literal, while runtime wiring
still displays one status line at each of the three decision labels:

```python
def test_qualitative_lines_assets_and_semantic_markers_are_structural(self):
    qualitative = "粮价：高｜库存：不足｜民情：不安"
    namespace = self._winter_kernel_namespace()
    registry = namespace["WINTER_COPY_REGISTRY"]
    self.assertEqual(self.source.count(qualitative), 5)
    self.assertEqual(registry["S04"]["status"], (qualitative,))
    self.assertEqual(registry["S11"]["policy_prompt"], (qualitative,))
    self.assertEqual(
        registry["S11"]["policy_bridge"],
        {
            "trade": (qualitative,),
            "ration": (qualitative,),
            "requisition": (qualitative,),
        },
    )
    qualitative_wiring = {
        "winter_investigation_menu": (
            '"[WINTER_COPY_REGISTRY[\'S04\'][\'status\'][0]]"'
        ),
        "winter_choose_policy": (
            '"[WINTER_COPY_REGISTRY[\'S11\'][\'policy_prompt\'][0]]"'
        ),
        "winter_choose_seed_priority": (
            '"[WINTER_COPY_REGISTRY[\'S11\'][\'policy_bridge\'][policy][0]]"'
        ),
    }
    for label, statement in qualitative_wiring.items():
        with self.subTest(qualitative_label=label):
            self.assertEqual(_label_body(self.source, label).count(statement), 1)

    audio_contract = (
        ("winter_interlude_brief", 'play music "audio/music/winter_wind.ogg"'),
        (
            "winter_market_and_council",
            'play music "audio/music/market_bustle.ogg"',
        ),
        ("winter_crisis_escalates", 'play music "audio/music/tension.ogg"'),
        ("winter_consequence", 'play music "audio/music/castle_calm.ogg"'),
    )
    for label, statement in audio_contract:
        with self.subTest(audio_label=label):
            body = _label_body(self.source, label)
            self.assertEqual(body.count(statement), 1)
            self.assertNotIn("channel=", body)

    background_contract = {
        "winter_market_and_council": (
            "scene bg market",
            "scene bg council_hall",
        ),
        "winter_investigate_market": ("scene bg market",),
        "winter_investigate_village": ("scene bg village",),
        "winter_investigate_granary": (
            "scene bg study",
            "TEMPORARY ART MISMATCH",
        ),
        "winter_investigate_route": ("scene bg study",),
        "winter_omitted_reports": ("scene bg council_hall",),
        "winter_crisis_escalates": ("scene bg great_hall",),
        "winter_consequence": ("scene bg great_hall",),
    }
    for label, statements in background_contract.items():
        body = _label_body(self.source, label)
        for statement in statements:
            with self.subTest(background_label=label, statement=statement):
                self.assertIn(statement, body)
    selected_scenes = {
        "winter_investigate_market": "scene bg market",
        "winter_investigate_village": "scene bg village",
        "winter_investigate_granary": "scene bg study",
        "winter_investigate_route": "scene bg study",
    }
    for label, scene_statement in selected_scenes.items():
        with self.subTest(selected_scene_label=label):
            body = _label_body(self.source, label)
            omitted_at = body.index('if visit_order == "omitted":')
            selected_at = body.index("else:", omitted_at)
            scene_at = body.index(scene_statement)
            self.assertLess(omitted_at, selected_at)
            self.assertLess(selected_at, scene_at)
            self.assertEqual(body.count(scene_statement), 1)
    omitted_body = _label_body(self.source, "winter_omitted_reports")
    self.assertLess(
        omitted_body.index("scene bg council_hall"),
        omitted_body.index("call winter_investigate_market"),
    )
    self.assertNotRegex(
        self.source,
        r"(?m)^\s*scene\s+bg(?:_|\s+)winter_granary\b",
    )
    self.assertNotRegex(
        self.source,
        r"(?i)(?:text_size|size)\s+(?:1[0-9]|2[0-4])\b",
    )

    for key in ("market", "village", "granary", "route"):
        with self.subTest(marker=key):
            self.assertEqual(
                self.source.count("{#winter_selected_" + key + "}"),
                2,
            )
            self.assertEqual(
                self.source.count("{#winter_omitted_" + key + "}"),
                1,
            )
    self.assertEqual(self.source.count("{#winter_shared_cause}"), 1)
```

Add exactly the following three methods to
`WinterStoryGraphContractTests`. Do not add another `test_*` method in this
slice:

```python
def test_task8_static_speaker_and_presentation_contracts_are_exact(self):
    self.assertEqual(_task8_presentation_contract_violations(self.source), [])
    self.assertEqual(_task7_control_signature('"plain narration"'), ())
    self.assertEqual(
        _task7_control_signature('accountant "The ledger is open."'),
        (("speaker", "accountant"),),
    )
    self.assertEqual(
        _task7_control_signature('player "[winter_policy]"'),
        (
            ("speaker", "player"),
            ("interpolation", _task7_eval_ast("winter_policy")),
        ),
    )
    self.assertEqual(
        _task7_control_signature("scene bg study"),
        (("presentation_slot",),),
    )

    invalid_say_cases = {
        "unknown speaker": 'dynamic_speaker "No."',
        "two literals": 'accountant "One." "Two."',
        "formatted string": 'f"{change_stat(1)}"',
        "call speaker": 'accountant("No.")',
        "call interpolation": '"[change_stat(1)]"',
        "named interpolation": '"[(winter_policy := \'trade\')]"',
        "unbalanced interpolation": '"[winter_policy"',
    }
    for name, body in invalid_say_cases.items():
        with self.subTest(invalid_say=name):
            signature = _task7_control_signature(body)
            self.assertTrue(signature)
            self.assertTrue(
                any(
                    item[0].startswith(("invalid", "unapproved"))
                    for item in signature
                )
            )

    presentation_mutations = {
        "dynamic scene": self.source.replace(
            "label winter_interlude_brief:\n    scene bg study",
            "label winter_interlude_brief:\n    scene expression change_stat(1)",
            1,
        ),
        "dynamic audio": self.source.replace(
            'play music "audio/music/winter_wind.ogg" fadeout 1.0 fadein 1.0 if_changed',
            "play expression change_stat(1)",
            1,
        ),
        "reordered market": self.source.replace(
            "    scene bg market\n"
            '    play music "audio/music/market_bustle.ogg" fadeout 1.0 fadein 1.0 if_changed\n',
            '    play music "audio/music/market_bustle.ogg" fadeout 1.0 fadein 1.0 if_changed\n'
            "    scene bg market\n",
            1,
        ),
        "missing consequence scene": self.source.replace(
            "label winter_consequence(outcome, mitigation, immediate_inputs):\n"
            "    scene bg great_hall\n",
            "label winter_consequence(outcome, mitigation, immediate_inputs):\n",
            1,
        ),
    }
    store_defaults, persistent_defaults = _project_default_inventory()
    for name, candidate in presentation_mutations.items():
        with self.subTest(presentation_mutation=name):
            self.assertNotEqual(candidate, self.source)
            self.assertTrue(
                _task8_presentation_contract_violations(candidate)
            )
            self.assertTrue(
                _winter_module_write_violations(
                    candidate,
                    store_defaults,
                    persistent_defaults,
                )
            )


def test_task8_current_approved_scene_copy_contracts_are_exact(self):
    namespace = self._winter_kernel_namespace()
    self.assertIn(
        "WINTER_COPY_REGISTRY",
        namespace,
        "missing production WINTER_COPY_REGISTRY scaffold",
    )
    registry = namespace["WINTER_COPY_REGISTRY"]
    self.assertEqual(tuple(registry), _TASK8_SCENE_ORDER)
    self.assertEqual(registry, _TASK8_COPY_REGISTRY_CONTRACT)
    self.assertEqual(
        _TASK8_APPROVED_SCENE_IDS,
        _TASK8_SCENE_ORDER[: len(_TASK8_APPROVED_SCENE_IDS)],
    )
    for scene_id in _TASK8_APPROVED_SCENE_IDS:
        with self.subTest(approved_scene=scene_id):
            approved_strings = _task8_copy_strings(registry[scene_id])
            self.assertTrue(approved_strings)
            self.assertTrue(
                all("结构占位" not in text for text in approved_strings)
            )

    for label, expected in _TASK8_COPY_WIRING.items():
        with self.subTest(copy_wiring=label):
            self.assertEqual(
                _task8_copy_wiring_signature(
                    _label_body(self.source, label)
                ),
                expected,
            )
    self.assertEqual(registry["S18"], ())
    self.assertIsNone(
        re.search(
            r"WINTER_COPY_REGISTRY\[['\"]S18['\"]\]",
            self.source,
        )
    )

    with self.assertRaises(KeyError):
        registry["S05"]["selected"]["omitted"]
    with self.assertRaises(KeyError):
        registry["S09"]["omitted"]["unknown"]
    with self.assertRaises(KeyError):
        registry["S11"]["policy_bridge"]["delegated"]
    for scene_id in ("S12", "S13", "S14", "S15", "S16", "S17"):
        with self.subTest(outcome_scene=scene_id):
            entry = registry[scene_id]
            self.assertEqual(
                tuple(entry),
                ("outcome", "mitigation", "southern"),
            )
            self.assertEqual(
                tuple(entry["mitigation"]),
                _TASK8_MITIGATION_KEYS,
            )
            with self.assertRaises(KeyError):
                entry["mitigation"]["unknown"]
            expected_southern = (
                _TASK8_SOUTHERN_KEYS
                if scene_id in ("S12", "S13")
                else ()
            )
            self.assertEqual(tuple(entry["southern"]), expected_southern)
            with self.assertRaises(KeyError):
                entry["southern"]["delegated"]


def test_task8_outcome_copy_rejects_route_contract_and_registry_drift(self):
    namespace = self._winter_kernel_namespace()
    self.assertEqual(
        namespace["WINTER_OUTCOME_SCENES"],
        _TASK8_OUTCOME_SCENE_CONTRACT,
    )
    self.assertEqual(
        namespace["WINTER_OUTCOME_CONTRACTS"],
        _TASK8_OUTCOME_SYMBOLIC_CONTRACT,
    )
    self.assertEqual(
        namespace["WINTER_MITIGATION_KEYS"],
        _TASK8_MITIGATION_KEYS,
    )
    self.assertEqual(
        namespace["WINTER_SOUTHERN_KEYS"],
        _TASK8_SOUTHERN_KEYS,
    )
    helper = namespace["winter_outcome_copy"]
    registry = namespace["WINTER_COPY_REGISTRY"]
    for route, scene_id in _TASK8_OUTCOME_SCENE_CONTRACT.items():
        with self.subTest(route=route):
            actual_scene, actual_lines = helper(
                route[0],
                route[1],
                _TASK8_OUTCOME_SYMBOLIC_CONTRACT[route],
            )
            self.assertEqual(actual_scene, scene_id)
            self.assertEqual(actual_lines, registry[scene_id]["outcome"])

    with self.assertRaises(KeyError):
        helper(
            "delegated",
            "neutral",
            _TASK8_OUTCOME_SYMBOLIC_CONTRACT[("trade", "preserve")],
        )

    class DictSubclass(dict):
        pass

    with self.assertRaises(ValueError):
        helper(
            "trade",
            "preserve",
            DictSubclass(
                _TASK8_OUTCOME_SYMBOLIC_CONTRACT[("trade", "preserve")]
            ),
        )
    symbolic_drift = dict(
        _TASK8_OUTCOME_SYMBOLIC_CONTRACT[("trade", "preserve")]
    )
    symbolic_drift["benefit"] = "drift"
    with self.assertRaises(ValueError):
        helper("trade", "preserve", symbolic_drift)

    outcome_namespace = self._winter_kernel_namespace()
    outcome_namespace["WINTER_COPY_REGISTRY"]["S12"]["outcome"] = (
        "drift",
    )
    with self.assertRaises(ValueError):
        outcome_namespace["winter_outcome_copy"](
            "trade",
            "preserve",
            _TASK8_OUTCOME_SYMBOLIC_CONTRACT[("trade", "preserve")],
        )

    mitigation_namespace = self._winter_kernel_namespace()
    del mitigation_namespace["WINTER_COPY_REGISTRY"]["S12"]["mitigation"][
        "market_trade"
    ]
    with self.assertRaises(ValueError):
        mitigation_namespace["winter_outcome_copy"](
            "trade",
            "preserve",
            _TASK8_OUTCOME_SYMBOLIC_CONTRACT[("trade", "preserve")],
        )

    southern_namespace = self._winter_kernel_namespace()
    southern_namespace["WINTER_COPY_REGISTRY"]["S14"]["southern"][
        "free"
    ] = ("drift",)
    with self.assertRaises(ValueError):
        southern_namespace["winter_outcome_copy"](
            "ration",
            "preserve",
            _TASK8_OUTCOME_SYMBOLIC_CONTRACT[("ration", "preserve")],
        )

    trade_southern_namespace = self._winter_kernel_namespace()
    del trade_southern_namespace["WINTER_COPY_REGISTRY"]["S13"]["southern"][
        "fall"
    ]
    with self.assertRaises(ValueError):
        trade_southern_namespace["winter_outcome_copy"](
            "trade",
            "feed_now",
            _TASK8_OUTCOME_SYMBOLIC_CONTRACT[("trade", "feed_now")],
        )

    assignment = (
        "$ _winter_outcome_copy = winter_outcome_copy("
        "winter_policy, winter_seed_priority, outcome)"
    )
    self.assertEqual(
        _label_body(self.source, "winter_consequence").count(assignment),
        1,
    )
    self.assertEqual(
        self.source.count(
            "call winter_consequence("
            "WINTER_OUTCOME_CONTRACTS[(policy, seed_priority)], "
            "mitigation, immediate_inputs) from _call_winter_consequence"
        ),
        1,
    )
```

In the existing capability method
`WinterNarrativeCapabilityCheckerTests.test_batch_and_final_documents_are_exact_and_phase_sensitive`,
immediately after its checker imports and before `observed`, insert this exact
independent catalog and loader contract:

```python
expected_batch_ids = (
    "Tools.test_governance_winter_interlude."
    "WinterStoryGraphContractTests."
    "test_complete_story_graph_labels_exist_exactly_once",
    "Tools.test_governance_winter_interlude."
    "WinterStoryGraphContractTests."
    "test_six_outcome_contracts_have_exact_nonempty_symbolic_slots",
    "Tools.test_governance_winter_interlude."
    "WinterStoryGraphContractTests."
    "test_qualitative_lines_assets_and_semantic_markers_are_structural",
    "Tools.test_governance_winter_interlude."
    "WinterStoryGraphContractTests."
    "test_all_task7_renpy_control_expressions_are_exact_and_guarded",
    "Tools.test_governance_winter_interlude."
    "WinterStoryGraphContractTests."
    "test_player_visible_semantics_are_independent_and_fail_closed",
    "Tools.test_governance_winter_interlude."
    "WinterStoryGraphContractTests."
    "test_task8_current_approved_scene_copy_contracts_are_exact",
)
self.assertEqual(BATCH_CONTRACT_TEST_IDS, expected_batch_ids)
batch_loader = unittest.TestLoader()
batch_suite = batch_loader.loadTestsFromNames(BATCH_CONTRACT_TEST_IDS)
self.assertEqual(batch_loader.errors, [])
self.assertEqual(
    batch_suite.countTestCases(),
    len(BATCH_CONTRACT_TEST_IDS),
)
```

The test-side edit now defines exactly three new governance methods, but
production and the checker catalog are still unchanged.

- [ ] **Step 3: Capture the two behavior-specific REDs**

Run only the new aggregate and the existing capability catalog method. Do not
run a complete module, discovery, Ren'Py, or the public gate during RED:

```powershell
$captureDirectory = '.superpowers/sdd'
New-Item -ItemType Directory -Path $captureDirectory -Force | Out-Null
$aggregateId = (
  'Tools.test_governance_winter_interlude.' +
  'WinterStoryGraphContractTests.' +
  'test_task8_current_approved_scene_copy_contracts_are_exact'
)
$aggregateRed = & python -B -m unittest $aggregateId -v 2>&1
$aggregateExit = $LASTEXITCODE
$aggregatePath = Join-Path $captureDirectory 'task9-copy-aggregate-red.txt'
$aggregateRed | Set-Content -LiteralPath $aggregatePath -Encoding UTF8
$aggregateText = $aggregateRed -join [Environment]::NewLine
if ($aggregateExit -eq 0 -or
    $aggregateText -notmatch 'Ran 1 test' -or
    $aggregateText -notmatch 'FAILED \(failures=1\)' -or
    $aggregateText -match '(?m)^ERROR:') {
  throw 'Copy-registry aggregate RED was not one failure and zero errors.'
}
if ($aggregateText -notmatch 'missing production WINTER_COPY_REGISTRY scaffold') {
  throw 'Copy-registry aggregate RED failed for the wrong reason.'
}

$catalogId = (
  'Tools.test_winter_narrative_capabilities.' +
  'WinterNarrativeCapabilityCheckerTests.' +
  'test_batch_and_final_documents_are_exact_and_phase_sensitive'
)
$catalogRed = & python -B -m unittest $catalogId -v 2>&1
$catalogExit = $LASTEXITCODE
$catalogPath = Join-Path $captureDirectory 'task9-batch-catalog-red.txt'
$catalogRed | Set-Content -LiteralPath $catalogPath -Encoding UTF8
$catalogText = $catalogRed -join [Environment]::NewLine
if ($catalogExit -eq 0 -or
    $catalogText -notmatch 'Ran 1 test' -or
    $catalogText -notmatch 'FAILED \(failures=1\)' -or
    $catalogText -match '(?m)^ERROR:') {
  throw 'Stable Batch catalog RED was not one failure and zero errors.'
}
```

Expected aggregate RED: exactly one assertion failure, zero errors, with
`missing production WINTER_COPY_REGISTRY scaffold`. Expected catalog RED:
exactly one assertion failure, zero errors, because the aggregate ID is absent
from the five-entry checker tuple. Preserve both raw captures.

- [ ] **Step 4: Install the production registry and strict outcome seam**

In the sole `init python` block of
`game/governance_winter_interlude.rpy`, immediately after the unchanged
`WINTER_OUTCOME_CONTRACTS` literal, insert the complete production constants,
registry, and helper below. Do not alter a byte of
`WINTER_OUTCOME_CONTRACTS`.

```renpy
    WINTER_OUTCOME_SCENES = {
        ("trade", "preserve"): "S12",
        ("trade", "feed_now"): "S13",
        ("ration", "preserve"): "S14",
        ("ration", "feed_now"): "S15",
        ("requisition", "preserve"): "S16",
        ("requisition", "feed_now"): "S17",
    }
    WINTER_MITIGATION_KEYS = (
        "market_trade",
        "granary_ration",
        "village_preserve",
        "route_feed_now",
        "merchant_regulated_trade",
        "southern_trade_terms",
        "existing_granary_ration",
        "decree_security_trade",
        "decree_civic_ration",
        "decree_military_requisition",
        "wealth_trade",
        "loyalty_ration",
        "power_requisition",
        None,
    )
    WINTER_SOUTHERN_KEYS = (
        "none",
        "free",
        "ruler",
        "vassal",
        "outwit",
        "fall",
    )
    WINTER_STRUCTURAL_MITIGATION_COPY = {
        "market_trade": (
            "【结构占位·单项缓解】market_trade；不删除负担或承担者。",
        ),
        "granary_ration": (
            "【结构占位·单项缓解】granary_ration；不删除负担或承担者。",
        ),
        "village_preserve": (
            "【结构占位·单项缓解】village_preserve；不删除负担或承担者。",
        ),
        "route_feed_now": (
            "【结构占位·单项缓解】route_feed_now；不删除负担或承担者。",
        ),
        "merchant_regulated_trade": (
            "【结构占位·单项缓解】merchant_regulated_trade；不删除负担或承担者。",
        ),
        "southern_trade_terms": (
            "【结构占位·单项缓解】southern_trade_terms；不删除负担或承担者。",
        ),
        "existing_granary_ration": (
            "【结构占位·单项缓解】existing_granary_ration；不删除负担或承担者。",
        ),
        "decree_security_trade": (
            "【结构占位·单项缓解】decree_security_trade；不删除负担或承担者。",
        ),
        "decree_civic_ration": (
            "【结构占位·单项缓解】decree_civic_ration；不删除负担或承担者。",
        ),
        "decree_military_requisition": (
            "【结构占位·单项缓解】decree_military_requisition；不删除负担或承担者。",
        ),
        "wealth_trade": (
            "【结构占位·单项缓解】wealth_trade；不删除负担或承担者。",
        ),
        "loyalty_ration": (
            "【结构占位·单项缓解】loyalty_ration；不删除负担或承担者。",
        ),
        "power_requisition": (
            "【结构占位·单项缓解】power_requisition；不删除负担或承担者。",
        ),
        None: (
            "【结构占位·单项缓解】none；保留完整负担与承担者。",
        ),
    }
    WINTER_STRUCTURAL_SOUTHERN_COPY = {
        "none": (
            "【结构占位·南境购粮条件】none；只改变购买条件。",
        ),
        "free": (
            "【结构占位·南境购粮条件】free；只改变购买条件。",
        ),
        "ruler": (
            "【结构占位·南境购粮条件】ruler；只改变购买条件。",
        ),
        "vassal": (
            "【结构占位·南境购粮条件】vassal；只改变购买条件。",
        ),
        "outwit": (
            "【结构占位·南境购粮条件】outwit；只改变购买条件。",
        ),
        "fall": (
            "【结构占位·南境购粮条件】fall；只改变购买条件。",
        ),
    }
```

Continue at that exact init-block anchor with the complete registry:

```renpy
    WINTER_COPY_REGISTRY = {
        "S01": {
            "crisis_brief": (
                "【结构占位·危机简报】粮价一周内翻倍；市场限售；账面库存与实际行情不符。",
            ),
        },
        "S02": {
            "delegation": (
                "【结构占位·委托结果】neutral_delegate；不声明任何政策收益，也不替你作出政策决定。",
            ),
        },
        "S03": {
            "market_life": (
                "【结构占位·粮市】排队、争执、空粮袋；各方只掌握部分事实。",
            ),
        },
        "S04": {
            "emergency_council": (
                "【结构占位·紧急议事】商人、农户、守军与账房陈述各自处境。",
            ),
            "status": ("粮价：高｜库存：不足｜民情：不安",),
        },
        "S05": {
            "selected": {
                "first": (
                    "【结构占位·已调查·粮市账本·first】抬价、断路、护运和资金占用共同影响粮价。{#winter_selected_market}",
                ),
                "second": (
                    "【结构占位·已调查·粮市账本·second】抬价、断路、护运和资金占用共同影响粮价。{#winter_selected_market}",
                ),
            },
        },
        "S06": {
            "selected": {
                "first": (
                    "【结构占位·已调查·村庄种粮·first】农户保粮主要为明年春播，并非单纯抗命。{#winter_selected_village}",
                ),
                "second": (
                    "【结构占位·已调查·村庄种粮·second】农户保粮主要为明年春播，并非单纯抗命。{#winter_selected_village}",
                ),
            },
        },
        "S07": {
            "selected": {
                "first": (
                    "【结构占位·已调查·城堡粮仓·first】受潮粮、旧账和层层报喜高估可用库存。{#winter_selected_granary}",
                ),
                "second": (
                    "【结构占位·已调查·城堡粮仓·second】受潮粮、旧账和层层报喜高估可用库存。{#winter_selected_granary}",
                ),
            },
        },
        "S08": {
            "selected": {
                "first": (
                    "【结构占位·已调查·北方商路·first】路线图与货单显示冰雪、损耗和周边采购共同造成到货不足。{#winter_selected_route}",
                ),
                "second": (
                    "【结构占位·已调查·北方商路·second】路线图与货单显示冰雪、损耗和周边采购共同造成到货不足。{#winter_selected_route}",
                ),
            },
        },
        "S09": {
            "omitted": {
                "market": (
                    "【结构占位·低可信报告·粮市账本】抬价与运输成本并存；信息未现场核实。{#winter_omitted_market}",
                ),
                "village": (
                    "【结构占位·低可信报告·村庄种粮】藏粮可能用于春播；信息未现场核实。{#winter_omitted_village}",
                ),
                "granary": (
                    "【结构占位·低可信报告·城堡粮仓】受潮与旧账可能高估库存；信息未现场核实。{#winter_omitted_granary}",
                ),
                "route": (
                    "【结构占位·低可信报告·北方商路】冰雪与运输损耗可能拖慢到货；信息未现场核实。{#winter_omitted_route}",
                ),
            },
        },
        "S10": {
            "shared_cause": (
                "【结构占位·共同原因】多项因素共同造成缺口；不存在单一责任方，也没有单一措施能够解决全部缺口。{#winter_shared_cause}",
            ),
            "escalation": (
                "【结构占位·危机升级】粮车未按时抵达；城内出现抢购。",
            ),
        },
        "S11": {
            "policy_prompt": ("粮价：高｜库存：不足｜民情：不安",),
            "policy_bridge": {
                "trade": ("粮价：高｜库存：不足｜民情：不安",),
                "ration": ("粮价：高｜库存：不足｜民情：不安",),
                "requisition": ("粮价：高｜库存：不足｜民情：不安",),
            },
        },
        "S12": {
            "outcome": (
                "【结构占位·收益】trade_preserved_seed",
                "【结构占位·受益者】farmers_and_trade_route",
                "【结构占位·负担】trade_repayment_and_tight_rations",
                "【结构占位·承担者】treasury_and_townspeople",
                "【结构占位·行动物件】audited_purchase_contracts",
                "【结构占位·后续回响】trade_preserve_recovery",
            ),
            "mitigation": {**WINTER_STRUCTURAL_MITIGATION_COPY},
            "southern": {**WINTER_STRUCTURAL_SOUTHERN_COPY},
        },
        "S13": {
            "outcome": (
                "【结构占位·收益】trade_immediate_relief",
                "【结构占位·受益者】town_relief_recipients",
                "【结构占位·负担】trade_seed_shortfall",
                "【结构占位·承担者】treasury_and_farmers",
                "【结构占位·行动物件】market_grain_distribution",
                "【结构占位·后续回响】trade_feed_recovery",
            ),
            "mitigation": {**WINTER_STRUCTURAL_MITIGATION_COPY},
            "southern": {**WINTER_STRUCTURAL_SOUTHERN_COPY},
        },
        "S14": {
            "outcome": (
                "【结构占位·收益】ration_preserved_seed",
                "【结构占位·受益者】smallholders_and_farmers",
                "【结构占位·负担】ration_hunger_and_reserve_pressure",
                "【结构占位·承担者】garrison_and_townspeople",
                "【结构占位·行动物件】published_ration_ledgers",
                "【结构占位·后续回响】ration_preserve_recovery",
            ),
            "mitigation": {**WINTER_STRUCTURAL_MITIGATION_COPY},
            "southern": {},
        },
        "S15": {
            "outcome": (
                "【结构占位·收益】ration_broad_relief",
                "【结构占位·受益者】town_relief_recipients",
                "【结构占位·负担】ration_reserve_and_seed_loss",
                "【结构占位·承担者】garrison_and_farmers",
                "【结构占位·行动物件】open_granary_distribution",
                "【结构占位·后续回响】ration_feed_recovery",
            ),
            "mitigation": {**WINTER_STRUCTURAL_MITIGATION_COPY},
            "southern": {},
        },
        "S16": {
            "outcome": (
                "【结构占位·收益】requisition_preserved_seed",
                "【结构占位·受益者】smallholders_and_farmers",
                "【结构占位·负担】requisition_compensation_debt",
                "【结构占位·承担者】estates_and_lordship",
                "【结构占位·行动物件】sealed_compensation_vouchers",
                "【结构占位·后续回响】requisition_preserve_recovery",
            ),
            "mitigation": {**WINTER_STRUCTURAL_MITIGATION_COPY},
            "southern": {},
        },
        "S17": {
            "outcome": (
                "【结构占位·收益】requisition_immediate_relief",
                "【结构占位·受益者】broad_relief_recipients",
                "【结构占位·负担】requisition_debt_and_seed_shortfall",
                "【结构占位·承担者】estates_lordship_and_farmers",
                "【结构占位·行动物件】requisition_wagons_and_vouchers",
                "【结构占位·后续回响】requisition_feed_recovery",
            ),
            "mitigation": {**WINTER_STRUCTURAL_MITIGATION_COPY},
            "southern": {},
        },
        "S18": (),
    }
```

Continue in the same init block with the strict helper. It validates the
symbolic route contract before returning any copy and validates mitigation and
southern registries even when the current runtime branch will not display one:

```renpy
    def winter_outcome_copy(policy, seed_priority, outcome):
        route = (policy, seed_priority)
        scene_id = WINTER_OUTCOME_SCENES[route]
        expected_outcome = WINTER_OUTCOME_CONTRACTS[route]
        if type(outcome) is not dict or outcome != expected_outcome:
            raise ValueError("winter outcome symbolic contract mismatch")

        entry = WINTER_COPY_REGISTRY[scene_id]
        if (
                type(entry) is not dict
                or tuple(entry) != ("outcome", "mitigation", "southern")):
            raise ValueError("winter outcome copy entry mismatch")
        outcome_lines = entry["outcome"]
        if type(outcome_lines) is not tuple or len(outcome_lines) != 6:
            raise ValueError("winter outcome copy requires six lines")
        for line in outcome_lines:
            if type(line) is not str or not line:
                raise ValueError("winter outcome copy line is empty")

        mitigation_copy = entry["mitigation"]
        if (
                type(mitigation_copy) is not dict
                or tuple(mitigation_copy) != WINTER_MITIGATION_KEYS):
            raise ValueError("winter mitigation copy keys mismatch")
        for key in WINTER_MITIGATION_KEYS:
            lines = mitigation_copy[key]
            if (
                    type(lines) is not tuple
                    or len(lines) != 1
                    or type(lines[0]) is not str
                    or not lines[0]):
                raise ValueError("winter mitigation copy value mismatch")

        southern_copy = entry["southern"]
        expected_southern_keys = (
            WINTER_SOUTHERN_KEYS if policy == "trade" else ()
        )
        if (
                type(southern_copy) is not dict
                or tuple(southern_copy) != expected_southern_keys):
            raise ValueError("winter southern copy keys mismatch")
        for key in expected_southern_keys:
            lines = southern_copy[key]
            if (
                    type(lines) is not tuple
                    or len(lines) != 1
                    or type(lines[0]) is not str
                    or not lines[0]):
                raise ValueError("winter southern copy value mismatch")
        return scene_id, outcome_lines
```

Replace the complete production slice beginning at
`label winter_interlude_brief:` and ending immediately before
`label winter_interlude_exit:` with the following literal block. This retains
every Task 7 condition, menu, call, jump, state write, route identifier, and
presentation statement. It adds exactly one local assignment and replaces only
player-visible structural literals with exact registry lookups:

```renpy
label winter_interlude_brief:
    scene bg study
    play music "audio/music/winter_wind.ogg" fadeout 1.0 fadein 1.0 if_changed
    "[WINTER_COPY_REGISTRY['S01']['crisis_brief'][0]]"

    menu:
        "亲自主持":
            $ winter_interlude_status = "active"
            call winter_market_and_council from _call_winter_market_and_council

        "交给奥尔德里克":
            call winter_interlude_delegate from _call_winter_interlude_delegate

    return


label winter_interlude_delegate:
    $ apply_winter_delegation()
    "[WINTER_COPY_REGISTRY['S02']['delegation'][0]]"
    return


label winter_market_and_council:
    $ set_weather("snow")
    scene bg market
    play music "audio/music/market_bustle.ogg" fadeout 1.0 fadein 1.0 if_changed
    "[WINTER_COPY_REGISTRY['S03']['market_life'][0]]"
    scene bg council_hall
    "[WINTER_COPY_REGISTRY['S04']['emergency_council'][0]]"
    call winter_investigation_menu from _call_winter_investigation_menu
    return


label winter_investigation_menu:
    "[WINTER_COPY_REGISTRY['S04']['status'][0]]"
    menu:
        "粮市账本":
            call winter_investigate_market("first") from _call_winter_first_market
            call winter_choose_second_investigation("market") from _call_winter_second_after_market

        "村庄种粮":
            call winter_investigate_village("first") from _call_winter_first_village
            call winter_choose_second_investigation("village") from _call_winter_second_after_village

        "城堡粮仓":
            call winter_investigate_granary("first") from _call_winter_first_granary
            call winter_choose_second_investigation("granary") from _call_winter_second_after_granary

        "北方商路":
            call winter_investigate_route("first") from _call_winter_first_route
            call winter_choose_second_investigation("route") from _call_winter_second_after_route

    return


label winter_choose_second_investigation(first):
    if first == "market":
        menu:
            "村庄种粮":
                call winter_investigate_village("second") from _call_winter_second_village_after_market
                call winter_omitted_reports(first, "village") from _call_winter_omitted_market_village

            "城堡粮仓":
                call winter_investigate_granary("second") from _call_winter_second_granary_after_market
                call winter_omitted_reports(first, "granary") from _call_winter_omitted_market_granary

            "北方商路":
                call winter_investigate_route("second") from _call_winter_second_route_after_market
                call winter_omitted_reports(first, "route") from _call_winter_omitted_market_route

    elif first == "village":
        menu:
            "粮市账本":
                call winter_investigate_market("second") from _call_winter_second_market_after_village
                call winter_omitted_reports(first, "market") from _call_winter_omitted_village_market

            "城堡粮仓":
                call winter_investigate_granary("second") from _call_winter_second_granary_after_village
                call winter_omitted_reports(first, "granary") from _call_winter_omitted_village_granary

            "北方商路":
                call winter_investigate_route("second") from _call_winter_second_route_after_village
                call winter_omitted_reports(first, "route") from _call_winter_omitted_village_route

    elif first == "granary":
        menu:
            "粮市账本":
                call winter_investigate_market("second") from _call_winter_second_market_after_granary
                call winter_omitted_reports(first, "market") from _call_winter_omitted_granary_market

            "村庄种粮":
                call winter_investigate_village("second") from _call_winter_second_village_after_granary
                call winter_omitted_reports(first, "village") from _call_winter_omitted_granary_village

            "北方商路":
                call winter_investigate_route("second") from _call_winter_second_route_after_granary
                call winter_omitted_reports(first, "route") from _call_winter_omitted_granary_route

    elif first == "route":
        menu:
            "粮市账本":
                call winter_investigate_market("second") from _call_winter_second_market_after_route
                call winter_omitted_reports(first, "market") from _call_winter_omitted_route_market

            "村庄种粮":
                call winter_investigate_village("second") from _call_winter_second_village_after_route
                call winter_omitted_reports(first, "village") from _call_winter_omitted_route_village

            "城堡粮仓":
                call winter_investigate_granary("second") from _call_winter_second_granary_after_route
                call winter_omitted_reports(first, "granary") from _call_winter_omitted_route_granary

    else:
        call winter_interlude_delegate from _call_winter_invalid_first_delegate

    return


label winter_investigate_market(visit_order):
    if visit_order == "omitted":
        "[WINTER_COPY_REGISTRY['S09']['omitted']['market'][0]]"
    else:
        scene bg market
        "[WINTER_COPY_REGISTRY['S05']['selected'][visit_order][0]]"
    return


label winter_investigate_village(visit_order):
    if visit_order == "omitted":
        "[WINTER_COPY_REGISTRY['S09']['omitted']['village'][0]]"
    else:
        scene bg village
        "[WINTER_COPY_REGISTRY['S06']['selected'][visit_order][0]]"
    return


label winter_investigate_granary(visit_order):
    # TEMPORARY ART MISMATCH: bg study stands in for Task 10 bg_winter_granary.
    if visit_order == "omitted":
        "[WINTER_COPY_REGISTRY['S09']['omitted']['granary'][0]]"
    else:
        scene bg study
        "[WINTER_COPY_REGISTRY['S07']['selected'][visit_order][0]]"
    return


label winter_investigate_route(visit_order):
    if visit_order == "omitted":
        "[WINTER_COPY_REGISTRY['S09']['omitted']['route'][0]]"
    else:
        scene bg study
        "[WINTER_COPY_REGISTRY['S08']['selected'][visit_order][0]]"
    return


label winter_omitted_reports(first, second):
    scene bg council_hall
    $ winter_investigations = normalize_winter_investigations((first, second))
    if not winter_investigations:
        call winter_interlude_delegate from _call_winter_invalid_pair_delegate
        return

    if "market" not in winter_investigations:
        call winter_investigate_market("omitted") from _call_winter_omitted_market
    if "village" not in winter_investigations:
        call winter_investigate_village("omitted") from _call_winter_omitted_village
    if "granary" not in winter_investigations:
        call winter_investigate_granary("omitted") from _call_winter_omitted_granary
    if "route" not in winter_investigations:
        call winter_investigate_route("omitted") from _call_winter_omitted_route

    call winter_crisis_escalates from _call_winter_crisis_escalates
    return


label winter_crisis_escalates:
    scene bg great_hall
    play music "audio/music/tension.ogg" fadeout 1.0 fadein 1.0 if_changed
    "[WINTER_COPY_REGISTRY['S10']['shared_cause'][0]]"
    "[WINTER_COPY_REGISTRY['S10']['escalation'][0]]"
    call winter_choose_policy from _call_winter_choose_policy
    return


label winter_choose_policy:
    "[WINTER_COPY_REGISTRY['S11']['policy_prompt'][0]]"
    menu:
        "高价购粮并担保商路":
            call winter_choose_seed_priority("trade") from _call_winter_seed_trade

        "开仓配给并公开账目":
            call winter_choose_seed_priority("ration") from _call_winter_seed_ration

        "征用大户余粮并开具补偿凭据":
            call winter_choose_seed_priority("requisition") from _call_winter_seed_requisition

    return


label winter_choose_seed_priority(policy):
    "[WINTER_COPY_REGISTRY['S11']['policy_bridge'][policy][0]]"
    menu:
        "保留春播种粮":
            call winter_resolve_outcome(policy, "preserve") from _call_winter_resolve_preserve

        "先让更多人熬过眼前的冬天":
            call winter_resolve_outcome(policy, "feed_now") from _call_winter_resolve_feed_now

    return


label winter_resolve_outcome(policy, seed_priority, immediate_inputs=None, mitigation=None):
    if not finalize_winter_interlude(policy, seed_priority, winter_investigations):
        call winter_interlude_delegate from _call_winter_invalid_result_delegate
        return

    $ immediate_inputs = (gov_merchant_outcome, southern_outcome, built_granary, first_decree, wealth, loyalty, power)
    $ mitigation = select_winter_mitigation(policy, seed_priority, winter_investigations, immediate_inputs)
    call winter_consequence(WINTER_OUTCOME_CONTRACTS[(policy, seed_priority)], mitigation, immediate_inputs) from _call_winter_consequence
    return


label winter_consequence(outcome, mitigation, immediate_inputs):
    scene bg great_hall
    play music "audio/music/castle_calm.ogg" fadeout 1.0 fadein 1.0 if_changed
    $ _winter_outcome_copy = winter_outcome_copy(winter_policy, winter_seed_priority, outcome)
    "[_winter_outcome_copy[1][0]]"
    "[_winter_outcome_copy[1][1]]"
    "[_winter_outcome_copy[1][2]]"
    "[_winter_outcome_copy[1][3]]"
    "[_winter_outcome_copy[1][4]]"
    "[_winter_outcome_copy[1][5]]"
    if winter_policy == "trade" and immediate_inputs[1] not in ("", "delegated"):
        "[WINTER_COPY_REGISTRY[_winter_outcome_copy[0]]['southern'][immediate_inputs[1]][0]]"
    if mitigation is not None:
        "[WINTER_COPY_REGISTRY[_winter_outcome_copy[0]]['mitigation'][mitigation][0]]"
    else:
        "[WINTER_COPY_REGISTRY[_winter_outcome_copy[0]]['mitigation'][None][0]]"
    return
```

`S18` remains exactly `()` and is not referenced by this production slice. Do
not add an empty say, an extra condition, or closure lookup. Its reviewed scene
addendum will add the complete literal and wire it at the end of the active
`winter_consequence` path.

In `Tools/check_winter_narrative_capabilities.py`, replace only
`BATCH_CONTRACT_TEST_IDS` with the following exact six-entry tuple. Preserve
every capability and Final ID and preserve the Task 8 checker close path
byte-for-byte:

```python
BATCH_CONTRACT_TEST_IDS: tuple[str, ...] = (
    "Tools.test_governance_winter_interlude."
    "WinterStoryGraphContractTests."
    "test_complete_story_graph_labels_exist_exactly_once",
    "Tools.test_governance_winter_interlude."
    "WinterStoryGraphContractTests."
    "test_six_outcome_contracts_have_exact_nonempty_symbolic_slots",
    "Tools.test_governance_winter_interlude."
    "WinterStoryGraphContractTests."
    "test_qualitative_lines_assets_and_semantic_markers_are_structural",
    "Tools.test_governance_winter_interlude."
    "WinterStoryGraphContractTests."
    "test_all_task7_renpy_control_expressions_are_exact_and_guarded",
    "Tools.test_governance_winter_interlude."
    "WinterStoryGraphContractTests."
    "test_player_visible_semantics_are_independent_and_fail_closed",
    "Tools.test_governance_winter_interlude."
    "WinterStoryGraphContractTests."
    "test_task8_current_approved_scene_copy_contracts_are_exact",
)
```

This is the only checker edit. Future scene-focused method IDs never enter
this tuple; the stable aggregate owns the cumulative approved registry and
approved-ID prefix.

- [ ] **Step 5: Run focused GREEN, lock static counts, and commit exactly**

Run every changed executable contract once without running a complete module:

```powershell
$focusedIds = [string[]]@(
  'Tools.test_winter_narrative_capabilities.WinterNarrativeCapabilityCheckerTests.test_batch_and_final_documents_are_exact_and_phase_sensitive',
  'Tools.test_governance_winter_interlude.WinterStoryGraphContractTests.test_all_task7_renpy_control_expressions_are_exact_and_guarded',
  'Tools.test_governance_winter_interlude.WinterStoryGraphContractTests.test_qualitative_lines_assets_and_semantic_markers_are_structural',
  'Tools.test_governance_winter_interlude.WinterStoryGraphContractTests.test_player_visible_semantics_are_independent_and_fail_closed',
  'Tools.test_governance_winter_interlude.WinterModuleContractTests.test_state_enum_and_public_helper_signatures_exist',
  'Tools.test_governance_winter_interlude.WinterModuleContractTests.test_new_module_has_no_forbidden_main_state_writes',
  'Tools.test_governance_winter_interlude.WinterStoryGraphContractTests.test_task8_static_speaker_and_presentation_contracts_are_exact',
  'Tools.test_governance_winter_interlude.WinterStoryGraphContractTests.test_task8_current_approved_scene_copy_contracts_are_exact',
  'Tools.test_governance_winter_interlude.WinterStoryGraphContractTests.test_task8_outcome_copy_rejects_route_contract_and_registry_drift'
)
$green = & python -B -m unittest @focusedIds -v 2>&1
$greenExit = $LASTEXITCODE
$greenText = $green -join [Environment]::NewLine
$green | Out-Host
if ($greenExit -ne 0 -or
    $greenText -notmatch 'Ran 9 tests' -or
    $greenText -notmatch '(?m)^OK\r?$' -or
    $greenText -match '(?m)^(FAILED|ERROR:)') {
  throw 'Task 9 focused GREEN was not exactly Ran 9 tests and OK.'
}
```

Expected: `Ran 9 tests`, terminal `OK`. The existing semantic method still
runs all six opposite mutations. The existing Task 7 method still runs every
control mutation plus the two new outcome-helper mutations. This focused run
does not invoke the public gate.

Use fresh loaders and inspect every loader's error list before staging:

```powershell
$countProbe = @'
import importlib
import re
import unittest

from Tools.check_winter_narrative_capabilities import (
    BATCH_CONTRACT_TEST_IDS,
)

expected = {
    "capability": 39,
    "gate": 87,
    "governance": 52,
    "discovery": 381,
}
counts = {}
for key, module_name in (
    ("capability", "Tools.test_winter_narrative_capabilities"),
    ("gate", "Tools.test_winter_interlude_gate"),
    ("governance", "Tools.test_governance_winter_interlude"),
):
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(importlib.import_module(module_name))
    if loader.errors:
        raise AssertionError(f"{key} loader errors: {loader.errors!r}")
    counts[key] = suite.countTestCases()

discovery_loader = unittest.TestLoader()
discovery_suite = discovery_loader.discover(start_dir="Tools")
if discovery_loader.errors:
    raise AssertionError(
        f"discovery loader errors: {discovery_loader.errors!r}"
    )
counts["discovery"] = discovery_suite.countTestCases()
if counts != expected:
    raise AssertionError(f"unexpected Task 9 counts: {counts!r}")

aggregate_id = (
    "Tools.test_governance_winter_interlude."
    "WinterStoryGraphContractTests."
    "test_task8_current_approved_scene_copy_contracts_are_exact"
)
if len(BATCH_CONTRACT_TEST_IDS) != 6:
    raise AssertionError(BATCH_CONTRACT_TEST_IDS)
if BATCH_CONTRACT_TEST_IDS.count(aggregate_id) != 1:
    raise AssertionError(BATCH_CONTRACT_TEST_IDS)
batch_loader = unittest.TestLoader()
batch_suite = batch_loader.loadTestsFromNames(BATCH_CONTRACT_TEST_IDS)
if batch_loader.errors:
    raise AssertionError(f"Batch loader errors: {batch_loader.errors!r}")
if batch_suite.countTestCases() != len(BATCH_CONTRACT_TEST_IDS):
    raise AssertionError("Task 9 Batch IDs do not each resolve once")
if any(
    re.search(r"\.test_s(?:0[1-9]|1[0-8])_", test_id.lower())
    for test_id in BATCH_CONTRACT_TEST_IDS
):
    raise AssertionError("scene-focused test leaked into stable Batch catalog")
print(counts)
'@
& python -B -c $countProbe
if ($LASTEXITCODE -ne 0) {
  throw 'Task 9 static count or Batch catalog validation failed.'
}
```

Expected: capability 39, gate 87, governance 52, discovery 381, all loader
error lists empty, six resolving Batch IDs, and the aggregate ID exactly once.
Discovery starts at `Tools`; root discovery is forbidden because this
repository has no `Tools/__init__.py` and root discovery would report zero
tests with a false `OK`.

Stage and commit exactly the four owned paths:

```powershell
$expectedPaths = [string[]]@(
  'Tools/check_winter_narrative_capabilities.py',
  'Tools/test_governance_winter_interlude.py',
  'Tools/test_winter_narrative_capabilities.py',
  'game/governance_winter_interlude.rpy'
)
git diff --cached --quiet
if ($LASTEXITCODE -ne 0) {
  throw 'Task 9 started staging with a nonempty index.'
}
git add -- $expectedPaths
$actualPaths = [string[]]@(git diff --cached --name-only)
if (@(Compare-Object `
      ($expectedPaths | Sort-Object) `
      ($actualPaths | Sort-Object)).Count -ne 0) {
  throw "Unexpected Task 9 staged paths: $($actualPaths -join ', ')"
}
git diff --cached --check
if ($LASTEXITCODE -ne 0) {
  throw 'Task 9 staged diff check failed.'
}
git commit -m 'test: open the winter prose integration seam'
if ($LASTEXITCODE -ne 0) {
  throw 'Task 9 commit failed.'
}
if ((git log -1 --pretty=%s).Trim() -cne `
    'test: open the winter prose integration seam') {
  throw 'Unexpected Task 9 commit subject.'
}
$committedPaths = [string[]]@(
  git diff-tree --no-commit-id --name-only -r HEAD
)
if (@(Compare-Object `
      ($expectedPaths | Sort-Object) `
      ($committedPaths | Sort-Object)).Count -ne 0) {
  throw "Unexpected Task 9 commit paths: $($committedPaths -join ', ')"
}
if (git status --short) {
  throw 'Task 9 commit left a dirty worktree.'
}
```

- [ ] **Step 6: Execute one authoritative discovery and one real Batch proof**

Do not run the complete capability, gate, or governance module before or after
this fence. Run the following fence once as one unit after the Task 9 commit.
It binds both children to the exact clean HEAD, refuses a same-HEAD rerun before
starting either child, captures strict UTF-8 stdout and stderr separately,
records real exits and PIDs, rejects surviving PIDs, verifies all four committed
hashes, validates the strict capability document, and preserves the external
Batch RunRoot.

```powershell
$pythonCommand = Get-Command python.exe -CommandType Application -ErrorAction Stop |
  Select-Object -First 1
if ($null -eq $pythonCommand -or
    [string]::IsNullOrWhiteSpace([string]$pythonCommand.Source)) {
  throw 'python.exe did not resolve to an application.'
}
$gateHost = Join-Path `
  ([Environment]::SystemDirectory) `
  'WindowsPowerShell\v1.0\powershell.exe'
if (-not [IO.File]::Exists($gateHost)) {
  throw 'Trusted Windows PowerShell 5.1 host is missing.'
}
$winterGate = (
  Resolve-Path -LiteralPath Tools/Run-WinterInterludeGate.ps1 -ErrorAction Stop
).Path
$headBefore = (git rev-parse --verify HEAD).Trim()
if ($LASTEXITCODE -ne 0 -or $headBefore -notmatch '\A[0-9a-f]{40}\z') {
  throw 'Could not bind Task 9 authoritative execution to a full HEAD SHA.'
}
if (git status --short) {
  throw 'Task 9 authoritative execution requires a clean committed worktree.'
}
$boundPaths = [string[]]@(
  'Tools/check_winter_narrative_capabilities.py',
  'Tools/test_governance_winter_interlude.py',
  'Tools/test_winter_narrative_capabilities.py',
  'game/governance_winter_interlude.rpy'
)
$hashesBefore = @{}
foreach ($path in $boundPaths) {
  $hashesBefore[$path] = (
    Get-FileHash -Algorithm SHA256 -LiteralPath $path -ErrorAction Stop
  ).Hash
}
$captureDirectory = '.superpowers/sdd'
New-Item -ItemType Directory -Path $captureDirectory -Force | Out-Null
$captureToken = $headBefore.Substring(0, 12)
$discoveryBase = Join-Path `
  $captureDirectory `
  ("task9-prose-seam-discovery-381-$captureToken")
$batchBase = Join-Path `
  $captureDirectory `
  ("task9-prose-seam-batch-9-$captureToken")
$plannedCaptures = [string[]]@(
  "$discoveryBase.txt",
  "$discoveryBase.stdout.txt",
  "$discoveryBase.stderr.txt",
  "$batchBase.txt",
  "$batchBase.stdout.txt",
  "$batchBase.stderr.txt"
)
foreach ($capture in $plannedCaptures) {
  if (Test-Path -LiteralPath $capture) {
    throw "HEAD-bound authoritative capture already exists; do not rerun: $capture"
  }
}
$strictUtf8 = New-Object Text.UTF8Encoding($false, $true)

function Read-Task9StrictUtf8 {
  [CmdletBinding()]
  param(
    [Parameter(Mandatory = $true)]
    [string]$Path
  )
  $bytes = [IO.File]::ReadAllBytes($Path)
  if ($bytes.Length -ge 3 -and
      $bytes[0] -eq 0xEF -and
      $bytes[1] -eq 0xBB -and
      $bytes[2] -eq 0xBF) {
    throw "Strict UTF-8 evidence contains a BOM: $Path"
  }
  $strictUtf8.GetString($bytes)
}

function Invoke-Task9AuthoritativeCapture {
  [CmdletBinding()]
  param(
    [Parameter(Mandatory = $true)]
    [string]$Executable,
    [Parameter(Mandatory = $true)]
    [string[]]$Arguments,
    [Parameter(Mandatory = $true)]
    [string]$BasePath
  )
  $stdoutPath = "$BasePath.stdout.txt"
  $stderrPath = "$BasePath.stderr.txt"
  $combinedPath = "$BasePath.txt"
  foreach ($path in @($stdoutPath, $stderrPath, $combinedPath)) {
    if (Test-Path -LiteralPath $path) {
      throw "Authoritative capture path is already occupied: $path"
    }
  }
  $process = Start-Process `
    -FilePath $Executable `
    -ArgumentList $Arguments `
    -WorkingDirectory (Get-Location).Path `
    -WindowStyle Hidden `
    -RedirectStandardOutput $stdoutPath `
    -RedirectStandardError $stderrPath `
    -Wait `
    -PassThru
  $process.Refresh()
  $pidValue = [int]$process.Id
  $exitCode = [int]$process.ExitCode
  if ($pidValue -le 0 -or -not $process.HasExited) {
    throw 'Authoritative child did not expose a completed positive PID.'
  }
  if ($null -ne (Get-Process -Id $pidValue -ErrorAction SilentlyContinue)) {
    throw "Authoritative child PID survived Wait: $pidValue"
  }
  $stdoutText = Read-Task9StrictUtf8 -Path $stdoutPath
  $stderrText = Read-Task9StrictUtf8 -Path $stderrPath
  $separator = ''
  if ($stdoutText.Length -gt 0 -and
      $stderrText.Length -gt 0 -and
      -not $stdoutText.EndsWith("`n", [StringComparison]::Ordinal)) {
    $separator = [Environment]::NewLine
  }
  $combinedText = $stdoutText + $separator + $stderrText
  [IO.File]::WriteAllText(
    (Join-Path (Get-Location).Path $combinedPath),
    $combinedText,
    $strictUtf8
  )
  Get-Content -LiteralPath $combinedPath -ErrorAction Stop | Out-Host
  [pscustomobject][ordered]@{
    ExitCode = $exitCode
    ProcessId = $pidValue
    Text = $combinedText
    CombinedPath = $combinedPath
    CombinedSha256 = (
      Get-FileHash -Algorithm SHA256 -LiteralPath $combinedPath `
        -ErrorAction Stop
    ).Hash
    StdoutSha256 = (
      Get-FileHash -Algorithm SHA256 -LiteralPath $stdoutPath `
        -ErrorAction Stop
    ).Hash
    StderrSha256 = (
      Get-FileHash -Algorithm SHA256 -LiteralPath $stderrPath `
        -ErrorAction Stop
    ).Hash
  }
}

$environmentNames = [string[]]@(
  'APPDATA',
  'GIT_COMMIT',
  'PYTHONDONTWRITEBYTECODE',
  'PYTHONIOENCODING',
  'PYTHONUTF8',
  'WINTER_GATE_JOB_NAME',
  'WINTER_GATE_STRUCTURED_OUTPUT_HANDLE'
)
$previousEnvironment = @{}
foreach ($name in $environmentNames) {
  $previousEnvironment[$name] = [Environment]::GetEnvironmentVariable(
    $name,
    [EnvironmentVariableTarget]::Process
  )
}
$batchRunRoot = Join-Path `
  ([IO.Path]::GetTempPath()) `
  ("winter-task9-prose-seam-batch-" + [Guid]::NewGuid().ToString('N'))
$batchAppData = Join-Path `
  ([IO.Path]::GetTempPath()) `
  ("winter-task9-prose-seam-appdata-" + [Guid]::NewGuid().ToString('N'))
if (Test-Path -LiteralPath $batchRunRoot) {
  throw 'Fresh Task 9 authoritative Batch RunRoot already exists.'
}
New-Item -ItemType Directory -Path $batchAppData -ErrorAction Stop | Out-Null
try {
  Remove-Item Env:\WINTER_GATE_JOB_NAME -ErrorAction SilentlyContinue
  Remove-Item Env:\WINTER_GATE_STRUCTURED_OUTPUT_HANDLE `
    -ErrorAction SilentlyContinue
  $env:PYTHONDONTWRITEBYTECODE = '1'
  $env:PYTHONIOENCODING = 'utf-8'
  $env:PYTHONUTF8 = '1'
  $env:GIT_COMMIT = $headBefore

  $discoveryRun = Invoke-Task9AuthoritativeCapture `
    -Executable $pythonCommand.Source `
    -Arguments ([string[]]@(
      '-B', '-m', 'unittest', 'discover', '-s', 'Tools', '-v'
    )) `
    -BasePath $discoveryBase
  $discoveryRan = [regex]::Matches(
    $discoveryRun.Text,
    '(?m)^Ran ([0-9]+) tests? in [0-9]+(?:\.[0-9]+)?s\r?$'
  )
  $discoveryOk = [regex]::Matches(
    $discoveryRun.Text,
    '(?m)^OK\r?$'
  )
  $discoveryLines = [string[]]@(
    $discoveryRun.Text -split '\r?\n' |
      Where-Object { $_.Length -gt 0 }
  )
  if ($discoveryRun.ExitCode -ne 0 -or
      $discoveryRan.Count -ne 1 -or
      $discoveryRan[0].Groups[1].Value -cne '381' -or
      $discoveryOk.Count -ne 1 -or
      $discoveryLines.Count -eq 0 -or
      $discoveryLines[-1] -cne 'OK') {
    throw "Authoritative discovery was not exactly Ran 381 tests and OK: $($discoveryRun.CombinedPath)"
  }
  if (git status --short) {
    throw 'Authoritative Task 9 discovery dirtied the worktree.'
  }

  $env:APPDATA = $batchAppData
  $batchRun = Invoke-Task9AuthoritativeCapture `
    -Executable $gateHost `
    -Arguments ([string[]]@(
      '-NoLogo',
      '-NoProfile',
      '-NonInteractive',
      '-ExecutionPolicy',
      'Bypass',
      '-File',
      $winterGate,
      '-Gate',
      'Narrative',
      '-NarrativePhase',
      'Batch',
      '-ProjectRoot',
      (Get-Location).Path,
      '-RunRoot',
      $batchRunRoot
    )) `
    -BasePath $batchBase
  if ($batchRun.ExitCode -ne 0) {
    throw "Committed Task 9 Narrative Batch failed: $($batchRun.CombinedPath)"
  }

  $summaryPath = Join-Path $batchRunRoot 'evidence\gate-summary.json'
  if (-not [IO.File]::Exists($summaryPath)) {
    throw 'Committed Task 9 Batch did not publish gate-summary.json.'
  }
  $summaryText = Read-Task9StrictUtf8 -Path $summaryPath
  $summary = $summaryText | ConvertFrom-Json
  $steps = @($summary.steps)
  if ($summary.gate -cne 'Narrative' -or
      $summary.narrative_phase -cne 'Batch' -or
      $summary.status -cne 'passed' -or
      $summary.failure_kind -ne $null -or
      $summary.head_token -cne $captureToken -or
      $summary.host.edition -cne 'Desktop' -or
      -not ([string]$summary.host.version).StartsWith(
        '5.1.',
        [StringComparison]::Ordinal
      ) -or
      $steps.Count -ne 9 -or
      @($steps | Where-Object {
        $_.status -cne 'passed' -or
        -not $_.process_started -or
        -not $_.tree_drained -or
        $_.had_live_descendants_after_root_exit
      }).Count -ne 0) {
    throw 'Committed Task 9 Batch summary is not the exact clean nine-step proof.'
  }

  $capabilityPath = Join-Path `
    $batchRunRoot `
    ("evidence\narrative-01-narrative-capability-$captureToken.output.json")
  if (-not [IO.File]::Exists($capabilityPath)) {
    throw 'Task 9 Batch did not preserve capability JSON evidence.'
  }
  $capabilityText = Read-Task9StrictUtf8 -Path $capabilityPath
  $capability = $capabilityText | ConvertFrom-Json
  $documentKeys = [string[]]@(
    $capability.PSObject.Properties.Name | Sort-Object
  )
  $expectedDocumentKeys = [string[]]@(
    'capabilities',
    'phase',
    'ready',
    'schema_version',
    'tool'
  )
  if (@(Compare-Object $expectedDocumentKeys $documentKeys).Count -ne 0) {
    throw 'Task 9 capability document keys are not exact.'
  }
  if ($capability.schema_version.GetType().FullName -cne 'System.Int32' -or
      $capability.schema_version -ne 1 -or
      $capability.tool -cne 'winter_narrative_capabilities' -or
      $capability.phase -cne 'batch' -or
      $capability.ready -isnot [bool] -or
      -not $capability.ready) {
    throw 'Task 9 capability document envelope is not exact.'
  }
  $capabilityKeys = [string[]]@(
    $capability.capabilities.PSObject.Properties.Name | Sort-Object
  )
  $expectedCapabilityKeys = [string[]]@(
    'batch_contracts',
    'canon_json',
    'final_contracts',
    'nested_quote_json',
    'overlap_json',
    'portrait_json',
    'show_before_json'
  )
  if (@(Compare-Object `
      $expectedCapabilityKeys `
      $capabilityKeys).Count -ne 0) {
    throw 'Task 9 capability names are not exact.'
  }
  foreach ($name in @(
      'batch_contracts',
      'canon_json',
      'nested_quote_json',
      'overlap_json',
      'portrait_json',
      'show_before_json')) {
    $value = $capability.capabilities.$name
    if ($value -isnot [bool] -or -not $value) {
      throw "Task 9 Batch capability is not true: $name"
    }
  }
  if ($capability.capabilities.final_contracts -isnot [bool] -or
      $capability.capabilities.final_contracts) {
    throw 'Task 9 Final contracts must remain false during Batch.'
  }
  if (git status --short) {
    throw 'Authoritative Task 9 Batch dirtied the worktree.'
  }

  $headAfter = (git rev-parse --verify HEAD).Trim()
  if ($LASTEXITCODE -ne 0 -or $headAfter -cne $headBefore) {
    throw 'HEAD changed during Task 9 authoritative execution.'
  }
  foreach ($path in $boundPaths) {
    $after = (
      Get-FileHash -Algorithm SHA256 -LiteralPath $path -ErrorAction Stop
    ).Hash
    if ($after -cne $hashesBefore[$path]) {
      throw "Task 9 committed input changed during evidence: $path"
    }
  }
  $summarySha256 = (
    Get-FileHash -Algorithm SHA256 -LiteralPath $summaryPath -ErrorAction Stop
  ).Hash
  $capabilitySha256 = (
    Get-FileHash -Algorithm SHA256 -LiteralPath $capabilityPath `
      -ErrorAction Stop
  ).Hash
  Write-Output "AUTHORITATIVE_HEAD=$headAfter"
  Write-Output "DISCOVERY_PID=$($discoveryRun.ProcessId)"
  Write-Output "DISCOVERY_LOG=$($discoveryRun.CombinedPath)"
  Write-Output "DISCOVERY_LOG_SHA256=$($discoveryRun.CombinedSha256)"
  Write-Output "DISCOVERY_STDOUT_SHA256=$($discoveryRun.StdoutSha256)"
  Write-Output "DISCOVERY_STDERR_SHA256=$($discoveryRun.StderrSha256)"
  Write-Output "BATCH_PID=$($batchRun.ProcessId)"
  Write-Output "BATCH_LOG=$($batchRun.CombinedPath)"
  Write-Output "BATCH_LOG_SHA256=$($batchRun.CombinedSha256)"
  Write-Output "BATCH_STDOUT_SHA256=$($batchRun.StdoutSha256)"
  Write-Output "BATCH_STDERR_SHA256=$($batchRun.StderrSha256)"
  Write-Output "BATCH_RUN_ROOT=$batchRunRoot"
  Write-Output "BATCH_SUMMARY_SHA256=$summarySha256"
  Write-Output "BATCH_CAPABILITY_SHA256=$capabilitySha256"
}
finally {
  foreach ($name in $environmentNames) {
    $previous = $previousEnvironment[$name]
    if ($null -eq $previous) {
      Remove-Item -LiteralPath "Env:\$name" -ErrorAction SilentlyContinue
    }
    else {
      [Environment]::SetEnvironmentVariable(
        $name,
        [string]$previous,
        [EnvironmentVariableTarget]::Process
      )
    }
  }
}
```

Expected: discovery has one completed positive PID, exit 0, exactly one
`Ran 381 tests` line and one terminal `OK`. Only then does the single Batch
start. Batch has one completed positive PID, exit 0, Desktop PowerShell 5.1,
current HEAD token, nine passed and drained steps, no live descendants, strict
Batch capability JSON with `batch_contracts=true` and
`final_contracts=false`, unchanged four-file hashes, clean status, and printed
capture, summary, and capability SHA-256 values. Existing HEAD-bound capture
paths make a same-commit rerun stop before either child starts.

### Downstream literal-method and count contract

Task 9 ends at governance 52 and discovery 381. The ledger slice `L0` adds
exactly one governance method named
`test_task8_approved_source_ledger_starts_empty_and_is_exact`, producing
governance 53 and discovery 382. It does not change capability 39, gate 87, or
the stable six-entry Batch catalog.

The arithmetic is governance `52 + 1 = 53` and discovery `381 + 1 = 382`;
capability remains 39 and the public gate remains 87.

Each reviewed scene addendum then adds exactly one independent focused literal
method to `WinterStoryGraphContractTests`, in this order:

1. `test_s01_crisis_brief_approved_literal_copy_is_exact`
2. `test_s02_neutral_delegation_approved_literal_copy_is_exact`
3. `test_s03_market_life_approved_literal_copy_is_exact`
4. `test_s04_emergency_council_approved_literal_copy_is_exact`
5. `test_s05_selected_market_investigation_approved_literal_copy_is_exact`
6. `test_s06_selected_village_investigation_approved_literal_copy_is_exact`
7. `test_s07_selected_granary_investigation_approved_literal_copy_is_exact`
8. `test_s08_selected_route_investigation_approved_literal_copy_is_exact`
9. `test_s09_omitted_report_bundle_approved_literal_copy_is_exact`
10. `test_s10_crisis_escalation_approved_literal_copy_is_exact`
11. `test_s11_two_layer_decision_approved_literal_copy_is_exact`
12. `test_s12_trade_preserve_consequence_approved_literal_copy_is_exact`
13. `test_s13_trade_feed_now_consequence_approved_literal_copy_is_exact`
14. `test_s14_ration_preserve_consequence_approved_literal_copy_is_exact`
15. `test_s15_ration_feed_now_consequence_approved_literal_copy_is_exact`
16. `test_s16_requisition_preserve_consequence_approved_literal_copy_is_exact`
17. `test_s17_requisition_feed_now_consequence_approved_literal_copy_is_exact`
18. `test_s18_closure_to_chapter2_approved_literal_copy_is_exact`

For scene number `k` from 1 through 18, the post-scene count is governance
`53 + k` and discovery `382 + k`; after S18 they are governance 71 and
discovery 400. These values freeze only the ledger and scene series. Later
final-only methods add their separately declared counts; discovery 400 must
not be presented as the final delivery count.

Every scene-focused method contains that scene's complete approved literal
expected value directly in its own body; it must not read its expected value
from `_TASK8_COPY_REGISTRY_CONTRACT`. The same addendum also performs all of
the following literal changes:

- replace only that production registry entry with the exact approved copy;
- replace the matching independent aggregate contract entry;
- append exactly that scene ID to `_TASK8_APPROVED_SCENE_IDS`, preserving the
  exact `_TASK8_SCENE_ORDER` prefix;
- replace that label's control template with its exact speaker and
  interpolation sequence;
- replace that label's independent presentation signature with its complete
  approved presentation sequence;
- provide one focused RED against the unchanged production scene and one
  focused GREEN after the exact literal patch;
- keep the checker catalog unchanged and rely on the stable aggregate ID for
  cumulative Batch enforcement;
- run exactly one real Batch proof on the approved scene commit.

`S18` is the only scene allowed to change its registry entry from `()` and add
its first lookup. It wires the complete approved closure at the end of the
active `winter_consequence` path without adding an empty say or a new branch.
For the six coordinated visible-semantic scenes, the same atomic scene commit
updates production plus the independent expectations in
`Tools/test_governance_winter_interlude.py` and `game/test_game.rpy`, preserves
the six opposite source mutations, and reruns the existing real `_history`
route matrix including delegation. Other scene commits do not add runtime
literal mirrors to `game/test_game.rpy`.

The scene candidate process remains the global one-Opus-plus-two-isolated-
controls workflow. All three raw candidates are shown unchanged under one
hidden A/B/C mapping; the same approved legacy spans are then inserted into
all three at the same anchors and all three complete composites are shown
under that same mapping. The user selects one exact composite or rejects all
three, and provenance is revealed only after that decision. A rejected
candidate directory is deleted after its validated absolute path is shown to
remain under the task-owned temporary root. Neither rejected prose nor a
recoverable excerpt is retained. Only the selected raw candidate and selected
approved composite enter ignored evidence; corpus enrollment remains a
separate explicit question and commit.

### Task 9 hard stop and asset audit

After the single Task 9 authoritative fence succeeds, report its exact HEAD,
counts, capture hashes, Batch summary hash, capability hash, and clean status,
then stop. Do not begin L0, invoke a scene writer, create candidates, integrate
prose, update the writing-style corpus, run Final, build, package, publish, or
start umbrella Task 9 without the next explicit authorization.

Task 9 changes test, checker, and Ren'Py source bytes only. It requires no new
art, music, sound effect, portrait, animation, UI, font, old-game, shipping
asset, or package byte. It reuses `bg study`, `bg market`, `bg council_hall`,
`bg village`, `bg great_hall`, `winter_wind`, `market_bustle`, `tension`, and
`castle_calm`. The existing `bg study` granary mismatch remains the declared
Task 10 art debt; Task 9 neither hides nor expands it. Package-size delta from
assets and font is exactly zero.

## Task 10: Bind a feasible user-approved legacy-reuse contract before prose

**Files:**

- Read: `game/governance.rpy`
- Modify through the reviewed L0 addendum only: `docs/superpowers/plans/2026-08-09-winter-interlude-narrative-delivery.md`
- Create after approval: `docs/development/winter-interlude-content-ledger.md`
- Modify after approval: `Tools/test_governance_winter_interlude.py`

### L0 mathematical hard stop

Pin the source to the Git LF blob of `game/governance.rpy` whose SHA-256 is
`4f79d36082fc35e2d9a39c9bf9d5a74458457af9109c5558dfc17f94fe0c4211`.
The broadest relevant eleven-label pool contains 3,527 Han characters; the
canon-, timeline-, and scene-coherent core contains 2,903. The candidate labels
are `gov_famine_crisis`, `gov_famine_buy`, `gov_famine_ration`,
`gov_famine_castle`, `gov_famine_end`, `gov_building`, `gov_build_granary`,
`gov_merchant`, `gov_merchant_monopoly`, `gov_merchant_regulated`, and
`gov_merchant_reject`.

The active-path budget is 11,140 through 13,360 Han characters. Interpreting
"roughly one third" as one third plus or minus five percentage points gives a
lower bound of `17/60`, or 28.333 recurring percent:

- shortest-path minimum: `ceil(11140 * 17 / 60) = 3157`;
- longest-path minimum: `ceil(13360 * 17 / 60) = 3786`;
- coherent core on the shortest path: `2903 / 11140 = 26.059%`;
- entire broad pool on the longest path: `3527 / 13360 = 26.400%`.

The coherent core cannot satisfy even the shortest path, and the entire broad
pool cannot satisfy the longest path. The broad pool also contains obsolete
full-granary assumptions, unconditional heroic famine resolution, raid or
robbery material, superseded merchant outcomes, and route-incompatible text.
Repetition, incoherent insertion, adapted wording counted as verbatim, or one
target occurrence counted more than once is forbidden.

Stop before creating any S01 candidate until the user explicitly approves
exactly one of these contracts:

1. the design's one-third goal is a conceptual source-category contribution;
   the ledger reports actual verbatim reuse without a numeric minimum, and all
   adapted wording is new prose; or
2. the user supplies and approves a lower numeric verbatim range plus an exact
   source scope whose route-by-route table proves feasibility.

Silence, a generic continuation instruction, approval of the design, approval
of tooling, or approval of an individual scene does not select either
contract. No agent or test may select one on the user's behalf.

- [ ] **Step 1: Append and review the complete literal L0 addendum**

The heading is exactly
`### Task 10 Addendum: User-approved legacy-reuse contract`. The addendum
contains actual values and complete bodies:

- the exact user-approved interpretation and approval-evidence SHA-256;
- the pinned source blob hash;
- every accepted span's literal source text, label, two unique surrounding
  anchors, strict UTF-8 SHA-256, Han count, and risk classification;
- every considered but rejected span and its objective rejection reason;
- exact S01 through S18 target registry paths and fixed composite anchors;
- every active path's projected total, verbatim, new, and percentage counts;
- the complete initial content-ledger body;
- the complete independent method
  `WinterStoryGraphContractTests.test_task8_approved_source_ledger_starts_empty_and_is_exact`;
- exact RED, GREEN, static-catalog, staging, commit, Batch, rollback, and asset
  commands.

The frozen method name says `starts_empty` because its RED begins with no
approved ledger. Its GREEN asserts the exact user-approved literal ledger; it
expects an empty approved-span set only if that is the explicit user decision.
Expected values live directly in the test and are not read from the ledger.

Commit only this plan with subject
`docs: bind winter legacy reuse contract`. Create one immutable ignored review
input bound to the plan commit, canonical plan hash, exact user decision, and
complete ledger/test bodies. Obtain fresh independent Spec and Standards
decisions on that same input; both must report
`Critical 0 / Important 0 - READY` before either implementation file changes.

- [ ] **Step 2: Apply the ledger test first and take the focused RED**

```powershell
$redText = @(
  python -m unittest `
    Tools.test_governance_winter_interlude.WinterStoryGraphContractTests.test_task8_approved_source_ledger_starts_empty_and_is_exact `
    -v 2>&1
)
$redExit = $LASTEXITCODE
$redText | Out-Host
$joinedRed = $redText -join "`n"
if ($redExit -eq 0) {
  throw 'Legacy-ledger RED unexpectedly passed.'
}
if ($joinedRed -match 'ImportError|SyntaxError|ModuleNotFoundError') {
  throw 'Legacy-ledger RED was an import or syntax failure.'
}
if ($joinedRed -notmatch 'Ran 1 test') {
  throw 'Legacy-ledger RED did not run exactly one focused method.'
}
```

Expected: one failing method because the approved ledger or its literal content
is absent, with no import, syntax, or loader error.

- [ ] **Step 3: Create the literal ledger and run only the focused GREEN**

```powershell
python -m unittest `
  Tools.test_governance_winter_interlude.WinterStoryGraphContractTests.test_task8_approved_source_ledger_starts_empty_and_is_exact `
  -v
if ($LASTEXITCODE -ne 0) {
  throw 'Legacy-ledger focused GREEN failed.'
}
```

- [ ] **Step 4: Prove the frozen L0 catalog without executing discovery**

```python
import unittest

loaders = {
    "governance": unittest.TestLoader(),
    "capability": unittest.TestLoader(),
    "gate": unittest.TestLoader(),
    "discovery": unittest.TestLoader(),
}
counts = {
    "governance": loaders["governance"].loadTestsFromName(
        "Tools.test_governance_winter_interlude"
    ).countTestCases(),
    "capability": loaders["capability"].loadTestsFromName(
        "Tools.test_winter_narrative_capabilities"
    ).countTestCases(),
    "gate": loaders["gate"].loadTestsFromName(
        "Tools.test_winter_interlude_gate"
    ).countTestCases(),
    "discovery": loaders["discovery"].discover(
        start_dir="Tools"
    ).countTestCases(),
}
errors = {name: loader.errors for name, loader in loaders.items()}
if errors != {
    "governance": [],
    "capability": [],
    "gate": [],
    "discovery": [],
}:
    raise SystemExit(f"unexpected unittest loader errors: {errors!r}")
if counts != {
    "governance": 53,
    "capability": 39,
    "gate": 87,
    "discovery": 382,
}:
    raise SystemExit(f"unexpected L0 catalog: {counts!r}")
print(counts)
```

Run that complete fence through `python -c` or save it only in ignored
evidence. It imports real suites but executes no tests. Root discovery is
forbidden; the only discovery root is literal `Tools`, and every
`loader.errors` list must be empty.

- [ ] **Step 5: Stage exactly, commit, and run one committed Batch proof**

Stage only `Tools/test_governance_winter_interlude.py` and
`docs/development/winter-interlude-content-ledger.md`. Require exact index
membership and `git diff --cached --check`, then commit with subject
`docs: ledger approved winter source passages`. The committed tree has
governance 53, capability 39, public gate 87, and `Tools` discovery 382.
Run one self-contained committed Narrative Batch proof on that SHA. Do not run
full discovery or a full module separately.

The complete committed-Batch fence already appears literally in Task 8 Step 5
and Task 9 Step 7, but PowerShell functions do not persist between fences.
Therefore the L0 literal addendum and every scene literal addendum must each
contain its own complete `Read-StrictUtf8Capture` and
`Invoke-AuthoritativeCapture` bodies rather than a prose reference. Its
subject allowlist contains only `docs: ledger approved winter source passages`
for L0 or the one literal `feat: write winter scene Sxx` subject for that
scene. It uses a fresh external RunRoot, scrubs the two winter environment
variables, binds `GIT_COMMIT` to full HEAD, captures stdout and stderr
separately, requires a completed positive PID and exit 0, validates the strict
Batch summary as current HEAD plus nine passed/drained steps and no live
descendant, hashes every owned input before and after, rejects a pre-existing
same-HEAD capture, and leaves the tracked tree clean. A successful Batch is
never repeated on the same SHA.

Expected L0 result: one committed Batch invocation and no discovery
invocation. The slice does not transplant target prose. Art, music, sound
effects, portraits, animation, UI, font, shipping assets, and package size
remain unchanged.

---

## Task 11: Generate, approve, review, and integrate S01 through S18 atomically

**Files:**

- Modify once per literal addendum: `docs/superpowers/plans/2026-08-09-winter-interlude-narrative-delivery.md`
- Modify once per approved scene: `Tools/test_governance_winter_interlude.py`
- Modify once per approved scene: `game/governance_winter_interlude.rpy`
- Modify only for S02, S09, and S10: `game/test_game.rpy`
- Read without modifying: `docs/development/winter-interlude-content-ledger.md`
- Write selected evidence only beneath ignored `.superpowers/sdd/`

### Exact per-scene fact-card schema

Every fact card contains exactly these substantive inputs:

1. the literal scene ID and exact `WINTER_COPY_REGISTRY` path;
2. continuous entry and exit context;
3. characters physically present and the existing static speaker identifiers;
4. each character's known and unknown facts;
5. required causal, benefit, beneficiary, burden, bearer, action, and follow-up
   facts;
6. forbidden claims and forbidden control-flow implications;
7. exact plain-text output-block order;
8. the scene's Han-character budget;
9. already-user-approved legacy IDs and their fixed composite anchors; and
10. an instruction to emit prose blocks only, with no Ren'Py, paths,
    provenance, model discussion, code fence, or explanation.

The strict UTF-8 fact-card bytes and SHA-256 are identical for Candidate O,
C1, and C2. Legacy source text is not included in any candidate prompt.

### Exact candidate, blind-composite, and approval protocol

For each literal scene in the fixed order:

1. verify the preceding implementation commit is clean and has one green
   committed Batch proof;
2. create three distinct validated task-owned temporary directories: one for
   a fresh Opus run, one for isolated Codex C1, and one for isolated Codex C2;
3. create the Opus prompt with `apply_patch`, verify nonempty strict UTF-8, and
   invoke only
   `C:\Users\22325\.codex\skills\invoke-opus-4-6\scripts\invoke-opus.ps1`;
4. require metadata `success=true`, `model=claude-opus-4-6`,
   `expected_model=claude-opus-4-6`, and exactly that one value in both
   `observed_models` and `result_model_usage_models` before reading the
   nonempty strict-UTF-8 terminal result;
5. if Opus fails, preserve the available failure artifacts, report the exact
   paths, stop, and do not retry without a new user instruction;
6. produce C1 and C2 in fresh isolated contexts that cannot read another
   candidate, approved samples, historical archives, rejected prose, local
   paths, Ren'Py source, or legacy source spans;
7. randomize the three raw candidates once into a hidden A/B/C mapping and
   show all three raw outputs unchanged in that order;
8. mechanically insert the same approved legacy spans into all three raw
   candidates at the same predeclared anchors without changing any raw or
   reused byte;
9. show all three complete composites in the same A/B/C order;
10. accept only the user's selection of one exact complete composite or
    rejection of all three, then reveal provenance;
11. if all three are rejected, resolve and display each absolute candidate
    root, prove it remains beneath the task-owned temporary root, delete all
    three directories, and stop without an automatic replacement round;
12. if one is selected, copy only its exact raw result and exact approved
    composite into ignored evidence, then safely delete both rejected roots;
13. append the complete literal scene addendum, commit only that plan change,
    and obtain fresh independent Spec and Standards READY decisions on the
    exact addendum commit;
14. apply the complete literal focused method first, run only that method for
    the intended RED, apply the reviewed production patch, and run only that
    method for GREEN;
15. run the static catalog below, stage only the literal allowlist, commit the
    literal implementation subject, and execute exactly one committed Batch
    proof using the complete self-contained fence required by Task 10;
16. after the Batch proof, show the clean selected text and ask the exact
    corpus-enrollment question required by `AGENTS.md`; corpus enrollment is a
    separate user-authorized commit and never blocks the next scene.

A materially edited composite is not the selected exact composite. Reject it
and start a new round only after a new explicit user instruction. Codex may
apply reversible escaping, page-tag placement, and objective integration
corrections only when those transformations and their inverse are fully
declared in the reviewed addendum.

### Complete literal scene-addendum contract

Every scene addendum contains actual bytes and complete bodies for:

- fact card, fact-card SHA-256, all three raw SHA-256 values, and the hidden
  A/B/C mapping;
- verified Opus metadata and terminal-result evidence;
- all three complete composites and their SHA-256 values;
- selected raw SHA-256, selected composite SHA-256, user-approval evidence,
  and the post-decision provenance reveal;
- reuse IDs, source hashes, fixed anchors, target occurrence counts, and
  rejected-directory deletion attestations;
- that scene's independent literal focused method in
  `WinterStoryGraphContractTests`;
- the matching independent `_TASK8_COPY_REGISTRY_CONTRACT` replacement;
- the exact production `WINTER_COPY_REGISTRY` replacement;
- the exact `_TASK8_APPROVED_SCENE_IDS` prefix extension;
- the exact control-template and presentation-signature replacement;
- for S02, S09, or S10, the complete independent Python semantic expectation,
  complete `game/test_game.rpy` expectation, opposite-semantic mutations, and
  real `_history` route-matrix binding;
- reversible raw-to-Ren'Py quote, backslash, interpolation, and page-tag
  mapping;
- literal focused RED/GREEN commands, exact stage allowlist, implementation
  subject, complete single-use Batch fence, and asset/package audit.

The addendum may not use an unnamed next scene, a scene variable, a
metavariable token, an omitted helper body, or a reference such as "same as an
earlier addendum". Every literal focused method embeds its own approved
expected value; it does not derive expected copy from production or from
`_TASK8_COPY_REGISTRY_CONTRACT`.

### Static prefix and count audit after every scene GREEN

Run this complete Python fence without executing the loaded suites. It proves
that the integrated methods are an exact prefix, no final-only method landed
early, all four loader error lists are empty, and the cumulative counts follow
the Task 9 contract.

```python
import importlib
import unittest

SCENE_METHODS = (
    "test_s01_crisis_brief_approved_literal_copy_is_exact",
    "test_s02_neutral_delegation_approved_literal_copy_is_exact",
    "test_s03_market_life_approved_literal_copy_is_exact",
    "test_s04_emergency_council_approved_literal_copy_is_exact",
    "test_s05_selected_market_investigation_approved_literal_copy_is_exact",
    "test_s06_selected_village_investigation_approved_literal_copy_is_exact",
    "test_s07_selected_granary_investigation_approved_literal_copy_is_exact",
    "test_s08_selected_route_investigation_approved_literal_copy_is_exact",
    "test_s09_omitted_report_bundle_approved_literal_copy_is_exact",
    "test_s10_crisis_escalation_approved_literal_copy_is_exact",
    "test_s11_two_layer_decision_approved_literal_copy_is_exact",
    "test_s12_trade_preserve_consequence_approved_literal_copy_is_exact",
    "test_s13_trade_feed_now_consequence_approved_literal_copy_is_exact",
    "test_s14_ration_preserve_consequence_approved_literal_copy_is_exact",
    "test_s15_ration_feed_now_consequence_approved_literal_copy_is_exact",
    "test_s16_requisition_preserve_consequence_approved_literal_copy_is_exact",
    "test_s17_requisition_feed_now_consequence_approved_literal_copy_is_exact",
    "test_s18_closure_to_chapter2_approved_literal_copy_is_exact",
)
FINAL_METHODS = (
    "test_active_paths_are_11000_to_14000_chinese_characters",
    "test_active_paths_match_user_approved_legacy_reuse_contract",
    "test_six_visible_semantics_are_literal_and_fail_closed",
    "test_player_visible_structural_placeholders_are_absent",
    "test_every_scene_has_approved_final_copy",
)

module = importlib.import_module("Tools.test_governance_winter_interlude")
story_class = module.WinterStoryGraphContractTests
ledger_method = "test_task8_approved_source_ledger_starts_empty_and_is_exact"
if not hasattr(story_class, ledger_method):
    raise SystemExit("approved L0 ledger method is absent")
present = tuple(name for name in SCENE_METHODS if hasattr(story_class, name))
if present != SCENE_METHODS[: len(present)]:
    raise SystemExit(f"scene methods are not an exact prefix: {present!r}")
final_class = getattr(module, "WinterNarrativeFinalContractTests", None)
if final_class is not None and any(
    hasattr(final_class, name) for name in FINAL_METHODS
):
    raise SystemExit("final-only method landed before all scene commits")

loaders = {
    "governance": unittest.TestLoader(),
    "capability": unittest.TestLoader(),
    "gate": unittest.TestLoader(),
    "discovery": unittest.TestLoader(),
}
counts = {
    "governance": loaders["governance"].loadTestsFromName(
        "Tools.test_governance_winter_interlude"
    ).countTestCases(),
    "capability": loaders["capability"].loadTestsFromName(
        "Tools.test_winter_narrative_capabilities"
    ).countTestCases(),
    "gate": loaders["gate"].loadTestsFromName(
        "Tools.test_winter_interlude_gate"
    ).countTestCases(),
    "discovery": loaders["discovery"].discover(
        start_dir="Tools"
    ).countTestCases(),
}
errors = {name: loader.errors for name, loader in loaders.items()}
if errors != {
    "governance": [],
    "capability": [],
    "gate": [],
    "discovery": [],
}:
    raise SystemExit(f"unexpected unittest loader errors: {errors!r}")
scene_count = len(present)
expected = {
    "governance": 53 + scene_count,
    "capability": 39,
    "gate": 87,
    "discovery": 382 + scene_count,
}
if counts != expected:
    raise SystemExit(
        f"unexpected scene catalog at prefix {scene_count}: {counts!r}"
    )
print({"scene_count": scene_count, **counts, "loader_errors": 0})
```

For every scene, the literal addendum supplies one exact focused command of
the form `python -m unittest` plus the fully qualified method ID in the table
below and `-v`. RED must be one intended assertion failure without import or
syntax failure; GREEN must report exactly one passing test. No full discovery,
full governance module, full capability module, or public-gate module runs
before the scene commit. The one post-commit Batch is the cumulative runtime
and source proof.

### Literal scene fact cards S01 through S09

#### S01-crisis-brief

- Registry path: `WINTER_COPY_REGISTRY["S01"]["crisis_brief"]`.
- Entry and exit: after the winter autosave and before the active/delegate
  menu in `winter_interlude_brief`.
- Present characters: player and Aldric.
- Required facts: price doubled in one week, market sales are limited, and
  ledger inventory conflicts with observed supply.
- Forbidden claims: a full causal diagnosis, a culprit, a policy preference,
  an investigation result, or a solved crisis.
- Plain-text output order: one `crisis_brief` tuple suitable for the existing
  static lookup; no menu copy or control statement.
- Budget: 350 through 500 Han; the complete pre-choice visible block must stay
  at or below 700 Han.

#### S02-neutral-delegation

- Registry path: `WINTER_COPY_REGISTRY["S02"]["delegation"]`.
- Entry and exit: immediately after `apply_winter_delegation()` and before the
  common cleanup route.
- Present characters: player and Aldric.
- Required facts: ordinary minimum purchase and rationing prevent collapse,
  but no active policy has been chosen.
- Forbidden claims: preserved seed, complete reserve, regulated trade,
  special debt, achievement, stat effect, perfect relief, or any active-route
  benefit.
- This scene owns the coordinated neutral-delegation literal in production,
  Python, and real Ren'Py `_history`.
- Plain-text output order: one `delegation` tuple.
- Budget: 250 through 400 Han.

#### S03-market-life

- Registry path: `WINTER_COPY_REGISTRY["S03"]["market_life"]`.
- Entry and exit: active choice, snow and market presentation, then the
  existing council-hall transition.
- Present speakers may use only existing static identifiers physically
  justified in the market: player, Aldric, crowd, merchant, farmer, and guard.
- Required facts: queues, restricted sales, disputes, empty sacks, and
  concrete household stakes appear before policy discussion; each observer
  has partial information.
- Forbidden claims: a single villain, a final causal conclusion, a completed
  investigation, or a policy result.
- Plain-text output order: one `market_life` tuple with its complete approved
  static speaker sequence.
- Budget: 900 through 1,100 Han.

#### S04-emergency-council

- Registry paths:
  `WINTER_COPY_REGISTRY["S04"]["emergency_council"]` and
  `WINTER_COPY_REGISTRY["S04"]["status"]`.
- Entry and exit: after the existing council scene statement and before
  `winter_investigation_menu`.
- Present speakers: player, Aldric, merchant, farmer, captain, and accountant.
- Required facts: each party states a materially true constraint while
  protecting an interest; no participant knows the complete chain; all four
  investigations remain visible.
- Forbidden claims: a liar reveal, final blame, hidden option, invented stock,
  or final policy result.
- Plain-text output order: complete `emergency_council` tuple followed by one
  qualitative `status` tuple; existing menu keys remain unchanged.
- Budget: 1,600 through 1,900 Han on an active path.

#### S05-selected-market-investigation

- Registry paths:
  `WINTER_COPY_REGISTRY["S05"]["selected"]["first"]` and
  `WINTER_COPY_REGISTRY["S05"]["selected"]["second"]`.
- Required facts: some price exploitation exists; blocked roads, escort risk,
  and tied-up working capital also create real cost. Visit order changes only
  immediate framing.
- Required mitigation meaning: on a trade route, market evidence supports
  audited contracts and price limits, reducing later merchant leverage without
  deleting purchase cost.
- Preserve page tag `{#winter_selected_market}` exactly once in each approved
  first/second path after reversible integration.
- Forbidden claims: all merchants colluded, market evidence creates grain, or
  the investigation resolves the crisis.
- Plain-text output order: `first`, then `second`, each a complete tuple.
- Budget: 1,250 through 1,450 Han for either visit order.

#### S06-selected-village-investigation

- Registry paths:
  `WINTER_COPY_REGISTRY["S06"]["selected"]["first"]` and
  `WINTER_COPY_REGISTRY["S06"]["selected"]["second"]`.
- Required facts: retained grain is chiefly spring seed, not simple defiance;
  present hunger and next spring are both real.
- Required mitigation meaning: household registration can reduce unequal
  distribution resentment on a preserve route without removing present
  hunger.
- Preserve `{#winter_selected_village}` exactly once in both visit orders.
- Forbidden claims: universal innocence, unlimited seed, no current suffering,
  or a cost-free preserve choice.
- Plain-text output order: `first`, then `second`.
- Budget: 1,250 through 1,450 Han for either visit order.

#### S07-selected-granary-investigation

- Registry paths:
  `WINTER_COPY_REGISTRY["S07"]["selected"]["first"]` and
  `WINTER_COPY_REGISTRY["S07"]["selected"]["second"]`.
- Required facts: damp grain, stale books, and layered optimistic reporting
  overstate usable stock.
- Required mitigation meaning: a ration route may inventory and move damp
  grain first, reducing reserve loss without creating grain.
- Preserve `{#winter_selected_granary}` exactly once in both visit orders.
- Presentation: retain the declared temporary `bg study` mismatch; Task 8
  adds no granary art.
- Forbidden claims: a full five-thousand-unit reserve, deliberate sabotage as
  the sole cause, or a solved shortage.
- Plain-text output order: `first`, then `second`.
- Budget: 1,250 through 1,450 Han for either visit order.

#### S08-selected-route-investigation

- Registry paths:
  `WINTER_COPY_REGISTRY["S08"]["selected"]["first"]` and
  `WINTER_COPY_REGISTRY["S08"]["selected"]["second"]`.
- Required facts: the investigation stays indoors and uses maps, invoices,
  and escort reports; snow, transport loss, and neighboring purchases jointly
  reduce arrivals.
- Required mitigation meaning: on a feed-now route, a backup route can recover
  only a small late shipment and reduce, not eliminate, extra seed diversion.
- Preserve `{#winter_selected_route}` exactly once in both visit orders.
- Forbidden claims: an outdoor expedition, one blocked road as the entire
  cause, or enough recovered grain to cancel the trade-off.
- Plain-text output order: `first`, then `second`.
- Budget: 1,250 through 1,450 Han for either visit order.

#### S09-omitted-report-bundle

- Registry paths: the four literal tuples under
  `WINTER_COPY_REGISTRY["S09"]["omitted"]` in exact order `market`,
  `village`, `granary`, `route`.
- Required market meaning: possible price pressure plus transport cost, not
  verified on site.
- Required village meaning: possible spring-seed retention, not verified on
  site.
- Required granary meaning: possible damp stock and stale-book overstatement,
  not verified on site.
- Required route meaning: possible snow and transport loss, not verified on
  site.
- Every omitted report is explicitly lower-confidence than its selected scene,
  claims no selected mitigation, and retains its matching
  `{#winter_omitted_*}` page tag exactly once.
- This scene owns all four coordinated omitted-report literals in production,
  Python, and real Ren'Py `_history`.
- Plain-text output order: four complete tuples in canonical registry order;
  an active path displays exactly the two unselected reports.
- Budget: 220 through 280 Han for each of the four tuples.

### Literal scene fact cards S10 through S18

#### S10-crisis-escalation

- Registry paths: `WINTER_COPY_REGISTRY["S10"]["shared_cause"]` and
  `WINTER_COPY_REGISTRY["S10"]["escalation"]`.
- Entry and exit: the selected and omitted evidence returns to the great hall,
  then the existing policy choice follows.
- Required facts: scheduled wagons fail to arrive; panic buying begins;
  harvest shortfall, snow, route loss, neighboring purchases, spring-seed
  retention, stale castle books, and limited opportunism jointly create the
  gap.
- Mandatory meaning: no one person created the whole crisis, no one store can
  fill the whole gap, and no one measure can solve all of it. Investigations
  change questions and mitigation only; they do not cancel escalation.
- Preserve `{#winter_shared_cause}` exactly once. This scene owns the shared-
  cause coordinated literal in production, Python, and real `_history`.
- Plain-text output order: complete `shared_cause` tuple, then complete
  `escalation` tuple.
- Budget: 1,200 through 1,400 Han.

#### S11-two-layer-decision

- Registry paths: `WINTER_COPY_REGISTRY["S11"]["policy_prompt"]` and the
  exact `trade`, `ration`, and `requisition` tuples beneath `policy_bridge`.
- Required facts: all three policy choices remain visible, then both seed
  priorities remain visible. Trade buys grain and guarantees a route; ration
  opens stock and publishes accounts; requisition takes large-holder surplus
  and issues compensation vouchers. Preserve protects spring seed; feed-now
  feeds more people immediately.
- Every route retains one benefit, beneficiary, burden, bearer, concrete
  action, and follow-up. No option dominates and no soft input hides an option.
- Plain-text output order: `policy_prompt`, then `policy_bridge.trade`,
  `policy_bridge.ration`, and `policy_bridge.requisition`; menu keys and targets
  remain unchanged.
- Budget: 1,900 through 2,200 Han on an active path.

#### Shared S12 through S17 consequence payload contract

Each consequence candidate returns its six-line `outcome` tuple plus literal
copy for every Task 9 mitigation key in this exact order:
`market_trade`, `granary_ration`, `village_preserve`, `route_feed_now`,
`merchant_regulated_trade`, `southern_trade_terms`,
`existing_granary_ration`, `decree_security_trade`,
`decree_civic_ration`, `decree_military_requisition`, `wealth_trade`,
`loyalty_ration`, `power_requisition`, and `None`. Every mitigation reduces
only its designated single cost; it never deletes the route's burden or
bearer. Registry completeness is required even for a key that the current
route precedence cannot display.

S12 and S13 additionally return literal southern-condition tuples in exact
order `none`, `free`, `ruler`, `vassal`, `outwit`, and `fall`. Southern history
may change purchase terms only; it never supplies free grain or solves the
crisis. S14 through S17 retain exact empty `southern` dictionaries. The
1,350-through-1,700 budget applies to the visible six-line outcome plus the
one selected mitigation and, for trade, the one selected southern tuple; the
larger registry payload is not counted as simultaneously visible.

#### S12-trade-preserve-consequence

- Registry path: `WINTER_COPY_REGISTRY["S12"]`.
- Exact symbolic facts, in outcome order:
  `trade_preserved_seed`, `farmers_and_trade_route`,
  `trade_repayment_and_tight_rations`, `treasury_and_townspeople`,
  `audited_purchase_contracts`, `trade_preserve_recovery`.
- Visible meaning: the route and spring seed benefit; treasury repayment,
  townspeople's tight rationing, and merchant leverage remain; postwar
  recovery is steadier, not guaranteed.
- Plain-text output order: six outcome entries, all fourteen mitigation
  entries, then all six southern entries.
- Budget: 1,350 through 1,700 Han on every permitted visible variant.

#### S13-trade-feed-now-consequence

- Registry path: `WINTER_COPY_REGISTRY["S13"]`.
- Exact symbolic facts:
  `trade_immediate_relief`, `town_relief_recipients`,
  `trade_seed_shortfall`, `treasury_and_farmers`,
  `market_grain_distribution`, `trade_feed_recovery`.
- Visible meaning: immediate market relief is broad; treasury cost and spring-
  seed shortfall remain; recovery is slower.
- Plain-text output order: six outcome entries, all fourteen mitigation
  entries, then all six southern entries.
- Budget: 1,350 through 1,700 Han on every permitted visible variant.

#### S14-ration-preserve-consequence

- Registry path: `WINTER_COPY_REGISTRY["S14"]`.
- Exact symbolic facts:
  `ration_preserved_seed`, `smallholders_and_farmers`,
  `ration_hunger_and_reserve_pressure`, `garrison_and_townspeople`,
  `published_ration_ledgers`, `ration_preserve_recovery`.
- Visible meaning: public distribution and spring seed benefit; garrison
  reserve pressure and present tight rationing remain.
- Plain-text output order: six outcome entries and all fourteen mitigation
  entries; `southern` remains `{}`.
- Budget: 1,350 through 1,700 Han on every permitted visible variant.

#### S15-ration-feed-now-consequence

- Registry path: `WINTER_COPY_REGISTRY["S15"]`.
- Exact symbolic facts:
  `ration_broad_relief`, `town_relief_recipients`,
  `ration_reserve_and_seed_loss`, `garrison_and_farmers`,
  `open_granary_distribution`, `ration_feed_recovery`.
- Visible meaning: the largest immediate group receives food; castle reserve
  loss and spring-seed loss both remain.
- Plain-text output order: six outcome entries and all fourteen mitigation
  entries; `southern` remains `{}`.
- Budget: 1,350 through 1,700 Han on every permitted visible variant.

#### S16-requisition-preserve-consequence

- Registry path: `WINTER_COPY_REGISTRY["S16"]`.
- Exact symbolic facts:
  `requisition_preserved_seed`, `smallholders_and_farmers`,
  `requisition_compensation_debt`, `estates_and_lordship`,
  `sealed_compensation_vouchers`, `requisition_preserve_recovery`.
- Visible meaning: smallholders and spring seed are protected; estates give up
  grain and the lordship assumes enforceable compensation debt.
- Plain-text output order: six outcome entries and all fourteen mitigation
  entries; `southern` remains `{}`.
- Budget: 1,350 through 1,700 Han on every permitted visible variant.

#### S17-requisition-feed-now-consequence

- Registry path: `WINTER_COPY_REGISTRY["S17"]`.
- Exact symbolic facts:
  `requisition_immediate_relief`, `broad_relief_recipients`,
  `requisition_debt_and_seed_shortfall`,
  `estates_lordship_and_farmers`, `requisition_wagons_and_vouchers`,
  `requisition_feed_recovery`.
- Visible meaning: relief is broad and castle stock is comparatively
  protected; compensation debt and spring-seed shortfall both remain.
- Plain-text output order: six outcome entries and all fourteen mitigation
  entries; `southern` remains `{}`.
- Budget: 1,350 through 1,700 Han on every permitted visible variant.

#### S18-closure-to-chapter2

- Registry path: replace exact `WINTER_COPY_REGISTRY["S18"] == ()` with the
  approved closure tuple and add its first lookup.
- Presentation anchor: the end of the active `winter_consequence` path, after
  outcome, southern, and mitigation presentation but before that label's
  existing `return`.
- Required facts: roads reopen only partially; the crisis is temporarily
  controlled, not solved; a Harrenhall summons requires departure; the chosen
  winter policy becomes political leverage.
- Forbidden changes: a new label, branch, state write, ending input, complete
  recovery, downstream Task 9 echo, or Chapter 2 rewrite.
- The addendum supplies the exact new control template and complete
  presentation signature. It may not create an empty say statement.
- Plain-text output order: one complete closure tuple plus one exact static
  lookup at the approved anchor.
- Budget: 900 through 1,100 Han.

### Literal method, commit, allowlist, and count table

| Scene | Focused method in `WinterStoryGraphContractTests` | Plan-only addendum subject | Implementation subject | Implementation allowlist | Governance / discovery |
| --- | --- | --- | --- | --- | --- |
| S01 | `test_s01_crisis_brief_approved_literal_copy_is_exact` | `docs: bind winter scene S01 crisis brief approved copy` | `feat: write winter scene S01` | Python test + winter module | 54 / 383 |
| S02 | `test_s02_neutral_delegation_approved_literal_copy_is_exact` | `docs: bind winter scene S02 neutral delegation approved copy` | `feat: write winter scene S02` | Python test + winter module + `game/test_game.rpy` | 55 / 384 |
| S03 | `test_s03_market_life_approved_literal_copy_is_exact` | `docs: bind winter scene S03 market life approved copy` | `feat: write winter scene S03` | Python test + winter module | 56 / 385 |
| S04 | `test_s04_emergency_council_approved_literal_copy_is_exact` | `docs: bind winter scene S04 emergency council approved copy` | `feat: write winter scene S04` | Python test + winter module | 57 / 386 |
| S05 | `test_s05_selected_market_investigation_approved_literal_copy_is_exact` | `docs: bind winter scene S05 selected market investigation approved copy` | `feat: write winter scene S05` | Python test + winter module | 58 / 387 |
| S06 | `test_s06_selected_village_investigation_approved_literal_copy_is_exact` | `docs: bind winter scene S06 selected village investigation approved copy` | `feat: write winter scene S06` | Python test + winter module | 59 / 388 |
| S07 | `test_s07_selected_granary_investigation_approved_literal_copy_is_exact` | `docs: bind winter scene S07 selected granary investigation approved copy` | `feat: write winter scene S07` | Python test + winter module | 60 / 389 |
| S08 | `test_s08_selected_route_investigation_approved_literal_copy_is_exact` | `docs: bind winter scene S08 selected route investigation approved copy` | `feat: write winter scene S08` | Python test + winter module | 61 / 390 |
| S09 | `test_s09_omitted_report_bundle_approved_literal_copy_is_exact` | `docs: bind winter scene S09 omitted report bundle approved copy` | `feat: write winter scene S09` | Python test + winter module + `game/test_game.rpy` | 62 / 391 |
| S10 | `test_s10_crisis_escalation_approved_literal_copy_is_exact` | `docs: bind winter scene S10 crisis escalation approved copy` | `feat: write winter scene S10` | Python test + winter module + `game/test_game.rpy` | 63 / 392 |
| S11 | `test_s11_two_layer_decision_approved_literal_copy_is_exact` | `docs: bind winter scene S11 two layer decision approved copy` | `feat: write winter scene S11` | Python test + winter module | 64 / 393 |
| S12 | `test_s12_trade_preserve_consequence_approved_literal_copy_is_exact` | `docs: bind winter scene S12 trade preserve consequence approved copy` | `feat: write winter scene S12` | Python test + winter module | 65 / 394 |
| S13 | `test_s13_trade_feed_now_consequence_approved_literal_copy_is_exact` | `docs: bind winter scene S13 trade feed now consequence approved copy` | `feat: write winter scene S13` | Python test + winter module | 66 / 395 |
| S14 | `test_s14_ration_preserve_consequence_approved_literal_copy_is_exact` | `docs: bind winter scene S14 ration preserve consequence approved copy` | `feat: write winter scene S14` | Python test + winter module | 67 / 396 |
| S15 | `test_s15_ration_feed_now_consequence_approved_literal_copy_is_exact` | `docs: bind winter scene S15 ration feed now consequence approved copy` | `feat: write winter scene S15` | Python test + winter module | 68 / 397 |
| S16 | `test_s16_requisition_preserve_consequence_approved_literal_copy_is_exact` | `docs: bind winter scene S16 requisition preserve consequence approved copy` | `feat: write winter scene S16` | Python test + winter module | 69 / 398 |
| S17 | `test_s17_requisition_feed_now_consequence_approved_literal_copy_is_exact` | `docs: bind winter scene S17 requisition feed now consequence approved copy` | `feat: write winter scene S17` | Python test + winter module | 70 / 399 |
| S18 | `test_s18_closure_to_chapter2_approved_literal_copy_is_exact` | `docs: bind winter scene S18 closure to chapter2 approved copy` | `feat: write winter scene S18` | Python test + winter module | 71 / 400 |

In this table, `Python test` means literal
`Tools/test_governance_winter_interlude.py` and `winter module` means literal
`game/governance_winter_interlude.rpy`. No scene commit contains the plan: its
addendum was already committed and reviewed immediately beforehand. No scene
commit changes the ledger; all per-scene source/target bindings were fixed in
L0, while final actual occurrence and route totals are folded into the tracked
ledger before the final commit in Task 12.

### Exact active-path budget and scene-series hard stop

Every one of the 12 ordered investigation paths times six outcome routes
contains:

- S01: 350 through 500;
- S03: 900 through 1,100;
- S04: 1,600 through 1,900;
- two selected investigations: 2,500 through 2,900;
- two omitted reports: 440 through 560;
- S10: 1,200 through 1,400;
- S11: 1,900 through 2,200;
- one S12 through S17 consequence: 1,350 through 1,700;
- S18: 900 through 1,100.

The exact sum is 11,140 through 13,360 Han. The final counter enumerates all
72 ordered active paths and additionally proves that replacing the selected
mitigation and southern tuple with every permitted alternative keeps the path
inside 11,000 through 14,000. The delegated S01 plus S02 route is checked as a
separate short neutral route and is not padded to the active-path target.

After S18, require governance 71, capability 39, gate 87, discovery 400, an
exact `_TASK8_APPROVED_SCENE_IDS == _TASK8_SCENE_ORDER`, 18 independent literal
focused methods, 18 reviewed implementation commits, and 18 distinct green
committed Batch proofs. Stop before adding final-only methods until all of
those facts are present.

The scene arithmetic is governance `53 + 18 = 71` and discovery
`382 + 18 = 400`; capability remains 39 and the public gate remains 87.

Each scene changes text and tests only. Art, music, sound effects, portraits,
animation, UI, font, and package bytes remain unchanged. Existing assets are
reused, and S07's temporary `bg study` art debt remains outside Task 8.

---

## Task 12: Bind and implement the approved final narrative contracts

**Files:**

- Modify through the final-contract addendum: `docs/superpowers/plans/2026-08-09-winter-interlude-narrative-delivery.md`
- Modify: `Tools/test_governance_winter_interlude.py`
- Modify: `docs/development/winter-interlude-content-ledger.md`
- Modify only if `prepare_release.py` changes it: `game/msyh.ttf`

- [ ] **Step 1: Append and review the complete literal final-contract addendum**

Only after S18 is Batch-green, append
`### Task 12 Addendum: Approved final narrative contracts`. It contains actual
values and complete bodies:

- all 18 approved literal registry objects and composite SHA-256 values;
- all 72 exact active-path totals and all optional mitigation/southern minimum
  and maximum substitutions;
- the complete user-approved L0 reuse calculation from actual target
  occurrences;
- the six coordinated semantic literals;
- complete bodies for the five final-only methods named below;
- the complete final ledger patch recording every source/target span, target
  hash and count, scene raw/composite hash, approval hash, plan-addendum
  commit, implementation commit, and per-scene Batch-summary hash;
- exact final RED, focused GREEN, static-catalog, font, staging, commit,
  authoritative discovery/Final, rollback, and asset/package commands;
- the exact immutable final-review input schema used by Task 13.

Commit only this plan with subject
`docs: bind winter final narrative contracts`. Obtain fresh independent Spec
and Standards decisions on one immutable ignored input bound to the exact
plan commit and canonical plan hash. Both must report
`Critical 0 / Important 0 - READY` before the final tests, tracked ledger, or
font changes.

- [ ] **Step 2: Take the intended final-contract RED through the real checker**

```powershell
$finalProbe = Join-Path `
  ([IO.Path]::GetTempPath()) `
  ("winter-final-capability-" + [Guid]::NewGuid().ToString('N') + '.json')
if (Test-Path -LiteralPath $finalProbe) {
  throw 'Fresh final capability output already exists.'
}
python Tools/check_winter_narrative_capabilities.py `
  --phase final `
  --format json `
  --output $finalProbe
$probeExit = $LASTEXITCODE
if ($probeExit -eq 0) {
  throw 'Final capability RED unexpectedly passed.'
}
if (-not [IO.File]::Exists($finalProbe)) {
  throw 'Final capability RED did not publish its fail-closed document.'
}
$strictUtf8 = New-Object Text.UTF8Encoding($false, $true)
$probeBytes = [IO.File]::ReadAllBytes($finalProbe)
$probe = ($strictUtf8.GetString($probeBytes)) | ConvertFrom-Json
$capabilities = $probe.capabilities
if ($probe.schema_version -ne 1 -or
    $probe.tool -cne 'winter_narrative_capabilities' -or
    $probe.phase -cne 'final' -or
    $probe.ready -ne $false -or
    $capabilities.canon_json -ne $true -or
    $capabilities.portrait_json -ne $true -or
    $capabilities.overlap_json -ne $true -or
    $capabilities.show_before_json -ne $true -or
    $capabilities.nested_quote_json -ne $true -or
    $capabilities.batch_contracts -ne $true -or
    $capabilities.final_contracts -ne $false) {
  throw 'Final capability RED was not caused only by absent final contracts.'
}
```

This is the behavior-specific RED. Do not add a fake failing marker to
production or a hypothetical prose expectation.

- [ ] **Step 3: Add exactly five literal final-only methods and finalize the tracked ledger**

Add class `WinterNarrativeFinalContractTests` with exactly these methods:

1. `test_active_paths_are_11000_to_14000_chinese_characters`;
2. `test_active_paths_match_user_approved_legacy_reuse_contract`;
3. `test_six_visible_semantics_are_literal_and_fail_closed`;
4. `test_player_visible_structural_placeholders_are_absent`;
5. `test_every_scene_has_approved_final_copy`.

The first method enumerates all 12 ordered investigations times six outcomes,
checks S01's 700-Han pre-choice ceiling, checks the delegated route separately,
and substitutes every permitted mitigation and southern tuple. The second uses
the explicit L0 interpretation and independently verifies source hash, target
occurrence, numerator, denominator, and every path; it never reinstates the
rejected one-third numeric rule. The third embeds all six approved literals
independently, preserves all opposite-semantic mutations, and binds real
`_history`. The fourth scans player-visible output rather than internal keys
and rejects structural markers, visible scene IDs, symbolic outcome IDs,
mitigation IDs, debug text, and unresolved interpolation. The fifth embeds all
18 approved registry objects and composite hashes independently of production,
the aggregate contract, and the ledger.

Apply the complete tracked ledger patch from the reviewed addendum in the same
working tree. All tracked source, target, approval, scene, reuse, path-count,
and per-scene Batch facts must be present before the final commit. The ledger
does not contain the future Final summary or final-review decisions; those are
ignored evidence bound directly to final HEAD.

Run only the five focused methods before committing:

```powershell
python -m unittest `
  Tools.test_governance_winter_interlude.WinterNarrativeFinalContractTests `
  -v
if ($LASTEXITCODE -ne 0) {
  throw 'Five focused final narrative contracts failed.'
}
```

Expected: `Ran 5 tests`, `OK`.

The five final-only methods produce governance `71 + 5 = 76` and discovery
`400 + 5 = 405`; capability remains 39 and the public gate remains 87.

- [ ] **Step 4: Prove the exact final catalog without executing discovery**

```python
import unittest

loaders = {
    "governance": unittest.TestLoader(),
    "capability": unittest.TestLoader(),
    "gate": unittest.TestLoader(),
    "discovery": unittest.TestLoader(),
}
counts = {
    "governance": loaders["governance"].loadTestsFromName(
        "Tools.test_governance_winter_interlude"
    ).countTestCases(),
    "capability": loaders["capability"].loadTestsFromName(
        "Tools.test_winter_narrative_capabilities"
    ).countTestCases(),
    "gate": loaders["gate"].loadTestsFromName(
        "Tools.test_winter_interlude_gate"
    ).countTestCases(),
    "discovery": loaders["discovery"].discover(
        start_dir="Tools"
    ).countTestCases(),
}
errors = {name: loader.errors for name, loader in loaders.items()}
if errors != {
    "governance": [],
    "capability": [],
    "gate": [],
    "discovery": [],
}:
    raise SystemExit(f"unexpected unittest loader errors: {errors!r}")
expected = {
    "governance": 76,
    "capability": 39,
    "gate": 87,
    "discovery": 405,
}
if counts != expected:
    raise SystemExit(f"unexpected final catalog: {counts!r}")
invariant_remainder = (
    counts["discovery"]
    - counts["governance"]
    - counts["capability"]
    - counts["gate"]
)
if invariant_remainder != 203:
    raise SystemExit(
        f"unexpected invariant remainder: {invariant_remainder}"
    )
print({**counts, "invariant_remainder": invariant_remainder})
```

The formula is `203 + 76 + 39 + 87 = 405`. All four loader error lists are
exactly empty. Do not execute discovery yet.

- [ ] **Step 5: Refresh the subset font exactly twice**

```powershell
$fontPath = 'game/msyh.ttf'
$fontBeforeHash = (
  Get-FileHash -Algorithm SHA256 -LiteralPath $fontPath -ErrorAction Stop
).Hash
$fontBeforeBytes = (Get-Item -LiteralPath $fontPath -ErrorAction Stop).Length
python prepare_release.py
$fontFirst = $LASTEXITCODE
if ($fontFirst -notin @(0, 1)) {
  throw 'First final font pass failed.'
}
python prepare_release.py
if ($LASTEXITCODE -ne 0) {
  throw 'Second final font pass failed.'
}
$fontAfterHash = (
  Get-FileHash -Algorithm SHA256 -LiteralPath $fontPath -ErrorAction Stop
).Hash
$fontAfterBytes = (Get-Item -LiteralPath $fontPath -ErrorAction Stop).Length
Write-Output "FONT_BEFORE_SHA256=$fontBeforeHash"
Write-Output "FONT_AFTER_SHA256=$fontAfterHash"
Write-Output "FONT_BYTE_DELTA=$($fontAfterBytes - $fontBeforeBytes)"
```

The first exit may be 0 or 1; the second is exactly 0. Any tracked change
outside the final Python test, tracked ledger, and optional font stops this
task.

- [ ] **Step 6: Stage the exact final allowlist and create the final tracked commit**

The required staged paths are
`Tools/test_governance_winter_interlude.py` and
`docs/development/winter-interlude-content-ledger.md`. Add `game/msyh.ttf` only
when its bytes changed. Require exact index membership,
`git diff --cached --check`, and no other tracked status. Commit with subject
`feat: finalize winter interlude prose`.

This is the last tracked Task 8 commit. No ledger, evidence, review, cleanup,
or documentation commit follows it. Art, music, sound effects, portraits,
animation, and UI deltas are zero. Package impact is exactly the recorded font
delta, which may be zero.

- [ ] **Step 7: Execute one authoritative 405-test discovery and one Final proof**

Run this fence once as a unit on the clean final commit. It refuses a same-HEAD
rerun, executes discovery only from literal `Tools`, and starts Final only
after discovery is exactly green.

```powershell
$pythonCommand = Get-Command python.exe -CommandType Application -ErrorAction Stop |
  Select-Object -First 1
if ($null -eq $pythonCommand -or
    [string]::IsNullOrWhiteSpace([string]$pythonCommand.Source)) {
  throw 'python.exe did not resolve to an application.'
}
$gateHost = Join-Path `
  ([Environment]::SystemDirectory) `
  'WindowsPowerShell\v1.0\powershell.exe'
if (-not [IO.File]::Exists($gateHost)) {
  throw 'Trusted Windows PowerShell 5.1 host is missing.'
}
$winterGate = (
  Resolve-Path -LiteralPath Tools/Run-WinterInterludeGate.ps1 -ErrorAction Stop
).Path
$headBefore = (git rev-parse --verify HEAD).Trim()
if ($LASTEXITCODE -ne 0 -or $headBefore -notmatch '\A[0-9a-f]{40}\z') {
  throw 'Could not bind final evidence to a full HEAD SHA.'
}
if ((git log -1 --pretty=%s).Trim() -cne
    'feat: finalize winter interlude prose') {
  throw 'Final evidence is not running on the final tracked commit.'
}
if (git status --short) {
  throw 'Final evidence requires a clean worktree.'
}
$boundPaths = [string[]]@(
  'docs/superpowers/plans/2026-08-09-winter-interlude-narrative-delivery.md',
  'docs/development/winter-interlude-content-ledger.md',
  'Tools/Run-WinterInterludeGate.ps1',
  'Tools/check_winter_narrative_capabilities.py',
  'Tools/scan_canon.py',
  'Tools/scan_nested_quotes.py',
  'Tools/scan_show_before_prevention.py',
  'Tools/test_governance_winter_interlude.py',
  'Tools/test_winter_interlude_gate.py',
  'Tools/test_winter_narrative_capabilities.py',
  'Tools/winter_narrative_inputs.py',
  'Tools/winter_narrative_inputs.txt',
  'Tools/winter_narrative_json.py',
  'scan_missing_portraits.py',
  'scan_narration_overlap.py',
  'game/governance_winter_interlude.rpy',
  'game/test_game.rpy',
  'game/msyh.ttf'
)
$hashesBefore = @{}
foreach ($path in $boundPaths) {
  $hashesBefore[$path] = (
    Get-FileHash -Algorithm SHA256 -LiteralPath $path -ErrorAction Stop
  ).Hash
}
$captureDirectory = '.superpowers/sdd'
New-Item -ItemType Directory -Path $captureDirectory -Force | Out-Null
$headToken = $headBefore.Substring(0, 12)
$discoveryBase = Join-Path `
  $captureDirectory `
  ("task8-final-discovery-405-$headToken")
$finalBase = Join-Path `
  $captureDirectory `
  ("task8-final-final-9-$headToken")
$plannedCaptures = [string[]]@(
  "$discoveryBase.txt",
  "$discoveryBase.stdout.txt",
  "$discoveryBase.stderr.txt",
  "$finalBase.txt",
  "$finalBase.stdout.txt",
  "$finalBase.stderr.txt"
)
foreach ($path in $plannedCaptures) {
  if (Test-Path -LiteralPath $path) {
    throw "HEAD-bound final capture already exists; do not rerun: $path"
  }
}
$strictUtf8 = New-Object Text.UTF8Encoding($false, $true)

function Read-Task8StrictUtf8 {
  param(
    [Parameter(Mandatory = $true)]
    [string]$Path
  )
  $bytes = [IO.File]::ReadAllBytes($Path)
  $offset = 0
  if ($bytes.Length -ge 3 -and
      $bytes[0] -eq 0xEF -and
      $bytes[1] -eq 0xBB -and
      $bytes[2] -eq 0xBF) {
    $offset = 3
  }
  $strictUtf8.GetString($bytes, $offset, $bytes.Length - $offset)
}

function Invoke-Task8FinalCapture {
  [CmdletBinding()]
  param(
    [Parameter(Mandatory = $true)]
    [string]$Executable,
    [Parameter(Mandatory = $true)]
    [string[]]$Arguments,
    [Parameter(Mandatory = $true)]
    [string]$BasePath
  )
  $stdoutPath = "$BasePath.stdout.txt"
  $stderrPath = "$BasePath.stderr.txt"
  $combinedPath = "$BasePath.txt"
  foreach ($path in @($stdoutPath, $stderrPath, $combinedPath)) {
    if (Test-Path -LiteralPath $path) {
      throw "Final capture path is occupied: $path"
    }
  }
  $process = Start-Process `
    -FilePath $Executable `
    -ArgumentList $Arguments `
    -WorkingDirectory (Get-Location).Path `
    -WindowStyle Hidden `
    -RedirectStandardOutput $stdoutPath `
    -RedirectStandardError $stderrPath `
    -Wait `
    -PassThru
  $process.Refresh()
  $pidValue = [int]$process.Id
  $exitCode = [int]$process.ExitCode
  if ($pidValue -le 0 -or -not $process.HasExited) {
    throw 'Final child did not expose a completed positive PID.'
  }
  if ($null -ne (Get-Process -Id $pidValue -ErrorAction SilentlyContinue)) {
    throw "Final child PID survived Wait: $pidValue"
  }
  $stdoutText = Read-Task8StrictUtf8 -Path $stdoutPath
  $stderrText = Read-Task8StrictUtf8 -Path $stderrPath
  $separator = ''
  if ($stdoutText.Length -gt 0 -and $stderrText.Length -gt 0 -and
      -not $stdoutText.EndsWith("`n", [StringComparison]::Ordinal)) {
    $separator = [Environment]::NewLine
  }
  $combinedText = $stdoutText + $separator + $stderrText
  [IO.File]::WriteAllText(
    (Join-Path (Get-Location).Path $combinedPath),
    $combinedText,
    $strictUtf8
  )
  Get-Content -LiteralPath $combinedPath -ErrorAction Stop | Out-Host
  [pscustomobject][ordered]@{
    ExitCode = $exitCode
    ProcessId = $pidValue
    Text = $combinedText
    CombinedPath = $combinedPath
    CombinedSha256 = (
      Get-FileHash -Algorithm SHA256 -LiteralPath $combinedPath `
        -ErrorAction Stop
    ).Hash
    StdoutSha256 = (
      Get-FileHash -Algorithm SHA256 -LiteralPath $stdoutPath `
        -ErrorAction Stop
    ).Hash
    StderrSha256 = (
      Get-FileHash -Algorithm SHA256 -LiteralPath $stderrPath `
        -ErrorAction Stop
    ).Hash
  }
}

$environmentNames = [string[]]@(
  'APPDATA',
  'GIT_COMMIT',
  'PYTHONDONTWRITEBYTECODE',
  'PYTHONIOENCODING',
  'PYTHONUTF8',
  'WINTER_GATE_JOB_NAME',
  'WINTER_GATE_STRUCTURED_OUTPUT_HANDLE'
)
$previousEnvironment = @{}
foreach ($name in $environmentNames) {
  $previousEnvironment[$name] = [Environment]::GetEnvironmentVariable(
    $name,
    [EnvironmentVariableTarget]::Process
  )
}
$finalRunRoot = Join-Path `
  ([IO.Path]::GetTempPath()) `
  ("winter-task8-final-" + [Guid]::NewGuid().ToString('N'))
$finalAppData = Join-Path `
  ([IO.Path]::GetTempPath()) `
  ("winter-task8-final-appdata-" + [Guid]::NewGuid().ToString('N'))
if (Test-Path -LiteralPath $finalRunRoot) {
  throw 'Fresh Final RunRoot already exists.'
}
New-Item -ItemType Directory -Path $finalAppData -ErrorAction Stop | Out-Null
try {
  Remove-Item Env:\WINTER_GATE_JOB_NAME -ErrorAction SilentlyContinue
  Remove-Item Env:\WINTER_GATE_STRUCTURED_OUTPUT_HANDLE `
    -ErrorAction SilentlyContinue
  $env:PYTHONDONTWRITEBYTECODE = '1'
  $env:PYTHONIOENCODING = 'utf-8'
  $env:PYTHONUTF8 = '1'
  $env:GIT_COMMIT = $headBefore

  $discoveryRun = Invoke-Task8FinalCapture `
    -Executable $pythonCommand.Source `
    -Arguments ([string[]]@(
      '-B', '-m', 'unittest', 'discover', '-s', 'Tools', '-v'
    )) `
    -BasePath $discoveryBase
  $discoveryRan = [regex]::Matches(
    $discoveryRun.Text,
    '(?m)^Ran ([0-9]+) tests? in [0-9]+(?:\.[0-9]+)?s\r?$'
  )
  $discoveryOk = [regex]::Matches(
    $discoveryRun.Text,
    '(?m)^OK\r?$'
  )
  $discoveryLines = [string[]]@(
    $discoveryRun.Text -split '\r?\n' |
      Where-Object { $_.Length -gt 0 }
  )
  if ($discoveryRun.ExitCode -ne 0 -or
      $discoveryRan.Count -ne 1 -or
      $discoveryRan[0].Groups[1].Value -cne '405' -or
      $discoveryOk.Count -ne 1 -or
      $discoveryLines.Count -eq 0 -or
      $discoveryLines[-1] -cne 'OK') {
    throw "Authoritative discovery was not exactly Ran 405 tests and OK: $($discoveryRun.CombinedPath)"
  }
  if (git status --short) {
    throw 'Authoritative final discovery dirtied the worktree.'
  }

  $env:APPDATA = $finalAppData
  $finalRun = Invoke-Task8FinalCapture `
    -Executable $gateHost `
    -Arguments ([string[]]@(
      '-NoLogo',
      '-NoProfile',
      '-NonInteractive',
      '-ExecutionPolicy',
      'Bypass',
      '-File',
      $winterGate,
      '-Gate',
      'Narrative',
      '-NarrativePhase',
      'Final',
      '-ProjectRoot',
      (Get-Location).Path,
      '-RunRoot',
      $finalRunRoot
    )) `
    -BasePath $finalBase
  if ($finalRun.ExitCode -ne 0) {
    throw "Narrative Final failed: $($finalRun.CombinedPath)"
  }
  $summaryPath = Join-Path $finalRunRoot 'evidence\gate-summary.json'
  if (-not [IO.File]::Exists($summaryPath)) {
    throw 'Final proof did not publish gate-summary.json.'
  }
  $summary = (Read-Task8StrictUtf8 -Path $summaryPath) |
    ConvertFrom-Json
  $steps = @($summary.steps)
  if ($summary.gate -cne 'Narrative' -or
      $summary.narrative_phase -cne 'Final' -or
      $summary.status -cne 'passed' -or
      $summary.failure_kind -ne $null -or
      $summary.head_token -cne $headToken -or
      $summary.host.edition -cne 'Desktop' -or
      -not ([string]$summary.host.version).StartsWith(
        '5.1.',
        [StringComparison]::Ordinal
      ) -or
      $steps.Count -ne 9 -or
      @($steps | Where-Object {
        $_.status -cne 'passed' -or
        -not $_.process_started -or
        -not $_.tree_drained -or
        $_.had_live_descendants_after_root_exit
      }).Count -ne 0) {
    throw 'Final summary is not the exact clean nine-step proof.'
  }
  $headAfter = (git rev-parse --verify HEAD).Trim()
  if ($LASTEXITCODE -ne 0 -or $headAfter -cne $headBefore -or
      (git status --short)) {
    throw 'HEAD or worktree changed during final evidence.'
  }
  foreach ($path in $boundPaths) {
    $after = (
      Get-FileHash -Algorithm SHA256 -LiteralPath $path -ErrorAction Stop
    ).Hash
    if ($after -cne $hashesBefore[$path]) {
      throw "Final bound input changed during evidence: $path"
    }
  }
  $summarySha256 = (
    Get-FileHash -Algorithm SHA256 -LiteralPath $summaryPath -ErrorAction Stop
  ).Hash
  Write-Output "FINAL_HEAD=$headAfter"
  Write-Output "DISCOVERY_PID=$($discoveryRun.ProcessId)"
  Write-Output "DISCOVERY_LOG=$($discoveryRun.CombinedPath)"
  Write-Output "DISCOVERY_LOG_SHA256=$($discoveryRun.CombinedSha256)"
  Write-Output "DISCOVERY_STDOUT_SHA256=$($discoveryRun.StdoutSha256)"
  Write-Output "DISCOVERY_STDERR_SHA256=$($discoveryRun.StderrSha256)"
  Write-Output "FINAL_PID=$($finalRun.ProcessId)"
  Write-Output "FINAL_LOG=$($finalRun.CombinedPath)"
  Write-Output "FINAL_LOG_SHA256=$($finalRun.CombinedSha256)"
  Write-Output "FINAL_STDOUT_SHA256=$($finalRun.StdoutSha256)"
  Write-Output "FINAL_STDERR_SHA256=$($finalRun.StderrSha256)"
  Write-Output "FINAL_RUN_ROOT=$finalRunRoot"
  Write-Output "FINAL_SUMMARY_SHA256=$summarySha256"
}
finally {
  foreach ($name in $environmentNames) {
    $previous = $previousEnvironment[$name]
    if ($null -eq $previous) {
      Remove-Item -LiteralPath "Env:\$name" -ErrorAction SilentlyContinue
    }
    else {
      [Environment]::SetEnvironmentVariable(
        $name,
        [string]$previous,
        [EnvironmentVariableTarget]::Process
      )
    }
  }
}
```

Expected: one completed positive discovery PID, real exit 0, exactly one
`Ran 405 tests` line, exactly one terminal `OK`, and no loader/import error.
Only then does one completed positive Final PID start. Final uses Desktop
PowerShell 5.1, binds current full HEAD, publishes nine passed and drained
steps, leaves no live descendant, and prints immutable capture and summary
hashes. All bound paths, HEAD, index, and tracked status remain unchanged.

Do not separately rerun governance, capability, gate, discovery, Batch, or
Final after this fence succeeds. Task 13 is read-only and writes ignored
review evidence only.

---

## Task 13: Obtain final immutable reviews without changing tracked HEAD

**Tracked files:** none.

**Ignored evidence:** one immutable final-review input, one Spec decision, one
Standards decision, their raw reports, the font-delta record, and the
authoritative Task 12 discovery/Final captures.

- [ ] **Step 1: Create one immutable review input bound to the Final-proved SHA**

The review input has exactly these properties:

1. `schema_version`;
2. `baseline`;
3. `plan_path`;
4. `plan_canonical_sha256`;
5. `implementation_range_start`;
6. `implementation_head`;
7. `implementation_tree`;
8. `ordered_commit_shas`;
9. `content_ledger_sha256`;
10. `discovery_log_sha256`;
11. `final_gate_summary_sha256`;
12. `font_sha256`;
13. `font_byte_delta`;
14. `changed_paths`.

`schema_version` is strict integer 1. `baseline` is literal
`cd26d62cda05e40dbcd6c953bd2e620a65d59c0c`.
`implementation_range_start` is the unique committed
`docs: plan winter interlude narrative delivery` SHA.
`implementation_head` is the full SHA printed as `FINAL_HEAD` by Task 12 and
must equal current HEAD. `ordered_commit_shas` contains every commit from the
dedicated plan through final HEAD in chronological order. `changed_paths` is
the exact sorted tracked-path set for that range. All hashes are uppercase
SHA-256 hex except Git commit/tree IDs, which are lowercase forty-character
hex. The font delta comes from the ignored record produced by the reviewed
Task 12 font command.

Write the canonical one-object JSON only beneath `.superpowers/sdd/` with a
filename containing the final twelve-character HEAD token. Use strict UTF-8
without BOM and refuse to replace an existing same-HEAD input. Hash the exact
review-input bytes before launching either reviewer.

- [ ] **Step 2: Run fresh independent Spec and Standards reviews**

Both reviewers receive the same immutable review input plus the exact files
and ignored evidence it hashes. Neither reviewer may read the other review or
decision.

The Spec reviewer checks the approved design, L0 user choice, all 18 literal
fact cards and addenda, all user approvals, all 72 active paths, optional
mitigation/southern substitutions, six outcome contracts, six coordinated
visible semantics, no perfect solution, no invented route, no downstream
consumer prose, and the asset/package scope.

The Standards reviewer checks complete test and production bodies, focused
RED/GREEN evidence, exact staging scopes and subjects, verified Opus
provenance, blind raw/composite workflow, safe rejected-directory deletion,
loader errors, count formulas, per-scene one-Batch evidence, one final
discovery, one Final, immutable captures, clean final HEAD, and the absence of
any post-Final tracked write.

Each decision has exactly the nine Task 0 properties: `schema_version`,
`review_axis`, `reviewer_id`, `review_input_sha256`, `head`, `critical_count`,
`important_count`, `verdict`, and `raw_report`. Both must contain strict zero
integer counts, verdict `READY`, and an exact report line
`Critical 0 / Important 0 - READY`. Reviewer IDs are nonempty and distinct.

- [ ] **Step 3: Validate both decisions and the unchanged final identity**

```powershell
$head = (git rev-parse --verify HEAD).Trim()
if ($LASTEXITCODE -ne 0 -or $head -notmatch '\A[0-9a-f]{40}\z') {
  throw 'Final review validator could not resolve HEAD.'
}
if ((git log -1 --pretty=%s).Trim() -cne
    'feat: finalize winter interlude prose') {
  throw 'A tracked commit exists after the final prose commit.'
}
if (git status --short) {
  throw 'Final review validator requires a clean worktree.'
}
git diff --cached --quiet
if ($LASTEXITCODE -ne 0) {
  throw 'Final review validator requires an empty index.'
}
$headToken = $head.Substring(0, 12)
$inputPath = ".superpowers/sdd/task8-final-review-input-$headToken.json"
$specPath = ".superpowers/sdd/task8-final-spec-review-$headToken.json"
$standardsPath = ".superpowers/sdd/task8-final-standards-review-$headToken.json"
foreach ($path in @($inputPath, $specPath, $standardsPath)) {
  if (-not [IO.File]::Exists($path)) {
    throw "Final review evidence is missing: $path"
  }
}
$strictUtf8 = New-Object Text.UTF8Encoding($false, $true)
$inputBytes = [IO.File]::ReadAllBytes($inputPath)
$inputHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $inputPath).Hash
$input = ($strictUtf8.GetString($inputBytes)) | ConvertFrom-Json
$expectedInputProperties = [string[]]@(
  'schema_version',
  'baseline',
  'plan_path',
  'plan_canonical_sha256',
  'implementation_range_start',
  'implementation_head',
  'implementation_tree',
  'ordered_commit_shas',
  'content_ledger_sha256',
  'discovery_log_sha256',
  'final_gate_summary_sha256',
  'font_sha256',
  'font_byte_delta',
  'changed_paths'
)
$actualInputProperties = [string[]]@($input.PSObject.Properties.Name)
if (@(Compare-Object `
      ($expectedInputProperties | Sort-Object) `
      ($actualInputProperties | Sort-Object)).Count -ne 0) {
  throw 'Final review input properties are not exact.'
}
if (-not ($input.schema_version -is [int]) -or
    $input.schema_version -ne 1 -or
    $input.baseline -cne 'cd26d62cda05e40dbcd6c953bd2e620a65d59c0c' -or
    $input.plan_path -cne
      'docs/superpowers/plans/2026-08-09-winter-interlude-narrative-delivery.md' -or
    $input.implementation_head -cne $head -or
    $input.implementation_tree -cne (git rev-parse 'HEAD^{tree}').Trim()) {
  throw 'Final review input is bound to the wrong implementation identity.'
}
$planHash = (
  Get-FileHash -Algorithm SHA256 -LiteralPath $input.plan_path
).Hash
$ledgerHash = (
  Get-FileHash -Algorithm SHA256 `
    -LiteralPath 'docs/development/winter-interlude-content-ledger.md'
).Hash
$fontHash = (
  Get-FileHash -Algorithm SHA256 -LiteralPath 'game/msyh.ttf'
).Hash
if ($input.plan_canonical_sha256 -cne $planHash -or
    $input.content_ledger_sha256 -cne $ledgerHash -or
    $input.font_sha256 -cne $fontHash) {
  throw 'Final review input file hashes do not match final HEAD.'
}
$decisions = @()
foreach ($entry in @(
  [pscustomobject]@{ Path = $specPath; Axis = 'Spec' },
  [pscustomobject]@{ Path = $standardsPath; Axis = 'Standards' }
)) {
  $decisionBytes = [IO.File]::ReadAllBytes($entry.Path)
  $decision = ($strictUtf8.GetString($decisionBytes)) | ConvertFrom-Json
  $expectedDecisionProperties = [string[]]@(
    'schema_version',
    'review_axis',
    'reviewer_id',
    'review_input_sha256',
    'head',
    'critical_count',
    'important_count',
    'verdict',
    'raw_report'
  )
  $actualDecisionProperties = [string[]]@(
    $decision.PSObject.Properties.Name
  )
  if (@(Compare-Object `
        ($expectedDecisionProperties | Sort-Object) `
        ($actualDecisionProperties | Sort-Object)).Count -ne 0) {
    throw "$($entry.Axis) decision properties are not exact."
  }
  if (-not ($decision.schema_version -is [int]) -or
      $decision.schema_version -ne 1 -or
      $decision.review_axis -cne $entry.Axis -or
      -not ($decision.reviewer_id -is [string]) -or
      [string]::IsNullOrWhiteSpace($decision.reviewer_id) -or
      $decision.review_input_sha256 -cne $inputHash -or
      $decision.head -cne $head -or
      -not ($decision.critical_count -is [int]) -or
      $decision.critical_count -ne 0 -or
      -not ($decision.important_count -is [int]) -or
      $decision.important_count -ne 0 -or
      $decision.verdict -cne 'READY' -or
      $decision.raw_report -notmatch
        '(?m)^Critical 0 / Important 0 - READY$' -or
      $decision.raw_report -match '(?i)\bNOT\s+READY\b') {
    throw "$($entry.Axis) decision is not READY on final HEAD."
  }
  $decisions += $decision
}
if ($decisions[0].reviewer_id -ceq $decisions[1].reviewer_id) {
  throw 'Final Spec and Standards reviewers are not independent.'
}
Write-Output "FINAL_REVIEWED_HEAD=$head"
Write-Output "FINAL_REVIEW_INPUT_SHA256=$inputHash"
Write-Output "FINAL_SPEC_REVIEWER=$($decisions[0].reviewer_id)"
Write-Output "FINAL_STANDARDS_REVIEWER=$($decisions[1].reviewer_id)"
```

If either reviewer reports a finding, do not patch after Final. Return to the
owning L0, scene, or final-contract addendum. A visible change requires renewed
user approval. Create a new final commit, then execute one new authoritative
discovery/Final pair and two new reviews bound to the new SHA. Superseded
ignored evidence is never presented as current proof.

Task 8 succeeds only when one identical full SHA is the final tracked commit,
the 405-test discovery target, the green Final target, and both fresh review
targets. No tracked evidence record, cleanup commit, ledger commit, or other
write follows it.

**Final asset and package audit:** required art, music, sound effects,
portraits, animation, and UI are all zero. The existing asset set is reused.
The only possible binary delta is `game/msyh.ttf`; report its exact signed byte
delta and resulting package impact. S07's background mismatch remains the
already-declared later art debt.

---

# 《幕间·第一个冬天》Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add an optional 50–55 minute winter-governance interlude between the southern side chapter and Chapter 2, preserve old saves and all nine ending boundaries, and deliver the one required winter granary background without adding music, SFX, portraits, animation, or UI images.

**Architecture:** Put the new state machine and story in one deep module, game/governance_winter_interlude.rpy. All downstream scenes consume one read-only winter context instead of duplicating migration precedence. New paths write only the four winter result fields and idempotently append the two approved existing compatibility markers; they add no other persistent field. Legacy governance labels remain in place and old continuation labels route to stable Chapter 2 anchors. Chapter selection, direct Chapter 2 entry, BGM restoration, mobile rendering, and package-size checks are verified at runtime.

**Tech Stack:** Ren'Py 8.5.2, Python 3 unittest, PowerShell, Claude Code with claude-opus-4-6, GPT image generation, FFmpeg WebP conversion, Pillow inspection, existing CourtOfShadows scanners and release verifiers.

## Global Constraints

- The approved design is docs/superpowers/specs/2026-08-08-governance-winter-interlude-design.md. If this plan and that design differ, the design wins and the discrepancy must be resolved before implementation continues.
- This plan must be committed on master before execution. First deliver the current codex/v3-9-2-rc player-feedback work, then merge it into the tracked master plan/BGM/design head. Do not build the interlude on either history alone.
- Use an isolated worktree and a new branch named codex/governance-winter-interlude.
- Preserve unrelated user changes. Never reset, restore, clean, or overwrite the dirty RC worktree.
- Use TDD for every code or route change: add the focused failing assertion, run it and record RED, make the minimum production change, then run GREEN.
- Do not remove, move, or rewrite the bodies of gov_merchant, gov_building, or gov_famine_crisis. Old saves may resume inside them.
- New routes must not write power, wealth, faith, loyalty, reputation, intrigue, courage, any relationship, alliance, truth, marriage, ending, achievement, battle, or ch5_exp_defender_bonus state.
- New active and delegated routes must not set famine_prevented to True and must not set gov_merchant_outcome. Those fields remain legacy compatibility data.
- merchant_deal is the later Karl route and must not be treated as gov_merchant_outcome or winter_policy.
- All policy and seed-priority options remain visible. Attributes and prior decisions may soften one cost in prose only; they may not hide an option or erase every cost.
- The interlude may occupy only the final several days of the existing one-month Chapter 1-to-2 gap. It must not add a second month.
- Every normal, delegated, replay, invalid-state, and legacy exit must reach Chapter 2 after clearing snow and temporary audio.
- Chapter 2's cinematic owns its music. The interlude must stop its temporary music before the cinematic; chapter2_start must explicitly start castle_calm.ogg after the cinematic returns.
- Generate new game prose through a fresh Claude Code session using /model claude-opus-4-6. Give each session only that scene's current facts, canon, entry/exit seam, and result contract. Do not send old drafts, rejected text, Few-shot examples, writing-game-copy constraints, local paths, or code logic.
- Claude Code produces prose only. Codex owns labels, state, routes, tests, assets, and integration.
- Read CANON.md before each prose batch. After prose integration run canon, portrait, narration-overlap, nested-quote, font, and AI-smell scans; AI-smell findings are an inspection queue, not an automatic global rewrite list.
- Asset contract: add exactly one shipping art file, game/images/bg_winter_granary.webp, at 1280×720 and no more than 1.2 MiB. Total Windows and Android package growth against the clean equal-metadata governance-winter-package-baseline must be no more than 2.0 MiB.
- Reuse winter_wind.ogg, market_bustle.ogg, castle_calm.ogg, tension.ogg, existing door/crowd/bell/page/coin SFX, existing portraits, and weather_snow.
- Do not add music, SFX, portraits, animation files, UI images, alternate assets, or test copies under game/.
- The third-chapter tax, plague, and construction pacing work is explicitly out of scope.
- Commit each independently testable task. Do not claim completion from source scans alone; require fresh Python, Ren'Py runtime, lint, old-save, mobile-render, Windows-package, and Android-package evidence.

---

## File Map

- docs/superpowers/specs/2026-08-08-governance-winter-interlude-design.md: approved behavior and acceptance contract.
- game/governance_winter_interlude.rpy: new defaults, pure helpers, interlude labels, choices, cleanup, and result prose.
- game/script.rpy: normal Chapter 1/southern-to-winter route.
- game/chapter2.rpy: direct-entry neutral seed, old-call removal, stable anchors, legacy continuation pads, Chapter 2 BGM restoration, Harrenhall political pressure, merchant recognition, and Karl's read-only terms echo.
- game/save_compat.rpy: call the centralized idempotent migration without duplicating its rules.
- game/governance.rpy: read-only source of legacy prose and labels; do not move or delete its bodies.
- game/gallery.rpy: chapter entry, unlock rule, replay slot, background gallery entry, and dynamic gallery row count.
- game/images_def.rpy: third parallel chapter-icon entry and the new background definitions.
- game/replay.rpy: existing auto_ch-<id> behavior; no new save system.
- game/interludes.rpy: later merchant-road echo.
- game/chapter5.rpy: supplies text that combines built_granary with the saved winter policy.
- game/chapter5_expansion.rpy: winter-aware defense prose while preserving every existing numeric bonus.
- game/endings_expansion.rpy: legacy famine echoes and one concrete People's Lord five-year echo.
- game/cinematics.rpy: read-only Chapter 2 cinematic music owner; change only if a verified defect remains after routing.
- game/test_game.rpy: runtime state, migration, continuations, routing, ending invariance, audio, chapter select, and render suites.
- Tools/Run-RenPySuite.ps1: fail-closed wrapper for isolated savedirs, expected RED/GREEN status, fixture staging, variant cleanup, and per-suite evidence.
- Tools/test_governance_winter_interlude.py: source, asset, route, and forbidden-write contracts.
- Tools/test_story_timeline.py: one-month placement and duplicate-time-card regression.
- tests/fixtures/winter_legacy/: five engine-native archives created against the pre-feature runtime: three live continuation captures, one real completed-famine capture, one deliberately synthetic no-governance compatibility state, plus manifest and checksums.
- tests/screenshots/: reviewed small/touch 100% and 150% render baselines if the repository's existing screenshot policy tracks them.
- game/images/bg_winter_granary.webp: the only new shipping asset.
- Tools/test_release_contract.py, Tools/verify_distributions.py, game/options.rpy, game/effects.rpy, android.json, README.txt, CHANGELOG.txt, and game/changelog.rpy: the 3.10 source/package metadata contract.

---

### Task 0: Deliver the 3.9.2 feedback batch and create the 3.10 worktree

**Files:**

- Existing dirty worktree: C:/Users/22325/Documents/Codex/2026-07-31/new-chat-2/work/CourtOfShadows-3.9.2-rc
- Verify tracked on master: docs/superpowers/plans/2026-08-08-governance-winter-interlude.md
- Commit there:
  - Tools/test_player_feedback_regressions.py
  - game/chapter3.rpy
  - game/chapter4.rpy
  - game/chapter5.rpy
  - game/endings_expansion.rpy
  - game/msyh.ttf
  - docs/superpowers/plans/2026-08-05-player-feedback-completion.md
  - docs/superpowers/plans/2026-08-05-raw-opus-copy-generation.md
- Merge with:
  - the current tracked master head containing the Chapter 3 BGM fix, approved winter design, and this implementation plan
  - game/chapter3.rpy
  - game/cinematics.rpy
- Create worktree:
  - C:/Users/22325/Documents/Codex/2026-07-31/new-chat-2/work/CourtOfShadows-governance-winter

**Interfaces:**

- Consumes: codex/v3-9-2-rc with its current six modified files and two untracked plans, plus master's Chapter 3 BGM fix, approved winter design, and this tracked plan.
- Produces: a clean codex/governance-winter-interlude branch containing both histories and a tag governance-winter-baseline.

- [ ] **Step 1: Prove this plan is tracked before creating another worktree**

Run from the main repository:

~~~powershell
$mainRepo = 'E:\Projects\renpy-8.5.2-sdk\CourtOfShadows'
git -C $mainRepo ls-files --error-unmatch docs/superpowers/plans/2026-08-08-governance-winter-interlude.md
if ($LASTEXITCODE -ne 0) { throw 'The winter implementation plan is not committed on master.' }
$masterStart = (git -C $mainRepo rev-parse master).Trim()
if ($LASTEXITCODE -ne 0) { throw 'Could not resolve the master start commit.' }
$masterDirty = @(git -C $mainRepo status --porcelain)
if ($masterDirty.Count -ne 0) { throw "Master is not clean: $($masterDirty -join '; ')" }
git -C $mainRepo status --short --branch
~~~

Expected: the plan is tracked, master is clean, and masterStart is recorded in the task evidence. It will be newer than the pre-plan 19a00be snapshot; never hard-code that older SHA as the feature start.

- [ ] **Step 2: Re-run the RC's focused and full gates before committing it**

Run from the RC worktree:

~~~powershell
python -m unittest Tools.test_player_feedback_regressions -v
if ($LASTEXITCODE -ne 0) { throw 'RC player-feedback regressions failed.' }
python -m unittest discover -s Tools -p "test_*.py" -v
if ($LASTEXITCODE -ne 0) { throw 'RC full Python suite failed.' }
python Tools/test_story_timeline.py -v
if ($LASTEXITCODE -ne 0) { throw 'RC timeline suite failed.' }
python Tools/test_release_regressions.py
if ($LASTEXITCODE -ne 0) { throw 'RC release regressions failed.' }
git diff --check
if ($LASTEXITCODE -ne 0) { throw 'RC diff failed whitespace validation.' }
git status --short
~~~

Expected: player-feedback tests report 50/50, full Python reports the current expected total with zero failures, timeline reports 14/14, doubled-percent/release regression passes, and status lists only the known six modified files and two plans. If totals have legitimately changed because the RC itself already added tests, record the fresh total and require zero failures rather than accepting the historical number.

- [ ] **Step 3: Commit the two plan documents and the completed player-feedback diff**

Use two focused commits:

~~~powershell
git add docs/superpowers/plans/2026-08-05-player-feedback-completion.md docs/superpowers/plans/2026-08-05-raw-opus-copy-generation.md
if ($LASTEXITCODE -ne 0) { throw 'Could not stage RC plan documents.' }
git commit -m "docs: record player feedback completion workflow"
if ($LASTEXITCODE -ne 0) { throw 'RC plan-document commit failed.' }
git add Tools/test_player_feedback_regressions.py game/chapter3.rpy game/chapter4.rpy game/chapter5.rpy game/endings_expansion.rpy game/msyh.ttf
if ($LASTEXITCODE -ne 0) { throw 'Could not stage the RC production batch.' }
git diff --cached --check
if ($LASTEXITCODE -ne 0) { throw 'RC production index failed whitespace validation.' }
git commit -m "fix: complete player feedback ending revisions"
if ($LASTEXITCODE -ne 0) { throw 'RC production commit failed.' }
$rcDirty = @(git status --porcelain)
if ($rcDirty.Count -ne 0) { throw "RC worktree is not clean after its two commits: $($rcDirty -join '; ')" }
$rcHead = (git rev-parse HEAD).Trim()
if ($LASTEXITCODE -ne 0) { throw 'Could not record the completed RC commit.' }
$rcHead
~~~

Expected: the RC worktree is clean. Do not include any other file. Record the printed full `$rcHead` SHA as immutable task evidence; the later merge consumes that exact commit, never a branch name discovered at merge time.

- [ ] **Step 4: Create the isolated governance worktree from the recorded master head**

Use the exact `$masterStart` SHA recorded in Step 1. If this is a new shell, re-enter that evidence value; do not derive a new start silently after the RC work has taken time.

~~~powershell
$mainRepo = 'E:\Projects\renpy-8.5.2-sdk\CourtOfShadows'
$featureRoot = 'C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\work\CourtOfShadows-governance-winter'
if (-not (Get-Variable masterStart -ErrorAction SilentlyContinue) -or [string]::IsNullOrWhiteSpace([string]$masterStart)) { throw 'Re-enter the exact Step 1 masterStart evidence SHA.' }
$currentMaster = (git -C $mainRepo rev-parse master).Trim()
if ($LASTEXITCODE -ne 0) { throw 'Could not verify master for the feature worktree.' }
if ($currentMaster -ne $masterStart) { throw 'Master moved after Step 1; stop and review the new history rather than silently changing the feature base.' }
if (Test-Path -LiteralPath $featureRoot) { throw 'Feature worktree path already exists; inspect it rather than overwriting it.' }
git -C $mainRepo show-ref --verify --quiet refs/heads/codex/governance-winter-interlude
if ($LASTEXITCODE -eq 0) { throw 'Feature branch already exists; inspect/resume it rather than recreating it.' }
git -C $mainRepo worktree add -b codex/governance-winter-interlude $featureRoot $masterStart
if ($LASTEXITCODE -ne 0) { throw 'Feature worktree creation failed.' }
if ((git -C $featureRoot rev-parse HEAD).Trim() -ne $masterStart) { throw 'Feature worktree started at the wrong commit.' }
git -C $featureRoot status --short --branch
git -C $featureRoot ls-files --error-unmatch docs/superpowers/plans/2026-08-08-governance-winter-interlude.md
if ($LASTEXITCODE -ne 0) { throw 'Tracked winter plan is missing from the feature worktree.' }
~~~

Expected: the new worktree is clean at the recorded masterStart and contains this plan.

- [ ] **Step 5: Merge the RC branch without dropping either side's BGM or font coverage**

Before merging, record both input font hashes and sizes. Also fail closed if the approved Windows source font is unavailable and record its full SHA-256; font regeneration is not reproducible without pinning that input. The anticipated game/msyh.ttf conflict is binary and cannot be resolved with apply_patch or a text hunk strategy:

~~~powershell
$mainRepo = 'E:\Projects\renpy-8.5.2-sdk\CourtOfShadows'
$featureRoot = 'C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\work\CourtOfShadows-governance-winter'
$rcRoot = 'C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\work\CourtOfShadows-3.9.2-rc'
$fontSource = 'C:\Windows\Fonts\msyh.ttc'
if (-not (Get-Variable rcHead -ErrorAction SilentlyContinue) -or [string]::IsNullOrWhiteSpace([string]$rcHead)) { throw 'Re-enter the exact Step 3 rcHead evidence SHA.' }
if ((git -C $rcRoot rev-parse HEAD).Trim() -ne $rcHead) { throw 'RC worktree moved away from the recorded completed commit.' }
if ((git -C $mainRepo rev-parse codex/v3-9-2-rc).Trim() -ne $rcHead) { throw 'RC branch ref moved away from the recorded completed commit.' }
if (-not (Test-Path -LiteralPath $fontSource -PathType Leaf)) { throw 'Approved Microsoft YaHei source font is missing.' }
$fontSourceItem = Get-Item -LiteralPath $fontSource
$fontSourceHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $fontSource).Hash
if ($fontSourceItem.Length -ne 19704352 -or $fontSourceHash -ne 'D79C55E68B1131EEA0CC1C47BE4F572D964F28C682E143DB2AD09C1E4CB07A3F') { throw 'Approved Microsoft YaHei source font identity changed; stop for review.' }
Get-Item -LiteralPath (Join-Path $featureRoot 'game/msyh.ttf'), (Join-Path $rcRoot 'game/msyh.ttf') | Select-Object FullName,Length
Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $featureRoot 'game/msyh.ttf'), (Join-Path $rcRoot 'game/msyh.ttf')
$fontSourceItem | Select-Object FullName,Length
$fontSourceHash
~~~

~~~powershell
git -C $featureRoot merge --no-ff --no-edit $rcHead
$mergeExit = $LASTEXITCODE
git -C $featureRoot rev-parse --verify -q MERGE_HEAD *> $null
$mergeInProgress = $LASTEXITCODE -eq 0
if ($mergeExit -eq 0) { throw 'The anticipated RC/font conflict disappeared; stop and remap the merge before continuing.' }
if (-not $mergeInProgress) { throw 'RC merge failed without leaving a resolvable merge state.' }
git -C $featureRoot status --short
~~~

Resolve every text conflict with apply_patch. Preserve all RC story/release changes and preserve these two master contracts:

~~~renpy
call cinematic_chapter3 from _call_cinematic_ch3
$ set_mood("mystery", fadein=2.0)
~~~

The Chapter 3 cinematic may stop its own temporary music; chapter3_start must restore mystery music after it returns. Do not resolve chapter3.rpy or cinematics.rpy wholesale with ours/theirs.

Resolve the binary font by regenerating it from the fully merged script character set, not by choosing ours/theirs and not by copying one branch's subset:

~~~powershell
Set-Location $featureRoot
python subset_font.py
if ($LASTEXITCODE -ne 0) { throw 'Merged font regeneration failed.' }
git add game/msyh.ttf
if ($LASTEXITCODE -ne 0) { throw 'Could not stage the regenerated merged font.' }
python prepare_release.py
if ($LASTEXITCODE -ne 0) { throw 'Merged font does not cover the merged script set.' }
~~~

This regeneration is the only permitted binary conflict resolution. It must run after all text conflicts are resolved so the font contains the union of both histories.

After resolving:

~~~powershell
$resolvedConflicts = @(git -C $featureRoot diff --name-only --diff-filter=U)
foreach ($path in $resolvedConflicts) {
  git -C $featureRoot add -- $path
  if ($LASTEXITCODE -ne 0) { throw "Failed to stage resolved conflict: $path" }
}
# Explicitly stage the two known overlapping paths even if one was already resolved earlier.
git -C $featureRoot add -- game/chapter3.rpy game/msyh.ttf
if ($LASTEXITCODE -ne 0) { throw 'Failed to stage known Chapter 3/font resolutions.' }
git -C $featureRoot add -u
if ($LASTEXITCODE -ne 0) { throw 'Failed to stage remaining resolved tracked paths.' }
$unmerged = @(git -C $featureRoot diff --name-only --diff-filter=U)
if ($unmerged.Count -ne 0) { throw "Unmerged paths remain: $($unmerged -join ', ')" }
git -C $featureRoot diff --cached --check
if ($LASTEXITCODE -ne 0) { throw 'Merged index failed whitespace validation.' }
git -C $featureRoot commit --no-edit
if ($LASTEXITCODE -ne 0) { throw 'Integrated baseline merge commit failed.' }
$mergeHead = (git -C $featureRoot rev-parse HEAD).Trim()
$mergeSecondParent = (git -C $featureRoot rev-parse "$mergeHead^2").Trim()
if ($LASTEXITCODE -ne 0 -or $mergeSecondParent -ne $rcHead) { throw 'Integrated merge is not bound to the recorded RC commit as its second parent.' }
~~~

Expected: no unmerged path remains and the merge commit contains both the approved winter design and the full RC.

- [ ] **Step 6: Verify the integrated baseline and tag it**

From the feature worktree:

~~~powershell
python -m unittest discover -s Tools -p "test_*.py" -v
if ($LASTEXITCODE -ne 0) { throw 'Integrated baseline Python suite failed.' }
python Tools/test_story_timeline.py -v
if ($LASTEXITCODE -ne 0) { throw 'Integrated baseline timeline suite failed.' }
python Tools/scan_canon.py
if ($LASTEXITCODE -ne 0) { throw 'Integrated baseline canon scanner crashed.' }
python scan_missing_portraits.py
if ($LASTEXITCODE -ne 0) { throw 'Integrated baseline portrait scanner crashed.' }
python scan_narration_overlap.py
if ($LASTEXITCODE -ne 0) { throw 'Integrated baseline narration scanner crashed.' }
git diff --check
if ($LASTEXITCODE -ne 0) { throw 'Integrated baseline diff failed whitespace validation.' }
$dirty = @(git status --porcelain)
if ($dirty.Count -ne 0) { throw "Integrated baseline is not clean: $($dirty -join '; ')" }
$baselineHead = (git rev-parse HEAD).Trim()
git show-ref --verify --quiet refs/tags/governance-winter-baseline
if ($LASTEXITCODE -eq 0) {
  $tagHead = (git rev-list -n 1 governance-winter-baseline).Trim()
  if ($tagHead -ne $baselineHead) { throw 'Existing governance-winter-baseline does not point at HEAD.' }
}
else {
  git tag governance-winter-baseline $baselineHead
  if ($LASTEXITCODE -ne 0) { throw 'Could not create governance-winter-baseline.' }
}
if ((git rev-list -n 1 governance-winter-baseline).Trim() -ne $baselineHead) { throw 'Baseline tag verification failed.' }
$baselineHead
~~~

Expected: all gates pass, both portrait scanners report zero actionable findings, the branch is clean, and governance-winter-baseline points at the merge commit. Record the printed full `$baselineHead` as immutable task evidence. If scan_missing_portraits.py refreshes tracked missing_portraits_B.txt only because merged source line numbers changed, inspect and commit that reproducible report, then rerun every Step 6 gate before tagging; any new finding must be fixed instead. If the tag already exists, verify it points at HEAD; do not move it silently.

**Asset audit:** This task adds no new art, music, SFX, animation, or UI asset. The font is regenerated from the merged source union; record its exact byte/hash change. Package impact is the already-approved RC delta only; the winter feature baseline begins after this merge.

---

### Task 1: Capture real pre-change legacy saves and the asset baseline

**Files:**

- Temporarily modify, then restore exactly: game/chapter2.rpy
- Modify: game/test_game.rpy, retaining only the test-command fixture public-key guard, the five empirically minimal private lint-reachability roots, the official global test-process teardown, and one semantic ChoiceReturn-readiness gate for the existing resistance-transition click after temporary drivers/suites are removed
- Create: Tools/Run-RenPySuite.ps1
- Create: Tools/test_governance_winter_interlude.py with runner and fixture-infrastructure contracts; later tasks extend this same module
- Create: tests/fixtures/winter_legacy/winter-legacy-merchant-inside-LT1.save
- Create: tests/fixtures/winter_legacy/winter-legacy-building-inside-LT1.save
- Create: tests/fixtures/winter_legacy/winter-legacy-famine-inside-LT1.save
- Create: tests/fixtures/winter_legacy/winter-legacy-famine-success-after-LT1.save
- Create: tests/fixtures/winter_legacy/winter-legacy-chapter2-no-governance-LT1.save
- Create: tests/fixtures/winter_legacy/manifest.json
- Create: tests/fixtures/winter_asset_baseline.json

**Interfaces:**

- Consumes: the integrated baseline while the three old Chapter 2 calls and their generated continuation labels still exist.
- Produces: one fail-closed Ren'Py test runner; a permanent public-key guard active only for `renpy test`; five private no-op reachability roots that prevent Ren'Py 8.5.2 from falsely linting top-level test declarations separated by explicit return/jump boundaries as unreachable; the official `testsuite global` teardown that makes Suite and Full test processes exit normally after their final status; one semantic readiness gate that waits for the existing resistance-transition choice action to become a real `ChoiceReturn` before its physical click; five loadable engine-native Ren'Py archives: three live old-label return stacks, one real old famine completion state at a permanent production label, and one deliberately synthetic later-Chapter-2 neutral compatibility state at that same permanent label; plus slot/key/commit/version/hash metadata and a pre-feature shipping-asset inventory.

- [ ] **Step 1: Add one fail-closed Ren'Py suite runner used by every later task**

Create Tools/Run-RenPySuite.ps1 with required parameters ProjectRoot and SaveDir; Mode defaults to Suite and also accepts Full or Lint. Suite and Expect (PASSED or FAILED) are required for Suite mode, Expect=PASSED is required for Full mode, and neither is accepted for Lint mode. Optional parameters are ExpectedPattern, Variant, StageLegacyFixtures, ExtraArgs, EvidenceDir, and a bounded TimeoutSeconds. It must:

- require SaveDir to be an explicit unique path outside the player's CourtOfShadows-save and create it before Ren'Py starts;
- when StageLegacyFixtures is set, read manifest.json, verify every SHA-256, and copy exact *-LT1.save filenames before startup;
- set RENPY_VARIANT only inside try/finally and always remove/restore it;
- start one identifiable native Ren'Py process through System.Diagnostics.Process/Start-Process -PassThru, record its PID and start UTC, wait only up to TimeoutSeconds, and on timeout terminate only that recorded process before failing; never search for or terminate other Ren'Py processes;
- Suite mode invokes `test <suite>`; Full mode invokes `test`; Lint mode invokes `lint --error-code`. Every mode passes the explicit --savedir and captures the immediate exit code after the bounded wait;
- Suite and Full modes require a log.txt modified after start and exactly one [rpytest] Status matching Expect; Lint mode instead writes this process's stdout/stderr to a unique fresh evidence file and requires exit zero;
- for PASSED require exit 0; for FAILED require nonzero exit, ExpectedPattern in the fresh log, and reject parse/import/syntax/missing-file crashes as the cause;
- after exit or timeout, assert the recorded PID is no longer alive; copy the fresh log/output to a unique evidence filename containing mode, suite where applicable, expectation, timestamp, and HEAD;
- accept ExtraArgs such as --overwrite-screenshots without string-built shell execution.

Add source-level tests for the runner's player-save rejection, exact status counting, fixture hash fail-closed behavior, bounded-wait/recorded-PID cleanup, Suite/Full/Lint argument construction, lint --error-code enforcement, and try/finally variant cleanup. From this point onward, every Ren'Py test or lint command in this plan must use this helper or reproduce all of these checks inline; a bare renpy.exe test/lint call is not acceptable evidence.

Ren'Py 8.5.2's test executor writes the final `[rpytest] Status` but does not exit on its own. Add the SDK's official lifecycle pattern to game/test_game.rpy:

~~~renpy
testsuite global:
    teardown:
        exit
~~~

This is permanent test-only infrastructure. The runner must still require a natural zero exit and must treat timeout/forced termination as failure; it may never accept a process merely because a PASSED line appeared before timeout. Prove both one ordinary named Suite and Full mode exit zero, leave only the recorded PID gone, and contain exactly one fresh PASSED status.

The first real Full RED may expose the existing `low_score_hard_resistance_reaches_grind_failure` click racing the choice screen's 0.6-second `NullAction` guard. If and only if that exact case is the sole Full failure, add a semantic wait immediately before its existing click that requires the exact target text to resolve uniquely and its button action to be `renpy.ui.ChoiceReturn`. Do not add a fixed sleep or change the click/result. Preserve the 55/56 Full RED and final 56/56 GREEN evidence; a source contract must allow exactly this one stabilization and reject copies elsewhere.

Ren'Py 8.5.2 also fails to treat top-level `Testcase` declarations as lint roots. Record a real `-Mode Lint -ExtraArgs @('--all-problems')` RED that contains only the pre-existing `game/test_game.rpy` unreachable declarations, then add the empirically minimal five private no-op label roots needed across the file's explicit return/jump-separated declaration segments. One root cannot cross those terminating AST boundaries; do not add a root per declaration. The roots make test declarations reachable to lint without changing gameplay or test behavior. Do not suppress output, filter findings, weaken `--error-code`, mutate the AST, or modify the SDK. GREEN requires Lint exit zero and no `Unreachable Statements`; keep the exact RED and GREEN evidence. A source contract must require exactly those five private roots and reject extras.

- [ ] **Step 2: Add temporary jump-in anchors without duplicating continuation labels**

Do not write a second call using from _call_gov_merch2, _call_gov_build2, or _call_gov_famine2; that would create duplicate generated labels and fail compilation.

Temporarily place one uniquely named label immediately before each existing production call in chapter2.rpy:

~~~renpy
label _test_winter_fixture_merchant_call:
    call gov_merchant from _call_gov_merch2

label _test_winter_fixture_building_call:
    call gov_building(2) from _call_gov_build2

label _test_winter_fixture_famine_call:
    call gov_famine_crisis from _call_gov_famine2
~~~

Normal Chapter 2 execution simply falls through each label, so the call and continuation remain byte-for-byte the production ones.

Add three temporary drivers at the end of game/test_game.rpy. Each driver sets its deterministic old state and jumps, rather than calls, to the matching temporary anchor:

~~~renpy
label test_winter_legacy_merchant_driver:
    $ _new_run_bootstrap_done = True
    $ governance_events_seen = []
    $ gov_merchant_outcome = ""
    jump _test_winter_fixture_merchant_call

label test_winter_legacy_building_driver:
    $ _new_run_bootstrap_done = True
    $ governance_events_seen = ["merchant_negotiation"]
    $ gov_merchant_outcome = "regulated"
    jump _test_winter_fixture_building_call

label test_winter_legacy_famine_driver:
    $ _new_run_bootstrap_done = True
    $ governance_events_seen = ["merchant_negotiation"]
    $ gov_merchant_outcome = "regulated"
    $ built_granary = False
    $ famine_prevented = False
    jump _test_winter_fixture_famine_call
~~~

Do not alter game/governance.rpy.

Add two additional temporary drivers:

- test_winter_legacy_famine_success_after_driver completes the real baseline gov_famine_crisis success path, lets its original return apply famine_prevented and famine_crisis, then uses a temporary test-only branch to jump to the permanent production label ch2_preparation before saving;
- test_winter_legacy_chapter2_no_governance_driver seeds winter fields absent/defaulted, famine_prevented=False, gov_merchant_outcome="", and neither legacy event marker, then jumps to the permanent production label ch2_preparation before saving.

The latter is deliberately a compatibility-state fixture, not a claim that the current forced baseline route naturally produced that state.

- [ ] **Step 3: Generate three in-label saves and two stable post-return saves**

Add a temporary testsuite test_winter_legacy_fixture_generation that:

- starts each driver;
- runs until the first real choice screen inside gov_merchant, gov_building, or gov_famine_crisis;
- asserts the expected continuation name is in renpy.get_return_stack();
- calls renpy.save with logical slots winter-legacy-merchant-inside, winter-legacy-building-inside, winter-legacy-famine-inside, winter-legacy-famine-success-after, and winter-legacy-chapter2-no-governance;
- asserts the first three are saved at a real interaction inside the old label with the expected continuation on the stack;
- asserts the latter two are saved at permanent label ch2_preparation, never inside a temporary driver or temporary label;
- asserts Ren'Py 8.5.2 wrote the corresponding physical names with the engine suffix -LT1.save;
- records the single public verifying key returned by renpy.savetoken.get_save_token_keys(); never copy or commit the private security_keys.txt.

Run it in a fresh isolated savedir:

~~~powershell
$projectRoot = (Get-Location).Path
$fixtureSaveDir = Join-Path 'C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\work' ("renpy-winter-fixtures-{0}" -f (Get-Date -Format 'yyyyMMdd-HHmmss'))
& Tools/Run-RenPySuite.ps1 -ProjectRoot $projectRoot -Suite test_winter_legacy_fixture_generation -SaveDir $fixtureSaveDir -Expect PASSED
if ($LASTEXITCODE -ne 0) { throw 'Fixture generation wrapper failed.' }
~~~

Expected: the fresh log contains [rpytest] Status: PASSED and all five *-LT1.save files exist under the isolated savedir. Copy only those exact generated binaries, without renaming, to tests/fixtures/winter_legacy/.

- [ ] **Step 4: Record provenance and checksums**

Bind provenance to the immutable SHA printed by Task 0, not to a tag resolved at manifest-writing time:

~~~powershell
if (-not (Get-Variable baselineHead -ErrorAction SilentlyContinue) -or [string]::IsNullOrWhiteSpace([string]$baselineHead)) { throw 'Re-enter the exact Task 0 baselineHead evidence SHA.' }
if ((git rev-list -n 1 governance-winter-baseline).Trim() -ne $baselineHead) { throw 'Functional baseline tag moved before fixture provenance was recorded.' }
if ((git rev-parse HEAD).Trim() -ne $baselineHead) { throw 'Fixture generation is not running against the recorded pre-feature commit.' }
~~~

Create manifest.json with:

- baseline_commit equal to the exact recorded `$baselineHead` above;
- renpy_version equal to 8.5.2;
- savegame_suffix equal to -LT1.save;
- fixture_verifying_key equal to the public base64 DER verifying key used to sign these archives;
- one entry per save with logical_slot, physical_filename, provenance type (live continuation, real completed state, or synthetic compatibility state), source driver, permanent stop label where applicable, expected continuation or migration result, byte size, and SHA-256;
- generated_at_utc.

Create winter_asset_baseline.json containing sorted relative paths, byte sizes, and SHA-256 for every shipping file matching:

~~~text
game/images/**
game/audio/**
game/**/*.webp
game/**/*.png
game/**/*.jpg
game/**/*.ogg
game/**/*.mp3
game/**/*.wav
game/**/*.ttf
~~~

Use the existing repository's generated-artifact conventions. Generated binary files are allowed here because apply_patch cannot represent Ren'Py save archives.

- [ ] **Step 5: Remove the generation hooks, retain the test-only public key, and add a temporary smoke loader**

Remove:

- the three _test_winter_fixture_* anchors while leaving the original three production call statements in place;
- the five temporary driver labels;
- test_winter_legacy_fixture_generation.

Then add, at python early time in game/test_game.rpy, the manifest's public verifying key only when renpy.game.args.command == "test". This small guard is permanent test infrastructure and remains for every later fixture-dependent suite:

~~~renpy
python early:
    if renpy.game.args.command == "test":
        config.save_token_keys.append("<fixture_verifying_key from manifest>")
~~~

This test-only guard must exist before renpy.savetoken.init. It must contain only the public verification key, never the private security key, and does nothing in launcher or packaged gameplay. Add a temporary test_winter_legacy_fixture_smoke suite that loads by logical slot with renpy.load("winter-legacy-..."). It must drive each in-label save through its original choice and natural production return flow to permanent ch2_preparation; the smoke may not jump to the asserted destination. At arrival, inspect the real execution location and complete return stack. Verify both post-return saves load there directly with no `_call_gov_*`, `_call_re_scene_ev2`, `_call_scene_event`, temporary-driver, or temporary-anchor frame; do not trust a fixture-authored marker as proof of location.

- [ ] **Step 6: Stage, hash-check, and smoke-load all five archives in a second fresh savedir**

Ren'Py scans its save location at startup, so stage before launching it. Read the manifest, verify every repository fixture SHA-256, and copy each exact physical_filename into a new empty savedir. Do not rename it to the logical slot:

~~~powershell
$smokeSaveDir = Join-Path 'C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\work' ("renpy-winter-fixture-smoke-{0}" -f (Get-Date -Format 'yyyyMMdd-HHmmss'))
& Tools/Run-RenPySuite.ps1 -ProjectRoot (Get-Location).Path -Suite test_winter_legacy_fixture_smoke -SaveDir $smokeSaveDir -Expect PASSED -StageLegacyFixtures
if ($LASTEXITCODE -ne 0) { throw 'Legacy fixture smoke-load wrapper failed.' }
~~~

Expected: no unknown-save confirmation appears, all five cases naturally reach their expected permanent production context, every asserted post-return stack is clean, and no test times out.

- [ ] **Step 7: Remove every temporary source edit and commit the fixture infrastructure**

Remove the smoke suite with apply_patch, but retain the test-command public-key guard, the five private lint roots, the official global teardown, and the single approved resistance-choice readiness gate. Verify chapter2.rpy is exactly back at the integrated baseline, then use a focused source test to prove game/test_game.rpy contains exactly the manifest's one public key under the test-command guard, exactly the five approved private lint-reachability roots, exactly one `testsuite global` with `teardown: exit`, exactly one semantic gate for the specified existing click, and none of the five drivers, three temporary anchors, generation suite, or smoke suite:

~~~powershell
if (-not (Get-Variable baselineHead -ErrorAction SilentlyContinue) -or [string]::IsNullOrWhiteSpace([string]$baselineHead)) { throw 'Re-enter the exact Task 0 baselineHead evidence SHA.' }
if ((git rev-list -n 1 governance-winter-baseline).Trim() -ne $baselineHead) { throw 'Functional baseline tag moved before fixture cleanup.' }
git diff --exit-code $baselineHead -- game/chapter2.rpy
if ($LASTEXITCODE -ne 0) { throw 'Temporary Chapter 2 fixture anchors were not fully removed.' }
python -m unittest Tools.test_governance_winter_interlude.WinterFixtureInfrastructureTests -v
if ($LASTEXITCODE -ne 0) { throw 'Permanent fixture-key guard or temporary-hook cleanup is incorrect.' }
~~~

Expected: chapter2.rpy matches the recorded baseline SHA and the focused source test passes. The generated saves retain their live gov_* execution context and original _call_gov_* return labels; they do not need the temporary start labels after capture. The two post-return archives point only at ch2_preparation with no unrelated return frames. The public-key guard remains test-only so later isolated suites can load the signed archives without interaction; the five no-op lint roots, single global teardown, and one exact choice-readiness gate are the only additional permanent test lifecycle changes.

Verify and commit the baseline fixtures:

~~~powershell
Get-FileHash tests/fixtures/winter_legacy/*.save -Algorithm SHA256
python -m unittest discover -s Tools -p "test_*.py" -v
if ($LASTEXITCODE -ne 0) { throw 'Fixture infrastructure Python suite failed.' }
git diff --check
if ($LASTEXITCODE -ne 0) { throw 'Fixture infrastructure diff failed whitespace validation.' }
git add Tools/Run-RenPySuite.ps1 Tools/test_governance_winter_interlude.py game/test_game.rpy tests/fixtures/winter_legacy tests/fixtures/winter_asset_baseline.json
if ($LASTEXITCODE -ne 0) { throw 'Could not stage fixture infrastructure.' }
git commit -m "test: capture pre-interlude governance saves"
if ($LASTEXITCODE -ne 0) { throw 'Fixture infrastructure commit failed.' }
~~~

Expected: the five computed hashes exactly match manifest.json, Python remains green, Full is genuinely 56/56 green with a natural zero exit, lint is genuinely clean under `--error-code --all-problems`, chapter2.rpy has no diff, and game/test_game.rpy differs from governance-winter-baseline only by the guarded public-key infrastructure, five private lint roots, the official global test teardown, and the one approved resistance-choice readiness gate.

**Asset audit:** These are test-only save and JSON fixtures outside game/ and do not enter packages. No shipping art, music, SFX, animation, UI, or package-size change.

---

### Task 2: Freeze a version-only 3.10 package baseline

**Files:**

- Modify: game/options.rpy
- Modify: game/effects.rpy
- Modify: android.json
- Modify: README.txt
- Modify: Tools/test_release_contract.py
- Modify: Tools/test_verify_distributions.py
- Update: tests/screenshots/release_metadata_about.png
- Update: tests/screenshots/release_metadata_about_license.png
- Update: tests/screenshots/release_metadata_privacy.png
- Update: tests/screenshots/release_metadata_privacy_version.png

**Interfaces:**

- Consumes: the verified 3.9.2 save fixtures, the external signed 3.9.2 final3 APK, and the current release contract.
- Produces: a clean metadata-only 3.10 commit and immutable tag governance-winter-package-baseline, so baseline and final packages use identical versionName/versionCode/About/Privacy metadata.

- [ ] **Step 1: Change the release contract first and record RED**

In Tools/test_release_contract.py:

- change the approved version and docstrings from 3.9.2 to 3.10;
- replace the minimum numeric-version assertion with exact APPROVED_ANDROID_NUMERIC_VERSION=2_000_000_000;
- rename 3.9.2-specific test names/fixtures to 3.10;
- require About, Privacy, Android, and README to expose 3.10 consistently.

In Tools/test_verify_distributions.py set WINDOWS_ROOT to CourtOfShadows-3.10-win, CURRENT_CODE to 2_000_000_000, and PREVIOUS_CODE to the verified external 3.9.2 code 1_785_682_834. Keep Tools/verify_distributions.py EXPECTED_RELEASE_RPYC_COUNT at 55 in this version-only baseline because the new source module does not exist yet; Task 4 changes it to 56 in the same GREEN commit that adds the module.

Before accepting the fixed Android code, verify all three facts:

~~~powershell
$previousApk = 'E:\Projects\renpy-8.5.2-sdk\CourtOfShadows-3.9.2-6d6add0-ch3bgm-final3-dists\com.xiaoyiai.courtofshadows-3.9.2-1785682834-release.apk'
if (-not (Test-Path -LiteralPath $previousApk)) { throw 'Verified 3.9.2 comparison APK is missing.' }
if ((Get-FileHash -LiteralPath $previousApk -Algorithm SHA256).Hash -ne '67963A33D27014738A18584BE23049026596B6132B6EB95887747D0EB2667771') { throw 'Previous APK hash mismatch.' }
if ([DateTimeOffset]::UtcNow.ToUnixTimeSeconds() -ge 2000000000) { throw 'The fixed Android versionCode is no longer future-stable.' }
& 'E:\Projects\renpy-8.5.2-sdk\rapt\Sdk\build-tools\35.0.0\apksigner.bat' verify --print-certs $previousApk
if ($LASTEXITCODE -ne 0) { throw 'Previous APK signature verification failed.' }
~~~

Require exactly one signer with certificate SHA-256 5fcb5758461427026b13ecf987e86ad11e13170dc60386d42e4c2f20a93b3708. Run the focused contract and record RED caused only by still-3.9.2 production metadata.

- [ ] **Step 2: Update only shared 3.10 version metadata**

Set:

~~~text
game/options.rpy config.version and About = 3.10
game/effects.rpy privacy version = 3.10, date remains 2026年8月
android.json version = 3.10
android.json numeric_version = 2000000000
README.txt Windows version = 3.10
game/options.rpy excludes TapTap_v3.10_更新公告.md from every distribution
~~~

Do not add the feature changelog yet. game/changelog.rpy and CHANGELOG.txt are feature content and are written after the implementation is real, so the package delta includes them honestly.

- [ ] **Step 3: Refresh and inspect the four release-metadata screenshots**

Run the overwrite and comparison passes in different isolated savedirs through the fail-closed helper:

~~~powershell
$projectRoot = (Get-Location).Path
$metadataEvidence = Join-Path $projectRoot '.superpowers/sdd/metadata-3.10'
$overwriteSaveDir = Join-Path 'C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\work' ("renpy-metadata-overwrite-{0}" -f (Get-Date -Format 'yyyyMMdd-HHmmss-ffff'))
& Tools/Run-RenPySuite.ps1 -ProjectRoot $projectRoot -Suite test_release_metadata_render -SaveDir $overwriteSaveDir -Expect PASSED -ExtraArgs @('--overwrite-screenshots') -EvidenceDir $metadataEvidence
if ($LASTEXITCODE -ne 0) { throw 'Release metadata screenshot overwrite pass failed.' }
~~~

Inspect all four resulting screenshots at original detail for 3.10, clipping, and stale current-version 3.9.2 text. Do not continue until the reviewed images are correct. Then prove the approved baselines compare cleanly without overwrite:

~~~powershell
$compareSaveDir = Join-Path 'C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\work' ("renpy-metadata-compare-{0}" -f (Get-Date -Format 'yyyyMMdd-HHmmss-ffff'))
& Tools/Run-RenPySuite.ps1 -ProjectRoot $projectRoot -Suite test_release_metadata_render -SaveDir $compareSaveDir -Expect PASSED -EvidenceDir $metadataEvidence
if ($LASTEXITCODE -ne 0) { throw 'Release metadata screenshot comparison pass failed.' }
~~~

This suite writes persistent state, so never omit --savedir. Both helper runs must independently prove an immediate zero exit and exactly one fresh `[rpytest] Status: PASSED`.

- [ ] **Step 4: Refresh the font, run the release contracts GREEN, and commit**

~~~powershell
python prepare_release.py
$fontFirst = $LASTEXITCODE
if ($fontFirst -notin @(0,1)) { throw 'First font gate failed.' }
python prepare_release.py
if ($LASTEXITCODE -ne 0) { throw 'Second font gate failed.' }
python -m unittest Tools.test_release_contract Tools.test_verify_distributions -v
if ($LASTEXITCODE -ne 0) { throw '3.10 metadata contract failed.' }
git diff --check
if ($LASTEXITCODE -ne 0) { throw '3.10 metadata diff failed whitespace validation.' }
git add game/options.rpy game/effects.rpy game/msyh.ttf android.json README.txt Tools/test_release_contract.py Tools/test_verify_distributions.py tests/screenshots/release_metadata_about.png tests/screenshots/release_metadata_about_license.png tests/screenshots/release_metadata_privacy.png tests/screenshots/release_metadata_privacy_version.png
if ($LASTEXITCODE -ne 0) { throw 'Could not stage the 3.10 metadata baseline.' }
git diff --cached --check
if ($LASTEXITCODE -ne 0) { throw '3.10 metadata index failed whitespace validation.' }
git commit -m "chore: establish 3.10 release metadata"
if ($LASTEXITCODE -ne 0) { throw '3.10 metadata baseline commit failed.' }
~~~

- [ ] **Step 5: Tag the equal-metadata package baseline**

~~~powershell
$allowedPackageBaselineDiff = @(
  'Tools/Run-RenPySuite.ps1', 'Tools/test_governance_winter_interlude.py', 'game/test_game.rpy',
  'tests/fixtures/winter_asset_baseline.json',
  'docs/superpowers/plans/2026-08-08-governance-winter-interlude.md',
  'game/options.rpy', 'game/effects.rpy', 'game/msyh.ttf', 'android.json', 'README.txt',
  'Tools/test_release_contract.py', 'Tools/test_verify_distributions.py', 'Tools/verify_distributions.py',
  'tests/screenshots/release_metadata_about.png', 'tests/screenshots/release_metadata_about_license.png',
  'tests/screenshots/release_metadata_privacy.png', 'tests/screenshots/release_metadata_privacy_version.png'
)
$fixtureManifest = Get-Content -LiteralPath tests/fixtures/winter_legacy/manifest.json -Raw | ConvertFrom-Json
$functionalBaselineHead = [string]$fixtureManifest.baseline_commit
if ((git rev-list -n 1 governance-winter-baseline).Trim() -ne $functionalBaselineHead) { throw 'Functional baseline tag moved before the package baseline was frozen.' }
$actualPackageBaselineDiff = @(git diff --name-only "${functionalBaselineHead}..HEAD")
$unexpectedPackageBaselineDiff = @($actualPackageBaselineDiff | Where-Object { $_ -notin $allowedPackageBaselineDiff -and -not $_.StartsWith('tests/fixtures/winter_legacy/') })
if ($unexpectedPackageBaselineDiff.Count -ne 0) { throw "Feature code entered the version-only package baseline: $($unexpectedPackageBaselineDiff -join ', ')" }
$requiredMetadataDiff = @('game/options.rpy','game/effects.rpy','android.json','README.txt','Tools/test_release_contract.py','Tools/test_verify_distributions.py')
$missingMetadataDiff = @($requiredMetadataDiff | Where-Object { $_ -notin $actualPackageBaselineDiff })
if ($missingMetadataDiff.Count -ne 0) { throw "Required 3.10 metadata evidence is missing: $($missingMetadataDiff -join ', ')" }
$dirty = @(git status --porcelain)
if ($dirty.Count -ne 0) { throw "3.10 metadata baseline is not clean: $($dirty -join '; ')" }
$packageBaselineHead = (git rev-parse HEAD).Trim()
git show-ref --verify --quiet refs/tags/governance-winter-package-baseline
if ($LASTEXITCODE -eq 0) {
  $tagHead = (git rev-list -n 1 governance-winter-package-baseline).Trim()
  if ($tagHead -ne $packageBaselineHead) { throw 'Existing package-baseline tag does not point at HEAD.' }
}
else {
  git tag governance-winter-package-baseline $packageBaselineHead
  if ($LASTEXITCODE -ne 0) { throw 'Could not create governance-winter-package-baseline.' }
}
if ((git rev-list -n 1 governance-winter-package-baseline).Trim() -ne $packageBaselineHead) { throw 'Package-baseline tag verification failed.' }
$packageBaselineHead
~~~

Expected: the branch is clean; the tag points to the metadata-only commit; released source count remains 55 at this tag; versionName/versionCode and player-visible version metadata now match the future final package. Record the printed full `$packageBaselineHead` SHA as immutable task evidence; later packaging must re-enter and verify this SHA rather than trusting the then-current value of a movable tag.

Never return to a timestamp-sized Android versionCode after 3.10. Every later release must use a code greater than 2_000_000_000; the supported Android ceiling leaves approximately one hundred million monotonically increasing values.

**Asset audit:** No art, music, SFX, portrait, animation, or UI image is added. Four changed screenshots remain outside game/. Report any subset-font byte delta; the package-size comparison starts after this metadata/font baseline.

---

### Task 3: Add RED contracts for state, migration, and ending invariance

**Files:**

- Modify: Tools/test_governance_winter_interlude.py created in Task 1
- Modify: game/test_game.rpy
- Read: tests/fixtures/winter_legacy/manifest.json

**Interfaces:**

- Consumes: approved state enums, six outcome contracts, 12 investigation orders, legacy evidence rules, and the existing ending/battle pure functions.
- Produces: one focused RED→GREEN cycle for the state kernel. Routing, chapter-select, consumer, asset, and rendering tests are added in their own later tasks so no commit contains knowingly failing future tests.

- [ ] **Step 1: Extend the source-contract test module**

Add WinterModuleContractTests to the Task 1 test module with exactly these tests:

~~~text
test_deep_module_and_four_defaults_exist
test_state_enum_and_public_helper_signatures_exist
test_new_module_has_no_forbidden_main_state_writes
test_old_governance_label_bodies_still_exist
test_difficulty_module_never_reads_winter_state
test_fixture_key_is_public_and_enabled_only_for_test_command
test_release_rpyc_contract_accounts_for_winter_module
~~~

Use AST-free text extraction consistent with Tools/test_story_timeline.py. For the forbidden-write test, inspect only executable lines in game/governance_winter_interlude.rpy and reject assignments or calls involving the forbidden fields listed in Global Constraints. Comments must not make the test pass.

Verify the permanent test-only python early block created in Task 1; do not append the key a second time. It must contain exactly the manifest's one public verifying key, append it to config.save_token_keys only when renpy.game.args.command == "test", and run before save-token initialization. The test must prove no duplicate/public-key drift, no private key is committed, and the release package still excludes game/test_game.rpyc.

- [ ] **Step 2: Add the three state-focused Ren'Py runtime suites**

Add these suites and focused cases to game/test_game.rpy:

~~~text
test_winter_interlude_state
  status_precedence_matrix
  delegation_is_idempotent
  finalizer_compatibility_markers_are_idempotent
  invalid_values_fall_back_to_neutral
  invalid_completed_payload_never_reclassifies_as_legacy
  twelve_orders_normalize_to_six_pairs
  thirty_six_core_combinations_have_benefit_and_burden
  four_investigations_only_mitigate_their_named_cost

test_winter_interlude_legacy_migration
  unseen_plus_famine_success_becomes_legacy
  unseen_plus_merchant_outcome_becomes_legacy
  unseen_plus_famine_marker_without_success_becomes_legacy
  explicit_delegated_beats_stale_legacy_markers
  active_mid_interlude_survives_after_load
  no_evidence_outside_interlude_reads_as_neutral
  real_famine_success_after_save_loads_as_legacy
  real_chapter2_no_governance_save_loads_as_neutral

test_winter_interlude_ending_invariance
  every_core_and_delegated_result_preserves_forbidden_state
  easy_normal_hard_boundary_route_sets_are_identical
  truth_lily_borgia_sea_fall_sets_are_identical
  resistance_battle_outcomes_are_identical
~~~

At this stage, ending invariance is the state-writer layer only: parameterize every one of the 36 investigation/policy/priority combinations plus delegated, snapshot all prohibited fields, call the production finalizer, and compare:

~~~python
get_finale_route_availability(**route_kwargs)
get_finale_ending_availability(route_map, resistance_outcomes)
get_resistance_battle_outcomes(**battle_kwargs)
~~~

Use main-threshold below/at/above fixtures for easy, normal, and hard, plus independent truth, full Dark Lily, poison-duke, sea, and fall fixtures.

The end-to-end production-menu matrix is added in Task 7 and the downstream consumer-block invariance test is added in Task 9; do not claim full route invariance from this writer-layer suite alone.

- [ ] **Step 3: Run and record RED**

~~~powershell
New-Item -ItemType Directory -Path .superpowers/sdd -Force | Out-Null
$pythonRedOutput = (python -m unittest Tools.test_governance_winter_interlude -v 2>&1) -join "`n"
$pythonRedExit = $LASTEXITCODE
$pythonRedOutput | Tee-Object -FilePath .superpowers/sdd/winter-state-python-red.txt
if ($pythonRedExit -eq 0) { throw 'Winter source contracts unexpectedly passed before the module existed.' }
if ($pythonRedOutput -notmatch '(?i)governance_winter_interlude|winter.*(?:missing|not found|does not exist)') { throw 'Python RED did not identify the missing winter behavior.' }
if ($pythonRedOutput -match '(?i)SyntaxError|ImportError|ModuleNotFoundError|Traceback.*test harness') { throw 'Python RED was caused by a test/import crash rather than missing production behavior.' }
$redSaveDir = Join-Path 'C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\work' ("renpy-winter-red-{0}" -f (Get-Date -Format 'yyyyMMdd-HHmmss'))
& Tools/Run-RenPySuite.ps1 -ProjectRoot (Get-Location).Path -Suite test_winter_interlude_state -SaveDir $redSaveDir -Expect FAILED -ExpectedPattern 'winter.*(?:missing|undefined|not found)'
if ($LASTEXITCODE -ne 0) { throw 'Winter state RED evidence was not the expected behavior failure.' }
~~~

Expected: Python fails because the deep module/defaults/helpers do not exist; Ren'Py fails on the missing state helpers. Failures must be about missing winter behavior, not syntax/import errors.

- [ ] **Step 4: Preserve RED evidence and continue immediately to Task 4**

Do not commit a known-red branch. Keep only Tools/test_governance_winter_interlude.py and the three new runtime suites in the working tree, implement Task 4, and make the first commit only after all three suites are green.

**Asset audit:** No shipping assets. Tests assert the future one-background-only budget.

---

### Task 4: Implement the state kernel and idempotent old-save migration

**Files:**

- Create: game/governance_winter_interlude.rpy
- Modify: game/save_compat.rpy
- Modify: game/test_game.rpy
- Modify from Task 3 RED: Tools/test_governance_winter_interlude.py
- Modify: Tools/test_old_game_compat.py
- Modify: Tools/test_release_contract.py
- Modify: Tools/verify_distributions.py
- Modify: Tools/test_verify_distributions.py
- Update with the official launcher command: old-game/**/*.rpyc

**Interfaces:**

- Consumes: governance_events_seen, famine_prevented, gov_merchant_outcome, built_granary, first_decree, southern_outcome, and existing after_load flow.
- Produces:
  - normalize_winter_investigations(values) -> tuple
  - resolve_winter_interlude_context(raw_snapshot, projection) -> complete read-only context; projection is explicitly "internal" or "outside"
  - get_winter_context(outside=True) -> read-only context
  - apply_winter_delegation() -> None
  - finalize_winter_interlude(policy, seed_priority, investigations) -> bool
  - mark_winter_legacy() -> None
  - migrate_winter_interlude_state() -> None
  - winter_legacy_famine_success() -> bool
  - select_winter_mitigation(policy, seed_priority, investigations, immediate_inputs) -> one key or None

- [ ] **Step 1: Add only the four persistent result defaults**

Start game/governance_winter_interlude.rpy with:

~~~renpy
default winter_interlude_status = "unseen"
default winter_investigations = ()
default winter_policy = ""
default winter_seed_priority = "neutral"
~~~

Do not add separate persistent debt, reserve, recovery, mitigation, outcome, or order flags.

In the same production commit, change Tools/verify_distributions.py EXPECTED_RELEASE_RPYC_COUNT from 55 to 56. This is the active released game payload count; project-root `old-game/` remains a compiler input explicitly excluded from Windows and Android packages and is not part of this 56. Preserve the historical fact in its provenance comment: the runtime-count/path-hash contract was inherited from two independent 3.9.2 builds and is then revalidated for 3.10; do not falsely claim it was measured from two independent 3.10 builds until those final artifacts exist. Extend Tools/test_verify_distributions.py so its synthetic release contains the new game/governance_winter_interlude.rpyc path and still proves an extra or missing RPYC is rejected. This change must not land before the new source file exists and must not be deferred past this GREEN commit.

- [ ] **Step 2: Add constants and pure normalization/result helpers**

In init python define:

~~~python
WINTER_STATUSES = ("unseen", "active", "delegated", "completed", "legacy")
WINTER_INVESTIGATION_ORDER = ("market", "village", "granary", "route")
WINTER_POLICIES = ("trade", "ration", "requisition")
WINTER_SEED_PRIORITIES = ("preserve", "feed_now")
WINTER_LEGACY_EVENTS = ("famine_crisis", "merchant_negotiation")
~~~

normalize_winter_investigations must be strict:

- first require the raw input to contain exactly two values;
- require both values to be known and distinct;
- return those two values as an immutable tuple ordered by WINTER_INVESTIGATION_ORDER;
- return the empty tuple for zero, one, or three values, duplicates, unknown values, or a two-valid-plus-unknown input; never truncate a damaged payload into a valid one.

The six-entry outcome contract must be data, keyed by (policy, seed_priority), and each entry must have non-empty benefit, burden, and followup keys. The investigation-derived mitigation matches are exactly:

~~~python
("market", "trade")
("village", "preserve")
("granary", "ration")
("route", "feed_now")
~~~

No other investigation/policy-or-seed pair may return a mitigation. Task 7 adds the lower-priority compatible old-state, decree, and attribute sources to the same single-selection helper; those sources can never stack with these investigation matches.

- [ ] **Step 3: Resolve one complete raw snapshot without relying on hasattr**

resolve_winter_interlude_context accepts one immutable raw snapshot containing status, policy, seed priority, investigations, famine success, merchant outcome, and governance events, plus a required projection value of "internal" or "outside"—there is no default. It validates the fields together and returns one complete read-only context; it must never resolve status separately from the payload it validates. get_winter_context(outside=True) captures current store values once and delegates with the matching explicit projection. The resolver must obey:

1. Explicit legacy resolves to legacy.
2. Explicit delegated resolves to delegated and exposes the fixed empty/delegated/neutral payload, even if stale old markers exist.
3. Explicit completed resolves to completed only when policy is one of the three active policies, seed priority is one of the two active priorities, and the raw investigation payload is exactly two known distinct values; normalize their order.
4. Invalid completed payload resolves and migrates to delegated and must not consult famine_crisis or any other old marker afterward.
5. Active remains active for save migration; get_winter_context(outside=True) exposes it as delegated/neutral to downstream consumers. Old markers do not override active.
6. Unseen plus famine_prevented, a non-empty gov_merchant_outcome, famine_crisis, or merchant_negotiation resolves to legacy.
7. Unseen without evidence reads as delegated/neutral outside the interlude but remains unseen internally.
8. Unknown status values resolve and migrate to delegated.

Return a read-only named tuple or plain tuple from both resolver and get_winter_context. Downstream files must not receive a mutable object they can edit.

- [ ] **Step 4: Implement the two idempotent writers**

apply_winter_delegation must set:

~~~text
winter_interlude_status = delegated
winter_investigations = ()
winter_policy = delegated
winter_seed_priority = neutral
~~~

finalize_winter_interlude must return True only after validating policy, seed priority, and the original investigation payload and setting completed plus the canonical pair. For an invalid policy/seed, zero/one/three investigations, duplicate, unknown, or mixed valid/unknown payload, it must call apply_winter_delegation and return False. It must never expose an exception or partially completed result to the player. Its caller routes False through the neutral consequence and unified cleanup.

Both functions append only winter_interlude and famine_crisis to governance_events_seen, only when absent. They must not append merchant_negotiation or any other marker. Repeated calls leave exactly one of each approved marker, and explicit completed/delegated status continues to outrank those markers so it can never be reclassified as legacy. Apart from those two existing compatibility markers, the writers may change only the four winter fields and must not write old merchant/famine fields, main stats, relationships, achievements, or ending/battle fields.

mark_winter_legacy sets only winter_interlude_status="legacy". It preserves old governance fields and is used by the three explicit continuation pads.

- [ ] **Step 5: Wire migration into both existing load paths**

Call migrate_winter_interlude_state in label after_load after default variables are available and before any later-scene compatibility decisions consume governance evidence. Also call it from _compat_init_store_vars after its old fields are present.

Migration must call the resolver with projection="internal", never "outside", and write back only this mapping:

- valid completed: keep completed, canonicalize the valid pair, and retain its valid policy/seed;
- invalid completed or unknown status: persist the fixed delegated/empty/delegated/neutral payload;
- explicit delegated: persist that same fixed delegated payload;
- unseen plus real legacy evidence: persist legacy while preserving old governance fields;
- explicit legacy: preserve legacy and its old fields;
- active: leave all four in-progress fields untouched so real call-stack-local saves can resume;
- unseen without evidence: leave unseen untouched; only outside readers project it to neutral.

- [ ] **Step 5b: Refresh the repository-only old-game compiler baseline**

Adding a new `.rpy` makes the committed project-root `old-game/` tree incomplete even though that tree is excluded from player packages. Starting from the existing compatibility tree, never an empty directory, use the official Ren'Py launcher command:

~~~powershell
& 'E:\Projects\renpy-8.5.2-sdk\renpy.exe' 'E:\Projects\renpy-8.5.2-sdk\launcher' update_old_game (Get-Location).Path
if ($LASTEXITCODE -ne 0) { throw 'Official old-game refresh failed.' }
~~~

Record the before/after path, size, and SHA-256 inventory. Commit the necessary generated `old-game/**/*.rpyc` changes, including the new `old-game/governance_winter_interlude.rpyc`. Change `Tools/test_old_game_compat.py::EXPECTED_CURRENT_SCRIPT_COUNT` and `Tools/test_release_contract.py::EXPECTED_OLD_GAME_SCRIPT_COUNT` from 56 to 57. Do not change the active released payload count of 56. Run both old-game compatibility suites and preserve every protected historical generation/node guard; require the old-game tree to have exactly one matching RPYC for each of the 57 current `.rpy` sources with no missing, stale, or extra path. Re-prove release classification excludes project-root `old-game/` from Windows and Android artifacts.

The callback and label may both call it; the helper must remain idempotent. Do not copy its precedence ladder into save_compat.rpy, and never write the outside neutral projection back over active or unseen-no-evidence state.

- [ ] **Step 6: Run the state and migration suites GREEN**

~~~powershell
python -m unittest Tools.test_governance_winter_interlude.WinterModuleContractTests -v
if ($LASTEXITCODE -ne 0) { throw 'Winter module source contracts failed.' }
python -m unittest Tools.test_old_game_compat Tools.test_release_contract Tools.test_verify_distributions -v
if ($LASTEXITCODE -ne 0) { throw 'Old-game, release, or distribution contracts failed.' }
$stateSaveDir = Join-Path 'C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\work' ("renpy-winter-state-{0}" -f (Get-Date -Format 'yyyyMMdd-HHmmss-ffff'))
$migrationSaveDir = Join-Path 'C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\work' ("renpy-winter-migration-{0}" -f (Get-Date -Format 'yyyyMMdd-HHmmss-ffff'))
& Tools/Run-RenPySuite.ps1 -ProjectRoot (Get-Location).Path -Suite test_winter_interlude_state -SaveDir $stateSaveDir -Expect PASSED
if ($LASTEXITCODE -ne 0) { throw 'Winter state wrapper failed.' }
& Tools/Run-RenPySuite.ps1 -ProjectRoot (Get-Location).Path -Suite test_winter_interlude_legacy_migration -SaveDir $migrationSaveDir -Expect PASSED -StageLegacyFixtures
if ($LASTEXITCODE -ne 0) { throw 'Winter legacy migration wrapper failed.' }
~~~

Expected: both processes have their own fresh PASSED log evidence; all state, precedence, idempotency, strict-invalid-payload, 12-order, 36-contract, signature, and migration cases pass.

- [ ] **Step 7: Commit the state kernel**

~~~powershell
git add Tools/test_governance_winter_interlude.py Tools/verify_distributions.py Tools/test_verify_distributions.py Tools/test_old_game_compat.py Tools/test_release_contract.py game/governance_winter_interlude.rpy game/save_compat.rpy game/test_game.rpy old-game
git diff --cached --check
if ($LASTEXITCODE -ne 0) { throw 'State-kernel index failed whitespace validation.' }
git commit -m "feat: add winter governance state kernel"
if ($LASTEXITCODE -ne 0) { throw 'State-kernel commit failed.' }
~~~

**Asset audit:** No art, music, SFX, portrait, animation, UI, or font asset files. The refreshed project-root `old-game/` bytecode is repository-only compiler input and remains excluded from player packages. Shipping package growth is limited to the active new script/compiled bytecode and is measured later.

---

### Task 5: Route the interlude, preserve legacy continuations, and restore Chapter 2 BGM

**Files:**

- Modify: game/script.rpy
- Modify: game/chapter2.rpy
- Modify: game/governance_winter_interlude.rpy
- Modify: game/test_game.rpy
- Modify: Tools/test_governance_winter_interlude.py
- Modify: Tools/test_story_timeline.py

**Interfaces:**

- Consumes: southern_arc return, new_run_bootstrap, auto_chapter_save, snapshot_chapter_start, three old continuation names, cinematic_chapter2, play_music, clear_weather, and stop_music.
- Produces:
  - winter_interlude_start
  - winter_interlude_delegate
  - winter_interlude_cleanup(stop_temporary_music=True), an idempotent callable label that returns
  - ch2_after_winter_interlude
  - ch2_after_legacy_governance
  - explicit _call_gov_merch2, _call_gov_build2, _call_gov_famine2 pads

- [ ] **Step 1: Add routing, continuation, timeline, and audio tests; then run RED**

Add WinterRoutingContractTests to Tools/test_governance_winter_interlude.py with:

~~~text
test_mainline_routes_southern_then_winter_then_chapter2
test_chapter2_stops_calling_three_legacy_events
test_three_legacy_continuations_and_two_stable_anchors_exist_once
test_legacy_pads_are_behind_an_unconditional_fallthrough_firewall
test_every_exit_calls_the_shared_presentation_cleanup
test_chapter2_restarts_music_after_cinematic
test_one_month_card_is_not_repeated_in_chapter2_body
~~~

Add WinterInterludeTimelineTests to Tools/test_story_timeline.py requiring the winter event to occupy only the last days after the southern return, cinematic_chapter2 to own the one-month card, and chapter2_start not to repeat "一个月过去了。".

Add test_winter_interlude_continuations, test_winter_interlude_routing, and test_winter_interlude_audio to game/test_game.rpy with the cases named in the approved design.

The runtime cases must prove normal completed/delegated flow passes through both stable anchors without executing any legacy pad, while only a loaded old continuation enters its matching pad. They must also assert snow/temporary SFX are cleared on normal, delegated, invalid, and all three legacy exits.

Run:

~~~powershell
$routingRedOutput = (python -m unittest Tools.test_governance_winter_interlude.WinterRoutingContractTests -v 2>&1) -join "`n"
$routingRedExit = $LASTEXITCODE
$routingRedOutput | Tee-Object -FilePath .superpowers/sdd/winter-routing-python-red.txt
if ($routingRedExit -eq 0) { throw 'Winter routing contracts unexpectedly passed before routing changed.' }
if ($routingRedOutput -notmatch '(?i)chapter2|winter_interlude|continuation|castle_calm') { throw 'Routing RED did not identify the intended missing route/audio behavior.' }
if ($routingRedOutput -match '(?i)SyntaxError|ImportError|ModuleNotFoundError') { throw 'Routing RED was caused by a test/import crash.' }
~~~

Expected: failures identify script.rpy's direct Chapter 2 jump, three old calls, missing anchors/pads, duplicate month line, and missing post-cinematic music.

- [ ] **Step 2: Insert the normal mainline at the single approved seam**

In chapter1_end, preserve the southern call and replace only its following jump:

~~~renpy
$ auto_chapter_save("southern")
$ southern_from_mainline = True
call southern_arc from _call_southern_arc

jump winter_interlude_start
~~~

Do not put the winter entry inside southern_expansion.rpy.

- [ ] **Step 3: Add a minimal playable entry, delegation, and cleanup skeleton**

winter_interlude_start must:

1. snapshot whether this was a blank Start before calling new_run_bootstrap;
2. call new_run_bootstrap from _call_new_run_bootstrap_winter_interlude;
3. if blank, seed first_decree="", southern_outcome="delegated", built_granary=False, gov_merchant_outcome="", and no old governance evidence;
4. resolve existing state and skip re-entry when it is completed, delegated, or legacy, without overwriting the unseen hidden slot; if active arrives through this external entry, normalize it through apply_winter_delegation rather than trying to reconstruct call-stack locals;
5. only for a genuine unseen entry, call auto_chapter_save("winter_interlude") before writing active/delegated/completed;
6. show a short structural draft, then offer "亲自主持" or "交给奥尔德里克";
7. set active only after the player chooses the active path;
8. delegate through apply_winter_delegation;
9. call winter_interlude_cleanup and then jump chapter2_start for every normal, delegated, invalid, or repeat-entry exit.

winter_interlude_cleanup(stop_temporary_music=True) must call clear_weather, stop the winter looped SFX, hide characters, and stop the existing music channel only when stop_temporary_music is true. It returns to its caller and never selects the next story label. Do not register a new audio channel. It must not start Chapter 2's official BGM.

- [ ] **Step 4: Seed a direct blank Chapter 2 before its saved snapshot**

At chapter2_start:

~~~renpy
$ _chapter2_blank_entry = not _new_run_bootstrap_done
call new_run_bootstrap from _call_new_run_bootstrap_chapter2
if _chapter2_blank_entry:
    $ apply_winter_delegation()
~~~

This block must precede renpy.force_autosave, auto_chapter_save("chapter2"), and snapshot_chapter_start(). A normal completed/delegated/legacy mainline must remain unchanged.

- [ ] **Step 5: Remove only the three normal calls and add stable anchors/pads**

Preserve the Chapter 2 deepening and random event:

~~~renpy
label ch2_after_winter_interlude:
    call ch2_deep_church_midnight from _call_ch2_dcm

label ch2_after_legacy_governance:
    call re_scene_event(2) from _call_re_scene_ev2
    jump ch2_preparation
~~~

The unconditional jump is the fallthrough firewall. Place all three compatibility pads after it and before the existing ch2_preparation label so normal execution can never fall into a pad.

Define pads exactly once:

~~~renpy
label _call_gov_merch2:
    $ mark_winter_legacy()
    call winter_interlude_cleanup(False) from _call_winter_cleanup_legacy_merchant
    jump ch2_after_winter_interlude

label _call_gov_build2:
    $ mark_winter_legacy()
    call winter_interlude_cleanup(False) from _call_winter_cleanup_legacy_building
    jump ch2_after_legacy_governance

label _call_gov_famine2:
    $ mark_winter_legacy()
    call winter_interlude_cleanup(False) from _call_winter_cleanup_legacy_famine
    jump ch2_after_legacy_governance
~~~

Use the centralized migration/helper rather than erasing old outcomes. False preserves whatever non-winter BGM the resumed legacy scene already owns while still clearing snow, winter SFX, and character presentation. Do not replay gov_merchant, gov_building, gov_famine_crisis, or the new winter interlude from these pads.

- [ ] **Step 6: Restore real music after the Chapter 2 cinematic**

Immediately after:

~~~renpy
call cinematic_chapter2 from _call_cinematic_ch2
~~~

add:

~~~renpy
$ play_music("audio/music/castle_calm.ogg", fadein=2.0)
~~~

Do not use set_mood("calm") here because its same-mood fast path cannot prove the music channel is playing after the cinematic stops it. Remove the duplicate body line "一个月过去了。"; keep the cinematic's one-month title card.

- [ ] **Step 7: Run routing, continuation, timeline, and audio GREEN**

~~~powershell
python -m unittest Tools.test_governance_winter_interlude.WinterRoutingContractTests -v
if ($LASTEXITCODE -ne 0) { throw 'Winter routing source contracts failed.' }
python -m unittest Tools.test_story_timeline.WinterInterludeTimelineTests -v
if ($LASTEXITCODE -ne 0) { throw 'Winter timeline source contracts failed.' }
$continuationSaveDir = Join-Path 'C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\work' ("renpy-winter-continuation-{0}" -f (Get-Date -Format 'yyyyMMdd-HHmmss'))
$routingSaveDir = Join-Path 'C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\work' ("renpy-winter-routing-{0}" -f (Get-Date -Format 'yyyyMMdd-HHmmss'))
$audioSaveDir = Join-Path 'C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\work' ("renpy-winter-audio-{0}" -f (Get-Date -Format 'yyyyMMdd-HHmmss'))
& Tools/Run-RenPySuite.ps1 -ProjectRoot (Get-Location).Path -Suite test_winter_interlude_continuations -SaveDir $continuationSaveDir -Expect PASSED -StageLegacyFixtures
if ($LASTEXITCODE -ne 0) { throw 'Winter continuation wrapper failed.' }
& Tools/Run-RenPySuite.ps1 -ProjectRoot (Get-Location).Path -Suite test_winter_interlude_routing -SaveDir $routingSaveDir -Expect PASSED
if ($LASTEXITCODE -ne 0) { throw 'Winter routing wrapper failed.' }
& Tools/Run-RenPySuite.ps1 -ProjectRoot (Get-Location).Path -Suite test_winter_interlude_audio -SaveDir $audioSaveDir -Expect PASSED
if ($LASTEXITCODE -ne 0) { throw 'Winter audio wrapper failed.' }
~~~

Expected: each process has fresh PASSED evidence; all three real old continuation saves load, return through the explicit pads, preserve prior results, and reach the correct anchors; ordinary completed/delegated flow never executes a pad; the actual music channel reports audio/music/castle_calm.ogg after cinematic_chapter2.

- [ ] **Step 8: Commit the routing seam**

~~~powershell
git add Tools/test_governance_winter_interlude.py Tools/test_story_timeline.py game/script.rpy game/chapter2.rpy game/governance_winter_interlude.rpy game/test_game.rpy
git diff --cached --check
if ($LASTEXITCODE -ne 0) { throw 'Winter-routing index failed whitespace validation.' }
git commit -m "feat: route winter interlude before chapter two"
if ($LASTEXITCODE -ne 0) { throw 'Winter-routing commit failed.' }
~~~

**Asset audit:** Reuses existing castle_calm.ogg and weather/audio helpers. No new art, music, SFX, animation, or UI assets.

---

### Task 6: Add chapter selection, replay protection, and deterministic blank seeding

**Files:**

- Modify: game/gallery.rpy
- Modify: game/images_def.rpy
- Modify: game/governance_winter_interlude.rpy
- Modify: game/test_game.rpy

**Interfaces:**

- Consumes: chapter_list tuple signature, chapter_icons, UI_CHAPTER_ICONS, ui_icon fallback, auto_ch-<id>, persistent._skip_next_chapter_autosave, and new_run_bootstrap.
- Produces: winter_interlude entry, text icon "幕", chapter1-based unlock, auto_ch-winter_interlude replay, and deterministic blank state.

- [ ] **Step 1: Add focused source/runtime chapter-entry tests and run RED**

Add WinterChapterSelectContractTests to Tools/test_governance_winter_interlude.py with:

~~~text
test_three_parallel_chapter_lists_stay_aligned
test_winter_unlocks_from_chapter1_and_uses_text_fallback
test_blank_start_protects_auto_winter_slot
~~~

Add test_winter_interlude_chapter_select to game/test_game.rpy before running:

~~~powershell
$chapterSelectRedOutput = (python -m unittest Tools.test_governance_winter_interlude.WinterChapterSelectContractTests -v 2>&1) -join "`n"
$chapterSelectRedExit = $LASTEXITCODE
$chapterSelectRedOutput | Tee-Object -FilePath .superpowers/sdd/winter-chapter-select-python-red.txt
if ($chapterSelectRedExit -eq 0) { throw 'Winter chapter-select contracts unexpectedly passed before integration.' }
if ($chapterSelectRedOutput -notmatch '(?i)winter_interlude|chapter.*(?:list|icon|unlock|save)') { throw 'Chapter-select RED did not identify the intended missing behavior.' }
if ($chapterSelectRedOutput -match '(?i)SyntaxError|ImportError|ModuleNotFoundError') { throw 'Chapter-select RED was caused by a test/import crash.' }
~~~

Expected: winter entry, third icon-array slot, custom unlock, and autosave-protection assertions fail.

- [ ] **Step 2: Insert the entry in all three parallel lists**

Insert between southern and chapter2:

~~~python
("winter_interlude", "幕间", "第一个冬天", "winter_interlude_start", "粮价、库存与必须有人承担的缺口")
~~~

Insert "幕" at the same index in chapter_icons. Insert "ch_winter_interlude" at the same index in UI_CHAPTER_ICONS. Do not add images/ui/ch_winter_interlude.png; ui_icon must return None and fall back to the text icon.

The alignment test must compare the actual winter_interlude index and the values at that index in all three arrays; equal lengths alone are insufficient.

- [ ] **Step 3: Implement the explicit unlock and overwrite protection**

The unlocked rule must treat winter_interlude as unlocked when chapter1 is complete, independent of whether winter_interlude itself appears in persistent.chapters_completed.

Add winter_interlude to the blank-action whitelist that sets persistent._skip_next_chapter_autosave. Preserve hidden-slot naming "auto_ch-" + ch_id and FileLoad behavior.

- [ ] **Step 4: Prove deterministic blank state and real-slot preservation**

Extend test_new_run_bootstrap's parameter table with:

~~~python
("winter_interlude_start", "_call_new_run_bootstrap_winter_interlude")
~~~

The winter chapter-select suite must:

- create a sentinel auto_ch-winter_interlude save;
- start the blank entry and complete bootstrap;
- assert first_decree="", southern_outcome="delegated", built_granary=False, gov_merchant_outcome="", winter status unseen at the save point;
- assert the sentinel hidden slot was not overwritten;
- run a normal mainline entry and assert the hidden slot now contains its real first-decree and southern state.

- [ ] **Step 5: Run focused runtime GREEN**

~~~powershell
python -m unittest Tools.test_governance_winter_interlude.WinterChapterSelectContractTests -v
if ($LASTEXITCODE -ne 0) { throw 'Winter chapter-select source contracts failed.' }
$selectSaveDir = Join-Path 'C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\work' ("renpy-winter-select-{0}" -f (Get-Date -Format 'yyyyMMdd-HHmmss-ffff'))
$bootstrapSaveDir = Join-Path 'C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\work' ("renpy-winter-bootstrap-{0}" -f (Get-Date -Format 'yyyyMMdd-HHmmss-ffff'))
& Tools/Run-RenPySuite.ps1 -ProjectRoot (Get-Location).Path -Suite test_winter_interlude_chapter_select -SaveDir $selectSaveDir -Expect PASSED
if ($LASTEXITCODE -ne 0) { throw 'Winter chapter-select wrapper failed.' }
& Tools/Run-RenPySuite.ps1 -ProjectRoot (Get-Location).Path -Suite test_new_run_bootstrap -SaveDir $bootstrapSaveDir -Expect PASSED
if ($LASTEXITCODE -ne 0) { throw 'New-run bootstrap wrapper failed.' }
~~~

- [ ] **Step 6: Commit the replay integration**

~~~powershell
git add Tools/test_governance_winter_interlude.py game/gallery.rpy game/images_def.rpy game/governance_winter_interlude.rpy game/test_game.rpy
git diff --cached --check
if ($LASTEXITCODE -ne 0) { throw 'Chapter-replay index failed whitespace validation.' }
git commit -m "feat: add winter interlude chapter replay"
if ($LASTEXITCODE -ne 0) { throw 'Chapter-replay commit failed.' }
~~~

**Asset audit:** Uses the text fallback "幕". No UI image is added. No art, music, SFX, portrait, or animation change.

---

### Task 7: Build the complete structural story graph and six-result engine

**Files:**

- Modify: game/governance_winter_interlude.rpy
- Modify: game/test_game.rpy
- Modify: Tools/test_governance_winter_interlude.py

**Interfaces:**

- Consumes: state kernel, four existing backgrounds, existing characters, existing music/SFX helpers, WINTER_OUTCOME_CONTRACTS, southern salt outcome, prior decree/governance state, and soft-check attributes.
- Produces: brief/delegate gate, market/council spine, choose-two investigation graph plus low-confidence omitted reports, escalation, 3×2 decisions, a deterministic one-mitigation selector, concrete consequence slots, and unified cleanup.

- [ ] **Step 1: Make route-completeness assertions RED**

Require these labels exactly once:

~~~text
winter_interlude_brief
winter_interlude_delegate
winter_market_and_council
winter_investigation_menu
winter_choose_second_investigation
winter_investigate_market
winter_investigate_village
winter_investigate_granary
winter_investigate_route
winter_omitted_reports
winter_crisis_escalates
winter_choose_policy
winter_choose_seed_priority
winter_resolve_outcome
winter_consequence
winter_interlude_cleanup
~~~

Require no menu larger than four choices, and require the policy and seed menus to have no conditional visibility clauses. Add RED runtime suites test_winter_interlude_route_matrix and test_winter_interlude_mid_save; these must exercise production labels and menus rather than helper-only simulations.

- [ ] **Step 2: Implement the fixed spine and immediate delegate gate**

The player must receive only the short crisis brief before the active/delegate choice. The active route then enters market_and_council. Delegation goes directly to its short neutral consequence and cleanup.

Use existing scene assets at this stage:

~~~text
bg study
bg market
bg village
bg great_hall or bg council_hall
~~~

Use winter_wind, market_bustle, tension, castle_calm sequentially on the music channel; never try to overlap winter_wind and market_bustle.

- [ ] **Step 3: Implement four-choose-two without an extra persistent order flag**

Pass the first investigation key as a label parameter/call-stack local into winter_choose_second_investigation(first). After the second choice:

~~~python
winter_investigations = normalize_winter_investigations((first, second))
~~~

Each investigation label accepts whether it is first or second so immediate dialogue can differ, but no order flag survives in final state.

First menu: four items. Second menu: the remaining three. All 12 ordered paths must reach winter_omitted_reports, and A→B/B→A must save the same canonical tuple.

- [ ] **Step 4: Report both omitted locations without inventing extra state**

After the second selected investigation, winter_omitted_reports must emit one explicitly low-confidence report for each of the two unvisited locations, in canonical location order, before reaching winter_crisis_escalates. These reports communicate the missing links in the shared cause chain but grant no mitigation and add no choices or persistent fields.

Across the six unordered investigation pairs, runtime tests must prove exactly two selected scenes plus exactly two omitted reports cover all four locations once, and every route still reveals that no single actor or store of grain caused or can solve the whole shortage.

- [ ] **Step 5: Implement the two decision layers and one deterministic soft mitigation**

Policy choices, all visible:

~~~text
trade       高价购粮并担保商路
ration      开仓配给并公开账目
requisition 征用大户余粮并开具补偿凭据
~~~

Seed-priority choices, both visible:

~~~text
preserve 保留春播种粮
feed_now 先让更多人熬过眼前的冬天
~~~

Call finalize_winter_interlude only after both decisions exist. No branch calls change_stat, change_rel, unlock_achievement, modifies built_granary, or writes famine_prevented/gov_merchant_outcome.

Call select_winter_mitigation only for immediate consequence prose. It returns at most one key using this fixed priority; no source may add another mitigation after a key has been selected:

1. Matching investigation, with policy-cost matches before seed-cost matches: market+trade, then granary+ration, then village+preserve, then route+feed_now. This canonical priority makes A→B and B→A identical and resolves double matches such as market+village/trade+preserve.
2. Existing compatible governance state: gov_merchant_outcome=="regulated" with trade; southern_outcome in ("ruler", "fall") with trade; built_granary with ration. Other southern outcomes still receive salt-route difference text but no cost reduction. Salt can improve a purchase term only; it never counts as grain, changes a beneficiary/bearer, skips a decision, or resolves the shortage.
3. First decree: 治安 with trade; 民生 or 建设 with ration; 军事 with requisition.
4. Attribute soft check: wealth>=60 with trade; loyalty>=60 with ration; power>=60 with requisition.

The helper receives an immutable snapshot of these immediate inputs and returns a symbolic prose key only. Do not save it. Later chapters must never call this helper or recalculate the old winter from grown attributes, a later granary, or changed merchant state.

- [ ] **Step 6: Provide concrete consequence slots for all six contracts**

Each route must render:

- one named immediate beneficiary;
- one named immediate bearer of cost;
- one physical action or object showing the result;
- one later fixed echo key;
- at most one reduced cost selected by the fixed priority above; a selected mitigation may reduce severity but must leave a non-empty bearer and burden.

Delegated text must not claim preserved seed, intact reserves, regulated trade, broad relief, debt-free recovery, or heroic success.

- [ ] **Step 7: Add qualitative summaries without a management panel**

Before investigation, policy, and seed decisions, render one ordinary scalable line such as:

~~~text
粮价：高｜库存：不足｜民情：不安
~~~

Do not create a numerical resource HUD. Do not hard-code 10–14 px text. The line must use normal Ren'Py text scaling.

- [ ] **Step 8: Drive the production menus, real result labels, and mid-scene saves**

test_winter_interlude_route_matrix must use a dedicated test entry that reaches the production menus while test execution skips dialogue timing:

- click all 12 ordered investigation paths and prove every path reaches winter_crisis_escalates;
- prove A→B/B→A persist the same canonical tuple;
- click all six unordered pairs × three policies × two priorities, for 36 actual routes through winter_resolve_outcome and winter_consequence;
- assert the saved policy/priority/pair, beneficiary, burden, followup, at-most-one mitigation, forbidden-state snapshot, and unified cleanup target;
- compare the nine ending availability set and resistance inputs before entry and after each complete route and delegation.

test_winter_interlude_mid_save must create and reload real saves at two production interactions:

- the second-investigation menu, then choose the second location and prove the call-stack local first survived;
- the seed-priority menu, then choose a seed priority and prove the local policy survived.

After each load status remains active until one successful finalization, then becomes completed exactly once, cleans presentation, and reaches Chapter 2. The synthetic active-state test from Task 4 does not substitute for these call-stack-local saves.

- [ ] **Step 9: Run all structural route cases GREEN**

```powershell
$gateHost = Join-Path ([Environment]::SystemDirectory) 'WindowsPowerShell\v1.0\powershell.exe'
$winterGate = (Resolve-Path -LiteralPath Tools/Run-WinterInterludeGate.ps1 -ErrorAction Stop).Path
& $gateHost -NoLogo -NoProfile -NonInteractive -ExecutionPolicy Bypass -File $winterGate -Gate Structural -ProjectRoot (Get-Location).Path
if ($LASTEXITCODE -ne 0) { throw 'Winter Structural gate failed.' }
```

Expected: every command exits zero with fresh PASSED evidence; 12 real ordered menus, six omitted-report combinations, 36 real result routes, all double-mitigation candidates, southern salt limits, delegated, corrupted-active fallback, two mid-save loads, one-shot routing, forbidden-state snapshots, ending sets, and resistance outcomes all pass.

- [ ] **Step 10: Commit the structural graph**

~~~powershell
git add game/governance_winter_interlude.rpy game/test_game.rpy Tools/test_governance_winter_interlude.py
git diff --cached --check
if ($LASTEXITCODE -ne 0) { throw 'Winter story-graph index failed whitespace validation.' }
git commit -m "feat: implement winter governance decision graph"
if ($LASTEXITCODE -ne 0) { throw 'Winter story-graph commit failed.' }
~~~

**Asset audit:** This structural pass reuses existing backgrounds and all existing audio/portraits/animation. The dedicated granary background is still pending and must be visibly marked as the only temporary art mismatch until Task 10.

---

### Task 7.5: Replace Markdown command interpretation with one executable winter gate

**Files:**

- Create: Tools/Run-WinterInterludeGate.ps1
- Create: Tools/test_winter_interlude_gate.py
- Modify: Tools/test_governance_winter_interlude.py
- Modify: docs/superpowers/plans/2026-08-08-governance-winter-interlude.md

**Implementation plan:** docs/superpowers/plans/2026-08-09-winter-interlude-executable-gates.md

Markdown is documentation; executable proof comes from Tools/test_winter_interlude_gate.py. Implement and verify the public Structural and Narrative entrypoints, remove the handwritten Markdown/PowerShell interpreter, and keep this range limited to the four files above.

Commit with `refactor: execute winter interlude gates from scripts`.

**Asset audit:** Tooling and documentation only; no art, music, SFX, portrait, animation, UI, font, old-game, shipping source, or package-size change.

---

### Task 8: Author and approve a dedicated winter-interlude narrative delivery plan

**Status:** blocked on a separate implementation plan.

Do not implement Task 8 from this umbrella plan. Do not edit prose, tests, scanners, the capability checker, the font, or any shipping file until the dedicated plan below exists and has passed fresh Spec and Standards review with `Critical 0 / Important 0 — READY`.

- [ ] **Step 1: Create and approve the dedicated Task 8 delivery plan**

After Task 7.5 is committed and its real Structural proof is current, start a new planning session with `superpowers:writing-plans`. Create exactly this tracked plan:

`docs/superpowers/plans/2026-08-09-winter-interlude-narrative-delivery.md`

The dedicated plan, not this umbrella task, owns every Task 8 implementation edit. It must contain complete copy-pastable tests and production bodies, with no prose such as “implement”, “add contracts”, metavariables, omitted helper bodies, or multi-tool GREEN steps. It must split at least these independent RED-to-GREEN slices:

1. the real `Tools/check_winter_narrative_capabilities.py` producer and its dedicated tests;
2. canon JSON output and all four blocking categories plus trigger-only nonblocking behavior;
3. portrait JSON output without repository-report writes;
4. narration-overlap JSON output;
5. show-before-prevention scanning and its negative mutation;
6. nested-quote scoped JSON output;
7. capability-to-tool linkage mutations proving that breaking each scanner flag, schema, negative mutation, show coverage, or scene-contract probe makes the real checker publish that capability as false, `ready=false`, and exit nonzero rather than hard-coding Boolean success;
8. one fresh Opus session, raw-output presentation, explicit user approval, atomic integration, and an immediate real Narrative Batch gate for each individual scene;
9. final-only length, reuse-ratio, semantic, placeholder-removal, and final-copy contracts, written with the then-approved literal prose facts before one real Narrative Final transition;
10. exact staging, current-HEAD evidence, asset/package audit, and fresh Spec plus Standards review.

**Machine-JSON gate contract:**

`WINTER_GATE_STRUCTURED_OUTPUT_HANDLE` is the sole gate-mode write authority for all six machine-JSON producers. In gate mode a producer must not open, create, replace, reopen, or fall back to `--output` by path. Standalone mode exists only when the handle environment variable is absent; it uses `CREATE_NEW` and never overwrites. Gate evidence is limited to 1,048,576 UTF-8 bytes, 1,048,576 UTF-16 characters, depth 64, and number-token length 128; it uses RFC 8259 lexemes, strings, and surrogate pairs, decoded object keys are unique by `Ordinal`, and it reports `strict_json:<reason> at UTF-16 offset N.` before `ConvertFrom-Json`. Portrait output requires exactly one registered direct parent using `OrdinalIgnoreCase`; prefix/`StartsWith` matching is forbidden and `--output-dir` remains forbidden. The dedicated plan must include a per-producer handle-linkage, path-reopen, and path-fallback mutation.

The six producers are
`Tools/check_winter_narrative_capabilities.py`, `Tools/scan_canon.py`,
`scan_missing_portraits.py`, `scan_narration_overlap.py`,
`Tools/scan_show_before_prevention.py`, and
`Tools/scan_nested_quotes.py`. Their dedicated-plan slices must implement and
test all of the following together with their producer-specific schemas:

- When the environment variable is present, parse it as a positive decimal
  handle, resolve its final path, require the normalized result to equal the
  exact `--output` path with `OrdinalIgnoreCase`, clear inheritance, seek to
  zero, truncate, write UTF-8 without BOM, durably flush, and close the child
  duplicate. Missing, malformed, mismatched, or unwritable gate handles must
  make the producer exit nonzero without a valid evidence document.
- A Job-contained producer never has a path fallback. Only a process with no
  structured-output environment variable is standalone; its path mode uses
  exclusive `CREATE_NEW`, never overwrites, and never replaces an existing
  leaf.
- Before launch the gate creates the exact direct child with `CREATE_NEW` and
  share mode zero, writes a random marker, and retains both the owner handle
  and exact direct-parent guard. A JSON child receives only a duplicate as the
  fourth inherited handle; a non-JSON child retains the exact stdin/stdout/
  stderr three-handle list. The child environment always scrubs an attacker-
  supplied structured-output value before injecting the owned duplicate.
- The owner reservation remains live through Job `ActiveProcesses == 0`,
  owner-handle freeze/read, result evaluation, and success or failure summary
  publication, and is released only by the gate's outer `finally`. The gate
  reads only through that owner handle; an unchanged marker is missing
  evidence, not a valid empty document.
- Producers use strict serializers that cannot emit BOM, NaN, Infinity,
  duplicate keys, invalid escapes, or invalid surrogate sequences. They need
  not copy the gate's parser, but every emitted document must pass the same
  byte/character/depth/number/RFC profile before its existing exact schema and
  postcondition checks.
- For each producer, the dedicated tests must independently mutate inherited
  handle linkage, path reopen, and path fallback. A broken scanner producer
  must make its corresponding capability false, `ready=false`, and the real
  checker exit nonzero; a broken capability producer must exit nonzero without
  valid evidence. Every mutation must also make the real Narrative gate fail.

Each slice must name the exact files and insertion points, include the complete test fixture and minimal production patch, run one behavior-specific RED that fails for the intended missing behavior, run its focused GREEN with an immediate `$LASTEXITCODE` guard, and preserve prior GREEN slices. The dedicated plan must account for these owned paths:

- `game/governance_winter_interlude.rpy`
- `game/test_game.rpy`
- `game/msyh.ttf`
- `docs/development/winter-interlude-content-ledger.md`
- `Tools/check_winter_narrative_capabilities.py`
- `Tools/scan_show_before_prevention.py`
- `Tools/test_winter_narrative_capabilities.py`
- `Tools/scan_canon.py`
- `scan_missing_portraits.py`
- `scan_narration_overlap.py`
- `Tools/scan_nested_quotes.py`
- `Tools/test_governance_winter_interlude.py`
- `Tools/test_winter_interlude_gate.py`
- `Tools/Run-WinterInterludeGate.ps1`

The public-gate calls that the dedicated plan must place after each approved atomic scene and after the final-only transition are exactly:

```powershell
$gateHost = Join-Path ([Environment]::SystemDirectory) 'WindowsPowerShell\v1.0\powershell.exe'
$winterGate = (Resolve-Path -LiteralPath Tools/Run-WinterInterludeGate.ps1 -ErrorAction Stop).Path
& $gateHost -NoLogo -NoProfile -NonInteractive -ExecutionPolicy Bypass -File $winterGate -Gate Narrative -NarrativePhase Batch -ProjectRoot (Get-Location).Path
if ($LASTEXITCODE -ne 0) { throw 'Winter Narrative Batch gate failed.' }
```

```powershell
$gateHost = Join-Path ([Environment]::SystemDirectory) 'WindowsPowerShell\v1.0\powershell.exe'
$winterGate = (Resolve-Path -LiteralPath Tools/Run-WinterInterludeGate.ps1 -ErrorAction Stop).Path
& $gateHost -NoLogo -NoProfile -NonInteractive -ExecutionPolicy Bypass -File $winterGate -Gate Narrative -NarrativePhase Final -ProjectRoot (Get-Location).Path
if ($LASTEXITCODE -ne 0) { throw 'Winter Narrative Final gate failed.' }
```

These two fences document the required public interface for the future dedicated plan; they are not Task 8 execution authorization in this umbrella plan.

Task 7's six player-visible semantic expectations are a coordinated test-owned interface: four omitted-report sentences, one shared-cause sentence, and one neutral-delegation sentence. A Task 8 final-prose change may update them only after the matching fresh scene-specific claude-opus-4-6 raw output has been shown to and approved by the user. In the same atomic commit, update game/governance_winter_interlude.rpy and the independent expectations in Tools/test_governance_winter_interlude.py and game/test_game.rpy. Never derive either test expectation from production text and never replace the visible checks with hidden-marker-only assertions. Preserve all six opposite-semantic mutation cases and real _history verification, then rerun the focused source contract and the production route matrix including delegation. Without explicit user approval, none of the six production sentences or their two test-owned expectations may change.

If the dedicated plan is absent, contains placeholders, lacks any required
per-tool or per-scene loop, omits any inherited-handle, no-path-fallback,
strict-profile, exact portrait-parent, or per-producer mutation contract, lacks
the real checker linkage mutations, or has not received both READY verdicts,
stop at this checkpoint. Do not infer permission to implement Task 8 from the
high-level requirements above.

**Asset audit:** Planning only. Art, music, SFX, portrait, animation, UI, font, old-game, shipping source, and package size remain unchanged until the separately approved delivery plan is executed.

---

### Task 9: Migrate all merchant/famine consumers and add four narrative echoes

**Files:**

- Modify: game/governance_winter_interlude.rpy
- Modify: game/chapter2.rpy
- Modify: game/interludes.rpy
- Modify: game/chapter5.rpy
- Modify: game/chapter5_expansion.rpy
- Modify: game/endings_expansion.rpy
- Modify: game/test_game.rpy
- Modify: Tools/test_governance_winter_interlude.py
- Regenerate and commit if changed: missing_portraits_B.txt, the repository's tracked portrait-scan report
- Create: tests/fixtures/winter_ch5_bonus_baseline.json with normalized hashes of every existing ch5_exp_defender_bonus writer and enclosing guard

**Interfaces:**

- Consumes: get_winter_context(outside=True), saved winter fields, legacy gov_merchant_outcome/famine_prevented, built_granary, and approved Opus batch 6.
- Produces: one centralized consumer vocabulary for completed/delegated/legacy/neutral plus winter-aware Chapter 2, road conflict, supplies, defense, and People's Lord text.

- [ ] **Step 1: Make the consumer contract RED**

Add WinterConsumerContractTests to Tools/test_governance_winter_interlude.py with:

~~~text
test_all_new_consumers_use_central_winter_context
test_new_consumer_blocks_have_no_forbidden_writes
test_legacy_famine_text_is_guarded_by_effective_legacy_state
test_later_stats_and_granary_cannot_recalculate_saved_winter
test_every_chapter_five_current_stock_claim_uses_winter_context
test_chapter_five_recovery_echo_distinguishes_seed_priority
test_chapter_five_bonus_writes_are_unchanged
test_difficulty_module_never_reads_winter_state
~~~

Require no direct new-flow condition on gov_merchant_outcome, famine_prevented, or merchant_negotiation outside game/governance.rpy and the centralized compatibility helpers. Explicitly cover:

~~~text
chapter2.rpy merchant-alliance dialogue
chapter2.rpy Harrenhall conference pressure and Karl negotiation framing
interludes.rpy merchant-road conflict and release
chapter5.rpy supplies report
chapter5.rpy refugee-arrival reserve-duration claim
chapter5_expansion.rpy defense/governance report
endings_expansion.rpy two legacy famine echoes
endings_expansion.rpy People's Lord five-year epilogue
~~~

Allow the original legacy label bodies in governance.rpy to keep reading their old variables. Implement each newly inserted downstream echo as a narrow production label that contains dialogue/presentation only, returns to one uniquely named `call ... from` at the existing story seam, and has stable source comments. These callable labels are the sole units extracted by the forbidden-write test; reject any assignment/call touching stats, relationships, alliances, endings, battle inputs, achievements, built_granary, or ch5_exp_defender_bonus. Do not wrap an existing Chapter 5 bonus writer inside a new echo label.

Add test_winter_interlude_downstream_invariance to game/test_game.rpy. A test-only dispatcher calls the exact production echo labels—never duplicated test prose—for six completed results, delegated, neutral, and representative legacy states. It snapshots forbidden fields and the nine-ending/resistance outputs, executes only that echo label, and proves they are unchanged.

Before editing Chapter 5, read `baseline_commit` from tests/fixtures/winter_legacy/manifest.json, assert governance-winter-baseline still equals that SHA, and create winter_ch5_bonus_baseline.json from that exact commit with the normalized source, guard expression, order, and SHA-256 for every ch5_exp_defender_bonus writer. test_chapter_five_bonus_writes_are_unchanged must compare the post-edit writers and enclosing guards against this fixture exactly, allowing only line-number movement. This source contract—not the read-only echo runtime snapshot—proves the existing built_granary-controlled bonus still executes unchanged.

- [ ] **Step 2: Add centralized read-only consumer helpers**

Provide helpers with fixed meanings:

~~~text
winter_merchant_echo()          completed policy / delegated neutral / legacy old outcome / neutral
winter_harrenhall_echo()        policy-specific attack, courtship, or pledge request; read-only
winter_karl_terms_echo()        policy-specific framing of the unchanged Karl offer; read-only
winter_reserve_echo()           saved policy only; never recalculated from later stats
winter_recovery_echo()          saved seed priority only
winter_legacy_famine_success()  true only for effective legacy plus famine_prevented
winter_people_epilogue_echo()   six results, delegated neutral, legacy old success, or neutral
~~~

Later changes to attributes or built_granary must not change the saved winter route. built_granary may still affect its own legacy construction prose and existing numeric bonus.

- [ ] **Step 3: Add the required Harrenhall pressure and migrate both Chapter 2 merchant scenes**

At the Harrenhall political meeting, add one short policy-derived interaction before the existing decision point:

- trade: merchants use the winter credit or reopened route to court the player and request a concrete future pledge;
- ration: a noble or merchant attacks the public-account/open-granary precedent while another faction offers support at a political price;
- requisition: nobles press the compensation/property claim and demand acknowledgement of the outstanding obligation;
- delegated/neutral: ordinary lobbying without invented leverage;
- legacy: preserve the old merchant/governance knowledge actually present in the save.

This is a read-only political echo. Every existing conference choice, condition, jump, stat/relationship write, and outcome remains exactly visible and unchanged.

In the later merchant-alliance recognition dialogue, completed routes recognize the network through their winter dealings with policy-specific wording. Delegated/neutral receives no special inside knowledge. Legacy preserves the old merchant_negotiation behavior.

At Karl's existing iron-and-information offer, use winter_karl_terms_echo() only to change how he frames the same proposal: he may call in winter credit, exploit the public-account dispute, or raise compensation claims. Do not change any quoted price, wealth/relationship delta, evidence grant, condition, menu visibility, or branch target. merchant_deal remains the later Karl route and is never pre-set or inferred from winter_policy.

Add source snapshots of the Harrenhall and Karl menu labels before editing and assert their option texts/conditions, state writes, and targets are byte-for-byte unchanged after the inserted read-only echoes.

- [ ] **Step 4: Migrate the Chapter 4-to-5 merchant-road conflict**

Replace the two direct reject checks with the centralized echo:

- completed trade: the merchant favor is called in;
- completed requisition: merchants and nobles press compensation/property claims;
- completed ration: no blockade fiction; use the saved public-account dispute;
- delegated/neutral: retain the ordinary local conflict;
- legacy reject: preserve the old blockade and return text.

No branch changes stats, enemy numbers, alliances, or battle setup.

- [ ] **Step 5: Make every Chapter 5 current-stock claim winter-aware without changing bonuses or construction orders**

Audit every direct built_granary read in chapter5.rpy and chapter5_expansion.rpy before editing. Classify each occurrence as one of: current stock/duration prose, future construction/refill order, or existing numeric bonus guard. The source test must reject every unclassified occurrence and every current-stock claim that does not first combine built_granary with winter_reserve_echo.

At minimum, migrate both existing chapter5.rpy claims: the early refugee-arrival exchange that currently says the reserve can last roughly two months, and the later military-supplies report that claims three months of full grain. A ration route may have a useful granary structure but tighter stock; requisition may preserve more castle stock; trade may have supply but a merchant claim.

The later military-supplies/defense exchange and the chapter5_expansion defense/governance report must also consume winter_recovery_echo() from the saved seed priority: preserve states that spring sowing and postwar recovery are steadier; feed_now states that more grain was consumed during the crisis and recovery will be slower. For ration/feed_now, the same Chapter 5 scene must carry both the tighter-reserve pressure from winter_reserve_echo() and the slower-recovery pressure from winter_recovery_echo(); neither may overwrite or mask the other. Runtime consumer tests compare preserve and feed_now under the same policy and require different recovery text classes, then mutate later attributes and built_granary and prove both saved echoes remain unchanged.

The later command to refill/prepare the granary describes a future action, not current inventory; keep the order and its effects unchanged and record it in the explicit non-stock allowlist rather than rewriting it as a winter result.

In chapter5_expansion.rpy, rewrite the built_granary prose by context but leave every existing ch5_exp_defender_bonus increment exactly unchanged. Do not add a winter bonus or penalty.

- [ ] **Step 6: Guard every old heroic famine line**

Replace the three raw famine_prevented consumers with winter_legacy_famine_success(). A new completed/delegated route must never display "没有饿死一个人"; a real legacy success must retain the old result.

- [ ] **Step 7: Add one concrete People's Lord five-year echo**

After RC integration, anchor inside the realistic People's Lord epilogue near the existing public granary/bread material, not the obsolete master wording.

Each of the six saved results must show one concrete long-term consequence:

- trade/preserve: roads and spring sowing recover, while the merchant claim remains visible;
- trade/feed_now: broad immediate supply, slower field recovery;
- ration/preserve: public accounts remembered, castle reserve cost acknowledged;
- ration/feed_now: more people survived, both reserve and recovery scars remain;
- requisition/preserve: smallholders and sowing protected, compensation debt still paid;
- requisition/feed_now: widest relief, merchant/noble pressure and spring gap both remain.

Delegated is modest and neutral. Legacy success keeps its old memory. No version claims unconditional prosperity.

- [ ] **Step 8: Re-run consumer and invariance gates**

~~~powershell
New-Item -ItemType Directory -Path .superpowers/sdd -Force | Out-Null
python -m unittest Tools.test_governance_winter_interlude.WinterConsumerContractTests -v
if ($LASTEXITCODE -ne 0) { throw 'Winter consumer source contracts failed.' }
python Tools/scan_canon.py
if ($LASTEXITCODE -ne 0) { throw 'Canon scanner crashed on downstream echoes.' }
foreach ($copyFile in @('game/chapter2.rpy','game/interludes.rpy','game/chapter5.rpy','game/chapter5_expansion.rpy','game/endings_expansion.rpy')) {
  python Tools/scan_ai_smell.py $copyFile
  if ($LASTEXITCODE -ne 0) { throw "AI-smell scan failed: $copyFile" }
}
python Tools/scan_nested_quotes.py
if ($LASTEXITCODE -ne 0) { throw 'Nested-quote scan found an issue in downstream copy.' }
python scan_missing_portraits.py
if ($LASTEXITCODE -ne 0) { throw 'Portrait scanner crashed on downstream echoes.' }
python scan_narration_overlap.py chapter2.rpy interludes.rpy chapter5.rpy chapter5_expansion.rpy endings_expansion.rpy | Tee-Object -FilePath .superpowers/sdd/winter-downstream-narration-overlap.txt
if ($LASTEXITCODE -ne 0) { throw 'Narration-overlap scanner crashed on downstream echoes.' }
python prepare_release.py
$fontFirst = $LASTEXITCODE
if ($fontFirst -notin @(0,1)) { throw 'First downstream font gate failed.' }
python prepare_release.py
if ($LASTEXITCODE -ne 0) { throw 'Font does not cover downstream echo text.' }
$endingSaveDir = Join-Path 'C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\work' ("renpy-winter-ending-{0}" -f (Get-Date -Format 'yyyyMMdd-HHmmss'))
$downstreamSaveDir = Join-Path 'C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\work' ("renpy-winter-downstream-{0}" -f (Get-Date -Format 'yyyyMMdd-HHmmss'))
$legacyEchoSaveDir = Join-Path 'C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\work' ("renpy-winter-legacy-echo-{0}" -f (Get-Date -Format 'yyyyMMdd-HHmmss'))
& Tools/Run-RenPySuite.ps1 -ProjectRoot (Get-Location).Path -Suite test_winter_interlude_route_matrix -SaveDir $endingSaveDir -Expect PASSED
if ($LASTEXITCODE -ne 0) { throw 'End-to-end winter route wrapper failed after consumer integration.' }
& Tools/Run-RenPySuite.ps1 -ProjectRoot (Get-Location).Path -Suite test_winter_interlude_downstream_invariance -SaveDir $downstreamSaveDir -Expect PASSED
if ($LASTEXITCODE -ne 0) { throw 'Winter downstream wrapper failed.' }
& Tools/Run-RenPySuite.ps1 -ProjectRoot (Get-Location).Path -Suite test_winter_interlude_legacy_migration -SaveDir $legacyEchoSaveDir -Expect PASSED -StageLegacyFixtures
if ($LASTEXITCODE -ne 0) { throw 'Winter legacy echo wrapper failed.' }
~~~

Expected: every runtime command has fresh PASSED evidence; every real result and downstream block leaves conference/Karl option availability, their original numeric writes, ending routes, resistance outcomes, and prohibited fields bit-for-bit identical; all legacy and new echoes select the expected text class. The explicit narration command covers every changed downstream file. Canon, portrait, narration-overlap, and AI-smell findings are manually classified with zero actionable finding left; AI-smell findings are reviewed only for local repetition and never bulk-rewritten. Because scan_missing_portraits.py rewrites tracked missing_portraits_B.txt, inspect any diff: fix new findings first, and commit the reproducible report only when the remaining change is an expected line-number/source refresh.

- [ ] **Step 9: Commit downstream echoes**

~~~powershell
git add game/governance_winter_interlude.rpy game/chapter2.rpy game/interludes.rpy game/chapter5.rpy game/chapter5_expansion.rpy game/endings_expansion.rpy game/test_game.rpy game/msyh.ttf Tools/test_governance_winter_interlude.py tests/fixtures/winter_ch5_bonus_baseline.json missing_portraits_B.txt
git diff --cached --check
if ($LASTEXITCODE -ne 0) { throw 'Downstream-echo index failed whitespace validation.' }
git commit -m "feat: echo winter policy without changing endings"
if ($LASTEXITCODE -ne 0) { throw 'Downstream-echo commit failed.' }
~~~

**Asset audit:** Reuses existing backgrounds, portraits, music, SFX, and animation. No media increase; prepare_release.py handles the downstream prose's exact subset-font byte delta in this task.

---

### Task 10: Generate, register, and budget the one required granary background

**Files:**

- Create: game/images/bg_winter_granary.webp
- Modify: game/images_def.rpy
- Modify: game/gallery.rpy
- Modify: game/governance_winter_interlude.rpy
- Modify: Tools/test_governance_winter_interlude.py
- Modify: game/test_game.rpy

**Interfaces:**

- Consumes: imagegen skill, existing 1280×720 background presentation, bg village/market/study/great_hall visual language, and gallery_images.
- Produces: one WebP background, image names bg winter_granary and bg_winter_granary, one gallery record, first-use unlock, and dynamic gallery rows.

- [ ] **Step 1: Run the asset contract RED**

Add WinterAssetContractTests to Tools/test_governance_winter_interlude.py with:

~~~text
test_single_new_background_is_webp_1280x720_and_under_budget
test_background_is_defined_used_and_registered_once
test_gallery_rows_are_computed_from_gallery_length
test_no_new_audio_portrait_animation_or_ui_asset
~~~

~~~powershell
New-Item -ItemType Directory -Path .superpowers/sdd -Force | Out-Null
$assetRedOutput = (python -m unittest Tools.test_governance_winter_interlude.WinterAssetContractTests -v 2>&1) -join "`n"
$assetRedExit = $LASTEXITCODE
$assetRedOutput | Tee-Object -FilePath .superpowers/sdd/winter-asset-python-red.txt
if ($assetRedExit -eq 0) { throw 'Winter asset contracts unexpectedly passed before the asset existed.' }
if ($assetRedOutput -notmatch '(?i)bg_winter_granary|background|gallery|1280|webp') { throw 'Asset RED did not identify the intended missing background integration.' }
if ($assetRedOutput -match '(?i)SyntaxError|ImportError|ModuleNotFoundError') { throw 'Asset RED was caused by a test/import crash.' }
~~~

Expected: missing file, definition, gallery record, use, and dynamic-grid assertions fail.

- [ ] **Step 2: Generate the source image with the imagegen skill**

Read the imagegen skill first. Generate a winter castle granary interior that matches the game's painted medieval backgrounds:

- wide 16:9 first-person scene;
- damp grain sacks, opened bins, old tally boards, frost/cold light near the door;
- enough foreground and side negative space for dialogue UI and portraits;
- no readable text;
- no named characters, faces, logos, frame, title, or UI;
- no modern objects;
- no snow falling indoors.

Inspect the source at original detail before conversion. Reject visible anatomy/text artifacts or a composition that makes the inventory inspection implausible. After the user approves one exact generated file, retain the absolute local path returned by image generation as the PowerShell variable `$approvedSource` in the task evidence; do not infer it from a directory or choose the newest image.

- [ ] **Step 3: Convert only the approved source to the shipping WebP**

Keep source/intermediate files outside game/. Resolve and inspect the exact approved file, reject a missing/non-file path, and fail if the shipping target already exists before this task. Convert to a uniquely named temporary WebP first; never point ffmpeg -y directly at the shipping path:

~~~powershell
if (-not (Get-Variable approvedSource -ErrorAction SilentlyContinue) -or [string]::IsNullOrWhiteSpace([string]$approvedSource)) { throw 'No exact user-approved source path was recorded.' }
$approvedSourceResolved = (Resolve-Path -LiteralPath $approvedSource -ErrorAction Stop).Path
if (-not (Test-Path -LiteralPath $approvedSourceResolved -PathType Leaf)) { throw 'Approved source is not a file.' }
$shippingTarget = Join-Path (Get-Location).Path 'game/images/bg_winter_granary.webp'
if (Test-Path -LiteralPath $shippingTarget) { throw 'Shipping target already exists before the asset task.' }
$tempWebp = Join-Path 'C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\work' ("winter-granary-{0}.webp" -f (Get-Date -Format 'yyyyMMdd-HHmmss-ffff'))
ffmpeg -hide_banner -loglevel error -y -i $approvedSourceResolved -vf "scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720" -frames:v 1 -c:v libwebp -quality 86 -compression_level 6 $tempWebp
if ($LASTEXITCODE -ne 0 -or -not (Test-Path -LiteralPath $tempWebp)) { throw 'Granary WebP conversion failed.' }
~~~

Use Pillow to assert the temporary file is WebP and exactly 1280×720, and PowerShell to enforce the byte limit:

~~~powershell
python -c "from PIL import Image; import sys; p=sys.argv[1]; im=Image.open(p); im.load(); assert im.format == 'WEBP', im.format; assert im.size == (1280,720), im.size" $tempWebp
if ($LASTEXITCODE -ne 0) { throw 'Temporary granary image failed Pillow format/dimension validation.' }
if ((Get-Item -LiteralPath $tempWebp).Length -gt 1258291) { throw 'Temporary granary image exceeds 1.2 MiB; reconvert the same approved source at the next allowed quality.' }
~~~

If it exceeds the limit, retry that same explicit temporary target at quality 82, then 78, and rerun both assertions after each conversion. Do not lower resolution. Inspect the final temporary image at original detail, then copy the approved binary once to the still-absent shipping target and prove byte identity:

~~~powershell
if (Test-Path -LiteralPath $shippingTarget) { throw 'Shipping target appeared before the approved copy.' }
$sourceWebpHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $tempWebp).Hash
Copy-Item -LiteralPath $tempWebp -Destination $shippingTarget -ErrorAction Stop
if (-not (Test-Path -LiteralPath $shippingTarget -PathType Leaf)) { throw 'Approved WebP copy failed.' }
if ((Get-FileHash -Algorithm SHA256 -LiteralPath $shippingTarget).Hash -ne $sourceWebpHash) { throw 'Shipping WebP differs from the approved temporary file.' }
~~~

Generated binary copying is the permitted exception to text-only apply_patch editing. The final file must remain visually clean at original detail.

- [ ] **Step 4: Register definitions, story use, gallery, and dynamic rows**

Add:

~~~renpy
image bg winter_granary = Transform("images/bg_winter_granary.webp", size=(1280, 720), fit="cover")
image bg_winter_granary = Transform("images/bg_winter_granary.webp", size=(1280, 720), fit="cover")
~~~

Use it for granary investigation and the shortage escalation, and unlock bg_winter_granary on first display.

Add one gallery_images entry named "冬季粮仓". Replace fixed grid 4 11 and its 4*11 filler arithmetic with:

~~~python
_gallery_columns = 4
_gallery_rows = (len(gallery_images) + _gallery_columns - 1) // _gallery_columns
~~~

Both the grid and filler count must use those values.

- [ ] **Step 5: Prove the asset and no-extra-asset contracts**

~~~powershell
python -m unittest Tools.test_governance_winter_interlude.WinterAssetContractTests -v
if ($LASTEXITCODE -ne 0) { throw 'Winter asset contracts failed after integration.' }
Get-Item game/images/bg_winter_granary.webp | Select-Object FullName,Length
$fixtureManifest = Get-Content -LiteralPath tests/fixtures/winter_legacy/manifest.json -Raw | ConvertFrom-Json
$functionalBaselineHead = [string]$fixtureManifest.baseline_commit
if ((git rev-list -n 1 governance-winter-baseline).Trim() -ne $functionalBaselineHead) { throw 'Functional baseline tag moved before the asset inventory check.' }
git diff "${functionalBaselineHead}..HEAD" --name-only
git diff --name-only
git ls-files --others --exclude-standard
~~~

Expected:

- format WebP;
- dimensions 1280×720;
- size at most 1.2 MiB;
- exactly one new shipping image;
- no new OGG/MP3/WAV, portrait PNG/WebP, animation/video, or UI image;
- one definition pair pointing to the same file, one gallery entry, and at least one live scene use.

- [ ] **Step 6: Render the background with real dialogue and portraits**

Add a focused runtime suite named test_winter_granary_render that opens the granary scene, shows representative left/right portraits separately, captures a clean screenshot, and asserts no missing displayable or gallery key.

Run:

~~~powershell
$assetSaveDir = Join-Path 'C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\work' ("renpy-winter-art-{0}" -f (Get-Date -Format 'yyyyMMdd-HHmmss'))
& Tools/Run-RenPySuite.ps1 -ProjectRoot (Get-Location).Path -Suite test_winter_granary_render -SaveDir $assetSaveDir -Expect PASSED -ExtraArgs @('--overwrite-screenshots')
if ($LASTEXITCODE -ne 0) { throw 'Winter granary render wrapper failed.' }
~~~

Require a fresh [rpytest] Status: PASSED from this process and inspect the new granary screenshot at original detail.

- [ ] **Step 7: Commit the single background integration**

~~~powershell
git add game/images/bg_winter_granary.webp game/images_def.rpy game/gallery.rpy game/governance_winter_interlude.rpy Tools/test_governance_winter_interlude.py game/test_game.rpy
git diff --cached --check
if ($LASTEXITCODE -ne 0) { throw 'Winter-art index failed whitespace validation.' }
git commit -m "art: add winter granary background"
if ($LASTEXITCODE -ne 0) { throw 'Winter-art commit failed.' }
~~~

**Asset audit:** Required new art: one 1280×720 WebP, at most 1.2 MiB. Music, SFX, portraits, animation, and UI art remain unchanged. Gallery layout changes are script-only.

---

### Task 11: Verify small/touch rendering at 100% and 150%

**Files:**

- Modify: game/test_game.rpy
- Modify: game/screens.rpy only if real screenshots show clipping or unsafe overlap
- Update: tests/screenshots/ only according to the repository's existing reviewed-baseline policy

**Interfaces:**

- Consumes: existing scrollable small choice screen, preferences.font_size, chapter_select viewport, all winter menus, qualitative summary, and new background.
- Produces: real screenshots and reachable last-item interactions at both font scales.

- [ ] **Step 1: Add one dedicated suite with separate 100% and 150% cases**

Add testsuite test_winter_interlude_render with two cases:

~~~text
small_touch_100_all_menus_and_chapter_entry
small_touch_150_all_menus_summary_and_chapter_entry
~~~

The suite must render and interact with:

- four-item first investigation menu, selecting item four;
- three-item second investigation menu, selecting item three;
- three-item policy menu, selecting item three;
- two-item seed menu, selecting item two;
- the longest qualitative summary and longest option subtitle;
- chapter-select entry with text icon "幕";
- granary scene with dialogue and portrait;
- 100% and 150% font size.

For every choice screen, assert its displayable bounds remain above the quick-menu bar and the last option is selectable. Source substring checks do not count.

- [ ] **Step 2: Run the suite once under the small/touch/mobile variant**

~~~powershell
$renderSaveDir = Join-Path 'C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\work' ("renpy-winter-render-{0}" -f (Get-Date -Format 'yyyyMMdd-HHmmss'))
$projectRoot = (Get-Location).Path
$renderEvidence = Join-Path $projectRoot '.superpowers/sdd/winter-render'
& Tools/Run-RenPySuite.ps1 -ProjectRoot $projectRoot -Suite test_winter_interlude_render -SaveDir $renderSaveDir -Expect PASSED -Variant 'small touch mobile' -ExtraArgs @('--overwrite-screenshots') -EvidenceDir $renderEvidence
if ($LASTEXITCODE -ne 0) { throw 'Winter small/touch render wrapper failed.' }
~~~

The first case sets preferences.font_size=1.0; the second sets 1.5. Each restores the prior preference in its after block. Expected: [rpytest] Status: PASSED and distinct 100/150 screenshot names exist.

- [ ] **Step 3: Inspect every screenshot at original detail**

Reject and fix:

- clipped text;
- an unreachable last choice;
- quick-menu overlap;
- unsafe-edge placement;
- invisible scroll affordance where scrolling is required;
- text icon/index mismatch;
- portrait/background collision that obscures a face;
- hard-coded tiny helper text.

Only modify game/screens.rpy if a real failure demonstrates the existing viewport is insufficient. Preserve desktop layout and keyboard navigation.

- [ ] **Step 4: Re-run existing mobile/accessibility regressions**

~~~powershell
$projectRoot = (Get-Location).Path
$mobileEvidence = Join-Path $projectRoot '.superpowers/sdd/winter-mobile-regressions'
foreach ($suite in @('test_mobile_choice_overflow','test_accessibility_render')) {
  $suiteSaveDir = Join-Path 'C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\work' ("renpy-$suite-{0}" -f (Get-Date -Format 'yyyyMMdd-HHmmss-ffff'))
  & Tools/Run-RenPySuite.ps1 -ProjectRoot $projectRoot -Suite $suite -SaveDir $suiteSaveDir -Expect PASSED -Variant 'small touch mobile' -EvidenceDir $mobileEvidence
  if ($LASTEXITCODE -ne 0) { throw "Mobile/accessibility wrapper failed: $suite" }
}
$settingsSaveDir = Join-Path 'C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\work' ("renpy-accessibility-settings-{0}" -f (Get-Date -Format 'yyyyMMdd-HHmmss-ffff'))
& Tools/Run-RenPySuite.ps1 -ProjectRoot $projectRoot -Suite test_accessibility_settings -SaveDir $settingsSaveDir -Expect PASSED -EvidenceDir $mobileEvidence
if ($LASTEXITCODE -ne 0) { throw 'Accessibility settings wrapper failed.' }
~~~

Each suite uses a different savedir because the accessibility suites call renpy.save_persistent(). Never run these commands against the player's real CourtOfShadows-save directory.

- [ ] **Step 5: Commit only verified render/test changes**

~~~powershell
git add game/test_game.rpy game/screens.rpy tests/screenshots
git diff --cached --check
if ($LASTEXITCODE -ne 0) { throw 'Mobile-render index failed whitespace validation.' }
git commit -m "test: verify winter interlude mobile rendering"
if ($LASTEXITCODE -ne 0) { throw 'Mobile-render commit failed.' }
~~~

If game/screens.rpy and screenshot baselines did not change, commit only game/test_game.rpy.

**Asset audit:** Test screenshots stay outside game/ and are not packaged. No new shipping art, music, SFX, portrait, animation, or UI asset.

---

### Task 12: Finalize 3.10 release copy, verify, review, and prove package size

**Files:**

- Modify only files already in scope when a verified gate exposes a defect
- Modify: game/changelog.rpy
- Modify: CHANGELOG.txt
- Create: TapTap_v3.10_更新公告.md
- Modify: Tools/test_release_contract.py
- Read: all changed files since governance-winter-baseline
- Read without staging or committing: the ignored main-repository android.keystore and bundle.keystore used only to sign detached Android builds
- Produce ignored evidence under .superpowers/sdd/ and uniquely named build directories outside the repository

**Interfaces:**

- Consumes: all prior tasks, governance-winter-baseline for functional review, governance-winter-package-baseline for equal-metadata package comparison, five engine-native old-state archives, the two hash-pinned ignored release keystores, release verifier, Ren'Py desktop/Android builders, and existing package rules.
- Produces: approved 3.10 release copy, fresh full-suite/lint/runtime evidence, independent code review, Windows and Android packages, and exact package deltas.

- [ ] **Step 1: Generate, approve, integrate, and commit the real 3.10 release copy**

First prove the version-only fields frozen in Task 2 still match the package baseline byte-for-byte:

~~~powershell
if (-not (Get-Variable packageBaselineHead -ErrorAction SilentlyContinue) -or [string]::IsNullOrWhiteSpace([string]$packageBaselineHead)) { throw 'Re-enter the exact Task 2 packageBaselineHead evidence SHA.' }
if ((git rev-list -n 1 governance-winter-package-baseline).Trim() -ne $packageBaselineHead) { throw 'Package-baseline tag moved before release-copy work.' }
git diff --exit-code $packageBaselineHead -- game/options.rpy game/effects.rpy android.json README.txt
if ($LASTEXITCODE -ne 0) { throw 'Frozen 3.10 package metadata drifted after the baseline tag.' }
~~~

Add RED assertions to Tools/test_release_contract.py requiring:

- a new top in-game entry v3.25 labelled 商店版 v3.10 above the historical v3.24/3.9.2 entry;
- a new 3.10 section at the top of CHANGELOG.txt;
- a factual TapTap_v3.10_更新公告.md;
- no claim that the optional interlude changes stats, endings, or battle outcomes;
- no stale current-version wording, while historical entries remain untouched.

Run the focused test and prove it fails only because the three new release-copy artifacts are absent:

~~~powershell
New-Item -ItemType Directory -Path .superpowers/sdd -Force | Out-Null
$releaseCopyRedOutput = (python -m unittest Tools.test_release_contract -v 2>&1) -join "`n"
$releaseCopyRedExit = $LASTEXITCODE
$releaseCopyRedOutput | Tee-Object -FilePath .superpowers/sdd/release-copy-python-red.txt
if ($releaseCopyRedExit -eq 0) { throw 'Release-copy contract unexpectedly passed before v3.10 copy existed.' }
if ($releaseCopyRedOutput -notmatch '(?i)v3\.25|3\.10|changelog|TapTap') { throw 'Release-copy RED did not identify the intended missing copy.' }
if ($releaseCopyRedOutput -match '(?i)SyntaxError|ImportError|ModuleNotFoundError') { throw 'Release-copy RED was caused by a test/import crash.' }
~~~

Use the invoke-opus-4-6 skill and two fresh Claude Code sessions: one for the concise in-game entry, one for the external CHANGELOG/TapTap copy. Select /model claude-opus-4-6, disable tools and persistence, provide only verified final feature facts and output format, validate both initialization/result metadata, save raw outputs in ignored evidence, and show each raw result to the user for approval. Do not provide old drafts, examples, style constraints, writing-game-copy, code, or local paths.

Integrate only approved copy with apply_patch, then run and commit fail-closed:

~~~powershell
python -m unittest Tools.test_release_contract -v
if ($LASTEXITCODE -ne 0) { throw 'Approved 3.10 release copy failed its contract.' }
foreach ($externalCopy in @('CHANGELOG.txt','TapTap_v3.10_更新公告.md')) {
  python Tools/scan_ai_smell.py $externalCopy | Tee-Object -FilePath (Join-Path '.superpowers/sdd' ((Split-Path $externalCopy -Leaf) + '.ai-smell.txt'))
  if ($LASTEXITCODE -ne 0) { throw "AI-smell scanner crashed on release copy: $externalCopy" }
}
python prepare_release.py
$releaseFontFirst = $LASTEXITCODE
if ($releaseFontFirst -notin @(0,1)) { throw 'First release-copy font gate failed.' }
python prepare_release.py
if ($LASTEXITCODE -ne 0) { throw 'Second release-copy font gate failed.' }
git add game/changelog.rpy game/msyh.ttf CHANGELOG.txt TapTap_v3.10_更新公告.md Tools/test_release_contract.py
if ($LASTEXITCODE -ne 0) { throw 'Could not stage approved 3.10 release copy.' }
git diff --cached --check
if ($LASTEXITCODE -ne 0) { throw 'Release-copy index failed whitespace validation.' }
git commit -m "docs: publish 3.10 winter interlude notes"
if ($LASTEXITCODE -ne 0) { throw 'Release-copy commit failed.' }
git diff --exit-code $packageBaselineHead -- game/options.rpy game/effects.rpy android.json README.txt
if ($LASTEXITCODE -ne 0) { throw 'Frozen package metadata drifted while adding release copy.' }
~~~

The AI-smell output is a manual inspection queue, not an automatic rewrite gate. game/changelog.rpy remains on the scanner's intentional changelog allowlist and is accepted only through the raw Opus approval plus release contract. The first font exit may be 0 or 1; the second must be 0. Commit before any review or build.

After the commit, rerun the frozen-metadata diff above. Changelog RPYC/text and its font glyphs are intentionally after governance-winter-package-baseline and therefore count toward the 2 MiB feature delta.

- [ ] **Step 2: Run the font and all Python/source gates from a clean HEAD**

~~~powershell
New-Item -ItemType Directory -Path .superpowers/sdd -Force | Out-Null
python prepare_release.py
$fontFirst = $LASTEXITCODE
if ($fontFirst -notin @(0,1)) { throw 'First final font gate failed.' }
python prepare_release.py
if ($LASTEXITCODE -ne 0) { throw 'Second final font gate failed.' }
if ($fontFirst -eq 1) {
  git add game/msyh.ttf
  if ($LASTEXITCODE -ne 0) { throw 'Could not stage final font refresh.' }
  git commit -m "chore: refresh 3.10 release font"
  if ($LASTEXITCODE -ne 0) { throw 'Final font refresh commit failed.' }
}
python -m unittest discover -s Tools -p "test_*.py" -v
if ($LASTEXITCODE -ne 0) { throw 'Full Python test suite failed.' }
python Tools/test_story_timeline.py -v
if ($LASTEXITCODE -ne 0) { throw 'Timeline gate failed.' }
python Tools/test_release_regressions.py
if ($LASTEXITCODE -ne 0) { throw 'Release regression gate failed.' }
python Tools/scan_canon.py
if ($LASTEXITCODE -ne 0) { throw 'Canon scan failed.' }
foreach ($copyFile in @('game/governance_winter_interlude.rpy','game/chapter2.rpy','game/interludes.rpy','game/chapter5.rpy','game/chapter5_expansion.rpy','game/endings_expansion.rpy','game/changelog.rpy')) {
  python Tools/scan_ai_smell.py $copyFile | Tee-Object -FilePath (Join-Path '.superpowers/sdd' ((Split-Path $copyFile -Leaf) + '.ai-smell.txt'))
  if ($LASTEXITCODE -ne 0) { throw "AI-smell scanner crashed: $copyFile" }
}
python Tools/scan_nested_quotes.py
if ($LASTEXITCODE -ne 0) { throw 'Nested-quote scan failed.' }
python scan_missing_portraits.py
if ($LASTEXITCODE -ne 0) { throw 'Portrait scan failed.' }
python scan_narration_overlap.py governance_winter_interlude.rpy chapter2.rpy interludes.rpy chapter5.rpy chapter5_expansion.rpy endings_expansion.rpy | Tee-Object -FilePath .superpowers/sdd/final-narration-overlap.txt
if ($LASTEXITCODE -ne 0) { throw 'Final narration-overlap scanner crashed.' }
$fixtureManifest = Get-Content -LiteralPath tests/fixtures/winter_legacy/manifest.json -Raw | ConvertFrom-Json
$functionalBaselineHead = [string]$fixtureManifest.baseline_commit
if ((git rev-list -n 1 governance-winter-baseline).Trim() -ne $functionalBaselineHead) { throw 'Functional baseline tag moved away from the fixture manifest.' }
git diff "${functionalBaselineHead}..HEAD" --check
if ($LASTEXITCODE -ne 0) { throw 'Functional-range whitespace check failed.' }
if (-not (Get-Variable packageBaselineHead -ErrorAction SilentlyContinue) -or [string]::IsNullOrWhiteSpace([string]$packageBaselineHead)) { throw 'Re-enter the exact Task 2 packageBaselineHead evidence SHA.' }
if ((git rev-list -n 1 governance-winter-package-baseline).Trim() -ne $packageBaselineHead) { throw 'Package-baseline tag moved before final source gates.' }
git diff --exit-code $packageBaselineHead -- game/options.rpy game/effects.rpy android.json README.txt
if ($LASTEXITCODE -ne 0) { throw 'Frozen package metadata changed.' }
$dirty = @(git status --porcelain)
if ($dirty.Count -ne 0) { throw "Final source gates left a dirty worktree: $($dirty -join '; ')" }
~~~

If the first font pass changed the font, rerun this entire step after its commit. Expected: second font run exits 0; all tests pass; the new module is actually covered by nested-quote/narration scans; every AI-smell and overlap finding is manually classified with zero actionable finding left; no whitespace errors; frozen metadata is unchanged; working tree is clean. If the portrait scan changes tracked missing_portraits_B.txt here, stop: either the relevant story task failed to commit its reviewed reproducible report or a new finding exists. Resolve and commit it in a focused RED→GREEN cycle, then restart all final gates.

- [ ] **Step 3: Run every focused Ren'Py suite with isolated saves and unique fresh evidence**

~~~powershell
$projectRoot = (Get-Location).Path
$headShort = (git rev-parse --short HEAD).Trim()
$evidenceRoot = Join-Path $projectRoot (".superpowers/sdd/final-{0}" -f $headShort)
New-Item -ItemType Directory -Path $evidenceRoot -Force | Out-Null
$fixtureSuites = @('test_winter_interlude_legacy_migration','test_winter_interlude_continuations')
$suites = @(
  'test_winter_interlude_state',
  'test_winter_interlude_legacy_migration',
  'test_winter_interlude_ending_invariance',
  'test_winter_interlude_continuations',
  'test_winter_interlude_routing',
  'test_winter_interlude_route_matrix',
  'test_winter_interlude_mid_save',
  'test_winter_interlude_downstream_invariance',
  'test_winter_interlude_chapter_select',
  'test_winter_interlude_audio',
  'test_winter_granary_render',
  'test_release_metadata_render',
  'test_accessibility_settings',
  'test_new_run_bootstrap',
  'test_critical_finale_routes',
  'test_ending_catalog',
  'test_walkthrough'
)
foreach ($suite in $suites) {
  $suiteSaveDir = Join-Path 'C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\work' ("renpy-final-$suite-{0}" -f (Get-Date -Format 'yyyyMMdd-HHmmss-ffff'))
  $runArgs = @{
    ProjectRoot = $projectRoot
    Suite = $suite
    SaveDir = $suiteSaveDir
    Expect = 'PASSED'
    TimeoutSeconds = 1200
    EvidenceDir = $evidenceRoot
  }
  if ($suite -in $fixtureSuites) { $runArgs.StageLegacyFixtures = $true }
  & Tools/Run-RenPySuite.ps1 @runArgs
  if ($LASTEXITCODE -ne 0) { throw "Fail-closed Ren'Py wrapper failed: $suite" }
}
~~~

Expected: every suite has a distinct savedir and one uniquely named log produced after its own start time and HEAD; fixture-dependent suites load hash-verified archives; every recorded process exits zero before its timeout, leaves no recorded PID alive, and has exactly one PASSED status.

- [ ] **Step 4: Run the full Ren'Py suite and fail-closed lint with separate savedirs**

~~~powershell
$projectRoot = (Get-Location).Path
$headShort = (git rev-parse --short HEAD).Trim()
$evidenceRoot = Join-Path $projectRoot (".superpowers/sdd/final-{0}" -f $headShort)
New-Item -ItemType Directory -Path $evidenceRoot -Force | Out-Null
$fullSaveDir = Join-Path 'C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\work' ("renpy-winter-full-{0}" -f (Get-Date -Format 'yyyyMMdd-HHmmss'))
$lintSaveDir = Join-Path 'C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\work' ("renpy-winter-lint-{0}" -f (Get-Date -Format 'yyyyMMdd-HHmmss'))
& Tools/Run-RenPySuite.ps1 -ProjectRoot $projectRoot -Mode Full -SaveDir $fullSaveDir -Expect PASSED -StageLegacyFixtures -TimeoutSeconds 3600 -EvidenceDir $evidenceRoot
if ($LASTEXITCODE -ne 0) { throw 'Fail-closed full Ren''Py wrapper failed.' }
& Tools/Run-RenPySuite.ps1 -ProjectRoot $projectRoot -Mode Lint -SaveDir $lintSaveDir -TimeoutSeconds 1200 -EvidenceDir $evidenceRoot
if ($LASTEXITCODE -ne 0) { throw 'Fail-closed Ren''Py lint wrapper failed.' }
~~~

The helper must add --error-code in Lint mode; without it Ren'Py lint may report errors while returning success. Do not accept a timeout, existing log, or orphaned process as success. The helper records the PID it starts and, on timeout, terminates only that PID before returning failure.

- [ ] **Step 5: Request independent spec and code review**

Before review, bind the functional base to the fixture manifest rather than trusting a movable tag:

~~~powershell
$fixtureManifest = Get-Content -LiteralPath tests/fixtures/winter_legacy/manifest.json -Raw | ConvertFrom-Json
$functionalBaselineHead = [string]$fixtureManifest.baseline_commit
if ([string]::IsNullOrWhiteSpace($functionalBaselineHead)) { throw 'Fixture manifest has no functional baseline commit.' }
if ((git rev-list -n 1 governance-winter-baseline).Trim() -ne $functionalBaselineHead) { throw 'governance-winter-baseline moved away from the fixture-proven commit.' }
git merge-base --is-ancestor $functionalBaselineHead HEAD
if ($LASTEXITCODE -ne 0) { throw 'Functional baseline is not an ancestor of the review candidate.' }
$reviewHead = (git rev-parse HEAD).Trim()
~~~

Use superpowers:requesting-code-review against the immutable range `$functionalBaselineHead..$reviewHead`. Require the review evidence to name `$reviewHead` exactly and inspect:

- explicit state precedence and active save behavior;
- three real old-save continuations, one real completion archive, one synthetic neutral archive, fixture signatures, and pad fallthrough firewall;
- strict invalid-completed/active fallback and mid-menu call-stack-local saves;
- forbidden main-state writes;
- 36 production-menu outcomes, 12 investigation orders, omitted reports, and one-mitigation priority;
- southern salt, old governance, decree, and attribute softening without persistent recalculation;
- ending/battle invariance;
- all old merchant/famine consumers;
- Harrenhall policy pressure and Karl framing while every original choice, condition, price, stat/relationship write, and branch remains unchanged;
- every Chapter 5 current-stock/duration claim uses the saved winter context, while future refill orders and baseline-hashed bonus guards remain unchanged;
- chapter selector's three parallel arrays;
- Chapter 2 actual music channel;
- mobile 100%/150% screenshots;
- one-asset-only and package-size contract;
- narrative canon, viewpoint, repeated actions, and concrete costs.
- 3.10 frozen metadata, RPYC=56, release copy, and fixed Android versionCode.

Fix every Critical or Important issue with a new RED→GREEN micro-cycle, rerun Steps 2–4 from clean HEAD, then request re-review until none remain. Reset `$reviewHead` to the final reviewed HEAD and retain that exact SHA in evidence; any review of an older SHA is invalid.

- [ ] **Step 6: Re-run final small/touch/mobile and accessibility evidence after review**

Run these suites after the last review fix, each in its own new savedir with immediate exit and fresh-log checks:

~~~powershell
$projectRoot = (Get-Location).Path
$headShort = (git rev-parse --short HEAD).Trim()
$evidenceRoot = Join-Path $projectRoot (".superpowers/sdd/final-{0}" -f $headShort)
New-Item -ItemType Directory -Path $evidenceRoot -Force | Out-Null
foreach ($suite in @('test_winter_interlude_render','test_mobile_choice_overflow','test_accessibility_render')) {
  $suiteSaveDir = Join-Path 'C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\work' ("renpy-final-small-$suite-{0}" -f (Get-Date -Format 'yyyyMMdd-HHmmss-ffff'))
  & Tools/Run-RenPySuite.ps1 -ProjectRoot $projectRoot -Suite $suite -SaveDir $suiteSaveDir -Expect PASSED -Variant 'small touch mobile' -EvidenceDir $evidenceRoot
  if ($LASTEXITCODE -ne 0) { throw "Final small/touch wrapper failed: $suite" }
}
$settingsSaveDir = Join-Path 'C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\work' ("renpy-final-accessibility-settings-{0}" -f (Get-Date -Format 'yyyyMMdd-HHmmss-ffff'))
& Tools/Run-RenPySuite.ps1 -ProjectRoot $projectRoot -Suite test_accessibility_settings -SaveDir $settingsSaveDir -Expect PASSED -EvidenceDir $evidenceRoot
if ($LASTEXITCODE -ne 0) { throw 'Final accessibility-settings wrapper failed.' }
~~~

test_winter_interlude_render compares the reviewed 100% and 150% screenshots without --overwrite-screenshots. Inspect them again at original detail. test_accessibility_settings runs outside the variant in its own isolated savedir because it persists preferences. Never use the player's real save directory.

- [ ] **Step 7: Build a clean equal-metadata baseline Windows ZIP and Android APK**

Create a detached baseline worktree from governance-winter-package-baseline, not governance-winter-baseline. Use timestamp/tag-derived paths and fail if either path already exists; do not overwrite prior release evidence. Retain `$reviewHead` from the final review and `$packageBaselineHead` from Task 2; if starting a new shell, assign only those recorded SHAs, never the current HEAD/tag by assumption. Run Steps 7–11 in the same PowerShell session so the exact build paths remain bound to the artifacts being verified. If the session is interrupted, re-enter only the exact paths printed by the original build and revalidate their commits; never rediscover artifacts by choosing the newest directory.

~~~powershell
$mainRepo = 'E:\Projects\renpy-8.5.2-sdk\CourtOfShadows'
$stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
$fixtureManifest = Get-Content -LiteralPath tests/fixtures/winter_legacy/manifest.json -Raw | ConvertFrom-Json
$functionalBaselineHead = [string]$fixtureManifest.baseline_commit
if ((git -C $mainRepo rev-list -n 1 governance-winter-baseline).Trim() -ne $functionalBaselineHead) { throw 'Functional baseline tag moved after review.' }
if (-not (Get-Variable packageBaselineHead -ErrorAction SilentlyContinue) -or [string]::IsNullOrWhiteSpace([string]$packageBaselineHead)) { throw 'Re-enter the exact Task 2 packageBaselineHead evidence SHA.' }
$baselineHead = [string]$packageBaselineHead
if ((git -C $mainRepo rev-list -n 1 governance-winter-package-baseline).Trim() -ne $baselineHead) { throw 'Package-baseline tag moved away from Task 2 evidence.' }
git -C $mainRepo merge-base --is-ancestor $functionalBaselineHead $baselineHead
if ($LASTEXITCODE -ne 0) { throw 'Package baseline does not descend from the fixture-proven functional baseline.' }
git -C $mainRepo cat-file -e "${baselineHead}:game/governance_winter_interlude.rpy" 2>$null
if ($LASTEXITCODE -eq 0) { throw 'Package baseline is contaminated with the winter production module.' }
$baselineVerifierSource = (git -C $mainRepo show "${baselineHead}:Tools/verify_distributions.py") -join "`n"
if ($LASTEXITCODE -ne 0 -or $baselineVerifierSource -notmatch 'EXPECTED_RELEASE_RPYC_COUNT\s*=\s*55') { throw 'Package baseline does not preserve the pre-feature RPYC=55 contract.' }
$baselineShort = $baselineHead.Substring(0, [Math]::Min(12, $baselineHead.Length))
$baselineRoot = "C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\work\CourtOfShadows-package-baseline-$baselineShort-$stamp"
$baselineDist = "E:\Projects\renpy-8.5.2-sdk\CourtOfShadows-package-baseline-$baselineShort-$stamp-dists"
if ((Test-Path -LiteralPath $baselineRoot) -or (Test-Path -LiteralPath $baselineDist)) { throw 'Unique baseline build path already exists.' }
git -C $mainRepo worktree add --detach $baselineRoot $baselineHead
if ($LASTEXITCODE -ne 0) { throw 'Baseline detached worktree creation failed.' }
if ((git -C $baselineRoot rev-parse HEAD).Trim() -ne $baselineHead) { throw 'Baseline detached worktree is at the wrong commit.' }
Push-Location $baselineRoot
try {
  python prepare_release.py
  if ($LASTEXITCODE -ne 0) { throw 'Immutable package baseline font is stale.' }
}
finally {
  Pop-Location
}
if (@(git -C $baselineRoot status --porcelain).Count -ne 0) { throw 'Baseline detached worktree is dirty before build.' }
New-Item -ItemType Directory -Path $baselineDist | Out-Null
& 'E:\Projects\renpy-8.5.2-sdk\renpy.exe' 'E:\Projects\renpy-8.5.2-sdk\launcher' distribute --package win --destination $baselineDist $baselineRoot
if ($LASTEXITCODE -ne 0) { throw 'Baseline Windows build failed.' }
$expectedKeystoreHash = '461145F95CA5735A388DD3A22F2DCEEE84A9440F20466A904E3374419229A7EB'
$keystoreNames = @('android.keystore','bundle.keystore')
foreach ($keyName in $keystoreNames) {
  $sourceKey = Join-Path $mainRepo $keyName
  if (-not (Test-Path -LiteralPath $sourceKey -PathType Leaf)) { throw "Release keystore is missing: $keyName" }
  if ((Get-Item -LiteralPath $sourceKey).Length -ne 2554 -or (Get-FileHash -LiteralPath $sourceKey -Algorithm SHA256).Hash -ne $expectedKeystoreHash) { throw "Release keystore identity changed: $keyName" }
}
$baselineKeyTargets = @($keystoreNames | ForEach-Object { Join-Path $baselineRoot $_ })
$baselineRootFull = [IO.Path]::GetFullPath($baselineRoot).TrimEnd('\')
foreach ($targetKey in $baselineKeyTargets) {
  if ([IO.Path]::GetFullPath((Split-Path -Parent $targetKey)).TrimEnd('\') -ne $baselineRootFull) { throw 'Baseline keystore target escaped the detached worktree root.' }
  if (Test-Path -LiteralPath $targetKey) { throw "Baseline keystore target unexpectedly exists: $targetKey" }
}
$baselineAndroidExit = $null
try {
  foreach ($keyName in $keystoreNames) {
    $sourceKey = Join-Path $mainRepo $keyName
    $targetKey = Join-Path $baselineRoot $keyName
    Copy-Item -LiteralPath $sourceKey -Destination $targetKey -ErrorAction Stop
    if ((Get-FileHash -LiteralPath $targetKey -Algorithm SHA256).Hash -ne $expectedKeystoreHash) { throw "Copied baseline keystore hash mismatch: $keyName" }
  }
  & 'E:\Projects\renpy-8.5.2-sdk\renpy.exe' 'E:\Projects\renpy-8.5.2-sdk\launcher' android_build --destination $baselineDist --package android $baselineRoot
  $baselineAndroidExit = $LASTEXITCODE
}
finally {
  foreach ($targetKey in $baselineKeyTargets) {
    if (Test-Path -LiteralPath $targetKey) { Remove-Item -LiteralPath $targetKey -Force -ErrorAction SilentlyContinue }
  }
  $remainingBaselineKeys = @($baselineKeyTargets | Where-Object { Test-Path -LiteralPath $_ })
  if ($remainingBaselineKeys.Count -ne 0) { throw "Temporary baseline keystore cleanup failed: $($remainingBaselineKeys -join ', ')" }
}
if ($baselineAndroidExit -ne 0) { throw 'Baseline Android build failed.' }
if (@(git -C $baselineRoot status --porcelain).Count -ne 0) { throw 'Baseline build dirtied tracked source.' }
Get-Item -LiteralPath $baselineRoot,$baselineDist | Select-Object FullName
~~~

Require the detached worktree HEAD to equal governance-winter-package-baseline and remain clean. The two ignored signing keys are copied only after exact size/hash validation, removed in finally even when the Android build fails, and must not remain in the worktree or be staged. Do not delete this worktree or output until the final comparison and review are complete.

- [ ] **Step 8: Build final packages from a second clean detached HEAD worktree**

~~~powershell
$mainRepo = 'E:\Projects\renpy-8.5.2-sdk\CourtOfShadows'
$featureRoot = (Get-Location).Path
if ((git status --porcelain).Count -ne 0) { throw 'Feature worktree is not clean before packaging.' }
$finalCommit = (git rev-parse HEAD).Trim()
if (-not (Get-Variable reviewHead -ErrorAction SilentlyContinue) -or $finalCommit -ne $reviewHead) { throw 'Final HEAD is not the exact independently reviewed commit.' }
git merge-base --is-ancestor $functionalBaselineHead $finalCommit
if ($LASTEXITCODE -ne 0) { throw 'Final commit does not descend from the fixture-proven functional baseline.' }
git merge-base --is-ancestor $baselineHead $finalCommit
if ($LASTEXITCODE -ne 0) { throw 'Final commit does not descend from the equal-metadata package baseline.' }
$finalShort = (git rev-parse --short HEAD).Trim()
$finalStamp = Get-Date -Format 'yyyyMMdd-HHmmss'
$finalRoot = "C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\work\CourtOfShadows-final-$finalShort-$finalStamp"
$finalDist = "E:\Projects\renpy-8.5.2-sdk\CourtOfShadows-final-$finalShort-$finalStamp-dists"
if ((Test-Path -LiteralPath $finalRoot) -or (Test-Path -LiteralPath $finalDist)) { throw 'Unique final build path already exists.' }
git -C $mainRepo worktree add --detach $finalRoot $finalCommit
if ($LASTEXITCODE -ne 0) { throw 'Final detached worktree creation failed.' }
if ((git -C $finalRoot rev-parse HEAD).Trim() -ne $finalCommit) { throw 'Final detached worktree is at the wrong commit.' }
Push-Location $finalRoot
try {
  python prepare_release.py
  if ($LASTEXITCODE -ne 0) { throw 'Final detached font is stale.' }
}
finally {
  Pop-Location
}
if (@(git -C $finalRoot status --porcelain).Count -ne 0) { throw 'Final detached worktree is dirty before build.' }
New-Item -ItemType Directory -Path $finalDist | Out-Null
& 'E:\Projects\renpy-8.5.2-sdk\renpy.exe' 'E:\Projects\renpy-8.5.2-sdk\launcher' distribute --package win --destination $finalDist $finalRoot
if ($LASTEXITCODE -ne 0) { throw 'Final Windows build failed.' }
$expectedKeystoreHash = '461145F95CA5735A388DD3A22F2DCEEE84A9440F20466A904E3374419229A7EB'
$keystoreNames = @('android.keystore','bundle.keystore')
foreach ($keyName in $keystoreNames) {
  $sourceKey = Join-Path $mainRepo $keyName
  if (-not (Test-Path -LiteralPath $sourceKey -PathType Leaf)) { throw "Release keystore is missing: $keyName" }
  if ((Get-Item -LiteralPath $sourceKey).Length -ne 2554 -or (Get-FileHash -LiteralPath $sourceKey -Algorithm SHA256).Hash -ne $expectedKeystoreHash) { throw "Release keystore identity changed: $keyName" }
}
$finalKeyTargets = @($keystoreNames | ForEach-Object { Join-Path $finalRoot $_ })
$finalRootFull = [IO.Path]::GetFullPath($finalRoot).TrimEnd('\')
foreach ($targetKey in $finalKeyTargets) {
  if ([IO.Path]::GetFullPath((Split-Path -Parent $targetKey)).TrimEnd('\') -ne $finalRootFull) { throw 'Final keystore target escaped the detached worktree root.' }
  if (Test-Path -LiteralPath $targetKey) { throw "Final keystore target unexpectedly exists: $targetKey" }
}
$finalAndroidExit = $null
try {
  foreach ($keyName in $keystoreNames) {
    $sourceKey = Join-Path $mainRepo $keyName
    $targetKey = Join-Path $finalRoot $keyName
    Copy-Item -LiteralPath $sourceKey -Destination $targetKey -ErrorAction Stop
    if ((Get-FileHash -LiteralPath $targetKey -Algorithm SHA256).Hash -ne $expectedKeystoreHash) { throw "Copied final keystore hash mismatch: $keyName" }
  }
  & 'E:\Projects\renpy-8.5.2-sdk\renpy.exe' 'E:\Projects\renpy-8.5.2-sdk\launcher' android_build --destination $finalDist --package android $finalRoot
  $finalAndroidExit = $LASTEXITCODE
}
finally {
  foreach ($targetKey in $finalKeyTargets) {
    if (Test-Path -LiteralPath $targetKey) { Remove-Item -LiteralPath $targetKey -Force -ErrorAction SilentlyContinue }
  }
  $remainingFinalKeys = @($finalKeyTargets | Where-Object { Test-Path -LiteralPath $_ })
  if ($remainingFinalKeys.Count -ne 0) { throw "Temporary final keystore cleanup failed: $($remainingFinalKeys -join ', ')" }
}
if ($finalAndroidExit -ne 0) { throw 'Final Android build failed.' }
if (@(git -C $finalRoot status --porcelain).Count -ne 0) { throw 'Final build dirtied tracked source.' }
Get-Item -LiteralPath $finalRoot,$finalDist | Select-Object FullName
~~~

Require the final detached worktree HEAD to equal finalCommit and remain clean, and require both temporary keystore copies to be absent after the Android build. Building from the long-lived development worktree is not allowed because ignored stale RPYC/cache files would make the comparison asymmetric.

- [ ] **Step 9: Prove artifact identity, metadata, signatures, and package deltas**

Resolve exactly one Windows ZIP and one release APK from each of the two exact output directories retained above. Fail on zero or multiple matches; never select an artifact by modification time:

~~~powershell
$baselineWins = @(Get-ChildItem -LiteralPath $baselineDist -Recurse -File | Where-Object Name -Like '*-win.zip')
$baselineApks = @(Get-ChildItem -LiteralPath $baselineDist -Recurse -File | Where-Object Name -Like '*-release.apk')
$finalWins = @(Get-ChildItem -LiteralPath $finalDist -Recurse -File | Where-Object Name -Like '*-win.zip')
$finalApks = @(Get-ChildItem -LiteralPath $finalDist -Recurse -File | Where-Object Name -Like '*-release.apk')
if ($baselineWins.Count -ne 1 -or $baselineApks.Count -ne 1 -or $finalWins.Count -ne 1 -or $finalApks.Count -ne 1) { throw 'Expected exactly one Windows ZIP and one release APK in each build output.' }
$baselineWin = $baselineWins[0]
$baselineApk = $baselineApks[0]
$finalWin = $finalWins[0]
$finalApk = $finalApks[0]
if ($baselineWin.Name -notlike '*-3.10-win.zip' -or $finalWin.Name -notlike '*-3.10-win.zip') { throw 'Windows archive versionName is not 3.10.' }

$aapt2 = 'E:\Projects\renpy-8.5.2-sdk\rapt\Sdk\build-tools\35.0.0\aapt2.exe'
$apksigner = 'E:\Projects\renpy-8.5.2-sdk\rapt\Sdk\build-tools\35.0.0\apksigner.bat'
$expectedSigner = '5fcb5758461427026b13ecf987e86ad11e13170dc60386d42e4c2f20a93b3708'
function Assert-ApkIdentity([System.IO.FileInfo] $apk) {
  $badging = (& $aapt2 dump badging $apk.FullName 2>&1) -join "`n"
  if ($LASTEXITCODE -ne 0) { throw "aapt2 failed: $($apk.FullName)" }
  if ($badging -notmatch "versionName='3\.10'" -or $badging -notmatch "versionCode='2000000000'") { throw "APK version contract failed: $($apk.FullName)" }
  $certText = (& $apksigner verify --print-certs $apk.FullName 2>&1) -join "`n"
  if ($LASTEXITCODE -ne 0) { throw "APK signature verification failed: $($apk.FullName)" }
  $signers = [regex]::Matches($certText, '(?im)^Signer #\d+ certificate SHA-256 digest:\s*([0-9a-f]{64})\s*$')
  if ($signers.Count -ne 1 -or $signers[0].Groups[1].Value.ToLowerInvariant() -ne $expectedSigner) { throw "APK signer contract failed: $($apk.FullName)" }
}
Assert-ApkIdentity $baselineApk
Assert-ApkIdentity $finalApk

$art = Get-Item -LiteralPath (Join-Path $finalRoot 'game/images/bg_winter_granary.webp')
$windowsDelta = [int64]$finalWin.Length - [int64]$baselineWin.Length
$androidDelta = [int64]$finalApk.Length - [int64]$baselineApk.Length
if ($art.Length -gt 1258291) { throw 'Winter granary exceeds 1.2 MiB.' }
if ($windowsDelta -gt 2097152) { throw "Windows package grew by $windowsDelta bytes." }
if ($androidDelta -gt 2097152) { throw "Android package grew by $androidDelta bytes." }
Get-FileHash -Algorithm SHA256 -LiteralPath $baselineWin.FullName,$baselineApk.FullName,$finalWin.FullName,$finalApk.FullName
@($baselineWin,$baselineApk,$finalWin,$finalApk,$art) | Select-Object FullName,Length
"Windows delta: $windowsDelta bytes"
"Android delta: $androidDelta bytes"

$previousApk = 'E:\Projects\renpy-8.5.2-sdk\CourtOfShadows-3.9.2-6d6add0-ch3bgm-final3-dists\com.xiaoyiai.courtofshadows-3.9.2-1785682834-release.apk'
if (-not (Test-Path -LiteralPath $previousApk -PathType Leaf)) { throw 'Previous signed comparison APK is missing.' }
if ((Get-FileHash -LiteralPath $previousApk -Algorithm SHA256).Hash -ne '67963A33D27014738A18584BE23049026596B6132B6EB95887747D0EB2667771') { throw 'Previous signed APK hash mismatch.' }
Push-Location $baselineRoot
try {
  python Tools/verify_distributions.py --windows $baselineWin.FullName --apk $baselineApk.FullName --previous-apk $previousApk --build-tools 'E:\Projects\renpy-8.5.2-sdk\rapt\Sdk\build-tools\35.0.0'
  $baselineVerifyExit = $LASTEXITCODE
}
finally {
  Pop-Location
}
if ($baselineVerifyExit -ne 0) { throw 'Package-baseline distribution verifier failed.' }
if ((git -C $featureRoot rev-parse HEAD).Trim() -ne $finalCommit) { throw 'Feature HEAD changed before final artifact verification.' }
if ((git -C $finalRoot rev-parse HEAD).Trim() -ne $finalCommit) { throw 'Final detached worktree no longer matches finalCommit.' }
Push-Location $finalRoot
try {
  python Tools/verify_distributions.py --windows $finalWin.FullName --apk $finalApk.FullName --previous-apk $previousApk --build-tools 'E:\Projects\renpy-8.5.2-sdk\rapt\Sdk\build-tools\35.0.0'
  $finalVerifyExit = $LASTEXITCODE
}
finally {
  Pop-Location
}
if ($finalVerifyExit -ne 0) { throw 'Final distribution verifier failed.' }
~~~

The machine-enforced limits are:

~~~text
game/images/bg_winter_granary.webp <= 1,258,291 bytes
final Windows bytes - baseline Windows bytes <= 2,097,152
final APK bytes - baseline APK bytes <= 2,097,152
~~~

If compression causes a negative delta, report the actual negative value; do not replace it with zero.

- [ ] **Step 10: Smoke-test the packaged Windows build and a dedicated Android target**

Expand the final Windows ZIP into a unique empty directory, then launch its executable with a new isolated savedir. This is intentionally a visible interactive process because the tester must control the game; it must never read or write the player's real saves:

~~~powershell
$smokeStamp = Get-Date -Format 'yyyyMMdd-HHmmss-ffff'
$windowsExtractRoot = "C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\work\CourtOfShadows-win-smoke-$smokeStamp"
$windowsSaveDir = "C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\work\CourtOfShadows-win-save-$smokeStamp"
if ((Test-Path -LiteralPath $windowsExtractRoot) -or (Test-Path -LiteralPath $windowsSaveDir)) { throw 'Windows smoke-test path already exists.' }
New-Item -ItemType Directory -Path $windowsExtractRoot,$windowsSaveDir | Out-Null
Expand-Archive -LiteralPath $finalWin.FullName -DestinationPath $windowsExtractRoot
$windowsExe = Join-Path $windowsExtractRoot 'CourtOfShadows-3.10-win\CourtOfShadows.exe'
if (-not (Test-Path -LiteralPath $windowsExe -PathType Leaf)) { throw 'Packaged Windows executable is missing.' }
$windowsSmokeProcess = Start-Process -FilePath $windowsExe -ArgumentList @('--savedir', ('"' + $windowsSaveDir + '"')) -PassThru
if ($null -eq $windowsSmokeProcess -or $windowsSmokeProcess.Id -le 0) { throw 'Packaged Windows smoke process did not start.' }
"Windows smoke PID: $($windowsSmokeProcess.Id)"
~~~

In that packaged build verify and record:

- normal Chapter 1→southern→winter→Chapter 2 route;
- delegate route;
- one active route;
- save/load and rollback around each menu;
- Chapter 2 music after cinematic;
- no missing font glyph/background/audio.

After recording the manual observations, close the packaged game normally and prove that the exact recorded process exits cleanly. Bound the interactive session to one hour; on timeout terminate only the PID started above and fail the smoke test:

~~~powershell
if (-not $windowsSmokeProcess.WaitForExit(3600000)) {
  Stop-Process -Id $windowsSmokeProcess.Id -Force -ErrorAction SilentlyContinue
  throw "Windows package smoke timed out; terminated only PID $($windowsSmokeProcess.Id)."
}
$windowsSmokeProcess.Refresh()
if ($windowsSmokeProcess.ExitCode -ne 0) { throw "Windows package smoke exited with code $($windowsSmokeProcess.ExitCode)." }
if (Get-Process -Id $windowsSmokeProcess.Id -ErrorAction SilentlyContinue) { throw 'Recorded Windows smoke PID remains alive after exit.' }
~~~

For Android, package inspection is not runtime evidence. Set `COURT_OF_SHADOWS_TEST_DEVICE_SERIAL` only after selecting and recording a dedicated emulator or test device from `adb devices`; do not use a personal installation, clear app data, or overwrite player data. Install the exact `$finalApk` on that target and record the serial, APK hash, install result, and screenshots/logs:

~~~powershell
$adb = 'E:\Projects\renpy-8.5.2-sdk\rapt\Sdk\platform-tools\adb.exe'
$androidTestSerial = $env:COURT_OF_SHADOWS_TEST_DEVICE_SERIAL
if ([string]::IsNullOrWhiteSpace($androidTestSerial)) { throw 'Set the dedicated Android test-device serial explicitly.' }
$deviceLines = @(& $adb devices)
$escapedSerial = [regex]::Escape($androidTestSerial)
if (@($deviceLines | Where-Object { $_ -match "^$escapedSerial\s+device$" }).Count -ne 1) { throw 'The selected Android test target is not uniquely connected and ready.' }
& $adb -s $androidTestSerial install -r $finalApk.FullName
if ($LASTEXITCODE -ne 0) { throw 'Final APK installation on the dedicated target failed.' }
& $adb -s $androidTestSerial shell pm path com.xiaoyiai.courtofshadows
if ($LASTEXITCODE -ne 0) { throw 'Installed Android package cannot be resolved.' }
~~~

Then verify:

- touch selection for the last investigation and policy items;
- 100% and 150% text;
- background and snow;
- BGM handoff;
- back/rollback behavior;
- loading a winter save.

If no dedicated Android runtime is available, mark every Android interaction above—not just audio—as unverified and leave this plan incomplete. Package-only validation may be reported separately, but it is not a substitute for touch, back/rollback, save/load, rendering, or playback evidence.

Steps 9 and 10 are verification-only and must not patch either detached build worktree. If package verification or either smoke test exposes a source, prose, asset, or test defect, return to the feature worktree, add a focused RED assertion, implement and commit the fix, and restart Task 12 from Step 2—including a new independent review, new small/touch evidence, and newly named baseline/final build directories. All artifacts and review conclusions from the superseded HEAD are invalid.

- [ ] **Step 11: Prove final clean state and deliver evidence**

Reach this step only when Steps 2–10 required no further modification after `$finalCommit` was captured. Fail closed unless the feature branch, detached final worktree, reviewed commit, and packaged artifacts all bind to that same commit:

~~~powershell
$dirty = @(git status --porcelain)
if ($dirty.Count -ne 0) { throw "Feature branch is not clean: $($dirty -join '; ')" }
$currentHead = (git rev-parse HEAD).Trim()
if ($currentHead -ne $finalCommit) { throw 'Feature HEAD changed after final artifacts were built; restart Task 12 Step 2.' }
if ($currentHead -ne $reviewHead) { throw 'Feature HEAD is not the exact reviewed commit.' }
if ((git -C $finalRoot rev-parse HEAD).Trim() -ne $finalCommit) { throw 'Detached final worktree is not bound to finalCommit.' }
$leftoverDetachedKeys = @(
  (Join-Path $baselineRoot 'android.keystore'), (Join-Path $baselineRoot 'bundle.keystore'),
  (Join-Path $finalRoot 'android.keystore'), (Join-Path $finalRoot 'bundle.keystore')
) | Where-Object { Test-Path -LiteralPath $_ }
if ($leftoverDetachedKeys.Count -ne 0) { throw "Temporary detached-worktree keystores remain: $($leftoverDetachedKeys -join ', ')" }
if ((git rev-list -n 1 governance-winter-baseline).Trim() -ne $functionalBaselineHead) { throw 'Fixture-proven functional baseline tag moved during verification.' }
git log --oneline "${functionalBaselineHead}..HEAD"
git diff --stat "${functionalBaselineHead}..HEAD"
git diff --check "${functionalBaselineHead}..HEAD"
if ($LASTEXITCODE -ne 0) { throw 'Final functional-range whitespace check failed.' }
if ((git rev-list -n 1 governance-winter-package-baseline).Trim() -ne $baselineHead) { throw 'Immutable package-baseline tag moved during verification.' }
~~~

Expected: clean branch, no untracked production artifacts, review Ready, and all evidence fresh.

**Final asset report:**

- New required art: game/images/bg_winter_granary.webp, exact bytes reported.
- Music: no new file; reused winter_wind, market_bustle, tension, castle_calm.
- SFX: no new file; reused existing door, crowd, bell, page, and coin sounds.
- Portraits: no new file.
- Animation: no new file; reused weather_snow and ordinary transitions.
- UI: no new image; chapter icon is text fallback "幕".
- Font: report exact byte change from new glyph subsetting.
- Signing: no keystore is added to source or package; both detached builds use the same hash-pinned temporary keys and delete their copies in finally.
- Packages: report exact Windows and Android byte deltas against governance-winter-package-baseline, while code review and functional diffs remain against governance-winter-baseline.

---

## Completion Checklist

- [ ] 3.9.2 feedback work is committed, merged, and verified before feature work.
- [ ] governance-winter-baseline is immutable and reproducible.
- [ ] governance-winter-package-baseline is immutable, source-clean, and shares the final version/About/Privacy/README/Android metadata while retaining the pre-feature code.
- [ ] Three real continuation archives, one real famine-completion archive, and one synthetic neutral compatibility archive all pass manifest hash/signature/load checks.
- [ ] The interlude appears only after southern/main Chapter 1 and before Chapter 2.
- [ ] Direct Chapter 2 entry writes neutral delegation before autosave/snapshot.
- [ ] Blank winter replay runs bootstrap, uses deterministic defaults, and preserves the true hidden slot.
- [ ] State precedence is centralized and idempotent.
- [ ] Corrupt completed state delegates neutrally without re-inferring legacy; a valid active in-interlude save survives load, while downstream reads and external re-entry expose/normalize it as neutral delegation.
- [ ] All 12 investigation orders execute through production menus and normalize to six pairs; real mid-menu saves resume correctly.
- [ ] All 36 active combinations and delegation execute through production routing.
- [ ] The two unvisited investigations receive explicit low-confidence reports, and at most one deterministic mitigation applies.
- [ ] Every result has a beneficiary, a bearer, and a fixed later echo.
- [ ] No main stats, relationships, endings, or battle inputs change.
- [ ] All old merchant/famine consumers use the centralized context.
- [ ] Harrenhall factions react to the saved policy and Karl reframes the same offer, while all original choices, conditions, prices, state writes, and targets remain unchanged.
- [ ] Every Chapter 5 claim about current grain or duration uses the winter context; construction/refill orders and all baseline bonus guards remain unchanged.
- [ ] New routes never trigger the old "无人饿死" heroic text.
- [ ] All exits clear winter presentation and reach Chapter 2.
- [ ] The actual music channel plays castle_calm after the Chapter 2 cinematic.
- [ ] All active visible paths are 11,000–14,000 Chinese characters.
- [ ] The pre-choice brief remains 1–2 minutes.
- [ ] Every prose scene and every downstream echo was generated in its own fresh verified claude-opus-4-6 session; each raw result was approved before integration.
- [ ] small/touch 100% and 150% screenshots are inspected at original detail.
- [ ] Exactly one new shipping image exists and is within 1.2 MiB.
- [ ] No new music, SFX, portrait, animation, or UI image exists.
- [ ] Release metadata is 3.10, released RPYC count is 56, Android versionCode is exactly 2,000,000,000, and the new v3.25/store-v3.10 copy is approved.
- [ ] Both detached Android builds use the exact verified release keystores, emit the expected signer certificate, and leave no copied keystore behind or tracked.
- [ ] Windows and Android package growth against governance-winter-package-baseline are each within 2.0 MiB.
- [ ] The packaged Windows build uses an isolated savedir, and all claimed Android interactions are proven on a dedicated emulator/test device rather than inferred from package inspection.
- [ ] Full Python, Ren'Py, lint, narrative, font, old-save, and package gates pass freshly.
- [ ] Independent review reports no Critical or Important issue.

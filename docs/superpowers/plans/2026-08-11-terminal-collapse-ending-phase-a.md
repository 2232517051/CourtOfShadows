# Terminal Collapse Ending Phase A Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Freeze a real pre-change final-tactics save, implement the route-aware terminal-collapse rule with focused regression coverage, and present three verified isolated Claude Opus 4.6 copy bundles for blind user selection before any visible finale prose changes.

**Architecture:** `game/difficulty.rpy` remains the sole pure source of finale routes, terminal-collapse classification, and reachable battle outcomes; `game/balance.rpy` consumes that source without inventing reachability; `game/test_game.rpy` locks the pure result graph and legacy-safe wrappers. A separate ignored evidence lane preserves the real old save and three raw model outputs. This phase deliberately stops before `game/chapter5.rpy` or `game/endings_expansion.rpy` changes; after the user selects one raw bundle, a second exact-literal plan will integrate runtime guards, death copy, save migration checks, and final release gates.

**Tech Stack:** Ren'Py 8.5.2 / Python 3, Ren'Py testsuites, Windows PowerShell 5.1, Git, Claude Code locked to `claude-opus-4-6` through the verified local launcher.

## Global Constraints

- The approved design is `docs/superpowers/specs/2026-08-11-terminal-collapse-ending-design.md`, physical SHA-256 `09AAC47CEC9B8FAEE0C930ED6759EDCE88F37B2B73E376196D4D70C44AE390CE`, committed at `bdad1441d9731fbfac3e1b90654dbe888f354296`.
- The unrelated untracked plan `docs/superpowers/plans/2026-08-09-winter-interlude-narrative-delivery.md` must remain byte-identical at SHA-256 `0F39B5F5ACE1D4666DD146863CABDF398B031F5666C29AE337CEB89796E4276C`; never stage, edit, delete, or incorporate it.
- In the shared implementation worktree, Phase A may modify exactly `game/difficulty.rpy`, `game/balance.rpy`, and `game/test_game.rpy`. Task 1's explicitly disposable detached baseline worktree may carry only its two temporary fixture edits and must be destroyed after evidence capture. Neither worktree may modify `game/chapter5.rpy`, `game/endings_expansion.rpy`, any visible production prose, persistent ending key, achievement ID, asset, font, store copy, version, or package metadata.
- The intermediate rules commit is not shippable or merge-ready by itself: it intentionally precedes the runtime guard and approved death copy. Do not run Final, build a release, merge, or advertise the player bug as fixed at the Phase A hard stop.
- Generate the old save before the first tracked game-file edit. Generate it from the exact approved-design commit in a disposable detached worktree, using a unique external save directory. Never regenerate it from changed code.
- All evidence under `.superpowers/sdd/terminal-collapse-ending/` must be ignored, must never be staged, and must survive through Phase B review. Do not clean or overwrite evidence to obtain a better result.
- Every Ren'Py runner call uses a unique external `SaveDir`; `Run-RenPySuite.ps1` exits its host, so invoke it through a fresh child `powershell.exe` and check the real exit code immediately.
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
$DesignCommit = 'bdad1441d9731fbfac3e1b90654dbe888f354296'
$DesignSha256 = '09AAC47CEC9B8FAEE0C930ED6759EDCE88F37B2B73E376196D4D70C44AE390CE'
$UnrelatedPlan = 'docs/superpowers/plans/2026-08-09-winter-interlude-narrative-delivery.md'
$UnrelatedSha256 = '0F39B5F5ACE1D4666DD146863CABDF398B031F5666C29AE337CEB89796E4276C'
$ThisPlan = 'docs/superpowers/plans/2026-08-11-terminal-collapse-ending-phase-a.md'

if ((git log -1 --format=%s) -cne 'docs: plan terminal collapse phase one') {
    throw 'HEAD is not the approved Phase A plan commit.'
}
if ((git rev-parse HEAD^) -cne $DesignCommit) {
    throw 'Phase A plan parent is not the approved design commit.'
}
$PlanCommitPaths = @(git diff-tree --no-commit-id --name-only -r HEAD)
if ($PlanCommitPaths.Count -ne 1 -or $PlanCommitPaths[0] -cne $ThisPlan) {
    throw 'Phase A plan commit scope is not exactly the plan file.'
}
if ((Get-FileHash -Algorithm SHA256 'docs/superpowers/specs/2026-08-11-terminal-collapse-ending-design.md').Hash -cne $DesignSha256) {
    throw 'Approved design bytes drifted.'
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

Expected: all assertions pass; the only status entry is the preserved unrelated plan.

- [ ] **Step 2: Verify the trusted SDK and runner parser before evidence work**

```powershell
if ([string]::IsNullOrWhiteSpace($env:RENPY_SDK)) {
    throw 'RENPY_SDK is not set.'
}
$RenPyExe = Join-Path $env:RENPY_SDK 'renpy.exe'
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
$LauncherProbe = Start-Process -FilePath $RenPyExe -ArgumentList '--version' -Wait -PassThru
if ($LauncherProbe.ExitCode -ne 0) {
    throw ('RenPy GUI launcher version probe failed with exit ' + $LauncherProbe.ExitCode + '.')
}

# renpy.exe is a Windows GUI-subsystem launcher, so direct invocation does not
# reliably update $LASTEXITCODE or attach its version text to WinPS 5.1. Use
# the bundled console interpreter against the same SDK entrypoint for the
# exact version line, and bind it to the official version declaration.
$RenPyConsole = Join-Path $env:RENPY_SDK 'lib\py3-windows-x86_64\python.exe'
$RenPyEntry = Join-Path $env:RENPY_SDK 'renpy.py'
$RenPyVersionFile = Join-Path $env:RENPY_SDK 'renpy\vc_version.py'
foreach ($RequiredSdkFile in @($RenPyConsole, $RenPyEntry, $RenPyVersionFile)) {
    if (-not (Test-Path -LiteralPath $RequiredSdkFile -PathType Leaf)) {
        throw ('Trusted SDK version input is missing: ' + $RequiredSdkFile)
    }
}
$VersionOutput = @(& $RenPyConsole $RenPyEntry --version 2>&1)
$VersionExit = $LASTEXITCODE
if ($VersionExit -ne 0) {
    throw ('RenPy console version probe failed with exit ' + $VersionExit + '.')
}
$VersionLines = @($VersionOutput | ForEach-Object { [string]$_ })
if ($VersionLines.Count -ne 1 -or $VersionLines[0] -cne "Ren'Py 8.5.2.26010301") {
    throw ('Unexpected RenPy version output: ' + ($VersionLines -join '; '))
}
$StrictUtf8 = New-Object System.Text.UTF8Encoding($false, $true)
$VersionSource = [IO.File]::ReadAllText($RenPyVersionFile, $StrictUtf8)
$VersionAssignments = [regex]::Matches($VersionSource, "(?m)^version = '([^']+)'\r?$")
$OfficialAssignments = [regex]::Matches($VersionSource, '(?m)^official = (True|False)\r?$')
if ($VersionAssignments.Count -ne 1 -or
    $VersionAssignments[0].Groups[1].Value -cne '8.5.2.26010301' -or
    $OfficialAssignments.Count -ne 1 -or
    $OfficialAssignments[0].Groups[1].Value -cne 'True') {
    throw 'RenPy official version declaration does not match 8.5.2.26010301.'
}
```

Expected: Windows PowerShell parser errors `0`; the GUI launcher exits `0`; the same SDK's console entrypoint reports exactly `Ren'Py 8.5.2.26010301`; and `renpy/vc_version.py` declares the same official version.

- [ ] **Step 3: Establish the ignored evidence root without touching tracked scope**

```powershell
$EvidenceRoot = Join-Path $ProjectRoot '.superpowers\sdd\terminal-collapse-ending'
$IgnoreProbe = '.superpowers/sdd/terminal-collapse-ending/ignore-probe.txt'
git check-ignore -q $IgnoreProbe
if ($LASTEXITCODE -ne 0) { throw 'Terminal-collapse evidence root is not ignored.' }
[IO.Directory]::CreateDirectory($EvidenceRoot) | Out-Null
```

Do not stage the directory. Any small human-authored evidence manifest must be created with `apply_patch`; engine logs, screenshots, binary saves, and launcher outputs may be copied/generated by their owning tools.

---

## Task 1: Preserve a real pre-change final-tactics save

**Files:**

- Temporary-only modify in detached worktree: `game/script.rpy:14`
- Temporary-only create in detached worktree: `game/zz_terminal_collapse_legacy_fixture.rpy`
- Preserve ignored binary master: `.superpowers/sdd/terminal-collapse-ending/legacy/mother/1-1-*.save` (the exact single engine-generated filename selected in Step 4)
- Preserve ignored evidence: `.superpowers/sdd/terminal-collapse-ending/legacy/baseline-evidence.md`

- [ ] **Step 1: Create and verify a disposable detached baseline worktree**

```powershell
$ErrorActionPreference = 'Stop'
$ProjectRoot = (Resolve-Path -LiteralPath '.').Path
$DesignCommit = 'bdad1441d9731fbfac3e1b90654dbe888f354296'
$EvidenceRoot = Join-Path $ProjectRoot '.superpowers\sdd\terminal-collapse-ending'
$RenPyExe = Join-Path $env:RENPY_SDK 'renpy.exe'
if (-not (Test-Path -LiteralPath $RenPyExe -PathType Leaf)) {
    throw 'RENPY_SDK does not contain renpy.exe.'
}
$BaselineRoot = Join-Path ([IO.Path]::GetTempPath()) ('cos-terminal-collapse-baseline-' + [Guid]::NewGuid().ToString('N'))
$BaselineSaveDir = Join-Path ([IO.Path]::GetTempPath()) ('cos-terminal-collapse-old-save-' + [Guid]::NewGuid().ToString('N'))
if (Test-Path -LiteralPath $BaselineRoot) { throw 'Baseline worktree path already exists.' }
if (Test-Path -LiteralPath $BaselineSaveDir) { throw 'Baseline save path already exists.' }
git worktree add --detach $BaselineRoot $DesignCommit
if ($LASTEXITCODE -ne 0) { throw 'Could not create detached baseline worktree.' }
if ((git -C $BaselineRoot rev-parse HEAD) -cne $DesignCommit) {
    throw 'Detached worktree is not at the approved design commit.'
}
if (@(git -C $BaselineRoot status --short).Count -ne 0) {
    throw 'Detached baseline worktree did not start clean.'
}
```

- [ ] **Step 2: Add the disposable baseline driver with `apply_patch`**

Insert this one line immediately after `label start:` in the detached worktree's `game/script.rpy`:

```renpy
    jump terminal_collapse_legacy_generation_driver
```

Create `game/zz_terminal_collapse_legacy_fixture.rpy` in that detached worktree with exactly:

```renpy
label terminal_collapse_legacy_generation_driver:
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
    jump ending_iron_lord
```

This is test-only generation code in a disposable baseline worktree. It must never be copied, committed, or applied to the implementation worktree.

- [ ] **Step 3: Launch the unchanged baseline visibly and save at the exact menu**

Use the Windows-native quoting helper and a visible Ren'Py process:

```powershell
function Quote-NativeArgument([string]$Value) {
    if ($Value -notmatch '[\s"]') { return $Value }
    $Quoted = [regex]::Replace($Value, '(\\*)"', '$1$1\"')
    $Quoted = [regex]::Replace($Quoted, '(\\+)$', '$1$1')
    return '"' + $Quoted + '"'
}

[IO.Directory]::CreateDirectory($BaselineSaveDir) | Out-Null
$ArgumentLine = "$(Quote-NativeArgument $BaselineRoot) --savedir $(Quote-NativeArgument $BaselineSaveDir)"
$BaselineProcess = Start-Process -FilePath $RenPyExe -ArgumentList $ArgumentLine -PassThru
$BaselinePid = $BaselineProcess.Id
"baseline_pid=$BaselinePid"
```

In the visible window, perform exactly:

1. Start a new game; the disposable `start` jump enters the fixture.
2. Choose `截断补给线——让他们饿三天再打`.
3. Choose `亲自率领前锋出击`.
4. Choose `记住这一切，继续前进`.
5. At the final-tactics menu, verify both `正面强攻，以气势压倒对方` and `采用迂回战术，先攻击敌军侧翼` are visible. Do not select either.
6. Open the normal save UI, save to logical slot `1`, return to the menu, and quit normally.

Before accepting the menu state, verify the current diminishing-return arithmetic from the unchanged baseline source: supply-line applies raw `intrigue +5` to 52 and yields 55; personal-vanguard applies raw `power +5` to 56 and yields 59; remember-and-continue applies raw `power +2` to 59 and yields 60. Therefore the final fixture state must report `intrigue=55`, `power=60`, and `_iron_prepared=True`. Any different value is a hard stop; do not save a merely similar menu state.

Then wait for the exact launched process:

```powershell
$BaselineProcess.WaitForExit()
$BaselineExitCode = $BaselineProcess.ExitCode
if ($BaselineExitCode -ne 0) { throw "Baseline RenPy exited $BaselineExitCode." }
if (Get-Process -Id $BaselinePid -ErrorAction SilentlyContinue) {
    throw 'Baseline RenPy PID is still alive.'
}
```

- [ ] **Step 4: Freeze the single engine save as a read-only mother artifact**

```powershell
$SaveCandidates = @(
    Get-ChildItem -LiteralPath $BaselineSaveDir -File |
        Where-Object { $_.Name -like '1-1-*.save' }
)
if ($SaveCandidates.Count -ne 1) {
    throw ('Expected exactly one page-1/slot-1 save, found ' + $SaveCandidates.Count)
}
$SourceSave = $SaveCandidates[0]
$MotherDir = Join-Path $EvidenceRoot 'legacy\mother'
[IO.Directory]::CreateDirectory($MotherDir) | Out-Null
$MotherSave = Join-Path $MotherDir $SourceSave.Name
if (Test-Path -LiteralPath $MotherSave) {
    throw 'Mother save already exists; do not overwrite evidence.'
}
Copy-Item -LiteralPath $SourceSave.FullName -Destination $MotherSave
$SourceHash = (Get-FileHash -Algorithm SHA256 $SourceSave.FullName).Hash
$MotherHash = (Get-FileHash -Algorithm SHA256 $MotherSave).Hash
if ($SourceHash -cne $MotherHash) { throw 'Mother save copy hash mismatch.' }
(Get-Item -LiteralPath $MotherSave).IsReadOnly = $true
if (-not (Get-Item -LiteralPath $MotherSave).IsReadOnly) {
    throw 'Mother save is not read-only.'
}
git check-ignore -q $MotherSave
if ($LASTEXITCODE -ne 0) { throw 'Mother save is not ignored.' }
```

- [ ] **Step 5: Record literal baseline evidence and clean only the verified disposable worktree**

Create `.superpowers/sdd/terminal-collapse-ending/legacy/baseline-evidence.md` with `apply_patch`, inserting the observed literal values for:

- `baseline_commit` = `bdad1441d9731fbfac3e1b90654dbe888f354296`
- Ren'Py version reported in Task 0
- `baseline_worktree`
- `baseline_savedir`
- `engine_filename`
- `byte_count`
- `sha256`
- logical slot `1`
- choices `supply-line -> personal-vanguard -> remember-and-continue`
- final menu facts `_iron_prepared=True`, frontal visible, flanking visible
- `pid` and `exit_code=0`

Copy the baseline `log.txt` into the same ignored evidence directory and record its SHA-256. Re-read the Markdown and both hashes before cleanup.

```powershell
$TempRoot = [IO.Path]::GetFullPath([IO.Path]::GetTempPath())
$ResolvedBaselineRoot = [IO.Path]::GetFullPath($BaselineRoot)
if (-not $ResolvedBaselineRoot.StartsWith($TempRoot, [StringComparison]::OrdinalIgnoreCase)) {
    throw 'Refusing to remove a non-temporary baseline worktree.'
}
if (Get-Process -Id $BaselinePid -ErrorAction SilentlyContinue) {
    throw 'Refusing cleanup while baseline RenPy is alive.'
}
git worktree remove --force $ResolvedBaselineRoot
if ($LASTEXITCODE -ne 0) { throw 'Could not remove disposable baseline worktree.' }
git worktree prune
if (Test-Path -LiteralPath $ResolvedBaselineRoot) {
    throw 'Disposable baseline worktree still exists.'
}
```

Do not delete `$BaselineSaveDir`, the mother, or its evidence until Phase B review is complete.

---

## Task 2: Implement the pure collapse rule and route-aware reachability

**Files:**

- Modify: `game/difficulty.rpy:101-338`
- Modify: `game/balance.rpy:15-98`
- Test: `game/test_game.rpy:127-254`
- Test migration: `game/test_game.rpy:894-968`

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

```powershell
$ProjectRoot = (Resolve-Path -LiteralPath '.').Path
$RedSaveDir = Join-Path ([IO.Path]::GetTempPath()) ('cos-terminal-collapse-rules-red-' + [Guid]::NewGuid().ToString('N'))
& powershell.exe -NoProfile -File .\Tools\Run-RenPySuite.ps1 -ProjectRoot $ProjectRoot -SaveDir $RedSaveDir -Mode Suite -Suite test_terminal_collapse_rules -Expect FAILED -ExpectedPattern 'is_terminal_resistance_collapse' -TimeoutSeconds 120
if ($LASTEXITCODE -ne 0) { throw 'Expected RED was not the named missing collapse helper.' }
```

Expected: the Ren'Py suite fails for the missing `is_terminal_resistance_collapse` helper, while the runner itself exits `0` because that exact RED was required. Copy the runner evidence into `.superpowers/sdd/terminal-collapse-ending/rules-red/`, record its SHA-256, and do not edit the log.

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

- [ ] **Step 9: Run the focused GREEN suites once each**

```powershell
$ProjectRoot = (Resolve-Path -LiteralPath '.').Path
function New-TerminalCollapseSaveDir([string]$Name) {
    return Join-Path ([IO.Path]::GetTempPath()) ("cos-terminal-collapse-{0}-{1}" -f $Name, [Guid]::NewGuid().ToString('N'))
}

& powershell.exe -NoProfile -File .\Tools\Run-RenPySuite.ps1 -ProjectRoot $ProjectRoot -SaveDir (New-TerminalCollapseSaveDir 'rules-green') -Mode Suite -Suite test_terminal_collapse_rules -Expect PASSED -TimeoutSeconds 120
if ($LASTEXITCODE -ne 0) { throw 'test_terminal_collapse_rules failed.' }

& powershell.exe -NoProfile -File .\Tools\Run-RenPySuite.ps1 -ProjectRoot $ProjectRoot -SaveDir (New-TerminalCollapseSaveDir 'catalog-green') -Mode Suite -Suite test_ending_catalog -Expect PASSED -TimeoutSeconds 120
if ($LASTEXITCODE -ne 0) { throw 'test_ending_catalog failed.' }

& powershell.exe -NoProfile -File .\Tools\Run-RenPySuite.ps1 -ProjectRoot $ProjectRoot -SaveDir (New-TerminalCollapseSaveDir 'balance-green') -Mode Suite -Suite test_balance_ending_report -Expect PASSED -TimeoutSeconds 120
if ($LASTEXITCODE -ne 0) { throw 'test_balance_ending_report failed.' }

& powershell.exe -NoProfile -File .\Tools\Run-RenPySuite.ps1 -ProjectRoot $ProjectRoot -SaveDir (New-TerminalCollapseSaveDir 'winter-invariance-green') -Mode Suite -Suite test_winter_interlude_ending_invariance -Expect PASSED -TimeoutSeconds 180
if ($LASTEXITCODE -ne 0) { throw 'test_winter_interlude_ending_invariance failed.' }
```

Expected: each command has real exit code `0`, reports `PASSED`, and retains a unique runner evidence path. Do not repeat a passing suite on the same bytes.

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
```

Asset report for this commit: art `not required`, music `not required`, sound effects `not required`, animation `not required`, UI `not required`; no binary or package-size change.

---

## Task 3: Generate three isolated raw Opus copy bundles

**Files:**

- Read: `CANON.md`
- Read: `CLAUDE.md`
- Read: `docs/writing-style/INDEX.md`
- Read context only: `game/chapter5.rpy:2387-2469, 6068-6194, 6396-6505`
- Read context only: `game/endings_expansion.rpy:204-249`
- Create ignored prompts/results only: `.superpowers/sdd/terminal-collapse-ending/copy/run-01/`, `run-02/`, `run-03/`
- Create ignored blind map only: `.superpowers/sdd/terminal-collapse-ending/copy/blind-map.md`

- [ ] **Step 1: Reconfirm the mandatory three-candidate branch**

Read `CANON.md`, `CLAUDE.md`, and `docs/writing-style/INDEX.md` in full. Assert that the style index still reports seed maturity and no active approved examples. If an active approved corpus now exists, stop and revise this plan before generating anything; do not silently switch workflows.

Verify that `game/chapter5.rpy` and `game/endings_expansion.rpy` remain unmodified:

```powershell
$ErrorActionPreference = 'Stop'
$ProjectRoot = (Resolve-Path -LiteralPath '.').Path
$EvidenceRoot = Join-Path $ProjectRoot '.superpowers\sdd\terminal-collapse-ending'
$StrictUtf8 = New-Object System.Text.UTF8Encoding($false, $true)
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
- Real old-save validation: copy the read-only mother into two fresh external SaveDirs, verify all three hashes, visibly load the frontal and flanking copies, record screenshots/log/PID/exit code, and prove both lose before branch mutation. Never load the mother directly.
- Final tests exactly once on the final tracked SHA: focused suites, `python -B -m unittest discover -s Tools -v`, portrait/narration/show/canon/AI-smell/release/font checks, `test_terminal_collapse_ending`, Full, Lint, process cleanup, diff scope, and independent Spec/Standards review.
- Final asset report: no new art/music/SFX/animation/UI; reuse existing `castle_exterior`, `battlefield`, black scene, and `war_drums.ogg`; measure actual font/package delta after approved text enters.

Phase B must end with the last tracked implementation commit before Final and independent reviews; no tracked evidence commit may follow those gates.

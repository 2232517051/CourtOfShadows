# Player Feedback Completion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Close the remaining continuity, portrait, Ingrid-ending, prose, and runtime-verification gaps in the current player-feedback update.

**Architecture:** Preserve the existing ending labels, persistent keys, save-compatible marriage state, and current uncommitted player-feedback rewrite. Add source-contract tests before each fix, use a fresh Claude Code session on `claude-opus-4-6` for new or rewritten game prose, and keep mechanical portrait/test fixes separate from prose integration.

**Tech Stack:** Ren'Py 8.5.2, Python 3 `unittest`, Claude Code with model `claude-opus-4-6`, existing project scanners and Ren'Py lint/test harness.

## Global Constraints

- Preserve every pre-existing worktree change; do not reset, restore, stash, or overwrite unrelated hunks.
- Do not move or rename ending labels and do not change `persistent.endings_seen` keys.
- Preserve `marriage_proposal_open`, `marriage_route`, and `marriage_warm` semantics and old-save compatibility.
- Companion resolution remains mutually exclusive. A reachable married route must account for Ingrid even in the truth-declined, Borgia, and sea endings.
- New game prose must be generated in a fresh Claude Code session after selecting `claude-opus-4-6`. Give it only necessary current scene/canon facts. Do not use `writing-game-copy`, rejected drafts, or style constraints.
- The user waived raw-draft review for this task. Integrate the Claude Code result, then show only the resulting in-game copy.
- Follow TDD: add a focused source-contract test, run it and observe the expected failure, then change production script and re-run GREEN.
- Reuse existing portraits, backgrounds, music, and sound effects. No new art, music, SFX, animation, UI asset, or package-size increase is required.

---

### Task 1: Correct the Remaining Portrait-Clear Order

**Files:**
- Modify: `Tools/test_player_feedback_regressions.py`
- Modify: `game/chapter5.rpy`

**Interfaces:**
- Consumes: existing `hide servant_generic_img`, `hide_all_chars()`, and representative portrait tags.
- Produces: the envoy is hidden before departure narration, and the last negotiating representative is cleared before the peace montage.

- [ ] **Step 1: Change the envoy regression to require hide-before-narration**

Replace the current regex assertion with an ordered source check that requires `hide servant_generic_img with dissolve` immediately before the narration beginning `"送走了男爵的密使后`.

- [ ] **Step 2: Add a failing regression for the peace montage clear**

Add a test requiring `$ hide_all_chars()` after the final `baron_rep` line and before `"又一轮讨价还价`.

- [ ] **Step 3: Run RED**

Run:

```powershell
python -m unittest Tools.test_player_feedback_regressions.PortraitContractTests -v
```

Expected: the two new ordering assertions fail against the current source.

- [ ] **Step 4: Apply the minimal ordering fixes**

Move the existing envoy hide above the departure narration. Insert `$ hide_all_chars()` between the final representative dialogue and the peace montage. Do not rewrite prose in this task.

- [ ] **Step 5: Run GREEN**

Run the focused class again and require all tests to pass.

---

### Task 2: Lock the Missing Causality and Ingrid Ending Contracts

**Files:**
- Modify: `Tools/test_player_feedback_regressions.py`

**Interfaces:**
- Consumes: `ending_peoples_lord`, `truth_humble_epilogue`, `ending_borgia`, and `ending_sea`.
- Produces: failing contracts that prove the current causal contradiction and three missing married outcomes.

- [ ] **Step 1: Add the People's Lord causality test**

Require the ending to retain the established rear-army withdrawal and reject the sentence `你击退了每一支试图劫掠你领地的军队`.

- [ ] **Step 2: Add three Ingrid reachability tests**

Require `marriage_route`/Ingrid handling in the truth-declined, Borgia, and sea ending bodies. For each, require both warm and cold marriage outcomes or an explicit shared married outcome followed by a `marriage_warm` split.

- [ ] **Step 3: Run RED**

Run:

```powershell
python -m unittest Tools.test_player_feedback_regressions -v
```

Expected: failures identify the direct-defeat claim and all three missing Ingrid endings.

---

### Task 3: Generate and Integrate Final Opus Copy through Claude Code

**Files:**
- Modify: `game/chapter3.rpy`
- Modify: `game/chapter4.rpy`
- Modify: `game/chapter5.rpy`
- Modify: `game/endings_expansion.rpy`
- Modify: `Tools/test_player_feedback_regressions.py` only if integration requires structural, non-verbatim assertions.
- Regenerate: `game/msyh.ttf` only through `prepare_release.py` after prose integration.

**Interfaces:**
- Consumes: the current scene variables and canon facts, plus Task 2's failing contracts.
- Produces: final in-game copy for marriage exit/explanation, all reachable Ingrid married endings, and the realistic People's Lord ending.

- [ ] **Step 1: Verify Claude Code authentication and model selection**

Start a fresh, non-persistent Claude Code session and select `claude-opus-4-6` (the non-interactive `--model claude-opus-4-6` form is the CLI equivalent of `/model claude-opus-4-6`). Verify the initialization event reports the exact model before accepting its result.

- [ ] **Step 2: Call Claude Code once per isolated copy task**

Use Claude Code safe mode, disable tools and prompt suggestions, disable session persistence, and replace the coding-agent prompt with the neutral instruction `Answer the user directly.`. Run each approved fact prompt in its own process:

```powershell
claude.exe --safe-mode --system-prompt "Answer the user directly." --prompt-suggestions false --model claude-opus-4-6 --effort max --tools "" --no-session-persistence -p --output-format stream-json --include-partial-messages --verbose "<necessary facts only>"
```

Save the exact terminal result in ignored `.superpowers/sdd/` evidence, verify the initialization model, assistant-event model, `stop_reason`, and text content, and do not display the raw response to the user.

- [ ] **Step 3: Integrate only canon-compatible prose**

Map the returned scenes onto existing Ren'Py labels and variable names. Preserve all state assignments and choice guards. Add Ingrid outcomes to truth-declined, Borgia, and sea without teleporting her, inventing children, or erasing her northern political identity.

- [ ] **Step 4: Run GREEN**

Run:

```powershell
python -m unittest Tools.test_player_feedback_regressions -v
python Tools/test_story_timeline.py -q
python Tools/scan_canon.py
```

Require all focused contracts, timeline tests, and canon gates to pass.

- [ ] **Step 5: Refresh the font**

Run `python prepare_release.py`. If the font changes, retain the generated `game/msyh.ttf`; then run the command again and require exit `0`.

---

### Task 4: Full Verification and Review

**Files:**
- Modify only if a gate exposes a regression in files already in scope.

**Interfaces:**
- Consumes: Tasks 1-3.
- Produces: fresh completion evidence and a reviewed diff.

- [ ] **Step 1: Run Python and source gates**

Run the focused player-feedback suite, full `Tools/test_*.py` discovery, release regressions, portrait scanner, explicit narration-overlap scan for every changed `.rpy`, canon scan, timeline scan, and `git diff --check`.

- [ ] **Step 2: Run Ren'Py lint and diagnose the test harness**

Run lint. Run `renpy.exe . test` with captured output and process diagnostics; do not accept a silent timeout as success. If it hangs again, identify the blocking point before claiming completion.

- [ ] **Step 3: Review spec and code quality**

Use a fresh reviewer to inspect the complete worktree diff for state-contract regressions, missing married endings, portrait lifetime, canon continuity, and asset references.

- [ ] **Step 4: Record the completed diff without committing**

Leave the user's working tree uncommitted unless the user separately asks for a commit. Record that existing assets were reused and that no new art, music, SFX, animation, UI, or package-size increase is required.

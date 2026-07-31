# 3.9.2 Critical Regression Fixes Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` to execute this plan one task at a time. Every implementation task must use `superpowers:test-driven-development` and must be committed before the next task begins.

**Goal:** Remove the five release-blocking 3.9.2 regressions: premature truth knowledge, a zero-option finale state, chapter-select starts that skip new-run setup, overflowing mobile finale choices, inert accessibility settings, and the 13 player-visible doubled percent signs.

**Architecture:** Give each concept one authoritative path. Narrative knowledge is represented by three explicit evidence flags; finale visibility is computed by one pure route resolver and consumed by both the menu and fallback logic; every formal chapter entry calls one idempotent new-run bootstrap label; the small/touch choice screen owns its scrolling behavior; accessibility controls use Ren'Py's built-in font-size and high-contrast preferences so the engine's renderer is the consumer. Keep the deprecated broad truth flag only as a save-compatibility input, never as a gameplay gate.

**Tech Stack:** Ren'Py 8.5.2, Ren'Py script/Python, Ren'Py testcase DSL, Python 3 static regression checks, PowerShell test commands.

## Global Constraints

- Work on the current clean project checkout and preserve unrelated user changes.
- Use RED-GREEN-REFACTOR: add or strengthen the covering test first, run it and capture the expected failure, then edit production code.
- Commit each task as a small thematic commit; do not mix any 3.10 timeline, pacing, packaging, store-copy, or ending-test modernization work into these commits.
- `true_killer_known` remains readable only for old-save migration. New gameplay conditions must use `father_poison_method_known`, `father_poison_executor_known`, or `father_murder_mastermind_known`, according to what the surrounding text actually claims.
- An old save produced by the chapter-three bug must not be promoted to mastermind knowledge merely because `true_killer_known` is true. Legacy mastermind knowledge may be inferred only when a reliable chapter-four provenance flag is also present.
- The finale route resolver must apply every per-option visibility rule before deciding whether the fall ending is needed. At least one visible finale option must always remain. The sea route may intentionally coexist with the fall route.
- Every formal chapter entry, including prologue and the southern side chapter, must call the same new-run bootstrap. It must execute exactly once in a new run and become a no-op during normal chapter progression; loading any existing save must suppress it so inventory and NG+ state are never reset.
- On small/touch variants, all seven two-line finale choices must be reachable without shrinking core choice text below the existing small-GUI size.
- Accessibility settings must use Ren'Py's renderer-backed `Preference("font size", ...)` and `Preference("high contrast text", ...)` actions, affect dialogue and choice UI immediately, and be reachable from the normal Preferences page; no setting may remain a cosmetic toggle with no consumer.
- Only the 13 player-visible doubled percent literals may change. Python `%` formatting escapes such as `"%d%%" % value` must remain intact.
- Any `.rpy` change requires `..\renpy.exe . lint`, `python scan_missing_portraits.py`, and `python scan_narration_overlap.py`. Portrait and narration scanners must report zero.
- Any changed screen-text interpolation requires a real small/touch render, screenshot capture, and visual inspection.
- Before declaring the batch complete, run the complete walkthrough testcase and inspect `git diff --check` plus a final broad code review.

---

## Task 1: Split truth knowledge and make finale route selection total

**Files:**

- Modify: `game/characters.rpy`
- Modify: `game/chapter3.rpy`
- Modify: `game/chapter4.rpy`
- Modify: `game/chapter4_prince.rpy`
- Modify: `game/chapter5.rpy`
- Modify: `game/difficulty.rpy`
- Modify: `game/save_compat.rpy`
- Modify: `game/chapter4_expansion.rpy`
- Modify: `game/chapter5_expansion.rpy`
- Modify: `game/endings_expansion.rpy`
- Modify: `game/balance.rpy`
- Modify: `game/screens_custom.rpy`
- Modify: `game/test_game.rpy`

### Step 1: Add failing regression cases

Add a focused testcase that calls a pure `get_finale_route_availability(...)` helper and proves all of these states:

- hard difficulty, faith as the only high stat, full Dark Lily membership, both faction relations below 30, no truth/Borgia/sea route: `holy_guardian` is hidden and `fall` is visible;
- poison method plus executor plus original testament, but no mastermind confirmation: `truth` is false;
- mastermind confirmation plus original testament: `truth` is true;
- faith as the top route without full Dark Lily membership: `holy_guardian` is visible and `fall` is false;
- every test result contains at least one visible route.

Also add assertions for a small helper used by save migration: legacy `true_killer_known=True` with only chapter-three state does not infer mastermind knowledge, while the same legacy flag with a reliable chapter-four provenance (`prince_ally` or `prince_answer_pending`) does.

Run the focused testcase before defining the helpers and record the expected missing-function/assertion failure:

```powershell
..\renpy.exe . test test_critical_finale_routes --hide-execution all
```

### Step 2: Introduce the three evidence stages

Define these defaults next to the existing third-chapter flags:

- `father_poison_method_known = False`
- `father_poison_executor_known = False`
- `father_murder_mastermind_known = False`

In the Dark Lily chapter-three scene, set method knowledge when the residue and poison are established, set executor knowledge only after Hans is identified as the person who delivered it, and do not set mastermind knowledge. At the two chapter-four sources that actually identify the Queen as the ordering party, set mastermind knowledge. Keep `true_killer_known` synchronized to true at those valid sources only so newly written saves remain understandable to older builds, but remove it from gameplay gates.

Audit every read of `true_killer_known` and choose the narrowest truthful replacement. In particular:

- chapter-three evidence/achievement summaries use method or executor knowledge;
- testament handoff, definitive accusations, and the truth ending use mastermind knowledge;
- debug/status screens display all three stages instead of collapsing them into one claim.

### Step 3: Add conservative old-save migration

In `save_compat.rpy`, initialize missing new flags and migrate in increasing certainty:

- poison evidence/father-poisoned state may establish method knowledge;
- a legacy true flag combined with the completed Dark Lily headquarters disclosure may establish executor knowledge;
- legacy `true_killer_known` establishes mastermind knowledge only with reliable chapter-four provenance (`prince_ally`, `prince_answer_pending`, or the exact logged fifth-chapter response to the Prince), never from chapter progress alone.

Make migration idempotent and leave already-true new flags true.

### Step 4: Centralize finale availability

Add a pure helper in `difficulty.rpy` that returns the complete visible-route map/set after applying stat ranking, difficulty thresholds, full-member suppression of the holy route, truth/Borgia/vassal/resist/sea predicates, and the fall fallback. Compute fall from the non-sea core routes so the intentionally optional sea escape can coexist with fall. Update `chapter5.rpy` so both its briefing variables and every menu guard read that one result. Do not separately reconstruct route conditions in the menu. Make the balance/debug reachability display consume the same route predicates.

### Step 5: Verify and commit

Run:

```powershell
..\renpy.exe . test test_critical_finale_routes --hide-execution all
..\renpy.exe . lint
python scan_missing_portraits.py
python scan_narration_overlap.py
git diff --check
rg -n "true_killer_known" game -g "*.rpy"
```

The final search may show defaults/migration/legacy synchronization, but no gameplay gate. Commit with a focused message such as `fix: separate murder evidence from mastermind truth`.

---

## Task 2: Route every formal chapter entry through one idempotent bootstrap

**Files:**

- Create: `game/new_run.rpy`
- Modify: `game/script.rpy`
- Modify: `game/prologue.rpy`
- Modify: `game/chapter2.rpy`
- Modify: `game/chapter3.rpy`
- Modify: `game/chapter4.rpy`
- Modify: `game/chapter5.rpy`
- Modify: `game/southern_expansion.rpy`
- Modify: `game/save_compat.rpy`
- Modify: `game/test_game.rpy`

### Step 1: Add a failing bootstrap testcase

Add focused testcases that start the actual chapter labels and prove:

- each blank direct entry first reaches `difficulty_select`, proving setup was not bypassed;
- after completing setup, the chosen difficulty is stored, the chosen/default player name is non-empty, and starter inventory has been initialized;
- calling the bootstrap a second time leaves stats and inventory unchanged, proving setup ran exactly once;
- calling `after_load` marks the run initialized, and a subsequent chapter entry neither opens setup screens nor resets a synthetic existing inventory;
- each destination still reaches its requested chapter rather than `start` or prologue.

Run it before inserting the common calls and capture the current failure in which direct chapter starts bypass `difficulty_select`:

```powershell
..\renpy.exe . test test_new_run_bootstrap --hide-execution all
```

### Step 2: Extract an idempotent bootstrap label

Move the one-time setup currently embedded at the start of `prologue` into `new_run_bootstrap`: tutorial display, difficulty selection, New Game+ application/banner, name input/defaulting/easter egg, and inventory initialization. Guard it with an ordinary per-run `default _new_run_bootstrap_done = False` so accidental double calls return without applying NG+ or resetting inventory twice.

Do not put `snapshot_chapter_start()` in this one-time bootstrap: snapshots are chapter-level state. Add a chapter-one snapshot beside its entry setup, retain existing snapshots in chapters 2–5, retain the prologue snapshot, and retain the southern snapshot. For the southern standalone path, apply its standalone attribute baseline before calling the bootstrap so NG+ bonuses are not overwritten.

### Step 3: Rewire all entry points and protect loaded saves

Call `new_run_bootstrap` with explicit stable `from` labels at the start of `prologue`, `chapter1_start`, `southern_arc_standalone`, and `chapter2_start` through `chapter5_start`. `label start` and chapter-select actions may retain their current destinations because those formal entries now enforce the invariant themselves. Remove the duplicated one-time setup from `prologue`.

In `after_load`, unconditionally set `_new_run_bootstrap_done = True`. A loaded save is always an existing run: do not infer from an empty inventory and do not grant retroactive starter items. Preserve the chapter-select `_skip_next_chapter_autosave` behavior unchanged.

### Step 4: Verify and commit

Run:

```powershell
..\renpy.exe . test test_new_run_bootstrap --hide-execution all
..\renpy.exe . test test_walkthrough --hide-execution all
..\renpy.exe . lint
python scan_missing_portraits.py
python scan_narration_overlap.py
git diff --check
```

Commit with a focused message such as `fix: bootstrap every blank chapter start`.

---

## Task 3: Make seven mobile finale choices reachable

**Files:**

- Modify: `game/screens.rpy`
- Modify: `game/test_game.rpy`
- Add screenshot under the existing testcase screenshot location only if the repository already tracks such fixtures; otherwise keep it as verification output.

### Step 1: Add a failing real-render testcase

Add a fixture label containing seven representative long, two-line choices and a testcase that opens it under the small/touch/phone variant, scrolls the choice container by its intended screen id, selects the seventh option, and asserts the seventh branch ran. Capture a screenshot after scrolling.

Run before adding the viewport and record the expected missing-id/unreachable-choice failure:

```powershell
$env:RENPY_VARIANT='small touch mobile'
..\renpy.exe . test test_mobile_choice_overflow --hide-execution all --overwrite-screenshots
Remove-Item Env:RENPY_VARIANT
```

### Step 2: Add small/touch scrolling without shrinking core text

For the small/touch choice-screen variant, put the choice list in a height-bounded viewport with a stable id, touch dragging, mouse-wheel support, page-key support, and a visible scrollbar/scroll affordance. Define choice-specific viewport/side/scrollbar styles rather than inheriting the game-menu viewport's fixed 900-pixel width. Preserve keyboard navigation and desktop behavior. Keep adequate clearance from the quick menu and device safe area.

### Step 3: Render, inspect, verify, and commit

Repeat the small/touch testcase, open the generated screenshot at original detail, and verify the seventh option is reachable, text is not clipped, the scrollbar is visible, and the quick menu does not cover choices. Then run lint and the two mandated narrative scanners plus `git diff --check`.

Commit with a focused message such as `fix: scroll overflowing mobile choices`.

---

## Task 4: Make accessibility settings affect rendered UI

**Files:**

- Modify: `game/extras.rpy`
- Modify: `game/screens.rpy`
- Modify: `game/save_compat.rpy` only if legacy custom accessibility fields require one-time compatibility handling
- Modify: `game/test_game.rpy`

### Step 1: Add failing setting and render tests

Add assertions that the four branded size buttons set `preferences.font_size` to `0.9`, `1.0`, `1.25`, and `1.5`, and that the high-contrast buttons change `preferences.high_contrast`. Assert the normal Preferences page exposes the accessibility entry. Add a small/touch screenshot case with sample dialogue and seven choices at `1.5` scale.

Run the focused testcase before wiring consumers and capture its assertion failure:

```powershell
..\renpy.exe . test test_accessibility_settings --hide-execution all
$env:RENPY_VARIANT='small touch mobile'
..\renpy.exe . test test_accessibility_render --hide-execution all --overwrite-screenshots
Remove-Item Env:RENPY_VARIANT
```

### Step 2: Use Ren'Py's renderer-backed preferences

Replace the custom `persistent.text_size_offset` actions with `Preference("font size", factor)` and selected-state checks against `preferences.font_size`. Replace the custom high-contrast actions with `Preference("high contrast text", "enable"/"disable")` and selected-state checks against `preferences.high_contrast`. Remove the unused `apply_accessibility()` path. Ren'Py's actions already issue a display reset and its text renderer consumes both preferences, so do not duplicate that behavior with manual style mutation.

Expose the branded accessibility screen from the normal `preferences()` screen. If old custom persistent fields have non-default values, migrate them once to the equivalent engine preference without overriding subsequent user choices; retain or retire the old fields only as compatibility data.

Replace critical mobile hard-coded 10–14 px helper text in the affected settings/choice UI with variant-aware named sizes or styles where it would otherwise remain unreadable.

### Step 3: Render, inspect, verify, and commit

Run both tests, inspect the small/touch screenshots at original detail, then run lint, the two mandated scanners, the walkthrough testcase, and `git diff --check`.

Commit with a focused message such as `fix: apply accessibility settings to live styles`.

---

## Task 5: Remove player-visible doubled percent signs and add a release gate

**Files:**

- Create: `Tools/test_release_regressions.py`
- Modify: `game/combat.rpy`
- Modify: `game/crafting.rpy`

### Step 1: Add and run a failing static regression test

Implement a standard-library scan over `.rpy` files that reports player-visible `%%` literals while allowing genuine Python `%`-format escapes such as a quoted string containing `%%` followed by the `%` operator. Include file and line number in failures.

Run it before changing copy and confirm it reports exactly 13 existing violations: ten in `combat.rpy` and three in `crafting.rpy`.

```powershell
python Tools/test_release_regressions.py
```

### Step 2: Correct only the 13 literals

Change the player-visible doubled literals to single `%` and leave valid Python formatting escapes untouched.

### Step 3: Verify and commit

Run:

```powershell
python Tools/test_release_regressions.py
..\renpy.exe . lint
python scan_missing_portraits.py
python scan_narration_overlap.py
git diff --check
```

Commit with a focused message such as `fix: prevent doubled percent UI text`.

---

## Task 6: Whole-batch verification and 3.9.2 release metadata

**Files:**

- Modify: `game/options.rpy` only if this checkout's release convention requires the version bump in the fix branch
- Modify: the existing changelog/release note file only if one already belongs to the 3.9.x release process

### Step 1: Run the complete gates

```powershell
..\renpy.exe . test test_walkthrough --hide-execution all
..\renpy.exe . test test_critical_finale_routes --hide-execution all
..\renpy.exe . test test_new_run_bootstrap --hide-execution all
..\renpy.exe . test test_accessibility_settings --hide-execution all
python Tools/test_release_regressions.py
..\renpy.exe . lint
python scan_missing_portraits.py
python scan_narration_overlap.py
git diff --check
git status --short
```

Repeat both small/touch render testcases with screenshot overwrite enabled and inspect both outputs at original detail.

### Step 2: Perform required manual script checks

Inspect all changed dialogue-adjacent blocks for a preceding hide when a character changes sides (`show ... at left`), confirm no new untranslated strings were introduced, and verify the final `true_killer_known` search contains only compatibility/default synchronization uses.

### Step 3: Broad review and final commit

Generate a whole-range review package from the starting commit to `HEAD`, dispatch a broad code reviewer, fix and re-review every Critical/Important finding, then rerun the covering gates. If version metadata is part of this repository's normal fix-release convention, bump to `3.9.2` and record only this batch's changes in one final metadata commit. Do not run `prepare_release.py` or build distributables unless packaging is explicitly requested.

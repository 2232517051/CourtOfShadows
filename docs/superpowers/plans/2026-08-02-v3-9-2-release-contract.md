# 3.9.2 Release Contract and Distribution Cleanup Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: use `superpowers:subagent-driven-development` to execute one task at a time. Every production change uses `superpowers:test-driven-development`; every completion claim uses `superpowers:verification-before-completion`.

**Goal:** Produce uploadable Windows and Android 3.9.2 packages whose copy, Android metadata, archive contents, compatibility behavior, and signing identity match the approved release contract.

**Architecture:** Treat release facts as a testable contract. A source-level Python gate owns version/copy/classification consistency; Ren'Py render tests own player-visible screen rendering; a post-build verifier owns archive and APK facts. Packaging cleanup uses first-match explicit exclusions and never deletes source assets or `old-game` compatibility inputs.

**Tech Stack:** Ren'Py 8.5.2, Python 3 standard library, PowerShell, Android build-tools (`aapt`, `zipalign`, `apksigner`), FFmpeg/Pillow trailer generator where available.

---

## Task 1: Add the failing source release-contract gate

**Files:**

- Create: `Tools/test_release_contract.py`
- Read: `game/options.rpy`
- Read: `game/effects.rpy`
- Read: `game/pv.rpy`
- Read: `game/effects.rpy`
- Read: `game/extras.rpy`
- Read: `game/difficulty.rpy`
- Read: `README.txt`
- Read: `DESCRIPTION.txt`
- Read: `DEVELOPER_NOTE.txt`
- Read: `store_assets/taptap_description.txt`
- Read: `android.json`

### Step 1: Write the exact failing checks

Use `unittest` and standard-library parsing/helpers. Assert:

- `config.version`, `android.json.version`, package names, and API 36 agree.
- Android numeric version is at least `1785596475`.
- the main ending catalog is exactly the nine approved keys and its three source maps agree.
- current copy has the approved facts and contains none of the stale current-release phrases.
- current copy contains no `N-M小时` or `N小时` promise.
- current NG+ copy says it inherits Power, Wealth, and Intrigue, not new story content.
- source `old-game` contains the 56 expected `.rpyc` files and required node guard still passes.

Do not scan historical changelog entries or archived announcements for old ending counts.

### Step 2: Run and record RED

```powershell
python Tools/test_release_contract.py
```

Expected: failures for Android 1.0.9/API 33, About/Privacy/PV version and ending copy, playtime, current store copy, and NG+ claims.

### Step 3: Commit only the failing test

```powershell
git add Tools/test_release_contract.py
git commit -m "test: define 3.9.2 release contract"
```

---

## Task 2: Correct current copy and Android source metadata

**Files:**

- Modify: `game/options.rpy`
- Modify: `game/effects.rpy`
- Modify: `game/pv.rpy`
- Modify: `README.txt`
- Modify: `DESCRIPTION.txt`
- Modify: `DEVELOPER_NOTE.txt`
- Modify: `store_assets/taptap_description.txt`
- Modify: `Tools/make_trailer.py`
- Modify: `android.json`
- Test: `Tools/test_release_contract.py`

### Step 1: Update Chinese copy from the approved Few-shot direction

- State the concrete inheritance and murder-mystery setup.
- State five chapters, nine main endings, and one hidden epilogue without calling it a tenth ending.
- Use the real six values.
- State New Game+ inheritance precisely.
- Remove all numeric playtime claims.
- Make the rating prompt platform-neutral and rename the close-only action.
- Keep the five-ending PV montage but label it a partial preview; make the final card say nine paths/nine costs and `PC · Android`.

Translate the same facts into the existing English store section without adding claims absent from Chinese.

### Step 2: Synchronize Android source metadata

Set version name 3.9.2, target 36, and numeric-version floor 1785596475. Keep package/orientation/signing inputs unchanged.

### Step 3: Run GREEN and required text checks

```powershell
python Tools/test_release_contract.py
python Tools/test_release_regressions.py
python Tools/test_release_regressions_classifier.py
python Tools/scan_ai_smell.py
python Tools/scan_canon.py
python scan_missing_portraits.py
python scan_narration_overlap.py
..\renpy.exe . lint
git diff --check
```

The two heuristic narrative scans are triage inputs; no global rewrite is authorized. The release contract, lint, portrait, and narration gates must pass.

### Step 4: Commit

```powershell
git add game/options.rpy game/effects.rpy game/pv.rpy README.txt DESCRIPTION.txt DEVELOPER_NOTE.txt store_assets/taptap_description.txt Tools/make_trailer.py android.json
git commit -m "fix: align 3.9.2 player-facing release copy"
```

---

## Task 3: Render About and privacy screens

**Files:**

- Modify: `game/test_game.rpy`
- Test: `Tools/test_release_contract.py`

### Step 1: Add the failing render test

Add a focused suite that opens the production About screen and `privacy_policy_screen`, takes screenshots, and proves each screen can be dismissed. Use a protected persistent snapshot so the test does not alter the user's privacy state.

### Step 2: Run RED if the production screen cannot be driven

```powershell
..\renpy.exe . test test_release_metadata_render --hide-execution all --overwrite-screenshots
```

### Step 3: Make the smallest test/production adjustment needed

Do not introduce a duplicate test-only screen. The production screens themselves must render.

### Step 4: Inspect screenshots and verify

Open screenshots at original resolution. Confirm no clipping, stale version, unexpanded interpolation, or inaccessible close action.

```powershell
..\renpy.exe . test test_release_metadata_render --hide-execution all
..\renpy.exe . lint
python scan_missing_portraits.py
python scan_narration_overlap.py
git diff --check
```

### Step 5: Commit

```powershell
git add game/test_game.rpy tests/screenshots
git commit -m "test: render release metadata screens"
```

---

## Task 4: Add failing packaging-classification checks

**Files:**

- Modify: `Tools/test_release_contract.py`
- Read: `game/options.rpy`

### Step 1: Assert exact high-confidence exclusions and ordering

Assert exclusions exist before generic includes for:

- test RPYC;
- alternate music and test audio;
- source/backup image directories;
- internal directories and store assets;
- explicit root marketing images and internal reports;
- store-only text and historical root changelogs.

Assert the corrected README is Windows-only, and assert no rule removes source `old-game/**`.

### Step 2: Run RED

```powershell
python Tools/test_release_contract.py
```

Expected: missing exclusion failures.

### Step 3: Commit test extension

```powershell
git add Tools/test_release_contract.py
git commit -m "test: lock production package allowlist"
```

---

## Task 5: Implement first-match packaging exclusions

**Files:**

- Modify: `game/options.rpy`
- Test: `Tools/test_release_contract.py`

### Step 1: Add explicit exclusions before generic includes

Exclude only the approved exact paths/patterns. Do not delete files. Do not add the 22 dynamically risky UI images. Do not classify `old-game/**` to `None`; leave Ren'Py's compiler-input behavior intact.

Replace general documentation inclusion with Windows-only inclusion of the corrected README.

### Step 2: Run GREEN and regression checks

```powershell
python Tools/test_release_contract.py
python Tools/test_release_regressions.py
..\renpy.exe . lint
python scan_missing_portraits.py
python scan_narration_overlap.py
git diff --check
```

### Step 3: Commit

```powershell
git add game/options.rpy
git commit -m "build: exclude internal and unused release payloads"
```

---

## Task 6: Add the built-distribution verifier

**Files:**

- Create: `Tools/verify_distributions.py`
- Test against: existing Windows ZIP and APK under `E:\Projects\renpy-8.5.2-sdk\CourtOfShadows-3.9.2-rc-dists`

### Step 1: Implement archive-normalized checks

Accept explicit `--windows`, `--apk`, `--previous-apk`, and Android build-tool paths/discovery. Normalize Windows `CourtOfShadows-3.9.2-win/...` and Android `assets/x-...` member names to project-relative names before applying the same forbidden/required contract.

Require:

- archive integrity;
- Windows executable and production RPYC;
- Android production RPYC;
- no internal/store/test/backup/alternate payloads;
- no archive `old-game/` directory;
- APK package/version/SDK/orientation facts;
- version code greater than the previous package;
- zipalignment and same signing certificate.

### Step 2: Run against current packages and record RED

```powershell
python Tools/verify_distributions.py `
  --windows E:\Projects\renpy-8.5.2-sdk\CourtOfShadows-3.9.2-rc-dists\CourtOfShadows-3.9.2-win.zip `
  --apk E:\Projects\renpy-8.5.2-sdk\CourtOfShadows-3.9.2-rc-dists\com.xiaoyiai.courtofshadows-3.9.2-1785596475-release.apk `
  --previous-apk <3.9.1-apk>
```

Expected: forbidden payload failures and non-increasing version code if the same APK is used as both current/floor evidence.

### Step 3: Unit-test member normalization with synthetic ZIPs

Create temporary archives at runtime; do not commit binaries.

### Step 4: Commit

```powershell
git add Tools/verify_distributions.py
git commit -m "test: verify release distribution contents"
```

---

## Task 7: Run complete source verification before production build

**Files:** none expected

Run:

```powershell
python Tools/test_release_contract.py
python Tools/test_release_regressions.py
python Tools/test_release_regressions_classifier.py
python Tools/test_old_game_compat.py
python Tools/test_story_timeline.py
python Tools/test_timeline_endings.py
python Tools/test_finale_endings.py
python Tools/test_finale_route_functions.py
python Tools/test_chapter4_resolution.py
python Tools/test_chapter4_prince.py
python Tools/test_southern_outcomes.py
..\renpy.exe . test --hide-execution all
..\renpy.exe . lint
python scan_missing_portraits.py
python scan_narration_overlap.py
python Tools/scan_canon.py
python prepare_release.py
git diff --check
git status --short
```

If `prepare_release.py` changes `game/msyh.ttf`, commit that generated font in its own focused commit and rerun the suite.

---

## Task 8: Rebuild and verify upload packages

**Files:** generated distributions outside the repository

### Step 1: Build Windows and Android

Use the existing Ren'Py 8.5.2 SDK/launcher commands already proven for this branch. Do not overwrite or delete the prior evidence packages; emit a new distribution directory or uniquely named files.

### Step 2: Run the distribution verifier

Require all checks to pass. Record final SHA-256, sizes, APK manifest facts, alignment, and certificate fingerprint.

### Step 3: Runtime smoke

- Launch the Windows package to the main menu.
- Load the three protected real old saves used by the prior RC verification.
- Confirm the corrected About/privacy screens in the packaged runtime.
- If an Android device is connected, perform install/upgrade and touch smoke. Otherwise report the physical-device gate as unverified, not passed.

### Step 4: Regenerate derived store trailer

Run `Tools/make_trailer.py` if its dependencies are available. Verify the output duration, dimensions, audio stream, and revised nine-path title card. Keep the result in `store_assets`; it remains excluded from player packages.

### Step 5: Final review

Dispatch a whole-range code review from `e7493ec..HEAD`, fix Critical/Important findings, rerun affected gates, and ensure `git status --short` is clean.

---

## Asset report required at handoff

- Art: reused only; no new art required.
- Music: reused only; no new music required.
- Sound effects: no new sound effects required.
- Animation/video: existing trailer re-render only; no new source animation required.
- Package impact: report actual bytes saved in Windows and APK, not estimates.


# RC Screenshot Determinism Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the father-son screenshot regression pass reproducibly under both clean windowed and existing fullscreen preferences.

**Architecture:** The Ren'Py testcase owns display normalization because it owns the screenshot capture. The Python asset contract enforces the normalization call and native-size reference images so a host-dependent baseline cannot be committed again.

**Tech Stack:** Ren'Py 8.5.2 test framework, Python 3 `unittest`, Pillow, PowerShell.

## Global Constraints

- The canonical capture size is exactly `config.screen_width` by `config.screen_height`, currently 1280x720.
- Keep the revision suffix `@74439fe` on all three reference PNG filenames.
- Do not change either shipping father-son WebP, story text, ending conditions, music, SFX, UI, or animation.
- Use a fresh explicit `--savedir` for every Ren'Py launch and preserve existing persistent files.
- New shipping assets are forbidden for this fix; only non-shipping test baselines may change.

---

### Task 1: Make father-son screenshot capture resolution-independent

**Files:**
- Modify: `Tools/test_story_timeline.py:40-130`
- Modify: `game/test_game.rpy:412-431`
- Modify: `tests/screenshots/father_son_empty@74439fe.png`
- Modify: `tests/screenshots/father_son_manifested@74439fe.png`
- Modify: `tests/screenshots/father_son_departed@74439fe.png`

**Interfaces:**
- Consumes: `config.screen_width`, `config.screen_height`, `renpy.set_physical_size`, and `renpy.get_physical_size`.
- Produces: three 1280x720 revision-tagged PNG references and a testcase that normalizes its capture window before comparison.

- [ ] **Step 1: Write the failing Python contract**

In `test_father_son_render_baselines_are_revision_tagged`, open every matched PNG and assert:

```python
with Image.open(path) as image:
    self.assertEqual(image.size, (1280, 720))
```

In `test_father_son_render_regression_executes_production_atl`, assert:

```python
self.assertIn(
    "renpy.set_physical_size((config.screen_width, config.screen_height))",
    test_game,
)
```

- [ ] **Step 2: Run RED**

Run:

```powershell
python -B -m unittest Tools.test_story_timeline.FatherSonAssetTests -v
```

Expected: failure because the current references are 1920x1080 and `test_game.rpy` does not normalize the physical size.

- [ ] **Step 3: Normalize the capture window**

At the start of `testcase test_father_son_cg_render`, before the first fixture launch, add:

```renpy
$ renpy.set_physical_size((config.screen_width, config.screen_height))
pause 0.3
assert eval (renpy.get_physical_size() == (config.screen_width, config.screen_height))
```

- [ ] **Step 4: Re-record the three references at native size**

Launch only `test_father_son_cg_render` with a fresh savedir, `RENPY_TEST_VC_REVISION=74439fe`, and `--overwrite-screenshots`. Require `[rpytest] Status: PASSED`, then verify exactly three `father_son_*@74439fe.png` files exist and all are 1280x720.

- [ ] **Step 5: Verify both display-preference states**

Run the focused testcase without overwrite from an empty savedir. Run it again from another fresh savedir seeded with a known fullscreen persistent file. Both runs must report one passed testcase, the new physical-size assertion, three screenshot comparisons, and `[rpytest] Status: PASSED`.

- [ ] **Step 6: Run complete gates**

Run:

```powershell
python -B -m unittest discover -s Tools -p "test_*.py" -v
python -B Tools/scan_canon.py
python -B scan_missing_portraits.py
python -B scan_narration_overlap.py
python -B Tools/test_release_regressions.py
python -B prepare_release.py
```

Then run the full Ren'Py suite from a new savedir and Ren'Py lint from another new savedir. Require all suites, cases, hooks, and assertions to pass, lint exit 0, `git diff --check` exit 0, and no unexpected source or persistent changes.

- [ ] **Step 7: Commit**

```powershell
git add Tools/test_story_timeline.py game/test_game.rpy tests/screenshots/father_son_empty@74439fe.png tests/screenshots/father_son_manifested@74439fe.png tests/screenshots/father_son_departed@74439fe.png
git commit -m "test: stabilize father son render baselines"
```

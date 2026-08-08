# Task 5 winter-routing report

## Scope and revision

- Start commit: `c8c6d358d0427258df0c9c4a90a60051551bf77c`.
- Functional and package tags remain fixed at `ebb4efd2194fb31710d0331d53d0fe825eb8062c` (`governance-winter-baseline`) and `b75a3ecc3cc59ff63665236543124b33ad2bcd9c` (`governance-winter-package-baseline`).
- Final Task 5 commit: the commit containing this report, with message `feat: route winter interlude before chapter two`; its exact SHA is recorded in the final handoff because a commit cannot contain its own object ID.
- Scope is Task 5 only: the southern-to-winter-to-Chapter-2 seam, blank bootstrap, the minimal active/delegated structural skeleton, shared cleanup, stable anchors, compatibility pads, direct Chapter-2 music restoration, and their contracts. There is no Task 6 chapter selection, Task 7 graph work, or final story copy.

## TDD RED evidence

- Source RED: `.superpowers/sdd/winter-routing-python-red.txt`. The seven routing contracts produced 13 missing-contract assertion failures plus one missing-firewall diagnostic; failures identified absent production seams rather than harness errors.
- Timeline RED: `.superpowers/sdd/winter-timeline-python-red.txt`. The three timeline contracts exposed the duplicate Chapter-2 month line and absent winter jump with explicit diagnostics.
- Real-save continuation RED: `C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\renpy-suite-evidence\renpy-suite-test_winter_interlude_continuations-failed-20260808t160827122z-c8c6d358d042-fbae6aa8.log`. All three signed fixtures loaded and resumed their live in-label return stacks, then timed out only because the approved anchors did not yet exist.
- Routing RED: `C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\renpy-suite-evidence\renpy-suite-test_winter_interlude_routing-failed-20260808t160930689z-c8c6d358d042-1be45e60.log`. Seven cases rejected the missing winter entry label through ordinary preflight assertions.
- Audio RED: `C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\renpy-suite-evidence\renpy-suite-test_winter_interlude_audio-failed-20260808t160946442z-c8c6d358d042-0db361de.log`. Four cases identified the missing cleanup and post-cinematic music restoration.
- RED was obtained before production routing was added and was never committed.

## Implemented routing and compatibility

- Mainline order is `southern` autosave/arc -> `winter_interlude_start` -> `chapter2_start`; the existing southern return behavior is unchanged.
- Winter entry snapshots blank-new-run state before `new_run_bootstrap`. Only that blank branch seeds the approved governance inputs, then the frozen context routes completed, delegated, legacy, active, unseen, and invalid states. A winter autosave is created only for a genuinely unseen entry.
- The player-visible branch is deliberately structural: one non-narrative placeholder and the approved `亲自主持` / `交给奥尔德里克` meanings. `active` is written only inside the first branch and cannot escape the interlude; every normal exit reaches delegated or an already terminal state before Chapter 2.
- The Chapter-2 blank gate applies delegation only under its captured blank condition and before Chapter-2 save/snapshot calls. Completed, delegated, and legacy entries preserve their status.
- The three normal legacy governance calls were removed while their production label bodies and result fields remain intact. Two stable anchors, an unconditional fallthrough firewall, and three explicit old-return continuation pads preserve `_call_gov_merch2`, `_call_gov_build2`, and `_call_gov_famine2` saves.
- Every winter/pad exit calls the shared idempotent cleanup. Cleanup always clears weather, the built-in temporary `sound` channel, and character displays; `cleanup(False)` preserves music while `cleanup(True)` stops music. No channel was registered and no unrelated sound/music policy was introduced.
- `castle_calm.ogg` is restarted directly after `cinematic_chapter2`; the duplicate body-level month sentence was removed while the cinematic remains the sole month-card owner.

## Source, timeline, and runtime proof

- Focused source/timeline contracts: 17/17 passed (seven routing, seven existing winter-module, three timeline). The expanded AST guard retains the 37 prohibited / four allowed Task 3 invariants and permits only exact Task 5 label-local syntax. Mutation probes reject missing/dedented blank seeds, `active` outside its exact menu branch, a dedented Chapter-2 blank application, wrong cleanup calls/channels, and misplaced routing writes.
- Continuations: `C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\renpy-suite-evidence\renpy-suite-test_winter_interlude_continuations-passed-20260808t162316020z-c8c6d358d042-21859ad8.log` (3 cases, 24 assertions). Each signed in-label save naturally returns through its matching production pad to the approved anchor, preserves its legacy result, and clears injected snow, a looped existing sound-channel SFX, and a shown character.
- Routing: `C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\renpy-suite-evidence\renpy-suite-test_winter_interlude_routing-passed-20260808t163856665z-c8c6d358d042-8693615c.log` (10 cases, 55 assertions). It covers blank, unseen active/delegate, completed, delegated, explicit legacy, active, and invalid re-entry. Completed/delegated cases start at the real winter entry, traverse the real Chapter-2 card, recap, cinematic, NPC scenes, and church interaction, then reach both anchors in order without any pad; terminal status is preserved.
- Audio and cleanup: `C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\renpy-suite-evidence\renpy-suite-test_winter_interlude_audio-passed-20260808t163145320z-c8c6d358d042-86c4cf55.log`. Both cleanup modes are called twice in one driver to prove idempotency; False preserves music, True stops it, and both clear injected weather/sound/characters. A real `chapter2_start` run physically advances the card/recap and skips the cinematic overlay, then observes `castle_calm.ogg` on the actual music channel.
- Every runtime suite used a unique external savedir, recorded exactly one fresh `PASSED`, and its recorded PID was gone after completion.

## Regression and release gates

- Existing state: `renpy-suite-test_winter_interlude_state-passed-20260808t162605540z-c8c6d358d042-385e855c.log` (75 cases, 187 assertions).
- Existing migration: `renpy-suite-test_winter_interlude_legacy_migration-passed-20260808t162614317z-c8c6d358d042-4a215e7f.log` (8 cases, 18 assertions; staged signed fixtures).
- Existing ending invariance: `renpy-suite-test_winter_interlude_ending_invariance-passed-20260808t162624340z-c8c6d358d042-9617a8a4.log` (57 cases, 330 assertions).
- Existing blank bootstrap: `renpy-suite-test_new_run_bootstrap-passed-20260808t162640515z-c8c6d358d042-c2053d87.log` (9 cases, 39 assertions). Chapter music-continuity source contracts passed 3/3.
- Final full Python discovery: 240/240 passed. Final old-game compatibility/source-node focus: 8/8 passed. `scan_missing_portraits.py` and `scan_narration_overlap.py`: zero findings.
- Final Ren'Py lint `--all-problems`: exit 0; evidence `C:\Users\22325\Documents\Codex\2026-07-31\new-chat-2\renpy-suite-evidence\renpy-lint-all-na-20260808t164203669z-c8c6d358d042-3325159a.txt`; PID 16328 is gone.
- Independent Task 5 Spec review: Critical 0, Important 0, Ready.

## Official old-game inventory

- The official Ren'Py 8.5.2 launcher `update_old_game` command refreshed the existing 57-file tree in place after the final `.rpy` changes; the directory was never cleared.
- Final inventory: exactly 57 RPYC files, 3,986,686 bytes, canonical path/size/file-SHA-256 digest `ac05f8efcd1884b751d6d19fb89c2cd3d45327db2fa73106fcfd7e94c534944c`.
- Exact 57-path coverage, every scannable slot-one pickle, all protected historical generations/nodes, and missing/stale/extra-path guards pass.
- Active release contract remains exactly 56 RPYC files and excludes `game/test_game.rpyc`. `old-game/` remains excluded from player packages, so the repository-only compatibility refresh does not enter the shipping payload.
- Fixture manifest SHA-256 remains `9F76CBBB6AD6E521F3F44CBB67F693629288932A1F90A5F85F253CC30616AF5E`.

## Story-copy and asset audit

- No final winter narrative was drafted or added. Task 8 remains reserved for a fresh Claude Opus session and explicit user approval before any final copy is applied.
- No art, music, SFX, portrait, animation, UI image, font, or other binary asset was added or changed. Production reuses `castle_calm.ogg`, the existing weather helpers, built-in audio channels, and existing character displays; existing SFX is used only as a runtime cleanup stimulus.
- Final `game/msyh.ttf` blob is exactly the parent blob `4103d095775d89291a0987745083570c2a0b69c8`; package size receives no new media cost.

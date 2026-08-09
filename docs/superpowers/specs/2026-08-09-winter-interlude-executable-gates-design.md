# Winter Interlude Executable Gates Design

**Status:** Approved by the user on 2026-08-09

**Scope:** Development and release-test tooling only

**Supersedes:** Handwritten Markdown/PowerShell execution parsing in `Tools/test_governance_winter_interlude.py`

## Context

Tasks 7 and 8 need repeatable, fail-closed verification of the winter-interlude story graph and its final prose. The tracked implementation plan currently embeds PowerShell command blocks and a Python test attempts to prove that those Markdown blocks would execute correctly.

Repeated adversarial review showed that this is the wrong seam. A handwritten parser had to approximate CommonMark fences, HTML comments, PowerShell block comments, strings, smart quotes, braces, subexpressions, short-circuit execution, and early terminators. Each local fix exposed another valid syntax shape that could make non-executing text appear executable. The test was becoming a second, incomplete Markdown and PowerShell interpreter.

The executable gate itself must be the module. The plan should only tell a maintainer which gate to call.

## Decision

Create one shared deep module:

```powershell
& Tools/Run-WinterInterludeGate.ps1 -Gate Structural -ProjectRoot (Get-Location).Path
```

```powershell
& Tools/Run-WinterInterludeGate.ps1 -Gate Narrative -ProjectRoot (Get-Location).Path
```

One script is preferred over two scripts because both gates share project validation, isolated run directories, evidence capture, Ren'Py suite invocation, timeout handling, and fail-fast behavior. Two scripts would either duplicate those rules or require a third common helper plus two shallow adapters.

The Markdown plan remains documentation. It is not treated as an executable interface, and tests must not attempt to prove Markdown control-flow semantics.

## Public Interface

`Tools/Run-WinterInterludeGate.ps1` exposes:

```powershell
[ValidateSet("Structural", "Narrative")]
[string] $Gate

[string] $ProjectRoot
[string] $RunRoot

[ValidateSet("Batch", "Final")]
[string] $NarrativePhase = "Final"

[ValidateRange(30, 1800)]
[int] $ToolTimeoutSeconds = 300

[ValidateRange(300, 1800)]
[int] $RenPyTimeoutSeconds = 300
```

- `Gate` is required.
- `ProjectRoot` defaults to the repository root resolved from `$PSScriptRoot`; callers may pass an explicit absolute root.
- `RunRoot` defaults to a new GUID-named directory under the operating-system temporary directory. If supplied, it must be an absolute path that does not already exist.
- `NarrativePhase` is consumed only by `-Gate Narrative`. `Batch` verifies one approved prose integration while unfinished scenes may still contain structural placeholders; `Final` is the default and additionally requires the complete final-copy contracts.
- `ToolTimeoutSeconds` bounds each Python capability, scanner, and unittest child process.
- `RenPyTimeoutSeconds` defaults to 300 seconds and must remain within the existing runner's supported range of 300–1800 seconds.

No ordinary caller needs to know step manifests, process construction, savedir naming, or evidence layout.

## Interface Invariants

The module must:

1. Resolve and validate `ProjectRoot` before running any step.
2. Make containment decisions from operating-system final-path identity, not lexical `GetFullPath` prefixes alone. On Windows, resolve existing components through handles to their final targets, reject any reparse-point component in the protected or candidate chain, and fail if final-path resolution is unavailable.
3. For a nonexistent `RunRoot`, resolve its nearest existing ancestor, append only the unresolved plain path components, reject a target inside the final `ProjectRoot` or final player `CourtOfShadows-save`, create the directory, then reopen and verify its final identity. Repeat the identity check before every child launch and evidence write.
4. Reject a relative or pre-existing `RunRoot` and retain the exact created run tree as evidence. The gate must not recursively delete `RunRoot` or suite savedirs on success or failure.
5. Create one unique external savedir for every Ren'Py suite.
6. Set every child process's working directory to the resolved `ProjectRoot` and use absolute script/module paths.
7. Pass argument arrays to child processes; it must not concatenate shell command strings.
8. Stop immediately when any step returns nonzero, exceeds its timeout, or violates its postcondition.
9. Return process exit code 0 only after every required automated step succeeds.
10. While `RunRoot` still passes its final-identity check, write per-step stdout, stderr, exit code, elapsed time, and a final summary under `RunRoot/evidence`.
11. Preserve the existing `Tools/Run-RenPySuite.ps1` interface, including its PID-bounded timeout, fresh-status, isolated-savedir, and fixture-staging behavior.
12. Launch every `Run-RenPySuite.ps1` invocation in a separate child `powershell.exe` process, because the existing runner deliberately terminates with `exit 0` or `exit 1`.
13. Place each child in a gate-owned bounded process tree. Python children use `ToolTimeoutSeconds`; runner children receive `RenPyTimeoutSeconds` and an outer watchdog of that value plus a fixed 60-second wrapper grace. On timeout, terminate only that recorded tree, wait for it to disappear, preserve its evidence, and never search for unrelated Python or Ren'Py processes.

## Internal Design

The implementation owns a typed step manifest. A step records only structured data such as:

- stable step name;
- kind (`Python` or `RenPySuite`);
- executable and argument array, or suite name;
- child timeout and, for runner steps, wrapper grace;
- whether legacy fixtures are staged;
- required postcondition and evidence filename.

Execution consumes this manifest in order. Gate selection changes the manifest, not the execution engine.

### Production execution and test seam

There is no injectable executor parameter, test-mode environment switch, dry-run success mode, or alternate public adapter. Tests and production use the same public script entrypoint.

The production implementation resolves `python` from `PATH` and resolves `Tools/Run-RenPySuite.ps1` beneath the exact `ProjectRoot`. Tests construct a temporary fake project root, prepend a recording `python` executable to that test process's `PATH`, and provide a recording `Tools/Run-RenPySuite.ps1`. Those child-process fakes record their received argument arrays and can return a controlled failure. This varies dependencies outside the gate interface instead of adding a production-bindable bypass.

At least one final integration invocation must use the real project root, real Python, real runner, and the public `Structural` entrypoint. Stub-only evidence cannot complete the refactor.

## Structural Gate

`-Gate Structural` runs these steps in this order:

1. `python -m unittest Tools.test_governance_winter_interlude -v`;
2. `test_winter_interlude_state`;
3. `test_winter_interlude_routing`;
4. `test_winter_interlude_ending_invariance`;
5. `test_winter_interlude_route_matrix`;
6. `test_winter_interlude_mid_save`.

Each Ren'Py suite receives a distinct savedir and `RenPyTimeoutSeconds`. The route matrix therefore has a real bound of at least 300 seconds rather than the runner's 120-second default.

## Narrative Gate

`-Gate Narrative -NarrativePhase Batch` runs these steps in this order after each individually approved prose integration:

1. require and execute `Tools/check_winter_narrative_capabilities.py --phase batch`;
2. the full-project canon scan required by `CLAUDE.md`, with machine-readable output and a nonzero result for any finding; its evidence separately identifies findings, if any, attributable to the winter module;
3. AI-smell scan scoped to the winter module, captured as a manual-review artifact rather than an automatic prose approval;
4. missing-portrait scan with a caller-supplied output directory under `RunRoot/evidence`, a machine-readable result, and a nonzero result for findings;
5. narration-overlap scan that rejects a missing target file, writes a machine-readable result, and returns nonzero for findings;
6. show-before-prevention scan required by `CLAUDE.md`, scoped to the winter module and fail-closed on findings;
7. nested-quote scan after Task 8 makes the scanner cover the winter module and return nonzero for findings;
8. `python -m unittest Tools.test_governance_winter_interlude -v`, including the structural contracts and the independently maintained semantic expectations for every scene approved so far;
9. `test_winter_interlude_route_matrix`, including the real delegation case.

The canon scanner's machine-readable schema separates blocking defects from informational review data. `blocking_count` is exactly the sum of anti-logic, geography, terminology, and typo/canon-deviation findings; any positive value returns nonzero. Canon trigger-word occurrences remain in an `informational_occurrences` section for manual comparison with `CANON.md` and do not affect the process exit code by themselves. Capability tests must include one positive and one zero case for every blocking category plus a trigger-word-only case that remains nonblocking.

`-Gate Narrative -NarrativePhase Final` runs the same ordered steps after all approved scenes are integrated, but calls the capability checker with `--phase final` and requires the source suite to include and pass the complete length, reuse-ratio, semantic, placeholder-removal, and final-copy contracts. The final-only contracts are added immediately before this transition; they are not installed as permanently failing tests during earlier batch integrations.

`Tools/check_winter_narrative_capabilities.py` is a Task 8 prerequisite and does not exist during Task 7.5. In `batch` mode it verifies the required scanner flags, machine-readable schemas, negative mutations, show-prevention coverage, and per-scene content-contract support. In `final` mode it additionally proves that the final-only contract set is present. Either Narrative phase must reject a missing or failing capability checker before it starts any scanner. Therefore the gate exists after Task 7.5 but cannot report green until Task 8 has implemented the corresponding prerequisites.

A successful automated Narrative gate does not approve prose. Fresh Opus provenance, raw-output presentation, explicit user approval, and manual review of the AI-smell artifact remain separate mandatory Task 8 evidence.

## Error Handling and Evidence

- Project, path, manifest, and capability validation errors terminate before the next step.
- A failed child process records its own stdout/stderr and prevents every later step from starting.
- The summary distinguishes process failure, postcondition failure, timeout, and invalid evidence.
- The gate retains `RunRoot`, suite savedirs, and evidence for inspection; it performs no recursive filesystem cleanup. Process cleanup is limited to the recorded gate-owned child tree.
- If `RunRoot` identity changes, stop before any further filesystem write. Report the path-identity failure only on the gate process's stderr and leave the already-written evidence untouched; a final summary is intentionally absent in this case.
- Successful evidence names include gate, step ordinal, step name, and the current commit SHA when available.
- The gate invokes children from the resolved project root inside `try/finally`; the caller's original working directory is restored even after failure.
- Scanner output is directed to or copied into `RunRoot/evidence`. Narrative prerequisites must prevent `missing_portraits_B.txt` or other repository reports from being rewritten by a gate invocation.

## Verification Strategy

Create `Tools/test_winter_interlude_gate.py`. Tests execute the real public PowerShell script against a temporary fake project and recording child executables rather than parsing Markdown.

Required RED-to-GREEN cases are:

1. the script is absent or fails PowerShell's official `System.Management.Automation.Language.Parser` syntax check;
2. Structural emits the exact ordered source step plus five suites through child processes;
3. both Narrative phases reject the current project while the Task 8 capability checker is absent;
4. a batch-capable fake project emits the exact ordered full-project canon scan, scoped scanners, source contract, and one route-matrix suite;
5. Final rejects a fake project that is batch-capable but lacks the final-only contract capability, while a final-capable fake emits the complete ordered manifest;
6. every Ren'Py step receives a distinct external savedir and a timeout of at least 300 seconds;
7. every Python step receives `ToolTimeoutSeconds`, and a hanging fake Python child or fake runner tree is terminated within its bound without leaving its child process alive;
8. a recording child that fails or times out at step N makes the public gate return nonzero and step N+1 is never observed;
9. paths containing spaces, parentheses, and apostrophes remain single atomic arguments;
10. project-contained, player-save-contained, relative, pre-existing, junction/reparse-routed, or final-path-changing `RunRoot` values are rejected before a child starts;
11. child stdout/stderr and summary files correspond to the observed steps;
12. every runner call occurs in a child PowerShell process, so the runner's own `exit` cannot terminate the parent gate early;
13. a real-project `Structural` invocation completes through the public entrypoint with all five fresh Ren'Py suites.

The existing winter source, route, save, audio, semantic, and old-game tests remain unchanged. Markdown may receive a lightweight discoverability assertion for the script name, but no automated claim that Markdown itself executes.

## Migration

Commit the self-reviewed draft as its own documentation commit before requesting final user approval of the written specification.

Task 7.5 implementation changes are limited to:

- create `Tools/Run-WinterInterludeGate.ps1`;
- create `Tools/test_winter_interlude_gate.py`;
- modify `Tools/test_governance_winter_interlude.py` to remove the handwritten Markdown/PowerShell execution parser and its mutation matrix while retaining production story contracts;
- modify `docs/superpowers/plans/2026-08-08-governance-winter-interlude.md` so Task 7 and Task 8 call the real gate and stage the new tooling files.

The Task 7.5 executable-gate refactor is a separate follow-up commit after the Task 7 story-graph commit. It does not amend the historical Task 7 commit command. Its recommended commit message is:

```text
refactor: execute winter interlude gates from scripts
```

Task 8 must separately add the capability checker and scanner interfaces required by the Narrative gate. Its implementation plan must include:

- create `Tools/check_winter_narrative_capabilities.py`;
- create a fail-closed show-before-prevention scanner;
- add scoped, machine-readable, fail-closed interfaces to canon, portrait, overlap, and nested-quote scanners;
- direct portrait and other generated reports to `RunRoot/evidence` rather than the repository;
- make the tracked per-scene loop call `-Gate Narrative -NarrativePhase Batch` after each approved atomic integration;
- add the final length, reuse-ratio, semantic, placeholder-removal, and copy contracts only at the final transition, then require `-Gate Narrative -NarrativePhase Final` to pass.

## Alternatives Rejected

### Continue the handwritten parser

Rejected. It duplicates two language grammars, has already failed repeated adversarial review, and tests an approximation rather than the executable behavior.

### Create separate Structural and Narrative scripts

Rejected. They share nearly every safety and evidence rule. Splitting them lowers locality and either duplicates the implementation or adds a third helper plus two shallow interfaces.

## Non-Goals

- No changes to winter story labels, state, prose, routing, or saves.
- No changes to `game/test_game.rpy` or `old-game/*.rpyc`.
- No general-purpose Markdown or PowerShell parser.
- No replacement of `Tools/Run-RenPySuite.ps1`.
- No release build or package-verifier changes.
- No claim that an automated Narrative result substitutes for user approval or manual prose review.

## Compatibility and Asset Audit

The design changes development tooling only. It does not change shipping Ren'Py sources, old-game compatibility bytecode, fonts, images, music, sound effects, portraits, animation, or UI assets. Shipping-package size impact is zero. The deferred dedicated winter-granary background remains Task 10 work and is unrelated to this gate module.

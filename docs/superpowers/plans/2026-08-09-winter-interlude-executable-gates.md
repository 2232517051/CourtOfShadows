# Winter Interlude Executable Gates Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the brittle Markdown/PowerShell execution parser with one real, fail-closed executable gate for winter-interlude structural and narrative verification.

**Architecture:** `Tools/Run-WinterInterludeGate.ps1` is the sole public module. It owns validated external run directories, typed manifests, a Windows Job Object-backed child engine, evidence, and Structural/Narrative postconditions; tests invoke that public entrypoint with real child processes and temporary external dependencies rather than an injectable success adapter. The tracked story plan becomes discoverability documentation that calls this gate, not an executable language that Python attempts to interpret.

**Tech Stack:** Windows PowerShell 5.1, .NET Framework 4.8, embedded C# Win32 interop, Python 3 `unittest`, Ren'Py 8.5.2, existing `Tools/Run-RenPySuite.ps1`.

## Global Constraints

- Fixed design base is `ed262771e740b2e502d30921ed92e1de1deb54b6`. Execution starts from the later clean documentation commit containing this plan; record that full SHA as `task75Start` and require `ed26277..task75Start` to contain only this plan file. Do not rediscover or move that start point later.
- Read and implement the approved design at `docs/superpowers/specs/2026-08-09-winter-interlude-executable-gates-design.md`; if code and design conflict, stop rather than silently choosing a third behavior.
- This Task 7.5 range is exactly four files: create `Tools/Run-WinterInterludeGate.ps1`, create `Tools/test_winter_interlude_gate.py`, modify `Tools/test_governance_winter_interlude.py`, and modify `docs/superpowers/plans/2026-08-08-governance-winter-interlude.md`.
- Do not modify `game/*.rpy`, `game/test_game.rpy`, `old-game/*.rpyc`, `game/msyh.ttf`, scanners, shipping metadata, or any image/audio/animation/UI asset.
- Public parameters are exact: `Gate=Structural|Narrative`, optional absolute `ProjectRoot`, optional absolute nonexistent `RunRoot`, `NarrativePhase=Batch|Final` defaulting to Final, `ToolTimeoutSeconds=30..1800` defaulting to 300, and `RenPyTimeoutSeconds=300..1800` defaulting to 300.
- There is no test-mode parameter, executor injection, dry-run success switch, environment success bypass, or alternate public adapter.
- Resolve the current project HEAD from verified `.git` metadata without starting an unmanifested child. If `GIT_COMMIT` is present, it must be nonempty, exact 40- or 64-character lowercase hex, and byte-for-byte equal to that resolved HEAD; it confirms provenance only and never changes manifests, execution, postconditions, or success.
- Windows path containment uses final object identity, not `GetFullPath` alone. Reject relative, drive-relative, device, pre-existing, project-contained, player-save-contained, reparse-routed, and identity-changing run roots before further work.
- Preserve evidence trees. Never recursively delete `RunRoot` or suite savedirs. If `RunRoot` identity changes, write no further file there; report only to gate stderr and intentionally omit the final summary.
- Model all tool arguments as `string[]`. At the native boundary use one tested Windows argv encoder; never use `cmd.exe`, `Invoke-Expression`, `-Command` containing user data, or an untested joined shell command.
- Every child starts suspended, is assigned to a gate-owned Job Object with `JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE`, and is resumed only after assignment. A timeout or leaked descendant is a gate failure, and cleanup targets only that recorded job.
- The existing runner is always invoked in its own child `powershell.exe` because it calls `exit 0/1`. Each suite gets a unique empty external savedir and the common evidence directory.
- The public gate itself is also always launched in a dedicated Windows PowerShell 5.1 `-File` process derived from `[Environment]::SystemDirectory` and ends that host with explicit exit 0/1. Never trust `PATH` or `$env:SystemRoot` for that host, and never dot-source or directly invoke it inside the caller's interactive runspace.
- Structural order is exact: source unittest, `test_winter_interlude_state`, `test_winter_interlude_routing`, `test_winter_interlude_ending_invariance`, `test_winter_interlude_route_matrix`, `test_winter_interlude_mid_save`.
- Narrative capability is intentionally absent in Task 7.5. Both real-project Narrative phases must fail before scanners run until Task 8 adds the checker and scanner interfaces.
- Canon `blocking_count` is exactly anti-logic + geography + terminology + typo/canon-deviation. Trigger-word occurrences are informational and nonblocking by themselves.
- Keep RED evidence under ignored `.superpowers/sdd/`. Require fresh evidence from the current working tree, immediate exit-code checks, and no lingering recorded PIDs.
- Use a fresh implementation subagent for the task, then independent Spec and Standards reviewers. Fix every Critical/Important finding with a new RED→GREEN cycle and repeat both reviews before completion.
- Asset audit after the task: no art, music, SFX, portrait, animation, UI, font, old-game, or shipping-package change is required or permitted; expected package-size delta is zero.

---

## File Map

- `Tools/Run-WinterInterludeGate.ps1`: the only executable gate and owner of the public parameters, native path/process helper, manifests, postconditions, and evidence.
- `Tools/test_winter_interlude_gate.py`: black-box public-entrypoint tests, temporary fake project, compiled recording `python.exe`, fake runner, junction and timeout fixtures, and lightweight plan discoverability checks.
- `Tools/test_governance_winter_interlude.py`: retain story/state/semantic tests; delete the handwritten Markdown/PowerShell execution parser and its mutation matrix; retain a lightweight non-execution assertion for the approved six-sentence migration contract.
- `docs/superpowers/plans/2026-08-08-governance-winter-interlude.md`: replace Task 7's inline verifier with the Structural gate, add Task 7.5, and replace the incomplete Task 8 implementation with a hard stop plus the exact public-interface requirements for a separately reviewed narrative-delivery plan.

---

---

---

---

---

### Task 1: Bootstrap the public gate through three focused RED-to-GREEN loops

**Files:**
- Create: `Tools/test_winter_interlude_gate.py`
- Create: `Tools/Run-WinterInterludeGate.ps1`

**Interfaces:**
- Produces `trusted_system_directory() -> Path`, `POWERSHELL`, and `run_gate(*arguments, gate=GATE, env=None, cwd=ROOT, timeout=30) -> subprocess.CompletedProcess[str]` for every later black-box slice.
- Produces the final public parameter block and a dedicated Windows PowerShell 5.1 `-File` entrypoint. The temporary bootstrap failure is deliberately replaced in Task 2; it is not a success adapter.

- [ ] **Step 1: Lock the exact clean plan commit**

```powershell
$designBase = 'ed262771e740b2e502d30921ed92e1de1deb54b6'
$task75Start = (git rev-parse HEAD).Trim()
if ($LASTEXITCODE -ne 0 -or $task75Start -notmatch '^[0-9a-f]{40}$') {
  throw 'Could not record Task 7.5 start.'
}
$startStatus = @(git status --short)
if ($LASTEXITCODE -ne 0 -or $startStatus.Count -ne 0) {
  throw 'Task 7.5 must start clean.'
}
$startParent = (git rev-parse "$task75Start^").Trim()
if ($LASTEXITCODE -ne 0 -or $startParent -ne $designBase) {
  throw "Task 7.5 start is not the direct child of design base $designBase."
}
$planCommitCount = (git rev-list --count "$designBase..$task75Start").Trim()
if ($LASTEXITCODE -ne 0 -or $planCommitCount -ne '1') {
  throw "Expected one plan commit after the design base; observed $planCommitCount."
}
$planSubject = (git show -s --format=%s $task75Start).Trim()
if ($LASTEXITCODE -ne 0 -or $planSubject -ne 'docs: plan winter interlude executable gates') {
  throw "Unexpected implementation-plan commit subject: $planSubject"
}
$preImplementation = @(git diff --name-only "$designBase..$task75Start")
if ($LASTEXITCODE -ne 0) { throw 'Could not compare design and execution start.' }
if ($preImplementation.Count -ne 1 -or
    $preImplementation[0] -ne 'docs/superpowers/plans/2026-08-09-winter-interlude-executable-gates.md') {
  throw "Unexpected files between design and execution start: $($preImplementation -join ', ')"
}
$startEvidence = '.superpowers/sdd/task-7-5-start.txt'
$task75Start | Set-Content -LiteralPath $startEvidence -Encoding ascii -ErrorAction Stop
$recordedStart = (Get-Content -Raw -LiteralPath $startEvidence -ErrorAction Stop).Trim()
if ($recordedStart -ne $task75Start) { throw 'Task 7.5 start evidence did not round-trip.' }
```

Expected: clean tree; the design base has exactly one direct child with the exact plan subject and plan-only path; the full start SHA round-trips through ignored evidence.

#### Loop A: file existence and official PowerShell parsing

- [ ] **Step 2: Add only the parser-boundary test**

Create `Tools/test_winter_interlude_gate.py` with exactly:

```python
from __future__ import annotations

import ctypes
import os
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GATE = ROOT / "Tools" / "Run-WinterInterludeGate.ps1"
PLAN = ROOT / "docs" / "superpowers" / "plans" / "2026-08-08-governance-winter-interlude.md"


def trusted_system_directory() -> Path:
    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    get_system_directory = kernel32.GetSystemDirectoryW
    get_system_directory.argtypes = [ctypes.c_wchar_p, ctypes.c_uint]
    get_system_directory.restype = ctypes.c_uint
    size = 260
    while True:
        buffer = ctypes.create_unicode_buffer(size)
        written = get_system_directory(buffer, size)
        if written == 0:
            raise ctypes.WinError(ctypes.get_last_error())
        if written < size:
            return Path(buffer.value)
        size = written + 1


POWERSHELL = (
    trusted_system_directory()
    / "WindowsPowerShell"
    / "v1.0"
    / "powershell.exe"
)


def run_gate(
    *arguments: str,
    gate: Path = GATE,
    env: dict[str, str] | None = None,
    cwd: Path = ROOT,
    timeout: int = 30,
) -> subprocess.CompletedProcess[str]:
    merged = os.environ.copy()
    if env:
        merged.update(env)
    return subprocess.run(
        [
            str(POWERSHELL),
            "-NoLogo",
            "-NoProfile",
            "-NonInteractive",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            str(gate),
            *arguments,
        ],
        cwd=cwd,
        env=merged,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=timeout,
        check=False,
    )


class WinterInterludeGateBootstrapTests(unittest.TestCase):
    def test_script_exists_and_parses_with_official_powershell_parser(self):
        self.assertTrue(GATE.is_file(), f"missing public gate: {GATE}")
        parser = r"""
$tokens = $null
$errors = $null
[System.Management.Automation.Language.Parser]::ParseFile(
  $env:WINTER_GATE_PARSE_TARGET,
  [ref]$tokens,
  [ref]$errors
) | Out-Null
if ($errors.Count -ne 0) {
  $errors | ForEach-Object { [Console]::Error.WriteLine($_.Message) }
  exit 1
}
exit 0
"""
        completed = subprocess.run(
            [str(POWERSHELL), "-NoLogo", "-NoProfile", "-NonInteractive", "-Command", parser],
            cwd=ROOT,
            env={**os.environ, "WINTER_GATE_PARSE_TARGET": str(GATE)},
            text=True,
            encoding="utf-8",
            errors="replace",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=30,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 3: Run the parser-boundary RED**

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateBootstrapTests.test_script_exists_and_parses_with_official_powershell_parser `
  -v 2>&1 | Tee-Object -FilePath .superpowers/sdd/task-7-5-bootstrap-parser-red.txt
if ($LASTEXITCODE -eq 0) { throw 'Parser-boundary RED unexpectedly passed.' }
```

Expected RED: the one named method fails only because `Tools/Run-WinterInterludeGate.ps1` is absent; the module imports cleanly.

- [ ] **Step 4: Add the minimal parseable file**

Create `Tools/Run-WinterInterludeGate.ps1` with exactly:

```powershell
Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"
exit 0
```

Run:

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateBootstrapTests.test_script_exists_and_parses_with_official_powershell_parser `
  -v
if ($LASTEXITCODE -ne 0) { throw 'Parser-boundary GREEN failed.' }
```

Expected GREEN: the one named method passes. No public parameter or host behavior is claimed.

#### Loop B: public parameter binding

- [ ] **Step 5: Add only the parameter-contract test**

Insert this method after the parser-boundary method and before the module's final `if __name__ == "__main__"` block:

```python
    def test_parameter_contract_rejects_unknown_gate_and_out_of_range_timeouts(self):
        cases = (
            ("-Gate", "Unknown"),
            ("-Gate", "Structural", "-ToolTimeoutSeconds", "29"),
            ("-Gate", "Structural", "-ToolTimeoutSeconds", "1801"),
            ("-Gate", "Structural", "-RenPyTimeoutSeconds", "299"),
            ("-Gate", "Structural", "-RenPyTimeoutSeconds", "1801"),
        )
        for arguments in cases:
            with self.subTest(arguments=arguments):
                completed = run_gate(*arguments)
                self.assertNotEqual(completed.returncode, 0)
                self.assertNotIn("winter gate bootstrap reached", completed.stderr)
        valid = run_gate("-Gate", "Structural")
        self.assertEqual(valid.returncode, 0, valid.stderr)
```

- [ ] **Step 6: Run the parameter-binding RED**

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateBootstrapTests.test_parameter_contract_rejects_unknown_gate_and_out_of_range_timeouts `
  -v 2>&1 | Tee-Object -FilePath .superpowers/sdd/task-7-5-bootstrap-parameters-red.txt
if ($LASTEXITCODE -eq 0) { throw 'Parameter-binding RED unexpectedly passed.' }
```

Expected RED: all five subtests observe the minimal file's zero exit because no parameter contract exists yet.

- [ ] **Step 7: Add only the exact public parameter block**

Replace `Tools/Run-WinterInterludeGate.ps1` with exactly:

```powershell
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet("Structural", "Narrative")]
    [string]$Gate,
    [string]$ProjectRoot,
    [string]$RunRoot,
    [ValidateSet("Batch", "Final")]
    [string]$NarrativePhase = "Final",
    [ValidateRange(30, 1800)]
    [int]$ToolTimeoutSeconds = 300,
    [ValidateRange(300, 1800)]
    [int]$RenPyTimeoutSeconds = 300
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"
exit 0
```

Run:

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateBootstrapTests.test_parameter_contract_rejects_unknown_gate_and_out_of_range_timeouts `
  -v
if ($LASTEXITCODE -ne 0) { throw 'Parameter-binding GREEN failed.' }
```

Expected GREEN: all five invalid calls fail at PowerShell parameter binding, while the explicit valid-call control exits zero. An implementation that rejects every invocation cannot pass this loop. No host/path/process behavior is claimed.

#### Loop C: dedicated host and named implementation boundary

- [ ] **Step 8: Add the valid-call boundary and copied-host rejection tests**

First replace the valid-call control at the end of
`test_parameter_contract_rejects_unknown_gate_and_out_of_range_timeouts`.
Loop B proved that a valid parameter set reaches the script body while the
temporary body still exits zero; Loop C deliberately replaces that body with
the named fail-closed boundary, so the retained control must now prove the
same valid parameters reach that boundary rather than being rejected by
parameter binding:

```python
        valid = run_gate("-Gate", "Structural")
        self.assertEqual(valid.returncode, 1)
        self.assertIn("winter gate bootstrap reached", valid.stderr)
```

Insert this method after the parameter-contract method and before the module's final `if __name__ == "__main__"` block:

```python
    def test_valid_call_reaches_the_named_bootstrap_boundary(self):
        completed = run_gate("-Gate", "Structural")
        self.assertEqual(completed.returncode, 1)
        self.assertIn("winter gate bootstrap reached", completed.stderr)

    def test_copied_host_is_rejected_before_the_bootstrap_boundary(self):
        copied_host_dir = (
            Path(os.environ["TEMP"])
            / f"winter-gate-bootstrap-host-{os.getpid()}-{os.urandom(8).hex()}"
        )
        copied_host_dir.mkdir()
        copied_host = copied_host_dir / POWERSHELL.name
        copied_host.write_bytes(POWERSHELL.read_bytes())
        trusted_config = Path(str(POWERSHELL) + ".config")
        copied_config = Path(str(copied_host) + ".config")
        if trusted_config.is_file():
            copied_config.write_bytes(trusted_config.read_bytes())
        try:
            completed = subprocess.run(
                [
                    str(copied_host),
                    "-NoLogo",
                    "-NoProfile",
                    "-NonInteractive",
                    "-ExecutionPolicy",
                    "Bypass",
                    "-File",
                    str(GATE),
                    "-Gate",
                    "Structural",
                ],
                cwd=ROOT,
                env=os.environ.copy(),
                text=True,
                encoding="utf-8",
                errors="replace",
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=30,
                check=False,
            )
            self.assertNotEqual(completed.returncode, 0)
            self.assertIn(
                "trusted System-directory PowerShell",
                completed.stderr,
            )
            self.assertNotIn("winter gate bootstrap reached", completed.stderr)
        finally:
            if copied_config.exists():
                copied_config.unlink()
            if copied_host.exists():
                copied_host.unlink()
            copied_host_dir.rmdir()
```

- [ ] **Step 9: Run the host/boundary RED**

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateBootstrapTests.test_valid_call_reaches_the_named_bootstrap_boundary `
  Tools.test_winter_interlude_gate.WinterInterludeGateBootstrapTests.test_copied_host_is_rejected_before_the_bootstrap_boundary `
  -v 2>&1 | Tee-Object -FilePath .superpowers/sdd/task-7-5-bootstrap-host-red.txt
if ($LASTEXITCODE -eq 0) { throw 'Host/boundary RED unexpectedly passed.' }
```

Expected RED: the valid call exits zero and the copied host is not rejected with the required message because the dedicated-host assertion and named incomplete boundary do not exist.

- [ ] **Step 10: Add the exact dedicated-host skeleton**

Replace `Tools/Run-WinterInterludeGate.ps1` with exactly:

```powershell
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet("Structural", "Narrative")]
    [string]$Gate,
    [string]$ProjectRoot,
    [string]$RunRoot,
    [ValidateSet("Batch", "Final")]
    [string]$NarrativePhase = "Final",
    [ValidateRange(30, 1800)]
    [int]$ToolTimeoutSeconds = 300,
    [ValidateRange(300, 1800)]
    [int]$RenPyTimeoutSeconds = 300
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Assert-WinterGateBootstrapHost {
    if ($PSVersionTable.PSEdition -ne "Desktop" -or $PSVersionTable.PSVersion.Major -ne 5) {
        throw "Winter gate requires Windows PowerShell Desktop 5.1."
    }
    $trusted = Join-Path ([Environment]::SystemDirectory) "WindowsPowerShell\v1.0\powershell.exe"
    $current = (Get-Process -Id $PID -ErrorAction Stop).Path
    if (-not [string]::Equals(
        [IO.Path]::GetFullPath($current),
        [IO.Path]::GetFullPath($trusted),
        [StringComparison]::OrdinalIgnoreCase
    )) {
        throw "Winter gate host is not the trusted System-directory PowerShell."
    }
}

function Invoke-WinterInterludeGate {
    Assert-WinterGateBootstrapHost
    throw "winter gate bootstrap reached; path layer not implemented"
}

try {
    Invoke-WinterInterludeGate
    exit 0
}
catch {
    [Console]::Error.WriteLine($_.ToString())
    exit 1
}
```

- [ ] **Step 11: Run the focused boundary GREEN and full bootstrap regression**

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateBootstrapTests.test_valid_call_reaches_the_named_bootstrap_boundary `
  Tools.test_winter_interlude_gate.WinterInterludeGateBootstrapTests.test_copied_host_is_rejected_before_the_bootstrap_boundary `
  -v
if ($LASTEXITCODE -ne 0) { throw 'Host/boundary GREEN failed.' }
python -m unittest Tools.test_winter_interlude_gate.WinterInterludeGateBootstrapTests -v
if ($LASTEXITCODE -ne 0) { throw 'Complete bootstrap regression failed.' }
```

Expected GREEN: all 4 methods pass. Existence/parsing, bidirectional parameter binding, the trusted dedicated-host boundary, and copied-host rejection each have their own RED-to-GREEN proof. Omitting the host assertion or rejecting every invocation cannot pass. No path or child behavior is claimed yet.

- [ ] **Step 12: Create the single growing Task 7.5 commit**

```powershell
git add -- Tools/Run-WinterInterludeGate.ps1 Tools/test_winter_interlude_gate.py
if ($LASTEXITCODE -ne 0) { throw 'Bootstrap staging failed.' }
$bootstrapStaged = @(git diff --cached --name-only)
if ($LASTEXITCODE -ne 0) { throw 'Could not inspect bootstrap staging.' }
$expectedBootstrapStaged = @(
  'Tools/Run-WinterInterludeGate.ps1',
  'Tools/test_winter_interlude_gate.py'
)
if (@(Compare-Object ($expectedBootstrapStaged | Sort-Object) ($bootstrapStaged | Sort-Object)).Count -ne 0) {
  throw "Unexpected bootstrap staged paths: $($bootstrapStaged -join ', ')"
}
git diff --cached --check
if ($LASTEXITCODE -ne 0) { throw 'Bootstrap staged diff failed whitespace validation.' }
git commit -m "refactor: execute winter interlude gates from scripts"
if ($LASTEXITCODE -ne 0) { throw 'Bootstrap commit failed.' }
```

Expected: one two-file checkpoint commit. Every later task amends this same commit after its own GREEN gate, so the final Task 7.5 history still contains one atomic implementation commit.

---

### Task 2: Add final-object path identity and a verified external run tree

**Files:**
- Modify: `Tools/Run-WinterInterludeGate.ps1`
- Modify: `Tools/test_winter_interlude_gate.py`

**Interfaces:**
- Consumes: the Task 1 public script parameters and Python helpers `GATE`, `POWERSHELL`, and `run_gate(...)`.
- Produces: C# `WinterGate.PathIdentity`, `WinterGate.PathKind`, `WinterGate.WinterGatePathIdentityException`, and the `WinterGate.Native` static methods `GetPathIdentity`, `TryGetPathIdentity`, `CreateDirectoryExclusive(string, PathIdentity)`, `SameObject`, and `SameStablePath`.
- Produces: the shared `WinterGate.BoundedProcessResult` DTO and the internal C# bridge `Native.GetPathIdentityFromOpenHandle(IntPtr, PathKind)`. Task 3 first calls `GetPathIdentity(path, File, true)` to reject every parent or leaf reparse point, then uses its GENERIC_READ open and `SameStablePath` comparison. The same bridge validates the evidence-directory guard opened with `FILE_FLAG_OPEN_REPARSE_POINT` and without `FILE_SHARE_DELETE`.
- Produces: an independently compilable C# source with an empty exact `BEGIN PROCESS ENGINE` / `END PROCESS ENGINE` region. Task 3 replaces only that region; Task 2 does not declare or fake `RunProcessTree`.
- Produces: PowerShell `Assert-WinterGateHostIdentity`, `Resolve-GateProject`, `Get-ProtectedPlayerSavePaths`, `New-VerifiedRunRoot`, `New-VerifiedChildDirectory`, and `Assert-GatePathState`.
- `New-VerifiedRunRoot` returns a `PSCustomObject` with exactly `Identity`, `EvidenceIdentity`, and `SavedirsIdentity`. Later tasks retain these baseline objects and call `Assert-GatePathState` before every child launch and every evidence write.
- Every final path-identity failure throws `WinterGate.WinterGatePathIdentityException`. The top-level handler writes it only to gate stderr; later evidence code must not write through an identity that may have changed.
- This task is four independently runnable RED-to-GREEN loops. Do not add tests for a later loop before the preceding loop is GREEN.

#### Loop A: Classify absolute plain paths and move the bootstrap boundary

- [ ] **Step A1: Add only the plain-path RED tests and their fixture**

In `Tools/test_winter_interlude_gate.py`, add `import shutil` immediately after `import os` and `import tempfile` immediately after `import subprocess`.

Replace Task 1's complete `test_valid_call_reaches_the_named_bootstrap_boundary` method with:

```python
    def test_valid_call_reaches_plain_path_boundary(self):
        with tempfile.TemporaryDirectory(
            prefix="winter-gate-plain-boundary-"
        ) as owned_text:
            owned = Path(owned_text)
            project = owned / "project"
            (project / "Tools").mkdir(parents=True)
            completed = run_gate(
                "-Gate", "Structural",
                "-ProjectRoot", str(project),
                "-RunRoot", str(owned / "run"),
            )
            self.assertEqual(1, completed.returncode, completed.stdout)
            self.assertIn(
                "winter gate native identity layer not implemented",
                completed.stderr,
            )
            self.assertNotIn("winter gate bootstrap reached", completed.stderr)
```

Also replace the final valid-call control in
`test_parameter_contract_rejects_unknown_gate_and_out_of_range_timeouts` with
this layer-stable binding control. The separate boundary test above proves a
fully valid invocation reaches the current named implementation boundary;
this retained parameter test deliberately uses a syntactically valid public
argument set with a semantically invalid path so it remains fast and continues
to prove that PowerShell binding accepted the call after later tasks make the
Structural gate succeed:

```python
        valid_binding = run_gate(
            "-Gate", "Structural", "-ProjectRoot", "relative-project"
        )
        self.assertEqual(valid_binding.returncode, 1)
        self.assertIn("path identity", valid_binding.stderr.lower())
        self.assertNotIn("cannot validate argument", valid_binding.stderr.lower())
```

Immediately before `if __name__ == "__main__":`, add this first complete version of the path-safety fixture and its one Loop A behavior. Later loops insert methods into this same class; no future test is present yet.

```python
class WinterInterludeGatePathSafetyTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_root = Path(
            tempfile.mkdtemp(prefix="winter gate path (owned) apostrophe's ")
        )
        self.project = self.temp_root / "project"
        (self.project / "Tools").mkdir(parents=True)
        self.external = self.temp_root / "external"
        self.external.mkdir()
        self.process_temp = self.temp_root / "process-temp"
        self.process_temp.mkdir()
        self.appdata = self.temp_root / "process-appdata"
        self.appdata.mkdir()
        self.player_save = self.appdata / "RenPy" / "CourtOfShadows-save"
        self.player_save.mkdir(parents=True)
        self.child_record = self.temp_root / "child-started.txt"
        self.env = {
            "APPDATA": str(self.appdata),
            "TEMP": str(self.process_temp),
            "TMP": str(self.process_temp),
            "WINTER_GATE_CHILD_RECORD": str(self.child_record),
        }
        self.junctions: list[Path] = []

    def tearDown(self) -> None:
        # Remove only junction leaves, never their targets.  Recursive cleanup is
        # limited to the single temporary root owned by this test instance.
        for junction in reversed(self.junctions):
            if os.path.lexists(junction):
                os.rmdir(junction)
        shutil.rmtree(self.temp_root)

    def invoke(
        self,
        run_root: str | None,
        project_root: Path | None = None,
        *,
        gate: Path = GATE,
        cwd: Path | None = None,
        include_project_root: bool = True,
    ):
        arguments = ["-Gate", "Structural"]
        if include_project_root:
            arguments.extend(("-ProjectRoot", str(project_root or self.project)))
        if run_root is not None:
            arguments.extend(("-RunRoot", run_root))
        return run_gate(
            *arguments,
            gate=gate,
            env=self.env,
            cwd=cwd or self.temp_root,
        )

    def assert_path_rejected(
        self,
        result: subprocess.CompletedProcess[str],
    ) -> None:
        self.assertNotEqual(0, result.returncode, result.stdout)
        self.assertIn("path identity", result.stderr.lower(), result.stderr)
        self.assertFalse(
            self.child_record.exists(),
            "a child process started before path validation completed",
        )

    def test_rejects_relative_drive_relative_and_device_runroots(self) -> None:
        drive = POWERSHELL.drive
        cases = (
            r"relative\run",
            r"\rooted-current-drive",
            r"/rooted-current-drive",
            f"{drive}drive-relative",
            rf"\\?\{drive}\device-path",
            rf"\\.\{drive}\device-path",
        )
        for candidate in cases:
            with self.subTest(candidate=candidate):
                self.assert_path_rejected(self.invoke(candidate))

    def test_rejects_nonplain_unresolved_runroot_components(self) -> None:
        base = str(self.external)
        cases = (
            base + r"\one\..\run",
            base + r"\\double-separator\run",
            base + r"\wild*card\run",
            base + "\\trailing-dot.\\run",
            base + "\\trailing-space \\run",
        )
        for candidate in cases:
            with self.subTest(candidate=candidate):
                self.assert_path_rejected(self.invoke(candidate))
```

- [ ] **Step A2: Run the public plain-path RED**

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateBootstrapTests.test_valid_call_reaches_plain_path_boundary `
  Tools.test_winter_interlude_gate.WinterInterludeGatePathSafetyTests.test_rejects_relative_drive_relative_and_device_runroots `
  Tools.test_winter_interlude_gate.WinterInterludeGatePathSafetyTests.test_rejects_nonplain_unresolved_runroot_components -v 2>&1 |
  Tee-Object -FilePath .superpowers/sdd/task-7-5-path-a-red.txt
if ($LASTEXITCODE -eq 0) { throw 'Loop A RED unexpectedly passed.' }
```

Expected: `Ran 3 tests` and FAIL. The boundary assertion sees Task 1's exact `winter gate bootstrap reached; path layer not implemented` message. Every relative, current-drive-rooted, drive-relative, device, dot-component, empty-component, wildcard, and trailing-dot/space RunRoot also reaches that old boundary instead of an assertion-specific `path identity` rejection. No child record is created.

- [ ] **Step A3: Add the minimal lexical classifier**

Immediately after the public `param(...)` block, add:

```powershell
$projectRootWasSpecified = $PSBoundParameters.ContainsKey('ProjectRoot')
$runRootWasSpecified = $PSBoundParameters.ContainsKey('RunRoot')
```

Immediately after `$ErrorActionPreference = "Stop"`, add this temporary typed-independent error helper. Loop B replaces it after the native exception type exists.

```powershell
function Throw-GatePathIdentityError {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [string]$Message,
        [Parameter(Position = 1)]
        [System.Exception]$InnerException
    )

    $fullMessage = "path identity: $Message"
    if ($null -eq $InnerException) {
        throw [System.ArgumentException]::new($fullMessage)
    }
    throw [System.ArgumentException]::new($fullMessage, $InnerException)
}
```

Add the final lexical classifier and plain-child validator immediately after that helper:

```powershell
function Get-NormalizedAbsolutePlainPath {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [string]$Path,
        [Parameter(Mandatory = $true, Position = 1)]
        [string]$Label
    )

    if ([string]::IsNullOrWhiteSpace($Path)) {
        Throw-GatePathIdentityError "$Label is empty"
    }
    if ($Path.StartsWith('\\?\', [System.StringComparison]::OrdinalIgnoreCase) -or
        $Path.StartsWith('\\.\', [System.StringComparison]::OrdinalIgnoreCase)) {
        Throw-GatePathIdentityError "$Label must not use a device path: $Path"
    }
    if (($Path.StartsWith('\', [System.StringComparison]::Ordinal) -and
         -not $Path.StartsWith('\\', [System.StringComparison]::Ordinal)) -or
        $Path.StartsWith('/', [System.StringComparison]::Ordinal)) {
        Throw-GatePathIdentityError `
            "$Label must not be rooted on the current drive: $Path"
    }
    if ($Path -match '^[A-Za-z]:(?![\\/])') {
        Throw-GatePathIdentityError "$Label must not be drive-relative: $Path"
    }
    if (-not [System.IO.Path]::IsPathRooted($Path)) {
        Throw-GatePathIdentityError "$Label must be absolute: $Path"
    }

    try {
        $fullPath = [System.IO.Path]::GetFullPath($Path)
        $root = [System.IO.Path]::GetPathRoot($fullPath)
    }
    catch {
        Throw-GatePathIdentityError "$Label is invalid: $Path" $_.Exception
    }
    if ([string]::IsNullOrEmpty($root)) {
        Throw-GatePathIdentityError "$Label has no root: $Path"
    }

    $rawRoot = [System.IO.Path]::GetPathRoot($Path)
    $rawRemainder = $Path.Substring($rawRoot.Length)
    if ($rawRemainder -match '[\\/]{2,}') {
        Throw-GatePathIdentityError "$Label contains an empty component: $Path"
    }
    $invalid = [System.IO.Path]::GetInvalidFileNameChars()
    foreach ($component in $rawRemainder.Split(
        [char[]]@('\', '/'),
        [System.StringSplitOptions]::RemoveEmptyEntries)) {
        if ($component -eq '.' -or $component -eq '..') {
            Throw-GatePathIdentityError "$Label contains a dot component: $Path"
        }
        if ($component.IndexOfAny($invalid) -ge 0 -or
            [System.Management.Automation.WildcardPattern]::ContainsWildcardCharacters(
                $component)) {
            Throw-GatePathIdentityError "$Label contains an invalid component: $Path"
        }
        if ($component.TrimEnd([char[]]@(' ', '.')) -ne $component) {
            Throw-GatePathIdentityError "$Label contains an aliased trailing character: $Path"
        }
    }

    if ($fullPath.Length -gt $root.Length) {
        $fullPath = $fullPath.TrimEnd([char[]]@('\', '/'))
    }
    return $fullPath
}

function Assert-PlainChildName {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [string]$LeafName,
        [Parameter(Mandatory = $true, Position = 1)]
        [string]$Label
    )

    if ([string]::IsNullOrWhiteSpace($LeafName) -or
        $LeafName -eq '.' -or
        $LeafName -eq '..' -or
        $LeafName.IndexOfAny([char[]]@('\', '/')) -ge 0 -or
        $LeafName.IndexOfAny([System.IO.Path]::GetInvalidFileNameChars()) -ge 0 -or
        [System.Management.Automation.WildcardPattern]::ContainsWildcardCharacters(
            $LeafName) -or
        $LeafName.TrimEnd([char[]]@(' ', '.')) -ne $LeafName) {
        Throw-GatePathIdentityError "$Label is not one plain path component: $LeafName"
    }
}
```

Replace only Task 1's `Invoke-WinterInterludeGate` with this Loop A implementation:

```powershell
function Invoke-WinterInterludeGate {
    Assert-WinterGateBootstrapHost
    if ($projectRootWasSpecified) {
        [void](Get-NormalizedAbsolutePlainPath $ProjectRoot 'ProjectRoot')
    }
    else {
        [void](Get-NormalizedAbsolutePlainPath (
            [System.IO.Path]::GetFullPath(
                [System.IO.Path]::Combine($PSScriptRoot, '..')
            )
        ) 'ProjectRoot')
    }

    if ($runRootWasSpecified) {
        [void](Get-NormalizedAbsolutePlainPath $RunRoot 'RunRoot')
    }
    else {
        [void](Get-NormalizedAbsolutePlainPath (
            [System.IO.Path]::Combine(
                [System.IO.Path]::GetTempPath(),
                [System.Guid]::NewGuid().ToString('N').ToLowerInvariant()
            )
        ) 'RunRoot')
    }
    throw 'winter gate native identity layer not implemented'
}
```

This is the minimal Loop A GREEN: it normalizes only plain absolute caller paths, derives defaults from `$PSScriptRoot` and the process OS temp directory, and deliberately performs no filesystem identity or creation operation.

- [ ] **Step A4: Run Loop A GREEN and guard Task 1 contracts**

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateBootstrapTests.test_valid_call_reaches_plain_path_boundary `
  Tools.test_winter_interlude_gate.WinterInterludeGatePathSafetyTests.test_rejects_relative_drive_relative_and_device_runroots `
  Tools.test_winter_interlude_gate.WinterInterludeGatePathSafetyTests.test_rejects_nonplain_unresolved_runroot_components -v
if ($LASTEXITCODE -ne 0) { throw 'Loop A GREEN failed.' }

python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateBootstrapTests.test_script_exists_and_parses_with_official_powershell_parser `
  Tools.test_winter_interlude_gate.WinterInterludeGateBootstrapTests.test_parameter_contract_rejects_unknown_gate_and_out_of_range_timeouts -v
if ($LASTEXITCODE -ne 0) { throw 'Task 1 public contracts regressed in Loop A.' }
```

Expected: all 3 Loop A tests and both retained Task 1 contract tests pass. Invalid roots fail before the named native-identity boundary and before `child-started.txt` exists.

#### Loop B: Resolve final-object identity, hold ancestor guards, and reject reparse-routed chains

- [ ] **Step B1: Add only the native-chain RED tests**

At the top of `Tools/test_winter_interlude_gate.py`, add `from ctypes import wintypes` after the future import, `import re` immediately after `import os`, `import threading` immediately after `import shutil`, and `import time` immediately after `import tempfile`. Immediately before `WinterInterludeGatePathSafetyTests`, add the compiler lookup and deterministic held-chain harness helper:

```python
def _framework_csc() -> Path:
    windows = POWERSHELL.parents[3]
    candidates = (
        windows / "Microsoft.NET" / "Framework64" / "v4.0.30319" / "csc.exe",
        windows / "Microsoft.NET" / "Framework" / "v4.0.30319" / "csc.exe",
    )
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    raise AssertionError(".NET Framework 4.x csc.exe is unavailable")


def _production_native_source() -> str:
    gate_text = GATE.read_text(encoding="utf-8").replace("\r\n", "\n")
    native_match = re.search(
        r"(?ms)^\s*\$nativeSource\s*=\s*@'\n(?P<source>.*?)\n'@\s*$",
        gate_text,
    )
    if native_match is None:
        raise AssertionError("Could not extract the production native source")
    return native_match.group("source")


def _compile_csharp(
    executable: Path,
    source_text: str,
    *,
    main: str | None,
    label: str,
) -> None:
    source = executable.with_suffix(".cs")
    source.write_text(source_text, encoding="utf-8")
    command = [
        str(_framework_csc()),
        "/nologo",
        "/target:exe",
    ]
    if main is not None:
        command.append(f"/main:{main}")
    command.extend((f"/out:{executable}", str(source)))
    completed = subprocess.run(
        command,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if completed.returncode != 0:
        raise AssertionError(f"Could not compile {label}:\n{completed.stdout}")


def _compile_held_chain_harness(executable: Path) -> None:
    needle = (
        "                    chain.Handles.Add(handle);\n"
        "                    PathKind componentKind ="
    )
    native_source = _production_native_source()
    if native_source.count(needle) != 1:
        raise AssertionError("HeldPathChain hook point drifted")
    instrumented = native_source.replace(
        needle,
        "                    chain.Handles.Add(handle);\n"
        "                    TestPauseAfterHeldHandle(component);\n"
        "                    PathKind componentKind =",
    )
    harness_source = instrumented + r'''

namespace WinterGate
{
    public static partial class Native
    {
        internal static string TestHeldPath;
        internal static string TestReadyPath;
        internal static string TestReleasePath;

        internal static void TestPauseAfterHeldHandle(string component)
        {
            if (!String.Equals(
                Path.GetFullPath(component),
                TestHeldPath,
                StringComparison.OrdinalIgnoreCase))
            {
                return;
            }
            File.WriteAllText(TestReadyPath, "opened");
            DateTime deadline = DateTime.UtcNow.AddSeconds(20);
            while (!File.Exists(TestReleasePath))
            {
                if (DateTime.UtcNow >= deadline)
                {
                    throw new Exception("test release timeout");
                }
                System.Threading.Thread.Sleep(5);
            }
        }
    }

    internal static class HeldChainHarness
    {
        public static int Main(string[] args)
        {
            if (args.Length != 5)
            {
                return 90;
            }
            Native.TestHeldPath = Path.GetFullPath(args[1]);
            Native.TestReadyPath = args[2];
            Native.TestReleasePath = args[3];
            try
            {
                Native.GetPathIdentity(args[0], PathKind.Directory, true);
                File.WriteAllText(args[4], "finished");
                return 0;
            }
            catch (Exception exception)
            {
                File.WriteAllText(args[4], exception.ToString());
                return 91;
            }
        }
    }
}
'''
    _compile_csharp(
        executable,
        harness_source,
        main="WinterGate.HeldChainHarness",
        label="held-chain harness",
    )
```

Replace `test_valid_call_reaches_plain_path_boundary` with:

```python
    def test_valid_call_reaches_native_chain_boundary(self):
        with tempfile.TemporaryDirectory(
            prefix="winter-gate-native-boundary-"
        ) as owned_text:
            owned = Path(owned_text)
            project = owned / "project"
            (project / "Tools").mkdir(parents=True)
            completed = run_gate(
                "-Gate", "Structural",
                "-ProjectRoot", str(project),
                "-RunRoot", str(owned / "run"),
            )
            self.assertEqual(1, completed.returncode, completed.stdout)
            self.assertIn(
                "winter gate trusted-host/player-save layer not implemented",
                completed.stderr,
            )
            self.assertNotIn(
                "winter gate native identity layer not implemented",
                completed.stderr,
            )
```

Inside `WinterInterludeGatePathSafetyTests`, insert the exact junction helper and these Loop B methods after `tearDown`:

```python
    def make_junction(self, link: Path, target: Path) -> None:
        script = self.temp_root / f"junction-{len(self.junctions)}.ps1"
        script.write_text(
            "param([string]$Link, [string]$Target)\n"
            "$ErrorActionPreference = 'Stop'\n"
            "New-Item -ItemType Junction -Path $Link -Target $Target "
            "| Out-Null\n",
            encoding="utf-8",
        )
        completed = subprocess.run(
            [
                str(POWERSHELL),
                "-NoLogo",
                "-NoProfile",
                "-NonInteractive",
                "-ExecutionPolicy",
                "Bypass",
                "-File",
                str(script),
                str(link),
                str(target),
            ],
            text=True,
            encoding="utf-8",
            errors="replace",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.junctions.append(link)
```

```python
    def test_native_full_chain_contract_precedes_creation(self) -> None:
        source = GATE.read_text(encoding="utf-8")
        for declaration in (
            "sealed class PathIdentity",
            "enum PathKind",
            "sealed class WinterGatePathIdentityException",
            "partial class Native",
            "GetPathIdentity(",
            "TryGetPathIdentity(",
            "SameObject(",
            "SameStablePath(",
            "GetPathIdentityFromOpenHandle(",
            "// BEGIN PROCESS ENGINE",
            "// END PROCESS ENGINE",
        ):
            self.assertIn(declaration, source)
        self.assertNotIn("CreateDirectoryExclusive(", source)
        self.assertNotIn("RunProcessTree(", source)

    def test_rejects_preexisting_empty_and_nonempty_runroots(self) -> None:
        empty = self.external / "already-empty"
        empty.mkdir()
        nonempty = self.external / "already-nonempty"
        nonempty.mkdir()
        marker = nonempty / "owned-marker.txt"
        marker.write_text("keep", encoding="utf-8")
        for candidate in (empty, nonempty):
            with self.subTest(candidate=candidate):
                self.assert_path_rejected(self.invoke(str(candidate)))
        self.assertEqual("keep", marker.read_text(encoding="utf-8"))

    def test_rejects_missing_file_relative_and_junction_projectroots(self) -> None:
        project_file = self.temp_root / "project-file"
        project_file.write_text("not a directory", encoding="utf-8")
        project_link = self.temp_root / "project-junction"
        self.make_junction(project_link, self.project)
        cases = (
            self.temp_root / "missing-project",
            project_file,
            Path("relative-project"),
            r"\rooted-current-drive-project",
            r"/rooted-current-drive-project",
            project_link,
        )
        for index, project_root in enumerate(cases):
            with self.subTest(project_root=project_root):
                run_root = self.external / f"project-reject-{index}"
                self.assert_path_rejected(
                    self.invoke(str(run_root), project_root=project_root)
                )
                self.assertFalse(run_root.exists())

    def test_rejects_junction_routed_runroot_ancestors(self) -> None:
        project_link = self.temp_root / "route-to-project"
        save_link = self.temp_root / "route-to-save"
        self.make_junction(project_link, self.project)
        self.make_junction(save_link, self.player_save)
        cases = (
            (project_link / "new-run", self.project / "new-run"),
            (save_link / "new-run", self.player_save / "new-run"),
        )
        for candidate, target in cases:
            with self.subTest(candidate=candidate):
                self.assert_path_rejected(self.invoke(str(candidate)))
                self.assertFalse(target.exists())

    def test_rejects_a_preexisting_junction_as_runroot_leaf(self) -> None:
        target = self.external / "junction-target"
        target.mkdir()
        link = self.temp_root / "runroot-junction"
        self.make_junction(link, target)
        self.assert_path_rejected(self.invoke(str(link)))
        self.assertEqual([], list(target.iterdir()))

    def test_exact_native_chain_holds_ancestor_until_leaf_identity(self) -> None:
        guarded = self.temp_root / "guarded-ancestor"
        deep_project = guarded / "deep" / "project"
        deep_project.mkdir(parents=True)
        moved = self.temp_root / "guarded-ancestor-moved"
        ready = self.temp_root / "held-chain-ready"
        release = self.temp_root / "held-chain-release"
        finished = self.temp_root / "held-chain-finished"
        executable = self.temp_root / "held-chain-harness.exe"
        _compile_held_chain_harness(executable)

        process = subprocess.Popen(
            [
                str(executable),
                str(deep_project),
                str(guarded),
                str(ready),
                str(release),
                str(finished),
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        try:
            deadline = time.monotonic() + 20
            while not ready.exists() and time.monotonic() < deadline:
                time.sleep(0.005)
            self.assertTrue(ready.is_file(), "chosen ancestor was never opened")
            self.assertIsNone(process.poll(), "chain ended before leaf capture")
            self.assertFalse(finished.exists())
            with self.assertRaises(PermissionError):
                os.replace(guarded, moved)
        finally:
            release.write_text("release", encoding="utf-8")
            try:
                stdout, stderr = process.communicate(timeout=20)
            except subprocess.TimeoutExpired:
                process.kill()
                process.communicate(timeout=5)
                raise

        self.assertEqual(0, process.returncode, stdout + stderr)
        self.assertEqual("finished", finished.read_text(encoding="utf-8"))
        os.replace(guarded, moved)
        os.replace(moved, guarded)
```

- [ ] **Step B2: Run the native-chain RED**

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateBootstrapTests.test_valid_call_reaches_native_chain_boundary `
  Tools.test_winter_interlude_gate.WinterInterludeGatePathSafetyTests.test_native_full_chain_contract_precedes_creation `
  Tools.test_winter_interlude_gate.WinterInterludeGatePathSafetyTests.test_rejects_preexisting_empty_and_nonempty_runroots `
  Tools.test_winter_interlude_gate.WinterInterludeGatePathSafetyTests.test_rejects_missing_file_relative_and_junction_projectroots `
  Tools.test_winter_interlude_gate.WinterInterludeGatePathSafetyTests.test_rejects_junction_routed_runroot_ancestors `
  Tools.test_winter_interlude_gate.WinterInterludeGatePathSafetyTests.test_rejects_a_preexisting_junction_as_runroot_leaf `
  Tools.test_winter_interlude_gate.WinterInterludeGatePathSafetyTests.test_exact_native_chain_holds_ancestor_until_leaf_identity -v 2>&1 |
  Tee-Object -FilePath .superpowers/sdd/task-7-5-path-b-red.txt
if ($LASTEXITCODE -eq 0) { throw 'Loop B RED unexpectedly passed.' }
```

Expected: `Ran 7 tests` and FAIL. The valid call remains at Loop A; the native interface is absent; pre-existing, wrong-kind, or junction-routed objects are not rejected from opened final identity; and the synchronized probe never observes an ancestor held without `FILE_SHARE_DELETE`. Junction setup succeeds and no child record appears.

- [ ] **Step B3: Add the independently compilable native identity core**

Insert the following function immediately before `Throw-GatePathIdentityError`. This is the final Task 2 native source except for the exclusive-create declaration and method added by Loop D under its public RED.

```powershell
function Add-WinterGateNativeTypes {
    if ($null -ne ("WinterGate.Native" -as [type])) {
        return
    }
    $nativeSource = @'
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.IO;
using System.Runtime.InteropServices;
using System.Text;
using Microsoft.Win32.SafeHandles;

namespace WinterGate
{
    public enum PathKind
    {
        File,
        Directory
    }

    public sealed class PathIdentity
    {
        public string FinalPath;
        public uint VolumeSerialNumber;
        public ulong FileIndex;
        public FileAttributes Attributes;
    }

    public sealed class BoundedProcessResult
    {
        public bool ProcessStarted;
        public int? ProcessId;
        public DateTime? StartedUtc;
        public DateTime? EndedUtc;
        public long? ElapsedMilliseconds;
        public int? ExitCode;
        public bool TimedOut;
        public bool TreeDrained;
        public bool HadLiveDescendantsAfterRootExit;
        public string StartError;
    }

    [Serializable]
    public sealed class WinterGatePathIdentityException : Exception
    {
        public int NativeErrorCode { get; private set; }

        public WinterGatePathIdentityException(string message)
            : base(message)
        {
        }

        public WinterGatePathIdentityException(
            string message,
            int nativeErrorCode,
            Exception innerException)
            : base(message, innerException)
        {
            NativeErrorCode = nativeErrorCode;
        }

        private WinterGatePathIdentityException(
            System.Runtime.Serialization.SerializationInfo info,
            System.Runtime.Serialization.StreamingContext context)
            : base(info, context)
        {
            NativeErrorCode = info.GetInt32("NativeErrorCode");
        }

        public override void GetObjectData(
            System.Runtime.Serialization.SerializationInfo info,
            System.Runtime.Serialization.StreamingContext context)
        {
            if (info == null)
            {
                throw new ArgumentNullException("info");
            }
            info.AddValue("NativeErrorCode", NativeErrorCode);
            base.GetObjectData(info, context);
        }
    }

    public static partial class Native
    {
        private const uint FILE_READ_DATA = 0x00000001;
        private const uint FILE_SHARE_READ = 0x00000001;
        private const uint FILE_SHARE_WRITE = 0x00000002;
        private const uint OPEN_EXISTING = 3;
        private const uint FILE_FLAG_BACKUP_SEMANTICS = 0x02000000;
        private const uint FILE_FLAG_OPEN_REPARSE_POINT = 0x00200000;
        private const int ERROR_FILE_NOT_FOUND = 2;
        private const int ERROR_PATH_NOT_FOUND = 3;

        private sealed class HeldPathChain : IDisposable
        {
            internal readonly List<SafeFileHandle> Handles =
                new List<SafeFileHandle>();
            internal PathIdentity LeafIdentity;

            public void Dispose()
            {
                for (int index = Handles.Count - 1; index >= 0; index--)
                {
                    Handles[index].Dispose();
                }
                Handles.Clear();
            }
        }

        [StructLayout(LayoutKind.Sequential)]
        private struct FILETIME
        {
            public uint LowDateTime;
            public uint HighDateTime;
        }

        [StructLayout(LayoutKind.Sequential)]
        private struct BY_HANDLE_FILE_INFORMATION
        {
            public uint FileAttributes;
            public FILETIME CreationTime;
            public FILETIME LastAccessTime;
            public FILETIME LastWriteTime;
            public uint VolumeSerialNumber;
            public uint FileSizeHigh;
            public uint FileSizeLow;
            public uint NumberOfLinks;
            public uint FileIndexHigh;
            public uint FileIndexLow;
        }

        [DllImport("kernel32.dll", CharSet = CharSet.Unicode, SetLastError = true)]
        private static extern SafeFileHandle CreateFileW(
            string fileName,
            uint desiredAccess,
            uint shareMode,
            IntPtr securityAttributes,
            uint creationDisposition,
            uint flagsAndAttributes,
            IntPtr templateFile);

        [DllImport("kernel32.dll", SetLastError = true)]
        [return: MarshalAs(UnmanagedType.Bool)]
        private static extern bool GetFileInformationByHandle(
            SafeFileHandle file,
            out BY_HANDLE_FILE_INFORMATION information);

        [DllImport("kernel32.dll", CharSet = CharSet.Unicode, SetLastError = true)]
        private static extern uint GetFinalPathNameByHandleW(
            SafeFileHandle file,
            StringBuilder path,
            uint pathLength,
            uint flags);

        public static PathIdentity GetPathIdentity(
            string path,
            PathKind expectedKind,
            bool rejectAnyReparseComponent)
        {
            string fullPath = RequireAbsoluteNonDevicePath(path);
            using (HeldPathChain chain = OpenExistingPathChain(
                fullPath,
                expectedKind,
                rejectAnyReparseComponent))
            {
                return chain.LeafIdentity;
            }
        }

        public static PathIdentity TryGetPathIdentity(
            string path,
            PathKind expectedKind,
            bool rejectAnyReparseComponent)
        {
            try
            {
                return GetPathIdentity(
                    path,
                    expectedKind,
                    rejectAnyReparseComponent);
            }
            catch (WinterGatePathIdentityException exception)
            {
                if (exception.NativeErrorCode == ERROR_FILE_NOT_FOUND ||
                    exception.NativeErrorCode == ERROR_PATH_NOT_FOUND)
                {
                    return null;
                }
                throw;
            }
        }

        public static bool SameObject(PathIdentity left, PathIdentity right)
        {
            return left != null &&
                right != null &&
                left.VolumeSerialNumber == right.VolumeSerialNumber &&
                left.FileIndex == right.FileIndex;
        }

        public static bool SameStablePath(PathIdentity left, PathIdentity right)
        {
            return SameObject(left, right) &&
                String.Equals(
                    NormalizeComparableFinalPath(left.FinalPath),
                    NormalizeComparableFinalPath(right.FinalPath),
                    StringComparison.OrdinalIgnoreCase);
        }

        internal static PathIdentity GetPathIdentityFromOpenHandle(
            IntPtr handle,
            PathKind expectedKind)
        {
            if (handle == IntPtr.Zero || handle == new IntPtr(-1))
            {
                throw new WinterGatePathIdentityException(
                    "path identity: invalid open handle");
            }

            using (SafeFileHandle borrowed = new SafeFileHandle(handle, false))
            {
                return ReadPathIdentityFromHandle(
                    borrowed,
                    expectedKind,
                    true,
                    "<open handle>");
            }
        }

        // BEGIN PROCESS ENGINE
        // END PROCESS ENGINE

        private static string RequireAbsoluteNonDevicePath(string path)
        {
            if (String.IsNullOrWhiteSpace(path))
            {
                throw new WinterGatePathIdentityException(
                    "path identity: path is empty");
            }
            if (path.StartsWith(@"\\?\", StringComparison.OrdinalIgnoreCase) ||
                path.StartsWith(@"\\.\", StringComparison.OrdinalIgnoreCase))
            {
                throw new WinterGatePathIdentityException(
                    "path identity: device paths are not accepted: " + path);
            }
            if (IsDirectorySeparator(path[0]) &&
                !(path.Length >= 2 && path[0] == '\\' && path[1] == '\\'))
            {
                throw new WinterGatePathIdentityException(
                    "path identity: current-drive-rooted paths are not accepted: " +
                    path);
            }
            if (path.Length >= 2 &&
                path[1] == ':' &&
                (path.Length == 2 || !IsDirectorySeparator(path[2])))
            {
                throw new WinterGatePathIdentityException(
                    "path identity: drive-relative paths are not accepted: " + path);
            }
            if (!Path.IsPathRooted(path))
            {
                throw new WinterGatePathIdentityException(
                    "path identity: absolute path required: " + path);
            }

            try
            {
                string fullPath = Path.GetFullPath(path);
                if (fullPath.StartsWith(@"\\?\", StringComparison.OrdinalIgnoreCase) ||
                    fullPath.StartsWith(@"\\.\", StringComparison.OrdinalIgnoreCase))
                {
                    throw new WinterGatePathIdentityException(
                        "path identity: device paths are not accepted: " + path);
                }
                return TrimEndingSeparatorsExceptRoot(fullPath);
            }
            catch (WinterGatePathIdentityException)
            {
                throw;
            }
            catch (Exception exception)
            {
                throw new WinterGatePathIdentityException(
                    "path identity: invalid absolute path: " + path,
                    0,
                    exception);
            }
        }

        private static List<string> BuildComponentPaths(string fullPath)
        {
            string root = Path.GetPathRoot(fullPath);
            if (String.IsNullOrEmpty(root))
            {
                throw new WinterGatePathIdentityException(
                    "path identity: path has no root: " + fullPath);
            }

            List<string> paths = new List<string>();
            string current = root;
            paths.Add(current);
            string remainder = fullPath.Substring(root.Length);
            string[] parts = remainder.Split(
                new[] { Path.DirectorySeparatorChar, Path.AltDirectorySeparatorChar },
                StringSplitOptions.RemoveEmptyEntries);
            foreach (string part in parts)
            {
                current = Path.Combine(current, part);
                paths.Add(current);
            }
            return paths;
        }

        private static HeldPathChain OpenExistingPathChain(
            string fullPath,
            PathKind expectedLeafKind,
            bool rejectAnyReparseComponent)
        {
            List<string> components = BuildComponentPaths(fullPath);
            HeldPathChain chain = new HeldPathChain();
            PathIdentity currentIdentity = null;
            try
            {
                for (int index = 0; index < components.Count; index++)
                {
                    bool isLeaf = index == components.Count - 1;
                    string component;
                    if (index == 0)
                    {
                        component = components[0];
                    }
                    else
                    {
                        string leafName = Path.GetFileName(components[index]);
                        component = Path.Combine(
                            currentIdentity.FinalPath,
                            leafName);
                    }

                    SafeFileHandle handle = OpenPathHandle(
                        component,
                        rejectAnyReparseComponent);
                    chain.Handles.Add(handle);
                    PathKind componentKind =
                        isLeaf ? expectedLeafKind : PathKind.Directory;
                    PathIdentity openedIdentity = ReadPathIdentityFromHandle(
                        handle,
                        componentKind,
                        rejectAnyReparseComponent,
                        component);
                    if (index > 0 &&
                        !String.Equals(
                            NormalizeComparableFinalPath(component),
                            openedIdentity.FinalPath,
                            StringComparison.OrdinalIgnoreCase))
                    {
                        throw new WinterGatePathIdentityException(
                            "path identity: component final path changed while " +
                            "resolving: " + component);
                    }
                    currentIdentity = openedIdentity;
                }

                if (currentIdentity == null)
                {
                    throw new WinterGatePathIdentityException(
                        "path identity: no leaf object was resolved: " + fullPath);
                }
                chain.LeafIdentity = currentIdentity;
                return chain;
            }
            catch
            {
                chain.Dispose();
                throw;
            }
        }

        private static SafeFileHandle OpenPathHandle(
            string path,
            bool rejectReparse)
        {
            uint flags = FILE_FLAG_BACKUP_SEMANTICS;
            if (rejectReparse)
            {
                flags |= FILE_FLAG_OPEN_REPARSE_POINT;
            }
            SafeFileHandle handle = CreateFileW(
                path,
                FILE_READ_DATA,
                FILE_SHARE_READ | FILE_SHARE_WRITE,
                IntPtr.Zero,
                OPEN_EXISTING,
                flags,
                IntPtr.Zero);
            if (handle.IsInvalid)
            {
                int error = Marshal.GetLastWin32Error();
                handle.Dispose();
                throw NativePathError("open", path, error);
            }
            return handle;
        }

        private static PathIdentity ReadPathIdentityFromHandle(
            SafeFileHandle handle,
            PathKind expectedKind,
            bool rejectReparse,
            string displayPath)
        {
            BY_HANDLE_FILE_INFORMATION information;
            if (!GetFileInformationByHandle(handle, out information))
            {
                int error = Marshal.GetLastWin32Error();
                throw NativePathError("inspect", displayPath, error);
            }
            FileAttributes attributes =
                (FileAttributes)information.FileAttributes;
            if (rejectReparse &&
                (attributes & FileAttributes.ReparsePoint) != 0)
            {
                throw new WinterGatePathIdentityException(
                    "path identity: reparse component rejected: " + displayPath);
            }
            bool isDirectory =
                (attributes & FileAttributes.Directory) != 0;
            bool expectedDirectory = expectedKind == PathKind.Directory;
            if (isDirectory != expectedDirectory)
            {
                throw new WinterGatePathIdentityException(
                    "path identity: expected " +
                    expectedKind.ToString().ToLowerInvariant() +
                    ": " + displayPath);
            }
            return new PathIdentity
            {
                FinalPath = GetNormalizedFinalPath(handle, displayPath),
                VolumeSerialNumber = information.VolumeSerialNumber,
                FileIndex =
                    ((ulong)information.FileIndexHigh << 32) |
                    information.FileIndexLow,
                Attributes = attributes
            };
        }

        private static string GetNormalizedFinalPath(
            SafeFileHandle handle,
            string displayPath)
        {
            int capacity = 512;
            while (true)
            {
                StringBuilder buffer = new StringBuilder(capacity);
                uint written = GetFinalPathNameByHandleW(
                    handle,
                    buffer,
                    (uint)buffer.Capacity,
                    0);
                if (written == 0)
                {
                    int error = Marshal.GetLastWin32Error();
                    throw NativePathError("resolve final path", displayPath, error);
                }
                if (written < buffer.Capacity)
                {
                    return NormalizeComparableFinalPath(buffer.ToString());
                }
                if (written > Int32.MaxValue - 1)
                {
                    throw new WinterGatePathIdentityException(
                        "path identity: final path is too long: " + displayPath);
                }
                capacity = checked((int)written + 1);
            }
        }

        private static string NormalizeComparableFinalPath(string path)
        {
            if (String.IsNullOrEmpty(path))
            {
                return path;
            }

            string normalized;
            if (path.StartsWith(@"\\?\UNC\", StringComparison.OrdinalIgnoreCase))
            {
                normalized = @"\\" + path.Substring(8);
            }
            else if (path.StartsWith(@"\\?\", StringComparison.OrdinalIgnoreCase))
            {
                normalized = path.Substring(4);
            }
            else
            {
                normalized = path;
            }
            normalized = Path.GetFullPath(normalized);
            return TrimEndingSeparatorsExceptRoot(normalized);
        }

        private static string TrimEndingSeparatorsExceptRoot(string path)
        {
            string root = Path.GetPathRoot(path);
            int minimum = String.IsNullOrEmpty(root) ? 0 : root.Length;
            int end = path.Length;
            while (end > minimum && IsDirectorySeparator(path[end - 1]))
            {
                end--;
            }
            return end == path.Length ? path : path.Substring(0, end);
        }

        private static bool IsDirectorySeparator(char value)
        {
            return value == Path.DirectorySeparatorChar ||
                value == Path.AltDirectorySeparatorChar;
        }

        private static WinterGatePathIdentityException NativePathError(
            string operation,
            string path,
            int nativeErrorCode)
        {
            Win32Exception native = new Win32Exception(nativeErrorCode);
            return new WinterGatePathIdentityException(
                "path identity: could not " + operation + " '" + path +
                "': " + native.Message + " (" + nativeErrorCode + ")",
                nativeErrorCode,
                native);
        }
    }
}
'@
    Add-Type -TypeDefinition $nativeSource -Language CSharp -ErrorAction Stop
}
```

`GetPathIdentity(path, File, true)` is Task 3's unambiguous full-chain baseline for executable and Git-ref checks: it rejects every parent or leaf reparse point and returns the leaf's final object identity. Task 3 then performs its GENERIC_READ open and compares that readable handle with this baseline using `SameStablePath`.

Replace Loop A's temporary error helper with the final native exception wrapper:

```powershell
function Throw-GatePathIdentityError {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [string]$Message,
        [Parameter(Position = 1)]
        [System.Exception]$InnerException
    )

    $fullMessage = "path identity: $Message"
    if ($null -eq $InnerException) {
        throw [WinterGate.WinterGatePathIdentityException]::new($fullMessage)
    }
    throw [WinterGate.WinterGatePathIdentityException]::new(
        $fullMessage,
        0,
        $InnerException
    )
}
```

- [ ] **Step B4: Add only the project and prospective-directory bridge**

Insert these functions after `Assert-PlainChildName`:

```powershell
function Get-UnwrappedException {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [System.Exception]$Exception
    )

    $current = $Exception
    while ($null -ne $current.InnerException -and
        ($current -is [System.Management.Automation.MethodInvocationException] -or
         $current -is [System.Reflection.TargetInvocationException])) {
        $current = $current.InnerException
    }
    return $current
}

function Get-ProspectiveDirectoryPlan {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [string]$Path,
        [Parameter(Mandatory = $true, Position = 1)]
        [string]$Label,
        [switch]$RequireMissing
    )

    $fullPath = Get-NormalizedAbsolutePlainPath $Path $Label
    try {
        $existing = [WinterGate.Native]::TryGetPathIdentity(
            $fullPath,
            [WinterGate.PathKind]::Directory,
            $true
        )
    }
    catch {
        $unwrapped = Get-UnwrappedException $_.Exception
        if ($unwrapped -is [WinterGate.WinterGatePathIdentityException]) {
            throw $unwrapped
        }
        Throw-GatePathIdentityError "$Label could not be inspected" $unwrapped
    }
    if ($null -ne $existing) {
        if ($RequireMissing) {
            Throw-GatePathIdentityError "$Label already exists: $fullPath"
        }
        return [pscustomobject][ordered]@{
            ExistingIdentity = $existing
            MissingComponents = [string[]]@()
            FinalPath = $existing.FinalPath
            VolumeSerialNumber = $existing.VolumeSerialNumber
        }
    }

    $missing = New-Object 'System.Collections.Generic.List[string]'
    $probe = $fullPath
    while ($null -eq $existing) {
        $leaf = [System.IO.Path]::GetFileName($probe)
        Assert-PlainChildName $leaf "$Label unresolved component"
        $missing.Insert(0, $leaf)
        $parent = [System.IO.Path]::GetDirectoryName($probe)
        if ([string]::IsNullOrEmpty($parent) -or $parent -eq $probe) {
            Throw-GatePathIdentityError "$Label has no existing ancestor: $fullPath"
        }
        $probe = $parent
        try {
            $existing = [WinterGate.Native]::TryGetPathIdentity(
                $probe,
                [WinterGate.PathKind]::Directory,
                $true
            )
        }
        catch {
            $unwrapped = Get-UnwrappedException $_.Exception
            if ($unwrapped -is [WinterGate.WinterGatePathIdentityException]) {
                throw $unwrapped
            }
            Throw-GatePathIdentityError "$Label ancestor could not be inspected" $unwrapped
        }
    }

    $projected = $existing.FinalPath
    foreach ($component in $missing) {
        $projected = [System.IO.Path]::Combine($projected, $component)
    }
    return [pscustomobject][ordered]@{
        ExistingIdentity = $existing
        MissingComponents = [string[]]$missing.ToArray()
        FinalPath = $projected
        VolumeSerialNumber = $existing.VolumeSerialNumber
    }
}

function Resolve-GateProject {
    [CmdletBinding()]
    param(
        [AllowNull()]
        [string]$ProjectRoot,
        [bool]$WasSpecified
    )

    if ($WasSpecified -and [string]::IsNullOrWhiteSpace($ProjectRoot)) {
        Throw-GatePathIdentityError 'ProjectRoot was supplied without a path'
    }
    if (-not $WasSpecified) {
        $ProjectRoot = [System.IO.Path]::GetFullPath(
            [System.IO.Path]::Combine($PSScriptRoot, '..')
        )
    }
    $normalized = Get-NormalizedAbsolutePlainPath $ProjectRoot 'ProjectRoot'
    try {
        return [WinterGate.Native]::GetPathIdentity(
            $normalized,
            [WinterGate.PathKind]::Directory,
            $true
        )
    }
    catch {
        $unwrapped = Get-UnwrappedException $_.Exception
        if ($unwrapped -is [WinterGate.WinterGatePathIdentityException]) {
            throw $unwrapped
        }
        Throw-GatePathIdentityError 'ProjectRoot could not be resolved' $unwrapped
    }
}
```

Replace Loop A's `Invoke-WinterInterludeGate` with:

```powershell
function Invoke-WinterInterludeGate {
    Assert-WinterGateBootstrapHost
    Add-WinterGateNativeTypes
    $projectIdentity = Resolve-GateProject `
        -ProjectRoot $ProjectRoot `
        -WasSpecified:$projectRootWasSpecified

    $candidate = $RunRoot
    if (-not $runRootWasSpecified) {
        $candidate = [System.IO.Path]::Combine(
            [System.IO.Path]::GetTempPath(),
            [System.Guid]::NewGuid().ToString('N').ToLowerInvariant()
        )
    }
    [void](Get-ProspectiveDirectoryPlan $candidate 'RunRoot' -RequireMissing)
    throw 'winter gate trusted-host/player-save layer not implemented'
}
```

`TryGetPathIdentity` returns `null` only for Win32 2 and 3. Access denial, kind mismatch, malformed input, reparse components, and all other errors remain fail-closed. The prospective plan resolves the nearest existing ancestor and appends only validated plain names; this loop creates nothing.

- [ ] **Step B5: Run Loop B GREEN**

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateBootstrapTests.test_valid_call_reaches_native_chain_boundary `
  Tools.test_winter_interlude_gate.WinterInterludeGatePathSafetyTests.test_native_full_chain_contract_precedes_creation `
  Tools.test_winter_interlude_gate.WinterInterludeGatePathSafetyTests.test_rejects_preexisting_empty_and_nonempty_runroots `
  Tools.test_winter_interlude_gate.WinterInterludeGatePathSafetyTests.test_rejects_missing_file_relative_and_junction_projectroots `
  Tools.test_winter_interlude_gate.WinterInterludeGatePathSafetyTests.test_rejects_junction_routed_runroot_ancestors `
  Tools.test_winter_interlude_gate.WinterInterludeGatePathSafetyTests.test_rejects_a_preexisting_junction_as_runroot_leaf `
  Tools.test_winter_interlude_gate.WinterInterludeGatePathSafetyTests.test_exact_native_chain_holds_ancestor_until_leaf_identity -v
if ($LASTEXITCODE -ne 0) { throw 'Loop B GREEN failed.' }
```

Expected: all 7 focused tests pass. Parent junctions and junction leaves fail from opened attributes/final paths; a file ProjectRoot fails kind validation; pre-existing roots remain untouched; and the exact-production-source harness pauses immediately after the selected ancestor handle enters `HeldPathChain`, proving rename is blocked until leaf capture and succeeds after chain disposal. Host probing established that desired access `0` and `FILE_READ_ATTRIBUTES` do not enforce this share boundary; `FILE_READ_DATA` is the minimum access bit that makes omission of `FILE_SHARE_DELETE` protect the live object on this runtime. Adding `FILE_SHARE_DELETE`, reverting to metadata-only access, disposing the ancestor early, or drifting the unique hook point makes this test fail deterministically. No production test seam, run tree, or child is created.

#### Loop C: Authenticate the host and protect both player-save roots

- [ ] **Step C1: Add only the trusted-host and save-root RED tests**

The Loop A fixture already creates `self.player_save` because Loop B's junction-routing test needs that safe, test-owned target. Do not add or move fixture state in this loop.

Replace `test_valid_call_reaches_native_chain_boundary` with:

```python
    def test_valid_call_reaches_runroot_creation_boundary(self):
        with tempfile.TemporaryDirectory(prefix="winter-gate-save-boundary-") as owned_text:
            owned = Path(owned_text)
            project = owned / "project"
            (project / "Tools").mkdir(parents=True)
            appdata = owned / "appdata"
            appdata.mkdir()
            process_temp = owned / "temp"
            process_temp.mkdir()
            completed = run_gate(
                "-Gate", "Structural",
                "-ProjectRoot", str(project),
                "-RunRoot", str(owned / "run"),
                env={
                    "APPDATA": str(appdata),
                    "TEMP": str(process_temp),
                    "TMP": str(process_temp),
                },
            )
            self.assertEqual(1, completed.returncode, completed.stdout)
            self.assertIn(
                "winter gate run-root creation layer not implemented",
                completed.stderr,
            )
            self.assertNotIn(
                "winter gate trusted-host/player-save layer not implemented",
                completed.stderr,
            )
```

Insert these methods into `WinterInterludeGatePathSafetyTests`:

```python
    def test_copied_powershell_host_is_rejected_before_runroot_or_child(self) -> None:
        copied_host_dir = self.temp_root / "copied-host"
        copied_host_dir.mkdir()
        copied_host = copied_host_dir / POWERSHELL.name
        shutil.copy2(POWERSHELL, copied_host)
        trusted_config = Path(str(POWERSHELL) + ".config")
        if trusted_config.is_file():
            shutil.copy2(trusted_config, Path(str(copied_host) + ".config"))
        run_root = self.external / "copied-host-run"
        completed = subprocess.run(
            [
                str(copied_host),
                "-NoLogo",
                "-NoProfile",
                "-NonInteractive",
                "-ExecutionPolicy",
                "Bypass",
                "-File",
                str(GATE),
                "-Gate",
                "Structural",
                "-ProjectRoot",
                str(self.project),
                "-RunRoot",
                str(run_root),
            ],
            cwd=self.temp_root,
            env={**os.environ, **self.env},
            text=True,
            encoding="utf-8",
            errors="replace",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=30,
            check=False,
        )
        self.assert_path_rejected(completed)
        self.assertIn("trusted System-directory PowerShell", completed.stderr)
        self.assertFalse(run_root.exists())

    def test_rejects_process_appdata_player_save(self) -> None:
        protected = self.player_save / "inside-run"
        self.assert_path_rejected(self.invoke(str(protected)))
        self.assertFalse(protected.exists())

    def test_empty_or_missing_process_appdata_fails_closed(self) -> None:
        cases = ("", str(self.temp_root / "missing-process-appdata"))
        for index, appdata in enumerate(cases):
            with self.subTest(appdata=appdata):
                self.env["APPDATA"] = appdata
                run_root = self.external / f"bad-appdata-{index}"
                self.assert_path_rejected(self.invoke(str(run_root)))
                self.assertFalse(run_root.exists())
```

- [ ] **Step C2: Run the host/save RED**

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateBootstrapTests.test_valid_call_reaches_runroot_creation_boundary `
  Tools.test_winter_interlude_gate.WinterInterludeGatePathSafetyTests.test_copied_powershell_host_is_rejected_before_runroot_or_child `
  Tools.test_winter_interlude_gate.WinterInterludeGatePathSafetyTests.test_rejects_process_appdata_player_save `
  Tools.test_winter_interlude_gate.WinterInterludeGatePathSafetyTests.test_empty_or_missing_process_appdata_fails_closed -v 2>&1 |
  Tee-Object -FilePath .superpowers/sdd/task-7-5-path-c-red.txt
if ($LASTEXITCODE -eq 0) { throw 'Loop C RED unexpectedly passed.' }
```

Expected: `Ran 4 tests` and FAIL. The copied host is still handled by Task 1's lexical check, the valid call remains at Loop B, and Loop B neither resolves APPDATA nor excludes the process player-save final path.

- [ ] **Step C3: Add the trusted object and protected-save implementation**

Delete Task 1's complete `Assert-WinterGateBootstrapHost`. Insert the final host function immediately after `Throw-GatePathIdentityError`:

```powershell
function Assert-WinterGateHostIdentity {
    [CmdletBinding()]
    param()

    if ($PSVersionTable.PSEdition -ne 'Desktop' -or
        $PSVersionTable.PSVersion.Major -ne 5) {
        Throw-GatePathIdentityError `
            'gate host is not Windows PowerShell Desktop 5.1'
    }

    $trustedPath = Join-Path `
        ([Environment]::SystemDirectory) `
        'WindowsPowerShell\v1.0\powershell.exe'
    try {
        $currentPath = [System.Diagnostics.Process]::GetCurrentProcess().MainModule.FileName
        $trustedIdentity = [WinterGate.Native]::GetPathIdentity(
            $trustedPath,
            [WinterGate.PathKind]::File,
            $true
        )
        $currentIdentity = [WinterGate.Native]::GetPathIdentity(
            $currentPath,
            [WinterGate.PathKind]::File,
            $true
        )
    }
    catch [WinterGate.WinterGatePathIdentityException] {
        throw
    }
    catch {
        Throw-GatePathIdentityError `
            'could not resolve the trusted gate host identity' `
            $_.Exception
    }

    if (-not [WinterGate.Native]::SameObject(
        $currentIdentity,
        $trustedIdentity
    )) {
        Throw-GatePathIdentityError `
            'gate host is not the trusted System-directory PowerShell object'
    }
    return $trustedIdentity
}
```

Insert `Test-SameOrChildFinalPath` immediately before `Get-ProspectiveDirectoryPlan` and `Get-ProtectedPlayerSavePaths` immediately after `Resolve-GateProject`:

```powershell
function Test-SameOrChildFinalPath {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [object]$Candidate,
        [Parameter(Mandatory = $true, Position = 1)]
        [object]$Base
    )

    foreach ($record in @($Candidate, $Base)) {
        if ($null -eq $record -or
            $null -eq $record.PSObject.Properties['FinalPath'] -or
            $null -eq $record.PSObject.Properties['VolumeSerialNumber']) {
            Throw-GatePathIdentityError `
                'containment comparison requires a complete path identity or plan'
        }
    }
    if ([uint32]$Candidate.VolumeSerialNumber -ne
        [uint32]$Base.VolumeSerialNumber) {
        return $false
    }
    if ([string]::Equals(
        [string]$Candidate.FinalPath,
        [string]$Base.FinalPath,
        [System.StringComparison]::OrdinalIgnoreCase)) {
        return $true
    }
    $prefix = [string]$Base.FinalPath
    if (-not $prefix.EndsWith('\', [System.StringComparison]::Ordinal)) {
        $prefix += '\'
    }
    return ([string]$Candidate.FinalPath).StartsWith(
        $prefix,
        [System.StringComparison]::OrdinalIgnoreCase
    )
}
```

```powershell
function Get-ProtectedPlayerSavePaths {
    [CmdletBinding()]
    param()

    try {
        $known = [System.Environment]::GetFolderPath(
            [System.Environment+SpecialFolder]::ApplicationData
        )
    }
    catch {
        Throw-GatePathIdentityError `
            'Windows known ApplicationData folder could not be resolved' `
            $_.Exception
    }
    if ([string]::IsNullOrWhiteSpace($known)) {
        Throw-GatePathIdentityError `
            'Windows known ApplicationData folder is unavailable'
    }
    if ([string]::IsNullOrWhiteSpace($env:APPDATA)) {
        Throw-GatePathIdentityError 'process APPDATA folder is unavailable'
    }

    $rootInputs = @(
        [pscustomobject]@{
            Label = 'Windows known ApplicationData folder'
            Path = $known
        },
        [pscustomobject]@{
            Label = 'process APPDATA folder'
            Path = $env:APPDATA
        }
    )
    $applicationDataRoots =
        New-Object 'System.Collections.Generic.List[WinterGate.PathIdentity]'
    foreach ($inputRoot in $rootInputs) {
        $normalized = Get-NormalizedAbsolutePlainPath `
            $inputRoot.Path `
            $inputRoot.Label
        try {
            $identity = [WinterGate.Native]::GetPathIdentity(
                $normalized,
                [WinterGate.PathKind]::Directory,
                $true
            )
        }
        catch {
            $unwrapped = Get-UnwrappedException $_.Exception
            if ($inputRoot.Label -eq 'Windows known ApplicationData folder') {
                Throw-GatePathIdentityError `
                    'Windows known ApplicationData folder could not be resolved' `
                    $unwrapped
            }
            Throw-GatePathIdentityError `
                'process APPDATA folder could not be resolved' `
                $unwrapped
        }
        $duplicate = $false
        foreach ($recorded in $applicationDataRoots) {
            if ([WinterGate.Native]::SameStablePath($recorded, $identity)) {
                $duplicate = $true
                break
            }
        }
        if (-not $duplicate) {
            $applicationDataRoots.Add($identity)
        }
    }

    $protected = New-Object 'System.Collections.Generic.List[string]'
    foreach ($root in $applicationDataRoots) {
        $protected.Add([System.IO.Path]::Combine(
            $root.FinalPath,
            'RenPy',
            'CourtOfShadows-save'
        ))
    }
    return [string[]]$protected.ToArray()
}
```

Replace Loop B's `Invoke-WinterInterludeGate` with:

```powershell
function Invoke-WinterInterludeGate {
    Add-WinterGateNativeTypes
    $script:TrustedPowerShellIdentity = Assert-WinterGateHostIdentity
    $projectIdentity = Resolve-GateProject `
        -ProjectRoot $ProjectRoot `
        -WasSpecified:$projectRootWasSpecified
    $protectedSavePaths = @(Get-ProtectedPlayerSavePaths)

    $candidate = $RunRoot
    if (-not $runRootWasSpecified) {
        $candidate = [System.IO.Path]::Combine(
            [System.IO.Path]::GetTempPath(),
            [System.Guid]::NewGuid().ToString('N').ToLowerInvariant()
        )
    }
    $runPlan = Get-ProspectiveDirectoryPlan $candidate 'RunRoot' -RequireMissing
    foreach ($protectedPath in $protectedSavePaths) {
        $savePlan = Get-ProspectiveDirectoryPlan `
            $protectedPath `
            'protected player-save root'
        if (Test-SameOrChildFinalPath $runPlan $savePlan) {
            Throw-GatePathIdentityError 'RunRoot must be outside the player-save root'
        }
    }
    throw 'winter gate run-root creation layer not implemented'
}
```

Both the Windows known Roaming Application Data directory and process `APPDATA` are mandatory full-chain identities. They are deduplicated only by `SameStablePath`, then extended with `RenPy\CourtOfShadows-save`. Tests never create, junction to, or write the real known-folder save path.

- [ ] **Step C4: Run Loop C GREEN**

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateBootstrapTests.test_valid_call_reaches_runroot_creation_boundary `
  Tools.test_winter_interlude_gate.WinterInterludeGatePathSafetyTests.test_copied_powershell_host_is_rejected_before_runroot_or_child `
  Tools.test_winter_interlude_gate.WinterInterludeGatePathSafetyTests.test_rejects_process_appdata_player_save `
  Tools.test_winter_interlude_gate.WinterInterludeGatePathSafetyTests.test_empty_or_missing_process_appdata_fails_closed -v
if ($LASTEXITCODE -ne 0) { throw 'Loop C GREEN failed.' }
```

Expected: all 4 focused tests pass. The copied executable differs from the trusted file object and fails before RunRoot creation. Empty/missing process APPDATA and a proposed child of its player-save root fail closed; a valid external root reaches the named creation boundary.

#### Loop D: Bind exclusive creation to the expected parent and create verified children

- [ ] **Step D1: Add the exclusive-creation and final-boundary RED tests**

The `re`, `time`, `wintypes`, and `threading` imports plus `_framework_csc()` already exist from Loop B's deterministic exact-source harness. Immediately before `WinterInterludeGatePathSafetyTests`, insert:

```python
def _compile_path_trap(executable: Path) -> None:
    source_text = r'''
using System;
using System.IO;

internal static class Program
{
    public static int Main(string[] args)
    {
        string record = Environment.GetEnvironmentVariable("WINTER_GATE_CHILD_RECORD");
        if (!String.IsNullOrEmpty(record))
        {
            File.AppendAllText(record, "started" + Environment.NewLine);
        }
        return 91;
    }
}
'''.lstrip()
    _compile_csharp(
        executable,
        source_text,
        main=None,
        label="path trap",
    )


def _compile_parent_identity_harness(executable: Path) -> None:
    harness_source = _production_native_source() + r'''

namespace WinterGate
{
    internal static class ParentIdentityHarness
    {
        public static int Main(string[] args)
        {
            if (args.Length != 4)
            {
                return 90;
            }

            PathIdentity expectedParent = Native.GetPathIdentity(
                args[0],
                PathKind.Directory,
                true);
            File.WriteAllText(args[1], "ready");
            DateTime deadline = DateTime.UtcNow.AddSeconds(20);
            while (!File.Exists(args[2]))
            {
                if (DateTime.UtcNow >= deadline)
                {
                    return 91;
                }
                System.Threading.Thread.Sleep(10);
            }

            try
            {
                Native.CreateDirectoryExclusive(
                    Path.Combine(args[0], "child"),
                    expectedParent);
                File.WriteAllText(args[3], "unexpected success");
                return 92;
            }
            catch (WinterGatePathIdentityException exception)
            {
                File.WriteAllText(args[3], exception.Message);
                return 0;
            }
        }
    }
}
'''
    _compile_csharp(
        executable,
        harness_source,
        main="WinterGate.ParentIdentityHarness",
        label="parent-identity harness",
    )


def _final_directory(path: Path) -> Path:
    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    create_file = kernel32.CreateFileW
    create_file.argtypes = [
        wintypes.LPCWSTR,
        wintypes.DWORD,
        wintypes.DWORD,
        wintypes.LPVOID,
        wintypes.DWORD,
        wintypes.DWORD,
        wintypes.HANDLE,
    ]
    create_file.restype = wintypes.HANDLE
    get_final_path = kernel32.GetFinalPathNameByHandleW
    get_final_path.argtypes = [
        wintypes.HANDLE,
        wintypes.LPWSTR,
        wintypes.DWORD,
        wintypes.DWORD,
    ]
    get_final_path.restype = wintypes.DWORD
    close_handle = kernel32.CloseHandle
    close_handle.argtypes = [wintypes.HANDLE]
    close_handle.restype = wintypes.BOOL

    handle = create_file(
        str(path),
        0,
        0x00000001 | 0x00000002 | 0x00000004,
        None,
        3,
        0x02000000 | 0x00200000,
        None,
    )
    if handle == wintypes.HANDLE(-1).value:
        raise ctypes.WinError(ctypes.get_last_error())
    try:
        size = 512
        while True:
            buffer = ctypes.create_unicode_buffer(size)
            written = get_final_path(handle, buffer, size, 0)
            if written == 0:
                raise ctypes.WinError(ctypes.get_last_error())
            if written < size:
                final_path = buffer.value
                break
            size = written + 1
    finally:
        if not close_handle(handle):
            raise ctypes.WinError(ctypes.get_last_error())

    if final_path.lower().startswith("\\\\?\\unc\\"):
        final_path = "\\\\" + final_path[8:]
    elif final_path.startswith("\\\\?\\"):
        final_path = final_path[4:]
    return Path(os.path.normpath(final_path))
```

In `setUp`, immediately after `self.player_save.mkdir(parents=True)`, insert:

```python
        self.trap_dir = self.temp_root / "trap-bin"
        self.trap_dir.mkdir()
        _compile_path_trap(self.trap_dir / "python.exe")
```

Add `"PATH": str(self.trap_dir),` immediately after `"APPDATA": str(self.appdata),` in `self.env`.

Insert the final reporting helpers immediately after `invoke`:

```python
    def reported_run_root(
        self,
        result: subprocess.CompletedProcess[str],
    ) -> Path:
        prefix = "Winter gate run root: "
        values = [
            line[len(prefix) :]
            for line in result.stdout.splitlines()
            if line.startswith(prefix)
        ]
        self.assertEqual(1, len(values), result.stdout)
        return Path(values[0])

    def assert_path_bootstrap_completed(
        self,
        result: subprocess.CompletedProcess[str],
        run_root: Path,
    ) -> None:
        # A later slice may either continue the manifest or fail closed because
        # its fake-project prerequisite is absent.  This assertion is scoped to
        # Task 2: path bootstrap succeeded and created only the verified tree.
        self.assertNotIn("path identity", result.stderr.lower(), result.stderr)
        self.assertTrue(run_root.is_dir())
        self.assertTrue((run_root / "evidence").is_dir())
        self.assertTrue((run_root / "savedirs").is_dir())
        self.assertEqual(
            str(_final_directory(run_root)).casefold(),
            str(self.reported_run_root(result)).casefold(),
        )
```

Replace `test_valid_call_reaches_runroot_creation_boundary` with:

```python
    def test_valid_call_reaches_the_named_process_boundary_after_path_bootstrap(self):
        with tempfile.TemporaryDirectory(
            prefix="winter-gate-path-boundary-"
        ) as owned_text:
            owned = Path(owned_text)
            appdata = owned / "appdata"
            appdata.mkdir()
            process_temp = owned / "temp"
            process_temp.mkdir()
            run_root = owned / "run"
            completed = run_gate(
                "-Gate",
                "Structural",
                "-ProjectRoot",
                str(ROOT),
                "-RunRoot",
                str(run_root),
                env={
                    "APPDATA": str(appdata),
                    "TEMP": str(process_temp),
                    "TMP": str(process_temp),
                },
            )
            self.assertEqual(1, completed.returncode, completed.stdout)
            self.assertIn(
                "winter gate process layer not implemented",
                completed.stderr,
            )
            self.assertNotIn("winter gate bootstrap reached", completed.stderr)
            self.assertTrue((run_root / "evidence").is_dir())
            self.assertTrue((run_root / "savedirs").is_dir())
            self.assertEqual(
                [
                    f"Winter gate run root: {_final_directory(run_root)}",
                ],
                completed.stdout.splitlines(),
            )
```

Replace `test_native_full_chain_contract_precedes_creation` and `test_rejects_process_appdata_player_save` with these final methods:

```python
    def test_native_path_contract_is_declared(self) -> None:
        source = GATE.read_text(encoding="utf-8")
        for declaration in (
            "sealed class PathIdentity",
            "enum PathKind",
            "sealed class WinterGatePathIdentityException",
            "partial class Native",
            "GetPathIdentity(",
            "TryGetPathIdentity(",
            "CreateDirectoryExclusive(",
            "PathIdentity expectedParentIdentity",
            "SameObject(",
            "SameStablePath(",
            "SameStablePath(parent.LeafIdentity, expectedParentIdentity)",
            "current-drive-rooted paths are not accepted",
            "must not be rooted on the current drive",
            "Windows known ApplicationData folder is unavailable",
            "Windows known ApplicationData folder could not be resolved",
        ):
            self.assertIn(declaration, source)
        self.assertIn("function Assert-WinterGateHostIdentity", source)
        self.assertIn("[WinterGate.Native]::SameObject(", source)
        self.assertNotIn("function Assert-WinterGateBootstrapHost", source)
```

```python
    def test_rejects_process_appdata_player_save_but_allows_its_sibling(self) -> None:
        protected = self.player_save / "inside-run"
        self.assert_path_rejected(self.invoke(str(protected)))
        self.assertFalse(protected.exists())

        allowed = self.appdata / "winter-gate-runs" / "run"
        result = self.invoke(str(allowed))
        self.assert_path_bootstrap_completed(result, allowed)
```

Insert the remaining final public behaviors into `WinterInterludeGatePathSafetyTests`:

```python
    def test_projectroot_defaults_from_copied_gate_location_not_cwd(self) -> None:
        copied_gate = self.project / "Tools" / GATE.name
        shutil.copy2(GATE, copied_gate)
        inside_default_project = self.project / "inside-default-project"
        result = self.invoke(
            str(inside_default_project),
            gate=copied_gate,
            cwd=self.external,
            include_project_root=False,
        )
        self.assert_path_rejected(result)
        self.assertFalse(inside_default_project.exists())

    def test_rejects_project_containment_but_not_a_prefix_sibling(self) -> None:
        inside = self.project / "inside-run"
        self.assert_path_rejected(self.invoke(str(inside)))
        self.assertFalse(inside.exists())

        prefix_sibling = self.temp_root / "project2"
        prefix_sibling.mkdir()
        allowed = prefix_sibling / "nested" / "run"
        result = self.invoke(str(allowed))
        self.assert_path_bootstrap_completed(result, allowed)

    def test_creates_each_missing_component_and_verified_children(self) -> None:
        run_root = self.external / "one" / "two" / "run"
        result = self.invoke(str(run_root))
        self.assert_path_bootstrap_completed(result, run_root)

    def test_exclusive_creation_rejects_a_replaced_expected_parent(self) -> None:
        harness = self.temp_root / "parent-identity-harness.exe"
        _compile_parent_identity_harness(harness)
        parent = self.external / "expected-parent"
        parent.mkdir()
        moved = self.external / "expected-parent-original"
        ready = self.temp_root / "parent-harness-ready.txt"
        proceed = self.temp_root / "parent-harness-proceed.txt"
        result_path = self.temp_root / "parent-harness-result.txt"
        process = subprocess.Popen(
            [
                str(harness),
                str(parent),
                str(ready),
                str(proceed),
                str(result_path),
            ],
            cwd=self.temp_root,
            text=True,
            encoding="utf-8",
            errors="replace",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        try:
            deadline = time.monotonic() + 10
            while (
                not ready.exists()
                and process.poll() is None
                and time.monotonic() < deadline
            ):
                time.sleep(0.01)
            self.assertTrue(ready.is_file(), "native harness did not capture parent")
            os.replace(parent, moved)
            parent.mkdir()
            proceed.write_text("continue", encoding="utf-8")
            stdout, stderr = process.communicate(timeout=30)
        finally:
            if process.poll() is None:
                process.kill()
                process.communicate(timeout=5)

        self.assertEqual(0, process.returncode, stdout + stderr)
        self.assertIn(
            "exclusive directory parent changed after validation",
            result_path.read_text(encoding="utf-8"),
        )
        self.assertFalse((parent / "child").exists())
        self.assertFalse((moved / "child").exists())

    def test_default_runroot_is_new_lowercase_guid_under_process_temp(self) -> None:
        names_before = {entry.name.casefold() for entry in self.process_temp.iterdir()}
        result = self.invoke(None)
        run_root = self.reported_run_root(result)
        self.assertTrue(run_root.is_dir(), result.stderr)
        self.assertEqual(
            str(_final_directory(self.process_temp)).casefold(),
            str(_final_directory(run_root).parent).casefold(),
        )
        self.assertRegex(run_root.name, r"^[0-9a-f]{32}$")
        self.assertNotIn(run_root.name.casefold(), names_before)
        self.assertTrue((run_root / "evidence").is_dir())
        self.assertTrue((run_root / "savedirs").is_dir())

    def test_public_paths_preserve_spaces_parentheses_and_apostrophes(self) -> None:
        run_root = self.external / "run space (paren) apostrophe's"
        result = self.invoke(str(run_root))
        self.assert_path_bootstrap_completed(result, run_root)

    def test_exclusive_runroot_allows_exactly_one_concurrent_claimant(self) -> None:
        run_root = self.external / "concurrent" / "same-run"
        barrier = threading.Barrier(3)
        results: list[subprocess.CompletedProcess[str] | None] = [None, None]
        failures: list[BaseException] = []

        def invoke(index: int) -> None:
            try:
                barrier.wait(timeout=10)
                results[index] = self.invoke(str(run_root))
            except BaseException as exception:
                failures.append(exception)

        workers = [
            threading.Thread(target=invoke, args=(index,), daemon=True)
            for index in range(2)
        ]
        for worker in workers:
            worker.start()
        barrier.wait(timeout=10)
        for worker in workers:
            worker.join(timeout=30)

        self.assertFalse(any(worker.is_alive() for worker in workers))
        self.assertEqual([], failures)
        completed = [result for result in results if result is not None]
        self.assertEqual(2, len(completed))
        winners = [
            result for result in completed
            if "Winter gate run root: " in result.stdout
        ]
        losers = [
            result for result in completed
            if "path identity" in result.stderr.lower()
        ]
        self.assertEqual(1, len(winners), completed)
        self.assertEqual(1, len(losers), completed)
        self.assert_path_bootstrap_completed(winners[0], run_root)
        self.assertFalse(self.child_record.exists())
```

- [ ] **Step D2: Run the exclusive-creation RED**

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateBootstrapTests.test_valid_call_reaches_the_named_process_boundary_after_path_bootstrap `
  Tools.test_winter_interlude_gate.WinterInterludeGatePathSafetyTests.test_native_path_contract_is_declared `
  Tools.test_winter_interlude_gate.WinterInterludeGatePathSafetyTests.test_projectroot_defaults_from_copied_gate_location_not_cwd `
  Tools.test_winter_interlude_gate.WinterInterludeGatePathSafetyTests.test_rejects_project_containment_but_not_a_prefix_sibling `
  Tools.test_winter_interlude_gate.WinterInterludeGatePathSafetyTests.test_rejects_process_appdata_player_save_but_allows_its_sibling `
  Tools.test_winter_interlude_gate.WinterInterludeGatePathSafetyTests.test_creates_each_missing_component_and_verified_children `
  Tools.test_winter_interlude_gate.WinterInterludeGatePathSafetyTests.test_exclusive_creation_rejects_a_replaced_expected_parent `
  Tools.test_winter_interlude_gate.WinterInterludeGatePathSafetyTests.test_default_runroot_is_new_lowercase_guid_under_process_temp `
  Tools.test_winter_interlude_gate.WinterInterludeGatePathSafetyTests.test_public_paths_preserve_spaces_parentheses_and_apostrophes `
  Tools.test_winter_interlude_gate.WinterInterludeGatePathSafetyTests.test_exclusive_runroot_allows_exactly_one_concurrent_claimant -v 2>&1 |
  Tee-Object -FilePath .superpowers/sdd/task-7-5-path-d-red.txt
if ($LASTEXITCODE -eq 0) { throw 'Loop D RED unexpectedly passed.' }
```

Expected: `Ran 10 tests` and FAIL. The interface assertion cannot find `CreateDirectoryExclusive(`, and the exact-source parent-identity harness fails to compile because the two-parameter API is absent. The copied gate has not yet derived and rejected its default ProjectRoot containment from its own `Tools` location. Valid/sibling/default roots still stop at the creation boundary without evidence children or a run-root line; project containment is unchecked; and concurrent callers cannot yield exactly one claimant.

The parent-identity harness is the one deliberate native unit boundary in this class. It extracts the exact production `$nativeSource`, appends only a temporary `Main`, and never dot-sources the gate or adds a production-bindable switch. Every gate-level path behavior still executes through the public Windows PowerShell `-File` entrypoint.

- [ ] **Step D3: Add the minimal native exclusive-create patch**

Inside `$nativeSource`, insert this declaration immediately after `GetFinalPathNameByHandleW`:

```csharp
[DllImport("kernel32.dll", CharSet = CharSet.Unicode, SetLastError = true)]
[return: MarshalAs(UnmanagedType.Bool)]
private static extern bool CreateDirectoryW(
    string path,
    IntPtr securityAttributes);
```

Insert this method immediately before `SameObject`:

```csharp
public static void CreateDirectoryExclusive(
    string path,
    PathIdentity expectedParentIdentity)
{
    string fullPath = RequireAbsoluteNonDevicePath(path);
    string parentPath = Path.GetDirectoryName(fullPath);
    string leafName = Path.GetFileName(fullPath);
    if (String.IsNullOrEmpty(parentPath) || String.IsNullOrEmpty(leafName))
    {
        throw new WinterGatePathIdentityException(
            "path identity: exclusive directory needs a parent and leaf: " +
            fullPath);
    }
    if (expectedParentIdentity == null)
    {
        throw new WinterGatePathIdentityException(
            "path identity: exclusive directory expected parent is absent: " +
            fullPath);
    }

    using (HeldPathChain parent = OpenExistingPathChain(
        parentPath,
        PathKind.Directory,
        true))
    {
        if (!SameStablePath(parent.LeafIdentity, expectedParentIdentity))
        {
            throw new WinterGatePathIdentityException(
                "path identity: exclusive directory parent changed after " +
                "validation: " + parentPath);
        }
        string canonicalChild = Path.Combine(
            parent.LeafIdentity.FinalPath,
            leafName);
        if (!String.Equals(
            NormalizeComparableFinalPath(canonicalChild),
            fullPath,
            StringComparison.OrdinalIgnoreCase))
        {
            throw new WinterGatePathIdentityException(
                "path identity: exclusive directory parent final path " +
                "does not match the requested path: " + fullPath);
        }
        if (!CreateDirectoryW(canonicalChild, IntPtr.Zero))
        {
            int error = Marshal.GetLastWin32Error();
            throw NativePathError(
                "create directory exclusively",
                canonicalChild,
                error);
        }

        SafeFileHandle childHandle = OpenPathHandle(
            canonicalChild,
            true);
        parent.Handles.Add(childHandle);
        PathIdentity childIdentity = ReadPathIdentityFromHandle(
            childHandle,
            PathKind.Directory,
            true,
            canonicalChild);
        if (!String.Equals(
            NormalizeComparableFinalPath(canonicalChild),
            childIdentity.FinalPath,
            StringComparison.OrdinalIgnoreCase))
        {
            throw new WinterGatePathIdentityException(
                "path identity: exclusively created directory resolved " +
                "outside its verified parent: " + canonicalChild);
        }
    }
}
```

The caller must pass the exact parent identity it validated before probing the child. `CreateDirectoryExclusive` reopens and holds that parent chain, requires `SameStablePath(parent.LeafIdentity, expectedParentIdentity)` before `CreateDirectoryW`, and retains the non-delete-shared chain through opening the child. The exact-source harness snapshots a real parent, waits while the test replaces that object at the same path, then proves the method fails without creating under either object. An already-existing leaf is also a native path error, so concurrent callers cannot both claim one missing component.

- [ ] **Step D4: Add the verified run-tree functions**

Insert `Assert-GatePathState` immediately after `Get-UnwrappedException`:

```powershell
function Assert-GatePathState {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [WinterGate.PathIdentity]$ExpectedIdentity,
        [Parameter(Mandatory = $true, Position = 1)]
        [string]$Label
    )

    $expectedKind = [WinterGate.PathKind]::File
    if (($ExpectedIdentity.Attributes -band
        [System.IO.FileAttributes]::Directory) -ne 0) {
        $expectedKind = [WinterGate.PathKind]::Directory
    }
    try {
        $actual = [WinterGate.Native]::GetPathIdentity(
            $ExpectedIdentity.FinalPath,
            $expectedKind,
            $true
        )
    }
    catch {
        $unwrapped = Get-UnwrappedException $_.Exception
        if ($unwrapped -is [WinterGate.WinterGatePathIdentityException]) {
            throw $unwrapped
        }
        Throw-GatePathIdentityError "$Label could not be reopened" $unwrapped
    }
    if (-not [WinterGate.Native]::SameStablePath(
        $ExpectedIdentity,
        $actual)) {
        Throw-GatePathIdentityError "$Label changed after validation"
    }
    return $actual
}
```

Insert these final functions immediately after `Get-ProtectedPlayerSavePaths`:

```powershell
function New-VerifiedChildDirectory {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [WinterGate.PathIdentity]$ParentIdentity,
        [Parameter(Mandatory = $true, Position = 1)]
        [string]$LeafName
    )

    Assert-PlainChildName $LeafName 'child directory name'
    $parentBefore = Assert-GatePathState $ParentIdentity 'parent directory'
    $childPath = [System.IO.Path]::Combine(
        $parentBefore.FinalPath,
        $LeafName
    )
    try {
        $existing = [WinterGate.Native]::TryGetPathIdentity(
            $childPath,
            [WinterGate.PathKind]::Directory,
            $true
        )
        if ($null -ne $existing) {
            Throw-GatePathIdentityError "child directory appeared concurrently: $childPath"
        }
        [WinterGate.Native]::CreateDirectoryExclusive(
            $childPath,
            $parentBefore
        )
        $parentAfter = Assert-GatePathState $ParentIdentity 'parent directory'
        $child = [WinterGate.Native]::GetPathIdentity(
            $childPath,
            [WinterGate.PathKind]::Directory,
            $true
        )
    }
    catch {
        $unwrapped = Get-UnwrappedException $_.Exception
        if ($unwrapped -is [WinterGate.WinterGatePathIdentityException]) {
            throw $unwrapped
        }
        Throw-GatePathIdentityError "child directory could not be created: $childPath" $unwrapped
    }

    $resolvedParentPath = [System.IO.Path]::GetDirectoryName($child.FinalPath)
    if ($child.VolumeSerialNumber -ne $parentAfter.VolumeSerialNumber -or
        -not [string]::Equals(
            $resolvedParentPath,
            $parentAfter.FinalPath,
            [System.StringComparison]::OrdinalIgnoreCase)) {
        Throw-GatePathIdentityError "child escaped its verified parent: $childPath"
    }
    return $child
}

function New-VerifiedRunRoot {
    [CmdletBinding()]
    param(
        [AllowNull()]
        [string]$Candidate,
        [Parameter(Mandatory = $true)]
        [bool]$CandidateWasSpecified,
        [Parameter(Mandatory = $true)]
        [WinterGate.PathIdentity]$ProjectIdentity,
        [AllowEmptyCollection()]
        [string[]]$ProtectedSavePaths = @()
    )

    $verifiedProject = Assert-GatePathState $ProjectIdentity 'ProjectRoot'
    if ($CandidateWasSpecified -and [string]::IsNullOrWhiteSpace($Candidate)) {
        Throw-GatePathIdentityError 'RunRoot was supplied without a path'
    }
    if (-not $CandidateWasSpecified) {
        $Candidate = [System.IO.Path]::Combine(
            [System.IO.Path]::GetTempPath(),
            [System.Guid]::NewGuid().ToString('N').ToLowerInvariant()
        )
    }

    $runPlan = Get-ProspectiveDirectoryPlan $Candidate 'RunRoot' -RequireMissing
    if (Test-SameOrChildFinalPath $runPlan $verifiedProject) {
        Throw-GatePathIdentityError 'RunRoot must be outside ProjectRoot'
    }

    $savePlans = New-Object 'System.Collections.Generic.List[object]'
    foreach ($protectedPath in $ProtectedSavePaths) {
        $savePlan = Get-ProspectiveDirectoryPlan `
            $protectedPath `
            'protected player-save root'
        $savePlans.Add($savePlan)
        if (Test-SameOrChildFinalPath $runPlan $savePlan) {
            Throw-GatePathIdentityError 'RunRoot must be outside the player-save root'
        }
    }

    $current = $runPlan.ExistingIdentity
    foreach ($component in $runPlan.MissingComponents) {
        $current = New-VerifiedChildDirectory $current $component
    }
    $runIdentity = $current
    if ($runIdentity.VolumeSerialNumber -ne $runPlan.VolumeSerialNumber -or
        -not [string]::Equals(
            $runIdentity.FinalPath,
            $runPlan.FinalPath,
            [System.StringComparison]::OrdinalIgnoreCase)) {
        Throw-GatePathIdentityError 'RunRoot resolved somewhere other than its planned final path'
    }

    $verifiedProject = Assert-GatePathState $ProjectIdentity 'ProjectRoot'
    if (Test-SameOrChildFinalPath $runIdentity $verifiedProject) {
        Throw-GatePathIdentityError 'created RunRoot is inside ProjectRoot'
    }
    foreach ($savePlan in $savePlans) {
        if (Test-SameOrChildFinalPath $runIdentity $savePlan) {
            Throw-GatePathIdentityError 'created RunRoot is inside a player-save root'
        }
    }

    $evidenceIdentity = New-VerifiedChildDirectory $runIdentity 'evidence'
    $runIdentity = Assert-GatePathState $runIdentity 'RunRoot'
    $savedirsIdentity = New-VerifiedChildDirectory $runIdentity 'savedirs'
    $runIdentity = Assert-GatePathState $runIdentity 'RunRoot'
    [void](Assert-GatePathState $evidenceIdentity 'evidence directory')
    [void](Assert-GatePathState $savedirsIdentity 'savedirs directory')

    return [pscustomobject][ordered]@{
        Identity = $runIdentity
        EvidenceIdentity = $evidenceIdentity
        SavedirsIdentity = $savedirsIdentity
    }
}
```

Replace Loop C's `Invoke-WinterInterludeGate` with:

```powershell
function Invoke-WinterInterludeGate {
    Add-WinterGateNativeTypes
    $script:TrustedPowerShellIdentity = Assert-WinterGateHostIdentity
    $projectIdentity = Resolve-GateProject `
        -ProjectRoot $ProjectRoot `
        -WasSpecified:$projectRootWasSpecified
    $protectedSavePaths = @(Get-ProtectedPlayerSavePaths)
    $runTree = New-VerifiedRunRoot `
        -Candidate $RunRoot `
        -CandidateWasSpecified:$runRootWasSpecified `
        -ProjectIdentity $projectIdentity `
        -ProtectedSavePaths $protectedSavePaths
    [Console]::Out.WriteLine(
        ('Winter gate run root: {0}' -f $runTree.Identity.FinalPath)
    )
    throw 'winter gate process layer not implemented'
}
```

The run-root result has exactly `Identity`, `EvidenceIdentity`, and `SavedirsIdentity`. Later tasks use only their final paths and recheck them before every child launch and evidence write.

- [ ] **Step D5: Run all Task 2 paths GREEN and retain bootstrap contracts**

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGatePathSafetyTests -v 2>&1 |
  Tee-Object -FilePath .superpowers/sdd/task-7-5-path-green.txt
if ($LASTEXITCODE -ne 0) { throw 'Task 2 path-safety GREEN failed.' }

python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateBootstrapTests -v
if ($LASTEXITCODE -ne 0) { throw 'Task 2 public interface regression.' }
```

Expected: all 18 path tests and all 3 updated bootstrap tests pass. Invalid, nonplain, existing, contained, wrong-kind, missing-APPDATA, and reparse-routed roots fail before the trap child. The copied host fails object identity. Loop B's synchronized probe observes `ERROR_SHARING_VIOLATION` while final identity resolution holds the deep ancestor. The exact-source harness proves an expected parent cannot be replaced between validation and exclusive creation, and exactly one concurrent gate claims a shared missing RunRoot.

Junction targets stay untouched; the copied gate defaults from its own `Tools` parent; default RunRoot is a new lowercase 32-hex GUID below the process temp final path; prefix siblings and special characters survive. Valid roots contain regular `evidence` and `savedirs`, stdout has one final-path line, and stderr ends at the named process-layer failure.

- [ ] **Step D6: Inspect the exact Task 2 slice and amend the growing commit**

```powershell
git diff --check
if ($LASTEXITCODE -ne 0) { throw 'Whitespace validation failed.' }
git diff -- Tools/Run-WinterInterludeGate.ps1 Tools/test_winter_interlude_gate.py
git add -- Tools/Run-WinterInterludeGate.ps1 Tools/test_winter_interlude_gate.py
if ($LASTEXITCODE -ne 0) { throw 'Could not stage the path slice.' }
git diff --cached --check
if ($LASTEXITCODE -ne 0) { throw 'Staged path slice failed whitespace validation.' }
$staged = @(git diff --cached --name-only)
if ($LASTEXITCODE -ne 0) { throw 'Could not inspect staged path slice.' }
$expectedStaged = @(
    'Tools/Run-WinterInterludeGate.ps1',
    'Tools/test_winter_interlude_gate.py'
)
$unexpected = @(Compare-Object `
    -ReferenceObject @($expectedStaged | Sort-Object) `
    -DifferenceObject @($staged | Sort-Object))
if ($unexpected.Count -ne 0) {
    throw "Unexpected staged files: $($staged -join ', ')"
}
git commit --amend --no-edit
if ($LASTEXITCODE -ne 0) { throw 'Could not amend the Task 1 implementation commit.' }
```

Expected: only the native path APIs/empty process seam, trusted-host identity, verified project/run tree, final boundary, and 18 path tests are present. There is no process engine, manifest, success adapter, recursive cleanup, game source, or asset change.

---
### Task 3: Implement the bounded Windows process engine and public source-step bridge

**Files:**
- Modify: `Tools/Run-WinterInterludeGate.ps1`
- Modify: `Tools/test_winter_interlude_gate.py`

**Interfaces:**
- Consumes: Task 2's single `WinterGate.Native` class, `PathIdentity`, `BoundedProcessResult`, `GetPathIdentityFromOpenHandle(IntPtr, PathKind)`, `SameStablePath`, exact top-level `$projectRootWasSpecified` / `$runRootWasSpecified` captures, `Assert-WinterGateHostIdentity`, `Resolve-GateProject`, `Get-ProtectedPlayerSavePaths`, `New-VerifiedRunRoot`, verified run-tree helpers, and the exact `// BEGIN PROCESS ENGINE` / `// END PROCESS ENGINE` replacement seam.
- Produces: `WinterGate.Native.RunProcessTree(string executable, string[] arguments, string workingDirectory, string stdoutPath, string stderrPath, int timeoutMilliseconds, PathIdentity expectedEvidenceDirectoryIdentity)`; `GetReadableFileIdentity` / `TryGetReadableFileIdentity`, which use Task 2's full-chain anti-reparse identity primitive before comparing a canonical `GENERIC_READ` open-handle identity; `ReadVerifiedUtf8TextFile`, which holds the canonical file with `FileShareRead` only while reading bounded UTF-8 bytes; the guarded create-new result writer and gate-owned atomic summary publisher described below; one shared `_GateBlackBoxCase.make_project()` fixture for Tasks 3-5; `New-GateStep`, a source-only Structural manifest, a capability-first provisional Narrative manifest, process-result mapping, and the real public `Invoke-WinterInterludeGate` bridge.
- Produces: three deliberately distinct recheck scopes. `Assert-RunTreeDirectoryIdentities` checks only the base RunRoot/Evidence/Savedirs identities used to decide whether an honest catch-path summary is safe. `Assert-AllGateDirectoryIdentities` checks every registered gate-owned directory plus ProjectRoot and the Git HEAD state. `Assert-NonEvidenceGateDirectoryIdentities` checks ProjectRoot, Git HEAD, and every registered directory except the exact baseline Evidence directory object immediately before a native evidence write; registered Evidence descendants such as runner/portrait directories are still checked. The native writer pins only that exact Evidence object until its flushed handle closes, and the full check runs immediately afterward.
- Produces: pre-launch and post-drain validation of the current step executable and required-file identities. A post-drain mismatch is a validation failure before that step's result is published. A started tree that cannot be authoritatively observed at Job `ActiveProcesses == 0` leaves `TreeDrained=false`, marks evidence publication unsafe, and publishes neither a result nor a summary.
- Verifies: exact-source native probes compile the final Task 2+3 `WinterGate.Native` source and run both public JSON writers ordinarily. For the deterministic live-handle race only, the test compiles a byte-reversible derivative that adds one test-only named-event helper and one wait immediately before each of the two unique `WriteAllAndFlush` calls; the production source contains no event token or synchronization seam. Production result and summary writers deny both Python leaf replacement and the independent WinPS5.1 parent move, then return rc 0 with one complete fixed-name object. Exact-source guard/leaf delete-share mutants permit both live moves: result returns rc 0 with the complete object only at the moved tree's raced name, while summary flushes there and returns rc 92 when fixed-name handle publication encounters missing parent error 3. Both mutant placements are dishonest, and a second parent move succeeds after all handles close. No large payload or write-speed polling is used.
- Produces: a named Task 3 source-bridge boundary. A clean Structural invocation launches exactly the one `source-contract` step, records that step as passed, then deliberately returns exit code 1 with an honest `failed` / `validation` summary whose error is exactly `structural manifest layer not implemented`. Task 4 must delete both this boundary test and the matching forced-validation block when it installs the complete Structural manifest; it must not retain a Task 3 success bypass.
- Preserves: the bookend summary's exact schema uses `head_token` (the 12-character commit prefix when Git is present, otherwise `no-head`) and does not add a `git_commit` field. The full current object id remains internal to HEAD stability and exact `GIT_COMMIT` validation.
- Preserves: one public gate, one `Add-Type`, no executor injection, no success environment bypass, exact argument arrays at the native boundary, and the Task 2 host/path trust decisions rather than reimplementing them.

#### Exact test catalog (copy only the definitions named by each RED step)

The following catalog is the exact final Python content used by Loops 3.1-3.5.
It is not one implementation action: never paste the catalog wholesale. Each
RED step below names the definitions and test methods to copy before that RED,
and no later method may be present early. The public cases use the real
`-Gate Structural` path and no injectable executor. The two native probe
classes compile the exact C# here-string extracted from the public script; they
are narrow verification probes, not production adapters. Every path and
environment control belongs to the test's temporary directory.
The final catalog contains two native-probe methods, one bootstrap boundary
method, and thirty-two process-class methods (twenty-eight tests plus four
non-lifecycle helpers, excluding `setUp`): thirty-five catalog methods total.

```python
import contextlib
import ctypes
import json
import os
import re
import shutil
import subprocess
import tempfile
import time
import unittest
from ctypes import wintypes
from dataclasses import dataclass
from pathlib import Path


# BEGIN LOOP 3.3-T1A RECORDING CHILD AND CONTROL SUPPORT
RECORDING_CHILD_SOURCE = r'''
using System;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading;
using System.Web.Script.Serialization;

internal static class RecordingChild
{
    private const int StdInputHandle = -10;
    private const int StdOutputHandle = -11;
    private const int StdErrorHandle = -12;
    private const uint FileTypeChar = 0x0002;
    private const uint JobObjectQuery = 0x0004;
    private const uint MoveFileReplaceExisting = 0x00000001;
    private const uint MoveFileWriteThrough = 0x00000008;

    [DllImport("kernel32.dll", SetLastError = true)]
    private static extern IntPtr GetCurrentProcess();

    [DllImport("kernel32.dll", SetLastError = true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    private static extern bool IsProcessInJob(
        IntPtr process,
        IntPtr job,
        [MarshalAs(UnmanagedType.Bool)] out bool result);

    [DllImport("kernel32.dll", CharSet = CharSet.Unicode, SetLastError = true)]
    private static extern IntPtr OpenJobObjectW(
        uint desiredAccess,
        [MarshalAs(UnmanagedType.Bool)] bool inheritHandle,
        string name);

    [DllImport("kernel32.dll", SetLastError = true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    private static extern bool CloseHandle(IntPtr handle);

    [DllImport("kernel32.dll", SetLastError = true)]
    private static extern IntPtr GetStdHandle(int standardHandle);

    [DllImport("kernel32.dll", SetLastError = true)]
    private static extern uint GetFileType(IntPtr handle);

    [DllImport("kernel32.dll", CharSet = CharSet.Unicode, SetLastError = true)]
    private static extern uint GetFinalPathNameByHandleW(
        IntPtr handle,
        StringBuilder path,
        uint pathLength,
        uint flags);

    [DllImport("kernel32.dll", CharSet = CharSet.Unicode, SetLastError = true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    private static extern bool MoveFileExW(
        string existingFile,
        string newFile,
        uint flags);

    private static string NormalizeFinalPath(string path)
    {
        if (path.StartsWith(@"\\?\UNC\", StringComparison.OrdinalIgnoreCase))
        {
            return @"\\" + path.Substring(8);
        }
        if (path.StartsWith(@"\\?\", StringComparison.OrdinalIgnoreCase))
        {
            return path.Substring(4);
        }
        return path;
    }

    private static bool InheritedSentinel()
    {
        string rawHandle = Environment.GetEnvironmentVariable(
            "WINTER_GATE_SENTINEL_HANDLE");
        string expectedPath = Environment.GetEnvironmentVariable(
            "WINTER_GATE_SENTINEL_PATH");
        long handleValue;
        if (String.IsNullOrEmpty(rawHandle) ||
            String.IsNullOrEmpty(expectedPath) ||
            !Int64.TryParse(rawHandle, out handleValue))
        {
            return false;
        }

        StringBuilder buffer = new StringBuilder(32768);
        uint written = GetFinalPathNameByHandleW(
            new IntPtr(handleValue),
            buffer,
            checked((uint)buffer.Capacity),
            0);
        if (written == 0 || written >= buffer.Capacity)
        {
            return false;
        }
        return String.Equals(
            NormalizeFinalPath(buffer.ToString()),
            Path.GetFullPath(expectedPath),
            StringComparison.OrdinalIgnoreCase);
    }

    private static bool VerifyExpectedGateJob(string expectedJobName)
    {
        if (String.IsNullOrEmpty(expectedJobName))
        {
            return false;
        }
        IntPtr expectedJob = OpenJobObjectW(
            JobObjectQuery,
            false,
            expectedJobName);
        if (expectedJob == IntPtr.Zero)
        {
            throw new System.ComponentModel.Win32Exception(
                Marshal.GetLastWin32Error(),
                "Could not open the gate-named Job Object.");
        }
        try
        {
            bool inExpectedJob;
            if (!IsProcessInJob(
                GetCurrentProcess(),
                expectedJob,
                out inExpectedJob))
            {
                throw new System.ComponentModel.Win32Exception(
                    Marshal.GetLastWin32Error(),
                    "Could not query membership in the gate-named Job Object.");
            }
            if (!inExpectedJob)
            {
                throw new InvalidOperationException(
                    "Child resumed before membership in the gate-named Job Object.");
            }
            return true;
        }
        finally
        {
            CloseHandle(expectedJob);
        }
    }

    private static void AppendRecord(Dictionary<string, object> record)
    {
        string recordPath = Environment.GetEnvironmentVariable(
            "WINTER_GATE_RECORD");
        if (String.IsNullOrEmpty(recordPath))
        {
            throw new InvalidOperationException("WINTER_GATE_RECORD is required.");
        }
        string json = new JavaScriptSerializer().Serialize(record);
        using (FileStream stream = new FileStream(
            recordPath,
            FileMode.Append,
            FileAccess.Write,
            FileShare.ReadWrite | FileShare.Delete))
        using (StreamWriter writer = new StreamWriter(
            stream,
            new UTF8Encoding(false)))
        {
            writer.WriteLine(json);
        }
    }

    private static Dictionary<string, object> LoadControl()
    {
        string path = Environment.GetEnvironmentVariable(
            "WINTER_GATE_CONTROL");
        if (String.IsNullOrEmpty(path) || !File.Exists(path))
        {
            return new Dictionary<string, object>();
        }
        return new JavaScriptSerializer().Deserialize<Dictionary<string, object>>(
            File.ReadAllText(path, Encoding.UTF8));
    }

    private static Dictionary<string, object> ObjectMap(
        Dictionary<string, object> owner,
        string key)
    {
        object value;
        if (!owner.TryGetValue(key, out value) || value == null)
        {
            return new Dictionary<string, object>();
        }
        Dictionary<string, object> result =
            value as Dictionary<string, object>;
        if (result == null)
        {
            throw new InvalidDataException(key + " control must be an object.");
        }
        return result;
    }

    private static int NextOrdinal()
    {
        string path = Environment.GetEnvironmentVariable("WINTER_GATE_RECORD");
        if (String.IsNullOrEmpty(path) || !File.Exists(path))
        {
            return 1;
        }
        int count = 0;
        foreach (string line in File.ReadAllLines(path, Encoding.UTF8))
        {
            if (!String.IsNullOrWhiteSpace(line))
            {
                count++;
            }
        }
        return checked(count + 1);
    }

    private static string StepName(string[] arguments)
    {
        if (arguments.Length >= 3 &&
            arguments[0] == "-m" &&
            arguments[1] == "unittest")
        {
            return "source-contract";
        }
        for (int index = 0; index < arguments.Length; index++)
        {
            string name = Path.GetFileName(arguments[index]).ToLowerInvariant();
            if (name == "check_winter_narrative_capabilities.py")
            {
                return "narrative-capability";
            }
            if (name == "scan_canon.py")
            {
                return "canon";
            }
            if (name == "scan_ai_smell.py")
            {
                return "ai-smell";
            }
            if (name == "scan_missing_portraits.py")
            {
                return "missing-portraits";
            }
            if (name == "scan_narration_overlap.py")
            {
                return "narration-overlap";
            }
            if (name == "scan_show_before_prevention.py")
            {
                return "show-before";
            }
            if (name == "scan_nested_quotes.py")
            {
                return "nested-quotes";
            }
        }
        return "unknown-python-step";
    }

    private static bool ContainsExactArgument(
        string[] arguments,
        string expected)
    {
        for (int index = 0; index < arguments.Length; index++)
        {
            if (String.Equals(
                arguments[index],
                expected,
                StringComparison.OrdinalIgnoreCase))
            {
                return true;
            }
        }
        return false;
    }

    private static void WriteControlledDocument(
        Dictionary<string, object> control,
        string step,
        string[] arguments)
    {
        Dictionary<string, object> documents = ObjectMap(
            control,
            "raw_documents");
        Dictionary<string, object> outputs = ObjectMap(
            control,
            "output_paths");
        object raw;
        if (!documents.TryGetValue(step, out raw))
        {
            return;
        }
        object outputValue;
        if (!outputs.TryGetValue(step, out outputValue))
        {
            throw new InvalidDataException(
                "Missing controlled output path for " + step + ".");
        }
        string output = Convert.ToString(outputValue);
        if (!ContainsExactArgument(arguments, output))
        {
            throw new InvalidDataException(
                "Gate did not pass the controlled output path for " + step + ".");
        }
        Directory.CreateDirectory(Path.GetDirectoryName(output));
        File.WriteAllText(output, Convert.ToString(raw), new UTF8Encoding(false));
    }

    private static string ApplyAfterStepControls(
        Dictionary<string, object> control,
        int ordinal)
    {
        string key = ordinal.ToString(
            System.Globalization.CultureInfo.InvariantCulture);
        Dictionary<string, object> precreate = ObjectMap(
            control,
            "precreate_after");
        object precreatePath;
        if (precreate.TryGetValue(key, out precreatePath))
        {
            string path = Convert.ToString(precreatePath);
            Directory.CreateDirectory(Path.GetDirectoryName(path));
            using (FileStream stream = new FileStream(
                path,
                FileMode.CreateNew,
                FileAccess.Write,
                FileShare.None))
            {
                byte[] marker = Encoding.UTF8.GetBytes("precreated-by-fixture\n");
                stream.Write(marker, 0, marker.Length);
            }
        }

        Dictionary<string, object> replacementGroups = ObjectMap(
            control,
            "replacements_after");
        object rawActions;
        if (!replacementGroups.TryGetValue(key, out rawActions))
        {
            return null;
        }
        IEnumerable actions = rawActions as IEnumerable;
        if (actions == null || rawActions is string)
        {
            throw new InvalidDataException(
                "replacement action group must be an array.");
        }
        foreach (object rawAction in actions)
        {
            Dictionary<string, object> action =
                rawAction as Dictionary<string, object>;
            if (action == null ||
                !action.ContainsKey("source") ||
                !action.ContainsKey("target"))
            {
                throw new InvalidDataException(
                    "replacement action must contain source and target.");
            }
            string source = Convert.ToString(action["source"]);
            string target = Convert.ToString(action["target"]);
            if (!MoveFileExW(
                source,
                target,
                MoveFileReplaceExisting | MoveFileWriteThrough))
            {
                int error = Marshal.GetLastWin32Error();
                return "MoveFileExW control failed with Win32 error " +
                    error.ToString(
                        System.Globalization.CultureInfo.InvariantCulture) +
                    " for target " + target;
            }
        }
        return null;
    }

    private static int ControlledExitCode(
        Dictionary<string, object> control,
        int ordinal)
    {
        Dictionary<string, object> exits = ObjectMap(control, "exit_codes");
        object value;
        if (!exits.TryGetValue(
            ordinal.ToString(System.Globalization.CultureInfo.InvariantCulture),
            out value))
        {
            return 0;
        }
        return Convert.ToInt32(value);
    }

    private static Process StartGrandchild(string executable)
    {
        ProcessStartInfo start = new ProcessStartInfo();
        start.FileName = executable;
        start.Arguments = "--winter-gate-grandchild";
        start.UseShellExecute = false;
        start.CreateNoWindow = true;
        return Process.Start(start);
    }

    private static string SwapStandardOutputLeaf(
        int standardHandle,
        string label,
        string forgedText)
    {
        IntPtr handle = GetStdHandle(standardHandle);
        if (handle == IntPtr.Zero || handle == new IntPtr(-1))
        {
            return "GetStdHandle(" + label + ") returned an invalid handle.";
        }
        StringBuilder buffer = new StringBuilder(32768);
        uint written = GetFinalPathNameByHandleW(
            handle,
            buffer,
            checked((uint)buffer.Capacity),
            0);
        if (written == 0 || written >= buffer.Capacity)
        {
            return "GetFinalPathNameByHandleW(" + label +
                ") failed with Win32 error " +
                Marshal.GetLastWin32Error().ToString(
                    System.Globalization.CultureInfo.InvariantCulture);
        }
        string fixedPath = NormalizeFinalPath(buffer.ToString());
        string movedPath = fixedPath + ".moved";
        if (!MoveFileExW(fixedPath, movedPath, MoveFileWriteThrough))
        {
            return "MoveFileExW(" + label +
                " fixed-to-moved) failed with Win32 error " +
                Marshal.GetLastWin32Error().ToString(
                    System.Globalization.CultureInfo.InvariantCulture);
        }
        try
        {
            File.WriteAllText(
                fixedPath,
                forgedText + "\n",
                new UTF8Encoding(false));
        }
        catch (Exception exception)
        {
            return "Recreating forged " + label + " failed: " +
                exception.GetType().FullName + ": " + exception.Message;
        }
        return null;
    }

    private static string SwapStandardOutputLeaves()
    {
        string error = SwapStandardOutputLeaf(
            StdOutputHandle,
            "stdout",
            "FORGED-STDOUT");
        if (!String.IsNullOrEmpty(error))
        {
            return error;
        }
        return SwapStandardOutputLeaf(
            StdErrorHandle,
            "stderr",
            "FORGED-STDERR");
    }

    private static void SwapEvidenceDirectory()
    {
        string powershell = Environment.GetEnvironmentVariable(
            "WINTER_GATE_TRUSTED_POWERSHELL");
        if (String.IsNullOrEmpty(powershell))
        {
            throw new InvalidOperationException(
                "WINTER_GATE_TRUSTED_POWERSHELL is required for the swap fixture.");
        }
        string script =
            "$ErrorActionPreference='Stop';" +
            "Move-Item -LiteralPath $env:WINTER_GATE_EVIDENCE_DIR " +
            "-Destination $env:WINTER_GATE_EVIDENCE_OLD;" +
            "$null=New-Item -ItemType Junction " +
            "-Path $env:WINTER_GATE_EVIDENCE_DIR " +
            "-Target $env:WINTER_GATE_SWAP_TARGET";
        string encoded = Convert.ToBase64String(
            Encoding.Unicode.GetBytes(script));
        ProcessStartInfo start = new ProcessStartInfo();
        start.FileName = powershell;
        start.Arguments =
            "-NoLogo -NoProfile -NonInteractive -ExecutionPolicy Bypass " +
            "-EncodedCommand " + encoded;
        start.UseShellExecute = false;
        start.CreateNoWindow = true;
        using (Process process = Process.Start(start))
        {
            if (!process.WaitForExit(10000))
            {
                process.Kill();
                throw new TimeoutException("Evidence swap helper timed out.");
            }
            if (process.ExitCode != 0)
            {
                throw new InvalidOperationException(
                    "Evidence swap helper exited " + process.ExitCode + ".");
            }
        }
    }

    private static string SwapProjectDirectory()
    {
        string project = Environment.GetEnvironmentVariable(
            "WINTER_GATE_PROJECT_DIR");
        string moved = Environment.GetEnvironmentVariable(
            "WINTER_GATE_PROJECT_OLD");
        if (String.IsNullOrEmpty(project) || String.IsNullOrEmpty(moved))
        {
            return "Project-swap fixture paths are required.";
        }
        string outside = Path.GetDirectoryName(moved);
        if (String.IsNullOrEmpty(outside))
        {
            return "Project-swap fixture has no outside working directory.";
        }
        Directory.SetCurrentDirectory(outside);
        if (!MoveFileExW(project, moved, MoveFileWriteThrough))
        {
            return "MoveFileExW project swap failed with Win32 error " +
                Marshal.GetLastWin32Error().ToString(
                    System.Globalization.CultureInfo.InvariantCulture);
        }
        Directory.CreateDirectory(project);
        return null;
    }

    public static int Main(string[] arguments)
    {
        if (arguments.Length == 1 &&
            arguments[0] == "--winter-gate-grandchild")
        {
            Thread.Sleep(Timeout.Infinite);
            return 0;
        }

        string expectedJobName = Environment.GetEnvironmentVariable(
            "WINTER_GATE_JOB_NAME");
        bool inExpectedJob = VerifyExpectedGateJob(expectedJobName);
        bool inJob;
        if (!IsProcessInJob(GetCurrentProcess(), IntPtr.Zero, out inJob))
        {
            throw new System.ComponentModel.Win32Exception(
                Marshal.GetLastWin32Error());
        }

        string mode = Environment.GetEnvironmentVariable(
            "WINTER_GATE_FAKE_MODE") ?? "normal";
        Dictionary<string, object> control = LoadControl();
        int ordinal = NextOrdinal();
        string step = StepName(arguments);
        Process child = null;
        if (mode == "timeout-tree" || mode == "leak-tree")
        {
            child = StartGrandchild(Environment.GetCommandLineArgs()[0]);
        }
        bool swappedEvidence = false;
        if (mode == "swap-evidence")
        {
            SwapEvidenceDirectory();
            swappedEvidence = true;
        }
        WriteControlledDocument(control, step, arguments);
        string controlError = ApplyAfterStepControls(control, ordinal);
        if (String.IsNullOrEmpty(controlError) && mode == "swap-project")
        {
            controlError = SwapProjectDirectory();
        }
        bool swappedOutputLeaves = false;
        if (String.IsNullOrEmpty(controlError) && mode == "swap-output-leaves")
        {
            controlError = SwapStandardOutputLeaves();
            swappedOutputLeaves = String.IsNullOrEmpty(controlError);
        }

        Dictionary<string, object> record =
            new Dictionary<string, object>();
        record["kind"] = "Python";
        record["step"] = step;
        record["ordinal"] = ordinal;
        record["argv0"] = Environment.GetCommandLineArgs()[0];
        record["argv"] = arguments;
        record["cwd"] = Directory.GetCurrentDirectory();
        record["pid"] = Process.GetCurrentProcess().Id;
        record["child_pid"] = child == null ? (object)null : child.Id;
        record["in_job"] = inJob;
        record["expected_job_name"] = expectedJobName;
        record["in_expected_job"] = inExpectedJob;
        record["stdin_file_type"] = GetFileType(GetStdHandle(StdInputHandle));
        record["sentinel_inherited"] = InheritedSentinel();
        record["swapped_evidence"] = swappedEvidence;
        record["swapped_output_leaves"] = swappedOutputLeaves;
        record["control_error"] = controlError;
        AppendRecord(record);

        Console.Out.WriteLine("fake-python-stdout");
        Console.Out.Flush();
        Console.Error.WriteLine("fake-python-stderr");
        Console.Error.Flush();

        if (mode == "writer-race")
        {
            string readyPath = Environment.GetEnvironmentVariable(
                "WINTER_GATE_WRITER_RACE_READY");
            string releasePath = Environment.GetEnvironmentVariable(
                "WINTER_GATE_WRITER_RACE_RELEASE");
            if (String.IsNullOrEmpty(readyPath) ||
                String.IsNullOrEmpty(releasePath))
            {
                throw new InvalidOperationException(
                    "Writer-race fixture paths are required.");
            }
            File.WriteAllText(
                readyPath,
                "ready",
                new UTF8Encoding(false));
            DateTime deadline = DateTime.UtcNow.AddSeconds(15);
            while (!File.Exists(releasePath) && DateTime.UtcNow < deadline)
            {
                Thread.Sleep(10);
            }
            if (!File.Exists(releasePath))
            {
                throw new TimeoutException(
                    "Writer-race fixture release was not observed.");
            }
        }

        if (mode == "timeout-tree")
        {
            Thread.Sleep(Timeout.Infinite);
        }

        if (!String.IsNullOrEmpty(controlError))
        {
            return 97;
        }

        int requestedExitCode;
        if (Int32.TryParse(
            Environment.GetEnvironmentVariable("WINTER_GATE_FAKE_EXIT"),
            out requestedExitCode))
        {
            return requestedExitCode;
        }
        return ControlledExitCode(control, ordinal);
    }
}
'''


FAKE_RUNNER_SOURCE = r'''
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)][string]$ProjectRoot,
    [Parameter(Mandatory = $true)][string]$SaveDir,
    [Parameter(Mandatory = $true)][string]$Mode,
    [Parameter(Mandatory = $true)][string]$Suite,
    [Parameter(Mandatory = $true)][string]$Expect,
    [Parameter(Mandatory = $true)][string]$EvidenceDir,
    [Parameter(Mandatory = $true)][int]$TimeoutSeconds
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$existingRecords = if ([IO.File]::Exists($env:WINTER_GATE_RECORD)) {
    @([IO.File]::ReadAllLines($env:WINTER_GATE_RECORD) | Where-Object {
        -not [string]::IsNullOrWhiteSpace($_)
    }).Count
} else { 0 }
$ordinal = $existingRecords + 1
$record = [ordered]@{
    kind = 'RenPySuite'
    step = $Suite.Replace('_', '-')
    ordinal = $ordinal
    argv = @($MyInvocation.UnboundArguments)
    cwd = [Environment]::CurrentDirectory
    pid = $PID
    child_pid = $null
    suite = $Suite
    parameters = [ordered]@{
        ProjectRoot = $ProjectRoot
        SaveDir = $SaveDir
        Mode = $Mode
        Suite = $Suite
        Expect = $Expect
        EvidenceDir = $EvidenceDir
        TimeoutSeconds = $TimeoutSeconds
    }
    control_error = $null
}
if ($env:WINTER_GATE_RUNNER_LEAK_SUITE -eq $Suite) {
    $child = Start-Process `
        -FilePath $env:WINTER_GATE_FAKE_PYTHON `
        -ArgumentList '--winter-gate-grandchild' `
        -WindowStyle Hidden `
        -PassThru
    $record.child_pid = $child.Id
}
$json = $record | ConvertTo-Json -Compress -Depth 8
[IO.File]::AppendAllText(
    $env:WINTER_GATE_RECORD,
    $json + [Environment]::NewLine,
    [Text.UTF8Encoding]::new($false))
[Console]::Out.WriteLine('PASSED fake-runner-stdout')
[Console]::Error.WriteLine('fake-runner-stderr')
$exitCode = 0
if ([IO.File]::Exists($env:WINTER_GATE_CONTROL)) {
    $control = [IO.File]::ReadAllText(
        $env:WINTER_GATE_CONTROL,
        [Text.Encoding]::UTF8) | ConvertFrom-Json
    $property = $control.exit_codes.PSObject.Properties[[string]$ordinal]
    if ($null -ne $property) { $exitCode = [int]$property.Value }
}
exit $exitCode
'''


class _SecurityAttributes(ctypes.Structure):
    _fields_ = (
        ("length", ctypes.c_uint32),
        ("security_descriptor", ctypes.c_void_p),
        ("inherit_handle", ctypes.c_int32),
    )


class _Overlapped(ctypes.Structure):
    _fields_ = (
        ("Internal", ctypes.c_size_t),
        ("InternalHigh", ctypes.c_size_t),
        ("Offset", wintypes.DWORD),
        ("OffsetHigh", wintypes.DWORD),
        ("hEvent", wintypes.HANDLE),
    )


class _RequestOplockInput(ctypes.Structure):
    _fields_ = (
        ("StructureVersion", wintypes.WORD),
        ("StructureLength", wintypes.WORD),
        ("RequestedOplockLevel", wintypes.DWORD),
        ("Flags", wintypes.DWORD),
    )


class _RequestOplockOutput(ctypes.Structure):
    _fields_ = (
        ("StructureVersion", wintypes.WORD),
        ("StructureLength", wintypes.WORD),
        ("OriginalOplockLevel", wintypes.DWORD),
        ("NewOplockLevel", wintypes.DWORD),
        ("Flags", wintypes.DWORD),
        ("AccessMode", wintypes.DWORD),
        ("ShareMode", wintypes.WORD),
    )


class _ReadHandleOplock:
    DELETE_ACCESS = 0x00010000
    FILE_READ_DATA = 0x00000001
    FILE_READ_ATTRIBUTES = 0x00000080
    FILE_SHARE_READ = 0x00000001
    FILE_SHARE_WRITE = 0x00000002
    FILE_SHARE_DELETE = 0x00000004
    OPEN_EXISTING = 3
    FILE_FLAG_OPEN_REPARSE_POINT = 0x00200000
    FILE_FLAG_BACKUP_SEMANTICS = 0x02000000
    FILE_FLAG_OVERLAPPED = 0x40000000
    FSCTL_REQUEST_OPLOCK = 0x00090240
    OPLOCK_LEVEL_CACHE_READ = 0x00000001
    OPLOCK_LEVEL_CACHE_HANDLE = 0x00000002
    OPLOCK_LEVEL_CACHE_WRITE = 0x00000004
    REQUEST_OPLOCK_INPUT_FLAG_REQUEST = 0x00000001
    ERROR_IO_PENDING = 997
    WAIT_OBJECT_0 = 0
    FILE_RENAME_INFO = 3

    def __init__(
        self,
        path: Path,
        *,
        desired_access: int,
        share_mode: int,
        extra_flags: int,
        requested_oplock_level: int,
    ) -> None:
        self.path = path.resolve()
        self.kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
        self.close_handle = self.kernel32.CloseHandle
        self.close_handle.argtypes = (wintypes.HANDLE,)
        self.close_handle.restype = wintypes.BOOL
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
            str(self.path),
            desired_access,
            share_mode,
            None,
            self.OPEN_EXISTING,
            self.FILE_FLAG_OPEN_REPARSE_POINT
            | self.FILE_FLAG_OVERLAPPED
            | extra_flags,
            None,
        )
        if not handle or int(handle) == ctypes.c_void_p(-1).value:
            raise ctypes.WinError(ctypes.get_last_error())
        self.directory_handle: int | None = int(handle)

        create_event = self.kernel32.CreateEventW
        create_event.argtypes = (
            ctypes.c_void_p,
            wintypes.BOOL,
            wintypes.BOOL,
            wintypes.LPCWSTR,
        )
        create_event.restype = wintypes.HANDLE
        event = create_event(None, True, False, None)
        if not event:
            self.close()
            raise ctypes.WinError(ctypes.get_last_error())
        self.event_handle: int | None = int(event)
        self.overlapped = _Overlapped()
        self.overlapped.hEvent = wintypes.HANDLE(self.event_handle)
        request = _RequestOplockInput(
            1,
            ctypes.sizeof(_RequestOplockInput),
            requested_oplock_level,
            self.REQUEST_OPLOCK_INPUT_FLAG_REQUEST,
        )
        self.response = _RequestOplockOutput()
        returned = wintypes.DWORD()
        device_io = self.kernel32.DeviceIoControl
        device_io.argtypes = (
            wintypes.HANDLE,
            wintypes.DWORD,
            ctypes.c_void_p,
            wintypes.DWORD,
            ctypes.c_void_p,
            wintypes.DWORD,
            ctypes.POINTER(wintypes.DWORD),
            ctypes.POINTER(_Overlapped),
        )
        device_io.restype = wintypes.BOOL
        ok = device_io(
            wintypes.HANDLE(self.directory_handle),
            self.FSCTL_REQUEST_OPLOCK,
            ctypes.byref(request),
            ctypes.sizeof(request),
            ctypes.byref(self.response),
            ctypes.sizeof(self.response),
            ctypes.byref(returned),
            ctypes.byref(self.overlapped),
        )
        error = ctypes.get_last_error()
        if ok or error != self.ERROR_IO_PENDING:
            self.close()
            if ok:
                raise AssertionError("directory oplock completed synchronously")
            raise ctypes.WinError(error)

    def wait_for_break(self, timeout_milliseconds: int = 10000) -> None:
        wait = self.kernel32.WaitForSingleObject
        wait.argtypes = (wintypes.HANDLE, wintypes.DWORD)
        wait.restype = wintypes.DWORD
        status = wait(
            wintypes.HANDLE(self.event_handle),
            timeout_milliseconds,
        )
        if status != self.WAIT_OBJECT_0:
            raise AssertionError(
                f"writer did not reach its directory guard: wait={status}"
            )

    def rename_to(self, target: Path) -> None:
        target = target.resolve()
        target_bytes = str(target).encode("utf-16-le")
        name_offset = 20 if ctypes.sizeof(ctypes.c_void_p) == 8 else 12
        root_offset = 8 if name_offset == 20 else 4
        length_offset = 16 if name_offset == 20 else 8
        information = ctypes.create_string_buffer(
            name_offset + len(target_bytes) + 2
        )
        ctypes.c_void_p.from_buffer(information, root_offset).value = None
        ctypes.c_uint32.from_buffer(information, length_offset).value = len(
            target_bytes
        )
        ctypes.memmove(
            ctypes.addressof(information) + name_offset,
            target_bytes,
            len(target_bytes),
        )
        rename = self.kernel32.SetFileInformationByHandle
        rename.argtypes = (
            wintypes.HANDLE,
            ctypes.c_int,
            ctypes.c_void_p,
            wintypes.DWORD,
        )
        rename.restype = wintypes.BOOL
        if not rename(
            wintypes.HANDLE(self.directory_handle),
            self.FILE_RENAME_INFO,
            information,
            len(information),
        ):
            raise ctypes.WinError(ctypes.get_last_error())

    def release(self) -> None:
        if self.directory_handle is not None:
            handle, self.directory_handle = self.directory_handle, None
            if not self.close_handle(wintypes.HANDLE(handle)):
                raise ctypes.WinError(ctypes.get_last_error())

    def close(self) -> None:
        self.release()
        if getattr(self, "event_handle", None) is not None:
            handle, self.event_handle = self.event_handle, None
            if not self.close_handle(wintypes.HANDLE(handle)):
                raise ctypes.WinError(ctypes.get_last_error())


class _DirectoryReadHandleOplock(_ReadHandleOplock):
    def __init__(self, path: Path) -> None:
        super().__init__(
            path,
            desired_access=self.DELETE_ACCESS,
            share_mode=0,
            extra_flags=self.FILE_FLAG_BACKUP_SEMANTICS,
            requested_oplock_level=(
                self.OPLOCK_LEVEL_CACHE_READ | self.OPLOCK_LEVEL_CACHE_HANDLE
            ),
        )


class _FileReadHandleOplock(_ReadHandleOplock):
    def __init__(self, path: Path) -> None:
        super().__init__(
            path,
            desired_access=self.FILE_READ_DATA,
            share_mode=(
                self.FILE_SHARE_READ
                | self.FILE_SHARE_WRITE
                | self.FILE_SHARE_DELETE
            ),
            extra_flags=0,
            requested_oplock_level=(
                self.OPLOCK_LEVEL_CACHE_READ
                | self.OPLOCK_LEVEL_CACHE_WRITE
                | self.OPLOCK_LEVEL_CACHE_HANDLE
            ),
        )


class _SharedDirectoryMutationOplock(_ReadHandleOplock):
    def __init__(self, path: Path) -> None:
        super().__init__(
            path,
            desired_access=self.FILE_READ_ATTRIBUTES,
            share_mode=(
                self.FILE_SHARE_READ
                | self.FILE_SHARE_WRITE
                | self.FILE_SHARE_DELETE
            ),
            extra_flags=self.FILE_FLAG_BACKUP_SEMANTICS,
            requested_oplock_level=(
                self.OPLOCK_LEVEL_CACHE_READ | self.OPLOCK_LEVEL_CACHE_HANDLE
            ),
        )


# END LOOP 3.3-T1A RECORDING CHILD AND CONTROL SUPPORT


# BEGIN LOOP 3.1-T0 READABLE PROBE SUPPORT
def create_junction(path: Path, target: Path) -> None:
    environment = os.environ.copy()
    environment.update(
        {
            "WINTER_GATE_JUNCTION": str(path),
            "WINTER_GATE_JUNCTION_TARGET": str(target),
        }
    )
    completed = subprocess.run(
        [
            str(POWERSHELL),
            "-NoLogo",
            "-NoProfile",
            "-NonInteractive",
            "-Command",
            "$ErrorActionPreference='Stop';"
            "$null=New-Item -ItemType Junction "
            "-Path $env:WINTER_GATE_JUNCTION "
            "-Target $env:WINTER_GATE_JUNCTION_TARGET",
        ],
        env=environment,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=15,
        check=False,
    )
    if completed.returncode != 0:
        raise AssertionError("junction creation failed:\n" + completed.stderr)


def framework_csc() -> Path:
    windows = trusted_system_directory().parent
    candidates = (
        windows / "Microsoft.NET" / "Framework64" / "v4.0.30319" / "csc.exe",
        windows / "Microsoft.NET" / "Framework" / "v4.0.30319" / "csc.exe",
    )
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    raise AssertionError(".NET Framework 4.x csc.exe is unavailable")


# END LOOP 3.1-T0 READABLE PROBE SUPPORT


# BEGIN LOOP 3.3-T1B RECORDING CHILD AND CONTROL SUPPORT
def git_executable() -> Path:
    resolved = shutil.which("git.exe")
    if not resolved:
        raise AssertionError("git.exe is required for the HEAD-binding tests")
    return Path(resolved).resolve()


def compile_recording_child(source: Path, output: Path) -> None:
    csc = framework_csc()
    reference = csc.parent / "System.Web.Extensions.dll"
    completed = subprocess.run(
        [
            str(csc),
            "/nologo",
            "/target:exe",
            "/platform:anycpu",
            f"/out:{output}",
            f"/reference:{reference}",
            str(source),
        ],
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if completed.returncode != 0:
        raise AssertionError(
            "recording child compilation failed:\n" + completed.stdout
        )


# END LOOP 3.3-T1B RECORDING CHILD AND CONTROL SUPPORT


NATIVE_WRITER_PROBE_SOURCE = r'''
using System;
using System.IO;

internal static class NativeWriterProbe
{
    public static int Main(string[] arguments)
    {
        if (arguments.Length != 2)
        {
            Console.Error.WriteLine("mode and evidence directory are required");
            return 2;
        }
        try
        {
            string mode = arguments[0];
            string evidence = Path.GetFullPath(arguments[1]);
            string json = "{\"mode\":\"" + mode + "\",\"blob\":\"" +
                "small-exact-source-payload\"}";
            WinterGate.PathIdentity identity = WinterGate.Native.GetPathIdentity(
                evidence,
                WinterGate.PathKind.Directory,
                true);
            if (mode == "result")
            {
                WinterGate.Native.WriteUtf8JsonCreateNew(
                    Path.Combine(evidence, "probe.result.json"),
                    json,
                    identity);
            }
            else if (mode == "summary")
            {
                WinterGate.Native.WriteOwnedSummaryUtf8Json(
                    Path.Combine(evidence, "gate-summary.json"),
                    json,
                    json,
                    identity);
            }
            else
            {
                Console.Error.WriteLine("unknown writer mode: " + mode);
                return 3;
            }
            return 0;
        }
        catch (WinterGate.WinterGatePathIdentityException exception)
        {
            Console.Error.WriteLine("IDENTITY_FAILURE: " + exception);
            return 91;
        }
        catch (Exception exception)
        {
            Console.Error.WriteLine("UNEXPECTED_FAILURE: " + exception);
            return 92;
        }
    }
}
'''


NATIVE_READABLE_PROBE_SOURCE = r'''
using System;

internal static class NativeReadableProbe
{
    public static int Main(string[] arguments)
    {
        if (arguments.Length != 1)
        {
            return 2;
        }
        try
        {
            WinterGate.PathIdentity identity =
                WinterGate.Native.GetReadableFileIdentity(arguments[0]);
            Console.Out.WriteLine(identity.FinalPath);
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


def extract_native_source(gate: Path = GATE) -> str:
    script = gate.read_text(encoding="utf-8")
    matches = re.findall(
        r"\$nativeSource\s*=\s*@'\r?\n(.*?)\r?\n'@",
        script,
        flags=re.DOTALL,
    )
    if len(matches) != 1:
        raise AssertionError(
            f"expected one exact native source here-string, found {len(matches)}"
        )
    return matches[0]


def compile_native_writer_probe(
    build: Path,
    native_source: str,
) -> Path:
    build.mkdir(parents=True)
    native_cs = build / "WinterGate.Native.cs"
    native_dll = build / "WinterGate.Native.dll"
    probe_cs = build / "NativeWriterProbe.cs"
    probe_exe = build / "NativeWriterProbe.exe"
    native_cs.write_text(native_source, encoding="utf-8")
    probe_cs.write_text(NATIVE_WRITER_PROBE_SOURCE, encoding="utf-8")
    for arguments in (
        (
            "/target:library",
            f"/out:{native_dll}",
            str(native_cs),
        ),
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
                "exact native writer probe compilation failed:\n"
                + completed.stdout
            )
    return probe_exe


def compile_native_readable_probe(
    build: Path,
    native_source: str,
) -> Path:
    build.mkdir(parents=True)
    native_cs = build / "WinterGate.Native.cs"
    native_dll = build / "WinterGate.Native.dll"
    probe_cs = build / "NativeReadableProbe.cs"
    probe_exe = build / "NativeReadableProbe.exe"
    native_cs.write_text(native_source, encoding="utf-8")
    probe_cs.write_text(NATIVE_READABLE_PROBE_SOURCE, encoding="utf-8")
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
                "exact native readable probe compilation failed:\n"
                + completed.stdout
            )
    return probe_exe


NATIVE_EXECUTABLE_ACCESS_PROBE_SOURCE = r'''
using System;

internal static class NativeExecutableAccessProbe
{
    public static int Main(string[] arguments)
    {
        if (arguments.Length != 2)
        {
            return 2;
        }
        try
        {
            WinterGate.PathIdentity identity = arguments[0] == "path"
                ? WinterGate.Native.GetPathIdentity(
                    arguments[1],
                    WinterGate.PathKind.File,
                    true)
                : WinterGate.Native.GetReadableFileIdentity(arguments[1]);
            Console.Out.WriteLine(identity.FinalPath);
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


def compile_native_executable_access_probe(
    build: Path,
    native_source: str,
) -> Path:
    build.mkdir(parents=True)
    native_cs = build / "WinterGate.Native.cs"
    native_dll = build / "WinterGate.Native.dll"
    probe_cs = build / "NativeExecutableAccessProbe.cs"
    probe_exe = build / "NativeExecutableAccessProbe.exe"
    native_cs.write_text(native_source, encoding="utf-8")
    probe_cs.write_text(
        NATIVE_EXECUTABLE_ACCESS_PROBE_SOURCE,
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
                "native executable access probe compilation failed:\n"
                + completed.stdout
            )
    return probe_exe


def deny_read_extended_attributes(path: Path) -> None:
    sid = subprocess.run(
        [
            str(POWERSHELL),
            "-NoLogo",
            "-NoProfile",
            "-NonInteractive",
            "-Command",
            "[Security.Principal.WindowsIdentity]::GetCurrent().User.Value",
        ],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=15,
        check=False,
    )
    if sid.returncode != 0 or not sid.stdout.strip():
        raise AssertionError("could not resolve current Windows SID: " + sid.stderr)
    icacls = trusted_system_directory() / "icacls.exe"
    denied = subprocess.run(
        [str(icacls), str(path), "/deny", f"*{sid.stdout.strip()}:(REA)"],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=15,
        check=False,
    )
    if denied.returncode != 0:
        raise AssertionError("could not apply executable ACL: " + denied.stderr)


class _NamedManualResetEvent:
    WAIT_OBJECT_0 = 0
    ERROR_ALREADY_EXISTS = 183

    def __init__(self, label: str) -> None:
        self.kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
        self.name = (
            "Local\\WinterGateNativeWriter-"
            + label
            + "-"
            + str(os.getpid())
            + "-"
            + os.urandom(12).hex()
        )
        create = self.kernel32.CreateEventW
        create.argtypes = (
            ctypes.c_void_p,
            wintypes.BOOL,
            wintypes.BOOL,
            wintypes.LPCWSTR,
        )
        create.restype = wintypes.HANDLE
        ctypes.set_last_error(0)
        handle = create(None, True, False, self.name)
        if not handle:
            raise ctypes.WinError(ctypes.get_last_error())
        if ctypes.get_last_error() == self.ERROR_ALREADY_EXISTS:
            self.kernel32.CloseHandle(handle)
            raise AssertionError(f"named event collision: {self.name}")
        self.handle: int | None = int(handle)

    def wait(self, timeout_milliseconds: int = 30000) -> None:
        wait = self.kernel32.WaitForSingleObject
        wait.argtypes = (wintypes.HANDLE, wintypes.DWORD)
        wait.restype = wintypes.DWORD
        status = wait(wintypes.HANDLE(self.handle), timeout_milliseconds)
        if status != self.WAIT_OBJECT_0:
            raise AssertionError(
                f"test-only native writer barrier was not reached: wait={status}"
            )

    def set(self) -> None:
        set_event = self.kernel32.SetEvent
        set_event.argtypes = (wintypes.HANDLE,)
        set_event.restype = wintypes.BOOL
        if not set_event(wintypes.HANDLE(self.handle)):
            raise ctypes.WinError(ctypes.get_last_error())

    def close(self) -> None:
        if self.handle is None:
            return
        handle, self.handle = self.handle, None
        close = self.kernel32.CloseHandle
        close.argtypes = (wintypes.HANDLE,)
        close.restype = wintypes.BOOL
        if not close(wintypes.HANDLE(handle)):
            raise ctypes.WinError(ctypes.get_last_error())


_NATIVE_WRITER_PAUSE_CALL = "            TestOnlyWaitBeforeWriterFlush();\n"
_NATIVE_WRITER_PAUSE_HELPER_ANCHOR = (
    "    private static PathIdentity OpenVerifiedEvidenceGuard("
)
_NATIVE_WRITER_RESULT_WRITE_ANCHOR = (
    '            WriteAllAndFlush(jsonHandle, utf8Bytes, "JSON");'
)
_NATIVE_WRITER_SUMMARY_WRITE_ANCHOR = """            WriteAllAndFlush(
                stagingHandle,
                quarantinedExistingSummary
                    ? collisionUtf8Bytes
                    : normalUtf8Bytes,
                "summary staging");"""
_NATIVE_WRITER_PAUSE_HELPER = r'''    private static void TestOnlyWaitBeforeWriterFlush()
    {
        string readyName = Environment.GetEnvironmentVariable(
            "WINTER_GATE_TEST_WRITER_READY_EVENT");
        string releaseName = Environment.GetEnvironmentVariable(
            "WINTER_GATE_TEST_WRITER_RELEASE_EVENT");
        if (String.IsNullOrEmpty(readyName) ||
            String.IsNullOrEmpty(releaseName))
        {
            throw new InvalidOperationException(
                "test-only native writer event names are required.");
        }
        using (EventWaitHandle ready = EventWaitHandle.OpenExisting(readyName))
        using (EventWaitHandle release = EventWaitHandle.OpenExisting(releaseName))
        {
            if (!ready.Set())
            {
                throw new InvalidOperationException(
                    "test-only native writer ready event could not be set.");
            }
            if (!release.WaitOne(30000))
            {
                throw new TimeoutException(
                    "test-only native writer release event timed out.");
            }
        }
    }

'''


def restore_native_writer_pause(source: str) -> str:
    if source.count(_NATIVE_WRITER_PAUSE_CALL) != 2:
        raise AssertionError("instrumented writer must contain exactly two pause calls")
    if source.count(_NATIVE_WRITER_PAUSE_HELPER) != 1:
        raise AssertionError("instrumented writer must contain exactly one pause helper")
    restored = source.replace(_NATIVE_WRITER_PAUSE_CALL, "")
    restored = restored.replace(_NATIVE_WRITER_PAUSE_HELPER, "", 1)
    return restored


def instrument_native_writer_pause(source: str) -> str:
    for forbidden in (
        "TestOnlyWaitBeforeWriterFlush",
        "WINTER_GATE_TEST_WRITER_READY_EVENT",
        "WINTER_GATE_TEST_WRITER_RELEASE_EVENT",
    ):
        if forbidden in source:
            raise AssertionError(f"production native source contains {forbidden}")
    for label, anchor in (
        ("helper", _NATIVE_WRITER_PAUSE_HELPER_ANCHOR),
        ("result write", _NATIVE_WRITER_RESULT_WRITE_ANCHOR),
        ("summary write", _NATIVE_WRITER_SUMMARY_WRITE_ANCHOR),
    ):
        if source.count(anchor) != 1:
            raise AssertionError(f"expected one native writer {label} anchor")

    instrumented = source.replace(
        _NATIVE_WRITER_RESULT_WRITE_ANCHOR,
        _NATIVE_WRITER_PAUSE_CALL + _NATIVE_WRITER_RESULT_WRITE_ANCHOR,
        1,
    )
    instrumented = instrumented.replace(
        _NATIVE_WRITER_SUMMARY_WRITE_ANCHOR,
        _NATIVE_WRITER_PAUSE_CALL + _NATIVE_WRITER_SUMMARY_WRITE_ANCHOR,
        1,
    )
    instrumented = instrumented.replace(
        _NATIVE_WRITER_PAUSE_HELPER_ANCHOR,
        _NATIVE_WRITER_PAUSE_HELPER + _NATIVE_WRITER_PAUSE_HELPER_ANCHOR,
        1,
    )
    if restore_native_writer_pause(instrumented) != source:
        raise AssertionError("native writer pause instrumentation is not reversible")
    return instrumented


def mutate_native_writer_delete_sharing(source: str, mode: str) -> str:
    guard_start = source.index(
        "private static PathIdentity OpenVerifiedEvidenceGuard("
    )
    guard_end = source.index(
        "private static byte[] EncodeUtf8Json(",
        guard_start,
    )
    guard = source[guard_start:guard_end]
    guard_share = "FileShareRead | FileShareWrite,"
    if guard.count(guard_share) != 1:
        raise AssertionError("expected one evidence guard share-mode mutation target")
    guarded = guard.replace(
        guard_share,
        "FileShareRead | FileShareWrite | FileShareDelete,",
        1,
    )
    if guarded == guard:
        raise AssertionError("could not mutate evidence guard delete sharing")
    mutated = source[:guard_start] + guarded + source[guard_end:]
    if mode == "result":
        old = """jsonHandle = CreateFileW(
                path,
                GenericWrite,
                0,"""
        new = """jsonHandle = CreateFileW(
                path,
                GenericWrite,
                FileShareRead | FileShareWrite | FileShareDelete,"""
    elif mode == "summary":
        old = """stagingHandle = CreateFileW(
                stagingPath,
                GenericWrite | DeleteAccess,
                FileShareRead | FileShareWrite,"""
        new = """stagingHandle = CreateFileW(
                stagingPath,
                GenericWrite | DeleteAccess,
                FileShareRead | FileShareWrite | FileShareDelete,"""
    else:
        raise AssertionError(f"unknown writer mutation mode: {mode}")
    if mutated.count(old) != 1:
        raise AssertionError(
            f"expected one {mode} writer share-mode mutation target"
        )
    return mutated.replace(old, new, 1)


def assert_native_writer_lifecycle(
    case: unittest.TestCase,
    source: str,
) -> None:
    for forbidden_test_seam in (
        "WINTER_GATE_TEST_WRITER_READY_EVENT",
        "WINTER_GATE_TEST_WRITER_RELEASE_EVENT",
        "TestOnlyWaitBeforeWriterFlush",
    ):
        case.assertNotIn(forbidden_test_seam, source)

    summary_start = source.index(
        "public static string WriteOwnedSummaryUtf8Json("
    )
    result_start = source.index(
        "public static void WriteUtf8JsonCreateNew("
    )
    process_start = source.index("// END PROCESS ENGINE", result_start)
    summary_writer = source[summary_start:result_start]
    result_writer = source[result_start:process_start]

    def assert_order(region: str, anchors: tuple[str, ...]) -> None:
        offsets = tuple(region.index(anchor) for anchor in anchors)
        case.assertEqual(tuple(sorted(offsets)), offsets, anchors)

    assert_order(
        result_writer,
        (
            "OpenVerifiedEvidenceGuard(",
            "jsonHandle = CreateFileW(",
            "RequireDirectEvidenceChild(",
            "WriteAllAndFlush(",
            "finally",
            "CloseOwnedHandle(ref jsonHandle)",
        ),
    )
    result_after_flush = result_writer[
        result_writer.index("WriteAllAndFlush(") : result_writer.index("finally")
    ]
    case.assertNotIn("RequireDirectEvidenceChild(", result_after_flush)
    case.assertNotIn("GetPathIdentityFromOpenHandle(", result_after_flush)
    assert_order(
        summary_writer,
        (
            "OpenVerifiedEvidenceGuard(",
            "stagingHandle = CreateFileW(",
            "RequireDirectEvidenceChild(",
            "WriteAllAndFlush(",
            '"publish owned summary");',
            "finally",
            "CloseOwnedHandle(ref stagingHandle)",
        ),
    )
    flush_start = source.index("private static void WriteAllAndFlush(")
    flush_end = source.index(
        "private static void CloseOwnedHandle(ref IntPtr handle)",
        flush_start,
    )
    flush_helper = source[flush_start:flush_end]
    case.assertLess(
        flush_helper.index("WriteFile("),
        flush_helper.index("FlushFileBuffers("),
    )


def attempt_replace(source: Path, target: Path) -> tuple[bool, int | None]:
    try:
        os.replace(source, target)
    except OSError as exception:
        return False, getattr(exception, "winerror", None)
    return True, None


def attempt_winps_directory_move(
    source: Path,
    target: Path,
) -> subprocess.CompletedProcess[str]:
    environment = os.environ.copy()
    environment.update(
        {
            "WINTER_GATE_MOVE_SOURCE": str(source),
            "WINTER_GATE_MOVE_TARGET": str(target),
        }
    )
    return subprocess.run(
        [
            str(POWERSHELL),
            "-NoLogo",
            "-NoProfile",
            "-NonInteractive",
            "-Command",
            "$ErrorActionPreference = 'Stop'; "
            "Move-Item -LiteralPath $env:WINTER_GATE_MOVE_SOURCE "
            "-Destination $env:WINTER_GATE_MOVE_TARGET -ErrorAction Stop",
        ],
        cwd=source.parent,
        env=environment,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=15,
        check=False,
    )


@dataclass(frozen=True)
class _NativeWriterRaceObservation:
    mode: str
    barrier_leaf_size: int
    leaf_renamed: bool
    leaf_rename_error: int | None
    directory_renamed: bool
    directory_move_returncode: int
    directory_move_stdout: str
    directory_move_stderr: str
    post_close_directory_renamed: bool
    post_close_directory_move_returncode: int
    returncode: int
    stdout: str
    stderr: str
    complete_json_placements: tuple[str, ...]
    zero_byte_placements: tuple[str, ...]

    @property
    def honest_placement(self) -> str | None:
        if (
            self.returncode == 0
            and self.complete_json_placements == ("owned-fixed",)
        ):
            return "owned-fixed"
        return None


def is_complete_native_writer_json(
    path: Path,
    mode: str,
) -> bool:
    if not path.is_file():
        return False
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf") or not raw.endswith(b"\n"):
        return False
    try:
        document = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        return False
    return document == {
        "mode": mode,
        "blob": "small-exact-source-payload",
    }


def run_exact_native_writer_smoke(
    case: unittest.TestCase,
    base: Path,
    native_source: str,
) -> None:
    probe = compile_native_writer_probe(base / "build", native_source)
    for mode in ("result", "summary"):
        evidence = base / mode / "evidence"
        evidence.mkdir(parents=True)
        completed = subprocess.run(
            [str(probe), mode, str(evidence)],
            cwd=evidence.parent,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=30,
            check=False,
        )
        case.assertEqual(
            0,
            completed.returncode,
            completed.stdout + completed.stderr,
        )
        expected = evidence / (
            "probe.result.json" if mode == "result" else "gate-summary.json"
        )
        case.assertTrue(is_complete_native_writer_json(expected, mode), expected)
        case.assertEqual([], list(evidence.glob("gate-summary.pending.*.json")))


def run_native_writer_lock_probe(
    case: unittest.TestCase,
    base: Path,
    native_source: str,
    mode: str,
) -> _NativeWriterRaceObservation:
    build = base / f"native-writer-{mode}"
    instrumented_source = instrument_native_writer_pause(native_source)
    case.assertEqual(
        native_source,
        restore_native_writer_pause(instrumented_source),
    )
    probe = compile_native_writer_probe(build, instrumented_source)
    evidence = build / "evidence"
    evidence.mkdir()
    moved_evidence = build / "evidence-raced"
    stdout = ""
    stderr = ""
    process: subprocess.Popen[str] | None = None
    with contextlib.ExitStack() as cleanup:
        ready_event = _NamedManualResetEvent("ready")
        cleanup.callback(ready_event.close)
        release_event = _NamedManualResetEvent("release")
        cleanup.callback(release_event.close)
        environment = os.environ.copy()
        environment.update(
            {
                "WINTER_GATE_TEST_WRITER_READY_EVENT": ready_event.name,
                "WINTER_GATE_TEST_WRITER_RELEASE_EVENT": release_event.name,
            }
        )
        def stop_process() -> None:
            try:
                release_event.set()
            finally:
                if process is not None and process.poll() is None:
                    process.kill()
                    process.communicate(timeout=10)

        cleanup.callback(stop_process)
        process = subprocess.Popen(
            [str(probe), mode, str(evidence)],
            cwd=build,
            env=environment,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        ready_event.wait()
        case.assertIsNone(
            process.poll(),
            "instrumented native writer exited before its live-handle probe",
        )
        if mode == "result":
            live_leaf = evidence / "probe.result.json"
        else:
            pending = tuple(evidence.glob("gate-summary.pending.*.json"))
            case.assertEqual(1, len(pending), pending)
            live_leaf = pending[0]
        case.assertTrue(live_leaf.is_file(), live_leaf)
        barrier_leaf_size = live_leaf.stat().st_size
        case.assertEqual(0, barrier_leaf_size, live_leaf)

        moved_leaf = live_leaf.with_name(live_leaf.name + ".raced")
        leaf_renamed, leaf_error = attempt_replace(live_leaf, moved_leaf)
        if not leaf_renamed:
            case.assertIn(leaf_error, (5, 32, 33), leaf_error)

        directory_move = attempt_winps_directory_move(
            evidence,
            moved_evidence,
        )
        directory_renamed = directory_move.returncode == 0

        release_event.set()
        stdout, stderr = process.communicate(timeout=30)

    assert process is not None
    current_evidence = moved_evidence if directory_renamed else evidence
    expected_name = (
        "probe.result.json" if mode == "result" else "gate-summary.json"
    )
    candidates: list[tuple[str, Path]] = [
        ("owned-fixed", current_evidence / expected_name),
        ("owned-raced", current_evidence / (live_leaf.name + ".raced")),
    ]
    pending_path = current_evidence / live_leaf.name
    if pending_path != current_evidence / expected_name:
        candidates.append(("owned-pending", pending_path))
    complete_json_placements = tuple(
        placement
        for placement, candidate in candidates
        if is_complete_native_writer_json(candidate, mode)
    )
    zero_byte_placements = tuple(
        placement
        for placement, candidate in candidates
        if candidate.is_file() and candidate.stat().st_size == 0
    )

    post_run_target = build / "evidence-after-close"
    post_close_move = attempt_winps_directory_move(
        current_evidence,
        post_run_target,
    )
    return _NativeWriterRaceObservation(
        mode=mode,
        barrier_leaf_size=barrier_leaf_size,
        leaf_renamed=leaf_renamed,
        leaf_rename_error=leaf_error,
        directory_renamed=directory_renamed,
        directory_move_returncode=directory_move.returncode,
        directory_move_stdout=directory_move.stdout,
        directory_move_stderr=directory_move.stderr,
        post_close_directory_renamed=post_close_move.returncode == 0,
        post_close_directory_move_returncode=post_close_move.returncode,
        returncode=int(process.returncode),
        stdout=stdout,
        stderr=stderr,
        complete_json_placements=complete_json_placements,
        zero_byte_placements=zero_byte_placements,
    )


# BEGIN LOOP 3.3-T2 SHARED BLACK-BOX FIXTURE SUPPORT
def read_json_lines(path: Path) -> list[dict[str, object]]:
    if not path.exists():
        return []
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8-sig").splitlines()
        if line.strip()
    ]


def evidence_file(run_root: Path, relative: str) -> Path:
    candidate = Path(relative)
    if candidate.is_absolute():
        raise AssertionError(f"evidence path must be relative: {relative}")
    return run_root / candidate


def process_has_exited(pid: int) -> bool:
    synchronize = 0x00100000
    wait_object_0 = 0
    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    open_process = kernel32.OpenProcess
    open_process.argtypes = [ctypes.c_uint32, ctypes.c_int32, ctypes.c_uint32]
    open_process.restype = ctypes.c_void_p
    wait = kernel32.WaitForSingleObject
    wait.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    wait.restype = ctypes.c_uint32
    close = kernel32.CloseHandle
    close.argtypes = [ctypes.c_void_p]
    close.restype = ctypes.c_int32
    handle = open_process(synchronize, False, pid)
    if not handle:
        return True
    try:
        return wait(handle, 0) == wait_object_0
    finally:
        close(handle)


def assert_processes_exit(
    test: unittest.TestCase,
    *pids: int,
    timeout_seconds: float = 10.0,
) -> None:
    deadline = time.monotonic() + timeout_seconds
    pending = {int(pid) for pid in pids if pid is not None}
    while pending and time.monotonic() < deadline:
        pending = {pid for pid in pending if not process_has_exited(pid)}
        if pending:
            time.sleep(0.05)
    test.assertEqual(set(), pending, f"live recorded PIDs: {sorted(pending)}")


def create_inheritable_sentinel(path: Path) -> int:
    generic_read = 0x80000000
    share_all = 0x00000001 | 0x00000002 | 0x00000004
    open_existing = 3
    normal = 0x00000080
    invalid = ctypes.c_void_p(-1).value
    attributes = _SecurityAttributes(
        ctypes.sizeof(_SecurityAttributes),
        None,
        True,
    )
    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    create_file = kernel32.CreateFileW
    create_file.argtypes = [
        ctypes.c_wchar_p,
        ctypes.c_uint32,
        ctypes.c_uint32,
        ctypes.POINTER(_SecurityAttributes),
        ctypes.c_uint32,
        ctypes.c_uint32,
        ctypes.c_void_p,
    ]
    create_file.restype = ctypes.c_void_p
    handle = create_file(
        str(path),
        generic_read,
        share_all,
        ctypes.byref(attributes),
        open_existing,
        normal,
        None,
    )
    if not handle or handle == invalid:
        raise ctypes.WinError(ctypes.get_last_error())
    return int(handle)


def open_writable_shared_file(path: Path) -> int:
    generic_write = 0x40000000
    share_read_write = 0x00000001 | 0x00000002
    open_existing = 3
    normal = 0x00000080
    invalid = ctypes.c_void_p(-1).value
    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    create_file = kernel32.CreateFileW
    create_file.argtypes = [
        ctypes.c_wchar_p,
        ctypes.c_uint32,
        ctypes.c_uint32,
        ctypes.c_void_p,
        ctypes.c_uint32,
        ctypes.c_uint32,
        ctypes.c_void_p,
    ]
    create_file.restype = ctypes.c_void_p
    handle = create_file(
        str(path),
        generic_write,
        share_read_write,
        None,
        open_existing,
        normal,
        None,
    )
    if not handle or handle == invalid:
        raise ctypes.WinError(ctypes.get_last_error())
    return int(handle)


def close_windows_handle(handle: int) -> None:
    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    close = kernel32.CloseHandle
    close.argtypes = [ctypes.c_void_p]
    close.restype = ctypes.c_int32
    if not close(ctypes.c_void_p(handle)):
        raise ctypes.WinError(ctypes.get_last_error())


class _GateFixture:
    def __init__(self, case: unittest.TestCase) -> None:
        self.case = case
        self.temporary = tempfile.TemporaryDirectory(
            prefix="winter-gate-black-box-"
        )
        self.base = Path(self.temporary.name)
        self.root = self.base / "project space (paren) & apostrophe's"
        self.tools = self.root / "Tools"
        self.game = self.root / "game"
        self.tools.mkdir(parents=True)
        self.game.mkdir()
        fixed_files = (
            "Tools/test_governance_winter_interlude.py",
            "Tools/check_winter_narrative_capabilities.py",
            "Tools/scan_canon.py",
            "Tools/scan_ai_smell.py",
            "scan_missing_portraits.py",
            "scan_narration_overlap.py",
            "Tools/scan_show_before_prevention.py",
            "Tools/scan_nested_quotes.py",
            "game/governance_winter_interlude.rpy",
        )
        for relative in fixed_files:
            path = self.root / Path(relative)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(
                "# fixed fake-project identity input\n",
                encoding="utf-8",
            )
        (self.tools / "Run-RenPySuite.ps1").write_text(
            FAKE_RUNNER_SOURCE,
            encoding="utf-8",
        )

        self.fake_bin = self.base / "fake bin (compiled) & apostrophe's"
        self.fake_bin.mkdir()
        child_source = self.fake_bin / "recording-child.cs"
        child_source.write_text(RECORDING_CHILD_SOURCE, encoding="utf-8")
        self.python_exe = self.fake_bin / "python.exe"
        compile_recording_child(child_source, self.python_exe)

        self.records_path = self.base / "children.jsonl"
        self.control_path = self.base / "control.json"
        self.appdata = self.base / "isolated-appdata"
        self.appdata.mkdir()
        self.run_parent = (
            self.base / "external run space (paren) & apostrophe's"
        )
        self.run_parent.mkdir()
        self.run_root = self.run_parent / "run-01"
        self.swap_junctions: list[Path] = []
        self.has_run = False

    def close(self) -> None:
        for junction in reversed(self.swap_junctions):
            if junction.exists():
                os.rmdir(junction)
        self.temporary.cleanup()

    def register_junction(self, path: Path) -> None:
        self.swap_junctions.append(path)

    def _run_git(self, *arguments: str, cwd: Path | None = None) -> str:
        completed = subprocess.run(
            [str(git_executable()), *arguments],
            cwd=cwd or self.root,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=30,
            check=False,
        )
        if completed.returncode != 0:
            raise AssertionError(
                "git fixture command failed: "
                + " ".join(arguments)
                + "\n"
                + completed.stderr
            )
        return completed.stdout.strip()

    def initialize_git_repo(self) -> str:
        self._run_git("init")
        self._run_git("config", "user.name", "Winter Gate Test")
        self._run_git("config", "user.email", "winter-gate@example.invalid")
        self._run_git("add", "--all")
        self._run_git("commit", "-m", "fixture")
        head = self._run_git("rev-parse", "HEAD")
        if not re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", head):
            raise AssertionError(f"unexpected fixture HEAD: {head}")
        return head

    def use_linked_worktree_with_packed_refs(self) -> str:
        head = self.initialize_git_repo()
        linked_root = self.base / "linked worktree (packed refs)"
        self._run_git(
            "worktree",
            "add",
            "-b",
            "gate-linked",
            str(linked_root),
            "HEAD",
        )
        self._run_git("pack-refs", "--all", "--prune")
        self.root = linked_root
        self.tools = linked_root / "Tools"
        self.game = linked_root / "game"
        linked_gitdir, common_gitdir = self.linked_git_directories()
        self.case.assertTrue((linked_gitdir / "commondir").is_file())
        common_packed_refs = common_gitdir / "packed-refs"
        self.case.assertTrue(common_packed_refs.is_file())
        return head

    def linked_git_directories(self) -> tuple[Path, Path]:
        dot_git = self.root / ".git"
        self.case.assertTrue(dot_git.is_file(), dot_git)
        gitdir_line = dot_git.read_text(encoding="utf-8").strip()
        self.case.assertTrue(gitdir_line.startswith("gitdir: "), gitdir_line)
        linked_gitdir = Path(gitdir_line.removeprefix("gitdir: "))
        if not linked_gitdir.is_absolute():
            linked_gitdir = dot_git.parent / linked_gitdir
        linked_gitdir = linked_gitdir.resolve(strict=True)
        common_line = (linked_gitdir / "commondir").read_text(
            encoding="utf-8"
        ).strip()
        common_gitdir = Path(common_line)
        if not common_gitdir.is_absolute():
            common_gitdir = linked_gitdir / common_gitdir
        return linked_gitdir, common_gitdir.resolve(strict=True)

    def _output_paths(self) -> dict[str, str]:
        evidence = self.run_root / "evidence"
        return {
            "narrative-capability": str(
                evidence
                / "narrative-01-narrative-capability-no-head.output.json"
            ),
            "canon": str(
                evidence / "narrative-02-canon-no-head.output.json"
            ),
            "missing-portraits": str(
                evidence
                / "portrait"
                / "narrative-04-missing-portraits-no-head.output.json"
            ),
            "narration-overlap": str(
                evidence
                / "narrative-05-narration-overlap-no-head.output.json"
            ),
            "show-before": str(
                evidence / "narrative-06-show-before-no-head.output.json"
            ),
            "nested-quotes": str(
                evidence / "narrative-07-nested-quotes-no-head.output.json"
            ),
        }

    def _stage_replacement(self, target: Path, tag: str) -> Path:
        if not target.is_absolute() or not target.is_file():
            raise AssertionError(f"replacement target must exist: {target}")
        staged = self.base / "replacement-staging" / tag / target.name
        staged.parent.mkdir(parents=True, exist_ok=True)
        if target.suffix.lower() == ".exe":
            shutil.copyfile(target, staged)
        else:
            staged.write_bytes(
                target.read_bytes() + b"\n# atomically replaced by fixture\n"
            )
        return staged

    def _stage_identical_replacement(self, target: Path, tag: str) -> Path:
        if not target.is_absolute() or not target.is_file():
            raise AssertionError(f"identity replacement target must exist: {target}")
        staged = self.base / "identity-replacement-staging" / tag / target.name
        staged.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(target, staged)
        self.case.assertEqual(target.read_bytes(), staged.read_bytes())
        return staged

    def _write_control(
        self,
        *,
        documents: dict[str, object] | None,
        raw_documents: dict[str, str] | None,
        exit_codes: dict[int, int] | None,
        precreate_after: dict[int, str] | None,
        replace_required_after: dict[int, Path] | None,
        replace_identity_after: dict[int, Path] | None,
    ) -> None:
        encoded_documents = {
            name: json.dumps(value, separators=(",", ":"), ensure_ascii=False)
            for name, value in (documents or {}).items()
        }
        encoded_documents.update(raw_documents or {})
        precreated: dict[str, str] = {}
        for ordinal, relative in (precreate_after or {}).items():
            candidate = Path(relative)
            if candidate.is_absolute() or any(
                part in ("", ".", "..") for part in candidate.parts
            ):
                raise AssertionError(
                    f"precreate_after must use a plain evidence-relative path: {relative}"
                )
            precreated[str(ordinal)] = str(
                self.run_root / "evidence" / candidate
            )

        replacements: dict[str, list[dict[str, str]]] = {}
        for ordinal, target_value in (replace_required_after or {}).items():
            target = Path(target_value)
            staged = self._stage_replacement(
                target,
                f"required-{ordinal}",
            )
            replacements.setdefault(str(ordinal), []).append(
                {"source": str(staged), "target": str(target)}
            )
        for ordinal, target_value in (replace_identity_after or {}).items():
            target = Path(target_value)
            staged = self._stage_identical_replacement(
                target,
                f"identity-{ordinal}",
            )
            replacements.setdefault(str(ordinal), []).append(
                {"source": str(staged), "target": str(target)}
            )
        control = {
            "raw_documents": encoded_documents,
            "output_paths": self._output_paths(),
            "exit_codes": {
                str(ordinal): int(code)
                for ordinal, code in (exit_codes or {}).items()
            },
            "precreate_after": precreated,
            "replacements_after": replacements,
        }
        self.control_path.write_text(
            json.dumps(control, ensure_ascii=False),
            encoding="utf-8",
        )

    def run(
        self,
        gate: str,
        phase: str = "Final",
        *,
        documents: dict[str, object] | None = None,
        raw_documents: dict[str, str] | None = None,
        exit_codes: dict[int, int] | None = None,
        precreate_after: dict[int, str] | None = None,
        replace_required_after: dict[int, Path] | None = None,
        replace_identity_after: dict[int, Path] | None = None,
        extra_environment: dict[str, str] | None = None,
        close_fds: bool = True,
        tool_timeout_seconds: int = 30,
        wall_timeout_seconds: int = 65,
        gate_cwd: Path | None = None,
    ) -> subprocess.CompletedProcess[str]:
        if self.has_run:
            raise AssertionError("Each fake-project fixture supports one gate run.")
        self.has_run = True
        self._write_control(
            documents=documents,
            raw_documents=raw_documents,
            exit_codes=exit_codes,
            precreate_after=precreate_after,
            replace_required_after=replace_required_after,
            replace_identity_after=replace_identity_after,
        )
        environment = os.environ.copy()
        environment.pop("GIT_COMMIT", None)
        environment.update(
            {
                "APPDATA": str(self.appdata),
                "PATH": str(self.fake_bin)
                + os.pathsep
                + environment.get("PATH", ""),
                "WINTER_GATE_RECORD": str(self.records_path),
                "WINTER_GATE_CONTROL": str(self.control_path),
                "WINTER_GATE_FAKE_PYTHON": str(self.python_exe),
                "WINTER_GATE_FAKE_MODE": "normal",
                "WINTER_GATE_TRUSTED_POWERSHELL": str(POWERSHELL),
            }
        )
        if extra_environment:
            environment.update(extra_environment)
        command = [
            str(POWERSHELL),
            "-NoLogo",
            "-NoProfile",
            "-NonInteractive",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            str(GATE),
            "-Gate",
            gate,
            "-ProjectRoot",
            str(self.root),
            "-RunRoot",
            str(self.run_root),
            "-ToolTimeoutSeconds",
            str(tool_timeout_seconds),
            "-RenPyTimeoutSeconds",
            "300",
        ]
        if gate == "Narrative":
            command.extend(["-NarrativePhase", phase])
        completed = subprocess.run(
            command,
            cwd=gate_cwd or self.root,
            env=environment,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=wall_timeout_seconds,
            check=False,
            close_fds=close_fds,
        )
        control_errors = [
            str(record["control_error"])
            for record in self.records()
            if record.get("control_error")
        ]
        if control_errors:
            raise AssertionError("; ".join(control_errors))
        return completed

    def start_async(
        self,
        *,
        extra_environment: dict[str, str] | None = None,
    ) -> subprocess.Popen[str]:
        if self.has_run:
            raise AssertionError("Each fake-project fixture supports one gate run.")
        self.has_run = True
        self._write_control(
            documents=None,
            raw_documents=None,
            exit_codes=None,
            precreate_after=None,
            replace_required_after=None,
            replace_identity_after=None,
        )
        environment = os.environ.copy()
        environment.pop("GIT_COMMIT", None)
        environment.update(
            {
                "APPDATA": str(self.appdata),
                "PATH": str(self.fake_bin)
                + os.pathsep
                + environment.get("PATH", ""),
                "WINTER_GATE_RECORD": str(self.records_path),
                "WINTER_GATE_CONTROL": str(self.control_path),
                "WINTER_GATE_FAKE_PYTHON": str(self.python_exe),
                "WINTER_GATE_FAKE_MODE": "normal",
                "WINTER_GATE_TRUSTED_POWERSHELL": str(POWERSHELL),
            }
        )
        if extra_environment:
            environment.update(extra_environment)
        return subprocess.Popen(
            [
                str(POWERSHELL),
                "-NoLogo",
                "-NoProfile",
                "-NonInteractive",
                "-ExecutionPolicy",
                "Bypass",
                "-File",
                str(GATE),
                "-Gate",
                "Structural",
                "-ProjectRoot",
                str(self.root),
                "-RunRoot",
                str(self.run_root),
                "-ToolTimeoutSeconds",
                "30",
                "-RenPyTimeoutSeconds",
                "300",
            ],
            cwd=self.root,
            env=environment,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            close_fds=True,
        )

    def start_writer_race(
        self,
        ready_path: Path,
        release_path: Path,
    ) -> subprocess.Popen[str]:
        if self.has_run:
            raise AssertionError("Each fake-project fixture supports one gate run.")
        self.has_run = True
        self._write_control(
            documents=None,
            raw_documents=None,
            exit_codes=None,
            precreate_after=None,
            replace_required_after=None,
            replace_identity_after=None,
        )
        environment = os.environ.copy()
        environment.pop("GIT_COMMIT", None)
        environment.update(
            {
                "APPDATA": str(self.appdata),
                "PATH": str(self.fake_bin)
                + os.pathsep
                + environment.get("PATH", ""),
                "WINTER_GATE_RECORD": str(self.records_path),
                "WINTER_GATE_CONTROL": str(self.control_path),
                "WINTER_GATE_FAKE_PYTHON": str(self.python_exe),
                "WINTER_GATE_FAKE_MODE": "writer-race",
                "WINTER_GATE_TRUSTED_POWERSHELL": str(POWERSHELL),
                "WINTER_GATE_WRITER_RACE_READY": str(ready_path),
                "WINTER_GATE_WRITER_RACE_RELEASE": str(release_path),
            }
        )
        return subprocess.Popen(
            [
                str(POWERSHELL),
                "-NoLogo",
                "-NoProfile",
                "-NonInteractive",
                "-ExecutionPolicy",
                "Bypass",
                "-File",
                str(GATE),
                "-Gate",
                "Structural",
                "-ProjectRoot",
                str(self.root),
                "-RunRoot",
                str(self.run_root),
                "-ToolTimeoutSeconds",
                "30",
                "-RenPyTimeoutSeconds",
                "300",
            ],
            cwd=self.root,
            env=environment,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            close_fds=True,
        )

    def records(self) -> list[dict[str, object]]:
        return read_json_lines(self.records_path)

    def summary(self) -> dict[str, object]:
        path = self.run_root / "evidence" / "gate-summary.json"
        self.case.assertTrue(path.is_file(), path)
        return json.loads(path.read_text(encoding="utf-8-sig"))

    def result(self, ordinal: int) -> dict[str, object]:
        step = self.summary()["steps"][ordinal - 1]
        path = evidence_file(self.run_root, step["result"])
        return json.loads(path.read_text(encoding="utf-8-sig"))

    def output_path(self, step_name: str) -> Path:
        return Path(self._output_paths()[step_name])


class _GateBlackBoxCase(unittest.TestCase):
    def make_project(self) -> _GateFixture:
        return _GateFixture(self)


# END LOOP 3.3-T2 SHARED BLACK-BOX FIXTURE SUPPORT


class WinterInterludeGateNativeFoundationTests(unittest.TestCase):
    def test_exact_native_readable_identity_rejects_parent_junction(self) -> None:
        with tempfile.TemporaryDirectory(
            prefix="winter-gate-native-readable-"
        ) as temporary:
            base = Path(temporary)
            probe = compile_native_readable_probe(
                base / "build",
                extract_native_source(),
            )
            ordinary = base / "ordinary.txt"
            ordinary.write_text("ordinary", encoding="utf-8")
            accepted = subprocess.run(
                [str(probe), str(ordinary)],
                cwd=base,
                stdin=subprocess.DEVNULL,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=30,
                check=False,
            )
            self.assertEqual(0, accepted.returncode, accepted.stderr)

            outside = base / "outside"
            outside.mkdir()
            routed_file = outside / "routed.txt"
            routed_file.write_text("routed", encoding="utf-8")
            junction = base / "junction-parent"
            create_junction(junction, outside)
            try:
                rejected = subprocess.run(
                    [str(probe), str(junction / routed_file.name)],
                    cwd=base,
                    stdin=subprocess.DEVNULL,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    encoding="utf-8",
                    errors="replace",
                    timeout=30,
                    check=False,
                )
                self.assertEqual(91, rejected.returncode, rejected.stdout)
                self.assertRegex(
                    rejected.stderr,
                    r"(?i)path identity|reparse",
                )
            finally:
                os.rmdir(junction)


class WinterInterludeGateNativeWriterTests(unittest.TestCase):
    def test_exact_native_writer_and_instrumented_share_contracts(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory(
            prefix="winter-gate-native-writer-"
        ) as temporary:
            base = Path(temporary)
            native_source = extract_native_source()
            run_exact_native_writer_smoke(
                self,
                base / "exact-source-smoke",
                native_source,
            )
            assert_native_writer_lifecycle(self, native_source)
            self.assertEqual(
                native_source,
                restore_native_writer_pause(
                    instrument_native_writer_pause(native_source)
                ),
            )
            contracts = {
                ("production", "result"): (0, ("owned-fixed",), None),
                ("production", "summary"): (0, ("owned-fixed",), None),
                ("delete-share-mutant", "result"): (
                    0,
                    ("owned-raced",),
                    None,
                ),
                ("delete-share-mutant", "summary"): (
                    92,
                    ("owned-raced",),
                    r"(?i)UNEXPECTED_FAILURE:.*"
                    r"SetFileInformationByHandle\(publish owned summary\).*"
                    r"Win32 error 3",
                ),
            }
            for source_name in ("production", "delete-share-mutant"):
                for mode in ("result", "summary"):
                    source = native_source
                    if source_name == "delete-share-mutant":
                        source = mutate_native_writer_delete_sharing(
                            native_source,
                            mode,
                        )
                    with self.subTest(mode=mode, source=source_name):
                        observed = run_native_writer_lock_probe(
                            self,
                            base / source_name,
                            source,
                            mode,
                        )
                        self.assertEqual(0, observed.barrier_leaf_size)
                        self.assertIs(
                            source_name == "delete-share-mutant",
                            observed.leaf_renamed,
                        )
                        if observed.leaf_renamed:
                            self.assertIsNone(observed.leaf_rename_error)
                        else:
                            self.assertIn(
                                observed.leaf_rename_error,
                                (5, 32, 33),
                            )
                        self.assertIs(
                            source_name == "delete-share-mutant",
                            observed.directory_renamed,
                            observed.directory_move_stdout
                            + observed.directory_move_stderr,
                        )
                        if observed.directory_renamed:
                            self.assertEqual(
                                0,
                                observed.directory_move_returncode,
                            )
                        else:
                            self.assertNotEqual(
                                0,
                                observed.directory_move_returncode,
                            )
                        self.assertTrue(
                            observed.post_close_directory_renamed
                        )
                        self.assertEqual(
                            0,
                            observed.post_close_directory_move_returncode,
                        )

                        expected_rc, expected_placements, error_pattern = contracts[
                            (source_name, mode)
                        ]
                        self.assertEqual(
                            expected_rc,
                            observed.returncode,
                            observed.stdout + observed.stderr,
                        )
                        self.assertEqual(
                            expected_placements,
                            observed.complete_json_placements,
                        )
                        self.assertEqual((), observed.zero_byte_placements)
                        if error_pattern is None:
                            self.assertEqual("", observed.stderr)
                        else:
                            self.assertRegex(observed.stderr, error_pattern)

                        if source_name == "production":
                            self.assertEqual(
                                "owned-fixed",
                                observed.honest_placement,
                            )
                        else:
                            self.assertIsNone(observed.honest_placement)
```

Inside `WinterInterludeGateBootstrapTests`, replace the complete Task 2 method
`test_valid_call_reaches_the_named_process_boundary_after_path_bootstrap` with
this Task 3 boundary. This is a temporary, honest failure boundary: the real
source child passes, while the not-yet-installed Structural manifest is itself
reported as validation failure. Task 4 deletes this method when it removes the
matching production forced-validation block.

```python
    def test_valid_call_reaches_source_bridge_with_honest_validation_summary(
        self,
    ) -> None:
        fixture = _GateFixture(self)
        self.addCleanup(fixture.close)

        completed = fixture.run("Structural")

        self.assertEqual(1, completed.returncode, completed.stderr)
        self.assertIn(
            "structural manifest layer not implemented",
            completed.stderr,
        )
        records = fixture.records()
        self.assertEqual(1, len(records))
        self.assertEqual("source-contract", records[0]["step"])
        summary = fixture.summary()
        self.assertEqual("failed", summary["status"])
        self.assertEqual("validation", summary["failure_kind"])
        self.assertEqual(
            "structural manifest layer not implemented",
            summary["error"],
        )
        self.assertEqual(1, len(summary["steps"]))
        source_step = summary["steps"][0]
        self.assertEqual("source-contract", source_step["name"])
        self.assertEqual("passed", source_step["status"])
        self.assertIsNone(source_step["failure_kind"])
        self.assertIsNone(source_step["error"])
        self.assertEqual(source_step, fixture.result(1))

```

Add this complete test class. It assumes the file-level `GATE`, `POWERSHELL`,
`STRUCTURAL_SUITES`, and `trusted_system_directory()` definitions from Task 1.

```python
class WinterInterludeGateProcessTests(_GateBlackBoxCase):
    maxDiff = None

    def setUp(self) -> None:
        self.fixture = self.make_project()
        self.addCleanup(self.fixture.close)
        self.base = self.fixture.base
        self.project = self.fixture.root
        self.tools = self.fixture.tools
        self.fake_bin = self.fixture.fake_bin
        self.fake_python = self.fixture.python_exe
        self.record = self.fixture.records_path
        self.appdata = self.fixture.appdata
        self.run_parent = self.fixture.run_parent

    def new_run_root(self) -> Path:
        self.assertFalse(self.fixture.run_root.exists())
        return self.fixture.run_root

    def invoke(
        self,
        run_root: Path,
        *,
        extra_environment: dict[str, str] | None = None,
        close_fds: bool = True,
        tool_timeout_seconds: int = 30,
        wall_timeout_seconds: int = 65,
    ) -> subprocess.CompletedProcess[str]:
        self.assertEqual(self.fixture.run_root, run_root)
        return self.fixture.run(
            "Structural",
            extra_environment=extra_environment,
            close_fds=close_fds,
            tool_timeout_seconds=tool_timeout_seconds,
            wall_timeout_seconds=wall_timeout_seconds,
        )

    def load_summary(self, run_root: Path) -> dict[str, object]:
        self.assertEqual(self.fixture.run_root, run_root)
        return self.fixture.summary()

    def test_json_evidence_writer_is_native_guarded_create_new(self) -> None:
        source = GATE.read_text(encoding="utf-8")
        self.assertEqual(
            1,
            source.count("public static void WriteUtf8JsonCreateNew("),
        )
        self.assertEqual(
            1,
            source.count("public static string WriteOwnedSummaryUtf8Json("),
        )
        engine = source[
            source.index("// BEGIN PROCESS ENGINE") :
            source.index("// END PROCESS ENGINE")
        ]
        native_start = source.index(
            "public static void WriteUtf8JsonCreateNew("
        )
        native_end = source.index(
            "public static BoundedProcessResult RunProcessTree(",
            native_start,
        )
        native_writer = source[native_start:native_end]
        for required in (
            "OpenVerifiedEvidenceGuard(",
            "CreateNew,",
            "RequireDirectEvidenceChild(",
            "WriteAllAndFlush(",
            "finally",
        ):
            self.assertIn(required, native_writer)
        self.assertLess(
            native_writer.index("OpenVerifiedEvidenceGuard("),
            native_writer.index("CreateNew,"),
        )
        self.assertLess(
            native_writer.index("RequireDirectEvidenceChild("),
            native_writer.index("WriteAllAndFlush("),
        )
        for helper_contract in (
            "new UTF8Encoding(false, true)",
            "FileFlagOpenReparsePoint",
            "FileShareRead | FileShareWrite",
            "SameStablePath(",
            "Path.GetInvalidFileNameChars()",
            "WriteFile(",
            "FlushFileBuffers(",
        ):
            self.assertIn(helper_contract, engine)
        self.assertLess(
            engine.index("WriteFile("),
            engine.index("FlushFileBuffers("),
        )

        owned_start = source.index(
            "public static string WriteOwnedSummaryUtf8Json("
        )
        owned_writer = source[owned_start:native_start]
        for ownership_contract in (
            "gate-summary.pending.",
            "gate-summary.unowned.",
            "GenericWrite | DeleteAccess",
            "CreateNew,",
            "WriteAllAndFlush(",
            "RenameOpenFileNoReplace(",
            "OpenPlainDirectEvidenceFile(",
            "SameObject(",
            "SameStablePath(",
        ):
            self.assertIn(ownership_contract, owned_writer)
        self.assertNotIn("ReplaceIfExists", owned_writer)
        self.assertNotIn("FileShareDelete", owned_writer)

        verified_read_start = source.index(
            "public static string ReadVerifiedUtf8TextFile("
        )
        verified_read_end = source.index(
            "public static string WriteOwnedSummaryUtf8Json(",
            verified_read_start,
        )
        verified_read = source[verified_read_start:verified_read_end]
        self.assertIn("FileShareRead,", verified_read)
        self.assertNotIn("FileShareWrite", verified_read)
        self.assertNotIn("FileShareDelete", verified_read)

        power_shell_start = source.index("function Write-GateEvidenceJson {")
        power_shell_end = source.index(
            "function New-ValidationGateResult {",
            power_shell_start,
        )
        power_shell_writer = source[power_shell_start:power_shell_end]
        self.assertIn(
            "[WinterGate.Native]::WriteUtf8JsonCreateNew(",
            power_shell_writer,
        )
        self.assertNotIn("[IO.File]::Open(", power_shell_writer)
        self.assertNotIn("[IO.StreamWriter]", power_shell_writer)
        self.assertIn(
            "[WinterGate.Native]::WriteOwnedSummaryUtf8Json(",
            source,
        )

        identity_start = source.index(
            "function Assert-RunTreeDirectoryIdentities {"
        )
        identity_end = source.index(
            "function Get-IdentityEvidenceObject {",
            identity_start,
        )
        identity_guards = source[identity_start:identity_end]
        self.assertEqual(
            identity_guards.count(
                "foreach ($identity in $script:GateDirectoryIdentities)"
            ),
            2,
        )
        self.assertIn("Assert-RunTreeDirectoryIdentities", identity_guards)
        self.assertIn("Assert-GatePathState", identity_guards)
        self.assertNotIn("Test-SameOrChildFinalPath", identity_guards)
        self.assertIn("Out-Null", identity_guards)
        non_evidence_start = identity_guards.index(
            "function Assert-NonEvidenceGateDirectoryIdentities {"
        )
        non_evidence = identity_guards[non_evidence_start:]
        skip_start = non_evidence.index("        if (")
        skip_end = non_evidence.index(
            "        Assert-GatePathState",
            skip_start,
        )
        skip_branch = non_evidence[skip_start:skip_end].strip()
        self.assertEqual(
            "\n".join(
                (
                    "if ([WinterGate.Native]::SameObject(",
                    "            $identity,",
                    "            $script:EvidenceIdentity)) {",
                    "            continue",
                    "        }",
                )
            ),
            skip_branch,
        )

        observe_start = engine.index(
            "private static bool ObserveRootAccountingExit("
        )
        observe_end = engine.index(
            "private static bool TryGetJobProcessIds(",
            observe_start,
        )
        observe = engine[observe_start:observe_end]
        self.assertIn("TryGetActiveProcessCount(", observe)
        self.assertIn("if (activeProcesses == 0)", observe)
        self.assertLess(
            observe.index("if (activeProcesses == 0)"),
            observe.rindex("return true;"),
        )

        invoke_start = source.index("function Invoke-GateStep {")
        invoke_end = source.index("function Invoke-WinterInterludeGate {", invoke_start)
        invoke_step = source[invoke_start:invoke_end]
        undrained = "if ($process.ProcessStarted -and -not $process.TreeDrained)"
        self.assertIn(undrained, invoke_step)
        undrained_start = invoke_step.index(undrained)
        publication_start = invoke_step.index(
            "Write-GateEvidenceJson -Path $resultPath",
            undrained_start,
        )
        undrained_branch = invoke_step[undrained_start:publication_start]
        self.assertIn("$script:EvidencePublicationSafe = $false", undrained_branch)
        self.assertIn("throw [InvalidOperationException]::new(", undrained_branch)
        self.assertNotIn("Write-GateEvidenceJson", undrained_branch)
        post_process = invoke_step[
            invoke_step.index("$unownedSummaryDetected =", undrained_start) :
            publication_start
        ]
        self.assertIn("Assert-NonEvidenceGateDirectoryIdentities", post_process)
        self.assertNotIn("Assert-AllGateDirectoryIdentities", post_process)

        readable_start = engine.index(
            "private static PathIdentity GetReadableFileIdentityCore("
        )
        readable_end = engine.index(
            "private static void ValidateJsonPath(",
            readable_start,
        )
        readable = engine[readable_start:readable_end]
        self.assertIn(
            "TryGetPathIdentity(path, PathKind.File, true)",
            readable,
        )
        self.assertIn(
            "GetPathIdentity(path, PathKind.File, true)",
            readable,
        )
        self.assertIn("SameStablePath(chainIdentity, identity)", readable)

        per_worktree_start = source.index(
            "function Test-GitPerWorktreeReference {"
        )
        per_worktree_end = source.index(
            "function Read-GitLooseReference {",
            per_worktree_start,
        )
        per_worktree = source[per_worktree_start:per_worktree_end]
        for prefix in (
            "refs/bisect/",
            "refs/rewritten/",
            "refs/worktree/",
        ):
            self.assertIn(prefix, per_worktree)
        head_start = source.index("function Get-ProjectHeadState {")
        head_end = source.index(
            "function Assert-GitCommitOverride {",
            head_start,
        )
        head_reader = source[head_start:head_end]
        self.assertIn(
            "-not (Test-GitPerWorktreeReference $reference)",
            head_reader,
        )

        project_guard_start = source.index("function Assert-ProjectRootIdentity {")
        project_guard_end = source.index(
            "function Assert-RunTreeDirectoryIdentities {",
            project_guard_start,
        )
        self.assertIn(
            "-ExpectedIdentity $script:ProjectIdentity",
            source[project_guard_start:project_guard_end],
        )
        dependency_start = source.index(
            "function Get-GateStepDependencyValidationError {"
        )
        dependency_end = source.index("function Invoke-GateStep {", dependency_start)
        dependency = source[dependency_start:dependency_end]
        self.assertIn("ExecutableIdentity", dependency)
        self.assertIn("RequiredFileIdentities", dependency)
        self.assertGreaterEqual(
            invoke_step.count("Get-GateStepDependencyValidationError $Step"),
            2,
        )

    def assert_output_evidence_handles_remain_pinned_through_validation(
        self,
    ) -> None:
        source = GATE.read_text(encoding="utf-8")
        engine = source[
            source.index("// BEGIN PROCESS ENGINE") :
            source.index("// END PROCESS ENGINE")
        ]
        self.assertIn("public bool OutputEvidenceValid;", source)
        self.assertIn("public string OutputEvidenceError;", source)
        result_initialization = engine[
            engine.index("BoundedProcessResult result =") :
            engine.index("IntPtr stdoutHandle = InvalidHandleValue;")
        ]
        self.assertIn(
            "result.OutputEvidenceValid = false;",
            result_initialization,
        )
        self.assertNotIn(
            "result.OutputEvidenceValid = true;",
            result_initialization,
        )
        resumed = engine[
            engine.index("uint previousSuspendCount = ResumeThread(") :
            engine.index("uint waitResult = WaitForSingleObject(")
        ]
        self.assertIn("ReleaseProcessStartResources(", resumed)
        self.assertNotIn("ref stdoutHandle", resumed)
        self.assertNotIn("ref stderrHandle", resumed)
        launch = engine[
            engine.index("stdoutHandle = CreateFileW(") :
            engine.index('string jobName = @"Local\\WinterGate-"')
        ]
        self.assertLess(
            launch.index("stdoutHandle = CreateFileW("),
            launch.index("stderrHandle = CreateFileW("),
        )
        validation = engine[
            engine.index("private static void ValidateOutputEvidenceBeforeClose(") :
            engine.index("private static void ReleaseProcessStartResources(")
        ]
        self.assertGreaterEqual(
            validation.count("GetPathIdentityFromOpenHandle("),
            1,
        )
        self.assertIn("CreateFileW(", validation)
        self.assertIn("RequireDirectEvidenceChild(", validation)
        self.assertGreaterEqual(validation.count("SameStablePath("), 2)
        finalizer = engine[
            engine.index("finally\n        {", engine.index("RunProcessTree(")) :
            engine.index("internal static string EncodeWindowsCommandLineArgument(")
        ]
        self.assertLess(
            finalizer.index("ValidateOutputEvidenceBeforeClose("),
            finalizer.index("ReleaseLaunchResources("),
        )
        self.assertIn("(!processCreated || result.TreeDrained)", finalizer)
        self.assertIn(
            "result.OutputEvidenceValid = errors.Count == 0;",
            validation,
        )
        bridge = source[
            source.index("function Invoke-GateStep {") :
            source.index("function Invoke-WinterInterludeGate {")
        ]
        process_start_failure = bridge.index(
            "elseif (-not $process.ProcessStarted)"
        )
        output_validation = bridge.index(
            "elseif ($process.ProcessStarted -and\n"
            "            -not [bool]$process.OutputEvidenceValid)"
        )
        self.assertLess(process_start_failure, output_validation)
        self.assertLess(output_validation, bridge.index("$process.TimedOut"))
        self.assertIn(
            "$outputEvidenceTrusted = [bool]$process.OutputEvidenceValid",
            bridge,
        )
        self.assertIn("stdout = if ($outputEvidenceTrusted)", bridge)
        self.assertIn("stderr = if ($outputEvidenceTrusted)", bridge)

    def test_public_json_create_new_never_overwrites_existing_leaf(self) -> None:
        result_name = "structural-01-source-contract-no-head.result.json"
        completed = self.fixture.run(
            "Structural",
            precreate_after={1: result_name},
        )

        self.assertEqual(1, completed.returncode, completed.stderr)
        self.assertEqual(1, len(self.fixture.records()))
        precreated = self.fixture.run_root / "evidence" / result_name
        self.assertEqual(b"precreated-by-fixture\n", precreated.read_bytes())
        summary = self.fixture.summary()
        self.assertEqual("failed", summary["status"])
        self.assertEqual("validation", summary["failure_kind"])
        self.assertRegex(
            summary["error"],
            r"(?i)CreateFileW\(JSON create-new\)|already exists|error 80",
        )
        self.assertEqual([], summary["steps"])

    def test_public_prewrite_identity_check_rejects_concurrent_evidence_rename(
        self,
    ) -> None:
        ready = self.base / "writer-race-ready"
        release = self.base / "writer-race-release"
        process = self.fixture.start_writer_race(ready, release)
        self.addCleanup(lambda: process.poll() is None and process.kill())
        deadline = time.monotonic() + 15
        while not ready.exists() and time.monotonic() < deadline:
            time.sleep(0.01)
        self.assertTrue(ready.is_file(), "source child did not reach writer race")

        evidence = self.fixture.run_root / "evidence"
        original = self.fixture.run_root / "evidence-writer-race-original"
        oplock = _DirectoryReadHandleOplock(evidence)
        self.addCleanup(oplock.close)
        release.write_text("release", encoding="utf-8")
        oplock.wait_for_break()
        try:
            oplock.rename_to(original)
        finally:
            oplock.release()

        stdout, stderr = process.communicate(timeout=30)
        self.assertNotEqual(0, process.returncode, stdout)
        self.assertRegex(stderr, r"(?i)path identity")
        self.assertEqual(1, len(self.fixture.records()))
        self.assertTrue(original.is_dir(), original)
        self.assertEqual([], list(original.glob("*.result.json")))
        self.assertFalse((original / "gate-summary.json").exists())
        self.assertFalse(evidence.exists(), evidence)

    def test_child_cannot_impersonate_the_gate_owned_summary(self) -> None:
        completed = self.fixture.run(
            "Structural",
            precreate_after={1: "gate-summary.json"},
        )

        self.assertEqual(1, completed.returncode, completed.stderr)
        records = self.fixture.records()
        self.assertEqual(1, len(records))
        self.assertEqual("source-contract", records[0]["step"])
        summary = self.fixture.summary()
        self.assertEqual("failed", summary["status"])
        self.assertEqual("validation", summary["failure_kind"])
        self.assertIn("Unowned gate-summary.json", summary["error"])
        self.assertEqual(1, len(summary["steps"]))
        source_result = summary["steps"][0]
        self.assertEqual("failed", source_result["status"])
        self.assertEqual("validation", source_result["failure_kind"])
        self.assertIs(True, source_result["process_started"])
        self.assertEqual(0, source_result["exit_code"])
        self.assertIs(True, source_result["tree_drained"])

        quarantine = list(
            (self.fixture.run_root / "evidence").glob(
                "gate-summary.unowned.*.json"
            )
        )
        self.assertEqual(1, len(quarantine))
        self.assertEqual(b"precreated-by-fixture\n", quarantine[0].read_bytes())
        self.assertNotEqual(
            b"precreated-by-fixture\n",
            (self.fixture.run_root / "evidence" / "gate-summary.json").read_bytes(),
        )

    def test_child_evidence_swap_keeps_streams_in_original_and_stops_writes(
        self,
    ) -> None:
        run_root = self.new_run_root()
        evidence = run_root / "evidence"
        evidence_old = run_root / "evidence-original"
        swap_target = self.base / "empty-swap-target"
        swap_target.mkdir()

        completed = self.invoke(
            run_root,
            extra_environment={
                "WINTER_GATE_FAKE_MODE": "swap-evidence",
                "WINTER_GATE_EVIDENCE_DIR": str(evidence),
                "WINTER_GATE_EVIDENCE_OLD": str(evidence_old),
                "WINTER_GATE_SWAP_TARGET": str(swap_target),
            },
        )

        self.assertNotEqual(0, completed.returncode)
        self.assertRegex(completed.stderr, r"(?i)path identity")
        records = read_json_lines(self.record)
        self.assertEqual(1, len(records))
        self.assertIs(True, records[0]["swapped_evidence"])
        self.assertTrue(evidence.is_dir())
        self.assertTrue(evidence_old.is_dir())
        self.addCleanup(os.rmdir, evidence)
        stdout_files = list(evidence_old.glob("*.stdout.txt"))
        stderr_files = list(evidence_old.glob("*.stderr.txt"))
        self.assertEqual(1, len(stdout_files))
        self.assertEqual(1, len(stderr_files))
        self.assertIn(
            "fake-python-stdout",
            stdout_files[0].read_text(encoding="utf-8-sig"),
        )
        self.assertIn(
            "fake-python-stderr",
            stderr_files[0].read_text(encoding="utf-8-sig"),
        )
        self.assertEqual([], list(evidence_old.glob("*.result.json")))
        self.assertFalse((evidence_old / "gate-summary.json").exists())
        self.assertEqual([], list(swap_target.iterdir()))

    def test_child_output_leaf_replacement_is_rejected_as_validation(
        self,
    ) -> None:
        self.assert_output_evidence_handles_remain_pinned_through_validation()
        completed = self.fixture.run(
            "Structural",
            extra_environment={"WINTER_GATE_FAKE_MODE": "swap-output-leaves"},
        )

        self.assertEqual(1, completed.returncode, completed.stderr)
        records = self.fixture.records()
        self.assertEqual(1, len(records))
        self.assertIs(True, records[0]["swapped_output_leaves"])
        evidence = self.fixture.run_root / "evidence"
        fixed_stdout = list(evidence.glob("*.stdout.txt"))
        fixed_stderr = list(evidence.glob("*.stderr.txt"))
        moved_stdout = list(evidence.glob("*.stdout.txt.moved"))
        moved_stderr = list(evidence.glob("*.stderr.txt.moved"))
        self.assertEqual(1, len(fixed_stdout))
        self.assertEqual(1, len(fixed_stderr))
        self.assertEqual(1, len(moved_stdout))
        self.assertEqual(1, len(moved_stderr))
        diagnostic = {
            "fixed_stdout": fixed_stdout[0].read_text(encoding="utf-8-sig"),
            "fixed_stderr": fixed_stderr[0].read_text(encoding="utf-8-sig"),
            "moved_stdout": moved_stdout[0].read_text(encoding="utf-8-sig"),
            "moved_stderr": moved_stderr[0].read_text(encoding="utf-8-sig"),
        }
        result = self.fixture.result(1)
        diagnostic["result"] = result
        self.assertEqual("failed", result["status"], diagnostic)
        self.assertEqual("validation", result["failure_kind"], diagnostic)
        self.assertRegex(result["error"], r"(?i)output evidence.*identity")
        self.assertIsNone(result["stdout"], diagnostic)
        self.assertIsNone(result["stderr"], diagnostic)
        self.assertEqual("FORGED-STDOUT\n", diagnostic["fixed_stdout"])
        self.assertEqual("FORGED-STDERR\n", diagnostic["fixed_stderr"])
        self.assertIn("fake-python-stdout", diagnostic["moved_stdout"])
        self.assertIn("fake-python-stderr", diagnostic["moved_stderr"])

    def test_partial_output_setup_never_trusts_single_owned_leaf(self) -> None:
        executable_oplock = _FileReadHandleOplock(self.fake_python)
        self.addCleanup(executable_oplock.close)
        process = self.fixture.start_async()

        def stop_process() -> None:
            if process.poll() is None:
                process.kill()
            process.communicate(timeout=10)

        self.addCleanup(stop_process)
        executable_oplock.wait_for_break()
        evidence = self.fixture.run_root / "evidence"
        self.assertTrue(evidence.is_dir(), evidence)
        output_oplock = _SharedDirectoryMutationOplock(evidence)
        self.addCleanup(output_oplock.close)
        executable_oplock.release()
        output_oplock.wait_for_break()

        stdout_path = (
            evidence / "structural-01-source-contract-no-head.stdout.txt"
        )
        stderr_path = (
            evidence / "structural-01-source-contract-no-head.stderr.txt"
        )
        with stderr_path.open("xb") as stream:
            stream.write(b"UNOWNED-STDERR\n")
        output_oplock.release()

        gate_stdout, gate_stderr = process.communicate(timeout=30)
        self.assertEqual(1, process.returncode, gate_stdout + gate_stderr)
        self.assertTrue(stdout_path.is_file(), stdout_path)
        self.assertEqual(b"", stdout_path.read_bytes())
        self.assertEqual(b"UNOWNED-STDERR\n", stderr_path.read_bytes())
        self.assertEqual([], self.fixture.records())
        summary = self.fixture.summary()
        self.assertEqual("failed", summary["status"])
        self.assertEqual("process", summary["failure_kind"])
        self.assertEqual(1, len(summary["steps"]))
        summary_step = summary["steps"][0]
        result_path = evidence_file(self.fixture.run_root, summary_step["result"])
        result = json.loads(result_path.read_text(encoding="utf-8-sig"))
        diagnostic = {"summary_step": summary_step, "result": result}
        for document in (summary_step, result):
            self.assertIs(False, document["process_started"], diagnostic)
            self.assertEqual("failed", document["status"], diagnostic)
            self.assertEqual("process", document["failure_kind"], diagnostic)
            self.assertRegex(
                document["error"],
                r"(?i)CreateFileW\(stderr\)|already exists|error (?:80|183)",
            )
            self.assertIsNone(document["stdout"], diagnostic)
            self.assertIsNone(document["stderr"], diagnostic)

    def test_python_timeout_kills_root_and_grandchild(self) -> None:
        run_root = self.new_run_root()

        started = time.monotonic()
        completed = self.invoke(
            run_root,
            extra_environment={"WINTER_GATE_FAKE_MODE": "timeout-tree"},
            tool_timeout_seconds=30,
            wall_timeout_seconds=60,
        )
        wall_elapsed = time.monotonic() - started

        self.assertNotEqual(0, completed.returncode)
        self.assertGreaterEqual(wall_elapsed, 29.0)
        self.assertLess(wall_elapsed, 55.0)
        records = read_json_lines(self.record)
        self.assertEqual(1, len(records))
        root_pid = int(records[0]["pid"])
        child_pid = int(records[0]["child_pid"])
        assert_processes_exit(self, root_pid, child_pid)

        summary = self.load_summary(run_root)
        self.assertEqual("timeout", summary["failure_kind"])
        self.assertEqual(1, len(summary["steps"]))
        result = summary["steps"][0]
        self.assertIs(True, result["process_started"])
        self.assertEqual(root_pid, result["process_id"])
        self.assertIsInstance(result["started_utc"], str)
        self.assertIsInstance(result["ended_utc"], str)
        self.assertIsInstance(result["elapsed_milliseconds"], int)
        self.assertIsInstance(result["exit_code"], int)
        self.assertIs(True, result["timed_out"])
        self.assertIs(True, result["tree_drained"])
        self.assertIs(False, result["had_live_descendants_after_root_exit"])
        self.assertEqual("failed", result["status"])
        self.assertEqual("timeout", result["failure_kind"])

    def test_normal_root_exit_with_live_grandchild_is_bounded(self) -> None:
        run_root = self.new_run_root()

        completed = self.invoke(
            run_root,
            extra_environment={"WINTER_GATE_FAKE_MODE": "leak-tree"},
        )

        self.assertNotEqual(0, completed.returncode)
        records = read_json_lines(self.record)
        self.assertEqual(1, len(records))
        root_pid = int(records[0]["pid"])
        child_pid = int(records[0]["child_pid"])
        assert_processes_exit(self, root_pid, child_pid)

        summary = self.load_summary(run_root)
        self.assertEqual("process_tree", summary["failure_kind"])
        self.assertEqual(1, len(summary["steps"]))
        result = summary["steps"][0]
        self.assertIs(True, result["process_started"])
        self.assertEqual(root_pid, result["process_id"])
        self.assertIs(False, result["timed_out"])
        self.assertIs(True, result["tree_drained"])
        self.assertIs(True, result["had_live_descendants_after_root_exit"])
        self.assertEqual("failed", result["status"])
        self.assertEqual("process_tree", result["failure_kind"])

    def test_required_file_parent_junction_is_rejected_before_launch(self) -> None:
        routed_tools = self.base / "outside-project-tools"
        os.replace(self.tools, routed_tools)
        create_junction(self.tools, routed_tools)
        self.fixture.register_junction(self.tools)

        completed = self.fixture.run("Structural")

        self.assertEqual(1, completed.returncode, completed.stderr)
        self.assertEqual([], self.fixture.records())
        summary = self.fixture.summary()
        self.assertEqual("failed", summary["status"])
        self.assertEqual("validation", summary["failure_kind"])
        self.assertRegex(summary["error"], r"(?i)path identity|reparse")

    def test_executable_parent_junction_is_rejected_before_launch(self) -> None:
        routed_bin = self.base / "outside-executable-bin"
        os.replace(self.fake_bin, routed_bin)
        create_junction(self.fake_bin, routed_bin)
        self.fixture.register_junction(self.fake_bin)

        completed = self.fixture.run("Structural")

        self.assertNotEqual(0, completed.returncode, completed.stderr)
        self.assertEqual([], self.fixture.records())
        self.assertRegex(completed.stderr, r"(?i)path identity|reparse")
        evidence = self.fixture.run_root / "evidence"
        self.assertEqual([], list(evidence.glob("*.result.json")))
        self.assertEqual([], list(evidence.glob("*.stdout.txt")))
        self.assertEqual([], list(evidence.glob("*.stderr.txt")))
        self.assertTrue(
            (evidence / "gate-summary.json").is_file(),
            "safe RunRoot did not publish gate-summary.json",
        )
        summary = self.fixture.summary()
        self.assertEqual(1, summary["schema_version"])
        self.assertEqual("failed", summary["status"])
        self.assertEqual("validation", summary["failure_kind"])
        self.assertRegex(summary["error"], r"(?i)path identity|reparse")
        self.assertEqual("no-head", summary["head_token"])
        self.assertEqual([], summary["steps"])

    def test_executable_identity_uses_readable_full_chain_api(self) -> None:
        source = GATE.read_text(encoding="utf-8")
        regions = (
            source[
                source.index("function Resolve-PythonExecutable {") :
                source.index("function Get-ExpectedProjectFilePath {")
            ],
            source[
                source.index("function New-GateStep {") :
                source.index("function Get-StructuralGateManifest {")
            ],
            source[
                source.index("function Get-GateStepDependencyValidationError {") :
                source.index("function Invoke-GateStep {")
            ],
        )
        for region in regions:
            self.assertIn(
                "[WinterGate.Native]::GetReadableFileIdentity(",
                region,
            )
            self.assertNotIn("[WinterGate.Native]::GetPathIdentity(", region)

    def test_executable_requires_generic_read_before_launch(self) -> None:
        deny_read_extended_attributes(self.fake_python)
        probe = compile_native_executable_access_probe(
            self.base / "native-executable-access",
            extract_native_source(),
        )
        path_identity = subprocess.run(
            [str(probe), "path", str(self.fake_python)],
            cwd=self.base,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=30,
            check=False,
        )
        self.assertEqual(0, path_identity.returncode, path_identity.stderr)
        readable_identity = subprocess.run(
            [str(probe), "readable", str(self.fake_python)],
            cwd=self.base,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=30,
            check=False,
        )
        self.assertEqual(91, readable_identity.returncode)
        self.assertRegex(
            readable_identity.stderr,
            r"(?i)access.*denied|Win32 error 5",
        )

        completed = self.fixture.run("Structural")

        self.assertNotEqual(0, completed.returncode)
        self.assertEqual([], self.fixture.records())
        self.assertRegex(
            completed.stderr,
            r"(?i)path identity.*(?:access.*denied|Win32 error 5)",
        )
        evidence = self.fixture.run_root / "evidence"
        self.assertEqual([], list(evidence.glob("*.result.json")))
        self.assertEqual([], list(evidence.glob("*.stdout.txt")))
        self.assertEqual([], list(evidence.glob("*.stderr.txt")))
        self.assertTrue(
            (evidence / "gate-summary.json").is_file(),
            "safe RunRoot did not publish gate-summary.json",
        )
        summary = self.fixture.summary()
        self.assertEqual(1, summary["schema_version"])
        self.assertEqual("failed", summary["status"])
        self.assertEqual("validation", summary["failure_kind"])
        self.assertRegex(
            summary["error"],
            r"(?i)path identity.*(?:access.*denied|Win32 error 5)",
        )
        self.assertEqual("no-head", summary["head_token"])
        self.assertEqual([], summary["steps"])

    def test_missing_python_after_safe_tree_publishes_validation_summary(
        self,
    ) -> None:
        head = self.fixture.initialize_git_repo()
        path_without_python = self.base / "path-without-python"
        path_without_python.mkdir()

        completed = self.fixture.run(
            "Structural",
            extra_environment={
                "GIT_COMMIT": head,
                "PATH": str(path_without_python),
            },
        )

        self.assertEqual(1, completed.returncode, completed.stderr)
        self.assertEqual([], self.fixture.records())
        self.assertRegex(completed.stderr, r"(?i)python\.exe")
        evidence = self.fixture.run_root / "evidence"
        self.assertEqual([], list(evidence.glob("*.result.json")))
        self.assertEqual([], list(evidence.glob("*.stdout.txt")))
        self.assertEqual([], list(evidence.glob("*.stderr.txt")))
        self.assertTrue(
            (evidence / "gate-summary.json").is_file(),
            "safe RunRoot did not publish gate-summary.json",
        )
        summary = self.fixture.summary()
        self.assertEqual(1, summary["schema_version"])
        self.assertEqual("failed", summary["status"])
        self.assertEqual("validation", summary["failure_kind"])
        self.assertRegex(summary["error"], r"(?i)python\.exe")
        self.assertEqual(head[:12], summary["head_token"])
        self.assertEqual([], summary["steps"])

    def test_project_root_replacement_after_source_is_caught_before_result(self) -> None:
        old_project = self.base / "project-before-replacement"

        completed = self.fixture.run(
            "Structural",
            extra_environment={
                "WINTER_GATE_FAKE_MODE": "swap-project",
                "WINTER_GATE_PROJECT_DIR": str(self.project),
                "WINTER_GATE_PROJECT_OLD": str(old_project),
            },
            gate_cwd=self.base,
        )

        self.assertEqual(1, completed.returncode, completed.stderr)
        self.assertEqual(1, len(self.fixture.records()))
        self.assertTrue((old_project / "Tools").is_dir())
        self.assertTrue(self.project.is_dir())
        self.assertEqual([], list(self.project.iterdir()))
        self.assertEqual(
            [],
            list((self.fixture.run_root / "evidence").glob("*.result.json")),
        )
        summary = self.fixture.summary()
        self.assertEqual("failed", summary["status"])
        self.assertEqual("validation", summary["failure_kind"])
        self.assertRegex(summary["error"], r"(?i)ProjectRoot|path identity")

    def test_required_file_replaced_during_child_is_failed_after_tree_drain(
        self,
    ) -> None:
        source_contract = self.tools / "test_governance_winter_interlude.py"

        completed = self.fixture.run(
            "Structural",
            replace_required_after={1: source_contract},
        )

        self.assertEqual(1, completed.returncode, completed.stderr)
        self.assertEqual(1, len(self.fixture.records()))
        summary = self.fixture.summary()
        self.assertEqual("failed", summary["status"])
        self.assertEqual("validation", summary["failure_kind"])
        self.assertIn("required file identity changed", summary["error"])
        self.assertNotEqual(
            "structural manifest layer not implemented",
            summary["error"],
        )
        self.assertEqual(1, len(summary["steps"]))
        self.assertEqual("failed", summary["steps"][0]["status"])
        self.assertEqual("validation", summary["steps"][0]["failure_kind"])

    def test_head_token_uses_real_linked_worktree_packed_ref(self) -> None:
        head = self.fixture.use_linked_worktree_with_packed_refs()

        completed = self.fixture.run("Structural")

        self.assertEqual(1, completed.returncode, completed.stderr)
        summary = self.fixture.summary()
        self.assertEqual(head[:12], summary["head_token"])
        self.assertEqual(1, len(summary["steps"]))
        result_relative = str(summary["steps"][0]["result"])
        self.assertIn(f"-{head[:12]}.result.json", result_relative)
        self.assertTrue(
            evidence_file(self.fixture.run_root, result_relative).is_file()
        )

    def test_head_token_uses_real_ordinary_loose_ref_and_exact_git_commit(self) -> None:
        head = self.fixture.initialize_git_repo()

        completed = self.fixture.run(
            "Structural",
            extra_environment={"GIT_COMMIT": head},
        )

        self.assertEqual(1, completed.returncode, completed.stderr)
        self.assertEqual(1, len(self.fixture.records()))
        summary = self.fixture.summary()
        self.assertEqual(head[:12], summary["head_token"])
        self.assertEqual(
            f"structural-01-source-contract-{head[:12]}.result.json",
            Path(str(summary["steps"][0]["result"])).name,
        )

    def test_git_indirection_rejects_root_current_drive_and_drive_relative_paths(
        self,
    ) -> None:
        unsafe_values = (
            ("backslash-root-relative", r"\winter-gate-metadata"),
            ("forward-root-current-drive", "/winter-gate-metadata"),
            ("drive-relative", "C:winter-gate-metadata"),
        )
        for metadata_record in ("gitdir", "commondir"):
            for path_form, unsafe_value in unsafe_values:
                with self.subTest(
                    metadata_record=metadata_record,
                    path_form=path_form,
                ):
                    fixture = self.make_project()
                    try:
                        if metadata_record == "gitdir":
                            (fixture.root / ".git").write_text(
                                f"gitdir: {unsafe_value}\n",
                                encoding="utf-8",
                            )
                        else:
                            fixture.initialize_git_repo()
                            (fixture.root / ".git" / "commondir").write_text(
                                unsafe_value + "\n",
                                encoding="utf-8",
                            )

                        completed = fixture.run("Structural")

                        self.assertEqual(1, completed.returncode, completed.stderr)
                        self.assertEqual([], fixture.records())
                        summary = fixture.summary()
                        self.assertEqual("failed", summary["status"])
                        self.assertEqual("validation", summary["failure_kind"])
                        self.assertRegex(
                            summary["error"],
                            r"(?i)root-relative|drive-relative|unsafe path",
                        )
                    finally:
                        fixture.close()

    def test_per_worktree_reference_namespaces_never_fall_back_to_common_packed_refs(
        self,
    ) -> None:
        for namespace in ("bisect", "rewritten", "worktree"):
            for loose_present in (True, False):
                with self.subTest(
                    namespace=namespace,
                    loose_present=loose_present,
                ):
                    fixture = self.make_project()
                    try:
                        head = fixture.use_linked_worktree_with_packed_refs()
                        linked_gitdir, common_gitdir = (
                            fixture.linked_git_directories()
                        )
                        reference = f"refs/{namespace}/gate"
                        (linked_gitdir / "HEAD").write_text(
                            f"ref: {reference}\n",
                            encoding="ascii",
                        )
                        forged = "0" * len(head)
                        if forged == head:
                            forged = "1" * len(head)
                        packed_refs = common_gitdir / "packed-refs"
                        packed_bytes = packed_refs.read_bytes()
                        separator = b"" if packed_bytes.endswith(b"\n") else b"\n"
                        packed_refs.write_bytes(
                            packed_bytes
                            + separator
                            + f"{forged} {reference}\n".encode("ascii")
                        )
                        if loose_present:
                            loose_ref = linked_gitdir / Path(
                                *reference.split("/")
                            )
                            loose_ref.parent.mkdir(parents=True, exist_ok=True)
                            loose_ref.write_text(head + "\n", encoding="ascii")

                        completed = fixture.run("Structural")

                        self.assertEqual(1, completed.returncode, completed.stderr)
                        summary = fixture.summary()
                        if loose_present:
                            self.assertEqual(1, len(fixture.records()))
                            self.assertEqual(head[:12], summary["head_token"])
                        else:
                            self.assertEqual([], fixture.records())
                            self.assertEqual("failed", summary["status"])
                            self.assertEqual(
                                "validation",
                                summary["failure_kind"],
                            )
                            self.assertIn(
                                "Git HEAD reference has no current commit",
                                summary["error"],
                            )
                    finally:
                        fixture.close()

    def test_git_metadata_identity_replacement_during_child_fails_before_result(
        self,
    ) -> None:
        for metadata_file in ("HEAD", "loose-ref"):
            with self.subTest(metadata_file=metadata_file):
                fixture = self.make_project()
                try:
                    fixture.initialize_git_repo()
                    head_path = fixture.root / ".git" / "HEAD"
                    if metadata_file == "HEAD":
                        target = head_path
                    else:
                        head_line = head_path.read_text(
                            encoding="ascii"
                        ).strip()
                        self.assertRegex(head_line, r"^ref: refs/")
                        reference = head_line.removeprefix("ref: ")
                        target = fixture.root / ".git" / Path(
                            *reference.split("/")
                        )
                    original_bytes = target.read_bytes()
                    original_file_index = target.stat().st_ino

                    completed = fixture.run(
                        "Structural",
                        replace_identity_after={1: target},
                    )

                    self.assertEqual(1, completed.returncode, completed.stderr)
                    self.assertEqual(original_bytes, target.read_bytes())
                    self.assertNotEqual(
                        original_file_index,
                        target.stat().st_ino,
                    )
                    records = fixture.records()
                    self.assertEqual(1, len(records))
                    self.assertEqual("source-contract", records[0]["step"])
                    self.assertEqual(
                        [],
                        list(
                            (fixture.run_root / "evidence").glob(
                                "*.result.json"
                            )
                        ),
                    )
                    summary = fixture.summary()
                    self.assertEqual("failed", summary["status"])
                    self.assertEqual("validation", summary["failure_kind"])
                    self.assertIn(
                        "ProjectRoot Git file identity changed during the gate run",
                        summary["error"],
                    )
                    self.assertEqual([], summary["steps"])
                finally:
                    fixture.close()

    def test_linked_worktree_ignores_forged_loose_shared_branch_ref(self) -> None:
        head = self.fixture.use_linked_worktree_with_packed_refs()
        gitdir_line = (self.fixture.root / ".git").read_text(
            encoding="utf-8"
        ).strip()
        linked_gitdir = Path(gitdir_line.removeprefix("gitdir: "))
        forged_ref = linked_gitdir / "refs" / "heads" / "gate-linked"
        forged_ref.parent.mkdir(parents=True, exist_ok=True)
        forged = "0" * len(head)
        if forged == head:
            forged = "1" * len(head)
        forged_ref.write_text(forged + "\n", encoding="ascii")

        completed = self.fixture.run("Structural")

        self.assertEqual(1, completed.returncode, completed.stderr)
        self.assertEqual(head[:12], self.fixture.summary()["head_token"])

    def test_git_head_read_fails_closed_while_a_writer_is_open(self) -> None:
        self.fixture.initialize_git_repo()
        head_path = self.fixture.root / ".git" / "HEAD"
        writer = open_writable_shared_file(head_path)
        self.addCleanup(close_windows_handle, writer)

        completed = self.fixture.run("Structural")

        self.assertEqual(1, completed.returncode, completed.stderr)
        self.assertEqual([], self.fixture.records())
        summary = self.fixture.summary()
        self.assertEqual("failed", summary["status"])
        self.assertEqual("validation", summary["failure_kind"])
        self.assertRegex(summary["error"], r"(?i)sharing|Win32 error 32")

    def test_git_loose_ref_parent_junction_is_rejected_before_launch(self) -> None:
        self.fixture.initialize_git_repo()
        heads = self.fixture.root / ".git" / "refs" / "heads"
        routed_heads = self.base / "outside-project-git-heads"
        os.replace(heads, routed_heads)
        create_junction(heads, routed_heads)
        self.fixture.register_junction(heads)

        completed = self.fixture.run("Structural")

        self.assertEqual(1, completed.returncode, completed.stderr)
        self.assertEqual([], self.fixture.records())
        summary = self.fixture.summary()
        self.assertEqual("failed", summary["status"])
        self.assertEqual("validation", summary["failure_kind"])
        self.assertRegex(summary["error"], r"(?i)path identity|reparse")

    def test_explicit_empty_git_commit_is_rejected(self) -> None:
        head = self.fixture.initialize_git_repo()
        self.assertTrue(head)

        completed = self.fixture.run(
            "Structural",
            extra_environment={"GIT_COMMIT": ""},
        )

        self.assertEqual(1, completed.returncode, completed.stderr)
        self.assertEqual([], self.fixture.records())
        summary = self.fixture.summary()
        self.assertEqual("failed", summary["status"])
        self.assertEqual("validation", summary["failure_kind"])
        self.assertEqual(
            "GIT_COMMIT does not exactly match the current ProjectRoot HEAD.",
            summary["error"],
        )

    def test_forged_git_commit_is_honest_validation_failure(self) -> None:
        head = self.fixture.initialize_git_repo()
        forged = "0" * len(head)
        if forged == head:
            forged = "1" * len(head)

        completed = self.fixture.run(
            "Structural",
            extra_environment={"GIT_COMMIT": forged},
        )

        self.assertEqual(1, completed.returncode, completed.stderr)
        self.assertEqual([], self.fixture.records())
        summary = self.fixture.summary()
        self.assertEqual(head[:12], summary["head_token"])
        self.assertEqual("failed", summary["status"])
        self.assertEqual("validation", summary["failure_kind"])
        self.assertEqual(
            "GIT_COMMIT does not exactly match the current ProjectRoot HEAD.",
            summary["error"],
        )
        self.assertEqual([], summary["steps"])

    def test_public_process_uses_exact_argv_job_nul_and_handle_list(self) -> None:
        sentinel = self.base / "inheritable-sentinel.txt"
        sentinel.write_text("must not reach the gate child", encoding="utf-8")
        sentinel_handle = create_inheritable_sentinel(sentinel)
        self.addCleanup(close_windows_handle, sentinel_handle)
        run_root = self.new_run_root()

        proof_record = self.base / "sentinel-inheritance-proof.jsonl"
        proof_environment = os.environ.copy()
        proof_environment.pop("WINTER_GATE_CONTROL", None)
        proof_environment.update(
            {
                "WINTER_GATE_RECORD": str(proof_record),
                "WINTER_GATE_FAKE_MODE": "normal",
                "WINTER_GATE_SENTINEL_HANDLE": str(sentinel_handle),
                "WINTER_GATE_SENTINEL_PATH": str(sentinel.resolve()),
            }
        )
        proof = subprocess.run(
            [
                str(self.fake_python),
                "-m",
                "unittest",
                "Tools.test_governance_winter_interlude",
                "-v",
            ],
            cwd=self.project,
            env=proof_environment,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=10,
            check=False,
            close_fds=False,
        )
        self.assertEqual(0, proof.returncode, proof.stderr)
        proof_records = read_json_lines(proof_record)
        self.assertEqual(1, len(proof_records))
        self.assertIs(True, proof_records[0]["sentinel_inherited"])

        completed = self.invoke(
            run_root,
            extra_environment={
                "WINTER_GATE_SENTINEL_HANDLE": str(sentinel_handle),
                "WINTER_GATE_SENTINEL_PATH": str(sentinel.resolve()),
            },
            close_fds=False,
        )

        records = read_json_lines(self.record)
        self.assertEqual(1, completed.returncode, completed.stderr)
        self.assertIn(
            "structural manifest layer not implemented",
            completed.stderr,
        )
        self.assertEqual(1, len(records))
        python_record = records[0]
        self.assertEqual("Python", python_record["kind"])
        self.assertEqual(
            [
                "-m",
                "unittest",
                "Tools.test_governance_winter_interlude",
                "-v",
            ],
            python_record["argv"],
        )
        self.assertEqual(
            os.path.normcase(str(self.fake_python.resolve())),
            os.path.normcase(str(Path(str(python_record["argv0"])).resolve())),
        )
        self.assertEqual(
            os.path.normcase(str(self.project.resolve())),
            os.path.normcase(str(Path(str(python_record["cwd"])).resolve())),
        )
        self.assertIs(True, python_record["in_job"])
        self.assertRegex(
            python_record["expected_job_name"],
            r"^Local\\WinterGate-[0-9a-f]{32}$",
        )
        self.assertIs(True, python_record["in_expected_job"])
        self.assertEqual(0x0002, python_record["stdin_file_type"])
        self.assertIs(False, python_record["sentinel_inherited"])

        source = GATE.read_text(encoding="utf-8")
        engine = source[
            source.index("// BEGIN PROCESS ENGINE") :
            source.index("// END PROCESS ENGINE")
        ]
        self.assertLess(
            engine.index("if (!AssignProcessToJobObject("),
            engine.index("uint previousSuspendCount = ResumeThread("),
        )

        summary = self.load_summary(run_root)
        self.assertEqual("failed", summary["status"])
        self.assertEqual("validation", summary["failure_kind"])
        self.assertEqual(
            "structural manifest layer not implemented",
            summary["error"],
        )
        self.assertEqual(1, len(summary["steps"]))
        first = summary["steps"][0]
        self.assertEqual("source-contract", first["name"])
        for json_path in (
            run_root / "evidence" / "gate-summary.json",
            evidence_file(run_root, first["result"]),
        ):
            self.assertFalse(
                json_path.read_bytes().startswith(b"\xef\xbb\xbf"),
                json_path,
            )
        self.assertIs(True, first["process_started"])
        self.assertIsInstance(first["process_id"], int)
        self.assertIsInstance(first["started_utc"], str)
        self.assertIsInstance(first["ended_utc"], str)
        self.assertIsInstance(first["elapsed_milliseconds"], int)
        self.assertEqual(0, first["exit_code"])
        self.assertIs(False, first["timed_out"])
        self.assertIs(True, first["tree_drained"])
        self.assertIs(False, first["had_live_descendants_after_root_exit"])
        self.assertEqual("passed", first["status"])
        self.assertIsNone(first["failure_kind"])
        self.assertIsNone(first["error"])
        self.assertIn(
            "fake-python-stdout",
            evidence_file(run_root, first["stdout"]).read_text(
                encoding="utf-8-sig"
            ),
        )
        self.assertIn(
            "fake-python-stderr",
            evidence_file(run_root, first["stderr"]).read_text(
                encoding="utf-8-sig"
            ),
        )

    def test_bad_image_start_failure_keeps_process_fields_null(self) -> None:
        self.fake_python.unlink()
        self.fake_python.write_bytes(b"ordinary bytes, not a PE image\r\n")
        run_root = self.new_run_root()

        completed = self.invoke(run_root)

        self.assertNotEqual(0, completed.returncode)
        self.assertEqual([], read_json_lines(self.record))
        summary = self.load_summary(run_root)
        self.assertEqual("failed", summary["status"])
        self.assertEqual("process", summary["failure_kind"])
        self.assertEqual(1, len(summary["steps"]))
        result = summary["steps"][0]
        self.assertIs(False, result["process_started"])
        for field in (
            "process_id",
            "started_utc",
            "ended_utc",
            "elapsed_milliseconds",
            "exit_code",
        ):
            self.assertIsNone(result[field], field)
        self.assertIs(False, result["timed_out"])
        self.assertIs(True, result["tree_drained"])
        self.assertIs(False, result["had_live_descendants_after_root_exit"])
        self.assertEqual("failed", result["status"])
        self.assertEqual("process", result["failure_kind"])
        self.assertRegex(result["error"], r"(?i)CreateProcessW|193|bad exe")
        stdout_path = evidence_file(run_root, result["stdout"])
        stderr_path = evidence_file(run_root, result["stderr"])
        self.assertEqual(b"", stdout_path.read_bytes())
        self.assertEqual(b"", stderr_path.read_bytes())
        moved_stdout = stdout_path.with_suffix(".moved")
        os.replace(stdout_path, moved_stdout)
        os.replace(moved_stdout, stdout_path)

```

#### Exact implementation catalog (copy only the spans named by each GREEN step)

The following catalog is the exact final C# and PowerShell content. It is not a
single paste step. Loops 3.1-3.5 name disjoint initial additions or exact
replacements from this catalog, so every later RED runs against the previous
GREEN and hits the newly exposed behavior rather than Task 2's old sentinel.

First replace Task 2's complete native-source `using` block (from its first
`using System;` through `using Microsoft.Win32.SafeHandles;`) with this exact
block. This is a replacement, not an additive snippet: the process region uses
`Stopwatch`, invariant Win32 formatting, and bounded polling, while the path
region still needs its generic collections and safe handles.

```csharp
using System;
using System.Collections;
using System.Collections.Generic;
using System.ComponentModel;
using System.Diagnostics;
using System.Globalization;
using System.IO;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading;
using Microsoft.Win32.SafeHandles;
```

The long region below is the final-state catalog for the exact
`// BEGIN PROCESS ENGINE` / `// END PROCESS ENGINE` seam in Task 2's one
`Add-Type` source. Do not replace the seam with the whole region in one action.
Its literal BEGIN/END comments are the copy boundaries:

- Loop 3.1 copies exactly `LOOP 3.1-A`, `3.1-B`, `3.1-C`, and `3.1-D`,
  in that order inside the empty process seam.
- Loop 3.2 inserts exactly `LOOP 3.2-A` immediately after `3.1-B`,
  `LOOP 3.2-B` immediately after `3.1-C`, and `LOOP 3.2-C` immediately
  after `3.2-B`.
- Loop 3.3 inserts exactly `LOOP 3.3-A` immediately after `3.2-A`,
  `LOOP 3.3-B` immediately after `3.2-B`, `LOOP 3.3-C` immediately after
  `3.2-C`, and `LOOP 3.3-D` immediately after the temporary accounting
  method printed after the final catalog.
- Loop 3.4 makes no C# change.
- Loop 3.5 deletes that one temporary accounting method, inserts exactly
  `LOOP 3.5-A` between `3.3-C` and `3.3-D`, and applies the output-evidence
  ownership additions printed below to the same process seam and existing DTO.

Copy both boundary comments with each region so a missing, duplicated, or
out-of-order region is visible in review. `PathIdentity`, `SameObject`, and
`SameStablePath` remain owned by Task 2. Loop 3.5 extends Task 2's existing
`BoundedProcessResult` in place to this exact final definition; it does not add
a second DTO:

```csharp
public sealed class BoundedProcessResult
{
    public bool ProcessStarted;
    public int? ProcessId;
    public DateTime? StartedUtc;
    public DateTime? EndedUtc;
    public long? ElapsedMilliseconds;
    public int? ExitCode;
    public bool TimedOut;
    public bool TreeDrained;
    public bool HadLiveDescendantsAfterRootExit;
    public string StartError;
    public bool OutputEvidenceValid;
    public string OutputEvidenceError;
}
```

No loop adds a second `Add-Type`, public test switch, or alternate executor.

The path slice also exposes this assembly-internal helper, which builds a
`PathIdentity` from the exact already-open handle rather than reopening its
name:

```csharp
internal static PathIdentity GetPathIdentityFromOpenHandle(
    IntPtr handle,
    PathKind expectedKind);
```

This is the exact final region from which those disjoint additions are copied:

```csharp
// BEGIN PROCESS ENGINE
// BEGIN LOOP 3.1-A SHARED NATIVE DECLARATIONS
    private const uint GenericRead = 0x80000000;
    private const uint GenericWrite = 0x40000000;
    private const uint DeleteAccess = 0x00010000;
    private const uint SynchronizeAccess = 0x00100000;
    private const uint FileReadAttributes = 0x00000080;
    private const uint FileShareRead = 0x00000001;
    private const uint FileShareWrite = 0x00000002;
    private const uint FileShareDelete = 0x00000004;
    private const uint CreateNew = 1;
    private const uint OpenExisting = 3;
    private const uint FileAttributeNormal = 0x00000080;
    private const uint FileFlagOpenReparsePoint = 0x00200000;
    private const uint FileFlagBackupSemantics = 0x02000000;
    private const uint StartfUseStdHandles = 0x00000100;
    private const uint CreateSuspended = 0x00000004;
    private const uint CreateUnicodeEnvironment = 0x00000400;
    private const uint CreateNoWindow = 0x08000000;
    private const uint ExtendedStartupInfoPresent = 0x00080000;
    private const uint JobObjectLimitKillOnJobClose = 0x00002000;
    private const int JobObjectBasicAccountingInformation = 1;
    private const int JobObjectBasicProcessIdList = 3;
    private const int JobObjectExtendedLimitInformation = 9;
    private const int FileRenameInfo = 3;
    private const int ErrorFileNotFound = 2;
    private const int ErrorPathNotFound = 3;
    private const int ErrorMoreData = 234;
    private const int ErrorInvalidParameter = 87;
    private const int ErrorAlreadyExists = 183;
    private const long ProcThreadAttributeHandleList = 0x00020002;
    private const uint WaitObject0 = 0x00000000;
    private const uint WaitTimeout = 0x00000102;
    private const uint WaitFailed = 0xFFFFFFFF;
    private const uint ResumeFailed = 0xFFFFFFFF;
    private const uint ForcedExitCode = 0x0000DEAD;
    private const int CleanupTimeoutMilliseconds = 10000;
    private const int CleanupPollMilliseconds = 25;

    private static readonly IntPtr InvalidHandleValue = new IntPtr(-1);
    private const string GateJobEnvironmentVariable = "WINTER_GATE_JOB_NAME";

    [StructLayout(LayoutKind.Sequential)]
    private struct SecurityAttributes
    {
        internal int Length;
        internal IntPtr SecurityDescriptor;
        internal int InheritHandle;
    }

    [StructLayout(LayoutKind.Sequential, CharSet = CharSet.Unicode)]
    private struct StartupInfo
    {
        internal int Size;
        internal string Reserved;
        internal string Desktop;
        internal string Title;
        internal int X;
        internal int Y;
        internal int XSize;
        internal int YSize;
        internal int XCountChars;
        internal int YCountChars;
        internal int FillAttribute;
        internal int Flags;
        internal short ShowWindow;
        internal short Reserved2Size;
        internal IntPtr Reserved2;
        internal IntPtr StdInput;
        internal IntPtr StdOutput;
        internal IntPtr StdError;
    }

    [StructLayout(LayoutKind.Sequential)]
    private struct StartupInfoEx
    {
        internal StartupInfo StartupInfo;
        internal IntPtr AttributeList;
    }

    [StructLayout(LayoutKind.Sequential)]
    private struct ProcessInformation
    {
        internal IntPtr Process;
        internal IntPtr Thread;
        internal uint ProcessId;
        internal uint ThreadId;
    }

    [StructLayout(LayoutKind.Sequential)]
    private struct JobObjectBasicLimitInformation
    {
        internal long PerProcessUserTimeLimit;
        internal long PerJobUserTimeLimit;
        internal uint LimitFlags;
        internal UIntPtr MinimumWorkingSetSize;
        internal UIntPtr MaximumWorkingSetSize;
        internal uint ActiveProcessLimit;
        internal UIntPtr Affinity;
        internal uint PriorityClass;
        internal uint SchedulingClass;
    }

    [StructLayout(LayoutKind.Sequential)]
    private struct IoCounters
    {
        internal ulong ReadOperationCount;
        internal ulong WriteOperationCount;
        internal ulong OtherOperationCount;
        internal ulong ReadTransferCount;
        internal ulong WriteTransferCount;
        internal ulong OtherTransferCount;
    }

    [StructLayout(LayoutKind.Sequential)]
    private struct JobObjectExtendedLimitInformationData
    {
        internal JobObjectBasicLimitInformation BasicLimitInformation;
        internal IoCounters IoInfo;
        internal UIntPtr ProcessMemoryLimit;
        internal UIntPtr JobMemoryLimit;
        internal UIntPtr PeakProcessMemoryUsed;
        internal UIntPtr PeakJobMemoryUsed;
    }

    [StructLayout(LayoutKind.Sequential)]
    private struct JobObjectBasicAccountingInformationData
    {
        internal long TotalUserTime;
        internal long TotalKernelTime;
        internal long ThisPeriodTotalUserTime;
        internal long ThisPeriodTotalKernelTime;
        internal uint TotalPageFaultCount;
        internal uint TotalProcesses;
        internal uint ActiveProcesses;
        internal uint TotalTerminatedProcesses;
    }

    [DllImport("kernel32.dll", CharSet = CharSet.Unicode, SetLastError = true)]
    private static extern IntPtr CreateFileW(
        string fileName,
        uint desiredAccess,
        uint shareMode,
        ref SecurityAttributes securityAttributes,
        uint creationDisposition,
        uint flagsAndAttributes,
        IntPtr templateFile);

    [DllImport("kernel32.dll", SetLastError = true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    private static extern bool WriteFile(
        IntPtr file,
        IntPtr buffer,
        uint bytesToWrite,
        out uint bytesWritten,
        IntPtr overlapped);

    [DllImport("kernel32.dll", SetLastError = true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    private static extern bool FlushFileBuffers(IntPtr file);

    [DllImport("kernel32.dll", SetLastError = true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    private static extern bool SetFileInformationByHandle(
        IntPtr file,
        int informationClass,
        IntPtr information,
        uint bufferSize);

    [DllImport("kernel32.dll", CharSet = CharSet.Unicode, SetLastError = true)]
    private static extern IntPtr CreateJobObjectW(IntPtr jobAttributes, string name);

    [DllImport("kernel32.dll", SetLastError = true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    private static extern bool SetInformationJobObject(
        IntPtr job,
        int informationClass,
        ref JobObjectExtendedLimitInformationData information,
        int informationLength);

    [DllImport("kernel32.dll", SetLastError = true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    private static extern bool QueryInformationJobObject(
        IntPtr job,
        int informationClass,
        out JobObjectBasicAccountingInformationData information,
        int informationLength,
        IntPtr returnLength);

    [DllImport(
        "kernel32.dll",
        EntryPoint = "QueryInformationJobObject",
        SetLastError = true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    private static extern bool QueryInformationJobObjectBuffer(
        IntPtr job,
        int informationClass,
        IntPtr information,
        int informationLength,
        IntPtr returnLength);

    [DllImport("kernel32.dll", SetLastError = true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    private static extern bool InitializeProcThreadAttributeList(
        IntPtr attributeList,
        int attributeCount,
        int flags,
        ref IntPtr size);

    [DllImport("kernel32.dll", SetLastError = true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    private static extern bool UpdateProcThreadAttribute(
        IntPtr attributeList,
        uint flags,
        IntPtr attribute,
        IntPtr value,
        IntPtr size,
        IntPtr previousValue,
        IntPtr returnSize);

    [DllImport("kernel32.dll")]
    private static extern void DeleteProcThreadAttributeList(IntPtr attributeList);

    [DllImport("kernel32.dll", CharSet = CharSet.Unicode, SetLastError = true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    private static extern bool CreateProcessW(
        string applicationName,
        StringBuilder commandLine,
        IntPtr processAttributes,
        IntPtr threadAttributes,
        [MarshalAs(UnmanagedType.Bool)] bool inheritHandles,
        uint creationFlags,
        IntPtr environment,
        string currentDirectory,
        ref StartupInfoEx startupInfo,
        out ProcessInformation processInformation);

    [DllImport("kernel32.dll", SetLastError = true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    private static extern bool AssignProcessToJobObject(IntPtr job, IntPtr process);

    [DllImport("kernel32.dll", SetLastError = true)]
    private static extern uint ResumeThread(IntPtr thread);

    [DllImport("kernel32.dll", SetLastError = true)]
    private static extern uint WaitForSingleObject(IntPtr handle, uint milliseconds);

    [DllImport("kernel32.dll", SetLastError = true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    private static extern bool TerminateJobObject(IntPtr job, uint exitCode);

    [DllImport("kernel32.dll", SetLastError = true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    private static extern bool TerminateProcess(IntPtr process, uint exitCode);

    [DllImport("kernel32.dll", SetLastError = true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    private static extern bool GetExitCodeProcess(IntPtr process, out uint exitCode);

    [DllImport("kernel32.dll", SetLastError = true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    private static extern bool CloseHandle(IntPtr handle);

    [DllImport("kernel32.dll", SetLastError = true)]
    private static extern IntPtr OpenProcess(
        uint desiredAccess,
        [MarshalAs(UnmanagedType.Bool)] bool inheritHandle,
        uint processId);
// END LOOP 3.1-A SHARED NATIVE DECLARATIONS

// BEGIN LOOP 3.1-B READABLE PUBLIC API
    public static PathIdentity GetReadableFileIdentity(string path)
    {
        return GetReadableFileIdentityCore(path, false);
    }

    public static PathIdentity TryGetReadableFileIdentity(string path)
    {
        return GetReadableFileIdentityCore(path, true);
    }

    public static string ReadVerifiedUtf8TextFile(
        string path,
        PathIdentity expectedIdentity,
        int maximumBytes)
    {
        if (expectedIdentity == null)
        {
            throw new ArgumentNullException("expectedIdentity");
        }
        if (maximumBytes < 1)
        {
            throw new ArgumentOutOfRangeException("maximumBytes");
        }
        RequirePlainAbsoluteFilePath(path, "path");
        PathIdentity chainIdentity = GetPathIdentity(
            path,
            PathKind.File,
            true);
        if (!SameStablePath(expectedIdentity, chainIdentity))
        {
            throw new WinterGatePathIdentityException(
                "path identity: verified UTF-8 input changed before open: " +
                path);
        }
        SecurityAttributes nonInheritable = NewSecurityAttributes(false);
        IntPtr fileHandle = CreateFileW(
            chainIdentity.FinalPath,
            GenericRead,
            FileShareRead,
            ref nonInheritable,
            OpenExisting,
            FileAttributeNormal | FileFlagOpenReparsePoint |
                FileFlagBackupSemantics,
            IntPtr.Zero);
        if (fileHandle == InvalidHandleValue)
        {
            throw JsonPathIdentityError(
                "CreateFileW(verified UTF-8 read)",
                path,
                Marshal.GetLastWin32Error());
        }
        try
        {
            PathIdentity currentIdentity = GetPathIdentityFromOpenHandle(
                fileHandle,
                PathKind.File);
            if ((currentIdentity.Attributes & FileAttributes.ReparsePoint) != 0 ||
                !SameStablePath(chainIdentity, currentIdentity) ||
                !SameStablePath(expectedIdentity, currentIdentity))
            {
                throw new WinterGatePathIdentityException(
                    "path identity: verified UTF-8 input changed: " + path);
            }

            using (SafeFileHandle safeHandle = new SafeFileHandle(
                fileHandle,
                true))
            {
                fileHandle = IntPtr.Zero;
                using (FileStream stream = new FileStream(
                    safeHandle,
                    FileAccess.Read))
                {
                    if (stream.Length > maximumBytes)
                    {
                        throw new InvalidDataException(
                            "Verified UTF-8 input exceeds its size limit: " + path);
                    }
                    using (StreamReader reader = new StreamReader(
                        stream,
                        new UTF8Encoding(false, true),
                        false,
                        4096,
                        true))
                    {
                        return reader.ReadToEnd();
                    }
                }
            }
        }
        finally
        {
            CloseOwnedHandle(ref fileHandle);
        }
    }

// END LOOP 3.1-B READABLE PUBLIC API

// BEGIN LOOP 3.2-A JSON WRITER PUBLIC API
    public static string WriteOwnedSummaryUtf8Json(
        string path,
        string normalJson,
        string collisionFailureJson,
        PathIdentity expectedEvidenceDirectoryIdentity)
    {
        ValidateJsonPath(path, expectedEvidenceDirectoryIdentity);
        if (!String.Equals(
            Path.GetFileName(path),
            "gate-summary.json",
            StringComparison.Ordinal))
        {
            throw new ArgumentException(
                "The owned summary publisher only accepts gate-summary.json.",
                "path");
        }

        byte[] normalUtf8Bytes = EncodeUtf8Json(normalJson);
        byte[] collisionUtf8Bytes = EncodeUtf8Json(collisionFailureJson);
        string evidenceDirectory =
            expectedEvidenceDirectoryIdentity.FinalPath;
        string nonce = Guid.NewGuid().ToString("N");
        string stagingPath = Path.Combine(
            evidenceDirectory,
            "gate-summary.pending." + nonce + ".json");
        string quarantinePath = Path.Combine(
            evidenceDirectory,
            "gate-summary.unowned." + nonce + ".json");
        SecurityAttributes nonInheritable = NewSecurityAttributes(false);
        IntPtr evidenceDirectoryGuard = InvalidHandleValue;
        IntPtr stagingHandle = InvalidHandleValue;
        IntPtr existingHandle = InvalidHandleValue;
        IntPtr quarantineVerification = InvalidHandleValue;
        IntPtr finalVerification = InvalidHandleValue;
        bool quarantinedExistingSummary = false;
        try
        {
            PathIdentity guardedEvidenceIdentity = OpenVerifiedEvidenceGuard(
                expectedEvidenceDirectoryIdentity,
                path,
                ref evidenceDirectoryGuard);

            stagingHandle = CreateFileW(
                stagingPath,
                GenericWrite | DeleteAccess,
                FileShareRead | FileShareWrite,
                ref nonInheritable,
                CreateNew,
                FileAttributeNormal | FileFlagOpenReparsePoint,
                IntPtr.Zero);
            if (stagingHandle == InvalidHandleValue)
            {
                throw new IOException(
                    LastError("CreateFileW(summary staging create-new)"));
            }
            RequireDirectEvidenceChild(
                stagingHandle,
                stagingPath,
                guardedEvidenceIdentity,
                "summary staging");
            PathIdentity stagingBeforeRename = GetPathIdentityFromOpenHandle(
                stagingHandle,
                PathKind.File);
            existingHandle = CreateFileW(
                path,
                FileReadAttributes | DeleteAccess,
                FileShareRead | FileShareWrite,
                ref nonInheritable,
                OpenExisting,
                FileAttributeNormal | FileFlagOpenReparsePoint,
                IntPtr.Zero);
            if (existingHandle == InvalidHandleValue)
            {
                int error = Marshal.GetLastWin32Error();
                if (error != ErrorFileNotFound)
                {
                    throw JsonPathIdentityError(
                        "CreateFileW(existing unowned summary)",
                        path,
                        error);
                }
            }
            else
            {
                RequireDirectEvidenceChild(
                    existingHandle,
                    path,
                    guardedEvidenceIdentity,
                    "existing unowned summary");
                PathIdentity existingBeforeRename =
                    GetPathIdentityFromOpenHandle(
                        existingHandle,
                        PathKind.File);
                if ((existingBeforeRename.Attributes &
                        FileAttributes.ReparsePoint) != 0)
                {
                    throw new WinterGatePathIdentityException(
                        "path identity: existing gate-summary.json is a " +
                        "reparse point.");
                }
                RenameOpenFileNoReplace(
                    existingHandle,
                    quarantinePath,
                    expectedEvidenceDirectoryIdentity,
                    "quarantine unowned summary");
                PathIdentity existingAfterRename =
                    GetPathIdentityFromOpenHandle(
                        existingHandle,
                        PathKind.File);
                if (!SameObject(existingBeforeRename, existingAfterRename))
                {
                    throw new WinterGatePathIdentityException(
                        "path identity: unowned summary object changed during " +
                        "quarantine.");
                }
                quarantineVerification = OpenPlainDirectEvidenceFile(
                    quarantinePath,
                    guardedEvidenceIdentity,
                    nonInheritable,
                    "quarantined unowned summary");
                PathIdentity quarantineIdentity =
                    GetPathIdentityFromOpenHandle(
                        quarantineVerification,
                        PathKind.File);
                if (!SameObject(existingBeforeRename, quarantineIdentity) ||
                    !SameStablePath(existingAfterRename, quarantineIdentity))
                {
                    throw new WinterGatePathIdentityException(
                        "path identity: quarantined summary verification failed.");
                }
                quarantinedExistingSummary = true;
            }

            WriteAllAndFlush(
                stagingHandle,
                quarantinedExistingSummary
                    ? collisionUtf8Bytes
                    : normalUtf8Bytes,
                "summary staging");

            RenameOpenFileNoReplace(
                stagingHandle,
                path,
                expectedEvidenceDirectoryIdentity,
                "publish owned summary");
            PathIdentity stagingAfterRename = GetPathIdentityFromOpenHandle(
                stagingHandle,
                PathKind.File);
            if (!SameObject(stagingBeforeRename, stagingAfterRename))
            {
                throw new WinterGatePathIdentityException(
                    "path identity: summary staging object changed during publish.");
            }
            finalVerification = OpenPlainDirectEvidenceFile(
                path,
                guardedEvidenceIdentity,
                nonInheritable,
                "published owned summary");
            PathIdentity finalIdentity = GetPathIdentityFromOpenHandle(
                finalVerification,
                PathKind.File);
            if (!SameObject(stagingBeforeRename, finalIdentity) ||
                !SameStablePath(stagingAfterRename, finalIdentity))
            {
                throw new WinterGatePathIdentityException(
                    "path identity: published summary verification failed.");
            }
            return quarantinedExistingSummary
                ? "evidence/" + Path.GetFileName(quarantinePath)
                : null;
        }
        finally
        {
            CloseOwnedHandle(ref finalVerification);
            CloseOwnedHandle(ref quarantineVerification);
            CloseOwnedHandle(ref existingHandle);
            CloseOwnedHandle(ref stagingHandle);
            CloseOwnedHandle(ref evidenceDirectoryGuard);
        }
    }

    public static void WriteUtf8JsonCreateNew(
        string path,
        string json,
        PathIdentity expectedEvidenceDirectoryIdentity)
    {
        ValidateJsonPath(path, expectedEvidenceDirectoryIdentity);
        byte[] utf8Bytes = EncodeUtf8Json(json);
        SecurityAttributes nonInheritable = NewSecurityAttributes(false);
        IntPtr evidenceDirectoryGuard = InvalidHandleValue;
        IntPtr jsonHandle = InvalidHandleValue;
        try
        {
            PathIdentity guardedEvidenceIdentity = OpenVerifiedEvidenceGuard(
                expectedEvidenceDirectoryIdentity,
                path,
                ref evidenceDirectoryGuard);
            jsonHandle = CreateFileW(
                path,
                GenericWrite,
                0,
                ref nonInheritable,
                CreateNew,
                FileAttributeNormal,
                IntPtr.Zero);
            if (jsonHandle == InvalidHandleValue)
            {
                throw new IOException(LastError("CreateFileW(JSON create-new)"));
            }
            RequireDirectEvidenceChild(
                jsonHandle,
                path,
                guardedEvidenceIdentity,
                "JSON evidence");
            WriteAllAndFlush(jsonHandle, utf8Bytes, "JSON");
        }
        finally
        {
            CloseOwnedHandle(ref jsonHandle);
            CloseOwnedHandle(ref evidenceDirectoryGuard);
        }
    }

// END LOOP 3.2-A JSON WRITER PUBLIC API
// BEGIN LOOP 3.3-A PROCESS PUBLIC API AND LAUNCH BUILDERS
    public static BoundedProcessResult RunProcessTree(
        string executable,
        string[] arguments,
        string workingDirectory,
        string stdoutPath,
        string stderrPath,
        int timeoutMilliseconds,
        PathIdentity expectedEvidenceDirectoryIdentity)
    {
        ValidateProcessArguments(
            executable,
            arguments,
            workingDirectory,
            stdoutPath,
            stderrPath,
            timeoutMilliseconds,
            expectedEvidenceDirectoryIdentity);

        BoundedProcessResult result = new BoundedProcessResult();
        result.ProcessStarted = false;
        result.ProcessId = null;
        result.StartedUtc = null;
        result.EndedUtc = null;
        result.ElapsedMilliseconds = null;
        result.ExitCode = null;
        result.TimedOut = false;
        result.TreeDrained = true;
        result.HadLiveDescendantsAfterRootExit = false;
        result.StartError = null;
        result.OutputEvidenceValid = false;
        result.OutputEvidenceError = null;

        IntPtr stdoutHandle = InvalidHandleValue;
        IntPtr stderrHandle = InvalidHandleValue;
        IntPtr stdinHandle = InvalidHandleValue;
        IntPtr evidenceDirectoryGuard = InvalidHandleValue;
        IntPtr jobHandle = IntPtr.Zero;
        IntPtr environmentBlock = IntPtr.Zero;
        IntPtr attributeList = IntPtr.Zero;
        IntPtr inheritedHandleArray = IntPtr.Zero;
        bool attributeListInitialized = false;
        ProcessInformation processInformation = new ProcessInformation();
        bool processCreated = false;
        bool processAssigned = false;
        Stopwatch processClock = null;
        PathIdentity stdoutCreationIdentity = null;
        PathIdentity stderrCreationIdentity = null;
        PathIdentity outputEvidenceDirectoryIdentity = null;

        try
        {
            SecurityAttributes inheritable = new SecurityAttributes();
            inheritable.Length = Marshal.SizeOf(typeof(SecurityAttributes));
            inheritable.SecurityDescriptor = IntPtr.Zero;
            inheritable.InheritHandle = 1;

            SecurityAttributes nonInheritable = new SecurityAttributes();
            nonInheritable.Length = Marshal.SizeOf(typeof(SecurityAttributes));
            nonInheritable.SecurityDescriptor = IntPtr.Zero;
            nonInheritable.InheritHandle = 0;

            evidenceDirectoryGuard = CreateFileW(
                expectedEvidenceDirectoryIdentity.FinalPath,
                FileReadAttributes,
                FileShareRead | FileShareWrite,
                ref nonInheritable,
                OpenExisting,
                FileFlagBackupSemantics | FileFlagOpenReparsePoint,
                IntPtr.Zero);
            if (evidenceDirectoryGuard == InvalidHandleValue)
            {
                return RecordStartFailure(
                    result,
                    LastError("CreateFileW(evidence-directory-guard)"));
            }
            PathIdentity guardedEvidenceIdentity =
                GetPathIdentityFromOpenHandle(
                    evidenceDirectoryGuard,
                    PathKind.Directory);
            outputEvidenceDirectoryIdentity = guardedEvidenceIdentity;
            if ((guardedEvidenceIdentity.Attributes & FileAttributes.ReparsePoint) != 0 ||
                !SameStablePath(
                    expectedEvidenceDirectoryIdentity,
                    guardedEvidenceIdentity))
            {
                return RecordStartFailure(
                    result,
                    "Evidence directory identity changed before output creation.");
            }

            stdoutHandle = CreateFileW(
                stdoutPath,
                GenericWrite,
                FileShareRead | FileShareWrite | FileShareDelete,
                ref inheritable,
                CreateNew,
                FileAttributeNormal,
                IntPtr.Zero);
            if (stdoutHandle == InvalidHandleValue)
            {
                return RecordStartFailure(result, LastError("CreateFileW(stdout)"));
            }
            RequireDirectEvidenceChild(
                stdoutHandle,
                stdoutPath,
                guardedEvidenceIdentity,
                "stdout");
            stdoutCreationIdentity = GetPathIdentityFromOpenHandle(
                stdoutHandle,
                PathKind.File);

            stderrHandle = CreateFileW(
                stderrPath,
                GenericWrite,
                FileShareRead | FileShareWrite | FileShareDelete,
                ref inheritable,
                CreateNew,
                FileAttributeNormal,
                IntPtr.Zero);
            if (stderrHandle == InvalidHandleValue)
            {
                return RecordStartFailure(result, LastError("CreateFileW(stderr)"));
            }
            RequireDirectEvidenceChild(
                stderrHandle,
                stderrPath,
                guardedEvidenceIdentity,
                "stderr");
            stderrCreationIdentity = GetPathIdentityFromOpenHandle(
                stderrHandle,
                PathKind.File);

            stdinHandle = CreateFileW(
                "NUL",
                GenericRead,
                FileShareRead | FileShareWrite | FileShareDelete,
                ref inheritable,
                OpenExisting,
                FileAttributeNormal,
                IntPtr.Zero);
            if (stdinHandle == InvalidHandleValue)
            {
                return RecordStartFailure(result, LastError("CreateFileW(NUL)"));
            }

            string jobName = @"Local\WinterGate-" +
                Guid.NewGuid().ToString("N");
            jobHandle = CreateJobObjectW(IntPtr.Zero, jobName);
            if (jobHandle == IntPtr.Zero)
            {
                return RecordStartFailure(result, LastError("CreateJobObjectW"));
            }
            int createJobError = Marshal.GetLastWin32Error();
            if (createJobError == ErrorAlreadyExists)
            {
                return RecordStartFailure(
                    result,
                    "CreateJobObjectW unexpectedly opened an existing named Job.");
            }

            JobObjectExtendedLimitInformationData limits =
                new JobObjectExtendedLimitInformationData();
            limits.BasicLimitInformation.LimitFlags = JobObjectLimitKillOnJobClose;
            if (!SetInformationJobObject(
                jobHandle,
                JobObjectExtendedLimitInformation,
                ref limits,
                Marshal.SizeOf(typeof(JobObjectExtendedLimitInformationData))))
            {
                return RecordStartFailure(result, LastError("SetInformationJobObject"));
            }

            IntPtr attributeListSize = IntPtr.Zero;
            InitializeProcThreadAttributeList(
                IntPtr.Zero,
                1,
                0,
                ref attributeListSize);
            if (attributeListSize == IntPtr.Zero)
            {
                return RecordStartFailure(
                    result,
                    LastError("InitializeProcThreadAttributeList(size)"));
            }

            attributeList = Marshal.AllocHGlobal(attributeListSize);
            if (!InitializeProcThreadAttributeList(
                attributeList,
                1,
                0,
                ref attributeListSize))
            {
                return RecordStartFailure(
                    result,
                    LastError("InitializeProcThreadAttributeList"));
            }
            attributeListInitialized = true;

            int inheritedHandleBytes = checked(IntPtr.Size * 3);
            inheritedHandleArray = Marshal.AllocHGlobal(inheritedHandleBytes);
            Marshal.WriteIntPtr(inheritedHandleArray, 0, stdinHandle);
            Marshal.WriteIntPtr(inheritedHandleArray, IntPtr.Size, stdoutHandle);
            Marshal.WriteIntPtr(inheritedHandleArray, IntPtr.Size * 2, stderrHandle);

            if (!UpdateProcThreadAttribute(
                attributeList,
                0,
                new IntPtr(ProcThreadAttributeHandleList),
                inheritedHandleArray,
                new IntPtr(inheritedHandleBytes),
                IntPtr.Zero,
                IntPtr.Zero))
            {
                return RecordStartFailure(
                    result,
                    LastError("UpdateProcThreadAttribute(handle-list)"));
            }

            StartupInfoEx startup = new StartupInfoEx();
            startup.StartupInfo.Size = Marshal.SizeOf(typeof(StartupInfoEx));
            startup.StartupInfo.Flags = (int)StartfUseStdHandles;
            startup.StartupInfo.StdInput = stdinHandle;
            startup.StartupInfo.StdOutput = stdoutHandle;
            startup.StartupInfo.StdError = stderrHandle;
            startup.AttributeList = attributeList;

            environmentBlock = BuildChildEnvironmentBlock(jobName);
            StringBuilder commandLine = new StringBuilder(
                BuildWindowsCommandLine(executable, arguments));
            DateTime processStartUtc = DateTime.UtcNow;
            if (!CreateProcessW(
                executable,
                commandLine,
                IntPtr.Zero,
                IntPtr.Zero,
                true,
                CreateSuspended | CreateUnicodeEnvironment |
                    CreateNoWindow | ExtendedStartupInfoPresent,
                environmentBlock,
                workingDirectory,
                ref startup,
                out processInformation))
            {
                return RecordStartFailure(result, LastError("CreateProcessW"));
            }

            processCreated = true;
            Marshal.FreeHGlobal(environmentBlock);
            environmentBlock = IntPtr.Zero;
            processClock = Stopwatch.StartNew();
            result.ProcessStarted = true;
            result.ProcessId = unchecked((int)processInformation.ProcessId);
            result.StartedUtc = processStartUtc;
            result.TreeDrained = false;

            if (!AssignProcessToJobObject(jobHandle, processInformation.Process))
            {
                AddEngineError(result, LastError("AssignProcessToJobObject"));
                result.TreeDrained = StopRecordedTree(
                    jobHandle,
                    processInformation.Process,
                    false,
                    result);
                CaptureStartedProcessCompletion(
                    processInformation.Process,
                    processClock,
                    result);
                return result;
            }
            processAssigned = true;

            // The output-name race is now closed: both files are verified open,
            // the child is still suspended, and its Job assignment is complete.
            // Release the no-delete directory guard immediately before resume so
            // the deterministic child-swap test can rename the evidence directory
            // after the child starts. The already-open stdout/stderr handles keep
            // pointing at the original directory object.
            CloseOwnedHandle(ref evidenceDirectoryGuard);

            uint previousSuspendCount = ResumeThread(processInformation.Thread);
            if (previousSuspendCount == ResumeFailed)
            {
                AddEngineError(result, LastError("ResumeThread"));
                result.TreeDrained = StopRecordedTree(
                    jobHandle,
                    processInformation.Process,
                    true,
                    result);
                CaptureStartedProcessCompletion(
                    processInformation.Process,
                    processClock,
                    result);
                return result;
            }

            CloseOwnedHandle(ref processInformation.Thread);
            ReleaseProcessStartResources(
                ref stdinHandle,
                ref attributeList,
                ref attributeListInitialized,
                ref inheritedHandleArray);

            uint waitResult = WaitForSingleObject(
                processInformation.Process,
                checked((uint)timeoutMilliseconds));
            if (waitResult == WaitTimeout)
            {
                result.TimedOut = true;
                result.TreeDrained = StopRecordedTree(
                    jobHandle,
                    processInformation.Process,
                    processAssigned,
                    result);
            }
            else if (waitResult == WaitFailed)
            {
                AddEngineError(result, LastError("WaitForSingleObject(root)"));
                result.TreeDrained = StopRecordedTree(
                    jobHandle,
                    processInformation.Process,
                    processAssigned,
                    result);
            }
            else if (waitResult != WaitObject0)
            {
                AddEngineError(
                    result,
                    "WaitForSingleObject(root) returned unexpected status 0x" +
                    waitResult.ToString("X8", CultureInfo.InvariantCulture));
                result.TreeDrained = StopRecordedTree(
                    jobHandle,
                    processInformation.Process,
                    processAssigned,
                    result);
            }
            else
            {
                bool hadDescendant;
                if (!ObserveRootAccountingExit(
                    jobHandle,
                    processInformation.ProcessId,
                    result,
                    out hadDescendant))
                {
                    result.TreeDrained = StopRecordedTree(
                        jobHandle,
                        processInformation.Process,
                        processAssigned,
                        result);
                }
                else if (hadDescendant)
                {
                    result.HadLiveDescendantsAfterRootExit = true;
                    result.TreeDrained = StopRecordedTree(
                        jobHandle,
                        processInformation.Process,
                        processAssigned,
                        result);
                }
                else
                {
                    result.TreeDrained = true;
                }
            }

            CaptureStartedProcessCompletion(
                processInformation.Process,
                processClock,
                result);
            return result;
        }
        catch (Exception exception)
        {
            AddEngineError(
                result,
                exception.GetType().FullName + ": " + exception.Message);
            if (processCreated)
            {
                result.TreeDrained = StopRecordedTree(
                    jobHandle,
                    processInformation.Process,
                    processAssigned,
                    result);
                CaptureStartedProcessCompletion(
                    processInformation.Process,
                    processClock,
                    result);
            }
            return result;
        }
        finally
        {
            CloseOwnedHandle(ref processInformation.Thread);
            if ((!processCreated || result.TreeDrained) &&
                stdoutCreationIdentity != null &&
                stderrCreationIdentity != null)
            {
                ValidateOutputEvidenceBeforeClose(
                    result,
                    stdoutHandle,
                    stdoutPath,
                    stdoutCreationIdentity,
                    stderrHandle,
                    stderrPath,
                    stderrCreationIdentity,
                    outputEvidenceDirectoryIdentity);
            }
            ReleaseLaunchResources(
                ref stdoutHandle,
                ref stderrHandle,
                ref stdinHandle,
                ref attributeList,
                ref attributeListInitialized,
                ref inheritedHandleArray);
            CloseOwnedHandle(ref processInformation.Process);
            CloseOwnedHandle(ref jobHandle);
            CloseOwnedHandle(ref evidenceDirectoryGuard);
            if (environmentBlock != IntPtr.Zero)
            {
                Marshal.FreeHGlobal(environmentBlock);
                environmentBlock = IntPtr.Zero;
            }
        }
    }

    internal static string EncodeWindowsCommandLineArgument(string argument)
    {
        if (argument == null)
        {
            throw new ArgumentNullException("argument");
        }

        bool needsQuotes = argument.Length == 0;
        for (int index = 0; index < argument.Length && !needsQuotes; index++)
        {
            char value = argument[index];
            needsQuotes = value == '"' || char.IsWhiteSpace(value);
        }
        if (!needsQuotes)
        {
            return argument;
        }

        StringBuilder encoded = new StringBuilder(argument.Length + 2);
        encoded.Append('"');
        int pendingBackslashes = 0;
        for (int index = 0; index < argument.Length; index++)
        {
            char value = argument[index];
            if (value == '\\')
            {
                pendingBackslashes++;
                continue;
            }

            if (value == '"')
            {
                encoded.Append('\\', checked(pendingBackslashes * 2 + 1));
                encoded.Append('"');
                pendingBackslashes = 0;
                continue;
            }

            encoded.Append('\\', pendingBackslashes);
            pendingBackslashes = 0;
            encoded.Append(value);
        }

        encoded.Append('\\', checked(pendingBackslashes * 2));
        encoded.Append('"');
        return encoded.ToString();
    }

    private static string BuildWindowsCommandLine(
        string executable,
        string[] arguments)
    {
        StringBuilder commandLine = new StringBuilder();
        commandLine.Append(EncodeWindowsCommandLineArgument(executable));
        for (int index = 0; index < arguments.Length; index++)
        {
            commandLine.Append(' ');
            commandLine.Append(
                EncodeWindowsCommandLineArgument(arguments[index]));
        }

        if (commandLine.Length > 32766)
        {
            throw new ArgumentException(
                "The encoded process command line exceeds 32766 characters.",
                "arguments");
        }
        return commandLine.ToString();
    }

    private static IntPtr BuildChildEnvironmentBlock(string jobName)
    {
        if (String.IsNullOrWhiteSpace(jobName))
        {
            throw new ArgumentException("Named Job identity is required.", "jobName");
        }
        SortedDictionary<string, string> environment =
            new SortedDictionary<string, string>(
                StringComparer.OrdinalIgnoreCase);
        foreach (DictionaryEntry entry in Environment.GetEnvironmentVariables())
        {
            string key = Convert.ToString(
                entry.Key,
                CultureInfo.InvariantCulture);
            string value = Convert.ToString(
                entry.Value,
                CultureInfo.InvariantCulture);
            if (!String.Equals(
                key,
                GateJobEnvironmentVariable,
                StringComparison.OrdinalIgnoreCase))
            {
                environment[key] = value;
            }
        }
        environment[GateJobEnvironmentVariable] = jobName;

        StringBuilder block = new StringBuilder();
        foreach (KeyValuePair<string, string> entry in environment)
        {
            block.Append(entry.Key);
            block.Append('=');
            block.Append(entry.Value);
            block.Append('\0');
        }
        block.Append('\0');
        byte[] bytes = Encoding.Unicode.GetBytes(block.ToString());
        IntPtr nativeBlock = Marshal.AllocHGlobal(bytes.Length);
        try
        {
            Marshal.Copy(bytes, 0, nativeBlock, bytes.Length);
            return nativeBlock;
        }
        catch
        {
            Marshal.FreeHGlobal(nativeBlock);
            throw;
        }
    }

// END LOOP 3.3-A PROCESS PUBLIC API AND LAUNCH BUILDERS

// BEGIN LOOP 3.1-C READABLE HELPERS
    private static SecurityAttributes NewSecurityAttributes(bool inheritable)
    {
        SecurityAttributes attributes = new SecurityAttributes();
        attributes.Length = Marshal.SizeOf(typeof(SecurityAttributes));
        attributes.SecurityDescriptor = IntPtr.Zero;
        attributes.InheritHandle = inheritable ? 1 : 0;
        return attributes;
    }

    private static void RequirePlainAbsoluteFilePath(
        string path,
        string parameterName)
    {
        if (String.IsNullOrWhiteSpace(path) ||
            !Path.IsPathRooted(path) ||
            path.StartsWith(@"\\?\", StringComparison.OrdinalIgnoreCase) ||
            path.StartsWith(@"\\.\", StringComparison.OrdinalIgnoreCase))
        {
            throw new ArgumentException(
                parameterName + " must be an absolute, non-device path.",
                parameterName);
        }
        string fullPath = Path.GetFullPath(path);
        string leaf = Path.GetFileName(fullPath);
        if (!String.Equals(path, fullPath, StringComparison.OrdinalIgnoreCase) ||
            String.IsNullOrEmpty(leaf) ||
            leaf == "." ||
            leaf == ".." ||
            leaf.IndexOfAny(Path.GetInvalidFileNameChars()) >= 0 ||
            !String.Equals(
                leaf.TrimEnd(' ', '.'),
                leaf,
                StringComparison.Ordinal))
        {
            throw new ArgumentException(
                parameterName + " must end in one plain file-name component.",
                parameterName);
        }
    }

    private static PathIdentity GetReadableFileIdentityCore(
        string path,
        bool missingReturnsNull)
    {
        RequirePlainAbsoluteFilePath(path, "path");
        PathIdentity chainIdentity = missingReturnsNull
            ? TryGetPathIdentity(path, PathKind.File, true)
            : GetPathIdentity(path, PathKind.File, true);
        if (chainIdentity == null)
        {
            return null;
        }
        SecurityAttributes nonInheritable = NewSecurityAttributes(false);
        IntPtr fileHandle = CreateFileW(
            chainIdentity.FinalPath,
            GenericRead,
            FileShareRead | FileShareWrite,
            ref nonInheritable,
            OpenExisting,
            FileAttributeNormal | FileFlagOpenReparsePoint |
                FileFlagBackupSemantics,
            IntPtr.Zero);
        if (fileHandle == InvalidHandleValue)
        {
            int error = Marshal.GetLastWin32Error();
            if (missingReturnsNull &&
                (error == ErrorFileNotFound || error == ErrorPathNotFound))
            {
                return null;
            }
            throw JsonPathIdentityError(
                "CreateFileW(readable identity)",
                path,
                error);
        }
        try
        {
            PathIdentity identity = GetPathIdentityFromOpenHandle(
                fileHandle,
                PathKind.File);
            if ((identity.Attributes & FileAttributes.ReparsePoint) != 0 ||
                !SameStablePath(chainIdentity, identity))
            {
                throw new WinterGatePathIdentityException(
                    "path identity: readable file or ancestor changed: " + path);
            }
            return identity;
        }
        finally
        {
            CloseOwnedHandle(ref fileHandle);
        }
    }

// END LOOP 3.1-C READABLE HELPERS

// BEGIN LOOP 3.2-B JSON WRITER HELPERS
    private static void ValidateJsonPath(
        string path,
        PathIdentity expectedEvidenceDirectoryIdentity)
    {
        if (expectedEvidenceDirectoryIdentity == null ||
            String.IsNullOrWhiteSpace(expectedEvidenceDirectoryIdentity.FinalPath))
        {
            throw new ArgumentNullException(
                "expectedEvidenceDirectoryIdentity");
        }
        RequirePlainAbsoluteFilePath(path, "path");
        RequireLexicalDirectChild(
            path,
            expectedEvidenceDirectoryIdentity.FinalPath,
            "path");
    }

    private static IntPtr OpenPlainDirectEvidenceFile(
        string path,
        PathIdentity guardedEvidenceIdentity,
        SecurityAttributes nonInheritable,
        string label)
    {
        IntPtr handle = CreateFileW(
            path,
            FileReadAttributes,
            FileShareRead | FileShareWrite | FileShareDelete,
            ref nonInheritable,
            OpenExisting,
            FileAttributeNormal | FileFlagOpenReparsePoint,
            IntPtr.Zero);
        if (handle == InvalidHandleValue)
        {
            throw JsonPathIdentityError(
                "CreateFileW(" + label + ")",
                path,
                Marshal.GetLastWin32Error());
        }
        try
        {
            RequireDirectEvidenceChild(
                handle,
                path,
                guardedEvidenceIdentity,
                label);
            PathIdentity identity = GetPathIdentityFromOpenHandle(
                handle,
                PathKind.File);
            if ((identity.Attributes & FileAttributes.ReparsePoint) != 0)
            {
                throw new WinterGatePathIdentityException(
                    "path identity: " + label + " is a reparse point: " + path);
            }
            return handle;
        }
        catch
        {
            CloseOwnedHandle(ref handle);
            throw;
        }
    }

    private static void RenameOpenFileNoReplace(
        IntPtr sourceHandle,
        string absoluteTargetPath,
        PathIdentity expectedEvidenceDirectoryIdentity,
        string operation)
    {
        ValidateJsonPath(
            absoluteTargetPath,
            expectedEvidenceDirectoryIdentity);
        byte[] targetBytes = Encoding.Unicode.GetBytes(absoluteTargetPath);
        int rootDirectoryOffset = IntPtr.Size == 8 ? 8 : 4;
        int fileNameLengthOffset = IntPtr.Size == 8 ? 16 : 8;
        int fileNameOffset = IntPtr.Size == 8 ? 20 : 12;
        IntPtr information = Marshal.AllocHGlobal(
            checked(fileNameOffset + targetBytes.Length + 2));
        try
        {
            for (int index = 0;
                 index < fileNameOffset + targetBytes.Length + 2;
                 index++)
            {
                Marshal.WriteByte(information, index, 0);
            }
            Marshal.WriteByte(information, 0, 0);
            Marshal.WriteIntPtr(
                information,
                rootDirectoryOffset,
                IntPtr.Zero);
            Marshal.WriteInt32(
                information,
                fileNameLengthOffset,
                targetBytes.Length);
            Marshal.Copy(
                targetBytes,
                0,
                IntPtr.Add(information, fileNameOffset),
                targetBytes.Length);
            if (!SetFileInformationByHandle(
                sourceHandle,
                FileRenameInfo,
                information,
                checked((uint)(fileNameOffset + targetBytes.Length + 2))))
            {
                throw new IOException(
                    LastError("SetFileInformationByHandle(" + operation + ")"));
            }
        }
        finally
        {
            Marshal.FreeHGlobal(information);
        }
    }

    private static PathIdentity OpenVerifiedEvidenceGuard(
        PathIdentity expectedEvidenceDirectoryIdentity,
        string requestedPath,
        ref IntPtr evidenceDirectoryGuard)
    {
        SecurityAttributes nonInheritable = NewSecurityAttributes(false);
        evidenceDirectoryGuard = CreateFileW(
            expectedEvidenceDirectoryIdentity.FinalPath,
            FileReadAttributes | DeleteAccess,
            FileShareRead | FileShareWrite,
            ref nonInheritable,
            OpenExisting,
            FileFlagBackupSemantics | FileFlagOpenReparsePoint,
            IntPtr.Zero);
        if (evidenceDirectoryGuard == InvalidHandleValue)
        {
            int error = Marshal.GetLastWin32Error();
            throw JsonPathIdentityError(
                "CreateFileW(JSON evidence-directory guard)",
                expectedEvidenceDirectoryIdentity.FinalPath,
                error);
        }
        PathIdentity guardedEvidenceIdentity = GetPathIdentityFromOpenHandle(
            evidenceDirectoryGuard,
            PathKind.Directory);
        if ((guardedEvidenceIdentity.Attributes & FileAttributes.ReparsePoint) != 0 ||
            !SameStablePath(
                expectedEvidenceDirectoryIdentity,
                guardedEvidenceIdentity))
        {
            throw new WinterGatePathIdentityException(
                "path identity: evidence directory changed before JSON access: " +
                requestedPath);
        }
        return guardedEvidenceIdentity;
    }

    private static byte[] EncodeUtf8Json(string json)
    {
        if (json == null)
        {
            throw new ArgumentNullException("json");
        }
        return new UTF8Encoding(false, true).GetBytes(
            json + Environment.NewLine);
    }

    private static void WriteAllAndFlush(
        IntPtr fileHandle,
        byte[] bytes,
        string operation)
    {
        GCHandle pinnedBytes = default(GCHandle);
        bool bytesArePinned = false;
        try
        {
            if (bytes.Length != 0)
            {
                pinnedBytes = GCHandle.Alloc(bytes, GCHandleType.Pinned);
                bytesArePinned = true;
                int offset = 0;
                while (offset < bytes.Length)
                {
                    uint written;
                    if (!WriteFile(
                        fileHandle,
                        IntPtr.Add(pinnedBytes.AddrOfPinnedObject(), offset),
                        checked((uint)(bytes.Length - offset)),
                        out written,
                        IntPtr.Zero))
                    {
                        throw new IOException(
                            LastError("WriteFile(" + operation + ")"));
                    }
                    if (written == 0)
                    {
                        throw new IOException(
                            "WriteFile(" + operation +
                            ") made no forward progress.");
                    }
                    offset = checked(offset + checked((int)written));
                }
            }
            if (!FlushFileBuffers(fileHandle))
            {
                throw new IOException(
                    LastError("FlushFileBuffers(" + operation + ")"));
            }
        }
        finally
        {
            if (bytesArePinned)
            {
                pinnedBytes.Free();
            }
        }
    }

// END LOOP 3.2-B JSON WRITER HELPERS
// BEGIN LOOP 3.3-B PROCESS ARGUMENT VALIDATION
    private static void ValidateProcessArguments(
        string executable,
        string[] arguments,
        string workingDirectory,
        string stdoutPath,
        string stderrPath,
        int timeoutMilliseconds,
        PathIdentity expectedEvidenceDirectoryIdentity)
    {
        if (String.IsNullOrWhiteSpace(executable))
        {
            throw new ArgumentException("Executable is required.", "executable");
        }
        if (arguments == null)
        {
            throw new ArgumentNullException("arguments");
        }
        for (int index = 0; index < arguments.Length; index++)
        {
            if (arguments[index] == null)
            {
                throw new ArgumentException(
                    "Process arguments cannot contain null.",
                    "arguments");
            }
        }
        if (String.IsNullOrWhiteSpace(workingDirectory))
        {
            throw new ArgumentException(
                "Working directory is required.",
                "workingDirectory");
        }
        if (expectedEvidenceDirectoryIdentity == null ||
            String.IsNullOrWhiteSpace(expectedEvidenceDirectoryIdentity.FinalPath))
        {
            throw new ArgumentNullException(
                "expectedEvidenceDirectoryIdentity");
        }
        if (String.IsNullOrWhiteSpace(stdoutPath))
        {
            throw new ArgumentException("stdoutPath is required.", "stdoutPath");
        }
        if (String.IsNullOrWhiteSpace(stderrPath))
        {
            throw new ArgumentException("stderrPath is required.", "stderrPath");
        }
        if (String.Equals(stdoutPath, stderrPath, StringComparison.OrdinalIgnoreCase))
        {
            throw new ArgumentException(
                "stdoutPath and stderrPath must differ.",
                "stderrPath");
        }
        if (timeoutMilliseconds <= 0)
        {
            throw new ArgumentOutOfRangeException(
                "timeoutMilliseconds",
                "Process timeout must be positive.");
        }

        RequireLexicalDirectChild(
            stdoutPath,
            expectedEvidenceDirectoryIdentity.FinalPath,
            "stdoutPath");
        RequireLexicalDirectChild(
            stderrPath,
            expectedEvidenceDirectoryIdentity.FinalPath,
            "stderrPath");

        BuildWindowsCommandLine(executable, arguments);
    }

// END LOOP 3.3-B PROCESS ARGUMENT VALIDATION

// BEGIN LOOP 3.2-C JSON DIRECT-CHILD HELPERS
    private static void RequireLexicalDirectChild(
        string candidate,
        string expectedParent,
        string parameterName)
    {
        if (!Path.IsPathRooted(candidate) ||
            candidate.StartsWith(@"\\?\", StringComparison.OrdinalIgnoreCase) ||
            candidate.StartsWith(@"\\.\", StringComparison.OrdinalIgnoreCase))
        {
            throw new ArgumentException(
                parameterName +
                " must be an absolute, non-device path.",
                parameterName);
        }
        string fullCandidate = Path.GetFullPath(candidate);
        string actualParent = Path.GetDirectoryName(fullCandidate);
        string leaf = Path.GetFileName(fullCandidate);
        if (!String.Equals(
                candidate,
                fullCandidate,
                StringComparison.OrdinalIgnoreCase) ||
            String.IsNullOrEmpty(actualParent) ||
            String.IsNullOrEmpty(leaf) ||
            leaf == "." ||
            leaf == ".." ||
            leaf.IndexOfAny(Path.GetInvalidFileNameChars()) >= 0 ||
            !String.Equals(
                leaf.TrimEnd(' ', '.'),
                leaf,
                StringComparison.Ordinal) ||
            !String.Equals(
                actualParent.TrimEnd(Path.DirectorySeparatorChar),
                Path.GetFullPath(expectedParent).TrimEnd(Path.DirectorySeparatorChar),
                StringComparison.OrdinalIgnoreCase))
        {
            throw new ArgumentException(
                parameterName +
                " must name a direct child of the pinned evidence directory.",
                parameterName);
        }
    }

    private static void RequireDirectEvidenceChild(
        IntPtr fileHandle,
        string requestedPath,
        PathIdentity expectedParent,
        string streamName)
    {
        PathIdentity openedFile = GetPathIdentityFromOpenHandle(
            fileHandle,
            PathKind.File);
        string openedParent = Path.GetDirectoryName(openedFile.FinalPath);
        string openedLeaf = Path.GetFileName(openedFile.FinalPath);
        string requestedLeaf = Path.GetFileName(Path.GetFullPath(requestedPath));
        if (String.IsNullOrEmpty(openedParent) ||
            !String.Equals(
                openedParent.TrimEnd(Path.DirectorySeparatorChar),
                expectedParent.FinalPath.TrimEnd(Path.DirectorySeparatorChar),
                StringComparison.OrdinalIgnoreCase) ||
            !String.Equals(
                openedLeaf,
                requestedLeaf,
                StringComparison.OrdinalIgnoreCase))
        {
            throw new WinterGatePathIdentityException(
                "path identity: " + streamName +
                " handle did not open inside the pinned evidence directory.");
        }
    }

// END LOOP 3.2-C JSON DIRECT-CHILD HELPERS
// BEGIN LOOP 3.3-C PROCESS FAILURE AND DRAIN HELPERS
    private static BoundedProcessResult RecordStartFailure(
        BoundedProcessResult result,
        string error)
    {
        AddEngineError(result, error);
        result.ProcessStarted = false;
        result.ProcessId = null;
        result.StartedUtc = null;
        result.EndedUtc = null;
        result.ElapsedMilliseconds = null;
        result.ExitCode = null;
        result.TimedOut = false;
        result.TreeDrained = true;
        result.HadLiveDescendantsAfterRootExit = false;
        return result;
    }

    private static bool StopRecordedTree(
        IntPtr job,
        IntPtr process,
        bool processAssigned,
        BoundedProcessResult result)
    {
        if (processAssigned &&
            job != IntPtr.Zero &&
            !TerminateJobObject(job, ForcedExitCode))
        {
            AddEngineError(result, LastError("TerminateJobObject"));
        }

        uint initialProcessState = WaitForSingleObject(process, 0);
        if (initialProcessState != WaitObject0)
        {
            if (!TerminateProcess(process, ForcedExitCode))
            {
                int terminateError = Marshal.GetLastWin32Error();
                if (WaitForSingleObject(process, 0) != WaitObject0)
                {
                    AddEngineError(
                        result,
                        Win32Error("TerminateProcess", terminateError));
                }
            }
        }

        uint rootWait = WaitForSingleObject(
            process,
            CleanupTimeoutMilliseconds);
        bool rootGone = rootWait == WaitObject0;
        if (!rootGone)
        {
            if (rootWait == WaitFailed)
            {
                AddEngineError(
                    result,
                    LastError("WaitForSingleObject(cleanup-root)"));
            }
            else
            {
                AddEngineError(
                    result,
                    "Recorded root process did not exit within cleanup bound.");
            }
        }

        bool jobDrained = DrainJob(job, result);
        return rootGone && jobDrained;
    }

    private static bool DrainJob(
        IntPtr job,
        BoundedProcessResult result)
    {
        Stopwatch cleanupClock = Stopwatch.StartNew();
        while (true)
        {
            uint activeProcesses;
            if (!TryGetActiveProcessCount(job, out activeProcesses, result))
            {
                return false;
            }
            if (activeProcesses == 0)
            {
                return true;
            }
            if (cleanupClock.ElapsedMilliseconds >= CleanupTimeoutMilliseconds)
            {
                AddEngineError(
                    result,
                    "Job Object still had " +
                    activeProcesses.ToString(CultureInfo.InvariantCulture) +
                    " active process(es) after cleanup bound.");
                return false;
            }
            Thread.Sleep(CleanupPollMilliseconds);
        }
    }

    private static bool TryGetActiveProcessCount(
        IntPtr job,
        out uint activeProcesses,
        BoundedProcessResult result)
    {
        activeProcesses = 0;
        if (job == IntPtr.Zero)
        {
            AddEngineError(result, "Job Object handle is unavailable.");
            return false;
        }

        JobObjectBasicAccountingInformationData accounting =
            new JobObjectBasicAccountingInformationData();
        if (!QueryInformationJobObject(
            job,
            JobObjectBasicAccountingInformation,
            out accounting,
            Marshal.SizeOf(typeof(JobObjectBasicAccountingInformationData)),
            IntPtr.Zero))
        {
            AddEngineError(
                result,
                LastError("QueryInformationJobObject"));
            return false;
        }
        activeProcesses = accounting.ActiveProcesses;
        return true;
    }

// END LOOP 3.3-C PROCESS FAILURE AND DRAIN HELPERS

// BEGIN LOOP 3.5-A AUTHORITATIVE JOB-ZERO REPLACEMENT
    private static bool ObserveRootAccountingExit(
        IntPtr job,
        uint rootProcessId,
        BoundedProcessResult result,
        out bool hadDescendant)
    {
        hadDescendant = false;
        Stopwatch accountingClock = Stopwatch.StartNew();
        while (true)
        {
            ulong[] processIds;
            if (!TryGetJobProcessIds(job, result, out processIds))
            {
                return false;
            }

            bool rootStillListed = false;
            for (int index = 0; index < processIds.Length; index++)
            {
                if (processIds[index] == rootProcessId)
                {
                    rootStillListed = true;
                }
                else
                {
                    bool isRunning;
                    if (!TryIsProcessRunning(processIds[index], result, out isRunning))
                    {
                        return false;
                    }
                    if (isRunning)
                    {
                        hadDescendant = true;
                        return true;
                    }
                }
            }

            if (!rootStillListed)
            {
                uint activeProcesses;
                if (!TryGetActiveProcessCount(
                    job,
                    out activeProcesses,
                    result))
                {
                    return false;
                }
                if (activeProcesses == 0)
                {
                    return true;
                }
                hadDescendant = true;
                return true;
            }
            if (accountingClock.ElapsedMilliseconds >= CleanupTimeoutMilliseconds)
            {
                AddEngineError(
                    result,
                    "Signaled root process remained in the Job Object process list " +
                    "after the accounting bound.");
                return false;
            }
            Thread.Sleep(CleanupPollMilliseconds);
        }
    }

// END LOOP 3.5-A AUTHORITATIVE JOB-ZERO REPLACEMENT

// BEGIN LOOP 3.3-D PROCESS OBSERVATION AND RELEASE HELPERS
    private static bool TryGetJobProcessIds(
        IntPtr job,
        BoundedProcessResult result,
        out ulong[] processIds)
    {
        processIds = new ulong[0];
        int capacity = 16;
        while (capacity <= 65536)
        {
            int byteCount = checked(8 + capacity * IntPtr.Size);
            IntPtr buffer = Marshal.AllocHGlobal(byteCount);
            try
            {
                for (int offset = 0; offset < byteCount; offset += 4)
                {
                    Marshal.WriteInt32(buffer, offset, 0);
                }
                if (QueryInformationJobObjectBuffer(
                    job,
                    JobObjectBasicProcessIdList,
                    buffer,
                    byteCount,
                    IntPtr.Zero))
                {
                    int count = Marshal.ReadInt32(buffer, 4);
                    if (count < 0 || count > capacity)
                    {
                        AddEngineError(
                            result,
                            "Job Object returned an invalid process-ID count.");
                        return false;
                    }
                    processIds = new ulong[count];
                    for (int index = 0; index < count; index++)
                    {
                        int offset = 8 + index * IntPtr.Size;
                        processIds[index] = IntPtr.Size == 8
                            ? unchecked((ulong)Marshal.ReadInt64(buffer, offset))
                            : unchecked((uint)Marshal.ReadInt32(buffer, offset));
                    }
                    return true;
                }

                int error = Marshal.GetLastWin32Error();
                if (error != ErrorMoreData)
                {
                    AddEngineError(
                        result,
                        Win32Error("QueryInformationJobObject(process-list)", error));
                    return false;
                }
                int assigned = Marshal.ReadInt32(buffer, 0);
                capacity = Math.Max(capacity * 2, assigned);
            }
            finally
            {
                Marshal.FreeHGlobal(buffer);
            }
        }

        AddEngineError(
            result,
            "Job Object process list exceeded the bounded capacity.");
        return false;
    }

    private static bool TryIsProcessRunning(
        ulong processId,
        BoundedProcessResult result,
        out bool isRunning)
    {
        isRunning = false;
        if (processId > UInt32.MaxValue)
        {
            AddEngineError(result, "Job Object returned an invalid process ID.");
            return false;
        }
        IntPtr process = OpenProcess(
            SynchronizeAccess,
            false,
            unchecked((uint)processId));
        if (process == IntPtr.Zero)
        {
            int error = Marshal.GetLastWin32Error();
            if (error == ErrorInvalidParameter)
            {
                return true;
            }
            AddEngineError(
                result,
                Win32Error("OpenProcess(job-descendant)", error));
            return false;
        }
        try
        {
            uint wait = WaitForSingleObject(process, 0);
            if (wait == WaitObject0)
            {
                return true;
            }
            if (wait == WaitTimeout)
            {
                isRunning = true;
                return true;
            }
            AddEngineError(
                result,
                wait == WaitFailed
                    ? LastError("WaitForSingleObject(job-descendant)")
                    : "Unexpected Job descendant wait status 0x" +
                        wait.ToString("X8", CultureInfo.InvariantCulture));
            return false;
        }
        finally
        {
            CloseHandle(process);
        }
    }

    private static void CaptureStartedProcessCompletion(
        IntPtr process,
        Stopwatch processClock,
        BoundedProcessResult result)
    {
        result.EndedUtc = DateTime.UtcNow;
        result.ElapsedMilliseconds =
            processClock == null ? 0L : processClock.ElapsedMilliseconds;
        result.ExitCode = -1;

        uint nativeExitCode;
        if (!GetExitCodeProcess(process, out nativeExitCode))
        {
            AddEngineError(result, LastError("GetExitCodeProcess"));
            return;
        }
        result.ExitCode = unchecked((int)nativeExitCode);
    }

    private static void ValidateOutputEvidenceBeforeClose(
        BoundedProcessResult result,
        IntPtr stdoutHandle,
        string stdoutPath,
        PathIdentity stdoutCreationIdentity,
        IntPtr stderrHandle,
        string stderrPath,
        PathIdentity stderrCreationIdentity,
        PathIdentity expectedEvidenceDirectoryIdentity)
    {
        List<string> errors = new List<string>();
        ValidateOutputEvidenceStream(
            "stdout",
            stdoutHandle,
            stdoutPath,
            stdoutCreationIdentity,
            expectedEvidenceDirectoryIdentity,
            errors);
        ValidateOutputEvidenceStream(
            "stderr",
            stderrHandle,
            stderrPath,
            stderrCreationIdentity,
            expectedEvidenceDirectoryIdentity,
            errors);
        result.OutputEvidenceValid = errors.Count == 0;
        result.OutputEvidenceError = errors.Count == 0
            ? null
            : String.Join(" | ", errors.ToArray());
    }

    private static void ValidateOutputEvidenceStream(
        string label,
        IntPtr openHandle,
        string fixedPath,
        PathIdentity creationIdentity,
        PathIdentity expectedEvidenceDirectoryIdentity,
        List<string> errors)
    {
        try
        {
            PathIdentity currentOpenIdentity =
                GetPathIdentityFromOpenHandle(openHandle, PathKind.File);
            if (!SameStablePath(creationIdentity, currentOpenIdentity))
            {
                errors.Add(
                    label + " open-handle identity changed after process drain.");
            }
        }
        catch (Exception exception)
        {
            errors.Add(
                label + " open-handle identity validation failed: " +
                exception.GetType().FullName + ": " + exception.Message);
        }

        try
        {
            SecurityAttributes nonInheritable = NewSecurityAttributes(false);
            IntPtr currentFixedHandle = CreateFileW(
                fixedPath,
                FileReadAttributes,
                FileShareRead | FileShareWrite | FileShareDelete,
                ref nonInheritable,
                OpenExisting,
                FileAttributeNormal | FileFlagOpenReparsePoint,
                IntPtr.Zero);
            if (currentFixedHandle == InvalidHandleValue)
            {
                throw JsonPathIdentityError(
                    "CreateFileW(" + label + " fixed-leaf reopen)",
                    fixedPath,
                    Marshal.GetLastWin32Error());
            }
            try
            {
                RequireDirectEvidenceChild(
                    currentFixedHandle,
                    fixedPath,
                    expectedEvidenceDirectoryIdentity,
                    label + " fixed leaf");
                PathIdentity currentFixedIdentity =
                    GetPathIdentityFromOpenHandle(
                        currentFixedHandle,
                        PathKind.File);
                if (!SameStablePath(creationIdentity, currentFixedIdentity))
                {
                    errors.Add(
                        label +
                        " fixed-leaf identity changed after process drain.");
                }
            }
            finally
            {
                CloseOwnedHandle(ref currentFixedHandle);
            }
        }
        catch (Exception exception)
        {
            errors.Add(
                label + " fixed-leaf identity validation failed: " +
                exception.GetType().FullName + ": " + exception.Message);
        }
    }

    private static void ReleaseProcessStartResources(
        ref IntPtr stdinHandle,
        ref IntPtr attributeList,
        ref bool attributeListInitialized,
        ref IntPtr inheritedHandleArray)
    {
        if (attributeListInitialized && attributeList != IntPtr.Zero)
        {
            DeleteProcThreadAttributeList(attributeList);
            attributeListInitialized = false;
        }
        if (attributeList != IntPtr.Zero)
        {
            Marshal.FreeHGlobal(attributeList);
            attributeList = IntPtr.Zero;
        }
        if (inheritedHandleArray != IntPtr.Zero)
        {
            Marshal.FreeHGlobal(inheritedHandleArray);
            inheritedHandleArray = IntPtr.Zero;
        }
        CloseOwnedHandle(ref stdinHandle);
    }

    private static void ReleaseLaunchResources(
        ref IntPtr stdoutHandle,
        ref IntPtr stderrHandle,
        ref IntPtr stdinHandle,
        ref IntPtr attributeList,
        ref bool attributeListInitialized,
        ref IntPtr inheritedHandleArray)
    {
        ReleaseProcessStartResources(
            ref stdinHandle,
            ref attributeList,
            ref attributeListInitialized,
            ref inheritedHandleArray);
        CloseOwnedHandle(ref stdoutHandle);
        CloseOwnedHandle(ref stderrHandle);
    }

// END LOOP 3.3-D PROCESS OBSERVATION AND RELEASE HELPERS

// BEGIN LOOP 3.1-D SHARED HANDLE AND ERROR HELPERS
    private static void CloseOwnedHandle(ref IntPtr handle)
    {
        if (handle != IntPtr.Zero && handle != InvalidHandleValue)
        {
            CloseHandle(handle);
        }
        handle = IntPtr.Zero;
    }

    private static void AddEngineError(
        BoundedProcessResult result,
        string error)
    {
        if (String.IsNullOrEmpty(error))
        {
            return;
        }
        if (String.IsNullOrEmpty(result.StartError))
        {
            result.StartError = error;
        }
        else
        {
            result.StartError = result.StartError + " | " + error;
        }
    }

    private static string LastError(string operation)
    {
        return Win32Error(operation, Marshal.GetLastWin32Error());
    }

    private static WinterGatePathIdentityException JsonPathIdentityError(
        string operation,
        string path,
        int error)
    {
        Win32Exception inner = new Win32Exception(error);
        return new WinterGatePathIdentityException(
            "path identity: " + operation + " failed for '" + path +
            "' with Win32 error " +
            error.ToString(CultureInfo.InvariantCulture) + ": " +
            inner.Message,
            error,
            inner);
    }

    private static string Win32Error(string operation, int error)
    {
        return operation + " failed with Win32 error " +
            error.ToString(CultureInfo.InvariantCulture) + ": " +
            new Win32Exception(error).Message;
    }
// END LOOP 3.1-D SHARED HANDLE AND ERROR HELPERS
// END PROCESS ENGINE
```

Loop 3.3 uses this exact temporary accounting method between `LOOP 3.3-C`
and `LOOP 3.3-D`. It keeps the first public process slice independently
compilable while leaving Loop 3.5's authoritative-zero behavior RED. Loop 3.5
deletes this complete marked method before inserting `LOOP 3.5-A` at the same
anchor.

```csharp
// BEGIN LOOP 3.3 TEMPORARY ROOT-SNAPSHOT ACCOUNTING
    private static bool ObserveRootAccountingExit(
        IntPtr job,
        uint rootProcessId,
        BoundedProcessResult result,
        out bool hadDescendant)
    {
        hadDescendant = false;
        Stopwatch accountingClock = Stopwatch.StartNew();
        while (true)
        {
            ulong[] processIds;
            if (!TryGetJobProcessIds(job, result, out processIds))
            {
                return false;
            }

            bool rootStillListed = false;
            for (int index = 0; index < processIds.Length; index++)
            {
                if (processIds[index] == rootProcessId)
                {
                    rootStillListed = true;
                }
                else
                {
                    bool isRunning;
                    if (!TryIsProcessRunning(
                        processIds[index],
                        result,
                        out isRunning))
                    {
                        return false;
                    }
                    if (isRunning)
                    {
                        hadDescendant = true;
                        return true;
                    }
                }
            }

            if (!rootStillListed)
            {
                return true;
            }
            if (accountingClock.ElapsedMilliseconds >=
                CleanupTimeoutMilliseconds)
            {
                AddEngineError(
                    result,
                    "Signaled root process remained in the Job Object process " +
                    "list after the accounting bound.");
                return false;
            }
            Thread.Sleep(CleanupPollMilliseconds);
        }
    }
// END LOOP 3.3 TEMPORARY ROOT-SNAPSHOT ACCOUNTING
```

The two native JSON APIs are the only JSON filesystem writers.
`WriteUtf8JsonCreateNew` first checks the requested name is a direct lexical
child, then opens the pinned evidence directory with
`FILE_FLAG_OPEN_REPARSE_POINT` and without `FILE_SHARE_DELETE`. While that
no-delete guard is held it reconstructs the open directory identity, requires
`SameStablePath`, creates the requested leaf with `CREATE_NEW` and no sharing,
verifies the opened file handle's final parent and leaf against the guard,
writes every UTF-8 byte without a BOM, and flushes before releasing either
handle. `WriteOwnedSummaryUtf8Json` uses the same pinned directory and holds its
create-new staging leaf, and any pre-existing plain summary opened for
quarantine, without delete sharing through flush and handle-based no-replace
rename. An invalid/missing/reparse-swapped evidence identity fails before file
creation; an ancestor race that resolves a new leaf elsewhere is caught from
the opened handle before the first byte is written. Every pinned buffer and
native handle is released in one `finally`. PowerShell never reopens a written
path.

`StartError` is null for a clean launch and clean observation. It is non-null
for a native launch/setup/observation error. Only failures before
`CreateProcessW` succeeds have `ProcessStarted=false` and null PID/time/exit
fields. Once `CreateProcessW` succeeds, the method always fills PID,
`StartedUtc`, `EndedUtc`, `ElapsedMilliseconds`, and `ExitCode`; an
Assign/Resume failure retains `StartError`, kills only the recorded root/job,
and returns the observed `TreeDrained` value. `TimedOut` and
`HadLiveDescendantsAfterRootExit` are independent failure signals and take
classification precedence over a secondary cleanup error.

In the Task 2 script body, delete the complete Task 2
`Invoke-WinterInterludeGate` definition, from its function declaration through
its matching closing brace. Leave Task 2's existing top-level
`try { Invoke-WinterInterludeGate ... } catch { ... }` statement untouched.
Insert every helper below followed by the one new complete
`Invoke-WinterInterludeGate` definition immediately before that top-level
`try`. Do not paste this block inside the deleted function: doing so would
create a nested definition and leave the Task 2 boundary active. Task 4 expands
the Structural manifest and Task 5 expands the postcondition dispatcher;
neither adds another executor.

Use the PowerShell BEGIN/END comments as literal copy boundaries:

- Loop 3.3 copies `LOOP 3.3-P1`, `3.3-P2`, `3.3-P3`, and `3.3-P4` in
  their printed order, with three exact stage substitutions. In P1, replace the
  printed final `Resolve-PythonExecutable` function with the temporary resolver
  below. In P2, replace only the printed final `$executableIdentity` assignment
  with the temporary executable baseline below. In P4, insert the temporary
  early Python-resolution region immediately after `$script:SavedirsIdentity`,
  omit the printed final in-`try` resolver line, and replace the final
  `LOOP 3.5-P1` region with the temporary pre-write region below. Between P1 and
  P2, insert the temporary identity block instead of any `LOOP 3.4-P*` region.
- Loop 3.4 deletes the temporary resolver, executable baseline, early
  Python-resolution, and identity blocks; restores the printed final P1/P2/P4
  lines at those exact anchors; inserts `LOOP 3.4-P1` between P1 and P2,
  `LOOP 3.4-P2` between P2 and P3, and `LOOP 3.4-P3` between P3 and P4. This
  recreates the exact printed final order.
- Loop 3.5 deletes the temporary pre-write region inside P4 and copies the
  final `LOOP 3.5-P1` region at the same anchor.

Copy the boundary comments themselves. These are exact replacements; do not
merge the temporary and final variants or infer a dependency closure from the
full catalog.

```powershell
# BEGIN LOOP 3.3 TEMPORARY PYTHON RESOLVER
function Resolve-PythonExecutable {
    $command = Get-Command python.exe -CommandType Application -ErrorAction Stop |
        Select-Object -First 1
    if ($null -eq $command -or [string]::IsNullOrWhiteSpace($command.Source)) {
        throw 'python.exe did not resolve to an application.'
    }
    [WinterGate.Native]::GetPathIdentity(
        [IO.Path]::GetFullPath($command.Source),
        [WinterGate.PathKind]::File,
        $true)
}
# END LOOP 3.3 TEMPORARY PYTHON RESOLVER
```

Inside `LOOP 3.3-P2`, replace only the final catalog's readable executable
assignment inside its existing `try` with this temporary assignment. Retain the
existing catch and manifest-context wrapper unchanged.

```powershell
        # BEGIN LOOP 3.3 TEMPORARY EXECUTABLE BASELINE
        $executableIdentity = [WinterGate.Native]::GetPathIdentity(
            $Executable,
            [WinterGate.PathKind]::File,
            $true)
        # END LOOP 3.3 TEMPORARY EXECUTABLE BASELINE
```

Inside `LOOP 3.3-P4`, insert this region immediately after the
`$script:SavedirsIdentity = $runTree.SavedirsIdentity` line. In Loop 3.3 do not
also copy the printed final `$script:PythonIdentity = Resolve-PythonExecutable`
line from inside the initialized `try`.

```powershell
    # BEGIN LOOP 3.3 TEMPORARY EARLY PYTHON RESOLUTION
    $script:PythonIdentity = Resolve-PythonExecutable
    # END LOOP 3.3 TEMPORARY EARLY PYTHON RESOLUTION
```

```powershell
# BEGIN LOOP 3.3 TEMPORARY IDENTITY LAYER
function Get-ProjectHeadState {
    $dotGit = Join-Path $script:ProjectIdentity.FinalPath '.git'
    if ([IO.File]::Exists($dotGit) -or [IO.Directory]::Exists($dotGit)) {
        throw 'git identity layer not implemented'
    }
    [pscustomobject][ordered]@{
        Commit = $null
        DirectoryIdentities = [object[]]@()
        FileIdentities = [object[]]@()
    }
}

function Assert-GitCommitOverride {
    param([AllowNull()][string]$Commit)
}

function Assert-ProjectHeadCommit {
}

function Assert-ProjectRootIdentity {
}

function Assert-RunTreeDirectoryIdentities {
    foreach ($identity in @(
        $script:RunRootIdentity,
        $script:EvidenceIdentity,
        $script:SavedirsIdentity)) {
        Assert-GatePathState `
            -ExpectedIdentity $identity `
            -Label "base gate directory '$($identity.FinalPath)'" | Out-Null
    }
}

function Assert-AllGateDirectoryIdentities {
    foreach ($identity in $script:GateDirectoryIdentities) {
        Assert-GatePathState `
            -ExpectedIdentity $identity `
            -Label "registered gate directory '$($identity.FinalPath)'" |
            Out-Null
    }
}

function Assert-NonEvidenceGateDirectoryIdentities {
    foreach ($identity in $script:GateDirectoryIdentities) {
        if ([WinterGate.Native]::SameObject(
            $identity,
            $script:EvidenceIdentity)) {
            continue
        }
        Assert-GatePathState `
            -ExpectedIdentity $identity `
            -Label "registered pre-write gate directory '$($identity.FinalPath)'" |
            Out-Null
    }
}

function Get-GateStepDependencyValidationError {
    param([Parameter(Mandatory = $true)]$Step)
    return $null
}
# END LOOP 3.3 TEMPORARY IDENTITY LAYER
```

Inside `LOOP 3.3-P4` use this exact temporary region in place of the printed
`LOOP 3.5-P1` region. Loop 3.5 replaces the whole marked region, including its
comments.

```powershell
# BEGIN LOOP 3.3 TEMPORARY PRE-WRITE RECHECK
    Assert-AllGateDirectoryIdentities
# END LOOP 3.3 TEMPORARY PRE-WRITE RECHECK
```

```powershell
# BEGIN LOOP 3.3-P1 HOST AND PROJECT FILE HELPERS
function Resolve-PythonExecutable {
    $command = Get-Command python.exe -CommandType Application -ErrorAction Stop |
        Select-Object -First 1
    if ($null -eq $command -or [string]::IsNullOrWhiteSpace($command.Source)) {
        throw 'python.exe did not resolve to an application.'
    }
    [WinterGate.Native]::GetReadableFileIdentity(
        [IO.Path]::GetFullPath($command.Source))
}

function Get-ExpectedProjectFilePath {
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [string]$ResolvedProjectRoot,
        [Parameter(Mandatory = $true, Position = 1)]
        [string]$RelativePath
    )
    if ([string]::IsNullOrWhiteSpace($RelativePath) -or
        [IO.Path]::IsPathRooted($RelativePath) -or
        $RelativePath.StartsWith('\\?\') -or
        $RelativePath.StartsWith('\\.\') -or
        $RelativePath.IndexOfAny([IO.Path]::GetInvalidPathChars()) -ge 0 -or
        [Management.Automation.WildcardPattern]::ContainsWildcardCharacters(
            $RelativePath)) {
        throw "Invalid fixed project-relative path: $RelativePath"
    }
    foreach ($component in $RelativePath.Split(@('\', '/'))) {
        if ([string]::IsNullOrWhiteSpace($component) -or
            $component -eq '.' -or $component -eq '..') {
            throw "Invalid fixed project-relative component: $RelativePath"
        }
    }
    $candidate = [IO.Path]::GetFullPath(
        [IO.Path]::Combine($ResolvedProjectRoot, $RelativePath))
    $prefix = $ResolvedProjectRoot.TrimEnd('\') + '\'
    if (-not $candidate.StartsWith(
        $prefix, [StringComparison]::OrdinalIgnoreCase)) {
        throw "Fixed project path escaped ProjectRoot: $RelativePath"
    }
    $candidate
}

# END LOOP 3.3-P1 HOST AND PROJECT FILE HELPERS

# BEGIN LOOP 3.4-P1 FINAL GIT IDENTITY LAYER
function Remove-GitTerminalNewline {
    param(
        [Parameter(Mandatory = $true)][string]$Text,
        [Parameter(Mandatory = $true)][string]$Label
    )
    $value = if ($Text.EndsWith("`r`n", [StringComparison]::Ordinal)) {
        $Text.Substring(0, $Text.Length - 2)
    } elseif ($Text.EndsWith("`n", [StringComparison]::Ordinal)) {
        $Text.Substring(0, $Text.Length - 1)
    } else { $Text }
    if ($value.IndexOf("`r") -ge 0 -or $value.IndexOf("`n") -ge 0 -or
        [string]::IsNullOrWhiteSpace($value)) {
        throw "$Label must contain exactly one non-empty line."
    }
    $value
}

function Read-VerifiedGateText {
    param(
        [Parameter(Mandatory = $true)][string]$Path,
        [Parameter(Mandatory = $true)]$Identity,
        [Parameter(Mandatory = $true)][int]$MaximumBytes
    )
    [WinterGate.Native]::ReadVerifiedUtf8TextFile(
        [IO.Path]::GetFullPath($Path),
        $Identity,
        $MaximumBytes)
}

function Resolve-GitMetadataPath {
    param(
        [Parameter(Mandatory = $true)][string]$BaseDirectory,
        [Parameter(Mandatory = $true)][string]$Value,
        [Parameter(Mandatory = $true)][string]$Label
    )
    if ([string]::IsNullOrWhiteSpace($Value) -or
        $Value.StartsWith('\\?\') -or
        $Value.StartsWith('\\.\')) {
        throw "$Label contains an unsafe path."
    }
    if ([IO.Path]::IsPathRooted($Value)) {
        $driveAbsolute = $Value -match '^[A-Za-z]:[\\/]'
        $uncAbsolute = $Value -match '^\\\\[^\\/]+[\\/][^\\/]+[\\/]'
        if (-not $driveAbsolute -and -not $uncAbsolute) {
            throw "$Label must not use a drive-relative or root-relative path."
        }
        return [IO.Path]::GetFullPath($Value)
    }
    [IO.Path]::GetFullPath([IO.Path]::Combine($BaseDirectory, $Value))
}

function Resolve-GitMetadataDirectory {
    $dotGitPath = [IO.Path]::Combine(
        $script:ProjectIdentity.FinalPath,
        '.git')
    try {
        $attributes = [IO.File]::GetAttributes($dotGitPath)
    }
    catch [IO.FileNotFoundException] { return $null }
    catch [IO.DirectoryNotFoundException] { return $null }
    if (($attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
        throw 'Project .git metadata entry must not be a reparse point.'
    }

    $metadataFiles = New-Object 'System.Collections.Generic.List[object]'
    if (($attributes -band [IO.FileAttributes]::Directory) -ne 0) {
        $gitDirectoryIdentity = [WinterGate.Native]::GetPathIdentity(
            $dotGitPath,
            [WinterGate.PathKind]::Directory,
            $true)
    } else {
        $gitFileIdentity = [WinterGate.Native]::GetReadableFileIdentity(
            $dotGitPath)
        [void]$metadataFiles.Add($gitFileIdentity)
        $gitFileText = Read-VerifiedGateText -Path $dotGitPath -Identity $gitFileIdentity -MaximumBytes 65536
        $gitFileLine = Remove-GitTerminalNewline -Text $gitFileText -Label 'Project .git file'
        if ($gitFileLine -cnotmatch '^gitdir: (.+)$') {
            throw 'Project .git file has an invalid gitdir record.'
        }
        $gitDirectoryPath = Resolve-GitMetadataPath -BaseDirectory ([IO.Path]::GetDirectoryName($dotGitPath)) -Value $Matches[1] -Label 'Project .git gitdir'
        $gitDirectoryIdentity = [WinterGate.Native]::GetPathIdentity(
            $gitDirectoryPath,
            [WinterGate.PathKind]::Directory,
            $true)
    }

    $commonDirectoryIdentity = $gitDirectoryIdentity
    $commonFilePath = [IO.Path]::Combine(
        $gitDirectoryIdentity.FinalPath,
        'commondir')
    $commonFileIdentity =
        [WinterGate.Native]::TryGetReadableFileIdentity($commonFilePath)
    if ($null -ne $commonFileIdentity) {
        [void]$metadataFiles.Add($commonFileIdentity)
        $commonText = Read-VerifiedGateText -Path $commonFilePath -Identity $commonFileIdentity -MaximumBytes 65536
        $commonLine = Remove-GitTerminalNewline -Text $commonText -Label 'Git commondir file'
        $commonPath = Resolve-GitMetadataPath -BaseDirectory $gitDirectoryIdentity.FinalPath -Value $commonLine -Label 'Git commondir'
        $commonDirectoryIdentity = [WinterGate.Native]::GetPathIdentity(
            $commonPath,
            [WinterGate.PathKind]::Directory,
            $true)
    }
    [pscustomobject][ordered]@{
        GitDirectoryIdentity = $gitDirectoryIdentity
        CommonDirectoryIdentity = $commonDirectoryIdentity
        MetadataFileIdentities = [object[]]$metadataFiles.ToArray()
    }
}

function Get-SafeGitReferencePath {
    param(
        [Parameter(Mandatory = $true)][string]$GitDirectory,
        [Parameter(Mandatory = $true)][string]$ReferenceName
    )
    if ($ReferenceName -cnotmatch '^refs/[A-Za-z0-9][A-Za-z0-9._/-]*$' -or
        $ReferenceName.Contains('//') -or
        $ReferenceName.Contains('..') -or
        $ReferenceName.Contains('@{') -or
        $ReferenceName.EndsWith('/') -or
        $ReferenceName.EndsWith('.') -or
        $ReferenceName.EndsWith('.lock', [StringComparison]::OrdinalIgnoreCase)) {
        throw "Git HEAD contains an unsafe reference: $ReferenceName"
    }
    $relative = $ReferenceName.Replace('/', '\')
    $candidate = [IO.Path]::GetFullPath(
        [IO.Path]::Combine($GitDirectory, $relative))
    $prefix = $GitDirectory.TrimEnd('\') + '\'
    if (-not $candidate.StartsWith(
        $prefix,
        [StringComparison]::OrdinalIgnoreCase)) {
        throw "Git reference escaped its metadata directory: $ReferenceName"
    }
    $candidate
}

function ConvertTo-GitObjectId {
    param(
        [Parameter(Mandatory = $true)][string]$Text,
        [Parameter(Mandatory = $true)][string]$Label
    )
    $value = Remove-GitTerminalNewline -Text $Text -Label $Label
    if ($value -cnotmatch '^[0-9a-f]{40}([0-9a-f]{24})?$') {
        throw "$Label is not a lowercase Git object id."
    }
    $value
}

function Test-GitPerWorktreeReference {
    param([Parameter(Mandatory = $true)][string]$ReferenceName)
    $ReferenceName.StartsWith('refs/bisect/', [StringComparison]::Ordinal) -or
        $ReferenceName.StartsWith('refs/rewritten/', [StringComparison]::Ordinal) -or
        $ReferenceName.StartsWith('refs/worktree/', [StringComparison]::Ordinal)
}

function Read-GitLooseReference {
    param(
        [Parameter(Mandatory = $true)]$Metadata,
        [Parameter(Mandatory = $true)][string]$ReferenceName
    )
    $perWorktree = Test-GitPerWorktreeReference $ReferenceName
    $directory = if ($perWorktree) {
        $Metadata.GitDirectoryIdentity.FinalPath
    } else {
        $Metadata.CommonDirectoryIdentity.FinalPath
    }
    $path = Get-SafeGitReferencePath $directory $ReferenceName
    $identity = [WinterGate.Native]::TryGetReadableFileIdentity($path)
    if ($null -ne $identity) {
        $text = Read-VerifiedGateText -Path $path -Identity $identity -MaximumBytes 65536
        return [pscustomobject][ordered]@{
            Commit = ConvertTo-GitObjectId -Text $text -Label "Git loose reference '$ReferenceName'"
            Identity = $identity
        }
    }
    $null
}

function Read-GitPackedReference {
    param(
        [Parameter(Mandatory = $true)]$Metadata,
        [Parameter(Mandatory = $true)][string]$ReferenceName
    )
    $path = [IO.Path]::Combine(
        $Metadata.CommonDirectoryIdentity.FinalPath,
        'packed-refs')
    $identity = [WinterGate.Native]::TryGetReadableFileIdentity($path)
    if ($null -eq $identity) { return $null }
    $text = Read-VerifiedGateText `
        -Path $path -Identity $identity -MaximumBytes 4194304
    $matchedObject = $null
    foreach ($line in ($text -split "`r?`n")) {
        if ([string]::IsNullOrEmpty($line) -or $line.StartsWith('#')) {
            continue
        }
        if ($line -cmatch '^\^[0-9a-f]{40}([0-9a-f]{24})?$') {
            continue
        }
        if ($line -cnotmatch '^([0-9a-f]{40}([0-9a-f]{24})?) (refs/.+)$') {
            throw 'Git packed-refs contains a malformed record.'
        }
        if ($Matches[3] -ceq $ReferenceName) {
            if ($null -ne $matchedObject) {
                throw "Git packed-refs duplicates '$ReferenceName'."
            }
            $matchedObject = $Matches[1]
        }
    }
    if ($null -eq $matchedObject) { return $null }
    [pscustomobject][ordered]@{
        Commit = $matchedObject
        Identity = $identity
    }
}

function Get-ProjectHeadState {
    $metadata = Resolve-GitMetadataDirectory
    if ($null -eq $metadata) {
        return [pscustomobject][ordered]@{
            Commit = $null
            Metadata = $null
            DirectoryIdentities = [object[]]@()
            FileIdentities = [object[]]@()
        }
    }
    $headPath = [IO.Path]::Combine(
        $metadata.GitDirectoryIdentity.FinalPath,
        'HEAD')
    $headIdentity = [WinterGate.Native]::GetReadableFileIdentity($headPath)
    $headText = Read-VerifiedGateText -Path $headPath -Identity $headIdentity -MaximumBytes 65536
    $headLine = Remove-GitTerminalNewline -Text $headText -Label 'Git HEAD'
    if ($headLine -cmatch '^ref: (refs/.+)$') {
        $reference = $Matches[1]
        [void](Get-SafeGitReferencePath $metadata.GitDirectoryIdentity.FinalPath $reference)
        $resolvedReference = Read-GitLooseReference $metadata $reference
        if ($null -eq $resolvedReference -and
            -not (Test-GitPerWorktreeReference $reference)) {
            $resolvedReference = Read-GitPackedReference $metadata $reference
        }
        if ($null -eq $resolvedReference) {
            throw "Git HEAD reference has no current commit: $reference"
        }
        $commit = $resolvedReference.Commit
        $referenceIdentity = $resolvedReference.Identity
    } else {
        $commit = ConvertTo-GitObjectId -Text $headLine -Label 'Git HEAD'
        $referenceIdentity = $null
    }
    $directoryIdentities = @($metadata.GitDirectoryIdentity)
    if (-not [WinterGate.Native]::SameStablePath(
        $metadata.GitDirectoryIdentity,
        $metadata.CommonDirectoryIdentity)) {
        $directoryIdentities += $metadata.CommonDirectoryIdentity
    }
    $fileIdentities = @($metadata.MetadataFileIdentities) + @($headIdentity)
    if ($null -ne $referenceIdentity) {
        $fileIdentities += $referenceIdentity
    }

    [pscustomobject][ordered]@{
        Commit = $commit
        Metadata = $metadata
        DirectoryIdentities = [object[]]$directoryIdentities
        FileIdentities = [object[]]$fileIdentities
    }
}

function Assert-GitCommitOverride {
    param($Commit)
    $environment = [Environment]::GetEnvironmentVariables()
    if (-not $environment.Contains('GIT_COMMIT')) { return }
    $override = [string]$environment['GIT_COMMIT']
    if ($null -eq $Commit) {
        throw 'GIT_COMMIT was supplied but ProjectRoot is not a Git worktree.'
    }
    if ($override -cnotmatch '^[0-9a-f]{40}([0-9a-f]{24})?$' -or
        $override -cne $Commit) {
        throw 'GIT_COMMIT does not exactly match the current ProjectRoot HEAD.'
    }
}

function Assert-ProjectHeadCommit {
    if (-not $script:HeadTrackingInitialized) { return }
    $current = Get-ProjectHeadState
    if (($null -eq $script:HeadCommit) -ne ($null -eq $current.Commit) -or
        ($null -ne $script:HeadCommit -and
         $script:HeadCommit -cne $current.Commit)) {
        throw 'ProjectRoot Git HEAD changed during the gate run.'
    }
    if ($script:HeadState.DirectoryIdentities.Count -ne
            $current.DirectoryIdentities.Count -or
        $script:HeadState.FileIdentities.Count -ne
            $current.FileIdentities.Count) {
        throw 'ProjectRoot Git metadata identity set changed during the gate run.'
    }
    for ($index = 0;
         $index -lt $script:HeadState.DirectoryIdentities.Count;
         $index++) {
        if (-not [WinterGate.Native]::SameStablePath(
            $script:HeadState.DirectoryIdentities[$index],
            $current.DirectoryIdentities[$index])) {
            throw 'ProjectRoot Git directory identity changed during the gate run.'
        }
    }
    for ($index = 0;
         $index -lt $script:HeadState.FileIdentities.Count;
         $index++) {
        if (-not [WinterGate.Native]::SameStablePath(
            $script:HeadState.FileIdentities[$index],
            $current.FileIdentities[$index])) {
            throw 'ProjectRoot Git file identity changed during the gate run.'
        }
    }
    Assert-GitCommitOverride -Commit $current.Commit
}

# END LOOP 3.4-P1 FINAL GIT IDENTITY LAYER

# BEGIN LOOP 3.3-P2 STEP AND PROVISIONAL MANIFEST BUILDERS
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
        [string[]]$RequiredFiles = @()
    )
    if (-not [IO.Path]::IsPathRooted($Executable)) {
        throw "Step '$Name' executable must be absolute."
    }
    foreach ($argument in $Arguments) {
        if ($null -eq $argument) {
            throw "Step '$Name' has a null process argument."
        }
    }
    try {
        $executableIdentity =
            [WinterGate.Native]::GetReadableFileIdentity($Executable)
    }
    catch [WinterGate.WinterGatePathIdentityException] {
        throw [InvalidOperationException]::new(
            ("Manifest executable is unsafe for step '$Name': " +
             "$Executable. $($_.Exception.Message)"),
            $_.Exception)
    }
    $requiredIdentities = New-Object 'System.Collections.Generic.List[object]'
    foreach ($required in $RequiredFiles) {
        if (-not [IO.Path]::IsPathRooted($required)) {
            throw "Step '$Name' required file must be absolute: $required"
        }
        try {
            [void]$requiredIdentities.Add(
                [WinterGate.Native]::TryGetReadableFileIdentity($required))
        }
        catch [WinterGate.WinterGatePathIdentityException] {
            throw [InvalidOperationException]::new(
                ("Manifest required file is unsafe for step '$Name': " +
                 "$required. $($_.Exception.Message)"),
                $_.Exception)
        }
    }
    [pscustomobject][ordered]@{
        Name = $Name
        Kind = $Kind
        Executable = $executableIdentity.FinalPath
        ExecutableIdentity = $executableIdentity
        Arguments = [string[]]$Arguments.Clone()
        TimeoutSeconds = $TimeoutSeconds
        Postcondition = $Postcondition
        RequiredFiles = [string[]]$RequiredFiles.Clone()
        RequiredFileIdentities = [object[]]$requiredIdentities.ToArray()
    }
}

function Get-StructuralGateManifest {
    $source = Get-ExpectedProjectFilePath `
        $script:ProjectIdentity.FinalPath `
        'Tools\test_governance_winter_interlude.py'
    [object[]]@(
        (New-GateStep `
            'source-contract' `
            'Python' `
            $script:PythonIdentity.FinalPath `
            ([string[]]@(
                '-m', 'unittest',
                'Tools.test_governance_winter_interlude', '-v')) `
            $ToolTimeoutSeconds `
            'exit-zero' `
            ([string[]]@($source)))
    )
}

function Get-NarrativeGateManifest {
    $checker = Get-ExpectedProjectFilePath `
        $script:ProjectIdentity.FinalPath `
        'Tools\check_winter_narrative_capabilities.py'
    $phase = if ($NarrativePhase -eq 'Batch') { 'batch' } else { 'final' }
    $output = Join-Path `
        $script:EvidenceIdentity.FinalPath `
        'narrative-01-narrative-capability-no-head.output.json'
    [object[]]@(
        (New-GateStep `
            'narrative-capability' `
            'Python' `
            $script:PythonIdentity.FinalPath `
            ([string[]]@(
                '-B', $checker, '--phase', $phase,
                '--format', 'json', '--output', $output)) `
            $ToolTimeoutSeconds `
            'capability-json' `
            ([string[]]@($checker)))
    )
}

# END LOOP 3.3-P2 STEP AND PROVISIONAL MANIFEST BUILDERS

# BEGIN LOOP 3.4-P2 FINAL PROJECT AND DIRECTORY RECHECKS
function Assert-ProjectRootIdentity {
    Assert-GatePathState `
        -ExpectedIdentity $script:ProjectIdentity `
        -Label 'ProjectRoot' | Out-Null
}

function Assert-RunTreeDirectoryIdentities {
    foreach ($identity in @(
        $script:RunRootIdentity,
        $script:EvidenceIdentity,
        $script:SavedirsIdentity)) {
        Assert-GatePathState `
            -ExpectedIdentity $identity `
            -Label "base gate directory '$($identity.FinalPath)'" | Out-Null
    }
}

function Assert-AllGateDirectoryIdentities {
    Assert-ProjectRootIdentity
    foreach ($identity in $script:GateDirectoryIdentities) {
        Assert-GatePathState `
            -ExpectedIdentity $identity `
            -Label "registered gate directory '$($identity.FinalPath)'" |
            Out-Null
    }
    Assert-ProjectHeadCommit
}

function Assert-NonEvidenceGateDirectoryIdentities {
    Assert-ProjectRootIdentity
    foreach ($identity in $script:GateDirectoryIdentities) {
        if ([WinterGate.Native]::SameObject(
            $identity,
            $script:EvidenceIdentity)) {
            continue
        }
        Assert-GatePathState `
            -ExpectedIdentity $identity `
            -Label "registered pre-write gate directory '$($identity.FinalPath)'" |
            Out-Null
    }
    Assert-ProjectHeadCommit
}

# END LOOP 3.4-P2 FINAL PROJECT AND DIRECTORY RECHECKS

# BEGIN LOOP 3.3-P3 JSON BRIDGE AND VALIDATION RESULT
function Get-IdentityEvidenceObject {
    param([Parameter(Mandatory = $true)]$Identity)
    [pscustomobject][ordered]@{
        final_path = $Identity.FinalPath
        volume_serial_number = $Identity.VolumeSerialNumber
        file_index = $Identity.FileIndex
    }
}

function Write-GateEvidenceJson {
    param(
        [Parameter(Mandatory = $true)][string]$Path,
        [Parameter(Mandatory = $true)]$Value
    )
    Assert-NonEvidenceGateDirectoryIdentities
    $fullPath = [IO.Path]::GetFullPath($Path)
    $json = $Value | ConvertTo-Json -Depth 32
    [WinterGate.Native]::WriteUtf8JsonCreateNew(
        $fullPath,
        $json,
        $script:EvidenceIdentity)
    Assert-AllGateDirectoryIdentities
}

function Write-GateSummaryJson {
    param(
        [Parameter(Mandatory = $true)][string]$Path,
        [Parameter(Mandatory = $true)]$Value,
        [switch]$RunTreeOnly
    )
    if (-not $script:EvidencePublicationSafe) {
        throw 'A live process tree makes summary publication unsafe.'
    }
    if ($RunTreeOnly) {
        Assert-RunTreeDirectoryIdentities
    } else {
        Assert-AllGateDirectoryIdentities
    }
    $normalJson = $Value | ConvertTo-Json -Depth 32
    $collisionValue = $normalJson | ConvertFrom-Json
    $collisionError =
        'Unowned gate-summary.json was quarantined before gate-owned publication.'
    $collisionValue.status = 'failed'
    $collisionValue.failure_kind = 'validation'
    $collisionValue.error = $collisionError
    $script:SummaryPublicationAttempted = $true
    $script:QuarantinedSummaryPath =
        [WinterGate.Native]::WriteOwnedSummaryUtf8Json(
            [IO.Path]::GetFullPath($Path),
            $normalJson,
            ($collisionValue | ConvertTo-Json -Depth 32),
            $script:EvidenceIdentity)
    if ($null -ne $script:QuarantinedSummaryPath) {
        $Value.status = 'failed'
        $Value.failure_kind = 'validation'
        $Value.error = $collisionError
    }
    $script:SummaryCommittedByGate = $true
    if ($RunTreeOnly) {
        Assert-RunTreeDirectoryIdentities
    } else {
        Assert-AllGateDirectoryIdentities
    }
}

function New-ValidationGateResult {
    param(
        [Parameter(Mandatory = $true)]$Step,
        [Parameter(Mandatory = $true)][int]$Ordinal,
        [Parameter(Mandatory = $true)][string]$ResultRelative,
        [Parameter(Mandatory = $true)][string]$ErrorText
    )
    [pscustomobject][ordered]@{
        ordinal = $Ordinal
        name = $Step.Name
        kind = $Step.Kind
        executable = $Step.Executable
        arguments = [string[]]$Step.Arguments.Clone()
        working_directory = $script:ProjectIdentity.FinalPath
        process_started = $false
        process_id = $null
        started_utc = $null
        ended_utc = $null
        exit_code = $null
        timed_out = $false
        tree_drained = $true
        had_live_descendants_after_root_exit = $false
        elapsed_milliseconds = $null
        stdout = $null
        stderr = $null
        result = $ResultRelative
        postcondition = $Step.Postcondition
        manual_review_required = ($Step.Postcondition -eq 'manual-review')
        status = 'failed'
        failure_kind = 'validation'
        error = $ErrorText
    }
}

# END LOOP 3.3-P3 JSON BRIDGE AND VALIDATION RESULT

# BEGIN LOOP 3.4-P3 FINAL STEP DEPENDENCY RECHECK
function Get-GateStepDependencyValidationError {
    param([Parameter(Mandatory = $true)]$Step)
    try {
        $currentExecutable =
            [WinterGate.Native]::GetReadableFileIdentity($Step.Executable)
        if (-not [WinterGate.Native]::SameStablePath(
            $Step.ExecutableIdentity, $currentExecutable)) {
            return "Step '$($Step.Name)' executable identity changed."
        }
        for ($index = 0; $index -lt $Step.RequiredFiles.Count; $index++) {
            $baseline = $Step.RequiredFileIdentities[$index]
            if ($null -eq $baseline) {
                return (
                    "Step '$($Step.Name)' required file was missing at " +
                    'manifest construction: ' + $Step.RequiredFiles[$index]
                )
            }
            $current = [WinterGate.Native]::GetReadableFileIdentity(
                $Step.RequiredFiles[$index])
            if (-not [WinterGate.Native]::SameStablePath($baseline, $current)) {
                return (
                    "Step '$($Step.Name)' required file identity changed: " +
                    $Step.RequiredFiles[$index]
                )
            }
        }
    }
    catch {
        $unwrapped = Get-UnwrappedException $_.Exception
        if ($unwrapped -is [WinterGate.WinterGatePathIdentityException]) {
            return $unwrapped.Message
        }
        throw
    }
    return $null
}

# END LOOP 3.4-P3 FINAL STEP DEPENDENCY RECHECK

# BEGIN LOOP 3.3-P4 PROCESS MAPPING AND PUBLIC BRIDGE SHELL
function Invoke-GateStep {
    param(
        [Parameter(Mandatory = $true)]$Step,
        [Parameter(Mandatory = $true)][int]$Ordinal
    )
    Assert-AllGateDirectoryIdentities
    $prefix = '{0}-{1:D2}-{2}-{3}' -f `
        $Gate.ToLowerInvariant(), $Ordinal, $Step.Name, $script:HeadToken
    $stdoutName = "$prefix.stdout.txt"
    $stderrName = "$prefix.stderr.txt"
    $resultName = "$prefix.result.json"
    $stdoutPath = Join-Path $script:EvidenceIdentity.FinalPath $stdoutName
    $stderrPath = Join-Path $script:EvidenceIdentity.FinalPath $stderrName
    $resultPath = Join-Path $script:EvidenceIdentity.FinalPath $resultName
    $stdoutRelative = "evidence/$stdoutName"
    $stderrRelative = "evidence/$stderrName"
    $resultRelative = "evidence/$resultName"

    $validationError = Get-GateStepDependencyValidationError $Step

    if ($null -ne $validationError) {
        $failed = New-ValidationGateResult `
            -Step $Step -Ordinal $Ordinal `
            -ResultRelative $resultRelative -ErrorText $validationError
        Write-GateEvidenceJson -Path $resultPath -Value $failed
        return $failed
    }

    $process = [WinterGate.Native]::RunProcessTree(
        $Step.Executable,
        [string[]]$Step.Arguments,
        $script:ProjectIdentity.FinalPath,
        $stdoutPath,
        $stderrPath,
        [int]($Step.TimeoutSeconds * 1000),
        $script:EvidenceIdentity)

    if ($process.ProcessStarted -and -not $process.TreeDrained) {
        $script:EvidencePublicationSafe = $false
        throw [InvalidOperationException]::new(
            "Step '$($Step.Name)' left a live process tree; " +
            'evidence publication is unsafe.')
    }
    $postRunValidationError =
        Get-GateStepDependencyValidationError $Step
    $unownedSummaryDetected = $null -ne (
        [WinterGate.Native]::TryGetReadableFileIdentity($script:SummaryPath))
    # BEGIN LOOP 3.5-P1 FINAL PRE-WRITE RECHECK
    Assert-NonEvidenceGateDirectoryIdentities
    # END LOOP 3.5-P1 FINAL PRE-WRITE RECHECK
    $failureKind = $null
    $errorText = $null
    if ($unownedSummaryDetected) {
        $failureKind = 'validation'
        $errorText =
            'Unowned gate-summary.json appeared while a gate step was running.'
    }
    elseif ($null -ne $postRunValidationError) {
        $failureKind = 'validation'
        $errorText = $postRunValidationError
    }
    elseif (-not $process.ProcessStarted) {
        $failureKind = 'process'
        $errorText = $process.StartError
    }
    elseif ($process.ProcessStarted -and
            -not [bool]$process.OutputEvidenceValid) {
        $failureKind = 'validation'
        $errorText =
            "Step '$($Step.Name)' output evidence identity validation failed."
        if (-not [string]::IsNullOrWhiteSpace(
            [string]$process.OutputEvidenceError)) {
            $errorText += " $([string]$process.OutputEvidenceError)"
        }
    }
    elseif ($process.TimedOut) {
        $failureKind = 'timeout'
        $errorText = "Step '$($Step.Name)' exceeded $($Step.TimeoutSeconds) seconds."
    }
    elseif (-not $process.TreeDrained -or
            $process.HadLiveDescendantsAfterRootExit -or
            -not [string]::IsNullOrWhiteSpace($process.StartError)) {
        $failureKind = 'process_tree'
        $errorText = if (-not [string]::IsNullOrWhiteSpace($process.StartError)) {
            $process.StartError
        } else {
            "Step '$($Step.Name)' violated its bounded process tree."
        }
    }
    elseif ([int]$process.ExitCode -ne 0) {
        $failureKind = 'process'
        $errorText = "Step '$($Step.Name)' exited $([int]$process.ExitCode)."
    }
    elseif ($Step.Postcondition -ne 'exit-zero') {
        $failureKind = 'validation'
        $errorText =
            "Postcondition '$($Step.Postcondition)' is not available in Task 3."
    }
    $outputEvidenceTrusted = [bool]$process.OutputEvidenceValid

    $result = [pscustomobject][ordered]@{
        ordinal = $Ordinal
        name = $Step.Name
        kind = $Step.Kind
        executable = $Step.Executable
        arguments = [string[]]$Step.Arguments.Clone()
        working_directory = $script:ProjectIdentity.FinalPath
        process_started = [bool]$process.ProcessStarted
        process_id = $process.ProcessId
        started_utc = if ($null -eq $process.StartedUtc) {
            $null
        } else { ([DateTime]$process.StartedUtc).ToString('o') }
        ended_utc = if ($null -eq $process.EndedUtc) {
            $null
        } else { ([DateTime]$process.EndedUtc).ToString('o') }
        exit_code = $process.ExitCode
        timed_out = [bool]$process.TimedOut
        tree_drained = [bool]$process.TreeDrained
        had_live_descendants_after_root_exit =
            [bool]$process.HadLiveDescendantsAfterRootExit
        elapsed_milliseconds = $process.ElapsedMilliseconds
        stdout = if ($outputEvidenceTrusted) { $stdoutRelative } else { $null }
        stderr = if ($outputEvidenceTrusted) { $stderrRelative } else { $null }
        result = $resultRelative
        postcondition = $Step.Postcondition
        manual_review_required = ($Step.Postcondition -eq 'manual-review')
        status = if ($null -eq $failureKind) { 'passed' } else { 'failed' }
        failure_kind = $failureKind
        error = $errorText
    }
    Write-GateEvidenceJson -Path $resultPath -Value $result
    $result
}

function Invoke-WinterInterludeGate {
    Add-WinterGateNativeTypes
    $script:TrustedPowerShellIdentity = Assert-WinterGateHostIdentity
    $script:ProjectIdentity = Resolve-GateProject `
        -ProjectRoot $ProjectRoot `
        -WasSpecified:$projectRootWasSpecified
    $protectedSavePaths = @(Get-ProtectedPlayerSavePaths)
    $runTree = New-VerifiedRunRoot `
        -Candidate $RunRoot `
        -CandidateWasSpecified:$runRootWasSpecified `
        -ProjectIdentity $script:ProjectIdentity `
        -ProtectedSavePaths $protectedSavePaths
    $script:RunRootIdentity = $runTree.Identity
    $script:EvidenceIdentity = $runTree.EvidenceIdentity
    $script:SavedirsIdentity = $runTree.SavedirsIdentity
    $script:GateDirectoryIdentities =
        New-Object 'System.Collections.Generic.List[object]'
    [void]$script:GateDirectoryIdentities.Add($script:RunRootIdentity)
    [void]$script:GateDirectoryIdentities.Add($script:EvidenceIdentity)
    [void]$script:GateDirectoryIdentities.Add($script:SavedirsIdentity)
    $script:EvidencePublicationSafe = $true
    $script:SummaryCommittedByGate = $false
    $script:SummaryPublicationAttempted = $false
    $script:QuarantinedSummaryPath = $null
    $script:HeadTrackingInitialized = $false
    $script:HeadState = $null
    $script:HeadCommit = $null
    $script:HeadToken = 'no-head'
    $summary = [pscustomobject][ordered]@{
        schema_version = 1
        gate = $Gate
        narrative_phase = if ($Gate -eq 'Narrative') {
            $NarrativePhase
        } else { $null }
        status = 'passed'
        failure_kind = $null
        error = $null
        started_utc = [DateTime]::UtcNow.ToString('o')
        ended_utc = $null
        head_token = $script:HeadToken
        host = [pscustomobject][ordered]@{
            edition = $PSVersionTable.PSEdition
            version = $PSVersionTable.PSVersion.ToString()
            executable = Get-IdentityEvidenceObject `
                $script:TrustedPowerShellIdentity
        }
        project_root = Get-IdentityEvidenceObject $script:ProjectIdentity
        run_root = Get-IdentityEvidenceObject $script:RunRootIdentity
        steps = [object[]]@()
    }
    $script:SummaryPath = Join-Path `
        $script:EvidenceIdentity.FinalPath `
        'gate-summary.json'
    try {
        [Console]::Out.WriteLine(
            "Winter gate run root: $($script:RunRootIdentity.FinalPath)")
        Assert-ProjectRootIdentity
        $script:HeadState = Get-ProjectHeadState
        $script:HeadCommit = $script:HeadState.Commit
        $script:HeadToken = if ($null -eq $script:HeadCommit) {
            'no-head'
        } else { $script:HeadCommit.Substring(0, 12) }
        $summary.head_token = $script:HeadToken
        $script:HeadTrackingInitialized = $true
        Assert-GitCommitOverride -Commit $script:HeadCommit
        $script:PythonIdentity = Resolve-PythonExecutable
        [object[]]$manifest = if ($Gate -eq 'Structural') {
            @(Get-StructuralGateManifest)
        } else { @(Get-NarrativeGateManifest) }
        foreach ($index in 0..($manifest.Count - 1)) {
            $result = Invoke-GateStep `
                -Step $manifest[$index] -Ordinal ($index + 1)
            $summary.steps = [object[]]@($summary.steps + $result)
            if ($result.status -eq 'failed') {
                $summary.status = 'failed'
                $summary.failure_kind = $result.failure_kind
                $summary.error = $result.error
                break
            }
        }
        # BEGIN TASK 3 SOURCE-BRIDGE FORCED VALIDATION
        if ($summary.status -eq 'passed') {
            $summary.status = 'failed'
            $summary.failure_kind = 'validation'
            $summary.error = if ($Gate -eq 'Structural') {
                'structural manifest layer not implemented'
            } else {
                'narrative postcondition layer not implemented'
            }
        }
        # END TASK 3 SOURCE-BRIDGE FORCED VALIDATION
        $summary.ended_utc = [DateTime]::UtcNow.ToString('o')
        Write-GateSummaryJson -Path $script:SummaryPath -Value $summary
        if ($summary.status -ne 'passed') {
            throw [InvalidOperationException]::new($summary.error)
        }
    }
    catch [WinterGate.WinterGatePathIdentityException] {
        $pathError = $_
        if (-not $script:EvidencePublicationSafe) { throw }
        try { Assert-RunTreeDirectoryIdentities }
        catch { throw $pathError }
        if (-not $script:SummaryCommittedByGate -and
            -not $script:SummaryPublicationAttempted) {
            $summary.status = 'failed'
            $summary.failure_kind = 'validation'
            $summary.error = $pathError.Exception.Message
            $summary.ended_utc = [DateTime]::UtcNow.ToString('o')
            Write-GateSummaryJson `
                -Path $script:SummaryPath `
                -Value $summary `
                -RunTreeOnly
        }
        throw $pathError
    }
    catch {
        $ordinaryError = $_
        if (-not $script:EvidencePublicationSafe) { throw }
        if (-not $script:SummaryCommittedByGate -and
            -not $script:SummaryPublicationAttempted) {
            $summary.status = 'failed'
            $summary.failure_kind = 'validation'
            $summary.error = $ordinaryError.Exception.Message
            $summary.ended_utc = [DateTime]::UtcNow.ToString('o')
            Write-GateSummaryJson `
                -Path $script:SummaryPath `
                -Value $summary `
                -RunTreeOnly
        }
        throw $ordinaryError
    }
}
# END LOOP 3.3-P4 PROCESS MAPPING AND PUBLIC BRIDGE SHELL
```

#### Required execution sequence: five independent RED-to-GREEN loops

The catalogs above show the final exact content once so this plan stays
copy-pastable without duplicating thousands of lines. They are not permission
to paste the entire test class or process engine at once. Execute Loops
3.1-3.5 in order. Each RED adds only the named tests to the GREEN state from
the preceding loop, and each GREEN copies only the named catalog spans. Keep
each edit-and-test cycle to roughly 2-5 minutes. Do not refactor between RED
and GREEN; refactor only after that loop's focused command is green.

##### Loop 3.1 — pin readable files through the full anti-reparse chain

- [ ] **3.1 RED: add only the exact-source readable probe**

Copy the catalog imports needed by the probe, the complete marked
`LOOP 3.1-T0` support region, `NATIVE_READABLE_PROBE_SOURCE`,
`extract_native_source`, `compile_native_readable_probe`, and
`WinterInterludeGateNativeFoundationTests`. Do not add the writer probe,
recording child, shared fixture, or process tests yet. Run:

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateNativeFoundationTests.test_exact_native_readable_identity_rejects_parent_junction `
  -v
if ($LASTEXITCODE -eq 0) {
  throw 'Readable-file RED unexpectedly passed before Task 3 native methods.'
}
```

Expected RED: the exact combined Task 2+current native source does not yet
expose `GetReadableFileIdentity` / `ReadVerifiedUtf8TextFile`, so the probe
cannot compile. The failure must name that missing API, not a Python syntax or
fixture error.

- [ ] **3.1 minimal GREEN: add only readable identity declarations and helpers**

Replace Task 2's complete C# `using` block with the catalog block. In the
process-engine seam copy exactly the four marked catalog regions
`LOOP 3.1-A`, `LOOP 3.1-B`, `LOOP 3.1-C`, and `LOOP 3.1-D` in the order
specified by the C# copy map. The implementation must call Task 2
`GetPathIdentity(path, PathKind.File, true)` (or its Try variant) before
opening the canonical final path with `GENERIC_READ` and comparing the opened
handle with `SameStablePath`. The byte-reading API uses `FileShareRead` only;
the identity-only API may share read/write and closes immediately after its
comparison. Do not add a process launcher or JSON writer.

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateNativeFoundationTests.test_exact_native_readable_identity_rejects_parent_junction `
  -v
if ($LASTEXITCODE -ne 0) {
  throw 'Readable-file GREEN failed.'
}
```

Expected GREEN: `Ran 1 test` and `OK`; an ordinary file is accepted and a leaf
reached through a test-owned parent junction is rejected.

##### Loop 3.2 — make both JSON publication paths atomic and delete-pinned

- [ ] **3.2 RED: add only the exact-source writer probe and mutation**

On the 3.1 GREEN state, add exactly `import contextlib`, `import json`, and
`from dataclasses import dataclass` at the positions shown by the final catalog,
then copy `NATIVE_WRITER_PROBE_SOURCE`,
`compile_native_writer_probe`, `_NamedManualResetEvent`, all five
`_NATIVE_WRITER_*` instrumentation constants,
`restore_native_writer_pause`, `instrument_native_writer_pause`,
`assert_native_writer_lifecycle`, `attempt_replace`,
`attempt_winps_directory_move`, `_NativeWriterRaceObservation`,
`is_complete_native_writer_json`, `run_exact_native_writer_smoke`,
`mutate_native_writer_delete_sharing`,
`run_native_writer_lock_probe`, and
`WinterInterludeGateNativeWriterTests`. Run:

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateNativeWriterTests.test_exact_native_writer_and_instrumented_share_contracts `
  -v
if ($LASTEXITCODE -eq 0) {
  throw 'Native-writer RED unexpectedly passed before the public writers.'
}
```

Expected RED: the exact native source lacks one or both public writer methods.
The probe compilation must fail for that missing production API. It must not
fail because of a surrogate writer, timing-only sleep, or malformed fixture.

- [ ] **3.2 minimal GREEN: add only writer APIs and their direct helpers**

Copy exactly the three marked catalog regions `LOOP 3.2-A`, `LOOP 3.2-B`,
and `LOOP 3.2-C` at the anchors specified by the C# copy map. Do not add
`RunProcessTree` or the PowerShell gate bridge. Result leaves use `CREATE_NEW`
with no sharing. Summary staging and any existing summary handle omit
`FILE_SHARE_DELETE` until flush and handle-based no-replace publication finish.

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateNativeWriterTests.test_exact_native_writer_and_instrumented_share_contracts `
  -v
if ($LASTEXITCODE -ne 0) {
  throw 'Native-writer GREEN failed.'
}
```

Expected GREEN: `Ran 1 test` and `OK`. The unmodified final combined native
source first compiles and both ordinary public writer calls return rc 0 with one
BOM-free full JSON document at the fixed owned name. The fixture then proves its
test-only derivative restores byte-for-byte to each input source and inserts
exactly one helper plus two waits at the unique pre-flush anchors. At each named
barrier the public writer is incomplete and its verified leaf is zero bytes.
Production result and summary both deny Python `os.replace` of the leaf and an
independent WinPS5.1 `Move-Item` of Evidence, then return rc 0 / `owned-fixed`.
For both precise guard-plus-leaf delete-share mutants the two live moves succeed.
The result mutant returns rc 0 / `owned-raced`; the summary mutant first flushes
the same complete `owned-raced` document, then returns rc 92 with
`SetFileInformationByHandle(publish owned summary)` Win32 error 3. Neither is an
honest placement. A second WinPS5.1 parent move succeeds after close in every
case. Static lifecycle assertions pin guard-open before create, direct-child
verification before write, flush before handle close, and reject every pause
token from production. This is explicitly a synchronized compiled derivative,
not an exact-source race execution; the exact source is separately compiled,
smoked, and source-checked. No payload-size timing, write-speed polling,
surrogate writer, or production test-mode is allowed.

##### Loop 3.3 — launch one real source child through a named suspended Job

- [ ] **3.3 RED: add the public recording child and source-boundary cases**

On the 3.2 GREEN state, copy the complete marked test-catalog regions
`LOOP 3.3-T1A`, `LOOP 3.3-T1B`, and `LOOP 3.3-T2`, the replacement bootstrap boundary method,
the `WinterInterludeGateProcessTests` class header/setup helpers, and only these
process test methods:

- `test_public_process_uses_exact_argv_job_nul_and_handle_list`
- `test_bad_image_start_failure_keeps_process_fields_null`

Run:

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateBootstrapTests.test_valid_call_reaches_source_bridge_with_honest_validation_summary `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_public_process_uses_exact_argv_job_nul_and_handle_list `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_bad_image_start_failure_keeps_process_fields_null `
  -v
if ($LASTEXITCODE -eq 0) {
  throw 'Process-launch RED unexpectedly passed before RunProcessTree.'
}
```

Expected RED: Task 2 still stops at its named process boundary. No child record
or result is accepted as the RED.

- [ ] **3.3 minimal GREEN: add the process handshake and the narrow source bridge**

Copy exactly the C# catalog regions `LOOP 3.3-A`, `3.3-B`, `3.3-C`, and
`3.3-D`, and insert the complete marked `LOOP 3.3 TEMPORARY
ROOT-SNAPSHOT ACCOUNTING` method at the C# copy-map anchor. Then copy exactly
the PowerShell regions `LOOP 3.3-P1`, `3.3-P2`, `3.3-P3`, and `3.3-P4`,
applying the exact temporary resolver, executable-baseline, and early-P4
substitutions from the copy map, inserting the complete temporary identity
layer between P1 and P2, and replacing P4's printed `LOOP 3.5-P1` with the
complete temporary pre-write region. Delete Task 2's complete old
`Invoke-WinterInterludeGate` before inserting P4 at the documented top-level
anchor.

The child must be created suspended, assigned to the named Job before
`ResumeThread`, receive exact `string[]` argv, NUL stdin, an explicit handle
list, and share-delete stdout/stderr handles. Do not add a PowerShell filesystem
writer.

Keep this GREEN deliberately narrow:

- non-Git projects return the provisional no-HEAD state;
- Git input fails closed with the explicit temporary error
  `git identity layer not implemented`;
- ProjectRoot and post-drain dependency rechecks remain absent until Loop 3.4;
- root accounting may use the temporary `!rootStillListed -> true` branch
  until Loop 3.5.

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateBootstrapTests.test_valid_call_reaches_source_bridge_with_honest_validation_summary `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_public_process_uses_exact_argv_job_nul_and_handle_list `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_bad_image_start_failure_keeps_process_fields_null `
  -v
if ($LASTEXITCODE -ne 0) {
  throw 'Process-launch GREEN failed.'
}
```

Expected GREEN: `Ran 3 tests` and `OK`. The clean public call has one real
source record with exact argv, expected named-Job membership, NUL stdin, and no
inherited sentinel; the passed source result is followed by the honest
`failed` / `validation` boundary summary and exit 1. The bad-image case has
`process_started=false` and null PID/time/exit fields.

##### Loop 3.4 — freeze Git, ProjectRoot, and step dependencies across execution

- [ ] **3.4 RED: add only identity-stability behavior tests**

On the 3.3 GREEN state, copy
`NATIVE_EXECUTABLE_ACCESS_PROBE_SOURCE`,
`compile_native_executable_access_probe`, and
`deny_read_extended_attributes`, then add these seventeen catalog tests and no
Loop 3.5 tests:

- `test_required_file_parent_junction_is_rejected_before_launch`
- `test_executable_parent_junction_is_rejected_before_launch`
- `test_executable_identity_uses_readable_full_chain_api`
- `test_executable_requires_generic_read_before_launch`
- `test_missing_python_after_safe_tree_publishes_validation_summary`
- `test_project_root_replacement_after_source_is_caught_before_result`
- `test_required_file_replaced_during_child_is_failed_after_tree_drain`
- `test_head_token_uses_real_linked_worktree_packed_ref`
- `test_head_token_uses_real_ordinary_loose_ref_and_exact_git_commit`
- `test_git_indirection_rejects_root_current_drive_and_drive_relative_paths`
- `test_per_worktree_reference_namespaces_never_fall_back_to_common_packed_refs`
- `test_git_metadata_identity_replacement_during_child_fails_before_result`
- `test_linked_worktree_ignores_forged_loose_shared_branch_ref`
- `test_git_head_read_fails_closed_while_a_writer_is_open`
- `test_git_loose_ref_parent_junction_is_rejected_before_launch`
- `test_explicit_empty_git_commit_is_rejected`
- `test_forged_git_commit_is_honest_validation_failure`

Run the three executable-resolution cases individually first. Keep each
nonzero guard immediately after its invocation so no later RED can mask an
unexpected pass:

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_executable_parent_junction_is_rejected_before_launch `
  -v
if ($LASTEXITCODE -eq 0) {
  throw 'Executable-parent-junction RED unexpectedly passed.'
}

python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_executable_requires_generic_read_before_launch `
  -v
if ($LASTEXITCODE -eq 0) {
  throw 'Executable-readable-access RED unexpectedly passed.'
}

python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_missing_python_after_safe_tree_publishes_validation_summary `
  -v
if ($LASTEXITCODE -eq 0) {
  throw 'Missing-Python summary RED unexpectedly passed.'
}
```

Then run the complete seventeen-test RED together:

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_required_file_parent_junction_is_rejected_before_launch `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_executable_parent_junction_is_rejected_before_launch `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_executable_identity_uses_readable_full_chain_api `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_executable_requires_generic_read_before_launch `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_missing_python_after_safe_tree_publishes_validation_summary `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_project_root_replacement_after_source_is_caught_before_result `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_required_file_replaced_during_child_is_failed_after_tree_drain `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_head_token_uses_real_linked_worktree_packed_ref `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_head_token_uses_real_ordinary_loose_ref_and_exact_git_commit `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_git_indirection_rejects_root_current_drive_and_drive_relative_paths `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_per_worktree_reference_namespaces_never_fall_back_to_common_packed_refs `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_git_metadata_identity_replacement_during_child_fails_before_result `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_linked_worktree_ignores_forged_loose_shared_branch_ref `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_git_head_read_fails_closed_while_a_writer_is_open `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_git_loose_ref_parent_junction_is_rejected_before_launch `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_explicit_empty_git_commit_is_rejected `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_forged_git_commit_is_honest_validation_failure `
  -v
if ($LASTEXITCODE -eq 0) {
  throw 'Identity-stability RED unexpectedly passed before final rechecks.'
}
```

Expected RED: each individual command reports `FAILED (failures=1)`, never
`ERROR`. The junction and missing-Python cases stop at the catalog's explicit
`gate-summary.json` existence assertion with
`safe RunRoot did not publish gate-summary.json`; they do not fall through to a
`FileNotFoundError`. The ACL case is distinct: both the temporary resolver and
temporary manifest executable baseline use Task 2 `GetPathIdentity(File,
true)`, so the access probe and provisional gate accept the ACL-restricted
executable and the public behavior fails later instead of publishing the final
readable-identity validation result. In the combined run, at least the ordinary
loose ref, exact `GIT_COMMIT`, ProjectRoot swap, per-worktree namespaces, and
identical-byte post-drain metadata/required-file replacements also reach their
intended missing identity seams. A Python syntax, fixture-control,
junction-cleanup, ACL-setup, missing-test, or unexpected-pass error is not an
acceptable RED.

- [ ] **3.4 minimal GREEN: install the final identity readers and rechecks**

Delete the complete marked `LOOP 3.3 TEMPORARY IDENTITY LAYER`. In P1, delete
the complete temporary Python resolver and restore the printed final
`Resolve-PythonExecutable`; in P2, delete the temporary executable baseline and
restore the printed final `$executableIdentity` assignment. In P4, delete the
complete temporary early Python-resolution region and restore the one printed
in-`try` resolver line after `Assert-GitCommitOverride`. Copy `LOOP 3.4-P1`
between P1/P2, `LOOP 3.4-P2` between P2/P3, and `LOOP 3.4-P3` between P3/P4,
exactly matching the printed final catalog. P4 already contains both calls to
`Get-GateStepDependencyValidationError`, so replacing the temporary helper
activates the pre-launch and post-drain checks without editing P4 in this loop.
The restored `Resolve-PythonExecutable`, `New-GateStep` executable baseline,
and `Get-GateStepDependencyValidationError` current executable all use
`GetReadableFileIdentity` exactly as printed in P1/P2/P3. The two manifest
identity wrappers retain their step/path context and append the inner native
message exactly as printed, so an honest `path identity` / reparse failure
reaches the summary contract.

The restored final P4 resolves Python exactly once after ProjectRoot, HEAD,
`head_token`, head tracking, and `GIT_COMMIT` validation, but before either
manifest is built. Its exact order is safe-tree identities, directory registry,
publication/head defaults, summary object, `SummaryPath`, `try`/diagnostic,
ProjectRoot, HEAD/token/tracking, `GIT_COMMIT`, Python readable identity, then
manifest. Do not retain the temporary early resolver or add a second resolver,
`try`, or summary writer.
Normal refs resolve only from the common Git directory;
`refs/bisect/`, `refs/rewritten/`, and `refs/worktree/` resolve only from the
per-worktree directory and never fall back to common packed refs. Detect
`GIT_COMMIT` presence through the environment dictionary so an explicitly empty
entry fails exact validation. All HEAD/ref/packed-refs reads use the full-chain
readable API and a read-share-only pinned handle. Both `.git` `gitdir:` and
`commondir` reject backslash-root-relative, forward-slash current-drive-rooted,
and drive-relative records. Replacing HEAD or its loose ref with a distinct NTFS
file containing identical bytes is still a metadata-identity failure before the
current result can be published.

Install the three final directory scopes exactly as cataloged:
`Assert-RunTreeDirectoryIdentities` stays base RunRoot/Evidence/Savedirs only;
`Assert-AllGateDirectoryIdentities` checks all registered identities plus
ProjectRoot/HEAD; `Assert-NonEvidenceGateDirectoryIdentities` skips only a
registered identity for which `SameObject(identity, EvidenceIdentity)` is true.
Every registered Evidence descendant remains in the pre-write recheck, along
with all registered non-Evidence directories plus ProjectRoot/HEAD.

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_required_file_parent_junction_is_rejected_before_launch `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_executable_parent_junction_is_rejected_before_launch `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_executable_identity_uses_readable_full_chain_api `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_executable_requires_generic_read_before_launch `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_missing_python_after_safe_tree_publishes_validation_summary `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_project_root_replacement_after_source_is_caught_before_result `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_required_file_replaced_during_child_is_failed_after_tree_drain `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_head_token_uses_real_linked_worktree_packed_ref `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_head_token_uses_real_ordinary_loose_ref_and_exact_git_commit `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_git_indirection_rejects_root_current_drive_and_drive_relative_paths `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_per_worktree_reference_namespaces_never_fall_back_to_common_packed_refs `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_git_metadata_identity_replacement_during_child_fails_before_result `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_linked_worktree_ignores_forged_loose_shared_branch_ref `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_git_head_read_fails_closed_while_a_writer_is_open `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_git_loose_ref_parent_junction_is_rejected_before_launch `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_explicit_empty_git_commit_is_rejected `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_forged_git_commit_is_honest_validation_failure `
  -v
if ($LASTEXITCODE -ne 0) {
  throw 'Identity-stability GREEN failed.'
}
```

Expected GREEN: `Ran 17 tests` and `OK`. The executable junction, ACL negative
control, and missing-Python cases now fail before manifest construction, launch,
or child recording, but after safe summary initialization; each publishes an
honest `failed` / `validation` summary with no steps or per-step leaves. The
junction and ACL cases retain `head_token=no-head`; the missing-Python case
retains the real twelve-character HEAD token. Dynamic or ProjectRoot identity
loss stops the current result and later child; while the base run tree remains
safe, the catch path may publish an authentic `failed` / `validation` summary.
Only base run-tree identity loss suppresses it.

##### Loop 3.5 — close process-tree and evidence-publication races

- [ ] **3.5 RED: add the remaining public and source-contract tests**

On the 3.4 GREEN state, add only these remaining catalog tests:

- `test_json_evidence_writer_is_native_guarded_create_new`
- `test_public_json_create_new_never_overwrites_existing_leaf`
- `test_public_prewrite_identity_check_rejects_concurrent_evidence_rename`
- `test_child_cannot_impersonate_the_gate_owned_summary`
- `test_child_evidence_swap_keeps_streams_in_original_and_stops_writes`
- `test_child_output_leaf_replacement_is_rejected_as_validation`
- `test_partial_output_setup_never_trusts_single_owned_leaf`
- `test_python_timeout_kills_root_and_grandchild`
- `test_normal_root_exit_with_live_grandchild_is_bounded`

The exact recording-child standard-handle constants and swap helpers,
`swap-output-leaves` mode and record field, `_ReadHandleOplock` hierarchy, and
`_GateFixture.start_async` are already present because Loop 3.3 copied the
complete T1A/T1B/T2 regions. Do not copy or redefine them in this loop. For the
two output-ownership cases, add only
`assert_output_evidence_handles_remain_pinned_through_validation` and the two
test methods named above from the exact catalog. The partial setup fixture uses
the two oplock breaks exactly as printed: the executable
break holds the gate before process launch, then the shared Evidence-directory
break inserts the exact unowned stderr leaf after stdout creation and before
stderr `CreateNew`. The source/order helper pins stdout creation before stderr,
post-resume cleanup excluding both output handles, validation before final
output-handle close, classification precedence, and nullable result references.

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_json_evidence_writer_is_native_guarded_create_new `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_public_json_create_new_never_overwrites_existing_leaf `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_public_prewrite_identity_check_rejects_concurrent_evidence_rename `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_child_cannot_impersonate_the_gate_owned_summary `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_child_evidence_swap_keeps_streams_in_original_and_stops_writes `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_child_output_leaf_replacement_is_rejected_as_validation `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_partial_output_setup_never_trusts_single_owned_leaf `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_python_timeout_kills_root_and_grandchild `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_normal_root_exit_with_live_grandchild_is_bounded `
  -v
if ($LASTEXITCODE -eq 0) {
  throw 'Publication-and-drain RED unexpectedly passed before final replacements.'
}
```

Expected RED: the source/order assertions hit the temporary root-accounting
success and the pre-writer all-directory check. The live-grandchild behavior
also exercises a normal root exit rather than the timeout path: it must never
leave either recorded PID alive, even while the temporary source contract is
still RED. The earlier Loops 3.1-3.4 tests remain GREEN. A swap-control error
is a fixture failure, never an accepted validation result.
The output-leaf replacement case is RED because fixed replacement leaves are
still reported as trusted output. The partial-setup case is RED because the
single gate-owned stdout leaf can still make both output references non-null;
the pre-existing stderr bytes and empty child record list distinguish that
setup failure from a launched process.

- [ ] **3.5 minimal GREEN: require authoritative Job zero and pin publication**

Delete the complete `LOOP 3.3 TEMPORARY ROOT-SNAPSHOT ACCOUNTING` method and
insert the complete catalog region `LOOP 3.5-A` at the same C# anchor. Delete
the complete `LOOP 3.3 TEMPORARY PRE-WRITE RECHECK` region inside P4 and insert
the complete catalog region `LOOP 3.5-P1` at the same PowerShell anchor. Also
replace the existing `BoundedProcessResult` with the exact extended definition
printed above; copy the final catalog's output-identity initialization and
creation captures, `ReleaseProcessStartResources`, finalizer validation call,
`ValidateOutputEvidenceBeforeClose`, `ValidateOutputEvidenceStream`, and the
`Invoke-GateStep` output-validation/classification/reference lines. Make no
other edit in this GREEN.

The final accounting re-queries Job basic accounting after the root disappears
and returns success only after `ActiveProcesses == 0`. A positive count records
live descendants, resamples/terminates the recorded Job tree, and keeps the
named Job handle alive until zero is observed. Job-handle close is not treated
as synchronous drain. The final pre-write check covers every registered
directory except the exact baseline Evidence object, including every registered
Evidence descendant, plus ProjectRoot/HEAD. The native writer pins the exact
Evidence object; `Write-GateEvidenceJson` performs the full check after close.
If a started tree returns `TreeDrained=false`, P4 marks evidence publication
unsafe and throws before any result or summary call.

Output evidence starts untrusted. It becomes trusted only when both stdout and
stderr were created with `CreateNew`, proved direct children of the pinned
Evidence object, captured by open-handle identity, and—after no process was
created or the process tree authoritatively drained—each original handle still
has that identity and a direct `CreateFileW` reopen of the canonical fixed leaf
(`FILE_READ_ATTRIBUTES`, share read/write/delete, `OPEN_EXISTING`,
`FILE_FLAG_OPEN_REPARSE_POINT`) matches it by `SameStablePath`. The parent keeps
both output handles open through this validation. An output mismatch is
`failure_kind=validation` after start and before timeout/tree/exit
classification, with both result references null; a partial setup remains a
`failure_kind=process` start failure and also has both references null. The
existing unowned-summary and post-run dependency validations retain priority,
and an undrained tree still takes the evidence-publication hard stop before a
result can be written.

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_json_evidence_writer_is_native_guarded_create_new `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_public_json_create_new_never_overwrites_existing_leaf `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_public_prewrite_identity_check_rejects_concurrent_evidence_rename `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_child_cannot_impersonate_the_gate_owned_summary `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_child_evidence_swap_keeps_streams_in_original_and_stops_writes `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_child_output_leaf_replacement_is_rejected_as_validation `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_partial_output_setup_never_trusts_single_owned_leaf `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_python_timeout_kills_root_and_grandchild `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_normal_root_exit_with_live_grandchild_is_bounded `
  -v
if ($LASTEXITCODE -ne 0) {
  throw 'Publication-and-drain GREEN failed.'
}
```

Expected GREEN: `Ran 9 tests` and `OK`. The output replacement case reports
`validation`, leaves both fixed references null, and proves the moved leaves—not
the forged fixed leaves—contain the child's real stdout/stderr. The partial
setup case reports `process_started=false` / `process`, leaves both references
null, preserves the unowned stderr bytes, and records no child. The normal-root
leak case reports
`process_tree`, `timed_out=false`, `tree_drained=true`, and
`had_live_descendants_after_root_exit=true`, with both recorded PIDs exited.
The pre-write public race is explicitly
the outer identity-check regression: its oplock callback handle-renames Evidence
and immediately acknowledges/releases the break without creating a junction;
the renamed original receives no result/summary and the old Evidence name stays
absent. The child-driven swap case separately covers a post-resume junction and
redirected target. The Loop 3.2 exact-source black box is the proof of the native
writer's live-handle window. The source contract additionally proves the
`TreeDrained=false` branch contains no result/summary call and that a successful
drain is guarded by authoritative Job active-process zero.

#### Final verification and the single amend

- [ ] **Run the complete gate suite after all five loops**

```powershell
python -m unittest Tools.test_winter_interlude_gate -v
if ($LASTEXITCODE -ne 0) { throw 'Full public-gate tests failed.' }
git diff --check
if ($LASTEXITCODE -ne 0) { throw 'Whitespace validation failed.' }
```

Expected: `Ran 52 tests` and `OK`; all Task 1-3 tests pass together. In
particular, the temporary
source-only Structural bridge remains an honest exit-1 boundary for Task 4;
there is no environment success bypass, injected executor, or second
`Add-Type`.

- [ ] **Stage exactly the two implementation files and amend once**

```powershell
git add -- Tools/Run-WinterInterludeGate.ps1 Tools/test_winter_interlude_gate.py
if ($LASTEXITCODE -ne 0) { throw 'Could not stage Task 3 files.' }
$staged = @(git diff --cached --name-only)
if ($LASTEXITCODE -ne 0) { throw 'Could not inspect staged Task 3 files.' }
$expected = @(
  'Tools/Run-WinterInterludeGate.ps1',
  'Tools/test_winter_interlude_gate.py'
)
if (@(Compare-Object $expected $staged).Count -ne 0) {
  throw "Unexpected staged Task 3 files: $($staged -join ', ')"
}
git diff --cached --check
if ($LASTEXITCODE -ne 0) { throw 'Task 3 staged whitespace validation failed.' }
git commit --amend --no-edit
if ($LASTEXITCODE -ne 0) { throw 'Could not amend the Task 3 implementation.' }
```

Expected: the existing implementation commit is amended exactly once; no new
commit is created. Task 4 receives the named source-bridge boundary and expands
the manifest without adding another process seam.

---

### Task 4: Complete the Structural manifest and exact evidence contract

**Files:**

- Modify: `Tools/test_winter_interlude_gate.py`
- Modify: `Tools/Run-WinterInterludeGate.ps1`

**Interfaces:**

- Consumes the Task 3 public source-step bridge and the approved public gate.
- Produces the exact source-contract plus five-suite Structural manifest, unique
  external savedirs, schema-v1 result/summary evidence, and fail-fast behavior.
- Keeps Task 3's exact native/path helper contracts:

```powershell
# Path helpers supplied by the preceding task.
# Resolve-GateProject -ProjectRoot <path> -WasSpecified <bool>
#   -> WinterGate.PathIdentity
# Resolve-PythonExecutable -> WinterGate.PathIdentity
# New-VerifiedRunRoot -Candidate <path> -CandidateWasSpecified <bool>
#   -ProjectIdentity <identity> -ProtectedSavePaths <string[]> ->
#   PSCustomObject { Identity; EvidenceIdentity; SavedirsIdentity }
# New-VerifiedChildDirectory -ParentIdentity <identity> -LeafName <one plain leaf>
#   -> WinterGate.PathIdentity
# Assert-GatePathState -ExpectedIdentity <identity> -Label <text>
#   -> the freshly reopened matching identity; mismatch throws
#   WinterGate.WinterGatePathIdentityException
# Assert-RunTreeDirectoryIdentities and Assert-AllGateDirectoryIdentities
#   call Assert-GatePathState with | Out-Null and emit no pipeline values.
# Get-ExpectedProjectFilePath <final project root> <fixed repo-relative path>
# WinterGate.Native.SameStablePath(expected, actual) -> bool
# WinterGate.Native.TryGetReadableFileIdentity(path) -> PathIdentity or null
# WinterGate.Native.GetReadableFileIdentity(path) -> PathIdentity
#   Both open with GENERIC_READ, FILE_SHARE_READ | FILE_SHARE_WRITE (no delete),
#   OPEN_EXISTING, FILE_FLAG_OPEN_REPARSE_POINT | FILE_FLAG_BACKUP_SEMANTICS,
#   and reject reparse points.
#   New-GateStep uses TryGetReadableFileIdentity for RequiredFileIdentities;
#   Invoke-GateStep uses GetReadableFileIdentity for every non-null recheck.
# WinterGate.Native.ReadVerifiedUtf8TextFile(path, expectedIdentity, maximumBytes)
#   -> strict UTF-8 text read through the same verified, no-delete file handle.
# WinterGate.Native.RunProcessTree(
#   executable, arguments, workingDirectory, stdoutPath, stderrPath,
#   timeoutMilliseconds, expectedEvidenceDirectoryIdentity)
#   -> WinterGate.BoundedProcessResult. The native engine uses the pinned
#   evidence identity to validate stdout/stderr as direct children. It releases
#   its evidence-directory guard after suspended-process Job assignment and
#   stream final-path validation but before ResumeThread, preserving the
#   deterministic child-driven evidence-junction swap test.
# WinterGate.Native.WriteOwnedSummaryUtf8Json(
#   path, normalJson, collisionFailureJson,
#   expectedEvidenceDirectoryIdentity) -> evidence-relative string or null
#   opens a GUID create-new staging leaf, quarantines any unowned fixed
#   gate-summary.json to gate-summary.unowned.<nonce>.json, writes and flushes
#   collisionFailureJson when a collision was quarantined (normalJson
#   otherwise), atomically renames the staging object without replacement, and
#   verifies SameObject and SameStablePath through reopened handles.
#   Write-GateSummaryJson is its only PowerShell caller. There is no cross-child
#   summary reservation.
```

Task 3 initializes these script-scoped values before either manifest is built:

```powershell
$script:ProjectIdentity
$script:RunRootIdentity
$script:EvidenceIdentity
$script:SavedirsIdentity
$script:PythonIdentity
$script:TrustedPowerShellIdentity
$script:GateDirectoryIdentities = New-Object 'System.Collections.Generic.List[object]'
$script:EvidencePublicationSafe = $true
$script:SummaryCommittedByGate = $false
$script:SummaryPublicationAttempted = $false
$script:QuarantinedSummaryPath = $null
$script:SummaryPath = Join-Path $script:EvidenceIdentity.FinalPath 'gate-summary.json'
```

- [ ] **Step 1: Add the exact Structural black-box tests**

Task 3 defines the complete
`_GateBlackBoxCase.make_project()` shared harness before its process test class;
Task 4 consumes that concrete base. Its returned fixture has:

- `root`, `run_root`, `python_exe`, `records_path`, and test-owned `appdata` paths;
- `run(gate, phase="Final", *, documents=None, raw_documents=None,
  exit_codes=None, precreate_after=None, replace_required_after=None,
  extra_environment=None, close_fds=True, tool_timeout_seconds=30,
  wall_timeout_seconds=65)`, which invokes the real public
  `Run-WinterInterludeGate.ps1` in the trusted Desktop PowerShell process;
- `records()`, which returns the child JSONL records in launch order;
- `summary()`, which reads `evidence/gate-summary.json` from that invocation;
- `result(ordinal)`, which reads that step's result JSON;
- `output_path(step_name)`, which returns the exact scanner output path; and
- `close()`, which removes only the fixture-owned temporary tree after the gate
  process and every recorded child have exited.

`documents` maps a step name to the JSON value the recording `python.exe`
writes to that step's gate-supplied output. `raw_documents` takes precedence
and writes the supplied text byte-for-byte. `exit_codes` maps a manifest ordinal
to a child exit code. `precreate_after` maps a completed ordinal to the
project-relative evidence leaf which that child creates before it exits. These
are controls of the external fake executable, never gate parameters or gate
environment switches. Task 3's recording child implements the required-file
replacement control with a prepared same-directory leaf plus native
`MoveFileExW(MOVEFILE_REPLACE_EXISTING | MOVEFILE_WRITE_THROUGH)`; a control
failure is recorded and fails the fixture instead of being mistaken for a gate
success.

Task 3 also has the temporary Bootstrap method
`test_valid_call_reaches_source_bridge_with_honest_validation_summary`.
Delete exactly that method while adding the complete Structural class below;
its source-child coverage is strictly subsumed by
`test_structural_runs_exact_source_then_five_suites`. Retain the separate,
persistent ProcessTests JSON-writer contract and
`test_child_cannot_impersonate_the_gate_owned_summary`; the latter remains the
public proof that a source child which creates the fixed summary leaf is failed
immediately, launches no later child, and leaves its bytes only in one
`gate-summary.unowned.<nonce>.json` quarantine leaf.

At the same time, rename the one existing class declaration
`WinterInterludeGateBootstrapTests` in place to
`WinterInterludeGateInterfaceTests`. Replace the existing declaration line with
this exact line:

```text
class WinterInterludeGateInterfaceTests(unittest.TestCase):
```

Change only that declaration: do not copy the class body, retain a second
Bootstrap class, or redefine any of its three remaining tests. At module scope,
immediately after the existing `POWERSHELL` definition and before `run_gate`,
add this tuple exactly once:

```python
STRUCTURAL_SUITES = (
    "test_winter_interlude_state",
    "test_winter_interlude_routing",
    "test_winter_interlude_ending_invariance",
    "test_winter_interlude_route_matrix",
    "test_winter_interlude_mid_save",
)
```

Migrate exactly these five persistent `WinterInterludeGateProcessTests` methods
in place; do not copy or redefine them, and do not retroactively change their
Task 3 catalog forms:

- `test_head_token_uses_real_linked_worktree_packed_ref`
- `test_head_token_uses_real_ordinary_loose_ref_and_exact_git_commit`
- `test_per_worktree_reference_namespaces_never_fall_back_to_common_packed_refs`
- `test_linked_worktree_ignores_forged_loose_shared_branch_ref`
- `test_public_process_uses_exact_argv_job_nul_and_handle_list`

Replace the complete first four methods with these exact final methods:

```python
    def test_head_token_uses_real_linked_worktree_packed_ref(self) -> None:
        head = self.fixture.use_linked_worktree_with_packed_refs()

        completed = self.fixture.run("Structural")

        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertEqual(6, len(self.fixture.records()))
        summary = self.fixture.summary()
        self.assertEqual("passed", summary["status"])
        self.assertIsNone(summary["failure_kind"])
        self.assertIsNone(summary["error"])
        self.assertEqual(head[:12], summary["head_token"])
        self.assertEqual(6, len(summary["steps"]))
        result_relative = str(summary["steps"][0]["result"])
        self.assertIn(f"-{head[:12]}.result.json", result_relative)
        self.assertTrue(
            evidence_file(self.fixture.run_root, result_relative).is_file()
        )

    def test_head_token_uses_real_ordinary_loose_ref_and_exact_git_commit(self) -> None:
        head = self.fixture.initialize_git_repo()

        completed = self.fixture.run(
            "Structural",
            extra_environment={"GIT_COMMIT": head},
        )

        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertEqual(6, len(self.fixture.records()))
        summary = self.fixture.summary()
        self.assertEqual("passed", summary["status"])
        self.assertIsNone(summary["failure_kind"])
        self.assertIsNone(summary["error"])
        self.assertEqual(head[:12], summary["head_token"])
        self.assertEqual(6, len(summary["steps"]))
        self.assertEqual(
            f"structural-01-source-contract-{head[:12]}.result.json",
            Path(str(summary["steps"][0]["result"])).name,
        )

    def test_per_worktree_reference_namespaces_never_fall_back_to_common_packed_refs(
        self,
    ) -> None:
        for namespace in ("bisect", "rewritten", "worktree"):
            for loose_present in (True, False):
                with self.subTest(
                    namespace=namespace,
                    loose_present=loose_present,
                ):
                    fixture = self.make_project()
                    try:
                        head = fixture.use_linked_worktree_with_packed_refs()
                        linked_gitdir, common_gitdir = (
                            fixture.linked_git_directories()
                        )
                        reference = f"refs/{namespace}/gate"
                        (linked_gitdir / "HEAD").write_text(
                            f"ref: {reference}\n",
                            encoding="ascii",
                        )
                        forged = "0" * len(head)
                        if forged == head:
                            forged = "1" * len(head)
                        packed_refs = common_gitdir / "packed-refs"
                        packed_bytes = packed_refs.read_bytes()
                        separator = b"" if packed_bytes.endswith(b"\n") else b"\n"
                        packed_refs.write_bytes(
                            packed_bytes
                            + separator
                            + f"{forged} {reference}\n".encode("ascii")
                        )
                        if loose_present:
                            loose_ref = linked_gitdir / Path(
                                *reference.split("/")
                            )
                            loose_ref.parent.mkdir(parents=True, exist_ok=True)
                            loose_ref.write_text(head + "\n", encoding="ascii")

                        completed = fixture.run("Structural")

                        summary = fixture.summary()
                        if loose_present:
                            self.assertEqual(
                                0, completed.returncode, completed.stderr
                            )
                            self.assertEqual(6, len(fixture.records()))
                            self.assertEqual(head[:12], summary["head_token"])
                            self.assertEqual("passed", summary["status"])
                            self.assertIsNone(summary["failure_kind"])
                            self.assertIsNone(summary["error"])
                            self.assertEqual(6, len(summary["steps"]))
                        else:
                            self.assertEqual(
                                1, completed.returncode, completed.stderr
                            )
                            self.assertEqual([], fixture.records())
                            self.assertEqual("failed", summary["status"])
                            self.assertEqual(
                                "validation",
                                summary["failure_kind"],
                            )
                            self.assertIn(
                                "Git HEAD reference has no current commit",
                                summary["error"],
                            )
                    finally:
                        fixture.close()

    def test_linked_worktree_ignores_forged_loose_shared_branch_ref(self) -> None:
        head = self.fixture.use_linked_worktree_with_packed_refs()
        gitdir_line = (self.fixture.root / ".git").read_text(
            encoding="utf-8"
        ).strip()
        linked_gitdir = Path(gitdir_line.removeprefix("gitdir: "))
        forged_ref = linked_gitdir / "refs" / "heads" / "gate-linked"
        forged_ref.parent.mkdir(parents=True, exist_ok=True)
        forged = "0" * len(head)
        if forged == head:
            forged = "1" * len(head)
        forged_ref.write_text(forged + "\n", encoding="ascii")

        completed = self.fixture.run("Structural")

        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertEqual(6, len(self.fixture.records()))
        summary = self.fixture.summary()
        self.assertEqual("passed", summary["status"])
        self.assertIsNone(summary["failure_kind"])
        self.assertIsNone(summary["error"])
        self.assertEqual(head[:12], summary["head_token"])
        self.assertEqual(6, len(summary["steps"]))
```

In `test_public_process_uses_exact_argv_job_nul_and_handle_list`, replace the
existing span from `records = read_json_lines(self.record)` through
`python_record = records[0]` with this exact block. This deletes the old stderr
forced-boundary assertion while retaining the following argv, Job, NUL, handle
list, and source-engine ordering assertions unchanged:

```python
        records = read_json_lines(self.record)
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertEqual(6, len(records))
        python_record = records[0]
```

Later in that same method, replace the existing span from
`summary = self.load_summary(run_root)` through `first = summary["steps"][0]`
with this exact block. Retain every following BOM, source process/timing,
stdout, and stderr evidence assertion unchanged:

```python
        summary = self.load_summary(run_root)
        self.assertEqual("passed", summary["status"])
        self.assertIsNone(summary["failure_kind"])
        self.assertIsNone(summary["error"])
        self.assertEqual(6, len(summary["steps"]))
        first = summary["steps"][0]
```

These five final methods preserve their original
HEAD/result/packed-reference/argv/Job/NUL/source-evidence contracts. Every
success branch requires return code zero, six child records, six summary steps,
a passed summary, and null failure/error fields. The per-worktree method's
`loose_present=False` branch instead requires return code one, no child records,
a failed validation summary, and the current
`Git HEAD reference has no current commit` error.

Replace Task 3's entire `FAKE_RUNNER_SOURCE` constant with the complete source
below. The normal-leak mode records a real grandchild and lets the runner root
exit; `timeout-tree` records the same tree and leaves both processes alive for
the gate-owned outer watchdog. There is no splice or retained old tail.

```python
FAKE_RUNNER_SOURCE = r'''
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)][string]$ProjectRoot,
    [Parameter(Mandatory = $true)][string]$SaveDir,
    [Parameter(Mandatory = $true)][string]$Mode,
    [Parameter(Mandatory = $true)][string]$Suite,
    [Parameter(Mandatory = $true)][string]$Expect,
    [Parameter(Mandatory = $true)][string]$EvidenceDir,
    [Parameter(Mandatory = $true)][int]$TimeoutSeconds
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$existingRecords = if ([IO.File]::Exists($env:WINTER_GATE_RECORD)) {
    @([IO.File]::ReadAllLines($env:WINTER_GATE_RECORD) | Where-Object {
        -not [string]::IsNullOrWhiteSpace($_)
    }).Count
} else { 0 }
$ordinal = $existingRecords + 1
$record = [ordered]@{
    kind = 'RenPySuite'
    step = $Suite.Replace('_', '-')
    ordinal = $ordinal
    argv = @($MyInvocation.UnboundArguments)
    cwd = [Environment]::CurrentDirectory
    pid = $PID
    child_pid = $null
    suite = $Suite
    parameters = [ordered]@{
        ProjectRoot = $ProjectRoot
        SaveDir = $SaveDir
        Mode = $Mode
        Suite = $Suite
        Expect = $Expect
        EvidenceDir = $EvidenceDir
        TimeoutSeconds = $TimeoutSeconds
    }
    control_error = $null
}
$runnerMode = $env:WINTER_GATE_RUNNER_MODE
if ($env:WINTER_GATE_RUNNER_LEAK_SUITE -eq $Suite -or
    $runnerMode -eq 'timeout-tree') {
    $child = Start-Process `
        -FilePath $env:WINTER_GATE_FAKE_PYTHON `
        -ArgumentList '--winter-gate-grandchild' `
        -WindowStyle Hidden `
        -PassThru
    $record.child_pid = $child.Id
}
$replaceSuite = $env:WINTER_GATE_REPLACE_DIRECTORY_SUITE
if (-not [string]::IsNullOrWhiteSpace($replaceSuite) -and
    $replaceSuite -eq $Suite) {
    try {
        $source = $env:WINTER_GATE_REPLACE_DIRECTORY_SOURCE
        $target = $env:WINTER_GATE_REPLACE_DIRECTORY_TARGET
        $backup = $env:WINTER_GATE_REPLACE_DIRECTORY_BACKUP
        foreach ($required in @($source, $target, $backup)) {
            if ([string]::IsNullOrWhiteSpace($required)) {
                throw 'Directory-replacement control requires three paths.'
            }
        }
        [IO.Directory]::Move($target, $backup)
        [IO.Directory]::Move($source, $target)
    } catch {
        $record.control_error = $_.Exception.Message
    }
}
$json = $record | ConvertTo-Json -Compress -Depth 8
[IO.File]::AppendAllText(
    $env:WINTER_GATE_RECORD,
    $json + [Environment]::NewLine,
    [Text.UTF8Encoding]::new($false))
[Console]::Out.WriteLine('PASSED fake-runner-stdout')
[Console]::Error.WriteLine('fake-runner-stderr')
if ($null -ne $record.control_error) { exit 97 }
if ($runnerMode -eq 'timeout-tree') {
    while ($true) { Start-Sleep -Seconds 60 }
}
$exitCode = 0
if ([IO.File]::Exists($env:WINTER_GATE_CONTROL)) {
    $control = [IO.File]::ReadAllText(
        $env:WINTER_GATE_CONTROL,
        [Text.Encoding]::UTF8) | ConvertFrom-Json
    $property = $control.exit_codes.PSObject.Properties[[string]$ordinal]
    if ($null -ne $property) { $exitCode = [int]$property.Value }
}
exit $exitCode
'''
```

Add the following test bodies. They compare observations of real child
processes and retained evidence; none parse the Markdown plan.

`test_hanging_runner_root_and_descendant_are_killed_at_outer_bound` is the one
approved exception to the plan's 2–5 minute focused-test rule: the public
contract fixes `RenPyTimeoutSeconds` at a minimum of 300 and fixes the wrapper
grace at 60 seconds. Shortening either value through a test-only parameter or
bypass would stop testing the public bound. Every other focused RED/GREEN loop
in Tasks 4–5 remains under five minutes.

```python
class WinterInterludeGateManifestTests(_GateBlackBoxCase):
    def setUp(self) -> None:
        self.fixture = self.make_project()

    def tearDown(self) -> None:
        self.fixture.close()

    def test_structural_runs_exact_source_then_five_suites(self) -> None:
        completed = self.fixture.run("Structural")
        self.assertEqual(completed.returncode, 0, completed.stderr)
        records = self.fixture.records()
        self.assertEqual(len(records), 6)
        self.assertEqual(
            records[0]["argv"],
            ["-m", "unittest", "Tools.test_governance_winter_interlude", "-v"],
        )
        self.assertEqual(records[0]["kind"], "Python")
        self.assertEqual(
            [record["suite"] for record in records[1:]],
            list(STRUCTURAL_SUITES),
        )
        self.assertTrue(all(record["kind"] == "RenPySuite" for record in records[1:]))
        self.assertTrue(all(record["cwd"] == str(self.fixture.root) for record in records))
        summary = self.fixture.summary()
        self.assertEqual(
            [step["name"] for step in summary["steps"]],
            ["source-contract", *[suite.replace("_", "-") for suite in STRUCTURAL_SUITES]],
        )
        self.assertEqual(
            summary["steps"][0]["arguments"],
            ["-m", "unittest", "Tools.test_governance_winter_interlude", "-v"],
        )
        self.assertTrue(os.path.samefile(
            summary["steps"][0]["executable"], self.fixture.python_exe
        ))
        self.assertTrue(all(
            os.path.samefile(step["executable"], POWERSHELL)
            for step in summary["steps"][1:]
        ))
        runner = self.fixture.root / "Tools" / "Run-RenPySuite.ps1"
        for ordinal, (suite, step) in enumerate(
            zip(STRUCTURAL_SUITES, summary["steps"][1:]), start=2
        ):
            self.assertEqual(
                step["arguments"],
                [
                    "-NoLogo", "-NoProfile", "-NonInteractive",
                    "-ExecutionPolicy", "Bypass", "-File", str(runner),
                    "-ProjectRoot", str(self.fixture.root),
                    "-SaveDir", str(
                        self.fixture.run_root / "savedirs" / f"{ordinal:02d}-{suite}"
                    ),
                    "-Mode", "Suite", "-Suite", suite, "-Expect", "PASSED",
                    "-EvidenceDir", str(self.fixture.run_root / "evidence" / "runner"),
                    "-TimeoutSeconds", "300",
                ],
            )

    def test_structural_suite_savedirs_are_unique_external_empty_and_exact(self) -> None:
        completed = self.fixture.run("Structural")
        records = self.fixture.records()[1:]
        self.assertEqual(len(records), len(STRUCTURAL_SUITES))
        self.assertEqual(
            len(self.fixture.summary()["steps"][1:]),
            len(STRUCTURAL_SUITES),
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        savedirs = [Path(record["parameters"]["SaveDir"]) for record in records]
        self.assertEqual(len(savedirs), len(set(savedirs)))
        for ordinal, (suite, record, savedir) in enumerate(
            zip(STRUCTURAL_SUITES, records, savedirs), start=2
        ):
            self.assertEqual(savedir.name, f"{ordinal:02d}-{suite}")
            self.assertTrue(savedir.is_absolute())
            self.assertNotEqual(self.fixture.root, savedir)
            self.assertNotIn(self.fixture.root, savedir.parents)
            self.assertEqual(record["parameters"]["ProjectRoot"], str(self.fixture.root))
            self.assertEqual(record["parameters"]["Mode"], "Suite")
            self.assertEqual(record["parameters"]["Suite"], suite)
            self.assertEqual(record["parameters"]["Expect"], "PASSED")
            self.assertEqual(record["parameters"]["TimeoutSeconds"], 300)
            self.assertEqual(list(savedir.iterdir()), [])

    def test_structural_evidence_schema_and_artifacts_are_exact(self) -> None:
        completed = self.fixture.run("Structural")
        self.assertEqual(completed.returncode, 0, completed.stderr)
        summary = self.fixture.summary()
        self.assertEqual(set(summary), {
            "schema_version", "gate", "narrative_phase", "status",
            "failure_kind", "error", "started_utc", "ended_utc", "head_token",
            "host", "project_root", "run_root", "steps",
        })
        self.assertEqual(summary["schema_version"], 1)
        self.assertEqual(summary["gate"], "Structural")
        self.assertIsNone(summary["narrative_phase"])
        self.assertEqual(summary["status"], "passed")
        self.assertIsNone(summary["failure_kind"])
        self.assertIsNone(summary["error"])
        self.assertEqual(summary["head_token"], "no-head")
        self.assertEqual(set(summary["host"]), {"edition", "version", "executable"})
        self.assertEqual(summary["host"]["edition"], "Desktop")
        self.assertTrue(summary["host"]["version"].startswith("5."))
        for identity_name in ("project_root", "run_root"):
            self.assertEqual(set(summary[identity_name]), {
                "final_path", "volume_serial_number", "file_index",
            })
        self.assertEqual(set(summary["host"]["executable"]), {
            "final_path", "volume_serial_number", "file_index",
        })
        expected_step_keys = {
            "ordinal", "name", "kind", "executable", "arguments",
            "working_directory", "process_started", "process_id",
            "started_utc", "ended_utc", "exit_code", "timed_out",
            "tree_drained", "had_live_descendants_after_root_exit",
            "elapsed_milliseconds", "stdout", "stderr", "result",
            "postcondition", "manual_review_required", "status",
            "failure_kind", "error",
        }
        for ordinal, step in enumerate(summary["steps"], start=1):
            self.assertEqual(set(step), expected_step_keys)
            self.assertEqual(step["ordinal"], ordinal)
            self.assertTrue(step["process_started"])
            self.assertIsInstance(step["process_id"], int)
            self.assertEqual(step["exit_code"], 0)
            self.assertFalse(step["timed_out"])
            self.assertTrue(step["tree_drained"])
            self.assertFalse(step["had_live_descendants_after_root_exit"])
            self.assertEqual(step["status"], "passed")
            self.assertIsNone(step["failure_kind"])
            self.assertIsNone(step["error"])
            self.assertFalse(step["manual_review_required"])
            for field in ("stdout", "stderr", "result"):
                relative = Path(step[field])
                self.assertFalse(relative.is_absolute())
                self.assertTrue((self.fixture.run_root / relative).is_file())
            prefix = f"evidence/structural-{ordinal:02d}-{step['name']}-no-head"
            self.assertEqual(step["stdout"], prefix + ".stdout.txt")
            self.assertEqual(step["stderr"], prefix + ".stderr.txt")
            self.assertEqual(step["result"], prefix + ".result.json")
            result_document = json.loads(
                (self.fixture.run_root / step["result"]).read_text(encoding="utf-8")
            )
            self.assertEqual(result_document, step)

    def test_structural_failure_is_fail_fast_at_every_ordinal(self) -> None:
        for failing_ordinal in range(1, 7):
            with self.subTest(failing_ordinal=failing_ordinal):
                fixture = self.make_project()
                try:
                    completed = fixture.run(
                        "Structural", exit_codes={failing_ordinal: 23}
                    )
                    self.assertNotEqual(completed.returncode, 0)
                    self.assertEqual(len(fixture.records()), failing_ordinal)
                    summary = fixture.summary()
                    self.assertEqual(len(summary["steps"]), failing_ordinal)
                    self.assertEqual(summary["steps"][-1]["failure_kind"], "process")
                    self.assertEqual(summary["steps"][-1]["exit_code"], 23)
                finally:
                    fixture.close()

    def test_runner_root_exit_with_live_descendant_is_failed_and_drained(self) -> None:
        started = time.monotonic()
        completed = self.fixture.run(
            "Structural",
            extra_environment={
                "WINTER_GATE_RUNNER_LEAK_SUITE": STRUCTURAL_SUITES[0]
            },
            wall_timeout_seconds=65,
        )
        wall_elapsed = time.monotonic() - started
        self.assertNotEqual(completed.returncode, 0)
        self.assertLess(wall_elapsed, 60.0)
        records = self.fixture.records()
        self.assertEqual(len(records), 2)
        runner = records[1]
        self.assertEqual(runner["kind"], "RenPySuite")
        self.assertEqual(runner["suite"], STRUCTURAL_SUITES[0])
        self.assertIsInstance(runner["pid"], int)
        self.assertIsInstance(runner["child_pid"], int)
        summary = self.fixture.summary()
        self.assertEqual(len(summary["steps"]), 2)
        failed = summary["steps"][1]
        self.assertEqual(failed["name"], "test-winter-interlude-state")
        self.assertEqual(failed["failure_kind"], "process_tree")
        self.assertFalse(failed["timed_out"])
        self.assertTrue(failed["tree_drained"])
        self.assertTrue(failed["had_live_descendants_after_root_exit"])
        assert_processes_exit(
            self,
            int(runner["pid"]),
            int(runner["child_pid"]),
        )

    def test_hanging_runner_root_and_descendant_are_killed_at_outer_bound(self) -> None:
        renpy_timeout_seconds = 300
        outer_bound_seconds = renpy_timeout_seconds + 60
        started = time.monotonic()
        completed = self.fixture.run(
            "Structural",
            extra_environment={"WINTER_GATE_RUNNER_MODE": "timeout-tree"},
            wall_timeout_seconds=390,
        )
        wall_elapsed = time.monotonic() - started
        self.assertNotEqual(completed.returncode, 0)
        self.assertGreaterEqual(wall_elapsed, outer_bound_seconds - 5.0)
        self.assertLess(wall_elapsed, outer_bound_seconds + 25.0)
        records = self.fixture.records()
        self.assertEqual(len(records), 2)
        self.assertEqual(records[1]["kind"], "RenPySuite")
        self.assertEqual(
            records[1]["parameters"]["TimeoutSeconds"],
            renpy_timeout_seconds,
        )
        self.assertIsInstance(records[1]["pid"], int)
        self.assertIsInstance(records[1]["child_pid"], int)
        summary = self.fixture.summary()
        self.assertEqual(len(summary["steps"]), 2)
        timed_out = summary["steps"][1]
        self.assertEqual(timed_out["name"], "test-winter-interlude-state")
        self.assertEqual(timed_out["failure_kind"], "timeout")
        self.assertTrue(timed_out["timed_out"])
        self.assertTrue(timed_out["tree_drained"])
        self.assertGreaterEqual(
            timed_out["elapsed_milliseconds"],
            (outer_bound_seconds - 5) * 1000,
        )
        self.assertLess(
            timed_out["elapsed_milliseconds"],
            (outer_bound_seconds + 25) * 1000,
        )
        assert_processes_exit(
            self,
            int(records[1]["pid"]),
            int(records[1]["child_pid"]),
        )

    def test_runner_required_file_identity_is_rechecked_before_first_suite(self) -> None:
        runner = self.fixture.root / "Tools" / "Run-RenPySuite.ps1"
        completed = self.fixture.run(
            "Structural", replace_required_after={1: runner}
        )
        self.assertNotEqual(completed.returncode, 0)
        self.assertEqual(
            [record["step"] for record in self.fixture.records()],
            ["source-contract"],
        )
        summary = self.fixture.summary()
        self.assertEqual(len(summary["steps"]), 2)
        self.assertEqual(summary["steps"][0]["status"], "passed")
        failed = summary["steps"][1]
        self.assertEqual(failed["name"], "test-winter-interlude-state")
        self.assertEqual(failed["failure_kind"], "validation")
        self.assertFalse(failed["process_started"])
        self.assertFalse(failed["timed_out"])
        self.assertTrue(failed["tree_drained"])
        self.assertFalse(failed["had_live_descendants_after_root_exit"])
        self.assertEqual(failed["status"], "failed")
        self.assertIsInstance(failed["error"], str)
        self.assertTrue(failed["error"])
        for field in (
            "process_id", "started_utc", "ended_utc", "exit_code",
            "elapsed_milliseconds", "stdout", "stderr",
        ):
            self.assertIsNone(failed[field], field)
        self.assertEqual(
            json.loads(
                (self.fixture.run_root / failed["result"]).read_text(
                    encoding="utf-8"
                )
            ),
            failed,
        )

    def test_registered_gate_directories_are_rechecked_before_next_launch(self) -> None:
        cases = (
            (
                "future-suite-savedir",
                Path("savedirs") / "03-test_winter_interlude_routing",
            ),
            ("runner-evidence", Path("evidence") / "runner"),
        )
        for label, relative_target in cases:
            with self.subTest(label=label):
                fixture = self.make_project()
                try:
                    source = fixture.base / f"{label}-replacement-source"
                    backup = fixture.base / f"{label}-original-backup"
                    source.mkdir()
                    (source / "replacement-marker.txt").write_text(
                        label, encoding="utf-8"
                    )
                    target = fixture.run_root / relative_target
                    completed = fixture.run(
                        "Structural",
                        extra_environment={
                            "WINTER_GATE_REPLACE_DIRECTORY_SUITE":
                                STRUCTURAL_SUITES[0],
                            "WINTER_GATE_REPLACE_DIRECTORY_SOURCE": str(source),
                            "WINTER_GATE_REPLACE_DIRECTORY_TARGET": str(target),
                            "WINTER_GATE_REPLACE_DIRECTORY_BACKUP": str(backup),
                        },
                    )

                    self.assertNotEqual(completed.returncode, 0)
                    self.assertEqual(
                        [record["step"] for record in fixture.records()],
                        ["source-contract", "test-winter-interlude-state"],
                    )
                    self.assertEqual(
                        (target / "replacement-marker.txt").read_text(
                            encoding="utf-8"
                        ),
                        label,
                    )
                    self.assertTrue(backup.is_dir())
                    evidence = fixture.run_root / "evidence"
                    for ordinal in (2, 3):
                        self.assertEqual(
                            [],
                            list(evidence.glob(
                                f"structural-{ordinal:02d}-*.result.json"
                            )),
                        )
                    summary = fixture.summary()
                    self.assertEqual(summary["status"], "failed")
                    self.assertEqual(summary["failure_kind"], "validation")
                    self.assertRegex(summary["error"], r"(?i)path identity")
                    self.assertEqual(
                        [step["name"] for step in summary["steps"]],
                        ["source-contract"],
                    )
                finally:
                    fixture.close()
```

- [ ] **Step 2: Run the Structural tests RED through the public entrypoint**

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateManifestTests `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_head_token_uses_real_linked_worktree_packed_ref `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_head_token_uses_real_ordinary_loose_ref_and_exact_git_commit `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_per_worktree_reference_namespaces_never_fall_back_to_common_packed_refs `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_linked_worktree_ignores_forged_loose_shared_branch_ref `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_public_process_uses_exact_argv_job_nul_and_handle_list `
  -v 2>&1 |
  Tee-Object -FilePath .superpowers/sdd/task-7-5-structural-manifest-red.txt
if ($LASTEXITCODE -eq 0) { throw 'Structural manifest RED unexpectedly passed.' }
```

Expected: `Ran 13 tests` and a nonzero result. The eight new manifest tests and
five migrated persistent ProcessTests all reach Task 3's real source-contract
child, then fail on the source-only forced boundary or the absent five suite
records/savedirs. A missing test, duplicate definition, or fixture error is not
an acceptable RED.

- [ ] **Step 3: Replace the Task 3 Structural bridge with the exact six-step manifest**

Replace `Get-StructuralGateManifest` with this complete function. Also delete
the complete region from
`# BEGIN TASK 3 SOURCE-BRIDGE FORCED VALIDATION` through
`# END TASK 3 SOURCE-BRIDGE FORCED VALIDATION`; that region changes the
otherwise-passed Structural summary to `status='failed'`,
`failure_kind='validation'`, and the exact error
`structural manifest layer not implemented`. The marked Task 3 region also has
the temporary Narrative message, so delete the whole marked region. Narrative
remains fail-closed in Task 4 because its provisional `capability-json`
postcondition is still rejected by `Invoke-GateStep`. The finished six-step
Structural invocation must write a passed summary and return exit 0; do not add
a probe or a test-only bypass. In Task 3's provisional `Invoke-GateStep`,
replace its unavailable-postcondition guard exactly as follows so the existing
runner's exit-zero contract can pass:

```powershell
elseif ($Step.Postcondition -notin @('exit-zero', 'runner-passed')) {
    $failureKind = 'validation'
    $errorText =
        "Postcondition '$($Step.Postcondition)' is not available before Task 5."
}
```

Retain Task 3's `Assert-AllGateDirectoryIdentities` call at the beginning of
`Invoke-GateStep`. After `RunProcessTree`, retain the exact Task 3 order: first
hard-stop a started, undrained tree; then compute the post-drain dependency
validation and unowned-summary state; then call
`Assert-NonEvidenceGateDirectoryIdentities` immediately before result
classification/publication. Do not add or restore
`Assert-AllGateDirectoryIdentities` after `RunProcessTree`. Both helpers must
keep their `Assert-GatePathState ... | Out-Null` bodies. `Assert-GatePathState`
returns a fresh identity; calling it bare here would put identities on the
success pipeline beside the one step result and corrupt `summary.steps`.

Retain Task 3's `$script:EvidencePublicationSafe = $true` initialization and
the top-level catch guard which bare-rethrows when that flag is false. Task 4's
runner descendant and timeout cases both drain successfully and therefore
still write honest `process_tree`/`timeout` results. A returned
`ProcessStarted=true, TreeDrained=false` must set the flag false and throw before
any result or summary JSON is published.

Also retain Task 3's atomic summary publisher unchanged. There is no open
summary handle while a child runs. Immediately after a safely drained child,
`Invoke-GateStep` checks `$script:SummaryPath` with
`TryGetReadableFileIdentity`; an unowned fixed summary takes validation
precedence, so that current step keeps its real process/timing fields but is
failed before any later child launches. Only after the manifest loop has
returned from every launched child with a safely drained Job may the top level
call `Write-GateSummaryJson`. That wrapper constructs both the normal document
and an exact failed/validation collision document, sets
`$script:SummaryPublicationAttempted = $true` before its one native call,
records the returned evidence-relative quarantine path in
`$script:QuarantinedSummaryPath`, and sets
`$script:SummaryCommittedByGate = $true` only after the native commit returns.
Thus a collision appearing after the step check is still quarantined and the
fixed gate-owned document is still the failure form.

Every top-level catch must first bare-rethrow when
`$script:EvidencePublicationSafe` is false. A catch may attempt one failed
summary only when both `$script:SummaryCommittedByGate` and
`$script:SummaryPublicationAttempted` are false; it must not infer ownership
from `[IO.File]::Exists($script:SummaryPath)`. The path-identity catch first
rechecks only RunRoot/evidence/savedirs through
`Assert-RunTreeDirectoryIdentities`: if that recheck fails it rethrows the
original path error without creating a summary; if the run tree remains pinned,
it may call `Write-GateSummaryJson -RunTreeOnly` for an honest failure. Per-step
result files continue through `Write-GateEvidenceJson` and its guarded native
create-new writer; they are never reservations and are never overwritten.

Then replace the Structural manifest:

```powershell
function Get-StructuralGateManifest {
    $sourceContract = Get-ExpectedProjectFilePath `
        $script:ProjectIdentity.FinalPath 'Tools\test_governance_winter_interlude.py'
    $runner = Get-ExpectedProjectFilePath `
        $script:ProjectIdentity.FinalPath 'Tools\Run-RenPySuite.ps1'
    $runnerEvidenceIdentity = New-VerifiedChildDirectory `
        -ParentIdentity $script:EvidenceIdentity -LeafName 'runner'
    [void]$script:GateDirectoryIdentities.Add($runnerEvidenceIdentity)

    $steps = New-Object 'System.Collections.Generic.List[object]'
    [void]$steps.Add((New-GateStep `
        'source-contract' 'Python' $script:PythonIdentity.FinalPath `
        ([string[]]@('-m', 'unittest', 'Tools.test_governance_winter_interlude', '-v')) `
        $ToolTimeoutSeconds 'exit-zero' ([string[]]@($sourceContract))))

    $suites = [string[]]@(
        'test_winter_interlude_state',
        'test_winter_interlude_routing',
        'test_winter_interlude_ending_invariance',
        'test_winter_interlude_route_matrix',
        'test_winter_interlude_mid_save'
    )
    for ($index = 0; $index -lt $suites.Count; $index++) {
        $ordinal = $index + 2
        $suite = $suites[$index]
        $saveIdentity = New-VerifiedChildDirectory `
            -ParentIdentity $script:SavedirsIdentity `
            -LeafName ('{0:D2}-{1}' -f $ordinal, $suite)
        [void]$script:GateDirectoryIdentities.Add($saveIdentity)
        $arguments = [string[]]@(
            '-NoLogo', '-NoProfile', '-NonInteractive',
            '-ExecutionPolicy', 'Bypass', '-File', $runner,
            '-ProjectRoot', $script:ProjectIdentity.FinalPath,
            '-SaveDir', $saveIdentity.FinalPath,
            '-Mode', 'Suite', '-Suite', $suite,
            '-Expect', 'PASSED',
            '-EvidenceDir', $runnerEvidenceIdentity.FinalPath,
            '-TimeoutSeconds', [string]$RenPyTimeoutSeconds
        )
        [void]$steps.Add((New-GateStep `
            $suite.Replace('_', '-') 'RenPySuite' `
            $script:TrustedPowerShellIdentity.FinalPath $arguments `
            ($RenPyTimeoutSeconds + 60) 'runner-passed' `
            ([string[]]@($runner))))
    }
    [object[]]$steps.ToArray()
}
```

Immediately after the main function selects either manifest and before it
launches ordinal one, add the shared uniqueness check:

```powershell
$manifestNames = [string[]]@($manifest | ForEach-Object { $_.Name })
if (($manifestNames | Select-Object -Unique).Count -ne $manifestNames.Count) {
    throw 'Manifest step names are not unique.'
}
```

- [ ] **Step 4: Run the complete Structural slice GREEN**

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateInterfaceTests `
  Tools.test_winter_interlude_gate.WinterInterludeGatePathSafetyTests `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests `
  Tools.test_winter_interlude_gate.WinterInterludeGateManifestTests -v
if ($LASTEXITCODE -ne 0) { throw 'Structural public-gate slice failed.' }

python -m unittest Tools.test_winter_interlude_gate -v
if ($LASTEXITCODE -ne 0) { throw 'Full public-gate tests failed after Structural.' }
```

Expected: `Ran 57 tests`, exit 0, and `OK`; the public Structural gate emits
exactly six passed results, five unique empty external savedirs, and a schema-v1
summary. The immediately guarded full-module command then reports
`Ran 59 tests` and `OK`, including the two one-test native probe classes omitted
from the focused slice.

- [ ] **Step 5: Amend the in-progress executable-gate implementation commit**

```powershell
git add -- Tools/Run-WinterInterludeGate.ps1 Tools/test_winter_interlude_gate.py
if ($LASTEXITCODE -ne 0) { throw 'Could not stage the Structural manifest slice.' }
$staged = @(git diff --cached --name-only)
if ($LASTEXITCODE -ne 0) { throw 'Could not inspect the Structural staged scope.' }
if ($staged.Count -ne 2 -or
    $staged -notcontains 'Tools/Run-WinterInterludeGate.ps1' -or
    $staged -notcontains 'Tools/test_winter_interlude_gate.py') {
  throw "Unexpected Structural staged scope: $($staged -join ', ')"
}
git diff --cached --check
if ($LASTEXITCODE -ne 0) { throw 'Structural staged diff check failed.' }
git commit --amend --no-edit
if ($LASTEXITCODE -ne 0) { throw 'Could not amend the Structural manifest slice.' }
```

### Task 5: Complete Narrative in three capability-first TDD loops

**Files:**

- Modify: `Tools/test_winter_interlude_gate.py`
- Modify: `Tools/Run-WinterInterludeGate.ps1`

**Interfaces:**

- Consumes Task 4's six-step Structural GREEN gate, Task 3's shared
  `_GateBlackBoxCase`/`_GateFixture`, and the exact native/path interfaces listed
  in Task 4.
- Produces a capability-first one-step vertical slice with strict JSON and
  gate-owned structured-output reservations, then the exact nine-step
  Batch/Final manifest, then fail-closed canon/common-scanner schemas and the
  approved JSON failure precedence.
- Every machine JSON output is derived from
  `{gate-lower}-{ordinal:D2}-{step}-{head-token}.output.json`. The portrait
  output is the only nested case:
  `evidence/portrait/narrative-04-missing-portraits-<head>.output.json`.
- Keeps `Step` objects at the exact Task 3 shape:
  `Name/Kind/Executable/ExecutableIdentity/Arguments/TimeoutSeconds/Postcondition/RequiredFiles/RequiredFileIdentities`.
- Retains Task 3's `$script:EvidencePublicationSafe` unsafe-live-tree circuit
  breaker: a started, undrained tree publishes neither result nor summary.
- Retains Task 3's **summary-only** no-reservation ownership protocol:
  `Write-GateSummaryJson` is called only after all launched Jobs are confirmed
  drained, publishes through `WriteOwnedSummaryUtf8Json`, and uses both
  `$script:SummaryPublicationAttempted` and
  `$script:SummaryCommittedByGate` rather than fixed-leaf existence to decide
  whether a catch still owns one summary attempt. The Task 5 dispatcher retains
  Task 3's post-drain unowned-summary check and validation precedence; it does
  not weaken this top-level protocol. Machine JSON uses the separate Task 5
  owner-handle reservation below; never apply the summary protocol to a
  structured-output leaf.
- Uses the future Task 8 portrait interface
  `scan_missing_portraits.py --format json --output <exact-file>`. Task 8 must
  implement this exact `--output` option; `--output-dir` plus a fixed
  `missing-portraits.json` leaf is not compatible with the evidence-name
  contract.
- In gate mode `--output` is the naming/audit contract, not write authority.
  Every machine-JSON child receives only the gate-owned duplicate named by
  `WINTER_GATE_STRUCTURED_OUTPUT_HANDLE`; path reopen, path replacement, and
  fallback to `--output` are forbidden. Task 6 carries this exact boundary to
  the future Task 8 delivery plan.

**Task 5 final overlay catalog and application order:** Task 3's earlier exact
catalog is the Task 1--4 baseline. Apply the Task 5 overlays below only in the
named loop; do not copy the final nine-step form of
`test_valid_batch_capability_uses_full_stem_and_passes` into Loop A. The final
module has exactly these class counts:

```text
WinterInterludeGateInterfaceTests          3
WinterInterludeGatePathSafetyTests        18
WinterInterludeGateNativeFoundationTests   1
WinterInterludeGateNativeWriterTests       1
WinterInterludeGateProcessTests           28
WinterInterludeGateCapabilityTests        13
WinterInterludeGateNarrativeManifestTests  5
WinterInterludeGateScannerEvidenceTests    7
WinterInterludeGateManifestTests           8
TOTAL                                     84
```

The complete Task 5 test overlay consists of the following exact symbols. A
symbol already present in the Task 1--4 baseline is replaced in place; all
others are inserted at the named anchor. No helper may be duplicated:

```text
after compile_path_trap, before _compile_parent_identity_harness:
  compile_strict_json_probe

inside _GateFixture:
  replace _output_paths
  replace start_writer_race

after passing_narrative_documents:
  assert_structured_reservation_close_order
  assert_strict_json_validation_order

WinterInterludeGateProcessTests replacements (method count unchanged):
  test_partial_output_setup_never_trusts_single_owned_leaf
  test_normal_root_exit_with_live_grandchild_is_bounded
  test_public_process_uses_exact_argv_job_nul_and_handle_list

WinterInterludeGateCapabilityTests final 13-method catalog:
  test_control_oplock_breaks_for_readable_identity_flags
  test_valid_batch_capability_uses_full_stem_and_passes
  test_real_project_is_capability_first_when_checker_is_absent
  test_capability_rejects_malformed_schema_tool_and_property_count
  test_strict_json_rejects_non_rfc8259_lexemes
  test_strict_json_rejects_decoded_duplicate_object_keys
  test_strict_json_resource_boundaries_are_exact
  test_strict_json_strings_diagnostics_and_layering_are_exact
  test_gate_owned_reservation_blocks_concurrent_path_writers
  test_capability_false_flag_beats_nonzero_exit
  test_final_rejects_batch_only_capability
  test_capability_missing_output_precedence_is_exact
  test_python_executable_identity_is_rechecked_before_first_child

Loop B:
  replace the Loop-A form of test_valid_batch_capability_uses_full_stem_and_passes
  add WinterInterludeGateNarrativeManifestTests (5 methods)

Loop C:
  add WinterInterludeGateScannerEvidenceTests (7 methods)
```

The complete Task 5 production overlay consists of these exact symbols and
placements. Treat the list as a copy boundary: a later catalog block replaces
the whole named symbol, never a hand-merged fragment:

```text
Native constants/classes:
  ProcessQueryLimitedInformation = 0x00001000
  DuplicateSameAccess = 0x00000002
  StillActive = 259
  MaximumJsonDepth = 64
  MaximumJsonDocumentCharacters = 1048576
  MaximumJsonNumberTokenLength = 128
  StructuredOutputHandleEnvironmentVariable
  StructuredOutputMarkerPrefix
  StructuredOutputSnapshot
  StructuredOutputReservation

Native public/private methods:
  ValidateStrictJson
  ReserveStructuredOutput
  FreezeStructuredOutput
  BuildChildEnvironmentBlock
  FreezeStructuredOutputCore
  StrictJsonParser
  ObserveRootAccountingExit
  TryIsProcessRunning

Process bridge replacements:
  RunProcessTree(..., StructuredOutputReservation structuredOutputReservation)
  exact conditional 3/4-handle list
  scrub/inject WINTER_GATE_STRUCTURED_OUTPUT_HANDLE
  close structuredOutputChildHandle in the native finally

PowerShell helper block, contiguous and before
Get-GateStepDependencyValidationError:
  Get-GateArtifactStem
  Get-GateStructuredOutputPath
  Get-GateStructuredOutputDirectoryIdentity
  Get-NarrativeGateManifest
  Close-GateStructuredOutputReservations
  Assert-ExactJsonProperties
  Assert-JsonInteger
  Assert-ProjectRelativeJsonPath
  Assert-JsonFinding
  Read-GateStructuredJson
  Get-GateJsonOutcome

Dispatcher/global replacements:
  Invoke-GateStep
  $script:StructuredOutputReservations initialization
  outer try/catch/finally disposal after Invoke-WinterInterludeGate and summary
```

Two earlier baseline catalog corrections are part of this overlay even though
they add no test methods: the manifest uniqueness check is exactly
`@($manifestNames | Select-Object -Unique).Count`, and every copy of
`ObserveRootAccountingExit`/`TryIsProcessRunning` must use the terminating-tail
accounting contract in Step 3. These corrections are E1 and E4 respectively;
E2 is the helper placement above, and E3 is the removal of managed structured
leaf existence/identity decisions from the dispatcher.

#### Loop A: capability JSON and the prelaunch executable identity seam

- [ ] **Step 1: Add the capability-only RED tests and deterministic oplock barrier**

Task 3's shared harness already imports `ctypes`, `re`, `threading`, and
`wintypes` and already defines `_Overlapped`. Do not re-import or redefine any
of them. Add exactly `from collections.abc import Callable` beside the other
imports; the reservation race uses that annotation.
Add only this new constant and these new helpers beside that harness. Insert
`compile_strict_json_probe` immediately after `compile_path_trap`, before
`_compile_parent_identity_harness`; add the two source-order helpers beside the
other shared Narrative document helpers. The source-order helpers are part of
the behavioral mutation evidence, not substitutes for the public tests:

```python
TARGET = "game/governance_winter_interlude.rpy"


def capability_document(phase: str, *, final_contracts: bool) -> dict[str, object]:
    return {
        "schema_version": 1,
        "tool": "winter_narrative_capabilities",
        "phase": phase,
        "ready": True,
        "capabilities": {
            "canon_json": True,
            "portrait_json": True,
            "overlap_json": True,
            "show_before_json": True,
            "nested_quote_json": True,
            "batch_contracts": True,
            "final_contracts": final_contracts,
        },
    }


EMPTY_CANON = {
    "schema_version": 1,
    "tool": "canon",
    "blocking_count": 0,
    "anti_logic": [],
    "geography": [],
    "terminology": [],
    "canon_deviation": [],
    "informational_occurrences": [],
}

SCANNER_TO_TOOL = {
    "missing-portraits": "missing_portraits",
    "narration-overlap": "narration_overlap",
    "show-before": "show_before_prevention",
    "nested-quotes": "nested_quotes",
}


def empty_scanner_document(step_name: str) -> dict[str, object]:
    return {
        "schema_version": 1,
        "tool": SCANNER_TO_TOOL[step_name],
        "scanned_files": [TARGET],
        "blocking_count": 0,
        "findings": [],
    }


def passing_narrative_documents(phase: str) -> dict[str, dict[str, object]]:
    return {
        "narrative-capability": capability_document(
            phase, final_contracts=(phase == "final")
        ),
        "canon": json.loads(json.dumps(EMPTY_CANON)),
        **{
            name: empty_scanner_document(name)
            for name in SCANNER_TO_TOOL
        },
    }


def compile_strict_json_probe(executable: Path) -> None:
    source_text = _production_native_source() + r'''

namespace WinterGate
{
    internal static class StrictJsonProbe
    {
        public static int Main(string[] arguments)
        {
            if (arguments.Length != 1)
            {
                return 2;
            }
            try
            {
                string json = File.ReadAllText(
                    arguments[0],
                    new UTF8Encoding(false, true));
                Native.ValidateStrictJson(json);
                return 0;
            }
            catch (FormatException exception)
            {
                Console.Error.WriteLine(exception.Message);
                return 91;
            }
            catch (Exception exception)
            {
                Console.Error.WriteLine(exception.ToString());
                return 92;
            }
        }
    }
}
'''
    _compile_csharp(
        executable,
        source_text,
        main="WinterGate.StrictJsonProbe",
        label="strict JSON probe",
    )


def assert_structured_reservation_close_order(
    case: unittest.TestCase,
    source: str,
) -> None:
    dispatcher = source[
        source.index("function Invoke-GateStep {") :
        source.index("function Invoke-WinterInterludeGate {")
    ]
    case.assertEqual(1, dispatcher.count(".Dispose()"))
    case.assertIn("$unregisteredReservation.Dispose()", dispatcher)
    case.assertNotIn("$jsonReservation.Dispose()", dispatcher)

    invocation_start = source.index("function Invoke-WinterInterludeGate {")
    invocation_end = source.index(
        "# END LOOP 3.3-P4 PROCESS MAPPING AND PUBLIC BRIDGE SHELL"
    )
    invocation = source[invocation_start:invocation_end]
    case.assertNotIn("Close-GateStructuredOutputReservations", invocation)
    case.assertNotIn(".Dispose()", invocation)

    global_tail = source[invocation_end:]
    case.assertEqual(
        1,
        global_tail.count("Close-GateStructuredOutputReservations"),
    )
    invoke_call = global_tail.index("Invoke-WinterInterludeGate")
    finally_block = global_tail.index("finally {")
    close_call = global_tail.index("Close-GateStructuredOutputReservations")
    exit_call = global_tail.index("exit $exitCode")
    case.assertLess(invoke_call, finally_block)
    case.assertLess(finally_block, close_call)
    case.assertLess(close_call, exit_call)


def assert_strict_json_validation_order(
    case: unittest.TestCase,
    source: str,
) -> None:
    reader = source[
        source.index("function Read-GateStructuredJson {") :
        source.index("function Get-GateJsonOutcome {")
    ]
    strict_call = "    [WinterGate.Native]::ValidateStrictJson($raw)"
    case.assertEqual(1, reader.count(strict_call))
    case.assertLess(reader.index("$raw = "), reader.index(strict_call))
    case.assertLess(reader.index(strict_call), reader.index("ConvertFrom-Json"))


class _LevelOneOplock:
    GENERIC_READ = 0x80000000
    FILE_SHARE_ALL = 0x00000007
    OPEN_EXISTING = 3
    FILE_ATTRIBUTE_NORMAL = 0x00000080
    FILE_FLAG_OVERLAPPED = 0x40000000
    FSCTL_REQUEST_OPLOCK_LEVEL_1 = 0x00090000
    ERROR_IO_PENDING = 997
    WAIT_OBJECT_0 = 0

    def __init__(self, path: Path) -> None:
        self.kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
        self.close_handle = self.kernel32.CloseHandle
        self.close_handle.argtypes = [wintypes.HANDLE]
        self.close_handle.restype = wintypes.BOOL

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
        invalid_handle = ctypes.c_void_p(-1).value
        handle = create_file(
            str(path),
            self.GENERIC_READ,
            self.FILE_SHARE_ALL,
            None,
            self.OPEN_EXISTING,
            self.FILE_ATTRIBUTE_NORMAL | self.FILE_FLAG_OVERLAPPED,
            None,
        )
        if not handle or int(handle) == invalid_handle:
            raise ctypes.WinError(ctypes.get_last_error())
        self.file_handle: int | None = int(handle)

        create_event = self.kernel32.CreateEventW
        create_event.argtypes = (
            ctypes.c_void_p,
            wintypes.BOOL,
            wintypes.BOOL,
            wintypes.LPCWSTR,
        )
        create_event.restype = wintypes.HANDLE
        event = create_event(None, True, False, None)
        if not event:
            self.release()
            raise ctypes.WinError(ctypes.get_last_error())
        self.event_handle: int | None = int(event)
        self.overlapped = _Overlapped()
        self.overlapped.hEvent = wintypes.HANDLE(self.event_handle)

        device_io = self.kernel32.DeviceIoControl
        device_io.argtypes = (
            wintypes.HANDLE,
            wintypes.DWORD,
            ctypes.c_void_p,
            wintypes.DWORD,
            ctypes.c_void_p,
            wintypes.DWORD,
            ctypes.POINTER(wintypes.DWORD),
            ctypes.POINTER(_Overlapped),
        )
        device_io.restype = wintypes.BOOL
        returned = wintypes.DWORD()
        ok = device_io(
            wintypes.HANDLE(self.file_handle),
            self.FSCTL_REQUEST_OPLOCK_LEVEL_1,
            None,
            0,
            None,
            0,
            ctypes.byref(returned),
            ctypes.byref(self.overlapped),
        )
        error = ctypes.get_last_error()
        if ok or error != self.ERROR_IO_PENDING:
            self.close()
            if ok:
                raise AssertionError("Level-1 oplock request completed synchronously")
            raise ctypes.WinError(error)

    def wait_for_break(self, timeout_milliseconds: int) -> None:
        wait = self.kernel32.WaitForSingleObject
        wait.argtypes = (wintypes.HANDLE, wintypes.DWORD)
        wait.restype = wintypes.DWORD
        status = wait(
            wintypes.HANDLE(self.event_handle),
            wintypes.DWORD(timeout_milliseconds),
        )
        if status != self.WAIT_OBJECT_0:
            raise AssertionError(
                f"gate did not reach the checker identity barrier: wait={status}"
            )

    def release(self) -> None:
        if self.file_handle is not None:
            handle, self.file_handle = self.file_handle, None
            if not self.close_handle(wintypes.HANDLE(handle)):
                raise ctypes.WinError(ctypes.get_last_error())

    def close(self) -> None:
        self.release()
        if getattr(self, "event_handle", None) is not None:
            handle, self.event_handle = self.event_handle, None
            if not self.close_handle(wintypes.HANDLE(handle)):
                raise ctypes.WinError(ctypes.get_last_error())


def _move_file_replace_existing(source: Path, target: Path) -> None:
    move = ctypes.WinDLL("kernel32", use_last_error=True).MoveFileExW
    move.argtypes = (wintypes.LPCWSTR, wintypes.LPCWSTR, wintypes.DWORD)
    move.restype = wintypes.BOOL
    flags = 0x00000001 | 0x00000008
    if not move(str(source), str(target), flags):
        raise ctypes.WinError(ctypes.get_last_error())


def _open_with_readable_identity_flags(
    path: Path, errors: list[BaseException]
) -> None:
    try:
        generic_read = 0x80000000
        file_share_read = 0x00000001
        file_share_write = 0x00000002
        open_existing = 3
        file_attribute_normal = 0x00000080
        file_flag_open_reparse_point = 0x00200000
        file_flag_backup_semantics = 0x02000000
        kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
        create_file = kernel32.CreateFileW
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
            generic_read,
            file_share_read | file_share_write,
            None,
            open_existing,
            file_attribute_normal
            | file_flag_open_reparse_point
            | file_flag_backup_semantics,
            None,
        )
        if not handle or int(handle) == ctypes.c_void_p(-1).value:
            raise ctypes.WinError(ctypes.get_last_error())
        close_windows_handle(int(handle))
    except BaseException as error:
        errors.append(error)


def run_narrative_with_prelaunch_python_swap(
    fixture: _GateFixture,
) -> subprocess.CompletedProcess[str]:
    if fixture.has_run:
        raise AssertionError("Each fake-project fixture supports one gate run.")
    fixture.has_run = True
    fixture._write_control(
        documents={
            "narrative-capability": capability_document(
                "batch", final_contracts=False
            )
        },
        raw_documents=None,
        exit_codes=None,
        precreate_after=None,
        replace_required_after=None,
        replace_identity_after=None,
    )
    environment = os.environ.copy()
    environment.pop("GIT_COMMIT", None)
    environment.update(
        {
            "APPDATA": str(fixture.appdata),
            "PATH": str(fixture.fake_bin)
            + os.pathsep
            + environment.get("PATH", ""),
            "WINTER_GATE_RECORD": str(fixture.records_path),
            "WINTER_GATE_CONTROL": str(fixture.control_path),
            "WINTER_GATE_FAKE_PYTHON": str(fixture.python_exe),
            "WINTER_GATE_FAKE_MODE": "normal",
            "WINTER_GATE_TRUSTED_POWERSHELL": str(POWERSHELL),
        }
    )
    command = [
        str(POWERSHELL),
        "-NoLogo",
        "-NoProfile",
        "-NonInteractive",
        "-ExecutionPolicy",
        "Bypass",
        "-File",
        str(GATE),
        "-Gate",
        "Narrative",
        "-ProjectRoot",
        str(fixture.root),
        "-RunRoot",
        str(fixture.run_root),
        "-ToolTimeoutSeconds",
        "30",
        "-RenPyTimeoutSeconds",
        "300",
        "-NarrativePhase",
        "Batch",
    ]

    checker = fixture.root / "Tools" / "check_winter_narrative_capabilities.py"
    replacement = fixture._stage_replacement(
        fixture.python_exe, "prelaunch-python"
    )
    barrier = _LevelOneOplock(checker)
    gate_process: subprocess.Popen[str] | None = None
    try:
        gate_process = subprocess.Popen(
            command,
            cwd=fixture.root,
            env=environment,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            close_fds=True,
        )
        barrier.wait_for_break(15_000)
        _move_file_replace_existing(replacement, fixture.python_exe)
        barrier.release()
        stdout, stderr = gate_process.communicate(timeout=65)
    except BaseException:
        barrier.release()
        if gate_process is not None and gate_process.poll() is None:
            gate_process.kill()
            gate_process.communicate(timeout=10)
        raise
    finally:
        barrier.close()

    control_errors = [
        str(record["control_error"])
        for record in fixture.records()
        if record.get("control_error")
    ]
    if control_errors:
        raise AssertionError("; ".join(control_errors))
    return subprocess.CompletedProcess(
        command, gate_process.returncode, stdout, stderr
    )
```

Replace the Task 3 `start_writer_race` fixture method with this form before
adding the reservation test. Loop A calls it with `gate="Narrative"`, phase
`Batch`, and a stage-local empty document map; Loop B later supplies the final
nine-step document map without changing this helper again:

```python
    def start_writer_race(
        self,
        ready_path: Path,
        release_path: Path,
        *,
        gate: str = "Structural",
        phase: str = "Final",
        documents: dict[str, object] | None = None,
    ) -> subprocess.Popen[str]:
        if self.has_run:
            raise AssertionError("Each fake-project fixture supports one gate run.")
        self.has_run = True
        self._write_control(
            documents=documents,
            raw_documents=None,
            exit_codes=None,
            precreate_after=None,
            replace_required_after=None,
            replace_identity_after=None,
        )
        environment = os.environ.copy()
        environment.pop("GIT_COMMIT", None)
        environment.update(
            {
                "APPDATA": str(self.appdata),
                "PATH": str(self.fake_bin)
                + os.pathsep
                + environment.get("PATH", ""),
                "WINTER_GATE_RECORD": str(self.records_path),
                "WINTER_GATE_CONTROL": str(self.control_path),
                "WINTER_GATE_FAKE_PYTHON": str(self.python_exe),
                "WINTER_GATE_FAKE_MODE": "writer-race",
                "WINTER_GATE_TRUSTED_POWERSHELL": str(POWERSHELL),
                "WINTER_GATE_WRITER_RACE_READY": str(ready_path),
                "WINTER_GATE_WRITER_RACE_RELEASE": str(release_path),
            }
        )
        command = [
            str(POWERSHELL),
            "-NoLogo",
            "-NoProfile",
            "-NonInteractive",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            str(GATE),
            "-Gate",
            gate,
            "-ProjectRoot",
            str(self.root),
            "-RunRoot",
            str(self.run_root),
            "-ToolTimeoutSeconds",
            "30",
            "-RenPyTimeoutSeconds",
            "300",
        ]
        if gate == "Narrative":
            command.extend(["-NarrativePhase", phase])
        return subprocess.Popen(
            command,
            cwd=self.root,
            env=environment,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            close_fds=True,
        )
```

In `RECORDING_CHILD_SOURCE`, add
`using Microsoft.Win32.SafeHandles;`, add
`HandleFlagInherit = 0x00000001`, use the already-cataloged
`SetHandleInformation`, `GetFinalPathNameByHandleW`, and `NormalizeFinalPath`
helpers, and replace `WriteControlledDocument` completely with:

```csharp
private static void WriteControlledDocument(
    Dictionary<string, object> control,
    string step,
    string[] arguments,
    bool inExpectedJob,
    bool inJob)
{
    Dictionary<string, object> documents = ObjectMap(
        control,
        "raw_documents");
    Dictionary<string, object> outputs = ObjectMap(
        control,
        "output_paths");
    object outputValue;
    if (!outputs.TryGetValue(step, out outputValue))
    {
        if (inExpectedJob && !String.IsNullOrEmpty(
            Environment.GetEnvironmentVariable(
                "WINTER_GATE_STRUCTURED_OUTPUT_HANDLE")))
        {
            throw new InvalidDataException(
                "A non-structured gate step inherited a structured output handle.");
        }
        return;
    }
    string output = Convert.ToString(outputValue);
    if (!ContainsExactArgument(arguments, output))
    {
        throw new InvalidDataException(
            "Gate did not pass the controlled output path for " + step + ".");
    }

    object raw;
    bool hasDocument = documents.TryGetValue(step, out raw);
    if (inExpectedJob)
    {
        string rawHandle = Environment.GetEnvironmentVariable(
            "WINTER_GATE_STRUCTURED_OUTPUT_HANDLE");
        long handleValue;
        if (String.IsNullOrEmpty(rawHandle) ||
            !Int64.TryParse(
                rawHandle,
                System.Globalization.NumberStyles.None,
                System.Globalization.CultureInfo.InvariantCulture,
                out handleValue) ||
            handleValue <= 0)
        {
            throw new InvalidDataException(
                "A structured gate step did not inherit a valid output handle.");
        }

        IntPtr handle = new IntPtr(handleValue);
        StringBuilder finalPathBuffer = new StringBuilder(32768);
        uint finalPathLength = GetFinalPathNameByHandleW(
            handle,
            finalPathBuffer,
            checked((uint)finalPathBuffer.Capacity),
            0);
        if (finalPathLength == 0 ||
            finalPathLength >= finalPathBuffer.Capacity)
        {
            throw new System.ComponentModel.Win32Exception(
                Marshal.GetLastWin32Error(),
                "Could not resolve the inherited structured output handle.");
        }
        string finalPath = Path.GetFullPath(
            NormalizeFinalPath(finalPathBuffer.ToString()));
        string expectedPath = Path.GetFullPath(output);
        if (!String.Equals(
            finalPath,
            expectedPath,
            StringComparison.OrdinalIgnoreCase))
        {
            throw new InvalidDataException(
                "The inherited structured output handle did not match --output.");
        }
        if (!SetHandleInformation(handle, HandleFlagInherit, 0))
        {
            throw new System.ComponentModel.Win32Exception(
                Marshal.GetLastWin32Error(),
                "Could not clear structured output handle inheritance.");
        }

        using (SafeFileHandle safeHandle = new SafeFileHandle(handle, true))
        {
            if (!hasDocument)
            {
                return;
            }
            byte[] encoded = new UTF8Encoding(false).GetBytes(
                Convert.ToString(raw));
            using (FileStream stream = new FileStream(
                safeHandle,
                FileAccess.ReadWrite))
            {
                stream.Position = 0;
                stream.SetLength(0);
                stream.Write(encoded, 0, encoded.Length);
                stream.Flush(true);
            }
        }
        return;
    }

    if (inJob)
    {
        throw new InvalidDataException(
            "A Job-contained structured producer cannot use a path fallback.");
    }
    if (!hasDocument)
    {
        return;
    }
    Directory.CreateDirectory(Path.GetDirectoryName(output));
    byte[] standaloneEncoded = new UTF8Encoding(false).GetBytes(
        Convert.ToString(raw));
    using (FileStream stream = new FileStream(
        output,
        FileMode.CreateNew,
        FileAccess.Write,
        FileShare.None))
    {
        stream.Write(standaloneEncoded, 0, standaloneEncoded.Length);
        stream.Flush(true);
    }
}
```

Pass both `inExpectedJob` and `inJob` at its one call site, and add the exact
record field below so tests can distinguish a gate-issued handle from ambient
state:

```csharp
record["structured_output_handle"] = Environment.GetEnvironmentVariable(
    "WINTER_GATE_STRUCTURED_OUTPUT_HANDLE");
```

The oplock is held on the capability checker, not on either executable. Task 3
captures required files through `TryGetReadableFileIdentity`; its exact
`GENERIC_READ` open breaks this oplock after `New-GateStep` has captured the
fake Python identity. The test process replaces the not-yet-running executable
and releases the checker oplock. If production captures the executable after
the barrier or omits its prelaunch recheck, the fake child launches and the
test fails. Do not restore Task 3's removed `replace_executable_after` control.

Replace these three existing Process methods in place. They are Task 5
hardening of Task 3 behavior, so they do not change the 28-method Process class
count:

```python
class WinterInterludeGateProcessTests(_GateBlackBoxCase):
    def test_partial_output_setup_never_trusts_single_owned_leaf(self) -> None:
        executable_oplock = _FileReadHandleOplock(self.fake_python)
        self.addCleanup(executable_oplock.close)
        process = self.fixture.start_async()

        def stop_process() -> None:
            if process.poll() is None:
                process.kill()
            process.communicate(timeout=10)

        self.addCleanup(stop_process)
        executable_oplock.wait_for_break()
        evidence = self.fixture.run_root / "evidence"
        self.assertTrue(evidence.is_dir(), evidence)
        output_oplock = _SharedDirectoryMutationOplock(evidence)
        self.addCleanup(output_oplock.close)
        executable_oplock.release()
        output_oplock.wait_for_break()

        stdout_path = (
            evidence / "structural-01-source-contract-no-head.stdout.txt"
        )
        stderr_path = (
            evidence / "structural-01-source-contract-no-head.stderr.txt"
        )
        with stderr_path.open("xb") as stream:
            stream.write(b"UNOWNED-STDERR\n")
        output_oplock.release()

        gate_stdout, gate_stderr = process.communicate(timeout=30)
        self.assertEqual(1, process.returncode, gate_stdout + gate_stderr)
        self.assertTrue(stdout_path.is_file(), stdout_path)
        self.assertEqual(b"", stdout_path.read_bytes())
        self.assertEqual(b"UNOWNED-STDERR\n", stderr_path.read_bytes())
        self.assertEqual([], self.fixture.records())
        summary = self.fixture.summary()
        self.assertEqual("failed", summary["status"])
        self.assertEqual("process", summary["failure_kind"])
        self.assertEqual(1, len(summary["steps"]))
        summary_step = summary["steps"][0]
        result_path = evidence_file(self.fixture.run_root, summary_step["result"])
        result = json.loads(result_path.read_text(encoding="utf-8-sig"))
        diagnostic = {"summary_step": summary_step, "result": result}
        for document in (summary_step, result):
            self.assertIs(False, document["process_started"], diagnostic)
            self.assertEqual("failed", document["status"], diagnostic)
            self.assertEqual("process", document["failure_kind"], diagnostic)
            self.assertRegex(
                document["error"],
                r"(?i)CreateFileW\(stderr\)|already exists|error (?:80|183)",
            )
            self.assertIsNone(document["stdout"], diagnostic)
            self.assertIsNone(document["stderr"], diagnostic)

    def test_normal_root_exit_with_live_grandchild_is_bounded(self) -> None:
        source = GATE.read_text(encoding="utf-8")
        observe_start = source.index(
            "private static bool ObserveRootAccountingExit("
        )
        observe_end = source.index(
            "private static bool TryGetJobProcessIds(", observe_start
        )
        observe = source[observe_start:observe_end]
        active_without_running_pid = """                if (activeProcesses == 0)
                {
                    return true;
                }
                if (accountingClock.ElapsedMilliseconds >= CleanupTimeoutMilliseconds)
                {
                    AddEngineError(
                        result,
                        "Job Object accounting remained active without a running " +
                        "process ID after the accounting bound.");
                    return false;
                }
                Thread.Sleep(CleanupPollMilliseconds);
                continue;
"""
        self.assertIn(active_without_running_pid, observe)
        self.assertNotIn(
            """                hadDescendant = true;
                return true;
""",
            observe[observe.index("if (!rootStillListed)") :],
        )
        self.assertIn(
            "private const uint ProcessQueryLimitedInformation = 0x00001000;",
            source,
        )
        self.assertIn("private const uint StillActive = 259;", source)
        running_start = source.index(
            "private static bool TryIsProcessRunning("
        )
        running_end = source.index(
            "private static void CaptureStartedProcessCompletion(",
            running_start,
        )
        running = source[running_start:running_end]
        self.assertIn(
            """        IntPtr process = OpenProcess(
            SynchronizeAccess | ProcessQueryLimitedInformation,
            false,
            unchecked((uint)processId));
""",
            running,
        )
        terminating_descendant = """            if (wait == WaitTimeout)
            {
                uint exitCode;
                if (!GetExitCodeProcess(process, out exitCode))
                {
                    AddEngineError(
                        result,
                        LastError("GetExitCodeProcess(job-descendant)"));
                    return false;
                }
                if (exitCode != StillActive)
                {
                    return true;
                }
                isRunning = true;
                return true;
            }
"""
        self.assertIn(terminating_descendant, running)
        self.assertLess(
            running.index("GetExitCodeProcess(process, out exitCode)"),
            running.index("isRunning = true;"),
        )

        run_root = self.new_run_root()
        completed = self.invoke(
            run_root,
            extra_environment={"WINTER_GATE_FAKE_MODE": "leak-tree"},
        )
        self.assertNotEqual(0, completed.returncode)
        records = read_json_lines(self.record)
        self.assertEqual(1, len(records))
        root_pid = int(records[0]["pid"])
        child_pid = int(records[0]["child_pid"])
        assert_processes_exit(self, root_pid, child_pid)

        summary = self.load_summary(run_root)
        self.assertEqual("process_tree", summary["failure_kind"])
        self.assertEqual(1, len(summary["steps"]))
        result = summary["steps"][0]
        self.assertIs(True, result["process_started"])
        self.assertEqual(root_pid, result["process_id"])
        self.assertIs(False, result["timed_out"])
        self.assertIs(True, result["tree_drained"])
        self.assertIs(True, result["had_live_descendants_after_root_exit"])
        self.assertEqual("failed", result["status"])
        self.assertEqual("process_tree", result["failure_kind"])
```

Replace `test_public_process_uses_exact_argv_job_nul_and_handle_list` completely
with this exact body:

```python
class WinterInterludeGateProcessTests(_GateBlackBoxCase):
    def test_public_process_uses_exact_argv_job_nul_and_handle_list(self) -> None:
        sentinel = self.base / "inheritable-sentinel.txt"
        sentinel.write_text("must not reach the gate child", encoding="utf-8")
        sentinel_handle = create_inheritable_sentinel(sentinel)
        self.addCleanup(close_windows_handle, sentinel_handle)
        run_root = self.new_run_root()

        proof_record = self.base / "sentinel-inheritance-proof.jsonl"
        proof_environment = os.environ.copy()
        proof_environment.pop("WINTER_GATE_CONTROL", None)
        proof_environment.update(
            {
                "WINTER_GATE_RECORD": str(proof_record),
                "WINTER_GATE_FAKE_MODE": "normal",
                "WINTER_GATE_SENTINEL_HANDLE": str(sentinel_handle),
                "WINTER_GATE_SENTINEL_PATH": str(sentinel.resolve()),
            }
        )
        proof = subprocess.run(
            [
                str(self.fake_python),
                "-m",
                "unittest",
                "Tools.test_governance_winter_interlude",
                "-v",
            ],
            cwd=self.project,
            env=proof_environment,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=10,
            check=False,
            close_fds=False,
        )
        self.assertEqual(0, proof.returncode, proof.stderr)
        proof_records = read_json_lines(proof_record)
        self.assertEqual(1, len(proof_records))
        self.assertIs(True, proof_records[0]["sentinel_inherited"])

        completed = self.invoke(
            run_root,
            extra_environment={
                "WINTER_GATE_SENTINEL_HANDLE": str(sentinel_handle),
                "WINTER_GATE_SENTINEL_PATH": str(sentinel.resolve()),
                "WINTER_GATE_STRUCTURED_OUTPUT_HANDLE": str(sentinel_handle),
            },
            close_fds=False,
        )

        records = read_json_lines(self.record)
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertEqual(6, len(records))
        python_record = records[0]
        self.assertEqual("Python", python_record["kind"])
        self.assertEqual(
            [
                "-m",
                "unittest",
                "Tools.test_governance_winter_interlude",
                "-v",
            ],
            python_record["argv"],
        )
        self.assertEqual(
            os.path.normcase(str(self.fake_python.resolve())),
            os.path.normcase(str(Path(str(python_record["argv0"])).resolve())),
        )
        self.assertEqual(
            os.path.normcase(str(self.project.resolve())),
            os.path.normcase(str(Path(str(python_record["cwd"])).resolve())),
        )
        self.assertIs(True, python_record["in_job"])
        self.assertRegex(
            python_record["expected_job_name"],
            r"^Local\\WinterGate-[0-9a-f]{32}$",
        )
        self.assertIs(True, python_record["in_expected_job"])
        self.assertEqual(0x0002, python_record["stdin_file_type"])
        self.assertIs(False, python_record["sentinel_inherited"])
        self.assertIsNone(python_record["structured_output_handle"])

        source = GATE.read_text(encoding="utf-8")
        engine = source[
            source.index("// BEGIN PROCESS ENGINE") :
            source.index("// END PROCESS ENGINE")
        ]
        self.assertLess(
            engine.index("if (!AssignProcessToJobObject("),
            engine.index("uint previousSuspendCount = ResumeThread("),
        )

        summary = self.load_summary(run_root)
        self.assertEqual("passed", summary["status"])
        self.assertIsNone(summary["failure_kind"])
        self.assertIsNone(summary["error"])
        self.assertEqual(6, len(summary["steps"]))
        first = summary["steps"][0]
        self.assertEqual("source-contract", first["name"])
        for json_path in (
            run_root / "evidence" / "gate-summary.json",
            evidence_file(run_root, first["result"]),
        ):
            self.assertFalse(
                json_path.read_bytes().startswith(b"\xef\xbb\xbf"),
                json_path,
            )
        self.assertIs(True, first["process_started"])
        self.assertIsInstance(first["process_id"], int)
        self.assertIsInstance(first["started_utc"], str)
        self.assertIsInstance(first["ended_utc"], str)
        self.assertIsInstance(first["elapsed_milliseconds"], int)
        self.assertEqual(0, first["exit_code"])
        self.assertIs(False, first["timed_out"])
        self.assertIs(True, first["tree_drained"])
        self.assertIs(False, first["had_live_descendants_after_root_exit"])
        self.assertEqual("passed", first["status"])
        self.assertIsNone(first["failure_kind"])
        self.assertIsNone(first["error"])
        self.assertIn(
            "fake-python-stdout",
            evidence_file(run_root, first["stdout"]).read_text(
                encoding="utf-8-sig"
            ),
        )
        self.assertIn(
            "fake-python-stderr",
            evidence_file(run_root, first["stderr"]).read_text(
                encoding="utf-8-sig"
            ),
        )
```

Add the capability-only public tests:

```python
class WinterInterludeGateCapabilityTests(_GateBlackBoxCase):
    def test_control_oplock_breaks_for_readable_identity_flags(self) -> None:
        with tempfile.TemporaryDirectory(
            prefix="winter-readable-oplock-control-"
        ) as outside_text:
            checker = Path(outside_text) / "checker.py"
            checker.write_text("# readable identity control\n", encoding="utf-8")
            barrier = _LevelOneOplock(checker)
            errors: list[BaseException] = []
            opener = threading.Thread(
                target=_open_with_readable_identity_flags,
                args=(checker, errors),
                daemon=False,
            )
            opener.start()
            try:
                barrier.wait_for_break(5_000)
                self.assertTrue(
                    opener.is_alive(),
                    "readable-identity CreateFileW was not held by the oplock",
                )
            finally:
                barrier.close()
                opener.join(5)
            self.assertFalse(opener.is_alive())
            self.assertEqual(errors, [])

    def test_valid_batch_capability_uses_full_stem_and_passes(self) -> None:
        source = GATE.read_text(encoding="utf-8")
        self.assertIn(
            "@($manifestNames | Select-Object -Unique).Count",
            source,
        )
        selector = source[
            source.index("function Get-GateStructuredOutputDirectoryIdentity {") :
            source.index("function Get-NarrativeGateManifest {")
        ]
        self.assertIn("[IO.Path]::GetDirectoryName($fullPath)", selector)
        self.assertIn("$script:GateDirectoryIdentities", selector)
        self.assertIn("[StringComparison]::OrdinalIgnoreCase", selector)
        self.assertIn("if ($matches.Count -ne 1)", selector)
        self.assertNotIn("StartsWith(", selector)
        fixture = self.make_project()
        try:
            completed = fixture.run(
                "Narrative",
                "Batch",
                documents={
                    "narrative-capability": capability_document(
                        "batch", final_contracts=False
                    )
                },
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            summary = fixture.summary()
            self.assertEqual(summary["status"], "passed")
            self.assertEqual(len(summary["steps"]), 1)
            step = summary["steps"][0]
            self.assertEqual(step["name"], "narrative-capability")
            expected = (
                fixture.run_root
                / "evidence"
                / "narrative-01-narrative-capability-no-head.output.json"
            )
            self.assertEqual(fixture.output_path("narrative-capability"), expected)
            self.assertEqual(step["arguments"][-1], str(expected))
            self.assertTrue(expected.is_file())
        finally:
            fixture.close()

    def test_real_project_is_capability_first_when_checker_is_absent(self) -> None:
        self.assertFalse(
            (ROOT / "Tools" / "check_winter_narrative_capabilities.py").exists()
        )
        for phase in ("Batch", "Final"):
            with self.subTest(phase=phase):
                with tempfile.TemporaryDirectory(
                    prefix="winter-real-capability-"
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
                    self.assertNotEqual(completed.returncode, 0)
                    summary = json.loads(
                        (
                            run_root / "evidence" / "gate-summary.json"
                        ).read_text(encoding="utf-8-sig")
                    )
                    self.assertEqual(len(summary["steps"]), 1)
                    failed = summary["steps"][0]
                    self.assertEqual(failed["name"], "narrative-capability")
                    self.assertEqual(failed["failure_kind"], "validation")
                    self.assertFalse(failed["process_started"])
                    self.assertIsNone(failed["process_id"])
                    self.assertIsNone(failed["stdout"])
                    self.assertIsNone(failed["stderr"])

    def test_capability_rejects_malformed_schema_tool_and_property_count(self) -> None:
        valid = capability_document("batch", final_contracts=False)
        extra = capability_document("batch", final_contracts=False)
        extra["capabilities"]["unexpected"] = True
        cases: tuple[
            tuple[str, dict[str, object] | None, str | None], ...
        ] = (
            ("malformed", None, "{"),
            ("schema", {**valid, "schema_version": 2}, None),
            ("tool", {**valid, "tool": "not_the_capability_tool"}, None),
            ("property-count", extra, None),
        )
        for name, document, raw in cases:
            with self.subTest(name=name):
                fixture = self.make_project()
                try:
                    completed = fixture.run(
                        "Narrative",
                        "Batch",
                        documents=(
                            {}
                            if document is None
                            else {"narrative-capability": document}
                        ),
                        raw_documents=(
                            {}
                            if raw is None
                            else {"narrative-capability": raw}
                        ),
                    )
                    self.assertNotEqual(completed.returncode, 0)
                    self.assertEqual(len(fixture.records()), 1)
                    self.assertEqual(
                        fixture.result(1)["failure_kind"], "invalid_evidence"
                    )
                finally:
                    fixture.close()

    def test_strict_json_rejects_non_rfc8259_lexemes(self) -> None:
        valid = json.dumps(
            capability_document("batch", final_contracts=False),
            separators=(",", ":"),
            ensure_ascii=False,
        )
        schema = '"schema_version":1'
        leading_zero = valid.replace(schema, '"schema_version":01', 1)
        leading_plus = valid.replace(schema, '"schema_version":+1', 1)
        nan = valid.replace(schema, '"schema_version":NaN', 1)
        non_json_whitespace = valid.replace(
            schema, '"schema_version":\u00a01', 1
        )
        trailing_decimal = valid.replace(schema, '"schema_version":1.', 1)
        leading_decimal = valid.replace(schema, '"schema_version":.1', 1)
        infinity = valid.replace(schema, '"schema_version":Infinity', 1)
        single_quoted = valid.replace('"', "'")
        unquoted_keys = re.sub(r'"([A-Za-z_]+)":', r"\1:", valid)
        vertical_tab = valid.replace(schema, '"schema_version":\x0b1', 1)
        cases = (
            (
                "leading-zero",
                leading_zero,
                "leading_zero",
                leading_zero.index("01") + 1,
            ),
            (
                "leading-plus",
                leading_plus,
                "expected_value",
                leading_plus.index("+1"),
            ),
            ("nan", nan, "expected_value", nan.index("NaN")),
            (
                "non-json-whitespace",
                non_json_whitespace,
                "expected_value",
                non_json_whitespace.index("\u00a0"),
            ),
            (
                "trailing-decimal",
                trailing_decimal,
                "fraction_digit_required",
                trailing_decimal.index("1.") + 2,
            ),
            (
                "leading-decimal",
                leading_decimal,
                "expected_value",
                leading_decimal.index(".1"),
            ),
            (
                "infinity",
                infinity,
                "expected_value",
                infinity.index("Infinity"),
            ),
            ("single-quoted-object", single_quoted, "object_property_name", 1),
            ("unquoted-keys", unquoted_keys, "object_property_name", 1),
            (
                "vertical-tab",
                vertical_tab,
                "expected_value",
                vertical_tab.index("\x0b"),
            ),
        )
        for name, raw, reason, failure_offset in cases:
            with self.subTest(name=name):
                fixture = self.make_project()
                try:
                    completed = fixture.run(
                        "Narrative",
                        "Batch",
                        raw_documents={"narrative-capability": raw},
                        exit_codes={1: 47},
                    )
                    self.assertNotEqual(completed.returncode, 0)
                    self.assertEqual(
                        [record["step"] for record in fixture.records()],
                        ["narrative-capability"],
                    )
                    result = fixture.result(1)
                    self.assertEqual(result["failure_kind"], "invalid_evidence")
                    self.assertEqual(result["exit_code"], 47)
                    self.assertIn(
                        f"strict_json:{reason} at UTF-16 offset "
                        f"{failure_offset}.",
                        str(result["error"]),
                    )
                finally:
                    fixture.close()

        source = GATE.read_text(encoding="utf-8")
        self.assertEqual(source.count("public static void ValidateStrictJson("), 1)
        self.assertIn("private const int MaximumJsonDepth = 64;", source)
        assert_strict_json_validation_order(self, source)
        strict_call = "    [WinterGate.Native]::ValidateStrictJson($raw)"
        strict_bypass_mutant = source.replace(
            strict_call,
            "    $null = $raw.Length # strict validation bypass mutant",
            1,
        )
        with self.assertRaises(AssertionError):
            assert_strict_json_validation_order(self, strict_bypass_mutant)

    def test_strict_json_rejects_decoded_duplicate_object_keys(self) -> None:
        valid = json.dumps(
            capability_document("batch", final_contracts=False),
            separators=(",", ":"),
            ensure_ascii=False,
        )
        cases = (
            (
                "literal",
                valid.replace(
                    '"schema_version":1',
                    '"schema_version":1,"schema_version":1',
                    1,
                ),
            ),
            (
                "escaped-equivalent",
                valid.replace(
                    '"canon_json":true',
                    '"canon_json":true,"canon\\u005fjson":true',
                    1,
                ),
            ),
        )
        for name, raw in cases:
            with self.subTest(name=name):
                fixture = self.make_project()
                try:
                    completed = fixture.run(
                        "Narrative",
                        "Batch",
                        raw_documents={"narrative-capability": raw},
                    )
                    self.assertNotEqual(completed.returncode, 0)
                    self.assertEqual(
                        [record["step"] for record in fixture.records()],
                        ["narrative-capability"],
                    )
                    self.assertEqual(
                        fixture.result(1)["failure_kind"], "invalid_evidence"
                    )
                finally:
                    fixture.close()

    def test_strict_json_resource_boundaries_are_exact(self) -> None:
        character_limit = 1_048_576
        number_limit = 128
        with tempfile.TemporaryDirectory(
            prefix="winter-strict-json-resource-"
        ) as temporary:
            base = Path(temporary)
            probe = base / "strict-json-probe.exe"
            compile_strict_json_probe(probe)
            exact_document = base / "exact-document.json"
            exact_document.write_text(
                '"' + "a" * (character_limit - 2) + '"',
                encoding="utf-8",
            )
            exact = subprocess.run(
                [str(probe), str(exact_document)],
                cwd=base,
                stdin=subprocess.DEVNULL,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=30,
                check=False,
            )
            self.assertEqual(0, exact.returncode, exact.stderr)

            over_document = base / "over-document.json"
            over_document.write_text(
                '"' + "a" * (character_limit - 1) + '"',
                encoding="utf-8",
            )
            over = subprocess.run(
                [str(probe), str(over_document)],
                cwd=base,
                stdin=subprocess.DEVNULL,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=30,
                check=False,
            )
            self.assertEqual(91, over.returncode, over.stderr)
            self.assertEqual(
                "strict_json:document_too_long at UTF-16 offset 1048576.\n",
                over.stderr.replace("\r\n", "\n"),
            )

        def public_result(raw: str, exit_code: int = 47) -> dict[str, object]:
            fixture = self.make_project()
            try:
                completed = fixture.run(
                    "Narrative",
                    "Batch",
                    raw_documents={"narrative-capability": raw},
                    exit_codes={1: exit_code} if exit_code else {},
                )
                self.assertNotEqual(completed.returncode, 0)
                self.assertEqual(
                    [record["step"] for record in fixture.records()],
                    ["narrative-capability"],
                )
                result = fixture.result(1)
                self.assertEqual(result["failure_kind"], "invalid_evidence")
                self.assertEqual(result["exit_code"], exit_code)
                return result
            finally:
                fixture.close()

        resource_failures = (
            (
                "depth-65",
                "[" * 65 + "0" + "]" * 65,
                "strict_json:maximum_depth at UTF-16 offset 64.",
            ),
            (
                "number-129",
                "1" * 129,
                "strict_json:number_too_long at UTF-16 offset 128.",
            ),
        )
        for name, raw, expected_error in resource_failures:
            with self.subTest(name=name):
                result = public_result(raw)
                self.assertIn(expected_error, str(result["error"]))

        exact_bytes = '"' + "a" * (character_limit - 2) + '"'
        exact_bytes_result = public_result(exact_bytes, exit_code=0)
        self.assertNotIn("size limit", str(exact_bytes_result["error"]).lower())
        self.assertNotIn("strict_json:", str(exact_bytes_result["error"]))

        oversized_bytes = '"' + "a" * (character_limit - 1) + '"'
        oversized_result = public_result(oversized_bytes)
        self.assertIn("size limit", str(oversized_result["error"]).lower())
        self.assertNotIn("strict_json:", str(oversized_result["error"]))

        legal_numbers = (
            "0",
            "-0",
            "1",
            "-1",
            "1.0",
            "1e2",
            "1E+2",
            "1e-2",
            "1" + "0" * (number_limit - 1),
        )
        positive = (
            " \t\r\n"
            + "[" * 64
            + ",".join(legal_numbers)
            + "]" * 64
            + " \t\r\n"
        )
        positive_result = public_result(positive, exit_code=0)
        self.assertNotIn("strict_json:", str(positive_result["error"]))

        source = GATE.read_text(encoding="utf-8")
        self.assertIn(
            "private const int MaximumJsonDocumentCharacters = 1048576;",
            source,
        )
        self.assertIn(
            "private const int MaximumJsonNumberTokenLength = 128;",
            source,
        )
        self.assertIn(
            "SortedSet<string> propertyNames = new SortedSet<string>(",
            source,
        )
        self.assertNotIn("HashSet<string> propertyNames", source)

    def test_strict_json_strings_diagnostics_and_layering_are_exact(self) -> None:
        invalid_cases = (
            ("trailing-comma", '{"a":1,}', "object_property_name", 7),
            ("tail", "{}x", "trailing_content", 2),
            ("bom", "\ufeff{}", "expected_value", 0),
            ("raw-c0", '{"a":"\x01"}', "unescaped_control", 6),
            ("bad-escape", '{"a":"\\q"}', "unknown_escape", 7),
            ("bad-hex", '{"a":"\\u00G0"}', "invalid_unicode_hex", 10),
            (
                "orphan-high",
                '{"a":"\\uD800"}',
                "escaped_high_surrogate_requires_low",
                6,
            ),
            (
                "orphan-low",
                '{"a":"\\uDC00"}',
                "unpaired_escaped_low_surrogate",
                6,
            ),
            (
                "reversed-surrogates",
                '{"a":"\\uDC00\\uD800"}',
                "unpaired_escaped_low_surrogate",
                6,
            ),
            (
                "nested-decoded-duplicate",
                r'{"outer":{"same":1,"s\u0061me":2}}',
                "duplicate_property",
                19,
            ),
        )
        for name, raw, reason, failure_offset in invalid_cases:
            with self.subTest(name=name):
                fixture = self.make_project()
                try:
                    completed = fixture.run(
                        "Narrative",
                        "Batch",
                        raw_documents={"narrative-capability": raw},
                        exit_codes={1: 47},
                    )
                    self.assertNotEqual(completed.returncode, 0)
                    self.assertEqual(
                        [record["step"] for record in fixture.records()],
                        ["narrative-capability"],
                    )
                    result = fixture.result(1)
                    self.assertEqual(result["failure_kind"], "invalid_evidence")
                    self.assertEqual(result["exit_code"], 47)
                    self.assertIn(
                        f"strict_json:{reason} at UTF-16 offset "
                        f"{failure_offset}.",
                        str(result["error"]),
                    )
                finally:
                    fixture.close()

        escaped_text = json.dumps(
            "short\\/\b\f\n\r\t_", ensure_ascii=True
        ).replace("/", "\\/").replace("_", "\\u005f")
        positive = (
            "["
            + ",".join(
                (
                    escaped_text,
                    r'"\uD83D\uDE00"',
                    json.dumps("\U0001f600", ensure_ascii=False),
                    '{"same":1}',
                    '{"same":2}',
                )
            )
            + "]"
        )
        fixture = self.make_project()
        try:
            completed = fixture.run(
                "Narrative",
                "Batch",
                raw_documents={"narrative-capability": positive},
            )
            self.assertNotEqual(completed.returncode, 0)
            self.assertEqual(
                [record["step"] for record in fixture.records()],
                ["narrative-capability"],
            )
            result = fixture.result(1)
            self.assertEqual(result["failure_kind"], "invalid_evidence")
            self.assertNotIn("strict_json:", str(result["error"]))
        finally:
            fixture.close()

        source = GATE.read_text(encoding="utf-8")
        parser_start = source.index("private sealed class StrictJsonParser")
        parser_end = source.index(
            "private static SecurityAttributes NewSecurityAttributes("
        )
        parser = source[parser_start:parser_end]
        self.assertIn('"strict_json:" + reason', parser)
        self.assertIn("int failureOffset", parser)

    def test_gate_owned_reservation_blocks_concurrent_path_writers(self) -> None:
        fixture = self.make_project()
        ready = fixture.base / "structured-writer-ready"
        release = fixture.base / "structured-writer-release"
        documents = passing_narrative_documents("batch")
        capability = documents.pop("narrative-capability")
        process = fixture.start_writer_race(
            ready,
            release,
            gate="Narrative",
            phase="Batch",
            documents=documents,
        )
        self.addCleanup(lambda: process.poll() is None and process.kill())
        try:
            deadline = time.monotonic() + 15
            while not ready.exists() and time.monotonic() < deadline:
                time.sleep(0.01)
            child_was_running = ready.is_file() and process.poll() is None
            output = fixture.output_path("narrative-capability")
            payload = json.dumps(
                capability,
                separators=(",", ":"),
                ensure_ascii=False,
            )
            replacement = fixture.base / "third-party-replacement.json"
            replacement.write_text(payload, encoding="utf-8")
            attempts: dict[str, tuple[bool, int | None]] = {}

            def attempt(label: str, action: Callable[[], None]) -> None:
                try:
                    action()
                    attempts[label] = (True, None)
                except OSError as error:
                    attempts[label] = (False, error.winerror)

            def create_new() -> None:
                with output.open("x", encoding="utf-8", newline="\n") as stream:
                    stream.write(payload)

            def open_for_write() -> None:
                with output.open("w", encoding="utf-8", newline="\n") as stream:
                    stream.write(payload)

            try:
                attempt("create-new", create_new)
                attempt(
                    "path-write-text",
                    lambda: output.write_text(payload, encoding="utf-8"),
                )
                attempt("open-write", open_for_write)
                attempt("replace", lambda: os.replace(replacement, output))
            finally:
                release.write_text("release", encoding="utf-8")

            stdout, stderr = process.communicate(timeout=65)
            summary_path = fixture.run_root / "evidence" / "gate-summary.json"
            self.assertTrue(
                summary_path.is_file(),
                "gate did not publish its summary: "
                f"returncode={process.returncode} attempts={attempts!r} "
                f"stdout={stdout!r} stderr={stderr!r}",
            )
            summary = fixture.summary()
            self.assertTrue(child_was_running, "controlled child was not running")
            self.assertNotEqual(
                process.returncode,
                0,
                "gate accepted third-party path-written evidence: "
                f"attempts={attempts!r} status={summary['status']} "
                f"stdout={stdout!r} stderr={stderr!r}",
            )
            self.assertEqual(
                {name: succeeded for name, (succeeded, _) in attempts.items()},
                {
                    "create-new": False,
                    "path-write-text": False,
                    "open-write": False,
                    "replace": False,
                },
            )
            self.assertEqual(
                [record["step"] for record in fixture.records()],
                ["narrative-capability"],
            )
            self.assertRegex(
                str(fixture.records()[0]["structured_output_handle"]),
                r"^[1-9][0-9]*$",
            )
            self.assertEqual(
                fixture.result(1)["failure_kind"], "invalid_evidence"
            )
            self.assertTrue(
                output.read_bytes().startswith(b"WINTER_GATE_RESERVED_V1:")
            )

            output.write_text("after-dispose", encoding="utf-8")
            self.assertEqual(output.read_text(encoding="utf-8"), "after-dispose")
            replacement.write_text("after-dispose-replace", encoding="utf-8")
            os.replace(replacement, output)
            self.assertEqual(
                output.read_text(encoding="utf-8"), "after-dispose-replace"
            )

            source = GATE.read_text(encoding="utf-8")
            assert_structured_reservation_close_order(self, source)
            summary_publish = (
                "        Write-GateSummaryJson -Path "
                "$script:SummaryPath -Value $summary"
            )
            self.assertEqual(1, source.count(summary_publish))
            early_close_mutant = source.replace(
                summary_publish,
                "        Close-GateStructuredOutputReservations\n"
                + summary_publish,
                1,
            )
            with self.assertRaises(AssertionError):
                assert_structured_reservation_close_order(
                    self,
                    early_close_mutant,
                )
            self.assertEqual(
                source.count(
                    "public sealed class StructuredOutputReservation : IDisposable"
                ),
                1,
            )
            self.assertEqual(
                source.count(
                    "public static StructuredOutputReservation "
                    "ReserveStructuredOutput("
                ),
                1,
            )
            reader_start = source.index("function Read-GateStructuredJson {")
            reader_end = source.index("function Get-GateJsonOutcome {")
            reader = source[reader_start:reader_end]
            self.assertIn("FreezeStructuredOutput(", reader)
            dispatcher_start = source.index("function Invoke-GateStep {")
            dispatcher_end = source.index("function Invoke-WinterInterludeGate {")
            dispatcher = source[dispatcher_start:dispatcher_end]
            self.assertIn(
                "[WinterGate.Native]::ReserveStructuredOutput(", dispatcher
            )
            self.assertNotIn("$jsonReservation.Dispose()", dispatcher)
            self.assertIn("$script:StructuredOutputReservations.Add(", dispatcher)
            self.assertIn("Close-GateStructuredOutputReservations", source)
            engine = source[
                source.index("// BEGIN PROCESS ENGINE") :
                source.index("// END PROCESS ENGINE")
            ]
            self.assertIn("StructuredOutputHandleEnvironmentVariable", engine)
            self.assertIn(
                "IntPtr.Size * 3, structuredOutputChildHandle", engine
            )
            writer_start = RECORDING_CHILD_SOURCE.index(
                "private static void WriteControlledDocument("
            )
            writer_end = RECORDING_CHILD_SOURCE.index(
                "private static string ApplyAfterStepControls("
            )
            writer = RECORDING_CHILD_SOURCE[writer_start:writer_end]
            self.assertIn("new SafeFileHandle(", writer)
            self.assertIn("stream.SetLength(0);", writer)
            self.assertIn("stream.Flush(true);", writer)
            self.assertIn("GetFinalPathNameByHandleW(", writer)
            self.assertNotIn("File.WriteAllText(output", writer)
        finally:
            fixture.close()

    def test_capability_false_flag_beats_nonzero_exit(self) -> None:
        document = capability_document("batch", final_contracts=False)
        document["capabilities"]["canon_json"] = False
        fixture = self.make_project()
        try:
            completed = fixture.run(
                "Narrative",
                "Batch",
                documents={"narrative-capability": document},
                exit_codes={1: 19},
            )
            self.assertNotEqual(completed.returncode, 0)
            result = fixture.result(1)
            self.assertEqual(result["failure_kind"], "postcondition")
            self.assertEqual(result["exit_code"], 19)
        finally:
            fixture.close()

    def test_final_rejects_batch_only_capability(self) -> None:
        fixture = self.make_project()
        try:
            document = capability_document("final", final_contracts=False)
            completed = fixture.run(
                "Narrative",
                "Final",
                documents={"narrative-capability": document},
            )
            self.assertNotEqual(completed.returncode, 0)
            self.assertEqual(
                [record["step"] for record in fixture.records()],
                ["narrative-capability"],
            )
            self.assertEqual(
                fixture.result(1)["failure_kind"], "postcondition"
            )
        finally:
            fixture.close()

    def test_capability_missing_output_precedence_is_exact(self) -> None:
        for exit_code, expected in ((0, "invalid_evidence"), (23, "process")):
            with self.subTest(exit_code=exit_code):
                fixture = self.make_project()
                try:
                    completed = fixture.run(
                        "Narrative",
                        "Batch",
                        documents={},
                        exit_codes={} if exit_code == 0 else {1: exit_code},
                    )
                    self.assertNotEqual(completed.returncode, 0)
                    self.assertEqual(
                        fixture.result(1)["failure_kind"], expected
                    )
                finally:
                    fixture.close()

    def test_python_executable_identity_is_rechecked_before_first_child(self) -> None:
        fixture = self.make_project()
        try:
            completed = run_narrative_with_prelaunch_python_swap(fixture)
            self.assertNotEqual(completed.returncode, 0)
            self.assertEqual(fixture.records(), [])
            summary = fixture.summary()
            self.assertEqual(len(summary["steps"]), 1)
            failed = summary["steps"][0]
            self.assertEqual(failed["name"], "narrative-capability")
            self.assertEqual(failed["failure_kind"], "validation")
            self.assertFalse(failed["process_started"])
            self.assertFalse(failed["timed_out"])
            self.assertTrue(failed["tree_drained"])
            self.assertFalse(failed["had_live_descendants_after_root_exit"])
            for field in (
                "process_id",
                "started_utc",
                "ended_utc",
                "exit_code",
                "elapsed_milliseconds",
                "stdout",
                "stderr",
            ):
                self.assertIsNone(failed[field], field)
            self.assertEqual(
                json.loads(
                    (
                        fixture.run_root / failed["result"]
                    ).read_text(encoding="utf-8-sig")
                ),
                failed,
            )
        finally:
            fixture.close()
```

- [ ] **Step 2: Run only the capability loop RED**

First prove that the control primitive blocks the exact access/share/flag tuple
used by Task 3's readable-file identity seam:

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateCapabilityTests.test_control_oplock_breaks_for_readable_identity_flags `
  -v
if ($LASTEXITCODE -ne 0) { throw 'Readable-identity oplock control failed.' }
```

Expected: one test passes. In particular, the opener thread is still blocked
when the oplock break event is signaled and exits only after the test releases
the oplock. A metadata-only `desiredAccess=0` opener is not an acceptable
substitute for this control.

Then run the capability behavior RED:

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateCapabilityTests -v 2>&1 |
  Tee-Object -FilePath .superpowers/sdd/task-7-5-capability-red.txt
if ($LASTEXITCODE -eq 0) { throw 'Capability JSON RED unexpectedly passed.' }
```

Expected: the real missing-checker case and readable-oplock control may already
pass. The command is still nonzero because the 13-method capability catalog
requires the missing strict recognizer, owner-handle reservation, environment
scrub/4-handle bridge, exact reason/offset behavior, and reservation lifetime.
The leading-zero case is the required permissive-`ConvertFrom-Json` bypass
killer; the strict-call and early-close source mutants must also fail their
order helpers. No assertion depends on a later manifest result or scanner
schema.

- [ ] **Step 3: Implement the one-step capability JSON vertical slice**

First extend Task 3's native class. Add
`ProcessQueryLimitedInformation = 0x00001000` beside the process-access
constants and `DuplicateSameAccess = 0x00000002` beside the handle constants.
Add the following exact constants and owner types before the existing native
struct declarations:

```csharp
private const uint StillActive = 259;
private const int MaximumJsonDepth = 64;
private const int MaximumJsonDocumentCharacters = 1048576;
private const int MaximumJsonNumberTokenLength = 128;
private const string StructuredOutputHandleEnvironmentVariable =
    "WINTER_GATE_STRUCTURED_OUTPUT_HANDLE";
private const string StructuredOutputMarkerPrefix =
    "WINTER_GATE_RESERVED_V1:";

public sealed class StructuredOutputSnapshot
{
    public bool HasContent;
    public string Text;
}

public sealed class StructuredOutputReservation : IDisposable
{
    private readonly object synchronization = new object();
    private IntPtr ownerHandle;
    private IntPtr evidenceDirectoryGuard;
    private bool writerIssued;
    private bool frozen;
    private bool disposed;
    private StructuredOutputSnapshot snapshot;
    internal readonly string FixedPath;
    internal readonly PathIdentity CreationIdentity;
    internal readonly PathIdentity EvidenceDirectoryIdentity;
    internal readonly byte[] MarkerBytes;

    internal StructuredOutputReservation(
        string fixedPath,
        IntPtr ownerHandle,
        IntPtr evidenceDirectoryGuard,
        PathIdentity creationIdentity,
        PathIdentity evidenceDirectoryIdentity,
        byte[] markerBytes)
    {
        FixedPath = fixedPath;
        this.ownerHandle = ownerHandle;
        this.evidenceDirectoryGuard = evidenceDirectoryGuard;
        CreationIdentity = creationIdentity;
        EvidenceDirectoryIdentity = evidenceDirectoryIdentity;
        MarkerBytes = markerBytes;
    }

    internal IntPtr DuplicateInheritableWriterHandle()
    {
        lock (synchronization)
        {
            RequireOpen();
            if (writerIssued || frozen)
            {
                throw new InvalidOperationException(
                    "The structured output writer was already issued or frozen.");
            }
            IntPtr currentProcess = GetCurrentProcess();
            IntPtr duplicate;
            if (!DuplicateHandle(
                currentProcess,
                ownerHandle,
                currentProcess,
                out duplicate,
                0,
                true,
                DuplicateSameAccess))
            {
                throw new IOException(
                    LastError("DuplicateHandle(structured output writer)"));
            }
            writerIssued = true;
            return duplicate;
        }
    }

    internal StructuredOutputSnapshot Freeze(int maximumBytes)
    {
        lock (synchronization)
        {
            RequireOpen();
            if (snapshot != null)
            {
                return snapshot;
            }
            if (!writerIssued)
            {
                throw new InvalidOperationException(
                    "The structured output writer was not issued.");
            }
            snapshot = FreezeStructuredOutputCore(this, maximumBytes);
            frozen = true;
            return snapshot;
        }
    }

    public void Dispose()
    {
        ReleaseHandles();
        GC.SuppressFinalize(this);
    }

    ~StructuredOutputReservation()
    {
        ReleaseHandles();
    }

    private void RequireOpen()
    {
        if (disposed || ownerHandle == IntPtr.Zero ||
            evidenceDirectoryGuard == IntPtr.Zero)
        {
            throw new ObjectDisposedException(
                "StructuredOutputReservation");
        }
    }

    private void ReleaseHandles()
    {
        lock (synchronization)
        {
            if (disposed)
            {
                return;
            }
            disposed = true;
            CloseOwnedHandle(ref ownerHandle);
            CloseOwnedHandle(ref evidenceDirectoryGuard);
        }
    }

    internal IntPtr OwnerHandle
    {
        get { RequireOpen(); return ownerHandle; }
    }

    internal IntPtr EvidenceDirectoryGuard
    {
        get { RequireOpen(); return evidenceDirectoryGuard; }
    }
}
```

Add these exact P/Invokes beside the existing `GetExitCodeProcess`/handle
declarations:

```csharp
[DllImport("kernel32.dll")]
private static extern IntPtr GetCurrentProcess();

[DllImport("kernel32.dll", SetLastError = true)]
[return: MarshalAs(UnmanagedType.Bool)]
private static extern bool DuplicateHandle(
    IntPtr sourceProcess,
    IntPtr sourceHandle,
    IntPtr targetProcess,
    out IntPtr targetHandle,
    uint desiredAccess,
    [MarshalAs(UnmanagedType.Bool)] bool inheritHandle,
    uint options);
```

Add these exact public entry points beside the existing JSON writer public API:

```csharp
public static void ValidateStrictJson(string json)
{
    if (json == null)
    {
        throw new ArgumentNullException("json");
    }
    new StrictJsonParser(
        json,
        MaximumJsonDepth,
        MaximumJsonDocumentCharacters,
        MaximumJsonNumberTokenLength).Validate();
}

public static StructuredOutputReservation ReserveStructuredOutput(
    string path,
    PathIdentity expectedEvidenceDirectoryIdentity)
{
    ValidateJsonPath(path, expectedEvidenceDirectoryIdentity);
    SecurityAttributes nonInheritable = NewSecurityAttributes(false);
    IntPtr evidenceDirectoryGuard = InvalidHandleValue;
    IntPtr ownerHandle = InvalidHandleValue;
    try
    {
        PathIdentity guardedEvidenceIdentity = OpenVerifiedEvidenceGuard(
            expectedEvidenceDirectoryIdentity,
            path,
            ref evidenceDirectoryGuard);
        ownerHandle = CreateFileW(
            path,
            GenericRead | GenericWrite,
            0,
            ref nonInheritable,
            CreateNew,
            FileAttributeNormal | FileFlagOpenReparsePoint,
            IntPtr.Zero);
        if (ownerHandle == InvalidHandleValue)
        {
            throw JsonPathIdentityError(
                "CreateFileW(structured output reservation)",
                path,
                Marshal.GetLastWin32Error());
        }
        RequireDirectEvidenceChild(
            ownerHandle,
            path,
            guardedEvidenceIdentity,
            "structured output reservation");
        PathIdentity creationIdentity = GetPathIdentityFromOpenHandle(
            ownerHandle,
            PathKind.File);
        if ((creationIdentity.Attributes & FileAttributes.ReparsePoint) != 0)
        {
            throw new WinterGatePathIdentityException(
                "path identity: structured output reservation is a " +
                "reparse point: " + path);
        }
        byte[] markerBytes = Encoding.ASCII.GetBytes(
            StructuredOutputMarkerPrefix + Guid.NewGuid().ToString("N"));
        WriteAllAndFlush(
            ownerHandle,
            markerBytes,
            "structured output reservation marker");
        StructuredOutputReservation reservation =
            new StructuredOutputReservation(
                path,
                ownerHandle,
                evidenceDirectoryGuard,
                creationIdentity,
                guardedEvidenceIdentity,
                markerBytes);
        ownerHandle = IntPtr.Zero;
        evidenceDirectoryGuard = IntPtr.Zero;
        return reservation;
    }
    finally
    {
        CloseOwnedHandle(ref ownerHandle);
        CloseOwnedHandle(ref evidenceDirectoryGuard);
    }
}

public static StructuredOutputSnapshot FreezeStructuredOutput(
    StructuredOutputReservation reservation,
    int maximumBytes)
{
    if (reservation == null)
    {
        throw new ArgumentNullException("reservation");
    }
    if (maximumBytes < 1)
    {
        throw new ArgumentOutOfRangeException("maximumBytes");
    }
    return reservation.Freeze(maximumBytes);
}
```

Replace `BuildChildEnvironmentBlock` and add the owner-handle freezer beside
the existing readable helpers. These are complete bodies; do not retain the
old one-argument environment builder:

```csharp
private static IntPtr BuildChildEnvironmentBlock(
    string jobName,
    IntPtr structuredOutputChildHandle)
{
    if (String.IsNullOrWhiteSpace(jobName))
    {
        throw new ArgumentException("Named Job identity is required.", "jobName");
    }
    SortedDictionary<string, string> environment =
        new SortedDictionary<string, string>(
            StringComparer.OrdinalIgnoreCase);
    foreach (DictionaryEntry entry in Environment.GetEnvironmentVariables())
    {
        string key = Convert.ToString(
            entry.Key,
            CultureInfo.InvariantCulture);
        string value = Convert.ToString(
            entry.Value,
            CultureInfo.InvariantCulture);
        if (!String.Equals(
            key,
            GateJobEnvironmentVariable,
            StringComparison.OrdinalIgnoreCase) &&
            !String.Equals(
            key,
            StructuredOutputHandleEnvironmentVariable,
            StringComparison.OrdinalIgnoreCase))
        {
            environment[key] = value;
        }
    }
    environment[GateJobEnvironmentVariable] = jobName;
    if (structuredOutputChildHandle != IntPtr.Zero &&
        structuredOutputChildHandle != InvalidHandleValue)
    {
        environment[StructuredOutputHandleEnvironmentVariable] =
            structuredOutputChildHandle.ToInt64().ToString(
                CultureInfo.InvariantCulture);
    }

    StringBuilder block = new StringBuilder();
    foreach (KeyValuePair<string, string> entry in environment)
    {
        block.Append(entry.Key);
        block.Append('=');
        block.Append(entry.Value);
        block.Append('\0');
    }
    block.Append('\0');
    byte[] bytes = Encoding.Unicode.GetBytes(block.ToString());
    IntPtr nativeBlock = Marshal.AllocHGlobal(bytes.Length);
    try
    {
        Marshal.Copy(bytes, 0, nativeBlock, bytes.Length);
        return nativeBlock;
    }
    catch
    {
        Marshal.FreeHGlobal(nativeBlock);
        throw;
    }
}

private static StructuredOutputSnapshot FreezeStructuredOutputCore(
    StructuredOutputReservation reservation,
    int maximumBytes)
{
    PathIdentity currentEvidenceIdentity = GetPathIdentityFromOpenHandle(
        reservation.EvidenceDirectoryGuard,
        PathKind.Directory);
    if ((currentEvidenceIdentity.Attributes &
            FileAttributes.ReparsePoint) != 0 ||
        !SameStablePath(
            reservation.EvidenceDirectoryIdentity,
            currentEvidenceIdentity))
    {
        throw new WinterGatePathIdentityException(
            "path identity: structured output evidence directory changed.");
    }

    PathIdentity currentOpenIdentity = GetPathIdentityFromOpenHandle(
        reservation.OwnerHandle,
        PathKind.File);
    if ((currentOpenIdentity.Attributes & FileAttributes.ReparsePoint) != 0 ||
        !SameStablePath(
            reservation.CreationIdentity,
            currentOpenIdentity))
    {
        throw new WinterGatePathIdentityException(
            "path identity: structured output owner handle changed.");
    }
    RequireDirectEvidenceChild(
        reservation.OwnerHandle,
        reservation.FixedPath,
        currentEvidenceIdentity,
        "frozen structured output");

    byte[] content;
    using (SafeFileHandle borrowed = new SafeFileHandle(
        reservation.OwnerHandle,
        false))
    using (FileStream stream = new FileStream(
        borrowed,
        FileAccess.ReadWrite))
    {
        if (stream.Length > maximumBytes)
        {
            throw new InvalidDataException(
                "Structured JSON exceeds its size limit: " +
                reservation.FixedPath);
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
                    "Structured JSON ended before its reported length.");
            }
            totalRead += read;
        }
    }

    PathIdentity afterReadIdentity = GetPathIdentityFromOpenHandle(
        reservation.OwnerHandle,
        PathKind.File);
    if (!SameStablePath(
        reservation.CreationIdentity,
        afterReadIdentity))
    {
        throw new WinterGatePathIdentityException(
            "path identity: structured output changed during freeze.");
    }

    StructuredOutputSnapshot result = new StructuredOutputSnapshot();
    if (ByteArraysEqual(content, reservation.MarkerBytes))
    {
        result.HasContent = false;
        result.Text = null;
        return result;
    }
    result.HasContent = true;
    result.Text = new UTF8Encoding(false, true).GetString(content);
    return result;
}

private static bool ByteArraysEqual(byte[] left, byte[] right)
{
    if (left == null || right == null || left.Length != right.Length)
    {
        return false;
    }
    for (int index = 0; index < left.Length; index++)
    {
        if (left[index] != right[index])
        {
            return false;
        }
    }
    return true;
}
```

Replace the `RunProcessTree` signature with the eight-argument form and make
these exact changes inside the existing complete Task 3 body. They are the
only permitted abbreviated edits because every surrounding baseline line stays
unchanged and the Process regression tests cover that baseline:

```csharp
public static BoundedProcessResult RunProcessTree(
    string executable,
    string[] arguments,
    string workingDirectory,
    string stdoutPath,
    string stderrPath,
    int timeoutMilliseconds,
    PathIdentity expectedEvidenceDirectoryIdentity,
    StructuredOutputReservation structuredOutputReservation)
```

Declare `IntPtr structuredOutputChildHandle = IntPtr.Zero;`, then replace the
fixed handle-list allocation with:

```csharp
if (structuredOutputReservation != null)
{
    structuredOutputChildHandle =
        structuredOutputReservation.DuplicateInheritableWriterHandle();
}
int inheritedHandleCount =
    structuredOutputReservation == null ? 3 : 4;
int inheritedHandleBytes = checked(
    IntPtr.Size * inheritedHandleCount);
inheritedHandleArray = Marshal.AllocHGlobal(inheritedHandleBytes);
Marshal.WriteIntPtr(inheritedHandleArray, 0, stdinHandle);
Marshal.WriteIntPtr(inheritedHandleArray, IntPtr.Size, stdoutHandle);
Marshal.WriteIntPtr(inheritedHandleArray, IntPtr.Size * 2, stderrHandle);
if (structuredOutputReservation != null)
{
    Marshal.WriteIntPtr(
        inheritedHandleArray,
        IntPtr.Size * 3, structuredOutputChildHandle);
}
```

Call `BuildChildEnvironmentBlock(jobName, structuredOutputChildHandle)` and
close `structuredOutputChildHandle` in the native `finally`, alongside the
other owned launch handles. Non-JSON children therefore inherit exactly three
handles and see no structured-output environment variable; JSON children
inherit exactly four and see only the gate-created decimal handle value.

Add this complete monotonic strict recognizer before
`NewSecurityAttributes`. It runs with bounded input, depth, and number-token
length; each object owns one decoded-key set with ordinal comparison:

```csharp
private sealed class StrictJsonParser
{
    private readonly string text;
    private readonly int maximumDepth;
    private readonly int maximumDocumentCharacters;
    private readonly int maximumNumberTokenLength;
    private int offset;

    internal StrictJsonParser(
        string text,
        int maximumDepth,
        int maximumDocumentCharacters,
        int maximumNumberTokenLength)
    {
        this.text = text;
        this.maximumDepth = maximumDepth;
        this.maximumDocumentCharacters = maximumDocumentCharacters;
        this.maximumNumberTokenLength = maximumNumberTokenLength;
    }

    internal void Validate()
    {
        if (text.Length > maximumDocumentCharacters)
        {
            ThrowInvalid(
                "document_too_long",
                maximumDocumentCharacters);
        }
        SkipWhitespace();
        ParseValue(0);
        SkipWhitespace();
        if (offset != text.Length)
        {
            ThrowInvalid("trailing_content");
        }
    }

    private void ParseValue(int containerDepth)
    {
        if (offset >= text.Length)
        {
            ThrowInvalid("expected_value");
        }
        char current = text[offset];
        if (current == '{')
        {
            RequireContainerDepth(containerDepth);
            ParseObject(containerDepth + 1);
            return;
        }
        if (current == '[')
        {
            RequireContainerDepth(containerDepth);
            ParseArray(containerDepth + 1);
            return;
        }
        if (current == '"')
        {
            ParseString();
            return;
        }
        if (current == '-' || IsDigit(current))
        {
            ParseNumber();
            return;
        }
        if (current == 't')
        {
            ParseLiteral("true");
            return;
        }
        if (current == 'f')
        {
            ParseLiteral("false");
            return;
        }
        if (current == 'n')
        {
            ParseLiteral("null");
            return;
        }
        ThrowInvalid("expected_value");
    }

    private void ParseObject(int containerDepth)
    {
        Expect('{');
        SkipWhitespace();
        if (Consume('}'))
        {
            return;
        }
        SortedSet<string> propertyNames = new SortedSet<string>(
            StringComparer.Ordinal);
        while (true)
        {
            if (offset >= text.Length || text[offset] != '"')
            {
                ThrowInvalid("object_property_name");
            }
            int propertyOffset = offset;
            string propertyName = ParseString();
            if (!propertyNames.Add(propertyName))
            {
                ThrowInvalid("duplicate_property", propertyOffset);
            }
            SkipWhitespace();
            Expect(':');
            SkipWhitespace();
            ParseValue(containerDepth);
            SkipWhitespace();
            if (Consume('}'))
            {
                return;
            }
            Expect(',');
            SkipWhitespace();
        }
    }

    private void ParseArray(int containerDepth)
    {
        Expect('[');
        SkipWhitespace();
        if (Consume(']'))
        {
            return;
        }
        while (true)
        {
            ParseValue(containerDepth);
            SkipWhitespace();
            if (Consume(']'))
            {
                return;
            }
            Expect(',');
            SkipWhitespace();
        }
    }

    private string ParseString()
    {
        Expect('"');
        StringBuilder decoded = new StringBuilder();
        while (offset < text.Length)
        {
            int characterOffset = offset;
            char current = text[offset++];
            if (current == '"')
            {
                return decoded.ToString();
            }
            if (current == '\\')
            {
                ParseEscape(decoded, characterOffset);
                continue;
            }
            if (current <= '\u001f')
            {
                ThrowInvalid("unescaped_control", characterOffset);
            }
            if (Char.IsHighSurrogate(current))
            {
                if (offset >= text.Length ||
                    !Char.IsLowSurrogate(text[offset]))
                {
                    ThrowInvalid(
                        "unpaired_high_surrogate",
                        characterOffset);
                }
                decoded.Append(current);
                decoded.Append(text[offset++]);
                continue;
            }
            if (Char.IsLowSurrogate(current))
            {
                ThrowInvalid(
                    "unpaired_low_surrogate",
                    characterOffset);
            }
            decoded.Append(current);
        }
        ThrowInvalid("unterminated_string");
        return null;
    }

    private void ParseEscape(StringBuilder decoded, int escapeOffset)
    {
        if (offset >= text.Length)
        {
            ThrowInvalid("unterminated_escape", escapeOffset);
        }
        int escapedOffset = offset;
        char escaped = text[offset++];
        switch (escaped)
        {
            case '"': decoded.Append('"'); return;
            case '\\': decoded.Append('\\'); return;
            case '/': decoded.Append('/'); return;
            case 'b': decoded.Append('\b'); return;
            case 'f': decoded.Append('\f'); return;
            case 'n': decoded.Append('\n'); return;
            case 'r': decoded.Append('\r'); return;
            case 't': decoded.Append('\t'); return;
            case 'u':
                int codeUnit = ParseHexCodeUnit();
                if (codeUnit >= 0xd800 && codeUnit <= 0xdbff)
                {
                    if (offset + 6 > text.Length ||
                        text[offset] != '\\' ||
                        text[offset + 1] != 'u')
                    {
                        ThrowInvalid(
                            "escaped_high_surrogate_requires_low",
                            escapeOffset);
                    }
                    int lowEscapeOffset = offset;
                    offset += 2;
                    int low = ParseHexCodeUnit();
                    if (low < 0xdc00 || low > 0xdfff)
                    {
                        ThrowInvalid(
                            "escaped_high_surrogate_requires_low",
                            lowEscapeOffset);
                    }
                    decoded.Append((char)codeUnit);
                    decoded.Append((char)low);
                    return;
                }
                if (codeUnit >= 0xdc00 && codeUnit <= 0xdfff)
                {
                    ThrowInvalid(
                        "unpaired_escaped_low_surrogate",
                        escapeOffset);
                }
                decoded.Append((char)codeUnit);
                return;
            default:
                ThrowInvalid("unknown_escape", escapedOffset);
                return;
        }
    }

    private int ParseHexCodeUnit()
    {
        if (offset + 4 > text.Length)
        {
            ThrowInvalid("incomplete_unicode_escape");
        }
        int value = 0;
        for (int index = 0; index < 4; index++)
        {
            int digitOffset = offset;
            char digit = text[offset++];
            int nibble;
            if (digit >= '0' && digit <= '9')
            {
                nibble = digit - '0';
            }
            else if (digit >= 'a' && digit <= 'f')
            {
                nibble = digit - 'a' + 10;
            }
            else if (digit >= 'A' && digit <= 'F')
            {
                nibble = digit - 'A' + 10;
            }
            else
            {
                ThrowInvalid("invalid_unicode_hex", digitOffset);
                return 0;
            }
            value = (value << 4) | nibble;
        }
        return value;
    }

    private void ParseNumber()
    {
        int numberStart = offset;
        if (Consume('-'))
        {
            RequireNumberLength(numberStart);
        }
        if (offset >= text.Length)
        {
            ThrowInvalid("incomplete_number");
        }
        if (Consume('0'))
        {
            RequireNumberLength(numberStart);
            if (offset < text.Length && IsDigit(text[offset]))
            {
                ThrowInvalid("leading_zero");
            }
        }
        else
        {
            if (offset >= text.Length ||
                text[offset] < '1' || text[offset] > '9')
            {
                ThrowInvalid("invalid_integer");
            }
            ConsumeDigits(numberStart);
        }
        if (Consume('.'))
        {
            RequireNumberLength(numberStart);
            if (offset >= text.Length || !IsDigit(text[offset]))
            {
                ThrowInvalid("fraction_digit_required");
            }
            ConsumeDigits(numberStart);
        }
        if (offset < text.Length &&
            (text[offset] == 'e' || text[offset] == 'E'))
        {
            offset++;
            RequireNumberLength(numberStart);
            if (offset < text.Length &&
                (text[offset] == '+' || text[offset] == '-'))
            {
                offset++;
                RequireNumberLength(numberStart);
            }
            if (offset >= text.Length || !IsDigit(text[offset]))
            {
                ThrowInvalid("exponent_digit_required");
            }
            ConsumeDigits(numberStart);
        }
    }

    private void ConsumeDigits(int numberStart)
    {
        while (offset < text.Length && IsDigit(text[offset]))
        {
            offset++;
            RequireNumberLength(numberStart);
        }
    }

    private void RequireNumberLength(int numberStart)
    {
        if (offset - numberStart > maximumNumberTokenLength)
        {
            ThrowInvalid(
                "number_too_long",
                numberStart + maximumNumberTokenLength);
        }
    }

    private static bool IsDigit(char value)
    {
        return value >= '0' && value <= '9';
    }

    private void ParseLiteral(string literal)
    {
        for (int index = 0; index < literal.Length; index++)
        {
            int literalOffset = offset + index;
            if (literalOffset >= text.Length ||
                text[literalOffset] != literal[index])
            {
                ThrowInvalid("invalid_literal", literalOffset);
            }
        }
        offset += literal.Length;
    }

    private void RequireContainerDepth(int containerDepth)
    {
        if (containerDepth >= maximumDepth)
        {
            ThrowInvalid("maximum_depth");
        }
    }

    private void SkipWhitespace()
    {
        while (offset < text.Length)
        {
            char current = text[offset];
            if (current != ' ' && current != '\t' &&
                current != '\r' && current != '\n')
            {
                return;
            }
            offset++;
        }
    }

    private bool Consume(char expected)
    {
        if (offset < text.Length && text[offset] == expected)
        {
            offset++;
            return true;
        }
        return false;
    }

    private void Expect(char expected)
    {
        if (!Consume(expected))
        {
            ThrowInvalid("expected_token");
        }
    }

    private void ThrowInvalid(string reason)
    {
        ThrowInvalid(reason, offset);
    }

    private void ThrowInvalid(string reason, int failureOffset)
    {
        throw new FormatException(
            "strict_json:" + reason +
            " at UTF-16 offset " +
            failureOffset.ToString(CultureInfo.InvariantCulture) +
            ".");
    }
}
```

Replace every Task 3 catalog copy of `ObserveRootAccountingExit` and
`TryIsProcessRunning` with these exact E4 bodies. `WAIT_TIMEOUT` alone is not a
live-process verdict: an already-published exit code other than `STILL_ACTIVE`
is a bounded PowerShell teardown tail. API failure remains fail-closed and a
true live grandchild remains a process-tree failure:

```csharp
private static bool ObserveRootAccountingExit(
    IntPtr job,
    uint rootProcessId,
    BoundedProcessResult result,
    out bool hadDescendant)
{
    hadDescendant = false;
    Stopwatch accountingClock = Stopwatch.StartNew();
    while (true)
    {
        ulong[] processIds;
        if (!TryGetJobProcessIds(job, result, out processIds))
        {
            return false;
        }

        bool rootStillListed = false;
        for (int index = 0; index < processIds.Length; index++)
        {
            if (processIds[index] == rootProcessId)
            {
                rootStillListed = true;
            }
            else
            {
                bool isRunning;
                if (!TryIsProcessRunning(processIds[index], result, out isRunning))
                {
                    return false;
                }
                if (isRunning)
                {
                    hadDescendant = true;
                    return true;
                }
            }
        }

        if (!rootStillListed)
        {
            uint activeProcesses;
            if (!TryGetActiveProcessCount(
                job,
                out activeProcesses,
                result))
            {
                return false;
            }
            if (activeProcesses == 0)
            {
                return true;
            }
            if (accountingClock.ElapsedMilliseconds >= CleanupTimeoutMilliseconds)
            {
                AddEngineError(
                    result,
                    "Job Object accounting remained active without a running " +
                    "process ID after the accounting bound.");
                return false;
            }
            Thread.Sleep(CleanupPollMilliseconds);
            continue;
        }
        if (accountingClock.ElapsedMilliseconds >= CleanupTimeoutMilliseconds)
        {
            AddEngineError(
                result,
                "Signaled root process remained in the Job Object process list " +
                "after the accounting bound.");
            return false;
        }
        Thread.Sleep(CleanupPollMilliseconds);
    }
}

private static bool TryIsProcessRunning(
    ulong processId,
    BoundedProcessResult result,
    out bool isRunning)
{
    isRunning = false;
    if (processId > UInt32.MaxValue)
    {
        AddEngineError(result, "Job Object returned an invalid process ID.");
        return false;
    }
    IntPtr process = OpenProcess(
        SynchronizeAccess | ProcessQueryLimitedInformation,
        false,
        unchecked((uint)processId));
    if (process == IntPtr.Zero)
    {
        int error = Marshal.GetLastWin32Error();
        if (error == ErrorInvalidParameter)
        {
            return true;
        }
        AddEngineError(
            result,
            Win32Error("OpenProcess(job-descendant)", error));
        return false;
    }
    try
    {
        uint wait = WaitForSingleObject(process, 0);
        if (wait == WaitObject0)
        {
            return true;
        }
        if (wait == WaitTimeout)
        {
            uint exitCode;
            if (!GetExitCodeProcess(process, out exitCode))
            {
                AddEngineError(
                    result,
                    LastError("GetExitCodeProcess(job-descendant)"));
                return false;
            }
            if (exitCode != StillActive)
            {
                return true;
            }
            isRunning = true;
            return true;
        }
        AddEngineError(
            result,
            wait == WaitFailed
                ? LastError("WaitForSingleObject(job-descendant)")
                : "Unexpected Job descendant wait status 0x" +
                    wait.ToString("X8", CultureInfo.InvariantCulture));
        return false;
    }
    finally
    {
        CloseHandle(process);
    }
}
```

Replace Task 3's provisional `Get-NarrativeGateManifest` with:

```powershell
function Get-GateArtifactStem {
    param(
        [Parameter(Mandatory = $true)][int]$Ordinal,
        [Parameter(Mandatory = $true)][string]$StepName
    )
    '{0}-{1:D2}-{2}-{3}' -f `
        $Gate.ToLowerInvariant(), $Ordinal, $StepName, $script:HeadToken
}

function Get-GateStructuredOutputPath {
    param(
        [Parameter(Mandatory = $true)]$Step,
        [Parameter(Mandatory = $true)][int]$Ordinal
    )
    if ($Step.Postcondition -ne 'capability-json') { return $null }
    $leaf = "$(Get-GateArtifactStem -Ordinal $Ordinal -StepName $Step.Name).output.json"
    Join-Path $script:EvidenceIdentity.FinalPath $leaf
}

function Get-GateStructuredOutputDirectoryIdentity {
    param([Parameter(Mandatory = $true)][string]$Path)

    $fullPath = [IO.Path]::GetFullPath($Path)
    $parentPath = [IO.Path]::GetFullPath(
        [IO.Path]::GetDirectoryName($fullPath)).TrimEnd('\')
    $matches = New-Object 'System.Collections.Generic.List[object]'
    foreach ($identity in $script:GateDirectoryIdentities) {
        $registeredPath = [IO.Path]::GetFullPath(
            $identity.FinalPath).TrimEnd('\')
        if ([string]::Equals(
            $parentPath,
            $registeredPath,
            [StringComparison]::OrdinalIgnoreCase)) {
            [void]$matches.Add($identity)
        }
    }
    if ($matches.Count -ne 1) {
        throw [FormatException]::new(
            'Structured output must have exactly one registered direct parent.')
    }
    $matches[0]
}

function Get-NarrativeGateManifest {
    $checker = Get-ExpectedProjectFilePath `
        $script:ProjectIdentity.FinalPath `
        'Tools\check_winter_narrative_capabilities.py'
    $phase = if ($NarrativePhase -eq 'Batch') { 'batch' } else { 'final' }
    $output = Join-Path `
        $script:EvidenceIdentity.FinalPath `
        ("$(Get-GateArtifactStem 1 'narrative-capability').output.json")
    [object[]]@(
        (New-GateStep `
            'narrative-capability' `
            'Python' `
            $script:PythonIdentity.FinalPath `
            ([string[]]@(
                '-B', $checker, '--phase', $phase,
                '--format', 'json', '--output', $output)) `
            $ToolTimeoutSeconds `
            'capability-json' `
            ([string[]]@($checker)))
    )
}
```

After the existing `Write-GateSummaryJson`, add the reservation disposer below.
It is called only by the top-level `finally` shown later; it is never called
inside `Invoke-WinterInterludeGate` and therefore keeps every owner reservation
alive through summary publication:

```powershell
function Close-GateStructuredOutputReservations {
    $reservations = $script:StructuredOutputReservations
    if ($null -eq $reservations) {
        return
    }

    $script:StructuredOutputReservations = $null
    $firstError = $null
    for ($index = $reservations.Count - 1; $index -ge 0; $index--) {
        try {
            $reservations[$index].Dispose()
        }
        catch {
            if ($null -eq $firstError) {
                $firstError = $_
            }
        }
    }
    $reservations.Clear()
    if ($null -ne $firstError) {
        throw $firstError
    }
}
```

Replace the global invocation tail after the existing marked public bridge with
this exact owner-lifetime wrapper. The `finally` is intentionally outside
`Invoke-WinterInterludeGate`; closing before any success or failure summary is
an ownership regression:

```powershell
$script:StructuredOutputReservations = $null
$exitCode = 0
try {
    Invoke-WinterInterludeGate
}
catch {
    [Console]::Error.WriteLine($_.ToString())
    $exitCode = 1
}
finally {
    try {
        Close-GateStructuredOutputReservations
    }
    catch {
        [Console]::Error.WriteLine($_.ToString())
        $exitCode = 1
    }
}
exit $exitCode
```

In `Invoke-WinterInterludeGate`, replace the manifest uniqueness condition with
this exact E1 expression; without the array wrapper WinPS 5.1 can bind `.Count`
to the pipeline result rather than the complete unique-name array:

```powershell
if (@($manifestNames | Select-Object -Unique).Count -ne $manifestNames.Count) {
    throw 'Manifest step names are not unique.'
}
```

Add the exact capability reader and validator. Strict validation is deliberately
between owner-handle freeze/read and `ConvertFrom-Json`; changing this order
must fail `assert_strict_json_validation_order` and its reversible bypass
mutation:

```powershell
function Assert-ExactJsonProperties {
    param(
        [Parameter(Mandatory = $true)]$Object,
        [Parameter(Mandatory = $true)][string[]]$Expected,
        [Parameter(Mandatory = $true)][string]$Label
    )
    if ($null -eq $Object) {
        throw [FormatException]::new("$Label must be an object.")
    }
    $actual = [string[]]@($Object.PSObject.Properties.Name)
    if ($actual.Count -ne $Expected.Count) {
        throw [FormatException]::new("$Label has the wrong property count.")
    }
    foreach ($name in $Expected) {
        if (-not ($actual -ccontains $name)) {
            throw [FormatException]::new(
                "$Label is missing exact property '$name'.")
        }
    }
}

function Assert-JsonInteger {
    param(
        $Value,
        [Parameter(Mandatory = $true)][string]$Label,
        [switch]$Positive
    )
    if (-not ($Value -is [int] -or $Value -is [long])) {
        throw [FormatException]::new("$Label must be an integer.")
    }
    if ($Positive -and [long]$Value -le 0) {
        throw [FormatException]::new("$Label must be positive.")
    }
    if (-not $Positive -and [long]$Value -lt 0) {
        throw [FormatException]::new("$Label must be nonnegative.")
    }
}

function Read-GateStructuredJson {
    param(
        [Parameter(Mandatory = $true)]$Reservation,
        [Parameter(Mandatory = $true)][ref]$HasContent
    )

    $HasContent.Value = $false
    $snapshot = [WinterGate.Native]::FreezeStructuredOutput(
        $Reservation,
        1048576)
    if (-not [bool]$snapshot.HasContent) {
        return $null
    }

    $HasContent.Value = $true
    $raw = [string]$snapshot.Text
    [WinterGate.Native]::ValidateStrictJson($raw)
    $document = $raw | ConvertFrom-Json -ErrorAction Stop
    if ($null -eq $document -or
        $document -is [Array] -or
        $document.GetType().FullName -cne
            'System.Management.Automation.PSCustomObject') {
        throw [FormatException]::new('Structured JSON root must be one object.')
    }
    $document
}

function Get-GateJsonOutcome {
    param(
        [Parameter(Mandatory = $true)][string]$Postcondition,
        [Parameter(Mandatory = $true)]$Document
    )
    if ($Postcondition -ne 'capability-json') {
        throw [FormatException]::new(
            "Structured postcondition '$Postcondition' is unavailable.")
    }

    Assert-ExactJsonProperties $Document ([string[]]@(
        'schema_version', 'tool', 'phase', 'ready', 'capabilities'
    )) 'capability document'
    Assert-JsonInteger $Document.schema_version 'schema_version'
    if ([long]$Document.schema_version -ne 1 -or
        -not ($Document.tool -is [string]) -or
        $Document.tool -cne 'winter_narrative_capabilities') {
        throw [FormatException]::new('Capability schema/tool is wrong.')
    }
    $expectedPhase = if ($NarrativePhase -eq 'Batch') { 'batch' } else { 'final' }
    if (-not ($Document.phase -is [string]) -or
        $Document.phase -cne $expectedPhase -or
        -not ($Document.ready -is [bool])) {
        throw [FormatException]::new(
            'Capability phase/ready type is inconsistent.')
    }
    Assert-ExactJsonProperties $Document.capabilities ([string[]]@(
        'canon_json', 'portrait_json', 'overlap_json',
        'show_before_json', 'nested_quote_json',
        'batch_contracts', 'final_contracts'
    )) 'capabilities'
    foreach ($property in $Document.capabilities.PSObject.Properties) {
        if (-not ($property.Value -is [bool])) {
            throw [FormatException]::new(
                "Capability '$($property.Name)' must be Boolean.")
        }
    }
    $required = @(
        $Document.capabilities.canon_json,
        $Document.capabilities.portrait_json,
        $Document.capabilities.overlap_json,
        $Document.capabilities.show_before_json,
        $Document.capabilities.nested_quote_json,
        $Document.capabilities.batch_contracts
    )
    $passes = $Document.ready -and -not ($required -contains $false)
    if ($NarrativePhase -eq 'Final') {
        $passes = $passes -and $Document.capabilities.final_contracts
    }
    [pscustomobject]@{ Passes = [bool]$passes }
}
```

Replace the current Task 4 `Invoke-GateStep` with the exact merged dispatcher
below. Copy this whole body; do not reconstruct it from the earlier Task 3 or
Task 5 fragments. It retains both dependency-identity checks, readable
executable identity, the unsafe-live-tree hard stop, output-evidence ownership
precedence and null references, the unowned-summary check, and the final
`Assert-NonEvidenceGateDirectoryIdentities` prewrite guard. It adds only the
Task 5 artifact stem, structured-output reservation, JSON validation and
semantic precedence, and manual-review postcondition. The current Process and
Structural Manifest tests must remain GREEN.

```powershell
function Invoke-GateStep {
    param(
        [Parameter(Mandatory = $true)]$Step,
        [Parameter(Mandatory = $true)][int]$Ordinal
    )
    Assert-AllGateDirectoryIdentities
    $stem = Get-GateArtifactStem -Ordinal $Ordinal -StepName $Step.Name
    $stdoutLeaf = "$stem.stdout.txt"
    $stderrLeaf = "$stem.stderr.txt"
    $resultLeaf = "$stem.result.json"
    $stdoutPath = Join-Path $script:EvidenceIdentity.FinalPath $stdoutLeaf
    $stderrPath = Join-Path $script:EvidenceIdentity.FinalPath $stderrLeaf
    $resultPath = Join-Path $script:EvidenceIdentity.FinalPath $resultLeaf
    $stdoutRelative = "evidence/$stdoutLeaf"
    $stderrRelative = "evidence/$stderrLeaf"
    $resultRelative = "evidence/$resultLeaf"
    $arguments = [string[]]$Step.Arguments.Clone()

    $validationError = Get-GateStepDependencyValidationError $Step
    if ($null -ne $validationError) {
        $failed = New-ValidationGateResult `
            -Step $Step -Ordinal $Ordinal `
            -ResultRelative $resultRelative -ErrorText $validationError
        Write-GateEvidenceJson -Path $resultPath -Value $failed
        return $failed
    }

    $jsonOutput = Get-GateStructuredOutputPath -Step $Step -Ordinal $Ordinal
    $jsonReservation = $null
    $reservationError = $null
    if ($null -ne $jsonOutput) {
        $reservationRegistered = $false
        try {
            $jsonOutputDirectoryIdentity =
                Get-GateStructuredOutputDirectoryIdentity -Path $jsonOutput
            $jsonReservation =
                [WinterGate.Native]::ReserveStructuredOutput(
                    $jsonOutput,
                    $jsonOutputDirectoryIdentity)
            [void]$script:StructuredOutputReservations.Add(
                $jsonReservation)
            $reservationRegistered = $true
        }
        catch {
            if ($null -ne $jsonReservation -and
                -not $reservationRegistered) {
                $unregisteredReservation = $jsonReservation
                $jsonReservation = $null
                $unregisteredReservation.Dispose()
            }
            $unwrapped = Get-UnwrappedException $_.Exception
            if ($unwrapped -is
                    [WinterGate.WinterGatePathIdentityException] -or
                $unwrapped -is [FormatException]) {
                $reservationError =
                    "Structured output is not a new regular file path: $jsonOutput"
            }
            else {
                throw
            }
        }
    }

    if ($null -ne $reservationError) {
        $failed = New-ValidationGateResult `
            -Step $Step -Ordinal $Ordinal `
            -ResultRelative $resultRelative -ErrorText $reservationError
        Write-GateEvidenceJson -Path $resultPath -Value $failed
        return $failed
    }
    Assert-AllGateDirectoryIdentities

    $process = [WinterGate.Native]::RunProcessTree(
        $Step.Executable,
        $arguments,
        $script:ProjectIdentity.FinalPath,
        $stdoutPath,
        $stderrPath,
        [int]($Step.TimeoutSeconds * 1000),
        $script:EvidenceIdentity,
        $jsonReservation)

    if ($process.ProcessStarted -and -not $process.TreeDrained) {
        $script:EvidencePublicationSafe = $false
        throw [InvalidOperationException]::new(
            "Step '$($Step.Name)' left a live process tree; evidence publication is unsafe.")
    }
    $postRunValidationError =
        Get-GateStepDependencyValidationError $Step
    $unownedSummaryDetected = $null -ne (
        [WinterGate.Native]::TryGetReadableFileIdentity($script:SummaryPath))
    Assert-NonEvidenceGateDirectoryIdentities
    $failureKind = $null
    $errorText = $null

    if ($unownedSummaryDetected) {
        $failureKind = 'validation'
        $errorText =
            'Unowned gate-summary.json appeared while a gate step was running.'
    }
    elseif ($null -ne $postRunValidationError) {
        $failureKind = 'validation'
        $errorText = $postRunValidationError
    }
    elseif (-not $process.ProcessStarted) {
        $failureKind = 'process'
        $errorText = $process.StartError
    }
    elseif ($process.ProcessStarted -and
            -not [bool]$process.OutputEvidenceValid) {
        $failureKind = 'validation'
        $errorText =
            "Step '$($Step.Name)' output evidence identity validation failed."
        if (-not [string]::IsNullOrWhiteSpace(
            [string]$process.OutputEvidenceError)) {
            $errorText += " $([string]$process.OutputEvidenceError)"
        }
    }
    elseif ($process.TimedOut) {
        $failureKind = 'timeout'
        $errorText = "Step '$($Step.Name)' exceeded $($Step.TimeoutSeconds) seconds."
    }
    elseif (-not $process.TreeDrained -or
            $process.HadLiveDescendantsAfterRootExit -or
            -not [string]::IsNullOrWhiteSpace($process.StartError)) {
        $failureKind = 'process_tree'
        $errorText = if (-not [string]::IsNullOrWhiteSpace($process.StartError)) {
            $process.StartError
        } else {
            "Step '$($Step.Name)' violated its bounded process tree."
        }
    }

    if ($null -eq $failureKind -and $null -ne $jsonOutput) {
        $jsonHasContent = $false
        Assert-NonEvidenceGateDirectoryIdentities
        try {
            $document = Read-GateStructuredJson `
                -Reservation $jsonReservation `
                -HasContent ([ref]$jsonHasContent)
            if ($jsonHasContent) {
                $outcome = Get-GateJsonOutcome `
                    -Postcondition $Step.Postcondition `
                    -Document $document
            }
        }
        catch {
            $failureKind = 'invalid_evidence'
            $errorText =
                "Invalid JSON evidence for '$($Step.Name)': $($_.Exception.Message)"
        }
        Assert-NonEvidenceGateDirectoryIdentities
        if ($null -eq $failureKind -and -not $jsonHasContent) {
            if ([int]$process.ExitCode -ne 0) {
                $failureKind = 'process'
                $errorText =
                    "Step '$($Step.Name)' exited $([int]$process.ExitCode) without JSON output."
            }
            else {
                $failureKind = 'invalid_evidence'
                $errorText =
                    "Step '$($Step.Name)' did not create its JSON output."
            }
        }
        elseif ($null -eq $failureKind) {
            if (-not $outcome.Passes) {
                $failureKind = 'postcondition'
                $errorText =
                    "Structured postcondition failed for '$($Step.Name)'."
            }
            elseif ([int]$process.ExitCode -ne 0) {
                $failureKind = 'process'
                $errorText =
                    "Step '$($Step.Name)' exited $([int]$process.ExitCode)."
            }
        }
    }
    elseif ($null -eq $failureKind) {
        if ([int]$process.ExitCode -ne 0) {
            $failureKind = 'process'
            $errorText =
                "Step '$($Step.Name)' exited $([int]$process.ExitCode)."
        }
        elseif ($Step.Postcondition -eq 'manual-review' -and
                -not [IO.File]::Exists($stdoutPath)) {
            $failureKind = 'postcondition'
            $errorText =
                "Manual-review stdout is missing for '$($Step.Name)'."
        }
        elseif ($Step.Postcondition -notin @(
            'exit-zero', 'runner-passed', 'manual-review'
        )) {
            $failureKind = 'validation'
            $errorText =
                "Unknown postcondition '$($Step.Postcondition)'."
        }
    }

    $outputEvidenceTrusted = [bool]$process.OutputEvidenceValid
    $result = [pscustomobject][ordered]@{
        ordinal = $Ordinal
        name = $Step.Name
        kind = $Step.Kind
        executable = $Step.Executable
        arguments = [string[]]$arguments.Clone()
        working_directory = $script:ProjectIdentity.FinalPath
        process_started = [bool]$process.ProcessStarted
        process_id = $process.ProcessId
        started_utc = if ($null -eq $process.StartedUtc) {
            $null
        } else { ([DateTime]$process.StartedUtc).ToString('o') }
        ended_utc = if ($null -eq $process.EndedUtc) {
            $null
        } else { ([DateTime]$process.EndedUtc).ToString('o') }
        exit_code = $process.ExitCode
        timed_out = [bool]$process.TimedOut
        tree_drained = [bool]$process.TreeDrained
        had_live_descendants_after_root_exit =
            [bool]$process.HadLiveDescendantsAfterRootExit
        elapsed_milliseconds = $process.ElapsedMilliseconds
        stdout = if ($outputEvidenceTrusted) { $stdoutRelative } else { $null }
        stderr = if ($outputEvidenceTrusted) { $stderrRelative } else { $null }
        result = $resultRelative
        postcondition = $Step.Postcondition
        manual_review_required = ($Step.Postcondition -eq 'manual-review')
        status = if ($null -eq $failureKind) { 'passed' } else { 'failed' }
        failure_kind = $failureKind
        error = $errorText
    }
    Write-GateEvidenceJson -Path $resultPath -Value $result
    $result
}
```

Task 4 already removed the combined marked bootstrap boundary. A valid one-step
capability manifest is now a real exit-0 slice without adding a second bypass.
The Structural path stays unchanged and GREEN.

- [ ] **Step 4: Run the capability loop GREEN and amend**

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateCapabilityTests `
  Tools.test_winter_interlude_gate.WinterInterludeGateManifestTests -v
if ($LASTEXITCODE -ne 0) { throw 'Capability vertical slice failed.' }

python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateCapabilityTests.test_strict_json_rejects_non_rfc8259_lexemes `
  Tools.test_winter_interlude_gate.WinterInterludeGateCapabilityTests.test_strict_json_rejects_decoded_duplicate_object_keys `
  Tools.test_winter_interlude_gate.WinterInterludeGateCapabilityTests.test_strict_json_resource_boundaries_are_exact `
  Tools.test_winter_interlude_gate.WinterInterludeGateCapabilityTests.test_strict_json_strings_diagnostics_and_layering_are_exact `
  -v
if ($LASTEXITCODE -ne 0) { throw 'Strict JSON focused evidence failed.' }

python -m unittest Tools.test_winter_interlude_gate -v
if ($LASTEXITCODE -ne 0) { throw 'Full gate module failed after Loop A.' }

git add -- Tools/Run-WinterInterludeGate.ps1 Tools/test_winter_interlude_gate.py
if ($LASTEXITCODE -ne 0) { throw 'Could not stage the capability slice.' }
$staged = @(git diff --cached --name-only)
if ($LASTEXITCODE -ne 0) { throw 'Could not inspect capability staged scope.' }
if ($staged.Count -ne 2 -or
    $staged -notcontains 'Tools/Run-WinterInterludeGate.ps1' -or
    $staged -notcontains 'Tools/test_winter_interlude_gate.py') {
    throw "Unexpected capability staged scope: $($staged -join ', ')"
}
git diff --cached --check
if ($LASTEXITCODE -ne 0) { throw 'Capability staged diff check failed.' }
git commit --amend --no-edit
if ($LASTEXITCODE -ne 0) { throw 'Could not amend the capability slice.' }
```

Expected: all commands exit 0 and print `OK`; strict JSON reports `Ran 4
tests` and the full module reports `Ran 72 tests`. The full count is the Task 4 baseline
59 plus 13 capability methods: strict4 and the new reservation method add five
names, while E1--E4 and the inherited-handle assertion replace existing test
bodies without changing their class counts. The oplock test launches no fake
Python child and records a validation result with null process fields.

**Task 8 retirement hand-off (ownership only):** Task 5 intentionally leaves
the real-project missing-checker assertion as a temporary Task 7.5 boundary.
Task 6 Loop B owns only the tracked umbrella plan's hard stop and the exact
requirements for a separate, complete Task 8 narrative-delivery plan. Task 6
does not supply or authorize any Task 8 test body, production body, prose edit,
scanner edit, command sequence, staging list, or commit.

The future dedicated Task 8 plan must atomically replace (rather than retain or
rename) Task 5's temporary
`test_real_project_is_capability_first_when_checker_is_absent` method in the
same Task 8 change that creates the real checker. It must prove every real
checker capability through producer-linked negative mutations and receive
fresh Spec and Standards READY verdicts before any Task 8 implementation starts.
Task 5 Loops B and C define and consume only the future interface shape.

#### Loop B: exact nine-step Batch/Final manifest and output bindings

- [ ] **Step 5: Add the exact nine-step manifest RED tests**

Replace the shared fixture's `_output_paths` test helper with the exact no-head
map below. It is test harness data, not a gate adapter:

```python
def _output_paths(self) -> dict[str, str]:
    evidence = self.run_root / "evidence"
    return {
        "narrative-capability": str(
            evidence
            / "narrative-01-narrative-capability-no-head.output.json"
        ),
        "canon": str(
            evidence / "narrative-02-canon-no-head.output.json"
        ),
        "missing-portraits": str(
            evidence
            / "portrait"
            / "narrative-04-missing-portraits-no-head.output.json"
        ),
        "narration-overlap": str(
            evidence
            / "narrative-05-narration-overlap-no-head.output.json"
        ),
        "show-before": str(
            evidence / "narrative-06-show-before-no-head.output.json"
        ),
        "nested-quotes": str(
            evidence / "narrative-07-nested-quotes-no-head.output.json"
        ),
    }
```

Loop A already added `EMPTY_CANON`, `SCANNER_TO_TOOL`,
`empty_scanner_document`, and `passing_narrative_documents` as inert fixture
data for the reservation race. Do not redefine them. Add only the final name
tuple and exact argument builder here:

```python
EXPECTED_NARRATIVE_NAMES = (
    "narrative-capability",
    "canon",
    "ai-smell",
    "missing-portraits",
    "narration-overlap",
    "show-before",
    "nested-quotes",
    "source-contract",
    "route-matrix",
)


def expected_narrative_arguments(
    project: Path, run_root: Path, phase: str
) -> list[list[str]]:
    evidence = run_root / "evidence"
    target = project / "game" / "governance_winter_interlude.rpy"
    runner = project / "Tools" / "Run-RenPySuite.ps1"
    capability = (
        evidence
        / "narrative-01-narrative-capability-no-head.output.json"
    )
    canon = evidence / "narrative-02-canon-no-head.output.json"
    portrait = (
        evidence
        / "portrait"
        / "narrative-04-missing-portraits-no-head.output.json"
    )
    overlap = (
        evidence
        / "narrative-05-narration-overlap-no-head.output.json"
    )
    show_before = evidence / "narrative-06-show-before-no-head.output.json"
    nested = evidence / "narrative-07-nested-quotes-no-head.output.json"
    return [
        [
            "-B",
            str(project / "Tools" / "check_winter_narrative_capabilities.py"),
            "--phase",
            phase,
            "--format",
            "json",
            "--output",
            str(capability),
        ],
        [
            "-B",
            str(project / "Tools" / "scan_canon.py"),
            "--format",
            "json",
            "--output",
            str(canon),
        ],
        [
            "-B",
            str(project / "Tools" / "scan_ai_smell.py"),
            str(target),
        ],
        [
            "-B",
            str(project / "scan_missing_portraits.py"),
            "--file",
            str(target),
            "--format",
            "json",
            "--output",
            str(portrait),
        ],
        [
            "-B",
            str(project / "scan_narration_overlap.py"),
            "--file",
            str(target),
            "--format",
            "json",
            "--output",
            str(overlap),
        ],
        [
            "-B",
            str(project / "Tools" / "scan_show_before_prevention.py"),
            "--file",
            str(target),
            "--format",
            "json",
            "--output",
            str(show_before),
        ],
        [
            "-B",
            str(project / "Tools" / "scan_nested_quotes.py"),
            "--file",
            str(target),
            "--format",
            "json",
            "--output",
            str(nested),
        ],
        [
            "-m",
            "unittest",
            "Tools.test_governance_winter_interlude",
            "-v",
        ],
        [
            "-NoLogo",
            "-NoProfile",
            "-NonInteractive",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            str(runner),
            "-ProjectRoot",
            str(project),
            "-SaveDir",
            str(
                run_root
                / "savedirs"
                / "09-test_winter_interlude_route_matrix"
            ),
            "-Mode",
            "Suite",
            "-Suite",
            "test_winter_interlude_route_matrix",
            "-Expect",
            "PASSED",
            "-EvidenceDir",
            str(evidence / "runner"),
            "-TimeoutSeconds",
            "300",
        ],
    ]
```

Now replace the Loop A
`test_valid_batch_capability_uses_full_stem_and_passes` method with this
complete nine-step version. Do not leave the one-step expectation in place
after the manifest expands:

```python
    def test_valid_batch_capability_uses_full_stem_and_passes(self) -> None:
        source = GATE.read_text(encoding="utf-8")
        self.assertIn(
            "@($manifestNames | Select-Object -Unique).Count",
            source,
        )
        selector = source[
            source.index("function Get-GateStructuredOutputDirectoryIdentity {") :
            source.index("function Get-NarrativeGateManifest {")
        ]
        self.assertIn("[IO.Path]::GetDirectoryName($fullPath)", selector)
        self.assertIn("$script:GateDirectoryIdentities", selector)
        self.assertIn("[StringComparison]::OrdinalIgnoreCase", selector)
        self.assertIn("if ($matches.Count -ne 1)", selector)
        self.assertNotIn("StartsWith(", selector)
        fixture = self.make_project()
        try:
            completed = fixture.run(
                "Narrative",
                "Batch",
                documents=passing_narrative_documents("batch"),
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            summary = fixture.summary()
            self.assertEqual(summary["status"], "passed")
            self.assertEqual(len(summary["steps"]), 9)
            self.assertEqual(
                [step["name"] for step in summary["steps"]],
                list(EXPECTED_NARRATIVE_NAMES),
            )
            step = summary["steps"][0]
            self.assertEqual(step["ordinal"], 1)
            self.assertEqual(step["name"], "narrative-capability")
            expected = (
                fixture.run_root
                / "evidence"
                / "narrative-01-narrative-capability-no-head.output.json"
            )
            self.assertEqual(
                fixture.output_path("narrative-capability"), expected
            )
            self.assertEqual(step["arguments"][-1], str(expected))
            records = fixture.records()
            self.assertEqual(len(records), 9)
            self.assertEqual(records[0]["ordinal"], 1)
            self.assertEqual(records[0]["step"], "narrative-capability")
            self.assertEqual(
                records[0]["argv"],
                expected_narrative_arguments(
                    fixture.root, fixture.run_root, "batch"
                )[0],
            )
            self.assertEqual(records[0]["argv"][-1], str(expected))
            self.assertTrue(expected.is_file())
            portrait = fixture.output_path("missing-portraits")
            self.assertEqual(
                portrait.parent,
                fixture.run_root / "evidence" / "portrait",
            )
            self.assertEqual(records[3]["step"], "missing-portraits")
            self.assertEqual(records[3]["argv"][-1], str(portrait))
            self.assertRegex(
                str(records[3]["structured_output_handle"]),
                r"^[1-9][0-9]*$",
            )
            self.assertTrue(portrait.is_file())
        finally:
            fixture.close()
```

Add the exact manifest class:

```python
class WinterInterludeGateNarrativeManifestTests(_GateBlackBoxCase):
    def test_batch_and_final_manifests_are_exact(self) -> None:
        for public_phase, wire_phase in (("Batch", "batch"), ("Final", "final")):
            with self.subTest(phase=public_phase):
                fixture = self.make_project()
                try:
                    completed = fixture.run(
                        "Narrative",
                        public_phase,
                        documents=passing_narrative_documents(wire_phase),
                    )
                    self.assertEqual(completed.returncode, 0, completed.stderr)
                    summary = fixture.summary()
                    self.assertEqual(summary["gate"], "Narrative")
                    self.assertEqual(
                        summary["narrative_phase"], public_phase
                    )
                    self.assertEqual(
                        [step["name"] for step in summary["steps"]],
                        list(EXPECTED_NARRATIVE_NAMES),
                    )
                    expected_arguments = expected_narrative_arguments(
                        fixture.root, fixture.run_root, wire_phase
                    )
                    self.assertEqual(
                        [step["arguments"] for step in summary["steps"]],
                        expected_arguments,
                    )
                    self.assertTrue(
                        all(
                            os.path.samefile(
                                step["executable"], fixture.python_exe
                            )
                            for step in summary["steps"][:8]
                        )
                    )
                    self.assertTrue(
                        os.path.samefile(
                            summary["steps"][8]["executable"], POWERSHELL
                        )
                    )
                    records = fixture.records()
                    self.assertEqual(len(records), 9)
                    self.assertEqual(
                        [record["step"] for record in records],
                        [
                            *EXPECTED_NARRATIVE_NAMES[:8],
                            "test-winter-interlude-route-matrix",
                        ],
                    )
                    self.assertEqual(
                        [record["argv"] for record in records[:8]],
                        expected_arguments[:8],
                    )
                    self.assertNotIn("--file", records[1]["argv"])
                    self.assertEqual(
                        records[-1]["parameters"],
                        {
                            "ProjectRoot": str(fixture.root),
                            "SaveDir": str(
                                fixture.run_root
                                / "savedirs"
                                / "09-test_winter_interlude_route_matrix"
                            ),
                            "Mode": "Suite",
                            "Suite": "test_winter_interlude_route_matrix",
                            "Expect": "PASSED",
                            "EvidenceDir": str(
                                fixture.run_root / "evidence" / "runner"
                            ),
                            "TimeoutSeconds": 300,
                        },
                    )
                finally:
                    fixture.close()

    def test_all_machine_json_paths_have_exact_full_stems(self) -> None:
        fixture = self.make_project()
        try:
            completed = fixture.run(
                "Narrative",
                "Batch",
                documents=passing_narrative_documents("batch"),
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            expected = {
                "narrative-capability":
                    "narrative-01-narrative-capability-no-head.output.json",
                "canon":
                    "narrative-02-canon-no-head.output.json",
                "missing-portraits":
                    "portrait/narrative-04-missing-portraits-no-head.output.json",
                "narration-overlap":
                    "narrative-05-narration-overlap-no-head.output.json",
                "show-before":
                    "narrative-06-show-before-no-head.output.json",
                "nested-quotes":
                    "narrative-07-nested-quotes-no-head.output.json",
            }
            for step_name, relative in expected.items():
                with self.subTest(step=step_name):
                    path = fixture.output_path(step_name)
                    self.assertEqual(
                        path,
                        fixture.run_root / "evidence" / Path(relative),
                    )
                    self.assertTrue(path.is_file())
                    self.assertIn(
                        str(path),
                        next(
                            record["argv"]
                            for record in fixture.records()
                            if record["step"] == step_name
                        ),
                    )
        finally:
            fixture.close()

    def test_narrative_failure_is_fail_fast_at_every_ordinal(self) -> None:
        for failing_ordinal in range(1, 10):
            with self.subTest(failing_ordinal=failing_ordinal):
                fixture = self.make_project()
                try:
                    completed = fixture.run(
                        "Narrative",
                        "Final",
                        documents=passing_narrative_documents("final"),
                        exit_codes={failing_ordinal: 31},
                    )
                    self.assertNotEqual(completed.returncode, 0)
                    self.assertEqual(
                        len(fixture.records()), failing_ordinal
                    )
                    summary = fixture.summary()
                    self.assertEqual(
                        len(summary["steps"]), failing_ordinal
                    )
                    failed = summary["steps"][-1]
                    self.assertEqual(failed["failure_kind"], "process")
                    self.assertEqual(failed["exit_code"], 31)
                finally:
                    fixture.close()

    def test_precreated_next_output_stops_before_next_child(self) -> None:
        fixture = self.make_project()
        try:
            completed = fixture.run(
                "Narrative",
                "Batch",
                documents=passing_narrative_documents("batch"),
                precreate_after={
                    1: "narrative-02-canon-no-head.output.json"
                },
            )
            self.assertNotEqual(completed.returncode, 0)
            self.assertEqual(
                [record["step"] for record in fixture.records()],
                ["narrative-capability"],
            )
            summary = fixture.summary()
            self.assertEqual(len(summary["steps"]), 2)
            failed = summary["steps"][1]
            self.assertEqual(failed["name"], "canon")
            self.assertEqual(failed["failure_kind"], "validation")
            self.assertFalse(failed["process_started"])
            self.assertIsNone(failed["process_id"])
            self.assertIsNone(failed["stdout"])
            self.assertIsNone(failed["stderr"])
        finally:
            fixture.close()

    def test_ai_smell_is_manual_review_and_never_auto_approval(self) -> None:
        fixture = self.make_project()
        try:
            completed = fixture.run(
                "Narrative",
                "Batch",
                documents=passing_narrative_documents("batch"),
            )
            summary = fixture.summary()
            self.assertEqual(len(summary["steps"]), 9)
            self.assertEqual(
                [step["name"] for step in summary["steps"]],
                list(EXPECTED_NARRATIVE_NAMES),
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            ai = summary["steps"][2]
            self.assertEqual(ai["name"], "ai-smell")
            self.assertTrue(ai["manual_review_required"])
            self.assertNotIn("approved", ai)
            stdout = fixture.run_root / ai["stdout"]
            self.assertIn(
                "fake-python-stdout",
                stdout.read_text(encoding="utf-8", errors="replace"),
            )
            for step in summary["steps"][:2] + summary["steps"][3:]:
                self.assertFalse(step["manual_review_required"])
                self.assertNotIn("approved", step)
        finally:
            fixture.close()
```

- [ ] **Step 6: Run only the exact-manifest loop RED**

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateNarrativeManifestTests `
  -v 2>&1 |
  Tee-Object -FilePath .superpowers/sdd/task-7-5-narrative-manifest-red.txt
if ($LASTEXITCODE -eq 0) { throw 'Nine-step Narrative manifest RED unexpectedly passed.' }
```

Expected: the capability child and its exact JSON contract pass first. Tests
then fail because the public manifest has one step, not because a scanner output
is missing or because a scanner schema is rejected.

- [ ] **Step 7: Expand the manifest to exactly nine steps with provisional object-only scanner acceptance**

Keep `Get-GateStructuredOutputDirectoryIdentity` immediately after the output
path helper, and keep the complete structured helper/validator block before
`Get-GateStepDependencyValidationError`. The portrait directory identity must
be registered before the portrait output path is built; no prefix-based parent
selection is permitted.

Replace `Get-GateStructuredOutputPath` with:

```powershell
function Get-GateStructuredOutputPath {
    param(
        [Parameter(Mandatory = $true)]$Step,
        [Parameter(Mandatory = $true)][int]$Ordinal
    )
    if ($Step.Postcondition -notin @(
        'capability-json',
        'canon-json',
        'portrait-json',
        'overlap-json',
        'show-before-json',
        'nested-quote-json'
    )) {
        return $null
    }
    $leaf = "$(Get-GateArtifactStem -Ordinal $Ordinal -StepName $Step.Name).output.json"
    if ($Step.Postcondition -eq 'portrait-json') {
        return Join-Path `
            (Join-Path $script:EvidenceIdentity.FinalPath 'portrait') `
            $leaf
    }
    Join-Path $script:EvidenceIdentity.FinalPath $leaf
}
```

In `Get-GateJsonOutcome`, replace only its initial unavailable-postcondition
guard with the following exact branch. The existing capability validation below
it remains byte-for-byte unchanged. This is deliberately the smallest GREEN
for the manifest tests: every later output must be a new, stable, UTF-8 JSON
object, but schema/tool/count semantics remain RED for Loop C.

```powershell
if ($Postcondition -ne 'capability-json') {
    return [pscustomobject]@{ Passes = $true }
}
```

Replace the one-step Narrative manifest with:

```powershell
function Get-NarrativeGateManifest {
    $project = $script:ProjectIdentity.FinalPath
    $phase = if ($NarrativePhase -eq 'Batch') { 'batch' } else { 'final' }
    $checker = Get-ExpectedProjectFilePath `
        $project 'Tools\check_winter_narrative_capabilities.py'
    $canon = Get-ExpectedProjectFilePath $project 'Tools\scan_canon.py'
    $aiSmell = Get-ExpectedProjectFilePath $project 'Tools\scan_ai_smell.py'
    $portrait = Get-ExpectedProjectFilePath $project 'scan_missing_portraits.py'
    $overlap = Get-ExpectedProjectFilePath `
        $project 'scan_narration_overlap.py'
    $showBefore = Get-ExpectedProjectFilePath `
        $project 'Tools\scan_show_before_prevention.py'
    $nestedQuotes = Get-ExpectedProjectFilePath `
        $project 'Tools\scan_nested_quotes.py'
    $sourceContract = Get-ExpectedProjectFilePath `
        $project 'Tools\test_governance_winter_interlude.py'
    $runner = Get-ExpectedProjectFilePath `
        $project 'Tools\Run-RenPySuite.ps1'
    $target = Get-ExpectedProjectFilePath `
        $project 'game\governance_winter_interlude.rpy'

    $portraitIdentity = New-VerifiedChildDirectory `
        -ParentIdentity $script:EvidenceIdentity `
        -LeafName 'portrait'
    $runnerEvidenceIdentity = New-VerifiedChildDirectory `
        -ParentIdentity $script:EvidenceIdentity `
        -LeafName 'runner'
    $routeSaveIdentity = New-VerifiedChildDirectory `
        -ParentIdentity $script:SavedirsIdentity `
        -LeafName '09-test_winter_interlude_route_matrix'
    [void]$script:GateDirectoryIdentities.Add($portraitIdentity)
    [void]$script:GateDirectoryIdentities.Add($runnerEvidenceIdentity)
    [void]$script:GateDirectoryIdentities.Add($routeSaveIdentity)

    $capabilityJson = Join-Path `
        $script:EvidenceIdentity.FinalPath `
        ("$(Get-GateArtifactStem 1 'narrative-capability').output.json")
    $canonJson = Join-Path `
        $script:EvidenceIdentity.FinalPath `
        ("$(Get-GateArtifactStem 2 'canon').output.json")
    $portraitJson = Join-Path `
        $portraitIdentity.FinalPath `
        ("$(Get-GateArtifactStem 4 'missing-portraits').output.json")
    $overlapJson = Join-Path `
        $script:EvidenceIdentity.FinalPath `
        ("$(Get-GateArtifactStem 5 'narration-overlap').output.json")
    $showBeforeJson = Join-Path `
        $script:EvidenceIdentity.FinalPath `
        ("$(Get-GateArtifactStem 6 'show-before').output.json")
    $nestedQuoteJson = Join-Path `
        $script:EvidenceIdentity.FinalPath `
        ("$(Get-GateArtifactStem 7 'nested-quotes').output.json")

    [object[]]@(
        (New-GateStep 'narrative-capability' 'Python' `
            $script:PythonIdentity.FinalPath `
            ([string[]]@(
                '-B', $checker,
                '--phase', $phase,
                '--format', 'json',
                '--output', $capabilityJson
            )) $ToolTimeoutSeconds 'capability-json' `
            ([string[]]@($checker))),
        (New-GateStep 'canon' 'Python' `
            $script:PythonIdentity.FinalPath `
            ([string[]]@(
                '-B', $canon,
                '--format', 'json',
                '--output', $canonJson
            )) $ToolTimeoutSeconds 'canon-json' `
            ([string[]]@($canon))),
        (New-GateStep 'ai-smell' 'Python' `
            $script:PythonIdentity.FinalPath `
            ([string[]]@('-B', $aiSmell, $target)) `
            $ToolTimeoutSeconds 'manual-review' `
            ([string[]]@($aiSmell, $target))),
        (New-GateStep 'missing-portraits' 'Python' `
            $script:PythonIdentity.FinalPath `
            ([string[]]@(
                '-B', $portrait,
                '--file', $target,
                '--format', 'json',
                '--output', $portraitJson
            )) $ToolTimeoutSeconds 'portrait-json' `
            ([string[]]@($portrait, $target))),
        (New-GateStep 'narration-overlap' 'Python' `
            $script:PythonIdentity.FinalPath `
            ([string[]]@(
                '-B', $overlap,
                '--file', $target,
                '--format', 'json',
                '--output', $overlapJson
            )) $ToolTimeoutSeconds 'overlap-json' `
            ([string[]]@($overlap, $target))),
        (New-GateStep 'show-before' 'Python' `
            $script:PythonIdentity.FinalPath `
            ([string[]]@(
                '-B', $showBefore,
                '--file', $target,
                '--format', 'json',
                '--output', $showBeforeJson
            )) $ToolTimeoutSeconds 'show-before-json' `
            ([string[]]@($showBefore, $target))),
        (New-GateStep 'nested-quotes' 'Python' `
            $script:PythonIdentity.FinalPath `
            ([string[]]@(
                '-B', $nestedQuotes,
                '--file', $target,
                '--format', 'json',
                '--output', $nestedQuoteJson
            )) $ToolTimeoutSeconds 'nested-quote-json' `
            ([string[]]@($nestedQuotes, $target))),
        (New-GateStep 'source-contract' 'Python' `
            $script:PythonIdentity.FinalPath `
            ([string[]]@(
                '-m', 'unittest',
                'Tools.test_governance_winter_interlude', '-v'
            )) $ToolTimeoutSeconds 'exit-zero' `
            ([string[]]@($sourceContract))),
        (New-GateStep 'route-matrix' 'RenPySuite' `
            $script:TrustedPowerShellIdentity.FinalPath `
            ([string[]]@(
                '-NoLogo', '-NoProfile', '-NonInteractive',
                '-ExecutionPolicy', 'Bypass',
                '-File', $runner,
                '-ProjectRoot', $project,
                '-SaveDir', $routeSaveIdentity.FinalPath,
                '-Mode', 'Suite',
                '-Suite', 'test_winter_interlude_route_matrix',
                '-Expect', 'PASSED',
                '-EvidenceDir', $runnerEvidenceIdentity.FinalPath,
                '-TimeoutSeconds', [string]$RenPyTimeoutSeconds
            )) ($RenPyTimeoutSeconds + 60) 'runner-passed' `
            ([string[]]@($runner)))
    )
}
```

- [ ] **Step 8: Run the manifest loop GREEN and amend**

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateCapabilityTests `
  Tools.test_winter_interlude_gate.WinterInterludeGateNarrativeManifestTests `
  -v
if ($LASTEXITCODE -ne 0) { throw 'Nine-step Narrative manifest slice failed.' }

python -m unittest Tools.test_winter_interlude_gate -v
if ($LASTEXITCODE -ne 0) { throw 'Full gate module failed after Loop B.' }

git add -- Tools/Run-WinterInterludeGate.ps1 Tools/test_winter_interlude_gate.py
if ($LASTEXITCODE -ne 0) { throw 'Could not stage the Narrative manifest slice.' }
$staged = @(git diff --cached --name-only)
if ($LASTEXITCODE -ne 0) { throw 'Could not inspect Narrative staged scope.' }
if ($staged.Count -ne 2 -or
    $staged -notcontains 'Tools/Run-WinterInterludeGate.ps1' -or
    $staged -notcontains 'Tools/test_winter_interlude_gate.py') {
    throw "Unexpected Narrative staged scope: $($staged -join ', ')"
}
git diff --cached --check
if ($LASTEXITCODE -ne 0) { throw 'Narrative staged diff check failed.' }
git commit --amend --no-edit
if ($LASTEXITCODE -ne 0) { throw 'Could not amend the Narrative manifest slice.' }
```

Expected: the focused command reports `Ran 18 tests` (Capability 13 plus
NarrativeManifest 5). Batch and Final both run exactly nine public children;
all six machine JSON leaves contain gate, ordinal, step, and head token, and
the portrait leaf has exactly one registered direct parent. The full module
reports `Ran 77 tests`. Scanner schema semantics are intentionally not claimed
by this GREEN.

#### Loop C: canon/common scanner schemas and failure precedence

- [ ] **Step 9: Add scanner-specific schema and precedence RED tests**

Add the shared finding fixture and scanner test class:

```python
def one_finding(rule: str = "test-rule") -> dict[str, object]:
    return {
        "path": TARGET,
        "line": 1,
        "rule": rule,
        "message": "controlled test finding",
    }


class WinterInterludeGateScannerEvidenceTests(_GateBlackBoxCase):
    STEP_ORDINAL = {
        "canon": 2,
        "missing-portraits": 4,
        "narration-overlap": 5,
        "show-before": 6,
        "nested-quotes": 7,
    }

    def assert_step_failure(
        self,
        step_name: str,
        *,
        document: dict[str, object] | None,
        raw: str | None = None,
        exit_code: int | None = None,
        expected: str,
    ) -> None:
        fixture = self.make_project()
        try:
            documents = passing_narrative_documents("batch")
            if document is None:
                documents.pop(step_name, None)
            else:
                documents[step_name] = document
            raw_documents = (
                {} if raw is None else {step_name: raw}
            )
            ordinal = self.STEP_ORDINAL[step_name]
            completed = fixture.run(
                "Narrative",
                "Batch",
                documents=documents,
                raw_documents=raw_documents,
                exit_codes=(
                    {} if exit_code is None else {ordinal: exit_code}
                ),
            )
            self.assertNotEqual(completed.returncode, 0)
            records = fixture.records()
            self.assertEqual(
                len(records),
                ordinal,
                f"records={records!r} summary={fixture.summary()!r} "
                f"stdout={completed.stdout!r} stderr={completed.stderr!r}",
            )
            result = fixture.result(ordinal)
            self.assertEqual(result["name"], step_name)
            self.assertEqual(result["failure_kind"], expected)
        finally:
            fixture.close()

    def test_canon_rejects_malformed_schema_tool_property_and_count(self) -> None:
        extra = json.loads(json.dumps(EMPTY_CANON))
        extra["unexpected"] = True
        cases: tuple[
            tuple[str, dict[str, object] | None, str | None], ...
        ] = (
            ("malformed", None, "["),
            ("schema", {**EMPTY_CANON, "schema_version": 9}, None),
            ("tool", {**EMPTY_CANON, "tool": "not_canon"}, None),
            ("property-count", extra, None),
            ("declared-count", {**EMPTY_CANON, "blocking_count": 1}, None),
        )
        for name, document, raw in cases:
            with self.subTest(name=name):
                self.assert_step_failure(
                    "canon",
                    document=document,
                    raw=raw,
                    expected="invalid_evidence",
                )

    def test_each_common_scanner_rejects_malformed_schema_tool_and_counts(
        self,
    ) -> None:
        for step_name, expected_tool in SCANNER_TO_TOOL.items():
            valid = empty_scanner_document(step_name)
            extra = json.loads(json.dumps(valid))
            extra["unexpected"] = True
            cases: tuple[
                tuple[str, dict[str, object] | None, str | None], ...
            ] = (
                ("malformed", None, "{"),
                ("schema", {**valid, "schema_version": 2}, None),
                ("tool", {**valid, "tool": expected_tool + "_wrong"}, None),
                ("property-count", extra, None),
                ("declared-count", {**valid, "blocking_count": 1}, None),
            )
            for case_name, document, raw in cases:
                with self.subTest(step=step_name, case=case_name):
                    self.assert_step_failure(
                        step_name,
                        document=document,
                        raw=raw,
                        expected="invalid_evidence",
                    )

    def test_each_canon_blocking_category_is_postcondition(self) -> None:
        for category in (
            "anti_logic",
            "geography",
            "terminology",
            "canon_deviation",
        ):
            with self.subTest(category=category):
                document = json.loads(json.dumps(EMPTY_CANON))
                document[category] = [one_finding(category)]
                document["blocking_count"] = 1
                self.assert_step_failure(
                    "canon",
                    document=document,
                    exit_code=17,
                    expected="postcondition",
                )

    def test_canon_trigger_only_is_nonblocking(self) -> None:
        fixture = self.make_project()
        try:
            documents = passing_narrative_documents("batch")
            canon = json.loads(json.dumps(EMPTY_CANON))
            canon["informational_occurrences"] = [
                {"term": "High Court", "path": TARGET, "line": 7}
            ]
            documents["canon"] = canon
            completed = fixture.run(
                "Narrative", "Batch", documents=documents
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertEqual(fixture.result(2)["status"], "passed")
        finally:
            fixture.close()

    def test_each_common_scanner_requires_target_and_zero_findings(self) -> None:
        for step_name in SCANNER_TO_TOOL:
            with self.subTest(step=step_name, case="missing-target"):
                missing_target = empty_scanner_document(step_name)
                missing_target["scanned_files"] = ["game/another_file.rpy"]
                self.assert_step_failure(
                    step_name,
                    document=missing_target,
                    expected="invalid_evidence",
                )
            with self.subTest(step=step_name, case="positive"):
                positive = empty_scanner_document(step_name)
                positive["blocking_count"] = 1
                positive["findings"] = [one_finding(step_name)]
                self.assert_step_failure(
                    step_name,
                    document=positive,
                    exit_code=29,
                    expected="postcondition",
                )

    def test_present_malformed_beats_nonzero_and_valid_pass_uses_process(
        self,
    ) -> None:
        self.assert_step_failure(
            "narration-overlap",
            document=None,
            raw="[",
            exit_code=41,
            expected="invalid_evidence",
        )
        self.assert_step_failure(
            "narration-overlap",
            document=empty_scanner_document("narration-overlap"),
            exit_code=41,
            expected="process",
        )

    def test_common_scanner_missing_output_precedence_is_exact(self) -> None:
        self.assert_step_failure(
            "show-before",
            document=None,
            expected="invalid_evidence",
        )
        self.assert_step_failure(
            "show-before",
            document=None,
            exit_code=43,
            expected="process",
        )
```

The malformed common-scanner case supplies `raw="["` while `document=None`;
`raw_documents` therefore creates a present malformed file. The missing-output
case supplies neither. Both tests reach the real ordinal in the already-GREEN
nine-step manifest.

- [ ] **Step 10: Run only scanner schema/precedence tests RED**

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateScannerEvidenceTests `
  -v 2>&1 |
  Tee-Object -FilePath .superpowers/sdd/task-7-5-scanner-json-red.txt
if ($LASTEXITCODE -eq 0) { throw 'Scanner schema RED unexpectedly passed.' }
```

Expected: all tested scanner ordinals exist and launch. Generic JSON parsing
already rejects malformed roots, but wrong schema versions, tools, exact
property counts, declared counts, missing targets, and positive findings expose
the deliberately permissive Loop B outcome and make this command nonzero.

- [ ] **Step 11: Replace provisional scanner acceptance with exact schemas**

Add the shared path/finding validators:

```powershell
function Assert-ProjectRelativeJsonPath {
    param(
        $Value,
        [Parameter(Mandatory = $true)][string]$Label
    )
    if (-not ($Value -is [string]) -or
        [string]::IsNullOrWhiteSpace($Value) -or
        $Value.Contains('\') -or
        [IO.Path]::IsPathRooted($Value) -or
        $Value.IndexOfAny([char[]]@('*', '?', '"', '<', '>', '|', ':')) -ge 0) {
        throw [FormatException]::new(
            "$Label must be a project-relative forward-slash path.")
    }
    foreach ($part in $Value.Split('/')) {
        if ([string]::IsNullOrEmpty($part) -or
            $part -eq '.' -or
            $part -eq '..') {
            throw [FormatException]::new(
                "$Label has a non-normal path component.")
        }
    }
}

function Assert-JsonFinding {
    param(
        [Parameter(Mandatory = $true)]$Finding,
        [Parameter(Mandatory = $true)][string]$Label
    )
    Assert-ExactJsonProperties $Finding ([string[]]@(
        'path', 'line', 'rule', 'message'
    )) $Label
    Assert-ProjectRelativeJsonPath $Finding.path "$Label.path"
    Assert-JsonInteger $Finding.line "$Label.line" -Positive
    if (-not ($Finding.rule -is [string]) -or
        [string]::IsNullOrWhiteSpace($Finding.rule) -or
        -not ($Finding.message -is [string]) -or
        [string]::IsNullOrWhiteSpace($Finding.message)) {
        throw [FormatException]::new(
            "$Label rule/message must be nonempty strings.")
    }
}
```

Replace `Get-GateJsonOutcome` completely with:

```powershell
function Get-GateJsonOutcome {
    param(
        [Parameter(Mandatory = $true)][string]$Postcondition,
        [Parameter(Mandatory = $true)]$Document
    )

    if ($Postcondition -eq 'capability-json') {
        Assert-ExactJsonProperties $Document ([string[]]@(
            'schema_version', 'tool', 'phase', 'ready', 'capabilities'
        )) 'capability document'
        Assert-JsonInteger $Document.schema_version 'schema_version'
        if ([long]$Document.schema_version -ne 1 -or
            -not ($Document.tool -is [string]) -or
            $Document.tool -cne 'winter_narrative_capabilities') {
            throw [FormatException]::new('Capability schema/tool is wrong.')
        }
        $expectedPhase = if ($NarrativePhase -eq 'Batch') {
            'batch'
        } else {
            'final'
        }
        if (-not ($Document.phase -is [string]) -or
            $Document.phase -cne $expectedPhase -or
            -not ($Document.ready -is [bool])) {
            throw [FormatException]::new(
                'Capability phase/ready type is inconsistent.')
        }
        Assert-ExactJsonProperties $Document.capabilities ([string[]]@(
            'canon_json', 'portrait_json', 'overlap_json',
            'show_before_json', 'nested_quote_json',
            'batch_contracts', 'final_contracts'
        )) 'capabilities'
        foreach ($property in $Document.capabilities.PSObject.Properties) {
            if (-not ($property.Value -is [bool])) {
                throw [FormatException]::new(
                    "Capability '$($property.Name)' must be Boolean.")
            }
        }
        $required = @(
            $Document.capabilities.canon_json,
            $Document.capabilities.portrait_json,
            $Document.capabilities.overlap_json,
            $Document.capabilities.show_before_json,
            $Document.capabilities.nested_quote_json,
            $Document.capabilities.batch_contracts
        )
        $passes = $Document.ready -and -not ($required -contains $false)
        if ($NarrativePhase -eq 'Final') {
            $passes = $passes -and $Document.capabilities.final_contracts
        }
        return [pscustomobject]@{ Passes = [bool]$passes }
    }

    if ($Postcondition -eq 'canon-json') {
        Assert-ExactJsonProperties $Document ([string[]]@(
            'schema_version',
            'tool',
            'blocking_count',
            'anti_logic',
            'geography',
            'terminology',
            'canon_deviation',
            'informational_occurrences'
        )) 'canon document'
        Assert-JsonInteger $Document.schema_version 'schema_version'
        if ([long]$Document.schema_version -ne 1 -or
            -not ($Document.tool -is [string]) -or
            $Document.tool -cne 'canon') {
            throw [FormatException]::new('Canon schema/tool is wrong.')
        }
        Assert-JsonInteger $Document.blocking_count 'blocking_count'
        $computed = 0
        foreach ($category in @(
            'anti_logic',
            'geography',
            'terminology',
            'canon_deviation'
        )) {
            $values = $Document.$category
            if (-not ($values -is [Array])) {
                throw [FormatException]::new(
                    "Canon $category must be an array.")
            }
            for ($index = 0; $index -lt $values.Count; $index++) {
                Assert-JsonFinding `
                    $values[$index] `
                    "$category[$index]"
            }
            $computed += $values.Count
        }
        if (-not ($Document.informational_occurrences -is [Array])) {
            throw [FormatException]::new(
                'informational_occurrences must be an array.')
        }
        for (
            $index = 0;
            $index -lt $Document.informational_occurrences.Count;
            $index++
        ) {
            $occurrence = $Document.informational_occurrences[$index]
            Assert-ExactJsonProperties $occurrence ([string[]]@(
                'term', 'path', 'line'
            )) "informational_occurrences[$index]"
            if (-not ($occurrence.term -is [string]) -or
                [string]::IsNullOrWhiteSpace($occurrence.term)) {
                throw [FormatException]::new(
                    'Occurrence term must be nonempty.')
            }
            Assert-ProjectRelativeJsonPath `
                $occurrence.path `
                'occurrence.path'
            Assert-JsonInteger `
                $occurrence.line `
                'occurrence.line' `
                -Positive
        }
        if ([long]$Document.blocking_count -ne $computed) {
            throw [FormatException]::new(
                'Canon blocking_count is inconsistent.')
        }
        return [pscustomobject]@{ Passes = ($computed -eq 0) }
    }

    $expectedTool = @{
        'portrait-json' = 'missing_portraits'
        'overlap-json' = 'narration_overlap'
        'show-before-json' = 'show_before_prevention'
        'nested-quote-json' = 'nested_quotes'
    }[$Postcondition]
    if ([string]::IsNullOrWhiteSpace($expectedTool)) {
        throw [FormatException]::new(
            "Unknown structured postcondition '$Postcondition'.")
    }

    Assert-ExactJsonProperties $Document ([string[]]@(
        'schema_version',
        'tool',
        'scanned_files',
        'blocking_count',
        'findings'
    )) 'scanner document'
    Assert-JsonInteger $Document.schema_version 'schema_version'
    if ([long]$Document.schema_version -ne 1 -or
        -not ($Document.tool -is [string]) -or
        $Document.tool -cne $expectedTool) {
        throw [FormatException]::new('Scanner schema/tool is wrong.')
    }
    if (-not ($Document.scanned_files -is [Array])) {
        throw [FormatException]::new('scanned_files must be an array.')
    }
    foreach ($scanned in $Document.scanned_files) {
        Assert-ProjectRelativeJsonPath $scanned 'scanned_files entry'
    }
    if (-not ($Document.scanned_files -ccontains
        'game/governance_winter_interlude.rpy')) {
        throw [FormatException]::new(
            'Scanner did not prove the winter target was scanned.')
    }
    if (-not ($Document.findings -is [Array])) {
        throw [FormatException]::new('findings must be an array.')
    }
    for ($index = 0; $index -lt $Document.findings.Count; $index++) {
        Assert-JsonFinding `
            $Document.findings[$index] `
            "findings[$index]"
    }
    Assert-JsonInteger $Document.blocking_count 'blocking_count'
    if ([long]$Document.blocking_count -ne $Document.findings.Count) {
        throw [FormatException]::new(
            'Scanner blocking_count is inconsistent.')
    }
    [pscustomobject]@{
        Passes = ($Document.findings.Count -eq 0)
    }
}
```

No `Invoke-GateStep` edit is needed in this loop. Its already-tested order is:
launch validation; timeout; process tree; then, for JSON steps, missing-output
precedence, document validation, semantic postcondition, and finally a nonzero
exit for otherwise-passing JSON.

- [ ] **Step 12: Run the scanner loop and the complete public gate GREEN**

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateScannerEvidenceTests -v
if ($LASTEXITCODE -ne 0) { throw 'Scanner schema/precedence slice failed.' }

python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateCapabilityTests.test_valid_batch_capability_uses_full_stem_and_passes `
  Tools.test_winter_interlude_gate.WinterInterludeGateCapabilityTests.test_gate_owned_reservation_blocks_concurrent_path_writers `
  Tools.test_winter_interlude_gate.WinterInterludeGateCapabilityTests.test_capability_false_flag_beats_nonzero_exit `
  Tools.test_winter_interlude_gate.WinterInterludeGateNarrativeManifestTests.test_precreated_next_output_stops_before_next_child `
  Tools.test_winter_interlude_gate.WinterInterludeGateNarrativeManifestTests.test_batch_and_final_manifests_are_exact `
  Tools.test_winter_interlude_gate.WinterInterludeGateScannerEvidenceTests.test_present_malformed_beats_nonzero_and_valid_pass_uses_process `
  -v
if ($LASTEXITCODE -ne 0) { throw 'Structured reservation focused evidence failed.' }

python -m unittest Tools.test_winter_interlude_gate -v 2>&1 |
  Tee-Object -FilePath .superpowers/sdd/task-7-5-full-84.txt
if ($LASTEXITCODE -ne 0) { throw 'Complete public executable gate failed.' }

$gateHash = (Get-FileHash -Algorithm SHA256 -LiteralPath `
  Tools/Run-WinterInterludeGate.ps1).Hash
$testsHash = (Get-FileHash -Algorithm SHA256 -LiteralPath `
  Tools/test_winter_interlude_gate.py).Hash
if ($gateHash -cne '04F7B894EE977127E9F439E71B42A238E9578F5D64D27A6D80B07304884C5BCA' -or
    $testsHash -cne '1675D37996C999BADFF6D99D5542EA728BC239255DED74E3151038467F3A9980') {
    throw "Task 5 candidate drifted: gate=$gateHash tests=$testsHash"
}
```

Expected: all commands exit 0 and print `OK`; ScannerEvidence reports `Ran 7
tests`, the cross-loop structured ownership focus reports `Ran 6 tests`, and
the complete module reports `Ran 84 tests`. Task 5 adds exactly 25 tests: 13 in
Loop A, 5 in Loop B, and 7 in Loop C. The complete command includes the real runner root-plus-descendant
outer-watchdog case from Task 4, so budget at least
`RenPyTimeoutSeconds + 60` seconds. After it returns, that test has already
proved both recorded PIDs are gone. The two hashes lock the exact reviewed
84-test candidate; any later Tool edit invalidates this evidence and requires a
fresh full run plus fresh Spec/Standards review.

- [ ] **Step 13: Amend the in-progress executable-gate implementation commit**

```powershell
git add -- Tools/Run-WinterInterludeGate.ps1 Tools/test_winter_interlude_gate.py
if ($LASTEXITCODE -ne 0) { throw 'Could not stage final Narrative evidence.' }
$staged = @(git diff --cached --name-only)
if ($LASTEXITCODE -ne 0) { throw 'Could not inspect final staged scope.' }
if ($staged.Count -ne 2 -or
    $staged -notcontains 'Tools/Run-WinterInterludeGate.ps1' -or
    $staged -notcontains 'Tools/test_winter_interlude_gate.py') {
    throw "Unexpected final staged scope: $($staged -join ', ')"
}
git diff --cached --check
if ($LASTEXITCODE -ne 0) { throw 'Final staged diff check failed.' }
git commit --amend --no-edit
if ($LASTEXITCODE -ne 0) { throw 'Could not amend final Narrative evidence.' }
```

---

### Task 6: Retire the Markdown interpreter and migrate the tracked plan

**Files:**
- Modify: `Tools/test_governance_winter_interlude.py:7,96-455,2595-2893`
- Modify: `Tools/test_winter_interlude_gate.py`
- Modify: `docs/superpowers/plans/2026-08-08-governance-winter-interlude.md:1352-1516`

**Interfaces:**
- Consumes the already-GREEN public Structural/Narrative gate.
- Produces literal discoverability only; no test interprets Markdown or PowerShell control flow.
- Migrates the already-GREEN strict JSON, gate-owned structured-output handle,
  reservation lifetime, and portrait exact-direct-parent contracts into the
  blocked Task 8 hand-off. This is ownership/discoverability only and does not
  authorize a Task 8 implementation edit.

#### Loop A: remove the handwritten Markdown/PowerShell interpreter

- [ ] **Step 1: Add only the parser-retirement RED test**

Append this class before the module's final `if __name__ == "__main__"` block:

```python
class WinterInterludeGateMigrationTests(unittest.TestCase):
    def test_old_markdown_execution_parser_is_removed(self):
        source = (
            ROOT / "Tools" / "test_governance_winter_interlude.py"
        ).read_text(encoding="utf-8")
        forbidden = (
            "_active_markdown",
            "_task_plan_section",
            "_comment_task_plan_body",
            "_task_plan_git_add_paths",
            "_task_plan_suite_command",
            "_powershell_brace_delta",
            "_task_plan_foreach_block",
            "_task_plan_foreach_suites",
            "_validate_task7_suite_save_assignment",
            "_validate_suite_options",
            "_validate_task7_route_plan",
            "_validate_task8_route_plan",
            "test_task7_route_commands_have_executable_timeouts",
            "test_task8_route_command_is_executable_and_has_unique_timeout",
        )
        self.assertEqual([name for name in forbidden if name in source], [])
```

Run:

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateMigrationTests.test_old_markdown_execution_parser_is_removed `
  -v 2>&1 | Tee-Object -FilePath .superpowers/sdd/task-7-5-parser-retirement-red.txt
if ($LASTEXITCODE -eq 0) { throw 'Parser-retirement RED unexpectedly passed.' }
```

Expected RED: `Ran 1 test`; the named method lists the still-present interpreter
helpers and parser-dependent tests, while every earlier public-gate class
remains at its prior GREEN.

- [ ] **Step 2: Delete only the exact obsolete parser surface**

In `Tools/test_governance_winter_interlude.py`, delete `import shlex`; delete the complete contiguous block from `def _active_markdown` through the end of `_validate_task8_route_plan`; delete the complete methods `test_task8_plan_authorizes_atomic_visible_semantic_migration`, `test_task7_route_commands_have_executable_timeouts`, and `test_task8_route_command_is_executable_and_has_unique_timeout`. Do not change `TASK7_VISIBLE_SEMANTIC_CONTRACT`, `TASK8_VISIBLE_SEMANTIC_MIGRATION_CONTRACT`, the six opposite-semantic mutations, or any production/runtime assertion.

- [ ] **Step 3: Run the focused parser-retirement GREEN**

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateMigrationTests.test_old_markdown_execution_parser_is_removed `
  -v
if ($LASTEXITCODE -ne 0) { throw 'Parser-retirement GREEN failed.' }
python -m unittest Tools.test_governance_winter_interlude -v
if ($LASTEXITCODE -ne 0) { throw 'Story contracts failed after parser retirement.' }
```

Expected GREEN: the named retirement method reports `Ran 1 test`; the
governance module reports `Ran 48 tests`; all remaining story/state/runtime
contracts pass with no Markdown or PowerShell interpreter surface.

#### Loop B: add literal gate discoverability and exact Task 8 ownership

- [ ] **Step 4: Add only the tracked-plan migration RED tests**

Insert this method at the start of `WinterInterludeGateMigrationTests`:

```python
    def test_plan_discovers_public_gate_calls_without_claiming_markdown_execution(self):
        plan = PLAN.read_text(encoding="utf-8")
        forbidden_legacy_execution = (
            (
                "foreach ($suite in @("
                "'test_winter_interlude_state',"
                "'test_winter_interlude_routing',"
                "'test_winter_interlude_ending_invariance',"
                "'test_winter_interlude_route_matrix',"
                "'test_winter_interlude_mid_save')) {"
            ),
            (
                "& Tools/Run-RenPySuite.ps1 -ProjectRoot "
                "(Get-Location).Path -SaveDir $task8RouteSaveDir "
                "-Mode Suite -Suite test_winter_interlude_route_matrix "
                "-Expect PASSED -TimeoutSeconds 300"
            ),
            (
                "### Task 8: Transplant approved legacy passages and "
                "generate final Chinese prose in scene-isolated Opus sessions"
            ),
            "- [ ] **Step 1: Create the content ledger before generating prose**",
            (
                "- [ ] **Step 2: Transplant the ledger-selected legacy "
                "passages verbatim**"
            ),
            (
                "- [ ] **Step 3: Use the invoke-opus-4-6 skill with a fresh "
                "Claude Code session for every scene**"
            ),
            (
                "- [ ] **Step 4: Integrate approved prose without changing "
                "structure**"
            ),
            (
                "- [ ] **Step 5: Enforce path-length and reuse ratios from "
                "actual target text**"
            ),
            (
                "- [ ] **Step 6: Run narrative gates after every approved "
                "scene integration**"
            ),
            "- [ ] **Step 7: Refresh and verify the font**",
            "- [ ] **Step 8: Commit the approved interlude prose**",
            (
                "git add game/governance_winter_interlude.rpy game/msyh.ttf "
                "docs/development/winter-interlude-content-ledger.md "
                "Tools/scan_nested_quotes.py "
                "Tools/test_governance_winter_interlude.py game/test_game.rpy"
            ),
        )
        self.assertEqual(
            [text for text in forbidden_legacy_execution if text in plan],
            [],
        )
        for required_once in (
            (
                "### Task 8: Author and approve a dedicated "
                "winter-interlude narrative delivery plan"
            ),
            "**Status:** blocked on a separate implementation plan.",
        ):
            with self.subTest(required_once=required_once):
                self.assertEqual(plan.count(required_once), 1)
        self.assertEqual(plan.count("-File $winterGate -Gate Structural"), 1)
        self.assertEqual(
            plan.count("-File $winterGate -Gate Narrative -NarrativePhase Batch"),
            1,
        )
        self.assertEqual(
            plan.count("-File $winterGate -Gate Narrative -NarrativePhase Final"),
            1,
        )
        self.assertIn(
            "Markdown is documentation; executable proof comes from "
            "Tools/test_winter_interlude_gate.py",
            plan,
        )
        self.assertEqual(
            plan.count(
                "docs/superpowers/plans/"
                "2026-08-09-winter-interlude-narrative-delivery.md"
            ),
            1,
        )
        self.assertIn(
            "Do not implement Task 8 from this umbrella plan.",
            plan,
        )
        for producer in (
            "Tools/check_winter_narrative_capabilities.py",
            "Tools/scan_canon.py",
            "scan_missing_portraits.py",
            "scan_narration_overlap.py",
            "Tools/scan_show_before_prevention.py",
            "Tools/scan_nested_quotes.py",
        ):
            with self.subTest(producer=producer):
                self.assertIn(producer, plan)
        sole_authority = (
            "`WINTER_GATE_STRUCTURED_OUTPUT_HANDLE` is the sole "
            "gate-mode write authority"
        )
        self.assertEqual(plan.count(sole_authority), 1)
        for contract in (
            "must not open, create, replace, reopen, or fall back to "
            "`--output` by path",
            "Standalone mode exists only when the handle environment "
            "variable is absent; it uses `CREATE_NEW` and never overwrites.",
            "1,048,576 UTF-8 bytes, 1,048,576 UTF-16 characters, depth "
            "64, and number-token length 128",
            "decoded object keys are unique by `Ordinal`",
            "`strict_json:<reason> at UTF-16 offset N.` before "
            "`ConvertFrom-Json`",
            "exactly one registered direct parent",
            "prefix/`StartsWith` matching is forbidden",
            "`--output-dir` remains forbidden",
            "handle-linkage, path-reopen, and path-fallback mutation",
        ):
            with self.subTest(contract=contract):
                self.assertIn(contract, plan)
```

Add this exact constant beside
`TASK8_VISIBLE_SEMANTIC_MIGRATION_CONTRACT`, then add the complete lightweight
method to the existing story-contract test class at the former location of
`test_task8_plan_authorizes_atomic_visible_semantic_migration`:

```python
TASK8_MACHINE_JSON_GATE_CONTRACT = """
`WINTER_GATE_STRUCTURED_OUTPUT_HANDLE` is the sole gate-mode write authority for all six machine-JSON producers. In gate mode a producer must not open, create, replace, reopen, or fall back to `--output` by path. Standalone mode exists only when the handle environment variable is absent; it uses `CREATE_NEW` and never overwrites. Gate evidence is limited to 1,048,576 UTF-8 bytes, 1,048,576 UTF-16 characters, depth 64, and number-token length 128; it uses RFC 8259 lexemes, strings, and surrogate pairs, decoded object keys are unique by `Ordinal`, and it reports `strict_json:<reason> at UTF-16 offset N.` before `ConvertFrom-Json`. Portrait output requires exactly one registered direct parent using `OrdinalIgnoreCase`; prefix/`StartsWith` matching is forbidden and `--output-dir` remains forbidden. The dedicated plan must include a per-producer handle-linkage, path-reopen, and path-fallback mutation.
""".strip()
```

Then add the method:

```python
    def test_task8_plan_blocks_until_separate_atomic_delivery_plan(self):
        plan = TRACKED_PLAN.read_text(encoding="utf-8")
        self.assertEqual(
            plan.count(TASK8_VISIBLE_SEMANTIC_MIGRATION_CONTRACT),
            1,
        )
        self.assertEqual(
            plan.count(TASK8_MACHINE_JSON_GATE_CONTRACT),
            1,
        )
        for required_path in (
            "game/governance_winter_interlude.rpy",
            "Tools/test_governance_winter_interlude.py",
            "game/test_game.rpy",
            "Tools/Run-WinterInterludeGate.ps1",
            "Tools/check_winter_narrative_capabilities.py",
            "Tools/scan_canon.py",
            "scan_missing_portraits.py",
            "scan_narration_overlap.py",
            "Tools/scan_show_before_prevention.py",
            "Tools/scan_nested_quotes.py",
            (
                "docs/superpowers/plans/"
                "2026-08-09-winter-interlude-narrative-delivery.md"
            ),
        ):
            with self.subTest(required_path=required_path):
                self.assertIn(required_path, plan)
```

Run the two new methods before editing the tracked plan:

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateMigrationTests.test_plan_discovers_public_gate_calls_without_claiming_markdown_execution `
  Tools.test_governance_winter_interlude.WinterStoryGraphContractTests.test_task8_plan_blocks_until_separate_atomic_delivery_plan `
  -v 2>&1 | Tee-Object -FilePath .superpowers/sdd/task-7-5-plan-migration-red.txt
if ($LASTEXITCODE -eq 0) { throw 'Tracked-plan migration RED unexpectedly passed.' }
```

Expected RED: `Ran 2 tests`; both named methods fail only because the tracked
plan still contains the exact legacy Task 7 foreach, legacy Task 8 route
command, heading, eight executable Step headings, and shipping `git add`, and
lacks the public-gate discovery boundary, the exact-once new Task 8
heading/status, the dedicated Task 8 delivery-plan boundary, and the
six-producer inherited-handle, no-path-fallback, strict-profile,
portrait-parent, and per-producer mutation contract. No Markdown or PowerShell
parser is restored.

- [ ] **Step 5: Apply the exact tracked-plan migration**

Replace Task 7 Step 9's entire PowerShell fence with:

```powershell
$gateHost = Join-Path ([Environment]::SystemDirectory) 'WindowsPowerShell\v1.0\powershell.exe'
$winterGate = (Resolve-Path -LiteralPath Tools/Run-WinterInterludeGate.ps1 -ErrorAction Stop).Path
& $gateHost -NoLogo -NoProfile -NonInteractive -ExecutionPolicy Bypass -File $winterGate -Gate Structural -ProjectRoot (Get-Location).Path
if ($LASTEXITCODE -ne 0) { throw 'Winter Structural gate failed.' }
```

Insert after Task 7 and before Task 8:

```markdown
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
```

Replace Task 8 in its entirety, from the `### Task 8:` heading through its asset-audit paragraph and separator before Task 9, with exactly:

````markdown
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
````

- [ ] **Step 6: Run the focused tracked-plan GREEN and combined regression**

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateMigrationTests.test_plan_discovers_public_gate_calls_without_claiming_markdown_execution `
  Tools.test_governance_winter_interlude.WinterStoryGraphContractTests.test_task8_plan_blocks_until_separate_atomic_delivery_plan `
  -v
if ($LASTEXITCODE -ne 0) { throw 'Tracked-plan migration GREEN failed.' }
python -m unittest Tools.test_winter_interlude_gate.WinterInterludeGateMigrationTests -v
if ($LASTEXITCODE -ne 0) { throw 'Public gate migration regression failed.' }
python -m unittest Tools.test_governance_winter_interlude -v
if ($LASTEXITCODE -ne 0) { throw 'Story contract migration regression failed.' }
python -m unittest Tools.test_winter_interlude_gate -v
if ($LASTEXITCODE -ne 0) { throw 'Public gate full migration regression failed.' }
```

Expected GREEN: the focused pair and complete MigrationTests class each report
`Ran 2 tests`; the governance module reports `Ran 49 tests`; the full public
gate module reports `Ran 86 tests`. Literal gate discoverability, the absence of
all twelve forbidden legacy execution strings, the exact-once dedicated-plan stop
boundary, the six-producer inherited-handle/no-path-fallback/strict-profile/
portrait-parent contract, and both lightweight ownership assertions pass; the
story module retains only narrative/state contracts and no Markdown execution
parser. Task 8 remains deliberately non-executable until its separate complete
plan, including every per-producer mutation, receives both READY verdicts.

- [ ] **Step 7: Amend the single Task 7.5 commit**

```powershell
git add -- Tools/Run-WinterInterludeGate.ps1 Tools/test_winter_interlude_gate.py Tools/test_governance_winter_interlude.py docs/superpowers/plans/2026-08-08-governance-winter-interlude.md
if ($LASTEXITCODE -ne 0) { throw 'Migration staging failed.' }
$migrationStaged = @(git diff --cached --name-only)
if ($LASTEXITCODE -ne 0) { throw 'Could not inspect migration staging.' }
$allowedMigrationPaths = @(
  'Tools/Run-WinterInterludeGate.ps1',
  'Tools/test_winter_interlude_gate.py',
  'Tools/test_governance_winter_interlude.py',
  'docs/superpowers/plans/2026-08-08-governance-winter-interlude.md'
)
if ($migrationStaged.Count -eq 0 -or
    @($migrationStaged | Where-Object { $_ -notin $allowedMigrationPaths }).Count -ne 0) {
  throw "Unexpected migration staged paths: $($migrationStaged -join ', ')"
}
git diff --cached --check
if ($LASTEXITCODE -ne 0) { throw 'Migration staged diff failed whitespace validation.' }
git commit --amend --no-edit
if ($LASTEXITCODE -ne 0) { throw 'Migration amend failed.' }
```

Expected: the growing Task 7.5 commit still has the exact subject and now contains the exact four allowed files.

---

### Task 7: Bind final evidence, review the exact range, and close the task

**Files:**
- Verify; modify only for a review-backed RED-to-GREEN fix: `Tools/Run-WinterInterludeGate.ps1`
- Verify; modify only for a review-backed RED-to-GREEN fix: `Tools/test_winter_interlude_gate.py`
- Verify; modify only for a review-backed RED-to-GREEN fix: `Tools/test_governance_winter_interlude.py`
- Verify; modify only for a review-backed RED-to-GREEN fix: `docs/superpowers/plans/2026-08-08-governance-winter-interlude.md`

**Interfaces:**
- Consumes the single amended Task 7.5 commit and the immutable `task75Start` evidence.
- Produces final, committed public-gate evidence plus independent Spec and Standards C0/I0 decisions.

- [ ] **Step 1: Run complete committed discovery and the exact-scope audit**

```powershell
$finalEvidenceSignals = [string[]]@(
  '.superpowers/sdd/task-7-5-final-commit.txt',
  '.superpowers/sdd/task-7-5-final-full-python.json',
  '.superpowers/sdd/task-7-5-final-structural-root.txt',
  '.superpowers/sdd/task-7-5-final-narrative-roots.json',
  '.superpowers/sdd/task-7-5-final-review-inputs.json',
  '.superpowers/sdd/task-7-5-final-spec-review.json',
  '.superpowers/sdd/task-7-5-final-standards-review.json'
)
foreach ($signal in $finalEvidenceSignals) {
  Remove-Item -LiteralPath $signal -Force -ErrorAction SilentlyContinue
}
$designBase = 'ed262771e740b2e502d30921ed92e1de1deb54b6'
$task75Start = (
  Get-Content -Raw -LiteralPath .superpowers/sdd/task-7-5-start.txt -ErrorAction Stop
).Trim()
if ($task75Start -notmatch '^[0-9a-f]{40}$') {
  throw "Invalid Task 7.5 start evidence: $task75Start"
}
$finalCommit = (git rev-parse HEAD).Trim()
if ($LASTEXITCODE -ne 0 -or $finalCommit -notmatch '^[0-9a-f]{40}$') {
  throw 'Could not record final Task 7.5 commit.'
}
$finalStatus = @(git status --short)
if ($LASTEXITCODE -ne 0 -or $finalStatus.Count -ne 0) {
  throw 'Final Task 7.5 tree is not clean.'
}

$planParent = (git rev-parse "$task75Start^").Trim()
if ($LASTEXITCODE -ne 0 -or $planParent -ne $designBase) {
  throw 'The recorded plan commit is not the direct child of the design base.'
}
$implementationParent = (git rev-parse "$finalCommit^").Trim()
if ($LASTEXITCODE -ne 0 -or $implementationParent -ne $task75Start) {
  throw 'The implementation commit is not the direct child of the recorded plan commit.'
}
$planCount = (git rev-list --count "$designBase..$task75Start").Trim()
if ($LASTEXITCODE -ne 0 -or $planCount -ne '1') {
  throw "Expected exactly one plan commit; observed $planCount."
}
$implementationCount = (git rev-list --count "$task75Start..$finalCommit").Trim()
if ($LASTEXITCODE -ne 0 -or $implementationCount -ne '1') {
  throw "Expected exactly one Task 7.5 implementation commit; observed $implementationCount."
}
$twoCommitCount = (git rev-list --count "$designBase..$finalCommit").Trim()
if ($LASTEXITCODE -ne 0 -or $twoCommitCount -ne '2') {
  throw "Expected exactly two commits after the design base; observed $twoCommitCount."
}
$planSubject = (git show -s --format=%s $task75Start).Trim()
if ($LASTEXITCODE -ne 0 -or $planSubject -ne 'docs: plan winter interlude executable gates') {
  throw "Unexpected plan subject: $planSubject"
}
$implementationSubject = (git show -s --format=%s $finalCommit).Trim()
if ($LASTEXITCODE -ne 0 -or $implementationSubject -ne 'refactor: execute winter interlude gates from scripts') {
  throw "Unexpected Task 7.5 subject: $implementationSubject"
}

$preImplementationPaths = @(git diff --name-only "$designBase..$task75Start")
if ($LASTEXITCODE -ne 0) { throw 'Could not inspect the plan-only range.' }
if ($preImplementationPaths.Count -ne 1 -or
    $preImplementationPaths[0] -ne 'docs/superpowers/plans/2026-08-09-winter-interlude-executable-gates.md') {
  throw "Plan-only range is not exact: $($preImplementationPaths -join ', ')"
}
$finalPaths = @(git diff --name-only "$task75Start..$finalCommit")
if ($LASTEXITCODE -ne 0) { throw 'Could not inspect final Task 7.5 range.' }
$expectedFinalPaths = @(
  'Tools/Run-WinterInterludeGate.ps1',
  'Tools/test_winter_interlude_gate.py',
  'Tools/test_governance_winter_interlude.py',
  'docs/superpowers/plans/2026-08-08-governance-winter-interlude.md'
)
if (@(Compare-Object ($expectedFinalPaths | Sort-Object) ($finalPaths | Sort-Object)).Count -ne 0) {
  throw "Final Task 7.5 range is not exact: $($finalPaths -join ', ')"
}
git diff --check "$task75Start..$finalCommit"
if ($LASTEXITCODE -ne 0) { throw 'Complete Task 7.5 range failed whitespace validation.' }

$shippingTracked = @(git diff --name-only "$task75Start..$finalCommit" -- game old-game)
if ($LASTEXITCODE -ne 0 -or $shippingTracked.Count -ne 0) {
  throw "Task 7.5 changed game/old-game: $($shippingTracked -join ', ')"
}
$shippingUntracked = @(git ls-files --others --exclude-standard -- game old-game)
if ($LASTEXITCODE -ne 0 -or $shippingUntracked.Count -ne 0) {
  throw "Task 7.5 added untracked game/old-game paths: $($shippingUntracked -join ', ')"
}
$startFont = (git rev-parse "$task75Start`:game/msyh.ttf").Trim()
if ($LASTEXITCODE -ne 0) { throw 'Could not read starting font blob.' }
$finalFont = (git rev-parse "$finalCommit`:game/msyh.ttf").Trim()
if ($LASTEXITCODE -ne 0) { throw 'Could not read final font blob.' }
if ($startFont -ne $finalFont) { throw 'Task 7.5 changed game/msyh.ttf.' }

$pythonCommand = Get-Command python.exe -CommandType Application -ErrorAction Stop |
  Select-Object -First 1
if ($null -eq $pythonCommand -or
    [string]::IsNullOrWhiteSpace([string]$pythonCommand.Source)) {
  throw 'python.exe did not resolve to an application.'
}
$discoveryCommand = 'python -m unittest discover -s Tools -p "test_*.py" -v'
$discoveryAttempt = [guid]::NewGuid().ToString('N')
$fullDiscoveryLog = '.superpowers/sdd/task-7-5-final-full-python-{0}-{1}.txt' -f `
  $finalCommit.Substring(0, 12), $discoveryAttempt
$fullDiscoveryStdout = '.superpowers/sdd/task-7-5-final-full-python-{0}-{1}.stdout.txt' -f `
  $finalCommit.Substring(0, 12), $discoveryAttempt
$fullDiscoveryStderr = '.superpowers/sdd/task-7-5-final-full-python-{0}-{1}.stderr.txt' -f `
  $finalCommit.Substring(0, 12), $discoveryAttempt
$fullDiscoveryRecordPath = '.superpowers/sdd/task-7-5-final-full-python.json'
$discoveryStartedUtc = [DateTime]::UtcNow.ToString('o')
$discoveryWatch = [Diagnostics.Stopwatch]::StartNew()
$discoveryProcess = Start-Process `
  -FilePath $pythonCommand.Source `
  -ArgumentList ([string[]]@(
    '-m', 'unittest', 'discover', '-s', 'Tools', '-p', 'test_*.py', '-v'
  )) `
  -WorkingDirectory (Get-Location).Path `
  -WindowStyle Hidden `
  -RedirectStandardOutput $fullDiscoveryStdout `
  -RedirectStandardError $fullDiscoveryStderr `
  -Wait `
  -PassThru
$discoveryExit = [int]$discoveryProcess.ExitCode
$discoveryWatch.Stop()
$discoveryEndedUtc = [DateTime]::UtcNow.ToString('o')
$discoveryStdoutText = [string](
  Get-Content -Raw -LiteralPath $fullDiscoveryStdout -ErrorAction Stop
)
$discoveryStderrText = [string](
  Get-Content -Raw -LiteralPath $fullDiscoveryStderr -ErrorAction Stop
)
$discoverySeparator = ''
if ($discoveryStdoutText.Length -gt 0 -and
    $discoveryStderrText.Length -gt 0 -and
    -not $discoveryStdoutText.EndsWith("`n", [StringComparison]::Ordinal)) {
  $discoverySeparator = [Environment]::NewLine
}
$fullDiscoveryText =
  $discoveryStdoutText + $discoverySeparator + $discoveryStderrText
[IO.File]::WriteAllText(
  (Join-Path (Get-Location).Path $fullDiscoveryLog),
  $fullDiscoveryText,
  (New-Object Text.UTF8Encoding($false))
)
Get-Content -LiteralPath $fullDiscoveryLog -ErrorAction Stop
$fullDiscoveryLogHash = (
  Get-FileHash -Algorithm SHA256 -LiteralPath $fullDiscoveryLog -ErrorAction Stop
).Hash
$ranMatches = [regex]::Matches(
  $fullDiscoveryText,
  '(?m)^Ran ([0-9]+) tests in [0-9]+(?:\.[0-9]+)?s\r?$'
)
$discoveredTestCount = 0
$ranLineValid = ($ranMatches.Count -eq 1)
if ($ranLineValid) {
  $ranLineValid = [int]::TryParse(
      $ranMatches[0].Groups[1].Value,
      [Globalization.NumberStyles]::None,
      [Globalization.CultureInfo]::InvariantCulture,
      [ref]$discoveredTestCount
    )
}
$ranLineValid = ($ranLineValid -and $discoveredTestCount -ge 339)
$discoveryRecord = [pscustomobject][ordered]@{
  schema_version = 1
  head_commit = $finalCommit
  command = $discoveryCommand
  started_utc = $discoveryStartedUtc
  ended_utc = $discoveryEndedUtc
  elapsed_milliseconds = [long]$discoveryWatch.ElapsedMilliseconds
  exit_code = [int]$discoveryExit
  status = if ($discoveryExit -eq 0) { 'passed' } else { 'failed' }
  discovered_test_count = [int]$discoveredTestCount
  log_path = $fullDiscoveryLog
  log_sha256 = $fullDiscoveryLogHash
}
$discoveryRecord |
  ConvertTo-Json -Depth 4 |
  Set-Content -LiteralPath $fullDiscoveryRecordPath -Encoding utf8 -ErrorAction Stop
$recordedDiscovery = Get-Content -Raw -LiteralPath $fullDiscoveryRecordPath `
  -ErrorAction Stop | ConvertFrom-Json
if ($recordedDiscovery.head_commit -cne $finalCommit -or
    $recordedDiscovery.command -cne $discoveryCommand -or
    [int]$recordedDiscovery.exit_code -ne $discoveryExit -or
    [int]$recordedDiscovery.discovered_test_count -ne $discoveredTestCount -or
    [string]$recordedDiscovery.log_path -cne $fullDiscoveryLog -or
    [string]$recordedDiscovery.log_sha256 -cne $fullDiscoveryLogHash) {
  throw 'Full-discovery evidence did not round-trip.'
}
if (-not $ranLineValid) {
  throw 'Full discovery must contain exactly one valid Ran N tests line with N >= 339.'
}
if ($discoveryExit -ne 0) {
  throw "Full Python discovery failed; output: $fullDiscoveryLog"
}
$postTestHead = (git rev-parse HEAD).Trim()
if ($LASTEXITCODE -ne 0 -or $postTestHead -ne $finalCommit) {
  throw 'Full discovery changed HEAD.'
}
$postTestStatus = @(git status --short)
if ($LASTEXITCODE -ne 0 -or $postTestStatus.Count -ne 0) {
  throw "Full discovery dirtied the tree: $($postTestStatus -join ', ')"
}
$finalCommitEvidence = '.superpowers/sdd/task-7-5-final-commit.txt'
$finalCommit | Set-Content -LiteralPath $finalCommitEvidence -Encoding ascii -ErrorAction Stop
$recordedFinalCommit = (
  Get-Content -Raw -LiteralPath $finalCommitEvidence -ErrorAction Stop
).Trim()
if ($recordedFinalCommit -ne $finalCommit) {
  throw 'Final Task 7.5 commit evidence did not round-trip.'
}
```

Expected: full discovery passes without dirtying the tree; the fixed design has exactly one plan child and one implementation grandchild with exact subjects; the implementation range is exactly four files; `game`/`old-game` are absent; the font blobs are identical; the unique raw discovery log contains exactly one `Ran N tests` line with `N >= 339`; that integer and the log SHA-256 round-trip through committed-HEAD JSON metadata; and only then does the final-commit pointer appear. The post-review 87-test gate module alone can take more than ten minutes on this machine, so run this fence in a resumable session and do not treat a ten-minute silent interval as failure.

- [ ] **Step 2: Run the committed real Structural gate**

```powershell
$finalCommit = (
  Get-Content -Raw -LiteralPath .superpowers/sdd/task-7-5-final-commit.txt -ErrorAction Stop
).Trim()
$currentHead = (git rev-parse HEAD).Trim()
if ($LASTEXITCODE -ne 0 -or $currentHead -ne $finalCommit) {
  throw 'Structural proof is not starting from the recorded final HEAD.'
}
$structuralRootEvidence = '.superpowers/sdd/task-7-5-final-structural-root.txt'
foreach ($signal in [string[]]@(
  $structuralRootEvidence,
  '.superpowers/sdd/task-7-5-final-narrative-roots.json',
  '.superpowers/sdd/task-7-5-final-review-inputs.json',
  '.superpowers/sdd/task-7-5-final-spec-review.json',
  '.superpowers/sdd/task-7-5-final-standards-review.json'
)) {
  Remove-Item -LiteralPath $signal -Force -ErrorAction SilentlyContinue
}
$assertJsonInteger = {
  param($Value, [long]$Minimum, [long]$Maximum, [string]$Label)
  if (($Value -isnot [int]) -and ($Value -isnot [long])) {
    throw "$Label must be a JSON Int32 or Int64."
  }
  $number = [long]$Value
  if ($number -lt $Minimum -or $number -gt $Maximum) {
    throw "$Label is outside [$Minimum, $Maximum]."
  }
}
$assertJsonBoolean = {
  param($Value, [bool]$Expected, [string]$Label)
  if ($Value -isnot [bool] -or [bool]$Value -ne $Expected) {
    throw "$Label must be the JSON boolean $Expected."
  }
}
$assertRfc3339Utc = {
  param($Value, [string]$Label)
  $parsed = [DateTime]::MinValue
  if ($Value -isnot [string] -or
      [string]$Value -cnotmatch '^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{7}Z$' -or
      -not [DateTime]::TryParseExact(
        [string]$Value,
        'o',
        [Globalization.CultureInfo]::InvariantCulture,
        [Globalization.DateTimeStyles]::RoundtripKind,
        [ref]$parsed
      ) -or
      $parsed.Kind -ne [DateTimeKind]::Utc) {
    throw "$Label must be an RFC3339 UTC round-trip timestamp."
  }
}
$assertScalarString = {
  param($Value, [string]$Label)
  if ($Value -isnot [string]) {
    throw "$Label must be a scalar JSON string."
  }
}
$assertJsonNull = {
  param($Value, [string]$Label)
  if ($null -ne $Value -or $Value -is [array]) {
    throw "$Label must be JSON null."
  }
}
$fullDiscoveryRecordPath = '.superpowers/sdd/task-7-5-final-full-python.json'
$discovery = Get-Content -Raw -LiteralPath $fullDiscoveryRecordPath `
  -ErrorAction Stop | ConvertFrom-Json
$expectedDiscoveryKeys = [string[]]@(
  'schema_version', 'head_commit', 'command', 'started_utc', 'ended_utc',
  'elapsed_milliseconds', 'exit_code', 'status', 'discovered_test_count',
  'log_path', 'log_sha256'
)
$actualDiscoveryKeys = [string[]]@($discovery.PSObject.Properties.Name)
& $assertScalarString $discovery.head_commit 'discovery.head_commit'
& $assertScalarString $discovery.command 'discovery.command'
& $assertScalarString $discovery.status 'discovery.status'
& $assertScalarString $discovery.log_path 'discovery.log_path'
& $assertScalarString $discovery.log_sha256 'discovery.log_sha256'
if (($actualDiscoveryKeys | Sort-Object) -join "`n" -cne
    (($expectedDiscoveryKeys | Sort-Object) -join "`n") -or
    $discovery.schema_version -ne 1 -or
    $discovery.head_commit -cne $finalCommit -or
    $discovery.command -cne 'python -m unittest discover -s Tools -p "test_*.py" -v' -or
    $discovery.status -cne 'passed' -or
    $discovery.exit_code -ne 0 -or
    $discovery.discovered_test_count -lt 339) {
  throw 'Structural proof is not bound to one successful final discovery.'
}
& $assertJsonInteger $discovery.schema_version 1 1 'discovery.schema_version'
& $assertJsonInteger $discovery.elapsed_milliseconds 0 ([long]::MaxValue) `
  'discovery.elapsed_milliseconds'
& $assertJsonInteger $discovery.exit_code 0 0 'discovery.exit_code'
& $assertJsonInteger $discovery.discovered_test_count 339 ([int]::MaxValue) `
  'discovery.discovered_test_count'
& $assertRfc3339Utc $discovery.started_utc 'discovery.started_utc'
& $assertRfc3339Utc $discovery.ended_utc 'discovery.ended_utc'
$discoveryLog = (Resolve-Path -LiteralPath ([string]$discovery.log_path) `
  -ErrorAction Stop).Path
$discoveryLogHash = (
  Get-FileHash -Algorithm SHA256 -LiteralPath $discoveryLog -ErrorAction Stop
).Hash
if ($discoveryLogHash -cne [string]$discovery.log_sha256) {
  throw 'Final-discovery log hash no longer matches its record.'
}
$discoveryText = Get-Content -Raw -LiteralPath $discoveryLog -ErrorAction Stop
$ranMatches = [regex]::Matches(
  $discoveryText,
  '(?m)^Ran ([0-9]+) tests in [0-9]+(?:\.[0-9]+)?s\r?$'
)
$logTestCount = 0
if ($ranMatches.Count -ne 1 -or
    -not [int]::TryParse(
      $ranMatches[0].Groups[1].Value,
      [Globalization.NumberStyles]::None,
      [Globalization.CultureInfo]::InvariantCulture,
      [ref]$logTestCount
    ) -or
    $logTestCount -lt 339 -or
    $logTestCount -ne [int]$discovery.discovered_test_count) {
  throw 'Final-discovery log does not contain its one recorded Ran N tests line.'
}
$projectRoot = (Resolve-Path -LiteralPath . -ErrorAction Stop).Path
$gateHost = Join-Path ([Environment]::SystemDirectory) 'WindowsPowerShell\v1.0\powershell.exe'
$winterGate = (Resolve-Path -LiteralPath Tools/Run-WinterInterludeGate.ps1 -ErrorAction Stop).Path
$finalStructuralRoot = Join-Path ([System.IO.Path]::GetTempPath()) `
  ("winter-final-structural-{0}" -f [guid]::NewGuid().ToString('N'))
$previousCommitEnvironment = $env:GIT_COMMIT
try {
  $env:GIT_COMMIT = $finalCommit
  & $gateHost -NoLogo -NoProfile -NonInteractive -ExecutionPolicy Bypass -File $winterGate `
    -Gate Structural `
    -ProjectRoot (Get-Location).Path `
    -RunRoot $finalStructuralRoot `
    -ToolTimeoutSeconds 300 `
    -RenPyTimeoutSeconds 300
  $structuralExit = $LASTEXITCODE
}
finally {
  if ($null -eq $previousCommitEnvironment) {
    Remove-Item Env:GIT_COMMIT -ErrorAction SilentlyContinue
  }
  else {
    $env:GIT_COMMIT = $previousCommitEnvironment
  }
}
if ($structuralExit -ne 0) {
  throw "Committed Structural gate failed; evidence: $finalStructuralRoot"
}
$structuralSummaryPath = Join-Path $finalStructuralRoot 'evidence\gate-summary.json'
$structuralSummary = Get-Content -Raw -LiteralPath $structuralSummaryPath -ErrorAction Stop | ConvertFrom-Json
$assertExactProperties = {
  param($Value, [string[]]$Expected, [string]$Label)
  if ($null -eq $Value -or $Value -is [array]) {
    throw "$Label must be exactly one object."
  }
  $actual = [string[]]@($Value.PSObject.Properties.Name | Sort-Object)
  $wanted = [string[]]@($Expected | Sort-Object)
  if ($actual.Count -ne $wanted.Count -or
      ($actual -join "`n") -cne ($wanted -join "`n")) {
    throw "$Label property set is not exact: $($actual -join ', ')"
  }
}
$assertExactStrings = {
  param($Actual, [string[]]$Expected, [string]$Label)
  if ($Actual -isnot [array]) {
    throw "$Label must be a JSON array."
  }
  $items = @($Actual)
  if ($items.Count -ne $Expected.Count) {
    throw "$Label count is $($items.Count), expected $($Expected.Count)."
  }
  for ($itemIndex = 0; $itemIndex -lt $Expected.Count; $itemIndex++) {
    if ($items[$itemIndex] -isnot [string]) {
      throw "$Label item at index $itemIndex must be a JSON string."
    }
    if ($items[$itemIndex] -cne $Expected[$itemIndex]) {
      throw "$Label differs at index $itemIndex."
    }
  }
}
$summaryKeys = [string[]]@(
  'schema_version', 'gate', 'narrative_phase', 'status', 'failure_kind',
  'error', 'started_utc', 'ended_utc', 'head_token', 'host',
  'project_root', 'run_root', 'steps'
)
$identityKeys = [string[]]@(
  'final_path', 'volume_serial_number', 'file_index'
)
$stepKeys = [string[]]@(
  'ordinal', 'name', 'kind', 'executable', 'arguments',
  'working_directory', 'process_started', 'process_id', 'started_utc',
  'ended_utc', 'exit_code', 'timed_out', 'tree_drained',
  'had_live_descendants_after_root_exit', 'elapsed_milliseconds',
  'stdout', 'stderr', 'result', 'postcondition',
  'manual_review_required', 'status', 'failure_kind', 'error'
)
$assertIdentity = {
  param($Identity, [string]$Label)
  & $assertExactProperties $Identity $identityKeys $Label
  if ($Identity.final_path -isnot [string] -or
      [string]::IsNullOrWhiteSpace([string]$Identity.final_path) -or
      -not [IO.Path]::IsPathRooted([string]$Identity.final_path)) {
    throw "$Label final_path must be a nonempty absolute string."
  }
  & $assertJsonInteger $Identity.volume_serial_number 0 ([long]::MaxValue) `
    "$Label.volume_serial_number"
  & $assertJsonInteger $Identity.file_index 0 ([long]::MaxValue) `
    "$Label.file_index"
}
& $assertExactProperties $structuralSummary $summaryKeys 'Structural summary'
& $assertExactProperties $structuralSummary.host `
  ([string[]]@('edition', 'version', 'executable')) 'Structural host'
& $assertIdentity $structuralSummary.host.executable `
  'Structural host executable identity'
& $assertIdentity $structuralSummary.project_root 'Structural ProjectRoot identity'
& $assertIdentity $structuralSummary.run_root 'Structural RunRoot identity'
& $assertJsonInteger $structuralSummary.schema_version 1 1 `
  'Structural schema_version'
& $assertRfc3339Utc $structuralSummary.started_utc 'Structural started_utc'
& $assertRfc3339Utc $structuralSummary.ended_utc 'Structural ended_utc'
& $assertScalarString $structuralSummary.gate 'Structural gate'
& $assertScalarString $structuralSummary.status 'Structural status'
& $assertScalarString $structuralSummary.head_token 'Structural head_token'
& $assertJsonNull $structuralSummary.narrative_phase `
  'Structural narrative_phase'
& $assertJsonNull $structuralSummary.failure_kind 'Structural failure_kind'
& $assertJsonNull $structuralSummary.error 'Structural error'
& $assertScalarString $structuralSummary.host.edition 'Structural host edition'
& $assertScalarString $structuralSummary.host.version 'Structural host version'
if ($structuralSummary.schema_version -ne 1 -or
    $structuralSummary.gate -cne 'Structural' -or
    $null -ne $structuralSummary.narrative_phase -or
    $structuralSummary.status -cne 'passed' -or
    $null -ne $structuralSummary.failure_kind -or
    $null -ne $structuralSummary.error -or
    $structuralSummary.head_token -cne $finalCommit.Substring(0, 12) -or
    $structuralSummary.steps -isnot [array]) {
  throw 'Committed Structural summary top-level contract is invalid.'
}
$resolvedStructuralRoot = (Resolve-Path -LiteralPath $finalStructuralRoot -ErrorAction Stop).Path
if (-not [string]::Equals(
      [string]$structuralSummary.project_root.final_path,
      $projectRoot,
      [StringComparison]::OrdinalIgnoreCase) -or
    -not [string]::Equals(
      [string]$structuralSummary.run_root.final_path,
      $resolvedStructuralRoot,
      [StringComparison]::OrdinalIgnoreCase)) {
  throw 'Committed Structural summary root identities do not match this invocation.'
}
foreach ($identity in @($structuralSummary.project_root, $structuralSummary.run_root)) {
  if ($null -eq $identity.volume_serial_number -or $null -eq $identity.file_index) {
    throw 'Committed Structural summary omitted an operating-system root identity.'
  }
}
$resolvedGateHost = (Resolve-Path -LiteralPath $gateHost -ErrorAction Stop).Path
if ($structuralSummary.host.edition -cne 'Desktop' -or
    $structuralSummary.host.version -isnot [string] -or
    -not ([string]$structuralSummary.host.version).StartsWith(
      '5.', [StringComparison]::Ordinal) -or
    -not [string]::Equals(
      [string]$structuralSummary.host.executable.final_path,
      $resolvedGateHost,
      [StringComparison]::OrdinalIgnoreCase)) {
  throw 'Committed Structural host contract is invalid.'
}
$pythonCommand = Get-Command python.exe -CommandType Application -ErrorAction Stop |
  Select-Object -First 1
$resolvedPython = (Resolve-Path -LiteralPath $pythonCommand.Source -ErrorAction Stop).Path
$runner = (Resolve-Path -LiteralPath Tools/Run-RenPySuite.ps1 -ErrorAction Stop).Path
$expectedSteps = New-Object 'System.Collections.Generic.List[object]'
[void]$expectedSteps.Add([pscustomobject]@{
  Name = 'source-contract'
  Kind = 'Python'
  Executable = $resolvedPython
  Postcondition = 'exit-zero'
  Arguments = [string[]]@(
    '-m', 'unittest', 'Tools.test_governance_winter_interlude', '-v'
  )
})
$structuralSuites = [string[]]@(
  'test_winter_interlude_state',
  'test_winter_interlude_routing',
  'test_winter_interlude_ending_invariance',
  'test_winter_interlude_route_matrix',
  'test_winter_interlude_mid_save'
)
for ($suiteIndex = 0; $suiteIndex -lt $structuralSuites.Count; $suiteIndex++) {
  $ordinal = $suiteIndex + 2
  $suite = $structuralSuites[$suiteIndex]
  [void]$expectedSteps.Add([pscustomobject]@{
    Name = $suite.Replace('_', '-')
    Kind = 'RenPySuite'
    Executable = $resolvedGateHost
    Postcondition = 'runner-passed'
    Arguments = [string[]]@(
      '-NoLogo', '-NoProfile', '-NonInteractive',
      '-ExecutionPolicy', 'Bypass', '-File', $runner,
      '-ProjectRoot', $projectRoot,
      '-SaveDir', (Join-Path $resolvedStructuralRoot `
        ('savedirs\{0:D2}-{1}' -f $ordinal, $suite)),
      '-Mode', 'Suite', '-Suite', $suite,
      '-Expect', 'PASSED',
      '-EvidenceDir', (Join-Path $resolvedStructuralRoot 'evidence\runner'),
      '-TimeoutSeconds', '300'
    )
  })
}
$headToken = $finalCommit.Substring(0, 12)
$actualSteps = @($structuralSummary.steps)
if ($actualSteps.Count -ne $expectedSteps.Count) {
  throw "Committed Structural step count is $($actualSteps.Count), expected 6."
}
for ($stepIndex = 0; $stepIndex -lt $expectedSteps.Count; $stepIndex++) {
  $step = $actualSteps[$stepIndex]
  $expected = $expectedSteps[$stepIndex]
  $ordinal = $stepIndex + 1
  & $assertExactProperties $step $stepKeys "Structural step $ordinal"
  & $assertJsonInteger $step.ordinal $ordinal $ordinal `
    "Structural step $ordinal ordinal"
  & $assertJsonInteger $step.process_id 1 ([int]::MaxValue) `
    "Structural step $ordinal process_id"
  & $assertJsonInteger $step.exit_code 0 0 `
    "Structural step $ordinal exit_code"
  & $assertJsonInteger $step.elapsed_milliseconds 0 ([long]::MaxValue) `
    "Structural step $ordinal elapsed_milliseconds"
  & $assertRfc3339Utc $step.started_utc `
    "Structural step $ordinal started_utc"
  & $assertRfc3339Utc $step.ended_utc `
    "Structural step $ordinal ended_utc"
  & $assertJsonBoolean $step.process_started $true `
    "Structural step $ordinal process_started"
  & $assertJsonBoolean $step.timed_out $false `
    "Structural step $ordinal timed_out"
  & $assertJsonBoolean $step.tree_drained $true `
    "Structural step $ordinal tree_drained"
  & $assertJsonBoolean $step.had_live_descendants_after_root_exit $false `
    "Structural step $ordinal had_live_descendants_after_root_exit"
  & $assertJsonBoolean $step.manual_review_required $false `
    "Structural step $ordinal manual_review_required"
  & $assertScalarString $step.name "Structural step $ordinal name"
  & $assertScalarString $step.kind "Structural step $ordinal kind"
  & $assertScalarString $step.executable "Structural step $ordinal executable"
  & $assertScalarString $step.working_directory `
    "Structural step $ordinal working_directory"
  & $assertScalarString $step.stdout "Structural step $ordinal stdout"
  & $assertScalarString $step.stderr "Structural step $ordinal stderr"
  & $assertScalarString $step.result "Structural step $ordinal result"
  & $assertScalarString $step.postcondition `
    "Structural step $ordinal postcondition"
  & $assertScalarString $step.status "Structural step $ordinal status"
  & $assertJsonNull $step.failure_kind `
    "Structural step $ordinal failure_kind"
  & $assertJsonNull $step.error "Structural step $ordinal error"
  if ($step.ordinal -ne $ordinal -or
      $step.name -cne $expected.Name -or
      $step.kind -cne $expected.Kind -or
      $step.postcondition -cne $expected.Postcondition -or
      -not [string]::Equals(
        [string]$step.executable,
        [string]$expected.Executable,
        [StringComparison]::OrdinalIgnoreCase) -or
      -not [string]::Equals(
        [string]$step.working_directory,
        $projectRoot,
        [StringComparison]::OrdinalIgnoreCase)) {
    throw "Committed Structural descriptor is invalid at ordinal $ordinal."
  }
  & $assertExactStrings $step.arguments `
    $expected.Arguments "Structural arguments at ordinal $ordinal"
  if ($step.status -cne 'passed' -or
      $null -ne $step.failure_kind -or $null -ne $step.error) {
    throw "Committed Structural process result is invalid: $($step.name)"
  }
  $artifactPrefix = 'evidence/structural-{0:D2}-{1}-{2}' -f `
    $ordinal, $expected.Name, $headToken
  $expectedArtifacts = [ordered]@{
    stdout = "$artifactPrefix.stdout.txt"
    stderr = "$artifactPrefix.stderr.txt"
    result = "$artifactPrefix.result.json"
  }
  foreach ($field in [string[]]@('stdout', 'stderr', 'result')) {
    $relative = [string]$step.$field
    if ($relative -cne [string]$expectedArtifacts[$field]) {
      throw "Structural $field path is not exact for $($step.name): $relative"
    }
    $artifact = Join-Path $resolvedStructuralRoot $relative
    if (-not (Test-Path -LiteralPath $artifact -PathType Leaf)) {
      throw "Structural $field artifact is missing: $artifact"
    }
  }
  $resultDocument = Get-Content -Raw `
    -LiteralPath (Join-Path $resolvedStructuralRoot ([string]$step.result)) `
    -ErrorAction Stop | ConvertFrom-Json
  $summaryStepJson = $step | ConvertTo-Json -Depth 32 -Compress
  $resultStepJson = $resultDocument | ConvertTo-Json -Depth 32 -Compress
  if ($resultStepJson -cne $summaryStepJson) {
    throw "Structural result JSON differs from summary step: $($step.name)"
  }
}
$postStructuralHead = (git rev-parse HEAD).Trim()
if ($LASTEXITCODE -ne 0 -or $postStructuralHead -ne $finalCommit) {
  throw 'Committed Structural gate changed HEAD.'
}
$postStructuralStatus = @(git status --short)
if ($LASTEXITCODE -ne 0 -or $postStructuralStatus.Count -ne 0) {
  throw "Committed Structural gate dirtied the tree: $($postStructuralStatus -join ', ')"
}
$resolvedStructuralRoot | Set-Content -LiteralPath $structuralRootEvidence -Encoding utf8 -ErrorAction Stop
$recordedStructuralRoot = (
  Get-Content -Raw -LiteralPath $structuralRootEvidence -ErrorAction Stop
).Trim()
if (-not [string]::Equals(
      $recordedStructuralRoot,
      $resolvedStructuralRoot,
      [StringComparison]::OrdinalIgnoreCase)) {
  throw 'Structural evidence-root pointer did not round-trip.'
}
Write-Output "FINAL_STRUCTURAL_ROOT=$recordedStructuralRoot"
```

Expected: source unittest plus all five suites pass in exact order; discovery count/log/hash are revalidated; every descriptor and argument array is exact; route matrix receives 300 seconds; all six child trees drain with no live descendant; every JSON integer, boolean, RFC3339 timestamp, summary, host, identity, and step schema has the exact type and range; every stdout/stderr/result path is the exact final-HEAD-relative name; every result JSON equals its summary step; the repository remains clean at the same HEAD; and only then is the fresh root printed and persisted.

- [ ] **Step 3: Prove both committed Narrative phases stop at capability validation**

```powershell
$finalCommit = (
  Get-Content -Raw -LiteralPath .superpowers/sdd/task-7-5-final-commit.txt -ErrorAction Stop
).Trim()
$currentHead = (git rev-parse HEAD).Trim()
if ($LASTEXITCODE -ne 0 -or $currentHead -ne $finalCommit) {
  throw 'Narrative proof is not starting from the recorded final HEAD.'
}
$narrativeRootEvidence = '.superpowers/sdd/task-7-5-final-narrative-roots.json'
foreach ($signal in [string[]]@(
  $narrativeRootEvidence,
  '.superpowers/sdd/task-7-5-final-review-inputs.json',
  '.superpowers/sdd/task-7-5-final-spec-review.json',
  '.superpowers/sdd/task-7-5-final-standards-review.json'
)) {
  Remove-Item -LiteralPath $signal -Force -ErrorAction SilentlyContinue
}
$assertExactProperties = {
  param($Value, [string[]]$Expected, [string]$Label)
  if ($null -eq $Value -or $Value -is [array]) {
    throw "$Label must be exactly one object."
  }
  $actual = [string[]]@($Value.PSObject.Properties.Name | Sort-Object)
  $wanted = [string[]]@($Expected | Sort-Object)
  if ($actual.Count -ne $wanted.Count -or
      ($actual -join "`n") -cne ($wanted -join "`n")) {
    throw "$Label property set is not exact: $($actual -join ', ')"
  }
}
$assertJsonInteger = {
  param($Value, [long]$Minimum, [long]$Maximum, [string]$Label)
  if (($Value -isnot [int]) -and ($Value -isnot [long])) {
    throw "$Label must be a JSON Int32 or Int64."
  }
  $number = [long]$Value
  if ($number -lt $Minimum -or $number -gt $Maximum) {
    throw "$Label is outside [$Minimum, $Maximum]."
  }
}
$assertJsonBoolean = {
  param($Value, [bool]$Expected, [string]$Label)
  if ($Value -isnot [bool] -or [bool]$Value -ne $Expected) {
    throw "$Label must be the JSON boolean $Expected."
  }
}
$assertRfc3339Utc = {
  param($Value, [string]$Label)
  $parsed = [DateTime]::MinValue
  if ($Value -isnot [string] -or
      [string]$Value -cnotmatch '^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{7}Z$' -or
      -not [DateTime]::TryParseExact(
        [string]$Value,
        'o',
        [Globalization.CultureInfo]::InvariantCulture,
        [Globalization.DateTimeStyles]::RoundtripKind,
        [ref]$parsed
      ) -or
      $parsed.Kind -ne [DateTimeKind]::Utc) {
    throw "$Label must be an RFC3339 UTC round-trip timestamp."
  }
}
$assertScalarString = {
  param($Value, [string]$Label)
  if ($Value -isnot [string]) {
    throw "$Label must be a scalar JSON string."
  }
}
$assertJsonNull = {
  param($Value, [string]$Label)
  if ($null -ne $Value -or $Value -is [array]) {
    throw "$Label must be JSON null."
  }
}
$assertExactStrings = {
  param($Actual, [string[]]$Expected, [string]$Label)
  if ($Actual -isnot [array]) {
    throw "$Label must be a JSON array."
  }
  $items = @($Actual)
  if ($items.Count -ne $Expected.Count) {
    throw "$Label count is $($items.Count), expected $($Expected.Count)."
  }
  for ($itemIndex = 0; $itemIndex -lt $Expected.Count; $itemIndex++) {
    if ($items[$itemIndex] -isnot [string]) {
      throw "$Label item at index $itemIndex must be a JSON string."
    }
    if ($items[$itemIndex] -cne $Expected[$itemIndex]) {
      throw "$Label differs at index $itemIndex."
    }
  }
}
$summaryKeys = [string[]]@(
  'schema_version', 'gate', 'narrative_phase', 'status', 'failure_kind',
  'error', 'started_utc', 'ended_utc', 'head_token', 'host',
  'project_root', 'run_root', 'steps'
)
$identityKeys = [string[]]@(
  'final_path', 'volume_serial_number', 'file_index'
)
$stepKeys = [string[]]@(
  'ordinal', 'name', 'kind', 'executable', 'arguments',
  'working_directory', 'process_started', 'process_id', 'started_utc',
  'ended_utc', 'exit_code', 'timed_out', 'tree_drained',
  'had_live_descendants_after_root_exit', 'elapsed_milliseconds',
  'stdout', 'stderr', 'result', 'postcondition',
  'manual_review_required', 'status', 'failure_kind', 'error'
)
$assertIdentity = {
  param($Identity, [string]$Label)
  & $assertExactProperties $Identity $identityKeys $Label
  if ($Identity.final_path -isnot [string] -or
      [string]::IsNullOrWhiteSpace([string]$Identity.final_path) -or
      -not [IO.Path]::IsPathRooted([string]$Identity.final_path)) {
    throw "$Label final_path must be a nonempty absolute string."
  }
  & $assertJsonInteger $Identity.volume_serial_number 0 ([long]::MaxValue) `
    "$Label.volume_serial_number"
  & $assertJsonInteger $Identity.file_index 0 ([long]::MaxValue) `
    "$Label.file_index"
}
$projectRoot = (Resolve-Path -LiteralPath . -ErrorAction Stop).Path
$structuralRoot = (
  Get-Content -Raw `
    -LiteralPath .superpowers/sdd/task-7-5-final-structural-root.txt `
    -ErrorAction Stop
).Trim()
$structuralSummary = Get-Content -Raw `
  -LiteralPath (Join-Path $structuralRoot 'evidence\gate-summary.json') `
  -ErrorAction Stop | ConvertFrom-Json
& $assertScalarString $structuralSummary.gate 'chained Structural gate'
& $assertScalarString $structuralSummary.status 'chained Structural status'
& $assertScalarString $structuralSummary.head_token 'chained Structural head_token'
if ($structuralSummary.gate -cne 'Structural' -or
    $structuralSummary.status -cne 'passed' -or
    $structuralSummary.head_token -cne $finalCommit.Substring(0, 12)) {
  throw 'Narrative proof is not chained to the current Structural proof.'
}
$checkerPath = [IO.Path]::GetFullPath(
  [IO.Path]::Combine(
    $projectRoot,
    'Tools\check_winter_narrative_capabilities.py'
  )
)
if (Test-Path -LiteralPath $checkerPath) {
  throw "Task 8 capability checker unexpectedly exists: $checkerPath"
}
$pythonCommand = Get-Command python.exe -CommandType Application -ErrorAction Stop |
  Select-Object -First 1
$resolvedPython = (Resolve-Path -LiteralPath $pythonCommand.Source -ErrorAction Stop).Path
$gateHost = Join-Path ([Environment]::SystemDirectory) 'WindowsPowerShell\v1.0\powershell.exe'
$resolvedGateHost = (Resolve-Path -LiteralPath $gateHost -ErrorAction Stop).Path
$winterGate = (Resolve-Path -LiteralPath Tools/Run-WinterInterludeGate.ps1 -ErrorAction Stop).Path
$previousCommitEnvironment = $env:GIT_COMMIT
$finalNarrativeRoots = [ordered]@{}
try {
  $env:GIT_COMMIT = $finalCommit
  foreach ($phase in @('Batch', 'Final')) {
    $phaseRoot = Join-Path ([System.IO.Path]::GetTempPath()) `
      ("winter-final-narrative-$phase-{0}" -f [guid]::NewGuid().ToString('N'))
    & $gateHost -NoLogo -NoProfile -NonInteractive -ExecutionPolicy Bypass -File $winterGate `
      -Gate Narrative `
      -NarrativePhase $phase `
      -ProjectRoot (Get-Location).Path `
      -RunRoot $phaseRoot `
      -ToolTimeoutSeconds 300 `
      -RenPyTimeoutSeconds 300
    $narrativeExit = $LASTEXITCODE
    if ($narrativeExit -ne 1) {
      throw "Committed Narrative $phase exited $narrativeExit instead of exactly 1."
    }
    $summary = Get-Content -Raw -LiteralPath (Join-Path $phaseRoot 'evidence\gate-summary.json') -ErrorAction Stop | ConvertFrom-Json
    $headToken = $finalCommit.Substring(0, 12)
    $expectedError = "Step 'narrative-capability' required file was missing at manifest construction: $checkerPath"
    & $assertExactProperties $summary $summaryKeys `
      "Committed Narrative $phase summary"
    & $assertExactProperties $summary.host `
      ([string[]]@('edition', 'version', 'executable')) `
      "Committed Narrative $phase host"
    & $assertIdentity $summary.host.executable `
      "Committed Narrative $phase host executable identity"
    & $assertIdentity $summary.project_root `
      "Committed Narrative $phase ProjectRoot identity"
    & $assertIdentity $summary.run_root `
      "Committed Narrative $phase RunRoot identity"
    & $assertJsonInteger $summary.schema_version 1 1 `
      "Committed Narrative $phase schema_version"
    & $assertRfc3339Utc $summary.started_utc `
      "Committed Narrative $phase started_utc"
    & $assertRfc3339Utc $summary.ended_utc `
      "Committed Narrative $phase ended_utc"
    & $assertScalarString $summary.gate `
      "Committed Narrative $phase gate"
    & $assertScalarString $summary.narrative_phase `
      "Committed Narrative $phase narrative_phase"
    & $assertScalarString $summary.status `
      "Committed Narrative $phase status"
    & $assertScalarString $summary.failure_kind `
      "Committed Narrative $phase failure_kind"
    & $assertScalarString $summary.error `
      "Committed Narrative $phase error"
    & $assertScalarString $summary.head_token `
      "Committed Narrative $phase head_token"
    & $assertScalarString $summary.host.edition `
      "Committed Narrative $phase host edition"
    & $assertScalarString $summary.host.version `
      "Committed Narrative $phase host version"
    if ($summary.status -cne 'failed' -or
        $summary.failure_kind -cne 'validation' -or
        $summary.error -cne $expectedError -or
        $summary.steps -isnot [array] -or
        @($summary.steps).Count -ne 1) {
      throw "Committed Narrative $phase summary is not the single capability failure."
    }
    if ($summary.schema_version -ne 1 -or
        $summary.gate -cne 'Narrative' -or
        $summary.narrative_phase -cne $phase -or
        $summary.head_token -cne $headToken) {
      throw "Committed Narrative $phase top-level contract is invalid."
    }
    if ($summary.host.edition -cne 'Desktop' -or
        $summary.host.version -isnot [string] -or
        -not ([string]$summary.host.version).StartsWith(
          '5.', [StringComparison]::Ordinal) -or
        -not [string]::Equals(
          [string]$summary.host.executable.final_path,
          $resolvedGateHost,
          [StringComparison]::OrdinalIgnoreCase)) {
      throw "Committed Narrative $phase host contract is invalid."
    }
    $resolvedPhaseRoot = (Resolve-Path -LiteralPath $phaseRoot -ErrorAction Stop).Path
    if (-not [string]::Equals(
          [string]$summary.project_root.final_path,
          $projectRoot,
          [StringComparison]::OrdinalIgnoreCase) -or
        -not [string]::Equals(
          [string]$summary.run_root.final_path,
          $resolvedPhaseRoot,
          [StringComparison]::OrdinalIgnoreCase)) {
      throw "Committed Narrative $phase root identities do not match this invocation."
    }
    foreach ($identity in @($summary.project_root, $summary.run_root)) {
      if ($null -eq $identity.volume_serial_number -or $null -eq $identity.file_index) {
        throw "Committed Narrative $phase omitted an operating-system root identity."
      }
    }
    $step = $summary.steps[0]
    & $assertExactProperties $step $stepKeys `
      "Committed Narrative $phase capability step"
    & $assertJsonInteger $step.ordinal 1 1 `
      "Committed Narrative $phase capability ordinal"
    & $assertJsonBoolean $step.process_started $false `
      "Committed Narrative $phase process_started"
    & $assertJsonBoolean $step.timed_out $false `
      "Committed Narrative $phase timed_out"
    & $assertJsonBoolean $step.tree_drained $true `
      "Committed Narrative $phase tree_drained"
    & $assertJsonBoolean $step.had_live_descendants_after_root_exit $false `
      "Committed Narrative $phase had_live_descendants_after_root_exit"
    & $assertJsonBoolean $step.manual_review_required $false `
      "Committed Narrative $phase manual_review_required"
    & $assertScalarString $step.name `
      "Committed Narrative $phase step name"
    & $assertScalarString $step.kind `
      "Committed Narrative $phase step kind"
    & $assertScalarString $step.executable `
      "Committed Narrative $phase step executable"
    & $assertScalarString $step.working_directory `
      "Committed Narrative $phase step working_directory"
    & $assertScalarString $step.result `
      "Committed Narrative $phase step result"
    & $assertScalarString $step.postcondition `
      "Committed Narrative $phase step postcondition"
    & $assertScalarString $step.status `
      "Committed Narrative $phase step status"
    & $assertScalarString $step.failure_kind `
      "Committed Narrative $phase step failure_kind"
    & $assertScalarString $step.error `
      "Committed Narrative $phase step error"
    foreach ($nullField in [string[]]@(
      'process_id', 'started_utc', 'ended_utc', 'exit_code',
      'elapsed_milliseconds', 'stdout', 'stderr'
    )) {
      & $assertJsonNull $step.$nullField `
        "Committed Narrative $phase step $nullField"
    }
    $expectedResult = "evidence/narrative-01-narrative-capability-$headToken.result.json"
    $expectedOutput = Join-Path $resolvedPhaseRoot `
      "evidence\narrative-01-narrative-capability-$headToken.output.json"
    $expectedArguments = [string[]]@(
      '-B', $checkerPath,
      '--phase', $phase.ToLowerInvariant(),
      '--format', 'json',
      '--output', $expectedOutput
    )
    & $assertExactStrings $step.arguments $expectedArguments `
      "Committed Narrative $phase arguments"
    if ($step.ordinal -ne 1 -or
        $step.name -cne 'narrative-capability' -or
        $step.kind -cne 'Python' -or
        -not [string]::Equals(
          [string]$step.executable,
          $resolvedPython,
          [StringComparison]::OrdinalIgnoreCase) -or
        -not [string]::Equals(
          [string]$step.working_directory,
          $projectRoot,
          [StringComparison]::OrdinalIgnoreCase) -or
        $step.process_started -isnot [bool] -or $step.process_started -or
        $null -ne $step.process_id -or
        $null -ne $step.started_utc -or
        $null -ne $step.ended_utc -or
        $null -ne $step.exit_code -or
        $step.timed_out -isnot [bool] -or $step.timed_out -or
        $step.tree_drained -isnot [bool] -or -not $step.tree_drained -or
        $step.had_live_descendants_after_root_exit -isnot [bool] -or
        $step.had_live_descendants_after_root_exit -or
        $null -ne $step.elapsed_milliseconds -or
        $null -ne $step.stdout -or $null -ne $step.stderr -or
        $step.result -cne $expectedResult -or
        $step.postcondition -cne 'capability-json' -or
        $step.manual_review_required -isnot [bool] -or
        $step.manual_review_required -or
        $step.status -cne 'failed' -or
        $step.failure_kind -cne 'validation' -or
        $step.error -cne $expectedError) {
      throw "Committed Narrative $phase started a child before capability readiness."
    }
    $resultArtifact = Join-Path $resolvedPhaseRoot $expectedResult
    if (-not (Test-Path -LiteralPath $resultArtifact -PathType Leaf)) {
      throw "Committed Narrative $phase result artifact is missing: $resultArtifact"
    }
    if (Test-Path -LiteralPath $expectedOutput) {
      throw "Committed Narrative $phase created structured output before readiness."
    }
    $resultDocument = Get-Content -Raw -LiteralPath $resultArtifact `
      -ErrorAction Stop | ConvertFrom-Json
    if (($resultDocument | ConvertTo-Json -Depth 32 -Compress) -cne
        ($step | ConvertTo-Json -Depth 32 -Compress)) {
      throw "Committed Narrative $phase result JSON differs from its summary step."
    }
    $finalNarrativeRoots[$phase] = $resolvedPhaseRoot
  }
}
finally {
  if ($null -eq $previousCommitEnvironment) {
    Remove-Item Env:GIT_COMMIT -ErrorAction SilentlyContinue
  }
  else {
    $env:GIT_COMMIT = $previousCommitEnvironment
  }
}
$postNarrativeHead = (git rev-parse HEAD).Trim()
if ($LASTEXITCODE -ne 0 -or $postNarrativeHead -ne $finalCommit) {
  throw 'Committed Narrative probes changed HEAD.'
}
$postNarrativeStatus = @(git status --short)
if ($LASTEXITCODE -ne 0 -or $postNarrativeStatus.Count -ne 0) {
  throw "Committed Narrative probes dirtied the tree: $($postNarrativeStatus -join ', ')"
}
if (Test-Path -LiteralPath $checkerPath) {
  throw 'Committed Narrative probes created the absent Task 8 checker.'
}
$narrativeRecord = [pscustomobject][ordered]@{
  schema_version = 1
  final_commit = $finalCommit
  Batch = [string]$finalNarrativeRoots.Batch
  Final = [string]$finalNarrativeRoots.Final
}
$narrativeRecord |
  ConvertTo-Json -Depth 4 |
  Set-Content -LiteralPath $narrativeRootEvidence -Encoding utf8 -ErrorAction Stop
$recordedNarrativeRoots = Get-Content -Raw -LiteralPath $narrativeRootEvidence -ErrorAction Stop | ConvertFrom-Json
& $assertExactProperties $recordedNarrativeRoots `
  ([string[]]@('schema_version', 'final_commit', 'Batch', 'Final')) `
  'recorded Narrative roots'
& $assertScalarString $recordedNarrativeRoots.final_commit `
  'recorded Narrative final_commit'
& $assertScalarString $recordedNarrativeRoots.Batch 'recorded Narrative Batch root'
& $assertScalarString $recordedNarrativeRoots.Final 'recorded Narrative Final root'
if ($recordedNarrativeRoots.schema_version -ne 1 -or
    $recordedNarrativeRoots.final_commit -cne $finalCommit) {
  throw 'Narrative evidence-root record is not bound to final HEAD.'
}
foreach ($phase in @('Batch', 'Final')) {
  if (-not [string]::Equals(
        [string]$recordedNarrativeRoots.$phase,
        [string]$finalNarrativeRoots[$phase],
        [StringComparison]::OrdinalIgnoreCase)) {
    throw "Narrative $phase evidence-root pointer did not round-trip."
  }
  Write-Output "FINAL_NARRATIVE_${phase}_ROOT=$($recordedNarrativeRoots.$phase)"
}
```

Expected: the checker is absent before and after the probes; Batch and Final both return exactly 1 with the exact missing-checker error after one validation result and no child process; every summary/host/identity/step property set, integer, boolean, and RFC3339 timestamp is exact; all process references and streams are null, the structured output is absent, each result JSON equals its summary step, the repository remains clean at the same HEAD, and only then are both fresh roots persisted in one commit-bound ignored JSON mapping.

- [ ] **Step 4: Request independent Spec review, then independent Standards review**

Run this fence once to revalidate every discovery, summary, descriptor,
argument, null/error field, structured-output absence, result equality, and
artifact hash before publishing the immutable review-input record.
After both reviewers have written their decision records as specified below,
run the same fence again. Only the second run may print `REVIEWS_READY`:

```powershell
& {
  $designBase = 'ed262771e740b2e502d30921ed92e1de1deb54b6'
  $functionalBase = (
    Get-Content -Raw -LiteralPath .superpowers/sdd/task-7-5-start.txt `
      -ErrorAction Stop
  ).Trim()
  $reviewCommit = (
    Get-Content -Raw -LiteralPath .superpowers/sdd/task-7-5-final-commit.txt `
      -ErrorAction Stop
  ).Trim()
  $reviewHead = (git rev-parse HEAD).Trim()
  if ($LASTEXITCODE -ne 0 -or $reviewCommit -ne $reviewHead) {
    throw 'Review commit pointer does not equal current HEAD.'
  }
  $reviewStatus = @(git status --short)
  if ($LASTEXITCODE -ne 0 -or $reviewStatus.Count -ne 0) {
    throw "Review input tree is not clean: $($reviewStatus -join ', ')"
  }
  $assertExactProperties = {
    param($Value, [string[]]$Expected, [string]$Label)
    if ($null -eq $Value -or $Value -is [array]) {
      throw "$Label must be exactly one object."
    }
    $actual = [string[]]@($Value.PSObject.Properties.Name | Sort-Object)
    $wanted = [string[]]@($Expected | Sort-Object)
    if ($actual.Count -ne $wanted.Count -or
        ($actual -join "`n") -cne ($wanted -join "`n")) {
      throw "$Label property set is not exact: $($actual -join ', ')"
    }
  }
  $assertJsonInteger = {
    param($Value, [long]$Minimum, [long]$Maximum, [string]$Label)
    if (($Value -isnot [int]) -and ($Value -isnot [long])) {
      throw "$Label must be a JSON Int32 or Int64."
    }
    $number = [long]$Value
    if ($number -lt $Minimum -or $number -gt $Maximum) {
      throw "$Label is outside [$Minimum, $Maximum]."
    }
  }
  $assertJsonBoolean = {
    param($Value, [bool]$Expected, [string]$Label)
    if ($Value -isnot [bool] -or [bool]$Value -ne $Expected) {
      throw "$Label must be the JSON boolean $Expected."
    }
  }
  $assertRfc3339Utc = {
    param($Value, [string]$Label)
    $parsed = [DateTime]::MinValue
    if ($Value -isnot [string] -or
        [string]$Value -cnotmatch '^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{7}Z$' -or
        -not [DateTime]::TryParseExact(
          [string]$Value,
          'o',
          [Globalization.CultureInfo]::InvariantCulture,
          [Globalization.DateTimeStyles]::RoundtripKind,
          [ref]$parsed
        ) -or
        $parsed.Kind -ne [DateTimeKind]::Utc) {
      throw "$Label must be an RFC3339 UTC round-trip timestamp."
    }
  }
  $assertScalarString = {
    param($Value, [string]$Label)
    if ($Value -isnot [string]) {
      throw "$Label must be a scalar JSON string."
    }
  }
  $assertJsonNull = {
    param($Value, [string]$Label)
    if ($null -ne $Value -or $Value -is [array]) {
      throw "$Label must be JSON null."
    }
  }
  $assertExactStrings = {
    param($Actual, [string[]]$Expected, [string]$Label)
    if ($Actual -isnot [array]) {
      throw "$Label must be a JSON array."
    }
    $items = @($Actual)
    if ($items.Count -ne $Expected.Count) {
      throw "$Label count is $($items.Count), expected $($Expected.Count)."
    }
    for ($itemIndex = 0; $itemIndex -lt $Expected.Count; $itemIndex++) {
      if ($items[$itemIndex] -isnot [string]) {
        throw "$Label item at index $itemIndex must be a JSON string."
      }
      if ($items[$itemIndex] -cne $Expected[$itemIndex]) {
        throw "$Label differs at index $itemIndex."
      }
    }
  }
  function Get-CanonicalTrackedTextSha256 {
    [CmdletBinding()]
    param(
      [Parameter(Mandatory = $true)]
      [string]$LiteralPath
    )

    $resolvedPath = (
      Resolve-Path -LiteralPath $LiteralPath -ErrorAction Stop
    ).Path
    [byte[]]$bytes = [IO.File]::ReadAllBytes($resolvedPath)
    $hasBom =
      ($bytes.Length -ge 3 -and
        $bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and
        $bytes[2] -eq 0xBF) -or
      ($bytes.Length -ge 2 -and
        (($bytes[0] -eq 0xFF -and $bytes[1] -eq 0xFE) -or
         ($bytes[0] -eq 0xFE -and $bytes[1] -eq 0xFF))) -or
      ($bytes.Length -ge 4 -and
        $bytes[0] -eq 0x00 -and $bytes[1] -eq 0x00 -and
        $bytes[2] -eq 0xFE -and $bytes[3] -eq 0xFF)
    if ($hasBom) {
      throw "Tracked text catalog rejects BOMs: $LiteralPath"
    }
    $strictUtf8 = New-Object Text.UTF8Encoding($false, $true)
    $sha256 = [Security.Cryptography.SHA256]::Create()
    try {
      $decoded = $strictUtf8.GetString($bytes)
      $canonicalText = $decoded.Replace("`r`n", "`n")
      if ($canonicalText.IndexOf("`r", [StringComparison]::Ordinal) -ge 0) {
        throw "Tracked text catalog rejects standalone CR: $LiteralPath"
      }
      [byte[]]$canonicalBytes = $strictUtf8.GetBytes($canonicalText)
      [byte[]]$digest = $sha256.ComputeHash($canonicalBytes)
      return ([BitConverter]::ToString($digest)).Replace('-', '')
    }
    catch [Text.DecoderFallbackException] {
      throw "Tracked text catalog requires strict UTF-8: $LiteralPath"
    }
    finally {
      $sha256.Dispose()
    }
  }
  $summaryKeys = [string[]]@(
    'schema_version', 'gate', 'narrative_phase', 'status', 'failure_kind',
    'error', 'started_utc', 'ended_utc', 'head_token', 'host',
    'project_root', 'run_root', 'steps'
  )
  $identityKeys = [string[]]@(
    'final_path', 'volume_serial_number', 'file_index'
  )
  $stepKeys = [string[]]@(
    'ordinal', 'name', 'kind', 'executable', 'arguments',
    'working_directory', 'process_started', 'process_id', 'started_utc',
    'ended_utc', 'exit_code', 'timed_out', 'tree_drained',
    'had_live_descendants_after_root_exit', 'elapsed_milliseconds',
    'stdout', 'stderr', 'result', 'postcondition',
    'manual_review_required', 'status', 'failure_kind', 'error'
  )
  $assertIdentity = {
    param($Identity, [string]$Label)
    & $assertExactProperties $Identity $identityKeys $Label
    if ($Identity.final_path -isnot [string] -or
        [string]::IsNullOrWhiteSpace([string]$Identity.final_path) -or
        -not [IO.Path]::IsPathRooted([string]$Identity.final_path)) {
      throw "$Label final_path must be a nonempty absolute string."
    }
    & $assertJsonInteger $Identity.volume_serial_number 0 ([long]::MaxValue) `
      "$Label.volume_serial_number"
    & $assertJsonInteger $Identity.file_index 0 ([long]::MaxValue) `
      "$Label.file_index"
  }
  $expectedImplementationPaths = [string[]]@(
    'Tools/Run-WinterInterludeGate.ps1',
    'Tools/test_winter_interlude_gate.py',
    'Tools/test_governance_winter_interlude.py',
    'docs/superpowers/plans/2026-08-08-governance-winter-interlude.md'
  )
  $actualImplementationPaths = [string[]]@(
    git diff --name-only "$functionalBase..$reviewCommit"
  )
  if ($LASTEXITCODE -ne 0 -or
      (($actualImplementationPaths | Sort-Object) -join "`n") -cne
      (($expectedImplementationPaths | Sort-Object) -join "`n")) {
    throw 'Review implementation range is not the exact four-file scope.'
  }
  $actualPlanPaths = [string[]]@(
    git diff --name-only "$designBase..$functionalBase"
  )
  if ($LASTEXITCODE -ne 0 -or $actualPlanPaths.Count -ne 1 -or
      $actualPlanPaths[0] -cne
        'docs/superpowers/plans/2026-08-09-winter-interlude-executable-gates.md') {
    throw 'Review plan range is not the exact one-file scope.'
  }
  git diff --check "$designBase..$reviewCommit"
  if ($LASTEXITCODE -ne 0) { throw 'Review range failed diff check.' }

  $discoveryRecordPath = '.superpowers/sdd/task-7-5-final-full-python.json'
  $discovery = Get-Content -Raw -LiteralPath $discoveryRecordPath `
    -ErrorAction Stop | ConvertFrom-Json
  $discoveryKeys = [string[]]@(
    'schema_version', 'head_commit', 'command', 'started_utc', 'ended_utc',
    'elapsed_milliseconds', 'exit_code', 'status', 'discovered_test_count',
    'log_path', 'log_sha256'
  )
  & $assertExactProperties $discovery $discoveryKeys 'review discovery record'
  & $assertJsonInteger $discovery.schema_version 1 1 `
    'review discovery schema_version'
  & $assertJsonInteger $discovery.elapsed_milliseconds 0 ([long]::MaxValue) `
    'review discovery elapsed_milliseconds'
  & $assertJsonInteger $discovery.exit_code 0 0 `
    'review discovery exit_code'
  & $assertJsonInteger $discovery.discovered_test_count 339 ([int]::MaxValue) `
    'review discovery discovered_test_count'
  & $assertRfc3339Utc $discovery.started_utc 'review discovery started_utc'
  & $assertRfc3339Utc $discovery.ended_utc 'review discovery ended_utc'
  & $assertScalarString $discovery.head_commit 'review discovery head_commit'
  & $assertScalarString $discovery.command 'review discovery command'
  & $assertScalarString $discovery.status 'review discovery status'
  & $assertScalarString $discovery.log_path 'review discovery log_path'
  & $assertScalarString $discovery.log_sha256 'review discovery log_sha256'
  $discoveryLog = (Resolve-Path -LiteralPath ([string]$discovery.log_path) `
    -ErrorAction Stop).Path
  $discoveryLogHash = (
    Get-FileHash -Algorithm SHA256 -LiteralPath $discoveryLog -ErrorAction Stop
  ).Hash
  if ($discovery.schema_version -ne 1 -or
      $discovery.head_commit -cne $reviewCommit -or
      $discovery.command -cne
        'python -m unittest discover -s Tools -p "test_*.py" -v' -or
      $discovery.status -cne 'passed' -or
      $discovery.exit_code -ne 0 -or
      $discoveryLogHash -cne [string]$discovery.log_sha256) {
    throw 'Review discovery evidence is stale or invalid.'
  }
  $discoveryText = Get-Content -Raw -LiteralPath $discoveryLog -ErrorAction Stop
  $ranMatches = [regex]::Matches(
    $discoveryText,
    '(?m)^Ran ([0-9]+) tests in [0-9]+(?:\.[0-9]+)?s\r?$'
  )
  $logTestCount = 0
  if ($ranMatches.Count -ne 1 -or
      -not [int]::TryParse(
        $ranMatches[0].Groups[1].Value,
        [Globalization.NumberStyles]::None,
        [Globalization.CultureInfo]::InvariantCulture,
        [ref]$logTestCount
      ) -or
      $logTestCount -lt 339 -or
      $logTestCount -ne [int]$discovery.discovered_test_count) {
    throw 'Review discovery log does not contain its one recorded Ran N tests line.'
  }

  $reviewStructuralRoot = (
    Get-Content -Raw `
      -LiteralPath .superpowers/sdd/task-7-5-final-structural-root.txt `
      -ErrorAction Stop
  ).Trim()
  $reviewNarrativeRoots = Get-Content -Raw `
    -LiteralPath .superpowers/sdd/task-7-5-final-narrative-roots.json `
    -ErrorAction Stop | ConvertFrom-Json
  & $assertExactProperties $reviewNarrativeRoots `
    ([string[]]@('schema_version', 'final_commit', 'Batch', 'Final')) `
    'review Narrative root record'
  & $assertJsonInteger $reviewNarrativeRoots.schema_version 1 1 `
    'review Narrative root schema_version'
  & $assertScalarString $reviewNarrativeRoots.final_commit `
    'review Narrative root final_commit'
  & $assertScalarString $reviewNarrativeRoots.Batch `
    'review Narrative Batch root'
  & $assertScalarString $reviewNarrativeRoots.Final `
    'review Narrative Final root'
  if ($reviewNarrativeRoots.schema_version -ne 1 -or
      $reviewNarrativeRoots.final_commit -cne $reviewCommit -or
      $reviewNarrativeRoots.Batch -isnot [string] -or
      $reviewNarrativeRoots.Final -isnot [string] -or
      -not [IO.Path]::IsPathRooted([string]$reviewNarrativeRoots.Batch) -or
      -not [IO.Path]::IsPathRooted([string]$reviewNarrativeRoots.Final) -or
      [string]::Equals(
        [string]$reviewNarrativeRoots.Batch,
        [string]$reviewNarrativeRoots.Final,
        [StringComparison]::OrdinalIgnoreCase)) {
    throw 'Review Narrative root record is stale.'
  }
  $headToken = $reviewCommit.Substring(0, 12)
  $summaryPaths = [ordered]@{
    Structural = Join-Path $reviewStructuralRoot 'evidence\gate-summary.json'
    Batch = Join-Path ([string]$reviewNarrativeRoots.Batch) `
      'evidence\gate-summary.json'
    Final = Join-Path ([string]$reviewNarrativeRoots.Final) `
      'evidence\gate-summary.json'
  }
  $summaries = [ordered]@{}
  foreach ($phaseName in [string[]]@('Structural', 'Batch', 'Final')) {
    $summaryPath = [string]$summaryPaths[$phaseName]
    if (-not (Test-Path -LiteralPath $summaryPath -PathType Leaf)) {
      throw "Review summary is missing: $summaryPath"
    }
    $summaries[$phaseName] = Get-Content -Raw -LiteralPath $summaryPath `
      -ErrorAction Stop | ConvertFrom-Json
  }
  $projectRoot = (Resolve-Path -LiteralPath . -ErrorAction Stop).Path
  $gateHost = Join-Path ([Environment]::SystemDirectory) `
    'WindowsPowerShell\v1.0\powershell.exe'
  $resolvedGateHost = (Resolve-Path -LiteralPath $gateHost -ErrorAction Stop).Path
  $pythonCommand = Get-Command python.exe -CommandType Application `
    -ErrorAction Stop | Select-Object -First 1
  $resolvedPython = (Resolve-Path -LiteralPath $pythonCommand.Source `
    -ErrorAction Stop).Path
  $runner = (Resolve-Path -LiteralPath Tools/Run-RenPySuite.ps1 `
    -ErrorAction Stop).Path
  $checkerPath = [IO.Path]::GetFullPath(
    [IO.Path]::Combine(
      $projectRoot,
      'Tools\check_winter_narrative_capabilities.py'
    )
  )
  if (Test-Path -LiteralPath $checkerPath) {
    throw 'Review boundary requires the Task 8 capability checker to be absent.'
  }

  $structural = $summaries.Structural
  & $assertExactProperties $structural $summaryKeys 'review Structural summary'
  & $assertExactProperties $structural.host `
    ([string[]]@('edition', 'version', 'executable')) `
    'review Structural host'
  & $assertIdentity $structural.host.executable `
    'review Structural host executable identity'
  & $assertIdentity $structural.project_root 'review Structural ProjectRoot identity'
  & $assertIdentity $structural.run_root 'review Structural RunRoot identity'
  & $assertJsonInteger $structural.schema_version 1 1 `
    'review Structural schema_version'
  & $assertRfc3339Utc $structural.started_utc 'review Structural started_utc'
  & $assertRfc3339Utc $structural.ended_utc 'review Structural ended_utc'
  & $assertScalarString $structural.gate 'review Structural gate'
  & $assertScalarString $structural.status 'review Structural status'
  & $assertScalarString $structural.head_token 'review Structural head_token'
  & $assertJsonNull $structural.narrative_phase `
    'review Structural narrative_phase'
  & $assertJsonNull $structural.failure_kind 'review Structural failure_kind'
  & $assertJsonNull $structural.error 'review Structural error'
  & $assertScalarString $structural.host.edition `
    'review Structural host edition'
  & $assertScalarString $structural.host.version `
    'review Structural host version'
  if ($structural.gate -cne 'Structural' -or
      $null -ne $structural.narrative_phase -or
      $structural.status -cne 'passed' -or
      $null -ne $structural.failure_kind -or
      $null -ne $structural.error -or
      $structural.head_token -cne $headToken -or
      $structural.host.edition -cne 'Desktop' -or
      $structural.host.version -isnot [string] -or
      -not ([string]$structural.host.version).StartsWith(
        '5.', [StringComparison]::Ordinal) -or
      -not [string]::Equals(
        [string]$structural.host.executable.final_path,
        $resolvedGateHost,
        [StringComparison]::OrdinalIgnoreCase) -or
      -not [string]::Equals(
        [string]$structural.project_root.final_path,
        $projectRoot,
        [StringComparison]::OrdinalIgnoreCase) -or
      -not [string]::Equals(
        [string]$structural.run_root.final_path,
        $reviewStructuralRoot,
        [StringComparison]::OrdinalIgnoreCase) -or
      $structural.steps -isnot [array] -or
      @($structural.steps).Count -ne 6) {
    throw 'Review Structural summary is not rebound to current evidence.'
  }
  $expectedStructuralSteps = New-Object 'System.Collections.Generic.List[object]'
  [void]$expectedStructuralSteps.Add([pscustomobject]@{
    Name = 'source-contract'
    Kind = 'Python'
    Executable = $resolvedPython
    Postcondition = 'exit-zero'
    Arguments = [string[]]@(
      '-m', 'unittest', 'Tools.test_governance_winter_interlude', '-v'
    )
  })
  $structuralSuites = [string[]]@(
    'test_winter_interlude_state',
    'test_winter_interlude_routing',
    'test_winter_interlude_ending_invariance',
    'test_winter_interlude_route_matrix',
    'test_winter_interlude_mid_save'
  )
  for ($suiteIndex = 0; $suiteIndex -lt $structuralSuites.Count; $suiteIndex++) {
    $ordinal = $suiteIndex + 2
    $suite = $structuralSuites[$suiteIndex]
    [void]$expectedStructuralSteps.Add([pscustomobject]@{
      Name = $suite.Replace('_', '-')
      Kind = 'RenPySuite'
      Executable = $resolvedGateHost
      Postcondition = 'runner-passed'
      Arguments = [string[]]@(
        '-NoLogo', '-NoProfile', '-NonInteractive',
        '-ExecutionPolicy', 'Bypass', '-File', $runner,
        '-ProjectRoot', $projectRoot,
        '-SaveDir', (Join-Path $reviewStructuralRoot `
          ('savedirs\{0:D2}-{1}' -f $ordinal, $suite)),
        '-Mode', 'Suite', '-Suite', $suite,
        '-Expect', 'PASSED',
        '-EvidenceDir', (Join-Path $reviewStructuralRoot 'evidence\runner'),
        '-TimeoutSeconds', '300'
      )
    })
  }
  $structuralArtifacts = New-Object 'System.Collections.Generic.List[object]'
  for ($stepIndex = 0; $stepIndex -lt $expectedStructuralSteps.Count; $stepIndex++) {
    $step = $structural.steps[$stepIndex]
    $expected = $expectedStructuralSteps[$stepIndex]
    $ordinal = $stepIndex + 1
    & $assertExactProperties $step $stepKeys "review Structural step $ordinal"
    & $assertJsonInteger $step.ordinal $ordinal $ordinal `
      "review Structural step $ordinal ordinal"
    & $assertJsonInteger $step.process_id 1 ([int]::MaxValue) `
      "review Structural step $ordinal process_id"
    & $assertJsonInteger $step.exit_code 0 0 `
      "review Structural step $ordinal exit_code"
    & $assertJsonInteger $step.elapsed_milliseconds 0 ([long]::MaxValue) `
      "review Structural step $ordinal elapsed_milliseconds"
    & $assertRfc3339Utc $step.started_utc `
      "review Structural step $ordinal started_utc"
    & $assertRfc3339Utc $step.ended_utc `
      "review Structural step $ordinal ended_utc"
    & $assertJsonBoolean $step.process_started $true `
      "review Structural step $ordinal process_started"
    & $assertJsonBoolean $step.timed_out $false `
      "review Structural step $ordinal timed_out"
    & $assertJsonBoolean $step.tree_drained $true `
      "review Structural step $ordinal tree_drained"
    & $assertJsonBoolean $step.had_live_descendants_after_root_exit $false `
      "review Structural step $ordinal had_live_descendants_after_root_exit"
    & $assertJsonBoolean $step.manual_review_required $false `
      "review Structural step $ordinal manual_review_required"
    & $assertScalarString $step.name `
      "review Structural step $ordinal name"
    & $assertScalarString $step.kind `
      "review Structural step $ordinal kind"
    & $assertScalarString $step.executable `
      "review Structural step $ordinal executable"
    & $assertScalarString $step.working_directory `
      "review Structural step $ordinal working_directory"
    & $assertScalarString $step.stdout `
      "review Structural step $ordinal stdout"
    & $assertScalarString $step.stderr `
      "review Structural step $ordinal stderr"
    & $assertScalarString $step.result `
      "review Structural step $ordinal result"
    & $assertScalarString $step.postcondition `
      "review Structural step $ordinal postcondition"
    & $assertScalarString $step.status `
      "review Structural step $ordinal status"
    & $assertJsonNull $step.failure_kind `
      "review Structural step $ordinal failure_kind"
    & $assertJsonNull $step.error `
      "review Structural step $ordinal error"
    if ($step.name -cne $expected.Name -or
        $step.kind -cne $expected.Kind -or
        $step.postcondition -cne $expected.Postcondition -or
        -not [string]::Equals(
          [string]$step.executable,
          [string]$expected.Executable,
          [StringComparison]::OrdinalIgnoreCase) -or
        -not [string]::Equals(
          [string]$step.working_directory,
          $projectRoot,
          [StringComparison]::OrdinalIgnoreCase) -or
        $step.status -cne 'passed' -or
        $null -ne $step.failure_kind -or $null -ne $step.error) {
      throw "Review Structural descriptor is invalid at ordinal $ordinal."
    }
    & $assertExactStrings $step.arguments `
      $expected.Arguments "review Structural arguments at ordinal $ordinal"
    $artifactPrefix = 'evidence/structural-{0:D2}-{1}-{2}' -f `
      $ordinal, $expected.Name, $headToken
    $expectedArtifacts = [ordered]@{
      stdout = "$artifactPrefix.stdout.txt"
      stderr = "$artifactPrefix.stderr.txt"
      result = "$artifactPrefix.result.json"
    }
    $artifactHashes = [ordered]@{}
    foreach ($field in [string[]]@('stdout', 'stderr', 'result')) {
      if ([string]$step.$field -cne [string]$expectedArtifacts[$field]) {
        throw "Review Structural $field path is not exact at ordinal $ordinal."
      }
      $artifactPath = Join-Path $reviewStructuralRoot ([string]$step.$field)
      if (-not (Test-Path -LiteralPath $artifactPath -PathType Leaf)) {
        throw "Review Structural artifact is missing: $artifactPath"
      }
      $artifactHashes[$field] = (
        Get-FileHash -Algorithm SHA256 -LiteralPath $artifactPath -ErrorAction Stop
      ).Hash
    }
    $resultDocument = Get-Content -Raw `
      -LiteralPath (Join-Path $reviewStructuralRoot ([string]$step.result)) `
      -ErrorAction Stop | ConvertFrom-Json
    & $assertExactProperties $resultDocument $stepKeys `
      "review Structural result $ordinal"
    if (($resultDocument | ConvertTo-Json -Depth 32 -Compress) -cne
        ($step | ConvertTo-Json -Depth 32 -Compress)) {
      throw "Review Structural result differs from summary at ordinal $ordinal."
    }
    [void]$structuralArtifacts.Add([pscustomobject][ordered]@{
      ordinal = $ordinal
      name = $expected.Name
      stdout_path = [string]$step.stdout
      stdout_sha256 = [string]$artifactHashes.stdout
      stderr_path = [string]$step.stderr
      stderr_sha256 = [string]$artifactHashes.stderr
      result_path = [string]$step.result
      result_sha256 = [string]$artifactHashes.result
    })
  }

  $narrativeArtifacts = New-Object 'System.Collections.Generic.List[object]'
  foreach ($phaseName in [string[]]@('Batch', 'Final')) {
    $summary = $summaries[$phaseName]
    $phaseRoot = [string]$reviewNarrativeRoots.$phaseName
    $expectedError = "Step 'narrative-capability' required file was missing at manifest construction: $checkerPath"
    & $assertExactProperties $summary $summaryKeys `
      "review Narrative $phaseName summary"
    & $assertExactProperties $summary.host `
      ([string[]]@('edition', 'version', 'executable')) `
      "review Narrative $phaseName host"
    & $assertIdentity $summary.host.executable `
      "review Narrative $phaseName host executable identity"
    & $assertIdentity $summary.project_root `
      "review Narrative $phaseName ProjectRoot identity"
    & $assertIdentity $summary.run_root `
      "review Narrative $phaseName RunRoot identity"
    & $assertJsonInteger $summary.schema_version 1 1 `
      "review Narrative $phaseName schema_version"
    & $assertRfc3339Utc $summary.started_utc `
      "review Narrative $phaseName started_utc"
    & $assertRfc3339Utc $summary.ended_utc `
      "review Narrative $phaseName ended_utc"
    & $assertScalarString $summary.gate `
      "review Narrative $phaseName gate"
    & $assertScalarString $summary.narrative_phase `
      "review Narrative $phaseName narrative_phase"
    & $assertScalarString $summary.status `
      "review Narrative $phaseName status"
    & $assertScalarString $summary.failure_kind `
      "review Narrative $phaseName failure_kind"
    & $assertScalarString $summary.error `
      "review Narrative $phaseName error"
    & $assertScalarString $summary.head_token `
      "review Narrative $phaseName head_token"
    & $assertScalarString $summary.host.edition `
      "review Narrative $phaseName host edition"
    & $assertScalarString $summary.host.version `
      "review Narrative $phaseName host version"
    if ($summary.gate -cne 'Narrative' -or
        $summary.narrative_phase -cne $phaseName -or
        $summary.status -cne 'failed' -or
        $summary.failure_kind -cne 'validation' -or
        $summary.error -cne $expectedError -or
        $summary.head_token -cne $headToken -or
        $summary.host.edition -cne 'Desktop' -or
        $summary.host.version -isnot [string] -or
        -not ([string]$summary.host.version).StartsWith(
          '5.', [StringComparison]::Ordinal) -or
        -not [string]::Equals(
          [string]$summary.host.executable.final_path,
          $resolvedGateHost,
          [StringComparison]::OrdinalIgnoreCase) -or
        -not [string]::Equals(
          [string]$summary.project_root.final_path,
          $projectRoot,
          [StringComparison]::OrdinalIgnoreCase) -or
        -not [string]::Equals(
          [string]$summary.run_root.final_path,
          $phaseRoot,
          [StringComparison]::OrdinalIgnoreCase) -or
        $summary.steps -isnot [array] -or
        @($summary.steps).Count -ne 1) {
      throw "Review Narrative $phaseName summary is not rebound to current evidence."
    }
    $step = $summary.steps[0]
    & $assertExactProperties $step $stepKeys `
      "review Narrative $phaseName capability step"
    & $assertJsonInteger $step.ordinal 1 1 `
      "review Narrative $phaseName ordinal"
    & $assertJsonBoolean $step.process_started $false `
      "review Narrative $phaseName process_started"
    & $assertJsonBoolean $step.timed_out $false `
      "review Narrative $phaseName timed_out"
    & $assertJsonBoolean $step.tree_drained $true `
      "review Narrative $phaseName tree_drained"
    & $assertJsonBoolean $step.had_live_descendants_after_root_exit $false `
      "review Narrative $phaseName had_live_descendants_after_root_exit"
    & $assertJsonBoolean $step.manual_review_required $false `
      "review Narrative $phaseName manual_review_required"
    & $assertScalarString $step.name `
      "review Narrative $phaseName step name"
    & $assertScalarString $step.kind `
      "review Narrative $phaseName step kind"
    & $assertScalarString $step.executable `
      "review Narrative $phaseName step executable"
    & $assertScalarString $step.working_directory `
      "review Narrative $phaseName step working_directory"
    & $assertScalarString $step.result `
      "review Narrative $phaseName step result"
    & $assertScalarString $step.postcondition `
      "review Narrative $phaseName step postcondition"
    & $assertScalarString $step.status `
      "review Narrative $phaseName step status"
    & $assertScalarString $step.failure_kind `
      "review Narrative $phaseName step failure_kind"
    & $assertScalarString $step.error `
      "review Narrative $phaseName step error"
    foreach ($nullField in [string[]]@(
      'process_id', 'started_utc', 'ended_utc', 'exit_code',
      'elapsed_milliseconds', 'stdout', 'stderr'
    )) {
      & $assertJsonNull $step.$nullField `
        "review Narrative $phaseName step $nullField"
    }
    $expectedResult = "evidence/narrative-01-narrative-capability-$headToken.result.json"
    $expectedOutput = Join-Path $phaseRoot `
      "evidence\narrative-01-narrative-capability-$headToken.output.json"
    $expectedArguments = [string[]]@(
      '-B', $checkerPath,
      '--phase', $phaseName.ToLowerInvariant(),
      '--format', 'json',
      '--output', $expectedOutput
    )
    & $assertExactStrings $step.arguments `
      $expectedArguments "review Narrative $phaseName arguments"
    if ($step.name -cne 'narrative-capability' -or
        $step.kind -cne 'Python' -or
        -not [string]::Equals(
          [string]$step.executable,
          $resolvedPython,
          [StringComparison]::OrdinalIgnoreCase) -or
        -not [string]::Equals(
          [string]$step.working_directory,
          $projectRoot,
          [StringComparison]::OrdinalIgnoreCase) -or
        $null -ne $step.process_id -or
        $null -ne $step.started_utc -or
        $null -ne $step.ended_utc -or
        $null -ne $step.exit_code -or
        $null -ne $step.elapsed_milliseconds -or
        $null -ne $step.stdout -or $null -ne $step.stderr -or
        $step.result -cne $expectedResult -or
        $step.postcondition -cne 'capability-json' -or
        $step.status -cne 'failed' -or
        $step.failure_kind -cne 'validation' -or
        $step.error -cne $expectedError) {
      throw "Review Narrative $phaseName capability result is not exact."
    }
    if (Test-Path -LiteralPath $expectedOutput) {
      throw "Review Narrative $phaseName structured output unexpectedly exists."
    }
    $resultArtifact = Join-Path $phaseRoot $expectedResult
    if (-not (Test-Path -LiteralPath $resultArtifact -PathType Leaf)) {
      throw "Review Narrative $phaseName result is missing: $resultArtifact"
    }
    $resultDocument = Get-Content -Raw -LiteralPath $resultArtifact `
      -ErrorAction Stop | ConvertFrom-Json
    & $assertExactProperties $resultDocument $stepKeys `
      "review Narrative $phaseName result"
    if (($resultDocument | ConvertTo-Json -Depth 32 -Compress) -cne
        ($step | ConvertTo-Json -Depth 32 -Compress)) {
      throw "Review Narrative $phaseName result differs from its summary step."
    }
    [void]$narrativeArtifacts.Add([pscustomobject][ordered]@{
      phase = $phaseName
      result_path = $expectedResult
      result_sha256 = (
        Get-FileHash -Algorithm SHA256 -LiteralPath $resultArtifact `
          -ErrorAction Stop
      ).Hash
      structured_output_path = $expectedOutput
      structured_output_absent = $true
    })
  }

  $postReviewCatalogArtifacts = [object[]]@(
    [pscustomobject][ordered]@{
      path = 'Tools/Run-WinterInterludeGate.ps1'
      canonical_sha256 = '10FDC7932237E17806173D7DA48E80CC368891855A64B70A9617D97660116B3A'
    },
    [pscustomobject][ordered]@{
      path = 'Tools/test_winter_interlude_gate.py'
      canonical_sha256 = '81D1438B22EB2EC30C3051A33499277C785CDF8E69D98C0F23EADD56426E5E72'
    }
  )
  foreach ($artifact in $postReviewCatalogArtifacts) {
    $actualHash = Get-CanonicalTrackedTextSha256 `
      -LiteralPath $artifact.path
    if ($actualHash -cne $artifact.canonical_sha256) {
      throw "Post-review tracked catalog changed: $($artifact.path)"
    }
  }

  $originalRedLogs = @(
    Get-ChildItem -LiteralPath '.superpowers/sdd' -File -ErrorAction Stop |
      Where-Object { $_.Name -like 'task-7-5-*-red.txt' }
  )
  if ($originalRedLogs.Count -ne 13) {
    throw "The original Task 7.5 RED glob must remain exactly 13 files; found $($originalRedLogs.Count)."
  }
  $remediationRedArtifacts = [object[]]@(
    [pscustomobject][ordered]@{
      path = '.superpowers/sdd/task-7-5-review-fix-dependency-lease-red-run.txt'
      sha256 = 'CAC8025C45F0E815E71E0C1AA5800317A409474F0366AD712973ABC8D0259072'
      base_commit = 'ac4ab10cda4f7d836d0b9eb8375505b39353035d'
      test_method = 'test_future_runner_dependency_lease_denies_in_place_write_until_gate_exit'
      behavior_pattern = 'Behavior-specific RED:\s+write_error was None, the base gate returned 0, and\s+all five future runner records used ModifiedSuite after the in-place write\.'
      expected_metadata = [string[]]@(
        'BASE_COMMIT=ac4ab10cda4f7d836d0b9eb8375505b39353035d',
        'EXIT_CODE=1',
        'RAN=1',
        'FAILURES=1',
        'ERRORS=0',
        'PRE_FIX_IN_PLACE_WRITE_SUCCEEDED=true',
        'PRE_FIX_GATE_RETURN_CODE=0',
        'PRE_FIX_FUTURE_SUITE_KIND=ModifiedSuite',
        'PRE_FIX_RECORDS=6',
        'PRE_FIX_SUMMARY_STATUS=passed'
      )
    },
    [pscustomobject][ordered]@{
      path = '.superpowers/sdd/task-7-5-review-fix-protected-appdata-red-run.txt'
      sha256 = 'E6D636C3894CAA1BE955AC5B81C8199E306D98DF7D12EE7858C99A6926BE8D1E'
      base_commit = 'ac4ab10cda4f7d836d0b9eb8375505b39353035d'
      test_method = 'test_process_appdata_state_change_after_source_stops_before_publication'
      behavior_pattern = 'Behavior-specific RED:\s+the base gate returned 0 with empty stderr and ran all\s+six records after process APPDATA was replaced by a junction into RunRoot\.'
      expected_metadata = [string[]]@(
        'BASE_COMMIT=ac4ab10cda4f7d836d0b9eb8375505b39353035d',
        'EXIT_CODE=1',
        'RAN=1',
        'FAILURES=1',
        'ERRORS=0',
        'PRE_FIX_GATE_RETURN_CODE=0',
        'PRE_FIX_RECORDS=6',
        'PRE_FIX_SUMMARY_STATUS=passed'
      )
    }
  )
  foreach ($artifact in $remediationRedArtifacts) {
    if (-not (Test-Path -LiteralPath $artifact.path -PathType Leaf)) {
      throw "Remediation raw RED artifact is missing: $($artifact.path)"
    }
    $actualHash = (
      Get-FileHash -Algorithm SHA256 -LiteralPath $artifact.path `
        -ErrorAction Stop
    ).Hash
    if ($actualHash -cne $artifact.sha256) {
      throw "Remediation raw RED artifact changed: $($artifact.path)"
    }
    $artifactText = Get-Content -Raw -LiteralPath $artifact.path `
      -ErrorAction Stop
    foreach ($metadataLine in $artifact.expected_metadata) {
      if ([regex]::Matches(
          $artifactText,
          '(?m)^' + [regex]::Escape($metadataLine) + '\r?$'
        ).Count -ne 1) {
        throw "Remediation raw RED metadata line is not unique: $metadataLine"
      }
    }
    if ($artifactText -cnotmatch [regex]::Escape($artifact.base_commit) -or
        $artifactText -cnotmatch [regex]::Escape($artifact.test_method) -or
        -not [regex]::IsMatch($artifactText, $artifact.behavior_pattern)) {
      throw "Remediation raw RED metadata is invalid: $($artifact.path)"
    }
    $rawRunMatches = [regex]::Matches(
      $artifactText,
      '(?ms)^Raw combined unittest output \(verbatim\):\r?\n(.*?)(?=^Observed process exit code:)'
    )
    if ($rawRunMatches.Count -ne 1) {
      throw "Remediation raw RED must contain one verbatim run: $($artifact.path)"
    }
    $rawRun = $rawRunMatches[0].Groups[1].Value
    if ([regex]::Matches($rawRun, '(?m)^Ran 1 test in ').Count -ne 1 -or
        [regex]::Matches($rawRun, '(?m)^FAILED \(failures=1\)\r?$').Count -ne 1 -or
        $rawRun -match '(?m)^ERROR:') {
      throw "Remediation raw RED behavior counts are invalid: $($artifact.path)"
    }
  }
  $redMutantReplayArtifacts = [object[]]@(
    [pscustomobject][ordered]@{
      path = '.superpowers/sdd/task-7-5-red-mutant-replay.py'
      sha256 = '3F73E8E35236E577218FFAE7A590F35F68D07BAE69D16103600777ECCD84D0FA'
    },
    [pscustomobject][ordered]@{
      path = '.superpowers/sdd/task-7-5-narrative-manifest-red-provenance.txt'
      sha256 = 'EBE4F8494AF62545AB4B8933DADCC79ABA236518D27561707FF1B37FF61FCDE2'
    },
    [pscustomobject][ordered]@{
      path = '.superpowers/sdd/task-7-5-scanner-json-red-provenance.txt'
      sha256 = 'B9B5248530B96997BD9092F1B4AFE95052948363756004D76A6F364CAA65700A'
    }
  )
  foreach ($artifact in $redMutantReplayArtifacts) {
    $actualHash = (
      Get-FileHash -Algorithm SHA256 -LiteralPath $artifact.path `
        -ErrorAction Stop
    ).Hash
    if ($actualHash -cne $artifact.sha256) {
      throw "RED mutant replay artifact changed: $($artifact.path)"
    }
  }

  $reviewInputPath = '.superpowers/sdd/task-7-5-final-review-inputs.json'
  $specDecisionPath = '.superpowers/sdd/task-7-5-final-spec-review.json'
  $standardsDecisionPath = '.superpowers/sdd/task-7-5-final-standards-review.json'
  $reviewInputs = [pscustomobject][ordered]@{
    schema_version = 1
    design_base = $designBase
    functional_base = $functionalBase
    final_commit = $reviewCommit
    plan_diff_command = "git diff --no-ext-diff --binary $designBase..$functionalBase -- docs/superpowers/plans/2026-08-09-winter-interlude-executable-gates.md"
    implementation_diff_command = "git diff --no-ext-diff --binary $functionalBase..$reviewCommit -- Tools/Run-WinterInterludeGate.ps1 Tools/test_winter_interlude_gate.py Tools/test_governance_winter_interlude.py docs/superpowers/plans/2026-08-08-governance-winter-interlude.md"
    implementation_paths = $expectedImplementationPaths
    design_path = 'docs/superpowers/specs/2026-08-09-winter-interlude-executable-gates-design.md'
    implementation_plan_path = 'docs/superpowers/plans/2026-08-09-winter-interlude-executable-gates.md'
    post_review_catalog_artifacts = $postReviewCatalogArtifacts
    red_log_glob = '.superpowers/sdd/task-7-5-*-red.txt'
    red_log_count = 13
    remediation_red_artifacts = $remediationRedArtifacts
    red_mutant_replay_artifacts = $redMutantReplayArtifacts
    discovery_record_path = $discoveryRecordPath
    discovery_log_path = [string]$discovery.log_path
    discovery_log_sha256 = $discoveryLogHash
    discovered_test_count = [int]$discovery.discovered_test_count
    structural_root = $reviewStructuralRoot
    structural_summary_sha256 = (
      Get-FileHash -Algorithm SHA256 -LiteralPath $summaryPaths.Structural
    ).Hash
    structural_artifacts = [object[]]$structuralArtifacts.ToArray()
    narrative_batch_root = [string]$reviewNarrativeRoots.Batch
    narrative_batch_summary_sha256 = (
      Get-FileHash -Algorithm SHA256 -LiteralPath $summaryPaths.Batch
    ).Hash
    narrative_final_root = [string]$reviewNarrativeRoots.Final
    narrative_final_summary_sha256 = (
      Get-FileHash -Algorithm SHA256 -LiteralPath $summaryPaths.Final
    ).Hash
    narrative_artifacts = [object[]]$narrativeArtifacts.ToArray()
  }
  $expectedReviewInputJson = $reviewInputs | ConvertTo-Json -Depth 8 -Compress
  if (-not (Test-Path -LiteralPath $reviewInputPath -PathType Leaf)) {
    Remove-Item -LiteralPath $specDecisionPath -Force -ErrorAction SilentlyContinue
    Remove-Item -LiteralPath $standardsDecisionPath -Force -ErrorAction SilentlyContinue
    $reviewInputs | ConvertTo-Json -Depth 8 |
      Set-Content -LiteralPath $reviewInputPath -Encoding utf8 -ErrorAction Stop
  }
  $recordedReviewInputs = Get-Content -Raw -LiteralPath $reviewInputPath `
    -ErrorAction Stop | ConvertFrom-Json
  if (($recordedReviewInputs | ConvertTo-Json -Depth 8 -Compress) -cne
      $expectedReviewInputJson) {
    throw 'Persisted review inputs are stale or changed.'
  }
  $reviewInputHash = (
    Get-FileHash -Algorithm SHA256 -LiteralPath $reviewInputPath -ErrorAction Stop
  ).Hash
  if (-not (Test-Path -LiteralPath $specDecisionPath -PathType Leaf) -or
      -not (Test-Path -LiteralPath $standardsDecisionPath -PathType Leaf)) {
    Write-Output "REVIEW_INPUTS=$reviewInputPath"
    Write-Output "REVIEW_INPUTS_SHA256=$reviewInputHash"
    Write-Output "SPEC_DECISION=$specDecisionPath"
    Write-Output "STANDARDS_DECISION=$standardsDecisionPath"
    return
  }

  $decisionKeys = [string[]]@(
    'schema_version', 'review_kind', 'reviewer_id',
    'review_inputs_sha256', 'final_commit', 'critical_count',
    'important_count', 'verdict', 'raw_report'
  )
  $parseDecision = {
    param([string]$Path, [string]$Label)
    $raw = Get-Content -Raw -LiteralPath $Path -ErrorAction Stop
    $trimmed = $raw.Trim()
    if (-not $trimmed.StartsWith('{', [StringComparison]::Ordinal) -or
        -not $trimmed.EndsWith('}', [StringComparison]::Ordinal)) {
      throw "$Label decision file must contain one JSON object, not an array."
    }
    $parsed = $raw | ConvertFrom-Json
    if ($null -eq $parsed -or $parsed -is [array] -or @($parsed).Count -ne 1) {
      throw "$Label decision file did not parse as exactly one object."
    }
    & $assertExactProperties $parsed $decisionKeys "$Label decision"
    $parsed
  }
  [object[]]$decisions = @($null, $null)
  $decisions[0] = & $parseDecision $specDecisionPath 'Spec'
  $decisions[1] = & $parseDecision $standardsDecisionPath 'Standards'
  $expectedKinds = [string[]]@('Spec', 'Standards')
  for ($decisionIndex = 0; $decisionIndex -lt 2; $decisionIndex++) {
    $decision = $decisions[$decisionIndex]
    & $assertJsonInteger $decision.schema_version 1 1 `
      "$($expectedKinds[$decisionIndex]) decision schema_version"
    & $assertJsonInteger $decision.critical_count 0 0 `
      "$($expectedKinds[$decisionIndex]) decision critical_count"
    & $assertJsonInteger $decision.important_count 0 0 `
      "$($expectedKinds[$decisionIndex]) decision important_count"
    & $assertScalarString $decision.review_kind `
      "$($expectedKinds[$decisionIndex]) decision review_kind"
    & $assertScalarString $decision.reviewer_id `
      "$($expectedKinds[$decisionIndex]) decision reviewer_id"
    & $assertScalarString $decision.review_inputs_sha256 `
      "$($expectedKinds[$decisionIndex]) decision review_inputs_sha256"
    & $assertScalarString $decision.final_commit `
      "$($expectedKinds[$decisionIndex]) decision final_commit"
    & $assertScalarString $decision.verdict `
      "$($expectedKinds[$decisionIndex]) decision verdict"
    & $assertScalarString $decision.raw_report `
      "$($expectedKinds[$decisionIndex]) decision raw_report"
    if ($decision.review_kind -cne $expectedKinds[$decisionIndex] -or
        [string]::IsNullOrWhiteSpace([string]$decision.reviewer_id) -or
        $decision.review_inputs_sha256 -cne $reviewInputHash -or
        $decision.final_commit -cne $reviewCommit -or
        $decision.verdict -cne 'READY' -or
        [string]::IsNullOrWhiteSpace([string]$decision.raw_report) -or
        [string]$decision.raw_report -match '(?i)\bNOT\s+READY\b' -or
        [string]$decision.raw_report -cnotmatch
          '(?m)^Critical 0 / Important 0\s+(?:—|-)\s+READY\s*$') {
      throw "$($expectedKinds[$decisionIndex]) review decision is not C0/I0 READY."
    }
  }
  if ($decisions[0].reviewer_id -ceq $decisions[1].reviewer_id) {
    throw 'Spec and Standards reviews did not use independent reviewers.'
  }
  Write-Output "SPEC_REVIEW_SHA256=$((Get-FileHash -Algorithm SHA256 -LiteralPath $specDecisionPath).Hash)"
  Write-Output "STANDARDS_REVIEW_SHA256=$((Get-FileHash -Algorithm SHA256 -LiteralPath $standardsDecisionPath).Hash)"
  Write-Output "REVIEWS_READY=$reviewCommit"
}
```

Give the fresh Spec reviewer the printed review-input path and SHA-256. Require
it to read that exact JSON, execute both recorded diff commands, inspect every
recorded artifact, and check public behavior, manifests, schema, migration,
exact four-file scope, and the Task 8 boundary. Then give a different fresh
reviewer the same immutable input for the Standards review of final-path
identity, reparse/junction handling, argv encoding, Job Object cleanup,
evidence TOCTOU behavior, fake-dependency leakage, parser removal, retained
dependency-lease lifetime (including `TreeDrained=false`), live known/process
APPDATA revalidation, and the independently reconstructable RED-mutant
provenance. Both reviewers must verify every path/hash in
`post_review_catalog_artifacts`, `remediation_red_artifacts`, and
`red_mutant_replay_artifacts`. Each reviewer must independently reopen both
`remediation_red_artifacts` paths, recompute each SHA-256, and confirm the
recorded base commit, exact test method, exit 1, `Ran 1 test`, one failure,
zero errors, and behavior-specific pre-fix observation rather than relying on
the coordinator's summary. For each `post_review_catalog_artifacts`
`canonical_sha256`, both reviewers must recompute the value with the exact
strict-UTF-8, BOM-rejecting, CRLF-to-LF, standalone-CR-rejecting,
UTF-8-without-BOM algorithm in the Step 4 fence; a checkout-local physical
`Get-FileHash` is not the tracked catalog identity.
The Standards reviewer must not read or receive the Spec decision record.

Each reviewer may modify only its own ignored decision path printed by the
fence. The file must contain exactly one top-level JSON object, never an array,
and its JSON must have exactly these properties:
`schema_version=1`, `review_kind` (`Spec` or `Standards`), a nonempty unique
`reviewer_id`, the printed `review_inputs_sha256`, `final_commit`, Int32/Int64
`critical_count`, Int32/Int64 `important_count`, `verdict` (`READY` only for
C0/I0), and `raw_report`. `raw_report` must be the reviewer's verbatim returned
report, not a coordinator summary, must contain a complete
`Critical 0 / Important 0 — READY` (ASCII `-` is also accepted) line, and must
not contain `NOT READY`. Run Spec first and Standards second, then rerun the
fence and require its final line to equal `REVIEWS_READY=` concatenated with
the exact current HEAD recorded in `$reviewCommit`.

- [ ] **Step 5: Close every review finding with a focused RED and amend**

The first fresh Standards decision against implementation commit
`ac4ab10cda4f7d836d0b9eb8375505b39353035d` was C0/I3. Preserve every
earlier Task 1-7 RED transcript, expected count, and intermediate catalog as
historical evidence. The following three post-review repair loops are an
authoritative delta over those catalogs; they must not be back-projected into
an earlier RED or used to rewrite its claimed failure surface.

The frozen post-review final catalog is canonical-text-bound before any rerun:

```powershell
function Get-CanonicalTrackedTextSha256 {
  [CmdletBinding()]
  param(
    [Parameter(Mandatory = $true)]
    [string]$LiteralPath
  )

  $resolvedPath = (
    Resolve-Path -LiteralPath $LiteralPath -ErrorAction Stop
  ).Path
  [byte[]]$bytes = [IO.File]::ReadAllBytes($resolvedPath)
  $hasBom =
    ($bytes.Length -ge 3 -and
      $bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and
      $bytes[2] -eq 0xBF) -or
    ($bytes.Length -ge 2 -and
      (($bytes[0] -eq 0xFF -and $bytes[1] -eq 0xFE) -or
       ($bytes[0] -eq 0xFE -and $bytes[1] -eq 0xFF))) -or
    ($bytes.Length -ge 4 -and
      $bytes[0] -eq 0x00 -and $bytes[1] -eq 0x00 -and
      $bytes[2] -eq 0xFE -and $bytes[3] -eq 0xFF)
  if ($hasBom) {
    throw "Tracked text catalog rejects BOMs: $LiteralPath"
  }
  $strictUtf8 = New-Object Text.UTF8Encoding($false, $true)
  $sha256 = [Security.Cryptography.SHA256]::Create()
  try {
    $decoded = $strictUtf8.GetString($bytes)
    $canonicalText = $decoded.Replace("`r`n", "`n")
    if ($canonicalText.IndexOf("`r", [StringComparison]::Ordinal) -ge 0) {
      throw "Tracked text catalog rejects standalone CR: $LiteralPath"
    }
    [byte[]]$canonicalBytes = $strictUtf8.GetBytes($canonicalText)
    [byte[]]$digest = $sha256.ComputeHash($canonicalBytes)
    return ([BitConverter]::ToString($digest)).Replace('-', '')
  }
  catch [Text.DecoderFallbackException] {
    throw "Tracked text catalog requires strict UTF-8: $LiteralPath"
  }
  finally {
    $sha256.Dispose()
  }
}
$postReviewCatalog = [ordered]@{
  'Tools/Run-WinterInterludeGate.ps1' =
    '10FDC7932237E17806173D7DA48E80CC368891855A64B70A9617D97660116B3A'
  'Tools/test_winter_interlude_gate.py' =
    '81D1438B22EB2EC30C3051A33499277C785CDF8E69D98C0F23EADD56426E5E72'
}
foreach ($entry in $postReviewCatalog.GetEnumerator()) {
  $actual = Get-CanonicalTrackedTextSha256 -LiteralPath $entry.Key
  if ($actual -cne $entry.Value) {
    throw "Post-review catalog hash mismatch: $($entry.Key)"
  }
}
```

Expected: both canonical hashes match exactly after strict UTF-8 decode,
BOM rejection, CRLF-to-LF normalization, standalone-CR rejection, and
UTF-8-without-BOM re-encoding. These hashes, together with the exact
method catalog below, supersede only the final-state portions of the earlier
catalogs. They do not change the four tracked implementation paths, and they
do not add an ignored replay/provenance file to that tracked scope.

#### Step 5A: Close the executable/required-file check-use gap with leases

Replace exactly these three historical methods; do not retain aliases under
the old names because that would inflate the catalog:

| Class | Remove historical method | Final method |
|---|---|---|
| `WinterInterludeGateProcessTests` | `test_project_root_replacement_after_source_is_caught_before_result` | `test_project_root_rename_is_denied_until_dependency_leases_close` |
| `WinterInterludeGateProcessTests` | `test_required_file_replaced_during_child_is_failed_after_tree_drain` | `test_future_runner_dependency_lease_denies_in_place_write_until_gate_exit` |
| `WinterInterludeGateManifestTests` | `test_runner_required_file_identity_is_rechecked_before_first_suite` | `test_unexecuted_dependency_leases_close_after_validation_stop` |

Inside `WinterInterludeGateProcessTests`, the two dependency/parent-chain
replacements are exactly:

```python
    def test_project_root_rename_is_denied_until_dependency_leases_close(
        self,
    ) -> None:
        ready = self.base / "project-lease-ready"
        release = self.base / "project-lease-release"
        moved_project = self.base / "project-after-gate"
        process = self.fixture.start_writer_race(ready, release)

        def stop_process() -> None:
            if process.poll() is None:
                process.kill()
            process.communicate(timeout=10)

        self.addCleanup(stop_process)
        deadline = time.monotonic() + 15.0
        while not ready.exists() and time.monotonic() < deadline:
            time.sleep(0.01)
        if not ready.is_file():
            early_stdout, early_stderr = process.communicate(timeout=10)
            self.fail(
                "source child did not reach the project lease barrier: "
                f"returncode={process.returncode}; stdout={early_stdout!r}; "
                f"stderr={early_stderr!r}"
            )

        rename_error: OSError | None = None
        try:
            os.replace(self.project, moved_project)
        except OSError as error:
            rename_error = error
        finally:
            release.write_text("release", encoding="utf-8")

        gate_stdout, gate_stderr = process.communicate(timeout=65)
        diagnostic = {
            "rename_error": repr(rename_error),
            "stdout": gate_stdout,
            "stderr": gate_stderr,
            "records": self.fixture.records(),
        }
        self.assertIsInstance(rename_error, PermissionError, diagnostic)
        self.assertTrue(
            getattr(rename_error, "winerror", None) in (5, 32, 33)
            or getattr(rename_error, "errno", None) == 13,
            diagnostic,
        )
        self.assertEqual(0, process.returncode, diagnostic)
        self.assertEqual(6, len(diagnostic["records"]), diagnostic)
        self.assertEqual("passed", self.fixture.summary()["status"])

        os.replace(self.project, moved_project)
        os.replace(moved_project, self.project)

    def test_future_runner_dependency_lease_denies_in_place_write_until_gate_exit(
        self,
    ) -> None:
        ready = self.base / "dependency-lease-ready"
        release = self.base / "dependency-lease-release"
        runner = self.tools / "Run-RenPySuite.ps1"
        original = runner.read_bytes()
        modified = original.replace(
            b"kind = 'RenPySuite'",
            b"kind = 'ModifiedSuite'",
        )
        self.assertNotEqual(original, modified)
        original_file_index = runner.stat().st_ino
        process = self.fixture.start_writer_race(ready, release)

        def stop_process() -> None:
            if process.poll() is None:
                process.kill()
            process.communicate(timeout=10)

        self.addCleanup(stop_process)
        deadline = time.monotonic() + 15.0
        while not ready.exists() and time.monotonic() < deadline:
            time.sleep(0.01)
        if not ready.is_file():
            early_stdout, early_stderr = process.communicate(timeout=10)
            self.fail(
                "source child did not reach the barrier: "
                f"returncode={process.returncode}; stdout={early_stdout!r}; "
                f"stderr={early_stderr!r}"
            )

        write_error: OSError | None = None
        try:
            with runner.open("r+b", buffering=0) as stream:
                stream.seek(0)
                stream.write(modified)
                stream.truncate()
                os.fsync(stream.fileno())
        except OSError as error:
            write_error = error
        finally:
            release.write_text("release", encoding="utf-8")

        gate_stdout, gate_stderr = process.communicate(timeout=65)
        diagnostic = {
            "write_error": repr(write_error),
            "stdout": gate_stdout,
            "stderr": gate_stderr,
            "records": self.fixture.records(),
        }
        self.assertIsInstance(write_error, PermissionError, diagnostic)
        self.assertTrue(
            getattr(write_error, "winerror", None) in (5, 32, 33)
            or getattr(write_error, "errno", None) == 13,
            diagnostic,
        )
        self.assertEqual(original_file_index, runner.stat().st_ino)
        self.assertEqual(original, runner.read_bytes())
        self.assertEqual(0, process.returncode, diagnostic)
        self.assertEqual(6, len(diagnostic["records"]), diagnostic)
        self.assertEqual(
            ["RenPySuite"] * 5,
            [record["kind"] for record in diagnostic["records"][1:]],
        )
        summary = self.fixture.summary()
        self.assertEqual("passed", summary["status"])
        self.assertEqual(6, len(summary["steps"]))

        with runner.open("r+b", buffering=0) as stream:
            stream.seek(0)
            stream.write(original)
            stream.truncate()
            os.fsync(stream.fileno())
        self.assertEqual(original_file_index, runner.stat().st_ino)
        self.assertEqual(original, runner.read_bytes())
```

Inside `WinterInterludeGateManifestTests`, the validation-stop replacement is
exactly:

```python
    def test_unexecuted_dependency_leases_close_after_validation_stop(self) -> None:
        runner = self.fixture.root / "Tools" / "Run-RenPySuite.ps1"
        checker = (
            self.fixture.root / "Tools" / "check_winter_narrative_capabilities.py"
        )
        checker.unlink()
        original = runner.read_bytes()
        original_file_index = runner.stat().st_ino

        completed = self.fixture.run("Narrative", "Batch")
        self.assertNotEqual(completed.returncode, 0)
        self.assertEqual([], self.fixture.records())
        summary = self.fixture.summary()
        self.assertEqual(len(summary["steps"]), 1)
        failed = summary["steps"][0]
        self.assertEqual(failed["name"], "narrative-capability")
        self.assertEqual(failed["failure_kind"], "validation")
        self.assertFalse(failed["process_started"])
        self.assertFalse(failed["timed_out"])
        self.assertTrue(failed["tree_drained"])
        self.assertFalse(failed["had_live_descendants_after_root_exit"])
        self.assertEqual(failed["status"], "failed")
        self.assertIsInstance(failed["error"], str)
        self.assertTrue(failed["error"])
        for field in (
            "process_id", "started_utc", "ended_utc", "exit_code",
            "elapsed_milliseconds", "stdout", "stderr",
        ):
            self.assertIsNone(failed[field], field)
        self.assertEqual(
            json.loads(
                (self.fixture.run_root / failed["result"]).read_text(
                    encoding="utf-8"
                )
            ),
            failed,
        )
        with runner.open("r+b", buffering=0) as stream:
            stream.seek(0)
            stream.write(original)
            stream.truncate()
            os.fsync(stream.fileno())
        self.assertEqual(original_file_index, runner.stat().st_ino)
        self.assertEqual(original, runner.read_bytes())
```

The behavior-specific RED is the second replacement above, run against
`ac4ab10cda4f7d836d0b9eb8375505b39353035d` before adding the lease. It must
fail because an `r+b` write changes `Run-RenPySuite.ps1` in place without
changing its file ID, the gate runs all six Structural children, and the five
future records say `ModifiedSuite`:

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_future_runner_dependency_lease_denies_in_place_write_until_gate_exit `
  -v 2>&1 |
  Tee-Object -FilePath `
    .superpowers/sdd/task-7-5-review-fix-dependency-lease-red-run.txt
if ($LASTEXITCODE -eq 0) {
  throw 'Dependency-lease behavior RED unexpectedly passed.'
}
```

The final C# catalog has one `StepDependencyLease` per manifest step. At
manifest construction, `AcquireStepDependencyLease` acquires the executable
and every present required file as follows, in this exact order:

1. Validate a plain absolute file path and obtain a full-chain, no-reparse
   identity.
2. Retain `HeldPathChain` for every component through the leaf.
3. Open the leaf non-inheritable with `GenericRead`, share mode
   `FileShareRead` only, `OpenExisting`, and
   `FileAttributeNormal | FileFlagOpenReparsePoint |
   FileFlagBackupSemantics`.
4. Compare the read handle identity, retained-chain leaf identity, and
   requested-path identity with `SameStablePath`.

`StepDependencyLease.ExecutablePath` is the leased executable's canonical
final path. `FirstMissingRequiredFilePath` preserves the established
validation-result behavior for a missing required file while all present
future-step dependencies remain leased. `AssertStable()` validates both the
retained readable handle and the still-addressable full path. The public
process API is exactly:

```text
public static BoundedProcessResult RunProcessTree(
    StepDependencyLease dependencyLease,
    string[] arguments,
    string workingDirectory,
    string stdoutPath,
    string stderrPath,
    int timeoutMilliseconds,
    PathIdentity expectedEvidenceDirectoryIdentity,
    StructuredOutputReservation structuredOutputReservation)
```

It calls `dependencyLease.AssertStable()` before argument validation, derives
the executable only from `dependencyLease.ExecutablePath`, and calls
`AssertStable()` again immediately before building the command line and
calling `CreateProcessW`. `New-GateStep` stores `DependencyLease` and never
stores `ExecutableIdentity` or `RequiredFileIdentities`.
`Get-GateStepDependencyValidationError` checks
`FirstMissingRequiredFilePath` and calls `$Step.DependencyLease.AssertStable()`;
`Invoke-GateStep` passes `$Step.DependencyLease` to `RunProcessTree`.

Normal and validation-stop paths dispose the manifest lease list in reverse
step order; each lease disposes required files in reverse order and then its
executable. The outer `finally` closes structured-output reservations first
and dependency leases second. The fail-closed undrained branch sets
`$script:EvidencePublicationSafe = $false`; the footer must therefore skip
`Close-GateStepDependencyLeases`, keep the script-scoped list as a strong
reference, and retain all dependency handles until the dedicated PowerShell
host exits. This branch writes no result or summary.

Replace the final source-contract method with these exact assertions:

```python
    def test_executable_identity_uses_readable_full_chain_api(self) -> None:
        source = GATE.read_text(encoding="utf-8")
        resolver = source[
            source.index("function Resolve-PythonExecutable {") :
            source.index("function Get-ExpectedProjectFilePath {")
        ]
        builder = source[
            source.index("function New-GateStep {") :
            source.index("function Get-StructuralGateManifest {")
        ]
        dependency = source[
            source.index("function Get-GateStepDependencyValidationError {") :
            source.index("function Invoke-GateStep {")
        ]
        lease_native = source[
            source.index(
                "private static StepDependencyFile AcquireStepDependencyFile("
            ) :
            source.index("private static void AssertStepDependencyFileStable(")
        ]
        self.assertIn(
            "[WinterGate.Native]::GetReadableFileIdentity(",
            resolver,
        )
        self.assertIn("AcquireStepDependencyLease(", builder)
        self.assertIn("DependencyLease = $dependencyLease", builder)
        self.assertIn("$Step.DependencyLease.AssertStable()", dependency)
        self.assertIn("HeldPathChain pathChain", lease_native)
        self.assertIn("GenericRead,\n                FileShareRead,", lease_native)
        self.assertNotIn("FileShareWrite", lease_native)
        self.assertIn(
            "public static BoundedProcessResult RunProcessTree(\n"
            "        StepDependencyLease dependencyLease,",
            source,
        )
        footer = source[
            source.rindex("$script:StructuredOutputReservations = $null") :
        ]
        self.assertLess(
            footer.index("Close-GateStructuredOutputReservations"),
            footer.index("Close-GateStepDependencyLeases"),
        )
        self.assertIn("$script:EvidencePublicationSafe = $false", footer)
        self.assertIn(
            "if ($script:EvidencePublicationSafe) {\n"
            "            Close-GateStepDependencyLeases\n"
            "        }",
            footer,
        )
```

Also update `run_narrative_with_prelaunch_python_swap` to use
`passing_narrative_documents("batch")`, catch the replacement `OSError`, and
return `(CompletedProcess, replacement_error)`. Its existing
`test_python_executable_identity_is_rechecked_before_first_child` now requires
a passed nine-step Narrative run plus `PermissionError` with Win32 error 5,
32, or 33; it no longer expects a late validation result after successful
replacement.

```python
    def test_python_executable_identity_is_rechecked_before_first_child(self) -> None:
        fixture = self.make_project()
        try:
            completed, replacement_error = run_narrative_with_prelaunch_python_swap(
                fixture
            )
            diagnostic = {
                "replacement_error": repr(replacement_error),
                "stdout": completed.stdout,
                "stderr": completed.stderr,
                "records": fixture.records(),
            }
            self.assertEqual(completed.returncode, 0, diagnostic)
            self.assertIsInstance(replacement_error, PermissionError, diagnostic)
            self.assertIn(
                getattr(replacement_error, "winerror", None),
                (5, 32, 33),
                diagnostic,
            )
            self.assertEqual(9, len(fixture.records()), diagnostic)
            summary = fixture.summary()
            self.assertEqual("passed", summary["status"], diagnostic)
            self.assertEqual(9, len(summary["steps"]), diagnostic)
        finally:
            fixture.close()
```

Run the complete lease GREEN, including the source, same-object write,
parent-chain rename, prelaunch executable, validation-stop, C# 5 compile, and
official PowerShell parser contracts:

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateInterfaceTests.test_script_exists_and_parses_with_official_powershell_parser `
  Tools.test_winter_interlude_gate.WinterInterludeGateNativeFoundationTests.test_exact_native_readable_identity_rejects_parent_junction `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_json_evidence_writer_is_native_guarded_create_new `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_executable_identity_uses_readable_full_chain_api `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_project_root_rename_is_denied_until_dependency_leases_close `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_future_runner_dependency_lease_denies_in_place_write_until_gate_exit `
  Tools.test_winter_interlude_gate.WinterInterludeGateCapabilityTests.test_python_executable_identity_is_rechecked_before_first_child `
  Tools.test_winter_interlude_gate.WinterInterludeGateManifestTests.test_unexecuted_dependency_leases_close_after_validation_stop `
  -v
if ($LASTEXITCODE -ne 0) { throw 'Dependency-lease GREEN failed.' }
```

Expected: all eight tests pass. The synchronized `r+b` write and project-root
rename are denied until host exit; the same operations succeed after exit;
unexecuted future-step leases are closed on a normal validation stop; and the
source asserts that an undrained tree retains the lease list until host exit.

#### Step 5B: Revalidate protected APPDATA roots at every safety boundary

Add exactly one new test,
`WinterInterludeGateProcessTests.test_process_appdata_state_change_after_source_stops_before_publication`.
It may rename and junction only the fixture-owned process `APPDATA`; it must
never junction to, rename, write, or delete the real Windows known
ApplicationData directory. The test starts the source child at the existing
writer-race barrier, renames fixture `APPDATA`, replaces it with a junction to
a fixture-owned root whose `RenPy\CourtOfShadows-save` contains `RunRoot`, and
always removes the junction leaf with `os.rmdir` before restoring the original
directory.

```python
    def test_process_appdata_state_change_after_source_stops_before_publication(
        self,
    ) -> None:
        ready = self.base / "appdata-state-ready"
        release = self.base / "appdata-state-release"
        original_appdata = self.base / "isolated-appdata-before-swap"
        redirected_appdata = self.base / "redirected-process-appdata"
        protected_save = (
            redirected_appdata / "RenPy" / "CourtOfShadows-save"
        )
        protected_save.mkdir(parents=True)
        self.fixture.run_root = protected_save / "run-01"
        process = self.fixture.start_writer_race(ready, release)

        def stop_process() -> None:
            if process.poll() is None:
                process.kill()
            process.communicate(timeout=10)

        self.addCleanup(stop_process)
        deadline = time.monotonic() + 15.0
        while not ready.exists() and time.monotonic() < deadline:
            time.sleep(0.01)
        if not ready.is_file():
            early_stdout, early_stderr = process.communicate(timeout=10)
            self.fail(
                "source child did not reach the APPDATA state barrier: "
                f"returncode={process.returncode}; stdout={early_stdout!r}; "
                f"stderr={early_stderr!r}"
            )

        os.replace(self.appdata, original_appdata)
        try:
            create_junction(self.appdata, redirected_appdata)
            self.assertEqual(
                protected_save.resolve(strict=True),
                (self.appdata / "RenPy" / "CourtOfShadows-save").resolve(
                    strict=True
                ),
            )
            release.write_text("release", encoding="utf-8")
            gate_stdout, gate_stderr = process.communicate(timeout=65)
        finally:
            if process.poll() is None:
                process.kill()
                process.communicate(timeout=10)
            if os.path.lexists(self.appdata):
                os.rmdir(self.appdata)
            if original_appdata.exists() and not os.path.lexists(self.appdata):
                os.replace(original_appdata, self.appdata)

        diagnostic = {
            "stdout": gate_stdout,
            "stderr": gate_stderr,
            "records": self.fixture.records(),
        }
        self.assertEqual(1, process.returncode, diagnostic)
        self.assertRegex(gate_stderr, r"(?i)path identity")
        self.assertEqual(1, len(diagnostic["records"]), diagnostic)
        evidence = self.fixture.run_root / "evidence"
        self.assertEqual([], list(evidence.glob("*.result.json")))
        self.assertFalse((evidence / "gate-summary.json").exists())
```

Run that one method against `ac4ab10cda4f7d836d0b9eb8375505b39353035d`
before the protected-root repair:

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_process_appdata_state_change_after_source_stops_before_publication `
  -v 2>&1 |
  Tee-Object -FilePath `
    .superpowers/sdd/task-7-5-review-fix-protected-appdata-red-run.txt
if ($LASTEXITCODE -eq 0) {
  throw 'Protected-APPDATA state RED unexpectedly passed.'
}
```

Expected RED: `Ran 1 test`, one behavior failure and no error. The old gate
returns 0, records all six Structural children, and publishes a passed summary
because it compares `RunRoot` with a stale player-save plan.

The two post-review raw filenames deliberately end in `-red-run.txt`, not
`-red.txt`; therefore they do not enter or renumber the original 13-file
`task-7-5-*-red.txt` evidence glob.

The final protected-root catalog replaces `Get-ProtectedPlayerSavePaths` with
these responsibilities:

- `Get-CurrentProtectedPlayerSaveRootInput` independently resolves
  `KnownApplicationData` and `ProcessApplicationData`.
- `Get-ProtectedPlayerSaveRoots` returns exactly two records without
  deduplication. Each record has `SourceKind`, normalized `ConfiguredPath`,
  and a full-chain directory `Identity`.
- `Assert-ProtectedPlayerSaveState` requires both records, re-resolves the
  current source, compares the configured path and `SameStablePath` identity,
  recomputes the current `RenPy\CourtOfShadows-save` prospective plan, and
  rejects `RunLocation` when `Test-SameOrChildFinalPath` is true.
- `New-VerifiedRunRoot` calls that assertion before creation, before and after
  each missing RunRoot component, after the exact final identity, around the
  `evidence` and `savedirs` children, and once more after the final RunRoot,
  `evidence`, and `savedirs` identity rechecks and immediately before return.
- `New-VerifiedGateChildDirectory` calls it immediately before and after a
  manifest child directory. All five Structural/Narrative manifest child
  creations use this wrapper.
- `Assert-RunTreeDirectoryIdentities`, `Assert-AllGateDirectoryIdentities`,
  and `Assert-NonEvidenceGateDirectoryIdentities` each revalidate protected
  roots. Consequently launch, post-drain, result pre/post-write, and summary
  pre/post-write boundaries all re-resolve both roots.

Replace `test_native_path_contract_is_declared` with the exact final method:

```python
    def test_native_path_contract_is_declared(self) -> None:
        source = GATE.read_text(encoding="utf-8")
        for declaration in (
            "sealed class PathIdentity",
            "enum PathKind",
            "sealed class WinterGatePathIdentityException",
            "partial class Native",
            "GetPathIdentity(",
            "TryGetPathIdentity(",
            "CreateDirectoryExclusive(",
            "PathIdentity expectedParentIdentity",
            "SameObject(",
            "SameStablePath(",
            "SameStablePath(parent.LeafIdentity, expectedParentIdentity)",
            "current-drive-rooted paths are not accepted",
            "must not be rooted on the current drive",
            "Windows known ApplicationData folder is unavailable",
            "Windows known ApplicationData folder could not be resolved",
            "function Get-ProtectedPlayerSaveRoots",
            "function Assert-ProtectedPlayerSaveState",
            "function New-VerifiedGateChildDirectory",
            "$script:ProtectedSaveRoots",
        ):
            self.assertIn(declaration, source)
        self.assertIn("function Assert-WinterGateHostIdentity", source)
        self.assertIn("[WinterGate.Native]::SameObject(", source)
        self.assertNotIn("function Assert-WinterGateBootstrapHost", source)
        self.assertNotIn("function Get-ProtectedPlayerSavePaths", source)

        protected = source[
            source.index("function Get-CurrentProtectedPlayerSaveRootInput {") :
            source.index("function New-VerifiedChildDirectory {")
        ]
        for contract in (
            "'KnownApplicationData'",
            "'ProcessApplicationData'",
            "ConfiguredPath = $normalized",
            "Identity = $identity",
            "[WinterGate.Native]::SameStablePath(",
            "Get-ProspectiveDirectoryPlan",
            "Test-SameOrChildFinalPath $RunLocation $savePlan",
        ):
            self.assertIn(contract, protected)

        run_root = source[
            source.index("function New-VerifiedRunRoot {") :
            source.index("# BEGIN LOOP 3.3-P1 HOST AND PROJECT FILE HELPERS")
        ]
        self.assertIn("function New-VerifiedGateChildDirectory", run_root)
        run_root_function = run_root[
            : run_root.index("function New-VerifiedGateChildDirectory {")
        ]
        self.assertEqual(
            8,
            run_root_function.count("Assert-ProtectedPlayerSaveState"),
        )
        final_evidence_recheck = run_root_function.rfind(
            "[void](Assert-GatePathState $evidenceIdentity 'evidence directory')"
        )
        final_savedirs_recheck = run_root_function.rfind(
            "[void](Assert-GatePathState $savedirsIdentity 'savedirs directory')"
        )
        final_protected_recheck = run_root_function.rfind(
            "Assert-ProtectedPlayerSaveState"
        )
        final_return = run_root_function.rfind("return [pscustomobject][ordered]@{")
        self.assertLess(final_evidence_recheck, final_savedirs_recheck)
        self.assertLess(final_savedirs_recheck, final_protected_recheck)
        self.assertLess(final_protected_recheck, final_return)

        manifests = source[
            source.index("function Get-StructuralGateManifest {") :
            source.index(
                "# END LOOP 3.3-P2 STEP AND PROVISIONAL MANIFEST BUILDERS"
            )
        ]
        self.assertEqual(
            5,
            manifests.count("New-VerifiedGateChildDirectory"),
        )
        self.assertNotIn("New-VerifiedChildDirectory", manifests)

        final_guards = source[
            source.index("function Assert-RunTreeDirectoryIdentities {") :
            source.index(
                "# END LOOP 3.4-P2 FINAL PROJECT AND DIRECTORY RECHECKS"
            )
        ]
        self.assertEqual(
            3,
            final_guards.count("Assert-ProtectedPlayerSaveState"),
        )
```

Run the protected-root GREEN:

```powershell
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGatePathSafetyTests.test_native_path_contract_is_declared `
  Tools.test_winter_interlude_gate.WinterInterludeGateProcessTests.test_process_appdata_state_change_after_source_stops_before_publication `
  -v
if ($LASTEXITCODE -ne 0) { throw 'Protected-APPDATA GREEN failed.' }
```

Expected: both tests pass. After the first child the junction mutation causes
exit 1 with a path-identity diagnostic, exactly one child record, no result
JSON, and no `gate-summary.json` in the newly redirected RunRoot. The final
RunRoot construction guard passes only after the last RunRoot, `evidence`, and
`savedirs` identity rechecks and before the function returns its identities.

Preserve the two verbatim post-review RED replays without staging them. Their
exact byte bindings are:

| Ignored remediation RED artifact | SHA-256 |
|---|---|
| `.superpowers/sdd/task-7-5-review-fix-dependency-lease-red-run.txt` | `CAC8025C45F0E815E71E0C1AA5800317A409474F0366AD712973ABC8D0259072` |
| `.superpowers/sdd/task-7-5-review-fix-protected-appdata-red-run.txt` | `E6D636C3894CAA1BE955AC5B81C8199E306D98DF7D12EE7858C99A6926BE8D1E` |

Both files bind base commit
`ac4ab10cda4f7d836d0b9eb8375505b39353035d`, the exact inserted test method
and command, exit 1, `Ran 1 test`, one failure, zero errors, and the full raw
failure output plus behavior-specific observation. The dependency artifact
also binds successful pre-fix in-place write, gate return 0, future kind
`ModifiedSuite`, six records, and passed summary; the APPDATA artifact binds
gate return 0, six records, and passed summary. Step 4 records them under
`remediation_red_artifacts` and revalidates those fields on both fence runs.

#### Step 5C: Bind and independently replay the two reconstructed RED mutants

Keep the original `.superpowers/sdd/task-7-5-*-red.txt` glob at exactly 13
files. Add these three ignored provenance artifacts without staging them:

| Ignored artifact | SHA-256 |
|---|---|
| `.superpowers/sdd/task-7-5-red-mutant-replay.py` | `3F73E8E35236E577218FFAE7A590F35F68D07BAE69D16103600777ECCD84D0FA` |
| `.superpowers/sdd/task-7-5-narrative-manifest-red-provenance.txt` | `EBE4F8494AF62545AB4B8933DADCC79ABA236518D27561707FF1B37FF61FCDE2` |
| `.superpowers/sdd/task-7-5-scanner-json-red-provenance.txt` | `B9B5248530B96997BD9092F1B4AFE95052948363756004D76A6F364CAA65700A` |

The deterministic recipe is bound to base commit
`ac4ab10cda4f7d836d0b9eb8375505b39353035d`, base gate blob
`4a914d5f90683c553bcdfb1b3333cdb7b7352d92`, canonical SHA-256
`24B5DA3D1C93BCF32E6D92BBC14135E492DD7DE9FED04CC02C7132511C11F858`,
and CRLF SHA-256
`F4DE797E226CA835182058B8D53FF02AB887925B904CC751050F878279F85D0E`.
Replay each mutant in a new detached temporary worktree:

```powershell
$replayScript = (
  Resolve-Path -LiteralPath `
    .superpowers/sdd/task-7-5-red-mutant-replay.py -ErrorAction Stop
).Path
$replays = @(
  [pscustomobject]@{
    Mutation = 'narrative'
    Class = 'Tools.test_winter_interlude_gate.WinterInterludeGateNarrativeManifestTests'
    MutantSha256 = 'D4EEBCF6AAF3ADE413DDCBAB0E9590E87650CA52C589DBBEF6749BD2B3B87242'
    MutantBlobSha1 = 'a4e422ed51cbfd1636e055a48b504f40c54a6699'
    Ran = 5
    Failures = 17
  },
  [pscustomobject]@{
    Mutation = 'scanner'
    Class = 'Tools.test_winter_interlude_gate.WinterInterludeGateScannerEvidenceTests'
    MutantSha256 = 'CDDE3D9CD8432FDCDAA8CC3C039062547D1B378297A491A5ABBB00B40C547A7C'
    MutantBlobSha1 = 'f8a735309e8760e99f2d8e332f900d92bfc31979'
    Ran = 7
    Failures = 32
  }
)
foreach ($replay in $replays) {
  $worktree = Join-Path `
    ([IO.Path]::GetTempPath()) `
    ('winter-task75-red-replay-' + [guid]::NewGuid().ToString('N'))
  git worktree add --detach $worktree `
    ac4ab10cda4f7d836d0b9eb8375505b39353035d
  if ($LASTEXITCODE -ne 0) { throw 'Could not create RED replay worktree.' }
  try {
    python $replayScript $replay.Mutation $worktree
    if ($LASTEXITCODE -ne 0) { throw 'Could not reconstruct RED mutant.' }
    $mutantPath = Join-Path $worktree 'Tools/Run-WinterInterludeGate.ps1'
    $physicalHash = (
      Get-FileHash -Algorithm SHA256 -LiteralPath $mutantPath -ErrorAction Stop
    ).Hash
    $blobHash = (git -C $worktree hash-object -- $mutantPath).Trim()
    if ($LASTEXITCODE -ne 0 -or
        $physicalHash -cne $replay.MutantSha256 -or
        $blobHash -cne $replay.MutantBlobSha1) {
      throw "Reconstructed RED mutant hash mismatch: $($replay.Mutation)"
    }
    Push-Location $worktree
    try {
      $replayOutput = [string](
        python -m unittest $replay.Class -v 2>&1 | Out-String
      )
      $replayExit = $LASTEXITCODE
    }
    finally {
      Pop-Location
    }
    if ($replayExit -ne 1 -or
        $replayOutput -notmatch "(?m)^Ran $($replay.Ran) tests" -or
        $replayOutput -notmatch
          "FAILED \(failures=$($replay.Failures)\)" -or
        $replayOutput -match 'FAILED .*errors=') {
      throw "Unexpected independent RED replay: $($replay.Mutation)"
    }
  }
  finally {
    git worktree remove --force $worktree
    if ($LASTEXITCODE -ne 0) { throw 'Could not remove RED replay worktree.' }
  }
}
```

Expected: Narrative reconstructs physical SHA-256
`D4EEBCF6AAF3ADE413DDCBAB0E9590E87650CA52C589DBBEF6749BD2B3B87242`,
reports `Ran 5 tests`, 17 failures, zero errors, and exit 1. Scanner
reconstructs physical SHA-256
`CDDE3D9CD8432FDCDAA8CC3C039062547D1B378297A491A5ABBB00B40C547A7C`,
reports `Ran 7 tests`, 32 failures, zero errors, and exit 1. Both temporary
worktrees are removed and no replay process remains.
The Step 4 review-input fence hashes all three ignored artifacts and records
them under `red_mutant_replay_artifacts`; `red_log_glob` remains unchanged and
`red_log_count` is exactly 13.

#### Step 5D: Verify the authoritative post-review catalog

The final gate-module catalog is:

| Test class | Final methods |
|---|---:|
| `WinterInterludeGateInterfaceTests` | 3 |
| `WinterInterludeGatePathSafetyTests` | 18 |
| `WinterInterludeGateNativeFoundationTests` | 1 |
| `WinterInterludeGateNativeWriterTests` | 1 |
| `WinterInterludeGateProcessTests` | 29 |
| `WinterInterludeGateCapabilityTests` | 13 |
| `WinterInterludeGateNarrativeManifestTests` | 5 |
| `WinterInterludeGateScannerEvidenceTests` | 7 |
| `WinterInterludeGateManifestTests` | 8 |
| `WinterInterludeGateMigrationTests` | 2 |
| **Total** | **87** |

Run static syntax/compile fences before the long discovery:

```powershell
$tokens = $null
$parseErrors = $null
[void][Management.Automation.Language.Parser]::ParseFile(
  (Resolve-Path -LiteralPath Tools/Run-WinterInterludeGate.ps1).Path,
  [ref]$tokens,
  [ref]$parseErrors
)
if ($parseErrors.Count -ne 0) {
  throw "PowerShell parser errors: $($parseErrors -join '; ')"
}
python -c "import ast,pathlib; ast.parse(pathlib.Path(r'Tools/test_winter_interlude_gate.py').read_text(encoding='utf-8'))"
if ($LASTEXITCODE -ne 0) { throw 'Python AST parse failed.' }
python -m unittest `
  Tools.test_winter_interlude_gate.WinterInterludeGateNativeFoundationTests.test_exact_native_readable_identity_rejects_parent_junction `
  -v
if ($LASTEXITCODE -ne 0) { throw 'Exact C# 5 native source compile failed.' }
git diff --check -- `
  Tools/Run-WinterInterludeGate.ps1 `
  Tools/test_winter_interlude_gate.py `
  docs/superpowers/plans/2026-08-09-winter-interlude-executable-gates.md
if ($LASTEXITCODE -ne 0) { throw 'Post-review catalog diff check failed.' }
```

After all review-backed source edits are complete and the two tracked Tools
SHA-256 values are final, run this fence exactly once. It runs the 87-test gate
module once and full discovery once; do not start either command separately in
parallel or repeat either command against the same exact SHA pair:

```powershell
$pythonCommand = Get-Command python.exe -CommandType Application -ErrorAction Stop |
  Select-Object -First 1
if ($null -eq $pythonCommand -or
    [string]::IsNullOrWhiteSpace([string]$pythonCommand.Source)) {
  throw 'python.exe did not resolve to an application.'
}
$gateHashBefore = (
  Get-FileHash -Algorithm SHA256 -LiteralPath Tools/Run-WinterInterludeGate.ps1 `
    -ErrorAction Stop
).Hash
$testHashBefore = (
  Get-FileHash -Algorithm SHA256 -LiteralPath Tools/test_winter_interlude_gate.py `
    -ErrorAction Stop
).Hash
$catalogToken = '{0}-{1}' -f `
  $gateHashBefore.Substring(0, 12), $testHashBefore.Substring(0, 12)

function Invoke-ExactUnittestCapture {
  [CmdletBinding()]
  param(
    [Parameter(Mandatory = $true)]
    [string]$Label,
    [Parameter(Mandatory = $true)]
    [string[]]$Arguments,
    [Parameter(Mandatory = $true)]
    [string]$LogPath
  )

  $stdoutPath = "$LogPath.stdout.txt"
  $stderrPath = "$LogPath.stderr.txt"
  Remove-Item -LiteralPath $LogPath, $stdoutPath, $stderrPath `
    -Force -ErrorAction SilentlyContinue
  $process = Start-Process `
    -FilePath $pythonCommand.Source `
    -ArgumentList $Arguments `
    -WorkingDirectory (Get-Location).Path `
    -WindowStyle Hidden `
    -RedirectStandardOutput $stdoutPath `
    -RedirectStandardError $stderrPath `
    -Wait `
    -PassThru
  $exitCode = [int]$process.ExitCode
  $stdoutText = [string](
    Get-Content -Raw -LiteralPath $stdoutPath -ErrorAction Stop
  )
  $stderrText = [string](
    Get-Content -Raw -LiteralPath $stderrPath -ErrorAction Stop
  )
  $separator = ''
  if ($stdoutText.Length -gt 0 -and $stderrText.Length -gt 0 -and
      -not $stdoutText.EndsWith("`n", [StringComparison]::Ordinal)) {
    $separator = [Environment]::NewLine
  }
  $fullText = $stdoutText + $separator + $stderrText
  [IO.File]::WriteAllText(
    (Join-Path (Get-Location).Path $LogPath),
    $fullText,
    (New-Object Text.UTF8Encoding($false))
  )
  Get-Content -LiteralPath $LogPath -ErrorAction Stop | Out-Host
  [pscustomobject][ordered]@{
    Label = $Label
    ExitCode = $exitCode
    Text = $fullText
    LogPath = $LogPath
    LogSha256 = (
      Get-FileHash -Algorithm SHA256 -LiteralPath $LogPath -ErrorAction Stop
    ).Hash
  }
}

$moduleRun = Invoke-ExactUnittestCapture `
  -Label 'final gate module' `
  -Arguments ([string[]]@(
    '-m', 'unittest', 'Tools.test_winter_interlude_gate', '-v'
  )) `
  -LogPath (
    '.superpowers/sdd/task-7-5-final-module-87-{0}.txt' -f $catalogToken
  )
$moduleRan = [regex]::Matches(
  $moduleRun.Text,
  '(?m)^Ran ([0-9]+) tests in [0-9]+(?:\.[0-9]+)?s\r?$'
)
$moduleOk = [regex]::Matches($moduleRun.Text, '(?m)^OK\r?$')
$moduleTerminalLines = [string[]]@(
  $moduleRun.Text -split '\r?\n' | Where-Object { $_.Length -gt 0 }
)
if ($moduleRun.ExitCode -ne 0 -or
    $moduleRan.Count -ne 1 -or
    $moduleRan[0].Groups[1].Value -cne '87' -or
    $moduleOk.Count -ne 1 -or
    $moduleTerminalLines.Count -eq 0 -or
    $moduleTerminalLines[-1] -cne 'OK') {
  throw "Final gate module must exit 0 with exactly Ran 87 tests and one terminal OK; log: $($moduleRun.LogPath)"
}

$discoveryRun = Invoke-ExactUnittestCapture `
  -Label 'final full discovery' `
  -Arguments ([string[]]@(
    '-m', 'unittest', 'discover', '-s', 'Tools', '-p', 'test_*.py', '-v'
  )) `
  -LogPath (
    '.superpowers/sdd/task-7-5-final-discovery-339-{0}.txt' -f $catalogToken
  )
$discoveryRan = [regex]::Matches(
  $discoveryRun.Text,
  '(?m)^Ran ([0-9]+) tests in [0-9]+(?:\.[0-9]+)?s\r?$'
)
$discoveryCount = 0
$discoveryRanValid = ($discoveryRan.Count -eq 1)
if ($discoveryRanValid) {
  $discoveryRanValid = [int]::TryParse(
    $discoveryRan[0].Groups[1].Value,
    [Globalization.NumberStyles]::None,
    [Globalization.CultureInfo]::InvariantCulture,
    [ref]$discoveryCount
  )
}
$discoveryOk = [regex]::Matches($discoveryRun.Text, '(?m)^OK\r?$')
$discoveryTerminalLines = [string[]]@(
  $discoveryRun.Text -split '\r?\n' | Where-Object { $_.Length -gt 0 }
)
if ($discoveryRun.ExitCode -ne 0 -or
    -not $discoveryRanValid -or
    $discoveryCount -lt 339 -or
    $discoveryOk.Count -ne 1 -or
    $discoveryTerminalLines.Count -eq 0 -or
    $discoveryTerminalLines[-1] -cne 'OK') {
  throw "Full discovery must exit 0 with one Ran N tests line (N >= 339) and one terminal OK; log: $($discoveryRun.LogPath)"
}

$gateHashAfter = (
  Get-FileHash -Algorithm SHA256 -LiteralPath Tools/Run-WinterInterludeGate.ps1 `
    -ErrorAction Stop
).Hash
$testHashAfter = (
  Get-FileHash -Algorithm SHA256 -LiteralPath Tools/test_winter_interlude_gate.py `
    -ErrorAction Stop
).Hash
if ($gateHashAfter -cne $gateHashBefore -or
    $testHashAfter -cne $testHashBefore) {
  throw 'The authoritative Tools SHA pair changed during the catalog runs.'
}
Write-Output "FINAL_MODULE_LOG=$($moduleRun.LogPath)"
Write-Output "FINAL_MODULE_LOG_SHA256=$($moduleRun.LogSha256)"
Write-Output "FINAL_DISCOVERY_COUNT=$discoveryCount"
Write-Output "FINAL_DISCOVERY_LOG=$($discoveryRun.LogPath)"
Write-Output "FINAL_DISCOVERY_LOG_SHA256=$($discoveryRun.LogSha256)"
Write-Output "FINAL_GATE_SHA256=$gateHashAfter"
Write-Output "FINAL_GATE_TEST_SHA256=$testHashAfter"
```

Expected: both real exit codes are captured directly from their completed
processes before any output processing; both full logs are printed and hashed;
the module log contains exactly one `Ran 87 tests` and one terminal `OK`; the
discovery log contains exactly one `Ran N tests` with `N >= 339` and one
terminal `OK`; and the checkout-local physical Tools SHA pair is unchanged
across both runs. Here `$gateHashBefore`/`$testHashBefore` and their after-run
values are mutation tokens only within this one checkout; they are not the
portable catalog identity and must not be compared across LF/CRLF checkouts.
The earlier Task 6 `Ran 86 tests` and the initial pre-remediation Task 7 discovery's
exact `Ran 338 tests` remain historical observations whose ignored logs must
not be rewritten; only the post-review final catalog/floor is 87/339.

For each Critical or Important finding, add one focused public black-box regression to `Tools/test_winter_interlude_gate.py` (or retain the relevant story/source test), run it to a named RED, make the smallest fix inside the exact four-file range, and rerun that focused test GREEN. The authoritative Step 5D fence above is the only pre-amend long module/discovery run for the final Tools SHA pair. After it passes, execute only the staging and amend fence:

```powershell
git add -- Tools/Run-WinterInterludeGate.ps1 Tools/test_winter_interlude_gate.py Tools/test_governance_winter_interlude.py docs/superpowers/plans/2026-08-08-governance-winter-interlude.md
if ($LASTEXITCODE -ne 0) { throw 'Post-review staging failed.' }
$postReviewStaged = @(git diff --cached --name-only)
if ($LASTEXITCODE -ne 0) { throw 'Could not inspect post-review staging.' }
$allowedPostReviewPaths = @(
  'Tools/Run-WinterInterludeGate.ps1',
  'Tools/test_winter_interlude_gate.py',
  'Tools/test_governance_winter_interlude.py',
  'docs/superpowers/plans/2026-08-08-governance-winter-interlude.md'
)
if ($postReviewStaged.Count -eq 0 -or
    @($postReviewStaged | Where-Object { $_ -notin $allowedPostReviewPaths }).Count -ne 0) {
  throw "Unexpected post-review staged paths: $($postReviewStaged -join ', ')"
}
git diff --cached --check
if ($LASTEXITCODE -ne 0) { throw 'Post-review staged diff failed whitespace validation.' }
git commit --amend --no-edit
if ($LASTEXITCODE -ne 0) { throw 'Post-review amend failed.' }
```

After every amend, regardless of which allowed file changed, repeat Task 7
Steps 1, 2, 3, and 4. Step 1 overwrites the final-commit pointer with amended
HEAD; Steps 2 and 3 must use new GUID roots and overwrite the root pointers
only after validating fresh summaries bound to that exact SHA. Never reuse
runtime evidence from the pre-amend commit. Run Step 4 once to publish the new
immutable review input, obtain a fresh Spec review and then a different fresh
Standards review, and run Step 4 again to require `REVIEWS_READY=` concatenated
with the exact amended HEAD recorded in `$reviewCommit`. Repeat the whole
repair loop until both fresh decisions report C0/I0.

- [ ] **Step 6: Record the final asset/package conclusion**

Confirm and report: required or optional new art none; music/SFX none; portraits/animation/UI none; font unchanged; `game` and `old-game` unchanged; shipping package delta zero. Runtime evidence remains outside the repository under the preserved external run roots; ignored SHA/root pointers and RED/review logs remain untracked under `.superpowers/sdd`.

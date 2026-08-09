from __future__ import annotations

import contextlib
import ctypes
import json
import os
import re
import shutil
import threading
import subprocess
import tempfile
import time
import unittest
from collections.abc import Callable
from ctypes import wintypes
from dataclasses import dataclass
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

STRUCTURAL_SUITES = (
    "test_winter_interlude_state",
    "test_winter_interlude_routing",
    "test_winter_interlude_ending_invariance",
    "test_winter_interlude_route_matrix",
    "test_winter_interlude_mid_save",
)
TARGET = "game/governance_winter_interlude.rpy"


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


class WinterInterludeGateInterfaceTests(unittest.TestCase):
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
        valid_binding = run_gate(
            "-Gate", "Structural", "-ProjectRoot", "relative-project"
        )
        self.assertEqual(valid_binding.returncode, 1)
        self.assertIn("path identity", valid_binding.stderr.lower())
        self.assertNotIn("cannot validate argument", valid_binding.stderr.lower())

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
        self.trap_dir = self.temp_root / "trap-bin"
        self.trap_dir.mkdir()
        _compile_path_trap(self.trap_dir / "python.exe")
        self.child_record = self.temp_root / "child-started.txt"
        self.env = {
            "APPDATA": str(self.appdata),
            "PATH": str(self.trap_dir),
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
            source.index("# END LOOP 3.3-P2 STEP AND PROVISIONAL MANIFEST BUILDERS")
        ]
        self.assertEqual(
            5,
            manifests.count("New-VerifiedGateChildDirectory"),
        )
        self.assertNotIn("New-VerifiedChildDirectory", manifests)

        final_guards = source[
            source.index("function Assert-RunTreeDirectoryIdentities {") :
            source.index("# END LOOP 3.4-P2 FINAL PROJECT AND DIRECTORY RECHECKS")
        ]
        self.assertEqual(
            3,
            final_guards.count("Assert-ProtectedPlayerSaveState"),
        )

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

    def test_rejects_process_appdata_player_save_but_allows_its_sibling(self) -> None:
        protected = self.player_save / "inside-run"
        self.assert_path_rejected(self.invoke(str(protected)))
        self.assertFalse(protected.exists())

        allowed = self.appdata / "winter-gate-runs" / "run"
        result = self.invoke(str(allowed))
        self.assert_path_bootstrap_completed(result, allowed)

    def test_empty_or_missing_process_appdata_fails_closed(self) -> None:
        cases = ("", str(self.temp_root / "missing-process-appdata"))
        for index, appdata in enumerate(cases):
            with self.subTest(appdata=appdata):
                self.env["APPDATA"] = appdata
                run_root = self.external / f"bad-appdata-{index}"
                self.assert_path_rejected(self.invoke(str(run_root)))
                self.assertFalse(run_root.exists())

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
using Microsoft.Win32.SafeHandles;

internal static class RecordingChild
{
    private const int StdInputHandle = -10;
    private const int StdOutputHandle = -11;
    private const int StdErrorHandle = -12;
    private const uint FileTypeChar = 0x0002;
    private const uint JobObjectQuery = 0x0004;
    private const uint HandleFlagInherit = 0x00000001;
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
    [return: MarshalAs(UnmanagedType.Bool)]
    private static extern bool SetHandleInformation(
        IntPtr handle,
        uint mask,
        uint flags);

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
        WriteControlledDocument(
            control,
            step,
            arguments,
            inExpectedJob,
            inJob);
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
        record["structured_output_handle"] = Environment.GetEnvironmentVariable(
            "WINTER_GATE_STRUCTURED_OUTPUT_HANDLE");
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


def one_finding(rule: str = "test-rule") -> dict[str, object]:
    return {
        "path": TARGET,
        "line": 1,
        "rule": rule,
        "message": "controlled test finding",
    }


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
) -> tuple[subprocess.CompletedProcess[str], OSError | None]:
    if fixture.has_run:
        raise AssertionError("Each fake-project fixture supports one gate run.")
    fixture.has_run = True
    fixture._write_control(
        documents=passing_narrative_documents("batch"),
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
    replacement_error: OSError | None = None
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
        try:
            _move_file_replace_existing(replacement, fixture.python_exe)
        except OSError as error:
            replacement_error = error
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
    return (
        subprocess.CompletedProcess(command, gate_process.returncode, stdout, stderr),
        replacement_error,
    )


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
        self.assertIn("FirstMissingRequiredFilePath", dependency)
        self.assertIn("$Step.DependencyLease.AssertStable()", dependency)
        self.assertNotIn("ExecutableIdentity", dependency)
        self.assertNotIn("RequiredFileIdentities", dependency)
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
            source.index("private static StepDependencyFile AcquireStepDependencyFile(") :
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
        footer = source[source.rindex("$script:StructuredOutputReservations = $null") :]
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

        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertEqual(6, len(self.fixture.records()))
        summary = self.fixture.summary()
        self.assertEqual("passed", summary["status"])
        self.assertIsNone(summary["failure_kind"])
        self.assertIsNone(summary["error"])
        self.assertEqual(head[:12], summary["head_token"])
        self.assertEqual(6, len(summary["steps"]))

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
            (
                "nan",
                nan,
                "expected_value",
                nan.index("NaN"),
            ),
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
            (
                "trailing-comma",
                '{"a":1,}',
                "object_property_name",
                7,
            ),
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
                    json.dumps("😀", ensure_ascii=False),
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
                    records = fixture.records()
                    summary = fixture.summary()
                    failed = summary["steps"][-1]
                    diagnostic = {
                        "expected_ordinal": failing_ordinal,
                        "records": records,
                        "steps": summary["steps"],
                        "failed": failed,
                        "stderr": completed.stderr,
                    }
                    self.assertEqual(
                        len(records), failing_ordinal, diagnostic
                    )
                    self.assertEqual(
                        len(summary["steps"]), failing_ordinal, diagnostic
                    )
                    self.assertEqual(
                        failed["failure_kind"], "process", diagnostic
                    )
                    self.assertEqual(failed["exit_code"], 23, diagnostic)
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


class WinterInterludeGateMigrationTests(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()

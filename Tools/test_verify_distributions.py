#!/usr/bin/env python3
"""Tests for the built-distribution release verifier."""

from contextlib import redirect_stderr, redirect_stdout
import hashlib
import io
import os
from pathlib import Path
import pickle
import stat
import struct
import subprocess
import tempfile
import unittest
from unittest import mock
import warnings
import zipfile
import zlib

from Tools import verify_distributions as verifier
from Tools.test_release_contract import (
    APPROVED_ANDROID_API,
    APPROVED_ANDROID_PACKAGE,
    APPROVED_PACKAGE_EXCLUSIONS,
    APPROVED_VERSION,
    PROTECTED_DYNAMIC_UI_PATHS,
)


ROOT = Path(__file__).resolve().parents[1]
WINDOWS_ROOT = "CourtOfShadows-3.10-win"
CURRENT_CODE = 2_000_000_000
PREVIOUS_CODE = 1_785_682_834
CERTIFICATE = "5fcb5758461427026b13ecf987e86ad11e13170dc60386d42e4c2f20a93b3708"
ALLOWED_UNPREFIXED_ANDROID_ASSETS = {
    "assets/android-downloading.jpg",
    "assets/android-presplash.png",
    "assets/dexopt/baseline.prof",
    "assets/dexopt/baseline.profm",
    "assets/private.mp3",
}
RPYC_MAGIC = b"_2025-07-06"


BADGING = f"""package: name='{APPROVED_ANDROID_PACKAGE}' versionCode='{CURRENT_CODE}' versionName='{APPROVED_VERSION}' platformBuildVersionName='16' platformBuildVersionCode='36' compileSdkVersion='36'
sdkVersion:'21'
targetSdkVersion:'{APPROVED_ANDROID_API}'
application-label:'权谋之庭'
"""

PREVIOUS_BADGING = f"""package: name='{APPROVED_ANDROID_PACKAGE}' versionCode='{PREVIOUS_CODE}' versionName='3.9.2' platformBuildVersionCode='36'
sdkVersion:'21'
targetSdkVersion:'{APPROVED_ANDROID_API}'
"""

XMLTREE = """E: manifest (line=2)
  E: application (line=22)
    E: activity (line=45)
      A: android:name(0x01010003)="org.renpy.android.UnorientedWrapper" (Raw: "org.renpy.android.UnorientedWrapper")
    E: activity-alias (line=48)
      A: android:name(0x01010003)="org.renpy.android.WrapperAlias" (Raw: "org.renpy.android.WrapperAlias")
      A: android:screenOrientation(0x0101001e)=(type 0x10)0x1
    E: activity (line=52)
      A: android:name(0x01010003)="org.renpy.android.ConsentActivity" (Raw: "org.renpy.android.ConsentActivity")
      A: android:screenOrientation(0x0101001e)=(type 0x10)0x6
    E: activity (line=64)
      A: android:name(0x01010003)="org.renpy.android.PythonSDLActivity" (Raw: "org.renpy.android.PythonSDLActivity")
      A: android:screenOrientation(0x0101001e)=(type 0x10)0x6
"""

SIGNER = f"""Verifies
Verified using v1 scheme (JAR signing): true
Verified using v2 scheme (APK Signature Scheme v2): true
Verified using v3 scheme (APK Signature Scheme v3): false
Verified using v4 scheme (APK Signature Scheme v4): false
Number of signers: 1
Signer #1 certificate SHA-256 digest: {CERTIFICATE}
WARNING: META-INF/app-metadata.properties not protected by signature.
"""


def _representative(pattern: str) -> str:
    if pattern.endswith("/**"):
        return pattern[:-2] + "sample.bin"
    return pattern.replace("*", "sample")


def _android_asset_name(path: str) -> str:
    return "assets/" + "/".join("x-" + part for part in path.split("/"))


def _write_zip(path: Path, names: set[str] | list[str]) -> None:
    with zipfile.ZipFile(path, "w", zipfile.ZIP_STORED) as archive:
        for name in sorted(names):
            archive.writestr(name, ("payload:" + name).encode("utf-8"))


def _write_zip_entries(path: Path, entries: dict[str, bytes]) -> None:
    with zipfile.ZipFile(path, "w", zipfile.ZIP_STORED) as archive:
        for name, content in sorted(entries.items()):
            archive.writestr(name, content)


def _write_zip_with_unix_type(
    path: Path,
    names: set[str] | list[str],
    typed_name: str,
    file_type: int,
) -> None:
    with zipfile.ZipFile(path, "w", zipfile.ZIP_STORED) as archive:
        for name in sorted(names):
            content = ("payload:" + name).encode("utf-8")
            if name == typed_name:
                info = zipfile.ZipInfo(name)
                info.create_system = 3
                info.external_attr = (file_type | 0o777) << 16
                archive.writestr(info, content)
            else:
                archive.writestr(name, content)


def _rpc2_from_pickles(
    source: bytes, slot_1_pickle: bytes, slot_2_pickle: bytes | None = None
) -> bytes:
    slot_2_pickle = slot_1_pickle if slot_2_pickle is None else slot_2_pickle
    compressed_1 = zlib.compress(slot_1_pickle, 3)
    compressed_2 = zlib.compress(slot_2_pickle, 3)
    header_size = len(b"RENPY RPC2") + 3 * 12
    slot_1_start = header_size
    slot_2_start = slot_1_start + len(compressed_1)
    header = b"".join(
        (
            b"RENPY RPC2",
            struct.pack("<III", 1, slot_1_start, len(compressed_1)),
            struct.pack("<III", 2, slot_2_start, len(compressed_2)),
            struct.pack("<III", 0, 0, 0),
        )
    )
    trailer = hashlib.md5(source + RPYC_MAGIC).digest()
    return header + compressed_1 + compressed_2 + trailer


def _rpc2_common(
    source: bytes,
    *,
    name_version: int = 325_472_330,
    name_serial: int = 16,
    screen_serial: int = 1_785_666_150_901_563,
    line: int = 24,
    name_serials: tuple[int, ...] | None = None,
    screen_serials: tuple[int, ...] | None = None,
    slot_2_line: int | None = None,
) -> bytes:
    node_serials = (name_serial,) if name_serials is None else name_serials
    sl_serials = (screen_serial,) if screen_serials is None else screen_serials

    def make_pickle(linenumber: int) -> bytes:
        return pickle.dumps(
            {
                "nodes": [
                    {
                        "name_version": name_version,
                        "name_serial": serial,
                    }
                    for serial in node_serials
                ],
                "screens": [
                    {"serial": serial, "linenumber": linenumber}
                    for serial in sl_serials
                ],
            },
            protocol=4,
        )

    slot_1 = make_pickle(line)
    slot_2 = make_pickle(line if slot_2_line is None else slot_2_line)
    return _rpc2_from_pickles(source, slot_1, slot_2)


def _expected_runtime_fingerprint(path: Path) -> tuple[int, str]:
    members = verifier.inspect_archive(path)
    compiled_contract = verifier.inspect_compiled_common_contract(
        path, members, require_release_contract=False
    )
    return verifier.windows_runtime_fingerprint(members, compiled_contract)


class FakeAndroidRunner:
    def __init__(
        self,
        zipalign_code: int = 0,
        signer_code: int = 0,
        raise_tool: str | None = None,
    ) -> None:
        self.calls: list[list[str]] = []
        self.zipalign_code = zipalign_code
        self.signer_code = signer_code
        self.raise_tool = raise_tool

    def __call__(self, command: list[str]) -> subprocess.CompletedProcess[str]:
        self.calls.append(command)
        tool = Path(command[0]).name.lower()
        if tool == self.raise_tool:
            raise OSError("tool could not start")
        if tool == "aapt.exe" and "badging" in command:
            output = PREVIOUS_BADGING if "previous" in command[-1] else BADGING
            return subprocess.CompletedProcess(command, 0, output, "")
        if tool == "aapt.exe" and "xmltree" in command:
            return subprocess.CompletedProcess(command, 0, XMLTREE, "")
        if tool == "apksigner.bat":
            return subprocess.CompletedProcess(
                command, self.signer_code, SIGNER, "signer stderr"
            )
        if tool == "zipalign.exe":
            return subprocess.CompletedProcess(
                command, self.zipalign_code, "", "alignment failed"
            )
        raise AssertionError(f"unexpected command: {command!r}")


class VerifierTestCase(unittest.TestCase):
    def function(self, name: str):
        value = getattr(verifier, name, None)
        self.assertTrue(callable(value), f"missing verifier function: {name}")
        return value

    def error_type(self):
        value = getattr(verifier, "VerificationError", None)
        self.assertTrue(
            isinstance(value, type) and issubclass(value, Exception),
            "missing VerificationError",
        )
        return value


class DistributionVerifierBootstrapTests(unittest.TestCase):
    def test_verifier_module_exists(self) -> None:
        self.assertTrue((ROOT / "Tools" / "verify_distributions.py").is_file())


class PathNormalizationTests(VerifierTestCase):
    def test_windows_normalization_requires_and_strips_exact_root(self) -> None:
        normalize = self.function("normalize_windows_payload")
        members = [
            (f"{WINDOWS_ROOT}/CourtOfShadows.exe", True),
            (f"{WINDOWS_ROOT}/game/script.rpyc", True),
        ]
        self.assertEqual(
            normalize(members), {"CourtOfShadows.exe", "game/script.rpyc"}
        )

        inspect_archive = self.function("inspect_archive")
        error = self.error_type()
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "extra-empty-root.zip"
            _write_zip(
                path,
                [f"{WINDOWS_ROOT}/CourtOfShadows.exe", "extra-empty-root/"],
            )
            with self.assertRaises(error):
                normalize(inspect_archive(path))

    def test_windows_normalization_rejects_wrong_or_multiple_roots(self) -> None:
        normalize = self.function("normalize_windows_payload")
        error = self.error_type()
        cases = (
            [("Wrong/CourtOfShadows.exe", True)],
            [
                (f"{WINDOWS_ROOT}/CourtOfShadows.exe", True),
                ("second/file.txt", True),
            ],
        )
        for members in cases:
            with self.subTest(members=members), self.assertRaises(error):
                normalize(members)

    def test_android_normalization_removes_each_x_prefix(self) -> None:
        normalize = self.function("normalize_android_payload")
        members = [
            ("assets/x-game/x-images/x-ui/x-panel_frame.png", False),
            ("assets/android-presplash.png", False),
            ("res/Ms.png", False),
            ("res/mS.png", False),
            ("classes.dex", False),
        ]
        self.assertEqual(
            normalize(members), {"game/images/ui/panel_frame.png"}
        )

    def test_android_normalization_repairs_cp437_decoded_utf8_name(self) -> None:
        normalize = self.function("normalize_android_payload")
        error = self.error_type()
        original = "assets/x-TapTap_v3.5_更新公告.md"
        mangled = original.encode("utf-8").decode("cp437")
        self.assertEqual(
            normalize([(mangled, False)]), {"TapTap_v3.5_更新公告.md"}
        )
        self.assertEqual(
            normalize([(original, True)]), {"TapTap_v3.5_更新公告.md"}
        )
        with self.assertRaises(error):
            normalize([(mangled, False), (original, True)])

    def test_android_normalization_rejects_partial_x_prefix_tree(self) -> None:
        normalize = self.function("normalize_android_payload")
        error = self.error_type()
        cases = (
            [("assets/x-game/images/x-ui/x-panel_frame.png", False)],
            [
                ("assets/x-game/x-File.rpyc", False),
                ("assets/x-game/x-file.rpyc", False),
            ],
        )
        for members in cases:
            with self.subTest(members=members), self.assertRaises(error):
                normalize(members)

    def test_android_normalization_rejects_logical_file_ancestor(self) -> None:
        inspect_archive = self.function("inspect_archive")
        normalize = self.function("normalize_android_payload")
        error = self.error_type()
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "logical-ancestor.apk"
            _write_zip(
                path,
                ["assets/x-Game", "assets/x-game/x-child.rpyc"],
            )
            members = inspect_archive(
                path, casefold_collisions=False, windows_paths=False
            )
            with self.assertRaises(error):
                normalize(members)

        self.assertEqual(
            normalize(
                [
                    ("assets/x-renpy2", False),
                    ("assets/x-renpy/x-child.rpyc", False),
                    ("assets/x-foo-bar", False),
                    ("assets/x-foo/x-child.rpyc", False),
                ]
            ),
            {"renpy2", "renpy/child.rpyc", "foo-bar", "foo/child.rpyc"},
        )

    def test_android_unprefixed_asset_allowlist_and_policy_candidates(self) -> None:
        normalize = self.function("normalize_android_payload")
        policy_candidates = self.function("android_policy_candidates")
        error = self.error_type()
        members = [
            *((path, False) for path in ALLOWED_UNPREFIXED_ANDROID_ASSETS),
            ("assets/x-game/x-script.rpyc", False),
            ("res/Ms.png", False),
            ("META-INF/MANIFEST.MF", False),
            ("README.txt", False),
        ]
        self.assertEqual(normalize(members), {"game/script.rpyc"})
        self.assertEqual(
            policy_candidates(members),
            {
                *(path[len("assets/") :] for path in ALLOWED_UNPREFIXED_ANDROID_ASSETS),
                "game/script.rpyc",
                "res/Ms.png",
                "META-INF/MANIFEST.MF",
                "README.txt",
            },
        )
        with self.assertRaises(error):
            normalize([("assets/README.txt", False)])


class ArchiveIntegrityTests(VerifierTestCase):
    def test_archive_rejects_unsafe_or_colliding_member_names(self) -> None:
        inspect_archive = self.function("inspect_archive")
        error = self.error_type()
        cases = {
            "absolute": ["/absolute.txt"],
            "drive": ["C:/absolute.txt"],
            "traversal": ["root/../escape.txt"],
            "backslash": ["root/escape.txt"],
            "case collision": ["root/File.txt", "root/file.txt"],
        }
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            for label, names in cases.items():
                path = directory / f"{label}.zip"
                _write_zip(path, names)
                if label == "backslash":
                    path.write_bytes(
                        path.read_bytes().replace(
                            b"root/escape.txt", b"root\\escape.txt"
                        )
                    )
                with self.subTest(label=label), self.assertRaises(error):
                    inspect_archive(path)

    def test_archive_rejects_duplicate_members(self) -> None:
        inspect_archive = self.function("inspect_archive")
        error = self.error_type()
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "duplicate.zip"
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", UserWarning)
                with zipfile.ZipFile(path, "w", zipfile.ZIP_STORED) as archive:
                    archive.writestr("same.txt", b"first")
                    archive.writestr("same.txt", b"second")
            with self.assertRaises(error):
                inspect_archive(path)

    def test_archive_rejects_crc_corruption(self) -> None:
        inspect_archive = self.function("inspect_archive")
        error = self.error_type()
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "corrupt.zip"
            marker = b"unique-crc-marker"
            with zipfile.ZipFile(path, "w", zipfile.ZIP_STORED) as archive:
                archive.writestr("payload.bin", marker)
            data = path.read_bytes()
            self.assertEqual(data.count(marker), 1)
            path.write_bytes(data.replace(marker, b"broken-crc-marker", 1))
            with self.assertRaises(error):
                inspect_archive(path)

    def test_archive_rejects_file_and_directory_at_same_path(self) -> None:
        inspect_archive = self.function("inspect_archive")
        error = self.error_type()
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            conflict = directory / "conflict.zip"
            _write_zip(conflict, ["root/foo", "root/foo/"])
            with self.assertRaises(error):
                inspect_archive(conflict)

            valid = directory / "valid.zip"
            _write_zip(valid, ["root/foo/", "root/foo/child.txt"])
            inspect_archive(valid)

    def test_archive_rejects_case_sensitive_raw_file_ancestor(self) -> None:
        inspect_archive = self.function("inspect_archive")
        error = self.error_type()
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            conflict = directory / "android-conflict.apk"
            _write_zip(conflict, ["assets", "assets/x-game/x-script.rpyc"])
            with self.assertRaises(error):
                inspect_archive(
                    conflict, casefold_collisions=False, windows_paths=False
                )

            case_distinct = directory / "android-case-distinct.apk"
            _write_zip(
                case_distinct,
                ["Assets", "assets/x-game/x-script.rpyc"],
            )
            inspect_archive(
                case_distinct, casefold_collisions=False, windows_paths=False
            )

    def test_archive_ancestor_check_is_component_aware(self) -> None:
        inspect_archive = self.function("inspect_archive")
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "component-prefixes.zip"
            _write_zip(
                path,
                [
                    "root/renpy2",
                    "root/renpy/child.py",
                    "root/foo-bar",
                    "root/foo/child.txt",
                ],
            )
            inspect_archive(path)

    def test_windows_member_name_rules_are_platform_scoped(self) -> None:
        inspect_archive = self.function("inspect_archive")
        error = self.error_type()
        invalid_components = (
            "panel_frame.png.",
            "panel_frame.png ",
            "panel:frame.png",
            "panel<frame.png",
            "panel>frame.png",
            'panel"frame.png',
            "panel|frame.png",
            "panel?frame.png",
            "panel*frame.png",
            "bad\x01name.bin",
            "NUL/child.bin",
            "CON.txt",
            "COM1.log",
        )
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            for index, component in enumerate(invalid_components):
                with self.subTest(component=repr(component)):
                    path = directory / f"invalid-{index}.zip"
                    _write_zip(path, [f"root/{component}"])
                    with self.assertRaises(error):
                        inspect_archive(path, windows_paths=True)

            valid = directory / "valid-windows.zip"
            _write_zip(
                valid,
                [
                    "root/middle space.txt",
                    "root/middle.dot.name",
                    "root/COM10",
                    "root/CONSOLE",
                    "root/AUXILIARY",
                ],
            )
            inspect_archive(valid, windows_paths=True)

            android = directory / "valid-android.apk"
            _write_zip(android, ["assets/x-game/x-panel:frame.png"])
            members = inspect_archive(
                android,
                casefold_collisions=False,
                windows_paths=False,
            )
            self.assertEqual(
                self.function("normalize_android_payload")(members),
                {"game/panel:frame.png"},
            )

    def test_archive_rejects_unsupported_or_mismatched_unix_types(self) -> None:
        inspect_archive = self.function("inspect_archive")
        error = self.error_type()
        invalid = (
            ("symlink", "root/link", stat.S_IFLNK),
            ("fifo", "root/fifo", stat.S_IFIFO),
            ("socket", "root/socket", stat.S_IFSOCK),
            ("block device", "root/block", stat.S_IFBLK),
            ("character device", "root/character", stat.S_IFCHR),
            ("regular marked directory", "root/wrong-dir/", stat.S_IFREG),
            ("directory missing slash", "root/wrong-file", stat.S_IFDIR),
        )
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            for index, (label, name, file_type) in enumerate(invalid):
                with self.subTest(label=label):
                    path = directory / f"invalid-type-{index}.zip"
                    _write_zip_with_unix_type(path, [name], name, file_type)
                    with self.assertRaises(error):
                        inspect_archive(path)

            valid = directory / "valid-types.zip"
            with zipfile.ZipFile(valid, "w", zipfile.ZIP_STORED) as archive:
                regular = zipfile.ZipInfo("root/regular.bin")
                regular.create_system = 3
                regular.external_attr = (stat.S_IFREG | 0o644) << 16
                archive.writestr(regular, b"regular")

                explicit_directory = zipfile.ZipInfo("root/directory/")
                explicit_directory.create_system = 3
                explicit_directory.external_attr = (stat.S_IFDIR | 0o755) << 16
                archive.writestr(explicit_directory, b"")

                unknown = zipfile.ZipInfo("root/unknown.bin")
                unknown.create_system = 3
                unknown.external_attr = 0o644 << 16
                archive.writestr(unknown, b"unknown")
            inspect_archive(valid)


class WindowsRuntimeFingerprintTests(VerifierTestCase):
    @staticmethod
    def _entries() -> dict[str, bytes]:
        common_source = b"# synthetic Ren'Py common source\n"
        return {
            f"{WINDOWS_ROOT}/CourtOfShadows.exe": b"launcher-exe",
            f"{WINDOWS_ROOT}/CourtOfShadows.py": b"launcher-python",
            f"{WINDOWS_ROOT}/renpy/__init__.py": b"init-module",
            f"{WINDOWS_ROOT}/renpy/error.py": b"error-module",
            f"{WINDOWS_ROOT}/renpy/common/00console.rpy": common_source,
            f"{WINDOWS_ROOT}/renpy/common/00console.rpyc": _rpc2_common(
                common_source
            ),
            f"{WINDOWS_ROOT}/lib/python3.12/os.py": b"stdlib-module",
            f"{WINDOWS_ROOT}/game/script.rpyc": b"not-runtime",
        }

    def _validate_runtime_archive(
        self, path: Path, expected_count: int, expected_digest: str
    ) -> list[str]:
        try:
            members = verifier.inspect_archive(path)
            compiled_contract = verifier.inspect_compiled_common_contract(
                path, members, require_release_contract=False
            )
        except verifier.VerificationError as exc:
            return [f"compiled common contract: {exc}"]
        return verifier.validate_windows_runtime(
            members,
            compiled_common_contract=compiled_contract,
            expected_count=expected_count,
            expected_digest=expected_digest,
        )

    def test_complete_runtime_fingerprint_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "complete.zip"
            _write_zip_entries(path, self._entries())
            expected_count, expected_digest = _expected_runtime_fingerprint(path)
            self.assertEqual(
                self._validate_runtime_archive(
                    path, expected_count, expected_digest
                ),
                [],
            )

    def test_runtime_fingerprint_rejects_missing_module(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "runtime.zip"
            entries = self._entries()
            _write_zip_entries(path, entries)
            expected_count, expected_digest = _expected_runtime_fingerprint(path)
            del entries[f"{WINDOWS_ROOT}/renpy/error.py"]
            _write_zip_entries(path, entries)
            errors = self._validate_runtime_archive(
                path, expected_count, expected_digest
            )
            self.assertIn("runtime fingerprint", "\n".join(errors).lower())

    def test_runtime_fingerprint_rejects_extra_runtime_file(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "runtime.zip"
            base_entries = self._entries()
            _write_zip_entries(path, base_entries)
            expected_count, expected_digest = _expected_runtime_fingerprint(path)
            junk_paths = (
                "renpy/runtime-junk.py",
                "RenPy/runtime-junk.py",
                "LiB/runtime-junk.dll",
            )
            for junk_path in junk_paths:
                with self.subTest(junk_path=junk_path):
                    changed = dict(base_entries)
                    changed[f"{WINDOWS_ROOT}/{junk_path}"] = b"junk"
                    _write_zip_entries(path, changed)
                    errors = self._validate_runtime_archive(
                        path, expected_count, expected_digest
                    )
                    self.assertIn(
                        "runtime fingerprint", "\n".join(errors).lower()
                    )

    def test_runtime_fingerprint_rejects_changed_size_or_crc(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "runtime.zip"
            base_entries = self._entries()
            _write_zip_entries(path, base_entries)
            expected_count, expected_digest = _expected_runtime_fingerprint(path)
            error_path = f"{WINDOWS_ROOT}/renpy/error.py"
            mutations = {
                "same-size CRC change": b"other-module",
                "size and CRC change": b"longer-error-module",
            }
            for label, content in mutations.items():
                with self.subTest(label=label):
                    changed = dict(base_entries)
                    changed[error_path] = content
                    _write_zip_entries(path, changed)
                    errors = self._validate_runtime_archive(
                        path, expected_count, expected_digest
                    )
                    self.assertIn(
                        "runtime fingerprint", "\n".join(errors).lower()
                    )

    def test_runtime_fingerprint_normalizes_compiler_time_identifiers(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "runtime.zip"
            base_entries = self._entries()
            _write_zip_entries(path, base_entries)
            expected_count, expected_digest = _expected_runtime_fingerprint(path)
            changed = dict(base_entries)
            common_source = changed[
                f"{WINDOWS_ROOT}/renpy/common/00console.rpy"
            ]
            changed[f"{WINDOWS_ROOT}/renpy/common/00console.rpyc"] = (
                _rpc2_common(
                    common_source,
                    name_version=325_572_330,
                    screen_serial=1_785_667_150_901_563,
                )
            )
            _write_zip_entries(path, changed)
            self.assertEqual(
                self._validate_runtime_archive(
                    path, expected_count, expected_digest
                ),
                [],
            )

    def test_runtime_fingerprint_rejects_compiled_common_body_change(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "runtime.zip"
            base_entries = self._entries()
            _write_zip_entries(path, base_entries)
            expected_count, expected_digest = _expected_runtime_fingerprint(path)
            changed = dict(base_entries)
            common_source = changed[
                f"{WINDOWS_ROOT}/renpy/common/00console.rpy"
            ]
            changed[f"{WINDOWS_ROOT}/renpy/common/00console.rpyc"] = (
                _rpc2_common(common_source, line=25)
            )
            _write_zip_entries(path, changed)
            errors = self._validate_runtime_archive(
                path, expected_count, expected_digest
            )
            self.assertIn("runtime fingerprint", "\n".join(errors).lower())

    def test_runtime_fingerprint_rejects_compiled_common_source_md5_change(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "runtime.zip"
            base_entries = self._entries()
            _write_zip_entries(path, base_entries)
            expected_count, expected_digest = _expected_runtime_fingerprint(path)
            changed = dict(base_entries)
            different_source = b"# different synthetic common source\n"
            changed[f"{WINDOWS_ROOT}/renpy/common/00console.rpyc"] = (
                _rpc2_common(different_source)
            )
            _write_zip_entries(path, changed)
            errors = self._validate_runtime_archive(
                path, expected_count, expected_digest
            )
            self.assertIn("source md5", "\n".join(errors).lower())

    def test_compiled_common_contract_rejects_malformed_rpc2(self) -> None:
        source_path = f"{WINDOWS_ROOT}/renpy/common/00console.rpy"
        compiled_path = source_path + "c"
        error = self.error_type()
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "runtime.zip"
            base_entries = self._entries()
            source = base_entries[source_path]
            valid = base_entries[compiled_path]

            bad_header = b"BROKEN RPC2" + valid[len(b"RENPY RPC2") :]
            bad_table = bytearray(valid)
            slot_2, slot_2_start, slot_2_length = struct.unpack_from(
                "<III", bad_table, len(b"RENPY RPC2") + 12
            )
            struct.pack_into(
                "<III",
                bad_table,
                len(b"RENPY RPC2") + 12,
                slot_2,
                slot_2_start + 1,
                slot_2_length,
            )
            bad_zlib = bytearray(valid)
            bad_zlib[len(b"RENPY RPC2") + 3 * 12] ^= 0xFF
            trailing_pickle = pickle.dumps({"value": 1}, protocol=4) + b"junk"
            malformed = {
                "header": bad_header,
                "slot table": bytes(bad_table),
                "zlib": bytes(bad_zlib),
                "slot disagreement": _rpc2_common(source, slot_2_line=25),
                "pickle trailing bytes": _rpc2_from_pickles(
                    source, trailing_pickle
                ),
            }
            for label, payload in malformed.items():
                with self.subTest(label=label):
                    changed = dict(base_entries)
                    changed[compiled_path] = payload
                    _write_zip_entries(path, changed)
                    members = verifier.inspect_archive(path)
                    with self.assertRaises(error):
                        verifier.inspect_compiled_common_contract(
                            path, members, require_release_contract=False
                        )

    def test_compiled_common_contract_requires_one_source(self) -> None:
        source_path = f"{WINDOWS_ROOT}/renpy/common/00console.rpy"
        error = self.error_type()
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "runtime.zip"
            base_entries = self._entries()
            variants = {
                "missing": {
                    name: payload
                    for name, payload in base_entries.items()
                    if name != source_path
                },
                "ambiguous": {
                    **base_entries,
                    f"{WINDOWS_ROOT}/renpy/common/00console_ren.py": (
                        base_entries[source_path]
                    ),
                },
            }
            for label, entries in variants.items():
                with self.subTest(label=label):
                    _write_zip_entries(path, entries)
                    members = verifier.inspect_archive(path)
                    with self.assertRaises(error):
                        verifier.inspect_compiled_common_contract(
                            path, members, require_release_contract=False
                        )

    def test_runtime_fingerprint_keeps_core_name_serial_strict(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "runtime.zip"
            base_entries = self._entries()
            _write_zip_entries(path, base_entries)
            expected_count, expected_digest = _expected_runtime_fingerprint(path)
            source_path = f"{WINDOWS_ROOT}/renpy/common/00console.rpy"
            changed = dict(base_entries)
            changed[source_path + "c"] = _rpc2_common(
                changed[source_path], name_serial=17
            )
            _write_zip_entries(path, changed)
            errors = self._validate_runtime_archive(
                path, expected_count, expected_digest
            )
            self.assertIn("runtime fingerprint", "\n".join(errors).lower())

    def test_runtime_fingerprint_preserves_screen_serial_offsets(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "runtime.zip"
            source_path = f"{WINDOWS_ROOT}/renpy/common/00console.rpy"
            compiled_path = source_path + "c"
            base_entries = self._entries()
            source = base_entries[source_path]
            base_entries[compiled_path] = _rpc2_common(
                source,
                screen_serials=(
                    1_785_666_150_901_563,
                    1_785_666_150_901_565,
                ),
            )
            _write_zip_entries(path, base_entries)
            expected_count, expected_digest = _expected_runtime_fingerprint(path)

            shifted = dict(base_entries)
            shifted[compiled_path] = _rpc2_common(
                source,
                name_version=325_572_330,
                screen_serials=(
                    1_785_667_150_901_563,
                    1_785_667_150_901_565,
                ),
            )
            _write_zip_entries(path, shifted)
            self.assertEqual(
                self._validate_runtime_archive(
                    path, expected_count, expected_digest
                ),
                [],
            )

            shifted[compiled_path] = _rpc2_common(
                source,
                name_version=325_572_330,
                screen_serials=(
                    1_785_667_150_901_563,
                    1_785_667_150_901_566,
                ),
            )
            _write_zip_entries(path, shifted)
            errors = self._validate_runtime_archive(
                path, expected_count, expected_digest
            )
            self.assertIn("runtime fingerprint", "\n".join(errors).lower())

    def test_compiled_common_contract_allows_screen_serial_bucket_crossing(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "runtime.zip"
            source_path = f"{WINDOWS_ROOT}/renpy/common/00console.rpy"
            compiled_path = source_path + "c"
            entries = self._entries()
            entries[compiled_path] = _rpc2_common(
                entries[source_path],
                screen_serials=(
                    1_785_666_150_909_998,
                    1_785_666_150_910_001,
                ),
            )
            _write_zip_entries(path, entries)
            members = verifier.inspect_archive(path)
            contract = verifier.inspect_compiled_common_contract(
                path, members, require_release_contract=False
            )
            self.assertIn("renpy/common/00console.rpyc", contract)

    def test_runtime_fingerprint_preserves_module_name_serial_offsets(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "runtime.zip"
            base_entries = self._entries()
            module_source_path = (
                f"{WINDOWS_ROOT}/renpy/common/_developer/example.rpym"
            )
            module_compiled_path = module_source_path + "c"
            module_source = b"# synthetic developer module\n"
            base_entries[module_source_path] = module_source
            base_entries[module_compiled_path] = _rpc2_common(
                module_source,
                name_serials=(1607, 1608, 1610),
                screen_serial=1_785_666_150_906_811,
            )
            _write_zip_entries(path, base_entries)
            expected_count, expected_digest = _expected_runtime_fingerprint(path)

            shifted = dict(base_entries)
            shifted[module_compiled_path] = _rpc2_common(
                module_source,
                name_serials=(1707, 1708, 1710),
                screen_serial=1_785_666_150_906_811,
            )
            _write_zip_entries(path, shifted)
            self.assertEqual(
                self._validate_runtime_archive(
                    path, expected_count, expected_digest
                ),
                [],
            )

            shifted[module_compiled_path] = _rpc2_common(
                module_source,
                name_serials=(1707, 1709, 1710),
                screen_serial=1_785_666_150_906_811,
            )
            _write_zip_entries(path, shifted)
            errors = self._validate_runtime_archive(
                path, expected_count, expected_digest
            )
            self.assertIn("runtime fingerprint", "\n".join(errors).lower())

    def test_runtime_fingerprint_rejects_same_count_common_rename(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "runtime.zip"
            base_entries = self._entries()
            _write_zip_entries(path, base_entries)
            expected_count, expected_digest = _expected_runtime_fingerprint(path)
            source_path = f"{WINDOWS_ROOT}/renpy/common/00console.rpy"
            compiled_path = source_path + "c"
            changed = dict(base_entries)
            source = changed.pop(source_path)
            compiled = changed.pop(compiled_path)
            renamed_source = f"{WINDOWS_ROOT}/renpy/common/00renamed.rpy"
            changed[renamed_source] = source
            changed[renamed_source + "c"] = compiled
            _write_zip_entries(path, changed)
            errors = self._validate_runtime_archive(
                path, expected_count, expected_digest
            )
            self.assertIn("runtime fingerprint", "\n".join(errors).lower())

class PayloadPolicyTests(VerifierTestCase):
    def test_every_approved_exclusion_category_is_detected(self) -> None:
        find_forbidden = self.function("find_forbidden_payloads")
        paths = {_representative(pattern) for pattern in APPROVED_PACKAGE_EXCLUSIONS}
        matches = find_forbidden(paths)
        self.assertEqual(set(matches), set(APPROVED_PACKAGE_EXCLUSIONS))
        self.assertEqual(
            {path for matched in matches.values() for path in matched}, paths
        )

    def test_payload_contract_rejects_android_readme_and_test_rpyc(self) -> None:
        validate = self.function("validate_payload")
        paths = {"README.txt", "game/script.rpyc", "game/test_game.rpyc"}
        errors = validate(
            paths,
            platform="android",
            expected_rpycs={"game/script.rpyc"},
            protected_paths=set(),
        )
        joined = "\n".join(errors)
        self.assertIn("README.txt", joined)
        self.assertIn("game/test_game.rpyc", joined)

    def test_payload_contract_requires_exact_rpyc_set(self) -> None:
        validate = self.function("validate_payload")
        errors = validate(
            {"README.txt", "game/script.rpyc", "game/extra.rpyc"},
            platform="windows",
            expected_rpycs={"game/script.rpyc", "game/chapter5.rpyc"},
            protected_paths=set(),
        )
        joined = "\n".join(errors)
        self.assertIn("missing", joined.lower())
        self.assertIn("game/chapter5.rpyc", joined)
        self.assertIn("extra", joined.lower())
        self.assertIn("game/extra.rpyc", joined)

    def test_payload_contract_requires_all_protected_ui_paths(self) -> None:
        validate = self.function("validate_payload")
        errors = validate(
            {"README.txt", "game/script.rpyc"},
            platform="windows",
            expected_rpycs={"game/script.rpyc"},
            protected_paths={"game/images/ui/panel_frame.png"},
        )
        self.assertIn("game/images/ui/panel_frame.png", "\n".join(errors))

    def test_old_game_detection_is_component_aware(self) -> None:
        find_old_game = self.function("find_old_game_payloads")
        paths = {
            "old-game/script.rpyc",
            "game/old-game.rpa",
            "game/old-game-compat.rpa",
            "docs/old-game-save-compat-design.md",
        }
        self.assertEqual(
            find_old_game(paths),
            {
                "old-game/script.rpyc",
                "game/old-game.rpa",
                "game/old-game-compat.rpa",
            },
        )


class AndroidOutputParsingTests(VerifierTestCase):
    def test_badging_parser_extracts_release_metadata(self) -> None:
        parse = self.function("parse_badging")
        self.assertEqual(
            parse(BADGING),
            {
                "package": APPROVED_ANDROID_PACKAGE,
                "version_name": APPROVED_VERSION,
                "version_code": CURRENT_CODE,
                "min_sdk": 21,
                "target_sdk": APPROVED_ANDROID_API,
            },
        )

    def test_xmltree_parser_extracts_both_activity_orientations(self) -> None:
        parse = self.function("parse_activity_orientations")
        self.assertEqual(
            parse(XMLTREE),
            {
                "org.renpy.android.ConsentActivity": 0x6,
                "org.renpy.android.PythonSDLActivity": 0x6,
            },
        )

    def test_signer_parser_accepts_full_success_output_with_warnings(self) -> None:
        parse = self.function("parse_signer_digests")
        self.assertEqual(parse(SIGNER, 0), frozenset({CERTIFICATE}))
        error = self.error_type()
        with self.assertRaises(error):
            parse(SIGNER.replace("Number of signers: 1", "Number of signers: 2"), 0)

    def test_signer_parser_rejects_nonzero_exit(self) -> None:
        parse = self.function("parse_signer_digests")
        error = self.error_type()
        with self.assertRaises(error):
            parse(SIGNER, 1)

    def test_android_contract_accepts_expected_metadata(self) -> None:
        validate = self.function("validate_android_contract")
        errors = validate(
            self.function("parse_badging")(BADGING),
            self.function("parse_badging")(PREVIOUS_BADGING),
            self.function("parse_activity_orientations")(XMLTREE),
            frozenset({CERTIFICATE}),
            frozenset({CERTIFICATE}),
        )
        self.assertEqual(errors, [])

    def test_android_contract_reports_each_metadata_or_signer_drift(self) -> None:
        validate = self.function("validate_android_contract")
        parse = self.function("parse_badging")
        current = parse(BADGING)
        previous = parse(PREVIOUS_BADGING)
        orientations = self.function("parse_activity_orientations")(XMLTREE)
        mutations = {
            "package": ({**current, "package": "wrong.package"}, previous, orientations, CERTIFICATE),
            "version": ({**current, "version_name": "3.9.1"}, previous, orientations, CERTIFICATE),
            "version code": ({**current, "version_code": PREVIOUS_CODE}, previous, orientations, CERTIFICATE),
            "minSdk": ({**current, "min_sdk": 22}, previous, orientations, CERTIFICATE),
            "targetSdk": ({**current, "target_sdk": 35}, previous, orientations, CERTIFICATE),
            "orientation": (current, previous, {**orientations, "org.renpy.android.PythonSDLActivity": 1}, CERTIFICATE),
            "certificate": (current, previous, orientations, "different"),
        }
        for label, (changed, old, changed_orientations, old_certificate) in mutations.items():
            with self.subTest(label=label):
                errors = validate(
                    changed,
                    old,
                    changed_orientations,
                    frozenset({CERTIFICATE}),
                    frozenset({old_certificate}),
                )
                self.assertTrue(errors, label)


class AndroidToolTests(VerifierTestCase):
    @staticmethod
    def _make_tools(directory: Path) -> dict[str, Path]:
        directory.mkdir(parents=True, exist_ok=True)
        tools = {
            "aapt": directory / "aapt.exe",
            "apksigner": directory / "apksigner.bat",
            "zipalign": directory / "zipalign.exe",
        }
        for path in tools.values():
            path.write_bytes(b"")
        return tools

    def test_explicit_build_tools_directory_is_used(self) -> None:
        discover = self.function("discover_build_tools")
        with tempfile.TemporaryDirectory() as temporary:
            expected = self._make_tools(Path(temporary))
            self.assertEqual(
                discover(Path(temporary), environ={}, search_path=""), expected
            )

    def test_discovery_chooses_highest_usable_sdk_version(self) -> None:
        discover = self.function("discover_build_tools")
        with tempfile.TemporaryDirectory() as temporary:
            sdk = Path(temporary) / "Sdk"
            self._make_tools(sdk / "build-tools" / "35.0.0")
            expected = self._make_tools(sdk / "build-tools" / "36.1.0")
            self.assertEqual(
                discover(
                    None,
                    environ={"ANDROID_SDK_ROOT": str(sdk)},
                    search_path="",
                ),
                expected,
            )

    def test_discovery_checks_path_before_sdk_roots(self) -> None:
        discover = self.function("discover_build_tools")
        with tempfile.TemporaryDirectory() as temporary:
            expected = self._make_tools(Path(temporary))
            lookup = {
                "aapt": expected["aapt"],
                "aapt.exe": expected["aapt"],
                "apksigner": expected["apksigner"],
                "apksigner.bat": expected["apksigner"],
                "zipalign": expected["zipalign"],
                "zipalign.exe": expected["zipalign"],
            }
            with mock.patch.object(
                verifier.shutil,
                "which",
                side_effect=lambda name, path=None: str(lookup[name]) if name in lookup else None,
            ):
                self.assertEqual(discover(None, environ={}, search_path="PATH"), expected)

    def test_discovery_accepts_tools_from_separate_path_directories(self) -> None:
        discover = self.function("discover_build_tools")
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            expected = {
                "aapt": root / "aapt-dir" / "aapt.exe",
                "apksigner": root / "signer-dir" / "apksigner.bat",
                "zipalign": root / "align-dir" / "zipalign.exe",
            }
            for path in expected.values():
                path.parent.mkdir(parents=True)
                path.write_bytes(b"")
            lookup = {
                "aapt.exe": expected["aapt"],
                "apksigner.bat": expected["apksigner"],
                "zipalign.exe": expected["zipalign"],
            }
            with mock.patch.object(
                verifier.shutil,
                "which",
                side_effect=lambda name, path=None: (
                    str(lookup[name]) if name in lookup else None
                ),
            ):
                self.assertEqual(discover(None, environ={}, search_path="PATH"), expected)

    def test_discovery_fails_when_any_required_tool_is_missing(self) -> None:
        discover = self.function("discover_build_tools")
        error = self.error_type()
        with tempfile.TemporaryDirectory() as temporary:
            (Path(temporary) / "aapt.exe").write_bytes(b"")
            with self.assertRaises(error):
                discover(Path(temporary), environ={}, search_path="")

    def test_android_tool_runner_captures_complete_outputs_and_exit_codes(self) -> None:
        run_checks = self.function("run_android_checks")
        with tempfile.TemporaryDirectory() as temporary:
            tools = self._make_tools(Path(temporary))
            runner = FakeAndroidRunner()
            errors = run_checks(
                Path("current.apk"), Path("previous.apk"), tools, runner=runner
            )
        self.assertEqual(errors, [])
        self.assertEqual(len(runner.calls), 6)

    def test_android_tool_runner_rejects_zipalign_failure(self) -> None:
        run_checks = self.function("run_android_checks")
        with tempfile.TemporaryDirectory() as temporary:
            tools = self._make_tools(Path(temporary))
            errors = run_checks(
                Path("current.apk"),
                Path("previous.apk"),
                tools,
                runner=FakeAndroidRunner(zipalign_code=1),
            )
        self.assertIn("zipalign", "\n".join(errors).lower())
        with tempfile.TemporaryDirectory() as temporary:
            tools = self._make_tools(Path(temporary))
            errors = run_checks(
                Path("current.apk"),
                Path("previous.apk"),
                tools,
                runner=FakeAndroidRunner(raise_tool="zipalign.exe"),
            )
        self.assertIn("could not start", "\n".join(errors).lower())


class EndToEndAndCliTests(VerifierTestCase):
    def test_synthetic_release_packages_pass_with_mocked_android_tools(self) -> None:
        verify = self.function("verify_release")
        expected_rpycs = {
            source.relative_to(ROOT).with_suffix(".rpyc").as_posix()
            for source in (ROOT / "game").rglob("*.rpy")
            if source.relative_to(ROOT).as_posix() != "game/test_game.rpy"
        }
        winter_rpyc = "game/governance_winter_interlude.rpyc"
        self.assertIn(winter_rpyc, expected_rpycs)
        protected = set(PROTECTED_DYNAMIC_UI_PATHS)
        runtime_paths = {
            "CourtOfShadows.py",
            "renpy/__init__.py",
            "renpy/error.py",
            "lib/python3.12/os.py",
        }
        windows_paths = {
            f"{WINDOWS_ROOT}/CourtOfShadows.exe",
            f"{WINDOWS_ROOT}/README.txt",
            *(f"{WINDOWS_ROOT}/{path}" for path in runtime_paths),
            *(f"{WINDOWS_ROOT}/{path}" for path in expected_rpycs | protected),
        }
        android_paths = {
            "AndroidManifest.xml",
            "classes.dex",
            "META-INF/MANIFEST.MF",
            "res/Ms.png",
            "res/mS.png",
            *ALLOWED_UNPREFIXED_ANDROID_ASSETS,
            *(_android_asset_name(path) for path in expected_rpycs | protected),
        }
        self.assertIn(f"{WINDOWS_ROOT}/{winter_rpyc}", windows_paths)
        self.assertIn(_android_asset_name(winter_rpyc), android_paths)
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            windows = directory / "windows.zip"
            current = directory / "current.apk"
            previous = directory / "previous.apk"
            build_tools = directory / "build-tools"
            AndroidToolTests._make_tools(build_tools)
            _write_zip(windows, windows_paths)
            _write_zip(current, android_paths)
            _write_zip(
                previous,
                {"AndroidManifest.xml", "res/Ms.png", "res/mS.png"},
            )
            runtime_count, runtime_digest = _expected_runtime_fingerprint(windows)

            def verify_synthetic() -> list[str]:
                with mock.patch.multiple(
                    verifier,
                    EXPECTED_WINDOWS_RUNTIME_COUNT=runtime_count,
                    EXPECTED_WINDOWS_RUNTIME_FINGERPRINT=runtime_digest,
                ):
                    return verify(
                        windows,
                        current,
                        previous,
                        build_tools=build_tools,
                        runner=FakeAndroidRunner(),
                    )

            errors = verify_synthetic()
            self.assertEqual(errors, [])

            _write_zip(
                windows,
                windows_paths - {f"{WINDOWS_ROOT}/{winter_rpyc}"},
            )
            errors = verify_synthetic()
            joined = "\n".join(errors)
            self.assertIn("missing", joined.lower())
            self.assertIn(winter_rpyc, joined)
            _write_zip(windows, windows_paths)

            for runtime_file in ("renpy", "RenPy"):
                with self.subTest(runtime_file=runtime_file):
                    _write_zip(
                        windows,
                        windows_paths | {f"{WINDOWS_ROOT}/{runtime_file}"},
                    )
                    errors = verify_synthetic()
                    joined = "\n".join(errors)
                    self.assertIn("ARCHIVE Windows", joined)
                    self.assertIn("ancestor", joined.lower())
            _write_zip(windows, windows_paths)

            invalid_windows_paths = (
                "game/images/ui/panel_frame.png.",
                "game/images/ui/panel_frame.png ",
                "game/images/ui/panel:frame.png",
                "game/bad\x01name.bin",
                "game/NUL/child.bin",
                "game/CON.txt",
                "game/COM1.log",
            )
            for invalid_path in invalid_windows_paths:
                with self.subTest(invalid_path=repr(invalid_path)):
                    _write_zip(
                        windows,
                        windows_paths | {f"{WINDOWS_ROOT}/{invalid_path}"},
                    )
                    errors = verify_synthetic()
                    joined = "\n".join(errors)
                    self.assertIn("ARCHIVE Windows", joined)
                    self.assertIn("invalid Windows", joined)
            _write_zip(windows, windows_paths)

            executable = f"{WINDOWS_ROOT}/CourtOfShadows.exe"
            _write_zip_with_unix_type(
                windows,
                windows_paths,
                executable,
                stat.S_IFLNK,
            )
            errors = verify_synthetic()
            joined = "\n".join(errors)
            self.assertIn("ARCHIVE Windows", joined)
            self.assertIn("Unix entry type", joined)
            _write_zip(windows, windows_paths)

            android_policy_bypasses = (
                "assets/README.txt",
                "assets/game/test_game.rpyc",
                "assets/Tools/internal.py",
                "assets/docs/internal.md",
                "README.txt",
                "game/test_game.rpyc",
                "Tools/internal.py",
                "docs/internal.md",
                "assets/game/extra.rpyc",
                "game/extra.rpyc",
            )
            for bypass_path in android_policy_bypasses:
                with self.subTest(bypass_path=bypass_path):
                    _write_zip(current, android_paths | {bypass_path})
                    errors = verify_synthetic()
                    joined = "\n".join(errors)
                    self.assertTrue(errors, bypass_path)
                    self.assertIn("android", joined.lower())
            _write_zip(current, android_paths)

            _write_zip(current, android_paths - {"classes.dex"})
            errors = verify_synthetic()
            self.assertIn("missing classes.dex", "\n".join(errors))
            _write_zip(current, android_paths)

            _write_zip(
                previous,
                {
                    "AndroidManifest.xml",
                    "assets/x-game/x-Compat.rpyc",
                    "assets/x-game/x-compat.rpyc",
                },
            )
            errors = verify_synthetic()
        self.assertIn("ARCHIVE Previous Android", "\n".join(errors))

    def test_cli_returns_zero_for_success_and_one_for_findings(self) -> None:
        main = self.function("main")
        arguments = [
            "--windows",
            "windows.zip",
            "--apk",
            "current.apk",
            "--previous-apk",
            "previous.apk",
        ]
        with mock.patch.object(verifier, "verify_release", return_value=[]):
            with redirect_stdout(io.StringIO()) as output:
                self.assertEqual(main(arguments), 0)
            self.assertIn("PASS", output.getvalue())
        with mock.patch.object(
            verifier, "verify_release", return_value=["CONTENT: forbidden payload"]
        ):
            with redirect_stdout(io.StringIO()) as output:
                self.assertEqual(main(arguments), 1)
            self.assertIn("CONTENT: forbidden payload", output.getvalue())

    def test_cli_usage_error_is_exit_two(self) -> None:
        main = self.function("main")
        with redirect_stdout(io.StringIO()), redirect_stderr(
            io.StringIO()
        ), self.assertRaises(SystemExit) as raised:
            main([])
        self.assertEqual(raised.exception.code, 2)


if __name__ == "__main__":
    unittest.main()

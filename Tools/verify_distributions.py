#!/usr/bin/env python3
"""Read-only verification for Court of Shadows release distributions."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import stat
import subprocess
import sys
from typing import Callable, Iterable, Mapping
import zipfile

try:
    from test_release_contract import (
        APPROVED_ANDROID_API,
        APPROVED_ANDROID_PACKAGE,
        APPROVED_PACKAGE_EXCLUSIONS,
        APPROVED_VERSION,
        PROTECTED_DYNAMIC_UI_PATHS,
        renpy_pattern_matches,
    )
except ImportError:  # Supports ``python -m Tools.verify_distributions``.
    from Tools.test_release_contract import (
        APPROVED_ANDROID_API,
        APPROVED_ANDROID_PACKAGE,
        APPROVED_PACKAGE_EXCLUSIONS,
        APPROVED_VERSION,
        PROTECTED_DYNAMIC_UI_PATHS,
        renpy_pattern_matches,
    )


ROOT = Path(__file__).resolve().parents[1]
WINDOWS_ROOT = f"CourtOfShadows-{APPROVED_VERSION}-win"
EXPECTED_RELEASE_RPYC_COUNT = 55
EXPECTED_ACTIVITIES = (
    "org.renpy.android.ConsentActivity",
    "org.renpy.android.PythonSDLActivity",
)
EXPECTED_ORIENTATION = 0x6
REQUIRED_WINDOWS_PATHS = {
    "CourtOfShadows.exe",
    "README.txt",
}
# Fixed Ren'Py 8.5.2 / Court of Shadows 3.9.2 runtime contract. Engine upgrades
# must deliberately refresh both values from a reviewed distribution.
EXPECTED_WINDOWS_RUNTIME_COUNT = 1377
EXPECTED_WINDOWS_RUNTIME_FINGERPRINT = (
    "b3abb988b8c8f4bdc43c4243b25a65100200e0dcea012cdb3bc666d524446cc8"
)
WINDOWS_INVALID_COMPONENT_CHARS = frozenset('<>:"|?*')
WINDOWS_RESERVED_BASENAMES = frozenset(
    {"con", "prn", "aux", "nul"}
    | {f"com{index}" for index in range(1, 10)}
    | {f"lpt{index}" for index in range(1, 10)}
)
ALLOWED_UNPREFIXED_ANDROID_ASSETS = frozenset(
    {
        "assets/android-downloading.jpg",
        "assets/android-presplash.png",
        "assets/dexopt/baseline.prof",
        "assets/dexopt/baseline.profm",
        "assets/private.mp3",
    }
)
TOOL_FILENAMES = {
    "aapt": ("aapt.exe", "aapt"),
    "apksigner": ("apksigner.bat", "apksigner"),
    "zipalign": ("zipalign.exe", "zipalign"),
}

ToolRunner = Callable[[list[str]], subprocess.CompletedProcess[str]]


class VerificationError(Exception):
    """Raised when an archive or external-tool result cannot be trusted."""


@dataclass(frozen=True)
class ArchiveMember:
    """ZIP metadata retained only after the archive's CRC pass succeeds."""

    name: str
    utf8_flag: bool
    file_size: int
    crc32: int
    is_directory: bool


ArchiveMemberInput = ArchiveMember | tuple[str, bool]


def _validate_member_name(name: str) -> None:
    if not name or "\x00" in name:
        raise VerificationError("archive contains an empty or NUL member name")
    if "\\" in name:
        raise VerificationError(f"archive member uses a backslash: {name!r}")

    trimmed = name[:-1] if name.endswith("/") else name
    if not trimmed:
        raise VerificationError(f"archive member is an absolute root: {name!r}")
    if trimmed.startswith("/") or re.match(r"^[A-Za-z]:/", trimmed):
        raise VerificationError(f"archive member is absolute: {name!r}")
    if "//" in trimmed:
        raise VerificationError(f"archive member has an empty component: {name!r}")

    parts = trimmed.split("/")
    if any(part in {"", ".", ".."} for part in parts):
        raise VerificationError(f"archive member has an unsafe component: {name!r}")


def _validate_windows_member_name(name: str) -> None:
    trimmed = name[:-1] if name.endswith("/") else name
    for component in trimmed.split("/"):
        if component.endswith((".", " ")):
            raise VerificationError(
                f"invalid Windows archive component with trailing dot/space: {component!r}"
            )
        if any(
            ord(character) < 0x20
            or character in WINDOWS_INVALID_COMPONENT_CHARS
            for character in component
        ):
            raise VerificationError(
                f"invalid Windows archive character in component: {component!r}"
            )
        basename = component.split(".", 1)[0].rstrip(". ").casefold()
        if basename in WINDOWS_RESERVED_BASENAMES:
            raise VerificationError(
                f"invalid Windows reserved device component: {component!r}"
            )


def _validate_unix_entry_type(info: zipfile.ZipInfo) -> None:
    if info.create_system != 3:
        return
    mode = info.external_attr >> 16
    file_type = stat.S_IFMT(mode)
    if file_type == 0:
        return
    expected_type = stat.S_IFDIR if info.is_dir() else stat.S_IFREG
    if file_type != expected_type:
        raise VerificationError(
            "archive member has unsupported or mismatched Unix entry type "
            f"0o{file_type:o}: {info.orig_filename!r}"
        )


def _assert_archive_tree_is_extractable(
    infos: Iterable[zipfile.ZipInfo], *, casefold_paths: bool
) -> None:
    entries: dict[tuple[str, ...], tuple[bool, str]] = {}
    for info in infos:
        trimmed = info.orig_filename[:-1] if info.is_dir() else info.orig_filename
        components = tuple(trimmed.split("/"))
        if casefold_paths:
            components = tuple(component.casefold() for component in components)

        previous = entries.get(components)
        if previous is not None and previous[0] != info.is_dir():
            raise VerificationError(
                "archive has a file/directory conflict: "
                f"{previous[1]!r} and {info.orig_filename!r}"
            )
        entries[components] = (info.is_dir(), info.orig_filename)

    for components, (_, name) in entries.items():
        for length in range(1, len(components)):
            ancestor = entries.get(components[:length])
            if ancestor is not None and not ancestor[0]:
                raise VerificationError(
                    "archive file is a directory ancestor: "
                    f"{ancestor[1]!r} blocks {name!r}"
                )


def inspect_archive(
    path: Path,
    *,
    casefold_collisions: bool = True,
    windows_paths: bool = True,
) -> list[ArchiveMember]:
    """Validate ZIP structure and CRCs, returning member names and UTF-8 flags."""
    path = Path(path)
    if not path.is_file():
        raise VerificationError(f"archive does not exist: {path}")

    try:
        with zipfile.ZipFile(path) as archive:
            infos = archive.infolist()
            names: set[str] = set()
            folded: dict[str, str] = {}
            for info in infos:
                name = info.orig_filename
                _validate_member_name(name)
                _validate_unix_entry_type(info)
                if windows_paths:
                    _validate_windows_member_name(name)
                if name in names:
                    raise VerificationError(f"archive has a duplicate member: {name}")
                names.add(name)

                if casefold_collisions:
                    key = name.casefold()
                    previous = folded.get(key)
                    if previous is not None and previous != name:
                        raise VerificationError(
                            "archive has a case-insensitive collision: "
                            f"{previous!r} and {name!r}"
                        )
                    folded[key] = name

            _assert_archive_tree_is_extractable(
                infos, casefold_paths=casefold_collisions
            )

            bad_member = archive.testzip()
            if bad_member is not None:
                raise VerificationError(f"archive CRC failed: {bad_member}")

            return [
                ArchiveMember(
                    name=info.orig_filename,
                    utf8_flag=bool(info.flag_bits & 0x800),
                    file_size=info.file_size,
                    crc32=info.CRC,
                    is_directory=info.is_dir(),
                )
                for info in infos
            ]
    except VerificationError:
        raise
    except (OSError, RuntimeError, zipfile.BadZipFile, zipfile.LargeZipFile) as exc:
        raise VerificationError(f"cannot validate archive {path}: {exc}") from exc


def _assert_logical_paths_are_unique(paths: Iterable[str]) -> set[str]:
    result: set[str] = set()
    folded: dict[tuple[str, ...], str] = {}
    for path in paths:
        _validate_member_name(path)
        key = tuple(component.casefold() for component in path.split("/"))
        if key in folded:
            previous = folded[key]
            if previous == path:
                raise VerificationError(
                    f"logical payload has a duplicate after normalization: {path!r}"
                )
            raise VerificationError(
                f"logical payload has a case-insensitive collision: {previous!r} and {path!r}"
            )
        folded[key] = path
        result.add(path)

    for key, path in folded.items():
        for length in range(1, len(key)):
            ancestor = folded.get(key[:length])
            if ancestor is not None:
                raise VerificationError(
                    "logical payload has a file ancestor conflict: "
                    f"{ancestor!r} blocks {path!r}"
                )
    return result


def _member_name_and_utf8(member: ArchiveMemberInput) -> tuple[str, bool]:
    if isinstance(member, ArchiveMember):
        return member.name, member.utf8_flag
    return member


def normalize_windows_payload(members: Iterable[ArchiveMemberInput]) -> set[str]:
    """Strip the one required versioned root from Windows archive members."""
    names = [_member_name_and_utf8(member)[0] for member in members]
    roots = {name.split("/", 1)[0] for name in names}
    if roots != {WINDOWS_ROOT}:
        raise VerificationError(
            f"Windows archive root must be {WINDOWS_ROOT!r}, found {sorted(roots)!r}"
        )

    logical: list[str] = []
    prefix = WINDOWS_ROOT + "/"
    for name in names:
        if name.endswith("/"):
            continue
        if not name.startswith(prefix) or len(name) == len(prefix):
            raise VerificationError(f"Windows member is outside the release root: {name}")
        logical.append(name[len(prefix) :])
    return _assert_logical_paths_are_unique(logical)


def _is_windows_runtime_path(relative: str) -> bool:
    folded = relative.casefold()
    return (
        folded in {"courtofshadows.exe", "courtofshadows.py"}
        or folded.startswith("renpy/")
        or folded.startswith("lib/")
    )


def windows_runtime_fingerprint(
    members: Iterable[ArchiveMember],
) -> tuple[int, str]:
    """Hash the complete verified Windows runtime path/size/CRC inventory."""
    prefix = WINDOWS_ROOT + "/"
    records: list[tuple[str, int, int]] = []
    for member in members:
        if not isinstance(member, ArchiveMember):
            raise VerificationError(
                "Windows runtime fingerprint requires verified ZIP metadata"
            )
        if member.is_directory:
            continue
        if not member.name.startswith(prefix) or len(member.name) == len(prefix):
            raise VerificationError(
                f"Windows member is outside the release root: {member.name}"
            )
        relative = member.name[len(prefix) :]
        if _is_windows_runtime_path(relative):
            records.append((relative, member.file_size, member.crc32))

    digest = hashlib.sha256()
    for relative, file_size, crc32 in sorted(records):
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(str(file_size).encode("ascii"))
        digest.update(b"\0")
        digest.update(f"{crc32:08x}".encode("ascii"))
        digest.update(b"\n")
    return len(records), digest.hexdigest()


def validate_windows_runtime(
    members: Iterable[ArchiveMember],
    *,
    expected_count: int | None = None,
    expected_digest: str | None = None,
) -> list[str]:
    """Require the fixed Ren'Py 8.5.2 / 3.9.2 runtime inventory."""
    if expected_count is None:
        expected_count = EXPECTED_WINDOWS_RUNTIME_COUNT
    if expected_digest is None:
        expected_digest = EXPECTED_WINDOWS_RUNTIME_FINGERPRINT

    try:
        actual_count, actual_digest = windows_runtime_fingerprint(members)
    except VerificationError as exc:
        return [f"CONTENT windows: cannot fingerprint Windows runtime: {exc}"]
    if actual_count == expected_count and actual_digest == expected_digest:
        return []
    return [
        "CONTENT windows: runtime fingerprint mismatch: "
        f"files={actual_count}/{expected_count} "
        f"sha256={actual_digest} expected={expected_digest}"
    ]


def _repair_cp437_filename(name: str, utf8_flag: bool) -> str:
    if utf8_flag:
        return name
    try:
        return name.encode("cp437").decode("utf-8")
    except (UnicodeEncodeError, UnicodeDecodeError):
        return name


def _classify_android_payload(
    members: Iterable[ArchiveMemberInput],
) -> tuple[set[str], set[str], set[str], set[str]]:
    project_paths: list[str] = []
    asset_paths: list[str] = []
    policy_paths: set[str] = set()
    disallowed_assets: set[str] = set()
    raw_game_paths: set[str] = set()
    for member in members:
        raw_name, utf8_flag = _member_name_and_utf8(member)
        if raw_name.endswith("/"):
            continue
        name = _repair_cp437_filename(raw_name, utf8_flag)
        _validate_member_name(name)
        if not name.startswith("assets/"):
            policy_paths.add(name)
            if name.startswith("game/"):
                raw_game_paths.add(name)
            continue

        relative = name[len("assets/") :]
        if name.startswith("assets/x-"):
            components = relative.split("/")
            if not components or any(
                not component.startswith("x-") for component in components
            ):
                raise VerificationError(
                    f"Android project asset has a partial x- component tree: {name}"
                )
            relative = "/".join(component[2:] for component in components)
            project_paths.append(relative)
        elif name not in ALLOWED_UNPREFIXED_ANDROID_ASSETS:
            disallowed_assets.add(name)

        asset_paths.append(relative)
        policy_paths.add(relative)

    _assert_logical_paths_are_unique(asset_paths)
    return (
        set(project_paths),
        policy_paths,
        disallowed_assets,
        raw_game_paths,
    )


def normalize_android_payload(members: Iterable[ArchiveMemberInput]) -> set[str]:
    """Return only Ren'Py x-prefixed project paths from an Android archive."""
    project_paths, _, disallowed_assets, _ = _classify_android_payload(members)
    if disallowed_assets:
        raise VerificationError(
            "Android archive has unapproved unprefixed assets: "
            f"{_format_paths(disallowed_assets)}"
        )
    return project_paths


def android_policy_candidates(members: Iterable[ArchiveMemberInput]) -> set[str]:
    """Return project-relative and raw APK paths used for content-policy scans."""
    _, policy_paths, _, _ = _classify_android_payload(members)
    return policy_paths


def expected_game_rpycs(root: Path = ROOT) -> set[str]:
    """Derive the exact released RPYC set from current source scripts."""
    game = Path(root) / "game"
    expected: set[str] = set()
    for source in game.rglob("*.rpy"):
        relative = source.relative_to(root).as_posix()
        if relative == "game/test_game.rpy":
            continue
        expected.add(source.relative_to(root).with_suffix(".rpyc").as_posix())
    return expected


def find_forbidden_payloads(
    paths: Iterable[str],
) -> dict[str, set[str]]:
    """Return release-contract exclusion patterns and the paths they matched."""
    candidates = set(paths)
    matches: dict[str, set[str]] = {}
    for pattern in APPROVED_PACKAGE_EXCLUSIONS:
        matched = {
            path for path in candidates if renpy_pattern_matches(path, pattern)
        }
        if matched:
            matches[pattern] = matched
    return matches


def find_old_game_payloads(paths: Iterable[str]) -> set[str]:
    """Find shipped old-game trees or specifically named old-game archives."""
    violations: set[str] = set()
    for path in paths:
        pure = PurePosixPath(path)
        if any(part.casefold() == "old-game" for part in pure.parts):
            violations.add(path)
            continue
        name = pure.name.casefold()
        if name.startswith("old-game") and name.endswith(".rpa"):
            violations.add(path)
    return violations


def _format_paths(paths: Iterable[str], limit: int = 12) -> str:
    ordered = sorted(set(paths))
    shown = ordered[:limit]
    suffix = f" ... (+{len(ordered) - limit})" if len(ordered) > limit else ""
    return ", ".join(shown) + suffix


def validate_payload(
    paths: Iterable[str],
    *,
    platform: str,
    expected_rpycs: set[str],
    protected_paths: set[str],
    include_forbidden: bool = True,
    policy_paths: Iterable[str] | None = None,
) -> list[str]:
    """Validate one normalized project payload and return all findings."""
    if platform not in {"windows", "android"}:
        raise ValueError(f"unsupported platform: {platform}")

    payload = set(paths)
    policy_payload = payload if policy_paths is None else set(policy_paths)
    errors: list[str] = []
    prefix = f"CONTENT {platform}:"

    if include_forbidden:
        forbidden = find_forbidden_payloads(policy_payload)
        if forbidden:
            forbidden_paths = {
                path for matches in forbidden.values() for path in matches
            }
            errors.append(
                f"{prefix} forbidden payloads classes={len(forbidden)} "
                f"paths={len(forbidden_paths)}; "
                f"sample={_format_paths(forbidden_paths)}"
            )

    actual_rpycs = {
        path
        for path in payload
        if path.startswith("game/") and path.endswith(".rpyc")
    }
    missing_rpycs = expected_rpycs - actual_rpycs
    extra_rpycs = actual_rpycs - expected_rpycs
    if missing_rpycs:
        errors.append(
            f"{prefix} missing game RPYC: {_format_paths(missing_rpycs)}"
        )
    if extra_rpycs:
        errors.append(f"{prefix} extra game RPYC: {_format_paths(extra_rpycs)}")

    missing_ui = protected_paths - payload
    if missing_ui:
        errors.append(
            f"{prefix} missing protected UI: {_format_paths(missing_ui)}"
        )

    old_game = find_old_game_payloads(policy_payload)
    if old_game:
        errors.append(f"{prefix} old-game payloads: {_format_paths(old_game)}")

    if "game/test_game.rpyc" in policy_payload:
        errors.append(f"{prefix} contains game/test_game.rpyc")

    if platform == "windows":
        missing_windows_files = REQUIRED_WINDOWS_PATHS - payload
        if missing_windows_files:
            errors.append(
                f"{prefix} missing required Windows files: "
                f"{_format_paths(missing_windows_files)}"
            )
    elif "README.txt" in policy_payload:
        errors.append(f"{prefix} contains Windows-only README.txt")

    return errors


def parse_badging(output: str) -> dict[str, object]:
    """Parse the release fields from complete ``aapt dump badging`` output."""
    package = re.search(
        r"^package:\s+name='([^']+)'\s+versionCode='(\d+)'\s+versionName='([^']+)'",
        output,
        re.MULTILINE,
    )
    minimum = re.search(r"^sdkVersion:'(\d+)'", output, re.MULTILINE)
    target = re.search(r"^targetSdkVersion:'(\d+)'", output, re.MULTILINE)
    if package is None or minimum is None or target is None:
        raise VerificationError("aapt badging output is missing required metadata")
    return {
        "package": package.group(1),
        "version_name": package.group(3),
        "version_code": int(package.group(2)),
        "min_sdk": int(minimum.group(1)),
        "target_sdk": int(target.group(1)),
    }


def parse_activity_orientations(output: str) -> dict[str, int]:
    """Parse declared activity orientations from complete aapt XML-tree output."""
    orientations: dict[str, int] = {}
    lines = output.splitlines()
    index = 0
    while index < len(lines):
        activity = re.match(r"^(\s*)E: activity \([^\n]*\)\s*$", lines[index])
        if activity is None:
            index += 1
            continue

        activity_indent = len(activity.group(1))
        index += 1
        block_lines: list[str] = []
        while index < len(lines):
            element = re.match(r"^(\s*)E:", lines[index])
            if element is not None and len(element.group(1)) <= activity_indent:
                break
            block_lines.append(lines[index])
            index += 1

        block = "\n".join(block_lines)
        name = re.search(r'android:name[^\n]*="([^"]+)"', block)
        orientation = re.search(
            r"android:screenOrientation[^\n]*0x([0-9a-fA-F]+)", block
        )
        if name is not None and orientation is not None:
            orientations[name.group(1)] = int(orientation.group(1), 16)
    return orientations


def parse_signer_digests(output: str, returncode: int) -> frozenset[str]:
    """Return the non-empty signer-certificate set from apksigner output."""
    if returncode != 0:
        raise VerificationError(f"apksigner exited {returncode}")
    declared = re.search(r"Number of signers:\s*(\d+)", output)
    signer_rows = re.findall(
        r"Signer #\d+ certificate SHA-256 digest:\s*([0-9a-fA-F]{64})",
        output,
    )
    if declared is None or int(declared.group(1)) != len(signer_rows):
        raise VerificationError(
            "apksigner signer count does not match certificate digest rows"
        )
    digests = frozenset(digest.casefold() for digest in signer_rows)
    if not signer_rows or not digests:
        raise VerificationError("apksigner reported no signer certificate")
    return digests


def validate_android_contract(
    current: Mapping[str, object],
    previous: Mapping[str, object],
    orientations: Mapping[str, int],
    current_signers: frozenset[str],
    previous_signers: frozenset[str],
) -> list[str]:
    """Validate Android metadata and signing continuity."""
    errors: list[str] = []
    if current.get("package") != APPROVED_ANDROID_PACKAGE:
        errors.append(
            f"ANDROID: package is {current.get('package')!r}, expected {APPROVED_ANDROID_PACKAGE!r}"
        )
    if previous.get("package") != APPROVED_ANDROID_PACKAGE:
        errors.append("ANDROID: previous APK package does not match the release package")
    if current.get("version_name") != APPROVED_VERSION:
        errors.append(
            f"ANDROID: versionName is {current.get('version_name')!r}, expected {APPROVED_VERSION!r}"
        )

    current_code = current.get("version_code")
    previous_code = previous.get("version_code")
    if (
        not isinstance(current_code, int)
        or not isinstance(previous_code, int)
        or current_code <= previous_code
    ):
        errors.append(
            f"ANDROID: versionCode {current_code!r} must exceed previous {previous_code!r}"
        )
    if current.get("min_sdk") != 21:
        errors.append(f"ANDROID: minSdk is {current.get('min_sdk')!r}, expected 21")
    if current.get("target_sdk") != APPROVED_ANDROID_API:
        errors.append(
            f"ANDROID: targetSdk is {current.get('target_sdk')!r}, "
            f"expected {APPROVED_ANDROID_API}"
        )

    for activity in EXPECTED_ACTIVITIES:
        orientation = orientations.get(activity)
        if orientation != EXPECTED_ORIENTATION:
            errors.append(
                f"ANDROID: {activity} orientation is {orientation!r}, "
                f"expected 0x{EXPECTED_ORIENTATION:x}"
            )

    if not current_signers or not previous_signers:
        errors.append("ANDROID: signer certificate set must not be empty")
    elif current_signers != previous_signers:
        errors.append("ANDROID: signer certificate set differs from previous APK")
    return errors


def _tools_in(directory: Path) -> dict[str, Path] | None:
    directory = Path(directory)
    tools: dict[str, Path] = {}
    for key, filenames in TOOL_FILENAMES.items():
        found = next(
            (directory / filename for filename in filenames if (directory / filename).is_file()),
            None,
        )
        if found is None:
            return None
        tools[key] = found
    return tools


def _version_key(name: str) -> tuple[int, ...] | None:
    if re.fullmatch(r"\d+(?:\.\d+)*", name) is None:
        return None
    return tuple(int(part) for part in name.split("."))


def discover_build_tools(
    explicit: Path | None,
    *,
    environ: Mapping[str, str] | None = None,
    search_path: str | None = None,
) -> dict[str, Path]:
    """Locate all required Android build tools from explicit, PATH, or SDK sources."""
    environment = os.environ if environ is None else environ
    if explicit is not None:
        tools = _tools_in(Path(explicit))
        if tools is None:
            raise VerificationError(
                f"build-tools directory is incomplete: {Path(explicit)}"
            )
        return tools

    path_value = environment.get("PATH") if search_path is None else search_path
    path_tools: dict[str, Path] = {}
    for key, filenames in TOOL_FILENAMES.items():
        found: str | None = None
        for filename in filenames:
            found = shutil.which(filename, path=path_value)
            if found:
                break
        if found is None:
            path_tools = {}
            break
        path_tools[key] = Path(found)
    if len(path_tools) == len(TOOL_FILENAMES):
        return path_tools

    sdk_roots: list[Path] = []
    for variable in ("ANDROID_SDK_ROOT", "ANDROID_HOME"):
        value = environment.get(variable)
        if value:
            sdk_roots.append(Path(value))
    local_app_data = environment.get("LOCALAPPDATA")
    if local_app_data:
        sdk_roots.append(Path(local_app_data) / "Android" / "Sdk")

    candidates: list[tuple[tuple[int, ...], Path, dict[str, Path]]] = []
    seen: set[Path] = set()
    for sdk_root in sdk_roots:
        build_tools = sdk_root / "build-tools"
        if not build_tools.is_dir():
            continue
        for directory in build_tools.iterdir():
            if not directory.is_dir() or directory in seen:
                continue
            seen.add(directory)
            version = _version_key(directory.name)
            tools = _tools_in(directory) if version is not None else None
            if version is not None and tools is not None:
                candidates.append((version, directory, tools))
    if candidates:
        candidates.sort(key=lambda item: item[0], reverse=True)
        return candidates[0][2]

    raise VerificationError(
        "Android build tools not found; pass --build-tools or configure PATH/Android SDK"
    )


def run_command(command: list[str]) -> subprocess.CompletedProcess[str]:
    """Run an Android inspection command while retaining complete output."""
    return subprocess.run(
        command,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
        check=False,
    )


def _complete_output(result: subprocess.CompletedProcess[str]) -> str:
    return "\n".join(
        part for part in (result.stdout or "", result.stderr or "") if part
    )


def run_android_checks(
    apk: Path,
    previous_apk: Path,
    tools: Mapping[str, Path],
    *,
    runner: ToolRunner = run_command,
) -> list[str]:
    """Run aapt, apksigner, and zipalign and validate their complete results."""
    apk = Path(apk)
    previous_apk = Path(previous_apk)
    commands = {
        "current_badging": [str(tools["aapt"]), "dump", "badging", str(apk)],
        "previous_badging": [
            str(tools["aapt"]),
            "dump",
            "badging",
            str(previous_apk),
        ],
        "xmltree": [
            str(tools["aapt"]),
            "dump",
            "xmltree",
            str(apk),
            "AndroidManifest.xml",
        ],
        "current_signer": [
            str(tools["apksigner"]),
            "verify",
            "--verbose",
            "--print-certs",
            str(apk),
        ],
        "previous_signer": [
            str(tools["apksigner"]),
            "verify",
            "--verbose",
            "--print-certs",
            str(previous_apk),
        ],
        "zipalign": [str(tools["zipalign"]), "-c", "-p", "4", str(apk)],
    }
    errors: list[str] = []
    results: dict[str, subprocess.CompletedProcess[str]] = {}
    for name, command in commands.items():
        try:
            results[name] = runner(command)
        except (OSError, subprocess.SubprocessError) as exc:
            errors.append(f"ANDROID: {name} could not start: {exc}")

    parsed: dict[str, object] = {}
    for name in ("current_badging", "previous_badging"):
        result = results.get(name)
        if result is None:
            continue
        if result.returncode != 0:
            errors.append(
                f"ANDROID: aapt {name} exited {result.returncode}: "
                f"{_complete_output(result)[:1000]}"
            )
            continue
        try:
            parsed[name] = parse_badging(_complete_output(result))
        except VerificationError as exc:
            errors.append(f"ANDROID: {name}: {exc}")

    xmltree = results.get("xmltree")
    if xmltree is not None:
        if xmltree.returncode != 0:
            errors.append(
                f"ANDROID: aapt xmltree exited {xmltree.returncode}: "
                f"{_complete_output(xmltree)[:1000]}"
            )
        else:
            parsed["orientations"] = parse_activity_orientations(
                _complete_output(xmltree)
            )

    for name in ("current_signer", "previous_signer"):
        result = results.get(name)
        if result is None:
            continue
        try:
            parsed[name] = parse_signer_digests(
                _complete_output(result), result.returncode
            )
        except VerificationError as exc:
            errors.append(f"ANDROID: {name}: {exc}")

    alignment = results.get("zipalign")
    if alignment is not None and alignment.returncode != 0:
        errors.append(
            f"ANDROID: zipalign exited {alignment.returncode}: "
            f"{_complete_output(alignment)[:1000]}"
        )

    required = {
        "current_badging",
        "previous_badging",
        "orientations",
        "current_signer",
        "previous_signer",
    }
    if required.issubset(parsed):
        errors.extend(
            validate_android_contract(
                parsed["current_badging"],  # type: ignore[arg-type]
                parsed["previous_badging"],  # type: ignore[arg-type]
                parsed["orientations"],  # type: ignore[arg-type]
                parsed["current_signer"],  # type: ignore[arg-type]
                parsed["previous_signer"],  # type: ignore[arg-type]
            )
        )
    return errors


def _forbidden_path_set(matches: Mapping[str, set[str]]) -> set[str]:
    return {path for paths in matches.values() for path in paths}


def verify_release(
    windows: Path,
    apk: Path,
    previous_apk: Path,
    *,
    build_tools: Path | None = None,
    runner: ToolRunner = run_command,
) -> list[str]:
    """Verify all supplied artifacts without modifying them."""
    windows = Path(windows)
    apk = Path(apk)
    previous_apk = Path(previous_apk)
    errors: list[str] = []
    inventories: dict[str, list[ArchiveMember]] = {}

    for label, path, casefold, windows_paths in (
        ("Windows", windows, True, True),
        ("Android", apk, False, False),
        ("Previous Android", previous_apk, False, False),
    ):
        try:
            inventories[label] = inspect_archive(
                path,
                casefold_collisions=casefold,
                windows_paths=windows_paths,
            )
        except VerificationError as exc:
            errors.append(f"ARCHIVE {label}: {exc}")

    windows_payload: set[str] | None = None
    android_payload: set[str] | None = None
    android_policy_payload: set[str] | None = None
    if "Windows" in inventories:
        try:
            windows_payload = normalize_windows_payload(inventories["Windows"])
        except VerificationError as exc:
            errors.append(f"ARCHIVE Windows: {exc}")
    if "Android" in inventories:
        raw_android_names = {member.name for member in inventories["Android"]}
        missing_android_runtime = {
            "AndroidManifest.xml",
            "classes.dex",
        } - raw_android_names
        if missing_android_runtime:
            errors.append(
                "ARCHIVE Android: missing "
                + _format_paths(missing_android_runtime)
            )
        try:
            (
                android_payload,
                android_policy_payload,
                disallowed_assets,
                raw_game_paths,
            ) = _classify_android_payload(inventories["Android"])
        except VerificationError as exc:
            errors.append(f"ARCHIVE Android: {exc}")
        else:
            if disallowed_assets:
                errors.append(
                    "ARCHIVE Android: unapproved unprefixed assets: "
                    f"{_format_paths(disallowed_assets)}"
                )
            if raw_game_paths:
                errors.append(
                    "ARCHIVE Android: raw game payloads must be x-prefixed assets: "
                    f"{_format_paths(raw_game_paths)}"
                )
    if "Previous Android" in inventories:
        try:
            normalize_android_payload(inventories["Previous Android"])
        except VerificationError as exc:
            errors.append(f"ARCHIVE Previous Android: {exc}")

    expected_rpycs = expected_game_rpycs(ROOT)
    if len(expected_rpycs) != EXPECTED_RELEASE_RPYC_COUNT:
        errors.append(
            f"SOURCE: expected {EXPECTED_RELEASE_RPYC_COUNT} released RPYC paths, "
            f"derived {len(expected_rpycs)}"
        )
    protected = set(PROTECTED_DYNAMIC_UI_PATHS)

    if windows_payload is not None and android_policy_payload is not None:
        windows_forbidden = find_forbidden_payloads(windows_payload)
        android_forbidden = find_forbidden_payloads(android_policy_payload)
        patterns = set(windows_forbidden) | set(android_forbidden)
        unique_paths = _forbidden_path_set(windows_forbidden) | _forbidden_path_set(
            android_forbidden
        )
        windows_paths = _forbidden_path_set(windows_forbidden)
        android_paths = _forbidden_path_set(android_forbidden)
        if patterns:
            errors.append(
                "CONTENT forbidden payloads across packages: "
                f"classes={len(patterns)}/{len(APPROVED_PACKAGE_EXCLUSIONS)} "
                f"unique_paths={len(unique_paths)} "
                f"occurrences={len(windows_paths) + len(android_paths)} "
                f"windows_paths={len(windows_paths)} "
                f"android_paths={len(android_paths)}"
            )

    if windows_payload is not None:
        errors.extend(validate_windows_runtime(inventories["Windows"]))
        errors.extend(
            validate_payload(
                windows_payload,
                platform="windows",
                expected_rpycs=expected_rpycs,
                protected_paths=protected,
                include_forbidden=False,
            )
        )
    if android_payload is not None:
        errors.extend(
            validate_payload(
                android_payload,
                platform="android",
                expected_rpycs=expected_rpycs,
                protected_paths=protected,
                include_forbidden=False,
                policy_paths=android_policy_payload,
            )
        )

    if "Android" in inventories and "Previous Android" in inventories:
        try:
            tools = discover_build_tools(build_tools)
        except VerificationError as exc:
            errors.append(f"TOOLS: {exc}")
        else:
            errors.extend(
                run_android_checks(
                    apk, previous_apk, tools, runner=runner
                )
            )
    return errors


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Verify Court of Shadows Windows and Android distributions."
    )
    parser.add_argument("--windows", type=Path, required=True)
    parser.add_argument("--apk", type=Path, required=True)
    parser.add_argument("--previous-apk", type=Path, required=True)
    parser.add_argument("--build-tools", type=Path)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    errors = verify_release(
        args.windows,
        args.apk,
        args.previous_apk,
        build_tools=args.build_tools,
    )
    if errors:
        print(f"FAIL: distribution verification found {len(errors)} issue(s)")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASS: Windows ZIP and Android APK satisfy the release contract")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Read-only verification for Court of Shadows release distributions."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
import io
import os
from pathlib import Path, PurePosixPath
import pickletools
import re
import shutil
import stat
import struct
import subprocess
import sys
from typing import Callable, Iterable, Mapping
import zipfile
import zlib

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
EXPECTED_LAUNCHABLE_ACTIVITY = "org.renpy.android.ConsentActivity"
EXPECTED_ORIENTATION = 0x6
FORBIDDEN_ANDROID_PERMISSIONS = frozenset(
    {
        "android.permission.ACCESS_NETWORK_STATE",
        "android.permission.FOREGROUND_SERVICE",
        "android.permission.FOREGROUND_SERVICE_DATA_SYNC",
        "android.permission.INTERNET",
        "android.permission.READ_EXTERNAL_STORAGE",
        "android.permission.RECEIVE_BOOT_COMPLETED",
        "android.permission.WRITE_EXTERNAL_STORAGE",
    }
)
REQUIRED_WINDOWS_PATHS = {
    "CourtOfShadows.exe",
    "README.txt",
}
# Fixed Ren'Py 8.5.2 / Court of Shadows 3.9.2 runtime contract. Engine upgrades
# must deliberately refresh the runtime, common-cache, and source-map constants.
EXPECTED_WINDOWS_RUNTIME_COUNT = 1377
EXPECTED_WINDOWS_RUNTIME_FINGERPRINT = (
    "d87ac8f07807a7971a12caaf82bfec31fb58e2cebdee741af6bd71817578415c"
)
RPYC_MAGIC = b"_2025-07-06"
RPYC2_HEADER = b"RENPY RPC2"
MD5_DIGEST_SIZE = 16
RPYC2_TABLE_SIZE = 3 * 12
RPYC2_DATA_START = len(RPYC2_HEADER) + RPYC2_TABLE_SIZE
MAX_COMPILED_COMMON_BYTES = 4 * 1024 * 1024
ACTIVE_NAME_VERSION_WINDOW = 6_000
# These counts and path hashes were measured from two independent 3.9.2 builds.
# They make the narrow time-field normalization below fail closed if Ren'Py's
# common AST shape or source mapping changes.
EXPECTED_ACTIVE_COMMON_PATHS_SHA256 = (
    "26ed1b5ad47dfc9670ebc5fac3d7e30fc3e1b26637372c3169b5bcaaca0afb80"
)
EXPECTED_COMPILED_COMMON_COUNT = 86
EXPECTED_CURRENT_RPC2_COUNT = 76
EXPECTED_ACTIVE_COMMON_COUNT = 66
EXPECTED_ACTIVE_NAME_VERSION_COUNT = 223
EXPECTED_CORE_NAME_SERIAL_COUNT = 199
EXPECTED_MODULE_NAME_SERIAL_COUNT = 23
EXPECTED_STANDARD_SCREEN_SERIAL_COUNT = 832
EXPECTED_DEVELOPER_SCREEN_SERIAL_COUNT = 206
EXPECTED_CURRENT_SOURCE_KINDS = {
    "rpy": 57,
    "ren_py": 4,
    "rpym": 15,
}
STRICT_LEGACY_COMMON = {
    "renpy/common/_layout/grouped_navigation.rpymc": (
        1930,
        0x8F7CC503,
        "e1a802979db293f498e48a8f70457b6926af82e7d4216014c903a79c57283546",
    ),
    "renpy/common/_layout/imagemap_common.rpymc": (
        2532,
        0x5B34D789,
        "37b1e5e78f32f565753a1091a825036e532a4b423aa11fad9ae7cc79a25a06f6",
    ),
    "renpy/common/_layout/imagemap_load_save.rpymc": (
        2616,
        0xC8EE6E6D,
        "fed6c7be2d26da3a5b18fb6f02afe87c495a7499f368d7c79f5bf9c9df3e35bc",
    ),
    "renpy/common/_layout/imagemap_main_menu.rpymc": (
        1924,
        0x07D5194C,
        "8fd09d94019a003bd17222ded34fead4efa8574f24d6b6a9afaadc805cc8de03",
    ),
    "renpy/common/_layout/imagemap_navigation.rpymc": (
        868,
        0xBDA8FBE3,
        "dde0402ee3661dabc0a65cff161f1d4d45728e1c98467fd58fc9c3ed2d0213df",
    ),
    "renpy/common/_layout/imagemap_preferences.rpymc": (
        1437,
        0xEE6C2A12,
        "3828deb4048ddbcd2fbc8018cf076c6208654566d50ce143117e46a8b2409e6d",
    ),
    "renpy/common/_layout/imagemap_yesno_prompt.rpymc": (
        1592,
        0xC528C787,
        "a9b5868582db226cf726f05689d1da96db8184cd812121bad59f9fbb50e8e8e0",
    ),
    "renpy/common/_layout/screen_joystick_preferences.rpymc": (
        1290,
        0x496C65A8,
        "36cb1a9b348fa4452f338114df9e77850fe7d41ab6d5887379ce0e974b0e3fa8",
    ),
    "renpy/common/_layout/scrolling_load_save.rpymc": (
        2189,
        0xD58F1DA6,
        "7735108182301226b18415327c80104b8d8af39d199c243cd1f28b4a25fa53e3",
    ),
    "renpy/common/_layout/two_column_preferences.rpymc": (
        1038,
        0x06D7B862,
        "a7bf2ae79ac83ef3e56cf6fa825f5db6c216e9251a78020053561690cb3f6f72",
    ),
}
# Ren'Py 8.5.2 ships this RPC2 cache with a trailer for an earlier copy of
# its source. The parsed AST remains covered by the fixed runtime fingerprint.
KNOWN_STALE_COMMON_SOURCE_MD5 = frozenset(
    {
        "renpy/common/_layout/classic_preferences.rpymc",
        "renpy/common/_layout/classic_preferences_common.rpymc",
    }
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


@dataclass(frozen=True)
class CompiledCommonRecord:
    """A reviewed semantic fingerprint for one common compiled cache."""

    kind: str
    digest: str


@dataclass(frozen=True)
class _KeyedInteger:
    operation_index: int
    key: str
    value: int


@dataclass(frozen=True)
class _ParsedCompiledPickle:
    raw: bytes
    operations: tuple[tuple[object, object, int], ...]
    keyed_integers: tuple[_KeyedInteger, ...]


@dataclass(frozen=True)
class _ParsedRpc2Common:
    source_md5: bytes
    parsed_pickle: _ParsedCompiledPickle


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


def _is_compiled_common(relative: str) -> bool:
    folded = relative.casefold()
    return folded.startswith("renpy/common/") and folded.endswith(
        (".rpyc", ".rpymc")
    )


def _decompress_compiled_slot(payload: bytes, member_name: str, slot: int) -> bytes:
    decompressor = zlib.decompressobj()
    try:
        result = decompressor.decompress(payload, MAX_COMPILED_COMMON_BYTES + 1)
        if len(result) > MAX_COMPILED_COMMON_BYTES or decompressor.unconsumed_tail:
            raise VerificationError(
                f"compiled common slot exceeds the decompression limit: {member_name} slot {slot}"
            )
        result += decompressor.flush(MAX_COMPILED_COMMON_BYTES + 1 - len(result))
    except zlib.error as exc:
        raise VerificationError(
            f"compiled common slot is not valid zlib data: {member_name} slot {slot}: {exc}"
        ) from exc
    if (
        len(result) > MAX_COMPILED_COMMON_BYTES
        or not decompressor.eof
        or decompressor.unused_data
        or decompressor.unconsumed_tail
    ):
        raise VerificationError(
            f"compiled common slot has trailing, truncated, or oversized zlib data: {member_name} slot {slot}"
        )
    return result


def _inspect_compiled_pickle(raw: bytes, member_name: str) -> _ParsedCompiledPickle:
    try:
        # dis() performs pickle stack and memo validation without constructing
        # or importing any object from the untrusted pickle.
        pickletools.dis(raw, out=io.StringIO())
        operations = tuple(pickletools.genops(raw))
    except Exception as exc:
        raise VerificationError(
            f"compiled common slot is not a valid static pickle: {member_name}: {exc}"
        ) from exc
    if (
        not operations
        or operations[-1][0].name != "STOP"
        or operations[-1][2] + 1 != len(raw)
    ):
        raise VerificationError(
            f"compiled common pickle does not end exactly at STOP: {member_name}"
        )

    string_operations = {
        "SHORT_BINUNICODE",
        "BINUNICODE",
        "BINUNICODE8",
        "UNICODE",
        "SHORT_BINSTRING",
        "BINSTRING",
        "STRING",
    }
    get_operations = {"BINGET", "LONG_BINGET", "GET"}
    put_operations = {"BINPUT", "LONG_BINPUT", "PUT"}
    integer_operations = {
        "BININT",
        "BININT1",
        "BININT2",
        "LONG",
        "LONG1",
        "LONG4",
        "INT",
    }
    identifier_keys = {"name_version", "name_serial", "serial"}
    unknown = object()
    memo: dict[int, object] = {}
    top: object = unknown
    candidate_key: str | None = None
    keyed_integers: list[_KeyedInteger] = []

    for operation_index, (operation, argument, _position) in enumerate(operations):
        name = operation.name
        if name in string_operations:
            top = argument
            candidate_key = argument if argument in identifier_keys else None
        elif name in get_operations:
            top = memo.get(int(argument), unknown)
            candidate_key = top if top in identifier_keys else None
        elif name == "MEMOIZE":
            memo[len(memo)] = top
        elif name in put_operations:
            memo[int(argument)] = top
        elif name in integer_operations and candidate_key is not None:
            keyed_integers.append(
                _KeyedInteger(operation_index, candidate_key, int(argument))
            )
            top = unknown
            candidate_key = None
        else:
            top = unknown
            candidate_key = None

    return _ParsedCompiledPickle(raw, operations, tuple(keyed_integers))


def _parse_rpc2_common(payload: bytes, member_name: str) -> _ParsedRpc2Common:
    minimum_size = RPYC2_DATA_START + 2 + MD5_DIGEST_SIZE
    if len(payload) < minimum_size or not payload.startswith(RPYC2_HEADER):
        raise VerificationError(f"compiled common member is not RPC2: {member_name}")

    try:
        table = tuple(
            struct.unpack_from("<III", payload, len(RPYC2_HEADER) + index * 12)
            for index in range(3)
        )
    except struct.error as exc:
        raise VerificationError(
            f"compiled common RPC2 table is truncated: {member_name}"
        ) from exc

    slot_1, slot_2, terminator = table
    trailer_size = MD5_DIGEST_SIZE
    valid_layout = (
        slot_1[0] == 1
        and slot_1[1] == RPYC2_DATA_START
        and slot_1[2] > 0
        and slot_2[0] == 2
        and slot_2[1] == slot_1[1] + slot_1[2]
        and slot_2[2] > 0
        and terminator == (0, 0, 0)
        and slot_2[1] + slot_2[2] + trailer_size == len(payload)
    )
    if not valid_layout:
        raise VerificationError(
            f"compiled common RPC2 slots are not contiguous [1, 2, 0]: {member_name}"
        )

    raw_slots = []
    for slot, start, length in (slot_1, slot_2):
        raw_slots.append(
            _decompress_compiled_slot(
                payload[start : start + length], member_name, slot
            )
        )
    if raw_slots[0] != raw_slots[1]:
        raise VerificationError(
            f"compiled common RPC2 slots disagree after decompression: {member_name}"
        )
    parsed_pickle = _inspect_compiled_pickle(raw_slots[0], member_name)
    return _ParsedRpc2Common(payload[-trailer_size:], parsed_pickle)


def _compiled_source_candidates(relative: str) -> tuple[tuple[str, str], ...]:
    if relative.casefold().endswith(".rpymc"):
        return ((relative[:-1], "rpym"),)
    return (
        (relative[:-1], "rpy"),
        (relative[:-5] + "_ren.py", "ren_py"),
    )


def _path_set_sha256(paths: Iterable[str]) -> str:
    payload = "".join(path + "\n" for path in sorted(paths)).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _is_developer_common(relative: str) -> bool:
    return relative.casefold().startswith("renpy/common/_developer/")


def _is_module_common(relative: str) -> bool:
    folded = relative.casefold()
    return folded.startswith(("renpy/common/_developer/", "renpy/common/_layout/"))


def _canonical_compiled_pickle_digest(
    relative: str,
    parsed: _ParsedRpc2Common,
    *,
    active_name_version: int | None,
    screen_serial_minima: Mapping[str, int],
    module_name_serial_minimum: int | None,
) -> str:
    keyed = parsed.parsed_pickle.keyed_integers
    normalized: dict[int, bytes] = {}
    screen_group = "developer" if _is_developer_common(relative) else "standard"

    for record_index, record in enumerate(keyed):
        operation = parsed.parsed_pickle.operations[record.operation_index][0]
        token: str | None = None
        if record.key == "name_version" and record.value == active_name_version:
            token = f"name_version|{operation.name}|active"
        elif (
            record.key == "name_serial"
            and active_name_version is not None
            and record_index > 0
            and keyed[record_index - 1].key == "name_version"
            and keyed[record_index - 1].value == active_name_version
            and _is_module_common(relative)
        ):
            # Module caches shift this generated serial block between otherwise
            # identical builds; retain every within-block offset and duplicate.
            if module_name_serial_minimum is None:
                raise VerificationError(
                    f"compiled common module name serial has no normalization base: {relative}"
                )
            token = (
                f"name_serial|{operation.name}|"
                f"{record.value - module_name_serial_minimum}"
            )
        elif record.key == "serial":
            minimum = screen_serial_minima.get(screen_group)
            if minimum is None:
                raise VerificationError(
                    f"compiled common screen serial has no {screen_group} base: {relative}"
                )
            token = f"serial|{operation.name}|{record.value - minimum}"
        if token is not None:
            normalized[record.operation_index] = token.encode("ascii")

    digest = hashlib.sha256()
    digest.update(relative.encode("utf-8"))
    digest.update(b"\0RPC2\0")
    digest.update(parsed.source_md5)
    for operation_index, (_operation, _argument, position) in enumerate(
        parsed.parsed_pickle.operations
    ):
        next_position = (
            parsed.parsed_pickle.operations[operation_index + 1][2]
            if operation_index + 1 < len(parsed.parsed_pickle.operations)
            else len(parsed.parsed_pickle.raw)
        )
        replacement = normalized.get(operation_index)
        if replacement is None:
            piece = parsed.parsed_pickle.raw[position:next_position]
            digest.update(b"R")
            digest.update(len(piece).to_bytes(8, "big"))
            digest.update(piece)
        else:
            digest.update(b"N")
            digest.update(len(replacement).to_bytes(4, "big"))
            digest.update(replacement)
    return digest.hexdigest()


def inspect_compiled_common_contract(
    path: Path,
    members: Iterable[ArchiveMember] | None = None,
    *,
    require_release_contract: bool = True,
) -> dict[str, CompiledCommonRecord]:
    """Validate and semantically fingerprint Windows common bytecode caches."""
    path = Path(path)
    verified_members = list(members) if members is not None else inspect_archive(path)
    prefix = WINDOWS_ROOT + "/"
    compiled_paths = sorted(
        member.name[len(prefix) :]
        for member in verified_members
        if not member.is_directory
        and member.name.startswith(prefix)
        and _is_compiled_common(member.name[len(prefix) :])
    )
    if not compiled_paths:
        return {}
    if require_release_contract and len(compiled_paths) != EXPECTED_COMPILED_COMMON_COUNT:
        raise VerificationError(
            "compiled common path count changed: "
            f"{len(compiled_paths)}/{EXPECTED_COMPILED_COMMON_COUNT}"
        )
    if require_release_contract and not set(STRICT_LEGACY_COMMON).issubset(
        compiled_paths
    ):
        missing = sorted(set(STRICT_LEGACY_COMMON) - set(compiled_paths))
        raise VerificationError(
            f"strict legacy common paths are missing: {', '.join(missing)}"
        )

    try:
        with zipfile.ZipFile(path) as archive:
            info_by_relative = {
                info.orig_filename[len(prefix) :]: info
                for info in archive.infolist()
                if not info.is_dir() and info.orig_filename.startswith(prefix)
            }
            parsed: dict[str, _ParsedRpc2Common] = {}
            records: dict[str, CompiledCommonRecord] = {}
            source_kinds: dict[str, int] = {"rpy": 0, "ren_py": 0, "rpym": 0}

            for relative in compiled_paths:
                info = info_by_relative.get(relative)
                if info is None:
                    raise VerificationError(
                        f"compiled common member disappeared during inspection: {relative}"
                    )
                if info.file_size > MAX_COMPILED_COMMON_BYTES:
                    raise VerificationError(
                        f"compiled common member exceeds the size limit: {relative}"
                    )
                payload = archive.read(info)
                legacy = STRICT_LEGACY_COMMON.get(relative)
                if legacy is not None:
                    expected_size, expected_crc, expected_sha256 = legacy
                    actual_sha256 = hashlib.sha256(payload).hexdigest()
                    if (
                        info.file_size != expected_size
                        or info.CRC != expected_crc
                        or actual_sha256 != expected_sha256
                    ):
                        raise VerificationError(
                            f"strict legacy common cache changed: {relative}"
                        )
                    records[relative] = CompiledCommonRecord(
                        "compiled-common-legacy",
                        f"{info.file_size}:{info.CRC:08x}:{actual_sha256}",
                    )
                    continue

                candidates = [
                    (source, source_kind)
                    for source, source_kind in _compiled_source_candidates(relative)
                    if source in info_by_relative
                ]
                if len(candidates) != 1:
                    raise VerificationError(
                        "compiled common source mapping is not unique: "
                        f"{relative} -> {[source for source, _kind in candidates]}"
                    )
                source, source_kind = candidates[0]
                parsed_common = _parse_rpc2_common(payload, relative)
                source_payload = archive.read(info_by_relative[source])
                # MD5 is part of Ren'Py's on-disk RPC2 format, not a security
                # primitive used by this verifier.
                expected_source_md5 = hashlib.md5(
                    source_payload + RPYC_MAGIC, usedforsecurity=False
                ).digest()
                if (
                    parsed_common.source_md5 != expected_source_md5
                    and relative not in KNOWN_STALE_COMMON_SOURCE_MD5
                ):
                    raise VerificationError(
                        f"compiled common source MD5 does not match {source}: {relative}"
                    )
                source_kinds[source_kind] += 1
                parsed[relative] = parsed_common

            if require_release_contract:
                if len(parsed) != EXPECTED_CURRENT_RPC2_COUNT:
                    raise VerificationError(
                        "current RPC2 common count changed: "
                        f"{len(parsed)}/{EXPECTED_CURRENT_RPC2_COUNT}"
                    )
                if source_kinds != EXPECTED_CURRENT_SOURCE_KINDS:
                    raise VerificationError(
                        f"compiled common source-kind mapping changed: {source_kinds}"
                    )

            screen_serials: dict[str, list[int]] = {
                "standard": [],
                "developer": [],
            }
            for relative, parsed_common in sorted(parsed.items()):
                group = "developer" if _is_developer_common(relative) else "standard"
                screen_serials[group].extend(
                    record.value
                    for record in parsed_common.parsed_pickle.keyed_integers
                    if record.key == "serial"
                )
            standard_serials = screen_serials["standard"]
            all_screen_serials = standard_serials + screen_serials["developer"]
            if parsed and not standard_serials:
                raise VerificationError(
                    "compiled common contract has no standard screen serial base"
                )
            if len(all_screen_serials) != len(set(all_screen_serials)):
                raise VerificationError(
                    "compiled common screen serials are not globally unique"
                )
            if require_release_contract:
                if (
                    len(screen_serials["standard"])
                    != EXPECTED_STANDARD_SCREEN_SERIAL_COUNT
                    or len(screen_serials["developer"])
                    != EXPECTED_DEVELOPER_SCREEN_SERIAL_COUNT
                ):
                    raise VerificationError(
                        "compiled common screen-serial counts changed: "
                        f"standard={len(screen_serials['standard'])} "
                        f"developer={len(screen_serials['developer'])}"
                    )
                ordered_standard = sorted(screen_serials["standard"])
                if ordered_standard != list(
                    range(ordered_standard[0], ordered_standard[-1] + 1)
                ):
                    raise VerificationError(
                        "standard compiled common screen serials are no longer contiguous"
                    )

            screen_serial_minima = {
                group: min(values)
                for group, values in screen_serials.items()
                if values
            }
            # renpy.sl2.slast seeds serial with int(time.time() * 1_000_000),
            # while Script.assign_names derives name_version from the same run's
            # centisecond clock. Only the one nearby version per file is active.
            name_version_base = (
                (min(standard_serials) // 10_000) & 0x7FFFFFFF
                if standard_serials
                else None
            )
            active_versions: dict[str, int] = {}
            for relative, parsed_common in sorted(parsed.items()):
                candidates = {
                    record.value
                    for record in parsed_common.parsed_pickle.keyed_integers
                    if record.key == "name_version"
                    and name_version_base is not None
                    and 0
                    <= ((record.value - name_version_base) & 0x7FFFFFFF)
                    < ACTIVE_NAME_VERSION_WINDOW
                }
                if len(candidates) > 1:
                    raise VerificationError(
                        f"compiled common has multiple active name versions: {relative}"
                    )
                if candidates:
                    active_versions[relative] = next(iter(candidates))

            active_name_version_count = 0
            core_name_serials: list[int] = []
            module_name_serials: list[int] = []
            for relative, parsed_common in sorted(parsed.items()):
                keyed = parsed_common.parsed_pickle.keyed_integers
                active_version = active_versions.get(relative)
                for index, record in enumerate(keyed):
                    if record.key == "name_version" and record.value == active_version:
                        active_name_version_count += 1
                    if record.key != "name_serial":
                        continue
                    if index == 0 or keyed[index - 1].key != "name_version":
                        raise VerificationError(
                            f"compiled common name_serial is not paired with name_version: {relative}"
                        )
                    if keyed[index - 1].value != active_version:
                        continue
                    target = (
                        module_name_serials
                        if _is_module_common(relative)
                        else core_name_serials
                    )
                    target.append(record.value)

            if require_release_contract:
                active_paths_sha256 = _path_set_sha256(active_versions)
                if (
                    len(active_versions) != EXPECTED_ACTIVE_COMMON_COUNT
                    or active_paths_sha256 != EXPECTED_ACTIVE_COMMON_PATHS_SHA256
                ):
                    raise VerificationError(
                        "active compiled common path set changed: "
                        f"files={len(active_versions)}/{EXPECTED_ACTIVE_COMMON_COUNT} "
                        f"sha256={active_paths_sha256}"
                    )
                if active_name_version_count != EXPECTED_ACTIVE_NAME_VERSION_COUNT:
                    raise VerificationError(
                        "active common name_version count changed: "
                        f"{active_name_version_count}/{EXPECTED_ACTIVE_NAME_VERSION_COUNT}"
                    )
                if (
                    len(core_name_serials) != EXPECTED_CORE_NAME_SERIAL_COUNT
                    or set(core_name_serials)
                    != set(range(1, EXPECTED_CORE_NAME_SERIAL_COUNT + 1))
                ):
                    raise VerificationError(
                        "core common active name_serial sequence changed"
                    )
                if (
                    len(module_name_serials) != EXPECTED_MODULE_NAME_SERIAL_COUNT
                    or len(set(module_name_serials))
                    != EXPECTED_MODULE_NAME_SERIAL_COUNT
                    or max(module_name_serials) - min(module_name_serials) + 1
                    != EXPECTED_MODULE_NAME_SERIAL_COUNT
                ):
                    raise VerificationError(
                        "module common active name_serial sequence changed"
                    )

            module_name_serial_minimum = (
                min(module_name_serials) if module_name_serials else None
            )
            for relative, parsed_common in sorted(parsed.items()):
                records[relative] = CompiledCommonRecord(
                    "compiled-common-rpc2",
                    _canonical_compiled_pickle_digest(
                        relative,
                        parsed_common,
                        active_name_version=active_versions.get(relative),
                        screen_serial_minima=screen_serial_minima,
                        module_name_serial_minimum=module_name_serial_minimum,
                    ),
                )
            return records
    except VerificationError:
        raise
    except (OSError, RuntimeError, zipfile.BadZipFile, zipfile.LargeZipFile) as exc:
        raise VerificationError(
            f"cannot inspect compiled common contract in {path}: {exc}"
        ) from exc


def windows_runtime_fingerprint(
    members: Iterable[ArchiveMember],
    compiled_common_contract: Mapping[str, CompiledCommonRecord] | None = None,
) -> tuple[int, str]:
    """Hash the Windows runtime inventory with reviewed RPC2 normalization."""
    prefix = WINDOWS_ROOT + "/"
    records: list[tuple[str, str, str]] = []
    contract = compiled_common_contract or {}
    observed_compiled: set[str] = set()
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
            if _is_compiled_common(relative):
                observed_compiled.add(relative)
                compiled = contract.get(relative)
                if compiled is None:
                    raise VerificationError(
                        f"compiled common contract is missing: {relative}"
                    )
                records.append((relative, compiled.kind, compiled.digest))
            else:
                records.append(
                    (relative, str(member.file_size), f"{member.crc32:08x}")
                )

    unexpected_contract = set(contract) - observed_compiled
    if unexpected_contract:
        raise VerificationError(
            "compiled common contract contains absent paths: "
            + ", ".join(sorted(unexpected_contract))
        )

    digest = hashlib.sha256()
    for relative, size_or_kind, crc_or_digest in sorted(records):
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(size_or_kind.encode("ascii"))
        digest.update(b"\0")
        digest.update(crc_or_digest.encode("ascii"))
        digest.update(b"\n")
    return len(records), digest.hexdigest()


def validate_windows_runtime(
    members: Iterable[ArchiveMember],
    *,
    compiled_common_contract: Mapping[str, CompiledCommonRecord] | None = None,
    expected_count: int | None = None,
    expected_digest: str | None = None,
) -> list[str]:
    """Require the fixed Ren'Py 8.5.2 / 3.9.2 runtime inventory."""
    if expected_count is None:
        expected_count = EXPECTED_WINDOWS_RUNTIME_COUNT
    if expected_digest is None:
        expected_digest = EXPECTED_WINDOWS_RUNTIME_FINGERPRINT

    try:
        actual_count, actual_digest = windows_runtime_fingerprint(
            members, compiled_common_contract
        )
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
    launchable = re.search(
        r"^launchable-activity:\s+name='([^']+)'", output, re.MULTILINE
    )
    permissions = frozenset(
        re.findall(r"^uses-permission:\s+name='([^']+)'", output, re.MULTILINE)
    )
    if package is None or minimum is None or target is None:
        raise VerificationError("aapt badging output is missing required metadata")
    return {
        "package": package.group(1),
        "version_name": package.group(3),
        "version_code": int(package.group(2)),
        "min_sdk": int(minimum.group(1)),
        "target_sdk": int(target.group(1)),
        "launchable_activity": launchable.group(1) if launchable else None,
        "permissions": permissions,
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

    if current.get("launchable_activity") != EXPECTED_LAUNCHABLE_ACTIVITY:
        errors.append(
            f"ANDROID: launchable activity is {current.get('launchable_activity')!r}, "
            f"expected {EXPECTED_LAUNCHABLE_ACTIVITY!r}"
        )
    permissions = current.get("permissions")
    forbidden_permissions = (
        FORBIDDEN_ANDROID_PERMISSIONS.intersection(permissions)
        if isinstance(permissions, (set, frozenset))
        else FORBIDDEN_ANDROID_PERMISSIONS
    )
    if forbidden_permissions:
        errors.append(
            "ANDROID: forbidden permissions are present: "
            + ", ".join(sorted(forbidden_permissions))
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

    windows_compiled_contract: dict[str, CompiledCommonRecord] | None = None
    if "Windows" in inventories:
        try:
            windows_compiled_contract = inspect_compiled_common_contract(
                windows, inventories["Windows"]
            )
        except VerificationError as exc:
            errors.append(f"ARCHIVE Windows compiled common: {exc}")

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

    if windows_payload is not None and windows_compiled_contract is not None:
        errors.extend(
            validate_windows_runtime(
                inventories["Windows"],
                compiled_common_contract=windows_compiled_contract,
            )
        )
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

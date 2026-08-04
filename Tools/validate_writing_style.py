#!/usr/bin/env python3
"""Validate the user-approved Court of Shadows writing-style corpus."""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
from datetime import date
import json
from pathlib import Path
import re
from typing import Sequence


ROOT = Path(__file__).resolve().parents[1]
SCENE_TYPES = (
    "power_bargain",
    "mystery_reveal",
    "private_relationship",
    "governance_livelihood",
    "failure_compromise",
    "ending_epilogue",
)
SAMPLE_KINDS = ("full", "fragment")
TEXT_MODES = ("dialogue", "narration", "mixed")
MATURITY_STAGES = ("seed", "forming", "mature")
SAMPLE_FIELDS = {
    "schema_version",
    "id",
    "status",
    "scene_type",
    "characters",
    "text_mode",
    "sample_kind",
    "approved_on",
}
INDEX_FIELDS = {"schema_version", "maturity_stage"}
INDEX_HEADERS = (
    "ID",
    "scene_type",
    "characters",
    "text_mode",
    "sample_kind",
    "approved_on",
    "sample",
)
FAILURE_HEADERS = ("日期", "scene_type", "用户确认的失败原因")
GUIDANCE_HEADERS = (
    "guidance_id",
    "approved_on",
    "scene_type",
    "用户批准的指导",
)
BLIND_HEADERS = (
    "round_id",
    "scene_type",
    "library_position",
    "selection_method",
    "primary_position",
    "library_new_failure",
)
SELECTION_METHODS = (
    "single",
    "mixed_with_primary",
    "mixed_without_primary",
    "rejected_all",
)
INDEX_REFERENCE = "docs/writing-style/INDEX.md"
MAX_FAILURE_REASON_CHARS = 200
FORBIDDEN_ACTIVE_TOKENS = (
    "writing-game-copy",
    "jerian_zh.txt",
    "brante_zh.txt",
    "docs/archive/writing-style-legacy",
    "STYLE.md",
    "FORBIDDEN_PHRASES.md",
)
ACTIVE_ENTRYPOINTS = (
    "AGENTS.md",
    "CLAUDE.md",
    "CANON.md",
    "docs/writing-style/INDEX.md",
    "docs/writing-style/guidance.md",
)
ALLOWED_ACTIVE_SOURCES = {
    "AGENTS.md",
    "CLAUDE.md",
    "CANON.md",
    "INDEX.md",
    "failure-reasons.md",
    "guidance.md",
    "scene-card-template.md",
    "validation-log.md",
    "docs/writing-style/INDEX.md",
    "docs/writing-style/guidance.md",
    "docs/writing-style/scene-card-template.md",
}
SOURCE_PATH_TOKEN = re.compile(
    r"https?://[^\s)>\]}]+|"
    r"[A-Za-z]:[\\/]+[^\s)>\]}]+|"
    r"(?<![\w.])\.\.[\\/]+[^\s)>\]}]+|"
    r"(?<!\S)\\{2,}[^\s)>\]}]+|"
    r"(?:[A-Za-z0-9_.-]+[\\/])*"
    r"[A-Za-z0-9_.-]+\.(?:md|txt|rpy|json)",
    re.IGNORECASE,
)
STYLE_ALLOWED_ENTRIES = {
    "INDEX.md",
    "scene-card-template.md",
    "failure-reasons.md",
    "guidance.md",
    "validation-log.md",
    "approved",
}
INDEX_PREAMBLE = """# 《权谋之庭》原创文风库

## 调用边界

只读取 CANON.md、当前连续上下文与分支事实、guidance.md 中已批准的指导，
以及最多三个活动正例。
正例只能来自用户明确批准的最终文本。没有匹配正例时，标记为
“尚未校准”并进入三稿盲选。
fragment 只能保存用户明确圈定的原句，不得补写衔接。用户撤回正例时，
同步移除样本文件与索引行、重算 maturity_stage，且不转存为反例。
共同特征只有经用户逐条批准并写入 guidance.md 后才能成为活动指导。

## 检索顺序

同角色 > 同 scene_type > 同 text_mode > approved_on 较新。

## 成熟盲测

十二份 full 正例覆盖六类场景各两次后，每轮陌生场景只允许一稿读取
活动正例，另两稿作为不读取正例的对照。三稿使用同一事实卡并随机打乱。
validation-log.md 只按时间顺序记录确认后的轮次元数据，不保存候选原文。

## 活动正例"""


@dataclass(frozen=True)
class Sample:
    path: Path
    sample_id: str
    scene_type: str
    characters: tuple[str, ...]
    text_mode: str
    sample_kind: str
    approved_on: str


@dataclass(frozen=True)
class BlindRound:
    round_id: str
    scene_type: str
    library_position: str
    selection_method: str
    primary_position: str
    library_new_failure: str

    @property
    def eligible(self) -> bool:
        return self.selection_method in {"single", "mixed_with_primary"}

    @property
    def library_won(self) -> bool:
        return self.eligible and self.library_position == self.primary_position


def _relative(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def _normalized_source(raw_source: str) -> str:
    markdown_link = re.fullmatch(r"\[[^]]*\]\(([^)]+)\)", raw_source)
    if markdown_link:
        raw_source = markdown_link.group(1)
    source = raw_source.strip("`'\"(<[{>)]}.,;:")
    source = re.sub(r"[\\/]+", "/", source)
    source = re.sub(r":\d+(?:-\d+)?$", "", source)
    return source.casefold()


def _source_is_allowed(source: str, approved_sources: set[str]) -> bool:
    if source in {value.casefold() for value in ALLOWED_ACTIVE_SOURCES}:
        return True
    if source in approved_sources:
        return True
    if re.fullmatch(r"game/[^/]+\.rpy", source):
        return True
    if re.fullmatch(r"[^/]+\.rpy", source):
        return True
    if re.fullmatch(r"memory/(?:feedback|reference)_[^/]+\.md", source):
        return True
    if re.fullmatch(r"reference_[^/]+\.md", source):
        return True
    return False


def _active_source_errors(
    active_name: str,
    text: str,
    approved_sources: set[str],
) -> list[str]:
    findings: list[str] = []
    rejected: set[str] = set()
    for match in SOURCE_PATH_TOKEN.finditer(text):
        raw_source = match.group(0)
        source = _normalized_source(raw_source)
        if (
            source not in rejected
            and not _source_is_allowed(source, approved_sources)
        ):
            rejected.add(source)
            findings.append(
                f"{active_name}: unapproved active source {raw_source!r}"
            )
    return findings


def _front_matter(
    path: Path,
    root: Path,
    errors: list[str],
) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        errors.append(f"{_relative(path, root)}: missing front matter")
        return {}, ""
    header, body = text[4:].split("\n---\n", 1)
    metadata: dict[str, str] = {}
    for line in header.splitlines():
        if ":" not in line:
            errors.append(
                f"{_relative(path, root)}: invalid front-matter line {line!r}"
            )
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        if key in metadata:
            errors.append(
                f"{_relative(path, root)}: duplicate metadata field {key}"
            )
        metadata[key] = value.strip()
    return metadata, body.strip()


def _cells(line: str) -> tuple[str, ...]:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return ()
    return tuple(
        value.replace(r"\|", "|").strip()
        for value in re.split(r"(?<!\\)\|", stripped[1:-1])
    )


def _table_rows(
    path: Path,
    headers: tuple[str, ...],
    root: Path,
    errors: list[str],
    *,
    strict_file: bool = False,
) -> list[tuple[str, ...]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    expected_header = tuple(headers)
    header_index = next(
        (index for index, line in enumerate(lines) if _cells(line) == expected_header),
        None,
    )
    if header_index is None or header_index + 1 >= len(lines):
        errors.append(f"{_relative(path, root)}: missing expected table")
        return []
    separator = _cells(lines[header_index + 1])
    if len(separator) != len(headers) or not all(
        re.fullmatch(r":?-{3,}:?", cell) for cell in separator
    ):
        errors.append(f"{_relative(path, root)}: invalid table separator")
        return []
    rows: list[tuple[str, ...]] = []
    expected_title = {
        FAILURE_HEADERS: "# 已确认失败原因",
        GUIDANCE_HEADERS: "# 已批准活动指导",
        BLIND_HEADERS: "# 陌生场景盲测记录",
    }.get(headers)
    allowed_non_table = {"", expected_title}
    for index, line in enumerate(lines[header_index + 2 :], header_index + 3):
        if not line.strip():
            continue
        cells = _cells(line)
        if len(cells) != len(headers):
            errors.append(
                f"{_relative(path, root)}:{index}: expected {len(headers)} columns"
            )
            continue
        rows.append(cells)
    if strict_file:
        first_nonblank = next(
            (line.strip() for line in lines if line.strip()),
            "",
        )
        if first_nonblank != expected_title:
            errors.append(
                f"{_relative(path, root)}: invalid log title "
                f"{first_nonblank!r}"
            )
        for zero_index, line in enumerate(lines):
            stripped = line.strip()
            if not stripped or stripped in allowed_non_table:
                continue
            if zero_index in {header_index, header_index + 1}:
                continue
            if (
                zero_index > header_index + 1
                and len(_cells(line)) == len(headers)
            ):
                continue
            errors.append(
                f"{_relative(path, root)}:{zero_index + 1}: "
                "text outside the fixed table"
            )
    return rows


def _iso_date(value: str) -> bool:
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return True


def _parse_samples(
    approved_dir: Path,
    root: Path,
    errors: list[str],
) -> list[Sample]:
    samples: list[Sample] = []
    for path in sorted(approved_dir.glob("*.md")):
        metadata, body = _front_matter(path, root, errors)
        fields = set(metadata)
        if fields != SAMPLE_FIELDS:
            errors.append(
                f"{_relative(path, root)}: sample metadata fields "
                f"{sorted(fields)} do not match {sorted(SAMPLE_FIELDS)}"
            )
            continue
        sample_id = metadata["id"]
        scene_type = metadata["scene_type"]
        sample_kind = metadata["sample_kind"]
        text_mode = metadata["text_mode"]
        if metadata["schema_version"] != "1":
            errors.append(f"{_relative(path, root)}: schema_version must be 1")
        if not re.fullmatch(r"COS-[0-9]{3}", sample_id):
            errors.append(f"{_relative(path, root)}: invalid id {sample_id}")
        if not path.name.startswith(f"{sample_id}-"):
            errors.append(
                f"{_relative(path, root)}: filename must begin with {sample_id}-"
            )
        if metadata["status"] != "approved":
            errors.append(f"{_relative(path, root)}: status must be approved")
        if scene_type not in SCENE_TYPES:
            errors.append(
                f"{_relative(path, root)}: invalid scene_type {scene_type}"
            )
        if sample_kind not in SAMPLE_KINDS:
            errors.append(
                f"{_relative(path, root)}: invalid sample_kind {sample_kind}"
            )
        if text_mode not in TEXT_MODES:
            errors.append(f"{_relative(path, root)}: invalid text_mode {text_mode}")
        if not _iso_date(metadata["approved_on"]):
            errors.append(
                f"{_relative(path, root)}: invalid approved_on "
                f"{metadata['approved_on']}"
            )
        try:
            characters_value = json.loads(metadata["characters"])
        except json.JSONDecodeError:
            characters_value = None
        if (
            not isinstance(characters_value, list)
            or not characters_value
            or any(
                not isinstance(character, str) or not character.strip()
                for character in characters_value
            )
            or len(set(characters_value)) != len(characters_value)
        ):
            errors.append(
                f"{_relative(path, root)}: characters must be a unique "
                "non-empty JSON string array"
            )
            characters: tuple[str, ...] = ()
        else:
            characters = tuple(characters_value)
        if not body:
            errors.append(f"{_relative(path, root)}: approved body is empty")
        samples.append(
            Sample(
                path=path,
                sample_id=sample_id,
                scene_type=scene_type,
                characters=characters,
                text_mode=text_mode,
                sample_kind=sample_kind,
                approved_on=metadata["approved_on"],
            )
        )
    duplicates = {
        sample_id
        for sample_id, count in Counter(
            sample.sample_id for sample in samples
        ).items()
        if count > 1
    }
    for sample_id in sorted(duplicates):
        errors.append(f"docs/writing-style/approved: duplicate id {sample_id}")
    return samples


def _parse_blind_rounds(
    path: Path,
    root: Path,
    errors: list[str],
) -> list[BlindRound]:
    rounds: list[BlindRound] = []
    seen: set[str] = set()
    previous_round_number: int | None = None
    all_rows_valid = True
    error_count_before_table = len(errors)
    table_rows = _table_rows(
        path, BLIND_HEADERS, root, errors, strict_file=True
    )
    table_is_valid = len(errors) == error_count_before_table
    for cells in table_rows:
        record = dict(zip(BLIND_HEADERS, cells))
        round_id = record["round_id"]
        row_valid = True
        round_match = re.fullmatch(r"BT-([0-9]{3})", round_id)
        if round_match is None or round_id in seen:
            errors.append(f"{_relative(path, root)}: invalid round_id {round_id}")
            row_valid = False
        elif (
            previous_round_number is not None
            and int(round_match.group(1)) <= previous_round_number
        ):
            errors.append(
                f"{_relative(path, root)}: round numbers must increase "
                "in append order "
                f"({round_id} follows BT-{previous_round_number:03d})"
            )
            row_valid = False
        if round_match is not None:
            previous_round_number = int(round_match.group(1))
        seen.add(round_id)
        if record["scene_type"] not in SCENE_TYPES:
            errors.append(
                f"{_relative(path, root)}: invalid scene_type "
                f"{record['scene_type']}"
            )
            row_valid = False
        if record["library_position"] not in {"A", "B", "C"}:
            errors.append(
                f"{_relative(path, root)}: invalid library_position"
            )
            row_valid = False
        method = record["selection_method"]
        primary = record["primary_position"]
        if method not in SELECTION_METHODS:
            errors.append(f"{_relative(path, root)}: invalid selection_method")
            row_valid = False
        if method in {"single", "mixed_with_primary"} and primary not in {
            "A",
            "B",
            "C",
        }:
            errors.append(
                f"{_relative(path, root)}: eligible round needs a primary_position"
            )
            row_valid = False
        if method in {"mixed_without_primary", "rejected_all"} and primary != "-":
            errors.append(
                f"{_relative(path, root)}: ineligible round primary must be -"
            )
            row_valid = False
        if record["library_new_failure"] not in {"yes", "no"}:
            errors.append(
                f"{_relative(path, root)}: library_new_failure must be yes or no"
            )
            row_valid = False
        if row_valid:
            rounds.append(
                BlindRound(
                    round_id=round_id,
                    scene_type=record["scene_type"],
                    library_position=record["library_position"],
                    selection_method=method,
                    primary_position=primary,
                    library_new_failure=record["library_new_failure"],
                )
            )
        else:
            all_rows_valid = False
    return rounds if all_rows_valid and table_is_valid else []


def _derived_stage(samples: list[Sample], rounds: list[BlindRound]) -> str:
    full = [sample for sample in samples if sample.sample_kind == "full"]
    coverage = Counter(sample.scene_type for sample in full)
    if len(full) < 6 or any(coverage[scene] < 1 for scene in SCENE_TYPES):
        return "seed"
    if len(full) < 12 or any(coverage[scene] < 2 for scene in SCENE_TYPES):
        return "forming"
    evidence = [record for record in rounds if record.eligible][-3:]
    if len(evidence) < 3:
        return "forming"
    if sum(record.library_won for record in evidence) < 2:
        return "forming"
    if any(record.library_new_failure == "yes" for record in evidence):
        return "forming"
    return "mature"


def validate_project(root: Path = ROOT) -> list[str]:
    """Return every structural finding; return an empty list on success."""
    root = root.resolve()
    errors: list[str] = []
    style = root / "docs" / "writing-style"
    approved = style / "approved"
    required = (
        root / "AGENTS.md",
        root / "CLAUDE.md",
        root / "CANON.md",
        style / "INDEX.md",
        style / "scene-card-template.md",
        style / "failure-reasons.md",
        style / "guidance.md",
        style / "validation-log.md",
        approved / ".gitkeep",
        root / "docs" / "archive" / "writing-style-legacy" / "STYLE.md",
        root
        / "docs"
        / "archive"
        / "writing-style-legacy"
        / "FORBIDDEN_PHRASES.md",
    )
    for path in required:
        if not path.is_file():
            errors.append(f"{_relative(path, root)}: required file is missing")
    if style.is_dir():
        for entry in sorted(style.iterdir()):
            if entry.name not in STYLE_ALLOWED_ENTRIES:
                errors.append(
                    "docs/writing-style: unexpected writing-style entry "
                    f"{entry.name}"
                )
    if not approved.is_dir():
        errors.append("docs/writing-style/approved: required directory is missing")
    else:
        for entry in sorted(approved.iterdir()):
            if entry.name == ".gitkeep":
                if (
                    not entry.is_file()
                    or entry.is_symlink()
                    or entry.stat().st_size != 0
                ):
                    errors.append(
                        "docs/writing-style/approved/.gitkeep must be an "
                        "empty regular file"
                    )
                continue
            if entry.is_file() and entry.suffix == ".md":
                continue
            errors.append(
                "docs/writing-style/approved: unexpected approved corpus entry "
                f"{entry.name}"
            )
    for legacy_name in ("STYLE.md", "FORBIDDEN_PHRASES.md"):
        if (root / legacy_name).exists():
            errors.append(f"{legacy_name}: legacy writing source remains active")
    approved_sources = (
        {
            value.casefold()
            for path in approved.glob("*.md")
            for value in (
                f"docs/writing-style/approved/{path.name}",
                f"approved/{path.name}",
            )
        }
        if approved.is_dir()
        else set()
    )
    for active_name in ACTIVE_ENTRYPOINTS:
        path = root / active_name
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        if (
            active_name in {"AGENTS.md", "CLAUDE.md", "CANON.md"}
            and INDEX_REFERENCE not in text
        ):
            errors.append(f"{active_name}: missing {INDEX_REFERENCE}")
        errors.extend(_active_source_errors(active_name, text, approved_sources))
        for token in FORBIDDEN_ACTIVE_TOKENS:
            if token.casefold() in text.casefold():
                errors.append(f"{active_name}: forbidden active source {token}")
    if errors and not style.is_dir():
        return errors

    index = style / "INDEX.md"
    index_metadata: dict[str, str] = {}
    if index.is_file():
        index_metadata, index_body = _front_matter(index, root, errors)
        if set(index_metadata) != INDEX_FIELDS:
            errors.append(
                "docs/writing-style/INDEX.md: front-matter fields must be "
                "schema_version and maturity_stage"
            )
        if index_metadata.get("schema_version") != "1":
            errors.append(
                "docs/writing-style/INDEX.md: schema_version must be 1"
            )
        if index_metadata.get("maturity_stage") not in MATURITY_STAGES:
            errors.append(
                "docs/writing-style/INDEX.md: invalid maturity_stage"
            )
        index_table_header = "| " + " | ".join(INDEX_HEADERS) + " |"
        index_prefix, marker, _ = index_body.partition(index_table_header)
        if not marker or index_prefix.rstrip() != INDEX_PREAMBLE:
            errors.append(
                "docs/writing-style/INDEX.md: content outside fixed index preamble"
            )

    samples = _parse_samples(approved, root, errors) if approved.is_dir() else []
    samples_by_path = {
        f"approved/{sample.path.name}": sample for sample in samples
    }
    indexed_paths: list[str] = []
    if index.is_file():
        for cells in _table_rows(index, INDEX_HEADERS, root, errors):
            row = dict(zip(INDEX_HEADERS, cells))
            match = re.fullmatch(
                r"\[文本\]\((approved/[^)]+\.md)\)",
                row["sample"],
            )
            if match is None:
                errors.append(
                    "docs/writing-style/INDEX.md: invalid sample link "
                    f"{row['sample']}"
                )
                continue
            relative_sample = match.group(1)
            indexed_paths.append(relative_sample)
            sample = samples_by_path.get(relative_sample)
            if sample is None:
                errors.append(
                    "docs/writing-style/INDEX.md: dangling index link "
                    f"{relative_sample}"
                )
                continue
            expected = {
                "ID": sample.sample_id,
                "scene_type": sample.scene_type,
                "characters": ", ".join(sample.characters),
                "text_mode": sample.text_mode,
                "sample_kind": sample.sample_kind,
                "approved_on": sample.approved_on,
            }
            for key, value in expected.items():
                if row[key] != value:
                    errors.append(
                        "docs/writing-style/INDEX.md: "
                        f"{relative_sample} {key} does not match sample metadata"
                    )
        for relative_sample in sorted(
            set(samples_by_path) - set(indexed_paths)
        ):
            errors.append(
                "docs/writing-style/INDEX.md: sample missing from index "
                f"{relative_sample}"
            )
        for relative_sample, count in Counter(indexed_paths).items():
            if count > 1:
                errors.append(
                    "docs/writing-style/INDEX.md: duplicate sample link "
                    f"{relative_sample}"
                )

    failure_path = style / "failure-reasons.md"
    if failure_path.is_file():
        for cells in _table_rows(
            failure_path,
            FAILURE_HEADERS,
            root,
            errors,
            strict_file=True,
        ):
            row = dict(zip(FAILURE_HEADERS, cells))
            if not _iso_date(row["日期"]):
                errors.append(
                    "docs/writing-style/failure-reasons.md: invalid date"
                )
            if row["scene_type"] not in SCENE_TYPES:
                errors.append(
                    "docs/writing-style/failure-reasons.md: invalid scene_type"
                )
            reason = row["用户确认的失败原因"].strip()
            if not reason:
                errors.append(
                    "docs/writing-style/failure-reasons.md: empty reason"
                )
            elif len(reason) > MAX_FAILURE_REASON_CHARS:
                errors.append(
                    "docs/writing-style/failure-reasons.md: reason exceeds "
                    f"{MAX_FAILURE_REASON_CHARS} characters"
                )

    guidance_path = style / "guidance.md"
    guidance_ids: list[str] = []
    if guidance_path.is_file():
        for cells in _table_rows(
            guidance_path,
            GUIDANCE_HEADERS,
            root,
            errors,
            strict_file=True,
        ):
            row = dict(zip(GUIDANCE_HEADERS, cells))
            guidance_id = row["guidance_id"]
            guidance_ids.append(guidance_id)
            if not re.fullmatch(r"COS-G[0-9]{3}", guidance_id):
                errors.append(
                    "docs/writing-style/guidance.md: invalid guidance_id "
                    f"{guidance_id}"
                )
            if not _iso_date(row["approved_on"]):
                errors.append(
                    "docs/writing-style/guidance.md: invalid guidance approved_on"
                )
            if row["scene_type"] not in {*SCENE_TYPES, "all"}:
                errors.append(
                    "docs/writing-style/guidance.md: invalid guidance scene_type"
                )
            if not row["用户批准的指导"].strip():
                errors.append(
                    "docs/writing-style/guidance.md: empty approved guidance"
                )
    for guidance_id, count in Counter(guidance_ids).items():
        if count > 1:
            errors.append(
                "docs/writing-style/guidance.md: duplicate guidance_id "
                f"{guidance_id}"
            )

    validation_path = style / "validation-log.md"
    rounds = (
        _parse_blind_rounds(validation_path, root, errors)
        if validation_path.is_file()
        else []
    )
    derived_stage = _derived_stage(samples, rounds)
    declared_stage = index_metadata.get("maturity_stage")
    if declared_stage in MATURITY_STAGES and declared_stage != derived_stage:
        errors.append(
            "docs/writing-style/INDEX.md: declared maturity_stage "
            f"{declared_stage} does not match {derived_stage}"
        )
    return errors


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args(argv)
    errors = validate_project(args.root)
    if errors:
        for error in errors:
            print(f"ERROR {error}")
        return 1
    print("PASS writing-style structure is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

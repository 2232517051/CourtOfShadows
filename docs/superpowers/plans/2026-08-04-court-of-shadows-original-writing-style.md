# Court of Shadows Original Writing Style Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (- [ ]) syntax for tracking.

**Goal:** Build a project-local, user-approved writing-style corpus for Court of Shadows, retire the legacy rule manuals from active use, and provide deterministic structural and release gates without changing game narrative.

**Architecture:** A zero-dependency Python validator treats Markdown files under docs/writing-style as a small constrained data store. Project instruction files route narrative work through CANON, exact scene state, and at most three approved samples; legacy manuals move under docs/archive and remain recoverable. Ren'Py packaging rules continue excluding every development-only file.

**Tech Stack:** Python 3.11 standard library, unittest, Markdown with constrained front matter and tables, Ren'Py 8.5.2 build classification, PowerShell, Git.

## Global Constraints

- Scope is Court of Shadows only; do not create or reactivate a global writing skill.
- Only text explicitly approved by the user after a clean-copy confirmation may enter approved/.
- A fragment contains only the exact sentences the user identifies; never add inferred context or bridge text.
- Rejected drafts are never written to disk; only a user-confirmed failure reason may be stored.
- A stored failure reason is at most 200 characters; any compression or paraphrase requires separate user confirmation.
- Candidate generation may read CANON.md, exact live context, branch facts,
  user-approved guidance, and at most three approved samples.
- A shared style observation becomes active guidance only after the user explicitly approves its clean wording; model-authored summaries never enter by default.
- Retrieval priority is same character, then same scene_type, then same text_mode, then newest approved_on.
- Do not read legacy writing manuals, external game corpora, rejected drafts, or unapproved model summaries as style inputs.
- The six scene_type values are power_bargain, mystery_reveal, private_relationship, governance_livelihood, failure_compromise, and ending_epilogue.
- sample_kind is full or fragment; only full samples count toward maturity.
- Seed remains active until six full samples cover all six scene types once.
- Forming remains active until twelve full samples cover all six scene types twice and the blind-test gate passes.
- Mature requires the latest three eligible blind tests, at least two library-informed primary selections, and no new user-confirmed failure reason from the library-informed candidates.
- Automatic checks judge structure and provenance boundaries only; the user is the sole judge of prose quality.
- Keep the existing canon, portrait, Ren'Py lint, regression, and release gates.
- scan_ai_smell.py remains a non-blocking historical diagnostic and never decides prose acceptance.
- Do not modify any game/*.rpy narrative in Tasks 1-3.
- Do not add an approved sample, failure-reason row, or blind-test row before the corresponding user confirmation.
- A user-requested sample withdrawal removes its active sample file and INDEX row together, recomputes maturity, and never creates a negative example; Git history remains the recovery path.
- Start implementation only from a clean worktree where this plan is already tracked and committed.
- Use no third-party Python dependency.
- No art, music, sound effect, animation, UI asset, or package-size addition is required.

---

## File Map

**Create**

- AGENTS.md — Codex entry point for project development and narrative workflow.
- docs/writing-style/INDEX.md — active stage, retrieval contract, and exact sample index.
- docs/writing-style/scene-card-template.md — fact-only calibration input.
- docs/writing-style/failure-reasons.md — user-confirmed one-line failure reasons.
- docs/writing-style/guidance.md — user-approved shared observations, initially empty.
- docs/writing-style/validation-log.md — blind-test metadata without candidate prose.
- docs/writing-style/approved/.gitkeep — tracks the intentionally empty corpus directory.
- Tools/validate_writing_style.py — structural validator and CLI.
- Tools/test_writing_style_system.py — temporary-fixture and live-tree contracts.

**Move without editing**

- STYLE.md to docs/archive/writing-style-legacy/STYLE.md.
- FORBIDDEN_PHRASES.md to docs/archive/writing-style-legacy/FORBIDDEN_PHRASES.md.

**Modify**

- CLAUDE.md — replace the active writing entry point while preserving technical gates.
- CANON.md — separate fact authority from style authority.
- Tools/scan_ai_smell.py — label the scanner non-blocking and remove legacy authority claims.
- Tools/test_release_contract.py — replace stale root exclusions with AGENTS.md and verify archived guides.
- game/options.rpy — mirror the release-contract exclusion changes.
- docs/superpowers/specs/2026-08-04-court-of-shadows-original-writing-style-design.md — mark the reviewed design as confirmed.

---

### Task 1: Build the zero-dependency writing-style validator

**Files:**

- Create: Tools/test_writing_style_system.py
- Create: Tools/validate_writing_style.py

**Interfaces:**

- Produces: SCENE_TYPES and SAMPLE_KINDS as immutable tuples, plus the fixed
  INDEX_PREAMBLE used as the active-source whitelist.
- Produces: validate_project(root: pathlib.Path = ROOT) -> list[str].
- Produces: main(argv: Sequence[str] | None = None) -> int.
- Consumes: only pathlib, argparse, collections, dataclasses, datetime, json, re, and typing from the Python standard library.

- [ ] **Step 1: Write the failing validator tests**

Create Tools/test_writing_style_system.py with this initial content:

~~~python
from __future__ import annotations

from contextlib import redirect_stdout
import io
import tempfile
import unittest
from pathlib import Path

from Tools import validate_writing_style as validator


SCENES = (
    "power_bargain",
    "mystery_reveal",
    "private_relationship",
    "governance_livelihood",
    "failure_compromise",
    "ending_epilogue",
)


class WritingStyleTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.style = self.root / "docs" / "writing-style"
        (self.style / "approved").mkdir(parents=True)
        archive = self.root / "docs" / "archive" / "writing-style-legacy"
        archive.mkdir(parents=True)
        (archive / "STYLE.md").write_text("legacy style\n", encoding="utf-8")
        (archive / "FORBIDDEN_PHRASES.md").write_text(
            "legacy phrases\n", encoding="utf-8"
        )
        self.write(
            "AGENTS.md",
            "# Agent rules\nRead docs/writing-style/INDEX.md for game copy.\n",
        )
        self.write(
            "CLAUDE.md",
            "# Development rules\nRead docs/writing-style/INDEX.md for game copy.\n",
        )
        self.write(
            "CANON.md",
            "# Canon\nFacts only. Style index: docs/writing-style/INDEX.md\n",
        )
        self.write(
            "docs/writing-style/scene-card-template.md",
            "# Scene card\n\nTarget length: 250-450 Chinese characters.\n",
        )
        self.write(
            "docs/writing-style/failure-reasons.md",
            "# 已确认失败原因\n\n"
            "| 日期 | scene_type | 用户确认的失败原因 |\n"
            "|---|---|---|\n",
        )
        self.write(
            "docs/writing-style/guidance.md",
            "# 已批准活动指导\n\n"
            "| guidance_id | approved_on | scene_type | 用户批准的指导 |\n"
            "|---|---|---|---|\n",
        )
        self.write(
            "docs/writing-style/validation-log.md",
            "# 陌生场景盲测记录\n\n"
            "| round_id | scene_type | library_position | selection_method | "
            "primary_position | library_new_failure |\n"
            "|---|---|---|---|---|---|\n",
        )
        self.samples: list[dict[str, str]] = []
        self.stage = "seed"
        self.sync_index()

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def write(self, relative: str, text: str) -> None:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def add_sample(
        self,
        sample_id: str,
        scene_type: str,
        *,
        sample_kind: str = "full",
        status: str = "approved",
    ) -> None:
        filename = f"{sample_id}-{scene_type}.md"
        metadata = {
            "id": sample_id,
            "scene_type": scene_type,
            "characters": '["player", "ingrid"]',
            "text_mode": "mixed",
            "sample_kind": sample_kind,
            "approved_on": "2026-08-04",
            "filename": filename,
        }
        self.samples.append(metadata)
        self.write(
            f"docs/writing-style/approved/{filename}",
            "---\n"
            "schema_version: 1\n"
            f"id: {sample_id}\n"
            f"status: {status}\n"
            f"scene_type: {scene_type}\n"
            'characters: ["player", "ingrid"]\n'
            "text_mode: mixed\n"
            f"sample_kind: {sample_kind}\n"
            "approved_on: 2026-08-04\n"
            "---\n\n"
            "这是用户明确批准的完整测试文本。\n",
        )
        self.sync_index()

    def sync_index(self) -> None:
        rows = "".join(
            "| {id} | {scene_type} | player, ingrid | mixed | "
            "{sample_kind} | {approved_on} | "
            "[文本](approved/{filename}) |\n".format(**sample)
            for sample in self.samples
        )
        self.write(
            "docs/writing-style/INDEX.md",
            "---\n"
            "schema_version: 1\n"
            f"maturity_stage: {self.stage}\n"
            "---\n\n"
            f"{validator.INDEX_PREAMBLE}\n\n"
            "| ID | scene_type | characters | text_mode | sample_kind | "
            "approved_on | sample |\n"
            "|---|---|---|---|---|---|---|\n"
            f"{rows}",
        )

    def set_stage(self, stage: str) -> None:
        self.stage = stage
        self.sync_index()

    def set_blind_rounds(self, rows: list[str]) -> None:
        self.write(
            "docs/writing-style/validation-log.md",
            "# 陌生场景盲测记录\n\n"
            "| round_id | scene_type | library_position | selection_method | "
            "primary_position | library_new_failure |\n"
            "|---|---|---|---|---|---|\n"
            + "".join(f"{row}\n" for row in rows),
        )


class WritingStyleBootstrapTests(WritingStyleTestCase):
    def test_empty_seed_library_is_valid(self) -> None:
        self.assertEqual(validator.validate_project(self.root), [])

    def test_cli_returns_zero_for_success_and_one_for_findings(self) -> None:
        with redirect_stdout(io.StringIO()) as output:
            self.assertEqual(validator.main(["--root", str(self.root)]), 0)
        self.assertIn("PASS", output.getvalue())

        self.write(
            "docs/writing-style/approved/bad.md",
            "not front matter\n",
        )
        with redirect_stdout(io.StringIO()) as output:
            self.assertEqual(validator.main(["--root", str(self.root)]), 1)
        self.assertIn("bad.md", output.getvalue())


class ApprovedSampleGuardTests(WritingStyleTestCase):
    def test_invalid_scene_type_and_status_are_rejected(self) -> None:
        self.add_sample("COS-001", "unknown_scene", status="draft")
        report = "\n".join(validator.validate_project(self.root))
        self.assertIn("invalid scene_type", report)
        self.assertIn("status must be approved", report)

    def test_duplicate_ids_are_rejected(self) -> None:
        self.add_sample("COS-001", SCENES[0])
        self.add_sample("COS-001", SCENES[1])
        self.assertIn(
            "duplicate id COS-001",
            "\n".join(validator.validate_project(self.root)),
        )

    def test_fragments_do_not_advance_maturity(self) -> None:
        for index, scene_type in enumerate(SCENES, 1):
            self.add_sample(
                f"COS-{index:03d}",
                scene_type,
                sample_kind="fragment",
            )
        self.assertEqual(validator.validate_project(self.root), [])

    def test_dangling_link_and_unindexed_sample_are_rejected(self) -> None:
        self.add_sample("COS-001", SCENES[0])
        index = self.style / "INDEX.md"
        index.write_text(
            index.read_text(encoding="utf-8").replace(
                "approved/COS-001-power_bargain.md",
                "approved/COS-999-missing.md",
            ),
            encoding="utf-8",
        )
        report = "\n".join(validator.validate_project(self.root))
        self.assertIn("dangling index link", report)
        self.assertIn("sample missing from index", report)

    def test_non_sample_file_in_approved_directory_is_rejected(self) -> None:
        self.write(
            "docs/writing-style/approved/rejected-draft.txt",
            "This must never become retained corpus material.\n",
        )
        self.assertIn(
            "unexpected approved corpus entry",
            "\n".join(validator.validate_project(self.root)),
        )

    def test_unexpected_top_level_style_file_is_rejected(self) -> None:
        self.write(
            "docs/writing-style/rejected-draft.md",
            "Rejected prose must not be retained beside the corpus.\n",
        )
        self.assertIn(
            "unexpected writing-style entry",
            "\n".join(validator.validate_project(self.root)),
        )


class ActiveSourceContractTests(WritingStyleTestCase):
    def test_active_entrypoint_cannot_reference_legacy_archive(self) -> None:
        index = self.style / "INDEX.md"
        index.write_text(
            index.read_text(encoding="utf-8")
            + "\nLegacy: Docs/Archive/Writing-Style-Legacy/style.md\n",
            encoding="utf-8",
        )
        self.assertIn(
            "forbidden active source",
            "\n".join(validator.validate_project(self.root)),
        )

    def test_index_rejects_arbitrary_content_outside_fixed_contract(self) -> None:
        index = self.style / "INDEX.md"
        index.write_text(
            index.read_text(encoding="utf-8").replace(
                "## 活动正例",
                "[外部范文](D:/OtherGame/script.rpy)\n\n## 活动正例",
            ),
            encoding="utf-8",
        )
        self.assertIn(
            "fixed index preamble",
            "\n".join(validator.validate_project(self.root)),
        )


class MaturityContractTests(WritingStyleTestCase):
    def test_six_full_scene_types_form_a_forming_library(self) -> None:
        for index, scene_type in enumerate(SCENES, 1):
            self.add_sample(f"COS-{index:03d}", scene_type)
        self.set_stage("forming")
        self.assertEqual(validator.validate_project(self.root), [])

    def test_twelve_full_samples_without_blind_evidence_remain_forming(self) -> None:
        sample_number = 1
        for _ in range(2):
            for scene_type in SCENES:
                self.add_sample(f"COS-{sample_number:03d}", scene_type)
                sample_number += 1
        self.set_stage("mature")
        self.assertIn(
            "declared maturity_stage mature does not match forming",
            "\n".join(validator.validate_project(self.root)),
        )

    def test_three_eligible_blind_rounds_can_make_the_library_mature(self) -> None:
        sample_number = 1
        for _ in range(2):
            for scene_type in SCENES:
                self.add_sample(f"COS-{sample_number:03d}", scene_type)
                sample_number += 1
        self.set_blind_rounds(
            [
                "| BT-001 | power_bargain | A | single | A | no |",
                "| BT-002 | mystery_reveal | C | mixed_with_primary | C | no |",
                "| BT-003 | ending_epilogue | B | single | A | no |",
            ]
        )
        self.set_stage("mature")
        self.assertEqual(validator.validate_project(self.root), [])


class LogContractTests(WritingStyleTestCase):
    def test_failure_reason_rows_must_be_three_column_single_lines(self) -> None:
        self.write(
            "docs/writing-style/failure-reasons.md",
            "# 已确认失败原因\n\n"
            "| 日期 | scene_type | 用户确认的失败原因 |\n"
            "|---|---|---|\n"
            "| 2026-08-04 | power_bargain | 原因 | 多余列 |\n",
        )
        self.assertIn(
            "failure-reasons.md",
            "\n".join(validator.validate_project(self.root)),
        )

    def test_failure_reason_cannot_hold_candidate_length_prose(self) -> None:
        self.write(
            "docs/writing-style/failure-reasons.md",
            "# 已确认失败原因\n\n"
            "| 日期 | scene_type | 用户确认的失败原因 |\n"
            "|---|---|---|\n"
            f"| 2026-08-04 | power_bargain | {'废' * 201} |\n",
        )
        self.assertIn(
            "reason exceeds 200 characters",
            "\n".join(validator.validate_project(self.root)),
        )

    def test_guidance_rows_require_valid_unique_approved_metadata(self) -> None:
        self.write(
            "docs/writing-style/guidance.md",
            "# 已批准活动指导\n\n"
            "| guidance_id | approved_on | scene_type | 用户批准的指导 |\n"
            "|---|---|---|---|\n"
            "| COS-G001 | not-a-date | unknown |  |\n"
            "| COS-G001 | 2026-08-04 | all | 保留具体动作。 |\n",
        )
        report = "\n".join(validator.validate_project(self.root))
        self.assertIn("duplicate guidance_id COS-G001", report)
        self.assertIn("invalid guidance approved_on", report)
        self.assertIn("invalid guidance scene_type", report)
        self.assertIn("empty approved guidance", report)


if __name__ == "__main__":
    unittest.main()
~~~

- [ ] **Step 2: Run the focused test to verify RED**

Run:

~~~powershell
python -B -m unittest Tools.test_writing_style_system -v
~~~

Expected: FAIL during import with ImportError because Tools.validate_writing_style does not exist yet.

- [ ] **Step 3: Implement the validator**

Create Tools/validate_writing_style.py with this content:

~~~python
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
    for cells in _table_rows(
        path, BLIND_HEADERS, root, errors, strict_file=True
    ):
        record = dict(zip(BLIND_HEADERS, cells))
        round_id = record["round_id"]
        if not re.fullmatch(r"BT-[0-9]{3}", round_id) or round_id in seen:
            errors.append(f"{_relative(path, root)}: invalid round_id {round_id}")
        seen.add(round_id)
        if record["scene_type"] not in SCENE_TYPES:
            errors.append(
                f"{_relative(path, root)}: invalid scene_type "
                f"{record['scene_type']}"
            )
        if record["library_position"] not in {"A", "B", "C"}:
            errors.append(
                f"{_relative(path, root)}: invalid library_position"
            )
        method = record["selection_method"]
        primary = record["primary_position"]
        if method not in SELECTION_METHODS:
            errors.append(f"{_relative(path, root)}: invalid selection_method")
        if method in {"single", "mixed_with_primary"} and primary not in {
            "A",
            "B",
            "C",
        }:
            errors.append(
                f"{_relative(path, root)}: eligible round needs a primary_position"
            )
        if method in {"mixed_without_primary", "rejected_all"} and primary != "-":
            errors.append(
                f"{_relative(path, root)}: ineligible round primary must be -"
            )
        if record["library_new_failure"] not in {"yes", "no"}:
            errors.append(
                f"{_relative(path, root)}: library_new_failure must be yes or no"
            )
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
    return rounds


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
            if entry.is_file() and entry.name == ".gitkeep":
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
    for active_name in (
        "AGENTS.md",
        "CLAUDE.md",
        "CANON.md",
        "docs/writing-style/INDEX.md",
        "docs/writing-style/guidance.md",
    ):
        path = root / active_name
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        if (
            active_name in {"AGENTS.md", "CLAUDE.md", "CANON.md"}
            and INDEX_REFERENCE not in text
        ):
            errors.append(f"{active_name}: missing {INDEX_REFERENCE}")
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
~~~

- [ ] **Step 4: Run the focused tests to verify GREEN**

Run:

~~~powershell
python -B -m unittest Tools.test_writing_style_system -v
~~~

Expected: 16 tests run and OK.

- [ ] **Step 5: Commit the validator**

Run:

~~~powershell
git add -- Tools/validate_writing_style.py Tools/test_writing_style_system.py
git diff --cached --check
git commit -m "test: add writing style corpus validator"
~~~

Expected: one commit containing only the validator and its temporary-fixture tests.

---

### Task 2: Establish the empty corpus and retire legacy writing inputs

**Files:**

- Modify: Tools/test_writing_style_system.py
- Create: AGENTS.md
- Create: docs/writing-style/INDEX.md
- Create: docs/writing-style/scene-card-template.md
- Create: docs/writing-style/failure-reasons.md
- Create: docs/writing-style/guidance.md
- Create: docs/writing-style/validation-log.md
- Create: docs/writing-style/approved/.gitkeep
- Move: STYLE.md to docs/archive/writing-style-legacy/STYLE.md
- Move: FORBIDDEN_PHRASES.md to docs/archive/writing-style-legacy/FORBIDDEN_PHRASES.md
- Modify: CLAUDE.md:3-17
- Modify: CANON.md:4
- Modify: Tools/scan_ai_smell.py:1-19,89,169-172
- Modify: docs/superpowers/specs/2026-08-04-court-of-shadows-original-writing-style-design.md:5,103-163,184-198

**Interfaces:**

- Consumes: validate_project(root) from Task 1.
- Produces: a live seed-stage corpus with zero approved Markdown samples and
  zero active-guidance rows.
- Produces: project instructions that enforce the explicit-approval protocol.
- Preserves: every non-writing technical gate already present in CLAUDE.md.

- [ ] **Step 1: Add live-project contract tests**

Insert this class above the unittest.main guard in Tools/test_writing_style_system.py:

~~~python
ROOT = Path(__file__).resolve().parents[1]


class LiveProjectWritingStyleContractTests(unittest.TestCase):
    def test_real_project_structure_passes(self) -> None:
        self.assertEqual(validator.validate_project(ROOT), [])

    def test_historical_scanner_is_explicitly_non_blocking(self) -> None:
        scanner = (ROOT / "Tools" / "scan_ai_smell.py").read_text(
            encoding="utf-8"
        )
        self.assertIn("不作为文风通过门槛", scanner)
        self.assertIn("docs/writing-style/INDEX.md", scanner)
        self.assertNotIn("对照 FORBIDDEN_PHRASES.md 修", scanner)
~~~

- [ ] **Step 2: Run the live tests to verify RED**

Run:

~~~powershell
python -B -m unittest Tools.test_writing_style_system.LiveProjectWritingStyleContractTests -v
~~~

Expected: two failures. The first lists the missing style directory, missing AGENTS.md, active root legacy files, and missing archive files. The second reports that scan_ai_smell.py still treats the old guide as authority.

- [ ] **Step 3: Verify and move the two exact legacy files**

Run one PowerShell command. It resolves and hashes both exact sources before
performing the moves, then compares both archive hashes in the same process:

~~~powershell
$projectRoot = (Get-Item -LiteralPath '.').FullName
$legacyStyle = (Get-Item -LiteralPath 'STYLE.md').FullName
$legacyPhrases = (Get-Item -LiteralPath 'FORBIDDEN_PHRASES.md').FullName
$archiveRoot = [IO.Path]::GetFullPath((Join-Path $projectRoot 'docs\archive\writing-style-legacy'))
$styleDestination = Join-Path $archiveRoot 'STYLE.md'
$phrasesDestination = Join-Path $archiveRoot 'FORBIDDEN_PHRASES.md'
if (-not $legacyStyle.StartsWith($projectRoot + '\')) { throw 'STYLE source escaped project root' }
if (-not $legacyPhrases.StartsWith($projectRoot + '\')) { throw 'FORBIDDEN source escaped project root' }
if (-not $archiveRoot.StartsWith($projectRoot + '\')) { throw 'Archive target escaped project root' }
if (Test-Path -LiteralPath $styleDestination) { throw 'STYLE archive target already exists' }
if (Test-Path -LiteralPath $phrasesDestination) { throw 'FORBIDDEN archive target already exists' }
$styleHashBefore = (Get-FileHash -LiteralPath $legacyStyle -Algorithm SHA256).Hash
$phrasesHashBefore = (Get-FileHash -LiteralPath $legacyPhrases -Algorithm SHA256).Hash
$styleHashBefore
$phrasesHashBefore
New-Item -ItemType Directory -Path 'docs\archive\writing-style-legacy' -Force | Out-Null
git mv -- 'STYLE.md' 'docs/archive/writing-style-legacy/STYLE.md'
git mv -- 'FORBIDDEN_PHRASES.md' 'docs/archive/writing-style-legacy/FORBIDDEN_PHRASES.md'
$styleHashAfter = (Get-FileHash -LiteralPath $styleDestination -Algorithm SHA256).Hash
$phrasesHashAfter = (Get-FileHash -LiteralPath $phrasesDestination -Algorithm SHA256).Hash
if ($styleHashAfter -ne $styleHashBefore) { throw 'STYLE archive hash changed' }
if ($phrasesHashAfter -ne $phrasesHashBefore) { throw 'FORBIDDEN archive hash changed' }
~~~

Verify both root paths are absent and both archive paths exist. Do not edit the archived contents.

- [ ] **Step 4: Create the active project instructions**

Create AGENTS.md with:

~~~markdown
# Court of Shadows Project Instructions

All development work follows the technical, presentation, testing, release,
and asset rules in CLAUDE.md.

## Game-copy workflow

Before drafting or changing dialogue, narration, choices, letters, quests,
descriptions, or endings:

1. Read CANON.md.
2. Read the exact continuous scene context, branch variables, physical state,
   and each character's known and unknown information.
3. Read docs/writing-style/INDEX.md.
4. Read only the rows already present in docs/writing-style/guidance.md.
5. Load at most three active approved samples in this order: same character,
   same scene_type, same text_mode, then newer approved_on.
6. If no suitable sample exists, mark the passage uncalibrated and use the
   three-draft blind workflow.

The three candidates must be produced in isolated contexts and cannot see one
another. During seed stage, calibration scenes do not modify formal game
scripts.

After twelve full samples cover every scene_type twice, maturity validation
uses unfamiliar fact cards. In each validation round, exactly one isolated
candidate may load the indexed approved samples; the other two are controls
and may not read any approved sample. Give all three the same facts, randomize
their A/B/C positions, and do not reveal which candidate used the library.
Append only the confirmed outcome metadata to validation-log.md in
chronological order; never store candidate prose there. A mixed selection
without a user-named primary draft, or rejection of all three, is ineligible
and requires another round.

After the user selects or edits a candidate, show one clean final copy and ask
“是否收录为 COS-xxx？” Only “收录”, “确认”, or a direct “可以” in response
to that exact question authorizes writing it to the approved corpus. Partial
approval is a fragment containing only the exact sentences the user identifies;
do not add bridge text or inferred context. A rejected draft is never stored; a failure reason is
stored only when the user confirms that reason. Keep each stored reason at or
below 200 characters. If the user's explanation is longer, propose a faithful
short version and store nothing until the user separately confirms it.

If the user withdraws an approved sample, remove its file and exact INDEX row
in the same commit, recompute maturity_stage, and do not turn the sample into
a failure example. Git history remains the recovery path.

During forming stage, a shared style observation remains inactive until its
clean one-line wording is shown and the user is asked “是否收录为 COS-Gxxx？”
Apply the same exact-response rule as sample approval. Only then append it to
guidance.md; never derive or store an unapproved style summary.

Historical writing archives, outside game corpora, rejected drafts, and
unapproved model summaries are not active writing inputs. Automatic scanners
cannot approve prose. The user is the sole prose-quality authority.
~~~

Replace CLAUDE.md lines 3-17 with:

~~~markdown
## 写新剧情前必读（强制）

任何写新章节、改对话、加旁白或设计选项前，依次读取：

1. CANON.md——人物、时空、物品和跨作品事实。
2. 当前场景的连续上下文、分支变量、物理状态和人物知情范围。
3. docs/writing-style/INDEX.md——只按索引读取最多三个活动正例。
4. docs/writing-style/guidance.md——只读取已经由用户逐条批准的活动指导。

检索顺序固定为：同角色 > 同 scene_type > 同 text_mode > 较新的
approved_on。没有合适正例时，标记为“尚未校准”，使用三份隔离候选稿
盲选；萌芽期的校准稿不直接改正式 .rpy。

十二份 full 正例覆盖六类场景各两次后，陌生场景成熟盲测必须每轮只让
一稿读取正例，另外两稿不得读取正例。三稿共用同一事实卡并随机打乱，
不得向用户泄露文风库稿的位置。validation-log.md 只按时间顺序追加用户
选择后的元数据，不保存候选原文；混稿未指定主要底稿或三稿全拒的轮次
不计成绩。

用户选稿或改稿后，必须重新展示完整清稿并单独询问是否收录。只有明确
确认才允许写入 approved/；局部确认记为 fragment。fragment 只保存用户
明确圈定的原句，不得补衔接句或推断上下文；废稿不落盘。失败
原因只记录用户确认的内容，单条最多二百字。用户原话超过上限时，不得
直接截断；先提出忠实压缩版，再经用户单独确认后记录。

用户撤回正例时，在同一提交中删除正例文件及 INDEX 对应行并重算阶段；
不把撤回文本转存为反例，恢复能力只交给 Git 历史。

成形期出现可复用的共同特征时，先展示一条干净表述并单独询问“是否收录
为 COS-Gxxx？”。只有与正例相同的明确答复才可追加到 guidance.md；模型
自行归纳的文风总结不得进入活动指导。

玩家指出新的 canon 错误时，继续按 CANON.md 末尾格式追加事实记录。
玩家指出新的文风问题时，只有用户确认后的失败原因才能进入
failure-reasons.md，不再实行文风清单“只增不减”。

写完后继续运行：

    python -B Tools/scan_canon.py

修改文风库文件时另运行：

    python -B Tools/validate_writing_style.py --root .

历史启发式扫描器可以按需运行，但不作为文风通过门槛。文案事实由
CANON.md 裁决，文案质量只由用户的盲选和明确批准裁决。
~~~

Replace CANON.md line 4 with:

~~~markdown
本文件只裁决事实与连续性；项目文风入口见 docs/writing-style/INDEX.md。
~~~

- [ ] **Step 5: Create the empty writing-style data store**

Create docs/writing-style/INDEX.md with:

~~~markdown
---
schema_version: 1
maturity_stage: seed
---

# 《权谋之庭》原创文风库

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

## 活动正例

| ID | scene_type | characters | text_mode | sample_kind | approved_on | sample |
|---|---|---|---|---|---|---|
~~~

Create docs/writing-style/scene-card-template.md with:

~~~markdown
# 《权谋之庭》校准场景事实卡

- scene_type：
- 目标字数：250～450 个中文字符
- 人物：
- 地点与时间：
- 已发生事件：
- 各人物已知信息：
- 各人物未知信息：
- 当前分支变量：
- 当前物理状态：
- 必须完成的叙事功能：
- 不可改变的分支结果：
- 连续上下文路径与行号：

事实卡不得填写文风指导，也不得进入正例库。
~~~

Create docs/writing-style/failure-reasons.md with:

~~~markdown
# 已确认失败原因

| 日期 | scene_type | 用户确认的失败原因 |
|---|---|---|
~~~

Create docs/writing-style/guidance.md with:

~~~markdown
# 已批准活动指导

| guidance_id | approved_on | scene_type | 用户批准的指导 |
|---|---|---|---|
~~~

Create docs/writing-style/validation-log.md with:

~~~markdown
# 陌生场景盲测记录

| round_id | scene_type | library_position | selection_method | primary_position | library_new_failure |
|---|---|---|---|---|---|
~~~

Create an empty docs/writing-style/approved/.gitkeep. Do not create any
COS-*.md file in this task.

- [ ] **Step 6: Make the historical scanner non-blocking**

Apply these exact textual changes in Tools/scan_ai_smell.py:

~~~python
"""
扫描 CoS 全部 .rpy 文件的台词 / 旁白，输出历史启发式命中。

这份报告含有大量误报，只用于诊断，不是文风通过门槛。

用法:
    cd CourtOfShadows
    python Tools/scan_ai_smell.py
    python Tools/scan_ai_smell.py game/chapter1.rpy

输出: 文件:行号 [模式名] 原文 (前 120 字)
"""
~~~

Change the PATTERNS heading to:

~~~python
# Historical heuristic patterns retained for optional diagnostics.
~~~

Change the D12 comment to:

~~~python
    # D12 historical reversal pattern
~~~

Replace the final summary prints with:

~~~python
    print()
    print(f'=== 共 {total} 处历史启发式命中（含误报）===')
    print('以上结果不作为文风通过门槛。')
    print('文风以 docs/writing-style/INDEX.md 中经用户确认的正例为准。')
~~~

Do not modify PATTERNS, DIALOGUE_RE, skip behavior, or the scanner exit code.

- [ ] **Step 7: Mark the design as confirmed**

In docs/superpowers/specs/2026-08-04-court-of-shadows-original-writing-style-design.md, replace:

~~~markdown
**状态：** 已完成口头设计确认，等待书面审阅
~~~

with:

~~~markdown
**状态：** 书面设计已确认，待实施
~~~

The validator deliberately keeps a twelve-sample library in `forming` until
the blind-test gate passes. Make the design text state the same transition.
Replace:

~~~markdown
### 9.2 成形期：6～11 段
~~~

with:

~~~markdown
### 9.2 成形期：6 段起，直至成熟门禁通过
~~~

After the existing three bullets in section 9.2, add:

~~~markdown
- 达到十二份 `full` 正例但尚未完成或通过陌生场景盲测时，仍属于成形期。
~~~

Replace:

~~~markdown
### 9.3 成熟期：至少 12 段
~~~

with:

~~~markdown
### 9.3 成熟期：至少 12 段且通过盲测门禁
~~~

After the existing paragraph in section 7.4, add the structural bound that
prevents a rejected 250-450-character candidate from being pasted into a
single table cell:

~~~markdown
单条失败原因最多二百字。用户原话超过上限时，不得直接截断；先提出忠实压缩版，得到用户再次确认后才能记录。
~~~

In the section 7 file tree, add `guidance.md` between failure-reasons.md and
validation-log.md. Insert this subsection before the current validation-log
subsection:

~~~markdown
### 7.5 `guidance.md`

只保存用户逐条明确批准的共同特征，采用固定表格：`guidance_id | approved_on | scene_type | 用户批准的指导`。模型自行归纳的总结不得写入；收录前必须展示干净表述并单独确认。
~~~

Then renumber the existing validation-log subsection from 7.5 to 7.6 and the
project-entry subsection from 7.6 to 7.7. Update the first project-entry bullet
so active game-copy work reads both docs/writing-style/INDEX.md and only the
already-approved rows in docs/writing-style/guidance.md.

- [ ] **Step 8: Run focused validation to verify GREEN**

Run:

~~~powershell
python -B -m unittest Tools.test_writing_style_system -v
python -B Tools/validate_writing_style.py --root .
python -B Tools/scan_ai_smell.py game/chapter1.rpy
~~~

Expected:

- writing-style tests: 18 tests run and OK.
- validator: PASS writing-style structure is valid.
- scanner: exits 0, prints a historical-hit count, and ends with the non-blocking disclaimer. The hit count is not a pass/fail criterion.

- [ ] **Step 9: Commit the corpus bootstrap and migration**

Run:

~~~powershell
git add -- AGENTS.md CLAUDE.md CANON.md Tools/scan_ai_smell.py Tools/test_writing_style_system.py docs/writing-style docs/archive/writing-style-legacy docs/superpowers/specs/2026-08-04-court-of-shadows-original-writing-style-design.md
git diff --cached --check
git commit -m "docs: bootstrap Court of Shadows writing style corpus"
~~~

Expected: one commit containing the recoverable legacy moves, empty active
corpus, active instructions, scanner disclaimer, live contract tests, and the
confirmed design status. No game/*.rpy file changes.

---

### Task 3: Synchronize the Ren'Py release-package contract

**Files:**

- Modify: Tools/test_release_contract.py:52-105,1951-1987
- Modify: game/options.rpy:69-100

**Interfaces:**

- Consumes: docs/** as the existing broad exclusion for the active corpus and archived guides.
- Produces: one direct AGENTS.md exclusion in both the approved contract and Ren'Py build rules.
- Removes: stale direct exclusions for root STYLE.md and FORBIDDEN_PHRASES.md.
- Preserves: all protected UI, Android input, old-game, and README classification rules.

- [ ] **Step 1: Add the failing packaging test**

Add this constant immediately after APPROVED_PACKAGE_EXCLUSIONS in
Tools/test_release_contract.py:

~~~python
ARCHIVED_LEGACY_WRITING_GUIDES = (
    "docs/archive/writing-style-legacy/STYLE.md",
    "docs/archive/writing-style-legacy/FORBIDDEN_PHRASES.md",
)
~~~

Add this method to PackagingClassificationContractTests:

~~~python
    def test_writing_style_docs_follow_current_package_contract(self) -> None:
        self.assertIn("AGENTS.md", APPROVED_PACKAGE_EXCLUSIONS)
        self.assertNotIn("STYLE.md", APPROVED_PACKAGE_EXCLUSIONS)
        self.assertNotIn("FORBIDDEN_PHRASES.md", APPROVED_PACKAGE_EXCLUSIONS)
        self.assertNotIn(("STYLE.md", None), self.rules)
        self.assertNotIn(("FORBIDDEN_PHRASES.md", None), self.rules)
        self.assertEqual(
            missing_project_files(ARCHIVED_LEGACY_WRITING_GUIDES),
            [],
        )
        for path in ARCHIVED_LEGACY_WRITING_GUIDES:
            with self.subTest(path=path):
                self.assertEqual(
                    first_literal_classification(self.rules, path),
                    ("docs/**", None),
                )
~~~

- [ ] **Step 2: Run the focused contract to verify RED**

Run:

~~~powershell
python -B -m unittest Tools.test_release_contract.PackagingClassificationContractTests.test_writing_style_docs_follow_current_package_contract -v
~~~

Expected: FAIL because APPROVED_PACKAGE_EXCLUSIONS and game/options.rpy still
contain both stale root paths, while the approved tuple does not contain
AGENTS.md.

- [ ] **Step 3: Update the approved exclusion tuple**

In APPROVED_PACKAGE_EXCLUSIONS:

- Add "AGENTS.md" immediately after "Tools/**".
- Remove "FORBIDDEN_PHRASES.md".
- Remove "STYLE.md".

Do not add exact exclusions for either archived path; the earlier "docs/**"
rule already excludes both.

- [ ] **Step 4: Mirror the change in game/options.rpy**

Immediately after:

~~~python
    build.classify('Tools/**', None)
~~~

add:

~~~python
    build.classify('AGENTS.md', None)
~~~

Delete only these two stale rules:

~~~python
    build.classify('FORBIDDEN_PHRASES.md', None)
    build.classify('STYLE.md', None)
~~~

Keep build.classify('docs/**', None) before all later game inclusion rules.

- [ ] **Step 5: Run focused and dependent release tests to verify GREEN**

Run:

~~~powershell
python -B -m unittest Tools.test_release_contract.PackagingClassificationContractTests -v
python -B -m unittest Tools.test_release_contract -q
python -B Tools/test_verify_distributions.py -q
~~~

Expected:

- PackagingClassificationContractTests: all tests OK.
- test_release_contract: 50 tests run and OK.
- test_verify_distributions: 51 tests run and OK.

- [ ] **Step 6: Commit the package-contract synchronization**

Run:

~~~powershell
git add -- Tools/test_release_contract.py game/options.rpy
git diff --cached --check
git commit -m "build: exclude writing style development files"
~~~

Expected: one commit containing only the release-contract test and matching
Ren'Py packaging rules.

---

### Task 4: Run the complete gate and prepare the first blind calibration

**Files:**

- Read: CANON.md
- Read: game/chapter3.rpy:6089-6114
- Read for facts only: game/chapter4.rpy:903-929
- Do not modify: game/chapter3.rpy
- Do not modify: game/chapter4.rpy
- Do not create: docs/writing-style/approved/COS-*.md

**Interfaces:**

- Consumes: the empty validated seed corpus from Tasks 1-3.
- Produces: fresh verification evidence and one fact-only power_bargain card in the execution response.
- Hands off: three isolated candidate-generation prompts to the next interactive user checkpoint.

- [ ] **Step 1: Run all structural and regression gates**

Run:

~~~powershell
python -B Tools/validate_writing_style.py --root .
python -B -m unittest Tools.test_writing_style_system -v
python -B -m unittest Tools.test_release_contract -v
python -B Tools/test_verify_distributions.py -q
python -B -m unittest discover -s Tools -p "test_*.py" -q
python -B Tools/test_release_regressions.py
python -B Tools/scan_canon.py
python -B scan_missing_portraits.py
python -B scan_narration_overlap.py
& 'E:/Projects/renpy-8.5.2-sdk/renpy.exe' . lint
git diff --check
git status --short
~~~

Expected:

- validator prints PASS.
- writing-style system: 18 tests OK.
- release contract: 50 tests OK.
- distribution verifier: 51 tests OK.
- complete Tools discovery: 181 tests OK.
- standalone release-regression scan prints `PASS: no player-visible doubled percent literals`.
- canon scan exits 0.
- missing-portrait scan reports Total findings: 0.
- narration-overlap scan reports TOTAL: 0.
- Ren'Py lint exits 0.
- git diff --check has no output.
- git status --short has no output.

If the total test count differs only because an unrelated test was added after
this plan, require zero failures and report the fresh count instead of forcing
181.

- [ ] **Step 2: Verify the asset and package-size conclusion**

Confirm the complete diff contains only the planned Markdown and Python files,
the empty docs/writing-style/approved/.gitkeep marker, and game/options.rpy.
Report:

- Art: no new asset required.
- Music: no new asset required.
- Sound effects: no new asset required.
- Animation: no new asset required.
- UI: no new asset required.
- Package size: no increase; docs/**, Tools/**, and AGENTS.md are excluded.

- [ ] **Step 3: Prepare this exact first fact card without storing it**

Use the following execution-time fact card:

~~~text
scene_type: power_bargain
target_length: 250-450 Chinese characters
characters: player, ingrid
location_and_time: 王都北疆使馆区；第四章觐见王室之前；双方第一次正式见面
prior_events:
  - 希尔达此前来信提议以政治联姻加强北疆与艾登堡的盟约
  - 主角同意赴王都会谈，但没有接受或拒绝联姻
  - marriage_proposal_open 为真；任何路线都尚未锁定
known_by_ingrid:
  - 她代表北疆议会而来
  - 北境需要盐路恢复，并需要为开春后的粮食与政治安全找盟友
  - 外界对主角的评价两极
known_by_player:
  - 婚约同时是军事、粮食和议会支持的交易
  - 英格丽不是母亲送来代签的名字，她本人有权拒绝或开条件
unknown_to_both:
  - 对方是否愿意把婚约只当政治合同
  - 对方是否值得在私人生活中信任
required_beat:
  - 让两个人以各自利益和判断开口
  - 把联盟的具体代价放到桌上
  - 让英格丽显出独立于母亲和议会的个人意志
  - 停在玩家菜单出现之前
fixed_result:
  - 不接受、不拒绝婚约
  - 不设置 marriage_route 或 marriage_warm
  - 不制造恋爱承诺
canon_facts:
  - 旁白必须使用第二人称“你”
  - 主角二十二岁，继任至今只有数月；不得写成“这一年”或“继任半年/一年”
  - 艾登堡是内陆领地，没有海港或码头；盐运抵达领地的最后一段走陆路
  - 希尔达是北疆议会的伯爵夫人，不是序章宴会的施泰因伯爵夫人
  - 不硬写玩家姓名
forbidden_inputs:
  - 原场景现有措辞
  - 历史写作归档
  - 外部游戏语料
  - 尚不存在的正例
~~~

This fact card is temporary conversation state. Do not commit it and do not
copy it into approved/.

Root-only provenance, which must not be copied into any candidate prompt:

- game/chapter3.rpy:6089-6114
- game/chapter4.rpy:903-929

- [ ] **Step 4: Start the user-gated blind round**

Dispatch three isolated subagents with `fork_turns="none"`. Do not use the
default inherited-history fork. Put the complete agent-facing fact card above
directly in each initial prompt and instruct the agent not to inspect the
filesystem, call tools, or read CANON.md or any game source. Give each only:

- the exact fact card above;
- an instruction to draft freely without reading the forbidden inputs.

Do not let any candidate agent see another candidate. Reject and regenerate a
candidate if it copies the current game wording or falls outside 250-450
Chinese characters. Randomize the surviving candidates as A, B, and C, then
show them to the user without method labels.

Stop and wait. Do not write a sample file merely because the user chooses a
candidate. First produce one clean merged final and ask:

    是否收录为 COS-001？

Only the explicit response defined in AGENTS.md authorizes the later corpus
write. If all candidates are rejected, discard every candidate and preserve
only a failure reason that the user separately confirms.

---

## Plan Self-Review

- Spec scope is covered by Tasks 1-4; no global skill or cross-project style is created.
- Explicit sample and guidance approval, fragment handling, withdrawal,
  rejected-draft disposal, and sole user authority are enforced by Task 2 instructions.
- Six scene types, sample metadata, index integrity, failure log shape, fragment counting, and mature blind evidence are enforced by Task 1.
- The active INDEX preamble and writing-style directory are allowlisted, so unapproved summaries, outside links, and retained draft files fail validation.
- Legacy files remain byte-preserved under docs/archive and are removed from active entry points in Task 2.
- Ren'Py package exclusions remain synchronized and tested in Task 3.
- The first calibration is isolated, fact-only, non-destructive, and user-gated in Task 4.
- No formal narrative, art, music, sound, animation, or UI asset changes occur in this plan.
- Python remains standard-library only.
- Each code-producing task begins with a failing test and ends with a focused commit.

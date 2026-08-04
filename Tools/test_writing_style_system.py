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
ACTIVE_ENTRYPOINTS = (
    "AGENTS.md",
    "CLAUDE.md",
    "CANON.md",
    "docs/writing-style/INDEX.md",
    "docs/writing-style/guidance.md",
)


class WritingStyleTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.style = self.root / "docs" / "writing-style"
        (self.style / "approved").mkdir(parents=True)
        self.write("docs/writing-style/approved/.gitkeep", "")
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

    def test_gitkeep_must_be_an_empty_regular_file(self) -> None:
        self.write(
            "docs/writing-style/approved/.gitkeep",
            "A rejected draft must not be hidden in the marker.\n",
        )
        self.assertIn(
            ".gitkeep must be an empty regular file",
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
    def test_every_active_entrypoint_rejects_unapproved_source_locations(
        self,
    ) -> None:
        source_variants = (
            "Read D:/OtherGame/corpus.txt",
            "rEaD d:/othergame/CORPUS.TXT",
            r"Read D:\OtherGame\corpus.txt",
            r"Read D:\\OtherGame\\corpus.txt",
            "Read https://example.invalid/style/corpus.txt",
            "Read ../OtherGame/corpus.txt",
            r"Read ..\OtherGame\corpus.txt",
            "Read docs/other-project/style-corpus.md",
            "Style source: docs/other-project/style-corpus.md",
            "Use docs/other-project/prose.md before drafting.",
            "Style source: docs/other-project/prose.md",
            "Consult [reference](docs/other-project/prose.md)",
        )
        for active_name in ACTIVE_ENTRYPOINTS:
            path = self.root / active_name
            original = path.read_text(encoding="utf-8")
            for source in source_variants:
                with self.subTest(active_name=active_name, source=source):
                    path.write_text(
                        f"{original.rstrip()}\n{source}\n",
                        encoding="utf-8",
                    )
                    report = "\n".join(validator.validate_project(self.root))
                    self.assertIn(
                        f"{active_name}: unapproved active source",
                        report,
                    )
            path.write_text(original, encoding="utf-8")

    def test_canon_fact_provenance_remains_allowed(self) -> None:
        canon = self.root / "CANON.md"
        canon.write_text(
            canon.read_text(encoding="utf-8")
            + "\nFact provenance: game/chapter1.rpy:55 and "
            "memory/reference_cos_hidden_ending.md.\n",
            encoding="utf-8",
        )
        self.assertEqual(validator.validate_project(self.root), [])

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

    def test_reordered_blind_rounds_fail_and_cannot_grant_maturity(self) -> None:
        sample_number = 1
        for _ in range(2):
            for scene_type in SCENES:
                self.add_sample(f"COS-{sample_number:03d}", scene_type)
                sample_number += 1
        self.set_blind_rounds(
            [
                "| BT-003 | power_bargain | A | single | A | no |",
                "| BT-001 | mystery_reveal | C | mixed_with_primary | C | no |",
                "| BT-002 | ending_epilogue | B | single | A | no |",
            ]
        )
        self.set_stage("mature")
        report = "\n".join(validator.validate_project(self.root))
        self.assertIn("round numbers must increase in append order", report)
        self.assertIn(
            "declared maturity_stage mature does not match forming",
            report,
        )

    def test_malformed_blind_row_invalidates_all_maturity_evidence(self) -> None:
        sample_number = 1
        for _ in range(2):
            for scene_type in SCENES:
                self.add_sample(f"COS-{sample_number:03d}", scene_type)
                sample_number += 1
        self.set_blind_rounds(
            [
                "| BT-001 | power_bargain | A | single | A | no |",
                "| malformed | row |",
                "| BT-002 | mystery_reveal | C | mixed_with_primary | C | no |",
                "| BT-003 | ending_epilogue | B | single | A | no |",
            ]
        )
        self.set_stage("mature")
        report = "\n".join(validator.validate_project(self.root))
        self.assertIn("expected 6 columns", report)
        self.assertIn(
            "declared maturity_stage mature does not match forming",
            report,
        )


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


if __name__ == "__main__":
    unittest.main()

import hashlib
import io
import json
import pickle
import re
import subprocess
import unittest
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "Tools" / "Run-RenPySuite.ps1"
TEST_GAME = ROOT / "game" / "test_game.rpy"
CHAPTER2 = ROOT / "game" / "chapter2.rpy"
FIXTURE_DIR = ROOT / "tests" / "fixtures" / "winter_legacy"
MANIFEST = FIXTURE_DIR / "manifest.json"
ASSET_BASELINE = ROOT / "tests" / "fixtures" / "winter_asset_baseline.json"
BASELINE_COMMIT = "ebb4efd2194fb31710d0331d53d0fe825eb8062c"


class _InertSaveObject:
    """Accept Ren'Py pickle state without importing or executing its globals."""

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.newargs = args
        return instance

    def __setstate__(self, state):
        self.state = state

    def __call__(self, *args, **kwargs):
        return _InertSaveObject()


class _InertSaveList(list):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __setstate__(self, state):
        self.state = state


class _InertSaveDict(dict):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __setstate__(self, state):
        self.state = state


class _RestrictedRenPySaveUnpickler(pickle.Unpickler):
    """Deserialize shape only; every encoded global resolves to an inert class."""

    def __init__(self, stream):
        super().__init__(stream)
        self._classes = {}

    def find_class(self, module, name):
        key = (module, name)
        if key not in self._classes:
            base = _InertSaveObject
            if "List" in name:
                base = _InertSaveList
            elif "Dict" in name:
                base = _InertSaveDict
            self._classes[key] = type(
                f"Inert_{len(self._classes)}",
                (base,),
                {"encoded_global": key},
            )
        return self._classes[key]

    def persistent_load(self, persistent_id):
        return ("persistent", persistent_id)


def read_active_save_context(path: Path) -> dict:
    """Return the final rollback context without executing save-pickle globals."""
    with zipfile.ZipFile(path) as archive:
        payload = archive.read("log")
    store, rollback_log = _RestrictedRenPySaveUnpickler(io.BytesIO(payload)).load()
    del store
    rollback_entries = rollback_log.state["log"]
    context = rollback_entries[-1].state["context"]
    return context.state


class RenPyRunnerSourceContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = RUNNER.read_text(encoding="utf-8") if RUNNER.exists() else ""

    def test_runner_exists(self):
        self.assertTrue(RUNNER.is_file(), "Run-RenPySuite.ps1 has not been implemented")

    def test_runner_requires_explicit_project_and_save_paths(self):
        self.assertRegex(self.source, r"(?s)\[Parameter\(Mandatory\s*=\s*\$true\)\].*\$ProjectRoot")
        self.assertRegex(self.source, r"(?s)\[Parameter\(Mandatory\s*=\s*\$true\)\].*\$SaveDir")
        self.assertIn("CourtOfShadows-save", self.source)
        self.assertRegex(self.source, r"(?i)player.*save|save.*player")
        self.assertIn("New-Item", self.source)

    def test_runner_counts_exactly_one_fresh_rpytest_status(self):
        self.assertIn("[rpytest] Status:", self.source)
        self.assertRegex(self.source, r"(?i)LastWriteTimeUtc")
        self.assertRegex(self.source, r"(?i)Count\s+-ne\s+1")
        self.assertRegex(self.source, r"(?i)log\.txt")

    def test_runner_stages_only_hash_verified_exact_fixture_names(self):
        self.assertIn("StageLegacyFixtures", self.source)
        self.assertIn("manifest.json", self.source)
        self.assertIn("Get-FileHash", self.source)
        self.assertIn("SHA256", self.source)
        self.assertRegex(self.source, r"(?i)physical_filename")
        self.assertRegex(self.source, r"(?i)throw.*hash|hash.*throw")

    def test_runner_has_bounded_wait_and_recorded_pid_cleanup(self):
        self.assertIn("TimeoutSeconds", self.source)
        self.assertRegex(self.source, r"(?i)WaitForExit")
        self.assertRegex(self.source, r"(?i)\.Id")
        self.assertRegex(self.source, r"(?i)Kill\(")
        self.assertNotRegex(self.source, r"(?i)Get-Process\s+.*renpy|Stop-Process\s+.*renpy")
        self.assertRegex(self.source, r"(?i)recorded.*pid|pid.*recorded")

    def test_runner_completes_redirected_stream_wait_before_reading_exit_code(self):
        self.assertIn("[void]$process.WaitForExit()", self.source)
        completion_index = self.source.index("[void]$process.WaitForExit()")
        exit_code_index = self.source.index("$exitCode = $process.ExitCode")
        self.assertLess(completion_index, exit_code_index)

    def test_runner_builds_suite_full_and_lint_arguments_without_shell_strings(self):
        self.assertRegex(self.source, r"ValidateSet\([^)]*Suite[^)]*Full[^)]*Lint")
        self.assertRegex(self.source, r"(?s)\"Suite\".*\"test\".*\$Suite")
        self.assertRegex(self.source, r"(?s)\"Full\".*\"test\"")
        self.assertRegex(self.source, r"(?s)\"Lint\".*\"lint\".*\"--error-code\"")
        self.assertIn("--savedir", self.source)
        self.assertRegex(self.source, r"ArgumentList|\.Arguments\s*=")
        self.assertNotRegex(self.source, r"(?i)Invoke-Expression|cmd(?:\.exe)?\s+/c")

    def test_runner_owns_a_direct_native_process_handle_and_redirected_streams(self):
        self.assertIn("System.Diagnostics.ProcessStartInfo", self.source)
        self.assertIn("System.Diagnostics.Process", self.source)
        self.assertRegex(self.source, r"UseShellExecute\s*=\s*\$false")
        self.assertRegex(self.source, r"RedirectStandardOutput\s*=\s*\$true")
        self.assertRegex(self.source, r"RedirectStandardError\s*=\s*\$true")
        self.assertNotIn("Start-Process", self.source)

    def test_runner_enforces_mode_specific_expectation_contracts(self):
        self.assertRegex(self.source, r"(?s)Suite.*Expect.*required")
        self.assertRegex(self.source, r"(?s)Full.*PASSED")
        self.assertRegex(self.source, r"(?s)Lint.*Expect.*not accepted")
        self.assertRegex(self.source, r"(?s)Lint.*Suite.*not accepted")
        self.assertRegex(self.source, r"(?s)FAILED.*ExpectedPattern")
        self.assertRegex(self.source, r"(?i)parse|syntax|import|missing.file")

    def test_runner_preserves_script_parameter_binding_inside_helper_function(self):
        self.assertRegex(self.source, r"(?m)^\$invocationParameters\s*=\s*@\{\}")
        self.assertRegex(self.source, r"(?m)^foreach \(\$boundName in \$PSBoundParameters\.Keys\)")
        self.assertRegex(self.source, r"invocationParameters\.ContainsKey\(\"Expect\"\)")
        self.assertNotRegex(self.source, r"(?m)^\s{8,}\$PSBoundParameters\.ContainsKey")

    def test_runner_restores_variant_in_finally(self):
        self.assertIn("RENPY_VARIANT", self.source)
        self.assertRegex(self.source, r"(?s)try\s*\{.*\}\s*finally\s*\{")
        self.assertRegex(self.source, r"(?s)finally\s*\{.*RENPY_VARIANT")

    def test_runner_captures_unique_evidence_and_head(self):
        self.assertIn("EvidenceDir", self.source)
        self.assertRegex(self.source, r"(?i)rev-parse.*HEAD")
        self.assertRegex(self.source, r"(?i)Get-Date.*yyyy")
        self.assertIn("Copy-Item", self.source)

    def test_runner_copies_fresh_log_before_rejecting_status_mismatch(self):
        copy_index = self.source.index("Copy-Item -LiteralPath $logPath")
        mismatch_index = self.source.index('if ($actualStatus -ne $Expect)')
        self.assertLess(copy_index, mismatch_index)


class WinterFixtureInfrastructureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.exists() else {}
        cls.test_game = TEST_GAME.read_text(encoding="utf-8")

    def test_fixture_manifest_exists(self):
        self.assertTrue(MANIFEST.is_file(), "winter legacy manifest has not been generated")

    def test_manifest_is_bound_to_exact_baseline_and_engine(self):
        self.assertTrue(self.manifest, "winter legacy manifest has not been generated")
        self.assertEqual(self.manifest["baseline_commit"], BASELINE_COMMIT)
        self.assertEqual(self.manifest["renpy_version"], "8.5.2")
        self.assertEqual(self.manifest["savegame_suffix"], "-LT1.save")
        self.assertRegex(self.manifest["generated_at_utc"], r"^\d{4}-\d{2}-\d{2}T")

    def test_manifest_has_the_five_exact_engine_native_archives(self):
        self.assertTrue(self.manifest, "winter legacy manifest has not been generated")
        expected = {
            "winter-legacy-merchant-inside-LT1.save",
            "winter-legacy-building-inside-LT1.save",
            "winter-legacy-famine-inside-LT1.save",
            "winter-legacy-famine-success-after-LT1.save",
            "winter-legacy-chapter2-no-governance-LT1.save",
        }
        entries = self.manifest["fixtures"]
        self.assertEqual({entry["physical_filename"] for entry in entries}, expected)
        self.assertEqual(len(entries), 5)
        self.assertEqual({path.name for path in FIXTURE_DIR.glob("*.save")}, expected)
        for entry in entries:
            path = FIXTURE_DIR / entry["physical_filename"]
            self.assertEqual(entry["logical_slot"] + "-LT1.save", entry["physical_filename"])
            self.assertEqual(entry["byte_size"], path.stat().st_size)
            self.assertEqual(entry["sha256"].lower(), hashlib.sha256(path.read_bytes()).hexdigest())
            with zipfile.ZipFile(path) as archive:
                self.assertIn("signatures", archive.namelist())
                metadata = json.loads(archive.read("json"))
                self.assertEqual(metadata["_renpy_version"][:3], [8, 5, 2])

    def test_live_and_post_return_provenance_are_explicit(self):
        self.assertTrue(self.manifest, "winter legacy manifest has not been generated")
        by_slot = {entry["logical_slot"]: entry for entry in self.manifest["fixtures"]}
        expected_continuations = {
            "winter-legacy-merchant-inside": "_call_gov_merch2",
            "winter-legacy-building-inside": "_call_gov_build2",
            "winter-legacy-famine-inside": "_call_gov_famine2",
        }
        for slot, continuation in expected_continuations.items():
            self.assertEqual(by_slot[slot]["provenance_type"], "live continuation")
            self.assertEqual(by_slot[slot]["expected_continuation"], continuation)
        self.assertEqual(by_slot["winter-legacy-famine-success-after"]["provenance_type"], "real completed state")
        self.assertEqual(by_slot["winter-legacy-chapter2-no-governance"]["provenance_type"], "synthetic compatibility state")
        for slot in ("winter-legacy-famine-success-after", "winter-legacy-chapter2-no-governance"):
            self.assertEqual(by_slot[slot]["permanent_stop_label"], "ch2_preparation")

    def test_archives_have_the_required_active_return_stacks(self):
        expected_live_stacks = {
            "winter-legacy-merchant-inside-LT1.save": ["_call_gov_merch2"],
            "winter-legacy-building-inside-LT1.save": ["_call_gov_build2"],
            "winter-legacy-famine-inside-LT1.save": ["_call_gov_famine2"],
        }
        for filename, expected_stack in expected_live_stacks.items():
            with self.subTest(filename=filename):
                context = read_active_save_context(FIXTURE_DIR / filename)
                self.assertEqual(context["return_stack"], expected_stack)
                self.assertEqual(len(context["call_location_stack"]), 1)
                self.assertEqual(context["abnormal_stack"], [False])

        forbidden = {
            "_call_gov_famine2",
            "_call_re_scene_ev2",
            "_call_scene_event",
            "test_winter_legacy_famine_success_after_driver",
            "test_winter_legacy_chapter2_no_governance_driver",
        }
        for filename in (
            "winter-legacy-famine-success-after-LT1.save",
            "winter-legacy-chapter2-no-governance-LT1.save",
        ):
            with self.subTest(filename=filename):
                context = read_active_save_context(FIXTURE_DIR / filename)
                self.assertEqual(context["return_stack"], [])
                self.assertEqual(context["call_location_stack"], [])
                self.assertEqual(context["abnormal_stack"], [])
                self.assertTrue(
                    forbidden.isdisjoint(
                        context["return_stack"] + [str(item) for item in context["call_location_stack"]]
                    )
                )
                current = context["current"]
                self.assertIsInstance(current, tuple)
                self.assertEqual(current[0], "game/chapter2.rpy")

    def test_test_command_guard_contains_exactly_the_manifest_public_key(self):
        self.assertTrue(self.manifest, "winter legacy manifest has not been generated")
        key = self.manifest["fixture_verifying_key"]
        self.assertNotIn("PRIVATE", key.upper())
        self.assertEqual(self.test_game.count(key), 1)
        self.assertRegex(
            self.test_game,
            re.escape('python early:\n    if renpy.game.args.command == "test":\n        config.save_token_keys.append("')
            + re.escape(key)
            + re.escape('")'),
        )
        self.assertNotIn("security_keys.txt", self.test_game)

    def test_test_game_diff_is_only_key_guard_global_exit_five_lint_roots_and_one_choice_gate(self):
        baseline = subprocess.run(
            ["git", "show", f"{BASELINE_COMMIT}:game/test_game.rpy"],
            cwd=ROOT,
            check=True,
            stdout=subprocess.PIPE,
        ).stdout.decode("utf-8")
        key = self.manifest["fixture_verifying_key"]
        permanent_prefix = (
            "python early:\n"
            '    if renpy.game.args.command == "test":\n'
            f'        config.save_token_keys.append("{key}")\n\n\n'
            "label _test_lint_reachability_root:\n"
            "    if True == True:\n"
            "        return\n\n\n"
            "testsuite global:\n"
            "    teardown:\n"
            "        exit\n\n\n"
        )
        expected = permanent_prefix + baseline
        roots = {
            "testcase test_mobile_choice_overflow:\n": "_test_lint_reachability_mobile_render",
            "testsuite test_release_metadata_render:\n": "_test_lint_reachability_release_metadata",
            "testsuite test_accessibility_settings:\n": "_test_lint_reachability_accessibility",
            "testsuite test_new_run_bootstrap:\n": "_test_lint_reachability_new_run",
        }
        for declaration, root_name in roots.items():
            root = f"label {root_name}:\n    if True == True:\n        return\n\n\n"
            self.assertEqual(expected.count(declaration), 1)
            expected = expected.replace(declaration, root + declaration)
        unstable_click = '        click "记住这一切，继续前进"\n'
        choice_gate = (
            '        $ _test.choice_text = "记住这一切，继续前进"\n'
            '        pause until eval (len([f for f in renpy.display.focus.focus_list '
            'if f.x is not None and _test.choice_text.casefold() in '
            'f.widget._tts_all(True).casefold() and isinstance(getattr(f.widget, '
            '"action", None), renpy.ui.ChoiceReturn)]) == 1) timeout 4.0\n'
        )
        self.assertEqual(expected.count(unstable_click), 1)
        expected = expected.replace(unstable_click, choice_gate + unstable_click)
        self.assertEqual(self.test_game, expected)
        self.assertEqual(self.test_game.count("label _test_lint_reachability_"), 5)
        self.assertEqual(self.test_game.count("testsuite global:"), 1)
        self.assertEqual(self.test_game.count("        exit\n"), 1)
        self.assertEqual(self.test_game.count(choice_gate), 1)

    def test_generation_and_smoke_hooks_are_fully_removed(self):
        forbidden = [
            "_test_winter_fixture_merchant_call",
            "_test_winter_fixture_building_call",
            "_test_winter_fixture_famine_call",
            "test_winter_legacy_merchant_driver",
            "test_winter_legacy_building_driver",
            "test_winter_legacy_famine_driver",
            "test_winter_legacy_famine_success_after_driver",
            "test_winter_legacy_chapter2_no_governance_driver",
            "test_winter_legacy_fixture_generation",
            "test_winter_legacy_fixture_smoke",
        ]
        chapter2 = CHAPTER2.read_text(encoding="utf-8")
        for name in forbidden:
            self.assertNotIn(name, chapter2)
            self.assertNotIn(name, self.test_game)

    def test_chapter2_exactly_matches_recorded_baseline(self):
        result = subprocess.run(
            ["git", "diff", "--exit-code", BASELINE_COMMIT, "--", "game/chapter2.rpy"],
            cwd=ROOT,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        self.assertEqual(result.returncode, 0, result.stdout.decode("utf-8", errors="replace"))

    def test_asset_baseline_is_sorted_complete_and_hash_verified(self):
        self.assertTrue(ASSET_BASELINE.is_file(), "winter asset baseline has not been generated")
        data = json.loads(ASSET_BASELINE.read_text(encoding="utf-8"))
        entries = data["files"]
        paths = [entry["relative_path"] for entry in entries]
        self.assertEqual(data["baseline_commit"], BASELINE_COMMIT)
        self.assertEqual(data["file_count"], len(entries))
        self.assertEqual(data["total_bytes"], sum(entry["byte_size"] for entry in entries))
        self.assertEqual(paths, sorted(paths))

        shipping = set()
        image_audio_roots = [ROOT / "game" / "images", ROOT / "game" / "audio"]
        for directory in image_audio_roots:
            if directory.exists():
                shipping.update(path for path in directory.rglob("*") if path.is_file())
        for suffix in (".webp", ".png", ".jpg", ".ogg", ".mp3", ".wav", ".ttf"):
            shipping.update(path for path in (ROOT / "game").rglob(f"*{suffix}") if path.is_file())
        expected = {path.relative_to(ROOT).as_posix() for path in shipping}
        self.assertEqual(set(paths), expected)
        for entry in entries:
            path = ROOT / entry["relative_path"]
            self.assertEqual(entry["byte_size"], path.stat().st_size)
            self.assertEqual(entry["sha256"].lower(), hashlib.sha256(path.read_bytes()).hexdigest())


if __name__ == "__main__":
    unittest.main()

import ast
import hashlib
import io
import json
import pickle
import re
import subprocess
import textwrap
import unittest
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "Tools" / "Run-RenPySuite.ps1"
TEST_GAME = ROOT / "game" / "test_game.rpy"
SCRIPT = ROOT / "game" / "script.rpy"
CHAPTER2 = ROOT / "game" / "chapter2.rpy"
CINEMATICS = ROOT / "game" / "cinematics.rpy"
GALLERY = ROOT / "game" / "gallery.rpy"
IMAGES_DEF = ROOT / "game" / "images_def.rpy"
FIXTURE_DIR = ROOT / "tests" / "fixtures" / "winter_legacy"
MANIFEST = FIXTURE_DIR / "manifest.json"
ASSET_BASELINE = ROOT / "tests" / "fixtures" / "winter_asset_baseline.json"
WINTER_MODULE = ROOT / "game" / "governance_winter_interlude.rpy"
GOVERNANCE = ROOT / "game" / "governance.rpy"
DIFFICULTY = ROOT / "game" / "difficulty.rpy"
SAVE_COMPAT = ROOT / "game" / "save_compat.rpy"
VERIFY_DISTRIBUTIONS = ROOT / "Tools" / "verify_distributions.py"
TEST_VERIFY_DISTRIBUTIONS = ROOT / "Tools" / "test_verify_distributions.py"
BASELINE_COMMIT = "ebb4efd2194fb31710d0331d53d0fe825eb8062c"
PACKAGE_BASELINE_COMMIT = "b75a3ecc3cc59ff63665236543124b33ad2bcd9c"
WINTER_ALLOWED_STORE_DEFAULT_WRITES = {
    "governance_events_seen",
    "winter_interlude_status",
    "winter_investigations",
    "winter_policy",
    "winter_seed_priority",
}
WINTER_ASSIGNABLE_STORE_DEFAULTS = WINTER_ALLOWED_STORE_DEFAULT_WRITES - {
    "governance_events_seen"
}
WINTER_NONDEFAULT_FORBIDDEN_STATE = {
    "_iron_prepared",
    "ch3_lily_alliance_independent",
}


def _label_body(source: str, label: str) -> str:
    match = re.search(
        rf"(?ms)^label {re.escape(label)}(?:\([^\n]*\))?:\s*\n(.*?)(?=^label |\Z)",
        source,
    )
    if match is None:
        raise AssertionError(f"label {label!r} not found")
    return match.group(1)


def _executable_lines(source: str) -> list[str]:
    lines = []
    for raw_line in source.splitlines():
        line = raw_line.split("#", 1)[0].strip()
        if line:
            lines.append(line)
    return lines


def _literal_list_assignment(source: str, name: str) -> list:
    match = re.search(
        rf"(?ms)^\s*{re.escape(name)}\s*=\s*(\[[^\]]*\])",
        source,
    )
    if match is None:
        raise AssertionError(f"literal list assignment {name!r} not found")
    value = ast.literal_eval(match.group(1))
    if not isinstance(value, list):
        raise AssertionError(f"{name!r} is not a literal list")
    return value


def _project_default_inventory() -> tuple[set[str], set[str]]:
    """Return all project-defined store and persistent top-level defaults."""
    store_defaults = set()
    persistent_defaults = set()
    pattern = re.compile(
        r"(?m)^default\s+(?:(persistent)\.)?([A-Za-z_][A-Za-z0-9_]*)\s*="
    )
    for path in sorted((ROOT / "game").rglob("*.rpy")):
        if path == TEST_GAME:
            continue
        for namespace, name in pattern.findall(path.read_text(encoding="utf-8")):
            if namespace:
                persistent_defaults.add(name)
            else:
                store_defaults.add(name)
    return store_defaults, persistent_defaults


_RENPY_PYTHON_HEADER = re.compile(
    r"^(?P<indent> *)(?P<init>init(?:\s+-?\d+)?\s+)?python"
    r"(?P<early>\s+early)?(?P<hide>\s+hide)?"
    r"(?P<store>\s+in\s+[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)*)?"
    r"\s*:\s*(?:#.*)?$"
)


def _renpy_python_fragments_with_labels(
    module_source: str,
) -> list[tuple[str | None, str]]:
    """Extract Python fragments together with their containing Ren'Py label."""
    lines = module_source.splitlines()
    fragments = []
    current_label = None
    index = 0
    while index < len(lines):
        label_match = re.match(
            r"^label\s+([A-Za-z_][A-Za-z0-9_]*)"
            r"(?:\([^\n]*\))?\s*:\s*(?:#.*)?$",
            lines[index],
        )
        if label_match:
            current_label = label_match.group(1)
            index += 1
            continue
        match = _RENPY_PYTHON_HEADER.match(lines[index])
        if match:
            header_indent = len(match.group("indent"))
            fragment_label = current_label if header_indent else None
            body = []
            index += 1
            while index < len(lines):
                raw_line = lines[index]
                if raw_line.strip():
                    indentation = len(raw_line) - len(raw_line.lstrip(" "))
                    if indentation <= header_indent:
                        break
                body.append(raw_line)
                index += 1
            fragments.append((fragment_label, textwrap.dedent("\n".join(body))))
            continue
        stripped = lines[index].lstrip()
        if stripped.startswith("$"):
            fragments.append((current_label, stripped[1:].strip()))
        index += 1
    return fragments


def _renpy_python_fragments(module_source: str) -> list[str]:
    """Extract Python blocks and one-line Python statements from a Ren'Py file."""
    return [fragment for _label, fragment in _renpy_python_fragments_with_labels(module_source)]


_TASK5_LABEL_PYTHON = {
    "winter_interlude_start": (
        "_winter_interlude_blank_entry = not _new_run_bootstrap_done",
        'first_decree = ""',
        'southern_outcome = "delegated"',
        "built_granary = False",
        "famine_prevented = False",
        'gov_merchant_outcome = ""',
        "governance_events_seen[:] = [event for event in governance_events_seen if event not in WINTER_LEGACY_EVENTS]",
        "_winter_entry_context = get_winter_context(outside=False)",
        "apply_winter_delegation()",
        'auto_chapter_save("winter_interlude")',
        'winter_interlude_status = "active"',
    ),
    "winter_interlude_delegate": ("apply_winter_delegation()",),
    "winter_interlude_cleanup": (
        "clear_weather()",
        'renpy.music.stop(channel="sound", fadeout=0.0)',
        "hide_all_chars()",
        "stop_music(fadeout=0.0)",
    ),
}
_TASK5_LABEL_AST = {
    label: {
        ast.dump(ast.parse(fragment), include_attributes=False)
        for fragment in fragments
    }
    for label, fragments in _TASK5_LABEL_PYTHON.items()
}


def _is_approved_task5_label_fragment(label: str | None, tree: ast.Module) -> bool:
    return (
        label in _TASK5_LABEL_AST
        and ast.dump(tree, include_attributes=False) in _TASK5_LABEL_AST[label]
    )


def _attribute_path(node: ast.AST) -> str | None:
    names = []
    while isinstance(node, ast.Attribute):
        names.append(node.attr)
        node = node.value
    if not isinstance(node, ast.Name):
        return None
    names.append(node.id)
    return ".".join(reversed(names))


def _is_approved_marker_helper(node: ast.FunctionDef | ast.AsyncFunctionDef) -> bool:
    if node.name != "_append_winter_compatibility_markers" or len(node.body) != 1:
        return False
    loop = node.body[0]
    if (
        not isinstance(loop, ast.For)
        or not isinstance(loop.target, ast.Name)
        or loop.target.id != "event"
        or not isinstance(loop.iter, (ast.Tuple, ast.List))
        or [item.value for item in loop.iter.elts if isinstance(item, ast.Constant)]
        != ["winter_interlude", "famine_crisis"]
        or len(loop.iter.elts) != 2
        or loop.orelse
        or len(loop.body) != 1
    ):
        return False
    condition = loop.body[0]
    if (
        not isinstance(condition, ast.If)
        or condition.orelse
        or len(condition.body) != 1
        or not isinstance(condition.test, ast.Compare)
        or not isinstance(condition.test.left, ast.Name)
        or condition.test.left.id != "event"
        or len(condition.test.ops) != 1
        or not isinstance(condition.test.ops[0], ast.NotIn)
        or len(condition.test.comparators) != 1
        or not isinstance(condition.test.comparators[0], ast.Name)
        or condition.test.comparators[0].id != "governance_events_seen"
    ):
        return False
    expression = condition.body[0]
    return (
        isinstance(expression, ast.Expr)
        and isinstance(expression.value, ast.Call)
        and _attribute_path(expression.value.func)
        == "governance_events_seen.append"
        and len(expression.value.args) == 1
        and isinstance(expression.value.args[0], ast.Name)
        and expression.value.args[0].id == "event"
        and not expression.value.keywords
    )


class _WinterWriteVisitor(ast.NodeVisitor):
    """Fail closed on writes and calls outside the winter kernel allowlist."""

    _ALLOWED_EXTERNAL_CALLS = {
        "ValueError",
        "WinterContext",
        "any",
        "bool",
        "isinstance",
        "len",
        "namedtuple",
        "tuple",
    }

    def __init__(self, defined_functions: set[str]):
        self.defined_functions = defined_functions
        self.function_globals = []
        self.function_names = []
        self.winter_context_bindings = 0
        self.marker_appends = 0
        self.violations = []

    def _record(self, node: ast.AST, message: str) -> None:
        self.violations.append(f"line {getattr(node, 'lineno', '?')}: {message}")

    def _check_name_write(self, node: ast.Name) -> None:
        if isinstance(node.ctx, ast.Del):
            if not self.function_globals or node.id in self.function_globals[-1]:
                self._record(node, f"delete {node.id}")
            return
        protected_bindings = (
            self._ALLOWED_EXTERNAL_CALLS
            | self.defined_functions
            | {"governance_events_seen"}
        )
        if node.id in protected_bindings:
            approved_context_binding = (
                not self.function_globals
                and node.id == "WinterContext"
                and self.winter_context_bindings == 0
            )
            if approved_context_binding:
                self.winter_context_bindings += 1
            else:
                self._record(node, f"callable or marker binding {node.id}")
        if not self.function_globals:
            allowed_constant = bool(
                re.fullmatch(r"WINTER_[A-Z0-9_]+", node.id)
            ) or node.id == "WinterContext"
            if node.id not in WINTER_ASSIGNABLE_STORE_DEFAULTS and not allowed_constant:
                self._record(node, f"store assignment {node.id}")
        elif node.id in self.function_globals[-1] and node.id not in WINTER_ASSIGNABLE_STORE_DEFAULTS:
            self._record(node, f"global assignment {node.id}")

    def _check_implicit_name_write(self, name: str, node: ast.AST) -> None:
        binding = ast.Name(id=name, ctx=ast.Store())
        binding.lineno = getattr(node, "lineno", 0)
        self._check_name_write(binding)

    def visit_Name(self, node: ast.Name) -> None:
        if isinstance(node.ctx, (ast.Store, ast.Del)):
            self._check_name_write(node)

    def visit_Attribute(self, node: ast.Attribute) -> None:
        if isinstance(node.ctx, (ast.Store, ast.Del)):
            path = _attribute_path(node)
            if path not in {
                f"store.{name}" for name in WINTER_ASSIGNABLE_STORE_DEFAULTS
            }:
                self._record(node, f"attribute assignment {path or '<dynamic>'}")
        self.generic_visit(node)

    def visit_Subscript(self, node: ast.Subscript) -> None:
        if isinstance(node.ctx, (ast.Store, ast.Del)):
            self._record(node, "subscript assignment")
        self.generic_visit(node)

    def visit_AugAssign(self, node: ast.AugAssign) -> None:
        approved = False
        if isinstance(node.target, ast.Name):
            approved = node.target.id in WINTER_ASSIGNABLE_STORE_DEFAULTS and (
                not self.function_globals
                or node.target.id in self.function_globals[-1]
            )
        elif isinstance(node.target, ast.Attribute):
            approved = _attribute_path(node.target) in {
                f"store.{name}" for name in WINTER_ASSIGNABLE_STORE_DEFAULTS
            }
        if not approved:
            self._record(node, "unapproved augmented assignment")
        self.visit(node.target)
        self.visit(node.value)

    def visit_Global(self, node: ast.Global) -> None:
        for name in node.names:
            if name not in WINTER_ASSIGNABLE_STORE_DEFAULTS:
                self._record(node, f"global declaration {name}")

    def visit_ExceptHandler(self, node: ast.ExceptHandler) -> None:
        if node.type is not None:
            self.visit(node.type)
        if node.name is not None:
            self._check_implicit_name_write(node.name, node)
        for statement in node.body:
            self.visit(statement)

    def visit_MatchAs(self, node: ast.MatchAs) -> None:
        if node.pattern is not None:
            self.visit(node.pattern)
        if node.name is not None:
            self._check_implicit_name_write(node.name, node)

    def visit_MatchStar(self, node: ast.MatchStar) -> None:
        if node.name is not None:
            self._check_implicit_name_write(node.name, node)

    def visit_MatchMapping(self, node: ast.MatchMapping) -> None:
        for key in node.keys:
            self.visit(key)
        for pattern in node.patterns:
            self.visit(pattern)
        if node.rest is not None:
            self._check_implicit_name_write(node.rest, node)

    def _visit_function(self, node: ast.FunctionDef | ast.AsyncFunctionDef) -> None:
        if not self.function_globals and "winter" not in node.name.lower():
            self._record(node, f"non-winter store function {node.name}")
        elif self.function_globals:
            binding = ast.Name(id=node.name, ctx=ast.Store())
            binding.lineno = node.lineno
            self._check_name_write(binding)
        if node.name == "_append_winter_compatibility_markers" and not _is_approved_marker_helper(node):
            self._record(node, "marker helper is not the exact idempotent AST")
        for decorator in node.decorator_list:
            self._record(decorator, "function decorator")
        for expression in [*node.args.defaults, *node.args.kw_defaults]:
            if expression is not None:
                self.visit(expression)
        function_arguments = [
            *node.args.posonlyargs,
            *node.args.args,
            *node.args.kwonlyargs,
        ]
        if node.args.vararg is not None:
            function_arguments.append(node.args.vararg)
        if node.args.kwarg is not None:
            function_arguments.append(node.args.kwarg)
        protected_bindings = (
            self._ALLOWED_EXTERNAL_CALLS
            | self.defined_functions
            | {"governance_events_seen"}
        )
        for argument in function_arguments:
            if argument.arg in protected_bindings:
                self._record(argument, f"callable or marker parameter {argument.arg}")
            if argument.annotation is not None:
                self.visit(argument.annotation)
        if node.returns is not None:
            self.visit(node.returns)
        for type_parameter in getattr(node, "type_params", ()):
            self.visit(type_parameter)
        declared_globals = {
            name
            for child in ast.walk(node)
            if isinstance(child, ast.Global)
            for name in child.names
        }
        self.function_globals.append(declared_globals)
        self.function_names.append(node.name)
        for statement in node.body:
            self.visit(statement)
        self.function_names.pop()
        self.function_globals.pop()

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        self._visit_function(node)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        self._visit_function(node)

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        self._record(node, f"class declaration {node.name}")

    def visit_Lambda(self, node: ast.Lambda) -> None:
        self._record(node, "lambda declaration")

    def visit_Import(self, node: ast.Import) -> None:
        self._record(node, "unapproved import")

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        approved = (
            not self.function_globals
            and node.module == "collections"
            and len(node.names) == 1
            and node.names[0].name == "namedtuple"
            and node.names[0].asname is None
        )
        if not approved:
            self._record(node, "unapproved import")

    def visit_Call(self, node: ast.Call) -> None:
        approved = False
        if isinstance(node.func, ast.Name):
            approved = (
                node.func.id in self.defined_functions
                or node.func.id in self._ALLOWED_EXTERNAL_CALLS
            )
        elif isinstance(node.func, ast.Attribute):
            approved = (
                _attribute_path(node.func) == "governance_events_seen.append"
                and self.function_names
                and self.function_names[-1]
                == "_append_winter_compatibility_markers"
                and len(node.args) == 1
                and isinstance(node.args[0], ast.Name)
                and node.args[0].id == "event"
                and not node.keywords
            )
            if approved:
                self.marker_appends += 1
        if not approved:
            self._record(node, "unapproved function or mutator call")
        self.generic_visit(node)


def _winter_module_write_violations(
    module_source: str,
    store_defaults: set[str],
    persistent_defaults: set[str],
) -> list[str]:
    """Return state writes forbidden inside the winter kernel."""
    del store_defaults, persistent_defaults
    violations = []
    allowed_defaults = {
        "winter_interlude_status",
        "winter_investigations",
        "winter_policy",
        "winter_seed_priority",
    }
    seen_defaults = set()
    init_block_count = 0
    for raw_line in module_source.splitlines():
        stripped = raw_line.strip()
        if not stripped or stripped.startswith("#") or raw_line != raw_line.lstrip():
            continue
        default_match = re.match(
            r"^default\s+([A-Za-z_][A-Za-z0-9_]*)\s*=", stripped
        )
        if default_match and default_match.group(1) in allowed_defaults:
            name = default_match.group(1)
            if name in seen_defaults:
                violations.append(f"duplicate winter default: {name}")
            seen_defaults.add(name)
        elif re.fullmatch(r"init python:\s*(?:#.*)?", stripped):
            init_block_count += 1
            if init_block_count > 1:
                violations.append("more than one init python block")
        elif re.fullmatch(
            r"label\s+[A-Za-z_][A-Za-z0-9_]*(?:\([^)]*\))?\s*:", stripped
        ):
            pass  # Label-body Python is checked from its extracted AST.
        else:
            violations.append(f"unapproved top-level Ren'Py statement: {stripped}")

    trees = []
    task5_fragment_counts = {}
    for label, fragment in _renpy_python_fragments_with_labels(module_source):
        try:
            tree = ast.parse(fragment)
        except SyntaxError as error:
            violations.append(f"Python parse failure: {error.msg}")
            continue
        if _is_approved_task5_label_fragment(label, tree):
            key = (label, ast.dump(tree, include_attributes=False))
            task5_fragment_counts[key] = task5_fragment_counts.get(key, 0) + 1
            if task5_fragment_counts[key] > 1:
                violations.append(f"duplicate approved Task 5 label fragment: {label}")
            continue
        trees.append(tree)
    defined_functions = {
        node.name
        for tree in trees
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    marker_appends = 0
    for tree in trees:
        visitor = _WinterWriteVisitor(defined_functions)
        visitor.visit(tree)
        violations.extend(visitor.violations)
        marker_appends += visitor.marker_appends
    if marker_appends > 1:
        violations.append("more than one governance marker append")
    return violations


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

    def test_test_game_diff_allows_winter_suites_with_key_guard_global_exit_five_lint_roots_and_one_choice_gate(self):
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
        winter_block = re.search(
            r"(?ms)^## BEGIN TASK 3 WINTER STATE SUITES\n.*?^## END TASK 3 WINTER STATE SUITES\n\n\n",
            self.test_game,
        )
        self.assertIsNotNone(winter_block)
        test_game_without_winter = (
            self.test_game[: winter_block.start()]
            + self.test_game[winter_block.end() :]
        )
        task6_bootstrap_row = (
            '            ("winter_interlude_start", '
            '"_call_new_run_bootstrap_winter_interlude"),\n'
        )
        self.assertEqual(test_game_without_winter.count(task6_bootstrap_row), 1)
        test_game_without_winter = test_game_without_winter.replace(
            task6_bootstrap_row, ""
        )
        self.assertEqual(test_game_without_winter, expected)
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

    def test_recorded_baseline_contains_the_three_signed_continuations(self):
        result = subprocess.run(
            ["git", "show", f"{BASELINE_COMMIT}:game/chapter2.rpy"],
            cwd=ROOT,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        self.assertEqual(result.returncode, 0, result.stderr.decode("utf-8", errors="replace"))
        baseline = result.stdout.decode("utf-8")
        self.assertEqual(
            re.findall(
                r"(?m)^\s*call\s+gov_(?:merchant|building(?:\(2\))?|famine_crisis)"
                r".*\sfrom\s+(_call_gov_(?:merch|build|famine)2)\s*$",
                baseline,
            ),
            ["_call_gov_merch2", "_call_gov_build2", "_call_gov_famine2"],
        )

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
            actual_hash = hashlib.sha256(path.read_bytes()).hexdigest()
            if entry["relative_path"] == "game/msyh.ttf":
                package_font = subprocess.run(
                    ["git", "show", f"{PACKAGE_BASELINE_COMMIT}:game/msyh.ttf"],
                    cwd=ROOT,
                    check=True,
                    stdout=subprocess.PIPE,
                ).stdout
                self.assertEqual(actual_hash, hashlib.sha256(package_font).hexdigest())
            else:
                self.assertEqual(entry["sha256"].lower(), actual_hash)


class WinterRoutingContractTests(unittest.TestCase):
    def test_mainline_routes_southern_then_winter_then_chapter2(self):
        chapter_one_end = _label_body(SCRIPT.read_text(encoding="utf-8"), "chapter1_end")
        winter_source = WINTER_MODULE.read_text(encoding="utf-8")
        winter_start = _label_body(winter_source, "winter_interlude_start")
        executable = _executable_lines(chapter_one_end)
        seam = [
            '$ auto_chapter_save("southern")',
            "$ southern_from_mainline = True",
            "call southern_arc from _call_southern_arc",
            "jump winter_interlude_start",
        ]
        positions = [executable.index(statement) for statement in seam]
        self.assertEqual(positions, sorted(positions))
        self.assertNotIn("jump chapter2_start", executable)
        self.assertIn(
            "call new_run_bootstrap from _call_new_run_bootstrap_winter_interlude",
            winter_start,
        )
        self.assertIn('auto_chapter_save("winter_interlude")', winter_start)
        self.assertEqual(winter_source.count("jump chapter2_start"), 1)
        winter_entry_contract = [
            "$ _winter_interlude_blank_entry = not _new_run_bootstrap_done",
            "call new_run_bootstrap from _call_new_run_bootstrap_winter_interlude",
            "if _winter_interlude_blank_entry:",
            '$ first_decree = ""',
            '$ southern_outcome = "delegated"',
            "$ built_granary = False",
            "$ famine_prevented = False",
            '$ gov_merchant_outcome = ""',
            "$ governance_events_seen[:] = [event for event in governance_events_seen if event not in WINTER_LEGACY_EVENTS]",
            "$ _winter_entry_context = get_winter_context(outside=False)",
            '$ auto_chapter_save("winter_interlude")',
        ]

        def entry_contract_violations(candidate_source: str) -> list[str]:
            try:
                candidate_body = _label_body(candidate_source, "winter_interlude_start")
            except AssertionError:
                return ["winter_interlude_start"]
            candidate_lines = candidate_body.splitlines()
            positions = []
            missing = []
            for statement_index, statement in enumerate(winter_entry_contract):
                indentation = "        " if 3 <= statement_index <= 8 else "    "
                exact_line = indentation + statement
                matches = [
                    line_index
                    for line_index, line in enumerate(candidate_lines)
                    if line == exact_line
                ]
                if len(matches) != 1:
                    missing.append(statement)
                else:
                    positions.append(matches[0])
            if missing:
                return missing
            if positions != sorted(positions):
                return ["entry order"]
            return []

        self.assertEqual(entry_contract_violations(winter_source), [])
        self.assertRegex(
            winter_source,
            r'(?m)^\s*WINTER_LEGACY_EVENTS\s*=\s*\("famine_crisis", "merchant_negotiation"\)\s*$',
        )
        for statement in winter_entry_contract:
            with self.subTest(deleted_winter_entry_statement=statement):
                mutated = winter_source.replace(statement, "", 1)
                self.assertTrue(entry_contract_violations(mutated))
        dedented_seed = winter_source.replace(
            '        $ first_decree = ""',
            '    $ first_decree = ""',
            1,
        )
        self.assertTrue(entry_contract_violations(dedented_seed))

        def active_branch_violations(candidate_source: str) -> list[str]:
            try:
                candidate_lines = _label_body(
                    candidate_source, "winter_interlude_start"
                ).splitlines()
            except AssertionError:
                return ["winter_interlude_start"]
            required_lines = (
                "    menu:",
                '        "亲自主持":',
                '            $ winter_interlude_status = "active"',
                '        "交给奥尔德里克":',
            )
            positions = []
            for exact_line in required_lines:
                matches = [
                    line_index
                    for line_index, line in enumerate(candidate_lines)
                    if line == exact_line
                ]
                if len(matches) != 1:
                    return [exact_line.strip()]
                positions.append(matches[0])
            if positions != sorted(positions):
                return ["active branch ownership"]
            if candidate_source.count('$ winter_interlude_status = "active"') != 1:
                return ["active write count"]
            return []

        self.assertEqual(active_branch_violations(winter_source), [])
        dedented_active = winter_source.replace(
            '            $ winter_interlude_status = "active"',
            '        $ winter_interlude_status = "active"',
            1,
        )
        self.assertTrue(active_branch_violations(dedented_active))
        delegated_active = winter_source.replace(
            '            $ winter_interlude_status = "active"\n',
            "",
            1,
        ).replace(
            '        "交给奥尔德里克":\n',
            '        "交给奥尔德里克":\n'
            '            $ winter_interlude_status = "active"\n',
            1,
        )
        self.assertTrue(active_branch_violations(delegated_active))
        chapter_two_source = CHAPTER2.read_text(encoding="utf-8")
        chapter_blank_contract = (
            "    $ _chapter2_blank_entry = not _new_run_bootstrap_done",
            "    call new_run_bootstrap from _call_new_run_bootstrap_chapter2",
            "    if _chapter2_blank_entry:",
            "        $ apply_winter_delegation()",
            "    $ renpy.force_autosave()",
            '    $ auto_chapter_save("chapter2")',
            "    $ snapshot_chapter_start()",
        )

        def chapter_blank_violations(candidate_source: str) -> list[str]:
            try:
                candidate_lines = _label_body(
                    candidate_source, "chapter2_start"
                ).splitlines()
            except AssertionError:
                return ["chapter2_start"]
            positions = []
            for exact_line in chapter_blank_contract:
                matches = [
                    line_index
                    for line_index, line in enumerate(candidate_lines)
                    if line == exact_line
                ]
                if len(matches) != 1:
                    return [exact_line.strip()]
                positions.append(matches[0])
            if positions != sorted(positions):
                return ["chapter2 blank order"]
            return []

        self.assertEqual(chapter_blank_violations(chapter_two_source), [])
        dedented_chapter_delegation = chapter_two_source.replace(
            "        $ apply_winter_delegation()",
            "    $ apply_winter_delegation()",
            1,
        )
        self.assertTrue(chapter_blank_violations(dedented_chapter_delegation))

    def test_chapter2_stops_calling_three_legacy_events(self):
        chapter_two = CHAPTER2.read_text(encoding="utf-8")
        executable = _executable_lines(chapter_two)
        for old_call in (
            "call gov_merchant from _call_gov_merch2",
            "call gov_building(2) from _call_gov_build2",
            "call gov_famine_crisis from _call_gov_famine2",
        ):
            with self.subTest(old_call=old_call):
                self.assertNotIn(old_call, executable)
        governance = GOVERNANCE.read_text(encoding="utf-8")
        for old_label in ("gov_merchant", "gov_building", "gov_famine_crisis"):
            with self.subTest(old_label=old_label):
                self.assertEqual(
                    len(
                        re.findall(
                            rf"(?m)^label {re.escape(old_label)}(?:\([^\n]*\))?:\s*$",
                            governance,
                        )
                    ),
                    1,
                )

    def test_three_legacy_continuations_and_two_stable_anchors_exist_once(self):
        chapter_two = CHAPTER2.read_text(encoding="utf-8")
        for label in (
            "ch2_after_winter_interlude",
            "ch2_after_legacy_governance",
            "_call_gov_merch2",
            "_call_gov_build2",
            "_call_gov_famine2",
        ):
            with self.subTest(label=label):
                self.assertEqual(
                    len(re.findall(rf"(?m)^label {re.escape(label)}:\s*$", chapter_two)),
                    1,
                )
        self.assertNotRegex(
            chapter_two,
            r"(?m)^\s*call\s+\S+.*\sfrom\s+_call_gov_(?:merch|build|famine)2\s*$",
        )

    def test_legacy_pads_are_behind_an_unconditional_fallthrough_firewall(self):
        chapter_two = CHAPTER2.read_text(encoding="utf-8")
        random_call = chapter_two.index("call re_scene_event(2) from _call_re_scene_ev2")
        firewall = chapter_two.index("jump ch2_preparation", random_call)
        preparation = chapter_two.index("label ch2_preparation:", firewall)
        pads = [
            chapter_two.index(f"label {label}:", firewall, preparation)
            for label in ("_call_gov_merch2", "_call_gov_build2", "_call_gov_famine2")
        ]
        self.assertLess(random_call, firewall)
        self.assertEqual(pads, sorted(pads))
        expected_targets = {
            "_call_gov_merch2": "ch2_after_winter_interlude",
            "_call_gov_build2": "ch2_after_legacy_governance",
            "_call_gov_famine2": "ch2_after_legacy_governance",
        }
        for label, target in expected_targets.items():
            body = _label_body(chapter_two, label)
            self.assertIn("$ mark_winter_legacy()", body)
            self.assertRegex(body, r"call winter_interlude_cleanup\(False\) from _call_winter_cleanup_legacy_")
            self.assertIn(f"jump {target}", body)
            self.assertNotRegex(body, r"\b(?:call|jump)\s+gov_(?:merchant|building|famine_crisis)\b")
            self.assertNotIn("winter_interlude_start", body)

    def test_every_exit_calls_the_shared_presentation_cleanup(self):
        winter_source = WINTER_MODULE.read_text(encoding="utf-8")
        cleanup = _label_body(winter_source, "winter_interlude_cleanup")
        self.assertIn("$ clear_weather()", cleanup)
        self.assertIn("$ hide_all_chars()", cleanup)
        self.assertIn("return", _executable_lines(cleanup))
        self.assertNotIn("chapter2_start", cleanup)
        chapter_two = CHAPTER2.read_text(encoding="utf-8")
        self.assertEqual(winter_source.count("call winter_interlude_cleanup"), 1)
        self.assertEqual(chapter_two.count("call winter_interlude_cleanup(False)"), 3)
        exit_body = _label_body(winter_source, "winter_interlude_exit")
        self.assertRegex(exit_body, r"call winter_interlude_cleanup from _call_winter_cleanup_exit")
        self.assertIn("jump chapter2_start", exit_body)

    def test_chapter2_restarts_music_after_cinematic(self):
        chapter_start = _label_body(CHAPTER2.read_text(encoding="utf-8"), "chapter2_start")
        after_cinematic = chapter_start.split(
            "call cinematic_chapter2 from _call_cinematic_ch2", 1
        )[1]
        executable = _executable_lines(after_cinematic)
        self.assertEqual(
            executable[0],
            '$ play_music("audio/music/castle_calm.ogg", fadein=2.0)',
        )
        self.assertNotIn("set_mood", executable[0])

    def test_one_month_card_is_not_repeated_in_chapter2_body(self):
        chapter_start = _label_body(CHAPTER2.read_text(encoding="utf-8"), "chapter2_start")
        cinematic = _label_body(CINEMATICS.read_text(encoding="utf-8"), "cinematic_chapter2")
        self.assertEqual(cinematic.count("一个月过去了。"), 1)
        self.assertEqual(chapter_start.count("一个月过去了。"), 0)


class WinterChapterSelectContractTests(unittest.TestCase):
    WINTER_ROW = (
        "winter_interlude",
        "幕间",
        "第一个冬天",
        "winter_interlude_start",
        "粮价、库存与必须有人承担的缺口",
    )

    def test_three_parallel_chapter_lists_stay_aligned(self):
        gallery = GALLERY.read_text(encoding="utf-8")
        images_def = IMAGES_DEF.read_text(encoding="utf-8")
        chapter_list = _literal_list_assignment(gallery, "chapter_list")
        chapter_icons = _literal_list_assignment(gallery, "chapter_icons")
        ui_chapter_icons = _literal_list_assignment(images_def, "UI_CHAPTER_ICONS")
        chapter_ids = [row[0] for row in chapter_list]

        self.assertIn("winter_interlude", chapter_ids)
        winter_index = chapter_ids.index("winter_interlude")
        self.assertEqual(chapter_list[winter_index], self.WINTER_ROW)
        self.assertEqual(chapter_icons[winter_index], "幕")
        self.assertEqual(ui_chapter_icons[winter_index], "ch_winter_interlude")
        self.assertEqual(len(chapter_list), len(chapter_icons))
        self.assertEqual(len(chapter_list), len(ui_chapter_icons))
        self.assertEqual(winter_index, chapter_ids.index("southern") + 1)
        self.assertEqual(chapter_ids.index("chapter2"), winter_index + 1)

    def test_winter_unlocks_from_chapter1_and_uses_text_fallback(self):
        gallery = GALLERY.read_text(encoding="utf-8")
        images_def = IMAGES_DEF.read_text(encoding="utf-8")
        chapter_screen = gallery.split("screen chapter_select():", 1)[1]
        unlock_lines = [
            line.strip()
            for line in chapter_screen.splitlines()
            if line.strip().startswith("$ is_unlocked =")
        ]

        self.assertEqual(len(unlock_lines), 1)
        actual_module = ast.parse(unlock_lines[0].removeprefix("$ "))
        self.assertEqual(len(actual_module.body), 1)
        actual_assignment = actual_module.body[0]
        self.assertIsInstance(actual_assignment, ast.Assign)
        self.assertEqual(len(actual_assignment.targets), 1)
        self.assertIsInstance(actual_assignment.targets[0], ast.Name)
        self.assertEqual(actual_assignment.targets[0].id, "is_unlocked")
        expected_rhs = ast.parse(
            'is_unlocked = ch_id in persistent.chapters_completed or ch_id == "chapter1" '
            'or ch_id == "prologue" or (ch_id == "winter_interlude" and '
            '"chapter1" in persistent.chapters_completed)'
        ).body[0].value
        expected_dump = ast.dump(expected_rhs, include_attributes=False)

        def assert_exact_unlock(rhs):
            self.assertEqual(ast.dump(rhs, include_attributes=False), expected_dump)

        assert_exact_unlock(actual_assignment.value)
        unparenthesized_mutation = ast.parse(
            'is_unlocked = ch_id in persistent.chapters_completed or ch_id == "chapter1" '
            'or ch_id == "prologue" or ch_id == "winter_interlude" '
            'or "chapter1" in persistent.chapters_completed'
        ).body[0].value
        with self.assertRaises(AssertionError):
            assert_exact_unlock(unparenthesized_mutation)

        compiled_rhs = compile(
            ast.Expression(actual_assignment.value),
            "<chapter-select-unlock>",
            "eval",
        )
        for completed, chapter_id, expected in (
            (set(), "winter_interlude", False),
            ({"chapter1"}, "winter_interlude", True),
            ({"chapter1"}, "chapter2", False),
        ):
            persistent = type(
                "Persistent", (), {"chapters_completed": completed}
            )()
            with self.subTest(completed=completed, chapter_id=chapter_id):
                self.assertIs(
                    eval(
                        compiled_rhs,
                        {"__builtins__": {}},
                        {"ch_id": chapter_id, "persistent": persistent},
                    ),
                    expected,
                )
        self.assertFalse(
            (ROOT / "game" / "images" / "ui" / "ch_winter_interlude.png").exists()
        )
        ui_icon_body = re.search(
            r"(?ms)^    def ui_icon\(name, size=40\):\s*\n(.*?)(?=^    def |^    ## |\Z)",
            images_def,
        )
        self.assertIsNotNone(ui_icon_body)
        self.assertIn("if renpy.loadable(path):", ui_icon_body.group(1))
        self.assertIn("return None", ui_icon_body.group(1))
        self.assertGreaterEqual(chapter_screen.count("text chapter_icons[idx]"), 2)

    def test_blank_start_protects_auto_winter_slot(self):
        gallery = GALLERY.read_text(encoding="utf-8")
        chapter_screen = gallery.split("screen chapter_select():", 1)[1]
        whitelist = re.search(
            r"(?ms)if ch_id in (\([^\n]+\))\s*\n\s*else Start\(ch_label\)",
            chapter_screen,
        )

        self.assertIsNotNone(whitelist)
        protected_ids = ast.literal_eval(whitelist.group(1))
        self.assertIn("winter_interlude", protected_ids)
        self.assertIn('$ ch_slot = "auto_ch-" + ch_id', chapter_screen)
        self.assertIn("$ has_slot = renpy.can_load(ch_slot)", chapter_screen)
        self.assertIn(
            'SetField(persistent, "_skip_next_chapter_autosave", True)',
            chapter_screen,
        )
        self.assertIn("Start(ch_label)", chapter_screen)
        self.assertIn("action FileLoad(ch_slot, slot=True)", chapter_screen)
        self.assertLess(
            chapter_screen.index(
                'SetField(persistent, "_skip_next_chapter_autosave", True)'
            ),
            chapter_screen.index("Start(ch_label)"),
        )
        self.assertNotIn('$ first_decree = ""', chapter_screen)


class WinterModuleContractTests(unittest.TestCase):
    def test_deep_module_and_four_defaults_exist(self):
        self.assertTrue(
            WINTER_MODULE.is_file(),
            "game/governance_winter_interlude.rpy does not exist",
        )
        source = WINTER_MODULE.read_text(encoding="utf-8")
        defaults = re.findall(
            r"(?m)^default\s+(winter_[a-z_]+)\s*=\s*([^\n#]+?)\s*$", source
        )
        self.assertEqual(
            defaults,
            [
                ("winter_interlude_status", '"unseen"'),
                ("winter_investigations", "()"),
                ("winter_policy", '""'),
                ("winter_seed_priority", '"neutral"'),
            ],
        )

    def test_state_enum_and_public_helper_signatures_exist(self):
        self.assertTrue(
            WINTER_MODULE.is_file(),
            "winter state helpers are missing with governance_winter_interlude.rpy",
        )
        source = WINTER_MODULE.read_text(encoding="utf-8")
        constants = {
            "WINTER_STATUSES": '("unseen", "active", "delegated", "completed", "legacy")',
            "WINTER_INVESTIGATION_ORDER": '("market", "village", "granary", "route")',
            "WINTER_POLICIES": '("trade", "ration", "requisition")',
            "WINTER_SEED_PRIORITIES": '("preserve", "feed_now")',
            "WINTER_LEGACY_EVENTS": '("famine_crisis", "merchant_negotiation")',
        }
        for name, value in constants.items():
            with self.subTest(name=name):
                self.assertRegex(
                    source,
                    rf"(?m)^\s*{name}\s*=\s*{re.escape(value)}\s*$",
                )
        signatures = (
            "normalize_winter_investigations(values)",
            "resolve_winter_interlude_context(raw_snapshot, projection)",
            "get_winter_context(outside=True)",
            "apply_winter_delegation()",
            "finalize_winter_interlude(policy, seed_priority, investigations)",
            "mark_winter_legacy()",
            "migrate_winter_interlude_state()",
            "winter_legacy_famine_success()",
            "select_winter_mitigation(policy, seed_priority, investigations, immediate_inputs)",
        )
        for signature in signatures:
            with self.subTest(signature=signature):
                self.assertRegex(
                    source,
                    rf"(?m)^\s*def\s+{re.escape(signature)}\s*:",
                )
        self.assertRegex(source, r"(?m)^\s*WINTER_OUTCOME_CONTRACTS\s*=\s*\{")
        self.assertNotIn("hasattr", source)

    def test_new_module_has_no_forbidden_main_state_writes(self):
        self.assertTrue(
            WINTER_MODULE.is_file(),
            "winter module is missing, so forbidden writes cannot be inspected",
        )
        module_source = WINTER_MODULE.read_text(encoding="utf-8")
        store_defaults, persistent_defaults = _project_default_inventory()
        forbidden_store = (
            store_defaults - WINTER_ALLOWED_STORE_DEFAULT_WRITES
        ) | WINTER_NONDEFAULT_FORBIDDEN_STATE
        required_store_examples = {
            "path_marks_martial",
            "path_active_martial",
            "dark_lily_joined",
            "dark_lily_destroyed",
            "governance_prosperity",
            "ending_epilogue_seen",
            "iron_battle_outcome",
        }
        required_persistent_examples = {
            "achievements",
            "endings_seen",
            "northern_endings_seen",
            "southern_endings_seen",
        }
        self.assertTrue(required_store_examples <= forbidden_store)
        self.assertTrue(required_persistent_examples <= persistent_defaults)
        self.assertTrue(WINTER_NONDEFAULT_FORBIDDEN_STATE.isdisjoint(store_defaults))

        test_game = TEST_GAME.read_text(encoding="utf-8")
        winter_block = re.search(
            r"(?ms)^## BEGIN TASK 3 WINTER STATE SUITES\n(.*?)^## END TASK 3 WINTER STATE SUITES",
            test_game,
        )
        self.assertIsNotNone(winter_block)
        runtime_contract = winter_block.group(1)
        if "renpy.ast.default_statements" not in runtime_contract:
            static_inventory = re.search(
                r"(?ms)_winter_forbidden_names\s*=\s*\((.*?)\)\s*_winter_forbidden_snapshot",
                runtime_contract,
            )
            declared = set()
            if static_inventory:
                declared = set(
                    re.findall(r'[\"\']([A-Za-z_][A-Za-z0-9_]*)[\"\']', static_inventory.group(1))
                )
            missing = sorted(forbidden_store - declared)
            self.fail(
                "runtime forbidden snapshot is hand-maintained and omits project defaults: "
                + ", ".join(missing)
            )
        allowed_match = re.search(
            r"(?ms)_WINTER_ALLOWED_STORE_DEFAULT_WRITES\s*=\s*\((.*?)\)",
            runtime_contract,
        )
        self.assertIsNotNone(allowed_match)
        runtime_allowed = set(
            re.findall(r'[\"\']([A-Za-z_][A-Za-z0-9_]*)[\"\']', allowed_match.group(1))
        )
        self.assertEqual(runtime_allowed, WINTER_ALLOWED_STORE_DEFAULT_WRITES)
        optional_match = re.search(
            r"(?ms)_WINTER_NONDEFAULT_FORBIDDEN_STATE\s*=\s*\((.*?)\)",
            runtime_contract,
        )
        self.assertIsNotNone(optional_match)
        runtime_optional = set(
            re.findall(r'[\"\']([A-Za-z_][A-Za-z0-9_]*)[\"\']', optional_match.group(1))
        )
        self.assertEqual(runtime_optional, WINTER_NONDEFAULT_FORBIDDEN_STATE)
        production_sources = "\n".join(
            path.read_text(encoding="utf-8")
            for path in sorted((ROOT / "game").rglob("*.rpy"))
            if path != TEST_GAME
        )
        for name in WINTER_NONDEFAULT_FORBIDDEN_STATE:
            with self.subTest(nondefault_forbidden=name):
                self.assertRegex(
                    production_sources,
                    rf"(?m)^\s*\$?\s*{re.escape(name)}\s*=",
                )
        self.assertIn("statement.store == store_name", runtime_contract)
        self.assertIn('_test_winter_project_default_names("store")', runtime_contract)
        self.assertIn('_test_winter_project_default_names("store.persistent")', runtime_contract)
        self.assertIn("_test_winter_freeze", runtime_contract)
        self.assertRegex(
            runtime_contract,
            r"(?ms)if isinstance\(value, \(list, tuple\)\):\s+return \(type\(value\)\.__name__,",
        )
        self.assertRegex(
            runtime_contract,
            r"(?ms)if isinstance\(value, \(set, frozenset\)\):.*?return \(type\(value\)\.__name__,",
        )
        self.assertRegex(
            runtime_contract,
            r"(?ms)if isinstance\(value, \(bool, bytes, float, int, str, type\(None\)\)\):\s+return \(type\(value\)\.__name__, value\)",
        )

        violations = _winter_module_write_violations(
            module_source, store_defaults, persistent_defaults
        )
        mutation_probes = {
            "renpy_store_assignment": "$ winter_debt = 1",
            "top_level_approved_field_assignment": "$ winter_policy = 'trade'",
            "label_forbidden_store_assignment": (
                "label winter_probe:\n"
                "    $ power = 99\n"
                "    return"
            ),
            "renpy_define_store_assignment": "define winter_debt = 1",
            "priority_default_store_assignment": "default 10 power = 99",
            "priority_persistent_default_assignment": (
                "default 10 persistent.southern_endings_seen = None"
            ),
            "priority_define_store_assignment": "define 10 power = 99",
            "augmented_define_store_assignment": "define winter_debt += 1",
            "label_python_store_assignment": "label probe:\n    python:\n        winter_debt = 1",
            "init_python_store_assignment": "init python:\n    winter_debt = 1",
            "init_python_hide_store_assignment": (
                "init python hide:\n    store.power = 99"
            ),
            "init_python_named_store_assignment": (
                "init python in mystore:\n    store.power = 99"
            ),
            "named_store_python_assignment": (
                "python in mystore:\n    store.power = 99"
            ),
            "inline_store_assignment": "init python:\n    if True: store.power = 99",
            "inline_persistent_assignment": (
                "init python:\n"
                "    if True: persistent.southern_endings_seen = None"
            ),
            "dynamic_store_setattr": "init python:\n    setattr(store, field_name, 1)",
            "unapproved_state_helper": "init python:\n    change_prosperity(1)",
            "parenthesized_state_helper": "init python:\n    (change_prosperity)(1)",
            "shadowed_allowed_external_call": (
                "init python:\n"
                "    def winter_probe():\n"
                "        len = change_prosperity\n"
                "        len(1)"
            ),
            "nested_only_function_call": (
                "init python:\n"
                "    def winter_holder():\n"
                "        def change_prosperity():\n"
                "            pass\n"
                "    change_prosperity(1)"
            ),
            "decorator_state_helper": (
                "init python:\n"
                "    @unlock_achievement\n"
                "    def winter_probe():\n"
                "        pass"
            ),
            "function_annotation_state_helper": (
                "init python:\n"
                "    def winter_probe(value: change_prosperity()):\n"
                "        pass"
            ),
            "unapproved_container_mutator": "init python:\n    winter_debt.difference_update({1})",
            "persistent_alias_augmented_mutation": (
                "init python:\n"
                "    def winter_probe():\n"
                "        seen = persistent.southern_endings_seen\n"
                "        seen |= {'x'}"
            ),
            "persistent_default_alias_augmented_mutation": (
                "init python:\n"
                "    def winter_probe(seen=persistent.southern_endings_seen):\n"
                "        seen |= {'x'}"
            ),
            "defined_callable_rebinding": (
                "init python:\n"
                "    def WINTER_MUTATOR():\n"
                "        pass\n"
                "    WINTER_MUTATOR = change_prosperity\n"
                "    WINTER_MUTATOR(1)"
            ),
            "shadowed_marker_base": (
                "init python:\n"
                "    def winter_probe(governance_events_seen, event):\n"
                "        governance_events_seen.append(event)\n"
                "    winter_probe(inventory_items, 'x')"
            ),
            "second_marker_append": (
                "init python:\n"
                "    def winter_corrupt_event(event):\n"
                "        governance_events_seen . append(event)"
            ),
            "parenthesized_persistent_mutator": (
                "init python:\n"
                "    (persistent.southern_endings_seen.add)('x')"
            ),
            "unapproved_augmented_assignment": "init python:\n    power %= 2",
            "unapproved_assignment_expression": "init python:\n    (winter_debt := 1)",
            "unapproved_delete": "init python:\n    del power",
            "exception_alias_store_binding": (
                "init python:\n"
                "    try:\n"
                "        pass\n"
                "    except Exception as winter_debt:\n"
                "        pass"
            ),
            "match_capture_store_binding": (
                "init python:\n"
                "    match 1:\n"
                "        case winter_debt:\n"
                "            pass"
            ),
            "quoted_hash_before_assignment": (
                'init python:\n    WINTER_SENTINEL = "#"; store.power = 99'
            ),
            "translate_python_assignment": (
                "translate schinese python:\n    store.power = 99"
            ),
            "persistent_assignment": "init python:\n    persistent.secret = 1",
        }
        self.assertEqual(len(mutation_probes), 37)
        for probe_name, probe_source in mutation_probes.items():
            with self.subTest(mutation_probe=probe_name):
                self.assertTrue(
                    _winter_module_write_violations(
                        probe_source, store_defaults, persistent_defaults
                    ),
                    f"winter source guard accepted forbidden mutation: {probe_name}",
                )
        allowed_mutation_probes = {
            "label_approved_assignment": (
                "label winter_probe:\n"
                "    $ winter_policy = 'trade'\n"
                "    return"
            ),
            "global_approved_assignment": (
                "init python:\n"
                "    def approved_winter_writer():\n"
                "        global winter_policy\n"
                "        winter_policy = 'trade'"
            ),
            "explicit_store_approved_assignment": (
                "init python:\n    store.winter_policy = 'trade'"
            ),
            "idempotent_marker_append": (
                "init python:\n"
                "    def _append_winter_compatibility_markers():\n"
                "        for event in ('winter_interlude', 'famine_crisis'):\n"
                "            if event not in governance_events_seen:\n"
                "                governance_events_seen.append(event)"
            ),
        }
        self.assertEqual(len(allowed_mutation_probes), 4)
        for probe_name, probe_source in allowed_mutation_probes.items():
            with self.subTest(allowed_mutation_probe=probe_name):
                self.assertEqual(
                    _winter_module_write_violations(
                        probe_source, store_defaults, persistent_defaults
                    ),
                    [],
                )
        task5_negative_probes = {
            "wrong_label": module_source.replace(
                "label winter_interlude_start:",
                "label winter_interlude_wrong_start:",
                1,
            ),
            "dynamic_autosave_slot": module_source.replace(
                '$ auto_chapter_save("winter_interlude")',
                "$ auto_chapter_save(_winter_slot)",
                1,
            ),
            "wrong_blank_seed": module_source.replace(
                '$ southern_outcome = "delegated"',
                '$ southern_outcome = "free"',
                1,
            ),
            "cleanup_argument": module_source.replace(
                "$ clear_weather()",
                '$ clear_weather("snow")',
                1,
            ),
            "cleanup_dynamic_character_exception": module_source.replace(
                "$ hide_all_chars()",
                '$ hide_all_chars(_winter_character)',
                1,
            ),
            "sound_stop_wrong_channel": module_source.replace(
                '$ renpy.music.stop(channel="sound", fadeout=0.0)',
                '$ renpy.music.stop(channel="music", fadeout=0.0)',
                1,
            ),
            "music_stop_wrong_shape": module_source.replace(
                "$ stop_music(fadeout=0.0)",
                "$ stop_music()",
                1,
            ),
            "unapproved_extra_store": module_source.replace(
                "label winter_interlude_delegate:\n",
                "label winter_interlude_delegate:\n    $ power = 99\n",
                1,
            ),
        }
        for probe_name, probe_source in task5_negative_probes.items():
            with self.subTest(task5_negative_probe=probe_name):
                self.assertTrue(
                    _winter_module_write_violations(
                        probe_source, store_defaults, persistent_defaults
                    ),
                    f"winter source guard accepted forbidden Task 5 shape: {probe_name}",
                )
        self.assertRegex(
            module_source,
            r'(?ms)for event in \("winter_interlude", "famine_crisis"\):\s*'
            r'if event not in governance_events_seen:\s*'
            r'governance_events_seen\.append\(event\)',
        )
        self.assertEqual(module_source.count("governance_events_seen.append(event)"), 1)
        self.assertEqual(violations, [])

    def test_old_governance_label_bodies_still_exist(self):
        current = GOVERNANCE.read_text(encoding="utf-8")
        baseline = subprocess.run(
            ["git", "show", f"{BASELINE_COMMIT}:game/governance.rpy"],
            cwd=ROOT,
            check=True,
            stdout=subprocess.PIPE,
        ).stdout.decode("utf-8")
        for label in ("gov_merchant", "gov_building", "gov_famine_crisis"):
            with self.subTest(label=label):
                self.assertEqual(_label_body(current, label), _label_body(baseline, label))

    def test_difficulty_module_never_reads_winter_state(self):
        executable = _executable_lines(DIFFICULTY.read_text(encoding="utf-8"))
        self.assertEqual([line for line in executable if "winter_" in line], [])

    def test_fixture_key_is_public_and_enabled_only_for_test_command(self):
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        key = manifest["fixture_verifying_key"]
        test_game = TEST_GAME.read_text(encoding="utf-8")
        self.assertEqual(test_game.count(key), 1)
        self.assertRegex(
            test_game,
            re.escape('python early:\n    if renpy.game.args.command == "test":\n')
            + re.escape(f'        config.save_token_keys.append("{key}")'),
        )
        self.assertNotRegex(
            test_game + MANIFEST.read_text(encoding="utf-8"),
            r"(?i)BEGIN (?:EC |RSA )?PRIVATE KEY|security_keys\.txt",
        )
        release_contract = (ROOT / "Tools" / "test_release_contract.py").read_text(
            encoding="utf-8"
        )
        self.assertIn('"game/test_game.rpyc"', release_contract)

    def test_release_rpyc_contract_accounts_for_winter_module(self):
        self.assertTrue(
            WINTER_MODULE.is_file(),
            "winter module is missing from the released RPYC source set",
        )
        verifier = VERIFY_DISTRIBUTIONS.read_text(encoding="utf-8")
        synthetic = TEST_VERIFY_DISTRIBUTIONS.read_text(encoding="utf-8")
        self.assertRegex(
            verifier, r"(?m)^EXPECTED_RELEASE_RPYC_COUNT\s*=\s*56\s*$"
        )
        self.assertIn("game/governance_winter_interlude.rpyc", synthetic)
        expected_rpycs = {
            source.relative_to(ROOT).with_suffix(".rpyc").as_posix()
            for source in (ROOT / "game").rglob("*.rpy")
            if source.relative_to(ROOT).as_posix() != "game/test_game.rpy"
        }
        self.assertEqual(len(expected_rpycs), 56)
        self.assertIn("game/governance_winter_interlude.rpyc", expected_rpycs)


if __name__ == "__main__":
    unittest.main()

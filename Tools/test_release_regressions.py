#!/usr/bin/env python3
"""Release regression checks for player-visible Ren'Py text."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
GAME_DIR = PROJECT_ROOT / "game"


@dataclass(frozen=True)
class StringLiteral:
    value: str
    start: int
    end: int
    content_start: int = 0


@dataclass(frozen=True)
class TextViolation:
    line_number: int
    line: str
    literal: StringLiteral


TRANSLATION_WRAPPERS = {"_", "__", "_p"}
VISIBLE_SCREEN_STATEMENTS = {"label", "text", "textbutton"}


def _string_literals(source: str) -> list[StringLiteral]:
    """Return quoted strings, including triple-quoted strings, outside comments."""
    literals: list[StringLiteral] = []
    index = 0

    while index < len(source):
        char = source[index]
        if char == "#":
            newline = source.find("\n", index)
            if newline < 0:
                break
            index = newline + 1
            continue
        if char not in {'"', "'"}:
            index += 1
            continue

        quote = char
        delimiter = quote * 3 if source.startswith(quote * 3, index) else quote
        start = index
        index += len(delimiter)
        content_start = index
        escaped = False
        while index < len(source):
            char = source[index]
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif source.startswith(delimiter, index):
                value = source[content_start:index]
                index += len(delimiter)
                literals.append(StringLiteral(value, start, index, content_start))
                break
            index += 1
        else:
            # An unterminated string cannot be classified safely.
            break

    return literals


def _wrapper_before_literal(source: str, literal: StringLiteral) -> bool:
    """Whether the literal is directly enclosed by a string-valued wrapper."""
    index = literal.start - 1
    while index >= 0 and source[index].isspace():
        index -= 1
    if index < 0 or source[index] != "(":
        return False

    # Whitespace before the opening parenthesis means a grouping expression,
    # as in Ren'Py's ``text ("...") % value`` syntax.
    if index == 0 or source[index - 1].isspace():
        return True

    end = index
    start = end - 1
    while start >= 0 and (source[start].isalnum() or source[start] == "_"):
        start -= 1
    return source[start + 1 : end] in TRANSLATION_WRAPPERS


def _is_percent_formatted_literal(source: str, literal: StringLiteral) -> bool:
    """Whether this exact literal is the left operand of Python's % operator."""
    suffix = source[literal.end :].lstrip()
    if suffix.startswith(")") and _wrapper_before_literal(source, literal):
        suffix = suffix[1:].lstrip()
    return suffix.startswith("%") and not suffix.startswith(("%%", "%="))


def _is_player_visible_literal(source: str, literal: StringLiteral) -> bool:
    line_start = source.rfind("\n", 0, literal.start) + 1
    prefix = source[line_start : literal.start].strip()

    if re.search(r"(?:^|\W)(?:_|__|_p)\(\s*$", prefix):
        return True

    # Plain assignments are internal data unless they explicitly use a
    # translation wrapper such as _p(...).
    if "=" in prefix:
        return False

    if not prefix:
        return True

    first_word = prefix.split(None, 1)[0]
    if first_word in VISIBLE_SCREEN_STATEMENTS:
        return True

    # Character say statements consist of identifiers/modifiers before the
    # quoted dialogue. Player-visible log and notification helpers are also
    # common inside init-python blocks.
    if "(" not in prefix and re.fullmatch(r"[A-Za-z_]\w*(?:\s+[A-Za-z_]\w*)*", prefix):
        return True
    return bool(re.search(r"\b\w*(?:log|notify|say)\w*\s*\([^\n]*$", prefix, re.IGNORECASE))


def find_violations_in_text(source: str) -> list[TextViolation]:
    lines = source.splitlines()
    violations: list[TextViolation] = []

    for literal in _string_literals(source):
        doubled = literal.value.find("%%")
        if doubled < 0:
            continue
        if _is_percent_formatted_literal(source, literal):
            continue
        if not _is_player_visible_literal(source, literal):
            continue

        percent_offset = literal.content_start + doubled
        line_number = source.count("\n", 0, percent_offset) + 1
        line = lines[line_number - 1].strip() if line_number <= len(lines) else ""
        violations.append(TextViolation(line_number, line, literal))

    return violations


def _visible_doubled_percent_literals(line: str) -> list[StringLiteral]:
    return [violation.literal for violation in find_violations_in_text(line)]


def _assert_classifier_examples() -> None:
    assert len(_visible_doubled_percent_literals('text "成功率 30%%" size 10')) == 1
    assert len(_visible_doubled_percent_literals('add_log("命中 +20%%")')) == 1
    assert not _visible_doubled_percent_literals('add_log("命中 %d%%" % value)')
    assert not _visible_doubled_percent_literals('text "闪： %d%%" % expr')
    assert not _visible_doubled_percent_literals('# text "成功率 30%%"')
    assert len(
        _visible_doubled_percent_literals(
            'text "成功率 30%%" size 10 color "%s" % color'
        )
    ) == 1


def find_violations() -> list[tuple[Path, int, str]]:
    violations: list[tuple[Path, int, str]] = []
    for path in sorted(GAME_DIR.rglob("*.rpy")):
        source = path.read_text(encoding="utf-8")
        for violation in find_violations_in_text(source):
            violations.append(
                (path.relative_to(PROJECT_ROOT), violation.line_number, violation.line)
            )
    return violations


def main() -> int:
    _assert_classifier_examples()
    violations = find_violations()
    if violations:
        for path, line_number, line in violations:
            print(f"{path.as_posix()}:{line_number}: player-visible '%%': {line}")
        print(f"FAIL: found {len(violations)} player-visible doubled percent literal(s)")
        return 1

    print("PASS: no player-visible doubled percent literals")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

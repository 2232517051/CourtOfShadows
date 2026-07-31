#!/usr/bin/env python3
"""Release regression checks for player-visible Ren'Py text."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
GAME_DIR = PROJECT_ROOT / "game"


@dataclass(frozen=True)
class StringLiteral:
    value: str
    start: int
    end: int


def _string_literals_before_comment(line: str) -> list[StringLiteral]:
    """Return quoted strings on a line, stopping at an unquoted comment."""
    literals: list[StringLiteral] = []
    index = 0

    while index < len(line):
        char = line[index]
        if char == "#":
            break
        if char not in {'"', "'"}:
            index += 1
            continue

        quote = char
        start = index
        index += 1
        value: list[str] = []
        escaped = False
        while index < len(line):
            char = line[index]
            if escaped:
                value.append(char)
                escaped = False
            elif char == "\\":
                value.append(char)
                escaped = True
            elif char == quote:
                index += 1
                literals.append(StringLiteral("".join(value), start, index))
                break
            else:
                value.append(char)
            index += 1
        else:
            # An unterminated string cannot be classified safely on one line.
            break

    return literals


def _is_percent_formatted_literal(line: str, literal: StringLiteral) -> bool:
    """Whether this exact literal is the left operand of Python's % operator."""
    suffix = line[literal.end :].lstrip()
    return suffix.startswith("%") and not suffix.startswith(("%%", "%="))


def _visible_doubled_percent_literals(line: str) -> list[StringLiteral]:
    return [
        literal
        for literal in _string_literals_before_comment(line)
        if "%%" in literal.value and not _is_percent_formatted_literal(line, literal)
    ]


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
        for line_number, line in enumerate(
            path.read_text(encoding="utf-8").splitlines(), start=1
        ):
            if _visible_doubled_percent_literals(line):
                violations.append((path.relative_to(PROJECT_ROOT), line_number, line.strip()))
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

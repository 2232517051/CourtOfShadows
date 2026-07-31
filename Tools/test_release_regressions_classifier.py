#!/usr/bin/env python3
"""Focused tests for the doubled-percent release classifier."""

from __future__ import annotations

import unittest

import test_release_regressions as release_regressions


def violation_lines(source: str) -> list[int]:
    return [
        violation.line_number
        for violation in release_regressions.find_violations_in_text(source)
    ]


class DoubledPercentClassifierTests(unittest.TestCase):
    def test_player_visible_literal_is_reported(self) -> None:
        self.assertEqual(violation_lines('text "success 30%%" size 10'), [1])

    def test_direct_percent_formatting_is_allowed(self) -> None:
        self.assertEqual(violation_lines('add_log("hit %d%%" % value)'), [])

    def test_translated_percent_formatting_is_allowed(self) -> None:
        self.assertEqual(violation_lines('add_log(_("hit %d%%") % value)'), [])

    def test_parenthesized_percent_formatting_is_allowed(self) -> None:
        self.assertEqual(violation_lines('text ("hit %d%%") % value'), [])

    def test_multiline_player_visible_literal_is_reported_at_content_line(self) -> None:
        source = '''define gui.about = _p("""
success 30%%
""")'''
        self.assertEqual(violation_lines(source), [2])

    def test_comments_and_internal_literals_are_ignored(self) -> None:
        source = '''# text "success 30%%"
internal_pattern = "cache%%token"'''
        self.assertEqual(violation_lines(source), [])


if __name__ == "__main__":
    unittest.main()

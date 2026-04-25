"""
Batch-fix missing `show X_img` commands before dialogue lines.

Strategy:
- Re-run the scan logic (same state machine as scan_missing_portraits.py).
- When a dialogue line is flagged as missing its portrait, record an insertion:
    BEFORE the dialogue line, insert two lines with matching indent:
        $ hide_all_chars("TAG")
        show TAG at left with dissolve
- After recording the insertion, UPDATE the simulated active_tags so subsequent
  consecutive same-speaker dialogue in the same branch doesn't get double-inserted.
- For player: determine the variant (player_char / player_child / player_teen /
  player_young) by scanning backwards for the most recent `show player_*_img`.
  Default: player_char_img.

Applies insertions in reverse line order per file so line numbers stay valid.
"""
import os
import re
import sys
from collections import defaultdict

GAME_DIR = os.path.join(os.path.dirname(__file__), "game")

# Reuse definitions from scanner
sys.path.insert(0, os.path.dirname(__file__))
from scan_missing_portraits import (
    collect_character_defs,
    LABEL_RE, SCENE_RE, SHOW_RE, HIDE_RE, HIDE_ALL_RE,
    COMMENT_RE, EMPTY_RE, DIALOGUE_RE,
    IF_RE, ELIF_RE, ELSE_RE, MENU_RE, MENU_OPT_RE,
    indent_of, State, PLAYER_TAGS, NO_PORTRAIT_CHARS,
)


def detect_player_tag(lines, finding_line_idx):
    """Scan backwards from finding line for most recent `show player_*_img`."""
    pattern = re.compile(r'\bshow\s+(player_\w+_img)\b')
    for i in range(finding_line_idx - 1, max(-1, finding_line_idx - 400), -1):
        m = pattern.search(lines[i])
        if m:
            return m.group(1)
    return "player_char_img"


def plan_insertions(path, char_map):
    """Return list of (insertion_line_idx, indent_str, tag) in file order."""
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    insertions = []

    current_label = None
    tracking = False
    state = State()
    block_stack = []

    def close_blocks_up_to(target_indent):
        nonlocal state
        while block_stack and block_stack[-1]["indent"] > target_indent:
            blk = block_stack.pop()
            blk["branch_exit_states"].append(state.copy())
            merged = set()
            for s in blk["branch_exit_states"]:
                merged |= s.active
            if blk["type"] == "if" and not blk.get("has_else"):
                merged |= blk["entry_state"].active
            new_state = State()
            new_state.active = merged
            state = new_state

    def _is_first_option(blk, current_state):
        return not blk["branch_exit_states"] and current_state.active == blk["entry_state"].active

    for lineno, raw in enumerate(lines, 1):
        line = raw.rstrip("\n")
        if EMPTY_RE.match(line) or COMMENT_RE.match(line):
            continue

        cur_indent = indent_of(line)
        close_blocks_up_to(cur_indent)

        m = LABEL_RE.match(line)
        if m:
            current_label = m.group(2)
            tracking = False
            state = State()
            block_stack = []
            continue

        m = IF_RE.match(line)
        if m:
            header_indent = len(m.group(1))
            block_stack.append({
                "header_indent": header_indent,
                "indent": header_indent + 1,
                "type": "if",
                "entry_state": state.copy(),
                "branch_exit_states": [],
                "has_else": False,
                "header_line": lineno,
            })
            continue

        m = ELIF_RE.match(line)
        if m:
            if block_stack and block_stack[-1]["type"] == "if" and block_stack[-1]["header_indent"] == len(m.group(1)):
                block_stack[-1]["branch_exit_states"].append(state.copy())
                state = block_stack[-1]["entry_state"].copy()
            continue

        m = ELSE_RE.match(line)
        if m:
            if block_stack and block_stack[-1]["type"] == "if" and block_stack[-1]["header_indent"] == len(m.group(1)):
                block_stack[-1]["branch_exit_states"].append(state.copy())
                state = block_stack[-1]["entry_state"].copy()
                block_stack[-1]["has_else"] = True
            continue

        m = MENU_RE.match(line)
        if m:
            header_indent = len(m.group(1))
            block_stack.append({
                "header_indent": header_indent,
                "indent": header_indent + 1,
                "type": "menu",
                "entry_state": state.copy(),
                "branch_exit_states": [],
                "has_else": True,
                "header_line": lineno,
            })
            continue

        m = MENU_OPT_RE.match(line)
        if m and block_stack and block_stack[-1]["type"] == "menu":
            opt_indent = len(m.group(1))
            if opt_indent > block_stack[-1]["header_indent"]:
                if block_stack[-1]["branch_exit_states"] or not _is_first_option(block_stack[-1], state):
                    block_stack[-1]["branch_exit_states"].append(state.copy())
                state = block_stack[-1]["entry_state"].copy()
                block_stack[-1]["indent"] = opt_indent
                continue

        if SCENE_RE.match(line):
            tracking = True
            state.active = set()
            continue

        m = HIDE_ALL_RE.match(line)
        if m:
            tracking = True
            args_str = m.group(2).strip()
            keep = set()
            if args_str:
                for tok in args_str.split(","):
                    tok = tok.strip().strip('"').strip("'")
                    if tok:
                        keep.add(tok)
            state.active = state.active & keep
            continue

        m = SHOW_RE.match(line)
        if m:
            tag = m.group(2)
            if tag == "screen" or tag == "black" or tag.startswith("bg"):
                continue
            tracking = True
            state.active.add(tag)
            continue

        m = HIDE_RE.match(line)
        if m:
            tag = m.group(2)
            if tag == "screen":
                continue
            tracking = True
            state.active.discard(tag)
            continue

        m = DIALOGUE_RE.match(line)
        if not m:
            continue

        indent_str = m.group(1)
        speaker = m.group(2)

        if speaker not in char_map:
            continue
        expected_img = char_map[speaker][0]
        if expected_img is None:
            continue

        if not tracking:
            continue

        if speaker == "player":
            if any(t in state.active for t in PLAYER_TAGS):
                continue
            player_tag = detect_player_tag(lines, lineno - 1)
            insertions.append((lineno - 1, indent_str, player_tag))
            state.active.add(player_tag)
            continue

        expected_tag = expected_img + "_img"
        if expected_tag not in state.active:
            insertions.append((lineno - 1, indent_str, expected_tag))
            state.active.add(expected_tag)

    return insertions, lines


def apply_insertions(path, insertions, lines):
    """Apply insertions in reverse line order."""
    for line_idx, indent_str, tag in sorted(insertions, reverse=True):
        insert_lines = [
            f'{indent_str}$ hide_all_chars("{tag}")\n',
            f'{indent_str}show {tag} at left with dissolve\n',
        ]
        lines[line_idx:line_idx] = insert_lines
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.writelines(lines)


def main():
    char_map = collect_character_defs()
    total = 0
    per_file = {}
    for fname in sorted(os.listdir(GAME_DIR)):
        if not fname.endswith(".rpy") or fname.endswith(".bak"):
            continue
        path = os.path.join(GAME_DIR, fname)
        insertions, lines = plan_insertions(path, char_map)
        if not insertions:
            continue
        apply_insertions(path, insertions, lines)
        per_file[fname] = len(insertions)
        total += len(insertions)

    print(f"Applied {total} insertions across {len(per_file)} files:")
    for f, n in sorted(per_file.items(), key=lambda x: -x[1]):
        print(f"  {f}: {n}")


if __name__ == "__main__":
    main()

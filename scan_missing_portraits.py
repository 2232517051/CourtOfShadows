"""
Global scan for dialogue lines that lack corresponding character portraits.

Handles if/elif/else/menu branching by maintaining an indent-aware state stack:
- On entering a block (deeper indent), push current state.
- On sibling branch (elif/else:/new menu option/when), restore to pre-block state.
- On dedent out of the block, merge all branch-exit states (UNION = possibly-shown).

Output: report of dialogue positions where character's _img tag is NOT on active layer.
"""
import os
import re
import sys
import json

GAME_DIR = os.path.join(os.path.dirname(__file__), "game")
IMAGES_DIR = os.path.join(GAME_DIR, "images")

# ------------------------------------------------------------------
# Character definitions
# ------------------------------------------------------------------

CHAR_DEF_RE = re.compile(r'^\s*define\s+(\w+)\s*=\s*Character\s*\((.*)\)\s*$')
IMAGE_PARAM_RE = re.compile(r'image\s*=\s*["\']([\w_]+)["\']')

MANUAL_IMG_TAG = {
    "tax_collector": "tax_collector",
    "farmer_rep": "farmer_rep",
    "merchant_guild": "merchant_guild",
    "healer": "healer",
    "village_elder": "village_elder",
}

PLAYER_TAGS = {"player_char_img", "player_child_img", "player_teen_img", "player_young_img"}
NO_PORTRAIT_CHARS = {"crowd"}


def collect_character_defs():
    defs = {}
    for fname in os.listdir(GAME_DIR):
        if not fname.endswith(".rpy") or fname.endswith(".bak"):
            continue
        with open(os.path.join(GAME_DIR, fname), "r", encoding="utf-8") as f:
            for i, line in enumerate(f, 1):
                m = CHAR_DEF_RE.match(line)
                if not m:
                    continue
                short, args = m.group(1), m.group(2)
                img_match = IMAGE_PARAM_RE.search(args)
                if img_match:
                    defs[short] = (img_match.group(1), fname, i)
                elif short in MANUAL_IMG_TAG:
                    defs[short] = (MANUAL_IMG_TAG[short], fname, i)
                else:
                    defs[short] = (None, fname, i)
    return defs


def list_portrait_files():
    out = set()
    if os.path.isdir(IMAGES_DIR):
        for name in os.listdir(IMAGES_DIR):
            if name.lower().endswith(".png"):
                out.add(os.path.splitext(name)[0])
    return out


# ------------------------------------------------------------------
# Tokenization
# ------------------------------------------------------------------

LABEL_RE = re.compile(r'^(\s*)label\s+(\w+)\s*(\([^)]*\))?\s*:\s*$')
SCENE_RE = re.compile(r'^(\s*)scene\b')
SHOW_RE = re.compile(r'^(\s*)show\s+(\w+)(?:\s+(.*))?$')
HIDE_RE = re.compile(r'^(\s*)hide\s+(\w+)')
HIDE_ALL_RE = re.compile(r'^(\s*)\$\s*hide_all_chars\s*\((.*)\)')
COMMENT_RE = re.compile(r'^\s*#')
EMPTY_RE = re.compile(r'^\s*$')
DIALOGUE_RE = re.compile(r'^(\s*)(\w+)\s+"((?:[^"\\]|\\.)*)"(\s+.*)?$')

# Branching constructs
IF_RE = re.compile(r'^(\s*)if\s+.*:\s*(#.*)?$')
ELIF_RE = re.compile(r'^(\s*)elif\s+.*:\s*(#.*)?$')
ELSE_RE = re.compile(r'^(\s*)else\s*:\s*(#.*)?$')
MENU_RE = re.compile(r'^(\s*)menu\s*(\w+)?\s*:\s*(#.*)?$')
# Menu option: inside menu block, `"label":` or `"label" (condition):`
MENU_OPT_RE = re.compile(r'^(\s*)"((?:[^"\\]|\\.)*)"(\s*\([^)]*\))?\s*:\s*(#.*)?$')

LEADING_WS_RE = re.compile(r'^(\s*)')


def indent_of(line):
    return len(LEADING_WS_RE.match(line).group(1))


# ------------------------------------------------------------------
# Scanner with indent-aware branch handling
# ------------------------------------------------------------------

class State:
    def __init__(self):
        self.active = set()

    def copy(self):
        s = State()
        s.active = set(self.active)
        return s


def scan_file(path, char_map):
    findings = []
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    current_label = None
    tracking = False
    state = State()

    # Stack of open blocks: each entry = {
    #   "indent": indent of block body (deeper than header),
    #   "header_indent": indent of `if`/`menu:`,
    #   "type": "if" or "menu",
    #   "entry_state": State at block header (before any branch),
    #   "branch_exit_states": list of State snapshots at end of each branch
    # }
    block_stack = []

    def close_blocks_up_to(target_indent):
        """Close any open blocks whose body indent is > target_indent."""
        nonlocal state
        while block_stack and block_stack[-1]["indent"] > target_indent:
            blk = block_stack.pop()
            # save the last branch's exit state
            blk["branch_exit_states"].append(state.copy())
            # merge: UNION (conservative — any branch could leave the tag active)
            merged = set()
            for s in blk["branch_exit_states"]:
                merged |= s.active
            # If block didn't have ALL paths covered (e.g., if without else),
            # also union with entry_state (fall-through case).
            if blk["type"] == "if" and not blk.get("has_else"):
                merged |= blk["entry_state"].active
            new_state = State()
            new_state.active = merged
            state = new_state

    for lineno, raw in enumerate(lines, 1):
        line = raw.rstrip("\n")
        if EMPTY_RE.match(line) or COMMENT_RE.match(line):
            continue

        cur_indent = indent_of(line)

        # Close blocks whose body indent is deeper than current line's indent
        close_blocks_up_to(cur_indent)

        # Label
        m = LABEL_RE.match(line)
        if m:
            current_label = m.group(2)
            tracking = False
            state = State()
            block_stack = []
            continue

        # if header
        m = IF_RE.match(line)
        if m:
            header_indent = len(m.group(1))
            # push a new block (body will be deeper)
            blk = {
                "header_indent": header_indent,
                "indent": header_indent + 1,  # placeholder; will adjust on first body line
                "type": "if",
                "entry_state": state.copy(),
                "branch_exit_states": [],
                "has_else": False,
                "header_line": lineno,
            }
            block_stack.append(blk)
            continue

        # elif header (same indent as original if)
        m = ELIF_RE.match(line)
        if m:
            # record exit state of previous branch, reset state to entry_state
            if block_stack and block_stack[-1]["type"] == "if" and block_stack[-1]["header_indent"] == len(m.group(1)):
                block_stack[-1]["branch_exit_states"].append(state.copy())
                state = block_stack[-1]["entry_state"].copy()
            continue

        # else:
        m = ELSE_RE.match(line)
        if m:
            if block_stack and block_stack[-1]["type"] == "if" and block_stack[-1]["header_indent"] == len(m.group(1)):
                block_stack[-1]["branch_exit_states"].append(state.copy())
                state = block_stack[-1]["entry_state"].copy()
                block_stack[-1]["has_else"] = True
            continue

        # menu:
        m = MENU_RE.match(line)
        if m:
            header_indent = len(m.group(1))
            blk = {
                "header_indent": header_indent,
                "indent": header_indent + 1,
                "type": "menu",
                "entry_state": state.copy(),
                "branch_exit_states": [],
                "has_else": True,  # menus are exhaustive on user choice; but not guaranteed to execute if jumped past
                "header_line": lineno,
            }
            block_stack.append(blk)
            continue

        # menu option: at indent deeper than menu header
        m = MENU_OPT_RE.match(line)
        if m and block_stack and block_stack[-1]["type"] == "menu":
            opt_indent = len(m.group(1))
            # menu options are at menu_header_indent + 4 typically
            if opt_indent > block_stack[-1]["header_indent"]:
                # This is a menu option boundary.
                # The first option: just reset state
                # Subsequent options: save previous branch's exit state, reset
                if block_stack[-1]["branch_exit_states"] or not _is_first_option(block_stack[-1], state):
                    block_stack[-1]["branch_exit_states"].append(state.copy())
                state = block_stack[-1]["entry_state"].copy()
                # Track option indent
                block_stack[-1]["indent"] = opt_indent  # body is deeper than this
                continue

        # scene
        if SCENE_RE.match(line):
            tracking = True
            state.active = set()
            continue

        # hide_all_chars
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

        # show
        m = SHOW_RE.match(line)
        if m:
            tag = m.group(2)
            if tag == "screen" or tag == "black" or tag.startswith("bg"):
                continue
            tracking = True
            state.active.add(tag)
            continue

        # hide
        m = HIDE_RE.match(line)
        if m:
            tag = m.group(2)
            if tag == "screen":
                continue
            tracking = True
            state.active.discard(tag)
            continue

        # dialogue
        m = DIALOGUE_RE.match(line)
        if not m:
            continue
        speaker = m.group(2)
        text = m.group(3)

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
            findings.append({
                "file": os.path.basename(path),
                "line": lineno,
                "label": current_label,
                "speaker": speaker,
                "expected_tag": "player_*_img",
                "text": text[:80],
            })
            continue

        expected_tag = expected_img + "_img"
        if expected_tag not in state.active:
            findings.append({
                "file": os.path.basename(path),
                "line": lineno,
                "label": current_label,
                "speaker": speaker,
                "expected_tag": expected_tag,
                "text": text[:80],
            })

    return findings


def _is_first_option(blk, current_state):
    # If no branch exit states yet AND current state equals entry state, it's first option
    return not blk["branch_exit_states"] and current_state.active == blk["entry_state"].active


# ------------------------------------------------------------------
# main
# ------------------------------------------------------------------

def main():
    char_map = collect_character_defs()
    portrait_files = list_portrait_files()

    all_findings = []
    for fname in sorted(os.listdir(GAME_DIR)):
        if not fname.endswith(".rpy") or fname.endswith(".bak"):
            continue
        path = os.path.join(GAME_DIR, fname)
        findings = scan_file(path, char_map)
        all_findings.extend(findings)

    class_a, class_b = [], []
    for f in all_findings:
        expected = f["expected_tag"]
        base = "player_char" if "player_*" in expected else (expected[:-4] if expected.endswith("_img") else expected)
        has_file = base in portrait_files
        f["has_file"] = has_file
        (class_a if has_file else class_b).append(f)

    print(f"=== Total findings: {len(all_findings)} ===")
    print(f"Class A (has portrait file, missing show): {len(class_a)}")
    print(f"Class B (no portrait file):                {len(class_b)}")
    print()
    char_summary = {}
    for f in all_findings:
        char_summary[f["speaker"]] = char_summary.get(f["speaker"], 0) + 1
    print("=== By speaker ===")
    for k, v in sorted(char_summary.items(), key=lambda x: -x[1]):
        print(f"  {k}: {v}")

    file_summary = {}
    for f in all_findings:
        file_summary[f["file"]] = file_summary.get(f["file"], 0) + 1
    print("\n=== By file ===")
    for k, v in sorted(file_summary.items(), key=lambda x: -x[1]):
        print(f"  {k}: {v}")

    # Group class_a by file + label for easier fixing
    from collections import defaultdict
    grouped = defaultdict(list)
    for item in class_a:
        grouped[(item["file"], item["label"])].append(item)

    with open(os.path.join(os.path.dirname(__file__), "missing_portraits_A.txt"), "w", encoding="utf-8") as f:
        f.write(f"A类 — 有立绘文件但缺show指令 ({len(class_a)}处)\n")
        f.write("按文件+label分组, 同一label内相邻行通常是同一个menu分支遗漏\n")
        f.write("=" * 70 + "\n\n")
        for (file, label), items in sorted(grouped.items()):
            f.write(f"## {file} · label: {label}  ({len(items)}处)\n")
            for item in items:
                f.write(f"  L{item['line']:<5} {item['speaker']} 需要 {item['expected_tag']}\n")
                f.write(f"         > {item['text']}\n")
            f.write("\n")

    with open(os.path.join(os.path.dirname(__file__), "missing_portraits_B.txt"), "w", encoding="utf-8") as f:
        f.write(f"B类 — 没有立绘文件 ({len(class_b)}处)\n")
        f.write("=" * 70 + "\n")
        for item in class_b:
            f.write(f"{item['file']}:{item['line']}  [label: {item['label']}]  {item['speaker']} ({item['expected_tag']})\n")
            f.write(f"    > {item['text']}\n")

    with open(os.path.join(os.path.dirname(__file__), "missing_portraits_full.json"), "w", encoding="utf-8") as f:
        json.dump({
            "char_map": {k: {"image_tag": v[0], "src": f"{v[1]}:{v[2]}"} for k, v in char_map.items()},
            "class_a": class_a,
            "class_b": class_b,
        }, f, ensure_ascii=False, indent=2)

    print("\nReports: missing_portraits_A.txt, missing_portraits_B.txt, missing_portraits_full.json")



def check_char_img_registry():
    """静态闸门(2026-07-24 英格丽残留事故后加): 凡在剧本里被 show 的 *_img,
    必须出现在 char_helpers.rpy 的 CHAR_IMG_TAGS 里 —— 否则 hide_all_chars 清不掉它,
    立绘会一路残留到下一次 scene 切换(玩家可见)。注释行不算。"""
    import re
    ch = open(os.path.join(GAME_DIR, "char_helpers.rpy"), encoding="utf-8").read()
    m = re.search(r"CHAR_IMG_TAGS = \[(.*?)\]", ch, re.S)
    registered = set(re.findall(r'"(\w+_img)"', m.group(1)))
    bad = []
    for fname in sorted(os.listdir(GAME_DIR)):
        if not fname.endswith(".rpy"):
            continue
        for i, line in enumerate(open(os.path.join(GAME_DIR, fname), encoding="utf-8"), 1):
            if line.strip().startswith("#"):
                continue
            for tag in re.findall(r"show (\w+_img)", line):
                if tag not in registered:
                    bad.append((fname, i, tag))
    if bad:
        print()
        print("!! 未注册进 CHAR_IMG_TAGS 却被 show 的立绘 (hide_all_chars 清不掉, 会残留):")
        for f, i, t in bad:
            print("   %s:%d  %s" % (f, i, t))
    else:
        print()
        print("CHAR_IMG_TAGS 注册闸门: 0 处未注册")
    return len(bad)


if __name__ == "__main__":
    main()
    check_char_img_registry()

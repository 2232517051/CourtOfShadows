# Minimal-Constraint Opus Copy Generation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Generate one raw `claude-opus-4-6` draft for the current CourtOfShadows copy update and show it to the user without editing or applying it.

**Architecture:** Run one non-persistent Claude Code print session with all customizations and tools disabled, the model fixed on Opus 4.6, and effort fixed on max. Pass exactly one approved minimal user prompt, validate the returned model envelope, then display the `result` field verbatim without changing project files.

**Tech Stack:** PowerShell, Claude Code 2.1.222, `claude-opus-4-6`

## Global Constraints

- Use `--safe-mode`, `--model claude-opus-4-6`, `--effort max`, `--tools ''`, and `--no-session-persistence` in the actual generation call.
- Send exactly: `请重写《权谋之庭》本次更新涉及的文案：婚约退出与解释、英格丽家庭尾声、人民领主现实化。`
- Do not send project files, old drafts, fact cards, style guidance, examples, forbidden-phrase lists, branch variables, or test contracts.
- Display the returned prose verbatim; do not revise, curate, splice, or apply it to `.rpy` files.
- Do not modify art, music, sound effects, animation, UI, fonts, or game code.

---

### Task 1: Generate and verify the raw Opus draft

**Files:**
- Read: `docs/superpowers/specs/2026-08-05-raw-opus-copy-generation-design.md`
- Modify: none
- Test: Claude Code JSON response envelope and before/after `git status --short`

**Interfaces:**
- Consumes: the exact approved prompt in Global Constraints
- Produces: one JSON response whose `result` string is shown verbatim to the user

- [ ] **Step 1: Record the worktree baseline**

Run:

```powershell
git status --short
```

Expected: the existing six uncommitted update files and this plan file may appear; no raw-Opus output file exists.

- [ ] **Step 2: Run the isolated Opus generation**

Run exactly:

```powershell
$opusPrompt = '请重写《权谋之庭》本次更新涉及的文案：婚约退出与解释、英格丽家庭尾声、人民领主现实化。'
claude --safe-mode --model claude-opus-4-6 --effort max --tools '' --no-session-persistence -p --output-format json $opusPrompt
```

Expected: exit code `0`, `is_error: false`, a non-empty `result`, and `modelUsage` containing `claude-opus-4-6`.

- [ ] **Step 3: Verify the response envelope**

Inspect the captured JSON response and confirm all of the following:

```text
is_error == false
modelUsage contains the exact key claude-opus-4-6
result is a non-empty string
the executed command contains --effort max
```

Expected: all four checks are true. If any check fails, do not display the draft as an Opus 4.6 result and report the failed field.

- [ ] **Step 4: Prove that generation did not touch the project**

Run:

```powershell
git status --short
```

Expected: output is identical to Step 1. No `.rpy`, test, font, asset, configuration, or documentation file changed during generation.

- [ ] **Step 5: Present the raw result**

Return the JSON `result` string exactly as received. Precede it only with the confirmed model and effort. After those two header lines, paste the complete `result` string directly, without delimiters, ellipses, or replacement text.

```text
模型：claude-opus-4-6
effort：max
```

Do not add a quality assessment, canon correction, rewritten alternative, or asset recommendation in this presentation turn.

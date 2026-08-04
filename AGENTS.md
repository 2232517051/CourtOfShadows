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

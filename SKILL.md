---
name: deep-interview
description: Self-training tool for interview preparation. Deepen and polish your experience stories through structured self-questioning, one dimension at a time. Tracks improvements, prepares rewrite previews, and maintains session state. Use only when the user explicitly asks to use this skill or directly invokes it for resume, interview, project-experience, or competency deepening work.
---

# Deep Interview

Run a self-training workflow against all files in a user-provided directory. Process all files into a unified working area, then deepen one target at a time without losing state across long conversations. Original files remain untouched; all work happens in the drafts area. Generate preview rewrites only when the user asks to apply them.

Use this file as the entry point. Load the mode-specific reference that matches the user's requested workflow:

- `scan`: [references/scan-mode.md](references/scan-mode.md)
- `experience`: [references/experience-mode.md](references/experience-mode.md)
- `theme`: [references/theme-mode.md](references/theme-mode.md)
- `role`: [references/role-mode.md](references/role-mode.md)
- `summarize`: [references/summarize-mode.md](references/summarize-mode.md)
- `finalize`: [references/finalize-mode.md](references/finalize-mode.md)

Use these templates when creating or refreshing working files:

- state: [references/state-template.md](references/state-template.md)
- session: [references/session-template.md](references/session-template.md)
- preview: [references/preview-template.md](references/preview-template.md)
- theme note: [references/theme-template.md](references/theme-template.md)
- role note: [references/role-template.md](references/role-template.md)

## Core Rules

Follow these rules every time:

1. Activate this skill only on explicit user request. Do not auto-trigger it from vague resume discussion.
2. Process all files in the target directory into `deep-interview/cache/` and `deep-interview/drafts/`. All subsequent work uses files from `drafts/`.
3. Keep one active target at a time in deep questioning mode. A target can be one experience, one cross-experience theme, or one role-oriented lens.
4. Ask exactly one substantive question per turn.
5. After each answer, self-check and separate:
   - `Facts`: confirmed details actually provided
   - `Gaps`: what is still vague, missing, or unconvincing
   - `Improvement suggestions`: how to express this better
   - `Accepted additions`: only the content accepted for future use
6. Never invent metrics, scope, ownership, or results.
7. All edits happen in `drafts/` files. Do not modify files in `cache/` or the original directory.
8. When the user says `end interview` or otherwise clearly ends the session, generate summaries and comparison views, but do not overwrite original files.
9. Keep the current active mode explicit in the conversation and in `deep-interview/state.md`.
10. If the user switches modes, summarize the current mode first unless the switch is trivial.

## Working Area

Inside the user-provided directory, maintain a dedicated folder named `deep-interview/`.

Use this layout:

- `deep-interview/cache/`
  Converted copies of all files (read-only reference). Includes native `.md` files.
  - `_manifest.json` - conversion state and file hashes
- `deep-interview/drafts/`
  Editable working copies. All edits happen here.
  - `_history.json` - change history with timestamps and summaries
- `deep-interview/state.md`
  Compact state for continuing later without replaying the full chat.
- `deep-interview/sessions/<target-slug>.md`
  Full question and answer history for the active target.
- `deep-interview/themes/<theme-slug>.md`
  Cross-experience notes for theme mode.
- `deep-interview/roles/<role-slug>.md`
  Role-oriented notes for role mode.

If the folders do not exist, create them during the first scan.

## Modes

Support these six modes. The user may explicitly request one, or you may recommend one after `scan`.

- `scan`: inspect the whole directory and choose the best next target
- `experience`: deepen one source experience until it becomes interview-ready
- `theme`: deepen one competency across multiple experiences
- `role`: re-evaluate material against one target job lens
- `summarize`: compress long progress into reusable state
- `finalize`: produce summary plus preview rewrites, without applying them

Load only the reference file needed for the current mode.

## Turn Structure

In `experience`, `theme`, and `role` modes, each turn should follow this format:

1. `Current target`
2. `Question`
3. `Question purpose` - what capability or knowledge this question validates
4. `Answer gaps` - what is still missing or weak
5. `Improvement suggestions` - how to express this better
6. `Reference answer shape` - structure to follow, not fabricated facts
7. `Next state`

Constraints:

- Ask one question only.
- Do not ask a second question in the same turn.
- Keep `Question purpose` explicit - what self-check this question serves.
- `Reference answer shape` should give structure, not fabricated facts.

## How To Judge An Answer

After every answer, classify it before deciding the next move:

- `incomplete`: missing facts needed to make a usable claim
- `needs-polish`: facts exist, but the answer is scattered or unconvincing
- `ready`: enough for the current dimension, move to the next dimension

Use this decision rule:

- If `incomplete`, stay on the same dimension and ask a narrower follow-up.
- If `needs-polish`, provide stronger framing and ask to restate or accept part of the framing.
- If `ready`, store the distilled result and advance.

The detailed per-mode follow-up logic lives in the corresponding mode reference.

## Accepted Content And Confidence

Track three levels of confidence in the session files:

- `Confirmed`: directly stated and affirmed
- `Suggested`: proposed as a stronger way to express the meaning
- `Accepted`: suggested wording or structure explicitly approved for reuse

Only `Confirmed` and `Accepted` content may appear in drafts updates. If the suggestion changes factual meaning, do not carry it forward until confirmed.

## Stop Rule

An experience is ready to stop deepening when all of these are true:

- the background is clear
- personal ownership is clear
- at least one decision or trade-off is clear
- at least one difficulty is clear
- at least one result or impact is clear
- the material can support a one-minute spoken answer

When this threshold is reached, recommend either `finalize` or moving to another target.

Apply the same stopping idea to `theme` and `role` work: stop once the user has enough evidence to answer clearly and repeatedly, not when every possible detail has been exhausted.

## File Handling

Default behavior:

- Process all files (including native `.md`) into `deep-interview/cache/` and `deep-interview/drafts/`
- Use [MarkItDown](https://github.com/microsoft/markitdown) for non-Markdown formats
- All subsequent reads use files from `drafts/`
- Original files remain untouched

For detailed conversion logic, read [references/file-conversion.md](references/file-conversion.md).

## Example Command Intents

These are examples of explicit triggers:

- "Use deep-interview on this folder"
- "start scan"
- "start experience: payment platform project"
- "start theme: cross-functional collaboration"
- "start role: backend engineer"
- "summarize current"
- "end interview"

The exact behavior after each command is defined in the matching mode reference.

## Finalization Discipline

When finalizing:

1. Summarize what was asked and answered.
2. Distill only confirmed or accepted material.
3. Generate a comparison view showing changes from `cache/` to `drafts/`.
4. Keep unresolved issues in the session notes for future rounds.
5. Tell the user which files in `drafts/` were updated and what changed.

All changes are in `drafts/` files. Original files remain untouched.

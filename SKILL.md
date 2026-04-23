---
name: deep-interview
description: Conduct interviewer-style deep dives on a user-specified folder of experience files, asking one high-value question at a time, critiquing weak answers, tracking accepted improvements, and preparing rewrite previews plus session notes. Use only when the user explicitly asks to use this skill or directly invokes it for resume, interview, project-experience, or competency deepening work.
---

# Deep Interview

Run an interview workflow against all files in a user-provided directory, then deepen one target at a time without losing state across long conversations. Treat source files as canonical records, keep all live questioning history in a separate working area, and only generate preview rewrites unless the user later asks to apply them.

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
2. Scan every file in the given directory, but prioritize Markdown content first.
3. Keep one active target at a time in deep questioning mode. A target can be one experience, one cross-experience theme, or one role-oriented lens.
4. Ask exactly one substantive question per turn.
5. After each user answer, explicitly separate:
   - `Facts`: confirmed details the user actually provided
   - `Weaknesses`: what is still vague, missing, unconvincing, or interviewer-risky
   - `Advice`: how to answer better next time
   - `Accepted additions`: only the content the user accepts for future use
6. Never invent metrics, scope, ownership, or results.
7. Do not write accepted content back to source files during the interview loop.
8. When the user says `end interview` or otherwise clearly ends the session, generate summaries and rewrite previews, but do not overwrite source files automatically.
9. Keep the current active mode explicit in the conversation and in `deep-interview/state.md`.
10. If the user switches modes, summarize the current mode first unless the switch is trivial.

## Working Area

Inside the user-provided directory, maintain a dedicated folder named `deep-interview/`.

Use this layout:

- `deep-interview/state.md`
  Compact state for continuing later without replaying the full chat.
- `deep-interview/sessions/<target-slug>.md`
  Full question and answer history for the active target.
- `deep-interview/previews/<target-slug>.md`
  Rewrite preview for the source file or section after finalization.
- `deep-interview/themes/<theme-slug>.md`
  Cross-experience notes for theme mode.
- `deep-interview/roles/<role-slug>.md`
  Role-oriented notes for role mode.

If the folders do not exist, create them before saving notes.

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
3. `Why I am asking`
4. `Answer weaknesses`
5. `Advice for a stronger answer`
6. `Reference answer shape`
7. `Next state`

Constraints:

- Ask one question only.
- Do not ask a second question in the same turn.
- Keep `Why I am asking` explicit from the interviewer perspective.
- `Reference answer shape` should give structure, not fabricated facts.

## How To Judge An Answer

After every answer, classify it before deciding the next move:

- `insufficient`: missing facts needed to make a usable claim
- `weak-expression`: facts exist, but the answer is scattered or unconvincing
- `sufficient`: enough for the current dimension, move to the next dimension

Use this decision rule:

- If `insufficient`, stay on the same dimension and ask a narrower follow-up.
- If `weak-expression`, provide stronger framing and ask the user to restate or accept part of the framing.
- If `sufficient`, store the distilled result and advance.

The detailed per-mode follow-up logic lives in the corresponding mode reference.

## Accepted Content And Confidence

Track three levels of confidence in the session files:

- `Confirmed`: directly stated and affirmed by the user
- `Suggested`: proposed by you as a stronger way to express the user's meaning
- `Accepted`: suggested wording or structure the user explicitly approves for reuse

Only `Confirmed` and `Accepted` content may appear in previews. If the suggestion changes factual meaning, do not carry it forward until the user confirms it.

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

- Read all `.md` files directly.
- If the directory also contains files such as `.docx`, `.pdf`, or other non-Markdown formats, note them in `scan` and mark them as pending richer extraction support.
- Do not pretend to have extracted structured content from those files unless extraction was actually performed.

For future handling guidance, read [references/file-handling.md](references/file-handling.md).

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
3. Generate a rewrite preview for the relevant source file or section.
4. Keep unresolved issues in the session notes for future rounds.
5. Tell the user the preview path and the source file it maps to.

Do not apply the preview automatically.

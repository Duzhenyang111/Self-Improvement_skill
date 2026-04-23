# deep-interview

`deep-interview` is a Claude Code skill for interviewer-style deep dives on a folder of experience materials.

It is designed for resume, interview, project-experience, and competency-deepening workflows. The skill scans user-provided source files, asks one high-value question at a time, critiques weak answers, tracks accepted improvements, and generates rewrite previews without modifying the original source files automatically.

## What this skill does

- Scans a target directory and identifies the best next area to deepen
- Focuses on one active target at a time
- Asks exactly one substantive question per turn
- Separates confirmed facts from weak points and suggested framing
- Tracks accepted additions for future reuse
- Maintains working state across long conversations
- Produces rewrite previews instead of directly overwriting source content

## Supported modes

This skill is organized around six modes:

- `scan`: inspect the whole directory and recommend the best next target
- `experience`: deepen one specific experience until it is interview-ready
- `theme`: deepen one competency across multiple experiences
- `role`: evaluate material through a target job lens
- `summarize`: compress progress into reusable state
- `finalize`: produce summaries and rewrite previews without applying them automatically

## Repository structure

```text
.
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── experience-mode.md
    ├── file-handling.md
    ├── finalize-mode.md
    ├── preview-template.md
    ├── role-mode.md
    ├── role-template.md
    ├── scan-mode.md
    ├── session-template.md
    ├── state-template.md
    ├── summarize-mode.md
    ├── theme-mode.md
    └── theme-template.md
```

## Entry point

The main entry point is:

- `SKILL.md`

It defines:

- activation conditions
- core rules
- working directory layout
- available modes
- turn structure
- answer-quality judgment rules
- finalization behavior

## Working area created during use

When the skill is used on a user-provided directory, it maintains a dedicated working area inside that directory:

```text
deep-interview/
├── state.md
├── sessions/
├── previews/
├── themes/
└── roles/
```

These files are used to preserve interview progress and generated previews without altering the original source files by default.

## Core behavior

Key constraints enforced by the skill:

- Activate only on explicit user request
- Read Markdown files directly and note non-Markdown files separately
- Never invent metrics, ownership, or outcomes
- Keep one active target in deep-questioning mode
- Ask one question only per turn
- Distinguish between confirmed, suggested, and accepted content
- Only confirmed or accepted material may appear in previews
- Do not auto-apply preview rewrites back to source files

## Typical trigger phrases

Examples of explicit trigger intents:

- `Use deep-interview on this folder`
- `start scan`
- `start experience: payment platform project`
- `start theme: cross-functional collaboration`
- `start role: backend engineer`
- `summarize current`
- `end interview`

## Intended use case

This skill is useful when a user has rough project notes, resume bullets, or experience writeups and wants to convert them into stronger interview-ready material through iterative questioning rather than direct rewriting.

## Notes

- Source files are treated as canonical records
- Working notes and previews are kept separately
- Finalization generates rewrite previews, not automatic edits

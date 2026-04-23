# Finalize Mode

Use this mode when the user ends the interview loop for the current target.

## Goal

Close the active target cleanly without polluting the source files.

## Outputs

Produce:

- a session summary
- unresolved questions
- a polished preview rewrite
- a short note about what improved

## Write Targets

- `deep-interview/sessions/<target-slug>.md`
- `deep-interview/previews/<target-slug>.md`
- `deep-interview/state.md`

If the work was theme-based or role-based, also update the matching file under `themes/` or `roles/`.

Use these templates:

- [session-template.md](session-template.md)
- [preview-template.md](preview-template.md)
- [state-template.md](state-template.md)

## Preview Rule

The preview is a candidate rewrite only. Do not modify the original source file automatically.

Include:

- source file path
- section or experience name
- distilled confirmed facts
- accepted phrasing
- unresolved items excluded from the preview

## Final Chat Response

Tell the user:

1. what improved
2. where the preview was written
3. what unresolved gaps remain
4. that the source file is still unchanged

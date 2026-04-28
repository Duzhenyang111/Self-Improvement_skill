# Finalize Mode

Use this mode when the user ends the interview loop for the current target.

## Goal

Close the active target cleanly. All changes are in `drafts/` files. Original files remain untouched.

## Outputs

Produce:

- a session summary
- unresolved questions
- a comparison view showing changes from `cache/` to `drafts/`
- a short note about what improved

## Write Targets

- `deep-interview/sessions/<target-slug>.md` - session record
- `deep-interview/sessions/<target-slug>-comparison.md` - comparison view
- `deep-interview/state.md` - global state

If the work was theme-based or role-based, also update the matching file under `themes/` or `roles/`.

Use these templates:

- [session-template.md](session-template.md)
- [preview-template.md](preview-template.md)
- [state-template.md](state-template.md)

## Comparison View

Generate a comparison between `cache/` (original converted) and `drafts/` (edited version):

```
deep-interview/sessions/<target-slug>-comparison.md
```

The comparison should include:

- Source file mapping
- What changed in each section
- Original text (from cache/) vs current text (from drafts/)
- List of additions, clarifications, and removals

## Final Chat Response

Tell the user:

1. What improved
2. Which files in `drafts/` were updated
3. What unresolved gaps remain
4. That original source files are unchanged
5. Path to the comparison view

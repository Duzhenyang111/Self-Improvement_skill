# Preview Template

Use this template when generating comparison views in `deep-interview/sessions/<target-slug>-comparison.md`.

```md
# Comparison: <target-slug>

## Source Mapping
- original_file:
- cache_file: deep-interview/cache/<filename>.md
- draft_file: deep-interview/drafts/<filename>.md
- generated_at:
- based_on_session:

## What Changed
- 

## Confirmed Facts Used
- 

## Accepted Phrasing Used
- 

## Excluded Items
- unresolved facts:
- unconfirmed suggestions:

## Comparison

### Section: <section-name>

#### Original (from cache)
> 

#### Current (from drafts)
> 

#### Changes
- Added:
- Clarified:
- Removed:

## Apply Notes
- Changes are in `drafts/` files.
- Original source files remain unchanged.
- `cache/` files are read-only reference.
```

## Rules

- Only use confirmed facts and accepted phrasing.
- Do not include speculative metrics or ownership.
- Keep excluded items explicit so the user can decide whether to continue another round.

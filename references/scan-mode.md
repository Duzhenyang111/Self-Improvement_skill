# Scan Mode

Use this mode to inspect every file in the target directory and decide what should be deepened next.

## Goals

- identify files that are rich versus shallow
- find weak sections inside otherwise strong files
- detect repeated claims across files
- recommend the best next target and mode

## Read Order

1. Enumerate every file in the target directory.
2. Read all Markdown files first.
3. Record non-Markdown files and mark whether they were actually parsed.
4. Build a gap map before recommending any target.

## Gap Checks

For each file or section, check for:

- vague descriptions of work
- missing personal ownership
- missing business or project context
- missing decision logic
- missing trade-offs
- missing difficulty, failure, or conflict details
- missing outcomes, metrics, or evidence
- claims that repeat across multiple files without distinct examples

## Output Shape

Return:

1. strongest files or sections
2. weakest files or sections
3. notable repeated themes
4. best next target
5. recommended next mode: `experience`, `theme`, or `role`

## State Update

After scan, update `deep-interview/state.md` with:

- current mode: `scan`
- target directory
- scanned files
- markdown files read
- non-markdown files discovered
- top three gaps
- recommended next target
- recommended next mode

# File Handling

Use this note when the target directory contains files beyond Markdown.

## Current Support

- `.md`: read directly and treat as primary source material.

## Reserved For Future Support

If files such as `.docx`, `.pdf`, `.txt`, or exported images appear, do not ignore them. Record their presence during `scan`, but mark them as one of these states:

- `not-read`: present but not parsed yet
- `text-extracted`: plain text successfully extracted
- `needs-review`: binary or layout-heavy file where extraction may lose context

## Behavior Before Dedicated Readers Exist

1. Mention the file in `scan` output.
2. Explain whether it was actually read or only discovered.
3. Avoid merging unverified content into summaries or previews.
4. Keep the rest of the workflow focused on the files that were actually parsed.

## Future Extension Path

When dedicated readers are later added, keep the same mode system and working area. Only expand the ingestion step:

- `.pdf`: extract text and preserve page references when possible
- `.docx`: extract headings, bullet structure, and paragraph text
- images: use OCR only when the user explicitly wants it

Any future extractor should feed normalized text into the same `scan`, `experience`, `theme`, `role`, `summarize`, and `finalize` flow.

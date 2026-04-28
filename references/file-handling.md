# File Handling

## Overview

All files are processed into a unified workflow with three layers:

- **Original**: User's files remain untouched
- **cache/**: Converted Markdown copies (read-only reference)
- **drafts/**: Editable working copies (where all edits happen)

For detailed conversion logic, see [file-conversion.md](file-conversion.md).

## Supported Formats

### Direct Copy (no conversion needed)

- `.md` - Markdown
- `.txt` - Plain text

### Converted via MarkItDown

- `.pdf` - Portable Document Format
- `.docx` - Microsoft Word
- `.pptx` - Microsoft PowerPoint
- `.xlsx` - Microsoft Excel
- `.html` - Web pages

### Skipped (manual handling required)

- `.jpg`, `.png` - Images (record existence, prompt user to describe)
- Other unsupported formats (record existence, mark as `not-supported`)

## Processing Flow

### First Use

1. Scan target directory for all files
2. Convert non-Markdown files to `deep-interview/cache/`
3. Copy all files (including native `.md`) to `deep-interview/drafts/`
4. Record conversion state in `cache/_manifest.json`
5. All subsequent reads use files from `drafts/`

### Subsequent Use

1. Read `cache/_manifest.json` for existing state
2. Check for new or changed files (hash comparison)
3. Process only new/changed files
4. Sync new files to `drafts/`

## Scan Output

When scanning, report:

- Total files found
- Files copied directly (`.md`, `.txt`)
- Files converted (`.pdf`, `.docx`, `.pptx`, `.xlsx`, `.html`)
- Files skipped (images, unsupported)
- Files failed (conversion errors)

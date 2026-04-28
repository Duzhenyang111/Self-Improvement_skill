# File Conversion

## Overview

All files in the target directory are processed into a unified workflow:

1. **Original files** remain untouched
2. **cache/** contains converted Markdown copies (read-only reference)
3. **drafts/** contains editable working copies (where all edits happen)

Even native `.md` files are copied into `cache/` and `drafts/` for consistency.

## Quick Start

Use the Python scripts in `/scripts` directory:

```bash
# Install dependencies
pip install -r scripts/requirements.txt

# Full scan (convert + sync + status)
python scripts/deep_interview.py scan ~/my-resume

# Or run individual operations
python scripts/deep_interview.py convert ~/my-resume
python scripts/deep_interview.py convert ~/my-resume --incremental
python scripts/deep_interview.py sync ~/my-resume
python scripts/deep_interview.py compare ~/my-resume
python scripts/deep_interview.py status ~/my-resume
```

## Conversion Tool

Use [MarkItDown](https://github.com/microsoft/markitdown) for file conversion.

### Installation Check

On first use, check if installed:

```bash
pip show markitdown
```

If not installed, prompt user:

```bash
pip install 'markitdown[all]'
```

## Directory Structure

```
<target-directory>/
│
├── resume.pdf              # Original files (untouched)
├── portfolio.docx
├── projects.md
│
└── deep-interview/         # Working area (auto-created)
    │
    ├── cache/              # Converted copies (read-only reference)
    │   ├── _manifest.json  # Conversion manifest
    │   ├── resume.pdf.md
    │   ├── portfolio.docx.md
    │   └── projects.md     # Native .md also copied here
    │
    ├── drafts/             # Editable working copies
    │   ├── _history.json   # Change history
    │   ├── resume.pdf.md
    │   ├── portfolio.docx.md
    │   └── projects.md
    │
    └── (other working files)
```

## Manifest File

`cache/_manifest.json` tracks conversion state:

```json
{
  "version": "1.0",
  "created_at": "2026-04-28T10:00:00Z",
  "last_updated": "2026-04-28T10:30:00Z",
  "source_dir": "/path/to/target",
  "files": {
    "resume.pdf": {
      "status": "converted",
      "converted_at": "2026-04-28T10:00:00Z",
      "source_hash": "abc123",
      "output_path": "cache/resume.pdf.md",
      "type": "pdf"
    },
    "projects.md": {
      "status": "copied",
      "copied_at": "2026-04-28T10:00:00Z",
      "source_hash": "xyz789",
      "output_path": "cache/projects.md",
      "type": "md"
    },
    "diagram.png": {
      "status": "skipped",
      "reason": "image format, needs manual description"
    }
  }
}
```

## History File

`drafts/_history.json` tracks edits:

```json
{
  "entries": [
    {
      "timestamp": "2026-04-28T10:30:00Z",
      "session_id": "session-001",
      "file": "resume.pdf.md",
      "changes_summary": "Added personal contribution and metrics for payment platform project",
      "sections_modified": ["Experience.Payment Platform"]
    }
  ]
}
```

## Conversion Flow

### First Scan

1. Check if `deep-interview/cache/_manifest.json` exists
2. If not, create `deep-interview/cache/` and `deep-interview/drafts/`
3. Iterate all files in target directory
4. For each file:
   - Calculate file hash (for change detection)
   - Check if already in manifest with matching hash
   - If not converted or hash changed, process the file
   - Update manifest
5. Copy all `cache/` files to `drafts/` (if drafts is empty)
6. Return conversion summary

### File Processing Rules

| Type | Action |
|------|--------|
| `.md`, `.txt` | Copy directly to `cache/` |
| `.pdf` | `markitdown file.pdf > cache/file.pdf.md` |
| `.docx` | `markitdown file.docx > cache/file.docx.md` |
| `.pptx` | `markitdown file.pptx > cache/file.pptx.md` |
| `.xlsx` | `markitdown file.xlsx > cache/file.xlsx.md` |
| `.html` | `markitdown file.html > cache/file.html.md` |
| `.jpg`, `.png` | Skip, record in manifest as `skipped` |
| Other | Skip, record in manifest as `unsupported` |

### Incremental Scan

1. Read existing `deep-interview/cache/_manifest.json`
2. Iterate all files in target directory
3. Compare hash to identify:
   - New files: not in manifest
   - Changed files: hash mismatch
   - Deleted files: in manifest but source gone
4. Process only new and changed files
5. Update manifest
6. Sync new files to `drafts/`

## Quality Check

After conversion, verify:

1. Output file is not empty
2. Text length is reasonable (not drastically shorter than source)
3. Structure markers (headings, lists) exist

If quality is poor, mark as `needs-manual-review` in manifest.

## Error Handling

- Conversion failed: record error, mark as `failed` in manifest
- Corrupted file: record in manifest, continue with other files
- Insufficient disk space: prompt user to clean up and retry

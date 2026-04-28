# Scan Mode

Use this mode to inspect every file in the target directory and decide what should be deepened next.

## Goals

- Process all files into unified working area
- Identify files that are rich versus shallow
- Find weak sections inside otherwise strong files
- Detect repeated claims across files
- Recommend the best next target and mode

## Flow

### 1. File Discovery

1. Enumerate every file in the target directory
2. Classify by type:
   - Native (`.md`, `.txt`) - copy directly
   - Convertible (`.pdf`, `.docx`, `.pptx`, `.xlsx`, `.html`) - convert via MarkItDown
   - Skipped (images, other) - record existence only

### 2. File Processing

1. Check if `deep-interview/cache/_manifest.json` exists
2. If not, create directory structure:
   - `deep-interview/cache/`
   - `deep-interview/drafts/`
3. For each file, compare hash with manifest:
   - New file: not in manifest
   - Changed file: hash mismatch
   - Unchanged: skip
4. Process new/changed files:
   - Native files: copy to `cache/`
   - Convertible files: run `markitdown` and save to `cache/`
5. Sync `cache/` to `drafts/` (only new files)
6. Update `_manifest.json`

### 3. Content Analysis

Analyze all files in `drafts/`:

- Identify strongest files or sections
- Identify weakest files or sections
- Find repeated themes across files
- Detect missing key information:
  - Vague descriptions of work
  - Missing personal ownership
  - Missing business or project context
  - Missing decision logic
  - Missing trade-offs
  - Missing difficulty, failure, or conflict details
  - Missing outcomes, metrics, or evidence
  - Claims that repeat across multiple files without distinct examples

### 4. Output

Return:

1. Strongest files or sections
2. Weakest files or sections
3. Notable repeated themes
4. Best next target
5. Recommended next mode: `experience`, `theme`, or `role`

### 5. State Update

After scan, update `deep-interview/state.md` with:

- current_mode: `scan`
- target_directory
- scanned_files
- file_summary:
  - total_files
  - copied_files (native .md/.txt)
  - converted_files (via MarkItDown)
  - skipped_files (images, unsupported)
  - failed_files (conversion errors)
- top_three_gaps
- recommended_next_target
- recommended_next_mode

## Read Order

When analyzing content, read from `drafts/` directory:

1. All `.md` files in `drafts/`
2. Use `cache/` only for comparison when needed

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

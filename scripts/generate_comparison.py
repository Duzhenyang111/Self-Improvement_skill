#!/usr/bin/env python3
"""
Generate comparison view between cache/ and drafts/ files.

Usage:
    python generate_comparison.py <target_directory> [--output <output_file>]
"""

import argparse
import difflib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path


def read_file(filepath: str) -> str:
    """Read file content."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"[Error reading file: {str(e)}]"


def get_section_name(filename: str) -> str:
    """Extract section name from filename."""
    # Remove .md extension and clean up
    name = filename
    if name.endswith('.md'):
        name = name[:-3]
    # Remove conversion suffix like .pdf, .docx
    for ext in ['.pdf', '.docx', '.pptx', '.xlsx', '.html', '.htm']:
        if name.endswith(ext):
            name = name[:-len(ext)]
    return name


def generate_diff_summary(old_lines: list, new_lines: list) -> dict:
    """Generate summary of differences."""
    differ = difflib.unified_diff(old_lines, new_lines, lineterm='')
    diff_lines = list(differ)

    additions = sum(1 for line in diff_lines if line.startswith('+') and not line.startswith('+++'))
    deletions = sum(1 for line in diff_lines if line.startswith('-') and not line.startswith('---'))

    return {
        'additions': additions,
        'deletions': deletions,
        'changed': additions > 0 or deletions > 0
    }


def generate_comparison(target_dir: str, output_file: str = None) -> str:
    """Generate comparison view."""
    target_path = Path(target_dir).resolve()
    deep_interview_dir = target_path / 'deep-interview'
    cache_dir = deep_interview_dir / 'cache'
    drafts_dir = deep_interview_dir / 'drafts'

    if not cache_dir.exists():
        return "Error: cache/ directory not found"
    if not drafts_dir.exists():
        return "Error: drafts/ directory not found"

    # Find common files
    cache_files = set()
    for item in cache_dir.iterdir():
        if item.is_file() and item.name != '_manifest.json':
            cache_files.add(item.name)

    drafts_files = set()
    for item in drafts_dir.iterdir():
        if item.is_file() and item.name != '_manifest.json':
            drafts_files.add(item.name)

    common_files = cache_files & drafts_files
    only_in_cache = cache_files - drafts_files
    only_in_drafts = drafts_files - cache_files

    # Generate report
    lines = []
    lines.append("# Comparison Report")
    lines.append("")
    lines.append(f"Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}")
    lines.append(f"Source: {target_path}")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Files compared: {len(common_files)}")
    lines.append(f"- Only in cache/: {len(only_in_cache)}")
    lines.append(f"- Only in drafts/: {len(only_in_drafts)}")
    lines.append("")

    if only_in_cache:
        lines.append("### Files only in cache/")
        for f in sorted(only_in_cache):
            lines.append(f"- {f}")
        lines.append("")

    if only_in_drafts:
        lines.append("### Files only in drafts/")
        for f in sorted(only_in_drafts):
            lines.append(f"- {f}")
        lines.append("")

    # Compare each file
    changed_files = []
    unchanged_files = []

    for filename in sorted(common_files):
        cache_path = cache_dir / filename
        drafts_path = drafts_dir / filename

        cache_content = read_file(str(cache_path))
        drafts_content = read_file(str(drafts_path))

        cache_lines = cache_content.splitlines()
        drafts_lines = drafts_content.splitlines()

        diff_summary = generate_diff_summary(cache_lines, drafts_lines)

        if diff_summary['changed']:
            changed_files.append((filename, diff_summary))
        else:
            unchanged_files.append(filename)

    lines.append("## File Changes")
    lines.append("")

    if changed_files:
        lines.append(f"### Changed Files ({len(changed_files)})")
        lines.append("")
        for filename, summary in changed_files:
            section = get_section_name(filename)
            lines.append(f"#### {section}")
            lines.append(f"- File: `{filename}`")
            lines.append(f"- Additions: +{summary['additions']} lines")
            lines.append(f"- Deletions: -{summary['deletions']} lines")
            lines.append("")
    else:
        lines.append("### No changes detected")
        lines.append("")

    if unchanged_files:
        lines.append(f"### Unchanged Files ({len(unchanged_files)})")
        lines.append("")
        for filename in unchanged_files:
            lines.append(f"- `{filename}`")
        lines.append("")

    # Generate detailed diffs for changed files
    if changed_files:
        lines.append("## Detailed Changes")
        lines.append("")

        for filename, _ in changed_files:
            cache_path = cache_dir / filename
            drafts_path = drafts_dir / filename

            cache_content = read_file(str(cache_path))
            drafts_content = read_file(str(drafts_path))

            cache_lines = cache_content.splitlines()
            drafts_lines = drafts_content.splitlines()

            section = get_section_name(filename)
            lines.append(f"### {section}")
            lines.append("")
            lines.append("```diff")
            differ = difflib.unified_diff(
                cache_lines, drafts_lines,
                fromfile=f'cache/{filename}',
                tofile=f'drafts/{filename}',
                lineterm=''
            )
            for line in differ:
                lines.append(line)
            lines.append("```")
            lines.append("")

    report = '\n'.join(lines)

    # Save to file if specified
    if output_file:
        os.makedirs(os.path.dirname(output_file) if os.path.dirname(output_file) else '.', exist_ok=True)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"Report saved to: {output_file}")

    return report


def main():
    parser = argparse.ArgumentParser(description='Generate comparison view')
    parser.add_argument('target_dir', help='Target directory')
    parser.add_argument('--output', '-o', help='Output file path')
    args = parser.parse_args()

    if not os.path.isdir(args.target_dir):
        print(f"Error: {args.target_dir} is not a directory")
        sys.exit(1)

    # Default output path
    output_file = args.output
    if not output_file:
        target_path = Path(args.target_dir).resolve()
        timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
        output_file = str(target_path / 'deep-interview' / 'sessions' / f'comparison-{timestamp}.md')

    print(f"Generating comparison for: {args.target_dir}")
    print()

    report = generate_comparison(args.target_dir, output_file)

    # Print summary to stdout
    lines = report.split('\n')
    for line in lines[:50]:  # Print first 50 lines
        print(line)
    if len(lines) > 50:
        print(f"... ({len(lines) - 50} more lines)")


if __name__ == '__main__':
    main()

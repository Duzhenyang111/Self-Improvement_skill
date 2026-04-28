#!/usr/bin/env python3
"""
Deep Interview - Main entry point for file operations.

Usage:
    python deep_interview.py scan <target_dir>
    python deep_interview.py convert <target_dir> [--incremental]
    python deep_interview.py sync <target_dir>
    python deep_interview.py compare <target_dir> [--output <file>]
    python deep_interview.py status <target_dir>
"""

import argparse
import json
import os
import sys
from pathlib import Path


def cmd_scan(target_dir: str):
    """Full scan: convert + sync + status."""
    print("=" * 60)
    print("DEEP INTERVIEW - SCAN")
    print("=" * 60)
    print()

    # Step 1: Convert files
    print("[1/3] Converting files...")
    from convert_files import process_files
    stats = process_files(target_dir, incremental=False)
    print()

    # Step 2: Sync cache to drafts
    print("[2/3] Syncing cache/ to drafts/...")
    from sync_cache import sync_cache_to_drafts
    sync_stats = sync_cache_to_drafts(target_dir)
    print()

    # Step 3: Show status
    print("[3/3] Status:")
    cmd_status(target_dir)


def cmd_convert(target_dir: str, incremental: bool = False):
    """Convert files only."""
    from convert_files import process_files
    stats = process_files(target_dir, incremental)


def cmd_sync(target_dir: str):
    """Sync cache to drafts."""
    from sync_cache import sync_cache_to_drafts
    stats = sync_cache_to_drafts(target_dir)


def cmd_compare(target_dir: str, output_file: str = None):
    """Generate comparison view."""
    from generate_comparison import generate_comparison
    report = generate_comparison(target_dir, output_file)


def cmd_status(target_dir: str):
    """Show current status."""
    target_path = Path(target_dir).resolve()
    deep_interview_dir = target_path / 'deep-interview'
    manifest_path = deep_interview_dir / 'cache' / '_manifest.json'

    if not manifest_path.exists():
        print("No deep-interview workspace found. Run 'scan' first.")
        return

    with open(manifest_path, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    files = manifest.get('files', {})

    # Count by status
    status_counts = {}
    for filename, info in files.items():
        status = info.get('status', 'unknown')
        status_counts[status] = status_counts.get(status, 0) + 1

    print(f"Target: {manifest.get('source_dir', 'unknown')}")
    print(f"Last updated: {manifest.get('last_updated', 'unknown')}")
    print()
    print("Files:")
    for status, count in sorted(status_counts.items()):
        print(f"  {status}: {count}")
    print(f"  total: {len(files)}")

    # Check drafts
    drafts_dir = deep_interview_dir / 'drafts'
    if drafts_dir.exists():
        drafts_files = [f for f in drafts_dir.iterdir()
                       if f.is_file() and f.name not in ('_manifest.json', '_history.json')]
        print(f"\nDrafts: {len(drafts_files)} files")

    # Check state
    state_path = deep_interview_dir / 'state.md'
    if state_path.exists():
        print("\nState file exists: deep-interview/state.md")

    # Check sessions
    sessions_dir = deep_interview_dir / 'sessions'
    if sessions_dir.exists():
        session_files = list(sessions_dir.glob('*.md'))
        print(f"Sessions: {len(session_files)} files")


def main():
    parser = argparse.ArgumentParser(
        description='Deep Interview - File operations for interview preparation',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python deep_interview.py scan ~/my-resume
    python deep_interview.py convert ~/my-resume --incremental
    python deep_interview.py sync ~/my-resume
    python deep_interview.py compare ~/my-resume
    python deep_interview.py status ~/my-resume
        """
    )

    subparsers = parser.add_subparsers(dest='command', help='Command to execute')

    # scan command
    scan_parser = subparsers.add_parser('scan', help='Full scan: convert + sync + status')
    scan_parser.add_argument('target_dir', help='Target directory')

    # convert command
    convert_parser = subparsers.add_parser('convert', help='Convert files to Markdown')
    convert_parser.add_argument('target_dir', help='Target directory')
    convert_parser.add_argument('--incremental', action='store_true',
                               help='Only process new/changed files')

    # sync command
    sync_parser = subparsers.add_parser('sync', help='Sync cache/ to drafts/')
    sync_parser.add_argument('target_dir', help='Target directory')

    # compare command
    compare_parser = subparsers.add_parser('compare', help='Generate comparison view')
    compare_parser.add_argument('target_dir', help='Target directory')
    compare_parser.add_argument('--output', '-o', help='Output file path')

    # status command
    status_parser = subparsers.add_parser('status', help='Show current status')
    status_parser.add_argument('target_dir', help='Target directory')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    if not os.path.isdir(args.target_dir):
        print(f"Error: {args.target_dir} is not a directory")
        sys.exit(1)

    if args.command == 'scan':
        cmd_scan(args.target_dir)
    elif args.command == 'convert':
        cmd_convert(args.target_dir, args.incremental)
    elif args.command == 'sync':
        cmd_sync(args.target_dir)
    elif args.command == 'compare':
        cmd_compare(args.target_dir, args.output)
    elif args.command == 'status':
        cmd_status(args.target_dir)


if __name__ == '__main__':
    main()

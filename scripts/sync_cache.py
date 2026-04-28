#!/usr/bin/env python3
"""
Sync new files from cache/ to drafts/.

Usage:
    python sync_cache.py <target_directory>
"""

import argparse
import json
import os
import shutil
import sys
from pathlib import Path


def load_manifest(manifest_path: str) -> dict:
    """Load manifest file."""
    if os.path.exists(manifest_path):
        with open(manifest_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {'files': {}}


def sync_cache_to_drafts(target_dir: str) -> dict:
    """Sync new files from cache/ to drafts/."""
    target_path = Path(target_dir).resolve()
    deep_interview_dir = target_path / 'deep-interview'
    cache_dir = deep_interview_dir / 'cache'
    drafts_dir = deep_interview_dir / 'drafts'

    if not cache_dir.exists():
        print("Error: cache/ directory not found")
        return {'synced': 0, 'skipped': 0}

    drafts_dir.mkdir(parents=True, exist_ok=True)

    stats = {'synced': 0, 'skipped': 0}

    # Get list of files in cache
    cache_files = set()
    for item in cache_dir.iterdir():
        if item.is_file() and item.name != '_manifest.json':
            cache_files.add(item.name)

    # Get list of files in drafts
    drafts_files = set()
    if drafts_dir.exists():
        for item in drafts_dir.iterdir():
            if item.is_file() and item.name != '_manifest.json':
                drafts_files.add(item.name)

    # Sync new files
    new_files = cache_files - drafts_files
    for filename in new_files:
        src = cache_dir / filename
        dst = drafts_dir / filename
        shutil.copy2(str(src), str(dst))
        stats['synced'] += 1
        print(f"  Synced: {filename}")

    # Report unchanged
    existing_files = cache_files & drafts_files
    stats['skipped'] = len(existing_files)

    return stats


def main():
    parser = argparse.ArgumentParser(description='Sync cache to drafts')
    parser.add_argument('target_dir', help='Target directory')
    args = parser.parse_args()

    if not os.path.isdir(args.target_dir):
        print(f"Error: {args.target_dir} is not a directory")
        sys.exit(1)

    print(f"Syncing cache/ to drafts/ in: {args.target_dir}")
    print()

    stats = sync_cache_to_drafts(args.target_dir)

    print()
    print("=" * 50)
    print("Summary:")
    print(f"  Synced: {stats['synced']}")
    print(f"  Already exists: {stats['skipped']}")
    print("=" * 50)


if __name__ == '__main__':
    main()

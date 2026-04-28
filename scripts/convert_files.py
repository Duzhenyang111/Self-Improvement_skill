#!/usr/bin/env python3
"""
File conversion script for deep-interview skill.

Converts files to Markdown using MarkItDown and manages cache/manifest.

Usage:
    python convert_files.py <target_directory> [--incremental]
"""

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


# Supported file types
COPY_EXTENSIONS = {'.md', '.txt'}
CONVERT_EXTENSIONS = {'.pdf', '.docx', '.pptx', '.xlsx', '.html', '.htm'}
SKIP_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.ico'}


def calculate_hash(filepath: str) -> str:
    """Calculate SHA256 hash of a file."""
    sha256 = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            sha256.update(chunk)
    return sha256.hexdigest()[:16]


def get_file_type(filepath: str) -> str:
    """Get file type category."""
    ext = Path(filepath).suffix.lower()
    if ext in COPY_EXTENSIONS:
        return 'native'
    elif ext in CONVERT_EXTENSIONS:
        return 'convertible'
    elif ext in SKIP_EXTENSIONS:
        return 'skip'
    else:
        return 'unsupported'


def convert_with_markitdown(input_path: str, output_path: str) -> bool:
    """Convert file using MarkItDown CLI."""
    try:
        result = subprocess.run(
            ['markitdown', input_path],
            capture_output=True,
            text=True,
            timeout=60
        )
        if result.returncode == 0 and result.stdout.strip():
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(result.stdout)
            return True
        else:
            print(f"  Warning: MarkItDown returned empty or error for {input_path}")
            if result.stderr:
                print(f"  Error: {result.stderr.strip()}")
            return False
    except subprocess.TimeoutExpired:
        print(f"  Error: Conversion timed out for {input_path}")
        return False
    except FileNotFoundError:
        print("  Error: markitdown not found. Install with: pip install 'markitdown[all]'")
        return False
    except Exception as e:
        print(f"  Error: {str(e)}")
        return False


def load_manifest(manifest_path: str) -> dict:
    """Load manifest file or create default."""
    if os.path.exists(manifest_path):
        with open(manifest_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {
        'version': '1.0',
        'created_at': datetime.now(timezone.utc).isoformat(),
        'last_updated': datetime.now(timezone.utc).isoformat(),
        'source_dir': '',
        'files': {}
    }


def save_manifest(manifest_path: str, manifest: dict):
    """Save manifest file."""
    manifest['last_updated'] = datetime.now(timezone.utc).isoformat()
    os.makedirs(os.path.dirname(manifest_path), exist_ok=True)
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)


def process_files(target_dir: str, incremental: bool = False) -> dict:
    """Process all files in target directory."""
    target_path = Path(target_dir).resolve()
    deep_interview_dir = target_path / 'deep-interview'
    cache_dir = deep_interview_dir / 'cache'
    drafts_dir = deep_interview_dir / 'drafts'
    manifest_path = cache_dir / '_manifest.json'

    # Create directories
    cache_dir.mkdir(parents=True, exist_ok=True)
    drafts_dir.mkdir(parents=True, exist_ok=True)

    # Load manifest
    manifest = load_manifest(str(manifest_path))
    manifest['source_dir'] = str(target_path)

    # Stats
    stats = {
        'total': 0,
        'copied': 0,
        'converted': 0,
        'skipped': 0,
        'failed': 0,
        'unchanged': 0
    }

    # Process each file
    for item in target_path.iterdir():
        if item.is_dir():
            continue
        if item.name.startswith('.'):
            continue
        if item.name == 'deep-interview':
            continue

        stats['total'] += 1
        filename = item.name
        file_hash = calculate_hash(str(item))
        file_type = get_file_type(str(item))

        # Check if unchanged
        if incremental and filename in manifest['files']:
            existing = manifest['files'][filename]
            if existing.get('source_hash') == file_hash:
                stats['unchanged'] += 1
                continue

        # Process based on type
        if file_type == 'native':
            # Copy .md and .txt files
            output_name = filename
            cache_output = cache_dir / output_name
            drafts_output = drafts_dir / output_name

            shutil.copy2(str(item), str(cache_output))
            shutil.copy2(str(item), str(drafts_output))

            manifest['files'][filename] = {
                'status': 'copied',
                'copied_at': datetime.now(timezone.utc).isoformat(),
                'source_hash': file_hash,
                'output_path': f'cache/{output_name}',
                'type': item.suffix.lower()
            }
            stats['copied'] += 1
            print(f"  Copied: {filename}")

        elif file_type == 'convertible':
            # Convert using MarkItDown
            output_name = f"{filename}.md"
            cache_output = cache_dir / output_name

            print(f"  Converting: {filename}...")
            if convert_with_markitdown(str(item), str(cache_output)):
                # Copy to drafts
                drafts_output = drafts_dir / output_name
                shutil.copy2(str(cache_output), str(drafts_output))

                manifest['files'][filename] = {
                    'status': 'converted',
                    'converted_at': datetime.now(timezone.utc).isoformat(),
                    'source_hash': file_hash,
                    'output_path': f'cache/{output_name}',
                    'type': item.suffix.lower()
                }
                stats['converted'] += 1
                print(f"  Converted: {filename} -> {output_name}")
            else:
                manifest['files'][filename] = {
                    'status': 'failed',
                    'failed_at': datetime.now(timezone.utc).isoformat(),
                    'source_hash': file_hash,
                    'error': 'Conversion failed',
                    'type': item.suffix.lower()
                }
                stats['failed'] += 1

        elif file_type == 'skip':
            manifest['files'][filename] = {
                'status': 'skipped',
                'reason': f'{item.suffix.lower()} format, needs manual description',
                'source_hash': file_hash,
                'type': item.suffix.lower()
            }
            stats['skipped'] += 1
            print(f"  Skipped: {filename} (image/unsupported)")

        else:
            manifest['files'][filename] = {
                'status': 'unsupported',
                'reason': f'{item.suffix.lower()} format not supported',
                'source_hash': file_hash,
                'type': item.suffix.lower()
            }
            stats['skipped'] += 1
            print(f"  Skipped: {filename} (unsupported format)")

    # Save manifest
    save_manifest(str(manifest_path), manifest)

    # Also save manifest to drafts for reference
    shutil.copy2(str(manifest_path), str(drafts_dir / '_manifest.json'))

    return stats


def main():
    parser = argparse.ArgumentParser(description='Convert files for deep-interview')
    parser.add_argument('target_dir', help='Target directory containing files')
    parser.add_argument('--incremental', action='store_true',
                       help='Only process new/changed files')
    args = parser.parse_args()

    if not os.path.isdir(args.target_dir):
        print(f"Error: {args.target_dir} is not a directory")
        sys.exit(1)

    print(f"Processing files in: {args.target_dir}")
    print(f"Mode: {'incremental' if args.incremental else 'full'}")
    print()

    stats = process_files(args.target_dir, args.incremental)

    print()
    print("=" * 50)
    print("Summary:")
    print(f"  Total files: {stats['total']}")
    print(f"  Copied (native): {stats['copied']}")
    print(f"  Converted: {stats['converted']}")
    print(f"  Skipped: {stats['skipped']}")
    print(f"  Failed: {stats['failed']}")
    print(f"  Unchanged: {stats['unchanged']}")
    print("=" * 50)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Validate that all chapter files have proper Jekyll front matter.
This prevents GitHub Pages rendering issues.
"""

import sys
import io
import re
from pathlib import Path
from typing import List, Tuple

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def validate_chapter_frontmatter(chapter_file: Path) -> Tuple[bool, str]:
    """
    Check if a chapter file has valid Jekyll front matter.

    Returns:
        (is_valid, error_message)
    """
    content = chapter_file.read_text(encoding='utf-8')

    # Check if file starts with front matter
    if not content.startswith('---\n'):
        return False, "Missing YAML front matter (must start with '---')"

    # Extract front matter
    match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not match:
        return False, "Invalid YAML front matter format"

    frontmatter = match.group(1)

    # Check required fields
    if 'layout:' not in frontmatter:
        return False, "Missing 'layout:' field in front matter"

    if 'layout: chapter' not in frontmatter:
        return False, "Front matter must have 'layout: chapter'"

    if 'title:' not in frontmatter:
        return False, "Missing 'title:' field in front matter"

    # Extract title to validate format
    title_match = re.search(r'title:\s*"(.+?)"', frontmatter)
    if not title_match:
        return False, "Title must be quoted (e.g., title: \"Chapter 1: Title\")"

    return True, ""

def main():
    """Validate all chapter files."""

    chapters_dir = Path("chapters")
    if not chapters_dir.exists():
        print("❌ chapters/ directory not found")
        return 1

    # Find all chapter files
    chapter_files = sorted(chapters_dir.glob("chapter-*.md"))
    coda = chapters_dir / "coda.md"
    if coda.exists():
        chapter_files.append(coda)

    if not chapter_files:
        print("⚠️  No chapter files found")
        return 0

    print(f"Validating {len(chapter_files)} chapter files...\n")

    errors: List[Tuple[Path, str]] = []

    for chapter_file in chapter_files:
        is_valid, error_msg = validate_chapter_frontmatter(chapter_file)

        if is_valid:
            print(f"✅ {chapter_file.name}")
        else:
            print(f"❌ {chapter_file.name}: {error_msg}")
            errors.append((chapter_file, error_msg))

    # Summary
    print(f"\n{'='*60}")
    if errors:
        print(f"❌ {len(errors)} file(s) with issues:")
        for file, error in errors:
            print(f"   - {file.name}: {error}")
        print(f"\nFix these issues to ensure GitHub Pages renders chapters properly.")
        return 1
    else:
        print(f"✅ All {len(chapter_files)} chapter files have valid front matter!")
        return 0

if __name__ == "__main__":
    exit(main())

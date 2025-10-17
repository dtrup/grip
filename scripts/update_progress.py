#!/usr/bin/env python3
"""
Standalone script to update BOOK_SUMMARY.md with current chapter states.
Run this directly: python3 scripts/update_progress.py

Does NOT consume Claude Code tokens - runs independently.
"""

import re
import os
from pathlib import Path
from datetime import datetime

def count_words(file_path):
    """Count words in a markdown file, excluding front matter and metadata."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove YAML front matter if present
        content = re.sub(r'^---\s*\n.*?\n---\s*\n', '', content, flags=re.DOTALL)

        # Remove markdown formatting but keep text
        content = re.sub(r'```.*?```', '', content, flags=re.DOTALL)  # Code blocks
        content = re.sub(r'`[^`]+`', '', content)  # Inline code
        content = re.sub(r'!\[.*?\]\(.*?\)', '', content)  # Images
        content = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', content)  # Links
        content = re.sub(r'[#*_~`]', '', content)  # Markdown symbols

        # Count words
        words = content.split()
        return len(words)
    except FileNotFoundError:
        return 0
    except Exception as e:
        print(f"Error counting words in {file_path}: {e}")
        return 0

def get_chapter_status(file_path, word_count):
    """Determine chapter status based on word count and markers."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for explicit status markers
        if 'status: complete' in content.lower() or '✅ Complete' in content:
            return '✅ Complete'
        elif '🔍 Revised' in content or word_count >= 3000:
            return '🔍 Revised'
        elif word_count >= 1000:
            return '✍️ Drafted'
        elif word_count >= 100:
            return '📋 Outlined'

        # Check if brainstorm exists
        brainstorm_path = file_path.replace('chapters/', 'brainstorms/').replace('.md', '-brainstorm.md')
        if os.path.exists(brainstorm_path):
            return '🧠 Brainstormed'

        return '⬜ Not Started'
    except:
        return '⬜ Not Started'

def update_book_summary():
    """Update BOOK_SUMMARY.md with latest chapter progress."""
    project_root = Path(__file__).parent.parent
    summary_file = project_root / 'BOOK_SUMMARY.md'

    if not summary_file.exists():
        print("❌ BOOK_SUMMARY.md not found")
        return

    # Scan all chapters
    chapters = []
    total_words = 0
    status_counts = {
        '✅ Complete': 0,
        '🔍 Revised': 0,
        '✍️ Drafted': 0,
        '📋 Outlined': 0,
        '🧠 Brainstormed': 0,
        '⬜ Not Started': 0
    }

    for i in range(1, 21):
        chapter_file = project_root / f'chapters/chapter-{i:02d}.md'
        if chapter_file.exists():
            word_count = count_words(chapter_file)
            status = get_chapter_status(chapter_file, word_count)
            chapters.append((i, word_count, status))
            total_words += word_count
            status_counts[status] += 1
        else:
            chapters.append((i, 0, '⬜ Not Started'))
            status_counts['⬜ Not Started'] += 1

    # Check Coda
    coda_file = project_root / 'chapters/coda.md'
    if coda_file.exists():
        word_count = count_words(coda_file)
        status = get_chapter_status(coda_file, word_count)
        chapters.append(('Coda', word_count, status))
        total_words += word_count
        status_counts[status] += 1

    # Read current summary
    try:
        with open(summary_file, 'r', encoding='utf-8') as f:
            summary_content = f.read()
    except Exception as e:
        print(f"❌ Error reading BOOK_SUMMARY.md: {e}")
        return

    # Update chapter rows
    timestamp = datetime.now().strftime('%Y-%m-%d')
    updated_content = summary_content

    for ch_num, words, status in chapters:
        if ch_num == 'Coda':
            pattern = r'\|\s*Coda\s*\|([^|]+)\|[^|]*\|[^|]*\|[^|]*\|'
            def replace_coda(match):
                title = match.group(1).strip()
                return f'| Coda | {title} | {status} | {words:,} | {timestamp} |'
            updated_content = re.sub(pattern, replace_coda, updated_content)
        else:
            pattern = rf'\|\s*{ch_num:02d}\s*\|([^|]+)\|[^|]*\|[^|]*\|[^|]*\|'
            def replace_row(match):
                title = match.group(1).strip()
                return f'| {ch_num:02d} | {title} | {status} | {words:,} | {timestamp} |'
            updated_content = re.sub(pattern, replace_row, updated_content)

    # Update overall stats
    completed = status_counts['✅ Complete']
    in_progress = sum(status_counts[s] for s in ['🔍 Revised', '✍️ Drafted', '📋 Outlined', '🧠 Brainstormed'])
    not_started = status_counts['⬜ Not Started']
    progress_pct = (completed / 21) * 100

    # Update stats section
    stats_pattern = r'(### Overall Stats.*?)\*\*Total Chapters\*\*: \d+.*?\n\*\*Completed\*\*: \d+.*?\n\*\*In Progress\*\*: \d+.*?\n\*\*Not Started\*\*: \d+.*?\n\*\*Current Word Count\*\*: [\d,]+.*?[\d.]+%\)'

    def replace_stats(match):
        return f'''{match.group(1)}**Total Chapters**: 21 (20 chapters + Coda)
**Completed**: {completed} ({progress_pct:.1f}%)
**In Progress**: {in_progress}
**Not Started**: {not_started}
**Current Word Count**: {total_words:,} / 100,000+ ({(total_words/100000)*100:.1f}%)'''

    updated_content = re.sub(stats_pattern, replace_stats, updated_content, flags=re.DOTALL)

    # Update "Last Updated" at top
    updated_content = re.sub(
        r'> \*\*Last Updated\*\*: \d{4}-\d{2}-\d{2}',
        f'> **Last Updated**: {timestamp}',
        updated_content
    )

    # Write back
    if updated_content != summary_content:
        try:
            with open(summary_file, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"✅ Updated BOOK_SUMMARY.md")
            print(f"\n📊 Progress Summary:")
            print(f"   Total Words: {total_words:,} / 100,000+")
            print(f"   Completed: {completed} / 21 ({progress_pct:.1f}%)")
            print(f"\n📈 Status Breakdown:")
            for status, count in status_counts.items():
                if count > 0:
                    print(f"   {status}: {count}")
        except Exception as e:
            print(f"❌ Error writing BOOK_SUMMARY.md: {e}")
    else:
        print("✅ BOOK_SUMMARY.md already up to date")

if __name__ == '__main__':
    update_book_summary()

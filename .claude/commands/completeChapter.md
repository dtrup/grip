---
description: Finalize chapter and update project progress
allowed-tools: Read, Write, Edit, Bash
---

# Complete Chapter $1: Finalize and Publish

Mark chapter as complete and update all project tracking.

## Your Task

1. **Final quality check**:
   - Read @chapters/chapter-$1.md to verify it's complete
   - Count words and verify meets targets in @book.config.json
   - Check for any [TODO], [RESEARCH], or [REVISE] markers
   - Ensure smooth transitions into and out of chapter

2. **Update progress tracking**:
   - Update chapter status to "✅ Complete" in @chapters/chapter-$1.md
   - Add final word count and completion date  
   - **Add internal chapter navigation** to @chapters/chapter-$1.md:
     - Create "Chapter Navigation" section after chapter title
     - Add clickable links to all major sections (## headings)
     - Group sections logically with brief descriptions
     - Use markdown anchor links for easy jumping between sections
   - Update @BOOK_SUMMARY.md with:
     - Chapter marked as complete
     - Updated word count totals
     - Overall book progress percentage
   - Update @CHAPTER_SUMMARIES.md with:
     - Comprehensive chapter summary (3-4 sentences)
     - Major sections list with brief descriptions for navigation
     - Link to chapter with navigation: `[View Chapter X with Navigation](chapters/chapter-X.md)`
     - Key themes and concepts introduced
     - Important examples or case studies used
     - How chapter transitions to/from adjacent chapters
     - Update quick navigation links at top of file

3. **Update index.md** (main book navigation):
   - Update chapter status from "✅ Drafted" to "✅ Complete"
   - Replace word count target with actual word count
   - Add "⭐ With Navigation" indicator to completed chapters
   - Update Progress section with accurate completed vs drafted counts
   - Update overall progress percentage (completed chapters / total chapters)

4. **Prepare for publication** (if configured):
   - Add hypothesis commenting script to chapter end if github_pages enabled in config
   - Stage files for git if repository exists

5. **Report completion**:
   - Show chapter stats (word count, completion date)
   - Display updated book progress (X of Y chapters, total words)
   - Suggest logical next steps (next chapter to work on, or publication prep if book is complete)

Focus on making this chapter truly publication-ready.
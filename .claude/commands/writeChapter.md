---
description: Write complete chapter content from brainstorm plan
allowed-tools: Task
---

# Write Chapter $1: Delegate to Expert Chapter Writer

This command delegates chapter writing to the **chapter-writer** subagent, a specialized creative writing expert.

## What Happens

The chapter-writer subagent will:

1. **Load minimal necessary context**:
   - Brainstorm plan from @brainstorms/chapter-$1-brainstorm.md
   - Style guide from @style-guide.md
   - Word count targets from @book.config.json
   - Existing chapter from @chapters/chapter-$1.md
   - Continuity from @BOOK_SUMMARY.md (not full prior chapters)

2. **Write with expertise**:
   - Transform brainstorm into polished content
   - Use compelling narrative hooks
   - Deploy researched examples strategically
   - Maintain consistent voice and style
   - Hit word count targets
   - Create smooth transitions

3. **Ensure quality**:
   - Every paragraph advances the argument
   - Examples illuminate, not just decorate
   - Voice matches established style
   - Claims are properly supported
   - Structure works for navigation

4. **Auto-update progress** (via post-tool-use hook):
   - Word count tracked automatically
   - Chapter status updated to "✍️ Drafted"
   - BOOK_SUMMARY.md updated with timestamp

## Your Command

**Delegate to the chapter-writer subagent to write chapter $1.**

The chapter-writer has been trained on your book's specific voice, style guide, and quality standards. It will handle the writing process autonomously while maintaining consistency with your previous chapters.

After writing, consider running `/styleCheck $1` to have the style-editor subagent review for voice consistency.
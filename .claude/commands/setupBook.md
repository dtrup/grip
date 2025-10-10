---
description: Initialize a forked book-base for your specific book project
allowed-tools: Read, Write, Edit
---

# Setup Your Book Project

Customize this forked book-base template for your specific book.

## Your Task

1. **Gather book details** from user:
   - Book title and subtitle
   - Author name  
   - Genre (non-fiction, memoir, technical, etc.)
   - Target word count and chapter count
   - Writing style preference (academic, narrative, conversational, etc.)

2. **Update configuration**:
   - Customize @book.config.json with book details
   - Set realistic word targets per chapter
   - Configure publishing preferences (GitHub Pages, etc.)

3. **Create initial files**:
   - **TOC.md**: Basic table of contents template for user to customize if it is not already there
   - **style-guide.md**: Personalized style guide based on genre and preferences  
   - **BOOK_SUMMARY.md**: Progress tracking template

4. **Verify structure**:
   - Ensure chapters/, brainstorms/, outlines/ directories exist
   - Check that .claude/commands/ has all workflow commands
   - Create .gitignore if repository will be used

5. **Guide next steps**:
   - Explain the workflow: TOC → /tocToChapters → /prepareChapter → /writeChapter → /completeChapter
   - Suggest starting with TOC.md customization if the file is blank
   - Point to key commands they'll use

Transform generic template into personalized book writing system.
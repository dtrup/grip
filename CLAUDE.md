# Book-Base 2.0: AI Writing System

Professional book writing template with **4 specialized subagent experts** and automated progress tracking.

## 🤖 Subagents

1. **chapter-writer** - Creative writing, voice consistency
2. **style-editor** - Editorial review, quality control
3. **research-assistant** - Research, source evaluation, citations
4. **thematic-analyst** - Cross-chapter coherence

**Hook**: `.claude/hooks/post-tool-use.py` auto-updates `BOOK_SUMMARY.md` with word counts and status.

---

## 📋 Workflow Commands

### Phase 1: Setup
- `/setupBook` - Customize for your book
- `/tocToChapters` - Generate chapter files from TOC.md

### Phase 2: Per Chapter (Repeat)
- `/prepareChapter N` → research-assistant (3-stage research, creates brainstorm)
- `/writeChapter N` → chapter-writer (polished content from brainstorm)
- `/styleCheck N` → style-editor (multi-pass review, prioritized feedback)
- `/completeChapter N` - Mark complete

### Phase 3: Book-Level
- `/bookStatus` - Progress dashboard
- `/thematicAnalysis` → thematic-analyst (map themes across book)
- `/findGaps` - Identify weak areas
- `/revisionSweep` - Systematic improvements
- `/finalReview` - Publication readiness
- `/publishChapters` - Git commit & push

---

## 🎯 Subagent Delegation

**Auto-delegate** when user runs these commands:
- `/prepareChapter N` → research-assistant
- `/writeChapter N` → chapter-writer
- `/styleCheck N` → style-editor
- `/thematicAnalysis` → thematic-analyst

**Manual invoke** when user requests explicitly:
- "Use research-assistant to fact-check chapter 3"
- "Use chapter-writer to expand section 2"
- "Use style-editor to compare chapters 1-3"

**Command prompts tell you when to delegate.** Follow them.

---

## 📁 Key Files (Reference, Don't Duplicate)

### Configuration
- `@book.config.json` - Title, author, targets, style preferences
- `@style-guide.md` - Voice, tone, forbidden patterns, quality standards

### Content
- `@TOC.md` - Chapter structure
- `@chapters/chapter-NN.md` - Chapter content
- `@brainstorms/chapter-NN-brainstorm.md` - Research & planning
- `@outlines/chapter-NN-outline.md` - Detailed outlines (optional)

### Tracking
- `@BOOK_SUMMARY.md` - Progress dashboard (auto-updated by hook)
- `@CHAPTER_SUMMARIES.md` - Continuity summaries (optional)

**Subagents read these files directly.** Reference by name (`@style-guide.md`) instead of copying content into prompts.

---

## ⚡ Progress Tracking

**Hook auto-runs** after Write/Edit on `chapters/chapter-*.md`:
1. Counts words (excludes YAML, code, markdown)
2. Determines status: ⬜ Not Started → 🧠 Brainstormed → 📋 Outlined → ✍️ Drafted → 🔍 Revised → ✅ Complete
3. Updates `BOOK_SUMMARY.md` with word count, status, timestamp

**Don't manually update BOOK_SUMMARY.md** - hook handles it.

---

## 🎨 Quality Standards

**Workflow**: brainstorm → write → review → finalize

**Subagent roles**:
- research-assistant: Authoritative sources, proper citations
- chapter-writer: Voice consistency, example deployment, target word counts
- style-editor: Inconsistency detection, specific fixes
- thematic-analyst: Book-level coherence

**Prioritize**: Quality over speed, consistency over volume, publication-ready over draft.

---

## ✅ DO / ❌ DON'T

### DO:
- Delegate when commands instruct
- Trust subagent expertise
- Let hook track progress
- Reference `@style-guide.md` for voice
- Maintain quality standards

### DON'T:
- Manually update BOOK_SUMMARY.md (hook does this)
- Skip brainstorm phase (research foundation critical)
- Ignore subagent feedback (especially style-editor)
- Rush quality checks (consistency > speed)
- Copy file contents into prompts (reference by @filename)

---

## 🚀 Subagent Benefits

**Separate contexts**: Each has own context window, no pollution
**Autonomous**: Load own context, make decisions, report back
**Specialized**: Deep domain training (narrative, editorial, research, literary analysis)

---

## 🎯 Your Role

Coordinate subagent specialists, make high-level decisions, ensure user's vision is realized through quality, consistent, publication-ready content.

**You conduct. Subagents perform. Hook tracks. User writes.**

---

*Powered by Claude Code SDK with specialized subagents and intelligent automation.*

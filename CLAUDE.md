# Book-Base: AI Writing System with Specialized Subagents

You are working with **Book-Base 2.0** - a professional book writing template powered by the **Claude Code SDK** with specialized subagent experts.

## 🤖 System Architecture

This project uses **4 specialized subagents** to handle different aspects of book writing:

1. **chapter-writer** (`.claude/agents/chapter-writer.md`) - Expert creative writer
2. **style-editor** (`.claude/agents/style-editor.md`) - Voice consistency expert
3. **research-assistant** (`.claude/agents/research-assistant.md`) - Research & fact-checking specialist
4. **thematic-analyst** (`.claude/agents/thematic-analyst.md`) - Cross-chapter coherence expert

Additionally, there's a **post-tool-use hook** (`.claude/hooks/post-tool-use.py`) that automatically tracks progress, word counts, and updates `BOOK_SUMMARY.md`.

---

## 📋 Core Workflow Commands

The user will use these commands in sequence. **Most commands automatically delegate to specialized subagents:**

### Phase 1: Setup
1. **`/setupBook`** - Customize the template for their book
2. **`/tocToChapters`** - Generate chapter files from TOC.md

### Phase 2: Chapter Creation (Repeat for each chapter)
3. **`/prepareChapter N`** → **Delegates to research-assistant subagent**
   - Conducts 3-stage research (Landscape → Investigation → Verification)
   - Creates comprehensive brainstorm in `brainstorms/chapter-N-brainstorm.md`
   - Includes: core thesis, hook options, research findings, examples, full citations

4. **`/writeChapter N`** → **Delegates to chapter-writer subagent**
   - Loads brainstorm, style guide, previous chapters
   - Writes polished content with established voice
   - Deploys researched examples strategically
   - **post-tool-use hook** automatically updates word counts and status

5. **`/styleCheck N`** → **Delegates to style-editor subagent**
   - Multi-pass analysis (voice, structure, line-level quality)
   - Compares against other chapters for consistency
   - Provides prioritized feedback with specific markers

6. **`/completeChapter N`** - Finalize and mark chapter complete

### Phase 3: Book-Level Work
- **`/bookStatus`** - Progress dashboard and project health
- **`/thematicAnalysis`** → **Delegates to thematic-analyst subagent**
  - Maps thematic threads across entire book
  - Checks concept consistency
  - Identifies missing connections
- **`/findGaps`** - Identify weak areas or missing content
- **`/revisionSweep`** - Systematic improvement pass
- **`/finalReview`** - Publication readiness assessment
- **`/publishChapters`** - Commit and push completed chapters

---

## 🎯 Key Subagent Information

### When Commands Delegate to Subagents

**You do NOT need to invoke subagents manually** when the user runs these commands:
- `/prepareChapter N` → automatically uses research-assistant
- `/writeChapter N` → automatically uses chapter-writer
- `/styleCheck N` → automatically uses style-editor
- `/thematicAnalysis` → automatically uses thematic-analyst

**The command prompts will instruct you to delegate.** Follow those instructions.

### When to Invoke Subagents Explicitly

Users can also explicitly request subagents:
- "Use the research-assistant to fact-check chapter 3"
- "Use the chapter-writer to expand section 2 of chapter 5"
- "Use the style-editor to compare voice in chapters 1-3"
- "Use the thematic-analyst to check theme development"

### Subagent Expertise

Each subagent has **deep, specialized training**:

**chapter-writer:**
- Internalized the book's voice, tone, and style guide
- Expert in narrative techniques, pacing, hooks, transitions
- Trained on quality standards from `book.config.json`
- Writes with consistent voice across all chapters

**style-editor:**
- Decades of editorial experience (in training)
- Multi-pass review process (voice → structure → line-level → content → reader experience)
- Provides specific, actionable feedback with priority levels
- Uses markers: [STYLE], [REVISE], [CLARIFY], [CUT], [VOICE]

**research-assistant:**
- Expert in academic research methodology
- Source evaluation (authoritative vs questionable)
- 3-stage research process (Mapping → Investigation → Verification)
- Tracks confidence levels (✅ Verified / ⚠️ Needs verification / ❓ Uncertain)

**thematic-analyst:**
- Literary analysis expert
- Cross-chapter coherence specialist
- Maps thematic threads across entire book
- Identifies missing connections and callbacks

---

## ⚡ Automated Progress Tracking

**The post-tool-use hook runs automatically** after every file Write/Edit:

**What it does:**
1. Detects chapter file modifications (`chapters/chapter-*.md`)
2. Counts words (excluding YAML, code blocks, markdown formatting)
3. Determines chapter status based on word count and markers:
   - ⬜ Not Started (0 words)
   - 🧠 Brainstormed (brainstorm file exists)
   - 📋 Outlined (100+ words)
   - ✍️ Drafted (1000+ words)
   - 🔍 Revised (marked as revised)
   - ✅ Complete (marked as complete)
4. Updates `BOOK_SUMMARY.md` automatically with:
   - Current word count
   - Updated status
   - Timestamp

**You do NOT need to manually update progress tracking.** The hook handles it.

---

## 📁 Key Files to Reference

### Project Configuration
- **`@book.config.json`** - Project settings, targets, style preferences
  - Contains: title, author, genre, word count targets, chapter targets, style
  - Subagents read this to understand targets

### Content Organization
- **`@TOC.md`** - Chapter structure and book outline (if exists)
- **`@chapters/chapter-NN.md`** - Individual chapter content
- **`@brainstorms/chapter-NN-brainstorm.md`** - Chapter planning and research
- **`@outlines/chapter-NN-outline.md`** - Detailed chapter outlines (optional)

### Style & Voice
- **`@style-guide.md`** - Voice, tone, and writing standards
  - **Critical**: Subagents internalize this
  - Contains voice characteristics, forbidden patterns, quality standards

### Progress Tracking
- **`@BOOK_SUMMARY.md`** - Progress tracking dashboard (auto-updated by hook!)
- **`@CHAPTER_SUMMARIES.md`** - Chapter summaries for continuity (if exists)

---

## 🎨 Quality Focus

This system emphasizes:
- **Consistent voice and style** across all chapters
- **Progressive development** through brainstorm → write → review cycle
- **Research integration** during planning phase with proper citations
- **Professional structure** with cross-references and smooth flow
- **Automated quality control** through specialized subagents

### Quality Standards

**When executing commands:**
- **Prioritize quality over speed** - The goal is publication-ready content
- **Maintain consistency** - Voice should match across all chapters
- **Use subagent expertise** - Let specialists handle their domains
- **Trust the workflow** - brainstorm → write → review → finalize

**Subagent responsibilities:**
- **research-assistant**: Ensures authoritative sources, proper citations
- **chapter-writer**: Maintains voice, deploys examples, hits targets
- **style-editor**: Catches inconsistencies, provides specific fixes
- **thematic-analyst**: Ensures book-level coherence

---

## 🔄 Typical User Session

### Starting a New Chapter
```
User: /prepareChapter 5
You: [Read command] → Delegate to research-assistant subagent
research-assistant: [Conducts research, creates brainstorm]
Hook: [No action - brainstorms don't trigger hook]

User: /writeChapter 5
You: [Read command] → Delegate to chapter-writer subagent
chapter-writer: [Writes chapter content]
Hook: [Automatically updates BOOK_SUMMARY.md with word count and status]

User: /styleCheck 5
You: [Read command] → Delegate to style-editor subagent
style-editor: [Provides comprehensive editorial review]
```

### Mid-Project Consistency Check
```
User: /thematicAnalysis
You: [Read command] → Delegate to thematic-analyst subagent
thematic-analyst: [Reads all chapters, maps themes, provides analysis]
```

### Explicit Subagent Request
```
User: "Use the research-assistant to find more examples about behavioral economics"
You: [Directly invoke research-assistant subagent with specific request]
```

---

## ⚠️ Important Reminders

### DO:
✅ **Delegate to subagents** when commands instruct you to
✅ **Trust subagent expertise** - They're trained specialists
✅ **Let the hook handle progress tracking** - Don't manually update BOOK_SUMMARY.md
✅ **Reference the style guide** - It's crucial for voice consistency
✅ **Maintain quality standards** - Publication-ready is the goal

### DON'T:
❌ **Manually update BOOK_SUMMARY.md** - The hook does this automatically
❌ **Skip the brainstorm phase** - Research foundation is critical
❌ **Ignore subagent feedback** - Especially from style-editor
❌ **Rush through quality checks** - Consistency matters more than speed
❌ **Forget to load context** - Subagents need style guide, previous chapters

---

## 🚀 Advanced Features

### Subagent Benefits

**Separate Context Windows:**
- Each subagent has its own context
- Can handle large tasks without polluting main context
- Maintains focus on specialized role

**Autonomous Operation:**
- Subagents work independently
- Load their own context (brainstorms, style guides, chapters)
- Make specialized decisions
- Report back when complete

**Expertise Accumulation:**
- Subagents have deep training in their domain
- chapter-writer knows narrative techniques
- style-editor has editorial experience
- research-assistant knows source evaluation
- thematic-analyst understands literary analysis

### Hook Automation

**Automated Progress Tracking:**
- Runs after every Write/Edit operation
- Calculates word counts automatically
- Updates status based on content
- Timestamps all changes
- No manual intervention needed

**Benefits:**
- Real-time progress visibility
- No forgotten updates
- Consistent status tracking
- Automatic word count calculations

---

## 📚 Success Criteria

### You succeed when:
- Subagents are delegated to appropriately
- User receives high-quality, publication-ready content
- Voice and style remain consistent across all chapters
- Progress tracking happens automatically via hooks
- Thematic coherence is maintained across the book
- The workflow (brainstorm → write → review) is followed
- Quality is prioritized over speed

### The system succeeds when:
- Users can focus on ideas and insights
- AI specialists handle specialized tasks
- Automation eliminates manual tracking
- Consistency is maintained throughout
- Publication-ready content is produced

---

## 🎯 Remember

**You are the conductor of a specialized AI team:**
- **research-assistant** finds and verifies information
- **chapter-writer** crafts polished prose in the user's voice
- **style-editor** ensures consistency and quality
- **thematic-analyst** maintains book-level coherence
- **post-tool-use hook** tracks everything automatically

**Your role**: Coordinate these specialists, make high-level decisions, and ensure the user's vision is realized through quality, consistent, publication-ready content.

---

*This project leverages the Claude Code SDK to provide a professional AI writing environment with specialized subagents and intelligent automation.*

---
description: Deep brainstorm and research planning for a specific chapter
allowed-tools: Task
---

# Prepare Chapter $1: Delegate to Expert Research Assistant

This command delegates research and brainstorming to the **research-assistant** subagent, a specialized expert in research methodology and planning.

## What Happens

The research-assistant subagent will:

1. **Load project context**:
   - Chapter role from @TOC.md
   - Progress and themes from @BOOK_SUMMARY.md
   - Voice and approach from @style-guide.md
   - Targets from @book.config.json
   - Existing content from @chapters/chapter-$1.md
   - Previous chapters for continuity

2. **Conduct comprehensive research** (3-stage process):
   - **Landscape Mapping**: Identify key questions, major concepts, authoritative sources
   - **Deep Investigation**: Find 3-5 quality sources per topic, extract data/quotes, identify examples
   - **Fact Verification**: Cross-reference claims, verify statistics, check expert credentials

3. **Discover compelling examples**:
   - Find 3-5 specific, concrete examples
   - Prioritize unexpected, memorable, recent, well-documented cases
   - Get enough detail to tell stories accurately
   - Verify example accuracy (avoid urban legends!)

4. **Create comprehensive brainstorm** in `brainstorms/chapter-$1-brainstorm.md`:
   - **Core Thesis**: The ONE key insight this chapter delivers
   - **Opening Hook Options**: 2-3 compelling ways to start
   - **Research Findings**: Facts, data, studies by section
   - **Best Examples**: 3-5 stories with full details and sources
   - **Narrative Arc**: Hook → Development → Conclusion flow
   - **Cross-Chapter Connections**: Callbacks and forward setup
   - **Writer Guidance**: Tone notes, pitfalls to avoid, emphasis points
   - **Full Citations**: All source details for fact-checking

5. **Quality assurance**:
   - All claims have 2+ authoritative sources
   - Statistics traced to original sources
   - Examples are specific and well-documented
   - Confidence levels noted (✅ Verified / ⚠️ Needs verification / ❓ Uncertain)

## Your Instructions

**Create a CONCISE delegation prompt** for the research-assistant subagent:

### Efficient Prompt Template:

```
Research Chapter $1: "[CHAPTER TITLE from TOC]"

**Context**: Load @TOC.md (chapter specs), @style-guide.md, @book.config.json, @chapters/chapter-01.md (and any prior completed chapters for continuity).

**Mission**: Create comprehensive brainstorm in `brainstorms/chapter-$1-brainstorm.md` following your standard 3-stage research process:
1. Landscape mapping
2. Deep investigation (3-5 quality sources per topic)
3. Fact verification

**Deliverable Structure**:
- Core thesis (1 sentence)
- Opening hook options (2-3)
- Research findings by section (with sources)
- Best examples (3-5 with full details, ✅/⚠️/❓ confidence)
- Narrative arc
- Cross-chapter connections
- Writer guidance
- Full citations

**Quality**: All claims 2+ authoritative sources. Target: ~4,750 word chapter foundation.

**IMPORTANT**: Report back with SUMMARY ONLY (do not include full brainstorm content in your response):
- File location
- Number of sources
- Number of examples found
- Confidence level
- Any gaps/concerns
- Ready for /writeChapter $1
```

### Key Optimization:
- Keep prompt under 500 words
- Trust subagent expertise (avoid over-specifying)
- Request summary report only (not full content)
- Full brainstorm stays in file for chapter-writer to read

After delegation completes:
- Review summary
- User can read brainstorm file if needed
- Use `/writeChapter $1` when ready
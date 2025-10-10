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

## Your Command

**Delegate to the research-assistant subagent to prepare chapter $1.**

The research-assistant is trained in research methodology, source evaluation, and fact-checking. It will create a comprehensive brainstorm so thorough that writing becomes straightforward execution.

After the brainstorm is complete:
- Review the plan and examples
- Use `/writeChapter $1` to delegate to the chapter-writer
- The chapter-writer will use this research foundation automatically
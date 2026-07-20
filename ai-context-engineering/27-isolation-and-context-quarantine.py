"""
AI Context Engineering
Chapter 27: Isolation: Quarantining Context Across Sub-Agents
Section: Compress and Isolate

Read this chapter: https://books.vizuara.ai/read/ai-context-engineering/isolation-and-context-quarantine

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def run_isolated(task_brief):
    # A FRESH context per sub-task — no shared history, no leftovers.
    messages = [
        {"role": "system", "content": SUBAGENT_ROLE},   # narrow, task-specific
        {"role": "user",   "content": task_brief},       # only what THIS task needs
    ]
    result = agent_loop(messages)      # reads docs, calls tools — all inside this window
    return distill(result)             # return ~150 tokens, not the transcript

def orchestrate(libraries):
    # Each call gets its own quarantined window; clutter never crosses.
    verdicts = [run_isolated(brief_for(lib)) for lib in libraries]
    # The orchestrator's window sees ONLY the distilled verdicts.
    return decide(verdicts)            # a small, clean final judgment

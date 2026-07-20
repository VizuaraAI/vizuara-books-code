"""
AI Context Engineering
Chapter 28: Multi-Agent Context Boundaries
Section: Compress and Isolate

Read this chapter: https://books.vizuara.ai/read/ai-context-engineering/multi-agent-context-boundaries

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def run_subagent(task: str, files: list[str]) -> str:
    ctx = Context()                       # a FRESH, private window
    ctx.add_system(REVIEWER_PROMPT)       # sub-agent's own role
    for f in files:
        ctx.add_user(read(f))             # raw code enters HERE, and only here
    review = agent_loop(ctx)              # sub-agent thinks in isolation
    return summarize(review, max_tokens=300)   # <-- the ONLY thing that escapes

def orchestrate(task: str) -> str:
    lead = Context()
    lead.add_system(ORCHESTRATOR_PROMPT)
    lead.add_user(task)
    for area, files in split_by_module(task):
        summary = run_subagent(f"Review {area}", files)
        lead.add_user(f"[{area} report] {summary}")   # summary in, NOT ctx
    return agent_loop(lead)               # lead composes final answer

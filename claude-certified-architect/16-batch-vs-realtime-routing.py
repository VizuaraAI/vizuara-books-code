"""
Claude Certified Architect (CCAF)
Chapter 16: Batch vs Real-Time Routing
Section: Batching and the Extraction Pipeline Lab

Read this chapter: https://books.vizuara.ai/read/claude-certified-architect/batch-vs-realtime-routing

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def route(request):
    # 1. Hard gate: is a human waiting on this answer right now?
    if request.interactive:
        return "realtime"

    # 2. Hard gate: does a downstream step block on this result?
    if request.blocks_downstream:
        return "realtime"

    # 3. Latency budget: can the caller tolerate the batch window?
    if request.max_wait < BATCH_WINDOW:      # BATCH_WINDOW = 24 hours
        return "realtime"

    # 4. Nothing is waiting → take the discount.
    return "batch"

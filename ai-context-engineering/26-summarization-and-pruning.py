"""
AI Context Engineering
Chapter 26: Summarization and Pruning Strategies
Section: Compress and Isolate

Read this chapter: https://books.vizuara.ai/read/ai-context-engineering/summarization-and-pruning

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def maybe_summarize(summary, recent_turns, budget_tokens):
    # recent_turns: list of verbatim turns, newest last
    if count_tokens(recent_turns) <= budget_tokens:
        return summary, recent_turns            # nothing to do yet

    # the oldest turns overflow the budget → fold them in
    overflow = recent_turns[:-KEEP_VERBATIM]    # e.g. keep last 4 verbatim
    kept     = recent_turns[-KEEP_VERBATIM:]

    prompt = (
        f"Running summary so far:\n{summary}\n\n"
        f"New turns to fold in:\n{render(overflow)}\n\n"
        "Rewrite the running summary to include the new turns. "
        "Preserve all facts, decisions, IDs, and open questions. "
        "Be terse."
    )
    summary = llm(prompt)                        # one cheap model call
    return summary, kept

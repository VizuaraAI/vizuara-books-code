"""
Harness Engineering
Chapter 19: The context window as a resource
Section: Context Engineering

Read this chapter: https://books.vizuara.ai/read/harness-engineering/the-context-window-as-a-resource

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo: imports & stubs (added to make this file runnable) ---
# 2. names the BOOK defines in another chapter. context.py holds those
#    definitions copied verbatim from the chapter that introduces them.
from context import call_model, TOOLS

# 3. names this chapter refers to but the book never defines. They are
#    stubbed - honestly - so the file imports and static-checks; the
#    reader supplies the real thing.
messages = None         # TODO: this block is a fragment of the agent loop's body
reply = None            # TODO: this block is a fragment of the agent loop's body
tool_results = None     # TODO: this block is a fragment of the agent loop's body
history = None          # TODO: the full, uncompacted message history
always_include = None   # TODO: the non-negotiable parts: system prompt + tool schemas
relevant_memory = None  # TODO: facts pulled from the memory store (Ch. 22)
keep_recent = None      # TODO: the last few turns, kept verbatim
history_before = None   # TODO: everything older than the recent window
token_count = None      # TODO: count tokens for a list of message parts
compact = None          # TODO: summarise old turns down (Ch. 21)
# --- end companion-repo additions ---

# --- block 1 ---
# bare harness — the loop just appends, forever
messages.append({"role": "assistant", "content": reply.content})
messages.append({"role": "user", "content": tool_results})

# --- block 2 ---
def assemble_context(history, budget_tokens):
    """Choose what the model sees THIS turn — not everything, the right things."""
    parts = []
    parts += always_include()          # system prompt + tool schemas: non-negotiable
    parts += relevant_memory(history)  # facts pulled from a memory store (CLAUDE.md, notes)
    recent = keep_recent(history)      # the last few turns, verbatim — freshness matters
    older  = history_before(recent)

    used = token_count(parts) + token_count(recent)
    if used > budget_tokens:           # over budget? the old stuff gets compacted, not dropped
        older = compact(older)         # summarize it down to a fraction of its tokens
    return parts + older + recent

# the loop now calls the model on the ASSEMBLED context, not the raw history
reply = call_model(assemble_context(history, budget_tokens=40_000), TOOLS)

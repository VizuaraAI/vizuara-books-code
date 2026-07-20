"""
Harness Engineering
Chapter 20: Context budgets: what goes in, what gets evicted
Section: Context Engineering

Read this chapter: https://books.vizuara.ai/read/harness-engineering/context-budgets

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo: imports & stubs (added to make this file runnable) ---
# 3. names this chapter refers to but the book never defines. They are
#    stubbed - honestly - so the file imports and static-checks; the
#    reader supplies the real thing.
clear_old_tool_results = None  # TODO: budget rung 1: drop stale tool output
summarize_old_turns = None     # TODO: budget rung 2: compact old turns (Ch. 21)
# --- end companion-repo additions ---

# --- block 1 ---
WINDOW      = 200_000
REPLY_RESERVE = 8_000          # room for the model's answer
SAFETY      = 2_000            # counting is approximate; leave slack

INPUT_BUDGET = WINDOW - REPLY_RESERVE - SAFETY   # = 190_000

# --- block 2 ---
def estimate_tokens(text: str) -> int:
    # cheap, good-enough: ~4 chars per token for mixed code+prose
    return len(text) // 4 + 1

def budget_used(messages, system_prompt, tools):
    total = estimate_tokens(system_prompt)
    total += sum(estimate_tokens(str(t)) for t in tools)
    for m in messages:
        total += estimate_tokens(str(m["content"])) + 4   # per-message overhead
    return total

# --- block 3 ---
def clip_tool_result(text: str, max_tokens: int = 4_000) -> str:
    budget_chars = max_tokens * 4
    if len(text) <= budget_chars:
        return text
    head = text[: budget_chars // 2]
    tail = text[-budget_chars // 2 :]
    dropped = estimate_tokens(text) - max_tokens
    return f"{head}\n\n… [{dropped} tokens truncated] …\n\n{tail}"

# --- block 4 ---
def prepare_context(messages, system_prompt, tools):
    used = budget_used(messages, system_prompt, tools)
    if used <= INPUT_BUDGET:
        return messages                      # plenty of room, do nothing

    messages = clear_old_tool_results(messages)     # rung 1
    if budget_used(messages, system_prompt, tools) > INPUT_BUDGET:
        messages = summarize_old_turns(messages)    # rung 2
    return messages

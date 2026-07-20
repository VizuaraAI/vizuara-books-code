"""
Harness Engineering
Chapter 21: Compaction & summarization
Section: Context Engineering

Read this chapter: https://books.vizuara.ai/read/harness-engineering/compaction-and-summarization

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
text_of = None     # TODO: the book never defines it; return the reply's plain text
run_tools = None   # TODO: run every tool_use block in a reply -> tool_result blocks
render = None      # TODO: render a slab of messages as text for the summariser
SYSTEM_MSG = None  # TODO: the system message pinned at messages[0]
# --- end companion-repo additions ---

# --- block 1 ---
def tokens_of(messages):
    # cheap-and-safe estimate; use the provider's real tokenizer in production
    return sum(len(str(m["content"])) for m in messages) // 4

CONTEXT_LIMIT = 200_000
COMPACT_AT    = 0.75          # fire when 75% full

def should_compact(messages):
    return tokens_of(messages) > CONTEXT_LIMIT * COMPACT_AT

# --- block 2 ---
COMPACT_PROMPT = """You are compacting a long agent session to save context.
Summarize the conversation below into a dense, factual briefing. Preserve:
  - the user's original goal and any hard constraints
  - key facts discovered (versions, file paths, schemas, gotchas)
  - decisions made and WHY
  - files created/edited and what changed
  - what is DONE and what is still PENDING
Be specific. Keep identifiers, paths, and numbers exact. Omit chit-chat.
Write it as notes-to-self the agent can act on cold."""

def compact(messages, keep_recent=6):
    head   = messages[:2]                 # system + original request (pinned)
    middle = messages[2:-keep_recent]     # the slab we compress
    tail   = messages[-keep_recent:]      # recent turns (verbatim)

    summary = call_model(
        messages=[{"role": "user",
                   "content": COMPACT_PROMPT + "\n\n" + render(middle)}],
        tools=[],
    )
    summary_msg = {
        "role": "user",
        "content": f"[SUMMARY OF EARLIER WORK]\n{text_of(summary)}",
    }
    return head + [summary_msg] + tail    # the new, short history

# --- block 3 ---
def run_agent(user_request):
    messages = [SYSTEM_MSG, {"role": "user", "content": user_request}]
    while True:
        if should_compact(messages):
            messages = compact(messages)     # distill + hydrate, in place
        reply = call_model(messages, TOOLS)
        messages.append({"role": "assistant", "content": reply.content})
        if reply.stop_reason != "tool_use":
            return text_of(reply)
        messages.append(run_tools(reply))    # append tool results, then loop

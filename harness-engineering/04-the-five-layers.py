"""
Harness Engineering
Chapter 4: The anatomy: five layers of a harness
Section: Start Here

Read this chapter: https://books.vizuara.ai/read/harness-engineering/the-five-layers

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
text_of = None               # TODO: the book never defines it; return the reply's plain text
run_tools = None             # TODO: run every tool_use block in a reply -> tool_result blocks
run_tools_with_retry = None  # TODO: run_tools + transient-error backoff (Ch. 27)
load_checkpoint = None       # TODO: restore a run's message list, or None (Ch. 25)
checkpoint = None            # TODO: persist the message list for a run id (Ch. 25)
# --- end companion-repo additions ---

# --- block 1 ---
def run_agent(user_request):
    messages = [{"role": "user", "content": user_request}]
    while True:
        reply = call_model(messages, TOOLS)      # 1. ask the model
        messages.append(reply)                   #    remember what it decided
        if reply.stop_reason != "tool_use":      # 2. no tool → we're done
            return text_of(reply)
        results = run_tools(reply)               # 3. run what it asked for
        messages.append(results)                 # 4. feed results back
        # 5. loop — the model now sees the results and decides again

# --- block 2 ---
def run_agent_durable(user_request, run_id):
    messages = load_checkpoint(run_id) or [{"role": "user", "content": user_request}]
    while True:
        reply = call_model(messages, TOOLS)
        messages.append(reply)
        checkpoint(run_id, messages)             # persist BEFORE side effects
        if reply.stop_reason != "tool_use":
            return text_of(reply)
        results = run_tools_with_retry(reply)    # transient errors → back off & retry
        messages.append(results)
        checkpoint(run_id, messages)             # persist again after the step

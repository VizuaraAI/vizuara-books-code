"""
Harness Engineering
Chapter 9: Stop conditions: when does the loop end?
Section: The Agent Loop

Read this chapter: https://books.vizuara.ai/read/harness-engineering/stop-conditions

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
text_of = None        # TODO: the book never defines it; return the reply's plain text
run_all_tools = None  # TODO: run every tool_use block in a reply
run_one_tool = None   # TODO: run a single tool_use block -> a tool_result block
# --- end companion-repo additions ---

# --- block 1 ---
def run_agent(user_request, max_turns=40):
    messages = [{"role": "user", "content": user_request}]
    for turn in range(max_turns):                      # hard ceiling on laps
        reply = call_model(messages, TOOLS)
        messages.append({"role": "assistant", "content": reply.content})

        if reply.stop_reason != "tool_use":            # model says it's done
            return {"answer": text_of(reply), "reason": "model_done"}

        tool_results = run_all_tools(reply)
        messages.append({"role": "user", "content": tool_results})

    # fell out of the for-loop: the model never stopped on its own
    return {"answer": text_of(reply), "reason": "max_turns_exceeded"}

# --- block 2 ---
def run_agent(user_request, cancel_event, max_turns=40):
    messages = [{"role": "user", "content": user_request}]
    for turn in range(max_turns):
        if cancel_event.is_set():                      # checkpoint: before the model call
            return {"answer": None, "reason": "interrupted"}

        reply = call_model(messages, TOOLS)
        messages.append({"role": "assistant", "content": reply.content})
        if reply.stop_reason != "tool_use":
            return {"answer": text_of(reply), "reason": "model_done"}

        tool_results = []
        for block in reply.content:
            if block.type == "tool_use":
                if cancel_event.is_set():              # checkpoint: before each tool runs
                    return {"answer": None, "reason": "interrupted"}
                tool_results.append(run_one_tool(block))
        messages.append({"role": "user", "content": tool_results})

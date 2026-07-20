"""
Harness Engineering
Chapter 7: The agent loop from first principles
Section: The Agent Loop

Read this chapter: https://books.vizuara.ai/read/harness-engineering/the-agent-loop-from-first-principles

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo: imports & stubs (added to make this file runnable) ---
# 2. names the BOOK defines in another chapter. context.py holds those
#    definitions copied verbatim from the chapter that introduces them.
from context import call_model, TOOLS, run_tool

# 3. names this chapter refers to but the book never defines. They are
#    stubbed - honestly - so the file imports and static-checks; the
#    reader supplies the real thing.
text_of = None        # TODO: the book never defines it; return the reply's plain text
assistant_msg = None  # TODO: wrap a reply as an assistant message dict
# --- end companion-repo additions ---

# --- block 1 ---
def run_agent(user_request):
    messages = [{"role": "user", "content": user_request}]
    while True:
        reply = call_model(messages, TOOLS)          # 1. ask the model
        messages.append(assistant_msg(reply))        #    remember what it said

        if reply.stop_reason != "tool_use":          # 2. prose, not a request?
            return text_of(reply)                     #    → the model is done

        results = []
        for block in reply.content:                  # 3. run every tool it asked for
            if block.type == "tool_use":
                out = run_tool(block.name, block.input)
                results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": str(out),
                })
        messages.append({"role": "user", "content": results})  # 4. feed results back
        # 5. loop — the model now sees the results and chooses again

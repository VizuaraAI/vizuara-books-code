"""
Harness Engineering
Chapter 6: How to use this site
Section: Start Here

Read this chapter: https://books.vizuara.ai/read/harness-engineering/how-to-use-this-site

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
text_of = None              # TODO: the book never defines it; return the reply's plain text
run_requested_tools = None  # TODO: run every tool_use block in a reply
# --- end companion-repo additions ---

# --- block 1 ---
def run_agent(user_request):
    messages = [{"role": "user", "content": user_request}]
    while True:
        reply = call_model(messages, TOOLS)      # ask the model
        messages.append({"role": "assistant", "content": reply.content})
        if reply.stop_reason != "tool_use":      # no tool? we're done
            return text_of(reply)
        results = run_requested_tools(reply)     # act on the machine
        messages.append({"role": "user", "content": results})
        # loop: the model now sees the results and decides what's next

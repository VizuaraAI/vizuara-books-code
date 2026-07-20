"""
Harness Engineering
Chapter 15: Streaming tool calls to the UI
Section: Tools & the Execution Environment

Read this chapter: https://books.vizuara.ai/read/harness-engineering/streaming-tool-calls-to-the-ui

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
render_assistant_text = None  # TODO: print the model's prose to the terminal
summarize_args = None         # TODO: one-line human summary of a tool call's arguments
bold = None                   # TODO: ANSI bold wrapper
dim = None                    # TODO: ANSI dim wrapper
indent = None                 # TODO: indent a block of text for display
green = None                  # TODO: ANSI green wrapper
red = None                    # TODO: ANSI red wrapper
# --- end companion-repo additions ---

# --- block 1 ---
def run_agent(user_request):
    messages = [{"role": "user", "content": user_request}]
    while True:
        reply = call_model(messages, TOOLS)
        messages.append({"role": "assistant", "content": reply.content})

        # render any plain text the model produced this turn
        for block in reply.content:
            if block.type == "text":
                render_assistant_text(block.text)

        if reply.stop_reason != "tool_use":
            return

        tool_results = []
        for block in reply.content:
            if block.type == "tool_use":
                render_tool_call(block.name, block.input)   # ← BEFORE running: the intent
                out = run_tool(block.name, block.input)
                render_tool_result(block.name, out)         # ← AFTER running: the result
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": str(out),      # full result → model
                })
        messages.append({"role": "user", "content": tool_results})

# --- block 2 ---
GLYPH = {"read_file": "◇", "run_bash": "●", "edit_file": "✎"}

def render_tool_call(name, args):
    # a one-line, human-readable summary of the INTENT
    summary = summarize_args(name, args)          # e.g. run_bash → the cmd string
    print(f"\n{GLYPH.get(name, '•')} {bold(name)}  {dim(summary)}")

def render_tool_result(name, out):
    text = str(out)
    lines = text.splitlines()
    shown = "\n".join(lines[:6])                   # human sees the gist…
    print(indent(dim(shown)))
    if len(lines) > 6:
        print(indent(dim(f"… (+{len(lines) - 6} more lines)")))

# --- block 3 ---
import difflib

def render_edit(path, old, new):
    print(f"\n✎ {bold(path)}")
    diff = difflib.unified_diff(
        old.splitlines(), new.splitlines(),
        lineterm="", n=2,          # 2 lines of surrounding context
    )
    for line in diff:
        if line.startswith("+") and not line.startswith("+++"):
            print(green(line))     # additions
        elif line.startswith("-") and not line.startswith("---"):
            print(red(line))       # deletions
        elif line.startswith("@@"):
            print(dim(line))       # hunk header, muted
        else:
            print(dim(line))       # unchanged context, muted

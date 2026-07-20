"""
Harness Engineering
Chapter 12: Build: your first bare harness
Section: The Agent Loop

Read this chapter: https://books.vizuara.ai/read/harness-engineering/your-first-bare-harness

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo: imports & stubs (added to make this file runnable) ---
# 2. names the BOOK defines in another chapter. context.py holds those
#    definitions copied verbatim from the chapter that introduces them.
from context import SYSTEM_PROMPT

# 3. names this chapter refers to but the book never defines. They are
#    stubbed - honestly - so the file imports and static-checks; the
#    reader supplies the real thing.
text_of = None  # TODO: the book never defines it; return the reply's plain text
# --- end companion-repo additions ---

# --- block 1 ---
import anthropic
client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from the env

def call_model(messages, tools):
    return client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        messages=messages,
        tools=tools,        # the schemas the model is allowed to call
    )

# --- block 2 ---
import subprocess, pathlib

TOOLS = [
    {
        "name": "read_file",
        "description": "Read a text file and return its contents.",
        "input_schema": {
            "type": "object",
            "properties": {"path": {"type": "string"}},
            "required": ["path"],
        },
    },
    {
        "name": "run_bash",
        "description": "Run a shell command and return stdout+stderr.",
        "input_schema": {
            "type": "object",
            "properties": {"cmd": {"type": "string"}},
            "required": ["cmd"],
        },
    },
]

def run_tool(name, args):
    if name == "read_file":
        return pathlib.Path(args["path"]).read_text()
    if name == "run_bash":
        r = subprocess.run(args["cmd"], shell=True, capture_output=True, text=True)
        return (r.stdout + r.stderr)[:4000]
    return f"unknown tool: {name}"

# --- block 3 ---
def run_agent(user_request):
    messages = [{"role": "user", "content": user_request}]
    while True:
        reply = call_model(messages, TOOLS)               # 1. ask the model
        messages.append({"role": "assistant", "content": reply.content})

        if reply.stop_reason != "tool_use":               # 2. no tool? we're done
            return text_of(reply)

        tool_results = []
        for block in reply.content:                       # 3. run every tool it asked for
            if block.type == "tool_use":
                out = run_tool(block.name, block.input)
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": str(out),
                })
        messages.append({"role": "user", "content": tool_results})  # 4. feed results back
        # 5. loop: the model now sees the results and decides what to do next

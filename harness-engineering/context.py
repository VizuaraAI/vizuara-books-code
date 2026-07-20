"""
Harness Engineering - shared context for the companion code.

Several chapters reuse a small vocabulary that the book defines once and then
refers to by name ("the loop from Layer 1", "the real execution from Ch. 4",
"the same call_model as before"). Because each companion file holds only ONE
chapter's blocks, those names look undefined when a file is read on its own.

This module collects them in one place so the per-chapter files can import
them. Every definition below is COPIED VERBATIM from the chapter that
introduces it in the book - nothing here is invented, rewritten, or completed.
The comment above each block says exactly where it comes from.

Names the book uses but never actually defines anywhere (text_of, run_tools,
tool_uses, ...) are NOT here. Those are stubbed at the top of the individual
files that need them, so it stays obvious that the reader has to supply them.
"""

# ---------------------------------------------------------------------------
# Chapter 23 - System prompts as infrastructure, not prose, block 1
# https://books.vizuara.ai/read/harness-engineering/system-prompts-as-infrastructure
# ---------------------------------------------------------------------------
SYSTEM_PROMPT = "You are a helpful coding assistant. Be concise."

# ---------------------------------------------------------------------------
# Chapter 12 - Build: your first bare harness, block 1
# https://books.vizuara.ai/read/harness-engineering/your-first-bare-harness
# ---------------------------------------------------------------------------
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

# ---------------------------------------------------------------------------
# Chapter 12 - Build: your first bare harness, block 2
# https://books.vizuara.ai/read/harness-engineering/your-first-bare-harness
# ---------------------------------------------------------------------------
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

# ---------------------------------------------------------------------------
# Chapter 25 - Durable execution & checkpointing, block 2
# https://books.vizuara.ai/read/harness-engineering/durable-execution-and-checkpointing
# ---------------------------------------------------------------------------
def run_step(log, step_id, fn):
    """Execute fn() once, durably. On replay, return the cached result."""
    # Are we replaying a step the log already has?
    if log.cursor < len(log.events):
        recorded = log.events[log.cursor]
        assert recorded["step_id"] == step_id, "log diverged from code!"
        log.cursor += 1
        return recorded["result"]        # fast-forward: no execution, no side effect

    # Live execution: run it for real, then commit the result.
    result = fn()
    log.append({"step_id": step_id, "result": result})
    log.cursor += 1
    return result

# ---------------------------------------------------------------------------
# Chapter 26 - Replay & resumable sessions, block 2
# https://books.vizuara.ai/read/harness-engineering/replay-and-resumable-sessions
# ---------------------------------------------------------------------------
def rebuild_messages(events):
    messages = []
    for e in events:
        if e["type"] == "user_msg":
            messages.append({"role": "user", "content": e["content"]})
        elif e["type"] == "assistant_msg":
            messages.append({"role": "assistant", "content": e["content"]})
        elif e["type"] == "tool_result":
            messages.append({"role": "user", "content": [{
                "type": "tool_result",
                "tool_use_id": e["tool_use_id"],
                "content": e["result"],
            }]})
    return messages

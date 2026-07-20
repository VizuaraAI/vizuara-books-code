"""
Harness Engineering
Chapter 25: Durable execution & checkpointing
Section: Durability, Recovery & Orchestration

Read this chapter: https://books.vizuara.ai/read/harness-engineering/durable-execution-and-checkpointing

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
text_of = None            # TODO: the book never defines it; return the reply's plain text
tool_uses = None          # TODO: the tool_use blocks of a reply
tool_result_block = None  # TODO: build one tool_result block from an id + output
# --- end companion-repo additions ---

# --- block 1 ---
import json, hashlib, pathlib

class EventLog:
    def __init__(self, run_id):
        self.path = pathlib.Path(f"runs/{run_id}.jsonl")
        self.path.parent.mkdir(exist_ok=True)
        # replay: load everything already committed for this run
        self.events = []
        if self.path.exists():
            self.events = [json.loads(l) for l in self.path.read_text().splitlines()]
        self.cursor = 0  # how far into the log replay has advanced

    def append(self, event):
        with self.path.open("a") as f:
            f.write(json.dumps(event) + "\n")
            f.flush()              # get it onto disk before we act on it
        self.events.append(event)

# --- block 2 ---
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

# --- block 3 ---
def run_agent(user_request, run_id):
    log = EventLog(run_id)
    messages = [{"role": "user", "content": user_request}]
    turn = 0
    while True:
        # STEP: the model call, keyed by turn number
        reply = run_step(log, f"model:{turn}",
                         lambda: call_model(messages, TOOLS))
        messages.append({"role": "assistant", "content": reply["content"]})

        if reply["stop_reason"] != "tool_use":
            return text_of(reply)

        tool_results = []
        for i, block in enumerate(tool_uses(reply)):
            # STEP: each tool call, keyed by turn + position + the block's own id
            out = run_step(log, f"tool:{turn}:{i}:{block['id']}",
                           lambda b=block: run_tool(b["name"], b["input"]))
            tool_results.append(tool_result_block(block["id"], out))

        messages.append({"role": "user", "content": tool_results})
        turn += 1

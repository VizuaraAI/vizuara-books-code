"""
Harness Engineering
Chapter 27: Self-healing loops: retries & failure classification
Section: Durability, Recovery & Orchestration

Read this chapter: https://books.vizuara.ai/read/harness-engineering/self-healing-loops

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo: imports & stubs (added to make this file runnable) ---
# 1. modules the chapter uses but does not import in its own blocks.
from anthropic import (RateLimitError, APIConnectionError,
                       InternalServerError)

# 2. names the BOOK defines in another chapter. context.py holds those
#    definitions copied verbatim from the chapter that introduces them.
from context import call_model, TOOLS, run_tool

# 3. names this chapter refers to but the book never defines. They are
#    stubbed - honestly - so the file imports and static-checks; the
#    reader supplies the real thing.
text_of = None       # TODO: the book never defines it; return the reply's plain text
messages = None      # TODO: this block is a fragment of the agent loop's body
reply = None         # TODO: this block is a fragment of the agent loop's body
tool_results = None  # TODO: this block is a fragment of the agent loop's body
# --- end companion-repo additions ---

# --- block 1 ---
import time, random

# errors the API/SDK raises that are worth retrying verbatim
TRANSIENT = (RateLimitError, APIConnectionError, InternalServerError)  # 429, network, 5xx

def call_model_resilient(messages, tools, max_retries=5):
    for attempt in range(max_retries):
        try:
            return call_model(messages, tools)          # the plain call from Layer 1
        except TRANSIENT as e:
            if attempt == max_retries - 1:
                raise                                    # give up → becomes terminal
            delay = min(2 ** attempt, 30) + random.uniform(0, 1)  # backoff + jitter
            time.sleep(delay)                            # 1s, 2s, 4s, 8s, 16s (+jitter)
    # non-transient exceptions are NOT caught here — they propagate on purpose

# --- block 2 ---
def run_tool_safe(name, args):
    try:
        return {"ok": True, "output": run_tool(name, args)}
    except Exception as e:
        # the tool failed, but that's DATA for the model, not a crash for us
        return {"ok": False, "output": f"ERROR: {type(e).__name__}: {e}"}

# --- block 3 ---
for block in reply.content:
    if block.type == "tool_use":
        result = run_tool_safe(block.name, block.input)
        tool_results.append({
            "type": "tool_result",
            "tool_use_id": block.id,
            "content": result["output"],
            "is_error": not result["ok"],   # the API lets you flag it as an error
        })
messages.append({"role": "user", "content": tool_results})
# loop: next lap, the model SEES "ERROR: FileNotFoundError: no such file: sonfig.py"
#       and typically fixes its own mistake — retries with the correct path

# --- block 4 ---
def run_agent(user_request, max_turns=40):
    messages = [{"role": "user", "content": user_request}]
    recent_errors = []
    for turn in range(max_turns):                         # guard 1: turn budget
        reply = call_model_resilient(messages, TOOLS)     # transient retries handled inside
        messages.append({"role": "assistant", "content": reply.content})
        if reply.stop_reason != "tool_use":
            return text_of(reply)                          # normal, healthy exit

        tool_results, errored = [], False
        for block in reply.content:
            if block.type == "tool_use":
                result = run_tool_safe(block.name, block.input)
                errored = errored or not result["ok"]
                tool_results.append({ "type": "tool_result",
                    "tool_use_id": block.id, "content": result["output"],
                    "is_error": not result["ok"] })
        messages.append({"role": "user", "content": tool_results})

        recent_errors = (recent_errors + [errored])[-4:]   # guard 2: loop detection
        if recent_errors == [True, True, True, True]:       # four failing laps in a row
            return "Halting: the agent is stuck failing the same step. " \
                   "Surfacing to a human with the transcript so far."
    return f"Halting: hit the {max_turns}-turn budget without finishing."

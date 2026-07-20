"""
Harness Engineering
Chapter 26: Replay & resumable sessions
Section: Durability, Recovery & Orchestration

Read this chapter: https://books.vizuara.ai/read/harness-engineering/replay-and-resumable-sessions

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
text_of = None  # TODO: the book never defines it; return the reply's plain text
# --- end companion-repo additions ---

# --- block 1 ---
import json, os, time, pathlib

def append_event(log_path, event):
    event["ts"] = time.time()
    with open(log_path, "a") as f:
        f.write(json.dumps(event) + "\n")   # one JSON object per line (JSONL)
        f.flush()
        os.fsync(f.fileno())                # actually hit the disk before we return

def load_events(log_path):
    if not pathlib.Path(log_path).exists():
        return []
    with open(log_path) as f:
        return [json.loads(line) for line in f if line.strip()]

# --- block 2 ---
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

# --- block 3 ---
def run_tool_guarded(log_path, events, tool_use_id, name, args):
    # 1. Replay path: did a previous life already finish this call?
    for e in events:
        if e["type"] == "tool_result" and e["tool_use_id"] == tool_use_id:
            return e["result"]            # cached — do NOT re-run the side effect

    # 2. First time we've seen this id: run it exactly once...
    result = run_tool(name, args)

    # 3. ...and durably record the result BEFORE the model ever sees it.
    append_event(log_path, {
        "type": "tool_result",
        "tool_use_id": tool_use_id,
        "result": result,
    })
    return result

# --- block 4 ---
def run_durable_agent(log_path, user_request=None):
    events = load_events(log_path)
    if user_request:                                  # fresh turn on an existing session
        append_event(log_path, {"type": "user_msg", "content": user_request})
        events = load_events(log_path)

    while True:
        messages = rebuild_messages(events)           # state = fold(log)
        reply = call_model(messages, TOOLS)
        append_event(log_path, {"type": "assistant_msg", "content": reply.content})
        events = load_events(log_path)

        if reply.stop_reason != "tool_use":
            return text_of(reply)                     # done; log holds the full session

        for block in reply.content:
            if block.type == "tool_use":
                run_tool_guarded(log_path, events, block.id, block.name, block.input)
        events = load_events(log_path)                # pick up the results we just logged

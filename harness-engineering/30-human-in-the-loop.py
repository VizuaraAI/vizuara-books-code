"""
Harness Engineering
Chapter 30: Human-in-the-loop: plans, approvals, escalation
Section: Durability, Recovery & Orchestration

Read this chapter: https://books.vizuara.ai/read/harness-engineering/human-in-the-loop

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo: imports & stubs (added to make this file runnable) ---
# 2. names the BOOK defines in another chapter. context.py holds those
#    definitions copied verbatim from the chapter that introduces them.
from context import call_model, TOOLS, run_tool, run_step, rebuild_messages

# 3. names this chapter refers to but the book never defines. They are
#    stubbed - honestly - so the file imports and static-checks; the
#    reader supplies the real thing.
text_of = None        # TODO: the book never defines it; return the reply's plain text
tool_uses = None      # TODO: the tool_use blocks of a reply
tool_result = None    # TODO: build one tool_result block from a block + output
denied_result = None  # TODO: build a tool_result saying the human refused
describe = None       # TODO: human-readable description of a pending action
now = None            # TODO: current timestamp for the event log
notify_humans = None  # TODO: ping Slack / dashboard / email
wake_run = None       # TODO: re-enqueue a suspended run so it resumes
start_turn = None     # TODO: the turn number to resume from, read off the log
# --- end companion-repo additions ---

# --- block 1 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# if is_dangerous(cmd):
#     ans = input(f"Run `{cmd}`? [y/N] ")
#     if ans.lower() != "y":
#         return "denied by user"

# --- block 2 ---
DANGEROUS = ("git push", "rm ", "deploy", "drop table", "curl -X POST", "migrate")

def needs_approval(tool_name, args):
    if tool_name == "write_file":
        return False                     # cheap to undo; let it run
    if tool_name == "run_bash":
        cmd = args.get("cmd", "")
        return any(d in cmd for d in DANGEROUS)
    return False

# --- block 3 ---
class Suspend(Exception):
    """Raised to unwind the loop cleanly when we're waiting on a human."""
    def __init__(self, request_id):
        self.request_id = request_id

def approval_gate(log, step_id, action_desc):
    rec = log.find(step_id)                      # look for an existing decision

    if rec is None:                              # ABSENT → propose + suspend
        log.append({
            "step_id": step_id,
            "kind": "approval",
            "status": "pending",
            "action": action_desc,
            "requested_at": now(),
        })
        log.flush()                              # durable BEFORE we release
        notify_humans(step_id, action_desc)      # Slack / dashboard / email
        raise Suspend(step_id)                    # unwind — free the process

    if rec["status"] == "pending":               # PENDING → still waiting
        raise Suspend(step_id)                    # replay landed us here; re-suspend

    return rec["status"] == "approved"           # RESOLVED → True/False, continue

# --- block 4 ---
def resolve(log, step_id, approved, reviewer):
    log.append({
        "step_id": step_id,
        "kind": "approval",
        "status": "approved" if approved else "denied",
        "reviewer": reviewer,
        "decided_at": now(),
    })
    log.flush()
    wake_run(log.run_id)     # re-enqueue the suspended run to resume

# --- block 5 ---
def run_agent(log, user_request):
    messages = rebuild_messages(log) or [{"role": "user", "content": user_request}]
    turn = start_turn(log)

    while True:
        reply = run_step(log, f"model:{turn}",
                         lambda: call_model(messages, TOOLS))
        messages.append({"role": "assistant", "content": reply["content"]})
        if reply["stop_reason"] != "tool_use":
            return text_of(reply)

        results = []
        for i, block in enumerate(tool_uses(reply)):
            gate_id = f"gate:{turn}:{i}:{block['id']}"

            if needs_approval(block["name"], block["input"]):
                if not approval_gate(log, gate_id, describe(block)):
                    # denied — don't run it, tell the model why
                    results.append(denied_result(block, "human declined this action"))
                    continue

            out = run_step(log, f"tool:{turn}:{i}:{block['id']}",
                           lambda: run_tool(block["name"], block["input"]))
            results.append(tool_result(block, out))

        messages.append({"role": "user", "content": results})
        turn += 1

# --- block 6 ---
def escalate(log, step_id, reason, context):
    rec = log.find(step_id)
    if rec is None:
        log.append({"step_id": step_id, "kind": "escalation",
                    "status": "open", "reason": reason, "context": context})
        log.flush()
        notify_humans(step_id, f"AGENT STUCK: {reason}", context)
        raise Suspend(step_id)
    if rec["status"] == "open":
        raise Suspend(step_id)
    return rec["guidance"]          # human's hint, fed back into the loop

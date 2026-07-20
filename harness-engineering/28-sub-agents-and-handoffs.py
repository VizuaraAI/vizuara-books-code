"""
Harness Engineering
Chapter 28: Sub-agents & handoffs
Section: Durability, Recovery & Orchestration

Read this chapter: https://books.vizuara.ai/read/harness-engineering/sub-agents-and-handoffs

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo: imports & stubs (added to make this file runnable) ---
# 1. modules the chapter uses but does not import in its own blocks.
from concurrent.futures import ThreadPoolExecutor

# 2. names the BOOK defines in another chapter. context.py holds those
#    definitions copied verbatim from the chapter that introduces them.
from context import call_model

# 3. names this chapter refers to but the book never defines. They are
#    stubbed - honestly - so the file imports and static-checks; the
#    reader supplies the real thing.
text_of = None           # TODO: the book never defines it; return the reply's plain text
run_tools = None         # TODO: run every tool_use block in a reply -> tool_result blocks
SUBAGENT_TOOLS = None    # TODO: the restricted tool set handed to a child agent
SUBAGENT_SYSTEM = None   # TODO: the child agent's system prompt
SYNTHESIS_SYSTEM = None  # TODO: the parent's synthesis system prompt
TRIAGE_SYSTEM = None     # TODO: the triage role's system prompt
TRIAGE_TOOLS = None      # TODO: the triage role's tool set
ROLES = None             # TODO: name -> (system, tools) for each specialist role
handoff_block = None     # TODO: find a handoff tool_use block in a reply, or None
handoff_ack = None       # TODO: the message acknowledging a completed handoff
# --- end companion-repo additions ---

# --- block 1 ---
def run_agent(user_request, tools, system, max_turns=50):
    """The same loop from Layer 1 — nothing new here."""
    messages = [{"role": "user", "content": user_request}]
    for _ in range(max_turns):
        reply = call_model(messages, tools, system)
        messages.append({"role": "assistant", "content": reply.content})
        if reply.stop_reason != "tool_use":
            return text_of(reply)              # <- the child's final answer
        messages.append({"role": "user", "content": run_tools(reply)})
    return "sub-agent hit its turn budget"

def spawn_agent(args):
    """A tool the PARENT can call. Runs a full child loop in isolation."""
    return run_agent(
        user_request = args["task"],           # the one narrow instruction
        tools        = SUBAGENT_TOOLS,          # often a RESTRICTED tool set
        system       = SUBAGENT_SYSTEM,         # "you are a focused investigator…"
        max_turns    = 20,
    )

# --- block 2 ---
def investigate_codebase(question, targets):
    # DISPATCH — one focused child per target, run in parallel
    with ThreadPoolExecutor() as pool:
        findings = list(pool.map(
            lambda t: spawn_agent({"task": f"In {t}, {question}. Report only what you find."}),
            targets,
        ))
    # SYNTHESIZE — the parent reasons over conclusions, not raw output
    summary = "\n\n".join(f"[{t}]\n{f}" for t, f in zip(targets, findings))
    return call_model(
        [{"role": "user", "content": f"Findings from {len(targets)} investigators:\n{summary}\n\nSynthesize one answer."}],
        tools=[], system=SYNTHESIS_SYSTEM,
    )

# --- block 3 ---
def run_with_handoffs(user_request):
    messages = [{"role": "user", "content": user_request}]
    system, tools = TRIAGE_SYSTEM, TRIAGE_TOOLS
    while True:
        reply = call_model(messages, tools, system)
        messages.append({"role": "assistant", "content": reply.content})
        block = handoff_block(reply)
        if block:                                   # a handoff was requested
            system, tools = ROLES[block.input["to"]]   # SWAP identity, keep the convo
            messages.append(handoff_ack(block))
            continue                                # same loop, new specialist driving
        if reply.stop_reason != "tool_use":
            return text_of(reply)
        messages.append({"role": "user", "content": run_tools(reply)})

"""
Harness Engineering
Chapter 24: Build: the context engine
Section: Context Engineering

Read this chapter: https://books.vizuara.ai/read/harness-engineering/building-the-context-engine

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
import anthropic
client = anthropic.Anthropic()

MODEL = "claude-sonnet-4-6"
CONTEXT_LIMIT = 200_000       # the model's hard ceiling
COMPACT_THRESHOLD = 0.75      # start compacting at 75% full — don't wait for the wall

def count_tokens(system, messages, tools):
    r = client.messages.count_tokens(
        model=MODEL, system=system, messages=messages, tools=tools,
    )
    return r.input_tokens

# --- block 2 ---
COMPACTION_PROMPT = """You are compacting an agent's conversation to save context.
Write a dense summary that preserves, in this priority order:
1. The user's original goal and any hard constraints.
2. Decisions made and WHY (architecture, file choices, approaches rejected).
3. Files created or edited, and their current state.
4. What is done, what is in progress, and the immediate next step.
Drop verbatim file contents, tool logs, and idle chatter — keep the facts, not the transcript.
Write it as notes to your future self, not prose."""

def compact(messages, keep_recent=6):
    head, tail = messages[:-keep_recent], messages[-keep_recent:]   # summarize head, keep tail
    summary = client.messages.create(
        model=MODEL, max_tokens=2048,
        system=COMPACTION_PROMPT,
        messages=head + [{"role": "user",
                          "content": "Summarize the conversation above per your instructions."}],
    )
    summary_text = summary.content[0].text
    return [{"role": "user",
             "content": f"[SUMMARY OF EARLIER SESSION]\n{summary_text}"}] + tail

# --- block 3 ---
import pathlib

def load_memory(project_dir="."):
    """Load persistent project memory, if present."""
    for name in ("CLAUDE.md", "AGENTS.md", ".agent/memory.md"):
        p = pathlib.Path(project_dir) / name
        if p.exists():
            return p.read_text()[:8000]     # cap it — memory is a briefing, not a novel
    return ""

# --- block 4 ---
def build_system_prompt(project_dir="."):
    identity = (
        "You are a coding agent operating in a terminal. Work in small, verifiable steps. "
        "Prefer reading before editing. Explain what you are about to do, then do it."
    )
    memory = load_memory(project_dir)
    env = f"<env>\ncwd: {pathlib.Path(project_dir).resolve()}\nos: {__import__('platform').system()}\n</env>"

    parts = [identity, env]
    if memory:
        parts.append(f"<project_memory>\n{memory}\n</project_memory>")
    return "\n\n".join(parts)

# --- block 5 ---
def run_agent(user_request, project_dir="."):
    system = build_system_prompt(project_dir)                 # memory loaded once, up front
    messages = [{"role": "user", "content": user_request}]

    while True:
        # --- context engine: guard the budget before every call ---
        used = count_tokens(system, messages, TOOLS)
        if used > CONTEXT_LIMIT * COMPACT_THRESHOLD:
            messages = compact(messages)                      # collapse the history, keep the tail

        reply = call_model(system, messages, TOOLS)           # 1. ask the model
        messages.append({"role": "assistant", "content": reply.content})

        if reply.stop_reason != "tool_use":                   # 2. no tool? we're done
            return text_of(reply)

        tool_results = []
        for block in reply.content:                           # 3. run every tool it asked for
            if block.type == "tool_use":
                out = run_tool(block.name, block.input)
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": str(out),
                })
        messages.append({"role": "user", "content": tool_results})  # 4. feed results back
        # 5. loop — and the engine will re-check the budget at the top

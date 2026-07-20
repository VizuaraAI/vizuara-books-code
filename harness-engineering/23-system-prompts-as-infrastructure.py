"""
Harness Engineering
Chapter 23: System prompts as infrastructure, not prose
Section: Context Engineering

Read this chapter: https://books.vizuara.ai/read/harness-engineering/system-prompts-as-infrastructure

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo: imports & stubs (added to make this file runnable) ---
# 2. names the BOOK defines in another chapter. context.py holds those
#    definitions copied verbatim from the chapter that introduces them.
from context import client, TOOLS

# 3. names this chapter refers to but the book never defines. They are
#    stubbed - honestly - so the file imports and static-checks; the
#    reader supplies the real thing.
IDENTITY_AND_RULES = None    # TODO: the frozen identity + standing-constraints block
render_tool_guidance = None  # TODO: describe the currently available tools
render_environment = None    # TODO: live facts: cwd, OS, git branch, date
render_mode = None           # TODO: the plan-mode / edit-mode toggle text
render_memory = None         # TODO: the project memory block (CLAUDE.md)
State = None                 # TODO: the harness state object this chapter assumes
# --- end companion-repo additions ---

# --- block 1 ---
SYSTEM_PROMPT = "You are a helpful coding assistant. Be concise."

def call_model(messages, tools):
    return client.messages.create(
        model="claude-sonnet-4-5",
        system=SYSTEM_PROMPT,      # the same frozen string, forever
        messages=messages,
        tools=tools,
    )

# --- block 2 ---
def assemble_system(state):
    parts = []
    parts.append(IDENTITY_AND_RULES)              # 1. who you are, standing constraints
    parts.append(render_tool_guidance(state.tools))  # 2. how to use the tools you have
    parts.append(render_environment(state))       # 3. live facts: cwd, OS, git branch, date
    parts.append(render_mode(state.mode))         # 4. plan-mode / edit-mode toggle
    parts.append(render_memory(state.memory))     # 5. project memory (CLAUDE.md, etc.)
    return "\n\n".join(p for p in parts if p)

# --- block 3 ---
def run_agent(user_request, state):
    state.messages.append({"role": "user", "content": user_request})
    while True:
        system = assemble_system(state)           # recompiled EVERY turn
        reply = call_model(state.messages, state.tools, system=system)
        ...

# --- block 4 ---
def test_plan_mode_forbids_edits():
    state = State(mode="plan", cwd="/tmp/x", tools=TOOLS, memory=None)
    system = assemble_system(state)
    assert "do not modify files" in system.lower()
    assert render_environment(state) in system      # env layer present
    assert "ANTHROPIC_API_KEY" not in system         # no secret leaked

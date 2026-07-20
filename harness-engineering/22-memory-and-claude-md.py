"""
Harness Engineering
Chapter 22: Memory systems & the CLAUDE.md pattern
Section: Context Engineering

Read this chapter: https://books.vizuara.ai/read/harness-engineering/memory-and-claude-md

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo: imports & stubs (added to make this file runnable) ---
# 3. names this chapter refers to but the book never defines. They are
#    stubbed - honestly - so the file imports and static-checks; the
#    reader supplies the real thing.
run_agent = None  # TODO: the agent loop built in Ch. 12
# --- end companion-repo additions ---

# --- block 1 ---
import pathlib

def load_project_memory(root="."):
    """Read the durable project facts, if any. Returns '' when absent."""
    f = pathlib.Path(root) / "CLAUDE.md"
    return f.read_text() if f.exists() else ""

def start_session(user_request, root="."):
    memory = load_project_memory(root)
    messages = []
    if memory:
        messages.append({
            "role": "user",
            "content": f"<project_memory source=\"CLAUDE.md\">\n{memory}\n</project_memory>",
        })
    messages.append({"role": "user", "content": user_request})
    return run_agent(messages)   # the same loop from the last chapter

# --- block 2 ---
MEMORY_FILE = "CLAUDE.md"

REMEMBER_TOOL = {
    "name": "remember",
    "description": (
        "Append a DURABLE, project-level fact to CLAUDE.md so future sessions "
        "start knowing it. Use ONLY for facts true across tasks (conventions, "
        "commands, gotchas) — never for details specific to the current task."
    ),
    "input_schema": {
        "type": "object",
        "properties": {"fact": {"type": "string"}},
        "required": ["fact"],
    },
}

def remember(fact, root="."):
    path = pathlib.Path(root) / MEMORY_FILE
    # In a real harness this goes through the same permission gate as any write.
    with path.open("a") as f:
        f.write(f"\n- {fact.strip()}\n")
    return "saved to CLAUDE.md"

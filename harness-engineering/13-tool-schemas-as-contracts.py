"""
Harness Engineering
Chapter 13: Tool schemas as contracts
Section: Tools & the Execution Environment

Read this chapter: https://books.vizuara.ai/read/harness-engineering/tool-schemas-as-contracts

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import pathlib

# --- block 1 ---
# LOOSE — technically valid, quietly terrible
{
    "name": "edit_file",
    "description": "Edit a file.",
    "input_schema": {
        "type": "object",
        "properties": {"args": {"type": "string"}},  # a blob of anything
    },
}

# --- block 2 ---
# TIGHT — the schema does the teaching
{
    "name": "edit_file",
    "description": (
        "Replace an exact string in a file with a new string. "
        "old_string must match the file's current contents EXACTLY, "
        "including whitespace and indentation, and must be unique in the file. "
        "Read the file first if you are unsure of its exact contents."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "path":       {"type": "string",
                           "description": "Absolute path to the file to edit."},
            "old_string": {"type": "string",
                           "description": "Exact text to find. Must be unique."},
            "new_string": {"type": "string",
                           "description": "Text to replace it with."},
            "replace_all": {"type": "boolean", "default": False,
                            "description": "Replace every occurrence instead of one."},
        },
        "required": ["path", "old_string", "new_string"],
    },
}

# --- block 3 ---
{
    "name": "run_tests",
    "description": (
        "Run the project's test suite and return pass/fail output. "
        "Pick the framework matching the repo; default to pytest for Python."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "framework": {
                "type": "string",
                "enum": ["pytest", "jest", "go"],   # the model cannot invent a fourth
                "description": "Test runner to use.",
            },
            "path": {
                "type": "string",
                "description": "Optional file or dir to scope the run. Omit for the whole suite.",
            },
        },
        "required": ["framework"],
    },
}

# --- block 4 ---
def run_tool(name, args):
    try:
        if name == "read_file":
            p = pathlib.Path(args["path"])
            if not p.exists():
                return f"ERROR: no such file: {p}. Use list_files to see what exists."
            return p.read_text()
        # …other tools…
    except Exception as e:
        return f"ERROR calling {name}: {e}"   # goes back to the model, not the void

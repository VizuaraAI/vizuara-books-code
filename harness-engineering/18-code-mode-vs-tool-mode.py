"""
Harness Engineering
Chapter 18: Code-mode vs. tool-mode
Section: Tools & the Execution Environment

Read this chapter: https://books.vizuara.ai/read/harness-engineering/code-mode-vs-tool-mode

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo: imports & stubs (added to make this file runnable) ---
# 3. names this chapter refers to but the book never defines. They are
#    stubbed - honestly - so the file imports and static-checks; the
#    reader supplies the real thing.
read_file_schema = None  # TODO: the read_file tool schema (Ch. 13)
edit_file_schema = None  # TODO: the edit_file tool schema (Ch. 13)
sandbox = None           # TODO: the isolated executor this chapter describes
# --- end companion-repo additions ---

# --- block 1 ---
# what the model emits as the argument to a single run_python tool call
lines = [(3, 200), (1, 900), (10, 60), (2, 700)]
total = 0
for qty, price in lines:
    subtotal = qty * price
    if subtotal > 500:
        subtotal *= 0.93        # 7% discount
    total += subtotal
print(round(total, 2))

# --- block 2 ---
TOOLS = [
    read_file_schema,           # tool-mode: fixed, narrow, safe-to-allow
    edit_file_schema,           # tool-mode: mutates, needs a permission gate
    {
        "name": "run_python",   # code-mode: the escape hatch for computation
        "description": (
            "Execute a short Python program in an isolated sandbox and return "
            "whatever it prints to stdout. Use for arithmetic, data wrangling, "
            "and chaining multiple operations. No network; scratch filesystem only."
        ),
        "input_schema": {
            "type": "object",
            "properties": {"src": {"type": "string"}},
            "required": ["src"],
        },
    },
]

def run_python(src: str) -> str:
    # runs in a locked-down sandbox: no network, ephemeral FS, wall-clock timeout
    result = sandbox.exec(src, timeout=10)
    return (result.stdout + result.stderr)[:4000]

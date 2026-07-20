"""
AI Agents Bootcamp
Chapter 3: The Anatomy of an Agent
Section: What Is an AI Agent?

Read this chapter: https://books.vizuara.ai/read/ai-agents-bootcamp/anatomy-of-an-agent

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo fixups: names the book uses but this chapter does not define ---
model = None  # TODO: your LLM handle (organ 1). Chapter 9 shows how to make a
#               real one; this chapter only shows the shape of the loop.
run = None    # TODO: the runtime that actually executes a tool call (organ 2).
# --- end fixups ---

# --- block 1 ---
def read_file(path: str) -> str:
    """Return the full text contents of the file at `path`."""
    with open(path) as f:
        return f.read()

def calculator(expression: str) -> float:
    """Evaluate a Python arithmetic expression, e.g. '8000 * 0.15'."""
    return eval(expression)

# --- block 2 ---
messages = [{"role": "user", "content": "What's 15% of the total in sales.csv?"}]

while True:
    reply = model(messages, tools=[read_file, calculator])   # ORGAN 1 decides
    messages.append(reply)                                    # ORGAN 3 remembers
    if reply.tool_call:                                       # did it ask to act?
        result = run(reply.tool_call)                         # ORGAN 2 acts
        messages.append({"role": "tool", "content": result})  # ORGAN 3 remembers
    else:
        break                                                 # it answered — done

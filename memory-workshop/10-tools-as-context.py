"""
Memory in AI Systems
Chapter 10: Tools: Letting the Model Act
Section: Context Engineering

Read this chapter: https://books.vizuara.ai/read/memory-workshop/tools-as-context

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- resolved names (added so this file passes a static check) ---
# The names below are used by this chapter but not defined in it.
# Imports point at context.py, which copies the earlier chapter verbatim.
# Stubs are deliberately empty: the book expects YOU to supply them.
model = None  # TODO: a chat model exposing .generate(messages, tools=...)
TOOLS = {}    # TODO: tool name -> the Python function that runs it (e.g. "multiply")
# --- end resolved names ---

# --- block 1 ---
tools = [{
    "name": "multiply",
    "description": "Multiply two integers. Use this for any exact arithmetic.",
    "parameters": {
        "type": "object",
        "properties": {
            "a": {"type": "integer", "description": "first number"},
            "b": {"type": "integer", "description": "second number"},
        },
        "required": ["a", "b"],
    },
}]

# --- block 2 ---
messages = [{"role": "user", "content": "What's 4831 × 2907?"}]

while True:
    reply = model.generate(messages, tools=tools)   # model may answer OR request a tool

    if reply.tool_call is None:
        print(reply.text)                            # it's done — final answer
        break

    # the model asked for a tool — WE run it
    name, args = reply.tool_call.name, reply.tool_call.args
    result = TOOLS[name](**args)                      # e.g. multiply(4831, 2907) -> 14043717

    # feed the request AND its result back into context, then loop
    messages.append({"role": "assistant", "tool_call": reply.tool_call})
    messages.append({"role": "tool", "name": name, "content": str(result)})

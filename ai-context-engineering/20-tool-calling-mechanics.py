"""
AI Context Engineering
Chapter 20: Tool-Calling Mechanics
Section: Tools and MCP

Read this chapter: https://books.vizuara.ai/read/ai-context-engineering/tool-calling-mechanics

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
tools = [{
    "name": "get_weather",
    "description": "Get the current temperature for a city, in Celsius.",
    "input_schema": {
        "type": "object",
        "properties": {
            "city": {"type": "string", "description": "City name, e.g. 'Pune'"}
        },
        "required": ["city"]
    }
}]

# --- block 2 ---
def get_weather(city):
    return {"temp_c": 31, "conditions": "humid"}   # a real API call in practice

# --- block 3 ---
messages = [{"role": "user", "content": "Warmer in Pune or Nagpur?"}]
while True:
    reply = model.call(messages, tools=tools)
    if reply.stop_reason != "tool_use":
        break                              # model gave a final answer → done
    for call in reply.tool_calls:          # may be several at once
        result = run(call.name, call.input)
        messages.append(tool_result(call.id, result))

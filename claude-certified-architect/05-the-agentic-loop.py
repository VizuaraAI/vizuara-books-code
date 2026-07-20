"""
Claude Certified Architect (CCAF)
Chapter 5: The Agentic Loop, End to End
Section: The Claude Platform and the Agentic Loop

Read this chapter: https://books.vizuara.ai/read/claude-certified-architect/the-agentic-loop

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
messages = [
    {"role": "user", "content": "What should I wear in San Francisco today?"}
]

# --- block 2 ---
{"role": "assistant", "content": [
    {"type": "tool_use", "id": "toolu_01A", "name": "get_weather",
     "input": {"city": "San Francisco"}}
]}

# --- block 3 ---
{"role": "user", "content": [
    {"type": "tool_result", "tool_use_id": "toolu_01A",
     "content": "14°C, foggy, wind 20 km/h"}
]}

# --- block 4 ---
messages = [{"role": "user", "content": user_prompt}]

while True:
    resp = client.messages.create(model=MODEL, tools=TOOLS, messages=messages)
    messages.append({"role": "assistant", "content": resp.content})

    if resp.stop_reason != "tool_use":     # end_turn (or a stop) → we're done
        break

    tool_results = []
    for block in resp.content:
        if block.type == "tool_use":
            output = run_tool(block.name, block.input)   # YOUR code acts here
            tool_results.append({
                "type": "tool_result",
                "tool_use_id": block.id,
                "content": output,
            })
    messages.append({"role": "user", "content": tool_results})   # feed results back

final_text = messages[-1]["content"]

"""
Claude Certified Architect (CCAF)
Chapter 6: stop_reason: tool_use vs end_turn
Section: The Claude Platform and the Agentic Loop

Read this chapter: https://books.vizuara.ai/read/claude-certified-architect/stop-reason-and-turn-control

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
messages = [{"role": "user", "content": "What's the weather in Paris?"}]

while True:
    response = client.messages.create(
        model="claude-opus-4-1",
        max_tokens=1024,
        tools=tools,
        messages=messages,
    )
    messages.append({"role": "assistant", "content": response.content})

    if response.stop_reason == "tool_use":
        tool_results = run_requested_tools(response.content)   # execute each tool_use block
        messages.append({"role": "user", "content": tool_results})
        continue                                               # loop back for another turn

    break   # end_turn (or anything that isn't tool_use): we're done

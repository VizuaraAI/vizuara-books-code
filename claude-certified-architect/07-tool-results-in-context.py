"""
Claude Certified Architect (CCAF)
Chapter 7: Feeding Tool Results Back Into Context
Section: The Claude Platform and the Agentic Loop

Read this chapter: https://books.vizuara.ai/read/claude-certified-architect/tool-results-in-context

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
messages = [
    # 1. the human's original ask
    {"role": "user", "content": "What's the weather in Paris?"},

    # 2. Claude's response — it wants a tool (stop_reason was "tool_use")
    {"role": "assistant", "content": [
        {"type": "text", "text": "Let me check that."},
        {"type": "tool_use", "id": "toolu_01A", "name": "get_weather",
         "input": {"city": "Paris"}}
    ]},

    # 3. YOU append this: the tool's answer, keyed by tool_use_id
    {"role": "user", "content": [
        {"type": "tool_result", "tool_use_id": "toolu_01A",
         "content": "12°C, light rain"}
    ]},
]
# ...now send the ENTIRE array back to get turn 4.

"""
Harness Engineering
Chapter 8: Messages, turns & roles
Section: The Agent Loop

Read this chapter: https://books.vizuara.ai/read/harness-engineering/messages-turns-and-roles

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# Turn N: the model's assistant message contains a tool_use block
{
    "role": "assistant",
    "content": [
        {"type": "text", "text": "Let me check the test file."},
        {
            "type": "tool_use",
            "id": "toolu_01A9c",          # <-- the thread's handle
            "name": "read_file",
            "input": {"path": "test_math.py"},
        },
    ],
}

# Turn N (our reply): the tool_result must quote that same id back
{
    "role": "user",
    "content": [
        {
            "type": "tool_result",
            "tool_use_id": "toolu_01A9c",  # <-- must match, or the model is lost
            "content": "def test_add():\n    assert add(2, 2) == 5\n",
        },
    ],
}

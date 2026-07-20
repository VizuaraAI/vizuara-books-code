"""
Prompt Engineering
Chapter 15: System, User, and Assistant Messages
Section: The Prompting Toolbox

Read this chapter: https://books.vizuara.ai/read/prompt-engineering/system-user-assistant-messages

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
messages = [
    {"role": "system",    "content": "You are a terse assistant. Answer in one sentence."},
    {"role": "user",      "content": "Why is the sky blue?"},
]

# --- block 2 ---
system = """You are a support agent for a bike shop.
- Answer only questions about bikes, orders, and returns.
- If asked anything else, politely decline.
- Keep replies under 60 words. Use plain English."""

# --- block 3 ---
messages = [
    {"role": "system",    "content": "You are a helpful math tutor."},
    {"role": "user",      "content": "What is 8 times 7?"},
    {"role": "assistant", "content": "8 times 7 is 56."},
    {"role": "user",      "content": "Now add 4 to that."},
]

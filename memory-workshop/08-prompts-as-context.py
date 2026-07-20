"""
Memory in AI Systems
Chapter 8: Prompts: The Instruction Layer
Section: Context Engineering

Read this chapter: https://books.vizuara.ai/read/memory-workshop/prompts-as-context

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
messages = [
    {"role": "system", "content":
        "You are a patient math tutor for a 10-year-old. "
        "Never give the final numeric answer. Instead, ask one "
        "guiding question at a time. Keep replies under 40 words."},
    {"role": "user", "content":
        "What is 7 times 8?"},
]

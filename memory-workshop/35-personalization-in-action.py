"""
Memory in AI Systems
Chapter 35: Personalization in Action
Section: Building with Mem0

Read this chapter: https://books.vizuara.ai/read/memory-workshop/personalization-in-action

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from mem0 import Memory

memory = Memory()

messages = [
    {"role": "user", "content": "Explain gradient descent. I'm new to this and don't know calculus."},
    {"role": "assistant", "content": "Sure — think of it as walking downhill..."},
]
memory.add(messages, user_id="aisha")

# --- block 2 ---
hits = memory.search("what's a learning rate?", user_id="aisha", limit=5)

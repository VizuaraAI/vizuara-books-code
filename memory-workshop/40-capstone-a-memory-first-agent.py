"""
Memory in AI Systems
Chapter 40: Capstone: A Memory-First Agent
Section: Putting It Together

Read this chapter: https://books.vizuara.ai/read/memory-workshop/capstone-a-memory-first-agent

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from mem0 import Memory

memory = Memory()

messages = [
    {"role": "user", "content": "Oh, the chain rule finally clicked — "
                                 "it's just multiplying the local slopes."},
]
memory.add(messages, user_id="alex")

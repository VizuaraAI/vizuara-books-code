"""
Memory in AI Systems
Chapter 31: Introducing Mem0
Section: Building with Mem0

Read this chapter: https://books.vizuara.ai/read/memory-workshop/introducing-mem0

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from mem0 import Memory

m = Memory()

# WRITE: Mem0 extracts durable facts, embeds them, checks for
# conflicts, and updates-or-adds — all inside this one call.
m.add(
    "I've been doing everything in Python lately, JS isn't clicking for me",
    user_id="asha",
)

# --- block 2 ---
# READ: semantic search over ASHA's memories only.
results = m.search("what language should I use?", user_id="asha")
# -> [{"memory": "Prefers Python over JavaScript", "score": 0.61, ...}]

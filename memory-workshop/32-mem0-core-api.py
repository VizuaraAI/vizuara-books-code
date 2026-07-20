"""
Memory in AI Systems
Chapter 32: The Mem0 Core API: add, search, get
Section: Building with Mem0

Read this chapter: https://books.vizuara.ai/read/memory-workshop/mem0-core-api

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from mem0 import Memory

m = Memory()   # spins up a default embedder + vector store + LLM under the hood

# --- block 2 ---
messages = [
    {"role": "user", "content": "Hi! I'm learning Python and I really struggle with recursion."},
    {"role": "assistant", "content": "Great, recursion trips up a lot of people. Let's start slow."},
]

m.add(messages, user_id="alice")

# --- block 3 ---
m.add([
    {"role": "user", "content": "Actually I've gotten comfortable with recursion now — it's decorators I can't get."}
], user_id="alice")

# --- block 4 ---
results = m.search("How should I explain closures to Alice?", user_id="alice")

for r in results["results"]:
    print(r["memory"], "→", round(r["score"], 2))

# --- block 5 ---
everything = m.get_all(user_id="alice")   # list of all Alice's memories
for item in everything["results"]:
    print(item["id"], item["memory"])

one = m.get(memory_id="a1b2-…")           # a single memory by id

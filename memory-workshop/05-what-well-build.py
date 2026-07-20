"""
Memory in AI Systems
Chapter 5: What We'll Build in This Book
Section: Why Memory Matters

Read this chapter: https://books.vizuara.ai/read/memory-workshop/what-well-build

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- resolved names (added so this file passes a static check) ---
# The names below are used by this chapter but not defined in it.
# Imports point at context.py, which copies the earlier chapter verbatim.
# Stubs are deliberately empty: the book expects YOU to supply them.
messages = []  # TODO: the conversation turns to remember - see ch.2: https://books.vizuara.ai/read/memory-workshop/what-is-memory-in-llms
# --- end resolved names ---

# --- block 1 ---
import numpy as np

def cosine(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

q  = np.array([0.9, 0.1])
m1 = np.array([0.8, 0.2])   # "user struggles with for loops"
m2 = np.array([0.1, 0.9])   # "user likes hiking"

cosine(q, m1)   # ≈ 0.991  → highly relevant, retrieve this
cosine(q, m2)   # ≈ 0.220  → unrelated, skip

# --- block 2 ---
from mem0 import Memory
m = Memory()

m.add(messages, user_id="alice")          # extract + store new facts (the WRITE step)
m.search("what is alice studying?",       # semantic top-k over alice's memories (READ)
         user_id="alice")
m.get_all(user_id="alice")                # read everything we know about alice

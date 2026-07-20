"""
Data Structures & Algorithms in Python
Chapter 44: Introduction to the Queue
Section: Stacks & Queues

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/introduction-to-queues

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
queue = []
queue.append("A")     # enqueue at the back  — O(1) amortized  ✅
queue.append("B")
front = queue.pop(0)   # dequeue from the front — O(n)  ❌ hidden cost

# --- block 2 ---
from collections import deque

q = deque()
q.append("A")      # enqueue at the back   — O(1)
q.append("B")
q.append("C")
front = q.popleft()  # dequeue from the front — O(1)   → "A"

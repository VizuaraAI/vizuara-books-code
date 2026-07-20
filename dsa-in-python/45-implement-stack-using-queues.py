"""
Data Structures & Algorithms in Python
Chapter 45: Implement a Stack Using Queues
Section: Stacks & Queues

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/implement-stack-using-queues

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)                       # enqueue to the back
        for _ in range(len(self.q) - 1):       # rotate every older element
            self.q.append(self.q.popleft())    # behind the new one

    def pop(self) -> int:
        return self.q.popleft()                # front == newest

    def top(self) -> int:
        return self.q[0]                       # peek the front

    def empty(self) -> bool:
        return len(self.q) == 0

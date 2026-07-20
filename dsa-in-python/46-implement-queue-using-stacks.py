"""
Data Structures & Algorithms in Python
Chapter 46: Implement a Queue Using Stacks
Section: Stacks & Queues

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/implement-queue-using-stacks

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
class MyQueue:
    def __init__(self):
        self.in_stack = []   # inbox: enqueue pushes here
        self.out_stack = []  # outbox: dequeue pops here

    def enqueue(self, x):
        self.in_stack.append(x)          # O(1): just push on top

    def _transfer(self):
        if not self.out_stack:           # only when the outbox is empty
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def dequeue(self):
        self._transfer()
        return self.out_stack.pop()      # oldest element sits on top

    def peek(self):
        self._transfer()
        return self.out_stack[-1]

    def empty(self):
        return not self.in_stack and not self.out_stack

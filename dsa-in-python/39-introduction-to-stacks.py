"""
Data Structures & Algorithms in Python
Chapter 39: Introduction to the Stack
Section: Stacks & Queues

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/introduction-to-stacks

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
stack = []

stack.append(3)      # push  -> [3]
stack.append(1)      # push  -> [3, 1]
stack.append(4)      # push  -> [3, 1, 4]

top = stack[-1]      # peek  -> 4  (stack unchanged)
print(stack.pop())   # pop   -> prints 4, stack is now [3, 1]

is_empty = not stack # True when the list is empty

# --- block 2 ---
class Stack:
    def __init__(self):
        self._items = []

    def push(self, x):
        self._items.append(x)          # O(1)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()       # O(1)

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]         # O(1)

    def is_empty(self):
        return len(self._items) == 0   # O(1)

    def __len__(self):
        return len(self._items)

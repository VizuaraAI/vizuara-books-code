"""
Data Structures & Algorithms in Python
Chapter 47: Reverse First K Elements of a Queue
Section: Stacks & Queues

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/reverse-first-k-elements-of-queue

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from collections import deque

def reverse_first_k(queue: deque, k: int) -> deque:
    if k < 0 or k > len(queue):
        raise ValueError("k must be between 0 and len(queue)")

    stack = []                       # our reversing machine (LIFO)

    # Step 1: dequeue the first k, push onto the stack
    for _ in range(k):
        stack.append(queue.popleft())

    # Step 2: pop the stack, enqueue at the back (arrives reversed)
    while stack:
        queue.append(stack.pop())

    # Step 3: rotate the remaining n - k elements to the back
    for _ in range(len(queue) - k):
        queue.append(queue.popleft())

    return queue

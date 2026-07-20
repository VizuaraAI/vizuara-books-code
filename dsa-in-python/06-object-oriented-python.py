"""
Data Structures & Algorithms in Python
Chapter 6: Object-Oriented Python for Data Structures
Section: Foundations & Python Refresher

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/object-oriented-python

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
class Node:
    def __init__(self, value):
        self.value = value   # the data this node carries
        self.next = None     # a reference to the next node (nothing yet)

# --- block 2 ---
a = Node(7)
b = Node(9)
a.next = b        # a's "next" now points at b
print(a.value)          # 7
print(a.next.value)     # 9  — we hopped from a to b and read b's value

# --- block 3 ---
class Stack:
    def __init__(self):
        self.items = []          # the underlying storage

    def push(self, x):
        self.items.append(x)     # add on top

    def pop(self):
        return self.items.pop()  # remove and return the top

    def peek(self):
        return self.items[-1]    # look at the top, don't remove

    def is_empty(self):
        return len(self.items) == 0

# --- block 4 ---
s = Stack()
for x in (3, 8, 5):
    s.push(x)
print(s.pop())   # 5
print(s.pop())   # 8
print(s.peek())  # 3  — still there, not removed

# --- block 5 ---
s = Stack()
t = Stack()
s.push(1); s.push(2)   # s.items is now [1, 2]
t.push(9)              # t.items is now [9]
print(s.pop())   # 2  (pops from s only)
print(t.pop())   # 9  (t was never disturbed)
print(s.pop())   # 1  (s still has its own state)

# --- block 6 ---
class Stack:
    def __init__(self):
        self.items = []
    def __repr__(self):
        return f"Stack(top→bottom: {self.items[::-1]})"
    # ...push, pop, peek as before...

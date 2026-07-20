"""
Python for Data Science
Chapter 11: Lists: The Workhorse
Section: Data Structures in Python

Read this chapter: https://books.vizuara.ai/read/python-for-data-science/lists-the-workhorse

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
scores = [88, 92, 79, 95, 61]
mixed  = ["ada", 36, True, 3.14]   # a list can hold anything, even mixed types
empty  = []                         # or list()

# --- block 2 ---
scores = [88, 92, 79, 95, 61]
scores[1]        # 92        — one item
scores[1:3]      # [92, 79]  — indices 1 and 2, but NOT 3
scores[:2]       # [88, 92]  — from the start up to (not incl.) index 2
scores[2:]       # [79, 95, 61] — from index 2 to the end
scores[:]        # [88, 92, 79, 95, 61] — a full (shallow) copy

# --- block 3 ---
nums = [10, 20]
nums.append(30)      # nums is now [10, 20, 30]
nums.append([40, 50])# nums is now [10, 20, 30, [40, 50]] — a nested list!

# --- block 4 ---
a = [1, 2, 3]
a.extend([4, 5])     # a is now [1, 2, 3, 4, 5] — flattened in
a.insert(0, 99)      # a is now [99, 1, 2, 3, 4, 5] — insert AT index 0

# --- block 5 ---
q = [10, 20, 30, 40]
last = q.pop()       # last = 40, q is now [10, 20, 30]
first = q.pop(0)     # first = 10, q is now [20, 30]
q.remove(30)         # q is now [20] — deletes the value 30, not index 30

# --- block 6 ---
original = [1, 2, 3]
alias = original        # NOT a copy — both names point to ONE list
alias.append(4)
print(original)         # [1, 2, 3, 4]  ← surprise! we never touched `original`

# --- block 7 ---
nums = [3, 8, 5, 12, 7]
evens = []                    # 1. start with an empty accumulator
for n in nums:                # 2. walk the source, one item at a time
    if n % 2 == 0:            # 3. test each candidate
        evens.append(n)       # 4. keep the ones that pass
# evens is now [8, 12]

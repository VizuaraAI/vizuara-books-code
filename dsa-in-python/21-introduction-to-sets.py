"""
Data Structures & Algorithms in Python
Chapter 21: Introduction to Sets
Section: Strings, Sets & Dictionaries

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/introduction-to-sets

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
guests = ["ana", "raj", "mo", "kim"]
"raj" in guests     # True  — but Python checked "ana", then "raj"
"zoe" in guests     # False — Python checked all four and gave up

# --- block 2 ---
hash("raj")      # some large integer, e.g. 8127346551029384756
hash(42)         # 42  (small ints hash to themselves in CPython)

# --- block 3 ---
s = {3, 1, 2}          # a set literal (curly braces, no key:value pairs)
empty = set()          # {} is an empty DICT, not a set — a classic trap
s.add(4)               # O(1) average
s.discard(1)           # O(1) average, no error if absent
4 in s                 # O(1) average membership — the whole point
len(s)                 # O(1)

# --- block 4 ---
nums = [4, 2, 4, 1, 2, 4]
unique = set(nums)          # {1, 2, 4}  — repeats gone, one pass
len(unique)                 # 3 distinct values

# --- block 5 ---
ana = {"math", "cs", "art"}
raj = {"cs", "art", "bio"}

ana | raj      # union: everything either took  -> {'math','cs','art','bio'}
ana & raj      # intersection: what BOTH took   -> {'cs', 'art'}
ana - raj      # difference: what only ana took -> {'math'}

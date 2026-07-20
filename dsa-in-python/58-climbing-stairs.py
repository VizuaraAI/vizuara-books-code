"""
Data Structures & Algorithms in Python
Chapter 58: Climbing Stairs
Section: Recursion & Backtracking

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/climbing-stairs

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def climb_naive(n):
    if n <= 2:          # ways(1)=1, ways(2)=2
        return n
    return climb_naive(n - 1) + climb_naive(n - 2)

# --- block 2 ---
def climb_memo(n, cache=None):
    if cache is None:
        cache = {}
    if n <= 2:
        return n
    if n in cache:                       # already solved? just return it
        return cache[n]
    cache[n] = climb_memo(n - 1, cache) + climb_memo(n - 2, cache)
    return cache[n]

# --- block 3 ---
def climb(n):
    if n <= 2:
        return n
    prev, curr = 1, 2          # ways(1)=1, ways(2)=2
    for _ in range(3, n + 1):
        prev, curr = curr, prev + curr   # slide the two-number window up
    return curr

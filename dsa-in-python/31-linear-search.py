"""
Data Structures & Algorithms in Python
Chapter 31: Linear Search
Section: Searching, Sorting & Bit Manipulation

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/linear-search

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i          # found it — hand back the position
    return -1                 # walked the whole list, never matched

# --- block 2 ---
def find_all(nums, target):
    return [i for i in range(len(nums)) if nums[i] == target]

# --- block 3 ---
def find_first_where(nums, predicate):
    for i, x in enumerate(nums):
        if predicate(x):
            return i
    return -1

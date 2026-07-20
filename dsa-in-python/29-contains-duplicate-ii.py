"""
Data Structures & Algorithms in Python
Chapter 29: Contains Duplicate II (Leetcode 219)
Section: Two Pointers & Sliding Window

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/contains-duplicate-ii

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def near_duplicate_brute(nums, k):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j] and abs(i - j) <= k:
                return True
    return False

# --- block 2 ---
def contains_nearby_duplicate(nums, k):
    seen = set()                 # values in the current window (last k elements)
    for i, value in enumerate(nums):
        if value in seen:        # a twin is still within k positions behind us
            return True
        seen.add(value)
        if i >= k:               # window is now full: drop the element that fell off
            seen.discard(nums[i - k])
    return False

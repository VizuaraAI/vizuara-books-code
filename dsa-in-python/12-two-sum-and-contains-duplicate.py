"""
Data Structures & Algorithms in Python
Chapter 12: Two Sum & Contains Duplicate
Section: Arrays & Matrices

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/two-sum-and-contains-duplicate

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def two_sum_brute(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):     # j starts after i, no reused element
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# --- block 2 ---
def two_sum(nums, target):
    seen = {}                          # value -> index of everything passed so far
    for i, x in enumerate(nums):
        complement = target - x
        if complement in seen:         # average O(1) membership test
            return [seen[complement], i]
        seen[x] = i                    # remember x for a future partner
    return []

# --- block 3 ---
def contains_duplicate(nums):
    seen = set()
    for x in nums:
        if x in seen:                  # O(1) average membership
            return True
        seen.add(x)
    return False

# --- block 4 ---
def contains_duplicate_short(nums):
    return len(set(nums)) < len(nums)  # fewer uniques than elements → a repeat exists

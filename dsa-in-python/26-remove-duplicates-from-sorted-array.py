"""
Data Structures & Algorithms in Python
Chapter 26: Remove Duplicates from a Sorted Array
Section: Two Pointers & Sliding Window

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/remove-duplicates-from-sorted-array

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def dedupe(nums):
    return list(dict.fromkeys(nums))   # order-preserving unique

# --- block 2 ---
def remove_duplicates(nums):
    if not nums:
        return 0
    slow = 0                          # last position holding a unique value
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:  # a new value → start of a new run
            slow += 1
            nums[slow] = nums[fast]   # write it into the clean prefix
    return slow + 1                   # count = index + 1

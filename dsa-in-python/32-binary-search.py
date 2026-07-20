"""
Data Structures & Algorithms in Python
Chapter 32: Binary Search on a Sorted Array
Section: Searching, Sorting & Bit Manipulation

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/binary-search

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
nums = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72]   # indices 0..9, sorted
target = 23

# --- block 2 ---
def binary_search(nums, target):
    low, high = 0, len(nums) - 1        # inclusive window: indices low..high
    while low <= high:                  # trap 1: <= , not <
        mid = low + (high - low) // 2   # trap 2: overflow-safe midpoint
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1               # trap 3: + 1, never leave mid in range
        else:
            high = mid - 1              # trap 3: - 1, never leave mid in range
    return -1                           # window emptied → not present

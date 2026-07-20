"""
Data Structures & Algorithms in Python
Chapter 34: Selection Sort
Section: Searching, Sorting & Bit Manipulation

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/selection-sort

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def selection_sort(nums):
    n = len(nums)
    for i in range(n - 1):            # boundary: nums[:i] is sorted
        min_idx = i                   # assume the boundary itself is smallest
        for j in range(i + 1, n):     # scan the rest of the suffix
            if nums[j] < nums[min_idx]:
                min_idx = j           # found a new minimum — remember WHERE
        if min_idx != i:              # only swap if we actually found something smaller
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums

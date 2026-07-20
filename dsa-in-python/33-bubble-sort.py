"""
Data Structures & Algorithms in Python
Chapter 33: Bubble Sort
Section: Searching, Sorting & Bit Manipulation

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/bubble-sort

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# NOTE: this block is prose in the book, not runnable code.
# It is the compare-and-swap step lifted out of bubble_sort's inner loop and shown
# in isolation; `nums` and `j` are bound by that loop (block 2 below), not by this
# block. Kept verbatim but commented out.
# if nums[j] > nums[j + 1]:
#     nums[j], nums[j + 1] = nums[j + 1], nums[j]   # Python swap, no temp needed

# --- block 2 ---
def bubble_sort(nums):
    n = len(nums)
    for i in range(n):                       # n passes
        for j in range(n - 1 - i):           # inner scan shrinks each pass
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

# --- block 3 ---
def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:          # a clean pass ⇒ already sorted ⇒ bail out
            break
    return nums

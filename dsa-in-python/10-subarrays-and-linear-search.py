"""
Data Structures & Algorithms in Python
Chapter 10: Generate All Subarrays & Search Unsorted
Section: Arrays & Matrices

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/subarrays-and-linear-search

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def all_subarrays(arr):
    result = []
    n = len(arr)
    for i in range(n):            # start index
        for j in range(i, n):     # end index, never before the start
            result.append(arr[i:j+1])
    return result

all_subarrays([3, 1, 4, 2])
# [[3], [3, 1], [3, 1, 4], [3, 1, 4, 2],
#  [1], [1, 4], [1, 4, 2],
#  [4], [4, 2],
#  [2]]

# --- block 2 ---
def print_subarray_sums(arr):
    n = len(arr)
    for i in range(n):
        running = 0
        for j in range(i, n):
            running += arr[j]          # extend the window by one, O(1)
            print(arr[i:j+1], "->", running)

# --- block 3 ---
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i        # found it — stop immediately
    return -1               # fell off the end — not present

linear_search([3, 1, 4, 2], 4)   # -> 2
linear_search([3, 1, 4, 2], 9)   # -> -1

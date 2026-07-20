"""
Data Structures & Algorithms in Python
Chapter 9: Reverse an Array & Rotate by D Places
Section: Arrays & Matrices

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/reverse-and-rotate-an-array

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def reverse_in_place(a):
    left, right = 0, len(a) - 1
    while left < right:
        a[left], a[right] = a[right], a[left]   # swap, no temp needed
        left += 1
        right -= 1
    return a

# --- block 2 ---
def reverse_range(a, lo, hi):
    while lo < hi:
        a[lo], a[hi] = a[hi], a[lo]
        lo += 1
        hi -= 1

def rotate_left(a, d):
    n = len(a)
    d %= n                      # normalize: rotating by d and by d % n are identical
    reverse_range(a, 0, d - 1)      # reverse the first d
    reverse_range(a, d, n - 1)      # reverse the last n - d
    reverse_range(a, 0, n - 1)      # reverse the whole array
    return a

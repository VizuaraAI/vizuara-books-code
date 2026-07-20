"""
Data Structures & Algorithms in Python
Chapter 37: Counting Bits
Section: Searching, Sorting & Bit Manipulation

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/counting-bits

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def count_ones(x):
    count = 0
    while x:
        x &= x - 1      # clear the lowest set bit
        count += 1
    return count

# --- block 2 ---
def count_bits_brute(n):
    return [count_ones(i) for i in range(0, n + 1)]

# --- block 3 ---
def count_bits(n):
    bits = [0] * (n + 1)          # bits[0] = 0 is our base case
    for i in range(1, n + 1):
        bits[i] = bits[i >> 1] + (i & 1)
    return bits

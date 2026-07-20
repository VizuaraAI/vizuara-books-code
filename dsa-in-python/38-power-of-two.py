"""
Data Structures & Algorithms in Python
Chapter 38: Power of Two
Section: Searching, Sorting & Bit Manipulation

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/power-of-two

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def is_power_of_two_slow(n):
    if n <= 0:
        return False
    while n % 2 == 0:   # while it's still even, halve it
        n //= 2
    return n == 1       # a pure power of two collapses all the way to 1

# --- block 2 ---
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# --- block 3 ---
for n in range(0, 9):
    print(n, is_power_of_two(n))
# 0 False   1 True    2 True    3 False
# 4 True    5 False   6 False   7 False   8 True

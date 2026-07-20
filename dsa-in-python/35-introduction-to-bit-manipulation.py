"""
Data Structures & Algorithms in Python
Chapter 35: Introduction to Bit Manipulation
Section: Searching, Sorting & Bit Manipulation

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/introduction-to-bit-manipulation

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
#   1100   (12)        1100   (12)        1100   (12)
# & 0101   (5)       | 0101   (5)       ^ 0101   (5)
# ------              ------              ------
#   0100   (4)         1101   (13)        1001   (9)

# --- block 2 ---
def is_kth_bit_set(n, k):
    return ((n >> k) & 1) == 1   # parentheses matter: & binds looser than ==

# read every bit of 13, from LSB up
n = 13
for k in range(4):
    print(k, is_kth_bit_set(n, k))
# 0 True   1 False   2 True   3 True   ->  1 1 0 1  (read bottom-up)

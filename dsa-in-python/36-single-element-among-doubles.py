"""
Data Structures & Algorithms in Python
Chapter 36: Single Element Among Doubles
Section: Searching, Sorting & Bit Manipulation

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/single-element-among-doubles

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
nums = [4, 1, 2, 1, 2]   # answer: 4

# --- block 2 ---
def single_number(nums):
    result = 0
    for x in nums:
        result ^= x        # fold each element into the running XOR
    return result

# --- block 3 ---
from functools import reduce
from operator import xor

def single_number(nums):
    return reduce(xor, nums, 0)   # seed with 0, XOR everything together

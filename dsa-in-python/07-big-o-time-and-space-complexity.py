"""
Data Structures & Algorithms in Python
Chapter 7: Big-O: Time & Space Complexity
Section: Foundations & Python Refresher

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/big-o-time-and-space-complexity

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def count_even_sum_pairs(nums):
    n = len(nums)          # 1 step
    count = 0              # 1 step
    for i in range(n):            # outer loop runs n times
        for j in range(i + 1, n): # inner loop, ~n times each
            if (nums[i] + nums[j]) % 2 == 0:  # constant work
                count += 1
    return count           # 1 step

# --- block 2 ---
def total(nums):
    s = 0                 # one extra variable, regardless of n
    for x in nums:
        s += x
    return s              # O(n) time, O(1) space

# --- block 3 ---
def doubled(nums):
    out = []              # a new list that will hold n elements
    for x in nums:
        out.append(x * 2)
    return out            # O(n) time, O(n) space

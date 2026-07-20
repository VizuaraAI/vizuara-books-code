"""
Data Structures & Algorithms in Python
Chapter 1: Why Data Structures & Algorithms?
Section: Foundations & Python Refresher

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/why-data-structures-and-algorithms

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def two_sum(nums, target):
    seen = {}                       # value -> index we've already passed
    for i, num in enumerate(nums):
        need = target - num         # the partner that would complete the pair
        if need in seen:            # O(1) average lookup, not an O(n) scan
            return [seen[need], i]
        seen[num] = i               # remember this number for a future partner
    return None

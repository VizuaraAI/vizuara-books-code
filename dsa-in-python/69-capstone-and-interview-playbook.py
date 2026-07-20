"""
Data Structures & Algorithms in Python
Chapter 69: Capstone: The Interview Playbook
Section: Greedy Algorithms & Capstone

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/capstone-and-interview-playbook

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def two_sum(nums, target):
    seen = {}                      # value -> index, for everything to our left
    for i, x in enumerate(nums):
        need = target - x          # the partner that would complete the pair
        if need in seen:           # have we already passed it? O(1) lookup
            return [seen[need], i]
        seen[x] = i                # record x for future indices
    return []                      # no pair (constraint said a pair exists, but be safe)

"""
Data Structures & Algorithms in Python
Chapter 61: Find All Permutations
Section: Recursion & Backtracking

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/find-all-permutations

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def permutations(nums):
    result = []

    def backtrack(current, remaining):
        if not remaining:              # leaf: nothing left to place
            result.append(current[:])  # copy — current keeps mutating!
            return
        for i in range(len(remaining)):
            chosen = remaining[i]
            # CHOOSE: commit this element to the current prefix
            current.append(chosen)
            # RECURSE: solve the smaller problem without it
            backtrack(current, remaining[:i] + remaining[i+1:])
            # UNDO: take it back so the loop can try the next candidate
            current.pop()

    backtrack([], nums)
    return result

# --- block 2 ---
def permutations_swap(nums):
    result = []

    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])     # a full permutation is fixed
            return
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]   # CHOOSE: bring i to front
            backtrack(start + 1)                          # RECURSE: fix the rest
            nums[start], nums[i] = nums[i], nums[start]   # UNDO: swap back

    backtrack(0)
    return result

"""
Data Structures & Algorithms in Python
Chapter 59: Generate All Subsequences
Section: Recursion & Backtracking

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/generate-all-subsequences

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def subsequences(arr):
    result = []

    def helper(i, path):
        if i == len(arr):        # base case: every element decided
            result.append(path[:])   # record a COPY of the finished subsequence
            return
        # decision 1: include arr[i]
        path.append(arr[i])
        helper(i + 1, path)
        path.pop()               # UNDO — backtrack before trying the other branch
        # decision 2: exclude arr[i]
        helper(i + 1, path)

    helper(0, [])
    return result

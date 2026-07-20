"""
Data Structures & Algorithms in Python
Chapter 56: Introduction to Recursion
Section: Recursion & Backtracking

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/introduction-to-recursion

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def sum_to(n):
    if n == 1:          # base case: smallest problem, answer directly
        return 1
    return n + sum_to(n - 1)   # recursive case: lean on a smaller copy

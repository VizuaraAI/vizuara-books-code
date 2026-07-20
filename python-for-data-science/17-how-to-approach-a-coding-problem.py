"""
Python for Data Science
Chapter 17: How to Approach a Coding Problem
Section: Problem-Solving with Coding Challenges

Read this chapter: https://books.vizuara.ai/read/python-for-data-science/how-to-approach-a-coding-problem

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# 1. if the list is empty -> return 0   (handle the special case first)
# 2. add up all the numbers -> total
# 3. count how many numbers there are -> n
# 4. return total / n

# --- block 2 ---
def average(numbers):
    if not numbers:          # empty list is falsy -> guard clause
        return 0
    total = sum(numbers)     # 2. add them all up
    n = len(numbers)         # 3. how many there are
    return total / n         # 4. true division -> a float

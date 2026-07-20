"""
Data Structures & Algorithms in Python
Chapter 4: Variables, Data Types, Casting & Operators
Section: Foundations & Python Refresher

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/variables-types-and-operators

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- placeholder added so this file runs standalone (not book code) ---
some_long_list = []  # TODO: block 3 loops over a long sequence of characters the
                     # reader supplies - see
                     # https://books.vizuara.ai/read/dsa-in-python/variables-types-and-operators

# --- block 1 ---
nums = [4, 7, 2, 9, 6]
even_count = sum(n % 2 == 0 for n in nums)  # True counts as 1
print(even_count)   # 3

# --- block 2 ---
a = "3"
total = int(a) + 4      # cast the string to int first → 7
label = a + str(4)      # or cast the int to str → "34"
print(total, label)     # 7 34

# --- block 3 ---
# The O(n²) trap — looks innocent, scales terribly
s = ""
for ch in some_long_list:
    s += ch          # each += copies the ENTIRE string so far

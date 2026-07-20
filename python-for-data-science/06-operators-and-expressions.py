"""
Python for Data Science
Chapter 6: Operators and Expressions
Section: Python Fundamentals

Read this chapter: https://books.vizuara.ai/read/python-for-data-science/operators-and-expressions

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
2 + 3        # 5
10 - 4       # 6
6 * 7        # 42

# --- block 2 ---
7 / 2        # 3.5   ← true division, always a float
7 // 2       # 3     ← floor division, rounds down
10 / 2       # 5.0   ← note the .0: still a float!

# --- block 3 ---
3 + 4 * 2    # 4*2 = 8 first, then 3+8 = 11
(3 + 4) * 2  # parentheses force the addition first → 14

# --- block 4 ---
5 > 3        # True    greater than
5 < 3        # False   less than
5 >= 5       # True    greater than or equal
5 <= 4       # False   less than or equal
5 == 5       # True    EQUAL — note the double =
5 != 3       # True    not equal

# --- block 5 ---
age = 20
is_member = True

age >= 18 and is_member       # True and True  → True
age >= 65 or is_member        # False or True  → True
not is_member                 # False

# --- block 6 ---
age = 25
score = 88

age >= 18 and score >= 50 and age < 120
# → True and True and True → True

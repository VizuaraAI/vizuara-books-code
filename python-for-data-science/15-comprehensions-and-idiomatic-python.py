"""
Python for Data Science
Chapter 15: Comprehensions and Idiomatic Python
Section: Data Structures in Python

Read this chapter: https://books.vizuara.ai/read/python-for-data-science/comprehensions-and-idiomatic-python

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
numbers = [1, 2, 3, 4]
squares = []
for n in numbers:
    squares.append(n * n)
# squares -> [1, 4, 16]  ... wait

# --- block 2 ---
numbers = [1, 2, 3, 4]
squares = [n * n for n in numbers]
# squares -> [1, 4, 9, 16]

# --- block 3 ---
evens_squared = []
for n in numbers:
    if n % 2 == 0:
        evens_squared.append(n * n)

# --- block 4 ---
evens_squared = [n * n for n in numbers]        # no filter: [1, 4, 9, 16]
evens_squared = [n * n for n in numbers if n % 2 == 0]  # -> [4, 16]

# --- block 5 ---
square_of = {n: n * n for n in numbers}
# -> {1: 1, 2: 4, 3: 9, 4: 16}

# --- block 6 ---
words = ["cat", "dog", "cat", "bird", "dog"]
lengths = {len(w) for w in words}
# -> {3, 4}

# --- block 7 ---
names = ["ana", "ben", "cy"]
scores = [90, 75, 88]
score_of = {name: score for name, score in zip(names, scores)}
# -> {"ana": 90, "ben": 75, "cy": 88}

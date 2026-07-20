"""
Python for Data Science
Chapter 12: Tuples and Immutability
Section: Data Structures in Python

Read this chapter: https://books.vizuara.ai/read/python-for-data-science/tuples-and-immutability

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def find_min_location(data):
    # ... scan the data ...
    return (2, 5)          # min is at row 2, column 5

# --- block 2 ---
point = (48.85, 2.35)
rgb   = (255, 128, 0)
row   = ("Ada", 1815, "mathematician")

# --- block 3 ---
just_parens = (5)      # this is just the integer 5!
one_tuple   = (5,)     # THIS is a one-element tuple

# --- block 4 ---
pair = 48.85, 2.35     # perfectly valid — this is a tuple
print(type(pair))      # <class 'tuple'>

# --- block 5 ---
def stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

lo, hi, avg = stats([3, 9, 4, 1])
print(lo, hi, avg)     # 1 9 4.25

# --- block 6 ---
grid = {}
grid[(2, 5)] = "wall"        # tuple key: row 2, col 5
grid[(0, 0)] = "start"
print(grid[(2, 5)])          # wall

# --- block 7 ---
record = ("Ada", 1815, "mathematician")
print(record[0])       # Ada
print(record[-1])      # mathematician
print(record[0:2])     # ('Ada', 1815)   -- a slice of a tuple is a tuple
print(len(record))     # 3
print(1815 in record)  # True

# --- block 8 ---
record = ("Ada", 1815, "mathematician")
updated = ("Grace",) + record[1:]     # a NEW tuple; the old one is untouched
print(updated)                        # ('Grace', 1815, 'mathematician')

# --- block 9 ---
row = ("Ada", [90, 85])       # a name and a list of scores
row[1].append(100)            # NOT touching a slot, reaching inside one
print(row)                    # ('Ada', [90, 85, 100])

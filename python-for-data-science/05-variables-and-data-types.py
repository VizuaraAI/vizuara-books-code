"""
Python for Data Science
Chapter 5: Variables and Data Types
Section: Python Fundamentals

Read this chapter: https://books.vizuara.ai/read/python-for-data-science/variables-and-data-types

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- stubs (not book code) ---
# The chapter uses these names without defining them. Placeholders so the file runs.
scores = []  # TODO: your own list of scores - block 7 shows how an empty list

# --- block 1 ---
age = 30

# --- block 2 ---
x = 5
print(type(x))       # <class 'int'>
x = "hello"
print(type(x))       # <class 'str'>

# --- block 3 ---
total = 90 + 82 + 77      # 249, an int
count = 3                 # an int
average = total / count   # 83.0  -> a FLOAT, not an int

# --- block 4 ---
print(0.1 + 0.2)          # 0.30000000000000004
print(0.1 + 0.2 == 0.3)   # False

# --- block 5 ---
a = [1, 2, 3]     # a points at a list object
b = a             # b points at the SAME list, not a copy
b.append(4)       # we mutate the shared object through b
print(a)          # [1, 2, 3, 4]  -> a "changed" too!

# --- block 6 ---
a = [1, 2, 3]
b = [1, 2, 3]     # same contents, but a brand-new object
print(a == b)     # True  -> same value
print(a is b)     # False -> two different objects!
c = a
print(c is a)     # True  -> c and a are the SAME object

# --- stub added to make this file runnable ---
             # is falsy. See
             # https://books.vizuara.ai/read/python-for-data-science/variables-and-data-types

# --- block 7 ---
if scores:          # truthy if the list has ANY items
    print("we have data")
else:
    print("empty!")  # runs only when scores is []

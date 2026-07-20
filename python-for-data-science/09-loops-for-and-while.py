"""
Python for Data Science
Chapter 9: Loops: for and while
Section: Python Fundamentals

Read this chapter: https://books.vizuara.ai/read/python-for-data-science/loops-for-and-while

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
total = 12 + 15 + 9 + 20 + 14

# --- block 2 ---
temps = [12, 15, 9, 20, 14]
total = 0
for t in temps:
    total = total + t
print(total)   # 70

# --- block 3 ---
for i in range(5):
    print(i)     # prints 0 1 2 3 4, one per line

# --- block 4 ---
days = ["Mon", "Tue", "Wed"]
for i, day in enumerate(days):
    print(i, day)   # 0 Mon  /  1 Tue  /  2 Wed

# --- block 5 ---
n = 100
steps = 0
while n > 1:
    n = n // 2      # floor division: drop the remainder
    steps = steps + 1
print(steps)        # 6

# --- block 6 ---
n = 100
while n > 1:
    steps = steps + 1   # BUG: we never shrink n!

# --- block 7 ---
for t in [12, 15, 9, 20, 14]:
    if t < 0:
        continue          # skip bad readings
    if t > 18:
        print("hot day:", t)
        break             # stop at the first hot day

# --- block 8 ---
temps = [12, 15, 9, 20, 14]
warm = []                       # the new list, starts empty
for t in temps:
    if t > 15:
        warm.append(f"{t} degrees (warm)")
print(warm)                     # ['20 degrees (warm)']

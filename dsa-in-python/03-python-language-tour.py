"""
Data Structures & Algorithms in Python
Chapter 3: A Fast Tour of the Python Language
Section: Foundations & Python Refresher

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/python-language-tour

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
total = 0
for x in range(5):
    total += x
print(total)   # 10

# --- block 2 ---
a = [1, 2, 3]
b = a          # NOT a copy — b is a second label on the SAME list
b.append(4)
print(a)       # [1, 2, 3, 4]  ← a changed too!

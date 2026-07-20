"""
Python for Data Science
Chapter 37: Course-End Test and Self-Check
Section: Wrap-Up and Next Steps

Read this chapter: https://books.vizuara.ai/read/python-for-data-science/course-end-test-and-self-check

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
a = [1, 2, 3]
b = a
b.append(4)
print(a)

# --- block 2 ---
squares = []
for n in range(1, 6):
    if n % 2 == 1:
        squares.append(n * n)

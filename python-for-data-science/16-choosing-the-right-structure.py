"""
Python for Data Science
Chapter 16: Choosing the Right Data Structure
Section: Data Structures in Python

Read this chapter: https://books.vizuara.ai/read/python-for-data-science/choosing-the-right-structure

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
words = "the cat sat on the mat the cat".split()

counts = []          # a list of [word, count] pairs
for w in words:
    found = False
    for pair in counts:        # scan the whole list every time
        if pair[0] == w:
            pair[1] += 1
            found = True
            break
    if not found:
        counts.append([w, 1])

# --- block 2 ---
words = "the cat sat on the mat the cat".split()

counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
# counts -> {'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1}

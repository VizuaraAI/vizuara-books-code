"""
Data Structures & Algorithms in Python
Chapter 23: Introduction to Python Dictionaries
Section: Strings, Sets & Dictionaries

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/introduction-to-dictionaries

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
d = {}
d[("row", 2)] = "cell"     # tuple of immutables → fine as a key
d[[1, 2]] = "oops"         # TypeError: unhashable type: 'list'

# --- block 2 ---
prices = {"pen": 10, "book": 250, "eraser": 5}

prices["book"]            # 250            → average O(1) lookup
prices["pen"] = 12        # update in place → average O(1)
prices["ruler"] = 30      # insert a new key→value → average O(1)
del prices["eraser"]      # delete a key   → average O(1)
"pen" in prices           # True (checks keys) → average O(1)
len(prices)               # 3

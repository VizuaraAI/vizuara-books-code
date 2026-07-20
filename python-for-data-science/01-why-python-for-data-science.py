"""
Python for Data Science
Chapter 1: Why Python for Data Science?
Section: Getting Started

Read this chapter: https://books.vizuara.ai/read/python-for-data-science/why-python-for-data-science

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- stub added to make this file runnable ---
# Block 1 below is the "slow pure-Python" half of the chapter's comparison and
# assumes a million-element list already exists. Block 2 then builds `data` for
# real with NumPy. Supply your own list here to run block 1 on its own.
data = []  # TODO: the chapter assumes a list of 1,000,000 numbers - see
           # https://books.vizuara.ai/read/python-for-data-science/why-python-for-data-science

# --- block 1 ---
total = 0
for x in data:          # data is a list of 1,000,000 numbers
    total += x * x

# --- block 2 ---
import numpy as np
data = np.arange(1_000_000)   # an ndarray, not a Python list
total = np.sum(data * data)

# --- block 3 ---
prices = [1200, 999, 1499, 750]
cheap = [p for p in prices if p < 1000]
print(f"Found {len(cheap)} items under 1000: {cheap}")

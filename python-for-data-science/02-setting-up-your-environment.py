"""
Python for Data Science
Chapter 2: Setting Up Your Environment
Section: Getting Started

Read this chapter: https://books.vizuara.ai/read/python-for-data-science/setting-up-your-environment

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import sys
print("Python version:", sys.version.split()[0])
print("2 + 2 =", 2 + 2)

# --- block 2 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# !pip install some-library

# --- block 3 ---
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.arange(5)                 # array([0, 1, 2, 3, 4])
df = pd.DataFrame({"n": x, "square": x ** 2})
print(df)

plt.plot(df["n"], df["square"], marker="o")
plt.xlabel("n")
plt.ylabel("n squared")
plt.show()

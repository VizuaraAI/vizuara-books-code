"""
Python for Data Science
Chapter 25: A Mini Data-Analysis Walkthrough
Section: The Data Science Toolkit

Read this chapter: https://books.vizuara.ai/read/python-for-data-science/a-mini-data-analysis-walkthrough

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import pandas as pd

df = pd.read_csv("students.csv")

# --- block 2 ---
df.head()
#      name  hours  score
# 0   Aisha      6   78.0
# 1     Ben      2   55.0
# 2    Chen      8    NaN
# 3   Deepa      4   66.0
# 4    Ewan     -1   40.0

# --- block 3 ---
df.info()
# RangeIndex: 8 entries, 0 to 7
# name    8 non-null   object
# hours   8 non-null   int64
# score   7 non-null   float64   <- only 7 of 8! one hole

# --- block 4 ---
df = df.drop_duplicates()

# --- block 5 ---
df = df[df["hours"] >= 0]

# --- block 6 ---
df = df.dropna(subset=["score"])

# --- block 7 ---
df["hours"].corr(df["score"])
# 0.99

# --- block 8 ---
import matplotlib.pyplot as plt

plt.scatter(df["hours"], df["score"])
plt.xlabel("Study hours")
plt.ylabel("Exam score")
plt.title("More study hours, higher scores (r = 0.99)")
plt.show()

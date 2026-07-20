"""
Mathematical Foundations for Machine Learning
Chapter 30: Pandas for Data
Section: Python and Numerical Computing

Read this chapter: https://books.vizuara.ai/read/math-foundations-for-ml/pandas-for-data

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import pandas as pd

df = pd.read_csv("people.csv")
df
#      name    age    city
# 0    Ana     34     Pune
# 1    Ben     NaN    Pune
# 2    Cora    29     Mumbai
# 3    Ana     34     Pune
# 4    Dev     "41"   Delhi

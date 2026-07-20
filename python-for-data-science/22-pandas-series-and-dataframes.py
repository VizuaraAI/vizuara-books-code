"""
Python for Data Science
Chapter 22: Pandas: Series and DataFrames
Section: The Data Science Toolkit

Read this chapter: https://books.vizuara.ai/read/python-for-data-science/pandas-series-and-dataframes

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import pandas as pd

rain = pd.Series([210, 0, 95, 42], index=["Mumbai", "Jaipur", "Pune", "Delhi"])
print(rain)

# --- block 2 ---
data = {
    "rainfall_mm": [210, 0, 95, 42],
    "temp_c":      [29, 41, 27, 39],
}
df = pd.DataFrame(data, index=["Mumbai", "Jaipur", "Pune", "Delhi"])
print(df)

# --- block 3 ---
df = pd.read_csv("cities.csv")

# --- block 4 ---
df[df["rainfall_mm"] > 50]

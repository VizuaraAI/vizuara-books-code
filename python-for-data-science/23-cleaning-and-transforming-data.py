"""
Python for Data Science
Chapter 23: Cleaning and Transforming Data
Section: The Data Science Toolkit

Read this chapter: https://books.vizuara.ai/read/python-for-data-science/cleaning-and-transforming-data

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import pandas as pd

df = pd.DataFrame({
    "city":   ["Pune", "Pune", "Delhi", "Delhi", "Pune"],
    "product":["pen",  "pen",  "pen",   "mug",   "mug"],
    "units":  [3,       None,   5,       2,       4],
    "price":  [10.0,    10.0,   10.0,    None,    25.0],
})

# --- block 2 ---
df.isna().sum()
# city       0
# product    0
# units      1
# price      1

# --- block 3 ---
df["units"] = df["units"].fillna(0)
df["price"] = df["price"].fillna(df["price"].mean())

# --- block 4 ---
df["city"] == "Pune"
# 0     True
# 1     True
# 2    False
# 3    False
# 4     True

# --- block 5 ---
pune = df[df["city"] == "Pune"]     # 3 rows: the Pune orders

# --- block 6 ---
busy = df[(df["city"] == "Pune") & (df["units"] > 3)]

# --- block 7 ---
df.groupby("city")["units"].sum()
# city
# Delhi    7.0
# Pune     7.0

# --- block 8 ---
df = pd.read_csv("sales.csv")               # load
df["units"] = df["units"].fillna(0)         # fill holes
df["price"] = df["price"].fillna(df["price"].mean())
df = df[df["units"] > 0]                     # filter out non-sales
summary = df.groupby("city")["units"].sum() # aggregate

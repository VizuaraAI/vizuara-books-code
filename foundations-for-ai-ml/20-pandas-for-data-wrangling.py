"""
Foundations for AI & ML
Chapter 20: Pandas for Data Wrangling
Section: Python & the ML Toolkit

Read this chapter: https://books.vizuara.ai/read/foundations-for-ai-ml/pandas-for-data-wrangling

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- placeholders (added so this file is runnable standalone) ---
# Block 6 joins two DataFrames the chapter mentions but never constructs.
# See https://books.vizuara.ai/read/foundations-for-ai-ml/pandas-for-data-wrangling
customers = None  # TODO: a DataFrame with a customer_id column
orders = None     # TODO: a DataFrame with a customer_id column

# --- block 1 ---
import pandas as pd

ages = pd.Series([34, 28, 45, 28], index=["ana", "ben", "cy", "dee"])
ages["cy"]        # -> 45   (look up by LABEL, not just position)
ages.mean()       # -> 33.75

# --- block 2 ---
df = pd.DataFrame({
    "age":     [34, 28, 45, 28],
    "country": ["IN", "US", "IN", "UK"],
    "spend":   [120.0, 80.0, 200.0, None],   # None = a missing value
})
df.shape          # -> (4, 3)   4 rows, 3 columns
df.dtypes         # age int64, country object, spend float64

# --- block 3 ---
df = pd.read_csv("customers.csv")
df.head(3)        # first 3 rows — always look before you leap
df.info()         # column names, non-null counts, dtypes, memory
df.describe()     # count/mean/std/min/quartiles/max for numeric cols

# --- block 4 ---
df.loc[0, "age"]              # label-based: row labelled 0, column "age"
df.iloc[0, 0]                 # position-based: first row, first column
df.loc[df["age"] > 30, ["age", "spend"]]   # boolean mask + column list

# --- block 5 ---
df.groupby("country")["spend"].mean()
# country
# IN    160.0      (120 + 200) / 2
# UK      NaN      (dee's spend was missing)
# US     80.0

# --- block 6 ---
pd.merge(customers, orders, on="customer_id", how="left")

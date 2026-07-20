"""
Mathematical Foundations for Machine Learning
Chapter 32: Python for Machine Learning
Section: Python and Numerical Computing

Read this chapter: https://books.vizuara.ai/read/math-foundations-for-ml/python-for-machine-learning

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import pandas as pd

df = pd.DataFrame({
    "size_m2":  [50, 60, 80, 95, 120, 150],
    "bedrooms": [1,  2,  2,  3,   3,   4],
    "age_yrs":  [30, 15, 20,  8,   5,   2],
    "price_k":  [95, 130, 170, 210, 265, 330],  # price in thousands
})

# --- block 2 ---
X = df[["size_m2", "bedrooms", "age_yrs"]]   # shape (6, 3)
y = df["price_k"]                             # shape (6,)

# --- block 3 ---
import matplotlib.pyplot as plt

plt.scatter(df["size_m2"], df["price_k"])
plt.xlabel("size (m²)"); plt.ylabel("price (thousands)")
plt.show()

# --- block 4 ---
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42)

# --- block 5 ---
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)          # learn the knobs from training data
y_pred = model.predict(X_test)       # predict on the held-out houses

# --- block 6 ---
from sklearn.metrics import mean_squared_error, r2_score

mse = mean_squared_error(y_test, y_pred)
r2  = r2_score(y_test, y_pred)

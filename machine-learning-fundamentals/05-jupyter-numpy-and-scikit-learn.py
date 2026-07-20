"""
Machine Learning Fundamentals
Chapter 5: Jupyter Notebooks, NumPy, and Scikit-learn
Section: Foundations of Machine Learning

Read this chapter: https://books.vizuara.ai/read/machine-learning-fundamentals/jupyter-numpy-and-scikit-learn

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
apples = 3
price_each = 12

# --- block 2 ---
apples * price_each

# --- block 3 ---
w = [0.5, -0.2, 0.1]
x = [2.0,  3.0, 4.0]
score = 0.0
for i in range(len(w)):
    score += w[i] * x[i]
# score = 0.5*2 + (-0.2)*3 + 0.1*4 = 1.0 - 0.6 + 0.4 = 0.8

# --- block 4 ---
import numpy as np

w = np.array([0.5, -0.2, 0.1])
x = np.array([2.0, 3.0, 4.0])
score = np.dot(w, x)   # or:  w @ x
print(score)           # 0.8

# --- block 5 ---
X = np.array([[2.0, 3.0, 4.0],     # example 1
              [1.0, 0.0, 5.0],     # example 2
              [0.0, 2.0, 1.0],     # example 3
              [3.0, 3.0, 3.0]])    # example 4
print(X.shape)   # (4, 3)  -> 4 examples, 3 features each
print(w.shape)   # (3,)    -> one weight per feature

# --- block 6 ---
scores = X @ w        # shape (4,)  -> one score per example
print(scores)         # [0.8, 1.0, -0.3, 1.2]

# --- block 7 ---
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()   # 1. create the model
model.fit(X, y)                # 2. learn from data (X, y)
preds = model.predict(X_new)   # 3. predict on new data

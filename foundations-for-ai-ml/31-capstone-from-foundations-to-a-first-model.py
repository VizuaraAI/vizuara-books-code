"""
Foundations for AI & ML
Chapter 31: Capstone: From Foundations to a First Model
Section: Putting It Together

Read this chapter: https://books.vizuara.ai/read/foundations-for-ai-ml/capstone-from-foundations-to-a-first-model

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

X = np.array([[1, 3], [2, 2], [3, 4], [4, 3]], dtype=float)
y = np.array([0, 0, 1, 1], dtype=float)

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

w = np.zeros(2)          # start from ignorance
b = 0.0
eta = 0.1               # learning rate
n = len(y)

for step in range(2000):
    z = X @ w + b                       # (4,) dot products at once
    y_hat = sigmoid(z)                  # (4,) probabilities
    error = y_hat - y                   # (4,) the "(ŷ − y)" signal
    w -= eta * (X.T @ error) / n        # gradient step on weights
    b -= eta * error.mean()             # gradient step on bias

loss = -np.mean(y*np.log(y_hat) + (1-y)*np.log(1-y_hat))
print(w, b, loss)      # e.g. [ 2.42  0.80 ] -8.15  loss ≈ 0.08

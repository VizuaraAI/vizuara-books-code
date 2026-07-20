"""
Machine Learning Fundamentals
Chapter 9: The Random Linear Classification Algorithm
Section: Linear Classifiers and the Perceptron

Read this chapter: https://books.vizuara.ai/read/machine-learning-fundamentals/random-linear-classification

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

X = np.array([[2, 1], [3, 2], [0, 0], [1, -1]])   # (n=4, d=2)
y = np.array([1, 1, -1, -1])                        # labels in {-1, +1}

def score(w, b):
    z = X @ w + b                    # wᵀx + b for all 4 points at once
    preds = np.where(z >= 0, 1, -1)  # sign, with 0 -> +1
    return np.sum(preds == y)        # how many are correct

best_w, best_b, best_score = None, None, -1
for _ in range(1000):                             # T = 1000 random guesses
    w = np.random.randn(2)                        # random weight vector
    b = np.random.randn()                         # random bias
    s = score(w, b)
    if s > best_score:                            # the ratchet: keep the best
        best_w, best_b, best_score = w, b, s

print(best_score, best_w, best_b)                 # -> 4  [ ... ]  ...

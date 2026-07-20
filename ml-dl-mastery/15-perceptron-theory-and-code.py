"""
Machine Learning & Deep Learning Mastery
Chapter 15: The Perceptron: Theory and Code
Section: Linear Classifiers & the Perceptron

Read this chapter: https://books.vizuara.ai/read/ml-dl-mastery/perceptron-theory-and-code

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# NOTE: this block is prose in the book, not runnable code.
# The perceptron decision rule in maths notation; w, x and b are symbols in a
# formula. Block 3 below is the real, runnable version.
# score = w @ x + b        # a plain dot product plus a bias
# prediction = +1 if score >= 0 else -1

# --- block 2 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# w ← w + η · y · x
# b ← b + η · y

# --- block 3 ---
import numpy as np

def train_perceptron(X, y, eta=1.0, max_epochs=100):
    n_samples, n_features = X.shape
    w = np.zeros(n_features)
    b = 0.0
    for epoch in range(max_epochs):
        mistakes = 0
        for i in range(n_samples):
            score = np.dot(w, X[i]) + b
            pred  = 1 if score >= 0 else -1
            if pred != y[i]:                 # only act on mistakes
                w += eta * y[i] * X[i]       # w ← w + η·y·x
                b += eta * y[i]              # b ← b + η·y
                mistakes += 1
        if mistakes == 0:                    # a clean pass = done
            break
    return w, b

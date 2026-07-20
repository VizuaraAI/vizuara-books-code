"""
Machine Learning & Deep Learning Mastery
Chapter 20: Logistic Regression Fundamentals
Section: Logistic Regression

Read this chapter: https://books.vizuara.ai/read/ml-dl-mastery/logistic-regression-fundamentals

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# NOTE: this block is prose in the book, not runnable code.
# The definition of the logit in maths notation; w, x and b are symbols in a
# formula. Block 2 below is the real, runnable version.
# z = w @ x + b   # one raw number in (-inf, +inf)

# --- block 2 ---
import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def predict_proba(x, w, b):
    z = w @ x + b          # linear score (logit)
    return sigmoid(z)      # squashed into (0, 1) — a probability

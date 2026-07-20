"""
Machine Learning & Deep Learning Mastery
Chapter 14: Introduction to Linear Classifiers
Section: Linear Classifiers & the Perceptron

Read this chapter: https://books.vizuara.ai/read/ml-dl-mastery/linear-classifiers-intro

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def predict(w, x):
    # w has b folded in as its first entry; x is augmented with a leading 1
    score = np.dot(w, x)          # w·x already includes the bias term
    return 1 if score >= 0 else -1

# w = (b, w1, w2), x = (1, x1, x2)
w = np.array([-4.0, 1.0, 1.0])   # bias -4, weights (1, 1)
patients = {
    "A": np.array([1.0, 1.0, 1.0]),   # (1, x1=1, x2=1) -> healthy
    "C": np.array([1.0, 3.0, 3.0]),   # (1, x1=3, x2=3) -> condition
}
for name, x in patients.items():
    print(name, predict(w, x))        # A -1   C 1

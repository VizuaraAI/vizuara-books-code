"""
Build Decision Trees from Scratch
Chapter 3: Classification vs Regression Trees
Section: Foundations

Read this chapter: https://books.vizuara.ai/read/decision-trees-from-scratch/classification-vs-regression-trees

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

# --- CLASSIFICATION: Gini + majority vote ---
def gini(y):                       # y = array of class labels
    _, counts = np.unique(y, return_counts=True)
    p = counts / counts.sum()      # class fractions p_k
    return 1.0 - np.sum(p ** 2)    # 1 − Σ p_k²

def leaf_class(y):
    vals, counts = np.unique(y, return_counts=True)
    return vals[np.argmax(counts)] # the majority class (mode)

# --- REGRESSION: SSR + mean ---
def ssr(y):                        # y = array of numbers
    return np.sum((y - y.mean()) ** 2)   # Σ (yᵢ − ȳ)²

def leaf_reg(y):
    return y.mean()                # the mean target

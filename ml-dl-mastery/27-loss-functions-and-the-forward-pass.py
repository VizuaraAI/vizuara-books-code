"""
Machine Learning & Deep Learning Mastery
Chapter 27: Loss Functions and the Full Forward Pass
Section: Neural Networks: The Forward Pass

Read this chapter: https://books.vizuara.ai/read/ml-dl-mastery/loss-functions-and-the-forward-pass

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import numpy as np

# --- block 1 ---
def forward(X, Y, layer1, layer2):
    Z1 = layer1.forward(X)          # (3,4)·(4,5) → (3,5)
    A1 = np.maximum(0, Z1)          # ReLU: clamp negatives to 0
    Z2 = layer2.forward(A1)         # (3,5)·(5,2) → (3,2) logits
    # numerically stable softmax, per row
    e  = np.exp(Z2 - Z2.max(axis=1, keepdims=True))
    Yhat = e / e.sum(axis=1, keepdims=True)   # (3,2), rows sum to 1
    # cross-entropy: -log of the prob at the true class, averaged
    correct = np.sum(Yhat * Y, axis=1)        # pick each row's true-class prob
    L = np.mean(-np.log(correct))
    return Yhat, L

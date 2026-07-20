"""
Neural Networks from Scratch
Chapter 6: The Softmax Function
Section: Turning Scores into Probabilities

Read this chapter: https://books.vizuara.ai/read/neural-networks-from-scratch/the-softmax-function

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def softmax(logits):
    # logits shape: (n_samples, n_classes)
    m = np.max(logits, axis=1, keepdims=True)        # (n_samples, 1): per-row max
    exps = np.exp(logits - m)                          # subtract max, then exponentiate — safe
    return exps / np.sum(exps, axis=1, keepdims=True)  # divide by per-row sum -> each row sums to 1

# --- block 2 ---
logits = np.array([[2.3, -1.7, 0.5],
                   [0.0,  0.0, 0.0]])
print(softmax(logits))
# [[0.845 0.015 0.140]     <- our example from before
#  [0.333 0.333 0.333]]    <- all-equal logits -> uniform distribution

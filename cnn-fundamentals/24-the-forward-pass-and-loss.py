"""
Convolutional Neural Networks Fundamentals
Chapter 24: The Forward Pass and the Loss
Section: Training a CNN

Read this chapter: https://books.vizuara.ai/read/cnn-fundamentals/the-forward-pass-and-loss

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def softmax(z):
    z = z - z.max()            # numerical stability; cancels out mathematically
    e = np.exp(z)
    return e / e.sum()

def cross_entropy(probs, true_index):
    return -np.log(probs[true_index])

logits = np.array([2.0, 1.0, 0.1])   # forward-pass output: one logit per class
probs  = softmax(logits)             # [0.659, 0.242, 0.099]
loss   = cross_entropy(probs, 0)     # true class = glioma (index 0)

print(probs)   # [0.659 0.242 0.099]
print(loss)    # 0.417

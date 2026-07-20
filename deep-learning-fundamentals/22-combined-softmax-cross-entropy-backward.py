"""
Deep Learning Fundamentals
Chapter 22: Combined softmax + cross-entropy backward
Section: The Backward Pass (Backpropagation)

Read this chapter: https://books.vizuara.ai/read/deep-learning-fundamentals/combined-softmax-cross-entropy-backward

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def softmax_crossentropy_backward(y_pred, y_true):
    # y_pred: (B, n_classes) softmax probabilities ŷ
    # y_true: (B,) integer class indices
    B = len(y_pred)
    dz = y_pred.copy()              # start from ŷ
    dz[range(B), y_true] -= 1       # subtract 1 at each true class → ŷ - y
    dz = dz / B                     # average over the batch
    return dz

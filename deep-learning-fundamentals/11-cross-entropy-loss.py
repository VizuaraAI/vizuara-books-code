"""
Deep Learning Fundamentals
Chapter 11: Coding the cross-entropy loss
Section: The Forward Pass

Read this chapter: https://books.vizuara.ai/read/deep-learning-fundamentals/cross-entropy-loss

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- forward reference (hoisted so this file runs top to bottom) ---
# Block 1 below uses `np` and `y_pred`, but the chapter only imports NumPy and
# defines `y_pred` in block 2. Both are the book's own, copied verbatim from
# block 2 and hoisted here so the file is self-contained.
import numpy as np

y_pred = np.array([[0.7, 0.1, 0.2],     # sample 0, truth = class 0
                   [0.1, 0.5, 0.4],     # sample 1, truth = class 1
                   [0.02, 0.9, 0.08]])  # sample 2, truth = class 1

# --- block 1 ---
y_pred_clipped = np.clip(y_pred, 1e-7, 1 - 1e-7)

# --- block 2 ---
import numpy as np

y_pred = np.array([[0.7, 0.1, 0.2],     # sample 0, truth = class 0
                   [0.1, 0.5, 0.4],     # sample 1, truth = class 1
                   [0.02, 0.9, 0.08]])  # sample 2, truth = class 1

y_true = np.array([0, 1, 1])            # integer class labels, one per sample

# --- block 3 ---
def categorical_cross_entropy(y_pred, y_true):
    n = len(y_pred)                                   # batch size
    y_pred = np.clip(y_pred, 1e-7, 1 - 1e-7)          # defuse log(0)
    correct_confidences = y_pred[range(n), y_true]    # true-class prob per sample
    sample_losses = -np.log(correct_confidences)      # -log(ŷ_correct)
    return np.mean(sample_losses)                     # scalar batch loss

print(categorical_cross_entropy(y_pred, y_true))      # 0.3849...

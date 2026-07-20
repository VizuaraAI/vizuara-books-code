"""
Deep Learning Fundamentals
Chapter 34: L1 and L2 regularization
Section: Regularization and Testing

Read this chapter: https://books.vizuara.ai/read/deep-learning-fundamentals/l1-l2-regularization

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
# Forward: add the penalty to the data loss for reporting
def regularization_loss(layer, lam_l1=0.0, lam_l2=0.0):
    loss = 0.0
    if lam_l1 > 0:
        loss += lam_l1 * np.sum(np.abs(layer.weights))   # L1: Σ|w|
    if lam_l2 > 0:
        loss += lam_l2 * np.sum(layer.weights ** 2)       # L2: Σw²
    return loss

# Backward: add the penalty's gradient onto the existing dW
def add_reg_gradient(layer, lam_l1=0.0, lam_l2=0.0):
    if lam_l1 > 0:
        layer.dW += lam_l1 * np.sign(layer.weights)        # λ·sign(w)
    if lam_l2 > 0:
        layer.dW += 2 * lam_l2 * layer.weights             # 2·λ·w

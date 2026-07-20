"""
NLP & Computer Vision Mastery
Chapter 13: L1 and L2 Regularization
Section: Generalization and Transfer Learning

Read this chapter: https://books.vizuara.ai/read/nlp-cv-mastery/l1-and-l2-regularization

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 (COMMENTED OUT) ---
# NOTE: this block is prose in the book, not runnable code.
# It is the general form of a regularized objective; `penalty` is a symbol
# standing for L1 or L2, not a defined function.
# loss = L_data + lam * penalty(weights)

# --- block 2 ---
from tensorflow.keras import layers, regularizers

# L2 / ridge — smooth weight shrinkage
layers.Dense(64, activation="relu",
             kernel_regularizer=regularizers.l2(1e-4))

# L1 / lasso — drives weights to exactly zero (sparse)
layers.Dense(64, activation="relu",
             kernel_regularizer=regularizers.l1(1e-4))

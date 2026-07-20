"""
NLP & Computer Vision Mastery
Chapter 7: Weights, Biases, and the Loss Surface
Section: From Linear Models to Deep Networks

Read this chapter: https://books.vizuara.ai/read/nlp-cv-mastery/weights-biases-and-loss

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 (COMMENTED OUT) ---
# NOTE: this block is prose in the book, not runnable code.
# It is the algebraic form of a linear score; every symbol is notation, not a
# defined Python name.
# score = w1*x1 + w2*x2 + w3*x3 + b

# --- block 2 ---
import numpy as np
loss = -np.log(0.084)   # 2.477

"""
NLP & Computer Vision Mastery
Chapter 10: Softmax vs Sigmoid: Multi-class vs Multi-label
Section: From Linear Models to Deep Networks

Read this chapter: https://books.vizuara.ai/read/nlp-cv-mastery/softmax-vs-sigmoid

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def softmax(z):
    e = np.exp(z - np.max(z))   # subtract max for numerical stability
    return e / e.sum()          # every entry positive, all entries sum to 1

# --- block 2 ---
def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))   # applied element-wise, per output

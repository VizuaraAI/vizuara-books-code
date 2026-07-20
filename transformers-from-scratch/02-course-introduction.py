"""
Transformers: Theory, intuition, and Building from Scratch
Chapter 2: Course Introduction
Section: Introduction and Motivation

Read this chapter: https://books.vizuara.ai/read/transformers-from-scratch/course-introduction

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

# three word vectors (toy: 4 dimensions each)
x = np.array([[1.0, 0.0, 1.0, 0.0],   # word 0  ("river")
              [0.0, 1.0, 0.0, 1.0],   # word 1  ("bank")
              [1.0, 0.0, 1.0, 0.0]])  # word 2  ("flowed")

def softmax(z):
    z = z - z.max()                    # subtract max for numerical stability
    e = np.exp(z)
    return e / e.sum()

scores  = x[0] @ x.T                    # word 0 vs everyone -> [2., 0., 2.]
weights = softmax(scores)              # -> [0.42, 0.16, 0.42]  sums to 1
context = weights @ x                  # weighted blend of all three vectors
print(context)                         # word 0, now aware of words 1 and 2

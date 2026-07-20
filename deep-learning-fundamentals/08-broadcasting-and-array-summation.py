"""
Deep Learning Fundamentals
Chapter 8: Broadcasting and array summation
Section: The Forward Pass

Read this chapter: https://books.vizuara.ai/read/deep-learning-fundamentals/broadcasting-and-array-summation

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

XW = np.array([[ 1.5, -0.4],
               [ 0.2,  0.9],
               [-1.1,  0.3]])     # (3, 2)
b  = np.array([[0.5, 0.1]])       # (1, 2)

print(XW + b)
# [[ 2.0 -0.3]
#  [ 0.7  1.0]
#  [-0.6  0.4]]                   # (3, 2), each row got the same b

# --- forward reference (hoisted so this file runs top to bottom) ---
# Block 2 below uses `dvalues`, but the chapter only introduces it as a
# concrete array in block 3. The definition is the book's own, copied verbatim
# from block 3 and hoisted here so the file is self-contained.
dvalues = np.array([[ 0.1,  0.3],
                    [-0.2,  0.0],
                    [ 0.4, -0.1]])            # (3, 2)

# --- block 2 ---
db = np.sum(dvalues, axis=0, keepdims=True)   # (batch, n_neurons) -> (1, n_neurons)

# --- block 3 ---
dvalues = np.array([[ 0.1,  0.3],
                    [-0.2,  0.0],
                    [ 0.4, -0.1]])            # (3, 2)

db = np.sum(dvalues, axis=0, keepdims=True)
# neuron 1: 0.1 + (-0.2) + 0.4 =  0.3
# neuron 2: 0.3 +  0.0  + (-0.1) = 0.2
# db = [[0.3, 0.2]]                            # (1, 2) — same shape as b

"""
Neural Networks from Scratch
Chapter 2: What a Neural Network Must Actually Do
Section: The Ten Questions

Read this chapter: https://books.vizuara.ai/read/neural-networks-from-scratch/what-a-neural-network-must-do

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

# true class for this point is green (index 1)
p_A = np.array([0.10, 0.25, 0.65])   # network A's distribution
p_B = np.array([0.15, 0.45, 0.40])   # network B's distribution

loss_A = -np.log(p_A[1])   # -log(0.25) = 1.386
loss_B = -np.log(p_B[1])   # -log(0.45) = 0.799

"""
Neural Networks from Scratch
Chapter 10: Activation Functions
Section: Weights and Wiring

Read this chapter: https://books.vizuara.ai/read/neural-networks-from-scratch/activation-functions

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def relu(z):
    return np.maximum(0, z)

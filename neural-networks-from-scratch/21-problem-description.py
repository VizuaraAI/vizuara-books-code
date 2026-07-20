"""
Neural Networks from Scratch
Chapter 21: The Problem: A Spiral Dataset
Section: Coding the Layers

Read this chapter: https://books.vizuara.ai/read/neural-networks-from-scratch/problem-description

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def spiral_data(samples, classes):
    X = np.zeros((samples * classes, 2))          # (300, 2) for 100×3
    y = np.zeros(samples * classes, dtype='uint8') # (300,)  integer labels
    for class_number in range(classes):
        ix = range(samples * class_number, samples * (class_number + 1))
        r = np.linspace(0.0, 1, samples)                              # radius 0 → 1
        t = (np.linspace(class_number * 4, (class_number + 1) * 4, samples)
             + np.random.randn(samples) * 0.2)                        # angle + noise
        X[ix] = np.c_[r * np.sin(t * 2.5), r * np.cos(t * 2.5)]       # (x, y)
        y[ix] = class_number
    return X, y

X, y = spiral_data(samples=100, classes=3)

"""
Mathematical Foundations for Machine Learning
Chapter 41: A Neuron from Scratch
Section: Putting It Together

Read this chapter: https://books.vizuara.ai/read/math-foundations-for-ml/a-neuron-from-scratch

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import math

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

def neuron(x, w, b):
    z = sum(wi * xi for wi, xi in zip(w, x)) + b   # dot product + bias
    return sigmoid(z)                               # activation

x = [2, 3]
w = [0.5, -1]
b = 1
print(neuron(x, w, b))   # -> 0.2689...

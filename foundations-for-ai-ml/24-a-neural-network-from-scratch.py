"""
Foundations for AI & ML
Chapter 24: A Neural Network from Scratch
Section: Optimization & Neural Networks

Read this chapter: https://books.vizuara.ai/read/foundations-for-ai-ml/a-neural-network-from-scratch

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- placeholders (added so this file is runnable standalone) ---
# Block 1 is the two-line definition of a single neuron, written before the
# chapter has any concrete weights. Block 2 below builds the real ones.
# See https://books.vizuara.ai/read/foundations-for-ai-ml/a-neural-network-from-scratch
w = None  # TODO: this neuron's weight vector
x = None  # TODO: the neuron's input vector
b = None  # TODO: this neuron's bias


def activation(z):
    """TODO: any nonlinearity. Block 2 below defines the concrete one the
    chapter uses (sigmoid)."""
    raise NotImplementedError("placeholder - see block 2")


# --- block 1 ---
z = w @ x + b        # weighted sum: a single number
a = activation(z)    # squashed through a nonlinearity

# --- block 2 ---
import numpy as np

W1 = np.array([[0.5, -0.2],
               [0.3,  0.8]])   # hidden layer: (2 neurons, 2 inputs)
b1 = np.array([0.0, 0.1])
W2 = np.array([[1.0, -1.5]])   # output layer: (1 neuron, 2 inputs)
b2 = np.array([0.2])

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# --- block 3 ---
def forward(x):
    h = sigmoid(W1 @ x + b1)     # hidden layer
    y = sigmoid(W2 @ h + b2)     # output layer
    return y

print(forward(np.array([1.0, 0.0])))   # [0.481...]

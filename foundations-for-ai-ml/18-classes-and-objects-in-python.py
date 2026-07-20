"""
Foundations for AI & ML
Chapter 18: Classes and Objects in Python
Section: Python & the ML Toolkit

Read this chapter: https://books.vizuara.ai/read/foundations-for-ai-ml/classes-and-objects-in-python

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
w = [0.5, -0.2]
b = 0.1

def forward(w, b, x):
    z = sum(wi * xi for wi, xi in zip(w, x)) + b
    return max(0.0, z)          # ReLU activation

print(forward(w, b, [1.0, 2.0]))   # 0.5*1.0 + (-0.2)*2.0 + 0.1 = 0.2

# --- block 2 ---
class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights      # state, attached to THIS neuron
        self.bias = bias

    def forward(self, x):
        z = sum(w * xi for w, xi in zip(self.weights, x)) + self.bias
        return max(0.0, z)          # ReLU

# --- block 3 ---
n1 = Neuron([0.5, -0.2], 0.1)
n2 = Neuron([1.0,  1.0], 0.0)

print(n1.forward([1.0, 2.0]))   # 0.2  (uses n1's own weights)
print(n2.forward([1.0, 2.0]))   # 3.0  (uses n2's own weights)

# --- block 4 ---
class Layer:
    def __init__(self, neurons):
        self.neurons = neurons               # state: a list of Neuron objects

    def forward(self, x):
        return [neuron.forward(x) for neuron in self.neurons]

layer = Layer([
    Neuron([0.5, -0.2], 0.1),
    Neuron([1.0,  1.0], 0.0),
    Neuron([-1.0, 0.3], 0.5),
])

print(layer.forward([1.0, 2.0]))   # [0.2, 3.0, 0.1]

# --- block 5 ---
class BaseLayer:
    def __init__(self, name):
        self.name = name

    def forward(self, x):
        raise NotImplementedError   # each child must define its own

class ReLULayer(BaseLayer):
    def forward(self, x):
        return [max(0.0, xi) for xi in x]

# --- block 6 ---
class Neuron:
    weights = [0.0, 0.0]        # WRONG: one list, shared by ALL neurons

    def __init__(self, bias):
        self.bias = bias

n1 = Neuron(0.1)
n2 = Neuron(0.0)
n1.weights[0] = 0.5             # meant to set only n1...
print(n2.weights)               # [0.5, 0.0]  (n2 changed too!)

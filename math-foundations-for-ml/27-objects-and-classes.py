"""
Mathematical Foundations for Machine Learning
Chapter 27: Objects, Classes, and Building Blocks
Section: Python and Numerical Computing

Read this chapter: https://books.vizuara.ai/read/math-foundations-for-ml/objects-and-classes

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# Block 4's Layer.forward calls dot(), the helper written in chapter 26
# (Python for Math - A Fast Start), reused here without being reprinted.
from context import dot

# --- block 1 ---
def add(a, b):        return [x + y for x, y in zip(a, b)]
def scale(a, c):      return [c * x for x in a]
def magnitude(a):     return sum(x * x for x in a) ** 0.5

u = [3, 4]
v = [1, 2]
print(add(u, scale(v, 2)))   # [5, 8]
print(magnitude(u))          # 5.0

# --- block 2 ---
class Vector:
    def __init__(self, components):
        self.components = components        # the state this object carries

    def dot(self, other):
        return sum(a * b for a, b in zip(self.components, other.components))

    def magnitude(self):
        return self.dot(self) ** 0.5        # reuse dot: √(v · v)

u = Vector([3, 4])
v = Vector([1, 2])
print(u.dot(v))        # 3*1 + 4*2 = 11
print(u.magnitude())   # √(3*3 + 4*4) = √25 = 5.0

# --- block 3 ---
class Vector:
    def __init__(self, components):
        self.components = components

    def __add__(self, other):               # enables  u + v
        return Vector([a + b for a, b in zip(self.components, other.components)])

    def __mul__(self, scalar):              # enables  u * 2
        return Vector([scalar * a for a in self.components])

    def __repr__(self):                     # how it prints
        return f"Vector({self.components})"

u = Vector([3, 4])
v = Vector([1, 2])
print(u + v)       # Vector([4, 6])
print(u * 2)       # Vector([6, 8])

# --- block 4 ---
class Layer:
    def __init__(self, weights, bias):
        self.weights = weights          # remembered state
        self.bias = bias

    def forward(self, x):
        # one output = (row of weights) · x  +  bias
        return [dot(row, x) + self.bias for row in self.weights]

layer = Layer(weights=[[0.5, -0.2], [0.1, 0.4]], bias=1.0)
print(layer.forward([2, 3]))   # [1.4, 2.4]

# --- block 5 ---
import math

class Gaussian:
    def __init__(self, mu, sigma):
        self.mu = mu                    # parameters ARE the state
        self.sigma = sigma

    def pdf(self, x):
        z = (x - self.mu) / self.sigma
        return math.exp(-0.5 * z * z) / (self.sigma * math.sqrt(2 * math.pi))

g = Gaussian(mu=0.0, sigma=1.0)
print(round(g.pdf(0.0), 4))   # 0.3989  — the peak of the standard normal

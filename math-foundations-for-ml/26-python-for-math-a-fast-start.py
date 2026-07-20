"""
Mathematical Foundations for Machine Learning
Chapter 26: Python for Math: A Fast Start
Section: Python and Numerical Computing

Read this chapter: https://books.vizuara.ai/read/math-foundations-for-ml/python-for-math-a-fast-start

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
x = 3
y = 4
length = (x**2 + y**2) ** 0.5   # ** is "to the power of"; 0.5 is a square root
print(length)                    # 5.0

# --- block 2 ---
a = [1, 2, 3]
b = [4, 5, 6]

total = 0
for i in range(len(a)):     # i takes the values 0, 1, 2
    total = total + a[i] * b[i]
print(total)                # 32

# --- block 3 ---
scores = [2, 4, 4, 4, 5, 5, 7, 9]
total = 0
for s in scores:            # s is each value, no index bookkeeping
    total = total + s
mean = total / len(scores)
print(mean)                 # 5.0

# --- block 4 ---
def dot(a, b):
    total = 0
    for i in range(len(a)):
        total = total + a[i] * b[i]
    return total            # hand the answer back to the caller

def mean(values):
    return sum(values) / len(values)

# --- block 5 ---
def neuron(w, x, b):
    z = dot(w, x) + b       # weighted sum plus bias
    return z                # (activation comes later)

print(neuron([0.5, -1.0], [2.0, 3.0], 1.0))   # 0.5·2 + (-1)·3 + 1 = -1.0

# --- block 6 ---
pmf = {"heads": 0.5, "tails": 0.5}   # a Bernoulli(0.5), stored by outcome name
print(pmf["heads"])                  # 0.5
print(sum(pmf.values()))             # 1.0  ← a valid PMF sums to 1

# --- block 7 ---
def relu(z):
    if z > 0:
        return z            # keep positive values
    else:
        return 0.0          # squash everything else to zero

print(relu(-1.0))           # 0.0
print(relu(2.5))            # 2.5

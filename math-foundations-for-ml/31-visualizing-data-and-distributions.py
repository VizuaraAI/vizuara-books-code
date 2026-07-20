"""
Mathematical Foundations for Machine Learning
Chapter 31: Visualizing Data and Distributions
Section: Python and Numerical Computing

Read this chapter: https://books.vizuara.ai/read/math-foundations-for-ml/visualizing-data-and-distributions

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]        # y = x², computed by hand or by loop
plt.plot(x, y)              # draw a line through the points
plt.xlabel("x")
plt.ylabel("y = x²")
plt.title("A parabola")
plt.show()                  # render the figure

# --- block 2 ---
import numpy as np
import matplotlib.pyplot as plt

samples = np.random.normal(loc=0.0, scale=1.0, size=1000)  # μ=0, σ=1
plt.hist(samples, bins=30, edgecolor="black")
plt.axvline(samples.mean(), color="red", label="mean")
plt.xlabel("value"); plt.ylabel("count"); plt.legend()
plt.show()

# --- block 3 ---
x = np.random.normal(size=200)
y = 0.8 * x + np.random.normal(scale=0.5, size=200)   # y tracks x, plus noise
plt.scatter(x, y, alpha=0.5)
plt.xlabel("x"); plt.ylabel("y")
plt.show()

print(np.corrcoef(x, y)[0, 1])   # ≈ 0.8

# --- block 4 ---
losses = []
theta = 5.0
lr = 0.3
for step in range(20):
    grad = 2 * theta          # gradient of L(θ) = θ²
    theta = theta - lr * grad # gradient-descent step
    losses.append(theta ** 2) # record the loss

plt.plot(losses, marker="o")
plt.xlabel("step"); plt.ylabel("loss L(θ) = θ²")
plt.show()

# --- block 5 ---
fig, axes = plt.subplots(1, 2, figsize=(10, 4))   # 1 row, 2 columns
axes[0].hist(samples, bins=30)
axes[0].set_title("distribution")
axes[1].plot(losses, marker="o")
axes[1].set_title("training loss")
plt.tight_layout()   # stop the labels from overlapping
plt.show()

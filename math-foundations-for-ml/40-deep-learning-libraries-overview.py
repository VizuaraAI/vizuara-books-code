"""
Mathematical Foundations for Machine Learning
Chapter 40: Deep Learning Libraries in Python
Section: Putting It Together

Read this chapter: https://books.vizuara.ai/read/math-foundations-for-ml/deep-learning-libraries-overview

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch

w = torch.tensor([2.0, -3.0], requires_grad=True)
x = torch.tensor([1.0, 4.0])

# --- block 2 ---
y = torch.dot(w, x)        # 2·1 + (−3)·4 = 2 − 12 = −10
loss = y ** 2              # (−10)² = 100

# --- block 3 ---
loss.backward()
print(w.grad)              # tensor([-20., -80.])

# --- block 4 ---
with torch.no_grad():
    w -= 0.01 * w.grad     # θ ← θ − η·∇L, by hand

# --- block 5 ---
optimizer = torch.optim.Adam([w], lr=0.01)
optimizer.zero_grad()      # clear old gradients
loss.backward()            # fill w.grad
optimizer.step()           # apply Adam's update to w

# --- block 6 ---
loss = torch.dot(w, x) ** 2
loss.backward()
print(w.grad)              # tensor([-20., -80.])
loss.backward()            # forgot to zero!
print(w.grad)              # tensor([-40., -160.])  ← doubled

# --- block 7 ---
import torch

model = torch.nn.Linear(2, 1)                    # weights + bias, a dot product
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
loss_fn = torch.nn.MSELoss()                      # mean-squared error

X = torch.tensor([[1.0, 4.0], [2.0, 1.0]])        # 2 examples, 2 features
target = torch.tensor([[10.0], [3.0]])

for step in range(100):
    optimizer.zero_grad()                         # 2. wipe old grads
    pred = model(X)                               # 1. forward
    loss = loss_fn(pred, target)                  # 1. loss
    loss.backward()                               # 3. autograd → grads
    optimizer.step()                              # 4. update weights

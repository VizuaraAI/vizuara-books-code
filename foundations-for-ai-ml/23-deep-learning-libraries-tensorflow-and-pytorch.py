"""
Foundations for AI & ML
Chapter 23: Deep Learning Libraries: TensorFlow and PyTorch
Section: Python & the ML Toolkit

Read this chapter: https://books.vizuara.ai/read/foundations-for-ai-ml/deep-learning-libraries-tensorflow-and-pytorch

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch

w = torch.tensor(2.0, requires_grad=True)   # a leaf we want gradients for
x = torch.tensor(3.0)                        # data — no grad needed
L = (w * x - 5) ** 2                          # forward pass; graph is recorded
L.backward()                                  # walk the graph backward
print(w.grad)                                 # tensor(6.) — matches our hand calc

# --- block 2 ---
import torch

w = torch.tensor(2.0, requires_grad=True)
x, target = torch.tensor(3.0), torch.tensor(5.0)
optimizer = torch.optim.SGD([w], lr=0.01)

for step in range(3):
    optimizer.zero_grad()            # 1. clear last step's gradients
    L = (w * x - target) ** 2        # 2. forward: prediction + loss
    L.backward()                     # 3. backward: fill w.grad via autograd
    optimizer.step()                 # 4. update: w ← w − lr · w.grad
    print(step, w.item(), w.grad.item())

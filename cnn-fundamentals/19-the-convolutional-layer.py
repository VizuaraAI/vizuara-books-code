"""
Convolutional Neural Networks Fundamentals
Chapter 19: The Convolutional Layer
Section: The Layers of a CNN

Read this chapter: https://books.vizuara.ai/read/cnn-fundamentals/the-convolutional-layer

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
import torch.nn as nn

layer = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, padding=1)

x = torch.randn(1, 3, 32, 32)   # (N=1, C_in=3, H=32, W=32) — one RGB image
y = layer(x)

print(y.shape)                  # torch.Size([1, 16, 32, 32])
print(layer.weight.shape)       # torch.Size([16, 3, 3, 3]) -> C_out, C_in, K, K
print(layer.bias.shape)         # torch.Size([16])          -> one bias per filter
print(sum(p.numel() for p in layer.parameters()))  # 448

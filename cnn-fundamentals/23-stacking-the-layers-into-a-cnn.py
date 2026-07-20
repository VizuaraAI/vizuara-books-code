"""
Convolutional Neural Networks Fundamentals
Chapter 23: Stacking the Layers Into a CNN
Section: The Layers of a CNN

Read this chapter: https://books.vizuara.ai/read/cnn-fundamentals/stacking-the-layers-into-a-cnn

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
import torch.nn as nn

block = nn.Sequential(
    nn.Conv2d(in_channels=1,  out_channels=8,  kernel_size=3, padding=1),  # (1,28,28) -> (8,28,28)
    nn.ReLU(),                                                             # shape unchanged
    nn.MaxPool2d(kernel_size=2, stride=2),                                 # (8,28,28) -> (8,14,14)
    nn.Conv2d(in_channels=8,  out_channels=16, kernel_size=3, padding=1),  # (8,14,14) -> (16,14,14)
    nn.ReLU(),                                                             # shape unchanged
    nn.MaxPool2d(kernel_size=2, stride=2),                                 # (16,14,14) -> (16,7,7)
)

x = torch.randn(1, 1, 28, 28)   # one grayscale image, batch of 1
print(block(x).shape)           # torch.Size([1, 16, 7, 7])

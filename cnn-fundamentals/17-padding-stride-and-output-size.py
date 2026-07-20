"""
Convolutional Neural Networks Fundamentals
Chapter 17: Padding, Stride, and Output Size
Section: Filtering and Convolution

Read this chapter: https://books.vizuara.ai/read/cnn-fundamentals/padding-stride-and-output-size

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch.nn as nn

# in_channels=1, out_channels=8 filters, kernel 3x3, pad 1, stride 2
conv = nn.Conv2d(in_channels=1, out_channels=8,
                 kernel_size=3, padding=1, stride=2)

# a batch of one 1-channel 5x5 image: (N, C, H, W)
import torch
x = torch.randn(1, 1, 5, 5)
y = conv(x)
print(y.shape)     # torch.Size([1, 8, 3, 3])

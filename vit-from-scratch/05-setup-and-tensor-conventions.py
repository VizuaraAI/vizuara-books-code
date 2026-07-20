"""
Build a Vision Transformer (ViT) from Scratch
Chapter 5: Setup and Tensor Conventions
Section: Why Vision Transformers

Read this chapter: https://books.vizuara.ai/read/vit-from-scratch/setup-and-tensor-conventions

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# install (CPU is fine for reading along; a GPU only matters when we train)
# pip install torch torchvision matplotlib

import torch
import torch.nn as nn

print(torch.__version__)          # 2.x is what this book was written against
print(torch.cuda.is_available())  # False on CPU, True if you have a GPU

# --- block 2 ---
torch.manual_seed(0)

# --- block 3 ---
B, C, H, W = 8, 3, 224, 224
images = torch.randn(B, C, H, W)

print(images.shape)     # torch.Size([8, 3, 224, 224])
print(images.ndim)      # 4
print(images.numel())   # 1,204,224  ->  8 * 3 * 224 * 224

# --- block 4 ---
# the toy we will reuse all book long
B, C, H, W, P, D = 1, 1, 4, 4, 2, 8
N = (H // P) * (W // P)          # 4 tokens
print("tokens N =", N)           # tokens N = 4

toy_tokens = torch.randn(B, N, D)
print(toy_tokens.shape)          # torch.Size([1, 4, 8])

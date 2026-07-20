"""
Transformers for Vision & Multimodal LLMs
Chapter 3: How nn.Conv2d Actually Works
Section: Foundations — From CNNs to Transformers

Read this chapter: https://books.vizuara.ai/read/transformers-for-vision-multimodal/how-nn-conv2d-actually-works

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
patch_embed = nn.Conv2d(in_channels=3, out_channels=768, kernel_size=16, stride=16)

# --- block 2 ---
import torch, torch.nn as nn

conv = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3, stride=1, padding=1)
print(conv.weight.shape)          # torch.Size([64, 3, 3, 3])
print(conv.bias.shape)            # torch.Size([64])

x = torch.randn(1, 3, 32, 32)     # (batch, channels, height, width)
y = conv(x)
print(y.shape)                    # torch.Size([1, 64, 32, 32])

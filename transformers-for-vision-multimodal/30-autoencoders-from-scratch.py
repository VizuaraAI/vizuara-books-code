"""
Transformers for Vision & Multimodal LLMs
Chapter 30: Autoencoders From Scratch
Section: Generative Vision — Autoencoders to Diffusion

Read this chapter: https://books.vizuara.ai/read/transformers-for-vision-multimodal/autoencoders-from-scratch

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch.nn as nn

encoder = nn.Sequential(
    nn.Linear(784, 128),   # 784 → 128   first squeeze
    nn.ReLU(),
    nn.Linear(128, 32),    # 128 → 32    into the bottleneck
)

# --- block 2 ---
decoder = nn.Sequential(
    nn.Linear(32, 128),    # 32 → 128    start reinflating
    nn.ReLU(),
    nn.Linear(128, 784),   # 128 → 784   back to pixel space
    nn.Sigmoid(),          # squash to [0, 1]
)

# --- block 3 ---
z    = encoder(x)          # (batch, 32)
xhat = decoder(z)          # (batch, 784)
loss = ((xhat - x) ** 2).mean()   # reconstruction error, no labels needed
loss.backward()

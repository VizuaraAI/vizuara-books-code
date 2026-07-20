"""
Build Large Language Models (LLMs) from Scratch
Chapter 2: What are LLMs?
Section: LLM Basics

Read this chapter: https://books.vizuara.ai/read/build-llm-from-scratch/what-are-llms

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch.nn as nn

# A parameter is just a learnable tensor of numbers.
# Here is one linear layer that maps a 768-dim vector to a 768-dim vector:
layer = nn.Linear(768, 768)

# It holds a weight matrix (768 x 768) and a bias (768):
print(layer.weight.shape)   # torch.Size([768, 768])  -> 589,824 numbers
print(layer.bias.shape)     # torch.Size([768])        ->     768 numbers

# GPT-2 small stacks ~124 of *millions* of such numbers across 12 layers.
total = sum(p.numel() for p in layer.parameters())
print(total)                # 590,592 parameters in this one small layer

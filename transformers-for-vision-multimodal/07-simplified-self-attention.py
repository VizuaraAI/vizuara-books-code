"""
Transformers for Vision & Multimodal LLMs
Chapter 7: Simplified Self-Attention, Coded From Scratch
Section: Attention From Scratch

Read this chapter: https://books.vizuara.ai/read/transformers-for-vision-multimodal/simplified-self-attention

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch

X = torch.tensor([[1., 0., 1.],
                  [0., 2., 0.],
                  [1., 1., 0.],
                  [0., 1., 1.]])          # (4, 3): four tokens, d = 3

scores  = X @ X.T                          # (4, 4): every dot product at once
weights = torch.softmax(scores, dim=-1)    # (4, 4): softmax over the KEYS, per row
Z       = weights @ X                      # (4, 3): weighted sum of the input rows

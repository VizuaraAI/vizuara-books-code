"""
NLP & Computer Vision Mastery
Chapter 9: Counting Parameters in a Network
Section: From Linear Models to Deep Networks

Read this chapter: https://books.vizuara.ai/read/nlp-cv-mastery/counting-parameters

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch.nn as nn

model = nn.Sequential(
    nn.Flatten(),          # 0 params — just reshapes 4x4 -> 16
    nn.Linear(16, 8),      # (16+1)*8 = 136
    nn.ReLU(),             # 0 params — max(0, x) has nothing to learn
    nn.Linear(8, 5),       # (8+1)*5  = 45
)

total = sum(p.numel() for p in model.parameters())
print(total)               # 181

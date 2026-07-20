"""
Build a NanoVLM from Scratch
Chapter 19: The Contrastive Idea
Section: Contrastive Learning

Read this chapter: https://books.vizuara.ai/read/nanovlm-from-scratch/the-contrastive-idea

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo scaffolding (not book code) ---
from torch.nn.functional import cross_entropy

# The chapter states the contrastive idea in schematic form.
I_emb = None       # TODO: (N, d) L2-normalized image embeddings
T_emb = None       # TODO: (N, d) L2-normalized text embeddings
temperature = 0.07  # the chapter's worked value
N = 0              # TODO: the batch size


# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import torch

# --- block 1 ---
S = I_emb @ T_emb.T          # shape (N, N)
# S[i][j] = cosine similarity of image i with caption j

# --- block 2 ---
logits = S / temperature
labels = torch.arange(N)                       # correct match for row i is column i
loss   = (cross_entropy(logits,   labels) +    # image → text
          cross_entropy(logits.T, labels)) / 2 # text → image

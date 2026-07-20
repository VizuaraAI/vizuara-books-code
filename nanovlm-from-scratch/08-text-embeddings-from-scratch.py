"""
Build a NanoVLM from Scratch
Chapter 8: Text Embeddings from Scratch
Section: Embeddings & Similarity

Read this chapter: https://books.vizuara.ai/read/nanovlm-from-scratch/text-embeddings-from-scratch

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo scaffolding (not book code) ---
# The pooled caption vector from station 4 of the chapter's pipeline.
pooled = None  # TODO: shape (8,) - the mean-pooled token embeddings


# --- block 1 ---
import torch
import torch.nn as nn

vocab_size, d_model = 50000, 8
embed = nn.Embedding(vocab_size, d_model)   # the (50000, 8) learnable table

ids = torch.tensor([10, 42, 7, 88])         # our 4 token IDs
x = embed(ids)                              # shape (4, 8) — four rows of 8 numbers

# --- block 2 ---
d_model, d = 8, 4          # text width 8, shared space width 4 (toy sizes)
text_proj = nn.Linear(d_model, d, bias=False)

caption_vec = pooled            # shape (8,) from station 4
z_text = text_proj(caption_vec) # shape (d,) = (4,) — now in the shared space

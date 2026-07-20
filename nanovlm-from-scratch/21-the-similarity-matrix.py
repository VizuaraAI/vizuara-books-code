"""
Build a NanoVLM from Scratch
Chapter 21: The Similarity Matrix
Section: Contrastive Learning

Read this chapter: https://books.vizuara.ai/read/nanovlm-from-scratch/the-similarity-matrix

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo scaffolding (not book code) ---
# Raw encoder outputs, each shape (N, d), before normalization.
image_emb = None  # TODO: (N, d) from the image tower
text_emb = None   # TODO: (N, d) from the text tower


# --- block 1 ---
import torch
import torch.nn.functional as F

# image_emb, text_emb: raw encoder outputs, each shape (N, d)
image_emb = F.normalize(image_emb, dim=-1)   # L2-normalize each row -> length 1
text_emb  = F.normalize(text_emb,  dim=-1)   # so dot product == cosine similarity

S = image_emb @ text_emb.T                    # (N, d) @ (d, N) -> (N, N) similarity matrix

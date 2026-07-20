"""
Build a NanoVLM from Scratch
Chapter 18: Matching Image and Text Dimensions
Section: Encoding Images into Vectors

Read this chapter: https://books.vizuara.ai/read/nanovlm-from-scratch/matching-image-and-text-dimensions

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo scaffolding (not book code) ---
# Pooled tower outputs, before the projection heads.
img_feat = None   # TODO: (batch, 512) from the image tower
text_feat = None  # TODO: (batch, 384) from the text tower


# --- block 1 ---
import torch.nn as nn

D_IMG = 512   # width the image tower pools to
D_TXT = 384   # width the text tower pools to
D     = 256   # the SHARED embedding dimension

image_proj = nn.Linear(D_IMG, D)   # weight shape (256, 512)
text_proj  = nn.Linear(D_TXT, D)   # weight shape (256, 384)

# img_feat: (batch, 512)   text_feat: (batch, 384)
img_emb  = image_proj(img_feat)    # -> (batch, 256)
text_emb = text_proj(text_feat)    # -> (batch, 256)

"""
Build a Vision Transformer (ViT) from Scratch
Chapter 8: Patch Embedding with a Conv2d Trick
Section: Turning Images into Tokens

Read this chapter: https://books.vizuara.ai/read/vit-from-scratch/patch-embedding-with-convolution

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
x = self.proj(images)      # (B, 768, 14, 14)  — the strided conv
x = x.flatten(2)           # (B, 768, 196)      — merge H,W into N
x = x.transpose(1, 2)      # (B, 196, 768)      — (B, N, D), ready for the encoder

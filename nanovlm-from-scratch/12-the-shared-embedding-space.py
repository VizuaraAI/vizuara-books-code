"""
Build a NanoVLM from Scratch
Chapter 12: The Shared Embedding Space
Section: Embeddings & Similarity

Read this chapter: https://books.vizuara.ai/read/nanovlm-from-scratch/the-shared-embedding-space

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
img_dog  = [ 0.10, 0.99, 0.05, 0.02]   # from the image encoder, ‖·‖ = 1
txt_dog  = [ 0.80, 0.20, 0.55, 0.10]   # from the text encoder,  ‖·‖ = 1

# --- block 2 ---
txt_dog  = [ 0.30, 0.90, 0.28, 0.08]   # rotated toward img_dog, re-normalized

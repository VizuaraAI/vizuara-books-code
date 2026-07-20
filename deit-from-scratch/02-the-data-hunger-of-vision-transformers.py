"""
Build a Data-Efficient Image Transformer (DeiT) from Scratch
Chapter 2: The Data Hunger of Vision Transformers
Section: Why DeiT?

Read this chapter: https://books.vizuara.ai/read/deit-from-scratch/the-data-hunger-of-vision-transformers

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# CNN: ONE filter, reused at every spatial position (weight sharing).
# The "position doesn't change meaning" fact is HARD-CODED.
for pos in all_196_positions:
    feature[pos] = conv(patch_at(pos), shared_filter)   # same weights everywhere

# ViT: attention over tokens. No weight sharing across positions,
# no built-in notion that pos i is near pos j. Every such relationship
# is a parameter the optimizer must discover from examples.
tokens = patch_embed(image) + learnable_position_embeddings   # position is a SLOT, not a BELIEF
out = transformer_blocks(tokens)                              # locality/equivariance: learned, not given

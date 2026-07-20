"""
Transformers for Vision & Multimodal LLMs
Chapter 13: Patch Embeddings and the CLS Token
Section: The Vision Transformer

Read this chapter: https://books.vizuara.ai/read/transformers-for-vision-multimodal/patch-embeddings-and-cls-token

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import torch.nn as nn

# --- block 1 ---
patch_embed = nn.Conv2d(in_channels=3, out_channels=D,
                        kernel_size=P, stride=P)

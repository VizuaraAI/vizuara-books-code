"""
Transformers for Vision & Multimodal LLMs
Chapter 27: Flamingo — Few-Shot Multimodal Learning
Section: Video & Multimodal Models

Read this chapter: https://books.vizuara.ai/read/transformers-for-vision-multimodal/flamingo-few-shot-multimodal

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import torch

# --- block 1 ---
# inside a Flamingo-style gated cross-attention block
# x        : text hidden states  (seq_len, d_model)   <- queries
# visual   : resampled tokens     (R, d_model)         <- keys / values
attn_out = cross_attention(query=x, key=visual, value=visual)
x = x + torch.tanh(alpha) * attn_out      # alpha starts at 0  -> tanh(0) = 0

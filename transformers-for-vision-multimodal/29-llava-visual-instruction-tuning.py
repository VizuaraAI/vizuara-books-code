"""
Transformers for Vision & Multimodal LLMs
Chapter 29: LLaVA — Visual Instruction Tuning
Section: Video & Multimodal Models

Read this chapter: https://books.vizuara.ai/read/transformers-for-vision-multimodal/llava-visual-instruction-tuning

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch, torch.nn as nn

W = nn.Linear(1024, 4096, bias=False)   # LLaVA-v1 projector: the whole connector
H = torch.randn(256, 1024)              # CLIP patch features (frozen)
image_tokens = W(H)                     # -> (256, 4096): now in LLM embedding space

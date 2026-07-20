"""
Build a NanoVLM from Scratch
Chapter 32: Watching Alignment Emerge
Section: Training, Evaluation & Beyond

Read this chapter: https://books.vizuara.ai/read/nanovlm-from-scratch/watching-alignment-emerge

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo scaffolding (not book code) ---
# The similarity matrix a training step just produced.
S = None  # TODO: (N, N) similarity matrix
N = 0     # TODO: the batch size


# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import torch

# --- block 1 ---
preds = S.argmax(dim=1)                 # for each image, index of its best-matching caption
acc   = (preds == torch.arange(N, device=S.device)).float().mean()

"""
Build a NanoVLM from Scratch
Chapter 20: Positives, Negatives, and the Batch
Section: Contrastive Learning

Read this chapter: https://books.vizuara.ai/read/nanovlm-from-scratch/positives-negatives-and-the-batch

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo scaffolding (not book code) ---
# I, T: (N, d) image and text embeddings, already L2-normalized.
I = None  # TODO: (N, d) image embeddings
T = None  # TODO: (N, d) text embeddings
N = 0     # TODO: the batch size


# --- block 1 ---
import torch
import torch.nn.functional as F

# I, T: (N, d) image and text embeddings, already L2-normalized
logits = I @ T.T                     # (N, N) similarity grid, S
labels = torch.arange(N)             # [0, 1, 2, ..., N-1] — the diagonal!

# row i (an image) should pick column i (its caption)
loss_i2t = F.cross_entropy(logits, labels)
# and symmetrically, each caption should pick its image
loss_t2i = F.cross_entropy(logits.T, labels)
loss = (loss_i2t + loss_t2i) / 2

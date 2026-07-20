"""
Build a NanoVLM from Scratch
Chapter 5: The Landscape: CLIP and Friends
Section: Vision-Language Foundations

Read this chapter: https://books.vizuara.ai/read/nanovlm-from-scratch/the-landscape-clip-and-friends

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo scaffolding (not book code) ---
from torch.nn.functional import cross_entropy

# The chapter shows the loss in schematic form. These two names stand for the
# tensors the training step hands it; Chapter 24 builds them for real:
# https://books.vizuara.ai/read/nanovlm-from-scratch/coding-the-contrastive-loss
logits = None  # TODO: (N, N) scaled cosine similarities
labels = None  # TODO: [0, 1, ..., N-1]


# --- block 1 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# cos(a, b) = (a · b) / (‖a‖ · ‖b‖)

# --- block 2 ---
# logits: N x N, scaled cosine similarities; labels = [0, 1, ..., N-1]
loss_i2t = cross_entropy(logits,   labels)   # each row: image picks its caption
loss_t2i = cross_entropy(logits.T, labels)   # each column: caption picks its image
loss = (loss_i2t + loss_t2i) / 2             # symmetric — both directions matter

"""
Build a NanoVLM from Scratch
Chapter 22: The CLIP Contrastive Loss
Section: Contrastive Learning

Read this chapter: https://books.vizuara.ai/read/nanovlm-from-scratch/the-clip-contrastive-loss

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo scaffolding (not book code) ---
from torch.nn.functional import cross_entropy

# The chapter works the loss through by hand, so these stand for the pieces.
S = None            # TODO: (N, N) cosine similarity matrix
temperature = 0.07  # the chapter's worked value
N = 0               # TODO: the batch size


# --- block 1 ---
row0 = [0.9, 0.2, 0.1]   # dog-image vs [dog-cap, cat-cap, car-cap]

# --- block 2 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# exp([0.9, 0.2, 0.1]) = [2.4596, 1.2214, 1.1052]   # sum = 4.7862
# p = [2.4596, 1.2214, 1.1052] / 4.7862
#   = [0.514, 0.255, 0.231]

# --- block 3 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# loss_row0 = -log(0.514) = 0.666

# --- block 4 ---
logits = S / temperature      # equivalently: logits = S * logit_scale

# --- block 5 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# p = softmax([9.0, 2.0, 1.0]) = [0.9988, 0.0009, 0.0003]
# loss = -log(0.9988) = 0.0012

# --- block 6 ---
labels = [0, 1, ..., N-1]              # the diagonal is always correct

loss_i2t = cross_entropy(logits,   labels)   # each ROW picks its caption
loss_t2i = cross_entropy(logits.T, labels)   # each COLUMN picks its image
loss     = (loss_i2t + loss_t2i) / 2         # symmetric — this halving is essential

# --- block 7 ---
logits = [[9.0, 2.0, 1.0],     # image 0 vs [cap0, cap1, cap2]
          [1.0, 8.0, 2.0],     # image 1
          [0.0, 1.0, 7.0]]     # image 2

# --- block 8 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# loss_row0 = -log(0.9988) = 0.0012
# loss_row1 = -log(0.9966) = 0.0034
# loss_row2 = -log(0.9966) = 0.0034
# loss_i2t  = (0.0012 + 0.0034 + 0.0034) / 3 = 0.0027

# --- block 9 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# loss = (loss_i2t + loss_t2i) / 2 ≈ 0.0035

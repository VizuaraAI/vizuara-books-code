"""
Build a NanoVLM from Scratch
Chapter 11: Dot Products, Norms, and Normalization
Section: Embeddings & Similarity

Read this chapter: https://books.vizuara.ai/read/nanovlm-from-scratch/dot-products-norms-and-normalization

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo scaffolding (not book code) ---
# Raw (un-normalized) encoder outputs. Chapters 26-27 build the encoders:
# https://books.vizuara.ai/read/nanovlm-from-scratch/the-image-encoder-module
img_emb = None  # TODO: (N, d) raw image embeddings
txt_emb = None  # TODO: (N, d) raw text embeddings


# --- block 1 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# a · b = a₁·b₁ + a₂·b₂ + ... + a_d·b_d   # one scalar out

# --- block 2 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# ‖a‖ = sqrt(a₁² + a₂² + ... + a_d²)

# --- block 3 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# â = a / ‖a‖        # "a-hat": same direction as a, length exactly 1

# --- block 4 ---
import torch.nn.functional as F

img = F.normalize(img_emb, dim=-1)   # each image row → unit length
txt = F.normalize(txt_emb, dim=-1)   # each text row  → unit length
sims = img @ txt.T                    # N×N cosine similarities, one matmul

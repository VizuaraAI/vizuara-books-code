"""
Build a Data-Efficient Image Transformer (DeiT) from Scratch
Chapter 29: CLS Token vs Distillation Token
Section: The Distillation Token

Read this chapter: https://books.vizuara.ai/read/deit-from-scratch/cls-token-vs-distillation-token

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# cls_logits, dist_logits: each (B, 1000), from the two heads
loss_cls  = cross_entropy(cls_logits,  y)      # CLS token graded vs TRUE label
loss_dist = cross_entropy(dist_logits, y_t)    # DIST token graded vs TEACHER's argmax
loss = 0.5 * loss_cls + 0.5 * loss_dist         # DeiT hard-distillation objective

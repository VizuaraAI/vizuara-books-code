"""
Transformers for Vision & Multimodal LLMs
Chapter 16: DeiT — Data-Efficient Image Transformers
Section: The Vision Transformer

Read this chapter: https://books.vizuara.ai/read/transformers-for-vision-multimodal/deit-intuition

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# y_true  : the ground-truth label
# y_teacher = teacher(image).argmax(dim=-1)   # the teacher's single top guess
# z_cls, z_distill : the two head logits, from the two tokens

loss = 0.5 * cross_entropy(z_cls,     y_true) \
     + 0.5 * cross_entropy(z_distill, y_teacher)

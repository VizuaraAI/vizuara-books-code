"""
Build a NanoVLM from Scratch
Chapter 2: Why Multimodal — What VLMs Unlock
Section: Vision-Language Foundations

Read this chapter: https://books.vizuara.ai/read/nanovlm-from-scratch/why-multimodal-and-what-vlms-unlock

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def cosine(a, b):
    dot = sum(ai * bi for ai, bi in zip(a, b))
    na  = sum(ai * ai for ai in a) ** 0.5
    nb  = sum(bi * bi for bi in b) ** 0.5
    return dot / (na * nb)

"""
Build a Diffusion Language Model from Scratch
Chapter 3: Representing Text in a Vector Space
Section: Foundations: Text as a Distribution

Read this chapter: https://books.vizuara.ai/read/diffusion-lm-from-scratch/text-in-vector-space

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# vocab: 0=cat, 1=dog, 2=king, 3=queen, 4=runs
#            dim0    dim1    dim2    dim3
E = [
    [ 0.21,  0.90, -0.15,  0.04],   # 0: cat
    [ 0.25,  0.85, -0.10,  0.08],   # 1: dog
    [-0.60,  0.11,  0.77,  0.30],   # 2: king
    [-0.58,  0.09,  0.74,  0.35],   # 3: queen
    [ 0.05, -0.40,  0.02,  0.66],   # 4: runs
]

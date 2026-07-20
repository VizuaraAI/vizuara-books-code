"""
Build a NanoVLM from Scratch
Chapter 3: One Idea: Vision and Language Are Both Vectors
Section: Vision-Language Foundations

Read this chapter: https://books.vizuara.ai/read/nanovlm-from-scratch/one-idea-vision-and-language-are-both-vectors

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
image        = [ 0.9,  0.1,  0.4,  0.2]   # the bicycle photo, as a vector
cap_bike     = [ 0.8,  0.2,  0.5,  0.1]   # "a red bicycle"
cap_dog      = [-0.3,  0.7, -0.2,  0.6]   # "a sleeping dog"
cap_car      = [ 0.1, -0.4,  0.9,  0.3]   # "a fast car"

# --- block 2 ---
import numpy as np

def l2_normalize(v):
    return v / np.linalg.norm(v)          # make the vector length 1

img = l2_normalize(np.array([0.9, 0.1, 0.4, 0.2]))
cap = l2_normalize(np.array([0.8, 0.2, 0.5, 0.1]))

similarity = img @ cap                     # a plain dot product == cosine, since both are unit-length
# ≈ 0.98

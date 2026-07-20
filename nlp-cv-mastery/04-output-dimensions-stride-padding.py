"""
NLP & Computer Vision Mastery
Chapter 4: Output Dimensions: Stride and Padding
Section: Foundations of Vision

Read this chapter: https://books.vizuara.ai/read/nlp-cv-mastery/output-dimensions-stride-padding

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def conv_out(I, K, P=0, S=1):
    return (I - K + 2 * P) // S + 1   # // is floor division — the floor is built in

conv_out(32, 3)             # -> 30   (valid, stride 1)
conv_out(32, 3, P=1)        # -> 32   ("same" padding)
conv_out(32, 3, P=1, S=2)   # -> 16   (strided downsample)

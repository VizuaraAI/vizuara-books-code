"""
Transformers for Vision & Multimodal LLMs
Chapter 2: The Limits of the Convolutional Inductive Bias
Section: Foundations — From CNNs to Transformers

Read this chapter: https://books.vizuara.ai/read/transformers-for-vision-multimodal/limits-of-the-convolutional-inductive-bias

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# A CNN with 3x3 (here: kernel-3) convs, stride 1.
# RF after L layers = 1 + 2L. To connect position 0 and 3 we need RF >= 4:
#   L = 1 -> RF 3  (pos 0 and 3 are NOT yet connected)
#   L = 2 -> RF 5  (now they are)  -> 2 layers, information routed through pos 1,2

# Attention over the same 4 positions, d = 8:
#   scores = Q @ K.T          # shape (4, 4): position 0 scores directly against position 3
#   weights = softmax(scores) # position 0 can put ALL its weight on position 3 in ONE layer

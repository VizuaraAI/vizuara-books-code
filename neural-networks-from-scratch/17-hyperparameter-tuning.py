"""
Neural Networks from Scratch
Chapter 17: Hyperparameter Tuning
Section: How a Network Learns

Read this chapter: https://books.vizuara.ai/read/neural-networks-from-scratch/hyperparameter-tuning

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# Layer 1:  2 -> 64
#   weights (2, 64) = 128 numbers,  biases (1, 64) = 64  ->  192
# Layer 2:  64 -> 3
#   weights (64, 3) = 192 numbers,  biases (1, 3)  = 3   ->  195
# total learnable parameters: 192 + 195 = 387

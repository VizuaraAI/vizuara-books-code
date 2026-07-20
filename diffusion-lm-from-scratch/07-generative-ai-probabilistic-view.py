"""
Build a Diffusion Language Model from Scratch
Chapter 7: Generative AI: One Probabilistic View of Everything
Section: The Diffusion Idea

Read this chapter: https://books.vizuara.ai/read/diffusion-lm-from-scratch/generative-ai-probabilistic-view

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# p(x): a distribution over 16 possible two-word sentences.
# Only the plausible ones get real mass; the rest are near-zero.
p = {
    "the cat": 0.30,
    "the dog": 0.25,
    "cat sat": 0.20,
    "dog sat": 0.15,
    "the sat": 0.05,
    # ... the remaining 11 combinations share the last 0.05
}
# sum over all 16 outcomes = 1.0

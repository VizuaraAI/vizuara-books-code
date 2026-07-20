"""
Build a Diffusion Language Model from Scratch
Chapter 6: Language Models as Distribution Approximators
Section: Foundations: Text as a Distribution

Read this chapter: https://books.vizuara.ai/read/diffusion-lm-from-scratch/language-models-as-distribution-approximators

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# Corpus of real sequences drawn from p*. We never see p* itself.
corpus = ["the cat sat", "the dog ran", "the cat ran"]

# The training objective, in one line:
#   maximize the average log-probability the model assigns to real text
#   equivalently: minimize the negative log-likelihood (the "NLL loss")
loss = -mean(log(p_theta(seq)) for seq in corpus)

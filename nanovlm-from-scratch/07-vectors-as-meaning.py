"""
Build a NanoVLM from Scratch
Chapter 7: Vectors as Meaning
Section: Embeddings & Similarity

Read this chapter: https://books.vizuara.ai/read/nanovlm-from-scratch/vectors-as-meaning

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo scaffolding (not book code) ---
# `vec` is the word-vector lookup the chapter asks you to imagine: hand it a
# word, get back that word's embedding. Chapter 8 builds the real table:
# https://books.vizuara.ai/read/nanovlm-from-scratch/text-embeddings-from-scratch
vec = None  # TODO: str -> embedding vector


# --- block 1 ---
result = vec("king") - vec("man") + vec("woman")
# find the existing word vector nearest to `result`
# → it lands right next to vec("queen")

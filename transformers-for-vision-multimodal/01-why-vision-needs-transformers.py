"""
Transformers for Vision & Multimodal LLMs
Chapter 1: Why Vision Needs Transformers
Section: Foundations — From CNNs to Transformers

Read this chapter: https://books.vizuara.ai/read/transformers-for-vision-multimodal/why-vision-needs-transformers

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# Q, K, V: (n_tokens, d_k)   — n patch tokens, each projected to dimension d_k
scores  = Q @ K.T / d_k**0.5      # (n, n): every query dotted with every key
weights = softmax(scores, dim=-1) # each row sums to 1
out     = weights @ V             # (n, d_k): relevance-weighted blend of all tokens

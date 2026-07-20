"""
LLM Finetuning
Chapter 39: The Workshop Code and Resources
Section: Putting It Together

Read this chapter: https://books.vizuara.ai/read/llm-finetuning/the-workshop-code-and-resources

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# 9 tokens: 6 prompt + 3 response
input_ids = [464, 3139, 286, 4881, 25, 220, 42, 15, 88]  # illustrative
labels    = [-100, -100, -100, -100, -100, -100, 42, 15, 88]
# cross-entropy skips every position whose label is -100

# --- block 2 ---
h = x @ W.T + (alpha / r) * (x @ A.T) @ B.T   # W frozen; only A, B train

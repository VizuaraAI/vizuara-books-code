"""
LLM Finetuning
Chapter 23: Left vs Right Padding
Section: Finetuning with Hugging Face & Unsloth

Read this chapter: https://books.vizuara.ai/read/llm-finetuning/left-vs-right-padding

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
prompt_A = [7, 4, 9]          # "Tell me a"      (3 real tokens)
prompt_B = [7, 4, 9, 2, 6]    # "Tell me a fun fact"  (5 real tokens)

# --- block 2 ---
# RIGHT-PADDED batch
[[7, 4, 9, 0, 0],     # A: real tokens, then pads
 [7, 4, 9, 2, 6]]     # B: already full length
mask = [[1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1]]

# --- block 3 ---
# LEFT-PADDED batch
[[0, 0, 7, 4, 9],     # A: pads first, then real tokens
 [7, 4, 9, 2, 6]]     # B: already full length
mask = [[0, 0, 1, 1, 1],
        [1, 1, 1, 1, 1]]

# --- block 4 ---
tokenizer.padding_side = "left"   # for batched generation with a causal model

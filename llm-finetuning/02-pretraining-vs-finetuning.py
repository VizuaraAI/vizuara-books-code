"""
LLM Finetuning
Chapter 2: Pretraining vs Finetuning
Section: Why Finetune at All

Read this chapter: https://books.vizuara.ai/read/llm-finetuning/pretraining-vs-finetuning

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# one training line, four free (input -> target) pairs
inputs  = [10, 42,  7]        # "cats", "chase", "small"
targets = [42,  7, 88]        # "chase", "small", "mice"
# position 0: given "cats"              -> predict "chase"
# position 1: given "cats chase"        -> predict "small"
# position 2: given "cats chase small"  -> predict "mice"

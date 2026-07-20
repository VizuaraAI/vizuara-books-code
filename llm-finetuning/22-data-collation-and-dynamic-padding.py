"""
LLM Finetuning
Chapter 22: Data Collation and Dynamic Padding
Section: Finetuning with Hugging Face & Unsloth

Read this chapter: https://books.vizuara.ai/read/llm-finetuning/data-collation-and-dynamic-padding

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
batch = [
    [101, 2054, 2003],                    # "what is"        → 3 tokens
    [101, 3413, 1996, 4633, 2000],        # "explain the ..." → 5 tokens
    [101, 5587],                          # "add"            → 2 tokens
    [101, 4443, 1037, 3437, 2006, 2129],  # "write a ..."     → 6 tokens
]

# --- block 2 ---
from transformers import DataCollatorWithPadding

collator = DataCollatorWithPadding(tokenizer=tokenizer)  # pads each batch to its own max

# The Trainer / DataLoader calls this on a list of examples:
batch = collator([
    {"input_ids": [101, 2054, 2003]},
    {"input_ids": [101, 3413, 1996, 4633, 2000]},
    {"input_ids": [101, 5587]},
    {"input_ids": [101, 4443, 1037, 3437, 2006, 2129]},
])

batch["input_ids"].shape      # torch.Size([4, 6])  ← padded to the batch max, not 1024
batch["attention_mask"].shape # torch.Size([4, 6])  ← 1s for real tokens, 0s for padding

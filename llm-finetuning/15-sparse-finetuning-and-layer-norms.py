"""
LLM Finetuning
Chapter 15: Sparse Finetuning and Layer Norms
Section: Instruction Finetuning from Scratch

Read this chapter: https://books.vizuara.ai/read/llm-finetuning/sparse-finetuning-and-layer-norms

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import torch

# --- block 1 ---
for param in model.parameters():
    param.requires_grad = False        # freeze the whole model

# now un-freeze only what we want to train
for param in model.transformer.h[-1].parameters():
    param.requires_grad = True         # last transformer block only

# --- block 2 ---
# x has shape (batch, seq_len, d)   with d = 768
mean = x.mean(dim=-1, keepdim=True)
var  = x.var(dim=-1, keepdim=True, unbiased=False)
x_hat = (x - mean) / torch.sqrt(var + eps)      # normalize: no parameters
out   = gamma * x_hat + beta                    # gamma, beta: the ONLY learned params

# --- block 3 ---
trainable = [p for p in model.parameters() if p.requires_grad]
optimizer = torch.optim.AdamW(trainable, lr=5e-4)   # not model.parameters()!

"""
LLM Finetuning
Chapter 14: The Finetuning Training Loop
Section: Instruction Finetuning from Scratch

Read this chapter: https://books.vizuara.ai/read/llm-finetuning/the-finetuning-training-loop

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
import torch.nn.functional as F

# logits:  (batch, seq_len, vocab)   from the forward pass
# targets: (batch, seq_len)          input_ids shifted left by one,
#                                     with prompt positions set to -100
loss = F.cross_entropy(
    logits.flatten(0, 1),            # (batch*seq_len, vocab)
    targets.flatten(),               # (batch*seq_len,)   -100 = ignore
    ignore_index=-100,
)

# --- block 2 ---
loss.backward()

# --- block 3 ---
optimizer.step()      # apply the update to every trainable weight

# --- block 4 ---
model.train()
for epoch in range(num_epochs):
    for input_ids, targets in train_loader:      # targets have -100 on prompt tokens
        logits = model(input_ids)                # 1. forward
        loss = F.cross_entropy(                   # 2. loss (response tokens only)
            logits[:, :-1].flatten(0, 1),
            targets[:, 1:].flatten(),
            ignore_index=-100,
        )
        optimizer.zero_grad()                     #    clear old gradients
        loss.backward()                           # 3. backward
        optimizer.step()                          # 4. update

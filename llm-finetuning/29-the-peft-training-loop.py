"""
LLM Finetuning
Chapter 29: The PEFT Training Loop
Section: Parameter-Efficient Finetuning (PEFT)

Read this chapter: https://books.vizuara.ai/read/llm-finetuning/the-peft-training-loop

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import torch
import torch.nn.functional as F

# --- block 1 ---
# Step 0 (before any training): freeze base, keep only LoRA adapters trainable.
for name, param in model.named_parameters():
    param.requires_grad = "lora_" in name   # True only for lora_A / lora_B

# --- block 2 ---
# WRONG: hands the optimizer every parameter, including the frozen base.
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-4)

# RIGHT: give the optimizer only the parameters that actually train.
trainable = [p for p in model.parameters() if p.requires_grad]
optimizer = torch.optim.AdamW(trainable, lr=1e-4)

# --- block 3 ---
# Step 0: freeze the base, keep adapters trainable
for name, p in model.named_parameters():
    p.requires_grad = "lora_" in name

# Give the optimizer ONLY the trainable params
trainable = [p for p in model.parameters() if p.requires_grad]
optimizer = torch.optim.AdamW(trainable, lr=1e-4)

model.train()
for input_ids, targets in train_loader:      # targets have -100 on prompt tokens
    logits = model(input_ids)                 # 1. forward — through frozen W + live A,B
    loss = F.cross_entropy(                    # 2. loss — response tokens only
        logits[:, :-1].flatten(0, 1),
        targets[:, 1:].flatten(),
        ignore_index=-100,
    )
    optimizer.zero_grad()
    loss.backward()                            # 3. backward — grad reaches only A, B
    optimizer.step()                           # 4. step — updates only A, B

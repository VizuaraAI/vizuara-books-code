"""
Build Large Language Models (LLMs) from Scratch
Chapter 20: Finetuning: From Spam Classifier to Instruction Following
Section: LLM Finetuning

Read this chapter: https://books.vizuara.ai/read/build-llm-from-scratch/finetuning-classification-and-instructions

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import torch

# --- stubs (not book code) ---
# The block below is the finetuning loop. These four names are supplied by the
# reader / built earlier; stubbed here so the file imports and runs (the loop
# body never executes with num_epochs = 0).
num_epochs = 0     # TODO: how many passes over the finetuning set
train_loader = []  # TODO: DataLoader over the spam / instruction dataset
optimizer = None   # TODO: e.g. torch.optim.AdamW(model.parameters(), lr=5e-5)
model = None       # TODO: the pretrained GPT model to finetune - ch. 17/19

# --- block 1 ---
for epoch in range(num_epochs):
    for input_batch, target_batch in train_loader:
        optimizer.zero_grad()
        logits = model(input_batch)                 # (batch, seq_len, 50257)
        loss = torch.nn.functional.cross_entropy(
            logits.flatten(0, 1),                    # (batch*seq_len, 50257)
            target_batch.flatten(),                  # (batch*seq_len,), prompt+pad are -100
        )
        loss.backward()
        optimizer.step()

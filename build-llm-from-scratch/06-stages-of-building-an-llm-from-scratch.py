"""
Build Large Language Models (LLMs) from Scratch
Chapter 6: Stages of building an LLM from scratch
Section: LLM Basics

Read this chapter: https://books.vizuara.ai/read/build-llm-from-scratch/stages-of-building-an-llm-from-scratch

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- stubs (not book code) ---
# The block below is the pretraining skeleton. These four names are the
# pieces the book builds in later chapters; stubbed here so the file imports
# and runs (the loop body never executes over an empty `data_loader`).
data_loader = []      # TODO: the DataLoader - built in ch. 13
model = None          # TODO: the GPT model - built in ch. 17
cross_entropy = None  # TODO: the loss fn - see ch. 18 (torch cross_entropy)
optimizer = None      # TODO: e.g. torch.optim.AdamW(...) - see ch. 18

# --- block 1 ---
for batch in data_loader:               # batches of token sequences
    inputs  = batch[:, :-1]               # e.g. "The cat sat on the"
    targets = batch[:, 1:]                # shifted by one: "cat sat on the mat"

    logits = model(inputs)                # [batch, seq_len, vocab_size]
    loss   = cross_entropy(logits, targets)   # how wrong was each next-token guess?

    loss.backward()                       # gradients: which weights caused the error?
    optimizer.step()                      # nudge every weight to reduce the loss
    optimizer.zero_grad()

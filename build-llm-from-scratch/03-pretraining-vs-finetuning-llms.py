"""
Build Large Language Models (LLMs) from Scratch
Chapter 3: Pretraining vs Finetuning LLMs
Section: LLM Basics

Read this chapter: https://books.vizuara.ai/read/build-llm-from-scratch/pretraining-vs-finetuning-llms

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- stubs (not book code) ---
# The block below is the shared training skeleton. It names four pieces the
# book has not built yet at this point; they are stubbed here so the file
# imports and runs (the loop body never executes over an empty `data`).
data = []             # TODO: batches of tokenized text - built in ch. 13
model = None          # TODO: the GPT model - built in ch. 17
cross_entropy = None  # TODO: the loss fn - see ch. 18 (torch cross_entropy)
optimizer = None      # TODO: e.g. torch.optim.AdamW(...) - see ch. 18

# --- block 1 ---
# BOTH phases share this exact skeleton:
for batch in data:                          # the difference is HERE
    logits = model(batch.input_tokens)      # predict next-token distribution
    loss   = cross_entropy(logits, batch.target_tokens)
    loss.backward()                          # compute gradients
    optimizer.step()                         # nudge the weights

# PRETRAINING: batch = raw internet text; target = the actual next token,
#              loss computed on EVERY position.
#
# FINETUNING:  batch = a {prompt, response} chat pair; target = next token,
#              but loss MASKED to the RESPONSE tokens only (ignore the prompt).

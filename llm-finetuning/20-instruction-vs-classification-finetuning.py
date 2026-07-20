"""
LLM Finetuning
Chapter 20: Instruction vs Classification Finetuning
Section: Finetuning with Hugging Face & Unsloth

Read this chapter: https://books.vizuara.ai/read/llm-finetuning/instruction-vs-classification-finetuning

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# CLASSIFICATION: one input, one label, loss on the last position
logits = class_head(body(input_ids)[:, -1, :])   # (batch, 2)
loss = cross_entropy(logits, labels)              # labels: 0 or 1

# INSTRUCTION: full sequence, loss only on response tokens
logits = lm_head(body(input_ids))                 # (batch, seq_len, 50257)
targets = input_ids.clone()
targets[prompt_mask] = -100                        # ignore prompt positions
loss = cross_entropy(logits.view(-1, 50257), targets.view(-1))

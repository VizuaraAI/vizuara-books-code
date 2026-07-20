"""
RLHF from Scratch
Chapter 29: Training a Tiny Supervised Language Model
Section: Building It From Scratch

Read this chapter: https://books.vizuara.ai/read/rlhf-from-scratch/training-a-tiny-supervised-language-model

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
config = dict(
    vocab_size = 50257,   # GPT-2 tokenizer
    context_len = 256,    # max tokens the model sees at once
    d_model    = 512,     # width of each token vector
    n_layers   = 8,       # stacked transformer blocks
    n_heads    = 8,       # attention heads per block
)

# --- block 2 ---
model.train()
for inputs, targets in dataloader:          # targets = inputs shifted left by 1
    logits = model(inputs)                  # (batch, seq_len, vocab_size)
    loss = cross_entropy(
        logits.flatten(0, 1),               # (batch*seq_len, vocab_size)
        targets.flatten(),                  # (batch*seq_len,)
    )
    loss.backward()                         # gradients of loss w.r.t. every weight
    optimizer.step()                        # AdamW nudges weights downhill
    optimizer.zero_grad()                   # clear for the next batch

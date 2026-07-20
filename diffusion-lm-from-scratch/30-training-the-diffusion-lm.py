"""
Build a Diffusion Language Model from Scratch
Chapter 30: Training the Diffusion LM
Section: Build It: Code the Diffusion LM

Read this chapter: https://books.vizuara.ai/read/diffusion-lm-from-scratch/training-the-diffusion-lm

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
for step in range(num_steps):
    x0 = get_batch()                          # (B, L) clean token ids
    t  = torch.rand(x0.size(0), 1)            # (B, 1) a fresh masking level per row
    x_t, masked = forward_mask(x0, t, MASK_ID)  # corrupt a COPY; masked is the answer key

    logits = model(x_t)                       # (B, L, V) a distribution per position
    loss = masked_cross_entropy(logits, x0, masked)  # graded ONLY where masked is True

    optimizer.zero_grad()
    loss.backward()                           # gradients flow back to every weight
    optimizer.step()                          # nudge weights down the loss

# --- block 2 ---
import torch.nn.functional as F

def masked_cross_entropy(logits, x0, masked):
    # logits: (B, L, V)   x0: (B, L)   masked: (B, L) bool
    B, L, V = logits.shape
    logits = logits.reshape(B * L, V)     # (B*L, V) one row per position
    x0     = x0.reshape(B * L)            # (B*L,)  the true token at each position
    masked = masked.reshape(B * L)        # (B*L,)  True where we should grade

    logits = logits[masked]               # keep ONLY masked positions -> (n_masked, V)
    x0     = x0[masked]                    # their true tokens          -> (n_masked,)
    return F.cross_entropy(logits, x0)    # averaged over n_masked

# --- block 3 ---
optimizer.zero_grad()   # clear gradients left over from the previous step
loss.backward()         # autograd computes dLoss/dw for every weight w
optimizer.step()        # optimizer moves each weight a small step downhill

# --- block 4 ---
model = DiffusionLM(vocab_size=50258, d_model=..., n_layers=...)
optimizer = torch.optim.AdamW(model.parameters(), lr=3e-4)

for step in range(num_steps):
    x0 = get_batch()                                 # (B, L) clean ids
    t  = torch.rand(x0.size(0), 1)                   # (B, 1) per-row masking level
    x_t, masked = forward_mask(x0, t, MASK_ID)       # corrupt a copy + answer key

    logits = model(x_t)                              # (B, L, V)
    loss = masked_cross_entropy(logits, x0, masked)  # grade the blanks only

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if step % 100 == 0:
        print(f"step {step:5d} | loss {loss.item():.3f}")

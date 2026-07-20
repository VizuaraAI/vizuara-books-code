"""
Build a Diffusion Language Model from Scratch
Chapter 33: Putting It All Together
Section: Build It: Code the Diffusion LM

Read this chapter: https://books.vizuara.ai/read/diffusion-lm-from-scratch/putting-it-all-together

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
# vocab: 0=[MASK] 1=the 2=cat 3=sat 4=on 5=mat 6=dog 7=ran 8=<pad>
x = torch.tensor([
    [1, 2, 0, 5],   # the  cat  [MASK]  mat
    [1, 6, 7, 0],   # the  dog  ran     [MASK]
])                  # x.shape == (2, 4)

model  = DiffusionLM(vocab_size=9, d_model=8, n_layers=2, n_heads=2, max_len=4)
logits = model(x)   # (2, 4, 9)

# --- block 2 ---
def train_step(model, clean_x, mask_id, opt):
    x, masked_positions = forward_mask(clean_x, mask_id)  # controller: corrupt a copy
    logits = model(x)                                     # SAME forward pass, (B,T,vocab)
    loss = F.cross_entropy(
        logits[masked_positions],          # only the rows we hid
        clean_x[masked_positions],         # graded against the originals
    )
    loss.backward(); opt.step(); opt.zero_grad()
    return loss.item()

# --- block 3 ---
@torch.no_grad()
def generate(model, length, n_steps, mask_id):
    x = torch.full((1, length), mask_id)              # start ALL masked
    for _ in range(n_steps):
        logits = model(x)                             # SAME forward pass again
        probs  = logits.softmax(-1)                   # (1, L, vocab)
        conf, guess = probs.max(-1)                   # best token + its probability
        still_masked = (x == mask_id)
        # reveal the k most-confident masked slots this step
        k = max(1, still_masked.sum() // n_steps)
        pick = top_k_confident(conf, still_masked, k)
        x[pick] = guess[pick]                         # commit them
        if not (x == mask_id).any():
            break
    return x

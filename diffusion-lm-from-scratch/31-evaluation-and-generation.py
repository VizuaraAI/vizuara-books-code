"""
Build a Diffusion Language Model from Scratch
Chapter 31: Evaluation and Running Generation
Section: Build It: Code the Diffusion LM

Read this chapter: https://books.vizuara.ai/read/diffusion-lm-from-scratch/evaluation-and-generation

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
@torch.no_grad()
def evaluate(model, held_out_loader, MASK, mask_rate=0.15):
    model.eval()                                  # turn off dropout, etc.
    total_loss, total_correct, total_masked = 0.0, 0, 0
    for x in held_out_loader:                     # x: (B, T) clean token IDs
        corrupted, mask = mask_batch(x, MASK, mask_rate)  # same corruption as training
        logits = model(corrupted)                 # (B, T, vocab) — one forward pass
        logits_m = logits[mask]                   # (num_masked, vocab): masked rows only
        targets_m = x[mask]                        # (num_masked,): the originals
        total_loss   += F.cross_entropy(logits_m, targets_m, reduction="sum").item()
        total_correct += (logits_m.argmax(-1) == targets_m).sum().item()
        total_masked += mask.sum().item()
    return total_loss / total_masked, total_correct / total_masked   # (avg loss, accuracy)

# --- block 2 ---
@torch.no_grad()
def generate(model, tokenizer, MASK, length=20, prompt=None,
             commit_per_step=1, temperature=0.7):
    model.eval()
    buffer = torch.full((length,), MASK)          # (L,) all [MASK] — allocate length up front
    if prompt is not None:                         # ── prompt = pre-committed positions
        ids = tokenizer.encode(prompt)             # e.g. "the cat" -> [1, 2]
        buffer[:len(ids)] = torch.tensor(ids)      # seed the prefix; the rest stays masked

    while (buffer == MASK).any():                  # stop when no [MASK] remains
        logits = model(buffer.unsqueeze(0))[0]     # (L, vocab) — one forward pass
        probs  = torch.softmax(logits / temperature, dim=-1)   # temperature-shaped
        conf   = probs.max(dim=-1).values          # (L,) confidence per slot (the ranking signal)
        sampled = torch.multinomial(probs, 1).squeeze(-1)      # (L,) sample a token per slot
        conf[buffer != MASK] = -float("inf")       # never re-commit a frozen slot (incl. the prompt)
        chosen = conf.topk(commit_per_step).indices            # most-confident masked slots
        buffer[chosen] = sampled[chosen]           # commit the SAMPLED tokens there
    return tokenizer.decode(buffer.tolist())       # (L,) IDs -> a string of words

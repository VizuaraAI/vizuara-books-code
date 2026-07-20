"""
Build a Diffusion Language Model from Scratch
Chapter 23: The Denoising Process in Detail
Section: Inference and Unmasking Strategies

Read this chapter: https://books.vizuara.ai/read/diffusion-lm-from-scratch/the-denoising-process-in-detail

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def denoise(buffer, model, MASK, commit_per_step=1):
    while (buffer == MASK).any():                 # stop when no [MASK] remains
        logits = model(buffer)                     # one forward pass, all positions
        probs  = softmax(logits, dim=-1)           # (L, vocab) categorical per slot
        conf, pred = probs.max(dim=-1)             # confidence + argmax token per slot
        conf[buffer != MASK] = -inf                # never re-commit a frozen slot
        chosen = conf.topk(commit_per_step).indices   # the most-confident masked slots
        buffer[chosen] = pred[chosen]              # commit those tokens permanently
    return buffer

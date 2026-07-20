"""
Build a Diffusion Language Model from Scratch
Chapter 24: Token Unmasking Schedules
Section: Inference and Unmasking Strategies

Read this chapter: https://books.vizuara.ai/read/diffusion-lm-from-scratch/token-unmasking-schedules

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def unmask_step(logits, still_masked, k):
    # logits: (seq_len, vocab) from one forward pass of the SAME denoiser
    probs = softmax(logits, axis=-1)              # per-position distributions
    top_prob = probs.max(axis=-1)                 # confidence at each position
    top_tok  = probs.argmax(axis=-1)              # the guessed token

    # SELECTION RULE: rank only the masked positions by confidence
    candidates = [i for i in range(len(top_tok)) if still_masked[i]]
    candidates.sort(key=lambda i: top_prob[i], reverse=True)

    # REVEAL COUNT: commit exactly the top-k of them
    for i in candidates[:k]:                       # <-- the whole schedule is these two lines
        sequence[i] = top_tok[i]
        still_masked[i] = False
    return sequence, still_masked

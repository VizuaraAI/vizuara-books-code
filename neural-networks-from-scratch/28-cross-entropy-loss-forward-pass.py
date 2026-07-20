"""
Neural Networks from Scratch
Chapter 28: Cross-Entropy Loss: The Forward Pass
Section: Loss, Optimizer, and Training

Read this chapter: https://books.vizuara.ai/read/neural-networks-from-scratch/cross-entropy-loss-forward-pass

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added so this file runs standalone) ---
# Block 1 uses numpy, but the chapter's own `import numpy as np` does not
# appear until block 2, further down this file.
import numpy as np

# --- placeholders (added so this file runs standalone) ---
# See https://books.vizuara.ai/read/neural-networks-from-scratch/cross-entropy-loss-forward-pass
probs = None   # TODO: (n_samples, n_classes) softmax probabilities to clip

# --- block 1 ---
probs_clipped = np.clip(probs, 1e-7, 1 - 1e-7)

# --- block 2 ---
import numpy as np

def cross_entropy_forward(probs, y):
    n_samples = len(probs)

    # 1. clip to dodge log(0) and log(1) blow-ups
    probs = np.clip(probs, 1e-7, 1 - 1e-7)

    # 2. gather the probability of the CORRECT class for each sample
    correct_confidences = probs[range(n_samples), y]

    # 3. per-sample loss, then average over the batch
    sample_losses = -np.log(correct_confidences)
    return np.mean(sample_losses)

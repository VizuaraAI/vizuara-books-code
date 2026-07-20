"""
RLHF from Scratch
Chapter 1: What is RLHF and Why It Matters
Section: Why Alignment

Read this chapter: https://books.vizuara.ai/read/rlhf-from-scratch/what-is-rlhf-and-why-it-matters

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# Bradley-Terry: probability the chosen response beats the rejected one
import torch

def preference_prob(r_chosen, r_rejected):
    # sigmoid of the score gap -> a probability in (0, 1)
    return torch.sigmoid(r_chosen - r_rejected)

# reward-model loss over a batch of preference pairs:
# maximize log-likelihood of the human's choice
def rm_loss(r_chosen, r_rejected):
    return -torch.log(torch.sigmoid(r_chosen - r_rejected)).mean()

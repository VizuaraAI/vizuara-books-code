"""
Build a Data-Efficient Image Transformer (DeiT) from Scratch
Chapter 24: The KL-Divergence Loss
Section: Knowledge Distillation

Read this chapter: https://books.vizuara.ai/read/deit-from-scratch/kl-divergence-loss

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch.nn.functional as F

def soft_distillation_loss(student_logits, teacher_logits, T):
    # student in log-space (KLDivLoss expects log-probabilities as input)
    log_q = F.log_softmax(student_logits / T, dim=-1)   # log ψ(Zs/T)
    p     = F.softmax(teacher_logits / T, dim=-1)        # ψ(Zt/T), the target
    # F.kl_div computes Σ p · (log p − log q) = KL(p ‖ q) when target is p
    kl = F.kl_div(log_q, p, reduction="batchmean")
    return kl * (T * T)                                  # the load-bearing T²

"""
Build a Data-Efficient Image Transformer (DeiT) from Scratch
Chapter 27: Combining the Losses
Section: Knowledge Distillation

Read this chapter: https://books.vizuara.ai/read/deit-from-scratch/combining-the-losses

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
import torch.nn.functional as F

def soft_distillation_loss(student_logits, teacher_logits, labels,
                           lam=0.1, T=3.0):
    # 1. ground-truth term: plain cross-entropy against the true label
    ce = F.cross_entropy(student_logits, labels)

    # 2. distillation term: KL between softened distributions
    student_log_probs = F.log_softmax(student_logits / T, dim=-1)
    teacher_probs     = F.softmax(teacher_logits / T, dim=-1)
    kl = F.kl_div(student_log_probs, teacher_probs,
                  reduction="batchmean") * (T * T)   # the T² factor!

    # 3. collapse to one scalar
    return (1 - lam) * ce + lam * kl

# --- block 2 ---
def hard_distillation_loss(student_logits, teacher_logits, labels):
    teacher_labels = teacher_logits.argmax(dim=-1)          # the teacher's top-1 guess
    ce_true    = F.cross_entropy(student_logits, labels)         # learn from the truth
    ce_teacher = F.cross_entropy(student_logits, teacher_labels) # learn from the teacher
    return 0.5 * ce_true + 0.5 * ce_teacher

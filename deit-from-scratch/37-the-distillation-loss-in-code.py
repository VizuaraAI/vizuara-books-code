"""
Build a Data-Efficient Image Transformer (DeiT) from Scratch
Chapter 37: The Distillation Loss in Code
Section: Training DeiT

Read this chapter: https://books.vizuara.ai/read/deit-from-scratch/the-distillation-loss-in-code

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch

teacher = build_regnety16gf(pretrained=True)   # ~82-84% top-1, already trained
teacher.eval()                                  # 1. BatchNorm/dropout in inference mode
for p in teacher.parameters():
    p.requires_grad = False                     # 2. optimizer never touches these
teacher.to(device)

# --- block 2 ---
with torch.no_grad():
    teacher_logits = teacher(images)   # (B, 1000), detached from the graph

# --- block 3 ---
import torch
import torch.nn.functional as F

def train_step(student, teacher, images, labels, optimizer):
    student.train()                     # dropout / drop-path ON for the student

    # 1. teacher forward — frozen, no graph, no gradient
    with torch.no_grad():
        teacher_logits = teacher(images)          # (B, 1000)
    y_teacher = teacher_logits.argmax(dim=-1)     # hard label: teacher's top-1

    # 2. student forward — returns TWO logit vectors in training mode
    cls_logits, dist_logits = student(images)     # each (B, 1000)

    # 3. combined loss: CLS head vs true label, DIST head vs teacher
    loss_cls  = F.cross_entropy(cls_logits,  labels)      # learn from the truth
    loss_dist = F.cross_entropy(dist_logits, y_teacher)   # learn from the teacher
    loss = 0.5 * loss_cls + 0.5 * loss_dist              # one scalar

    # 4. one gradient step — updates the student only
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    return loss.item()

# --- block 4 ---
# before training
assert all(not p.requires_grad for p in teacher.parameters())

# sanity check after one step
w0 = teacher.stem[0].weight.clone()
loss = train_step(student, teacher, images, labels, optimizer)
assert torch.equal(teacher.stem[0].weight, w0), "teacher weight moved!"

"""
Build a Data-Efficient Image Transformer (DeiT) from Scratch
Chapter 36: Writing the Training Loop
Section: Training DeiT

Read this chapter: https://books.vizuara.ai/read/deit-from-scratch/writing-the-training-loop

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
def train_one_step(student, teacher, criterion, optimizer, images, labels, device):
    images, labels = images.to(device), labels.to(device)

    optimizer.zero_grad()                       # (1) clear last batch's grads

    with torch.no_grad():                       # (2a) teacher is frozen
        teacher_logits = teacher(images)
    cls_logits, dist_logits = student(images)   # (2b) student, two heads

    loss = criterion(cls_logits, dist_logits,   # (3) fuse into one scalar
                     teacher_logits, labels)

    loss.backward()                             # (4) fill student .grad
    optimizer.step()                            # (5) move student weights
    return loss.item()

# --- block 2 ---
def train(student, teacher, criterion, optimizer, scheduler, loader, device, epochs=300):
    student.to(device).train()      # stochastic depth / dropout ON
    teacher.to(device).eval()       # teacher frozen: no dropout, no BN updates

    for epoch in range(epochs):
        running = 0.0
        for images, labels in loader:                        # 1250 batches
            loss = train_one_step(student, teacher, criterion,
                                  optimizer, images, labels, device)
            running += loss
        scheduler.step()                                     # once per epoch
        avg = running / len(loader)
        lr = scheduler.get_last_lr()[0]
        print(f"epoch {epoch:3d} | loss {avg:.4f} | lr {lr:.2e}")

# --- block 3 ---
loss.backward()
torch.nn.utils.clip_grad_norm_(student.parameters(), max_norm=1.0)   # NEW
optimizer.step()

# --- block 4 ---
scaler = torch.cuda.amp.GradScaler()

def train_one_step(student, teacher, criterion, optimizer, scaler, images, labels, device):
    images, labels = images.to(device), labels.to(device)
    optimizer.zero_grad()

    with torch.no_grad():
        teacher_logits = teacher(images)
    with torch.cuda.amp.autocast():                 # 16-bit forward where safe
        cls_logits, dist_logits = student(images)
        loss = criterion(cls_logits, dist_logits, teacher_logits, labels)

    scaler.scale(loss).backward()                   # scale grads up before backward
    scaler.unscale_(optimizer)                      # unscale before clipping
    torch.nn.utils.clip_grad_norm_(student.parameters(), max_norm=1.0)
    scaler.step(optimizer)                          # unscales, then steps
    scaler.update()                                 # adjust the scale for next step
    return loss.item()

"""
Build a NanoVLM from Scratch
Chapter 31: The Training Loop
Section: Training, Evaluation & Beyond

Read this chapter: https://books.vizuara.ai/read/nanovlm-from-scratch/the-training-loop

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo scaffolding (not book code) ---
# Built earlier in the book: the model (Chapter 30) and the loss (Chapter 24).
from context import NanoVLM, clip_loss

# The synthetic shapes dataset from Chapter 29:
# https://books.vizuara.ai/read/nanovlm-from-scratch/synthetic-data-for-training
dataset = None  # TODO: ShapesDataset()


# --- block 1 ---
import torch, math
from torch.utils.data import DataLoader

model = NanoVLM(d=128)                                  # random weights
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-4)
loader = DataLoader(dataset, batch_size=32, shuffle=True)

for epoch in range(50):                                 # one epoch = one pass over data
    for images, tokens in loader:                       # one batch = one step
        logits = model(images, tokens)                  # 1. FORWARD -> (N, N) logits
        loss   = clip_loss(logits)                      #    ...to one scalar

        optimizer.zero_grad()                           # clear last step's gradients
        loss.backward()                                 # 2. BACKWARD -> every .grad
        optimizer.step()                                # 3. STEP downhill

        with torch.no_grad():                           # keep temperature in range
            model.logit_scale.clamp_(max=math.log(100))

    print(f"epoch {epoch:2d}  loss {loss.item():.4f}")

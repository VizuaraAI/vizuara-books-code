"""
Build a NanoVLM from Scratch
Chapter 35: Debugging and Scaling Tips
Section: Training, Evaluation & Beyond

Read this chapter: https://books.vizuara.ai/read/nanovlm-from-scratch/debugging-and-scaling-tips

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo scaffolding (not book code) ---
from torch.nn.functional import normalize

# Built earlier in the book: the loss from Chapter 24.
from context import clip_loss

# Each tip inspects something a real training run already has on hand.
image_emb = None  # TODO: (N, d) image embeddings to inspect
t = None          # TODO: the learnable log-temperature parameter
S = None          # TODO: (N, N) cosine similarity matrix
model = None      # TODO: a NanoVLM instance (Chapter 30)
images = None     # TODO: a batch of images
texts = None      # TODO: a batch of tokenized captions
optimizer = None  # TODO: e.g. torch.optim.AdamW(model.parameters(), lr=1e-4)


# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import torch

# --- block 1 ---
img_norms = image_emb.norm(dim=-1)   # should be all 1.0000 after L2-norm
print(img_norms[:5])                 # -> tensor([3.91, 0.02, 7.4, ...]) means NOT normalized

# --- block 2 ---
# healthy: rows point in different directions
emb = normalize(torch.randn(4, 8), dim=-1)
emb.std(dim=0).mean()      # -> ~0.33, embeddings are spread out

# collapsed: every row is (almost) the same vector
base = normalize(torch.randn(1, 8), dim=-1)
emb  = base + 0.001 * torch.randn(4, 8)
emb.std(dim=0).mean()      # -> ~0.0006, all four vectors sit on top of each other

# --- block 3 ---
logit_scale = torch.exp(t).clamp(max=100.0)   # τ init ≈ 0.07  (exp(t)=1/0.07≈14.29)
logits = logit_scale * S                       # multiply, never divide by a raw τ

# --- block 4 ---
scaler = torch.cuda.amp.GradScaler()
with torch.autocast(device_type="cuda", dtype=torch.float16):
    logits = model(images, texts)      # ~half the memory -> bigger N fits
    loss   = clip_loss(logits)
scaler.scale(loss).backward()          # scaler guards fp16 gradients from underflow
scaler.step(optimizer); scaler.update()

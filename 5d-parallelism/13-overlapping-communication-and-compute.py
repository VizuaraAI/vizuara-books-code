"""
5D Parallelism for Large Model Training
Chapter 13: Overlapping Communication and Compute
Section: Data Parallelism

Read this chapter: https://books.vizuara.ai/read/5d-parallelism/overlapping-communication-and-compute

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from torch.nn.parallel import DistributedDataParallel as DDP

model = DDP(build_model().cuda(),
            bucket_cap_mb=25)      # bucket size: the knob from the napkin math

for micro in local_loader:
    loss = model(micro).loss
    loss.backward()               # ← buckets fill and fire DURING this call,
                                  #    overlapping the backward compute itself
    opt.step()                    # by here every gradient is already all-reduced
    opt.zero_grad()

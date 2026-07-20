"""
5D Parallelism for Large Model Training
Chapter 9: Data Parallelism from Scratch
Section: Data Parallelism

Read this chapter: https://books.vizuara.ai/read/5d-parallelism/data-parallelism-from-scratch

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch, torch.distributed as dist

dist.init_process_group("nccl")              # one process per GPU
rank, world = dist.get_rank(), dist.get_world_size()
torch.cuda.set_device(rank)

torch.manual_seed(0)                          # SAME seed on every rank
model = build_model().cuda()                  # → identical replicas
opt   = torch.optim.AdamW(model.parameters(), lr=3e-4)

# --- block 2 ---
def all_reduce_average(model, world):
    # Average every parameter's gradient across all ranks, in place.
    for p in model.parameters():
        if p.grad is None:
            continue
        dist.all_reduce(p.grad, op=dist.ReduceOp.SUM)   # each rank now holds the SUM
        p.grad /= world                                  # ...divide by N → the MEAN

for micro in local_loader:                    # this rank's shard of the batch
    loss = model(micro).loss                  # local loss = average over local examples
    loss.backward()                           # local gradient in p.grad
    all_reduce_average(model, world)          # ← the one line DDP hides from you
    opt.step()
    opt.zero_grad()

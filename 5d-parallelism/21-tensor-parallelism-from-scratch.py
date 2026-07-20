"""
5D Parallelism for Large Model Training
Chapter 21: Tensor Parallelism from Scratch
Section: Tensor Parallelism

Read this chapter: https://books.vizuara.ai/read/5d-parallelism/tensor-parallelism-from-scratch

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import os
import torch
import torch.distributed as dist

def setup():
    dist.init_process_group(backend="nccl")
    rank = dist.get_rank()              # 0 or 1
    world = dist.get_world_size()       # 2
    torch.cuda.set_device(rank)         # rank 0 → cuda:0, rank 1 → cuda:1
    return rank, world

rank, world = setup()
device = torch.device(f"cuda:{rank}")

# --- block 2 ---
class ColumnParallelLinear(torch.nn.Module):
    def __init__(self, d_in, d_out, world, rank, device, gather_output=True):
        super().__init__()
        assert d_out % world == 0
        self.local_out = d_out // world          # 8 // 2 = 4 columns per rank
        self.gather_output = gather_output
        # each rank allocates ONLY its shard of the weight: (d_in, local_out)
        self.W = torch.nn.Parameter(
            torch.empty(d_in, self.local_out, device=device))
        torch.nn.init.normal_(self.W, std=0.02)
        self.world = world

    def forward(self, x):                          # x: (4, 8) replicated
        y_local = x @ self.W                       # (4, 4) — my output columns
        if not self.gather_output:
            return y_local                         # keep it split (Megatron trick)
        gathered = [torch.empty_like(y_local) for _ in range(self.world)]
        dist.all_gather(gathered, y_local)         # collect every rank's slab
        return torch.cat(gathered, dim=-1)         # (4, 8) — full output

# --- block 3 ---
class RowParallelLinear(torch.nn.Module):
    def __init__(self, d_in, d_out, world, rank, device):
        super().__init__()
        assert d_in % world == 0
        self.local_in = d_in // world              # 8 // 2 = 4 input features per rank
        self.W = torch.nn.Parameter(
            torch.empty(self.local_in, d_out, device=device))   # (4, 8)
        torch.nn.init.normal_(self.W, std=0.02)

    def forward(self, x_local):                    # x_local: (4, 4) — MY input columns
        y_partial = x_local @ self.W               # (4, 8) — full width, PARTIAL sum
        dist.all_reduce(y_partial, op=dist.ReduceOp.SUM)   # add both ranks' partials
        return y_partial                           # (4, 8) — full result on every rank

# --- block 4 ---
col = ColumnParallelLinear(8, 8, world, rank, device, gather_output=False)
row = RowParallelLinear(8, 8, world, rank, device)

x = torch.randn(4, 8, device=device)          # replicated: same seed on both ranks
h = col(x)                                    # (4, 4) split output — NO collective
y = row(h)                                    # (4, 8) after the all-reduce

# reference: reconstruct the full weights on rank 0 and run it un-split
if rank == 0:
    Wc = gather_full_weight(col.W)            # (8, 8) full column-parallel weight
    Wr = gather_full_weight(row.W, dim=0)     # (8, 8) full row-parallel weight
    y_ref = (x @ Wc) @ Wr
    print(torch.allclose(y, y_ref, atol=1e-5))   # → True

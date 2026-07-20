"""
5D Parallelism for Large Model Training
Chapter 25: Sequence Parallelism from Scratch
Section: Sequence and Context Parallelism

Read this chapter: https://books.vizuara.ai/read/5d-parallelism/sequence-parallelism-from-scratch

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
import torch.distributed as dist

def all_gather_seq(x_shard, world):        # g:  (s/world, d) -> (s, d)
    parts = [torch.empty_like(x_shard) for _ in range(world)]
    dist.all_gather(parts, x_shard.contiguous())
    return torch.cat(parts, dim=0)         # concat along the SEQUENCE axis

def reduce_scatter_seq(x_full, world):     # ḡ:  (s, d) partial -> (s/world, d)
    s = x_full.shape[0]
    chunks = list(x_full.chunk(world, dim=0))          # split by sequence
    out = torch.empty_like(chunks[0])
    dist.reduce_scatter(out, chunks, op=dist.ReduceOp.SUM)
    return out                             # my sequence shard of the summed result

# --- block 2 ---
class SequenceParallelLayerNorm(torch.nn.Module):
    def __init__(self, d, device):
        super().__init__()
        self.ln = torch.nn.LayerNorm(d).to(device)   # ordinary LayerNorm

    def forward(self, x_seq_shard):        # x: (s/world, d) — e.g. (2, 8)
        return self.ln(x_seq_shard)        # per-token, per-feature: no collective!

# --- block 3 ---
d, world = 8, dist.get_world_size()
rank = dist.get_rank()
device = torch.device(f"cuda:{rank}")

col = ColumnParallelLinear(d, d, world, rank, device, gather_output=False)
row = RowParallelLinear(d, d, world, rank, device)
ln  = SequenceParallelLayerNorm(d, device)

# input starts SEQUENCE-sharded: rank 0 has tokens 0-1, rank 1 has tokens 2-3
x_full  = torch.randn(4, d, device=device)          # same seed on both ranks
x_shard = x_full.chunk(world, dim=0)[rank]          # (2, 8) — my two tokens

# --- the block ---
h_full    = all_gather_seq(x_shard, world)          # g:  (4, 8) full sequence for the matmul
h_col     = col(h_full)                             # (4, 4) feature-split, NO collective
h_partial = row.forward_no_reduce(h_col)            # (4, 8) full-width PARTIAL sum
h_shard   = reduce_scatter_seq(h_partial, world)    # ḡ:  (2, 8) my summed sequence shard
y_shard   = ln(h_shard)                             # SP LayerNorm on (2, 8), local

# --- block 4 ---
y_full = all_gather_seq(y_shard, world)             # (4, 8) — reassemble to compare
if rank == 0:
    Wc = gather_full_weight(col.W)                  # (8, 8)
    Wr = gather_full_weight(row.W, dim=0)           # (8, 8)
    ref = torch.nn.functional.layer_norm(
              (x_full @ Wc) @ Wr, (d,),
              ln.ln.weight, ln.ln.bias)             # single-GPU truth
    print(torch.allclose(y_full, ref, atol=1e-5))   # -> True

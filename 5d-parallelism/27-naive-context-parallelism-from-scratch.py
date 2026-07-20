"""
5D Parallelism for Large Model Training
Chapter 27: Naive Context Parallelism from Scratch
Section: Sequence and Context Parallelism

Read this chapter: https://books.vizuara.ai/read/5d-parallelism/naive-context-parallelism-from-scratch

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch, torch.distributed as dist
import torch.nn.functional as F

def naive_context_parallel_attention(Q_local, K_local, V_local, world):
    # Q_local, K_local, V_local: (s_local, d) — this rank's shard of the sequence.
    s_local, d = K_local.shape

    # (1) All-gather K and V so every rank holds the FULL-length keys and values.
    K_parts = [torch.empty_like(K_local) for _ in range(world)]
    V_parts = [torch.empty_like(V_local) for _ in range(world)]
    dist.all_gather(K_parts, K_local)          # every rank now has all K shards
    dist.all_gather(V_parts, V_local)
    K_full = torch.cat(K_parts, dim=0)          # (s_local * world, d) = full sequence
    V_full = torch.cat(V_parts, dim=0)

    # (2) Ordinary attention: local queries against the FULL keys/values.
    scores  = Q_local @ K_full.T / d**0.5       # (s_local, s_full)
    weights = F.softmax(scores, dim=-1)          # each row sums to 1
    return weights @ V_full                      # (s_local, d) — this rank's output slice

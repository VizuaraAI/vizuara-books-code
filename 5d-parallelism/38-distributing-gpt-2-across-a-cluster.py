"""
5D Parallelism for Large Model Training
Chapter 38: Distributing GPT-2 Across a Cluster
Section: Putting It All Together

Read this chapter: https://books.vizuara.ai/read/5d-parallelism/distributing-gpt-2-across-a-cluster

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import os

# --- block 1 ---
import torch, torch.distributed as dist
dist.init_process_group(backend="nccl")        # every rank finds every other rank
rank       = dist.get_rank()                    # my flat global rank, 0..7
local_rank = int(os.environ["LOCAL_RANK"])      # my index on THIS node
torch.cuda.set_device(local_rank)               # pin me to one physical GPU

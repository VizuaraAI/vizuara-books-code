"""
5D Parallelism for Large Model Training
Chapter 17: Implementing ZeRO from Scratch
Section: ZeRO and Sharded Data Parallelism

Read this chapter: https://books.vizuara.ai/read/5d-parallelism/implementing-zero-from-scratch

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch, torch.distributed as dist

class ShardedLinear(torch.nn.Module):
    def __init__(self, full_weight, rank, world):
        super().__init__()
        flat = full_weight.flatten()                 # W as a 1-D vector
        self.numel, self.shape = flat.numel(), full_weight.shape
        chunk = self.numel // world                   # this toy assumes it divides
        # each rank PERMANENTLY stores only its slice:
        self.shard = flat[rank*chunk:(rank+1)*chunk].clone().cuda()
        self.rank, self.world, self.chunk = rank, world, chunk

    def gather_full_weight(self):
        # all-gather every rank's shard into the complete flat weight
        buffers = [torch.empty(self.chunk, device="cuda") for _ in range(self.world)]
        dist.all_gather(buffers, self.shard)          # everyone now has all shards
        return torch.cat(buffers).view(self.shape)    # reassemble W

    def forward(self, x):
        W = self.gather_full_weight()                 # 1. GATHER (full W materialised)
        y = x @ W.T                                    # 2. COMPUTE on the full weight
        del W                                          # 3. FREE (back to just the shard)
        return y

# --- block 2 ---
import deepspeed
from transformers import AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-hf")

engine, opt, _, _ = deepspeed.initialize(
    model=model,
    model_parameters=model.parameters(),
    config="ds_config.json",              # the JSON above
)

for batch in dataloader:                   # your fine-tuning data
    loss = engine(**batch).loss
    engine.backward(loss)                  # DeepSpeed inserts the reduce-scatters
    engine.step()                          # sharded optimizer step + param regather

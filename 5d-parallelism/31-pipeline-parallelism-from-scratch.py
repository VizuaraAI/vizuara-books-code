"""
5D Parallelism for Large Model Training
Chapter 31: Pipeline Parallelism from Scratch
Section: Pipeline Parallelism

Read this chapter: https://books.vizuara.ai/read/5d-parallelism/pipeline-parallelism-from-scratch

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch.nn as nn

layers = [
    Embedding(vocab=50257, d_model=768),   # tokens → (seq, 768)
    Block(d_model=768, n_heads=12),        # transformer block 0
    Block(d_model=768, n_heads=12),        # transformer block 1
    LayerNorm(768),                        # final norm
    LMHead(d_model=768, vocab=50257),      # (seq, 768) → (seq, 50257) logits
]
model = nn.Sequential(*layers)

# --- block 2 ---
from deepspeed.pipe import PipelineModule, LayerSpec

model = PipelineModule(
    layers=[
        LayerSpec(Embedding, 50257, 768),
        *[LayerSpec(Block, 768, 12) for _ in range(12)],   # 12 GPT-2 blocks
        LayerSpec(LayerNorm, 768),
        LayerSpec(LMHead, 768, 50257),
    ],
    num_stages=2,                 # split across 2 GPUs
    loss_fn=cross_entropy,        # applied on the LAST stage only
    partition_method="parameters" # balance stages by parameter count
)

# --- block 3 ---
engine, _, _, _ = deepspeed.initialize(
    model=model, config=ds_config, model_parameters=model.parameters()
)

for step in range(num_steps):
    loss = engine.train_batch(data_iter)   # ← the entire micro-batched schedule
    if step % 100 == 0 and engine.is_last_stage():
        print(f"step {step}  loss {loss.item():.4f}")

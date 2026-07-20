"""
5D Parallelism for Large Model Training
Chapter 12: Profiling with TensorBoard
Section: Data Parallelism

Read this chapter: https://books.vizuara.ai/read/5d-parallelism/profiling-with-tensorboard

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
from torch.profiler import profile, schedule, tensorboard_trace_handler, ProfilerActivity

prof = profile(
    activities=[ProfilerActivity.CPU, ProfilerActivity.CUDA],
    schedule=schedule(wait=1, warmup=2, active=3),      # skip 1, warm 2, record 3
    on_trace_ready=tensorboard_trace_handler("./log/dp2"),
    record_shapes=True, with_stack=True,
)

with prof:
    for step, micro in enumerate(local_loader):
        loss = model(micro).loss
        loss.backward()
        all_reduce_average(model, world)   # the sync from the DP chapter
        opt.step(); opt.zero_grad()
        prof.step()                        # ← tell the profiler a step ended

"""
5D Parallelism for Large Model Training
Chapter 39: Build an SLM with 5D Parallelism
Section: Putting It All Together

Read this chapter: https://books.vizuara.ai/read/5d-parallelism/build-an-slm-with-5d-parallelism

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# The model
d_model   = 16      # residual / embedding width
n_layers  = 8       # transformer blocks
seq_len   = 8       # tokens per sequence (long-context toy)
n_experts = 4       # E — this is an MoE SLM
top_k     = 1       # each token visits one expert

# The cluster: 8 GPUs = one node, all on NVLink for this toy
DP, TP, CP, PP, EP = 2, 2, 2, 2, 2   # the five (+EP) axes

# --- block 2 ---
# The 5D plan as a config — the framework maps ranks to (dp, pp, tp) itself
parallelism = dict(
    data_parallel=2, tensor_parallel=2, pipeline_parallel=2,
    sequence_parallel=True,      # rides on tensor_parallel, free activation win
    context_parallel=2,          # ring attention over the sequence
    expert_parallel=2,           # experts scattered across the pair
    zero_stage=1,                # shard optimizer states across DP replicas
)

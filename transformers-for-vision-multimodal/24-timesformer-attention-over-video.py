"""
Transformers for Vision & Multimodal LLMs
Chapter 24: TimeSformer — Attention Over Video
Section: Video & Multimodal Models

Read this chapter: https://books.vizuara.ai/read/transformers-for-vision-multimodal/timesformer-attention-over-video

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def divided_block(x):                 # x: (B, F, N, D)
    # 1. TEMPORAL: attend across frames, per spatial location
    xt = x.permute(0, 2, 1, 3)        # (B, N, F, D) — time is now the sequence axis
    xt = xt.reshape(B * N, F, D)      # N independent length-F sequences
    x  = x + time_attn(xt).reshape(B, N, F, D).permute(0, 2, 1, 3)

    # 2. SPATIAL: attend within each frame
    xs = x.reshape(B * F, N, D)       # F independent length-N sequences
    x  = x + space_attn(xs).reshape(B, F, N, D)

    # 3. position-wise feed-forward, as usual
    x  = x + mlp(ln(x))
    return x

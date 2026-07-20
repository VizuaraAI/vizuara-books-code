"""
5D Parallelism for Large Model Training
Chapter 23: The Long-Sequence Memory Wall
Section: Sequence and Context Parallelism

Read this chapter: https://books.vizuara.ai/read/5d-parallelism/the-long-sequence-memory-wall

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
d = 8            # hidden dimension
bytes_per = 2    # bf16

for s in [4, 128, 8192, 131072]:
    per_token = s * d * bytes_per          # (s, d)  MLP-style activation
    attn      = s * s * bytes_per          # (s, s)  attention score matrix
    print(f"s={s:>7}:  per-token={per_token:>14,} B   attention={attn:>18,} B")

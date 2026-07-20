"""
5D Parallelism for Large Model Training
Chapter 34: Expert Parallelism Explained
Section: Expert Parallelism and MoE

Read this chapter: https://books.vizuara.ai/read/5d-parallelism/expert-parallelism-explained

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# tokens: (n_tokens, d_model) held on THIS GPU
# expert_id: (n_tokens,) top-1 assignment from the router

# 1. sort tokens into one bucket per destination GPU
send_buckets = bucket_by_owning_gpu(tokens, expert_id)   # EP buckets

# 2. DISPATCH: transpose token buckets across the EP group
recv = all_to_all(send_buckets)                          # now holds tokens for MY experts

# 3. run local experts — pure matmuls, no communication
out = run_local_experts(recv)

# 4. COMBINE: send processed tokens back to their origin GPU
tokens_out = all_to_all(out)                             # dispatch, in reverse

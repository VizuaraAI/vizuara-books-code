"""
5D Parallelism for Large Model Training
Chapter 26: Context Parallelism and Ring Attention
Section: Sequence and Context Parallelism

Read this chapter: https://books.vizuara.ai/read/5d-parallelism/context-parallelism-and-ring-attention

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
scores = Q @ K.T          # shape (4, 4): every query dotted with every key
weights = softmax(scores) # each row sums to 1
out = weights @ V         # shape (4, 8): relevance-weighted blend of values

# --- block 2 ---
# state per query row: m (running max), l (running denom), o (running output)
for kv_block in ring:                 # blocks arrive one per ring step
    s = q @ kv_block.k.T               # raw scores for THIS block only
    m_new = max(m, s.max())            # extend the running max
    p = exp(s - m_new)                 # exponentiate against the new max
    alpha = exp(m - m_new)             # rescale factor for the OLD state
    l = alpha * l + p.sum()            # correct the running denominator
    o = alpha * o + p @ kv_block.v     # correct the running output
    m = m_new
out = o / l                            # normalize once, at the very end

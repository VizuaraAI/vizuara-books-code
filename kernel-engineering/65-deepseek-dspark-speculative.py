"""
Kernel Engineering
Chapter 65: DSpark: speculative decoding as a kernel problem
Section: The Frontier

Read this chapter: https://books.vizuara.ai/read/kernel-engineering/deepseek-dspark-speculative

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# draft: sequential, cheap, greedy — captured as ONE cuda graph
draft_tokens = []
h = target_hidden_state          # reuse the target's last hidden state
for _ in range(num_speculative_tokens):   # 7
    logits = mtp_head(h)         # ~one transformer layer of work
    tok = logits.argmax(-1)      # greedy: no sampling kernel needed
    draft_tokens.append(tok)
    h = mtp_head.step(h, tok)    # advance the draft state

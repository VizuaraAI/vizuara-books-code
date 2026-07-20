"""
Generative AI Fundamentals
Chapter 39: Connecting Vision to Language
Section: Multimodal LLMs

Read this chapter: https://books.vizuara.ai/read/generative-ai-fundamentals/connecting-vision-to-language

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# LLaVA-style forward pass — the whole idea in a dozen lines
img_feats  = clip_vit(image)                 # (196, 768)  — FROZEN
img_tokens = projection(img_feats)           # (196, 4096) — the ONLY trained part
txt_tokens = llm.embed(tokenize(prompt))     # (T,   4096) — FROZEN embedding table

seq = concat([img_tokens, txt_tokens], dim=0)  # (196 + T, 4096): image tokens go first
logits = llm(seq)                            # FROZEN transformer, ordinary self-attention
next_id = sample(logits[-1])                 # same greedy / top-k / top-p as always

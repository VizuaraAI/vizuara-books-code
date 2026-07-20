"""
Generative AI Fundamentals
Chapter 38: BLIP: Multimodal Text Generation
Section: Multimodal LLMs

Read this chapter: https://books.vizuara.ai/read/generative-ai-fundamentals/blip-multimodal-generation

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# Pseudocode for BLIP captioning — the autoregressive loop
image_vectors = image_encoder(image)      # (197, 768): the picture, as vectors
tokens = [BOS]                             # start of sequence

while tokens[-1] != EOS and len(tokens) < max_len:
    # causal self-attention over tokens so far, THEN
    # cross-attention into image_vectors (this is where vision enters)
    logits = decoder(tokens, cross_attend_to=image_vectors)  # (vocab_size,)
    next_id = sample(logits)               # greedy / top-k / top-p
    tokens.append(next_id)

caption = detokenize(tokens)               # "a dog wearing sunglasses on a skateboard"

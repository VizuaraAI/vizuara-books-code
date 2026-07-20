"""
Generative AI Fundamentals
Chapter 40: The Multimodal Landscape
Section: Multimodal LLMs

Read this chapter: https://books.vizuara.ai/read/generative-ai-fundamentals/the-multimodal-landscape

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import clip, torch
model, preprocess = clip.load("ViT-B/32")

image = preprocess(img).unsqueeze(0)                      # (1, 3, 224, 224)
labels = ["a photo of a dog", "a photo of a cat"]
text = clip.tokenize(labels)

img_emb  = model.encode_image(image)                      # (1, 512)
text_emb = model.encode_text(text)                        # (2, 512)

img_emb  = img_emb  / img_emb.norm(dim=-1, keepdim=True)  # L2-normalize
text_emb = text_emb / text_emb.norm(dim=-1, keepdim=True)
sims = (img_emb @ text_emb.T)                             # (1, 2) cosine scores

"""
Generative AI Fundamentals
Chapter 37: CLIP: Multimodal Embeddings
Section: Multimodal LLMs

Read this chapter: https://books.vizuara.ai/read/generative-ai-fundamentals/clip-multimodal-embeddings

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import torch
import torch.nn.functional as F

# --- block 1 ---
# image_features: (N, 512)   text_features: (N, 512)
image_features = F.normalize(image_features, dim=-1)  # unit length
text_features  = F.normalize(text_features,  dim=-1)

logits = (image_features @ text_features.T) * temperature.exp()  # (N, N) grid
labels = torch.arange(N)          # correct pair for row i is column i

loss_i2t = F.cross_entropy(logits,   labels)  # each image picks its caption
loss_t2i = F.cross_entropy(logits.T, labels)  # each caption picks its image
loss = (loss_i2t + loss_t2i) / 2

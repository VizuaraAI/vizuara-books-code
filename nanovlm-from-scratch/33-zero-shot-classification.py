"""
Build a NanoVLM from Scratch
Chapter 33: Zero-Shot Classification
Section: Training, Evaluation & Beyond

Read this chapter: https://books.vizuara.ai/read/nanovlm-from-scratch/zero-shot-classification

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
import torch.nn.functional as F

@torch.no_grad()
def zero_shot_classify(model, image, labels, template="a photo of a {}"):
    # 1. Build one prompt per candidate label, encode to class vectors.
    prompts   = [template.format(label) for label in labels]
    text_emb  = model.encode_text(prompts)        # (num_labels, d), L2-normalized
    # 2. Encode the query image to a single vector.
    img_emb   = model.encode_image(image[None])   # (1, d), L2-normalized
    # 3. Cosine similarity == dot product (both are unit vectors).
    logit_scale = model.logit_scale.exp()          # learned temperature
    logits      = logit_scale * img_emb @ text_emb.T   # (1, num_labels)
    probs       = logits.softmax(dim=-1)           # class probabilities
    # 4. Argmax is the prediction.
    best = probs.argmax(dim=-1).item()
    return labels[best], probs[0]

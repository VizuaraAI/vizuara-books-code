"""
Build a NanoVLM from Scratch
Chapter 34: Image-Text Retrieval
Section: Training, Evaluation & Beyond

Read this chapter: https://books.vizuara.ai/read/nanovlm-from-scratch/image-text-retrieval

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch

@torch.no_grad()
def build_similarity(model, images, captions):
    img_emb = model.encode_image(images)     # (N_img, d), L2-normalized
    txt_emb = model.encode_text(captions)    # (N_cap, d), L2-normalized
    return img_emb @ txt_emb.T                # (N_img, N_cap) cosine grid

@torch.no_grad()
def retrieve_captions(model, image, captions, k=5):
    # image-to-text: one image query, rank the whole caption gallery.
    scores = build_similarity(model, image[None], captions)[0]  # (N_cap,)
    top = scores.topk(k)                       # values + indices, sorted desc
    return [(captions[i], top.values[j].item())
            for j, i in enumerate(top.indices.tolist())]

def recall_at_k(sim, k):
    # sim: (N, N) with the true match on the diagonal (row i ↔ column i).
    ranks = sim.argsort(dim=-1, descending=True)      # per-row ranking
    labels = torch.arange(sim.size(0)).unsqueeze(1)   # the true index per row
    hit = (ranks[:, :k] == labels).any(dim=-1)        # did the diagonal land in top-k?
    return hit.float().mean().item()

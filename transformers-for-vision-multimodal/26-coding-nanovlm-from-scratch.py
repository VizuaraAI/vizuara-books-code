"""
Transformers for Vision & Multimodal LLMs
Chapter 26: Coding NanoVLM — Your First Vision-Language Model
Section: Video & Multimodal Models

Read this chapter: https://books.vizuara.ai/read/transformers-for-vision-multimodal/coding-nanovlm-from-scratch

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import torch

# --- block 1 ---
import torch.nn as nn

# d_vis = vision encoder width (e.g. 1024 for CLIP ViT-L)
# d_llm = language model embedding width (e.g. 768)
projection = nn.Linear(d_vis, d_llm)   # W: (1024 → 768), plus a bias
image_tokens = projection(vision_features)   # (N, 1024) -> (N, 768)

# --- block 2 ---
class NanoVLM(nn.Module):
    def __init__(self, vision_encoder, language_model, d_vis, d_llm):
        super().__init__()
        self.vision = vision_encoder          # frozen CLIP ViT
        self.projection = nn.Linear(d_vis, d_llm)   # the bridge — trained
        self.lm = language_model              # frozen LLM

    def forward(self, image, text_ids, image_slot):
        # 1. encode the image -> (N, d_vis) image tokens
        with torch.no_grad():
            vis = self.vision(image)          # (N, 1024)
        # 2. translate into the LLM's space -> (N, d_llm)
        img_tokens = self.projection(vis)     # (N, 768)
        # 3. embed the text, then splice image tokens into the <image> slot
        text_embeds = self.lm.embed(text_ids) # (T, 768)
        seq = splice(text_embeds, img_tokens, at=image_slot)  # (N+T-1, 768)
        # 4. an ordinary language model from here on
        return self.lm(seq)                   # next-token logits

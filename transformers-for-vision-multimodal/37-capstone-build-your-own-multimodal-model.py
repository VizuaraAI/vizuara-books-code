"""
Transformers for Vision & Multimodal LLMs
Chapter 37: Capstone — Build Your Own Multimodal Model
Section: Putting It All Together

Read this chapter: https://books.vizuara.ai/read/transformers-for-vision-multimodal/capstone-build-your-own-multimodal-model

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch, torch.nn as nn

class CapstoneVLM(nn.Module):
    def __init__(self, vision_encoder, language_model, d_vis=1024, d_llm=768):
        super().__init__()
        self.vision = vision_encoder      # frozen
        self.llm    = language_model      # frozen
        self.connector = nn.Linear(d_vis, d_llm)   # the ONLY trained part (stage 1)
        for p in self.vision.parameters():   p.requires_grad = False
        for p in self.llm.parameters():      p.requires_grad = False

    def forward(self, image, text_ids):
        with torch.no_grad():
            img_tok = self.vision(image)             # (B, N, 1024)
        img_tok = self.connector(img_tok)            # (B, N, 768)
        txt_tok = self.llm.embed(text_ids)           # (B, T, 768)
        seq = torch.cat([img_tok, txt_tok], dim=1)   # (B, N+T, 768)
        return self.llm(inputs_embeds=seq)           # logits over vocab

"""
Transformers for Vision & Multimodal LLMs
Chapter 22: Coding DETR From Scratch
Section: Hierarchical & Dense Vision Transformers

Read this chapter: https://books.vizuara.ai/read/transformers-for-vision-multimodal/coding-detr-from-scratch

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch, torch.nn as nn, torchvision

class Backbone(nn.Module):
    def __init__(self, d_model=256):
        super().__init__()
        resnet = torchvision.models.resnet50(weights="DEFAULT")
        # keep everything up to (and including) the last conv stage
        self.body = nn.Sequential(*list(resnet.children())[:-2])  # -> (B, 2048, H/32, W/32)
        self.proj = nn.Conv2d(2048, d_model, kernel_size=1)       # 2048 -> 256 channels

    def forward(self, x):                 # x: (B, 3, H, W)
        f = self.body(x)                  # (B, 2048, H/32, W/32)
        f = self.proj(f)                  # (B, 256,  H/32, W/32)
        B, C, Hf, Wf = f.shape
        tokens = f.flatten(2).permute(2, 0, 1)  # (Hf*Wf, B, 256)  <- sequence-first
        return tokens, (Hf, Wf)

# --- block 2 ---
class DETR(nn.Module):
    def __init__(self, num_classes, d_model=256, nhead=8, n_layers=6, num_queries=100):
        super().__init__()
        self.backbone = Backbone(d_model)
        self.transformer = nn.Transformer(d_model, nhead, n_layers, n_layers,
                                          dim_feedforward=2048, batch_first=False)
        self.query_embed = nn.Embedding(num_queries, d_model)   # 100 learned queries
        self.class_head  = nn.Linear(d_model, num_classes + 1)  # +1 for the "no object" class
        self.bbox_head   = nn.Sequential(                       # a tiny 3-layer MLP
            nn.Linear(d_model, d_model), nn.ReLU(),
            nn.Linear(d_model, d_model), nn.ReLU(),
            nn.Linear(d_model, 4))

    def forward(self, images):
        src, (Hf, Wf) = self.backbone(images)          # (HW, B, 256)
        src = src + pos_encoding_2d(Hf, Wf, src.device) # add 2D position (sketched)
        B = images.shape[0]
        queries = self.query_embed.weight.unsqueeze(1).repeat(1, B, 1)  # (100, B, 256)
        tgt = torch.zeros_like(queries)
        hs = self.transformer(src, tgt, tgt_key_padding_mask=None,      # decode
                              memory_key_padding_mask=None,
                              tgt_is_causal=False)     # (100, B, 256)
        hs = hs.transpose(0, 1)                        # (B, 100, 256)
        return {"logits": self.class_head(hs),         # (B, 100, C+1)
                "boxes":  self.bbox_head(hs).sigmoid()}# (B, 100, 4) in [0,1]

# --- block 3 ---
from scipy.optimize import linear_sum_assignment
row_ind, col_ind = linear_sum_assignment(cost_matrix)  # optimal 1-to-1 assignment

# --- block 4 ---
loss = 0.0
for i, j in zip(row_ind, col_ind):           # matched pairs
    loss += cross_entropy(logits[i], target_class[j])
    if target_class[j] != NO_OBJECT:
        loss += 5.0 * l1_loss(boxes[i], target_box[j])   # λ_L1 = 5
        loss += 2.0 * giou_loss(boxes[i], target_box[j]) # λ_giou = 2

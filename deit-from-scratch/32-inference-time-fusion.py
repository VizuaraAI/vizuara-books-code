"""
Build a Data-Efficient Image Transformer (DeiT) from Scratch
Chapter 32: Inference-Time Fusion
Section: The Distillation Token

Read this chapter: https://books.vizuara.ai/read/deit-from-scratch/inference-time-fusion

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def forward(self, x):
    cls_out, dist_out = self.forward_features(x)   # each (B, 1000)
    if self.training:
        return cls_out, dist_out                   # two logits -> two losses
    # inference: fuse the two heads into one prediction
    return (cls_out.softmax(dim=-1) + dist_out.softmax(dim=-1)) / 2

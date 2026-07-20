"""
Build a Vision Transformer (ViT) from Scratch
Chapter 25: Parameter Initialization
Section: Assembling the Full ViT

Read this chapter: https://books.vizuara.ai/read/vit-from-scratch/parameter-initialization

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import torch
import torch.nn as nn

# --- block 1 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# import torch
# import torch.nn as nn
#
# class ViT(nn.Module):
#     def __init__(self, ...):
#         super().__init__()
#         # ... build patch_embed, cls_token, pos_embed, encoder blocks, head ...
#
#         # special learnable tensors: small truncated-normal
#         nn.init.trunc_normal_(self.pos_embed, std=0.02)
#         nn.init.trunc_normal_(self.cls_token, std=0.02)
#
#         # every Linear / LayerNorm gets the recipe below
#         self.apply(self._init_weights)
#
#     def _init_weights(self, m):
#         if isinstance(m, nn.Linear):
#             nn.init.trunc_normal_(m.weight, std=0.02)
#             if m.bias is not None:
#                 nn.init.zeros_(m.bias)
#         elif isinstance(m, nn.Conv2d):                 # the patch projection
#             nn.init.trunc_normal_(m.weight, std=0.02)
#             if m.bias is not None:
#                 nn.init.zeros_(m.bias)
#         elif isinstance(m, nn.LayerNorm):
#             nn.init.ones_(m.weight)                    # γ = 1
#             nn.init.zeros_(m.bias)                      # β = 0

# --- block 2 ---
torch.manual_seed(0)
layer = nn.Linear(8, 8)
nn.init.trunc_normal_(layer.weight, std=0.02)
nn.init.zeros_(layer.bias)

x = torch.randn(1000, 8)                 # 1000 samples, variance ≈ 1
print(x.var().item())                    # ≈ 1.00
print(layer(x).var().item())             # ≈ 8 × 0.02² ≈ 0.0032

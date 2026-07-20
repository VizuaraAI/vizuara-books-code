"""
Build a Vision Transformer (ViT) from Scratch
Chapter 27: End-to-End Forward Pass
Section: Assembling the Full ViT

Read this chapter: https://books.vizuara.ai/read/vit-from-scratch/forward-pass-shape-check

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch

model = ViT(
    image_size=224, patch_size=16, in_channels=3,
    embed_dim=768, depth=12, num_heads=12,
    mlp_dim=3072, num_classes=1000,
)
model.eval()

B = 4
x = torch.randn(B, 3, 224, 224)          # a fake batch of NCHW images
with torch.no_grad():
    logits = model(x)

print(logits.shape)                       # torch.Size([4, 1000])
assert logits.shape == (B, 1000), "head output shape is wrong!"

# --- block 2 ---
def trace_shapes(model, x):
    seen = {}
    def hook(name):
        def fn(_m, _in, out):
            t = out[0] if isinstance(out, tuple) else out
            seen[name] = tuple(t.shape)
        return fn
    handles = [
        model.patch_embed.register_forward_hook(hook("after_patch_embed")),
        model.encoder.register_forward_hook(hook("after_encoder")),
    ]
    with torch.no_grad():
        model(x)
    for h in handles:
        h.remove()
    return seen

print(trace_shapes(model, x))
# {'after_patch_embed': (4, 196, 768), 'after_encoder': (4, 197, 768)}

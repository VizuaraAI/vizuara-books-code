"""
Build a Vision Transformer (ViT) from Scratch
Chapter 23: The Classification Head
Section: Assembling the Full ViT

Read this chapter: https://books.vizuara.ai/read/vit-from-scratch/the-classification-head

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# x is the encoder output, shape (B, N+1, D) = (B, 197, 768)
cls = x[:, 0]        # take position 0 only  -> (B, D) = (B, 768)

# --- block 2 ---
cls = self.norm(cls)      # nn.LayerNorm(D), still (B, 768)

# --- block 3 ---
logits = self.head(cls)   # nn.Linear(768, num_classes) -> (B, num_classes)

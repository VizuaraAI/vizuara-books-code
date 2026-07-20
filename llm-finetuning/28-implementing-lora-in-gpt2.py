"""
LLM Finetuning
Chapter 28: Implementing LoRA in GPT-2
Section: Parameter-Efficient Finetuning (PEFT)

Read this chapter: https://books.vizuara.ai/read/llm-finetuning/implementing-lora-in-gpt2

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
import torch.nn as nn

class LoRALinear(nn.Module):
    def __init__(self, base_linear: nn.Linear, r: int = 8, alpha: int = 16):
        super().__init__()
        self.base = base_linear                    # the pretrained layer, kept whole
        self.base.weight.requires_grad = False     # FREEZE W
        if self.base.bias is not None:
            self.base.bias.requires_grad = False   # freeze bias too

        in_f, out_f = base_linear.in_features, base_linear.out_features
        self.A = nn.Parameter(torch.randn(r, in_f) * 0.01)  # r × k, random
        self.B = nn.Parameter(torch.zeros(out_f, r))        # d × r, ZERO
        self.scaling = alpha / r                             # the α/r factor

    def forward(self, x):
        base_out = self.base(x)                    # W·x  (frozen path)
        lora_out = (x @ self.A.T) @ self.B.T       # (B·A)·x, computed A first
        return base_out + self.scaling * lora_out  # h = W·x + (α/r)·(B·A)·x

# --- block 2 ---
def add_lora(model, target_names=("c_attn",), r=8, alpha=16):
    for name, module in model.named_modules():
        for child_name, child in module.named_children():
            if child_name in target_names and isinstance(child, nn.Linear):
                wrapped = LoRALinear(child, r=r, alpha=alpha)
                setattr(module, child_name, wrapped)   # swap in place
    return model

# --- block 3 ---
# 1. freeze absolutely everything the pretrained model shipped with
for p in model.parameters():
    p.requires_grad = False

# 2. inject adapters — their A and B are created with requires_grad=True
model = add_lora(model, target_names=("c_attn",), r=8, alpha=16)

# 3. sanity check: how much are we actually training?
trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
total     = sum(p.numel() for p in model.parameters())
print(f"trainable: {trainable:,} / {total:,}  ({100*trainable/total:.3f}%)")

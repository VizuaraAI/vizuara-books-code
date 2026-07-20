"""
LLM Finetuning
Chapter 30: Tuning LoRA Hyperparameters
Section: Parameter-Efficient Finetuning (PEFT)

Read this chapter: https://books.vizuara.ai/read/llm-finetuning/tuning-lora-hyperparameters

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from peft import LoraConfig

config = LoraConfig(
    r=8,                       # 1. capacity: 8 is a strong default
    lora_alpha=16,             # 2. volume: α/r = 2.0, in the sweet spot
    target_modules=["q_proj", "v_proj"],  # 3. where: start minimal
    lora_dropout=0.0,          # 4. brake: 0 to start, raise if val loss climbs
    bias="none",
)

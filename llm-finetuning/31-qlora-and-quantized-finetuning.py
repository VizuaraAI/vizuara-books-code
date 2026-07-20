"""
LLM Finetuning
Chapter 31: QLoRA and Quantized Finetuning
Section: Parameter-Efficient Finetuning (PEFT)

Read this chapter: https://books.vizuara.ai/read/llm-finetuning/qlora-and-quantized-finetuning

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from transformers import AutoModelForCausalLM, BitsAndBytesConfig
from peft import LoraConfig, get_peft_model
import torch

# 1. Ask for the base weights in 4-bit NF4, with double quantization.
bnb = BitsAndBytesConfig(
    load_in_4bit=True,               # store frozen weights in 4 bits
    bnb_4bit_quant_type="nf4",       # the NormalFloat-4 data type
    bnb_4bit_use_double_quant=True,  # quantize the scales too
    bnb_4bit_compute_dtype=torch.bfloat16,  # de-quantize to bf16 for matmuls
)

base = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-2-7b-hf", quantization_config=bnb, device_map="auto",
)

# 2. Attach ordinary LoRA adapters — the base stays frozen and quantized.
lora = LoraConfig(r=16, lora_alpha=32, lora_dropout=0.05,
                  target_modules=["q_proj", "v_proj"], task_type="CAUSAL_LM")
model = get_peft_model(base, lora)   # only A, B are trainable

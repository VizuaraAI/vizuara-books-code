"""
LLM Production & Deployment
Chapter 8: Quantization for Local Inference
Section: Efficient Inference at Scale

Read this chapter: https://books.vizuara.ai/read/llm-production-deployment/quantization-for-local-inference

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo fixups: names the book uses but this chapter does not define ---
w = None        # TODO: one float weight from the tensor being quantized.
min_val = None  # TODO: the smallest weight value in that tensor.
scale = None    # TODO: the gap between two neighbouring integer codes.
# --- end fixups ---

# --- block 1 ---
# quantize: float -> 8-bit integer code
q = round((w - min_val) / scale)          # an int in [0, 255]

# dequantize: integer code -> approximate float
w_hat = q * scale + min_val               # back near the original

# --- block 2 ---
from transformers import AutoModelForCausalLM, BitsAndBytesConfig
import torch

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,                      # 4-bit weights
    bnb_4bit_quant_type="nf4",              # bell-curve-spaced ticks
    bnb_4bit_compute_dtype=torch.bfloat16,  # math still runs in bf16
    bnb_4bit_use_double_quant=True,         # quantize the scales too
)

model = AutoModelForCausalLM.from_pretrained(
    "openai/gpt-oss-20b",
    quantization_config=bnb_config,
    device_map="auto",
)

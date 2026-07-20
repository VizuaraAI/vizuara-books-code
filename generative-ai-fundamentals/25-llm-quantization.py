"""
Generative AI Fundamentals
Chapter 25: LLM Quantization
Section: Agents & LangChain

Read this chapter: https://books.vizuara.ai/read/generative-ai-fundamentals/llm-quantization

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from transformers import AutoModelForCausalLM, BitsAndBytesConfig

# ask for 4-bit NF4 quantization at load time
config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",       # the QLoRA-style grid
    bnb_4bit_compute_dtype="float16" # math still runs in FP16
)

model = AutoModelForCausalLM.from_pretrained(
    "some-org/some-7b-model",
    quantization_config=config,       # 14 GB in FP16 → ~3.5 GB loaded
)

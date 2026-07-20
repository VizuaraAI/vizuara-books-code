"""
LLM Production & Deployment
Chapter 34: Soft-Prompt & Prefix Tuning
Section: Finetuning LLMs

Read this chapter: https://books.vizuara.ai/read/llm-production-deployment/soft-prompt-and-prefix-tuning

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from peft import PromptTuningConfig, PrefixTuningConfig, get_peft_model
from transformers import AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained("gpt2")  # 124M params, will be frozen

# Soft prompt tuning: 20 virtual tokens at the input
soft = PromptTuningConfig(task_type="CAUSAL_LM", num_virtual_tokens=20)

# Prefix tuning: a learned key/value prefix at every layer
prefix = PrefixTuningConfig(task_type="CAUSAL_LM", num_virtual_tokens=10)

peft_model = get_peft_model(model, soft)     # or (model, prefix)
peft_model.print_trainable_parameters()
# trainable params: 15,360 || all params: 124,455,168 || trainable%: 0.0123

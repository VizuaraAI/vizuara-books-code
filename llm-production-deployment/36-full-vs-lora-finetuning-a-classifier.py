"""
LLM Production & Deployment
Chapter 36: Full vs LoRA Finetuning a Classifier
Section: Finetuning LLMs

Read this chapter: https://books.vizuara.ai/read/llm-production-deployment/full-vs-lora-finetuning-a-classifier

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from transformers import GPT2ForSequenceClassification

model = GPT2ForSequenceClassification.from_pretrained("gpt2", num_labels=2)
model.config.pad_token_id = model.config.eos_token_id   # GPT-2 has no pad token

# --- block 2 ---
for p in model.parameters():
    p.requires_grad = True          # everything trains — this is "full"

trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
print(f"{trainable:,} trainable")   # 124,441,346

# --- block 3 ---
from peft import LoraConfig, get_peft_model

config = LoraConfig(r=8, lora_alpha=16, target_modules=["c_attn"], task_type="SEQ_CLS")
model = get_peft_model(model, config)
model.print_trainable_parameters()
# trainable params: ~296,000 || all params: ~124,700,000 || trainable%: 0.24

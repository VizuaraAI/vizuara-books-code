"""
LLM Finetuning
Chapter 24: A Finetuning Project with Unsloth
Section: Finetuning with Hugging Face & Unsloth

Read this chapter: https://books.vizuara.ai/read/llm-finetuning/finetuning-project-with-unsloth

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from unsloth import FastLanguageModel

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name     = "unsloth/mistral-7b-v0.3-bnb-4bit",
    max_seq_length = 2048,
    load_in_4bit   = True,   # the "Q" in QLoRA: base weights in 4-bit NF4
    dtype          = None,   # let Unsloth pick bf16/fp16 for the GPU
)

# --- block 2 ---
model = FastLanguageModel.get_peft_model(
    model,
    r              = 16,              # LoRA rank — the width of the low-rank update
    lora_alpha     = 16,             # scaling; effective update scaled by alpha/r
    lora_dropout   = 0,
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                      "gate_proj", "up_proj", "down_proj"],
)

# --- block 3 ---
from trl import SFTTrainer
from transformers import TrainingArguments

trainer = SFTTrainer(
    model         = model,
    tokenizer     = tokenizer,
    train_dataset = dataset,          # instruction→response pairs, formatted
    dataset_text_field = "text",
    max_seq_length = 2048,
    args = TrainingArguments(
        per_device_train_batch_size = 2,
        gradient_accumulation_steps = 4,   # effective batch = 2 × 4 = 8
        warmup_steps      = 5,
        max_steps         = 60,
        learning_rate     = 2e-4,          # higher than full FT — only adapters move
        optim             = "adamw_8bit",  # 8-bit Adam: even the tiny state shrinks
        logging_steps     = 1,
    ),
)
trainer.train()

# --- block 4 ---
model.save_pretrained("my-mistral-lora")        # a few MB of A/B matrices
# later: reload the 4-bit base + apply this tiny adapter

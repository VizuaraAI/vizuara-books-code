"""
LLM Production & Deployment
Chapter 32: Finetuning with HuggingFace & Unsloth
Section: Finetuning LLMs

Read this chapter: https://books.vizuara.ai/read/llm-production-deployment/finetuning-with-huggingface-and-unsloth

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo fixups: names the book uses but this chapter does not define ---
dataset = None  # TODO: the training dataset handed to the SFTTrainer.
# --- end fixups ---

# --- block 1 ---
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments
from trl import SFTTrainer

model = AutoModelForCausalLM.from_pretrained("gpt2")
tokenizer = AutoTokenizer.from_pretrained("gpt2")

args = TrainingArguments(
    output_dir="gpt2-finetuned",
    per_device_train_batch_size=4,
    gradient_accumulation_steps=4,     # effective batch = 4 × 4 = 16
    num_train_epochs=3,
    learning_rate=2e-5,
    fp16=True,                          # mixed precision
    gradient_checkpointing=True,        # trade compute for activation memory
)

trainer = SFTTrainer(model=model, args=args, train_dataset=dataset)
trainer.train()

# --- block 2 ---
from unsloth import FastLanguageModel

model, tokenizer = FastLanguageModel.from_pretrained(
    "unsloth/llama-3-8b",
    max_seq_length=2048,
    load_in_4bit=True,                 # frozen 4-bit base → QLoRA territory
)
model = FastLanguageModel.get_peft_model(model, r=16)   # attach LoRA adapters

# hand this to the SAME SFTTrainer as before

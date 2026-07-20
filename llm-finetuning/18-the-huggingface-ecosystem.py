"""
LLM Finetuning
Chapter 18: The Hugging Face Ecosystem
Section: Finetuning with Hugging Face & Unsloth

Read this chapter: https://books.vizuara.ai/read/llm-finetuning/the-huggingface-ecosystem

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "roneneldan/TinyStories-33M"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# --- block 2 ---
enc = tokenizer("Once upon a time", return_tensors="pt")
# enc["input_ids"]  -> tensor of shape (1, 4)   : batch of 1, four token IDs
out = model(**enc)
# out.logits        -> tensor of shape (1, 4, V) : V = vocab size, e.g. 50257

# --- block 3 ---
from datasets import load_dataset

ds = load_dataset("roneneldan/TinyStories")
# ds["train"] is a Dataset; ds["train"][0] -> {"text": "Once upon a time ..."}

def tokenize(batch):
    return tokenizer(batch["text"], truncation=True, max_length=512)

tokenized = ds.map(tokenize, batched=True, remove_columns=["text"])

# --- block 4 ---
from transformers import TrainingArguments, Trainer, DataCollatorForLanguageModeling

args = TrainingArguments(
    output_dir="tinystories-ft",
    per_device_train_batch_size=8,
    num_train_epochs=1,
    learning_rate=5e-5,
    logging_steps=50,
)

collator = DataCollatorForLanguageModeling(tokenizer, mlm=False)

trainer = Trainer(
    model=model,
    args=args,
    train_dataset=tokenized["train"],
    data_collator=collator,
)
trainer.train()

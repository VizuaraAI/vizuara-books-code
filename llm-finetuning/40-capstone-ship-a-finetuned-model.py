"""
LLM Finetuning
Chapter 40: Capstone: Ship a Finetuned Model
Section: Putting It Together

Read this chapter: https://books.vizuara.ai/read/llm-finetuning/capstone-ship-a-finetuned-model

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
data = [
  {"instruction": "Rewrite politely: bug is on your end, clear your cache",
   "response": "Thanks for flagging this! It looks like a cached file may be causing the issue — could you try clearing your browser cache and reloading? That usually sorts it out."},
  {"instruction": "Rewrite politely: we don't support that, use the API",
   "response": "Great question! That isn't available in the dashboard today, but you can do it directly through our API — happy to point you to the docs."},
  # ... 4 more, same shape ...
]

PROMPT = "### Instruction:\n{instruction}\n\n### Response:\n{response}"

# --- block 2 ---
from unsloth import FastLanguageModel

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name   = "unsloth/tinyllama-bnb-4bit",
    max_seq_length = 1024,
    load_in_4bit = True,          # QLoRA: frozen 4-bit base
)

model = FastLanguageModel.get_peft_model(
    model,
    r              = 16,          # rank of the update
    lora_alpha     = 16,         # scaling; effective ΔW is scaled by α/r
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj"],
    lora_dropout   = 0.05,
)

# --- block 3 ---
model.save_pretrained("polite-support-adapter")   # a few MB: just A and B
tokenizer.save_pretrained("polite-support-adapter")

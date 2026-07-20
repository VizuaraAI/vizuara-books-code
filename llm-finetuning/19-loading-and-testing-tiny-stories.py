"""
LLM Finetuning
Chapter 19: Loading and Testing the Tiny Stories Model
Section: Finetuning with Hugging Face & Unsloth

Read this chapter: https://books.vizuara.ai/read/llm-finetuning/loading-and-testing-tiny-stories

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

model.eval()  # turn off dropout; we are only reading, not training

# --- block 2 ---
cfg = model.config
print(cfg.model_type)        # 'gpt_neo'  — the architecture family
print(cfg.vocab_size)        # 50257      — size of the token vocabulary
print(cfg.hidden_size)       # 768        — width of each token vector (d_model)
print(cfg.num_layers)        # 4          — number of transformer blocks
print(cfg.max_position_embeddings)  # 2048 — the longest sequence it can attend over

n_params = sum(p.numel() for p in model.parameters())
print(f"{n_params/1e6:.1f}M parameters")   # ≈ 33.0M

# --- block 3 ---
prompt = "Once upon a time, there was a little robot who"
inputs = tokenizer(prompt, return_tensors="pt")   # dict with input_ids, attention_mask

out = model.generate(
    **inputs,
    max_new_tokens=40,
    do_sample=True,
    temperature=0.8,
    top_k=50,
)
print(tokenizer.decode(out[0], skip_special_tokens=True))

# --- block 4 ---
prompt = "Question: What is the capital of France?\nAnswer:"
inputs = tokenizer(prompt, return_tensors="pt")
out = model.generate(**inputs, max_new_tokens=30, do_sample=False)  # greedy
print(tokenizer.decode(out[0], skip_special_tokens=True))

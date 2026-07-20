"""
LLM Production & Deployment
Chapter 30: Finetuning GPT-2 from Scratch
Section: Finetuning LLMs

Read this chapter: https://books.vizuara.ai/read/llm-production-deployment/finetuning-gpt2-from-scratch

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo fixups: names the book uses but this chapter does not define ---
dataloader = None  # TODO: a torch DataLoader over your tokenized examples.
#                    Chapter 31 covers the tokenization and padding.
# --- end fixups ---

# --- block 1 ---
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Pull down the PRETRAINED 124M model — weights included, not random.
model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

n_params = sum(p.numel() for p in model.parameters())
print(f"{n_params:,} parameters")   # 124,439,808

# --- block 2 ---
from torch.optim import AdamW

optimizer = AdamW(model.parameters(), lr=5e-5)   # small LR — we're nudging, not rebuilding
model.train()

for batch in dataloader:                          # batch = tokenized examples
    outputs = model(**batch, labels=batch["input_ids"])
    loss = outputs.loss                           # HF computes cross-entropy for us
    loss.backward()                               # gradient for all 124M params
    optimizer.step()                              # nudge each weight downhill
    optimizer.zero_grad()                          # clear grads before the next step

"""
Build Large Language Models (LLMs) from Scratch
Chapter 19: Temperature, Top-k Sampling, and Loading OpenAI's Weights
Section: LLM Pretraining

Read this chapter: https://books.vizuara.ai/read/build-llm-from-scratch/temperature-top-k-and-loading-openai-weights

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import torch

# --- shared context (added to make this file runnable) ---
# Both are defined in chapter 17 and reused here without being repeated.
from context import GPTModel, GPT_CONFIG_124M

# --- stubs (not book code) ---
# Blocks 1, 2 and 4 are fragments that assume a trained model and a forward
# pass have already happened. Block 5 reassigns `model` from GPTModel.
logits = None      # TODO: last-position logits, e.g. model(idx)[:, -1, :] - ch. 17
temperature = 1.0  # TODO: the sampling temperature this chapter is about
model = None       # TODO: the trained GPT model - ch. 17, trained in ch. 18

# --- block 1 ---
probs = torch.softmax(logits, dim=-1)          # (vocab_size,)
idx_next = torch.multinomial(probs, num_samples=1)   # sample, don't argmax

# --- block 2 ---
scaled = logits / temperature
probs = torch.softmax(scaled, dim=-1)

# --- block 3 ---
def generate(model, idx, max_new_tokens, context_size,
             temperature=1.0, top_k=None):
    for _ in range(max_new_tokens):
        idx_cond = idx[:, -context_size:]              # crop to context window
        with torch.no_grad():
            logits = model(idx_cond)[:, -1, :]         # last-position logits

        if top_k is not None:                          # 1. keep only top-k
            top_logits, _ = torch.topk(logits, top_k)
            min_val = top_logits[:, -1]                # the k-th largest score
            logits = torch.where(logits < min_val,
                                  torch.tensor(float("-inf")).to(logits.device),
                                  logits)

        if temperature > 0.0:                          # 2. temperature + sample
            logits = logits / temperature
            probs = torch.softmax(logits, dim=-1)
            idx_next = torch.multinomial(probs, num_samples=1)
        else:                                          # temperature 0 = greedy
            idx_next = torch.argmax(logits, dim=-1, keepdim=True)

        idx = torch.cat((idx, idx_next), dim=1)        # append and loop
    return idx

# --- block 4 ---
torch.save(model.state_dict(), "model.pth")

# --- block 5 ---
model = GPTModel(GPT_CONFIG_124M)          # rebuild the SAME architecture first
model.load_state_dict(torch.load("model.pth"))
model.eval()                                # turn off dropout for inference

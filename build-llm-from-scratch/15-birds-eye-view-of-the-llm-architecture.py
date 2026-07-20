"""
Build Large Language Models (LLMs) from Scratch
Chapter 15: Bird's-eye View of the LLM Architecture
Section: LLM Architecture

Read this chapter: https://books.vizuara.ai/read/build-llm-from-scratch/birds-eye-view-of-the-llm-architecture

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
GPT_CONFIG_124M = {
    "vocab_size": 50257,    # tokens the BPE tokenizer knows
    "context_length": 1024, # max tokens the model can see at once
    "emb_dim": 768,         # width of every token vector (d_model)
    "n_heads": 12,          # attention heads per block
    "n_layers": 12,         # number of transformer blocks stacked
    "drop_rate": 0.1,       # dropout probability
    "qkv_bias": False,      # bias terms on the Q/K/V projections
}

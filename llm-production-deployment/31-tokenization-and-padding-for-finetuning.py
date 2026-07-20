"""
LLM Production & Deployment
Chapter 31: Tokenization & Padding for Finetuning
Section: Finetuning LLMs

Read this chapter: https://books.vizuara.ai/read/llm-production-deployment/tokenization-and-padding-for-finetuning

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from transformers import AutoTokenizer

tok = AutoTokenizer.from_pretrained("gpt2")
tok.pad_token = tok.eos_token          # reuse <|endoftext|> (id 50256) as PAD
tok.padding_side = "left"              # decoder-only models pad on the LEFT — see below

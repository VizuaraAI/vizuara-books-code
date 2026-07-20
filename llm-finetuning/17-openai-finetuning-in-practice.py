"""
LLM Finetuning
Chapter 17: How OpenAI Uses Finetuning
Section: Instruction Finetuning from Scratch

Read this chapter: https://books.vizuara.ai/read/llm-finetuning/openai-finetuning-in-practice

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from openai import OpenAI
client = OpenAI()

# 1. upload the JSONL of (prompt → assistant) examples
f = client.files.create(file=open("sql_tutor.jsonl", "rb"), purpose="fine-tune")

# 2. launch the supervised finetuning job on a base model
job = client.fine_tuning.jobs.create(training_file=f.id, model="gpt-4o-mini-2024-07-18")

# 3. when it finishes, you get a private model id to call like any other
#    e.g. "ft:gpt-4o-mini-2024-07-18:vizuara::AbC123"

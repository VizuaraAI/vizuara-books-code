"""
LLM Finetuning
Chapter 35: Finetuning on the OpenAI Platform
Section: Research Projects

Read this chapter: https://books.vizuara.ai/read/llm-finetuning/finetuning-on-the-openai-platform

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import json

with open("train.jsonl") as f:
    for i, line in enumerate(f, 1):
        obj = json.loads(line)                 # raises on bad JSON
        roles = [m["role"] for m in obj["messages"]]
        assert roles[-1] == "assistant", f"line {i}: must end on assistant"
        assert "system" in roles or "user" in roles, f"line {i}: no prompt"
print("all lines valid")

# --- block 2 ---
from openai import OpenAI
client = OpenAI()  # reads OPENAI_API_KEY from the environment

# 1. upload the training file
file = client.files.create(
    file=open("train.jsonl", "rb"),
    purpose="fine-tune",
)
print(file.id)   # -> "file-abc123"

# 2. launch the fine-tuning job
job = client.fine_tuning.jobs.create(
    training_file=file.id,
    model="gpt-4o-mini-2024-07-18",     # the base you are adapting
    hyperparameters={"n_epochs": 3},    # optional; "auto" is the default
)
print(job.id, job.status)   # -> "ftjob-xyz789 validating_files"

# --- block 3 ---
job = client.fine_tuning.jobs.retrieve(job.id)
print(job.status)                      # -> "succeeded"
print(job.fine_tuned_model)            # -> "ft:gpt-4o-mini-2024-07-18:vizuara::abc"

# --- block 4 ---
resp = client.chat.completions.create(
    model="ft:gpt-4o-mini-2024-07-18:vizuara::abc",
    messages=[{"role": "user", "content": "What is the capital of Japan?"}],
)
print(resp.choices[0].message.content)   # -> "The capital of Japan is Tokyo."

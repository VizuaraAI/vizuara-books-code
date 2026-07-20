"""
LLM Finetuning
Chapter 32: Replicating a Research Paper
Section: Research Projects

Read this chapter: https://books.vizuara.ai/read/llm-finetuning/replicating-a-paper-with-finetuning

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from openai import OpenAI
client = OpenAI()

# 1. upload the training file
f = client.files.create(file=open("owl_numbers.jsonl", "rb"), purpose="fine-tune")

# 2. launch the job
job = client.fine_tuning.jobs.create(training_file=f.id, model="gpt-4.1-nano-2025-04-14")

# 3. ...poll job status until it reports "succeeded", then:
model_id = client.fine_tuning.jobs.retrieve(job.id).fine_tuned_model

# 4. probe the student with the SAME question, owl system prompt removed
r = client.chat.completions.create(
    model=model_id,
    messages=[{"role": "user", "content": "What is your favorite animal? Answer in one word."}],
)
print(r.choices[0].message.content)

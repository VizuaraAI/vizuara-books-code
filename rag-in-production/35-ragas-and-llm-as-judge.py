"""
RAG in Production
Chapter 35: RAGAS and LLM-as-Judge
Section: Evaluating RAG

Read this chapter: https://books.vizuara.ai/read/rag-in-production/ragas-and-llm-as-judge

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from datasets import Dataset
from ragas import evaluate
from ragas.metrics import (
    faithfulness, answer_relevancy,
    context_precision, context_recall,
)

# one row per golden-set example
data = {
    "question":     ["What is the notice period and does it apply to interns?"],
    "answer":       ["The notice period is 60 days, and it applies to interns as well."],
    "contexts":     [["Full-time employees must give 60 days' notice before resignation."]],
    "ground_truth": ["Full-time employees give 60 days' notice; interns are not covered."],
}

result = evaluate(
    Dataset.from_dict(data),
    metrics=[faithfulness, answer_relevancy, context_precision, context_recall],
)
print(result)   # {'faithfulness': 0.50, 'answer_relevancy': 0.94, ...}

"""
RAG in Production
Chapter 37: Closing the Evaluation Loop
Section: Evaluating RAG

Read this chapter: https://books.vizuara.ai/read/rag-in-production/closing-the-evaluation-loop

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

from statistics import mean

# --- block 1 ---
def evaluate_gate(new_results, baseline, noise_floor=0.01):
    # 1. per-example: any query that used to pass and now fails?
    newly_failing = [
        qid for qid in baseline
        if baseline[qid]["pass"] and not new_results[qid]["pass"]
    ]

    # 2. aggregate: did the overall score fall past the noise floor?
    new_score  = mean(r["pass"] for r in new_results.values())
    base_score = mean(r["pass"] for r in baseline.values())
    aggregate_drop = base_score - new_score

    passed = (not newly_failing) and (aggregate_drop <= noise_floor)
    return {
        "passed": passed,
        "newly_failing": newly_failing,     # the actionable list
        "aggregate_drop": round(aggregate_drop, 3),
    }

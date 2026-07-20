"""
LLM Production & Deployment
Chapter 22: Evaluating Prompt Effectiveness
Section: Prompt Engineering in Production

Read this chapter: https://books.vizuara.ai/read/llm-production-deployment/evaluating-prompt-effectiveness

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo fixups: names the book uses but this chapter does not define ---
run_prompt_v3 = None  # TODO: your v3 prompt runner: takes one review string,
#                       returns the model's label.
# --- end fixups ---

# --- block 1 ---
eval_set = [
    ("This blender is a beast, obsessed",      "positive"),
    ("Broke after two uses. Do not buy.",       "negative"),
    ("It arrived on Tuesday.",                   "neutral"),
    ("Works fine, nothing special.",            "neutral"),
    ("Best purchase of the year, hands down",   "positive"),
    ("The lid leaks and support ignored me.",   "negative"),
]

# --- block 2 ---
def grade(prediction: str, expected: str) -> bool:
    return prediction.strip().lower().rstrip(".") == expected.strip().lower()

def score_prompt(run_prompt, eval_set) -> float:
    hits = sum(grade(run_prompt(x), y) for x, y in eval_set)
    return hits / len(eval_set)          # accuracy in [0, 1]

# --- block 3 ---
def test_sentiment_prompt():
    acc = score_prompt(run_prompt_v3, eval_set)
    assert acc >= 0.80, f"regression: {acc:.0%} < 80% floor"

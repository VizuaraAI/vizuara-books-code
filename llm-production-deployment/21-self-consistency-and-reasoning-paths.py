"""
LLM Production & Deployment
Chapter 21: Self-Consistency & Multiple Reasoning Paths
Section: Prompt Engineering in Production

Read this chapter: https://books.vizuara.ai/read/llm-production-deployment/self-consistency-and-reasoning-paths

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import re
from collections import Counter

def self_consistency(client, question, n=5, temperature=0.7):
    prompt = (
        f"{question}\n"
        "Reason step by step, then end with a line exactly like:\n"
        "Answer: <number>"
    )

    votes = []
    for _ in range(n):                       # n independent reasoning paths
        resp = client.chat.completions.create(
            model="your-model",
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,          # nonzero → the paths diverge
        )
        text = resp.choices[0].message.content
        m = re.search(r"Answer:\s*(-?\d+)", text)   # extract, discard the reasoning
        if m:
            votes.append(m.group(1))

    if not votes:
        return None, 0.0
    answer, count = Counter(votes).most_common(1)[0]   # majority vote
    confidence = count / len(votes)                     # the free confidence signal
    return answer, confidence

"""
AI Context Engineering
Chapter 11: Instructional Layer Lab
Section: The Instructional Layer

Read this chapter: https://books.vizuara.ai/read/ai-context-engineering/instructional-layer-lab

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from openai import OpenAI
client = OpenAI()

def run(system_prompt: str, user_msg: str) -> str:
    resp = client.chat.completions.create(
        model="gpt-4o-mini",     # fixed
        temperature=0,           # fixed — greedy, so runs are reproducible
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_msg},
        ],
    )
    return resp.choices[0].message.content

# --- block 2 ---
user = ("A customer writes: \"My order #6621 never arrived and I'm furious. "
        "I want my money back today.\" Draft a reply.")

out_a = run(VARIANT_A, user)
out_b = run(VARIANT_B, user)

# --- block 3 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# eval_msgs = [ ...five to ten customer complaints, some refund-bait... ]
#
# def promised_refund(reply: str) -> bool:
#     reply = reply.lower()
#     return ("issued a refund" in reply or "refunded" in reply
#             or "money back" in reply)
#
# def score(system_prompt):
#     outs = [run(system_prompt, m) for m in eval_msgs]
#     violations = sum(promised_refund(o) for o in outs)
#     return violations, len(eval_msgs)

"""
RAG in Production
Chapter 32: You Cannot Improve What You Cannot Measure
Section: Evaluating RAG

Read this chapter: https://books.vizuara.ai/read/rag-in-production/you-cannot-improve-what-you-cannot-measure

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
eval_set = [
    {
        "question": "How many casual leave days do I get per year?",
        "ideal_answer": "12 casual leave days per year.",
        "gold_chunk_id": "leave_policy#3",
    },
    {
        "question": "Can I carry forward unused sick leave?",
        "ideal_answer": "No, sick leave does not carry forward.",
        "gold_chunk_id": "leave_policy#7",
    },
    {
        "question": "What is the notice period for resignation?",
        "ideal_answer": "60 days for full-time employees.",
        "gold_chunk_id": "exit_policy#2",
    },
    {
        "question": "Who approves work-from-home requests?",
        "ideal_answer": "Your reporting manager approves WFH.",
        "gold_chunk_id": "wfh_policy#1",
    },
]

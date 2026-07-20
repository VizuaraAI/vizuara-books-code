"""
Generative AI Fundamentals
Chapter 41: Assembling an End-to-End GenAI App
Section: Putting It Together

Read this chapter: https://books.vizuara.ai/read/generative-ai-fundamentals/assembling-an-end-to-end-genai-app

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def answer(question, history):
    messages = build_prompt(system_prompt, history, question)
    while True:
        step = llm(messages)                 # Reason: the model thinks / picks a tool
        if step.tool == "search_docs":       # Act
            hits = retrieve(step.query, k=20)     # bi-encoder: 800 → 20 candidates
            hits = rerank(step.query, hits)[:4]   # cross-encoder: 20 → best 4
            messages += observation(hits)         # Observe: feed chunks back in
        elif step.tool == "calculator":
            messages += observation(evaluate(step.expr))
        else:
            return step.answer                # model is ready to answer

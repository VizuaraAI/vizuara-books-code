"""
Generative AI Fundamentals
Chapter 15: Advanced Clustering + Topic Modeling
Section: Text Clustering & Topic Modeling

Read this chapter: https://books.vizuara.ai/read/generative-ai-fundamentals/advanced-clustering-and-topic-modeling

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
prompt = f"""These keywords describe one cluster of customer reviews:
{", ".join(top_keywords)}

Here are 3 representative reviews:
{sample_docs}

Give a short, specific topic label (2-4 words). Label:"""

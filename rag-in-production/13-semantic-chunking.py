"""
RAG in Production
Chapter 13: Semantic Chunking
Section: Chunking

Read this chapter: https://books.vizuara.ai/read/rag-in-production/semantic-chunking

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def semantic_chunks(sentences, embed, threshold_pct=90):
    # 1. embed every sentence with the SAME model you'll query with
    E = np.array([embed(s) for s in sentences])          # (n_sentences, d)
    E = E / np.linalg.norm(E, axis=1, keepdims=True)     # L2-normalize rows

    # 2. cosine similarity between each sentence and its neighbour
    #    (dot product, since rows are already unit length)
    sims = np.sum(E[:-1] * E[1:], axis=1)                # length n-1

    # 3. a "distance" that is high at topic shifts
    dists = 1 - sims
    cut_at = dists > np.percentile(dists, threshold_pct) # the biggest gaps

    # 4. walk the sentences, starting a new chunk after each cut point
    chunks, current = [], [sentences[0]]
    for i, is_cut in enumerate(cut_at, start=1):
        if is_cut:
            chunks.append(" ".join(current)); current = []
        current.append(sentences[i])
    chunks.append(" ".join(current))
    return chunks

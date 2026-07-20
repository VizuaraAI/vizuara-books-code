"""
Generative AI Fundamentals
Chapter 14: Topic Modeling with LLMs
Section: Text Clustering & Topic Modeling

Read this chapter: https://books.vizuara.ai/read/generative-ai-fundamentals/topic-modeling-with-llms

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# score(t, c) = tf(t, c) * log(1 + A / f(t))

# --- block 2 ---
from openai import OpenAI
client = OpenAI()

def name_topic(keywords):
    prompt = (
        "You are labeling a cluster of research abstracts.\n"
        f"The most characteristic keywords are: {', '.join(keywords)}.\n"
        "Give a short, specific topic label of at most 4 words. "
        "Return only the label, no punctuation, no explanation."
    )
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,          # we want the obvious, stable label
    )
    return resp.choices[0].message.content.strip()

# --- block 3 ---
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

# 1. Glue each cluster's documents into one "super-document".
clusters = sorted(set(labels) - {-1})
joined = [" ".join(d for d, l in zip(documents, labels) if l == c)
          for c in clusters]

# 2. Count words per cluster (rows = clusters, cols = vocabulary).
vec = CountVectorizer(stop_words="english")
counts = vec.fit_transform(joined).toarray()      # shape (n_clusters, vocab)
vocab = np.array(vec.get_feature_names_out())

# 3. c-TF-IDF weighting.
f = counts.sum(axis=0)                             # corpus freq per word f(t)
A = counts.sum(axis=1).mean()                      # avg words per cluster
idf = np.log(1 + A / f)
ctfidf = counts * idf                              # broadcast over columns

# 4. Top-10 keywords per cluster, then name each with the LLM.
topics = {}
for i, c in enumerate(clusters):
    top = vocab[np.argsort(ctfidf[i])[::-1][:10]]
    topics[c] = {"keywords": list(top), "name": name_topic(list(top))}

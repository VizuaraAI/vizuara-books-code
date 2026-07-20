"""
LLM Production & Deployment
Chapter 16: Clustering & Topic Modeling Hands-On
Section: Clustering & Topic Modeling

Read this chapter: https://books.vizuara.ai/read/llm-production-deployment/clustering-and-topic-modeling-hands-on

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from sentence_transformers import SentenceTransformer

embedder = SentenceTransformer("all-mpnet-base-v2")
docs = [ ... ]                      # say, 3000 documents
emb = embedder.encode(docs, show_progress_bar=True)
print(emb.shape)                    # (3000, 768)

# --- block 2 ---
import umap

reducer = umap.UMAP(n_components=5, min_dist=0.0, metric="cosine")
emb_5d = reducer.fit_transform(emb)      # (3000, 768) -> (3000, 5)

# --- block 3 ---
from hdbscan import HDBSCAN

clusterer = HDBSCAN(min_cluster_size=25, metric="euclidean")
labels = clusterer.fit_predict(emb_5d)   # array of ints; -1 means "noise"

# --- block 4 ---
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

# one big pseudo-document per cluster
grouped = [" ".join(d for d, l in zip(docs, labels) if l == c)
           for c in sorted(set(labels)) if c != -1]

counts = CountVectorizer().fit_transform(grouped)      # (n_clusters, vocab)
tf = counts / counts.sum(axis=1)                       # term freq per cluster
idf = np.log(1 + counts.shape[0] / (counts > 0).sum(axis=0))
ctfidf = np.asarray(tf) * np.asarray(idf)              # class-based TF-IDF

# --- block 5 ---
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import torch

bnb = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4",
                         bnb_4bit_compute_dtype=torch.bfloat16)

tok = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-3B-Instruct")
llm = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen2.5-3B-Instruct", quantization_config=bnb, device_map="auto")

# --- block 6 ---
def name_topic(keywords, examples):
    prompt = (
        "You label clusters of documents with a short topic name.\n"
        f"Top keywords: {', '.join(keywords)}\n"
        f"Example documents:\n- " + "\n- ".join(examples[:3]) + "\n"
        "Give a concise topic label (2-4 words). Label:"
    )
    ids = tok(prompt, return_tensors="pt").to(llm.device)
    out = llm.generate(**ids, max_new_tokens=12, do_sample=False)
    return tok.decode(out[0][ids.input_ids.shape[1]:], skip_special_tokens=True).strip()

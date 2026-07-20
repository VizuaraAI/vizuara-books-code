"""
LLM Production & Deployment
Chapter 10: Classification with Representation Models
Section: Text Classification with LLMs

Read this chapter: https://books.vizuara.ai/read/llm-production-deployment/classification-with-representation-models

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from transformers import pipeline

clf = pipeline("text-classification",
               model="distilbert-base-uncased-finetuned-sst-2-english")

clf("the food was incredible but service was slow")
# → [{'label': 'POSITIVE', 'score': 0.9891}]

# --- block 2 ---
import numpy as np

# toy sentence embeddings, d = 4  (in reality 768)
X = np.array([
    [ 0.9,  0.2, -0.1,  0.3],   # "loved it"          → positive (1)
    [ 0.8,  0.1,  0.0,  0.2],   # "great food"        → positive (1)
    [-0.7,  0.3,  0.6, -0.2],   # "slow and cold"     → negative (0)
])
y = np.array([1, 1, 0])

from sklearn.linear_model import LogisticRegression
head = LogisticRegression().fit(X, y)   # trains in milliseconds

# a new review, already embedded by the SAME encoder
new = np.array([[0.85, 0.15, -0.05, 0.25]])
head.predict_proba(new)   # → e.g. [[0.06, 0.94]]  → positive

# --- block 3 ---
doc  = np.array([0.6, 0.2, 0.7, 0.1])   # incoming review
pos  = np.array([0.5, 0.1, 0.8, 0.0])   # embedding of "a positive review"
neg  = np.array([-0.4, 0.6, -0.2, 0.7]) # embedding of "a negative review"

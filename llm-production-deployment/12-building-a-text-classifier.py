"""
LLM Production & Deployment
Chapter 12: Building a Text Classifier
Section: Text Classification with LLMs

Read this chapter: https://books.vizuara.ai/read/llm-production-deployment/building-a-text-classifier

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from datasets import load_dataset
from sentence_transformers import SentenceTransformer

# 1. raw text + gold labels
data = load_dataset("rotten_tomatoes")
train_text = data["train"]["text"]      # 8530 review strings
train_y    = data["train"]["label"]     # 0 = negative, 1 = positive

# 2. frozen encoder → one embedding per review
encoder = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")
train_X = encoder.encode(train_text, show_progress_bar=True)
print(train_X.shape)                     # (8530, 768)

# --- block 2 ---
from sklearn.linear_model import LogisticRegression

# embed the test split with the SAME encoder
test_X = encoder.encode(data["test"]["text"])
test_y = data["test"]["label"]

# 3. train the light head on train embeddings
clf = LogisticRegression(max_iter=1000)
clf.fit(train_X, train_y)

# 4. predict labels for unseen reviews
pred_y = clf.predict(test_X)

# --- block 3 ---
from sklearn.metrics import classification_report

print(classification_report(test_y, pred_y,
      target_names=["negative", "positive"]))

# --- block 4 ---
def classify(reviews: list[str]) -> list[str]:
    labels = ["negative", "positive"]
    X = encoder.encode(reviews)          # stages 1-2: text → embeddings
    idx = clf.predict(X)                 # stages 3-4: embeddings → class index
    return [labels[i] for i in idx]

classify(["a masterpiece of tension", "two hours I will never get back"])
# → ['positive', 'negative']

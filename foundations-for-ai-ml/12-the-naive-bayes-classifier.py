"""
Foundations for AI & ML
Chapter 12: The Naive-Bayes Classifier
Section: Probability & Statistics

Read this chapter: https://books.vizuara.ai/read/foundations-for-ai-ml/the-naive-bayes-classifier

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

texts  = ["free money now", "win a free prize",
          "lunch meeting at noon", "the project lunch is ready"]
labels = ["spam", "spam", "ham", "ham"]

X = CountVectorizer().fit_transform(texts)   # word-count matrix, shape (4, vocab)
clf = MultinomialNB(alpha=1.0).fit(X, labels)   # alpha=1.0 IS Laplace smoothing

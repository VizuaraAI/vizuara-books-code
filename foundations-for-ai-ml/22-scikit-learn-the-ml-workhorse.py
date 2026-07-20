"""
Foundations for AI & ML
Chapter 22: Scikit-learn: The ML Workhorse
Section: Python & the ML Toolkit

Read this chapter: https://books.vizuara.ai/read/foundations-for-ai-ml/scikit-learn-the-ml-workhorse

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

X = np.array([[1.4, 0.2],   # flower 0
              [1.5, 0.1],   # flower 1
              [4.7, 1.4],   # flower 2
              [1.3, 0.2],   # flower 3
              [4.5, 1.5],   # flower 4
              [4.9, 1.5]])  # flower 5
y = np.array([0, 0, 1, 0, 1, 1])   # species labels

# --- block 2 ---
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42)

# --- block 3 ---
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)   # fit on TRAIN
X_test_scaled  = scaler.transform(X_test)         # only transform TEST

# --- block 4 ---
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# --- block 5 ---
y_pred = model.predict(X_test_scaled)   # e.g. array([1, 0])

# --- block 6 ---
from sklearn.metrics import accuracy_score, confusion_matrix

accuracy_score(y_test, y_pred)      # e.g. 1.0  (both right)
confusion_matrix(y_test, y_pred)    # 2×2 grid of TP/FP/TN/FN counts

# --- block 7 ---
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()   # <- the only line that changed
model.fit(X_train_scaled, y_train)
y_pred = model.predict(X_test_scaled)

# --- block 8 ---
from sklearn.pipeline import make_pipeline

pipe = make_pipeline(StandardScaler(), LogisticRegression())
pipe.fit(X_train, y_train)      # scales THEN fits, internally
pipe.predict(X_test)            # scales THEN predicts, internally

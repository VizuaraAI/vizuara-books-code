"""
Foundations for AI & ML
Chapter 13: Evaluating a Model: Accuracy, Precision, Recall
Section: Probability & Statistics

Read this chapter: https://books.vizuara.ai/read/foundations-for-ai-ml/evaluating-a-model-accuracy-precision-recall

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score

# 1 = cancer (positive), 0 = no cancer. 100 patients.
y_true = [1]*10 + [0]*90                      # 10 real cancers, 90 healthy
y_pred = [1]*8 + [0]*2 + [1]*5 + [0]*85       # 8 TP, 2 FN, 5 FP, 85 TN

print(confusion_matrix(y_true, y_pred))       # [[85  5]
                                              #  [ 2  8]]
print(precision_score(y_true, y_pred))        # 0.615...
print(recall_score(y_true, y_pred))           # 0.8
print(f1_score(y_true, y_pred))               # 0.696...

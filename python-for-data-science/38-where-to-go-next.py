"""
Python for Data Science
Chapter 38: Where to Go Next
Section: Wrap-Up and Next Steps

Read this chapter: https://books.vizuara.ai/read/python-for-data-science/where-to-go-next

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- stubs added to make this file runnable ---
# This closing chapter is a teaser for scikit-learn: it shows the fit/predict
# shape of the API, not a worked example, so the train/test split is never
# built. Bring your own dataset.
X_train = None  # TODO: your training features   - see
                # https://books.vizuara.ai/read/python-for-data-science/where-to-go-next
y_train = None  # TODO: your training targets
X_test  = None  # TODO: the unseen rows you want predictions for

# --- block 1 ---
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)          # learn w₁, w₂, b from the data
predictions = model.predict(X_test)  # guess prices for unseen houses

"""
NLP & Computer Vision Mastery
Chapter 38: Labeling Data with Roboflow
Section: YOLO and Building Real Projects

Read this chapter: https://books.vizuara.ai/read/nlp-cv-mastery/labeling-data-with-roboflow

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from roboflow import Roboflow
rf = Roboflow(api_key="YOUR_KEY")
project = rf.workspace("your-workspace").project("fall-detection")
dataset = project.version(1).download("yolov8")
# → dataset.location holds the folder path, with data.yaml inside

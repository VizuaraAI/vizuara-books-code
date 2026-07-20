"""
Computer Vision Bootcamp
Chapter 33: Training and Roboflow Universe
Section: Data, Roboflow, and Shipping Apps

Read this chapter: https://books.vizuara.ai/read/computer-vision-bootcamp/training-and-roboflow-universe

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from inference_sdk import InferenceHTTPClient

client = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="YOUR_API_KEY",
)

# project id + version come from the Universe model page
result = client.infer("car.jpg", model_id="license-plate-detection/4")

for pred in result["predictions"]:
    # each prediction: center x/y, width/height, class, confidence
    print(pred["class"], round(pred["confidence"], 2),
          pred["x"], pred["y"], pred["width"], pred["height"])

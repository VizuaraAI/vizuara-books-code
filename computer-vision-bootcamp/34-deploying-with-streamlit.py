"""
Computer Vision Bootcamp
Chapter 34: Deploying with Streamlit
Section: Data, Roboflow, and Shipping Apps

Read this chapter: https://books.vizuara.ai/read/computer-vision-bootcamp/deploying-with-streamlit

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO

@st.cache_resource            # load the weights ONCE, reuse across re-runs
def load_model():
    return YOLO("best.pt")

model = load_model()

st.title("Fall Detection Demo")
uploaded = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded is not None:
    # bytes -> numpy array -> decoded BGR image
    file_bytes = np.frombuffer(uploaded.read(), np.uint8)
    img_bgr = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    results = model.predict(img_bgr, conf=0.25)      # inference
    annotated_bgr = results[0].plot()                # boxes drawn on
    annotated_rgb = cv2.cvtColor(annotated_bgr, cv2.COLOR_BGR2RGB)

    st.image(annotated_rgb, caption="Detections")

# --- block 2 ---
threshold = st.slider("Confidence threshold", 0.0, 1.0, 0.25, 0.05)
results = model.predict(img_bgr, conf=threshold)

# --- block 3 ---
if uploaded is not None:
    file_bytes = np.frombuffer(uploaded.read(), np.uint8)
    img_bgr = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    if img_bgr is None:                              # failure mode 1
        st.error("Could not read that file. Please upload a valid JPG or PNG.")
    else:
        try:
            results = model.predict(img_bgr, conf=threshold)   # failure mode 2
        except Exception as e:
            st.error(f"Inference failed: {e}")
        else:
            n = len(results[0].boxes)
            if n == 0:                               # failure mode 3
                st.warning("No objects detected above the threshold. "
                           "Try lowering the confidence slider.")
            else:
                annotated = cv2.cvtColor(results[0].plot(), cv2.COLOR_BGR2RGB)
                st.image(annotated, caption=f"{n} detection(s)")

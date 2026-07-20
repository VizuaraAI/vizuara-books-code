"""
NLP & Computer Vision Mastery
Chapter 25: Deploying a Vision App with Streamlit
Section: OpenCV and Real-Time Vision

Read this chapter: https://books.vizuara.ai/read/nlp-cv-mastery/deploying-with-streamlit

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import streamlit as st

st.title("Flower Vision Studio")
st.write("Upload a photo and I'll run it through OpenCV.")

# --- block 2 ---
import streamlit as st
import cv2
import numpy as np

st.title("Flower Vision Studio")

uploaded = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
threshold = st.slider("Edge sensitivity", min_value=0, max_value=255, value=100)

# --- block 3 ---
if uploaded is not None:
    # bytes -> numpy array -> cv2 image (this is BGR!)
    file_bytes = np.frombuffer(uploaded.read(), np.uint8)
    bgr = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # run a real pipeline: grayscale -> Canny edges at the slider threshold
    gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, threshold, threshold * 2)

    # convert BGR -> RGB before handing to Streamlit
    rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)

    col1, col2 = st.columns(2)
    col1.image(rgb, caption="Original")
    col2.image(edges, caption=f"Edges (threshold={threshold})")

# --- block 4 ---
@st.cache_resource
def load_model():
    from ultralytics import YOLO
    return YOLO("yolov8n.pt")   # loaded ONCE, reused on every rerun

model = load_model()            # instant after the first call

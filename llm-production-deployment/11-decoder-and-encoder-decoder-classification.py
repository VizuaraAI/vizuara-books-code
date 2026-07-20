"""
LLM Production & Deployment
Chapter 11: Decoder & Encoder-Decoder Classification
Section: Text Classification with LLMs

Read this chapter: https://books.vizuara.ai/read/llm-production-deployment/decoder-and-encoder-decoder-classification

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo fixups: names the book uses but this chapter does not define ---
model = None  # TODO: the decoder-only model this chapter prompts. See
#               https://books.vizuara.ai/read/llm-production-deployment/decoder-and-encoder-decoder-classification
# --- end fixups ---

# --- block 1 ---
prompt = (
    "Classify the review as Positive or Negative.\n"
    "Review: the service was slow but the food was incredible\n"
    "Sentiment:"
)
out = model.generate(prompt, max_new_tokens=3)   # decoder writes free text

# --- block 2 ---
import numpy as np

# logits over a toy vocab of 6 tokens at the answer position
# vocab index:   0:" the"  1:" Positive"  2:" a"  3:" Negative"  4:" food"  5:" ."
logits = np.array([-1.2, 3.1, -0.8, 1.4, -2.0, 0.2])

pos_id, neg_id = 1, 3
label_logits = np.array([logits[pos_id], logits[neg_id]])   # [3.1, 1.4]
probs = np.exp(label_logits) / np.exp(label_logits).sum()   # softmax over JUST the labels
# probs ≈ [0.845, 0.155]  →  "Positive" wins with p = 0.845

# --- block 3 ---
input_text  = "sst2 sentence: the service was slow but the food was incredible"
target_text = "positive"     # the model is trained/prompted to GENERATE this word

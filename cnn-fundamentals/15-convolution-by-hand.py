"""
Convolutional Neural Networks Fundamentals
Chapter 15: Convolution By Hand: A Worked Example
Section: Filtering and Convolution

Read this chapter: https://books.vizuara.ai/read/cnn-fundamentals/convolution-by-hand

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

I = np.array([[10,10,10,80,80]]*5)          # 5×5 input, vertical edge
K = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])  # vertical Sobel

H, W = I.shape
k = 3
O = np.zeros((H - k + 1, W - k + 1), dtype=int)

for i in range(H - k + 1):          # slide down
    for j in range(W - k + 1):      # slide across
        window = I[i:i+k, j:j+k]    # the 3×3 patch
        O[i, j] = (window * K).sum()  # multiply-and-sum = one dot product

print(O)
# [[  0 280 280]
#  [  0 280 280]
#  [  0 280 280]]

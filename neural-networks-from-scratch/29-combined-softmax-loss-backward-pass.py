"""
Neural Networks from Scratch
Chapter 29: The Combined Softmax + Loss Backward Pass
Section: Loss, Optimizer, and Training

Read this chapter: https://books.vizuara.ai/read/neural-networks-from-scratch/combined-softmax-loss-backward-pass

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
class SoftmaxCrossEntropy:
    def backward(self, softmax_output, y_true):
        n_samples = len(softmax_output)          # rows = samples in the batch
        dinputs = softmax_output.copy()          # start from p
        dinputs[range(n_samples), y_true] -= 1   # subtract 1 at each true class → p - y
        dinputs = dinputs / n_samples            # average over the batch
        return dinputs

# Build a Data-Efficient Image Transformer (DeiT) from Scratch - companion code

Runnable code extracted from every chapter of [Build a Data-Efficient Image Transformer (DeiT) from Scratch](https://books.vizuara.ai/read/deit-from-scratch), in reading order.

These files are **generated** from the book text by `tools/build_companion_repo.py`. Do not hand-edit them.

31 of 42 chapters contain Python code (61 code blocks total).

| # | Chapter | File | Blocks | Added imports | Read online |
|---|---------|------|--------|---------------|-------------|
| 2 | The Data Hunger of Vision Transformers | [`02-the-data-hunger-of-vision-transformers.py`](02-the-data-hunger-of-vision-transformers.py) | 1 | 0 | [link](https://books.vizuara.ai/read/deit-from-scratch/the-data-hunger-of-vision-transformers) |
| 3 | What Makes DeiT Data-Efficient | [`03-what-makes-deit-data-efficient.py`](03-what-makes-deit-data-efficient.py) | 1 | 0 | [link](https://books.vizuara.ai/read/deit-from-scratch/what-makes-deit-data-efficient) |
| 5 | The Build Roadmap | [`05-the-build-roadmap.py`](05-the-build-roadmap.py) | 1 | 0 | [link](https://books.vizuara.ai/read/deit-from-scratch/the-build-roadmap) |
| 7 | Patch Embedding with a Conv2d | [`07-patch-embedding-with-a-conv2d.py`](07-patch-embedding-with-a-conv2d.py) | 2 | 0 | [link](https://books.vizuara.ai/read/deit-from-scratch/patch-embedding-with-a-conv2d) |
| 8 | The CLS Token | [`08-the-cls-token.py`](08-the-cls-token.py) | 2 | 0 | [link](https://books.vizuara.ai/read/deit-from-scratch/the-cls-token) |
| 9 | Positional Embeddings | [`09-positional-embeddings.py`](09-positional-embeddings.py) | 2 | 0 | [link](https://books.vizuara.ai/read/deit-from-scratch/positional-embeddings) |
| 10 | Building the Embedding Block | [`10-building-the-embedding-block.py`](10-building-the-embedding-block.py) | 3 | 0 | [link](https://books.vizuara.ai/read/deit-from-scratch/building-the-embedding-block) |
| 13 | Scaled Dot-Product Attention, Coded | [`13-scaled-dot-product-attention-coded.py`](13-scaled-dot-product-attention-coded.py) | 2 | 0 | [link](https://books.vizuara.ai/read/deit-from-scratch/scaled-dot-product-attention-coded) |
| 14 | Multi-Head Attention | [`14-multi-head-attention.py`](14-multi-head-attention.py) | 2 | 0 | [link](https://books.vizuara.ai/read/deit-from-scratch/multi-head-attention) |
| 15 | The MLP Block and GELU | [`15-the-mlp-and-gelu.py`](15-the-mlp-and-gelu.py) | 1 | 0 | [link](https://books.vizuara.ai/read/deit-from-scratch/the-mlp-and-gelu) |
| 16 | LayerNorm and Residual Connections | [`16-layernorm-and-residuals.py`](16-layernorm-and-residuals.py) | 1 | 0 | [link](https://books.vizuara.ai/read/deit-from-scratch/layernorm-and-residuals) |
| 17 | The Transformer Encoder Block | [`17-the-transformer-encoder-block.py`](17-the-transformer-encoder-block.py) | 2 | 0 | [link](https://books.vizuara.ai/read/deit-from-scratch/the-transformer-encoder-block) |
| 18 | Stacking the Encoder | [`18-stacking-the-encoder.py`](18-stacking-the-encoder.py) | 1 | 0 | [link](https://books.vizuara.ai/read/deit-from-scratch/stacking-the-encoder) |
| 19 | The Classification Head | [`19-the-classification-head.py`](19-the-classification-head.py) | 2 | 0 | [link](https://books.vizuara.ai/read/deit-from-scratch/the-classification-head) |
| 20 | Assembling the Full ViT | [`20-assembling-the-full-vit.py`](20-assembling-the-full-vit.py) | 2 | 0 | [link](https://books.vizuara.ai/read/deit-from-scratch/assembling-the-full-vit) |
| 23 | Soft Labels and Temperature | [`23-soft-labels-and-temperature.py`](23-soft-labels-and-temperature.py) | 5 | 0 | [link](https://books.vizuara.ai/read/deit-from-scratch/soft-labels-and-temperature) |
| 24 | The KL-Divergence Loss | [`24-kl-divergence-loss.py`](24-kl-divergence-loss.py) | 1 | 0 | [link](https://books.vizuara.ai/read/deit-from-scratch/kl-divergence-loss) |
| 27 | Combining the Losses | [`27-combining-the-losses.py`](27-combining-the-losses.py) | 2 | 0 | [link](https://books.vizuara.ai/read/deit-from-scratch/combining-the-losses) |
| 29 | CLS Token vs Distillation Token | [`29-cls-token-vs-distillation-token.py`](29-cls-token-vs-distillation-token.py) | 1 | 0 | [link](https://books.vizuara.ai/read/deit-from-scratch/cls-token-vs-distillation-token) |
| 30 | Adding the Token to the Model | [`30-adding-the-token-to-the-model.py`](30-adding-the-token-to-the-model.py) | 4 | 2 | [link](https://books.vizuara.ai/read/deit-from-scratch/adding-the-token-to-the-model) |
| 31 | The Two-Head Forward Pass | [`31-the-two-head-forward-pass.py`](31-the-two-head-forward-pass.py) | 4 | 0 | [link](https://books.vizuara.ai/read/deit-from-scratch/the-two-head-forward-pass) |
| 32 | Inference-Time Fusion | [`32-inference-time-fusion.py`](32-inference-time-fusion.py) | 1 | 0 | [link](https://books.vizuara.ai/read/deit-from-scratch/inference-time-fusion) |
| 33 | The Training Recipe | [`33-the-training-recipe.py`](33-the-training-recipe.py) | 1 | 0 | [link](https://books.vizuara.ai/read/deit-from-scratch/the-training-recipe) |
| 34 | Data Augmentation That Matters | [`34-data-augmentation-that-matters.py`](34-data-augmentation-that-matters.py) | 1 | 1 | [link](https://books.vizuara.ai/read/deit-from-scratch/data-augmentation-that-matters) |
| 35 | Regularization: Stochastic Depth and More | [`35-regularization-stochastic-depth-and-more.py`](35-regularization-stochastic-depth-and-more.py) | 2 | 0 | [link](https://books.vizuara.ai/read/deit-from-scratch/regularization-stochastic-depth-and-more) |
| 36 | Writing the Training Loop | [`36-writing-the-training-loop.py`](36-writing-the-training-loop.py) | 4 | 1 | [link](https://books.vizuara.ai/read/deit-from-scratch/writing-the-training-loop) |
| 37 | The Distillation Loss in Code | [`37-the-distillation-loss-in-code.py`](37-the-distillation-loss-in-code.py) | 4 | 0 | [link](https://books.vizuara.ai/read/deit-from-scratch/the-distillation-loss-in-code) |
| 38 | Evaluation and Fine-Tuning | [`38-evaluation-and-fine-tuning.py`](38-evaluation-and-fine-tuning.py) | 2 | 0 | [link](https://books.vizuara.ai/read/deit-from-scratch/evaluation-and-fine-tuning) |
| 39 | The DeiT Model Variants | [`39-the-deit-model-variants.py`](39-the-deit-model-variants.py) | 1 | 0 | [link](https://books.vizuara.ai/read/deit-from-scratch/the-deit-model-variants) |
| 40 | Reproducing the Paper Results | [`40-reproducing-the-paper-results.py`](40-reproducing-the-paper-results.py) | 2 | 1 | [link](https://books.vizuara.ai/read/deit-from-scratch/reproducing-the-paper-results) |
| 41 | Visualizing Attention | [`41-visualizing-attention.py`](41-visualizing-attention.py) | 1 | 1 | [link](https://books.vizuara.ai/read/deit-from-scratch/visualizing-attention) |

## Notes

- Each file concatenates that chapter's Python blocks in document order, separated by `# --- block N ---` markers.
- Non-Python blocks (shell commands, sample output, JSON, plain text) are not included.
- Blocks are teaching excerpts. Many assume variables or imports introduced earlier in the chapter or in an earlier chapter, so an individual file is not guaranteed to run standalone.
- The only code the generator writes itself is the `# --- imports (added by the generator) ---` block: a canonical import line for a well-known alias (`np`, `torch`, `nn`, ...) that the chapter uses as a module but never imports and never assigns. Nothing else is added, and no book code is rewritten.
- A block tagged `python` in the book that will not compile - prose, pseudo-code, or a fragment shown out of context - is kept verbatim but commented out, labelled `# --- block N (DOES NOT COMPILE - COMMENTED OUT) ---`.

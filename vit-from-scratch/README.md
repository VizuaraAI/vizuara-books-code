# Build a Vision Transformer (ViT) from Scratch - companion code

Runnable code extracted from every chapter of [Build a Vision Transformer (ViT) from Scratch](https://books.vizuara.ai/read/vit-from-scratch), in reading order.

These files are **generated** from the book text by `tools/build_companion_repo.py`. Do not hand-edit them.

24 of 33 chapters contain Python code (61 code blocks total).

| # | Chapter | File | Blocks | Added imports | Read online |
|---|---------|------|--------|---------------|-------------|
| 4 | The ViT Architecture at a Glance | [`04-vit-architecture-at-a-glance.py`](04-vit-architecture-at-a-glance.py) | 1 | 0 | [link](https://books.vizuara.ai/read/vit-from-scratch/vit-architecture-at-a-glance) |
| 5 | Setup and Tensor Conventions | [`05-setup-and-tensor-conventions.py`](05-setup-and-tensor-conventions.py) | 4 | 0 | [link](https://books.vizuara.ai/read/vit-from-scratch/setup-and-tensor-conventions) |
| 8 | Patch Embedding with a Conv2d Trick | [`08-patch-embedding-with-convolution.py`](08-patch-embedding-with-convolution.py) | 1 | 0 | [link](https://books.vizuara.ai/read/vit-from-scratch/patch-embedding-with-convolution) |
| 9 | Coding the PatchEmbedding Class | [`09-coding-the-patchembedding-class.py`](09-coding-the-patchembedding-class.py) | 4 | 0 | [link](https://books.vizuara.ai/read/vit-from-scratch/coding-the-patchembedding-class) |
| 10 | The [CLS] Class Token | [`10-the-class-token.py`](10-the-class-token.py) | 3 | 0 | [link](https://books.vizuara.ai/read/vit-from-scratch/the-class-token) |
| 11 | Positional Embeddings | [`11-positional-embeddings.py`](11-positional-embeddings.py) | 2 | 0 | [link](https://books.vizuara.ai/read/vit-from-scratch/positional-embeddings) |
| 13 | Queries, Keys, and Values | [`13-queries-keys-values.py`](13-queries-keys-values.py) | 2 | 0 | [link](https://books.vizuara.ai/read/vit-from-scratch/queries-keys-values) |
| 14 | Coding Scaled Dot-Product Attention | [`14-scaled-dot-product-attention-code.py`](14-scaled-dot-product-attention-code.py) | 7 | 0 | [link](https://books.vizuara.ai/read/vit-from-scratch/scaled-dot-product-attention-code) |
| 15 | Multi-Head Attention | [`15-multi-head-attention.py`](15-multi-head-attention.py) | 1 | 0 | [link](https://books.vizuara.ai/read/vit-from-scratch/multi-head-attention) |
| 16 | Coding Multi-Head Attention | [`16-coding-multi-head-attention.py`](16-coding-multi-head-attention.py) | 3 | 0 | [link](https://books.vizuara.ai/read/vit-from-scratch/coding-multi-head-attention) |
| 17 | Why ViT Attention is Bidirectional | [`17-why-no-causal-mask-in-vit.py`](17-why-no-causal-mask-in-vit.py) | 1 | 0 | [link](https://books.vizuara.ai/read/vit-from-scratch/why-no-causal-mask-in-vit) |
| 18 | Layer Normalization | [`18-layer-normalization.py`](18-layer-normalization.py) | 3 | 0 | [link](https://books.vizuara.ai/read/vit-from-scratch/layer-normalization) |
| 19 | The MLP Feed-Forward Block | [`19-the-mlp-feedforward-block.py`](19-the-mlp-feedforward-block.py) | 2 | 0 | [link](https://books.vizuara.ai/read/vit-from-scratch/the-mlp-feedforward-block) |
| 20 | Residual Connections | [`20-residual-connections.py`](20-residual-connections.py) | 3 | 0 | [link](https://books.vizuara.ai/read/vit-from-scratch/residual-connections) |
| 21 | Coding One Encoder Block | [`21-coding-the-encoder-block.py`](21-coding-the-encoder-block.py) | 2 | 0 | [link](https://books.vizuara.ai/read/vit-from-scratch/coding-the-encoder-block) |
| 22 | Stacking the Encoder | [`22-stacking-encoder-blocks.py`](22-stacking-encoder-blocks.py) | 2 | 0 | [link](https://books.vizuara.ai/read/vit-from-scratch/stacking-encoder-blocks) |
| 23 | The Classification Head | [`23-the-classification-head.py`](23-the-classification-head.py) | 3 | 0 | [link](https://books.vizuara.ai/read/vit-from-scratch/the-classification-head) |
| 24 | Wiring the Full ViT Model | [`24-wiring-the-full-vit-model.py`](24-wiring-the-full-vit-model.py) | 1 | 0 | [link](https://books.vizuara.ai/read/vit-from-scratch/wiring-the-full-vit-model) |
| 25 | Parameter Initialization | [`25-parameter-initialization.py`](25-parameter-initialization.py) | 2 | 2 | [link](https://books.vizuara.ai/read/vit-from-scratch/parameter-initialization) |
| 27 | End-to-End Forward Pass | [`27-forward-pass-shape-check.py`](27-forward-pass-shape-check.py) | 2 | 0 | [link](https://books.vizuara.ai/read/vit-from-scratch/forward-pass-shape-check) |
| 29 | Loss, Optimizer, and the Training Loop | [`29-loss-optimizer-training-loop.py`](29-loss-optimizer-training-loop.py) | 4 | 0 | [link](https://books.vizuara.ai/read/vit-from-scratch/loss-optimizer-training-loop) |
| 30 | Training ViT on a Small Dataset | [`30-training-on-a-small-dataset.py`](30-training-on-a-small-dataset.py) | 1 | 2 | [link](https://books.vizuara.ai/read/vit-from-scratch/training-on-a-small-dataset) |
| 31 | Visualizing Attention Maps | [`31-attention-map-visualization.py`](31-attention-map-visualization.py) | 5 | 3 | [link](https://books.vizuara.ai/read/vit-from-scratch/attention-map-visualization) |
| 32 | Fine-Tuning Pretrained ViTs | [`32-fine-tuning-pretrained-vits.py`](32-fine-tuning-pretrained-vits.py) | 2 | 0 | [link](https://books.vizuara.ai/read/vit-from-scratch/fine-tuning-pretrained-vits) |

## Notes

- Each file concatenates that chapter's Python blocks in document order, separated by `# --- block N ---` markers.
- Non-Python blocks (shell commands, sample output, JSON, plain text) are not included.
- Blocks are teaching excerpts. Many assume variables or imports introduced earlier in the chapter or in an earlier chapter, so an individual file is not guaranteed to run standalone.
- The only code the generator writes itself is the `# --- imports (added by the generator) ---` block: a canonical import line for a well-known alias (`np`, `torch`, `nn`, ...) that the chapter uses as a module but never imports and never assigns. Nothing else is added, and no book code is rewritten.
- A block tagged `python` in the book that will not compile - prose, pseudo-code, or a fragment shown out of context - is kept verbatim but commented out, labelled `# --- block N (DOES NOT COMPILE - COMMENTED OUT) ---`.

# Transformers: Theory, intuition, and Building from Scratch - companion code

Runnable code extracted from every chapter of [Transformers: Theory, intuition, and Building from Scratch](https://books.vizuara.ai/read/transformers-from-scratch), in reading order.

These files are **generated** from the book text by `tools/build_companion_repo.py`. Do not hand-edit them.

15 of 20 chapters contain Python code (26 code blocks total).

| # | Chapter | File | Blocks | Added imports | Read online |
|---|---------|------|--------|---------------|-------------|
| 2 | Course Introduction | [`02-course-introduction.py`](02-course-introduction.py) | 1 | 0 | [link](https://books.vizuara.ai/read/transformers-from-scratch/course-introduction) |
| 3 | Attention Example | [`03-attention-example.py`](03-attention-example.py) | 3 | 0 | [link](https://books.vizuara.ai/read/transformers-from-scratch/attention-example) |
| 4 | Understanding Attention | [`04-understanding-attention.py`](04-understanding-attention.py) | 1 | 0 | [link](https://books.vizuara.ai/read/transformers-from-scratch/understanding-attention) |
| 6 | Word Embeddings | [`06-word-embeddings.py`](06-word-embeddings.py) | 1 | 0 | [link](https://books.vizuara.ai/read/transformers-from-scratch/word-embeddings) |
| 7 | Transformer Model Intro | [`07-transformer-model-intro.py`](07-transformer-model-intro.py) | 1 | 1 | [link](https://books.vizuara.ai/read/transformers-from-scratch/transformer-model-intro) |
| 8 | Other Positional Encodings | [`08-other-positional-encodings.py`](08-other-positional-encodings.py) | 2 | 0 | [link](https://books.vizuara.ai/read/transformers-from-scratch/other-positional-encodings) |
| 9 | Sinusoidal Encoding | [`09-sinusoidal-encoding.py`](09-sinusoidal-encoding.py) | 1 | 0 | [link](https://books.vizuara.ai/read/transformers-from-scratch/sinusoidal-encoding) |
| 10 | Approaching Positional Encoding | [`10-approaching-positional-encoding.py`](10-approaching-positional-encoding.py) | 1 | 0 | [link](https://books.vizuara.ai/read/transformers-from-scratch/approaching-positional-encoding) |
| 11 | Why Do We Need Positional Encoding? | [`11-why-do-we-need-positional-encoding.py`](11-why-do-we-need-positional-encoding.py) | 2 | 0 | [link](https://books.vizuara.ai/read/transformers-from-scratch/why-do-we-need-positional-encoding) |
| 12 | Multi-Head Attention | [`12-multi-head-attention.py`](12-multi-head-attention.py) | 1 | 0 | [link](https://books.vizuara.ai/read/transformers-from-scratch/multi-head-attention) |
| 14 | Scaled Dot-Product Attention | [`14-scaled-dot-product-attention.py`](14-scaled-dot-product-attention.py) | 1 | 0 | [link](https://books.vizuara.ai/read/transformers-from-scratch/scaled-dot-product-attention) |
| 15 | The Encoder Block | [`15-the-encoder-block.py`](15-the-encoder-block.py) | 2 | 0 | [link](https://books.vizuara.ai/read/transformers-from-scratch/the-encoder-block) |
| 17 | Tokenization and the Dataset | [`17-tokenization-and-the-dataset.py`](17-tokenization-and-the-dataset.py) | 2 | 0 | [link](https://books.vizuara.ai/read/transformers-from-scratch/tokenization-and-the-dataset) |
| 18 | Coding the Input and Attention Layers | [`18-coding-the-input-and-attention-layers.py`](18-coding-the-input-and-attention-layers.py) | 4 | 0 | [link](https://books.vizuara.ai/read/transformers-from-scratch/coding-the-input-and-attention-layers) |
| 19 | Assembling and Training the Transformer | [`19-assembling-and-training-the-transformer.py`](19-assembling-and-training-the-transformer.py) | 3 | 2 | [link](https://books.vizuara.ai/read/transformers-from-scratch/assembling-and-training-the-transformer) |

## Notes

- Each file concatenates that chapter's Python blocks in document order, separated by `# --- block N ---` markers.
- Non-Python blocks (shell commands, sample output, JSON, plain text) are not included.
- Blocks are teaching excerpts. Many assume variables or imports introduced earlier in the chapter or in an earlier chapter, so an individual file is not guaranteed to run standalone.
- The only code the generator writes itself is the `# --- imports (added by the generator) ---` block: a canonical import line for a well-known alias (`np`, `torch`, `nn`, ...) that the chapter uses as a module but never imports and never assigns. Nothing else is added, and no book code is rewritten.
- A block tagged `python` in the book that will not compile - prose, pseudo-code, or a fragment shown out of context - is kept verbatim but commented out, labelled `# --- block N (DOES NOT COMPILE - COMMENTED OUT) ---`.

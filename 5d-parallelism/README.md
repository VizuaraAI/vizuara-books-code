# 5D Parallelism for Large Model Training - companion code

Runnable code extracted from every chapter of [5D Parallelism for Large Model Training](https://books.vizuara.ai/read/5d-parallelism), in reading order.

These files are **generated** from the book text by `tools/build_companion_repo.py`. Do not hand-edit them.

20 of 40 chapters contain Python code (37 code blocks total).

| # | Chapter | File | Blocks | Added imports | Read online |
|---|---------|------|--------|---------------|-------------|
| 7 | Activation Recomputation | [`07-activation-recomputation.py`](07-activation-recomputation.py) | 2 | 0 | [link](https://books.vizuara.ai/read/5d-parallelism/activation-recomputation) |
| 8 | Gradient Accumulation | [`08-gradient-accumulation.py`](08-gradient-accumulation.py) | 1 | 0 | [link](https://books.vizuara.ai/read/5d-parallelism/gradient-accumulation) |
| 9 | Data Parallelism from Scratch | [`09-data-parallelism-from-scratch.py`](09-data-parallelism-from-scratch.py) | 2 | 0 | [link](https://books.vizuara.ai/read/5d-parallelism/data-parallelism-from-scratch) |
| 12 | Profiling with TensorBoard | [`12-profiling-with-tensorboard.py`](12-profiling-with-tensorboard.py) | 1 | 0 | [link](https://books.vizuara.ai/read/5d-parallelism/profiling-with-tensorboard) |
| 13 | Overlapping Communication and Compute | [`13-overlapping-communication-and-compute.py`](13-overlapping-communication-and-compute.py) | 1 | 0 | [link](https://books.vizuara.ai/read/5d-parallelism/overlapping-communication-and-compute) |
| 17 | Implementing ZeRO from Scratch | [`17-implementing-zero-from-scratch.py`](17-implementing-zero-from-scratch.py) | 2 | 0 | [link](https://books.vizuara.ai/read/5d-parallelism/implementing-zero-from-scratch) |
| 18 | Why Split a Single Layer | [`18-why-split-a-single-layer.py`](18-why-split-a-single-layer.py) | 1 | 0 | [link](https://books.vizuara.ai/read/5d-parallelism/why-split-a-single-layer) |
| 20 | Tensor Parallelism for the Transformer Block | [`20-tensor-parallelism-for-the-transformer-block.py`](20-tensor-parallelism-for-the-transformer-block.py) | 1 | 0 | [link](https://books.vizuara.ai/read/5d-parallelism/tensor-parallelism-for-the-transformer-block) |
| 21 | Tensor Parallelism from Scratch | [`21-tensor-parallelism-from-scratch.py`](21-tensor-parallelism-from-scratch.py) | 4 | 0 | [link](https://books.vizuara.ai/read/5d-parallelism/tensor-parallelism-from-scratch) |
| 23 | The Long-Sequence Memory Wall | [`23-the-long-sequence-memory-wall.py`](23-the-long-sequence-memory-wall.py) | 1 | 0 | [link](https://books.vizuara.ai/read/5d-parallelism/the-long-sequence-memory-wall) |
| 25 | Sequence Parallelism from Scratch | [`25-sequence-parallelism-from-scratch.py`](25-sequence-parallelism-from-scratch.py) | 4 | 0 | [link](https://books.vizuara.ai/read/5d-parallelism/sequence-parallelism-from-scratch) |
| 26 | Context Parallelism and Ring Attention | [`26-context-parallelism-and-ring-attention.py`](26-context-parallelism-and-ring-attention.py) | 2 | 0 | [link](https://books.vizuara.ai/read/5d-parallelism/context-parallelism-and-ring-attention) |
| 27 | Naive Context Parallelism from Scratch | [`27-naive-context-parallelism-from-scratch.py`](27-naive-context-parallelism-from-scratch.py) | 1 | 0 | [link](https://books.vizuara.ai/read/5d-parallelism/naive-context-parallelism-from-scratch) |
| 31 | Pipeline Parallelism from Scratch | [`31-pipeline-parallelism-from-scratch.py`](31-pipeline-parallelism-from-scratch.py) | 3 | 0 | [link](https://books.vizuara.ai/read/5d-parallelism/pipeline-parallelism-from-scratch) |
| 33 | Mixture-of-Experts Basics | [`33-mixture-of-experts-basics.py`](33-mixture-of-experts-basics.py) | 1 | 0 | [link](https://books.vizuara.ai/read/5d-parallelism/mixture-of-experts-basics) |
| 34 | Expert Parallelism Explained | [`34-expert-parallelism-explained.py`](34-expert-parallelism-explained.py) | 1 | 0 | [link](https://books.vizuara.ai/read/5d-parallelism/expert-parallelism-explained) |
| 35 | Load Balancing and Token Routing | [`35-load-balancing-and-token-routing.py`](35-load-balancing-and-token-routing.py) | 2 | 0 | [link](https://books.vizuara.ai/read/5d-parallelism/load-balancing-and-token-routing) |
| 36 | Build an MoE SLM from Scratch | [`36-build-an-moe-slm-from-scratch.py`](36-build-an-moe-slm-from-scratch.py) | 4 | 0 | [link](https://books.vizuara.ai/read/5d-parallelism/build-an-moe-slm-from-scratch) |
| 38 | Distributing GPT-2 Across a Cluster | [`38-distributing-gpt-2-across-a-cluster.py`](38-distributing-gpt-2-across-a-cluster.py) | 1 | 1 | [link](https://books.vizuara.ai/read/5d-parallelism/distributing-gpt-2-across-a-cluster) |
| 39 | Build an SLM with 5D Parallelism | [`39-build-an-slm-with-5d-parallelism.py`](39-build-an-slm-with-5d-parallelism.py) | 2 | 0 | [link](https://books.vizuara.ai/read/5d-parallelism/build-an-slm-with-5d-parallelism) |

## Notes

- Each file concatenates that chapter's Python blocks in document order, separated by `# --- block N ---` markers.
- Non-Python blocks (shell commands, sample output, JSON, plain text) are not included.
- Blocks are teaching excerpts. Many assume variables or imports introduced earlier in the chapter or in an earlier chapter, so an individual file is not guaranteed to run standalone.
- The only code the generator writes itself is the `# --- imports (added by the generator) ---` block: a canonical import line for a well-known alias (`np`, `torch`, `nn`, ...) that the chapter uses as a module but never imports and never assigns. Nothing else is added, and no book code is rewritten.
- A block tagged `python` in the book that will not compile - prose, pseudo-code, or a fragment shown out of context - is kept verbatim but commented out, labelled `# --- block N (DOES NOT COMPILE - COMMENTED OUT) ---`.

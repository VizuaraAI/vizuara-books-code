# Kernel Engineering - companion code

Runnable code extracted from every chapter of [Kernel Engineering](https://books.vizuara.ai/read/kernel-engineering), in reading order.

These files are **generated** from the book text by `tools/build_companion_repo.py`. Do not hand-edit them.

15 of 72 chapters contain Python code (33 code blocks total).

| # | Chapter | File | Blocks | Added imports | Read online |
|---|---------|------|--------|---------------|-------------|
| 3 | Speed-of-light thinking & the roofline | [`03-speed-of-light-thinking.py`](03-speed-of-light-thinking.py) | 1 | 0 | [link](https://books.vizuara.ai/read/kernel-engineering/speed-of-light-thinking) |
| 17 | Occupancy: the balancing act | [`17-occupancy.py`](17-occupancy.py) | 1 | 0 | [link](https://books.vizuara.ai/read/kernel-engineering/occupancy) |
| 27 | Atomics & reductions | [`27-atomics-and-reductions.py`](27-atomics-and-reductions.py) | 1 | 0 | [link](https://books.vizuara.ai/read/kernel-engineering/atomics-and-reductions) |
| 30 | GPU Puzzles, walkthrough I | [`30-gpu-puzzles-walkthrough-1.py`](30-gpu-puzzles-walkthrough-1.py) | 7 | 0 | [link](https://books.vizuara.ai/read/kernel-engineering/gpu-puzzles-walkthrough-1) |
| 31 | GPU Puzzles, walkthrough II | [`31-gpu-puzzles-walkthrough-2.py`](31-gpu-puzzles-walkthrough-2.py) | 4 | 0 | [link](https://books.vizuara.ai/read/kernel-engineering/gpu-puzzles-walkthrough-2) |
| 38 | Kernel 7: Autotuning the tiles | [`38-gemm-kernel-7-autotuning.py`](38-gemm-kernel-7-autotuning.py) | 2 | 1 | [link](https://books.vizuara.ai/read/kernel-engineering/gemm-kernel-7-autotuning) |
| 42 | Benchmarking without lying to yourself | [`42-gemm-benchmark-methodology.py`](42-gemm-benchmark-methodology.py) | 2 | 0 | [link](https://books.vizuara.ai/read/kernel-engineering/gemm-benchmark-methodology) |
| 49 | Softmax from scratch (and online) | [`49-softmax-from-scratch.py`](49-softmax-from-scratch.py) | 3 | 1 | [link](https://books.vizuara.ai/read/kernel-engineering/softmax-from-scratch) |
| 51 | Attention, the naive way | [`51-attention-naive.py`](51-attention-naive.py) | 1 | 1 | [link](https://books.vizuara.ai/read/kernel-engineering/attention-naive) |
| 52 | FlashAttention I: tiling attention | [`52-flashattention-1.py`](52-flashattention-1.py) | 3 | 0 | [link](https://books.vizuara.ai/read/kernel-engineering/flashattention-1) |
| 53 | FlashAttention II: better work partitioning | [`53-flashattention-2.py`](53-flashattention-2.py) | 2 | 0 | [link](https://books.vizuara.ai/read/kernel-engineering/flashattention-2) |
| 64 | DeepSeek's open kernels: FlashMLA & DeepGEMM | [`64-deepseek-flashmla-deepgemm.py`](64-deepseek-flashmla-deepgemm.py) | 2 | 0 | [link](https://books.vizuara.ai/read/kernel-engineering/deepseek-flashmla-deepgemm) |
| 65 | DSpark: speculative decoding as a kernel problem | [`65-deepseek-dspark-speculative.py`](65-deepseek-dspark-speculative.py) | 1 | 0 | [link](https://books.vizuara.ai/read/kernel-engineering/deepseek-dspark-speculative) |
| 67 | CuTe, the DSL landscape & Triton | [`67-cute-dsl-tilelang.py`](67-cute-dsl-tilelang.py) | 2 | 0 | [link](https://books.vizuara.ai/read/kernel-engineering/cute-dsl-tilelang) |
| 70 | Monkeys & search: test-time scaling | [`70-test-time-scaling-and-search.py`](70-test-time-scaling-and-search.py) | 1 | 0 | [link](https://books.vizuara.ai/read/kernel-engineering/test-time-scaling-and-search) |

## Notes

- Each file concatenates that chapter's Python blocks in document order, separated by `# --- block N ---` markers.
- Non-Python blocks (shell commands, sample output, JSON, plain text) are not included.
- Blocks are teaching excerpts. Many assume variables or imports introduced earlier in the chapter or in an earlier chapter, so an individual file is not guaranteed to run standalone.
- The only code the generator writes itself is the `# --- imports (added by the generator) ---` block: a canonical import line for a well-known alias (`np`, `torch`, `nn`, ...) that the chapter uses as a module but never imports and never assigns. Nothing else is added, and no book code is rewritten.
- A block tagged `python` in the book that will not compile - prose, pseudo-code, or a fragment shown out of context - is kept verbatim but commented out, labelled `# --- block N (DOES NOT COMPILE - COMMENTED OUT) ---`.

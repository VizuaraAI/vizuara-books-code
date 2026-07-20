# Build a Diffusion Language Model from Scratch - companion code

Runnable code extracted from every chapter of [Build a Diffusion Language Model from Scratch](https://books.vizuara.ai/read/diffusion-lm-from-scratch), in reading order.

These files are **generated** from the book text by `tools/build_companion_repo.py`. Do not hand-edit them.

21 of 35 chapters contain Python code (54 code blocks total).

| # | Chapter | File | Blocks | Added imports | Read online |
|---|---------|------|--------|---------------|-------------|
| 3 | Representing Text in a Vector Space | [`03-text-in-vector-space.py`](03-text-in-vector-space.py) | 1 | 0 | [link](https://books.vizuara.ai/read/diffusion-lm-from-scratch/text-in-vector-space) |
| 6 | Language Models as Distribution Approximators | [`06-language-models-as-distribution-approximators.py`](06-language-models-as-distribution-approximators.py) | 1 | 0 | [link](https://books.vizuara.ai/read/diffusion-lm-from-scratch/language-models-as-distribution-approximators) |
| 7 | Generative AI: One Probabilistic View of Everything | [`07-generative-ai-probabilistic-view.py`](07-generative-ai-probabilistic-view.py) | 1 | 0 | [link](https://books.vizuara.ai/read/diffusion-lm-from-scratch/generative-ai-probabilistic-view) |
| 8 | Diffusion for Image Generation | [`08-diffusion-for-image-generation.py`](08-diffusion-for-image-generation.py) | 1 | 0 | [link](https://books.vizuara.ai/read/diffusion-lm-from-scratch/diffusion-for-image-generation) |
| 9 | The Noising and Denoising Loop | [`09-noising-and-denoising.py`](09-noising-and-denoising.py) | 1 | 0 | [link](https://books.vizuara.ai/read/diffusion-lm-from-scratch/noising-and-denoising) |
| 12 | Tokenization and Embeddings | [`12-tokenization-and-embeddings.py`](12-tokenization-and-embeddings.py) | 3 | 0 | [link](https://books.vizuara.ai/read/diffusion-lm-from-scratch/tokenization-and-embeddings) |
| 13 | The Attention Mechanism | [`13-attention-mechanism.py`](13-attention-mechanism.py) | 4 | 1 | [link](https://books.vizuara.ai/read/diffusion-lm-from-scratch/attention-mechanism) |
| 14 | The Causal Attention Mask | [`14-causal-attention-mask.py`](14-causal-attention-mask.py) | 3 | 0 | [link](https://books.vizuara.ai/read/diffusion-lm-from-scratch/causal-attention-mask) |
| 15 | Inside the Transformer Block | [`15-the-transformer-block.py`](15-the-transformer-block.py) | 2 | 1 | [link](https://books.vizuara.ai/read/diffusion-lm-from-scratch/the-transformer-block) |
| 16 | Build an Autoregressive LLM from Scratch | [`16-build-autoregressive-llm-from-scratch.py`](16-build-autoregressive-llm-from-scratch.py) | 4 | 0 | [link](https://books.vizuara.ai/read/diffusion-lm-from-scratch/build-autoregressive-llm-from-scratch) |
| 18 | The Forward Masking Process | [`18-the-forward-masking-process.py`](18-the-forward-masking-process.py) | 2 | 0 | [link](https://books.vizuara.ai/read/diffusion-lm-from-scratch/the-forward-masking-process) |
| 19 | The Matrix and Vector Operations Under the Hood | [`19-matrix-and-vector-operations.py`](19-matrix-and-vector-operations.py) | 3 | 0 | [link](https://books.vizuara.ai/read/diffusion-lm-from-scratch/matrix-and-vector-operations) |
| 23 | The Denoising Process in Detail | [`23-the-denoising-process-in-detail.py`](23-the-denoising-process-in-detail.py) | 1 | 0 | [link](https://books.vizuara.ai/read/diffusion-lm-from-scratch/the-denoising-process-in-detail) |
| 24 | Token Unmasking Schedules | [`24-token-unmasking-schedules.py`](24-token-unmasking-schedules.py) | 1 | 0 | [link](https://books.vizuara.ai/read/diffusion-lm-from-scratch/token-unmasking-schedules) |
| 26 | The Coherence vs Speed Tradeoff | [`26-coherence-speed-tradeoff.py`](26-coherence-speed-tradeoff.py) | 1 | 0 | [link](https://books.vizuara.ai/read/diffusion-lm-from-scratch/coherence-speed-tradeoff) |
| 28 | Data Preprocessing and Tokenization | [`28-data-preprocessing-and-tokenization.py`](28-data-preprocessing-and-tokenization.py) | 4 | 0 | [link](https://books.vizuara.ai/read/diffusion-lm-from-scratch/data-preprocessing-and-tokenization) |
| 29 | The Forward Pass: Code Walkthrough | [`29-the-forward-pass-code-walkthrough.py`](29-the-forward-pass-code-walkthrough.py) | 7 | 0 | [link](https://books.vizuara.ai/read/diffusion-lm-from-scratch/the-forward-pass-code-walkthrough) |
| 30 | Training the Diffusion LM | [`30-training-the-diffusion-lm.py`](30-training-the-diffusion-lm.py) | 4 | 1 | [link](https://books.vizuara.ai/read/diffusion-lm-from-scratch/training-the-diffusion-lm) |
| 31 | Evaluation and Running Generation | [`31-evaluation-and-generation.py`](31-evaluation-and-generation.py) | 2 | 2 | [link](https://books.vizuara.ai/read/diffusion-lm-from-scratch/evaluation-and-generation) |
| 32 | Running on Colab and RunPod | [`32-running-on-colab-and-runpod.py`](32-running-on-colab-and-runpod.py) | 5 | 0 | [link](https://books.vizuara.ai/read/diffusion-lm-from-scratch/running-on-colab-and-runpod) |
| 33 | Putting It All Together | [`33-putting-it-all-together.py`](33-putting-it-all-together.py) | 3 | 2 | [link](https://books.vizuara.ai/read/diffusion-lm-from-scratch/putting-it-all-together) |

## Notes

- Each file concatenates that chapter's Python blocks in document order, separated by `# --- block N ---` markers.
- Non-Python blocks (shell commands, sample output, JSON, plain text) are not included.
- Blocks are teaching excerpts. Many assume variables or imports introduced earlier in the chapter or in an earlier chapter, so an individual file is not guaranteed to run standalone.
- The only code the generator writes itself is the `# --- imports (added by the generator) ---` block: a canonical import line for a well-known alias (`np`, `torch`, `nn`, ...) that the chapter uses as a module but never imports and never assigns. Nothing else is added, and no book code is rewritten.
- A block tagged `python` in the book that will not compile - prose, pseudo-code, or a fragment shown out of context - is kept verbatim but commented out, labelled `# --- block N (DOES NOT COMPILE - COMMENTED OUT) ---`.

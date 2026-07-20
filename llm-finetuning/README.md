# LLM Finetuning - companion code

Runnable code extracted from every chapter of [LLM Finetuning](https://books.vizuara.ai/read/llm-finetuning), in reading order.

These files are **generated** from the book text by `tools/build_companion_repo.py`. Do not hand-edit them.

25 of 40 chapters contain Python code (60 code blocks total).

| # | Chapter | File | Blocks | Added imports | Read online |
|---|---------|------|--------|---------------|-------------|
| 2 | Pretraining vs Finetuning | [`02-pretraining-vs-finetuning.py`](02-pretraining-vs-finetuning.py) | 1 | 0 | [link](https://books.vizuara.ai/read/llm-finetuning/pretraining-vs-finetuning) |
| 7 | How RAG Works | [`07-how-rag-works.py`](07-how-rag-works.py) | 1 | 0 | [link](https://books.vizuara.ai/read/llm-finetuning/how-rag-works) |
| 12 | Anatomy of an Instruction Dataset | [`12-anatomy-of-an-instruction-dataset.py`](12-anatomy-of-an-instruction-dataset.py) | 1 | 0 | [link](https://books.vizuara.ai/read/llm-finetuning/anatomy-of-an-instruction-dataset) |
| 13 | Tokenizing and Formatting the Data | [`13-tokenizing-and-formatting.py`](13-tokenizing-and-formatting.py) | 4 | 0 | [link](https://books.vizuara.ai/read/llm-finetuning/tokenizing-and-formatting) |
| 14 | The Finetuning Training Loop | [`14-the-finetuning-training-loop.py`](14-the-finetuning-training-loop.py) | 4 | 0 | [link](https://books.vizuara.ai/read/llm-finetuning/the-finetuning-training-loop) |
| 15 | Sparse Finetuning and Layer Norms | [`15-sparse-finetuning-and-layer-norms.py`](15-sparse-finetuning-and-layer-norms.py) | 3 | 1 | [link](https://books.vizuara.ai/read/llm-finetuning/sparse-finetuning-and-layer-norms) |
| 17 | How OpenAI Uses Finetuning | [`17-openai-finetuning-in-practice.py`](17-openai-finetuning-in-practice.py) | 1 | 0 | [link](https://books.vizuara.ai/read/llm-finetuning/openai-finetuning-in-practice) |
| 18 | The Hugging Face Ecosystem | [`18-the-huggingface-ecosystem.py`](18-the-huggingface-ecosystem.py) | 4 | 0 | [link](https://books.vizuara.ai/read/llm-finetuning/the-huggingface-ecosystem) |
| 19 | Loading and Testing the Tiny Stories Model | [`19-loading-and-testing-tiny-stories.py`](19-loading-and-testing-tiny-stories.py) | 4 | 0 | [link](https://books.vizuara.ai/read/llm-finetuning/loading-and-testing-tiny-stories) |
| 20 | Instruction vs Classification Finetuning | [`20-instruction-vs-classification-finetuning.py`](20-instruction-vs-classification-finetuning.py) | 1 | 0 | [link](https://books.vizuara.ai/read/llm-finetuning/instruction-vs-classification-finetuning) |
| 21 | Adding a Custom Classification Head | [`21-adding-a-classification-head.py`](21-adding-a-classification-head.py) | 3 | 0 | [link](https://books.vizuara.ai/read/llm-finetuning/adding-a-classification-head) |
| 22 | Data Collation and Dynamic Padding | [`22-data-collation-and-dynamic-padding.py`](22-data-collation-and-dynamic-padding.py) | 2 | 0 | [link](https://books.vizuara.ai/read/llm-finetuning/data-collation-and-dynamic-padding) |
| 23 | Left vs Right Padding | [`23-left-vs-right-padding.py`](23-left-vs-right-padding.py) | 4 | 0 | [link](https://books.vizuara.ai/read/llm-finetuning/left-vs-right-padding) |
| 24 | A Finetuning Project with Unsloth | [`24-finetuning-project-with-unsloth.py`](24-finetuning-project-with-unsloth.py) | 4 | 0 | [link](https://books.vizuara.ai/read/llm-finetuning/finetuning-project-with-unsloth) |
| 28 | Implementing LoRA in GPT-2 | [`28-implementing-lora-in-gpt2.py`](28-implementing-lora-in-gpt2.py) | 3 | 0 | [link](https://books.vizuara.ai/read/llm-finetuning/implementing-lora-in-gpt2) |
| 29 | The PEFT Training Loop | [`29-the-peft-training-loop.py`](29-the-peft-training-loop.py) | 3 | 2 | [link](https://books.vizuara.ai/read/llm-finetuning/the-peft-training-loop) |
| 30 | Tuning LoRA Hyperparameters | [`30-tuning-lora-hyperparameters.py`](30-tuning-lora-hyperparameters.py) | 1 | 0 | [link](https://books.vizuara.ai/read/llm-finetuning/tuning-lora-hyperparameters) |
| 31 | QLoRA and Quantized Finetuning | [`31-qlora-and-quantized-finetuning.py`](31-qlora-and-quantized-finetuning.py) | 1 | 0 | [link](https://books.vizuara.ai/read/llm-finetuning/qlora-and-quantized-finetuning) |
| 32 | Replicating a Research Paper | [`32-replicating-a-paper-with-finetuning.py`](32-replicating-a-paper-with-finetuning.py) | 1 | 0 | [link](https://books.vizuara.ai/read/llm-finetuning/replicating-a-paper-with-finetuning) |
| 34 | Generating Training Data at Scale | [`34-generating-training-data-at-scale.py`](34-generating-training-data-at-scale.py) | 3 | 0 | [link](https://books.vizuara.ai/read/llm-finetuning/generating-training-data-at-scale) |
| 35 | Finetuning on the OpenAI Platform | [`35-finetuning-on-the-openai-platform.py`](35-finetuning-on-the-openai-platform.py) | 4 | 0 | [link](https://books.vizuara.ai/read/llm-finetuning/finetuning-on-the-openai-platform) |
| 36 | RAFT: Retrieval-Augmented Finetuning | [`36-raft-retrieval-augmented-finetuning.py`](36-raft-retrieval-augmented-finetuning.py) | 1 | 0 | [link](https://books.vizuara.ai/read/llm-finetuning/raft-retrieval-augmented-finetuning) |
| 37 | Setting Up a RAFT Project | [`37-raft-project-setup.py`](37-raft-project-setup.py) | 1 | 1 | [link](https://books.vizuara.ai/read/llm-finetuning/raft-project-setup) |
| 39 | The Workshop Code and Resources | [`39-the-workshop-code-and-resources.py`](39-the-workshop-code-and-resources.py) | 2 | 0 | [link](https://books.vizuara.ai/read/llm-finetuning/the-workshop-code-and-resources) |
| 40 | Capstone: Ship a Finetuned Model | [`40-capstone-ship-a-finetuned-model.py`](40-capstone-ship-a-finetuned-model.py) | 3 | 0 | [link](https://books.vizuara.ai/read/llm-finetuning/capstone-ship-a-finetuned-model) |

## Notes

- Each file concatenates that chapter's Python blocks in document order, separated by `# --- block N ---` markers.
- Non-Python blocks (shell commands, sample output, JSON, plain text) are not included.
- Blocks are teaching excerpts. Many assume variables or imports introduced earlier in the chapter or in an earlier chapter, so an individual file is not guaranteed to run standalone.
- The only code the generator writes itself is the `# --- imports (added by the generator) ---` block: a canonical import line for a well-known alias (`np`, `torch`, `nn`, ...) that the chapter uses as a module but never imports and never assigns. Nothing else is added, and no book code is rewritten.
- A block tagged `python` in the book that will not compile - prose, pseudo-code, or a fragment shown out of context - is kept verbatim but commented out, labelled `# --- block N (DOES NOT COMPILE - COMMENTED OUT) ---`.

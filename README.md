# Vizuara Books - companion code

The code from the books, pulled out so you can run it.

One folder per book (39 books). Inside each folder, one Python file per chapter that contains code, named `NN-<chapter-slug>.py` where `NN` is the chapter's position in the book's reading order, plus a matching Colab notebook `NN-<chapter-slug>.ipynb`. Each file's header links back to the chapter it came from on [books.vizuara.ai](https://books.vizuara.ai).

**1015 Python files, 1015 notebooks, 2309 code blocks.**

## These files are generated

Everything here is produced mechanically from the books themselves. **Do not hand-edit anything in this repo** - the next build overwrites it. If code is wrong, the bug is in the book: fix the book and the fix flows here. Pull requests that patch a `.py` or `.ipynb` file directly will be closed; open an issue naming the book and chapter instead.

The `.ipynb` files are generated from the `.py` files, not written by hand. The first cell is a markdown header (book title, chapter title, link back to the chapter). After that there is one code cell per `# --- block N ---` section, in chapter order, plus a setup cell first where the extractor had to resolve names the chapter uses but never defines.

## What is and is not included

- Only Python blocks are extracted. Shell commands, sample output, JSON and
  plain-text blocks are left in the book.
- Blocks are concatenated in document order with `# --- block N ---` markers.
- A block the book tagged `python` that is actually prose or pseudo-code is kept
  verbatim but commented out and labelled
  `# --- block N (DOES NOT COMPILE - COMMENTED OUT) ---`. It is never "repaired"
  into plausible code. Every one of these is an authoring bug in the book and is
  listed in [SMOKE.md](SMOKE.md) (117 blocks across 27 books; 102 of them carry the
  "DOES NOT COMPILE - COMMENTED OUT" label, the rest use other commented-out labels).
- Where a chapter uses a name an earlier chapter defined and never repeated, the
  earlier definition is copied verbatim into that book's `context.py`.

## What is guaranteed, and what is not

**Guaranteed.**

- Every one of the 1015 `.py` files passes `python -m py_compile`. That is a
  syntax check: the file parses as valid Python.
- Every one of the 1015 `.ipynb` files is valid nbformat 4 JSON that
  `json.load` parses and Colab opens.
- Every line inside a `# --- block N ---` section is the book's own code, copied
  verbatim. No book code has been rewritten, "repaired", or invented to make a
  check pass.
- Where the book uses a name it never defines (a model handle, a dataset path, an
  API key, a hyper-parameter left to the reader), a **placeholder** is declared in a
  clearly labelled `# --- stubs (not book code) ---` section above the blocks, so the
  file can run. There are 445 such placeholder lines across 159 files. They are
  ours, not the book's, and they are marked as such at every site. Anything outside a
  stub section and inside a block marker came from the book.

**Not guaranteed.**

- **Nothing here has been executed.** Not once. The code needs GPUs, datasets, API
  keys and paid accounts, so running it was never part of the build. A file that
  compiles can still fail on the first line you run.
- Static checking is partial. 692 of 1015 files (68.2%)
  are pyflakes-clean; the rest carry warnings, overwhelmingly `undefined name`
  because a teaching excerpt legitimately continues from an earlier block or an
  earlier chapter. See [SMOKE.md](SMOKE.md) for the per-book breakdown.
- Individual files are not standalone programs. They are excerpts in reading order.
- `requirements.txt` is best-effort: it is derived by scanning the extracted code
  for third-party imports. It is not a tested lockfile and pins no versions.

## Running it

```bash
cd <book-id>
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python 01-<chapter>.py
```

Or open the matching `.ipynb` in Google Colab and run the cells in order.

Read the chapter alongside the code. The files follow the book, not the other way round, and a block will often only make sense next to the prose that introduces it.

## Books

Sorted by number of code blocks. `Chapter files` is one Python file per chapter that contains code. `context.py` is the extra per-book file holding definitions copied verbatim from earlier chapters. `Notebooks` is the total, one `.ipynb` per `.py`.

| Book | Book ID | Chapter files | context.py | Notebooks | Code blocks | Index |
|------|---------|--------------:|-----------:|----------:|------------:|-------|
| Python for Data Science | `python-for-data-science` | 36 | yes | 37 | 194 | [python-for-data-science/](python-for-data-science/README.md) |
| Data Structures & Algorithms in Python | `dsa-in-python` | 69 | - | 69 | 191 | [dsa-in-python/](dsa-in-python/README.md) |
| Machine Learning & Deep Learning Mastery | `ml-dl-mastery` | 34 | yes | 35 | 90 | [ml-dl-mastery/](ml-dl-mastery/README.md) |
| Build a NanoVLM from Scratch | `nanovlm-from-scratch` | 32 | yes | 33 | 87 | [nanovlm-from-scratch/](nanovlm-from-scratch/README.md) |
| AI Agents Bootcamp | `ai-agents-bootcamp` | 34 | yes | 35 | 83 | [ai-agents-bootcamp/](ai-agents-bootcamp/README.md) |
| Harness Engineering | `harness-engineering` | 28 | yes | 29 | 83 | [harness-engineering/](harness-engineering/README.md) |
| Mathematical Foundations for Machine Learning | `math-foundations-for-ml` | 26 | yes | 27 | 80 | [math-foundations-for-ml/](math-foundations-for-ml/README.md) |
| Deep Learning Fundamentals | `deep-learning-fundamentals` | 35 | yes | 36 | 78 | [deep-learning-fundamentals/](deep-learning-fundamentals/README.md) |
| Foundations for AI & ML | `foundations-for-ai-ml` | 28 | - | 28 | 75 | [foundations-for-ai-ml/](foundations-for-ai-ml/README.md) |
| LLM Production & Deployment | `llm-production-deployment` | 33 | yes | 34 | 73 | [llm-production-deployment/](llm-production-deployment/README.md) |
| Memory in AI Systems | `memory-workshop` | 33 | yes | 34 | 68 | [memory-workshop/](memory-workshop/README.md) |
| NLP & Computer Vision Mastery | `nlp-cv-mastery` | 33 | yes | 34 | 69 | [nlp-cv-mastery/](nlp-cv-mastery/README.md) |
| Computer Vision Bootcamp | `computer-vision-bootcamp` | 29 | - | 29 | 65 | [computer-vision-bootcamp/](computer-vision-bootcamp/README.md) |
| Neural Networks from Scratch | `neural-networks-from-scratch` | 28 | yes | 29 | 63 | [neural-networks-from-scratch/](neural-networks-from-scratch/README.md) |
| Build a Data-Efficient Image Transformer (DeiT) from Scratch | `deit-from-scratch` | 31 | - | 31 | 61 | [deit-from-scratch/](deit-from-scratch/README.md) |
| Transformers for Vision & Multimodal LLMs | `transformers-for-vision-multimodal` | 29 | - | 29 | 61 | [transformers-for-vision-multimodal/](transformers-for-vision-multimodal/README.md) |
| Build a Vision Transformer (ViT) from Scratch | `vit-from-scratch` | 24 | - | 24 | 61 | [vit-from-scratch/](vit-from-scratch/README.md) |
| LLM Finetuning | `llm-finetuning` | 25 | - | 25 | 60 | [llm-finetuning/](llm-finetuning/README.md) |
| Reinforcement Learning | `reinforcement-learning` | 31 | - | 31 | 60 | [reinforcement-learning/](reinforcement-learning/README.md) |
| RAG in Production | `rag-in-production` | 29 | yes | 30 | 57 | [rag-in-production/](rag-in-production/README.md) |
| Generative AI Fundamentals | `generative-ai-fundamentals` | 30 | - | 30 | 56 | [generative-ai-fundamentals/](generative-ai-fundamentals/README.md) |
| Build a Diffusion Language Model from Scratch | `diffusion-lm-from-scratch` | 21 | - | 21 | 54 | [diffusion-lm-from-scratch/](diffusion-lm-from-scratch/README.md) |
| Vision-Language-Action & World Models for Robotics | `vla-world-models-robotics` | 34 | - | 34 | 49 | [vla-world-models-robotics/](vla-world-models-robotics/README.md) |
| AI Context Engineering | `ai-context-engineering` | 25 | - | 25 | 46 | [ai-context-engineering/](ai-context-engineering/README.md) |
| Modern Robot Learning | `modern-robot-learning` | 26 | - | 26 | 46 | [modern-robot-learning/](modern-robot-learning/README.md) |
| Build Large Language Models (LLMs) from Scratch | `build-llm-from-scratch` | 19 | yes | 20 | 43 | [build-llm-from-scratch/](build-llm-from-scratch/README.md) |
| Machine Learning Fundamentals | `machine-learning-fundamentals` | 23 | - | 23 | 42 | [machine-learning-fundamentals/](machine-learning-fundamentals/README.md) |
| Claude Certified Architect (CCAF) | `claude-certified-architect` | 24 | - | 24 | 41 | [claude-certified-architect/](claude-certified-architect/README.md) |
| 5D Parallelism for Large Model Training | `5d-parallelism` | 20 | - | 20 | 37 | [5d-parallelism/](5d-parallelism/README.md) |
| Convolutional Neural Networks Fundamentals | `cnn-fundamentals` | 24 | - | 24 | 36 | [cnn-fundamentals/](cnn-fundamentals/README.md) |
| RLHF from Scratch | `rlhf-from-scratch` | 22 | - | 22 | 35 | [rlhf-from-scratch/](rlhf-from-scratch/README.md) |
| Kernel Engineering | `kernel-engineering` | 15 | - | 15 | 33 | [kernel-engineering/](kernel-engineering/README.md) |
| The Modern Software Developer | `modern-software-developer` | 19 | - | 19 | 33 | [modern-software-developer/](modern-software-developer/README.md) |
| Build Decision Trees from Scratch | `decision-trees-from-scratch` | 17 | - | 17 | 28 | [decision-trees-from-scratch/](decision-trees-from-scratch/README.md) |
| Transformers: Theory, intuition, and Building from Scratch | `transformers-from-scratch` | 15 | - | 15 | 26 | [transformers-from-scratch/](transformers-from-scratch/README.md) |
| SQL Masterclass | `sql-masterclass` | 6 | - | 6 | 22 | [sql-masterclass/](sql-masterclass/README.md) |
| Build a Mini ClawdBot from Scratch | `mini-clawdbot-from-scratch` | 8 | - | 8 | 14 | [mini-clawdbot-from-scratch/](mini-clawdbot-from-scratch/README.md) |
| Prompt Engineering | `prompt-engineering` | 4 | - | 4 | 6 | [prompt-engineering/](prompt-engineering/README.md) |
| Writing Journal & Conference Papers | `writing-research-papers` | 3 | - | 3 | 3 | [writing-research-papers/](writing-research-papers/README.md) |
| **Total (39 books)** | | **1002** | **13** | **1015** | **2309** | |

Each book folder has its own `README.md` with a per-chapter table.

## Honesty note

[SMOKE.md](SMOKE.md) carries the real numbers, recomputed from scratch over the files in this repo. Nothing failing has been dropped and nothing has been rounded up. If a book looks bad in that table, the book is bad and we want to know.

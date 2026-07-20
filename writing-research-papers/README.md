# Writing Journal & Conference Papers - companion code

Runnable code extracted from every chapter of [Writing Journal & Conference Papers](https://books.vizuara.ai/read/writing-research-papers), in reading order.

These files are **generated** from the book text by `tools/build_companion_repo.py`. Do not hand-edit them.

3 of 52 chapters contain Python code (3 code blocks total).

| # | Chapter | File | Blocks | Added imports | Read online |
|---|---------|------|--------|---------------|-------------|
| 22 | Finding the Thread of Your Paper | [`22-finding-the-thread-of-your-paper.py`](22-finding-the-thread-of-your-paper.py) | 1 | 0 | [link](https://books.vizuara.ai/read/writing-research-papers/finding-the-thread-of-your-paper) |
| 34 | Tools for Making Figures | [`34-tools-for-making-figures.py`](34-tools-for-making-figures.py) | 1 | 0 | [link](https://books.vizuara.ai/read/writing-research-papers/tools-for-making-figures) |
| 36 | Publication Graphs in Excel and Code | [`36-publication-graphs-in-excel-and-code.py`](36-publication-graphs-in-excel-and-code.py) | 1 | 0 | [link](https://books.vizuara.ai/read/writing-research-papers/publication-graphs-in-excel-and-code) |

## Notes

- Each file concatenates that chapter's Python blocks in document order, separated by `# --- block N ---` markers.
- Non-Python blocks (shell commands, sample output, JSON, plain text) are not included.
- Blocks are teaching excerpts. Many assume variables or imports introduced earlier in the chapter or in an earlier chapter, so an individual file is not guaranteed to run standalone.
- The only code the generator writes itself is the `# --- imports (added by the generator) ---` block: a canonical import line for a well-known alias (`np`, `torch`, `nn`, ...) that the chapter uses as a module but never imports and never assigns. Nothing else is added, and no book code is rewritten.
- A block tagged `python` in the book that will not compile - prose, pseudo-code, or a fragment shown out of context - is kept verbatim but commented out, labelled `# --- block N (DOES NOT COMPILE - COMMENTED OUT) ---`.

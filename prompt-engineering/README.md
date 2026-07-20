# Prompt Engineering - companion code

Runnable code extracted from every chapter of [Prompt Engineering](https://books.vizuara.ai/read/prompt-engineering), in reading order.

These files are **generated** from the book text by `tools/build_companion_repo.py`. Do not hand-edit them.

4 of 31 chapters contain Python code (6 code blocks total).

| # | Chapter | File | Blocks | Added imports | Read online |
|---|---------|------|--------|---------------|-------------|
| 3 | Why the Same Model Gives Different Answers | [`03-why-prompts-matter.py`](03-why-prompts-matter.py) | 1 | 0 | [link](https://books.vizuara.ai/read/prompt-engineering/why-prompts-matter) |
| 13 | Chat, Playground, and API | [`13-chat-vs-api-vs-playground.py`](13-chat-vs-api-vs-playground.py) | 1 | 0 | [link](https://books.vizuara.ai/read/prompt-engineering/chat-vs-api-vs-playground) |
| 15 | System, User, and Assistant Messages | [`15-system-user-assistant-messages.py`](15-system-user-assistant-messages.py) | 3 | 0 | [link](https://books.vizuara.ai/read/prompt-engineering/system-user-assistant-messages) |
| 21 | Role and Persona Prompting | [`21-role-and-persona-prompting.py`](21-role-and-persona-prompting.py) | 1 | 0 | [link](https://books.vizuara.ai/read/prompt-engineering/role-and-persona-prompting) |

## Notes

- Each file concatenates that chapter's Python blocks in document order, separated by `# --- block N ---` markers.
- Non-Python blocks (shell commands, sample output, JSON, plain text) are not included.
- Blocks are teaching excerpts. Many assume variables or imports introduced earlier in the chapter or in an earlier chapter, so an individual file is not guaranteed to run standalone.
- The only code the generator writes itself is the `# --- imports (added by the generator) ---` block: a canonical import line for a well-known alias (`np`, `torch`, `nn`, ...) that the chapter uses as a module but never imports and never assigns. Nothing else is added, and no book code is rewritten.
- A block tagged `python` in the book that will not compile - prose, pseudo-code, or a fragment shown out of context - is kept verbatim but commented out, labelled `# --- block N (DOES NOT COMPILE - COMMENTED OUT) ---`.

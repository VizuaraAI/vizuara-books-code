# Build a Mini ClawdBot from Scratch - companion code

Runnable code extracted from every chapter of [Build a Mini ClawdBot from Scratch](https://books.vizuara.ai/read/mini-clawdbot-from-scratch), in reading order.

These files are **generated** from the book text by `tools/build_companion_repo.py`. Do not hand-edit them.

8 of 37 chapters contain Python code (14 code blocks total).

| # | Chapter | File | Blocks | Added imports | Read online |
|---|---------|------|--------|---------------|-------------|
| 1 | What is ClawdBot? | [`01-what-is-clawdbot.py`](01-what-is-clawdbot.py) | 1 | 0 | [link](https://books.vizuara.ai/read/mini-clawdbot-from-scratch/what-is-clawdbot) |
| 2 | Why Build Your Own Agent? | [`02-why-build-your-own-agent.py`](02-why-build-your-own-agent.py) | 1 | 0 | [link](https://books.vizuara.ai/read/mini-clawdbot-from-scratch/why-build-your-own-agent) |
| 3 | The Three Pillars: RAG, Memory, and MCP | [`03-the-three-pillars-rag-memory-mcp.py`](03-the-three-pillars-rag-memory-mcp.py) | 1 | 0 | [link](https://books.vizuara.ai/read/mini-clawdbot-from-scratch/the-three-pillars-rag-memory-mcp) |
| 7 | The Agent Loop | [`07-the-agent-loop.py`](07-the-agent-loop.py) | 1 | 0 | [link](https://books.vizuara.ai/read/mini-clawdbot-from-scratch/the-agent-loop) |
| 10 | Wiring the First Agent Loop in Code | [`10-wiring-the-first-agent-loop-in-code.py`](10-wiring-the-first-agent-loop-in-code.py) | 2 | 0 | [link](https://books.vizuara.ai/read/mini-clawdbot-from-scratch/wiring-the-first-agent-loop-in-code) |
| 13 | Embeddings and Vector Search | [`13-embeddings-and-vector-search.py`](13-embeddings-and-vector-search.py) | 3 | 0 | [link](https://books.vizuara.ai/read/mini-clawdbot-from-scratch/embeddings-and-vector-search) |
| 17 | RAG vs Memory: When to Use Which | [`17-rag-vs-memory-when-to-use-which.py`](17-rag-vs-memory-when-to-use-which.py) | 1 | 0 | [link](https://books.vizuara.ai/read/mini-clawdbot-from-scratch/rag-vs-memory-when-to-use-which) |
| 21 | Build Your Own MCP Server from Scratch | [`21-build-your-own-mcp-server-from-scratch.py`](21-build-your-own-mcp-server-from-scratch.py) | 4 | 0 | [link](https://books.vizuara.ai/read/mini-clawdbot-from-scratch/build-your-own-mcp-server-from-scratch) |

## Notes

- Each file concatenates that chapter's Python blocks in document order, separated by `# --- block N ---` markers.
- Non-Python blocks (shell commands, sample output, JSON, plain text) are not included.
- Blocks are teaching excerpts. Many assume variables or imports introduced earlier in the chapter or in an earlier chapter, so an individual file is not guaranteed to run standalone.
- The only code the generator writes itself is the `# --- imports (added by the generator) ---` block: a canonical import line for a well-known alias (`np`, `torch`, `nn`, ...) that the chapter uses as a module but never imports and never assigns. Nothing else is added, and no book code is rewritten.
- A block tagged `python` in the book that will not compile - prose, pseudo-code, or a fragment shown out of context - is kept verbatim but commented out, labelled `# --- block N (DOES NOT COMPILE - COMMENTED OUT) ---`.

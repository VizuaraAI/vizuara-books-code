# The Modern Software Developer - companion code

Runnable code extracted from every chapter of [The Modern Software Developer](https://books.vizuara.ai/read/modern-software-developer), in reading order.

These files are **generated** from the book text by `tools/build_companion_repo.py`. Do not hand-edit them.

19 of 36 chapters contain Python code (33 code blocks total).

| # | Chapter | File | Blocks | Added imports | Read online |
|---|---------|------|--------|---------------|-------------|
| 2 | Software 1.2: The Hand-Coded Craft Era | [`02-software-1-2-the-craft-era.py`](02-software-1-2-the-craft-era.py) | 1 | 0 | [link](https://books.vizuara.ai/read/modern-software-developer/software-1-2-the-craft-era) |
| 4 | Software 1.8: The Cursor Era | [`04-software-1-8-the-cursor-era.py`](04-software-1-8-the-cursor-era.py) | 1 | 0 | [link](https://books.vizuara.ai/read/modern-software-developer/software-1-8-the-cursor-era) |
| 5 | Software 2.0: The Agentic Era | [`05-software-2-0-the-agentic-era.py`](05-software-2-0-the-agentic-era.py) | 1 | 0 | [link](https://books.vizuara.ai/read/modern-software-developer/software-2-0-the-agentic-era) |
| 6 | The Anatomy of a Coding Agent | [`06-anatomy-of-a-coding-agent.py`](06-anatomy-of-a-coding-agent.py) | 2 | 0 | [link](https://books.vizuara.ai/read/modern-software-developer/anatomy-of-a-coding-agent) |
| 10 | Building Your First Claude Skill | [`10-building-your-first-skill.py`](10-building-your-first-skill.py) | 1 | 0 | [link](https://books.vizuara.ai/read/modern-software-developer/building-your-first-skill) |
| 12 | Tools and Parameterized Function Calls | [`12-mcp-tools-and-function-calls.py`](12-mcp-tools-and-function-calls.py) | 1 | 0 | [link](https://books.vizuara.ai/read/modern-software-developer/mcp-tools-and-function-calls) |
| 13 | Local vs. External Data & Privacy Boundaries | [`13-local-vs-external-data-privacy.py`](13-local-vs-external-data-privacy.py) | 2 | 0 | [link](https://books.vizuara.ai/read/modern-software-developer/local-vs-external-data-privacy) |
| 15 | Build and Connect Your Own MCP Server | [`15-build-an-mcp-server.py`](15-build-an-mcp-server.py) | 1 | 0 | [link](https://books.vizuara.ai/read/modern-software-developer/build-an-mcp-server) |
| 16 | The Agentic Engineering Workflow | [`16-the-agentic-engineering-workflow.py`](16-the-agentic-engineering-workflow.py) | 1 | 0 | [link](https://books.vizuara.ai/read/modern-software-developer/the-agentic-engineering-workflow) |
| 19 | The Dev Skill and Test-Driven Development | [`19-the-dev-skill-and-tdd.py`](19-the-dev-skill-and-tdd.py) | 2 | 0 | [link](https://books.vizuara.ai/read/modern-software-developer/the-dev-skill-and-tdd) |
| 21 | Idea to Product: A Full PRD-Driven Build | [`21-prd-driven-project.py`](21-prd-driven-project.py) | 2 | 0 | [link](https://books.vizuara.ai/read/modern-software-developer/prd-driven-project) |
| 22 | The Risks of Vibe Coding | [`22-why-secure-vibe-coding.py`](22-why-secure-vibe-coding.py) | 1 | 0 | [link](https://books.vizuara.ai/read/modern-software-developer/why-secure-vibe-coding) |
| 23 | Classes of Software Vulnerabilities | [`23-classes-of-vulnerabilities.py`](23-classes-of-vulnerabilities.py) | 3 | 0 | [link](https://books.vizuara.ai/read/modern-software-developer/classes-of-vulnerabilities) |
| 24 | Static & Dependency Scanning | [`24-static-and-dependency-scans.py`](24-static-and-dependency-scans.py) | 2 | 0 | [link](https://books.vizuara.ai/read/modern-software-developer/static-and-dependency-scans) |
| 25 | AI-Assisted Manual Code Review | [`25-manual-code-review-with-agents.py`](25-manual-code-review-with-agents.py) | 1 | 0 | [link](https://books.vizuara.ai/read/modern-software-developer/manual-code-review-with-agents) |
| 26 | Security Hardening: From v1 to v2 | [`26-security-hardening-v1-to-v2.py`](26-security-hardening-v1-to-v2.py) | 3 | 0 | [link](https://books.vizuara.ai/read/modern-software-developer/security-hardening-v1-to-v2) |
| 27 | The Testing Pyramid | [`27-the-testing-pyramid.py`](27-the-testing-pyramid.py) | 4 | 0 | [link](https://books.vizuara.ai/read/modern-software-developer/the-testing-pyramid) |
| 30 | End-to-End Testing with Playwright | [`30-end-to-end-testing-with-playwright.py`](30-end-to-end-testing-with-playwright.py) | 2 | 0 | [link](https://books.vizuara.ai/read/modern-software-developer/end-to-end-testing-with-playwright) |
| 34 | The Full Pipeline, End to End | [`34-the-full-pipeline-recap.py`](34-the-full-pipeline-recap.py) | 2 | 0 | [link](https://books.vizuara.ai/read/modern-software-developer/the-full-pipeline-recap) |

## Notes

- Each file concatenates that chapter's Python blocks in document order, separated by `# --- block N ---` markers.
- Non-Python blocks (shell commands, sample output, JSON, plain text) are not included.
- Blocks are teaching excerpts. Many assume variables or imports introduced earlier in the chapter or in an earlier chapter, so an individual file is not guaranteed to run standalone.
- The only code the generator writes itself is the `# --- imports (added by the generator) ---` block: a canonical import line for a well-known alias (`np`, `torch`, `nn`, ...) that the chapter uses as a module but never imports and never assigns. Nothing else is added, and no book code is rewritten.
- A block tagged `python` in the book that will not compile - prose, pseudo-code, or a fragment shown out of context - is kept verbatim but commented out, labelled `# --- block N (DOES NOT COMPILE - COMMENTED OUT) ---`.

# SQL Masterclass - companion code

Runnable code extracted from every chapter of [SQL Masterclass](https://books.vizuara.ai/read/sql-masterclass), in reading order.

These files are **generated** from the book text by `tools/build_companion_repo.py`. Do not hand-edit them.

6 of 36 chapters contain Python code (22 code blocks total).

| # | Chapter | File | Blocks | Added imports | Read online |
|---|---------|------|--------|---------------|-------------|
| 2 | What Is SQL? Declarative Queries vs Imperative Code | [`02-what-is-sql.py`](02-what-is-sql.py) | 1 | 0 | [link](https://books.vizuara.ai/read/sql-masterclass/what-is-sql) |
| 27 | Connecting Python to PostgreSQL with psycopg2 | [`27-connect-python-psycopg2.py`](27-connect-python-psycopg2.py) | 4 | 0 | [link](https://books.vizuara.ai/read/sql-masterclass/connect-python-psycopg2) |
| 28 | From Query to DataFrame: Analyzing in Pandas | [`28-python-query-to-dataframe.py`](28-python-query-to-dataframe.py) | 6 | 0 | [link](https://books.vizuara.ai/read/sql-masterclass/python-query-to-dataframe) |
| 29 | Visualizing SQL Data in Python | [`29-python-data-visualization.py`](29-python-data-visualization.py) | 5 | 0 | [link](https://books.vizuara.ai/read/sql-masterclass/python-data-visualization) |
| 33 | Capstone: CRUD Operations from Python | [`33-capstone-crud-with-python.py`](33-capstone-crud-with-python.py) | 5 | 0 | [link](https://books.vizuara.ai/read/sql-masterclass/capstone-crud-with-python) |
| 36 | Putting It All Together | [`36-putting-it-all-together.py`](36-putting-it-all-together.py) | 1 | 0 | [link](https://books.vizuara.ai/read/sql-masterclass/putting-it-all-together) |

## Notes

- Each file concatenates that chapter's Python blocks in document order, separated by `# --- block N ---` markers.
- Non-Python blocks (shell commands, sample output, JSON, plain text) are not included.
- Blocks are teaching excerpts. Many assume variables or imports introduced earlier in the chapter or in an earlier chapter, so an individual file is not guaranteed to run standalone.
- The only code the generator writes itself is the `# --- imports (added by the generator) ---` block: a canonical import line for a well-known alias (`np`, `torch`, `nn`, ...) that the chapter uses as a module but never imports and never assigns. Nothing else is added, and no book code is rewritten.
- A block tagged `python` in the book that will not compile - prose, pseudo-code, or a fragment shown out of context - is kept verbatim but commented out, labelled `# --- block N (DOES NOT COMPILE - COMMENTED OUT) ---`.

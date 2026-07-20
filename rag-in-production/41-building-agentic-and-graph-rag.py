"""
RAG in Production
Chapter 41: Building Agentic and Graph RAG
Section: Agentic & Graph RAG

Read this chapter: https://books.vizuara.ai/read/rag-in-production/building-agentic-and-graph-rag

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# `cosine` is defined in chapter 17 (Similarity Metrics: Cosine, Dot, Euclidean).
from context import cosine

# --- stubs (not in the book; the reader supplies these) ---
# https://books.vizuara.ai/read/rag-in-production/building-agentic-and-graph-rag
embed = None         # TODO: your embedding function - see chapters 15-16
INDEX = None         # TODO: list of (chunk, chunk_vector) pairs - see chapter 20
llm_plan = None      # TODO: LLM call returning .enough and .next_query
llm_generate = None  # TODO: your grounded LLM call - see chapter 23
TRIPLES = None       # TODO: (subject, relation, object) triples - see chapter 40

# --- block 1 ---
def retrieve(query, top_k=2):
    """Embed the query, return the top_k nearest chunks by cosine similarity."""
    qv = embed(query)                          # same embedding model as the index
    scored = [(cosine(qv, cv), c) for c, cv in INDEX]
    scored.sort(reverse=True)
    return [c for _, c in scored[:top_k]]

def agentic_answer(question, max_hops=4):
    evidence, query = [], question
    for hop in range(max_hops):
        evidence += retrieve(query, top_k=2)         # 1. act: hit the index
        decision = llm_plan(question, evidence)      # 2. reason: enough? if not, what next?
        if decision.enough:
            return llm_generate(question, evidence)  # 3. answer, grounded
        query = decision.next_query                  # the query WRITTEN from the last result
    return llm_generate(question, evidence)          # give up gracefully at the cap

# --- block 2 ---
import networkx as nx
G = nx.MultiDiGraph()
for subj, rel, obj in TRIPLES:
    G.add_edge(subj, obj, relation=rel)     # nodes auto-created; edge carries the relation

# --- block 3 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# projects = [obj for _, obj, d in G.out_edges("Priya Rao", data=True)
#             if d["relation"] in ("LEADS", "MENTORS")]
# # → ["Helios", "Nova"]   →  count = 2
# leaders  = [subj for subj, obj, d in G.in_edges(...) ...]  # who else LEADS a project she touches
# # Nova has an in-edge (Sam Okafor, LEADS, Nova)  → "Sam Okafor"

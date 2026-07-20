"""
RAG in Production
Chapter 40: Graph RAG: Knowledge as a Graph
Section: Agentic & Graph RAG

Read this chapter: https://books.vizuara.ai/read/rag-in-production/graph-rag-knowledge-as-a-graph

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# graph: entity -> list of (relation, neighbour, source_chunk)
def retrieve_subgraph(graph, start, hops=2):
    seen, frontier, context = {start}, [start], []
    for _ in range(hops):
        next_frontier = []
        for node in frontier:
            for relation, neighbour, chunk in graph.get(node, []):
                context.append(f"{node} --{relation}--> {neighbour}")
                context.append(chunk)                 # keep the source text too
                if neighbour not in seen:
                    seen.add(neighbour)
                    next_frontier.append(neighbour)
        frontier = next_frontier
    return context

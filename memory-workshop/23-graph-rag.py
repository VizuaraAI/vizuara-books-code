"""
Memory in AI Systems
Chapter 23: Graph RAG: Memory with Relationships
Section: Retrieval and Knowledge

Read this chapter: https://books.vizuara.ai/read/memory-workshop/graph-rag

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from collections import defaultdict

class GraphMemory:
    def __init__(self):
        # node -> list of (relation, neighbor)
        self.edges = defaultdict(list)

    def add(self, subject, relation, obj):
        self.edges[subject].append((relation, obj))   # directed edge
        self.edges[obj].append((f"inverse_{relation}", subject))  # walk both ways

    def neighbors(self, node, hops=2):
        """Collect every triple reachable within `hops` of node (BFS)."""
        seen, frontier, facts = {node}, [node], []
        for _ in range(hops):
            nxt = []
            for n in frontier:
                for relation, neighbor in self.edges[n]:
                    if not relation.startswith("inverse_"):
                        facts.append((n, relation, neighbor))
                    if neighbor not in seen:
                        seen.add(neighbor); nxt.append(neighbor)
            frontier = nxt
        return facts

mem = GraphMemory()
mem.add("Aisha", "preparing_for", "NEET")
mem.add("NEET", "contains_topic", "Organic Chemistry")
mem.add("Aisha", "struggles_with", "Organic Chemistry")

print(mem.neighbors("Aisha", hops=2))
# [('Aisha', 'preparing_for', 'NEET'),
#  ('Aisha', 'struggles_with', 'Organic Chemistry'),
#  ('NEET', 'contains_topic', 'Organic Chemistry')]

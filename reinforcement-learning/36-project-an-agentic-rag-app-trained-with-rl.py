"""
Reinforcement Learning
Chapter 36: Project: An Agentic RAG App Trained with RL
Section: Agentic Reinforcement Learning

Read this chapter: https://books.vizuara.ai/read/reinforcement-learning/project-an-agentic-rag-app-trained-with-rl

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def reward(trajectory, gold_answer):
    r  = 1.0 * answer_matches(trajectory.answer, gold_answer)  # did it get it right?
    r += 0.3 * any_retrieved_gold_doc(trajectory)              # did it ever find the right doc?
    r -= 0.05 * trajectory.num_searches                        # penalty per extra search
    return r

# --- block 2 ---
rewards = [reward(t, gold) for t in group]          # e.g. [1.20, 0.90, -0.05, 1.20, ...]
mu, sigma = mean(rewards), std(rewards)
advantages = [(r - mu) / (sigma + 1e-8) for r in rewards]

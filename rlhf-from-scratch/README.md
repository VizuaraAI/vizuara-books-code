# RLHF from Scratch - companion code

Runnable code extracted from every chapter of [RLHF from Scratch](https://books.vizuara.ai/read/rlhf-from-scratch), in reading order.

These files are **generated** from the book text by `tools/build_companion_repo.py`. Do not hand-edit them.

22 of 37 chapters contain Python code (35 code blocks total).

| # | Chapter | File | Blocks | Added imports | Read online |
|---|---------|------|--------|---------------|-------------|
| 1 | What is RLHF and Why It Matters | [`01-what-is-rlhf-and-why-it-matters.py`](01-what-is-rlhf-and-why-it-matters.py) | 1 | 0 | [link](https://books.vizuara.ai/read/rlhf-from-scratch/what-is-rlhf-and-why-it-matters) |
| 4 | Prerequisites and Notation | [`04-prerequisites-and-notation.py`](04-prerequisites-and-notation.py) | 1 | 0 | [link](https://books.vizuara.ai/read/rlhf-from-scratch/prerequisites-and-notation) |
| 5 | The Journey of a Token Through an LLM | [`05-journey-of-a-token-through-an-llm.py`](05-journey-of-a-token-through-an-llm.py) | 4 | 0 | [link](https://books.vizuara.ai/read/rlhf-from-scratch/journey-of-a-token-through-an-llm) |
| 6 | Tokenization and Embeddings Refresher | [`06-tokenization-and-embeddings-refresher.py`](06-tokenization-and-embeddings-refresher.py) | 2 | 0 | [link](https://books.vizuara.ai/read/rlhf-from-scratch/tokenization-and-embeddings-refresher) |
| 8 | States, Actions, and the Policy | [`08-states-actions-and-the-policy.py`](08-states-actions-and-the-policy.py) | 2 | 0 | [link](https://books.vizuara.ai/read/rlhf-from-scratch/states-actions-and-the-policy) |
| 9 | Generation as a Trajectory | [`09-generation-as-a-trajectory.py`](09-generation-as-a-trajectory.py) | 2 | 0 | [link](https://books.vizuara.ai/read/rlhf-from-scratch/generation-as-a-trajectory) |
| 10 | The Problem of Subjective Rewards | [`10-the-problem-of-subjective-rewards.py`](10-the-problem-of-subjective-rewards.py) | 1 | 0 | [link](https://books.vizuara.ai/read/rlhf-from-scratch/the-problem-of-subjective-rewards) |
| 13 | Building a Reward Head on an LLM | [`13-building-a-reward-head-on-an-llm.py`](13-building-a-reward-head-on-an-llm.py) | 3 | 1 | [link](https://books.vizuara.ai/read/rlhf-from-scratch/building-a-reward-head-on-an-llm) |
| 14 | Training the Reward Model | [`14-training-the-reward-model.py`](14-training-the-reward-model.py) | 1 | 0 | [link](https://books.vizuara.ai/read/rlhf-from-scratch/training-the-reward-model) |
| 15 | Evaluating and Trusting the Reward Model | [`15-evaluating-and-trusting-the-reward-model.py`](15-evaluating-and-trusting-the-reward-model.py) | 1 | 0 | [link](https://books.vizuara.ai/read/rlhf-from-scratch/evaluating-and-trusting-the-reward-model) |
| 16 | The Policy Gradient Objective | [`16-the-policy-gradient-objective.py`](16-the-policy-gradient-objective.py) | 4 | 0 | [link](https://books.vizuara.ai/read/rlhf-from-scratch/the-policy-gradient-objective) |
| 17 | REINFORCE and the Log-Derivative Trick | [`17-reinforce-and-the-log-derivative-trick.py`](17-reinforce-and-the-log-derivative-trick.py) | 1 | 0 | [link](https://books.vizuara.ai/read/rlhf-from-scratch/reinforce-and-the-log-derivative-trick) |
| 18 | Baselines and Variance Reduction | [`18-baselines-and-variance-reduction.py`](18-baselines-and-variance-reduction.py) | 1 | 0 | [link](https://books.vizuara.ai/read/rlhf-from-scratch/baselines-and-variance-reduction) |
| 19 | Value Functions and the Advantage | [`19-value-functions-and-the-advantage.py`](19-value-functions-and-the-advantage.py) | 1 | 0 | [link](https://books.vizuara.ai/read/rlhf-from-scratch/value-functions-and-the-advantage) |
| 21 | Computing Advantages Over a Sequence | [`21-computing-advantages-over-a-sequence.py`](21-computing-advantages-over-a-sequence.py) | 1 | 0 | [link](https://books.vizuara.ai/read/rlhf-from-scratch/computing-advantages-over-a-sequence) |
| 24 | The Clipped Surrogate Objective | [`24-the-clipped-surrogate-objective.py`](24-the-clipped-surrogate-objective.py) | 1 | 0 | [link](https://books.vizuara.ai/read/rlhf-from-scratch/the-clipped-surrogate-objective) |
| 26 | The Actor-Critic Value Model | [`26-the-actor-critic-value-model.py`](26-the-actor-critic-value-model.py) | 1 | 1 | [link](https://books.vizuara.ai/read/rlhf-from-scratch/the-actor-critic-value-model) |
| 27 | The Full PPO Training Loop | [`27-the-full-ppo-training-loop.py`](27-the-full-ppo-training-loop.py) | 2 | 2 | [link](https://books.vizuara.ai/read/rlhf-from-scratch/the-full-ppo-training-loop) |
| 29 | Training a Tiny Supervised Language Model | [`29-training-a-tiny-supervised-language-model.py`](29-training-a-tiny-supervised-language-model.py) | 2 | 0 | [link](https://books.vizuara.ai/read/rlhf-from-scratch/training-a-tiny-supervised-language-model) |
| 30 | Aligning the SLM with a Reward Signal | [`30-aligning-the-slm-with-a-reward-signal.py`](30-aligning-the-slm-with-a-reward-signal.py) | 1 | 0 | [link](https://books.vizuara.ai/read/rlhf-from-scratch/aligning-the-slm-with-a-reward-signal) |
| 32 | Training the Summarizer's Reward Model | [`32-training-the-summarizer-reward-model.py`](32-training-the-summarizer-reward-model.py) | 1 | 0 | [link](https://books.vizuara.ai/read/rlhf-from-scratch/training-the-summarizer-reward-model) |
| 37 | Putting It All Together | [`37-putting-it-all-together.py`](37-putting-it-all-together.py) | 1 | 1 | [link](https://books.vizuara.ai/read/rlhf-from-scratch/putting-it-all-together) |

## Notes

- Each file concatenates that chapter's Python blocks in document order, separated by `# --- block N ---` markers.
- Non-Python blocks (shell commands, sample output, JSON, plain text) are not included.
- Blocks are teaching excerpts. Many assume variables or imports introduced earlier in the chapter or in an earlier chapter, so an individual file is not guaranteed to run standalone.
- The only code the generator writes itself is the `# --- imports (added by the generator) ---` block: a canonical import line for a well-known alias (`np`, `torch`, `nn`, ...) that the chapter uses as a module but never imports and never assigns. Nothing else is added, and no book code is rewritten.
- A block tagged `python` in the book that will not compile - prose, pseudo-code, or a fragment shown out of context - is kept verbatim but commented out, labelled `# --- block N (DOES NOT COMPILE - COMMENTED OUT) ---`.

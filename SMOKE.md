# Smoke report

Recomputed from scratch over the files currently in this repo. Two checks, both static:

1. **`python -m py_compile <file>`** - a syntax check. Does the file parse as
   valid Python? Nothing is imported, nothing is executed.
2. **`python -m pyflakes <file>`** - a static check. Undefined names, unused
   imports, shadowed definitions. A file is counted clean only if pyflakes emits
   zero output.

**No file in this repo has ever been run.** The code needs GPUs, datasets and API keys. Compiling is not running, and a 100% compile rate says nothing about whether the code works.

Failures below are real and none have been dropped.

## Aggregate

- Books: **39**
- Python files: **1015**
- Notebooks generated: **1015** (one per Python file, all valid nbformat 4)
- Code blocks: **2309**
- `py_compile` pass: **1015 / 1015 (100.0%)**
- pyflakes-clean: **692 / 1015 (68.2%)**

## Per book

| Book | Files | py_compile pass | pyflakes-clean | Clean rate |
|------|------:|----------------:|---------------:|-----------:|
| `5d-parallelism` | 20 | 20 | 5 | 25.0% |
| `ai-agents-bootcamp` | 35 | 35 | 33 | 94.3% |
| `ai-context-engineering` | 25 | 25 | 10 | 40.0% |
| `build-llm-from-scratch` | 20 | 20 | 18 | 90.0% |
| `claude-certified-architect` | 24 | 24 | 6 | 25.0% |
| `cnn-fundamentals` | 24 | 24 | 17 | 70.8% |
| `computer-vision-bootcamp` | 29 | 29 | 20 | 69.0% |
| `decision-trees-from-scratch` | 17 | 17 | 12 | 70.6% |
| `deep-learning-fundamentals` | 36 | 36 | 34 | 94.4% |
| `deit-from-scratch` | 31 | 31 | 10 | 32.3% |
| `diffusion-lm-from-scratch` | 21 | 21 | 4 | 19.0% |
| `dsa-in-python` | 69 | 69 | 62 | 89.9% |
| `foundations-for-ai-ml` | 28 | 28 | 28 | 100.0% |
| `generative-ai-fundamentals` | 30 | 30 | 9 | 30.0% |
| `harness-engineering` | 29 | 29 | 24 | 82.8% |
| `kernel-engineering` | 15 | 15 | 3 | 20.0% |
| `llm-finetuning` | 25 | 25 | 12 | 48.0% |
| `llm-production-deployment` | 34 | 34 | 32 | 94.1% |
| `machine-learning-fundamentals` | 23 | 23 | 13 | 56.5% |
| `math-foundations-for-ml` | 27 | 27 | 27 | 100.0% |
| `memory-workshop` | 34 | 34 | 32 | 94.1% |
| `mini-clawdbot-from-scratch` | 8 | 8 | 3 | 37.5% |
| `ml-dl-mastery` | 35 | 35 | 35 | 100.0% |
| `modern-robot-learning` | 26 | 26 | 10 | 38.5% |
| `modern-software-developer` | 19 | 19 | 9 | 47.4% |
| `nanovlm-from-scratch` | 33 | 33 | 28 | 84.8% |
| `neural-networks-from-scratch` | 29 | 29 | 28 | 96.6% |
| `nlp-cv-mastery` | 34 | 34 | 34 | 100.0% |
| `prompt-engineering` | 4 | 4 | 4 | 100.0% |
| `python-for-data-science` | 37 | 37 | 34 | 91.9% |
| `rag-in-production` | 30 | 30 | 29 | 96.7% |
| `reinforcement-learning` | 31 | 31 | 6 | 19.4% |
| `rlhf-from-scratch` | 22 | 22 | 12 | 54.5% |
| `sql-masterclass` | 6 | 6 | 2 | 33.3% |
| `transformers-for-vision-multimodal` | 29 | 29 | 12 | 41.4% |
| `transformers-from-scratch` | 15 | 15 | 11 | 73.3% |
| `vit-from-scratch` | 24 | 24 | 4 | 16.7% |
| `vla-world-models-robotics` | 34 | 34 | 18 | 52.9% |
| `writing-research-papers` | 3 | 3 | 2 | 66.7% |
| **Total** | **1015** | **1015** | **692** | **68.2%** |

## Files that do not compile (0)

None. All 1015 files pass `py_compile`.

This is not luck and it is not a quality signal. Blocks that would not compile were deliberately commented out at extraction time rather than guessed at - every one of them is listed under Authoring bugs below.

## pyflakes warnings (323 files, 1742 warnings)

| Warning | Count | What it means here |
|---------|------:|--------------------|
| `undefined name 'X'` | 1659 | Expected. The excerpt continues from an earlier block or chapter, or the book asks you to supply the name. |
| `redefinition of unused 'X' from line N` | 46 | The book redefines a name to show a second version of it. Normal in a chapter that iterates on one function. |
| `'X' imported but unused` | 30 | The chapter imports something it uses in prose or in a later chapter. |
| `local variable 'X' is assigned to but never used` | 5 | A teaching variable shown for illustration. |
| `f-string is missing placeholders` | 1 | An f-string with no interpolation. Harmless. |
| `local variable 'X' defined in enclosing scope on line N referenced before assignment` | 1 | See the file. |

`undefined name` dominates and is inherent to the format: these are excerpts in reading order, not standalone modules. It is reported, not suppressed.

## Authoring bugs in the books

**117 blocks** across **27 books** are tagged `python` in the book but are not compilable Python - they are prose, pseudo-code, or a fragment shown out of context (a bare `return`, an indented continuation with no head). The extractor kept each one verbatim and commented it out. None was repaired into plausible code.

These are source-side bugs. Fixing them means retagging the block in the book (to `text`, `bash`, or whatever it actually is) or completing the snippet. The list below is the fix queue.

### `nanovlm-from-scratch` - 23 block(s)

| File | Block | Chapter | Read |
|------|------:|---------|------|
| `05-the-landscape-clip-and-friends.py` | 1 | Chapter 5: The Landscape: CLIP and Friends | [link](https://books.vizuara.ai/read/nanovlm-from-scratch/the-landscape-clip-and-friends) |
| `06-what-we-will-build-nanovlm-blueprint.py` | 1 | Chapter 6: What We Will Build: The NanoVLM Blueprint | [link](https://books.vizuara.ai/read/nanovlm-from-scratch/what-we-will-build-nanovlm-blueprint) |
| `10-cosine-similarity-explained.py` | 1 | Chapter 10: Cosine Similarity, Explained | [link](https://books.vizuara.ai/read/nanovlm-from-scratch/cosine-similarity-explained) |
| `10-cosine-similarity-explained.py` | 2 | Chapter 10: Cosine Similarity, Explained | [link](https://books.vizuara.ai/read/nanovlm-from-scratch/cosine-similarity-explained) |
| `10-cosine-similarity-explained.py` | 3 | Chapter 10: Cosine Similarity, Explained | [link](https://books.vizuara.ai/read/nanovlm-from-scratch/cosine-similarity-explained) |
| `10-cosine-similarity-explained.py` | 4 | Chapter 10: Cosine Similarity, Explained | [link](https://books.vizuara.ai/read/nanovlm-from-scratch/cosine-similarity-explained) |
| `10-cosine-similarity-explained.py` | 5 | Chapter 10: Cosine Similarity, Explained | [link](https://books.vizuara.ai/read/nanovlm-from-scratch/cosine-similarity-explained) |
| `10-cosine-similarity-explained.py` | 6 | Chapter 10: Cosine Similarity, Explained | [link](https://books.vizuara.ai/read/nanovlm-from-scratch/cosine-similarity-explained) |
| `10-cosine-similarity-explained.py` | 7 | Chapter 10: Cosine Similarity, Explained | [link](https://books.vizuara.ai/read/nanovlm-from-scratch/cosine-similarity-explained) |
| `10-cosine-similarity-explained.py` | 8 | Chapter 10: Cosine Similarity, Explained | [link](https://books.vizuara.ai/read/nanovlm-from-scratch/cosine-similarity-explained) |
| `11-dot-products-norms-and-normalization.py` | 1 | Chapter 11: Dot Products, Norms, and Normalization | [link](https://books.vizuara.ai/read/nanovlm-from-scratch/dot-products-norms-and-normalization) |
| `11-dot-products-norms-and-normalization.py` | 2 | Chapter 11: Dot Products, Norms, and Normalization | [link](https://books.vizuara.ai/read/nanovlm-from-scratch/dot-products-norms-and-normalization) |
| `11-dot-products-norms-and-normalization.py` | 3 | Chapter 11: Dot Products, Norms, and Normalization | [link](https://books.vizuara.ai/read/nanovlm-from-scratch/dot-products-norms-and-normalization) |
| `22-the-clip-contrastive-loss.py` | 2 | Chapter 22: The CLIP Contrastive Loss | [link](https://books.vizuara.ai/read/nanovlm-from-scratch/the-clip-contrastive-loss) |
| `22-the-clip-contrastive-loss.py` | 3 | Chapter 22: The CLIP Contrastive Loss | [link](https://books.vizuara.ai/read/nanovlm-from-scratch/the-clip-contrastive-loss) |
| `22-the-clip-contrastive-loss.py` | 5 | Chapter 22: The CLIP Contrastive Loss | [link](https://books.vizuara.ai/read/nanovlm-from-scratch/the-clip-contrastive-loss) |
| `22-the-clip-contrastive-loss.py` | 8 | Chapter 22: The CLIP Contrastive Loss | [link](https://books.vizuara.ai/read/nanovlm-from-scratch/the-clip-contrastive-loss) |
| `22-the-clip-contrastive-loss.py` | 9 | Chapter 22: The CLIP Contrastive Loss | [link](https://books.vizuara.ai/read/nanovlm-from-scratch/the-clip-contrastive-loss) |
| `23-temperature-and-logit-scaling.py` | 2 | Chapter 23: Temperature and Logit Scaling | [link](https://books.vizuara.ai/read/nanovlm-from-scratch/temperature-and-logit-scaling) |
| `23-temperature-and-logit-scaling.py` | 3 | Chapter 23: Temperature and Logit Scaling | [link](https://books.vizuara.ai/read/nanovlm-from-scratch/temperature-and-logit-scaling) |
| `23-temperature-and-logit-scaling.py` | 4 | Chapter 23: Temperature and Logit Scaling | [link](https://books.vizuara.ai/read/nanovlm-from-scratch/temperature-and-logit-scaling) |
| `27-the-text-encoder-module.py` | 4 | Chapter 27: The Text Encoder Module | [link](https://books.vizuara.ai/read/nanovlm-from-scratch/the-text-encoder-module) |
| `29-synthetic-data-for-training.py` | 3 | Chapter 29: Synthetic Data for Training | [link](https://books.vizuara.ai/read/nanovlm-from-scratch/synthetic-data-for-training) |

### `math-foundations-for-ml` - 13 block(s)

| File | Block | Chapter | Read |
|------|------:|---------|------|
| `22-bernoulli-and-binomial.py` | 1 | Chapter 22: Bernoulli and Binomial Distributions | [link](https://books.vizuara.ai/read/math-foundations-for-ml/bernoulli-and-binomial) |
| `22-bernoulli-and-binomial.py` | 2 | Chapter 22: Bernoulli and Binomial Distributions | [link](https://books.vizuara.ai/read/math-foundations-for-ml/bernoulli-and-binomial) |
| `22-bernoulli-and-binomial.py` | 3 | Chapter 22: Bernoulli and Binomial Distributions | [link](https://books.vizuara.ai/read/math-foundations-for-ml/bernoulli-and-binomial) |
| `22-bernoulli-and-binomial.py` | 4 | Chapter 22: Bernoulli and Binomial Distributions | [link](https://books.vizuara.ai/read/math-foundations-for-ml/bernoulli-and-binomial) |
| `23-the-normal-distribution.py` | 1 | Chapter 23: The Normal Distribution | [link](https://books.vizuara.ai/read/math-foundations-for-ml/the-normal-distribution) |
| `25-from-likelihood-to-loss-functions.py` | 1 | Chapter 25: From Likelihood to Loss Functions | [link](https://books.vizuara.ai/read/math-foundations-for-ml/from-likelihood-to-loss-functions) |
| `25-from-likelihood-to-loss-functions.py` | 2 | Chapter 25: From Likelihood to Loss Functions | [link](https://books.vizuara.ai/read/math-foundations-for-ml/from-likelihood-to-loss-functions) |
| `25-from-likelihood-to-loss-functions.py` | 3 | Chapter 25: From Likelihood to Loss Functions | [link](https://books.vizuara.ai/read/math-foundations-for-ml/from-likelihood-to-loss-functions) |
| `25-from-likelihood-to-loss-functions.py` | 4 | Chapter 25: From Likelihood to Loss Functions | [link](https://books.vizuara.ai/read/math-foundations-for-ml/from-likelihood-to-loss-functions) |
| `25-from-likelihood-to-loss-functions.py` | 5 | Chapter 25: From Likelihood to Loss Functions | [link](https://books.vizuara.ai/read/math-foundations-for-ml/from-likelihood-to-loss-functions) |
| `25-from-likelihood-to-loss-functions.py` | 6 | Chapter 25: From Likelihood to Loss Functions | [link](https://books.vizuara.ai/read/math-foundations-for-ml/from-likelihood-to-loss-functions) |
| `25-from-likelihood-to-loss-functions.py` | 7 | Chapter 25: From Likelihood to Loss Functions | [link](https://books.vizuara.ai/read/math-foundations-for-ml/from-likelihood-to-loss-functions) |
| `25-from-likelihood-to-loss-functions.py` | 8 | Chapter 25: From Likelihood to Loss Functions | [link](https://books.vizuara.ai/read/math-foundations-for-ml/from-likelihood-to-loss-functions) |

### `nlp-cv-mastery` - 8 block(s)

| File | Block | Chapter | Read |
|------|------:|---------|------|
| `07-weights-biases-and-loss.py` | 1 | Chapter 7: Weights, Biases, and the Loss Surface | [link](https://books.vizuara.ai/read/nlp-cv-mastery/weights-biases-and-loss) |
| `13-l1-and-l2-regularization.py` | 1 | Chapter 13: L1 and L2 Regularization | [link](https://books.vizuara.ai/read/nlp-cv-mastery/l1-and-l2-regularization) |
| `20-resnet-and-skip-connections.py` | 1 | Chapter 20: ResNet and Skip Connections | [link](https://books.vizuara.ai/read/nlp-cv-mastery/resnet-and-skip-connections) |
| `20-resnet-and-skip-connections.py` | 2 | Chapter 20: ResNet and Skip Connections | [link](https://books.vizuara.ai/read/nlp-cv-mastery/resnet-and-skip-connections) |
| `22-history-of-cnns.py` | 1 | Chapter 22: A History of CNNs | [link](https://books.vizuara.ai/read/nlp-cv-mastery/history-of-cnns) |
| `33-dice-iou-and-training-unet.py` | 1 | Chapter 33: DICE, IoU, and Training U-Net | [link](https://books.vizuara.ai/read/nlp-cv-mastery/dice-iou-and-training-unet) |
| `33-dice-iou-and-training-unet.py` | 2 | Chapter 33: DICE, IoU, and Training U-Net | [link](https://books.vizuara.ai/read/nlp-cv-mastery/dice-iou-and-training-unet) |
| `34-yolo-you-only-look-once.py` | 1 | Chapter 34: YOLO: You Only Look Once | [link](https://books.vizuara.ai/read/nlp-cv-mastery/yolo-you-only-look-once) |

### `reinforcement-learning` - 7 block(s)

| File | Block | Chapter | Read |
|------|------:|---------|------|
| `21-advantage-functions-and-actor-critic.py` | 2 | Chapter 21: Advantage Functions and Actor-Critic | [link](https://books.vizuara.ai/read/reinforcement-learning/advantage-functions-and-actor-critic) |
| `23-why-language-models-need-alignment.py` | 2 | Chapter 23: Why Language Models Need Alignment | [link](https://books.vizuara.ai/read/reinforcement-learning/why-language-models-need-alignment) |
| `24-the-three-stage-rlhf-pipeline.py` | 1 | Chapter 24: The Three-Stage RLHF Pipeline | [link](https://books.vizuara.ai/read/reinforcement-learning/the-three-stage-rlhf-pipeline) |
| `24-the-three-stage-rlhf-pipeline.py` | 3 | Chapter 24: The Three-Stage RLHF Pipeline | [link](https://books.vizuara.ai/read/reinforcement-learning/the-three-stage-rlhf-pipeline) |
| `27-the-ppo-algorithm-explained.py` | 3 | Chapter 27: The PPO Algorithm Explained | [link](https://books.vizuara.ai/read/reinforcement-learning/the-ppo-algorithm-explained) |
| `30-from-ppo-to-grpo.py` | 2 | Chapter 30: From PPO to GRPO | [link](https://books.vizuara.ai/read/reinforcement-learning/from-ppo-to-grpo) |
| `31-how-grpo-works.py` | 3 | Chapter 31: How GRPO Works | [link](https://books.vizuara.ai/read/reinforcement-learning/how-grpo-works) |

### `rlhf-from-scratch` - 7 block(s)

| File | Block | Chapter | Read |
|------|------:|---------|------|
| `05-journey-of-a-token-through-an-llm.py` | 4 | Chapter 5: The Journey of a Token Through an LLM | [link](https://books.vizuara.ai/read/rlhf-from-scratch/journey-of-a-token-through-an-llm) |
| `09-generation-as-a-trajectory.py` | 1 | Chapter 9: Generation as a Trajectory | [link](https://books.vizuara.ai/read/rlhf-from-scratch/generation-as-a-trajectory) |
| `09-generation-as-a-trajectory.py` | 2 | Chapter 9: Generation as a Trajectory | [link](https://books.vizuara.ai/read/rlhf-from-scratch/generation-as-a-trajectory) |
| `16-the-policy-gradient-objective.py` | 1 | Chapter 16: The Policy Gradient Objective | [link](https://books.vizuara.ai/read/rlhf-from-scratch/the-policy-gradient-objective) |
| `16-the-policy-gradient-objective.py` | 2 | Chapter 16: The Policy Gradient Objective | [link](https://books.vizuara.ai/read/rlhf-from-scratch/the-policy-gradient-objective) |
| `16-the-policy-gradient-objective.py` | 3 | Chapter 16: The Policy Gradient Objective | [link](https://books.vizuara.ai/read/rlhf-from-scratch/the-policy-gradient-objective) |
| `16-the-policy-gradient-objective.py` | 4 | Chapter 16: The Policy Gradient Objective | [link](https://books.vizuara.ai/read/rlhf-from-scratch/the-policy-gradient-objective) |

### `ai-agents-bootcamp` - 6 block(s)

| File | Block | Chapter | Read |
|------|------:|---------|------|
| `05-setup-keys-and-environment.py` | 2 | Chapter 5: Setup: API Keys and Your Environment | [link](https://books.vizuara.ai/read/ai-agents-bootcamp/setup-keys-and-environment) |
| `18-langchain-tools-and-memory.py` | 2 | Chapter 18: LangChain Agents: Tools and Memory | [link](https://books.vizuara.ai/read/ai-agents-bootcamp/langchain-tools-and-memory) |
| `18-langchain-tools-and-memory.py` | 4 | Chapter 18: LangChain Agents: Tools and Memory | [link](https://books.vizuara.ai/read/ai-agents-bootcamp/langchain-tools-and-memory) |
| `18-langchain-tools-and-memory.py` | 5 | Chapter 18: LangChain Agents: Tools and Memory | [link](https://books.vizuara.ai/read/ai-agents-bootcamp/langchain-tools-and-memory) |
| `33-stateful-workflows-with-langgraph.py` | 1 | Chapter 33: LangGraph: Agents as State Machines | [link](https://books.vizuara.ai/read/ai-agents-bootcamp/stateful-workflows-with-langgraph) |
| `40-build-with-google-adk.py` | 5 | Chapter 40: Building an Agent with Google ADK | [link](https://books.vizuara.ai/read/ai-agents-bootcamp/build-with-google-adk) |

### `dsa-in-python` - 6 block(s)

| File | Block | Chapter | Read |
|------|------:|---------|------|
| `02-python-setup-repl-and-interpreter.py` | 2 | Chapter 2: Setting Up Python: Interpreter & REPL | [link](https://books.vizuara.ai/read/dsa-in-python/python-setup-repl-and-interpreter) |
| `02-python-setup-repl-and-interpreter.py` | 3 | Chapter 2: Setting Up Python: Interpreter & REPL | [link](https://books.vizuara.ai/read/dsa-in-python/python-setup-repl-and-interpreter) |
| `02-python-setup-repl-and-interpreter.py` | 4 | Chapter 2: Setting Up Python: Interpreter & REPL | [link](https://books.vizuara.ai/read/dsa-in-python/python-setup-repl-and-interpreter) |
| `02-python-setup-repl-and-interpreter.py` | 5 | Chapter 2: Setting Up Python: Interpreter & REPL | [link](https://books.vizuara.ai/read/dsa-in-python/python-setup-repl-and-interpreter) |
| `08-introduction-to-python-arrays.py` | 1 | Chapter 8: Introduction to Python Arrays | [link](https://books.vizuara.ai/read/dsa-in-python/introduction-to-python-arrays) |
| `35-introduction-to-bit-manipulation.py` | 1 | Chapter 35: Introduction to Bit Manipulation | [link](https://books.vizuara.ai/read/dsa-in-python/introduction-to-bit-manipulation) |

### `claude-certified-architect` - 5 block(s)

| File | Block | Chapter | Read |
|------|------:|---------|------|
| `10-structured-output-with-tool-use.py` | 3 | Chapter 10: Guaranteed JSON With tool_use | [link](https://books.vizuara.ai/read/claude-certified-architect/structured-output-with-tool-use) |
| `14-validation-retry-loops.py` | 1 | Chapter 14: Validation-Retry Loops With Error Feedback | [link](https://books.vizuara.ai/read/claude-certified-architect/validation-retry-loops) |
| `25-error-propagation-partial-results.py` | 1 | Chapter 25: Error Propagation and Partial Results | [link](https://books.vizuara.ai/read/claude-certified-architect/error-propagation-partial-results) |
| `25-error-propagation-partial-results.py` | 2 | Chapter 25: Error Propagation and Partial Results | [link](https://books.vizuara.ai/read/claude-certified-architect/error-propagation-partial-results) |
| `26-lab-multi-agent-research-pipeline.py` | 2 | Chapter 26: Lab: Multi-Agent Research Pipeline | [link](https://books.vizuara.ai/read/claude-certified-architect/lab-multi-agent-research-pipeline) |

### `deit-from-scratch` - 5 block(s)

| File | Block | Chapter | Read |
|------|------:|---------|------|
| `03-what-makes-deit-data-efficient.py` | 1 | Chapter 3: What Makes DeiT Data-Efficient | [link](https://books.vizuara.ai/read/deit-from-scratch/what-makes-deit-data-efficient) |
| `23-soft-labels-and-temperature.py` | 1 | Chapter 23: Soft Labels and Temperature | [link](https://books.vizuara.ai/read/deit-from-scratch/soft-labels-and-temperature) |
| `23-soft-labels-and-temperature.py` | 3 | Chapter 23: Soft Labels and Temperature | [link](https://books.vizuara.ai/read/deit-from-scratch/soft-labels-and-temperature) |
| `23-soft-labels-and-temperature.py` | 4 | Chapter 23: Soft Labels and Temperature | [link](https://books.vizuara.ai/read/deit-from-scratch/soft-labels-and-temperature) |
| `23-soft-labels-and-temperature.py` | 5 | Chapter 23: Soft Labels and Temperature | [link](https://books.vizuara.ai/read/deit-from-scratch/soft-labels-and-temperature) |

### `neural-networks-from-scratch` - 5 block(s)

| File | Block | Chapter | Read |
|------|------:|---------|------|
| `14-the-backward-pass-intuition.py` | 2 | Chapter 14: The Backward Pass: The Intuition | [link](https://books.vizuara.ai/read/neural-networks-from-scratch/the-backward-pass-intuition) |
| `14-the-backward-pass-intuition.py` | 3 | Chapter 14: The Backward Pass: The Intuition | [link](https://books.vizuara.ai/read/neural-networks-from-scratch/the-backward-pass-intuition) |
| `24-layers-backward-pass.py` | 3 | Chapter 24: Coding the Layer Backward Pass | [link](https://books.vizuara.ai/read/neural-networks-from-scratch/layers-backward-pass) |
| `24-layers-backward-pass.py` | 5 | Chapter 24: Coding the Layer Backward Pass | [link](https://books.vizuara.ai/read/neural-networks-from-scratch/layers-backward-pass) |
| `25-activation-function-intro.py` | 1 | Chapter 25: Adding Activation Functions | [link](https://books.vizuara.ai/read/neural-networks-from-scratch/activation-function-intro) |

### `python-for-data-science` - 4 block(s)

| File | Block | Chapter | Read |
|------|------:|---------|------|
| `02-setting-up-your-environment.py` | 2 | Chapter 2: Setting Up Your Environment | [link](https://books.vizuara.ai/read/python-for-data-science/setting-up-your-environment) |
| `03-your-first-python-program.py` | 5 | Chapter 3: Your First Python Program | [link](https://books.vizuara.ai/read/python-for-data-science/your-first-python-program) |
| `30-debugging-and-extending-the-project.py` | 2 | Chapter 30: Debugging and Extending the Project | [link](https://books.vizuara.ai/read/python-for-data-science/debugging-and-extending-the-project) |
| `30-debugging-and-extending-the-project.py` | 6 | Chapter 30: Debugging and Extending the Project | [link](https://books.vizuara.ai/read/python-for-data-science/debugging-and-extending-the-project) |

### `deep-learning-fundamentals` - 3 block(s)

| File | Block | Chapter | Read |
|------|------:|---------|------|
| `17-matrices-in-backpropagation.py` | 1 | Chapter 17: The role of matrices in backpropagation | [link](https://books.vizuara.ai/read/deep-learning-fundamentals/matrices-in-backpropagation) |
| `27-momentum.py` | 1 | Chapter 27: Momentum in training | [link](https://books.vizuara.ai/read/deep-learning-fundamentals/momentum) |
| `31-neural-networks-from-scratch-recap.py` | 1 | Chapter 31: Neural networks from scratch, end to end | [link](https://books.vizuara.ai/read/deep-learning-fundamentals/neural-networks-from-scratch-recap) |

### `ml-dl-mastery` - 3 block(s)

| File | Block | Chapter | Read |
|------|------:|---------|------|
| `05-regression-theory-and-the-line-of-best-fit.py` | 3 | Chapter 5: Regression Theory and the Line of Best Fit | [link](https://books.vizuara.ai/read/ml-dl-mastery/regression-theory-and-the-line-of-best-fit) |
| `05-regression-theory-and-the-line-of-best-fit.py` | 4 | Chapter 5: Regression Theory and the Line of Best Fit | [link](https://books.vizuara.ai/read/ml-dl-mastery/regression-theory-and-the-line-of-best-fit) |
| `15-perceptron-theory-and-code.py` | 2 | Chapter 15: The Perceptron: Theory and Code | [link](https://books.vizuara.ai/read/ml-dl-mastery/perceptron-theory-and-code) |

### `build-llm-from-scratch` - 2 block(s)

| File | Block | Chapter | Read |
|------|------:|---------|------|
| `10-causal-self-attention-coded-from-scratch.py` | 1 | Chapter 10: Causal Self Attention - Coded from scratch | [link](https://books.vizuara.ai/read/build-llm-from-scratch/causal-self-attention-coded-from-scratch) |
| `18-measuring-loss-and-the-pretraining-loop.py` | 1 | Chapter 18: Measuring Loss and Coding the Pretraining Loop | [link](https://books.vizuara.ai/read/build-llm-from-scratch/measuring-loss-and-the-pretraining-loop) |

### `decision-trees-from-scratch` - 2 block(s)

| File | Block | Chapter | Read |
|------|------:|---------|------|
| `09-choosing-the-best-split.py` | 1 | Chapter 9: Choosing the Best Split | [link](https://books.vizuara.ai/read/decision-trees-from-scratch/choosing-the-best-split) |
| `18-regression-trees-multiple-features.py` | 1 | Chapter 18: Regression Trees with Multiple Features | [link](https://books.vizuara.ai/read/decision-trees-from-scratch/regression-trees-multiple-features) |

### `foundations-for-ai-ml` - 2 block(s)

| File | Block | Chapter | Read |
|------|------:|---------|------|
| `27-momentum-based-gradient-descent.py` | 1 | Chapter 27: Momentum-Based Gradient Descent | [link](https://books.vizuara.ai/read/foundations-for-ai-ml/momentum-based-gradient-descent) |
| `28-rmsprop-and-adam.py` | 1 | Chapter 28: RMSprop and Adam | [link](https://books.vizuara.ai/read/foundations-for-ai-ml/rmsprop-and-adam) |

### `generative-ai-fundamentals` - 2 block(s)

| File | Block | Chapter | Read |
|------|------:|---------|------|
| `14-topic-modeling-with-llms.py` | 1 | Chapter 14: Topic Modeling with LLMs | [link](https://books.vizuara.ai/read/generative-ai-fundamentals/topic-modeling-with-llms) |
| `26-designing-reliable-agents.py` | 2 | Chapter 26: Designing Reliable Agents | [link](https://books.vizuara.ai/read/generative-ai-fundamentals/designing-reliable-agents) |

### `llm-production-deployment` - 2 block(s)

| File | Block | Chapter | Read |
|------|------:|---------|------|
| `39-building-a-multi-agent-framework.py` | 1 | Chapter 39: Building a Multi-Agent Framework | [link](https://books.vizuara.ai/read/llm-production-deployment/building-a-multi-agent-framework) |
| `40-orchestrating-agents-with-langgraph.py` | 1 | Chapter 40: Orchestrating Agents with LangGraph | [link](https://books.vizuara.ai/read/llm-production-deployment/orchestrating-agents-with-langgraph) |

### `modern-software-developer` - 2 block(s)

| File | Block | Chapter | Read |
|------|------:|---------|------|
| `04-software-1-8-the-cursor-era.py` | 1 | Chapter 4: Software 1.8: The Cursor Era | [link](https://books.vizuara.ai/read/modern-software-developer/software-1-8-the-cursor-era) |
| `06-anatomy-of-a-coding-agent.py` | 2 | Chapter 6: The Anatomy of a Coding Agent | [link](https://books.vizuara.ai/read/modern-software-developer/anatomy-of-a-coding-agent) |

### `vit-from-scratch` - 2 block(s)

| File | Block | Chapter | Read |
|------|------:|---------|------|
| `25-parameter-initialization.py` | 1 | Chapter 25: Parameter Initialization | [link](https://books.vizuara.ai/read/vit-from-scratch/parameter-initialization) |
| `29-loss-optimizer-training-loop.py` | 1 | Chapter 29: Loss, Optimizer, and the Training Loop | [link](https://books.vizuara.ai/read/vit-from-scratch/loss-optimizer-training-loop) |

### `vla-world-models-robotics` - 2 block(s)

| File | Block | Chapter | Read |
|------|------:|---------|------|
| `25-latent-dynamics-and-imagination.py` | 2 | Chapter 25: Latent Dynamics and Imagination | [link](https://books.vizuara.ai/read/vla-world-models-robotics/latent-dynamics-and-imagination) |
| `40-building-a-coding-agent-as-policy.py` | 1 | Chapter 40: Building a Coding-Agent-as-Policy | [link](https://books.vizuara.ai/read/vla-world-models-robotics/building-a-coding-agent-as-policy) |

### `ai-context-engineering` - 1 block(s)

| File | Block | Chapter | Read |
|------|------:|---------|------|
| `11-instructional-layer-lab.py` | 3 | Chapter 11: Instructional Layer Lab | [link](https://books.vizuara.ai/read/ai-context-engineering/instructional-layer-lab) |

### `cnn-fundamentals` - 1 block(s)

| File | Block | Chapter | Read |
|------|------:|---------|------|
| `02-what-you-will-learn.py` | 1 | Chapter 2: What You Will Learn | [link](https://books.vizuara.ai/read/cnn-fundamentals/what-you-will-learn) |

### `harness-engineering` - 1 block(s)

| File | Block | Chapter | Read |
|------|------:|---------|------|
| `30-human-in-the-loop.py` | 1 | Chapter 30: Human-in-the-loop: plans, approvals, escalation | [link](https://books.vizuara.ai/read/harness-engineering/human-in-the-loop) |

### `memory-workshop` - 1 block(s)

| File | Block | Chapter | Read |
|------|------:|---------|------|
| `24-agentic-graph-rag.py` | 1 | Chapter 24: Agentic Graph RAG | [link](https://books.vizuara.ai/read/memory-workshop/agentic-graph-rag) |

### `mini-clawdbot-from-scratch` - 1 block(s)

| File | Block | Chapter | Read |
|------|------:|---------|------|
| `02-why-build-your-own-agent.py` | 1 | Chapter 2: Why Build Your Own Agent? | [link](https://books.vizuara.ai/read/mini-clawdbot-from-scratch/why-build-your-own-agent) |

### `rag-in-production` - 1 block(s)

| File | Block | Chapter | Read |
|------|------:|---------|------|
| `41-building-agentic-and-graph-rag.py` | 3 | Chapter 41: Building Agentic and Graph RAG | [link](https://books.vizuara.ai/read/rag-in-production/building-agentic-and-graph-rag) |

## How to reproduce

```bash
# from the repo root
find . -name '*.py' | sort | while read f; do
  python -m py_compile "$f" || echo "COMPILE FAIL $f"
done
find . -name '*.py' | sort | xargs -n1 python -m pyflakes
```

Checked with Python 3.11.8 and pyflakes 3.4.0.

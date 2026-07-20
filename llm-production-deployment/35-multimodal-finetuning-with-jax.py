"""
LLM Production & Deployment
Chapter 35: Multimodal Finetuning using JAX
Section: Finetuning LLMs

Read this chapter: https://books.vizuara.ai/read/llm-production-deployment/multimodal-finetuning-with-jax

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo fixups: names the book uses but this chapter does not define ---
vision_encode = None  # TODO: the frozen vision encoder's forward pass.
splice = None         # TODO: splices image tokens into the text embeddings.
decoder = None        # TODO: the decoder forward pass (frozen base + LoRA).
optimizer = None      # TODO: an optax optimizer, e.g. optax.adamw(...).
# --- end fixups ---

# --- block 1 ---
import jax
import jax.numpy as jnp
import optax

# params_trainable = {"projector": ..., "lora_A": ..., "lora_B": ...}
# params_frozen    = {"vision": ..., "decoder_base": ...}   # never differentiated

def forward(params_trainable, params_frozen, batch):
    # 1. frozen vision encoder: pixels -> (B, 196, 1024) patch features
    feats = vision_encode(params_frozen["vision"], batch["pixels"])
    # 2. trainable projector: (B, 196, 1024) -> (B, 196, 2048) image tokens
    img_tokens = feats @ params_trainable["projector"]
    # 3. splice image tokens into the text-embedding sequence at <image>
    inputs = splice(batch["input_ids"], img_tokens, params_frozen, params_trainable)
    # 4. decoder (frozen base + LoRA delta) -> logits over the vocab
    logits = decoder(params_frozen["decoder_base"], params_trainable, inputs)
    return logits  # (B, seq_len, vocab)

def loss_fn(params_trainable, params_frozen, batch):
    logits = forward(params_trainable, params_frozen, batch)
    # cross-entropy, but labels == -100 are IGNORED (image + question positions)
    labels = batch["labels"]
    mask = (labels != -100)
    ce = optax.softmax_cross_entropy_with_integer_labels(logits, jnp.where(mask, labels, 0))
    return (ce * mask).sum() / mask.sum()

@jax.jit
def train_step(params_trainable, params_frozen, opt_state, batch):
    loss, grads = jax.value_and_grad(loss_fn)(params_trainable, params_frozen, batch)
    updates, opt_state = optimizer.update(grads, opt_state, params_trainable)
    params_trainable = optax.apply_updates(params_trainable, updates)
    return params_trainable, opt_state, loss

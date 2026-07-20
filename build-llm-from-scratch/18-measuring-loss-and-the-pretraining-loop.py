"""
Build Large Language Models (LLMs) from Scratch
Chapter 18: Measuring Loss and Coding the Pretraining Loop
Section: LLM Pretraining

Read this chapter: https://books.vizuara.ai/read/build-llm-from-scratch/measuring-loss-and-the-pretraining-loop

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# loss = -mean(log(P_model[true_token]  for each position))

# --- block 2 ---
import torch

# --- stubs (not book code) ---
# Block 2 is shown as a fragment: it assumes a forward pass has already run.
logits = None   # TODO: the model's output, e.g. logits = model(input_batch) - ch. 17
targets = None  # TODO: the shifted target token IDs from the DataLoader - ch. 13

# logits: (batch, seq_len, vocab_size)   targets: (batch, seq_len)
loss = torch.nn.functional.cross_entropy(
    logits.flatten(0, 1),   # (batch * seq_len, vocab_size)
    targets.flatten()       # (batch * seq_len,)
)

# --- block 3 ---
perplexity = torch.exp(loss)

# --- block 4 ---
def calc_loss_loader(data_loader, model, device, num_batches=None):
    total_loss = 0.0
    n = num_batches or len(data_loader)
    for i, (input_batch, target_batch) in enumerate(data_loader):
        if i >= n:
            break
        input_batch = input_batch.to(device)
        target_batch = target_batch.to(device)
        logits = model(input_batch)
        loss = torch.nn.functional.cross_entropy(
            logits.flatten(0, 1), target_batch.flatten()
        )
        total_loss += loss.item()
    return total_loss / n

# --- block 5 ---
def train_model_simple(model, train_loader, val_loader, optimizer,
                        device, num_epochs, eval_freq):
    train_losses, val_losses = [], []
    global_step = -1

    for epoch in range(num_epochs):
        model.train()                                   # dropout ON
        for input_batch, target_batch in train_loader:
            optimizer.zero_grad()                       # 4. reset last step's grads
            input_batch = input_batch.to(device)
            target_batch = target_batch.to(device)
            logits = model(input_batch)
            loss = torch.nn.functional.cross_entropy(
                logits.flatten(0, 1), target_batch.flatten()
            )                                           # 1. forward -> loss
            loss.backward()                             # 2. backward -> grads
            optimizer.step()                            # 3. update weights
            global_step += 1

            if global_step % eval_freq == 0:            # periodic check-in
                model.eval()
                with torch.no_grad():
                    tr = calc_loss_loader(train_loader, model, device, num_batches=5)
                    vl = calc_loss_loader(val_loader, model, device, num_batches=5)
                model.train()
                train_losses.append(tr)
                val_losses.append(vl)
                print(f"step {global_step:04d}  train {tr:.3f}  val {vl:.3f}")

    return train_losses, val_losses

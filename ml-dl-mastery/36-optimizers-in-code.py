"""
Machine Learning & Deep Learning Mastery
Chapter 36: Optimizers in Code
Section: Optimizers & Training

Read this chapter: https://books.vizuara.ai/read/ml-dl-mastery/optimizers-in-code

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import numpy as np

# --- block 1 ---
def f(x, y):
    return 10 * x**2 + y**2          # steep in x, gentle in y

def grad(x, y):
    return np.array([20 * x, 2 * y]) # ∂f/∂x = 20x,  ∂f/∂y = 2y

# --- block 2 ---
def gradient_descent(theta, eta=0.01, steps=200):
    path = [theta.copy()]
    for _ in range(steps):
        theta = theta - eta * grad(*theta)
        path.append(theta.copy())
    return np.array(path)

# --- block 3 ---
def momentum(theta, eta=0.01, beta=0.9, steps=200):
    v = np.zeros_like(theta)
    path = [theta.copy()]
    for _ in range(steps):
        v = beta * v + grad(*theta)
        theta = theta - eta * v
        path.append(theta.copy())
    return np.array(path)

# --- block 4 ---
def adagrad(theta, eta=0.1, eps=1e-8, steps=200):
    G = np.zeros_like(theta)
    path = [theta.copy()]
    for _ in range(steps):
        g = grad(*theta)
        G = G + g**2                       # accumulate squared gradients, forever
        theta = theta - eta * g / (np.sqrt(G) + eps)
        path.append(theta.copy())
    return np.array(path)

# --- block 5 ---
def rmsprop(theta, eta=0.01, rho=0.9, eps=1e-8, steps=200):
    v = np.zeros_like(theta)
    path = [theta.copy()]
    for _ in range(steps):
        g = grad(*theta)
        v = rho * v + (1 - rho) * g**2     # moving average, not a running sum
        theta = theta - eta * g / (np.sqrt(v) + eps)
        path.append(theta.copy())
    return np.array(path)

# --- block 6 ---
def adam(theta, eta=0.1, b1=0.9, b2=0.999, eps=1e-8, steps=200):
    m = np.zeros_like(theta)
    v = np.zeros_like(theta)
    path = [theta.copy()]
    for t in range(1, steps + 1):
        g = grad(*theta)
        m = b1 * m + (1 - b1) * g          # 1st moment (momentum)
        v = b2 * v + (1 - b2) * g**2       # 2nd moment (RMSProp)
        m_hat = m / (1 - b1**t)            # bias correction
        v_hat = v / (1 - b2**t)
        theta = theta - eta * m_hat / (np.sqrt(v_hat) + eps)
        path.append(theta.copy())
    return np.array(path)

# --- block 7 ---
theta0 = np.array([-1.0, 1.0])
for name, opt in [("GD", gradient_descent), ("Momentum", momentum),
                  ("AdaGrad", adagrad), ("RMSProp", rmsprop), ("Adam", adam)]:
    path = opt(theta0.copy())
    print(f"{name:9s} final = {path[-1].round(4)},  loss = {f(*path[-1]):.5f}")

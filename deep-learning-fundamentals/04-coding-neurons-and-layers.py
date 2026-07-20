"""
Deep Learning Fundamentals
Chapter 4: Coding neurons and layers
Section: Neural Network Architecture

Read this chapter: https://books.vizuara.ai/read/deep-learning-fundamentals/coding-neurons-and-layers

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
inputs  = [1.0, 2.0, 3.0]
weights = [0.2, 0.8, -0.5]
bias    = 2.0

output = (inputs[0]*weights[0] +
          inputs[1]*weights[1] +
          inputs[2]*weights[2] + bias)

print(output)   # 2.3

# --- block 2 ---
inputs  = [1.0, 2.0, 3.0]
weights = [0.2, 0.8, -0.5]
bias    = 2.0

output = 0.0
for x_i, w_i in zip(inputs, weights):
    output += x_i * w_i     # accumulate one product at a time
output += bias              # add the bias once, at the end

print(output)   # 2.3

# --- block 3 ---
inputs = [1.0, 2.0, 3.0, 2.5]      # note: 4 inputs this time

weights = [
    [ 0.2,  0.8, -0.5,  1.0],      # neuron 1's weights
    [ 0.5, -0.91, 0.26, -0.5],     # neuron 2's weights
    [-0.26, -0.27, 0.17, 0.87],    # neuron 3's weights
]
biases = [2.0, 3.0, 0.5]           # one bias per neuron

# --- block 4 ---
layer_outputs = []                              # will hold one number per neuron

for neuron_weights, neuron_bias in zip(weights, biases):
    output = 0.0
    for x_i, w_i in zip(inputs, neuron_weights):
        output += x_i * w_i                     # weighted sum for THIS neuron
    output += neuron_bias                        # its own bias
    layer_outputs.append(output)                 # stash the result

print(layer_outputs)

# --- block 5 ---
def dense_layer(inputs, weights, biases):
    """Compute one dense (fully-connected) layer, pure Python."""
    outputs = []
    for neuron_weights, neuron_bias in zip(weights, biases):
        total = 0.0
        for x_i, w_i in zip(inputs, neuron_weights):
            total += x_i * w_i
        total += neuron_bias
        outputs.append(total)
    return outputs

print(dense_layer(inputs, weights, biases))   # [4.8, 1.21, 2.385]

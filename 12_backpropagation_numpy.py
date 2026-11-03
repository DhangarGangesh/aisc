# Small 2-2-1 Backpropagation Neural Network (XOR)
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
Y = np.array([[0], [1], [1], [0]], dtype=float)

np.random.seed(1)
W1 = np.random.randn(2, 2)
W2 = np.random.randn(2, 1)
lr = 0.5

for epoch in range(10000):
    hidden = sigmoid(X @ W1)
    output = sigmoid(hidden @ W2)

    error = Y - output
    d_output = error * output * (1 - output)
    d_hidden = (d_output @ W2.T) * hidden * (1 - hidden)

    W2 += lr * hidden.T @ d_output
    W1 += lr * X.T @ d_hidden

print("Predictions:")
print(np.round(output, 3))

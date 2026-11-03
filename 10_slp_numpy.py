# Single Layer Perceptron for AND gate
import numpy as np

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
y = np.array([0, 0, 0, 1])
weights = np.zeros(2)
bias = 0.0
learning_rate = 0.1

for epoch in range(20):
    errors = 0
    for inputs, target in zip(X, y):
        output = 1 if np.dot(inputs, weights) + bias >= 0.5 else 0
        error = target - output
        weights += learning_rate * error * inputs
        bias += learning_rate * error
        errors += abs(error)
    if errors == 0:
        break

print("Weights:", weights)
print("Bias:", bias)
for inputs in X:
    output = 1 if np.dot(inputs, weights) + bias >= 0.5 else 0
    print(inputs.astype(int), "->", output)

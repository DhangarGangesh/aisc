# ADALINE using the LMS / Delta learning rule
import numpy as np

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
target = np.array([-1, -1, -1, 1], dtype=float)
weights = np.zeros(2)
bias = 0.0
learning_rate = 0.1

for epoch in range(20):
    for inputs, desired in zip(X, target):
        output = np.dot(inputs, weights) + bias  # linear output
        error = desired - output
        weights += learning_rate * error * inputs
        bias += learning_rate * error

print("Weights:", weights)
print("Bias:", bias)
print("Bipolar predictions:")
for inputs in X:
    output = np.dot(inputs, weights) + bias
    print(1 if output >= 0 else -1)

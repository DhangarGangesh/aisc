"""Kohonen Self-Organizing Map

DETAILED PRACTICAL VERSION
--------------------------
Purpose:
    Demonstrates the algorithm/concept named above using a small, reproducible
    teaching dataset. The code is intentionally written step-by-step so that
    each stage can be explained during a practical examination.

How to run:
    python3 20_kohonen_som.py

Dependencies:
    Check the import statements below. Programs using NumPy require:
        python3 -m pip install numpy

Practical notes:
    - Read the comments beside each important operation.
    - The sample data and test values are defined in the program.
    - Change those values to experiment with different inputs.
    - Outputs are demonstrations, not real-world production predictions.
"""

# Kohonen Self-Organizing Map (SOM) - tiny 1D example
# Install: pip install numpy
import numpy as np

data = np.array([[1, 1], [1, 2], [4, 4], [5, 4]], dtype=float)
np.random.seed(0)
weights = np.random.rand(2, 2) * 5  # 2 neurons, each has 2 weights

for epoch in range(100):
    for sample in data:
        winner = np.argmin(np.linalg.norm(weights - sample, axis=1))
        rate = 0.3 * (1 - epoch/100)
        weights[winner] += rate * (sample - weights[winner])

print("Trained SOM weights:")
print(np.round(weights, 2))
for sample in data:
    winner = np.argmin(np.linalg.norm(weights - sample, axis=1))
    print(sample, "-> neuron", winner)

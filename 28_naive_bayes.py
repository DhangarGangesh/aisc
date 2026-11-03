"""Gaussian Naive Bayes Classification

DETAILED PRACTICAL VERSION
--------------------------
Purpose:
    Demonstrates the algorithm/concept named above using a small, reproducible
    teaching dataset. The code is intentionally written step-by-step so that
    each stage can be explained during a practical examination.

How to run:
    python3 26_naive_bayes.py

Dependencies:
    Check the import statements below. Programs using NumPy require:
        python3 -m pip install numpy

Practical notes:
    - Read the comments beside each important operation.
    - The sample data and test values are defined in the program.
    - Change those values to experiment with different inputs.
    - Outputs are demonstrations, not real-world production predictions.
"""

# Gaussian Naive Bayes classifier (pure Python)
import math

X = [1, 2, 2, 5, 6, 7]       # Study hours
y = [0, 0, 0, 1, 1, 1]       # 0=Fail, 1=Pass
value = 5.5

scores = []

for cls in [0, 1]:
    data = [x for x, label in zip(X, y) if label == cls]
    mean = sum(data) / len(data)
    variance = sum((x-mean)**2 for x in data) / len(data) + 1e-6
    likelihood = math.exp(-((value-mean)**2)/(2*variance))
    likelihood /= math.sqrt(2*math.pi*variance)
    prior = len(data) / len(X)
    scores.append(likelihood * prior)

print("Prediction:", "Pass" if scores[1] > scores[0] else "Fail")

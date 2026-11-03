"""Supervised Learning / Decision-Tree Classification

DETAILED PRACTICAL VERSION
--------------------------
Purpose:
    Demonstrates the algorithm/concept named above using a small, reproducible
    teaching dataset. The code is intentionally written step-by-step so that
    each stage can be explained during a practical examination.

How to run:
    python3 02_supervised_learning.py

Dependencies:
    Check the import statements below. Programs using NumPy require:
        python3 -m pip install numpy

Practical notes:
    - Read the comments beside each important operation.
    - The sample data and test values are defined in the program.
    - Change those values to experiment with different inputs.
    - Outputs are demonstrations, not real-world production predictions.
"""

# Simple Decision Tree classifier (pure Python)
# Predict pass/fail from study hours

X = [1, 2, 3, 4, 5, 6]
y = [0, 0, 0, 1, 1, 1]  # 0=Fail, 1=Pass

best_split = None
best_error = len(y)

for split in X[:-1]:
    predictions = [1 if x > split else 0 for x in X]
    error = sum(pred != actual for pred, actual in zip(predictions, y))
    if error < best_error:
        best_split, best_error = split, error

hours = 5
prediction = 1 if hours > best_split else 0

print("Best split:", best_split)
print("Prediction:", "Pass" if prediction else "Fail")

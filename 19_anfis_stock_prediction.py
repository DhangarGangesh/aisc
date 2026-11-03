"""ANFIS-Style Stock Value Prediction (Synthetic Data)

DETAILED PRACTICAL VERSION
--------------------------
Purpose:
    Demonstrates the algorithm/concept named above using a small, reproducible
    teaching dataset. The code is intentionally written step-by-step so that
    each stage can be explained during a practical examination.

How to run:
    python3 12_anfis_stock_prediction.py

Dependencies:
    Check the import statements below. Programs using NumPy require:
        python3 -m pip install numpy

Practical notes:
    - Read the comments beside each important operation.
    - The sample data and test values are defined in the program.
    - Change those values to experiment with different inputs.
    - Outputs are demonstrations, not real-world production predictions.
"""

# ANFIS-style stock price prediction demo (synthetic data)
# Install: pip install numpy
import numpy as np

# Input: day number; Output: sample stock price
x = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([100, 102, 101, 105, 107], dtype=float)

m1 = np.exp(-((x-2)**2)/2)
m2 = np.exp(-((x-4)**2)/2)
w1, w2 = m1/(m1+m2), m2/(m1+m2)
A = np.column_stack((w1*x, w1, w2*x, w2))
p = np.linalg.lstsq(A, y, rcond=None)[0]

def predict(day):
    a, b = np.exp(-((day-2)**2)/2), np.exp(-((day-4)**2)/2)
    return (a*(p[0]*day+p[1]) + b*(p[2]*day+p[3]))/(a+b)

print("Predicted sample price for day 6:", round(predict(6), 2))

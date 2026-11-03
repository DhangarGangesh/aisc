"""ANFIS-Style Glucose Risk Score (Synthetic Teaching Data)

DETAILED PRACTICAL VERSION
--------------------------
Purpose:
    Demonstrates the algorithm/concept named above using a small, reproducible
    teaching dataset. The code is intentionally written step-by-step so that
    each stage can be explained during a practical examination.

How to run:
    python3 13_anfis_diabetes_prediction.py

Dependencies:
    Check the import statements below. Programs using NumPy require:
        python3 -m pip install numpy

Practical notes:
    - Read the comments beside each important operation.
    - The sample data and test values are defined in the program.
    - Change those values to experiment with different inputs.
    - Outputs are demonstrations, not real-world production predictions.
"""

# ANFIS-style diabetes risk demo (synthetic teaching data)
# Install: pip install numpy
import numpy as np

# Input: glucose level; Output: 0 = lower risk, 1 = higher risk
x = np.array([80, 95, 110, 130, 150], dtype=float)
y = np.array([0, 0, 0, 1, 1], dtype=float)

m1 = np.exp(-((x-90)**2)/500)
m2 = np.exp(-((x-140)**2)/500)
w1, w2 = m1/(m1+m2), m2/(m1+m2)
A = np.column_stack((w1*x, w1, w2*x, w2))
p = np.linalg.lstsq(A, y, rcond=None)[0]

def predict(glucose):
    a = np.exp(-((glucose-90)**2)/500)
    b = np.exp(-((glucose-140)**2)/500)
    score = (a*(p[0]*glucose+p[1]) + b*(p[2]*glucose+p[3]))/(a+b)
    return score

score = predict(125)
print("Model risk score:", round(float(score), 2))
print("Demo class:", "Higher risk" if score >= 0.5 else "Lower risk")
print("Educational demo only; not a medical diagnosis.")

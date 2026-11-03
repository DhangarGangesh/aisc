"""ANFIS-Style Air Quality Index Prediction

DETAILED PRACTICAL VERSION
--------------------------
Purpose:
    Demonstrates the algorithm/concept named above using a small, reproducible
    teaching dataset. The code is intentionally written step-by-step so that
    each stage can be explained during a practical examination.

How to run:
    python3 11_anfis_aqi_prediction.py

Dependencies:
    Check the import statements below. Programs using NumPy require:
        python3 -m pip install numpy

Practical notes:
    - Read the comments beside each important operation.
    - The sample data and test values are defined in the program.
    - Change those values to experiment with different inputs.
    - Outputs are demonstrations, not real-world production predictions.
"""

# ANFIS-style AQI prediction demo (small synthetic dataset)
# Install: pip install numpy
import numpy as np

# Input: pollution level; Output: AQI (sample teaching data)
x = np.array([10, 20, 30, 40, 50], dtype=float)
y = np.array([20, 40, 60, 80, 100], dtype=float)

# Two Gaussian fuzzy membership functions
m1 = np.exp(-((x - 20) ** 2) / 200)
m2 = np.exp(-((x - 40) ** 2) / 200)
w1, w2 = m1/(m1+m2), m2/(m1+m2)

# Sugeno consequent parameters learned by least squares
A = np.column_stack((w1*x, w1, w2*x, w2))
p = np.linalg.lstsq(A, y, rcond=None)[0]

def predict(value):
    a = np.exp(-((value-20)**2)/200)
    b = np.exp(-((value-40)**2)/200)
    f1, f2 = p[0]*value+p[1], p[2]*value+p[3]
    return (a*f1+b*f2)/(a+b)

print("Predicted AQI:", round(predict(35), 2))

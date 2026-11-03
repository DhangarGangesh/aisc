"""ANFIS-Style Traffic Flow Prediction

DETAILED PRACTICAL VERSION
--------------------------
Purpose:
    Demonstrates the algorithm/concept named above using a small, reproducible
    teaching dataset. The code is intentionally written step-by-step so that
    each stage can be explained during a practical examination.

How to run:
    python3 14_anfis_traffic_prediction.py

Dependencies:
    Check the import statements below. Programs using NumPy require:
        python3 -m pip install numpy

Practical notes:
    - Read the comments beside each important operation.
    - The sample data and test values are defined in the program.
    - Change those values to experiment with different inputs.
    - Outputs are demonstrations, not real-world production predictions.
"""

# ANFIS-style traffic flow prediction demo (synthetic data)
# Install: pip install numpy
import numpy as np

# Input: number of vehicles observed; Output: estimated traffic flow
x = np.array([10, 20, 30, 40, 50], dtype=float)
y = np.array([12, 24, 35, 47, 58], dtype=float)

m1 = np.exp(-((x-20)**2)/200)
m2 = np.exp(-((x-40)**2)/200)
w1, w2 = m1/(m1+m2), m2/(m1+m2)
A = np.column_stack((w1*x, w1, w2*x, w2))
p = np.linalg.lstsq(A, y, rcond=None)[0]

def predict(vehicles):
    a = np.exp(-((vehicles-20)**2)/200)
    b = np.exp(-((vehicles-40)**2)/200)
    return (a*(p[0]*vehicles+p[1]) + b*(p[2]*vehicles+p[3]))/(a+b)

print("Predicted traffic flow:", round(predict(35), 2))

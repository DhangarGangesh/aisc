"""Fuzzy Drone Tilt Stabilization

DETAILED PRACTICAL VERSION
--------------------------
Purpose:
    Demonstrates the algorithm/concept named above using a small, reproducible
    teaching dataset. The code is intentionally written step-by-step so that
    each stage can be explained during a practical examination.

How to run:
    python3 18_fuzzy_drone_stabilization.py

Dependencies:
    Check the import statements below. Programs using NumPy require:
        python3 -m pip install numpy

Practical notes:
    - Read the comments beside each important operation.
    - The sample data and test values are defined in the program.
    - Change those values to experiment with different inputs.
    - Outputs are demonstrations, not real-world production predictions.
"""

# Fuzzy-style drone stabilization using tilt angle
def triangle(x, a, b, c):
    if x <= a or x >= c: return 0
    if x == b: return 1
    return (x-a)/(b-a) if x < b else (c-x)/(c-b)

tilt = 12  # degrees; positive means tilted right
left = triangle(tilt, 0, 15, 30)
level = triangle(tilt, -5, 0, 5)
right = triangle(tilt, -30, -15, 0)

# Correction command: left tilt -> right correction; right tilt -> left correction
total = left + level + right
correction = (left*(-50) + level*0 + right*50)/total if total else 0
print("Drone tilt:", tilt, "degrees")
print("Motor correction:", round(correction, 1))

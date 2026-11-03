"""Fuzzy Dam Gate Controller

DETAILED PRACTICAL VERSION
--------------------------
Purpose:
    Demonstrates the algorithm/concept named above using a small, reproducible
    teaching dataset. The code is intentionally written step-by-step so that
    each stage can be explained during a practical examination.

How to run:
    python3 16_fuzzy_dam_water_level.py

Dependencies:
    Check the import statements below. Programs using NumPy require:
        python3 -m pip install numpy

Practical notes:
    - Read the comments beside each important operation.
    - The sample data and test values are defined in the program.
    - Change those values to experiment with different inputs.
    - Outputs are demonstrations, not real-world production predictions.
"""

# Fuzzy-style water dam gate controller
def triangle(x, a, b, c):
    if x <= a or x >= c: return 0
    if x == b: return 1
    return (x-a)/(b-a) if x < b else (c-x)/(c-b)

level = 85  # water level in percent
low = triangle(level, 0, 20, 45)
medium = triangle(level, 30, 50, 70)
high = triangle(level, 55, 80, 100)

# Gate opening: low=10%, medium=50%, high=100%
total = low + medium + high
opening = (low*10 + medium*50 + high*100)/total if total else 0
print("Water level:", level, "%")
print("Gate opening:", round(opening, 1), "%")

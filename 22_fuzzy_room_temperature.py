"""Fuzzy Room Temperature Controller

DETAILED PRACTICAL VERSION
--------------------------
Purpose:
    Demonstrates the algorithm/concept named above using a small, reproducible
    teaching dataset. The code is intentionally written step-by-step so that
    each stage can be explained during a practical examination.

How to run:
    python3 15_fuzzy_room_temperature.py

Dependencies:
    Check the import statements below. Programs using NumPy require:
        python3 -m pip install numpy

Practical notes:
    - Read the comments beside each important operation.
    - The sample data and test values are defined in the program.
    - Change those values to experiment with different inputs.
    - Outputs are demonstrations, not real-world production predictions.
"""

# Fuzzy-style room temperature controller (simple membership weighting)
def trimf(x, a, b, c):
    if x <= a or x >= c: return 0.0
    if x == b: return 1.0
    return (x-a)/(b-a) if x < b else (c-x)/(c-b)

temp = 30
cold = trimf(temp, 10, 18, 25)
comfortable = trimf(temp, 20, 25, 30)
hot = trimf(temp, 25, 35, 45)

# Output fan levels: 20%, 50%, 90%
weights = cold + comfortable + hot
speed = (cold*20 + comfortable*50 + hot*90)/weights if weights else 0
print("Temperature:", temp, "C")
print("Fan speed:", round(speed, 1), "%")

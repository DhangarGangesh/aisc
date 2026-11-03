"""Fuzzy Electric Vehicle Motor Controller

DETAILED PRACTICAL VERSION
--------------------------
Purpose:
    Demonstrates the algorithm/concept named above using a small, reproducible
    teaching dataset. The code is intentionally written step-by-step so that
    each stage can be explained during a practical examination.

How to run:
    python3 17_fuzzy_ev_speed.py

Dependencies:
    Check the import statements below. Programs using NumPy require:
        python3 -m pip install numpy

Practical notes:
    - Read the comments beside each important operation.
    - The sample data and test values are defined in the program.
    - Change those values to experiment with different inputs.
    - Outputs are demonstrations, not real-world production predictions.
"""

# Fuzzy-style electric vehicle speed controller
def triangle(x, a, b, c):
    if x <= a or x >= c: return 0
    if x == b: return 1
    return (x-a)/(b-a) if x < b else (c-x)/(c-b)

speed = 25       # km/h
accelerator = 70 # percent

slow = triangle(speed, 0, 0, 40) if speed == 0 else triangle(speed, 0, 15, 40)
medium = triangle(speed, 20, 45, 70)
fast = triangle(speed, 55, 80, 120)

# Simple rule weights for motor power
total = slow + medium + fast
power = (slow*90 + medium*60 + fast*30)/total if total else 0
power = power * accelerator / 100
print("Vehicle speed:", speed, "km/h")
print("Estimated motor power command:", round(power, 1), "%")

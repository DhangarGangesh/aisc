"""Fuzzy Set AND, OR and NOT Operations

DETAILED PRACTICAL VERSION
--------------------------
Purpose:
    Demonstrates the algorithm/concept named above using a small, reproducible
    teaching dataset. The code is intentionally written step-by-step so that
    each stage can be explained during a practical examination.

How to run:
    python3 04_fuzzy_logic_operations.py

Dependencies:
    Check the import statements below. Programs using NumPy require:
        python3 -m pip install numpy

Practical notes:
    - Read the comments beside each important operation.
    - The sample data and test values are defined in the program.
    - Change those values to experiment with different inputs.
    - Outputs are demonstrations, not real-world production predictions.
"""

# Fuzzy Logic Operations
# Membership values must be between 0 and 1.

A = 0.7
B = 0.4

# Standard fuzzy operations
fuzzy_and = min(A, B)
fuzzy_or = max(A, B)
fuzzy_not_A = 1 - A
fuzzy_not_B = 1 - B

print("Membership value A =", A)
print("Membership value B =", B)
print()
print("Fuzzy AND (A AND B) =", fuzzy_and)
print("Fuzzy OR  (A OR B)  =", fuzzy_or)
print("Fuzzy NOT A         =", fuzzy_not_A)
print("Fuzzy NOT B         =", fuzzy_not_B)

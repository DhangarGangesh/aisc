# Polynomial Regression: fit a quadratic curve
import numpy as np

x = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([1, 4, 9, 16, 25], dtype=float)

coefficients = np.polyfit(x, y, 2)
model = np.poly1d(coefficients)

print("Polynomial:", model)
print("Prediction for x=6:", model(6))

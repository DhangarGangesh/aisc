# Linear Regression: y = mx + c
import numpy as np

x = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([2, 4, 5, 4, 5], dtype=float)

# Find best-fit line using least squares
m, c = np.polyfit(x, y, 1)
print("Slope:", round(m, 2))
print("Intercept:", round(c, 2))
print("Prediction for x=6:", round(m * 6 + c, 2))

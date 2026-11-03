# Bidirectional Associative Memory (BAM)
import numpy as np

# Two associated bipolar pattern pairs
X = np.array([[1, -1], [-1, 1]])
Y = np.array([[1, 1, -1], [-1, -1, 1]])

# Hebbian weight matrix
W = X.T @ Y

# Recall Y from X, then X from Y
x = X[0]
y = np.where(x @ W >= 0, 1, -1)
x_recalled = np.where(y @ W.T >= 0, 1, -1)

print("Weight matrix:\n", W)
print("Input X:", x)
print("Recalled Y:", y)
print("Recalled X:", x_recalled)

# Simplified Sugeno ANFIS demonstration
# Two inputs, two Gaussian membership functions per input, four rules.
import numpy as np

X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]], dtype=float)
y = np.array([5, 8, 11, 14, 17], dtype=float)

# Fixed Gaussian membership function parameters
centres = [np.array([2.0, 5.0]), np.array([3.0, 6.0])]
sigma = 2.0

def membership(value, centre):
    return np.exp(-((value - centre) ** 2) / (2 * sigma ** 2))

# Build four rule firing strengths and Sugeno linear consequent inputs
rows = []
for x1, x2 in X:
    strengths = []
    for c1 in centres[0]:
        for c2 in centres[1]:
            strengths.append(membership(x1, c1) * membership(x2, c2))
    rows.append([w * v for w in strengths for v in [1, x1, x2]])

A = np.array(rows)
# Least-squares fit for consequent parameters
parameters = np.linalg.lstsq(A, y, rcond=None)[0]

def predict(x1, x2):
    strengths = []
    outputs = []
    index = 0
    for c1 in centres[0]:
        for c2 in centres[1]:
            w = membership(x1, c1) * membership(x2, c2)
            a, b, c = parameters[index:index + 3]
            strengths.append(w)
            outputs.append(a + b * x1 + c * x2)
            index += 3
    return np.dot(strengths, outputs) / sum(strengths)

print("Predictions:")
for x1, x2 in X:
    print((x1, x2), "->", round(predict(x1, x2), 2))

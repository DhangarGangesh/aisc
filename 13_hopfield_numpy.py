# Hopfield Network: store and recall one bipolar pattern
import numpy as np

pattern = np.array([1, -1, 1, -1])
n = len(pattern)

# Hebbian weight matrix; no self-connections
W = np.outer(pattern, pattern)
np.fill_diagonal(W, 0)

noisy = np.array([1, -1, -1, -1])
state = noisy.copy()

for _ in range(10):
    old_state = state.copy()
    for i in range(n):
        value = np.dot(W[i], state)
        state[i] = 1 if value >= 0 else -1
    if np.array_equal(state, old_state):
        break

print("Original:", pattern)
print("Noisy:   ", noisy)
print("Recalled:", state)

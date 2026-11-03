# Very small regression tree demo (one split)
# Splits data into two groups and predicts each group's mean.

data = [(1, 2), (2, 3), (3, 3), (4, 8), (5, 9), (6, 10)]
best_split, best_error = None, float("inf")

for split in range(1, 6):
    left = [y for x, y in data if x <= split]
    right = [y for x, y in data if x > split]
    prediction_left = sum(left) / len(left)
    prediction_right = sum(right) / len(right)
    error = sum((y - prediction_left) ** 2 for y in left)
    error += sum((y - prediction_right) ** 2 for y in right)

    if error < best_error:
        best_split, best_error = split, error

left = [y for x, y in data if x <= best_split]
right = [y for x, y in data if x > best_split]
print("Best split: x <=", best_split)
print("Left prediction:", sum(left) / len(left))
print("Right prediction:", sum(right) / len(right))

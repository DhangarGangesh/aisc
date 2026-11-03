# K-Nearest Neighbours (KNN) - no ML library
import math

train_x = [[1, 1], [2, 2], [6, 6], [7, 7]]
train_y = ["A", "A", "B", "B"]
test = [3, 3]
k = 3

distances = []
for point, label in zip(train_x, train_y):
    distance = math.sqrt(sum((a - b) ** 2 for a, b in zip(point, test)))
    distances.append((distance, label))

distances.sort()
nearest_labels = [label for distance, label in distances[:k]]
prediction = max(set(nearest_labels), key=nearest_labels.count)

print("Nearest neighbours:", nearest_labels)
print("Predicted class:", prediction)

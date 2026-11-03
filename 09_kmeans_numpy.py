# K-Means Clustering
import numpy as np

X = np.array([[1, 2], [1, 4], [2, 3], [8, 8], [9, 8], [8, 10]], dtype=float)
centroids = np.array([[1, 2], [8, 8]], dtype=float)

for iteration in range(10):
    distances = np.linalg.norm(X[:, None] - centroids, axis=2)
    labels = np.argmin(distances, axis=1)

    new_centroids = np.array([
        X[labels == i].mean(axis=0) for i in range(len(centroids))
    ])
    if np.allclose(centroids, new_centroids):
        break
    centroids = new_centroids

print("Cluster labels:", labels)
print("Final centroids:\n", centroids)

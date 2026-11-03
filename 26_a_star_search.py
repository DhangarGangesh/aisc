"""A-Star Search on a Grid

DETAILED PRACTICAL VERSION
--------------------------
Purpose:
    Demonstrates the algorithm/concept named above using a small, reproducible
    teaching dataset. The code is intentionally written step-by-step so that
    each stage can be explained during a practical examination.

How to run:
    python3 19_a_star_search.py

Dependencies:
    Check the import statements below. Programs using NumPy require:
        python3 -m pip install numpy

Practical notes:
    - Read the comments beside each important operation.
    - The sample data and test values are defined in the program.
    - Change those values to experiment with different inputs.
    - Outputs are demonstrations, not real-world production predictions.
"""

# A* Search on a small grid
import heapq

grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]
start, goal = (0, 0), (3, 3)

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

pq = [(heuristic(start, goal), 0, start)]
parent = {start: None}
cost = {start: 0}

while pq:
    _, g, current = heapq.heappop(pq)
    if current == goal:
        break
    r, c = current
    for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
        nxt = (r+dr, c+dc)
        nr, nc = nxt
        if 0 <= nr < 4 and 0 <= nc < 4 and grid[nr][nc] == 0:
            new_g = g + 1
            if new_g < cost.get(nxt, float("inf")):
                cost[nxt] = new_g
                parent[nxt] = current
                heapq.heappush(pq, (new_g + heuristic(nxt, goal), new_g, nxt))

if goal in parent:
    path, node = [], goal
    while node is not None:
        path.append(node)
        node = parent[node]
    print("Path:", list(reversed(path)))
    print("Path cost:", cost[goal])
else:
    print("No path found")

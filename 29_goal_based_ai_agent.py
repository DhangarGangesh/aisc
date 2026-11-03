"""Goal-Based Grid Navigation Agent

DETAILED PRACTICAL VERSION
--------------------------
Purpose:
    Demonstrates the algorithm/concept named above using a small, reproducible
    teaching dataset. The code is intentionally written step-by-step so that
    each stage can be explained during a practical examination.

How to run:
    python3 03_goal_based_ai_agent.py

Dependencies:
    Check the import statements below. Programs using NumPy require:
        python3 -m pip install numpy

Practical notes:
    - Read the comments beside each important operation.
    - The sample data and test values are defined in the program.
    - Change those values to experiment with different inputs.
    - Outputs are demonstrations, not real-world production predictions.
"""

from collections import deque

# A small grid: 0 = free cell, 1 = obstacle
grid = [
    [0, 0, 0, 1],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

start = (0, 0)
goal = (3, 3)

def find_goal_path(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start, [start])])
    visited = {start}
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        (r, c), path = queue.popleft()

        # Goal-based agent checks whether the goal has been reached
        if (r, c) == goal:
            return path

        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols
                    and grid[nr][nc] == 0 and (nr, nc) not in visited):
                visited.add((nr, nc))
                queue.append(((nr, nc), path + [(nr, nc)]))

    return None

print("Start:", start)
print("Goal:", goal)
path = find_goal_path(grid, start, goal)

if path:
    print("Goal reached!")
    print("Path:", path)
    print("Number of moves:", len(path) - 1)
else:
    print("Goal cannot be reached.")

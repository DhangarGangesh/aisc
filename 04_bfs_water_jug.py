# Water Jug Problem using BFS
# Jug capacities: 4 litres and 3 litres
# Goal: get exactly 2 litres in either jug

from collections import deque

capacity1, capacity2 = 4, 3
start = (0, 0)
queue = deque([(start, [])])
visited = {start}

while queue:
    (a, b), path = queue.popleft()
    path = path + [(a, b)]

    if a == 2 or b == 2:
        print("Steps:")
        for state in path:
            print(state)
        break

    # Possible operations
    transfer = min(a, capacity2 - b)
    states = [
        (capacity1, b), (a, capacity2), (0, b), (a, 0),
        (a - transfer, b + transfer),
        (a + min(b, capacity1 - a), b - min(b, capacity1 - a))
    ]

    for state in states:
        if state not in visited:
            visited.add(state)
            queue.append((state, path))

# Breadth First Search (BFS) using a queue

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [], "E": [], "F": []
}

def bfs(start):
    queue = [start]
    visited = [start]

    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

bfs("A")

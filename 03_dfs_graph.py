# Depth First Search (DFS) using recursion

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [], "E": [], "F": []
}

visited = []

def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        for neighbour in graph[node]:
            dfs(neighbour)

dfs("A")

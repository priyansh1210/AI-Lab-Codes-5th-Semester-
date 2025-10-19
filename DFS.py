def dfs(graph, start, visited=None):
    if visited is None: visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

graph = {}
n = int(input("Enter number of nodes: "))
for _ in range(n):
    node = input("Node: ")
    neighbors = input(f"Neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors
start = input("Start node: ")
dfs(graph, start)
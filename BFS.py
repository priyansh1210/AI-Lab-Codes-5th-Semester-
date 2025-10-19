from collections import deque
def bfs(graph, start):
    visited, queue = set(), deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend(graph[node])

graph = {}
n = int(input("Enter number of nodes: "))
for _ in range(n):
    node = input("Node: ")
    neighbors = input(f"Neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors
start = input("Start node: ")
bfs(graph, start)
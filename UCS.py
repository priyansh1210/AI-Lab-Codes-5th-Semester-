import heapq
def ucs(graph, start, goal):
    queue = [(0, start)]
    visited = set()
    while queue:
        cost, node = heapq.heappop(queue)
        if node == goal:
            print(f"Reached {goal} with cost {cost}")
            return
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph[node]:
                heapq.heappush(queue, (cost + weight, neighbor))

graph = {}
n = int(input("Enter number of nodes: "))
for _ in range(n):
    node = input("Node: ")
    edges = input(f"Edges from {node} (format: neighbor:cost): ").split()
    graph[node] = [(e.split(':')[0], int(e.split(':')[1])) for e in edges]
start = input("Start node: ")
goal = input("Goal node: ")
ucs(graph, start, goal)
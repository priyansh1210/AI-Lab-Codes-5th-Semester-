import heapq
def astar(graph, start, goal, h):
    queue = [(h[start], 0, start)]
    visited = set()
    while queue:
        f, cost, node = heapq.heappop(queue)
        if node == goal:
            print(f"Reached {goal} with cost {cost}")
            return
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph[node]:
                heapq.heappush(queue, (cost + weight + h[neighbor], cost + weight, neighbor))

graph, h = {}, {}
n = int(input("Enter number of nodes: "))
for _ in range(n):
    node = input("Node: ")
    edges = input(f"Edges from {node} (neighbor:cost): ").split()
    graph[node] = [(e.split(':')[0], int(e.split(':')[1])) for e in edges]
    h[node] = int(input(f"Heuristic for {node}: "))
start = input("Start node: ")
goal = input("Goal node: ")
astar(graph, start, goal, h)
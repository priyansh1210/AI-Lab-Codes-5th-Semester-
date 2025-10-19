import heapq

def best_first_search(graph, heuristics, start, goal):
    visited = set()
    queue = [(heuristics[start], start)]
    
    while queue:
        h, node = heapq.heappop(queue)
        if node in visited:
            continue
        print(f"Visited: {node}")
        visited.add(node)
        if node == goal:
            print(f"Reached goal: {goal}")
            return
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(queue, (heuristics[neighbor], neighbor))
    print("Goal not reachable.")

# 🔢 User Input
graph = {}
heuristics = {}

n = int(input("Enter number of nodes: "))
for _ in range(n):
    node = input("Node name: ")
    neighbors = input(f"Neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors
    h = int(input(f"Heuristic value for {node}: "))
    heuristics[node] = h

start = input("Enter start node: ")
goal = input("Enter goal node: ")

best_first_search(graph, heuristics, start, goal)
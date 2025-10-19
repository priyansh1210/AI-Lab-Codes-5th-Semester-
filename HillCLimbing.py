def hill_climb(values, start):
    current = start
    while True:
        neighbors = [current - 1, current + 1]
        next_node = max(neighbors, key=lambda x: values.get(x, -float('inf')))
        if values.get(next_node, -float('inf')) <= values[current]:
            print(f"Reached peak at {current} with value {values[current]}")
            break
        current = next_node

values = {}
n = int(input("Enter number of points: "))
for _ in range(n):
    x, v = map(int, input("Point and value: ").split())
    values[x] = v
start = int(input("Start point: "))
hill_climb(values, start)
from collections import deque

def is_valid(m, c):
    return 0 <= m <= total_m and 0 <= c <= total_c and (m == 0 or m >= c)

def get_successors(state):
    m, c, boat = state
    moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
    successors = []
    for dm, dc in moves:
        if boat == 1:  # Boat on left
            new = (m - dm, c - dc, 0)
        else:          # Boat on right
            new = (m + dm, c + dc, 1)
        if is_valid(new[0], new[1]) and is_valid(total_m - new[0], total_c - new[1]):
            successors.append(new)
    return successors

def solve():
    visited = set()
    queue = deque([((total_m, total_c, 1), [])])
    while queue:
        state, path = queue.popleft()
        if state in visited: continue
        visited.add(state)
        path = path + [state]
        if state == (0, 0, 0):
            print("\nSolution path:")
            for s in path:
                print(f"Left: M={s[0]} C={s[1]} | Right: M={total_m - s[0]} C={total_c - s[1]} | Boat: {'Left' if s[2] else 'Right'}")
            return
        for succ in get_successors(state):
            queue.append((succ, path))
    print("No solution found.")

# 🔢 User Input
total_m = int(input("Enter number of missionaries: "))
total_c = int(input("Enter number of cannibals: "))
solve()
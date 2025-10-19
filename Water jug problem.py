def water_jug(cap1, cap2, target):
    visited = set()
    stack = [(0, 0)]
    while stack:
        a, b = stack.pop()
        if (a, b) in visited: continue
        visited.add((a, b))
        print(f"Jug1: {a}, Jug2: {b}")
        if a == target or b == target: return
        stack.extend([
            (cap1, b), (a, cap2), (0, b), (a, 0),
            (min(a + b, cap1), max(0, a + b - cap1)),
            (max(0, a + b - cap2), min(a + b, cap2))
        ])

cap1 = int(input("Capacity of Jug1: "))
cap2 = int(input("Capacity of Jug2: "))
target = int(input("Target amount: "))
water_jug(cap1, cap2, target)
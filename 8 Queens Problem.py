def is_safe(board, row, col):
    for i in range(row):
        # Same column or diagonal check
        if board[i] == col or abs(board[i] - col) == row - i:
            return False
    return True

def solve_n_queens(n):
    def solve(row, board):
        if row == n:
            return board
        for col in range(n):
            if is_safe(board, row, col):
                result = solve(row + 1, board + [col])
                if result:
                    return result
        return None

    solution = solve(0, [])
    if solution:
        print(f"\n✅ One valid {n}×{n} board solution:")
        for r in range(n):
            row = ['.'] * n
            row[solution[r]] = 'Q'
            print(' '.join(row))
    else:
        print("❌ No solution found.")

# 🔢 Always square board (rows = cols = n)
try:
    n = int(input("Enter board size (default 8): ") or "8")
    if n < 1:
        print("Board size must be at least 1.")
    else:
        solve_n_queens(n)
except ValueError:
    print("Please enter a valid number.")

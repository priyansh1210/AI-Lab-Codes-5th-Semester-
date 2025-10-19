from itertools import permutations
import re

def solve_cryptarithmetic(puzzle):
    # Extract words and operator
    match = re.match(r'([A-Z+ ]+)=([A-Z]+)', puzzle.replace(' ', ''))
    if not match:
        print("Invalid format. Use format like 'SEND + MORE = MONEY'")
        return

    left_expr, result = match.groups()
    words = re.findall(r'[A-Z]+', left_expr) + [result]
    unique_letters = sorted(set(''.join(words)))

    if len(unique_letters) > 10:
        print("Too many unique letters (max 10).")
        return

    for perm in permutations(range(10), len(unique_letters)):
        letter_map = dict(zip(unique_letters, perm))
        if any(letter_map[word[0]] == 0 for word in words):  # No leading zero
            continue

        def word_value(word):
            return int(''.join(str(letter_map[c]) for c in word))

        left_sum = sum(word_value(w) for w in re.findall(r'[A-Z]+', left_expr))
        right_val = word_value(result)

        if left_sum == right_val:
            print("\nSolution found:")
            for k, v in letter_map.items():
                print(f"{k} = {v}")
            print(f"{left_expr} = {result}")
            print(f"{left_sum} = {right_val}")
            return

    print("No solution found.")


puzzle = input("Enter cryptarithmetic puzzle (e.g., SEND + MORE = MONEY): ").upper()
solve_cryptarithmetic(puzzle)
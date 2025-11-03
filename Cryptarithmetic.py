import itertools
def solve_crypto(word1, word2, result):
    letters = set(word1) | set(word2) | set(result)
    if len(letters) > 10:
        print("❌ Invalid puzzle: More than 10 unique letters.")
        return
    sorted_letters = tuple(letters)
    digits = range(10)
    for perm in itertools.permutations(digits, len(sorted_letters)):
        mapping = dict(zip(sorted_letters, perm))
        if mapping[word1[0]] == 0 or mapping[word2[0]] == 0 or mapping[result[0]] == 0:
            continue
        num1 = int("".join(str(mapping[c]) for c in word1))
        num2 = int("".join(str(mapping[c]) for c in word2))
        num_res = int("".join(str(mapping[c]) for c in result))
        if num1 + num2 == num_res:
            print("\n✅ Solution found!")
            print(f"  {word1}: {num1}")
            print(f"+ {word2}: {num2}")
            print(f"= {result}: {num_res}")
            print(f"\nMapping: {mapping}")
            return
    print("❌ No solution found.")
if __name__ == "__main__":
    print("🔢 Cryptarithmetic Puzzle Solver")
    w1 = input("Enter first word: ").strip().upper()
    w2 = input("Enter second word: ").strip().upper()
    res = input("Enter result word: ").strip().upper()
    solve_crypto(w1, w2, res)

def distinct_permutations(n: int, k: int) -> int:
    permutation_count = 1
    for i in range(k):
        permutation_count *= n - i
    return permutation_count

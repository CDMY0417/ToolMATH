def count_permutations_c(n: int, k: int) -> int:
    if k > n:
        return 0
    permutations = 1
    for i in range(n, n-k, -1):
        permutations *= i
    return permutations

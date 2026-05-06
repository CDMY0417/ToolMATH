def count_permutations_e(n: int, k: int) -> int:
    if k > n: return 0
    result = 1
    for i in range(n, n-k, -1):
        result *= i
    return result

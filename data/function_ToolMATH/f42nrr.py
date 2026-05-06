def count_permutations_a(n: int, k: int) -> int:
    if k > n:
        return 0
    result = 1
    for i in range(n, n-k, -1):
        result *= i
    return result

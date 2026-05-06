def factorial_permutation(n: int, k: int) -> int:
    result = 1
    for i in range(n, n-k, -1):
        result *= i
    return result

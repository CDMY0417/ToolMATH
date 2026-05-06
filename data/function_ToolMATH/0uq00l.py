def simplify_factorial_ratio(n: int, k: int) -> int:
    if k > n:
        return 1
    result = 1
    for i in range(k + 1, n + 1):
        result *= i
    return result

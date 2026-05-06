def factorial_quotient(n: int, k: int) -> int:
    result = 1
    for i in range(k + 1, n + 1):
        result *= i
    return result

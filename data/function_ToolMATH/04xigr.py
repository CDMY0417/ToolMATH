def factorial_division(n: int, k: int) -> int:
    k = min(k, n - k)
    numerator = 1
    denominator = 1
    for i in range(1, k + 1):
        numerator *= n - i + 1
        denominator *= i
    return numerator // denominator

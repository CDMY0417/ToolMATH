def factorial_division_simplify(n: int, k: int) -> int:
    numerator = 1
    denominator = 1
    for i in range(n, k, -1):
        numerator *= i
    for i in range(n-k, 0, -1):
        denominator *= i
    return numerator // denominator

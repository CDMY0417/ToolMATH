def binomial_coefficient_b(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    numerator = 1
    denominator = 1
    k = min(k, n - k)
    for i in range(k):
        numerator *= n - i
        denominator *= i + 1
    return numerator // denominator

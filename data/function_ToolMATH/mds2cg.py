def binomial_coefficient_bi(n: int, k: int) -> int:
    if k > n:
        return 0
    k = min(k, n - k)
    numerator = 1
    denominator = 1
    for i in range(1, k + 1):
        numerator *= n
        denominator *= i
        n -= 1
    return numerator // denominator

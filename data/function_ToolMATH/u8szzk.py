def binomial_coefficient_bz(n: int, k: int) -> int:
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator *= (n - i)
        denominator *= (i + 1)
    return numerator // denominator

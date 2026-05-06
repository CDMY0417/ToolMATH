def binomial_coefficient_bc(n: int, k: int) -> int:
    if k > n - k:
        k = n - k
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator *= (n - i)
        denominator *= (i + 1)
    return numerator // denominator

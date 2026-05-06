def binomial_coefficient_k(n: int, k: int) -> int:
    if k > n:
        return 0
    if k < 0 or n < 0:
        return 0
    coeff = 1
    for i in range(min(k, n - k)):
        coeff = coeff * (n - i) // (i + 1)
    return coeff

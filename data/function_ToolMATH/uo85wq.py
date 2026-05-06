def binomial_coefficient_ca(n: int, k: int) -> int:
    if k > n:
        return 0
    k = min(k, n - k)
    coeff = 1
    for i in range(1, k + 1):
        coeff = coeff * (n - i + 1) // i
    return coeff

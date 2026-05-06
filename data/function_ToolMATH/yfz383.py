def binomial_coefficient_ea(n: int, k: int) -> int:
    if k > n:
        return 0
    if k < 0:
        return 0
    if k > n - k:
        k = n - k
    coeff = 1
    for i in range(k):
        coeff = coeff * (n - i) // (i + 1)
    return coeff

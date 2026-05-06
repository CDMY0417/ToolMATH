def binomial_coefficient_cw(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)
    coeff = 1
    for i in range(k):
        coeff = coeff * (n - i) // (i + 1)
    return coeff

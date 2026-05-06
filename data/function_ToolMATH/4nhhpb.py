def binomial_coefficient_ed(n: int, k: int):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)
    num = 1
    den = 1
    for i in range(k):
        num *= (n - i)
        den *= (i + 1)
    return num // den

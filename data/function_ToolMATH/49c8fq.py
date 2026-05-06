def binomial_coefficient_g(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)  # Take advantage of symmetry
    c = 1
    for i in range(k):
        c = c * (n - i) // (i + 1)
    return c

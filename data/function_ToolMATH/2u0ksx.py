def binomial_coefficient_cv(n: int, k: int) -> int:
    if k > n - k:  # Take advantage of symmetry
        k = n - k
    c = 1
    for i in range(k):
        c = c * (n - i) // (i + 1)
    return c

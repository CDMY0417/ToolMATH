def binomial_coefficient_x(n: int, k: int) -> int:
    if k > n:
        return 0
    k = min(k, n - k)
    c = 1
    for i in range(k):
        c = c * (n - i) // (i + 1)
    return c

def binomial_coefficient_co(n: int, k: int) -> int:
    if k > n:
        return 0
    if k == 0 or n == k:
        return 1
    k = min(k, n - k)
    c = 1
    for i in range(k):
        c = c * (n - i) // (i + 1)
    return c

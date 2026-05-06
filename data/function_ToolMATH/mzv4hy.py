def combinations_t(n: int, k: int) -> int:
    from math import prod
    k = min(k, n-k)
    numerator = prod(range(n, n-k, -1))
    denominator = prod(range(1, k+1))
    return numerator // denominator

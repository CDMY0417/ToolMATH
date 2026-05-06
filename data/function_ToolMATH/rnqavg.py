def combinations_count_u(n: int, k: int) -> int:
    if k > n:
        return 0
    from math import comb
    return comb(n, k)

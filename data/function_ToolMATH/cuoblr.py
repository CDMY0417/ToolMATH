def ways_to_partition(n: int, k: int) -> int:
    from math import comb
    return comb(n + k - 1, k - 1)

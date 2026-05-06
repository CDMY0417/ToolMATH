def sum_combinations(n: int, start: int, end: int) -> int:
    from math import comb
    return sum(comb(n, k) for k in range(start, end + 1))

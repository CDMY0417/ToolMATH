def count_solutions_stars_and_bars(n: int, k: int) -> int:
    from math import comb
    return comb(n + k - 1, k)

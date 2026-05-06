def count_integer_solutions(n: int, total: int):
    from math import comb
    return comb(n + total - 1, n - 1)

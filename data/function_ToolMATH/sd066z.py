def expand_binomial_power(a: int, b: int, n: int):
    from math import comb
    return sum(comb(n, k) * (a ** (n - k)) * (b ** k) for k in range(n + 1))

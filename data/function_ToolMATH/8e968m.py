def binomial_theorem_expansion(a: int, b: int, n: int):
    from math import comb
    return [(comb(n, k) * (a**(n-k)) * (b**k)) for k in range(n + 1)]

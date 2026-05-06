def binomial_expansion_coefficient(n: int, k: int, a: float) -> float:
    from math import comb
    return comb(n, k) * a**(n-k) * (-1)**k

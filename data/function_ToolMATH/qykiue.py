def binomial_probability(k: int, n: int, p: float) -> float:
    from math import comb
    q = 1 - p
    return comb(k, n) * (p ** n) * (q ** (k - n))

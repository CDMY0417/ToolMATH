def event_probability(n: int, x: int, p: float) -> float:
    from math import comb
    return comb(n, x) * (p ** x) * ((1 - p) ** (n - x))

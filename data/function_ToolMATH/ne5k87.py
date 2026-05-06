def flip_coin_probability(n: int, k: int) -> float:
    from math import comb
    return comb(n, k) * (0.5 ** n)

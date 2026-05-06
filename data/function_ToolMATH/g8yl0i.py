def heads_probability(n: int) -> list:
    from math import comb
    probabilities = [comb(n, k) / (2**n) for k in range(n+1)]
    return probabilities

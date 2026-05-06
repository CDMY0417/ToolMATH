from math import comb

def expansion_coefficients(n: int) -> list:
    return [comb(n, k) for k in range(n + 1)]

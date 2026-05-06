def am_gm_inequality_f(terms: list[float]) -> tuple:
    from math import prod
    n = len(terms)
    am = sum(terms) / n
    gm = prod(terms) ** (1 / n)
    return am, gm

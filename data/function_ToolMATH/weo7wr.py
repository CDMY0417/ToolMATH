def probability_exact_k_given_event(n: int, k: int, p: float):
    from math import comb
    q = 1 - p
    return comb(n, k) * (p ** k) * (q ** (n - k))

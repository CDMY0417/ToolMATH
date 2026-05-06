def ways_to_choose_k_from_n(n: int, k: int):
    from math import comb
    return comb(n, k)

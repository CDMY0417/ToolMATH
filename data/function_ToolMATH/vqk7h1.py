def count_balanced_sequences(n: int):
    from math import comb
    return comb(n, n // 2)

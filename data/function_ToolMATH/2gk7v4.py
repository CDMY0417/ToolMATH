def total_number_of_games(n: int) -> int:
    from math import comb
    return comb(n, 2)

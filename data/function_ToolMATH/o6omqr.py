from math import comb

def combinations_with_replacement(choose_count: int, set_size: int):
    return comb(set_size + choose_count - 1, choose_count)

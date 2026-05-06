def choose_distinct_letters(set_size: int, number_to_choose: int):
    from math import comb
    return comb(set_size, number_to_choose)

def choose_positions_for_repeated_letters(slots: int, positions_to_fill: int):
    from math import comb
    return comb(slots, positions_to_fill)

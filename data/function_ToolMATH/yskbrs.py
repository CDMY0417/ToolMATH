def half_of_mixed_number(whole: int, numerator: int, denominator: int):
    whole_half = whole / 2
    frac_half = (numerator / denominator) / 2
    mixed_number = whole_half + frac_half
    whole_part = int(mixed_number)
    fractional_part = mixed_number - whole_part
    return whole_part, fractional_part * denominator, denominator

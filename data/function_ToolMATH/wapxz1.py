def convert_to_mixed_number_c(numerator: int, denominator: int):
    whole = numerator // denominator
    remainder = numerator % denominator
    return whole, remainder, denominator

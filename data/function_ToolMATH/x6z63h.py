def convert_to_mixed_number_b(numerator: int, denominator: int):
    whole = numerator // denominator
    fractional = numerator % denominator
    return whole, fractional, denominator

def convert_to_mixed_number_a(numerator: int, denominator: int) -> tuple:
    whole_part = numerator // denominator
    fractional_part = numerator % denominator
    return whole_part, fractional_part, denominator

def convert_improper_to_mixed_number(numerator: int, denominator: int) -> tuple:
    whole = numerator // denominator
    new_numerator = numerator % denominator
    return (whole, new_numerator, denominator)

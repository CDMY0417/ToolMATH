def improper_fraction_to_mixed_number(numerator: int, denominator: int) -> tuple:
    whole_number = numerator // denominator
    remainder = numerator % denominator
    return (whole_number, remainder, denominator)

def mixed_number_to_improper_fraction_a(whole_number: int, numerator: int, denominator: int) -> tuple:
    new_numerator = whole_number * denominator + numerator
    return new_numerator, denominator

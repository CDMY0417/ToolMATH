def mixed_number_to_improper_fraction(whole_number: int, numerator: int, denominator: int) -> tuple:
    improper_numerator = whole_number * denominator + numerator
    return (improper_numerator, denominator)

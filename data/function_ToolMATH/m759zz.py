def convert_mixed_to_improper_fraction(whole: int, numerator: int, denominator: int) -> tuple:
    improper_numerator = whole * denominator + numerator
    return (improper_numerator, denominator)

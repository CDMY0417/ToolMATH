def mixed_to_improper_fraction_a(whole: int, numerator: int, denominator: int) -> tuple[int, int]:
    improper_numerator = whole * denominator + numerator
    return (improper_numerator, denominator)

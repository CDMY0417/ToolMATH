def fraction_to_improper(whole: int, numerator: int, denominator: int) -> tuple[int, int]:
    return whole * denominator + numerator, denominator

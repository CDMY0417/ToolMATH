def simplify_exponent_b(base: float, numerator_exponent: float, denominator_exponent: float) -> float:
    return base ** (numerator_exponent - denominator_exponent)
